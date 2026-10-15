# video-shotcraft 调研（B-14）

> 任务：同作者（Vincentwei1021 / @VincentWei93）的 video-shotcraft（Claude Code / Codex 视频技能包）——是什么 / 解决什么 / 与 mg-styles-15 的关系（演进线）/ 工程细节（目录结构、SKILL.md、安装）/ 借鉴点（≥5，映射 B-11/B-13/B-08）/ 缺口。
> 方法：GitHub API + raw.githubusercontent / GitHub Pages 直读（2026-10-15 实测）；**未克隆仓库、未安装技能、未跑任何渲染**。
> 证据分级：`[自述]`=仓库文档自述；`[实测]`=本次 API/raw 实读；`[归纳]`=本次总结；`[推测]`=推断；`[UNVERIFIED]`=未跑未核。
> 姊妹卡：`mg-styles-15_compare.md`（B-10，15 卡溯源与 MIT 边界）· `mg-styles-15_handbook.md`（B-13）· `review_rubric.md`（B-11 评审表）。
> 作者身份核对：GitHub owner `Vincentwei1021`（vsc README「Follow me」链 X [@VincentWei93]；plugin.json 署名 `Wei Yihao`）——与 mg-styles-15 同一账号 `[实测]`。

## 0. 结论速览

1. **是什么**：一个**agent 技能包**（不是视频生成器）——把「给我的产品做一支宣传片」变成 Claude Code / Codex 可执行的端到端流程：真实页面截图采集 → 124 张镜头配方卡选卡分镜 → Remotion（React）代码作画 → 卡点剪辑 + 音效设计 → 逐帧 QA → 成片 MP4 + 浏览器动效工作台 + 剪映工程导出。**11,988★ / 1,072 forks**（2026-10-15 API 实测；created 2026-07-19，pushed 2026-10-13）。`[实测]`
2. **与 mg-styles-15 的关系**：同作者、同方法论家族（代码作画 + 确定性逐帧 + 卡库 + 独立 AI 评审两轮），但**技术路线不同**——vsc = Remotion + 真实页面截图 + 录制音效库；mg-styles-15 = 单文件 HTML/`window.renderAt(t)` + headless Chrome 捕获 + ffmpeg + 代码合成音频。**时间线上 vsc 更早（07-19 vs 10-02）且持续迭代**，mg-styles-15 是其后的提示词优先展示型实验（我们 15 卡的来源）。两仓**互不引用**（grep 0 命中）`[实测]`——「演进线」判定为同作者两条并行产品线 `[归纳]`。
3. **最值钱的三样**：①**判例式规则体系**（aesthetic-rules：每条 = 规则 + 用户原话判例 + 自检问题；编号 R/Q/S/C/P 一经发布不重排）；②**镜头卡格式**（YAML frontmatter 机读层 + 意图/动效核心/参数表/已知坑/参考实现）；③**验收工程**（每镜头 2 个写死的验收帧号 + 交付前干净上下文 subagent 对照清单出带帧号证据报告）。
4. **授权**：代码与文档 **Apache-2.0**；音频逐文件（Mixkit free license，见 ATTRIBUTION.md）；**Remotion 有独立许可**（个人/小团队免费，公司可能需付费）——与 mg-styles-15 的 MIT 不同，借用时分开记账。`[自述]`
5. **数字口径**：GitHub 仓库简介仍写「152 cards / 209 previews」是**旧值**；当前机读真相源 `gallery/api/library.json` = **cardCount 124 / styleCount 150 / previewCount 150**，树计数 124 卡（10 类）吻合 `[实测]`。

## 1. 它是什么、解决什么问题

`[自述]`（README / SKILL.md / llms.txt，2026-10-15 直读）：

- **定位**：面向 Claude Code & Codex 的 **agent skill**——「Tell Claude Code or Codex "make a promo for my product"」。Agent 自己采集真实页面、从镜头库里选卡、分镜、用 Remotion 写代码动画、卡点、加音效、逐帧检查，交出一支可继续编辑的 MP4。
- **不是视频生成器**：「Every frame is drawn by code from your own screenshots and copy, so the result is sharp, on-brand and fully editable.」——画面 = 代码（React/Remotion 组件），素材 = 产品真实页面截图，没有视频模型参与。
- **解决的问题**：把「做产品宣传片」这件需要动效设计师 + 剪辑 + 声音设计的事，拆成 agent 可执行、可验收、可复现的**流水线**，且把「调校积累」（缓动/时值/已知坑）沉淀成**可读的代码资产**而不是模型记忆。
- **交付物**（README「What you get」）：成片 MP4（1920×1080@30fps h264）· Remotion 完整工程（每镜头一个 React 组件）· 浏览器动效工作台（剪映式多轨编辑，端口 5198）· 可选剪映（CapCut CN）工程导出 · 可选社交平台发布（Upload-Post API）。
- **规模自述**：124 张镜头配方卡（10 类）+ 150 支动态样片 + 149 个 SFX（16 类）+ 5 支 BGM + 36.2s 已验收模板片（Ink Press）`[实测]`（landing/README/library.json 一致）。

