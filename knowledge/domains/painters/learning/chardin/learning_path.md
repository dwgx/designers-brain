<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-chardin；原正文 SHA-256 `504f838b4b4be4f3ae5b1e145d9eb05d0fed88fceebd4ecdb9a4f69a591a4bfb`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-chardin — 学习路径卡（Jean Siméon Chardin）

> 任务 `LEARN-chardin`（**A-30** 单片）· lane=learning · 依赖 内部证据 382bee103ab3d7a6（未公开；来源记录由维护者保留）（attempt 2，磁盘 `receipt.json` `status=accepted` / `review.verdict=accepted` / `review-evidence.md` Verdict=**accepted**）——本 lane **复用 ACCEPTED 审计的 locator 纪律与分母结论，不重审、不改仓库/审计产物**。
> 本文按 **A-30 §8.1 形状**（`01-AUDIT.md:269-273`）：前置知识 → 重点作品及来源 → 要观察的机制 → 具体练习（3 阶梯）→ 可观察结果 → 常见失败 → 下一步 → 使用边界。
> **证据底座**：仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`（只读）。开工 `sha256sum` 实测（见 `RESULT.md §0`）：
> - card [chardin.md](../../modules/chardin.md) = `df57eb65…8c640`
> - dossier [chardin.md](../../dossiers/chardin.md) = `323f72f3…a832`
> - corpus [chardin.md](../../dossiers/_corpus/chardin.md) = `7b11679f…6495`
> - `_images/manifest.md` = `5698124d…b470` ｜ `conflicts.md` = `314a24da…bbef` ｜ `ops/GOALS.md` = `2727d1f0…1144`
> - 上游 内部证据 5508b414a6316524（未公开；来源记录由维护者保留） = `6e304471…ba9d`、`RESULT.md` = `65af849e…5e91`、`review-evidence.md` = `c36f91a8…752b8`、`coverage-manifest.json` = `dc588fed…cc15`
>
> **等级口径（全文一致，沿用 dossier `L5` / corpus `L4`）**：`[自述]`（corpus `[self-written]` 书信）/ `[自述转记]`（`[reported speech]` 他人转记本人话语）/ `[史料]`（`[archive]`/`[contemporary record]` 同时代记录/档案/馆藏）/ `[研究]`（馆方与艺术史研究 `[research]`）/ `[归纳]`（本项目从作品与文字归纳的**可判定操作规则/参数**，**不是史料、不是作者自述、不是原图像素实测**）/ `[推测]`（本路径**不使用**）。夏尔丹**无画论、无书信集、无日记**（`dossiers/chardin.md:L10`、`_corpus/chardin.md:L5`）——凡「他心里如何」一律按项目宪章降级为可执行操作规则（`dossiers/chardin.md:L10`、`00-GOAL.md:L9` 红线）。
>
> **本片强调（brief 指定，逐节落地）**：① **静物·质感层积 + 弱光源机制**（§1 K2/K3、§3 M1/M2、§4 三阶梯、[how-to-think.md](how-to-think.md)、[mechanism_notes.md](mechanism_notes.md)）——拆成「放而不混的层积笔触（质感层积）」+「漫射侧光、无戏剧性光源、暗部暖褐有层次（弱光源）」两半，**二者须成对使用**；② **Cochin/Diderot 闭环逐字证据**（§2 专段、§3 M1、§8 B2、`claim_evidence_map.md §B`）——把 Cochin 1780 信、Diderot 1763 沙龙、Goncourt 1864、Met/NGL 现代图录串成闭环，逐字引文见 `corpus`；③ **「引文 37/37」分母辨析**（§2 专段、§8 B3、`claim_evidence_map.md §D`）——**37/37 = dossier 自审 C 归一化引文抽查（D:478–516），不是语料条数；语料分母 = 28**（`grep -c '^### '`=28）；GOALS A-92 / INDEX L74 同句并列两个分母，本片诚实分栏、不混用；④ **17 张图 = 卢浮宫 11 + Met 3 + NGL 3**（§2 专段、§8 B4）。
>
> **练习状态（硬边界）**：以下所有练习均为 **建议练习**（`[归纳]`，本项目设计）。学习收益**尚未由人完成或评价**，不写「已证实学习收益」「已验证有效」（`01-AUDIT.md:273`）。每条练习只给「可操作动作 / 自查 / 完成定义」，不声称经过学习实验。本 lane `image_seen=0`（未目检原图像素）、无真人评价。

---

<a id="db-source-line-20"></a>
## 1. 前置知识（先知道什么，才看得懂这些练习）

| # | 前置知识 | 等级 | locator |
|---|---|---|---|
| K1 | **「夏尔丹风格」= 静物的触感——厚涂质感 + 谦卑日常的诗意**（`roster §2.4` 原文），不是「暗调静物滤镜」：同屏 ≥3 类材质各有专属表面处理（铜暖光/玻璃湿亮/面包颗粒）、反光软而宽、表面保留颜料质地；物体贴前缘、背景简化中性场；悬浮静默、重复变体。能力落点 = 「让无生命之物获得存在感」。`[归纳]`（能力定位）+ `[研究]`（视觉证据） | `[归纳]`/`[研究]` | `dossiers/chardin.md:L9,L23,L39-L48`（§0 一句话定位 / §1 指纹 10 条）；`modules/chardin.md:L7-L13`（浓缩 5 条） |
| K2 | **「质感层积」（tactile layering）= 放而不混的笔触一层层堆出材质的手感**（brief 强调①，本项目 `[归纳]` 机制标签，档案未用此四字词）——它由四段可回源的操作纪律合成，**不是「一律点彩」**：① 放而不混（颜色一笔一笔并置、不预先调匀；Raynal 1750「mosaïque… point carré」）；② 近看崩坏 / 退远成立（Diderot 远近检验）；③ 堆叠 + 罩染 + 揉合、表面密实（无裸露画布、厚涂与透明层并存）；④ 材质专属处理（金属宽软反光带/玻璃透射+反光/面包颗粒点触/瓷温润渐变，禁止两材质共用同一处理）。**质感层积是可见输出半。** | `[归纳]`（机制标签）+ `[史料]`/`[研究]`（四段各自来源） | `_corpus/chardin.md:L76-L81`（Q10 Raynal）、`L90-L95`（Q12 Diderot 远近）、`L199-L204`（Q27 Met「never disguise the rough texture of paint」）、`L192-L197`（Q26 Rosenberg）；`dossiers/chardin.md:L39,L40,L48,L59,L60,L62,L63,L65`（§1-1/-2/-10、§2-4/-5/-7/-8/-10）、`L208`（§8.2-6 材质专属）、`L210`（§8.2-8 完成度）；`modules/chardin.md:L44,L49,L51` 逐字一致 |
| K3 | **「弱光源」（soft / diffused light）= 光为触感服务的漫射侧光**（brief 强调①，本项目 `[归纳]` 机制标签，档案未用此三字词）——① 漫射侧光（多自左上/前方）、**无戏剧性光源、无画外单光**；② 暗部暖褐/灰绿、**保留层次、无纯黑大块、无冷蓝主导**；③ 全画中调为骨架、亮暗过渡带柔；④ **弱 ≠ 无方向、≠ 平光**——夏的光仍有方向与「反光网络」（每物带邻物之色光），只是不独立成图案。**弱光源是不可见前提半；与 K2 成对：层积提供可读表面，弱光让表面可读而不被硬阴影吃掉。** | `[归纳]`（机制标签）+ `[归纳]`/`[研究]`/`[史料]`（四段证据） | `dossiers/chardin.md:L42,L43,L45`（§1-4 柔和明暗 / -5 / -7）、`L87,L88`（§3.1 触感档：漫射软光 + 有层次暖暗部）、`L205,L206,L207,L212`（§8.2-3/-4/-5/-8 注）、`L196`（§8.1 中文强度建议 P4 60%）；`modules/chardin.md:L24,L46,L53`；`_corpus/chardin.md:L83-L88`（Q11 Diderot「substance même des objets… air et lumière」）；AUDIT [claim_evidence_map.md](claim_evidence_map.md) S1-4/S1-7（**均 partial：`[归纳]` 未像素实测**） |
| K4 | 三条可判定主线规则（本路径骨架，全部 `[归纳]`、未对原作像素测量）：§8.2-1 触感表面可辨笔触面积 **30–80%**、粒径 2–8px、**禁统一方向角度族**（方向直方图峰值 ≤35%）；§8.2-2 反光形态**宽软形**（圆度 ≤0.7 或长宽比 ≥2、σ ≥2px）、**跨物反光 ≥2 处**、禁 1–3px 点状系统；§8.2-3 纯黑 ≤0.5%、阴影色相暖（H20–60° 或灰绿 60–120°）、禁 200–250° 冷蓝主导、暗部层次标准差 ≥2/255。 | `[归纳]` | `dossiers/chardin.md:L203,L204,L205`（§8.2-1/-2/-3）；`modules/chardin.md:L44,L45,L46` 逐字一致；阈值性质 `modules/chardin.md:L53`、`dossiers/chardin.md:L212,L281`（§10-7） |
| K5 | §4 六参数与「是不是夏尔丹」判据：**P1 触感密度 70% / P2 反光网络 65% / P3 材质对比 70% / P4 光质柔和 60% / P5 空间浅度 65% / P6 表面整合度 50%（时期滑轨）**；**P1+P2 两条 ≥ 中档才成立**（D:112/C:66）。P3/P4 定材质与光档，P5 定构图，P6 是工作流参数。全部 `[归纳]`。 | `[归纳]` | `dossiers/chardin.md:L105-L110`（§4）、`L112`（用法）；`modules/chardin.md:L59-L64`、`L66` 逐字一致 |
| K6 | **Cochin/Diderot 闭环（brief 强调②，逐字证据底本）**：夏尔丹没有画论，机制规则的「证据环」由四类文字互相支撑——**Cochin 1780 致 Haillet 信**（Q1「sentiment」句逐字 + 「rupture de tones / accord magique」反复重画）、**Diderot 1763 沙龙**（Q11「substance même des objets / air et lumière」、Q12「Approchez-vous, tout se brouille… Éloignez-vous, tout se crée」、Q13「the great magician」）、**Goncourt 1864**（Q18「un travail systématique de reflets… envelopper chaque chose de la teinte et de la lumière de tout ce qui l'avoisine」）、**现代 Met/NGL 图录**（Q27「never disguise the rough texture of paint」、Q28「keeping objects slightly out of focus」）。四者共同支撑 §1-2 放而不混、§1-3 反光网络、§1-4 柔和明暗、§3-2/3-3/3-4，并回锚到 §8.2-1/2/3。**逐字原文见 §2 专段与 `claim_evidence_map.md §B`**；本 lane 复用 AUDIT 的 4 份 fetch 缓存结论（Q1/Q27 逐字核、Q11 英文核），**不重访外部 URL**。 | `[自述转记]`/`[史料]`/`[研究]`（逐条按 corpus 类型） | `_corpus/chardin.md:L11-L16`（Q1）、`L83-L88`（Q11）、`L90-L95`（Q12）、`L97-L102`（Q13）、`L134-L139`（Q18）、`L199-L204`（Q27）、`L206-L211`（Q28）；AUDIT `claim_evidence_map.md:L129-L130`（闭环专节）、`RESULT.md §2`/`§5`（F1/F3 fetch）、`review-evidence.md §2` |
| K7 | **「引文 37/37」分母辨析（brief 强调③，口径红线）**：GOALS A-92（G:88）与 INDEX L74 同句写「语料 **28** 条…引文 **37/37**」——**两个不同分母**：`28` = [chardin.md](../../dossiers/_corpus/chardin.md) 的 `### ` 语料条数（本 lane `grep -c '^### '`=28 复核、AUDIT+审者独立复跑 28）；`37/37` = **dossier 自审 C「引文抽查（37 条 vs 本机源文件，归一化后逐字命中）」**（D:478 表头 / D:516 `--- 37/37 ---`），是作者 wave20 对自己 `_scratch` 源文件的归一化字节匹配抽查，**不是语料条数、不是语料引文条数**。AUDIT 与审者（review-evidence.md §3）确认该 37/37 块存在但**未重跑**（`_scratch` 不在只读仓库），记为**作者自审主张、非本 lane 重认证**；28 为独立核实。INDEX L74 的「3\|5\|11」是把 archive+contemporary 折叠的分组口径（实测逐条类型 2/4/1/10/11=28），属解读差异非缺陷。 | `[史料]`（GOALS/INDEX 记录）+ `[归纳]`（分母辨析） | `ops/GOALS.md:L88`；`dossiers/_corpus/INDEX.md:L74`；`dossiers/chardin.md:L478,L516`（自审 C）；`dossiers/chardin.md:L541,L548`（自审 D 复跑 `37/37`）；AUDIT `RESULT.md §2`、[claim_evidence_map.md](claim_evidence_map.md) H-A92/H-IDX、`review-evidence.md §3`、§5 F2（H-IDX 措辞瑕疵） |
| K8 | **17 张公开图 = 卢浮宫 11 + Met 3 + NGL 3（brief 强调④）**：`_images/manifest.md` L564–580 恰 17 行 `chardin/…jpg`；机构拆分 11/3/3（本 lane `sed -n '564,580p'` 复核、AUDIT+审者独立复跑）。权利：Public domain 9 + PD-Art 5 + CC0 2 + CC0(Met Open Access) 1 = 17，unknown 0（AUDIT `rights_review.md` 逐张 verbatim 标签）；chardin **不是 private-layer 艺术家**，`images_public=17` 是事实，另 `_private` 研究副本层（hi-res 10 + PDF 2，3 待补）不改变公开计数。GOALS A-92「图库 17 张全 PD/CC0（卢浮宫 11）」一致。 | `[史料]`（馆藏/权利记录） | `_images/manifest.md:L564-L580`；`dossiers/chardin.md:L31`（§0 语料/图库）、`L7`（来源口径）、`L441`（自审 A 图库先行）；AUDIT `RESULT.md §7`、`coverage-manifest.json`、`rights_review.md`、`review-evidence.md §4` |
| K9 | 三条分工预检（组合前必读，`[归纳]`；**conflicts.md 无 chardin 具名行**，C 条按 ID 引用、ID 均解析）：**vs 维米尔**（光学室内 vs 触觉静物，5 判据 ≥2 轴；夏站软光侧/宽软反光/暖褐阴影）、**vs 塞尚**（结构 vs 质感，形体处理 N4 不可拆、不得折中「半几何半触感」）；组合预检 C-01（软光侧顺风）/C-05（笔触「可见但非全覆盖」显式取值）/C-11（按 N7 单列「反光带」类）/C-12（暖土色系显式取值）/C-13（暖褐/灰绿阴影）。 | `[归纳]` | `dossiers/chardin.md:L85-L97`（§3.1）、`L212`（§8.2 注）；`modules/chardin.md:L69-L75`（冲突注记）；`conflicts.md:L32,L36,L42,L43,L44`（总表）、`L305,L311,L314,L326`（N1/N3/N4/N7）；AUDIT `claim_evidence_map.md §conflicts drift`（报导不修） |

