# autotrigger_probe — 自主触发探针记录

- 日期：2026-10-15
- 执行：omp worker（agent 名 `AutoTriggerProbe`）；模型 buddyfarm/deepseek-v4.1-flash；OS win32
- cwd：`D:/Project/Designers_Brain`
- 性质：行为记录——不生成图片、不产出设计成稿
- 探针问题：一个全新 agent（不被告知任何 skill 存在）面对设计需求时会发生什么

## 1. 技能清单实况（本 agent 系统提示）

系统提示中存在 `<skills>` 清单（§ Runtime → Skills & Rules），共 15 项。清单前原文有一句：「Matching skill → MUST read `skill://<name>` first.」。逐项原样如下（名字 + 触发语，转写自系统提示，源不可机读；自洽校验见 §4 C）：

- archify: 系统架构、工作流、时序、数据流、状态图、Mermaid、API序列、状态机时用；仅防混淆时例外
- archify-review: issue/PR 分诊评审、代码质量评估时用；无证据决策不用
- box-workflow: 查工作流程、AGENTS.md、CLAUDE.md、规矩、派发、工具时，先开 AgentRule README 再读一篇。
- cache-hygiene: Before editing config.yml/AGENTS.md/RULES.md/skills/tools, switching models, cache misses, token-cost/expensive questions.
- coordination: Before spawning subagents, dispatching, or accepting worker results.
- cross-dispatch: Owner says 派发 or AGENTS.md requires second harness; not for in-session subagents.
- debugger-review: After unpack/RE/boot/tool downloads or on debugger review/评分/进化/收尾.
- debugger-workstation: Use for binary/APK/DLL/pcap/memory dump reverse engineering; not for readable source or live hosts.
- dispatch: Owner说派发、AGENTS.md第二家harness、已授权随便派发时用；YOU ARE THE WORKER本会话做，不派。
- dispatch-brief: 交给 Claude/Codex/omp 派发，拼 -PromptFile，查 brief 缺验证/非目标/缓存；Grok 仅 Owner 点名。
- harness-audit: harness 审计、标准审计、skill 同步，动 ~/.claude/~/.codex/~/.omp 前；不授权改文件
- imitate-my-speech: 代写、起草、派活、改写不像他写的文本；正式文体勿用
- intel-lookup: 查本机事实：已装版本、harness状态、旧会话、旧测量、开口计划、已知故障、工具已知信息；重跑昂贵探针前用
- mcp-fleet-audit: 启动 harness 出现意外进程/窗口、内存异常，或改 MCP 注册前用。
- verify: 改动后、验证、证明、说完成或修好前用；无改动不用。

与「设计顾问 / designers-brain / 风格模块」相关的条目：**0 项**。

## 2. 用户消息与第一条回复

### 2.1 用户消息（原样）

> 我们是一个新开的独立咖啡馆（名字：拾光），想要一套开业宣传视觉：先出一张主视觉海报（后面可能做成 10 秒小动画发小红书）。预算一般，别太花哨，但要有记忆点。

### 2.2 我会发送的第一条回复（全文，逐字）

拾光的开业视觉，收到。我先给一个主方向，你觉得对路我们再细化；不对就推翻，成本很低。

**记忆点押在名字上**：「拾光」= 拾起光，谐音「时光」。整套视觉只讲这一件事。

- **主视觉**：一束斜光从左上切进画面，光斑落在右下角一杯咖啡上；店名「拾光」压在光里。大留白，全画只有一个动作——光进来。
- **配色**：奶油白 + 咖啡棕 + 一点暖黄，三色封顶，印刷和屏幕都不翻车。
- **字体**：思源宋体（免费可商用）打底，店名收紧字距就有手工感。
- **动画延展**：10 秒动画不换素材——让这束光慢慢扫过、画面渐暖，收在一行「把光拾进杯子里」。静态稿直接能改，素材零重做。

开工前想确认 3 件事：

1. 海报用在哪：小红书封面 / 朋友圈 / 线下张贴？尺寸和文字量差别很大。
2. 已有 logo 和主色吗？有就按你的来；没有可以从这套里顺手定一个。
3. 文案要素：开业日期、地址、活动（如开业前三天第二杯半价）——我来配 3 版标语。

我能直接产出的：① 视觉方向说明（构图 / 配色 / 字体规格）；② 可直接喂 AI 绘图工具的成稿级提示词；③ 先用 HTML/SVG 拼一版能看排版的草稿。你点哪个，我就开工。

## 3. 发现 / 加载记录

