# 19 项当前交付独立审阅与绑定提案

## 裁决范围

这是 19 个历史 `materials_present_binding_pending` 任务的**当前内容映射与有限独立审阅**，不是把 19 个数字改成全项目通过。原 19 份 receipt 的 `accepted` 保留；新当前副本、补丁、运行与人的验收各自记状态。所有报告中的“当前”先指 2026-11-17T22:27:58Z 读取的 candidate e0 快照；最终接收必须在 Root 的独占 root-final 重新计算 SHA。此提案没有写远端、没有发布，也没有修改旧 staging/receipt/chain。

### 证据范围

- 13 个 STYLE 的三份实质正文（draft、counterexamples、capability_delta）全部阅读；2 个 LEARN 的四份正文全部阅读，共 47 份实质文档；15 份 source-claims 的字段、代表性条目及版本范围逐项核对。
- 原 19 份 receipt 的 107 个 artifact 条目均已从旧 campaign 只读取得元数据，107/107 的实际 SHA 等于 receipt 声明值。对 STYLE/LEARN 的旧实质 Markdown 另读取正文；其余旧操作性文件在本次仅核对存在/字节/hash，不能据此声称本轮又执行旧 runner。
- 13 个 STYLE direct contract 路径虽不存在，15 个 STYLE/LEARN 实际 accept-v2 bound snapshots 可以按 task_id 与 execution_dedup_key 追到；不是缺契约。另保留 direct contracts 与 retrospective-v2 的范围差异：核心 kinds 与当时操作性 evidence kinds 不混算。
- 15 个公共 source-claims 的 source_receipt_sha256 全部与本轮取得的对应原 receipt 匹配；它们保存源时点主张，不能因为 source_execution_status=accepted 推定公共投影、学习效果或 E4 已独立通过。
- 本报告作者 `/root/requirements_audit` 独立于这些历史正文作者。这里的 16 文件修复提案由本作者提出；其最终接收须由 Root 复核，不能把自写补丁称为已获第二人独立接受。

### 当前三种不同的工作

历史 result_summary、完整 claim map、runner 原件以 campaign-relative path+SHA 保留在私有审计链；当前知识正文只是 projection，UI 是 reimplementation。本文每个任务小节是**本轮新写的当前 result_summary**，不是旧 RESULT.md 的逐字复制。JSON 每个 kind 同时列历史原件与当前目标；找不到当前字节的项明确为空，不将父目录存在当交付。

## 本轮有界修复

16 个现有文件的 before/after 字节、SHA、精确替换和差异见 `PATCH-MANIFEST.json` 与 `current19-bounded-fixes.patch`。这些文件不改原研究 receipt 或原 bound contract。

| 问题 | 本轮修正 | 尚不能据此声称 |
|---|---|---|
| C02 用宽边换算短边 | 1920×1080 → 1080×1.5%=16.2；1080×0.6%=6.48；正文与自审同步 | 原作阈值已实测 |
| C04 方向 B 与旧双掩膜门相互冲突 | B 保持主模块全帧；方向 A 是另行预注册的历史方案；矩阵/注记/N3 列表同步 | E2d 已执行 |
| N1 存在量词与单卡豁免 | 四处统一“任何同适用域正向规则均不矛盾”；单卡基础检查，新增模块重算 | 所有组合视觉有效 |
| Hogarth 两面板套至少六帧 | 静态对位例明确关闭 R2；系列档必须另给 ≥6 帧/≥2 变化 | 只凭两面板通过系列规则 |
| Hopper 一光误判超三光 | 1≤3 通过；暗域/光池/照射面各自按明确条件判 | 单烛光必然不合格 |
| Korin 互斥色域总和 102% | 70%+18%+10%=98%，各阈值保持 | 实际像素图已存在 |
| Piero 等距例违反透视 | 改为单/双点透视例，排除平行等距作为 R2 正例 | 更改原 R2 或 E4 通过 |
| Goya 未脱离语义却称纯风格 | 明示 partial_semantic_transfer，保留未实现掩膜与状态映射 | 任意内容迁移已实现 |
| O’Keeffe 画外灯算画内光源 | 只在实际指定的投影/对比等超阈值时判失败 | 画外光必使画内灯数>0 |
| Durer 线距用角度单位 | 线距≤10%、方向≤10°，与机制原文一致 | 新增效果验证 |
| Sargent 53 条标签错汇总 | 重数 39 supported/9 partial/5 N/A；细分53与代表性10分开 | 改写旧 claim 等级或重开已收口 Zorn |

