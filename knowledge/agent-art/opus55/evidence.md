# 证据卷：Claude Code · Opus 5.5 作为代码作画引擎

采集日期：2026-10-15。方法：直接抓取来源页（`read`）＋ 少量 web_search；X/Twitter 拒绝自动化访问（`x-unavailable`），凡 X 帖一律标注「转引」。星标数为 2026-10-15 抓取 GitHub 页面所见，会漂移。
证据分级：`[史料]`＝公开一手来源（带 URL）；`[归纳]`＝我们跨来源总结；`[推测]`＝推断，未验证。每条 VERIFIED 项都带 URL；INFERENCE 集中放 §5。

## 1. 模型与平台公开事实（VERIFIED，[史料]）

1. **发布**：Claude Opus 5.5 于 2026-09-22 发布，$4/$20 per MTok，缓存读 $0.20（比 Opus 5 降 60%），输出速度 +30%+。1M 上下文、128K 最大输出、adaptive thinking 常开不可关、默认 effort `medium`、知识截止 2026-06。
   - https://www.anthropic.com/claude-opus-5-5
   - https://platform.claude.com/docs/en/models/opus-5-5/overview
2. **官方对视觉/创作相关能力的表述**（发布文）：某测试者让多个模型「单提示词做游戏」，Opus 5.5 因画面与完成度得分为所有模型最高；Column 公司评价「delegates to subagents far more effectively and **checks its own work in creative ways. Self-verification loops feel easier to set up**」。
   - https://www.anthropic.com/claude-opus-5-5
3. **视觉输入**（官方 prompting 指南）：读密集图表/示意图/截图比 Opus 5 准得多（最低 effort 读图表胜过 Opus 5 最高 effort）；对「位置承载含义」（流程图中箭头连接哪两个框、两版图的差异、日历截图里的起止时间）更可靠；密集输入仍建议给 agent 配图像工具（裁剪/放大/测量）自验。
   - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
4. **「反约束」有官方依据**：同一指南 §Frontend design defaults——不给定设计方向时模型会落到几种默认风格；泛泛说「避免 AI 味」只会换一种默认，**「It responds well to instructions that name specific patterns to avoid」**（点名具体要避免的样式才有效）。
   - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
5. **创作工具连接器**（2026-04-28, Claude for Creative Work）：Blender / Ableton / Adobe / Autodesk Fusion / SketchUp / Resolume 等连接器；文中明说「Claude Code can write scripts, plugins, and generative systems… build a custom shader, script a procedural animation, or generate parametric models」；与 RISD（Art and Computation）、Ringling、Goldsmiths 计算艺术项目合作。
   - https://www.anthropic.com/news/claude-for-creative-work
6. **Blender 官方通道**：Blender 开发者做的 MCP 连接器（Blender 5.1+，add-on + MCP server；LLM 生成代码无护栏执行，官方建议虚拟机）。Claude Academy 有官方教程（Claude Desktop 连接器目录直接装）。示例用例：场景命名清理、读懂 Geometry Nodes、按屏占比找多边形热点。
   - https://www.blender.org/lab/mcp-server/
   - https://academy.claude.com/tutorials/using-the-blender-connector-in-claude
   - https://projects.blender.org/lab/blender_mcp
7. **Claude Motion**（Anthropic 一方功能，2026-10-08 beta，Team/Enterprise）：把想法/季报变成 30 秒解释动画；**「Claude writes code that animates your text, charts, shapes, and images」，「It doesn't use a video generation model」**，可改字/数/时序，导出 MP4。
   - https://claude.com/resources/articles/dashboards-and-motion

## 2. 「代码生成动画」生态（VERIFIED，[史料]；星标 2026-10-15）

1. **yihui-dev/awesome-opus5-5-videos**：5.1k★、528 fork、MIT。703 条提示词（`prompts/`＋`data/videos.json`），418 条在 Skillry 有在线复刻；分类：Motion graphics 58 / Explainers 16 / 3D scenes 14 / Games 12；每条链接原作者 X 帖与提示词原文；最近更新 2026-10-12。
   - https://github.com/yihui-dev/awesome-opus5-5-videos
   - https://skillry.dev/ai-videos/opus-5-5
