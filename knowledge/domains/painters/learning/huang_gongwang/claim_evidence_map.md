<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-huang_gongwang；原正文 SHA-256 `d68d1b3d12ba3f72eed443a57b64831c60d60dda97b416cbcbd67e98a7a5c974`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-huang_gongwang — claim / evidence 图（逐 claim 带定位）

> 本图给 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 里**每一条实质 claim** 配 `文件 : 节 : 行号` 定位（dossier / corpus / 卡 / conflicts / AUDIT 产物 / 01-AUDIT 与 00-GOAL 规范）。沿用 ACCEPTED 审计 内部证据 b4ec96ea6d2f14dc（未公开；来源记录由维护者保留） 的 locator 纪律，不重审、不改 repo。
> 基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（repo READ-ONLY）。等级照录 [huang_gongwang.md](../../dossiers/huang_gongwang.md) §0 L5：`[自述]/[史料]/[研究]/[归纳]/[推测]`；语料类型照 `corpus/huang_gongwang.md` L4：`[self-written]/[contemporary record]/[later reception]`。
> **support_status 只评「本机档案内自洽 / 定位可寻址 / 类型正确」**，不评外部原文真伪、不评学习成效（AUDIT 同口径）。
> 输入 hash（开工实测，见 `RESULT.md` §0）：card `29e87100…98e5`、dossier `95eb6a68…fbd5`、corpus `c31e10c4…8fb`、conflicts `314a24da…aaef`、AUDIT claim_evidence_map `8ffb5ab0…f58`、AUDIT RESULT `a850dffc…a0cc`、AUDIT counterexample `a17967a8…d04`、AUDIT review-evidence `ee9b5a86…56b`。

---

<a id="db-source-line-10"></a>
## §A 证据结构 / 分级（learning_path §1、how-to-think §0/§2）

| claim_id | 内容 | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| C-SELF-YES | 黄公望**有自述**：《写山水诀》（《辍耕录》卷八转录）Q1–Q10 + 自题自识 Q11–Q13 全为 `[self-written]`；本 shard 可引用其**语义/技法层** | `[自述]` / `[self-written]` | `corpus/huang_gongwang.md` L4（类型定义）、L8–L73（§一 Q1–Q10）、L77–L94（§二 Q11–Q13）；[huang_gongwang.md](../../dossiers/huang_gongwang.md) §5 L108–L131；`AUDIT/claim_evidence_map.md` §E（HG-Q1…Q13） | corpus + dossier + AUDIT |
| C-SELF-LIMIT | `[自述]` **不可扩大**到 §4 六参数 / §8.2 七规则 / §3.1 分工 / 量化阈值：档案自陈「未对原作做像素测量 / 未实测参数」 | 口径 | [huang_gongwang.md](../../dossiers/huang_gongwang.md) §10-10 L264、自审 D L427；`AUDIT/claim_evidence_map.md` §D（HG-§4-P1…P6 全 unverified） | dossier + AUDIT |
| C-GRADE-DEF | 证据级定义（自述/史料/研究/归纳/推测） | 口径 | [huang_gongwang.md](../../dossiers/huang_gongwang.md) §0 L5；`AUDIT/claim_evidence_map.md` L16 | dossier + AUDIT |
| C-NO-PSYCH | 禁止从画面外观编造作者心理；§11 生平「迎静气，去躁气 / 淡泊宁和 / 宗教性静观」是 `[研究]/[史料]` 学界解读，不是自述、不是心理学结论 | 规范 + `[研究]` | `00-GOAL.md` L9；`01-AUDIT.md` §8.4 L308；[huang_gongwang.md](../../dossiers/huang_gongwang.md) §11 L276 | 规范 + dossier |
| C-QUOTE-TRANS | 6 条语料 Q14/Q16/Q17/Q18/Q19/Q23 标「转引、未直读原件」→ unverified，不得当一手自述 | 口径 | `corpus/huang_gongwang.md` L98、L112、L119、L125、L131、L158、L171；`AUDIT/claim_evidence_map.md` §E（HG-Q14/16/17/18/19/23）；`AUDIT/RESULT.md` §4 | corpus + AUDIT |
| C-48-DENOM | AUDIT 分母：65 行 = §1–§4 33（§1:10+§2:10+§3:7+§4:6）+ corpus 24 + meta 8；per-status 44/7/2/12 | observation supported | `AUDIT/claim_evidence_map.md` L13–L21；`AUDIT/coverage-manifest.json`；`AUDIT/review-evidence.md` §1 L14–L19（独立复核） | AUDIT |
| C-81B-NONE | 本卡 `card_has_81b = False`（ledger），无 §8.1b 纯风格段；不虚构派生关系 | observation | 内部证据 9d3994cf3e8723cb（未公开；来源记录由维护者保留） huang 条目；[huang_gongwang.md](../../dossiers/huang_gongwang.md) §8.3 L209–L212 | ledger + dossier |