## 2. 与 mg-styles-15 的关系（同作者演进线）

### 2.1 时间线（GitHub API created_at，2026-10-15 实测）

| 日期 | 仓库 | ★ | 定位 |
|---|---|---|---|
| 2026-07-19 | `Vincentwei1021/video-shotcraft` | 11,988 | Remotion 产品宣传片技能（本卡主角；持续更新至 10-13） |
| 2026-08-22 | `video-talkcraft` | 1,590 | 配音解说片姊妹技能（vsc 的 workbench 从其移植 `[自述]`） |
| 2026-09-18 | `anything2explainer` | 2,509 | 任意主题 → 解说片 |
| 2026-10-02 | `mg-styles-15` | 868 | 15 风格 × 单提示词展示（**我们 15 卡的来源**，MIT） |

### 2.2 两条技术路线对照 `[实测+自述]`

| 维度 | video-shotcraft | mg-styles-15（B-10 已拆） |
|---|---|---|
| 渲染器 | **Remotion**（React 组件逐帧） | 单文件 HTML/Canvas/WebGL，页面暴露 `window.renderAt(t)`；`harness/render.mjs` 用 headless Chrome 逐帧捕获 → ffmpeg |
| 素材 | **真实页面截图**（整页 2x + 元素抠图 + layout.json）+ 少量手搓 UI | 纯代码作画（SVG/Canvas/WebGL/Three.js）+ 3D 片用 Blender |
| 音频 | 录制音效库（Mixkit 149 SFX + 5 BGM），卡点用 librosa 分析 | **代码合成**（`audio.py` + mgaudio + VCSL 采样） |
| 组织 | 技能包（SKILL.md + references/ + demos/ + template/ + workbench） | 展示仓（prompts/ + demos/ + harness/ + rubric.md） |
| 评审 | `final-review.md` 独立终检清单（干净上下文 subagent） | `rubric.md` 两轮 AI 评审（7 维 1-10，终评 7.57-8.21） |
| 许可 | Apache-2.0（音频逐文件；Remotion 独立） | MIT |

### 2.3 共同 DNA（同作者方法论家族）`[归纳]`

1. **代码作画**：无图像/视频生成模型，画面 = 可逐帧复现的代码。
2. **确定性**：帧 = 时间的纯函数（vsc 明令禁 `Date.now()`/`Math.random()`；mg-styles 用 `renderAt(t)`）。
3. **卡库 + 参考实现**：配方卡（语义/参数）与调校过的源码分离，卡指向实现。
4. **独立评审两轮制**：制作者不做首检，评审者干净上下文、按清单出证据。
5. **中文优先文档 + 双语展示页**（vsc 有 README_CN/JA；mg-styles 有中英展示页）。

> 互引核查：`grep mg-styles` 在 vsc 的 README.md / README_CN.md / SKILL.md 命中数 = 0；mg-styles-15 README 全文无 video-shotcraft 字样 `[实测]`。作者**未自述**两条线关系——「同一方法论家族的两条并行产品线」是本次归纳 `[归纳]`，不是作者原话。

## 3. 工程细节

### 3.1 仓库总览（git trees API，1,648 条未截断，2026-10-15 `[实测]`）

| 路径 | 内容 | 规模 |
|---|---|---|
| `SKILL.md` | agent 入口 + 核心制作规则 | 20,853 B |
| `references/` | 9 个方法论文档 + `shots/`（124 卡 10 类 + ATTRIBUTION）+ `sequences/` | 136 文件 |
| `demos/` | 每卡 Remotion 参考实现（含 `_fixtures/` 共享件、`_legacy/` 下架、`_textures/` 截图） | 203 目录 / 280 文件 |
| `template/` | 已验收成片模板 Ink Press（36.2s / 1085f / 10 镜头） | 70 文件 |
| `workbench/` | 交付后浏览器动效工作台（Vite + Remotion Player） | 73 文件 |
| `gallery/` | 静态画廊 + `api/library.json`（206,605 B 机读卡索引）+ `llms.txt`（32,287 B） | 196 文件 |
| `shot-polish/` | **作者内部打磨工作区**（216 notes → 150 final-notes + decisions.json） | 376 文件 |
| `assets/` | `lib/` 7 组件 + `scripts/` 采集/冒烟 + `audio/`（149 SFX 16 类 + 5 BGM） | 193 文件 |
| `jianying-export/` `publish/` | 剪映工程导出（pyJianYingDraft）/ Upload-Post 发布（纯标准库 Python） | 5 / 2 文件 |
| `.claude-plugin/plugin.json` `agents/openai.yaml` | Claude Code 插件清单 / Codex UI 元数据 | 549 / 531 B |
| `.github/workflows/` | `pr-checks.yml`（tsc 全 demo + vitest + 冒烟渲染）· `deploy-pages.yml` · `showcase-publish.yml` | 3 |