**前置知识边界**：K2「质感层积」、K3「弱光源」是**本项目 `[归纳]` 机制标签**，档案与语料从未使用这两词；它们只用来把可回源的操作纪律组织成学习对象，不得写成「夏尔丹提出『质感层积』」。K4/K5 全部数值是 `[归纳]` 操作阈值，不是作者说过的话、不是原图像素实测（AUDIT `coverage-manifest.json` 记本轮 `image_seen=0`、dossier `L281` §10-7）。K6 的「sentiment」句虽经 fetch1 逐字核，但**原档私人文书未回查**（dossier `L275` §10-1、AUDIT unresolved #1），逐字证据是**转录层**逐字、非一手档案。

---

<a id="db-source-line-38"></a>
## 2. 重点作品及来源（引用现有记录，不新增作品、不重新取证）

> 作品与权利信息**沿用 dossier §0（5 件带 URL）/ §12（10 件临摹清单）/ §9（R1–R35）与 `_images/manifest.md`**；AUDIT `rights_review.md` 已逐张核 17 张公开图权利。本 lane **不重访外部 URL、不目检原图**（无 `image_seen`），外部可读性沿用 AUDIT 的 4/4 fetch 结论（Q1/Q27 逐字、Q11 英文、La Raie/2024 新闻稿）。

