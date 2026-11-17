<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-hopper；原正文 SHA-256 `93c9676c60f8d3a5b1d82301c17b8da1e6f3c1e1749542f5b536689463d1edcc`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `hopper` §8.1b（draft）

> 比较对象：现有卡 [hopper.md](../../modules/hopper.md)（`card_sha256=2b964115…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。[STYLE-hopper]

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

**能做**：在「美式都市/海岸 20 世纪场景」**默认题材域**内，用 §8.2 的 8 条（梯度宽度中位数、投影主轴直方图、霍夫直线、人物+视线、直方图+色相聚类、光源连通域、帧差图、边界框相交）自查 §8.1/§8.2/§4 逐字一致（AUDIT-hopper 记录 §8.1b 被排除在逐字比对之外）。

**不能做**：**跨场景路由**。把「硬边光 × 正交几何 × 人烟预算 × 画中框」迁到抽象展厅、UI 仪表盘、建筑立面、空舱界面时，§8.1 正向段会强制带回 diner / gas station / hotel room、美国时代地域与「frozen stillness just before or after an event」的叙事情绪，把内容对象当风格前提。

**本卡特有的未消歧张力（AUDIT-hopper accepted 登记）**：§4 P1 弱档「漫射柔光」被明写为**越界：进入维米尔档**，分工注 L98 写死「柔窗光 + 点状高光组合禁止同档出现」；无 §8.1b 时卡没有「柔光是不适用条件而非可选弱档」的拆法，跨场景容易在组合时把维米尔柔光与霍珀硬边光混档。另有 Lane B C-01「别做成硬阴影」反约束须同口径显式改写（AUDIT-hopper counterexample 已登记其 near-miss）。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
| --- | --- | --- |
| 介质/语义无关的关系量 | §8.1 绑定 diner/gas station/hotel room、美国 20 世纪、孤寂情绪、窗门器物 | 拆成 R1–R8：硬边(过渡带 px/羽化)、投影(方位偏差°/边数)、正交(夹角°/矩形块数)、人烟(人数/面积/视线)、明度(色相簇/亮暗占比/光池面积)、光源(个数/照射面)、静止(帧间差%/闪烁 Hz)、画中框(裁切数/偏心宽比)——全是梯度/角度/霍夫/直方图/帧差统计量 |
| 默认题材泄漏剥离表 | 无 | §1 表把场所专名/时代地域/孤寂情绪/窗门器物/色名逐项降级；给「迁移判据」：撤掉专名后 §8.2 八条**全部仍可算** = 纯风格（霍珀八条本就是纯几何/光度量） |
| 档位硬边界显式化 | 卡内分工注散落 | §1 注把 P1 弱档柔光写成**不适用条件**而非可选弱档；C1 登记硬边×投影双护栏、C5 登记夜档光池×光源数；§5 列 Lane B C-01 同口径改写 |
| 正例 + 强反例 | 卡只有同域自查三问 | 抽象几何展厅 + 建筑立面/空舱界面正例；counterexamples.md 4 条 [inference]：撤硬边改柔窗光 / 反转几何改曲线居中 / 保留色板改人群运动 / 内容泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 7 类不适用（维米尔柔光、sfumato 雾、印象派笔触、人群运动、卡拉瓦乔烛光、霓虹怀旧、荷兰室内）+ 维米尔二选一分区、C-01 改写预检 |

**路由收益（一句话）**：从「认出 diner/夜街题材 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意建筑/界面帧是否满足硬边光×投影几何、正交矩形×偏心画中框等耦合，并按 P3/P4 档位决定人烟与日/夜光源数」；跨场景判定**不再依赖餐馆或美国街景**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[hopper.md](../../modules/hopper.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。[STYLE-hopper]
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）` （hopper 专属口径：量纲取自 §8.2 L240-247 的「硬边光影」与 §4 L87-98 档位表，跨场景迁移不改此量纲。），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-hopper]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-hopper]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） hopper `card_has_81b=false`；AUDIT-hopper/receipt.json + RESULT.md（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
