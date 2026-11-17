<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-vermeer；原正文 SHA-256 `36d90e4218e9015914fe3bfb353b2877d0a93a5249e343af97f93c31653411cd`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-vermeer — claim / evidence 图（逐 claim 带定位）

> 本图给 [learning_path.md](learning_path.md) / [how-to-think.md](how-to-think.md) / [mechanism_notes.md](mechanism_notes.md) 里**每一条实质 claim** 配 `文件 : 节 : 行号` 定位（dossier / corpus / 卡 / conflicts / AUDIT 产物）。沿用 ACCEPTED 审计 内部证据 afe3a7f6f1ef559f（未公开；来源记录由维护者保留） 的 locator 纪律，不重审。
> 基线 `f008952365a77e140cbda3f3959d43ef000f9a22`（repo READ-ONLY）。等级照录 [vermeer.md](../../dossiers/vermeer.md) L5：`[自述]/[史料]/[研究]/[归纳]/[推测]`。
> **support_status 只评「本机档案内自洽 / 定位可寻址 / 类型正确」**，不评外部原文真伪、不评学习成效（AUDIT 同口径）。
> 输入 hash（开工实测，见 `RESULT.md` §0）：card `c12e8672…`、dossier `6a2020ce…`、corpus `f013eec2…`、conflicts `314a24da…`、caravaggio `64bedbc4…`、AUDIT coverage-manifest `b74d7e0d…`。

---

<a id="db-source-line-10"></a>
## §A 结构性无自述 / 证据分级（learning_path 前置、how-to-think §0/§2）

| claim_id | 内容 | 等级 | 定位 | 来源文件 |
|---|---|---|---|---|
| C-SELF-0 | 维米尔无任何自述留世，`[self-written]` 条目数 = 0（结构性事实，非采集缺口）；本 shard 无一条 `[自述]` | `[史料]`/事实（档案自声明） | [vermeer.md](../../dossiers/_corpus/vermeer.md) L5、L193；[vermeer.md](../../dossiers/vermeer.md) L6、L99、L305；`_crosscheck.md` L114、L150–152、L280；`INDEX.md` L28 | corpus + dossier + crosscheck + INDEX |
| C-CAVEAT-C2 | 禁止把任何档案条目改写为「维米尔说过/写过」 | project rule | [vermeer.md](../../dossiers/_corpus/vermeer.md) L193；[vermeer.md](../../dossiers/vermeer.md) L69、L99、L101 | corpus + dossier |
| C-CAVEAT-C3 | 创作原则/§3/§1/§4/§8.2 只能按 `[归纳]`/研究者假设使用，不得冒充作者内心 | project rule | `_crosscheck.md` L127、L139、L148、L151–152；[vermeer.md](../../dossiers/vermeer.md) L69；[vermeer.md](../../modules/vermeer.md) L76、L90 | crosscheck + dossier + 卡 |
| C-GRADE-DEF | 证据级定义（自述/史料/研究/归纳/推测） | 口径 | [vermeer.md](../../dossiers/vermeer.md) L5；`AUDIT-vermeer/claim-evidence-map.md` L3 | dossier + AUDIT |
| C-A40 | A-40 = wave14 维米尔 §11/§12 加固 + 语料新建 22 条 | `[史料]`（本机记录） | `ops/GOALS.md` L54 | GOALS |
| C-22-QUOTES | 语料 22 条（分母 `grep -c '^### '`），21×`[contemporary record]` + 1×`[later record]`，0×`[self-written]` | supported（本机） | `AUDIT-vermeer/claim-evidence-map.md` §A L7–34；[vermeer.md](../../dossiers/_corpus/vermeer.md) L11–187；`INDEX.md` L13、L28 | AUDIT + corpus + INDEX |

---

<a id="db-source-line-23"></a>
## §B 重点作品及来源（learning_path §2，全部引用现有记录）

