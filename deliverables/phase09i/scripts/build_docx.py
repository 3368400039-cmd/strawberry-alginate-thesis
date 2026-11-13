from pathlib import Path
from copy import deepcopy
import json,re,io,zipfile,hashlib
from lxml import etree
from docx import Document
from docx.shared import Cm,Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_BREAK,WD_TAB_ALIGNMENT,WD_TAB_LEADER
from docx.enum.section import WD_SECTION_START
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
import tempfile,subprocess
R=Path(__file__).resolve().parents[3];O=R/'deliverables/phase09i';T=Path(tempfile.mkdtemp(prefix='phase09i_docx_'))
OUT=O/'可食性海藻酸钠膜对草莓常温保鲜效果的研究_初稿精修版.docx'
data=json.loads((O/'audit/引用身份与修订计量.json').read_text())
(T/'page_map.json').write_text(json.dumps(data['page_map'],ensure_ascii=False))
(T/'table_cut.txt').write_text(str(data['table_cut']))
combined='\n\n'.join((O/'chapters'/n).read_text() for n in data['names'])
(T/'body.md').write_text(combined.replace('../../../analysis/',str(R/'analysis')+'/'))
subprocess.run(['pandoc',str(T/'body.md'),'--from','markdown+tex_math_dollars','--to','docx','--reference-doc='+str(R/'四川工业科技学院本科毕业设计(论文)-样式模板(定稿).docx'),'-o',str(T/'body.docx')],check=True)
S=Document(T/'body.docx');D=Document(R/'四川工业科技学院本科毕业设计(论文)-样式模板(定稿).docx')
cover=[deepcopy(p._p) for p in D.paragraphs[:27]]
declaration=[deepcopy(p._p) for p in D.paragraphs[29:35]]
authorization=[deepcopy(p._p) for p in D.paragraphs[39:45]]
b=D._element.body
for e in list(b):
 if e.tag!=qn('w:sectPr'):b.remove(e)
for e in list(D.settings.element):
 if e.tag==qn('w:evenAndOddHeaders'):D.settings.element.remove(e)
def font(r,size=12,cjk='宋体',bold=None):
 r.font.name='Times New Roman';r.font.size=Pt(size)
 f=r._element.get_or_add_rPr().get_or_add_rFonts()
 for k,v in [('eastAsia',cjk),('ascii','Times New Roman'),('hAnsi','Times New Roman'),('cs','Times New Roman')]:f.set(qn('w:'+k),v)
 if bold is not None:r.bold=bold
def style(name,size=12,cjk='宋体',first=0,line=1.5):
 s=D.styles[name] if name in D.styles else D.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
 s.font.name='Times New Roman';s.font.size=Pt(size);s.font.bold=False
 f=s._element.get_or_add_rPr().get_or_add_rFonts();f.set(qn('w:eastAsia'),cjk)
 p=s.paragraph_format;p.line_spacing=line;p.space_before=Pt(0);p.space_after=Pt(0);p.first_line_indent=Pt(first);p.keep_with_next=False;p.keep_together=False;p.widow_control=True
 snap=OxmlElement('w:snapToGrid');snap.set(qn('w:val'),'0');s._element.get_or_add_pPr().append(snap)
 return s
style('Normal',first=24)
for lev,size in [(1,16),(2,14),(3,12)]:
 s=style('Heading '+str(lev),size,'黑体');s.paragraph_format.keep_with_next=True
 s.paragraph_format.space_before=Pt(12 if lev==1 else 6);s.paragraph_format.space_after=Pt(12 if lev==1 else 6)
 s.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.CENTER if lev==1 else WD_ALIGN_PARAGRAPH.LEFT
 s._element.get_or_add_pPr().find(qn('w:outlineLvl')).set(qn('w:val'),str(lev-1))
