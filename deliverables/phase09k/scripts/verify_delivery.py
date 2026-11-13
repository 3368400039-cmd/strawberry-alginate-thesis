"""Compare the finished document to frozen inputs; no statistical recalculation."""
from copy import deepcopy
from pathlib import Path
import csv
import hashlib
import json
import re
import zipfile

import fitz
from lxml import etree
from docx import Document
from docx.oxml.ns import qn

R = Path(__file__).resolve().parents[3]
O = R / 'deliverables/phase09k'
J = R / 'deliverables/phase09j'
S = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load(p):
    return json.loads(p.read_text(encoding='utf-8'))


def cells_from_selected_sheets(path, selected):
    """Open only named worksheet XML. Never open auxiliary sheet 18."""
    out = {}
    with zipfile.ZipFile(path) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(c.itertext()) for c in etree.fromstring(z.read('xl/sharedStrings.xml'))]
        rels = {e.get('Id'): e.get('Target') for e in etree.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        wb = etree.fromstring(z.read('xl/workbook.xml'))
        for sh in wb.findall('s:sheets/s:sheet', S):
            name = sh.get('name')
            if name not in selected:
                continue
            target = rels[sh.get(qn('r:id'))].lstrip('/')
            target = target if target.startswith('xl/') else 'xl/' + target
            for c in etree.fromstring(z.read(target)).findall('.//s:c', S):
                if c.find('s:f', S) is not None:
                    continue
                v, inline = c.find('s:v', S), c.find('s:is', S)
                value = strings[int(v.text)] if c.get('t') == 's' and v is not None else ''.join(inline.itertext()) if inline is not None else v.text if v is not None else None
                out[(name, c.get('r'))] = value
    return out


def main():
    protected = load(O / 'evidence/输入文件SHA-256.json')
    assert len(protected) == 287
    for name, h in protected.items():
        assert sha(R / name) == h, name
    assert sha(R / '实验记录.xlsx') == 'a63c8b0e1a07724e861d4b9a379ab632b3c0d41038f77310db36fb3b6b9f66f6'

    old, new = Document(J / '最终初稿.docx'), Document(O / '本科毕业论文_完整初稿.docx')
    edits = load(O / 'evidence/局部修订记录.json')
    actual = [p.text for p in new.paragraphs if p.style.name != 'I TOC']
    expected = [p.text for p in old.paragraphs if p.style.name != 'I TOC' and not p.text.startswith('续表3-1')]
    for x in edits['text_changes']:
        i = expected.index(x['before'])
        expected[i] = x['after']
    for label, value in edits['cover_values'].items():
        i = expected.index(label + '____________')
        expected[i] = label + value
    expected[expected.index('______年____月')] = '二〇二七年六月'
    expected += edits['acknowledgements']
    assert actual == expected, 'Unapproved paragraph change'
    assert len(edits['text_changes']) == 9
    for label, value in edits['cover_values'].items():
        assert label + value in actual
    assert '二级学院：____________' in actual
    assert '二〇二七年六月' in actual
    assert sum('毕业论文作者签名：____________' in p.text for p in new.paragraphs) == 2

    old_tables = [[[c.text for c in row.cells] for row in t.rows] for t in old.tables]
    new_tables = [[[c.text for c in row.cells] for row in t.rows] for t in new.tables]
    assert len(old_tables) == 6 and len(new_tables) == 5
    assert new_tables[0:2] == old_tables[0:2]
    assert new_tables[2][1:] == old_tables[2][1:] + old_tables[3][1:]
    assert new_tables[3:] == old_tables[4:]
    assert new.tables[2].rows[0]._tr.xpath('./w:trPr/w:tblHeader')
    assert all(row._tr.xpath('./w:trPr/w:cantSplit') for row in new.tables[2].rows)
    assert [etree.tostring(e) for e in old.element.xpath('.//m:oMath')] == [etree.tostring(e) for e in new.element.xpath('.//m:oMath')]
    with zipfile.ZipFile(J / '最终初稿.docx') as a, zipfile.ZipFile(O / '本科毕业论文_完整初稿.docx') as b:
        changed_parts = [name for name in a.namelist() if a.read(name) != b.read(name)]
    assert set(changed_parts) == {'word/document.xml', 'docProps/core.xml'}, changed_parts

    approved = load(R / 'analysis/phase09b/results/phase09b_results.json')
    summary = {(x['metric'], x['group'], x['day']): x for x in approved['summary']}
    with (R / 'analysis/phase09b/tables/新数据描述统计汇总.csv').open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(summary) == len(rows) == 48
    for row in rows:
        src = summary[(row['metric'], row['group'], int(row['day']))]
        for key in ['mean', 'sd', 'min', 'max']:
            assert abs(float(row[key]) - src[key]) < 1e-10
        for key in ['n_containers', 'n_fruits', 'n_readings', 'missing_readings', 'missing_containers']:
            assert int(row[key]) == src[key]
        assert json.loads(row['source_locations']) == src['source_locations']

    def metric(label):
        return 'mass_loss' if '失重率' in label else 'decay_pct' if '累计腐烂' in label else 'firmness' if '表观硬度' in label else 'TSS'

    for row in new_tables[2][1:] + new_tables[4][1:]:
        label, day, group, ms, rng, nc, nf, _ = row
        src = summary[(metric(label), group, int(day))]
        assert ms == f'{src["mean"]:.3f} ± {src["sd"]:.3f}'
        assert rng == f'{src["min"]:.3f}—{src["max"]:.3f}'
        assert (int(nc), int(nf)) == (src['n_containers'], src['n_fruits'])
    selected = ['03_仪器与方法', '07_连续称重', '08_腐烂观察', '09_品质检测', '10_环境监测']
    raw = cells_from_selected_sheets(R / '实验记录.xlsx', selected)
    derived = cells_from_selected_sheets(R / 'analysis/phase09b/实验记录_派生计算修订副本.xlsx', selected)
    cols = {'03_仪器与方法': set('BCDEF'), '07_连续称重': set('HI'), '08_腐烂观察': set('IJ'), '09_品质检测': {'I'}, '10_环境监测': set('DE')}
    checked = {s: 0 for s in selected}
    xml_numeric_roundtrip_differences = []
    for key, value in raw.items():
        sh, address = key
        if re.sub(r'\d', '', address) not in cols[sh] or int(re.sub(r'\D', '', address)) < 5:
            continue
        other = derived.get(key)
        if other != value:
            # Approved Excel-engine export can serialize 83.24 as
            # 83.23999999999999. Check numerical equivalence without rounding
            # or changing either workbook, and retain this representation fact.
            assert value is not None and other is not None, (key, value, other)
            difference = abs(float(value) - float(other))
            assert difference < 1e-10, (key, value, other)
            xml_numeric_roundtrip_differences.append({'sheet': sh, 'cell': address, 'raw': value, 'approved_copy': other, 'absolute_difference': difference})
        checked[sh] += 1
    # Environment and TSS are direct raw values, compared without recomputing means.
    for e in approved['environment_records']:
        sh, region = e['source'].split('!')
        first, last = region.split(':')
        assert float(raw[(sh, first)]) == e['temperature_C']
        assert float(raw[(sh, last)]) == e['relative_humidity_pct']
    tss_count = 0
    for e in approved['fruit_quality']:
        if e['metric'] == 'TSS':
            sh, address = e['source'][0].split('!')
            value = raw[(sh, address)]
            assert (None if value is None else float(value)) == e['value']
            tss_count += 1

    start = next(i for i, p in enumerate(new.paragraphs) if p.text == '第1章 绪论' and p.style.name == 'Heading 1')
    end = next(i for i, p in enumerate(new.paragraphs) if p.text == '参考文献' and p.style.name == 'Heading 1')
    body = '\n'.join(p.text for p in new.paragraphs[start:end])
    assert list(dict.fromkeys(re.findall(r'\[(\d+)\]', body))) == [str(i) for i in range(1, 21)]
    references = [p.text for p in new.paragraphs if p.style.name == 'I Reference']
    assert references == [p.text for p in old.paragraphs if p.style.name == 'I Reference']
    assert len(references) == 20
    meta = load(J / 'audit/引用身份与装配信息.json')
    for ref in meta['records']:
        assert sha(R / ref['pdf_path']) == ref['sha256']
        assert ref['body_positions']
    assert not re.search(r'待确认|待核实|待填写|待作者|未定稿|预合稿|审核中|Codex|Git|Phase09|QA', '\n'.join(actual))
    image_hashes = []
    for document in [old, new]:
        hashes = []
        for shape in document.inline_shapes:
            rid = shape._inline.xpath('.//a:blip')[0].get(qn('r:embed'))
            hashes.append(hashlib.sha256(document.part.related_parts[rid].blob).hexdigest())
        image_hashes.append(hashes)
    assert image_hashes[0] == image_hashes[1] and len(image_hashes[1]) == 6

    pdf = fitz.open(O / '本科毕业论文_完整初稿预览.pdf')
    assert len(pdf) == 44
    actual_pages = {title: 'I' if title == '摘 要' else 'II' if title == 'Abstract' else pg - 8 for _, title, pg in pdf.get_toc()}
    assert actual_pages == load(O / 'evidence/page_map.json')
    for p in new.paragraphs:
        if p.style.name == 'I TOC' and p.text:
            title, pg = p.text.rsplit('\t', 1)
            assert pg == str(actual_pages[title])
    blank = [i + 1 for i, p in enumerate(pdf) if not p.get_text().strip()]
    assert blank == [2, 4]
    han = lambda text: ''.join(re.findall('[\u4e00-\u9fff]', text))
    # Remove repeated running headers before checking paragraphs that span pages.
    visible = han(''.join(b[4] for p in pdf for b in p.get_text('blocks') if b[1] > 65 and b[3] < 795))
    for p in new.paragraphs:
        if p.style.name in ['Normal', 'I Note', 'I Caption', 'I Reference'] and len(han(p.text)) > 10:
            assert han(p.text) in visible, p.text
    table_page = [i + 1 for i, p in enumerate(pdf) if '表3-1' in p.get_text() and '累计/初始' in p.get_text()]
    assert table_page == [24]
    assert all(token in pdf[23].get_text() for token in ['0.000 ± 0.000', '7.315 ± 1.814', '5.429 ± 0.688', '8.256 ± 0.190', '硬度有效技术读数'])
    assert all(t in pdf[0].get_text().replace(' ', '') for t in ['王馨', '202329060037', '食品质量与安全', '23级食品质量与安全02班', '陈琪玉', '二〇二七年六月'])

    result = {
        'status': 'PASS: bounded content/data/format consistency checks; not Windows Word final acceptance',
        'protected_paths': len(protected), 'raw_sha256': sha(R / '实验记录.xlsx'),
        'changed_docx_parts': changed_parts, 'local_text_spans': 9, 'reference_identities': 20,
        'approved_summary_combinations': 48, 'data_rows': {'table3_1': 24, 'table3_2': 8, 'appendix': 24},
        'raw_cells_compared_to_approved_copy': checked, 'direct_TSS_values_compared': tss_count,
        'xml_numeric_roundtrip_differences': xml_numeric_roundtrip_differences,
        'environment_values_compared': 60, 'auxiliary_sheet_18_opened': False,
        'embedded_image_hashes': image_hashes[1], 'unchanged_math_objects': len(new.element.xpath('.//m:oMath')),
        'pdf_pages': len(pdf), 'blank_pages': blank, 'table3_1_physical_page': 24,
        'toc_entries': len(actual_pages), 'acknowledgements_han': len(han(''.join(edits['acknowledgements']))),
        'docx_sha256': sha(O / '本科毕业论文_完整初稿.docx'),
        'pdf_sha256': sha(O / '本科毕业论文_完整初稿预览.pdf'),
    }
    (O / 'evidence/一致性核验结果.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
