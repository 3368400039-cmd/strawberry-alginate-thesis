"""Phase 02 descriptive analysis. Read-only XLSX inputs; no formula-engine rerun or p values.
Run from any directory: python analysis/scripts/analyze_phase02.py
Outputs: phase02_results.json and six PNG/SVG figure pairs in ../figures.
"""
from pathlib import Path
import os,json,hashlib,platform
from collections import Counter,defaultdict
from statistics import mean,stdev,median
import openpyxl,numpy as np
os.environ.setdefault('MPLCONFIGDIR','/tmp/thesis-phase02-mpl')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/thesis-phase02-cache')
for key in ['MPLCONFIGDIR','XDG_CACHE_HOME']:Path(os.environ[key]).mkdir(parents=True,exist_ok=True)
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt,font_manager
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent;FIG=ROOT/'analysis/figures';FIG.mkdir(exist_ok=True)
SRC=ROOT/'analysis/研究数据_公式修复核验副本.xlsx';RAW=ROOT/'研究数据S1.xlsx'
EXPECTED={'研究数据S1.xlsx':'7ffc712bbfd8648fbd359a3bf26e6af75af2a21fde7b7be801c862546d3cb550','analysis/研究数据_公式修复核验副本.xlsx':'9167c63e20dc6f9d6a454981620644897a631c653f861309bb90d66da0f298f2'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for path,digest in EXPECTED.items():assert sha(ROOT/path)==digest,'Unexpected source version: '+path
w=openpyxl.load_workbook(SRC,data_only=True) # use previously verified caches; do not rerun 582 formulas
G=['CK','Ca','SA-Ca'];B=['B1','B2','B3']
def records(sn):
 s=w[sn];heads=[c.value for c in s[1]]
 return [dict(zip(heads,row))|{'source_row':i,'source_sheet':sn} for i,row in enumerate(s.iter_rows(min_row=2,values_only=True),2) if row[0] is not None]
units=records('01_实验单位');fruit=records('02_果实清单');treat=records('03_处理记录');mass=records('04_质量变化');decay=records('05_腐烂观察');quality=records('06_品质检测');env=records('07_环境记录');deviations=records('08_偏离记录')
U={r['unit_id']:r for r in units}
assert len(units)==54 and len(fruit)==189
for r in treat:assert (r['SA_conc_w_w_pct'],r['CaCl2_conc_w_w_pct'])=={'CK':(0,0),'Ca':(0,1),'SA-Ca':(1.5,1)}[r['group_id']]
# Explicit aggregation hierarchy: technical readings -> fruit -> container.
qfruit=[]
for (f,trait),rs in __import__('itertools').groupby(sorted(quality,key=lambda r:(r['fruit_id'],r['trait'])),key=lambda r:(r['fruit_id'],r['trait'])):
 rs=list(rs);valid=[r for r in rs if r['record_status']=='有效' and isinstance(r['raw_value'],(int,float))]
 qfruit.append({'fruit_id':f,'unit_id':rs[0]['unit_id'],'trait':trait,'day':rs[0]['elapsed_days'],'group':rs[0]['group_id'],'batch':rs[0]['batch_id'],'n_reads':len(valid),'value':mean(r['raw_value'] for r in valid) if valid else None,'source_rows':[r['source_row'] for r in rs]})
qunit=[]
for u in units:
 if u['cohort']=='L':continue
 for trait in ['firmness','TSS']:
  fs=[f for f in qfruit if f['unit_id']==u['unit_id'] and f['trait']==trait];vs=[f['value'] for f in fs if f['value'] is not None]
  qunit.append({'metric':trait,'unit_id':u['unit_id'],'group':u['group_id'],'batch':u['batch_id'],'day':int(u['cohort'][1:]),'value':mean(vs) if vs else None,'n_fruits':len(vs),'n_reads':sum(f['n_reads'] for f in fs),'nominal_fruits':3,'source_rows':[row for f in fs for row in f['source_rows']]})
# L mass percentages retain original two-decimal unit-level rounding.
munit=[{'metric':'mass_loss','unit_id':r['unit_id'],'group':r['group_id'],'batch':r['batch_id'],'day':r['elapsed_days'],'value':r['mass_loss_pct'] if r['observed_mass_g'] is not None else None,'n_fruits':r['fruit_count'] if r['observed_mass_g'] is not None else 0,'n_reads':int(r['observed_mass_g'] is not None),'nominal_fruits':r['fruit_count'],'source_rows':[r['source_row']]} for r in mass]
dunit=[]
for u in units:
 if u['cohort']!='L':continue
 for day in range(5):
  rs=[r for r in decay if r['unit_id']==u['unit_id'] and r['elapsed_days']==day]
  assert len(rs)==u['fruit_count_initial']==4
  k=sum(r['visible_decay_1_0'] for r in rs)
  dunit.append({'metric':'decay_pct','unit_id':u['unit_id'],'group':u['group_id'],'batch':u['batch_id'],'day':day,'value':100*k/u['fruit_count_initial'],'decayed':k,'denominator':u['fruit_count_initial'],'n_fruits':len(rs),'n_reads':len(rs),'nominal_fruits':4,'source_rows':[r['source_row'] for r in rs]})
allunits=munit+dunit+qunit
MET=['mass_loss','decay_pct','firmness','TSS']
def summarize(rs):
 valid=[r for r in rs if r['value'] is not None];vals=[r['value'] for r in valid]
 return {'n_units':len(vals),'n_fruits':sum(r['n_fruits'] for r in valid),'n_reads':sum(r['n_reads'] for r in valid),'mean':mean(vals) if vals else None,'sd':stdev(vals) if len(vals)>1 else None,'median':median(vals) if vals else None,'min':min(vals) if vals else None,'max':max(vals) if vals else None,'unit_ids':[r['unit_id'] for r in valid]}
summary=[];batch_summary=[]
for metric in MET:
 for g in G:
  for day in (range(5) if metric in MET[:2] else [0,2,4]):
   rs=[r for r in allunits if r['metric']==metric and r['group']==g and r['day']==day]
   row={'metric':metric,'group':g,'day':day,**summarize(rs)}
   if metric=='decay_pct':row.update(decayed=sum(r['decayed'] for r in rs),denominator=sum(r['denominator'] for r in rs));assert abs(row['mean']-100*row['decayed']/row['denominator'])<1e-12
   summary.append(row)
   for batch in B:batch_summary.append({'metric':metric,'group':g,'day':day,'batch':batch,**summarize([r for r in rs if r['batch']==batch])})
# New statistical aggregates vs already-verified summary caches, not formula revalidation.
cache_checks=[]
def check(label,a,b):
 assert a is not None and b is not None and abs(a-b)<1e-7,(label,a,b)
 cache_checks.append({'item':label,'computed':a,'existing_cache':b,'absolute_difference':abs(a-b)})
for i,row in enumerate(w['10_描述统计'].iter_rows(min_row=5,max_row=19,values_only=True),5):
 g,day=row[:2]
 for metric,fields in [('mass_loss',[('mean',3),('sd',4)]),('decay_pct',[('mean',7)])]:
  s=next(s for s in summary if s['metric']==metric and s['group']==g and s['day']==day)
  for field,col in fields:check(f'10!{i}/{metric}/{field}',s[field],row[col])
for i,row in enumerate(w['11_品质汇总'].iter_rows(min_row=5,max_row=13,values_only=True),5):
 for metric,fields in [('firmness',[('mean',3),('sd',4)]),('TSS',[('mean',6),('sd',7)])]:
  s=next(s for s in summary if s['metric']==metric and s['group']==row[0] and s['day']==row[1])
  for field,col in fields:check(f'11!{i}/{metric}/{field}',s[field],row[col])
assert len(cache_checks)==81
# Equal-date-batch weighting and leave-one-batch-out are descriptive sensitivity, not intervals.
sensitivity=[]
for s in summary:
 bs=[b for b in batch_summary if all(b[k]==s[k] for k in ['metric','group','day'])];vals=[b['mean'] for b in bs]
 sensitivity.append({'metric':s['metric'],'group':s['group'],'day':s['day'],'container_weighted':s['mean'],'equal_batch':mean(vals),'difference':mean(vals)-s['mean']})
quality_weight_sensitivity=[]
for s in summary:
 if s['metric'] not in ['firmness','TSS']:continue
 fs=[r for r in qfruit if r['trait']==s['metric'] and r['group']==s['group'] and r['day']==s['day'] and r['value'] is not None]
 fm=mean(r['value'] for r in fs)
 quality_weight_sensitivity.append({'metric':s['metric'],'group':s['group'],'day':s['day'],'container_equal_mean':s['mean'],'fruit_equal_mean':fm,'difference':fm-s['mean'],'valid_fruits':len(fs)})
day_changes=[]
for metric in MET:
 for g in G:
  end=next(r for r in summary if (r['metric'],r['group'],r['day'])==(metric,g,4))
  start=next(r for r in summary if (r['metric'],r['group'],r['day'])==(metric,g,0))
  day_changes.append({'metric':metric,'group':g,'day4_minus_day0':end['mean']-start['mean'],'interpretation':'different D containers' if metric in ['firmness','TSS'] else 'same L containers'})
contrasts=[]
for metric in MET:
 for a,b in [('SA-Ca','Ca'),('SA-Ca','CK'),('Ca','CK')]:
  pairs=[]
  for batch in B:
   x=next(r['mean'] for r in batch_summary if (r['metric'],r['group'],r['day'],r['batch'])==(metric,a,4,batch));y=next(r['mean'] for r in batch_summary if (r['metric'],r['group'],r['day'],r['batch'])==(metric,b,4,batch));pairs.append(x-y)
  contrasts.append({'metric':metric,'contrast':a+' - '+b,'day':4,'B1':pairs[0],'B2':pairs[1],'B3':pairs[2],'mean_delta':mean(pairs),'sd_delta':stdev(pairs),'min_delta':min(pairs),'max_delta':max(pairs),'leave_one_batch_out_min':min(mean(pairs[:i]+pairs[i+1:]) for i in range(3)),'leave_one_batch_out_max':max(mean(pairs[:i]+pairs[i+1:]) for i in range(3))})
envs=[]
for batch in B+['ALL']:
 rs=env if batch=='ALL' else [r for r in env if r['batch_id']==batch]
 for field in ['temperature_C','relative_humidity_pct']:
  vals=[r[field] for r in rs];envs.append({'batch':batch,'metric':field,'n_records':len(vals),'mean':mean(vals),'sd':stdev(vals),'min':min(vals),'max':max(vals),'outside_target':sum(x<23 or x>25 for x in vals) if field=='temperature_C' else None})
first=Counter((r['group_id'],r['elapsed_days']) for r in decay if r['cohort']=='L' and r['first_decay_1_0']==1)
images=defaultdict(list)
for sn,col,rs in [('04_质量变化','photo_ref',mass),('05_腐烂观察','photo_ref',decay)]:
 for r in rs:
  if r[col]:images[r[col]].append(f"{sn}!{'L' if sn.startswith('04') else 'M'}{r['source_row']}")
image_status=[{'image_id':ref,'status':'IMAGE_STATUS_UNKNOWN','accessible_in_supplied_files':False,'source_cells':cells} for ref,cells in images.items()]
assert len(image_status)==216
qmissing=[{'source_row':r['source_row'],'fruit_id':r['fruit_id'],'unit_id':r['unit_id'],'trait':r['trait'],'reason':r['record_status']} for r in quality if r['raw_value'] is None]
counts={'units':len(units),'fruit':len(fruit),'L_units':sum(u['cohort']=='L' for u in units),'D_units':sum(u['cohort']!='L' for u in units),'mass_planned':len(mass),'mass_valid':sum(r['observed_mass_g'] is not None for r in mass),'L_decay_events':sum(r['cohort']=='L' for r in decay),'quality_planned':len(quality),'quality_valid':sum(r['raw_value'] is not None for r in quality),'quality_missing':len(qmissing)}
# Charts: every plotted number is taken from the exported summary/unit rows.
font=Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
if font.exists():font_manager.fontManager.addfont(str(font));plt.rcParams['font.family']=font_manager.FontProperties(fname=str(font)).get_name()
plt.rcParams.update({'font.size':11,'axes.titlesize':14,'axes.labelsize':12,'axes.unicode_minus':False,'svg.fonttype':'none','savefig.facecolor':'white'})
COL={'CK':'#3C658A','Ca':'#B07A19','SA-Ca':'#B34F79'};MARK={'CK':'o','Ca':'s','SA-Ca':'^'};LS={'CK':'-','Ca':'--','SA-Ca':'-.'}
labels={'mass_loss':'失重率 / %','decay_pct':'累计腐烂率 / %','firmness':'表观硬度 / N','TSS':'TSS / °Brix'}
figure_metadata=[]
def style(ax):
 ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',color='#e5e5e5',lw=.7);ax.set_axisbelow(True)
def save(fig,name,rows,note):
 fig.savefig(FIG/(name+'.png'),dpi=240);fig.savefig(FIG/(name+'.svg'));plt.close(fig)
 svg=FIG/(name+'.svg');svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines()).rstrip()+'\n')
 figure_metadata.append({'id':name,'files':[name+'.png',name+'.svg'],'source':'analysis/研究数据_公式修复核验副本.xlsx','rows':rows,'note':note})
