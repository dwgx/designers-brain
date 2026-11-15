<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-aivazovsky；原正文 SHA-256 `c69b17266cda46214ad6907039fffd9b21053d70c3d6bc771bce788e31c124b8`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `aivazovsky` §8.1b（draft）

> 比较对象：现有模块卡 [aivazovsky.md](../../modules/aivazovsky.md)（`card_sha256=883b9681…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（**候选 §8.1b 草案**）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡包含：视觉指纹要点（浓缩 5 条，仍带「透明浪体/月光路径/海景」题材词）、§8.1 图像 prompt（**英文正向段把海/浪/月/船/人写死为题材**）、§8.2 八条逐帧可判定规则、§4 六参数三档表、冲突注记、来源。

- **能做**：在「海景/浪/月光海」这一**默认题材域**内，用 §8.2 的 8 条逐帧自查 + §4 参数档位判定「像不像艾瓦佐夫斯基」；`_extract.py --check` 的 228/228 只校验 §8.1/§8.2/§4 逐字一致（AUDIT-aivazovsky 记录 `_extract.py` L21-22 **排除 §8.1b**）。
- **不能做**：**跨场景路由**。skill 在「把这套视觉语言迁到非海景题材」（玻璃静物、抽象光场、无字 key visual、UI 主视觉）时，卡里唯一可粘贴的 §8.1 正向段会强制带回 `marine / sea / full moon / ships / tiny human figures`，等于把内容对象当风格前提 → 要么生成不对题的「海」，要么无法判定迁移后是否仍成立。这正是 01-AUDIT.md A06「『有模块』『能抽取』『已做纯风格迁移』被混为一谈」所指的缺口。

<a id="db-source-line-12"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| **介质无关的关系量** | §8.1 正向段绑定「水/海/月/船」 | 拆成 R1–R8：透光阶梯(ΔL/级/带宽)、单连通路径柱(连通域/画高%/宽度比)、水平分界(位置/倾角/面积比)、双色温(HSV 面积)、剪影明度差、频域能量比、帧间光流——全是像素/几何/统计量，**换介质仍逐帧可算** |
| **默认题材泄漏剥离表** | 无 | §1 表逐项把 `marine/full moon/ships/figures/sky/storm` 降为可选基底，并给「迁移判据」：撤掉介质名词后 §8.2 自查仍可写成与题材无关的量 = 纯风格候选；并按 C-05 收紧——「可迁」≠「已在非海景实测通过」，逐格适用性见 §7 |
| **必要耦合 C1–C5** | §4 用法/越界警报有零散提示，未成关系图 | 显式写 ⟨R1∧R2∧R7⟩ 透光体积、⟨R3∧R5⟩ 单柱×双色温、⟨R4∧R6⟩ 低分界×剪影、⟨R8∧R1⟩ 悬停×阶梯、⟨R5 银灰档例外⟩；路由时知道**哪些参数不能单独调** |
| **正例（跨场景）+ 强反例** | 卡只有同域自查三问 | 玻璃/抽象正例（关系层可写，非实测通过）+ [counterexamples.md](counterexamples.md) 的 4 条 `[inference]` 书面失效规格；均为 draft / E4-unexecuted |
| **S02 题材独立性修复（C-05）** | 旧 STYLE 稿 R7/C1 仍靠「泡沫/非泡沫」语义掩膜、R8 靠「落水线」、§5⑤ 按「冰封/冻海」对象类别整类排除 | R7/C1 改写为 `B`（高亮高频带）/`S`（平滑透射主体层）/`E_hi` 算子；R8 改写为长水平亮度不连续 `D` + 闭合度 + 悬停预算（无 `D` 时 ① 走 not-applicable、其余仍判）；frozen-sea 排除改为分类性纹理均匀度检验 `T_u`（`B` 近空/分母无定义 → not-applicable，非因题材名）；新增 §7 玻璃/冰/抽象三例同一张 R1–R8 适用性表，逐格给 applicable/conditional/not-applicable + 理由 |

**路由收益（一句话）**：从「认出这是海景 → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意场景是否满足这些关系 + 是否触发 C1–C5 耦合 / 越界轴」。跨场景判定**不再依赖题材识别**。

<a id="db-source-line-24"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：本产物为 **staging-only 草案**；[aivazovsky.md](../../modules/aivazovsky.md) 在集成写者把 §8.1b 写入之前**保持无 §8.1b**（`card_has_81b=false`）。若本草案未被采纳、或集成未发生，卡**退回**到只有 §8.1/§8.2/§4 的状态：仍可在海景默认题材域内自查，但**不获得**任何跨场景路由能力；不得把「草案已写」记成「卡已具备 §8.1b」。
- **draft ≠ E4 passed**：本草案、§7 适用性表、正/反例全部是 `[inference]` 纸面推演；**未渲染像素、未跑生成通道、未做预注册 E4**（02-EXECUTION-PLAN Lane C）。[counterexamples.md](counterexamples.md) 明确区分「书面失效规格」与「已执行图像测试」，全部标 `draft / E4-unexecuted / written spec only`。所有阈值沿用 dossier `[归纳] 未对原作做像素测量（分母＝假想参考帧）`，不升级为 validated。
- **能力矩阵口径**：本项只登记「§8.1b 候选草案存在 + 跨场景路由的**判定规则/逐格适用性**已写」；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否；「题材独立性」= 纸面约束检查（CE-F4 标签互换规格预注册，未执行）。
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受，能力增量由独立审者复核。S03 修复轮见 `RESULT.md` 修复注记。

<a id="db-source-line-31"></a>
## 4. 依据

- 01-AUDIT.md A06 / §6.3（基线 `style_only_section=11/76`，存在性检查不是 E4 通过检查）；
- 02-EXECUTION-PLAN.md Lane C（只补 65 缺节、去默认题材泄漏、列正反例与 capability、draft 不当 E4）；
- 03-RESEARCH-AGENDA.md §R2 / L145 / L149（参数+单位+真实范围、正例/强反例、适用/不适用、冲突链接；草案完成/来源支持/E4 实测分别记录）；
- 内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） → aivazovsky `card_has_81b=false`；AUDIT-aivazovsky/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
