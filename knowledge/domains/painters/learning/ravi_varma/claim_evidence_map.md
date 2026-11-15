<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-ravi_varma；原正文 SHA-256 `44bc16bc29215ead2829972077cbfa5157bd9f18089f59883fdc102bdb750732`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-ravi_varma — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-ravi_varma` · 依赖 `AUDIT-ravi_varma`（**ACCEPTED**：`review-gate-receipt.json` `review.verdict=accepted`、reviewer `ReviewGateAuditCRQ`；`receipt.json:6` status=accepted；`review-evidence.md §8` 无 blocking defect）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 3d072716879b8d6a（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 f4610084e29b8a61（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]`/`[self-written]`/`[reported speech]`/`[contemporary record]` = 作者/同时代人言语记录；`[归纳]` = 项目操作规则/研究者归纳；`[研究]` = 二手研究/文本比对；`[史料]` = 史实/权利记录；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`）。
> **行号纪律**：本表一律用**实测行号 + 子串**；AUDIT 已登记的漂移（C-07 语义、near-miss 8/11、Girgaum/Ghatkopar、`_extract.py` 指纹、Kilimanoor/Attingal 异说）**登记不修、不裁定**，见 §F。
> **本轮强调覆盖**：① 印度油画西法+神话题材机制（§C）；② oleograph 印刷传播 axis（§D）；③ 5 PD-Art + 12 PD rights（§E）；④ Kilimanoor WEAKENED 处理（§F）。

---

<a id="db-source-line-12"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LRV-INPUT-CARD | card sha = ledger `53a7835e…f2c4` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（ravi_varma `card_sha256`）× [ravi_varma.md](../../modules/ravi_varma.md) 全文件 sha × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LRV-INPUT-DOSSIER | dossier sha = ledger `a531171d…2992` | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（`dossier_sha256`）× [ravi_varma.md](../../dossiers/ravi_varma.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等 |
| 3 | LRV-INPUT-CORPUS | corpus sha = ledger `c0c8825f…f983`（30 quotes） | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（`corpus_sha256`/`corpus_quotes=30`）× [ravi_varma.md](../../dossiers/_corpus/ravi_varma.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等；30 条沿用 AUDIT 计数（5/9/16 三分区） |
| 4 | LRV-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-ravi_varma/coverage-manifest.json` sha = `54dad847…ac2df` | fact/supported | 内部证据 26e7eafbf3a1088b（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `review-evidence.md §7`（15/15 产物复核） | `[史料]`（字节实测） | RECEIPT input_hashes 第 4 项 |
| 5 | LRV-AUDIT-ACCEPTED | 上游 AUDIT-ravi_varma 已 ACCEPTED | fact/supported | 内部证据 46f08f54c4b9c1e1（未公开；来源记录由维护者保留） `review.verdict=accepted`；`receipt.json:6` status=accepted；`review-evidence.md §8` verdict accepted | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 6 | LRV-SECONDARY-HASHES | conflicts/GOALS/INDEX/_images manifest 与 AUDIT 登记一致 | fact/supported | [conflicts.md](../../../../cross/conflicts.md)=`314a24da…bbef`、`ops/GOALS.md`=`2727d1f0…1144`、[INDEX.md](../../dossiers/_corpus/INDEX.md)=`b74bf44f…65b4`、`_images/manifest.md`=`5698124d…b470` × AUDIT `RESULT.md §1` / `coverage-manifest.json hashes` | `[史料]` | 全等；conflicts.md 无 ravi_varma 专属 C-row |

