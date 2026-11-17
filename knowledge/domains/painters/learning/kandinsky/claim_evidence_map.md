<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-kandinsky；原正文 SHA-256 `30b669de7c45366ab60397b7a1c77dc794ba2f1ca1e3cc7a25e9d67c2d640b51`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-kandinsky — claim_evidence_map（逐断言回源）

> goal `Designers-Brain-Upgrade-20261115` · task `LEARN-kandinsky`（A-30 / A-44 承接）· source `f008952365a77e140cbda3f3959d43ef000f9a22`（只读）· 上游 `AUDIT-kandinsky` **ACCEPTED** · status `submitted`
> 每 claim 1 行：`claim_id · grade · support_status · locator（文件:节:行号 + 子串）· basis`。等级沿用原档词表（`[自述]`/`[史料]`/`[研究]`/`[归纳]`）；`[归纳]` 为本项目操作规则，**不冒充史料/自述/像素实测**；`[推测]` 计数 = 0。`[self-written]` ≈ `[自述]`（corpus 卷首 L4）。
> 本 lane **不重审 ACCEPTED 审计**：凡引 AUDIT 结论均标注其产物与判定（supported/partial/conflict/unverified），照实携带 known-open 项。`retrieved_bytes_sha256` / `read_scope` / `access_status` 的完整字段见 `receipt.json` `claims[].source_refs`；本文件用「路径:L行」简写定位，全部行号为本机 `nl -ba` 实测（工作树文件 hash 与 ledger / 冻结 head 声明一致）。
> 缩写：`D`=[kandinsky.md](../../dossiers/kandinsky.md) · `C`=`…/_corpus/kandinsky.md` · `M`=`…/modules/kandinsky.md` · `X`=[conflicts.md](../../../../cross/conflicts.md) · `AUD`=内部证据 6566a938eb0df270（未公开；来源记录由维护者保留）。

<a id="db-source-line-8"></a>
## 0. 源文件登记表（开工 `sha256sum` 实测，与 内部证据 221eaea2b22a1146（未公开；来源记录由维护者保留） head 一致）

| 对象 | 路径 | sha256 | read_scope / access |
|---|---|---|---|
| card | `…/modules/kandinsky.md` | `88e8d4ddffbc673c2b7fed64f60bf476ff552b8634a5599e67703e75327c60c7` | fulltext / available |
| dossier | `…/dossiers/kandinsky.md` | `63f56ff4f7fc324e55aa44540e18e5c87ad62958433eccb94591aae295284731` | fulltext / available |
| corpus | `…/_corpus/kandinsky.md` | `71b6b0fa141a1650b8a7d362e222aa683ada73bb167afb6fe1dbe37e45088517` | fulltext / available |
| conflicts | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | sections / available |
| goals | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | metadata / available |
| DE 底本缓存 | `AUD/web/pg46203_de.txt` | `78cda16455be2c6e57a65f7da81f5c42187d916481dba2568f4b1e532dfbf07c` | fulltext / available（AUDIT 抓取，本 lane 复用） |
| EN 底本缓存 | `AUD/web/pg5321_en.txt` | `a0457a553c14ca755b14594dc1ab1ef80ed3687916aa6d5c140728c648e7daa8` | fulltext / available（同上） |
| DE 逐字证据 | `AUD/raw/web-quote-verify2.out` | `a6eba8ab43251b86d86867617a53789898bbde56eaf3b07ea662249fa7d93578` | artifact / available |
| AUDIT RESULT | `AUD/RESULT.md` | `73a78eadf70aa19e95e83dbba3bc8c03462ba87e386cc4eadace52f616860d78` | fulltext / available |
| AUDIT claim map | `AUD/claim_evidence_map.md` | `71966241eb53576a22102474ee163879b4487f64495cbddebba98da8047a3902` | fulltext / available |
| AUDIT quote audit | `AUD/quote_audit.md` | `a948e769e13cab6c41f34f7fa6d8d844a512b04aaed23392f9adbe2f623fd363` | fulltext / available |
| AUDIT review-evidence | `AUD/review-evidence.md` | `a6d7eacf62be9144ac363a32c33a61e1e4f31357f0fc288c520ec6a94cac4cd1` | fulltext / available |
| AUDIT coverage | `AUD/coverage-manifest.json` | `826ae7f4d7b9392c973bf250fc64b343d9e866f15d76cd17ee26415ecde14abf` | artifact / available |
| AUDIT receipt | `AUD/receipt.json` | `fdec7f7d68cfaadfadadef4f89262f678c6af7ed679810a1c0b647be6810c0d9` | sections / available（`status=accepted`, L6） |

