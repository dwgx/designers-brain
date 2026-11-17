<a id="db-source-line-1"></a>

> 公共知识投影；源任务 LEARN-cezanne；原正文 SHA-256 `fbcb837b614c8402780ecf5b85cbd755cf2f155d005e4d5930c622a0fe08c95d`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# LEARN-cezanne — claim_evidence_map

> `locator` = `文件 : 行号`（或 `文件 : 节 : 行号`），相对 **READ-ONLY repo** 内部证据 db3a99569f8d41cd（未公开；来源记录由维护者保留） @ `f008952365a77e140cbda3f3959d43ef000f9a22` 解析；`A/*` 相对 内部工作区 内部证据 0ed20c3499324da5（未公开；来源记录由维护者保留）。
> `grade` = repo 内原文证据等级（verbatim）：`[自述]` / `[史料]` / `[研究]` / `[归纳]` / `[推测]`；语料类型 `[self-written]` / `[reported speech]` / `[contemporary record]` 按 `C : L4` 交叉表对应。`support_status` 判断「本路径里该论断按其引用是否被支持」。`read_scope` 是本轮实际读取范围。
> 本轮**未联网重抓**任何 §9/§11.3 外部底本（`A/coverage_manifest.md` §3 L48：availability=`unknown`）；3 张 JPG 仅字节校验、`read_scope=metadata`，**非 `image_seen`**（`A/coverage_manifest.md` §3 L47）。
> 别名：`D`=档案 [cezanne.md](../../dossiers/cezanne.md)、`M`=模块卡 [cezanne.md](../../modules/cezanne.md)、`C`=语料 [cezanne.md](../../dossiers/_corpus/cezanne.md)、`X`=[conflicts.md](../../../../cross/conflicts.md)、`A`=内部证据 0ed20c3499324da5（未公开；来源记录由维护者保留）、内部证据 45095df41e6342ca（未公开；来源记录由维护者保留）= campaign package `01-AUDIT.md` / `02-EXECUTION-PLAN.md` / `00-GOAL.md`。各文件 sha256 见 `raw/input-hashes.txt`。

<a id="db-source-line-8"></a>
## §A — 路径形状与契约（learning_path.md 的结构性 claims）

| claim_id | claim | grade | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| L01 | A-30 每位路径至少 8 节：前置知识/重点作品及来源/要观察的机制/具体练习/可观察结果/常见失败/下一步/使用边界 | `[史料]`（契约文本） | supported | 内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.1 L271 | sections |
| L02 | 所引用作品与权利信息沿用现有记录；练习效果未由人完成/评价时明确为「建议练习」，不写「已证实学习收益」 | `[史料]`（契约文本） | supported | 内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.1 L273；§9 L322「学习建议不冒充学习成效」 | sections |
| L03 | Lane B 练习顺序：观察对象→创作决策→机制→参数→一次可做的练习→反例→自检；自述与推断决策程序分开 | `[史料]`（契约文本） | supported | 内部证据 8d639d70db06b341（未公开；来源记录由维护者保留） : §「Lane B」L64 | sections |
| L04 | How to Think 必须区分作者可核实的自述与研究者推断，不能编造作者心理 | `[史料]`（契约文本） | supported | 内部证据 c89c2d672fd51dc9（未公开；来源记录由维护者保留） : L9；内部证据 8d639d70db06b341（未公开；来源记录由维护者保留） : L66 | sections |
| L05 | 人评未提交前保持 pending/未评；Agent 数值核验不得冒充人评或审美通过 | `[史料]`（契约文本） | supported | 内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.4 L306–310、L308；§9 L322 | sections |
| L06 | 本任务 required_artifact_kinds = result_summary / learning_path / mechanism_notes / claim_evidence_map；依赖 AUDIT-cezanne；写路径仅 内部证据 9657f37f6a3bc3e7（未公开；来源记录由维护者保留） | `[史料]`（账本） | supported | 内部证据 4ae7502a27185a8e（未公开；来源记录由维护者保留） : L693–714；内部证据 5bb16c2a50dc0e26（未公开；来源记录由维护者保留） : L1541–1578 | sections |
| L07 | §3 创作原则是从作品/书信/资料归纳的操作规则，不冒充艺术家真实内心 | `[归纳]`（项目口径） | supported | `D` : L5；`D` : L66 | fulltext |
| L08 | 证据分级定义（自述/史料/研究/归纳/推测） | `[归纳]`（项目定义） | supported | `D` : L4；`C` : L4 | fulltext |
| L09 | Gasquet「对话」为文学性重构，可靠性低于书信；不作第一手引语 | `[归纳]` | supported | `C` : L6；`C` : L167；`A/RESULT.md` : §2.2 L47–52 | fulltext |
| L10 | 「绝交信」旧说 OVERTURNED（A-36），不得重引入 | `[史料]` | supported | `A/RESULT.md` : §2.1 L37–45；`C` : Q18 L123–127、Q19 L129–133；`D` : §11.2 L272 | fulltext |

