<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-bruegel；原正文 SHA-256 `1bec7c345fd81b774bbb8b2b5bfb80080550890686b208d778a8a1838e2c431e`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-bruegel — Claim ↔ Evidence Map

> 任务 LEARN-bruegel ｜ A-30 Lane B ｜ 仓库只读 @ f008952365a77e140cbda3f3959d43ef000f9a22 ｜ 依据 **ACCEPTED** 内部证据 ccdba56153755810（未公开；来源记录由维护者保留） verdict=accepted），证据层不重审、不升级。
> 证据分级 [自述]/[史料]/[研究]/[归纳]/[推测]/[inference]；support_status: supported / partial / unverified / not_applicable。所有 locator 为冻结树实测行号或 AUDIT 已接受的 artifact 定位。
> 缩写：档案 = knowledge/domains/painters/dossiers/bruegel.md (sha 49ae3337…aa0) ｜ 卡 = knowledge/domains/painters/modules/bruegel.md (672040c3…562) ｜ corpus = .../_corpus/bruegel.md (e0bc5f61…79c) ｜ AUDIT-CM = 内部证据 caf5a0a5f865889c（未公开；来源记录由维护者保留） (3d5540c8…484) ｜ AUDIT-RG = 内部证据 9ede3248fa080957（未公开；来源记录由维护者保留） (b83b6d62…495) ｜ wiki = 内部证据 65bf051b120e7698（未公开；来源记录由维护者保留） (f0eef694…ea8)。

<a id="db-source-line-7"></a>
## 0. 输入哈希（本轮实跑 sha256sum，均与 内部证据 2ebae964cab4c8d5（未公开；来源记录由维护者保留） 一致）

| 输入 | sha256 |
|---|---|
| 档案 bruegel.md | 49ae33376fcb75357bcdef950cc766ce4acc495d3534dc008140d7b70c515aa0 |
| 卡 bruegel.md | 672040c3e51a54a6389f63972b87030f92f4a31415ecfb79595665af22b9b562 |
| corpus bruegel.md | e0bc5f612dfbb97510fd9d1bfe925072f9c15e6ccfeaa56069eb71848c29c79c |
| conflicts.md | 314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef |
| AUDIT coverage-manifest.json | 1599d3f701d57576de69623683008ee3289db581539944a9b443ffb0f1cfb457 |
| AUDIT claim_evidence_map.md | 3d5540c891c50f7422e7185ba4a60049c4df832418591d3b88a98c703510f484 |
| AUDIT RESULT.md | 0fc9fb658ac9d9f28a833b42cfaa9f60ed6f5385cde143a6a5407915a3551fcc |
| AUDIT review-gate-receipt.json | b83b6d626a23ff0f3d1ac16d0019ed00d193fc2c8c7f97046ea9383bc5c71495 |
| AUDIT receipt.json | f65176953c28bff4d03704e77c128757e4545d884178b93d0e7683f43d4228f8 |
| AUDIT runner_receipt.json | 2a379be673ee0a94d6e93186d210648e66a41978aa78ba65ca687e0f481e0efd |
| wiki raw cache | f0eef6940ee1a2c2513b03adf8ec2dcd5c483cfb52ca2b7a8a56546a7cc95ea8 |

<a id="db-source-line-23"></a>
## 1. 前置 / 身份（LP §1 / HT §0 / MN §1）

