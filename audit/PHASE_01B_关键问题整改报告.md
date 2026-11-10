# Phase 01B｜关键问题整改报告

项目：3368400039-cmd/strawberry-alginate-thesis
正式题目：《可食性海藻酸钠膜对草莓常温保鲜效果的研究》
审核日期：2026-11-10（UTC+8）｜定向整改，等待外部人工审核

## 1. 结论

**DQ01在独立派生副本中完成语法规范化及真实计算引擎核验；正式统计分析仍不放行。**

582处非规范公式全部规范化，原始S1保持不变。LibreOffice实际重算得到580个数值结果和2个空结果，与原缓存全部在绝对容差1e-7内一致；最大绝对差9.947598300641403e-14，属于本次比较的浮点舍入量级，没有发现超容差结果差异或计算错误。对重算副本又按Phase 01的独立算术规则复算，576个指标缓存校验无差异，首页6个规模缓存亦吻合。

研究者本轮解释了DEMO-01/02、独立容器、同组母液分装不复用、随机分配及定期轮换。上述解释改善了语义和设计可理解性，但属于**研究者陈述，DOCUMENTED_BUT_UNVERIFIED**；尚未提交实验日志、仪器原始导出、配液分装与随机化/轮换记录、IMG原图或完整SOP。不能因此认证全部数值来自实测或消除所有混杂，也不据缺证断言伪造。

当前候选数据结构可开展后续方法规划，但来源证据、实际实验单位和测量方法尚未达到正式统计推断准入。文件生成、自检、公式核验成功都不等于科研验收通过。没有进行显著性检验、正式实验结果图表或论文写作。

## 2. 版本与授权核对

开始时工作区干净，分支`audit/phase01-source-data`，HEAD为`177a561a401aa06ab3005b4bbb1149f1f04fa82e`。新建`audit/phase01b-provenance-formulas`，不修改main。

AGENTS.md仍描述Phase 01的旧交付范围；本次用户TASK 02是针对当前阶段整改的明确新授权，故仅新增本轮两份报告和一个经验证的派生副本，不改写AGENTS、项目档案或Phase 01报告，也不视为获准Phase 02。

四个必读文件均实际读取，并确认与上述提交中的Git对象逐字节一致：

|文件|SHA-256|
|---|---|
|AGENTS.md|`e31edd08b80445db35a9206d8d1e9cbee9bbb2b949b4d89b13c5cb6f75a2a636`|
|THESIS_PROFILE.md|`b9d018fb2db0e30dddbc5567bd867571242bc996fb69b5473217cb3d5d4bbfb2`|
|audit/PHASE_01_资料与数据可用性审核.md|`ffea0e32a253cc21019a45cc58b9ef5cb02499f1fad1dd7af18f7421b822ac54`|
|研究数据S1.xlsx|`7ffc712bbfd8648fbd359a3bf26e6af75af2a21fde7b7be801c862546d3cb550`|

S1哈希亦与Phase 01报告F31登记一致（以报告中实际文件名及SHA为定位，不以本轮重新编目替代）。本轮不重做PDF、学校模板或全仓库文献初审。只为确定是否新增来源证据检查文件路径及本地Git历史，不重新生成原始文件清单。

实际读取并采用`analyze-data-quality`的来源、粒度与关联核查，以及`validate-data`的局部计算核验。沿用Phase 01已读的Data index与交付约束；共同shared资源上轮不可访问的限制仍保留，未声称应用不可读指引。读取cloud-environment-runtime；工具为Python/openpyxl/lxml/zipfile/hashlib、Git和真实LibreOffice Calc。没有使用并不存在的专用论文审计技能，没有多人独立复核。

## 3. 来源定向核验（DQ02）

### 3.1 研究者本轮补充说明

以下内容由本轮对话提供，未写回原始Excel，也未把用户陈述升级为独立验证：

> “由我和同学进行实验得出 DEMO01指的是我进行操作 02指的是我同学和我一起的操作 该实验全程由老师指导 大部分都由我独自完成 部分程序有同学的协助”

> “54个处理单位各自配有独立容器；同组浸渍液统一配制为同一母液，分装至各个独立容器使用，不重复循环使用浸泡液。架位编号重复代表同一层放置多个独立容器；实验开展前完成容器随机分配，实验期间定期进行架位位置轮换，消除环境位置带来的系统误差，保证生物学重复的独立性。”

“消除系统误差、保证独立性”为研究者对设计的解释，本审计仅记录其所述做法，不能在无布局、时间和随机化记录时认证效果。

### 3.2 文件与Git证据

- `03_处理记录!L2:L55`原字段名为`protocol_version`，记录DEMO-01共38、DEMO-02共16。按新解释应理解为**操作参与模式编码**，不再凭“DEMO”字面猜测为模拟数据。但旧字段名及编码含义必须由码表/日志说明；本轮不改字段。
- DEMO-01覆盖CK13/Ca13/SA-Ca12单位；DEMO-02覆盖CK5/Ca5/SA-Ca6单位。这是人员标记分布的审核计数，不是处理效果。`K2:K55`均为OP-01，不能区分协作者实际参与的步骤、身份或时间。需提供操作步骤—参与人—记录映射；既不能自动认为两个SOP，也不能默认两种操作模式等效。
- 文件core属性creator为openpyxl，created/modified为2026-11-10 15:27:11（元数据时区未获确认）；仅证明文件整理属性，不能判断数字来源或认定生成数据。
- 可访问本地仓库非浅克隆，`git log --all -- ...`中S1仅在`8b710096f2ef6cd34ce4bede2aaa5ed4b7059056`以“Add files via upload”加入；没有更早的XLSX修改版本、早期演示工作簿、生成/替换脚本、CSV测量导出或实验日志。此结论限定当前本地可达历史和已提供文件，不推断其他电脑、未获取分支或被删除历史中不存在资料。
- 现有原始候选列是字面数值，未存为公式；派生列可通过公式定位。但“字面数值”不等于“来自仪器实测”。用户说明也不能单独证明全部候选读数真实。

### 3.3 七项核验结果

|核验事项|现有证据|结果/未核验部分|
|---|---|---|
|1 实验原始读数来源|用户称由本人及同学实测、老师指导；S1有记录与设备代码|DOCUMENTED_BUT_UNVERIFIED：缺原日志/设备导出及责任人核对|
|2 表格生成整理过程|文件元数据和一次Git上传|MISSING：谁在何软件整理、录入规则、修改履历及校对记录不明|
|3 日志与实际记录对应|unit/fruit/record内部编号及时间|MISSING：没有外部日志逐条对应，内部关联不能替代|
|4 DEMO真实含义|研究者本轮明确解释为独自/共同操作|DOCUMENTED_BUT_UNVERIFIED：语义已说明，需同日期日志/人员码表支持|
|5 从演示/生成数据继承|没有早期演示文件或脚本可比较|无法核验：不猜测“继承”或“未继承”|
|6 实测值是否替换旧值|无前后版本/替换映射|无法核验：不猜测已替换或未替换；也不要求从无到有编造比较文件|
|7 测量值与计算值区分|582公式可枚举；04 I/H、02 F、06 I等是字面值|VERIFIED仅限数据存储类型；其测量出处仍DOCUMENTED_BUT_UNVERIFIED|

没有比较文件，未实施所谓“模拟版对照结果”。若确有早期版本，后续须按unit/fruit/trait/day/repeat键、原始数值、公式及文件哈希比较，说明哪些保留、哪些替换、为何替换；若从未有过，书面说明“不存在”即可，不能杜撰一份早期文件充数。未修改来源描述来换取验收。

## 4. 公式存储、修复与真实重算（DQ01）

### 4.1 原始性质

`openpyxl data_type=f`读取582处为`==...`；OOXML工作表`f`元素文本以额外`=`开头，而通常OOXML公式体不含输入框前导等号。规范化规则为：仅对原始公式值删去**第一个**等号，`==IF(...)`变成`=IF(...)`；不替换其他比较运算符，不改变引用、条件、分母或统计口径，不处理字面字符串。

|工作表|位置|数量|
|---|---|---:|
|首页|B9:B14|6|
|04_质量变化|J2:J136，N2:N136|270|
|09_品质单元汇总|G2:J28，L2:M28|162|
|10_描述统计|C5:H19|90|
|11_品质汇总|C5:H13|54|
|合计|完整582条见附录B|582|

不能把582处非规范存储等同582个算术错误。本轮真实引擎补充了兼容性证据，更新了Phase 01中尚未实测的风险判断；旧报告作为阶段快照保留不改。

### 4.2 实际执行及失败诊断

1. 记录原始SHA，独立读取公式与原缓存。
2. 在`/tmp/phase01b/normalized/recalc_input.xlsx`内仅规范`f`文本，并**删除全部582个公式的v缓存**；源S1从未作为引擎输出目标。
3. 首次直接以此包结构加载LibreOffice失败，日志为`Error: source file could not be loaded`。随后简单独立工作簿`2×3`能由同一引擎得6，排除“仅有命令、无实际计算能力”的误判。不能单凭首次失败认定S1损坏或把原因归给等号。
4. 将临时规范化副本经openpyxl重新序列化为`reserialized.xlsx`，解决本次导入问题。对比原S1的所有非公式单元格：值变化0；156个值为None的空单元格存储类型发生`s→inlineStr`等序列化差异，无测量值改动。包结构导入失败的具体底层原因未完全定位，不能宣称“原始公式导致加载失败”。
5. 用独立用户配置目录和可写字体缓存运行真实引擎，成功输出XLSX；由于输入已删缓存，输出值不是简单保留旧缓存。成功日志明确`as a Calc document ... using filter : Calc MS Excel 2007 XML`。
6. 对582个引擎结果逐一与原缓存比对，核验公式数、错误类型、空值、非公式值、工作表顺序；再按Phase 01的独立算术核验代码重算副本。
7. 另做受控探针：保留双等号公式、删除缓存并同样重新序列化后交给同一Calc引擎。引擎能够容忍并规范化这些公式，输出无错误类型。因此**本次未证明原非规范公式在所有软件中会算错**，也不声称曾实际出现#NAME?。探针是已有数值/公式副本，不是模拟替代实验数据，不交付为研究数据。

真实引擎：`LibreOfficeDev 26.8.0.0.alpha0 2c87e51eeaa2b413ff4ae097b2705eea1995d8e5`。这是开发版本Calc，不是Microsoft Excel；已验证本文件的计算结果，不将它称为“Microsoft Excel认证”或跨版本普遍兼容性保证。

主要命令（均针对临时副本）：

```bash
XDG_CACHE_HOME=/tmp/phase01b/cache soffice   -env:UserInstallation=file:///tmp/phase01b/lo-roundtrip-profile   --headless --convert-to 'xlsx:Calc MS Excel 2007 XML'   --outdir /tmp/phase01b/recalculated   /tmp/phase01b/normalized/reserialized.xlsx
```

### 4.3 结果与交付副本

- 派生文件：`analysis/研究数据_公式修复核验副本.xlsx`。
- 派生SHA-256：`9167c63e20dc6f9d6a454981620644897a631c653f861309bb90d66da0f298f2`。
- 源SHA-256：`7ffc712bbfd8648fbd359a3bf26e6af75af2a21fde7b7be801c862546d3cb550`，本轮前后相同。
- 实际重算：582处；580数值、2空结果（04 J114/N114，对应漏测）。
- 绝对容差：1e-07；最大绝对差：9.947598300641403e-14；超容差差异：0；错误类型单元格：0；仍以双等号开头的公式：0。
- 非公式矩形单元格检查：21531个（含格式空白），值变化0；14个工作表名称与顺序未改变。

Calc导出会重新序列化样式、共享字符串、空单元格类型、公式表达及工作簿元数据，故本副本不是原件字节级复制。保真结论限定全部现有单元格逻辑值、公式数及已核验结果；未作视觉排版一致性保证。它是公式核验用派生文件，原件仍为唯一原始资料，不据派生软件元数据倒推实验日期。

本轮仅规范公式语法，保留DQ09的原有直接读数平均定义。对当前完整配对的技术重复，直接平均等于“先果再单位”；将来重复不平衡不能依赖此等价。

误差/差异清单：附录B完整列出582条原公式、对应缓存/实际重算值及差。没有超容差差异条目，但保留全部浮点差，不把近似相等写成逐位完全相同。本副本仅展示核验原汇总所必需的结果，不是正式论文结果表或显著性分析。

## 5. 图片引用核查（DQ03）

定位：04 L2:L136及05 M2:M784，共216个不同IMG-*引用。当前路径及已提供资料中没有对应IMG原始图像；仅有的两张PNG是Phase 01已确认的文献截图，本轮不重新做文献清点。引用编号可内部追踪到unit/day，不能替代照片本体、拍摄时间或腐烂判读证据。

研究者本轮没有说明这些图像是否实际拍摄、存储位置或能否找回，故状态MISSING。附录D列全216个引用及首个引用单元格，便于补交映射。照片缺失不单独证明读数虚假，但严重限制腐烂判定、成膜状态及异常事件复核。若本来未拍照，应明确IMG是预留标记并解释，不能事后重拍假充当时实验照。

## 6. 实验独立性定向复核（DQ04）

### 6.1 已核查与研究者解释

|事项|表内证据|本轮解释与审计边界|
|---|---|---|
|54候选单位|01 B/F各54个unit/container编码|研究者称每单位独立容器；物理实物、标签和空间记录未提供，DOCUMENTED_BUT_UNVERIFIED|
|配液/处理批次|01 G2:G55均为unit-PREP式唯一编码，03 A为TR-001等处理记录号|同组母液分装不循环。母液不是54份独立配制；PREP编号不能证明配方独立。03未有PREP到母液批次、分装批次的外部登记|
|重复rack_position|每批18单位仅12不同架位编码，18个重复编码各对应2容器；详附录C|研究者称架位代表同一层多容器，重复不再直接解释为位置冲突；仍缺层内具体位置/间距及时间变更|
|随机分配|01 I列只有静态编码|研究者称实验前随机分配，缺随机方法、分配表、执行日期及批次对应|
|轮换|表内无逐日位置历史|研究者称定期轮换，缺频率、时间、顺序、执行及偏离记录；不能认证已消除系统误差|
|果实嵌套|02 B/C及01 E|L每容器4果，D每容器3果，内部一致；189果不是189独立处理重复|
|连续/破坏性|L Day0—4同单位；D0/D2/D4独立容器到取样终点|时间和技术重复不扩充独立n；D每批×组×日仅1容器|

共享母液不会自动否定各分装容器对既定处理流程的独立施加，也不自动保证独立。若分装后各容器只使用各自浸泡液且没有交叉复用，容器可以成为候选实验单位；同一母液的配制误差仍是共享因素，不能把所有容器当独立配方制备重复。关键还取决于“同组”究竟指每个B批次分别配液，还是跨B1/B2/B3使用同一母液；该粒度尚未说明。须记录母液ID、配制日、储存、分装与unit映射，以及独立处理施加的实际流程，再判定可识别的变异层级。

### 6.2 当前统计单位判断

- L：每组9候选容器，跨3来源/日期批次，每批每组3容器；108颗L果嵌套于27容器。135质量记录、540 L果日均非独立重复数。
- D：每组每取样日3候选容器，来自3批次；每容器3果。81颗D果的243计划技术读数不能视为243独立样本。每批×组×日仅1个D容器，没有格内容器重复。
- 同组母液、同批环境、共架/轮换、操作参与模式均可能形成共享因素，不能只按标签唯一性认定完全独立。小批次数也不能自动保证功效或支持所有复杂随机效应模型。
- 没有SA单独臂，不能估计完整SA×Ca交互；SA-Ca对Ca只能解释在钙处理条件下加入SA流程的增量，对CK是复合流程差异，不是纯SA单因素效应。