---

<a id="db-source-line-24"></a>
## §B 重点作品及来源（learning_path §2，全部引用 §12 现有记录）

| claim_id | 作品（照录 §12 标题/馆藏） | 定位 | 引用性质 |
|---|---|---|---|
| C-W1 | 《富春山居图·剩山图》卷（浙江省博物馆；1347–1350）：长披麻组线节奏、淡墨层积痕 | [huang_gongwang.md](../../dossiers/huang_gongwang.md) §12-1 L319–L322；§1-2 L29；§2-2 L42 | §12 现有记录 + `[自述]` Q2 工序 |
| C-W2 | 《富春山居图·无用师卷》（台北故宫；33×636.9cm 六纸）：段落节奏、点苔、点景极小、自题「閱三四載」 | §12-2 L323–L326；§1-3 L30、§1-10 L37；§5-4 L119；§3-7 L60；`corpus` Q11 L77–L82 | §12 + NPM 著录（AUDIT RF-2 命中）+ `[自述]` 自题 |
| C-W3 | 《九峰雪霁图》轴（故宫；1349，117×55.5cm，81 岁）：借地为雪、干笔勾廓叠石、P1=弱/P2=2 级 | §12-3 L327–L330；§7-2；`AUDIT/risk_fetches.md` RF-3（dpm 234602）；`modules` §4 P1 弱 L59、P2 弱 L64 | §12 + `[研究]` 故宫（RF-3）+ CE-1 边界样本 |
| C-W4 | 《天池石壁图》轴（故宫；1341，139.4×57.3cm，73 岁）：浅绛「淡赭/墨青墨绿合染」、P1=强/P4=强 | §12-4 L331–L334；§1-7 L34；§2-8 L48；`AUDIT/risk_fetches.md` RF-4（dpm 229315） | §12 + `[研究]` 故宫评（非自述）+ `[自述]` 设色法 |
| C-W5 | 《丹崖玉树图》轴（故宫）：纸本干笔松秀、云烟「不画之画」 | §12-5 L335–L338 | §12 |
| C-W6 | 《快雪时晴图》卷（故宫；29.7×102.6cm）：小幅雪景、题跋参与构图 | §12-6 L339–L342 | §12 |
| C-W7 | 《九珠峰翠图》轴（台北故宫；约 1346–48）：低饱和青绿、中锋使笔 | §12-7 L343–L346；`_images/manifest.md` CC0 行；`AUDIT/rights_review.md` 第 10 行 | §12 + 权利记录 |
| C-W8 | 《富春大岭图》轴（南京博物院）／《剡溪访戴图》轴（云南省博物馆；1349）：立轴 vs 长卷；公开高清图未获取（L351） | §12-8 L347–L352 | §12（含 L351 边界声明） |
| C-W-RIGHTS | 10 张公开图 = 9 PD-Art + 1 CC0，私有层 14 件版权未清；image_seen=false / read_scope=metadata、不复制像素 | [manifest.md](../../dossiers/_images/manifest.md) §huang；`AUDIT/rights_review.md`；`AUDIT/claim_evidence_map.md` HG-RT-01；`AUDIT/coverage-manifest.json` | AUDIT + manifest |

