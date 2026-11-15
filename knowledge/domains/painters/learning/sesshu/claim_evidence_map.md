<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-sesshu；原正文 SHA-256 `eaf5c39a916b03dc15bc375b3d50603af371440076e24037209237c51cbcdbef`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-sesshu — claim → evidence map（每条论断带 locator）

> 任务 `LEARN-sesshu`（A-30） · 依赖 `AUDIT-sesshu`（**ACCEPTED**，内部证据 521852d22357ad9b（未公开；来源记录由维护者保留） status=accepted、`review.verdict=accepted`、`review-evidence.md §3` Verdict=ACCEPTED；独立 gate actor `ReviewGateAUDIT-sesshu(glm-5.3-flash)` ≠ 作者 `AuditSesshu`）。
> **口径（复用 ACCEPTED 审计的 locator 纪律，不重新审计）**：每条论断给「来源文件 + 具体行/节定位 + 证据等级 + 支持状态」。内部证据 4874f193014ae79c（未公开；来源记录由维护者保留） 为只读回源（声明基线 `f008952365a77e140cbda3f3959d43ef000f9a22`，本 lane 开工已 sha256sum 复核三件冻结输入，见 `RESULT.md §2`）；内部证据 2320ac48fc462346（未公开；来源记录由维护者保留） 为上游 ACCEPTED 产物；内部证据 98e1321e185dd894（未公开；来源记录由维护者保留） 为本 lane 生成。
> 等级沿用仓库 dossier L5 词表：`[自述]`/`[self-written]`/`[contemporary record]`/`[later record]` = 言语记录；`[史料]` = 史实/馆藏/权利/接受史；`[研究]` = 二手分析；`[归纳]` = 项目操作规则/研究者归纳；`[inference]` = 规则层推理（AUDIT §6 反例，非实测）；`[推测]` 本 lane **不使用，计数 = 0**。
> 版本列：仓库文件 = `f0089523…`；staging artifact = 本轮/上游生成（给 sha256）。`read_scope` 与 `access_status` 分开：外部 URL 本轮未重访 = `unknown`，本机文件 = `available`，原图像素目检 = 0（无 `image_seen`，AUDIT `RESULT.md:78`）。
> **行号纪律**：本表一律用**实测行号 + 子串**（dossier §2-1=L53、§3.1=L78-96、§4=L100-111、§8.2=L200-211、§12=L373-427；card §8.2=L41-52、§4=L54-65）；AUDIT 登记的 `_extract.py` sha 漂移 / near-miss 8-vs-11 / GOALS A-78 简写均**只登记、不修仓库**（见 #LS-REG-*）。

---

<a id="db-source-line-11"></a>
## A. 输入与版本（本 lane 开工复核）

| # | claim_id | 论断（短） | kind/status | 证据定位（source : locator） | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 1 | LS-INPUT-CARD | card sha = ledger `6b2de1f1…aa0dd` | fact/supported | [sesshu.md](../../modules/sesshu.md) 全文件 sha × `AUDIT-sesshu/coverage-manifest.json:6` × `RESULT.md §2` 实跑 | `[史料]`（字节实测） | 开工 sha256sum 全等 |
| 2 | LS-INPUT-DOSSIER | dossier sha = ledger `98bd600a…9db1d6` | fact/supported | [sesshu.md](../../dossiers/sesshu.md) 全文件 sha × `coverage-manifest.json:7` × `RESULT.md §2` | `[史料]` | 全等（511 行） |
| 3 | LS-INPUT-CORPUS | corpus sha = ledger `b546a021…92ac70`（17 条） | fact/supported | [sesshu.md](../../dossiers/_corpus/sesshu.md) 全文件 sha × `coverage-manifest.json:8` × `RESULT.md §2`；`grep -c '^### '`=17 | `[史料]` | 全等；17 条沿用 AUDIT 计数 |
| 4 | LS-INPUT-AUDIT-MANIFEST | 上游 `AUDIT-sesshu/coverage-manifest.json` sha = `f132eab3…531f5` | fact/supported | 内部证据 52f986b503c2f610（未公开；来源记录由维护者保留） 全文件 sha × `RESULT.md §2` × AUDIT `receipt.json` artifacts 登记值 | `[史料]`（字节实测） | RECEIPT input_hashes 第 4 项 |
| 5 | LS-INPUT-CONFLICTS | conflicts.md sha = `314a24da…bbef` | fact/supported | [conflicts.md](../../../../cross/conflicts.md) 全文件 sha × `RESULT.md §2` × AUDIT `RESULT.md:26` | `[史料]` | 全等 |
| 6 | LS-AUDIT-ACCEPTED | 上游 AUDIT-sesshu 已 ACCEPTED（独立 gate，作者不自验收） | fact/supported | 内部证据 521852d22357ad9b（未公开；来源记录由维护者保留） status=accepted / `review.verdict=accepted` / `review.reviewer_actor_id=ReviewGateAUDIT-sesshu(glm-5.3-flash)` / `review-evidence.md §3` Verdict=ACCEPTED | `[史料]`（产物） | 本 lane 不重新审计，只复用结论 |
| 7 | LS-EXTRACT-228 | card §8.1/§8.2/§4 与 dossier 逐字一致（`--check` 228/228 ok, fail=0） | fact/supported | AUDIT `RESULT.md:13` × `coverage-manifest.json:23` × 实测 `_extract.py` sha `4afa31ec…` | `[史料]`（产物） | 228/228 钉在本轮实测内容，不沿用 execution-snapshot 旧 hash |

