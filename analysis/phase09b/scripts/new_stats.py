"""Pure new-record descriptive analysis. No historical numerical sources are opened."""
from pathlib import Path
import openpyxl, statistics, collections, math, datetime

def analyze_records(source):
    w = openpyxl.load_workbook(source, data_only=True, read_only=False)

    def rows(sn):
        return [dict(row=i, **{openpyxl.utils.get_column_letter(j): value for j, value in enumerate(row, 1)}) for i, row in enumerate(w[sn].iter_rows(min_row=5, values_only=True), 5) if row[0] is not None]
    U = rows('04_实验单位')
    F = rows('05_果实清单')
    TR = rows('06_处理记录')
    M = rows('07_连续称重')
    DC = rows('08_腐烂观察')
    Q = rows('09_品质检测')
    EN = rows('10_环境监测')
    DV = rows('11_异常偏离')
    UM = {r['B']: r for r in U}
    FM = {r['C']: r for r in F}
    TM = {r['B']: r for r in TR}
    md = {(r['E'], r['C']): r for r in M}
    dd = {(r['F'], r['C']): r for r in DC}
    days = {'B1': datetime.date(2026, 10, 5), 'B2': datetime.date(2026, 10, 13), 'B3': datetime.date(2026, 10, 21)}
    find = []

    def issue(id, severity, evidence, impact):
        find.append(dict(id=id, severity=severity, evidence=evidence, impact=impact))

    def checks(condition, id, where):
        if not condition:
            issue(id, 'HIGH', where, '层级/引用或时间不一致')

    def dt(x):
        return x if isinstance(x, datetime.datetime) else datetime.datetime.fromisoformat(x)
    keycounts = {}
    for sn, rr, key in [('04', U, lambda r: r['B']), ('05', F, lambda r: r['C']), ('06', TR, lambda r: r['A']), ('07', M, lambda r: r['A']), ('08', DC, lambda r: r['A']), ('09', Q, lambda r: r['A']), ('10', EN, lambda r: r['A']), ('11', DV, lambda r: r['A'])]:
        c = collections.Counter((key(r) for r in rr))
        keycounts[sn] = dict(rows=len(rr), duplicate_ids=[k for k, v in c.items() if v > 1])
        for k, v in c.items():
            checks(v == 1, 'duplicate_ID', sn + ':' + str(k))
    for key, rr, kfn in [('mass_unit_day', M, lambda r: (r['E'], r['C'])), ('decay_fruit_day', DC, lambda r: (r['F'], r['C'])), ('quality_fruit_day_trait_repeat', Q, lambda r: (r['F'], r['C'], r['H'], r['L']))]:
        cc = collections.Counter((kfn(r) for r in rr))
        checks(max(cc.values()) == 1, 'composite_duplicate', key)
    for r in F:
        u = UM.get(r['B'])
        checks(u is not None and (r['A'], r['D'], r['E']) == (u['A'], u['C'], u['D']), 'fruit_parent', '05!' + str(r['row']))
    for u in U:
        ff = [f for f in F if f['B'] == u['B']]
        checks(len(ff) == u['E'], 'unit_fruit_n', u['B'])
        checks(u['E'] == (4 if u['D'] == 'L' else 3), 'design', u['B'])
    for r in TR:
        u = UM.get(r['B'])
        checks(u is not None and (r['C'], r['D'], r['K']) == (u['A'], u['C'], u['G']), 'treatment_join', '06!' + str(r['row']))
        checks((r['F'], r['G']) == {'CK': (0, 0), 'Ca': (0, 1), 'SA-Ca': (1.5, 1)}[r['D']], 'dose', '06!' + str(r['row']))
    for r in M:
        u = UM.get(r['E'])
        checks(u is not None and (r['D'], r['F'], r['G']) == (u['A'], u['C'], u['E']) and (u['D'] == 'L'), 'mass_join', '07!' + str(r['row']))
        checks(dt(r['B']).date() == days[r['D']] + datetime.timedelta(days=r['C']), 'mass_date', '07!' + str(r['row']))
        checks(r['H'] == md[r['E'], 0]['I'], 'baseline_consistency', '07!' + str(r['row']))
        checks(r['H'] > 0 and (r['I'] is None or 0 < r['I'] <= r['H']), 'mass_domain', '07!' + str(r['row']))
    for r in DC:
        f = FM.get(r['F'])
        checks(f is not None and (r['D'], r['E'], r['G'], r['H']) == (f['A'], f['B'], f['D'], f['E']), 'decay_join', '08!' + str(r['row']))
        checks(r['I'] in [0, 1] and r['J'] in [0, 1] and (r['K'] == 0), 'decay_domain', '08!' + str(r['row']))
        checks(dt(r['B']).date() == days[r['D']] + datetime.timedelta(days=r['C']), 'decay_date', '08!' + str(r['row']))
        if f:
            end = 4 if f['E'] == 'L' else int(f['E'][1])
            checks(0 <= r['C'] <= end, 'D_after_sampling', '08!' + str(r['row']))
    for f in F:
        ss = sorted([x for x in DC if x['F'] == f['C']], key=lambda r: r['C'])
        end = 4 if f['E'] == 'L' else int(f['E'][1])
        checks([x['C'] for x in ss] == list(range(end + 1)), 'decay_schedule', f['C'])
        prev = 0
        for r in ss:
            checks(r['I'] >= prev and r['J'] == int(r['I'] == 1 and prev == 0), 'cumulative_or_first', '08!' + str(r['row']))
            prev = r['I']
    for r in Q:
        f = FM.get(r['F'])
        checks(f is not None and (r['D'], r['E'], r['G']) == (f['A'], f['B'], f['D']) and (f['E'] != 'L') and (r['C'] == int(f['E'][1])), 'quality_join', '09!' + str(r['row']))
        checks(r['J'] == ('N' if r['H'] == 'firmness' else '°Brix'), 'quality_unit', '09!' + str(r['row']))
        checks(dt(r['B']).date() == days[r['D']] + datetime.timedelta(days=r['C']), 'quality_date', '09!' + str(r['row']))
        checks(r['I'] is None or (math.isfinite(r['I']) and r['I'] > 0), 'quality_domain', '09!' + str(r['row']))
        if r['H'] == 'TSS' and r['I'] is not None:
            checks(abs(r['I'] * 10 - round(r['I'] * 10)) < 1e-08, 'TSS_resolution', '09!' + str(r['row']))
        d = dd[r['F'], r['C']]
        checks(dt(r['B']) >= dt(d['B']), 'quality_before_appearance', '09!' + str(r['row']))
        if d['O'] == 2:
            checks(r['I'] is None, 'severe_measured', '09!' + str(r['row']))
        if d['I'] == 1 and r['I'] is not None:
            checks(d['O'] == 1 and bool(r['N']), 'mild_qualification', '09!' + str(r['row']))
    for u in U:
        t = TM[u['B']]
        end = dt(t['E']) + datetime.timedelta(minutes=t['H'] + t['I'] + t['J'])
        dd0 = [r for r in DC if r['E'] == u['B'] and r['C'] == 0]
        checks(min((dt(r['B']) for r in dd0)) >= end, 'appearance_before_dry', u['B'])
        if u['D'] == 'L':
            checks(dt(md[u['B'], 0]['B']) >= end, 'baseline_before_dry', u['B'])
            for d in range(5):
                checks(dt(md[u['B'], d]['B']) <= min((dt(r['B']) for r in DC if r['E'] == u['B'] and r['C'] == d)), 'mass_after_appearance', u['B'] + str(d))
    for b in days:
        cc = collections.Counter((u['I'] for u in U if u['A'] == b))
        checks(max(cc.values()) == 1, 'rack_duplicate', b)
    checks(len(U)==54 and len(F)==189 and len(TR)==54,'complete_design','04/05/06')
    checks(len({r['B'] for r in TR})==54,'treatment_unit_unique','06')
    for b in days:
        for g in ['CK','Ca','SA-Ca']:
            cc=collections.Counter(u['D'] for u in U if u['A']==b and u['C']==g)
            checks(cc=={'L':3,'D0':1,'D2':1,'D4':1},'balanced_allocation',b+g)
    for b in days:
        er=[r for r in EN if r['C']==b]
        checks(len(er)==10,'environment_count',b)
        expected={(days[b]+datetime.timedelta(days=d),h) for d in range(5) for h in [9,17]}
        checks({(dt(r['B']).date(),dt(r['B']).hour) for r in er}==expected,'environment_schedule',b)
        checks(all(0<r['E']<=100 and math.isfinite(r['D']) for r in er),'environment_domain',b)
    mr = []
    fq = []
    qr = []
    dr = []
    for r in M:
        x = None if r['I'] is None else (r['H'] - r['I']) / r['H'] * 100
        mr.append(dict(batch=r['D'], group=r['F'], unit=r['E'], day=r['C'], value=x, rounded=None if x is None else round(x, 2), source='07_连续称重!H' + str(r['row']) + ':I' + str(r['row'])))
    for f in F:
        if f['E'] == 'L':
            continue
        rr = [r for r in Q if r['F'] == f['C']]
        checks(len(rr) == 3 and sorted(((r['H'], r['L']) for r in rr)) == [('TSS', 1), ('firmness', 1), ('firmness', 2)], 'tech_schedule', f['C'])
        for metric in ['firmness', 'TSS']:
            ss = [r for r in rr if r['H'] == metric and r['I'] is not None]
            fq.append(dict(batch=f['A'], group=f['D'], unit=f['B'], fruit=f['C'], day=int(f['E'][1]), metric=metric, value=statistics.mean((r['I'] for r in ss)) if ss else None, n_reads=len(ss), source=['09_品质检测!I' + str(r['row']) for r in rr if r['H'] == metric]))
    for u in U:
        if u['D'] == 'L':
            for day in range(5):
                rr = [r for r in DC if r['E'] == u['B'] and r['C'] == day]
                dr.append(dict(batch=u['A'], group=u['C'], unit=u['B'], day=day, value=sum((r['I'] for r in rr)) / u['E'] * 100, decayed=sum((r['I'] for r in rr)), denom=u['E']))
        else:
            for metric in ['firmness', 'TSS']:
                rr = [r for r in fq if r['unit'] == u['B'] and r['metric'] == metric and (r['value'] is not None)]
                qr.append(dict(batch=u['A'], group=u['C'], unit=u['B'], day=int(u['D'][1]), metric=metric, value=statistics.mean((r['value'] for r in rr)) if rr else None, n_fruits=len(rr), n_reads=sum((r['n_reads'] for r in rr))))

    def summary(rr, metric, valuekey='value'):
        out = []
        for g, day in sorted(set(((r['group'], r['day']) for r in rr))):
            ss = [r for r in rr if r['group'] == g and r['day'] == day and (r[valuekey] is not None)]
            vv = [r[valuekey] for r in ss]
            out.append(dict(metric=metric, group=g, day=day, n=len(vv), mean=statistics.mean(vv), sd=statistics.stdev(vv) if len(vv) > 1 else None, min=min(vv), max=max(vv), n_fruits=sum((r.get('n_fruits', r.get('denom', 4)) for r in ss))))
        return out
    ss = summary(mr, 'mass_loss_full') + summary(mr, 'mass_loss_book_rounded', 'rounded') + summary(dr, 'decay_pct') + sum([summary([r for r in qr if r['metric'] == m], m) for m in ['firmness', 'TSS']], [])
    by = {(r['metric'], r['group'], r['day']): r for r in ss}
    agg = []

    def eqcache(sn, cell, val, why):
        c = w[sn][cell].value
        ok = c is None and val is None or (isinstance(c, (int, float)) and isinstance(val, (int, float)) and math.isclose(c, val, abs_tol=1e-08, rel_tol=1e-09)) or c == val
        if not ok:
            agg.append(dict(sheet=sn, cell=cell, cache=c, recalc=val, reason=why))
    for row in rows('14_失重腐烂统计'):
        g, d = (row['A'], row['B'])
        m = by['mass_loss_book_rounded', g, d]
        de = [r for r in dr if r['group'] == g and r['day'] == d]
        for col, val in [('C', m['n']), ('D', m['mean']), ('E', m['sd']), ('F', sum((r['decayed'] for r in de))), ('G', sum((r['denom'] for r in de))), ('H', by['decay_pct', g, d]['mean'])]:
            eqcache('14_失重腐烂统计', col + str(row['row']), val, 'raw -> unit -> group')
    for row in rows('15_品质组统计'):
        g, d = (row['A'], row['B'])
        for metric, cols in [('firmness', 'CDE'), ('TSS', 'FGH')]:
            x = by[metric, g, d]
            for col, val in zip(cols, [x['n'], x['mean'], x['sd']]):
                eqcache('15_品质组统计', col + str(row['row']), val, 'tech -> fruit -> unit -> group')
    for row in rows('13_品质盒均值'):
        for metric, cols in [('firmness', 'GH'), ('TSS', 'IJ')]:
            r = next((x for x in qr if x['unit'] == row['A'] and x['metric'] == metric))
            for col, val in zip(cols, [r['n_fruits'], r['value']]):
                eqcache('13_品质盒均值', col + str(row['row']), val, 'raw -> fruit -> unit')
    for row in rows('07_连续称重'):
        r = next((r for r in mr if r['unit'] == row['E'] and r['day'] == row['C']))
        eqcache('07_连续称重', 'J' + str(row['row']), r['rounded'], 'new baseline/input net mass')
    batch = []
    sens = []
    for metric, rr, key in [('mass_loss_full', mr, 'value'), ('mass_loss_book_rounded', mr, 'rounded'), ('decay_pct', dr, 'value'), ('firmness', [r for r in qr if r['metric'] == 'firmness'], 'value'), ('TSS', [r for r in qr if r['metric'] == 'TSS'], 'value')]:
        for g in ['CK', 'Ca', 'SA-Ca']:
            xx = [r for r in rr if r['group'] == g and r['day'] == 4]
            bm = {b: statistics.mean((r[key] for r in xx if r['batch'] == b and r[key] is not None)) for b in days}
            batch.append(dict(metric=metric, group=g, day=4, **bm))
            if metric in ['firmness', 'TSS']:
                ff = [r['value'] for r in fq if r['metric'] == metric and r['group'] == g and (r['day'] == 4) and (r['value'] is not None)]
                sens.append(dict(metric=metric, group=g, container_mean=by[metric, g, 4]['mean'], fruit_equal_mean=statistics.mean(ff), n_fruits=len(ff)))
    contrasts = []
    for metric in ['mass_loss_full', 'decay_pct', 'firmness', 'TSS']:
        for g in ['CK', 'Ca']:
            a = next((r for r in batch if r['metric'] == metric and r['group'] == 'SA-Ca'))
            b = next((r for r in batch if r['metric'] == metric and r['group'] == g))
            dv = [a[x] - b[x] for x in days]
            loo = [statistics.mean(dv[:i] + dv[i + 1:]) for i in range(3)]
            contrasts.append(dict(metric=metric, contrast='SA-Ca - ' + g, B1=dv[0], B2=dv[1], B3=dv[2], mean=statistics.mean(dv), sd=statistics.stdev(dv), leave_one_min=min(loo), leave_one_max=max(loo)))
    outliers = []
    for r in ss:
        if r['metric'] == 'mass_loss_book_rounded':
            continue
        if r['metric'] in ['mass_loss_full', 'decay_pct']:
            xx = [x for x in (mr if r['metric'] == 'mass_loss_full' else dr) if x['group'] == r['group'] and x['day'] == r['day'] and (x['value'] is not None)]
            if len(xx) >= 4:
                q1, _, q3 = statistics.quantiles([x['value'] for x in xx], n=4, method='inclusive')
                iqr = q3 - q1
                if iqr:
                    outliers.extend((dict(metric=r['metric'], group=r['group'], day=r['day'], unit=x['unit'], value=x['value'], bounds=[q1 - 1.5 * iqr, q3 + 1.5 * iqr]) for x in xx if x['value'] < q1 - 1.5 * iqr or x['value'] > q3 + 1.5 * iqr))
    profiles = {}
    for name, rr, col in [('arrival', F, 'F'), ('baseline', M, 'H'), ('observed', M, 'I'), ('firmness', [r for r in Q if r['H'] == 'firmness'], 'I'), ('TSS', [r for r in Q if r['H'] == 'TSS'], 'I'), ('temperature', EN, 'D'), ('RH', EN, 'E')]:
        vv = [r[col] for r in rr if isinstance(r[col], (int, float))]
        profiles[name] = dict(n=len(vv), missing=len(rr) - len(vv), min=min(vv), max=max(vv))
    qual = collections.Counter()
    sev = []
    for f in F:
        if f['E'] == 'L':
            continue
        day = int(f['E'][1])
        d = dd[f['C'], day]
        rr = [r for r in Q if r['F'] == f['C']]
        qual[str(d['I']), str(d['O']), str(any((r['I'] is not None for r in rr)))] += 1
    h2 = []
    for f in F:
        rr = sorted([r for r in Q if r['F'] == f['C'] and r['H'] == 'firmness' and (r['I'] is not None)], key=lambda r: r['L'])
        if len(rr) == 2:
            h2.append(rr[1]['I'] - rr[0]['I'])
    notes = dict(quality_qualification={str(k): v for k, v in qual.items()}, hardness_pairs=dict(n=len(h2), second_higher=sum((x > 0 for x in h2)), second_lower=sum((x < 0 for x in h2)), equal=sum((x == 0 for x in h2))), mother_ids=sorted(set((u['G'] for u in U))), time_earliest=min((r['B'] for r in Q)), time_latest=max((r['B'] for r in Q)), actual_dip_range=[min((r['H'] for r in TR)), max((r['H'] for r in TR)), min((r['I'] for r in TR)), max((r['I'] for r in TR))], dry_range=[min((r['J'] for r in TR)), max((r['J'] for r in TR))])
    raw = {name: rows(name) for name in ['04_实验单位', '05_果实清单', '06_处理记录', '07_连续称重', '08_腐烂观察', '09_品质检测', '10_环境监测', '11_异常偏离']}
    w.close()
    return dict(raw=raw, findings=find, original_aggregate_mismatches=agg, units=U, fruits=F, mass=mr, decay=dr, quality_units=qr, fruit_quality=fq, summary=ss, batch=batch, contrasts=contrasts, sensitivity=sens, profiles=profiles, notes=notes, outlier_flags=outliers, keycounts=keycounts)