| 阶梯 | 对应作品（§12 编号 / §0 编号） | 看什么 / 与本路径主线的关系 | 等级 | locator |
|---|---|---|---|---|
| 阶梯一（质感层积：放而不混 + 材质分工） | §12-1《La Raie》1728（卢浮宫 INV 3197）；§12-2《Le Buffet》1728（卢浮宫 INV 3198）；§12-3《The Silver Tureen》约1728–30（Met 59.9） | 入院两作 = 「触感宣言」：鳐鱼内脏红/蓝/白 + 猫的警觉，同屏 5+ 材质各用专属笔法；银汤碗「生/死、生食/熟食」平衡 + 「never disguise the rough texture of paint」。对应 K2、§8.2-1/-2/-6、P1/P2/P3 强档 | 作品信息 `[史料]` / 练习映射 `[归纳]` | `dossiers/chardin.md:L25,L26,L27`（§0 关键 5 件）、`L383-L386`（§12-1）、`L388-L391`（§12-2）、`L393-L396`（§12-3）、`L153`（§7-1 Met 条目） |
| 阶梯二（弱光源 + 反光网络） | §12-7《The Water Cistern / La Fontaine》1733（NGL NG1664）；§12-10《Le Panier de fraises》1761（卢浮宫 RFML.PE.2024.7.1）；§0-5《Soap Bubbles》约1733–34（Met 49.24） | 铜缸的宽软反光 + 肉红映在铜上 + 门洞第二空间（荷兰装置但不破坏静默）；草莓篮的颗粒/霜光、水杯的「水感只用透明与反光」；肥皂泡球面反射映两件环境物。对应 K3、§8.2-2/-3、P2/P4 | 同上 | `dossiers/chardin.md:L29`（§0-5）、`L413-L416`（§12-7）、`L428-L431`（§12-10）、`L398-L401`（§12-4 Soap Bubbles）、`L159`（§7-7 NGL 水缸）、`L162`（§7-10 草莓篮） |
| 阶梯三（悬浮静默 + 边界自律） | §12-5《The Young Schoolmistress》约1737（NGL NG4077）；§12-6《The House of Cards》约1740–1（NGL NG4078）；§12-9《La Pourvoyeuse》1739（卢浮宫 MI 720）；§12-8《Le Bénédicité》1740（卢浮宫 INV 3202） | 「keeping objects slightly out of focus」用清晰度差表心理差；搭牌看空白背面、专注本身为题材；「temps mort」动作中停、餐前将开始的瞬间。对应 §8.2-7、P5/P6、反叙事；粉彩自画像（1771/1775）与《Le Gobelet d'argent》作第 11/12 扩展练习 | 同上 | `dossiers/chardin.md:L28`（§0-4）、`L403-L406`（§12-5）、`L408-L411`（§12-6）、`L423-L426`（§12-9）、`L418-L421`（§12-8）、`L433`（§12 组合练习建议 + 第 11/12 件） |
| 跨艺术家比较（下一步，不在阶梯内） | §3.1 vs 维米尔 / 塞尚；§6 物性谱系（荷兰静物 → 夏 → 写实主义/塞尚 → 莫兰迪/弗洛伊德/马蒂斯） | 与维米尔比「高光形态/表面/阴影色相」，与塞尚比「笔触系统/形体轮廓/完成度」（≥2 轴）；A-30 总路线寻址用 | `[归纳]` | `dossiers/chardin.md:L85-L97`（§3.1）、`L134-L147`（§6）、`L433`（§12 组合练习建议）；`modules/chardin.md:L73-L75` |