<a id="db-source-line-23"></a>
## B. 前置知识（learning_path.md §1）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 8 | LS-K1-APPARATUS | 雪舟模块 = 构造装置（骨架→破墨空气→实景再構成→移动视点），非「日式水墨滤镜」 | observation/supported | `dossiers/sesshu.md:9,21,149`；`modules/sesshu.md:9-13` | `[归纳]`（能力定位）/ `[史料]`（影响链） | 非作者原话 |
| 9 | LS-K2-HABOKU-WHITE | 破墨 + 留白是同一机制两半：破墨工序（先淡墨立要所、趁湿点浓墨互破成面，骨架可读）+ 留白 30–60% 服务云/水/气（非空场） | observation/supported | `dossiers/sesshu.md:53,54,39,40,155,204,206`；`modules/sesshu.md:45,47` | `[史料]`（工序）/ `[归纳]`（阈值） | 本片强调①；数值非史料/非像素实测 |
| 10 | LS-K3-INTERSECTION | 40–60% 交集分工条款：雪舟留白 30–60% ∩ 八大 ≥60% = 40–60% 交集区，组合取交集并显式取值、联合 ≥2 轴 | observation/partial | `dossiers/sesshu.md:85`（边界注②）、`:84`（判据四条）、`:111`（越界警报②）、`:197`；`modules/sesshu.md:65`；AUDIT `RESULT.md:72-74`、`claim_evidence_map.md:38-41` | `[归纳]`（AUDIT 判 partial，可被组合实验推翻） | 本片强调②；反例为 [inference] 非实测 |
| 11 | LS-K4-KANO | 「狩野派 vs 水墨」轴：dossier **无**狩野派 §3.1 写死分工条款 / 专属 C 行；狩野派出现在输出/接受史（奉其为师、《本朝画史》1693、涙鼠、「雪舟作」激增） | observation/supported | `dossiers/sesshu.md:145-146,298,334`；`_corpus/sesshu.md:114,117`；AUDIT `RESULT.md:54`、`coverage-manifest.json:38`（`sesshu_named_C_rows=0`） | `[史料]`（接受史）/ `[归纳]`（学习对照轴） | 本片强调④；**不得升格为写死分工** |
| 12 | LS-K5-18PD | 18 张公开图全部 PD-Art、全 Commons、0 CC-BY/0 CC0/0 unknown-license；本 lane 未目检像素/未复核许可页 | fact/supported | AUDIT `rights_review.md:3-8,12-29`（18 行逐张）；`RESULT.md:78`；`coverage-manifest.json:35`；`dossiers/sesshu.md:7,28` | `[史料]`（权利账） | 本片强调③；`image_seen=0`、外部 unknown |
| 13 | LS-K6-PARAMS | §4 六参数 / §8.2 八规则数值全 `[归纳]`、未对原作做像素测量（分母＝假想参考帧） | fact/supported | `dossiers/sesshu.md:104-111,202-211,274`；`modules/sesshu.md:52,56-65`；AUDIT `RESULT.md:47` | `[归纳]`（性质标注） | L274 / card L52 自陈 |
| 14 | LS-K7-SELF | 作者自述层（破墨の法 / 吾祖如拙周文 / 四明天童第一座 / 六十有七歳筆受）与 `[归纳]` 严格分开 | fact/supported | `dossiers/sesshu.md:71,120,122,123`；`_corpus/sesshu.md:12,20,27,48,55`（Q1–Q3/Q6/Q7） | `[自述]` | 書き下し文 / 转引 / 汉文冒頭互证，不升级 |
| 15 | LS-K8-INTERFACE | card 只把 C-07/C-12/C-16/C-17 作组合预检接口引用（§8.2-8 另与 C-09 静场对齐），均非雪舟专属冲突 | fact/supported | `modules/sesshu.md:50,67-74`；`conflicts.md:38,40,43,47,48`；AUDIT `RESULT.md:54`、`coverage-manifest.json:37-48` | `[归纳]` / `[研究]` | 0 专属 C 行 |

