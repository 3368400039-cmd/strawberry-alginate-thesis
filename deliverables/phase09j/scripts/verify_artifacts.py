"""Read-only verification against approved results; never runs experiment statistics.

Run from any directory. --record writes only this delivery's verification JSON.
Dependencies: python-docx, PyMuPDF. No Excel worksheet is read.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

import fitz
from docx import Document
from docx.oxml.ns import qn

R = Path(__file__).resolve().parents[3]
O = R / 'deliverables/phase09j'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_text(encoding='utf-8'))


def paragraphs(t):
    section, in_math, result = '结论', False, []
    for line in t.splitlines():
        if line.startswith(('## ', '### ')):
            section = line.split()[1]
            continue
        if line.startswith('$$'):
            in_math = not in_math
            continue
        if (not line or in_math or line.startswith(('#', '|', '![', '注：'))
                or re.match(r'^[图表]\d', line)):
            continue
        result.append((section, line))
    return result


def han(t):
    return ''.join(re.findall('[\u4e00-\u9fff]', t))


def tables(t):
    result, buf = [], []
    for line in t.splitlines() + ['']:
        if line.startswith('|'):
            buf.append([v.strip() for v in line.strip('|').split('|')])
        elif buf:
            result.append([buf[0]] + buf[2:])
            buf = []
    return result


def main(record=False):
    protected = read(O / 'audit/输入文件SHA-256.json')
    assert len(protected) == 232
    for name, digest in protected.items():
        assert sha(R / name) == digest, f'Protected input changed: {name}'
    assert sha(R / '实验记录.xlsx') == 'a63c8b0e1a07724e861d4b9a379ab632b3c0d41038f77310db36fb3b6b9f66f6'
    assert sha(O / 'literature/viewcontent.cgi 2.pdf') == '78863121c126ffe6f95f7faaf4724037e8405d44a070e24df35eb76c3397d0d3'

    meta = read(O / 'audit/引用身份与装配信息.json')
    approved = read(R / 'analysis/phase09b/results/phase09b_results.json')
    summary = {(s['metric'], s['group'], s['day']): s for s in approved['summary']}
    assert len(summary) == 48
    with (R / 'analysis/phase09b/tables/新数据描述统计汇总.csv').open(encoding='utf-8-sig', newline='') as f:
        csv_rows = list(csv.DictReader(f))
    assert len(csv_rows) == 48
    for row in csv_rows:
        src = summary[(row['metric'], row['group'], int(row['day']))]
        for key in ['mean', 'sd', 'min', 'max']:
            assert abs(float(row[key]) - src[key]) < 1e-10
        for key in ['n_containers', 'n_fruits', 'n_readings', 'missing_readings', 'missing_containers']:
            assert int(row[key]) == src[key]
        assert json.loads(row['source_locations']) == src['source_locations']

    texts = [(O / 'chapters' / n).read_text(encoding='utf-8') for n in meta['names']]
    narrative = [paragraphs(t) for t in texts]
    body = '\n'.join(texts)
    assert not re.search(r'\[LE\d+\]|Codex|Git|Phase|QA|待核|待确认|尚待|审计|未定稿|预合稿', body)
    first = list(dict.fromkeys(re.findall(r'\[(\d+)\]', body)))
    assert first == [str(i) for i in range(1, 21)]
    assert len(meta['records']) == len({x['source_id'] for x in meta['records']}) == 20
    refs = (O / '统一参考文献表.md').read_text(encoding='utf-8')
    assert re.findall(r'^\[(\d+)\]', refs, flags=re.M) == first
    for ref in meta['records']:
        assert sha(R / ref['pdf_path']) == ref['sha256']
        assert ref['body_positions']
        assert f"[{ref['number']}] {ref['bibliography']}" in refs

    doc = Document(O / '最终初稿.docx')
    assert len(doc.inline_shapes) == 6
    doc_text = '\n'.join(p.text for p in doc.paragraphs)
    assert not re.search(r'待确认|待核实|待填写|待作者|未定稿|预合稿|审核中|Phase09J|审计', doc_text)
    doc_han = han(doc_text)
    for chapter in narrative:
        for _, para in chapter:
            assert han(para) in doc_han
    for i, bib in meta['bibliography'].items():
        assert f'[{i}] {bib}' in doc_text

    pngs = {sha(p): str(p.relative_to(R)) for p in (R / 'analysis/phase09b/figures').glob('*.png')}
    embedded = []
    for shape in doc.inline_shapes:
        rid = shape._inline.xpath('.//a:blip')[0].get(qn('r:embed'))
        digest = hashlib.sha256(doc.part.related_parts[rid].blob).hexdigest()
        assert digest in pngs
        embedded.append(pngs[digest])
    assert len(set(embedded)) == 6
    display_equations = [p for p in doc.paragraphs if p.text.strip() in ['（2-1）', '（2-2）']]
    assert len(display_equations) == 2
    assert all(len(p._p.xpath('.//m:oMath')) == 1 for p in display_equations)

    md_tables = tables(texts[2])
    dt = [[[c.text for c in row.cells] for row in tb.rows] for tb in doc.tables]
    assert dt[2][1:] + dt[3][1:] == md_tables[0][1:]
    assert dt[4][1:] == md_tables[1][1:]
    assert len(md_tables[0][1:]) == 24 and len(md_tables[1][1:]) == 8

    def metric(label):
        return 'mass_loss' if '失重率' in label else 'decay_pct' if '累计腐烂' in label else 'firmness' if '表观硬度' in label else 'TSS'

    for row in md_tables[0][1:]:
        label, day, group, ms, rng, nc, nf, decay = row
        src = summary[(metric(label), group, int(day))]
        assert ms == f'{src["mean"]:.3f} ± {src["sd"]:.3f}'
        assert rng == f'{src["min"]:.3f}—{src["max"]:.3f}'
        assert (int(nc), int(nf)) == (src['n_containers'], src['n_fruits'])
        if src['metric'] == 'decay_pct':
            # A count identity against an approved percentage, not a new analysis.
            assert decay == f'{round(src["mean"] * 36 / 100)}/36'
        else:
            assert decay == '—'

    appendix = dt[5][1:]
    assert len(appendix) == 24
    for row in appendix:
        label, day, group, ms, rng, nc, nf, missing = row
        src = summary[(metric(label), group, int(day))]
        assert ms == f'{src["mean"]:.3f} ± {src["sd"]:.3f}'
        assert rng == f'{src["min"]:.3f}—{src["max"]:.3f}'
        assert (int(nc), int(nf), int(missing)) == (src['n_containers'], src['n_fruits'], src['missing_readings'])

    contrasts = {(s['metric'], s['contrast'].replace(' ', '')): s for s in approved['batch_contrasts']}
    for label, contrast, b1, b2, b3, ms in md_tables[1][1:]:
        src = contrasts[(metric(label), contrast.replace(' ', '').replace('−', '-'))]
        assert [b1, b2, b3] == [f'{src[k]:.3f}' for k in ['B1', 'B2', 'B3']]
        assert ms == f'{src["mean"]:.3f} ± {src["sd"]:.3f}'

    pdf = fitz.open(O / '完整排版预览.pdf')
    assert len(pdf) == 45
    start = next(pg for _, title, pg in pdf.get_toc() if title.startswith('第1章'))
    actual = {title: 'I' if title == '摘 要' else 'II' if title == 'Abstract' else pg - start + 1 for _, title, pg in pdf.get_toc()}
    assert actual == meta['page_map']
    for p in doc.paragraphs:
        if p.style.name == 'I TOC' and p.text:
            title, page = p.text.rsplit('\t', 1)
            assert page == str(actual[title])
    visible = han(''.join(b[4] for p in pdf for b in p.get_text('blocks') if b[1] > 65 and b[3] < 795))
    for chapter in narrative:
        for _, para in chapter:
            assert han(para) in visible
    for n in [2, 4]:
        assert not pdf[n - 1].get_text().strip()

    result = {
        'checks': 'PASS: artifact consistency only; not external scientific or Microsoft Word acceptance',
        'protected_inputs': len(protected), 'summary_combinations': len(summary),
        'main_table_rows': 24, 'batch_table_rows': 8, 'appendix_rows': 24,
        'embedded_approved_figures': embedded, 'pdf_pages': len(pdf),
        'toc_entries': len(actual), 'different_cited_identities': 20,
        'narrative_han_by_chapter': [len(han(''.join(p for _, p in ps))) for ps in narrative],
        'docx_sha256': sha(O / '最终初稿.docx'), 'pdf_sha256': sha(O / '完整排版预览.pdf'),
        'no_worksheet_content_read': True,
    }
    if record:
        (O / 'audit/自动一致性复核.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', action='store_true')
    main(parser.parse_args().record)