---

<a id="db-source-line-40"></a>
## §C 南宗山水三机制 + 关联机制（learning_path §3 / mechanism_notes §A-§B）

| claim_id | 内容（含数值） | 等级 | 定位 | 卡对应 |
|---|---|---|---|---|
| C-M1-PIMA | 用笔·披麻皴：成组 ≥3 线/组、夹角 ≤30°、折角 ≤1/10 线、线宽变化 ≤50%、无斧劈钉头 | `[归纳]` 判据 / `[自述]` 用笔观 / `[研究]` 故宫评 | [huang_gongwang.md](../../dossiers/huang_gongwang.md) §1-1 L28、§2-1 L41、§2-10 L50、§4 P1 L78–L81、§8.2-1 L201；`corpus` Q6 L45；`modules` L48、L58–L61 | 卡 L48/L58 |
| C-M2-JIMO | 用笔·积墨：淡墨→焦墨浓墨工序（`[自述]`）；判据 3–5 带、淡墨 ≥50%、浓墨 ≤10%、禁中灰平涂 | `[自述]`（工序 Q2/Q3）+ `[归纳]`（级数/阈值） | `dossiers` §1-2 L29、§2-2 L42、§2-3 L43、§8.2-2 L202；`corpus` Q2 L18、Q3 L24；`modules` L49、L63–L66 | 卡 L49/L63 |
| C-M3-PAPER | 留白·纸色主调：留纸 40–60%、浓墨 ≤10% | `[归纳]`（AUDIT HG-§1-8 = partial，未实测） | `dossiers` §1-8 L35；§8.2-2 L202；`AUDIT/claim_evidence_map.md` §A HG-§1-8 | 卡 L49 |
| C-M4-WATER | 水位：水面高亮带 ≥25%（§8.2-3）/ ≥30%（§1-4）双阈值、横向贯穿 ≥60%、水面墨线 ≤3% | `[归纳]`（阈值）/ `[自述]`（三远/水法输入） | `dossiers` §1-4 L31、§2-4 L44、§2-7 L47、§4 P5 L98–L101、§8.2-3 L203；`corpus` Q5 L37–L42；`modules` L50、L78–L81 | 卡 L50/L78 |
| C-M5-DIANTAI | 点苔：簇 ≥3/段、单点 ≤山高 2%、落位比例 ≥60%；§1-5 另取「≥20 点」 | `[归纳]`（两处均无独立实测，AUDIT partial）/ `[自述]`（矾头/淡螺青 §2-6 L46） | `dossiers` §1-5 L32、§2-6 L46、§8.2-4 L204；`AUDIT/claim_evidence_map.md` HG-§1-5 | 卡 L51 |
| C-M6-RHYTHM | 长卷节奏：≥5:1 时 ≥3 段、段落极差 ≥30%、镜像相关系数 ≤0.6 | `[归纳]`（判据）/ `[自述]`（自题事实）+ `[归纳]`（「时间容器」命名 HG-§3-7） | `dossiers` §1-3 L30、§3-7 L60、§4 P3 L88–L91、§5-4 L119–L121、§8.2-5 L205；`corpus` Q11；`modules` L52、L68–L71 | 卡 L52/L68 |
| C-M7-QIANJIANG | 浅绛色域：彩色 ≤20%、色相 ≤2 族、平均饱和度 ≤35%、单块 ≥70% 饱和区 ≤2% | `[归纳]` / `[自述]`（藤黄水/螺青入墨）+ `[研究]`（故宫浅绛评） | `dossiers` §1-7 L34、§2-8 L48、§4 P4 L93–L96、§8.2-6 L206、§8.1 L186–L197；`modules` L53、L73–L76 | 卡 L53/L73 |
| C-M8-POINT | 点景/动画：人物 ≤树高 1/5、每段 1–3 处；点景位移 ≤1%/秒、墨迹帧间差 ≤1%、禁特写/叙事/推拉 | `[归纳]` / `[自述]`（远人无目/士人家风） | `dossiers` §1-9 L36、§2-7 L47、§3-5 L58、§4 P6 L103–L106、§8.2-7 L207；`corpus` Q8；`modules` L54、L83–L86 | 卡 L54/L83 |
| C-THRESH-INDUCTION | 全部 §4/§8.2 阈值 `[归纳]`、未像素测量、分母应为同批对照实验全部帧 | 口径 | `dossiers` §10-10 L264、自审 D L427；`AUDIT/claim_evidence_map.md` §D；`AUDIT/RESULT.md` §4 第 2 条 | dossier + AUDIT |
| C-81 | §8.1 正向/负向/6 项核对/强度旋钮/退化处理/组合注记；`--no` 是生成护栏、不是历史断言 | `[归纳]` | `dossiers` §8.1 L163–L197（自注 L197）；`modules` L15–L44 | 卡 + dossier |
| C-83 | §8.3 野外样本「未见成熟可复制 prompt 模板」，§8.1 原创首版 | `[史料]`（本机） | `dossiers` §8.3 L209–L212 | dossier |
| C-NO-GUARD-HIST | 《天池石壁图》设色略重是 §8.2-6 边界；不得把 `--no` 护栏写成黄公望主张 | `[归纳]` | `dossiers` §8.1 L197 | dossier |

