<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-bada_shanren；原正文 SHA-256 `af0c4939736f58c267d5adcdf6643dcf56884749ba6b209cd6c2780c3f8e63ac`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-bada_shanren — Claim/Evidence Map

> 任务 `LEARN-bada_shanren`（A-30）· baseline `f008952365a77e140cbda3f3959d43ef000f9a22` · 2026-11-15。
> **证据底座 = ACCEPTED 的 内部证据 e4749e062c77ce88（未公开；来源记录由维护者保留）**（`receipt.json status=accepted`；`review-evidence.md §9` PASS/accepted，reviewer `ReviewGateAUDIT-bada_shanren(glm-5.3-flash)` 独立复核）。本 lane **不重新审计冻结仓库**，复用 AUDIT 的 81 行 claim map（`AUDIT-bada_shanren/claim_evidence_map.md` sha `846775bf…0550`）+ `coverage_manifest.json`（`d86f719d…437e`）+ `RESULT.md`（`4e3a88cd…5353`）+ `counterexample.md`（`1b2bf68b…c31c`）作为输入哈希。
> 定位格式 `file :: section :: line(s)`，对冻结仓库；规则类冲突一律用**规则 ID + 子串**（conflicts.md 绝对行号已过时，AUDIT `RESULT.md §27-32` 报告未修）。
> 等级：`[自述]`(本卡=0) / `[self-written·转录]` `[reported speech]` `[contemporary record]` `[later reception]`（同代/转述/转录/后世记录）/ `[史料]` / `[研究]` / `[归纳]`（项目推断，未实测）/ `[推测]`（本卡=0）。
> 支持状态：supported / partial / conflict / unverified / not_applicable。

---

<a id="db-source-line-11"></a>
## A. 输入、依赖与验收（本 lane 实跑 / 照记）

| claim_id | claim (short) | locator | grade | support_status | basis |
|---|---|---|---|---|---|
| LBS-INPUT-01 | 三件冻结输入 sha = dossier `2df14ad4…9007` / card `45441d8b…7c8a` / corpus `2427a3cc…96c0`，逐字等于 内部证据 8de1937ac62ea341（未公开；来源记录由维护者保留） 与 `AUDIT-bada_shanren.contract.json` | `RESULT.md §Evidence`；`AUDIT-bada_shanren.contract.json:21-30` | `[实测]` | supported | 本 lane 开工 `sha256sum`（cwd 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留））6 个仓库文件全中；`runner_receipt.json` 命令段记录 |
| LBS-INPUT-02 | 二级哈希 = conflicts `314a24da…bbef` / `_images/manifest.md` `5698124d…b470` / GOALS `2727d1f0…1144` | `RESULT.md §Evidence` | `[实测]` | supported | 同上 `sha256sum` 实跑 |
| LBS-DEP-01 | 上游 `AUDIT-bada_shanren` = **ACCEPTED**（`status=accepted`、`review` 独立 reviewer、`verdict` 非自审）；无需重审 | `AUDIT-bada_shanren/receipt.json:6`（status）、`review-evidence.md §9`（PASS/accepted）、`§1`（reviewer 复点 81/22/14/per-status/locator 全 MATCH） | `[实测]` | supported | 本 lane 实读；依赖状态写入 `runner_receipt.json dependency` |
| LBS-DEP-02 | 4 个 web fetch 缓存 sha 全中（sohu `57c3c222…` / CUHK `0c04e30c…` / wiki `a6183c4b…` / Met `5f27ea09…`） | `AUDIT-bada_shanren/review-evidence.md §2`、`coverage_manifest.json external_fetches` | `[实测]`(上游) | supported | reviewer 独立 re-hash；本 lane 照记，不升级为「本轮已重访」 |
| LBS-A30-SHAPE | 学习路径 = A-30 §8.1 八节形状（前置/作品/机制/练习/结果/失败/下一步/边界），练习标「建议练习」不写「已证实学习收益」 | `01-AUDIT.md:269-273`（package sha `738d6a5a…aacf`）；`learning_path.md §1-§8` | `[实测]` | supported | 八节标题 + 抬头练习状态声明齐备 |
| LBS-VERIFY | `verify-receipt.py` 对本 lane `receipt.json` → `{"ok":true,"status":"submitted","errors":[]}`，exit 0 | `receipt.json`；`runner_receipt.json verify_result` | `[实测]` | supported | 本 lane 实跑；`jsonschema 4.26.0` 在场（非 BLOCKED） |

<a id="db-source-line-22"></a>
## B. 两条主轴（白眼向天造型 + 计白当黑机制）

