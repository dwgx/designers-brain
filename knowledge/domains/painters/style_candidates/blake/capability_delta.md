<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-blake；原正文 SHA-256 `eb0c9e09470454d470a6f78e1bae0804674151fe2a18224bb396c792c2d98d2a`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `blake` §8.1b（draft）

> 比较对象：现有卡 [blake.md](../../modules/blake.md)（`card_sha256=b34b0c4a…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `Urizen/Los/Orc/Albion` 命名神谱、heroic muscular bodies、hand-lettered verse、illuminated page 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记（C-07/C-14/C-16）。

- **能做**：在「幻视书页/神谱版画」**默认题材域**内，用 §8.2 的 8 条（Sobel 边缘+线宽剖面、交叉排线 0 命中、文字区 5–35%、平涂 ≤10 主色、单中心辐射、非重力动态、神谱锚点、页面框对称）自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致（AUDIT-blake 记录 §8.1b 被排除在逐字比对之外）。
- **不能做**：**跨场景路由**。把这套「线体系 + 平涂 + 单中心光 + 中心/涡旋对称」迁到抽象徽章、图标族、产品爆炸图、无字 key visual 时，§8.1 正向段会强制带回命名神话人物与可读经文，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- **本卡特有的两处未消歧张力（AUDIT-blake accepted 登记）**：§4 P4 弱档 `0%` × §8.2-3 `5–35%`；§4 P6 强档 `≥20%` × §8.2-5 `≥8%`。无 §8.1b 时，卡没有「文字带 / 辐射装置是**档位可选层**」的写法，跨场景路由容易把这两个量误当无条件阈值。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质/语义无关的关系量** | §8.1 绑定命名神谱、裸体、经文、illuminated page | 拆成 R1–R8：硬轮廓(边界覆盖/过渡带 px/线宽比)、交叉排线命中=0、同墨同层手写质感带(面积比 0 / 0.05–0.35)、平涂(区明度Δ/主色数/金占比)、单中心辐射(射线数/面积/画内光源)、非重力动态(轴偏角/无支撑)、锚点计数、轴对称/旋转对称分量——全是像素/几何/层统计量 |
| **默认题材泄漏剥离表** | 无 | §1 表把 `Urizen/Los/Orc`、heroic nude、hand-lettered verse、visionary/religious、器物清单逐项降级；给「迁移判据」：撤掉专名后 §8.2 自查仍可算 = 纯风格；R3/R7 只保留**计数/面积/层关系**，语义不迁 |
| **张力显式化** | 卡内两处下限互斥未处理 | §1 注把 P4 写成**档位开关**（大彩色版画档 0% / 书页叙事档 5–35%），把 P6 的 8–20% 区间标为「须显式取值」；C1–C5 列出 ⟨铁丝轮廓×无排线⟩、⟨平涂×单中心光⟩、⟨中心对称×单中心光源⟩、⟨同版关系⟩、⟨单色墨档重配⟩ |
| **正例 + 强反例** | 卡只有同域自查三问 | 抽象徽章正例（八条全可算，无需认出神话人物）+ 图标族正例（S-06 无字）；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理改交叉排线 / 反转空间改散点分布 / 保留淡彩色板改 sfumato+独立字体层 / 内容泄漏反证（把命名神谱升为必要条件会误判大彩色版画档） |
| **适用/不适用 + 组合预检** | 散落在越界警报 | 列 7 类不适用（排线、sfumato、点阵、分布式无中心、纯情绪变形、金>5%、S-06 关闭文字带）+ C-07/C-14/C-16 预检 |

**路由收益（一句话）**：从「认出幻视书页 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意线描/版式场景是否满足硬轮廓×无排线、平涂×单中心光等耦合，并按 P4/P6 档位决定是否带文字/辐射层」；跨场景判定**不再依赖命名神谱或可读经文**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[blake.md](../../modules/blake.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在幻视书页默认题材域内自查，但**不获得**跨场景路由能力，也不解决 P4/P6 两处张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L221 / §10-6 L265），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-blake]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-blake]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） blake `card_has_81b=false`；AUDIT-blake/receipt.json + counterexample.md（accepted，两处阈值张力）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