<a id="db-source-line-49"></a>
### Cochin/Diderot 闭环 — 逐字证据（brief 强调②，本片所有引用的原文）

> 口径：夏尔丹**无画论、无书信集、无日记**（`_corpus/chardin.md:L5`）。下表每条逐字照录 corpus 原文（法文旧拼写 `reconnoissoit`/`quoy` 等不改），`类型` 按 corpus `L4` 图例；「支撑哪条机制」列指向本片 K2/K3/K4 与 AUDIT claim map。4 份 fetch 缓存的 sha 与锚点核对见 AUDIT `review-evidence.md §2`（本 lane 复用、不重访）。

| 环节 | 逐字原文（verbatim） | 出处 / 类型 / locator | 支撑 | 核验状态 |
|---|---|---|---|---|
| **A. Cochin 1780 信·sentiment 句** | « On se sert des couleurs, reprit M. Chardin, mais on peint avec le sentiment. » | Q1 `_corpus/chardin.md:L11-L16`；Cochin 致 Haillet 信 1780，经 rivagedeboheme.fr 转录；`[reported speech]` / `[自述转记]` | §3-2「用感受作画而非用颜色」（D:75）；K2 的「不预先调匀」原则层 | **fetch1 逐字核**（`94105c40…87e3`，含 `reconnoissoit`/`Avec quoy donc`）；**原档私人文书未回查**（§10-1）→ 转录层逐字 |
| **A′. Cochin 1780 信·反复重画** | 「反复重画，直到达到**色调的断裂（rupture de tons）**与最终的**魔法般的和谐（accord magique）**」 | `dossiers/chardin.md:L58`（§2-3）、`L76`（§3-3）；经 [R27]/[R33]/[R22] 转录；`[史料]` | K2 层积的「慢工/反复」半；§1-2 放而不混的工序理由 | fetch1 旁证「repeignait… rupture de tons… accord magique」（AUDIT `RESULT.md §5` F1）；转录层 |
| **B. Diderot 1763·物的实体** | « Ô Chardin ! Ce n'est pas du blanc, du rouge, du noir que tu broies sur ta palette : c'est la substance même des objets, c'est l'air et la lumière que tu prends à la pointe de ton pinceau et que tu attaches sur la toile. » | Q11 `_corpus/chardin.md:L83-L88`；《Salon de 1763》论《Le Bocal d'olives》，fr.wikipedia 转录；`[contemporary record]` / `[史料]` | K2「材质手感 + 颜料质地」、K3「光为触感服务」的总纲；§1-1 | **fetch3 英文旁证**（Met「grind 'the very substance'… dip your brush in air and light」，`ed46f94b…d99b`）；法文逐字为转录层 |
| **B′. Diderot 1763·远近检验** | « Approchez-vous, tout se brouille, s'aplatit et disparaît ; éloignez-vous, tout se crée et se reproduit. » | Q12 `_corpus/chardin.md:L90-L95`；同上；`[contemporary record]` | K2「放而不混」的判读：近看崩坏/退远成立 → §8.2-1 可辨笔触 30–80% 的语义来源 | 法文逐字**未独立 web 复取**（AUDIT `claim_evidence_map.md:L130` 明示保持 supported-via-corpus-transcription，不升一手）；fetch3 英文「dip your brush in air and light」为旁证 |
| **B″. Diderot·大魔法师** | « Denis Diderot called Chardin 'the great magician'. » | Q13 `_corpus/chardin.md:L97-L102`；NGL 2018 图录（Whitlum-Cooper）转述；`[contemporary record]`（转述） | 与 A 的「accord magique」呼应，闭环的另一锚点 | NGL 图录转述，非 Diderot 原句 |
| **C. Goncourt 1864·反光网络** | « …il les lie, les assemble, les corrige, les caresse avec un travail systématique de reflets, qui… semble envelopper chaque chose de la teinte et de la lumière de tout ce qui l'avoisine. » | Q18 `_corpus/chardin.md:L134-L139`；Gazette des Beaux-Arts 1864，fr.wikipedia 转录；`[research]` | K2/K3 的「反光网络」：每物带邻物色光 → §8.2-2 跨物反光 ≥2；§3-4 | 转录层；与 §2-5（D:60）同记 |
| **D. Met 图录 2015·粗糙质地** | « Fur, feathers, orange rind, and reflective silver are visually convincing yet never disguise the rough texture of paint… » | Q27 `_corpus/chardin.md:L199-L204`；Baetjer 2015《The Silver Tureen》/《The Water Cistern》；`[research]` | K2「表面保留颜料质地」、§8.2-1 可辨笔触；「触感」的现代馆方确认 | **fetch3 逐字核**（`ed46f94b…d99b`）；CC0/Open Access 权利基础同页 |
| **D′. NGL 图录 2018·略失焦 / 平凡之美** | « Chardin's distinctive method of keeping objects slightly out of focus… the extraordinary beauty with which he endowed ordinary objects. » | Q28 `_corpus/chardin.md:L206-L211`；NGL 2018（NG4077 页/艺术家条目）；`[research]` | K3「弱光源」的清晰度维度（略失焦 ≠ 硬边锐焦点）；谦卑母题 | 转录层；AUDIT [claim_evidence_map.md](claim_evidence_map.md) Q28 supported |

