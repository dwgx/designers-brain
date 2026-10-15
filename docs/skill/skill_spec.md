# Designers_Brain 设计顾问 skill · 规格 v0.2

> 版本 v0.2（2026-10-15）｜沿革：v0.1 初稿 → **R1 并入 SkillEcosystem 交付**（`docs/skill/skill_ecosystem.md`，456 行 + refs 精选 23 文件）｜写手：SkillSpec｜本文件 = 规格；配套草案：`docs/skill/draft/SKILL.md`
> R1 并入清单：§2.6 视觉决策协议、§2.3/§2.4 增补、§5.1/§5.2 引用规范、§1.1/§1.4/§1.5 补充、引文路径修正（SkillEcosystem 已把旧归档目录精选化移除 → 改引 `refs/superpowers/`）。明细见 §7。
> 口径：本规格不新增研究结论，只定义「路由 + 协议」层；内容一律引用仓库既有文件（单点，不复制）。
> 路径基准：`D:/Project/Designers_Brain`（下称 **REPO**）。本文件引用路径已自检（§6）。

---

## 0. 定位

**一句话**：把仓库既有研究资产（11 画家模块卡 / 15 MG 风格卡 / 冲突清单 C-01–C-18 / 组合规则 N1–N9 / 三种输出形态与确定性契约）打包成一个**设计顾问 skill**——agent 拿到「设计 / 替换」需求后**先问**（三句话 + 风格意图 + 替换意图），多轮收敛，然后**按推荐逻辑选卡、按替换语义改写、按输出形态出稿**；全程引用仓库既有文件，不复制、不漂移。

### 0.1 资产盘点（skill 的「零件」全部已存在）

| 资产 | 位置（REPO 相对） | 在 skill 里的角色 |
|---|---|---|
| 11 画家模块卡 + 索引 | `knowledge/domains/painters/modules/`（README + 11 卡） | 推荐域 A：图像 / 动画风格模块 |
| 11 份画家档案（正本） | `knowledge/domains/painters/dossiers/` | 卡的上游正本（卡 = 浓缩，档案 = 全量） |
| 15 MG 风格卡 | `knowledge/domains/motion-graphics/origin/`（截图 + `提示词全文.md`） | 推荐域 B：10 秒 MG 动画骨架 |
| 15 卡结构蒸馏 / 管线手册 | `knowledge/domains/motion-graphics/cards/structure.md`、`knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md` | 域 B 的索引与实现细节 |
| 冲突清单 + 组合规则 | `knowledge/cross/conflicts.md`（C-01–C-18 / N1–N9 / 8 对 near-miss） | 推荐逻辑的预检层（正本） |
| 输出形态与契约 | `templates/style_card.md`、`templates/determinism_contract.md`、`knowledge/cross/transfer_guide.md` | 「怎么出」 |
| 管线（网页 / Blender） | `knowledge/agent-art/html/workflow.md`、`knowledge/agent-art/blender/workflow.md` | 「怎么出」的实现细节 |
| 实验证据与缺口 | `experiments/design.md`、`experiments/E1_t1b/`、`experiments/E1_t1c/`、`experiments/E2_t1/`、`experiments/anim_test_01/`、`experiments/anim_test_02/`、`experiments/anim_test_03_blender/` | 推荐的可信度标注与缺口 |
| 图像通道 | `knowledge/cross/image_channel.md` | 图像形态的通道口径 |
| 评审 | `knowledge/cross/review_rubric.md` | 出稿后的评审步骤 |
| 交互协议出处 | `knowledge/domains/motion-graphics/cards/author_tutorial.md`（三句话 / 只换内容不动骨架）、`docs/skill/refs/superpowers/brainstorming_SKILL.md`（问法纪律）、`docs/skill/skill_ecosystem.md` §4（问法清单 / 视觉协议 / 停止规则） | §2 的根据 |
| 格式与打包事实 | `docs/skill/refs/spec/`（官方摘录）、`docs/skill/refs/superpowers/manifest_samples.md`（三份清单实样）、`docs/skill/skill_ecosystem.md` §2–§3 | §1 的官方依据（SkillEcosystem 归档） |

### 0.2 非目标

- 不新增 / 不改写研究结论；卡有冲突时以 `conflicts.md` 为正本，卡级注记次之。
- 不做发布 / 分发动作（repo 无 git）；打包件只做「文件就位」设计，本机激活走 junction（§1）。
- 不跑强度扫描实验（E3 未做）——缺口在 §4.4 标注。
- 不把任何仓库内容复制进 skill（除指针与协议文字本身）。

---

## 1. 激活方式：仓库内嵌 skill + 多 harness 打包（最小可行）

### 1.1 设计原则（三条）

1. **单源**：skill 物理实体只有一份，住在仓库里；harness 通过 junction / 打包件「看到」它——内容改动发生在仓库文件上，天然无副本漂移。
2. **零拷贝激活**：本机三 harness 全部用 junction（本机既有惯例，2026-10-15 实测 16 个同型实例：claude 7 / codex 5 / omp 4）；不复制、不安装。
3. **渐进披露**：SKILL.md 是入口（<500 行）；细节都在 `references/` 指针与仓库既有文件里，用到才读——catalog（name+description，~100 token 常驻）→ 正文（触发时加载）→ 资源（按需）；口径见 agentskills.io 规范与 `docs/skill/skill_ecosystem.md` §3.1。

### 1.2 布局（L0 · 单源，⏳ 规划）

```
REPO/skills/designers-brain/         ← 技能包（⏳ v0.2 落地；v0.1 先落草案）
├── SKILL.md                          ← 入口（草案见 docs/skill/draft/SKILL.md）
├── references/                       ← 指针文件（只写「去哪读什么」，不复制内容）
│   ├── painter-modules.md            → knowledge/domains/painters/modules/README.md
│   ├── mg-cards.md                   → knowledge/domains/motion-graphics/cards/structure.md 等
│   ├── conflicts.md                  → knowledge/cross/conflicts.md
│   ├── output-forms.md               → templates/ + transfer_guide.md
│   └── evidence.md                   → experiments/ 相关文件
├── agents/openai.yaml                ← Codex 技能级 UI 元数据（§1.4）
└── domains.yaml                      ← 域注册表（§5.3）
```