<a id="db-source-line-27"></a>
## 覆盖

| 区块 | 断言 | 行数 |
|---|---|---|
| §A 输入 / 依赖 / 边界 | K50·K51·K52·K53 | 4 |
| §B 机制 / 参数 / 规则 | K01·K02·K03·K04·K05 | 5 |
| §C 强调① 色彩-形状对应 + 音乐类比 | K10·K11·K12·K13·K14 | 5 |
| §D 强调② 德文 6 条 ACCEPTED 证据 | K20·K21·K22 | 3 |
| §E 强调③ Q09 EN-anchor known-open | K30·K31 | 2 |
| §F 强调④ B&W 木刻 scope-boundary probe | K40·K41 | 2 |
| **claims_total** | | **21** |

按 support_status：`supported` 10（K01/K02/K03/K04/K05/K12/K13/K14/K20/K21）· `partial` 6（K10/K11/K22/K50/K51/K52）· `conflict` 2（K30/K31，known-open 携带）· `[inference]` 归入 `partial` 2（K40/K41）· `supported`（事实登记）1（K53）。**不把 AUDIT 的 partial/conflict/unverified 升级为 supported；不新增 unverified。** 练习建议为 design_candidate / 建议练习，未经人评（`human_review=not_applicable`）。

---

<a id="db-source-line-43"></a>
## §A 输入 / 依赖 / 边界

- **K50** `[归纳]` `partial` — §4/§8.2 阈值全部 `[归纳]`、未对原作像素测量；11 公开图 `image_seen=0`；Q12/Q13/Q14/Q29 `unverified`、Q15–Q28 `partial`
  - locator: `D:L319`（§10-7「量化阈值为归纳、未实测……分母＝假想参考帧」）、`D:L254`（§8.2 注）、`D:L529`（自审 D「全部量化阈值未实测」）、`C:L229-L231`（corpus 缺口三条）、`AUD/coverage-manifest.json`（`per_status_counts` partial=62 / unverified=5 / supported=22 / conflict=1，sum=90；`image_seen` 未声称）
  - basis: AUDIT 90 行覆盖以「归纳未实测 + 转引级」为主；本 LEARN 不升级任何级别，所有阈值仅作自查靶值。⟨K50⟩
- **K51** `[归纳]` `partial` — `conflicts.md` 0 条 kandinsky 具名 C 行 / 0 near-miss 行；C-15/C-16/C-17 仅组合预检；8 处 body 行号漂移登记不修
  - locator: `X`（grep `kandinsky|康定斯基` = 0，AUDIT RESULT §5 / `coverage-manifest.json conflicts_rows_checked`）、`M:L65-L74`（冲突注记）、`D:L93`（§3.1 组合预检）、`D:L247`（C-15 色数不在 ≤3 上限域）、`D:L262`（§8.3 N6 口径）、`AUD/RESULT.md §5`（8 处 drift 表）、`AUD/review-evidence.md §5`（抽查 5/8 确认）
  - basis: 「0 行」是事实非缺陷；组合边界（N3 单主 / N6 声明口径 / 蒙德里安·波洛克·罗斯科禁区 D:L92 / §4 分工注 D:L109）沿用现有记录，本 lane 不重审、不改仓库。⟨K51⟩
- **K52** `[史料]` `partial` — 9 件重点作品 + 11 张公开图权利信息沿用现有记录，未做视觉检视
  - locator: `D:L414-L453`（§12 九件，各含看什么/学什么/怎么练）、`D:L153-L163`（图库 manifest）、`AUD/rights_review.md`（Lenbachhaus CC0 ×2 / Commons PD·PD-Art ×7 / CC0 摄影 ×1 / CC BY-SA 3.0 摄影 ×1 = 11）
  - basis: 不新增 provenance；外部许可有效性未独立再判（AUDIT `access_status=unknown` for 授权页）；`image_seen=0`。⟨K52⟩
