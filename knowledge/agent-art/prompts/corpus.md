# Prompt 语料猎场（B-04）

> 产出：`knowledge/agent-art/prompts/corpus.md`（本文件）+ `patterns.md`（共性结构提炼）。
> 猎人：PromptCorpusHunt；日期：2026-10-15。
> 口径：每条 = 原文（截断到必要长度）+ URL + 来源类型 + 一句话点评。引用保留原文语言。
> 来源类型图例：`repo`（代码仓库/文件）、`repo-index`（索引页）、`article`（文章/专题页）、`tweet-case`（推文案例页，含逐字提示词）、`tweet`（原推文）、`site`（站点页面）、`skill`（Agent Skill 文件）。
> 检索通道说明：本机 `web_search` 全 provider 限流（429/bot 挑战，2026-10-15），以下全部经 `read`(URL) / curl / GitHub API 直达取得；未取到的在 §缺口 写明已试路径。

## 0. 与本项目内部素材的关系（先看这一条）

- 内部素材 = `knowledge/domains/motion-graphics/origin/` 的 **15 张中文卡**（署名 `Claude Code · Opus 5.5`，视频 1280×720, 30fps, 2m52s）。
- 外部存在一份**风格一一对应的英文全量版**：`Vincentwei1021/mg-styles-15`（864★，MIT，署名 `Claude Opus 5.5`）。15 种风格名逐一对应（3D 质感↔3D Render、液态↔Liquid、等轴 2.5D↔Isometric、复古未来↔Synthwave/VHS、形变↔Shape Morph、包豪斯↔Bauhaus、科幻 HUD↔Cyberpunk HUD/FUI、一笔画↔Line Art、玻璃拟态↔Aurora & Glassmorphism、拼贴↔Collage、像素↔Pixel、手绘线条沸腾↔Frame-by-Frame/Line Boil、扁平矢量↔Flat Vector、贴纸科普↔Sticker Explainer、综艺花字↔Variety Captions）。
- 二者同源与否**未取得确证** [推测]（署名同为 Opus 5.5、风格集 15/15 重合；但内部卡是中文、外部 prompts 是英文+中文风格注）。**可用的结论**：外部 repo 提供 15 条提示词的**英文全文 + 全部源码 + 评审 rubric + 写新风格的模板**，与内部 15 卡可逐条对照。

---

## A 类：代码生成艺术 / 动画（MG · creative coding · shader · three.js/p5 · SVG）

### A1. mg-styles-15 · 扁平矢量动画 prompt 全文
- URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/prompts/01-flat-vector.md
- 来源类型: `repo`（每条风格一个文件；`prompts/` 下共 15 条）
- 原文（截断）:
  > "You are the director, motion designer, engineer and sound designer of ONE 10-second motion-design film. The goal is the most classic, yet most stunning form of this style — award-shortlist / high-end commercial quality. A clean, template-looking result is a fail. Benchmarks: Buck, ManvsMachine, Ordinary Folk, Giant Ant, Territory Studio, Apple keynote motion…"
  > "# Output (fixed) — 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS integrated, true peak ≤ −1 dBTP. Final file: video.mp4."
  > "# How to work — 1. Treatment … 2. Key frames before motion. Build the look, render stills at 6–10 key times and actually look at them … 5. Final … exactly 10.00 s, resolution, fps, audio present and at the right loudness … 6. Write an honest self-critique"
  > "# Rules — Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only … Assets: only CC0 / public domain / OFL … Record each source and licence in CREDITS.md."
- 点评: 与内部 15 卡同风格的外部全文版——多出「角色设定 / 输出硬规格 / 对标基准 / 自评 / CREDITS」五块，是我们四段结构的直接升级线索。

### A2. mg-styles-15 · 写新风格的模板（四段）
- URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/template.md
- 来源类型: `repo`
- 原文（截断）:
  > "每份风格提示词都由「通用部分」和「风格专属部分」组成。通用部分（开头的角色设定，以及 How to work / Rules / Craft checklist / 自评 / Deliver）所有风格都一样…… 要写一种新风格，只需要填下面四段：# Style / # Output (fixed) / # Suggested technical route / # Creative seed / # Signature features and key techniques"
  > "写好的关键：**Signature features 要可检验**。写「弹性缓动 overshoot 用 cubic-bezier(0.34,1.56,0.64,1)，错峰 2–4 帧」，而不是「动效要有弹性」。"
- 点评: 与我们 `templates/style_card.md` 同构（任务头/画风/内容/反约束），但把「通用部分」与「风格专属部分」显式拆开——换风格只填 4 段。

### A3. mg-styles-15 · 评审 rubric（让第二个 AI 当评委）
- URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/rubric.md
- 来源类型: `repo`
- 原文（截断）:
  > "You are a senior motion-design jury member … You did NOT make this film. Judge it harshly and precisely … Score 1–10 on each dimension (5 = competent student work; 6 = decent template level; 7 = solid professional; 8 = high-end agency work; 9 = award shortlist …). Most first renders deserve 5–7. Do not inflate."
  > 第二步（贴回制作会话）: "An independent jury reviewed your film … First keep a copy of the current video and source as version N. Implement every critical issue …"