> **闭环读法**：A（Cochin：用感受、反复重画至色调断裂）→ B（Diderot：磨的是物的实体与空气光、走近糊退远成）→ C（Goncourt：系统性反光把并置色「联结」而不「混」）→ D（Met/NGL：粗糙质地从不掩饰、略失焦）**互相印证同一件事**——表面是并置的、可读的、带邻物光的、为触感服务的；这正好是 K2（质感层积）+ K3（弱光源）两半，并回锚到可执行 §8.2-1/2/3。**闭环是证据环、不是画家自述链**：B/C/D 全是他人文字，A 是他人转记本人话语；不得写成「夏尔丹自述其层积法」。

<a id="db-source-line-66"></a>
### 「引文 37/37」分母辨析（brief 强调③，口径诚实）

| 数字 | 是什么 | 分母/证据 | 本片用法 |
|---|---|---|---|
| **28** | [chardin.md](../../dossiers/_corpus/chardin.md) 的语料条数（`### ` 头） | 本 lane `grep -c '^### '` = **28**；`- 类型：`=28、`- 来源：`=28、`- 中文意译：`=28；逐条类型 self-written 2 / reported speech 4 / archive 1 / contemporary record 10 / research 11 = **28**。AUDIT + 审者独立复跑 28 | **语料分母 = 28**；GOALS A-92「语料 28 条」、INDEX L74 首列「28」指此 |
| **37/37** | dossier **自审 C 的归一化引文抽查**：37 个引文片段 vs 本机 `_scratch` 源文件，归一化后逐字命中 37 个 | `dossiers/chardin.md:L478` 表头「引文抽查（37 条 vs 本机源文件，归一化后逐字命中）」、`L479-L515` 逐条 `HIT | …`、`L516` `--- 37/37 ---`；自审 D `L548` 复跑记「引文复抽（归一化）: 37/37」 | **作者自审主张**，不是语料条数；AUDIT 与审者确认块存在但**未重跑**（`_scratch` 不在只读仓库，`RESULT.md §9.5`、`review-evidence.md §3`），本片沿用「照实携带、不重认证」 |
| **11 / 3 / 3** | 17 张公开图的机构拆分 | `_images/manifest.md:L564-L580`；GOALS A-92「卢浮宫 11」 | 见 K8；与 28/37 完全无关的第三个分母 |

> **GOALS A-92（G:88）原句同时含两个数**：「语料 **28** 条（Cochin/Diderot 闭环）+ 图库 17 张全 PD/CC0（卢浮宫 11）… 引文 **37/37**」——AUDIT `RESULT.md §2` 已辨析「hint conflates two different denominators」，审者 `review-evidence.md §3` 判 **VERIFIED**。本片**分栏携带**：语料查引用到 Q1–Q28（28 条），自审 37/37 只作「作者 wave20 自检记录」提及，**绝不把 37 当语料条数、也绝不把 28 写成 37/37 的命中数**。INDEX L74「3\|5\|11」为折叠分组（实测 2/4/1/10/11=28），AUDIT 审者 §5 F2 记为 H-IDX 措辞瑕疵（非阻塞），本片照实登记、不改仓库。

---

<a id="db-source-line-78"></a>
## 3. 要观察的机制（把参数变成「看什么」）

| 机制 | 参数（等级） | 观察点（可判定） | 失败形态（与 §6 呼应） | locator |
|---|---|---|---|---|
| **M1 质感层积**（brief 强调①；可见输出半） | §8.2-1 可辨笔触 30–80% / 粒径 2–8px / 方向峰值 ≤35% `[归纳]`；§8.2-6 材质 ≥2 类各有专属处理 `[归纳]`；放而不混/远近检验/表面密实 `[史料]`/`[研究]`（Q10/Q12/Q27） | 近看是否「马赛克/针脚」、退后是否聚合成物；同屏金属/玻璃/面包/瓷是否用了**不同笔法**（防「一律点彩」）；有无大面积平滑渐变 / 裸露画布 / 硬线；笔触是否**无统一方向族**（与塞尚 4–8 角度族区分） | 把层积读成「一律点彩」→ 违 §8.2-6、材质串味（F2）；把笔触抹平/罩染成渐变 → 越界达·芬奇侧（C-05 对侧）；做成方向族化 tache → 越界塞尚（`modules/chardin.md:L67` ②） | `modules/chardin.md:L44,L49,L51,L53`；`dossiers/chardin.md:L203,L208,L210,L212,L39,L40,L48`；`_corpus/chardin.md:L76-L81,L90-L95,L199-L204` |
| **M2 弱光源 + 反光网络**（brief 强调①；前提半） | §8.2-2 高光宽软形（圆度 ≤0.7 或长宽比 ≥2 / σ ≥2px）、跨物反光 ≥2、禁 1–3px 点状系统 `[归纳]`；§8.2-3 纯黑 ≤0.5% / 阴影暖 H20–60° 或灰绿 60–120° / 禁 200–250° 冷蓝 / 暗部标准差 ≥2/255 `[归纳]`；P4 光质柔和 60% `[归纳]` | 光是否**漫射侧光、无戏剧性光源/无锐投影**；暗部是否暖褐/灰绿**且有层次**（非纯黑、非冷蓝平坦）；高光是否**宽软反光带**（非维米尔式 1–3px 点）；铜面是否映肉红、玻璃是否含红蓝（≥2 处跨物反光） | 画外单光 + 近黑背景 + 亮部只落主体 → 越界卡拉瓦乔（`L67` ③）；点状高光 + 平坦冷暗部 + 地砖网格 → 越界维米尔（`L67` ①）；把「弱」做成无方向平光 → 丢反光网络、退化普通暗调静物（§8.1 `L196` 警告） | `modules/chardin.md:L45,L46,L24,L62,L67`；`dossiers/chardin.md:L204,L205,L42,L87,L88,L196`；`_corpus/chardin.md:L83-L88,L134-L139`；`conflicts.md:L32,L42,L43`（C-01/C-11/C-12） |
| **M3 浅空间 + 中性场 + 悬浮静默** | §8.2-4 背景边缘密度 ≤前景 30% / 主体包围盒 ≥50% / 无地砖网格 `[归纳]`；§8.2-7 0 帧运动模糊 / 帧间差 Δ ≤1% / 动作中停 `[归纳]`；P5 65% `[归纳]` | 物体是否贴前缘、桌沿水平基线（可略斜）、背景是否为大块低细节中性半调；人物是否「动作中停」、无叙事/无动势线 | 纵深可读 + 背景细节 + 地砖网格 → 越界荷兰室内/维米尔；画进情节/道德剧/运动模糊 → 违反叙反叙事（§3-6）与静止规则 | `modules/chardin.md:L47,L50,L63`；`dossiers/chardin.md:L206,L209,L43,L46,L79`；`_corpus/chardin.md:L185-L190`（Q25 Démoris temps mort） |
| **M4 分工自律（横切，组合预检）** | vs 维米尔 5 判据 / vs 塞尚 5 判据（≥2 轴）`[归纳]`；C-01/C-05/C-11/C-12/C-13 + N1/N3/N4/N7 `[归纳]` | 组合时每轴是否只有一个持有者（N3）；反光按 N7 是否单列「反光带」类（不并入 C-11 点状计数）；形体处理是否守住 N4 不可拆；色相是否显式取「暖土」值 | 把维米尔平滑冷光 + 夏触感折中 → 双标准；把塞尚几何化 + 夏质感折中「半几何半触感」→ N4 违例；把「宽软反光」误计入点状高光 → C-11/N7 错判 | `dossiers/chardin.md:L85-L97,L212`；`modules/chardin.md:L69-L75,L67`；`conflicts.md:L305,L311,L314,L326`；AUDIT `claim_evidence_map.md §conflicts drift`（**conflicts.md 无 chardin 具名行，按 ID 引用、ID 全解析**） |