for metric,name,title,ylim in [('mass_loss','P02_F01_失重率','L队列：失重率随贮藏时间变化',(0,11)),('decay_pct','P02_F02_累计腐烂','L队列：累计腐烂情况',(0,105)),('firmness','P02_F03_表观硬度','D队列：表观硬度随取样日变化',(0,13)),('TSS','P02_F04_TSS','D队列：可溶性固形物随取样日变化',(0,11))]:
 fig,ax=plt.subplots(figsize=(9.2,5.9));plotrows=[r for r in summary if r['metric']==metric]
 for g in G:
  rows=sorted([r for r in plotrows if r['group']==g],key=lambda r:r['day']);xs=[r['day'] for r in rows];ys=[r['mean'] for r in rows]
  if metric=='decay_pct':ax.plot(xs,ys,color=COL[g],marker=MARK[g],ls=LS[g],label=g,lw=1.8)
  else:ax.errorbar(xs,ys,yerr=[r['sd'] for r in rows],color=COL[g],marker=MARK[g],ls=LS[g],label=g,capsize=3,lw=1.8)
  # D-unit points display the three source-batch containers; L decay shows observed unit proportions.
  if metric in ['decay_pct','firmness','TSS']:
   rs=[r for r in allunits if r['metric']==metric and r['group']==g and r['value'] is not None]
   for x in rs:
    offset=(G.index(g)-1)*.06
    ax.scatter(x['day']+offset,x['value'],color=COL[g],marker=MARK[g],s=23,alpha=.42,zorder=2,edgecolors='none')
 ax.set(xlabel=('贮藏时间 / d（Day0为处理后基线）' if metric in MET[:2] else '取样日 / d（不同D容器，非同果重复）'),ylabel=labels[metric],title=title,ylim=ylim,xticks=list(range(5)) if metric in MET[:2] else [0,2,4]);style(ax);ax.legend(ncol=3,loc='upper center',frameon=False)
 note={'mass_loss':'点/线：容器均值；误差线：容器间样本SD；每组n=9容器，Ca Day2 n=8。','decay_pct':'线：累计腐烂果数/初始36果；散点：各容器比例（每组9盒×4果）；无推断区间。','firmness':'线：容器均值±样本SD；点：3批次的D容器均值；每组每时点n=3容器。','TSS':'线：容器均值±样本SD；点：3批次的D容器均值；仅代表可检测果。'}[metric]
 fig.text(.5,.025,note,ha='center',fontsize=10);fig.subplots_adjust(bottom=.19,top=.89,left=.12,right=.96)
 save(fig,name,plotrows,note)
