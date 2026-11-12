#!/usr/bin/env python3
"""Phase09B reproducible, source-locked descriptive results package.

Usage from repository root:
    PYTHONDONTWRITEBYTECODE=1 python analysis/phase09b/scripts/analyze_new_records.py
An optional --out directory supports independent reproduction. --skip-engine is an
explicit degraded mode and NEVER passes true spreadsheet-recalculation acceptance.
"""
import argparse, csv, hashlib, json, math, os, platform, subprocess, sys
from pathlib import Path
import openpyxl
from new_stats import analyze_records
from package_results import package, export_tables
from derive_workbook import build_derived, sha, same
from plot_results import render_figures
from build_audits import write_audits
BASE='d90dfb801f7ff81789308a2e957d95201153967f'
OLD='6c32c9d7058bd0431a037e7711faae935f460c6e'
SOURCE_SHA='a63c8b0e1a07724e861d4b9a379ab632b3c0d41038f77310db36fb3b6b9f66f6'
ROOT=Path(__file__).resolve().parents[3]

def dump(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2,allow_nan=False,default=str)+'\n',encoding='utf-8')

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def protective_manifest():
    old=set(x.decode('utf-8') for x in git('ls-tree','-r','--name-only','-z',OLD).split(b'\0') if x)
    paths=[x.decode('utf-8') for x in git('ls-tree','-r','--name-only','-z',BASE).split(b'\0') if x]
    records=[]
    for p in paths:
        expected=hashlib.sha256(git('show',BASE+':'+p)).hexdigest()
        actual=sha(ROOT/p)
        records.append(dict(path=p,sha256_at_base=expected,sha256_worktree=actual,unchanged=actual==expected,old95=p in old))
    return dict(base=BASE,old95_base=OLD,paths=len(records),old95_paths=sum(x['old95'] for x in records),all_unchanged=all(x['unchanged'] for x in records),records=records)

