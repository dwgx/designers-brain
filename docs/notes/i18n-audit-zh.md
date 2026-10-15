# i18n 审计 · zh-CN ↔ EN（5 对文件）

> **For:** Designers_Brain · R-03（i18n zh-CN 质量审计），2026-10-15。
> **范围（5 对 / 10 文件）：** `README.md` ↔ `README.zh-CN.md`；`docs/{ARCHITECTURE,WORKFLOW,PROTOCOLS,ROADMAP}.md` ↔ `docs/i18n/zh-CN/{ARCHITECTURE,WORKFLOW,PROTOCOLS,ROADMAP}.md`。
> **方法：** 全文逐对对读；逐句抽查 15 处（每文件 3 处）；代码块字节比对；内联代码 / 链接 / 标识符 / 证据分级标签 / 数值集合的逐对集合比对；17 项术语 grep 核对；与仓库内部用语（`ops/OPS-LOG.md`、`ops/session-digest.md`、`ops/GOALS.md`）交叉验证。ja 版仅作个别用词对照，不在审计范围。
> **基线：** 5 份 zh 文件均为工作区新增（未提交），翻译头注「Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)」格式统一 ✓。
> **证据等级：** `[研究]`（直接比对）+ `[归纳]`（建议）。
> **声明：** 只读审计；未改动任何被审文件；本报告为唯一新增文件。

## 0. 结论摘要

**PASS-with-notes。**

- 逐句抽查 15 处：**义 / 强调 / 限制条件均无实质漂移**（3 处备注，均为编辑级）。
- 术语核对 17 项：**全部一致**；`skill` 首现注 5/5 齐备，`junction` 首现注 2/2 齐备（其余文件无散文出现）。
- 零翻译零改动核对 14 项：**全部通过**（含 5 处代码块字节级完全一致）。
- 问题清单：3 项（用词混用 ×1、括号嵌套 ×1、可读性 ×1），均为次要/轻微，不阻塞发布。

## 1. 逐句抽查记录（15 处，每文件 3 处）

> 判定口径：**义**（语义）、**强调**（粗斜体/加重）、**限制条件**（数量、范围、only/never/≤ 等）、**文风**（中文技术写作自然度）。

| # | 位置（zh ↔ EN 行号） | EN 摘句 | ZH 摘句 | 维度 | 判定 |
|---|---|---|---|---|---|
| 1 | README.zh L8 ↔ README L3 | "Deep-research distillation … **asks before it designs**" | 「经深度研究蒸馏…**先问再设计**」 | 义 / 强调 | 一致；用词混用见 Q-1 |
| 2 | README.zh L15 ↔ README L12 | "checks conflicts before combining" | 「组合前先查冲突」 | 义 | 一致 |
| 3 | README.zh L82 ↔ README L79 | "first two domains distilled… three pipelines verified end-to-end" | 「前两个领域已蒸馏…三条管线端到端验证通过」 | 限制条件 | 一致 |
| 4 | ARCH.zh L12 ↔ ARCH L7 | "Most "style prompts" are vibes." | 「大多数「风格提示词」都只是感觉。」 | 文风 | 一致（口语化处理可接受） |
| 5 | ARCH.zh L65 ↔ ARCH L60 | "only if it ships all of" | 「只有同时具备以下全部内容，才能处于 `active`」 | 限制条件 | 一致 |
| 6 | ARCH.zh L86 ↔ ARCH L81 | "≤3 conversation rounds… stop after showing… gate file" | 「对话不超过 3 轮…展示后即停…gate 文件」 | 限制 / 义 | 一致（「≤3」表述差异见 R-2） |
| 7 | WORKFLOW.zh L13 ↔ WORKFLOW L8 | "accepts results (reads artifacts + runs acceptance)" | 「验收（读产物 + 跑验收条件）」 | 义 | 一致 |
| 8 | WORKFLOW.zh L33 ↔ WORKFLOW L28 | "tag `CONFIRMED/WEAKENED/OVERTURNED` + the command run" | 「打 `CONFIRMED/WEAKENED/OVERTURNED` 标签 + 所运行的命令」 | 义 / 零翻译 | 一致 |
| 9 | WORKFLOW.zh L56 ↔ WORKFLOW L51 | "with board + briefcheck gates" | 「带板 + briefcheck 两道关卡」 | 文风 | 轻微 → Q-3 |
| 10 | PROTOCOLS.zh L8 ↔ PROTOCOLS L3 | "Where a rule says *must*" | 「凡标注 *must*（必须）之处」 | 强调 | 一致（「（必须）」为有意注释） |
| 11 | PROTOCOLS.zh L45 ↔ PROTOCOLS L40 | "**removed entirely**, never downgraded" | 「**整行移除**，绝不降级」 | 强调 / 限制 | 一致 |
| 12 | PROTOCOLS.zh L52 ↔ PROTOCOLS L47 | "**no negative-prompt parameter**" | 「**没有负向提示参数**」 | 义 | 一致 |
| 13 | ROADMAP.zh L13 ↔ ROADMAP L8 | "style-separation 7/7 resolved" | 「风格分离 7/7 解除」 | 义 | 一致（沿用内部用语，见 R-1） |
| 14 | ROADMAP.zh L12 ↔ ROADMAP L7 | "activated (junctions + packaging)" | 「已激活（junction（目录联接）+ 打包件）」 | 排版 | 轻微 → Q-2 |
| 15 | ROADMAP.zh L47 ↔ ROADMAP L42 | "honest ceiling: P1, ≤0.05% pixels" | 「诚实上限：P1，≤0.05% 像素差」 | 义 / 限制 | 一致 |

