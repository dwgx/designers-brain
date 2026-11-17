<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-vermeer；原正文 SHA-256 `272a6966b4d0263aec5ca8d7f51df44cbc8431224a2137065881c5106abcacda`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-vermeer — 学习路径（A-30 §8.1 形状）

> 本路径是**建议练习**（suggested practice），不是「已证实学习收益」。截至本轮，所有 §8.2 阈值均为本项目 `[归纳]`、未对维米尔原作做像素测量（[vermeer.md](../../dossiers/vermeer.md) L244；[vermeer.md](../../modules/vermeer.md) L76；`conflicts.md` §5.D L420），也没有任何 human review / 真人学习成效评价。不得把本文件写成「已验证的教学法」或「维米尔本人的方法」。
>
> 证据底本：内部证据 056cb11f78df0e19（未公开；来源记录由维护者保留）（`claim-evidence-map.md`、`coverage-manifest.md`、`RESULT.md`，ACCEPTED 审计）。沿用其 `文件 : 节 : 行号` 定位纪律，不重审、不改 repo。基线 commit `f008952365a77e140cbda3f3959d43ef000f9a22`。
>
> 证据级别照录 [vermeer.md](../../dossiers/vermeer.md) L5：`[自述]` 本人写下/说出 ｜ `[史料]` 当时记录/档案/馆藏 ｜ `[研究]` 艺术史家/博物馆/学术资料 ｜ `[归纳]` 本项目从作品与资料归纳的操作规则 ｜ `[推测]` 低置信。
> **结构性事实（AUDIT-vermeer §1）**：维米尔无任何自述留世（[vermeer.md](../../dossiers/_corpus/vermeer.md) L5、L193；[vermeer.md](../../dossiers/vermeer.md) L6、L69、L99、L305）——因此本路径所有「创作决策」只能是 `[归纳]/[推测]`（研究者从作品与资料归纳），**没有一条能标 `[自述]`**，也不得写成「维米尔说过/主张」。

---

<a id="db-source-line-12"></a>
## §1 前置知识（先具备什么，再开练）

1. **先接受「无自述」这条硬约束**：本课题没有作者本人方法论可引用。能用的是 (a) 同时代档案（Monconys 日记、遗产清单、Dissius 拍卖目录等，[vermeer.md](../../dossiers/_corpus/vermeer.md) 22 条）；(b) 馆方/艺术史研究（Rijksmuseum、Mauritshuis、National Gallery、EV 工作室页等 `[R#]`）；(c) 本项目从作品归纳的可判定规则（§4 参数、§8.2）。→ 定位 `AUDIT-vermeer/claim-evidence-map.md` §C（AV-SELF-0 / AV-CAVEAT-C1/C2/C3）。
2. **三个要先分清的「层」**（`02-EXECUTION-PLAN.md` L64 的学习顺序，及本项目口径）：
   - **档案事实层**（`[史料]/[研究]`）：作品、日期、馆藏、材料（2018 *Girl with a Pearl Earring* 剖面、群青 μ-XANES、针孔/圆规孔）。[vermeer.md](../../dossiers/vermeer.md) §2 L48–63、§7 L170–192。
   - **操作化规则层**（`[归纳]`）：§4 六个控制参数（P1–P6）、§8.2 八条可判定规则、§8.1/§8.1b prompt。[vermeer.md](../../modules/vermeer.md) L63–90；[vermeer.md](../../dossiers/vermeer.md) L83–95、L231–244。**档位划分本身为 `[归纳]`，未做渲染实验**（[vermeer.md](../../modules/vermeer.md) L90）。
   - **规则层冲突层**（`[归纳]`）：[conflicts.md](../../../../cross/conflicts.md) 的 C/near-miss 判定「均为规则层判定，不排除实测后被修正」（§5.D L420）。
3. **最小工具/概念**：单侧平行光、暗部局部亮度标准差（std）、连通域分析、圆度、Canny 边缘宽度中位数、帧差图（Δ）、单点透视消失点、色相簇。这些是 §8.2「自查方法」列要求的量（[vermeer.md](../../dossiers/vermeer.md) L235–242），不是史实。
4. **先读冲突表**：本路径练习集中在 C-09、C-11、near-miss #1/#2/#3/#7/#8 涉及的三个机制（运动、高光、暗部/边缘）；跨模块组合前先读 `conflicts.md` §1/§2/§4 与 [vermeer.md](../../modules/vermeer.md) L92–99 冲突注记。

