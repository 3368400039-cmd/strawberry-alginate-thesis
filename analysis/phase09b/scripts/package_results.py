"""Package source-only descriptive statistics with explicit grains and provenance."""
import datetime, statistics, collections, csv, json, hashlib
from pathlib import Path
GROUPS = ['CK', 'Ca', 'SA-Ca']
METRICS = ['mass_loss', 'decay_pct', 'firmness', 'TSS']
LABELS = {'mass_loss': '失重率', 'decay_pct': '累计腐烂比例', 'firmness': '表观硬度', 'TSS': '可溶性固形物TSS'}
UNITS = {'mass_loss': '%', 'decay_pct': '%', 'firmness': 'N', 'TSS': '°Brix'}
BATCH_START = {'B1': '2026-10-05', 'B2': '2026-10-13', 'B3': '2026-10-21'}

def write_csv(path, rows, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False, separators=(',', ':')) if isinstance(v, (dict, list, tuple)) else v for k, v in r.items() if k in fields})

def package(source, a, source_sha, code_hashes):
    raw = a['raw']
    units = {u['B']: u for u in raw['04_实验单位']}
    unit = []
    for metric, rr in [('mass_loss', a['mass']), ('decay_pct', a['decay']), ('quality', a['quality_units'])]:
        for x in rr:
            r = x.copy()
            r['metric'] = x.get('metric', metric)
            r['unit_of_measure'] = UNITS[r['metric']]
            r['date'] = (datetime.date.fromisoformat(BATCH_START[r['batch']]) + datetime.timedelta(days=r['day'])).isoformat()
            if metric == 'mass_loss':
                r['n_fruits'] = 4 if r['value'] is not None else 0
                r['n_reads'] = int(r['value'] is not None)
            if metric == 'decay_pct':
                r['n_fruits'] = r['denom']
                r['n_reads'] = r['denom']
            if metric == 'quality':
                r['sources'] = [s for f in a['fruit_quality'] if f['unit'] == r['unit'] and f['metric'] == r['metric'] for s in f['source']]
            unit.append(r)

    def group_summary(metric, g, day, batch=None):
        allu = [r for r in unit if r['metric'] == metric and r['group'] == g and (r['day'] == day) and (batch is None or r['batch'] == batch)]
        valid = [r for r in allu if r['value'] is not None]
        vv = [r['value'] for r in valid]
        if metric == 'mass_loss':
            sources = [r for r in raw['07_连续称重'] if r['F'] == g and r['C'] == day and (batch is None or r['D'] == batch)]
            locs = ['07_连续称重!H' + str(r['row']) + ':I' + str(r['row']) for r in sources]
            dates = sorted(set((str(r['B'])[:10] for r in sources)))
            missing = sum((r['I'] is None for r in sources))
        elif metric == 'decay_pct':
            sources = [r for r in raw['08_腐烂观察'] if r['G'] == g and r['C'] == day and (r['H'] == 'L') and (batch is None or r['D'] == batch)]
            locs = ['08_腐烂观察!I' + str(r['row']) + ':J' + str(r['row']) for r in sources]
            dates = sorted(set((str(r['B'])[:10] for r in sources)))
            missing = sum((r['I'] is None for r in sources))
        else:
            sources = [r for r in raw['09_品质检测'] if r['G'] == g and r['C'] == day and (r['H'] == metric) and (batch is None or r['D'] == batch)]
            locs = ['09_品质检测!I' + str(r['row']) for r in sources]
            dates = sorted(set((str(r['B'])[:10] for r in sources)))
            missing = sum((r['I'] is None for r in sources))
        nfr = sum((r['n_fruits'] for r in valid))
        planned_fruits = sum((units[r['unit']]['E'] for r in allu))
        return dict(metric=metric, metric_label=LABELS[metric], unit=UNITS[metric], group=g, day=day, batch=batch or 'ALL', calendar_dates=dates, n_containers=len(vv), planned_containers=len(allu), n_fruits=nfr, planned_fruits=planned_fruits, uncovered_fruits=planned_fruits - nfr, n_readings=sum((r['n_reads'] for r in valid)), n_technical_readings=sum((r['n_reads'] for r in valid)) if metric == 'firmness' else None, missing_readings=missing, missing_containers=len(allu) - len(vv), mean=statistics.mean(vv) if vv else None, sd=statistics.stdev(vv) if len(vv) > 1 else None, min=min(vv) if vv else None, max=max(vv) if vv else None, source_locations=locs, unit_ids=[r['unit'] for r in valid], sd_meaning='有效容器间样本SD，ddof=1；n=1时不可估计，记null')
    summary = []
    bs = []
    for metric in METRICS:
        for g in GROUPS:
            for d in [0, 1, 2, 3, 4] if metric in ['mass_loss', 'decay_pct'] else [0, 2, 4]:
                summary.append(group_summary(metric, g, d))
                bs.extend((group_summary(metric, g, d, b) for b in BATCH_START))
    assert len(summary) == 48 and len(bs) == 144
    rounding = []
    for x in a['summary']:
        if x['metric'] != 'mass_loss_book_rounded':
            continue
        p = next((r for r in summary if r['metric'] == 'mass_loss' and r['group'] == x['group'] and (r['day'] == x['day'])))
        rounding.append(dict(group=x['group'], day=x['day'], n_containers=x['n'], full_precision_mean=p['mean'], full_precision_sd=p['sd'], rounded_unit_mean=x['mean'], rounded_unit_sd=x['sd'], delta_rounded_minus_full=x['mean'] - p['mean'], sources=p['source_locations']))
    first = []
    for g in GROUPS:
        for d in range(5):
            rr = [r for r in raw['08_腐烂观察'] if r['G'] == g and r['H'] == 'L' and (r['C'] == d)]
            denominator = sum((u['E'] for u in raw['04_实验单位'] if u['C'] == g and u['D'] == 'L'))
            first.append(dict(group=g, day=d, first_decayed=sum((r['J'] for r in rr)), cumulative_decayed=sum((r['I'] for r in rr)), denominator=denominator, cumulative_pct=sum((r['I'] for r in rr)) / denominator * 100, source_locations=['08_腐烂观察!I' + str(r['row']) + ':J' + str(r['row']) for r in rr]))
    env = []
    es = []
    for r in raw['10_环境监测']:
        env.append(dict(id=r['A'], date_time=r['B'], batch=r['C'], temperature_C=r['D'], relative_humidity_pct=r['E'], source='10_环境监测!D' + str(r['row']) + ':E' + str(r['row'])))
    for b in ['ALL', *BATCH_START]:
        for m in ['temperature_C', 'relative_humidity_pct']:
            rr = [r for r in env if b == 'ALL' or r['batch'] == b]
            vv = [r[m] for r in rr]
            es.append(dict(batch=b, metric=m, n_time_records=len(vv), mean=statistics.mean(vv), time_sample_sd=statistics.stdev(vv), min=min(vv), max=max(vv), sources=[r['source'] for r in rr]))
    sensitivity = []
    for metric in ['firmness', 'TSS']:
        for g in GROUPS:
            for d in [0, 2, 4]:
                ss = next((x for x in summary if (x['metric'], x['group'], x['day']) == (metric, g, d)))
                ff = [x['value'] for x in a['fruit_quality'] if (x['metric'], x['group'], x['day']) == (metric, g, d) and x['value'] is not None]
                fm = statistics.mean(ff)
                sensitivity.append(dict(metric=metric, group=g, day=d, container_mean=ss['mean'], fruit_equal_mean=fm, n_fruits=len(ff), delta_fruit_minus_container=fm - ss['mean']))
    for g in GROUPS:
        for d in range(5):
            rr = [r for r in a['mass'] if r['group'] == g and r['day'] == d and (r['value'] is not None)]
            vv = [statistics.mean((r['value'] for r in rr if r['batch'] == b)) for b in BATCH_START]
            cm = statistics.mean((r['value'] for r in rr))
            bm = statistics.mean(vv)
            sensitivity.append(dict(metric='mass_loss', group=g, day=d, container_mean=cm, batch_equal_mean=bm, delta_batch_minus_container=bm - cm))
    contrasts = [dict(**r, display_unit='百分点' if r['metric'] in ['mass_loss_full', 'decay_pct'] else UNITS[r['metric']]) for r in a['contrasts']]
    for r in contrasts:
        if r['metric'] == 'mass_loss_full':
            r['metric'] = 'mass_loss'
    missing = []
    for r in raw['07_连续称重']:
        if r['I'] is None:
            missing.append(dict(metric='mass_loss', record_id=r['A'], batch=r['D'], group=r['F'], day=r['C'], unit_id=r['E'], fruit_id=None, source='07_连续称重!I' + str(r['row']), status=r['K'], reason=r['M'], action='保持缺失，不补0/不借旧值；其余时点保留'))
    for r in raw['09_品质检测']:
        if r['I'] is None:
            missing.append(dict(metric=r['H'], record_id=r['A'], batch=r['D'], group=r['G'], day=r['C'], unit_id=r['E'], fruit_id=r['F'], source='09_品质检测!I' + str(r['row']), status=r['M'], reason=r['N'], action='保持缺失，容器只汇总可测果；缺失与果实状态有关'))
    assert len(missing) == 7
    methods = {}
    import openpyxl
    ww = openpyxl.load_workbook(source, read_only=True, data_only=True)
    for i, row in enumerate(ww['03_仪器与方法'].iter_rows(min_row=5, values_only=True), 5):
        if row[0]:
            methods['03_仪器与方法!A' + str(i) + ':F' + str(i)] = dict(statement=list(row[:6]), status='DOCUMENTED_BUT_UNVERIFIED；不等于独立原仪器/实测来源核验')
    ww.close()
    return dict(schema_version='phase09b.v1', title='可食性海藻酸钠膜对草莓常温保鲜效果的研究', source=dict(path='实验记录.xlsx', sha256=source_sha, authority='用户指定唯一数值主源', historical_sources_used_for_statistics=False, excluded_sheet='18_内部一致性检查'), scripts_sha256=code_hashes, method=dict(primary_mass_precision='100*(Day0_net_mass-day_net_mass)/Day0_net_mass; no early rounding', workbook_comparison='round each container mass loss to 2 decimals before aggregation', quality='technical readings -> fruit -> container -> group', sd='sample SD among containers, ddof=1; single container SD null', inference='descriptive only; no hypothesis test, p-value, CI or significance letters', missing='no zero-fill, no imputation, no old values, no exclusions by result', date_interpretation='relative storage day aligned within three date batches; timestamps have no independently confirmed timezone'), summary=summary, batch_summary=bs, container_results=unit, fruit_quality=a['fruit_quality'], rounding_comparison=rounding, first_decay=first, environment_records=env, environment_summary=es, batch_contrasts=contrasts, weight_sensitivity=sensitivity, missing_records=missing, deviations=raw['11_异常偏离'], outlier_flags=a['outlier_flags'], quality_qualification=a['notes']['quality_qualification'], mother_solution_ids=a['notes']['mother_ids'], source_profiles=a['profiles'], integrity_findings=a['findings'], source_cache_mismatches=a['original_aggregate_mismatches'], key_checks=a['keycounts'], method_statements=methods, limitations=['仪器/去皮/校准/制样/母液来源与随机轮换实际执行尚无独立材料闭环', '54容器/189果/读数不等于同层独立处理重复；共享母液及三批次限制推断', 'D0/D2/D4不同果；处理后基线差异、17局部可测果和2严重不可测果限定解释', '材料安全、微生物抑菌、膜透湿/交联机制及货架期延长未验证'])

def export_tables(out, r):
    td = Path(out) / 'tables'
    write_csv(td / '新数据描述统计汇总.csv', r['summary'])
    write_csv(td / '各批次描述统计.csv', r['batch_summary'])
    write_csv(td / '容器水平结果.csv', r['container_results'], list(dict.fromkeys((k for x in r['container_results'] for k in x))))
    write_csv(td / '单果品质及技术折叠.csv', r['fruit_quality'])
    write_csv(td / '失重率舍入口径对照.csv', r['rounding_comparison'])
    write_csv(td / '首次腐烂及累计计数.csv', r['first_decay'])
    write_csv(td / '温湿度时间统计.csv', r['environment_summary'])
    write_csv(td / '批次内组差与留一敏感性.csv', r['batch_contrasts'])
    write_csv(td / '权重与缺失敏感性.csv', r['weight_sensitivity'], list(dict.fromkeys((k for x in r['weight_sensitivity'] for k in x))))
    write_csv(td / '缺失记录.csv', r['missing_records'])
    write_csv(td / '异常值标记_全部保留.csv', r['outlier_flags'])
