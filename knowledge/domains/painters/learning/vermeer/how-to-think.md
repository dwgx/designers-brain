<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-vermeer；原正文 SHA-256 `58ec3ede87a2592ebf92af8d4d89ab28d95547595fd0eee3a6bb0ce0df13870b`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-vermeer — How to Think（创作决策序）

> **严格分离声明（本文件最重要的一条）**
> - `[自述]` = 维米尔本人写下/说出。**本例为 0 条**：结构性无自述（[vermeer.md](../../dossiers/_corpus/vermeer.md) L5、L193；[vermeer.md](../../dossiers/vermeer.md) L6、L69、L99、L305；`_crosscheck.md` L114、L150–152、L280；`AUDIT-vermeer/claim-evidence-map.md` §C AV-SELF-0）。因此**本文件没有任何一步能标 `[自述]`**，凡出现「他主张/他认为/他说过」一律是误用。
> - `[归纳]` = 本项目从作品、档案与 art-historical 资料归纳的**操作规则**（[vermeer.md](../../dossiers/vermeer.md) L3 项目口径、L69；[vermeer.md](../../modules/vermeer.md) L76、L90）。
> - `[推测]` = 低置信推断。
> - `[研究]`/`[史料]` = 馆方/艺术史家/同时代档案（用作归纳的**输入**，不是决策本身）。
>
> **禁止从画面外观编造作者心理**（`00-GOAL.md` L9；`01-AUDIT.md` §8.4 L308；`AUDIT-vermeer/claim-evidence-map.md` §C AV-CAVEAT-C3）：本文件写的是「面对一张图，一个**采用维米尔模块的操作者**按什么顺序做取舍」，不是「维米尔当时脑子里想什么」。每一步都带 **evidence grade** 与定位；决策序本身是 `[归纳]`（研究者构造），不是史实。
>
> 基线 `f008952365a77e140cbda3f3959d43ef000f9a22`；定位沿用 `AUDIT-vermeer` 的 `文件 : 节 : 行号` 纪律。

---

<a id="db-source-line-15"></a>
## 0. 决策序总览（先选什么 → 牺牲什么 → 为什么 → 何时失效）

| 步 | 先选什么 | 牺牲什么 | 为什么（`[归纳]`） | 何时失效 | 证据级 |
|---|---|---|---|---|---|
| D1 | 题材＝静默室内单/双人 + **单一事件** | 多事件、群像、戏剧冲突、全画面运动 | 把叙事噪音压到最低，让「光的行为」成为主题（§3-6 L76、§1-8 L38） | 需要多动作/运动场时（→梵高 C-09） | `[归纳]`（决策）/ `[研究]`（静默） |
| D2 | **单侧左窗光**主导（P1 默认 75%） | 多光源、双侧光、逆光、戏剧性硬光 | 「是不是维米尔」由 P1/P2/P6 三件套定（L225） | 组合卡拉瓦乔且要求硬光边缘时（[vermeer.md](../../dossiers/vermeer.md) L228 明确不许） | `[归纳]` |
| D3 | **暗部压平**（P2 默认 70%，std ≤5/255） | 暗部渐层、暗部细节、光晕 | 平坦暗部是指纹（§1-3 L33）；缺 P2 退化成普通荷兰风俗画（L225） | 需要「暗部保细节」的卡拉瓦乔同帧（near-miss #8：区间 [1.5,5]，须显式取值） | `[归纳]` / `[研究]`（EV 描述） |
| D4 | **高光＝信息载体**：用 pointillé 形状/数量分档 | 轮廓线、逐根细描、色的分解 | 材质靠高光形状区分（§3-7 L77、§1-10 L40）；色调/轮廓真实 > 细节累积（§3-1 L71） | P3 到 100% → 修拉式分割主义（L227）；或按 0.9×max 全帧计数 → C-11 | `[归纳]` / `[研究]`（pointillé 形态） |
| D5 | **无硬边**：边缘过渡带 ≥2px、细节主动省略 | 1px 描边、清晰轮廓、耳环挂钩等细节 | sfumato／「省略作为完成度」（§1-7 L37、§12-2 L436） | 与米开朗基罗硬边阴影同帧（#7 量纲不同，不能混测） | `[归纳]` / `[研究]`（Mauritshuis 引文） |
| D6 | **限色**：蓝-黄主色对、色相簇 ≤8、红仅点缀 | 饱和多元色板、互补色堆叠 | 群青蓝×赭黄成对（§1-6 L36）；冷调阴影（§1-5 L35） | 限色 ≤5 的组合（#5，×北斋/毕加索） | `[归纳]` |
| D7 | **动态范围压缩**：受光 ≤88%、暗部 ≥8% | 纯白/纯黑、HDR、强黑白对比 | 低动态范围（§1-2 L32、§1-11 L41） | near-miss #1 × 卡拉瓦乔背景 ≤10% → 背景取 [8,10]% 且纯黑收紧 0% | `[归纳]` |
| D8 | **单点透视网格** + 表面平滑（P6 85%） | 多点透视、可见笔触/织纹 | 房间几何网格（§1-9 L39）；levigated effect（§1-12 L42） | 晚期/早期作品（《吉他手》《维金纳琴》P6 弱档，L226、§12-10） | `[归纳]` / `[研究]`（Steadman [R14]） |