| claim_id | 作品（照录 §12 标题/馆藏） | 定位 | 引用性质 |
|---|---|---|---|
| C-W1 | 《倒牛奶的女仆》(c.1658–1661, Rijksmuseum SK-A-2344)：单一事件、数百彩点、材质＝高光形状 | [vermeer.md](../../dossiers/vermeer.md) §12-1 L428–431；§1-4 L34、§1-8 L38；[vermeer.md](../../modules/vermeer.md) §4 P3 L84；`conflicts.md` C-11 L193 | §12 现有记录 + 馆方描述转引 |
| C-W2 | 《戴珍珠耳环的少女》(c.1665, Mauritshuis inv.670)：珍珠＝两笔白、无挂钩、sfumato、暗背景前推 | [vermeer.md](../../dossiers/vermeer.md) §12-2 L433–436；§2-13 L62；§1-7 L37、§1-11 L41 | §12 + Mauritshuis 引文 |
| C-W3 | 《小街》(c.1657–1661, Rijksmuseum)：哑光、暗部平而不死、无人感 | [vermeer.md](../../dossiers/vermeer.md) §12-4 L443–446 | §12 |
| C-W4 | 《蓝衣读信女》(c.1662–1665, Rijksmuseum)：群青权重、限色、暗部纯色平面 | [vermeer.md](../../dossiers/vermeer.md) §12-8 L463–466；§4 P2 L88、P4 L90 | §12 + §4 |
| C-W5 | 《持天平的女人》(NGA 1942.9.97) /《绘画的艺术》(KHM)：单点透视、景深 | [vermeer.md](../../dossiers/vermeer.md) §12-5 L448–451、§12-6 L453–456；§8.2-6 L240 | §12 + §8.2 |
| C-W6 | 《窗前读信的少女》(Dresden, 丘比特覆绘 2021 去除) /《站在维金纳琴前的女子》(NG London, 晚期简化) → 失效边界样本 | [vermeer.md](../../dossiers/vermeer.md) §12-7 L458–461、§12-10 L473–476；§4 P6 L92 | §12 + §4 |
| C-W-RIGHTS | 3 张公开图权利声明可寻址；本 lane image_seen=0、read_scope=metadata、不复制像素 | [manifest.md](../../dossiers/_images/manifest.md)；`AUDIT-vermeer/coverage-manifest.md` §1 L17、§4 L36、L48 | AUDIT + manifest |
| C-W-HUNDREDS | "hundreds of colourful dots" 是 Rijksmuseum 描述（经 §4 P3 转引），非自述、非实测点数 | [vermeer.md](../../dossiers/vermeer.md) §4 P3 L89；[vermeer.md](../../modules/vermeer.md) L84；`conflicts.md` L193 | `[研究]` 馆方描述转引 |

---

<a id="db-source-line-38"></a>
## §C 三个主机制 + 关联机制（learning_path §3 / mechanism_notes §A-§B）