<a id="db-source-line-23"></a>
## B. 前置知识 / 自述层（learning_path.md §1 / how-to-think.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 7 | LRV-K1-NO-TREATISE | 拉维·瓦尔马传世文字极少、书信原件均未直读、**无画论传世** | fact/supported | `dossiers/ravi_varma.md:7`（特殊性口径）、`:131`（§5「任何一条都不得当作画论体系引用」）；`_corpus/ravi_varma.md:226`（缺口） | `[研究]`（档案口径） | 决策序整体标 `[归纳]` 的依据 |
| 8 | LRV-K2-SELF-6 | §5 六条 = 2 自述（含转引）+ 4 转述/自署；唯一实物级自署「Ravi Varma」 | fact/supported | `dossiers/ravi_varma.md:129-156`；`_corpus/ravi_varma.md:10-43`（Q1–Q5）、`:31-36`（Q4 自署铭文） | `[self-written]`/`[reported speech]`（**转引级**） | 不规定任何阈值/决策顺序 |
| 9 | LRV-K3-ART-FOR-ALL | 「为所有人而艺术 / Art for all」被讥「Bazar art」= `[reported speech]` 转述，非逐字原话 | observation/supported | `_corpus/ravi_varma.md:24-29`（Q3）；`dossiers/ravi_varma.md:76`（§3-1 `[自述/转述]`） | `[reported speech]` | 只支持「为大众」这一侧，不证 P5/P6 工作流 |
| 10 | LRV-K4-GRADES | 证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]` 照录 | fact/supported | `dossiers/ravi_varma.md:5`（卷首分级）；`00-GOAL.md:9`（How to Think 须区分自述与推断、不编造作者心理） | `[史料]`（规格） | `[推测]`=0 |
| 11 | LRV-K5-PRACTICE | 练习 = 建议练习，不写「已证实学习收益」 | fact/supported | `01-AUDIT.md:273`（§8.1）；`02-EXECUTION-PLAN.md:64,66`（Lane B 学习顺序/四问） | `[史料]`（spec） | `human_review=not_applicable` |

<a id="db-source-line-33"></a>
## C. 主轴 A：印度油画「西法 + 神话题材」机制（learning_path §3 / mechanism_notes §2 / how-to-think §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 12 | LRV-M-DIV37 | §3.7 分工（vs 欧洲学院派）=「技术输入 → 本土化转译」，四判据 光/面孔/空间/题材功能 | observation/supported | `dossiers/ravi_varma.md:85-93`（§3.7 a–d + 组合注记）；`modules/ravi_varma.md:73`（卡「冲突注记」） | `[归纳]`（写死分工，可被组合实验推翻） | AUDIT [claim_evidence_map.md](claim_evidence_map.md) D-37 partial |
| 13 | LRV-M-SOFT-LIGHT | 拉维=柔光均匀化（识读/礼拜）vs 卡拉瓦乔硬光开关 / 伦勃朗连续衰减心理光斑 / 维米尔光学室内 | observation/supported | `dossiers/ravi_varma.md:88`（§3.7a）、`:93`（「技术同源，功能相反」）、`:127`（§4 分工注）、`:226`（§8.1 边界提醒） | `[归纳]`（分工）+ `[研究]`（Sheikh Q16/Q18） | 越界判据见 #20 |
| 14 | LRV-M-SHALLOW-STAGE | 舞台式场面（proscenium tableau）：框景 ≥1、纵深 ≤2、人物如走位 | observation/supported | `dossiers/ravi_varma.md:38`（§1-1）；`:59`（§2-3）；`:90`（§3.7c）；`_corpus/ravi_varma.md:120`（Q16 Sheikh "theatric tableaux on a proscenium stage"） | `[研究]`（形态）/ `[归纳]`（阈值） | §8.2-3 量化 |
| 15 | LRV-M-TYPE-FACE | 理想类型脸（跨画同款）vs 心理个案；§4 P2 弱档已容纳个体肖像 | observation/supported | `dossiers/ravi_varma.md:40`（§1-3）、`:89`（§3.7b）、`:100`（§3.8b）、`:120`（P2 弱档） | `[归纳]` + `[研究]` | AUDIT `counterexample.md 尝试2` 规则自洽 |
| 16 | LRV-M-DARSHAN | 达显正面性 + 图像志清晰化：「看过即识、识过即拜」；「人照自己的形象造了神」 | observation/supported | `dossiers/ravi_varma.md:43`（§1-6）、`:63`（§2-7）、`:80`（§3-5）、`:224`（达显模式追加句）；`_corpus/ravi_varma.md:204`（Q28） | `[研究]`（Q28）/ `[归纳]`（达显句） | 法器清单/正面 ≥80% |
| 17 | LRV-M-DIV38 | §3.8 分工（vs 谢尔吉尔）= 大众复制/标准化神祇/礼拜凝视 vs 独幅/个体观察/现代主义凝视 | observation/supported | `dossiers/ravi_varma.md:95-104`（§3.8 a–d + 三判据）；`modules/ravi_varma.md:74` | `[归纳]`（写死分工） | 未来卡，判据为规则层 |
| 18 | LRV-M-NORTH | §3.9 vs 北斋：石版彩印（明暗渐层+套色）vs 木版（等宽线+平涂+留白） | observation/supported | `dossiers/ravi_varma.md:108`（§3.9）；`modules/ravi_varma.md:75` | `[归纳]` | 同属「大众印刷」两路 |
| 19 | LRV-M-FIRST-INDIAN | 「first Indian to use Western techniques」只归 Britannica 单一主源，不夸大为普遍共识 | observation/supported | `_corpus/ravi_varma.md:162`（Q22 Britannica）；AUDIT `risk_fetch.md:29-35`（R2：Wikipedia 正文未命中、Britannica 命中） | `[研究]`（单源）+ `[史料]`（AUDIT 取证） | 单源口径 |
| 20 | LRV-M-BOUNDARY | 硬光开关→卡拉瓦乔域 / 单张脸连续衰减→伦勃朗域 / 个体凝视+后印象派色→谢尔吉尔域 / 单线平涂→北斋域 | observation/supported | `dossiers/ravi_varma.md:127`（§4 分工注）、`:226`（§8.1 边界提醒）、`:110`（§3.9 不得复制邻近机制） | `[归纳]`（分工口径） | N1 重算：不得同时上硬光开关与达显正面性（`:92`） |

<a id="db-source-line-47"></a>
## D. 主轴 B：oleograph 印刷传播 axis（learning_path §1.3/§4 阶梯3 / mechanism_notes §3）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 21 | LRV-O-CATALYST | T. Madhava Rao 信「送画去欧洲石印」= oleograph axis 催化文书（**他人来信、转引级**） | fact/supported | `_corpus/ravi_varma.md:82-87`（Q11）；AUDIT [claim_evidence_map.md](claim_evidence_map.md) Q11 unverified（转引） | `[contemporary record]`（转引级） | **不是拉维自述**；不证他设计了 P5/P6 |
| 22 | LRV-O-TRANSFORM | 「复制不只是复制，而是转换」：油画→工坊复刻→石版分色套印（德国机材 + Fritz Schleicher） | fact/supported | `dossiers/ravi_varma.md:66`（§2-10）、`:17`（§0 主要媒介） | `[史料]` | 平版色层 + 强化饱和 |
| 23 | LRV-O-PRESS-1894 | 1894-07 Ravi Varma Press 开工（首张《Birth of Shakuntala》，9 月 Lakshmi/Saraswati）；1901 转让 Schleicher；1972 大火 | fact/supported | `dossiers/ravi_varma.md:322`（§11.1）、`:347`（§11.2 年份表）、`:281`（§9 交叉核 #2 CONFIRMED）；AUDIT `risk_fetch.md:38-43`（R3 外部 1894 笼统确认） | `[史料]` + `[研究]`（多源） | **建厂地 Girgaum vs Ghatkopar 漂移见 #33，登记不修** |
| 24 | LRV-O-DEMOCRACY | 石版画让「统一宗教图像」进入每一个印度教家庭 = 图像的民主 | observation/supported | `_corpus/ravi_varma.md:196-201`（Q27 基金会）；`dossiers/ravi_varma.md:322`（§11.1「图像的民主」）、`:183`（§7-4）、`:104`（§3.8 一句话） | `[研究]`（基金会）+ `[归纳]`（本项目归并） | 跨阶层/种姓分发 |
| 25 | LRV-O-SPEC | 印刷品进入日历/广告（Vinolia 香皂 1927 年历、Sivakasi 仿作）→ 人名变成图像通用规格 | fact/supported | `dossiers/ravi_varma.md:324`（§11.1） | `[史料]` | 传播终点 |
| 26 | LRV-O-READY | oleograph-ready：正面、轮廓清晰、缩印仍可读（§1-10 / §8.2-8 / P6） | observation/supported | `dossiers/ravi_varma.md:47`（§1-10）、`:238`（§8.2-8）、`:124`（§4 P6）、`:224`（达显追加句 `readable when reduced to postcard size`）；`modules/ravi_varma.md:13,51` | `[归纳]`（未实测参数） | 全部阈值只作自查口径 |
| 27 | LRV-O-P5P6 | 「印刷档（P5 强 + P6 强）即 Press 图像志」——传播载体反向约束画面参数 | observation/supported | `dossiers/ravi_varma.md:126`（§4 用法）；`modules/ravi_varma.md:66` | `[归纳]` | 两轴咬合点（本轮核心） |
| 28 | LRV-O-OLEOGRAPH-IMG | #16《Saraswati》油画版 × #17 石版彩印版 oleograph 双图在库，作练习对照端点 | fact/supported | AUDIT `rights_review.md:29-30`（#16/#17）；`dossiers/ravi_varma.md:29`（§0）、`:412`（§12-10） | `[史料]`（权利账）/ `[归纳]`（练习映射） | #17 为 500px 缩略图补取（Commons 429），未 image_seen |

<a id="db-source-line-60"></a>
## E. 权利：5 PD-Art + 12 PD（learning_path §1.5/§2 / mechanism_notes §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 29 | LRV-R-17 | images_public=17：17 行 manifest = 17 个 .jpg 一一对应 | fact/supported | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留）（images_public=17, images_manifest=true） × AUDIT `coverage-manifest.json:29,61,66-67` × `rights_review.md:1-10` | `[史料]`（字节/账目实测） | review-evidence.md §1 复算 17 行 |
| 30 | LRV-R-SPLIT | license = `Public domain（PD-Art）` **5**（#1/#4/#7/#12/#14）+ `Public domain` **12** = 17，全 PD 族 | fact/supported | AUDIT `rights_review.md:37`（机器计分布）；`review-evidence.md:12`（独立复算 PD-Art 5 / PD 12 一致）；`coverage-manifest.json license_distribution` | `[史料]`（声明级账目） | GOALS A-54「全 PD」是标签粒度差（review-evidence.md §8） |
| 31 | LRV-R-DECLARATION | 权利判定只到本机 manifest 声明级；未逐张回源、未 image_seen、外部许可真实性 `unverified` | fact/supported | AUDIT `rights_review.md:3,35-36`；`RESULT.md §7`（image_seen=false）；`review-evidence.md:54`（§8 正确未升级） | `[史料]`（诚实边界） | 不重授权、不复制像素 |
| 32 | LRV-R-UNKNOWN | `#2/#3/#8/#10/#13/#15/#17` 等「馆藏」记「未注/藏处未注」——unknown 保持 unknown | fact/supported | AUDIT `rights_review.md:34` | `[史料]` | 不猜测、不填实 |

