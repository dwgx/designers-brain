<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-constable；原正文 SHA-256 `5939e58d7b23f0008868946c65542b56698a70731fdd202d9e8931131d3101a3`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-constable — claim_evidence_map（逐断言回源）

> **task_id:** LEARN-constable · **lane:** learning · **kind:** claim_evidence_map
> **用途:** [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 中每条 `⟨Lxx⟩` 断言在此给出**定位（source_id + version + locator + read_scope + access_status）**与证据级。沿用 AUDIT-constable 的定位纪律（claim_evidence_map.md 85 行 / coverage-manifest.json）：不新编生平、不重审来源、不升级验证级别、不把未取得项写成已核。
> **version:** `f008952365a77e140cbda3f3959d43ef000f9a22`（repo HEAD，READ-ONLY）。
> **分级:** `[自述]` / `[史料]` / `[研究]` / `[归纳]` / `[推测]`，沿用 dossier 卷首 L5；`[归纳]` 阈值另带 `[UNVERIFIED]`。
> **access_status:** `available`＝本机文件直读；`partial`＝外部可达性/转引载体仅取 AUDIT 自报告，本 LEARN 未重抓；`unknown`＝明确未取得。
> **retrieved_bytes_sha256:** 取对应文件整体 sha256（下表 S 行给全值；每行以 `sha=S##` 简写引用）。

---

<a id="db-source-line-12"></a>
## 0. 源文件登记表（S 行）

| S | source_id | sha256 | 说明 |
|---|---|---|---|
| S01 | [constable.md](../../dossiers/constable.md) | `ea5eb512c68f145f547f0f7326bb77c92c9e13beb66e0faac87b56611d985085` | dossier 正本（472 行）；AUDIT §2 与 ledger artists[11] 逐字一致 |
| S02 | [constable.md](../../modules/constable.md) | `054ebfea3f0b607c8611df652fdac3b087dc46bb1d5bc3ef0890b0270377c7de` | 模块卡（§8.1/§8.2/§4 与 dossier 逐字一致，228/228） |
| S03 | [constable.md](../../dossiers/_corpus/constable.md) | `5bc87388bc3116676ff55e3ca75da6c0b325a1a56347463e351bc06fdac1ba51` | 36 条语料（22 self-written / 7 inscription / 3 reported / 2 contemporary / 2 later）；AUDIT §3.2 |
| S04 | [friedrich.md](../../dossiers/friedrich.md) | `a8c7e4b427da4109822efdc60faa8c3320e0edb5558137e90b7daf8d833e9149` | 互查对侧；**L8 写死分工 / L83 四判据**（本次交办） |
| S05 | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 18 C 行 + 11 near-miss = 29；对 constable **0 命中**（AUDIT §3.4） |
| S06 | `ops/GOALS.md` | `2727d1f079e164ee05bba50fb63d281947fce9251339ae73be99acc8a5e91144` | A-79 宿主 L117（语料 36 / 图库 17 / 引文 13/13 / 分工互查） |
| S07 | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` | 全局权利账 L389-405 共 17 行 constable 权利行 |
| S08 | [MANIFEST.md](../../dossiers/_images/constable/MANIFEST.md) | `4997cccafc332459696c6cf31f82c037aaf5ade04b25ec43dec579bfe7394e00` | 逐张 17 行总表 + 17 行 sha256(16) + 核验记录 |
| S09 | 内部证据 d7b24c80eeaab091（未公开；来源记录由维护者保留） | `6e8d6a697a9d678ac32a57990973cfe852b5f65ca5b49a481637a94affb8d9ba` | ACCEPTED 审计结论（证据底本） |
| S10 | 内部证据 cbd5aa1b011413a4（未公开；来源记录由维护者保留） | `5f2c737af701c96fca02b536471cbb02c94e59a05a67cf58ab418e616c1a2777` | AUDIT 85 行断言定位（C1-1…M-CX1） |
| S11 | 内部证据 58e7b17bce6fa627（未公开；来源记录由维护者保留） | `4f739f5e9455e25f8cbf2b904e4c456ba93783f59ccc6d6019f3b5ac978f838c` | 覆盖分母 + honest_limits + external_fetches + 输入哈希 |
| S12 | 内部证据 530cbdf705ff5fd9（未公开；来源记录由维护者保留） | `5b729263ff4c01387eede2179d1ee227fdae5525784f71ee6d93e55876c1672f` | CX-1 主强反例 / CX-2 / CX-3 |
| S13 | 内部证据 007ebaf40eaea1ca（未公开；来源记录由维护者保留） | `f9dee457e81973476abfd30f75bf8cd9b179d5b6b4e1a01af7590235e2f76245` | 17 行逐张权利 + **16 PD + 1 CC0** + honesty boundaries |
| S14 | 内部证据 2ecd5830d584e550（未公开；来源记录由维护者保留） | `9432541599b1bf926b61913f1eb478a81d84be8054882407d7e32668ff596b4e` | 独立审阅 verdict **accepted**（§2 互查 / §3 漂移 / §4 CX-1 复现） |
| S15 | 内部证据 70048fdaf724bd8f（未公开；来源记录由维护者保留） | `1cd9c1338eb3c8121cc5206b64ce8e2816c13d2d001efcf7d8a26780c3b993cf` | AUDIT 自身回执（status=submitted）；本 LEARN 只引用其输入哈希 |
| S16 | `package/00-GOAL.md` | `3799710118a32d6aeaf2f2fdc9524f779ba4d1132318e1a7422413df44fbfa81` | A-30 / §8.1 形状 / L9 How-to-Think 纪律 |
| S17 | `package/01-AUDIT.md` | `738d6a5a7dde17e444a594c1116da7322f2b0b127cc000c43c835f7f4e65aacf` | §8.1 L269-273 / §8.4 L308 / §9 学习与交互门 |
| S18 | `package/02-EXECUTION-PLAN.md` | `a2a3ad058f9fbe713ef4bb0ea3487c02ef6d6e81a3e5c70a6ac9dca30b5be992` | Lane B L62-66（观察对象→决策→机制→参数→练习→反例→自检） |
| S19 | 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） | `e1ec2d11ed3b3458a2e233a101319ffdf12d253b22562a97d4e25618b1158ce9` | 权威输入基准 artists[11]（card/dossier/corpus 三哈希 + corpus_quotes=36 + images_public=17） |

> **包根** = 内部证据 1ebc1865fb26af94（未公开；来源记录由维护者保留）；**staging 根** = 内部证据 0e7b0a8c2ae9a0fb（未公开；来源记录由维护者保留）。S01–S08 / S19 的 sha 为本 LEARN 开工用 `sha256sum` 实跑复测（与 AUDIT §2 / ledger 一致）；S09–S15 / S16–S18 为同一命令实跑。外部 URL 重访由 AUDIT 承担（coverage-manifest.json `external_fetches` 4 条），本 LEARN 未重抓、只引用其 `partial`/`supported` 结论。

---

<a id="db-source-line-40"></a>
## 1. 断言—定位表（L01–L57，分母＝57，同一次统计）

> 列：`id | kind | grade | claim（简写） | locator（S:行） | scope | access | 出现在`。`sha=S##` 指向 §0 整体 sha256。`scope` 取值：`fulltext`/`sections`/`citation_context`/`artifact`/`metadata`。

| id | kind | grade | claim | locator | scope | access | 出现 |
|---|---|---|---|---|---|---|---|
| **L01** | validated_rule 候选 | `[归纳]` | 三条写死分工轴不得混用（vs 透纳 / 莫奈 / 弗里德里希） | S01:L8,§3.1 L78-97 / S02:L69-76 / S04:L8 | sections | available | path §1.1/§7；think D9/§3 |
| **L02** | validated_rule 候选 | `[归纳]` | **friedrich.md L8 写死「vs 康斯泰勃尔＝忠实观察 vs 精神化」** | S04:L8 / S01:L8,L92-95 / S09:§3.5 / S10:C3.1-F / S14:§2 / S11:known_history_a79 | sections | available | path §1.2/§4 C2/§5.4；think §0/§3/D1；mech C/D |
| **L03** | validated_rule 候选 | `[归纳]` | **friedrich.md L83 四判据**（地点忠实度/象征计数/天空角色/人物）与 constable.md L94 逐条同轴同侧；AUDIT CONFIRMED 文本级 | S04:L83 / S01:L94-96 / S09:§3.5 / S10:C3.1-F / S14:§2 | sections | available | path §1.2/§4 C2/§6 F3；think §3/D1/D7/D8；mech A/D/F |
| **L04** | fact | `[自述]`+`[归纳]` | 无画论专著；三「层」分工（事实/原则/操作化）；§3 八条 + §5 十条原话 | S01:L9,L69-76,L116-129 / S03:卷首 L4-7 / S18:L64 | sections | available | path §1.3；think §1/§2 |
| **L05** | observation | `[史料]` | skying 云研究：1821–22 汉普斯特德、背面题记、Howard/Forster | S01:L53 / S02:L9 / S03:Q17-23 / S09:§3.6 / S10:C2-2 | sections | available | path §1.4/§3 M9；think D4；mech A/C |
| **L06** | observation | `[史料]` | 六英尺大画机制骨架：现场速写库→等大稿→six-footer | S01:L148 / S03:Q13 / S09:§3.1 / S10:C2-3 | sections | available | path §1.5/§3 M8/§5.2；think D5；mech A/C.2/F |
| **L07** | observation | `[史料]` | 等大稿 987-1900 / 12 组成对 + 第 13 件无对 / 两档并存 / Lucas 40 幅 13 校样 | S01:L44,L54,L60,L148 / S02:L10,L13 / S10:C1-10,C2-3,C2-9 | sections | available | path §1.5/§4 B2；mech A/C.2 |
| **L08** | observation | `[史料]` | **「Constable's snow」＝细小白色点亮斑（高光笔点，非降雪）** | S01:L36,L56 / S02:L10,L28 / S09:§3.6 / S10:C1-2,C2-5 / S11:known_history_a79 | sections | available | path §1.6/§3 M2/§4 C1/§6 F4；think D6；mech A/C.1 |
| **L09** | observation | `[史料]`+`[归纳] [UNVERIFIED]` | 白点批评史（sleet/snow/whitewash）+ §8.2-2 可判定面 V≥0.9 / 0.05–0.6% / ≥15 | S01:L36,L204 / S02:L46 / S10:C1-2,C4-P3 | sections | available | path §1.6/§3 M2/§4 C1；mech B/C.1/E |
| **L10** | observation | `[归纳]` | conflicts.md 对 constable 0 命中（29 行）；C-01/05/09/12 是组合预检引用非冲突行 | S05:§1/§4 / S01:L97 / S02:L76 / S09:§3.4 / S11:conflicts_rows_checked=29 | sections | available | path §1.7/§7；mech D/F |
| **L11** | observation | `[归纳]` | 语料/权利边界：原书页码未回查、7 条 V&A 题记 carrier 级、image_seen=0 | S03:L278 / S01:§10-1 / S09:§3.2,§5 / S13:Honesty / S11:honest_limits | sections | available | path §1.7/§7；think §1 缺口/§4；mech F.7 |
| **L12** | fact | `[史料]`+`[归纳]` | §12 十件作品信息沿用现有记录、练习条目为项目设计 | S01:L345-399 / S17:L271-273 | sections | available | path §2 表头；mech 底本 |
| **L13** | observation | `[史料]` | 《干草车》1821 NG1207：写生库→画室组装、等大稿、X 光两次改动 | S01:L154,L349-352 / S02:L23 | sections | available | path §2-1/§4 B1；mech C.2 |
| **L14** | observation | `[研究]` | 《萨利斯伯里》气象合成 / 彩虹＝自然物承载象征 / Thornes ≥15 分钟 | S01:L156,L354-357 / S09:§3.6 | sections | available | path §2-2；think D8 |
| **L15** | observation | `[史料]` | 《白马》1819 第一幅成功六英尺、亮/暗两半、镜像水面 | S01:L359-362 | sections | available | path §2-3 |
| **L16** | observation | `[史料]` | 《Flatford Mill》1816–17 现场/画室两档；图库此件为唯一 CC0 | S01:L364-367 / S13:表#3 | sections | available | path §2-4/§4 B2；mech A |
| **L17** | observation | `[史料]` | 《麦田》1826 田园叙事最小配置 | S01:L369-372 | sections | available | path §2-5 |
| **L18** | observation | `[史料]` | 《Dedham Vale》1802 地标锚定原型 | S01:L374-377 | sections | available | path §2-6/§4 C3；think D1 |
| **L19** | observation | `[史料]` | 《Wivenhoe Park》1816 构图谈判 / 5 元素 | S01:L379-382 | sections | available | path §2-7 |
| **L20** | observation | `[史料]` | 《Brighton Beach with Colliers》1824 背面题记＝观察记录制度 | S01:L384-387 / S13:表#1 | sections | available | path §2-8；mech C |
| **L21** | observation | `[史料]` | 《Seascape Study with Rain Cloud》c.1827 无地标、天空即主题（CX-1 对象） | S01:L389-392 / S12:CX-1 / S13:表#7 | sections | available | path §2-9/§4 A2/§6 F6 |
| **L22** | observation | `[史料]` | 云研究三张 V&A 590/784/240-1888；七天 skying 练习 | S01:L394-397 / S03:Q17-23 | sections | available | path §2-10/§4 A1/§5.1；mech A/C |
| **L23** | design_candidate | `[归纳]` | §12 末组合练习分组（1/4/7 建构、2/9 气象、3/6 地标、8/10 记录）→ 三阶重排 | S01:L399 / S18:L64 | sections | available | path §2 末/§4；mech C |
| **L24** | fact | `[史料]` | **16 PD + 1 CC0**（flatford_mill.jpg Tate N01273）；双 manifest 17/17/17/17；drift 3 措辞不精确非缺陷 | S07:L389-405 / S08:总表 / S13:§Aggregate,表#3 / S09:§3.3,§4-3 / S14:§3 / S01:L7,L27 | sections | available | path §2 末/§6 F8/§7；think §4 B5；mech C/F.3 |
| **L25** | observation | `[自述][研究]`+`[归纳]` | 天空主音 ≥35%、云型可辨、地平线可见（§8.2-1） | S01:L35,L203 / S02:L9,L45 / S10:C1-1,C4-P1 | sections | available | path §3 M1；think D3；mech A/B |
| **L26** | observation | `[史料][归纳]` | 固定地点锚定 ≥1 地标 / 单消失点（§8.2-5）；friedrich L83 判据① | S01:L37,L207 / S04:L83 / S02:L11,L49 / S10:C1-3,C4-P4 | sections | available | path §3 M3；think D1；mech A/B/D/E |
| **L27** | observation | `[史料]`+`[归纳]` | 绿-蓝-红预算 30/10/0.3–3%（§8.2-3）/ Lucas 红缨对位 | S01:L39,L58,L205 / S02:L47 / S10:C1-5,C2-7 | sections | available | path §3 M4/§4 B3；think D6；mech A/B/E |
| **L28** | observation | `[史料][归纳]` | 劳作小人物 ≤5、无背向凝视者（§8.2-7）/ friedrich L83 判据④ | S01:L40,L209 / S04:L83 / S02:L51 / S10:C1-6 | sections | available | path §3 M5；think D7；mech B/D/E |
| **L29** | observation | `[归纳] [UNVERIFIED]` | 水＝天空之镜（色相差 ≤25°、饱和 0.4–0.8×，§8.2-6） | S01:L38,L208 / S02:L50 / S10:C1-4 | sections | available | path §3 M6/§5.3；mech B/E |
| **L30** | observation | `[史料]`+`[归纳]` | 表面清脆 / 无硬阴影 / C-01 预检（§8.2-8） | S01:L43,L97,L210 / S02:L52,L76 / S05:C-01 | sections | available | path §3 M7/§6 F5；mech B/D/E |
| **L31** | observation | `[归纳]` | 无事件 / 低动势（§8.2-4）/ vs 透纳四判据 + 边界注 ≥2 轴联合（L84） | S01:L80-86,L112,L206 / S02:L48,L67 / S09:§3.5 / S10:C3.1-T | sections | available | path §3 M10/§5.1/§6 F1；think D2/§4 B1；mech A/B/D/E/F.8 |
| **L32** | design_candidate | `[归纳]` | 阶梯 A（看天制度 + 云景）＝建议练习 A1/A2 + 自查靶值 | S01:L197,L392,L397 / S18:L64 | sections | available | path §4 A；mech A/C |
| **L33** | design_candidate | `[归纳]` | 云研究档 P2 升强、P6 降弱、P1 ≥50%（§8.1 L197「无人物无地标也成立」） | S01:L197 / S02:L67 / S12:CX-1 | sections | available | path §4 A 自查；mech A/F.4 |
| **L34** | design_candidate | `[归纳]` | 阶梯 B（乡土云景 + 六英尺机制）B1/B2/B3 | S01:L54,L55,L352,L367 / S18:L64 | sections | available | path §4 B；mech A/C.2 |
| **L35** | observation | `[史料]` | 有色底子：粉底＝晴 / 褐底＝风暴，故意留底 | S01:L55 / S10:C2-4（partial，本轮 web 未复现） | sections | available | path §4 B2 |
| **L36** | design_candidate | `[归纳]` | 阶梯 C（白点锚 + 分工 A/B）C1/C2/C3 | S01:L36,L94,L377 / S04:L83 / S18:L64 | sections | available | path §4 C；mech C.1 |
| **L37** | observation | `[归纳]`+`[研究]` | 象征只由自然物承载（彩虹）；vs 弗里德里希外加装置不同轴（L96 边界注） | S01:L96,L156,L356 / S04:L83 / S10:C3.1-F | sections | available | path §4 C2/§5.4/§6 F3；think D8/§3；mech D |
| **L38** | design_candidate | `[归纳]` | 收口：§8.2 八条自查 + §4 L112 越界警报 + CX-1 反例代入 | S01:L112,L198,L203-210 / S12:CX-1 / S17:L273 | sections | available | path §4 收口；mech B/F.4 |
| **L39** | observation | `[归纳][推测]` | **CX-1**：云研究档被 §4/§8.2-5 单独误判，文本级内部张力 CONFIRMED，未改规则未做实验 | S12:CX-1 / S01:L84,L112,L197,L207,L389-392 / S09:§3.7 / S14:§4 / S10:M-CX1 | sections | available | path §4 A2/§4 收口/§6 F6/§7.5；think D9/§4；mech A/B/D/E/F.4 |
| **L40** | observation | `[归纳]` | 静态图不套用动画专属项（S-06 第 4 项） | S17:L275-280 / S16:L24 / S01:L206 | sections | available | path §4 收口/§7；mech B/F.9 |
| **L41** | fact | `[归纳] [UNVERIFIED]` | §4/§8.2 全部阈值未实测（分母＝假想参考帧）；练习≠学习成效 | S01:L212,§10-7 / S02:L54 / S09:§5 / S17:L271-273,L308 / S10:C4-P* | sections | available | path §1 全局/§5.5/§7；think §4；mech 级别纪律/B 末/F.1 |
| **L42** | observation | `[归纳]` | vs 莫奈＝瞬时氛围 vs 观察笔记；AUDIT C3.1-M = partial（未做 E 系列），不升级 | S01:L87-91 / S02:L74 / S09:§3.5 / S10:C3.1-M | sections | available | path §6 F2/§7；think §3/§4；mech D/F.8 |
| **L43** | fact | `[史料]` | 13/13 引文抽查 ≠ 36 条语料（CX-3，两分母不同） | S09:§3.2 / S12:CX-3 / S01:L418,L443-457 / S03:§统计 L277 / S06:L117 | sections | available | path §6 F7；think §4 B4；mech F.6 |
| **L44** | observation | `[归纳]` | 3 处内容漂移（28→36 / 126·129→228/228 / 全PD→16PD+1CC0）只读不修 | S09:§4 / S14:§3 / S11:known_content_drift_recorded_not_fixed / S01:L27,L460,L471 | sections | available | path §6 F9/§7；think §4；mech F.5 |
| **L45** | observation | `[归纳]` | 下一步：独立审者 / 人评样本包 / E 系列 / 像素实测 / CX-1 裁定 / STYLE lane | S01:L471 / S17:L308,L310 / S11:card_has_81b=false / S12:CX-1 | sections | available | path §7 下一步；think §4；mech F.2/F.10 |
| **L46** | observation | `[归纳]` | 使用边界：沿用现有记录、未重抓/未目检/未复核许可、无凭据、无子代理、repo READ-ONLY、submitted 仅 schema 门 | S09:§5 / S13:Honesty / S14:verdict / S16:L9 / S17:L322 | sections | available | path §7 使用边界；think 末尾；mech F.10 |
| **L47** | observation | `[史料]` | 4 个公开 URL 重访（Wikipedia/NGL/V&A/Tate；Tate partial/sections）为上游已接受证据，只引用不升级 | S11:external_fetches / S09:§3.6 / S14:§3 | artifact | available | path §7；think §1 缺口；mech F.7 |
| **L48** | fact | `[自述]` | corpus Q1「There is room enough for a natural painture」（异文 painture/painter 已注） | S03:Q1 L11-17 / S01:L70,L121 | citation_context | available | think §1 S1 |
| **L49** | fact | `[自述]` | corpus Q2「laborious studies from nature」 | S03:Q2 L19-24 | citation_context | available | think §1 S2 |
| **L50** | fact | `[自述]` | corpus Q3「forget that I have ever seen a picture」（原信日期未回查） | S03:Q3 L26-31 | citation_context | available | think §1 S3 |
| **L51** | fact | `[自述]` | corpus Q4「painting is but another word for feeling / those scenes made me a painter」 | S03:Q4 L33-38 / S01:L69,L120 | citation_context | available | think §1 S4 |
| **L52** | fact | `[自述]` | corpus Q11/Q12「sky is the key note, the standard of scale / source of light」 | S03:Q11,Q12 / S01:L71,L123-124 | citation_context | available | think §1 S5/D2/D3 |
| **L53** | fact | `[自述]` | corpus Q13「I do not consider myself at work unless I am before a six-foot canvas / skying」 | S03:Q13 / S01:L76,L125 | citation_context | available | think §1 S6/D5；mech C.2 |
| **L54** | fact | `[自述]` | corpus Q9「a sketch will not serve more than one state of mind」 | S03:Q9 / S01:L73,L126 | citation_context | available | think §1 S7/D4 |
| **L55** | fact | `[自述]`（已削弱） | corpus Q15/Q24「Painting is a science … pictures are but experiments」；B2 已削弱为「科学+艺术许可合成」 | S03:Q15,Q24 / S01:L72,L127,L156,L416 / S12:CX-2 | citation_context | available | think §1 S8/D8/§4 B2；mech F.4 |
| **L56** | fact | `[自述]` | corpus Q6/Q8「My art flatters nobody / The world is wide…」 | S03:Q6,Q8 / S01:L74 | citation_context | available | think §1 S9 |
| **L57** | fact | `[inscription]` ≈ `[自述]` | corpus Q17-23 七条 V&A 背面题记（日/时刻/风向/云型），carrier 级 | S03:Q17-23 / S01:L53 / S10:C2-2 | citation_context | available | think §1 S10/D4；mech A |

---

<a id="db-source-line-106"></a>
## 2. 统计与分母（同一次统计）

| 项 | 值 |
|---|---|
| 断言总数 | **L01–L57 = 57 行**（本表 §1 逐行编号，连续无缺） |
| 按 kind | fact 17（L04,L12,L13…L20 部分,L24,L41,L43,L48–L57）/ observation 30 / validated_rule 候选 3（L01,L02,L03）/ design_candidate 7（L23,L32,L33,L34,L36,L38 + L12 附）→ 合计按主标记归类，详见每行 |
| 按 grade | 含 `[归纳]` 34 行 / 含 `[史料]` 12 行 / 含 `[自述]` 10 行 / 含 `[研究]` 4 行 / `[归纳][推测]` 1 行（L39）；`[归纳] [UNVERIFIED]` 标注 5 行（L09,L29,L30,L41 及 §8.2 相关） |
| 按 access | `available` 57 / `partial` 0 / `unknown` 0（所有 locator 均为本机文件或 AUDIT 已落盘产物；外部 URL 仅通过 S11 `external_fetches` 作 `artifact` 级引用，不单列断言） |
| 三文档 `⟨Lxx⟩` 覆盖 | learning_path L01–L47；how-to-think L48–L57 + 复用 L01–L47；mechanism_notes 复用 L01–L47。**0 个悬空锚点**（每个 `⟨Lxx⟩` 在本表有对应行） |
| 源文件 S | S01–S19 = 19 行，全部带实跑 sha256 |

> **分母纪律**：L57 行是「本 LEARN 三份文档内联断言」的分子分母同一次统计；**不等于** AUDIT-constable 的 85 行 claim map、也不等于 corpus 36 条、图库 17 张、引文 13/13、conflicts 29 行——五个分母各自独立，不混称（AUDIT §3.2 / §5 / CX-3 口径）。

---

<a id="db-source-line-121"></a>
## 3. 诚实边界

- **不新编、不重审**：作品、来源、权利、分级全部沿用 S01/S02/S03/S07/S08/S19 与 AUDIT 产物；本 LEARN 未重新抓取外部 URL、未复核外部许可有效性、未做视觉图像检视（`image_seen=0`，沿用 S13 Honesty boundaries / S11 honest_limits）。
- **不升级验证级别**：§8.2 全部阈值保持 `[归纳] [UNVERIFIED]`；vs 透纳/莫奈分工条款保持 AUDIT 的 `partial`；只有 vs 弗里德里希 `C3.1-F` 是文本级互查 `supported`（非实验验收）。
- **练习 ≠ 学习成效**：全部练习标「建议练习」；无真人完成或评价，不写「已证实学习收益」；模型/脚本自查不是人评（S17 §8.1 L271-273 / §8.4 L308）。
- **自述/推断严格分区**：how-to-think §1 为 `[自述]`/ `[inscription]`（S03 逐条带出处），§2/§3 为 `[归纳]` 决策序并声明「顺序是本项目设计、无作者原话规定」；不从画面外观反推心理（S01:L9）；B2「严格科学」已削弱（S12:CX-2）。
- **定位纪律**：一律采用当前仓库实测行号（S01 L36/L94/L112/L197/L207/L389-392、S04 L8/L83 等），不沿用 dossier 自审里的旧计数（28/126/129/全PD）。3 处漂移由 AUDIT 报告、归档案 owner，本 lane 只读不修（写权限仅 内部证据 397eb7a93bdb1219（未公开；来源记录由维护者保留））。
- **静态图边界**：§8.2-4 动画项只在动画练习使用，静态图不套用（S-06 第 4 项 / S17 L280）。
- **无凭据 / 无子代理**：所有源文件、产出文件均不含账号/口令/邮箱/哈希凭据/TOTP；本表仅含内容 sha256（公开文件哈希，非凭据）；`spawns_allowed=false`，本 leaf 未派发任何子代理。
- **回执自哈希**：`receipt.json` 不列入自己的 `artifacts`（自哈希循环），其 hash 由 parent runner 另封存；`status=submitted` 仅走 JSON Schema 结构门。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