- 点评: 「制作 → 独立评审 → 修改 → 再评审」的完整二轮闭环；内部 15 卡只有「最后逐帧自查」，没有换人/换会话评审这一层。

### A4. mg-styles-15 · 15 条 prompt 文件目录（索引）
- URL: https://github.com/Vincentwei1021/mg-styles-15/tree/main/prompts
- 来源类型: `repo-index`
- 原文（截断）: 目录含 `01-flat-vector.md`、`03-isometric.md`、`04-3d-render.md`、`05-cel-boil.md`、`06-collage.md`、`07-liquid.md`、`08-morph.md`、`09-bauhaus.md`、`10-synthwave.md`、`12-aurora-glass.md`、`18-hanazi.md`、`19-paperclip.md`、`20-pixel.md`、`22-hud.md`、`02-line-art.md`（15 条）
- 点评: 内部 15 卡逐条对应外部全文；本项目做「15 卡 → 泛化模板」时可把英文原文当参照系。

### A5. awesome-ai-motion · AI 动效作品语料库（821 作品 + prompts/ 目录）
- URL: https://github.com/guanmo-ai/awesome-ai-motion （索引页 https://guanmo-ai.github.io/awesome-ai-motion/）
- 来源类型: `repo-index`
- 原文（截断）:
  > "发现惊艳动效、创意视频与交互艺术，探索背后的源码、提示词与制作过程。Curated motion design, creative video & interactive art — with source code, prompts & making-of resources."
  > "汇集由 AI 编写代码绘制、渲染或驱动的动效与交互作品，包括 Blender、Three.js、Canvas 等工具制作的动画…… 公开提示词不保证相同结果，作品尚未逐条独立复现。"
  > `prompts/<推文ID>.txt` = 逐字原文；`cases/`、`browse/`（产品宣传 155 / 知识讲解 159 / 短动效 108 / 角色动画 56 / 交互演示 199 / 叙事短片 81 / 音乐与歌词 63）
- 点评: 目前找到的最大同类提示词语料池（按推文 ID 存原文、附作者与收藏数），是 B-04 的长期取数口。

### A6. @stephanlivera · 15 秒简历作品集短片（一句话 prompt，17,072 赞）
- URL: https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/2103315922098470926.txt ；原推 https://x.com/stephanlivera/status/2103315922098470926
- 来源类型: `tweet`（原文经 awesome-ai-motion 存档为 txt）
- 原文（全文，仅一句）:
  > "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out."
- 点评: 极简一句话也能出片的样本——任务句式 = 动词 + 时长 + 体裁 + 动机（"like it's your showreel"）+ 全力以赴；对照我们固定任务头看「短句式」的边界在哪。

### A7. @twoclipping · 纯代码 UI 变形动效（19,303 收藏）
- URL: https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/2103273003555402193.txt ；原推 https://x.com/twoclipping/status/2103273003555402193
- 来源类型: `tweet`
- 原文（截断）:
  > "<inputs> Ask me for: 8 to 12 UI states I want the shape to become … and a royalty-free song around 120 BPM"
  > "<direction> Dribbble-level UI motion. One shape, never cut … Banned: bouncy easing, particle bursts, glows, gradients on UI chrome, mismatched icon strokes, dead time, anything that looks like a template."
  > "<build> … Every style is computed from time inside seek(t): no CSS transitions, no timers, no state carried between frames. … Render with Playwright: 4 subframes per frame, blended with ffmpeg tmix for motion blur at 60fps. … Render one frame per beat before the full render."
  > "<gotchas> Never put will-change on anything the camera scales or the text renders blurry. … Make the last frame identical to the first, cursor position and speed included, or the loop stutters."
  > "<start> Ask me for the inputs, then show me the state list on the beat grid before you write any code."
- 点评: 结构最完整的社区 prompt：输入反问（<inputs>）→ 方向+禁列表 → 时间纯函数（seek(t)）→ 渲染管线（Playwright+tmix）→ 陷阱清单 → 先给状态表再写代码；把「关键帧先行」升级成了「先给我看分镜表」。

### A8. @akokoi1 · 线稿回顾中华五千年（中文一句话）
- URL: https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/2102583898865873225.txt ；原推 https://x.com/akokoi1/status/2102583898865873225
- 来源类型: `tweet`
- 原文（全文）:
  > "做一个动画，快速回顾中华五千年的历史。风格轻松有趣，动画格式为线稿，添加合适的音乐，请务必做到引人入胜"
- 点评: 中文一句话模板：主题 + 体裁（动画）+ 风格（线稿）+ 音乐 + 效果目标（引人入胜）；与内部 15 卡同语言族，可当「最短可用中文 prompt」基准。

