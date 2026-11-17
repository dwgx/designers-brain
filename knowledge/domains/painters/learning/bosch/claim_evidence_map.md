<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-bosch；原正文 SHA-256 `3325f778197f86eff6f03214e227328bee098dee8c5e9d0f55dcb1cb62ef5578`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-bosch — claim / evidence 图（逐 claim 带定位）

> TASK_ID `LEARN-bosch` · A-30 · 消费 `AUDIT-bosch`（ACCEPTED，`receipt.json status=accepted`）作为证据底本，复用其 locator 纪律与 §4 反例 A / 身份门 proposal / rights 10 行，**不重审、不改写**。
> Repo 只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22`；唯一写区 内部证据 e5069c7b42e76424（未公开；来源记录由维护者保留）。
> locator 格式 = `文件:节:行号`（或 内部证据 ddf6734dea92fa8c（未公开；来源记录由维护者保留））；AUDIT 的 78 行 claim map 由 `audit_scripts.py` 程序化解析（78 = 50 supported + 22 partial + 6 unverified + 0 conflict，同源同次统计），本文件引用其行号/claim_id，不另造分母。
> 等级沿用原档：`[自述]`（**0 条**）· `[史料]` · `[史料-转记]` · `[研究]` · `[归纳]` · `[推测]`；`[inference]` 用于反例 A / 身份门 proposal（规则级，非史实）。

<a id="db-source-line-8"></a>
## 输入 SHA-256（开工现场 `sha256sum` 复核，与 ledger / AUDIT 一致）

| 对象 | 路径 | sha256 | 用途 |
|---|---|---|---|
| dossier | [bosch.md](../../dossiers/bosch.md) | `fd4bc602e71a5631a28cfd8ac5e49a981035c26ef2c51ff89671fb30f290be3f` | §0–§4 / §8.2 / §10 / §12 全部定位 |
| card | [bosch.md](../../modules/bosch.md) | `66a06edd111e0f0f2417f8e9cb9797491269b8a9b69e304f109249f76f1037c2` | §8.1 / §8.2 / §4 卡侧 + 冲突注记 L78/L83 |
| corpus | [bosch.md](../../dossiers/_corpus/bosch.md) | `bf58f6ac7eb5bbc8e5958b2d6e98edff882e92def568f461bf02ea412b280f91` | 26 条语料；L4/L211 = 无自述声明 |
| conflicts | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 零 bosch 行 + 7 漂移 + near-miss 16 行 |
| goals | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | A-46 历史行（L129） |
| AUDIT RESULT | 内部证据 2573d9fe9e3debd0（未公开；来源记录由维护者保留） | `af7686c2afb4b530424f3eb2af44d8328439a3a84d5735431f2e52e8614ff52a` | §4 反例 A / §5 外部 / §6 漂移 / §7 限制 |
| AUDIT claim map | 内部证据 2f22d4365101af06（未公开；来源记录由维护者保留） | `9791a048dff779416c03539c013553d20491d2c95716a3db1c4c42ac2abfd911` | 78 行 + §5 corpus 逐条 + §4 8 参数 + §8 漂移表 |
| AUDIT coverage | 内部证据 2e7a179b9e30b41b（未公开；来源记录由维护者保留） | `22e9e9107faf766f03c5c18769ac31f5cc2efbe8f6f0fc5552e69c3477cb5c9d` | quote_count=26 / zero_self_statements / image 10 / license 分布 |
| AUDIT rights md | 内部证据 6d37e138cd77f9ac（未公开；来源记录由维护者保留） | `0c5d82870fc6e2ad6e219e2d41fc2a939758e7fe892f07a3d738e2db6e4d7942` | 10 行权利 + 2 争议 + 注 A PDM |
| AUDIT rights json | 内部证据 c73cd07262da0cd2（未公开；来源记录由维护者保留） | `b25c0615d4354536cfb3324c99eb303931def9bb0d6437917eaf65245caaab3e` | images[].file_sha256 全 10 张 |
| AUDIT review-evidence | 内部证据 ab4450309b0e12d5（未公开；来源记录由维护者保留） | `4a73d131526f72ca6bb553fb3be7908072b6b0d2666da3f5e5e6b6baff0a8b6b` | 独立 gate 逐字段复核 |
| AUDIT receipt | 内部证据 b570c3f261f0270c（未公开；来源记录由维护者保留） | `d768aea206e09b4743faf5b1f34cdb08c29e4d6cab582f17b1229f6ed9a331f1` | 确认 `status=accepted` / author=AuditBosch / reviewer=ReviewGateAUDIT-bosch |
| AUDIT runner | 内部证据 3b17c01968b6cc3f（未公开；来源记录由维护者保留） | `eacdc09e5ba38c6acac2d951894eb16abf95d78cca87bf4aed8f24a992f30f6b` | 执行记录 |
| AUDIT scripts | 内部证据 90e126fe9899217f（未公开；来源记录由维护者保留） / `.out` | `bbd20ea6…` / `2b38b87e…` | 78 行程序化复核 / locator 解析 |
| package 00-GOAL | 内部证据 49ff27e7b1c8e2c3（未公开；来源记录由维护者保留） | — | L9 自述/推断分离 |
| package 01-AUDIT | 内部证据 658354c7d03f3bb7（未公开；来源记录由维护者保留） | — | §8.1 L269–L273 / §8.4 L308–L310 |

> ledger `artist-shards.json`（冻结副本 内部证据 fab0092a7013b137（未公开；来源记录由维护者保留），sha `e1ec2d11…9`）的 bosch 三 hash 与现场实测一致；`corpus_quotes=26` / `images_public=10` 沿用 AUDIT，不重设分母。

<a id="db-source-line-31"></a>
## §A 结构 / 证据分级 / 零自述（learning_path §1、how-to-think §0/§2）

| claim_id | 主张 | kind / status | locator |
|---|---|---|---|
| LB-A46-ZERO-SELF | 博斯无任何存世文字；全文 `[自述]=0`，26 条语料零自写 | fact / supported | [bosch.md](../../dossiers/bosch.md):L7（卷首特殊性）、:§10-1:L306、:[bosch.md](../../dossiers/_corpus/bosch.md):L4/L211；`AUDIT-bosch/RESULT.md`:§3；`coverage-manifest.json`:`quote_audit.zero_self_statements=true`；`AUDIT-bosch/claim_evidence_map.md`:§0 头注 + §5 表头 |
| LB-QUOTE-26-TYPES | corpus 26 条 = `[contemporary record]`12 / `[early account]`12 / `[research]`2；26/26 有中文意译，逐条标原文语种 | fact / supported | `AUDIT-bosch/coverage-manifest.json`:`quote_audit.{type_tag_counts, chinese_translation_per_quote}`；[bosch.md](../../dossiers/_corpus/bosch.md):L13–L202（26 个 `###` header，行号见 coverage `denominator`）；`AUDIT-bosch/claim_evidence_map.md`:§5 逐行 |
| LB-GRADING-5 | 证据分级 = `[自述]`（0）/`[史料]`/`[史料-转记]`/`[研究]`/`[归纳]`/`[推测]`；`[归纳]` 明确「不冒充艺术家内心」 | fact / supported | [bosch.md](../../dossiers/bosch.md):L5（分级定义）、:L61（口径提醒「本档案不写他心里想的」） |
| LB-NO-PSYCH | How-to-Think 不得从画面外观编造作者心理、不得把 agent 解释冒充作者原意 | fact / supported | 内部证据 49ff27e7b1c8e2c3（未公开；来源记录由维护者保留）:L9；内部证据 68fa178b402cc451（未公开；来源记录由维护者保留）:L14；[bosch.md](../../dossiers/bosch.md):L61 |
| LB-TWO-DEVICES | 两件装置 = 混合生物语法 + 全景道德叙事；能力标签 5 个 | observation / supported | [bosch.md](../../dossiers/bosch.md):§0:L18（能力定位）、:L19（标签）；`AUDIT-bosch/claim_evidence_map.md`:§0 BO-HIST-01 |
| LB-INPUT-3CLASS | 三类输入 = 档案记录 / 早期文献 / 本项目操作规则 | fact / supported | [bosch.md](../../dossiers/bosch.md):L7；`AUDIT-bosch/RESULT.md`:§3（0 条自述 + 已记录口径分歧） |
| LB-D-SEQ-INDUCTION | how-to-think D1–D9 全部为研究者构造 `[归纳]`，非自述 | fact / supported | [how-to-think.md](how-to-think.md):§0 表 / §1 各 D 步标题 / §2 硬对照；[bosch.md](../../dossiers/bosch.md):L5；内部证据 49ff27e7b1c8e2c3（未公开；来源记录由维护者保留）:L9 |