<a id="db-source-line-36"></a>
## C. 重点作品及来源（learning_path.md §2）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 16 | LS-WORKS-12 | §12 共 10 件临摹/学习清单；§0 国宝 5 件；本文引用现有记录不新增作品 | fact/supported | `dossiers/sesshu.md:23-27`（§0）、`:377-425`（§12） × AUDIT `RESULT.md:32`（§0–§12 + 自审四段 511 行全文实读） | `[史料]`（作品信息）/ `[归纳]`（练习映射） | 作品与权利沿用 |
| 17 | LS-WORKS-HABOKU | 《破墨山水図》/《慧可断臂図》→ 破墨+骨架练习 | observation/supported | `dossiers/sesshu.md:377-380,397-400,155`；AUDIT `rights_review.md:12-13,20` | `[归纳]`（映射） | 练习映射归本项目 |
| 18 | LS-WORKS-WHITE | 《秋冬山水図》/《倣夏珪山水図》/《天橋立図》→ 留白+斧劈构造练习 | observation/supported | `dossiers/sesshu.md:382-390,402-405`；AUDIT `rights_review.md:14-16,23` | `[归纳]`（映射） | 同上 |
| 19 | LS-WORKS-INTERSECTION | 《倣梁楷黄初平図》→ 交集区实操；山水長巻/画本 → 长卷；雪村对照件 → 接受史 | observation/supported | `dossiers/sesshu.md:392-395,417-425`；AUDIT `rights_review.md:17-19,24,26`；`dossiers/sesshu.md:145` | `[归纳]`（映射） | 同上 |
| 20 | LS-WORKS-RIGHTS | 18 张逐张权利/来源/字节 sha256 前 16 位有记录，本 lane 未目检、未联网复核 | fact/supported | AUDIT `rights_review.md:12-29` × `RESULT.md:78` × `coverage-manifest.json:35` | `[史料]`（权利账） | 不重访外部 URL；`bishamonten.jpg` unknown 保持 unknown、国宝第 6 件《山水図》列缺口（`rights_review.md:8`） |
| 21 | LS-WORKS-ATTRIB | `portrait_sesshu_copy.jpg`（模本）/ `birds_flowers_*`（伝雪舟）/ 雪村对照件只作接受史/系谱对照，不作真笔机制证据 | observation/supported | AUDIT `rights_review.md:26-29`；`dossiers/sesshu.md:146,298` | `[史料]`（传称标记）/ `[归纳]`（对读） | 与 #LS-K4 / F8 一致 |