| id | claim | where | locator | grade | status | basis |
|---|---|---|---|---|---|---|
| LB-01 | 勃鲁盖尔无存世自述文字（self-written=0），转记按 [reported speech] 降级 | LP §1-3 / HT §0 / MN §4 | 档案 :9, :109, 自审 B6 :406；corpus L5；AUDIT X-4 | [史料] | supported | 档案已查 5 类源；AUDIT CM §F X-4 supported |
| LB-02 | 鸟瞰全景：地平线上 1/4–1/3、俯角 ≥15°、无单一消失点；KHM「唯一办法」 | LP §3.1 / HT 步1 / MN §1 P1 | 档案 §1-1 :34, §2-5 :53, §8.2-1 :191；corpus Q17 :128-133；AUDIT S1-1 | [研究]+[归纳] | partial | 视角事实 supported；量化阈值 [归纳] 未实测（AUDIT S1-1 标 partial） |
| LB-03 | P1 三档（平视/低俯/高俯）默认 70% | LP §3.1 / MN §1 | 档案 §4 P1 :96；卡 :61 | [归纳] | unverified | 阈值未对原作像素测量（档案 :200/:239；AUDIT S4-P1 unverified 量化） |
| LB-04 | 季节组画＝六件各领两月（存五件）、3/1 岁首；六 vs 十二争议并存 | LP §1-2/§3.3 / HT 步2 | 档案 §1-4 :37, §3-1 :66, §10-3 :238；corpus Q19 :142-147, Q26 :191-196；wiki「six or twelve」；AUDIT S1-4 | [研究] | supported | Q19/Q26 + wiki 双源；AUDIT S1-4 supported |
| LB-05 | 共时叙事：同地不同时并置一帧（KHM「勃鲁盖尔的发明」） | LP §3.2 / HT 步2 / MN §2 规则3 | 档案 §1-3 :36, §8.2-3 :193；corpus Q16 :121-126；AUDIT S1-3 | [研究] | supported | KHM x-320 原文 Q16 |
| LB-06 | 分布式人群：≥30/≥100、最大聚类 ≤15%、每人独立动作、无主角 | LP §3.2 / HT 步3 / MN §1 P2/§2 规则2 | 档案 §1-2 :35, §2-7 :55, §8.2-2 :192；corpus Q17, Q22；AUDIT S1-2/S2-7 | [研究]+[归纳] | supported (文)/partial (操作化) | Q17「painted encyclopaedia」；阈值 [归纳] |
| LB-07 | 细节微缩：逐人可读「slow and selective study」、中位 ≤画高 1/15 | LP §3.2 / MN §1 P4/§2 规则5 | 档案 §1-7 :40, §8.2-5 :195；corpus Q17；AUDIT S1-7/S4-P4 | [研究]+[归纳] | partial | Q17 注 supported；阈值 unverified |
| LB-08 | 谚语/民俗/农俗编码（83 游戏、约百谚语、农事/节庆）可解码、P6 密度可控 | LP §3.2 / HT 步3 / MN §1 P6 | 档案 §1-9 :42, §3-6 :71, §4 P6 :101；corpus Q17；AUDIT S1-9 | [研究]+[归纳] | supported | Q17 + wiki；「约百条」档内估计 |
| LB-09 | 单一基调「不是细节总和而是整体效果」；「永久寒冷」；P3 65% | LP §3.3 / HT 步2 / MN §1 P3/§2 规则4 | 档案 §1-5 :38, §2-8 :56, §8.2-4 :194；corpus Q20 :149-154, Q21 :156-161；AUDIT S1-5 | [研究]+[归纳] | supported (文)/unverified (阈值) | KHM x-327/x-326；web 复核命中 permanent cold/overall effect |
| LB-10 | 前景暗框 repoussoir + ≥1 导引线指向纵深 | LP §3.4 / MN §2 规则6 | 档案 §1-6 :39, §8.2-6 :196；corpus Q25 :184-189；AUDIT S1-6 | [研究]+[归纳] | partial | repoussoir 由馆方导览转引、私有文本未直读（AUDIT S1-6 partial） |

<a id="db-source-line-38"></a>
## 2. 边界 / 组合（LP §3.4/§6 / HT 步4 / MN §5）

| id | claim | where | locator | grade | status | basis |
|---|---|---|---|---|---|---|
| LB-11 | 漫射天光、无单点光源（软光）；C-01 软侧同侧声明 | LP §3.4/§6 / HT 步4 / MN §5 | 档案 §8.2-8 :198, §8.3-1 :206, §3.1 :90；卡 :77 | [归纳] | partial | conflicts.md 无 bruegel C-row（AUDIT §G drift）→ 立场属档案自述归纳 |
| LB-12 | 反理想人体：短壮弯曲、身高/肩宽 <4、对称站姿 ≤20% | LP §3.4 / HT 步4 / MN §2 规则7 | 档案 §1-8 :41, §8.2-7 :197；corpus Q24 :177-182, Q23；AUDIT S1-8 | [研究]+[归纳] | supported (文)/unverified (阈值) | KHM x-330/x-331 |
| LB-13 | 满构图 C-17 ≤15%、蓝仅远景大气 C-12（不主张 ≥40%） | LP §3.4/§6 / HT 步4 / MN §5 | 档案 §3.1 :82/:90；卡 :77；§8.2-4 :194；AUDIT S3.1-d/S3.1-b | [归纳] | partial | 无 bruegel C-row（AUDIT §7）；C-12 主张方为他卡、布未登记 |
| LB-14 | 土色低饱和＋红点锚；全帧中位饱和 ≤0.45 | LP §3.3/§3.4 / HT 步4 / MN §1 | 档案 §1-10 :43；AUDIT S1-10 | [归纳] | partial | 无单一外部原文逐字支持（AUDIT S1-10 partial） |
| LB-15 | §4 六越界警报（硬光→卡拉瓦乔 / 天气→透纳 / 英雄向心→米 / 平面装饰→北斋 / 新物种→博 / 夜街→霍珀） | LP §6 / HT 步1-4 / MN §5 | 档案 §4 用法 :103；卡 :68 | [归纳] | unverified | 全为项目操作规则、无外部实测（AUDIT S4-usage unverified） |
| LB-16 | vs 北斋＝油画全景/时间序列 vs 版画单景/母题连作；≥2 轴联合、限定绘画；70/30 | LP §1-4/§3.5/§6 / HT 步1/步5 / MN §3 | 档案 §3.1 :77-82；卡 :74；自审 B1 :401；AUDIT S3.1-a | [归纳] | partial | 项目写死分工、无外部独立判据；自审 B1 WEAKENED→边界注 |

