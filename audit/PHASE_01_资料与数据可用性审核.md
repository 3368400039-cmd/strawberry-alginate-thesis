# Phase 01｜资料与数据可用性审核

正式题目：《可食性海藻酸钠膜对草莓常温保鲜效果的研究》
学校：四川工业科技学院｜本科毕业实验研究
审核日期：2026-11-10（UTC+8）｜性质：机器辅助初审，等待外部人工验收

## 1. 审核结论与范围

**本轮资料建档及计算核验已完成；科研放行结论：暂不进入实验数据正式统计研究。**
主要阻碍是数据原始来源链及实际实验独立性未获外部证据支持、582个公式存在非规范双等号存储、操作SOP不足以复现实验。可以复算不等于实验真实、独立或因果解释成立。不得据本报告宣布处理有效、显著或已验收。

未运行任何假设检验、效应显著性分析或正式论文结果图表，未制作论文目录、章节大纲或正文。本报告表格均为审计登记及校验，不是论文结果表。未修改任何原始资料。

### 1.1 实际技能与工具

实际调用云skills.list两页（列完25项）及executor skills.list（0项）。读取并采用`data-analytics:analyze-data-quality`的主键、缺失、关联、粒度、来源核验流程；读取并采用`data-analytics:validate-data`的计算与支持性复核流程（本次是质量审核中的局部核验，不是另开深度分析）。读取Data index执行用户指定Markdown交付优先。两个技能的共用shared文档读取返回`failed to read skill resource`，未声称完整执行不可访问部分。

未发现thesis-evidence-audit、undergrad-thesis-workflow或独立DOCX/document-processing技能。可用的convert-to-doc面向已有Data应用转文档，不适合只读模板审计，未使用。university-paper-writing可见但本轮不写论文，未调用。不因“审核团队”角色描述虚称多人独立评议，未启动子代理。

工具依赖：Python openpyxl（公式/缓存双读）、PyMuPDF（逐页文字读取及渲染抽查）、python-docx与lxml（段落/样式/OOXML）、Pillow（PNG校验）、hashlib（SHA-256）、Git。均使用已安装工具，无新增依赖；没有套用营销问卷方法。读取cloud-environment-runtime及networking，仅用于执行环境与Git连接；未变更、重应用或发布云环境配置。

### 1.2 方法与边界

对仓库所有业务文件递归清点（不把.git内部对象作为研究资料），对每个原件计算字节级SHA-256；PDF逐页读取文本，检查页数、文字层和首末内容线索，扫描PDF仅抽查渲染，不等于完整OCR或逐字精读；PNG实际查看。DOCX读取342个顶层段落、2张表、10个节及XML样式/页眉页脚。Excel读取全部14表的非空单元格、公式及缓存，检查候选主键、复合键、单位/果实/组/批次关联、日期偏移、合理范围及派生计算。复算只用于核验原有汇总；未保存重算工作簿。

## 2. 仓库文件清单与分类统计

审计开始时工作分支为`work`，工作区干净；新建`audit/phase01-source-data`。以下为新增交付物之前的36个原始业务文件。路径均以仓库根`/workspace/strawberry-alginate-thesis/`为基准，每个列出路径即实际相对路径；未发现嵌套业务文件。类别A中文PDF、B外文PDF（不冒称全部英文全文）、C学校Word、D实验Excel、E图片/截图、F其他。

|类别|文件数|
|---|---:|
|A|20|
|B|11|
|C|1|
|D|1|
|E|2|
|F|1|

31个PDF中3组字节完全重复，按指纹去重后28份PDF；近似版本不作自动去重。

### F01｜4EA7E7811F4D44AB8B3892557FC72A52.pdf

- 路径：`4EA7E7811F4D44AB8B3892557FC72A52.pdf`
- 类别/格式/大小：A / .pdf / 448358 bytes
- SHA-256：`525d5c9c5395ae73c9041326b9c7f460e1b673d22f2a9af1ec0bb61fb6971354`
- 可读性：PDF可打开，6页；0页无可抽取正文
- 用途及缺损线索：马陆葡萄/海藻酸钠-溶菌酶；原始研究；间接（异果种、冷藏）
- 重复登记：未发现同SHA副本

### F02｜Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf

- 路径：`Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf`
- 类别/格式/大小：B / .pdf / 561957 bytes
- SHA-256：`7a795bdae972cb1c90d740c657642ab8d6e6d71312a405a24c36f7b1baa064bb`
- 可读性：PDF可打开，11页；0页无可抽取正文
- 用途及缺损线索：英题/摘要、泰语正文；原始研究；草莓SA-Ca冷藏，间接于常温；不计为英文全文
- 重复登记：完全重复：Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf

### F03｜Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf

- 路径：`Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf`
- 类别/格式/大小：B / .pdf / 561957 bytes
- SHA-256：`7a795bdae972cb1c90d740c657642ab8d6e6d71312a405a24c36f7b1baa064bb`
- 可读性：PDF可打开，11页；0页无可抽取正文
- 用途及缺损线索：英题/摘要、泰语正文；原始研究；草莓SA-Ca冷藏，间接于常温；不计为英文全文
- 重复登记：完全重复：Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf

### F04｜Greta_Peretto_PhD_dissertation.pdf

- 路径：`Greta_Peretto_PhD_dissertation.pdf`
- 类别/格式/大小：B / .pdf / 1586149 bytes
- SHA-256：`a056765038865fdb6c5bfaa2f69cc83e8ca7f4f0cbee996bf198e67c163ef151`
- 可读性：PDF可打开，202页；0页无可抽取正文
- 用途及缺损线索：英文为主、意大利语封面；博士论文/原始研究合集；浆果采后相关；学位论文本体DOI未确认
- 重复登记：未发现同SHA副本

### F05｜Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf

- 路径：`Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf`
- 类别/格式/大小：A / .pdf / 861790 bytes
- SHA-256：`d9fbb2814e9a053f20f66993548aec97ca6ec24d38820a49fc3aaa4273c7d8e0`
- 可读性：PDF可打开，6页；0页无可抽取正文
- 用途及缺损线索：哈密瓜复合处理；原始研究；间接（异果种、多活性组分）
- 重复登记：未发现同SHA副本

### F06｜QQ20261110-155042.png

- 路径：`QQ20261110-155042.png`
- 类别/格式/大小：E / .png / 524423 bytes
- SHA-256：`e19a4e3f73f70e6ec5424712340ed25fcf8e8614d99f58bb76651a286c790a3e`
- 可读性：PNG完整解码且已目视查看
- 用途及缺损线索：文献检索截图，不是实验原始照片
- 重复登记：未发现同SHA副本

### F07｜QQ20261110-155132.png

- 路径：`QQ20261110-155132.png`
- 类别/格式/大小：E / .png / 663030 bytes
- SHA-256：`07f5a2b789846a1d078f26e22bab6fb0cb96984210e3bd2062c0ba59e762848f`
- 可读性：PNG完整解码且已目视查看
- 用途及缺损线索：文献检索截图，不是实验原始照片
- 重复登记：未发现同SHA副本

### F08｜README.md

- 路径：`README.md`
- 类别/格式/大小：F / .md / 28 bytes
- SHA-256：`6aaacb9b48b47ec377c73f1054539325988871190f7b1976d53954dc987b6c92`
- 可读性：UTF-8可读
- 用途及缺损线索：仓库说明，内容仅项目名称
- 重复登记：未发现同SHA副本

### F09｜S1-2018-333159-abstract.pdf

- 路径：`S1-2018-333159-abstract.pdf`
- 类别/格式/大小：B / .pdf / 287363 bytes
- SHA-256：`002b73d5a7840f349d5977b2076af85acbb7aaeaeefbffb70b8c793d2b3ebd94`
- 可读性：PDF可打开，2页；0页无可抽取正文
- 用途及缺损线索：印尼语/英语摘要；仅摘要，不是全文；热带草莓涂膜；原研究性质待全文核验
- 重复登记：未发现同SHA副本

### F10｜coatings-14-01331 2.pdf