<a id="db-source-line-47"></a>
## D. 机制与参数（learning_path.md §3 / mechanism_notes.md §1-§5）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 22 | LS-M1-HABOKU | 破墨工序 = 先淡墨立要所、未干点浓墨互破成面（元代玉澗系潑墨在日本的实践），骨架不拆 | fact/supported | `dossiers/sesshu.md:53`（§2-1 引 [R2] 衛藤駿/玉澗）、`:54`（§2-2 [R3]）、`:155`（e国宝 [R3]） | `[史料]` | 工序有馆方/研究支撑（AUDIT `RESULT.md:21` 1–6 有馆方支撑） |
| 23 | LS-M1-SELFNAME | 「破墨」称呼来源之一 = 自序「相随ひて設色の旨と兼ねて破墨の法を伝ふ」 | fact/supported | `dossiers/sesshu.md:120`（§5-2）、`_corpus/sesshu.md:20`（Q2 `[self-written]`）；AUDIT `RESULT.md:49`（Q1–Q3 書き下し文、漢文冒頭以東文研 #3148 互证） | `[自述]` | 不写成雪舟规定了 §8.2 阈值 |
| 24 | LS-M1-RULE | §8.2-3 破墨规则：≥1 墨面区无硬轮廓（≤2/255 每像素段梯度）、区内 ≥1 浓墨结构线、洒点方差 ≤30° | fact/supported | `dossiers/sesshu.md:204`；`modules/sesshu.md:45`（原样） | `[归纳]` | 逐帧判分规则，非史料/非实测 |
| 25 | LS-M2-WHITE | §8.2-5 留白规则：纸色 ±5% 面积 30–60%、≥1 横带贯通 ≥50% 画宽、水面波纹 ≤3% | fact/supported | `dossiers/sesshu.md:206`；`modules/sesshu.md:47`；`:40`（§1-5）、`:107`（P4 默认中 35%） | `[归纳]` | 留白服务云/水，非空场 |
| 26 | LS-M2-SKELETON | §8.2-1/-2 斧劈 + 岩组：直线段 ≥60%、单段 ≤8% 画高、岩组 ≥3 层、层界纹理方向差 ≥20° | fact/supported | `dossiers/sesshu.md:202-203`；`modules/sesshu.md:43-44`；`:36-38`（§1） | `[归纳]` | [R5][R14][R17] 为 `[研究]` 支撑 |
| 27 | LS-M3-40-60-RULE | 40–60% 交集区 = §3.1 边界注② 管辖，须显式取值 + 联合 ≥2 轴（题材/空间为主） | fact/partial | `dossiers/sesshu.md:85`（逐字「取交集并显式取值」）、`:84`（判据四条）、`:86`（70/30 主导轴）、`:111`（越界警报②） | `[归纳]`（AUDIT partial） | 本片强调②；与 §8.2 管辖不同（见 #LS-M3-JURIS） |
| 28 | LS-M3-JURIS | §4→§8.2 边界注可达性弱点：只跑 §8.2 自查表、不读 §3.1 边界注 → P4=55% 与八大同帧双标准不落值 | observation/partial | AUDIT `RESULT.md:74`（登记 [inference]）；`dossiers/sesshu.md:85`、`modules/sesshu.md:52` | `[归纳]` + `[inference]`（非实测） | 交 RULE/CONFLICT lane，本片不修仓库 |
| 29 | LS-M3-COUNTEREX | AUDIT §6 强反例：构造山水 + 斧劈 + ≥100 笔 + P4=55% 仍判雪舟、不满足越界三连 → 规则文本无矛盾 | observation/partial | AUDIT `RESULT.md:73`（反例构造）、`:72`（目标规则）、`:74`（结论/弱点）；`dossiers/sesshu.md:84-85,111` | `[inference]`（规则层推理，非实验验证） | 不写「已验证」 |
| 30 | LS-M4-INK | §8.2-4 墨阶规则：4–5 带、淡墨（≤40% 降幅）≥35%、浓墨（≥70%）≤25%、无一次成型灰平涂块 | fact/supported | `dossiers/sesshu.md:205`；`modules/sesshu.md:46`；`:38`（§1-3）、`:44`（§1-9） | `[归纳]` / `[研究]`（馆方分析） | 淡彩 S ≤30%、色相 ≤2 族 |
| 31 | LS-M5-VIEW | §8.2-6 散点视点：无居中单点透视消失线、视点区 ≥2；长卷 = 时间容器 | fact/supported | `dossiers/sesshu.md:207,59,58,156`；`modules/sesshu.md:48` | `[归纳]` / `[研究]`（[R4][R17]） | 「再構成」非作者心理断言 |
| 32 | LS-PARAMS-P1P6 | §4 六参数三档（P1 默认 40% / P2 强 / P3 强 / P4 中 35% / P5 中 / P6 中强 4 级） | fact/supported | `dossiers/sesshu.md:104-111`；`modules/sesshu.md:56-65` | `[归纳]` | 默认档非史料常数 |
| 33 | LS-STATIC-C09 | §8.2-8 静场规则与 C-09 对齐「雪舟站静侧」，但 C-09 本体是梵高×维米尔条、非 sesshu 专属 | fact/supported | `modules/sesshu.md:50`；`conflicts.md:40,164`；AUDIT `coverage-manifest.json:42` | `[研究]`（文本比对）/ `[归纳]`（接口） | 不在三条静态阶梯内 |

