<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-blake；原正文 SHA-256 `45eda12f186712a495d77adec04b7b99c82a2e7c1a905f76eeda3ca8e919647b`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-blake — claim / evidence 图（逐 claim 带定位）

> TASK_ID `LEARN-blake`｜依赖：内部证据 2b847b400bdd4643（未公开；来源记录由维护者保留）（**ACCEPTED**）+ 本机只读档案 @ `f008952365a77e140cbda3f3959d43ef000f9a22`。
> 口径：每条 claim 带 `文件:节:行号` 定位；grade 沿用 `[自述]/[史料]/[研究]/[归纳]/[推测]`；`support_status` 用 schema 枚举 `supported / partial / conflict / unverified / not_applicable`。
> **等级纪律**：`[归纳]` 阈值一律 `unverified`（§8.2 注 L221 未像素实测）；建议练习为 `design_candidate / not_applicable`；不冒充作者内心、不冒充人评。

<a id="db-source-line-7"></a>
## 输入 SHA-256（开工现场复核，与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） 一致）

| key | file | sha256 |
|---|---|---|
| dossier | [blake.md](../../dossiers/blake.md) | `3a52c8e0083ee5cb32ef6ee6c7cdf30a953cbe6c66840005df527876aad671ba` |
| card | [blake.md](../../modules/blake.md) | `b34b0c4a6961bccf052582a885056114ea56159e6e1dcd270359daad903c63d5` |
| corpus | [blake.md](../../dossiers/_corpus/blake.md) | `e482a7786c8d5c6d27f41c6bb74295833131870aa63be2941ff24a2f5103a24e` |
| conflicts | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` |
| AUDIT RESULT | 内部证据 977d22372732ec8e（未公开；来源记录由维护者保留） | 见 receipt `input_hashes`（本 shard 实取） |
| AUDIT counterexample | 内部证据 a9a940914651cdd0（未公开；来源记录由维护者保留） | 见 receipt `input_hashes` |
| AUDIT review-evidence | 内部证据 0620833333259678（未公开；来源记录由维护者保留） | 见 receipt `input_hashes` |
| AUDIT claim map | 内部证据 a097890d7f3b6955（未公开；来源记录由维护者保留） | 见 receipt `input_hashes` |

---

<a id="db-source-line-22"></a>
## §A 结构 / 证据分级（learning_path §1、how-to-think §0/§2）

| claim_id | claim | grade | locator | support_status |
|---|---|---|---|---|
| LB-STRUCT-1 | 布莱克 = 诗人-版画家；「作品」= 自写自画自刻自印自色的图文一体书页，不是「为文本配图」 | `[研究]` | `dossiers/blake.md:L6`（卷首语）、`:L19-21`（§0 能力定位） | supported |
| LB-STRUCT-2 | 幻视按 `[自述]`/`[史料]` 存档、不做病理化判断；「他内心如何」一律降级为操作规则 | `[归纳]` | `dossiers/blake.md:L6`；`00-GOAL.md:L9` | supported |
| LB-SELF-0 | 28 条语料（25 `[self-written]` / 1 `[contemporary record]` / 2 `[reported speech]`）是本机 Erdman 1988 底本；未对 R12 在线底本二次逐字复核 | `[史料]` | `_corpus/blake.md:L1-232`；`AUDIT-blake/RESULT.md:§6 L70`；`AUDIT-blake/coverage-manifest.json` | partial（外部真伪 unverified） |
| LB-GRADE-1 | §4 六参数 / §8.2 八规则全部 `[归纳]`，未对原作像素测量（分母＝假想参考帧） | `[归纳]` | `dossiers/blake.md:L221`、`:L260`（§10-6）；`modules/blake.md:§8.2 注` | supported（作为「未验证」这一事实） |

---

<a id="db-source-line-33"></a>
## §B 重点作品及来源（learning_path §2，全部引用现有记录）

| claim_id | claim | grade | locator | support_status |
|---|---|---|---|---|
| LB-WORK-1 | §12 十件代表作各含「看什么/学什么/怎么练」，作为学习清单 | `[史料]`+`[归纳]` | `dossiers/blake.md:L343-L398`（§12，作品行 L347/352/357/362/367/372/377/382/387/392） | supported |
| LB-WORK-2 | 18 张公开图 = 17 PD + 1 CC0（Met 开放数据，《淫欲之环》）；`milton_preface_1804.jpg` 馆藏未著录保留未知 | `[史料]` | `AUDIT-blake/rights_review.md`；`AUDIT-blake/RESULT.md:§5 L65`；`dossiers/blake.md:L28` | supported（metadata only，image_seen=0） |
| LB-OVT-1 | **已解决事实 ①**：「天上使者」信日期 = **1802-01-10**（旧说 1803-07-06 已 OVERTURNED） | `[史料]` | `dossiers/blake.md:L115`（§5-4）、`:L312`（§11.2）、`:L413`（自审 B）、`_corpus/blake.md:L41`（Q5）；`AUDIT-blake/RESULT.md:§4 L55`；`AUDIT-blake/review-evidence.md:§2 L28`（`dateCreated=10 January 1802`） | supported |
| LB-OVT-2 | **已解决事实 ②**：MHH 图 = **Plate 5**（copy I, Fitzwilliam），非扉页 | `[史料]` | `dossiers/blake.md:L357`（§12-3）、`:L414`（自审 B）；`AUDIT-blake/RESULT.md:§4 L56`；`review-evidence.md:§2 L29`（`Marriage of Heaven and Hell - Plate 5`） | supported |
| LB-OVT-3 | **已解决事实 ③**：《欧洲》扉页馆藏 = **YCBA**（lido-TMS-3878）；BM 1936,1116.32 另引 §7-2，不矛盾 | `[史料]` | `dossiers/blake.md:L362`（§12-4）、`:L415`（自审 B）、`:L169`（§7-2）；`AUDIT-blake/RESULT.md:§4 L57`；`review-evidence.md:§2 L30`（`Yale Center for British Art`） | supported |

---

<a id="db-source-line-45"></a>
## §C 主机制 + 关联机制（learning_path §3 / mechanism_notes §A-§B）

| claim_id | claim | grade | locator | support_status |
|---|---|---|---|---|
| LB-M1-RELIEF | 浮雕蚀刻：防酸墨镜像书写/描画 → 酸蚀背景、线凸起 → 凸版印刷；图文同版一次印出 | `[史料]`+`[研究]` | `dossiers/blake.md:L48`（§2-1）、`:L49`（§2-2）、`:L55`（§2-8）、`:L167`（§7-1 BM）、`:L173`（§7-7 Met） | supported |
| LB-M1-TEXT | 图文同版可判定规则：手写体文字区 5–35% 页面、同墨同质感层、不得排印字体 | `[归纳]` | `dossiers/blake.md:L214`（§8.2-3）、`:L207`（§8.1 自查）、`:L35`（§1-3 写 5–40%） | unverified（阈值未像素实测） |
| LB-M2-WIRE | 铁丝轮廓：≥80% 边界连续硬线、线宽变异 2–3:1；交叉排线 0 命中 | `[自述]`+`[归纳]` | `dossiers/blake.md:L33`（§1-1）、`:L34`（§1-2）、`:L122`（§5-8 E550）、`:L212`（§8.2-1）、`:L213`（§8.2-2） | partial（线价值有自述支撑；量化阈值 unverified） |
| LB-M3-WASH | 手工水彩套色：印后逐本上色、平涂 ≤12%、主色 ≤10、金 ≤5%、每本配色不同 | `[史料]`+`[归纳]` | `dossiers/blake.md:L39`（§1-7）、`:L50`（§2-3）、`:L51`（§2-4）、`:L52`（§2-5）、`:L215`（§8.2-4） | partial（工艺有馆方著录；阈值 unverified） |
| LB-M4-P4ZERO | **版画线雕+水彩套色机制**：先同版印纯线，再逐本手工平涂上色；灰阶不来自线密度 | `[史料]`+`[归纳]` | `dossiers/blake.md:L34`、`:L39`、`:L48`、`:L50`、`:L52`；`modules/blake.md:视觉指纹 1-3` | supported（机制）/ 阈值 unverified |
| LB-M4-P4 | P4 文字板比例弱档 = **`0%（纯图像；大彩色版画档）`**；§8.1 说明写 0–5%；中 5–15%；强 25–40% | `[归纳]` | `dossiers/blake.md:L95`（§4 P4）、`:L206`（§8.1 中文说明） | unverified |
| LB-M6-LIGHT | 辐射光：§8.2-5 面积 ≥8%；§4 P6 强档 ≥20%；同一量两个下限 | `[归纳]` | `dossiers/blake.md:L216`（§8.2-5）、`:L97`（§4 P6）、`:L36`（§1-4） | unverified |
| LB-M7-PANTHEON | 神谱锚点 / 非重力动态 / 页面框（§8.2-6/7/8） | `[研究]`+`[归纳]` | `dossiers/blake.md:L217`、`:L218`、`:L219`；`:L40`（§1-8 Tate `[R5]`） | partial |

---

<a id="db-source-line-60"></a>
## §D 冲突行 / 反例（learning_path §4 阶梯、§6；mechanism_notes §D）

| claim_id | claim | grade | locator | support_status |
|---|---|---|---|---|
| LB-C-NOROW | conflicts.md **无 blake 专属 C-row**（`grep -c -i 'blake|布莱克'` = 0）；`blake_own_C_rows=0` 为事实非缺陷 | `[归纳]` | [conflicts.md](../../../../cross/conflicts.md)（全文）；`AUDIT-blake/RESULT.md:§5 L61`；`AUDIT-blake/coverage-manifest.json` | supported |
| LB-C07 | C-07 硬冲突（丢勒排线 × 北斋平涂）；blake 为「无排线」侧第三例（轮廓线+手工色层+文字板），须额外声明「图文一体」轴 | `[归纳]` | `conflicts.md:L38`、`:L136-L147`；`dossiers/blake.md:L85`（§3.1）、`:L224`（§8.3-1） | supported（规则层） |
| LB-C12 | C-12 色相面积预算（北斋蓝 ≥40% / 卡拉瓦乔土色 / 梵高互补 1:1）；blake 主张蓝绿/赭/玫红+金 ≤5% | `[归纳]` | `conflicts.md:L43`、`:L203-L215`；`dossiers/blake.md:L231`（§8.3-3） | supported（规则层） |
| LB-C14 | C-14 渐变：Lane B 反约束「别做成：渐变」不误伤 blake（平涂水彩不需要渐变） | `[归纳]` | `conflicts.md:L45`、`:L229-L241`；`dossiers/blake.md:L208`、`:L226` | supported（规则层） |
| LB-C16 | C-16 反约束适用域：「没有高光的平涂」须删除/加限定，否则误伤平涂系（含 blake） | `[归纳]` | `conflicts.md:L47`、`:L258-L270` | supported（规则层） |
| LB-N3 | 组合按 §3 N3「轴所有权表」：同轴唯一持有者、辅模块 §8.2 整条移除 | `[归纳]` | `conflicts.md:L311-L312` | supported（规则层） |
| LB-NM-NOROW | `conflicts.md` §4 near-miss 表（L345–356，10 行）**无 blake 行**；P6 ≥20% × §8.2-5 ≥8% 应补未补 | `[inference]` | `conflicts.md:L345-L356`；`AUDIT-blake/counterexample.md:§反例2 L14-L17` | partial（应补未补，登记不改写） |
| **LB-CE-1** | **反例 1（重点）**：§4 P4 弱档 `0%（大彩色版画档）`（L95 / L206 0–5%）× §8.2-3 `文字区 5–35%`（L214）在「大彩色版画档」合法取值上**互斥**；自查双判 | `[inference]` | `dossiers/blake.md:L95`、`:L206`、`:L214`；`AUDIT-blake/counterexample.md:§反例1 L5-L12` | partial（规则系统内部张力，非史实证伪） |
| LB-CE-2 | 反例 2：§4 P6 强档 ≥20%（L97）× §8.2-5 ≥8%（L216）交集非空须显式取值；取 12% 满足后者不满足前者 | `[inference]` | `dossiers/blake.md:L97`、`:L216`；`AUDIT-blake/counterexample.md:§反例2 L14-L17` | partial |
| LB-DRIFT | conflicts.md 7 处行号漂移（durer/hokusai/caravaggio/vermeer）只报告不修改 | `[归纳]` | `AUDIT-blake/locator_drift.md`；`conflicts.md:§5.C L404` | supported（文书层） |

---

<a id="db-source-line-77"></a>
## §E How-to-Think 决策步（how-to-think.md §1 的 D1–D8，每步带 grade + 定位）

| claim_id | D 步 | grade | locator | support_status |
|---|---|---|---|---|
| LB-D1 | D1 先判「图文同版一次印」，拒「图+配文/文字另起一层」 | `[归纳]`（依据 `[史料]`） | `dossiers/blake.md:L6`、`:L48`、`:L49`、`:L55`；`how-to-think.md:§1 D1` | supported（规则层） |
| LB-D2 | D2 拒交叉排线/线密度明暗，线只留给轮廓 | `[归纳]`（线价值 `[自述]` E550） | `dossiers/blake.md:L34`、`:L122`、`:L212`、`:L213`；`how-to-think.md:§1 D2` | partial |
| LB-D3 | **D3 先声明 P4 档位并显式写值**（书页 5–40% / 大彩色版画 0–5%） | `[归纳]` | `dossiers/blake.md:L95`、`:L206`、`:L214`；`how-to-think.md:§1 D3` | unverified |
| LB-D4 | D4 文字当图形安排、同墨同层、非排印字体 | `[归纳]`（原理 `[研究]` Tate） | `dossiers/blake.md:L35`、`:L214`、`:L202`、`:L347`（§12-1）；`how-to-think.md:§1 D4` | partial |
| LB-D5 | D5 画内单中心光源、显式写面积（≥8% / ≥20%） | `[归纳]`（装置 `[史料]` BM） | `dossiers/blake.md:L36`、`:L216`、`:L97`；`how-to-think.md:§1 D5` | unverified |
| LB-D6 | D6 符号来自命名神谱而非情绪结晶（vs 蒙克） | `[归纳]`（清单 `[研究]` Tate） | `dossiers/blake.md:L40`、`:L218`、`:L77-L80`（§3.1）；`how-to-think.md:§1 D6` | partial |
| LB-D7 | D7 幻视身体而非写生人体（躯干轴 ≥15°） | `[归纳]` | `dossiers/blake.md:L37`、`:L217`、`:L96`（§4 P5）；`how-to-think.md:§1 D7` | unverified |
| LB-D8 | D8 页面建筑收尾（框/拱/对称 ≥60% 或涡旋） | `[归纳]`（装置 `[史料]`） | `dossiers/blake.md:L38`、`:L42`、`:L219`；`how-to-think.md:§1 D8` | unverified |
| LB-D-SEP | D1–D8 全部为研究者构造 `[归纳]`，**不是布莱克自述**；自述/史料只作输入 | `[归纳]` | `how-to-think.md:§2`；`dossiers/blake.md:L6`；`00-GOAL.md:L9` | supported |

---

<a id="db-source-line-93"></a>
## §F 练习 / 边界 claims（learning_path §4–§8、mechanism_notes §F）

| claim_id | claim | claim_kind | support_status | locator |
|---|---|---|---|---|
| LB-LADDER | 三段阶梯 rung1 线雕+套色 → rung2 图文同版+0%/5–35% 灰区显式取值 → rung3 辐射装置+组合预检，全部为**建议练习** | design_candidate | not_applicable | `learning_path.md:§4`；`dossiers/blake.md:L343-L398`（§12）；`01-AUDIT.md:§8.1 L273` |
| LB-PRACTICE-SUGGESTED | 练习效果未由人完成/评价；不写「已证实学习收益」；`human_review.status=not_applicable` | design_candidate | not_applicable | `01-AUDIT.md:§8.1 L273`、`:§8.4 L308-L310`；`receipt.json:human_review` |
| LB-BOUND-1 | 未打开外部 URL / 未目检 18 图（image_seen=0）/ 未像素测量 / 无真人评价 | fact | supported | `AUDIT-blake/RESULT.md:§6 L70-L74`；`receipt.json:execution.limitations` |
| LB-BOUND-2 | NO repo writes / NO subagent spawns / NO credentials；写入仅 内部证据 b0f0d1cc8da67ca2（未公开；来源记录由维护者保留）；AUDIT 为 ACCEPTED 依赖不重审 | fact | supported | `receipt.json:allowed_write_paths`、`:spawns_allowed`、`:execution_kind` |
| LB-BOUND-3 | 3 条 OVERTURNED 作为已解决事实，不作为未决争议进入 C-rows/失败条件 | fact | supported | `AUDIT-blake/RESULT.md:§4`、`:review-evidence.md:§2`；`learning_path.md:§2` |
| LB-RECEIPT | `status=submitted` / `review:null` / attempt 1 / repair_round 0；verify-receipt.py 仅跑 JSON Schema 结构门 | fact | supported | `receipt.json`；`tools/verify-receipt.py:validate()` |

---

<a id="db-source-line-106"></a>
## §G 定位方法（照 AUDIT locator 纪律）

- 每条 locator 为 `文件:行号` 或 `文件:节:行号`；本机档案行号按 `git HEAD f0089523…` 当前工作树实测（`nl -ba`）。
- AUDIT-blake 自身 `raw/check_locators.py` 实跑 `locators_checked=78 bad=0`（`AUDIT-blake/RESULT.md:§3 L43`）；本 LEARN 沿用同一纪律，新增行号均现场 `nl -ba` 复核（L95 / L97 / L206 / L212–L219 / L345–L356 / L413–L415 等）。
- conflicts.md 7 处行号漂移按 §5.C L404「先怀疑行号、再怀疑内容」处理，**不改文件**。
- 外部 URL（archiveofletters / Commons / BM / Met / Tate）只引用 AUDIT 已取回并记 sha 的缓存字节，本 shard 不重跑外网、不升级 partial 为 supported-to-online-text。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