<a id="db-source-line-23"></a>
## §B — 四个 brief 指定参数（学习路径 §3 / mechanism_notes §2 的核心 claims）

| claim_id | claim（含阈值） | grade（repo 原文） | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| P01 | **笔触覆盖率 ≥80%**（边缘检测密度判定）；长轴 8–24 px；4–8 角度族；同族偏差 ≤25° | `[归纳]` | supported | `D` : L176（§8.2-1）＝`M` : L66；`X` : L116 引 `cezanne.md` L175 | fulltext |
| P02 | **全帧 L\* 直方图无单一桶占比 >20%**（防大面积均匀天空块）；暖冷像素各 30–70% | `[归纳]` | supported | `D` : L182（§8.2-7）＝`M` : L72；`X` : L101 引 `cezanne.md` L181 | fulltext |
| P03 | **阴影与轮廓区域蓝色像素（H 200–250°）占比 ≥15%**；天空/地面平均饱和度差 ≤15% | `[归纳]` | supported | `D` : L179（§8.2-4）＝`M` : L69；`X` : L221 引 `cezanne.md` L178 | fulltext |
| P04 | **远景物体高度 ÷ 近景同类物体高度 ≥0.5**（空间压缩）；两条近水平结构线夹角 ≥2° | `[归纳]` | supported | `D` : L180（§8.2-5）＝`M` : L70；`X` : L181 引 §8.2-5 L179 | fulltext |
| P05 | §4 P1–P6 参数（弱/中/强 + 默认建议）全部 `[归纳]` | `[归纳]` | supported | `D` : L68–77＝`M` : L75–84；`A/RESULT.md` : §4 L73（`_extract.py --check` 228/228） | fulltext |
| P06 | P1 默认中强、P3 默认强档「仍像塞尚的关键」、P4 默认中强、P5 默认中档 12% 左右、P6 默认中档 5–8% | `[归纳]` | supported | `D` : L72 / L74 / L75 / L76 / L77 | fulltext |
| P07 | §8.1 正向段写「blue…(12–15% of pixels)」，与 §8.2-4 的「阴影+轮廓区 ≥15%」是不同作用域口径 | `[归纳]`（本路径 reconciliation） | supported | `D` : L154＝`M` : L26（12–15% 全画面）；`D` : L179（≥15% 阴影+轮廓） | fulltext |
| P08 | §8.2 是「把塞尚视觉语言翻译成可逐帧自查的量化规则」——阈值用途是自查，不是史料 | `[归纳]` | supported | `D` : L174；`M` : L64 | fulltext |
| P09 | 色阶建模配套：近黑 L\*≤10 像素 ≤0.5%；单物色相 ≥3、明度级 ≥5；64×64 块 L\* 梯度均值 ≤2 | `[归纳]` | supported | `D` : L177（§8.2-2）＝`M` : L67 | fulltext |
| P10 | 轮廓配套：线宽 2–4 px；≥30% 轮廓段断口/第二重线（错位 ≥3 px） | `[归纳]` | supported | `D` : L178（§8.2-3）＝`M` : L68 | fulltext |
| P11 | 未完成配套：≥5% 面积保留底色（ΔE ≥15） | `[归纳]` | supported | `D` : L181（§8.2-6）＝`M` : L71 | fulltext |
| P12 | 金字塔骨架：重心三角形面积 ÷ 画面 ≥0.25 | `[归纳]` | supported | `D` : L183（§8.2-8）＝`M` : L73 | fulltext |
| P13 | 防退化关键：模型默认用「黑阴影 + 渐变」塑形；负向段前两项 + 正段 `never by black shading` 必须保留 | `[归纳]`（使用说明） | supported | `D` : L169；`M` : L33–39（负向段）；`D` : L158（正段 `never by black shading`） | fulltext |
| P14 | 强度建议：印象派期放大笔触/亮色板/去 multiple outlines；立体主义前夜 P4 拉满 + 角度族收到 3 个 | `[归纳]` | supported | `D` : L168；`D` : L126 | fulltext |