<a id="db-source-line-64"></a>
## E. 分工条款 / 冲突接口（how-to-think.md §3 / mechanism_notes.md §4）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 34 | LS-DIV-BADA | §3.1 第一写死条款（vs 八大/徐渭）：刚健/实景 vs 减笔/冷峻 vs 爆发，判据四条 + 70/30 主导轴 + N3 轴单主 | fact/partial | `dossiers/sesshu.md:80-86`；`modules/sesshu.md:71`；AUDIT `claim_evidence_map.md:38` | `[归纳]`（partial，可被组合实验推翻） | 雪舟侧不得主张「一笔造型」 |
| 35 | LS-DIV-HOKUSAI | §3.1 第二写死条款（vs 北斋）：水墨 vs 版画、表面系统二选一（N4）、蓝轴按 C-12 | fact/partial | `dossiers/sesshu.md:87-91`；`modules/sesshu.md:72`；AUDIT `claim_evidence_map.md:39` | `[归纳]`（partial） | 北斋影响链（弱口径）≠ 风格同化（`:91`、B4 `:446`） |
| 36 | LS-DIV-OTHERS | §3.1 第二层分档（vs 齐白石/黄公望/伊藤若冲）：色彩轴归齐、皴法/空间轴单主、若冲只取水墨轨 | fact/partial | `dossiers/sesshu.md:92-95`；`modules/sesshu.md:73`；AUDIT `claim_evidence_map.md:40-41` | `[归纳]`（partial） | 横向比较入口属总路线 |
| 37 | LS-INTERFACE-C | C-07/C-12/C-16/C-17 为组合预检接口（Lane B），AUDIT 逐条回源文本一致（supported）；0 sesshu 专属 C 行 | fact/supported | `modules/sesshu.md:74`；`conflicts.md:38,43,47,48`（总表）+ `:136,203,258,272`（详节）；AUDIT `RESULT.md:54`、`coverage-manifest.json:37-46` | `[归纳]`（接口）/ `[史料]`（产物登记） | 不冒充专属冲突 |
| 38 | LS-REG-NOMISS | card L79「near-miss 8 对」 vs conflicts.md §4 现 11 编号行（#9–#11 带 2026-10-16 补） | fact/partial | `modules/sesshu.md:79`；`conflicts.md` §4；AUDIT `RESULT.md:55`、`coverage-manifest.json:47-48` | `[史料]`（漂移登记）/ `[归纳]`（口径） | 交 CONFLICT/RULE lane，本片不修仓库 |
| 39 | LS-REG-EXTRACT | `_extract.py` 实测 `4afa31ec…` vs execution-snapshot `e7e96645…`（GatesRepair 另 lane 编辑） | fact/partial | AUDIT `RESULT.md:28,56,84`；`coverage-manifest.json:24-25` | `[史料]`（漂移登记） | 228/228 钉在实测内容 |
| 40 | LS-REG-A78 | GOALS A-78 括号简写易误读；dossier B6 逐字为推翻更宽「系统首个（毛笔）水墨模块」、保留「**首个日本水墨模块**」 | fact/supported | `dossiers/sesshu.md:448`（B6）；`ops/GOALS.md:116`；AUDIT `RESULT.md:57,79-80`；`claim_evidence_map.md:79-80` | `[史料]`（逐字正本） | 按 dossier 口径，不改仓库 |
| 41 | LS-REG-B6-OVERTURN | 1 条 OVERTURNED（B6）/ 26/26 HIT / 18 张全 PD 为 A-78 已知历史 | fact/supported | AUDIT `RESULT.md:7`；`dossiers/sesshu.md:448,472-479,498` | `[史料]`（档内自陈）/ unverified（外部未逐条复演） | 26/26 HIT 为 dossier 自审自陈（AUDIT `RESULT.md:86`） |

