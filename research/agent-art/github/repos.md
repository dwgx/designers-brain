# GitHub 猎场：代码艺术系统候选表

> 采集：2026-10-15，GitHub Search API 实测（stars / license / 最近 push 均为当日值）。原始检索记录：`_hunt.jsonl`（同目录，本次 30+ 条查询的落盘证据）。
> 排序：按优先级（可直接复用的同族系统 → 逐帧管线 → 渲染/动画库 → Blender → 数据集/API → 提示词库 → 基准与对照）。
> fit：A = 画家车道（Lane A）/ B = 代码动画车道（Lane B）/ both。
> license：GitHub API 判定（spdx）；标「无许可文件」的为 API=NONE 且 raw LICENSE 探测（5–7 个常见路径）均未命中；标「实测」的为 raw 文件内容确认。
> 同族判定（B 车道关键发现）："Claude Code/Opus 5.5 skill + 纯代码逐帧 + 音画同源" 已是一个成型品类，见第 1–16 行。

| name | URL | what it gives us | license | fit | notes |
|---|---|---|---|---|---|
| Vincentwei1021/mg-styles-15 | https://github.com/Vincentwei1021/mg-styles-15 | 15 支 10 秒 MG 片：完整提示词 + 全源码 + 逐帧渲染器 harness/render.mjs（headless Chrome→ffmpeg）+ 合成音轨 lib/audio（103 采样）+ 评审 rubric.md + 四段模板 template.md | MIT | B | 866★/139 fork；与本项目 15 卡同族（15 风格×10 秒×纯代码×音画同源）[推测同源，待 B-06 核]；AI 评审两轮 7.57–8.21/10；字体未随库发布 |
| lemomo-ai/lemo-opuscar | https://github.com/lemomo-ai/lemo-opuscar | 43 种影片风格 skill：每风格=风格提示词+纯代码样片（Opus 5.5 制作）+导演/技术指南 | MIT | B | 2387★；"风格=提示词+样片+指南"三层打包形态可直接对照 |
| yihui-dev/awesome-opus5-5-videos | https://github.com/yihui-dev/awesome-opus5-5-videos | Opus 5.5 病毒视频+背后提示词集（持续更新，含 live remake 对照） | MIT | B | 5088★；提示词蒸馏对照集 |
| joeseesun/opus-video-prompts | https://github.com/joeseesun/opus-video-prompts | 54 个 Opus 5.5 代码视频案例 + 可复制提示词（中文） | 无许可文件 | B | 348★；无 license，只读不搬 |
| klsoen/opus-js-animations | https://github.com/klsoen/opus-js-animations | brief→声音（文件/YouTube/生成/AI 配音）→导演稿→frame-exact MP4 的 Claude Code skill+plugin | MIT | B | 23★；Opus 5.5 直证素材（B-06 证据链） |
| cth9191/animate | https://github.com/cth9191/animate | 单文件 canvas 短片 skill：故事/外观/storyboard check-ins、7 内置风格、beat-mapped 音乐、真实产品截图 | MIT | B | 710★；check-in 机制≈"先出 6 关键帧" |
| marcelo-earth/generative-manim | https://github.com/marcelo-earth/generative-manim | LLM 写 manim 代码生成视频（GPT for video generation），含 benchmark/mcp 子库 | Apache-2.0 | B | 933★；原 digiplay/generative-manim 迁移至此 |
| HarleyCoops/Math-To-Manim | https://github.com/HarleyCoops/Math-To-Manim | 文本/图片→manim 动画与讲义 | MIT | B | 2772★；prompt→动画代码的另一种实现 |
| buildwithhanif/claude-animation-skill | https://github.com/buildwithhanif/claude-animation-skill | 手绘 2D 动画 skill：detail bible、蚂蚁 rig、笔刷/水彩笔、帧匹配复刻、合成音；Node canvas+ffmpeg | MIT | B | 38★；手绘风格段实现参考 |
| EGSECDA/vocaloid-style-mv-pipeline | https://github.com/EGSECDA/vocaloid-style-mv-pipeline | 手书 MV 流水线：确定性 Canvas2D/WebGL2 引擎+歌词动效+Blender toon 3D+headless 渲染 16:9/9:16 | MIT | B | 136★；确定性引擎+Blender 混合路线 |
| chuspeeism/dashi-animationstyle | https://github.com/chuspeeism/dashi-animationstyle | 中文口播→7 画风讲解动画 skill（HTML/Canvas 逐帧，不用生图模型） | NOASSERTION | B | 64★；中文场景同构 |
| beriki770-ship-it/code-animations | https://github.com/beriki770-ship-it/code-animations | 程序逐帧画（Canvas 2D+Web Audio）→headless MP4，16:9/9:16/4:5 skill | MIT | B | 5★ |
| JakeB-5/motion-graphic-skill | https://github.com/JakeB-5/motion-graphic-skill | 卡点单文件 canvas MG（HTML）+合成音+移动端播放器+自动验证 skill | MIT | B | 5★；"自动验证"对应自查段 |
| JohnHeibel/PDoomVideo | https://github.com/JohnHeibel/PDoomVideo | 一支 Opus 5.5 音乐视频全部源码 | 无许可文件 | B | 2112★；成品级样例 |
| dgreenheck/tidewater | https://github.com/dgreenheck/tidewater | Opus 5.5 用代码建的 3D 海滨小镇（three.js 场景） | MIT | B | 1279★；3D 场景代码参考 |
| asgeirtj/system_prompts_leaks | https://github.com/asgeirtj/system_prompts_leaks | 已记录系统提示词：Claude Opus 5.5 / Claude Code / Claude Design 等 | CC0-1.0 | both | 69.7k★；蒸馏 agent 行为口径的素材 |
| mattdesl/canvas-sketch | https://github.com/mattdesl/canvas-sketch | 生成艺术框架：确定性帧导出+ffmpeg 集成 | MIT | B | 5309★；beta；harness 备选实现 |
| spite/ccapture.js | https://github.com/spite/ccapture.js | canvas 固定帧率捕获（webm/png/tar） | MIT | B | 3775★；逐帧管线备选 |
| tungs/timecut | https://github.com/tungs/timecut | 无头捕获网页动画→视频（确定性时间轴） | BSD-3-Clause | B | 654★；2023 后未更新 |
| puppeteer/puppeteer | https://github.com/puppeteer/puppeteer | 无头 Chrome 控制（截帧/截图底座） | Apache-2.0 | B | 95.7k★ |
| prasanaworld/puppeteer-screen-recorder | https://github.com/prasanaworld/puppeteer-screen-recorder | Puppeteer 录屏插件（ffmpeg 直录） | MIT | B | 457★ |
| processing/p5.js | https://github.com/processing/p5.js | 最主流 creative coding 库（canvas/WebGL 双渲染器） | LGPL-2.1 | B | 24.1k★ |
| mrdoob/three.js | https://github.com/mrdoob/three.js | WebGL 3D 渲染底座 | MIT | B | 116.4k★ |
| patriciogonzalezvivo/thebookofshaders | https://github.com/patriciogonzalezvivo/thebookofshaders | GLSL 系统教程（噪声/图案/材质） | 自定义版权声明（NOASSERTION） | B | 7048★；用前读其许可页 |
| aferriss/p5jsShaderExamples | https://github.com/aferriss/p5jsShaderExamples | p5.js+GLSL 注释示例集 | MIT | B | 898★ |
| mmmerl/shader-doodle | https://github.com/mmmerl/shader-doodle | 写 shader 的 web component | MIT | B | 588★；原 halvves 迁移 |
| shader-park/shader-park-core | https://github.com/shader-park/shader-park-core | JS→GLSL 实时 2D/3D shader | MIT | B | 827★ |
| ojack/hydra | https://github.com/ojack/hydra | 浏览器 live coding 视觉合成（帧缓冲链式操作） | AGPL-3.0 | B | 279★；AGPL 注意；引擎在 hydra-synth |
| CedricGuillemet/SDF | https://github.com/CedricGuillemet/SDF | SDF/raymarching 资源+shadertoy 链接集 | MIT | B | 793★ |
| Tonejs/Tone.js | https://github.com/Tonejs/Tone.js | Web Audio 音乐合成框架（音画同源的音频层） | MIT | B | 14.8k★ |
| juliangarnier/anime | https://github.com/juliangarnier/anime | JS 补间/时间轴引擎（缓动曲线库） | MIT | B | 73.6k★ |
| motion-canvas/motion-canvas | https://github.com/motion-canvas/motion-canvas | 代码驱动动画（TS，场景/时间轴/导出） | MIT | B | 19.3k★ |
| remotion-dev/remotion | https://github.com/remotion-dev/remotion | React 写视频（渲染管线成熟） | 自定义 Remotion License | B | 64.2k★；商用条款需读 |
| pixijs/pixijs | https://github.com/pixijs/pixijs | 2D WebGL 渲染引擎（滤镜/特效） | MIT | B | 48.4k★ |
| paperjs/paper.js | https://github.com/paperjs/paper.js | 矢量图形脚本（路径/布尔运算） | MIT（LICENSE.txt 实测） | B | 15.1k★ |
| svgdotjs/svg.js | https://github.com/svgdotjs/svg.js | SVG 操作/动画轻库 | MIT（LICENSE.txt 实测） | B | 11.8k★ |
| rough-stuff/rough | https://github.com/rough-stuff/rough | 手绘/草图风格渲染（铅笔线、剖面线填充） | MIT | B | 21.3k★；手绘美学直接可用 |
| greensock/GSAP | https://github.com/greensock/GSAP | 工业级 JS 动画平台 | 无许可文件（GSAP 标准许可） | B | 29.2k★；许可需读官网 |
| openframeworks/openFrameworks | https://github.com/openframeworks/openFrameworks | C++ 创意编程工具包 | MIT（LICENSE.md 实测） | B | 10.4k★ |
| terkelg/awesome-creative-coding | https://github.com/terkelg/awesome-creative-coding | 创意编程资源大全（猎场入口） | 无许可文件 | B | 15.4k★ |
| spite/genuary-2026 | https://github.com/spite/genuary-2026 | GENUARY 2026 每日命题（约束式创作 prompt 集） | MIT | B | 45★；prompt 挑战语料 |
| 3b1b/manim | https://github.com/3b1b/manim | 数学动画引擎（程序化动画范式） | MIT | B | 95.1k★ |
| ManimCommunity/manim | https://github.com/ManimCommunity/manim | 社区版 manim（更工程化） | MIT | B | 41.5k★ |
| ahujasid/mcp-for-blender | https://github.com/ahujasid/mcp-for-blender | LLM 经 MCP 控制 Blender（原 ahujasid/blender-mcp） | MIT | B | 30.9k★；社区插件非官方（README 自述） |
| DLR-RM/BlenderProc | https://github.com/DLR-RM/BlenderProc | 程序化 Blender 渲染管线（无头/批渲染） | GPL-3.0 | B | 3746★ |
| carson-katri/dream-textures | https://github.com/carson-katri/dream-textures | Blender 内置 Stable Diffusion（贴图/纹理生成） | GPL-3.0 | both | 8219★ |
| nortikin/sverchok | https://github.com/nortikin/sverchok | Blender 节点式参数化建模 | GPL-3.0 | B | 2531★ |
| blender/blender | https://github.com/blender/blender | Blender 官方镜像（bpy API 参考源） | GPL（COPYING 实测） | B | 20.9k★ |
| metmuseum/openaccess | https://github.com/metmuseum/openaccess | 大都会博物馆开放数据（CC0 图像+元数据） | CC0-1.0 | A | 1440★ |
| MuseumofModernArt/collection | https://github.com/MuseumofModernArt/collection | MoMA 馆藏数据（毕加索/马蒂斯等） | CC0-1.0 | A | 1557★ |
| art-institute-of-chicago/data-aggregator | https://github.com/art-institute-of-chicago/data-aggregator | AIC 公共 API 后端；API 实测在线 133,169 件（2026-10-15） | AGPL-3.0 | A | 96★；数据条款按馆方公开域 |
| Rijksmuseum/rijksmuseum.github.io | https://github.com/Rijksmuseum/rijksmuseum.github.io | 荷兰国立博物馆 API 文档 | 无许可文件 | A | 55★；API 需 key |
| harvardartmuseums/api-docs | https://github.com/harvardartmuseums/api-docs | 哈佛艺术博物馆 API 文档 | 无许可文件 | A | 423★；API 需 key |
| asahi417/wikiart-image-dataset | https://github.com/asahi417/wikiart-image-dataset | WikiArt 爬虫/处理库（绘画图像语料渠道） | 无许可文件 | A | 62★ |
| bhargavvader/WikiArtVectors | https://github.com/bhargavvader/WikiArtVectors | 风格/艺术家向量数据集（画风度量） | 无许可文件 | A | 3★ |
| me9hanics/PainterPalette | https://github.com/me9hanics/PainterPalette | 历史画家调色板数据集 | MIT | A | 15★ |
| huggan/wikiart (HF) | https://huggingface.co/datasets/huggan/wikiart | WikiArt 数据集镜像（未 gated，可直取） | 见数据集卡 | A | 非 GitHub；2023-03 最后修改（实测在线） |
| willwulfken/MidJourney-Styles-and-Keywords-Reference | https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference | 图像模型风格词/艺术家词参考大全 | 无许可文件 | A | 12.3k★；风格词表可作画家模块对照 |
| pharmapsychotic/clip-interrogator | https://github.com/pharmapsychotic/clip-interrogator | 图像→提示词（BLIP+CLIP） | MIT | A | 2984★；反向提取画风词 |
| lumenastrum/clio-style-preview | https://github.com/lumenastrum/clio-style-preview | 414 条艺术风格 prompt（ComfyUI 节点+实时预览） | MIT（LICENSE 实测） | A | 178★ |
| Leonxlnx/taste-skill | https://github.com/Leonxlnx/taste-skill | 给 coding agent"品味"的 skill：艺术指导/参考图/浏览器检查 | MIT | both | 96.7k★（API 实测值）；"agent 审美"直接相关 |
| joanrod/star-vector | https://github.com/joanrod/star-vector | SVG 生成基础模型（位图→矢量） | Apache-2.0 | both | 4621★ |
| ZJU-REAL/SVGenius | https://github.com/ZJU-REAL/SVGenius | LLM 的 SVG 理解/编辑/生成基准（ACM MM 2025） | Apache-2.0 | B | 80★ |
| johnbean393/SVGBench | https://github.com/johnbean393/SVGBench | LLM SVG 基准（知识/编码/物理推理） | 无许可文件 | B | 81★ |
| simonw/pelican-bicycle | https://github.com/simonw/pelican-bicycle | "骑自行车的鹈鹕"LLM SVG 基准现象 | 无许可文件 | both | 210★；验收协议参考 |
| nerdyrodent/VQGAN-CLIP | https://github.com/nerdyrodent/VQGAN-CLIP | 经典 AI 艺术系统（VQGAN+CLIP 本地跑） | MIT（LICENSE 实测） | A | 2645★；历史参照 |
| fogleman/primitive | https://github.com/fogleman/primitive | 图像→几何图元重构（形状分解工具） | MIT | A | 13.5k★；构图/色块分析工具 |
| facebookresearch/AnimatedDrawings | https://github.com/facebookresearch/AnimatedDrawings | 让儿童画动起来（姿态迁移） | MIT | B | 12.8k★；"动画化他人画作"的参照 |
| guoyww/AnimateDiff | https://github.com/guoyww/AnimateDiff | 视频扩散模型（15 卡明确避开的路线，作对照） | Apache-2.0 | B | 12.3k★ |