- **为什么用 `skills/`（复数）**：Claude Code / Codex 插件在插件根下的默认扫描位就是 `skills/`（默认恒扫，清单字段只是「加扫」）——放这里，将来做插件时零配置（§1.4 已核）。
- 备选布局（规划）：包留在 `docs/skill/designers-brain/`（孵化期不动目录归属）；v0.2 定稿时二选一。
- 为什么单源可行：本机所有 harness 的激活都是「指向文件夹」而非「导入内容」——见 §1.3。

### 1.3 本机激活（L1 · MVP，零拷贝）

**原理**：三 harness 各自扫描固定目录；把 skill 目录 junction 进去即完成激活。本机既有同型实例（cross-dispatch / box-workflow / harness-audit 等）[实测]。

| Harness | 扫描位置（依据） | MVP 激活 |
|---|---|---|
| **omp** | `.agent/skills` + `.agents/skills`（project walk-up + user home）；另扫 `~/.codex/skills`、`.claude/skills/*/SKILL.md`、opencode 目录 [omp.exe 扫描串，实测] | junction `~/.agents/skills/designers-brain` → `REPO/skills/designers-brain` |
| **Claude Code** | `~/.claude/skills/<name>/SKILL.md` [本机 7 个 junction 实例，实测] | junction `~/.claude/skills/designers-brain` → 同上 |
| **Codex** | `~/.codex/skills` [本机 5 个 junction 实例，实测]；另认 `~/.agents/skills` 跨客户端别名（Codex / Copilot CLI / Gemini CLI，SkillEcosystem 直读） | junction `~/.codex/skills/designers-brain` → 同上 |

命令骨架（⏳ 执行时逐条先核目标不存在）：

```powershell
# 三条同型；-Target 均为 REPO/skills/designers-brain
New-Item -ItemType Junction -Path "$HOME\.agents\skills\designers-brain" -Target "D:\Project\Designers_Brain\skills\designers-brain"
New-Item -ItemType Junction -Path "$HOME\.claude\skills\designers-brain" -Target "D:\Project\Designers_Brain\skills\designers-brain"
New-Item -ItemType Junction -Path "$HOME\.codex\skills\designers-brain"  -Target "D:\Project\Designers_Brain\skills\designers-brain"
```

- 可选变体（跨客户端项目级约定）：在仓库内放 `<REPO>/.agents/skills/designers-brain`（junction 指回 `skills/designers-brain`）→ omp 在仓库内工作时 **project walk-up 自动激活**，且 Codex 等别名客户端同样受益。规则：项目级 `<project>/.agents/skills/` 与用户级 `~/.agents/skills/` 同名时**项目级覆盖**；扫描 = 找「含 SKILL.md 的子目录」，跳过 .git / node_modules，深度限 4–6 层（SkillEcosystem 直读）。取舍：激活更「本地」，但仓库多一个隐藏目录；v0.2 定。
- 注：omp 的「user home」即 `~/.agents/skills`——与上表第一行同一条 junction，无重复安装。
- 交叉核验：与 `docs/skill/skill_ecosystem.md` §3.4「本机实测交叉」一致（该节引本线 7+ 实例口径）。

### 1.4 打包件（L2 · 分发就绪，⏳ 未验证）

本机 MVP 不需要打包件；以下是「repo 将来可被当插件安装」的设计。**字段语义已按 SkillEcosystem 交付修正**（2026-10-15；官方摘录归档：`docs/skill/refs/spec/claude-code_plugin_manifest_excerpt.md`、`docs/skill/refs/spec/codex_plugin_manifest_spec.md`；三份清单实样：`docs/skill/refs/superpowers/manifest_samples.md`；综述：`docs/skill/skill_ecosystem.md` §3.5）。

| Harness | 打包件 | 关键语义（已核） |
|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` | `skills` 字段 = **加扫**（adds to the default `skills/` scan，默认恒扫）：值为「技能目录」——`<name>/SKILL.md` 的父目录，或直接含 `SKILL.md` 的单技能目录；路径必须 `./` 开头。特例：插件根有 `SKILL.md`、无 `skills/`、清单无 `skills` 键 → 整插件按单 skill 加载。组件（skills/ 等）放插件根，**不放** `.claude-plugin/` 里 |
| Codex | `.codex-plugin/plugin.json` | 字段含 `skills`（相对路径；同样「默认发现之上加扫」）+ `interface` UI 块；**技能级** UI 元数据放 skill 目录下 `agents/openai.yaml`（`interface: display_name / short_description / icon_small / icon_large`）。`interface.defaultPrompt` ≤3 条 × ≤128 字符；screenshots 必须 PNG 且存 `./assets/` |
| omp / 跨家 | `.agents/plugins/marketplace.json` | 仓库级市场文件（个人级 = `~/.agents/plugins/marketplace.json`）；条目 = `name / source{source: local, path: ./plugins/<name>} / policy{installation, authentication} / category`；`interface.displayName` 放顶层 |

样例骨架（⏳ 设计稿；布局按 §1.2 的 `skills/designers-brain/`）：

```jsonc
// .claude-plugin/plugin.json（⏳；skills/ 为默认扫描位——无需 skills 字段）
{ "name": "designers-brain", "version": "0.1.0", "description": "Designers_Brain 设计顾问：画家模块 × MG 卡 × 冲突清单 × 输出契约", "keywords": ["design", "agent-skill"] }

// .codex-plugin/plugin.json（⏳；"skills" 为加扫字段，superpowers 实样写法）
{ "name": "designers-brain", "version": "0.1.0", "description": "…", "skills": "./skills", "interface": { "displayName": "Designers Brain", "shortDescription": "设计顾问 skill", "defaultPrompt": ["帮我为这个需求选风格并出稿"] } }