---

<a id="db-source-line-59"></a>
## §D 冲突行 / 已知未决冲突 / 分工（learning_path §6/§8、how-to-think D1/D8、mechanism_notes §D）

| claim_id | 对象 | 双方定位（回源） | 判定 | support_status |
|---|---|---|---|---|
| **C-CONFLICT-Q1** | **《写山水诀》去四病 引文逐字冲突**（brief 点名 known-open） | wikisource《辍耕录》卷八底本 `AUDIT/raw/fetch_80237e36.bin`（sha `e77732ca…9737`，`AUDIT/risk_fetches.md` RF-1）：「作畫大要去邪、甜、俗、賴四個字」（**无逗号**）；dossier §3-1 L54 / §5-1 L110 / `corpus` Q1 L11：「作畫大要，去邪、甜、俗、賴四個字。」（**加逗号**）；`dossiers` Q1 备注见 `corpus` L15「另有版本作…」未记出处 | `conflict`（引文措辞级，HG-§3-1 / HG-Q1），语义不变；`AUDIT/review-evidence.md` §5 L49–52 独立确认（缓存 `四個字` 出现 1 次） | **conflict（known-open，不裁断）** |
| C-CF-ZERO | conflicts.md 18 条 C + 11 条 near-miss 全扫，**0 条命名黄公望**；卡 L90 要求「先读对应 C 条」但无专属详条 | `conflicts.md` §1 L32–L49、§4 L345–L357；`modules` L88–L100；`AUDIT/claim_evidence_map.md` HG-CF-01；`AUDIT/locator_drift.md` DR-1 | 覆盖/指针漂移，只报告不修；本 lane 不虚构 C 行 | supported（observation） |
| C-N-RULES | §3 通用 N1–N9 可援引（N2 适用域、N3 轴所有权、N4 可拆判别、N8 运动字段、N9 验收口径） | `conflicts.md` §3 L300–L337（N1 L305、N2 L308、N3 L311、N4 L314、N9 L332）、L303 采纳状态 | `[归纳]` 通用规则正本 | supported（本机定位） |
| C-DIVISION | §3.1 四组分工（vs 八大山人/塞尚/北斋/范宽）写死、`[归纳]`、可被组合实验推翻（L62） | `dossiers` §3.1 L62–L74；`modules` L88–L95；`AUDIT/claim_evidence_map.md` HG-§3.1 | 卡内分档，非 conflicts.md 专属 C 行 | supported（作为已写死规则文本存在且可寻址） |
| C-CE1 | CE-1：P1=弱 雪景 × §8.2-1「≥3 线/组」在同合法帧互斥 | `AUDIT/counterexample.md` CE-1（L10–L30）；`conflicts.md` §3 N3 L312；`dossiers` §4 P1 L79；`AUDIT/risk_fetches.md` RF-3（故宫「留白/勾廓」） | `[inference]`，未实测像素（image_seen=false） | unverified（构造反例） |
| C-CE2 | CE-2：§1-4 ≥30% vs §8.2-3 ≥25% 同轴双阈值，27% 帧给相反判定 | `AUDIT/counterexample.md` CE-2（L34–L48）；`AUDIT/claim_evidence_map.md` §G HG-CF-INTERNAL；`conflicts.md` §3 N3 L312、N4 L315 | `[inference]`，阈值均无独立实测 | unverified（构造帧） |
| C-CE3 | CE-3：§8.2-7 运动预算 × 长卷「时间展开」适用域未声明 | `AUDIT/counterexample.md` CE-3（L52–L62）；`dossiers` §3-7 L60、§8.1 L179；`conflicts.md` §3 N2 L309、N8 L330 | `[inference]`，「镜头推拉 vs 视点水平平移」未定义 | unverified（构造动画） |
| C-NM-DRIFT | 卡 L100 / `conflicts.md` §5-C L365「near-miss 8 对」vs §4 实 11 行（#9–#11 带 2026-10-16 补） | `modules` L100；`conflicts.md` §4 L347–L357、§5-C L365；`AUDIT/claim_evidence_map.md` HG-NM-01；`AUDIT/locator_drift.md` DR-2 | 历史计数口径漂移，只报告不修 | supported（漂移事实层） |
| C-DR-GOALS | GOALS A-47 L130「全 PD / 《写山水诀》11 条 / 三卷+剩山图」与落盘事实（1 张 CC0 / §一 10 标题 / 重叠计数）措辞差 | `ops/GOALS.md` L130；`AUDIT/claim_evidence_map.md` HG-GO-01；`AUDIT/locator_drift.md` DR-4 | partial（历史摘要措辞） | partial |
| C-DR-EXTRACT | `_extract.py` 观测 sha `4afa31ec…44d4`（AUDIT 实跑 228/228 EXIT=0）≠ execution-snapshot `e7e96645…30fee` | `AUDIT/claim_evidence_map.md` HG-IN-01、HG-DR-01；`AUDIT/RESULT.md` §2、§4 第 7 条 | 另一 lane（GatesRepair）工作树编辑，已声明 | supported（observation） |