`references/` 方法论文档清单（实测字节数）：`pipeline.md` 25,226 · `aesthetic-rules.md` 27,528 · `sound-design.md` 27,677 · `music-beat-sync.md` 13,019 · `workbench.md` 13,212 · `guided-free-creation.md` 10,874 · `jianying-export.md` 9,348 · `final-review.md` 7,095 · `publish-upload-post.md` 6,596。

**镜头卡 10 类**（树计数 124 卡）：typography 22 · ui-entrance 21 · transition 15 · effects 15 · opening 11 · interaction 11 · camera 10 · rhythm 8 · outro 6 · data 5。README 另按「镜位数」口径列 150（单卡可带多个 `style-key` 变体）`[实测]`。

### 3.2 SKILL.md 写法（agent 入口）

- **frontmatter**：`name: video-shotcraft` + `description:`（**双语触发词**：「use video-shotcraft to make a video/promo」「把前端项目/网页做成产品视频」「点名 Ink Press 模板」「单个动效镜头」）——触发面写得极具体，等于把「什么时候该激活我」写成检索条件。
- **先判断模式**（三选一，不合并）：① 直接使用模板（读 `template/TEMPLATE.md`）② 自主自由创作（读 `references/pipeline.md`，不逐阶段等确认）③ 共同创作（读 `references/guided-free-creation.md`，阶段 0–3 逐级确认）。附**两个例外**（点名模板 = 已选模式；点名镜头卡 = 镜头约束已定）。模式未定时先做**最小只读产品检查**再推荐。
- **核心理念 9 条**（浓缩版）：① 复刻既有页面必须真实截图（手搓 UI 限非复刻场景，质量/表达是硬门槛）；② 视觉语言从产品自身生长（先提设计 spec：字体/栅格/色 tokens，卡只借运动语法，蒙皮必须换）；③ 电影感来自运镜/光影/节奏/声音，不来自炫技；④ 每镜头只讲一个动效，落定必须呼吸（hold）；⑤ 强节奏 BGM 全片卡拍（网格拟合 + 瞬态钉帧 + 回测 ≤3 帧；整画面冲击全片 ≤3 处）；⑥ 用卡必须先解析 Gallery 索引并读**准确 demo 源码**（凭卡名新写 = 放弃全部调校积累）；⑦ 共同创作前置确认 vs 自主创作记录判断；⑧ 验收贯穿全程 + 交付前**干净上下文 subagent** 独立终检；⑨ **确定性渲染**（禁 `Date.now()`/`Math.random()`，种子从 index 派生）。
- **「何时读哪个文件」路由表**：把 9 个方法论文档按触发时机（模式未定/BGM 已选/分镜/逐镜头实现/声音设计/验收/交付收尾…）映射成一张表——**渐进披露**：入口小、按需加载。
- **交付收尾 1-2-3**（成片后主动做，不等人问）：先打开动效工作台 → 依次说三件事（自愿 @ 作者 / 邀请进 Showcase / 可导剪映工程），每件只说一次——**产品化叙事**，把开源项目的增长动作写成 agent 行为规范。

### 3.3 镜头卡格式（以 `references/shots/opening/text-as-mask.md` 为实例 `[实测]`）

```yaml
---
name: text-as-mask
一句话: 文字视频遮罩——超粗大标题字内透出产品面板，结尾字形指数冲入放大 46 倍溢出、内部画面接管全屏
适用: 品牌词/口号与产品画面二合一的开场或章节卡；字是门、产品在门里
时长: 165f（入场 18f + 字内漂移 78f + 吸气 8f + 冲入接管 24f + 落定/hold 37f）
能量: 中高（漂移段沉稳，接管段一次爆发）
标签: typography
---
```