<a id="db-source-line-42"></a>
## §C — 作品、来源、机制观察（learning_path.md §2/§3）

| claim_id | claim | grade | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| W01 | 能力定位 = 结构 / 体积 / 空间构成 | `[研究/归纳]` | supported | `D` : L15；[README.md](../../modules/README.md) : L16（`A/RESULT.md` §4 L73） | fulltext |
| W02 | 关键作品 3–5 件（浴者 NG6359 / 大浴者 PMA / 玩纸牌者 Courtauld / 有蓝水壶的静物 NG L696 / 圣维克多山系列） | `[史料]` | supported | `D` : L16–21 | fulltext |
| W03 | §12 临摹/学习清单 9 件，按「结构→静物→人物→晚期→水彩→立体主义前夜」排序 | `[归纳]`（清单） | supported | `D` : L312–361；`D` : L314；`A/coverage_manifest.md` §2 L38（9/9） | fulltext |
| W04 | §9 参考资料 [1]–[18] 全部 URL 编号清单 | `[史料]` | supported | `D` : L189–210 | fulltext |
| W05 | §11.3 S1–S16 独立编号；S15 Wikipedia 为三手、S4/S16 书目/摘要级 | `[史料]` | supported | `D` : L287–306；`D` : L308 | fulltext |
| W06 | 建设性笔触约 1880 起，NG 原句「constructive stroke…unify the entire surface」 | `[研究]` | supported | `D` : L25；`D` : L42（§2-3） | fulltext |
| W07 | 色阶代替明暗：用红↔绿强度差塑形（NG 「instead of using shading…different intensities of red and green」） | `[研究]` | supported | `D` : L26；`D` : L34（暖冷交错） | fulltext |
| W08 | 蓝网贯穿（阴影/轮廓/天空/远山）；浴者蓝色断裂轮廓 + 黑加固 | `[研究]` | supported | `D` : L28；`D` : L45；`D` : L338 | fulltext |
| W09 | 反大气透视：天空与大地同样实、纵深不靠变淡 | `[研究]` | supported | `D` : L29；`D` : L30（视点游移，Met） | fulltext |
| W10 | 多点透视：桌沿错位、圆斜看不画成椭圆 | `[研究]` | supported | `D` : L43；`D` : L30 | fulltext |
| W11 | 四阶段作画流程（NG 对未完成静物的逐层复原） | `[研究]` | supported | `D` : L40（§2-1）；`D` : L326–329（§12-3） | fulltext |
| W12 | 未完成 = 工序外显，不是随意（自审 B-4 OVERTURNED） | `[归纳]`（自审结论） | supported | `D` : L375；`D` : L31（MoMA purposeful unfinish） | fulltext |
| W13 | 「全画无黑」修正为「无黑阴影（L\*≤10 ≤0.5%），保留黑色用于轮廓加固与最深点」（B-5 WEAKENED） | `[归纳]`（自审结论） | supported | `D` : L376；`D` : L338（NG reinforced by black） | fulltext |
| W14 | 练习产物含临摹照片按 `_private/` 留档、勿入公开仓 | `[归纳]`（清单说明） | supported | `D` : L361 | fulltext |
| W15 | 3 张 JPG 为 CC0 1.0（Met Open Access），仅字节校验、未解码 | `[史料]`（manifest） | supported | `A/RESULT.md` : §4 L72；`A/coverage_manifest.md` §3 L47；`_images/manifest.md` : L35–37、L835–847 | metadata |

<a id="db-source-line-62"></a>
## §D — How to Think 的自述 / 转述锚点（how-to-think.md §3A）

