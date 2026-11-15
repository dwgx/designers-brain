<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-wu_guanzhong；原正文 SHA-256 `8e303c1bec061a0e0cc2299cd84e87f08b83572d2399589d17cf92244bfefc4d`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `wu_guanzhong` §8.1b（draft · ReviewGateStyleB5 语义修复）

> 比较对象：现有卡 [wu_guanzhong.md](../../modules/wu_guanzhong.md)（`card_sha256=16ba79884688…`，**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，本 lane 无 repo 写权，卡保持原样。
>
> 本版按 ReviewGateStyleB5 / S12 §A 校准（**§2 已收窄**）：不再宣称 R1, R2, R3, R4, R5, R6, R7, R8「全部是像素/几何统计量、不依赖器物」，也不把「拆开会破」当既成能力，也不宣称无语义几何图标逐条满足；带语义前提/动画的规则在无对应内容的输入上标不适用。

<a id="db-source-line-7"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

现有卡：视觉指纹要点、§8.1 图像 prompt（正向段把 吴冠中 默认题材专名写死为题材）、§8.2 逐帧规则（8 条）、§4 六参数、冲突注记。

- **能做**：在「吴冠中 默认题材域」内，用 §8.2 的 8 条（含带语义条件的规则）自查 `_extract.py --check` 所校验的 §8.1/§8.2/§4 逐字一致(AUDIT-wu_guanzhong 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把关系量迁到抽象海报、图标族、产品爆炸图时，§8.1 正向段会强制带回默认题材、器物与年代标签，把内容对象当风格前提 → 01-AUDIT.md A06 所指「有模块/能抽取/已做纯风格迁移」混淆。

<a id="db-source-line-14"></a>
## 2. §8.1b 草案新增的跨场景路由能力（已收窄）

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案（ReviewGateStyleB5） |
|---|---|---|
| 来源映射 | §8.1 绑定默认题材专名 | 保留 **R1, R2, R3, R4, R5, R6, R7, R8 8 条源规则原文**作为来源映射；R→P 映射按 §4 内容重算、行号已校准（§7），不再用索引恒等模板，无对应处明写「无直接对应」 |
| 可迁移形式子集 | 无区分 | 单列**可原样转移的形式子集 R1, R2, R3, R4, R5, R6**（面积/直方图/连通域/方向场等无语义统计量），这些在无器物/文字的几何输入上仍可判定 |
| 语义依赖显式化 | 无 | 单列 R7 **仍带语义前提**、R8 **动画/媒介规则**；无对应内容/静态输出时标**不适用/未知**，不记通过。撤回「全部是像素/几何/统计量、不依赖器物」的过强声明 |
| 组合条件 | 卡内规则并列 | 旧「五条必要耦合、拆开无法判定」删除；改为**有来源的联合身份判据**（§4 用法）与 **5 条 `[inference]` 组合假说 H-C1…H-C5**（各带可推翻反证），不写成必要性结论 |
| 正例 + 强反例 | 卡只有同域自查三问 | 一条**完整逐项可判定**的纸面正例（适用/不适用/未知逐条列，阈值按 §8.2 原文补全）；反例按「保持项—单项改变—具体 R-ID—跨越门槛」重建，内容泄漏反证单列 |
| 适用/不适用 | 散落在越界警报 | 适用/不适用逐条连到确切 R-ID；语义/动画规则在无承载输入标不适用 |

**路由收益（已收窄，一句话）**：从「认出 吴冠中 默认题材 → 套 §8.1 prompt」升级为「读出关系量 → 判断任意平面/版式场景**在哪些规则上适用、哪些不适用**」；跨场景判定不再依赖题材专名，**但带语义前提/动画的规则在无对应内容时必须标不适用，不能被当作已通过**。

<a id="db-source-line-27"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[wu_guanzhong.md](../../modules/wu_guanzhong.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。若草案未采纳或集成未发生，卡退回只有 §8.1/§8.2/§4：仍可在默认题材域内自查，但**不获得**跨场景路由能力。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案非实测结论**：正例与反例都只是 `[inference]` 纸面推演；吴冠中 §4/§8.2 的阈值仍是 `[归纳]`、分母＝假想参考帧，不升格为 validated（02-EXECUTION-PLAN Lane C）。H-C* 是项目工程假说 `[inference]`，未实测、未渲染、不等价于源规则。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「无语义几何图标逐条满足 8 条 R」= **否**（已按 ReviewGateStyleB5 撤回）；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-wu_guanzhong]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-wu_guanzhong]

<a id="db-source-line-34"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3（存在性检查非 E4）；02-EXECUTION-PLAN.md Lane C；03-RESEARCH-AGENDA.md；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） wu_guanzhong `card_has_81b=false`；AUDIT-wu_guanzhong/receipt.json（accepted）；S12 §A（内部证据 52a2efbc3f2fabad（未公开；来源记录由维护者保留） §A）；ReviewGateStyleB5 `worklist.json` / `trunc-v3.json`。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