---

<a id="db-source-line-24"></a>
## §2 重点作品及来源（引用现有记录，不新增编造）

作品与馆藏、权利信息**沿用 [vermeer.md](../../dossiers/vermeer.md) §12「临摹/学习清单（10 件）」L424–476** 与 §10/§11 的既有记录；本 lane 未打开任何外部 URL、未逐张目检 3 张公开图（`AUDIT-vermeer/coverage-manifest.md` §4：image_seen=0，read_scope=metadata）。下列定位均可寻址到现有档案。

| 练习用作品（照录 §12 标题/馆藏） | 本路径用来观察的机制 | 来源定位（现有记录） |
|---|---|---|
| 《倒牛奶的女仆》*The Milkmaid*（c. 1658–1661，Rijksmuseum，SK-A-2344） | 单一事件（牛奶流）对全画静止；「数百个彩点」pointillés；材质＝高光形状；低动态范围 | [vermeer.md](../../dossiers/vermeer.md) §12-1 L428–431；§1-4 L34、§1-8 L38；[vermeer.md](../../modules/vermeer.md) §4 P3 L84；`conflicts.md` C-11 L193 |
| 《戴珍珠耳环的少女》*Girl with a Pearl Earring*（c. 1665，Mauritshuis，inv. 670） | 极简高光（珍珠＝两笔白、无挂钩）；面部无轮廓线；暗背景把主体前推；边缘过渡带 ≥2px | §12-2 L433–436；§2-13 L62；§1-7 L37、§1-11 L41 |
| 《小街》*The Little Street*（c. 1657–1661，Rijksmuseum） | 哑光质感；门洞/窗内暗部「平而不死」；静默街景无人感 | §12-4 L443–446 |
| 《蓝衣读信女》*Woman in Blue Reading a Letter*（c. 1662–1665，Rijksmuseum） | 群青蓝权重（限色）；高调画面的冷调统一；暗部为纯色平面 | §12-8 L463–466；§4 P2 L88、P4 L90（卡 L83、L85） |
| 《持天平的女人》*Woman Holding a Balance*（c. 1664，NGA 1942.9.97）／《绘画的艺术》*The Art of Painting*（c. 1666–1668，KHM） | 单点透视＋网格几何；三层以上景深 | §12-5 L448–451、§12-6 L453–456；§8.2-6 L240 |
| 《窗前读信的少女》（c. 1657–1659，Dresden）／《站在维金纳琴前的女子》（c. 1670–1674，NG London） | pentimenti（改动痕迹）；晚期简化/书法性笔触 → 作为「何时失效」边界样本 | §12-7 L458–461、§12-10 L473–476；§4 P6 L92 弱/中/强档 |

> **权利/图像边界**：3 张公开图像的权利声明见 [manifest.md](../../dossiers/_images/manifest.md)（`AUDIT-vermeer/coverage-manifest.md` §1 登记 sha `5698124d…`），本 lane 只引用记录、不复制像素、不重新授权。
> **引文性质**：「hundreds of colourful dots」是 Rijksmuseum 对 *The Milkmaid* 的描述（经 [vermeer.md](../../dossiers/vermeer.md) §4 P3 L89 转引），属 `[研究]`/馆方描述，不是维米尔自述，也不是本项目实测点数。

---

<a id="db-source-line-42"></a>
## §3 要观察的机制（三个主机制 + 关联机制，全部带定位与等级）

