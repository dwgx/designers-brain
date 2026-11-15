<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-hiroshige；原正文 SHA-256 `86103baba1e3aceff32d39f7c431a4879724ec6b9fda319229d81d6795101548`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-hiroshige · Claim / Evidence Map

> 任务 `LEARN-hiroshige`｜作者 LearnHiroshige（hy4free）｜2026-11-15｜kind: `claim_evidence_map`
> 仓库 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22` **只读**；证据底座 = 已 ACCEPTED 内部证据 4919edab864eb7ff（未公开；来源记录由维护者保留）。
> **locator 形式**：`FILE Lx[-Ly]` 或 `FILE §节`；FILE 缩写见 §0。所有 locator 指向**本机已落盘文本 / AUDIT 分片 / 包内文档**，本 lane 未重访外部 URL、未目检原图。
> **support_status**：`supported / partial / conflict / unverified / not_applicable`。**不把「来源存在」当「来源支持」、不把 `[归纳]` 阈值当史实、不把转引当原刊逐字**（AUDIT 纪律）。
> **分级**：`[自述]`（极薄：`corpus Q1/Q2` 且存疑）· `[史料]` · `[研究]` · `[归纳]`（项目操作规则）· `[推测]`（=0，本片不用）。

---

<a id="db-source-line-11"></a>
## 0. 输入与证据底座哈希（开工 `sha256sum` 实跑，全部与 AUDIT 登记一致）

| 缩写 | 文件 | sha256（本 lane 实测） | 来源登记 |
|---|---|---|---|
| CARD | [hiroshige.md](../../modules/hiroshige.md) | `d2b2c4c257e6cb226ed67bbd01e52b435c98f380951e88b7c0f6a960348580bb` | 内部证据 13d23d01bea327c6（未公开；来源记录由维护者保留）；AUDIT `receipt.json input_hashes` |
| DOSSIER | [hiroshige.md](../../dossiers/hiroshige.md) | `83b65e655d676d390a60d7bdfd3a930d66188d213f0defccabda07b832fbe027` | 同上 `.dossier_sha256` |
| CORPUS | [hiroshige.md](../../dossiers/_corpus/hiroshige.md) | `3206752eba5f7181d1e07aba985b78d5eb33789d1d6332e0555a9ccca3607301` | 同上 `.corpus_sha256` |
| CONFLICTS | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | AUDIT `RESULT.md §1` 全局哈希 |
| GOALS | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | 同上 |
| IMGMANIFEST | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` | 同上 |
| SHARDS | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） | `e1ec2d11ed3b3458a2e233a101319ffdf12d253b22562a97d4e25618b1158ce9` | AUDIT `coverage-manifest.json.hashes` |
| REGISTRY | 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） | `7daf31bbac2826179f3d7beecb6e0ec30f9628acd638ce4b3bffc39bafc6c374` | 同上 |
| A-RESULT | 内部证据 43c3bb8c2faf126f（未公开；来源记录由维护者保留） | `6abde2bfabd4ec4372dd34a3968d17f8a8a1bf6737efc815635167fba4b58b5d` | 本 lane 实测（AUDIT receipt artifact） |
| A-CLAIM | 内部证据 834a74baac33f9a7（未公开；来源记录由维护者保留） | `cc8f1cc4ae0c5417052bb577fce80b7c8a8156f7b51487bdaba42d5c6ab2e8c1` | 本 lane 实测 |
| A-COVER | 内部证据 8999417d12fe0177（未公开；来源记录由维护者保留） | `1619b4730591dddfd8dc5acc881e3fa561e12a84a436b5753d1e07a831e1aca4` | 本 lane 实测 |
| A-RIGHTS | 内部证据 d4655f089dfa31f6（未公开；来源记录由维护者保留） | `db30fc2f38ce3e83419a6fc6d346f290594150232793a8cebc6450a6333081fd` | 本 lane 实测 |
| A-CX | 内部证据 545a12e27c8ad79c（未公开；来源记录由维护者保留） | `f959a3371c18cd995ecf54be9f0ab623931eb5dc17f7f0678a60b77ef78e3a80` | 本 lane 实测 |
| A-RECEIPT | 内部证据 d6669657f6ba3a57（未公开；来源记录由维护者保留） | `2550e652b1b4bb2ac7e09f14ad286326142798816c55e71bec391c98fd0f2b33` | 本 lane 实测（status=accepted） |
| P-01AUDIT | `01-AUDIT.md`（包内） | `738d6a5a7dde17e444a594c1116da7322f2b0b127cc000c43c835f7f4e65aacf` | 本 lane 实测 |
| P-00GOAL | `00-GOAL.md`（包内） | `3799710118a32d6aeaf2f2fdc9524f779ba4d1132318e1a7422413df44fbfa81` | 本 lane 实测 |
| P-03AGENDA | `03-RESEARCH-AGENDA.md`（包内） | `8da2ef1cce7a4090ec45de82a98c9a6d5e17af68cff849f66c381b67beeaefd9` | 本 lane 实测 |

