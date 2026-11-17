<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-bruegel；原正文 SHA-256 `1535c91871714243f61775e8cfcc7bc02bb06b1ae1d2fe99059f9bb23165025d`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `bruegel` §8.1b（draft）

> 比较对象：现有卡 [bruegel.md](../../modules/bruegel.md)（`card_sha256=672040c3…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `village, fields, river / dozens of small anonymous figures … reaping, skating / one unified seasonal key / Netherlandish Proverbs / Children's Games` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记。

- **能做**：在「尼德兰全景/农民/季节/谚语画」**默认题材域**内，用 §8.2 的 8 条（地平线检测+透视、实例分割+聚类+姿态去重、场景分类、HSV 掩膜、多尺度能量、亮度+Hough、姿态比例、梯度带宽+高光计数）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-bruegel 记录 228/228 有效性钉在所跑 checker 内容，§8.1b 被排除）。
- **不能做**：**跨场景路由**。把这套「高视点 + 分布式多实例 + 无中心 + 单基调 + 微缩细节 + 漫射软光」迁到数据可视化、城市俯瞰信息图、密集型 UI、无字 key visual 时，§8.1 正向段会强制带回村庄/农民/雪/谚语，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。
- **本卡特有注意**：§8.2-2 的 `≥30 人`、§8.2-3 的 `≥3 类活动`、§8.2-5 的 `高度 ≤ 画高 1/15` 都以「人/实例」为分母；无 §8.1b 时卡没有「实例类别可替换」的写法，跨场景路由容易把「人」写死。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定地物/人物/季相/谚语 | 拆成 R1–R8：高视点(地平线 %画高/俯角/消失点组)、分布式实例(计数/最大聚类/重复率)、共时性(活动类/无汇聚)、色相族 ≤4、微缩尺度(高度比/2–16px)、前景暗框(明度差/导引线)、反理想比例(高肩比/对称站姿)、漫射软光(带宽/高亮连通域/暗部 V)——换实例类别仍逐帧可算 |
| **默认题材泄漏剥离表** | 无 | §1 表把 village/figures/snow/Proverbs/encyclopedia 逐项降级；给「迁移判据」；显式注明「换成非人物实例时须声明实例类别已替换，不可把人写死」 |
| **必要耦合 C1–C5** | §4 用法/越界警报零散 | ⟨R1∧R2∧R6⟩ 全景骨架、⟨R2∧R3∧R5⟩ 百科细节、⟨R4∧R8⟩ 统一基调×漫射光、⟨红锚点×分布⟩、⟨P6 编码密度可关⟩；路由时知道哪些参数不能单独调 |
| **正例 + 强反例** | 卡只有同域自查三问 | 数据可视化/城市俯瞰正例（≥60 微缩图标、八条全可算，无需认出村庄/农民）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理改概括大笔 / 反转空间改平视单点透视+向心集中 / 保留土色板撤软光暗框 / 内容泄漏反证（把农民/谚语/冬季升为必要条件会误判纯观察档） |
| **适用/不适用 + 组合预检** | 散落 | 7 类不适用 + C-12（蓝仅作远景，不主张 ≥40%）/C-01/§3.1 与北斋·米开朗基罗·博斯 70/30 主导轴 |

**路由收益（一句话）**：从「认出尼德兰全景 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意满幅多实例场景是否满足高视点×无中心×微缩×漫射光耦合」；跨场景判定**不再依赖农民/雪/谚语识别**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[bruegel.md](../../modules/bruegel.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在全景/农民默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L200 / §10-4 L239），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-bruegel]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-bruegel]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） bruegel `card_has_81b=false`；AUDIT-bruegel/receipt.json（accepted；72 claim 行全 locator 可解析、0 处野外样本卡）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
