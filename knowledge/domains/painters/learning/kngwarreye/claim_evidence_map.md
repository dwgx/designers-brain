<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-kngwarreye；原正文 SHA-256 `22581398f90c0dd81136b7ee3e179aadea15330be42a0f0988844a85035a52b9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-kngwarreye — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-kngwarreye/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 8209195d65f28b40（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 f5bb52eff413859e（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/kngwarreye.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `af2c129d453ffd225ece59fe9b1fcb8b4c2543997bfb74b0689fe9cf165663eb`；`§0`、`§1`、`§4`、`§8.2:L221-234`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [kngwarreye.md](../../modules/kngwarreye.md) sha256 `215887d4229eaa1b6561de5bfebb0229958429c16f9f5c61b37e525b91c5de50`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [kngwarreye.md](../../dossiers/_corpus/kngwarreye.md) sha256 `ce51f59fe37b949f8d93c6837e2ba314cf5bb0761970dc59541f62032a3da470`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/kngwarreye.md:L224` §8.2-1「\| 1 \| **点场覆盖与脉动** \| 点场覆盖率 60–95%；沿画幅滑窗密度方差 ≥0.02（≥2 个涨落峰） \| 逐帧分块密度统计（8×8 滑窗） \|」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/kngwarreye.md:L225` §8.2-2「\| 2 \| **手势尺度方差** \| 点径 p90/p10 ≥ 4；同帧内 ≥3 种尺度档共存；禁止单一同径点阵 \| 连通域尺寸分布统计 \|」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/kngwarreye.md:L226` §8.2-3「\| 3 \| **全幅无方向** \| 旋转 90° 后密度直方图差异 ≤5%；无主导水平/垂直轴向（边缘角度直方图无 >35% 单峰） \| 旋转不变性检查 + 边缘角度直方图 \|」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/kngwarreye.md:L227` §8.2-4「\| 4 \| **线网自由度** \| 线档：允许连续缠绕长线（≥1 条贯穿 ≥1/2 画幅）；线宽可变（p90/p10 ≥ 2.5） \| 线骨架提取 + 宽度统计 \|」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/kngwarreye.md:L228` §8.2-5「\| 5 \| **色域分期（四档选一）** \| 同屏色相簇 ≤8；黑底条纹档条带 ≥6 条且黑底占比 ≥45%；亮色档饱和度峰值 ≥70% 但平均 ≤45% \| 逐帧直方图 + 色相聚类 \|」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/kngwarreye.md:L229` §8.2-6「\| 6 \| **呼吸式运动预算** \| 全片无叙事位移；密度/尺度调制幅度 ≤2%/s；帧间差 ≤1.5% \| 帧差图 + 调制曲线拟合 \|」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/kngwarreye.md:L230` §8.2-7「\| 7 \| **语义锚点预算** \| 锚点（三趾印/块根/岩孔类）0–3 个，单个面积 ≤2%，且被点/线覆盖 ≥50%（"半淹没"） \| 形状检测 + 覆盖比例检查 \|」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/kngwarreye.md:L231` §8.2-8「\| 8 \| **文化合规检查** \| 素材与语义清单核对：神圣/仪式专属元素 0 个（清单外元素为 0）；无文字/签名/品牌 \| 清单对照 + OCR 扫描 \|」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/kngwarreye.md:§1-1`「\| 1 \| **全幅图案场（all-over field）** \| 无地平线、无消失点、无中心焦点；四个画边等权；"no right way up"（挂哪个方向都不算倒） \| `[研究]`（[R37]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/kngwarreye.md:§1-2`「\| 2 \| **点阵（dot field）** \| 点=种子/花/植物的符号（Ntange 草籽、kam 山药籽）；"dots within dots"（点内套点）；点径从针尖到指节跨度极大 \| `[…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/kngwarreye.md:§1-3`「\| 3 \| **线网（line network）** \| 缠绕的连续线束=山药藤/地下块根/地面裂纹（NGV：白色线网 = 地面裂缝＋地下块根）；单线连续 \| `[研究]`（[R10]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/kngwarreye.md:§1-4`「\| 4 \| **条纹/身体图式（stripes/awelye）** \| 黑底上白/彩粗条＝女性体绘（awelye）图式；条纹随笔势轻微起伏、不修边 \| `[研究]`（[R3][R20][R21]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/kngwarreye.md:§1-5`「\| 5 \| **手势性（gestural）** \| 笔触带速度感与刷毛痕；"raw gesture"（生猛手势）；"seething, linear"（翻涌的线）；完成一幅即放下笔走开 \| `[研究]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/kngwarreye.md:§1-6`「\| 6 \| **色域分期演化** \| 早期红黄赭/黑/白 → 1990 起灰、紫、棕（氛围）→ 亮色爆发（"dump dump"）→ 黑底白线（1995）→ 晚期粉彩色块（1996） \| `[研究]`…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/kngwarreye.md:§1-7`「\| 7 \| **大尺幅＋多联屏** \| 常见 2–9 m 级；22 联屏（Alhalker suite）、4 联屏（Earth's Creation）、18 联屏（Utopia panels）；8×3…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/kngwarreye.md:§1-8`「\| 8 \| **分层叠加（layering）** \| 底色→线层→点层→再覆盖；"layering of colour upon colour"（MCA）；层与层互相"拉开"（pulling apar…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/kngwarreye.md:§1-9`「\| 9 \| **点的呼吸/振荡** \| 点场密度涨落（oscillating pinpoints；"expand or contract across the surface"）；整幅呈现脉动感 \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/kngwarreye.md:§1-10`「\| 10 \| **不签名、不落款** \| AGNSW 馆藏记录："Not signed. Not dated."；无个人标记 \| `[史料]`（[R18]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/kngwarreye.md:§1-11`「\| 11 \| **语义锚点会"沉入"点阵** \| 三趾鸸鹋脚印、山药块根、岩石孔洞等具象锚点先出现、后被点场淹没（"submerged or disappear completely"） \| `[研究]`（[R21][R6]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/kngwarreye.md:§1-12`「\| 12 \| **材料痕迹与哑光表面** \| 丙烯不透明、无罩染、无渐变；干笔与飞白可见；画布边缘不收齐（地面作画的自然痕） \| `[研究]`（[R37][R21]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/kngwarreye.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/kngwarreye.md:§8.2 尾注:L233`「> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 [style_card.md](../../../../../templates/style_card.md) 的填写规则对齐。第 8 条为本模块特有的伦理验收项（与档案头部"文化伦…」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-kngwarreye/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 cdf6cd926214a7aa（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-kngwarreye/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-kngwarreye/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
