<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-el_greco；原正文 SHA-256 `e29dce2c5894a85958ee51186e32fd389d5b150fea530ff0e79285aef688f548`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `el_greco` §8.1b（draft）

> 比较对象：现有卡 [el_greco.md](../../modules/el_greco.md)（`card_sha256=068fb227…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `saints, martyrs, the Virgin / long thin hands / Byzantine undercurrent, Greek-letter inscription / sulphurous yellow-greens / each figure carries its own light` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记（C-01/C-05/C-09/C-12）。

- **能做**：在「宗教/圣像/托莱多」**默认题材域**内，用 §8.2 的 8 条（实例分割框比例、轮廓环带边缘密度+法线、HSV 掩膜面积、阴影方向场+分区亮度、熵图+直线检测、轮廓跟踪+折角、光流直方图、色相直方图面积预算）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-el_greco 记录 228/228 钉在所跑 checker；§8.1b 排除）。
- **不能做**：**跨场景路由**。把这套「纵向拉伸 + 火舌碎边 + 酸色红事件 + 自有光 + 云幕 + 弱上升」迁到抽象柱体/光柱构成、无字 key visual、动态海报时，§8.1 正向段会强制带回圣徒/圣母/希腊文题记，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。S-06 无文字 key visual 边界下，正向段里的 `Greek-letter inscription` 更是必须剥离的内容文字。
- **本卡特有的变形边界**：§8.2-6「形体连续性（折角段 = 0）」是与毕加索区分的写死判据；§8.1 `[portrait variant]` 与中文说明「早期/意大利档把 P1 降到 20–30%（只剩威尼斯色）」说明连**纵向拉伸都是合法弱档**。无 §8.1b 时卡没有把这些写成「档位/关系」的写法，跨场景路由容易把「拉长」或「圣徒」误当无条件前提。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定圣像学/人物/色名 | 拆成 R1–R8：纵向拉伸(框高宽 ≥3.5/头身 ≤0.11/断裂 ≤1/折角段=0)、火舌碎边(环带密度 ≥1.5×/段长 ≤1.5% 短边)、非现实色(≥2 区块各 ≥5%/红 ≤12% 最高饱和/中位饱和 ≤0.55)、自有光(方向一致性 ≤0.3/亮度离散 ≤0.15/高光域 ≥4)、云幕(熵 ≤0.7×/地平线 ≤1/收敛 ≤2)、弱上升场(v_y<0/\|v_y\| ≤1.5% 短边/帧)、主色族 ≤3+红事件、薄罩染无厚涂 |
| **默认题材泄漏剥离表** | 无 | §1 表把 saints/martyrs/Virgin、long thin hands、Byzantine/Greek-letter、具体色名、inner radiance bleaches the robes 逐项降级；给「迁移判据」；S-06 下不补任何题记 |
| **必要耦合 C1–C5** | §3.1 判据散落 | ⟨R1∧R2∧R8⟩ 连续拉长×火舌碎边×薄罩染（与毕加索/梵高分界）、⟨R4∧R5⟩ 自有光×云幕、⟨R3∧R7⟩ 酸色+红事件两口径、⟨R6∧R4⟩ 弱上升×自有光、⟨P1/P3/P4 三档滑轨⟩（P1 弱档合法） |
| **正例 + 强反例** | 卡只有同域自查三问 | 抽象柱体/光柱正例（八条全可算，无需认出圣徒/圣母）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理改厚涂能量场 / 反转空间改深线性透视+单一外光 / 保留酸色板撤纵向拉伸与形体连续性 / 内容泄漏反证（把圣徒/题记升为必要条件会误判 portrait variant 与抽象构成） |
| **适用/不适用 + 组合预检** | 散落 | 6 类不适用 + C-01/C-05（「可见碎笔触但无厚涂堆料」）/C-09 弱上升/C-12（蓝为罩染层积）与 §3.1 蒙克 70/30、毕加索、卡拉瓦乔分工轴 |

**路由收益（一句话）**：从「认出圣像/托莱多 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意纵向构成是否满足连续拉长×自有光×云幕×酸色预算耦合，并按 P1/P3/P4 档位取强度」；跨场景判定**不再依赖宗教人物识别**，且不违反 S-06 无文字边界。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[el_greco.md](../../modules/el_greco.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在宗教/圣像默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L237 / §10-8 L289），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-el_greco]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-el_greco]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） el_greco `card_has_81b=false`；AUDIT-el_greco/receipt.json（accepted；17 张公开图全 PD、1 处语料覆盖缺口、1 处文档自相矛盾、1 处跨文档计数漂移 —— 本段只取 §8.2/§4 关系，不触碰事实层）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