### N1 当前可复核的有限反例

同一物体同时存在正向“硬边宽度≤6 px”、正向“颜色为红”与反向“禁止任何硬边”。旧“与某条正向规则不矛盾”可由颜色规则满足，却漏过硬边冲突；新规则逐对检查会报告该冲突。若硬边禁令仅针对另一个显式掩膜，则该配对可判不适用，不能仅凭词面冲突。这是逻辑反例，不是新增像素实验；旧 RULE-01 CE1 的相反处置说法不借此复活。

## 逐任务当前审阅

### CONFLICT-02

**当前有限状态：`reviewed_rule_text_delivery`。**

C-02 双方比例规则的交集确实为空。现行正文误用宽边 1920；本轮在正文与自审算例同时更正为 1920×1080 的短边 1080，即≥16.2 px 与≤6.48 px，并把中间失败示例改为 10 px。

**保留边界：**规则逻辑与文本迁移可核验；不是原作阈值验证或 E2/E4 出图。旧 RESULT/claim map/delta/runner 均保留原 SHA，当前正文只是有限投影。

**效果/人评：**`E2_not_run_by_this_review`。

### CONFLICT-04

**当前有限状态：`reviewed_rule_text_delivery`。**

现行方向 B 为直方图轴单主、保留主模块全帧规则。当前仍把方向 A 双掩膜脚本列为 E2d 前置，矩阵也混写 masked-histogram；本轮两文同步为 B，N3 适用列表加 C04。40% 在三桶均摊只是可行构造，不是所有分布的单桶上界，现已明确。

**保留边界：**旧方向 A 方案仍可在新的独立预注册中研究，不能复活为 B 的门。没有运行 E2d、重建 histogram checker 或验证像素阈值。L*/归一化亮度单位仍须按各试验固定。

**效果/人评：**`E2d_planned_not_executed`。

### LEARN-durer

**当前有限状态：`reviewed_learning_draft_delivery`。**

四份实质正文完整阅读：6 步学习路径、7 决策 How to Think、M1–M8 排线与 G1–G5 几何机制、16 个细分 claim（15 supported/1 unverified）。来源分级、练习顺序与 C07 排线/平涂轴所有权均保留。本轮纠正练习自检把线距变化写为度数的单位错误；机制原文分别为线距≤10%、方向≤10°。

**保留边界：**这些是学习建议、可执行操作候选与历史来源映射，不证明学习收益。source-claims 只有 12 个代表性 claim，不等于逐条细分正文均被本轮回源验证。旧 locator 漂移属于源版本，尚不能自动变成当前文件事实。

**效果/人评：**`learning_outcomes_unverified; no_human_score`。

### LEARN-sargent

**当前有限状态：`reviewed_learning_draft_delivery`。**

四份实质正文完整阅读：8 节学习路径、3 组练习、8 步 How to Think、机制注及 53 细分 claim；材料区分 9 自写/13 转述/6 同时代/2 后人来源。当前已存在 F20-B 的 2026-11-16 Zorn 收口注，本轮不重开。53 条标签独立重数为 39/9/5，本轮修正误写 45/6/2，并将 53 与 receipt/public-source-claims 的 10 个代表性 claim 区分。

**保留边界：**历史 Zorn pending/图像大小/near-miss 计数不能当当前最新状态；当前收口注覆盖旧文本。未重访全部史料或补学习效果实测，不改任何细分 claim 标签，不回写旧 receipt。

**效果/人评：**`learning_outcomes_unverified; no_human_score`。

### RULE-01

**当前有限状态：`reviewed_rule_text_delivery`。**

N1 正本与三个消费副本完整核对：conflicts、style_card、modules/README、experiments/design。原“某条正向规则”是存在量词，不能保证与其他规则不冲突；本轮改为同一适用域内任何正向规则均不矛盾。单卡执行内部一致性；新增模块才触发重算。四处相同规范句，更新回链/历史状态。

**保留边界：**旧 RULE-01 accepted 是研究版接收，旧 needs_update 不是 overturned_candidate；此前 CE1 对相反处置的结论不成立。当前文本修补不验证全部组合效果。