| 机制 | 可判定量 | 来源定位 | 等级 |
|---|---|---|---|
| **M1 单一事件运动 / 全画面静止** | 除事件区域（牛奶流/烛焰/烟）外帧间差 **Δ ≤1%**；运动区域数 = 1 | [vermeer.md](../../dossiers/vermeer.md) §8.2-8 L242；[vermeer.md](../../modules/vermeer.md) L74；§1-8 L38 | `[归纳]`（阈值）/ `[研究]`（「stream of milk… everything else is still」） |
| **M2 pointillé 密度分档** | 圆点直径 **1–3 px**（1024 px 宽基准）、软边 σ = 0.5–1 px；数量按 P3 分档 **0–2 / 5–20 / 100+**；连通域面积单峰、圆度 >0.7、禁线状高光 | [vermeer.md](../../dossiers/vermeer.md) §8.2-3 L237、§4 P3 L89；[vermeer.md](../../modules/vermeer.md) L69、L84 | `[归纳]`（档位/阈值）/ `[研究]`（pointillé 形态） |
| **M3 物体边缘过渡带 ≥2px（无硬边）** | 任意物体边缘过渡带 **≥2 px**；禁止 1 px 描边；Canny 边缘宽度中位数 | [vermeer.md](../../dossiers/vermeer.md) §8.2-5 L239、§4 P5 L91；[vermeer.md](../../modules/vermeer.md) L71、L86；§1-7 L37 | `[归纳]`（阈值）/ `[研究]`（「without any hard lines」） |
| M4 平坦暗部（关联 M3/#8） | 暗部（亮度 ≤ 受光面 25%）内部 std **≤ 5/255** | §8.2-2 L236；§4 P2 L88 | `[归纳]` / `[研究]`（EV「flat and virtually unmodulated」§1-3 L33） |
| M5 单侧左窗光（关联 #2/#3） | 主光画面左 ±15°；填充光 ≤ 主光 15% | §8.2-1 L235；§4 P1 L87 | `[归纳]` |
| M6 动态范围压缩（关联 #1） | 受光面 ≤88%、暗部下限 ≥8%（禁纯白/纯黑） | §8.2-7 L241 | `[归纳]` |
| M7 单点透视网格 | 消失点 1 个，画面高 55–65%；地砖 29.3 cm 比例 | §8.2-6 L240；§1-9 L39 | `[归纳]` / `[研究]`（Steadman [R14]） |

---

<a id="db-source-line-56"></a>
## §4 具体练习（建议练习 · 三段阶梯 ladder，≥3 级，可操作）

> 练习总顺序按 brief 指定：**single-event room scenes → pointillé highlight studies → quiet-surface discipline**。与 §12 既有「1→4 基本功 / 5→7 构图 / 8→10 限色」顺序（L426）兼容：本 ladder 是「机制维度」的三阶，§12 是「作品维度」的序列，二者不互相替代、不重写 §12。
> 每段均为**建议练习**：先规定输入、动作、自查量、通过/失败判据；**练习效果（是否真的提升学习者能力）未由人评价，标 `pending_human / not_applicable`，不写「已证实学习收益」**（`01-AUDIT.md` §8.1 L273）。

<a id="db-source-line-61"></a>
### 阶梯 1 — Single-event room scenes（练 M1「单一事件 + Δ≤1%」）

- **输入**：一个室内单侧左窗光场景（参考 §8.1 正向段 [vermeer.md](../../modules/vermeer.md) L20–31 的题材词；或 §12-1《倒牛奶的女仆》L428）、一个明确的「事件」（倒液/烛焰/烟），2–3 帧短序列。
- **动作**：① 把画面分成「事件区」掩膜与「非事件区」；② 只让事件区在帧间变化；③ 逐帧生成帧差图，统计非事件区「非零像素占比」。
- **自查量**：非事件区帧间差 **Δ ≤1%**（§8.2-8 L242 / 卡 L74）；全片运动模糊帧数 = 0（`conflicts.md` C-08 解法 L161）；运动区域数 = 1。
- **可观察结果（产物级，非学习成效）**：帧差图里非事件区接近全零；事件区是唯一连通的变化簇；无第二处运动。
- **关联冲突**：C-09（×梵高 `conflicts.md` L164–174）——若加入天空旋涡/全画面场漂移即违反 Δ≤1%；C-08（×Lane B 运动模糊 L149–162）。
- **失败判据**：非事件区出现 >1% 的帧差；或出现第 2 个运动簇；或出现运动模糊帧。

<a id="db-source-line-70"></a>
### 阶梯 2 — Pointillé highlight studies（练 M2「密度分档 0–2 / 5–20 / 100+」）

- **输入**：同一静物（面包/铜壶/瓷罐/珍珠，§12-1 L431、§12-2 L436），固定单侧光与机位；画三档 **建议练习**变体。
- **动作**：按 `§4 P3` 三档（[vermeer.md](../../dossiers/vermeer.md) L89 / 卡 L84）各做一张——
  - 弱档 **0–2 点**（仅眼睛/珍珠级）；
  - 中档 **5–20 点**（局部：金属、瓷、面包）；
  - 强档 **100+ 点**（满画面数百点，对应 Rijksmuseum「hundreds of colourful dots」）。
  - 每张跑连通域分析：记录亮点直径（1–3 px @1024 宽）、软边 σ（0.5–1 px）、圆度（>0.7）、是否出现线状高光。