### A9. @WinterArc2125 · 用代码讲奥斯特里茨战役（5:01 叙事片）
- URL: https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/2103116235009347650.txt ；原推 https://x.com/WinterArc2125/status/2103116235009347650
- 来源类型: `tweet`
- 原文（截断）:
  > "Create a 4–5 minute cinematic video about the Battle of Austerlitz (1805), built entirely in code. Research the battle thoroughly and decide for yourself how to tell the story … I want it to be historically accurate, dramatic, easy to understand, and visually exceptional. … Don't make it feel like a generic infographic or strategy game. It should feel like a cinematic historical film that happens to be rendered with code. You have complete creative control. Surprise me."
- 点评: 长片叙事型：研究要求 + 参考画作（"use the attached paintings as visual inspiration, not a strict style requirement"）+ 反退化（别像信息图/策略游戏）+ 放权（Surprise me）——「反约束 + 放权」并存的高级写法。

### A10. PromptMotion · 「15 种动效设计风格」专题页
- URL: https://promptmotion.art/zh/p/15-motion-design-styles （英文版 /p/15-motion-design-styles；来源 repo 同上 A1）
- 来源类型: `article`（案例站，逐字收录提示词）
- 原文（截断）:
  > "十五部 10 秒动效设计短片，画面、动画和声音全部来自代码。项目说明称每部都由 Claude Opus 5.5 根据一段提示词写成，提示词和源码与短片一同公开。"
  > FAQ: "提示词经过修改吗？没有。提示词逐字引自公开来源，译文会明确标注。"
- 点评: 对 mg-styles-15 的第三方索引站（含中英双语页），可作为「15 卡」外链引用与交叉核对源。

### A11. @majidmanzarpour · 施法的像素风巫师（promptmotion 收录逐字提示词）
- URL: https://promptmotion.art/zh/p/opus-pixel-art-wizard-spell
- 来源类型: `tweet-case`
- 原文（截断，页面为中文译录，原推英文）:
  > "创建一个单一的自包含 HTML 文件，用以渲染一个正在施放法术的动画像素艺术巫师，使用原生 JavaScript 和 Canvas 2D。不要外部资源、库或网络请求。"
  > "把一切绘制到固定逻辑分辨率为 128x96 的离屏画布上…… 设置 imageSmoothingEnabled = false …… 不要子像素位置、抗锯齿、渐变或 shadowBlur。"
  > "以固定的 60hz 时间步更新…… 循环内部的对象分配为零。"
  > "质量标准 —— 在任何窗口尺寸下像素都清晰、循环无缝、60fps 稳定、剪影可读。看起来应当像精致的 16-bit 精灵动画，而不是被缩小的矢量形状。"
- 点评: 像素风格的可判定规则样板（逻辑分辨率/调色板/吸附网格/固定时间步/零分配），与内部「像素」卡同族但更工程化。

### A12. @riku720720 · 彩虹赛道躲陨石的像素小人（超长逐字提示词）
- URL: https://promptmotion.art/zh/p/opus-pixel-runner-dodging-meteors
- 来源类型: `tweet-case`
- 原文（截断）:
  > "把摄像机当作逻辑坐标上的整数偏移来处理。不使用缩放或旋转，只用位置的移动和晃动来表现。"
  > "顿帧：在擦身而过的瞬间，只把整体停止 3〜4 帧，然后做约 0.3 秒的慢动作…… 震动从定好的模式数组中读出，不使用随机数。"
  > "障碍不是随机的，而是把预先定好的「攻击模式」按顺序播放，并设计成整体在固定的一段时间内循环"
  > "「快」「在最后一刻躲开」「帅气」这三件，要在每一次回避中传达出来。"
- 点评: 把「确定性」贯彻到内容层：不用随机数、攻击模式预排、循环无缝；并给情绪目标（快/擦身而过/帅气）做验收句。

### A13. @Chris_Wozniczek · Totality Engine（GLSL 大教堂短片，含全套技术禁令）
- URL: https://promptmotion.art/zh/p/totality-engine-opus55-glsl
- 来源类型: `tweet-case`
- 原文（截断）:
  > "创建一个打磨过的、视觉上令人印象深刻的、自包含的单文件 HTML/WebGL 体验，名为： totality-engine.html 放入 documents/llm-benchmarks。不要只描述这个想法。要实际生成完整可运行的 HTML 文件，并保存到当前目录。"
  > "0.0–4.0s DUST … 4.0–10.0s NAVE … 24.0–30.0s TOTALITY 日冕爆开成一圈白金色的火…… 30.0–32.0s CODA 缓入一段与第 0 帧相吻合的缓慢延续，使循环看不出来。不要硬切。"
  > "有限的调色板，锁定：湿石灰岩 #8a8680、黄铜 #c4a574、铜绿 #2f6f66、日食绯红 #6b1020、日冕 #ffe9c2、黑水 #05070c、金尘 #e6c27a。不要青色，不要品红，不要霓虹，不要彩虹，不要黑底配紫的「人工智能观感」。"
  > "只能使用设了种子的 RNG，种子常量为 0xA2E1。…… 不要 TODO 注释、伪代码、占位符、缺失的函数…… 目标是在 2023 年的笔记本电脑上达到 60fps。…… 如果 26 秒处的截图不能被读作「日食时刻一座大教堂尺度的钟」，你就还没有完成。"