for n,size in [('I Caption',10.5),('I Note',10.5),('I Reference',10.5),('I TOC',12),('I Admin',12)]:style(n,size)
style('I Cover',14,'黑体')
style('I TOC Title',16,'黑体').paragraph_format.alignment=WD_ALIGN_PARAGRAPH.CENTER
def setup(s,fmt=None):
 s.page_width=Cm(21);s.page_height=Cm(29.7);s.top_margin=Cm(2);s.bottom_margin=Cm(1.5);s.left_margin=Cm(2);s.right_margin=Cm(2);s.gutter=Cm(1);s.header_distance=Cm(1.5);s.footer_distance=Cm(1)
 s.different_first_page_header_footer=False
 for x in list(s._sectPr):
  if x.tag in [qn('w:docGrid'),qn('w:pgNumType')]:s._sectPr.remove(x)
 s.header.is_linked_to_previous=False;s.footer.is_linked_to_previous=False
 for c in [s.header,s.footer]:
  for x in list(c._element):c._element.remove(x)
  c.add_paragraph()
 if fmt:
  p=s.header.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER;font(p.add_run('四川工业科技学院本科毕业设计（论文）'),10.5);p.paragraph_format.first_line_indent=Pt(0)
  p=s.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.first_line_indent=Pt(0)
  field(p,' PAGE ','1')
  x=OxmlElement('w:pgNumType');x.set(qn('w:fmt'),fmt);x.set(qn('w:start'),'1');s._sectPr.append(x)
def field(p,instruction,result):
 for ty in ['begin','instr','separate','result','end']:
  r=p.add_run();font(r,10.5)
  if ty in ['begin','separate','end']:
   x=OxmlElement('w:fldChar');x.set(qn('w:fldCharType'),ty)
  elif ty=='instr':x=OxmlElement('w:instrText');x.set(qn('xml:space'),'preserve');x.text=instruction
  else:x=OxmlElement('w:t');x.text=result
  r._r.append(x)
def add(t='',style='Normal',page=False):
 p=D.add_paragraph(t,style=style);p.paragraph_format.page_break_before=page
 return p
def heading(t,page=False):
 p=add(t,'Heading 1',page);return p
def breakpage():
 p=add('',style='I Admin');p.paragraph_format.line_spacing=Pt(1);p.paragraph_format.space_after=Pt(0);p.add_run().add_break(WD_BREAK.PAGE)
setup(D.sections[0])
# Reuse actual school artwork and cover paragraph formatting. Consolidate the
# template's consecutive empty cover paragraphs into paragraph spacing.
for idx in [1,10,12,15,16,17,18,19,20,26]:
 e=cover[idx];b.insert(len(b)-1,e);p=Paragraph(e,D)
 if idx==1:
  p.paragraph_format.space_before=Pt(22);p.paragraph_format.line_spacing=Pt(22)
 elif idx==10:
  p.paragraph_format.space_before=Pt(176);p.paragraph_format.line_spacing=Pt(33)
  p.clear();font(p.add_run('本科毕业设计（论文）'),22,'黑体')
  # Remove non-content template anchors/empty compatibility shapes in title.
  for x in list(p._p.xpath('.//w:drawing | .//w:pict')):x.getparent().remove(x)
 elif idx==12:
  for r in list(p.runs):r._r.getparent().remove(r._r)
  font(p.add_run('可食性海藻酸钠膜对草莓常温保鲜效果的研究'),16,'黑体')
  p.paragraph_format.space_before=Pt(16);p.paragraph_format.line_spacing=Pt(24);p.paragraph_format.keep_together=True
 elif idx in [15,16,17,18,19,20]:
  # Keep the template's field indentation and use its 22 pt cover line pitch.
  p.paragraph_format.line_spacing=Pt(22);p.paragraph_format.space_before=Pt(10);p.paragraph_format.space_after=Pt(0)
  sp=p._p.pPr.find(qn('w:spacing'))
  for key in ['beforeLines','afterLines']:
   if sp.get(qn('w:'+key)) is not None:del sp.attrib[qn('w:'+key)]
  if idx==15:p.paragraph_format.space_before=Pt(26)
  if idx==18:
   for r in list(p.runs):r._r.getparent().remove(r._r)
   font(p.add_run('年 级 班：'),14,'黑体')
  font(p.add_run('〔待填写〕'),14,'黑体')
 elif idx==26:
  for r in list(p.runs):r._r.getparent().remove(r._r)
  font(p.add_run('〔毕业年月待填写〕'),14,'黑体');p.paragraph_format.space_before=Pt(88);p.paragraph_format.line_spacing=Pt(22)
