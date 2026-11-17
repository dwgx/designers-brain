<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-fan_kuan；原正文 SHA-256 `fc64ed5c68755126d3e484b5902f16fb52384d7c263e8aa34e012d6f29a838ef`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-fan_kuan — Claim–Evidence Map（逐 claim 带 `文件 : 节 : 行号` 定位）

> 证据底本：内部证据 d1cb1fe5c1a7bc81（未公开；来源记录由维护者保留）（ACCEPTED；RESULT.md / claim_evidence_map.csv 135 行 / counterexample.md / rights_review.md / quote_audit.md / coverage-manifest.json）。**复用不重审**，沿用其 `文件 : 节 : 行号` 定位纪律。基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（READ-ONLY）。
>
> 定位口径：repo 相对路径 `knowledge/domains/painters/...` 行号指**本机当前工作树**（AUDIT §2 逐字一致，sha256 已现场复核与 ledger 一致）；内部证据 caf055ff828e1306（未公开；来源记录由维护者保留） 为 ACCEPTED 审计产物行号。read_scope 全为 `sections`（本机档案节选 + 依赖底本节选），未做 `fulltext` 外部回源、未做 `image_seen`（AUDIT §3 image_seen=0）。`[自述]`/`[史料]`/`[研究]`/`[归纳]`/`[推测]` 级别照录档案。
>
> 本文件是 LEARN shard 自产 claim 的定位索引（A–F 组），与 `receipt.json` 的 `claims[]` 一一对应；不改写 AUDIT 的 135 行 claim map。练习类断言（E 组）标 `not_applicable`，不冒充已验证（见 §F 边界）。

---

<a id="db-source-line-11"></a>
## §A 组 — 结构性事实与术语史（brief 强调：OVERTURNED / FK-B-02）