<a id="db-source-line-69"></a>
## F. Kilimanoor WEAKENED 与已登记漂移（learning_path §6/§8 / how-to-think §4 / mechanism_notes §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 33 | LRV-W-KILIMANOOR | 卒日 1906-10-02 **CONFIRMED**（三源）；卒地 **Kilimanoor vs Attingal → WEAKENED**（异说并存） | fact/supported | `dossiers/ravi_varma.md:280`（§9 交叉核 #1）、`:290`（§10 异说）、`:14`（§0） | `[史料]` + `[归纳]`（WEAKENED 判定） | **本轮强调：不写成单一确定值、不升级为定论** |
| 34 | LRV-W-EXTERNAL | AUDIT 外部取证复现两说：`Kilimanoor Palace`（Britannica-Wayback）/ `Attingal`（Wikipedia 信息框） | fact/supported | AUDIT `risk_fetch.md:23-36`（R2）；`raw/risk_britannica_wayback.html` sha `071c9a71…` / `raw/risk_wikipedia.html` sha `ed816ece…`；`review-evidence.md:24-32`（§4 判定「WEAKENED 处置正确」） | `[史料]`（AUDIT 缓存字节） | 本 lane 未重访 URL、不重新抓取 |
| 35 | LRV-W-GIRGAUM | Press 建厂地 Girgaum（档案）vs Ghatkopar（Wikipedia）= 地点漂移，登记不修 | fact/supported | `dossiers/ravi_varma.md:322,347`（Girgaum）；AUDIT `risk_fetch.md:38-43`（R3 Ghatkopar）、`RESULT.md §4 R3`/§6.3；`review-evidence.md:30-32` | `[史料]`（差异登记） | 交 CONFLICT/RULE lane |
| 36 | LRV-W-C07 | C-07 语义漂移：卡 L76/L111 + dossier L111 写「印刷 vs 油画表面两分」，conflicts.md 正本为「丢勒排线 vs 北斋平涂」 | fact/supported | `modules/ravi_varma.md:76`；`dossiers/ravi_varma.md:111`；`knowledge/cross/conflicts.md:136-147,417`；AUDIT `RESULT.md §6.1`、`review-evidence.md:18-22`（§3 独立确认） | `[史料]`（漂移登记） | ravi_varma **无专属 C-row**（review-evidence.md §3 `ravi_named_c_rows: []`） |
| 37 | LRV-W-NEARMISS | near-miss 自审「8 条」vs 现表「11 编号行」计数口径漂移 | fact/supported | `knowledge/cross/conflicts.md:365`（自审 A）、`:341-357`（§4 表 11 行）；`modules/ravi_varma.md:81`（卡记「near-miss 8 对」）；AUDIT `RESULT.md §6.2`、`review-evidence.md §5` | `[史料]`（漂移登记） | 登记不修 |
| 38 | LRV-W-EXTRACT | `_extract.py` 实跑指纹 `4afa31ec…` vs 基线文档 `e7e96645…`（跨 lane 改动）；AUDIT 已绑定 228/228 到实跑内容 | fact/supported | AUDIT `RESULT.md §1`（L25）、§6.5；`coverage-manifest.json:16-17`；`review-evidence.md §7` | `[史料]` | 本 lane 不重跑、不改口径 |
| 39 | LRV-W-COUNTER | AUDIT 两 `[inference]` 反例：① P3 夜色单光源 vs §3.7 柔光禁硬边 = 未达推翻门槛/缺显式取值；② 类型脸 vs 个体肖像 = 规则自洽 | observation/supported | AUDIT `counterexample.md:5-23`；`dossiers/ravi_varma.md:119-124,127,231-232,405-408,88,89,103,120`；`review-evidence.md §6`（逐行定位确认、无 overclaim） | `[inference]`（AUDIT） | 判别动作交实证 lane（像素实测），本 lane 不升级 |