现阶段判定：容器独立设计**有研究者解释支持但未形成外部证据链**，正式独立n尚未认证，不能据“54容器独立”一句话直接放行。配液分装、随机/轮换实际记录补齐后再定分析层级；本轮不拟合统计模型。

## 7. SOP缺口逐项核查（DQ10）

状态定义：VERIFIED=本轮在指定证据范围直接可复核；DOCUMENTED_BUT_UNVERIFIED=有工作簿或研究者说明、无实际操作佐证；MISSING=现资料未提供；NOT_APPLICABLE=该指标/情境确实不适用。字段有数值不使其方法自动VERIFIED。

|项目/组成|定位与现有内容|状态|最小缺口|
|---|---|---|---|
|1 草莓对象与成熟度记录|研究设定B5完整果；02 H有7/8/9成熟，I无表面损伤；01 J同批筛选果|DOCUMENTED_BUT_UNVERIFIED|采购/采收原记录、筛选操作记录；主观分级判据与人员|
|1 来源、品种、产地/采后时长|01 J未具体指明|MISSING|品种、供应来源/批号、购入采收时间与运输预处理|
|2 SA与CaCl₂标称用量|研究设定B11/B12及03 F/G：1.5%、1% w/w|DOCUMENTED_BUT_UNVERIFIED|实际称量与配液记录；不是证明称量已执行|
|2 材料规格|无厂家批号/级别/黏度或分子量、CaCl₂水合态及纯度|MISSING|标签/采购与批号，SA适用规格、钙盐形态和浓度质量基准|
|3 顺序/时长|研究设定B8:B14、03 H:J；浸渍1.8—2.3min，风干18—30min|DOCUMENTED_BUT_UNVERIFIED|起止时间定义、实际步骤日志；膜形成/沥液终点|
|3 母液与分装|本轮研究者称同组母液分装不复用|DOCUMENTED_BUT_UNVERIFIED|每批配液ID、配制日与配方质量、溶解温度/时间、混匀冷却、分装体积、液果比、容器映射、处置规则|
|4 贮藏实测与布局|07温湿度记录；01 I；研究者称独立容器/随机/轮换|DOCUMENTED_BUT_UNVERIFIED|传感器原始日志/校准，容器尺寸材质/盖膜通气、架位图及轮换时间表|
|5 基线/失重定义|12第20—22行：处理沥液后L单位Day0；04 H/I/J|DOCUMENTED_BUT_UNVERIFIED（测量）；VERIFIED（给定读数的计算）|天平型号精度/校准、皮重去除、基线时点与风干统一标准、称量操作记录|
|6 腐烂判据|12第24—26行“可见霉斑/软腐”，05事件及无移除标记|DOCUMENTED_BUT_UNVERIFIED|判据足够可复现的阈值/示例照片、观察员、盲法、首次时间/疑似状态及复核规则|
|7 硬度记录|06 H/J/K：firmness/N/TEXTURE-01，每果2读数|DOCUMENTED_BUT_UNVERIFIED|实际机型、测量模式、探头直径、速度、穿刺/压缩深度、去皮否、测点、校准及原始曲线|
|8 TSS记录|06 TSS/°Brix/REFRACT-01，每果1读数|DOCUMENTED_BUT_UNVERIFIED|仪器机型校准、温度补偿、取汁/混样与测点、清洗及实际导出/读数记录|
|8 TSS技术重复精度估计|该设计仅每果1次|NOT_APPLICABLE（重复间精度估计）|不能从单次读数估计同果技术重复精度；不代表仪器校准可省略|
|9 缺失和异常说明|08 DV-001—007；04/06空值；12保留原则|DOCUMENTED_BUT_UNVERIFIED|原始事件日志、发生/发现/录入时间、参与人及是否预定规则|
|9 终止/排除规则|有D0/D2/D4计划与L至Day4，未见正式SOP|MISSING（完整规则）|腐烂后保留/移除、无法检测阈值、意外终止/排除的预设原则与执行记录|

没有根据任何参考文献补写“实际做过”的操作。研究者关于老师指导的说明为人员背景陈述，不替代材料、仪器及流程记录。后续补证应优先已有同期原件；事后回忆必须注明回忆整理日期，不能冒充实验当天日志。

## 8. DQ05—DQ09影响统计解释的核查

|问题|本轮核验及定位|保留风险/处理边界|
|---|---|---|
|DQ05漏测|04 I114空、J114/N114原缓存与引擎均空；08 DV-005；10 Ca/Day2有效单位缓存8|不补0、不修改数值。说明漏测原因需原记录，后续按实际可观测单位定义|
|DQ06品质缺测|06 I107:I109为B2-CK-D4-F03，I239:I241为B3-SA-Ca-D4-F02；05对应第481、771行均visible=1、first=1|与腐坏说明内部吻合，不是真实性证明；无法检测与结局相关，不能默认随机缺失或代表全果均值|
|DQ06表述差异|同一果硬度标“过软”、TSS标“样品腐坏”，08同时说明两项不可测|属于可解释的指标状态文字差异，需日志确认，不随意统一改写|
|DQ07事件时间|08 B2在首日12:00即描述前期失重速度；DV-003追述沥液；DV-005 10:00而常规称量10:05|新研究者说明尚未解释这些时间；不能当预注册或当造假证明。补发生/发现/录入时间|
|DQ08批次范围事件|08 C5=B3-ALL不是unit；事件为B3湿度波动|内部关联规则应扩展到B3全18单位，不误删事件；原始表保持不变|
|DQ09技术重复折叠|79个有硬度读数的果，各有恰好2有效重复；其余2果双重复均缺失；09 G仅计repeat1，H直均有效读数|本数据下技术→果→单位与直均相等，独立复算已验证；未来不平衡时须显式两级平均/unique fruit计数，不把读数扩充n|

这里的核验只处理现有计算/映射，不制定正式缺失数据模型、不开展假设检验、不用显著性方向挑选样本。

## 9. 已解决、部分解决和未解决

|问题|状态|实际完成与剩余条件|
|---|---|---|
|DQ01|已解决（限交付派生副本计算核验）|582语法规范、真实引擎重算、结果/原始非公式值保留通过；源S1仍保持原存储；未认证所有Excel版本|
|DQ02|部分澄清、未闭环|DEMO有研究者解释；无同期日志/导出、整理链或早期比较材料，不能认证实测来源|
|DQ03|未解决|216引用清单定位完成；原图或预留标记说明未提供|
|DQ04|部分澄清、未认证|独立容器/母液分装/随机轮换有研究者陈述；缺操作证据及母液跨批范围|
|DQ10|未解决|9类方法逐项登记；材料与仪器关键参数、实际SOP仍缺|
|DQ05—09|内部核查完成，方法解释仍有条件|缺失未改，关联与折叠现时一致，事件时间及预设规则需补证|

## 10. 质量门槛与Phase 02准入

|门槛|结果|判定范围|
|---|---|---|
|GATE A 数据来源可追溯性|FAIL|内部编号和研究者说明存在，缺外部原始读数/整理链，不能认证全部数值的测量出处|
|GATE B 公式与计算正确性|PASS|仅本交付副本、本次Calc引擎和现有数据；582重算一致、独立算术吻合，不认证实验真实性|
|GATE C 实验独立性|CONDITIONAL PASS|研究者给出合理设计说明；物理单位、配液层级及随机轮换实际记录未独立核验，不满足正式推断放行条件|
|GATE D 测量方法可复现性|FAIL|关键材料/仪器/操作参数和同期执行证据仍缺|
|GATE E 主要研究指标可分析性|CONDITIONAL PASS|现有读数可按层级整理且计算可复现；来源、测量、信息性缺失和批次限制尚待解决|

**正式统计分析：维持不放行。** 先按《待补原始证据清单》补齐来源链、材料/方法及独立性关键证据，由外部审核者决定是否关闭问题。任何PASS均不代替整体科研验收。没有自动进入Phase 02。

## 11. 交付及自检

仅新增本轮授权文件：两份Markdown报告和`analysis/研究数据_公式修复核验副本.xlsx`。不改原始PDF、Excel、PNG、学校Word及先前交付；最终自检已逐一确认此前39个文件（36原始资料与3份Phase 01交付）SHA-256前后不变；递归路径差集恰为上述3个本轮授权文件，派生ZIP成员CRC通过，无额外测量单元格，附录B为582条、附录D为216条。分支安全提交/推送，不强推、不合并main、不发布云环境。

代码及引擎运行全部使用/tmp临时区；报告附录保存可检查规则，临时工作簿、日志、探针不加入Git。最终Commit SHA及真实GitHub链接由最终交付消息提供，避免提交中循环引用自身SHA。完成即停止并等待外部审核。

## 附录A｜可复现实跑代码与核验方法

运行前创建/tmp/phase01b；脚本输出均在临时区。最后派生文件来自验证成功的Calc输出，使用字节复制进入analysis，而非对源S1运行save。重现时软件元数据可能变化，不要求派生ZIP字节哈希相同，要求原件哈希不变、公式数/原始值与重算结果满足本报告规则。

### A1 原始公式登记、缓存删除与语法规范

```python
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree as E
from openpyxl import load_workbook
import json,hashlib
root=Path('/workspace/strawberry-alginate-thesis'); src=root/'研究数据S1.xlsx'
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
w=load_workbook(src);cache=load_workbook(src,data_only=True)
entries=[]
for sheet in w:
 for row in sheet:
  for c in row:
   if c.data_type=='f':
    assert c.value.startswith('==')
    entries.append({'sheet':sheet.title,'cell':c.coordinate,'original':c.value,'normalized':c.value[1:],'original_cache':cache[sheet.title][c.coordinate].value})
assert len(entries)==582
Path('/tmp/phase01b/formulas.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
for mode in ['normalized','malformed_probe']:
 target=Path('/tmp/phase01b')/mode;target.mkdir(exist_ok=True)
 count=0
 with ZipFile(src) as z,ZipFile(target/'recalc_input.xlsx','w',ZIP_DEFLATED) as out:
  for name in z.namelist():
   data=z.read(name)
   if name.startswith('xl/worksheets/') and name.endswith('.xml'):
    doc=E.fromstring(data)
    for c in doc.findall('.//s:c',ns):
     f=c.find('s:f',ns)
     if f is None:continue
     assert f.text.startswith('=')
     if mode=='normalized':f.text=f.text[1:]
     # delete every formula cache: final values must be engine-generated
     for val in c.findall('s:v',ns):c.remove(val)
     count+=1
    data=E.tostring(doc,encoding='UTF-8',xml_declaration=True,standalone=True)
   out.writestr(name,data)
 assert count==582
 print(mode,count,hashlib.sha256((target/'recalc_input.xlsx').read_bytes()).hexdigest())

```

### A2 导入兼容性处理与引擎命令

```python
from openpyxl import load_workbook
w = load_workbook("/tmp/phase01b/normalized/recalc_input.xlsx")
w.save("/tmp/phase01b/normalized/reserialized.xlsx")
```

创建`/tmp/phase01b/cache`和`/tmp/phase01b/recalculated`，然后执行第4.2节命令。检查退出码、成功转换日志及当前输出文件，不以旧文件或仅有进程判成功。

### A3 输出逐单元格验证

```python
from pathlib import Path
from openpyxl import load_workbook
from collections import Counter
import math,json,hashlib
R=Path('/workspace/strawberry-alginate-thesis');raw=R/'研究数据S1.xlsx';derived=Path('/tmp/phase01b/recalculated/reserialized.xlsx')
f=load_workbook(raw);nc=load_workbook(derived);vals=load_workbook(derived,data_only=True)
entries=json.load(open('/tmp/phase01b/formulas.json'));assert f.sheetnames==nc.sheetnames
nonformula_diffs=[];type_only=[];n=0
for s in f:
 for row in s:
  for c in row:
   d=nc[s.title][c.coordinate]
   if c.data_type=='f':continue
   n+=1
   if c.value!=d.value:nonformula_diffs.append([s.title,c.coordinate,str(c.value),str(d.value)])
   elif c.data_type!=d.data_type:type_only.append([s.title,c.coordinate,str(c.value),c.data_type,d.data_type])
assert not nonformula_diffs,nonformula_diffs[:10]
assert sum(c.data_type=='f' for s in nc for row in s for c in row)==582
assert not [(s.title,c.coordinate) for s in vals for row in s for c in row if c.data_type=='e']
assert not [(s.title,c.coordinate) for s in nc for row in s for c in row if c.data_type=='f' and c.value.startswith('==')]
maxdelta=0;numeric=blank=0;diffs=[]
for e in entries:
 c=vals[e['sheet']][e['cell']];a=e['original_cache'];b=c.value;e['engine_formula']=nc[e['sheet']][e['cell']].value;e['recalculated']=b
 if a in [None,''] and b in [None,'']:blank+=1;e['delta']=None;e['status']='PASS_EMPTY'
 elif isinstance(a,(int,float)) and isinstance(b,(int,float)) and math.isfinite(a) and math.isfinite(b):
  numeric+=1;e['delta']=b-a;maxdelta=max(maxdelta,abs(b-a));e['status']='PASS_NUMERIC' if abs(b-a)<=1e-7 else 'FAIL'
 else:e['status']='FAIL';e['delta']=None
 if e['status']=='FAIL':diffs.append(e)
assert not diffs
summary={'source_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'derived_sha256':hashlib.sha256(derived.read_bytes()).hexdigest(),'formula_count':len(entries),'numeric':numeric,'blank':blank,'max_abs_delta':maxdelta,'tolerance':1e-7,'nonformula_checked':n,'nonformula_value_differences':len(nonformula_diffs),'empty_type_only_changes':len(type_only),'sheet_order_unchanged':True,'formula_errors':0,'formula_counts':dict(Counter(e['sheet'] for e in entries))}
Path('/tmp/phase01b/verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));Path('/tmp/phase01b/results.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False,indent=2))

```

独立算术检查使用Phase 01报告附录A的原脚本，输入路径改为临时目录中的重算副本，其余ROUND_HALF_UP、逐果均值、单位等权及ddof=1规则保持不变；执行结果`cached arithmetic mismatch = 0`。它是复核既有公式的算术步骤，不是新的显著性分析。

## 附录B｜582处问题公式及重算差异完整清单

每条“规范规则”为原公式仅删除第一个等号；交付副本保存的是Calc输出公式。所有条目状态PASS表示本次比较通过，未声称原存储在所有引擎都报错。`∅`表示空结果，不是零。差定义=实际Calc重算−原缓存；未以显示舍入掩盖数值差。

