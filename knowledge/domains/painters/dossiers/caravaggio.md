# 米开朗基罗·梅里西·达·卡拉瓦乔（Michelangelo Merisi da Caravaggio, 1571–1610）档案

> 标注清扫 2026-10-15（依据 _crosscheck.md）
> 模板：`templates/artist_module.md`｜写手：ArtistCaravaggio（wave2，GOALS A-15）｜日期：2026-10-15
> 证据分级：`[自述]`（本人写下/说出，带出处）· `[史料]`（当时记录/档案/法庭证词/馆藏信息）· `[研究]`（艺术史家/博物馆分析）· `[归纳]`（本项目从作品与资料归纳的操作规则，不冒充艺术家内心）· `[推测]`（低置信）
> 正文中文；引用保留原文；prompt 用英文。
> **本档案的特殊性（写在前面的口径）**：卡拉瓦乔几乎没有文字留世——无书信集、无论述、无笔记；现代传记作者 Graham-Dixon 的判断是「关于绘画，我们只有他的一句话」，且出自 1603 年诽谤罪的审讯记录 `[研究]`[R11]。因此本档案第 5 节以**法庭证词转录**与**同代传记（Baglione 1642 / Bellori 1672，两人都对他有敌意：前者是诉讼对手，后者属古典主义阵营且从未见过他）**为主，全部标 `[史料]` 并注明性质；不把同代转述包装成「他本人说的」。

---

## 0. 元信息

- **生卒 / 国别**：1571-09-29 生于米兰；1610-07-18 卒于 Porto Ercole（托斯卡纳 Grosseto 附近）。意大利。`[史料]`（[R1]；另见 [R14] 的死亡档案）**出生地注**：旧说生于 Caravaggio 镇，现代学界共识为生于米兰（"It was previously assumed that he had been born in Caravaggio"）`[史料]`[R1]。
- **主要流派**：无自建学派；被艺术史归为**巴洛克形成期的关键革命者**与「现实主义/自然主义」潮流的开创人物（梵蒂冈博物馆用语："the protagonist of a real artistic revolution… the most important personage of the 'realist' trend of seventeenth century painting"）`[研究]`[R8]。追随者统称 **Caravaggisti**（亦称 tenebrosi，"shadowists"）`[研究]`[R1]。
- **主要媒介**：油画（布面为主；《美杜莎》为木盾凸面圆画）`[史料]`[R1][R16]。
- **一句话能力定位**：**舞台式硬光 / 「光的开关」**——给系统补上「光可以是非自然的」这一档：单一硬光源、无反射、背景压到近黑，亮部只落在**脸、手与关键道具**三类对象上；与「人物贴住画面平面 + 定格瞬间」共同构成叙事语法。（缺口归属：`expansion.md` §2.2 **G1 戏剧性光影（舞台式硬光）**，本档案即该缺口的模块化落地；§1.2 已定能力标签：`戏剧布光(舞台式)` · `高反差明暗两级` · `瞬间定格叙事` · `非理想化人体` · `暗底静物`）
- **关键作品 5 件（带馆藏与 URL）**：
  1. *The Supper at Emmaus*《以马忤斯的晚餐》1601，141 × 196.2 cm，National Gallery London（NG172）— [R5]
  2. *David with the Head of Goliath*《大卫手提歌利亚的头》1606–07 或 1609–10，125 × 101 cm，Galleria Borghese（inv. 455）— [R10]
  3. *The Deposition (Entombment)*《基督下葬》1603–04，Musei Vaticani, Pinacoteca, Sala XII — [R8]
  4. *The Beheading of Saint John the Baptist*《施洗者圣约翰被斩首》1608，370 × 520 cm，St John's Co-Cathedral, Valletta（**唯一署名作品**，画幅最大）— [R1]（馆方页本轮未直读，见 §10）
  5. *Boy with a Basket of Fruit*《捧果篮的男孩》c. 1595，70 × 67 cm，Galleria Borghese（inv. 136）— [R9]

---

## 1. 视觉指纹（10 条）

| # | 特征 | 可观察量 | 证据级 |
|---|---|---|---|
| 1 | **单光源、无反射、背景近黑**：光来自画外高处（左或右上方），画内不出现光源；环境反光被取消 | 背景（墙/地）最亮像素 ≤ 全帧最亮的 ~10%；画面内可见光源数 = 0 | `[史料]` [R4]（Met 引同代批评家："a focused light source from high up, without reflections, as though in a room with a single window and the walls painted black"）；[R16]（Bellori：灯置高处、光直落） |
| 2 | **两级明暗（tenebrism）**：亮部极亮、暗部极暗，中间调被压缩；黑暗本身成为画面主体（"darkness becomes a dominating feature"） | 亮度直方图双峰；中间带 [0.35,0.65] 像素占比显著低于常规油画 | `[研究]` [R2][R1]（"the shift from light to dark with little intermediate value"） |
| 3 | **暗部不是死黑**：暗区保留可辨的中间调结构（深色底被有意留出当中间调用） | 暗区内部仍有明度层次；纯黑（=0）像素占比低 | `[研究]` [R6]（NG 论《莎乐美》："the dark ground left deliberately exposed in several areas to provide the mid-tone in the shadows"） |
| 4 | **人物贴住画面平面**：前景人物被推到最外层，越出/贴边，空间深度被压扁 | 主人物包围盒高度 ≥ 画幅高 ~80%；至少 1 个主体被画幅边缘裁切 | `[研究]` [R4]（"pushed the figures up against the picture plane"）；量化阈值为 `[归纳]`（对照 [R5][R6] 作品） |
| 5 | **手势是叙事主语**：指、伸、插、摊——关键信息由手传递，且手被光点亮 | 高光连通域与「手」相交 ≥1；手势延长线指向叙事对象 | `[归纳]`（依据 [R5] 的 Thomas 手指、[R5]《以马忤斯》前伸的手、[R13] 的"手臂朝向"分析） |
| 6 | **反理想化的人体与面孔**：脏指甲、破衣缝、粗糙市井面孔当圣徒 | 布料有磨损/撕裂细节；指甲、脚底、衣缝可见污痕 | `[史料]` [R1]（"dirt under his fingernails"）[R5]（"bearded, lined faces and ragged clothes"） |
| 7 | **当代服装 + 当代空间**：圣徒穿 17 世纪衣服，场景像当代罗马室内/酒馆/地下室 | 服装年代 = 17 世纪；背景为素墙/室内，无风景、无天空 | `[史料]` [R1]（"figures in contemporary dress inhabiting a religious scene"）[R16]（"a dingy modern tax collector's office somewhere in a basement of Rome"，Graham-Dixon 语） |
| 8 | **定格瞬间**：画面是一个被冻结的动作极值（认出的一瞬、刀落的一瞬） | 每帧只有一个"动作极值"；无运动模糊 | `[研究]` [R1]（"the passing of a crucial moment"）；[R5]（"captures the dramatic climax… the moment of revelation"） |
| 9 | **色域收窄**：土色系（赭、红棕、铅白、黑）为主；晚期进一步收窄、更少纯色 | 同屏色相数少；晚期作品（[R6][R10]）色彩范围明显窄于罗马期（[R5]） | `[研究]` [R6]（"restricted range of colour"）[R10]（Borghese：晚期"la riduzione della gamma cromatica"） |
| 10 | **深色底（dark ground）**：画布先铺深棕底，亮部在其上"塑出"，底色参与中间调 | 暗部可见底色透出；亮部从深底上叠加 | `[研究]` [R6]；配套技法见 §2 |

