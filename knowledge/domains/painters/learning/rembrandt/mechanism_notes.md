<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-rembrandt；原正文 SHA-256 `e471b509968811ca5bc4fb1e96bbde4829c41404a101a069c59742eb560b5c7e`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-rembrandt — mechanism_notes（光暗分区 + 群像叙事机制）

> **task_id:** LEARN-rembrandt · **lane:** learning · **repo:** READ-ONLY @ `f008952365a77e140cbda3f3959d43ef000f9a22`
> **契约来源:** 00-GOAL.md L9/L24（A-30、How to Think 须区分自述与推断）、02-EXECUTION-PLAN.md Lane B L62-66（观察→决策→机制→参数→一次练习→反例→自检）、本次交办（强调「伦勃朗光暗分区 + 群像叙事机制」、near-miss 11 行 / L107 8对 stale 作为 known-open、RF1-RF4 作为 accepted basis）。
> **底本:** 依赖 内部证据 160cd8fbf96ed1ee（未公开；来源记录由维护者保留）（**ACCEPTED**，review-evidence.md verdict accepted）＋ 只读本机 dossier / corpus / 卡 / conflicts.md。**不重审、不改 repo、不复制 AUDIT 产物。**
> **级别纪律:** §4 六参数与 §8.2 七规则均为本项目 `[归纳]`（dossier L76 / §10 L320 自标「未对原作做像素测量」）；RF1-RF4 是 AUDIT 已接受的联网全文佐证（HTTP 200、bytes+sha 记录在 `risk_fetches/fetch_index.json`），本 shard **不重新联网、不重设分母**。练习为建议练习，效果未经人评。

---

<a id="db-source-line-10"></a>
## A. 核心机制一：光暗分区（伦勃朗光的「连续衰减 + 心理」）— 本次点名重点

> **分工写死（dossier L6 / L70 / L108 / 卡 L93 / §8.1 L252）**：伦勃朗 = **光的连续衰减 + 心理（心理化光斑）**；卡拉瓦乔 = **光的开关 + 物理（硬光戏剧 / 舞台感）**。视觉结果重叠约 60%（`expansion.md` §0.2，本批最高），但机制互斥。**本模块 P1 强档 = 连续衰减**；卡拉瓦乔 P1 强档（无反射硬光）与 P3 强档（中间调抽空 / 直方图双峰）为其专属，本档一律不采用（RE-DIV-01 / AUDIT result §7）。RF1 为这条分工提供外部佐证：NG 艺术家页逐字含 `patterns of light and shadow, rather than simply lighting one side and shading the other`。

<a id="db-source-line-14"></a>
### A.1 光暗分区的三层骨架（dossier §1 / §2 / §4）

| 层 | 机制 | 可判定量 / 判分口径 | 证据级 / 定位 | RF 佐证 |
|---|---|---|---|---|
| **分区 1 单光源 + 暗部塌陷** | 光自侧上方（常见左上）进入，画面内不出现光源；人物从暗里「浮」出；背景压至全帧最亮 ≤15%，但暗部保留微弱层次（非死黑） | 单光源；背景 ≤15% 最亮；暗区内部亮度 std ≥ 2/255（§8.2-3）；纯黑（≤0.03）≤5% | `[研究]` dossier L32（[R4][R1]）/ 卡 L9；`[归纳]` 阈值 §8.2-3 dossier L260 | RF1（NG `patterns of light and shadow`）间接支持「非一侧亮一侧暗」 |
| **分区 2 面部亮斑地图（签名）** | 用光与影的**图案**描述面孔，而非简单照亮一侧压暗另一侧；亮斑 3–7（强档 4–7）处集中于前额/鼻梁/颧骨/下巴/唇周；鼻梁最窄亮条；**眼窝必暗、表情读不准**→「面孔之后有活着的、思考的心智」 | §8.2-1：高光连通域（≥0.85×帧最大）∈[3,7] 且全部与面部/主体关键区相交；眼窝区平均亮度 ≤ 面部平均 60%；鼻梁亮带 ≤ 面宽 15% | `[研究]` dossier L33-34（[R1] 原话）/ 卡 L10-11；数量区间 `[归纳]` dossier L33 | **RF1 直接命中** `patterns of light and shadow`、`living, thinking mind`、`hard to read a precise expression`（AUDIT R-RF1） |
| **分区 3 连续衰减（非开关）** | 亮→暗为连续渐变、**无硬切边**；沿主光方向亮度单调下降（无跳变）；明暗边界过渡带 ≥8 px；亮斑边缘弥散 ≥15 px（P1 强档） | §8.2-2：亮度单调下降区间占比 ≥80%；过渡带 ≥8 px；相邻像素亮度跳变 >12% 的「阶跃边界」像素占比 ≤1% | `[归纳]` dossier L35（依据 [R1]+`expansion.md` §6-B2）/ 卡 L12；阈值 dossier L258 | **硬切即越界**：§8.1 中文说明 L253 判「出现硬切光斑 → 判卡拉瓦乔模块」 |
| **材质载体（厚涂 / 排线）** | 厚度地图与光斑地图重合：亮部厚涂到立体化（「用颜料塑皮肤」）、暗部薄画草图态；蚀刻排线＝同一明暗逻辑的**线条版**（加线压暗） | §8.2-4 亮部高频纹理能量 ≥ 暗部 1.5×；§8.2-5 线密度与亮度负相关 R²≥0.8、暗部叠 ≥2 方向交叉线 | `[研究]` dossier L37/L39、§2-2/3（[R3][R8][R10]）/ 卡 L13；`[归纳]` 阈值 dossier L261-262 | RF2（Rijksmuseum SK-C-5）含 `master of Impasto` 语境；RF1 含晚期宽笔触/调色板刀 |

