<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hopper；原正文 SHA-256 `40aa2cbbb393564e93a0948ae38ec9bdd19ab21870ef8bb8da557145641854dc`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hopper — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-hopper/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 911675ebcf51e312（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 7a3d59ce762a7461（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/hopper.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `b9db59fcedfe8a7f11f1736a49e40c21f8049f36354a77ba0aff962edd935d09`；`§0`、`§1`、`§4`、`§8.2:L237-250`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [hopper.md](../../modules/hopper.md) sha256 `2b96411562be396a68092f38f08fb5d0d004b5e11f1da130c216090715f4b7b0`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [hopper.md](../../dossiers/_corpus/hopper.md) sha256 `5e59adb804abe76f361f012678c8f70d7a1f9ec03389ab1a3a76c77197e761f4`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/hopper.md:L240` §8.2-1「\| 1 \| **硬边光影** \| 亮暗边界过渡带 ≤2 px（1024 px 宽画布）；禁止 ≥8 px 的羽化渐晕 \| 对明暗交界做梯度宽度统计，取中位数 \|」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/hopper.md:L241` §8.2-2「\| 2 \| **投影几何一致** \| 所有投影方向同一光源方位（偏差 ≤5°）；投影为简单多边形（边数 ≤6） \| 投影主轴角度直方图 + 形状简化度 \|」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/hopper.md:L242` §8.2-3「\| 3 \| **正交几何主导** \| 建筑长边 ≥70% 与水平/垂直轴夹角 ≤2°；画面矩形块 ≥6 个 \| 边缘角度直方图 / 霍夫直线统计 \|」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/hopper.md:L243` §8.2-4「\| 4 \| **人烟预算** \| 人物数 ≤2（默认 0–1）；若有人物：占画面积 ≤8%，且无互动（视线不相交、无肢体接触） \| 人物检测 + 面积与视线向量检查 \|」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/hopper.md:L244` §8.2-5「\| 5 \| **色域与两级明度** \| 色相簇 ≤7；亮部（≥75%）与暗部（≤35%）像素合计 ≥60%，中间调压缩；夜档暖光池面积 ≤25% 且集中在光源/照射面 \| 逐帧直方图 + 色相聚类 \|」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/hopper.md:L245` §8.2-6「\| 6 \| **光源数受控** \| 昼档：1 个太阳方向；夜档：≤3 个可见光源，各带明确照射面；禁止无源漫射光 \| 高光/光源连通域计数 \|」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/hopper.md:L246` §8.2-7「\| 7 \| **全片静止** \| 相机固定；帧间差 ≤1%（除光源闪烁 ≤2 Hz 外不允许运动元素） \| 帧差图：非光源区域非零像素占比 \|」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/hopper.md:L247` §8.2-8「\| 8 \| **画中框取景** \| 至少 1 个画中框（窗/门/镜/柜台）且被画边裁切 ≥1 处；主体（若存在）距画面中心 ≥1/8 宽 \| 边界框位置与边缘相交统计 \|」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（12 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/hopper.md:§1-1`「\| 1 \| **硬边光影（crisp light/shadow）** \| 亮暗边界过渡带窄；投影边缘锐利、方向一致且平行（如 *Early Sunday Morning* 消防栓与理发杆"long,…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/hopper.md:§1-2`「\| 2 \| **几何化建筑块面** \| 建筑/窗/墙被简化为矩形；"radically simplified geometry"（Whitney）；边缘多为水平/垂直直线段 \| `[研究]`（[R1]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/hopper.md:§1-3`「\| 3 \| **无人 / 稀疏人烟** \| 画面"human-scale and largely unpopulated"（Whitney）；MoMA："devoid of or sparsely p…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/hopper.md:§1-4`「\| 4 \| **窗 / 门槛母题（frame-in-frame）** \| "The window became one of Hopper's most enduring symbols"（Whitn…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/hopper.md:§1-5`「\| 5 \| **夜间人造光 / 霓虹** \| 夜档画面由"光池"构成：餐车/橱窗/加油站灯光在深色环境里形成高对比亮区（*Nighthawks*"harsh electric light"；"acid…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/hopper.md:§1-6`「\| 6 \| **日光本身是主角** \| 光斑作为明确几何形状落在墙面/地面；晚期 *Sun in an Empty Room*（1963）为"pure study of sunlight"；Troye…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/hopper.md:§1-7`「\| 7 \| **电影式取景 / 非常规裁切** \| 视点"cinematic—from the sidewalk"（*Nighthawks*）；"As if he were creating stil…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/hopper.md:§1-8`「\| 8 \| **低饱和场 × 局部饱和色对撞** \| 整体灰调（赭/砖红/橄榄绿/骨白）中放少量高饱和点（红理发杆、绿店面、黄加油泵、蓝天空）；"used saturated color to hei…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/hopper.md:§1-9`「\| 9 \| **凝滞的瞬间（frozen moment）** \| 无动作；人物"captured just before or just after the climax of a scene"；"S…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/hopper.md:§1-10`「\| 10 \| **孤独人物（多为女性、背对/低头）** \| 单人为主：读书、望窗、工作；背或侧身、面部无细节；*Automat*、*Hotel Room* 为典型 \| `[研究]`（[R20]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/hopper.md:§1-11`「\| 11 \| **"霍珀式房屋"原型** \| 孤立建筑（维多利亚/曼萨德屋顶、塔楼）与周围环境成对比；*House by the Railroad* 为原型，"turrets and towers... cast wonderful shadows" \| `[研究]`（[R20][R25]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F12 | `dossiers/hopper.md:§1-12`「\| 12 \| **水平色带分割** \| 天空/建筑/地面（或墙/床/地板）构成 3–4 条水平或斜向色带；*Hotel Room*："spare vertical and diagonal bands of color"（Levin） \| `[研究]`（[R20]） \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-46"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/hopper.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/hopper.md:§8.2 尾注:L249`「> 说明：全部阈值为 `[归纳]`（本项目操作化建议），未经渲染实验校准；与 [style_card.md](../../../../../templates/style_card.md) 的填写规则对齐。第 5 条的"两级明度"对应 *Nighthawks*…」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-hopper/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-54"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 843e9b0f1ae06797（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-hopper/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-hopper/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **31 行**（§A5+§B8+§C12+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