---

## 2. 技法规则（10 条）

1. **直接画法：不做纸上素描，直接在画布上工作**。NG 明说这是他"最有争议的技法之一"——"painting directly onto the canvas, rather than following the traditional method of working out a composition through numerous preparatory studies. Indeed, not a single drawing that can be firmly attributed to Caravaggio survives." `[研究]` [R5]
2. **但"直接画"≠"无准备"**：技术检查发现他会在画布上先用深棕色颜料以笔画轮廓（**abbozzo**）；《以马忤斯》桌上酒杯底部的最终轮廓上方就有这种笔绘痕迹 `[研究]` [R5]。Borghese 藏品页记载：2012 年的分析在《捧果篮的男孩》上发现了**直接画在画布上的底层草图**，恰好印证古代文献所说的"dal naturale"（从自然写生）的画法 `[研究]` [R9]。
3. **incisions（刻线定位）**：他常在尚软的底子（priming/undercoat）上用笔杆尾端**徒手刻出人物位置线**——"to mark out where figures were to be placed, and presumably to allow models to resume their poses" `[研究]` [R5]；《大卫》的诊断分析同样发现了 incisioni `[研究]` [R10]；Wikipedia 综述同此说（"scoring basic guides directly onto the canvas with the end of the brush handle"）`[研究]` [R1]。
4. **深色底 + 留底作中间调**：深色 ground 被有意暴露在若干区域充当暗部中间调（见 §1-3）`[研究]` [R6]。
5. **真人摆姿势、从真人写生**：Met："His practice of painting directly from posed models violated the idealizing premise of Renaissance theory" `[研究]` [R4]；模特可考者包括 Mario Minniti、Francesco Boneri，女性模特多为当时登记在册的妓女（Fillide Melandroni、Anna Bianchini、Maddalena Antognetti/Lena）`[史料]` [R1]。
6. **快速工作**：以极快的速度完成（"worked at great speed, from live models"）`[史料]` [R1]；1604 年印行的记述说他"干两周活、晃荡一两个月"（见 §5-5）。
7. **光＝画外单灯**：同代批评家与 Bellori 的记载一致（§5-3、§5-7）：高置单光源、无反射、暗室黑墙 `[史料]` [R4][R16]。
8. **笔触：亮部"概括性"厚笔 + 晚期放宽**：《以马忤斯》中"两条快速、高度厚涂（impastoed）的斜笔"被当作人物定位的概括手段 `[研究]` [R5]；晚期"broad application in place of finely modelled gradations" `[研究]` [R6]。
9. **少 pentimenti、高预谋**：NG 指出《以马忤斯》几乎没有重大改动，唯一的显著改动是把使徒的左膝移到地毯后，以增强手臂前伸的推力——说明构图经过高度准备 `[研究]` [R5]。
10. **覆盖重画**：有时放弃不满意的构图，直接在上面画新画 `[史料]` [R7]（NG 艺术家页："Sometimes he abandoned a disappointing composition and painted new work over the top."）。

---

## 3. 创作原则（8 条）

1. **从自然/真人写生优先于程式**：古代文献（Mancini 1617–21、Baglione、Bellori）一致记载其画法为"dal naturale"，Borghese 的 2012 年分析以画布上的底层草图佐证此说。`[史料]` [R9]（另见 [R1]）
2. **光的取舍先于色彩**：同代与后世的第一手描述都把机制落在光上——高置单灯、直落、只揭示"身体的主要部分"；颜色服务于光的分区。`[史料]` [R16]；据此归纳的操作序列（先定光位→再定亮部三对象→最后压暗背景）标 `[归纳]`。
3. **反理想化是立场，不是疏忽**：把圣徒画成普通劳动者（破衣、皱纹、脏指甲），宗教场景按"正在眼前发生"来处理——Met 称之为"a provocative insistence on the physical reality of the scene portrayed"。`[研究]` [R4][R5]
4. **叙事只取一瞬**：画面永远是决定性瞬间的动作极值，不画过程。`[研究]` [R1][R5]
5. **为对抗委托方的口味承担代价**：《圣母与蛇》（Madonna dei Palafrenieri）上墙两天即被撤下 `[史料]` [R1]；《圣母之死》被加尔默罗会拒收（Mancini 记因以名妓为圣母模特，Baglione 记因"露腿"失礼，Gash 认为可能还有神学原因）`[史料]/[研究]` [R1]。Graham-Dixon 的判断："他拒绝改变做法"。`[研究]` [R11]
6. **物理真实压倒象征程式**：圣像的象征符号（光环等）被压缩到最低，代之以可触摸的物证（伤口、面包、水杯折射）。`[研究]` [R5][R13]
7. **不做工作室、不立学派**：与 Carracci 相反，他没有建立工坊来传播技法，也没有留下理论（"Nor did he ever set out his underlying philosophical approach to art"）——这既是他死后声誉脆弱的原因，也是后世只能"从他的画里反推规则"的原因。`[研究]` [R1]
8. **把模特当材料，反复使用同一批脸**：Minniti、Boneri、Fillide 等反复出现在不同角色里（天使、圣约翰、大卫……），同一张脸可以同时是神与市井。`[史料]` [R1]

> 口径提醒（项目宪章）：以上 1–8 是**从作品与艺术史资料归纳的操作规则**，不冒充"他心里想的"；按行内标注：第 1/2/5/8 条有 `[史料]` 支撑（#2 另含 `[归纳]` 操作序列），第 3/4/6/7 条为 `[研究]`。

---

## 4. 控制参数（6 个，各带弱/中/强三档）