<a id="db-source-line-43"></a>
## §B 重点作品及来源（learning_path §2，全部引用现有记录）

| claim_id | 主张 | kind / status | locator |
|---|---|---|---|
| LB-WORKS-10 | §12 的 10 件代表作「看什么/学什么/怎么练」可寻址，与主轴三件套对应 | fact / supported | [bosch.md](../../dossiers/bosch.md):§12:L385–L439（10 件 + L439 组合练习建议）；:L21–L25（5 件关键作品带馆藏） |
| LB-WORK-TRIPTYCH | 《人间乐园》三联 = 伊甸—人间—地狱三幕 + 编目式中央板 + 两缘成对猫头鹰 | observation / supported | [bosch.md](../../dossiers/bosch.md):§12-1:L389–L392；:§1-10:L42；`AUDIT-bosch/rights_review.md`:§1 第 1 行 |
| LB-WORK-PROVERB | 《干草车》= 谚语「世界=干草车」图像化 + 阶层队列 | observation / supported | [bosch.md](../../dossiers/bosch.md):§12-2:L394–L397；:§3-3:L69（Dirk Bax 1949） |
| LB-WORK-DISPUTED-2 | #7《七宗罪》/ #9 根特《负十字架》为归属争议件，引用须标注 | fact / supported | [bosch.md](../../dossiers/bosch.md):§10-6:L311、§12-7:L419、§12-9:L429–L431；`AUDIT-bosch/rights_review.md`:§1 第 7/9 行 |
| LB-WORK-RIGHTS | 作品/权利信息沿用现有记录，不新增编造、不升级为联网复核 | fact / supported | `AUDIT-bosch/rights_review.md`:§0（10 行 / 声明级 / image_seen=0）；内部证据 658354c7d03f3bb7（未公开；来源记录由维护者保留）:§8.1:L273（沿用现有记录） |