- 路径：`coatings-14-01331 2.pdf`
- 类别/格式/大小：B / .pdf / 3272094 bytes
- SHA-256：`0daef1792527746bb83ddc35429acb73fe612ddf47de9e8cbe05f879b92a81a4`
- 可读性：PDF可打开，15页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；草莓海藻酸钠-蒙脱土复合膜；相关但材料不同
- 重复登记：未发现同SHA副本

### F11｜eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf

- 路径：`eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf`
- 类别/格式/大小：B / .pdf / 224783 bytes
- SHA-256：`d4f9e735c0b02f01bf568dd9ce8b06485d00fadfe9a9047a1d8664dc78606634`
- 可读性：PDF可打开，7页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；茶多酚/海藻酸钠草莓；相关；温度与结果可信度需后续精读
- 重复登记：完全重复：eb0e68fb8f6c2a811368a62e444e782162e8.pdf

### F12｜eb0e68fb8f6c2a811368a62e444e782162e8.pdf

- 路径：`eb0e68fb8f6c2a811368a62e444e782162e8.pdf`
- 类别/格式/大小：B / .pdf / 224783 bytes
- SHA-256：`d4f9e735c0b02f01bf568dd9ce8b06485d00fadfe9a9047a1d8664dc78606634`
- 可读性：PDF可打开，7页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；茶多酚/海藻酸钠草莓；相关；温度与结果可信度需后续精读
- 重复登记：完全重复：eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf

### F13｜foods-08-00203-v2 2.pdf

- 路径：`foods-08-00203-v2 2.pdf`
- 类别/格式/大小：B / .pdf / 2022786 bytes
- SHA-256：`ca6776176de675559ba75c9b8fa207704ce4a835ea710d6fff973b99ecd18f0f`
- 可读性：PDF可打开，21页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；甜瓜/草莓海藻酸钠膜及水分屏障；相关
- 重复登记：未发现同SHA副本

### F14｜jcs-04-00123 2.pdf

- 路径：`jcs-04-00123 2.pdf`
- 类别/格式/大小：B / .pdf / 1592335 bytes
- SHA-256：`424d6ba731c6e2997fba900c8e77c7cc077de75fe7562a0580901122f541c534`
- 可读性：PDF可打开，15页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；鲜切草莓SA-Ca；相关，但不能直接外推完整果常温
- 重复登记：完全重复：jcs-04-00123.pdf

### F15｜jcs-04-00123.pdf

- 路径：`jcs-04-00123.pdf`
- 类别/格式/大小：B / .pdf / 1592335 bytes
- SHA-256：`424d6ba731c6e2997fba900c8e77c7cc077de75fe7562a0580901122f541c534`
- 可读性：PDF可打开，15页；0页无可抽取正文
- 用途及缺损线索：英文原始研究；鲜切草莓SA-Ca；相关，但不能直接外推完整果常温
- 重复登记：完全重复：jcs-04-00123 2.pdf

### F16｜mh611.pdf

- 路径：`mh611.pdf`
- 类别/格式/大小：B / .pdf / 79444 bytes
- SHA-256：`954c07da9bbb54aa4db3426b974de56b095e71f0a5f30e180da430a6f83708ae`
- 可读性：PDF可打开，1页；0页无可抽取正文
- 用途及缺损线索：英文文摘单页；藻酸盐/拮抗酵母草莓；相关；全文缺失
- 重复登记：未发现同SHA副本

### F17｜中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf

- 路径：`中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf`
- 类别/格式/大小：A / .pdf / 1383975 bytes
- SHA-256：`4acf4c5f7f4f7308aa449d8158d396a7a5501658dc8646e25fe96335346ac940`
- 可读性：PDF可打开，7页；0页无可抽取正文
- 用途及缺损线索：原始研究；圣女果复合膜；间接
- 重复登记：未发现同SHA副本

### F18｜四川工业科技学院本科毕业设计(论文)-样式模板(定稿).docx

- 路径：`四川工业科技学院本科毕业设计(论文)-样式模板(定稿).docx`
- 类别/格式/大小：C / .docx / 138521 bytes
- SHA-256：`1ba80eb5e63d06a3242162cda358648a8c6a303490b040e5069e9f452a6656f7`
- 可读性：DOCX结构可读
- 用途及缺损线索：学校格式证据；不含本课题已确认作者信息
- 重复登记：未发现同SHA副本

### F19｜基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf

- 路径：`基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf`
- 类别/格式/大小：A / .pdf / 5038343 bytes
- SHA-256：`71b6a326ae412bdd5721d35ca7e295081adea4111350da7f3750f950bb0f6f90`
- 可读性：PDF可打开，86页；0页无可抽取正文
- 用途及缺损线索：硕士论文/原始研究；溶菌酶相转变膜草莓；间接（材料不同）
- 重复登记：未发现同SHA副本

### F20｜壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf

- 路径：`壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf`
- 类别/格式/大小：A / .pdf / 213342 bytes
- SHA-256：`819b79c2ebdeca081808a53db19acf6197da2be24fd730c2e107d600100cc90e`
- 可读性：PDF可打开，7页；0页无可抽取正文
- 用途及缺损线索：原始研究；银纳米复合物草莓；间接，不能替代SA证据
- 重复登记：未发现同SHA副本

### F21｜壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf

- 路径：`壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf`
- 类别/格式/大小：A / .pdf / 5617725 bytes
- SHA-256：`80dee03ecf1ed141a567f3e5463f9eca1de3473c022484878aed2bfc80ab257a`
- 可读性：PDF可打开，101页；0页无可抽取正文
- 用途及缺损线索：硕士论文/原始研究；双金属纳米酶膜；间接
- 重复登记：未发现同SHA副本

### F22｜柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf

- 路径：`柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf`
- 类别/格式/大小：A / .pdf / 3527405 bytes
- SHA-256：`65f17f5af496699859c550b947a7014e8dbe316d88b2ba34336b215f82786271`
- 可读性：PDF可打开，5页；0页无可抽取正文
- 用途及缺损线索：原始研究；果胶-SA草莓；相关但复合配方不同
- 重复登记：未发现同SHA副本

### F23｜油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf

- 路径：`油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf`
- 类别/格式/大小：A / .pdf / 7253062 bytes
- SHA-256：`e10b3b5f65d3815976c3d0764b5cd50f5ed27d1836f4bd91d225657703b11d17`
- 可读性：PDF可打开，104页；0页无可抽取正文
- 用途及缺损线索：硕士论文/原始研究；蛋白-SA膜水果；相关但材料不同
- 重复登记：未发现同SHA副本

### F24｜海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf

- 路径：`海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf`
- 类别/格式/大小：A / .pdf / 1454285 bytes
- SHA-256：`9874a84f6002329e1dd2722a1f3ee22fc1e5a3cbeed8b22588ba93a55c4e30f8`
- 可读性：PDF可打开，4页；0页无可抽取正文
- 用途及缺损线索：原始研究；海藻糖/茶多酚白灵菇；低相关；海藻糖≠海藻酸钠
- 重复登记：未发现同SHA副本

### F25｜海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf

- 路径：`海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf`
- 类别/格式/大小：A / .pdf / 5362932 bytes
- SHA-256：`5352e499fcc9b3b00c01260d7e694ceceef2094aa8207e3eefb5d5e68db660f2`
- 可读性：PDF可打开，73页；2页无可抽取正文
- 用途及缺损线索：硕士论文/原始研究；樱桃番茄海藻糖；低相关；海藻糖≠SA
- 重复登记：未发现同SHA副本

### F26｜海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf

- 路径：`海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf`
- 类别/格式/大小：A / .pdf / 2346157 bytes
- SHA-256：`07e8969a8dfbfb153ed2c30ed25f6d7562c0783833996274c313422b95907c24`
- 可读性：PDF可打开，9页；0页无可抽取正文
- 用途及缺损线索：原始研究；SA/壳聚糖/纳米硒草莓；相关但多组分
- 重复登记：未发现同SHA副本

### F27｜海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf

- 路径：`海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf`
- 类别/格式/大小：A / .pdf / 6840001 bytes
- SHA-256：`b071ee75d131b94d86450166dbde8172cc587fde9e68866c8c950255d1f2d5c7`
- 可读性：PDF可打开，71页；71页无可抽取正文
- 用途及缺损线索：扫描硕士论文，首尾渲染抽查；冷藏草莓风味；相关；未OCR、完整正文可读性未确认
- 重复登记：未发现同SHA副本

### F28｜海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf

- 路径：`海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf`
- 类别/格式/大小：A / .pdf / 1641594 bytes
- SHA-256：`24981bf71632a7ec94e46fdd1fc74cec695829c4ee7092371b8b01a886aa9a9b`
- 可读性：PDF可打开，4页；0页无可抽取正文
- 用途及缺损线索：综述；果蔬SA进展；相关；疑似同作者网络首发的后续版本，需比对
- 重复登记：近似版本候选：梁昭榆同主题另一文件

### F29｜海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf

- 路径：`海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf`
- 类别/格式/大小：A / .pdf / 834241 bytes
- SHA-256：`7d9ffd1ad25f2020ef54dbe6653fd33b7ea58d82f818a64789607e0acdd577b1`
- 可读性：PDF可打开，5页；0页无可抽取正文
- 用途及缺损线索：综述/网络首发；相关；疑似另一梁昭榆文件的版本，不能按两项独立证据计数
- 重复登记：近似版本候选：梁昭榆同主题另一文件

### F30｜海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf

- 路径：`海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf`
- 类别/格式/大小：A / .pdf / 1448754 bytes
- SHA-256：`92afac99ce254b88546a54480634217ad6ada7c4cf87763d0cc664fb55c0b38a`
- 可读性：PDF可打开，14页；0页无可抽取正文
- 用途及缺损线索：原始研究；污泥厌氧氨氧化；与食品草莓保鲜明显无关，排除核心证据但保留原件
- 重复登记：未发现同SHA副本

### F31｜研究数据S1.xlsx

- 路径：`研究数据S1.xlsx`
- 类别/格式/大小：D / .xlsx / 125235 bytes
- SHA-256：`7ffc712bbfd8648fbd359a3bf26e6af75af2a21fde7b7be801c862546d3cb550`
- 可读性：14表结构/公式/缓存可读
- 用途及缺损线索：用户提交的主要实验研究数据；来源真实性待补证
- 重复登记：未发现同SHA副本

### F32｜空气负离子环境中草莓采后品质的变化_范鹏.pdf

- 路径：`空气负离子环境中草莓采后品质的变化_范鹏.pdf`
- 类别/格式/大小：A / .pdf / 2400692 bytes
- SHA-256：`c735e005609562535f83bce4a1ab3cf638caffbeabb35c8f77e5daf288f6dce1`
- 可读性：PDF可打开，11页；0页无可抽取正文
- 用途及缺损线索：原始研究；负离子草莓采后；间接（处理和温度不同）
- 重复登记：未发现同SHA副本

### F33｜脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf

- 路径：`脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf`
- 类别/格式/大小：A / .pdf / 2948042 bytes
- SHA-256：`e62021d88ed63646a67802aa433678f55ce9bbcab99ac71968498ca1ebde40d3`
- 可读性：PDF可打开，14页；0页无可抽取正文
- 用途及缺损线索：原始研究；KGM/SA脂肪酸膜材料性能；间接；SA在该文亦可指硬脂酸，须辨义
- 重复登记：未发现同SHA副本

### F34｜茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf

- 路径：`茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf`
- 类别/格式/大小：A / .pdf / 1852904 bytes
- SHA-256：`0aba23c944ac72f509bcd19ef4d506c2d7f1c46c4ec4b132fff6da7d626901a8`
- 可读性：PDF可打开，7页；0页无可抽取正文
- 用途及缺损线索：原始研究；茶多糖-SA草莓；相关但4℃；p1将草莓称为呼吸跃变型，存在科学表述疑点，不直接采信
- 重复登记：未发现同SHA副本

### F35｜茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf

- 路径：`茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf`
- 类别/格式/大小：A / .pdf / 990499 bytes
- SHA-256：`2c130df5506a3646ca24f441ba1d2f371b1016fec4325109741d64bb60d1c7a1`
- 可读性：PDF可打开，5页；0页无可抽取正文
- 用途及缺损线索：原始研究；茶多酚-SA草莓；相关但4℃
- 重复登记：未发现同SHA副本

### F36｜草莓的涂膜保鲜研究.pdf

- 路径：`草莓的涂膜保鲜研究.pdf`
- 类别/格式/大小：A / .pdf / 205343 bytes
- SHA-256：`61c82c555105dcce92813d7b49fb027361bf8242dc34f03e33466757ae83855f`
- 可读性：PDF可打开，4页；0页无可抽取正文
- 用途及缺损线索：原始研究；乳状涂膜草莓常温；相关；4页仅231—234，文章编号提示5页且末页参考文献仅[1]，疑缺末页
- 重复登记：未发现同SHA副本

## 3. 重复、损坏与文献初步质量

### 3.1 重复登记（只登记，未删除）

- 完全重复：`Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf` ↔ `Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf`。字节SHA及归一化逐页抽取文本指纹均相同。
- 完全重复：`eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf` ↔ `eb0e68fb8f6c2a811368a62e444e782162e8.pdf`。字节SHA及归一化逐页抽取文本指纹均相同。
- 完全重复：`jcs-04-00123 2.pdf` ↔ `jcs-04-00123.pdf`。字节SHA及归一化逐页抽取文本指纹均相同。

梁昭榆两份综述题名“在/对”及版式不同：一份4页，标示2026年第7期，含DOI；一份5页，含2026-01-19网络首发封页。不能凭题名认定两篇独立综述，也不能判定完全重复；后续应核对正文及出版版本，引用采用经确认的一个版本。其余归一化全文文本指纹未发现额外相同组；未做全部非重复文献的语义相似性判定。

### 3.2 完整性与文种

未发现打不开的PDF或损坏的Office压缩包/PNG，但这不证明内容齐全。重点限制：

- `mh611.pdf`仅1页题录摘要，原始论文刊页84—90；不是7页全文。
- `S1-2018-333159-abstract.pdf`仅2页印尼语/英语摘要，页码xiv等；不是学位论文全文。
- `草莓的涂膜保鲜研究.pdf`共4页，231—234，首篇文章编号尾码05且末页参考文献只到[1]；疑少第235页，需权威全文核对，不武断认定损坏。
- 朱金花扫描论文71页全部缺乏可用文字层；已查看封面及末页（末页空白），仅确认可以渲染，不把71页自动记为全文已读。文件名“复含”与封面“复合”不一致。需后续OCR/逐页核查正文连续性。
- 夏明慧论文73页中2页无抽取文字（含封面），其他页有文字；封面/空白页不等同损坏。
- `Effect+...`两份实为泰语正文伴英题/摘要；Greta论文为英文主体、意大利语封面；不得把外文文件总数当英文全文数。
- 原始命名中的哈希串、加号、“ 2/3”、拼写与题名不一致仅登记，未重命名。

外文PDF11份中英文主体7份（含mh611摘要与两组英文重复），泰语正文2份（同一文献副本），印尼语/英语摘要1份，英文主体/意大利语封面学位论文1份。按字节去重，外文8份；中文PDF20份。所有研究类型判断为题名、摘要/方法标记初判，不能代表全文证据已掌握。

### 3.3 单篇初步登记

下表DOI仅记录本篇题录/首部可识别DOI；“未确认”不等于没有DOI，不把参考文献中的DOI错当本篇DOI。未联网核验期刊身份、撤稿、版本或出版真实性。