| claim_id | claim (short) | locator | grade | support_status | basis |
|---|---|---|---|---|---|
| LBS-M-WE-01 | **白眼向天**：眼棱角、瞳孔上角、视线朝上外 | `dossiers/bada_shanren.md:30`（§1-3）、`:56`（§3-3）、`:47`（§2-7） | `[研究]` | supported | AUDIT `§A BS-§1-3` supported（R3/R4/R20）；「气节写照」为 `[研究]` 措辞，不作意图自述 |
| LBS-M-WE-02 | **§8.2-4 可判定谓词**：4±1 边 / 瞳孔中心≤包围盒上半(中心−20%高) / 面积≤25% | `dossiers/bada_shanren.md:194`；`modules/bada_shanren.md:46 区` | `[归纳]` | unverified | AUDIT `§F BS-§8.2-4` unverified（未实测）；dossier `§D:394` 自认 |
| LBS-M-WE-03 | **P3 白眼符号化** 弱圆眼/中方眼/强方眼+顶角+缩颈独立 | `dossiers/bada_shanren.md:80-83`（§4 P3）；`modules/bada_shanren.md:58 区` | `[归纳]` | unverified | AUDIT `§D BS-§4-P3` unverified |
| LBS-M-WE-04 | 白眼是**局部几何 + 主体 gestalt 双层**（CE-2 语义反转：合规方眼 + 圆胖可爱鸟） | `AUDIT-bada_shanren/counterexample.md §CE-2`；`dossiers/bada_shanren.md:178-180`（§8.1 负向段禁 cute round eyes） | `[inference]` | unverified | AUDIT 3 反例均 `[inference]`、未渲染；本卡照记为边界，不升级 |
| LBS-M-NS-01 | **计白当黑 / 大留白**：空白≥55%（默认60–70%），白多于墨 | `dossiers/bada_shanren.md:28`（§1-1）、`:42`（§2-2 王祥北 `[研究]`） | `[研究]`+`[归纳]` | partial | AUDIT `§A BS-§1-1` partial（R4 支撑，阈值为项目量） |
| LBS-M-NS-02 | **§8.2-1**：空白≥55% 且空白区禁纹理/噪点/渐变（渗化过渡带≤2%） | `dossiers/bada_shanren.md:191`；`modules/bada_shanren.md:43 区` | `[归纳]` | unverified | AUDIT `§F BS-§8.2-1` unverified |
| LBS-M-NS-03 | **§8.2-5 悬置**：重心≥中心+5% / 距边≥8%短边 / 下方≥30%无墨 | `dossiers/bada_shanren.md:195`（§8.2-5）、`:33`（§1-6）、`:46`（§2-6） | `[归纳]` | unverified | AUDIT `§F BS-§8.2-5` unverified |
| LBS-M-NS-04 | **P1 留白率 / P6 悬置度** 三档 | `dossiers/bada_shanren.md:70-73,95-98`（§4） | `[归纳]` | unverified | AUDIT `§D BS-§4-P1/P6` unverified |
| LBS-M-NS-05 | **C-17 负空间硬轴**：本卡≥60% vs 米氏≤15%/北斋≥35%/马蒂斯≥20%；「精神场」≠平涂包围的大气留白 | `conflicts.md:272-284`（C-17）；`dossiers/bada_shanren.md:61-62`（§3-7a/7b） | `[归纳]` | supported | AUDIT `§H BS-C-17` supported（规则层判定） |
| LBS-M-NS-06 | 留白率 ≠ 材质空纸（CE-1 低幅 dither 浅灰底） | `AUDIT-bada_shanren/counterexample.md §CE-1` | `[inference]` | unverified | 未渲染；证明 §8.2-1 非充分 |
| LBS-M-SCOPE | §8.2 为**逐帧/单幅册页·立轴**判据；长卷《河上花图》豁免（CE-3） | `dossiers/bada_shanren.md:189`（§8.2 标题）、`:313-316`（§12-3）；`AUDIT-bada_shanren/counterexample.md §CE-3` | `[归纳]`/`[inference]` | unverified | 适用范围边界，非作品缺陷 |
| LBS-M-STATIC | 静态性：位移=0、无运动线/风纹、主体≤2 | `dossiers/bada_shanren.md:37`（§1-10）、`:197`（§8.2-7）、`:61`（§3-7a） | `[归纳]` | unverified | AUDIT `§F BS-§8.2-7` unverified |

<a id="db-source-line-39"></a>
## C. 严格分栏（`[自述]=0`）