<a id="db-source-line-53"></a>
## §C 主机制 + 关联机制（learning_path §3 / mechanism_notes §A–§B）

| claim_id | 主张 | kind / status | locator |
|---|---|---|---|
| LB-MECH-TRIPTYCH-MORAL | M1 多联画/道德三幕：三幕可读 + 帧内成对 ≥2 组 | observation / supported | [bosch.md](../../dossiers/bosch.md):§1-10:L42、§3-1:L67、§4-P4:L102、§8.2-8:L240；[bosch.md](../../modules/bosch.md):L13/L64 |
| LB-MECH-HYBRID | M2 想象生物群：混合体 ≥3/帧、每个 ≥2 类部件来源，非单物种畸变 | observation / supported | [bosch.md](../../dossiers/bosch.md):§1-3:L35、§2-7:L56、§4-P2:L100、§8.2-3:L235；[bosch.md](../../modules/bosch.md):L10/L48/L62；`AUDIT-bosch/claim_evidence_map.md`:§2 BO-S2-07（`[归纳]` supported） |
| LB-MECH-PANORAMA | M3 全景多事件编目：单元 ≥5、焦点 ≤20%、地平线 ≥上 1/3、景深 ≥2 | observation / partial | [bosch.md](../../dossiers/bosch.md):§1-1:L33 / §1-2:L34、§4-P1:L99、§8.2-1/-2:L233–L234；阈值为 `[归纳]` 未实测（L242、§10-9:L314）→ AUDIT BO-S1-01/02 标 partial，本 LEARN 不升级 |
| LB-MECH-MORAL-CODE | M4 怪诞=说教手段（西古恩萨 1605「大智之书」）；谚语/隐喻图像化 | observation / supported | [bosch.md](../../dossiers/bosch.md):§3-1:L67、§3-3:L69；[bosch.md](../../dossiers/_corpus/bosch.md):#19:L149–L155；`AUDIT-bosch/claim_evidence_map.md`:§3 BO-S3-01（supported）/ §5 Q18 Q19 |
| LB-MECH-MATTE-AMBIENT | M5 薄涂哑光 + 平光环境光（单点主光=0、夜景火光 ≥2） | observation / supported | [bosch.md](../../dossiers/bosch.md):§1-6:L38 / §1-8:L40、§2-2/-3:L51–L52（范·曼德 `[史料-转记]`）、§8.2-6:L238；[bosch.md](../../modules/bosch.md):L11/L51；`AUDIT-bosch/claim_evidence_map.md`:§2 BO-S2-02/03（DBNL 逐字 corroborated） |
| LB-MECH-OWL-SCALE | M6 直视目光/猫头鹰 + M7 尺度错乱 + 宝石谱 | observation / supported | [bosch.md](../../dossiers/bosch.md):§1-4:L36 / §1-5:L37 / §1-7:L39、§4-P3:L101/P5:L103/P6:L104、§8.2-4/-5/-7:L236/L237/L239 |
| LB-MECH-DIVISION | M8 分工边界：5 判据 + 四轴同名 + 分区/分帧禁折中 | observation / supported | [bosch.md](../../dossiers/bosch.md):§3.1:L76–L91（判据 L81、四轴 L88、70/30 L90）、§4 分工注:L107；[bosch.md](../../modules/bosch.md):L68–L69/L75–L78；`AUDIT-bosch/claim_evidence_map.md`:§3 BO-S3.1-01/04（supported） |
| LB-THRESHOLDS-UNVERIFIED | §4 六参数 / §8.2 八规则全部 `[归纳]` 未像素实测（分母=假想参考帧） | fact / supported | [bosch.md](../../dossiers/bosch.md):§8.2 注:L242、§10-9:L314；[bosch.md](../../modules/bosch.md):L55；`AUDIT-bosch/RESULT.md`:§7 限制 5 |
| LB-82-8RULES | §8.2 八条可判定规则逐帧可查，3/5 条与 §3.1 分工判据同轴 | fact / supported | [bosch.md](../../dossiers/bosch.md):§8.2:L231–L242；[bosch.md](../../modules/bosch.md):§8.2:L44–L55；`AUDIT-bosch/claim_evidence_map.md`:§4（8 行 BO-S4-01..08 全 supported） |