- 点评: 单条最接近「完整工程规格书」的 prompt：具名节拍 + 锁定色板 + 种子常量 + 禁 TODO/伪代码 + 性能目标 + 一句可截帧验收的质量标准。

### A14. @WescheNex1q · 轨道视角星球（GLSL 片元着色器，一句话）
- URL: https://promptmotion.art/zh/p/grok-planet-fragment-shader
- 来源类型: `tweet-case`
- 原文（全文，页面译录）:
  > "一颗从轨道上看到的星球：地形、海洋、飘动的云、带城市灯光的昼夜分界线、边缘的大气层、缓慢自转、拖动可倾斜视角，还有一个「季节」按钮，可以改变冰盖。"
- 点评: 「场景清单式一句话」：把画面元素与交互逐项列出即可，说明 shader 类不必长篇——可判定性来自要素枚举。

### A15. @vikktorrrre · Three.js + WebGPU 弹性果冻
- URL: https://promptmotion.art/zh/p/fable51-webgpu-bouncy-jelly
- 来源类型: `tweet-case`
- 原文（全文，页面译录）:
  > "用 Three.js + WebGPU 做出看起来很好吃、Q 弹的果冻。"
- 点评: 短句 + 质感形容词（好吃/Q 弹）也能跑——但需模型自行补齐物理参数；与「量化代替形容词」互为反例，标注为低可控样本。

### A16. @AxtonLiu · 会呼吸的水墨画（角色设定型中文 prompt）
- URL: https://promptmotion.art/zh/p/breathing-ink-wash-painting
- 来源类型: `tweet-case`
- 原文（截断）:
  > "你是 opus 5.5，当前世界最强模型，请发挥你的想象力，动用你所有的能力，做一件事情，让每一个看到你的结果的人，无论是 AI 专家还是不懂科技的文科生、小孩子，看到后都会惊叹，opus 你真是太厉害了。你会做什么事呢？"
- 点评: 纯「角色设定 + 动机」式 prompt（无画风段/无反约束），验证了角色设定块本身的驱动力；但可控性全靠模型自觉，适合当上限实验而非模板。

### A17. @riba2534 · 鹈鹕骑自行车 3D 页面（Three.js，1,010★）
- URL: https://promptmotion.art/zh/p/pelican-on-a-bike ；源码/演示 https://github.com/riba2534/claude-opus-5-5-demo （页面注明：一次生成、超高推理强度、代码无人工改动）
- 来源类型: `tweet-case` + `repo`
- 原文（全文）:
  > "生成一个鹈鹕骑自行车的 3D 页面，尽可能把你所有的能力全部都用上. 然后上传到 CDN 上, 把访问链接给我"
- 点评: 社区把 Simon Willison 的鹈鹕基准（见 A20）扩展成了 3D/WebGL 版；「上传 CDN 给我链接」= 把交付物写进 prompt 的样例。

### A18. @Xanares · 37 秒分形技术演示
- URL: https://promptmotion.art/zh/p/fractal-demoscene-raymarcher
- 来源类型: `tweet-case`
- 原文（全文，页面译录）:
  > "去做一个你能想到的最疯狂的技术演示。"
- 点评: 极端放权样本（6 词）；与 A13 的规格书式 prompt 构成光谱两端——「放权 vs 规格」正是我们模板要显式二选一的旋钮。

### A19. @twoclipping · 卡点同步的产品宣传片（第二条模板）
- URL: https://promptmotion.art/zh/p/beat-synced-product-promo-template ；原推 https://x.com/twoclipping/status/2102554209166000267
- 来源类型: `tweet-case`
- 原文（截断，页面注明"逐字引用英文原文"）: 提示词为原文，模板 · 443 词；页面归类「模板 · 卡点同步的产品宣传片」。
- 点评: 同作者第二份可复用模板（卡点产品片）；配套 twoclipping 的 UI morph 模板（A7）可对比「输入反问 + 禁列表」在同作者两片中的复用率。

### A20. Simon Willison · 鹈鹕骑自行车基准（SVG/WebGL/Blender 三种一句话 prompt）
- URL: https://simonwillison.net/tags/pelican-riding-a-bicycle/ （150 帖标签页）
- 来源类型: `site`（博客标签页；内含各帖链接）
- 原文（截断）:
  > "My benchmark for LLMs: "Generate an SVG of a pelican riding a bicycle"."
  > "build me an HTML page that renders a three-dimensional pelican riding a bicycle using WebGL"
  > Blender 版: "Use the already install /Applications/Blender to render a scene of a pelican riding a bicycle" → "OK add a background and a lot of flair" → "OK make it a whole lot better"