| claim_id | 原话（摘录） | grade / type | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| Q01 | «traitez la nature par le cylindre, la sphère, le cône…»（1904-04-15 致 Bernard） | `[self-written]`≈`[自述]` | supported（repo 侧有底本，未联网复核） | `C` : Q1 L11–15；`D` : L55（§3-1）；F1 互证 `D` : L213 | fulltext |
| Q02 | «Les lignes parallèles à l'horizon donnent l'étendue… une somme suffisante de bleutés, pour faire sentir l'air» | `[self-written]`≈`[自述]` | supported | `C` : Q1 L12；`D` : L56（§3-2）；`D` : L81–83（§5-1） | fulltext |
| Q03 | «Le dessin et la couleur ne sont point distincts…» | `[reported speech]`（Bernard《L'Occident》1904 p.24） | supported | `C` : Q2 L17–21 | fulltext |
| Q04 | «On ne devrait pas dire modeler, on devrait dire moduler.» | `[reported speech]` | supported | `C` : Q3 L23–27；`D` : L41（§2-2 引「光对画家并不存在」`[自述]`） | fulltext |
| Q05 | «Il n'y a pas de ligne, il n'y a pas de modelé, il n'y a que des contrastes…» | `[reported speech]` | supported | `C` : Q4 L29–33 | fulltext |
| Q06 | «L'ombre est une couleur comme la lumière…» | `[reported speech]` | supported | `C` : Q6 L43–47 | fulltext |
| Q07 | «Je vous dois la vérité en peinture et je vous la dirai.»（1905-10-23） | `[self-written]`≈`[自述]` | supported | `C` : Q10 L69–73；`D` : L61（§3-7）、`D` : L90–92（§5-4） | fulltext |
| Q08 | «Je procède très lentement, la nature s'offrant à moi très complexe…»（1904-05-12） | `[self-written]`≈`[自述]` | supported | `C` : Q15 L101–105；`D` : L60（§3-6） | fulltext |
| Q09 | 「我不想在理论上正确，我要在自然中正确」/「别当艺术批评家，去画」 | `[自述]` | supported | `D` : L58（§3-4）；`D` : L87–89（§5-3） | fulltext |
| Q10 | 「感觉的实现（réalisation de sensations）仍然非常吃力」 | `[自述]` | supported | `D` : L63（§3-9）；`D` : L96–98（§5-6） | fulltext |
| Q11 | §3 第 1–9 条出自 1904–1906 致 Bernard/儿子书信；第 10 条为 Gasquet 转述、`[史料]`、不作一手 | `[归纳]`（口径注） | supported | `D` : L66 | fulltext |

<a id="db-source-line-78"></a>
## §E — 明确排除、不得当自述（how-to-think.md §3B）

| claim_id | 被排除的句子 | 排除理由 | grade | support_status | source_ref (locator) |
|---|---|---|---|---|---|
| E01 | 「风景在我之中思考，我是它的意识」 | Gasquet 转述，B-2 WEAKENED，降为 `[史料]`、不作一手引语 | `[史料]` | supported（降级已核） | `D` : L64、`D` : L99–101、`D` : L373；`C` : L6 |
| E02 | Gasquet 对话体 Q8/Q9/Q11 | 文学性重构，可靠性低于书信 | `[reported speech]` | supported | `C` : L6、`C` : Q8 L55–59 / Q9 L61–65 / Q11 L75–79；`A/claim_evidence_map.md` §B L34/35/37 |
| E03 | 「With an apple I will astonish Paris」「My one and only master」 | 单源/转述/无一手文本；B-3 WEAKENED | `[史料]` | supported | `D` : L222、`D` : L374、`D` : L118；`A/RESULT.md` §5 L79 |
| E04 | 1886-04-04 信 = 「绝交信」 | A-36 OVERTURNED，1887-11-28 信证伪 | `[史料]` | supported（OVERTURNED 已核） | `A/RESULT.md` §2.1 L37–45；`C` : Q18 L123–127、Q19 L129–133 |
| E05 | 任何从作品外观反推塞尚心理的命题 | `00-GOAL.md` L9 / `D` : L5 明禁 | — | not_applicable（本路径未写此类命题） | 内部证据 c89c2d672fd51dc9（未公开；来源记录由维护者保留） : L9；`D` : L5 |

<a id="db-source-line-88"></a>
## §F — 冲突行（mechanism_notes.md §3；grep 结果见 `raw/conflicts-grep.txt`）

