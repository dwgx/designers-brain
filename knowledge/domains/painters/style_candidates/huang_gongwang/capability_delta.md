<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-huang_gongwang；原正文 SHA-256 `3acbb1a368a89f1f5a1ebf6c2cb35faccbd6942f0efa982b9aa72d191fd232c0`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `huang_gongwang` §8.1b（draft）

> 比较对象：现有卡 [huang_gongwang.md](../../modules/huang_gongwang.md)（`card_sha256=29e871000f17…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 黄公望 默认题材专名写死为题材**）、§8.2 逐帧规则、§4 六参数、冲突注记。

- **能做**：在「元文人山水 / 《富春山居图》/ 披麻皴长卷浅绛」**默认题材域**内，用 §8.2 的 7 条逐帧自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-huang_gongwang 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把「披麻皴成组长线 × 积墨3–5带 × 水面留白≥25% × 点苔簇 × 长卷疏密节奏 × 色域≤20% × 静场」迁到抽象海报、图标族、产品图时，§8.1 正向段会强制带回题材专名与体裁标签，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- **本卡特有的未消歧张力**：§8.2-3 L203「水面面积≥25%」与 §3.1 L69 判据③「留白40–60%且随空间均匀分布」为水面带/全幅留白两口径；本段把两者写成显式分工，不擅自合并分母。 无 §8.1b 时卡没有显式取值写法，跨场景路由易把两口径误当无条件阈值。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| 形式 / 语义拆分 | §8.1 绑定元文人山水 / 《富春山居图》/ 披麻皴长卷浅绛 | 拆成 R1–R7 后区分：**形式可计算** R1、R2、R3、R4、R6（面积 / 比例 / 方差 / 直方图 / 方向场，无语义输入仍可判定）；**需语义承载** R5、R7（人物 / 面孔 / 文字 / 事件 / 器物 / 材质识别），无对应内容时标**不适用 / 未知**，不记通过 |
| 默认题材泄漏剥离表 | 无 | §1 表把题材专名、器物清单、体裁标签逐项降级；给迁移判据：撤专名后 §8.2 自查仍可算 = 纯风格 |
| 张力显式化 | 卡内两口径未处理 | §1 注把口径写成显式取值；旧「五条必要耦合」断言删除，改为有来源的 §4 联合身份判据 + 5 条 `[inference]` 组合假说 H-C1…H-C5（各带可推翻反证） |
| 正例 + 强反例 | 卡只有同域自查 | 跨场景正例 + 图标族正例；[counterexamples.md](counterexamples.md) 3 条 [inference]：机制撤去 / 关系反转 / 内容泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 5 类不适用 + vs 八大山人（§3.1 L64–70：山水长卷/积 vs 花鸟单页/减）、vs 塞尚（L71：笔墨累积 vs 结构推导）、vs 北斋（L72：渗化提按 vs 等宽刻线）、vs 范宽（L73：淡墨长线 vs 密点雨点） 预检 |

**路由收益（一句话）**：从「认出元文人山水 / 《富春山居图》/ 披麻皴长卷浅绛 → 套 §8.1 prompt」升级为「读出 R1–R7 关系 → 判断任意平面/版式场景是否满足 披麻皴成组长线 × 积墨3–5带 × 水面留白≥25% × 点苔簇 × 长卷疏密节奏 × 色域≤20% × 静场 的耦合」；跨场景判定**不再依赖题材专名**；但带语义前提的规则在无对应内容时必须标**不适用 / 未知**，不能被当作已通过。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[huang_gongwang.md](../../modules/huang_gongwang.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力，也不解决两口径张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案非实测结论**：正例与反例都只是 `[inference]` 纸面推演；关系是否被真实渲染器复现、有无预注册 E4，本 lane 一概未做（02-EXECUTION-PLAN Lane C）。黄公望 §4/§8.2 的阈值仍是 `[归纳]`、分母＝假想参考帧，不升格为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-huang_gongwang]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-huang_gongwang]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） huang_gongwang `card_has_81b=false`；AUDIT-huang_gongwang/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
