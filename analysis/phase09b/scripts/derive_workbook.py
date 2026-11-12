"""Surgical XLSX changes and real LibreOffice cache validation.
Raw literal values and the excluded sheet XML are preserved. Only approved derived
formulas/constants and engine-generated formula caches may change.
"""
from pathlib import Path
from copy import deepcopy
import zipfile, xml.etree.ElementTree as ET, json, hashlib, math, subprocess, tempfile, shutil, datetime, statistics
import openpyxl
from formula_oracle import evaluate_all
NS = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
Q = lambda tag: '{' + NS + '}' + tag
EXCLUDED = '18_内部一致性检查'
ET.register_namespace('', NS)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def same(a, b):
    if a in (None, '') and b in (None, ''):
        return True
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=1e-09, abs_tol=1e-08)
    return a == b

def sheet_paths(z):
    book = ET.fromstring(z.read('xl/workbook.xml'))
    rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    refs = {r.attrib['Id']: r.attrib['Target'] for r in rels}
    result = {}
    for node in book.find(Q('sheets')):
        target = refs[node.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
        result[node.attrib['name']] = target.lstrip('/') if target.startswith('/') else 'xl/' + target
    return result

def build_derived(source, output, stats, skip_engine=False):
    output = Path(output)
    results = output / 'results'
    tables = output / 'tables'
    results.mkdir(parents=True, exist_ok=True)
    tables.mkdir(parents=True, exist_ok=True)
    dest = output / '实验记录_派生计算修订副本.xlsx'
    sw = openpyxl.load_workbook(source, data_only=False)
    raw = stats['raw']
    U = raw['04_实验单位']
    M = raw['07_连续称重']
    D = raw['08_腐烂观察']
    ENV = raw['10_环境监测']
    changes = {}
    fixed = []
    special = {}

    def sumrefs(sheet, rows, col):
        return 'SUM(' + ','.join(("'" + sheet + "'!" + col + str(r['row']) for r in rows)) + ')'

    def countrefs(sheet, rows, col):
        return 'COUNT(' + ','.join(("'" + sheet + "'!" + col + str(r['row']) for r in rows)) + ')'

    def register(sn, cell, before, after, reason):
        changes[sn, cell] = dict(sheet=sn, cell=cell, before=before, after=after, reason=reason)
    for sh in sw:
        if sh.title == EXCLUDED:
            continue
        for row in sh:
            for c in row:
                if c.data_type == 'f':
                    assert c.value.startswith('=='), (sh.title, c.coordinate, c.value)
                    register(sh.title, c.coordinate, c.value, '=' + c.value.lstrip('='), 'A1_NORMALIZE_ONLY')
    assert len(changes) == 1458
    qw = {r['A']: r for r in raw['09_品质检测']}
    for row in sw['21_检测时序索引'].iter_rows(min_row=5):
        rid = row[9].value
        if not rid:
            continue
        r = qw[rid]
        if r['I'] is None:
            addr = 'H' + str(row[0].row)
            ref = "'09_品质检测'!I" + str(r['row'])
            changes['21_检测时序索引', addr]['after'] = '=IF(' + ref + '="","",' + ref + ')'
            changes['21_检测时序索引', addr]['reason'] += ';A3_PRESERVE_MISSING'
    assert sum(('A3_' in x['reason'] for x in changes.values())) == 6
    for row in sw['14_失重腐烂统计'].iter_rows(min_row=5):
        if not row[0].value:
            continue
        g, day = (row[0].value, row[1].value)
        uu = [u for u in U if u['C'] == g and u['D'] == 'L']
        dd = [r for r in D if r['G'] == g and r['C'] == day and (r['H'] == 'L')]
        for col, val, formula in [('F', sum((r['I'] for r in dd)), sumrefs('08_腐烂观察', dd, 'I')), ('G', sum((u['E'] for u in uu)), sumrefs('04_实验单位', uu, 'E'))]:
            c = sw['14_失重腐烂统计'][col + str(row[0].row)]
            assert same(c.value, val), (c.coordinate, c.value, val)
            fixed.append(dict(sheet='14_失重腐烂统计', cell=c.coordinate, original=c.value, independent_recalc=val, equal=True, action='LINK_TO_RAW'))
            register('14_失重腐烂统计', c.coordinate, c.value, '=' + formula, 'A4_LINK_VERIFIED_FIXED_SUMMARY')
    for row in sw['16_逐日观察总表'].iter_rows(min_row=5):
        if not row[0].value:
            continue
        b, day, g = (row[0].value, row[2].value, row[3].value)
        uu = [u for u in U if (u['A'], u['C'], u['D']) == (b, g, 'L')]
        mm = [r for r in M if (r['D'], r['F'], r['C']) == (b, g, day)]
        dd = [r for r in D if (r['D'], r['G'], r['C'], r['H']) == (b, g, day, 'L')]
        du = [u for u in U if (u['A'], u['C'], u['D']) == (b, g, 'D' + str(day))]
        specs = [('E', len(uu), countrefs('04_实验单位', uu, 'E')), ('F', sum((r['I'] is not None for r in mm)), countrefs('07_连续称重', mm, 'I')), ('H', sum((r['I'] for r in dd)), sumrefs('08_腐烂观察', dd, 'I')), ('I', sum((u['E'] for u in uu)), sumrefs('04_实验单位', uu, 'E')), ('K', len(du), countrefs('04_实验单位', du, 'E') if du else '0')]
        date = datetime.date(2026, 10, {'B1': 5, 'B2': 13, 'B3': 21}[b]) + datetime.timedelta(days=day)
        for hour, cols in [(9, 'PQ'), (17, 'RS')]:
            e = next((r for r in ENV if r['C'] == b and datetime.datetime.fromisoformat(r['B']).date() == date and (datetime.datetime.fromisoformat(r['B']).hour == hour)))
            specs.extend([(cols[0], e['D'], "'10_环境监测'!D" + str(e['row'])), (cols[1], e['E'], "'10_环境监测'!E" + str(e['row']))])
        for col, val, formula in specs:
            c = sw['16_逐日观察总表'][col + str(row[0].row)]
            assert same(c.value, val), (c.coordinate, c.value, val)
            fixed.append(dict(sheet='16_逐日观察总表', cell=c.coordinate, original=c.value, independent_recalc=val, equal=True, action='LINK_TO_RAW'))
            register('16_逐日观察总表', c.coordinate, c.value, '=' + formula, 'A4_LINK_VERIFIED_FIXED_SUMMARY')
    assert len(fixed) == 435
    labels = {'B5': f"{len({u['A'] for u in U})}批", 'B6': f"{len({u['C'] for u in U})}组", 'B7': f'{len(U)}盒', 'B8': f"{len(raw['05_果实清单'])}颗", 'B9': f'{len(M)}条', 'B10': f'{len(D)}条', 'B11': f"{len(raw['09_品质检测'])}条", 'B12': f'{len(ENV)}条', 'B13': f"{len(raw['11_异常偏离'])}项", 'B14': f"{sum((r['metric'] == 'firmness' and r['value'] is not None for r in stats['fruit_quality']))}颗有效"}
    for cell, expected in labels.items():
        assert sw['00_实验总览'][cell].value == expected, (cell, expected)
        fixed.append(dict(sheet='00_实验总览', cell=cell, original=expected, independent_recalc=expected, equal=True, action='VERIFIED_LABEL_UNCHANGED'))
    with zipfile.ZipFile(source) as z:
        paths = sheet_paths(z)
        xmls = {}
        for sn, path in paths.items():
            if sn == EXCLUDED:
                continue
            root = ET.fromstring(z.read(path))
            changed = False
            for c in root.findall('.//' + Q('c')):
                k = (sn, c.attrib['r'])
                if k not in changes:
                    continue
                item = changes[k]
                f = c.find(Q('f'))
                if f is None:
                    f = ET.Element(Q('f'))
                    c.insert(0, f)
                f.text = item['after'][1:]
                changed = True
            if changed:
                xmls[path] = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        with tempfile.TemporaryDirectory(prefix='phase09b_calc_') as tmp:
            tmp = Path(tmp)
            prepared = tmp / 'prepared.xlsx'
            engine_dir = tmp / 'recalculated'
            engine_dir.mkdir()
            with zipfile.ZipFile(prepared, 'w', compression=zipfile.ZIP_DEFLATED) as zz:
                for info in z.infolist():
                    zz.writestr(deepcopy(info), xmls.get(info.filename, z.read(info.filename)))
            transport = tmp / 'calculation_input.xlsx'
            cw = openpyxl.load_workbook(prepared, data_only=False)
            cw.save(transport)
            cw.close()
            # Standardize the derivative's OOXML package as well as the temporary
            # engine transport. Retain the excluded XML and its original SST as
            # opaque bytes, without interpreting their content.
            with zipfile.ZipFile(transport) as tz:
                final_parts={name:tz.read(name) for name in tz.namelist()}
            final_parts['docProps/core.xml']=z.read('docProps/core.xml')
            final_parts[paths[EXCLUDED]]=z.read(paths[EXCLUDED])
            if 'xl/sharedStrings.xml' in z.namelist():
                final_parts['xl/sharedStrings.xml']=z.read('xl/sharedStrings.xml')
                relns='http://schemas.openxmlformats.org/package/2006/relationships'
                trns='http://schemas.openxmlformats.org/package/2006/content-types'
                rel=ET.fromstring(final_parts['xl/_rels/workbook.xml.rels'])
                ET.SubElement(rel,'{'+relns+'}Relationship',dict(Type='http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings',Id='rIdOriginalSharedStrings',Target='sharedStrings.xml'))
                final_parts['xl/_rels/workbook.xml.rels']=ET.tostring(rel)
                types=ET.fromstring(final_parts['[Content_Types].xml'])
                ET.SubElement(types,'{'+trns+'}Override',dict(PartName='/xl/sharedStrings.xml',ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml'))
                final_parts['[Content_Types].xml']=ET.tostring(types)
            engine = dict(status='FAIL', real_engine_recalculation=False, reason='not run')
            if not skip_engine and shutil.which('soffice'):
                version = subprocess.run(['soffice', '--version'], capture_output=True, text=True, timeout=30).stdout.strip()
                cmd = ['soffice', '-env:UserInstallation=' + (tmp / 'profile').as_uri(), '--headless', '--convert-to', 'xlsx', '--outdir', str(engine_dir), str(transport)]
                try:
                    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
                    eng = engine_dir / 'calculation_input.xlsx'
                    engine = dict(status='PASS' if proc.returncode == 0 and eng.exists() else 'FAIL', real_engine_recalculation=proc.returncode == 0 and eng.exists(), version=version, returncode=proc.returncode, command=[v.replace(str(tmp), '<temporary>') for v in cmd], stdout=proc.stdout.replace(str(tmp), '<temporary>'), stderr=proc.stderr.replace(str(tmp), '<temporary>'))
                    if engine['real_engine_recalculation']:
                        engine['raw_engine_output_sha256'] = sha(eng)
                        engine['engine_input_transport'] = 'openpyxl OOXML metadata normalization; all original non-derived literal values and excluded worksheet XML/SST preserved'
                        engine['engine_input_sha256'] = sha(transport)
                        ew = openpyxl.load_workbook(eng, data_only=True)
                        oracle = evaluate_all(prepared)
                        mismatch = []
                        errs = []
                        engine_values = {}
                        for (sn, cell), value in oracle.items():
                            c = ew[sn][cell]
                            engine_values[sn, cell] = c.value
                            if c.data_type == 'e':
                                errs.append(dict(sheet=sn, cell=cell, value=c.value))
                            if not same(value, c.value):
                                mismatch.append(dict(sheet=sn, cell=cell, python_intent=value, real_engine=c.value))
                        engine.update(formula_cells_compared=len(oracle), mismatches=mismatch, error_cells=errs)
                        engine['status'] = 'PASS' if not mismatch and (not errs) else 'FAIL'
                        ez = zipfile.ZipFile(eng)
                        ep = sheet_paths(ez)
                        for sn, path in paths.items():
                            if sn == EXCLUDED:
                                continue
                            root = ET.fromstring(final_parts[path])
                            eroot = ET.fromstring(ez.read(ep[sn]))
                            ec = {c.attrib['r']: c for c in eroot.findall('.//' + Q('c'))}
                            touched = False
                            for c in root.findall('.//' + Q('c')):
                                if c.find(Q('f')) is None:
                                    continue
                                e = ec[c.attrib['r']]
                                new = e.find(Q('v'))
                                for oldv in [c.find(Q('v')), c.find(Q('is'))]:
                                    if oldv is not None:
                                        c.remove(oldv)
                                if 't' in e.attrib:
                                    c.attrib['t'] = e.attrib['t']
                                else:
                                    c.attrib.pop('t', None)
                                if new is not None:
                                    c.append(deepcopy(new))
                                touched = True
                            if touched:
                                final_parts[path] = ET.tostring(root, encoding='utf-8', xml_declaration=True)
                        ez.close()
                        ew.close()
                except Exception as exc:
                    engine = dict(status='FAIL', real_engine_recalculation=False, version=version, reason=str(exc))
            with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED) as zz:
                original_infos={i.filename:i for i in z.infolist()}
                for name in sorted(final_parts):
                    info=deepcopy(original_infos.get(name,zipfile.ZipInfo(name,(1980,1,1,0,0,0))))
                    info.compress_type=zipfile.ZIP_DEFLATED
                    zz.writestr(info,final_parts[name])
            # A numerically correct temporary transport is insufficient: verify
            # the delivered derivative itself can be opened and recalculated.
            if engine.get('status')=='PASS':
                final_dir=tmp/'final_readback';final_dir.mkdir()
                final_in=tmp/'delivered_copy.xlsx';final_in.write_bytes(dest.read_bytes())
                final_cmd=['soffice','-env:UserInstallation='+(tmp/'readback_profile').as_uri(),'--headless','--convert-to','xlsx','--outdir',str(final_dir),str(final_in)]
                try:
                    final_proc=subprocess.run(final_cmd,capture_output=True,text=True,timeout=180)
                    final_calc=final_dir/final_in.name
                    readback=dict(returncode=final_proc.returncode,delivered_input_sha256=sha(final_in),stdout=final_proc.stdout.replace(str(tmp),'<temporary>'),stderr=final_proc.stderr.replace(str(tmp),'<temporary>'),command=[x.replace(str(tmp),'<temporary>') for x in final_cmd])
                    diffs=[]
                    if final_proc.returncode==0 and final_calc.exists():
                        fw=openpyxl.load_workbook(final_calc,data_only=True)
                        for (sn,cell),value in oracle.items():
                            if not same(value,fw[sn][cell].value):diffs.append(dict(sheet=sn,cell=cell,expected=value,readback=fw[sn][cell].value))
                        fw.close()
                        readback.update(status='PASS' if not diffs else 'FAIL',formula_cells_compared=len(oracle),mismatches=diffs)
                    else:readback.update(status='FAIL',reason='delivered workbook could not be opened/recalculated')
                    engine['delivered_workbook_readback']=readback
                    if readback['status']!='PASS':engine['status']='FAIL'
                except Exception as exc:
                    engine['delivered_workbook_readback']=dict(status='FAIL',reason=str(exc));engine['status']='FAIL'
        with zipfile.ZipFile(dest) as dz:
            assert z.read(paths[EXCLUDED]) == dz.read(paths[EXCLUDED])
    dw = openpyxl.load_workbook(dest, data_only=False)
    dv = openpyxl.load_workbook(dest, data_only=True)
    preserved = 0
    for sh in sw:
        if sh.title == EXCLUDED:
            continue
        for row in sh:
            for c in row:
                k = (sh.title, c.coordinate)
                if k in changes:
                    assert dw[sh.title][c.coordinate].value == changes[k]['after']
                elif c.value is not None:
                    assert dw[sh.title][c.coordinate].value == c.value, k
                    preserved += 1
    day0 = [('07_连续称重', 'N' + str(r['row'])) for r in M if r['C'] == 0]
    idx = [(x['sheet'], x['cell']) for x in changes.values() if 'A3_' in x['reason']]
    engine['day0_zero_cells'] = len(day0)
    engine['day0_zero_pass'] = all((dv[s][c].value == 0 for s, c in day0))
    engine['index_missing_cells'] = len(idx)
    engine['index_missing_pass'] = all((dv[s][c].value in (None, '') for s, c in idx))
    engine['unmodified_literal_cells_verified'] = preserved
    engine['excluded_sheet_xml_byte_equal'] = True
    engine['normalized_original_formula_count'] = 1458
    engine['added_summary_formula_count'] = 435
    engine['final_formula_count'] = sum((c.data_type == 'f' for sh in dw if sh.title != EXCLUDED for row in sh for c in row))
    original_cache = openpyxl.load_workbook(source, data_only=True)
    cache_rows = []
    for (sn, cell), change in changes.items():
        old = original_cache[sn][cell].value
        new = dv[sn][cell].value
        category = 'INDEX_MISSING_ZERO_TO_EMPTY' if 'A3_' in change['reason'] else 'DAY0_AUX_EMPTY_TO_ZERO' if (sn, cell) in day0 else 'FIXED_SUMMARY_TO_FORMULA' if 'A4_' in change['reason'] else 'ORIGINAL_FORMULA_CACHE'
        cache_rows.append(dict(sheet=sn, cell=cell, category=category, original_cache=old, recalculated_cache=new, equal_under_empty_semantics=same(old, new), numeric_difference=new - old if isinstance(old, (int, float)) and isinstance(new, (int, float)) else None))
    engine['original_cache_comparison_cells'] = len(cache_rows)
    engine['cache_change_counts'] = {k: sum((x['category'] == k and (not x['equal_under_empty_semantics']) for x in cache_rows)) for k in sorted({x['category'] for x in cache_rows})}
    original_cache.close()
    sw.close()
    dw.close()
    dv.close()
    import csv

    def write_csv(path, values, fields):
        with path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
            writer.writeheader()
            writer.writerows(values)
    write_csv(tables / '公式修订映射.csv', list(changes.values()), ['sheet', 'cell', 'before', 'after', 'reason'])
    write_csv(tables / '公式缓存重算对照.csv', cache_rows, list(cache_rows[0]))
    write_csv(tables / '固定汇总复核.csv', fixed, ['sheet', 'cell', 'original', 'independent_recalc', 'equal', 'action'])
    (results / 'engine_validation.json').write_text(json.dumps(engine, ensure_ascii=False, indent=2))
    return dict(file=dest.name, sha256=sha(dest), engine=engine, changes=list(changes.values()), fixed=fixed)