---

<a id="db-source-line-76"></a>
## §E How-to-Think D 步（how-to-think.md §0/§1，逐 D 定位）

| D | 核心 claim | `[自述]` 锚点 | `[归纳]/[推测]` 锚点 | known-open / 失效 |
|---|---|---|---|---|
| D1 | 先立题目 + 去四病语义护栏 | §3-4 L57（先立題目，`[自述]`）；Q1 语义（去四病） | D 排序为 `[归纳]`；§8.1 L181/L191「never sweet」护栏 | **去四病逐字 conflict**（C-CONFLICT-Q1） |
| D2 | 师董巨 + 师造化 | §3-6 L59（必以董为师法）、§2-9 L49 / Q7（皮袋描笔） | §3.1 L71–L73 分档 `[归纳]` | 组合时按分档 |
| D3 | 用笔：先淡后浓、筋骨相连 | Q2 L18 / §2-2 L42、Q3 / §2-3 L43、§2-10 L50 / Q6、§3-2 L55 | §8.2-1/-2 L201–L202、§4 P1/P2 三档 | CE-1（弱档） |
| D4 | 水位/留白：平远·阔远、江面为主骨 | §2-4 L44 / Q5（三远定义）、§2-7 L47（水法） | §8.2-3 L203、§1-4 L31、§4 P5；「阔远代深远」为 `[研究]` [R10]（HG-§2-4） | CE-2 双阈值 |
| D5 | 浅绛 + 点苔 | §2-8 L48（藤黄水/螺青）、§2-6 L46（矾头） | §8.2-4/-6 L204/L206、§4 P4；故宫浅绛评 `[研究]` | §8.1 L197 护栏非史断言 |
| D6 | 长卷 = 时间容器 | §5-4 L119 / Q11（逐旋填剳，閱三四載）、§3-7 L60 | 「时间容器」命名 `[归纳]`（HG-§3-7）；§8.2-5 L205、§4 P3 | CE-3 适用域 |
| D7 | 点景极小 + 收束 | §2-7 L47（遠人無目）、§3-5 L58 / Q8（士人家风） | §1-9 L36、§4 P6、§8.2-7 L207；款印 `[史料]` §1-10 L37 | §3.1 八大分档；CE-3 |
| D8 | 组合前预检分工 + N 规则 | —（全部 `[归纳]`） | §3.1 L62–L74、`conflicts.md` §3 N1–N9、卡 L88–L100 | 0 专属 C 行（C-CF-ZERO）；near-miss 计数漂移 |

