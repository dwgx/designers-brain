# Skill 生态调研 — superpowers 体系与「设计顾问 skill」可复用模式

> 调研日期: 2026-10-15 · 方法: GitHub API + raw.githubusercontent.com 直读（web_search 限流，全程未用）
> 目的: 为 Designers_Brain 提炼「设计顾问 skill」的 ① 格式规范 ② 触发/加载机制 ③ 提问协议 ④ 落地建议
> 留档: 关键原文全文/摘录见 `refs/`（索引见 §6.2）；引文均标注来源文件
> 验收对照: 参照项目 ≥4（实际 8）· superpowers 格式与提问原文摘录 ✓ · Designers_Brain 建议节 ✓（§5）

---

## 0. 速览（TL;DR）

1. **格式**：事实标准 = Agent Skills 开放规范（agentskills.io）——两个必填 frontmatter 字段 `name` + `description`；SKILL.md 主体 + 可选 `scripts/` `references/` `assets/`；渐进披露三层（元数据 ~100 token 常驻 → 正文 <5000 token 触发时加载 → 资源按需）。
2. **触发**：不靠关键词匹配，靠「description 进系统提示的 catalog + 模型自行判断 + Skill 工具加载」。superpowers 的独门增强 = **SessionStart hook 每会话注入 bootstrap**（using-superpowers），并用「1% 规则 + 红线表」压住模型"跳过 skill"的倾向。bootstrap 是全部集成的关键：没有它，skill 文件只是磁盘上的死重。
3. **提问（核心）**：现行 brainstorming 的公式 = 先自检已知 → **一次一个问题、单句、无选项列表** → 用具体锚定问法（"Walk me through the last time…"）→ 边聊边 **200-300 字复述回放、问"哪里不对/缺什么"** → HARD-GATE：批准前不建造。反模式明确点名：审问式清单、菜单诱导（garden-pathing）、"让用户替 agent 思考"的问法。
4. **设计场景变体**：huashu-design 把「视觉决策」从文字问答里拿出来——**三方向硬门**（先出 3 版真实视觉再让用户选，指定风格也不豁免）+ **选择无效铁律**（"绝不让用户在只有文字、没看到视觉时选风格"）+ **展示后必须停**；Waza 的补充是 **infer-first**（最多两个子问题、只让用户纠正实质假设）；grill-me 是 **七问一轮 + 未问项写成 assumption 留档**。
5. **对 Designers_Brain**：建议单 skill + references 拆分（§5.1）、引用项目模块卡用「一层深 + REQUIRED 标记 + 不用 @」的规范（§5.2）、交互协议采用「先推断后确认 + 视觉决策给看得见的候选 + gate 文件留档 + 拒绝回答不枯等」的组合（§5.3）。

---

## 1. 参照项目地图（8 个）

