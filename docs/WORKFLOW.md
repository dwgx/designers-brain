# WORKFLOW — 四车道 + LOOP 协议

> 入口 `AGENTS.md` · 宪章 `docs/ARCHITECTURE.md` · 队列 `ops/GOALS.md` · 模板 `templates/`。
> 本文件 = 项目操作手册。改它 = 改工作流，先跟主脑说。

## 1. 角色

- **主脑（omp 主会话）**：定方向、切切片、派发、验收（核产物 + 跑完成条件）、汇总、维护 `ops/GOALS.md` / 本文件 / `docs/ARCHITECTURE.md`。
- **研究工人（in-session subagents，`task` 工具；并发不限制——`config.yml` `task.maxConcurrency: 0`，2026-10-15 Owner 令）**：按 brief 的**独占路径**落盘；有名字（IRC 地址 `agent://<Name>`）；可互相 `write agent://<Name>` 交叉核对；**默认不再生小代理**（`maxRecursionDepth: 2` 允许再开一层只读 child——brief 没写就不开）。
- **跨家工人（`dispatch.ps1`：claude / codex / omp；grok 仅 Owner 点名）**：大块、长时、跨进程。先 `board.py open` 占写路径 → brief 过 `briefcheck` → 派 → 读 `last.md` + 核产物 → `board.py close --verify`。

## 2. 四车道

| 车道 | 内容 | 现状 |
|---|---|---|
| **A 画家蒸馏** | 8 位核心画家（达芬奇/米开朗基罗/梵高/莫奈/毕加索 + 塞尚/马蒂斯/北斋）档案 + 扩展候选 + 原话语料 | wave1 进行中 |
| **B Agent 代码艺术** | 15 卡结构蒸馏；HTML/WebGL 逐帧渲染；Blender；prompt 语料猎场；GitHub 系统猎场；Opus 5.5 证据链 | wave1 进行中 |
| **C 跨家派发** | 把大块研究切片派给 claude/codex/omp，board 记账、回执对账 | 通道已建，3 个工人在飞 |
| **D 联网/浏览器/子代理** | `web_search` + `read`(URL) + eval `browser` + chrome-devtools MCP + 子代理扇出 | 通道已建 |

## 3. LOOP 协议（每条研究线都这么转）

1. 从 `ops/GOALS.md` 取一条 `open`（必须已有：产出路径 + 完成条件）。
2. 深研究：工具不限；**发现新线头 → 立即在 `ops/GOALS.md` 追加子条目**（新 ID + 产出路径），不许丢。
3. 产物落盘：写进条目指定路径；每条结论带出处；证据分级 `[自述]/[史料]/[研究]/[归纳]/[推测]`。
4. 自审四段：**A 早产出**（先落盘再继续）→ **B 反驳**（挑 3–5 条最强结论逐条试推翻，标 `CONFIRMED/WEAKENED/OVERTURNED` + 跑过的命令；被推翻的从产物里删）→ **C 机械验证**（指名一个检查器，原样粘输出）→ **D ≤14 行小结**（已确立/被推翻/未知/下一步）。
5. 主脑验收：读产物、跑完成条件；**实现者不验收自己的活**，关键产物换人复核。
6. 更新 `ops/GOALS.md`（done + 新条目）→ 向 Owner 报一句（结论先行）。

## 4. 写路径纪律

- 一个路径一个写手；撞车由主脑重切切片，不许绕。
- 文件名即归属：`knowledge/domains/painters/dossiers/<id>.md` 归该画家的工人；`knowledge/agent-art/<topic>/` 归该 topic 的工人。
- 原始素材（`knowledge/domains/motion-graphics/origin/`）只读。

## 5. 证据标准

- 每条关键结论 = `path + key` 或 URL；原话必须可查（书信/访谈/馆方页面）。
- 数字带分母与日期；「查不到」≠「不存在」。
- 项目口径：「创作原则」是**归纳的操作规则**，不冒充艺术家内心；有资料支持的与 AI 归纳的分开标。

## 6. 工具地图

| 工具 | 用途 |
|---|---|
| `web_search` / `read`(URL) | 常规检索与静态抓取 |
| eval `browser` / chrome-devtools MCP | JS 重页面、交互、截图、浏览器抓取 |
| `task` 子代理 | 同进程研究扇出（**并发不限制**，`maxConcurrency: 0`；有名字，IRC） |
| `dispatch.ps1` | 跨家派发（claude/codex/omp），board + briefcheck 门 |
| `sessq` / `archive` | 查历史会话与旧测量 |
| `board.py` | 派发记账（open/close/reconcile） |

## 7. 汇报形状（对 Owner）

第一行是结论或下一步；编号多步；一组最多 5 条；不写开场白与客套；时间给具体量。