| # | 参数 | 弱（20–30%） | 中（50–60%） | 强（80–95%） | 默认建议 |
|---|---|---|---|---|---|
| P1 | **光源聚焦度 / 硬度（Light Hardness）**`[归纳]` | 柔和环境光，多个光源或天光；有反射补光 | 单一方向光，允许少量反射；亮部边界略软 | 单一硬光（画外、高置 30°–60° 仰角），无反射、无补光，亮部边界硬 | **85%**（本模块强档即其身份） |
| P2 | **背景明度上限（Background Ceiling）**`[归纳]` | 背景可达全帧最亮的 40–50%（近自然室内） | ≤20% | ≤8–10%（近黑，墙/地几乎只剩轮廓暗示） | **10%** |
| P3 | **中间调压缩（Midtone Compression）**`[归纳]` | 全调域，中间调充足（学院式渐变） | 中间调 [0.35,0.65] 占比 25–40% | ≤25%，直方图双峰；暗带 [0,0.25) ≥40% | **30%**（比强档松一档，保可读性） |
| P4 | **贴平面度（Figure-to-Plane）**`[归纳]` | 人物在景深中，有明确地面/环境纵深 | 半身/大半身，背景压暗但仍有空间暗示 | 主人物高度 ≥ 画幅 80%、被边缘裁切、前景物越出画面 | **80%** |
| P5 | **色域收窄（Palette Restraint）**`[归纳]` | 色相多、含冷色与高纯色（晚期以后被弃） | 土色系为主，1–2 个饱和强调色（红/绿） | 近乎单色阶：赭/红棕/铅白/黑，饱和色仅出现在道具 | **60%**（罗马期）／晚期取 85% |
| P6 | **手势—光斑绑定（Gesture & Highlight Binding）**`[归纳]` | 光均匀落在全身；手部无特别强调 | 脸部优先受光，手部次之 | 光斑只落在**脸 / 手 / 关键道具**三类对象；高光连通域 ≤5 且都与三者相交 | **85%** |

> **分工口径（与伦勃朗，必须写死，来源 `expansion.md` §1.1/§1.2 与 §4.3 冲突规则）**：两人同属"从黑暗里打光"一族（视觉重叠 ~60%），本档案固定为——**卡拉瓦乔 = 光的开关 + 物理（硬光戏剧）**；**伦勃朗 = 光的连续衰减 + 心理（心理化光斑）**。落到参数上：P1 的强档（无反射硬光）与 P3 的强档（中间调双峰）**是本模块专属**；一旦把 P1 降到中档并允许"光在面部连续衰减"，产出就进入伦勃朗的地盘，组合实验里必须按此判分。本判据为 `[归纳]`，可被 wave3 实验推翻。
> **用法**：P1/P2 定"是不是卡拉瓦乔"；P4/P6 定叙事（贴平面 + 手势受光）；P3/P5 定时期（罗马期 vs 晚期）。三档描述可直接当判定标准写进自查表。

---

## 5. 自述与原话（8 条，逐条标性质；本档案"自述"以审讯记录与同代转述为主）

1. **1603 年诽谤案法庭证词（唯一被现代学者认定为"他关于绘画的话"的记录）**
   原文（英译）："I don't know any painter who thinks Giovanni Baglione is a good painter."；另一句：the Resurrection altarpiece was "clumsy [goffa]"，"it's the worst he's done, and I haven't heard a single painter praise the said painting."
   中译：我不认识任何一个认为乔瓦尼·巴利奥内画得好的画家。……（他的《复活》）笨拙，是他画得最差的一件，我没听到任何一个画家夸过那幅画。
   出处：[R3]（Wikipedia "Giovanni Baglione" 引 1603 年法庭文书；同一引文另见 [R15]）。
   性质：**法庭证词转录** `[史料]`——且据 [R11]（Graham-Dixon）："关于绘画，我们只有他的一句话——而这句话的真诚度本身就可疑，因为它是在他以诽谤罪（死罪）被审讯时挤出来的。" 使用注意：这是**贬损对手**的语境，不是画论。
2. **Baglione《Vite》1642（敌意传记作者；1603 年官司的原告）**
   原文（意）："fece alcuni quadretti da lui nello specchio ritratti. E il primo fu un Bacco con alcuni grappoli d'uve diverse, con gran diligenza fatte ma di maniera un poco secca"
   中译：他画了一些小画，是他照着镜子画的自己的肖像。第一幅是一个巴克斯，手里拿着几串不同的葡萄，画得极用心，但手法有点干。
   出处：[R12]（Galleria Borghese 藏品页引 Baglione 1642, p. 136）。
   性质：`[史料]`，**带贬抑的转述**（"maniera un poco secca"＝手法干涩）；也是"用镜子作画"这条记载的出处。
3. **Bellori《Le vite》1672（古典主义理论家；从未见过他本人）**
   原文（英译）："He went so far in this style that he never showed any of his figures in open daylight, but instead found a way to place them in the darkness of a closed room, placing a lamp high so that the light would fall straight down, revealing the principal part of the body and leaving the rest in shadow."
   中译：他在这条路上走得太远：从不让任何人物出现在天光下，而是设法把他们安置在暗室之中，把灯放在高处，让光直直落下，只揭示身体的主要部分，其余留在阴影里。
   出处：[R16]（The Art Story 所载英译，系 Bellori 1672 论《施洗者圣约翰被斩首》段落的转引）。**本条为二手转引，原书页码回查未做（见 §10）。**
   性质：`[史料]`（同代记录，敌意框架）。
4. **1604-04-26 侍者 Pietro Antonio de Fosaccia 的报案陈述（罗马国家档案馆文书）**
   原文（英译）："About 17 o'clock [lunchtime] the accused, together with two other people, was eating in the Moor's restaurant at La Maddalena, where I work as a waiter. I brought them eight cooked artichokes, four cooked in butter and four fried in oil. The accused asked me which were cooked in butter and which fried in oil, and I told him to smell them… He got angry and without saying anything more, grabbed an earthenware dish and hit me on the cheek…"
   中译：约 17 时（午餐时分），被告与另外两人在拉·马达莱纳的"摩尔人"餐馆吃饭，我在那里当侍者。我端上八个熟洋蓟，四个黄油煮的、四个油炸的。被告问我哪几个是黄油的、哪几个是油炸的，我让他闻一闻就能分出来……他就火了，二话不说抓起一个陶盘打在我脸颊上……
   出处：[R14]（BBC 公布的档案英译，2011-02-18）。
   性质：`[史料]`（档案文书，**不是**他本人的话；但这是与艺术家直接相关的原样证词）。
5. **1604 年印行的早期记述（时人对他的描述）**
   原文："after a fortnight's work he will swagger about for a month or two with a sword at his side and a servant following him, from one ball-court to the next, ever ready to engage in a fight or an argument, so that it is most awkward to get along with him."
   中译：干两周活，然后就佩着剑、带着仆人晃荡一两个月，从一个球场到另一个球场，随时准备吵架或打架，跟他相处极难。
   出处：[R7]（NG 艺术家页，注明"据他的一位传记作者"）；同文另见 [R1]（1604 年印行的早期记述）。
   性质：`[史料]`（当时出版物）。