|文件|页数|研究类型、相关性与限制|本篇DOI线索|
|---|---:|---|---|
|4EA7E7811F4D44AB8B3892557FC72A52.pdf|6|马陆葡萄/海藻酸钠-溶菌酶；原始研究；间接（异果种、冷藏）|未确认|
|Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf|11|英题/摘要、泰语正文；原始研究；草莓SA-Ca冷藏，间接于常温；不计为英文全文|未确认|
|Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf|11|英题/摘要、泰语正文；原始研究；草莓SA-Ca冷藏，间接于常温；不计为英文全文|未确认|
|Greta_Peretto_PhD_dissertation.pdf|202|英文为主、意大利语封面；博士论文/原始研究合集；浆果采后相关；学位论文本体DOI未确认|未确认|
|Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf|6|哈密瓜复合处理；原始研究；间接（异果种、多活性组分）|10.13982/j.mfst.1673-9078.2015.4.040|
|S1-2018-333159-abstract.pdf|2|印尼语/英语摘要；仅摘要，不是全文；热带草莓涂膜；原研究性质待全文核验|未确认|
|coatings-14-01331 2.pdf|15|英文原始研究；草莓海藻酸钠-蒙脱土复合膜；相关但材料不同|10.3390/coatings14101331|
|eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf|7|英文原始研究；茶多酚/海藻酸钠草莓；相关；温度与结果可信度需后续精读|10.19026/ajfst.9.1981|
|eb0e68fb8f6c2a811368a62e444e782162e8.pdf|7|英文原始研究；茶多酚/海藻酸钠草莓；相关；温度与结果可信度需后续精读|10.19026/ajfst.9.1981|
|foods-08-00203-v2 2.pdf|21|英文原始研究；甜瓜/草莓海藻酸钠膜及水分屏障；相关|10.3390/foods8060203|
|jcs-04-00123 2.pdf|15|英文原始研究；鲜切草莓SA-Ca；相关，但不能直接外推完整果常温|10.3390/jcs4030123|
|jcs-04-00123.pdf|15|英文原始研究；鲜切草莓SA-Ca；相关，但不能直接外推完整果常温|10.3390/jcs4030123|
|mh611.pdf|1|英文文摘单页；藻酸盐/拮抗酵母草莓；相关；全文缺失|未确认|
|中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf|7|原始研究；圣女果复合膜；间接|10.16101/j.cnki.cn32-1749/z.2026.02.002|
|基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf|86|硕士论文/原始研究；溶菌酶相转变膜草莓；间接（材料不同）|未确认|
|壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf|7|原始研究；银纳米复合物草莓；间接，不能替代SA证据|首部DOI被换行截断，待核对|
|壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf|101|硕士论文/原始研究；双金属纳米酶膜；间接|未确认|
|柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf|5|原始研究；果胶-SA草莓；相关但复合配方不同|10.13684/j.cnki.spkj.2017.03.015|
|油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf|104|硕士论文/原始研究；蛋白-SA膜水果；相关但材料不同|未确认|
|海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf|4|原始研究；海藻糖/茶多酚白灵菇；低相关；海藻糖≠海藻酸钠|未确认|
|海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf|73|硕士论文/原始研究；樱桃番茄海藻糖；低相关；海藻糖≠SA|未确认|
|海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf|9|原始研究；SA/壳聚糖/纳米硒草莓；相关但多组分|首部可读：10.13995/j.cnki.11-1802/ts.041356（去除排版空格）|
|海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf|71|扫描硕士论文，首尾渲染抽查；冷藏草莓风味；相关；未OCR、完整正文可读性未确认|未确认|
|海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf|4|综述；果蔬SA进展；相关；疑似同作者网络首发的后续版本，需比对|10.16693/j.cnki.1671-9646（X）.2026.14.020|
|海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf|5|综述/网络首发；相关；疑似另一梁昭榆文件的版本，不能按两项独立证据计数|未确认|
|海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf|14|原始研究；污泥厌氧氨氧化；与食品草莓保鲜明显无关，排除核心证据但保留原件|10.19674/j.cnki.issn1000-6923.20261009.008|
|空气负离子环境中草莓采后品质的变化_范鹏.pdf|11|原始研究；负离子草莓采后；间接（处理和温度不同）|10.13624/j.cnki.issn.1001-7445.2026.0984|
|脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf|14|原始研究；KGM/SA脂肪酸膜材料性能；间接；SA在该文亦可指硬脂酸，须辨义|10.16429/j.1009-7848.2026.07.015|
|茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf|7|原始研究；茶多糖-SA草莓；相关但4℃；p1将草莓称为呼吸跃变型，存在科学表述疑点，不直接采信|10.19362/j.cnki.cn10-1400/tb.2024.01.002|
|茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf|5|原始研究；茶多酚-SA草莓；相关但4℃|未确认|
|草莓的涂膜保鲜研究.pdf|4|原始研究；乳状涂膜草莓常温；相关；4页仅231—234，文章编号提示5页且末页参考文献仅[1]，疑缺末页|未确认|

两张PNG均为文献平台题录/摘要截图：155042为李勇锋茶多糖-SA论文（DOI与对应PDF相符）；155132为2024年《不同处理对马铃薯货架期内保鲜效果的影响》题录摘要，属于异果种间接背景且无对应完整PDF。截图不是全文，也不是实验照片。

茶多糖论文p1“草莓是呼吸跃变型果实”的表述与通常食品采后分类有冲突，列为待权威来源复核的科学性警讯；不据单篇原文直接移植该表述。所有冷藏、鲜切、多组分、其他果蔬研究只能提供限定背景，不直接证明本项目完整草莓常温下单独SA效应。

## 4. 学校模板关键规则

证据定位P为python-docx顶层段落从1起计数，节号/样式名对应OOXML；不是渲染后页码。未运行Word/LibreOffice排版验证，动态目录和实际分页待后续文档工程阶段验证。

|事项|实际证据|分类及处理|
|---|---|---|
|外封面|P1：封面封底黄色150g皮纹纸，外封面背面无内容|EXPLICIT_REQUIREMENT；仅记录该模板明文|
|身份字段|P13、16—21：题目、姓名、学号、专业、年级班、导师、二级学院|TEMPLATE_STYLE；本课题实际值UNCONFIRMED|
|封面时间|P27“二〇二七年六月”|EXAMPLE_ONLY；不据此确定毕业日期|
|声明授权|P30—47原创声明、版权授权、签字日期；P47背面无内容|模板组成TEMPLATE_STYLE；背面留空为EXPLICIT_REQUIREMENT|
|中文/英文摘要|P48—61存在摘要、Abstract、关键词/Keywords；示例搜索引擎文本|TEMPLATE_STYLE；内容EXAMPLE_ONLY；未见摘要字数、必须5关键词等明文要求，均UNCONFIRMED|
|目录|P63—106，toc 1/2/3，点引导页码|TEMPLATE_STYLE；示例5章及示例标题EXAMPLE_ONLY，不能据此生成本论文大纲|
|章/节层级|Heading 1、节(论文)、小节(论文)；P178有2.1.1.2示例|TEMPLATE_STYLE；不能把示例章节数量当强制规则|
|正文默认|styles.xml Normal：宋体/Times New Roman，24半磅=12pt（小四），两端对齐，固定440 twips=22pt行距|TEMPLATE_STYLE，不是全篇无例外的明文规定|
|标题直接格式差异|Heading 1样式黑体18pt，但P111直接格式黑体16pt；节样式15pt而P113直接14pt；小节样式14pt而P164直接12pt|TEMPLATE_STYLE有覆盖冲突；后续须采用经学校/导师确认的有效格式，不能只抄样式表|
|摘要/标题行距|P48、49、52、56、61、111、113、164直接行距1.5倍|TEMPLATE_STYLE；与Normal固定22pt区分|
|纸张/页边距|10节：A4约21×29.7cm，上/左/右2cm，下约1.5cm，装订线1cm；页眉约1.5cm、页脚约1cm|TEMPLATE_STYLE；读到的底部微差系twips舍入，不另造规则|
|图表|P141：图表分别按章编号“图章号-顺序号/表章号-顺序号”；图与图名不跨页；续页表注明“续表”；表左右边框隐去；引用图表标引|EXPLICIT_REQUIREMENT|
|图表字号/三线表|P141：图表文字含标题建议5号；表头加粗；按导师习惯也可三线表|建议性EXPLICIT_REQUIREMENT，不能升级为唯一强制三线表；P142—147为EXAMPLE_ONLY|
|量/单位/公式|P149量符号斜体、单位正体；P150公式居中、按章编号、末不加标点；P153正文不大段空白（章末除外）|EXPLICIT_REQUIREMENT；标准编号按模板原文登记，不声称已核验现行版本|
|参考文献|P290—311列[J]/[M]/[D]/[C]/[S]/[N]/[R]/[EB/OL]格式及示例|格式TEMPLATE_STYLE；计算机示例EXAMPLE_ONLY；未见必须条数、近五年比例、外文比例或明确GB/T 7714版本，均UNCONFIRMED|
|结论、附录、致谢|P281、312、320、322及目录对应条目|TEMPLATE_STYLE；两附录是EXAMPLE_ONLY，不是必须两份|
|页码/页眉|sectPr前2节upperRoman start=1；第3节start=1；后节有继承；footer存在PAGE域，header有学校名称|TEMPLATE_STYLE；字段缓存数字不是当前准确分页，实际分节页码位置/连续性须渲染复核|

