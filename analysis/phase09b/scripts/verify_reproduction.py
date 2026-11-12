#!/usr/bin/env python3
"""Re-run the full package in an independent directory and verify raw-to-summary math.

Uses a separately implemented NumPy path (no new_stats/package_results calculations)
for all 48 primary cells, including SD, n, and provenance coverage. Then updates
QA and reports without any source edits or additional statistical inference.
"""
import argparse, collections, csv, json, os, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
import openpyxl
import analyze_new_records as main
from derive_workbook import sha
from new_stats import analyze_records
from build_audits import write_audits

def independent_numpy(source,result):
    w=openpyxl.load_workbook(source,read_only=True,data_only=True)
    # Explicitly select raw sheets; no formula caches or excluded-sheet data.
    units={x[1]:x for x in w['04_实验单位'].iter_rows(min_row=5,values_only=True) if x[0] is not None}
    mass=[x for x in w['07_连续称重'].iter_rows(min_row=5,values_only=True) if x[0] is not None]
    decay=[x for x in w['08_腐烂观察'].iter_rows(min_row=5,values_only=True) if x[0] is not None and x[7]=='L']
    quality=[x for x in w['09_品质检测'].iter_rows(min_row=5,values_only=True) if x[0] is not None]
    failures=[];checked=0
    for target in result['summary']:
        metric,g,d=target['metric'],target['group'],target['day']
        values=[];nfruit=0;nread=0
        if metric=='mass_loss':
            for x in mass:
                if x[5]==g and x[2]==d and x[8] is not None:
                    values.append(100*(1-x[8]/x[7]));nfruit+=units[x[4]][4];nread+=1
        elif metric=='decay_pct':
            for uid,u in units.items():
                if u[2]!=g or u[3]!='L':continue
                xx=[x for x in decay if x[4]==uid and x[2]==d]
                values.append(100*np.asarray([x[8] for x in xx],dtype=float).sum()/u[4]);nfruit+=len(xx);nread+=len(xx)
        else:
            for uid,u in units.items():
                if u[2]!=g or u[3]!='D'+str(d):continue
                selected=[x for x in quality if x[4]==uid and x[7]==metric and x[8] is not None]
                byfruit=collections.defaultdict(list)
                for x in selected:byfruit[x[5]].append(float(x[8]))
                vv=[np.asarray(v).mean() for v in byfruit.values()]
                if vv:values.append(float(np.asarray(vv).mean()))
                nfruit+=len(vv);nread+=len(selected)
        a=np.asarray(values,dtype=float)
        obtained={'mean':float(a.mean()),'sd':float(a.std(ddof=1)),'min':float(a.min()),'max':float(a.max()),'n_containers':len(a),'n_fruits':nfruit,'n_readings':nread}
        for field,value in obtained.items():
            if not np.isclose(value,target[field],rtol=1e-10,atol=1e-10):failures.append(dict(metric=metric,group=g,day=d,field=field,independent=value,result=target[field]))
        checked+=1
    w.close()
    return dict(status='PASS' if not failures else 'FAIL',primary_cells=checked,fields=['mean','sd','min','max','n_containers','n_fruits','n_readings'],numpy_version=np.__version__,failures=failures)

def refresh_manifest(out):
    p=out/'results/run_manifest.json';m=json.loads(p.read_text())
    m['artifacts']={str(p.relative_to(out)):sha(p) for p in sorted(out.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.name!='run_manifest.json'}
    main.dump(out/'results/run_manifest.json',m)

def run(out,repeat_dir=None):
    result=json.loads((out/'results/phase09b_results.json').read_text())
    assert result['scripts_sha256']=={p.name:sha(p) for p in Path(__file__).parent.glob('*.py')},'代码已变更，应先重新运行入口再核验'
    independent=independent_numpy(main.ROOT/'实验记录.xlsx',result)
    main.dump(out/'results/independent_numpy_validation.json',independent)
    if repeat_dir is None:
        repeat_dir=Path(tempfile.mkdtemp(prefix='phase09b_reproduce_'))
    repeat_dir=Path(repeat_dir).resolve()
    env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';env.setdefault('XDG_CACHE_HOME','/tmp/phase09b/cache')
    cmd=[sys.executable,str(Path(__file__).with_name('analyze_new_records.py')),'--out',str(repeat_dir)]
    proc=subprocess.run(cmd,capture_output=True,text=True,env=env,timeout=360)
    other=repeat_dir/'results/phase09b_results.json'
    mismatches=[];comparisons=[]
    if proc.returncode==0 and other.exists():
        reproduced=json.loads(other.read_text())
        if result!=reproduced:
            mismatches += ['results.json:'+k for k in result if result[k]!=reproduced.get(k)]
        files=[out/'实验记录_派生计算修订副本.xlsx',*sorted((out/'tables').glob('*.csv')),*sorted((out/'figures').glob('*'))]
        for p in files:
            rel=p.relative_to(out);q=repeat_dir/rel;equal=q.exists() and sha(p)==sha(q)
            comparisons.append(dict(path=str(rel),sha256=sha(p),reproduced_sha256=sha(q) if q.exists() else None,byte_equal=equal))
            if not equal:mismatches.append(str(rel))
        engine=json.loads((repeat_dir/'results/engine_validation.json').read_text())
        if engine['status']!='PASS':mismatches.append('reproduced_engine')
    else:mismatches.append('entry_process_or_results_missing')
    rep=dict(analyzed_result_sha256=sha(out/'results/phase09b_results.json'),scripts_sha256=result['scripts_sha256'],status='PASS' if not mismatches and independent['status']=='PASS' else 'FAIL',entry_command='PYTHONDONTWRITEBYTECODE=1 python analysis/phase09b/scripts/analyze_new_records.py --out <independent temporary directory>',returncode=proc.returncode,stdout=proc.stdout.replace(str(repeat_dir),'<independent temporary directory>'),stderr=proc.stderr.replace(str(repeat_dir),'<independent temporary directory>'),numeric_json_equal=not any(s.startswith('results.json:') for s in mismatches) and other.exists(),independent_numpy_status=independent['status'],independent_primary_cells=48,compared_artifacts=comparisons,mismatches=mismatches,interpretation='Reproducibility of calculations and exported coordinates is not independent proof of measurement provenance.')
    main.dump(out/'results/reproduction_validation.json',rep)
    a=analyze_records(main.ROOT/'实验记录.xlsx')
    derived=dict(file='实验记录_派生计算修订副本.xlsx',sha256=sha(out/'实验记录_派生计算修订副本.xlsx'),engine=json.loads((out/'results/engine_validation.json').read_text()))
    with (out/'tables/固定汇总复核.csv').open(encoding='utf-8') as f:derived['fixed']=[dict(x,equal=x['equal']=='True') for x in csv.DictReader(f)]
    protected=main.protective_manifest();assert protected['all_unchanged']
    qa=main.validate(out,result,a,derived,protected)
    main.dump(out/'results/qa_results.json',qa)
    write_audits(out,result,derived,qa)
    refresh_manifest(out)
    print(json.dumps(dict(reproduction=rep['status'],independent_numpy=independent['status'],qa=qa['computation_status'],mismatches=mismatches),ensure_ascii=False))
    return rep

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=main.ROOT/'analysis/phase09b');p.add_argument('--repeat-dir',type=Path);args=p.parse_args()
    report=run(args.out.resolve(),args.repeat_dir)
    raise SystemExit(0 if report['status']=='PASS' else 1)