|工作表!单元格|原始非规范公式（完整）|原缓存|实际Calc重算|差|状态|
|---|---|---:|---:|---:|---|
|首页!B9|`==COUNTA('01_实验单位'!$A$2:$A$55)`|54|54|0|PASS_NUMERIC|
|首页!B10|`==COUNTA('02_果实清单'!$A$2:$A$190)`|189|189|0|PASS_NUMERIC|
|首页!B11|`==COUNTA('04_质量变化'!$A$2:$A$136)`|135|135|0|PASS_NUMERIC|
|首页!B12|`==COUNTA('05_腐烂观察'!$A$2:$A$784)`|783|783|0|PASS_NUMERIC|
|首页!B13|`==COUNTA('06_品质检测'!$A$2:$A$244)`|243|243|0|PASS_NUMERIC|
|首页!B14|`==COUNTA('07_环境记录'!$A$2:$A$31)`|30|30|0|PASS_NUMERIC|
|04_质量变化!J2|`==IF(ISNUMBER(I2),ROUND((H2-I2)/H2*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N2|`==IF(ISNUMBER(J2),J2^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J3|`==IF(ISNUMBER(I3),ROUND((H3-I3)/H3*100,2),"")`|2.34|2.34|0.0|PASS_NUMERIC|
|04_质量变化!N3|`==IF(ISNUMBER(J3),J3^2,"")`|5.4756|5.4756|0.0|PASS_NUMERIC|
|04_质量变化!J4|`==IF(ISNUMBER(I4),ROUND((H4-I4)/H4*100,2),"")`|4.66|4.66|0.0|PASS_NUMERIC|
|04_质量变化!N4|`==IF(ISNUMBER(J4),J4^2,"")`|21.7156|21.7156|0.0|PASS_NUMERIC|
|04_质量变化!J5|`==IF(ISNUMBER(I5),ROUND((H5-I5)/H5*100,2),"")`|7.05|7.05|0.0|PASS_NUMERIC|
|04_质量变化!N5|`==IF(ISNUMBER(J5),J5^2,"")`|49.7025|49.7025|0.0|PASS_NUMERIC|
|04_质量变化!J6|`==IF(ISNUMBER(I6),ROUND((H6-I6)/H6*100,2),"")`|9.38|9.38|0.0|PASS_NUMERIC|
|04_质量变化!N6|`==IF(ISNUMBER(J6),J6^2,"")`|87.9844|87.9844|0.0|PASS_NUMERIC|
|04_质量变化!J7|`==IF(ISNUMBER(I7),ROUND((H7-I7)/H7*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N7|`==IF(ISNUMBER(J7),J7^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J8|`==IF(ISNUMBER(I8),ROUND((H8-I8)/H8*100,2),"")`|0.54|0.54|0.0|PASS_NUMERIC|
|04_质量变化!N8|`==IF(ISNUMBER(J8),J8^2,"")`|0.2916|0.2916|0.0|PASS_NUMERIC|
|04_质量变化!J9|`==IF(ISNUMBER(I9),ROUND((H9-I9)/H9*100,2),"")`|1.15|1.15|0.0|PASS_NUMERIC|
|04_质量变化!N9|`==IF(ISNUMBER(J9),J9^2,"")`|1.3225|1.3225|0.0|PASS_NUMERIC|
|04_质量变化!J10|`==IF(ISNUMBER(I10),ROUND((H10-I10)/H10*100,2),"")`|1.59|1.59|0.0|PASS_NUMERIC|
|04_质量变化!N10|`==IF(ISNUMBER(J10),J10^2,"")`|2.5281|2.5281|0.0|PASS_NUMERIC|
|04_质量变化!J11|`==IF(ISNUMBER(I11),ROUND((H11-I11)/H11*100,2),"")`|2.6|2.6|0.0|PASS_NUMERIC|
|04_质量变化!N11|`==IF(ISNUMBER(J11),J11^2,"")`|6.76|6.76|0.0|PASS_NUMERIC|
|04_质量变化!J12|`==IF(ISNUMBER(I12),ROUND((H12-I12)/H12*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N12|`==IF(ISNUMBER(J12),J12^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J13|`==IF(ISNUMBER(I13),ROUND((H13-I13)/H13*100,2),"")`|1.62|1.62|0.0|PASS_NUMERIC|
|04_质量变化!N13|`==IF(ISNUMBER(J13),J13^2,"")`|2.6244|2.6244|0.0|PASS_NUMERIC|
|04_质量变化!J14|`==IF(ISNUMBER(I14),ROUND((H14-I14)/H14*100,2),"")`|3.44|3.44|0.0|PASS_NUMERIC|
|04_质量变化!N14|`==IF(ISNUMBER(J14),J14^2,"")`|11.8336|11.8336|0.0|PASS_NUMERIC|
|04_质量变化!J15|`==IF(ISNUMBER(I15),ROUND((H15-I15)/H15*100,2),"")`|5.39|5.39|0.0|PASS_NUMERIC|
|04_质量变化!N15|`==IF(ISNUMBER(J15),J15^2,"")`|29.0521|29.0521|0.0|PASS_NUMERIC|
|04_质量变化!J16|`==IF(ISNUMBER(I16),ROUND((H16-I16)/H16*100,2),"")`|7.41|7.41|0.0|PASS_NUMERIC|
|04_质量变化!N16|`==IF(ISNUMBER(J16),J16^2,"")`|54.9081|54.9081|0.0|PASS_NUMERIC|
|04_质量变化!J17|`==IF(ISNUMBER(I17),ROUND((H17-I17)/H17*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N17|`==IF(ISNUMBER(J17),J17^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J18|`==IF(ISNUMBER(I18),ROUND((H18-I18)/H18*100,2),"")`|1.98|1.98|0.0|PASS_NUMERIC|
|04_质量变化!N18|`==IF(ISNUMBER(J18),J18^2,"")`|3.9204|3.9204|0.0|PASS_NUMERIC|
|04_质量变化!J19|`==IF(ISNUMBER(I19),ROUND((H19-I19)/H19*100,2),"")`|4.4|4.4|0.0|PASS_NUMERIC|
|04_质量变化!N19|`==IF(ISNUMBER(J19),J19^2,"")`|19.36|19.36|0.0|PASS_NUMERIC|
|04_质量变化!J20|`==IF(ISNUMBER(I20),ROUND((H20-I20)/H20*100,2),"")`|6.72|6.72|0.0|PASS_NUMERIC|
|04_质量变化!N20|`==IF(ISNUMBER(J20),J20^2,"")`|45.1584|45.1584|0.0|PASS_NUMERIC|
|04_质量变化!J21|`==IF(ISNUMBER(I21),ROUND((H21-I21)/H21*100,2),"")`|9.16|9.16|0.0|PASS_NUMERIC|
|04_质量变化!N21|`==IF(ISNUMBER(J21),J21^2,"")`|83.9056|83.9056|0.0|PASS_NUMERIC|
|04_质量变化!J22|`==IF(ISNUMBER(I22),ROUND((H22-I22)/H22*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N22|`==IF(ISNUMBER(J22),J22^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J23|`==IF(ISNUMBER(I23),ROUND((H23-I23)/H23*100,2),"")`|1.77|1.77|0.0|PASS_NUMERIC|
|04_质量变化!N23|`==IF(ISNUMBER(J23),J23^2,"")`|3.1329|3.1329|0.0|PASS_NUMERIC|
|04_质量变化!J24|`==IF(ISNUMBER(I24),ROUND((H24-I24)/H24*100,2),"")`|3.57|3.57|0.0|PASS_NUMERIC|
|04_质量变化!N24|`==IF(ISNUMBER(J24),J24^2,"")`|12.7449|12.7449|0.0|PASS_NUMERIC|
|04_质量变化!J25|`==IF(ISNUMBER(I25),ROUND((H25-I25)/H25*100,2),"")`|5.43|5.43|0.0|PASS_NUMERIC|
|04_质量变化!N25|`==IF(ISNUMBER(J25),J25^2,"")`|29.4849|29.4849|0.0|PASS_NUMERIC|
|04_质量变化!J26|`==IF(ISNUMBER(I26),ROUND((H26-I26)/H26*100,2),"")`|7.38|7.38|0.0|PASS_NUMERIC|
|04_质量变化!N26|`==IF(ISNUMBER(J26),J26^2,"")`|54.4644|54.4644|0.0|PASS_NUMERIC|
|04_质量变化!J27|`==IF(ISNUMBER(I27),ROUND((H27-I27)/H27*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N27|`==IF(ISNUMBER(J27),J27^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J28|`==IF(ISNUMBER(I28),ROUND((H28-I28)/H28*100,2),"")`|2.34|2.34|0.0|PASS_NUMERIC|
|04_质量变化!N28|`==IF(ISNUMBER(J28),J28^2,"")`|5.4756|5.4756|0.0|PASS_NUMERIC|
|04_质量变化!J29|`==IF(ISNUMBER(I29),ROUND((H29-I29)/H29*100,2),"")`|4.61|4.61|0.0|PASS_NUMERIC|
|04_质量变化!N29|`==IF(ISNUMBER(J29),J29^2,"")`|21.2521|21.2521|0.0|PASS_NUMERIC|
|04_质量变化!J30|`==IF(ISNUMBER(I30),ROUND((H30-I30)/H30*100,2),"")`|7|7|0|PASS_NUMERIC|
|04_质量变化!N30|`==IF(ISNUMBER(J30),J30^2,"")`|49|49|0|PASS_NUMERIC|
|04_质量变化!J31|`==IF(ISNUMBER(I31),ROUND((H31-I31)/H31*100,2),"")`|9.5|9.5|0.0|PASS_NUMERIC|
|04_质量变化!N31|`==IF(ISNUMBER(J31),J31^2,"")`|90.25|90.25|0.0|PASS_NUMERIC|
|04_质量变化!J32|`==IF(ISNUMBER(I32),ROUND((H32-I32)/H32*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N32|`==IF(ISNUMBER(J32),J32^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J33|`==IF(ISNUMBER(I33),ROUND((H33-I33)/H33*100,2),"")`|1.96|1.96|0.0|PASS_NUMERIC|
|04_质量变化!N33|`==IF(ISNUMBER(J33),J33^2,"")`|3.8416|3.8416|0.0|PASS_NUMERIC|
|04_质量变化!J34|`==IF(ISNUMBER(I34),ROUND((H34-I34)/H34*100,2),"")`|3.9|3.9|0.0|PASS_NUMERIC|
|04_质量变化!N34|`==IF(ISNUMBER(J34),J34^2,"")`|15.21|15.21|0.0|PASS_NUMERIC|
|04_质量变化!J35|`==IF(ISNUMBER(I35),ROUND((H35-I35)/H35*100,2),"")`|5.97|5.97|0.0|PASS_NUMERIC|
|04_质量变化!N35|`==IF(ISNUMBER(J35),J35^2,"")`|35.6409|35.6409|0.0|PASS_NUMERIC|
|04_质量变化!J36|`==IF(ISNUMBER(I36),ROUND((H36-I36)/H36*100,2),"")`|8.28|8.28|0.0|PASS_NUMERIC|
|04_质量变化!N36|`==IF(ISNUMBER(J36),J36^2,"")`|68.5584|68.5584|0.0|PASS_NUMERIC|
|04_质量变化!J37|`==IF(ISNUMBER(I37),ROUND((H37-I37)/H37*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N37|`==IF(ISNUMBER(J37),J37^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J38|`==IF(ISNUMBER(I38),ROUND((H38-I38)/H38*100,2),"")`|1.96|1.96|0.0|PASS_NUMERIC|
|04_质量变化!N38|`==IF(ISNUMBER(J38),J38^2,"")`|3.8416|3.8416|0.0|PASS_NUMERIC|
|04_质量变化!J39|`==IF(ISNUMBER(I39),ROUND((H39-I39)/H39*100,2),"")`|4.04|4.04|0.0|PASS_NUMERIC|
|04_质量变化!N39|`==IF(ISNUMBER(J39),J39^2,"")`|16.3216|16.3216|0.0|PASS_NUMERIC|
|04_质量变化!J40|`==IF(ISNUMBER(I40),ROUND((H40-I40)/H40*100,2),"")`|6.07|6.07|0.0|PASS_NUMERIC|
|04_质量变化!N40|`==IF(ISNUMBER(J40),J40^2,"")`|36.8449|36.8449|0.0|PASS_NUMERIC|
|04_质量变化!J41|`==IF(ISNUMBER(I41),ROUND((H41-I41)/H41*100,2),"")`|8.29|8.29|0.0|PASS_NUMERIC|
|04_质量变化!N41|`==IF(ISNUMBER(J41),J41^2,"")`|68.7241|68.7241|0.0|PASS_NUMERIC|
|04_质量变化!J42|`==IF(ISNUMBER(I42),ROUND((H42-I42)/H42*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N42|`==IF(ISNUMBER(J42),J42^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J43|`==IF(ISNUMBER(I43),ROUND((H43-I43)/H43*100,2),"")`|1.56|1.56|0.0|PASS_NUMERIC|
|04_质量变化!N43|`==IF(ISNUMBER(J43),J43^2,"")`|2.4336|2.4336|0.0|PASS_NUMERIC|
|04_质量变化!J44|`==IF(ISNUMBER(I44),ROUND((H44-I44)/H44*100,2),"")`|3.52|3.52|0.0|PASS_NUMERIC|
|04_质量变化!N44|`==IF(ISNUMBER(J44),J44^2,"")`|12.3904|12.3904|0.0|PASS_NUMERIC|
|04_质量变化!J45|`==IF(ISNUMBER(I45),ROUND((H45-I45)/H45*100,2),"")`|5.2|5.2|0.0|PASS_NUMERIC|
|04_质量变化!N45|`==IF(ISNUMBER(J45),J45^2,"")`|27.04|27.04|0.0|PASS_NUMERIC|
|04_质量变化!J46|`==IF(ISNUMBER(I46),ROUND((H46-I46)/H46*100,2),"")`|7.17|7.17|0.0|PASS_NUMERIC|
|04_质量变化!N46|`==IF(ISNUMBER(J46),J46^2,"")`|51.4089|51.4089|0.0|PASS_NUMERIC|
|04_质量变化!J47|`==IF(ISNUMBER(I47),ROUND((H47-I47)/H47*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N47|`==IF(ISNUMBER(J47),J47^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J48|`==IF(ISNUMBER(I48),ROUND((H48-I48)/H48*100,2),"")`|2.02|2.02|0.0|PASS_NUMERIC|
|04_质量变化!N48|`==IF(ISNUMBER(J48),J48^2,"")`|4.0804|4.0804|0.0|PASS_NUMERIC|
|04_质量变化!J49|`==IF(ISNUMBER(I49),ROUND((H49-I49)/H49*100,2),"")`|4.02|4.02|0.0|PASS_NUMERIC|
|04_质量变化!N49|`==IF(ISNUMBER(J49),J49^2,"")`|16.1604|16.1604|0.0|PASS_NUMERIC|
|04_质量变化!J50|`==IF(ISNUMBER(I50),ROUND((H50-I50)/H50*100,2),"")`|6|6|0|PASS_NUMERIC|
|04_质量变化!N50|`==IF(ISNUMBER(J50),J50^2,"")`|36|36|0|PASS_NUMERIC|
|04_质量变化!J51|`==IF(ISNUMBER(I51),ROUND((H51-I51)/H51*100,2),"")`|8.26|8.26|0.0|PASS_NUMERIC|
|04_质量变化!N51|`==IF(ISNUMBER(J51),J51^2,"")`|68.2276|68.2276|0.0|PASS_NUMERIC|
|04_质量变化!J52|`==IF(ISNUMBER(I52),ROUND((H52-I52)/H52*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N52|`==IF(ISNUMBER(J52),J52^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J53|`==IF(ISNUMBER(I53),ROUND((H53-I53)/H53*100,2),"")`|1.64|1.64|0.0|PASS_NUMERIC|
|04_质量变化!N53|`==IF(ISNUMBER(J53),J53^2,"")`|2.6896|2.6896|0.0|PASS_NUMERIC|
|04_质量变化!J54|`==IF(ISNUMBER(I54),ROUND((H54-I54)/H54*100,2),"")`|3.23|3.23|0.0|PASS_NUMERIC|
|04_质量变化!N54|`==IF(ISNUMBER(J54),J54^2,"")`|10.4329|10.4329|0.0|PASS_NUMERIC|
|04_质量变化!J55|`==IF(ISNUMBER(I55),ROUND((H55-I55)/H55*100,2),"")`|5.15|5.15|0.0|PASS_NUMERIC|
|04_质量变化!N55|`==IF(ISNUMBER(J55),J55^2,"")`|26.5225|26.5225|0.0|PASS_NUMERIC|
|04_质量变化!J56|`==IF(ISNUMBER(I56),ROUND((H56-I56)/H56*100,2),"")`|6.89|6.89|0.0|PASS_NUMERIC|
|04_质量变化!N56|`==IF(ISNUMBER(J56),J56^2,"")`|47.4721|47.4721|0.0|PASS_NUMERIC|
|04_质量变化!J57|`==IF(ISNUMBER(I57),ROUND((H57-I57)/H57*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N57|`==IF(ISNUMBER(J57),J57^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J58|`==IF(ISNUMBER(I58),ROUND((H58-I58)/H58*100,2),"")`|1.98|1.98|0.0|PASS_NUMERIC|
|04_质量变化!N58|`==IF(ISNUMBER(J58),J58^2,"")`|3.9204|3.9204|0.0|PASS_NUMERIC|
|04_质量变化!J59|`==IF(ISNUMBER(I59),ROUND((H59-I59)/H59*100,2),"")`|3.8|3.8|0.0|PASS_NUMERIC|
|04_质量变化!N59|`==IF(ISNUMBER(J59),J59^2,"")`|14.44|14.44|0.0|PASS_NUMERIC|
|04_质量变化!J60|`==IF(ISNUMBER(I60),ROUND((H60-I60)/H60*100,2),"")`|5.91|5.91|0.0|PASS_NUMERIC|
|04_质量变化!N60|`==IF(ISNUMBER(J60),J60^2,"")`|34.9281|34.9281|0.0|PASS_NUMERIC|
|04_质量变化!J61|`==IF(ISNUMBER(I61),ROUND((H61-I61)/H61*100,2),"")`|8.18|8.18|0.0|PASS_NUMERIC|
|04_质量变化!N61|`==IF(ISNUMBER(J61),J61^2,"")`|66.9124|66.9124|0.0|PASS_NUMERIC|
|04_质量变化!J62|`==IF(ISNUMBER(I62),ROUND((H62-I62)/H62*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N62|`==IF(ISNUMBER(J62),J62^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J63|`==IF(ISNUMBER(I63),ROUND((H63-I63)/H63*100,2),"")`|1.62|1.62|0.0|PASS_NUMERIC|
|04_质量变化!N63|`==IF(ISNUMBER(J63),J63^2,"")`|2.6244|2.6244|0.0|PASS_NUMERIC|
|04_质量变化!J64|`==IF(ISNUMBER(I64),ROUND((H64-I64)/H64*100,2),"")`|3.3|3.3|0.0|PASS_NUMERIC|
|04_质量变化!N64|`==IF(ISNUMBER(J64),J64^2,"")`|10.89|10.89|0.0|PASS_NUMERIC|
|04_质量变化!J65|`==IF(ISNUMBER(I65),ROUND((H65-I65)/H65*100,2),"")`|5.14|5.14|0.0|PASS_NUMERIC|
|04_质量变化!N65|`==IF(ISNUMBER(J65),J65^2,"")`|26.4196|26.4196|0.0|PASS_NUMERIC|
|04_质量变化!J66|`==IF(ISNUMBER(I66),ROUND((H66-I66)/H66*100,2),"")`|6.79|6.79|0.0|PASS_NUMERIC|
|04_质量变化!N66|`==IF(ISNUMBER(J66),J66^2,"")`|46.1041|46.1041|0.0|PASS_NUMERIC|
|04_质量变化!J67|`==IF(ISNUMBER(I67),ROUND((H67-I67)/H67*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N67|`==IF(ISNUMBER(J67),J67^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J68|`==IF(ISNUMBER(I68),ROUND((H68-I68)/H68*100,2),"")`|1.87|1.87|0.0|PASS_NUMERIC|
|04_质量变化!N68|`==IF(ISNUMBER(J68),J68^2,"")`|3.4969|3.4969|0.0|PASS_NUMERIC|
|04_质量变化!J69|`==IF(ISNUMBER(I69),ROUND((H69-I69)/H69*100,2),"")`|3.67|3.67|0.0|PASS_NUMERIC|
|04_质量变化!N69|`==IF(ISNUMBER(J69),J69^2,"")`|13.4689|13.4689|0.0|PASS_NUMERIC|
|04_质量变化!J70|`==IF(ISNUMBER(I70),ROUND((H70-I70)/H70*100,2),"")`|5.61|5.61|0.0|PASS_NUMERIC|
|04_质量变化!N70|`==IF(ISNUMBER(J70),J70^2,"")`|31.4721|31.4721|0.0|PASS_NUMERIC|
|04_质量变化!J71|`==IF(ISNUMBER(I71),ROUND((H71-I71)/H71*100,2),"")`|7.58|7.58|0.0|PASS_NUMERIC|
|04_质量变化!N71|`==IF(ISNUMBER(J71),J71^2,"")`|57.4564|57.4564|0.0|PASS_NUMERIC|
|04_质量变化!J72|`==IF(ISNUMBER(I72),ROUND((H72-I72)/H72*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N72|`==IF(ISNUMBER(J72),J72^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J73|`==IF(ISNUMBER(I73),ROUND((H73-I73)/H73*100,2),"")`|1.95|1.95|0.0|PASS_NUMERIC|
|04_质量变化!N73|`==IF(ISNUMBER(J73),J73^2,"")`|3.8025|3.8025|0.0|PASS_NUMERIC|
|04_质量变化!J74|`==IF(ISNUMBER(I74),ROUND((H74-I74)/H74*100,2),"")`|3.9|3.9|0.0|PASS_NUMERIC|
|04_质量变化!N74|`==IF(ISNUMBER(J74),J74^2,"")`|15.21|15.21|0.0|PASS_NUMERIC|
|04_质量变化!J75|`==IF(ISNUMBER(I75),ROUND((H75-I75)/H75*100,2),"")`|5.98|5.98|0.0|PASS_NUMERIC|
|04_质量变化!N75|`==IF(ISNUMBER(J75),J75^2,"")`|35.7604|35.7604|0.0|PASS_NUMERIC|
|04_质量变化!J76|`==IF(ISNUMBER(I76),ROUND((H76-I76)/H76*100,2),"")`|8.09|8.09|0.0|PASS_NUMERIC|
|04_质量变化!N76|`==IF(ISNUMBER(J76),J76^2,"")`|65.4481|65.4481|0.0|PASS_NUMERIC|
|04_质量变化!J77|`==IF(ISNUMBER(I77),ROUND((H77-I77)/H77*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N77|`==IF(ISNUMBER(J77),J77^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J78|`==IF(ISNUMBER(I78),ROUND((H78-I78)/H78*100,2),"")`|1.83|1.83|0.0|PASS_NUMERIC|
|04_质量变化!N78|`==IF(ISNUMBER(J78),J78^2,"")`|3.3489|3.3489|0.0|PASS_NUMERIC|
|04_质量变化!J79|`==IF(ISNUMBER(I79),ROUND((H79-I79)/H79*100,2),"")`|3.7|3.7|0.0|PASS_NUMERIC|
|04_质量变化!N79|`==IF(ISNUMBER(J79),J79^2,"")`|13.69|13.69|0.0|PASS_NUMERIC|
|04_质量变化!J80|`==IF(ISNUMBER(I80),ROUND((H80-I80)/H80*100,2),"")`|5.7|5.7|0.0|PASS_NUMERIC|
|04_质量变化!N80|`==IF(ISNUMBER(J80),J80^2,"")`|32.49|32.49|0.0|PASS_NUMERIC|
|04_质量变化!J81|`==IF(ISNUMBER(I81),ROUND((H81-I81)/H81*100,2),"")`|7.63|7.63|0.0|PASS_NUMERIC|
|04_质量变化!N81|`==IF(ISNUMBER(J81),J81^2,"")`|58.2169|58.2169|0.0|PASS_NUMERIC|
|04_质量变化!J82|`==IF(ISNUMBER(I82),ROUND((H82-I82)/H82*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N82|`==IF(ISNUMBER(J82),J82^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J83|`==IF(ISNUMBER(I83),ROUND((H83-I83)/H83*100,2),"")`|1.59|1.59|0.0|PASS_NUMERIC|
|04_质量变化!N83|`==IF(ISNUMBER(J83),J83^2,"")`|2.5281|2.5281|0.0|PASS_NUMERIC|
|04_质量变化!J84|`==IF(ISNUMBER(I84),ROUND((H84-I84)/H84*100,2),"")`|3.11|3.11|0.0|PASS_NUMERIC|
|04_质量变化!N84|`==IF(ISNUMBER(J84),J84^2,"")`|9.6721|9.6721|0.0|PASS_NUMERIC|
|04_质量变化!J85|`==IF(ISNUMBER(I85),ROUND((H85-I85)/H85*100,2),"")`|4.57|4.57|0.0|PASS_NUMERIC|
|04_质量变化!N85|`==IF(ISNUMBER(J85),J85^2,"")`|20.8849|20.8849|0.0|PASS_NUMERIC|
|04_质量变化!J86|`==IF(ISNUMBER(I86),ROUND((H86-I86)/H86*100,2),"")`|6.22|6.22|0.0|PASS_NUMERIC|
|04_质量变化!N86|`==IF(ISNUMBER(J86),J86^2,"")`|38.6884|38.6884|0.0|PASS_NUMERIC|
|04_质量变化!J87|`==IF(ISNUMBER(I87),ROUND((H87-I87)/H87*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N87|`==IF(ISNUMBER(J87),J87^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J88|`==IF(ISNUMBER(I88),ROUND((H88-I88)/H88*100,2),"")`|2.36|2.36|0.0|PASS_NUMERIC|
|04_质量变化!N88|`==IF(ISNUMBER(J88),J88^2,"")`|5.5696|5.5696|0.0|PASS_NUMERIC|
|04_质量变化!J89|`==IF(ISNUMBER(I89),ROUND((H89-I89)/H89*100,2),"")`|4.88|4.88|0.0|PASS_NUMERIC|
|04_质量变化!N89|`==IF(ISNUMBER(J89),J89^2,"")`|23.8144|23.8144|0.0|PASS_NUMERIC|
|04_质量变化!J90|`==IF(ISNUMBER(I90),ROUND((H90-I90)/H90*100,2),"")`|7.57|7.57|0.0|PASS_NUMERIC|
|04_质量变化!N90|`==IF(ISNUMBER(J90),J90^2,"")`|57.3049|57.3049|0.0|PASS_NUMERIC|
|04_质量变化!J91|`==IF(ISNUMBER(I91),ROUND((H91-I91)/H91*100,2),"")`|10.2|10.2|0.0|PASS_NUMERIC|
|04_质量变化!N91|`==IF(ISNUMBER(J91),J91^2,"")`|104.04|104.04|0.0|PASS_NUMERIC|
|04_质量变化!J92|`==IF(ISNUMBER(I92),ROUND((H92-I92)/H92*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N92|`==IF(ISNUMBER(J92),J92^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J93|`==IF(ISNUMBER(I93),ROUND((H93-I93)/H93*100,2),"")`|2.43|2.43|0.0|PASS_NUMERIC|
|04_质量变化!N93|`==IF(ISNUMBER(J93),J93^2,"")`|5.9049|5.9049|0.0|PASS_NUMERIC|
|04_质量变化!J94|`==IF(ISNUMBER(I94),ROUND((H94-I94)/H94*100,2),"")`|4.78|4.78|0.0|PASS_NUMERIC|
|04_质量变化!N94|`==IF(ISNUMBER(J94),J94^2,"")`|22.8484|22.8484|0.0|PASS_NUMERIC|
|04_质量变化!J95|`==IF(ISNUMBER(I95),ROUND((H95-I95)/H95*100,2),"")`|7.28|7.28|0.0|PASS_NUMERIC|
|04_质量变化!N95|`==IF(ISNUMBER(J95),J95^2,"")`|52.9984|52.9984|0.0|PASS_NUMERIC|
|04_质量变化!J96|`==IF(ISNUMBER(I96),ROUND((H96-I96)/H96*100,2),"")`|9.83|9.83|0.0|PASS_NUMERIC|
|04_质量变化!N96|`==IF(ISNUMBER(J96),J96^2,"")`|96.6289|96.6289|0.0|PASS_NUMERIC|
|04_质量变化!J97|`==IF(ISNUMBER(I97),ROUND((H97-I97)/H97*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N97|`==IF(ISNUMBER(J97),J97^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J98|`==IF(ISNUMBER(I98),ROUND((H98-I98)/H98*100,2),"")`|2.03|2.03|0.0|PASS_NUMERIC|
|04_质量变化!N98|`==IF(ISNUMBER(J98),J98^2,"")`|4.1209|4.1209|0.0|PASS_NUMERIC|
|04_质量变化!J99|`==IF(ISNUMBER(I99),ROUND((H99-I99)/H99*100,2),"")`|4.05|4.05|0.0|PASS_NUMERIC|
|04_质量变化!N99|`==IF(ISNUMBER(J99),J99^2,"")`|16.4025|16.4025|0.0|PASS_NUMERIC|
|04_质量变化!J100|`==IF(ISNUMBER(I100),ROUND((H100-I100)/H100*100,2),"")`|6.1|6.1|0.0|PASS_NUMERIC|
|04_质量变化!N100|`==IF(ISNUMBER(J100),J100^2,"")`|37.21|37.21|0.0|PASS_NUMERIC|
|04_质量变化!J101|`==IF(ISNUMBER(I101),ROUND((H101-I101)/H101*100,2),"")`|8.39|8.39|0.0|PASS_NUMERIC|
|04_质量变化!N101|`==IF(ISNUMBER(J101),J101^2,"")`|70.3921|70.3921|0.0|PASS_NUMERIC|
|04_质量变化!J102|`==IF(ISNUMBER(I102),ROUND((H102-I102)/H102*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N102|`==IF(ISNUMBER(J102),J102^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J103|`==IF(ISNUMBER(I103),ROUND((H103-I103)/H103*100,2),"")`|1.67|1.67|0.0|PASS_NUMERIC|
|04_质量变化!N103|`==IF(ISNUMBER(J103),J103^2,"")`|2.7889|2.7889|0.0|PASS_NUMERIC|
|04_质量变化!J104|`==IF(ISNUMBER(I104),ROUND((H104-I104)/H104*100,2),"")`|3.64|3.64|0.0|PASS_NUMERIC|
|04_质量变化!N104|`==IF(ISNUMBER(J104),J104^2,"")`|13.2496|13.2496|0.0|PASS_NUMERIC|
|04_质量变化!J105|`==IF(ISNUMBER(I105),ROUND((H105-I105)/H105*100,2),"")`|5.49|5.49|0.0|PASS_NUMERIC|
|04_质量变化!N105|`==IF(ISNUMBER(J105),J105^2,"")`|30.1401|30.1401|0.0|PASS_NUMERIC|
|04_质量变化!J106|`==IF(ISNUMBER(I106),ROUND((H106-I106)/H106*100,2),"")`|7.35|7.35|0.0|PASS_NUMERIC|
|04_质量变化!N106|`==IF(ISNUMBER(J106),J106^2,"")`|54.0225|54.0225|0.0|PASS_NUMERIC|
|04_质量变化!J107|`==IF(ISNUMBER(I107),ROUND((H107-I107)/H107*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N107|`==IF(ISNUMBER(J107),J107^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J108|`==IF(ISNUMBER(I108),ROUND((H108-I108)/H108*100,2),"")`|1.6|1.6|0.0|PASS_NUMERIC|
|04_质量变化!N108|`==IF(ISNUMBER(J108),J108^2,"")`|2.56|2.56|0.0|PASS_NUMERIC|
|04_质量变化!J109|`==IF(ISNUMBER(I109),ROUND((H109-I109)/H109*100,2),"")`|3.32|3.32|0.0|PASS_NUMERIC|
|04_质量变化!N109|`==IF(ISNUMBER(J109),J109^2,"")`|11.0224|11.0224|0.0|PASS_NUMERIC|
|04_质量变化!J110|`==IF(ISNUMBER(I110),ROUND((H110-I110)/H110*100,2),"")`|5.21|5.21|0.0|PASS_NUMERIC|
|04_质量变化!N110|`==IF(ISNUMBER(J110),J110^2,"")`|27.1441|27.1441|0.0|PASS_NUMERIC|
|04_质量变化!J111|`==IF(ISNUMBER(I111),ROUND((H111-I111)/H111*100,2),"")`|6.91|6.91|0.0|PASS_NUMERIC|
|04_质量变化!N111|`==IF(ISNUMBER(J111),J111^2,"")`|47.7481|47.7481|0.0|PASS_NUMERIC|
|04_质量变化!J112|`==IF(ISNUMBER(I112),ROUND((H112-I112)/H112*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N112|`==IF(ISNUMBER(J112),J112^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J113|`==IF(ISNUMBER(I113),ROUND((H113-I113)/H113*100,2),"")`|1.5|1.5|0.0|PASS_NUMERIC|
|04_质量变化!N113|`==IF(ISNUMBER(J113),J113^2,"")`|2.25|2.25|0.0|PASS_NUMERIC|
|04_质量变化!J114|`==IF(ISNUMBER(I114),ROUND((H114-I114)/H114*100,2),"")`|∅|∅|∅|PASS_EMPTY|
|04_质量变化!N114|`==IF(ISNUMBER(J114),J114^2,"")`|∅|∅|∅|PASS_EMPTY|
|04_质量变化!J115|`==IF(ISNUMBER(I115),ROUND((H115-I115)/H115*100,2),"")`|4.65|4.65|0.0|PASS_NUMERIC|
|04_质量变化!N115|`==IF(ISNUMBER(J115),J115^2,"")`|21.6225|21.6225|0.0|PASS_NUMERIC|
|04_质量变化!J116|`==IF(ISNUMBER(I116),ROUND((H116-I116)/H116*100,2),"")`|6.52|6.52|0.0|PASS_NUMERIC|
|04_质量变化!N116|`==IF(ISNUMBER(J116),J116^2,"")`|42.5104|42.5104|0.0|PASS_NUMERIC|
|04_质量变化!J117|`==IF(ISNUMBER(I117),ROUND((H117-I117)/H117*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N117|`==IF(ISNUMBER(J117),J117^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J118|`==IF(ISNUMBER(I118),ROUND((H118-I118)/H118*100,2),"")`|1.96|1.96|0.0|PASS_NUMERIC|
|04_质量变化!N118|`==IF(ISNUMBER(J118),J118^2,"")`|3.8416|3.8416|0.0|PASS_NUMERIC|
|04_质量变化!J119|`==IF(ISNUMBER(I119),ROUND((H119-I119)/H119*100,2),"")`|4.18|4.18|0.0|PASS_NUMERIC|
|04_质量变化!N119|`==IF(ISNUMBER(J119),J119^2,"")`|17.4724|17.4724|0.0|PASS_NUMERIC|
|04_质量变化!J120|`==IF(ISNUMBER(I120),ROUND((H120-I120)/H120*100,2),"")`|6.42|6.42|0.0|PASS_NUMERIC|
|04_质量变化!N120|`==IF(ISNUMBER(J120),J120^2,"")`|41.2164|41.2164|0.0|PASS_NUMERIC|
|04_质量变化!J121|`==IF(ISNUMBER(I121),ROUND((H121-I121)/H121*100,2),"")`|8.75|8.75|0.0|PASS_NUMERIC|
|04_质量变化!N121|`==IF(ISNUMBER(J121),J121^2,"")`|76.5625|76.5625|0.0|PASS_NUMERIC|
|04_质量变化!J122|`==IF(ISNUMBER(I122),ROUND((H122-I122)/H122*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N122|`==IF(ISNUMBER(J122),J122^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J123|`==IF(ISNUMBER(I123),ROUND((H123-I123)/H123*100,2),"")`|2.25|2.25|0.0|PASS_NUMERIC|
|04_质量变化!N123|`==IF(ISNUMBER(J123),J123^2,"")`|5.0625|5.0625|0.0|PASS_NUMERIC|
|04_质量变化!J124|`==IF(ISNUMBER(I124),ROUND((H124-I124)/H124*100,2),"")`|4.62|4.62|0.0|PASS_NUMERIC|
|04_质量变化!N124|`==IF(ISNUMBER(J124),J124^2,"")`|21.3444|21.3444|0.0|PASS_NUMERIC|
|04_质量变化!J125|`==IF(ISNUMBER(I125),ROUND((H125-I125)/H125*100,2),"")`|7.12|7.12|0.0|PASS_NUMERIC|
|04_质量变化!N125|`==IF(ISNUMBER(J125),J125^2,"")`|50.6944|50.6944|0.0|PASS_NUMERIC|
|04_质量变化!J126|`==IF(ISNUMBER(I126),ROUND((H126-I126)/H126*100,2),"")`|9.66|9.66|0.0|PASS_NUMERIC|
|04_质量变化!N126|`==IF(ISNUMBER(J126),J126^2,"")`|93.3156|93.3156|0.0|PASS_NUMERIC|
|04_质量变化!J127|`==IF(ISNUMBER(I127),ROUND((H127-I127)/H127*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N127|`==IF(ISNUMBER(J127),J127^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J128|`==IF(ISNUMBER(I128),ROUND((H128-I128)/H128*100,2),"")`|2.25|2.25|0.0|PASS_NUMERIC|
|04_质量变化!N128|`==IF(ISNUMBER(J128),J128^2,"")`|5.0625|5.0625|0.0|PASS_NUMERIC|
|04_质量变化!J129|`==IF(ISNUMBER(I129),ROUND((H129-I129)/H129*100,2),"")`|4.42|4.42|0.0|PASS_NUMERIC|
|04_质量变化!N129|`==IF(ISNUMBER(J129),J129^2,"")`|19.5364|19.5364|0.0|PASS_NUMERIC|
|04_质量变化!J130|`==IF(ISNUMBER(I130),ROUND((H130-I130)/H130*100,2),"")`|6.81|6.81|0.0|PASS_NUMERIC|
|04_质量变化!N130|`==IF(ISNUMBER(J130),J130^2,"")`|46.3761|46.3761|0.0|PASS_NUMERIC|
|04_质量变化!J131|`==IF(ISNUMBER(I131),ROUND((H131-I131)/H131*100,2),"")`|9.29|9.29|0.0|PASS_NUMERIC|
|04_质量变化!N131|`==IF(ISNUMBER(J131),J131^2,"")`|86.3041|86.3041|0.0|PASS_NUMERIC|
|04_质量变化!J132|`==IF(ISNUMBER(I132),ROUND((H132-I132)/H132*100,2),"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!N132|`==IF(ISNUMBER(J132),J132^2,"")`|0|0|0|PASS_NUMERIC|
|04_质量变化!J133|`==IF(ISNUMBER(I133),ROUND((H133-I133)/H133*100,2),"")`|1.63|1.63|0.0|PASS_NUMERIC|
|04_质量变化!N133|`==IF(ISNUMBER(J133),J133^2,"")`|2.6569|2.6569|0.0|PASS_NUMERIC|
|04_质量变化!J134|`==IF(ISNUMBER(I134),ROUND((H134-I134)/H134*100,2),"")`|3.44|3.44|0.0|PASS_NUMERIC|
|04_质量变化!N134|`==IF(ISNUMBER(J134),J134^2,"")`|11.8336|11.8336|0.0|PASS_NUMERIC|
|04_质量变化!J135|`==IF(ISNUMBER(I135),ROUND((H135-I135)/H135*100,2),"")`|5.11|5.11|0.0|PASS_NUMERIC|
|04_质量变化!N135|`==IF(ISNUMBER(J135),J135^2,"")`|26.1121|26.1121|0.0|PASS_NUMERIC|
|04_质量变化!J136|`==IF(ISNUMBER(I136),ROUND((H136-I136)/H136*100,2),"")`|7.17|7.17|0.0|PASS_NUMERIC|
|04_质量变化!N136|`==IF(ISNUMBER(J136),J136^2,"")`|51.4089|51.4089|0.0|PASS_NUMERIC|
|09_品质单元汇总!G2|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H2|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.86166666666667|8.86166666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I2|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J2|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A2,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.19666666666667|7.19666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L2|`==IF(ISNUMBER(H2),H2^2,"")`|78.5291361111111|78.5291361111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M2|`==IF(ISNUMBER(J2),J2^2,"")`|51.7920111111111|51.7920111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G3|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H3|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.895|7.895|0.0|PASS_NUMERIC|
|09_品质单元汇总!I3|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J3|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A3,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.92666666666667|7.92666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L3|`==IF(ISNUMBER(H3),H3^2,"")`|62.331025|62.331025|0.0|PASS_NUMERIC|
|09_品质单元汇总!M3|`==IF(ISNUMBER(J3),J3^2,"")`|62.8320444444445|62.8320444444445|0.0|PASS_NUMERIC|
|09_品质单元汇总!G4|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H4|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|4.16333333333333|4.16333333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!I4|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J4|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A4,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.64|8.64|0.0|PASS_NUMERIC|
|09_品质单元汇总!L4|`==IF(ISNUMBER(H4),H4^2,"")`|17.3333444444444|17.3333444444444|0.0|PASS_NUMERIC|
|09_品质单元汇总!M4|`==IF(ISNUMBER(J4),J4^2,"")`|74.6496|74.6496|0.0|PASS_NUMERIC|
|09_品质单元汇总!G5|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H5|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.835|9.835|0.0|PASS_NUMERIC|
|09_品质单元汇总!I5|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J5|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A5,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.93666666666667|7.93666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L5|`==IF(ISNUMBER(H5),H5^2,"")`|96.727225|96.727225|0.0|PASS_NUMERIC|
|09_品质单元汇总!M5|`==IF(ISNUMBER(J5),J5^2,"")`|62.9906777777778|62.9906777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!G6|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H6|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.28666666666667|7.28666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I6|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J6|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A6,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.69|7.69|0.0|PASS_NUMERIC|
|09_品质单元汇总!L6|`==IF(ISNUMBER(H6),H6^2,"")`|53.0955111111111|53.0955111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M6|`==IF(ISNUMBER(J6),J6^2,"")`|59.1361|59.1361|0.0|PASS_NUMERIC|
|09_品质单元汇总!G7|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H7|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|4.54666666666667|4.54666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I7|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J7|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A7,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.36666666666667|9.36666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L7|`==IF(ISNUMBER(H7),H7^2,"")`|20.6721777777778|20.6721777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!M7|`==IF(ISNUMBER(J7),J7^2,"")`|87.7344444444445|87.7344444444445|0.0|PASS_NUMERIC|
|09_品质单元汇总!G8|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H8|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.80666666666667|9.80666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I8|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J8|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A8,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.77666666666667|7.77666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L8|`==IF(ISNUMBER(H8),H8^2,"")`|96.1707111111111|96.1707111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M8|`==IF(ISNUMBER(J8),J8^2,"")`|60.4765444444445|60.4765444444444|-9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!G9|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H9|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.675|7.675|0.0|PASS_NUMERIC|
|09_品质单元汇总!I9|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J9|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A9,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.06666666666667|8.06666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L9|`==IF(ISNUMBER(H9),H9^2,"")`|58.905625|58.905625|0.0|PASS_NUMERIC|
|09_品质单元汇总!M9|`==IF(ISNUMBER(J9),J9^2,"")`|65.0711111111111|65.0711111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G10|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H10|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|5.3|5.3|0.0|PASS_NUMERIC|
|09_品质单元汇总!I10|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J10|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A10,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.1|8.1|0.0|PASS_NUMERIC|
|09_品质单元汇总!L10|`==IF(ISNUMBER(H10),H10^2,"")`|28.09|28.09|0.0|PASS_NUMERIC|
|09_品质单元汇总!M10|`==IF(ISNUMBER(J10),J10^2,"")`|65.61|65.61|0.0|PASS_NUMERIC|
|09_品质单元汇总!G11|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H11|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.28|9.28|0.0|PASS_NUMERIC|
|09_品质单元汇总!I11|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J11|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A11,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.27666666666667|8.27666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L11|`==IF(ISNUMBER(H11),H11^2,"")`|86.1184|86.1184|0.0|PASS_NUMERIC|
|09_品质单元汇总!M11|`==IF(ISNUMBER(J11),J11^2,"")`|68.5032111111111|68.5032111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G12|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H12|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.69833333333334|7.69833333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!I12|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J12|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A12,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.35333333333334|7.35333333333333|-9.769962616701378e-15|PASS_NUMERIC|
|09_品质单元汇总!L12|`==IF(ISNUMBER(H12),H12^2,"")`|59.2643361111111|59.2643361111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M12|`==IF(ISNUMBER(J12),J12^2,"")`|54.0715111111111|54.0715111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G13|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|2|2|0|PASS_NUMERIC|
|09_品质单元汇总!H13|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|5.74|5.74|0.0|PASS_NUMERIC|
|09_品质单元汇总!I13|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|2|2|0|PASS_NUMERIC|
|09_品质单元汇总!J13|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A13,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.96|7.96|0.0|PASS_NUMERIC|
|09_品质单元汇总!L13|`==IF(ISNUMBER(H13),H13^2,"")`|32.9476|32.9476|0.0|PASS_NUMERIC|
|09_品质单元汇总!M13|`==IF(ISNUMBER(J13),J13^2,"")`|63.3616|63.3616|0.0|PASS_NUMERIC|
|09_品质单元汇总!G14|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H14|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.36166666666667|9.36166666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I14|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J14|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A14,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.28|8.28|0.0|PASS_NUMERIC|
|09_品质单元汇总!L14|`==IF(ISNUMBER(H14),H14^2,"")`|87.6408027777778|87.6408027777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!M14|`==IF(ISNUMBER(J14),J14^2,"")`|68.5584|68.5584|0.0|PASS_NUMERIC|
|09_品质单元汇总!G15|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H15|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.83833333333334|8.83833333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!I15|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J15|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A15,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.19333333333334|8.19333333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!L15|`==IF(ISNUMBER(H15),H15^2,"")`|78.1161361111111|78.1161361111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M15|`==IF(ISNUMBER(J15),J15^2,"")`|67.1307111111111|67.1307111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G16|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H16|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|6.065|6.065|0.0|PASS_NUMERIC|
|09_品质单元汇总!I16|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J16|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A16,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.76666666666667|8.76666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L16|`==IF(ISNUMBER(H16),H16^2,"")`|36.784225|36.784225|0.0|PASS_NUMERIC|
|09_品质单元汇总!M16|`==IF(ISNUMBER(J16),J16^2,"")`|76.8544444444444|76.8544444444445|9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!G17|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H17|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.54166666666667|9.54166666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I17|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J17|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A17,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.53666666666667|7.53666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L17|`==IF(ISNUMBER(H17),H17^2,"")`|91.0434027777778|91.0434027777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!M17|`==IF(ISNUMBER(J17),J17^2,"")`|56.8013444444445|56.8013444444444|-9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!G18|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H18|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.53666666666667|8.53666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I18|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J18|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A18,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.83|7.83|0.0|PASS_NUMERIC|
|09_品质单元汇总!L18|`==IF(ISNUMBER(H18),H18^2,"")`|72.8746777777778|72.8746777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!M18|`==IF(ISNUMBER(J18),J18^2,"")`|61.3089|61.3089|0.0|PASS_NUMERIC|
|09_品质单元汇总!G19|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H19|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|4.95666666666667|4.95666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I19|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J19|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A19,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.71333333333334|8.71333333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!L19|`==IF(ISNUMBER(H19),H19^2,"")`|24.5685444444444|24.5685444444444|0.0|PASS_NUMERIC|
|09_品质单元汇总!M19|`==IF(ISNUMBER(J19),J19^2,"")`|75.9221777777778|75.9221777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!G20|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H20|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|9.51333333333334|9.51333333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!I20|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J20|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A20,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.62666666666667|8.62666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L20|`==IF(ISNUMBER(H20),H20^2,"")`|90.5035111111111|90.5035111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M20|`==IF(ISNUMBER(J20),J20^2,"")`|74.4193777777778|74.4193777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!G21|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H21|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.21|7.21|0.0|PASS_NUMERIC|
|09_品质单元汇总!I21|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J21|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A21,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.38333333333334|8.38333333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|09_品质单元汇总!L21|`==IF(ISNUMBER(H21),H21^2,"")`|51.9841|51.9841|0.0|PASS_NUMERIC|
|09_品质单元汇总!M21|`==IF(ISNUMBER(J21),J21^2,"")`|70.2802777777778|70.2802777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!G22|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H22|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|4.77833333333333|4.77833333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!I22|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J22|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A22,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.45666666666667|8.45666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L22|`==IF(ISNUMBER(H22),H22^2,"")`|22.8324694444445|22.8324694444444|-9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!M22|`==IF(ISNUMBER(J22),J22^2,"")`|71.5152111111111|71.5152111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!G23|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H23|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|11.4133333333333|11.4133333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!I23|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J23|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A23,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.75333333333334|8.75333333333333|-8.881784197001252e-15|PASS_NUMERIC|
|09_品质单元汇总!L23|`==IF(ISNUMBER(H23),H23^2,"")`|130.264177777778|130.264177777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!M23|`==IF(ISNUMBER(J23),J23^2,"")`|76.6208444444445|76.6208444444444|-9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!G24|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H24|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|6.74666666666667|6.74666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!I24|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J24|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A24,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.23333333333333|8.23333333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!L24|`==IF(ISNUMBER(H24),H24^2,"")`|45.5175111111111|45.5175111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M24|`==IF(ISNUMBER(J24),J24^2,"")`|67.7877777777778|67.7877777777778|0.0|PASS_NUMERIC|
|09_品质单元汇总!G25|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H25|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|4.74333333333333|4.74333333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!I25|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J25|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A25,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.05|8.05|0.0|PASS_NUMERIC|
|09_品质单元汇总!L25|`==IF(ISNUMBER(H25),H25^2,"")`|22.4992111111111|22.4992111111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M25|`==IF(ISNUMBER(J25),J25^2,"")`|64.8025|64.8025|0.0|PASS_NUMERIC|
|09_品质单元汇总!G26|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H26|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|10.0533333333333|10.0533333333333|0.0|PASS_NUMERIC|
|09_品质单元汇总!I26|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J26|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A26,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.72|8.72|0.0|PASS_NUMERIC|
|09_品质单元汇总!L26|`==IF(ISNUMBER(H26),H26^2,"")`|101.069511111111|101.069511111111|0.0|PASS_NUMERIC|
|09_品质单元汇总!M26|`==IF(ISNUMBER(J26),J26^2,"")`|76.0384|76.0384|0.0|PASS_NUMERIC|
|09_品质单元汇总!G27|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!H27|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|7.91|7.91|0.0|PASS_NUMERIC|
|09_品质单元汇总!I27|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|3|3|0|PASS_NUMERIC|
|09_品质单元汇总!J27|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A27,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.06666666666667|8.06666666666667|0.0|PASS_NUMERIC|
|09_品质单元汇总!L27|`==IF(ISNUMBER(H27),H27^2,"")`|62.5681|62.5681|0.0|PASS_NUMERIC|
|09_品质单元汇总!M27|`==IF(ISNUMBER(J27),J27^2,"")`|65.0711111111112|65.0711111111111|-9.947598300641403e-14|PASS_NUMERIC|
|09_品质单元汇总!G28|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效",'06_品质检测'!$L$2:$L$244,1)`|2|2|0|PASS_NUMERIC|
|09_品质单元汇总!H28|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"firmness",'06_品质检测'!$M$2:$M$244,"有效"),"")`|6.3575|6.3575|0.0|PASS_NUMERIC|
|09_品质单元汇总!I28|`==COUNTIFS('06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")`|2|2|0|PASS_NUMERIC|
|09_品质单元汇总!J28|`==IFERROR(SUMIFS('06_品质检测'!$I$2:$I$244,'06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效")/COUNTIFS('06_品质检测'!$E$2:$E$244,$A28,'06_品质检测'!$H$2:$H$244,"TSS",'06_品质检测'!$M$2:$M$244,"有效"),"")`|8.225|8.225|0.0|PASS_NUMERIC|
|09_品质单元汇总!L28|`==IF(ISNUMBER(H28),H28^2,"")`|40.41780625|40.41780625|0.0|PASS_NUMERIC|
|09_品质单元汇总!M28|`==IF(ISNUMBER(J28),J28^2,"")`|67.650625|67.650625|0.0|PASS_NUMERIC|
|10_描述统计!C5|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A5,'04_质量变化'!$C$2:$C$136,$B5,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D5|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A5,'04_质量变化'!$C$2:$C$136,$B5,'04_质量变化'!$K$2:$K$136,"有效")/C5,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!E5|`==IF(C5>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A5,'04_质量变化'!$C$2:$C$136,$B5,'04_质量变化'!$K$2:$K$136,"有效")-C5*D5^2)/(C5-1))),"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!F5|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A5,'05_腐烂观察'!$C$2:$C$784,$B5,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|0|0|0|PASS_NUMERIC|
|10_描述统计!G5|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A5,'05_腐烂观察'!$C$2:$C$784,$B5,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H5|`==IFERROR(100*F5/G5,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!C6|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A6,'04_质量变化'!$C$2:$C$136,$B6,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D6|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A6,'04_质量变化'!$C$2:$C$136,$B6,'04_质量变化'!$K$2:$K$136,"有效")/C6,"")`|1.80777777777778|1.80777777777778|0.0|PASS_NUMERIC|
|10_描述统计!E6|`==IF(C6>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A6,'04_质量变化'!$C$2:$C$136,$B6,'04_质量变化'!$K$2:$K$136,"有效")-C6*D6^2)/(C6-1))),"")`|0.557242715918697|0.557242715918696|-9.992007221626409e-16|PASS_NUMERIC|
|10_描述统计!F6|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A6,'05_腐烂观察'!$C$2:$C$784,$B6,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|1|1|0|PASS_NUMERIC|
|10_描述统计!G6|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A6,'05_腐烂观察'!$C$2:$C$784,$B6,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H6|`==IFERROR(100*F6/G6,"")`|2.77777777777778|2.77777777777778|0.0|PASS_NUMERIC|
|10_描述统计!C7|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A7,'04_质量变化'!$C$2:$C$136,$B7,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D7|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A7,'04_质量变化'!$C$2:$C$136,$B7,'04_质量变化'!$K$2:$K$136,"有效")/C7,"")`|3.64111111111111|3.64111111111111|0.0|PASS_NUMERIC|
|10_描述统计!E7|`==IF(C7>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A7,'04_质量变化'!$C$2:$C$136,$B7,'04_质量变化'!$K$2:$K$136,"有效")-C7*D7^2)/(C7-1))),"")`|1.06573266399745|1.06573266399746|9.992007221626409e-15|PASS_NUMERIC|
|10_描述统计!F7|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A7,'05_腐烂观察'!$C$2:$C$784,$B7,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|5|5|0|PASS_NUMERIC|
|10_描述统计!G7|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A7,'05_腐烂观察'!$C$2:$C$784,$B7,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H7|`==IFERROR(100*F7/G7,"")`|13.8888888888889|13.8888888888889|0.0|PASS_NUMERIC|
|10_描述统计!C8|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A8,'04_质量变化'!$C$2:$C$136,$B8,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D8|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A8,'04_质量变化'!$C$2:$C$136,$B8,'04_质量变化'!$K$2:$K$136,"有效")/C8,"")`|5.55111111111111|5.55111111111111|0.0|PASS_NUMERIC|
|10_描述统计!E8|`==IF(C8>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A8,'04_质量变化'!$C$2:$C$136,$B8,'04_质量变化'!$K$2:$K$136,"有效")-C8*D8^2)/(C8-1))),"")`|1.64879838400913|1.64879838400913|0.0|PASS_NUMERIC|
|10_描述统计!F8|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A8,'05_腐烂观察'!$C$2:$C$784,$B8,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|7|7|0|PASS_NUMERIC|
|10_描述统计!G8|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A8,'05_腐烂观察'!$C$2:$C$784,$B8,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H8|`==IFERROR(100*F8/G8,"")`|19.4444444444444|19.4444444444444|0.0|PASS_NUMERIC|
|10_描述统计!C9|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A9,'04_质量变化'!$C$2:$C$136,$B9,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D9|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A9,'04_质量变化'!$C$2:$C$136,$B9,'04_质量变化'!$K$2:$K$136,"有效")/C9,"")`|7.58777777777778|7.58777777777778|0.0|PASS_NUMERIC|
|10_描述统计!E9|`==IF(C9>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A9,'04_质量变化'!$C$2:$C$136,$B9,'04_质量变化'!$K$2:$K$136,"有效")-C9*D9^2)/(C9-1))),"")`|2.09579208044225|2.09579208044224|-1.021405182655144e-14|PASS_NUMERIC|
|10_描述统计!F9|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A9,'05_腐烂观察'!$C$2:$C$784,$B9,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|16|16|0|PASS_NUMERIC|
|10_描述统计!G9|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A9,'05_腐烂观察'!$C$2:$C$784,$B9,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H9|`==IFERROR(100*F9/G9,"")`|44.4444444444445|44.4444444444444|-9.947598300641403e-14|PASS_NUMERIC|
|10_描述统计!C10|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A10,'04_质量变化'!$C$2:$C$136,$B10,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D10|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A10,'04_质量变化'!$C$2:$C$136,$B10,'04_质量变化'!$K$2:$K$136,"有效")/C10,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!E10|`==IF(C10>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A10,'04_质量变化'!$C$2:$C$136,$B10,'04_质量变化'!$K$2:$K$136,"有效")-C10*D10^2)/(C10-1))),"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!F10|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A10,'05_腐烂观察'!$C$2:$C$784,$B10,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|0|0|0|PASS_NUMERIC|
|10_描述统计!G10|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A10,'05_腐烂观察'!$C$2:$C$784,$B10,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H10|`==IFERROR(100*F10/G10,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!C11|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A11,'04_质量变化'!$C$2:$C$136,$B11,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D11|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A11,'04_质量变化'!$C$2:$C$136,$B11,'04_质量变化'!$K$2:$K$136,"有效")/C11,"")`|1.84333333333333|1.84333333333333|0.0|PASS_NUMERIC|
|10_描述统计!E11|`==IF(C11>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A11,'04_质量变化'!$C$2:$C$136,$B11,'04_质量变化'!$K$2:$K$136,"有效")-C11*D11^2)/(C11-1))),"")`|0.255783111248574|0.255783111248574|0.0|PASS_NUMERIC|
|10_描述统计!F11|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A11,'05_腐烂观察'!$C$2:$C$784,$B11,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|0|0|0|PASS_NUMERIC|
|10_描述统计!G11|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A11,'05_腐烂观察'!$C$2:$C$784,$B11,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H11|`==IFERROR(100*F11/G11,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!C12|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A12,'04_质量变化'!$C$2:$C$136,$B12,'04_质量变化'!$K$2:$K$136,"有效")`|8|8|0|PASS_NUMERIC|
|10_描述统计!D12|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A12,'04_质量变化'!$C$2:$C$136,$B12,'04_质量变化'!$K$2:$K$136,"有效")/C12,"")`|3.86875|3.86875|0.0|PASS_NUMERIC|
|10_描述统计!E12|`==IF(C12>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A12,'04_质量变化'!$C$2:$C$136,$B12,'04_质量变化'!$K$2:$K$136,"有效")-C12*D12^2)/(C12-1))),"")`|0.490318773860432|0.490318773860436|3.9968028886505635e-15|PASS_NUMERIC|
|10_描述统计!F12|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A12,'05_腐烂观察'!$C$2:$C$784,$B12,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|0|0|0|PASS_NUMERIC|
|10_描述统计!G12|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A12,'05_腐烂观察'!$C$2:$C$784,$B12,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H12|`==IFERROR(100*F12/G12,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!C13|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A13,'04_质量变化'!$C$2:$C$136,$B13,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D13|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A13,'04_质量变化'!$C$2:$C$136,$B13,'04_质量变化'!$K$2:$K$136,"有效")/C13,"")`|5.79555555555556|5.79555555555556|0.0|PASS_NUMERIC|
|10_描述统计!E13|`==IF(C13>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A13,'04_质量变化'!$C$2:$C$136,$B13,'04_质量变化'!$K$2:$K$136,"有效")-C13*D13^2)/(C13-1))),"")`|0.789162706783452|0.789162706783448|-3.9968028886505635e-15|PASS_NUMERIC|
|10_描述统计!F13|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A13,'05_腐烂观察'!$C$2:$C$784,$B13,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|7|7|0|PASS_NUMERIC|
|10_描述统计!G13|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A13,'05_腐烂观察'!$C$2:$C$784,$B13,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H13|`==IFERROR(100*F13/G13,"")`|19.4444444444444|19.4444444444444|0.0|PASS_NUMERIC|
|10_描述统计!C14|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A14,'04_质量变化'!$C$2:$C$136,$B14,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D14|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A14,'04_质量变化'!$C$2:$C$136,$B14,'04_质量变化'!$K$2:$K$136,"有效")/C14,"")`|7.85333333333333|7.85333333333333|0.0|PASS_NUMERIC|
|10_描述统计!E14|`==IF(C14>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A14,'04_质量变化'!$C$2:$C$136,$B14,'04_质量变化'!$K$2:$K$136,"有效")-C14*D14^2)/(C14-1))),"")`|1.08258948821796|1.08258948821794|-1.9984014443252818e-14|PASS_NUMERIC|
|10_描述统计!F14|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A14,'05_腐烂观察'!$C$2:$C$784,$B14,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|12|12|0|PASS_NUMERIC|
|10_描述统计!G14|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A14,'05_腐烂观察'!$C$2:$C$784,$B14,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H14|`==IFERROR(100*F14/G14,"")`|33.3333333333333|33.3333333333333|0.0|PASS_NUMERIC|
|10_描述统计!C15|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A15,'04_质量变化'!$C$2:$C$136,$B15,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D15|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A15,'04_质量变化'!$C$2:$C$136,$B15,'04_质量变化'!$K$2:$K$136,"有效")/C15,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!E15|`==IF(C15>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A15,'04_质量变化'!$C$2:$C$136,$B15,'04_质量变化'!$K$2:$K$136,"有效")-C15*D15^2)/(C15-1))),"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!F15|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A15,'05_腐烂观察'!$C$2:$C$784,$B15,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|0|0|0|PASS_NUMERIC|
|10_描述统计!G15|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A15,'05_腐烂观察'!$C$2:$C$784,$B15,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H15|`==IFERROR(100*F15/G15,"")`|0|0|0|PASS_NUMERIC|
|10_描述统计!C16|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A16,'04_质量变化'!$C$2:$C$136,$B16,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D16|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A16,'04_质量变化'!$C$2:$C$136,$B16,'04_质量变化'!$K$2:$K$136,"有效")/C16,"")`|1.93222222222222|1.93222222222222|0.0|PASS_NUMERIC|
|10_描述统计!E16|`==IF(C16>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A16,'04_质量变化'!$C$2:$C$136,$B16,'04_质量变化'!$K$2:$K$136,"有效")-C16*D16^2)/(C16-1))),"")`|0.304949904811339|0.304949904811339|0.0|PASS_NUMERIC|
|10_描述统计!F16|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A16,'05_腐烂观察'!$C$2:$C$784,$B16,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|1|1|0|PASS_NUMERIC|
|10_描述统计!G16|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A16,'05_腐烂观察'!$C$2:$C$784,$B16,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H16|`==IFERROR(100*F16/G16,"")`|2.77777777777778|2.77777777777778|0.0|PASS_NUMERIC|
|10_描述统计!C17|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A17,'04_质量变化'!$C$2:$C$136,$B17,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D17|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A17,'04_质量变化'!$C$2:$C$136,$B17,'04_质量变化'!$K$2:$K$136,"有效")/C17,"")`|3.95888888888889|3.95888888888889|0.0|PASS_NUMERIC|
|10_描述统计!E17|`==IF(C17>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A17,'04_质量变化'!$C$2:$C$136,$B17,'04_质量变化'!$K$2:$K$136,"有效")-C17*D17^2)/(C17-1))),"")`|0.587121036168115|0.587121036168103|-1.199040866595169e-14|PASS_NUMERIC|
|10_描述统计!F17|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A17,'05_腐烂观察'!$C$2:$C$784,$B17,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|2|2|0|PASS_NUMERIC|
|10_描述统计!G17|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A17,'05_腐烂观察'!$C$2:$C$784,$B17,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H17|`==IFERROR(100*F17/G17,"")`|5.55555555555556|5.55555555555556|0.0|PASS_NUMERIC|
|10_描述统计!C18|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A18,'04_质量变化'!$C$2:$C$136,$B18,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D18|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A18,'04_质量变化'!$C$2:$C$136,$B18,'04_质量变化'!$K$2:$K$136,"有效")/C18,"")`|6.01333333333333|6.01333333333333|0.0|PASS_NUMERIC|
|10_描述统计!E18|`==IF(C18>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A18,'04_质量变化'!$C$2:$C$136,$B18,'04_质量变化'!$K$2:$K$136,"有效")-C18*D18^2)/(C18-1))),"")`|0.996656911880921|0.99665691188091|-1.099120794378905e-14|PASS_NUMERIC|
|10_描述统计!F18|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A18,'05_腐烂观察'!$C$2:$C$784,$B18,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|5|5|0|PASS_NUMERIC|
|10_描述统计!G18|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A18,'05_腐烂观察'!$C$2:$C$784,$B18,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H18|`==IFERROR(100*F18/G18,"")`|13.8888888888889|13.8888888888889|0.0|PASS_NUMERIC|
|10_描述统计!C19|`==COUNTIFS('04_质量变化'!$F$2:$F$136,$A19,'04_质量变化'!$C$2:$C$136,$B19,'04_质量变化'!$K$2:$K$136,"有效")`|9|9|0|PASS_NUMERIC|
|10_描述统计!D19|`==IFERROR(SUMIFS('04_质量变化'!$J$2:$J$136,'04_质量变化'!$F$2:$F$136,$A19,'04_质量变化'!$C$2:$C$136,$B19,'04_质量变化'!$K$2:$K$136,"有效")/C19,"")`|8.21222222222223|8.21222222222222|-1.0658141036401503e-14|PASS_NUMERIC|
|10_描述统计!E19|`==IF(C19>1,SQRT(MAX(0,(SUMIFS('04_质量变化'!$N$2:$N$136,'04_质量变化'!$F$2:$F$136,$A19,'04_质量变化'!$C$2:$C$136,$B19,'04_质量变化'!$K$2:$K$136,"有效")-C19*D19^2)/(C19-1))),"")`|1.30862311015984|1.30862311015986|1.9984014443252818e-14|PASS_NUMERIC|
|10_描述统计!F19|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A19,'05_腐烂观察'!$C$2:$C$784,$B19,'05_腐烂观察'!$H$2:$H$784,"L",'05_腐烂观察'!$I$2:$I$784,1)`|15|15|0|PASS_NUMERIC|
|10_描述统计!G19|`==COUNTIFS('05_腐烂观察'!$G$2:$G$784,$A19,'05_腐烂观察'!$C$2:$C$784,$B19,'05_腐烂观察'!$H$2:$H$784,"L")`|36|36|0|PASS_NUMERIC|
|10_描述统计!H19|`==IFERROR(100*F19/G19,"")`|41.6666666666667|41.6666666666667|0.0|PASS_NUMERIC|
|11_品质汇总!C5|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D5|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5)/C5,"")`|9.21833333333334|9.21833333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|11_品质汇总!E5|`==IF(C5>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5)-C5*D5^2)/(C5-1))),"")`|0.330180926833217|0.330180926833217|0.0|PASS_NUMERIC|
|11_品质汇总!F5|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G5|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5)/F5,"")`|8.03333333333334|8.03333333333333|-1.0658141036401503e-14|PASS_NUMERIC|
|11_品质汇总!H5|`==IF(F5>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A5,'09_品质单元汇总'!$E$2:$E$28,$B5)-F5*G5^2)/(F5-1))),"")`|0.745408165593391|0.745408165593391|0.0|PASS_NUMERIC|
|11_品质汇总!C6|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D6|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6)/C6,"")`|7.60111111111111|7.60111111111111|0.0|PASS_NUMERIC|
|11_品质汇总!E6|`==IF(C6>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6)-C6*D6^2)/(C6-1))),"")`|0.352697278654607|0.352697278654587|-1.9984014443252818e-14|PASS_NUMERIC|
|11_品质汇总!F6|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G6|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6)/F6,"")`|7.88777777777778|7.88777777777778|0.0|PASS_NUMERIC|
|11_品质汇总!H6|`==IF(F6>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A6,'09_品质单元汇总'!$E$2:$E$28,$B6)-F6*G6^2)/(F6-1))),"")`|0.516100047722591|0.516100047722591|0.0|PASS_NUMERIC|
|11_品质汇总!C7|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D7|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7)/C7,"")`|4.89388888888889|4.89388888888889|0.0|PASS_NUMERIC|
|11_品质汇总!E7|`==IF(C7>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7)-C7*D7^2)/(C7-1))),"")`|0.794659838710418|0.794659838710409|-8.992806499463768e-15|PASS_NUMERIC|
|11_品质汇总!F7|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G7|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7)/F7,"")`|8.35222222222222|8.35222222222222|0.0|PASS_NUMERIC|
|11_品质汇总!H7|`==IF(F7>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A7,'09_品质单元汇总'!$E$2:$E$28,$B7)-F7*G7^2)/(F7-1))),"")`|0.351825924970677|0.351825924970697|1.9984014443252818e-14|PASS_NUMERIC|
|11_品质汇总!C8|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D8|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8)/C8,"")`|10.2033333333333|10.2033333333333|0.0|PASS_NUMERIC|
|11_品质汇总!E8|`==IF(C8>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8)-C8*D8^2)/(C8-1))),"")`|1.07428399928096|1.07428399928098|1.9984014443252818e-14|PASS_NUMERIC|
|11_品质汇总!F8|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G8|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8)/F8,"")`|8.32333333333334|8.32333333333333|-8.881784197001252e-15|PASS_NUMERIC|
|11_品质汇总!H8|`==IF(F8>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A8,'09_品质单元汇总'!$E$2:$E$28,$B8)-F8*G8^2)/(F8-1))),"")`|0.410054196959927|0.41005419695991|-1.6986412276764895e-14|PASS_NUMERIC|
|11_品质汇总!C9|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D9|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9)/C9,"")`|7.62388888888889|7.62388888888889|0.0|PASS_NUMERIC|
|11_品质汇总!E9|`==IF(C9>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9)-C9*D9^2)/(C9-1))),"")`|1.08584367267184|1.08584367267184|0.0|PASS_NUMERIC|
|11_品质汇总!F9|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G9|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9)/F9,"")`|8.03888888888889|8.03888888888889|0.0|PASS_NUMERIC|
|11_品质汇总!H9|`==IF(F9>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A9,'09_品质单元汇总'!$E$2:$E$28,$B9)-F9*G9^2)/(F9-1))),"")`|0.3028078476403|0.3028078476403|0.0|PASS_NUMERIC|
|11_品质汇总!C10|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D10|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10)/C10,"")`|5.11833333333333|5.11833333333333|0.0|PASS_NUMERIC|
|11_品质汇总!E10|`==IF(C10>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10)-C10*D10^2)/(C10-1))),"")`|0.825713496182413|0.825713496182412|-9.992007221626409e-16|PASS_NUMERIC|
|11_品质汇总!F10|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G10|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10)/F10,"")`|8.72777777777778|8.72777777777778|0.0|PASS_NUMERIC|
|11_品质汇总!H10|`==IF(F10>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A10,'09_品质单元汇总'!$E$2:$E$28,$B10)-F10*G10^2)/(F10-1))),"")`|0.659194233164304|0.659194233164271|-3.3084646133829665e-14|PASS_NUMERIC|
|11_品质汇总!C11|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D11|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11)/C11,"")`|9.80055555555556|9.80055555555556|0.0|PASS_NUMERIC|
|11_品质汇总!E11|`==IF(C11>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11)-C11*D11^2)/(C11-1))),"")`|0.255888068701428|0.255888068701372|-5.601075159233915e-14|PASS_NUMERIC|
|11_品质汇总!F11|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G11|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11)/F11,"")`|8.01111111111111|8.01111111111111|0.0|PASS_NUMERIC|
|11_品质汇总!H11|`==IF(F11>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A11,'09_品质单元汇总'!$E$2:$E$28,$B11)-F11*G11^2)/(F11-1))),"")`|0.625533846080763|0.625533846080774|1.099120794378905e-14|PASS_NUMERIC|
|11_品质汇总!C12|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D12|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12)/C12,"")`|8.04055555555556|8.04055555555556|0.0|PASS_NUMERIC|
|11_品质汇总!E12|`==IF(C12>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12)-C12*D12^2)/(C12-1))),"")`|0.445422188407738|0.445422188407738|0.0|PASS_NUMERIC|
|11_品质汇总!F12|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G12|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12)/F12,"")`|7.98777777777778|7.98777777777778|0.0|PASS_NUMERIC|
|11_品质汇总!H12|`==IF(F12>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A12,'09_品质单元汇总'!$E$2:$E$28,$B12)-F12*G12^2)/(F12-1))),"")`|0.136639563708116|0.136639563708168|5.1986193128072955e-14|PASS_NUMERIC|
|11_品质汇总!C13|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13,'09_品质单元汇总'!$H$2:$H$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!D13|`==IFERROR(SUMIFS('09_品质单元汇总'!$H$2:$H$28,'09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13)/C13,"")`|5.53805555555556|5.53805555555556|0.0|PASS_NUMERIC|
|11_品质汇总!E13|`==IF(C13>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$L$2:$L$28,'09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13)-C13*D13^2)/(C13-1))),"")`|0.730127620757219|0.730127620757219|0.0|PASS_NUMERIC|
|11_品质汇总!F13|`==COUNTIFS('09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13,'09_品质单元汇总'!$J$2:$J$28,">0")`|3|3|0|PASS_NUMERIC|
|11_品质汇总!G13|`==IFERROR(SUMIFS('09_品质单元汇总'!$J$2:$J$28,'09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13)/F13,"")`|8.34611111111111|8.34611111111111|0.0|PASS_NUMERIC|
|11_品质汇总!H13|`==IF(F13>1,SQRT(MAX(0,(SUMIFS('09_品质单元汇总'!$M$2:$M$28,'09_品质单元汇总'!$C$2:$C$28,$A13,'09_品质单元汇总'!$E$2:$E$28,$B13)-F13*G13^2)/(F13-1))),"")`|0.324107035360749|0.324107035360749|0.0|PASS_NUMERIC|