- **K53** `[史料]` `supported` — A-44「剔除 1 误认件」为已确立事实（非缺陷）：Franz Marc 木刻页已换源，11 张全为剔除后
  - locator: `D:L471`（自审 B5 OVERTURNED）、`D:L528`（自审 D「已推翻」）、`…/_images/kandinsky/MANIFEST.md`「未采用」段、`AUD/rights_review.md` §A-44
  - basis: AUDIT RESULT §4 确认「fact, not a defect」；review-evidence §3 逐张 11/11 复核一致。⟨K53⟩

<a id="db-source-line-58"></a>
## §B 机制 / 参数 / 规则（全部 `[归纳]` 操作规则，非实测）

- **K01** `[研究]`+`[归纳]` `supported` — 零对象（成熟期非具象，可命名对象 ≈0）+ 元素可枚举（类别 ≥3、可数 ≥8）
  - locator: `D:L32`（§1-1「零对象……可命名对象数 ≈ 0」）、`D:L33`（§1-2「元素类别 ≥3；可数元素 ≥8」）、`D:L245-L246`（§8.2-1/-2）、`M:L40-L41`
  - basis: 定位与 AUDIT K1-01/K1-02 一致；本项目操作规则，§10-7 记未实测。⟨K01⟩
- **K02** `[归纳]` `supported` — 线独立于形：细长连通域 ≥5、≥2 条穿越色块、线不闭合为轮廓
  - locator: `D:L36`（§1-5）、`D:L248`（§8.2-4）、`D:L224`（§8.1 `thin, independent lines…never outlining objects`）、`M:L23/L43`
  - basis: AUDIT K1-05/K82-04；依据的 Q13《点线面》1947 OCR 本轮 `unverified`，故规则本身按 `[归纳]` 用，不进「已核实」栏。⟨K02⟩
- **K03** `[归纳]` `supported` — 色彩声部化 / 色彩预算 / 黑重音：色相族 4–8、互补对 ≥1、高饱和 S≥0.5 ≥15%、黑 5–25%
  - locator: `D:L34`（§1-3）、`D:L247`（§8.2-3）、`D:L251`（§8.2-7）、`D:L39-L40`（§1-8/-9）、`M:L42/L46`
  - basis: AUDIT K1-03/K82-03/K82-07 均 `partial`（归纳未实测）；本 LEARN 同口径，靶值非史实。⟨K03⟩
- **K04** `[研究]`+`[归纳]` `supported` — 浅空间/漂浮/对位：无地平线/透视/接地投影，上下左右质量差 ≤35%
  - locator: `D:L37-L38`（§1-6/-7）、`D:L249-L250`（§8.2-5/-6）、`D:L226`（§8.1 `weightless, no horizon`）、`M:L44-L45`
  - basis: AUDIT K1-06/K1-07/K82-05/K82-06。⟨K04⟩
- **K05** `[归纳]` `supported` — §4 六参数（默认 80/50/70/75/65/50）与 §8.2 八条判分规则；用法 P1+P3 定「是不是康定斯基」
  - locator: `D:L99-L109`（§4 表 + 用法 L108 + 分工注 L109）、`D:L245-L254`（§8.2 八条 + 总注 L254）、`D:L239-L241`（§8.1 三档先跑 + 自查三件事）、`M:L53-L63 / L40-L49`
  - basis: 模块卡 §4/§8.1/§8.2 与 dossier 逐字一致（`_extract.py --check` 228/228 覆盖 3 节）；AUDIT K4-01..08 / K82-01..08 全 `partial`。⟨K05⟩

<a id="db-source-line-76"></a>
## §C 强调① 抽象构成 = 色彩-形状对应 + 音乐类比机制

- **K10** `[史料]` `partial` — 色彩-形状对应：圆↔蓝 / 方↔红 / 三角↔黄（包豪斯期，对位声部）
  - locator: `D:L35`（§1-4 `[史料]` [R2] Schlemmer 1923 记录）、`D:L440`（§12-6「色-形对应（蓝-圆/红-方/黄-三角）如何对位」）、`D:L52`（§2-4 几何化期）、`D:L252`（§8.2-8 包豪斯档「色形对应对 ≥1」）、`AUD/claim_evidence_map.md` K1-04（`partial`：「经 WEB-WQ 见 Schlemmer 1923 引语同源口径，但原记录未直读」）
  - basis: **不是 `[自述]` 逐字**；AUDIT 经 WEB-WQ 核到同源句但转引载体未直读 → 照实 `partial`，不升级。⟨K10⟩
