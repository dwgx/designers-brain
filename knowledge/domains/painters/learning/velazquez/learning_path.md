<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-velazquez；原正文 SHA-256 `f84b396929b67c7e5c5757195834a7cc5a35e3cd901efa44d2acd8a81101d9a9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-velazquez — 学习路径（learning_path）

> A-30 Lane B 产物。依赖 ACCEPTED 内部证据 d33a99999ef7f3d3（未公开；来源记录由维护者保留）（RESULT.md / claim_evidence_map.md 66 行 / coverage-manifest.json / rights_review.md）作为证据底本，复用其 locator 纪律，**不重审**。repo 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22` READ-ONLY；写入仅在 内部证据 0507fe2a102aa784（未公开；来源记录由维护者保留）。NO repo writes / NO subagent spawns / NO credentials。
> 顺序遵循 `02-EXECUTION-PLAN.md` §Lane B L64「观察对象 → 创作决策 → 机制 → 参数 → 一次可做的练习 → 反例 → 自检」。
> 等级（照录 [velazquez.md](../../dossiers/velazquez.md) L5）：`[自述]` 本人写下/说出带出处 · `[史料]` 当时记录/馆藏 · `[研究]` 艺术史家/馆方分析 · `[归纳]` 本项目从作品与资料归纳的操作规则，**不冒充艺术家内心** · `[推测]` 低置信。
> **特殊口径（本 shard 根本前提）**：委拉斯开兹**无任何自述留世**——无书信、无画论、无日记（[velazquez.md](../../dossiers/velazquez.md) L6、[velazquez.md](../../dossiers/_corpus/velazquez.md) L6，AUDIT 判 `quote_self_written=0`）。因此本路径的 `[自述]` 计数恒为 **0**；20 条语料全部为他人转记/同时代记述/后世评价。凡「为什么这么决策」一律标作**输入材料**（`[史料]/[研究]`）或**研究者构造**（`[归纳]`），不得从画面外观反推作者心理（`00-GOAL.md` L9）。
> **全部练习为建议练习；练习效果尚未由人完成或评价，不写「已证实学习收益」**（`01-AUDIT.md` §8.1 L273）；`human_review.status=not_applicable`、无渲染实验、无像素测量、`image_seen=0`。

---

<a id="db-source-line-11"></a>
## §1 前置知识（先分清楚三类知识，标错等级 = 把推断冒充史料）

| 类 | 内容 | 等级 | 定位 |
|---|---|---|---|
| ① 无自述 | 全档 0 条 `[自述]`；§5 与 20 条 corpus 全为他人转记 | 结构性事实（AUDIT `VL-META-01` supported） | [velazquez.md](../../dossiers/velazquez.md) L6；[velazquez.md](../../dossiers/_corpus/velazquez.md) L6 |
| ② 史料/研究输入 | Pacheco《El arte de la pintura》(1649) 转引、Palomino《El museo pictórico》(1724/1795 OCR)、普拉多技术研究、Met/Prado/NG 馆方 | `[史料]/[研究]` | [velazquez.md](../../dossiers/velazquez.md) §9 R1–R23 (L219–L241) |
| ③ 本项目操作规则 | §3.1 分工条款、§4 六参数三档、§8.2 八条逐帧规则、§8.1 prompt | `[归纳]`（L63/L87/L206 明言「不冒充内心」「未对原作做像素测量」） | [velazquez.md](../../dossiers/velazquez.md) L74–L99 / L195–L206 |

**brief 强调点 ①：奠定「光的三档机制」**——系统内「光」的持有者分工（[velazquez.md](../../dossiers/velazquez.md) §3.1 L76，`roster.md` §2.6 写死）：

- **卡拉瓦乔 = 光的开关 + 物理**（硬光戏剧）；
- **伦勃朗 = 光的连续衰减 + 心理**；
- **维米尔 = 荷兰光学**（单侧窗光 + 点状高光）；
- **委拉斯开兹 = 光的第三档：画室与空气**（多光源柔化的画室光 + 可被看见的空气）。

§3.1 写死「本模块固定为『环境光（画室）+ 空气 + 银灰调』，不得复制另三者的签名机制」，并给出三对判分轴（a 伦勃朗 / b 维米尔 / c 达·芬奇）+ (d) 卡拉瓦乔旁注（L78–L81）。**这是本路径的主轴**：学委拉斯开兹 = 学「第三档」如何在四者分工中被判出来，而非学一套泛用的巴洛克光影。

