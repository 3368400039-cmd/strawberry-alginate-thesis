# Phase09B：新版主数据描述统计结果包

本包只新增派生计算、描述统计及替换准备资料，不修改论文或任何旧阶段成果。唯一数值主源为仓库根目录`实验记录.xlsx`，SHA-256锁定为`a63c8b0e1a07724e861d4b9a379ab632b3c0d41038f77310db36fb3b6b9f66f6`。`18_内部一致性检查`不参与分析、方法或有效性判断，保留原表。历史S1和Phase02数据没有进入新数值计算。

## 查看顺序

1. [公式整改与真实重算](audit/PHASE_09B_公式整改与重算验证.md)：1458公式、27辅助零值、6索引空值、435固定汇总及10标签的核验。
2. [统计口径、48格结果和QA](audit/PHASE_09B_新结果统计核验.md)。
3. [论文替换准备清单](audit/PHASE_09B_论文结果替换准备清单.md)：只规划，不改正文。
4. [全精度JSON](results/phase09b_results.json)、[主统计CSV](tables/新数据描述统计汇总.csv)、[六组新图及源数据](figures/)。

## 运行与复现

从仓库根目录运行（需要完整Git历史，以核对受保护路径）：

```bash
PYTHONDONTWRITEBYTECODE=1 python analysis/phase09b/scripts/analyze_new_records.py
PYTHONDONTWRITEBYTECODE=1 python analysis/phase09b/scripts/verify_reproduction.py
```

依赖为Python3.12、openpyxl、Matplotlib；独立核对额外使用NumPy。实际版本见`results/run_manifest.json`与`results/independent_numpy_validation.json`。字体使用环境已安装Noto Sans CJK。真实电子表格引擎为环境已有`soffice`，版本及命令见`results/engine_validation.json`。未安装未知插件，未上传论文数据到外部服务。

入口会生成派生副本并重算1893格公式，同时从原始数字另算48格描述统计。首次入口运行时QA12为FAIL（尚未执行本轮独立目录复现）；QA09还要求六图实际目视检查记录与当前PNG哈希相符。运行复现脚本后，重新生成正式目录QA及三报告。临时独立目录尚无自身目视/复现记录，入口stdout中出现QA未通过不等于数值复现失败；临时计算输出与正式包的逐项比较、独立数值实现及正式目录最终QA分别记录。复现脚本在临时独立目录重跑完整入口，并通过独立NumPy实现检查全部48格的均值、SD、极值与n。最终副本的OOXML封装同步标准化，逐格保留原始非派生文字/数值及排除表XML/原共享字符串，并另做真实引擎打开重算回读。

可显式选择`--out /tmp/phase09b_check`保存独立结果。`--skip-engine`仅供受限环境输出Python统计，不得据此声称真实Excel重算通过；引擎/相应QA保持FAIL。原件SHA不符、受保护路径变化或新结构/原汇总冲突时停止，不能自动借用旧数据替代。

## 两种失重率口径

主JSON/CSV/图采用原质量全精度先算每盒、再容器等权。派生Excel保留原先每盒先ROUND到2位再汇总的公式意义。差值单独见`tables/失重率舍入口径对照.csv`。不能混用主均值与另一口径SD，也不能据排名切换口径。

结果包仅用于带限定的描述比较，不提供ANOVA、p值、置信区间或显著性字母。工作簿参数记载、计算一致与独立实测来源证明是不同层次；后两项不能互相替代。完成后须停止并等待外部审核，未授权论文修订。
