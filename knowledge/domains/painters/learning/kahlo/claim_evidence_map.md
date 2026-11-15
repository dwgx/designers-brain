<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-kahlo；原正文 SHA-256 `a7e8ae10136114669d44c0e623a217944bfc7f3be7408b6b16fbaaee39a79940`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-kahlo — claim_evidence_map

> A-30 Lane B · artist `kahlo` (A-48) · 依赖 ACCEPTED 内部证据 ddc7ed9c8499317c（未公开；来源记录由维护者保留）（review-evidence.md verdict=PASS，复用 locator 纪律，不重审）。
> repo 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22` READ-ONLY；本表为 staging 内建议文本，无仓库写、无联网复核。
> `locator` 口径：`<repo相对路径>:L<行号>|<章节/标题>`；外部执行包文档标 `<package>/<file>:L<行号>`；staging 依赖标 内部证据 4108383d7cf77267（未公开；来源记录由维护者保留）。
> `grade`：档案自标 `[自述]/[史料]/[研究]/[归纳]/[推测]`（dossier L5）+ 本 shard 增用 `[史料-转引]`（外部文化标志，档案 §1 未列）与 `fact(已决)`（AUDIT 已独立复核）。
> `support_status`：`supported`（本机档案/缓存可回源命中）/ `partial`（档案内转引或外部标志、未直读一手）/ `not_applicable`（建议练习/规则层）。

---

<a id="db-source-line-11"></a>
## §A 输入与依赖（hash 开工实跑，与 ledger 一致）

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-IN-DOSSIER | fact | supported | [kahlo.md](../../dossiers/kahlo.md) 全文 | `[史料]` | 实跑 sha256 `2a238801778873d3af7a7987e7eadda324b053619bef85442a46f6613f844f34`，与 ledger `dossier_sha256` / AUDIT claim_evidence_map.md 抬头一致 |
| LK-IN-CARD | fact | supported | [kahlo.md](../../modules/kahlo.md) 全文 | `[史料]` | sha `738045da3831678544eafcf7327dae2b37ce071202ec6b5e775a3868b0fa35da`；`_extract.py --check` 228/228（AUDIT RESULT §2） |
| LK-IN-CORPUS | fact | supported | [kahlo.md](../../dossiers/_corpus/kahlo.md) 全文 | `[史料]` | sha `04fa85c61e8ecb0a3e344a3a1dac8cc9c7bae693d72247ffdec0921aa2d27ae0`；`grep -c '^### '`=24（AUDIT review-evidence §2） |
| LK-AUDIT-ACCEPTED | fact | supported | 内部证据 048585725a4e6868（未公开；来源记录由维护者保留） | `[史料]` | 独立审者 glm-5.3-flash 判 **PASS**；74 行 50/24、74/74 locator、7 fetch sha、NMWA 权利行 ×5、173cm 例外档逐条复核 |

<a id="db-source-line-20"></a>
## §B 自画像符号系统（monobrow / hummingbird）— brief 强调点 1

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-SYM-HUMMINGBIRD | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L54\|§2-8 符号编制（清单含「蜂鸟」）`；`L218\|§8.1 正向 a hummingbird pendant`；`L387–390\|§12 #2 蜂鸟坠饰（悬停的生死双重符号）`；`L20\|§0 作品名 Self-Portrait with Thorn Necklace and Hummingbird`；`knowledge/domains/painters/modules/kahlo.md:L26` | `[研究]` | 蜂鸟是**档案内**可回源自传符号：具体作品 [R14] HRC 的可命名指涉物，计入 §8.2-2「≥2」与 §3.1 L78「具体事件指涉物 ≥2→卡罗档」；归 P3 象征身体密度。本 shard 逐字命中 5 处 |
| LK-SYM-SYSTEM | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L54\|§2-8 把物件排布成句`；`L76\|§3.1 符号必须知道生平才能解码`；`L239–240\|§8.1 中文说明 符号必须可解码/要求生平词典`；`L250\|§8.2-2 自传指涉物 ≥2`；`L255\|§8.2-7 符号 ≥2 类` | `[研究]` + `[归纳]` | 符号系统 = 逐件摆放成可解码图句；§8.2 计数阈值是 `[归纳]`，不冒充作者内心 |
| LK-SYM-MONOBROW-EXTERNAL | observation | **partial** | `knowledge/domains/painters/_scratch/kahlo/pages/wiki_kahlo.wiki:L282`（2018 Mattel Barbie「noticeably missing [[unibrow]]」，NYT 2018-03-09 转引）；对照 `knowledge/domains/painters/dossiers/kahlo.md:L31–42\|§1 十二条视觉指纹（未逐字列 monobrow）`、`L92–97\|§4 六参数（无）`、`L212–223\|§8.1 正向段（无）`、`L247–256\|§8.2 八规则（无）` | `[史料-转引]` | **诚实降级**：monobrow 是大众辨识度最高的自画像标志物，本机唯一逐字命中在 scratch 维基；**档案 §1 未列、非 §4 参数、不冒充档案内已证符号、不补进模块卡、不单独满足「≥2 指涉物」**。与蜂鸟的差别正是阶梯1 要教的分级 |
| LK-SYM-SELF-INTENT | fact | supported | `knowledge/domains/painters/dossiers/_corpus/kahlo.md:L33–38\|#4「我常独处，所以我画自己」[self-written]`；`L24–29\|#3「我自己最坦率的表达」[self-written]`；`knowledge/domains/painters/dossiers/kahlo.md:L109\|§5-1「我从未画梦，我画的是我自己的现实」` | `[自述]` | 作者自述支持「自画像＝自我作为主语」的**意图**；不提供任何符号清单数值（数值全 `[归纳]`） |
| LK-SYM-GUARDRAIL | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L229\|§8.1 负向 --no dream surrealism`；`L243\|「模块护栏，不是历史断言」`；`L240\|越界警报 vs 蒙克` | `[归纳]` | `--no dream surrealism` 是身份护栏非历史断言；符号不得退化为「无需生平即可读」的通用情绪原型 |

<a id="db-source-line-30"></a>
## §C 镜像 vs 里维拉互查 — brief 强调点 2

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-MIRROR | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L32\|§1-2 正面凝视＋镜像构图（床上方装镜、以镜作画，MoMA 'alter and extend her field of vision'）`；`L49\|§2-3 镜像工作法（床+镜）`；`L331\|§11 1925 卧床装镜→1926 第一幅自画像`；`L213\|§8.1 正向 staring directly at the viewer`；`knowledge/domains/painters/modules/kahlo.md:L9` | `[研究]` | 镜像＝自我作为可反复进入的图像现场（§7 L178 轴③）；参数化为 P4 |
| LK-MIRROR-P4 | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L95\|§4-P4 正面凝视/镜像度 默认 80%（含双身变体）`；`L99\|§4 用法 P1/P4 定是不是卡罗`；`L249\|§8.2-1 面轴 ≤10°/瞳孔 ±15°`；`knowledge/domains/painters/modules/kahlo.md:L66` | `[归纳]` | P4 数值与自查阈值是研究者规则；双身只是「镜像结构变体」（L37），不是「必须画镜子」 |
| LK-DIV-RIVERA | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L80–84\|§3.1 vs 里维拉（写死；私密小幅 vs 公共巨幅）`；`L81\|MoMA 'intimate scale… sharply contrasted with the Mexican Muralists'`；`L83\|四条判据 ≥3 归判`；`L84\|显式分区、不得互相吞并`；`L101\|§4 分工注 禁公共巨幅+群像+历史叙事同档` | `[归纳]`（MoMA 句 `[研究]` 转引） | 写死条款 L73 自标「`[归纳]`，可被组合实验推翻」；四条判据=尺度/题材域/构图/功能 |
| LK-DIV-MUNCH | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L75–79\|§3.1 vs 蒙克`；`L78\|符号可解码性测试 + 具体事件指涉物 ≥2→卡罗档`；`knowledge/domains/painters/modules/kahlo.md:L78–79` | `[归纳]` | carried 的第二条分工；与里维拉轴共同组成阶梯2「两轴互查表」 |
| LK-DIV-CROSSCHECK | design_candidate | not_applicable | 内部证据 4ff3cd691a0692ea（未公开；来源记录由维护者保留）；本 shard `learning_path.md §4 阶梯2` / `how-to-think.md D3` | `[inference]` | 生成前同时过蒙克/里维拉两把尺是**本 shard 建议决策程序**，非档案既有条款；反例B 混合区（1 件具体+通用原型）未被 L78 覆盖，待实验定值 |

<a id="db-source-line-40"></a>
## §D Las dos Fridas 173cm × §4-P6 例外档 — brief 强调点 3

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-P6-EXCEPTION | fact | supported | `knowledge/domains/painters/dossiers/kahlo.md:L97\|§4-P6 强档「例外：《Las dos Fridas》式双身巨幅须显式标注为『例外档』」`；`L39\|§1-9 约 173×173 cm / Trotsky 约 76 cm`；`L81\|§3.1 个别例外仍属近观/私密语义档`；`L437\|§自审 B3 WEAKENED→增设例外档、判据改语义非绝对尺寸`；`knowledge/domains/painters/modules/kahlo.md:L68` | `[归纳]` + `fact(已决)` | 例外档文本与 B3 弱化为档案写死规则层；AUDIT review-evidence §5 逐条复核 L39/L97/L81 一致 |
| LK-P6-COUNTEREXAMPLE-A | observation | partial | 内部证据 266429c75d9f5104（未公开；来源记录由维护者保留）；内部证据 902800881002838f（未公开；来源记录由维护者保留） | `[inference]` | 173cm 过四条判据：①尺度→里维拉 ②③④→卡罗 → **3/4 归卡罗**，命中 §4-P6 预置例外档、机制自洽、未推翻。整体仍 `[inference]` 纸面、未渲染；本 shard 采信已决例外档事实、不重新论证 |
| LK-P6-PRESSURE-POINT | observation | partial | 内部证据 1d968ce2b49c6615（未公开；来源记录由维护者保留）；`knowledge/domains/painters/dossiers/kahlo.md:L73\|§3.1 可被组合实验推翻`、`L79`、`L101` | `[inference]` | 「尺度米级+群像+历史叙事+公共墙」四条全落里维拉却保留卡罗标志 → 须拆图/分区（L84/L101）；本次未渲染验证，指定可推翻点 |

<a id="db-source-line-48"></a>
## §E images_public=0 + NMWA 权利行 — brief 强调点 4 / 5

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-IMG-PUBLIC-0 | fact | supported | `knowledge/domains/painters/dossiers/_images/manifest.md:L7\|kahlo/kngwarreye 公开 0——全私有`；`L3161\|同口径`；`L3185\|` | `[史料]` | `images_public=0` **是事实非缺陷**（AUDIT RESULT §2、coverage-manifest.json `images_public:0`）；公开侧 kahlo 行=0，rights_review.md §public image rows 如实记空集 |
| LK-IMG-MANIFEST-FALSE | fact | supported | 内部证据 7804a795bc2ce6d6（未公开；来源记录由维护者保留）；内部证据 e811fd28d865348a（未公开；来源记录由维护者保留）；内部证据 1ddc543e332468f8（未公开；来源记录由维护者保留） | `[史料]` | `false` 意为「无公开侧 manifest 行」非「缺文件」；与 dossier §5 L5 / §10-1 L313「公开侧只列作品清单+馆藏链接，不嵌图」一致 |
| LK-IMG-PRIVATE-13 | fact | supported | `knowledge/domains/painters/dossiers/_images/manifest.md:L3185\|逐件列 13 件`；内部证据 a434a8dba3cd37d8（未公开；来源记录由维护者保留）；`knowledge/domains/painters/dossiers/kahlo.md:L5\|§0 版权声明` | `[史料]` | 13 张私有研究副本统一「未清 © Fideicomiso/ARS」；本 shard image_seen=0、read_scope=metadata，不读私有层本体、不猜 PD、不编造 CC 署名 |
| LK-NMWA-RIGHTS-LINE | fact | supported | 内部证据 6e5c91486e84ed93（未公开；来源记录由维护者保留）（HTTP-200，463535 B，sha `d6d8fdb21f1171cc51883f715133188f720a21b6d45007d1d2346a892800ea59`）；内部证据 2ee5b3e6c9a59317（未公开；来源记录由维护者保留）；内部证据 f2cbc964662519ef（未公开；来源记录由维护者保留） | `[史料]` + `fact(已决)` | grep 命中 `© Banco de México Diego Rivera Frida Kahlo Museums Trust, Mexico, CDMX/Artists Rights Society (ARS), New York` **×5**；独立审者复核 ×5；dossier §0 L5 / §9 交叉3 L306「NMWA/MoMA/HRC 三馆权利行一致」。本 shard 仅承接本地缓存字节，未重新联网 |
| LK-RIGHTS-CONSISTENCY | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L306\|§9 交叉3 三馆权利行一致`；`L313\|§10-1 统一按未清处理`；内部证据 9d6a940ec708ea46（未公开；来源记录由维护者保留） | `[史料]` | 权利结论锚定 manifest + dossier + NMWA live 页；MoMA 403 / Time 订阅 / AAA 快照 3 源不可达（risk_fetch.md）诚实标注，不影响权利结论 |

