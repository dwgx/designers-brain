<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-wu_guanzhong；原正文 SHA-256 `050027ad13eefe6ab25c8d76e8c9abaf4bc61cc64ddd4e69fca8843347d02a1c`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-wu_guanzhong — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-wu_guanzhong` · 依赖 `AUDIT-wu_guanzhong`（**ACCEPTED**，`receipt.json` status=accepted、`review-gate-receipt.json` verdict=accepted / blocking_defects=0）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核四件冻结输入，见 `RESULT.md §2`）；内部证据 edee2f07de0827fa（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 7001a2e188254881（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库口径：`[自述]` / `[self-written]` = 作者言语记录；`[史料]` = 史实/权利/字节记录；`[研究]` = 二手研究/文本比对；`[归纳]` = 项目操作规则/研究者归纳；`[inference]` = AUDIT 反例分析推理（沿用）；`[推测]` 本 lane **不使用**（计数 0）。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` / `access_status`：本机文件 = `available` / `fulltext`|`sections`|`artifact`；外部 URL 本轮**未重访** = `unknown`（沿用 AUDIT 上游 4 次 HTTP 200，不升级）；原图像素目检 = `0`（无 `image_seen`）。
> **行号纪律**：`card:90` 与 dossier §9 写「near-miss 8 对」而 conflicts.md §4 表实为 11 行——计数漂移**报告不修**（AUDIT `RESULT.md §Conflicts.md locator drift`）。本表一律用**实测行号 + 子串**。wu_guanzhong **零专属 C-行**（`conflicts_rows_checked=0` 正确，非漏审）。（**2026-11-18 收口核验**：module L90 已按 F01 于 2026-11-16 更正为「11 对」，漂移已消除；本行保留为历史登记。）

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LW-INPUT-CARD | card sha = ledger `16ba7988…a6006785a515` | fact/supported | 内部证据 7252e35ecabb8a82（未公开；来源记录由维护者保留） × [wu_guanzhong.md](../../modules/wu_guanzhong.md) 全文件 sha × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LW-INPUT-DOSSIER | dossier sha = ledger `584c1419…debec18b40` | fact/supported | 内部证据 4f23ac8ca4fbed85（未公开；来源记录由维护者保留） × [wu_guanzhong.md](../../dossiers/wu_guanzhong.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 全等 |
| 3 | LW-INPUT-CORPUS | corpus sha = ledger `282bf7d5…e4eee283c4`（40 quotes） | fact/supported | 内部证据 706ca232d344cb33（未公开；来源记录由维护者保留） × [wu_guanzhong.md](../../dossiers/_corpus/wu_guanzhong.md) 全文件 sha × `RESULT.md §2` | `[史料]` | 40 条沿用 AUDIT `quote_audit.md` 计数 |
| 4 | LW-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-wu_guanzhong/coverage-manifest.json` sha = `b1e2ccca…68f181d4a17` | fact/supported | 内部证据 bbb396a9116f0bc6（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json` artifacts 登记值 | `[史料]`（字节实测） | RECEIPT input_hashes 第 4 项 |
| 5 | LW-INPUT-CONFLICTS | conflicts.md sha = `314a24da…bbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json` input_hashes | `[史料]` | 全等 |
| 6 | LW-AUDIT-ACCEPTED | 上游 AUDIT-wu_guanzhong 已 ACCEPTED | fact/supported | 内部证据 163baf67dc274885（未公开；来源记录由维护者保留） status=accepted × `review-gate-receipt.json` verdict=accepted / blocking_defects=0 | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 7 | LW-IMAGES-PUBLIC-0 | `images_public=0` 是事实、不是缺陷 | fact/supported | 内部证据 4f4503ca0a86a4aa（未公开；来源记录由维护者保留）（`images_public:0, images_manifest:false`） × AUDIT `rights_review.md §Verdict`、`:3198` × `coverage-manifest.json images_public=0, images_public_is_fact_not_defect=true` × `dossiers/wu_guanzhong.md:4,232` | `[史料]`（权利/字节） | 25 张私有图版权未清；本 lane 不嵌图/不重访 URL/不目检原图 |

<a id="db-source-line-23"></a>
## B. 前置知识（learning_path.md §1 / how-to-think.md §0-1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 8 | LW-K1-DUAL | 风格 = 形式抽象 × 乡土母题双约束（互锁）；只写「半抽象水墨」会丢断线禁令 | observation/supported | `dossiers/wu_guanzhong.md:0 一句话能力定位`、`:64`（§3-4）、`:81-83`（§3.1 分工）；`modules/wu_guanzhong.md:82`；`_corpus/wu_guanzhong.md:81-82` | `[归纳]`（系统定位）+ `[自述]`（风筝命题） | 非作者原话；从作品与规则归纳 |
| 9 | LW-K2-KITE | 风筝不断线 = 「作品完全断绝物象与人情联系，风筝便断了线」；参数化 P5≠0 | fact/supported | `dossiers/wu_guanzhong.md:64`（§3-4）、`:113`（§4 P5）、`:116`（用法）、`:118`（分工注）、`:226-227`（§8.1）；`_corpus/wu_guanzhong.md:81-82,87-88,93-94,100-101`（Q12/Q13/Q14/Q15） | `[自述]`（命题 Q12）+ `[归纳]`（参数化） | Q13 `[self-written·转引]` 原书页码未核、Q15 英译转引；不升级 |
| 10 | LW-K3-PARAMS | P1 80% / P2 75% / P5 60% / P6 50% 默认档 | fact/supported | `dossiers/wu_guanzhong.md:109-114`（§4 P1–P6）× `modules/wu_guanzhong.md:67-72`（逐字一致） | `[归纳]` | 各参数标 `[归纳]`；非史料/非像素实测 |
| 11 | LW-K4-KANDINSKY-4 | kandinsky 互洽 3 判据（①母题来源 ②媒介 ③抽象化动力）+ ④色彩角色（吴侧专属补轴）；A-74 互洽 holds | observation/supported | `dossiers/wu_guanzhong.md:80-84`（§3.1 四判据/越界/组合注意）；`dossiers/kandinsky.md:86-88`（vs 吴冠中 3 判据）；`modules/kandinsky.md:71`（反向分工注）、`:19-29`（§8.1 声部化）、`:55-57`（§4 P1/P3）；AUDIT `RESULT.md §Conflicts.md locator drift` | `[归纳]`（分工条款）+ `[研究]`（文本比对） | 前 3 双向互洽；④非康卡判据、是吴侧补轴，非矛盾 |
| 12 | LW-K5-SELF | 作者自述层：形式美 1979 / 风筝不断线 1983 / 遥控在手 2001 / 美比漂亮价值高 | fact/supported | `dossiers/wu_guanzhong.md:126-134`（§5-1/-2/-3/-4）、`:139-145`（§5-10/-11）；`_corpus/wu_guanzhong.md:81-104`（Q12–Q15） | `[自述]` | Q14 底本=[R3] HKMA 藏品说明；Q34「1949 信」英译摘录、中文原信未核（AUDIT `quote_audit.md` / `risk_fetches.md` partial），不引用为逐字核 |
| 13 | LW-K6-RIGHTS | images_public=0 事实 + 版权护栏（2060 前受保护、不得伪造「荼」款） | fact/supported | 内部证据 4f4503ca0a86a4aa（未公开；来源记录由维护者保留） × AUDIT `rights_review.md §Verdict`、`:3198` × `dossiers/wu_guanzhong.md:4,232` | `[史料]` | 全私有 25 张「版权未清 / unknown stays unknown」 |
| 14 | LW-K7-CONFLICTS | wu_guanzhong 零专属 C-行（`conflicts_rows_checked=0` 正确）；仅受通用 C-17/N1–N9/near-miss 表约束；「8 对」计数漂移报告不修 | fact/supported | AUDIT `coverage-manifest.json conflicts_rows_checked=0, conflicts_near_miss_drift_reported` × `RESULT.md §Conflicts.md locator drift` × `modules/wu_guanzhong.md:90` | `[归纳]`（判定）+ `[史料]`（漂移事实） | 仓库只读，不修 |

<a id="db-source-line-35"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 15 | LW-WORKS-12 | §12 共 10 件临摹/学习清单 + §0 关键 6 件；本 lane 引用现有记录、不新增作品 | fact/supported | `dossiers/wu_guanzhong.md:384`（§12 抬头）/`:385-427`（10 件）/`:20-27`（§0 关键 6 件） × AUDIT `RESULT.md §What was checked` | `[史料]`（作品信息）/ `[归纳]`（练习映射） | 作品与权利沿用 |
| 16 | LW-WORKS-L1 | 山村晴雪/扎什伦布寺/一九七四·长江 → 灰调与结构阶梯 | observation/supported | `dossiers/wu_guanzhong.md:385-395`（§12-1/-2/-3） | `[归纳]`（映射） | 练习映射归本项目 |
| 17 | LW-WORKS-L2 | 鲁迅故乡/双燕/苏州狮子林/交河故城 → 黑白块面+点线面+锚点（风筝线核心） | observation/supported | `dossiers/wu_guanzhong.md:396-411`（§12-4/-5/-6/-7） | `[归纳]`（映射） | 同上 |
| 18 | LW-WORKS-L3 | 都市之夜/补网/《朱颜未改》→ 彩点预算、油墨互译、P5 弱档极端档 | observation/supported | `dossiers/wu_guanzhong.md:412-421`（§12-8/-9/-10）；`:130-134,227`（《朱颜未改》）；`_corpus/wu_guanzhong.md:93-98`（Q14） | `[归纳]`（映射） | 《朱颜未改》2001 HKMA 藏 |
| 19 | LW-WORKS-RIGHTS | 作品与权利信息沿用 §9/§12 与 `_images/manifest.md`；外部来源本轮未重访 | fact/supported | `dossiers/wu_guanzhong.md:256-297`（§9）、`:380-383`（§11.3）；`_images/manifest.md:3198` × AUDIT `coverage-manifest.json external_fetch_count=4` | `[史料]` | 本轮 `access_status=unknown`（未重取） |

<a id="db-source-line-45"></a>
## D. 机制与练习（learning_path.md §3-5 / mechanism_notes.md §1-3 / how-to-think.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 20 | LW-M1-MECH | 形式抽象×乡土母题互锁：P1 80%+P2 75%+P5 60%，§8.2-1/-3/-7 可判定 | fact/supported | `dossiers/wu_guanzhong.md:109-118`（§4）、`:226-228`（§8.1）、`:52-59`（§8.2）；`modules/wu_guanzhong.md:52-59,67-76`；`_corpus/wu_guanzhong.md:81-82,93-94` | `[归纳]`（阈值）+ `[自述]`（命题） | 阈值未经渲染校准 |
| 21 | LW-M2-MECH | kandinsky 四判据互洽；冲突轴=母题残留度/色彩角色二选一（N3），同屏显式分区 | fact/supported | `dossiers/wu_guanzhong.md:80-84`（§3.1）、`:118`（分工注）、`:228,231`（§8.1 越界/组合）；`modules/wu_guanzhong.md:82`；`dossiers/kandinsky.md:86-88`；`modules/kandinsky.md:19-29,71`；AUDIT `RESULT.md §Conflicts.md locator drift` | `[归纳]` | 不得同屏双开（N9） |
| 22 | LW-M3-TENSION | 《朱颜未改》P5-弱档反例张力：身份门（P1+P2≥中档）vs P5 弱档 in-domain，AUDIT 判 counterexample found（internal inconsistency） | observation/supported | `dossiers/wu_guanzhong.md:113,116,117,227`（§4 P5/用法/§8.1 近抽象档）、`:130-134`（§5-3/-4）；`_corpus/wu_guanzhong.md:93-98`（Q14）；AUDIT `counterexample.md` Attempt 1、`RESULT.md §Deliverables / §Unresolved #1` | `[归纳]`（规则）+ `[自述]`（Q14）+ `[inference]`（AUDIT） | **carried 不抹平、不升级、不伪造渲染验证**；结论=待 E 系列 |
| 23 | LW-M3-ATTEMPT2 | Attempt 2：P5=0 + P1 strong 落入未分类边界洞；Attempt 3：§8.1 `--no` 比 §4 分工注更严（措辞漂移） | observation/supported | AUDIT `counterexample.md` Attempt 2 / Attempt 3 / Summary 表 | `[inference]`（沿用） | 均 `[inference]`，非渲染验证 |
| 24 | LW-M4-MECH | 彩点预算 P6 / 线自主性 P4 / §8.2-2/-4/-6 失败条件 | fact/supported | `dossiers/wu_guanzhong.md:112,114`（§4 P4/P6）、`:53-58`（§8.2-2/-4/-5/-6/-7）、`:227`（档位切换） | `[归纳]` | |
| 25 | LW-LADDER-3 | 三阶梯练习（灰调结构→点线面+风筝线→近抽象档+彩点+反例登记），全部标「建议练习」，不声称学习收益 | design_candidate/supported | 内部证据 7fb982435df9ed69（未公开；来源记录由维护者保留） × `01-AUDIT.md:273`（建议练习口径）× `dossiers/wu_guanzhong.md:385-427`（§12 怎么练） | `[归纳]`（本 lane 设计） | `human_review=not_applicable` |
| 26 | LW-HTHINK-0GUESS | How to Think 严格分栏：`[自述]`/`[归纳]` 不混写一句；`[推测]`=0；无从画面推作者心理 | validated_rule/supported | `00-GOAL.md:9` × `02-EXECUTION-PLAN.md:66` × `03-RESEARCH-AGENDA.md:14` × 内部证据 624ee330d77b4b52（未公开；来源记录由维护者保留） | `[归纳]`（契约） | A-30 红线 |

<a id="db-source-line-57"></a>
## E. 失败、下一步、边界（learning_path.md §6-8）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 27 | LW-F1-F7 | 七类常见失败：P5=0 / 同屏双开 / 抹平反例张力 / 等级混淆 / 彩点越界 / 锚点写实化 / 回源与版权 | observation/supported | 内部证据 70ea80094ac16534（未公开；来源记录由维护者保留） × `dossiers/wu_guanzhong.md:113-118,226-232` × AUDIT `counterexample.md` × `rights_review.md` | `[归纳]` | |
| 28 | LW-NEXTLANE | 总路线负责跨艺术家比较（kandinsky/八大/黄公望/林风眠/马蒂斯）；STYLE lane 负责 `card_has_81b=false` 缺节 | observation/supported | `01-AUDIT.md:269-273`（§8.1 总路线）× `dossiers/wu_guanzhong.md:85-99`（§3.1 其余分工）× 内部证据 42471df28a60bfea（未公开；来源记录由维护者保留）（`card_has_81b=false`）× `task-registry.json`（STYLE-wu_guanzhong） | `[归纳]` | 本单片不单独交付总路线 |
| 29 | LW-UNVERIFIED | §4/§8.2 阈值 `[归纳]` 未实测；同屏分区方案待 E 系列；1991 毁画 `[转述]`、原刊期号/1949 信中文原信/书籍版次 UNVERIFIED —— 沿用 AUDIT 不升级 | observation/supported | `dossiers/wu_guanzhong.md:117,298-313`（§10-12）× AUDIT `RESULT.md §Unresolved #1-5` × `quote_audit.md`（12 转引/转述 partial、Q40 毁画一级来源未核） | `[归纳]`/ `[史料]`（部分） | `unresolved` 登记，不伪造成功值 |
| 30 | LW-DRIFT | `card:90` 与 dossier §9「near-miss 8 对」vs conflicts.md §4 表 11 行 = 计数漂移，报告不修 | fact/supported | `modules/wu_guanzhong.md:90` × `conflicts.md:347-357`（11 行） × AUDIT `RESULT.md §Conflicts.md locator drift` / `coverage-manifest.json conflicts_near_miss_drift_reported` | `[史料]`（漂移事实） | 仓库只读 |

---

<a id="db-source-line-68"></a>
## F. 等级 / 支持状态汇总

| 维度 | 计数 |
|---|---|
| claims_total | 30 |
| support_status：supported / partial / unverified / conflict / not_applicable | 30 / 0 / 0 / 0 / 0（本表只登记有本机/上游产物支撑的论断；未决项以 `unresolved` 形式进 `receipt.json`，不混入 claim 表） |
| `[推测]` | **0** |
| kind：fact / observation / design_candidate / validated_rule | 18 / 10 / 1 / 1（合计 30；见上表逐行 kind） |
| 外部 URL 本轮 `access_status` | `unknown`（未重访；上游 AUDIT 4 次 HTTP 200 沿用，不升级） |
| 本机文件 `access_status` | `available`（`fulltext` / `sections` / `artifact`） |

> **诚实声明**：本表验证的是「论断↔locator↔等级」的可追溯性，**不证明**来源真实性、作者身份、模型是否真的看图、或学习效果（`verify-receipt.py` 自述范围）。`status=submitted` ≠ `accepted`；独立审阅由 review gate 承担，author 不自我验收。上游 AUDIT 的 95 条 claim 与 40 条 corpus quote 由 `AUDIT-wu_guanzhong/claim_evidence_map.md` / `.csv` / `quote_audit.md` 负责，本表不重复计数、不重新审计。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