- **K11** `[自述]`+`[研究]` `partial` — 两阶段色彩-形式策略：1911–14 反几何不协和 / 1922 起几何化
  - locator: `D:L52`（§2-4）、`C:L121-L127`（Q16 反几何「不协和」）、`C:L128-L134`（Q17「线与面不合拍」）、`AUD/claim_evidence_map.md` K2-04（`partial`：Q16 经 WEB-WQ 核对、馆方文本未重抓）
  - basis: 两阶段均为「内在必然性」的不同解（D:L52 原话）；Q16/Q17 德文原信未回查 → `partial`。⟨K11⟩
- **K12** `[归纳]` `supported` — 「音乐类比机制」是本项目 `[归纳]` 标签，档案未用此四字词；组织三条 `[自述]` 支点
  - locator: `D:L70`（§3-5「音乐为模范……借的是**结构原则**，不是描摹音乐」）、`D:L7`（§0「凡从理论文本推导的规则一律标 `[归纳]`，不写成他作画时想着什么」）、`D:L53`（§2-5「以『声部』而非『象征词典』……避免图解化」）
  - basis: 标签只作组织用；不得反写为「康定斯基提出音乐类比机制」；借结构原则（节奏/对位/不协和/声部）是自述，标签是归纳。⟨K12⟩
- **K13** `[自述]` `supported` — 音乐类比三支点①色彩是琴键 ②通感映射 ③（黄=小号为同章旁证，不冒充第 7 条逐字）
  - locator: `C:L11`（Q01 德文 `Die Farbe ist die Taste…`）、`C:L76`（Q10 德文 `Musikalisch dargestellt ist helles Blau einer Flöte ähnlich…Baßgeige…Orgel`）、`C:L81`（Q10 注「刺柠檬黄……wie dem Ohr eine hochklingende Trompete」= 同章旁证）、`D:L117-L121`（§5-1）、`D:L53`（§2-5）、`AUD/raw/web-quote-verify2.out`（`DE Q1 keyboard: FOUND` / `DE Q10 floete: FOUND`）
  - basis: AUDIT K5-01/K2-05/Q01/Q10 = `supported`（WEB-DE 逐字命中）；黄=小号仅 C:L81 旁证，明确标注。⟨K13⟩
- **K14** `[自述]` `supported` — 音乐类比三支点③作品三分（印象/即兴/构图）+「不给计算给感觉」
  - locator: `C:L84`（Q11 德文 `…Improvisationen…Komposition…Nur wird dabei nicht der Berechnung, sondern stets dem Gefühl recht gegeben`）、`D:L49`（§2-1 三分工作法）、`D:L73`（§3-8 感觉优先）、`C:L89`（Q11 注 1936 回声）、`AUD/raw/web-quote-verify2.out`（`DE Q11 impro: FOUND`）
  - basis: AUDIT K2-01/Q11 = `supported`；1936 Composition IX 具体引语（§5-10 D:L162-166）AUDIT K5-10 = `unverified`（Pompidou 页未重抓），**只用 1912 德文回声**。⟨K14⟩

<a id="db-source-line-94"></a>
## §D 强调② 德文 6 条逐字（PG #46203）= ACCEPTED 证据

