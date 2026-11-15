<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-kahlo；原正文 SHA-256 `684894bfd0cec1707a663ae96a94b6558856066a50c47a84190f776e141cd075`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-kahlo — 机制说明（mechanism_notes）

> A-30 Lane B · 依赖 ACCEPTED 内部证据 ddc7ed9c8499317c（未公开；来源记录由维护者保留）。本文件把 [kahlo.md](../../dossiers/kahlo.md) §4 六参数 + §8.2 八规则 + §3.1 分工条款映射到练习，记录 §4-P6 例外档、失败/适用条件、已知漂移。repo READ-ONLY；参数全是 `[归纳]`、未经渲染实验校准（dossier L100 / L320 / §10-8）；本 shard 不渲染、不像素测量、不改规则文本。
> 等级同 [kahlo.md](../../dossiers/kahlo.md) L5；`fact(已决)` = AUDIT 独立复核的 resolved fact（images_public=0 / NMWA 权利行 ×5 / 173cm 例外档）。

---

<a id="db-source-line-8"></a>
## §A 参数→机制→练习映射表（§4 六参数，`[归纳]`）

| P | 参数（§4） | 默认 | 机制作用 | 可判定自查（§8.2） | 练习落点 | 失效/越界 |
|---|---|---|---|---|---|---|
| P1 | 自传具体度 L92 | **80%** | 定「是不是卡罗」；具体事件/人物密集指涉 ≥2 件 | §8.2-2 L250 自传指涉物 ≥2（事故/手术/迭戈/民族服饰/宠物） | 阶梯1「4 符号 + 每符号一行生平对应」 | 弱档=通用肖像/静物（无差别肖像档）；若 P1 强但整体读成梦 → 反例C 张力 |
| P2 | 民间色彩强度 L93 | **75%** | 底盘：民间色平涂块面（洋红/钴蓝/翠绿/黄/血红） | §8.2-3 L251 色相簇 6–9 / ≥3 区饱和 ≥60% / 色区内方差 ≤5% | 阶梯1 背景=单色/植被平面 | 弱档=低饱和欧式色域（学院档）；与马蒂斯「快乐平涂大色块」区分（§3.1 L85） |
| P3 | 象征身体密度 L94 | **70%** | 符号强度：打开的/被替代的身体（外露心脏、钉柱、鹿身、分裂双身） | §8.2-2 / §8.2-7 L255 动物/植物/首饰符号 ≥2 类且焦平面内 | 阶梯1 蜂鸟坠饰 / 荆棘项链 / 双猴 | 弱档=身体完整无器官符号（早期肖像档）；符号只是装饰→违反 §8.1 L239 |
| P4 | 正面凝视/镜像度 L95 | **80%** | 定「是不是卡罗」（含双身变体）；自我作为可反复进入的图像现场 | §8.2-1 L249 面轴 ≤10° / 瞳孔 ±15° | 阶梯2 两轴互查表 + 直视保持 | 弱档=侧身/低头/回避对视；字面化成「必须画镜子」=误读 |
| P5 | 服饰与纹样密度 L96 | **70%** | 身份符号：全套 Tehuana/huipil + 玉石珠链 + 发花 | §8.2-7 L255 ≥2 类符号清晰呈现 | 阶梯1 Tehuana 装束 | 弱档=素衣/西装（*Cropped Hair* 反常档，§12 #5） |
| P6 | 画幅与观看距离 L97 | **85%** | 底盘：还愿画级小画幅（30–60cm）+ 近距单人对视 | §8.2-6 L254 人物数=1（≥90% 帧）/ 主体占高度 40–70% | 阶梯3「两个我」+ 一行例外档标注 | 弱档=大画幅远观（**越界：壁画档/里维拉**）；**例外档见 §C** |

