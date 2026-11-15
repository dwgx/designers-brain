<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-namatjira；原正文 SHA-256 `3bb9e36a85c3392c2762d182ccdb0caa8c914a36698c28706ad64ffa316c1238`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `namatjira` §8.1b（draft）

> 比较对象：现有卡 [namatjira.md](../../modules/namatjira.md)（`card_sha256=9126af70a17d…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 纳马吉拉 默认题材专名写死为题材**）、§8.2 逐帧规则、§4 六参数、冲突注记。

- **能做**：在「中部澳大利亚水彩风景」**默认题材域**内，用 §8.2 的 8 条(分带色相直方图、带划分、色相聚类、连通域明度筛选、分块纹理、明度分层、帧差/OCR)自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-namatjira 记录 §8.1b 被排除在逐字比对之外)，并保留 R8 伦理合规。
- **不能做**：**跨场景路由**。把「远山蓝紫位移 + 高地平线层带 + 空场天空 + 分层罩染 + 静场」迁到抽象分带色阶图、UI 背景、数据带时，§8.1 正向段会强制带回中部澳大利亚地名、乡国圣地语义、ghost gum 树肖像与「land itself is the portrait」阐释，把内容对象当风格前提(且触 ICIP 风险) → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- ****本卡特有的双重张力(AUDIT-namatjira 登记)**：§8.2-8 是伦理验收层而非视觉关系、不可删；§4 P4 弱档「阴影平涂(无受光逻辑)」× §8.2-6「每块≥3 明度台阶、无单色平涂大块」为平涂/分层两写。无 §8.1b 时卡没有「P4 是峡谷档位开关、R8 单列不进风格判定」的写法，跨场景路由易把弱档误当无条件阈值、或漏掉伦理层。**

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| 介质/语义无关的关系量 | §8.1 绑定中部澳洲地名/乡国/圣地/ghost gum 树肖像 | 拆成 R1–R8：分带 ΔH、地平线/层带/天空、色相簇/饱和、白干值/干宽/分叉、云占比、明度台阶、帧间差/调制、合规零命中——全是色相/带划分/聚类/帧差/OCR 统计量 |
| 默认题材泄漏剥离表 + 伦理层 | 无 | §1 表把 Central Australia/Hermannsburg/named country、ghost gum/峡谷山系专名、土色清单、材料史、神圣仪式图式逐项降级；给迁移判据：撤专名后 §8.2 自查仍可算 = 纯风格；R8 单列为**伦理验收层(不进风格判定、不可删)** |
| 张力显式化 | 卡内 P4 弱档/R8 层级未处理 | §1 注把 P4 标为「单侧受光未启用的峡谷档、须显式取值」，把 R8 标为伦理层；C1–C5 列出 ⟨远山位移×高地平线⟩、⟨土色预算×分层罩染⟩、⟨天空空场×静场⟩、⟨剪影择一×层带⟩、⟨伦理层不可删⟩ |
| 正例 + 强反例 | 卡只有同域自查三问 | 抽象分带色阶图正例(八条全可算，无需认出乡国)+ UI 数据带正例；[counterexamples.md](counterexamples.md) 3 条 [inference]：撤静场改事件光色 / 保留色板改云型系统 / 内容-伦理泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 6 类不适用(湿润农事、事件光色、互补霓虹、单色平涂、神圣图式、恩格瓦雷默认组合)+ §4 分工注/§8.1 越界警报/C-09/C-06 预检 |

**路由收益（一句话）**：从「认出中部澳洲风景 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意分带/层带场景是否满足远山位移×高地平线、空场×静场等耦合，并保留 R8 伦理零命中」；跨场景判定**不再依赖地名、圣地语义或树肖像**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：回退契约：staging-only 草案；[namatjira.md](../../modules/namatjira.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查(含伦理层)，但**不获得**跨场景路由能力，也不解决 P4/R8 两处张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **本稿不是实测报告**：正/强反例均为 `[inference]` 纸面判定；分带色相位移与静场是否在真实渲染器成立、E4 是否预注册，本 lane 未做。纳马吉拉 §8.2 注 / §10-12 的 `[归纳]` 与 R8 伦理层均不升级、不删除。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-namatjira]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-namatjira]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） namatjira `card_has_81b=false`；AUDIT-namatjira/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