- 点评: 社区最通用的「代码作画」一句话基准（SVG→3D/WebGL→Blender 全链）；证明短 prompt 的评估价值在可比性（同一句跨模型横评），不是质量上限。

### A21. Genuary 2026 · 31 条 creative coding 月更提示词
- URL: https://genuary.art/prompts
- 来源类型: `site`（每年一月的生成艺术挑战清单）
- 原文（截断，示例 3 条）:
  > "JAN. 20 — One line. An artwork that is made of a single line only."
  > "JAN. 21 — Bauhaus Poster. Create a poster design inspired by the German art school Bauhaus."
  > "JAN. 31 — GLSL day. Create an artwork using only shaders."
- 点评: 「提示词」的另一物种：不是交给模型的任务书，而是人类艺术家的创作约束题——可拿来当「同一约束下模型 vs 人」的对照组，也可给 B-07 端到端实验当题面。

### A22. Anthropic `algorithmic-art` skill（p5.js 生成艺术流程）
- URL: https://raw.githubusercontent.com/anthropics/skills/main/skills/algorithmic-art/SKILL.md
- 来源类型: `skill`（`anthropics/skills`，181k★ 的官方 Skills 仓库）
- 原文（截断）:
  > "Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. … Create original algorithmic art rather than copying existing artists' work to avoid copyright violations."
  > "Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms). This happens in two steps: 1. Algorithmic Philosophy Creation (.md file) 2. Express by creating p5.js generative art (.html + .js files)"
  > "Seeded Randomness (Art Blocks Pattern): ALWAYS use a seed for reproducibility … randomSeed(seed); noiseSeed(seed);"
  > "⚠️ STEP 0: READ THE TEMPLATE FIRST ⚠️ … Use that file as the LITERAL STARTING POINT - not just inspiration … Avoid: Creating HTML from scratch"
- 点评: 官方 skill 形态的「两阶段」流程：先写哲学宣言（.md）再写代码（.html/.js），并用模板文件锁 UI、用种子锁可复现——把「风格段」换成了「哲学段」。

### A23. Anthropic `canvas-design` skill（海报/静态视觉流程）
- URL: https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md
- 来源类型: `skill`
- 原文（截断）:
  > "Design Philosophy Creation (.md file) 2. Express by creating it on a canvas (.pdf file or .png file)"
  > "**Emphasize craftsmanship REPEATEDLY**: The philosophy MUST stress multiple times that the final work should appear as though it took countless hours to create … 'meticulously crafted,' 'the product of deep expertise' …"
  > "The user ALREADY said 'It isn't perfect enough. It must be pristine, a masterpiece of craftsmanship, as if it were about to be displayed in a museum.'"
  > "avoid adding more graphics; instead refine what has been created and make it extremely crisp"
- 点评: 值得注意的「修辞工程」：把工艺感通过重复宣言写进 prompt；最终轮要求「不加元素、只精修」——可借给我们的自查段（第二遍不许加东西）。

### A24. 歸藏（@op7418）· 游戏结算 / 抽卡动画提示词
- URL: 原推 https://x.com/op7418/status/2104085484347818226 ；转述 https://airebao.com/item/36775
- 来源类型: `tweet`（全文未取得，见缺口）
- 原文（截断，airebao 转述 + 原推开头）:
  > "归藏（guizang.ai）用 Opus 5.5 制作游戏结算动画，最初生成的是 2D SVG 图标，随后改为 3D 效果并优化光效。他还做了一个新的抽卡动画，包含宝箱和徽章两个版本。作者公开了完整提示词，可直接复用。"
  > 原推开头: "Opus 5.5 游戏动效制作提示词来了！…… 顺便还做了一个新的抽卡动画，提示词太长放下面了"
- 点评: 同作者（15 卡体系的重要传播者）的另一套「游戏 UI 动效」prompt；正文在推文线程里，本轮未逐字取到——列入缺口，值后续回捞。

---

## B 类：画家风格 prompt（达芬奇 / 米开朗基罗 / 梵高 / 莫奈 / 毕加索 / 塞尚 / 马蒂斯 / 北斋）

> Midlibrary（Andrei Kovalev 维护的 Midjourney 风格库）为每位画家给出一条**可复制的 Midjourney 模板句**：`<画家名>'s painting depicting … by <画家名> --v 6.1`（北斋为 `Hokusai's Ukiyo-e print depicting …`；米开朗基罗页只给 `by Michelangelo`）。以下 8 条同源，逐条列出。

### B1. 梵高 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/vincent-van-gogh
- 来源类型: `site`
- 原文: `Vincent van Gogh's painting depicting … by Vincent van Gogh --v 6.1`（页面另有 SREF code 与 16 条基准题横评）
- 点评: MJ 生态「画家名即风格锚」的标准写法：主句嵌 `…` 槽 + 尾缀 `by <artist>`；风格说明词为 vivid colors / expressive / fine brushstrokes / moody colors。