**效果/人评：**`E2_not_run_by_this_review`。

### STYLE-chardin

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系覆盖材质/软反光/暖暗/浅空间/土色/静止与完成度；4 条反例与 source-claims 的 4 个代表性条目已读。

**保留边界：**未发现需本轮强制改写的算术错误。R6 要求至少两类材质；非静物应用仍须显式定义材质区域，不能把一形海报自动算成满足。C2 的因果耦合属假设。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-el_greco

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系与 4 条反例已读；P1 弱档、拉长比例、火焰边、酸性色、自发光、云空间及参数门有区分。

**保留边界：**非人物主题的上/下部包围盒及掩膜尚须定义；低档不应无条件套强拉长阈值。未进行新像素测量。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-goya

**当前有限状态：`reviewed_draft_delivery`。**

R1/R3 的阵营、R4 的生死状态、R5 的伤口/血迹和高光对象、R8 的怪诞分类仍然依赖语义；已将当前草案/能力说明修正为 partial_semantic_transfer。

**保留边界：**这是已交付的候选草案和可审的缺口，不是任意内容纯风格迁移实现。停机/运行状态没有被证明等价于生死状态；相关掩膜未实现。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-hogarth

**当前有限状态：`reviewed_draft_delivery`。**

8 条规则、4 条反例及 P1/P6 工作流开关已读。两面板例子原本违反 R2 至少 6 帧且两次状态变化；本轮明确静态对位不启用系列档。

**保留边界：**图标与人物面孔关键点的等价分类仍待定义。R7/R8 按印品/版画档触发；不把未启用规则算通过。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-hopper

**当前有限状态：`reviewed_draft_delivery`。**

R6 夜景最多 3 光源，单烛光 1≤3；原 C5/强反例 3 将数量误判失败。本轮拆成数量通过与具体光池/暗域条件分别判断。

**保留边界：**硬边、投影、正交、人数/静止/明度预算仍是纸面规则；没有测量实例。不能仅凭题材或一盏烛光判失败。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-ito_jakuchu

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系、4 条反例及 P3=0/100 网格开关已读；非网格正例明确关闭该档。模板复用、饱和/边缘差、暖白底与墨色预算区分。

**保留边界：**K/暖白等代理量和跨域对象分割未标定；未做颜色/像素测量。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-manet

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系、3 条反例已读；黑面积、双峰、平面空间、笔触/层数、人物正面与可选目光锚点有具体规则。

**保留边界：**非人物例子的面孔/目光锚点仍需明确适用域；纸面可计算不等于已实现通用语义掩膜。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-mir_sayyid_ali

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系、3 条反例已读；多主体、细节、棱角岩石、眼白、无收敛、尺度与平金约束有明确关系。

**保留边界：**R6/其他语义规则中的印度元素、人物计数、事件分类仍未由抽象异质标记等价实现。该稿仅有限迁移候选，不应升级为通用纯风格完成。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-munch

**当前有限状态：`reviewed_draft_delivery`。**

8 条关系、3 条反例已读；波线豁免、人物/面孔预算、对角线、地平线、静止与可选版画档有分层。

**保留边界：**非人物主题的面孔检测适用域及波线掩膜需要定义，阈值未经实测。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-ni_zan

**当前有限状态：`reviewed_draft_delivery`。**

真实是 7 条规则；3 条反例已读。三带、留白、单色、折线、树数、零人物与静止覆盖。

**保留边界：**将树改为垂直元素还未形成可验证的等价分类；最暗 10% 占比≤10% 近似同义约束，不应当成有效性证据。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-ogata_korin

**当前有限状态：`reviewed_draft_delivery`。**

10 条规则、3 条反例已读。金/蓝/绿色相区间互斥，原正例 72+18+12=102%；本轮改为 70+18+10=98%，各自阈值仍满足。

**保留边界：**修正纸面可行性，不声称已存在相应像素图。斑纹、区域、双幅关系仍需实际实现与测量。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-okeeffe

**当前有限状态：`reviewed_draft_delivery`。**

真实是 7 条规则；3 条反例已读。单主体、曲率/细节、渐变、平光、色域与尺度关系具备数值。画外光不增加画内光源计数，本轮纠正该反例。

**保留边界：**硬光只在投影/对比等明确超阈值时构成对应反例；系列规则按档位触发，不能据单幅写全 7 条实测通过。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### STYLE-piero_della_francesca

