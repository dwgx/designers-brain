<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-aivazovsky；原正文 SHA-256 `5f82a400d35cda4d7438c7f054594847e673c4ca450e5e163433242223ea1a08`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-aivazovsky — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-aivazovsky/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 009d90208b24dc69（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 106d1da5823ab194（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/aivazovsky.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `b78fdd7396b974b6cf85c516a6caaaf4c7f5c54860fb70ba4da53a4df765219c`；`§0`、`§1`、`§4`、`§8.2:L201-212`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [aivazovsky.md](../../modules/aivazovsky.md) sha256 `883b9681d0a0e9da50e68b7d5e715a879072a2dd674d5ac631a31415e9d53d11`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [aivazovsky.md](../../dossiers/_corpus/aivazovsky.md) sha256 `bf4c0c257b68b740f3151bedf8c68b5e7579b72f37b4d1f34e0a00df2204a6c9`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/aivazovsky.md:L202` §8.2-1「1. **透光浪体规则**：主浪面（非泡沫掩膜区）存在 ≥2 级由深到亮的连续明度阶梯（每级 ΔL ≥8/255、带宽 ≥2% 画幅），阶梯沿浪脊方向单调；泡沫区（高亮高频掩膜）面积 ≤30% 浪体。自查：分区明度直方图…」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/aivazovsky.md:L203` §8.2-2「2. **月光路径规则**：全帧高亮柱（L ≥0.9 且 S ≤0.25 的银白像素）构成**单一连通路径**，自发光体（唯一连通域）延伸至画面下部 ≥40% 画高；路径宽度沿远端收束（近宽远窄，比率 ≥2）；无第二发光…」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/aivazovsky.md:L204` §8.2-3「3. **低地平线规则**：开放海景帧地平线位于画面**下 1/3 带**（0.55–0.75 画高区间，自顶算 ≥55% 处）；天/海面积比 ≥1.2；天海交界线水平度 ±1.5°。自查：线检测 + 面积比。（依据：§…」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/aivazovsky.md:L205` §8.2-4「4. **泡沫花边规则**：泡沫以**高频细碎结构**呈现（边缘密度 ≥3 倍于浪面区），形态为线网/花边而非实心白块（实心白连通域面积 ≤泡沫总面积 25%）；泡沫只出现在脊线与落点，谷底无泡沫。自查：边缘检测 + 连…」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/aivazovsky.md:L206` §8.2-5「5. **双色温规则**：火水档帧内暖族（H 20–60°）与冷族（H 160–230°）面积各 ≥15%，且**暖族集中于光源/光路带、冷族集中于水体**（分区显著）；银灰档例外（全帧饱和 ≤0.25，规则改判「单色档…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/aivazovsky.md:L207` §8.2-6「6. **剪影规则**：船只/人物/建筑为深剪影（L ≤25%，细节线 ≤10 条/对象）；人物高 ≤10% 画高、无面部特征；剪影对象与高亮水面的明度差 ≥0.5。自查：对象分割 + 明度统计。（依据：§1-6）」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/aivazovsky.md:L208` §8.2-7「7. **平滑表面规则**：非泡沫区高频纹理能量 ≤ 泡沫区的 1/3；无厚涂阴影（局部对比度与画布纹理均匀）；笔触方向性 ≤弱（方向直方图熵高）。自查：频域能量 + 局部对比。（依据：§1-8「не исправлял…」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/aivazovsky.md:L209` §8.2-8「8. **浪峰定格规则（运动预算）**：动画帧间，浪脊线**不闭合**（无完整落水线）；主浪高度 ≥1/3 画高；帧间浪体位移 ≤2% 画幅/帧（「将落未落」的悬停态）；泡沫位移允许 ≤10%/秒（水在动、势能悬停）。自…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（10 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/aivazovsky.md:§1-1`「\| 1 \| **透明浪体（transparent wave body）**：浪不是色块而是**光可穿过的体积**——浪脊呈现 2–4 级由青绿到白的透光阶梯；浪面可读出「内部的光」，泡沫只出现在**脊…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/aivazovsky.md:§1-2`「\| 2 \| **月光路径（лунная дорожка）**：夜海有且仅有一条**发光路径柱**——从月亮/光源经水面直达近景，路径宽度沿透视收束；月亮为单一发光体、常隔「轻透明云」；水面对光的**反…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/aivazovsky.md:§1-3`「\| 3 \| **极低地平线＋天海二分**：开放海景中地平线压低（多为下 1/3 或更低），**天空占 ≥55–60%**；《黑海》式画面「除了天空和水一无所有」（Крамской）；云是天空层的主角…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/aivazovsky.md:§1-4`「\| 4 \| **火水对撞色温**：暖（红/橙/金——日落、火焰、月光偏暖版）与冷（青绿/铅蓝——水体、雨云）**同屏对撞**；暴风/夜战题材用「第二类配色」（Томилов 语：非自然色并列，在眼中产…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/aivazovsky.md:§1-5`「\| 5 \| **浪峰「将落未落」的定格**：戏剧点取在浪**尚未砸下**的一瞬（《九级浪》大浪悬于人群上方）；不画落定后的平寂，也不画完整崩解——取「最高势能」帧 \| 主浪脊线呈凸弧且**未闭合**（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/aivazovsky.md:§1-6`「\| 6 \| **人造物剪影**：船、桅、小艇、堡垒、城市轮廓以**深剪影**（L≤25%）压在高亮水面/天空上；人是**尺度单位**（≤1/10 画高，常更小），不画脸；人与海的关系＝渺小 vs 宏大…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/aivazovsky.md:§1-7`「\| 7 \| **水的形态库（三档循环）**：一生重复画水的**同一套状态目录**——штиль（镜平）/ зыбь（涌浪）/ буря（风暴），晚年加「прибой」（拍岸碎浪）档；同一构图换档重画是…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/aivazovsky.md:§1-8`「\| 8 \| **表面平滑（无厚涂）**：整体为**罩染＋一次成型的平滑面**——笔触隐没、无堆叠肌理；速度体现为「形准」而非「笔痕」（与梵高/莫奈的笔触可见度完全相反侧） \| 非泡沫区笔触可见度低（高…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/aivazovsky.md:§1-9`「\| 9 \| **记忆合成地理**：场景非写生拼贴——意大利的暴风搬到克里米亚海岸、博斯普鲁斯的月光照塞瓦斯托波尔（自述）；同一画面可有「不可同时出现」的光/地组合——**合成是常态不是失误** \| 地…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/aivazovsky.md:§1-10`「\| 10 \| **银灰晚年档**：1890 年代一批**近乎单色**的银灰海（铅灰天＋橄榄赭水＋珍珠母高光）；与 1840s 的「火色浪漫」、1870s 的「蓝色海」（голубые марины）构…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-44"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/aivazovsky.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/aivazovsky.md:§8.2 尾注:L211`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母＝假想参考帧）；1/2/4/6 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-aivazovsky/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-52"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 5719c7ef1f96eb50（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-aivazovsky/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-aivazovsky/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **29 行**（§A5+§B8+§C10+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