| claim_id | 内容（含数值） | 等级 | 定位 | 卡对应 |
|---|---|---|---|---|
| **C-M1** | 单一事件运动：事件区外帧间差 **Δ≤1%**；运动区域数=1 | `[归纳]` 阈值 / `[研究]` 静默描述 | [vermeer.md](../../dossiers/vermeer.md) §8.2-8 L242；§1-8 L38（[R24]）；[vermeer.md](../../modules/vermeer.md) L74 | 卡 L74 |
| **C-M2** | pointillé 直径 **1–3px@1024**、σ0.5–1px、数量分档 **0–2 / 5–20 / 100+**、圆度>0.7、禁线状 | `[归纳]` 档位 / `[研究]` 形态 | [vermeer.md](../../dossiers/vermeer.md) §8.2-3 L237；§4 P3 L89；§1-4 L34、§1-10 L40；[vermeer.md](../../modules/vermeer.md) L69、L84 | 卡 L69/L84 |
| **C-M3** | 物体边缘过渡带 **≥2px**、禁 1px 描边、Canny 宽度中位数 | `[归纳]` 阈值 / `[研究]` 无硬线 | [vermeer.md](../../dossiers/vermeer.md) §8.2-5 L239；§4 P5 L91；§1-7 L37；[vermeer.md](../../modules/vermeer.md) L71、L86 | 卡 L71/L86 |
| C-M4 | 平坦暗部 std **≤5/255**；EV「flat and virtually unmodulated」 | `[归纳]` / `[研究]` | [vermeer.md](../../dossiers/vermeer.md) §8.2-2 L236；§4 P2 L88；§1-3 L33 | 卡 L68/L83 |
| C-M5 | 单侧左光 ±15°、填充 ≤15% | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) §8.2-1 L235；§4 P1 L87 | 卡 L67/L82 |
| C-M6 | 受光 ≤88%、暗部 ≥8%、禁纯白/纯黑 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) §8.2-7 L241；§1-2 L32、§1-11 L41 | 卡 L73 |
| C-M7 | 色相簇 ≤8、蓝200–230°/黄35–50°、阴影向蓝 ≥15°；单点透视消失点@55–65%、29.3cm | `[归纳]` / `[研究]` Steadman [R14] | [vermeer.md](../../dossiers/vermeer.md) §8.2-4 L238、§8.2-6 L240；§1-6 L36、§1-9 L39；L244 | 卡 L70/L72 |
| C-THRESH-INDUCTION | 全部 §8.2 阈值 `[归纳]`、未经渲染实验校准；档位划分本身 `[归纳]`；未做像素测量 | 口径 | [vermeer.md](../../dossiers/vermeer.md) L244；[vermeer.md](../../modules/vermeer.md) L76、L90；`conflicts.md` §5.D L420 | 卡 + dossier + conflicts |
| C-TRIO | 定调三件套 P1 75% / P2 70% / P6 85%；缺 P2 退化风俗画、缺 P6 变厚涂印象派；P1/P2 定是不是维米尔 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L225；[vermeer.md](../../modules/vermeer.md) L89 | 卡 + dossier |
| C-P3-OVER | P3 100% → 修拉式分割主义越界警报 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L227；§8.1 负向 L229 | dossier |
| C-PERIOD | 早期 P6 30%/P5 30% 硬边、晚期 P6 40% 书法性笔触；成熟期默认不适用 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L226；§12-10 L473–476；§4 P6 L92 | dossier |
| C-81B | §8.1b 纯风格段存在、派生自 §8.1、列删除项；明细 `experiments/E1_t1b/RESULTS_t1b.md §2` 本机 unavailable | partial | [vermeer.md](../../modules/vermeer.md) L43–61；`01-AUDIT.md` L99；`AUDIT-vermeer/RESULT.md` §3、unresolved #3 | 卡 + AUDIT |
| C-83 | §8.3 野外样本「未找到」，首样本待 wave3 | `[史料]`（本机） | [vermeer.md](../../dossiers/vermeer.md) L248 | dossier |

---

<a id="db-source-line-58"></a>
## §D 冲突行 / near-miss（learning_path §4 阶梯、mechanism_notes §D）

