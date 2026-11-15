<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-degas；原正文 SHA-256 `6a360111d271fcbc8e9161532bfb927a49c6ab8a10ddb28ba61e7fb237545781`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `degas` §8.1b（draft）

> 比较对象：现有卡 [degas.md](../../modules/degas.md)（`card_sha256=84f6d39f…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `dancers / rehearsal room / theatre interior / adjusting a ribbon, tying a shoe / white tulle, tutus / pastel over monotype` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数（P6 为工作流参数）、冲突注记（C-01/C-05/C-08）。

- **能做**：在「芭蕾/排练室/浴女」**默认题材域**内，用 §8.2 的 8 条（质心+Hough、消失点+区域分割、亮度直方图+光源检测、人脸关键点+姿态、边缘方向场+渐变带+色彩层、姿态+支撑点、SSIM 聚类、底材色+完成度热力图）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-degas 记录 228/228 钉在所跑 checker；§8.1b 排除）。
- **不能做**：**跨场景路由**。把这套「偏心裁切 + 高视点对角 + 人工方向光 + 方向性笔触 + 过程态 + 未完成」迁到机械车间俯拍、工作台特写、UI 取景、无字 key visual 时，§8.1 正向段会强制带回舞者/排练室/纱裙，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。
- **本卡特有的工作流参数**：§4 P6「系列/变体幅度」被归为**工作流参数**（不进画面重叠计算，`expansion.md §4.3 规则 5`），§8.2-7 同标。无 §8.1b 时卡没有把「族谱/变体」写成**可选关系**的写法，跨场景路由容易把「同一姿态 20+ 变体」误当画面内必要像素条件。AUDIT-degas 的 A-55 原书级核验确认「repetition is exactly what the dancers do」是**操作陈述**，不是内心状态证据。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定舞者/场所/媒介名 | 拆成 R1–R8：偏心裁切(质心偏 ≥15% 画宽/切割 ≥1/对角 ≥60%)、高视点(视平线 ≥55%/俯角 10–25%/线族 ≥3)、人工方向光(夹角 ≤45°/亮部 ≤35%)、背面比例(≥1/3 / ≤1/3)、方向性笔触(覆盖 ≥70%/方向族 2–5/渐变带 ≤2% 短边/色层 ≥2)、失衡过程态(重心偏 ≥10% 身高/臂展差 ≥20%)、族谱变体(SSIM ≥0.6，**工作流可选**)、未完成(裸底 ≥5%/完成度差 ≥1 档) |
| **默认题材泄漏剥离表** | 无 | §1 表把 dancers/rehearsal room/tulle/tutus/pastel-monotype 逐项降级；给「迁移判据」；P6 明写为可选族谱关系而非画面像素条件 |
| **必要耦合 C1–C5** | §4 用法「P1/P2/P5 三条 ≥2 条 ≥ 中档」零散 | ⟨R1∧R2⟩ 取景框×高视点、⟨R3∧R5⟩ 人工光×方向性笔触（与莫奈两轴）、⟨方向族 2–5 × 修拉点阵⟩ 同轴互斥、⟨R6∧R4⟩ 过程态×背面、⟨R8∧R7⟩ 未完成×变体 |
| **正例 + 强反例** | 卡只有同域自查三问 | 机械车间/工作台俯拍正例（八条全可算，无需认出舞者/排练室）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理改均匀点阵/sfumato / 反转空间改正面居中舞台全景 / 保留赭棕色板撤人工方向光与亮部集中 / 内容泄漏反证（把芭蕾舞者升为必要条件会误判车间俯拍与 sculpture variant） |
| **适用/不适用 + 组合预检** | 散落 | 6 类不适用 + C-05（与达·芬奇硬冲突、与梵高/莫奈/塞尚同侧但机制不同——「描线成面」）/C-01/C-08 与 §3.1 莫奈 70/30、修拉表面系统不叠加 |

**路由收益（一句话）**：从「认出芭蕾排练 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意偏心取景/人工光场景是否满足取景框×高视点、人工光×方向笔触耦合」；跨场景判定**不再依赖舞者识别**，且把变体/重复明确归到工作流层。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[degas.md](../../modules/degas.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在芭蕾默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L254 / §10-5 L298），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-degas]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-degas]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） degas `card_has_81b=false`；AUDIT-degas/receipt.json + quote_audit.md（accepted；A-55 Moore 1891 / Vollard 1927 八条原书级核验；13 张公开图含 1 CC BY-SA）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