## 附录C｜重复架位的单位映射

以下为所有18个重复编码，均为每码2容器；研究者解释为同层多容器，尚缺层内位置图与轮换记录。

|rack_position|unit_id与原表行|
|---|---|
|B1-R08|B1-CK-L1（01第2行）；B1-SA-Ca-L1（01第14行）|
|B1-R03|B1-CK-L2（01第3行）；B1-SA-Ca-L2（01第15行）|
|B1-R10|B1-CK-L3（01第4行）；B1-SA-Ca-L3（01第16行）|
|B1-R05|B1-CK-D0（01第5行）；B1-SA-Ca-D0（01第17行）|
|B1-R12|B1-CK-D2（01第6行）；B1-SA-Ca-D2（01第18行）|
|B1-R07|B1-CK-D4（01第7行）；B1-SA-Ca-D4（01第19行）|
|B2-R02|B2-CK-L1（01第20行）；B2-SA-Ca-L1（01第32行）|
|B2-R09|B2-CK-L2（01第21行）；B2-SA-Ca-L2（01第33行）|
|B2-R04|B2-CK-L3（01第22行）；B2-SA-Ca-L3（01第34行）|
|B2-R11|B2-CK-D0（01第23行）；B2-SA-Ca-D0（01第35行）|
|B2-R06|B2-CK-D2（01第24行）；B2-SA-Ca-D2（01第36行）|
|B2-R01|B2-CK-D4（01第25行）；B2-SA-Ca-D4（01第37行）|
|B3-R08|B3-CK-L1（01第38行）；B3-SA-Ca-L1（01第50行）|
|B3-R03|B3-CK-L2（01第39行）；B3-SA-Ca-L2（01第51行）|
|B3-R10|B3-CK-L3（01第40行）；B3-SA-Ca-L3（01第52行）|
|B3-R05|B3-CK-D0（01第41行）；B3-SA-Ca-D0（01第53行）|
|B3-R12|B3-CK-D2（01第42行）；B3-SA-Ca-D2（01第54行）|
|B3-R07|B3-CK-D4（01第43行）；B3-SA-Ca-D4（01第55行）|