- **自查量**：数量落在对应分档；亮点面积分布单峰；圆度 >0.7；**无「线状高光」**（§8.2-3 L237 / 卡 L69）。
- **可观察结果**：三档只看「高光数量/形状」这一变量，其余（光位、色板、边缘）保持不变；强档仍保持「点＝镜面高光」而非「色的分解」。
- **越界警报（照录 [vermeer.md](../../dossiers/vermeer.md) L227）**：P3 到 100% 会变成修拉式分割主义——一旦点变成「色的分解」而非「高光」，就进入修拉模块地盘，判失败。
- **关联冲突**：C-11（×卡拉瓦乔 `conflicts.md` L188–201）——若把 pointillés 按「亮度 ≥0.9×max 的高光连通域」全帧统计，100+ 点中只要有 6 个达标即与 [2,5] 互斥；但 `conflicts.md` §5.B #4 L374 已 **WEAKENED**：维米尔未给 pointillé 亮度阈值，故这是**条件式互斥**。组合解法 L196–201：拆「主光斑（面积 ≥0.05% 画面）/ 点状高光（1–3 px）」两类分别计数。
- **失败判据**：出现线状/条状高光；强档退化成色点分解；把点误计入卡拉瓦乔 [2,5] 主光斑计数。

<a id="db-source-line-84"></a>
### 阶梯 3 — Quiet-surface discipline（练 M3「边缘 ≥2px」+ M4 平坦暗部 + M5/M6，含 near-miss 取值）

- **输入**：同一室内场景再画一张，重点放在「暗部色面 / 物体边缘 / 白墙高调 / 蓝-黄限色」。
- **动作**：① 在 Canny 边缘图上量边缘过渡带宽度中位数，确保 **≥2 px**、删除任何闭合 1 px 轮廓（§8.2-5 L239 / 卡 L71）；② 对暗部区域跑局部 std，确保 **≤ 5/255**（§8.2-2 L236 / 卡 L68）；③ 检查 min/max：受光面 ≤88%、暗部下限 ≥8%、禁纯白纯黑（§8.2-7 L241 / 卡 L73）；④ 色相簇 ≤8、蓝-黄主色对、阴影向蓝偏移 ≥15°（§8.2-4 L238）。
- **自查量**：边缘宽度中位数 ≥2px；暗部 std ≤5/255；动态范围两端；色相簇数。
- **可观察结果**：暗部是「平而不断死」的大块色面、面部/器物无硬描边、白墙高调但不爆白、蓝-黄成对且红只作小点缀。
- **关联 near-miss（必须显式写值，否则被静默折中）**——取自 `conflicts.md` §4 L347–354 与 `AUDIT-vermeer/RESULT.md` §4：
  - **#1** 背景 ≤10% × 暗部下限 ≥8% → 背景取 **[8%,10%]**，且卡拉瓦乔「纯黑 ≤10%」在维米尔在场时收紧为 0%（L347；`caravaggio.md` L215 / `vermeer.md` L241）。
  - **#2** 环境光 ≤5% × 填充光 ≤15% → 取 **≤5%**（L348；`caravaggio.md` L214 / `vermeer.md` L235）。
  - **#3** 主光「左上或右上（±0.7,−0.7）」×「画面左 ±15°」→ 选 **左上** 同时满足（L349）。
  - **#7** 边缘过渡带 ≥2px × 明暗过渡带 ≤0.6% 短边（1920 宽 ≈≤11.5px）→ 交集 [2, 11.5] 非空但**量纲不同**（物体边缘 vs 形体转折明暗），卡内必须写清测的是哪一个，否则自查脚本误判（L353；`michelangelo.md` L176）。
  - **#8（本轮 upgraded）** 维米尔暗部 std ≤5/255（`vermeer.md` L236）× 卡拉瓦乔暗区 std ≥1.5/255 → 交集 **[1.5, 5]**；两者对「暗部是否平坦」取向相反，同帧取区间中点附近并显式写值（L354）。**端点此前在 AUDIT 记为 partial**（`AUDIT-vermeer/RESULT.md` L113–116 / `claim-evidence-map.md` §E AV-NM8）：卡拉瓦乔侧数值曾被记为「本机未逐字命中」。本 LEARN 回源核到 **`caravaggio.md` L220**「暗部保细节：暗区（亮度 < 0.15）内部亮度标准差 **≥ 1.5/255**（非死黑）」逐字命中 → **升级为 supported**，定位 `caravaggio.md : §8.2-7 : L220`（见 [mechanism_notes.md](mechanism_notes.md) §冲突行、本目录 [claim_evidence_map.md](claim_evidence_map.md) C-NM8）。不改写 AUDIT 产物，只在 LEARN 记录「同一端点已可寻址」。
  - **#5**（卡内已声明、brief 未点名，照 `AUDIT-vermeer/RESULT.md` L118–120 一并保留）色相簇 ≤7/≤5/≤8 → 取 **≤5**（L351）。
