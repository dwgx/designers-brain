<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-hiroshige；原正文 SHA-256 `14847440a6531318eadf4203d6a55e66075d574002b947d01c8a455d4d57e8d4`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `hiroshige` §8.1b（draft）

> 比较对象：现有卡 [hiroshige.md](../../modules/hiroshige.md)（`card_sha256=d2b2c4c257e6…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。

<a id="db-source-line-5"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（**正向段把 歌川广重 默认题材专名写死为题材**）、§8.2 逐帧规则、§4 六参数、冲突注记。

- **能做**：在「浮世绘风景版画 / 东海道五十三次 / 名所江户百景 / weather as lyric subject」**默认题材域**内，用 §8.2 的 8 条逐帧自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-hiroshige 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把「系列一致性 × 天气线族（雨线/留纸白）× bokashi 渐印 × 裁剪框景 × 旅人缩放 × 蓝系预算 × 竖幅叠层 × 静场」迁到抽象海报、图标族、产品图时，§8.1 正向段会强制带回题材专名与体裁标签，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。
- **本卡特有的未消歧张力**：§4 P6 强档「蓝≥40%」与北斋 C-12 主张「蓝≥40%」互斥（§4 越界蓝轴特别条款 L106）；本段把广重侧写成默认25–40%、组合时二选一，不擅自合并两卡蓝轴。 无 §8.1b 时卡没有显式取值写法，跨场景路由易把两口径误当无条件阈值。

<a id="db-source-line-13"></a>
## 2. §8.1b 草案新增的跨场景路由能力

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案 |
|---|---|---|
| 形式 / 语义拆分 | §8.1 绑定浮世绘风景版画 / 东海道五十三次 / 名所江户百景 / weather as lyric subject | 拆成 R1–R8 后区分：**形式可计算** R2、R3、R6、R7、R8（面积 / 比例 / 方差 / 直方图 / 方向场，无语义输入仍可判定）；**需语义承载** R1、R4、R5（人物 / 面孔 / 文字 / 事件 / 器物 / 材质识别），无对应内容时标**不适用 / 未知**，不记通过 |
| 默认题材泄漏剥离表 | 无 | §1 表把题材专名、器物清单、体裁标签逐项降级；给迁移判据：撤专名后 §8.2 自查仍可算 = 纯风格 |
| 张力显式化 | 卡内两口径未处理 | §1 注把口径写成显式取值；旧「五条必要耦合」断言删除，改为有来源的 §4 联合身份判据 + 5 条 `[inference]` 组合假说 H-C1…H-C5（各带可推翻反证） |
| 正例 + 强反例 | 卡只有同域自查 | 跨场景正例 + 图标族正例；[counterexamples.md](counterexamples.md) 3 条 [inference]：机制撤去 / 关系反转 / 内容泄漏反证 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 列 5 类不适用 + vs 北斋（§3.1 L79–84：地理-季节序列/抒情天气 vs 母题连作/动势事件）、vs 贝赫扎德（L85–89：版画序列 vs 手抄本单页）、vs 透纳（L90：可重访天气 vs 一次性事件） 预检 |

**路由收益（一句话）**：从「认出浮世绘风景版画 / 东海道五十三次 / 名所江户百景 / weather as lyric subject → 套 §8.1 prompt」升级为「读出 R1–R8 关系 → 判断任意平面/版式场景是否满足 系列一致性 × 天气线族（雨线/留纸白）× bokashi 渐印 × 裁剪框景 × 旅人缩放 × 蓝系预算 × 竖幅叠层 × 静场 的耦合」；跨场景判定**不再依赖题材专名**；但带语义前提的规则在无对应内容时必须标**不适用 / 未知**，不能被当作已通过。

<a id="db-source-line-25"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[hiroshige.md](../../modules/hiroshige.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力，也不解决两口径张力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案非实测结论**：正例与反例都只是 `[inference]` 纸面推演；关系是否被真实渲染器复现、有无预注册 E4，本 lane 一概未做（02-EXECUTION-PLAN Lane C）。歌川广重 §4/§8.2 的阈值仍是 `[归纳]`、分母＝假想参考帧，不升格为 validated。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-hiroshige]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-hiroshige]

<a id="db-source-line-32"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（11/76 存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） hiroshige `card_has_81b=false`；AUDIT-hiroshige/receipt.json（accepted）。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