fig,axs=plt.subplots(2,2,figsize=(11,8.4))
for ax,metric in zip(axs.flat,MET):
 for g in G:
  rs=[next(r for r in batch_summary if (r['metric'],r['group'],r['day'],r['batch'])==(metric,g,4,b)) for b in B]
  ax.plot(B,[r['mean'] for r in rs],marker=MARK[g],ls=LS[g],color=COL[g],label=g,lw=1.7)
 ax.set(title='Day4 '+labels[metric],xlabel='实验日期批次',ylabel=labels[metric]);style(ax)
 ax.set_ylim(0,100 if metric=='decay_pct' else 13 if metric=='firmness' else 11)
axs[0,0].legend(ncol=3,frameon=False,fontsize=10);fig.suptitle('Day4结果的批次差异（描述性）',y=.98,fontsize=16)
fig.text(.5,.025,'各点：批次×组别的容器均值；L每格3盒，D每格1盒；连线用于辨别批次，非同一果的时间轨迹。',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.06,1,.95]);save(fig,'P02_F05_批次差异',[r for r in batch_summary if r['day']==4],'No intervals; batch-specific means; D n=1 per batch/group/time.')
fig,axs=plt.subplots(2,1,figsize=(10,7),sharex=True)
for i,field in enumerate(['temperature_C','relative_humidity_pct']):
 for batch,col,mark in zip(B,['#3C658A','#B07A19','#B34F79'],['o','s','^']):
  rs=sorted([r for r in env if r['batch_id']==batch],key=lambda r:r['recorded_at']);start=rs[0]['recorded_at'];x=[(r['recorded_at']-start).total_seconds()/86400 for r in rs]
  axs[i].plot(x,[r[field] for r in rs],marker=mark,ms=4,color=col,label=batch,lw=1.4)
 axs[i].set(ylabel='温度 / ℃' if i==0 else '相对湿度 / %RH');style(axs[i])