> repo HEAD 实测 `f008952365a77e140cbda3f3959d43ef000f9a22`（`git rev-parse HEAD`，只读），与 AUDIT `coverage-manifest.json.repo_head` 一致。本 lane **不运行任何 git 写操作**。

---

<a id="db-source-line-37"></a>
## 1. 上游依赖 ACCEPTED（本 lane 不重审）

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-DEP-ACCEPTED | `AUDIT-hiroshige` = **ACCEPTED**；reviewer `ReviewGateAUDIT-hiroshige(glm-5.3-flash)`，verdict=accepted | `A-RECEIPT` L6 status=accepted；`review.verdict`；`review.reviewer_actor_id` | `[史料]`（回执） | supported | 本 lane 直读 内部证据 d6669657f6ba3a57（未公开；来源记录由维护者保留） |
| LH-DEP-73 | AUDIT 73 行 claim，`per_status = {supported 57, partial 14, conflict 2}`（和=73），locators 全解析 | `A-RESULT §7`；`A-COVER claims_total=73, per_status, locators_all_resolve=true` | `[归纳]`（审计结论） | supported | 复用 AUDIT ACCEPTED 覆盖口径 |
| LH-DEP-228 | `_extract.py --check` 本轮实跑 `checks=228 ok=228 fail=0`（锚定 `_extract.py` sha `4afa31ec…`）；§C 的 60/60 是 wave18「20 卡」快照 | `A-RESULT §2`；`A-COVER.hashes._extract_check` | `[史料]` | supported | 复用，不重跑（本 lane 只读 LEARN 分片） |

---

