# Gallery：Claude / Claude Code 生成动画与生成艺术的外部公开实例

计数口径：每个条目以 `### E<n>.` 开头；`grep -c "^### " gallery.md` 即条目数。采集 2026-10-15；星标为该日 GitHub 页面所见。X 帖因平台拒绝自动化访问，标注「转引」并给出转引来源。

### E01. Kevin Ngo —「Claude Opus 5.5 drew every frame of this animation in JavaScript」
现象级起点的短视频：无图片素材、无视频模型，整片由程序在 canvas 上逐帧画出。转引（iart.ai 明确以其帖为引；X 原文未能直接抓取）：
- 原帖：https://x.com/kevin_t_ngo/status/2102437977435893771
- 转引：https://www.iart.ai/blog/ai-javascript-animation

### E02. @shfred0 — 水墨/木刻风动画
iart 指南收录其墨色动画并注明「Inspired by」；同风格提示词与成片对照展示。转引：
- 原帖：https://x.com/shfred0/status/2102495989194236158
- 转引：https://www.iart.ai/blog/ai-javascript-animation

### E03. iart-ai/javascript-animation-skills —「I only asked you to fix one line」等纯代码影片
一个 81 KB HTML 文件＝整支 30 秒片（无图片/无字体文件，全部音符与音效由 Web Audio 合成）；另有 42 秒《What a newborn sees》；gallery 里三支片各由全新 agent 从一行请求产出（喜剧/睡前故事/理财解释）。MIT。
- https://github.com/iart-ai/javascript-animation-skills

### E04. yihui-dev/awesome-opus5-5-videos — 703 条提示词＋418 支在线复刻
目前最大的 Opus 5.5 视频作品库：每条含原作者 X 帖＋提示词原文；分类 Motion graphics 58 / Explainers 16 / 3D scenes 14 / Games 12；可在 Skillry 与原片并排对照复刻。5.1k★。
- https://github.com/yihui-dev/awesome-opus5-5-videos
- https://skillry.dev/ai-videos/opus-5-5

### E05. lemo-opuscar — 43 风格短片＋《OPUSCAR 98》长片
98 届奥斯卡最佳影片逐届重画成 6:31 长片，全片逐帧代码绘制；每风格带可复用 STYLE.md＋成片＋镜头说明；含在线 gallery 与 1080p 下载。2.4k★。
- https://github.com/lemomo-ai/lemo-opuscar
- https://lemomo-ai.github.io/lemo-opuscar/
- 1080p 片：https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/opuscar98.mp4

### E06. pdoom-video —《I'm Upping My P(doom)》代码渲染 MV
Claude Opus 5.5 在 Claude Code 中完成概念、词对齐、音频分析与渲染；1080p60 默认、4K 可选；衍生出 anime OP 版与 Grimes 曲目复用版。主仓 2.8k★（另有 2.1k★ 镜像仓）。
- https://github.com/mexicat/pdoom-video
- https://github.com/JohnHeibel/PDoomVideo
- 衍生：https://github.com/2606156052/Pdoom-video-anime-version ; https://github.com/lycfyi/power-video

### E07. heygen-com/hyperframes — HTML→确定性 MP4 框架与 showcase
Agent 向 HTML 视频框架（Apache-2.0，63.9k★）：可 seek 动画＋校验＋渲染一条龙，21 个 skills，官方 showcase 页展示成品。
- https://github.com/heygen-com/hyperframes
- https://hyperframes.heygen.com/showcase

### E08. remotion-dev/skills — Remotion 官方 Agent Skills
Claude Code/Codex/Cursor 可用的官方技能包（create/markup/render/captions/maps…），Remotion 用 `useCurrentFrame()` 把动画钉在帧上而非壁钟。5.2k★。
- https://github.com/remotion-dev/skills

### E09. BintzGavin/helios — promo 视频「created with Opus 5.5 + Helios」
web 标准程序化视频引擎（示例即 10s@30fps）；README 首屏内嵌的 2026-09-22 promo 片注明由 Opus 5.5＋Helios 产出；带 Claude Code/Codex 插件。
- https://github.com/BintzGavin/helios

### E10. Cicadas.ai showcase — 四支「一次回答、未编辑」MP4
2026-10-10 实测：同一提示词给 Claude Opus/Sonnet 出场景 JSON→页内画布渲染成 MP4；含季度财报、URL shortener、竖版 launch teaser、中文复利解释四支成片（15–20s，1080p，30fps）。
- https://cicadas.ai/claude-motion-graphics

### E11. iArt 指南附片 — 六支含 MP4 直链的样片
纸雕云朵、水墨纸船、1950s 教科书《Why is the sky blue?》、降噪耳机、种子长成树、tap-to-pay 等，均给出视频直链与完整逐秒 brief（beat/LOOK/MOTION/SOUND 分段）。
- https://www.iart.ai/blog/ai-javascript-animation
- 例：https://cdn.iart.ai/video-asset/javascript-animation/paper-cloud-storybook.mp4 ; https://cdn.iart.ai/video-asset/javascript-animation/ink-paper-boat.mp4 ; https://cdn.iart.ai/video-asset/javascript-animation/sky-blue-v2.mp4

### E12. Blender 官方 MCP ＋ Claude 连接器 — Claude 直接驱动 Blender Python
Blender 开发者提供的 MCP server＋add-on（Blender 5.1+）；官方示例含场景多边形热点分析、Geometry Nodes 自动文档（生成 frame 标注与说明文本）。Claude Academy 官方教程覆盖安装与用例。
- https://www.blender.org/lab/mcp-server/
- https://academy.claude.com/tutorials/using-the-blender-connector-in-claude
- https://projects.blender.org/lab/blender_mcp

### E13. ahujasid/mcp-for-blender — 社区 Blender×LLM 连接器
30.9k★ 的社区项目（原 blender-mcp）：一条命令接入 Claude Desktop/Claude Code/Codex/Cursor；prompt 辅助建模、场景创建与操控。
- https://github.com/ahujasid/mcp-for-blender

### E14. Claude Motion（Anthropic 一方）— 代码驱动的解释动画
2026-10-08 beta（Team/Enterprise）：由 Claude 写代码来动画化文字/图表/形状/图片，非视频生成模型，可编辑可导 MP4；官方博客含演示与迁移说明。
- https://claude.com/resources/articles/dashboards-and-motion

### E15. OpenVGLab/awesome-opus5.5-frontend-showcases — 前端展示合集
Opus 5.5 产出的 SVG 游戏与动画、Lottie、体素、Three.js/WebGL 站点合集（2026-10-15 GitHub 搜索结果页所见，描述级，未逐条抓取）。12★。
- https://github.com/OpenVGLab/awesome-opus5.5-frontend-showcases

### E16. nikemafia044-a11y/awesome-opus5-5-videos-plugin — 提示词 Claude 插件
把 yihui-dev 的提示词库打包成 Claude（app 与 Claude Code）插件并每日同步（描述级，未逐条抓取）。1★。
- https://github.com/nikemafia044-a11y/awesome-opus5-5-videos-plugin