> 八步全是 `[归纳]`（研究者构造的操作顺序）。`[研究]`/`[史料]` 只是 D 步里「为什么」所引的输入材料，**不等于**维米尔的决策记录。

---

<a id="db-source-line-32"></a>
## 1. 逐步展开（每步带 evidence grade + 定位 + 失效条件）

<a id="db-source-line-34"></a>
### D1 — 先选「单一事件」而不是「故事」 `[归纳]`
- **先选**：1–2 人、一个被冻结的日常动作（倒牛奶/读信/持天平），全画只允许 1 个「事件区」在动。
- **牺牲**：多事件叙事、群像、全画面运动、运动模糊。
- **为什么**：静默与时间停滞是归纳出的构图取向（[vermeer.md](../../dossiers/vermeer.md) §3-6 L76「构图压掉一切叙事噪音…极短一瞬被冻结」；§3-8 L78「选择性描述」）；§1-8 L38 引 [R24]「Except for the stream of milk, everything else is still」。操作化量 = `§8.2-8 Δ≤1%`（L242，卡 L74）。
- **何时失效**：一旦引入梵高式全画面场（角速度 2–6°/s、闪烁 0.8–1.5s，`van_gogh.md` L207–208），即 C-09 硬冲突（`conflicts.md` L164–174）；或引入 Lane B 运动模糊（C-08 L149–162）。组合解法只能是「题材分层掩膜 + 角速度降到 ≤1°/s」且显式写两层角速度上限，否则不可拆（L172–174）。
- **grade**：`[归纳]`（阈值/决策序）/ `[研究]`（静默描述）。定位：[vermeer.md](../../dossiers/vermeer.md) L38、L76、L242；`conflicts.md` L164–174。

<a id="db-source-line-41"></a>
### D2 — 定「单侧左窗光」再定其它 `[归纳]`
- **先选**：主光画面左 ±15°、≤1 个弱填充光（≤主光 15%）、P1 默认 75%（§8.2-1 L235；§4 P1 L87）。
- **牺牲**：第二组反向高光、双侧光、暖钨丝光、戏剧硬光。
- **为什么**：P1/P2/P6「定是不是维米尔」（[vermeer.md](../../dossiers/vermeer.md) L225）；模块 negative 段禁 `multiple light sources / rim light`（[vermeer.md](../../modules/vermeer.md) L37）。
- **何时失效**：与卡拉瓦乔同帧——#2 环境光 ≤5% × 填充光 ≤15% 取 **≤5%**；#3 主光「左上或右上」×「画面左」选 **左上**（`conflicts.md` L348–349；`caravaggio.md` L214）。[vermeer.md](../../dossiers/vermeer.md) L228 还明确写：维米尔 70% + 卡拉瓦乔 30% 时**只允许**把 P1 提到 90%、压暗背景，**不要**引入硬光边缘与戏剧投影。
- **grade**：`[归纳]`。定位：[vermeer.md](../../dossiers/vermeer.md) L235、L87、L225、L228；`conflicts.md` L348–349。