**当前有限状态：`reviewed_draft_delivery`。**

8 条规则、3 条反例已读。R2 要有限消失点及进深递减；原等距例名不相容。本轮改为透视信息图，并注明纯等距/正交不是 R2 正例。

**保留边界：**没有改变 R2 或重新做 E4；主轴、光影、空间、颜色耦合只是候选规则。

**效果/人评：**`E4_not_run; human_aesthetic_not_done`。

### UI-01

**当前有限状态：`reviewed_implementation_pending_final_rebind`。**

绑定根代理最终 Windows proposal 而非 Main e0 旧 checker。已读新的 UI 跨审原件：UTF8 修复后 UI01 119 assertions 与四种目标负例、UI02 63 assertions/20 resolver 控制/真实 CDP 组合输入、UI03 geometry/behavior/semantics 三层 gate。此项历史 required-kind 是 UI01；UI02/03 仅相关增量，不冒充 UI01 视觉证明。

**保留边界：**Root 后续独立 profile/严格负例诊断/UTF8 修复将改变 UI 源字节，须 final runtime rebind。旧 UI01 visual_evidence.png 属旧源码；本快照没有取得新 UI01 图片字节，需在 root-final 生成/绑定当次视觉证据。网络 SSE 重连、OS IME、完整无障碍、人类审美不在当前证明内。

**效果/人评：**`human_pending; final_UI01_visual_binding_pending`。

## UI 的最新版本边界

`analysis/evidence/UI-CROSS-REVIEW.md` 是另一位独立审阅者对原 Windows 修复的裁决，SHA `2909dc2e02f40a9c1157a34494013730db89578281aa9b565a02ca34210c8a0f`。本轮已读其审阅全文与原运行 JSON；没有把本人重新截图、浏览器交互或完整代码重审写成事实。

35 文件 UI proposal 的 SOURCE-MANIFEST 与 Windows 两个 UTF8 checker delta 是已读版本，后续 Root 独立 profile/严格负例错误/UTF8 修改要重新绑定。映射使用 `examples/ui/...` 路径，保留这个审阅基线 SHA 以识别 drift，不把它定为最终版本。最终运行记录必须绑定实际 fixture/checker/shared support 字节；旧首轮 cp1252 错误保留为失败，修复后成功另记。

UI01 的原 visual_evidence.png 仅证明历史旧实现截图存在。本次没有取得新实现 UI01 图片字节；UI03 320×200 变体图与 UI02 CDP 输入不能替代这个 kind。Root 若补当次 UI01 screenshot，绑定脚本可通过显式 `--ui-visual` 指定真实文件并记录 hash/bytes；它仍然不表示人类审美接收。

## 最终绑定与阻断

1. 先在独占 checkout 用 `apply_guarded.py --target <checkout>` dry-run，全部 source guards 一致后再 `--apply`。任何文件改变会零写拒绝；保留源快照、before/after SHA 与 diff。补丁只涉及列明的 16 文件。
2. 将本文作为当前新 summary 放入映射指定的 `docs/audit/current19/CURRENT-DELIVERY-REVIEW.md`。这是新审阅正文，不是旧任务 RESULT.md 的回写。旧完整 result_summary、claim maps、runner、receipt 继续由历史链承担。
3. 在最终 root-final 执行 `bind_current_delivery.py --target <checkout> --output <new mapping>`，如有当次 UI01 截图，显式提供 `--ui-visual <repo-relative path>`。脚本只读取候选并另写 mapping；逐文件重新计算 SHA/bytes，报告 missing/drift，绝不自动把 drift 变成通过。
4. 正文/补丁/读到的最终文件仍是 draft 或研究实现。Goya 等明确语义缺口、E4 未实测、真实 23 格人评、Owner 审美均保持原边界；本轮不代填评分，也不把这些需求变成无限新增研究门。

真正阻挡“当前绑定已闭合”的条件是：目标文件缺失、hash 与所审版本不一致且未核增量、required kind 无实际内容对应、旧回执冒充新运行、已知逻辑错未修复、UI01 新视觉证据未绑定。E4 与人评未完成则阻挡相应效果/审美宣称，不推翻已接受的历史研究版。

本报告不授权发布，也不将其他项目（BabelTower/ORIGIN）的工作写入 Designers_Brain 的交付范围。