- **K20** `[自述]` `supported` — A-44「德文 6 条逐字核过」本轮重抓字节 FOUND，作为 ACCEPTED 证据使用
  - locator: `D:L495-L505`（自审 C 原样输出 6 条 FOUND + 1 条 EN 行）、`AUD/raw/web-quote-verify2.out`（`DE all-found: True`；`DE Q1..Q11` 全 FOUND；`Total found: 18 / 19`）、`AUD/web/pg46203_de.txt`（sha `78cda164…`，215143 B）、`AUD/RESULT.md §2`（「all 6 FOUND……A-44 逐字-German claim holds on freshly fetched bytes」）、`AUD/review-evidence.md §2`（审稿人抽查 Q07 L2063 / Q04 L1653 FOUND）
  - 6 条：G1 `Es gibt kein „muß"…`(Q04 C:L33) · G2 `Der Künstler muß etwas zu sagen haben…`(Q07 C:L55) · G3 `Alle Mittel sind heilig…`(Q08 C:L62) · G4 `Je tiefer das Blau wird…`(Q09 C:L69) · G5 `Die Farbe ist die Taste…`(Q01 C:L11) · G6 `Jedes Kunstwerk ist Kind seiner Zeit…`(Q02 C:L19)
  - basis: 证据级＝「重抓 PG #46203 字节上的逐字命中」（DE 底本 = *Über das Geistige in der Kunst* 3. Aufl. München 1912）；**不升级为「已直读纸本 / 已回查全部德文原信」**（§10-1 L313 / C:L229）。本 lane 不重开验证、不改字节、不标 unverified。⟨K20⟩
- **K21** `[自述]` `supported` — 内在必然性 / 自由+语法 / 感觉裁决 的创作原则可直接引用（G1/G2/G3 + Q03 + Q11 支撑）
  - locator: `D:L66`（§3-1 内在必然性）、`D:L68`（§3-3 手段神圣/有罪）、`D:L72`（§3-7 自由+语法）、`C:L26`（Q03 `Das ist schön, was einer inneren seelischen Notwendigkeit entspringt`）、`AUD/claim_evidence_map.md` K3-01/K3-02/K3-03（`supported`，WEB-DE 命中）
  - basis: 注意 K3-06「艺术家三重责任」三分表述为档案归纳 `partial`（德文底本仅见 `Der Künstler ist kein Sonntagskind des Lebens`），不冒充逐字。⟨K21⟩
- **K22** `[自述]` `partial` — 键盘引语德文单数 Taste/Hammer vs Sadler 英译复数 keyboard/hammers，两存并注（自审 B2）
  - locator: `C:L16`（Q01 注「德语原文为单数……Sadler 英译作 keyboard / hammers（复数化）」）、`D:L120`（§5-1）、`D:L468`（自审 B2 WEAKENED → 两存并注）、`AUD/claim_evidence_map.md` K5-01（`supported` 双底本）
  - basis: 事实 `supported` 但「两存并注」是项目口径（`partial`）；不写成「德文原文即键盘（复数）」。⟨K22⟩

<a id="db-source-line-107"></a>
## §E 强调③ Q09 EN-anchor 冲突（Sadler/Sadleir）= known-open

- **K30** `conflict` `conflict` — Q09 英文引号句 + `[R5]` 标注与 PG #5321 字节不符；德文命中但英译出处错误
  - locator: `C:L69`（Q09 德文 `Je tiefer das Blau wird…`，WEB-DE L2063-2064 命中）、`C:L71`（Q09 英译 `The deeper the blue becomes…towards the infinite…supernatural`，标 `英译（Sadler）`）、`D:L148/L150`（§5-7 德文 + 「英译对照 [R5]」）、`AUD/web/pg5321_en.txt`（EN 蓝段 `The inclination of blue to depth is so strong…` L2144-L2148）、`AUD/RESULT.md §2/§8-1`、`AUD/review-evidence.md §2`（`grep -c "The deeper the blue becomes"` = **0**）、`AUD/claim_evidence_map.md` Q09 行（`conflict`）/ K5-07（`partial`）
  - basis: AUDIT 新发现 conflict（90 行里 `conflict=1`）；**本 lane 作为 known-open 携带，不重新锚定、不静默保留 `[R5]`、不合并两个判定、不改写仓库**。下一步（交拥有者）：识别实际译本重锚或改标「中译/意译」。⟨K30⟩
- **K31** `conflict` `conflict` — 译名 Sadler/Sadleir 双写：源文本自身即有两种拼法，非单纯档案笔误
  - locator: `AUD/web/pg5321_en.txt:L15`（`Translator: Michael Sadleir`）、`:L48`/`:L496`（标题页 `MICHAEL T. H. SADLER`）、`AUD/review-evidence.md §2`（审稿人 nuance）、`AUD/RESULT.md §2/§8-2`（档案统一写 "Sadler"）
  - basis: 档案「Sadler」与标题页一致、现代学术形为 Sadleir；归一化为 `Sadler (M.T.H. Sadleir)` 加注是下一步；本 lane 不收口。⟨K31⟩