<a id="db-source-line-49"></a>
## 3. 反例 / 史料锚（brief emphasis）★

| id | claim | where | locator | grade | status | basis |
|---|---|---|---|---|---|---|
| LB-17 ★ | Large Landscapes 版画设计（1555–56，Cock，40+ 件）同样鸟瞰 Weltlandschaft 全景＋可含分布式小人物＋系列化 | LP §3.5 / HT 步5 / MN §3 | 档案 :17, §3.1 :81, §2-6 :54, §6.1 :129, §11.1 :257, 自审 B1 :401；wiki「Large Landscapes…published by Hieronymus Cock」×2；AUDIT CM §H L140-146 | [史料]+[inference] | supported (存在) | AUDIT review-evidence §5 复核 wiki 锚点「Large Landscapes」×2 命中；档内多处 |
| LB-18 ★ | 纯视觉阈值（P1/P2/P4 ≥2 中档）会把作者自己的版画同判为「是勃鲁盖尔」→ 与 §3.1 媒介轴冲突；故阈值不是充分身份判据 | LP §3.5 / HT 步5 / MN §3 | 档案 §4 用法 :103, §8.2-1 :191, §3.1 :81；AUDIT CM §H L142-146；AUDIT RESULT §6；review-evidence.md §5 | [inference] | partial | 文本层反例；AUDIT verdict 逻辑成立；实验层 [UNVERIFIED]（未做像素级组合实验） |
| LB-19 ★ | 反例不推翻 §4 数值阈值，只削弱「充分判据」读法；须联合 §3.1 媒介/系列骨架轴 | LP §3.5/§4 L3 / HT 步5 / MN §3 | 档案 §3.1 :81, 自审 B1 :401；AUDIT CM §H L146；AUDIT RESULT §6 | [inference] | partial | AUDIT 判定「does not overturn [归纳] numeric thresholds」 |
| LB-20 ★ | 「吸入前」教学序：先讲原始强规则 → 用作者自己版画撞穿 → 再看档内 :81/:401 预吸收边界注 | LP §3.5 / HT 步5 / MN §3 | 档案 §3.1 :81, 自审 B1 :401；AUDIT CM §H | [归纳] | supported (设计) | 本 LEARN 分片的教学编排，标注为 [归纳] 非史实 |
| LB-21 ★ | 127 件摹本（《冬景与捕鸟器》，小彼得复制）＝可复制性史料锚；≠ P1/P2 参数、不反推「原作是版画」 | LP §3.6 / LP §2 / HT 步5 / MN §4 | 档案 :133, :232, :265；wiki「127 copies are recorded」；AUDIT X-1, review-evidence §2 | [史料] | supported | wiki 缓存命中；AUDIT high_risk_claims_verified_public=3 |
| LB-22 ★ | Kapellekerk：1569-09-09 卒葬卡佩勒教堂、1563 婚礼亦此；用于时间轴、抵挡「农民=出身」接受史外壳 | LP §3.6 / LP §1-5 / MN §4 | 档案 :15, :261, :265, :293, §11.1 :253；wiki「Kapellekerk」「9 September 1569」；AUDIT §5 | [史料] | supported | wiki 缓存命中；AUDIT high_risk 3 之一 |
| LB-23 | Q27 Gutenberg #75540 SSL 失败 → partial；无伪造字节 | LP §8 / RESULT §6 | AUDIT RESULT §5/§9, review-evidence §3, coverage-manifest external_fetches | [史料] | supported (诚实记录) | AUDIT 接受、本片不升级 |