**观察纪律**：M1–M4 的阈值是 `[归纳]` 判据，用来给「建议练习」做自查，**不是对原画的事实测报告**（AUDIT `coverage-manifest.json` 记 `image_seen=0`，§4/§8.2 阈值未对原作做像素测量 = `dossiers/chardin.md:L281,L212`）。把「练习时自查通过」与「原作被证实如此」分开。**CE-1/CE-2 反例（AUDIT `RESULT.md §6`/`claim_evidence_map.md §反例`）照实携带**：晚期粉彩自画像（单头、中性场、P1 弱档、无 ≥2 跨物反光）按字面会被 D:112「P1/P2 ≥中档才成立」判「不是夏尔丹」；§2-7 粉彩「纯色平行笔触」与 §8.2-1「方向峰值 ≤35%」在介质未显式分栏时相冲。二者是**操作规则的边界反例、非归属错误**，AUDIT 未渲染验证、本片不修（见 §8 B5）。

---

<a id="db-source-line-91"></a>
## 4. 具体练习（3 阶梯；全部为「建议练习」`[归纳]`，未经人评）

> 作业顺序按机制两半设计：**先定弱光源与反光网络（M2，前提）→ 再在光内做质感层积（M1，输出）→ 最后做浅空间/静默与组合自律（M3+M4）**。每条含「可操作动作 / 自查 / 完成定义」，**不声称学习收益**。

<a id="db-source-line-95"></a>
### 阶梯一：material layering on a front-edge table（先定材质分工，再放而不混地堆）
- **目标机制**：M1（质感层积）+ §8.2-1/-6、P1/P3 强档；取 §12-1/2/3 为参照。
- **动作**：取《La Raie》/《Le Buffet》/《The Silver Tureen》为参照（`dossiers/chardin.md:L383-L396`）。摆「一铜器 + 一玻璃器 + 一食物（面包/果）+ 一瓷/织物」共 4 件于贴近前缘的台面。**动笔前先写一张材质分工卡**（`[归纳]` 练习设计，非史料）：规定金属=宽软反光带、玻璃=透射+反光、食物=颗粒点触、瓷=温润渐变，**四种笔法不得互串**。然后**颜色一笔一笔并置、不预先调匀**（Raynal Q10）、近看保留颗粒与并置色块；表面堆厚涂 + 局部罩染但不抹平、不露画布（§1-10/Q26）。
- **自查（可判定）**：可辨笔触面积是否落在 30–80%、粒径 2–8px、方向直方图峰值 ≤35%（无统一角度族）；四件物体是否用了四种可区分的表面处理；有无大面积平滑渐变 / 裸露画布 / 硬线；「近看崩坏、退远成物」（Q12）是否成立。
- **完成定义**：四材质靠笔法可区分、近观有颜料颗粒、退看聚合成物、未触发 §8.2-1/-6 失败形态；材质分工卡与成稿可对照。
- **来源**：`dossiers/chardin.md:L383-L396,L39,L40,L48,L203,L208,L210`；`_corpus/chardin.md:L76-L81,L90-L95,L192-L197,L199-L204`；`modules/chardin.md:L44,L49,L51`。练习映射 `[归纳]`。

