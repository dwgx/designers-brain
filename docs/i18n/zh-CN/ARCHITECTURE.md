# 架构

> 本文件为翻译版；以英文正本为准（可能滞后于最新改动）。
Translation baseline: README/docs as of 2026-10-15 (commit 534924e+)

[English](../../ARCHITECTURE.md) · 中文 · [日本語](../ja/ARCHITECTURE.md)

> Designers_Brain 把艺术家与设计师的创作语言蒸馏为可组合、可验证、AI agent 可执行的模块——并打包成一个任何 agent 都能加载的 skill（技能包）。把仓库交给 agent：它先问，再做设计与替换，全程带证据。

## 1. 理念

大多数「风格提示词」都只是感觉。本项目把它们变成**工程产物**：

- **蒸馏**——对每个领域（先从画家开始），我们阅读一手来源（作品、书信、论著、学术研究），提取视觉语言背后的*操作规则*，压缩成可组合、可调节、可验证的**模块**。
- **证据分级**——每条论断都带标签：`[自述]`（本人自述 / 一手引文）、`[史料]`（历史记录）、`[研究]`（研究文献）、`[归纳]`（我们的归纳）、`[推测]`（推测）。分级随论断一起进入所有下游产物。
- **实验**——每个模块都端到端跑过（图像生成、网页动画、Blender 场景）并配机械检查；没有支撑的论断保持 `[UNVERIFIED]` 标记。
- **skill**——蒸馏出的知识打包成一个 agent skill（`skills/designers-brain/`），把任何有能力的 agent 变成设计顾问：先问对问题，推荐模块时附带冲突预检，产出三种形态之一（图像提示词 / 10 秒网页动画 / Blender 任务书）。

项目的名字就是它的野心：一个*为设计师而生的大脑*——逐领域深度研究，向外扩展。

## 2. 仓库布局

```
designers-brain/
├── README.md · README.zh-CN.md · README.ja.md   — public face (EN primary + translations)
├── LICENSE · LICENSE-CODE · NOTICE.md            — CC BY 4.0 (content) + MIT (code) + third-party notices
├── AGENTS.md · CLAUDE.md                         — entry points for AI agents
├── CONTRIBUTING.md                               — how to contribute (domains, cards, fixes)
├── docs/
│   ├── ARCHITECTURE.md · WORKFLOW.md · PROTOCOLS.md · ROADMAP.md
│   ├── MIGRATION.md                              — layout history (old → new paths)
│   ├── skill/                                    — skill design research: ecosystem study, spec, tests, walkthrough
│   └── i18n/zh-CN/ · i18n/ja/                    — translations of the four docs above
├── knowledge/                                    — the distilled product
│   ├── INDEX.md                                  — full source/image index
│   ├── domains/
│   │   ├── painters/       (dossiers/ + modules/) — domain #1: 11 painters
│   │   └── motion-graphics/ (cards/ + origin/ + sources/) — domain #2: 15 MG style cards
│   ├── cross/                                    — cross-domain rules: conflicts, transfer guide, review rubric, image channel
│   └── agent-art/                                — how agents make art with code: HTML/Blender pipelines, prompt corpus, evidence
├── skills/designers-brain/                       — the consumable skill (SKILL.md + references/ + domains.yaml)
├── experiments/                                  — evidence runs (E-series + animation tests), scripts included
├── templates/                                    — reusable templates (module, style card, determinism contract, design brief)
└── ops/                                          — AI-ops state: GOALS.md (work queue) · OPS-LOG.md (append-only log)
```

## 3. 知识模型

### 3.1 分层

```
sources ──▶ dossiers ──▶ modules / cards ──▶ skill (pointers only)
(quotes,     (full evidence    (operational,      (routing + protocols,
 images,      per artist,       composable)        never copies content)
 literature)  ~300 lines each)
```

- **档案**（`knowledge/domains/painters/dossiers/`）——每位艺术家的证据文件：视觉指纹、技法规则、工作原则、控制参数、带出处的引文、图像清单。11 位画家，每份约 250–380 行。
- **模块**（`.../modules/`）——每位艺术家的*模块卡*：图像提示词片段（§8.1 / §8.1b 纯风格段）、代码艺术规则（§8.2）、控制参数（§4）、冲突注记。模块卡由档案机械抽取（`_extract.py`，33 项逐字校验）。
- **跨域规则**（`knowledge/cross/`）——模块间冲突（C-01–C-18）、组合规则（N1–N9）、模型迁移指南、评审标准、图像通道文档。
- **skill**（`skills/designers-brain/`）——以指针方式路由到上述内容；不含重复内容，因此知识更新无需改动 skill。

### 3.2 领域与注册契约

领域注册在 `skills/designers-brain/domains.yaml`。一个领域只有同时具备以下全部内容，才能处于 `active`：