> 用法（§4 L99，卡 L70）：**P1/P4 定「是不是卡罗」；P3/P5 定身体与身份的符号强度；P2/P6 定民间色彩与小画幅的底盘**。§8.1 中文说明 L238「定调三件套」= P1 80% / P4 80% / P6 85%（卡 [kahlo.md](../../modules/kahlo.md) 同值）。**档位划分本身为 `[归纳]`**（L100），阈值未经渲染实验校准（L320）。

<a id="db-source-line-21"></a>
## §B §8.2 八规则逐条（卡 [kahlo.md](../../modules/kahlo.md) L46–55 逐字一致，`[归纳]`）

| # | 规则 | 默认阈值 | 对应参数 | 本 shard 状态 |
|---|---|---|---|---|
| 1 | 正视性 | 面轴与垂直中轴 ≤10°；瞳孔 ±15° | P4 | 纸面承接，未测量 |
| 2 | 自传指涉物计数 | ≥2 个可识别生平符码物 | P1 | 纸面承接；「1 件具体+通用原型」混合区未被覆盖（反例B） |
| 3 | 民间色与平涂 | 色相簇 6–9 / ≥3 区饱和 ≥60% / 区内方差 ≤5% | P2 | 纸面承接，未直方图实测 |
| 4 | 硬边/无羽化 | 过渡带 ≤2px @1024；禁 ≥8px 羽化 | P2 | 纸面承接 |
| 5 | 背景压缩 | 纵深 ≤2 平面；无收敛透视；植被/幕布 ≥60% | P6/构图 | 纸面承接 |
| 6 | 单人·画幅语义 | 人物数=1（≥90% 帧）；主体占高度 40–70%；裁切 ≤1 | P6 | 纸面承接 |
| 7 | 符号清晰呈现 | 动物/植物/首饰 ≥2 类，均焦平面、边缘清晰度 ≥主体 80% | P3/P5 | 纸面承接 |
| 8 | 全片静止（动画档） | 帧间差 ≤1%；仅花/鸟微动 ≤2%（可选） | — | 纸面承接；本 shard 无动画产物 |

> 第 2 条依赖 §5/§12 建立的**生平符码表**（事故-飞床 / 手术-断柱 / 迭戈-肖像坠饰 / 民族-服饰 / 宠物-猴与鹦鹉，L258、卡 L57）。全部阈值 `[归纳]`、未对原作做像素测量（L258、L320）。

---

<a id="db-source-line-38"></a>
## §A-SYMBOL 自画像符号系统：蜂鸟（档案内）vs monobrow（外部标志）

| 项 | 证据级 | 定位 | 在机制中的位置 |
|---|---|---|---|
| **蜂鸟 hummingbird pendant** | `[研究]`（档案内符号） | [kahlo.md](../../dossiers/kahlo.md) §2-8 L54（符号编制清单含「蜂鸟」）、§12 #2 L387–390（「蜂鸟坠饰（悬停的生死双重符号）」）、§8.1 正向 L218 `a hummingbird pendant`、[kahlo.md](../../modules/kahlo.md) L26 同值、§0 L20 作品名 *Self-Portrait with Thorn Necklace and Hummingbird*（[R14] HRC） | 具体作品的可命名指涉物；计入 §8.2-2「≥2」与 §3.1 L78「具体事件指涉物 ≥2 件→卡罗档」；归 P3 象征身体密度 |
| **monobrow / 一字眉 / unibrow** | `[史料-转引]`（外部文化标志，**档案 §1 未列**） | 本机唯一逐字命中 `_scratch/kahlo/pages/wiki_kahlo.wiki` L282：2018 Mattel Barbie「noticeably missing [[unibrow]]」（NYT 2018-03-09 转引）。**[kahlo.md](../../dossiers/kahlo.md) §1 十二条视觉指纹 L31–42 未逐字列 monobrow；§4 六参数、§8.1 正向段、§8.2 八规则亦无它** | 作为「大众辨识度最高的自画像标志物」承接；**不写成档案内已证符号、不补进模块卡、不单独满足「≥2 指涉物」、不升级为 supported 档案断言** |