<a id="db-source-line-48"></a>
### D3 — 先决定「暗部要多平」 `[归纳]`
- **先选**：暗部压成平色面，局部 std ≤5/255（§8.2-2 L236），P2 默认 70%（§4 P2 L88）。
- **牺牲**：暗部渐层、暗部纹理、光晕渐变。
- **为什么**：EV「the deep shadows … often flat and virtually unmodulated areas of paint」（§1-3 L33，`[研究]`）；这是与「普通荷兰风俗画」的分界（L225）。
- **何时失效**：near-miss **#8** 与卡拉瓦乔「暗区 std ≥1.5/255（非死黑）」取向相反 → 交集 [1.5, 5]，同帧取中点附近并**显式写值**（`conflicts.md` L354；`caravaggio.md` **L220**「暗部保细节：暗区（亮度<0.15）内部亮度标准差 ≥1.5/255」逐字命中；`vermeer.md` L236）。本轮把 AUDIT 的 `partial` 升级为 `supported`，见 [mechanism_notes.md](mechanism_notes.md) §冲突行 / [claim_evidence_map.md](claim_evidence_map.md) C-NM8。
- **grade**：`[归纳]`（阈值）/ `[研究]`（EV 描述）。定位：[vermeer.md](../../dossiers/vermeer.md) L33、L236、L88；`caravaggio.md` L220；`conflicts.md` L354。

<a id="db-source-line-55"></a>
### D4 — 把「细节预算」全部押在高光形状上 `[归纳]`
- **先选**：用 pointillés（1–3px / σ0.5–1 / 圆度>0.7）分档 **0–2 / 5–20 / 100+**（§8.2-3 L237、§4 P3 L89）；材质靠高光形状区分（锐利小点＝瓷、宽软面＝锡、哑光＝毛呢，§1-10 L40）。
- **牺牲**：轮廓线、逐根毛皮细描、显微镜式细节、「色的分解」。
- **为什么**：§3-1 L71「色调与轮廓的真实 > 细节的累积」（[R2][R12]）；§3-7 L77「材质＝光的证据链」；§2-13 L62「珍珠只用了两笔白颜料，没有挂钩、没有轮廓」（Mauritshuis，`[研究]`）。
- **何时失效**：① P3 到 100% 变成修拉式分割主义（L227 越界警报）；② 按卡拉瓦乔「亮度 ≥0.9×max 的高光连通域 ∈[2,5]」全帧统计 100+ 点 → C-11（`conflicts.md` L188–201）。但 §5.B #4 **L374 WEAKENED**：维米尔未给 pointillé 亮度阈值，故是**条件式互斥**，不能断言 100+ 点必然 ≥0.9×max；解法是拆「主光斑/点状高光」两类（L196–201）。
- **grade**：`[归纳]`（档位/阈值/决策）/ `[研究]`（pointillé 形态、珍珠两笔）。定位：[vermeer.md](../../dossiers/vermeer.md) L237、L89、L40、L71、L77、L62、L227；`conflicts.md` L188–201、L374。

<a id="db-source-line-62"></a>
### D5 — 主动「删」而不是「加」 `[归纳]`
- **先选**：物体边缘过渡带 **≥2px**、禁 1px 描边（§8.2-5 L239），P5 默认 80%（§4 P5 L91）；细节主动省略（耳环挂钩不画）。
- **牺牲**：硬轮廓、清晰边线、完整道具细节。
- **为什么**：Mauritshuis「Vermeer painted the girl without any hard lines … the hook for the earring – Vermeer did not paint that at all」（§1-7 L37，`[研究]`）；§12-2 L436「『省略』作为完成度」。
- **何时失效**：near-miss **#7**：维米尔「物体边缘过渡带 ≥2px」× 米开朗基罗「形体转折明暗过渡带 ≤0.6% 短边（1920 宽 ≈≤11.5px）」交集 [2,11.5] 非空但**量纲不同**（`conflicts.md` L353；`michelangelo.md` L176）；卡内必须写清测的是哪一个，否则自查脚本误判。
- **grade**：`[归纳]`（阈值）/ `[研究]`（无硬线引文）。定位：[vermeer.md](../../dossiers/vermeer.md) L239、L91、L37；`conflicts.md` L353；`michelangelo.md` L176。

