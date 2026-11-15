<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-matisse；原正文 SHA-256 `e3ff8037f584f442b8fb814c4b01d6d9e36199494ec4d12146580c4c645285e8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-matisse — claim_evidence_map（逐断言回源）

> **task_id:** LEARN-matisse · **lane:** learning · **kind:** claim_evidence_map
> **用途:** [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 中每条 `⟨Lxx⟩` 断言在此给出**定位（source_id + version + locator + read_scope + access_status）**与证据级。沿用 AUDIT-matisse 的定位纪律（claims.csv C01–C15 的字段形状）：不新编生平、不重审来源、不升级验证级别、不把未取得项写成已核。
> **version:** `f008952365a77e140cbda3f3959d43ef000f9a22`（repo HEAD，READ-ONLY）。
> **分级:** `[自述]` / `[史料]` / `[研究]` / `[归纳]` / `[推测]`，沿用 dossier 卷首 L5；`[归纳]` 阈值另带 `[UNVERIFIED]`。
> **access_status:** 全部 `available`（本机文件直读）／`partial`（外部可达性只取 dossier 自报告，未重抓）／`unknown`（明确未取得）。
> **retrieved_bytes_sha256:** 取对应文件整体 sha256（下表 S 行给全值；每行以 `sha=` 简写引用 S 编号）。

---

<a id="db-source-line-12"></a>
## 0. 源文件登记表（S 行）

| S | source_id（repo 相对路径 / 包路径 / staging 路径） | sha256 | 说明 |
|---|---|---|---|
| S01 | [matisse.md](../../dossiers/matisse.md) | `e2296b0e8bb13de307eed529cf601edbf7b5f4c053c10484e4be1fc0e5e83b70` | dossier 正本；AUDIT-matisse C01 复核一致 |
| S02 | [matisse.md](../../modules/matisse.md) | `550b4b89f651fdbb2dd8cf25ffbff6ed18d427d09003ad79414c2eeb38fc6b0b` | 模块卡（§8.1/§8.2/§4 与 dossier 逐字一致）；AUDIT C01/C02 |
| S03 | [matisse.md](../../dossiers/_corpus/matisse.md) | `9bc182458f30a378d4c87da9f33268ad05dfa5b84e58ce524f2c48a78c3ef9f3` | 自述/同代记录语料 Q1–Q24；AUDIT C12 |
| S04 | [conflicts.md](../../../../cross/conflicts.md) | `314a24da96ccf13e5f8ca2ab32f5689926627216a9471761e916f98427aabbef` | 18 冲突 + N1–N9 + near-miss；AUDIT C04–C11 |
| S05 | [expansion.md](../../dossiers/expansion.md) | `83d22559ecbe1a7f9e0b652a37d631b1056c5fa86ef978cfdede6261a9c0e056` | G4 / §1.5 克里姆特×马蒂斯分工与测试协议 |
| S06 | [manifest.md](../../dossiers/_images/manifest.md) | `5698124daf47c989fd26232a686ec54cda2658b623e1a302ddb5806ebf95b470` | §matisse L849-861 权利；AUDIT C13 |
| S07 | [提示词全文.md](../../../motion-graphics/origin/提示词全文.md) | `7227cbf02572c5226c154f84ea3f0cc022c07112ee2518cb8072a7f2d1ad34e6` | Lane B 02 卡 L72；AUDIT C07 |
| S08 | 内部证据 f02f8f0563db9074（未公开；来源记录由维护者保留） | `f805e26a131235242a37721289a906810a01c6e9d11c858ea052a42eb0828e1e` | ACCEPTED 审计结论（证据底本） |
| S09 | 内部证据 b18792f5ec7a0547（未公开；来源记录由维护者保留） | `46d68590ba125d6a72a3f71d43502026510f23f6fb1093eb6a6f2adc3918f10c` | AUDIT 15 条断言定位 |
| S10 | 内部证据 925dc4b73971092f（未公开；来源记录由维护者保留） | `accc1ad1ca1705ff74a2e6db8cb579c08563ef2f9a147c77b11d3bc74c728e13` | 覆盖分母 + honest_limits + 输入哈希 |
| S11 | `package/00-GOAL.md` | `3799710118a32d6aeaf2f2fdc9524f779ba4d1132318e1a7422413df44fbfa81` | A-30 / §8.1 形状 |
| S12 | `package/01-AUDIT.md` | `738d6a5a7dde17e444a594c1116da7322f2b0b127cc000c43c835f7f4e65aacf` | §8.1 L269-273 / §8.4 L308 |
| S13 | `package/02-EXECUTION-PLAN.md` | `a2a3ad058f9fbe713ef4bb0ea3487c02ef6d6e81a3e5c70a6ac9dca30b5be992` | Lane B L62-66 |
| S14 | 内部证据 130c3b54c30b1996（未公开；来源记录由维护者保留） | `e1ec2d11ed3b3458a2e233a101319ffdf12d253b22562a97d4e25618b1158ce9` | 输入哈希基准；AUDIT §1 |

> **包根** = 内部证据 1ebc1865fb26af94（未公开；来源记录由维护者保留）；**staging 根** = 内部证据 0e7b0a8c2ae9a0fb（未公开；来源记录由维护者保留）。S07 的 sha 取自 AUDIT-matisse coverage-manifest.json `mg_prompts_sha256`（本 leaf 未重算该卡，沿用 AUDIT 已核值）。S06 的 §matisse 行号 L849-861 取自 AUDIT C13。

---

<a id="db-source-line-35"></a>
## 1. 断言—定位表（L01–L56）

> 列：`claim_id | kind | grade | claim（简写） | source_refs（S:locator） | read_scope | access_status | 出现在`。`sha=` 一律指向 §0 的 S 行整体 sha256。

| id | kind | grade | claim | locator | scope | access | 出现 |
|---|---|---|---|---|---|---|---|
| **L01** | validated_rule 候选 | `[归纳]` `[UNVERIFIED]` | §8.2-1：同屏纯色块 ≤8（含黑白）、每块 S≥70%、明度分层 ≤3 级、除纸底外渐变面积 ≤5% | S01:L186 / S02:L43 / S04:L127(C-06 引文) / S08:§3 表 C-06 / S09:C06 | sections | available | path §1.2/§3 M2/§4 A/§5/§8.5；mech B/C/E |
| **L02** | validated_rule 候选 | `[归纳]` `[UNVERIFIED]` | §8.2-5：背景/纸色可见 ≥20%；间隙 ∈ [2%,12%] 最短边 | S01:L190 / S02:L47 / S04:L278(C-17 引文) / S08:§3 C-17 / S09:C08 | sections | available | path §1.3/§3 M8/§4 A/§5/§6/§8.6；mech B/C/E |
| **L03** | observation | `[归纳]` `[UNVERIFIED]` | §8.2-8 三档共同硬约束：纹样区内部明度动态 ≤5%；纹样与主体同线宽同色阶层数；判定失败回退一档 | S01:L193 / S02:L50 / S05:L252 / S04:L249(C-15 引文) / S08:§2 / S09:C04 | sections | available | path §3 M5/§4 B/§5/§6/§8.1；mech B/C/E |
| **L04** | validated_rule 候选 | `[归纳]` | §8.2-2 剪裁边：无描边/羽化/投影；直线段＋圆弧，夹角 ≤15° 视为同一弧 | S01:L187 / S02:L44 / S04:L263(C-16 引文) / S08:§3 C-16 / S09:C07 | sections | available | path §1.4/§3 M3/§4 A/§5/§6/§8.4；mech B/E |
| **L05** | validated_rule 候选 | `[归纳]`（量化）+ `[自述]`（取向） | §8.2-3 垂直参照：夹角 ∈[0°,75°]；失控曲线计数 = 0；「我的曲线不疯狂」 | S01:L35(§1-7 `[自述]`),L105-107(§5-4),L188(§8.2-3) / S02:L45 / S03:Q1-13 不含此句→见 §5-4 | sections | available | path §1.4/§3 M7/§5/§8.2；mech A(P6)/B/E；think §1 S14/§2 D6 |
| **L06** | validated_rule 候选 | `[归纳]` `[UNVERIFIED]` | §8.2-4 面积配比：最大 25–45%／次大 15–30%／其余 <12%；防「碎花」相邻同色相近块 | S01:L189 / S02:L46 / S01:L366(§12-2 面积图) | sections | available | path §2 表#2/§3 M6/§5/§6；mech B/E |
| **L07** | validated_rule 候选 | `[归纳]` | §8.2-7 符号复用 ≥3 次变形 ≤20%；§8.2-6 动画项（旋转 ≤12°、过冲 ≤3%、回弹 ≤1、禁 crossfade、停留 ≥0.8s） | S01:L191-192 / S02:L48-49 | sections | available | path §3 M9/§4 收口/§5/§6；mech B/E |
| **L08** | validated_rule 候选 | `[归纳]` `[UNVERIFIED]` | §8.2-8 档位映射：弱/中/强 $A_p$/$L_p$ 阈值；旋钮值≠实测 $A_p$；「P4=强」须旋钮 ≥80% 且实测 $A_p$≥50%，失配记一条 | S01:L193-194 / S02:L50-51 / S05:L252-253 | sections | available | path §4 B/§5/§6/§8.5；mech A(P4)/B/C/E |
| **L09** | observation | `[研究]` | §1-1 平涂色块：内部明度变化 ≤5%、剪纸期 0 渐变；§2-1 平涂（peint à plat） | S01:L29,L44 / S02:L9 / S05:L250(指纹 1 引述) | sections | available | path §1.1/§3 M1/§5/§8.5；mech C/E |
| **L10** | observation | `[研究]` | §1-2 色相少而纯（5–8 高纯色、互补对撞）；§1-4 黑当彩色用（黑/深色面积 5–20%） | S01:L30,L32 / S02:L10 | sections | available | path §3 M2/M4/§5；mech E |
| **L11** | observation | `[归纳]`（对照作品图） | §1-8 留白是主角：负空间可见 ≥20% | S01:L36 / S02:L12 | sections | available | path §1.3/§3 M8；mech — |
| **L12** | observation | `[史料]` | §12-4《舞蹈》1910 冬宫：5 人体/3 色/闭合弧线、装饰与主体同权 | S01:L373-376 | sections | available | path §2 表#4；mech — |
| **L13** | observation | `[史料]` | §12-6《爵士》1947 Tériade：剪刀直接剪入颜色；§5-3 原话 | S01:L101-104,L383-386 | sections | available | path §2 表#6/§4 A；mech — |
| **L14** | observation | `[史料]` | §12-9《蜗牛》1953 泰特：分解—重组为互锁色块 | S01:L398-401 | sections | available | path §2 表#9/§4 A；mech — |
| **L15** | observation | `[研究]` | §12-8《蓝色裸体 II》1952 蓬皮杜：极限简化、4 版各改 ≤20%；§10-3 馆方页待补 | S01:L393-396,L236 | sections | available | path §2 表#8；mech — |
| **L16** | observation | `[史料]` | §12-3《红色画室》1911 MoMA：单色域统一、最大平面化 | S01:L368-371 | sections | available | path §2 表#3；mech — |
| **L17** | observation | `[史料]` | §12-7《游泳池》1952 MoMA：唯一为特定房间而作、环带、间隙呼吸；§7-1 | S01:L145,L388-391 | sections | available | path §2 表#7/§4 A/§5；mech — |
| **L18** | observation | `[史料]` | §12-2《生活的欢乐》1905–06 巴恩斯：4×6 色块面积图、最大块 25–45% | S01:L363-366 | sections | available | path §2 表#2/§5；mech B |
| **L19** | observation | `[史料]` | §12-1《戴帽子的妇人》1905 SFMOMA：色相置换、色相对撞靠面积配比取胜 | S01:L358-361 | sections | available | path §2 表#1；mech — |
| **L20** | observation | `[研究]`/`[史料]` | §12-5《大型斜卧裸体》22 张过程照、十步推进；§2-10《主题与变奏》158 张/17 组 | S01:L53,L378-381 | sections | available | path §2 表#5；mech B(§8.2-7)；think §2 D8 |
| **L21** | observation | `[史料]` | §12-10 旺斯玫瑰礼拜堂 1949–51：总体艺术、三色系统+黑白线画 | S01:L403-406 | sections | available | path §2 表#10；mech — |
| **L22** | observation | `[史料]`（清单自报） | 3 张公开图像权利：la_danse.jpg=PD(Wikimedia/Thierry Caro)、另 2 张=CC0(AIC)；未视觉检视 image_seen=0；外部许可未独立再判 | S06:§matisse L849-861 / S09:C13 / S10:honest_limits / S08:§6 | sections | available | path §2/§5/§8.8；mech F.2；think — |
| **L23** | observation | `[归纳]` | §4 六参数 P1–P6 弱/中/强三档与默认值（85/7/80/50/90·60/70） | S01:L76-87 / S02:L53-64 | sections | available | path §3 M10/§4 A/§5；mech A |
| **L24** | observation | `[归纳]` | **P4 边界注（克里姆特接口）**：P4 只调密度、承载面恒为平涂纯色无材质；不含金属/金箔/纹理明度范围/写实面孔×装饰；交给克里姆特类模块；可被 wave2 推翻 | S01:L88 / S02:L65 / S04:L246,L249 / S05:L250-252 / S08:§2 / S09:C03,C04 | sections | available | path §4 C/§6/§7/§8.1；mech C/D/E/F.5；think §2 D7 |
| **L25** | observation | `[归纳]`（冲突处置） | C-06 硬冲突：马蒂斯「每块 ≥70%」× 毕加索「全帧均值 ≤35%」空交集；轴单主、可拆方案、N4 条件 | S04:L37,L123-134,L314-315(N4) / S08:§3 C-06 / S09:C06 | sections | available | path §6/§7/§8.6；mech D/E；think §2 D2 |
| **L26** | observation | `[归纳]`（冲突处置）+ `[史料]`(Lane B 引文) | C-16 覆盖冲突：Lane B 02 卡 L72「没有高光的平涂」误伤平涂系；N1/N2 反约束带适用域 | S04:L47,L258-270,L305-309(N1/N2) / S07:L72 / S08:§3 C-16 / S09:C07 | sections | available | path §6/§8.6；mech D；think §4 |
| **L27** | observation | `[归纳]`（冲突处置） | C-17 硬冲突：≥20% vs ≤15% 空交集；空白/留白定义对齐 | S04:L48,L272-283 / S08:§3 C-17 / S09:C08 | sections | available | path §1.3/§6/§8.6；mech C/D/E；think §2 D5 |
| **L28** | observation | `[归纳]`（冲突处置） | C-18 退化冲突：平涂无投影 vs 浮雕65%硬边投影；分对象拆、主体掩膜、70/30 | S04:L49,L285-296,L332-333(N9) / S08:§3 C-18 / S09:C09 | sections | available | path §6/§8.6；mech A(P3)/D/E；think §2 D4 |
| **L29** | observation | `[归纳]` | C-15 色数计数口径 + N6：色数上限只约束平涂层；金属/金箔/高光材质层单列、不计色数、面积 ≤5%、明度可 100%（豁免 ≤5% 动态仅限该层） | S04:L46,L244-256,L323-324(N6) / S05:L349(G4) / S08:§2 / S09:C04 | sections | available | path §4 C/§6/§8.3；mech C/D/E；think — |
| **L30** | observation | `[归纳]` | near-miss #9：克里姆特×光琳×马蒂斯三选口径（金属+人物→克里姆特／金·水→光琳／平涂纯色→马蒂斯），同屏分区、金来源不得混用、预检 C-15/C-16 | S04:L355 / S08:§4 / S09:C10 / S10:findings_summary.near_miss_row_9 | sections | available | path §4 C/§6/§7/§8.2；mech D.2/E；think §2 D7 |
| **L31** | observation | `[归纳]` | §3 组合规则 N1/N2/N3/N4/N6/N9（轴所有权、反约束适用域、可拆判别、色数口径、组合卡验收）；N3 规定冲突轴整条移除而非调档 | S04:L305-333 / S02:L69-75(冲突注记) | sections | available | path §1.6/§8.6；mech D；think §2 D9 |
| **L32** | observation | `[史料]`（AUDIT 实测） | 7/7 matisse.md 行号定位在 conflicts.md 中 stale +6（C-06/C-15/C-16/C-17/C-18+§5），内容完好、定位漂移 | S08:§5 CE-1 / S09:C05 / S10:findings_summary.locator_drift / S04:L385 | sections | available | path §7.3/§8(边界说明)；mech D.3/F.4；think — |
| **L33** | observation | `[史料]`（AUDIT 实测） | near-miss 计数漂移：§4 实有 11 行，但 §5 A/skills 参考/modules 卡仍写「8」；派生文档漂移，归 Lane F/SCHEMA | S08:§5 CE-2 / S09:C11 / S10:findings_summary / S04:L365 | sections | available | mech D.3/F.4 |
| **L34** | observation | `[史料]`（AUDIT 实测） | dossier §11.2 标题「46 行」vs §11 intro/实测 54 行；标题-only 漂移 | S08:§5 CE-3 / S10:findings_summary.timeline_count_discrepancy / S01:L245,L263 | sections | available | mech D.3/F.4 |
| **L35** | observation | `[归纳]` | §8.2-8 把 P4 做成可判定定义；expansion.md §1.5 测试协议①②③（挂负向原文、盲评、记分母） | S05:L252-255 / S01:L193-194 | sections | available | path §4 B；mech B/C |
| **L36** | observation | `[史料]`/`[归纳]` | §2-8 剪纸工艺（助手涂 gouache 纸→剪形→墙面钉放调整→定稿）；§12-7 钉墙 3 轮 | S01:L51,L391 / S05:L254 | sections | available | path §4 A；mech — |
| **L37** | observation | `[史料]` | §7-1/§7-2 馆方深度分析（MoMA Cut-Outs 2014 finish vs process；Tate 120 件 1936–1954、The Snail 等） | S01:L143-150 | sections | available | path §2 表#7；mech — |
| **L38** | observation | `[史料]`（本机素材） | §8.3 野外样本＝拼贴反例卡（影子+噪点+照片网点），删三条即近 §8.1 正向段 | S01:L196-201 | sections | available | path §4 C/§6；mech B(§8.2-2)/E |
| **L39** | observation | `[归纳]` | §1-6 空间＝色面积与方向、无消失点（0–1 个常 0）；§2-7 明暗体系＝色面积体系 | S01:L34,L50 | sections | available | path §3 M6；mech E |
| **L40** | observation | `[自述]` | 「垂直在我精神里……我的曲线不疯狂」（Jazz 1947） | S01:L35,L105-107 / S03:Q12 附近（§5-4） | sections | available | path §3 M7；think §1 S14 |
| **L41** | observation | `[归纳]` | §2-5「装饰性构图」作者自述「Composition is the art of arranging in a decorative manner…」 | S01:L48 `[自述]` [R1] / S03:Q6 关联 | sections | available | think §2 D7（依据 `[自述]` 侧） |
| **L42** | observation | `[归纳]`（本项目设计） | A-30 形状：前置知识/重点作品及来源/要观察机制/具体练习/可观察结果/常见失败/下一步/使用边界；练习效果未人评须标建议练习 | S11:L24 / S12:L269-273,L322 / S13:L62-66 | sections | available | path 卷首/§4/§8；mech 卷首；think 卷首 |
| **L43** | observation | `[归纳]` | §3 创作原则 9 条（表达优先、只画差异、整体先于执行、凝练、转译、形式服从色调比例、不回避影响、打破牢笼、身体记忆） | S01:L57-67 `[自述]` [R1]/[R10]/[R5] | sections | available | think §1/§2 D1-D3 |
| **L44** | observation | `[归纳]` | §12 末组合练习建议分组（1/2/3 色块面积与平面化；4/5/8 变奏节奏；6/7/9 剪纸机制；10 总体设计） | S01:L408 | sections | available | path §2/§4 阶梯分组 |
| **L45** | observation | `[归纳]`（禁令范围） | §8.1 禁令范围注：`--no` 只约束默认/强档输出，不是「马蒂斯从不用明暗/排线」的历史断言；P3 弱档保留体积明暗与透视 | S01:L179 / S02:L—(card §8.1 未含此注) / S05:L250 | sections | available | path §6/§8.4；mech E；think §3/§4 |
| **L46** | observation | `[归纳]` | §8.1 强度旋钮（色数 P2/平涂 P3/剪纸感 P5）与退化修补（扁平插画/矢量干净追加词） | S01:L180-181 | sections | available | path §6/§7.4；mech A |
| **L47** | observation | `[归纳]` | §8.1 `--no` 原文（gradient/airbrush/soft edges/blur/glow/outline stroke/drop shadow/3D/realistic lighting/more than 8 hues/texture noise…） | S01:L170-176 / S02:L29-35 / S05:L254 | sections | available | path §4 B/§6/§8.4；mech B/C/E；等同 L45 的护栏原文 |
| **L48** | observation | `[史料]`（本机素材） | §8.3 拼贴反例卡「影子+噪点+照片」三条；用于 D4/阶梯 C 反例对照 | S01:L198-201 | sections | available | path §4 C/§6（与 L38 同段，分列引用） |
| **L49** | hypothesis | `[归纳]` `[UNVERIFIED]` | §8.2 的 7 条量化阈值未经真实渲染器/像素实测；dossier §10-6 + 自审 D 声明；只能当自查靶值 | S01:L239,L466-467 / S08:§5 CE-4 / S09:C14 / S10:honest_limits | sections | available | path 卷首/§4 B/§5/§8.5；mech F.1；think ⟨H-UNV⟩ |
| **L50** | observation | `[自述]`原则 + 量化`[归纳]` | §1-9 缩略图可读：缩至 64px 仍可辨主体与色块布局 | S01:L37 / S02:L12 | sections | available | path §3 M8/§4 A/§5 |
| **L51** | observation | `[归纳]`（规范） | 练习效果未经真人完成或评价 → 建议练习，不写已证实学习收益；模型/脚本自查≠人评 | S12:L271-273,L308 / S11:L9 / S13:L64-66 | sections | available | path 卷首/§4/§8.7；mech F.3；think 卷首 |
| **L52** | observation | `[归纳]` | P4 边界注可被 wave2 实验推翻；C-15 实测阈值待克里姆特档案落地回填 | S01:L88 / S04:L256 / S05:L252 | sections | available | path §8.1；mech F.5 |
| **L53** | observation | `[推测]` | 马蒂斯—北斋直接影响关系无直接文献支持（仅「受日本艺术影响」`[史料]` [R10]），按 `[推测]` 处理、未写入正文结论；自审 D 已「被推翻」 | S01:L130,L238,L463 / S10:findings_summary | sections | available | path §1.5；think §3 |
| **L54** | observation | `[归纳]` | module card §8.1b（E-02/E1_t1b）：§8.1 仅含装饰母题词、风格可迁移、人物实体化未见；可删母题词更纯净 | S02:L37-39 / S08:§1(card_has_81b=true) / S09:C02 | sections | available | path §7.4；think — |
| **L55** | observation | `[史料]`（自报告）/ `[归纳]` | 缺口：1908/1939 法语原文、Q17/Q19/Q20 原始出处、R14(Met 429)、R15(未核)、Q9 末句截断；本 leaf 未重抓外部 URL、未复核外部许可 | S01:L234-239 / S03:L163-168,L38 / S08:§5 CE-4 / S09:C15 / S10:honest_limits | sections | partial | path §1.7/§8.5/§8.8；mech F.2；think §1 缺口 |
| **L56** | observation | `[归纳]` | S-06 第 4 项：静态图不套用动画专属检查项（Review rubric 对静态图的适配） | S12:L275-280 / S11:L24 | sections | available | path §4 收口/§8.7；mech B(§8.2-6)/E；think §4 |

---

<a id="db-source-line-100"></a>
## 2. 作者自述断言（how-to-think.md §1 的 S1–S14 / ⟨H-S14⟩）

> 这些是 `[自述]`（corpus `[self-written]`/`[reported speech]`）或 `[史料]`（`[contemporary record]`）；**逐条带出处**，不在本表混入任何 `[归纳]` 决策。

| id | grade | claim（简写） | locator | scope | access |
|---|---|---|---|---|---|
| H-S1 | `[自述]` `[self-written]` | 线描是情感最纯粹的翻译；白纸之光不可再添减 | S03:Q1 L10-14 | sections | available |
| H-S2 | `[自述]` `[self-written]` | 素描是表达手段而非技巧表演；简化以求单纯即兴 | S03:Q2 L16-20 | sections | available |
| H-S3 | `[自述]` `[self-written]` | 最简单手段最利表达；刻意风格偏离真实 | S03:Q3 L22-26 | sections | available |
| H-S4 | `[自述]` `[self-written]` | 剪刀直接剪入颜色＝雕塑家的直接雕刻 | S03:Q4 L30-34 / S01:L101-104 | sections | available |
| H-S5 | `[自述]` `[self-written]`（英译；法语原文未取得） | 色彩服务表达；不带预设铺色、保住最初一块、逐步改动其它 | S03:Q5 L36-40 | sections | partial |
| H-S6 | `[自述]` `[self-written]` | 首要追求表达；感受与翻译方式不可分 | S03:Q6 L44-48 / S01:L59,L94-97 | sections | available |
| H-S7 | `[自述]` `[self-written]` | 梦想均衡/纯粹/宁静的艺术，如好扶手椅 | S03:Q7 L50-54 / S01:L108-111 | sections | available |
| H-S8 | `[自述]` `[reported speech]` | 从不回避他人影响；个性在搏斗中生长 | S03:Q8 L56-60 / S01:L65,L112-114 | sections | available |
| H-S9 | `[自述]` `[reported speech]`（末句截断，corpus L167） | 「塞尚若对，我就对」；塞尚的建筑法则 | S03:Q9 L62-66 | sections | partial |
| H-S10 | `[自述]` `[self-written]` | 画家最好的证明来自画布 | S03:Q10 L68-72 | sections | available |
| H-S11 | `[自述]` `[self-written]`（回忆性） | 卢浮宫临摹；「我想理解我自己」；旧书库之喻 | S03:Q11 L76-80 / S01:L127 | sections | available |
| H-S12 | `[自述]` `[self-written]` | 《变奏》：路线毫无预定，「我是被带领的，不是我带领」 | S03:Q12 L82-86 | sections | available |
| H-S13 | `[自述]` `[self-written]` | 先做大量柔软练习以释放优雅自然（舞者/走钢丝者喻） | S03:Q13 L88-92 / S01:L67 | sections | available |
| H-S14 | `[自述]` | 「垂直在我精神里……我的曲线不疯狂」Jazz 1947 | S01:L35,L105-107 | sections | available |

---

<a id="db-source-line-123"></a>
## 3. 决策步骤断言（how-to-think.md §2 D1–D9）

> 全部为**本项目归纳的操作序列** `[归纳]`；「依据」列里的 `[自述]`/`[研究]`/`[史料]` 是所引上游材料的级别，**不改变决策序本身的 `[归纳]`**。

| id | grade | 决策（先选/牺牲） | 依据定位 | scope | access |
|---|---|---|---|---|---|
| H-D1 | `[归纳]`（依据 `[自述]`） | 先定整体色块面积与垂直骨架；牺牲局部/解剖/面部细节 | S01:L61,L46,L47,L82,L179 | sections | available |
| H-D2 | `[归纳]`（依据 `[自述]`；失效 `[归纳]`） | 先落一色再逐步调整到色调比例成立；牺牲理论预设；C-06 条件下失效 | S03:Q5 / S01:L45,L64 / S04:L123-134,L314-315 | sections | available |
| H-D3 | `[归纳]` | 色数 ≤8、每块 S≥70%；牺牲灰阶缓冲；低饱和组合失效 | S01:L186,L80-81,L361 / S04:C-06 L127 | sections | available |
| H-D4 | `[归纳]`（S4 `[自述]`） | 剪影硬边定义形；牺牲明暗/投影/高光；C-18 下须主体掩膜 | S01:L187 / S03:Q4 / S04:L285-296,L332-333 / S01:L464(自审 D 削弱) | sections | available |
| H-D5 | `[归纳]`（S1 `[自述]`） | 负空间当主角（≥20%、间隙 2–12%）；牺牲填满画面；C-17 须定义对齐 | S01:L190,L36,L390 / S03:Q1 / S04:L272-283 | sections | available |
| H-D6 | `[自述]`（取向）+ `[归纳]`（量化/旋钮） | 曲线回应隐含垂直轴；牺牲失控曲线；P6 弱档失效 | S01:L35,L105-107,L188,L85 | sections | available |
| H-D7 | `[归纳]`（依据 `[研究]`+`[自述]`；边界 `[归纳]`） | 装饰与主体同平面；牺牲层级差；进入材质域即失效→克里姆特 | S01:L33,L52,L193,L88,L48 / S04:L355 | sections | available |
| H-D8 | `[归纳]`（工序 `[史料]`/`[研究]`；S12/S13 `[自述]`） | 主题—变奏推进；牺牲一张定稿；单张交付/禁 crossfade 时受限 | S01:L53,L378-381,L192,L191 / S03:Q12,Q13 | sections | available |
| H-D9 | `[归纳]` | 收口跑 §8.2 八条 + P4 边界注判归属；牺牲「差不多就交」 | S01:L177-178,L88 / S04:L305-333 / S12:L280 | sections | available |

---

<a id="db-source-line-141"></a>
## 4. 覆盖与诚实声明

- **分母（同一次统计）**：本表 L01–L56 共 **56** 条主断言 + H-S1–H-S14 **14** 条自述 + H-D1–H-D9 **9** 条决策 = **79** 条；每条都给了 `S:locator` 与 `access_status`，无一条仅凭观感。
- **使用范围**：三份交付文档中出现的 `⟨Lxx⟩` 全部在本表有对应行；`⟨H-…⟩` 在 §2/§3 有对应行。**未出现无名断言**。
- **不升级**：L01/L02/L03/L06/L08/L23/L49 等 `[归纳]` 阈值保持 `[UNVERIFIED]`，不因被本路径引用而变成已验证规则；L55 的 `partial`/缺口保持未知；无 `image_seen` 主张（L22）。
- **不重审**：本表沿用 AUDIT-matisse 已核的输入哈希（S14 / S08 / S09 / S10）与冲突对照结论，未重新抓取外部 URL、未运行渲染器、未做视觉检视、未改 repo。
- **定位纪律**：conflicts.md 内 7/7 旧 `matisse.md` 行号已由 AUDIT-matisse 报告 stale +6（L32）；本表一律给**当前 dossier/card 实测行号**（L186/187/188/189/190/191/192/193/194、L88、L80-85 等），不沿用旧编号。
- **无凭据**：所有源文件、产出文件均不含账号/口令/邮箱/哈希凭据/TOTP；本表仅含内容 sha256（公开文件哈希，非凭据）。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