---

<a id="db-source-line-30"></a>
## §2 观察对象（照 §12 十件清单，不重写作品序列）

| # | 作品（照录 §12 标题/馆藏/年代） | 观察什么（本路径取用） | 定位 |
|---|---|---|---|
| 1 | 《宫娥》Las Meninas (1656, Prado P001174) | 三层空间开口（画布背面/镜/门）、视线系统、多光源弥散、完成度分级 | [velazquez.md](../../dossiers/velazquez.md) §12 #1 L335–L338 |
| 2 | 《纺纱女》Las Hilanderas (c.1655–60, Prado P001173) | 前景/后景两级空间、画中画、运动可见 | §12 #2 L340–L343 |
| 3 | 《镜前的维纳斯》Rokeby Venus (1647–51, NG2057) | 背身 + 镜面故意模糊、最少信息 | §12 #3 L345–L348 |
| 4 | 《英诺森十世像》(1650, Galleria Doria Pamphilj) | 唯一饱和色（红）、完成度分配、坐姿权力 | §12 #4 L350–L353 |
| 5 | 《胡安·德·帕雷哈》(1650, Met 1971.86, CC0) | 单头写生热身、经济笔触 | §12 #5 L355–L358 |
| 6 | 《塞维利亚的卖水人》(c.1620, Apsley House) | 三材质静物、早期 bodegón 物性 | §12 #6 L360–L363 |
| 7 | **《煎蛋的老妇》(1618, 苏格兰国立美术馆)** | **反例锚点**：单一硬侧光 + 深暗背景（tenebrist 早期） | §12 #7 L365–L368 |
| 8 | 《布雷达的投降》(c.1634–35, Prado P001172) | 直接画布多人物、节制、站位几何 | §12 #8 L370–L373 |
| 9 | 《美第奇别墅花园》(c.1630, Prado) | 外光空气、灰调、小人物尺度 | §12 #9 L375–L378 |
| 10 | 《酒神的胜利》Los Borrachos (1628–29, Prado P001170) | 神话自然主义转译、暖土色系 | §12 #10 L380–L383 |

**权利（brief 强调点 ⑤ 12 行 9PD+3CC0，沿用现有记录）**：12 张公开图 = 9 Public domain（Wikimedia Commons，PD-old-100，作者卒于 1660）+ 3 CC0（Met Open Access：Juan de Pareja 1971.86 / The Supper at Emmaus 14.40.631 / María Teresa 49.7.43）。逐行逐字见 `AUDIT-velazquez/rights_review.md` L9–L20；本机声明级，仅 1/12（juan_de_pareja）经 Met API 当场 web-reverified，11/12 未独立回查 license page，`image_seen=0`。本 lane 不复制像素、不改权利表。

**brief 强调点 ② Pacheco/Palomino OCR 证据**（作为「史料输入」而非作者自述）：

- **Pacheco 底本**（[velazquez.md](../../dossiers/_corpus/velazquez.md) #1–#3 L10–L29；[velazquez.md](../../dossiers/velazquez.md) §9 R17 L235）：`bodegones no se deben estimar` / `verdadera imitación del natural`（「对自然的真正模仿」）。AUDIT RESULT §5-1：es.wikipedia HTML 含两短语 → 转引 substrate 确认；**原书 Cátedra 1990 印本未回查 → 全文原刊 scope 仍 `unverified`**（corpus §缺口、AUDIT §9）。
- **Palomino 底本**（archive.org 1795 `elmuseopictorico23palo_djvu.txt`，AUDIT RESULT §5-2 byte-verified）：`hízole con pinceles y brochas … de cerca no se comprehendia, y de lejos es un mila-gro`（#4 长柄笔）、`entre las figuras hay ambiente` / `porque es verdad, no pintura`（#9 人物之间有空气/真实不是绘画，均 exact）、`Señor, esta es la Teología de la Pintura`（#10 exact）、`manera valiente del gran Ticiano`+`hastas largas`（#12 exact）、`Juan de Pareja, esclavo suyo`（#8 exact）、`Poned, que á mí me consta de su calidad`（#11 授勋 exact modulo OCR）。5 条 corpus Palomino 引文对照 1795 OCR 底本 byte-verified；OCR 有噪声（断词 `mila-gro` / 拼写），核验是归一化子串命中、非 facsimile 校勘（AUDIT §5 诚实边界）。
- **等级纪律**：这些是**他人转记/早期传记**（`[史料]`/reported speech），**不是**委拉斯开兹自述；不得写成「他说」。全档 `[self-written]=0`。

