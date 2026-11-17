<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-holbein；原正文 SHA-256 `e0deb4cff61109e685f248403b8ccd7bc0aacc2394d548486fedb1256cc6db66`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-holbein — claim_evidence_map（五类来源定位索引）

> Campaign `Designers-Brain-Upgrade-20261115` / TASK_ID `LEARN-holbein` / lane `learning`。
> **证据底本:** 内部证据 c4717bb05ac27410（未公开；来源记录由维护者保留）（**ACCEPTED**）。Repo 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22`（READ-ONLY；本 lane 0 repo 写、0 subagent spawns、0 credentials、0 外部重抓）。
> **本文件用途:** 把 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) / `RESULT.md` 的每条主张映射到 **dossier / corpus / card / conflicts / AUDIT** 五类来源的 `节:行` 定位 + 证据级 + support_status。**不复制 AUDIT 产物、不重审、不改源**。
> **grade 沿用** dossier §0 / AUDIT claim map 卷首 L6：`[自述]` 本人手笔（画内文字/遗嘱）｜`[史料]` 同时代记录/档案/馆藏｜`[研究]` 艺术史家/博物馆/学术｜`[归纳]` 本项目操作规则｜`[推测]` 低置信｜`[inference]` 反例推演。
> **support_status ∈ {supported, partial, conflict, unverified}**；known-open 一律 explicit 携带、不关闭。

---

<a id="db-source-line-11"></a>
## 0. 来源清单与锚（本 shard 读过的输入）

| 类别 | 路径 | sha256（本机实测） | read_scope |
|---|---|---|---|
| dossier | [holbein.md](../../dossiers/holbein.md) | `070cb50f570fbacd4646e3d0850cedec150bf9497a308c96b8f981b68b039aed` | fulltext（503 行） |
| corpus | [holbein.md](../../dossiers/_corpus/holbein.md) | `f7ae535678b36715c4251b1881731e8fb3eb085a91978ade6d0943533059df5e` | fulltext（243 行，26 条 Q1–Q26） |
| card | [holbein.md](../../modules/holbein.md) | `c175d2bfca1ace0ba5e9e48e6c0b190af713ab2ecb268feae3dc4252fbb61a83` | fulltext（91 行） |
| conflicts | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | sections（§1/§2/§3/§4/§C） |
| AUDIT RESULT | 内部证据 0a10f88f59855367（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | fulltext |
| AUDIT claim map | 内部证据 be11318559216d9f（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | fulltext（§A–§H） |
| AUDIT coverage | 内部证据 5cc715d9305319c3（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | metadata |
| AUDIT rights | 内部证据 4a9fdf1ecb3ea8b6（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | fulltext（13 行） |
| AUDIT counterexample | 内部证据 3151350c5955afba（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | fulltext（3 反例） |
| AUDIT review | 内部证据 04a5a36a9b8a66a2（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | fulltext（verdict accepted） |
| ledger | 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） | 见 receipt.json `input_hashes` | metadata |
| 抓取原文（AUDIT 已锚定，本 shard 只读） | `ngl_ambassadors.html` `19a66af15497…` / `hervey1900.txt` `f7734f75e602…` / `wiki_holbein3.html` `f5f856124577…` / `ngl_erasmus.html` `efa3efacb188…` / `chamberlain1.txt` `92f2cb480215…` / `chamberlain2_raw.txt` `62bcfbaa4c4e…` | 见 coverage-manifest.json | 逐字命中片段 |

> AUDIT 已接受状态：内部证据 152f099a4d351899（未公开；来源记录由维护者保留） status=accepted / review.verdict=accepted / author=AuditHolbein；`review-gate-receipt.json` verdict=accepted（reviewer ReviewGateAuditHES，glm-5.3-flash，independent）；`review-evidence.md` §8「0 blocking / 0 non-blocking」。本 shard 作为依赖复用，不自接受。

---

<a id="db-source-line-32"></a>
## 1. 北方文艺复兴肖像精工 + 织物质感（本次点名重点）

| claim_id | 主张 | 定位（dossier / card / AUDIT） | grade | status |
|---|---|---|---|---|
| LH-TEXTURE-1 | 「物证级细节 + 织物质感」= ≥3 类材质各自高光签名、每类 ≥5%（缎/毛/金/玻璃/纸） | dossier §1-1 L34；§8.2-3 L209；§2-3 L51（R13 Ganz「deep glaze and enamel-like lustre」）；card §8.2-3；AUDIT S1-1（NGL「a supreme display … to recreate a variety of textures」R1 + Foister「minutely rendered clothing」R15，risk-fetch NGL 页 sha 19a66a… 逐字命中） | `[史料]`+`[归纳]`（阈值） | supported |
| LH-TEXTURE-2 | 净面工艺：无排线/无笔触、薄层罩染、珐琅光泽，明暗交给罩染过渡 | dossier §1-2 L35；§8.2-1 L207；§2-3 L51；card §8.2-1；AUDIT S1-2 / S2-3（hatching=0 / <2px 为 `[归纳]` 未实测） | `[史料]`+`[归纳]` | supported |
| LH-TEXTURE-3 | 精工 = 物证装置（写生→几何转写→罩染交付材质→铭文/物品编码→隐藏机械装置），不是高清滤镜 | dossier §6.2 L142（一句话来历）；§2-1/2/3 L49-51；§12 组合建议 L421；AUDIT S2-1/2（Strong「everything began with a drawing」、Ganz「transferred … with geometrical instruments」） | `[史料]`（工艺）+`[归纳]`（装置框架） | supported |
| LH-TEXTURE-4 | 金流苏 mordant gilding（油媒染 + 金箔）逐件可数 | dossier §2-5 L53（R1 逐句）；AUDIT S2-5（risk-fetch NGL 页「oil mordant … gold leaf」verbatim） | `[史料]` | supported |
| LH-TEXTURE-5 | 「手=第二面孔」手部密度 ×0.8 | dossier §1-5 L38；AUDIT S1-5 | `[归纳]` | **partial**（仅对照图版归纳，无馆方/文献级直引；AUDIT 判 partial） |
| LH-TEXTURE-6 | §4 P1 物证级细节密度三档 / 默认 70% | dossier §4 L95；card §4 P1；AUDIT S4-P1 | `[归纳]` | **partial**（项目设定、未像素实测，dossier §10-6 L270） |

---

<a id="db-source-line-45"></a>
## 2. 分工条款（写死）+ 失败条件

| claim_id | 主张 | 定位（dossier / card / conflicts） | grade | status |
|---|---|---|---|---|
| LH-DIV-DURER | vs 丢勒 = 线的密度/版画线网 vs 材质的物证/罩染净面；4 判据 + 「≥2 轴联合成立」边界注 | dossier §3.1 L76-82（第一写死条款）；卷首 L8；卡「冲突注记」；AUDIT S3-3.1 | `[归纳]`（口径级写死） | **partial**（B1 WEAKENED：丢勒也画油画肖像、荷尔拜因也做版画；边界注已补、未做组合实验实测） |
| LH-DIV-REMBRANDT | vs 伦勃朗 = 客观物证/信息照明/情绪画外 vs 内心光/情感照明/情绪画内 | dossier §3.1 L83-89（第二写死条款）；卷首 L8；AUDIT S3-3.1 | `[归纳]` | **partial**（B2 WEAKENED：Woltmann 读出内心；判定以「心理是否被画内光/笔触承载」为准） |
| LH-CONFLICT-ROWS | holbein 在 conflicts.md **无专属 C-row**（grep Holbein/荷尔拜因 0 命中）；仅预检指针引用通用 C-01(L55)/C-05(L109)/C-12(L203)；§4 near-miss 11 对无 holbein | conflicts.md L55 / L109 / L203 / §4 L345-357；dossier §3.1 L90；卡 L85；AUDIT §9 / X-CONFLICTS | `[归纳]` | **partial**（无专属行是事实非缺陷；通用行行号 stale 见 §3） |
| LH-OVERRUN | §4 六条越界警报（排线→丢勒 / 硬切→卡拉瓦乔 / 厚涂→伦勃朗梵高 / 拉长→格列柯 / 装饰金平面→克里姆特 / 高彩度→梵高） | dossier §4 L102；card §4 用法；conflicts.md C-01/C-05/C-12 | `[归纳]` | supported（规则文本内部一致；作用域为生成帧自查、非原作像素声称） |
| LH-DRIFT-C | 通用 C-row 的 `(dossier.md L<行号>)` 普遍 stale（11 处：michelangelo+1 / caravaggio+1,+1 / da_vinci+1,+1 / van_gogh+2 / monet L200→L33 / cezanne+1 / matisse+6 / picasso+5 / durer+2） | conflicts.md §C L384-386（自承曾修 4 处）；AUDIT §G 实测表 / RESULT §9 / coverage-manifest.json.locator_drift_reported；review-evidence.md §2/§7 | `[归纳]` | **partial**（记录漂移，报告不修；本 shard 不改 repo） |

---

<a id="db-source-line-57"></a>
## 3. X-AGES 双说（本次点名，conflict 携带）

| claim_id | 主张 | 定位（corpus / AUDIT / 抓取原文） | grade | status |
|---|---|---|---|---|
| LH-AGES-NGL-A | NGL 现页 In-depth：「the men are **28 and 24** years old respectively」（同页又含「aetatis suae 25」自身不一致） | 内部证据 af1610fda0363ab9（未公开；来源记录由维护者保留） sha 19a66a… **L709**；AUDIT RESULT §7 额外发现 / claim map §F X-AGES；review-evidence.md §3 独立复现 | `[史料]`（馆方英译） | **conflict** |
| LH-AGES-NGL-B | 同页 Audio description：「These reveal that the men are **25 and 29** years old respectively」 | 同 sha 19a66a… **L738**；AUDIT X-AGES / review-evidence.md §3 | `[史料]`（馆方英译） | **conflict** |
| LH-AGES-INSCRIPTION | 语料 Q3/Q4 + Hervey 拉丁铭文逐字 = **AET. SVAE 29 / AETATIS SVE (_sic_) 25** → 29/25 优先 | corpus Q3 L33-39 / Q4 L41-47；dossier §9 L257 交叉核对；`hervey1900.txt` sha f7734f75… L456-457 / L6059 / L6161；AUDIT RISK-6 / Q3/Q4 supported | `[自述]`（画内铭文）+`[史料]`（Hervey 转录） | supported（铭文原文层）；馆方双说仍 conflict |
| LH-AGES-DISPOSAL | 馆方英译自相矛盾 → **报告不修**；铭文拉丁原文优先；不裁断、不写入默认档 | AUDIT RESULT §7 / §12 限制 / claim map §F X-AGES（conflict (NEW)）；review-gate-receipt.json checks；本 shard learning_path §3/§4、how-to-think §3、mechanism_notes §D | `[归纳]`（处置口径） | **conflict（携带）** |

---

<a id="db-source-line-68"></a>
## 4. Windsor drawings + 遗嘱逐字证据（本次点名）

| claim_id | 主张 | 定位（corpus / AUDIT / 抓取原文） | grade | status |
|---|---|---|---|---|
| LH-WILL-VERBATIM | 遗嘱 Q1 逐字含 `gohooste / John Holbeine / servaunte to the Kynges Magestye / two Chylder / Octaber / sealed and sealed [sic] / MVCxliij / Snecher / Obynger / Maynert` | corpus Q1 L15-23（中译 L22）；dossier §5-1 L110；`chamberlain2_raw.txt` sha 62bcfbaa… **L17540-17565**（AUDIT RISK-5 confirmed）；review-evidence.md §2 读 L17538-17546 复核 | `[自述]`（self-written 遗嘱） | supported（载体级逐字；B4 已降级，OCR 未回校原刊） |
| LH-WILL-DRIFT | Q1 自身注 `chamberlain2_raw.txt:13601-13614` 实为 **"248 THE WINDSOR DRAWINGS"** 页文本（L13600-13603），非遗嘱 | corpus Q1 注 L20；`chamberlain2_raw.txt` **L13600-13603**；AUDIT §9 / §G 表 / RESULT §7 RISK-5 / review-evidence.md §2 / coverage-manifest.json.locator_drift_reported | `[史料]` | **partial**（corpus 自身 locator drift，+~3939 行；只报告两种定位、不判对错、不改源） |
| LH-WILL-SELFWRITTEN | 遗嘱是荷尔拜因**唯一较完整第一人称文本**；书信/日记自述缺失 | dossier 卷首 L9 / §10-3 L267；corpus 卷首 L5-6 / 末 L240；AUDIT X-GOALS / §12 | `[史料]` | supported |
| LH-ERASMUS-UNVERIFIED | Q5/Q6 拉丁/希腊原文未逐字核到（NGL 仅给英译）；X-AMERBACH-VERSE 上方拉丁诗句未转录 | corpus Q5 L49-55 / Q6 L57-63 / Q7 L65-71；dossier §10-1 L265 / §10-2 L266；`ngl_erasmus.html` sha efa3efac…「In English, it reads」；AUDIT X-ERASMUS / X-AMERBACH-VERSE | `[史料]` | **unverified**（honest unknown，不猜，不冒充原刊级） |

---

<a id="db-source-line-79"></a>
## 5. §4 六参数 / §8.2 八规则 → 练习映射（参数层）

| claim_id | 主张 | 定位（dossier / card / AUDIT） | grade | status |
|---|---|---|---|---|
| LH-PARAMS | P1 物证细节 70% / P2 净面 65% / P3 情绪克制 60% / P4 铭文密度 50% / P5 光线档 55% / P6 隐藏装置 30%（各三档） | dossier §4 L95-100；card §4 P1-P6；AUDIT §D S4-P1..P6 | `[归纳]` | **partial**（全部项目设定、未对原作像素测量，§8.2 末注 L216 / §10-6 L270） |
| LH-RULES8 | §8.2 八条可判定规则（净面 / 外硬内柔 / 材质分化 / 物证清单 / 铭文 / 软光 / 几何 / 变形装置） | dossier §8.2 L207-214 + 末注 L216；card §8.2；AUDIT §D | `[归纳]`（阈值）/ `[史料]`（依据） | **partial**（阈值未实测；规则文本内部一致） |
| LH-USAGE | §4 用法：P1/P2/P3 ≥2 条 ≥ 中档才成立；P4/P5 定文本与光；P6 可选（多数在「中」以下，不要硬塞变形） | dossier §4 L102；card §4 用法；AUDIT S4-用法（补充行，不计入 35 分母） | `[归纳]` | **partial**（粗筛必要非充分，见 §7 反例 1） |
| LH-LADDER | 3 阶梯（净面物证+织物质感 / 物证叙事+铭文编码 / 几何平面+格式极端）+ 8-section 路径；全部建议练习、未经人评 | 02-EXECUTION-PLAN.md L64（学习顺序）；01-AUDIT.md §8.1 L273（不写已证实收益）；dossier §12 L367-421（10 件练习清单 + L421 组合建议）；本 shard learning_path.md §1-§8 | `[归纳]`（设计候选） | **not_applicable**（建议练习，不声称学习收益；`human_review.status=not_applicable`） |

---

<a id="db-source-line-90"></a>
## 6. 13 rights rows = 12 PD + 1 CC0（本次点名）

| claim_id | 主张 | 定位（AUDIT / 现有记录） | grade | status |
|---|---|---|---|---|
| LH-RIGHTS-13 | 13 张公开图逐张 rights row：**12 Public domain + 1 CC0**（`dead_christ.jpg`），无 guessed PD | 内部证据 4a9fdf1ecb3ea8b6（未公开；来源记录由维护者保留） §逐张表（13 行）/ RESULT §6；`_images/manifest.md` L456-468 / 分节 L2204-2242 / `_images/holbein/MANIFEST.md` L15-27 三处一致；coverage-manifest.json `images_public=13`；review-evidence.md §5 复核 | `[史料]`（现有记录 metadata） | supported（metadata 层） |
| LH-RIGHTS-BOUNDARY | 权利是「引用现有记录 metadata 层」、非独立再 adjudicate；未 image_seen、未复访 Commons imageinfo；`henry_viii.jpg`=After Holbein 摹本、`darmstadt_madonna.jpg` 1528 补笔工作室参与不升级/不降级 | AUDIT rights_review.md §一致性/缺口 L33-38 / §私有层说明 L40-42 / RESULT §12 限制；review-evidence.md §5 | `[归纳]`（边界） | **partial**（外部许可页真实性 / 像素内容 `unverified`） |
| LH-RIGHTS-PRIVATE | 私有层 8 件研究副本（manifest L3205）与公开 13 张分开记；本艺术家非 images_public=0 私有层画家 | dossier §10-9 L273；`_images/manifest.md` L3205；AUDIT rights_review.md §汇总 L12 / RESULT §6 | `[史料]` | supported |

---

<a id="db-source-line-100"></a>
## 7. 反例 / 失败条件（3 个 `[inference]`）

| claim_id | 主张 | 定位（AUDIT counterexample / RESULT） | grade | status |
|---|---|---|---|---|
| LH-CE-1 | §4「≥2 条≥中档」必要非充分：《墓中基督》6:1 横幅 P1/P2 满档仍难满足 §8.2-7 / §8.2-3 → 画幅比+题材类别是隐藏分母 | 内部证据 3151350c5955afba（未公开；来源记录由维护者保留） §反例1 / §结论；AUDIT RESULT §8；review-evidence.md §7 | `[inference]` | **partial**（规则层推演，未像素实测、未目检、未跑生成器、未推翻规则） |
| LH-CE-2 | 可读铭文与净面无笔触 + 软边低阶跃在同像素区张力 → 「功能表面」是隐藏必要机制、不是装饰条款 | counterexample.md §反例2（引 §8.1 正段「painted inscriptions … on a functional surface」）；AUDIT RESULT §8 | `[inference]` | **partial** |
| LH-CE-3 | 《墓中基督》冲击来自物证 + 极端格式而非光 → 「情感强度不得由光承载」 | counterexample.md §反例3（Q25 陀氏接受史 + §12-2）；AUDIT RESULT §8 | `[inference]` | **partial**（支持现有规则） |

---

<a id="db-source-line-110"></a>
## 8. 自述 vs 归纳 / 推断（how-to-think 严格分界）

| claim_id | 主张 | 定位（corpus / dossier / GOALS） | grade | status |
|---|---|---|---|---|
| LH-SELFWRITE-10 | 26 条语料中 self-written=10（Q1–Q10：遗嘱 + 画内签名/题铭/箴言）；contemporary record=9 / reported speech=4 / 身后=3 = 26（条目标签口径） | corpus §一 L13-95（Q1-Q10）/ §二/§三/§四；dossier §5 L106-120；AUDIT §E 分型 / X-QUOTES26 / review-evidence.md §1（10/9/4/3 独立复现） | `[自述]`（Q1-Q10）/ `[史料]`（其余） | supported |
| LH-NO-PSYCH | 不从画面反推作者心理；荷尔拜因自述无任何数值阈值/决策顺序/机制词/创作心情；Woltmann「inner life」是 `[研究]` 非自述 | 00-GOAL.md L9；dossier 卷首 L9 / §3.1 边界注 L87 / §10-3 L267；corpus 末 L240；本 shard how-to-think.md §0/§3 | `[归纳]`（纪律） | supported（契约级；本文件未写任何作者心理断言） |
| LH-SELF-VS-INDUCTION | `[自述]` 仅画内文字/遗嘱字面；「物证级细节/净面/信息照明/物证装置」及全部阈值与决策序都是 `[归纳]` | dossier 卷首 L4（分级定义）/ §4 节级声明 / §8.2 末注 L216 / §10-6 L270；card §8.2 末注；AUDIT §D / §F | `[归纳]` | supported |
| LH-INDUCTION-ORDER | 「先写生→转写→罩染→编码→几何/格式→收口」是本项目为学习设计的操作序列，无作者原话规定此顺序 | 02-EXECUTION-PLAN.md L64 / L66；dossier §6.2 L142；本 shard how-to-think.md §2 D1-D7 | `[归纳]` | supported（设计候选，不自称史实） |

---

<a id="db-source-line-121"></a>
## 9. AUDIT 已接受基础 / 覆盖分母（不重审、不混称）

| claim_id | 主张 | 定位（AUDIT） | grade | status |
|---|---|---|---|---|
| LH-AUDIT-ACCEPTED | 内部证据 c4717bb05ac27410（未公开；来源记录由维护者保留） 为 ACCEPTED 依赖（receipt status=accepted / review accepted；review-gate verdict accepted；review-evidence 0 blocking / 0 non-blocking） | 内部证据 152f099a4d351899（未公开；来源记录由维护者保留） / `review-gate-receipt.json` / `review-evidence.md` §8 | metadata | supported |
| LH-DENOMINATOR | AUDIT 分母：79 claim units（supported 52 / partial 20 / conflict 5 / unverified 2）、26 corpus quotes、6 次公开抓取、3 反例、13 图 | AUDIT RESULT §4 / coverage-manifest.json / review-evidence.md §1（独立复现 79 / 52-20-5-2 / 26 / 10-9-4-3 / 12-11-6-5 / 13=12PD+1CC0 / 6 caches） | metadata | supported（本 shard 不新增分母、不混称出现次数 12/11/6/5 与条目标签 10/9/4/3） |
| LH-228-NOT-OURS | AUDIT 明确不主张 228/228，`_extract.py` 未读未跑未记 sha；本 LEARN shard 同样不主张 | AUDIT RESULT §2「228/228 有效性归属」/ §12；本 shard 不运行任何抽取器 | metadata | supported（诚实不归属） |
| LH-UNBOUND | 本包 dispatch_contract_state 对 LEARN 未绑定 bound contract → 本产物 `submitted` 不经 accepted/reused 语义门（verify-receipt.py 只跑 schema 结构门） | tasks-plan.json LEARN-holbein `dispatch_contract_state=unbound`；AUDIT receipt unresolved 末条同口径；本 shard receipt.json status=submitted / review=null | metadata | supported |

---

<a id="db-source-line-132"></a>
## 10. Locator resolution / 覆盖诚实边界

- 本文件所有 `dossiers/holbein.md:L<n>` / `_corpus/holbein.md:L<n>` / `modules/holbein.md:L<n>` / `conflicts.md:L<n>` 定位以 AUDIT §10「Locator resolution」程序化抽样（12 个全命中）为底本；本 shard 复核了 §4 L95-102、§8.2 L207-216、§3.1 L75-89、§12 L367-421、corpus Q1 L15-23 / Q3 L33-39 / Q4 L41-47、conflicts.md C-01/C-05/C-12 行号。
- Public-web 定位以 AUDIT 抓取文件 sha256 锚定（不依赖易变 URL 行号）：ngl_ambassadors.html `19a66af15497…` L709/L738、hervey1900.txt `f7734f75e602…` L456-457、chamberlain2_raw.txt `62bcfbaa4c4e…` L13600-13603 / L17540-17565。`review-evidence.md` §3 已 6/6 重算 match。
- **未决 / known-open 全携带**：X-AGES 双说、X-ANGLE 观看角度两说（NGL「bottom right corner」vs 1787「à prendre de l'angle gauche」）、X-ITALY 两说、Q22/Q23 conflict→订正、11 处 C-row 行号漂移、Q1 遗嘱 locator drift、Q5/Q6 拉丁/希腊原文 unverified、Q13/Q14 OCR 回校、13 图 image_seen 未设 —— 均**报告不修、不裁断、不关闭**（AUDIT §5/§9/§12 / RESULT §12）。
- **练习效果未由人评价**；`human_review.status=not_applicable`，全部为**建议练习**，不写「已证实学习收益」。`review:null`：本产物 `submitted`，待独立审者（非作者）裁定，作者不自接受；`receipt.json` 不列入自己的 artifacts（自哈希循环），其 hash 由 parent runner 另封存。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