**为什么这个区分是机制问题而非考据洁癖**：§3.1 L76 / §8.1 L240 要求符号「需生平词典才能解码」。蜂鸟坠饰有具体作品与馆方来源可回指；monobrow 在本机只有一条大众文化转引，无档案内符号学定位。把两者混为同一证据级，会污染 §8.2-2 的「≥2 可命名指涉物」计数，也会把 `[归纳]` 判据伪装成 `[研究]` 事实。学习路径阶梯1 用「4 符号 + 每符号一行生平对应」的练习把这条边界变成可操作自检。

---

<a id="db-source-line-49"></a>
## §B-DIVISION 镜像 vs 里维拉互查（写死条款，`[归纳]`，可被组合实验推翻）

**镜像轴（P4）** — 正面凝视 / 以镜作画：
- [kahlo.md](../../dossiers/kahlo.md) §1-2 L32（正面/近正面、目光直视；「病床上方装镜、以镜作画」，MoMA 'alter and extend her field of vision'）；§2-3 L49（镜像工作法成为构图机制本身，*Fulang-Chang and I* 画+镜成对）；§11 L331（1925 事故卧床 → 床帐上方装镜 → 1926 第一幅自画像）；§8.1 正向 L213；§7 L178 轴③「正面镜像凝视（自我作为可反复进入的图像现场）」；卡 [kahlo.md](../../modules/kahlo.md) L9。

**里维拉轴（P6 + 分工注）** — 私密小幅 vs 公共巨幅：
- §3.1 L80–84「写死；来源 roster §2.12/§3 + wave15 brief；`[归纳]`，可被组合实验推翻」。L81 MoMA 对照句「her intimate scale… sharply contrasted with the work of her contemporaries, the Mexican Muralists」；L82 里维拉＝壁画/纪念碑尺度、多人群像、公共建筑、民族历史。
- **四条判据 ≥3 归判（L83）**：① 尺度/观看距离（小画幅近距 vs 米级公共远观）② 题材域（私人事件 vs 集体历史）③ 构图（正面单人+压缩舞台 vs 多人群像+深空间）④ 功能（自传私物 vs 公共教育/纪念碑）。
- **组合纪律（L84）**：默认不并置；组合须显式分区并保留各自标志（卡罗：正面镜像+符号身体；里维拉：群像+历史叙事），不得互相吞并。§4 分工注 L101：「公共巨幅＋群像＋历史叙事」整体属里维拉模块，**禁止在本模块同档出现**；需要大场景时不得同时保留本模块「正面单人＋符号身体」标志机制。

**另一条分工（蒙克，carried）** — §3.1 L75–79：卡罗＝具体自传符号系统（需生平词典）vs 蒙克＝普世焦虑原型语法（无需生平）；符号可解码性测试 + 「具体事件指涉物 ≥2 件→卡罗档」（L78）；同屏须显式分区、默认二选一（L79）。卡 [kahlo.md](../../modules/kahlo.md) L78–79 落为冲突注记。

**互查表（本 shard 记录，不渲染）**：生成前对每件作品同时填两轴——左「蒙克：是否需生平词典 / 具体指涉物 ≥2？」右「里维拉四条各落哪档？」。两轴独立于 P4/P6 数值，都是 `[归纳]` 规则层。

---

<a id="db-source-line-65"></a>
## §C-EXCEPTION Las dos Fridas 173cm × §4-P6 例外档（专节）

| 事实 | 定位 |
|---|---|
| 尺寸例外 ≈173×173 cm（《Las dos Fridas》）、≈76 cm（《Trotsky》） | [kahlo.md](../../dossiers/kahlo.md) §1-9 L39 |
| §4-P6 强档写死：「例外：《Las dos Fridas》式双身巨幅须**显式标注为『例外档』**」 | §4-P6 L97；卡 [kahlo.md](../../modules/kahlo.md) L68 同值 |
| §3.1 vs 里维拉：「个别例外如《Las dos Fridas》约 173 cm 仍属『近观/私密语义』档」 | §3.1 L81 |
| 自审 B3：初稿「小画幅（30–60 cm）是模块身份」→ **WEAKENED** → 增设「例外档」；判据改为**语义**（私密/近观）非绝对尺寸 | §自审 B3 L437（指向 §1-9 / §4-P6 / §3.1） |
| 尺度语义：「以『私密/近观』为准，非绝对尺寸」 | §1-9 L39 |