axs[0].axhspan(23,25,color='#aaaaaa',alpha=.14,label='目标23—25℃');axs[0].legend(ncol=4,frameon=False,fontsize=10)
axs[1].set(xlabel='相对Day0 09:00的贮藏日 / d',xticks=[0,1,2,3,4],ylim=(55,85));axs[0].set(title='实际贮藏环境记录（每日09:00、17:00）',ylim=(21,27))
fig.text(.5,.015,'每批10条记录；阴影是目标温度范围，不是实际测量误差带；未设定湿度恒定。',ha='center',fontsize=10)
fig.tight_layout(rect=[0,.04,1,1]);save(fig,'P02_F06_温湿度',env,'Actual environmental records, not treatment-specific replicates.')
raw_ranges={trait:{'n_reads':sum(r['raw_value'] is not None for r in quality if r['trait']==trait),'min':min(r['raw_value'] for r in quality if r['trait']==trait and r['raw_value'] is not None),'max':max(r['raw_value'] for r in quality if r['trait']==trait and r['raw_value'] is not None)} for trait in ['firmness','TSS']}
result={'input_hashes':EXPECTED,'source_revision':'6f07d97c71e989898af45dd2d93597f109bfbe00','researcher_addendum':{'filename':'已粘贴的文本.txt','sha256':'dc05561e463f0139ae05393318ee40fb8f8c2d9fbc5c5a9dcb5e15e819cfda68','date':'2026-11-10','evidence_status':'researcher_supplied_statement_not_independently_verified'},'method':'Descriptive container summaries; shared parent solution by batch and treatment; no significance testing.','versions':{'python':platform.python_version(),'openpyxl':openpyxl.__version__,'numpy':np.__version__,'matplotlib':matplotlib.__version__},'counts':counts,'units':units,'treatments':treat,'unit_results':allunits,'fruit_quality':qfruit,'summary':summary,'batch_summary':batch_summary,'equal_batch_sensitivity':sensitivity,'day4_batch_contrasts':contrasts,'quality_weight_sensitivity':quality_weight_sensitivity,'day_changes':day_changes,'environment':env,'environment_summary':envs,'deviations':deviations,'quality_missing':qmissing,'first_decay_counts':[{'group':g,'day':day,'new_cases':first[g,day]} for g in G for day in range(5)],'image_status':image_status,'raw_quality_ranges':raw_ranges,'new_summary_cache_checks':cache_checks,'figures':figure_metadata}
(OUT/'phase02_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str,allow_nan=False)+'\n')
for path,digest in EXPECTED.items():assert sha(ROOT/path)==digest
print('COUNTS',counts)
print('DAY4 CONTRASTS',json.dumps(contrasts,ensure_ascii=False,indent=2))
print('ENV',envs)
print('SENSITIVITY max',max(sensitivity,key=lambda r:abs(r['difference'])))
print('Wrote result JSON and 6 PNG/SVG figure pairs; 81 new aggregation checks passed; no p values.')