## 5. Excel完整结构与口径

文件：`研究数据S1.xlsx`。读取公式与data_only缓存两份；无Excel错误类型单元格、无批注、外链0，设置fullCalcOnLoad=True。openpyxl不提供Excel公式计算引擎。本次对全部公式的存储和缓存进行读取，核验原有汇总的算术；没有在Excel/LibreOffice引擎中触发重算。

各表声明占用区域包含格式空行，不以max_row当样本量。表头有1行与4行两种位置：01—09表头第1行，10—12表头第4行；首页/研究设定是说明布局。

|工作表|读取范围（含格式空白）|实际业务记录/说明|公式数（全为双等号）|
|---|---|---|---:|
|首页|A1:H24|19个非空行，说明布局|6|
|研究设定|A1:F22|18个非空行，说明布局|0|
|01_实验单位|A1:L55|54条|0|
|02_果实清单|A1:J200|189条|0|
|03_处理记录|A1:M55|54条|0|
|04_质量变化|A1:N200|135条|270|
|05_腐烂观察|A1:N784|783条|0|
|06_品质检测|A1:N244|243条|0|
|07_环境记录|A1:H31|30条|0|
|08_偏离记录|A1:H8|7条|0|
|09_品质单元汇总|A1:M28|27条|162|
|10_描述统计|A1:H23|15组×时间汇总行，另有说明|90|
|11_品质汇总|A1:H16|9组×取样日汇总行|54|
|12_字段字典|A1:F39|35条字段/口径解释|0|

### 5.1 全字段与空值登记

以下空值分母为实际记录行；notes、photo、说明栏等可选空白不自动判错。计算列的空字符串/缓存空白与原始缺测分别判断。

- **01_实验单位**：batch_id；unit_id；group_id；cohort；fruit_count_initial；container_id；treatment_batch_id；allocated_at；rack_position；fruit_source；initial_check；notes。
  空白字段计数：notes=54。

- **02_果实清单**：batch_id；unit_id；fruit_id；group_id；cohort；arrival_mass_g；size_grade；maturity_grade；screening_result；notes。
  空白字段计数：notes=189。

- **03_处理记录**：treatment_id；unit_id；batch_id；group_id；treated_at；SA_conc_w_w_pct；CaCl2_conc_w_w_pct；first_dip_min；second_dip_min；air_dry_min；operator_id；protocol_version；notes。
  空白字段计数：notes=52。

- **04_质量变化**：record_id；measured_at；elapsed_days；batch_id；unit_id；group_id；fruit_count；baseline_mass_g；observed_mass_g；mass_loss_pct；record_status；photo_ref；notes；mass_loss_sq。
  空白字段计数：observed_mass_g=1；notes=134。

- **05_腐烂观察**：event_id；observed_at；elapsed_days；batch_id；unit_id；fruit_id；group_id；cohort；visible_decay_1_0；first_decay_1_0；removed_1_0；record_status；photo_ref；notes。
  空白字段计数：notes=732。

- **06_品质检测**：measurement_id；measured_at；elapsed_days；batch_id；unit_id；fruit_id；group_id；trait；raw_value；unit；instrument_id；technical_repeat_no；record_status；notes。
  空白字段计数：raw_value=6；notes=237。

- **07_环境记录**：record_id；recorded_at；batch_id；temperature_C；relative_humidity_pct；sensor_id；exception_1_0；notes。
  空白字段计数：notes=29。

- **08_偏离记录**：deviation_id；recorded_at；related_unit_id；related_fruit_id；event_type；description；handling_decision；reviewer_code。
  空白字段计数：related_fruit_id=5。

- **09_品质单元汇总**：unit_id；batch_id；group_id；cohort；elapsed_days；fruit_count_initial；valid_firmness_fruits；unit_firmness_mean_N；valid_TSS_fruits；unit_TSS_mean_Brix；notes；firmness_sq；TSS_sq。
  空白字段计数：notes=25。

- **10_描述统计**：group_id；elapsed_days；valid_mass_units；mean_mass_loss_pct；sd_mass_loss_pct；decayed_fruit_n；observed_fruit_n；visible_decay_pct。
  空白字段计数：elapsed_days=1；valid_mass_units=1；mean_mass_loss_pct=1；sd_mass_loss_pct=1；decayed_fruit_n=1；observed_fruit_n=1；visible_decay_pct=1。

- **11_品质汇总**：group_id；elapsed_days；firmness_valid_units；firmness_mean_N；firmness_sd_N；TSS_valid_units；TSS_mean_Brix；TSS_sd_Brix。
  空白字段计数：elapsed_days=1；firmness_valid_units=1；firmness_mean_N=1；firmness_sd_N=1；TSS_valid_units=1；TSS_mean_Brix=1；TSS_sd_Brix=1。

- **12_字段字典**：表；字段；单位或取值；解释；补充解释；研究补充。
  空白字段计数：研究补充=4。


### 5.2 实验结构（工作簿记载，未外部确证）

- 日期：2026-10-05—10-25；B1起10/05、B2起10/13、B3起10/21。观察相对日期Day0—4，日期偏移检查通过，不存在相对审核日期的未来实验记录。
- 处理编码CK（水→水）、Ca（水→CaCl₂）、SA-Ca（SA→CaCl₂）。研究设定B11/B12标1.5% SA与1% CaCl₂（w/w）；处理表54行编码与浓度匹配检查无不符；实际执行仍须结合原始SOP确认。浸渍记录1.8—2.3min、风干18—30min，不得将“约2min”写成严格统一2min。
- 54个候选处理单位：3批次×3组×6单位；每个批次×组有3个L、D0/D2/D4各1个。27个L单位，每单位4果；27个D单位，每单位3果。
- 189颗果实：L108，D0/D2/D4各27。处理前单果到货质量不等于处理后L单位失重基线，不能混用。
- 连续质量135行=27×5，1个缺测，134个实际质量读数；Day0基线与后续质量单位g，失重率%、平方%²。单位质量是同容器多果总质量，不是单果重复。
- 腐烂783事件：L540=108×5；D0为27、D2为81、D4为135，各D队列仅观察到破坏性取样日。主腐烂时间比较限定L；不能把随时间退出的D队列混入分母。
- 品质243计划读数=81颗D果×（硬度2次+TSS1次）；6个读数缺失，237个有效值。硬度N、TSS °Brix（可溶性固形物，不是总糖）。79颗具有有效硬度与TSS的D果；技术读数不得替代果数或单位数。
- 环境30行=3批次×5天×每日09/17时，22.2—25.2℃、62.8—79.5%RH；应报告实测波动，不写成精确恒温24℃。记录位置不等于容器内微环境。

## 6. 数据质量检查结果与异常定位

### 6.1 已完成检查

