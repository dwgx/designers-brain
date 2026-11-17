<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-namatjira；原正文 SHA-256 `27d9199eaa75a1f69ddd8eef9f610ef9cfab4cd987779880ae762b5e993db3cd`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-namatjira — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-namatjira/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 8c631c77c5bca578（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 27be7614eb6b5088（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/namatjira.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `c39536d33a02303222e15b9c5bc6062523a26df2bc567c20d4023cb1694d4aff`；`§0`、`§1`、`§4`、`§8.2:L238-251`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [namatjira.md](../../modules/namatjira.md) sha256 `9126af70a17dc1279a1102fe4ae0ca3e087fe120925019fd634699399ddc759d`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [namatjira.md](../../dossiers/_corpus/namatjira.md) sha256 `f47cf44555c8731a725153e1ff3bdf88a8db40fd52bce6ef295afb8eb2008455`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/namatjira.md:L241` §8.2-1「\| 1 \| **远山色相位移** \| 远景带（画面上 1/3 山体区）平均色相 vs 前景带位移 ≥25°（向蓝紫）；明度对比逐带递减 \| 分带色相直方图 + 带间 ΔH 计算 \|」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/namatjira.md:L242` §8.2-2「\| 2 \| **地平线与层带** \| 地平线位于画面高度 35–60%（自上而下计）；层带 ≥3 条（前景/中景/远景）；天空带 ≤40% \| 水平边缘检测 + 带划分 \|」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/namatjira.md:L243` §8.2-3「\| 3 \| **色数预算（土色系）** \| 同屏色相簇 ≤7（赭红/土黄/紫灰/深蓝/纸白 + ≤2 点缀）；饱和度均值 ≤55%、峰值 ≤75%；互补色对撞面积 ≤10% \| 逐帧直方图 + 色相聚类 \|」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/namatjira.md:L244` §8.2-4「\| 4 \| **白干桉剪影** \| 树档：≥1 株近垂直白干（值 ≥85%、干宽 ≤4% 画幅、分叉 ≥2）；非树档允许 0 株但须有山体剪影（轮廓可辨） \| 连通域明度筛选 + 形状检查 \|」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/namatjira.md:L245` §8.2-5「\| 5 \| **天空空场** \| 天空区域 ≥20% 画幅；云覆盖 ≤15%；无事件性云型（积雨云/风暴云纹理） \| 分块明度/纹理统计 \|」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/namatjira.md:L246` §8.2-6「\| 6 \| **分层罩染可见度** \| 岩面/山体每块 ≥3 个明度台阶（步长 ≤12%/级），无单色平涂大块；可选档：检出底稿线残留 \| 明度分层计数 + 边缘图（可选） \|」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/namatjira.md:L247` §8.2-7「\| 7 \| **静场运动预算** \| 视频档：无天气运动；仅允许 ≤1%/s 的光色慢调制；帧间差 ≤1.5%；无溶解/位移 \| 帧差图 + 调制曲线拟合 \|」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/namatjira.md:L248` §8.2-8「\| 8 \| **文化合规检查** \| 素材与语义清单核对：神圣/仪式专属元素 0 个；人物 0–2 个且非仪式场景；无文字/签名/品牌；无冒充署名 \| 清单对照 + OCR 扫描 \|」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/namatjira.md:§1-1`「\| 1 \| **白干桉（ghost gum）剪影** \| 近垂直白干＋分叉枝，明度 ≥85%（纸白＋极淡灰）；"luminous white trunks"；树可裁切为"肖像" \| `[研究]`（[R…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/namatjira.md:§1-2`「\| 2 \| **远山转色（距离色）** \| 中远景山体色相随距离向紫/蓝位移（红褐→紫灰→蓝紫）；明度对比随距离下降 \| `[研究]`（[R2] "transformations"；[R9]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/namatjira.md:§1-3`「\| 3 \| **高地平线＋层带构图** \| 山体占画面上半为主，天空带 ≤40%；"repetition, detailed patterning and high horizons"（ADB） \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/namatjira.md:§1-4`「\| 4 \| **透明水彩分层** \| 同一区域多次回到、变体淡彩叠加（variant washes）；色层薄而透，无厚涂 \| `[研究]`（[R2] "looking"） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/namatjira.md:§1-5`「\| 5 \| **铅笔/石墨底稿可见** \| 馆藏介质记录"watercolour over pencil / watercolour, pencil on paper"；山脊线与树位有底稿痕 \| `[…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/namatjira.md:§1-6`「\| 6 \| **峡谷/隘口题材** \| Angkerle（Standley Chasm）、Runutjirba（Simpson's Gap）、Ntaripe（Heavitree Gap）、Kwarta…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/namatjira.md:§1-7`「\| 7 \| **独立山峰的"profile"处理** \| 从平原上独立升起的峰（Rutjipma/Atila/Central Mount Wedge）以侧影轮廓为主、少"移动阴影" \| `[研究]`（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/namatjira.md:§1-8`「\| 8 \| **天空空场** \| 大面积深蓝或晨昏纯色天空，云少或无云；"deep blue Centralian Sky"（Clune 目击） \| `[史料]`（[R9] 转录 Clune 1957…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/namatjira.md:§1-9`「\| 9 \| **三带式前景—中景—远景** \| 前景树/岩、中景河床滩地（Lhere pirnte 等）、远景山体；水（水潭/河床/洪水痕）为中景枢纽 \| `[研究]`（[R2][R5]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/namatjira.md:§1-10`「\| 10 \| **水的在场与缺席** \| 水潭、河床、冲刷痕；"Water is a powerful presence; it is the central dynamic for change"（…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/namatjira.md:§1-11`「\| 11 \| **土色系为主的色域** \| 赭红、土黄、紫灰、深蓝、纸白；饱和对比克制，无互补对撞；"his colours were similar to the ochres that his ancestors had used"（Wikipedia 综述，需回核） \| `[研究]`（[R9]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/namatjira.md:§1-12`「\| 12 \| **署名不署日期** \| 右下 "ALBERT NAMATJIRA"（红/黑/棕颜料）；早期 "ALBERT"（红漆）；馆藏记录 "Not dated" \| `[史料]`（[R6][R7]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/namatjira.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/namatjira.md:§8.2 尾注:L250`「> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 [style_card.md](../../../../../templates/style_card.md) 的填写规则对齐。第 8 条为本模块特有的伦理验收项（与档案头部"文化伦…」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-namatjira/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 cc7f2a8084caf3c6（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-namatjira/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-namatjira/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