<a id="db-source-line-116"></a>
## §F 强调④ 黑白木刻反例 = scope-boundary probe

- **K40** `[归纳]` `partial`（`[inference]`）— 44 幅 B&W *Klänge* 木刻触发 §4+P3 与 §8.2-3 误判 → **scope-boundary probe，非 confirmed overturn**
  - locator: `D:L57`（§2-9「《声响集》56 幅……黑白木刻训练『线的纯化』」）、`C:L223`（56 木刻其中 12 彩色 ⇒ 44 黑白）、`D:L108`（§4 用法 P1+P3 定「是不是康定斯基」）、`D:L247`（§8.2-3 色相族 4–8 / 互补对 ≥1 / 高饱和 ≥15%）、`AUD/RESULT.md §7`（`[inference]` Verdict「scope-boundary probe, not a confirmed overturn」）、`AUD/review-evidence.md §4`（CONFIRMED [inference]）、`AUD/claim_evidence_map.md` K82-03 / K4-07（`partial`）
  - basis: 一幅 B&W 木刻 = 2 色族 / 0 互补对 / 0 高饱和，满足 P1 与 §8.2-1/-4 却失败 P3 与 §8.2-3；规则作用域是「成熟期非具象 + 色彩声部」绘画默认档（D:L218/L239/L254），早期具象档（D:L109）与版画（§2-9）是分开 lane。**rules unchanged，K82-03/K4-07 保持 `partial`**。⟨K40⟩
- **K41** `[归纳]` `partial`（`[inference]`）— 三处口径不互相替代；近单色豁免解不了反例；判别动作＝预注册 E4
  - locator: `D:L247`（§8.2-3「近单色档仅在『刻意克制』时允许且须显式声明」= 规则内豁免）、`D:L109`（§4 分工注早期具象档允许 = 时期档）、`D:L57`（版画 = 媒介档）、`D:L218/L239/L254`（绘画默认档声明）、`AUD/review-evidence.md §4`（「互补对 ≥1 和色相族 4–8 仍 fail even under that clause……pre-registered E4 test feeding the 44 B&W frames」）、`AUD/RESULT.md §7` 末
  - basis: 即使显式声明「版画/黑白档」援引近单色豁免，互补对/色族仍失败 → 反例力度不减；本 leaf **不预填 E4 结果、不加豁免、不写「已证实推翻」**。⟨K41⟩

---

<a id="db-source-line-127"></a>
## 定位方法 / 诚实声明

1. 全部行号为本机 `nl -ba` 对**工作树**文件实测；工作树三件输入 hash 与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） / 冻结 head `f0089523` 声明逐字一致（开工 `sha256sum` 复核，见 `runner_receipt.json`）。AUDIT 的 `run_checks.py` 90/90 locators resolve（`raw/locator-check.out`）；本 LEARN 沿用同一纪律，不复制 X 中 8 处 stale 行号。
2. `conflicts.md` 对 kandinsky 的 grep 结果 = 0 具名行是**事实**，不是漏审；C-15/C-16/C-17 body 的 8 处行号漂移按 AUDIT RESULT §5 **登记不修**（写权限在 CONFLICT lane）。
3. AUDIT 的 `supported=22 / partial=62 / conflict=1 / unverified=5 / sum=90` 与 `quote_count=29` 照实携带；本 LEARN 21 条断言**不新增 unverified、不把 partial/conflict 升级 supported**；两个 `conflict`（K30/K31）就是 known-open 项本身。
4. 德文 6 条（K20）是「重抓字节逐字命中」级 ACCEPTED 证据；Q09 英文句（K30）与德文 G4 是**同一条目的两个不同对象**，德文可用、英文不可用，不混写。
5. 全部练习为**建议练习**（design_candidate），学习收益未经人评（`human_review=not_applicable`，01-AUDIT.md §8.1 L273 / §8.4 L308）；`status=submitted` / `review=null` / 作者不自接受；`execution_dedup_key=null`（无 bound dispatch contract，不经 accepted 语义门）。`verify-receipt.py` 对 submitted 只跑 JSON Schema 结构门。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