<a id="db-source-line-61"></a>
## 4. 练习 / 来源 / 验证（LP §4/§5/§7/§8 / HT §4）

| id | claim | where | locator | grade | status | basis |
|---|---|---|---|---|---|---|
| LB-24 | §12 十件「看什么/学什么/怎么练」练习骨架 + 组合建议四步/三档/隐藏 | LP §4 / MN §1/§6 | 档案 §12 :330-384；AUDIT CM §A/§C | [归纳] | supported (存在) | 练习条目为项目设计（档案 :332 明标 [归纳]） |
| LB-25 | 三阶梯 L1 视角 / L2 农俗调度 / L3 反例自检，均为建议练习、效果未经人评 | LP §4 / RESULT §6 | 档案 §12；01-AUDIT.md :273；00-GOAL.md :9 | [归纳] | not_applicable | 无人类学习成效证据（按 01-AUDIT §8.1 不写「已证实学习收益」） |
| LB-26 | §4 六参数 / §8.2 八规则阈值 [归纳] 未实测、分母假想参考帧 | LP §5/§8 / HT §3 自查5 / MN §2 | 档案 :200, :239；AUDIT S4-* / S1-* | [归纳] | unverified | 本 LEARN 分片不补做像素实验 |
| LB-27 | _extract.py --check 228/228 本轮未复跑（pin 到 A-81 自审） | LP §7/§8 / RESULT §6 | 档案 自审 C :426；AUDIT RESULT §2/§9, coverage-manifest extract_contract | [史料] | unverified | AUDIT 诚实标注 not re-run；本片沿用 |
| LB-28 | conflicts.md 无 bruegel C-row、C-16 适用性偏宽 → 报告不修、repo 只读 | LP §6 末/§8 / HT §4 / MN §5 / RESULT §6 | 档案 卡 :77；conflicts.md :258-271/:341-357；AUDIT §G L127-136/RESULT §7 | [归纳] | partial | AUDIT 已记录漂移，CONFLICT lane 复核项 |
| LB-29 | 权利口径 20/20 Public domain、1 外部抽核、image_seen=no（本片未看图） | LP §2 尾 / RESULT §6 | AUDIT rights_review.md, RESULT §9, review-evidence §4 | [史料] | supported | AUDIT 接受、本片不做视觉断言 |
| LB-30 | 本片 status=submitted、review=null、作者不自接受；verify-receipt.py schema-only 分支 exit 0 | RESULT §7 | tools/verify-receipt.py :20-21；receipt.schema.json | — | supported | 本地实跑（见 runner_receipt.json / RESULT §7） |

<a id="db-source-line-73"></a>
## 5. 可复跑数字（同一统计口径）

- 本片 7 文件：RESULT.md / learning_path.md / how-to-think.md / mechanism_notes.md / claim_evidence_map.md / runner_receipt.json / receipt.json。
- 内容 claim 行：30（LB-01…LB-30）；其中 ★强调项 6（LB-02 全景俯视机制链 / LB-06 农俗机制 / LB-17/18/19/20 反例 / LB-21/22 史料锚）。
- AUDIT 输入计数（复用、不重算）：quote_count=28、claims_total=72（52/10/0/10/0）、images_public=20、high_risk_claims_verified_public=3、counterexample_attempt=1、locators 131/131（AUDIT coverage-manifest / RESULT §4 / review-evidence §1）。
- 输入哈希：11 条（本轮 sha256sum 实跑，见 §0）；冻结 repo head = f008952365a77e140cbda3f3959d43ef000f9a22。

<a id="db-source-line-80"></a>
## 6. LOCATOR-RESOLUTION

所有档案/corpus/card/§4/§8.2/§12 行号均来自冻结树 f0089523 实测（dossier 439 行、card 82 行、corpus 28 条 header）；AUDIT 已用 audit_checks.py 对同一冻结文件验证 131/131 locators resolved（AUDIT RESULT §8 / review-evidence §1 复核）。本 LEARN 分片沿用该定位，不新增行号断言、不修仓库。wiki 锚点（127 copies / Kapellekerk / 9 September 1569 / Large Landscapes / six or twelve / dropped the h）经 AUDIT §5 与 review-evidence §2 双次命中。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
