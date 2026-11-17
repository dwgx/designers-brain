<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-gauguin；原正文 SHA-256 `9608101a9aed0582b4646bf7a323fcedf13bb9ca4d7ecf7865e9cc5098032d64`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `gauguin` §8.1b（draft）

> 比较对象：现有卡 [gauguin.md](../../modules/gauguin.md)（`card_sha256=bb5a3059…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。[STYLE-gauguin]

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

**能做**：在「布列塔尼/塔希提/宗教幻象」**默认题材域**内，用 §8.2 的 8 条（分区统计、暗像素掩膜、色彩量化+点阵检测、边界梯度、透视检测、渲染级别比对、色相异常、光流）自查 §8.1/§8.2/§4 逐字一致（AUDIT-gauguin 记录 §8.1b 被排除在逐字比对之外）。

**不能做**：**跨场景路由**。把「平涂 × 景泰蓝轮廓 × 象征色 × 层叠浅空间」迁到抽象海报、图标族、数据色阶、无字 key visual 时，§8.1 正向段会强制带回白帽农妇、calvary、vahine、芒果林与可读的「神秘/原始」语义，把内容对象当风格前提。

**本卡特有的未消歧张力（AUDIT-gauguin accepted 登记）**：§4 P3 象征色强度（默认 70%）与 §8.2-7「非自然色区 ≥8% 面积 + 须能指出主题对应」绑定了语义对应层；无 §8.1b 时卡没有「对应层可选、色相异常关系必选」的拆法，跨场景容易把「能指出宗教/神话/异域对应」误当无条件阈值。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
| --- | --- | --- |
| 介质/语义无关的关系量 | §8.1 绑定白帽农妇、calvary、vahine、偶像、朱红/铬黄色名 | 拆成 R1–R8：平涂(区明度σ/色相Δ/渐变带面积)、暗轮廓(明度/线宽/覆盖率)、色数(主色数/点阵命中)、硬边界(梯度带/明度跳变)、浅空间(消失点/色带层数)、装饰同权(渲染级差/面积)、象征色(非自然色区面积)、静止(光流/模糊核)——全是分区/边缘/色相/透视统计量 |
| 默认题材泄漏剥离表 | 无 | §1 表把农妇/十字架/vahine/果林/偶像/色名/情绪词逐项降级；给「迁移判据」：撤掉专名后 §8.2 自查仍可算 = 纯风格；R7 只保留「色相异常区面积」，主题对应语义不迁 |
| 分工轴显式化 | 卡内越界警报散落 | C1–C5 列出 ⟨平涂×暗轮廓⟩、⟨平涂×零点阵⟩、⟨硬边界×暗轮廓⟩、⟨浅空间×装饰同权⟩、⟨象征色×主色≤10⟩，对应马蒂斯/修拉/梵高/蒙克四条越界 |
| 正例 + 强反例 | 卡只有同域自查三问 | 抽象色带海报 + 图标族/数据色阶正例；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤平涂改点阵 / 反转空间改透视 / 保留色名改宽渐变+厚涂 / 内容泄漏反证（农妇升必要条件会误判抽象正例） |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 7 类不适用（点阵、渐变笔触、厚涂振动、深空间、物理变形、纯装饰配比、运动镜头）+ §3.1 四轴预检 |

**路由收益（一句话）**：从「认出塔希提/布列塔尼题材 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意平涂/版式场景是否满足平涂×描边、零点阵×硬边界等耦合，并按 P3/P4/P5 档位决定是否带象征色/装饰层」；跨场景判定**不再依赖白帽农妇或十字架**。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[gauguin.md](../../modules/gauguin.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。[STYLE-gauguin]
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）` （gauguin 专属口径：量纲取自 §8.2 L219-226 的「平涂色块」与 §4 L92-102 档位表，跨场景迁移不改此量纲。），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-gauguin]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-gauguin]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） gauguin `card_has_81b=false`；AUDIT-gauguin/receipt.json + RESULT.md（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