---

<a id="db-source-line-91"></a>
## §F 规范 / 建议练习口径（learning_path §5/§8、how-to-think §3、mechanism_notes §F）

| claim_id | 内容 | 定位 |
|---|---|---|
| C-A30-SHAPE | A-30 §8.1 要求每路径至少 8 节：前置知识 / 重点作品及来源 / 要观察的机制 / 具体练习 / 可观察结果 / 常见失败 / 下一步 / 使用边界；总路线说明基础-进阶、可替换分支、跨艺术家比较 | `01-AUDIT.md` §8.1 L269–L273（「每位路径至少明确」L271）、L272（跨艺术家比较）、L273（建议练习） |
| C-SUGGESTED | 练习效果尚未由人评价 → 明确为**建议练习**，不写「已证实学习收益」 | `01-AUDIT.md` §8.1 L273；`01-AUDIT.md` §8.4 L308（禁止模拟人评 / 多模型一致替代人评）、L310（人评材料就绪 vs 完成） |
| C-NO-HUMAN | 本 shard `human_review.status=not_applicable`、`review:null`、status=submitted；练习为建议练习，产物级观察 ≠ 学习成效 | `RESULT.md` §5；`receipt.json` |
| C-NO-REPO | 本 lane NO repo writes / NO subagent spawns / NO credentials；AUDIT 为 ACCEPTED 依赖、复用不重审 | brief；`AUDIT/review-gate-receipt.json`（verdict `accepted`）；`AUDIT/review-evidence.md` L8 |
| C-RIGHTS-BOUND | 9 PD-Art + 1 CC0、私有层 14 件版权未清、image_seen=false、不复制像素/不重新授权 | `AUDIT/rights_review.md`；`AUDIT/coverage-manifest.json`；[manifest.md](../../dossiers/_images/manifest.md) |

---

<a id="db-source-line-103"></a>
## §G 定位可复跑 / 自洽性声明

- 本图所有 locator 均为 `文件 : 节 : 行号` 或 `文件 : 行号`，沿用 AUDIT `verify_locators.py` 已 exit 0 的同一套钉定行号（基线 `f008952365a77e140cbda3f3959d43ef000f9a22`）；本 lane 未改动任何 repo 文件，故行号不漂移。
- 冲突行 C-CONFLICT-Q1 的「无逗号」侧证据是 AUDIT 缓存字节 `raw/fetch_80237e36.bin`（sha `e77732ca…9737`），经 `AUDIT/review-evidence.md` §5 独立复核；本 lane 未重新打开外部 URL，只复用 ACCEPTED 判定。
- 证据底本：内部证据 a37e92977cc1f75e（未公开；来源记录由维护者保留）（ACCEPTED）——本图复用其 §A/§B/§C/§D/§E/§G 判定与 locator，未重新盘点、未重审。
- `support_status` 仅评本机自洽与定位可寻址；外部原文真伪、图像像素、学习成效均不在本图判定范围（AUDIT 同口径）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