- **失败判据**：暗部出现渐层/细节（std 超阈）；出现 1px 硬线；纯黑或纯白像素；跨模块组合时把 #7 两种过渡带混为同一统计量。

---

<a id="db-source-line-101"></a>
## §5 可观察结果（产物级 / 不是学习成效）

| 阶梯 | 可交付观察物 | 判定口径 | 性质 |
|---|---|---|---|
| 1 | 帧差图（非事件区接近全零）+ 运动区域数记录 | Δ≤1%（§8.2-8） | 产物自查，`[归纳]` 阈值 |
| 2 | 三档 pointillé 连通域统计表（直径/圆度/数量/有无线状） | §8.2-3 + P3 分档 | 产物自查，`[归纳]` 阈值 |
| 3 | 边缘宽度中位数、暗部 std、min/max、色相簇、near-miss 显式取值表 | §8.2-2/4/5/7 + conflicts §4 | 产物自查，`[归纳]` 规则层 |

> 这些是**「一张图/一段序列是否满足本模块可判定规则」**的观察，不是「学习者经过练习后能力提升」的证据。后者需要真人评价与预注册实验，当前 `human_review.status = not_applicable`（见 `RESULT.md`），一律标 `pending_human / 未评价`，不写「已证实学习收益」（`01-AUDIT.md` §8.1 L273）。

---

<a id="db-source-line-113"></a>
## §6 常见失败（反例，照录现有档案 + 冲突表）

1. **把点画成「色的分解」** → 修拉式分割主义越界（[vermeer.md](../../dossiers/vermeer.md) L227）；点必须仍是镜面高光。
2. **出现线状/条状高光或闭合 1px 轮廓** → 违反 §8.2-3「圆度 >0.7、无线状」与 §8.2-5「≥2px、禁 1px 描边」（[vermeer.md](../../dossiers/vermeer.md) L237、L239）。
3. **暗部画成渐层/塞细节** → 违反平坦暗部 std ≤5/255（L236），退化成普通荷兰风俗画（L225「缺 P2 会退化成普通荷兰风俗画」）。
4. **加第二个运动 / 全画面漂移 / 运动模糊** → 违反 Δ≤1%（L242）与 C-09/C-08（`conflicts.md` L164–174、L149–162）。
5. **纯黑或纯白** → 违反动态范围压缩（L241）；且 near-miss #1 在维米尔在场时把「纯黑 ≤10%」收紧为 0%（`conflicts.md` L347）。
6. **把 #7 两种过渡带当成同一个量** → 量纲不同（物体边缘 px vs 形体转折 %短边），自查脚本会误判（L353）。
7. **把 pointillés 计入卡拉瓦乔 [2,5] 主光斑** → C-11 条件式互斥；须用 L196–201 分类口径，并记住 §5.B #4 L374「不能断言 100+ 点必然 ≥0.9×max」。
8. **把本模块规则说成「维米尔主张」** → A-40 caveat C3（`AUDIT-vermeer/claim-evidence-map.md` §C AV-CAVEAT-C3；`_crosscheck.md` L151–152；[vermeer.md](../../modules/vermeer.md) L76、L90）。结构性无自述，所有 §3/§4/§8.2 只能 `[归纳]`。
9. **用晚期作品当成熟期范本** → 《站在维金纳琴前的女子》/《吉他手》是 P6 弱档（可见笔触/书法性），与成熟室内「levigated / 织纹不可见」相反（§12-10 L473–476、§4 P6 L92）；[vermeer.md](../../dossiers/vermeer.md) L226 给出时期切换口径。
10. **静默折中 near-miss 取值** → `conflicts.md` §4 要求「显式写值」；不写值即被静默折中（#1/#2/#3/#7/#8 各条）。

