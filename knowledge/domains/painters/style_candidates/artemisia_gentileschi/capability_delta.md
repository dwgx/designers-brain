<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-artemisia_gentileschi；原正文 SHA-256 `7e119a63ba84ce2112eac6ed863d2932f655aa4653d766dc604bc35a9d0a7d7b`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `artemisia_gentileschi` §8.1b（draft）

> 比较对象：现有卡 [artemisia_gentileschi.md](../../modules/artemisia_gentileschi.md)（`card_sha256=477149b4d510…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 阿尔泰米西娅·真蒂莱斯基 默认题材专名写死为题材**）、§8.2 逐帧规则、§4 六参数、冲突注记。

- **能做**：在「朱迪斯斩首荷罗孚尼 / 圣经女性复仇 / 17世纪意大利巴洛克」**默认题材域**内，用 §8.2 的 7 条逐帧自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-artemisia_gentileschi 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把「叙事光源×光斑-动作绑定×做功身体×定格×新鲜物证×复合情绪×贴平面暗部」迁到抽象海报、图标族、产品图时，§8.1 正向段会强制带回题材专名与体裁标签，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- **本卡特有的未消歧张力**：§8.2-1 L191「光源计数∈{0,≥1}」与 §3.1 L78 判据①「卡=0画外 / 阿=可出现且承担叙事」为「允许画内光」的两种口径；本段把「≥1必为叙事道具」写成显式取值，不擅自合并「计数范围」与「分工判据」。 无 §8.1b 时卡没有显式取值写法，跨场景路由易把两口径误当无条件阈值。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| 形式 / 语义拆分 | §8.1 绑定朱迪斯斩首荷罗孚尼 / 圣经女性复仇 / 17世纪意大利巴洛克 | 拆成 R1–R7 后区分：**形式可计算** R4、R7（面积 / 比例 / 方差 / 直方图 / 方向场，无语义输入仍可判定）；**需语义承载** R1、R2、R3、R5、R6（人物 / 面孔 / 文字 / 事件 / 器物 / 材质识别），无对应内容时标**不适用 / 未知**，不记通过 |
| 默认题材泄漏剥离表 | 无 | §1 表把题材专名、器物清单、体裁标签逐项降级；给迁移判据：撤专名后 §8.2 自查仍可算 = 纯风格 |
| 张力显式化 | 卡内两口径未处理 | §1 注把口径写成显式取值；旧「五条必要耦合」断言删除，改为有来源的 §4 联合身份判据 + 5 条 `[inference]` 组合假说 H-C1…H-C5（各带可推翻反证） |
| 正例 + 强反例 | 卡只有同域自查 | 跨场景正例 + 图标族正例；[counterexamples.md](counterexamples.md) 3 条 [inference]：机制撤去 / 关系反转 / 内容泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 6 类不适用 + vs 卡拉瓦乔（§3.1 L75–80：叙事光源/身体做功 vs 光开关/物理物证）、vs 米开朗基罗（L81：真实暴力 vs 理想化）、vs 伦勃朗（L82：事件心理 vs 肖像心理） 预检 |

**路由收益（一句话）**：从「认出朱迪斯斩首荷罗孚尼 / 圣经女性复仇 / 17世纪意大利巴洛克 → 套 §8.1 prompt」升级为「读出 R1–R7 关系 → 判断任意平面/版式场景是否满足 叙事光源×光斑-动作绑定×做功身体×定格×新鲜物证×复合情绪×贴平面暗部 的耦合」；跨场景判定**不再依赖题材专名**；但带语义前提的规则在无对应内容时必须标**不适用 / 未知**，不能被当作已通过。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[artemisia_gentileschi.md](../../modules/artemisia_gentileschi.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力，也不解决两口径张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案非实测结论**：正例与反例都只是 `[inference]` 纸面推演；关系是否被真实渲染器复现、有无预注册 E4，本 lane 一概未做（02-EXECUTION-PLAN Lane C）。阿尔泰米西娅·真蒂莱斯基 §4/§8.2 的阈值仍是 `[归纳]`、分母＝假想参考帧，不升格为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-artemisia_gentileschi]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-artemisia_gentileschi]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） artemisia_gentileschi `card_has_81b=false`；AUDIT-artemisia_gentileschi/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