> **机制一句话（dossier §6.3 L146）**：伦勃朗的风格 = **把卡拉瓦乔的「开关」升级成「调光器」**——同一族「从黑暗里打光」，被连续化（衰减代替切分）、心理化（光斑地图代替表情符号）、材质化（厚涂与排线各自成为光的载体）。提示词若只写 `Rembrandt lighting` / `chiaroscuro` 会丢两半：① 连续衰减的**梯度**才是身份（硬切即越界）；② 蚀刻排线是同一套明暗逻辑的线条版（约 300–350 件样本池，口径分歧见 dossier §10-1）。

<a id="db-source-line-25"></a>
### A.2 参数 → 规则的对齐（§4 P1-P6 ↔ §8.2 七规则）

> 全部 `[归纳]`、未实测（dossier L76 / L265 / §10 L320）；规则 1/2/3 对齐 P2/P1/P3，规则 5 对齐 P6；**与 `caravaggio.md` §8.2 对应规则互斥使用**（其 2/3 条为本模块负向）。「用法」照录 dossier L110：P1/P2/P3 定「是不是心理化的伦勃朗光」，P4/P5 定材质与色域，P6 只在版画/线条模式启用。

| 参数（默认 / 三档） | 判定面（§8.2 规则） | 失败条件（越界/退化） |
|---|---|---|
| **P1 衰减连续性 75%** 弱<4px 台阶 / 中 4–15px / 强 全画连续无硬切、单调、弥散≥15px | §8.2-2 衰减连续性 | 出现硬切光斑 / 亮暗两级无过渡 / 无反射单光源 → **判卡拉瓦乔（越界）**；无向柔边（sfumato）→ 违「渐变必须有方向」（与达·芬奇分工，卡 L100） |
| **P2 面部光斑地图 70%** 弱≤2处侧照 / 中 3–5处 / 强 4–7处成「地图」、眼窝必暗 | §8.2-1 光斑地图 | 亮斑连通域 <3 或 >7 / 眼窝不留暗 / 表情可被唯一分类 → 丢失「活着的思考的心智」 |
| **P3 暗部塌陷深度 65%** 弱≥25% / 中 10–25% / 强 ≤8–10% 但保微层次、亮暗比≥8:1 | §8.2-3 暗部活性 | 暗部死黑（std<2/255）/ 纯黑>5% / 中间调抽空、直方图双峰 → **越界到卡拉瓦乔 P3 强档** |
| **P4 厚涂与表面 60%** 弱平滑 / 中亮部见笔触 / 强宽笔触刮刀、近看崩坏远看成立 | §8.2-4 厚涂纹理 | 亮部高频能量 <暗部 1.5× / 近看不崩坏 → 退化为早期光洁风 |
| **P5 色域收窄 70%** 弱≥8簇 / 中 5–7簇 / 强 ≤4簇（赭棕黑暖黄）、高饱和仅 1–2 道具 | §8.2-6 色域 | 色相簇>6 / S>50%（强调色面积>5%）/ 明度动态 <8:1 |
| **P6 蚀刻排线梯度 55%**（版画/线条）弱轮廓浅阴影 / 中 3–4 档 / 强 线密度=f(明度) 连续 | §8.2-5 排线 | R²<0.8 / 暗部无交叉排线 / 最亮区留白>20% |

