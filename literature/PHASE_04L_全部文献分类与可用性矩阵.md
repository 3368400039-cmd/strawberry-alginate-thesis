# Phase 04L｜全部文献分类与可用性矩阵

正式题目：《可食性海藻酸钠膜对草莓常温保鲜效果的研究》

学校：四川工业科技学院｜日期：2026-11-11（UTC+8）

基准：`thesis/phase04-chapter01-draft`，`62f658aa6d2bc4837f9cbdc03a5a9d000d1202fb`。本轮为Phase 04L文献研究资料包；自检不代替外部人工审核，不执行Phase 04R或正文扩写。

## 证据与计数口径

- LE01—LE28是本轮文献档案ID，不是正式论文顺序编码。首次引用顺序须在后续获授权的正文修订中统一；不修改当前第一章[1]—[4]。
- 物理页码p1从PDF第一页起算，含封面/摘要/空白页；仅明确标出的“印刷页”才是刊物或论文内页码。浓度保留原有w/w、w/v、wt%、g/L等基准，未确认的%不补单位。
- SOURCE_TEXT：原文明确记载的条件、定义或理论表述；引言转述的理论不自动成为该文原始实验发现。SOURCE_RESULT：实际结果文字或已查看图表支持的发现。AUTHOR_INTERPRETATION：原作者解释。RESEARCHER_INFERENCE：本轮比较判断。UNVERIFIED：未充分核实。
- PRIMARY_RESULT_VERIFIED只表示卡中指定结果点已核到原文，不表示全篇无误、统计独立性/研究真实性/食品安全已认证。ABSTRACT_ONLY不进入正文详细结果证据；METHOD_VERIFIED_LIMITED限方法；VERSION_UNCONFIRMED须先解决版本；EXCLUDED_WITH_REASON不得纳入本题核心引用。
- 相关性A/B/C/D与可靠程度分开：A不等于可直接引用，D不等于造假。APPARENTLY_COMPLETE仅指当前文件可打开、页面/章节表面连续；不代替与出版社全文逐页校勘。未使用出版年份推断未记载的实验日期。
- 本轮没有系统检索外部数据库、PRISMA流程、Meta-analysis或统计合并；仅梳理已上传资料。PDF印刷DOI可在本地核读，但未联网完成解析、撤稿检查或最终版本确认，不称“官方题录已全部核验”。

## 1. 全库结果

实际31个PDF路径，SHA-256字节去重后28个不同PDF，3组各2份完全重复。28条CSV主记录对应不同PDF；LE21/LE22另合为V01疑似同源内容家族，按内容最多约27个家族（其中V01版本关系尚待出版信息闭环），不能称“28项独立实验”。所有原件保留、不改名、不删除。

按不同PDF计：中文20，英文正文/英文摘要摘件6，泰文正文1，印度尼西亚文/英文摘要摘件1。中文论文中的英文摘要不另算一篇英文研究。31路径口径为中文20、英文8、泰文2、印尼/英文摘件1；英文与泰文增加来自完全重复文件。

按资料形态计：期刊原始研究18（含环境工程等排除项）、硕博士学位论文6、仅摘要/题录摘件2、综述版本2。扫描件LE20包含在6篇学位论文中；语言、形态和完整性是交叉属性，不相加。31份均能打开；LE20的71页无文本层，不能误判为损坏；LE28疑缺续页，仍保留已可核的局部结果。

|相关性|不同PDF数|用途|
|---|---|---|
|A|14|草莓/海藻酸盐核心；其中摘要/语言限制仍保留|
|B|8|材料性质、其他草莓处理、方法或综述线索|
|C|3|其他果实定向辅助|
|D|3|化学物质或应用对象不适用|

|核验状态|记录数|
|---|---|
|ABSTRACT_ONLY|5|
|EXCLUDED_WITH_REASON|3|
|METHOD_VERIFIED_LIMITED|1|
|PRIMARY_RESULT_VERIFIED|17|
|VERSION_UNCONFIRMED|2|

## 2. 全部31份原始PDF文件清单

路径相对仓库根目录，大小为字节；同一ID重复路径有完全相同SHA及可读状态。完整阅读范围见§5，能抽取文字不等于读完。

|ID|实际路径/原始文件名|字节|PDF页数|SHA-256|可读取状态|重复情况|
|---|---|---|---|---|---|---|
|LE01|4EA7E7811F4D44AB8B3892557FC72A52.pdf|448358|6|525d5c9c5395ae73c9041326b9c7f460e1b673d22f2a9af1ec0bb61fb6971354|可打开；有文本层；未逐页人工通读|规范主记录|
|LE02|Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf|561957|11|7a795bdae972cb1c90d740c657642ab8d6e6d71312a405a24c36f7b1baa064bb|可打开；有文本层；未逐页人工通读|规范主记录|
|LE02|Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf|561957|11|7a795bdae972cb1c90d740c657642ab8d6e6d71312a405a24c36f7b1baa064bb|可打开；有文本层；未逐页人工通读|字节完全重复，保留原件|
|LE03|Greta_Peretto_PhD_dissertation.pdf|1586149|202|a056765038865fdb6c5bfaa2f69cc83e8ca7f4f0cbee996bf198e67c163ef151|可打开；有文本层；未逐页人工通读|规范主记录|
|LE04|Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf|861790|6|d9fbb2814e9a053f20f66993548aec97ca6ec24d38820a49fc3aaa4273c7d8e0|可打开；有文本层；未逐页人工通读|规范主记录|
|LE05|S1-2018-333159-abstract.pdf|287363|2|002b73d5a7840f349d5977b2076af85acbb7aaeaeefbffb70b8c793d2b3ebd94|可打开；有文本层；未逐页人工通读|规范主记录|
|LE06|coatings-14-01331 2.pdf|3272094|15|0daef1792527746bb83ddc35429acb73fe612ddf47de9e8cbe05f879b92a81a4|可打开；有文本层；未逐页人工通读|规范主记录|
|LE07|eb0e68fb8f6c2a811368a62e444e782162e8.pdf|224783|7|d4f9e735c0b02f01bf568dd9ce8b06485d00fadfe9a9047a1d8664dc78606634|可打开；有文本层；未逐页人工通读|规范主记录|
|LE07|eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf|224783|7|d4f9e735c0b02f01bf568dd9ce8b06485d00fadfe9a9047a1d8664dc78606634|可打开；有文本层；未逐页人工通读|字节完全重复，保留原件|
|LE08|foods-08-00203-v2 2.pdf|2022786|21|ca6776176de675559ba75c9b8fa207704ce4a835ea710d6fff973b99ecd18f0f|可打开；有文本层；未逐页人工通读|规范主记录|
|LE09|jcs-04-00123.pdf|1592335|15|424d6ba731c6e2997fba900c8e77c7cc077de75fe7562a0580901122f541c534|可打开；有文本层；未逐页人工通读|规范主记录|
|LE09|jcs-04-00123 2.pdf|1592335|15|424d6ba731c6e2997fba900c8e77c7cc077de75fe7562a0580901122f541c534|可打开；有文本层；未逐页人工通读|字节完全重复，保留原件|
|LE10|mh611.pdf|79444|1|954c07da9bbb54aa4db3426b974de56b095e71f0a5f30e180da430a6f83708ae|可打开；有文本层；未逐页人工通读|规范主记录|
|LE11|中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf|1383975|7|4acf4c5f7f4f7308aa449d8158d396a7a5501658dc8646e25fe96335346ac940|可打开；有文本层；未逐页人工通读|规范主记录|
|LE12|基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf|5038343|86|71b6a326ae412bdd5721d35ca7e295081adea4111350da7f3750f950bb0f6f90|可打开；有文本层；未逐页人工通读|规范主记录|
|LE13|壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf|213342|7|819b79c2ebdeca081808a53db19acf6197da2be24fd730c2e107d600100cc90e|可打开；有文本层；未逐页人工通读|规范主记录|
|LE14|壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf|5617725|101|80dee03ecf1ed141a567f3e5463f9eca1de3473c022484878aed2bfc80ab257a|可打开；有文本层；未逐页人工通读|规范主记录|
|LE15|柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf|3527405|5|65f17f5af496699859c550b947a7014e8dbe316d88b2ba34336b215f82786271|可打开；有文本层；未逐页人工通读|规范主记录|
|LE16|油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf|7253062|104|e10b3b5f65d3815976c3d0764b5cd50f5ed27d1836f4bd91d225657703b11d17|可打开；有文本层；未逐页人工通读|规范主记录|
|LE17|海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf|1454285|4|9874a84f6002329e1dd2722a1f3ee22fc1e5a3cbeed8b22588ba93a55c4e30f8|可打开；有文本层；未逐页人工通读|规范主记录|
|LE18|海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf|5362932|73|5352e499fcc9b3b00c01260d7e694ceceef2094aa8207e3eefb5d5e68db660f2|可打开；有文本层；未逐页人工通读|规范主记录|
|LE19|海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf|2346157|9|07e8969a8dfbfb153ed2c30ed25f6d7562c0783833996274c313422b95907c24|可打开；有文本层；未逐页人工通读|规范主记录|
|LE20|海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf|6840001|71|b071ee75d131b94d86450166dbde8172cc587fde9e68866c8c950255d1f2d5c7|可打开；无文本层，定向目视|规范主记录|
|LE21|海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf|1641594|4|24981bf71632a7ec94e46fdd1fc74cec695829c4ee7092371b8b01a886aa9a9b|可打开；有文本层；未逐页人工通读|规范主记录|
|LE22|海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf|834241|5|7d9ffd1ad25f2020ef54dbe6653fd33b7ea58d82f818a64789607e0acdd577b1|可打开；有文本层；未逐页人工通读|规范主记录|
|LE23|海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf|1448754|14|92afac99ce254b88546a54480634217ad6ada7c4cf87763d0cc664fb55c0b38a|可打开；有文本层；未逐页人工通读|规范主记录|
|LE24|空气负离子环境中草莓采后品质的变化_范鹏.pdf|2400692|11|c735e005609562535f83bce4a1ab3cf638caffbeabb35c8f77e5daf288f6dce1|可打开；有文本层；未逐页人工通读|规范主记录|
|LE25|脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf|2948042|14|e62021d88ed63646a67802aa433678f55ce9bbcab99ac71968498ca1ebde40d3|可打开；有文本层；未逐页人工通读|规范主记录|
|LE26|茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf|1852904|7|0aba23c944ac72f509bcd19ef4d506c2d7f1c46c4ec4b132fff6da7d626901a8|可打开；有文本层；未逐页人工通读|规范主记录|
|LE27|茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf|990499|5|2c130df5506a3646ca24f441ba1d2f371b1016fec4325109741d64bb60d1c7a1|可打开；有文本层；未逐页人工通读|规范主记录|
|LE28|草莓的涂膜保鲜研究.pdf|205343|4|61c82c555105dcce92813d7b49fb027361bf8242dc34f03e33466757ae83855f|可打开；有文本层；未逐页人工通读|规范主记录|