<a id="db-source-line-102"></a>
### 阶梯二：wrapped diffused light + cross-object reflections（弱光源 + 反光网络）
- **目标机制**：M2 + §8.2-2/-3、P2/P4；取 §12-7/10 与 §0-5 为参照。
- **动作**：取《The Water Cistern》/《Le Panier de fraises》/《Soap Bubbles》为参照（`dossiers/chardin.md:L413-L416,L428-L431,L398-L401`）。**先把光定死**：单一漫射侧光（多自左上/前方），**禁止画外戏剧光、禁锐投影**；暗部只用暖褐/灰绿、保留层次（禁纯黑、禁冷蓝）。然后在阶梯一的成稿上**织反光网络**：铜面至少映一处邻物色（肉红/果）、玻璃/球面至少含一处邻物色（红/蓝）——**≥2 处跨物反光**；所有高光画成**宽软反光带**（非 1–3px 圆点）。水杯/肥皂泡的「水感/球感」只用透明与反光表达，不加轮廓硬线。
- **自查（可判定）**：纯黑像素 ≤0.5%、阴影色相落 H20–60° 或 60–120°（无 200–250° 冷蓝主导）、暗区亮度标准差 ≥2/255；高光连通域圆度 ≤0.7 或长宽比 ≥2、边缘 σ ≥2px、无 1–3px 点状系统；跨物反光 ≥2 处且可对应邻物色相；光是否「包裹」而非「打光」。
- **完成定义**：无硬边投影/无纯黑、暗部暖而有层次、宽软反光带与 ≥2 处跨物反光成立、未滑向卡拉瓦乔（画外单光）或维米尔（点状高光/冷暗部）。
- **来源**：`dossiers/chardin.md:L413-L416,L428-L431,L398-L401,L204,L205,L42,L87,L88,L196`；`_corpus/chardin.md:L83-L88,L134-L139,L206-L211`；`modules/chardin.md:L45,L46,L24,L62,L67`。练习映射 `[归纳]`。

<a id="db-source-line-109"></a>
### 阶梯三：shallow neutral ground + suspended time + boundary discipline
- **目标机制**：M3 + M4（§8.2-4/-7 / C-01 / C-05 / C-11 / C-12 / C-13 / 四条越界警报 / **CE-1·CE-2 介质边界**）。
- **动作**：取《The Young Schoolmistress》/《The House of Cards》/《La Pourvoyeuse》/《Le Bénédicité》为参照（`dossiers/chardin.md:L403-L411,L418-L426`）。把阶梯二的静物收进**浅空间 + 中性场**：物体贴前缘（包围盒 ≥50% 画幅）、桌沿水平（可略斜）、背景为单一中性半调、无地砖网格/无叙事细节。人物档（若加入）取「动作中停」：餐前/搭牌/放下面包喘气的间隙，目光离画、无动作矢量链、0 帧运动模糊。**组合自律（本阶梯硬要求）**：逐条守 `modules/chardin.md:L67` 四条越界警报——① 表面压平/点状高光/冷蓝阴影/地砖网格 → 维米尔；② tache 方向族/多轮廓/蓝网/裸露画布 → 塞尚；③ 画外单光 + 近黑背景 + 亮部只落脸/手 → 卡拉瓦乔；④ 平涂无笔触无高光 → 马蒂斯。C-05 按 N3 让「笔触可见度」轴单主；C-11 按 N7 把「宽软反光带」单列一类、不并入点状高光计数；C-12 显式取「暖土色系」值；C-13 取「暖褐/灰绿阴影」。**介质边界**：若做粉彩自画像变体（第 11 件扩展练习），必须显式标注「CE-1 的 P1/P2 门、CE-2 的方向族规则按介质分栏」，**不把晚期粉彩硬套进 D:112 的油画门**、不把规则空白写成「已完成」。
- **自查（可判定）**：背景区边缘密度 ≤前景 30%、主体包围盒 ≥50%、无透视网格；帧间差 Δ ≤1%（静物）/ 无动势线；冲突轴无双标准；四条越界警报逐条未触发；粉彩变体处附 CE-1/CE-2 介质注记。
- **完成定义**：浅空间中性场成立、静默无叙事、组合稿冲突轴单主、反光按 N7 单列、CE 反例以 open 注记携带而非掩盖。
- **来源**：`dossiers/chardin.md:L403-L411,L418-L426,L206,L209,L43,L46,L85-L97,L212`；`modules/chardin.md:L47,L50,L63,L67,L69-L75`；`conflicts.md:L305,L311,L314,L326`；AUDIT `RESULT.md §6`、`claim_evidence_map.md §反例`（CE-1/CE-2 均 `[inference]` 未渲染验证）。练习映射 `[归纳]`。

---

<a id="db-source-line-118"></a>
## 5. 可观察结果（每条练习交出什么，不是「学会了」）

| 练习 | 可观察产物 | 可判定自查（来自 §3/K4/K5） | 不算「学习收益」 |
|---|---|---|---|
| 阶梯一 | 一张四材质静物 + 一张材质分工卡 | 可辨笔触 30–80% / 粒径 2–8px / 方向峰值 ≤35% / 四种专属笔法可区分 / 近看崩坏退远成物 | 不写「已掌握质感层积」；只记成稿与自查表 |
| 阶梯二 | 阶梯一稿 + 反光网络标注（≥2 处邻物色） | 纯黑 ≤0.5% / 暖阴影 / 暗部标准差 ≥2/255 / 高光宽软形 σ ≥2px / 无 1–3px 点 / 跨物反光 ≥2 | 不写「已验证弱光源有效」；只记自查数值 |
| 阶梯三 | 浅空间成稿 + 组合预检表（C 轴/N 规则/越界警报/CE 注记） | 背景边缘密度 ≤前景 30% / 包围盒 ≥50% / Δ ≤1% / 冲突轴单主 / 四条越界未触发 | 不写「已证实组合规则」；CE-1/CE-2 保持 open |

> 全部为 `[归纳]` 建议练习的可观察**输出**，学习成效需固定样本包 + 真人评价（§8 B6、`01-AUDIT.md:273,308-310`），本 lane `human_review=not_applicable`。

---

<a id="db-source-line-130"></a>
## 6. 常见失败（F1–F8，全部 `[归纳]` 设计反例）