<a id="db-source-line-81"></a>
## G. 交付物自证（learning_path / how-to-think / mechanism_notes / RESULT）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 40 | LRV-DELIVER-7 | 7 文件契约齐备（5 内容 artifact + RESULT 即第 5 内容、+ runner_receipt.json + receipt.json） | fact/supported | 内部证据 5a7638bc6980ba65（未公开；来源记录由维护者保留） 目录 × `RESULT.md §3` × `receipt.json artifacts` × `runner_receipt.json` | `[史料]`（本 lane 产物） | required_artifact_kinds 4 项全覆 + how_to_think 追加登记 |
| 41 | LRV-DELIVER-81 | learning_path.md 覆盖 A-30 §8.1 八节（前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界） | fact/supported | `01-AUDIT.md:271`（§8.1 八节清单）；内部证据 2771b88a486e52eb（未公开；来源记录由维护者保留） | `[史料]`（spec 对齐） | 练习全标建议练习 |
| 42 | LRV-DELIVER-GRADE | how-to-think.md 严格分栏 `[自述]` 与 `[归纳]/[研究]/[史料]`、`[推测]`=0、无从画面推心理 | fact/supported | `00-GOAL.md:9`；`02-EXECUTION-PLAN.md:66`；内部证据 2354cb6e85730d46（未公开；来源记录由维护者保留） | `[史料]`（spec 对齐） | D0 写死前提非决策 |
| 43 | LRV-DELIVER-VERIFY | verify-receipt.py 对本 receipt 的 schema + 本地字节校验结果 | fact/supported | `RESULT.md §6`（复跑命令）、`runner_receipt.json verify_command`；**exit code 与 JSON 输出在最终答复如实报告，不预写进 artifact（避免自哈希循环）** | `[史料]`（实跑） | status=submitted 仅做 schema 校验 |

---

<a id="db-source-line-92"></a>
## H. 计数与诚实边界

- **本表 43 条论断**，全部带 `source : locator`；等级分布：`[史料]` / `[研究]` / `[归纳]` / `[self-written]` / `[reported speech]` / `[contemporary record]` / `[inference]`；**`[推测]`=0**（本 lane 不使用）。
- **support_status**：全部 `supported` 指「仓内证据链/上游 ACCEPTED 产物支撑该条按现状记录在案」，**不是「该条外部为真」**（沿用 AUDIT `claim_evidence_map.md §判定口径`）。外部 URL 本轮未重访 = `access_status=unknown`；17 张原图未目检 = 无 `image_seen`；权利 = manifest 声明级。
- **未升级项**：§8.2 八阈值 / §4 六参数为 `[归纳]` 未实测；WEAKENED/漂移项登记不修；练习 = 建议练习、无 human review；`submitted` ≠ `accepted`，`review=null`（作者不自验收，独立 gate 另担）。
- **写入边界**：仅 内部证据 5a7638bc6980ba65（未公开；来源记录由维护者保留）；仓库 READ-ONLY、0 git 操作、0 子代理派发（`spawns_allowed=false`）、0 凭据。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