## 3. 重复、版本与完整性处理

|组|原始路径|处理|
|---|---|---|
|LE02|Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf；Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf|只建一个主ID，不计两项证据，原件保留|
|LE07|eb0e68fb8f6c2a811368a62e444e782162e8.pdf；eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf|只建一个主ID，不计两项证据，原件保留|
|LE09|jcs-04-00123.pdf；jcs-04-00123 2.pdf|只建一个主ID，不计两项证据，原件保留|

**V01版本家族：LE21与LE22。** 两份均为梁昭榆等六人同主题综述。LE21 p1题名“在”、正文页眉另见“对”，有2026年第7期与含`.2026.14.020`的印刷DOI；LE22 p1记录2026-01-19网络首发、收稿2025-08-15，p2题名“对”。对照特性、2.1单膜、2.2生物胶、2.3抗菌剂等段落及参考文献，主体结构高度重合，非两项原始实验。将LE21全篇与LE22去除首发封面后文本去空白，以Python difflib.SequenceMatcher（autojunk=False）比对，相似比0.89385；该数字仅作版本线索，不是学术相似度定论。正文存在润色、引文序号和题录变化，最终题名/期次/页码仍VERSION_UNCONFIRMED。CSV保留2条不同PDF记录，内容证据只计一次；暂不把任何一版列为已完成正式引文。

**完整性重点：** LE05是2页学位摘要（xiv–xv），LE10是1页题录摘要，均缺原方法/结果/图表；不是完整论文。LE02为泰文全文，英文摘要可读，不能称英文全文或PDF损坏。LE20为71页扫描学位论文，只核指定页，不假称全文OCR。LE28实际4页、印刷231–234；首页编号`0231-05`提示可能5页，末页只有参考文献[1]而正文引至[8]，标POSSIBLY_INCOMPLETE；不猜缺页必为235，不补齐终页。长篇论文的少量前置空白页不当作缺损证据。

文件名问题只登记：LE01哈希式名称、LE05/LE10不显题名、LE20文件名“复含”与原文“复合”不一致、若干`2.pdf/3.pdf`后缀；均不改名。没有发现打不开的PDF，不据此宣称内容全无缺损。

## 4. 分层使用矩阵

|ID|真实题名|等级|当前状态|建议章节|引用优先级|
|---|---|---|---|---|---|
|LE01|海藻酸钠和溶菌酶复合涂膜对马陆葡萄贮藏的保鲜效果|C|ABSTRACT_ONLY|1.2.2（可选背景）|LOW|
|LE02|Effect of edible coating with alginate and calcium chloride on postharvest quality of strawberry fruits during low temperature storage|A|ABSTRACT_ONLY|1.2.2；1.2.3；2.3（条件对照）|HOLD_FULLTEXT_REVIEW|
|LE03|POST-HARVEST AS A TOOL TO IMPROVE BERRY FRUIT QUALITY|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；4.1；4.2|HIGH_QUALITATIVE|
|LE04|Harpin处理结合羧甲基壳聚糖/海藻酸钠复合涂膜对哈密瓜保鲜效果的影响|C|ABSTRACT_ONLY|1.2.2（仅可选材料背景）|LOW|
|LE05|QUALITY CHANGES ANALYSIS OF FRESH STRAWBERRY (Fragaria x ananassa) c.v. Kellybright UNDER TROPICAL CONDITION WITH EDIBLE COATINGS|A|ABSTRACT_ONLY|1.2.2；1.2.3（取得全文后）|HOLD_FULLTEXT|
|LE06|Sodium Alginate–Montmorillonite Composite Film Coatings for Strawberry Preservation|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；2.4.4；4.1；4.2|MEDIUM_WITH_CAVEATS|
|LE07|Composite Solution of Tea Polyphenols and Sodium Alginate for Coating Preservation of Strawberries|A|PRIMARY_RESULT_VERIFIED|1.1；1.2.2；1.2.3；2.4.2；4.1；4.2|MEDIUM_QUALITATIVE_ONLY|
|LE08|The Development of a Uniform Alginate-Based Coating for Cantaloupe and Strawberries and the Characterization of Water Barrier Properties|A|PRIMARY_RESULT_VERIFIED|1.1；1.2.1；1.2.2；1.2.3；2.3；2.4.1；4.1；4.2|HIGH|
|LE09|The Effect of Sodium Alginate-Calcium Chloride Coating on the Quality Parameters and Shelf Life of Strawberry Cut Fruits|A|PRIMARY_RESULT_VERIFIED|1.1；1.2.1；1.2.2；1.2.3；2.3；2.4.1；2.4.3；2.4.4；4.1；4.2|HIGH|
|LE10|Effect of alginate coating combined with yeast antagonist on strawberry (Fragaria × ananassa) preservation quality|A|ABSTRACT_ONLY|1.2.2；4.1（取得全文后）|HOLD_FULLTEXT|
|LE11|中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果|C|METHOD_VERIFIED_LIMITED|1.2.1（辅助）；2.3（文献工艺对照）|LOW_OPTIONAL_METHOD|
|LE12|基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究|B|PRIMARY_RESULT_VERIFIED|1.2.3；2.4.1（公式对照）；4.1；4.2|MEDIUM_DISCUSSION|
|LE13|壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究|B|PRIMARY_RESULT_VERIFIED|1.2.3；4.2（可选）|LOW_PENDING_METADATA|
|LE14|壳聚糖/双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用|B|PRIMARY_RESULT_VERIFIED|1.2.3；4.1；4.2（可选）|LOW_WITH_METHOD_CAVEATS|
|LE15|柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜|A|PRIMARY_RESULT_VERIFIED|1.1；1.2.2；1.2.3；2.4.4；4.1；4.2|HIGH_QUALITATIVE|
|LE16|油茶籽饼蛋白-海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；4.1；4.2|MEDIUM_QUALITATIVE_WITH_CONFLICT|
|LE17|海藻糖复合茶多酚对白灵菇保鲜效果的研究|D|EXCLUDED_WITH_REASON|不分配|EXCLUDE|
|LE18|海藻糖对樱桃番茄果实常温保鲜作用及其机理研究|D|EXCLUDED_WITH_REASON|不分配|EXCLUDE|
|LE19|海藻酸钠/壳聚糖/纳米硒复合膜的制备及其在草莓保鲜中的应用|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；2.4.2（定义对照）；4.1；4.2|MEDIUM_RESTRICTED_OUTCOMES|
|LE20|海藻酸钠/纳米CaCO₃复合材料涂膜对冷藏草莓风味的影响|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；2.4.3；2.4.4；4.1；4.2|MEDIUM_SELECTED_PAGES|
|LE21|海藻酸钠在果蔬保鲜中的研究进展|B|VERSION_UNCONFIRMED|1.2.1（辅助线索）；1.2.2（分类线索）|HOLD_VERSION_RESOLUTION|
|LE22|海藻酸钠对果蔬保鲜的研究进展|B|VERSION_UNCONFIRMED|1.2.1（线索）；1.2.2（线索）|HOLD_VERSION_RESOLUTION|
|LE23|海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理|D|EXCLUDED_WITH_REASON|不分配|EXCLUDE|
|LE24|空气负离子环境中草莓采后品质的变化|B|PRIMARY_RESULT_VERIFIED|1.1（指标辅助）；1.2.3；2.4.1；2.4.3；2.4.4；4.1；4.2|MEDIUM_METHOD_LOW_MECHANISM|
|LE25|脂肪酸对魔芋葡甘聚糖/海藻酸钠复合膜结构和性质的影响|B|PRIMARY_RESULT_VERIFIED|1.2.1；4.1；4.2|HIGH_MATERIAL_ONLY|
|LE26|茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究|A|PRIMARY_RESULT_VERIFIED|1.2.2；1.2.3；2.4.2（定义反例）；4.1；4.2|HIGH_QUALITATIVE_WITH_ERROR_FLAGS|
|LE27|茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究|A|PRIMARY_RESULT_VERIFIED|1.2.1；1.2.2；1.2.3；2.3；2.4.4；4.1；4.2|MEDIUM_PENDING_BIBLIOGRAPHY|
|LE28|草莓的涂膜保鲜研究|B|PRIMARY_RESULT_VERIFIED|1.1；1.2.3；4.1；4.2（备选）|HOLD_COMPLETE_VERSION|