<a id="db-source-line-67"></a>
## §D 冲突行 / 反例 / 身份门（learning_path §4 rung3、§6；mechanism_notes §D）

| claim_id | 主张 | kind / status | locator |
|---|---|---|---|
| LB-CE-A-CONJUNCTION | 反例 A：P1/P2/P4 三条联立（L106）vs §8.2-3+§8.2-8 各自可数 → 判据粒度不一致 `[inference]` | hypothesis / partial | `AUDIT-bosch/RESULT.md`:§4（反例 A 全文）；[bosch.md](../../dossiers/bosch.md):§4 用法行:L106、分工注:L107、§8.2:L233–L240、注:L242、§3.1 判据①:L81；`coverage-manifest.json`:`counterexample.performed=true / marked=[inference]` |
| LB-CE-A-NOT-REBUTTAL | 反例 A 不是推翻档案、不是史实证伪、不是像素实测 | hypothesis / supported | `AUDIT-bosch/RESULT.md`:§4「判定」段 + §7 限制 5；[bosch.md](../../dossiers/bosch.md):§8.2:L242（分母=假想参考帧） |
| LB-ID-GATE-PROPOSAL | 身份门 proposal：P1≥中 ∧ P2≥中 ∧ P4≥中 三条同时成立才允许打 bosch 标签；否则即使生物计数达标也判 not_bosch | design_candidate / partial | `AUDIT-bosch/RESULT.md`:§4「可操作修正建议」段；[bosch.md](../../dossiers/bosch.md):§4:L106、§10-9:L314（组合实验可按 §8.2 自查表回改） |
| LB-ID-GATE-NOT-FALSIFIED | 身份门提案 **作为 not-falsified 的设计候选保留**：反例未证伪、未验证；不升级 validated、不实测、不改仓库、交 RULE/CONFLICT lane | design_candidate / partial | `AUDIT-bosch/RESULT.md`:§4 建议标 `[inference]` + §9 移交（CONFLICT/RULE lane）；本 lane [learning_path.md](learning_path.md):§6 / [mechanism_notes.md](mechanism_notes.md):§D / [how-to-think.md](how-to-think.md):D8 三处同口径；[bosch.md](../../dossiers/bosch.md):§10-9:L314 |
| LB-CROWS-NO-BOSCH-OWN | `conflicts.md` 全文 0 命中 bosch；18 C 行 + 16 near-miss 行均无此画家；card L78 的 C-01/C-06/C-12/C-15 是通用冲突轴引用 | fact / supported | `AUDIT-bosch/RESULT.md`:§6；`AUDIT-bosch/claim_evidence_map.md`:§6 BO-CF-01/02；`coverage-manifest.json`:`conflicts_rows_checked.{fulltext_scan, artist_specific_C_rows=0, artist_specific_near_miss_rows=0, card_referenced_C_rows}`；[bosch.md](../../modules/bosch.md):L78 |
| LB-DRIFT-7-REPORT-ONLY | 7 处跨档案行号漂移 + near-miss 8-vs-16 计数口径漂移，只报告不修复 | fact / supported | `AUDIT-bosch/RESULT.md`:§6（7 处表 + 1 处口径）；`AUDIT-bosch/claim_evidence_map.md`:§8 漂移表；`coverage-manifest.json`:`conflicts_rows_checked.locator_drift_recorded`（7 项 + count_drift_note）；[bosch.md](../../modules/bosch.md):L83 |
| LB-NEAR-MISS-NO-BOSCH | §4 near-miss 表无 bosch 行；身份门属「应补第 9 条自查项」而非 near-miss 行 | observation / supported | [bosch.md](../../dossiers/bosch.md):§8.2 注:L242（无第 9 条）；`AUDIT-bosch/RESULT.md`:§4 判定段 / §6；`conflicts.md`:§4（16 编号行） |