### B2. 莫奈 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/claude-monet
- 来源类型: `site`
- 原文: `Claude Monet's painting depicting … by Claude Monet --v 6.1`
- 点评: 同构模板，仅换画家名——说明该库把「画家风格」当作可参数化的后缀；对照我们「控制参数」节的强度档位。

### B3. 毕加索 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/pablo-picasso
- 来源类型: `site`
- 原文: `Pablo Picasso's painting depicting … by Pablo Picasso --v 6.1`
- 点评: 注意：该库不分毕加索时期（蓝色/立体主义），一个名字糊掉多时期——恰好是我们 Lane A「分时期规则」要补的缺口。

### B4. 塞尚 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/paul-cezanne
- 来源类型: `site`
- 原文: `Paul Cézanne's painting depicting … by Paul Cézanne --v 6.1`
- 点评: 与梵高页互为「相似风格」互链；可作为 MJ 侧「结构/色块」与印象派区分的观察样本。

### B5. 马蒂斯 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/henri-matisse
- 来源类型: `site`
- 原文: `Henri Matisse's painting depicting … by Henri Matisse --v 6.1`
- 点评: 同构；马蒂斯的剪纸/平面色块特征在该库靠图片横评体现，文字描述极简——文字 prompt 对「平面色块」类特征的可控性天然弱。

### B6. 北斋 · Midlibrary 模板句（变体句式）
- URL: https://midlibrary.io/styles/katsushika-hokusai
- 来源类型: `site`
- 原文: `Hokusai's Ukiyo-e print depicting … by Hokusai --v 6.1`
- 点评: 唯一换了「媒介词」的画家页（print 而非 painting）——浮世绘=版画的事实被写进句式，值得收进北斋模块的英文 prompt 段。

### B7. 米开朗基罗 · Midlibrary 模板句（页面为简式）
- URL: https://midlibrary.io/styles/michelangelo
- 来源类型: `site`
- 原文: `by Michelangelo --v 6.1`（该页未给 `… depicting` 前句；同页 SREF code 区）
- 点评: 同库少数不完整条目；说明该库质量参差，取用时需逐页核。

### B8. 达·芬奇 · Midlibrary 模板句
- URL: https://midlibrary.io/styles/leonardo-da-vinci
- 来源类型: `site`
- 原文: `Leonardo Da Vinci's painting depicting … by Leonardo Da Vinci --v 6.1`
- 点评: 同构；「painting」限定词会压掉手稿/解剖图那一支——若要覆盖达芬奇手稿，需另写 `sketch/codex` 变体。

### B9. 梵高 · Civitai LoRA「Van Gogh Style」（触发词 vg）
- URL: https://civitai.com/models/100873
- 来源类型: `site`（模型页；数据经 civitai 公共 API 核）
- 原文: trainedWords = `["vg"]`（模型类型 LORA；同页另有 Van Gogh Diffusion checkpoint, id 91, trainedWords `["lvngvncnt"]`）
- 点评: SD 生态的「画家风格」形态是**触发词 + 权重**（不是句子）；与 MJ 的 `by <artist>` 句式为两套控制语言，模板里必须分开写。

### B10. 莫奈 · Civitai LoRA「Monet painting style」
- URL: https://civitai.com/models/460366
- 来源类型: `site`
- 原文（描述截断）: "A style LoRA to reproduce Claude Monet's painting. It's a merge of multiples LoRA trained with the same dataset on SDXL but with different training parameters. **Use a weight between 0.6 and 1.2.**"（trainedWords: `cmnt`）
- 点评: 给权重区间（0.6–1.2）——正是我们「控制参数（弱/中/强）」要做的事，可把「权重」列为 SD 版强度旋钮。

### B11. 塞尚 · Civitai LoRA「Paul Cezanne style」
- URL: https://civitai.com/models/296836
- 来源类型: `site`
- 原文（描述截断）: "Try to use both **"PaulCezanne"** and **"oil paining"** in your prompt. Works with CGF scale (~3 - 9) … Weights in betwee[n]…"（trainedWords: `PaulCezanne`, `oil paining`）
- 点评: 给出**组合用法**（触发词+媒介词）与 CFG 区间——SD 版「句法」的最小例子。

### B12. 马蒂斯 · Civitai LoRA「Henri Matisse Style - Fauvism」
- URL: https://civitai.com/models/792117
- 来源类型: `site`
- 原文（描述截断）: "The trigger word is "Matisse". img2img style transfer is best achieved by using ControlNet canny model with denoising strength…"（trainedWords: `Matisse`）
- 点评: 提到「风格迁移用 ControlNet canny」——把构图与风格拆开的工程做法，对应我们「70/30 组合」思路的外部实现。