正文五段：**意图**（为什么存在 + 同族/不并用关系）→ **动效核心**（逐条物理参数：`mask-image` data-URI、漂移 `bezier(0.3,0,0.7,1)`、冲入对数空间 `t^1.8`、transform-origin 必须钉在实心笔画内…）→ **参数表**（`| 参数 | 典型值 | 调节手感 |`）→ **已知坑**（每条都是踩过的坑：「别给字形做描边高光——可变字体字形由重叠轮廓拼成」「换词/换字体后 origin 手推值必失效」）→ **参考实现**（`demos/opening/text-as-mask/`）。

**与本地 15 卡对照**：本地卡「画风段」= 量化可判定规则（vsc 放在 frontmatter + 动效核心）；本地「别做成」= 反退化约束（vsc 放在**已知坑**，且每条都带原因/后果）；vsc 多出的是 **frontmatter 机读层**与**参考实现指针**——这两样本地卡没有 `[归纳]`。

### 3.4 判例式规则体系（`aesthetic-rules.md`）

- **每条 = 规则（一句可执行的话）+ 判例（用户原话/返工经过）+ 自检问题**，三要素缺一不可。
- 编号体系 R(节奏)/Q(质感·运镜·构图)/S(声音)/C(文案)/P(流程)；**编号一经发布不重排，新增只追加**；准则可以有意识违反，但每次违反必须写进项目文档。
- 已读实例：R1 字标 hold ≥1s（判例：用户原话两处）· R2 加速度而非匀速 + 收尾 0.5s 停顿 · R3 **「节奏宁慢勿快」**（判例：全片六次独立反馈全部指向放慢，**从未有一次「太慢了」**）· R4 整画面级冲击全片 ≤3 处 · Q1 真实截图 · Q2 3D 文字发糊先查栅格化路径（CSS `zoom` 而非 transform scale）· Q4 光效不群发且裁进圆角 · Q9 飞入终点必须是真实槽位 · Q11 字幕有效字高 ≥5% 帧高 · S1 按「片种」选音不按「事件」选音（禁游戏音色不禁动作）。
- 验收动作：阶段 7 逐条过一遍，输出 `编号 ✓` 或 `编号 ✗(位置=镜头名/帧号)`。

### 3.5 制作流水线（`pipeline.md`，八阶段 0–7）+ 验收工程

| 阶段 | 内容 | 关键机制 |
|---|---|---|
| 0 | 产品理解与执行约束 | 只读检查 → 产品简报 + 需求到执行决策表；敏感数据先冻结/脱敏 |
| 1 | 视觉方向与 styleframe | **不渲染视频、不写 Remotion**，纯 HTML 静态 styleframe 定调；**品牌→动效参数推导表**（能量轴×调性轴 → 6 预设：主时长/easing/过冲/squash）；参考片 ffmpeg 抽帧做 motion breakdown |
| 2 | 功能→镜头映射 | 扫 `shots/` frontmatter 按能量曲线选卡；一种手法全片只当一次主角 |
| 3 | 分镜与放行 | 先查 `sequences/` 骨架（`promo-energy-arc` 4 段位）；**帧预算先划 hold**（字标 ≥30f、批量收尾 15f、开场 ≥3s）；帧级时间轴 `| shot | from | duration | 内容 |` |
| 4 | 素材采集 | `capture-template.mjs` 三件套：整页 2x 截图（`deviceScaleFactor:2`）+ 元素抠图 + `layout.json` 坐标表 |
| 5 | 逐镜头实现 | **三读硬规则**（library.json 校验卡名 → 读卡全文 → 读准确 demo TSX → copy 组件）；**每镜头写死 2 个验收帧号**，`npx remotion still` 静帧肉眼验收；每轮改完整片重渲 + ffmpeg 抽帧回看；**确定性铁律**；为工作台留接口 |
| 6 | 声音设计 | **画面锁定后才开始**（最贵的顺序教训）；16 类 SFX 先类别后音色；BGM 用布尔 inputProp 出**带/不带 BGM 两版** |
| 7 | 独立终检 | `final-review.md`：干净上下文 subagent、17 项审查输入、P/F/V/S/B/D/A/Q 检查项、**逐条带帧号证据**、缺输入标「无法验证」 |

**终检要点**（`final-review.md` 实读）：审查 Agent 不参与制作、不给它制作过程理由；报告格式 `S2 ✗ 第 515 帧：用户选择 whip-pan，实际实现为 flash-cut`；「不要用没有证据的『整体不错』代替逐项检查，也不要为了报告好看而全部标记通过」。

### 3.6 模板与工作台契约