| claim_id | claim | grade | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| F01 | C-04 = 塞尚 × 卡拉瓦乔「直方图单桶上限」，硬冲突；cezanne 侧 §8.2-7 无单一桶 >20% `[归纳]` | `[归纳]` | supported | `X` : §1 L35；`X` : L97–107（L101 双方原文、L103 后果、L105–107 处置）；`A/RESULT.md` §3 L60/L64 | sections |
| F02 | C-04 处置 = 可拆（N4）：作用域改「受光区 + 中间调区」，双掩膜分别统计 | `[归纳]`（source 处置） | supported | `X` : L105–107；`X` : L314–315（N4）；`A/claim_evidence_map.md` §D L70 | sections |
| F03 | C-04 强反例「两条同时执行则卡拉瓦乔的背景压暗机制被拆掉」 | `[归纳]` | supported | `X` : L103 | sections |
| F04 | C-10 = 莫奈 × 塞尚「深度衰减」，硬冲突；cezanne 侧 §4 P4 + §8.2-5 反大气透视 / ≥0.5 `[归纳]` | `[归纳]` | supported | `X` : §1 L41；`X` : L176–186（L181 双方原文、L182 后果、L184–185 处置）；`A/RESULT.md` §3 L61 | sections |
| F05 | C-10 处置 = 可拆（N3 轴所有权 + N4 分层）：远景层用莫奈包络、中近景用塞尚压缩、梯度只在远景层内拟合；无分层则深度轴单主 | `[归纳]`（source 处置） | supported | `X` : L184–185；`X` : L311–312（N3）；`A/claim_evidence_map.md` §D L71 | sections |
| F06 | C-10 强反例「远景既没雾也没压平」 | `[归纳]` | supported | `X` : L182 | sections |
| F07 | C-13 = 塞尚 × 卡拉瓦乔「阴影色相」，硬冲突；cezanne 侧 §8.2-4 蓝 ≥15% `[归纳]` | `[归纳]` | supported | `X` : §1 L44；`X` : L217–227（L221 双方原文、L223 后果、L225–227 处置）；`A/RESULT.md` §3 L62 | sections |
| F08 | C-13 处置 = 可拆（N4 区域改写）：作用域收窄「轮廓区 ±2 px 带」，暗部色相归深棕、分掩膜统计 | `[归纳]`（source 处置） | supported | `X` : L225–227；`X` : L314–315（N4）；`A/claim_evidence_map.md` §D L72 | sections |
| F09 | C-13 强反例「丢掉深棕底这一核心机制」 | `[归纳]` | supported | `X` : L223 | sections |
| F10 | N3 轴所有权表：每轴一个持有者；辅模块冲突轴 §8.2 规则整条移除（不是调档） | `[归纳]`（治理规则） | supported | `X` : L311–312 | sections |
| F11 | N4 可拆判别：同一像素统计量→不可拆二选一；可分空间区域→可拆但须写死分区表 + 掩膜定义 | `[归纳]`（治理规则） | supported | `X` : L314–315 | sections |
| F12 | C-05（塞尚 × 达·芬奇/梵高/莫奈，笔触可见度）是第 4 条涉塞尚冲突，但**不在本 brief 指派集合**，交持有 lane | `[归纳]` | supported（out-of-scope 记录） | `X` : §1 L36；`X` : L109–121；`A/coverage_manifest.md` §2 L42；`A/claim_evidence_map.md` §D L74 | sections |
| F13 | 三条 cezanne 侧冲突规则全部 `[归纳]`（非塞尚本人文字） | `[归纳]` | supported | `A/RESULT.md` §3 L64；`X` : L101/L181/L221 各条尾注 `[归纳]` | sections |
| F14 | 模块卡 `M : L90–93` 冲突注记指向 C-04/C-05/C-10/C-13；能力行列此四条 | `[归纳]` | supported | `M` : L86–93；[README.md](../../modules/README.md) : L16（`A/RESULT.md` §4 L73） | fulltext |

<a id="db-source-line-107"></a>
## §G — 练习（learning_path.md §4；全部「建议练习」，非已证实收益）

| claim_id | claim（练习动作） | grade | support_status | source_ref (locator) | read_scope |
|---|---|---|---|---|---|
| X01 | A0：6 色、≤1 cm 平行短笔触铺满、禁黑/禁渐变；3 明度层底稿 → 4–6 方向族重画 | `[归纳]`（练习配方） | supported（改编自现有 §12 配方，非新事实） | `D` : L319（§12-1）、`D` : L349（§12-7 6 色）、`D` : L169 | fulltext |
| X02 | 阶梯 1 暖冷编织；对照练习 A 版近暖远冷 / B 版冷暖互换 | `[归纳]` | supported（照录 §12-2） | `D` : L321–324（§12-2）；判据 `D` : L182 | fulltext |
| X03 | 阶梯 2 轮廓两遍留 ≥30% 断口 → 蓝重描 + 局部黑加固 → 按规则 3/4 自查 | `[归纳]` | supported（照录 §12-5） | `D` : L339（§12-5 三步）；判据 `D` : L179、`D` : L178 | fulltext |
| X04 | 阶梯 3 桌面两侧不共线、远景抬到 ≥0.5；A 忠实写生 / B 块面+色阶、方向族收到 3 个 | `[归纳]` | supported（照录 §12-9 + §12-3） | `D` : L356–359（§12-9）、`D` : L326–329（§12-3）；判据 `D` : L180 | fulltext |
| X05 | 四阶段工序逐段拍照、停在第三阶段即合格 | `[归纳]` | supported（照录 §12-3） | `D` : L329；`D` : L40 | fulltext |
| X06 | 练习规模 15×20 / 30×40 / 40×50 cm、20 分钟分阶段 | `[归纳]` | supported（照录 §12） | `D` : L314、L319、L329 | fulltext |
| X07 | 所有练习为「建议练习」，本轮无人完成/无人评价/无模型审美评审，不写「已证实学习收益」 | `[史料]`（契约 + 本轮事实） | supported | 内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.1 L273、§8.4 L306–310；本轮 `receipt.json` `human_review.status=not_applicable` | sections |
| X08 | 可观察结果是画面数值自查，不是学习成效/审美通过 | `[归纳]`（本路径口径） | supported | 内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.4 L308；`D` : L174 | sections |