---

<a id="db-source-line-55"></a>
## §3 三个主机制（M1 / M2 / M3，全部标等级）

<a id="db-source-line-57"></a>
### M1 — 光的第三档：画室与空气（主轴）`[归纳]` 分工 + `[史料]` 空气措辞

- **分工**（§3.1 L76，`[归纳]` 写死、可被组合实验推翻 L74）：环境光（画室）+ 空气 + 银灰调；不得复制另三者签名机制。
- **判分轴**（§3.1 L78–L81）：
  - (a) vs 伦勃朗：出现「单光斑地图 + 大片近黑背景 + 亮部堆料」→ 判伦勃朗；「多光源弥散 + 银灰全域 + 人物间空气」→ 判委。参数侧：本模块强档 = P6≥80% + P2≥80%，暗部占比 ≤35%、亮部薄透；伦强档「暗部塌陷 ≤8–10%、亮部厚涂」为伦专属。
  - (b) vs 维米尔：高光形态（碎笔触亮灰 vs 圆点 pointillés）、空间结构（多层开口 vs 单室单点透视）；本模块不采用 pointillé 与「无痕」。
  - (c) vs 达·芬奇：渐变（sfumato，过渡带 ≥1.5% 短边、无可见笔触）vs 笔触空气（断笔/色斑拼出）；两模块组合时「空气」轴只能一位持有者（`conflicts.md` N3 L311），推荐达做底子、委做空气与表面事件。
  - (d) 卡拉瓦乔旁注：塞维利亚期受其自然主义影响但**不复制硬光开关**；判分 = 亮暗边界是否被化开、背景是否被空气填充（卡：背景压暗 ≤10% 且边界硬）。
- **史料锚**：`entre las figuras hay ambiente` / `porque es verdad, no pintura`（corpus #9 L64–L68，Palomino OCR exact）；Mengs「让空气在画中物周围流动」（§3-3 L67，R20 转引）。
- **落到参数**：P6 光的多源柔性 + P2 空气密度定「是不是第三档的委」（§4 用法注 L98：缺 P6 退化为卡拉瓦乔/伦勃朗系单光、缺 P2 退化为普通写实）。

<a id="db-source-line-68"></a>
### M2 — 碎笔触成像 + 完成度分级（borrones / near-view falls apart）`[研究]` + `[归纳]`

- 近看散落笔痕/色斑（2–12 px 级）、远看自动合成形；面部精细、次要对象（手/狗/织物/道具）只给色斑（§1-3/§1-9 L35/L41；§2-9 L56；§8.2-4 L200 / §8.2-8 L204）。
- `[史料]` 长柄笔「近看不可解，远看是奇迹」（corpus #4 L33–L36，Palomino OCR byte-verified）；`lograr más con menos`（§3-4 L68）。
- 参数：P1 直接画法 65% / P4 笔触经济 60%（§4 L91/L94）。

<a id="db-source-line-74"></a>
### M3 — 空间与自反观看（多层开口 + 视线轴）`[归纳]` + `[研究]`

- 空间 = 多层开口（门/窗/镜/画中画）而非单室网格；主人物视线指向画外观者位（§1-6/§1-7 L38/L39；§3-2/§3-6 L66/L70）。
- 参数：P3 空间层数 55%（只在「空间与观看」题材拉满，宫娥类；§4 L93、用法注 L98）。
- §8.2-6 空间开口 / §8.2-7 视线轴（L202/L203）为 `[归纳]` 逐帧自查。

---

<a id="db-source-line-82"></a>
## §4 三段练习阶梯（顺序 = 判光档 → 控笔触 → 套时期 / 反例）

> 全部为**建议练习**（`01-AUDIT.md` L273）。每段给「一次可做的练习 / 可观察结果 / 常见失败 / 自检」。

<a id="db-source-line-86"></a>
### 阶梯 1 — 把「第三档」从伦勃朗/维米尔/达·芬奇里判出来（M1）