| claim_id | 对象 | 双方定位（回源） | 判定 | support_status |
|---|---|---|---|---|
| C-C09 | 梵高×维米尔 运动预算硬冲突 | `conflicts.md` §1 L40、§2 L164–174；`van_gogh.md` L207–208；`vermeer.md` L242 / 卡 L74 | 规则层硬冲突；解法=运动区域数 + 分层掩膜 ≤1°/s | supported |
| C-C11 | 卡拉瓦乔×维米尔 高光计数（条件式） | `conflicts.md` §1 L42、§2 L188–201、§5.B #4 L374；`caravaggio.md` L217；`vermeer.md` L89、L237 / 卡 L84、L69 | **WEAKENED**：维米尔未给 pointillé 亮度阈值 → 「若全帧统计则互斥」；解法=主光斑/点状高光分类 | partial（条件式） |
| C-C08 | 运动模糊关联（维米尔定格） | `conflicts.md` §1 L39、§2 L149–162（L156）；`vermeer.md` L242；`caravaggio.md` L218 | 帧级开关；定格模块在场时全程关闭 | supported |
| C-NM1 | 背景 ≤10% × 暗部 ≥8% → [8,10]%、纯黑收紧 0% | `conflicts.md` §4 L347；`caravaggio.md` L215；`vermeer.md` L241 | near-miss 成立，须显式写值 | supported |
| C-NM2 | 环境光 ≤5% × 填充 ≤15% → ≤5% | `conflicts.md` §4 L348；`caravaggio.md` L214；`vermeer.md` L235 | near-miss 成立 | supported |
| C-NM3 | 主光左上/右上 × 画面左 → 左上 | `conflicts.md` §4 L349；`caravaggio.md` L214；`vermeer.md` L235 | near-miss 成立 | supported |
| C-NM5 | 色相簇 ≤7/≤5/≤8 → ≤5（卡 L99 已声明） | `conflicts.md` §4 L351；`hokusai.md` L200；`picasso.md` L172；`vermeer.md` L238；`AUDIT-vermeer/RESULT.md` L118–120 | near-miss 成立 | supported |
| C-NM7 | 过渡带 ≥2px × ≤0.6% 短边 → [2,11.5] 非空但量纲不同 | `conflicts.md` §4 L353；`vermeer.md` L239；`michelangelo.md` L176；§2 C-02 L76 | near-miss 成立 + 量纲警告 | supported |
| **C-NM8（升级）** | 暗部 std ≤5/255 × 暗区 std ≥1.5/255 → [1.5,5] | `conflicts.md` §4 L354；`vermeer.md` L236；**`caravaggio.md` §8.2-7 L220**「暗区（亮度<0.15）内部亮度标准差 ≥1.5/255（非死黑）」 | **supported**：两端均可寻址。AUDIT 曾判 partial（RESULT L113–116 / claim-evidence-map §E AV-NM8 / unresolved #4），因只核到 L214–215；本 LEARN 回源命中 L220 → 升级 | supported（本 LEARN 实测） |
| C-DRIFT | C-09(L168/169)、C-11(L192/193)、C-02(L76) 共 4 处行号 +1/+2 偏移，内容逐字相符 | `conflicts.md` §5.C L404；`AUDIT-vermeer/RESULT.md` L80、L122 | 文书层定位偏移，非内容冲突；本 lane 不改文件 | supported（observation） |

---

<a id="db-source-line-75"></a>
## §E How-to-Think 决策步（how-to-think.md §1 的 D1–D8，每步带 grade + 定位）

| claim_id | 决策步（先选/牺牲/为什么） | grade | 定位 |
|---|---|---|---|
| C-HT-D1 | 选单一事件、压掉叙事噪音；失效=梵高全画面场(C-09)/运动模糊(C-08) | `[归纳]` 决策 / `[研究]` 静默 | [vermeer.md](../../dossiers/vermeer.md) L38、L76、L78、L242；`conflicts.md` L164–174 |
| C-HT-D2 | 定单侧左窗光 P1 75%；失效=#2/#3 与卡拉瓦乔组合，L228 禁硬光 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L235、L87、L225、L228；`conflicts.md` L348–349 |
| C-HT-D3 | 先定暗部多平 P2 70%/std≤5；失效=#8 区间 [1.5,5]（caravaggio L220） | `[归纳]` / `[研究]` | [vermeer.md](../../dossiers/vermeer.md) L33、L236、L88；`caravaggio.md` L220；`conflicts.md` L354 |
| C-HT-D4 | 细节预算押在高光形状（pointillé 分档/珍珠两笔）；失效=修拉越界(L227)/C-11(L374) | `[归纳]` / `[研究]` | [vermeer.md](../../dossiers/vermeer.md) L237、L89、L40、L71、L77、L62、L227；`conflicts.md` L188–201、L374 |
| C-HT-D5 | 主动删（≥2px/省挂钩）；失效=#7 量纲混测 | `[归纳]` / `[研究]` | [vermeer.md](../../dossiers/vermeer.md) L239、L91、L37；`conflicts.md` L353；`michelangelo.md` L176 |
| C-HT-D6 | 先限色（≤8 色相/蓝黄/冷阴影）；失效=#5 取 ≤5 | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L238、L90、L36、L51；`conflicts.md` L351 |
| C-HT-D7 | 动态范围夹中间（≤88%/≥8%）；失效=#1 背景 [8,10]% | `[归纳]` | [vermeer.md](../../dossiers/vermeer.md) L241、L32、L41、L229；`caravaggio.md` L215；`conflicts.md` L347 |
| C-HT-D8 | 几何+表面收尾（单点透视/P6 85%）；失效=早/晚期弱档 | `[归纳]` / `[研究]` | [vermeer.md](../../dossiers/vermeer.md) L240、L92、L39、L42、L56、L226、L473–476 |
| C-HT-NO-PSYCH | 禁止从画面外观编造作者心理；决策序是研究者构造，不是维米尔内心 | project rule | `00-GOAL.md` L9；`01-AUDIT.md` §8.4 L308；`AUDIT-vermeer/claim-evidence-map.md` §C |
| C-HT-CAMERA | 暗箱之争两派并列、未定论；s'Gravesande 为后世反方记录 | `[研究]` / `[史料]` | [vermeer.md](../../dossiers/vermeer.md) §2-10 L58–59；[vermeer.md](../../dossiers/_corpus/vermeer.md) L182–187 |
| C-HT-SLOW | 产量 2–3 幅/年、分层干燥痕迹；动机不作推断 | `[史料]/[研究]` | [vermeer.md](../../dossiers/vermeer.md) §3-3 L73 |