<a id="db-source-line-77"></a>
## F. 接受史 / 权利 / 证据边界（how-to-think.md S7/S8 / mechanism_notes.md §6-§7）

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 42 | LS-KANO-HISTORY | 狩野派（江户期）奉雪舟为师；狩野永納《本朝画史》(1693) 收涙鼠传说；「雪舟作」激增 = 神格化 | fact/supported | `dossiers/sesshu.md:145-146,298,334`；`_corpus/sesshu.md:114,117`（Q14） | `[史料]`（接受史） | 本片强调④；**非画面机制证据** |
| 43 | LS-KANO-Q14 | Q14 涙鼠传说 `[later record]`「**不作史实使用**」，初出江户期、ja.wiki 明言「後年の創作という説もある」 | fact/supported | `_corpus/sesshu.md:112-117,149`；`dossiers/sesshu.md:284,300` | `[later record]`（传说）/ `[史料]`（口径） | 不得当生平史实 |
| 44 | LS-KANO-0ROWS | dossier 无狩野派 §3.1 写死分工条款 / conflicts.md 无 sesshu 专属 C 行 → 本轴是学习对照轴而非系统写死分工 | fact/supported | AUDIT `RESULT.md:54`、`coverage-manifest.json:38`（`sesshu_named_C_rows=0`）；`dossiers/sesshu.md:78-96`（§3.1 无狩野派条） | `[史料]`（产物）/ `[归纳]`（对照轴定性） | 与 #LS-K4 / #LS-REG-NOMISS 一致 |
| 45 | LS-RIGHTS-18 | 18/18 PD-Art、全 Commons、0 CC-BY/0 CC0/0 unknown-license；双份 manifest 一致；私有层 6 高清副本另计（公开侧=18 非缺陷） | fact/supported | AUDIT `rights_review.md:3-6`；`RESULT.md:78`；`coverage-manifest.json:35-36` | `[史料]`（权利账） | 本片强调③ |
| 46 | LS-RIGHTS-GAP | `bishamonten.jpg` 馆藏口径 unknown 保持 unknown；国宝第 6 件《山水図》无开放图像列缺口；许可页真实性/像素未独立复核 | fact/supported | AUDIT `rights_review.md:8`、`RESULT.md:78,86-87`；`receipt.json:unresolved[5]/[6]` | `[史料]`（缺口登记） | `image_seen=0`、`access_status=unknown` |
| 47 | LS-EXTERNAL-FETCH | AUDIT 本轮 3 条档案级联网抽检（R3 e国宝 / R10 東文研 / R17 en.wiki）HTTP 200、关键词命中；本 LEARN lane 未重访外部 URL | fact/supported | AUDIT `RESULT.md:60-68`；`coverage-manifest.json:56-93`；`rights_review.md:7` | `[史料]`（抽检产物） | 不等于 26/26 逐字回源或 Commons 18/18 许可页复核 |
| 48 | LS-SELF-AUDIT | 26/26 HIT、§11 2035 CJK / 43 行年表 / 18 来源 / §12 10 件均为 dossier 自审自陈；保持 supported(档内自陈)/unverified(外部) 分级 | fact/partial | AUDIT `RESULT.md:86`；`dossiers/sesshu.md:459-463,511` | `[史料]`（档内自陈）/ unverified（外部） | 不扩大为已独立验证 |
| 49 | LS-B2-WEAKENED | dossier 自审 B2「刚健通用于全部作品」被破墨山水図反例 WEAKENED 并加 P1 档位（档案内已有强反例） | fact/supported | `dossiers/sesshu.md:444`（B2）；AUDIT `RESULT.md:74`（复述不新增推翻） | `[史料]`（档内自审） | 本片不新增推翻 |
| 50 | LS-PRACTICE-STATUS | 三条阶梯 = 建议练习（`[归纳]`），学习收益未经人完成或评价；`human_review=not_applicable`；`[推测]`=0 | design_candidate/supported | `01-AUDIT.md:273`；`00-GOAL.md:9`；`receipt.json:human_review`；本 lane `learning_path.md §4/§8`、`how-to-think.md §5` | `[归纳]`（项目设计）/ `[史料]`（spec） | 不写「已证实学习收益」 |