// skills/designers-brain/agents/openai.yaml（⏳ 技能级 UI 元数据）
interface:
  display_name: "Designers Brain"
  short_description: "设计顾问：选风格 / 换风格 / 换内容 / 出稿"
  default_prompt: "帮我为这个需求选风格并出稿"

// .agents/plugins/marketplace.json（⏳ 仓库级；source.path 按 Codex 规范）
{ "name": "designers-brain-dev", "interface": { "displayName": "Designers Brain" }, "plugins": [ { "name": "designers-brain", "source": { "source": "local", "path": "./plugins/designers-brain" }, "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" }, "category": "Design" } ] }
```

- 无 git → marketplace 分发暂不适用；打包件是「文件就位」，安装路径未在本机验证，标 [UNVERIFIED]。
- 说明：三种打包件与 §1.3 的 junction 激活**互相独立**——junction 是「本机现在就能用」，打包件是「将来可分发」；skill 本体（SKILL.md + references + domains.yaml）对两者是同一份。

### 1.5 命名与 frontmatter 规范（agentskills.io 口径）

- `name: designers-brain`——≤64 字符；仅小写字母 / 数字 / 连字符；不得以连字符开头结尾、不得连续连字符；**必须与父目录同名**。
- `description` ≤1024 字符；含触发关键词（中文为主 + 关键英文词）。
- 可选字段：`license` / `compatibility` / `metadata` / `allowed-tools`（v0.1 不用；`metadata` 可留 version）。
- description 写法纪律（superpowers 实证）：**只写「何时用」，不概括流程**——防 agent 按 description 走捷径、跳过正文；触发面写具体（点名画家 / 卡 / 任务类型）；可加中英关键词（`skill_ecosystem.md` §2.2a / §5.2）。
- 非标准字段（如 `disable-model-invocation`）生态里有人用，但**别依赖所有客户端都读**；核心触发只靠 `name` / `description`（`skill_ecosystem.md` §2.3）。
- SKILL.md 正文 <500 行；详细内容全走 `references/` 指针。

### 1.6 激活自检（⏳ 三条）

1. **junction 解析**：`realpath` 各 harness 路径 == `REPO/skills/designers-brain`。
2. **frontmatter 校验**：name / description 存在且合规（name 与目录同名）。
3. **路径存在性**：§6 同款脚本——抽取 skill 内全部 `REPO/...` 引用逐条 `exists()`。

---

## 2. 交互协议：先问什么、怎么收敛、何时停

> 出处：三句话法 = `knowledge/domains/motion-graphics/cards/author_tutorial.md` §3 第 7 条 / §4.1 t0050（① 你是做什么的 ② 给谁看 ③ 手上有什么物料）；「只换内容不动骨架」= 同文 t0064；问法纪律（一次一题、先开放、回述、默认说出口）= `docs/skill/refs/superpowers/brainstorming_SKILL.md`（superpowers 实证，改写为项目口径）；增补（问法清单 / 视觉协议 / 停止规则）= `docs/skill/skill_ecosystem.md` §4.2–§4.5。

### 2.1 触发与例外

- **触发**：用户要做设计 / 替换 / 出稿——「帮我选风格」「换个画家」「换内容不换骨架」「调强度」「做一张图像 prompt / 一支 10 秒 MG 动画 / Blender 场景」等。
- **先问后做**（本 skill 的身份）：拿到需求**不得直接出稿**；先发「首问包」（§2.2），除非：
  - **例外 A（opt-out）**：用户说「直接做 / 随便」→ 停问，用默认值做（§2.4），一行列出假设；
  - **例外 B（信息已在场）**：需求里已含三句话 + 两个意图的全部信息 → 复述确认一次，直接进推荐（§3）。

### 2.2 首问包（一条消息，3+2 项，填空式）

```text
先确认 5 件事（填多少算多少，剩下我按默认来）：
① 你是做什么的：<业务 / 产品 / 身份，一句话>
② 给谁看：<受众 + 场景，一句话>
③ 手上有什么物料：<文件 / 图片 / 文档 / 现成文案，列路径>
④ 风格意图：想要什么感觉 / 点名谁？（11 画家、15 张 MG 卡，或说气质我推荐）
⑤ 替换意图：这次是——A 换内容（有骨架，换故事/品牌/文案）/ B 换风格（同一内容换模块）/ C 调强度（同模块强弱）/ D 从零选型？
```

### 2.3 多轮收敛（≤3 轮）

- **轮次预算**：首问包（1 轮）→ 补问（≤2 轮，每轮 ≤2 问）→ 出「推荐单」（§3.6）或首稿。总轮数到 3 必须落稿（或明说缺什么、用默认值落稿）。
- **问法纪律**：
  - 一次一题（补问阶段）；先开放后选择——用户卡住才给 2–3 个短选项（不给长菜单）；
  - 猜测式提问优先：「我猜是 X，因为 Y？」——用户纠正比从零描述便宜；
  - **每问必须改变工作**（`skill_ecosystem.md` §4.2-4）：两个答案产出同一稿 → 那不是问题，是默认值——取默认、说出口；
  - **infer-first 上限**（§4.2-9）：能自己定的不问；补问最多两个子问题；只请用户纠正「会实质改变产出」的假设；
  - 能查的不问：物料路径、卡是否存在、冲突命中——自己去仓库核（§3）。
- **回述（playback）**：每理解一块，用自己的话回述；本项目压缩为「推荐单预览」——候选卡 + 冲突预检 + 输出形态 + 强度，让用户一次校正（比逐块回述省轮次）。
- **默认值规则**：问不到就用默认，且**默认要说出口**（没说出口的默认 = 用户无法否决）；被否决则更新推荐单。

### 2.4 停止条件（何时停止提问）

**最小可执行集**（五件齐 → 停问，落稿）：

1. 主题 / 内容（含受众）；2. 风格模块（单卡或主 + 辅）；3. 替换轴（A/B/C/D）；4. 输出形态（图像 / 网页动画 / Blender）；5. 强度档（§4 默认起步）。

- **缺件 → 用默认补**：默认 = 卡内 §4 默认档、单模块（非组合）、组合时 70/30、T1 类主题、按 §3.5 的形态映射。
- **必须问**（不许默认）：业务 / 受众完全未知且影响选型；替换轴不明（A / B 产出完全不同）；风格意图与物料硬冲突（如物料品牌色撞「同屏 ≤3 色」）。
- **不许问**：仓库可查的（先查）；用户明确表示不要问的；已有默认且不影响方向的（说出口即可）。
- **假设留档**（R1 并入 `skill_ecosystem.md` §4.2-12）：未问项写成 assumption（内容 + 默认 + 错了的代价）随推荐单一起给出——「静默的假设 = 猜测」。
- **批准不越级**（§4.5-1）：确认只覆盖「实际展示过的东西」（推荐单 / 关键帧 / 对比页）；没展示的阶段不算已批准。

### 2.5 视觉决策协议（设计场景专条；R1 并入 `skill_ecosystem.md` §4.3）

风格 / 画面类的关键决策，**不许让用户在「只有文字、没看到视觉」时选**：

- 候选要给「看得见的东西」：2–3 个差异化方向（项目现成手段：E 系列出图通道 / HTML 渲染 / 参考帧）。
- **候选数口径（S-04 裁定，2026-10-15）**：默认 2–3 个；成本敏感可压到 2；不得只出 1 个（用户明确要求单一方向除外）。
- 成本敏感时走两步法：先给文字方向卡（各 3–4 行）让用户选，定得下来就只做选中那一个；要画面再做对比页。
- **展示后必须停**：等用户选择，不得自选继续（含无人值守会话）。
- 用户拒答 / 无回应：不枯等——补齐 assumption 标注（§2.4），继续到「可展示」再停。
- 出处：`skill_ecosystem.md` §4.3（huashu 三方向门 / 选择无效铁律 / oil-ui 两步法 / 展示后停）。

### 2.6 反模式（写进 SKILL.md 的「红旗」表）

| 想法 | 现实 |
|---|---|
| 「先做一版再问」 | 出稿成本高、方向错全废；先问（opt-out 除外） |
| 「给一堆选项让用户挑」 | 选项会带偏；先让用户描述，卡住才给短菜单 |
| 「默认不用说了吧」 | 没说出口的默认，用户无法否决 |
| 「用户说随便，那我不问了」 | 对——但要一行列出所有假设再动手 |
| 「再问一轮更保险」 | 超过 3 轮就是审问；用默认值 + 缺口标注落稿 |
| 「文字里选风格也一样」 | 没看到视觉的选择无效；给看得见的候选，展示后停（§2.5） |

---

## 3. 推荐逻辑：意图 / 物料 → 模块卡选择

### 3.1 输入 / 输出

- **输入**：意图（业务、受众、情绪目标、参考物）+ 物料（文案 / 图片 / 品牌 / 路径）+ 约束（输出形态、时长、渠道）。
- **输出**：**推荐单**（§3.6）——候选卡（主 / 辅）、冲突预检结果、强度、输出形态与必带字段清单、缺口与假设。

### 3.2 域与卡过滤（第一层）

**域 A · 画家模块（11 卡）**——能力定位速查（正本：`knowledge/domains/painters/modules/README.md`）：

| 卡 | 能力定位 | 相关 C 条（conflicts.md） |
|---|---|---|
| 达·芬奇 | 塑造真实 / 柔和明暗（sfumato） | C-02 · C-03 · C-05 · C-06 · C-14 |
| 米开朗基罗 | 人体结构 / 力量感 / 动态构图 | C-01 · C-02 · C-17 · C-18 |
| 梵高 | 情绪表达 / 方向性笔触 / 色彩张力 | C-05 · C-09 · C-12 |
| 莫奈 | 光线 / 空气感 / 环境色 | C-05 · C-06 · C-10 · C-14 |
| 毕加索 | 几何解构 / 多视角 / 形体重组 | C-06 · C-16 · C-18 |
| 塞尚 | 结构 / 体积 / 空间构成 | C-04 · C-05 · C-10 · C-13 |
| 马蒂斯 | 色彩设计 / 轮廓 / 平面构成 | C-06 · C-15 · C-16 · C-17 · C-18 |
| 北斋 | 线条 / 剪影 / 动态构图 / 平面叙事 | C-07 · C-12 · C-16 · C-17 |
| 卡拉瓦乔 | 光的开关 + 物理（硬光戏剧） | C-01 · C-03 · C-04 · C-08 · C-11 · C-12 · C-13 |
| 维米尔 | 室内自然光 + 材质表面 | C-08 · C-09 · C-11 |
| 丢勒 | 排线明暗 + 版画工艺 | C-07 |

**域 B · MG 风格卡（15 卡）**——按内容 / 氛围选（正本：`knowledge/domains/motion-graphics/origin/提示词全文.md`；结构：`knowledge/domains/motion-graphics/cards/structure.md`）：

01 3D 质感（Blender）· 02 液态 · 03 等轴 2.5D · 04 复古未来 · 05 形变 · 06 包豪斯 · 07 科幻 HUD · 08 一笔画 · 09 玻璃拟态 · 10 拼贴 · 11 像素 · 12 手绘线条沸腾 · 13 扁平矢量 · 14 贴纸科普 · 15 综艺花字。

**意图 → 卡 的信号映射（示例，非穷举）**：

- 情绪张力 / 表现主义 → 梵高；宁静光感 → 莫奈 / 维米尔；戏剧冲突 → 卡拉瓦乔；力量 / 人体 → 米开朗基罗；解构 / 先锋 → 毕加索；结构稳重 → 塞尚；色彩欢快 / 海报感 → 马蒂斯；东方线韵 → 北斋；工艺 / 版画感 → 丢勒。
- 「发布会 / 科技感」→ MG 07 / 03；「数据科普」→ 14 / 13；「复古潮流」→ 04 / 15；「极简高级」→ 06 / 13；「手工 / 温情」→ 12 / 10；「像素 / 游戏」→ 11。
- 物料含照片 → 注意贴纸 / 拼贴卡需真实素材（vsc 教训：复刻必须真实截图）；物料含品牌色 → 触发马蒂斯 vs 低饱和模块的 C-06 预检。

### 3.3 组合预检（第二层，仅当 ≥2 模块）

**顺序**（照 `artist_modules/README.md`「组合前检查单」+ `conflicts.md` 正本）：

1. 查 `conflicts.md` §1 总表：命中 C 条 → 按该条处置（反约束改写 / 轴单主 / 分区表 + 掩膜）；
2. 查 §4 near-miss 表：非冲突但**必须显式取值**（不取值会被静默折中成「两个都不像」）；
3. **N1** 反约束一致性检查：逐条反约束 × 逐条画风规则，标一致 / 冲突；组合卡必须**重算反约束段**；
4. **N3** 轴所有权表（`轴名 | 持有模块 | 对方处置`）；辅模块冲突轴规则**整条移除**（不是降档）；
5. **N4** 可拆 / 不可拆：同一像素统计量 → 二选一；可分区域 → 写死分区表 + 掩膜；
6. **N9** 验收口径：自查表 = 主模块全集 + 辅模块非冲突轴规则；「冲突轴上出现双标准」= 失败形态。

**N1–N9 速览**（正本 `knowledge/cross/conflicts.md` §3）：N1 反约束一致性 / N2 适用域（`别做成：<对象>的<行为>`）/ N3 轴所有权表 / N4 可拆判别 / N5 改写句式模板（硬阴影、运动模糊、渐变、强调色）/ N6 色数计数口径（平涂层 vs 材质层）/ N7 高光分类口径 / N8 运动预算字段 / N9 组合卡验收。

**18 条 C 冲突结构**（写进推荐单时的口径）：12 硬 / 5 覆盖 / 1 退化；四类根因 = ① 同一统计量两端（不可拆，二选一）② 同一预算的分区主张（可拆，须分区表）③ 反约束字面超范围（改写句式）④ 全画面表面系统互斥（二选一）。

### 3.4 强度映射（第三层）

- 起步 = 卡内 §4 默认值；用户给「时期 / 子风格」时按 §4 三档调（如梵高：早期 / 阿尔勒 / 圣雷米）。
- **只调 §4；§8.2 不调档**（N3 纪律：冲突轴用删除 / 分区，不用降档）。
- 跨场景 / 去题材 → 用 §8.1b 纯风格段（7 卡有；4 卡为注记；michelangelo 为 v2 改写版）。
- **缺口（必须标注）**：强度扫描实验（E3：30/50/75/100%）**未做**——`experiments/design.md` §2 有设计、无结果；凡涉及「强度定量响应」的承诺标 [UNVERIFIED]。

### 3.5 输出形态映射（第四层）

| 条件 | 形态 |
|---|---|
| 单张 / 静帧、探索风格、给图像模型用 | **图像 prompt**（§4.5.1） |
| 10 秒成片、2D / 排版 / 特效、可逐帧自查 | **网页动画 brief**（§4.5.2） |
| 3D / 材质 / 物理、玻璃 / 金属 / 回弹类 | **Blender brief**（§4.5.3） |

（MG 卡 01 固定 Blender，其余 14 张固定网页逐帧——任务头写死。）

### 3.6 推荐单模板（输出物）

```text
推荐单 v1
① 候选：主 <卡>（70%）+ 辅 <卡>（30%，可选）｜理由：<能力定位一句>
② 冲突预检：命中 C-xx（处置：…）｜near-miss 取值：…｜N1 反约束重算：…
③ 强度：§4 档 <弱/中/强>（默认 <值>）；是否用 §8.1b：<是/否>
④ 输出形态：<图像/网页/Blender> + 必带字段清单（照 §4.5）
⑤ 缺口与假设：<[UNVERIFIED] 项、默认值项>
下一步：确认后出稿 / 直接出首稿
```

---

## 4. 替换语义：三种操作 × 三种输出形态

### 4.1 「骨架」定义（先定义再替换）

以 MG 卡为例（四段结构，`templates/style_card.md`）：

| 段 | 换内容时 | 换风格时 |
|---|---|---|
| 任务头（渲染器 / 规格 / 流程） | 🔒 | 🔒（渲染器按新卡切换：01↔网页） |
| 画风段（S1…Sn 量化规则） | 🔒 | ✅ 整段替换 |
| 内容段（故事 / 分镜 / 收尾文案） | ✅ | 🔒 |
| 反约束段（F1…Fn） | 🔒（但要重算：N1） | ✅ 随风格重算（N1） |
| Output 规格块 / 确定性条款 / 6 关键帧流程 | 🔒 | 🔒 |

画家卡口径：§8.1 / §8.1b 风格段 = 风格；主题句 = 内容；§4 = 强度；§8.2 = 验收规则（不调档）。

### 4.2 换内容不换骨架（A 操作）

**步骤**：① 拿卡 → ② 只改内容段 / Creative seed（故事、品牌（编造）、文案、配色）→ ③ **N1 重算**：逐条反约束 × 新内容（例：新配色撞「同屏 ≤3 色」→ 标冲突、按 N5 改写或收窄内容）→ ④ 收尾文案重写（验收锚点）→ ⑤ 出稿。

**守卫**：🔒 画风段、反约束段（除 N1 改写）、Output / Rules、流程不许动——「像风格那些的话就别动，那个的话是视频的灵魂」（作者原话，`author_tutorial.md` t0064）。

### 4.3 换风格不换骨架（B 操作）

**步骤**：① 保留内容段 / 主题句 / 规格 / 流程 → ② 风格段**整段替换**（A 卡 → B 卡；§8.1 ↔ §8.1b 按场景选）→ ③ 若新卡与同卡内其它模块组合 → 重跑 §3.3 冲突预检（N1 / N3 / N4）→ ④ 渲染器按新卡切换（01 Blender ↔ 其余网页）→ ⑤ 出稿。

**守卫**：风格段不许「两段并存 / 混写」（双模块走 70/30 组合规则，不是拼接）；Output 规格与验收锚点保留（收尾文案 = 一帧可核对）；实验口径：E1 / E2 系列即此操作的验证模式（同主题跨模块）。

### 4.4 强度调节（C 操作）

- **§4 档位**：默认起步、按时期 / 子风格调档；三档为可观察描述（见卡内）。
- **§8.1b 纯风格段**：跨场景 / 去题材时替换 §8.1 使用（E-02 派生；michelangelo v2 为从句级改写版）；4 张未偏置卡用「场景可迁移性注记」。
- **缺口（标注）**：强度扫描（E3）未做 → 强度-画面响应曲线无实测；建议档位间差异**先按描述使用**，需要定量时补 E3（设计已就绪：`experiments/design.md` §2 E3 行）。

### 4.5 输出形态与必带字段

#### 4.5.1 图像 prompt

**必带字段**：① 主题句（逐字、场景 + 光 + 情绪）② 风格段（§8.1 或 §8.1b，逐字）③ 强度档 ④ 融合句（70/30 时：`Fusion of two painterly languages: <Main> dominant (70%), <Aux> secondary (30%).`）⑤ 分区句（可拆冲突时写死分层边界）⑥ 负向段（**留档标注：通道无负向参数、不发送** [实测 B-20]）⑦ 通道口径（裸模型名 `grok-imagine-image-2.0`；size 请求 1024x1536 → 实回 768×1152 不严格）。

**确定性契约要点**（图像形态无逐帧契约，用「留档契约」）：

- req / resp JSON 原样留档 + sha256 manifest（照 E1 / E2 模式）；
- 不承诺可复现（采样通道；种子参数未验证 [UNVERIFIED]）——承诺**可追溯**；
- 「负向未发送」写进记录（防误读为「负向生效了」）。

#### 4.5.2 网页动画 brief

**必带字段**：① 任务头（固定句式：10 秒 MG、1920×1080、30 帧、网页逐帧渲染、音效代码合成卡点、先 6 关键帧）② 画风段（S1…Sn）③ 内容段（分镜 + 收尾文案）④ 反约束段（F1…Fn，判例式格式）⑤ 输出规格块（exactly 10.000 s / 300 帧 / −14 LUFS ±1 / ≤−1 dBTP）⑥ 确定性条款 ⑦ 6 关键帧锚点（0/45/90/150/225/285，末帧含收尾文案）⑧ 2 个验收帧号（写死在实施计划）⑨ 交付清单（video.mp4 / 6 帧 / contact sheet / cue 表 / 源码 / CREDITS.md / 自查报告）。

**确定性契约要点**（`templates/determinism_contract.md`）：

- C1–C8 最小集（renderAt 纯函数 / 禁壁钟 / 播种随机 / 可 seek / cue 单表双读 / 输出规格 / 素材许可）+ C10 关键帧先行；
- **①b 乱序重渲**（P0）：第二遍乱序抽帧重渲 → 逐帧 SHA256 全等；同序重渲会漏跨帧状态泄漏（B-07 实测 f0150 差 158 源像素）；
- 两跑一致 = 乱序 + SHA256；不通过先修非确定性源，不许说完成。

#### 4.5.3 Blender brief

**必带字段**：① 任务头（渲染器 = Blender Python 脚本搭场景）② 画风段（材质 / 光照 / 物理规则）③ 内容段 ④ 反约束段 ⑤ **C9 等价条款**（`blender -b --factory-startup -P ...`、显式 `--range`、物理预计算数据文件、PNG 序列）⑥ 6 关键帧先行（C10）⑦ 输出规格块 ⑧ 自查（帧数 / 时长 / 响度 + P1 口径）。

**确定性契约要点**：

- C9（无实时模拟；物理先算成数据文件）+ C10；
- 确定性口径 = **P1**：EEVEE 采样随机性 → 记录像素差（B-19 实测 max 5/255、≤0.05% 像素），非位级承诺；逐帧 SHA256 条款不适用于 Blender 路线（用像素差阈值替代）。

---

## 5. 文件布局与扩展

### 5.1 布局与「指针不复制」原则

（同 §1.2；关键纪律：`references/` 里每个文件 = 一屏内的**路由说明**（读哪个既有文件、读哪节、为什么），正文内容永远在仓库原文件里——单点更新，skill 侧零维护。）

指针文件示例（`references/conflicts.md` 的全文形态）：

```markdown
# 冲突清单（指针）
- 正本：REPO/knowledge/cross/conflicts.md —— §1 总表（C-01–C-18）、§3 组合规则（N1–N9）、§4 near-miss（8 对）。
- 用法：组合 ≥2 模块时必读；单模块时读 §4（取值）。
- 卡侧副本：REPO/knowledge/domains/painters/modules/*.md 的「冲突注记」（以正本为准）。
```

**引用规范**（R1 并入 `skill_ecosystem.md` §5.2）：

- **一层深**：SKILL.md → `references/*.md` → 项目文件；不许链中链（深链会让 agent 用 head 只读一半）。
- **不用 `@` 强加载**（`@` = 立即 force-load、烧 context）；用相对路径 + 显式要求标记（`**REQUIRED**: 先读 <路径>`）。
- **脚本经解释器调用**（`python scripts/x.py`），不裸路径。
- 引用上游文案时留**同步基线**（来源 commit / version / date，可对账）。

### 5.2 references 指针清单（全部指向既有文件）

| 指针文件 | 指向 |
|---|---|
| `references/painter-modules.md` | `knowledge/domains/painters/modules/README.md`（11 卡索引 + 组合速查）+ 各卡 |
| `references/mg-cards.md` | `knowledge/domains/motion-graphics/cards/structure.md` + `knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md` + `knowledge/domains/motion-graphics/origin/提示词全文.md` |
| `references/conflicts.md` | `knowledge/cross/conflicts.md` |
| `references/output-forms.md` | `templates/style_card.md` + `templates/determinism_contract.md` + `knowledge/cross/transfer_guide.md` |
| `references/pipelines.md` | `knowledge/agent-art/html/workflow.md` + `knowledge/agent-art/blender/workflow.md` + `knowledge/cross/image_channel.md` |
| `references/evidence.md` | `experiments/design.md` + `experiments/E1_t1b/` + `experiments/E1_t1c/` + `experiments/E2_t1/` + `experiments/anim_test_01/`、`experiments/anim_test_02/`、`experiments/anim_test_03_blender/` |
| `references/review.md` | `knowledge/cross/review_rubric.md` |

可选增补（R1 候选，v0.2 定稿时取舍；均指向既有文件）：`references/question-bank.md` → `docs/skill/skill_ecosystem.md` §4.2（12 条问法）；`references/direction-protocol.md` → 同文 §4.3 + `docs/skill/refs/design-packs/huashu-design_consultant_excerpts.md`。

### 5.3 域注册表设计（新域插拔）

**注册表**：`domains.yaml`（skill 根）——推荐逻辑只读注册表，不硬编码域；插拔 = 改一处。

```yaml
version: 1
domains:
  - id: painter                 # 域 A：画家模块
    name: 画家模块
    status: active              # active | incubating | planned
    cards: knowledge/domains/painters/modules/
    count: 11
    index: knowledge/domains/painters/modules/README.md
    sources: knowledge/domains/painters/dossiers/                  # 档案正本（11 份）
    conflicts: knowledge/cross/conflicts.md  # C-01–C-18 + N1–N9
    outputs: [image-prompt, web-animation, blender]
    intensity: card-§4          # 弱/中/强 + §8.1b
  - id: mg-motion               # 域 B：MG 动效卡
    name: MG 风格卡
    status: active
    cards: knowledge/domains/motion-graphics/origin/               # 15 卡（只读素材）
    count: 15
    index: knowledge/domains/motion-graphics/cards/structure.md
    handbook: knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md
    conflicts: knowledge/cross/conflicts.md
    outputs: [web-animation, blender]           # 01=Blender，其余网页
    intensity: none             # 固定骨架；强度调节待设计（缺口）
```

**新域插拔契约**（每域必须提供，缺一项 = 不许 `status: active`）：

1. **卡片目录**：每卡 = 独立 md（建议 frontmatter：name / 一句话 / 适用 / 强度）；数量与索引一致；
2. **索引**：卡清单 + 能力定位 + 组合注记；
3. **冲突清单**：本域 C 条（或声明「复用 N1–N9 通用规则 + 本域增量 C 条」并写明）；
4. **输出形态映射**：支持 image-prompt / web-animation / blender 中的哪些，各自必带字段差异；
5. **强度机制**：§4 式档位 / 固定骨架 / 或标缺口；
6. **证据**：对应实验记录或标 [UNVERIFIED]（未验证域 `status: incubating`）；
7. **登记**：`domains.yaml` 加条目 + 自检脚本的路径校验清单更新。

**插拔流程**：新增域 = 建卡目录（新写手）→ 写索引 / 冲突 / 证据 → `domains.yaml` 登记 → 自检 → 通知 skill 维护者复核。移除域 = 删注册表条目（其余引用不允许硬编码，自然失效）。

**候选新域**（非画家，示意）：摄影 / 电影镜头（可接 video_shotcraft 方向）、字体排版、3D 材质。共同要求：照上契约准备「卡 + 冲突 + 输出 + 证据」四件，才允许进注册表。

### 5.4 维护与防漂移

- **单点纪律**：内容永远在仓库原文件；skill 只存指针与协议。卡更新 → skill 无需改；指针失效 → 自检脚本抓。
- **既有校验器复用**：模块卡逐字校验 `python knowledge/domains/painters/modules/_extract.py --check`（期望 `checks=33 ok=33 fail=0`）；冲突清单被推翻时的「三处同步」（conflicts.md 正本 / style_card / design.md）纪律照旧。
- **skill 自检**（脚本已落盘：`docs/skill/_selfcheck.py`；包建成后扩展 ③/④）：① 全部 `REPO/...` 引用 exists()；② frontmatter 合规；③ junction 解析；④ `domains.yaml` 中 cards 数与目录实际数一致。
- **并入记录**：R1 已完成（2026-10-15，`skill_ecosystem.md` 交付并入——§2.5/§2.6、§5.1/§5.2、§1.1/§1.4/§1.5、§2.3/§2.4）；后续生态更新按同法复核（改动只落对应节 + §7 记录）。

---

## 6. 自检记录（本文件与草案的引用路径核验）

**检查器**：`docs/skill/_selfcheck.py`（本目录；可复跑：`python docs/skill/_selfcheck.py`）。

**口径**：抽取两文件全部 `REPO/...`、`D:/...`、`knowledge/...`、`templates/...`、`skills/...`、`references/...` 形态引用（反斜杠写法归一化同扫）→ 逐条 `exists()`（目录 / 文件 / 通配符分别处理）；`⏳ 规划`（包内文件、备选布局）与「打包件 / 机器级设计路径」单独列示、不计失败。

**结论**：仓库既有路径 **checked=36 ok=36 fail=0**；规划 18 条、打包 / 机器级设计 15 条、示意 5 条（均属设计稿，非「引用既有文件」）；草案 frontmatter 合规。时点：v0.2 / R1（2026-10-15）。

```
== 文件 ==
  docs/skill/skill_spec.md  refs(unique)=59
  docs/skill/draft/SKILL.md  refs(unique)=16

== 路径核验（仓库既有）==
  checked=36 ok=36 fail=0
  （目录 11 / 文件 24 / 通配符 1）
    ok   knowledge/agent-art/blender/workflow.md  [file]
    ok   knowledge/domains/motion-graphics/cards/author_tutorial.md  [file]
    ok   knowledge/cross/image_channel.md  [file]
    ok   knowledge/domains/motion-graphics/cards/mg-styles-15_handbook.md  [file]
    ok   knowledge/cross/review_rubric.md  [file]
    ok   knowledge/domains/motion-graphics/cards/structure.md  [file]
    ok   knowledge/cross/conflicts.md  [file]
    ok   knowledge/agent-art/html/workflow.md  [file]
    ok   knowledge/cross/transfer_guide.md  [file]
    ok   knowledge/domains/painters/dossiers/  [dir]
    ok   experiments/  [dir]
    ok   experiments/E1_t1b/  [dir]
    ok   experiments/E1_t1c/  [dir]
    ok   experiments/E2_t1/  [dir]
    ok   experiments/anim_test_01/  [dir]
    ok   experiments/anim_test_02/  [dir]
    ok   experiments/anim_test_03_blender/  [dir]
    ok   experiments/design.md  [file]
    ok   knowledge/domains/motion-graphics/origin/  [dir]
    ok   knowledge/domains/motion-graphics/origin/提示词全文.md  [file]
    ok   knowledge/domains/painters/modules/  [dir]
    ok   knowledge/domains/painters/modules/*.md  [glob(12)]
    ok   knowledge/domains/painters/modules/README.md  [file]
    ok   knowledge/domains/painters/modules/_extract.py  [file]
    ok   docs/skill/_selfcheck.py  [file]
    ok   docs/skill/draft/SKILL.md  [file]
    ok   docs/skill/refs/design-packs/huashu-design_consultant_excerpts.md  [file]
    ok   docs/skill/refs/spec/  [dir]
    ok   docs/skill/refs/spec/claude-code_plugin_manifest_excerpt.md  [file]
    ok   docs/skill/refs/spec/codex_plugin_manifest_spec.md  [file]
    ok   docs/skill/refs/superpowers/brainstorming_SKILL.md  [file]
    ok   docs/skill/refs/superpowers/manifest_samples.md  [file]
    ok   docs/skill/skill_ecosystem.md  [file]
    ok   docs/skill/skill_spec.md  [file]
    ok   templates/determinism_contract.md  [file]
    ok   templates/style_card.md  [file]

== 规划路径（⏳，不计失败）== planned=18
    ⏳ agents/openai.yaml
    ⏳ domains.yaml
    ⏳ references/*.md
    ⏳ references/conflicts.md
    ⏳ references/direction-protocol.md
    ⏳ references/evidence.md
    ⏳ references/mg-cards.md
    ⏳ references/output-forms.md
    ⏳ references/painter-modules.md
    ⏳ references/pipelines.md
    ⏳ references/question-bank.md
    ⏳ references/review.md
    ⏳ docs/skill/designers-brain/
    ⏳ skills/*/SKILL.md
    ⏳ skills/designers-brain
    ⏳ skills/designers-brain/
    ⏳ skills/designers-brain/SKILL.md
    ⏳ skills/designers-brain/agents/openai.yaml