**反例A（AUDIT counterexample.md L6–18，`[inference]` 纸面，carried as resolved exception）**：把 173cm 喂给四条判据（L83）——① 尺度=米级 → 里维拉档；② 题材域=双身/身份谈判/婚姻 → 卡罗档；③ 构图=正面并置双身+压缩雷云背景（非多人群像深空间）→ 卡罗档；④ 功能=自传性私物 → 卡罗档 → **3/4 归卡罗档**。§4-P6 已预置例外档，§1-9/L437 已把尺度弱化为语义，故**未推翻机制、命中预置例外档、机制自洽**。`review-evidence.md` §5 由独立审者逐条复核 L39/L97/L81 与反例A 一致。**本 shard 采信为已决例外档事实，不重新论证、不改成「无例外」、不渲染验证。**

**真正的压力点（反例A 标注，本次未验证）**：若一件作品同时「尺度米级 + 群像 + 历史叙事 + 公共墙」（四条全落里维拉）却仍带「正面单人+符号身体」（卡罗标志），则 §4 L101 与 §3.1 L84 要求拆图/分区；该边界标 `[inference]`、「可被组合实验推翻」（L73/L79），需 E 系列实验定值，本 shard 不补阈值。

**练习侧强制动作**：凡画「两个我」/双身巨幅，练习记录必须写一行「本作按 §4-P6 例外档标注（近观/私密语义，非 30–60cm 常规档）」——静默按 P6 弱档（大画幅→越界壁画档）处理即违反 L97 的显式标注要求（learning_path 阶梯3、how-to-think D4）。

---

<a id="db-source-line-83"></a>
## §D 失败条件 / 反例账（全部 `[inference]` 纸面，来自 AUDIT counterexample.md）

| CE | 对象 | 判定 | 机制含义 |
|---|---|---|---|
| 反例A L6–18 | 173cm × 四条判据 + §4-P6 | **命中预置例外档，未推翻，机制自洽** | §C；P6 判语义不判 cm；例外档须显式标注 |
| 反例B L20–26 | 符号可解码性测试（L78）「1 件具体 + 通用原型」混合区 | **判据未覆盖的缺口**（指定可推翻点） | §8.2-2 的「≥2 / 全部通用」二分未覆盖混合区；待 E 系列组合实验定值，本 shard 不补阈值 |
| 反例C L28–32 | P1 强档但整体被读成「梦/超现实」 | **张力已被 §8.1 越界警报 L240–242 缓解，未判推翻** | `--no dream surrealism` 是护栏非历史断言（L243）；P1 强档与身份护栏同段共存但无优先级，记录不裁定 |

诚实口径（AUDIT counterexample.md L3/L36–38、rights_review.md §边界）：3 则全为 `[inference]`、纸面、无帧、无像素、无真人练习；`conflict`/`unverified` 未伪装成 `supported`；可推翻点均自标 `[归纳]` 且「未经渲染实验校准」（L100/L320）。本 shard 未重跑、未渲染、未假装已核。

---

<a id="db-source-line-95"></a>
## §E 权利 / 事实边界（fact(已决)，不越权）