| claim_id | claim (short) | locator | grade | support_status | basis |
|---|---|---|---|---|---|
| LBS-SEP-01 | **语料 22 条全为 contemporary/reported/later-reception 记录**：`grep -c '^### '`=22、`grep -c '\*\*类型\*\*'`=22；分布 `[reported speech]`×2 / `[self-written·转录]`×8 / `[contemporary record]`×9 / `[later reception]`×3 | `_corpus/bada_shanren.md:4`（类型定义）、`:9-155`（Q1–Q22）、`:159-162`（缺口） | `[实测]` | supported | 本 lane 实跑 `grep`；AUDIT `§E` 22 行审计逐条 supported/partial/conflict |
| LBS-SEP-02 | dossier §5「自述与原话（8 条）」中的 `[自述]` 全为**转录/转述**（题诗转录、尺牍经第三方转录、原画藏处未核、Q7 存疑待核），非可核实第一手创作意图自述 | `dossiers/bada_shanren.md:102-127`（§5）；`_corpus/bada_shanren.md:26,33,40,46,53,61,132,159-162` | `[史料]`/`[研究]` | supported | AUDIT `§E BS-Q3…Q10` 判 partial/conflict；corpus 类型标签照用 |
| LBS-SEP-03 | 「墨点无多泪点多」**OVERTURNED（降级）**，不作八大自述，仅 Q20 郑板桥 `[later reception]` | `dossiers/bada_shanren.md:353`（§B-4）、`:247`（§10-5）；`_corpus/bada_shanren.md:139-143,160` | `[史料]` | supported | AUDIT `RESULT.md §36` 明确「deliberately NOT written as 八大自述」；`claim_evidence_map.md §E BS-Q20` supported |
| LBS-SEP-04 | **本卡 `[自述]` 决策来源计数 = 0；`[推测]` 计数 = 0**；不写「八大觉得/想要/潜意识」 | `how-to-think.md §0/§3/§4`、[learning_path.md](learning_path.md) 抬头 + B2、`mechanism_notes.md §7` | `[实测]`(本卡产物) | supported | 决策序 7 步「为什么」列全为 `[归纳]`/`[研究]`/`[史料]`；`00-GOAL.md:9`（sha `37997101…fa81`）红线照用 |
| LBS-SEP-05 | 「孤/冷/气节」类词只作 `[研究]`/`[史料]` 层**带标签引用**，不反推作者心理 | `dossiers/bada_shanren.md:55-56`（§3-2/§3-3）、`how-to-think.md §3` | `[研究]` | supported | 与 LEARN-monet「有 `[自述]` 决策来源」形成对照；差异源于语料性质，非省略 |

<a id="db-source-line-49"></a>
## D. 来源锚点（accepted evidence / 诚实差异）

| claim_id | claim (short) | locator | grade | support_status | basis |
|---|---|---|---|---|---|
| LBS-ANCHOR-CUHK | **朱道朗 ≠ 八大山人 CUHK anchor**：何璇 DAO1213/04 PDF，繁体锚「朱道朗並非八大山人」(p.11)、「八大山人不可能是朱道朗」(p.4)；反对方王方宇1976/叶叶1982/汪世清1986,1990；郭武2018 肯定说所据为民国刊本《青云谱志》改笔 | `AUDIT-bada_shanren/claim_evidence_map.md §I BS-WEB-QINGYUN`；`review-evidence.md §2`；`raw/fetch_he.pdf` sha `0c04e30c…61636`（3503150 B）；`dossiers/bada_shanren.md:272` | `[研究]`（accepted 学术结论） | supported | reviewer pypdf 独立提取 40 页 43,778 字复核；`朱道朗`×75/`郭武`×14。简化字 grep 假阴性（review-evidence `F2`）非反证 |
| LBS-ANCHOR-CUHK-BOUND | CUHK 结论为**学界公案反对方证据链的 accepted 学术结论**，非本 lane 新证、非「已定史实」、不用于解释画面心理 | `mechanism_notes.md §3 诚实边界`、`how-to-think.md §3` | `[实测]`(口径) | supported | `review-evidence.md §9` PASS；dossier `:248` 原仅按维基简述「有争议，未展开」；A-65 加固后 `:272` 补公案 |
| LBS-ANCHOR-HUAYA | 花押应读「十有三月」（闰月符号，薛尚功/王方宇/白谦慎），非顾文彬「三月十九日」；仅见于 1694/1697/1699/1705 闰年 | `AUDIT-bada_shanren/claim_evidence_map.md §I BS-WEB-HUAYA`；`raw/fetch_sohu.html` sha `57c3c222…`；`dossiers/bada_shanren.md:276` | `[研究]`（accepted） | supported | A-65 高风险项，独立 web 佐证；作书法性符号背景，不作意图自述 |
| LBS-DISC-YEARS | **15-vs-14 年表差异**：§11.2 当前 = **14** 数据行（L284–297）；注记「14/15」之 **15** 无本地 KB 依据；`§D:389`「16 行年表」为历史账 | `dossiers/bada_shanren.md:280-297,368,389`；`AUDIT-bada_shanren/claim_evidence_map.md §G BS-§11.2-ROWS`、`RESULT.md §21,§37`、`review-evidence.md §4`；`coverage_manifest.json section_11_2_year_table_rows_current=14` | `[史料]`(14) / 差异诚实登记 | supported | reviewer 独立复点 = 14；本卡三处（`mechanism_notes.md §4`、`receipt.json unresolved[]`、本表）一致照记，**不重置、不猜** |
| LBS-DISC-HIST | 关联历史账：GOALS A-26「370 行」vs 当前 394 行；「私有补遗 5 条」vs manifest 私有 4（`:3176`）vs `_scratch/p2_bada_shanren/` 13 文件 = 不同计量口径 | `ops/GOALS.md:40,71`；`_images/manifest.md:3176`；`AUDIT-bada_shanren/claim_evidence_map.md §G BS-GOALS-A26 / BS-PRIVATE-5`、`RESULT.md §37` | `[史料]`(历史账) | partial | 记录为历史差异；60/60 回归、370 行本 lane 未复跑 |