== 打包件/机器级路径（设计稿，非仓库文件）== harness=15
    ⌂ .agents/plugins/marketplace.json
    ⌂ .agents/skills
    ⌂ .agents/skills/
    ⌂ .agents/skills/designers-brain
    ⌂ .claude-plugin/plugin.json
    ⌂ .claude/skills/*/SKILL.md
    ⌂ .codex-plugin/plugin.json
    ⌂ ~/.agents/plugins/marketplace.json
    ⌂ ~/.agents/skills
    ⌂ ~/.agents/skills/
    ⌂ ~/.agents/skills/designers-brain
    ⌂ ~/.claude/skills/<name>/SKILL.md
    ⌂ ~/.claude/skills/designers-brain
    ⌂ ~/.codex/skills
    ⌂ ~/.codex/skills/designers-brain

== 示意形态（占位符，跳过）== schematic=5
    ~ references/...
    ~ research/...
    ~ skills/...
    ~ skills/<name>/SKILL.md
    ~ templates/...

== 草案 frontmatter（docs/skill/draft/SKILL.md）==
  OK: name='designers-brain' (len=15, 小写/连字符=True, 首尾/连续连字符=True)
  OK: description 长度=294 (≤1024)
  note: name 与父目录同名的硬要求 → 最终落位 skills/designers-brain/SKILL.md 时满足（当前 draft/ 为临时位）

RESULT: PASS  (checked=36 fail=0 planned=18 schematic=5)
```

---

## 7. 变更记录

- **v0.1（2026-10-15）**：初稿五节（激活 / 交互 / 推荐 / 替换 / 布局）+ 草案 `draft/SKILL.md` + 自检脚本 `_selfcheck.py`。
- **v0.1+（同日）**：并入 SkillEcosystem 早期答复——§1.4 打包字段语义修正；§1.2 布局定为 `skills/designers-brain/`（默认扫描位）；§1.3 补 `.agents` 项目级约定。
- **v0.2 / R1（同日）**：并入 SkillEcosystem 交付（`skill_ecosystem.md` 456 行 + `refs/` 精选 23 文件）——新增 §2.5 视觉决策协议；§2.3/§2.4 增补（每问必须改变工作 / infer-first / 假设留档 / 批准不越级）；§2.6 反模式补一条；§5.1 引用规范（一层深 / 禁 @ / 脚本经解释器 / 同步基线）；§5.2 补全路径 + 可选增补指针；§1.1/§1.4/§1.5 补充；全引文路径修正（旧归档目录已精选化移除 → 改引 `refs/superpowers/`）。
- **v0.2+（同日）**：S-04 盲测裁定——候选数口径写入 §2.5（默认 2–3 / 成本敏感可压到 2 / 不得只出 1）；`skills/designers-brain/SKILL.md` 同步；建包与盲测记录见 `build_receipt.md` / `test_report.md`。
- **待办**：① 命名裁定：**`designers-brain`（主脑 2026-10-15 裁定确认；目录名与 frontmatter 同步采用）**；② 建包落地（§1.2）、junction 激活（§1.3）、打包件文件就位（§1.4）、`references/` 指针与 `domains.yaml` 落盘；③ 可选增补指针取舍（§5.2）；④ 压力测试（writing-skills RED-GREEN：无 skill vs 有 skill 对照，`skill_ecosystem.md` §5.5）。