---

<a id="db-source-line-40"></a>
## B. 核心机制二：群像叙事机制（「正在做事」/ 进行时群像）— 本次点名重点

> **馆方口径（[R2]）**：`Rembrandt was the first to paint figures in a group portrait actually doing something`（Rijksmuseum《夜巡》SK-C-5 对象页）。dossier §9 **CC-4 (L309) 明确标为「单源标注，不当定论」**；RF2 联网全文命中该句（AUDIT R-RF2），AUDIT 仍**按单源口径不升级为定论**——本 shard 沿用，**accepted basis 不等于定论**。

<a id="db-source-line-44"></a>
### B.1 机制拆解（dossier §1-9 / §1-10 / §3-3 / §2-1 / §12）

| 子机制 | 内容 | 可判定量 | 来源 / 级别 / 定位 | 证据强度 |
|---|---|---|---|---|
| **M-G1 进行时动作** | 组画里 ≥2 个可读的进行时动作（队长下令开步走、卫兵列队、枪响三段：装填/击发/清理），而非排排站的静态肖像 | 组画中 ≥2 个可读进行时动作 | `[研究]` dossier L40（[R2]）/ §7-4 L204；RF2 全文 | **单源**（CC-4），RF2 佐证 |
| **M-G2 光＝叙事聚光灯** | 光聚焦关键细节（队长的手势、背景小女孩＝连队吉祥物），其余卫兵在暗部列队但动作可辨 | 高光落在叙事关键物；亮斑连通域仍 ∈[3,7]（§8.2-1 对齐 P2） | `[研究]` dossier L40 / §7-4；§4 P2 光斑地图 | RF2 含 `used the light to focus on particular details, like the captain's gesturing hand and the young girl` |
| **M-G3 视线/手势分配** | 《蒂尔普解剖课》「七人各自看着不同方向」（[R42]）；《呢商行会理事》「全体抬头看向观众，像被到访打断」（[R47]）；单人「手势与目光是叙事主语、沉入思考」（`immersed in thought`） | 视线向量图不聚成一点；半身单人 ≥70% 画幅、动作幅度小 | `[研究]` dossier L41（[R1][R4]）/ §12-2/8 L430/L465 | 馆方口径 |
| **M-G4 戏剧瞬间「一束光＋一个动作」** | 《伯沙撒的盛宴》墙上字＋后仰的国王＋众人视线；`Deep shadows and shafts of brilliant light`；冷色作为点火例外 | 自查色相簇 ≤6 但允许 1 个高饱和道具 | `[研究]` dossier §12-3 L435（[R4]）/ §1-1 L32 | 馆方口径 |
| **M-G5 自述侧「运动/情感最大值」** | 1639 致 Huygens 信 `die meeste ende die naetuereelste beweechgelickheijt`（最充分、最自然的运动/情感）——**唯一被学界公认的画论性自述**；Binstock 认为兼指内在情绪与外在动作 | —（这是 `[自述]`，不是可测量阈值） | `[自述]` dossier §3-1 L62 / §5-1 L115-120；corpus #4 L36-42；AUDIT R-§3-01 | Worp 排印×Strauss 转写双转录一致（CC-2）；英译分歧已记 |
| **M-G6 同代反证「宁愿多放点光」** | Van Hoogstraten 1672 评《夜巡》：比全场都强，「但我宁愿他往里面多放一点光」——证明暗部策略当年即激进、且被同代抱怨 | —（史料，不是规则） | `[reported speech]/[contemporary record]` corpus #11；dossier §7-9 [R15] | 一手转述；「《夜巡》当年受批评」的当代证据 |

> **群像叙事与光暗分区的咬合**：M-G2 是两机制的接口——「光斑地图」（脸/手/关键道具，§2-1 L47 先定光斑地图再压暗其余）在群像里被复用为**叙事聚光灯**。先光后暗的取舍序列（dossier §2-1 `[归纳]`）：先定光斑地图（脸/手/关键道具）→ 再定亮部材质 → 最后把背景与其余压暗、抽掉中间调但保留下限层次。练习里「光只允许落在 3 个关键物上」（§12-4 L439）即把 P2 的 [3,7] 连通域约束接到叙事关键物上。

<a id="db-source-line-57"></a>
### B.2 群像叙事练习阶梯（建议练习，非已证实收益）