<a id="db-source-line-47"></a>
## 2. 两条主机制（雨雪风大气瞬间 / 斜视角构图）

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-M-WEATHER-SUBJECT | 天气即主角：雨雪雾月为情绪装置，天气符号面积 ≥15%、同系列 ≥2 张以天气命名 | `DOSSIER L36` §1-2；`CARD L10` 浓缩 5 条第 2 条；`CORPUS Q15`（TNM「signaling shifts in time and weather」） | `[研究]+[归纳]` | supported | 馆方原文 + §1-2 可观察量 |
| LH-M-RAIN-LINES | 雨＝等宽等距斜线族（15°–45°、方向方差 ≤10°、长度方差 ≤20%、线宽变化 ≤30%），**不承担明暗**；雪＝留纸白 V≥0.9 无颜料边缘；雾＝横带；月＝单一发光体 | `CARD L46` §8.2-2；`DOSSIER L55` §2-4；`DOSSIER L41` §1-7 | `[史料]+[归纳]` | supported | 《庄野》《大はし》《蒲原》+ 留纸工艺 `[R2]` |
| LH-M-WIND-BOUNDARY | **「风」不是广重的第五种天气符号**：风以动势题材出现（《阿波 鳴門の風波》漩涡/暴雪），属 §3.1 边界样本，判定须 ≥2 轴联合；风拆成曲线族＝北斋档 | `DOSSIER L83` §3.1 边界注；`DOSSIER L402-405` §12-9；`DOSSIER L81` 北斋档「自然力是动势事件」 | `[归纳]` | supported | 本片诚实口径：不编造第五符号；§3.1 写死分工 |
| LH-M-WEATHER-INSTANT | 天气是「可重访的系列情绪」而非一次性事件现场（vs 透纳）；天气在动画面不动（光流 Δ≤2%/帧、雨线整体 ≤10%/s 视差） | `DOSSIER L90` §3.1 vs 透纳；`CARD L52` §8.2-8；`DOSSIER L36` | `[归纳]` | supported | C-09 静侧；版画为静态媒介 |
| LH-M-CROPPED | 裁剪式取景：近景物被画框裁切、贴到镜头前，远景被前景框住；「too close to the lens」把视线推向画外 | `DOSSIER L35` §1-1；`CORPUS Q20`（Potter 2007 **转引**）；`CARD L9` | `[研究]`（转引 partial） | partial | Q20 原刊未直读（`CORPUS:209` 转引清单）；`DOSSIER L56` 引「夸张单点透视」为研究描述 |
| LH-M-CROPPED-METRIC | 裁剪可判定量：≥1 前景与框相交、边缘带 10% 内被占 ≥15%、前景纹理 ≤10 边缘点/千像素、远景符号中轴 ±25% | `CARD L48` §8.2-4；`DOSSIER L208` §8.2-4 原样 | `[归纳]` | supported | 假想参考帧阈值，非原作像素实测 |
| LH-M-NO-SINGLE-POINT | 斜视角 ≠ 单点透视：§8.1 负向段禁 `single-point linear perspective with vanishing lines / dramatic cast shadows / chiaroscuro`；§3.1 判据④ 广重侧＝裁剪框景+水平/纵深秩序 | `CARD L34-36` 负向段；`DOSSIER L82` §3.1 判据④；`CARD L48` | `[归纳]` | supported | 生成禁令优先于 `DOSSIER L56` 的研究描述 |
| LH-M-VERTICAL-3LAYER | 竖幅三层叠合（近特写→中事件→远符号）、地平线在上/下 1/3 不在中线 ±5%；横版给「路与河」竖版给「切片」 | `CARD L51` §8.2-7；`DOSSIER L38` §1-4、`L59` §2-8；`DOSSIER L398-400` §12-8 | `[归纳]+[史料]` | supported | `[R1]` 近中远叠合构图 |
| LH-M-BOKASHI | 渐印 bokashi＝天空/水面/雾连续梯度（长边 ≥30%、带内明度差 ≤2/255、方向单调）；是系列可调参数不是特效 | `CARD L47` §8.2-3；`DOSSIER L54` §2-3；`CORPUS Q21`（后印加深蓝 bokashi） | `[史料]+[归纳]` | supported | `[R2][R7]` 工艺记述 + 版本差异 |
| LH-M-BLUE | 蓝系 H190–250° 面积 25–40%、≥60% 在渐印带、纯平涂大块蓝 ≤1、主色 ≤8；**「Hiroshige blue＝普鲁士蓝」命名 partial** | `CARD L50` §8.2-6、`L65` P6；`CORPUS Q19`（转引 田辺昌子 2011 原刊未直读）；`A-RESULT §3` | `[归纳]` + 命名 unverified | partial | en.wikipedia 全文未出现 "Prussian blue"/"Hiroshige blue" → 英文页未复核到；**不升级** |
| LH-M-CX1 | §4「P1/P2/P4 ≥2 条 ≥ 中档」是**必要过滤器、非充分身份判据**：北斋式曲线族可过闸却违反 §3.1 ≥2 轴 | `A-CX CX-1`；`DOSSIER L83` 边界注；`CARD L67` 用法 | `[归纳]`（inference 反例） | supported | AUDIT 4 个 `[inference]` 反例全部非完成的真人实验 |
| LH-M-CX2 | §8.2-3（有渐印）与 §8.2-6（蓝 ≥60% 在带内）可同时满足但互不蕴含 → 分开练 | `A-CX CX-2` | `[归纳]`（inference） | supported | 教学排序结论 |

---

<a id="db-source-line-66"></a>
## 3. §4 六参数 / §8.2 八规则（逐条可判定，全部 `[归纳]`）

| claim_id | 论断 | locator | 等级 | status |
|---|---|---|---|---|
| LH-P-P1 | 系列叙事强度三档（单张/10–30/55–120），默认 70% | `CARD L60`；`DOSSIER L99` | `[归纳]` | supported |
| LH-P-P2 | 天气/时刻强度三档，默认 60% | `CARD L61`；`DOSSIER L100` | `[归纳]` | supported |
| LH-P-P3 | 渐印大气梯度三档，默认 65% | `CARD L62`；`DOSSIER L101` | `[归纳]` | supported |
| LH-P-P4 | 裁剪框景强度三档，默认 60% | `CARD L63`；`DOSSIER L102` | `[归纳]` | supported |
| LH-P-P5 | 旅人密度三档（0–2/3–8/≥10），默认 50% | `CARD L64`；`DOSSIER L103` | `[归纳]` | supported |
| LH-P-P6 | 蓝三档（<15%/25–40%/≥40%），默认 55%；C-12 蓝轴二选一 | `CARD L65,67,74`；`DOSSIER L104,106` | `[归纳]` | supported |
| LH-P-THRESHOLDS-INDUCTIVE | 全部 §8.2/§4 阈值 = `[归纳]`、**分母＝假想参考帧、未对原作做像素测量** | `CARD L54`（§8.2 末注）；`DOSSIER L214,266` | `[归纳]` | supported |
| LH-R-1..8 | 八条自查规则：系列一致性 / 天气线族 / 渐印 / 裁剪框景 / 旅人 / 色相预算 / 竖幅叠层 / 静场运动预算 | `CARD L45-52`；`DOSSIER L205-212` | `[归纳]` | supported |
| LH-R-OVERRUN | 五类越界警报：①曲线族/动势→北斋 ②一次性天气→透纳 ③建筑剖面/图内书法→贝赫扎德 ④排线/实心黑→丢勒 ⑤画内单光源→卡拉瓦乔/伦勃朗 | `CARD L67`；`DOSSIER L106` | `[归纳]` | supported |