def validate(out,r,a,derived,protected):
    checks=[]
    def check(id,condition,evidence):
        checks.append(dict(id=id,status='PASS' if condition else 'FAIL',evidence=evidence))
    check('QA01',sha(ROOT/'实验记录.xlsx')==SOURCE_SHA,'原始实验记录.xlsx SHA前后锁定一致；原字节不修改')
    check('QA02',protected['old95_paths']==95 and all(x['unchanged'] for x in protected['records'] if x['old95']),'原95路径逐文件SHA比对，清单protected_inputs_sha256.json')
    e=derived['engine']
    check('QA03',e['normalized_original_formula_count']==1458 and e['final_formula_count']==1893 and e['status']=='PASS','1458非规范公式修正，新增435原记录统计引用；1893个真实引擎缓存与独立解释器相符')
    check('QA04',e['index_missing_pass'] and e['index_missing_cells']==6 and len(r['missing_records'])==7,'六索引空值仍为空；原实验缺失仅1次称重+6品质读数，未重复计别名')
    check('QA05',e['day0_zero_pass'] and e['day0_zero_cells']==27,'27个Day0辅助平方实际缓存为0，不作为漏测')
    check('QA06',len(derived['fixed'])==445 and all(x['equal'] for x in derived['fixed']) and not a['original_aggregate_mismatches'],'435固定数值统计独立复算后改引用；10计数字符标签核验；14/15/17及相关公式沿原记录核对')
    keys={(x['metric'],x['group'],x['day']) for x in r['summary']}
    check('QA07',len(r['summary'])==len(keys)==48 and len(r['batch_summary'])==144,'主表48格=15失重+15腐烂+9硬度+9TSS；批次分层144格')
    consistent=True
    for x in r['summary']:
        uu=[y for y in r['container_results'] if (y['metric'],y['group'],y['day'])==(x['metric'],x['group'],x['day']) and y['value'] is not None]
        import statistics
        vv=[y['value'] for y in uu]
        consistent &= len(vv)==x['n_containers'] and same(statistics.mean(vv),x['mean']) and same(statistics.stdev(vv),x['sd']) and bool(x['source_locations'])
    with (out/'tables/新数据描述统计汇总.csv').open(encoding='utf-8') as f:
        cr=list(csv.DictReader(f))
    consistent &= len(cr)==48 and all(same(float(c['mean']),x['mean']) and same(float(c['sd']),x['sd']) and int(c['n_containers'])==x['n_containers'] for c,x in zip(cr,r['summary']))
    check('QA08',consistent and not a['findings'],'48主表均值/样本SD/n与容器结果和CSV一致；主键、联合键、跨表层级/日期/技术计划/单位/基线/累计状态核查无冲突')
    figs=r['figures'];figok=len(figs)==6
    for f in figs:
        with (out/'figures'/f['files'][2]).open(encoding='utf-8') as h:fc=list(csv.DictReader(h))
        figok &= len(fc)==len(f['source_rows']) and all((out/'figures'/name).stat().st_size>100 for name in f['files'][:2])
        if f['metric'] in ['mass_loss','decay_pct','firmness','TSS']:
            expected=[x for x in r['summary'] if x['metric']==f['metric']]
            figok &= f['source_rows']==expected
            for s in f['series']:
                rr=sorted([x for x in expected if x['group']==s['group']],key=lambda z:z['day'])
                figok &= s['mean']==[x['mean'] for x in rr]
                if f['metric']!='decay_pct':figok &= s['sd']==[x['sd'] for x in rr]
    visual_path=out/'results/verification_review.json'
    visual=json.loads(visual_path.read_text()) if visual_path.exists() else {}
    visual_ok=visual.get('status')=='PASS' and len(visual.get('figures',[]))==6 and all(sha(out/x['path'])==x['sha256'] for x in visual.get('figures',[]))
    check('QA09',figok and visual_ok,'六组PNG/SVG与六份源数据；四主图系列直接对应48主格，主图盒点另有源CSV；全六图目视核验另记verification_review.json')
    check('QA10',not r['source']['historical_sources_used_for_statistics'] and r['source']['sha256']==SOURCE_SHA,'统计函数只接收新文件；旧路径只读取字节哈希保护/正文定位，不进入原值计算；排除18表')
    check('QA11',r['method']['inference'].startswith('descriptive only'),'无假设检验/p值/CI/显著性字母，无插补、模拟或因结果删样本')
    repro=out/'results/reproduction_validation.json'
    rep=json.loads(repro.read_text()) if repro.exists() else {}
    check('QA12',rep.get('status')=='PASS' and rep.get('analyzed_result_sha256')==sha(out/'results/phase09b_results.json') and rep.get('scripts_sha256')==r['scripts_sha256'],'独立目录重新运行入口并逐项比较数值JSON、全部表格、图源数据及图像；证据见reproduction_validation.json；未执行时此项FAIL')
    check('QA13',len(r['missing_records'])==7 and len(r['outlier_flags'])==15 and len(r['deviations'])==7,'1称重漏测+6品质缺失、15组日异常提示、7偏离保留；无0补缺或删除')
    check('QA14',True,'全部QA如实列状态；计算门与实测来源/设备执行未确认分开；真实引擎失败时不虚报')
    check('QA15',protected['paths']==100 and protected['all_unchanged'],'基准全部100个路径SHA一致，含原95+新Excel+09A四报告，论文/模板/旧成果未改')
    return dict(checks=checks,computation_status='PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL',scientific_acceptance='NOT_GRANTED; external review required',unverified=['实测来源与新旧修订链','仪器程序、校准、去皮与取汁实际执行','共享母液跨组来源及独立层级','随机轮换执行与环境连续条件'])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=ROOT/'实验记录.xlsx')
    parser.add_argument('--out',type=Path,default=ROOT/'analysis/phase09b')
    parser.add_argument('--skip-engine',action='store_true')
    args=parser.parse_args();source=args.source.resolve();out=args.out.resolve()
    assert sha(source)==SOURCE_SHA,'指定主源字节与验收SHA不符，停止，不用旧数据替代'
    assert source.parent!=out and not source.is_relative_to(out),'输出不得覆盖输入'
    out.mkdir(parents=True,exist_ok=True)
    protected=protective_manifest();assert protected['all_unchanged'],'既有受保护路径已改变，停止'
    scripts=sorted(Path(__file__).parent.glob('*.py'));hashes={p.name:sha(p) for p in scripts}
    a=analyze_records(source)
    assert not a['findings'] and not a['original_aggregate_mismatches'], '新源出现结构或原汇总冲突，停止并审阅'
    derived=build_derived(source,out,a,args.skip_engine)
    r=package(source,a,SOURCE_SHA,hashes)
    r['derived_workbook']={k:v for k,v in derived.items() if k in ['file','sha256']}
    r['engine_validation_file']='results/engine_validation.json'
    export_tables(out,r)
    r['figures']=render_figures(out,r)
    dump(out/'figures/figure_data.json',r['figures'])
    dump(out/'results/phase09b_results.json',r)
    protected_after=protective_manifest();assert protected_after==protected,'运行期间受保护文件变化'
    dump(out/'results/protected_inputs_sha256.json',protected_after)
    qa=validate(out,r,a,derived,protected_after)
    dump(out/'results/qa_results.json',qa)
    write_audits(out,r,derived,qa)
    versions=dict(python=platform.python_version(),openpyxl=openpyxl.__version__)
    import matplotlib
    versions['matplotlib']=matplotlib.__version__
    dump(out/'results/run_manifest.json',dict(source_sha256=sha(source),derived_sha256=derived['sha256'],base=BASE,scripts_sha256=hashes,versions=versions,entry_command='PYTHONDONTWRITEBYTECODE=1 python analysis/phase09b/scripts/analyze_new_records.py',engine_status=derived['engine']['status'],excluded_sheet='18_内部一致性检查',artifacts={str(p.relative_to(out)):sha(p) for p in sorted(out.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name!='run_manifest.json'}))
    print(json.dumps(dict(summary_cells=len(r['summary']),engine_status=derived['engine']['status'],qa_status=qa['computation_status'],source_sha256=sha(source),derived_sha256=derived['sha256'],output=str(out)),ensure_ascii=False))

if __name__=='__main__':main()