<a id="db-source-line-59"></a>
## E. 练习/验收状态与边界

| claim_id | claim (short) | locator | grade | support_status | basis |
|---|---|---|---|---|---|
| LBS-PRACTICE | 3 阶梯练习（计白当黑 / 白眼向天 / 笔墨经济+组合边界）全部为**建议练习**，学习收益未经人评 | `learning_path.md §4/§5/§8-B1`、`mechanism_notes.md §5` | `[归纳]` | unverified | `01-AUDIT.md:273`；`human_review=not_applicable`，不写「已证实学习收益」 |
| LBS-PARAM | §4 六参数 / §8.2 七规则为**未实测 `[归纳]`**，修正权归图像/代码实验 lane | `dossiers/bada_shanren.md:252`（§10-10）、`:394`（§D）；`AUDIT-bada_shanren/counterexample.md §Summary` | `[归纳]` | unverified | 3 反例均 `[inference]`、未渲染；分母应为同批对照全部帧 |
| LBS-IMAGE | 9 张公开图**未目检**（`image_seen=0`）、外部 URL 本轮**未重访** | `AUDIT-bada_shanren/rights_review.md`、`coverage_manifest.json`、`review-evidence.md §3` | `[实测]`(状态) | supported | 作品/权利沿用现有记录，不新增、不升级 |
| LBS-CONFLICT-DRIFT | conflicts.md C-07/C-17 内 `durer.md L206/L208/L212`、`hokusai.md L188/L193`、`michelangelo.md L176`、`matisse.md L184` 为过时绝对行号 | `AUDIT-bada_shanren/RESULT.md §27-32`（报告、未修） | `[实测]`(上游) | supported | 本卡一律用规则 ID（§8.2-x / §4 Px / C-07 / C-17 / N1/N3）+ 子串定位 |
| LBS-WRITE | 本 lane 仅写 内部证据 e54f049040ea1644（未公开；来源记录由维护者保留），仓库只读、无 git、无 spawns、无凭据；`status=submitted`、`review=null` | `receipt.json allowed_write_paths/spawns_allowed/status`、`runner_receipt.json limitations` | `[实测]` | supported | 作者不自审，独立审阅由 review gate 承担 |

---

<a id="db-source-line-71"></a>
## F. 分母与口径（避免混用）

- AUDIT 底座：**81** claim 行 = 77 graded（supported 40 / partial 16 / conflict 1 / unverified 19 / not_applicable 1）+ 4 web-risk-fetch 行；语料 22 条；反例 3 个 `[inference]`；§11.2 = 14 行；9 公开图 / 4 私有。见 `AUDIT-bada_shanren/coverage_manifest.json`。
- 本 LEARN 表：**33** 行（A6 + B12 + C5 + D5 + E5 + 本说明段不计行），是**消费/映射**而非重新审计：每条回指 AUDIT 行或冻结仓库 locator，不新增史料断言。
- 两条主轴（白眼向天 / 计白当黑）、`[自述]=0`、CUHK anchor、15-vs-14 四项强调均可在 B/C/D 段逐条寻址。
- `[归纳]` = 项目推断（决策结构/参数/练习）；`[研究]`/`[史料]` = 同代与馆藏记录（带标签引用）；`[自述]`/`[推测]` = 0。**练习自查通过 ≠ 原作被证实如此 ≠ 学习收益已验证**。

> **Repair note (repair_round 1, 2026-11-15, S01 内部工作区)**: the total on this line was previously hand-written as **26** while the per-category counts on the same line already summed to 33 (A6+B12+C5+D5+E5). Machine recount `grep -c '^| LBS-' claim_evidence_map.md` = **33**, and per-section `awk` = A6 / B12 / C5 / D5 / E5 (sum 33). The defect reproduced; only the total was corrected to the machine-derived **33**. No claim rows, locator, grade, support_status, or any other content was changed. Per-category counts are preserved verbatim. Repaired in place; `receipt.json` artifact sha256 for [claim_evidence_map.md](claim_evidence_map.md) re-sealed and `repair_round` bumped 0 → 1.

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