---

<a id="db-source-line-82"></a>
## 4. 分工条款 / 冲突预检（AUDIT：conflicts.md 无广重命名 C 行）

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-C-DIVISION | 四条写死分工：vs 北斋（系列骨架+蓝轴，≥2 轴）、vs 贝赫扎德（叙事单位）、vs 透纳（天气时间性）、同侧丢勒（平涂/雨线声明） | `DOSSIER L79-91` §3.1；`CARD L73-77` 冲突注记；`DOSSIER L8` 分工口径 | `[归纳]` | supported | 写死条款，可被组合实验推翻 |
| LH-C-NO-HIROSHIGE-ROW | `conflicts.md` 是原始 20 卡冻结台账（18 C 行 + §4 near-miss 11 行）；`grep -i 'hiroshige\|广重\|広重'` **零命中** → **无广重 party 的 C 行** | `A-RESULT §4`；`A-CLAIM §C G13-CONFLICTS-ZERO`；`A-COVER.conflicts_rows_naming_hiroshige=0` | `[归纳]`（审计结论） | supported | 复用 AUDIT ACCEPTED，不重审 |
| LH-C-ADJACENCY | 模块卡/§3.1 引 C-07/C-09/C-12/C-16 是**邻接预检轴**（当事人丢勒/北斋/梵高/莫奈等），广重不是 party | `CARD L73-77`；`DOSSIER L84,89,91`；`A-RESULT §4` | `[归纳]` | supported | 同上 |
| LH-C-LOCATOR-DRIFT | conflicts.md 数值行号（L188/L189/L193 引 hokusai §8.2）**已 stale**；re-anchoring 属 CONFLICT-xx lane（repo 只读，AUDIT 只报不改） | `A-RESULT §4,§9-3`；`A-COVER.conflicts_locator_drift[]` | `[归纳]`（审计结论） | supported | 本片用实测子串 + 本片 locator，不沿用陈旧绝对行号 |
| LH-C-NOT-EXPERIMENT | C-06 可拆 / C-18 分区 / C-12 二选一等**未经本 lane 或 AUDIT 组合实验验证**；规则层互斥 ≠ 实验验证 | `A-RESULT §9`；`A-CX`（全部 `[inference]` 非完成的真人实验） | `[归纳]` | supported | 不宣称 E2/E4 通过 |

---