01—09按对应unit_id/fruit_id/treatment_id/record_id/event_id/measurement_id/deviation_id检查主键，未发现重复；质量unit×day、腐烂fruit×day、品质fruit×trait×technical_repeat_no复合键均无重复。01—06及09的unit、fruit、batch、group、cohort关联检查没有发现错配；每单位果数与01表fruit_count_initial一致。偏离表的B3-ALL另作批次事件，见下。

质量/腐烂/品质的日期与allocated_at日差逐条一致；L完整5日、D观察窗与取样日结构一致。腐烂0/1、首次事件及持续腐烂逻辑检查未见反转；不能据此证明观察者判读一致。质量现存读数随时间未见增加；硬度/TSS非缺失读数均正，范围分别2.15—12.69N、6.58—9.77°Brix。全量混合时点IQR初筛未标记极端硬度/TSS值，但此筛查不验证仪器精度，也可能掩盖分层异常；本轮不以统计阈值删除任何读数。腐烂全部0/1取值有效、removed全部0；逐果D队列观察窗及品质检测日与D0/D2/D4匹配检查无异常。

逐单位现有失重率的相邻日变化初筛：最小0.44个百分点/日位于B1-CK-L2的Day2→3，最大2.69位于B2-SA-Ca-L3的Day2→3；前者08第2行登记速度较低，后者08第3行登记涂层不均。其原始读数定位04 E/J列该unit相应日，计算为相邻J差除以C日差。这些是变化极值与备注对应线索，不是异常阈值或因果解释；未观察到质量反增，剩余幅度差异是否属真实生物差异仍需原日志、照片及方法核实。

### 6.2 问题、风险与最小整改

|编号/级别|可定位证据|判定与影响|最小补充/修复要求（本轮不改原件）|
|---|---|---|---|
|DQ01 高|首页B9:B14、04 J2:J136/N2:N136、09 G:J/L:M第2—28行、10 C:H第5—19行、11 C:H第5—13行，共582公式|openpyxl均读为`==...`，OOXML f节点文本含多余前导`=`。缓存存在并可复算不等于公式规范可执行；fullCalcOnLoad=True使后续重算风险尤其重要|保留原件；后续经授权另建派生工作副本，规范公式并在真实引擎全量重算，对照本次审计算法；本轮引擎重算未验证，不宣称实际弹出了#NAME?|
|DQ02 高|03 L2:L55 protocol_version：DEMO-01共38、DEMO-02共16；K列OP-01；XLSX core creator=openpyxl，created/modified均2026-11-10 15:27:11（元数据未带可确证时区）|提示整理/示例命名来源待解释，不是造假证据；内部一致无法认证真实实验|说明文件形成过程、DEMO含义及版本差异；提供至少原始称重/检测导出、纸质实验日志及整理链|
|DQ03 高|04 L2:L136、05 M2:M784含IMG-*引用；仓库仅两张文献截图|216个不同IMG引用未形成可访问原图闭环，无法复核涂层、腐烂及称量状态|提供带unit/fruit/date映射的原始图像清单及文件；若未拍摄须明确说明而非补造|
|DQ04 高|01 I2:I55：每批18单位仅12不同rack_position；如I2=I14=B1-R08，I3=I15=B1-R03|架位是共享大区域还是同一位置冲突未定义；CK/SA-Ca的重复位置具有系统配对模式，随机分配与位置混杂未确认|架位图、随机化/轮换记录、容器间距与通风、共液复用情况；编号PREP唯一不替代独立配液证据|
|DQ05 中|04 I114空白，unit B3-Ca-L2、Day2；K114漏测-未补值；08第6行DV-005|1/135=0.74%计划质量记录缺测，有事件说明；10 Ca Day2有效单位应8，其余点9|保留空白、核对原日志；后续模型注明缺测与排除口径，不插补成0|
|DQ06 高|06 I107:I109（B2-CK-D4-F03）、I239:I241（B3-SA-Ca-D4-F02）；08第7—8行DV-006/007|6/243=2.47%计划读数缺失，2/81=2.47%D果无法检测；腐坏/过软相关，为潜在信息性缺失。已算均值只代表可检测果|核对日志与相应腐烂记录，预定缺失敏感性方案；不得无条件称为全体果平均品质|
|DQ07 中|08 B2为10/05 12:00，F2却称“前期失重速度较低”；DV-003 10/07说明首日沥液差异；DV-005时间10:00而质量常规测量10:05|至少DV-001首次称重当天就评价前期速度，需解释系追记/录入时间或其他预观察；并非证明不可能|提供事件发生、发现、录入三个时间及原记录；不能默认为预注册决策|
|DQ08 中|08 C5=B3-ALL，非01单位ID；D列多数空|批次环境事件标识不是单位外键，机械内连接会丢失这一事件|声明批次范围事件规则，关联B3全部单位；空fruit_id对于单位/批次事件可合理|
|DQ09 中|09 H2:H28直接对所有“有效”硬度读数取均值；G列只计repeat_no=1|当前每有效果恰有2硬度重复，直接平均与先果均值再单位均值恰好相等；将来不平衡会权重偏置，repeat1计数不普适|派生分析明确先技术→果→单位；有效果计数用unique fruit_id；保留原始重复读数|
|DQ10 高|03仅TEXTURE/REFRACT等见06 K列设备代码，protocol_version无附加SOP；01 J仅笼统同批筛选果|缺品种、产地/采购凭证、收获成熟标准、SA规格与黏度/分子量、CaCl₂水合/纯度、配液和共液规则、成膜验证、硬度探头速度深度去皮/位置、折光校准温补、天平精度、腐烂判据与盲法等|补最小SOP与仪器型号校准记录；不要从参考论文替补为“本实验已执行”|
|DQ11 中|10 F:H为L总体腐烂果数比例，未给每单位二项结果；表述初始果数与可观察果数并存|当前无移除、L观测齐全，分母每组每时点36，口径现时相等；未来缺失/移除会分歧|后续明确固定初始分母或风险集规则并以unit保留聚类结构；总体百分比不证明独立n=36|
|DQ12 低/待核|硬度79有效果中4对两次读数完全相同|记录精度下可发生，不是重复记录；主键不同，不据此认定复制|保留，结合分辨率及仪器原始导出核对|

### 6.3 独立复算范围与结果

对04全部135行J/N，09全部27单位G/H/I/J/L/M，10全部15汇总行C:H，11全部9汇总行C:H合计576个缓存单元格进行独立算术核验，另复核首页6个规模缓存，**未发现缓存数值差异**。空读数对应派生空白而非0。首页规模缓存54/189/135/783/243/30与实际记录一致。

复算规则：失重率=ROUND_HALF_UP[100×(baseline-observed)/baseline,2]，平方用已舍入失重率；品质先每果技术均值再每单位果均值；组汇总等权按单位求均值和样本标准差（ddof=1）；腐烂仅L队列按组×日计数/观察果数。均值/标准差仅用于核验既存汇总，不在报告输出正式处理差异结果。比较容差1e-7，缺失要求缓存空白。当前重复平衡使两级平均与Excel直接平均等价；未将此等价外推到不平衡数据。

算术核验通过不消除DQ01公式存储错误，也不认证原始读数来源。没有独立实验员签字、仪器文件或原图证据，不能从“数字能算平”推断记录真实。

## 7. 实验独立性与样本层级

|层级|工作簿数量|分析意义与限制|
|---|---:|---|
|来源/日期批次|3（B1/B2/B3）|共同采购/操作/环境区组，不能把来源批次与处理批次混同；泛化批次只有3，不能任意声称充分统计功效|
|候选处理单位|54容器/操作ID|物理独立与共液复用未证实，必须以实际随机化和操作层级决定独立n|
|L单位|27，每组9，每批每组3|同单位4果、5天相关；每组9是候选容器数，非独立性认证|
|D单位|27，每组×日3（来自3批）|每批每组×取样日只有1单位，不能估计该格内单位变异；每单位3果是嵌套子样|
|果实|189，L108/D81|不是189独立处理重复；L腐烂可保留果事件但须处理容器聚类|
|时间重复|L Day0—4|同一单位/果纵向，135质量行及540 L果日不等于独立n|
|硬度技术重复|2次/每D果|先折叠技术重复；不能把162计划硬度读数当独立n|
|TSS|1次/每D果|无技术重复精度估计，仍为容器内果实子样|