**全量结构比对（辅助证据）：** 标题数逐对相等（15、13、8、12、7）；粗体跨度逐对相等（13/13、23/23、18/18、22/22、8/8）；斜体跨度逐对相等（1/1、5/5、0/0、5/5、0/0）；列表项/表格行数逐对相等（13/13、31/31、9/9、34/34、24/24；表行 16/16）。强调层级无丢失、无新增。

## 2. 术语核对表（17 项）

| 术语（zh） | EN 对应 | 出现（代表位置，zh 文件） | 判定 |
|---|---|---|---|
| 档案 | dossier(s) | README L19；ARCH L58；WORKFLOW L21；PROTOCOLS L30；ROADMAP L10 | 一致 ※ |
| 模块 | module(s) | README L8；ARCH L14/L59；WORKFLOW L21；PROTOCOLS L45；ROADMAP L28 | 一致 |
| 模块卡 | module card(s) | README L20；ARCH L59；WORKFLOW L21；ROADMAP L10 | 一致 |
| 风格卡 | style card(s) | README L20；ARCH L75；PROTOCOLS L41；ROADMAP L11 | 一致 |
| 车道 | lane(s) | WORKFLOW L1/L17/L19/L26 | 一致 |
| LOOP 协议 | the LOOP protocol | ARCH L104；WORKFLOW L1/L28 | 一致 |
| 主脑 | main brain | ARCH L104；WORKFLOW L9/L13/L34/L39；PROTOCOLS L12 | 一致 |
| 工人 | worker(s) | WORKFLOW L14/L15/L23/L40 | 一致 |
| gate 文件 | gate file | ARCH L86；PROTOCOLS L59；ROADMAP L12 | 一致（gate 保留英文） |
| junction（首现注） | junction | ARCH L84；ROADMAP L12 | 一致：均注「（目录联接）」；README 仅出现在代码块（保持原文，零改动正确） |
| skill（首现注） | skill | README L8；ARCH L8；WORKFLOW L25；PROTOCOLS L16；ROADMAP L12 | 一致：5/5 首现均注「（技能包）」 |
| 管线 | pipeline(s) | README L23/L82；ARCH L96/L117；WORKFLOW L22；ROADMAP L11/L13/L39 | 一致 |
| 验证器 | verifier | ARCH L92/L117；PROTOCOLS L37 | 一致 |
| 验收 | acceptance | ARCH L92/L102/L104；WORKFLOW L13/L30/L34；PROTOCOLS L37/L45 | 一致 |
| 冲突轴 | conflict axis/axes | ARCH L95；PROTOCOLS L45 | 一致 |
| 证据分级 | evidence grade(s) | README L57；ARCH L15/L77/L104/L124；WORKFLOW L32；PROTOCOLS L13/L71；ROADMAP L38 | 一致 |
| 注册契约 | registry contract | ARCH L63/L115；PROTOCOLS L33；ROADMAP L27 | 一致 |

※ 仅记录：PROTOCOLS §3 中 EN「archives」亦译「档案」（与「dossiers」同形）；语境可区分，可不改。

**延伸抽查（非清单项）：** 首问包 / 任务书（brief）/ 确定性契约 / 乱序重渲 / 派发板 / 走查 / 盲测 / 落盘 / 收口 / 解除 / 建包 / 一笔画卡 —— 均一致，且与 ops 内部用语吻合（见 R-1）。

## 3. 零翻译零改动核对（14 项）