## 5. 逐篇机器记录对照

下列每张表与CSV同名字段来自同一份结构化记录，含全部CSV字段；未知项保留原值。引用资格以证据卡的指定论点为单位，不能只看状态列。

### LE01｜海藻酸钠和溶菌酶复合涂膜对马陆葡萄贮藏的保鲜效果

相关性理由：其他果实/复合因素，仅定向辅助用途

原件：[4EA7E7811F4D44AB8B3892557FC72A52.pdf](../4EA7E7811F4D44AB8B3892557FC72A52.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE01|
|canonical_filename|4EA7E7811F4D44AB8B3892557FC72A52.pdf|
|duplicate_files|NONE|
|sha256|525d5c9c5395ae73c9041326b9c7f460e1b673d22f2a9af1ec0bb61fb6971354|
|file_size|448358|
|pdf_pages|6|
|title|海藻酸钠和溶菌酶复合涂膜对马陆葡萄贮藏的保鲜效果|
|authors|胡晓亮；周国燕|
|year|2011|
|journal|食品科学，32(20)：271–276|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|C|
|research_subject|完整马陆葡萄|
|material|海藻酸钠；溶菌酶|
|concentration|摘要报告1%海藻酸钠+0.1%溶菌酶；浓度计量基准UNVERIFIED|
|storage_conditions|4±1℃；RH UNVERIFIED|
|period|25 d|
|groups|水、溶菌酶及不同SA浓度复配，细节未核|
|main_indicators|感官、腐烂指数、质量损失率、硬度、呼吸、VC、SSC、SOD|
|evidence_status|ABSTRACT_ONLY|
|recommended_sections|1.2.2（可选背景）|
|citation_priority|LOW|
|limitations|仅读摘要；葡萄、低温和溶菌酶均不同；不能借作本实验草莓结果|
|read_scope|p1题录、摘要|
|visual_pages||
|version_family|LE01|
|in_chapter01|否|
|new_citation|暂不新增；现有草莓证据优先|

### LE02｜Effect of edible coating with alginate and calcium chloride on postharvest quality of strawberry fruits during low temperature storage

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf](../Effect%2Bof%2Bedible%2Bcoating%2Bwith%2Balginate%2Band%2Bcalcium%2Bchloride%2B.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE02|
|canonical_filename|Effect+of+edible+coating+with+alginate+and+calcium+chloride+.pdf|
|duplicate_files|Effect+of+edible+coating+with+alginate+and+calcium+chloride+ 3.pdf|
|sha256|7a795bdae972cb1c90d740c657642ab8d6e6d71312a405a24c36f7b1baa064bb|
|file_size|561957|
|pdf_pages|11|
|title|Effect of edible coating with alginate and calcium chloride on postharvest quality of strawberry fruits during low temperature storage|
|authors|Tanaporn Kraiyut；Araya Youngjorhor；Nattareya Nusean；Wasna Pithakpol|
|year|2023|
|journal|Health Science, Science and Technology Reviews，16(2)：95–105|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊原始研究|
|language|泰文正文；英/泰摘要|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓，cv. Paratchatan 80，70–80%转红|
|material|海藻酸盐；CaCl₂；臭氧水前处理|
|concentration|alginate 0.25%、0.5%、1.0%；CaCl₂ 2%；上述%基准UNVERIFIED；臭氧水100 ppm 30 s|
|storage_conditions|先5±2℃、80%RH 15 d；再25±2℃、65%RH 2 d|
|period|15+2 d；不是连续常温17 d|
|groups|单独/组合涂膜与对照；泰文完整组表待核|
|main_indicators|失重、腐烂等品质；完整指标定义待泰文核读|
|evidence_status|ABSTRACT_ONLY|
|recommended_sections|1.2.2；1.2.3；2.3（条件对照）|
|citation_priority|HOLD_FULLTEXT_REVIEW|
|limitations|泰文正文尚未可靠通读；p4显示每盒12果/盒通气，不能把果实数直接当独立n；需泰文方法、图表译核后才可正式比较结果|
|read_scope|p1–2题录/双语摘要；p3–4方法局部；结果未完成核译|
|visual_pages||
|version_family|LE02|
|in_chapter01|否|
|new_citation|暂缓结果引用；可登记方法线索，不能声称完成全文精读|

### LE03｜POST-HARVEST AS A TOOL TO IMPROVE BERRY FRUIT QUALITY

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[Greta_Peretto_PhD_dissertation.pdf](../Greta_Peretto_PhD_dissertation.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE03|
|canonical_filename|Greta_Peretto_PhD_dissertation.pdf|
|duplicate_files|NONE|
|sha256|a056765038865fdb6c5bfaa2f69cc83e8ca7f4f0cbee996bf198e67c163ef151|
|file_size|1586149|
|pdf_pages|202|
|title|POST-HARVEST AS A TOOL TO IMPROVE BERRY FRUIT QUALITY|
|authors|Greta Peretto|
|year|2014（p3声明日期2014-01-31）|
|journal|博士学位论文，Università degli Studi di Padova；非期刊卷期|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|博士学位论文|
|language|英文正文；意大利文封面/摘要|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|第5章完整草莓；论文其他章另含蓝莓及草莓泥|
|material|海藻酸钠；香芹酚；肉桂酸甲酯；静电喷涂|
|concentration|SA 2% w/v；甘油1.5% w/v；香芹酚0.98% w/w、肉桂酸甲酯1.45% w/w；不含本研究Ca步骤|
|storage_conditions|7.5±0.5℃；90%RH；配液70℃/喷液40℃不是贮藏温度|
|period|13 d；主要检测0、4、8、13 d；腐烂逐日|
|groups|未涂CK；普通喷涂NE；85 kV静电喷涂ES；文中36果/三重复，物理独立单位分配仍不宜擅推|
|main_indicators|沉积效率与均匀性、可见腐烂、失重、硬度、颜色、总酚、抗氧化力；TSP不是TSS|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；4.1；4.2|
|citation_priority|HIGH_QUALITATIVE|
|limitations|定向深读第5章，不宣称202页全篇精读；复配挥发活性物、静电设备及低温均不同；相同课题的已发表期刊研究若后续入库需查重，当前未发现已证实同源刊文|
|read_scope|p1、3、5–7、14–16；第5章p177–190定向方法/结果/讨论；p195–199图表定位（195–197已目视）|
|visual_pages|195,196,197|
|version_family|LE03|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE04｜Harpin处理结合羧甲基壳聚糖/海藻酸钠复合涂膜对哈密瓜保鲜效果的影响

相关性理由：其他果实/复合因素，仅定向辅助用途

原件：[Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf](../Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE04|
|canonical_filename|Harpin处理结合羧甲基壳聚糖_海藻酸钠复合涂膜对哈密瓜保鲜效果的影响.pdf|
|duplicate_files|NONE|
|sha256|d9fbb2814e9a053f20f66993548aec97ca6ec24d38820a49fc3aaa4273c7d8e0|
|file_size|861790|
|pdf_pages|6|
|title|Harpin处理结合羧甲基壳聚糖/海藻酸钠复合涂膜对哈密瓜保鲜效果的影响|
|authors|周研；谢晶；周然；李念文|
|year|2015|
|journal|现代食品科技，31(4)；现有PDF印刷248–253，首页文章篇号248–252，正式终页UNVERIFIED|
|doi|10.13982/j.mfst.1673-9078.2015.4.040|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|C|
|research_subject|完整哈密瓜|
|material|Harpin；羧甲基壳聚糖；SA；肉桂醛等|
|concentration|Harpin 90 mg/L 3 min；羧甲基壳聚糖0.5%、SA 1%、甘油0.5%、Tween80 0.6%、肉桂醛0.5%；%基准本轮未展开核对|
|storage_conditions|19±2℃；RH UNVERIFIED|
|period|UNVERIFIED|
|groups|CK、复合涂膜、Harpin+复合涂膜|
|main_indicators|硬度、VC、MDA、POD、霉菌酵母等|
|evidence_status|ABSTRACT_ONLY|
|recommended_sections|1.2.2（仅可选材料背景）|
|citation_priority|LOW|
|limitations|对象和多重处理均不同；仅定向摘要/题录，不作为草莓核心原始结果；首页文章篇号终页252与现有p6印刷253不一致，正式终页不自行补定|
|read_scope|p1题录/摘要；p6终页|
|visual_pages||
|version_family|LE04|
|in_chapter01|否|
|new_citation|不建议为了篇幅新增|

### LE05｜QUALITY CHANGES ANALYSIS OF FRESH STRAWBERRY (Fragaria x ananassa) c.v. Kellybright UNDER TROPICAL CONDITION WITH EDIBLE COATINGS

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[S1-2018-333159-abstract.pdf](../S1-2018-333159-abstract.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE05|
|canonical_filename|S1-2018-333159-abstract.pdf|
|duplicate_files|NONE|
|sha256|002b73d5a7840f349d5977b2076af85acbb7aaeaeefbffb70b8c793d2b3ebd94|
|file_size|287363|
|pdf_pages|2|
|title|QUALITY CHANGES ANALYSIS OF FRESH STRAWBERRY (Fragaria x ananassa) c.v. Kellybright UNDER TROPICAL CONDITION WITH EDIBLE COATINGS|
|authors|摘要署名Putri Wahyuni S.；Jumeri Mangunwikarta；Moh. Affan Fajar Falah；页脚学位作者为PUTRI W SIBURIAN（姓名形式待正式题录统一）|
|year|2018（PDF页脚机构记录）|
|journal|Universitas Gadjah Mada学位论文摘要；p xiv–xv；完整论文题录UNVERIFIED|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|学位论文摘要摘件|
|language|印度尼西亚文/英文摘要|
|completeness|ABSTRACT_EXCERPT|
|relevance_level|A|
|research_subject|完整草莓，Kellybright|
|material|SA；CMC；硬脂酸；肉桂精油；Tween20|
|concentration|SA 2% w/v；甘油0.5% v/v；CMC 0.1% w/v；硬脂酸0.5% w/v；肉桂精油0.5% v/v；Tween20 0.2% v/v|
|storage_conditions|27±2℃；RH UNVERIFIED|
|period|UNVERIFIED|
|groups|普通alginate与抗菌alginate涂膜；完整对照设置UNVERIFIED|
|main_indicators|失重、硬度、色、SSC、VC、酸、气味、微生物；另有经济分析|
|evidence_status|ABSTRACT_ONLY|
|recommended_sections|1.2.2；1.2.3（取得全文后）|
|citation_priority|HOLD_FULLTEXT|
|limitations|仅2页摘要，原方法、结果、图表全部不在本文件；作者姓名/导师身份正式题录需统一；不把摘要所称三重复和ANOVA当作独立性已核|
|read_scope|p1–2全部现有摘要（不是全文）|
|visual_pages||
|version_family|LE05|
|in_chapter01|否|
|new_citation|暂不作为正式结果引文；优先补全文而非补写摘要结论|

### LE06｜Sodium Alginate–Montmorillonite Composite Film Coatings for Strawberry Preservation

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[coatings-14-01331 2.pdf](../coatings-14-01331%202.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE06|
|canonical_filename|coatings-14-01331 2.pdf|
|duplicate_files|NONE|
|sha256|0daef1792527746bb83ddc35429acb73fe612ddf47de9e8cbe05f879b92a81a4|
|file_size|3272094|
|pdf_pages|15|
|title|Sodium Alginate–Montmorillonite Composite Film Coatings for Strawberry Preservation|
|authors|Xiaoping Yan；Zuolong Yu；Yao Chen；Chao Han；Yunxiao Wei；Fan Yang；Yan Qian；Yong Wang|
|year|2024|
|journal|Coatings，14：1331|
|doi|10.3390/coatings14101331|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|英文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓|
|material|SA；蒙脱土MMT；甘油；乙酸配液|
|concentration|SA 2.0 g；甘油为SA质量10%；MMT材料图标称0、10、12、14、16、18、20%，百分比基准UNVERIFIED；果实用T1单SA、T2标称10%、T3标称20%MMT；50 mL+100 mL的2% v/v乙酸配液步骤，不能写纯水SA|
|storage_conditions|4℃；RH UNVERIFIED；50℃流延干燥不是果实贮藏|
|period|12 d；0、3、6、9、12 d|
|groups|CK；T1 SA；T2 10%MMT；T3 20%MMT；36果/组，独立容器层级未清楚闭环|
|main_indicators|失重、MDA、呼吸、TA、可溶性糖、总酚、SSC；材料拉伸不是果实硬度|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；2.4.4；4.1；4.2|
|citation_priority|MEDIUM_WITH_CAVEATS|
|limitations|低温/填料/乙酸不同；p3与p6/13 WVP量纲写法不一致，不跨文比较WVP数值；图4标为0 d时各组已非零，称重基线解释未闭环，结果仅定性采用；机理解释不能当本研究实测|
|read_scope|p1–6题录/方法/材料结果；p7–13果实相关结果与结论定向；p8、12图已目视|
|visual_pages|8,12|
|version_family|LE06|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE07｜Composite Solution of Tea Polyphenols and Sodium Alginate for Coating Preservation of Strawberries

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[eb0e68fb8f6c2a811368a62e444e782162e8.pdf](../eb0e68fb8f6c2a811368a62e444e782162e8.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE07|
|canonical_filename|eb0e68fb8f6c2a811368a62e444e782162e8.pdf|
|duplicate_files|eb0e68fb8f6c2a811368a62e444e782162e8 2.pdf|
|sha256|d4f9e735c0b02f01bf568dd9ce8b06485d00fadfe9a9047a1d8664dc78606634|
|file_size|224783|
|pdf_pages|7|
|title|Composite Solution of Tea Polyphenols and Sodium Alginate for Coating Preservation of Strawberries|
|authors|Cuili Gao；Ying Ding；Jinhua Li；Zonghua Wang；Dongwei Han；Yanzhi Xia|
|year|2015|
|journal|Advance Journal of Food Science and Technology，9(8)：651–657|
|doi|10.19026/ajfst.9.1981|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|英文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓，Laoshan Mingbao|
|material|SA；茶多酚|
|concentration|SA 1 g/100 mL水；茶多酚0.1–0.5 g/100 mL梯度；原文后段0.4%/4%混写，不照抄4%|
|storage_conditions|room temperature；具体℃与RH UNVERIFIED；50℃为制液水浴|
|period|20 d；摘要/图2 d间隔与方法部分4 d检查表述不一致|
|groups|CK0未处理；CK单SA；A–E茶多酚梯度复配|
|main_indicators|失重、腐烂指数、硬度、呼吸、VC、TA、TSS|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1；1.2.2；1.2.3；2.4.2；4.1；4.2|
|citation_priority|MEDIUM_QUALITATIVE_ONLY|
|limitations|温湿度数值缺失、观察间隔和剂量写法不一；腐烂为等级加权指数而非累计腐烂比例；不采精确效应量、保质天数或最佳剂量；仪器重复不可当独立n；p6图6酸度横轴延至40 d，与20 d研究期不符，不采TA图定量；图7 TSS上升不宜被概述为各组糖含量下降|
|read_scope|p1–6题录、实验/结果/讨论；p7题录/参考文献抽核；p3图1/2目视（既有核验复用）；本轮目视p6图6/7|
|visual_pages|3,6|
|version_family|LE07|
|in_chapter01|是，[4]|
|new_citation|已用于第一章[4]；保留限定引用，新增硬度/TSS不确定性时先处理其内部表述问题|

### LE08｜The Development of a Uniform Alginate-Based Coating for Cantaloupe and Strawberries and the Characterization of Water Barrier Properties

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[foods-08-00203-v2 2.pdf](../foods-08-00203-v2%202.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE08|
|canonical_filename|foods-08-00203-v2 2.pdf|
|duplicate_files|NONE|
|sha256|ca6776176de675559ba75c9b8fa207704ce4a835ea710d6fff973b99ecd18f0f|
|file_size|2022786|
|pdf_pages|21|
|title|The Development of a Uniform Alginate-Based Coating for Cantaloupe and Strawberries and the Characterization of Water Barrier Properties|
|authors|Tugce Senturk Parreidt；Martina Lindner；Isabell Rothkopf；Markus Schmid；Kajetan Müller|
|year|2019|
|journal|Foods，8：203|
|doi|10.3390/foods8060203|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|英文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓及鲜切甜瓜，须分别识别|
|material|SA；乳酸钙；甘油；葵花油；Span80；Tween80|
|concentration|SA 1.25%、甘油2%、葵花油0.2%、Span80 1%、Tween80 0.2%（配方w/w）；乳酸钙2%|
|storage_conditions|果实10℃、90%RH；独立膜23℃/50%RH及RH梯度试验另列，不能混为贮藏条件|
|period|贮藏试验14 d；其他材料/吸脱湿试验不同周期|
|groups|未涂；常规SA→Ca；新增前置Ca的Ca→SA→Ca；保鲜比较用新流程与未涂，不把额外钙步骤抹去|
|main_indicators|涂层均匀性/厚度、失重、水活度、水蒸气阻力WVR；独立膜WVTR|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1；1.2.1；1.2.2；1.2.3；2.3；2.4.1；4.1；4.2|
|citation_priority|HIGH|
|limitations|含脂质/表活剂、乳酸钙、额外前置钙，与本研究双步CaCl₂不同；独立膜和果面膜、WVR和WVP指标不可互换；深入分子机理需另核基础一手文献|
|read_scope|p1–17与本题相关的引言、方法、结果、讨论和结论；参考文献p18–21未逐条精读；p9图3目视既有核验复用|
|visual_pages|9|
|version_family|LE08|
|in_chapter01|是，[3]|
|new_citation|已用于第一章[3]；可深化物理阻隔的条件性，不重复罗列结果|

### LE09｜The Effect of Sodium Alginate-Calcium Chloride Coating on the Quality Parameters and Shelf Life of Strawberry Cut Fruits

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[jcs-04-00123.pdf](../jcs-04-00123.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE09|
|canonical_filename|jcs-04-00123.pdf|
|duplicate_files|jcs-04-00123 2.pdf|
|sha256|424d6ba731c6e2997fba900c8e77c7cc077de75fe7562a0580901122f541c534|
|file_size|1592335|
|pdf_pages|15|
|title|The Effect of Sodium Alginate-Calcium Chloride Coating on the Quality Parameters and Shelf Life of Strawberry Cut Fruits|
|authors|Ghaidaa Alharaty；Hosahalli S. Ramaswamy|
|year|2020|
|journal|Journal of Composites Science，4：123|
|doi|10.3390/jcs4030123|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|英文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|鲜切草莓（约1 cm切片），非完整果|
|material|SA；CaCl₂|
|concentration|SA 2% w/w、CaCl₂ 2% w/w；依次浸渍各5 min，步骤间沥液1 min，末次晾10 min|
|storage_conditions|4℃；RH UNVERIFIED；PVC覆盖并开4–5孔，容器6–7切片|
|period|15 d；每3 d检测|
|groups|未涂切片；SA→CaCl₂切片|
|main_indicators|初始质量失重、呼吸、质构、TSS、pH、TA、颜色、微生物|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1；1.2.1；1.2.2；1.2.3；2.3；2.4.1；2.4.3；2.4.4；4.1；4.2|
|citation_priority|HIGH|
|limitations|切片损伤、4℃、包装、浸渍时间均不同；文章称多次检测未使其成为本项目独立n证据；微生物平板计数不是本实验累计腐烂率|
|read_scope|p1–12相关理论、方法与结果；p13图注定位；p14结论；参考文献未逐条精读；p6图2目视既有核验复用|
|visual_pages|6|
|version_family|LE09|
|in_chapter01|是，[2]|
|new_citation|已用于第一章[2]；保留，方法参数仅作为文献方法，不填成本实验参数|

### LE10｜Effect of alginate coating combined with yeast antagonist on strawberry (Fragaria × ananassa) preservation quality

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[mh611.pdf](../mh611.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE10|
|canonical_filename|mh611.pdf|
|duplicate_files|NONE|
|sha256|954c07da9bbb54aa4db3426b974de56b095e71f0a5f30e180da430a6f83708ae|
|file_size|79444|
|pdf_pages|1|
|title|Effect of alginate coating combined with yeast antagonist on strawberry (Fragaria × ananassa) preservation quality|
|authors|Yan Fan；Ying Xu；Dongfeng Wang；Li Zhang；Jipeng Sun；Liping Sun；Bin Zhang|
|year|2009|
|journal|Postharvest Biology and Technology，53(1–2)：84–90（摘要页题录）|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊文献摘要/题录摘件|
|language|英文|
|completeness|ABSTRACT_EXCERPT|
|relevance_level|A|
|research_subject|草莓；完整形态仅摘要语境，详细取样待全文|
|material|SA；Cryptococcus laurentii；脂质/β-环糊精|
|concentration|摘要列SA 2% w/v、甘油2% w/v、棕榈酸0.5% w/v、单硬脂酸甘油酯0.5% w/v、β-环糊精0.5% w/v；酵母10⁹ CFU/mL|
|storage_conditions|温度及RH UNVERIFIED|
|period|UNVERIFIED|
|groups|基础alginate与酵母复配；完整分组UNVERIFIED|
|main_indicators|腐烂、失重、硬度、颜色、花青素等|
|evidence_status|ABSTRACT_ONLY|
|recommended_sections|1.2.2；4.1（取得全文后）|
|citation_priority|HOLD_FULLTEXT|
|limitations|1页不是84–90完整论文；温湿度/样本结构未知，不虚构DOI；只作追索线索，不写正式详细结果|
|read_scope|p1全部现有内容|
|visual_pages||
|version_family|LE10|
|in_chapter01|否|
|new_citation|暂不新增结果引文|

### LE11｜中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果

相关性理由：其他果实/复合因素，仅定向辅助用途

原件：[中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf](../中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE11|
|canonical_filename|中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果_朱莹恒.pdf|
|duplicate_files|NONE|
|sha256|4acf4c5f7f4f7308aa449d8158d396a7a5501658dc8646e25fe96335346ac940|
|file_size|1383975|
|pdf_pages|7|
|title|中草药海藻酸钠复合膜的制备及其对圣女果的保鲜效果|
|authors|朱莹恒；魏晴；王麒迦；钟天宇；张晶|
|year|2026|
|journal|苏州工学院学报，40(2)：39–45|
|doi|10.16101/j.cnki.cn32-1749/z.2026.02.002|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|C|
|research_subject|完整圣女果|
|material|五倍子提取物；SA；CaCl₂|
|concentration|提取物100 g/L；SA 5 g/L；CaCl₂ 20 g/L；果实浸复合液30 s再钙处理（时长未核）|
|storage_conditions|4℃；RH UNVERIFIED；PE自封袋|
|period|12 d；每3 d|
|groups|提取物浓度梯度复合膜与对照|
|main_indicators|成膜、失重、品质等|
|evidence_status|METHOD_VERIFIED_LIMITED|
|recommended_sections|1.2.1（辅助）；2.3（文献工艺对照）|
|citation_priority|LOW_OPTIONAL_METHOD|
|limitations|非草莓且有中草药；p5失重正文“最多”对应浓度和给定数值排序疑有不一致，未扩大解释；不能替本研究确认交联程度|
|read_scope|p1–3方法/成膜段；p5文字抽核，未作图值正式证据|
|visual_pages||
|version_family|LE11|
|in_chapter01|否|
|new_citation|仅确需其他果实例证时选用，不为增数量强引|

### LE12｜基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf](../基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE12|
|canonical_filename|基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究_侯秋月.pdf|
|duplicate_files|NONE|
|sha256|71b6a326ae412bdd5721d35ca7e295081adea4111350da7f3750f950bb0f6f90|
|file_size|5038343|
|pdf_pages|86|
|title|基于相转变溶菌酶的抑菌薄膜构建及其在草莓保鲜中的应用研究|
|authors|侯秋月|
|year|2026|
|journal|湖北工业大学硕士学位论文|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|硕士学位论文|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|第3章完整草莓；重点PTL/ε-PL包装膜|
|material|相转变溶菌酶PTL；还原型谷胱甘肽；ε-聚赖氨酸；PE承载膜|
|concentration|溶菌酶7 mg/mL、GSH 7 mg/mL溶液及ε-PL 1 mg/mL等制膜步骤；混合后最终浓度不得自行折算|
|storage_conditions|室温，具体℃及RH UNVERIFIED；30℃为PE上成膜干燥温度|
|period|7 d；0、1、3、5、7 d|
|groups|无覆盖CK；PE；PTL/PE；PTL/ε-PL/PE|
|main_indicators|硬度N、初始质量失重、糖度/酸度、外观；材料抗菌为另项试验|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.3；2.4.1（公式对照）；4.1；4.2|
|citation_priority|MEDIUM_DISCUSSION|
|limitations|无SA；PE覆盖包装不同于果面浸渍；实际温度缺失；“硬度保留率”以N表达不应作为百分比；糖度样品稀释流程与直接果汁TSS不同，不能横比绝对值；只深读第3章，不宣称86页全读|
|read_scope|p1、3–6摘要、p8–10目录；p49–51方法；p57–60相关结果/讨论|
|visual_pages|58,59,60|
|version_family|LE12|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE13｜壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf](../壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE13|
|canonical_filename|壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究_罗阳.pdf|
|duplicate_files|NONE|
|sha256|819b79c2ebdeca081808a53db19acf6197da2be24fd730c2e107d600100cc90e|
|file_size|213342|
|pdf_pages|7|
|title|壳聚糖-银纳米粒子复合物的抗氧化活性及其对草莓保鲜效果的研究|
|authors|罗阳；郑一丹；肖益东|
|year|2025|
|journal|农产品加工，2025年第8期：17–23；DOI字符串含.15，正式期次对应待核|
|doi|10.16693/j.cnki.1671-9646（X）.2025.15.005（PDF印刷，期次对应UNVERIFIED）|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|完整草莓|
|material|壳聚糖CS；银纳米粒子Ag-NPs|
|concentration|Ag:CS质量比1:3、1:6、1:9；最终浸液材料浓度UNVERIFIED|
|storage_conditions|4℃；RH UNVERIFIED|
|period|8 d；0、2、4、6、8 d|
|groups|超纯水；CS；三种Ag:CS复合处理；浸渍30 s|
|main_indicators|失重、腐烂、感官、pH、VC；体外抗氧化另项|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.3；4.2（可选）|
|citation_priority|LOW_PENDING_METADATA|
|limitations|无SA/钙、低温且含银；刊期与DOI编号对应有待官方题录确认；材料食品接触/食用安全不由这些品质试验证明；引言不严谨术语不采|
|read_scope|p1–3题录、合成与果实方法；p4–5果实结果|
|visual_pages|4,5|
|version_family|LE13|
|in_chapter01|否|
|new_citation|不优先入第一章；第四章确需其他材料对照且题录复核后选用|

### LE14｜壳聚糖/双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf](../壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE14|
|canonical_filename|壳聚糖_双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用_周渲皓.pdf|
|duplicate_files|NONE|
|sha256|80dee03ecf1ed141a567f3e5463f9eca1de3473c022484878aed2bfc80ab257a|
|file_size|5617725|
|pdf_pages|101|
|title|壳聚糖/双金属纳米酶抗菌复合膜的制备及其在葡萄和草莓保藏中的应用|
|authors|周渲皓|
|year|2025|
|journal|四川农业大学硕士学位论文|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|硕士学位论文|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|第2章完整红颜草莓；同章葡萄须排除混用|
|material|壳聚糖；CoFe₂O₄/MXene（CM）独立覆盖膜|
|concentration|p26概述CS 3 wt%、CM 1/3/5/7 vol%；p28制备改写CS 3% w/v、CM 0/1/3/5/7% w/v、甘油1% v/v。计量基准内部不一致，最终应用CS/5%CM的实际浓度UNVERIFIED，不自行统一|
|storage_conditions|20–26℃；54–70%RH；培养皿上方覆膜|
|period|草莓6 d每日；葡萄12 d每2 d，不能混用|
|groups|无膜；PE；CS；CS/5%CM|
|main_indicators|草莓感官、硬度、失重、TSS等；体外抗菌/光照试验另列|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.3；4.1；4.2（可选）|
|citation_priority|LOW_WITH_METHOD_CAVEATS|
|limitations|只核第2章相关部分；每组三次测量不说明独立容器n；p27“9 mol/mL盐酸”量纲及CoFe材料步骤写“氯化铜”有明显方法表述疑点，不能借作可复现合成SOP；硬度kg/cm²不能与本研究N直接比；p26与p28配方浓度基准矛盾，不复用其精确配方。p27两处问题经页面目视确认|
|read_scope|p1–10题录/摘要/目录；p26–28制备；p31–34方法；p46–50果实结果；未精读第3章|
|visual_pages|27,50|
|version_family|LE14|
|in_chapter01|否|
|new_citation|不优先第一章；讨论中确有覆盖方式对照需要时限定使用|

### LE15｜柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf](../柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE15|
|canonical_filename|柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜_陈妮娜.pdf|
|duplicate_files|NONE|
|sha256|65f17f5af496699859c550b947a7014e8dbe316d88b2ba34336b215f82786271|
|file_size|3527405|
|pdf_pages|5|
|title|柚皮果胶-海藻酸钠可食复合膜对草莓的保鲜|
|authors|陈妮娜；曾稍俏|
|year|2017|
|journal|食品科技，42(3)：60–64|
|doi|10.13684/j.cnki.spkj.2017.03.015|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓，八成熟|
|material|柚皮果胶；SA；甘油；茶树油；PE包装|
|concentration|配制2%SA、2%果胶液（质量比例制液）；甘油/茶树油最终用量文中未充分闭环，不自行补数|
|storage_conditions|5–10℃、60%RH；正文称“常温”但须用实际条件|
|period|12 d；每2 d|
|groups|空白A；PE B；独立复合膜托盘C；复合液浸1 min D；液涂+PE E；每组6份约200 g|
|main_indicators|腐烂、失重、TA、SSC、蛋白、VC、MDA、SOD等|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1；1.2.2；1.2.3；2.4.4；4.1；4.2|
|citation_priority|HIGH_QUALITATIVE|
|limitations|温度不是一般室温；复合液+PE有包装混杂；p3海藻酸钠“阳离子”及p4出现“葡萄”属于原文表述问题，不照抄；腐烂判据引用他文，不自动当本研究累计腐烂率；p4文字“第2天所有处理均略升”与图4多数组下降不一致，不照抄该共同时间趋势|
|read_scope|p1–5定向核读相关材料/方法/结果/结论；p3图1/2目视（既有核验复用）；p4 SSC文字和图4已目视|
|visual_pages|3,4|
|version_family|LE15|
|in_chapter01|是，[1]|
|new_citation|已用于第一章[1]；保留条件限定，不把SSC解释当已证机制|

### LE16｜油茶籽饼蛋白-海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf](../油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE16|
|canonical_filename|油茶籽饼蛋白—海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究_陈静.pdf|
|duplicate_files|NONE|
|sha256|e10b3b5f65d3815976c3d0764b5cd50f5ed27d1836f4bd91d225657703b11d17|
|file_size|7253062|
|pdf_pages|104|
|title|油茶籽饼蛋白-海藻酸钠活性包装膜的制备及其在水果保鲜中的应用研究|
|authors|陈静|
|year|2025|
|journal|广西大学硕士学位论文|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|硕士学位论文|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|第3/4章完整草莓；香蕉硬度结果须与草莓区分|
|material|SA；油茶籽饼蛋白CCP；柠檬酸CA；甘油；第4章另有丁香精油/单宁酸体系CE|
|concentration|第3章20 g、3 wt%SA液；CCP 0–0.48 g；甘油0.48 g；柠檬酸0.8 g；SA-CCP0.6为应用配方；最终单位按原步骤保留|
|storage_conditions|果实25℃、50%RH；膜表征/干燥40℃、WVP杯条件不是果实贮藏|
|period|第3章草莓7 d（1、3、5、7 d等）；第4章9 d|
|groups|第3章未处理CK与SA-CCP0.6喷涂；p44–45明确喷3次，非仅独立膜包裹|
|main_indicators|草莓失重、颜色、感官、腐烂；该段硬度测定对象是香蕉，不能编成草莓硬度|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；4.1；4.2|
|citation_priority|MEDIUM_QUALITATIVE_WITH_CONFLICT|
|limitations|SA-CCP、柠檬酸交联/复合不同于SA-Ca；p43 CaCl₂是WVP干燥剂，CA是citric acid非calcium；独立容器n不明；失重幅度很大，不能认证原始准确度；第4章配方方法未完整核读，只作冲突登记，不接纳其定量效应|
|read_scope|p1–8题录/摘要/目录；p42–45第3章方法；p57–58结果；p86–87第4章结果矛盾定位，非全论文精读|
|visual_pages|58,87|
|version_family|LE16|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE17｜海藻糖复合茶多酚对白灵菇保鲜效果的研究

相关性理由：排除理由见限制与论点栏

原件：[海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf](../海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE17|
|canonical_filename|海藻糖复合茶多酚对白灵菇保鲜效果的研究_张爱莉.pdf|
|duplicate_files|NONE|
|sha256|9874a84f6002329e1dd2722a1f3ee22fc1e5a3cbeed8b22588ba93a55c4e30f8|
|file_size|1454285|
|pdf_pages|4|
|title|海藻糖复合茶多酚对白灵菇保鲜效果的研究|
|authors|张爱莉；苗泽；王梦茹；肖意南；卢作焜|
|year|2026|
|journal|许昌学院学报，45(5)：74–77|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|D|
|research_subject|白灵菇|
|material|海藻糖trehalose；茶多酚；不是海藻酸钠|
|concentration|海藻糖1 g/L、茶多酚2 g/L（摘要方案）|
|storage_conditions|4℃；RH UNVERIFIED|
|period|14 d|
|groups|本轮不展开|
|main_indicators|白灵菇品质|
|evidence_status|EXCLUDED_WITH_REASON|
|recommended_sections|不分配|
|citation_priority|EXCLUDE|
|limitations|不能因“海藻”二字引入SA理论或草莓讨论|
|read_scope|p1题录、摘要、材料|
|visual_pages||
|version_family|LE17|
|in_chapter01|否|
|new_citation|否|

### LE18｜海藻糖对樱桃番茄果实常温保鲜作用及其机理研究

相关性理由：排除理由见限制与论点栏

原件：[海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf](../海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE18|
|canonical_filename|海藻糖对樱桃番茄果实常温保鲜作用及其机理研究_夏明慧.pdf|
|duplicate_files|NONE|
|sha256|5352e499fcc9b3b00c01260d7e694ceceef2094aa8207e3eefb5d5e68db660f2|
|file_size|5362932|
|pdf_pages|73|
|title|海藻糖对樱桃番茄果实常温保鲜作用及其机理研究|
|authors|夏明慧|
|year|2022|
|journal|合肥工业大学硕士学位论文|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|硕士学位论文|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|D|
|research_subject|樱桃番茄|
|material|海藻糖trehalose；不是SA|
|concentration|不用于本题，未抽取|
|storage_conditions|常温，数值本轮不核|
|period|本轮不核|
|groups|本轮不核|
|main_indicators|番茄保鲜/机理|
|evidence_status|EXCLUDED_WITH_REASON|
|recommended_sections|不分配|
|citation_priority|EXCLUDE|
|limitations|前置空白页不认定损坏；不需要精读无关机理|
|read_scope|p1–4封面及英文题录（p4日期May 2022）|
|visual_pages||
|version_family|LE18|
|in_chapter01|否|
|new_citation|否|

### LE19｜海藻酸钠/壳聚糖/纳米硒复合膜的制备及其在草莓保鲜中的应用

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf](../海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE19|
|canonical_filename|海藻酸钠_壳聚糖_纳米硒复合膜的制备及其在草莓保鲜中的应用_王清.pdf|
|duplicate_files|NONE|
|sha256|07e8969a8dfbfb153ed2c30ed25f6d7562c0783833996274c313422b95907c24|
|file_size|2346157|
|pdf_pages|9|
|title|海藻酸钠/壳聚糖/纳米硒复合膜的制备及其在草莓保鲜中的应用|
|authors|王清；陈秋怡；雷磊；孙鹤；赵艺飞；朱静；刘涛|
|year|2025|
|journal|食品与发酵工业，51(17)：317–325|
|doi|10.13995/j.cnki.11-1802/ts.041356|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓|
|material|SA；壳聚糖CS；纳米硒；甘油|
|concentration|SA/CS液各1.5 g/100 mL；质量比0:1、1:0、1:1、2:1、1:2；另加甘油1 g与纳米硒2 mL；纳米硒最终浓度UNVERIFIED|
|storage_conditions|温度/RH UNVERIFIED；45℃8 h为流延干燥，不是贮藏|
|period|7 d；0、1、3、5、7 d|
|groups|CK及不同SA:CS复合膜；应用描述为覆膜，未核清实际固定/包覆方式|
|main_indicators|硬度、腐烂率、失重、VC；材料性能/体外抑菌另列|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；2.4.2（定义对照）；4.1；4.2|
|citation_priority|MEDIUM_RESTRICTED_OUTCOMES|
|limitations|p3式(6)实存m₄/(m₃−m₄)×100，m₃初始、m₄贮藏质量，非标准失重公式，目视确认非抽取错误；温湿度、实际覆膜与重复层级未闭环；不证明材料安全或本实验抑菌|
|read_scope|p1–3材料/方法；p6–8相关结果/讨论/结论；p3、7图式目视|
|visual_pages|3,7|
|version_family|LE19|
|in_chapter01|否|
|new_citation|可选硬度/腐烂限定论点；失重精确结果不建议新增|

### LE20｜海藻酸钠/纳米CaCO₃复合材料涂膜对冷藏草莓风味的影响

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf](../海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE20|
|canonical_filename|海藻酸钠_纳米CaCO_3复含材料涂膜对冷藏草莓风味的影响_朱金花.pdf|
|duplicate_files|NONE|
|sha256|b071ee75d131b94d86450166dbde8172cc587fde9e68866c8c950255d1f2d5c7|
|file_size|6840001|
|pdf_pages|71|
|title|海藻酸钠/纳米CaCO₃复合材料涂膜对冷藏草莓风味的影响|
|authors|朱金花|
|year|2019|
|journal|扬州大学硕士学位论文（封面2019年5月）|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|硕士学位论文（扫描件）|
|language|中文；英文摘要|
|completeness|APPARENTLY_COMPLETE_SCAN|
|relevance_level|A|
|research_subject|完整草莓；第2章品质评价|
|material|SA；CMC；改性纳米CaCO₃；甘油|
|concentration|基础CTS：SA 1.5 g、CMC 1.0 g、甘油0.3 g/100 mL水；初始CTSS另加改性CaCO₃ 0.05 g；摘要优化SA 1.6 g/CMC 0.85 g/CaCO₃ 0.05 g，勿与基础配方混同，最优配制基准待完整设计表复核|
|storage_conditions|4℃、85%RH冷藏12 d；再20℃2 d模拟货架期|
|period|12+2 d；冷藏每3 d取样|
|groups|CK无处理；CTS基础液；CTSS优化膜；每组60果、浸5–10 s、重复3次；独立处理/容器层级UNVERIFIED|
|main_indicators|失重、硬度、SSC、呼吸、色差、TA、VC等；后续风味/GC–MS未深读|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；2.4.3；2.4.4；4.1；4.2|
|citation_priority|MEDIUM_SELECTED_PAGES|
|limitations|71页无文本层，不是损坏；只定向目视所列页，未全篇OCR/精读；p21失重式称“称重前后”，是否始终初始基线应再核；不能把60果×3当本实验独立n；风味结论没有在本轮核验|
|read_scope|仅目视p1、3、4、6、7、8、9、17、19、21、22、30、31、33；结果限第2章所列图|
|visual_pages|1,3,4,6,7,8,9,17,19,21,22,30,31,33|
|version_family|LE20|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE21｜海藻酸钠在果蔬保鲜中的研究进展

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf](../海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE21|
|canonical_filename|海藻酸钠在果蔬保鲜中的研究进展_梁昭榆.pdf|
|duplicate_files|NONE|
|sha256|24981bf71632a7ec94e46fdd1fc74cec695829c4ee7092371b8b01a886aa9a9b|
|file_size|1641594|
|pdf_pages|4|
|title|海藻酸钠在果蔬保鲜中的研究进展|
|authors|梁昭榆；卓琳；温建珊；陈晓莹；林慧仪；吴慧|
|year|2026|
|journal|农产品加工，2026年第7期；p1印刷107，后续页码待正式题录统一|
|doi|10.16693/j.cnki.1671-9646（X）.2026.14.020（PDF印刷；刊期/版本对应UNVERIFIED）|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|综述|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|多种果蔬研究综述，非独立实验|
|material|SA及各类复配膜|
|concentration|NOT_APPLICABLE（无本篇原始处理）|
|storage_conditions|NOT_APPLICABLE（综述汇集，不设统一温湿度）|
|period|NOT_APPLICABLE|
|groups|NOT_APPLICABLE|
|main_indicators|材料、应用、发展方向|
|evidence_status|VERSION_UNCONFIRMED|
|recommended_sections|1.2.1（辅助线索）；1.2.2（分类线索）|
|citation_priority|HOLD_VERSION_RESOLUTION|
|limitations|VERSION_UNCONFIRMED：标题p1用“在”、页眉出现“对”；与LE22同作者、同主题、主体段落与参考文献高度相近，版本题录尚未闭环；安全/抗菌/普遍低失重断言不能照搬|
|read_scope|p1–2及p4，另与LE22正文/题录及参考文献比较；非被引原文精读|
|visual_pages||
|version_family|V01|
|in_chapter01|否|
|new_citation|暂不列完成正式引文；V01家族最多选一个经核版本|

### LE22｜海藻酸钠对果蔬保鲜的研究进展

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf](../海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE22|
|canonical_filename|海藻酸钠对果蔬保鲜的研究进展_梁昭榆.pdf|
|duplicate_files|NONE|
|sha256|7d9ffd1ad25f2020ef54dbe6653fd33b7ea58d82f818a64789607e0acdd577b1|
|file_size|834241|
|pdf_pages|5|
|title|海藻酸钠对果蔬保鲜的研究进展|
|authors|梁昭榆；卓琳；温建珊；陈晓莹；林慧仪；吴慧|
|year|2026（网络首发2026-01-19；收稿2025-08-15不是出版年）|
|journal|农产品加工，网络首发；卷期终页UNVERIFIED；CNKI urlid 14.1310.S.20260119.0957.010|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|综述（网络首发版）|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|多种果蔬研究综述|
|material|SA及复配膜|
|concentration|NOT_APPLICABLE|
|storage_conditions|NOT_APPLICABLE|
|period|NOT_APPLICABLE|
|groups|NOT_APPLICABLE|
|main_indicators|成膜/应用研究归纳|
|evidence_status|VERSION_UNCONFIRMED|
|recommended_sections|1.2.1（线索）；1.2.2（线索）|
|citation_priority|HOLD_VERSION_RESOLUTION|
|limitations|VERSION_UNCONFIRMED：与LE21字体/标题/引文序号变更但主体高度相近；未依据期次编号擅定最终发表信息；不得把综述引出的未上传论文冒充已读|
|read_scope|p1–3、5；正文与LE21作规范化文本比对及对应段落检查|
|visual_pages||
|version_family|V01|
|in_chapter01|否|
|new_citation|暂缓正式引用；与LE21合并为V01内容家族|

### LE23｜海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理

相关性理由：排除理由见限制与论点栏

原件：[海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf](../海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE23|
|canonical_filename|海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理_任武昂.pdf|
|duplicate_files|NONE|
|sha256|92afac99ce254b88546a54480634217ad6ada7c4cf87763d0cc664fb55c0b38a|
|file_size|1448754|
|pdf_pages|14|
|title|海藻酸钠诱导下厌氧氨氧化颗粒污泥快速培养及自凝聚强化机理|
|authors|任武昂；霍睿婕；池玉蕾；张彬鸿；陈智婷|
|year|2026|
|journal|中国环境科学，网络首发2026-10-09；最终卷期页码UNVERIFIED|
|doi|10.19674/j.cnki.issn1000-6923.20261009.008|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究（网络首发）|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|D|
|research_subject|厌氧氨氧化颗粒污泥/环境工程|
|material|海藻酸钠，但用途为污泥培养与凝聚|
|concentration|本题不抽取|
|storage_conditions|NOT_APPLICABLE（非果实贮藏）|
|period|NOT_APPLICABLE|
|groups|本题不抽取|
|main_indicators|污泥培养/自凝聚|
|evidence_status|EXCLUDED_WITH_REASON|
|recommended_sections|不分配|
|citation_priority|EXCLUDE|
|limitations|非食品对象及实验系统，禁止为20000字目标强引|
|read_scope|p1首发封面、p2题名/摘要|
|visual_pages||
|version_family|LE23|
|in_chapter01|否|
|new_citation|否|

### LE24｜空气负离子环境中草莓采后品质的变化

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[空气负离子环境中草莓采后品质的变化_范鹏.pdf](../空气负离子环境中草莓采后品质的变化_范鹏.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE24|
|canonical_filename|空气负离子环境中草莓采后品质的变化_范鹏.pdf|
|duplicate_files|NONE|
|sha256|c735e005609562535f83bce4a1ab3cf638caffbeabb35c8f77e5daf288f6dce1|
|file_size|2400692|
|pdf_pages|11|
|title|空气负离子环境中草莓采后品质的变化|
|authors|范鹏；李宇裕；黄泽雄；胡华宇|
|year|2026|
|journal|广西大学学报（自然科学版），51(4)：984–994|
|doi|10.13624/j.cnki.issn.1001-7445.2026.0984|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|完整草莓；负离子环境箱|
|material|空气负离子涂料/箱环境；非SA膜|
|concentration|0、1×10⁴、2×10⁴、3×10⁴ ions/cm³|
|storage_conditions|15℃、90%RH|
|period|4 d|
|groups|4种箱环境，每盘8果；独立箱数及箱效应UNVERIFIED|
|main_indicators|失重、硬度、TSS、TA、VC、总酚等|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1（指标辅助）；1.2.3；2.4.1；2.4.3；2.4.4；4.1；4.2|
|citation_priority|MEDIUM_METHOD_LOW_MECHANISM|
|limitations|非SA、15℃高湿、箱环境处理；不能直接推出钙交联机制；三仪器读数/盘内8果不能当独立箱；不采未经实测的“小分子团水”等解释|
|read_scope|p1–4题录/方法；p5–6相关结果/图注；其余酚类等不作本轮核心证据|
|visual_pages|5,6|
|version_family|LE24|
|in_chapter01|否|
|new_citation|优先方法定义和讨论的条件对照，非第一章必引|

### LE25｜脂肪酸对魔芋葡甘聚糖/海藻酸钠复合膜结构和性质的影响

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf](../脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE25|
|canonical_filename|脂肪酸对魔芋葡甘聚糖_海藻酸钠复合膜结构和性质的影响_汪秀妹.pdf|
|duplicate_files|NONE|
|sha256|e62021d88ed63646a67802aa433678f55ce9bbcab99ac71968498ca1ebde40d3|
|file_size|2948042|
|pdf_pages|14|
|title|脂肪酸对魔芋葡甘聚糖/海藻酸钠复合膜结构和性质的影响|
|authors|汪秀妹；谢倩芸；李璐璐；赵晓旭；庞杰|
|year|2026|
|journal|中国食品学报，26(7)：173–186|
|doi|10.16429/j.1009-7848.2026.07.015|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究（材料）|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|B|
|research_subject|独立流延膜；没有草莓保鲜实验|
|material|KGM；NaAlg；甘油；LA月桂酸；SA硬脂酸（本文SA不指海藻酸钠）|
|concentration|KGM/NaAlg液各20 g/L，混合体积3:1；LA 0.1–0.6%、硬脂酸0.02–0.12%（质量分数）；勿将0.08%SA写为海藻酸钠浓度|
|storage_conditions|NOT_APPLICABLE（无果实）；WVP测试25℃、90%RH，CaCl₂置杯底为干燥剂|
|period|材料测试周期，非贮藏保鲜天数|
|groups|KGM、NaAlg、KN与脂肪酸梯度复合膜|
|main_indicators|流变、结构、机械、WVP、水溶性|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.1；4.1；4.2|
|citation_priority|HIGH_MATERIAL_ONLY|
|limitations|没有果实实测；独立膜与果面涂层不同；SA缩写在此为硬脂酸；CaCl₂非涂膜交联；引用亲水性为材料证据，不拿水溶性数值预测SA-Ca果实失重|
|read_scope|p1–3材料/配方/测试；p10表2与结论；其他光谱图未逐图核读|
|visual_pages|10|
|version_family|LE25|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE26｜茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf](../茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE26|
|canonical_filename|茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究_李勇锋.pdf|
|duplicate_files|NONE|
|sha256|0aba23c944ac72f509bcd19ef4d506c2d7f1c46c4ec4b132fff6da7d626901a8|
|file_size|1852904|
|pdf_pages|7|
|title|茶多糖-海藻酸钠复合涂膜对草莓的保鲜效果研究|
|authors|李勇锋|
|year|2024|
|journal|绿色包装，2024(1)：20–26|
|doi|10.19362/j.cnki.cn10-1400/tb.2024.01.002|
|doi_status|PDF_PRINTED_NOT_EXTERNALLY_RESOLVED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整章姬草莓|
|material|茶多糖TPS；SA；预洗ClO₂|
|concentration|TPS 2 wt%；SA 0/1/2/3/4 wt%；预洗ClO₂ 20 mg/L 30 s；涂膜浸30 s|
|storage_conditions|4±0.5℃；RH UNVERIFIED|
|period|10 d；0、2、4、6、8、10 d|
|groups|CK；S0T2至S4T2；每组15盒，每盒300±5 g；重复测量3次不自动等同独立盒重复|
|main_indicators|失重、腐烂指数、硬度、SSC、TA、VC、MDA|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.2；1.2.3；2.4.2（定义反例）；4.1；4.2|
|citation_priority|HIGH_QUALITATIVE_WITH_ERROR_FLAGS|
|limitations|p3式(1)视觉确认缺少/m₀，不能用作失重公式；p3式(2)为0–3级加权腐烂指数而非二分类率；p5正文图5/6与SSC实际图4等错配；背景“呼吸跃变型”不采；不使用精确失重效应量|
|read_scope|p1–6相关材料/方法/结果/讨论；p3式1/2和p4图2/3已目视；p7参考文献非逐条精读|
|visual_pages|3,4|
|version_family|LE26|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE27｜茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究

相关性理由：直接涉及草莓与海藻酸盐/相关涂膜；相关性不等于全文结果已核

原件：[茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf](../茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE27|
|canonical_filename|茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究_季春艳.pdf|
|duplicate_files|NONE|
|sha256|2c130df5506a3646ca24f441ba1d2f371b1016fec4325109741d64bb60d1c7a1|
|file_size|990499|
|pdf_pages|5|
|title|茶多酚-海藻酸钠涂膜对草莓的保鲜效果研究|
|authors|季春艳；段梦晴；刘生杰；张乐乐；王小咪；贺荣；李双芳|
|year|2021|
|journal|滁州学院学报，23(5)；现有页2–5印刷4–7，起页及正式连续页码UNVERIFIED|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊原始研究|
|language|中文|
|completeness|APPARENTLY_COMPLETE|
|relevance_level|A|
|research_subject|完整草莓|
|material|SA；茶多酚；CaCl₂；柠檬酸；甘油；玉米油|
|concentration|SA 0.01 g/mL；茶多酚0/0.5/1.0/1.5%（基准UNVERIFIED）；甘油1.16%、玉米油0.025%；CaCl₂ 2%+柠檬酸1%交联液；浸液2 min再交联2 min|
|storage_conditions|4±0.5℃；RH UNVERIFIED；PE保鲜覆盖托盘|
|period|5 d，每日|
|groups|CK水处理；T0单SA配方；T1/2/3茶多酚梯度；每组3果/重复检测独立n未清楚|
|main_indicators|感官、VC、MDA、SSC、TA；无本轮可用失重测量结果|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.2.1；1.2.2；1.2.3；2.3；2.4.4；4.1；4.2|
|citation_priority|MEDIUM_PENDING_BIBLIOGRAPHY|
|limitations|首页文章编号2021)02-0001-04与23(5)/实际5页不一致，正式起止页及DOI待核；p3 MDA波长450/600写法问题不迁移；机制性抑菌解释不是果实实测；不以文献3果替本研究n|
|read_scope|p1–5题录/方法/相关结果/结论；p1和p5题录、p4图5已目视|
|visual_pages|1,4,5|
|version_family|LE27|
|in_chapter01|否|
|new_citation|建议按限定论点新增；不在本轮改正文|

### LE28｜草莓的涂膜保鲜研究

相关性理由：支持材料性质、草莓指标方法或条件差异；不能直接替代本实验

原件：[草莓的涂膜保鲜研究.pdf](../草莓的涂膜保鲜研究.pdf)

|字段（对应CSV）|值|
|---|---|
|literature_id|LE28|
|canonical_filename|草莓的涂膜保鲜研究.pdf|
|duplicate_files|NONE|
|sha256|61c82c555105dcce92813d7b49fb027361bf8242dc34f03e33466757ae83855f|
|file_size|205343|
|pdf_pages|4|
|title|草莓的涂膜保鲜研究|
|authors|张安宁；王鑫；陈洁|
|year|2006|
|journal|食品科学，27(3)；现有印刷231–234；文章编号0231-05提示可能5页，正式终页UNVERIFIED|
|doi|UNVERIFIED|
|doi_status|UNVERIFIED|
|type|期刊原始研究（现有PDF疑缺参考文献续页）|
|language|中文|
|completeness|POSSIBLY_INCOMPLETE|
|relevance_level|B|
|research_subject|完整草莓，丰收三号、八成熟|
|material|壳聚糖（不同分子量）；阿拉伯胶；乳化配方；山梨醇；VC；无SA|
|concentration|成膜剂1%等乳化体系；不同试验按各配方表，不混为单配方；细节见p2–4|
|storage_conditions|room temperature；数值℃/RH UNVERIFIED|
|period|本轮不统一给保质期限；不同子试验图分别读取|
|groups|不同成膜剂、保湿剂、抗氧化剂子试验；每组15果；独立容器结构UNVERIFIED|
|main_indicators|腐烂、失重、色差等|
|evidence_status|PRIMARY_RESULT_VERIFIED|
|recommended_sections|1.1；1.2.3；4.1；4.2（备选）|
|citation_priority|HOLD_COMPLETE_VERSION|
|limitations|现有4页末仅参考文献[1]而正文引至[8]，文章编号提示5页，POSSIBLY_INCOMPLETE；未确认缺失的具体页码不杜撰235；正式页码/完整版本未闭环前不作已完成正式引用|
|read_scope|p1–4现有正文/方法/结果/结论；p3、4相关图目视既有核验复用|
|visual_pages|3,4|
|version_family|LE28|
|in_chapter01|否|
|new_citation|原大纲L07，第一章未引用；暂缓正式新增，优先完整SA相关证据|