| # | 项目 | ★（2026-10-15） | 定位 | 本调研关注点 |
|---|---|---|---|---|
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 299k | 本体：agentic skills 框架 + 开发方法论（v7.0.0，15 个核心 skill） | skill 格式、bootstrap 加载、brainstorming、分发 |
| 2 | [obra/superpowers-skills](https://github.com/obra/superpowers-skills) | 751 | 社区可编辑 skill 库（分类目录 + 请求机制） | 社区组织方式 |
| 3 | [obra/superpowers-marketplace](https://github.com/obra/superpowers-marketplace) | 1.3k | Claude Code 插件市场（superpowers 及同族插件） | marketplace 分发 |
| 4 | [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) | 8.3k | 中文增强 fork（15 翻译 + 4 原创 + 26 工具适配） | 本地化方法、上游同步机制 |
| 5 | [tw93/Waza](https://github.com/tw93/Waza) | 7.3k | 8 个工程习惯 skill（think/ui/check/hunt/write/learn/read/health） | 路由、infer-first 提问、ui/think |
| 6 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | 25k | HTML 原生设计 skill（原型/幻灯片/动画/评审） | **设计顾问模式、三方向硬门** |
| 7 | [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | 1.8k | 高级设计架构师 kit（25 skill + 52 门禁 + 138 设计系统） | **grill-me 提问 skill**、gate 验证 |
| 8 | [oil-oil/oil-ui](https://github.com/oil-oil/oil-ui) | 1.5k | UI 设计 skill（方向探索 + 截图对比） | 两步式方向收敛协议 |

> 同族延伸（未深扫）：superpowers-lab（实验技能）、superpowers-chrome、episodic-memory 等，均见 superpowers-marketplace 清单（线上可查：obra/superpowers-marketplace）。

---

## 2. ① 格式规范摘要（带原文摘录）

### 2.1 官方规范：Agent Skills（agentskills.io）

superpowers 的 writing-skills 明确指向 [agentskills.io/specification](https://agentskills.io/specification)，这是跨客户端的事实标准（全文留档 `refs/spec/agentskills_specification.md`）。

**目录结构**（原文）：

> ```
> skill-name/
> ├── SKILL.md          # Required: metadata + instructions
> ├── scripts/          # Optional: executable code
> ├── references/       # Optional: documentation
> ├── assets/           # Optional: templates, resources
> └── ...               # Any additional files or directories
> ```

**frontmatter 字段表**（原文整理）：

| 字段 | 必填 | 约束 |
|---|---|---|
| `name` | ✅ | ≤64 字符；仅小写字母/数字/连字符；不能以连字符开头/结尾；不能连续连字符；**必须与父目录同名** |
| `description` | ✅ | ≤1024 字符；非空；描述「做什么 + 何时用」 |
| `license` | – | 许可名或指向随附许可文件 |
| `compatibility` | – | ≤500 字符；环境要求（产品、依赖、网络等） |
| `metadata` | – | 任意 string→string 键值（客户端自定义扩展位） |
| `allowed-tools` | – | 空格分隔的预批准工具列表（**实验性**，支持度因客户端而异） |

**正文**：「There are no format restrictions. Write whatever helps agents perform the task effectively.」推荐节：分步指令 / 输入输出示例 / 边界情况。**「the agent will load this entire file once it's decided to activate a skill. Consider splitting longer SKILL.md content into referenced files.」**

**引用规则**（原文）：文件引用用相对路径、**保持一层深**（"Keep file references one level deep from SKILL.md. Avoid deeply nested reference chains."）；建议 SKILL.md 正文 <500 行；>100 行的 reference 文件顶部加目录。

### 2.2 superpowers 实践：writing-skills（描述写法 / 预算 / 引用）

`refs/superpowers/writing-skills_SKILL.md`（全文）里，最重要的两条硬规则：

**(a) description 只写「何时用」，绝不总结流程**（原文）：

> - `description`: Third-person, describes ONLY when to use (NOT what it does)
>   - Start with "Use when..." to focus on triggering conditions
>   - Include specific symptoms, situations, and contexts
>   - **NEVER summarize the skill's process or workflow**

为什么（原文的实验证据）：

> Testing revealed that when a description summarizes the skill's workflow, an agent may follow the description instead of reading the full skill content. A description saying "code review between tasks" caused an agent to do ONE review, even though the skill's flowchart clearly showed TWO reviews.

**(b) 交叉引用格式与「不许 @」**（原文）：

> - ✅ Good: `**REQUIRED SUB-SKILL:** Use superpowers:test-driven-development`
> - ❌ Bad: `@skills/testing/test-driven-development/SKILL.md` (force-loads, burns context)
>
> **Why no @ links:** `@` syntax force-loads files immediately, consuming 200k+ context before you need them.

**(c) token 预算**（原文）："getting-started workflows: <150 words each · Frequently-loaded skills: <200 words total · Other skills: <500 words (still be concise)"。

**(d) 文件组织三模式**（原文）：自包含（仅 SKILL.md）/ 带可复用工具（+ example.ts）/ 带重参考（+ 600 行 API 文档 + scripts）。脚本一律「经解释器调用」（`bash scripts/tool.sh`），不许裸路径（部分打包器会丢可执行位）。

**(e) 形式要匹配失败类型**（原文表格「Match the Form to the Failure」）：违反规则 → 禁令 + 合理化表 + 红线表；产出形状不对 → **正向配方/契约**（禁令反而更差，有头对头实验）；漏要素 → 模板槽位；条件行为 → 可观察谓词的条件式。

### 2.3 各包的 frontmatter 扩展实践（生态现状）

| 包 | frontmatter 实际字段 | 说明 |
|---|---|---|
| superpowers 本体 | `name` + `description`（最小集） | 见 `refs/superpowers/*_SKILL.md` |
| superpowers-zh | + `version` / `license` / `metadata.hermes.tags` | 翻译时补充，供多平台识别 |
| Waza | `name` / `description` / `when_to_use` / `dispatch_intent` | 自研校验器 `scripts/skill_frontmatter.py` 只认这四个「intentionally tiny」的标量；拒绝 legacy `metadata.version` |
| ux-ui-agent-skills | + `disable-model-invocation: true`（grill-me） | 用户手动触发型 skill：不进模型的选择清单、不进 listing 预算 |
| oil-ui | + `allowed-tools`（实验字段实际使用）/ `metadata.version` / `metadata.compatibility` | 长 description（中英双语触发词） |

**结论**：自定义字段是允许的（规范留了 `metadata` 位），但**别依赖非标准字段被所有客户端读取**；核心触发只能靠 `name`/`description`。用户手动型 skill 可用 `disable-model-invocation`（grill-me 的注释说明其语义：不进模型的 skill 选择清单）。

### 2.4 一句话版「写 skill 的 TDD」（superpowers 特有）

writing-skills 把 skill 当**行为塑造代码**管理：先跑压力场景看 agent 裸奔失败（RED）→ 写最小 skill 针对那些失败（GREEN）→ 收口新的合理化借口（REFACTOR）。核心原文：**"If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing."** 部署前 micro-test 措辞（≥5 reps + 无指导对照组 + 人工读每一条命中）。

---

## 3. ② 触发 / 加载机制（progressive disclosure）

### 3.1 三层渐进披露（官方）

`refs/spec/progressive_disclosure_client_guide_excerpt.md` 原文表格：

| Tier | What's loaded | When | Token cost |
|---|---|---|---|
| 1. Catalog | Name + description | Session start | ~50-100 tokens per skill |
| 2. Instructions | Full `SKILL.md` body | When the skill is activated | <5000 tokens (recommended) |
| 3. Resources | Scripts, references, assets | When the instructions reference them | Varies |

配套原文："The model sees the catalog from the start, so it knows what skills are available. When it decides a skill is relevant, it loads the full instructions." —— 20 个装好的 skill 不会预付费 20 份正文，只为实际用到的付费。

**发现路径**（原文整理）：项目级 `<project>/.<client>/skills/` + `<project>/.agents/skills/`；用户级 `~/.<client>/skills/` + `~/.agents/skills/`。`.agents/skills/` 是跨客户端共享的通行约定（"widely-adopted convention for cross-client skill sharing"）。同名冲突：**项目级覆盖用户级**。扫描规则：找「含 `SKILL.md` 的子目录」；跳过 `.git`/`node_modules`；限深 4-6 层。

**激活方式**（原文两选）：① 文件读取激活（模型直接 read 目录里的 SKILL.md，适合有文件工具的一切场景）；② 专用工具激活（`activate_skill` 之类，返回正文 + 可附带资源清单，可做权限/分析）。**都由模型自主判断**，不做 harness 侧关键词匹配。

### 3.2 触发链：从 description 到加载

完整链条（综合官方指南 + superpowers 实践）：

```
会话开始
  → 扫描 skills 目录，读全部 SKILL.md 的 frontmatter
  → 组装 catalog（name + description + 路径）注入系统提示 / 工具描述
  → 用户消息到达，模型比对 description 判断相关性
  → 命中 → 调用 Skill 工具（或 read）加载 SKILL.md 正文
  → 正文引用的 references/scripts 按需再加载
```

**所以 description 是唯一的「触发面」**：写作规范（§2.2a）+ 关键词覆盖（错误消息、症状、同义词、工具名都写进去）+ 动词优先命名（`creating-skills` 而非 `skill-creation`）。

### 3.3 superpowers 的 bootstrap：让触发「保底」

superpowers 不满足于"模型碰巧想起用 skill"，用两个机制强制：

**(a) SessionStart hook 注入**（`refs/superpowers/session-start_hook.sh` 全文）——每个会话启动时把 using-superpowers 全文包进 `<EXTREMELY_IMPORTANT>` 注入：

> ```
> You have superpowers.
> **Below is the full content of your 'superpowers:using-superpowers' skill - your introduction to using skills. For all other skills, use the 'Skill' tool:**
> ```

hook 配置（`hooks/hooks.json`）：`SessionStart` matcher = `startup|clear|compact`——启动、清空、压缩后都会重注入。脚本还处理了各平台差异（Claude Code 读 `hookSpecificOutput.additionalContext`；Cursor 读 `additional_context`；Copilot 等读顶层 `additionalContext`）。

**(b) using-superpowers 的「1% 规则」**（`refs/superpowers/using-superpowers_SKILL.md` 全文）：

> If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.
> Invoke relevant or requested skills BEFORE any response or action — including clarifying questions, exploring the codebase, or checking files.

配套「红线表」压制常见跳过借口（"这是个小问题"→"问题也是任务"；"我先探索下代码库"→"skill 告诉你**如何**探索，先检查"）。技能优先级：**process skills 先行**（brainstorming / systematic-debugging），实现类 skill 随后。用户指令（CLAUDE.md 等）> skill > 默认行为。

### 3.4 跨 harness 三组件模型（porting 文档原文）

`refs/superpowers/porting_across_harnesses_excerpt.md`（Part 1-3 摘录）——同一份 skill 跑遍 15+ harness 的架构：

1. **Skills（harness 无关）**：「Skills are written to describe *actions* — "invoke a skill", "read a file", "dispatch a subagent", "create a todo" — and never name a specific tool.」→ 这就是「**Skills name actions, not tools**」规则。
2. **Tool mapping（每 harness）**：动作词汇 → 真实工具名（`references/<harness>-tools.md`）。
3. **Bootstrap（每 harness）**：「**The bootstrap is the entire integration.** Without it, the skill files are inert — present on disk, never invoked.」

**硬性要求**（原文）："The harness must let you inject text into the model's context **at the start of every session, with no per-session opt-in**… If the only way to get Superpowers in front of the model is for your human partner to opt in each session… the harness cannot be properly supported." 以及「**Everything ships through the harness's own install mechanism. Never edit the user's files.**」

**各 harness 差异（要点）**：

| Harness | 加载形态 | 备注 |
|---|---|---|
| Claude Code | plugin + SessionStart hook 注入 bootstrap；Skill 工具加载其余 | 参考实现；官方 marketplace `claude-plugins-official` 可装 |
| Codex | **原生展示 skills，无 session-start hook**；`.codex-plugin/plugin.json` 用空 `hooks: {}` 抑制 hooks 自动发现 | 子代理需 `multi_agent = true` |
| Cursor | hook 注入（`additional_context`） | `.cursor-plugin/plugin.json` |
| Gemini CLI | extension + `contextFileName` 指向扩展自带的 GEMINI.md | Shape C（instructions-file） |
| OpenCode / pi | 进程内插件（session/message 生命周期回调注入） | `superpowers.js` / `superpowers.ts` |
| 其余（Kimi/Hermes/Muse/Devin/Droid/Qwen…） | 各自 install 命令或 marketplace | README 逐一列了安装命令 |

**验收测试**（原文，跨 harness 通用）：干净会话发一句 "Let's make a react todo list"，若集成正确，**在写任何代码前自动触发 brainstorming**。

**本机实测交叉**（同项目 SkillSpec 工人，2026-10-15）：本机 omp.exe 扫描 `.agent/skills`、`.agents/skills`（project walk-up + user home）、`.claude/skills/*/SKILL.md`、`~/.codex/skills`、`.codex/skills`、`~/.config/opencode/skills`；本机惯例是物理技能放 `~/.agents/skills/<name>`，junction 进各 harness 目录（cross-dispatch / box-workflow 等 7+ 实例）——即 `.agents/skills` 作为「真身」、各客户端目录做链接的落法。

### 3.5 安装与分发（plugin / marketplace）

**Claude Code 插件清单语义**（官方 plugins-reference 摘录，`refs/spec/claude-code_plugin_manifest_excerpt.md`）：

- 清单放 `.claude-plugin/plugin.json`；**其余文件（skills/、commands/、hooks/）放插件根**，不放 `.claude-plugin/` 里。
- `skills` 字段可选：路径或数组，「**Adds to the default `skills/` scan**」——默认 `skills/` 永远扫描，字段只是加扫；`"."`/`"./"` = 插件根。
- 特例：插件根有 `SKILL.md`、无 `skills/`、无 `skills` 键 → 整个插件按单 skill 加载。

**Codex 打包正解**（openai/plugins 官方仓库，`refs/spec/codex_plugin_manifest_spec.md`）：

- 清单 = `.codex-plugin/plugin.json`（name/version/description/author/license/keywords + 可选 `skills`/`hooks`/`mcpServers`/`apps` + `interface` 展示块）；`skills` 同样「supplemented on top of default component discovery」。
- 每个 skill 可带 `agents/openai.yaml` = **技能级 UI 元数据**（display_name / short_description / icon_small / icon_large）。
- 市场文件：个人 `~/.agents/plugins/marketplace.json`、仓库级 `<repo>/.agents/plugins/marketplace.json`；entry 含 `source` / `policy{installation,authentication}` / `category`。

**superpowers 分发矩阵**（README 原文归纳）：Claude Code（官方市场 `/plugin install superpowers@claude-plugins-official`；或 `obra/superpowers-marketplace`）→ Antigravity（`agy plugin install <repo>`）→ Codex App/CLI（openai 官方插件市场）→ Cursor（`/add-plugin superpowers`）→ Gemini（`gemini extensions install`）→ Copilot CLI（marketplace add）→ Grok / Kimi / OpenCode / Pi / Qwen / Hermes / Muse / Devin / Droid……共 15+ 种安装路径。**要点：同一仓库用 polyglot 清单（`.claude-plugin/`、`.codex-plugin/`、`.cursor-plugin/`、`.kimi-plugin/`…）一次分发全部平台**。

**社区库组织**（superpowers-skills）：按类目分目录（`architecture/` `collaboration/` `debugging/` `meta/` `problem-solving/` `research/` `testing/` + `using-skills/`）；贡献方式 = fork + PR；带 `skills/REQUESTS.md`（「希望存在的 skill」登记表，格式 = What I need / When I'd use it / Why / Added 日期）；插件自动 clone 到 `~/.config/superpowers/skills/`。

**中文 fork 的本地化方法**（superpowers-zh；其 brainstorming 译版见 §4.1）：

- 定位（CLAUDE.md 原文）：「完整翻译上游 skill + 叠加 4 个中国原创 skill（chinese-code-review / chinese-commit-conventions / chinese-documentation / chinese-git-workflow）+ 多工具适配（npx 一条命令支持 26 款 IDE/CLI）」。
- 翻译层：全部 SKILL.md 中文化 + frontmatter 补充 version/license/metadata；README 双语；26 个工具各配 docs。
- **上游同步机制**（`refs/zh/upstream-sync.json` 原文注释）：「audit 对已翻译文件只比『标题数』，正文改多少行都看不见——上游 v6.3.0 给 subagent-driven-development 加了 113 行，我们这边一声不吭。有了基线，audit 才能算出『自上次同步以来上游改了哪些文件、各多少行』」→ 记录 `upstream commit / version / date` 三个字段做同步基线。
- 边界：fork 专属内容（中文化、chinese-* skill）**只提 fork、不提上游**（上游 94% PR 拒绝率 + 「Fork-specific changes」规则）。

---

## 4. ③ 提问协议模式（哪些问法有效，附例子）

### 4.1 brainstorming 的三代演化（理解"为什么这样写"）

| 代际 | 版本/时间 | 结构 | 特征 |
|---|---|---|---|
| 一代 | 社区版 v2.2（`refs/community/brainstorming_v2.2_SKILL.md`） | 5 Phase：理解 → 探索 → 设计展示 → worktree → 计划交接 | 「一次一个问题」「Prefer multiple choice when possible」「200-300 词分节展示」 |
| 二代 | v6.x（中文版在译版，`refs/zh/brainstorming_SKILL.zh-CN.md`） | 三路径路由（探路/有界/架构级）+ HARD-GATE | 分类先行、路径声明、批准粒度细化；但「almost all of it about routing… Intent got squeezed into one paragraph」（重写文档自评） |
| 三代 | 2026-10-05 重写（`refs/superpowers/brainstorming_SKILL.md` + `refs/superpowers/brainstorming_rebuild_spec.md`） | 意图优先：自检 → 提问 → 回放 → 分级 → 书面设计 → builder-check → HARD-GATE | 删掉大部分路由仪式；「Ask, one question at a time. … Questions should help the human think, not quiz them.」 |

**重写的初心**（rebuild spec 原文）——最初只有 40 词的原始 prompt：

> "I've got an idea in my head. I'd like you to ask me lots of questions about it. As you think you understand what I really want, describe it to me in chunks of about 200-300 words. Once we're dialed in, write out an informal spec."

以及目标（原文）："The agent understands the *why* behind anything non-trivial, because **an agent that knows the why makes the hundred unstated decisions well.**"

### 4.2 有效问法清单（12 条，全部带原文例子）

**A. 节奏与形式**

1. **一次一个问题，单句，不带选项尾巴**：
   > "Each message ends with one question: a single sentence with no list of example answers hanging off it."
2. **开场 = 退出提示 + 一个开放式描述题**（新 brainstorming 的 first message 结构）：
   > "1. One line letting them know that if they'd rather skip the questions and have you just start, they can say so. … 2. One open question that gets them describing. Ask about a real moment or a concrete picture: **'What's the moment you find yourself wishing this existed?'** or **'Tell me about the people who'll be in the room.'**"
3. **一轮问完上限**（grill-me，适合"信息缺口明确"的场合，与"一次一问"互补）：
   > "**Maximum seven questions, asked in one round.** A drip of one question at a time is worse than a wrong assumption."
4. **每问必须改变工作**（grill-me）：
   > "Every question must change the work. If both answers produce the same build, it is not a question, it is a default — take it and say so."

**B. 问法质量**

5. **具体锚定三式**（brainstorming 原文）：
   > "Questions that work anchor in specifics: **'Walk me through the last time…'**, **'If it could only do one of these well, which?'**, **'What would make you wince if I got it wrong?'**"
6. **先猜后纠**（brainstorming 原文）：
   > "A guess they can correct (**'I'm guessing this is because X keeps biting you?'**) often beats a question."
7. **先描述后菜单**（brainstorming + rebuild spec 原文）：
   > "Get them describing. Open questions come first. **Their own words carry intent that your options can't. Offer a short menu only when they're stuck.**" / "menus garden-path people toward the agent's assumptions."
8. **"随便猜"/"你觉得呢" → 必须给具体提案**（brainstorming 原文）：
   > "When they say 'just guess' or 'what do you think?', propose something concrete."
9. **Infer-first：能自己定的不问**（Waza ui 原文）：
   > "**Infer first.** … ask in one compact clarification round with **at most two sub-questions**, only when the missing answer would materially change a deliverable. **State the strongest inferred answer for every unresolved dimension and ask the user to correct only the material assumptions.**"
   （grill-me 版："**Never ask what you can choose well. Taste is the job.** Ask about intent, content, and constraint; decide the rest."）
10. **先读再问**（grill-me 原文）：
    > "**Read before you ask.** Asking for something the repo already answers is noise, and it teaches the user that answering you is a waste of time."
    （先查 brief / CLAUDE.md / tokens / 相邻组件；「Every question you keep after this pass is one the code genuinely cannot answer.」）

**C. 回放与留档**

11. **200-300 字复述回放 + 问"哪里不对"**（brainstorming 原文）：
    > "Play back as you go. As soon as you understand one part well enough to describe it …, **describe that part back in about 200-300 words**, then return to questions about the next part. … **Mark anything you're guessing as your guess; only what they said goes in as theirs. End each chunk by asking what's wrong or missing.**"
    （huashu 的对应物 = "Phase 2 · 顾问式重述（**≥200 字**，把需求真正嚼透，不是敷衍一句）"。）
12. **未问项 = 书面 assumption（默认 + 代价）**（grill-me 原文）：
    > "**An assumption held silently is indistinguishable from a guess.** Each one gets a line: what was assumed, the default taken, and what it costs if it is wrong."
    （brainstorming 的同类机制 = builder-check：派一个"本领域的优秀建造者"子代理读设计文档，列出"还需要问什么"，问题经筛选后带回用户，一轮为止。）

### 4.3 视觉/设计场景的特殊协议（文字问不到位的，用"看得见的东西"）

13. **三方向硬门**（huashu-design，适用于任何"会产出新视觉"的任务；**指定风格也不豁免**）：
    > "任何会产出新视觉设计的任务，无一例外……做任何设计前，必须先提供三个差异化方向（含真实初稿）给用户选择，用户选定后才进入执行。"
    > 原因（实锤复盘）："『Apple 风格』是一个语境不是一个设计：深空暗场、大白底衬线、产品色沉浸都是合法诠释，选哪个是用户的权利。**风格词收窄解释空间，不转移选择权。**"
14. **选择无效铁律**（huashu-design 原文）：
    > "**绝不让用户在「只有文字、没看到视觉」时选风格——用户没依据。** 所以不抛文字单选题，而是并行启动 3 个 subagent 同时跑三套互补逻辑，各产出一版真实视觉，一次性摆出来让用户选「看得见的东西」。"
    （对比：oil-ui 更省成本的两步法——**"先用文字问一次，再决定做几个"**：先把 3 个方向各写三四行让用户选，"用户从文字里定得下来，就只做选中的那一个"；想看画面再做成对比页。两种取舍：huashu = 保真但贵；oil-ui = 省但接受"文字选择"的置信度。）
15. **展示后必须停**（huashu-design 原文）：
    > "三方向摆出来后**结束回合等用户选择**，不得自行选定继续执行——包括 autonomous / 无人值守会话（这是真正只有用户能做的决策，停轮不算阻塞）。"
16. **拒绝回答 ≠ 跳过门**（huashu-design 原文）：
    > "拒答问题≠跳过三方向：问题可以不问（自己补assumption），方向门照走——直接出三版初稿摆给用户选。"
    > 以及无应答策略："若用户没回应任何信息……按 best judgment 补齐假设（标 assumption），直接往下跑完 Phase 2-4 把三版真实视觉摆出来——**用「看得见的东西」代替继续追问**。"
17. **假设即选项**（Waza ui 原文）：
    > "**Two labeled candidates beat one landed guess**, because the reply is a single letter instead of a rewrite round."
    （"Offer without being asked when the decision is taste, not correctness: icon, weight, accent, motion feel."）
18. **superpowers 自己的对应机制 = Visual Companion（浏览器标签页）**：当"看到比读到更清楚"时才提供——「**Offer it just-in-time.** Offer it the first time one of the moments above comes up, **never upfront.**」提供语原文：「"This might be easier if I show you. Want me to open a browser tab with some mockups?"」用途：mockups 反应、并排选项、可点击的 throwaway prototypes；纯文字/概念问题留在终端（"A question *about* a UI topic is not automatically a visual question."）。实现 = 本地 server 监听目录、新 HTML 即推送到浏览器、用户点选写回 events（原文见 [visual-companion.md](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/visual-companion.md)，留档 `refs/superpowers/visual-companion.md`）。

### 4.4 反模式（原文点名，设计 skill 时直接抄进 Red Flags）

- **审问**："Interrogation: a checklist of questions read at the human."（rebuild spec anti-goals）
- **菜单诱导**："Garden-pathing: steering the human into the agent's preferred idea with leading menus."
- **让用户替 agent 思考**："'What are you actually trying to do?' style questions that ask the human to do the agent's thinking."
- **小需求膨胀**："Small asks inflating into multi-phase projects."
- **没批准就建造**："Building before the human agrees with the playback."
- **静默决策**（huashu）：「异常时**先告诉用户发生了什么**（1句话），再按表处理。**不要静默决策。**」
- **代理自作主张**（superpowers red flags 表）："I'll offer options to save them effort" → "Options steer. Ask them to describe it first."；"They said 'sounds good' to the idea" → "Approval covers what you showed them. A description you haven't written isn't approved."

### 4.5 停止/批准规则（三层设计）

1. **HARD-GATE（brainstorming）**："Nothing gets built until your human partner approves the full description: in chat for a small change, the document for a project." 批准覆盖范围 = 实际展示过的阶段，不许"一次批准跳全程"。
2. **Gate 文件物化（huashu）**：关键检查点落成项目目录里必须存在的文件（`direction-approved.md` 记「用户选择原话」；`brand-spec.md`；`导演稿`）——"文件不在=环节没做，任何模型都能自查，hook 也能硬拦"；"**「用户说继续」授权的是进入下一步，不是跳过该步内部的 gate**"。
3. **批准语言的最小集**（Waza think）：用户说 "Implement the plan / 可以干 / 直接改 / 按你说的来 / 不用确认" 即视为授权执行、不再重复要批准；但"提交、发布等动作仍需其对应授权"。

---

## 5. ④ 对 Designers_Brain skill 的可复用结论

> 结合本项目现状：无 git 仓库；已有 `research/prompts/artist_modules/`（11 张模块卡 + README + 校验器）、`templates/style_card.md v0.3`、`research/agent-art/transfer_guide.md`、E1-E2 实验链（含 `_verify` 脚本）、LOOP/GOALS 体系与跨家派发通道（scout/worker）。「设计顾问 skill」= 在**新实验设计 / 新组合 / 新模板 / 新产出**前，先向 Owner 问清意图、给得出可验证方案的那个 skill。

### 5.1 文件布局建议

**建议一（先简单）**：单文件起步——`skills/designers-brain/SKILL.md`（与 SkillSpec 线草案命名对齐；名称须与目录同名——官方硬规则），<500 行；超过再拆。符合官方「Start simple / 超限再拆 references」与 Waza「八个小 skill、每 skill 一个职责」的教训（"too many skills, too much configuration" 是反例）。

**建议二（拆分后的目标布局）**：

```
skills/designers-brain/
├── SKILL.md                  # 主流程：分级 → 提问 → 回放 → 方案 → 批准 → 交接（<500 行）
├── references/
│   ├── question-bank.md      # 提问库（§4.2 十二式 + 项目专用问法：画家/媒介/强度/验收）
│   ├── direction-protocol.md # 视觉选择协议（三方向门 / 对比页生成 / gate 文件格式）
│   ├── modules-index.md      # 指到 research/prompts/artist_modules/README.md 的用法索引
│   └── house-style.md        # 术语表（模块卡/视觉指纹/组合/强度）+ 措辞（"你的人类伙伴"式）
└── scripts/
    └── build-comparison.mjs  # 可选：把 2-3 个候选 HTML 截图拼成对比页（复用项目 puppeteer）
```

**要点**：
- `name`：`designers-brain`（小写连字符、与目录同名——官方硬规则；与 SkillSpec 草案一致）；
- 目录位置：项目内（`skills/` 或 `research/skill/`）；将来若要给本机 harness 用，按本机惯例 junction 到 `~/.agents/skills/` 真身 + 各 harness 链接（见 §3.4 本机实测）；
- 本项目**不需要** bootstrap hook（skill 是项目自用）；若要装进本机 Claude Code/Codex，再考虑 plugin 化（polyglot 清单，见 §3.5）。

### 5.2 引用方式（skill 怎么引用项目已有资产）

1. **一层深原则**：SKILL.md 直接链到 `references/*.md`；`references/modules-index.md` 再指向项目路径——**不许链中链**（官方："Keep file references one level deep"，深链会让 agent 用 `head -100` 只读一半）。
2. **禁止 `@` 强加载**（writing-skills 原文理由：@ = 立即 force-load，烧 200k+ context）；用相对路径 + 显式要求标记：`**REQUIRED**: 先读 research/prompts/artist_modules/README.md`。
3. **不复制易腐内容**：模块卡/模板/迁移指南留在原位，skill 只写「何时读哪个」+「怎么用」；引用上游时留**同步基线**（照 zh 的 `upstream-sync.json` 模式：记来源 commit/version/date，改动可对账）。
4. **脚本经解释器调用**（`python scripts/x.py` 而非裸路径），与项目现有 `python _verify_t1b.py` 习惯一致。
5. **description 只写触发条件**（不总结流程）：建议双语关键词——「设计顾问 / 问一下需求 / 组合实验 / 挑模块 / 新实验设计 / 新模板 / 动笔前 / before building / design consult」+ 症状词（"组合怎么选""强度多少""这版为什么不对"）。

### 5.3 交互协议建议（Designers_Brain 版「设计顾问」对话流程 v0）

结合 brainstorming（骨架）+ huashu（视觉门）+ Waza/grill-me（infer-first + assumption 留档）+ 项目 gate 文化：

```
0) 分级（先说出口，允许 Owner 覆盖）
   - 快速任务（如"跑一张 E 系列实验图"）→ 直接做 + 一句话说明假设
   - 小改动（单文件/单卡调整）→ 对话内给简短方案，点头即做
   - 项目级（新系列/新组合矩阵/新模板/新 skill）→ 走完整流程
1) 先自检 + 先读再问
   - 已知的：PROJECT/GOALS/相关实验 RESULTS/模块卡现状 → 不重复问
   - 缺的且「答案会改变产出」的才问；其余 infer-first（最多两个子问题，或一轮 ≤7 问）
2) 提问（一次一问优先；具体锚定）
   - 描述优先："上一次你做 E2 组合实验时，哪一格让你觉得'对，就是这个'？"
   - 先猜后纠："我猜这次要的是 70/30 融合的第三个对照，对吗？"
   - 验收前置："什么情况下你会说这版失败了？"
3) 回放（200-300 字）：复述意图/目标/非目标/约束，标出 guess vs 原话；
   末尾问"哪里不对或缺什么"
4) 视觉/方案选择（关键决策必须"看得见"）
   - 风格/画面类 → 生成 2-3 个真实候选（本项目已有：HTML 渲染 + E 系列出图通道）
   - 结构性方案 → 文字方向卡（各 3-4 行）先问；要看画面再做对比页（oil-ui 两步法，
     成本敏感时）；关键审美决策走"三方向门"（huashu）
   - 展示后必须停，等 Owner 选择；不得自选继续
5) 批准与留档（gate 文件化）
   - 批准前不产出（HARD-GATE）；批准覆盖"实际展示过的阶段"
   - 在实验目录留 design-brief.md：意图/非目标/约束/用户选择原话/假设清单
     （每假设 = 内容 + 默认 + 错了的代价）
   - Owner 拒答 → 不枯等：补齐 assumption 标注，继续到"可展示"再停
6) 交接：产出物 + 验证方式（沿用项目 _verify 脚本文化）+ 回放式收尾
```

**措辞纪律**（从 superpowers 抄）：plain language、match their vocabulary、不用 process jargon；"你的人类伙伴"式第二人称；每次报告先给最重要发现。

### 5.4 可迁移的工程机制清单（按优先级）

| 机制 | 来源 | 落地动作 |
|---|---|---|
| description = 触发条件（不总结流程） | writing-skills | 写 skill 时执行；加中英症状词 |
| 三层渐进披露 + 一层深引用 | 官方规范 | 模块卡等大内容不进 SKILL.md 正文 |
| 1% 规则 + Red Flags 表 | using-superpowers | skill 内写"先检查再动笔"的红线表 |
| 200-300 字回放 + "哪里不对" | brainstorming | 写进交互协议 |
| 三方向门 + 选择无效铁律 + 展示后停 | huashu | 视觉决策的硬门 + gate 文件 |
| infer-first + assumption 留档 | Waza / grill-me | 提问上限 + brief 假设清单 |
| HARD-GATE 批准范围 | brainstorming | 批准不越级、不跳步 |
| 压力场景测试（RED-GREEN-REFACTOR） | writing-skills | 用本项目的 scout/worker 跑对抗测试 |
| 上游同步基线 | superpowers-zh | 若引用上游文案，记 commit 对账 |
| polyglot 清单 / 市场分发 | superpowers / Codex | 仅在需要对外分发时启用 |

### 5.5 落地清单（下一步可做）

- [ ] 与 SkillSpec 线合并：`skill_ecosystem.md`（本文）§2-4 → spec 的格式/机制节；§5 → 建议节。
- [ ] 产出 v0.1 单文件 `SKILL.md`（含 §5.3 流程 + §4.2 问法子集）。
- [ ] 用本项目真实场景跑一次"压力测试"（例：让一个 scout 在无 skill 时直接开工 vs 有 skill 时先问），按 writing-skills 的 RED-GREEN 方法记录。
- [ ] 建立 `design-brief.md` 模板（gate 文件），并入 templates/。
- [ ] 视觉选择协议：复用 puppeteer 缓存写 `build-comparison.mjs` 原型（2-3 候选截图拼页）。

---

## 6. ⑤ 参考链接清单

### 6.1 主要链接

**superpowers 体系**
- https://github.com/obra/superpowers （本体，v7.0.0；skills/ 15 个核心 skill）
- https://github.com/obra/superpowers-skills （社区库）
- https://github.com/obra/superpowers-marketplace （市场清单）
- https://github.com/obra/superpowers-lab （实验技能）
- 关键文件直链：
  - `skills/brainstorming/SKILL.md` · `skills/using-superpowers/SKILL.md` · `skills/writing-skills/SKILL.md`
  - `hooks/session-start` · `hooks/hooks.json`
  - `docs/porting-to-a-new-harness.md`
  - `docs/superpowers/specs/2026-10-05-brainstorming-rebuild-design.md`

**规范与官方文档**
- https://agentskills.io/specification （格式规范）
- https://agentskills.io/client-implementation/adding-skills-support （加载机制）
- https://code.claude.com/docs/en/plugins-reference （Claude Code 插件清单）
- https://github.com/openai/plugins （Codex 官方插件仓库；`.agents/skills/plugin-creator/references/plugin-json-spec.md`）
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview （Anthropic skills 概览）

**同族参照**
- https://github.com/jnMetaCode/superpowers-zh （中文 fork）
- https://github.com/tw93/Waza （工程习惯 skill 包）
- https://github.com/alchaincyf/huashu-design （设计 skill）
- https://github.com/plugin87/ux-ui-agent-skills （设计架构师 kit；grill-me）
- https://github.com/oil-oil/oil-ui （UI 方向探索）

### 6.2 refs/ 留档索引（本目录）

`spec/`（规范层）· `superpowers/`（本体关键文件 7 份）· `community/`（社区版 brainstorming）· `zh/`（中文 fork 2 份）· `waza/`（路由 + 摘录）· `design-packs/`（huashu / oil-ui / grill-me）——详见 [`refs/README.md`](refs/README.md)。

### 6.3 复现命令（示例）

```bash
# 列表与树
curl -s "https://api.github.com/repos/obra/superpowers/git/trees/main?recursive=1"
# 直读任意文件（不耗 API 配额）
curl -s "https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md"
# 官方规范 markdown 版
curl -sL "https://agentskills.io/specification.md"
```

---

## 附: 方法与局限

- **方法**：全程 GitHub API（树/元数据）+ raw.githubusercontent.com 直读；官方规范走 `agentskills.io/*.md`；未用 web_search（当日限流，与项目环境实测一致）。
- **局限**：★ 数与版本为 2026-10-15 快照；brainstorming 重写（2026-10-05）「Ship something small and sharp」——作者预期按真实使用继续调优，后续版本可能再变（复读 URL 即可刷新）。
- **交叉**：本机加载路径/ junction 惯例为同项目 SkillSpec 工人实测（2026-10-15），与官方文档互为印证。
- **许可**：各参照项目均为 MIT（除另行标注）；本报告引用仅作研究留档。
- **证据分级**（按项目惯例）：本报告所有引文均为原文直读（URL/refs 可复验，属 [自述]/[史料] 层）；综合与建议部分为 [研究]/[归纳]，标于各节标题；未在本机跑过的机制（如未激活的 harness 安装）未作断言。