6. **友人 Marzio Milesi 所撰墓志铭（1610）**
   原文："Michelangelo Merisi, son of Fermo di Caravaggio – in painting not equal to a painter, but to Nature itself – died in Port' Ercole… He lived thirty-six years nine months and twenty days."
   中译：米开朗基罗·梅里西，费尔莫·达·卡拉瓦乔之子——在绘画上不逊于任何画家，而堪比自然本身——卒于圣埃尔科港……他活了三十六年九个月零二十天。
   出处：[R1]。
   性质：`[史料]`（友人撰，带溢美；注意按此计算生卒与 1610-07-18 一致）。
7. **同代批评家对"该画派"的机制描述（Met 转引）**
   原文："a characteristic of this school [of painting] is to use a focused light source from high up, without reflections, as though in a room with a [single] window and the walls painted black. In this fashion the lit and shadowed areas are very light and very dark and give enormous three-dimensionality to the painting, but in an unnatural fashion neither done or even conceived before by such artists as Raphael, Titian, Correggio, or others."
   中译：这个（画）派的特点是用一个高处的聚焦光源、没有反射，就像在一间只有一扇窗、墙被涂成黑色的房间里。这样，受光与阴影的部分都极亮极暗，给画面巨大的立体感，但以**不自然**的方式——拉斐尔、提香、科雷焦等人既没做过、也没想到过。
   出处：[R4]（Met，Christiansen 2003 转引"一位同代批评家"；Met 未具名原文作者，回查待办）。
   性质：`[史料]`（**这是本项目 §1-1、P1、P2 参数的直接史料依据**）。
8. **Graham-Dixon 对其"文字留世"的判语（给本节定性的现代研究）**
   原文："He was one of the most original artists ever to have lived, yet we have only one solitary sentence from him on the subject of painting…"
   中译：他是史上最具原创性的艺术家之一，然而关于绘画，我们只有他孤零零的一句话……
   出处：[R11]。
   性质：`[研究]`（现代传记作者判断）。

> **本节用法**：第 1 条是"他嘴里出来的"（且敌意语境）；第 2/3/7 条是"同代/近同代说他怎么画"（2、3 带敌意）；第 4/5 条是档案与时人记述；第 6 条是友人。**没有任何一条可以当作画论引用**——这决定了本模块的 prompt 只能从"作品可见机制"反推（§8）。

---

## 6. 临摹与影响链

### 6.1 他学过谁（来源方向）

- **Simone Peterzano（1584–88 学徒）**：米兰画家，学徒合约注明他是**提香的学生**；伦巴第自然主义（更近德国式写实、远于罗马风格主义的程式）经他传入 `[史料]` [R1]；Borghese 藏品页进一步指出《病酒神》的姿势引用了 Peterzano 在 Garegnano 的《波斯女先知》草图，并引 Dürer 版画《Ecce Homo》 `[研究]` [R12]。
- **米兰的公共资源**：达·芬奇《最后的晚餐》与伦巴第地方传统；反宗教改革大主教 Carlo Borromeo 所推的"朴素而有力"的宗教图像口味（Graham-Dixon 认为这是他的一个影响来源） `[史料]/[研究]` [R1][R11]。
- **威尼斯（可能）**：据载他可能到过威尼斯、看过乔尔乔内与提香——这是 `[推测]` 级：Zuccari 后来指责他"模仿乔尔乔内" `[史料]` [R1]。
- **罗马初期**：初到罗马时佩服拉斐尔（Gombrich 语，经 [R16] 转引）；进入 Cavalier d'Arpino（Giuseppe Cesari）工坊画花卉果实 `[史料]` [R1][R9]。
- **古典与前辈的直接引用（可考）**：《下葬》的 Nicodemus 用**米开朗基罗的脸**（其佛罗伦萨《哀悼基督》的自画像）、《圣母》姿态关联米开朗基罗《圣殇》与拉斐尔《博尔盖塞下葬》 `[研究]` [R13]；《病酒神》引用 Dürer `[研究]` [R12]。
- **同代对手**：与 **Annibale Carracci** 的路线之争（在罗马与意大利，最终胜出的是 Carracci 一路） `[研究]` [R1]。

### 6.2 谁学过他（输出方向）

- **罗马第一代 Caravaggisti**：Orazio Gentileschi、Giovanni Baglione（短暂的 Caravaggesco 期）、Carlo Saraceni、Orazio Borgianni；**Bartolomeo Manfredi 被 Met 称为"关键意大利传播者"** `[史料]/[研究]` [R1][R4]；Artemisia Gentileschi 风格上靠近该运动 `[研究]` [R1]。
- **那不勒斯**：Battistello Caracciolo、Carlo Sellitto（该派随 1656 年瘟疫终结）；NG 补充晚期直接影响 Caracciolo、Mattia Preti、**Jusepe de Ribera** `[研究]` [R1][R6]。
- **荷兰（Utrecht Caravaggisti）**：Hendrick ter Brugghen、Gerrit van Honthorst、Dirck van Baburen 到罗马受其影响，回国后形成 Utrecht Caravaggism；**再下一代传到 Rembrandt 与 Vermeer——两人都没去过意大利** `[研究]` [R1][R4]。
- **法国**：Valentin de Boulogne、Nicolas Tournier、Simon Vouet，以及**Georges de La Tour**（远距离影响） `[研究]` [R1][R4]。
- **西班牙**：Ribera、Zurbarán、Juan Bautista Maino；Velázquez 可能通过复制品接触 `[研究]` [R4]。
- **佛兰德斯**：**Rubens** 1601 年在罗马即接触其作品，后来画过《下葬》的"演绎"版，并建议曼图亚公爵买下被拒收的《圣母之死》（后入路易十四收藏） `[史料]/[研究]` [R1][R13]。
- **19–20 世纪重估**：Roberto Longhi 在 1920 年代把他重新推入欧洲传统——"Ribera, Vermeer, La Tour and Rembrandt could never have existed without him. And the art of Delacroix, Courbet and Manet would have been utterly different."；Bernard Berenson："除米开朗基罗外，没有哪位意大利画家影响如此之大。"；Berne-Joffroy："现代绘画，就始于卡拉瓦乔的作品。"；1951 年米兰 Palazzo Reale《Mostra del Caravaggio》展（Borghese 藏品页的展览史亦记此次）；1986 年 Derek Jarman 电影《Caravaggio》 `[研究]` [R1][R9]。

### 6.3 一句话总结（给提示词模块的"来历"注脚）

这条链说明卡拉瓦乔的 prompt 不是"风格滤镜"，而是一套**操作序列**：**先决定光从哪里来（开关）→ 再让光只落在脸/手/关键道具 → 最后把背景压到近黑、把中间调抽掉**；上游是伦巴第写实与威尼斯色（Peterzano/达芬奇/Borromeo 的口味），下游是整条欧洲巴洛克的明暗谱系（Caravaggisti → Utrecht → Rembrandt/Vermeer → La Tour → Ribera），并在 20 世纪经 Longhi 一脉被重新追认为"现代绘画的起点"。

