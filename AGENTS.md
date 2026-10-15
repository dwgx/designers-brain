# Designers_Brain — 入口

「艺术家视觉语言蒸馏系统」研究项目。Owner: dwgx1。**不建 git。** 纯研究，产物是模块与知识。

- 工作流 / 四车道 / LOOP 协议 → `docs/WORKFLOW.md`
- 项目宪章 / 来源原话 / 开放决策 → `docs/ARCHITECTURE.md`
- 当前任务队列（谁在写哪条路径）→ `ops/GOALS.md`
- 运维日志 / 通道状态 / 事故教训 / 授权记录 → `ops/OPS-LOG.md`（append-only；改动一律整份重写，不用 edit——其 §2.8）
- 跨家派发记账 → `board.py`（`C:/Users/dwgx1/.omp/extra-hands/CACHE/board.py`）：open 占写路径 → 派 → close --verdict ok --verify；对账 `board.py reconcile`
- 模板 → `templates/`（artist_module / style_card / determinism_contract / loop_goal）
- 素材索引（所有图片与来源）→ `knowledge/INDEX.md`
- 原始素材 `knowledge/domains/motion-graphics/origin/`（原 `owners research prompt/`，2026-10-15 迁移归档）**只读**，不许改。

## 硬规矩（本项目内）

- **一个路径一个写手**：动笔前先看 `ops/GOALS.md` 里该路径归谁；不写别人的文件。
- **证据分级**：每条结论标 `[自述]`（本人原话，带出处）/ `[史料]` / `[研究]` / `[归纳]`（我们总结的操作规则）/ `[推测]`。没出处的结论不落盘。
- **口径**：「创作原则」= 从作品、书信和艺术史资料归纳的操作规则，**不冒充**艺术家的真实内心。
- 查不到写「未找到（已查: …）」，不写「不存在」；数字带分母与日期。
- 没跑过 / 没核过的标 `[UNVERIFIED]`。
- 语言：正文中文，术语与引用保留原文；prompt 模板用英文。

## 当前波次（2026-10-15）

- **wave5 全收**：A-18 标注清扫（7/7）· B-08 迁移指南（457 行）· B-16 vsc 深拆（645 行）· B-17 端到端 #2（300 帧 / 15/15）——全部 done。
- **wave6**：B-18 模板 v0.3 已收；B-19（Blender 端到端 #3）· B-20（图像通道调研）running；跨家 C-01 running · C-02 reconcile open（DB-* 全 CLOSE）；产物未落盘前状态不许改 done。
- 待 Owner 决策：E 系列图像实验出图通道（`experiments/design.md` §3「生成模型+版本：待定」）。