breakpage();breakpage()  # school requires a blank cover reverse
# Standard declarations are preserved from template, with unsigned fields.
for elems,title in [(declaration,'原创声明'),(authorization,'学位论文版权使用授权书')]:
 p=add(title,'Heading 1');p.style='I Admin';p.alignment=WD_ALIGN_PARAGRAPH.CENTER
 for r in p.runs:font(r,16,'黑体')
 p.paragraph_format.space_after=Pt(20)
 # actual template statement paragraphs, no example research statements
 for e in elems:
  text=''.join(e.itertext()) if False else ''.join(e.xpath('.//w:t/text()'))
  if len(text)>60:
   p=add(text,'Normal');p.paragraph_format.first_line_indent=Pt(24)
 sig=add('毕业论文作者签名：____________    签字日期：____年____月','I Admin');sig.paragraph_format.space_after=Pt(20)
breakpage()  # template combines both declarations on one page, reverse blank
s=D.add_section(WD_SECTION_START.ODD_PAGE);setup(s,'upperRoman')
zh=[
'草莓贮藏期间的质量、可见腐烂、力学状态及可溶性固形物可能对处理方式产生不同响应。本研究以完整草莓为对象，比较CK（水—新水）、Ca（水—氯化钙）和SA-Ca（海藻酸钠—氯化钙）三种双步浸渍流程在短期常温条件下的品质表现。',
'实验设置三个日期批次，共54个容器189果。L队列27盒108果连续观察第0—4天的失重及累计腐烂；D队列27盒81果在第0、2、4天取不同果实测定表观硬度及可溶性固形物（TSS）。以容器为主要层级进行描述统计。离散监测温度为22.5—24.8 ℃，相对湿度为62.9%—78.4%。',
'三组失重率均随贮藏日升高，第4天均值由高到低为Ca、SA-Ca、CK。累计腐烂分别为15/36、12/36、13/36，Ca最低；可测果中SA-Ca表观硬度均值最高，为5.429 N，CK的TSS均值最高，为8.561 °Brix。三组TSS从第0天到第2天均升高，随后CK和SA-Ca略升，Ca组均值保持不变。四指标未形成某组全面占优的排序，部分组间差随批次改变方向。上述结果为四天窗口内的描述比较，共享母液、不同D取样果及终点不可测果限制了推广范围。']
en=[
'Strawberry mass, visible decay, mechanical response, and soluble solids may respond differently to postharvest treatments. This study compared three two-step dipping procedures for whole strawberries during short-term ambient storage: CK (water followed by fresh water), Ca (water followed by calcium chloride), and SA-Ca (sodium alginate followed by calcium chloride).',
'Three date batches comprised 54 containers and 189 fruits. The L cohort included 27 containers with 108 fruits for repeated weighing and cumulative decay observations from day 0 to day 4. The D cohort included 27 containers with 81 fruits, with different fruits sampled on days 0, 2, and 4 for apparent firmness and total soluble solids (TSS). Descriptive statistics were calculated primarily at the container level. Discrete environmental measurements ranged from 22.5 to 24.8 °C and from 62.9% to 78.4% relative humidity.',
'Mean mass loss increased in all groups, with day-4 means ordered Ca > SA-Ca > CK. Cumulative decay was 15/36, 12/36, and 13/36 for CK, Ca, and SA-Ca, respectively, and was lowest in Ca. Among measurable fruits, SA-Ca had the highest final mean apparent firmness (5.429 N), whereas CK had the highest final mean TSS (8.561 °Brix). TSS increased from day 0 to day 2 in all groups; it then increased slightly in CK and SA-Ca, while the Ca group mean remained unchanged. No treatment performed favorably across all four indicators, and some contrasts changed direction across batches. These findings describe a four-day observation window; shared mother solutions, different D-cohort fruits across sampling days, and unmeasurable endpoint fruits limit their generalizability.']
heading('摘 要')
for t in zh:add(t)
p=add('关键词：草莓; 海藻酸钠; 双步浸渍; 常温贮藏; 品质评价');p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.space_before=Pt(18)
heading('Abstract',True)
for t in en:add(t)
p=add('Keywords: strawberry; sodium alginate; two-step dipping; ambient storage; quality evaluation');p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.space_before=Pt(18)
toc_heading=heading('目 录',True);toc_heading.style='I TOC Title'
toc=[(1,'摘 要'),(1,'Abstract')]
for p in S.paragraphs:
 if p.style.name.startswith('Heading'):toc.append((int(p.style.name[-1]),p.text))