- **前置**：读 §3.1 L76–L81 + §4 P2/P6 + §8.2-1/2/3（L197–L199）。
- **一次可做的练习**：取《宫娥》构图草图，列一张「四选一判分表」——逐行勾：单光斑?大片近黑?亮部堆料?→ 伦；点状高光/单室窗光?→ 维；连续长渐变无笔触?→ 达；多光源弥散 + 银灰 + 人物间空气?→ 委。再把同一草图**故意改成单光斑 + 厚涂亮部**，写成对照稿，重跑判分表。
- **可观察结果**（`[归纳]` 自查表，非原作实测）：§8.2-3 亮斑连通域 ≥4 且质心 ≥3 高度带、最大亮斑 ≤3%；§8.2-2 饱和中位数 ≤0.35、纯白/纯黑各 ≤2%、灰调面积 ≥45%；§8.2-1 轮廓断口率 ≥20%、过渡带 ≥4 px 非均匀。
- **常见失败**：把 `--no extreme chiaroscuro / pitch-black background`（§8.1 负向 L180–L186）当成历史断言 → 见阶梯 3 反例；把 P2 强档「远景化开」做成连续长渐变带 → 撞 C-14（§4 注 L99、§8.1 L193，应改写为「大气包络允许，但不得出现连续长渐变带」）。
- **自检**：判分表每行能指到 §3.1 的 a/b/c/d 条款号；改图后判分结果翻转说明轴起作用（B3 自审 L403 判「轴可分离」，但**组合实验 A-12 未做**）。

<a id="db-source-line-94"></a>
### 阶梯 2 — 近看崩解 / 完成度分配（M2 + M3）

- **一次可做的练习**：照 §12 #4 临摹《英诺森十世像》头部（约 1/6 画面）到 90% 完成度，其余部分限 30 分钟、允许「崩解」；再按 §12 #2 把《纺纱女》纺轮（约 40px 区域）**只用 10 笔**；对照远看效果。
- **可观察结果**：§8.2-8 面部细节密度 ≥ 其余 3×、次要对象 ≤ 面部 40%；§8.2-4 笔触尺度 2–12 px、高频能量 ≤ 中频 60%；§8.2-5 高光区局部纹理能量 ≤ 中间调 80%（反伦勃朗亮部厚涂）。
- **常见失败**：全画均匀完成（撞 §8.2-8）、亮部堆料（撞 §3.1a）、1px 硬描边（撞 §1-4 L36）；把「未完成」当缺陷而非收笔纪律（§2-10 L57 `manera abreviada`）。
- **自检**：§8.2 八条逐条勾（L197–L204）；注意全部阈值 `[归纳]`、分母＝假想参考帧、未对原作做像素测量（L206）。

<a id="db-source-line-101"></a>
### 阶梯 3 — 时期切换 + bodegones 反例（brief 强调点 ③）

- **一次可做的练习**：把阶梯 1 的「第三档判分表」应用到 §12 #7《煎蛋的老妇》(1618) 与 §12 #6《塞维利亚的卖水人》(c.1620) 的单光源草图；再照 §8.1 L191 做一次**时期切换**：塞维利亚期把 P6 降到 30%、P1 降到 35%，宫廷盛期用默认，晚期（宫娥/纺纱女类）P1→85% / P4→80% / P3→75%。
- **反例（AUDIT RESULT §6 `[inference]`）**：`Las Meninas` 式「多光源 + 空气」判据若套到 *Old Woman Frying Eggs*（1618，单一硬侧光、深暗背景），会**把一件真委拉斯开兹误判为卡拉瓦乔/伦勃朗**。§4 P6 弱档明确 =「单一侧光、深暗背景（tenebrist 早期）」(L96)，§8.1 L190 把 P6 降到 30%，§8.1 负向约束 L193 自承「其早期 bodegones 确有较暗背景」。
- **判定（照录，不夸大）**：§4/§3.1 判分轴是**成熟-/宫廷期 scoped**，**不是 whole-œuvre 分类器**；dossier 用「时期切换」(L191) + 自审 B2 `WEAKENED`(L402) 部分缓解，但**没有作为单一全局规则解决**——需 A-12 组合实验证伪（B3 L403、§自审 D L449）。第二反例（§3.1c 达·芬奇「只有渐变」vs 委「笔触空气」）由 §4 注 L99 自标 C-14 误伤，记为定位/一致性漂移，非硬推翻。
- **可观察结果 / 自检**：判分表必须带「时期」列；对 bodegones 行显式写 `mature/court-scoped → out of scope for early Seville`，不得输出「非委拉斯开兹」结论。