2. **lemomo-ai/lemo-opuscar**：2.4k★、251 fork、MIT。43 种影片风格，每种＝一个 `STYLE.md` 提示词＋一支纯代码样片；旗舰片 **OPUSCAR 98**（98 届奥斯卡最佳影片各按适配风格重画，6:31，「Every frame, every note and every cut was written in code by Claude Opus 5.5」；98 风格中 77 2D / 4 2.5D / 17 3D）。作者注：「styles are tuned for Opus 5.5; other models may not reproduce them」。工作方式：`DIRECTOR.md`（导演：故事/声音/节奏/镜头/表演/**self-checks**）＋`TECHNIQUE.md`（逐帧渲染/配音/配乐/混音）＋`styles/<name>/STYLE.md`。
   - https://github.com/lemomo-ai/lemo-opuscar
   - https://lemomo-ai.github.io/lemo-opuscar/
3. **pdoom-video**：单曲《I'm Upping My P(doom)》的代码渲染 MV，Claude Opus 5.5 在 Claude Code 里全程产出。主仓 mexicat/pdoom-video 2.8k★；JohnHeibel/PDoomVideo 2.1k★；衍生：anime OP 版、Grimes《We Appreciate Power》引擎复用版、中文逐词版。
   - https://github.com/mexicat/pdoom-video
   - https://github.com/JohnHeibel/PDoomVideo
   - https://github.com/lycfyi/power-video ; https://github.com/xiaoming6680/Zh-CN-pdoom-video
4. **heygen-com/hyperframes**：63.9k★、5.7k fork、Apache-2.0。「Write HTML. Render video. Built for agents.」HTML/CSS＋可 seek 动画→确定性 MP4；21 个 skills；`claude plugin marketplace add heygen-com/hyperframes`；`data-start`/`data-duration` 协议。
   - https://github.com/heygen-com/hyperframes
5. **remotion-dev/skills**：5.2k★。官方 Agent Skills（Claude Code / Codex / Kimi Code / Cursor 可用）：`/remotion-create`、`/remotion-markup`、`/remotion-render`、`/remotion-captions` 等；`npx skills add remotion-dev/skills`。
   - https://github.com/remotion-dev/skills
6. **BintzGavin/helios**：120★。程序化视频引擎（web 标准，CSS 动画可直接用）；示例即 10s/30fps 组合；README 内嵌 promo 视频注明 **「created with Opus 5.5 + Helios」**；提供 Claude Code/Codex 插件与 skills。
   - https://github.com/BintzGavin/helios
7. **iart-ai/javascript-animation-skills**：23★、MIT。「逐帧画在 JavaScript 里」的 agent skills 包（`javascript-animation`＋`soundtrack`）；**「Built and tested with Claude Opus 5.5」**；自检清单：零素材审计、A/V 同步（cut 落在拍上、无吓人音量跳变）、版面（文字不叠文字/不压物体）、逐镜静帧对分镜、2fps contact sheet 导演检视。
   - https://github.com/iart-ai/javascript-animation-skills
8. **ahujasid/mcp-for-blender**（原 blender-mcp）：30.9k★、2.8k fork、MIT。社区 Blender×LLM 连接器，一条命令装 Claude Desktop/Claude Code/Codex/Cursor 等。
   - https://github.com/ahujasid/mcp-for-blender

## 3. 提示词体系与工作流（VERIFIED，[史料]）

1. **4SAPI 综述**（2026-10-13）：称 awesome 仓两周 4,620★、整理 853 条提示词（与 §2.1 页面 703 条口径不同，见 gaps）；给出「**determinism contract**」：页面须暴露 `window.DUR`、`window.render(t)`、`window.READY`、`window.EV`；禁 `Date.now()`、`Math.random()` 须带种子、帧间不得留状态。「one timeline, five outputs」（画面/旁白/音乐/音效/字幕同一条时间线）；lemo 的 `readcheck.mjs` 检查文字停留可读时长；pdoom 用 Demucs+Whisper 做词级对齐、132.007 BPM 拍格切镜、子帧平均做运动模糊；与 MiniMax H3 类视频生成模型的分工表。
   - https://blog.4sapi.com/blog/ai-video-code-animation-tutorial
2. **roo.beehiiv「28 Claude Video Prompts」**（2026-10-06）：给出可粘贴的 **RENDER CONTRACT**（单一 HTML、暴露 `window.renderFrame(t)`、禁 requestAnimationFrame/CSS 动画/setTimeout、禁 Math.random 用种子 RNG、每次运动是 t 的纯函数、安全区/最小字号、**最后列出每个场景的起止秒**）；实测对比：CSS 动画壁钟方案 300 帧中 166 帧冻结（55%），确定性方案 300/300 帧正确（1.04 MB, 18.4s 渲染）。结论原文：「the contract fixes it. The model doesn't.」
   - https://roo.beehiiv.com/p/claude-video-prompts
3. **iArt 指南**（2026-10-14）：`draw(ctx, t)` 无状态逐帧；种子随机防闪烁；Web Audio 离线渲染配乐；「beat grid＋shot list＋event list 一份数据同时喂画面和声音」；自检＝contact sheet（每 0.5s 一帧）＋自动检查（无外载素材、文字不碰撞、cut 在拍、响度无跳变）；实测「14 of 14 cuts on the beat」「300 帧抽样无文字重叠」；六支盲测中「完整 brief」胜过「一句话」5 胜 1 平。
   - https://www.iart.ai/blog/ai-javascript-animation
4. **aiidelist「Opus 5.5 Motion Design」**（2026-10-05）：九层提示词解剖（Role/Objective/Format/Story/Art direction/Motion language…）；七阶段工作流（目标→素材→分镜→选渲染系统→**先渲代表帧逐项检查**→审时序→终渲）；栈选择：Remotion/HyperFrames/Canvas-SVG/Three.js/Blender/Manim。
   - https://aiidelist.com/blog/opus-5-5-motion-design
5. **cicadas.ai**（2026-10-10 实测页）：同一提示词给 Claude Opus/Sonnet/Haiku 各出场景 JSON，6/6 一次通过校验；Opus/Sonnet 4 支样片成片 15–20s、1080p、30fps、无音轨；Haiku 版面溢出。该页四支 MP4 即「一次回答未编辑」。
   - https://cicadas.ai/claude-motion-graphics

## 4. 与 15 卡体系的对照（[归纳]）

15 卡（`knowledge/domains/motion-graphics/origin/`，署名「Claude Code · Opus 5.5」，[自述]）＝任务头（10 秒 1920×1080@30fps＋**先 6 关键帧→再做→逐帧自查**）＋量化画风段＋内容段（含收尾文案）＋「别做成」反约束段。逐项对照：

| 15 卡 | 外部对应 |
|---|---|
| 先出 6 张关键帧 | iart「逐镜静帧对分镜/contact sheet」；aiidelist 阶段 5「先渲代表帧」；roo「先打印场景时间线」；lemo「先给 storyboard」选项 |
| 最后逐帧自查 | iart 自检包（零素材/同步/版面/导演检视）；lemo `DIRECTOR.md` self-checks＋`readcheck.mjs`；Anthropic 发布文 Column 证词「self-verification loops」 |
| 画风段＝可机械判定的量化规则 | roo/4SAPI 的 determinism contract；iart 的「纯函数＋种子随机」；卡片「30°/1-2px/16-32 色」＝可逐帧验收 |
| 「别做成」反约束 | Anthropic prompting 指南 §Frontend design defaults：泛泛负指令无效，**点名具体模式**才有效——「别做成：交叉淡化冒充形变…」正是点名式 |
| 音画同源（代码合成配乐、卡点） | iart `soundtrack`（同一时间线、cut 落拍、同步检查）；4SAPI「one timeline, five outputs」；pdoom 拍格切镜 |
| 两种渲染器（Blender/网页） | 官方 Blender MCP＋Claude 连接器；网页侧＝Canvas/SVG/Three.js/Remotion/HyperFrames 生态 |

注：**未找到**任何外部公开的「15 卡」原文或同名体系（已查：web_search 两组查询、上述各来源全文）。该具体卡组目前看是本项目独有的整理；其每个组件均有外部同构做法。

## 5. INFERENCE（推断，未验证）

- [推测] 15 卡确由「Claude Code · Opus 5.5」产出：依据仅为素材署名与视频时间（2026-10，[自述]＋转录），我们未能拿到原始会话或视频源文件（源视频本机未找到，见 docs/ARCHITECTURE.md A-13）。
- [推测] 6 关键帧前置的核心收益＝低成本早期人类检查点，与 iart/aiidelist 的「先渲代表帧」动机一致；但卡片场景（人类先看）与外部流程（agent 自查）中人类介入位置不同。
- [推测] 「逐帧自查」在能力上依赖模型读图自评（iart 明说需要 vision 模型看自己的 contact sheet；官方指南亦称读图/截图能力是 Opus 5.5 强项），故该步骤对非视觉模型会退化——待 B-07 端到端实验验证。
- [推测] 反约束段每条都在封堵一个已知模型默认退化（交叉淡化、塑料材质…），机制与官方「点名具体要避免的 pattern」一致；哪些默认在 Opus 5.5 上真实存在，未逐条实测。

## 6. 来源清单（全部 URL 汇总）

见 gallery.md 各条目；另含 §1-§3 中逐条给出的 URL。