toc.extend([(1,'参考文献'),(1,'附录1 中间时点描述统计补充'),(1,'致 谢')])
pages=json.loads((T/'page_map.json').read_text()) if (T/'page_map.json').exists() else {}
for i,(lev,title) in enumerate(toc):
 p=add('',style='I TOC');p.paragraph_format.line_spacing=1.5;p.paragraph_format.left_indent=Cm((lev-1)*.5);p.paragraph_format.tab_stops.add_tab_stop(Cm(15.5-(lev-1)*.5),WD_TAB_ALIGNMENT.RIGHT,WD_TAB_LEADER.DOTS)
 if i==0:
  rr=p.add_run();f=OxmlElement('w:fldChar');f.set(qn('w:fldCharType'),'begin');rr._r.append(f)
  rr=p.add_run();f=OxmlElement('w:instrText');f.text=' TOC \\o "1-3" \\h \\z \\u ';rr._r.append(f)
  rr=p.add_run();f=OxmlElement('w:fldChar');f.set(qn('w:fldCharType'),'separate');rr._r.append(f)
 r=p.add_run(title+'\t'+str(pages.get(title,'—')));font(r,12,'黑体' if lev==1 else '宋体')
 if i==len(toc)-1:
  rr=p.add_run();f=OxmlElement('w:fldChar');f.set(qn('w:fldCharType'),'end');rr._r.append(f)
s=D.add_section(WD_SECTION_START.ODD_PAGE);setup(s,'decimal')
bid=100;eq=0
def bookmark(p,title):
 global bid
 a=OxmlElement('w:bookmarkStart');a.set(qn('w:id'),str(bid));a.set(qn('w:name'),'I_'+str(bid));p._p.insert(0,a)
 z=OxmlElement('w:bookmarkEnd');z.set(qn('w:id'),str(bid));p._p.append(z);bid+=1
alts={'L队列失重率随贮藏日变化','L队列累计腐烂比例与容器分布','不同D取样日的表观硬度','不同D取样日的TSS','三个日期批次的终点组均值','三批次的离散温湿度监测'}
for src in S._element.body:
 if src.tag==qn('w:p') and Paragraph(src,S).text in alts:continue
 if src.tag==qn('w:sectPr'):continue
 e=deepcopy(src);b.insert(len(b)-1,e)
 for blip in e.iter(qn('a:blip')):
  rid=blip.get(qn('r:embed'))
  if rid:
   newrid,_=D.part.get_or_add_image(io.BytesIO(S.part.related_parts[rid].blob));blip.set(qn('r:embed'),newrid)
 if e.tag==qn('w:p'):
  oldp=Paragraph(src,S);p=Paragraph(e,D);t=p.text
  if oldp.style.name.startswith('Heading'):
   p.style=oldp.style.name;p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.page_break_before=(p.style.name=='Heading 1' and not t.startswith('第1章'));bookmark(p,t)
  elif p._p.xpath('.//m:oMathPara'):
   p.style='Normal';p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.line_spacing=1.5;eq+=1
   m=p._p.xpath('.//m:oMathPara')[0];mo=m.find(qn('m:oMath'));p._p.remove(m);p.add_run('\t');p._p.append(mo);p.add_run(f'\t（2-{eq}）');p.paragraph_format.tab_stops.add_tab_stop(Cm(7.75),WD_TAB_ALIGNMENT.CENTER);p.paragraph_format.tab_stops.add_tab_stop(Cm(15.5),WD_TAB_ALIGNMENT.RIGHT)
  elif p._p.xpath('.//w:drawing'):
   p.style='Normal';p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.line_spacing=1.0;p.paragraph_format.keep_with_next=True;p.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.CENTER
  elif re.match(r'^[图表]\d',t):
   p.style='I Caption';p.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.keep_with_next=True
  elif t.startswith('注：'):p.style='I Note';p.paragraph_format.keep_with_next=False;p.paragraph_format.keep_together=True
  else:p.style='Normal'
  for r in p.runs:font(r,16 if p.style.name=='Heading 1' else 14 if p.style.name=='Heading 2' else 12 if p.style.name not in ['I Caption','I Note'] else 10.5,'黑体' if p.style.name.startswith('Heading') else '宋体')
  if p.style.name=='Normal':
   for r in list(p.runs):
    if re.search(r'\[\d+\]',r.text):
     prev=r._r
     for ch in re.split(r'(\[\d+\])',r.text):
      if not ch:continue
      rr=OxmlElement('w:r');pr=deepcopy(r._r.rPr);rr.append(pr)
      if re.fullmatch(r'\[\d+\]',ch):v=OxmlElement('w:vertAlign');v.set(qn('w:val'),'superscript');pr.append(v)
      x=OxmlElement('w:t');x.set(qn('xml:space'),'preserve');x.text=ch;rr.append(x);prev.addnext(rr);prev=rr
     r._r.getparent().remove(r._r)