---

<a id="db-source-line-110"></a>
## §5 下一步及使用边界（A-30 §8.1 要求的八项收口）

| 项 | 落地 |
|---|---|
| 前置知识 | §1 三类知识分级 + 无自述口径 |
| 重点作品及来源 | §2 十件（§12）+ 权利 12 行（rights_review.md）+ Pacheco/Palomino OCR 底本 |
| 要观察的机制 | §3 M1/M2/M3 |
| 具体练习 | §4 三阶梯（判光档 / 控笔触 / 时期切换+反例） |
| 可观察结果 | 各阶梯「可观察结果」= §8.2 自查表（`[归纳]`、非原作实测） |
| 常见失败 | 各阶梯「常见失败」+ 阶梯 3 bodegones 误判 |
| 下一步 | 跨艺术家 A/B 对照（§12 组合建议 L385：1/2 练空间、3/5/6 练空气肖像经济、4/8 练完成度、9 练外光；分别与伦勃朗心理光 / 维米尔光学 / 达·芬奇渐变空气对照）；待独立审者 + A-12 组合实验 |
| 使用边界 | 建议练习 ≠ 已证实学习收益；`human_review.status=not_applicable`；AUDIT 为 ACCEPTED 依赖、复用不重审；repo READ-ONLY；12 权利行本机声明级、11/12 未独立回查；`image_seen=0`、无像素测量、无渲染、无真人评价 |

**总路线接口**：本卡属 A-30 76 位学习路径之一，基础/进阶顺序按 §4 三阶梯；可替换分支 = 把 M1 换成任一「光持有者」（伦勃朗/维米尔/卡拉瓦乔/达·芬奇）做 A/B；跨艺术家比较方式 = §3.1 三对判分轴 + `conflicts.md` N1/N3 程序（L305/L311）。不另造生平材料（`01-AUDIT.md` L271）。

---

<a id="db-source-line-127"></a>
## §6 dangling 「本卡 §3.1」 指针（brief 强调点 ④，照录 AUDIT §7，不修）

- [velazquez.md](../../modules/velazquez.md) 的「冲突注记」L79/L80/L81/L82 四处写「**本卡 §3.1 分工条款**」（另 L57/L73 引用「§3.1 判据/判分轴」共 6 处提到 §3.1），但**模块卡根本没有 §3.1 节**（headers：视觉指纹 / 图像 prompt / 代码艺术规则 / 控制参数 / 冲突注记 / 来源）。§3.1 分工条款**只存在于 dossier** 的 L74–L81。→ `VL-DRIFT-01`（support_status=conflict），规则文本本身无错，**只有指针悬空**。
- [velazquez.md](../../modules/velazquez.md) L87 写 `conflicts.md` =「18 条 C + N1–N9 + near-miss **8 对**」，但 `conflicts.md` §4 现有 **11** 条编号 near-miss（L347–L357，#9–#11 于 2026-10-16 补）。→ `VL-DRIFT-02`（2026-11-18 收口核验：module L87 已按 F01 更正为「11 对」，漂移已消除；本行保留为历史登记）（conflict）。同 8-vs-11 漂移亦由 AUDIT-durer lane 记录。
- C-14 / N1 / N3 的行号引用（velazquez §3.1c L80、§4 注 L99）**能解析**：C-14 §1 行 L45 / 详 L229、N1 L305、N3 L311（AUDIT §7-3）。velazquez 在 conflicts.md §1/§4 的**直接 C/near-miss 行 = 0**（AUDIT §7-4，诚实）。
- **处置**：本 shard 只在自己的产物里「指向 dossier §3.1 / conflicts.md」并注明「模块卡『本卡 §3.1』为悬空指针，应读作 dossier §3.1」；**不改模块卡、不改 conflicts.md、不改 AUDIT 产物**（repo READ-ONLY，AUDIT 为 ACCEPTED 依赖）。报告，不修复。

## 同一条目的附页

- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