---

## 7. 深度分析（10 条，馆方/学者，逐条带 URL）

1. **The Met, Heilbrunn Timeline — Keith Christiansen, "Caravaggio (Michelangelo Merisi) (1571–1610) and His Followers"（2003-10）**：给出机制的最凝练表述——"把人物推向画面平面 + 用光增强戏剧冲击与即时性"，并转引同代批评家对"高处聚焦光源、无反射、黑墙"的描述；把 Manfredi 定为意大利关键传播者，列出 ter Brugghen/Honthorst/Valentin/Tournier/Maino/Ribera/Zurbarán，判定"Caravaggism 由此成为国际运动、巴洛克绘画的拱心石之一"。[R4]
2. **National Gallery London —《The Supper at Emmaus》in-depth**：技法证据链最完整的一篇：abbozzo 笔绘底线、"not a single drawing… survives"、incised freehand lines 刻在软底上以便模特复位、两条厚涂斜笔作概括指示、几乎无 pentimenti 说明高度预谋；光从左侧来，在基督身后墙上投下"近乎反向光环"的阴影。[R5]
3. **National Gallery London —《Salome receives the Head of John the Baptist》in-depth**：晚期风格的三条判据——色域收窄、宽笔触替代精细过渡、**深色底被有意留出作暗部中间调**；并给出影响链（Caracciolo、Preti、Ribera）。[R6]
4. **Musei Vaticani — Pinacoteca, Sala XII《Deposition》**：馆方把它定义为"卡拉瓦乔最伟大的杰作之一"，并给出构图重解——不是"下葬"而是把基督安放在**敷油石（Anointing Stone）**上；同时给出馆方对艺术史地位的定性："realist trend of seventeenth century painting 最重要的人物"。[R8]（房间页见 [R12b]）
5. **Galleria Borghese 藏品目录 —《David con la testa di Golia》(inv. 455)**：出处链（1613 已在 Scipione Borghese 收藏，Manilli 1650 首次指出巨人脸＝卡拉瓦乔自画像、大卫＝"他的 Caravaggino"）、剑刃铭文 "H.AS O S" 的奥古斯丁格言读法（'H[umilit]AS O[ccidit] S[uperbiam]'）、以及**诊断分析发现 incisioni** 与晚期色彩收窄的实证。[R10]
6. **Galleria Borghese 藏品目录 —《Giovane con canestra di frutta》(inv. 136)**：记录 **2012 年分析发现画布上的底层草图**，用于印证古代文献"他直接从自然写生"的说法；并梳理 1607 年 Cavalier d'Arpino 收藏被没收→Scipione Borghese 的流传链。[R9]
7. **Andrew Graham-Dixon, *Caravaggio: A Life Sacred and Profane*（Penguin, 2010）摘录**：作者自述花十年拼证据；"只有一句话"的判语；把《朱迪斯斩首荷罗孚尼》读作"亚述帐篷里的神圣处决变成了罗马妓院里的谋杀"；对 1606 决斗与 1610 死亡的叙述（热衰竭/心脏骤停的可能）。[R11]
8. **BBC News — "Caravaggio's crimes exposed in Rome's police files"（2011-02-18）**：罗马国家档案馆展览报道，给出**档案日期表**（1598 携剑、1600 打人、1604 洋蓟、1606 杀人等）与**1604 侍者报案英译全文**；并给出一个与旧传记冲突的说法：他"不是在沙滩上独自死去，而是在医院病床上"。[R14]
9. **Literary Review — Jonathan Keates 评 Helen Langdon, *Caravaggio: A Life*（Chatto & Windus, 1998）**：书评强调"现代人把卡拉瓦乔重塑成 20 世纪艺术家形象"的投射问题，主张 17 世纪的语境比传记神话更复杂；Langdon 的这部传记被 Met 列为延伸阅读。[R17]（该页付费墙，仅开头可读）
10. **The Art Story — Caravaggio 条目（转引 Bellori 1672 英译与 Gombrich 等）**：作为 §5-3 Bellori 引文的载体与作品细读的二手来源；注意其为通俗资源，引文必须回查原书（见 §10）。[R16]

---

## 8. 提示词模块

### 8.1 图像生成模块（英文 prompt + 中文说明）

**正向段（可直接粘贴）**
```
Caravaggio-style tenebrist oil painting:
one single hard directional light from high left, no fill light, no reflected light;
background walls and floor in near-black shadow (values under 10% of the lit highlights);
deep dark brown ground left visible inside the shadows as their mid-tone;
violent chiaroscuro: lit passages bright and warm, shadows crushed, midtones suppressed;
one frozen instant of a narrative action; faces and hands catch the light;
gestures point at the narrative object; figures pushed flat against the picture plane,
half-length or three-quarter figures cropped by the frame edge;
ordinary working people as saints — weathered faces, torn clothes, dirty fingernails,
contemporary 17th-century Roman clothing; plain dark interior, no landscape, no sky;
restrained earth palette — ochre, madder red, lead white, bitumen black,
one or two saturated accents on a prop; direct painting, broad final touches,
impasto highlights on the lit edges
```
**负向约束（`--no` 风格）**
```
--no soft diffuse lighting, ambient light, multiple light sources, rim light, backlight,
glow, bloom, lens flare, volumetric rays, evenly lit faces, bright background,
landscape, sky, daylight, symmetry, idealised anatomy, smooth airbrushed gradients,
pastel palette, neon colours, cartoon, 3D render, photographic realism, motion blur,
fog, haze, mirror, chandelier, candles visible in frame, halo disc, crowd
```
**中文使用说明与强度建议**
- 先跑 6 张关键帧（1920×1080 静止构图），核对三件事：① 背景最亮像素是否 ≤ 全帧最亮的 ~10%？② 高光是否只落在脸/手/道具（P6）？③ 直方图是否双峰（P3）？
- 强度旋钮：①「光的硬度」由 P1 控制（默认 85%；想试伦勃朗式心理光降到 50%，但此时已越界，见 §4 分工注）；②「背景暗度」由 P2 控制（默认 10%）；③「贴平面」由 P4 控制（默认 80%）。
- 若模型退化成"普通暗调照片"：追加 `single unseen lamp above and outside the frame, hard shadow edges, no ambient occlusion fill`；若退化成"死黑剪影"：追加 `shadow areas still readable, dark brown ground visible in the half-tones`（对应 §1-3、8.2 规则 7）。
- 与达·芬奇模块组合时：只借用其**人物结构的体感**，禁止其 sfumato 的柔边与全调域（两条规则的冲突点就是"光的硬度轴"两端）。

### 8.2 代码艺术模块（7 条可判定规则，逐帧可自查）