# Separate the long 24-row table at a measured layout boundary. All data cells
# remain byte-for-text identical; the continuation caption is a layout element.
cut=int((T/'table_cut.txt').read_text()) if (T/'table_cut.txt').exists() else 10
for tb in list(D.tables):
 if len(tb.rows)==25 and len(tb.columns)==8:
  e=tb._tbl;rows=list(e.findall(qn('w:tr')));sec=deepcopy(e)
  for rr in list(sec.findall(qn('w:tr'))):sec.remove(rr)
  sec.append(deepcopy(rows[0]))
  for rr in rows[cut+1:]:sec.append(deepcopy(rr));e.remove(rr)
  x=OxmlElement('w:p');p=Paragraph(x,D);p.style='I Caption';p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.page_break_before=True;p.paragraph_format.keep_with_next=True;font(p.add_run('续表3-1　各指标基线与终点的描述统计汇总'),10.5)
  e.addnext(x);x.addnext(sec)
heading('参考文献',True)
for k,v in data['bibliography'].items():
 p=add(f'[{k}] {v}','I Reference');p.paragraph_format.left_indent=Cm(.74);p.paragraph_format.first_line_indent=Cm(-.74);p.paragraph_format.keep_together=True
heading('附录1 中间时点描述统计补充',True)
add('下表补充正文表3-1未列出的中间时点。均值、SD及范围按有效容器计算，D队列不同日使用不同果实。','I Note')
add('附表1　中间时点容器层级描述统计','I Caption').alignment=WD_ALIGN_PARAGRAPH.CENTER
J=json.loads((R/'analysis/phase09b/results/phase09b_results.json').read_text());xs=[r for r in J['summary'] if r['day'] not in [0,4]];assert len(xs)==24
tb=D.add_table(rows=1,cols=8)
for c,t in zip(tb.rows[0].cells,['指标（单位）','日','组','均值 ± SD','容器值范围','有效盒','覆盖/可测果','缺失读数']):c.text=t
for x in xs:
 for c,t in zip(tb.add_row().cells,[x['metric_label']+'（'+x['unit']+'）',str(x['day']),x['group'],f'{x["mean"]:.3f} ± {x["sd"]:.3f}',f'{x["min"]:.3f}—{x["max"]:.3f}',str(x['n_containers']),str(x['n_fruits']),str(x['missing_readings'])]):c.text=t
add('注：L称重果数表示盒内覆盖果数；累计腐烂分母每组初始36果。SD为容器间样本标准差。硬度技术读数先在同果内平均，缺失保留。','I Note')
heading('致 谢',True);add('〔待作者填写真实人员与贡献〕','I Admin')
# Merge identical indicator labels vertically. The 24 logical observations remain intact.
for tb in D.tables:
 if len(tb.columns)!=8:continue
 start=1
 while start<len(tb.rows):
  label=tb.cell(start,0).text;end=start
  while end+1<len(tb.rows) and tb.cell(end+1,0).text==label:end+=1
  if end>start:
   cell=tb.cell(start,0).merge(tb.cell(end,0));cell.text=label
  start=end+1
# Textbox example notes and template watermarks cannot leak into the thesis.
for x in list(b.xpath('.//w:txbxContent')):
 parent=x
 while parent.getparent() is not None and parent.tag not in [qn('w:drawing'),qn('w:pict')]:parent=parent.getparent()
 if parent.getparent() is not None:parent.getparent().remove(parent)
