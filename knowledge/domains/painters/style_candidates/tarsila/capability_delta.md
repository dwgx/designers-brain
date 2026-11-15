<a id="db-source-line-1"></a>

> 公共知识投影；源任务 STYLE-tarsila；原正文 SHA-256 `8be08dc6d61282f28fc1c1ae64fccec6927bb39e1de2436b51c7822d07023626`。原证据等级、建议练习/草案与未验证限制保持；执行接受不等于效果验证。
# 能力增量 — `tarsila` §8.1b（draft · ReviewGateStyleB5 语义修复）

> 比较对象：现有卡 [tarsila.md](../../modules/tarsila.md)（**无 §8.1b**，`card_has_81b=false`）vs 本 [style_only_draft.md](style_only_draft.md)（候选）。repo READ-ONLY，卡保持原样。

> 本版按 ReviewGateStyleB5 / S12 §A 校准：不再宣称 7 条规则「全部是像素/几何统计量、不依赖器物」，也不把「拆开会破」当既成能力；带语义前提的规则在无对应内容的输入上标不适用。

<a id="db-source-line-7"></a>
## 1. 无 §8.1b 时，卡能做什么 / 不能做什么

- **能做**：在「塔西拉 默认题材域」内，用 §8.2 的 7 条（含带语义条件的规则）自查逐字一致(AUDIT-tarsila 记录 §8.1b 被排除在逐字比对之外)。
- **不能做**：**跨场景路由**。把关系量迁到抽象海报、图标族时，§8.1 正向段会强制带回默认题材，把内容对象当风格前提。

<a id="db-source-line-12"></a>
## 2. §8.1b 草案新增的跨场景路由能力（已收窄）

| 增量 | 无 §8.1b 的卡 | 本 §8.1b 草案（ReviewGateStyleB5） |
|---|---|---|
| 来源映射 | §8.1 绑定默认题材专名 | 保留 **R1–R7 八条源规则原文**；R→P 按 dossier §4 内容重算（§4 用法 L101：R3 几何化简→P2 几何化简度（非 P3 前缩夸张）；R4 平涂→P5 平面层次（非 P4 梦境性）），无对应明写「无直接对应」 |
| 可迁移形式子集 | 无区分 | 单列**可原样转移的形式子集 R1, R2, R3, R4, R5, R6**，在无语义几何输入上仍可判定 |
| 语义依赖显式化 | 无 | 单列 R7(梦境-夸张) **仍带语义前提**；无对应内容时标**不适用/未知**，不记通过 |
| 组合条件 | 卡内规则并列 | 旧「五条必要耦合、拆开无法判定」删除；改为**有来源的联合身份判据**(§4 用法) 与 **5 条 `[inference]` 组合假说 H-C1…H-C5**（各带反证） |
| 正例 + 强反例 | 卡只有同域自查三问 | 逐项可判定纸面正例（适用/不适用/未知）；反例按「保持项—单项改变—具体 R-ID—跨越门槛」重建，内容泄漏反证单列 |
| 截断阈值 | 旧正例引用在数值/词中途截断 | 按 §8.2 原文补全全句阈值；dossier 无值处标 未实测/unknown，不补数 |
| 适用/不适用 + 组合预检 | 散落在越界警报 | 逐条连到确切 R-ID；恢复 §4 用法完整来源文字 |

**路由收益（已收窄）**：从「认出 塔西拉 默认题材 → 套 §8.1 prompt」升级为「读出关系量 → 判断任意平面/版式场景**在哪些规则上适用、哪些不适用**」；带语义前提的规则在无对应内容时必须标不适用，不能被当作已通过。

<a id="db-source-line-26"></a>
## 3. 回退与状态（关键，不得夸大）

- **回退契约**：staging-only 草案；[tarsila.md](../../modules/tarsila.md) 在集成写者写入 §8.1b 之前**保持无 §8.1b**(`card_has_81b=false`)。不得把「草案已写」记成「卡已具备 §8.1b」。
- **草案非实测结论**：正例与反例都只是 `[inference]` 纸面推演；阈值仍是 `[归纳]`、分母＝假想参考帧，不升格为 validated。H-C* 与 R→P 对读是项目工程假说/内容校准，未实测、未渲染。
- **能力矩阵口径**：「§8.1b 候选草案存在 + 跨场景路由判定规则已写」= 是；「可迁移已实测通过」= 否；「无语义几何图标逐条满足 7 条 R」= **否**（已撤回）；「card 含 §8.1b」= 否；「E4 passed」= 否。 [STYLE-tarsila]
- **独立审阅**：`receipt.json` status=`submitted`、`review: null`、`human_review.status: not_applicable`；作者不自接受。 [STYLE-tarsila]

<a id="db-source-line-33"></a>
## 4. 依据

01-AUDIT.md A06 / §6.3；02-EXECUTION-PLAN.md Lane C；内部证据 32f9d1d499ba4c9e（未公开；来源记录由维护者保留） tarsila `card_has_81b=false`；AUDIT-tarsila/receipt.json（accepted）；内部证据 52a2efbc3f2fabad（未公开；来源记录由维护者保留） §A；REVIEW-GATES/STYLEB5/worklist.json + review-evidence-styleb5.md。

## 同一条目的附页

- [style_only_draft.md](style_only_draft.md)
- [counterexamples.md](counterexamples.md)
- [source-claims.json](source-claims.json)