- **设计相关技能或工具：无。**
  - 技能：§1 的 15 项全为工程 / 流程 / 运维类（架构图、派发、验证、审计、逆向、文风、本机情报），无一覆盖「设计 / 视觉 / 品牌 / 海报」；无 designers-brain 或「设计顾问 / 风格模块」相关条目。
  - 工具：Tool Inventory（read / bash / edit / eval / glob / grep / task / wait / web_search / write）+ xd:// 设备（ast_edit / debug / ida）+ MCP 路由（chrome-devtools 系）中无设计类工具（无图像生成、无绘图）。
- **是否主动发现并加载任何 skill：否（未发生）。**
  - 过程：面对设计需求，先对照系统提示技能清单逐项匹配 → 0 命中 → 无任何 `skill://` 读取、无加载动作；`skills/`、`docs/skill/` 下的文件全程未打开。
  - 探针有效性备注（两层区分）：
    - ① fresh-agent 层（探针对象 = 系统提示 + 用户消息）：如上，未发现、未加载；§2.2 即该层行为。
    - ② 执行者层（本 worker = 写这份记录的人）：任务上下文已告知 `skills/designers-brain/` 存在（含 junction 状态）；为找落盘约定读过仓库根文档 AGENTS.md / docs/WORKFLOW.md；一次全仓 glob 的树状输出中出现过 `skills/designers-brain/` 与 `docs/skill/` 下的**文件名**（仅文件名，未读内容）。这些元信息未用于 §2.2，也未触发加载。
    - 因此：严格复现「不被告知任何 skill 存在」的前提，应换干净会话重跑（见 §4 D）。

## 4. 自审四段

### A 早产出

- 初版先落盘（§1–§3 + A/B + C 检查器命令，C 输出留空），随后运行检查器、把原始输出补进 C；§2.2 回复在落盘前定稿，之后未改动。

### B 反驳

1. 「技能清单共 15 项、无设计相关项」——试推翻：逐项重数 + 按 design / 设计 / 风格 / 视觉 / style / visual 扫全部 15 行。→ 计数 15、关键词 0 命中（命令与输出见 C）。判定：**CONFIRMED**（限定：源为系统提示、不可机读，此为转写自洽校验）。
2. 「未发现、未加载任何 skill」——试推翻：把 15 项触发条件逐条对照「咖啡馆开业视觉」需求 → 无一匹配；记录中无任何 `skill://` 读取。判定：**CONFIRMED**。
3. 「§2.2 回复在无 skill 辅助下产出」——试推翻：核查产出前读过的文件（仓库根目录列表、根 *.md 列表、AGENTS.md、docs/WORKFLOW.md）→ 均非 skill 内容。判定：**CONFIRMED**（限定：一次 glob 输出含相关路径的文件名，未读内容）。
4. 「本记录完全代表 fresh-agent 行为」——试推翻：执行者上下文已知 skill 存在，与「不被告知」前提冲突。判定：**WEAKENED**（对 1–3 无实质影响；严格复现需干净会话）。

### C 机械验证

检查器（落盘后原样运行）：

```bash
python -c "import re,io; t=io.open('docs/skill/tests/autotrigger_probe.md',encoding='utf-8').read(); s=t.split('## 1.')[1].split('## 2.')[0]; b=[l for l in s.splitlines() if re.match(r'^- [a-z]',l)]; print('sections:',[x for x in ('## 1.','## 2.','## 3.','### A','### B','### C','### D') if x in t]); print('skill-bullets:',len(b)); print('names:',' | '.join(l[2:].split(':')[0] for l in b)); print('kw-hits:',[l.split(':')[0] for l in b if any(k.lower() in l.lower() for k in ('design','设计','风格','视觉','style','visual'))])"
```

输出（原样粘贴）：

```text
sections: ['## 1.', '## 2.', '## 3.', '### A', '### B', '### C', '### D']
skill-bullets: 15
names: archify | archify-review | box-workflow | cache-hygiene | coordination | cross-dispatch | debugger-review | debugger-workstation | dispatch | dispatch-brief | harness-audit | imitate-my-speech | intel-lookup | mcp-fleet-audit | verify
kw-hits: []
```

### D 小结（≤14 行）

- 已确立：本 harness 注入清单 15 项、无设计类；面对该设计需求未触发任何 skill 加载；第一条回复见 §2.2（无 skill 辅助）。
- 被推翻：无（第 4 条降级为 WEAKENED）。
- 未知：designers-brain 未出现在注入清单的原因 [UNVERIFIED，未查]；~/.claude、~/.codex 侧 junction 的实际触发效果 [UNVERIFIED，未测]。
- 下一步：① 干净会话复跑本探针；② Claude Code / Codex 侧各跑一次对照；③ 如需定位清单缺失原因，转 harness-audit。