<a id="db-source-line-79"></a>
## §E How-to-Think 决策步（how-to-think.md §1 的 D1–D9，每步带 grade + 定位）

| claim_id | D 步 | kind / status | locator |
|---|---|---|---|
| LB-D1 | 先判多联画/三幕装置 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§0:L18、§12-1:L389–L392、§3-1:L67、§4-P4:L102 |
| LB-D2 | 生物=多来源拼装而非单物种畸变 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§1-3:L35、§2-7:L56、§8.2-3:L235、§3.1:L81 |
| LB-D3 | 形象可逐件道德解码（vs 林飞龙仪式档）`[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§3-1:L67、§3-3:L69、§3.1:L86–L89 |
| LB-D4 | 全景编目密度并显式写 P1 档 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§1-1/-2:L33–L34、§3-4:L70、§4-P1:L99、§8.2-1/-2:L233–L234 |
| LB-D5 | 画内单点主光=0 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§1-6:L38、§8.2-6:L238、§3.1 判据④:L81 |
| LB-D6 | 色域=宝石谱亮色铺开并写 P6 档 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§1-7:L39、§4-P6:L104、§8.2-7:L239、§4 分工注:L107 |
| LB-D7 | 直视目光/猫头鹰 + 尺度错乱 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§1-4:L36/§1-5:L37、§4-P3:L101/P5:L103、§8.2-4/-5:L236–L237 |
| LB-D8 | 身份门联立自查（守门步）`[归纳]` / 设计候选 | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§4:L106、注:L242；`AUDIT-bosch/RESULT.md`:§4 反例 A |
| LB-D9 | 组合预检 + 边界声明 `[归纳]` | design_candidate / not_applicable | [bosch.md](../../dossiers/bosch.md):§3.1:L82/L90/L91；[bosch.md](../../modules/bosch.md):L78（C-01/C-06/C-12/C-15） |
| LB-SELF-VS-INFERENCE | §2 七行对照 + 四行硬对照：早期文献/研究/账簿均非自述，D 序为归纳，禁用「博斯说/他认为」 | fact / supported | [how-to-think.md](how-to-think.md):§2 表；[bosch.md](../../dossiers/bosch.md):L7、§10-1:L306；[bosch.md](../../dossiers/_corpus/bosch.md):L4/L211、#15/#18/#19/#21/#22/#25；内部证据 49ff27e7b1c8e2c3（未公开；来源记录由维护者保留）:L9 |

<a id="db-source-line-94"></a>
## §F 练习 / 权利 / 边界 claims（learning_path §4–§8、mechanism_notes §F–§G）

| claim_id | 主张 | kind / status | locator |
|---|---|---|---|
| LB-PRACTICE-3RUNG | 三段阶梯 rung1/2/3 全部为**建议练习**，标题带 `建议练习` | design_candidate / not_applicable | [learning_path.md](learning_path.md):§4（三个 `### 阶梯 … 建议练习` 标题）、§8 边界 1；内部证据 658354c7d03f3bb7（未公开；来源记录由维护者保留）:§8.1:L273 |
| LB-PRACTICE-NO-HUMAN | 练习效果未由人评价；`human_review=not_applicable` / `review:null`，不写「已证实学习收益」 | model_judgment / unverified | 内部证据 658354c7d03f3bb7（未公开；来源记录由维护者保留）:§8.4:L308–L310；[learning_path.md](learning_path.md):§5/§8；本包 `receipt.json`:`human_review.status=not_applicable` |
| LB-RIGHTS-10-ROWS | 10 张公开图 = 1 PDM / 8 PD / 1 CC0；2 张归属争议保留标注；PDM-owner 不猜测 PD | fact / supported | `AUDIT-bosch/rights_review.md`:§0/§1（10 行）/ 注 A；`rights_review.json`:`images[]`；`coverage-manifest.json`:`images_audit.license_distribution={PDM:1,PD:8,CC0:1}`、`images_public=10`；[bosch.md](../../dossiers/bosch.md):§10-6:L311、§10-10:L315 |
| LB-RIGHTS-DECLARED | 许可为 `declared_*` 非 `verified_*`；`image_seen=0`；逐张 imageinfo/馆方许可页未联网复核 | fact / supported | `AUDIT-bosch/rights_review.md`:§0/§3（unknown 项）、`coverage-manifest.json`:`images_audit.{image_seen=0, license_pages_reverified_externally=0}`；`AUDIT-bosch/RESULT.md`:§7 限制 2 |
| LB-NO-NEW-FETCH | 本 LEARN 未做新外部抓取；4 次 HTTP 200（RF-01..04）沿用 AUDIT；原始档案/意大利语原文/1788 首版/普拉多 Wayback 未回查 | fact / supported | `AUDIT-bosch/RESULT.md`:§5（4 次表）/ §7 限制 3；`coverage-manifest.json`:`external_fetches[]` / `unverified_sources_recorded[]`；`raw/*.html` 4 份字节 sha256（见 AUDIT receipt claims） |
| LB-AUDIT-ACCEPTED | 依赖 `AUDIT-bosch` 的 `receipt.json status=accepted`（author=AuditBosch，reviewer=ReviewGateAUDIT-bosch，independent_from_author=true） | fact / supported | 内部证据 b570c3f261f0270c（未公开；来源记录由维护者保留）:`status` / `author_actor_id` / `review.reviewer_actor_id`；`review-evidence.md`（独立 gate 复核） |
| LB-NO-REPO-WRITE | 本 lane 仅写 内部证据 e5069c7b42e76424（未公开；来源记录由维护者保留），0 仓库写入 / 0 spawns / 0 凭据；漂移只报告不修复 | observation / supported | 内部证据 bf734f37faff581f（未公开；来源记录由维护者保留）:内部证据 133d89d2c23bec0e（未公开；来源记录由维护者保留）、`spawns_allowed=false`；`AUDIT-bosch/RESULT.md`:§6 `action=report_only_no_repo_fix`、§7 限制 1 |
| LB-SUBMITTED-GATE | 本产物 `status=submitted` / `review:null`，作者不自接受，待独立审者；`execution_dedup_key=null`（dispatch_contract_state=unbound） | fact / supported | 本包 `receipt.json`:`status` / `review`；内部证据 bf734f37faff581f（未公开；来源记录由维护者保留）:LEARN-bosch `dispatch_contract_state=unbound`；`AUDIT-bosch/RESULT.md`:§7 限制 6（同口径） |