---

<a id="db-source-line-93"></a>
## §F 练习 / 边界 claims（learning_path §4–§8、mechanism_notes §F）

| claim_id | 内容 | 定位 | status |
|---|---|---|---|
| C-PRACTICE-LADDER | 三段阶梯 single-event room scenes → pointillé highlight studies → quiet-surface discipline | [learning_path.md](learning_path.md) §4；brief 指定顺序；兼容 [vermeer.md](../../dossiers/vermeer.md) §12 序 L426 | 建议练习（设计候选） |
| C-PRACTICE-SUGGESTED | 练习是建议练习，非「已证实学习收益」 | `01-AUDIT.md` §8.1 L273；`human_review.status=not_applicable` | supported（口径） |
| C-OBSERVABLE | 可观察结果=产物自查（帧差图/连通域表/std/边缘宽度），不是学习成效 | [learning_path.md](learning_path.md) §5；[vermeer.md](../../dossiers/vermeer.md) §8.2 L233–242 | `[归纳]` 阈值 |
| C-FAIL-10 | 10 条常见失败（色分解/线状高光/暗部渐层/第二运动/纯黑纯白/#7 混测/C-11 误计/冒充自述/晚期当成熟期/静默折中） | [learning_path.md](learning_path.md) §6；逐条见本图 §C/§D | supported（本机自洽） |
| C-NM8-NO-REPO | near-miss #8 升级只记于 LEARN，不改写 conflicts.md / AUDIT 产物；不升级为实验验证 | 本 shard 契约；`conflicts.md` L420 | 口径 |
| C-EXT-UNVERIFIED | 22 条语料原文/英译、[R#] URL/扫描件未逐字回源；本 lane 离线只读本机 | `AUDIT-vermeer/RESULT.md` §2、unresolved #2；`coverage-manifest.md` §4 | unverified（外部） |
| C-REVIEW-NULL | `review:null`、`human_review.status=not_applicable`；作者不自接受 | 本 shard `receipt.json`；AUDIT 同口径 | submitted |

---

<a id="db-source-line-107"></a>
## §G 定位方法（照 AUDIT locator 纪律）

- 所有 `文件 : 行号` 以基线 commit `f008952365a77e140cbda3f3959d43ef000f9a22` 的 live 文件为准；开工用 `sha256sum` 复核（见 `RESULT.md` §0）。
- conflicts.md 内 4 处行号偏移按 `conflicts.md` §5.C L404「先怀疑行号、再怀疑内容」处理：内容逐字相符 → 标「定位偏移」，不判内容冲突、不擅自改文件。
- near-miss #8 的升级证据是现场 `grep -n "1.5" caravaggio.md` + `sed -n '220p'` 逐字命中，登记在 [mechanism_notes.md](mechanism_notes.md) §D「升级记录」；不重审 AUDIT、不把规则层判定升格为实测。
- 证据底本：内部证据 056cb11f78df0e19（未公开；来源记录由维护者保留）（ACCEPTED）——本图复用其 §A/§C/§D/§E 判定与 locator，未重新盘点。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
