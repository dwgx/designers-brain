# S-04 盲测报告：Designers_Brain skill（RED-GREEN 对照）

- 日期：2026-10-15 ｜ 写手：主脑 ｜ 方法出处：`skill_ecosystem.md` §5.5（writing-skills RED-GREEN）
- 测试对象：`skills/designers-brain/`（v0.2 建包版，SKILL.md 106 行）
- 场景（两组同一需求）：「拾光」独立咖啡馆开业视觉——先出主视觉海报（后续可能做成 10 秒小动画发小红书）；预算一般；别太花哨；要有记忆点。
- 组设置：**RED** = 普通设计助手（禁读 skill；`tests/red_transcript.md`）；**GREEN** = 加载 skill（先读 SKILL.md 按协议行动；`tests/green_transcript.md`）。同 agent 类型（task），同日、同需求。
- 口径说明：真实触发 = 模型按 description 自主加载；本测试为「显式加载」近似。**机械激活另测**：junction ×4 全部解析到仓库（`build_receipt.md`）。

## 1. 结果对照

| 维度 | RED（无 skill） | GREEN（有 skill） |
|---|---|---|
| 第一动作 | 先抛 2 个具体方向 + 5 个自拟问题 | **首问包（3+2 填空式）**，未出稿 |
| 方向给不给 | 给得早（锚定风险；其自评承认「方向给得偏早」） | 留到风格环节（文字方向卡 → 看得见候选） |
| 提问结构 | 5 条自由问（无默认、无优先级） | 3+2 项 +「填多少算多少、默认说出口」 |
| 替换轴 | 无概念 | A/B/C/D 轴（猜 D 并留默认） |
| 冲突预检 / 选卡 | 无 | 承诺「推荐单 = 候选卡 + 冲突预检 + 形态 + 强度」 |
| 视觉决策门 | 无（纯文字沟通） | 两步法（文字卡 → 看得见对比图）+ 展示后停 |
| 出稿字段纪律 | 无 | 图像形态必带字段 + 留档契约（引至通道口径） |
| gate 文件 / 评审 | 无 | opt-out 路径含 design-brief 落盘 + 独立评审 |
| opt-out 处理 | — | 8 步（停问 → 假设一行 → 视觉门 → 预检 → 出稿字段 → gate → 评审 → 停轮） |

## 2. 判定

**PASS（行为增量成立）**。skill 把 RED 基线的三个行为差修掉：
① 「5 条自由问」→「5 项带默认填空」；② 「方向给太早」→「方向留到风格环节」；③ 「信息不全就抛方案」→「默认 + 假设 + 可否决」。
并新增 RED 完全没有的层：替换轴、冲突预检、视觉决策门、出稿字段、gate 文件、评审纪律。
GREEN 的引用核对逐字命中正本（见 `green_transcript.md` 附录 grep 原样输出）。

## 3. 遗留与裁定

- **候选数口径**（GREEN 留注：主规则 2–3 / huashu 三版 / 成本敏感可压缩）——**裁定**：默认 2–3 个看得见候选；成本敏感可压到 2；不得只出 1 个（用户明确要求单一方向除外）。已写回 `skill_spec.md` §2.5 与 `SKILL.md` 视觉专条。
- 首条回复偏长（术语偏专业）——观察项，留给下一版措辞压缩；不影响行为正确性。
- 强度定量承诺 [UNVERIFIED]（E3 未做）——按红线正确标注，不修。
- **自主触发实测（AutoTriggerProbe + 新鲜 omp 进程探针）**：本会话内 spawn 的 agent 继承「会话启动时」的旧技能目录（15 项，无 designers-brain）→ 未触发（与 catalog 枚举时机一致）。**新鲜 omp 进程**（cwd=仓库）实测：catalog 含 `designers-brain` → **新会话自主触发已就绪**。证据：`tests/autotrigger_probe.md` + `omp -p` 探针输出（17 项清单）。
- **未覆盖**：真实多轮走查 + 真出图 + gate 文件实跑（ConsultWalkthrough 演练中）→ S-05。

## 4. 文件

`tests/red_transcript.md`（4.7KB）｜`tests/green_transcript.md`（17.3KB）｜`build_receipt.md`（267 行）｜`skill_ecosystem.md` §5.5（方法出处）｜本报告 = S-04 验收件。
