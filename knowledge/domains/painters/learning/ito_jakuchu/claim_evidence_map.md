<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-ito_jakuchu；原正文 SHA-256 `918e7ceba222b82b5576e7f4aec42c8bca1c2dfe839d888ab1e985b4469e5be2`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-ito_jakuchu — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-ito_jakuchu/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 2544b58c37400330（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 ac71fa648ea542ab（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/ito_jakuchu.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `0ed28b154198a0668f07a1df4b821909b679da0cc188f7b605133b789b82cac1`；`§0`、`§1`、`§4`、`§8.2:L234-243`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [ito_jakuchu.md](../../modules/ito_jakuchu.md) sha256 `7b07c0cf93d92b7eb2de39ed4f844ecdaefd74af49cb434e874b973eacf228df`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [ito_jakuchu.md](../../dossiers/_corpus/ito_jakuchu.md) sha256 `775898e51e1b1129bfa995e743b6bea0b3099d249710acd0f86ddda60a505d19`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/ito_jakuchu.md:L235` §8.2-1「1. **无描边**：不存在宽度 ≥2px 且连续长度 >20px 的均匀深色轮廓线；相邻色区边界色差 ΔE ≥ 15（边界可读但不靠线）。」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/ito_jakuchu.md:L236` §8.2-2「2. **彩度/色数**：色相簇 8–14 个；饱和像素（S ≥ 40%）占比 ≥55%；平均饱和度 ≥50%；低饱和区（S <15%）≤15% 面积。」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/ito_jakuchu.md:L237` §8.2-3「3. **填充率**：主体覆盖 ≥85% 画面；最大连续背景空区 ≤8% 面积；空区只能作水面/天空且必须带色（不得为白纸）。」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/ito_jakuchu.md:L238` §8.2-4「4. **升目模式（P3=100% 时）**：格边长 = 画面短边的 1/40–1/120；跨格渐变 = 0（相邻格独立取色）；每格主色数 = 1（允许格角 1 处加深）；格线对齐误差 ≤0.3 格。」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/ito_jakuchu.md:L239` §8.2-5「5. **裏彩代理（图像级）**：白/浅色区色温相对中性偏暖（+200~600K）；镜面高光（亮度 >95% 且低饱和的孤立斑点）面积 ≤0.3%；「金色感」只能来自暖白+明度层次，不得出现金属反射带。」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/ito_jakuchu.md:L240` §8.2-6「6. **姿态冻结（动画）**：主体像素位移 ≤1px/帧；允许的动只有极慢介质（水波 ≤2px/帧、无风感）；禁止翅膀/尾羽/花瓣的连续摆动（对照北斋「曲线族动势」互斥）。」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/ito_jakuchu.md:L241` §8.2-7「7. **重复模板**：同类单元（鸟/鱼/花/虫）出现 ≥5 个时，姿态模板 ≤3 种；模板的分布呈图案节奏（间距变异系数 ≤0.3），不得随机散布。」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/ito_jakuchu.md:L242` §8.2-8「8. **墨线规则**：墨只作两种用途——极细结构线（宽 ≤1.5px）与点/苔；不得用墨做大面积暗部（暗部由深色染料/颜料叠加，暗部不得出现纯黑 <5% 明度区块 >2% 面积）。」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（11 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/ito_jakuchu.md:§1-1`「\| 1 \| **无轮廓成形**：不靠描边线，形与形由色面直接相接 \| 边缘处无等宽深色线；切形靠色差/明度差 \| `[研究]`（[R9] "the absence of outlining"） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/ito_jakuchu.md:§1-2`「\| 2 \| **色彩浓密**：高彩度、多色相、低饱和区极少 \| 饱和面积占比高；色相簇 ≥8 \| `[研究]`（[R3][R10]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/ito_jakuchu.md:§1-3`「\| 3 \| **正反两面叠色（裏彩色）**：颜色也上在绢背 \| 白色区带暖调、厚度感；同色比单面更深 \| `[研究]`（[R9][R11][R18]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/ito_jakuchu.md:§1-4`「\| 4 \| **高填充率**：画面几乎被主体填满 \| 空区（水面/天空通道外）≤15% \| `[研究]`（[R9]：no.22 几乎全画面） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/ito_jakuchu.md:§1-5`「\| 5 \| **母题重复成图案**：群雀/群鱼姿态高度重复 \| 同一姿态模板重复 ≥10 次（群雀 58 羽） \| `[研究]`（[R10]「空間に貼りついた文様」） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/ito_jakuchu.md:§1-6`「\| 6 \| **静态定格**：戏剧性姿态但完全冻结，无风动、无动线 \| 无主导动势线；主体零位移 \| `[归纳]`（对照 [R3][R10] 图版） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/ito_jakuchu.md:§1-7`「\| 7 \| **网格量化（升目）**：全画面 1cm 级方格逐格上色 \| 方格边长≈1cm；跨格渐变=0；格角加深处 \| `[研究]`（[R2][R5]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/ito_jakuchu.md:§1-8`「\| 8 \| **墨彩双轨**：浓彩花鸟 ↔ 水墨逸品画风并存 \| 同作者两种极端（彩色/一色） \| `[研究]`（[R6][R13]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/ito_jakuchu.md:§1-9`「\| 9 \| **点描材质**：石質/苔用点的大小浓淡造质感 \| 点密度变化对应表面 \| `[研究]`（[R14]：石燈籠「大小の無数の点」） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/ito_jakuchu.md:§1-10`「\| 10 \| **「白羽の下に金泥」**：白不用金而似金 \| 白色区暖色偏移；无金属镜面反射 \| `[研究]`（[R11]：太田彩语） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/ito_jakuchu.md:§1-11`「\| 11 \| **版画负像**：拓版画=黑地白图（阴刻） \| 地部满黑、图样留白；无常规阳刻线 \| `[研究]`（[R7][R15]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-45"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/ito_jakuchu.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/ito_jakuchu.md:§8.2 尾注:L242`「」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-ito_jakuchu/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-53"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 e0bbc965838b2ef3（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-ito_jakuchu/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-ito_jakuchu/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **30 行**（§A5+§B8+§C11+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