# Format tables without locking a whole table into a single unbreakable block.
for tb in D.tables:
 tb.autofit=False;tb.alignment=WD_ALIGN_PARAGRAPH.CENTER;n=len(tb.columns)
 widths=[2.1,.65,1.1,2.65,2.8,1.2,1.4,1.6] if n==8 else ([3.0,2.6,3.8,2.4,3.7,] if n==5 else [2.7,2.4,2.4,2.4,2.4,3.2] if n==6 else [15.5/n]*n)
 widths=[v*15.5/sum(widths) for v in widths]
 for k,w in enumerate(widths):
  tb.columns[k].width=Cm(w)
  for c in tb.columns[k].cells:c.width=Cm(w)
 pr=tb._tbl.tblPr
 for name in ['tblStyle','tblBorders']:
  x=pr.find(qn('w:'+name))
  if x is not None:pr.remove(x)
 bd=OxmlElement('w:tblBorders')
 for side in ['top','bottom','left','right','insideH','insideV']:
  x=OxmlElement('w:'+side);x.set(qn('w:val'),'single' if side in ['top','bottom'] else 'nil');x.set(qn('w:sz'),'6');bd.append(x)
 pr.append(bd)
 tw=pr.find(qn('w:tblW'));tw.set(qn('w:type'),'dxa');tw.set(qn('w:w'),str(Cm(15.5).twips))
 for ri,row in enumerate(tb.rows):
  tr=row._tr.get_or_add_trPr();x=OxmlElement('w:cantSplit');tr.append(x)
  if ri==0:x=OxmlElement('w:tblHeader');tr.append(x)
  for c in row.cells:
   mar=OxmlElement('w:tcMar')
   for side in ['left','right']:
    xx=OxmlElement('w:'+side);xx.set(qn('w:w'),'30');xx.set(qn('w:type'),'dxa');mar.append(xx)
   c._tc.get_or_add_tcPr().append(mar)
   for p in c.paragraphs:
    p.style='Normal';p.paragraph_format.first_line_indent=Pt(0);p.paragraph_format.line_spacing=1.5;p.paragraph_format.space_before=Pt(0);p.paragraph_format.space_after=Pt(0);p.paragraph_format.keep_with_next=((len(tb.columns)==6 and len(tb.rows)==9) or ri==0 or (ri==len(tb.rows)-1 and (tb._tbl.getnext() is None or not ''.join(tb._tbl.getnext().itertext()).startswith('续表'))));p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:font(r,10.5,bold=ri==0)
    if ri==0:
     pb=OxmlElement('w:tcBorders');x=OxmlElement('w:bottom');x.set(qn('w:val'),'single');x.set(qn('w:sz'),'4');pb.append(x);c._tc.get_or_add_tcPr().append(pb)
# Size only new inline figure instances; original PNG bytes remain unchanged.
for shape in D.inline_shapes:
 if shape.width and shape.height:
  ratio=shape.height/shape.width;shape.width=Cm(15.0);shape.height=int(Cm(15.0)*ratio)
for p in D.paragraphs:
 if p.style.name in ['Normal','I Note','I Caption','I Reference','I TOC','Heading 1','Heading 2','Heading 3','I Admin']:
  for r in p.runs:
   if r.font.size is None:font(r,10.5 if p.style.name in ['I Note','I Caption','I Reference'] else 16 if p.style.name=='Heading 1' else 14 if p.style.name=='Heading 2' else 12,'黑体' if p.style.name.startswith('Heading') else '宋体')
D.core_properties.title='可食性海藻酸钠膜对草莓常温保鲜效果的研究';D.core_properties.author='';D.core_properties.subject='本科毕业论文初稿'
u=OxmlElement('w:updateFields');u.set(qn('w:val'),'true');D.settings.element.append(u)
# Remove unused template picture relationships; retain school artwork and six approved figures.
used=set(D.element.xpath('//@r:embed'))
for rid,rel in list(D.part.rels.items()):
 if rel.reltype.endswith('/image') and rid not in used:del D.part.rels[rid]
D.save(OUT)
with zipfile.ZipFile(OUT) as z:parts={n:z.read(n) for n in z.namelist()}
root=etree.fromstring(parts['docProps/app.xml'])
for e in list(root):
 if etree.QName(e).localname in ['Pages','Words','Characters','Lines','Paragraphs','TotalTime','CharactersWithSpaces','Application','Template']:root.remove(e)
parts['docProps/app.xml']=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
with zipfile.ZipFile(T/'clean.docx','w',zipfile.ZIP_DEFLATED) as z:
 for k,v in parts.items():z.writestr(k,v)
OUT.write_bytes((T/'clean.docx').read_bytes())
(T/'build.json').write_text(json.dumps({'output':str(OUT),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'zh':zh,'en':en,'toc':toc,'table_cut':cut},ensure_ascii=False,indent=2))
print(str(OUT));print('TOC entries',len(toc),'figures',len(D.inline_shapes))