<a id="db-source-line-94"></a>
## 5. 数字口径 / 权利底座 / known-open（核心挂账）

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-N-24-QUOTES | 语料实为 **24 条**（Q1–Q24，`grep -c '^### ' = 24`）；ledger `corpus_quotes=24` | `CORPUS` 全文 Q1–Q24；`SHARDS.artists[hiroshige].corpus_quotes=24`；`A-CLAIM §C G13-CORPUS-24` | `[史料]` | supported | 本 lane 读全文确认 |
| LH-N-25-25-PROBES | 「引文 25/25」= **25 条逐字字符串探针**（vs 本地源文件命中），**不是 25 条语料** | `DOSSIER L465,494`；`GOALS L74`；`A-RESULT §2`；`A-CLAIM §C G13-QUOTE-25-25` | `[史料]` | supported | AUDIT G13 清账：分母不同 |
| LH-N-23-STALE | §5 标题「完整语料 23 条」是**第三个 stale 数**（疑似 wave18 残留），与实际 24 冲突；AUDIT 判 `conflict`，报告不改 | `DOSSIER L110`；`A-CLAIM §C G13-SECTION5-23`；`A-RESULT §9-1` | `[史料]` | conflict | **挂账，不改写仓库** |
| LH-N-IMAGES-18 | 图库 18 张 = **12 Met CC0 + 6 Commons `Public domain`**；精确口径 ≠「18 张全 PD/CC0」宽松合称 | `DOSSIER L7,27`；`A-RESULT §2`；`A-RIGHTS` 18 行；`A-COVER.images_rights_breakdown` | `[史料]` + AUDIT `[归纳]` 精确化 | supported | 6 件 Commons **非 CC0**（`A-CLAIM §C G13-IMG-RIGHTS` = partial） |
| LH-N-MET-12-CC0 | Met 12 件 `isPublicDomain=true`（CC0）逐件可核：36922/56915/56916/36932/37248/55433/36539/56689/53783/36719/45294/36545 | `A-RESULT §2`；`A-CLAIM §C G13-MET-12-CC0`；`A-COVER.external_fetches[0..1]`（`raw/met_*.json`）；`CORPUS Q24`（object 55433 著录范式） | `[史料]` | supported | **本片未复访 API、未目检图**；沿用 AUDIT 本轮活检 |
| LH-N-744-747-KNOWNOPEN | **v1.1 total 744→747 漂移 = known-open**：历史快照 744（2026-10-16）/ `v1.1/search?q=Hiroshige` 活值 **747** / `v1/search` **RETIRED (2026-10-01)**；744 不可按原文复跑 | `DOSSIER L158` §7-3/R12；`A-RESULT §2,§9-2`；`A-CLAIM §C G13-MET-744`（conflict）；`A-COVER.external_fetches[2..3]`（`met_v11_search.json` sha `b2b9a062…`、`v1` sha `2db82187…`） | `[史料]` conflict / **known-open** | conflict | 三件并列引用；不写成任一单值现状、不把 +3 当错误修正、下一次复跑重取 v1.1 + 记 retrieval time |
| LH-N-SERIES-118-120 | 名所江戸百景 118/119/120 口径并存：广重 118 + 二代 1 + 目次 1 = 120；119 = 118 + 二代 1；en.wiki 现文「two were added by Hiroshige II」构件拆分不同、数值 120 一致 | `DOSSIER L23,249,431`（自审 B4 CONFIRMED）；`CORPUS Q17`；`A-RESULT §2`；`A-CLAIM §C G13-SERIES-118` | `[史料]` | supported | 口径并存，非缺陷 |

---

<a id="db-source-line-108"></a>
## 6. 亲笔层 / 引用卫生（诚实缺口，不升级）

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-Q-NO-TREATISE | 广重**无画论专著**；亲笔＝《甲州日記》(1841) + 辞世句（存疑）；「他内心如何」按操作规则处理 | `DOSSIER L10`；`CORPUS L5`；`P-00GOAL L9`；`P-03AGENDA L14` | 项目宪章 / `[史料]` | supported | 本片 `how-to-think.md §0` 的硬约束 |
| LH-Q-THIN-AUTOGRAPH | Q1 辞世句归属存疑（「後代の広重の作ではないか」、两处表记并存）；Q2《甲州日記》**日记正文与狂歌 11 首逐字未取得**（前半 1923 烧失） | `CORPUS L16-17,24-25,206`；`DOSSIER L114-115,258,260`；`A-RESULT §3` | `[史料]` | partial | 亲笔层极薄，不生成「广重认为」 |
| LH-Q-VANGOGH-ZERO | 梵高书信全站 `Hiroshige` **零命中**；Q8–Q10 为「日本艺术」通论，**不得写成对广重的直接评价**；直接证据 = Q11（VGM 摹本著录）+ 两幅摹本 | `DOSSIER L259` §10-2、`L429` 自审 B2 **OVERTURNED**；`CORPUS L79,207`；`DOSSIER L117-119` | `[史料]` + 审计结论 | supported | `vangoghletters.org` 全字段检索（AUDIT 沿用） |
| LH-Q-TRANSCRIPTION | 转引清单 `Q5/Q12/Q13/Q17–Q23` 原刊/原书未直读；Q19「Hiroshige blue」命名未在英文页复核到；Amsden 1912 英译需 OCR 安全归一（自审 B5） | `CORPUS L209-210`；`DOSSIER L263,433`；`A-RESULT §3,§9-4` | `[史料]` | partial | 「书名+页码列在 corpus」≠「原书已读」 |
| LH-Q-NO-PSYCH | 本片全部「为什么」落到可观察参数或馆方 `[研究]` 描述，**不以「广重想要/认为」开头**；`[推测]`=0 | `P-00GOAL L9`；`P-03AGENDA L14`；本片 `how-to-think.md §1/§2.3` | `[归纳]`（设计纪律） | supported | no invented psychology from artwork appearance |