<a id="db-source-line-58"></a>
## §F 参数 / 规则层（全部 `[归纳]`，未经渲染实验校准）

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-PARAM-6 | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L92–97\|§4 六参数 P1–P6`；`L99\|用法`；`L100\|档位划分本身为 [归纳]`；`knowledge/domains/painters/modules/kahlo.md:L61–72` | `[归纳]` | 默认值 P1=80/P2=75/P3=70/P4=80/P5=70/P6=85；卡侧逐字一致（_extract.py 228/228） |
| LK-RULES-8 | observation | supported | `knowledge/domains/painters/dossiers/kahlo.md:L247–256\|§8.2 八规则`；`L258\|全部阈值 [归纳]`；`L320\|§10-8 未实测`；`knowledge/domains/painters/modules/kahlo.md:L46–55` | `[归纳]` | 八规则逐帧自查；本 shard 纸面承接、未跑自查、未像素测量 |
| LK-§12-PRACTICES | design_candidate | not_applicable | `knowledge/domains/painters/dossiers/kahlo.md:L380–418\|§12 九件临摹/学习清单（看什么/学什么/怎么练）` | `[研究]` 作品 + `[归纳]` 练习 | 三段阶梯（符号→镜像/分工→例外档+权利）由 §12 现有清单**组织**而来，练习为**建议练习**；`01-AUDIT.md` §8.1 L273 不写「已证实学习收益」、`human_review.status=not_applicable` |
| LK-EXTRACT-SAMENESS | fact | supported | 内部证据 8823a61a7434a1dd（未公开；来源记录由维护者保留）；`knowledge/domains/painters/modules/kahlo.md:L5` | `[史料]` | 卡 §8.1/§8.2/§4 与档案逐字一致；GatesRepair 对 `_extract.py` 的工作树改动属另一 lane，228/228 锚定本次实跑内容 |

<a id="db-source-line-67"></a>
## §G 失败 / 漂移 / 边界（沿用 AUDIT 口径，只报告不修）

| claim_id | claim_kind | support_status | locator | grade | basis |
|---|---|---|---|---|---|
| LK-CE-B | observation | partial | 内部证据 4ff3cd691a0692ea（未公开；来源记录由维护者保留）；`knowledge/domains/painters/dossiers/kahlo.md:L78\|L78 二分` | `[inference]` | 「1 件具体指涉物 + 通用原型」混合区未被 L78 覆盖；待 E 系列组合实验定值，本 shard 不补阈值 |
| LK-CE-C | observation | partial | 内部证据 3aae7524040c2ee3（未公开；来源记录由维护者保留）；`knowledge/domains/painters/dossiers/kahlo.md:L240–243\|越界警报/护栏/组合建议` | `[inference]` | P1 强档但整体读成「梦」→ 张力已被护栏缓解、未判推翻；本 shard 不裁定优先级 |
| LK-CONFLICTS-ZERO | fact | supported | [conflicts.md](../../../../cross/conflicts.md)（全文）；内部证据 615c2ab62d1e9335（未公开；来源记录由维护者保留）；内部证据 ed05d305bc6cd0ac（未公开；来源记录由维护者保留） | `[史料]` | `grep -ic "kahlo\|卡罗\|弗里达"`=0（exit 1）；相关 C 仅为卡片 L80 指针 C-05(L109)/C-12(L203)/C-14(L229)；D1/D2 near-miss 计数漂移（卡 L85「8 对」vs 实际 11 行、§C L365 仍写 8）AUDIT **只报告不修**，本 shard 不改 |
| LK-UNREACHABLE-SOURCES | fact | partial | 内部证据 fc0abd4af4561824（未公开；来源记录由维护者保留）；内部证据 ab1e9717abbcab66（未公开；来源记录由维护者保留）；内部证据 161719b25e77ccc9（未公开；来源记录由维护者保留） | `[史料]` | 7 HTTP-200 源 + MoMA 403 / Time 订阅 / AAA 快照 3 项诚实 unavailable/partial；相关 `partial` claim 若后续可达需重取并记 retrieved_bytes_sha256 才能升级 |
| LK-SUGGESTED-PRACTICE | design_candidate | not_applicable | `<package>/01-AUDIT.md:L273\|§8.1`；内部证据 555645ed2138c022（未公开；来源记录由维护者保留） / `learning_path.md §0` | `[史料]` | 全部练习为建议练习；无 human review、无真人学习成效数据；`review:null`、作者不自接受 |

---

<a id="db-source-line-79"></a>
## 收口

- brief 5 个强调点逐条落位：§B（monobrow/hummingbird 分级）、§C（镜像 vs 里维拉互查）、§D（173cm §4-P6 例外档）、§E（images_public=0 + NMWA 权利行 ×5）。
- 全部 `fact/observation + supported` 的 claim 均有本机档案/缓存 locator 或 AUDIT 独立复核结论；`partial` 项（monobrow 外部标志、反例A/B/C `[inference]`、不可达源）如实降级、`not_applicable` 项（建议练习）不冒充学习成效。
- 本表复用 AUDIT [claim_evidence_map.md](claim_evidence_map.md) 74 行 50/24 的 locator 纪律，不重审；本 shard 为 `submitted`，待独立审者复验 5 产物 hash 与定位。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