| # | 失败 | 触发点 | 纠正（回到哪条机制/练习） |
|---|---|---|---|
| F1 | **只练层积、不先定弱光源**（或反之）——两半拆开 | K2/K3 未成对 | 回 §4 作业顺序：先 M2（光+反光）再 M1（层积）；§8.1 `L196` 明言「缺 P2 退化普通暗调静物、缺 P4 滑向卡拉瓦乔」 |
| F2 | **「一律点彩」**：四材质共用同一颗粒点触 | M1 / §8.2-6 | 回阶梯一材质分工卡；金属宽软反光带、玻璃透射、食物颗粒、瓷渐变各归各 |
| F3 | **把「弱光源」做成无方向平光**：丢反光网络 | M2 / C-01 | 回阶梯二：弱 = 漫射但仍有方向 + 跨物反光，不是平光；§8.3 `L218` 防「把光压平为无方向平光」 |
| F4 | **点状高光 / 冷蓝平坦暗部 / 地砖网格** → 越界维米尔 | M2/M3 组合 | 回 §8.2-2/-3、§3.1 分工判据②③⑤（≥2 轴）；`modules/chardin.md:L67` ① |
| F5 | **画外单光 + 近黑背景** → 越界卡拉瓦乔；或 **tache 方向族/多轮廓** → 越界塞尚 | M4 组合自律 | 回阶梯三四条越界警报 + C-05/N3、C-12/N4、C-13 |
| F6 | **把「引文 37/37」当语料条数**，或把 GOALS A-92 两个分母混写 | K7 / brief ③ | 回 §2 分母辨析表：语料=28、自审抽查=37/37、图像=17；GOALS/INDEX 同句并列属不同口径 |
| F7 | **从画面外观反推作者心理**（「夏尔丹觉得…」「他想要表达…」） | 等级红线 | `00-GOAL.md:L9` 禁止；dossier `L10` 把一切「他心里如何」降级为操作规则；本片 `[推测]` 计数 = 0 |
| F8 | **把 CE-1/CE-2 规则空白写成「已完成」**，或把晚期粉彩硬套 D:112 油画门 | §3 观察纪律 | 回阶梯三「介质边界」：CE 以 open 注记携带，AUDIT 未渲染验证、本片不修 |

---

<a id="db-source-line-145"></a>
## 7. 下一步（A-30 总路线寻址 + 本片 open 的收口路径）

- **基础 → 进阶**：阶梯一（材质层积）→ 阶梯二（弱光源+反光）→ 阶梯三（浅空间/静默/组合自律）；与 §12 组合练习建议对齐（第 1/2/3 件材质清单、第 4/6/9 件悬浮时间、第 5/7/8 件门洞与互动、第 10 件晚期密度），第 11/12 件（粉彩自画像/银杯）作扩展（`dossiers/chardin.md:L433`）。
- **可替换分支**：人物档（genre）把 P5 保持中档、可加门洞第二空间（§8.1 `L197`、`§3.1` 边界注）；晚期档把 P6 升强（反光/透明/fondu 主导）；粉彩档按 CE 注记显式分栏、不套油画门。
- **跨艺术家比较**：vs 维米尔（高光形态/表面/阴影色相）、vs 塞尚（笔触系统/形体轮廓/完成度）按 §3.1 ≥2 轴；物性谱系（荷兰静物泥土气 → 夏 → 写实主义/塞尚 → 莫兰迪/弗洛伊德/马蒂斯）见 §6（`dossiers/chardin.md:L134-L147`）。
- **总路线（A-30）**：本卡为 76 位之一，供 `knowledge/domains/painters/program/learning/` 总路线编址；总路线说明基础/进阶顺序与跨艺术家比较方式（`01-AUDIT.md:271`）。
- **本片 open 的收口路径（不越权）**：① CE-1/CE-2 介质边界 → 实验 lane 按预注册 E 系列像素/生成实测、给 P1/P2 门加粉彩豁免或显式声明 §8.2 的 oil/canvas scope（AUDIT unresolved #4）；② §4/§8.2 阈值像素实测 → 视觉 lane（`dossiers/chardin.md:L281,L559`）；③ 原话原档（Cochin 1780 信 / 1778 d'Angivillier 信 / Artcurial €24,381,400）→ 来源刷新 lane（AUDIT unresolved #1/#2）；④ conflicts.md 无 chardin 具名行 + C-11/12/13 数值 locator 陈旧 → CONFLICT lane 单独写权（AUDIT unresolved #3）；⑤ 37/37 自审重跑 → 待 `_scratch/chardin/` 进入可读 lane（AUDIT unresolved #5）。本 lane **NO repo writes**，以上全部只登记。

---

<a id="db-source-line-155"></a>
## 8. 使用边界（B1–B8，诚实边界，不冒充完成）

- **B1 写入边界**：本 lane 仅写 内部证据 562c4c154356a09b（未公开；来源记录由维护者保留），仓库只读、无 git 操作、无子代理派发、无凭据（`receipt.json` `allowed_write_paths` / `spawns_allowed=false`）。`status=submitted`、`review=null`、作者不自接受；AUDIT-chardin 为 ACCEPTED 依赖，复用而非重审。
- **B2 Cochin/Diderot 闭环**是**证据环**（他人文字 + 转记），不是画家自述链；Q1 逐字经 fetch1 核但**原档私人文书未回查**（§10-1），Q12 法文逐字未独立 web 复取。本片不重访 4 份 fetch、不升级为一手档案认证。
- **B3 分母口径**：语料 **28**（独立核实）、自审 **37/37**（作者主张、未重跑）、图像 **17 = 11+3+3**（独立核实）——三个分母分栏，不互相换算。GOALS/INDEX 同句并列属不同口径，AUDIT+审者已辨析。
- **B4 图像真实性**：`image_seen=0`（未目检 17 张图像素），权利字段/文件存在沿用 AUDIT `rights_review.md` 逐张 verbatim 标签；不声称看过画面、不补许可页逐站复核。
- **B5 反例与阈值**：§4 六参数 / §8.2 八规则全 `[归纳]` 未对原作像素测量（分母＝假想参考帧，`dossiers/chardin.md:L281,L212`）；CE-1/CE-2 为 `[inference]` 边界反例、AUDIT 未渲染验证、本片不修不升级。
- **B6 练习效果**：全部为建议练习，无 human review、无真人学习成效数据，`human_review.status=not_applicable`，不写「已证实学习收益」（`01-AUDIT.md:273,308-310`）。
- **B7 等级纪律**：`[自述]`/`[自述转记]`/`[史料]`/`[研究]`/`[归纳]` 严格分栏；`[推测]` 计数 = 0；不从画面推作者心理（`00-GOAL.md:L9`）；「质感层积」「弱光源」是本项目机制标签、非史料术语。
- **B8 治理**：本包对 LEARN **无 bound contract**（仅 `AUDIT-chardin.contract.json` 存在），`execution_dedup_key=null`（submitted 允许）；verify-receipt.py 走 schema-only 提前返回，与 LEARN-sargent/monet 同口径。独立审者由单独 review-gate 承担。

## 同一条目的附页

- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
