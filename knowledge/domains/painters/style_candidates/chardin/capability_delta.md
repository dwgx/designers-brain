<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-chardin；原正文 SHA-256 `e60c2132a8119b593f5909c0b2097a9bfe7751ba205bd179795b524816c927e9`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `chardin` §8.1b（draft）

> 比较对象：现有卡 [chardin.md](../../modules/chardin.md)（`card_sha256=df57eb65…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 `copper cauldron / earthenware jug / glass bottle / loaf / game and fruit / 18th-century French still life` 写死为题材**）、§8.2 八条逐帧规则、§4 六参数、冲突注记（C-01/C-05/C-11/C-12/C-13）。

- **能做**：在「 humble domestic 静物」**默认题材域**内，用 §8.2 的 8 条（高频能量图+梯度方向直方图、高光连通域形态+色相相关矩阵、直方图+阴影区统计、边缘密度分区+透视线、饱和度+色相聚类、材质分区、帧差图+光流、底色检测+边缘宽度）自查；`_extract.py --check` 校验 §8.1/§8.2/§4 逐字一致（AUDIT-chardin 记录 228/228 钉在所跑 checker，§8.1b 排除）。
- **不能做**：**跨场景路由**。把这套「中间档可辨纹理 + 宽软互映高光 + 暖暗部 + 浅中性场 + 静止」迁到工业材质样张、产品微距、包装特写、抽象表面、无字 key visual 时，§8.1 正向段会强制带回铜锅/面包/野味，把内容对象当风格前提 → 01-AUDIT.md A06 的混淆。
- **本卡特有的中间档定位**：§8.2-1 明写「可辨笔触 30–80%（介于『不可见』与『全覆盖』之间）」+ 方向峰值 ≤35%（与塞尚 4–8 角度族切开）。无 §8.1b 时卡没有把「触感/反光网络」从「静物器物」里拆出来的写法，跨场景路由容易把「画的是不是静物」当判据——而 chardin 与**同样画静物/室内的维米尔**的差别恰全在表面/高光关系。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 绑定器物清单与年代体裁 | 拆成 R1–R8：可辨纹理(面积 0.30–0.80/粒径 2–8px/方向峰值 ≤0.35)、宽软高光(圆度/长宽比/σ/跨物 ≥2 处)、暖暗部(纯黑 ≤0.5%/阴影 H/暗部 σ)、浅空间(背景密度比/主体 ≥0.50/无网格)、暖土色预算(中位饱和/高饱和/色相簇)、材质专属表面(≥2 类/共用处理=0)、静止(0 模糊帧/Δ≤1%)、完成度(裸底/边缘过渡/块内梯度) |
| **默认题材泄漏剥离表** | 无 | §1 表把器物名/18 世纪法国/具体互映对象/人物档/humble elevated 逐项降级；给「迁移判据」：撤掉器物名后 §8.2 自查仍可算 |
| **必要耦合 C1–C5** | §4 用法「P1+P2 两条 ≥ 中档」零散 | ⟨R1∧R6∧R8⟩ 触感三件套、⟨R2∧R3∧R5⟩ 反光网络×暖暗部、⟨R4∧R8⟩ 浅空间×密实表面、⟨P4 光质柔和×R3⟩ 硬光即失效、⟨P6 时期滑轨⟩ 只改权重不改存在 |
| **正例 + 强反例** | 卡只有同域自查三问 | 工业材质样张正例（拉丝金属/磨砂玻璃/颗粒陶，八条全可算，无需认出铜锅/面包）+ 无字 key visual；[counterexamples.md](counterexamples.md) 4 条 [inference]：撤纹理压成 levigated 平滑面 / 反转空间改深单点透视+地砖网格 / 保留暖土色板撤跨物反光与暖暗部 / 内容泄漏反证 |
| **适用/不适用 + 组合预检** | 散落 | 6 类不适用 + C-01/C-05（「可见但非全覆盖」显式取值）/C-11/C-12/C-13 与 §3.1 维米尔 70/30、塞尚 N4 分轴 |

**路由收益（一句话）**：从「认出静物 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意多材质浅空间静帧是否满足触感中间档×宽软互映×暖暗部耦合」；跨场景判定**不再依赖器物识别**，且与同题材的维米尔/塞尚按关系轴而非题材轴区分。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[chardin.md](../../modules/chardin.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**（`card_has_81b=false`）。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在静物默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：正例/反例全部 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`（§8.2 注 L212 / §10-7 L281），不升级为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-chardin]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-chardin]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md L145/L149；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） chardin `card_has_81b=false`；AUDIT-chardin/receipt.json（accepted；A-92 Cochin/Diderot 闭环、37/37 引文）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
