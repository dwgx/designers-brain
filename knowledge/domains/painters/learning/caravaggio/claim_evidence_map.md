<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-caravaggio；原正文 SHA-256 `70e8db2c6bce825cb36c9603247d7539fa7d990e285eb8c2f0c771dea513c5d8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-caravaggio — 论断→证据定位图（claim_evidence_map）

> 任务 `LEARN-caravaggio` ｜ 仓库只读 @ `f008952365a77e140cbda3f3959d43ef000f9a22`。
> 覆盖对象：[learning_path.md](learning_path.md)（LP）、[how-to-think.md](how-to-think.md)（HT）、[mechanism_notes.md](mechanism_notes.md)（MN）三份产物里的**每一条实质论断**。
> **复用 `AUDIT-caravaggio`（ACCEPTED）的 locator 纪律，不重审、不新增史实考证、不改仓库。**
> 证据分级沿用档案 `:5`：`[史料]`/`[研究]`/`[归纳]`/`[推测]`/`[自述]`。§4/§8.2 阈值一律 `[归纳]` 未实测（`:222`、`:503`）。

<a id="db-source-line-8"></a>
## 0. 源文件缩写与 sha256（开工已核对，全部匹配 ledger `artist-shards.json`）

| 缩写 | 路径（相对 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留）） | sha256 | 版本 |
|---|---|---|---|
| **DOSSIER** | [caravaggio.md](../../dossiers/caravaggio.md) | `64bedbc40c1f36ed250bcbf79716e7cbca9dc4bae649ef9dc13c5cbba1a0ab76` | `f008952…` |
| **CARD** | [caravaggio.md](../../modules/caravaggio.md) | `2d511d4aaaa63d0492e4963d2bb812f1c6a577d374f77a4ce479a256c8db4262` | 同上 |
| **CORPUS** | [caravaggio.md](../../dossiers/_corpus/caravaggio.md) | `ffea54b0e6314b0f7d08492c0c310428407bf773fa7dec277a32ff837c1331f3` | 同上 |
| **CONFLICTS** | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 同上 |
| **AUDIT-CM** | 内部证据 50ee800818dbb93a（未公开；来源记录由维护者保留） | `efd62d7f1afeaeb24d136d5561fa2ccb1517fd44db247e9cf87b5797c853879f` | ACCEPTED |

> locator 写作 `文件:行号`，行号均为**冻结 head 实测值**（本轮 `grep -n` / `read` 核对）。
> **漂移注记**：AUDIT RESULT §5.3 + AUDIT-CM `conflicts_crossref_drift` 记录 CONFLICTS 引用 caravaggio.md 的 L76/L213… 比冻结 head 少 1（实际 P1 `:77`、§8.2 `:214-220`）。本图引用 caravaggio.md **一律用冻结实测行号**，不抄 CONFLICTS 内旧 L 号。

---

<a id="db-source-line-23"></a>
## 1. 身份 / 口径类论断

| # | 论断（出现在） | 证据级 | locator |
|---|---|---|---|
| C1 | 卡拉瓦乔几乎无文字留世、无画论；Graham-Dixon「关于绘画只有一句话」 | `[研究]`/`[史料]` | DOSSIER `:7`, `:127`, `:132`; CORPUS `:6`, `:178`; AUDIT RESULT §4.4 |
| C2 | `[自述]` 为空集；唯一法庭证词是贬损 Baglione 的敌意语境、非画论 | `[史料]` | DOSSIER `:91-95`; CORPUS `:18-23`, `:25-31` |
| C3 | §1–§8 的操作规则是「从作品归纳」，不冒充艺术家内心 | 项目口径 | DOSSIER `:69`, `:132`, `:503` |
| C4 | P1 强档 + P3 双峰是本模块专属；降中档/允许面部连续衰减 → 伦勃朗地盘；判据 `[归纳]` 可被实验推翻 | `[归纳]` | DOSSIER `:84`; CARD `:83` |
| C5 | §4/§8.2 量化阈值 `[归纳]` 未对原作像素测量 | `[归纳]` | DOSSIER `:222`, `:503`; CARD `:70`; AUDIT RESULT §5.7, §7 |
| C6 | 练习为「建议练习」、未经真人学习效果验证（本 LEARN 自行标注，不来自仓库） | LEARN 口径 | [learning_path.md](learning_path.md) §0/§4; [how-to-think.md](how-to-think.md) §0; [mechanism_notes.md](mechanism_notes.md) §0 |

---

<a id="db-source-line-36"></a>
## 2. §4 参数类论断（LP §3、MN §1、HT 决策序）

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C7 | P1 弱/中/强三档 = 柔和多光 / 单方向略软 / **单一硬光（画外高置 30°–60°、无反射、边界硬）**；默认 **85% 强档即身份** | `[归纳]` | DOSSIER `:77`; CARD `:76` |
| C8 | P2 背景明度上限 40–50% / ≤20% / ≤8–10%；默认 10% | `[归纳]` | DOSSIER `:78`; CARD `:77` |
| C9 | P3 中间调 全调域 / 25–40% / ≤25% 双峰+暗带≥40%；默认 30%（比强档松一档） | `[归纳]` | DOSSIER `:79`; CARD `:78` |
| C10 | P4 贴平面度 纵深 / 半身 / 主体≥80%高+裁切+越出；默认 80% | `[归纳]` | DOSSIER `:80`; CARD `:79` |
| C11 | P5 色域收窄 多色 / 土色+1–2强调 / 近单色阶；60%（罗马期）/ 晚期 85% | `[归纳]` | DOSSIER `:81`; CARD `:80` |
| C12 | P6 手势—光斑绑定 全身均匀 / 脸优先 / **光斑只落脸·手·道具、连通域 ≤5**；默认 85% | `[归纳]` | DOSSIER `:82`; CARD `:81` |
| C13 | 用法：P1/P2 定身份、P4/P6 定叙事、P3/P5 定时期 | `[归纳]` | DOSSIER `:85`; CARD `:84` |

---

<a id="db-source-line-50"></a>
## 3. §8.2 规则类论断（LP §3/§5、MN §2、HT 步 1–5）

| # | 规则 | locator（DOSSIER §8.2 / CARD §8.2） |
|---|---|---|
| C14 | §8.2-1 光源单一性：可见光源 = 0、方向左上/右上 (±0.7,−0.7)、环境光 ≤ 主光 5% | DOSSIER `:214`; CARD `:62` |
| C15 | §8.2-2 背景明度上限：≤0.10×max、标准差 ≤全帧 5%（禁光晕渐变） | DOSSIER `:215`; CARD `:63` |
| C16 | §8.2-3 中间调压缩双峰：中间带 [0.35,0.65] ≤25%、暗带 [0,0.25) ≥40%（强档），中档 ≥25%/≤40% | DOSSIER `:216`; CARD `:64` |
| C17 | §8.2-4 光斑三处法则 `[2,5]`：连通域 ≥0.9×max、数量 ∈[2,5]、每域相交脸/手/道具、背部 = 0 | DOSSIER `:217`; CARD `:65` |
| C18 | §8.2-5 贴平面：主体包围盒 ≥80% 高、被裁切、地平线 ≤下缘以上 15% | DOSSIER `:218`; CARD `:66` |
| C19 | §8.2-6 定格：1 个动作极值、运动模糊核 = 0、手势 ±15° 指向叙事对象 | DOSSIER `:219`; CARD `:67` |
| C20 | §8.2-7 暗部保细节：暗区(<0.15)标准差 ≥1.5/255、纯黑 ≤10% | DOSSIER `:220`; CARD `:68` |
| C21 | §8.2-3 与 §8.2-7 一体两面（压中间调但暗部非死黑） | DOSSIER `:32`, `:39`, `:209`, `:220`; AUDIT counterexample break 2 |

---

<a id="db-source-line-65"></a>
## 4. 史料 / 视觉指纹 / 技法锚点（HT 各步「为什么」、LP §1、MN）

| # | 论断 | 证据级 | locator |
|---|---|---|---|
| C22 | 同代批评家（Met 转引）：「高置聚焦光、无反射、暗室黑墙」「不自然」—— P1/P2 直接史料依据 | `[史料]` | DOSSIER `:121-125` (§5-7); CORPUS `:154-159` (#20) |
| C23 | Mancini《Considerazioni》「lume unito … d'alto senza reflessi … pariete colorite di negro」 | `[史料]` | CORPUS `:88-93` (#11) |
| C24 | Bellori 1672「暗室高灯、光直落、只揭示身体主要部分」 | `[史料]` | DOSSIER `:102-105` (§5-3); CORPUS `:110-115` (#14) |
| C25 | 两级明暗（tenebrism）「shift from light to dark with little intermediate value」、黑暗成主体 | `[研究]` | DOSSIER `:31` |
| C26 | 暗部不是死黑：NG「dark ground left deliberately exposed … to provide the mid-tone in the shadows」 | `[研究]` | DOSSIER `:32`, `:39` |
| C27 | 人物贴住画面平面：Met「pushed the figures up against the picture plane」 | `[研究]` | DOSSIER `:33` |
| C28 | 手势是叙事主语、手被光点亮 | `[归纳]` | DOSSIER `:34` |
| C29 | 反理想化人体/面孔、当代服装+当代空间 | `[史料]` | DOSSIER `:35`, `:36` |
| C30 | 定格瞬间「the passing of a crucial moment」「the moment of revelation」 | `[研究]` | DOSSIER `:37` |
| C31 | 色域收窄「restricted range of colour」、深色底 | `[研究]` | DOSSIER `:38`, `:39` |
| C32 | 直接画法「not a single drawing … survives」；abbozzo / incisions；dal naturale 真人写生 | `[研究]` | DOSSIER `:45`, `:46`, `:47`, `:49` |
| C33 | 直接画 ≠ 无准备（NG「carefully composed / high degree of preparation」、少 pentimenti） | `[研究]` | DOSSIER `:53`; AUDIT RESULT §4.2 (RF-2) |
| C34 | 创作原则「先定光位→再定亮部三对象→最后压暗背景」操作序列 | `[归纳]`（含 `[史料]` 锚 :61） | DOSSIER `:61`, `:69` |
| C35 | 物理真实压倒象征程式、反理想化是立场不是疏忽、叙事只取一瞬 | `[研究]`/`[归纳]` | DOSSIER `:62`, `:63`, `:64`, `:65` |
| C36 | §8.1 正向段（土色、脸手受光、贴平面裁切、定格）与负向段（禁柔光/多光源/光晕/motion blur/mirror/candles/halo/crowd） | `[归纳]` | DOSSIER `:184-204`; CARD `:19-40` |
| C37 | 退化修复提示：普通暗调照片→加 `single unseen lamp…`；死黑剪影→加 `dark brown ground visible in the half-tones` | `[归纳]` | DOSSIER `:209` |

---

<a id="db-source-line-88"></a>
## 5. 作品 / 练习来源（LP §2、LP §4、MN §1）

| # | 论断 | locator |
|---|---|---|
| C38 | 关键作品 5 件（含馆藏/URL 编号 R5/R8/R9/R10/R1） | DOSSIER `:17-22` |
| C39 | §12 临摹清单 9 件、建议顺序「单光源静物→叙事装置→巨幅黑暗→晚期极简」 | DOSSIER `:378-426`, 顺序 `:381` |
| C40 | 《捧果篮的男孩》看/学/练（含「摆真实水果+单硬光拍照」「只画明暗两大区」「加一只手」「§8.2-4/-2 自查」） | DOSSIER `:383-386` |
| C41 | 《圣马太蒙召》「光选人」分镜、5 人视线链、只画 3 个亮块、§8.2-4 自查 | DOSSIER `:388-391` |
| C42 | 《以马忤斯的晚餐》abbozzo/incisions、手—面包—酒杯三角、30 分钟直接定形、§8.2-3/-7 自查 | DOSSIER `:393-396` |
| C43 | 《基督下葬》群像压缩、手势合力、裁切检查、质感两级对比 | DOSSIER `:398-401` |
| C44 | 《大卫》限三色临摹、只照两物缩略图 6 张、§4-P5 自查 | DOSSIER `:408-411` |
| C45 | 《施洗者圣约翰被斩首》暗面 ≥60%、可见光源 = 0、光斑三部位 | DOSSIER `:413-416` |
| C46 | 《七件善事》七行分镜压一格、每件至少一只可辨的手+光斑覆盖 | DOSSIER `:418-421` |
| C47 | 《圣乌尔苏拉殉道》只 3 个高光连通域 | DOSSIER `:423-426` |
| C48 | 3 张公开图（bacchus / calling_of_saint_matthew / judith_beheading_holofernes，manifest :44-46） | AUDIT-CM `image_files`; `_images/manifest.md:44-46` |
| C49 | §8.1b 纯风格段存在（`card_has_81b: true`） | AUDIT-CM `card_has_81b`; CARD `:42-58` |

---

<a id="db-source-line-107"></a>
## 6. 冲突条目（LP §6、MN §3、HT「何时失效」）

| # | 冲突 | locator（CONFLICTS 冻结实测） | 关联模块断言 locator |
|---|---|---|---|
| C50 | C-01 硬阴影：Lane B 反约束 × 卡拉瓦乔 P1 强档 / §8.2-1 | `CONFLICTS:55` | DOSSIER `:77`, `:214`, `:228`; CARD `:90` |
| C51 | C-03 直方图：达·芬奇中间调 ≥55% × 卡拉瓦乔 ≤25%+暗带≥40% | `CONFLICTS:84` | DOSSIER `:79`, `:210`, `:216`; CARD `:91` |
| C52 | C-04 直方图单桶上限：塞尚「无单桶 >20%」× 暗带≥40%+背景均匀 | `CONFLICTS:97` | DOSSIER `:215`, `:216`; CARD `:92` |
| C53 | C-11 高光计数：`[2,5]` × 维米尔 100+ 点 | `CONFLICTS:188` | DOSSIER `:217`; CARD `:94` |
| C54 | C-12 色相面积预算：北斋蓝≥40% × 土色收窄 × 梵高互补 1:1 | `CONFLICTS:203` | DOSSIER `:81`, `:194-195`; CARD `:95` |
| C55 | C-13 阴影色相：塞尚阴影蓝≥15% × 深棕黑暗部 | `CONFLICTS:217` | DOSSIER `:32`, `:81`, `:220`; CARD `:96` |
| C56 | C-08 运动模糊（边界注记，不计入点名 6 条） | `CONFLICTS:149` | CARD `:93` |
| C57 | 6 条行号与 AUDIT 一致；CONFLICTS 对 caravaggio.md 行号 +1 漂移 | AUDIT RESULT §3(`:36`), §5.3; AUDIT-CM `conflict_rows`, `conflicts_crossref_drift` | — |
| C58 | 各 C 行的处置立场（显式覆盖 / 二选一 / 作用域改写 / 分类计数 / 预算表 / 分区掩膜） | `CONFLICTS:55`, `:84`, `:97`, `:188`, `:203`, `:217` 各「组合时怎么解」段 | MN §3 表 |

---

<a id="db-source-line-123"></a>
## 7. 计数与一致性（可复算）

| 项 | 值 | 复算命令 / 来源 |
|---|---|---|
| 本图论断条数 | **58**（C1–C58） | 本文件表格行计数 |
| 覆盖的产物 | 3（LP / HT / MN） | 内部证据 18a3a4a988b2fe1c（未公开；来源记录由维护者保留） |
| 点名冲突条数 | **6**（C-01/03/04/11/12/13） | `grep -nE '^### C-(01\|03\|04\|11\|12\|13)' conflicts.md` → :55/:84/:97/:188/:203/:217 |
| 输入 sha 全部匹配 ledger | 3/3 | 本轮 `sha256sum` 开工核对；AUDIT RESULT §2 |
| §4 参数 / §8.2 规则 | 6 / 7 | DOSSIER `:77-82` / `:214-220` |
| corpus 语料条数 | 22 | AUDIT-CM `quote_count`; `grep -c '^### ' _corpus/caravaggio.md` |
| 练习阶梯数 | 3（L1/L2/L3），每级 ≥4 步 | [learning_path.md](learning_path.md) §4 |

> **未在本图出现的仓库事实一律未写入三份产物**：例如生卒年、死亡原因、2007 受洗档案、墓志铭年龄、图库权利标签——这些属 AUDIT 证据域，本 LEARN 不引用、不重审。
> **本图不主张**：不主张任何练习已验证、不主张组合已通过、不主张 §4/§8.2 阈值是原作实测、不主张 `[自述]` 非空。

---

<a id="db-source-line-140"></a>
## 8. 使用边界

- 本图是**定位索引**，不替代源文本；引用请回读对应 `文件:行号`。
- 证据级沿用档案 `:5`；CONFLICTS 内 caravaggio.md 旧 L 号不采用（见 §0 漂移注记）。
- 处置权归集成/实验 lane；本 LEARN 仅记录失败条件与摘录立场，无 repo 写入、无子代理、无联网、无凭据。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