没有SA单独处理臂，不能分离完整SA×Ca交互；SA-Ca对Ca可讨论“给定钙条件下SA流程增量”，SA-Ca对CK代表整套复合工艺，不能称“SA单因素纯效应”。容器若共享同一次配液且真正处理施加在共液批次，实验单位可能应上移，必须补证后再定模型。后续可讨论分层/区组、重复测量/二项聚类模型，但本轮不拟合、不做功效保证。

## 8. 来源核验及证据链

用户明确将S1作为实验研究资料提交，此为来源声明。仓库快照及SHA证明“本次读取的是哪些文件且未被本轮更改”，不证明采样和读数的实验真实性。03的DEMO标记、OP-01、08的审核签名“王馨”仅为文件内容：不据此确认作者姓名或实验人员身份。创建软件为openpyxl仅说明整理工具，不说明生成数字的机制。

已形成内部链：unit→fruit→处理/质量/腐烂/品质→单位品质→组汇总；环境按batch关联，偏离按unit/fruit或B3批次范围关联。外部链缺采购/样本来源、原始实验记录、设备导出/校准、照片原件与映射、SOP版本、整理修改履历及责任人确认。因此来源结论为**UNVERIFIED（部分内部可追溯，外部真实性尚未确证）**，既不宣布真实，也不无证据宣布模拟或伪造。

## 9. 分析适用性与实验充分性

SUPPORTED=现有文件在限定范围直接支持；PARTIALLY_SUPPORTED=内部具备部分结构但有明确条件；UNVERIFIED=关键外部证据未证实；NOT_SUPPORTED=当前设计不支持相应推断。

|问题|状态|可支持范围/限制|
|---|---|---|
|A 处理组品质差异|PARTIALLY_SUPPORTED|有3组及单位层读数；来源与实际独立性待核，小样本且无SA单独臂；不作显著性判断|
|B 贮藏时间变化|PARTIALLY_SUPPORTED|L具Day0—4连续结构；品质为D0/2/4不同容器截面，不能当同果纵向|
|C 失重率复现计算|SUPPORTED|限定“给定现有读数按定义复算缓存”已通过；实际基线统一性/仪器证据待核，Excel重算可靠性不在此通过范围|
|D 腐烂指标比较|PARTIALLY_SUPPORTED|L完整观察、固定36果/组/日，事件链一致；单位聚类、判据/照片及盲法待确认|
|E 硬度/TSS可分析性|PARTIALLY_SUPPORTED|已读数且可折叠技术重复；每组每时点仅3候选单位，腐坏相关缺失及方法不足，不能承诺模型有效|
|F 批次/单位关联|PARTIALLY_SUPPORTED|内部键一致，B3-ALL须单独范围关联；物理独立及共享处理液未核实|
|G 独立重复支持拟分析|UNVERIFIED|候选n已厘清，尚无已授权正式分析方案和物理独立证据，不先承诺ANOVA或充分功效|
|H 方法可复现|NOT_SUPPORTED|DQ10所列关键SOP缺失，现文件不足以独立复现实验|
|I 支撑主要问题|PARTIALLY_SUPPORTED|能为限定复合处理、短期常温质量变化提供结构性输入；尚不足以放行正式推断或SA单独效应结论|

## 10. 尚需补充的最少必要资料

1. 实验负责人对S1来源、真实/整理/演示性质及DEMO-01/02含义的书面说明；至少提供对应实际读数的纸质/电子原日志、仪器原始导出或称重原始记录，说明整理时间与修改链。不要求在聊天公开个人隐私。
2. 处理单位的实际独立施加方式、配液与复用批次、容器及架位图、随机分配/位置轮换记录；解释重复rack_position。明确unit与treatment_batch_id到底代表什么物理实体。
3. 最小方法SOP：果实品种/来源、成熟筛选、SA/CaCl₂材料与配制、处理顺序/共液/干燥与Day0基准、贮藏条件、称重/硬度/TSS的仪器型号精度校准及关键设置、腐烂判定标准。
4. IMG引用原图及unit/fruit/date对应清单，或明确原图不存在的原因；解释DV-001等事件时间与追记方式，确认缺失记录和保留决策。
5. 经单独授权的派生副本修复/重算计划及真实表格引擎验证；保留本原件SHA，不在本轮纠正582个公式。

文献精读前另需补mh611与S1摘要对应全文、核对草莓涂膜论文缺页、扫描论文OCR、梁综述版本及学校现行书面格式说明。这些不全部构成数据建模前置条件，但构成后续可靠引用/排版前置条件。

## 11. 下一阶段建议（未执行）

先交外部审核者复核本报告，按整改意见补证；仍在Phase 01内关闭来源、独立性、方法和公式可靠性问题。只有外部验收通过且用户明确授权后，才制定正式统计方案（定义实验单位、批次/时间结构、缺失和敏感性处理以及推断边界），随后开展正式统计研究。本轮没有自动进入Phase 02，也没有生成论文大纲。

## 12. 质量验收与自检

|门槛|机器初审结果|说明|
|---|---|---|
|GATE-01 全部原件清点|PASS|36文件、路径/大小/SHA/格式/用途/可读/重复/缺损均登记|
|GATE-02 Excel实际读取|PASS|14表全部读取，公式与缓存双读；582公式问题已登记|
|GATE-03 重要异常有定位|PASS|DQ01—12有单元格/文件位置、风险、补证要求；未以空泛推测判造假|
|GATE-04 独立重复核查|CONDITIONAL PASS|文件层级厘清，但物理独立性及随机化尚需原证据|
|GATE-05 来源追溯评估|CONDITIONAL PASS|已明确内部链与外部缺口，不能认定实验来源已认证|
|GATE-06 学校规则提取|PASS|文字要求、样式、示例及未确认项分开；未渲染分页|
|GATE-07 文献初点|CONDITIONAL PASS|31PDF全部初点；摘要/缺页/扫描限制及未核DOI版本明确|
|GATE-08 原件未改|PASS|所有36原件前后SHA一致；仅三个授权文件新增|

**总体：CONDITIONAL PASS（仅资料建档与初审交付）；正式统计科研准入：暂不放行。** 这不是外部人工验收结果。必须先关闭DQ01—04及DQ10所涉关键证据缺口，并确认DQ05—09处理口径。文件生成或Codex自检通过不能替代人工审核。

原件完整性复查：36份原件SHA逐一与审计开始基线一致，DOCX/XLSX ZIP全部成员CRC检查通过；递归文件集合新增项仅三个授权交付物。01—07工作表均可见。

自检检查范围：三个文件名称与授权一致；没有正式假设检验/显著性结论/结果图表/论文大纲/模拟替代数据；原件未覆盖、删除、改名；分支单独提交。Git推送与最终Commit SHA以最终交付消息记录，避免在提交内循环写入自身SHA。

## 附录A｜可复核检查代码

以下为本轮实跑的核心Python检查（依赖openpyxl标准读取；仅输出到/tmp，不写原件）。保留代码在本报告内，以遵守仅三个交付文件的约束。PDF/模板抽取依据见各节，原件SHA见第2节。重跑时先创建/tmp/phase01；工作簿路径须指向本报告记录的同SHA文件。