1. **光源单一性**：全帧可见光源数 = 0（光从画外来）；主光方向固定为左上或右上（方向向量取 (±0.7, −0.7) 一类）；环境光强度 ≤ 主光的 5%。
2. **背景明度上限**：背景区域（非人物/非道具像素）最大亮度 ≤ 0.10 × 全帧最大亮度；背景亮度标准差 ≤ 全帧 5%（禁光晕渐变）。
3. **中间调压缩（直方图双峰）**：亮度直方图中，中间带 [0.35, 0.65] 像素占比 ≤ 25%；暗带 [0, 0.25) 占比 ≥ 40%。（强档默认；中档放宽到 ≥25% / ≤40%）
4. **光斑三处法则**：高光连通域（亮度 ≥ 0.9 × max）数量 ∈ [2, 5]，且每个连通域必须与"脸 / 手 / 关键道具"之一相交；人物背部的高光连通域数 = 0。
5. **贴平面构图**：主人物包围盒高度 ≥ 画幅高 80%；至少 1 个主体被画幅边缘裁切；地平线（若出现）不得高于画幅下缘以上 15%。
6. **定格瞬间**：每帧只允许 1 个"动作极值"（最大手势位移向量的方向唯一）；运动模糊核 = 0；手势向量的延长线在 ±15° 内指向叙事对象中心。
7. **暗部保细节**：暗区（亮度 < 0.15）内部亮度标准差 ≥ 1.5/255（非死黑）；纯黑像素（=0）占比 ≤ 10%（对应 §1-3 的"底色作中间调"）。

> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（见 §10）；3、5 两条与 `expansion.md` §1.2 的三条建议（光源仰角、背景明度上限 8%、贴平面）对齐。

### 8.3 野外样本（本机素材；未找到以卡拉瓦乔命名的卡）

- **来源**：`knowledge/domains/motion-graphics/origin/提示词全文.md`（15 张 10 秒 MG 卡语料，Claude Code · Opus 5.5 制作）。
- **检索结果**：以 `卡拉瓦乔|Caravaggio|伦勃朗|明暗|光|暗|影` 全目录 grep，**未命中任何以卡拉瓦乔（或明暗对照）命名的卡**；命中均为其他卡里的"光"字。
- **有价值的是"护栏冲突"**：该语料的**结构模板**把"硬阴影"列为默认退化行为，须在固定位置的「别做成」里封堵——第 40 行（模板说明：反向约束要封堵"默认塑料材质、**硬阴影**、运动模糊……"）与第 60 行（3D 卡："别做成：默认的塑料材质、**硬阴影**、全画面都清楚。"）。
  **点评**：这意味着 Lane B 的默认护栏**正好禁止**卡拉瓦乔模块的核心机制（硬光/硬阴影）。系统组合时必须在 prompt 里**显式覆盖**这条默认禁令（例如把"别做成：硬阴影"替换为"别做成：多光源、环境补光、背景发亮"），否则两个模块会互相抵消。`[史料]`（本机素材，行号已核）
- **状态**：`[史料]`（grep 于 2026-10-15；未找到外部"Caravaggio AI prompt"样本——web_search 全 provider 限流，见 §10）。

---

## 9. 参考资料（编号 ↔ 正文标注）

| # | 来源 | URL | 本机可达性（2026-10-15） |
|---|---|---|---|
| R1 | Wikipedia: Caravaggio（生平/年表/技法/影响链；三手来源，仅用于交叉核对与索引） | https://en.wikipedia.org/wiki/Caravaggio | ✅ read 200 |
| R2 | Wikipedia: Tenebrism（术语定义） | https://en.wikipedia.org/wiki/Tenebrism | ✅ read 200 |
| R3 | Wikipedia: Giovanni Baglione（1603 诽谤案证词引文、敌意传记背景） | https://en.wikipedia.org/wiki/Giovanni_Baglione | ✅ read 200 |
| R4 | The Met (Heilbrunn Timeline), Keith Christiansen, "Caravaggio (Michelangelo Merisi) (1571–1610) and His Followers", 2003-10 | https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers | ⚠️ 直读 429（限流）；**Wayback 快照 ✅**：https://web.archive.org/web/20250219231149/https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers |
| R5 | National Gallery London —《The Supper at Emmaus》NG172（in-depth 技法段） | https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus | ✅ read 200 |
| R6 | National Gallery London —《Salome receives the Head of John the Baptist》NG6389（in-depth 晚期风格段） | https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-salome-receives-the-head-of-john-the-baptist | ✅ read 200 |
| R7 | National Gallery London — 艺术家页（生平叙事 + "painted straight onto the canvas"） | https://www.nationalgallery.org.uk/artists/michelangelo-merisi-da-caravaggio | ✅ read 200 |
| R8 | Musei Vaticani — Pinacoteca, Sala XII《Caravaggio, Deposition》 | https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/la-pinacoteca/sala-xii---secolo-xvii/caravaggio--deposizione-dalla-croce.html | ✅ read 200 |
| R9 | Galleria Borghese 藏品目录 —《Giovane con canestra di frutta》inv. 136（2012 底层草图发现） | https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta | ✅ read 200 |
| R10 | Galleria Borghese 藏品目录 —《David con la testa di Golia》inv. 455（铭文/自画像/incisioni 诊断） | https://www.collezionegalleriaborghese.it/opere/david-con-la-testa-di-golia | ✅ read 200 |
| R11 | Andrew Graham-Dixon, *Caravaggio: A Life Sacred and Profane*（Penguin 2010）官方摘录页 | https://www.andrewgrahamdixon.com/extract/caravaggio-a-life-sacred-and-profane.html | ✅ read 200 |
| R12 | Galleria Borghese 藏品目录 —《Autoritratto in veste di Bacco (Bacchino malato)》inv. 534（Baglione 1642 引文"nello specchio"） | https://www.collezionegalleriaborghese.it/opere/autoritratto-in-veste-di-bacco-bacchino-malato | ✅ read 200 |
| R12b | Musei Vaticani — Pinacoteca, Sala XII 房间页（R8 的父页） | https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/la-pinacoteca/sala-xii---secolo-xvii.html | ✅ read 200 |
| R13 | Wikipedia: The Entombment of Christ (Caravaggio)（构图分析 + 被临摹史：Rubens/Fragonard/Géricault/Cézanne） | https://en.wikipedia.org/wiki/The_Entombment_of_Christ_(Caravaggio) | ✅ read 200 |
| R14 | BBC News — "Caravaggio's crimes exposed in Rome's police files"（2011-02-18；含 1604 侍者报案英译） | https://www.bbc.com/news/world-europe-12497978 | ✅ read 200 |
| R15 | Through Eternity Tours — "The Seven Crimes of Caravaggio"（1603 审讯引文、马耳他除籍用语 "putridum et foetidum membrum"） | https://www.througheternity.com/travel-guide/seven-crimes-caravaggio-rome | ✅ read 200 |
| R16 | The Art Story — Caravaggio（转引 Bellori 1672 英译与 Gombrich；二手，引文须回查） | https://www.theartstory.org/artist/caravaggio/ | ✅ read 200 |
| R17 | Literary Review — Jonathan Keates 评 Helen Langdon《Caravaggio: A Life》(1998) | https://literaryreview.co.uk/works-of-faith-hope-and-eroticism | ✅ 可读开头（付费墙） |
| R18 | Internet Archive — Helen Langdon, *Caravaggio: A Life*（全文借阅） | https://archive.org/details/caravaggiolife00lang | ⚠️ 未直读（检索命中，未打开） |
| R19 | Uffizi —《Bacchus》 | https://www.uffizi.it/opere/caravaggio-bacco | ⚠️ 未直读（由 [R12] 外链） |
| R20 | Met 藏品页 —《The Musicians》435844 /《The Denial of Saint Peter》437986 | https://www.metmuseum.org/en/art/collection/search/435844 | ⚠️ 未直读（由 [R4] 外链；Met 站直读限流） |
| R21 | 本机素材：`knowledge/domains/motion-graphics/origin/提示词全文.md`（L40、L60 护栏条目） | 本地路径 | ✅ grep 命中（见 §8.3） |

