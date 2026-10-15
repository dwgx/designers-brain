# 候选评估：Top 10

> 依据：2026-10-15 GitHub Search API 实测数据（stars/license/描述）+ 对 mg-styles-15 与 ojack/hydra 的仓库页直读；未逐一跑通代码，运行结论均标 [UNVERIFIED]。
> 完整 69 行候选表见 `repos.md`。每条给：能复用什么 / 该避开什么 / 对应车道（A 画家蒸馏 / B 代码动画）。

### 1. Vincentwei1021/mg-styles-15（MIT，866★）
单库内含 B 车道要做的整条管线：15 条完整提示词、每片全源码、harness/render.mjs（headless Chrome 逐帧捕获→ffmpeg 合成）、lib/audio（mgaudio + 103 乐器采样，音画同源）、rubric.md（AI 评审两轮，7.57–8.21/10）、template.md（output spec / technical route / creative seed / signature features 四段）。**复用**：harness 与 rubric 直接作为 B-02 的基线实现；四段模板与本项目 `templates/style_card.md` 逐段对照；其"同一提示词每次出片不同、需多轮迭代"的自述支持我们的"先 6 关键帧再动画"流程。**避开**：字体未随库发布；11/15 条音轨因数值库漂移不能位级复现——别把"重跑必然同结果"当保证。**车道**：B 核心，A 参照（风格说明写法）。

### 2. lemomo-ai/lemo-opuscar（MIT，2387★）
43 种影片风格，每风格 = 风格提示词 + 纯代码样片（Opus 5.5 制作）+ 导演/技术指南，是"风格 = 可判定规则 + 样片"的大规模实例。**复用**：三层打包形态（提示词→样片→指南）与 43 风格的覆盖面，作为风格卡库的对照集。**避开**：以视频成品为主，代码可复用性未验证 [UNVERIFIED]。**车道**：B。

### 3. cth9191/animate（MIT，710★）
单文件 canvas 短片 skill：内置 7 风格、beat-mapped 音乐、storyboard check-in 机制——check-in 与本项目"先出 6 关键帧"同构。**复用**：check-in 的措辞与结构、单文件约束（利于确定性逐帧捕获）；其"从参考匹配风格"的能力对应我们的模块组合实验。**避开**：风格数量少，需外接我们的画风段。**车道**：B。

### 4. klsoen/opus-js-animations（MIT，23★）
明确署名 Opus 5.5 的 JS 影片 skill：brief→声音（文件/YouTube/生成/AI 配音）→导演稿→frame-exact MP4。**复用**：作为 B-06 Opus 5.5 证据链的一环；流程描述可直接对表四段结构。**避开**：样本小、更新少，不作代码依赖。**车道**：B（证据链）。

### 5. yihui-dev/awesome-opus5-5-videos（MIT，5088★）+ joeseesun/opus-video-prompts（无许可，348★）
两个"案例 + 提示词"语料库：前者英文持续更新（含 live remake 对照），后者中文 54 例可复制。**复用**：作为提示词蒸馏的对照集，检验我们归纳的"量化规则 + 反约束"是否覆盖它们的写法。**避开**：后者无 license，只读不整段搬。**车道**：B。

### 6. mattdesl/canvas-sketch（MIT，5309★）
生成艺术框架，自带确定性帧导出与 ffmpeg 集成。**复用**：作为 harness 的替代实现或参照，对比 mg-styles-15 自研 render.mjs 的取舍。**避开**：beta 状态、API 变动史。**车道**：B。

### 7. processing/p5.js（LGPL-2.1，24.1k★）+ aferriss/p5jsShaderExamples（MIT，898★）
最通用的浏览器渲染底座 + 注释完备的 GLSL 示例集。**复用**：作为 02–15 卡"网页逐帧"的备选渲染器；shader 示例直接服务"纸张/笔触/颗粒"画风段的实现。**避开**：LGPL 只约束分发修改版，工具链内使用无碍——但别把 p5 代码嵌进闭源分发物。**车道**：B。

### 8. patriciogonzalezvivo/thebookofshaders（自定义许可，7048★）
噪声/图案/材质系统的 GLSL 教材，是"把画家技法翻译成可判定规则"的现成词典。**复用**：学习材料与技法对照（手绘线、纸张、颜料层叠）。**避开**：自定义版权声明（"sole copyright owner"字样）——复制代码前先读其许可页。**车道**：A×B 桥。

### 9. ahujasid/mcp-for-blender（MIT，30.9k★，原 blender-mcp）+ DLR-RM/BlenderProc（GPL-3.0，3746★）
LLM↔Blender 的现成 MCP 通道 + 无头程序化渲染管线。**复用**：01 卡（Blender 路线）的执行层；BlenderProc 的 headless 批渲染可作渲染农场；mcp-for-blender 的"LLM 操作 Blender"闭环与本项目 B-03 直接对应。**避开**：mcp 为社区插件、非官方（README 自述）；BlenderProc 是 GPL，工具自用无碍、再分发注意。**车道**：B。

### 10. metmuseum/openaccess（CC0，1440★）+ MuseumofModernArt/collection（CC0，1557★）+ art-institute-of-chicago/data-aggregator（AGPL-3.0，96★）
三家馆藏开放数据，覆盖核心画家（梵高/莫奈/塞尚/毕加索/马蒂斯）；AIC API 实测在线（133,169 件，2026-10-15）。**复用**：画家模块的原作图与元数据（年代/媒介/尺寸）做"视觉指纹"核验与组合实验素材；WikiArt 渠道（asahi417 爬虫 / HF huggan/wikiart）补风格标签。**避开**：图像逐件核对公开域状态；Rijksmuseum 与哈佛 API 需申请 key。**车道**：A。

## 备选（未进前十，一句话理由）
- marcelo-earth/generative-manim（Apache-2.0，933★）：LLM→manim 全自动视频 + benchmark，B 车道次选。
- Tonejs/Tone.js（MIT，14.8k★）：Web Audio 合成；若不用 mgaudio 就用它。
- asgeirtj/system_prompts_leaks（CC0，69.7k★）：含 Opus 5.5/Claude Code 系统提示词，agent 行为口径素材。
- Leonxlnx/taste-skill（MIT，96.7k★）：agent 审美 skill，"品味"进提示词的现成做法。
- joanrod/star-vector（Apache-2.0，4621★）+ ZJU-REAL/SVGenius（Apache-2.0，80★）：SVG 生成模型与 LLM-SVG 基准。
- willwulfken/MidJourney-Styles-and-Keywords-Reference（无许可，12.3k★）+ pharmapsychotic/clip-interrogator（MIT，2984★）：风格词表与反向提取。
- EGSECDA/vocaloid-style-mv-pipeline（MIT，136★）：确定性引擎 + Blender toon + 多画幅 headless。
- dgreenheck/tidewater（MIT，1279★）：Opus 5.5 的 three.js 场景代码样例。