| 阶 | 一次可做的练习 | 自检（用 §8.2 可判定量） | 反例 / 失效 |
|---|---|---|---|
| 1 | 写一张 5 人「出发前一刻」分镜，至少 2 个进行时动作（§12-4 L439） | §8.2-2（衰减连续）、§8.2-1（亮斑连通域 [3,7] 与关键物相交） | 排排站静态肖像 → 无 M-G1；硬切光 → 越界卡拉瓦乔 |
| 2 | 画七人圆桌、每人视线方向不同（§12-2 L430）；画视线向量图检查不聚成一点 | 临摹只做「三个亮块」（脸/手/纸）再压暗其余；亮斑连通域 [3,7] | 视线聚成一点 → 退回旧式行会肖像 |
| 3 | 画 5 人「抬头瞬间」，视线全部出画（§12-8 L465）；红/白/黑三色骨架 | P4 强档「近看崩坏远看成立」；一双手 ≤10 笔 | 近看工整 → 未达晚期厚涂 |

---

<a id="db-source-line-67"></a>
## C. near-miss 11 行 reality 与 L107「8 对」stale — **known-open，不作为缺陷关闭**（本次点名）

> 这是 AUDIT 判 **R-CF-02 `partial`** 的跨文件计数漂移；review-evidence.md §4 已独立复现并确认「drift real, correctly reported, not fixed — read-only lane respected」。本 LEARN shard **作为 known-open 携带，不修正、不关闭、不改写任何 repo 或 AUDIT 文件**。

| 事实 | 实测 / 定位 | 判定 |
|---|---|---|
| `conflicts.md` §4 near-miss 表**实为 11 编号行**（#1–#11），其中 **#9 / #10 / #11 带「（2026-10-16 补）」** | [conflicts.md](../../../../cross/conflicts.md) L347-L357（11 行）；review-evidence.md §4 复现 | **11 行是 present reality** |
| 模块卡 `rembrandt.md` **L107** 仍写「conflicts.md（18 条 C + N1–N9 + **near-miss 8 对**）」 | [rembrandt.md](../../modules/rembrandt.md) L107；AUDIT R-CF-02（locator `L107`） | **8 对是 stale**（补 #9-#11 之前的旧计数），`partial` |
| `grep -niE 'rembrandt|伦勃朗' conflicts.md` = **0 命中**；18 条 C-row + 11 near-miss 均无 rembrandt | AUDIT R-CF-01；review-evidence.md §4；`conflicts_rows_checked=29` | 对 rembrandt 本身 = **空集**（事实，不是缺陷） |
| 另两处 AUDIT 已报漂移（同属 known-open，本 shard 不处理）：INDEX L31 记 `17|12|3|6` vs 实测 corpus 11/2/5（#11 双标）；dossier §9 [R22] L301 记「4 文件」vs 清单、内部台账与文件系统记录均为 6 文件 | AUDIT R-CF-03 / RESULT §6；review-evidence.md §4 | `partial`，报告不修 |

- **为何不在本 shard 关闭**：本 lane 写权限仅 内部证据 37afdf379f4b3624（未公开；来源记录由维护者保留），repo READ-ONLY；AUDIT-rembrandt 是 **ACCEPTED 依赖**（复用而非重审）。计数口径的订正属 CONFLICT / MODULE-CARD owner 与 INVENTORY lane（AUDIT unresolved #1/#2/#3 已交出 next_discriminating_action）。
- **对学习路径的实际影响**：**无**。11 行 near-miss 中 0 行涉及 rembrandt，本档规则文本（§4/§8.2/分工条款）保持 `supported`；练习阶梯（§B.2）不引用任何 near-miss 数值端点。known-open 只在 `RESULT.md` / `receipt.unresolved` / [claim_evidence_map.md](claim_evidence_map.md) 登记，不进入决策步骤的「已核实」栏。
- **诚实边界**：不把「8 对」当作 11 行的别名，不把「0 冲突行」包装成「已解决冲突」；两者都是待 owner 订正的历史口径。

---

<a id="db-source-line-84"></a>
## D. RF1-RF4 作为 accepted basis（不重新联网、不升级为定论）

> AUDIT 4 次外部回源（`/risk_fetches/*.bin`，HTTP 200、bytes+sha256 见 `fetch_index.json`）；review-evidence.md §3 已**逐字节重算 4/4 match**、RF2 锚句命中。本 shard 把 RF 当作**已接受的上游证据**引用，不重新抓取、不重设分母、不把「文本命中」升级为「原作像素真值」。