**交叉核对（≥2 条关键事实，两条独立来源）**

1. **"无纸上素描、直接在画布上画 + incisions 定位"**：NG《以马忤斯》in-depth（[R5]："not a single drawing… survives"、"incised freehand lines into the still malleable priming"、abbozzo 深棕笔绘）**×** Galleria Borghese《捧果篮的男孩》（[R9]：2012 年分析发现"直接画在画布上的底层草图"，印证 "dal naturale"）**×** Wikipedia（[R1]："scoring basic guides directly onto the canvas with the end of the brush handle"）。三条来源分属两家馆方著录与百科，独立。**结论：CONFIRMED（但需加精确化：不是"零准备"，而是"准备都发生在画布上"——笔绘底稿 abbozzo + 刻线 incisions + 高度预谋构图）。**
2. **"硬光机制＝画外高处单光源、无反射、背景近黑"**：Met 转引同代批评家（[R4]："focused light source from high up, without reflections… walls painted black"）**×** Bellori 1672（[R16]："placing a lamp high so that the light would fall straight down"）**×** NG（[R5]："A strong light from the left… casts a shadow on the blank wall behind Christ, almost like a reverse halo"）。**结论：CONFIRMED**（两条同代记录 + 一条馆方观察；注意 [R16] 为二手转引，见 §10）。
3. **1603 年诽谤案与证词**：Wikipedia "Giovanni Baglione"（[R3]：诉讼时间、当事人、Caravaggio 被判有罪并关押 Tor di Nona 两周、证词原文）**×** Through Eternity（[R15]：同段证词的英文表述与"Baglione 胜诉"叙述）。**结论：CONFIRMED（两条最终都源自 1603 年法庭文书，视为同源双引；已在 §5-1 注明）。**
4. **《大卫》自画像与铭文**：Galleria Borghese 藏品页（[R10]：Manilli 1650 记载、'H[umilit]AS O[ccidit] S[uperbiam]' 读法）**×** Wikipedia（[R1]："the severed head of the giant, which is again Caravaggio"）。**结论：CONFIRMED。**

---

## 10. 缺口与待验证

1. **原话几乎为零（结构性缺口，不是没查到）**：除 1603 年审讯那一句外，未找到任何书信/笔记/画论（已查：[R1][R11] 均称其文字留世极少；Graham-Dixon 明说"只有一句"）。§5 的其余条目均为同代转述或档案，**不可当画论使用**。
2. **Bellori 引文回查**：§5-3 用的是 [R16]（The Art Story）所载英译；**未回查 Bellori 1672 原书（Borea 编 1976 版）页码**。待办：找到 Bellori《Le vite》"Caravaggio" 节的原文页码。
3. **Met 馆方专文**：本机直读全程 429（curl 亦 429），仅经 Wayback 2025-02-19 快照读取 [R4]；引文作者（"同代批评家"）Met 未具名——**该段原始出处待考**（常见说法指向某 17 世纪评论，但本档案未证实，不写死）。
4. **死亡情形四说并存且互斥**：热病 [R1]／他杀（Tomassoni 家族或骑士团复仇）[R1]／铅中毒（2010 骨骼研究）[R1]／那不勒斯斗殴伤口引发的金黄色葡萄球菌败血症（2018 研究）[R1]；另有 [R14] 的"医院病床"说与传记的"海滩"说冲突。**结论：未决**——本档案不采信任一版本，只记录分歧。
5. **量化阈值为本项目归纳、未实测**：§4 的 P2/P3 百分比、§8.2 的 7 条规则阈值均未对原作做像素测量（分母＝假想参考帧），也未跑过渲染器；wave3 的 A-12 组合实验（建议主题"暴风雨中的海边灯塔"）可按 §8.2 逐帧自查后回改。
6. **未直读的 URL**：[R18]（Langdon 全文）、[R19]（Uffizi《Bacchus》）、[R20]（Met 藏品页）——均为检索/外链命中，未打开，标 `[UNVERIFIED]`。
7. **出生地分歧**：米兰（现代共识 [R1]）vs Caravaggio 镇（旧说；[R16] 仍写 Caravaggio）——已在 §0 双注。
8. **web_search 全 provider 限流**（2026-10-15）：外部"Caravaggio AI prompt"样本未能采集（§8.3 因此只有本机素材与护栏冲突分析）；替代通道用了 Brave HTML、Bing HTML、Wikipedia API、Wayback、Google Books API（429）。DuckDuckGo/Mojeek/Ecosia 均反爬拦截（实测）。
9. **画家页之外未核**：St John's Co-Cathedral（马耳他《斩首》）的馆方页未直读，§0 第 4 件作品的馆藏信息取自 [R1]。

---

## 自审四段

### A. 早产出
骨架（0–10 全节标题）在开工第 7 次工具调用时即落盘 `knowledge/domains/painters/dossiers/caravaggio.md`（write，1554 bytes）；随后按"来源到手即回填"的顺序逐节覆盖，最终版覆盖模板全部节（0–10 + 自审）。

### B. 反驳（挑最强结论逐条试推翻）