| # | 核对项 | 方法 | 结果 |
|---|---|---|---|
| 1 | README 代码块①（junction 激活命令） | 字节比对 | 完全一致（211 B） |
| 2 | README 代码块②（实验复现命令） | 字节比对 | 完全一致（210 B） |
| 3 | README 代码块③（仓库地图） | 字节比对 | 完全一致（448 B） |
| 4 | ARCHITECTURE 代码块①（仓库布局树） | 字节比对 | 完全一致（1819 B） |
| 5 | ARCHITECTURE 代码块②（知识分层图） | 字节比对 | 完全一致（243 B） |
| 6 | 内联代码 span 集合（全 5 对） | 集合比对 | 逐对完全一致（19 / 52 / 30 / 37 / 11 项） |
| 7 | 标识符：N1–N9、C-01–C-18、C1–C10、P1 | 计数比对 | 逐文件相等（N1–N9：1/1、1/1、2/2；C-01–C-18：1/1、1/1、2/2；C1–C10：1/1、1/1；P1：1/1、1/1、2/2） |
| 8 | 证据分级标签 `[自述][史料][研究][归纳][推测]` | 计数比对 | 逐文件相等（README 1×5、ARCH 2×5、WORKFLOW 1×5、PROTOCOLS 1×5） |
| 9 | `[UNVERIFIED]` | 计数比对 | ARCH 3/3、PROTOCOLS 1/1、ROADMAP 2/2 |
| 10 | 链接 | 集合比对 | README 12/12（仅语言切换行按惯例互换）；四篇 docs 仅新增切换行且目标存在（`../../X.md`、`../ja/X.md`）；正文引用产物路径全部存在 |
| 11 | 命令串：`_extract.py --check`、`_verify_e2.py`、`board.py open`/`close --verify`、`dispatch.ps1`、`briefcheck`、`last.md`、`agent://<Name>` | 逐字比对 | 一致 |
| 12 | 模型/尺寸串：`grok-imagine-image-2.0`、`buddyfarm/`、`1024×1536`、`768×1152` | 逐字比对 | 一致 |
| 13 | 实验/产物标识：`E1_t1*`、`E1_t1b/c`、`E2_t1`、`anim_test_01/02/03`、`mg-styles-15`、`designers-brain` v0.2 | 逐字比对 | 一致 |
| 14 | 数值集合（7/7、9/9、33/33、126、33、≤0.05%、30 / 50 / 75 / 100% 等） | 集合比对 | 一致；差异仅为头注行新增（2026 / 10 / 15 / 534924）与「batch 2 → 第二批」 |

## 4. 问题清单

| ID | 严重度 | 位置 | 证据 | 建议修法 |
|---|---|---|---|---|
| Q-1 | 次要（一致性） | README.zh-CN.md L8、L57；ARCHITECTURE.md L19、L104；WORKFLOW.md L31 | 「deep research」译法混用：README L8「深度研究」×1，其余 4 处「深研究」；EN 五处均为 deep research | 二选一统一：推荐「深度研究」（更规范；ja 版五处均取自然表达且一致）＝改 4 处；若沿用 ops 用语则统一「深研究」＝改 1 处 |
| Q-2 | 次要（排版） | ROADMAP.md L12 | 「已激活（junction（目录联接）+ 打包件）」括号嵌套 | 改「已激活（junction 目录联接 + 打包件）」或拆句 |
| Q-3 | 轻微（可读性） | WORKFLOW.md L56 | 「带板 + briefcheck 两道关卡」中「带板」略生造（「板」在本文档为孤例） | 改「带派发板 + briefcheck 两道关卡」（与「机器级派发板 / 派发板」对齐） |

**附加备注（不构成问题，供知悉）**

- R-1：「7/7 解除」「收口」「建包」「一笔画卡」等表述与仓库内部用语（OPS-LOG / GOALS）一致，属有意沿用，保留即可。
- R-2：「≤3」在 ARCHITECTURE 作「不超过 3 轮」、PROTOCOLS 作「≤3 轮」——语义等价；如求形式统一可选改（低优先）。

## 5. 结论

**PASS-with-notes。** 对照审计通过：5 对文件在语义、强调、限制条件上无实质漂移；17 项术语一致、`skill`/`junction` 首现注齐备；零翻译零改动（含 5 处代码块字节比对、内联代码/链接/标识符/证据标签全量核对）全部通过。3 项次要/轻微备注（Q-1～Q-3）为编辑级优化，不阻塞发布；建议在下次译稿维护时一并处理。

> 审计未改动任何被审文件；本报告为 `docs/notes/` 下唯一新增文件。
