<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-mir_sayyid_ali；原正文 SHA-256 `6000d32beedf41441cb2a7b2a1962822a33371f52618ff5e036bbced3d3226ff`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-mir_sayyid_ali — claim_evidence_map

> 逐 claim 带 `文件:节:行号` 定位（沿用 ACCEPTED `AUDIT-mir_sayyid_ali/claim_evidence_map.md` 的 locator 纪律）。本片 locator 指向本包 4 文件 + 仓库只读输入 + AUDIT 产物。
> 等级：dossier §0 词表 `[自述]/[史料]/[研究]/[归纳]/[推测]`；support_status ∈ {supported, partial, conflict, unverified, not_applicable}。本片 `[推测]` 计数 = 0。
> 约定：`@ f008952365a77e140cbda3f3959d43ef000f9a22` = 仓库只读 commit；`AUDIT` 前缀 = 内部证据 efe5d74370878080（未公开；来源记录由维护者保留）；`LEARN` 前缀 = 内部证据 fe9ea9768f4d08da（未公开；来源记录由维护者保留）。**rows = dossier lines**：§B 每行精确锚定 dossier §8.2 一条规则的 `L<line>`。
<a id="db-source-line-6"></a>
## §A 依赖与输入（5 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-IN-01 | `dossiers/mir_sayyid_ali.md @ f008952365a77e140cbda3f3959d43ef000f9a22` sha256 `4819e4f61163852b6355e48fa0575ce917c1f73016eab21235cfce795d228223`；`§0`、`§1`、`§4`、`§8.2:L196-207`、`§12` | [史料] | supported | 开工现场 sha256sum 实测；本片全部机制/作品/阈值回源此档案 |
| LM-IN-02 | [mir_sayyid_ali.md](../../modules/mir_sayyid_ali.md) sha256 `1a18c2ba07fc122f0ddb9520348f68cd8407ee2c08d4d983e24c867940103585`（§4/§8.1/§8.2 抽取卡） | [史料] | supported | 同上；卡片与 dossier 逐字一致由 AUDIT 抽取契约保证 |
| LM-IN-03 | [mir_sayyid_ali.md](../../dossiers/_corpus/mir_sayyid_ali.md) sha256 `0db38d6aab5dd7a57c7e0e1dce338578ba7e5c9aeb39cd866c12b74dc34d1c9f`（引文逐条带回源） | [史料] | supported | 语料分级照用；本片不重跑 quote_audit |
| LM-IN-04 | [conflicts.md](../../../../cross/conflicts.md) sha256 `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | [史料] | supported | C 行预检口径沿用 AUDIT；命中情况按 AUDIT 报告携带 |
| LM-IN-05 | `ops/GOALS.md` sha256 `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144`；`01-AUDIT.md:L273` 建议练习口径 | [史料] | supported | A-30 §8.1 + 不写已证实学习收益 |

<a id="db-source-line-16"></a>
## §B §8.2 8 条规则逐条回源（8 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-R01 | `dossiers/mir_sayyid_ali.md:L197` §8.2-1「1. **事件动势群像规则**：画面含 ≥1 事件进行时（战斗/夜袭/救援/追逐）且人物 ≥8（群像档）；全静场判失败（弱档除外）。自查：事件计数 + 人体框计数。（依据：§3.1 轴②；[R19][R20]）」 | [归纳] | partial | §8.2 第 1 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R02 | `dossiers/mir_sayyid_ali.md:L198` §8.2-2「2. **细节密度规则**：高频细节区 ≥1——局部窗口的边缘密度高于全帧中位数 ≥1.5×（纹样/织物/建筑装饰可读）。自查：分块边缘密度统计。（依据：微书档 [R1][R19]）」 | [归纳] | partial | §8.2 第 2 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R03 | `dossiers/mir_sayyid_ali.md:L199` §8.2-3「3. **尖角几何岩规则**：沿水道出现的岩块以直线边为主（直线边 ≥2、圆润度低）。自查：形状近似（多边形拟合 + 直线边计数）。（依据：[R19]）」 | [归纳] | partial | §8.2 第 3 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R04 | `dossiers/mir_sayyid_ali.md:L200` §8.2-4「4. **小瞳孔眼白规则**：在可辨尺度下，人物眼部为点状瞳孔 + 可见眼白（人检；可选模板匹配）。自查：局部区域目检。（依据：Seyller「签名式清单」[R19]）」 | [归纳] | partial | §8.2 第 4 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R05 | `dossiers/mir_sayyid_ali.md:L201` §8.2-5「5. **无消失点规则（族征）**：全帧直线族中，平行后退线不得收敛——「消失点检验」= 0 组汇聚线（≥3 条线共点即失败）。自查：Hough 线检测 + 共点聚类。（依据：层叠平面 [R11][R19]；与贝赫扎德同…」 | [归纳] | partial | §8.2 第 5 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R06 | `dossiers/mir_sayyid_ali.md:L202` §8.2-6「6. **人物比例恒定规则（族征）**：人物高度不随「纵深」缩放；同帧人物高度方差 ≤15%。自查：人体框高度统计。（依据：无透视纵深语法 [R19]）」 | [归纳] | partial | §8.2 第 6 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R07 | `dossiers/mir_sayyid_ali.md:L203` §8.2-7「7. **融合风物规则**：印度元素 ≥1 处可辨（象/热带植物/印度建筑形制/深肤色人物）；「纯波斯」判弱档。自查：元素目检计数。（依据：转译轴 [R11][R8]）」 | [归纳] | partial | §8.2 第 7 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |
| LM-R08 | `dossiers/mir_sayyid_ali.md:L204` §8.2-8「8. **色彩与金层规则**：高饱和不透明色（S ≥0.5）面积 ≥30%；金区为**平涂点金**（区域内部明度动态范围 ≤5%、无光泽起伏）、面积 ≤5%、单列不计色数（C-15/N6 接口）。自查：HSV 掩膜 +…」 | [归纳] | partial | §8.2 第 8 条原文；阈值未像素实测（分母＝假想参考帧）→ 不升 supported |

<a id="db-source-line-29"></a>
## §C §1 视觉指纹（11 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-F01 | `dossiers/mir_sayyid_ali.md:§1-1`「\| 1 \| **大幅开本 + 棉布载体**（《哈姆扎纳马》档）：近方大幅叶，画在细密棉布上 \| 叶面长边 ≥60 cm（约 65–70 × 50–55 cm）；布纹/布底可见；画心近方形 \| `[史料…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F02 | `dossiers/mir_sayyid_ali.md:§1-2`「\| 2 \| **多层合装叶结构**：画（棉布）+ 书法（纸）+ 加固层胶合、边缘裁切 \| 画与文本对页；边缘有裁切痕；「四层胶合」结构 \| `[史料]` [R11][R19] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F03 | `dossiers/mir_sayyid_ali.md:§1-3`「\| 3 \| **微书级细节**：纹样/器物/织物/建筑装饰高密度可读（Met：「meticulous attention to detail」） \| 高频细节区 ≥1；局部纹理可读；细节不计成本 \|…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F04 | `dossiers/mir_sayyid_ali.md:§1-4`「\| 4 \| **物质世界的准确记录**（BM：「accurate depiction of the material world」）：器物、纺织、武器、陈设「记录式」呈现 \| 可辨器物/织物类型 ≥5…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F05 | `dossiers/mir_sayyid_ali.md:§1-5`「\| 5 \| **图案控（pattern）**：对精心描绘纹样的显著偏好（Seyller「签名式清单」之一） \| 毯纹/砖饰/织物纹样成组；纹样区 ≥2 \| `[研究]` [R19] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F06 | `dossiers/mir_sayyid_ali.md:§1-6`「\| 6 \| **签名式手法三件**：小瞳孔 + 可见眼白的人物；细密纹样；主题诗句上书上毯 \| 瞳孔点状、眼白可辨（可辨尺度下）；诗行 ∈ 画面物件 \| `[研究]` [R19][R16] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F07 | `dossiers/mir_sayyid_ali.md:§1-7`「\| 7 \| **尖角几何岩**：沿溪/水系的岩石为多角直线边（「lithic shards」），反复出现 \| 岩块直线边 ≥2；沿水道成组 \| `[研究]` [R19] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F08 | `dossiers/mir_sayyid_ali.md:§1-8`「\| 8 \| **事件动势群像**：战斗/夜袭/救援/追逐——「large, dynamic, and fantastic」（Welch 年表） \| 事件进行时 ≥1；人物 ≥8（群像档）；武器/马匹在…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F09 | `dossiers/mir_sayyid_ali.md:§1-9`「\| 9 \| **印度融合风物**：伊朗构图 + 印度动物/植物/建筑自然主义（V&A：Hindustani 传统） \| 印度元素 ≥1（象/热带树/印度建筑/深肤色人物） \| `[研究]` [R11]…」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F10 | `dossiers/mir_sayyid_ali.md:§1-10`「\| 10 \| **夜景与火光**（《城中夜》档）：灯光/火把照明的夜场景 \| 暖色光源点 ≥3；背景明度 ≤35%；深底暖点 \| `[史料/研究]` [R13][R20] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |
| LM-F11 | `dossiers/mir_sayyid_ali.md:§1-11`「\| 11 \| **对页/双叶设计单位**：画与文本对页一体；早期卷「一叶双画」 \| 文本栏/对页 ≥1；或双画叶结构 \| `[史料]` [R19][R11] \|」 | [研究] | partial | §1 视觉指纹逐条；现象级观察 + [归纳] 量化阈值 |

<a id="db-source-line-45"></a>
## §D 机制 / 练习 / 反例映射（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-P01 | `dossiers/mir_sayyid_ali.md:§4`（六控制参数表） | [归纳] | partial | 六参数档位；阈值未实测 |
| LM-P02 | `dossiers/mir_sayyid_ali.md:§8.2 尾注:L206`「> 以上阈值为本项目 `[归纳]`，**未对原作做像素测量**（分母 = 假想参考帧）；1/3/4 条与 §3.1 分工判据同轴，组合实验时以本节自查表为准。」 | [归纳] | supported | 明记未像素测量；本片据此不升级阈值 |
| LM-P03 | `LEARN-mir_sayyid_ali/mechanism_notes.md:§5`（8 条 counters，逐条回指 §8.2-1…§8.2-8） | [归纳] | partial | 反例为 [inference] 纸面推演，非已验证实验 |

<a id="db-source-line-53"></a>
## §E 诚实边界与 open（3 行）

| claim_id | locator（file:section:line + 子串） | grade | status | basis |
|---|---|---|---|---|
| LM-OPEN-01 | 内部证据 70248970276dd844（未公开；来源记录由维护者保留） | [史料] | supported | ACCEPTED 依赖；复用结论不重审、不改其产物 |
| LM-OPEN-02 | `01-AUDIT.md:L273` + `LEARN-mir_sayyid_ali/RESULT.md §4` | [史料] | supported | 练习=建议练习；human_review=not_applicable；无真人学习成效 |
| LM-OPEN-03 | `LEARN-mir_sayyid_ali/RESULT.md §5`（verify schema-only 门） | [史料] | supported | status=submitted / review=null / execution_dedup_key=null；作者不自接受 |


> 合计 **30 行**（§A5+§B8+§C11+§D3+§E3）。本节声明 total 与上方 `|` 数据行逐行核数一致；§B 的 8 行 = dossier §8.2 的 8 条规则（一规则一行、一 `L<line>`）。本片 `[推测]` = 0；无「已证实学习收益 / 已收口 / 已双向写死」正向主张。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