<a id="db-source-line-91"></a>
## G. 回执 / 写入边界

| # | claim_id | 论断（短） | kind/status | 证据定位 | 等级 | 备注 |
|---|---|---|---|---|---|---|
| 51 | LS-RECEIPT-SUBMITTED | 本 lane `status=submitted`（非 accepted），`review=null`，独立审阅由 review gate 承担；上游 AUDIT-sesshu 才是 accepted | fact/supported | `receipt.json`（本 lane）；AUDIT `receipt.json:6`；`RESULT.md §7` | `[史料]`（产物） | author 不自我验收 |
| 52 | LS-WRITE-BOUNDARY | 仅写 内部证据 e4e037660cb54a45（未公开；来源记录由维护者保留）；仓库只读、0 git 操作、0 子代理派发、无凭据 | fact/supported | `receipt.json:allowed_write_paths` / `spawns_allowed=false`；task-registry `LEARN-sesshu.allowed_write_paths` | `[史料]`（契约） | 7 文件 = 5 内容 artifact + runner_receipt.json + receipt.json |
| 53 | LS-ARTIFACT-KINDS | `required_artifact_kinds` = result_summary / learning_path / mechanism_notes / claim_evidence_map 四者齐备；how_to_think 为模板交付物追加登记 | fact/supported | task-registry `LEARN-sesshu.required_artifact_kinds`；`RESULT.md §3`；`receipt.json:artifacts` | `[史料]`（契约） | 与 LEARN-monet 同形 |

---

<a id="db-source-line-101"></a>
## 汇总（分母 / 同一次统计 / 等级分布）

- **claim 行数**：本表共 **53** 条（A:7 / B:8 / C:6 / D:12 / E:8 / F:9 / G:3），逐条给 locator；`receipt.json:claims` 为本表的机读摘要（见 `RESULT.md §5`）。
- **支持状态分布**（本表 53 条，同一次统计，程序化重算 `grep -c`）：`supported` = **43**、`partial` = **10**，sum = 53（= 总分母 ✅）。partial 10 条 = #10（K3 交集）、#27（M3 交集规则）、#28（管辖弱点）、#29（[inference] 反例）、#34/#35/#36（§3.1 三条分工）、#38（near-miss 漂移）、#39（_extract.py 漂移）、#48（自审自陈）。`conflict`=0、`not_applicable`=0；「外部 unverified」按各行等级备注标注，不另造独立 status 值。**分子分母同一次统计**（逐行 `kind/status` 列为准，汇总不另造数）。
- **等级分布**：`[归纳]`（操作规则/判据/映射/对照轴）为主；`[史料]`（工序/权利账/接受史/产物登记）、`[自述]`（Q1–Q3/Q6/Q7 款记自序）、`[研究]`（馆方/西方分析）、`[inference]`（AUDIT §6 反例，仅 #29）、`[later record]`（Q14，仅 #43）。**`[推测]` = 0**（how-to-think.md §5 全表 0、本表 0；00-GOAL.md:9 红线）。
- **四条强调覆盖**：① 破墨+留白 = #9/#22/#23/#24/#25 + learning_path K2/M1 + mechanism_notes §3 M1；② 40–60% 交集 = #10/#27/#28/#29 + K3/M3 + how-to-think S5 + 阶梯三；③ 18 张 PD-Art = #12/#20/#45/#46 + K5 + mechanism_notes §6；④ 狩野派 vs 水墨 = #11/#42/#43/#44 + K4/M5 + how-to-think S8。均有等级 + locator + 支持状态，不靠形容词带过。
- **诚实边界**：外部 URL 本轮未重访（`access_status=unknown`）；18 图 `image_seen=0`、许可页未联网复核；规则层互斥/`[inference]` 反例 ≠ 实验验证；`submitted ≠ accepted`；本机文件 available ≠ 外部来源 available。漂移交对应 lane，本片不修仓库。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