- **模板 Ink Press**（36.2s / 1085f / 10 镜头）：换产品复现指南 = 采集三件套 → 换 layout.json → 逐镜头适配（**必改**：PageCam keys/切片文件名/文案；**不要动**：缓动曲线、时长配比、hold 帧预算、SFX 钉帧结构——「改了等于重做调校」）。
- **工作台契约**（`workbench.md`）：成片工程写 `src/workbench.ts` 清单（`WORKBENCH` 常量：shots/transitions/captions/overlays/sfx/bgm），浏览器里把成片拆成多轨编辑（挪镜头/改文案/换音效/变速）后导出。**三层可编辑度**：时间与图层（所有 clip）→ 内容与样式（**语境参数 props + schema**）→ 拆解导入（清单同源）。**「节奏命门」保持常量**（弹入时长/错峰/缓动/相机路径不暴露）；时间表只写一份（`SHOTS` 唯一事实源，SFX/字幕/转场派生并 export）；交付前 `npm run parity` 证明拆解无损；版本按清单内容哈希判同版。
- **CI 与测试**：`npm test`（vitest 覆盖 mulberry32/velocityAt/lagged/dampedSettle/handheld，确定性断言）；`smoke-render-demos.py` 渲染每个 demo 首帧断言不崩；`pr-checks.yml` 自动跑 tsc 严格编译 + 测试 + 冒烟。

### 3.7 音频与卡点

- 149 SFX 分 16 类（transition/impact/riser/camera/ui/text/paper/film/light/data/scifi/mech/glass/fluid/crowd/counter）；词汇表 `sparkle` 的目录名是 `light/`；`ui/` 一半是合成反馈音，**不可整目录放行**。
- 卡点方法论（`music-beat-sync.md`）：librosa 网格拟合求 BPM/相位 + kick/snare/hihat 三分类鼓点定位；时间线用 `beatF(n)` 写；**渲后从成片抽音轨回测切点误差 ≤3 帧**；整画面级冲击全片 ≤3 处（R4）。
- 长样本（>5s，21 个）必须显式给 `durationInFrames`；轻音素材（峰值 <-12dB，7 个）需预归一化/给增益——终检清单 A5/A6 逐条核。

### 3.8 安装方式（4 种，全部 `[自述]` 实测原文）

1. **把链接丢给 agent**（最简单）：`Install this skill for me: https://github.com/Vincentwei1021/video-shotcraft`。
2. **skills CLI**：`npx skills add Vincentwei1021/video-shotcraft`（skills.sh）。
3. **手动 clone + 软链**：
   ```bash
   git clone https://github.com/Vincentwei1021/video-shotcraft.git
   cd video-shotcraft
   ln -s "$(pwd)" ~/.claude/skills/video-shotcraft   # Claude Code
   ln -s "$(pwd)" ~/.codex/skills/video-shotcraft    # Codex
   ```
4. **Claude Code 插件**：仓内有 `.claude-plugin/plugin.json`（`"skills": "./"`，整仓即技能）；Codex 侧另有 `agents/openai.yaml`（harness 读 UI 元数据，**不读 agent**；Claude Code 读 SKILL.md frontmatter）——跨 harness 双轨打包的样板。
   - 中国大陆慢速镜像：`git clone https://atomgit.com/VincentWei/video-shotcraft.git`。
- **环境要求**：Node.js + npm（Remotion/模板/工作台）；ffmpeg/ffprobe（抽帧 QA）；uv（仅 BGM 节奏分析）；puppeteer（仅页面采集，按需装）。headless Linux 三坑：`--concurrency=1`、用 chrome-headless-shell、CDN 被墙时 `--browser-executable`。

### 3.9 作者内部打磨流程（`shot-polish/`，vsc 独有的透明度）

- `BRIEF.md` / `BRAND-BRIEF.md`（13.3K / 9.3K）+ `notes/`（216 条）+ `final-notes/`（150 条）+ `decisions.json`（42.7K）。
- `decisions.json` 结构实测：`{savedAt, summary, decisions[]}`；summary = `{"before": 8, "v1": 50, "after": 92, "drop": 66, "undecided": 0}`——即 **216 个 demo 逐个三选一（原版 8 / 第一版 50 / 第二版 92），砍掉 66 个**，落成今天的 150 镜；单条 decision = `{stem, path, name(中文), pick, note}`。
- 工具：`build-compare.py`（对比页）、`serve.py`、`sheet.py`、`tsc-demos.sh`、`compare.template.html`。→ **「卡库不是写出来的，是 216 个候选逐个 A/B 裁出来的」**——这是最直白的一条工艺证据 `[实测]`。

## 4. 对我们的借鉴点（逐条映射 B-11 / B-13 / B-08）