- **images_public=0 是事实非缺陷**（AUDIT RESULT §2、coverage-manifest.json `images_public:0` / `images_private:13`）。定位：`_images/manifest.md` L7（「kahlo / kngwarreye 公开 0——全私有」）、L3161（同口径）、**L3185**（`| kahlo | 0 | 13 | 全部版权未清（© Fideicomiso/ARS）…` 逐件列 13 件）、ledger `images_public=0, images_manifest=false`、[kahlo.md](../../dossiers/kahlo.md) §0 L5 / §10-1 L313。
- **images_manifest=false 的准确含义**：「无公开侧 manifest 行」，非「缺文件」（AUDIT claim IMG-MANIFEST-FALSE、coverage-manifest.json `images_public_note`）。公开侧 kahlo 行 = 0，rights_review.md §public image rows 如实记为空集。
- **NMWA 权利行证据**：`AUDIT-kahlo/raw/nmwa_trotsky.html`（HTTP-200，463535 B，sha `d6d8fdb21f1171cc51883f715133188f720a21b6d45007d1d2346a892800ea59`）grep 命中 `© Banco de México Diego Rivera Frida Kahlo Museums Trust, Mexico, CDMX/Artists Rights Society (ARS), New York` **×5**；rights_review.md L15 逐字登记、review-evidence.md §4 独立审者复核 ×5；dossier §0 L5 权利主体、§9 交叉3 L306「NMWA/MoMA/HRC 三馆权利行一致」。**本 shard 仅承接本地缓存字节 + 已复核结论，未重新联网、未做 image_seen、不升级 claim。**
- **13 张私有件处置**：统一「未清 / 仅私有层研究，不公开引用其路径」（rights_review.md §逐件 rights 表 L24–38、§边界 L46–50）。不猜 PD、不编造 CC 署名；公开引用只给馆藏页/文件页 URL。MoMA 403 Cloudflare / Time 订阅 / AAA 快照 3 源不可达（risk_fetch.md）诚实标注，但权利结论锚定 manifest + dossier + NMWA live 页，不受影响。

---

<a id="db-source-line-104"></a>
## §F 已知漂移 / 未覆盖（沿用 AUDIT 口径，只报告不修）

- **conflicts.md 零 kahlo 专属 C 行**：AUDIT locator_drift.md / claim S3.1-OTHER — `grep -i kahlo/卡罗/弗里达` 于 conflicts.md 零命中（review-evidence.md §6 复核 0 hits, exit 1）；相关 C 仅为卡片 L80 指针 C-05(L109)/C-12(L203)/C-14(L229)。
- **D1/D2 near-miss 计数漂移**：卡 L85「near-miss 8 对」vs conflicts.md §4 实际 **11 行**；§C L365 自审仍写 8。AUDIT **只报告不修**（repo READ-ONLY），本 shard 不改 conflicts.md、不改 AUDIT 产物。
- **不可达源**：MoMA（403 Cloudflare）/ Time（订阅）/ AAA（快照）3 项标 unavailable/partial；相关 `partial` claim 若后续可达，需重取并记 retrieved_bytes_sha256 才能升级（AUDIT RESULT §next action）。
- **§8.2 八规则 / §4 六参数**阈值全部 `[归纳]`、未经渲染/组合实验校准（L100/L320/§10-8）；本 shard 未渲染、未像素测量、未跑八规则自查。反例B 混合区阈值、反例C 优先级均未定义，不擅自补。
- **练习效果**：全部建议练习，无 human review、无真人学习成效数据，不写「已证实学习收益」（`01-AUDIT.md` §8.1 L273）。

---

<a id="db-source-line-114"></a>
## §G 收口

- §4 六参数 / §8.2 八规则 / §3.1 两条分工判据 / §4-P6 例外档 / 5 个 brief 强调点全部落位并标等级；`fact(已决)` 与 `[归纳]` / `[inference]` / `[史料-转引]` 严格分离。
- 本文件为机制与参数说明，不含 prompt 模板；决策序在 [how-to-think.md](how-to-think.md)、练习顺序在 [learning_path.md](learning_path.md)、逐 claim 定位在 [claim_evidence_map.md](claim_evidence_map.md)。
- `review:null`、`human_review.status=not_applicable`；作者不自接受，待独立审者复验 5 产物 hash 与定位。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [claim_evidence_map.md](claim_evidence_map.md)
- [source-claims.json](source-claims.json)