---

<a id="db-source-line-128"></a>
## §7 下一步（接入 A-30 总路线）

1. **本 shard 的出口**：[how-to-think.md](how-to-think.md)（创作决策序）、[mechanism_notes.md](mechanism_notes.md)（§4 参数/§8.2 规则 → 可执行练习映射、冲突行、失败条件）、[claim_evidence_map.md](claim_evidence_map.md)（逐 claim 定位）三份与本文件同目录，供 A-30 总路线寻址（registry `LEARN-vermeer`）。
2. **跨艺术家比较分支**（`01-AUDIT.md` §8.1 L271「可替换分支/跨艺术家比较方式」）：
   - 运动预算对照 → 梵高（C-09，`van_gogh.md` L207–208）；
   - 高光计数对照 → 卡拉瓦乔（C-11、`caravaggio.md` L217、L220）；
   - 过渡带量纲对照 → 米开朗基罗（#7、`michelangelo.md` L176）；
   - 限色对照 → 北斋/毕加索（#5）。
3. **留给其它 lane 的实测**：§8.2 阈值未做像素测量（[vermeer.md](../../dossiers/vermeer.md) L244）；首个 AI 野外样本尚未生成（§8.3 L248）；§8.1b 派生明细 `experiments/E1_t1b/RESULTS_t1b.md §2` 属已迁出实验目录、本机 unavailable（`AUDIT-vermeer/RESULT.md` §3、unresolved #3）。这些是 RECOVERY / 实验 lane 的职责，本 LEARN 不越权重跑、不假装已核。
4. **人评**：若要主张「学习收益」，需固定样本包 + 评价维度 + 真人提交评价（`01-AUDIT.md` §8.4 L310）；在此之前保持 `pending_human`。

---

<a id="db-source-line-141"></a>
## §8 使用边界（硬边界，照录）

- **不是作者方法论**：维米尔无任何自述留世；本路径的「创作决策」全是研究者 `[归纳]/[推测]`，不得表述为「维米尔说过/主张」（`AUDIT-vermeer/claim-evidence-map.md` §C AV-CAVEAT-C2/C3）。
- **规则层 ≠ 实测层**：§4/§8.2/冲突阈值均为 `[归纳]`，未对原作做像素测量（[vermeer.md](../../modules/vermeer.md) L76、L90；`conflicts.md` §5.D L420）。conflicts 的「空交集/互斥」是规则层判定，实测后可能被修正。
- **建议练习 ≠ 已证实学习收益**：`01-AUDIT.md` §8.1 L273；`human_review.status = not_applicable`；模型/agent 判断不得冒充人评（`01-AUDIT.md` §8.4 L308）。
- **图像与权利**：只引用现有记录与权利声明（`_images/manifest.md`），不复制像素、不重新授权、不逐张目检（AUDIT coverage §4 image_seen=0）。
- **外部来源未核**：22 条语料原文/英译、[R#] URL/馆方扫描件未逐字回源（AUDIT RESULT §2、unresolved #2）；本 lane 离线只读本机，外部真伪标 `unverified`。
- **不重审、不写 repo**：沿用 ACCEPTED 的 `AUDIT-vermeer`；NO repo writes、NO subagent spawns、NO credentials（本 lane 契约）。
- **C-11 是条件式**：维持 `conflicts.md` §5.B #4 L374 的 WEAKENED 口径，不恢复为无条件硬冲突。
- **near-miss #8 升级范围**：本 LEARN 仅记录「卡拉瓦乔侧端点已可在 `caravaggio.md` L220 逐字命中」；不改写 `conflicts.md`、不改写 AUDIT 产物、不声称已验证暗部像素统计。

---

<a id="db-source-line-154"></a>
## 附：本文件每条断言的定位索引

见同目录 [claim_evidence_map.md](claim_evidence_map.md)（A/B/C/D/E 各组）。[mechanism_notes.md](mechanism_notes.md) 给 §4/§8.2 → 练习的逐条映射与失败条件；[how-to-think.md](how-to-think.md) 给创作决策序并严格分离 `[自述]`（本例为 0 条）与 `[归纳]/[推测]`。

## 同一条目的附页

- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
