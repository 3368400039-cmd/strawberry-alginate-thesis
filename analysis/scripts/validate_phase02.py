"""Independent pandas aggregation and artifact checks. No significance tests or formula engine.
Run after analyze_phase02.py and build_phase02_reports.py.
"""
from pathlib import Path
from collections import Counter
import hashlib,json,re,math
import pandas as pd
import numpy as np
from PIL import Image
from lxml import etree
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
D=json.loads((P/'phase02_results.json').read_text());src=R/'analysis/研究数据_公式修复核验副本.xlsx'
def close(a,b):assert math.isclose(float(a),float(b),rel_tol=1e-10,abs_tol=1e-10),(a,b)
for n,h in D['input_hashes'].items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h
m=pd.read_excel(src,sheet_name='04_质量变化').dropna(subset=['record_id']);m=m.dropna(subset=['observed_mass_g'])
for (g,day),df in m.groupby(['group_id','elapsed_days']):
 s=next(r for r in D['summary'] if (r['metric'],r['group'],r['day'])==('mass_loss',g,day))
 assert s['n_units']==len(df)==df.unit_id.nunique();close(s['mean'],df.mass_loss_pct.mean());close(s['sd'],df.mass_loss_pct.std(ddof=1))
q=pd.read_excel(src,sheet_name='06_品质检测');v=q[(q.record_status=='有效') & q.raw_value.notna()]
f=v.groupby(['unit_id','fruit_id','trait','group_id','batch_id','elapsed_days'],as_index=False).raw_value.mean()
u=f.groupby(['unit_id','trait','group_id','batch_id','elapsed_days'],as_index=False).raw_value.mean()
for row in u.itertuples():
 expected=next(x for x in D['unit_results'] if x['metric']==row.trait and x['unit_id']==row.unit_id)
 close(expected['value'],row.raw_value)
for (trait,g,day),df in u.groupby(['trait','group_id','elapsed_days']):
 s=next(r for r in D['summary'] if (r['metric'],r['group'],r['day'])==(trait,g,day))
 assert s['n_units']==len(df)==3;close(s['mean'],df.raw_value.mean());close(s['sd'],df.raw_value.std(ddof=1))
d=pd.read_excel(src,sheet_name='05_腐烂观察');d=d[d.cohort=='L'];assert len(d)==540
for (g,day),df in d.groupby(['group_id','elapsed_days']):
 s=next(r for r in D['summary'] if (r['metric'],r['group'],r['day'])==('decay_pct',g,day))
 assert len(df)==36 and s['denominator']==36 and s['decayed']==df.visible_decay_1_0.sum()
 unitpct=df.groupby('unit_id').visible_decay_1_0.mean()*100
 close(s['mean'],unitpct.mean());close(s['sd'],unitpct.std(ddof=1))
# Integrity of source rows behind every chart, and all 216 image status records.
for fig in D['figures']:
 if fig['id'][-3:]=='温湿度':assert fig['rows']==D['environment']
 elif '批次' in fig['id']:assert fig['rows']==[r for r in D['batch_summary'] if r['day']==4]
 else:
  metric={'P02_F01_失重率':'mass_loss','P02_F02_累计腐烂':'decay_pct','P02_F03_表观硬度':'firmness','P02_F04_TSS':'TSS'}[fig['id']]
  assert fig['rows']==[r for r in D['summary'] if r['metric']==metric]
 for name in fig['files']:
  path=R/'analysis/figures'/name;assert path.exists()
  if path.suffix=='.png':
   with Image.open(path) as im:assert im.width>=2000 and im.height>=1200;im.verify()
  else:etree.parse(str(path))
assert Counter(r['status'] for r in D['image_status'])=={'IMAGE_STATUS_UNKNOWN':216}
assert len({x['image_id'] for x in D['image_status']})==216
assert D['counts']['mass_valid']==134 and D['counts']['quality_valid']==237
# Local document links must exist, including literature sources and image assets.
for p in (R/'analysis').glob('PHASE_02_*.md'):
 text=p.read_text();assert text.count('```')%2==0
 for link in re.findall(r'\]\(([^)]+)\)',text):
  target=link.strip('<>').split('#')[0]
  if not target or '://' in target:continue
  assert (p.parent/target).resolve().exists(),(p.name,target)
 assert '水杨酸' not in text
assert len(D['new_summary_cache_checks'])==81
assert max(r['absolute_difference'] for r in D['new_summary_cache_checks'])<1e-7
print('PASS: independent pandas mass/quality/decay summaries; sample hierarchy; missingness; 6 chart sources/12 assets; 216 image states; local report links and input hashes.')
print('Pandas version',pd.__version__,'No formula-engine rerun, p values, or XLSX writes.')