## 附录D｜216个照片引用补证索引

列出每个引用的首个单元格；同一容器同日多个果共用引用不自动算照片重复错误。实际原图仍未提供。

|引用编码|首个引用位置|引用单元格数|
|---|---|---:|
|IMG-B1-CK-L1-D0|04_质量变化!L2|5|
|IMG-B1-CK-L1-D1|04_质量变化!L3|5|
|IMG-B1-CK-L1-D2|04_质量变化!L4|5|
|IMG-B1-CK-L1-D3|04_质量变化!L5|5|
|IMG-B1-CK-L1-D4|04_质量变化!L6|5|
|IMG-B1-CK-L2-D0|04_质量变化!L7|5|
|IMG-B1-CK-L2-D1|04_质量变化!L8|5|
|IMG-B1-CK-L2-D2|04_质量变化!L9|5|
|IMG-B1-CK-L2-D3|04_质量变化!L10|5|
|IMG-B1-CK-L2-D4|04_质量变化!L11|5|
|IMG-B1-CK-L3-D0|04_质量变化!L12|5|
|IMG-B1-CK-L3-D1|04_质量变化!L13|5|
|IMG-B1-CK-L3-D2|04_质量变化!L14|5|
|IMG-B1-CK-L3-D3|04_质量变化!L15|5|
|IMG-B1-CK-L3-D4|04_质量变化!L16|5|
|IMG-B1-Ca-L1-D0|04_质量变化!L17|5|
|IMG-B1-Ca-L1-D1|04_质量变化!L18|5|
|IMG-B1-Ca-L1-D2|04_质量变化!L19|5|
|IMG-B1-Ca-L1-D3|04_质量变化!L20|5|
|IMG-B1-Ca-L1-D4|04_质量变化!L21|5|
|IMG-B1-Ca-L2-D0|04_质量变化!L22|5|
|IMG-B1-Ca-L2-D1|04_质量变化!L23|5|
|IMG-B1-Ca-L2-D2|04_质量变化!L24|5|
|IMG-B1-Ca-L2-D3|04_质量变化!L25|5|
|IMG-B1-Ca-L2-D4|04_质量变化!L26|5|
|IMG-B1-Ca-L3-D0|04_质量变化!L27|5|
|IMG-B1-Ca-L3-D1|04_质量变化!L28|5|
|IMG-B1-Ca-L3-D2|04_质量变化!L29|5|
|IMG-B1-Ca-L3-D3|04_质量变化!L30|5|
|IMG-B1-Ca-L3-D4|04_质量变化!L31|5|
|IMG-B1-SA-Ca-L1-D0|04_质量变化!L32|5|
|IMG-B1-SA-Ca-L1-D1|04_质量变化!L33|5|
|IMG-B1-SA-Ca-L1-D2|04_质量变化!L34|5|
|IMG-B1-SA-Ca-L1-D3|04_质量变化!L35|5|
|IMG-B1-SA-Ca-L1-D4|04_质量变化!L36|5|
|IMG-B1-SA-Ca-L2-D0|04_质量变化!L37|5|
|IMG-B1-SA-Ca-L2-D1|04_质量变化!L38|5|
|IMG-B1-SA-Ca-L2-D2|04_质量变化!L39|5|
|IMG-B1-SA-Ca-L2-D3|04_质量变化!L40|5|
|IMG-B1-SA-Ca-L2-D4|04_质量变化!L41|5|
|IMG-B1-SA-Ca-L3-D0|04_质量变化!L42|5|
|IMG-B1-SA-Ca-L3-D1|04_质量变化!L43|5|
|IMG-B1-SA-Ca-L3-D2|04_质量变化!L44|5|
|IMG-B1-SA-Ca-L3-D3|04_质量变化!L45|5|
|IMG-B1-SA-Ca-L3-D4|04_质量变化!L46|5|
|IMG-B2-CK-L1-D0|04_质量变化!L47|5|
|IMG-B2-CK-L1-D1|04_质量变化!L48|5|
|IMG-B2-CK-L1-D2|04_质量变化!L49|5|
|IMG-B2-CK-L1-D3|04_质量变化!L50|5|
|IMG-B2-CK-L1-D4|04_质量变化!L51|5|
|IMG-B2-CK-L2-D0|04_质量变化!L52|5|
|IMG-B2-CK-L2-D1|04_质量变化!L53|5|
|IMG-B2-CK-L2-D2|04_质量变化!L54|5|
|IMG-B2-CK-L2-D3|04_质量变化!L55|5|
|IMG-B2-CK-L2-D4|04_质量变化!L56|5|
|IMG-B2-CK-L3-D0|04_质量变化!L57|5|
|IMG-B2-CK-L3-D1|04_质量变化!L58|5|
|IMG-B2-CK-L3-D2|04_质量变化!L59|5|
|IMG-B2-CK-L3-D3|04_质量变化!L60|5|
|IMG-B2-CK-L3-D4|04_质量变化!L61|5|
|IMG-B2-Ca-L1-D0|04_质量变化!L62|5|
|IMG-B2-Ca-L1-D1|04_质量变化!L63|5|
|IMG-B2-Ca-L1-D2|04_质量变化!L64|5|
|IMG-B2-Ca-L1-D3|04_质量变化!L65|5|
|IMG-B2-Ca-L1-D4|04_质量变化!L66|5|
|IMG-B2-Ca-L2-D0|04_质量变化!L67|5|
|IMG-B2-Ca-L2-D1|04_质量变化!L68|5|
|IMG-B2-Ca-L2-D2|04_质量变化!L69|5|
|IMG-B2-Ca-L2-D3|04_质量变化!L70|5|
|IMG-B2-Ca-L2-D4|04_质量变化!L71|5|
|IMG-B2-Ca-L3-D0|04_质量变化!L72|5|
|IMG-B2-Ca-L3-D1|04_质量变化!L73|5|
|IMG-B2-Ca-L3-D2|04_质量变化!L74|5|
|IMG-B2-Ca-L3-D3|04_质量变化!L75|5|
|IMG-B2-Ca-L3-D4|04_质量变化!L76|5|
|IMG-B2-SA-Ca-L1-D0|04_质量变化!L77|5|
|IMG-B2-SA-Ca-L1-D1|04_质量变化!L78|5|
|IMG-B2-SA-Ca-L1-D2|04_质量变化!L79|5|
|IMG-B2-SA-Ca-L1-D3|04_质量变化!L80|5|
|IMG-B2-SA-Ca-L1-D4|04_质量变化!L81|5|
|IMG-B2-SA-Ca-L2-D0|04_质量变化!L82|5|
|IMG-B2-SA-Ca-L2-D1|04_质量变化!L83|5|
|IMG-B2-SA-Ca-L2-D2|04_质量变化!L84|5|
|IMG-B2-SA-Ca-L2-D3|04_质量变化!L85|5|
|IMG-B2-SA-Ca-L2-D4|04_质量变化!L86|5|
|IMG-B2-SA-Ca-L3-D0|04_质量变化!L87|5|
|IMG-B2-SA-Ca-L3-D1|04_质量变化!L88|5|
|IMG-B2-SA-Ca-L3-D2|04_质量变化!L89|5|
|IMG-B2-SA-Ca-L3-D3|04_质量变化!L90|5|
|IMG-B2-SA-Ca-L3-D4|04_质量变化!L91|5|
|IMG-B3-CK-L1-D0|04_质量变化!L92|5|
|IMG-B3-CK-L1-D1|04_质量变化!L93|5|
|IMG-B3-CK-L1-D2|04_质量变化!L94|5|
|IMG-B3-CK-L1-D3|04_质量变化!L95|5|
|IMG-B3-CK-L1-D4|04_质量变化!L96|5|
|IMG-B3-CK-L2-D0|04_质量变化!L97|5|
|IMG-B3-CK-L2-D1|04_质量变化!L98|5|
|IMG-B3-CK-L2-D2|04_质量变化!L99|5|
|IMG-B3-CK-L2-D3|04_质量变化!L100|5|
|IMG-B3-CK-L2-D4|04_质量变化!L101|5|
|IMG-B3-CK-L3-D0|04_质量变化!L102|5|
|IMG-B3-CK-L3-D1|04_质量变化!L103|5|
|IMG-B3-CK-L3-D2|04_质量变化!L104|5|
|IMG-B3-CK-L3-D3|04_质量变化!L105|5|
|IMG-B3-CK-L3-D4|04_质量变化!L106|5|
|IMG-B3-Ca-L1-D0|04_质量变化!L107|5|
|IMG-B3-Ca-L1-D1|04_质量变化!L108|5|
|IMG-B3-Ca-L1-D2|04_质量变化!L109|5|
|IMG-B3-Ca-L1-D3|04_质量变化!L110|5|
|IMG-B3-Ca-L1-D4|04_质量变化!L111|5|
|IMG-B3-Ca-L2-D0|04_质量变化!L112|5|
|IMG-B3-Ca-L2-D1|04_质量变化!L113|5|
|IMG-B3-Ca-L2-D2|04_质量变化!L114|5|
|IMG-B3-Ca-L2-D3|04_质量变化!L115|5|
|IMG-B3-Ca-L2-D4|04_质量变化!L116|5|
|IMG-B3-Ca-L3-D0|04_质量变化!L117|5|
|IMG-B3-Ca-L3-D1|04_质量变化!L118|5|
|IMG-B3-Ca-L3-D2|04_质量变化!L119|5|
|IMG-B3-Ca-L3-D3|04_质量变化!L120|5|
|IMG-B3-Ca-L3-D4|04_质量变化!L121|5|
|IMG-B3-SA-Ca-L1-D0|04_质量变化!L122|5|
|IMG-B3-SA-Ca-L1-D1|04_质量变化!L123|5|
|IMG-B3-SA-Ca-L1-D2|04_质量变化!L124|5|
|IMG-B3-SA-Ca-L1-D3|04_质量变化!L125|5|
|IMG-B3-SA-Ca-L1-D4|04_质量变化!L126|5|
|IMG-B3-SA-Ca-L2-D0|04_质量变化!L127|5|
|IMG-B3-SA-Ca-L2-D1|04_质量变化!L128|5|
|IMG-B3-SA-Ca-L2-D2|04_质量变化!L129|5|
|IMG-B3-SA-Ca-L2-D3|04_质量变化!L130|5|
|IMG-B3-SA-Ca-L2-D4|04_质量变化!L131|5|
|IMG-B3-SA-Ca-L3-D0|04_质量变化!L132|5|
|IMG-B3-SA-Ca-L3-D1|04_质量变化!L133|5|
|IMG-B3-SA-Ca-L3-D2|04_质量变化!L134|5|
|IMG-B3-SA-Ca-L3-D3|04_质量变化!L135|5|
|IMG-B3-SA-Ca-L3-D4|04_质量变化!L136|5|
|IMG-B1-CK-D0-D0|05_腐烂观察!M2|3|
|IMG-B1-CK-D2-D0|05_腐烂观察!M5|3|
|IMG-B1-CK-D4-D0|05_腐烂观察!M8|3|
|IMG-B1-Ca-D0-D0|05_腐烂观察!M23|3|
|IMG-B1-Ca-D2-D0|05_腐烂观察!M26|3|
|IMG-B1-Ca-D4-D0|05_腐烂观察!M29|3|
|IMG-B1-SA-Ca-D0-D0|05_腐烂观察!M44|3|
|IMG-B1-SA-Ca-D2-D0|05_腐烂观察!M47|3|
|IMG-B1-SA-Ca-D4-D0|05_腐烂观察!M50|3|
|IMG-B1-CK-D2-D1|05_腐烂观察!M65|3|
|IMG-B1-CK-D4-D1|05_腐烂观察!M68|3|
|IMG-B1-Ca-D2-D1|05_腐烂观察!M83|3|
|IMG-B1-Ca-D4-D1|05_腐烂观察!M86|3|
|IMG-B1-SA-Ca-D2-D1|05_腐烂观察!M101|3|
|IMG-B1-SA-Ca-D4-D1|05_腐烂观察!M104|3|
|IMG-B1-CK-D2-D2|05_腐烂观察!M119|3|
|IMG-B1-CK-D4-D2|05_腐烂观察!M122|3|
|IMG-B1-Ca-D2-D2|05_腐烂观察!M137|3|
|IMG-B1-Ca-D4-D2|05_腐烂观察!M140|3|
|IMG-B1-SA-Ca-D2-D2|05_腐烂观察!M155|3|
|IMG-B1-SA-Ca-D4-D2|05_腐烂观察!M158|3|
|IMG-B1-CK-D4-D3|05_腐烂观察!M173|3|
|IMG-B1-Ca-D4-D3|05_腐烂观察!M188|3|
|IMG-B1-SA-Ca-D4-D3|05_腐烂观察!M203|3|
|IMG-B1-CK-D4-D4|05_腐烂观察!M218|3|
|IMG-B1-Ca-D4-D4|05_腐烂观察!M233|3|
|IMG-B1-SA-Ca-D4-D4|05_腐烂观察!M248|3|
|IMG-B2-CK-D0-D0|05_腐烂观察!M263|3|
|IMG-B2-CK-D2-D0|05_腐烂观察!M266|3|
|IMG-B2-CK-D4-D0|05_腐烂观察!M269|3|
|IMG-B2-Ca-D0-D0|05_腐烂观察!M284|3|
|IMG-B2-Ca-D2-D0|05_腐烂观察!M287|3|
|IMG-B2-Ca-D4-D0|05_腐烂观察!M290|3|
|IMG-B2-SA-Ca-D0-D0|05_腐烂观察!M305|3|
|IMG-B2-SA-Ca-D2-D0|05_腐烂观察!M308|3|
|IMG-B2-SA-Ca-D4-D0|05_腐烂观察!M311|3|
|IMG-B2-CK-D2-D1|05_腐烂观察!M326|3|
|IMG-B2-CK-D4-D1|05_腐烂观察!M329|3|
|IMG-B2-Ca-D2-D1|05_腐烂观察!M344|3|
|IMG-B2-Ca-D4-D1|05_腐烂观察!M347|3|
|IMG-B2-SA-Ca-D2-D1|05_腐烂观察!M362|3|
|IMG-B2-SA-Ca-D4-D1|05_腐烂观察!M365|3|
|IMG-B2-CK-D2-D2|05_腐烂观察!M380|3|
|IMG-B2-CK-D4-D2|05_腐烂观察!M383|3|
|IMG-B2-Ca-D2-D2|05_腐烂观察!M398|3|
|IMG-B2-Ca-D4-D2|05_腐烂观察!M401|3|
|IMG-B2-SA-Ca-D2-D2|05_腐烂观察!M416|3|
|IMG-B2-SA-Ca-D4-D2|05_腐烂观察!M419|3|
|IMG-B2-CK-D4-D3|05_腐烂观察!M434|3|
|IMG-B2-Ca-D4-D3|05_腐烂观察!M449|3|
|IMG-B2-SA-Ca-D4-D3|05_腐烂观察!M464|3|
|IMG-B2-CK-D4-D4|05_腐烂观察!M479|3|
|IMG-B2-Ca-D4-D4|05_腐烂观察!M494|3|
|IMG-B2-SA-Ca-D4-D4|05_腐烂观察!M509|3|
|IMG-B3-CK-D0-D0|05_腐烂观察!M524|3|
|IMG-B3-CK-D2-D0|05_腐烂观察!M527|3|
|IMG-B3-CK-D4-D0|05_腐烂观察!M530|3|
|IMG-B3-Ca-D0-D0|05_腐烂观察!M545|3|
|IMG-B3-Ca-D2-D0|05_腐烂观察!M548|3|
|IMG-B3-Ca-D4-D0|05_腐烂观察!M551|3|
|IMG-B3-SA-Ca-D0-D0|05_腐烂观察!M566|3|
|IMG-B3-SA-Ca-D2-D0|05_腐烂观察!M569|3|
|IMG-B3-SA-Ca-D4-D0|05_腐烂观察!M572|3|
|IMG-B3-CK-D2-D1|05_腐烂观察!M587|3|
|IMG-B3-CK-D4-D1|05_腐烂观察!M590|3|
|IMG-B3-Ca-D2-D1|05_腐烂观察!M605|3|
|IMG-B3-Ca-D4-D1|05_腐烂观察!M608|3|
|IMG-B3-SA-Ca-D2-D1|05_腐烂观察!M623|3|
|IMG-B3-SA-Ca-D4-D1|05_腐烂观察!M626|3|
|IMG-B3-CK-D2-D2|05_腐烂观察!M641|3|
|IMG-B3-CK-D4-D2|05_腐烂观察!M644|3|
|IMG-B3-Ca-D2-D2|05_腐烂观察!M659|3|
|IMG-B3-Ca-D4-D2|05_腐烂观察!M662|3|
|IMG-B3-SA-Ca-D2-D2|05_腐烂观察!M677|3|
|IMG-B3-SA-Ca-D4-D2|05_腐烂观察!M680|3|
|IMG-B3-CK-D4-D3|05_腐烂观察!M695|3|
|IMG-B3-Ca-D4-D3|05_腐烂观察!M710|3|
|IMG-B3-SA-Ca-D4-D3|05_腐烂观察!M725|3|
|IMG-B3-CK-D4-D4|05_腐烂观察!M740|3|
|IMG-B3-Ca-D4-D4|05_腐烂观察!M755|3|
|IMG-B3-SA-Ca-D4-D4|05_腐烂观察!M770|3|