**借 1 · 判例式规则写法 → B-11（+B-13）**
每条规则三要素：规则 + 用户原话判例 + 自检问题；编号一经发布不重排、只追加；违反必须写进项目文档。
→ 动作：`templates/style_card.md` v0.2 的「别做成」段升级为**判例格式**（每条附「模型默认行为是什么/踩过的坑/怎么自检」）；`review_rubric.md` 增补「规则违反须记录」条款；B-13 手册收录判例原文。

**借 2 · 镜头卡格式（frontmatter 机读层 + 参考实现指针） → B-11（+B-13）**
vsc 卡 = YAML frontmatter（name/一句话/适用/时长分段/能量/标签）+ 意图/动效核心/参数表/已知坑/参考实现；frontmatter 汇成 `gallery/api/library.json`（124 cards, stats 机读）+ `llms.txt`（LLM 索引）。
→ 动作：style_card v0.2 加 frontmatter 层（能量/时长/适用/标签）与「参考实现」指针字段；B-13 手册给 15 卡建 `library.json` 式索引（卡名 ↔ demo 文件 ↔ 组件）。

**借 3 · 三读链 + 「参数不得降档」 → B-13（+B-08）**
「解析卡名 → 读卡全文 → 读**准确 demo 源码** → copy 组件」是硬规则；demo 代码是「调校过的参数真相」，卡上「已知坑/命门」参数只升不降；凭卡名新写 = 放弃全部调校积累。
→ 动作：B-13 手册把「卡 → 参考实现 → 调校参数」的优先级链写成章；B-08 迁移指南用此证明「调校积累应放代码资产里，而非模型记忆里」——换任何模型都吃同一份真相。

**借 4 · 确定性渲染铁律 → B-11（+B-13）**
禁 `Date.now()`/`Math.random()`/无参 `new Date()`；伪随机用 mulberry32/哈希，**seed 从 index 派生**；tween 全部 clamp；组件是 `useCurrentFrame()` 纯函数（→ 才能上工作台被任意拉伸/变速）。
→ 动作：对照 `templates/determinism_contract.md` 补「种子派生写法 + clamp + 纯函数」三条实现级条款；B-13 手册收 vsc 的 `helpers/rand.ts` 作范例（本机可 0 成本复刻）。

**借 5 · 验收贯穿全程 + 独立终检 → B-11（+B-08）**
每镜头在计划里**写死 2 个验收帧号**，完成即 still 静帧肉眼验收（`out/qa/` 版本归档）；每轮改完整片重渲 + ffmpeg 抽帧；交付前干净上下文 subagent 按清单出**带帧号证据**报告（缺输入标「无法验证」，不许「整体不错」）。
→ 动作：review_rubric 补「每镜头 2 验收帧号」为制作侧硬要求；终检输入清单（17 项）可直接改写成我们的评审 prompt 附件；B-08 把「自查」从口号变成 agent 的 stop 条件（不跑不算完成）。

**借 6 · 品牌→动效参数推导表 → B-11（+B-08）**
不凭手感挑 easing：品牌放「能量轴 × 调性轴」→ 从 6 个预设起步（主时长/easing/过冲/squash 全给数）；自检两条（三个词能否对上品牌词；同一套 tokens 必须同时管入场/转场/hold——「一个品牌一种动效嗓音」）。
→ 动作：style_card 的「控制参数（弱/中/强）」升级为**两轴推导 + 预设表**；这是「可调强度」的量化实现路径，直接服务 A×B 组合实验。

**借 7 · 能量骨架 + 节奏单向性 → B-11（+B-13）**
`promo-energy-arc` 4 段位（品牌开场 8-12% / 单主角立传 12-15% / 功能爬升 55-65% / 峰值收场 13-16%）+ 呼吸字卡规则；**帧预算先划 hold 再排动效**；「节奏宁慢勿快」有实证（六次反馈全放慢、零次「太慢」）。
→ 动作：10s 片组合实验的骨架模板（压缩段位比例即可）；style_card 增「hold 预算」字段；B-13 手册把「放慢从未被否」列为默认参数取向。

**借 8 · 技能包打包与跨 harness 分发 → B-08（+B-11）**
SKILL.md frontmatter 双语触发词 + 「何时读哪个文件」路由表（渐进披露）+ `agents/openai.yaml`（Codex UI 元数据）+ `.claude-plugin/plugin.json`（整仓即技能）+ skills CLI/软链安装。
→ 动作：B-08 迁移指南直接采用此四件套结构：我们的「画家模块 + 代码艺术工作流」未来打包成技能时，入口小、按需加载、双 harness 可装；触发词写法（「当用户要求 X/Y/Z 时使用」）比抽象描述有效。