### B13. 北斋 · Civitai LoRA「Hokusai Style (Thirty-six+ Views of Mount Fuji)」
- URL: https://civitai.com/models/137656
- 来源类型: `site`
- 原文（描述截断）: "Hokusai style trained on the Thirty-six Views of Mount Fuji and some additional selected other art from him."（trainedWords: `Hokusai style`, `painting`）
- 点评: 训练集写明=富岳三十六景——数据来源透明，与我们「视觉指纹」要引作品来源的要求一致。

### B14. 米开朗基罗 · Civitai LoRA「Michelangelo Style (Italian Renaissance)」
- URL: https://civitai.com/models/1118249
- 来源类型: `site`
- 原文: trainedWords = `[" michelangelo style"]`（LORA；另有 id 337228「Michelangelo Paintings High Renaissance」）
- 点评: 触发词直接是自然短语 `michelangelo style`——SD 生态也在往「句式」靠；对照 B9/B10 可见两种流派并存。

### B15. 达·芬奇 · Civitai LoRA「Da Vinci Drawing style - CE」
- URL: https://civitai.com/models/671809
- 来源类型: `site`
- 原文（描述截断）: "Weight around 0.9 suits most pictures, within a range of around 0.5 - 1.2 depending on desired result."（trainedWords: `dvnciCE_style`）
- 点评: 「Drawing style」定位=手稿/素描支（与 B8 的 painting 支互补）；权重建议 0.5–1.2 再给一档强度参数样本。

### B16. 毕加索 · Civitai LoRA「Pablo Picasso Blue」
- URL: https://civitai.com/models/774233
- 来源类型: `site`
- 原文（描述截断）: "Experimental LoRA to capture the colors and palette of Picasso's Blue Period. … The intensity and saturation of blues become more prominent at 0.4 and intensify further at higher weights."（trainedWords: `picasso`）
- 点评: **按时期切片**的 LoRA（Blue Period）——正好补 B3 的「一个名字糊掉多时期」缺口；可写进毕加索模块的「分时期控制参数」。

### B17. willwulfken 关键词参照表 · 画家关键词行（MJ 生态 12.3k★）
- URL: https://github.com/willwulfken/MidJourney-Styles-and-Keywords-Reference/blob/main/Pages/MJ_V4/Style_Pages/Just_The_Style/Artists.md
- 来源类型: `repo`（该 repo 12.3k★；Artists.md 为 V4 关键词对照页）
- 原文（截断，行内关键词）:
  > `| Painting By Van Gogh |` … `| Painting By Salvador Dali | Painting By Pablo Picasso | Painted By Andre Masson |` … `| Painted By Leonardo Da Vinci | Painted By Da Vinci |`
- 点评: 关键词型（`Painting By X` / `Painted By X`）prompt 片段的对照表——MJ 早期生态把画家名当**滤镜关键词**堆进 prompt；可作为「句式 A：by <artist>」的历史来源注脚。

---

## 缺口（未取到 / 已试路径）

1. **歸藏抽卡/结算动画提示词全文**：正文在 X 线程（https://x.com/op7418/status/2104085484347818226），X 页面 JS 渲染，`read` 只拿到 200 + 空壳；已试：read(X)、read(airebao 转述)、read(guizang.ai 首页 200 但无该文)、GitHub 搜 `op7418` repos（仅 guizang-s-prompt 提示词库，无此条）。**未找到（已查: X/airebao/guizang.ai/GitHub op7418）**。
2. **Lexica（SD prompt 搜索）**：`https://lexica.art/api/v1/search?q=…` 对 8 位画家全部 HTTP 500（已试 2 轮）。未取得。
3. **PromptHero 搜索页**：`https://prompthero.com/search?q=van%20gogh` 两次超时（read 通道）。未取得。
4. **HuggingFace 数据集内搜索**（`Gustavosta/Stable-Diffusion-Prompts` 等）：datasets-server search API 超时（一次 25s、一次 60s），未取得。
5. **Reddit / OpenArt / Krea 等画廊**：本轮未试（web_search 全限流，无入口；按缺口规范记一条）。
6. **Midlibrary 的 SREF code 字段**：页面由 JS 注入，`read` 未渲染出 code 值（prompt 句与版本参数已取到）。未取得。
7. 搜索通道整体限流（2026-10-15，parallel/exa/firecrawl/startpage/duckduckgo/ecosia/google/mojeek 全灭）——以上均绕行 read/curl/GitHub API 直取。

---

## 自审（四段）

### A 早产出
- 本文件与 `patterns.md` 同批落盘；猎场期间先取得外部 15 条全文（A1–A4）即已可对照，后补 B 类 17 条。