---

<a id="db-source-line-120"></a>
## 7. 交付形状 / A-30 / 练习状态

| claim_id | 论断 | locator | 等级 | status | basis |
|---|---|---|---|---|---|
| LH-A30-SHAPE | A-30 §8.1 要求每位路径至少：前置知识 / 重点作品及来源 / 要观察的机制 / 具体练习 / 可观察结果 / 常见失败 / 下一步 / 使用边界；本片 `learning_path.md §1–§8` 八节齐备 | `P-01AUDIT L269-273` §8.1；本片 [learning_path.md](learning_path.md) 八节标题 | `[归纳]`（规格复述） | supported | 复用现有档案 §12、作品与机制，不新编生平（`L271`） |
| LH-A30-TOTALROUTE | 本片是 `LEARNING-INDEX`（76 路径 + 总路线）的一片；基础档→进阶档→跨艺术家比较分支 | `REGISTRY.LEARNING-INDEX.dependencies`（含 `LEARN-hiroshige`）；`DOSSIER L412` 组合练习建议；`P-03AGENDA L125-126` | `[归纳]` | supported | 总路线由集成 lane 汇总，本片不冒充总路线 |
| LH-A30-STYLE-SEPARATE | `card_has_81b=false`（SHARDS）；§8.1b 纯风格缺节属 `STYLE-hiroshige` lane，**不占本学习路径分母**（65 缺节对象另计） | `SHARDS.artists[hiroshige].card_has_81b=false`；`REGISTRY.STYLE-hiroshige`；`P-03AGENDA L125-126` | `[归纳]` | supported | `A-RESULT §9-5` 同样挂账 |
| LH-PRACTICE-UNVERIFIED | 全部练习 = **建议练习 `[归纳]`**；学习收益未经真人完成或评价（`human_review=not_applicable`），**不写「已证实学习收益」** | `P-01AUDIT L273`；本片 `learning_path.md §4 抬头`、[mechanism_notes.md](mechanism_notes.md) 抬头；`RESULT.md §7` | `[归纳]`（规格） | supported | `01-AUDIT.md:273` 硬要求 |
| LH-NO-REPO-WRITE | 本 lane 只读仓库、写路径仅 内部证据 d7ceb4e2a8c6ca02（未公开；来源记录由维护者保留）、无 git 写、无子代理派发（`spawns_allowed=false`）、产物无凭据 | 本片 `runner_receipt.json`；`receipt.json.allowed_write_paths` | `[史料]`（执行记录） | supported | `submitted` ≠ `accepted`，作者不自我验收 |
| LH-EXT-NOT-REVISITED | 外部 URL（R1–R17、Met/Brooklyn/TNM/VGM、archive.org、专门馆）本轮**未重访**（`access_status=unknown`）；18 张图**未目检**（`image_seen=0`） | `DOSSIER L225-243` §9；`A-RESULT §5`（7 次 fetch 由 AUDIT 本轮完成） | `[史料]` | supported | 沿用 AUDIT 记录，不升级 |

---

<a id="db-source-line-133"></a>
## 8. 覆盖 / 诚实声明

- 本表 **46 条论断**逐条带 locator + 等级 + support_status；`conflict` 2 条（LH-N-23-STALE、LH-N-744-747-KNOWNOPEN）、`partial` 5 条（LH-M-CROPPED、LH-M-BLUE、LH-Q-THIN-AUTOGRAPH、LH-Q-TRANSCRIPTION 等），**无一条被升级超过其引用字节**。
- 「来源存在」≠「来源支持」；`[归纳]` 阈值 ≠ 史实 / 原作像素实测；转引 ≠ 原刊逐字；本机文件 available ≠ 外部来源 available。
- **744→747 known-open**、§5「23 条」stale、conflicts.md 行号漂移、亲笔层极薄、原刊未直读 → 全部按 AUDIT `unresolved` 原样挂账，写入 `RESULT.md §7` 与 `receipt.json.unresolved`，**不改仓库、不补标、不升级**。
- `submitted` ≠ `accepted`；独立审阅（review=null）由主脑 / glm-flash review gate 依据原始产物验收，交付作者不能成为唯一验收者。
- 本文件为映射表，不运行图像生成、不重访外部 URL、不跑组合实验、不改仓库。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