| # | 结论 | 反驳动作（跑过什么） | 判定 |
|---|---|---|---|
| 1 | "卡拉瓦乔不做任何准备、不打底稿直接画" | 逐篇复读馆方文本：[R5] 同时写了 "not a single drawing… survives" **和** abbozzo/incisions；[R9] 记 2012 年发现画布上的底层草图；[R1] 记"用笔杆尾端在画布上划定位线" | **WEAKENED → 改写**：正文（§2-1/2/3、§9 交叉核对 1）改为"**准备全部发生在画布上**（abbozzo 笔绘底稿 + incisions 刻线 + 高度预谋、少 pentimenti），不是纸上素描/卡通" |
| 2 | "他是'从自然写生'的纯粹现实主义者" | 查 [R12]：Bacchino 的姿势引用 Peterzano 草图与 Dürer 版画；[R13]：《下葬》引用米开朗基罗《圣殇》/自画像与拉斐尔构图；[R1]：钦佩拉斐尔 | **WEAKENED**：正文 §6.1 增列"古典与前人的直接引用（可考）"；§3 不写"拒绝传统"，只写"反理想化 + 物理真实优先" |
| 3 | "他死于 1610 年热病/铅中毒" | 交叉 [R1]（四说并存 + 2010 骨骼研究 + 2018 败血症研究）与 [R14]（档案展："死在医院病床，不是海滩"） | **OVERTURNED（作为单一结论不成立）**：正文不采信任一死因，§10-4 只记录分歧 |
| 4 | "Bellori 的'灯置于高处'引文可直接引用" | 追源：该英译见 [R16]（通俗艺术网站），未回查 Bellori 1672 原书 | **WEAKENED**：§5-3 与 §7-10 均标注"二手转引、原书页码回查未做"，并进 §10-2 缺口 |
| 5 | "1603 年那句'没有画家认为 Baglione 画得好'是他关于绘画的唯一一句话" | 核 [R11] 原文："only one solitary sentence from him on the subject of painting — … elicited when he was under interrogation for the capital crime of libel"；核 [R3] 证词两处引文 | **CONFIRMED（措辞收窄）**：正文写"唯一被现代学者认定为'他关于绘画的话'的记录"，不写"他一生只说过一句关于画的话" |

### C. 机械验证（原样粘贴；检查器：`read` 直读 3 条关键 URL，见下）

**① National Gallery London《The Supper at Emmaus》in-depth（R5）——`read` 返回头部逐字：**
```
URL: https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus
Content-Type: text/html
Method: native

---
canonical: https://www.nationalgallery.org.uk/paintings/michelangelo-merisi-da-caravaggio-the-supper-at-emmaus
meta-author: The National Gallery, London
meta-description: Michelangelo Merisi da Caravaggio, The Supper at Emmaus, 1601. Read about this painting, learn the key facts and zoom in to discover more.
meta-viewport: width=device-width, initial-scale=1, shrink-to-fit=no
title: Michelangelo Merisi da Caravaggio | The Supper at Emmaus | NG172 | National Gallery, London
```
正文命中（逐字）：`"In many of his works he also incised freehand lines into the still malleable priming (or undercoat) to mark out where figures were to be placed, and presumably to allow models to resume their poses."`；`"not a single drawing that can be firmly attributed to Caravaggio survives"`。

**② Galleria Borghese《Giovane con canestra di frutta》inv.136（R9）——`read` 返回头部逐字：**
```
URL: https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta
Content-Type: text/html
Method: native

---
meta-author: Galleria Borghese
meta-og:site_name: collezionegalleriaborghese.it
meta-og:title: Merisi Michelangelo detto Caravaggio - Giovane con canestra di frutta
meta-og:type: website
meta-og:url: https://www.collezionegalleriaborghese.it/opere/giovane-con-canestra-di-frutta
title: Giovane con canestra di frutta - Merisi Michelangelo detto Caravaggio
```
正文命中（逐字）：`"In seguito ad alcune analisi effettuate sull'opera nel 2012, è stata evidenziata la presenza di un disegno preparatorio sottostante, uno schizzo fatto dall'artista direttamente sulla tela che conferma quanto testimoniato dalle fonti antiche a proposito del modo di Caravaggio di dipingere 'dal naturale'."`

**③ BBC News（R14）——`read` 返回头部逐字：**
```
URL: https://www.bbc.com/news/world-europe-12497978
Content-Type: text/html
Method: native

---
canonical: https://www.bbc.com/news/world-europe-12497978
meta-article:section: Europe
meta-description: An exhibition of documents at Rome's State Archives throws vivid light on Caravaggio's tumultuous life in the city, 400 years ago.
meta-og:title: Caravaggio's crimes exposed in Rome's police files
meta-og:url: https://www.bbc.com/news/world-europe-12497978
title: Caravaggio's crimes exposed in Rome's police files - BBC News
```
正文命中（逐字）：`"Statement to police by Pietro Antonio de Fosaccia, waiter, 26 April 1604:"`；`"He did not die alone on a beach after escaping from his creditors and the police, as some of his biographers say, but in a hospital bed."`

（三条 URL 的完整 `read` 返回体量较大，此处按"头部 meta 块 + 正文命中句"原样摘录，未改一字；完整输出见本会话工具回执。）

**④ 附加机械核对（Met 通道）**：`curl -A "Mozilla/5.0…" https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers` → `429 34224`（限流确认）；`read https://web.archive.org/web/2024/https://www.metmuseum.org/essays/caravaggio-michelangelo-merisi-1571-1610-and-his-followers` → 200，快照正文含 `"Caravaggio pushed the figures up against the picture plane and used light to enhance the dramatic impact and give the figures a quality of immediacy."`

### D. 小结（≤14 行）
- **已确立**：10 条视觉指纹、10 条技法规则、8 条创作原则、6 个控制参数（各三档 + 与伦勃朗的分工口径）、8 条"原话"（全部注明性质：审讯/敌意传记/档案/友人墓志）、10 条馆方与学者深度分析、21 条参考来源（其中 15 条本机 ✅ 直读）。
- **已确立（交叉核对 4 组）**：①"准备全在画布上"（NG × Borghese × Wikipedia）；②硬光机制（Met 引同代 × Bellori 转引 × NG）；③1603 审讯证词（Wikipedia Baglione × Through Eternity，同源双引）；④《大卫》自画像与铭文（Borghese × Wikipedia）。
- **已改写/被削弱**：①"零准备直接画"→"准备在画布上"；②"纯粹写生现实主义者"→补古典引用；③Bellori 引文降为二手转引；④"唯一一句话"措辞收窄。
- **被推翻**：单一死因（四说并存 + 医院床 vs 海滩冲突）——正文不采信任何版本。
- **未知**：Bellori 原书页码；Met 所引"同代批评家"是谁；Langdon/Uffizi/Met 藏品页未直读；外部 AI prompt 样本未采（搜索通道全限流）。
- **下一步**：wave3 A-12 用 §8.1 正/负向 prompt 跑同一主题对照（建议"暴风雨中的海边灯塔"），按 §8.2 的 7 条逐帧自查；组合实验时**必须**处理 §8.3 的护栏冲突（默认禁硬阴影）。
- **我仍赌错的是什么**：§4/§8.2 的量化阈值（背景 ≤10%、中间调 ≤25%、贴平面 ≥80%）是我从馆方文本与作品归纳的**未实测**参数——若对照实验显示原作分布更宽，以实测分布修正（分母＝该实验全部帧）。