### B 反驳（挑 5 条最强结论逐条试推翻）
1. 「mg-styles-15 与内部 15 卡同源」→ 试推翻：两者署名同为 Opus 5.5、风格 15/15 重合，但语言（中/英）与时长（10s vs 10s）一致、未找到作者同一性的直接证据 → **WEAKENED**（保留 [推测]，文中已改写为「风格一一对应，同源未确证」）。跑过的命令：read github.com/Vincentwei1021/mg-styles-15（README 全文）、read knowledge/domains/motion-graphics/origin/提示词全文.md。
2. 「awesome-ai-motion 的 prompts/ 目录都是逐字原文」→ 试推翻：README 原文写「公开提示词不保证相同结果，作品尚未逐条独立复现」，且 A6/A7/A8/A9 抽查 4 条与推文标题一致、长度不一（1 句～848 字符）→ **CONFIRMED（逐字性由站点自述 + 抽 4 条一致性支持）**。跑过的命令：curl raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/{4 个 ID}.txt。
3. 「Midlibrary 每页都有一条可复制 prompt」→ 试推翻：米开朗基罗页只有 `by Michelangelo`（无 `… depicting` 前句）→ **WEAKENED**（8 页中 7 页同构、1 页简式；B7 已如实标注）。
4. 「Civitai 模型页含示例 prompt」→ 试推翻：`/api/v1/images?modelId=…` 抽 8 模型×40 图，meta.prompt 全为 null → **OVERTURNED**（示例 prompt 字段不可得；B9–B16 已改为引用 trainedWords + 描述里的用法建议，不再声称有示例 prompt）。
5. 「Genuary 是 prompt 语料」→ 试推翻：其 31 条是给人（艺术家）的创作约束题，不是给模型的指令 → **WEAKENED**（保留但改口径：标注为「另一物种/对照组」，不作直接 prompt 模板用）。

### C 机械验证
检查器：`bash` 计数 + `read` 抽 3 条 URL。结果见文末附「验证输出」节（同一次运行粘贴）。

### D 小结（≤14 行）
- 已确立：外部同类 prompt 体系存在且量大（mg-styles-15 全量 15 条 + rubric + 模板；awesome-ai-motion 821 作品/prompts 目录；promptmotion 22+17 案例逐字提示词；Genuary 31 题；Anthropic 官方 skills 2 条；Midlibrary 8 画家句；Civitai 8 画家触发词）。
- 被推翻：Civitai 图库含示例 prompt（API meta 全空）；「Midlibrary 每页同构」降级为 7/8。
- 未知：歸藏抽卡 prompt 全文；Lexica/PromptHero/HF 数据集通道；mg-styles 与内部视频同源确证。
- 下一步：patterns.md 已同步提炼 14 条模式并指出缺口；建议 B-07 直接用 A7（twoclipping）与 A1（mg-styles）做「输入反问 vs 固定任务头」对照实验。
- 我仍赌错的是什么：把 Civitai 当作「有示例 prompt 的画廊」下注，输了；下轮若需画家 prompt 实例，优先走 Midlibrary 的 benchmark 页（16 题横评）与 awesome-ai-motion 类索引，而不是模型站。

---

## 验证输出（C 机械验证，原样粘贴）

```
（1）计数检查（bash，2026-10-15，cwd=D:/Project/Designers_Brain）：
$ grep -c "^### [AB][0-9]" knowledge/agent-art/prompts/corpus.md
41          # 条目数：A 类 24 条 + B 类 17 条
$ grep -o "https://" knowledge/agent-art/prompts/corpus.md | wc -l
52          # URL 出现次数（含复用）
$ grep -c "^## P" knowledge/agent-art/prompts/patterns.md
14          # patterns.md 模式数（总表 14 行同）

（2）抽 3 条 URL read 验证（原样输出）：
--- [1] https://midlibrary.io/styles/henri-matisse ---
「Midjourney prompt (click to copy) [Copied to clipboard! Henri Matisse's painting depicting … by Henri Matisse --v 6.1]」
（与 B5 记录一致；页面另含 SREF code 区与 16 题 SREF Benchmark）

--- [2] https://promptmotion.art/zh/p/pelican-on-a-bike ---
提示词（原文引用）:
「生成一个鹈鹕骑自行车的 3D 页面，尽可能把你所有的能力全部都用上. 然后上传到 CDN 上, 把访问链接给我」
来源: GitHub @riba2534 https://github.com/riba2534/claude-opus-5-5-demo （1,010 个星标；「一次生成」「超高」推理强度；代码没有人工改动）
（与 A17 记录一致）

--- [3] https://raw.githubusercontent.com/guanmo-ai/awesome-ai-motion/main/prompts/2103116235009347650.txt ---
「Create a 4–5 minute cinematic video about the Battle of Austerlitz (1805), built entirely in code.
Research the battle thoroughly and decide for yourself how to tell the story, structure the pacing, explain the strategy, and visualize the events. I want it to be historically accurate, dramatic, easy to understand, and visually exceptional.
Use the attached paintings as visual inspiration, not a strict style requirement. … Don't make it feel like a generic infographic or strategy game. It should feel like a cinematic historical film that happens to be rendered with code.
You have complete creative control. Surprise me.」
（与 A9 记录一致，848 字符全文）
```