<a id="db-source-line-107"></a>
## §G 定位方法（照 AUDIT locator 纪律）

- 所有 `文件:节:行号` 取自本会话对只读工作树的 `nl -ba` 实测（[bosch.md](../../dossiers/bosch.md) 511 行 / [bosch.md](../../modules/bosch.md) 84 行），与 `AUDIT-bosch/claim_evidence_map.md` 的程序化节行号（`audit_scripts.out → dossier_section_lines`）一致。
- AUDIT 的 78 行 claim 由 `audit_scripts.py` 程序化计数（50/22/6/0 = 78，同源同次统计）；本文件引用其 claim_id（BO-S1-xx / BO-S2-xx / BO-S3-xx / BO-S4-xx / BO-CF-xx / §5 Q01–Q26）与行号，不另造分母、不重审。
- 行号漂移（7 处）按 `conflicts.md` §5.C「先怀疑行号、再怀疑内容」标为定位偏移，不判内容冲突、不改文件；AUDIT 已登记，本 lane 照录。
- 外部取证 locator = `raw/<file>.html` 的字节 sha256 + `coverage-manifest.json → external_fetches[].{access_status,read_scope,retrieved_bytes_sha256}`；本 LEARN 不新增 access_status=available 的抓取。
- 图像 locator = `rights_review.json → images[].file_sha256` + 本机 manifest 行号；`read_scope=metadata`（无 `image_seen`），模型未见原图像素，不填 `image_seen`。
- 「未证伪 / not-falsified」为**状态标签**，不是 supported/validated；写在 `LB-ID-GATE-NOT-FALSIFIED` 的 status=`partial` + kind=`design_candidate`，与 `01-AUDIT.md` §8.4 / `05-RELEASE-ACCEPTANCE.md` 的「草案完成 ≠ E4 实测通过」口径一致。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