<a id="db-source-line-120"></a>
## §H — 使用边界与未决项（learning_path.md §7/§8）

| claim_id | claim | support_status | source_ref (locator) |
|---|---|---|---|
| B01 | 单分片 1/76，不代表 76/76 或 18 冲突全核验 | supported | `A/coverage_manifest.md` §1 L5、§2 L42 |
| B02 | 外部底本本轮未联网复核，availability=`unknown` | supported（限制如实记录） | `A/coverage_manifest.md` §3 L48；`A/RESULT.md` §5 L80 |
| B03 | §10 七项缺口（`D : L221–227`）与语料三项缺口（`C : L165–169`）保持原状 | supported | `D` : L221–227；`C` : L165–169；`A/coverage_manifest.md` §2 L34–35 |
| B04 | §8.1b 推导日志 [RESULTS_t1b.md](../../../../../experiments/E1_t1b/RESULTS_t1b.md) 于 pinned commit 不存在（未找到） | supported | `A/RESULT.md` §5 L77；`A/receipt.json` unresolved[0]；`A/raw/e1t1b-check.txt` : L2–4 |
| B05 | `images_manifest=false`：无逐画家 MANIFEST.md；权利信息只在全局 manifest | supported | `A/RESULT.md` §5 L78；`A/coverage_manifest.md` §3 L49 |
| B06 | X: L186「建议补一组 莫奈+塞尚 E2」是建议口径，不是已跑过的组合 | supported | `X` : L186；`A/RESULT.md` §3 L61 |
| B07 | 本路径状态 submitted、review=null、human_review=not_applicable；作者不自我接受 | supported | `receipt.json`；`A/RESULT.md` §6 L88 |
| B08 | C-05 与其余 75 位 artist 属各自 lane；本回执不代写 A-30 总路线 | supported | `A/coverage_manifest.md` §2 L42；内部证据 f27236748bc78087（未公开；来源记录由维护者保留） : §8.1 L271、L273 |

<a id="db-source-line-133"></a>
## §I — 分母与核对

- 本表 claim 条目：§A 10 · §B 14 · §C 15 · §D 11 · §E 5 · §F 14 · §G 8 · §H 8 = **85** 条，每条至少 1 个 locator。
- 输入文件分母（开工实测 sha，见 `raw/input-hashes.txt`）：`D` 441 行 · `M` 99 行 · `C` 169 行（24 quote Q1–Q24）· `X` 421 行 · `A` 三份证据基。四份 repo 文件 sha 与 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） L109–119 及 `A/coverage_manifest.md` §1 全部一致。
- `grep -n "塞尚\|cezanne" X` 命中 20 行，存 `raw/conflicts-grep.txt`；C-04/C-10/C-13 三段全文另见 `A/raw/conflicts-cezanne.txt`（`A/RESULT.md` §3 L64）。
- **未声称**：`image_seen`（图片未解码）、外部网页重抓、真人评价、模型审美评审、76/76 覆盖、18 冲突全核验、练习收益。这些按 `01-AUDIT.md` §8.4 / §9 保持准确状态。
- 所有 `[归纳]` 决策序命题（S1–S8）性质见 [how-to-think.md](how-to-think.md) §3C：研究者假设，不冒充塞尚真实心理；`[推测]` 计数 = **0**。

## 同一条目的附页

- [learning_path.md](learning_path.md)
- [how-to-think.md](how-to-think.md)
- [mechanism_notes.md](mechanism_notes.md)
- [source-claims.json](source-claims.json)