**借 9 · 工作台契约 / 同源原则（备选，偏工具链） → B-13（+B-11）**
`SHOTS` 唯一事实源（SFX/字幕/转场全派生并 export）；语境参数 props+schema、**节奏命门保持常量**；`durationProp` 让拉长跟着走；`parity` 验证拆解无损；版本哈希判同版。
→ 动作：B-13 手册「确定性管线」章收录「可编辑度分层」原则（哪些参数开放/哪些锁死），给未来实验工具链留设计依据。

## 5. 缺口节

1. **未安装未运行**：skill 未装、Remotion 未渲染、workbench 未启动——本卡所有「行为」描述来自仓库文档 `[自述]`，未做运行验证 `[UNVERIFIED]`（本机无 Remotion 工程；首渲需下载 headless Chrome，超出本轮范围）。落地验证建议：B-07 之后另立一条实验（跑 template 首帧）。
2. **数字口径漂移（引用时注意）**：GitHub 仓库简介「152 cards / 209 previews」= 旧值；当前真相源 `gallery/api/library.json` = 124/150/150/150 `[实测]`。另：`demos/README.md` 与 `workbench.md` 仍有个别「152」遗留引用；`llms.txt` 写「six-stage production methodology」而 `pipeline.md` 标题是**八阶段 0–7**——文档漂移两处，均不影响机制结论 `[实测]`。
3. **只抽样未全量**：`library.json`（206KB）仅核 stats + card[0] 结构；124 卡未逐卡读；`mediaCount/previewCount` 的字段语义未逐项核；`shot-polish/decisions.json` 只看 summary 与首条。
4. **互引关系**：「作者未自述两条线关系」——已查：vsc README/README_CN/SKILL 中 `mg-styles` 命中 0；mg-styles-15 README 全文无 `video-shotcraft`。不排除 GitHub 之外（X/抖音/小红书）有表述 `[未找到（已查: 上列 4 文件，2026-10-15）]`。
5. **姊妹仓只到元数据级**：video-talkcraft（1,590★）/ anything2explainer（2,509★）未读内容；「workbench 从 talkcraft 移植」为 vsc 文档自述。
6. **授权边界未做法律解读**：vsc = Apache-2.0（代码/文档），音频逐文件（Mixkit），Remotion 独立商用许可——若未来直接借用其卡文本/组件代码，需按 Apache-2.0 保留版权与许可声明；与 mg-styles-15 的 MIT 分开记账。
7. **建议下一步**：① B-13 手册新增「参考实现链 / 工作台契约 / 判例格式」三节（素材本卡 §3.3–3.6）；② B-11 用借 1/2/4/5/6 修订 style_card v0.2 与 review_rubric；③ B-08 直接引用借 3/8 作为「能力打包」范式；④ 可选实验：Remotion 栈成本标定（对比 mg-styles 的 harness 路线）。

## 6. 自审四段

### A · 早产出
本卡首版在调研中段落盘后成文；上列所有结构、数字、URL 均来自本轮 20+ 次工具调用的实时输出（GitHub API / raw 直读 / tree JSON 解析），未引用二手转述。

### B · 反驳（最强结论试推翻）

1. **「同作者」** → 推翻尝试：核 owner login 与署名。命令：`curl api.github.com/repos/Vincentwei1021/video-shotcraft`（owner=Vincentwei1021）+ plugin.json author「Wei Yihao」+ README 链 X @VincentWei93。**CONFIRMED**。
2. **「当前 124 卡 / 150 镜，GitHub 简介的 152/209 是旧值」** → 推翻尝试：三源交叉。命令：tree JSON 计数（124 卡 + ATTRIBUTION.md）、`library.json` stats（cardCount 124 / styleCount 150）、landing/README 口径（124/150）。**CONFIRMED**（简介为旧值）。
3. **「video-shotcraft 早于 mg-styles-15」** → 推翻尝试：API created_at。结果：2026-07-19 vs 2026-10-02。**CONFIRMED**。
4. **「两仓互不引用」** → 推翻尝试：全文字符计数。命令：`python: t.count('mg-styles')` → vsc README/README_CN/SKILL = 0/0/0；mg-styles README 全文读毕无 vsc 字样。**CONFIRMED**（范围限上述文件）。
5. **「确定性铁律是其明文规则」** → 推翻尝试：三处独立出处。SKILL.md 理念 9 + pipeline.md 阶段 5.6 + demos/README.md（「动画全部是帧的纯函数（无真随机 / 无 Date）」）。**CONFIRMED**。