| RF | 来源 / 命中文本 | 佐证的 claim | 本 shard 用法边界 |
|---|---|---|---|
| **RF1** NG 艺术家页 `2a920f21…`（89,994 B） | `patterns of light and shadow … rather than simply lighting one side and shading the other`、`the living, thinking mind behind the face`、`hard to read a precise expression` | §1-2 面部亮斑地图 / §1-3 眼窝留暗 / 分工条款（AUDIT RE-RF-01 / R-RF1） | 支持「机制文本自洽 + 外部定性佐证」；**不支持** 3–7 处等 `[归纳]` 数值（NG 只给定性「图案」） |
| **RF2** Rijksmuseum SK-C-5 `08721ed2…`（299,117 B） | `Rembrandt was the first to paint figures in a group portrait actually doing something`、`used the light to focus on particular details` | §1-9 / §3-3 群像叙事（AUDIT R-RF2） | 仍按 dossier §9 CC-4 **单源口径**，不写死为定论；RF2 是 HTML 文本，**不是像素**（见 §E 反例） |
| **RF3** Wikipedia Rembrandt `67c5cd63…`（842,161 B） | `1606`、`Rembrandt never went abroad` | §0 生卒 / §3-7 不赴意大利（AUDIT R-RF3） | 佐证生平框架，不进入练习判定 |
| **RF4** nl.wikipedia Saskia `683f8aa0…`（159,382 B） | `22 juni` / `Juliaanse kalender` / `2 juli` / `10 juni` / `ondertrouw` | §11.4 婚期两历并记（AUDIT RE-114-01 / R-RF4）；A-60 GOALS L66 | 佐证「两历并记」口径，与视觉机制/学习路径无关；登记为 accepted basis 的组成 |

---

<a id="db-source-line-97"></a>
## E. 反例（concrete counterexample，AUDIT RESULT §7 已接受的 `[inference]`）— 不升级为已推翻

- **目标规则**：§4 P1 强档（dossier L81「全画明暗均为连续渐变、无硬切边；亮斑边缘弥散 ≥15 px」）＋ §8.2-2（dossier L258 / 卡 L50「相邻像素亮度跳变 >12% 的阶跃边界像素占比 ≤1%」）。
- **具体候选反例**：用本档旗舰作品 1642《夜巡》本身（§1-9 / §7-4 即引它）。RF2 与 dossier L204/L473 描述**队长着黑衣**下令、光聚焦其手势与背景女孩、卫兵在暗部列队。黑衣对受光的手正是「无硬边 / ≤1% 阶跃」规则要禁的高对比局部边界；若把 P1 强档 + §8.2-2 字面施加于整帧，队长黑袖/剪影边与亮手周围的锐利亮暗转换**可能**超过 12% 阈值且 >1% 像素——即在作者自己的典范作品上违反规则。`[inference]`。
- **为何不推翻（AUDIT 已判）**：规则作用域是**生成/代码艺术帧的逐帧自查**，不是对 1642 画布像素直方图的声称（§8.2 L265）；dossier §10 L320 预注册此防御（「量化阈值为 [归纳]、未实测 … 分母＝假想参考帧；wave3 组合实验 A-12 可按 §8.2 逐帧自查后回改」）。RF2 是 HTML 文本非像素，本 lane 未跑像素测量。
- **诚实判定**：`supported（规则文本内部一致、作用域受限）` + `unverified（原作像素级真值）`。下一步判别动作 = 对参考帧做像素测量，属 **A-12 组合实验 lane**，本 LEARN 不越权。
- **学习路径落点**：练习阶梯收口时跑 §8.2 七条逐帧自查；「出现硬切 → 换模块或降档」按 §8.1 中文说明 L253 执行，而不是去改这条规则。

---

<a id="db-source-line-107"></a>
## F. 等级 / 覆盖诚实边界

- 全部 §4 六参数与 §8.2 七阈值为 `[归纳]`、未实测；RF 命中只证明**外部文本可回源**，不证明数值。
- 17 条 corpus 引文（Worp 排印 × Strauss 转写；拉丁文以 Binstock 英译为准、原稿未直读）外部真伪 `unverified`（AUDIT unresolved）；本 shard 只声称「本机档案内自洽 + 定位可寻址」。
- 6 张公开图外部许可页真实性与像素内容 `unverified`（AUDIT RE-RT-02）；本 shard 无 `image_seen`、不复制像素。
- 练习效果未由人评价；`human_review.status=not_applicable`，全部为**建议练习**，不写「已证实学习收益」（01-AUDIT.md §8.1 L273）。
- `review:null`：本产物 `submitted`，待独立审者（非作者）裁定；作者不自接受。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
