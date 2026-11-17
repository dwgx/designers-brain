<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-friedrich；原正文 SHA-256 `c054127461aac4aab90f49872fecc065a01dcd5e801eca11545aea2a2bae48d1`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `friedrich` §8.1b（draft）

> 比较对象：现有卡 [friedrich.md](../../modules/friedrich.md)（`card_sha256=5a26ced2…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `a single figure seen from behind / land, water, sky / a cross on a rock, a Gothic ruin, a bare oak / mist veils and snow haze / the sublime` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记（C-01/C-09/C-12）。

- **能做**：在「背影人凝视风景/雾海」**默认题材域**内，用 §8.2 的 8 条（人脸关键点+中轴、光流+模糊核、水平带分割、Hough+消失点、亮度质心+剪影、HSV 掩膜、对象检测+位置、梯度带宽+多尺度能量）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-friedrich 记录 228/228 钉在所跑 checker；§8.1b 排除）。
- **不能做**：**跨场景路由**。把这套「水平层带 + 无透视轴 + 逆光剪影 + 冻结 + 冷调低饱和 + 雾面软光」迁到抽象层带构成、无人物纯风景、无字 key visual、静帧海报时，§8.1 正向段会强制带回背影人/十字架/哥特废墟，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。
- **本卡最关键的档案自审结论**：dossier 自审 B2（`friedrich.md` L411）清点图库 12 件、**5/12 无人物**（《冰海》《瓦茨曼山》《山十字》《孤独的树》等），把「Rückenfigur 是核心指纹」判为 **WEAKENED（限定已内建）**，结论「核心是**凝视结构**，不要求必须有人物；参数表兜底」；§8.1 中文说明也写「《海边僧侣》档…**无人物也成立**——纯风景 + 层带 + 逆光即可」。AUDIT-friedrich 的 counterexample 把「Rückenfigur-only identity 张力」标为 `[inference]`。**无 §8.1b 时，卡正文仍把背影人写在正向段首句**，跨场景路由会重复把人物当必要条件——这是本批 8 张里最明确由档案自审亲自削弱过的默认题材泄漏。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定背影人/象征物/自然物 | 拆成 R1–R8：背向/中轴/小尺度（**条件关系，P1 弱档允许 0 人**）、冻结(≤0.5%/帧/无模糊核)、水平层带(≥3 条/倾角 ≤3°/天空 ≥40%/带内密度 ≤0.8×)、无透视轴(消失点=0/向心斜线对 ≥1)、逆光剪影(明度差 <−0.15/光源上 1/3/高亮 ≥2 成带)、冷调低饱和(中位 ≤0.35/三族 ≥80%/高饱和块=0)、象征点(**P6 可关，0–1**)、软光雾面(带宽 ≥2%/暗部 V≥0.05/高光块=0/2–8px) |
| **默认题材泄漏剥离表** | 无 | §1 表把背影人/十字架/枯橡树/land-water-sky/sublime 逐项降级；给「迁移判据」；§1 注直接引用自审 B2 的 WEAKENED 结论，把 R1/R7 写成**条件/可选**关系 |
| **必要耦合 C1–C5** | §3.1 判据散落 | ⟨R3∧R4∧R5⟩ **凝视结构三件套（不依赖人物）**、⟨R2∧R8⟩ 冻结×雾面软光、⟨R5∧R6⟩ 逆光×冷调、⟨R1∧R7⟩ 可选人物×可选象征、⟨R8 无纯黑×卡拉瓦乔⟩ |
| **正例 + 强反例** | 卡只有同域自查三问 | 抽象层带构成/**零人物零象征**正例（八条全可算，无需认出背影人/十字架，且与自审 B2「5/12 无人物」一致）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理改硬边平涂+glossy / 反转空间改深线性透视+事件动势 / 保留冷调色板撤逆光剪影与向中轴收束 / 内容泄漏反证（把背影人/十字架升为必要条件会误判纯风景档） |
| **适用/不适用 + 组合预检** | 散落 | 7 类不适用（含**明确允许无人物、无象征物**）+ C-01/C-09 冻结侧/C-12 与 §3.1 透纳 70/30、康斯泰勃尔、蒙克、普桑分工轴 |

**路由收益（一句话）**：从「认出背影人 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意层带/逆光/冻结场景是否满足凝视结构三件套，并按 P1/P6 档位决定是否带人物/象征层」；跨场景判定**不再依赖背影人或十字架识别**，且与档案自审 B2 的 WEAKENED 结论对齐。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[friedrich.md](../../modules/friedrich.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`），其 §8.1 正向段仍以背影人开头。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在凝视风景默认题材域内自查，但**不获得**跨场景路由能力，且「人物是否必要」的泄漏风险仍在卡正文里。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L198 / §10-4 L246；该行写「九条规则」，§8.2 实为 8 条，AUDIT 已登记文档口径差，本段按实有 8 条取），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-friedrich]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-friedrich]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） friedrich `card_has_81b=false`；dossier 自审 B2 L411（WEAKENED，5/12 无人物）；AUDIT-friedrich/receipt.json + counterexample.md（accepted；12 张 PD、Rückenfigur-only identity 张力 [inference]）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