<a id="db-source-line-69"></a>
### D6 — 先限色，再谈氛围 `[归纳]`
- **先选**：色相簇 ≤8、蓝相 200–230°/黄相 35–50°、阴影向蓝偏移 ≥15°（§8.2-4 L238）；P4 群青权重 60%（§4 P4 L90）；红只作小点缀（§1-6 L36）。
- **牺牲**：饱和多元色板、多组互补簇、霓虹色（模块 negative L39）。
- **为什么**：群青蓝×赭黄主色对 + 冷调阴影（§1-5 L35、§1-6 L36，`[研究]/[归纳]`）；群青当罩染用（§2-4 L51，`[研究]` [R3]）。
- **何时失效**：near-miss **#5** 北斋主色 ≤7 × 毕加索色相 ≤5 × 维米尔色相簇 ≤8 → 取 **≤5**（`conflicts.md` L351；`hokusai.md` L200、`picasso.md` L172，见 `AUDIT-vermeer/RESULT.md` L118–120）。
- **grade**：`[归纳]`。定位：[vermeer.md](../../dossiers/vermeer.md) L238、L90、L36；`conflicts.md` L351。

<a id="db-source-line-76"></a>
### D7 — 把动态范围夹在中间 `[归纳]`
- **先选**：受光面 ≤88%、暗部下限 ≥8%、禁纯白/纯黑（§8.2-7 L241）。
- **牺牲**：HDR、纯黑背景、纯白高光、强黑白对比。
- **为什么**：高调（§1-2 L32）、低动态范围（§1-11 L41）；`--no harsh chiaroscuro / pure black` 是模块护栏而非历史断言（L229 自注）。
- **何时失效**：near-miss **#1** 卡拉瓦乔背景 ≤0.10×max（`caravaggio.md` L215）× 维米尔暗部 ≥8% → 背景取 **[8%,10%]**，且「纯黑 ≤10%」在维米尔在场时收紧为 0%（`conflicts.md` L347）。
- **grade**：`[归纳]`。定位：[vermeer.md](../../dossiers/vermeer.md) L241、L32、L41、L229；`caravaggio.md` L215；`conflicts.md` L347。

<a id="db-source-line-83"></a>
### D8 — 用几何与表面收尾 `[归纳]`
- **先选**：单点透视（消失点 1 个、画面高 55–65%、地砖 29.3cm 等比方形，§8.2-6 L240）；P6 表面平滑 85%（§4 P6 L92，levigated / 织纹不可见，§1-12 L42）。
- **牺牲**：多点透视、可见笔触、厚涂、canvas weave。
- **为什么**：房间几何网格（§1-9 L39，`[研究]` Steadman [R14]）；成熟期「levigated effect」（§2-12 L62、§1-12 L42，`[研究]` [R2]）。针孔/圆规孔支持 pin-and-string 构造（§2-9 L56，`[研究]` [R5]）——注意这是**技法证据**，不是「维米尔决定这样构图」的自述。
- **何时失效**：早期历史画（P6 30%、P5 30% 硬边）与晚期《吉他手》《站在维金纳琴前的女子》（P6 40%、书法性笔触）都不适用成熟期默认值（[vermeer.md](../../dossiers/vermeer.md) L226、§12-10 L473–476）；§4 P6 弱档本身即反例。
- **grade**：`[归纳]`（阈值/时期切换）/ `[研究]`（Steadman、材料证据）。定位：[vermeer.md](../../dossiers/vermeer.md) L240、L92、L39、L42、L56、L226、L473–476。

---

<a id="db-source-line-92"></a>
## 2. 自述 vs 推断：显式对照（防越级）