1. 卡片目录（一卡一文件，索引一致）；
2. 索引（能力地图 + 组合说明）；
3. 冲突清单（或显式复用通用规则 + 领域增量）；
4. 输出形态映射（图像提示词 / 网页动画 / Blender——支持哪些，以及字段差异）；
5. 强度机制（或显式的缺口标注）；
6. 证据（实验）或 `[UNVERIFIED]` 状态；
7. 注册项 + 自检覆盖。

已激活领域：`painter`（11 个模块）、`mg-motion`（15 张风格卡）。新领域（摄影、字体排印……）满足同一契约即可接入。

### 3.3 证据分级

`[自述]` 本人自述（必须带出处）· `[史料]` 历史记录 · `[研究]` 研究文献 · `[归纳]` 我们的归纳 · `[推测]` 推测。未验证的能力一律标 `[UNVERIFIED]`，绝不承诺为已交付。

## 4. skill

- **入口**：`skills/designers-brain/SKILL.md`（渐进披露：目录 → 正文 → 参考文件）。
- **激活（本地）**：以 junction（目录联接）接入 harness 的扫描路径（`~/.agents/skills`、`~/.claude/skills`、`~/.codex/skills`）；仓库内会话用项目级 `.agents/skills/`。
- **分发**：插件清单（`.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`、`.agents/plugins/marketplace.json`）。
- **交互协议**（全文在 skill 中）：第一个动作是**首问包**（业务 / 受众 / 素材 / 风格意图 / 替换轴——3+2 填空，默认项明确说出）；对话不超过 3 轮；视觉决策必须有*可见*候选，展示后即停；`design-brief.md` gate 文件记录意图、假设与批准范围。
- **替换语义**：换内容（保留骨架）/ 换风格（保留内容）/ 调节强度——每种模式都有明确的锁定区段。
- **输出形态**：图像提示词（通道：`grok-imagine-image-2.0` 网关直连；无负向通道；768×1152）、10 秒网页动画任务书（确定性契约 C1–C10 + 乱序重渲检查）、Blender 任务书（C9 + P1 确定性说明）。

## 5. 实验

`experiments/` 存放证据。每个实验目录包含脚本、原始请求/响应存档、输出，以及一个验证器（`_verify*.py`）——验证器通过即验收门槛。

- `E1_t1*`——12 格风格迁移矩阵：基线、题材偏置诊断、纯风格段拆分（7/7 解除）。
- `E2_t1`——首批组合（莫奈×梵高、达·芬奇×卡拉瓦乔、莫奈×塞尚）：融合可行，冲突轴以二选一或分区方式解决。
- `anim_test_01/02/03`——用非前沿模型验证的三条端到端管线：像素卡（网页）、一笔画卡（网页）、3D 质感卡（Blender）。关键发现：*管线可迁移，风格机制必须重写并配套机械检查*。

## 6. 运维（AI-ops）

本仓库由 **AI agent 运维**；ops 层是一等公民：

- `ops/GOALS.md`——工作状态的唯一事实来源（每项：状态 / 目标 / 产物路径 / 归属 + 一行验收）。
- `ops/OPS-LOG.md`——只追加：通道状态、事故、教训、授权记录。
- **LOOP 协议**：取目标 → 深度研究 → 落盘产物（带证据分级）→ 自审 → 主脑验收 → 新线索入队。详见 `docs/WORKFLOW.md`；硬性规则见 `docs/PROTOCOLS.md`。
- 机器级派发板位于仓库之外（`~/.dwgx/ops/boards/`）——板只是快照，永远不是事实来源。

## 7. 文档与 i18n

- `docs/` 以英文撰写（正本）。`docs/i18n/zh-CN/` 与 `docs/i18n/ja/` 对应 `ARCHITECTURE / WORKFLOW / PROTOCOLS / ROADMAP` 四篇；根目录 README 三件套遵循 GitHub 惯例。
- 译稿会做术语一致性评审；英文源发生实质性变更时，译稿同步更新或明确标注为过期。
- 中文仍是原始研究笔记（档案、日志）的工作语言；对外界面为三语。

## 8. 扩展点

- **新领域** → 注册契约（§3.2）+ `domains.yaml` 注册项 + 自检覆盖。
- **新输出形态**（如印刷级海报、视频）→ 加入输出形态映射，附必填字段 + 确定性/验证说明。
- **新管线**（如 Blender → 网页）→ 在 `knowledge/agent-art/` 中记录，含探针与验证器。
- **新语言** → 镜像 `docs/i18n/<lang>/` + README 变体；并加入语言切换行。

## 9. 非目标

- 不是模型训练项目（不做微调、不做 LoRA 训练——蒸馏知识停留在提示词/代码层面）。
- 不二次分发第三方媒体（视频、参考片均不收录；见 `.gitignore` 与 `NOTICE.md`）。
- 没有证据分级就没有论断；没有可运行的检查就没有「完成」。