### C · 机械验证（read 原样输出，2026-10-15）

**URL 1：`https://vincentwei1021.github.io/video-shotcraft/`**（read 工具输出，全文原样）

````
URL: https://vincentwei1021.github.io/video-shotcraft/
Content-Type: text/html
Method: native

---

---
canonical: https://vincentwei1021.github.io/video-shotcraft/
meta-color-scheme: dark
meta-description: video-shotcraft is an AI agent skill for Claude Code & Codex that makes cinematic product promo videos with Remotion. 124 shot recipe cards organized by function, tuned demos, and a production-ready template.
meta-google-site-verification: Qu8vMAC99goV9xnwf_0ZlGGimtmj24TWFNVUiTz2mhM
meta-og:description: An agent skill for crafting cinematic product videos with Remotion: 124 shot recipe cards, 150 motion previews, and a production-ready promo template.
meta-og:image: https://vincentwei1021.github.io/video-shotcraft/og-image.jpg?v=20260726b
meta-og:image:alt: video-shotcraft Gallery — shot recipes and motion samples
meta-og:image:height: 640
meta-og:image:width: 1280
meta-og:site_name: video-shotcraft
meta-og:title: video-shotcraft — AI Video Skill for Claude Code & Codex
meta-og:type: website
meta-og:url: https://vincentwei1021.github.io/video-shotcraft/
meta-twitter:card: summary_large_image
meta-twitter:description: An agent skill for crafting cinematic product videos with Remotion: 124 shot recipe cards, 150 motion previews, and a production-ready promo template.
meta-twitter:image: https://vincentwei1021.github.io/video-shotcraft/og-image.jpg?v=20260726b
meta-twitter:title: video-shotcraft — AI Video Skill for Claude Code & Codex
meta-viewport: width=device-width, initial-scale=1
title: video-shotcraft — AI Video Skill for Claude Code &amp; Codex | Cinematic Product Videos with Remotion
---

An agent skill for Claude Code & Codex

# 124 cinematic shot recipes. *One prompt* to a finished promo.

Every motion you see behind this page is a tuned, ready-to-use shot recipe card — your agent picks the shots, animates real product screenshots with Remotion, syncs the beats, and delivers the film.

[Browse all motions](https://github.com/Vincentwei1021/video-shotcraft) [![SVG Image] Star on GitHub ★](https://github.com/Vincentwei1021/video-shotcraft)

- **124**recipe cards
- **150**styles
- **150**motion previews
- **36.2s**ready template
````

**URL 2：`https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/.claude-plugin/plugin.json`**（read 工具输出，全文）

````
URL: https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/.claude-plugin/plugin.json
Content-Type: text/plain
Method: text

---

{
  "name": "video-shotcraft",
  "version": "1.0.0",
  "description": "Craft cinematic product videos with Remotion using shot recipes, motion previews, reusable components, SFX, and a production-ready template.",
  "author": {
    "name": "Wei Yihao"
  },
  "homepage": "https://vincentwei1021.github.io/video-shotcraft/",
  "repository": "https://github.com/Vincentwei1021/video-shotcraft",
  "license": "Apache-2.0",
  "keywords": [
    "video",
    "remotion",
    "motion-design",
    "product-video",
    "agent-skill"
  ],
  "skills": "./"
}
````

### D · 小结（≤14 行）

1. video-shotcraft = 同作者的 Remotion 产品宣传片 agent 技能：11,988★，Apache-2.0，124 卡/150 镜/149 SFX/36.2s 模板/工作台/剪映导出。
2. 与 mg-styles-15：同作者同方法论家族（代码作画/确定性/卡库/两轮评审），不同路线（Remotion+真实截图 vs HTML+headless Chrome）；vsc 更早且持续迭代；两仓互不引用（已查）。
3. 最值钱：判例式规则（规则+判例+自检）、卡格式（frontmatter+已知坑+参考实现）、验收工程（2 验收帧/镜头、干净上下文终检带帧号）。
4. 交付物：8 条借鉴点逐条映射 B-11/B-13/B-08（另备 1 条工作台契约）。
5. 数字口径：当前 = 124/150（简介 152/209 为旧值）；llms.txt「six-stage」vs pipeline.md 八阶段——两处文档漂移已记录。
6. 未核：未安装未运行（全为文档自述）；library.json 仅抽样；姊妹仓仅元数据。
7. 下一步：B-13 收 §3.3–3.6 三节；B-11 按借 1/2/4/5/6 修订模板与评审表；B-08 按借 3/8 写「能力打包」范式。