```python
from pathlib import Path
from openpyxl import load_workbook
from collections import Counter,defaultdict
from statistics import mean,stdev
from decimal import Decimal,ROUND_HALF_UP
import json,zipfile,re
Path('/tmp/phase01').mkdir(exist_ok=True)
R=Path('/workspace/strawberry-alginate-thesis');w=load_workbook(R/'研究数据S1.xlsx');v=load_workbook(R/'研究数据S1.xlsx',data_only=True)
S={};schema=[]
for s in w:
 start=1 if s.title[:2].isdigit() and not s.title.startswith(('10','11','12')) else 4
 heads=[c.value for c in s[start]]
 records=[dict(zip(heads,row))|{'_row':i} for i,row in enumerate(s.iter_rows(min_row=start+1,values_only=True),start+1) if row[0] is not None]
 S[s.title]=records
 fs=[c.coordinate for row in s for c in row if c.data_type=='f'];bad=[c.coordinate for row in s for c in row if c.data_type=='f' and c.value.startswith('==')]
 schema.append({'sheet':s.title,'dimension':s.calculate_dimension(),'records':len(records),'heads':heads,'formulas':len(fs),'double_equals':len(bad),'missing':{str(h):sum(r.get(h) is None for r in records) for h in heads if h}})
json.dump(schema,open('/tmp/phase01/schema.json','w'),ensure_ascii=False,indent=2)
U={r['unit_id']:r for r in S['01_实验单位']};F={r['fruit_id']:r for r in S['02_果实清单']};M=S['04_质量变化'];D=S['05_腐烂观察'];Q=S['06_品质检测'];results=[]
def add(check,items):results.append((check,len(items),items[:15]))
for sn,rs in S.items():
 if sn[:2].isdigit() and int(sn[:2])<10:
  hs=schema[w.sheetnames.index(sn)]['heads']; key={'01_实验单位':['unit_id'],'02_果实清单':['fruit_id'],'03_处理记录':['treatment_id'],'04_质量变化':['record_id'],'05_腐烂观察':['event_id'],'06_品质检测':['measurement_id'],'07_环境记录':['record_id'],'08_偏离记录':['deviation_id'],'09_品质单元汇总':['unit_id']}[sn]
  ct=Counter(tuple(r[k] for k in key) for r in rs);add(sn+' duplicate key',[k for k,n in ct.items() if n>1])
  if sn not in ['07_环境记录','08_偏离记录']:
   errs=[]
   for r in rs:
    u=U.get(r.get('unit_id'))
    if u is None:errs.append((r['_row'],'orphan unit'));continue
    for k in ['batch_id','group_id','cohort']:
     if k in r and r[k]!=u[k]:errs.append((r['_row'],k,r[k],u[k]))
    if 'fruit_id' in r and (r['fruit_id'] not in F or F[r['fruit_id']]['unit_id']!=r['unit_id']):errs.append((r['_row'],'fruit join'))
   add(sn+' joins',errs)
for rs,key,label in [(M,['unit_id','elapsed_days'],'mass unit-day'),(D,['fruit_id','elapsed_days'],'decay fruit-day'),(Q,['fruit_id','trait','technical_repeat_no'],'quality technical key')]:
 c=Counter(tuple(r[k] for k in key) for r in rs);add(label+' duplicates',[k for k,n in c.items() if n>1])
add('unit counts',[u for u,r in U.items() if sum(f['unit_id']==u for f in F.values())!=r['fruit_count_initial']])
errs=[]
for rs,dt in [(M,'measured_at'),(D,'observed_at'),(Q,'measured_at')]:
 for r in rs:
  if (r[dt].date()-U[r['unit_id']]['allocated_at'].date()).days!=r['elapsed_days']:errs.append(r['_row'])
add('date offset',errs)
add('missing mass',[(r['_row'],r['unit_id'],r['elapsed_days'],r['record_status'],r['notes']) for r in M if r['observed_mass_g'] is None])
add('missing quality',[(r['_row'],r['fruit_id'],r['trait'],r['technical_repeat_no'],r['notes']) for r in Q if r['raw_value'] is None])
# independent arithmetic checks; never evaluate malformed Excel formula strings
mcalc={};comp=[]
def compare(sn,row,col,expected):
 actual=v[sn].cell(row,col).value
 if expected is None: good=actual in [None,'']
 else:good=isinstance(actual,(int,float)) and abs(actual-expected)<1e-7
 if not good:comp.append((sn,row,col,actual,expected))
for r in M:
 val=None if r['observed_mass_g'] is None else float((Decimal(str(r['baseline_mass_g']))-Decimal(str(r['observed_mass_g'])))/Decimal(str(r['baseline_mass_g']))*100)
 val=None if val is None else float(Decimal(str(val)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP))
 mcalc[r['record_id']]=val;compare('04_质量变化',r['_row'],10,val);compare('04_质量变化',r['_row'],14,None if val is None else val*val)
qc={}
for r in S['09_品质单元汇总']:
 qs=[q for q in Q if q['unit_id']==r['unit_id'] and q['record_status']=='有效' and q['raw_value'] is not None]
 fm=defaultdict(list)
 for q in qs:fm[(q['trait'],q['fruit_id'])].append(q['raw_value'])
 for trait,cols in [('firmness',(7,8,12)),('TSS',(9,10,13))]:
  vs=[mean(a) for (t,f),a in fm.items() if t==trait]; val=mean(vs) if vs else None;qc[(r['unit_id'],trait)]=val
  for col,e in zip(cols,[len(vs),val,None if val is None else val*val]):compare('09_品质单元汇总',r['_row'],col,e)
for r in S['10_描述统计']:
 if not isinstance(r.get('elapsed_days'),int):continue
 g,t=r['group_id'],r['elapsed_days']; ms=[mcalc[x['record_id']] for x in M if x['group_id']==g and x['elapsed_days']==t and mcalc[x['record_id']] is not None];ds=[x for x in D if x['group_id']==g and x['elapsed_days']==t and x['cohort']=='L']
 for col,e in enumerate([len(ms),mean(ms),stdev(ms),sum(x['visible_decay_1_0'] for x in ds),len(ds),100*sum(x['visible_decay_1_0'] for x in ds)/len(ds)],3):compare('10_描述统计',r['_row'],col,e)
for r in S['11_品质汇总']:
 if not isinstance(r.get('elapsed_days'),int):continue
 for trait,cols in [('firmness',(3,4,5)),('TSS',(6,7,8))]:
  vals=[qc[u,trait] for u,un in U.items() if un['group_id']==r['group_id'] and un['cohort']=='D'+str(r['elapsed_days']) and qc.get((u,trait)) is not None]
  for col,e in zip(cols,[len(vals),mean(vals),stdev(vals)]):compare('11_品质汇总',r['_row'],col,e)
add('cached arithmetic mismatch',comp)
errs=[]
for f in F:
 ds=sorted([r for r in D if r['fruit_id']==f],key=lambda r:r['elapsed_days']); seen=0
 for r in ds:
  if r['visible_decay_1_0']<seen or r['first_decay_1_0']!=int(r['visible_decay_1_0']==1 and seen==0):errs.append((r['_row'],f))
  seen=max(seen,r['visible_decay_1_0'])
add('decay monotonic/first',errs)
for k,rs,field in [('mass',M,'observed_mass_g'),('quality',Q,'raw_value')]:
 add(k+' nonpositive',[(r['_row'],r[field]) for r in rs if r[field] is not None and r[field]<=0])
for unit in U:
 ms=sorted([r for r in M if r['unit_id']==unit and r['observed_mass_g'] is not None],key=lambda r:r['elapsed_days'])
 for a,b in zip(ms,ms[1:]):
  if b['observed_mass_g']>a['observed_mass_g']:print('mass increase',unit,a['_row'],b['_row'])
for x in results:print(x)
print('FORMULA XML', zipfile.ZipFile(R/'研究数据S1.xlsx').read('xl/worksheets/sheet5.xml').decode()[0:450])
print('META',w.properties)
print('RANGE QUALITY',[(t,min(r['raw_value'] for r in Q if r['trait']==t and r['raw_value'] is not None),max(r['raw_value'] for r in Q if r['trait']==t and r['raw_value'] is not None)) for t in ['firmness','TSS']])
print('ENV',[(f,min(r[f] for r in S['07_环境记录']),max(r[f] for r in S['07_环境记录'])) for f in ['temperature_C','relative_humidity_pct']])
print('PROTOCOL',Counter(r['protocol_version'] for r in S['03_处理记录']))
json.dump(results,open('/tmp/phase01/checks.json','w'),ensure_ascii=False,default=str,indent=2)

```
