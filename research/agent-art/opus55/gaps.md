# Gaps：未能验证 / 待补

采集 2026-10-15。已查渠道：web_search（成功 3 组查询；另 3 组因全部 provider 限流/拦截失败，见下）、直接抓取 24 个 URL（`read`）、GitHub 站内搜索页 2 次。

1. **15 卡原始出处未获直接验证**。署名「Claude Code · Opus 5.5」仅见于本项目素材与转录（[自述]）；源视频 `10cd03a4d43ec624cdbb96bbc0ec1f6d.mp4` 本机未找到（PROJECT.md A-13），无原始会话、无该视频的在线发布页。已查：对 15 卡内容特征（6 关键帧/逐帧自查/「别做成」）做检索，未找到外部同源版本；未找到任何站点转载这 15 条原文。
2. **X/Twitter 原帖无法直接读取**（平台拒绝自动化访问，`x-unavailable`）。E01（Kevin Ngo）、E02（shfred0）等帖内容均属转引（iart.ai 等），未能独立核对原帖文字、日期与视频本体。
3. **搜索 provider 大面积不可用**：Parallel/Exa/Firecrawl 限流（429），DuckDuckGo/Ecosia/Mojeek/Google 反爬拦截。成功仅 3 组查询（Opus 5.5 发布、Blender MCP、10-second MG prompts）。因此「Claude Code 更早期的生成艺术（p5.js/three.js 时代）」类实例可能漏检；本卷 gallery 以 Opus 5.5 波段为主。
4. **数字口径不一致**：4SAPI（2026-10-13）称 awesome 仓 4,620★/853 提示词；该仓页面（2026-10-15）为 5.1k★/703 提示词＋418 复刻。两口径的「提示词数」定义不同（可能含 `data/videos.json` 全量 vs README 精选），未逐文件核对。
5. **星标为瞬时值**，2026-10-15 抓取，会漂移；helios 许可证徽章（ELv2 文字 vs 元数据 Apache-2.0）两处不一致，未读 LICENSE 原文裁决。
6. **未观看/未抽帧任何成片**。所有 MP4/视频「质量」描述均转述来源方自述或评测方文字，未独立验证。
7. **lemo「styles tuned for Opus 5.5, other models may not reproduce」** 为作者声明，未做跨模型复现实验。
8. **E15/E16 为描述级**：仅见 GitHub 搜索结果页摘要，未逐条抓取仓库内容；E15 的「SVG games/Lottie/voxel」清单未核实。
9. **Claude Motion 细节未核**：未读官方帮助中心文章（support.claude.com 的 get-started 页）与定价页原文；cicadas 对其「Team/Enterprise 专属」的转述未独立复核。
10. **Opus 5.5 System Card PDF 未读**（安全评估为主，与本议题相关性低，属主动略过）。
11. **卡片自查项的可执行性未实测**：如「冲过头 5-10%、回弹约 8 帧」是否真能被逐帧机械检查，待 B-07 端到端实验（有模板 vs 无模板）。
12. **未验证**：本项目 15 卡里「网页逐帧渲染」的具体管线（捕获、ffmpeg、音效合成）与外部（iart/roo/4SAPI 所述）是否同构——外部管线已核实为独立来源，卡片方管线无原始记录（B-02 线待办）。