| 说法 | 能否写 | 正确写法 | 定位 |
|---|---|---|---|
| 「维米尔主张把光当主题」 | ❌ | 「本项目 `[归纳]`：Steadman 引 Gowing 把光学视为风格引擎（§3-5 L75，`[研究]`）；操作化为单侧窗光主导」 | [vermeer.md](../../dossiers/vermeer.md) L69、L75、L87 |
| 「他认为细节不重要」 | ❌ | 「`[归纳]` 操作规则：色调/轮廓真实 > 细节累积（§3-1 L71）」 | L71 |
| 「他用暗箱直接描摹」 | ❌ 当自述 | 「`[研究]` 两派并列：正方 Steadman（§2-10 L58）/反方无文献痕迹（L59）；反方含 s'Gravesande（[vermeer.md](../../dossiers/_corpus/vermeer.md) L182–187）；未定论」 | L58–59；[vermeer.md](../../dossiers/_corpus/vermeer.md) L182–187 |
| 「他画得慢是因追求完美」 | ❌ 编造心理 | 「`[史料]/[研究]`：Montias 估 2–3 幅/年、Costaras 见分层干燥痕迹（§3-3 L73）；动机不作推断」 | L73 |
| 「他说过…」 | ❌ 结构性 0 条 | 任何「自述与原话」8 条全是 `[史料]`（他人记录，[vermeer.md](../../dossiers/vermeer.md) L99–140）；语料 22 条 0 条 `[self-written]` | `AUDIT-vermeer/claim-evidence-map.md` §A/§B/§C |

> 唯一允许的「作者侧」内容是：**结构性无自述这一事实本身**（`[史料]` 级，档案自声明 + 已列检索范围），以及它带来的使用禁令（A-40 caveat C1/C2/C3，`AUDIT-vermeer/claim-evidence-map.md` §C）。不得据此外推为「穷尽证明维米尔绝无一字留世」（`AUDIT-vermeer/RESULT.md` §1.1 L55）。

---

<a id="db-source-line-106"></a>
## 3. 何时整套决策序失效（总边界）

1. **跨模块组合**：C-09（×梵高）、C-11（×卡拉瓦乔，条件式）、C-08（×Lane B 运动模糊）、near-miss #1/#2/#3/#5/#7/#8 —— 必须按 `conflicts.md` §2/§4 显式取值或分层，否则静默折中/误判（[vermeer.md](../../modules/vermeer.md) L92–99）。
2. **时期不对**：早期历史画、晚期书法性笔触作品不适用成熟期默认 P5/P6（L226、§12-7/§12-10）。
3. **规则层未实测**：所有 §8.2 阈值 `[归纳]`、未做像素测量（[vermeer.md](../../dossiers/vermeer.md) L244；`conflicts.md` L420）；conflicts 的互斥是规则层判定，实测后可能修正。
4. **人评/学习成效未做**：本决策序是「建议练习的思考支架」，不是已证实的学习收益（`01-AUDIT.md` §8.1 L273）；`human_review.status=not_applicable`。
5. **外部来源未回源**：22 条语料、[R#] URL/扫描件未逐字核（AUDIT RESULT §2、unresolved #2）；本 lane 离线只读本机。
6. **§8.1b 明细不可寻址**：`experiments/E1_t1b/RESULTS_t1b.md §2`（[vermeer.md](../../modules/vermeer.md) L46）属已迁出实验目录，本机 unavailable（AUDIT RESULT §3、unresolved #3）——决策序不依赖该明细。

---

<a id="db-source-line-117"></a>
## 4. 与同目录产物的接口

- 练习阶梯（single-event → pointillé → quiet-surface）见 [learning_path.md](learning_path.md) §4。
- §4 参数/§8.2 规则 → 可执行练习的逐条映射、冲突行、失败条件见 [mechanism_notes.md](mechanism_notes.md)。
- 本文件每个 D 步的 claim 级定位见 [claim_evidence_map.md](claim_evidence_map.md) §HowToThink。
- 证据底本：内部证据 056cb11f78df0e19（未公开；来源记录由维护者保留）（ACCEPTED）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