| claim_id | 断言 | 级别 | support | 定位（文件 : 节 : 行号） |
|---|---|---|---|---|
| LFK-A1 | 范宽无文字传世；Q1/Q2「自述」均宋/元人转述，不得写「范宽写道」 | `[史料]` | supported | [fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : 文件头 L4「`[self-reported]`＝本人之语（**经宋人转述**——范宽无文字传世）」+ 缺口 L199；[fan_kuan.md](../../dossiers/fan_kuan.md) : §5 标题 L108「『自述』均为宋元人转述」+ §10-9 L273；内部证据 e915934ba699da34（未公开；来源记录由维护者保留） : L11 |
| LFK-A2 | 郭若虚《圖畫見聞誌》北宋同代判语「搶（上聲）筆俱均」「以墨籠染…鐵屋」（密点短笔**操作**有据） | `[史料]` | supported | [fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q6 L50（原文）/ L53（白话）/ L54（备注）；[fan_kuan.md](../../dossiers/fan_kuan.md) : §2-1 L42、§5-5 L122–123；内部证据 0d87d3fbe3e6a2ac（未公开；来源记录由维护者保留） : FK-S2-01 L12 / FK-Q06 L100 |
| LFK-A3 | **OVERTURNED**：「雨点皴」之名出明代著录（陈继儒《妮古录》/唐志契《绘事微言》/汪珂玉《珊瑚网》/朱谋垔《画史会要》），北宋文献只称「枪笔」；「操作先于名称」 | `[研究]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §10-4 L268、§自审 B-2 L391、§1-2 L30；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §4.2（artouch 刘芳如文逐字，HTTP 200）/ claim_evidence_map.csv : FK-W-02 L133 / FK-S1-02 L3(partial) / FK-B-02 L91(conflict) |
| LFK-A4 | **FK-B-02 为开放项**：郭若虚「槍筆」× 明代「雨点皴」的术语层对应在 `conflicts.md` 无 fan_kuan 专属行可挂（grep 0 命中，wave19 并入晚于 B-12 清单，非缺陷）；本 shard 只记录、不裁决、不改写 | `[归纳]` | partial | 内部证据 0d87d3fbe3e6a2ac（未公开；来源记录由维护者保留） : FK-B-02 L91、FK-X-01 L129；`RESULT.md` : §5 L46–51；[conflicts.md](../../../../cross/conflicts.md) : §3 N1/N3/N4/N9 + §4 表 L341–357（`grep -Ei '范宽|范寬|Fan Kuan|fan_kuan|雨点皴|雨點皴'` = 0 命中）；[fan_kuan.md](../../dossiers/fan_kuan.md) : §3.1-4 L74 |
| LFK-A5 | 语料 26 条（Q1–Q26）；四庫本 Q3/Q4/Q5/Q16/Q17 无标点照录；Q20/Q23/Q24/Q26 转引未直读原件 | `[史料]` | supported | [fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : `grep -c '^### '` = 26；内部证据 e915934ba699da34（未公开；来源记录由维护者保留） : L5、L9–12、L43；`RESULT.md` : §3 L33 |
| LFK-A6 | 《宋朝名畫評》四庫本卷2 范宽条全文（Q3）公网独立复核逐字命中；「危坐終日」「對景造意不取華飾寫山真骨」 | `[史料]` | supported | [fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q3 L29–33；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §4.1；claim_evidence_map.csv : FK-W-01 L132 / FK-S3-02 L23 / FK-S3-03 L24 |

<a id="db-source-line-22"></a>
## §B 组 — §4 参数 / §8.2 规则（均为 `[归纳]` 未实测）

| claim_id | 断言 | 级别 | support | 定位 |
|---|---|---|---|---|
| LFK-B1 | P1 雨点皴密度 / P2 主山压迫度 / P3 墨色 / P4 云雾带 / P5 点景 / P6 方折度 六参数各三档，默认 P1/P2/P5/P6 强、P3 中–强、P4 中 | `[归纳]` | partial | [fan_kuan.md](../../dossiers/fan_kuan.md) : §4 L78–106；[fan_kuan.md](../../modules/fan_kuan.md) : L60–88；[fan_kuan.md](../../dossiers/fan_kuan.md) : §8.1 中文说明 L196；claim_evidence_map.csv : FK-S4-P*-DEF L33/L37/L41/L45/L49/L53 (`partial`) |
| LFK-B2 | §8.2 八条可判定规则（覆盖/巨碑/墨色/亮带/悬瀑/点景/方折/动画）逐帧可查 | `[归纳]` | unverified | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2 L202–209；[fan_kuan.md](../../modules/fan_kuan.md) : L49–56；claim_evidence_map.csv : FK-S82-01…08 L57–64（全 `unverified`：§10-8 自述未实测，228/228 是逐字一致非像素验证） |
| LFK-B3 | §4/§8.2 阈值 `[归纳]`、未对原作做像素测量；`_extract.py --check` 228/228 校验卡↔档案逐字一致 | `[归纳]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §10-8 L272、§自审 D L425；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §2 L27、§7-2；`coverage-manifest.json` : extractor_check L6 |
| LFK-B4 | 228/228 = 76 卡 × §8.1/§8.2/§4 逐字比对；抽取器 sha `4afa31ec…` | `[归纳]` | supported | 内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §2 L27；`coverage-manifest.json` : L5–6；claim_evidence_map.csv : FK-X-03 L131 |
| LFK-B5 | §8.1 正向/负向 prompt：巨碑主山 + 密点短皴 + 云雾带 + 一线悬瀑 + 渺小点景 + 深暗墨色；负向禁披麻/等宽线/排线/色点分解/青绿/西式透视 | `[归纳]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.1 L167–193（正向 L167–182 / 负向 L185–193 / 中文说明 L195–198）；[fan_kuan.md](../../modules/fan_kuan.md) : L18–45 |

<a id="db-source-line-32"></a>
## §C 组 — 视觉机制 M1–M7（brief 强调 雨点皴 + 立幅主峰压迫）

| claim_id | 断言 | 级别 | support | 定位 |
|---|---|---|---|---|
| LFK-C1 | **M2 立幅主峰压迫**：主峰 ≥60% 画高、中轴（重心 ≤10% 宽）、顶部 ≤5% 高；徐悲鸿「一山頭幾佔三分之二」/ 赵孟頫「大圖闊幅，山勢逼人」为观察对象非阈值来源 | `[归纳]`+`[史料]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-2 L203、§1-1 L29、§4 P2 L83–86；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q18 L134–138、Q24 L177–178；[fan_kuan.md](../../dossiers/fan_kuan.md) : §7-8 L159（NPM 2021 巨碑式典范）；[fan_kuan.md](../../modules/fan_kuan.md) : L50 / L65–68 |
| LFK-C2 | **M1 雨点皴 / 密点积墨**：短笔 ≤山高 2%、覆盖 ≥60%、方向 std ≥20°、单一方向 <30%；「搶筆俱均」+ 刘芳如「千筆萬筆逐層疊搭」+ NPM「皴法：雨點皴」；名称晚出括注必带 | `[归纳]`+`[史料]`+`[研究]` | supported（操作）/ partial（名称） | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-1 L202、§1-2 L30、§2-1 L42、§4 P1 L78–81；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q6 L50；[fan_kuan.md](../../dossiers/fan_kuan.md) : §7-1 L152；claim_evidence_map.csv : FK-S1-02 L3 / FK-S2-01 L12 |
| LFK-C3 | M3 云雾留白带：8–25%、横贯 ≥60%、画高 35–60%、带内墨线 ≤3%；NPM「近中遠三段式」「與山石成虛實之呼應」 | `[归纳]`+`[史料]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-4 L205、§1-3 L31、§2-6 L47、§4 P4 L93–96；[fan_kuan.md](../../modules/fan_kuan.md) : L52 |
| LFK-C4 | M4 墨色浓重分层：深色 25–60%、≥3 明度带、禁平涂块；米芾「深暗如暮夜晦暝」「晚年用墨太多，土石不分」；P3 强档「土石不分为退化」 | `[归纳]`+`[史料]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-3 L204、§1-7 L35、§2-2 L43、§4 P3 L88–91；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q10 L78、Q11 L85 |
| LFK-C5 | M5 方折轮廓 + 山顶密林 + 水际大石：折角 60–120° ≥50%、长弧 ≤30%、山顶 10% 高带密林、水岸巨石 ≥1（≥15% 宽）；米芾《畫史》Q9 | `[归纳]`+`[史料]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-7 L208、§1-4/5/6 L32–34、§2-3/4/5 L44–46；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q9 L71 |
| LFK-C6 | M6 一线悬瀑 + 点景渺小：亮线宽 ≤1%/高 ≥8%/亮度 ≥95%/上 1/3–1/2；点景 ≤1.5% 高、≤8 个、下 1/4、面部 ≤3px；尺度对照强化压迫 | `[归纳]`+`[史料]+[研究]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §8.2-5/6 L206–207、§1-8/9 L36–37、§2-7 L48、§7-1 L152；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q10 L78「水若有聲」 |
| LFK-C7 | M7 界画「铁屋」：屋脊/飞檐/斗栱/柱椽逐一可辨、以墨笼染 | `[史料]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §1-10 L38、§2-9 L50；[fan_kuan.md](../../dossiers/_corpus/fan_kuan.md) : Q6 L50 |

<a id="db-source-line-44"></a>
## §D 组 — 分工 / 冲突 / 反例 / 权利

| claim_id | 断言 | 级别 | support | 定位 |
|---|---|---|---|---|
| LFK-D1 | 分工条款 vs 黄公望（皴法/构图/墨法/形制四轴 + 4 判据 + 两卡互禁）、vs 北斋、vs 塞尚；标 `[归纳]` 可被组合实验推翻；hokusai/cezanne 对侧条款待后续互查 | `[归纳]` | partial | [fan_kuan.md](../../dossiers/fan_kuan.md) : §3.1 L63–74、§10-12 L276；[fan_kuan.md](../../modules/fan_kuan.md) : L94–97；claim_evidence_map.csv : FK-S31-01/02/03 L29–31（`unverified`）/ FK-S31-04 L32（`partial`） |
| LFK-D2 | `conflicts.md` 无 fan_kuan 专属 C 行 / §4 near-miss 行（0 命中，wave19 并入晚于 B-12，非缺陷）；组合按 §3 N1/N3/N4/N9 预检 | `[归纳]` | supported | 内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §5 L46；claim_evidence_map.csv : FK-X-01 L129；[conflicts.md](../../../../cross/conflicts.md) : §3（N1/N3/N4/N9）、§4 L341–357 |
| LFK-D3 | `conflicts.md` 3 处定位漂移（michelangelo L175→176 / da_vinci L162→163 / §5-B-2 L372 历史行号）只报告不修 | `[归纳]` | partial | 内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §5 L48–51；claim_evidence_map.csv : FK-X-02 L130；[conflicts.md](../../../../cross/conflicts.md) : §5-C L398–401 |
| LFK-D4 | FK-CE-01 `[inference]` 纸面反例：P1/P3/P4 三强同开 → §8.2-1/3/4 同像素集面积竞争 + P3 自我退化；0 帧渲染、0 像素测量、不推翻规则 | `[归纳]`(inference) | partial | 内部证据 b1d0ab66ddeade0b（未公开；来源记录由维护者保留） : L3、L15–27、L29；claim_evidence_map.csv : FK-CE-01 L136；[fan_kuan.md](../../dossiers/fan_kuan.md) : §4 P1 强 L81 / P3 强 L91 / P4 强 L96 |
| LFK-D5 | **NPM 署名要求**：8 张公开图 = PD×3 + CC0×4 + NPM 开放资料×1；`wanghui_fa_fankuan.jpg` 许可「政府资料开放授权条款，相容 CC BY 4.0；署名：国立故宫博物院」为唯一强制署名；正确源 NPM IIIF 5100（5099 误链已 OVERTURNED） | `[史料]` | supported | 内部证据 064e65a48f3f3d23（未公开；来源记录由维护者保留） : L14、L20、L7、L22–24；[MANIFEST.md](../../dossiers/_images/fan_kuan/MANIFEST.md) : L18、L34；[manifest.md](../../dossiers/_images/manifest.md) : L366；claim_evidence_map.csv : FK-R-04 L124 / FK-B-03 L92；[fan_kuan.md](../../dossiers/fan_kuan.md) : §自审 B-3 L392 |
| LFK-D6 | §12 临摹/学习清单 8 件（谿山行旅/雪景寒林/临流独坐/雪山萧寺/秋林飞瀑/群峰雪霁/倣范寬山水/王翬+趙原），各「看什么/学什么/怎么练」 | `[史料]`+`[归纳]` | supported | [fan_kuan.md](../../dossiers/fan_kuan.md) : §12 L342–376；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §3 |

<a id="db-source-line-55"></a>
## §E 组 — 练习 / 决策序（design_candidate，不冒充验证）

| claim_id | 断言 | 级别 | support | 定位 |
|---|---|---|---|---|
| LFK-E1 | 三段练习阶梯「立幅巨碑比例 → 雨点皴密度 → 满皴+浓墨+云雾带联合约束」为**建议练习**（A-30 §8.1 形状：前置/作品/机制/练习/结果/失败/下一步/边界） | design_candidate | not_applicable | [learning_path.md](learning_path.md) : §1–§8（本目录）；`01-AUDIT.md` : §8.1 L269–273；`02-EXECUTION-PLAN.md` : L64 |
| LFK-E2 | How-to-Think D1–D8 决策序全为 `[归纳]`（研究者构造），`[自述]`=0 条本人文字；禁止从画面外观编造作者心理 | design_candidate | not_applicable | [how-to-think.md](how-to-think.md) : §0–§2（本目录）；`00-GOAL.md` : L9；`03-RESEARCH-AGENDA.md` : L14；`01-AUDIT.md` : §8.4 L308 |
| LFK-E3 | 练习效果未由人完成或评价 → `human_review.status=not_applicable`，不写「已证实学习收益」 | fact | supported | `01-AUDIT.md` : §8.1 L273、§8.4 L308；`receipt.json` : human_review（本目录） |
| LFK-E4 | §4/§8.2 → 练习自查映射、FK-B-02 开放项、FK-CE-01 失败条件 | design_candidate | not_applicable | [mechanism_notes.md](mechanism_notes.md) : §A–§E（本目录） |

<a id="db-source-line-64"></a>
## §F 组 — 诚实边界（未升级 / 未覆盖）

| claim_id | 断言 | 级别 | support | 定位 |
|---|---|---|---|---|
| LFK-F1 | `card_has_81b=false` 属 `STYLE-fan_kuan` 独立任务；§8.3 野外样本「未找到」；本 LEARN 不越权重跑 | `[归纳]` | supported | 内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §7-1；[fan_kuan.md](../../dossiers/fan_kuan.md) : §8.3 L213–214；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） : style_only_missing line 1009 |
| LFK-F2 | 外部来源：本 LEARN 未开任何 URL、未逐张目检 8 张图（image_seen=0 / metadata）；AUDIT 仅取 4 个 URL，其余 [R#] 未逐一重取；Q20/Q23/Q24/Q26 转引未直读 | fact | partial | 内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §3 L34、§7-4 L62；`quote_audit.md` : L43；[fan_kuan.md](../../dossiers/fan_kuan.md) : §9 L218–254 |
| LFK-F3 | 真迹/传称边界：学界公认真迹仅《谿山行旅图》，余多传称；传称作品练「样式」不冒充真迹定论 | `[研究]` | partial | [fan_kuan.md](../../dossiers/fan_kuan.md) : §10-3 L267；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §7-3 |
| LFK-F4 | 生卒异说、名字两说、四处出处未找到、原名推测、`照金=写山原型` 单线证据——保留未知/推测，不猜测不补造 | `[史料]`/`[推测]` | partial | [fan_kuan.md](../../dossiers/fan_kuan.md) : §10-1/2/5/6 L265–270、§自审 D L425；内部证据 a57c9b8c68171977（未公开；来源记录由维护者保留） : §7-3 |
| LFK-F5 | 本 shard `status=submitted`、`review:null`、作者不自接受；NO repo writes / NO subagent spawns / NO credentials | fact | supported | `receipt.json`（本目录）；`RESULT.md` : §0、§6（本目录）；内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） : LEARN-fan_kuan 条目 L1394–1415 |

---

<a id="db-source-line-76"></a>
## 附：定位分母与一致性

- 5 个内容文件（learning_path / how-to-think / mechanism_notes / claim_evidence_map / RESULT）+ 2 回执（runner_receipt / receipt）= **7 文件契约**。
- `required_artifact_kinds`（registry L1409–1413）= {result_summary, learning_path, mechanism_notes, claim_evidence_map} **全满足**，另含 how_to_think。
- 所有 repo 行号对应本机当前工作树 sha256（开工 `sha256sum` 现场复核，与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） 及 `AUDIT-fan_kuan.contract.json` 一致）：dossier `5535fa2a…` / card `a8609ed7…` / corpus `5ef890d9…` / conflicts `314a24da…` / images manifest `5698124d…` / local MANIFEST `fe4579ca…`。
- AUDIT 产物 sha256（现场复核）：RESULT `fbb4dce6…` / claim_evidence_map.csv `29e540a0…` / counterexample `03074020…` / rights_review `b6109165…` / quote_audit `54b9fa21…` / coverage-manifest `7ec3f565…` / receipt `143434af…`。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
