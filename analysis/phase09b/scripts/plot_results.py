"""Publication-oriented new-data figures. All plotted coordinates are exported."""
from pathlib import Path
import os, datetime, math
os.environ.setdefault('MPLCONFIGDIR', '/tmp/phase09b_matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager, dates as mdates
from package_results import GROUPS, METRICS, UNITS, LABELS, write_csv
C = {'CK': '#24648d', 'Ca': '#ae7317', 'SA-Ca': '#bd4e79'}
MARK = {'CK': 'o', 'Ca': 's', 'SA-Ca': '^'}
LINE = {'CK': '-', 'Ca': '--', 'SA-Ca': '-.'}

def render_figures(out, result):
    out = Path(out) / 'figures'
    out.mkdir(parents=True, exist_ok=True)
    fp = Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')
    if fp.exists():
        font_manager.fontManager.addfont(str(fp))
        family = font_manager.FontProperties(fname=str(fp)).get_name()
    else:
        family = 'DejaVu Sans'
    plt.rcParams.update({'font.family': family, 'font.size': 11, 'axes.titlesize': 14, 'axes.labelsize': 12, 'axes.spines.top': False, 'axes.spines.right': False, 'axes.unicode_minus': False, 'svg.fonttype': 'none', 'svg.hashsalt': 'phase09b-strawberry'})
    figspec = []

    def save(fig, stem, metadata):
        fig.savefig(out / (stem + '.png'), dpi=220, facecolor='white', metadata={'Software': 'phase09b source-only analysis'})
        fig.savefig(out / (stem + '.svg'), facecolor='white', metadata={'Date': None, 'Creator': 'phase09b source-only analysis'})
        plt.close(fig)
        metadata.update(id=stem, files=[stem + '.png', stem + '.svg', stem + '_source.csv'])
        figspec.append(metadata)
    subtitles = {'mass_loss': 'L队列：失重率随贮藏时间的变化', 'decay_pct': 'L队列：累计腐烂比例', 'firmness': 'D队列：表观硬度随取样日的变化', 'TSS': 'D队列：可溶性固形物随取样日的变化'}
    foot = {'mass_loss': '点/线：容器等权均值；误差线：容器间样本SD。每组每时点n=9盒，Ca Day2 n=8；每盒4果。', 'decay_pct': '线：累计腐烂果/初始36果；散点：9盒各4果的比例；无误差线/推断区间，水平错开仅便辨识。', 'firmness': '线：容器均值±样本SD；散点：3批D容器。每组每时点n=3盒；Day4可测果CK/Ca/SA-Ca为8/9/8。', 'TSS': '线：容器均值±样本SD；每组每时点n=3盒；Day4可测果CK/Ca/SA-Ca为8/9/8，每果一次读数。'}
    names = ['P09B_F01_失重率', 'P09B_F02_累计腐烂', 'P09B_F03_表观硬度', 'P09B_F04_TSS']
    for metric, stem in zip(METRICS, names):
        rows = [r for r in result['summary'] if r['metric'] == metric]
        ur = [r for r in result['container_results'] if r['metric'] == metric]
        write_csv(out / (stem + '_source.csv'), rows)
        write_csv(out / (stem + '_containers.csv'), ur, list(dict.fromkeys((k for r in ur for k in r))))
        fig, ax = plt.subplots(figsize=(9.5, 6.2))
        fig.subplots_adjust(left=0.11, right=0.97, top=0.84, bottom=0.25)
        ax.set_title(subtitles[metric], pad=16)
        ax.grid(axis='y', color='#d8dfe5', linewidth=0.65)
        ax.set_axisbelow(True)
        series = []
        for gi, g in enumerate(GROUPS):
            rr = sorted([r for r in rows if r['group'] == g], key=lambda r: r['day'])
            x = [r['day'] for r in rr]
            y = [r['mean'] for r in rr]
            sd = [r['sd'] for r in rr]
            if metric == 'decay_pct':
                ax.plot(x, y, color=C[g], marker=MARK[g], linestyle=LINE[g], linewidth=2, markersize=6, label=g)
                for d in x:
                    uu = sorted([r for r in ur if r['group'] == g and r['day'] == d], key=lambda r: r['unit'])
                    ax.scatter([d + (gi - 1) * 0.055 + (k - 4) * 0.006 for k in range(len(uu))], [r['value'] for r in uu], color=C[g], marker=MARK[g], s=20, alpha=0.32, edgecolors='none')
            else:
                ax.errorbar(x, y, yerr=sd, color=C[g], marker=MARK[g], linestyle=LINE[g], linewidth=2, markersize=6, capsize=3, label=g)
                if metric in ['firmness', 'TSS']:
                    for d in x:
                        uu = sorted([r for r in ur if r['group'] == g and r['day'] == d], key=lambda r: r['batch'])
                        ax.scatter([d + (gi - 1) * 0.055 + (k - 1) * 0.025 for k in range(len(uu))], [r['value'] for r in uu], color=C[g], marker=MARK[g], s=24, alpha=0.3, edgecolors='none')
            series.append(dict(group=g, day=x, mean=y, sd=sd if metric != 'decay_pct' else None, n_containers=[r['n_containers'] for r in rr], n_fruits=[r['n_fruits'] for r in rr], calendar_dates=[r['calendar_dates'] for r in rr]))
        ax.set_xticks([0, 1, 2, 3, 4] if metric in ['mass_loss', 'decay_pct'] else [0, 2, 4])
        ax.set_xlim(-0.2, 4.2)
        ax.set_xlabel('贮藏日 / d（同一L容器连续观察）' if metric in ['mass_loss', 'decay_pct'] else '取样日 / d（不同D容器、不同果实）')
        ax.set_ylabel(LABELS[metric] + ' / ' + UNITS[metric])
        ax.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.025), frameon=False)
        if metric == 'decay_pct':
            ax.set_ylim(-2, 105)
        elif metric == 'mass_loss':
            ax.set_ylim(bottom=0)
        elif metric == 'firmness':
            ax.set_ylim(bottom=0)
        fig.text(0.5, 0.12, foot[metric], ha='center', va='center', fontsize=9)
        note = '三批Day0：2026-10-05、10-13、10-21；Day0为处理沥液后基线。'
        if metric in ['firmness', 'TSS']:
            note += '\nD连线仅示日别组均值；非同果轨迹，技术重复不扩大独立n。'
        fig.text(0.5, 0.055, note, ha='center', va='center', fontsize=9, color='#3d4d5a')
        save(fig, stem, dict(metric=metric, source_rows=rows, series=series, container_source_file=stem + '_containers.csv', errorbar='none' if metric == 'decay_pct' else 'container sample SD, ddof=1'))
    stem = 'P09B_F05_批次差异'
    rows = [r for r in result['batch_summary'] if r['day'] == 4]
    write_csv(out / (stem + '_source.csv'), rows)
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    fig.subplots_adjust(left=0.09, right=0.98, top=0.86, bottom=0.14, hspace=0.4, wspace=0.23)
    for ax, metric in zip(axes.flat, METRICS):
        for gi, g in enumerate(GROUPS):
            rr = [next((r for r in rows if r['metric'] == metric and r['group'] == g and (r['batch'] == b))) for b in ['B1', 'B2', 'B3']]
            ax.scatter([i + (gi - 1) * 0.16 for i in range(3)], [r['mean'] for r in rr], color=C[g], marker=MARK[g], s=50, label=g)
        ax.set_xticks([0, 1, 2], ['B1\n10-05', 'B2\n10-13', 'B3\n10-21'])
        ax.set_ylabel(LABELS[metric] + ' / ' + UNITS[metric])
        ax.set_title('Day4 ' + LABELS[metric], fontsize=12)
        ax.grid(axis='y', alpha=0.3)
        ax.set_axisbelow(True)
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.93))
    fig.suptitle('三个日期批次的Day4组均值', y=0.98, fontsize=16)
    fig.text(0.5, 0.055, '每批每组L为3盒，D为1盒；各日历日期为该批Day0。无误差线/推断区间。\n横轴比较不同批次，不表示同果纵向变化；D每格仅1盒，不能估计格内容器SD。', ha='center', fontsize=9)
    save(fig, stem, dict(metric='batch_day4', source_rows=rows, errorbar='none', batch_start_dates=['2026-10-05', '2026-10-13', '2026-10-21']))
    stem = 'P09B_F06_温湿度'
    rows = result['environment_records']
    write_csv(out / (stem + '_source.csv'), rows)
    fig, axes = plt.subplots(2, 3, figsize=(12, 7), sharey='row')
    fig.subplots_adjust(left=0.08, right=0.98, top=0.86, bottom=0.16, wspace=0.15, hspace=0.35)
    for j, b in enumerate(['B1', 'B2', 'B3']):
        rr = sorted([r for r in rows if r['batch'] == b], key=lambda r: r['date_time'])
        x = [datetime.datetime.fromisoformat(r['date_time']) for r in rr]
        for i, (metric, label, color) in enumerate([('temperature_C', '温度 / ℃', '#ad6229'), ('relative_humidity_pct', '相对湿度 / %', '#257696')]):
            ax = axes[i, j]
            ax.plot(x, [r[metric] for r in rr], marker='o', markersize=4, color=color, linewidth=1.5)
            ax.xaxis.set_major_locator(mdates.DayLocator())
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
            ax.tick_params(axis='x', labelsize=9)
            ax.grid(alpha=0.25)
            if j == 0:
                ax.set_ylabel(label)
            if i == 0:
                ax.set_title(b + '（2026年；n=10监测点）', fontsize=11)
        axes[1, j].set_xlabel('实际监测日期（09:00与17:00）', fontsize=10)
    fig.suptitle('贮藏环境的离散温湿度监测', y=0.96, fontsize=16)
    fig.text(0.5, 0.055, '三批共30个时间监测点，不是30次独立贮藏实验；线连接观测时点，无误差线。\n仅呈现新文件实测记录，不擅自添加未确认的贮藏目标带或恒湿设定。', ha='center', fontsize=9)
    save(fig, stem, dict(metric='environment', source_rows=rows, errorbar='none', n_time_records=30))
    return figspec
