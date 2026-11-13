"""Apply only authorized finishing edits to the frozen Phase09J DOCX.

This script does not open experimental worksheets or run statistics.
Optional evidence/page_map.json holds verified TOC results from actual rendering.
"""
from copy import deepcopy
from pathlib import Path
import json

from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn

R = Path(__file__).resolve().parents[3]
O = R / 'deliverables/phase09k'
SRC = R / 'deliverables/phase09j/最终初稿.docx'
OUT = O / '本科毕业论文_完整初稿.docx'

REPLACEMENTS = [
    ('2.1.2', '实验记录所载质量测量设备为YP30002电子天平，表观硬度设备为TA.XTC-18穿刺质构仪及P-2不锈钢圆柱探头，TSS设备为PAL-1折光仪。',
     '质量测量采用YP30002电子天平，表观硬度测量采用TA.XTC-18穿刺质构仪及P-2不锈钢圆柱探头，TSS测量采用PAL-1折光仪。'),
    ('2.1.2', '以下仪器参数与制样条件按实验记录记述。', ''),
    ('2.4.1', '实验记录将整盒称量扣除容器皮重后的数值定义为盒内4果总净质量。', '整盒称量后扣除容器皮重，得到盒内4果的总净质量。'),
    ('2.4.2', 'D队列外观记录不进入L比例分母。', 'D果不计入该分母。'),
    ('2.4.3', '记录的穿刺条件为', '穿刺条件为'),
    ('2.4.3', '按记录的检测资格，', '检测时，'),
    ('2.4.4', '按记录，单果去萼后取果肉研磨', '单果去萼后取果肉研磨'),
    ('2.4.4', '测定室温记为22—25 ℃', '测定室温为22—25 ℃'),
    ('4.3', '本研究按实验记录的净质量定义和检测条件整理结果。', ''),
]

ACKNOWLEDGEMENTS = [
    '本论文在陈琪玉老师的指导下完成。感谢陈老师在课题研究和论文写作中给予的指导。在整理实验记录、分析结果和修改论文的过程中，我逐步认识到，清楚记录实验过程、准确表达数据，是开展食品品质研究的基本要求。',
    '感谢四川工业科技学院提供的学习环境。食品质量与安全专业的学习为我理解品质评价与实验方法打下了基础。完成这篇论文，也让我看到了自己在研究设计和学术表达方面仍需改进的地方。对于论文中的不足，恳请老师批评指正。',
]


def main():
    d = Document(SRC)
    changes = []
    for section, old, new in REPLACEMENTS:
        ps = [p for p in d.paragraphs if old in p.text]
        assert len(ps) == 1, (section, old)
        p = ps[0]
        before = p.text
        ts = [t for t in p._p.xpath('.//w:t') if old in (t.text or '')]
        assert len(ts) == 1, 'Keep run formatting: replacement must not span runs'
        ts[0].text = ts[0].text.replace(old, new, 1)
        changes.append({'section': section, 'before': before, 'after': p.text})

    values = {
        '姓    名：': '王馨', '学    号：': '202329060037',
        '专    业：': '食品质量与安全', '年 级 班：': '23级食品质量与安全02班',
        '指导教师：': '陈琪玉',
    }
    for label, value in values.items():
        p = next(p for p in d.paragraphs if p.text.startswith(label))
        assert p.runs[-1].text == '____________'
        p.runs[-1].text = value
    # College has expressly not been supplied: keep the normal template blank.
    assert next(p for p in d.paragraphs if p.text.startswith('二级学院：')).text == '二级学院：____________'
    date = next(p for p in d.paragraphs if p.text == '______年____月')
    date.runs[0].text = '二〇二七年六月'
    date.runs[0].font.color.rgb = RGBColor(0, 0, 0)

    # Merge the existing 3+21 data-row tables; remove only the duplicated header
    # and layout continuation caption. Every logical data cell is retained.
    t1, t2 = d.tables[2], d.tables[3]
    before_rows = [[c.text for c in row.cells] for t in [t1, t2] for row in list(t.rows)[1:]]
    assert len(before_rows) == 24 and len(t1.rows) == 4 and len(t2.rows) == 22
    for row in list(t2._tbl.tr_lst)[1:]:
        t1._tbl.append(deepcopy(row))
    t2._tbl.getparent().remove(t2._tbl)
    cont = next(p for p in d.paragraphs if p.text.startswith('续表3-1'))
    cont._p.getparent().remove(cont._p)
    # Restore one common label for the six mass-loss rows (0 d and 4 d).
    # Other metric labels already span their six rows in the source table.
    merged = t1.cell(1, 0).merge(t1.cell(6, 0))
    merged.text = before_rows[0][0]
    exemplar = t1.cell(7, 0).paragraphs[0]
    for p in merged.paragraphs:
        if p._p.pPr is not None:
            p._p.remove(p._p.pPr)
        p._p.insert(0, deepcopy(exemplar._p.pPr))
        for run in p.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(10.5)
            run._element.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), '宋体')
    assert [[c.text for c in row.cells] for row in list(t1.rows)[1:]] == before_rows
    caption = next(p for p in d.paragraphs if p.text.startswith('表3-1'))
    caption.paragraph_format.page_break_before = True
    caption.paragraph_format.keep_with_next = True
    # The native repeated header and cantSplit rows are inherited intact.
    assert t1.rows[0]._tr.xpath('./w:trPr/w:tblHeader')

    assert d.paragraphs[-1].text == '致 谢'
    normal_example = next(p for p in d.paragraphs if p.style.name == 'Normal' and p.text.startswith('本研究回答三个问题'))
    for text in ACKNOWLEDGEMENTS:
        p = d.add_paragraph(text, style='Normal')
        p.paragraph_format.first_line_indent = Pt(24)
        p.paragraph_format.line_spacing = 1.5
        for run in p.runs:
            run._r.insert(0, deepcopy(normal_example.runs[0]._r.rPr))

    page_map = O / 'evidence/page_map.json'
    if page_map.exists():
        pages = json.loads(page_map.read_text())
        for p in d.paragraphs:
            if p.style.name == 'I TOC' and p.text:
                title, _ = p.text.rsplit('\t', 1)
                run = next(r for r in p.runs if '\t' in r.text)
                run.text = title + '\t' + str(pages[title])
    d.core_properties.author = '王馨'
    d.save(OUT)
    (O / 'evidence/局部修订记录.json').write_text(json.dumps({
        'text_changes': changes, 'cover_values': values,
        'cover_college': '留空：用户明确要求', 'cover_date': '二〇二七年六月',
        'table_3_1_logical_rows': before_rows, 'acknowledgements': ACKNOWLEDGEMENTS,
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(OUT)
    print('Local text edits:', len(changes), '; table3-1 data rows:', len(before_rows))


if __name__ == '__main__':
    main()
