# 迁移指南：让任意 agent 模型复现「10 秒 MG 动画」本领（B-08）

> 归属：GOALS B-08｜状态 v1.0（2026-10-15）｜作者：TransferGuide（wave5）
> 读者：人类操作者 + 任意 agent 模型（**不限于 Opus 5.5**；15 卡原作者署名 `Claude Code · Opus 5.5`，本指南解决的问题就是「换模型照样能出片」）。
> 已落盘来源（全部在 `D:/Project/Designers_Brain/`）：
> - `templates/determinism_contract.md`（C1–C10 + ①b 乱序重渲 + 自查命令）
> - `templates/style_card.md` v0.2（四段卡 / 输出规格块 / 评审步骤 / 6 关键帧落地）
> - `research/agent-art/cards/structure.md`（15 卡骨架蒸馏：4 段 + 页头提示）
> - `research/agent-art/cards/mg-styles-15_handbook.md`（参考实现管线手册 B-13）
> - `research/agent-art/cards/author_tutorial.md`（两智能体分工 / 三句话 / 只换内容不动骨架）
> - `research/agent-art/cards/video_shotcraft.md`（判例式规则 / 镜头卡 / 验收工程）
> - `research/agent-art/html/workflow.md`（HTML 逐帧管线与自查五件套 B-02）
> - `research/experiments/anim_test_01/checks.md`（B-07 端到端实测：非 Opus 模型真跑一支片）
> - `research/agent-art/cards/review_rubric.md`（7 维评审表）
> 证据分级沿用本项目：`[实测]`/`[史料]`/`[研究]`/`[归纳]`/`[推测]`/`[UNVERIFIED]`；引文均带来源路径与节号，可回查。
> 用法：**7 节各自独立**，每节内的 ```text/```bash 块可直接复制；不确定从哪读起就先读 §1。

**这套本领的可迁移内核（四件资产，模型换了它们不变）**
1. **卡**（`templates/style_card.md`）：任务头 / 画风段 / 内容段 / 反约束段——风格以「可逐帧自查的量化规则」形式存在，不依赖模型记忆。
2. **契约**（`templates/determinism_contract.md`）：帧=时间的纯函数；让「同一提示词每次出片不同」这个模型通病无处发生。
3. **管线**（`research/agent-art/html/workflow.md` + `harness/render.mjs` 等价物）：seek 化渲染页 → 无头逐帧捕获 → ffmpeg 合成 → 机械自查。
4. **验收**（`review_rubric.md` 7 维 + 乱序重渲 P0）：把「好不好」拆成机器能判的部分（先）和评委才能判的部分（后）。
> 已证：B-07 用非 Opus 模型按第 11 张卡（像素风）端到端产出 300 帧 / 10.000 s / 24 色 / 含合成音轨的成片，画面渲染→成片约 21 s（`research/experiments/anim_test_01/checks.md` 结论行 + §9）。未证：其余 14 张卡的端到端；跨机器位级一致（同上 §11）。

---

## 1. 一页版「怎么开始」（给人类）

**前提（一次装好）**：Node ≥ 20（B-07 实测 v24.19.0）｜`npm i puppeteer-core`（无头浏览器用 puppeteer 缓存里的 chrome-headless-shell，或用环境变量 `CHROME_BIN` 指定；仓库 harness 用 `MG_CHROME`）｜ffmpeg/ffprobe 在 PATH（B-07 实测 n9.0.1）｜可选 Python+numpy+Pillow（跑机械自查脚本）。依据：`checks.md` §9 环境行；`handbook` §6.2-1（`MG_CHROME` 默认是 macOS 路径，Windows 必须显式指定）。

**三条命令**（在渲染工程目录内执行；数字为 B-07 实测耗时，见 `checks.md` §9）：

```bash
# ① 6 张关键帧 —— 先给人看，通过才做全片（0.7 s）
node render.js --keys          # → key/k0000.png … k0250.png（B-07 锚点 0/50/100/150/200/250）
                               #   推荐锚点 0/45/90/150/225/285，末帧必须含收尾文案（style_card v0.2）

# ② 全片 300 帧 + 合成音轨（18.3 s + 0.5 s）
node render.js --frames && node render_audio.js   # → frames/f0000…f0299.png + audio/score.wav

# ③ 出片（1.4 s + 0.3 s）
ffmpeg -framerate 30 -i frames/f%04d.png -i audio/score.wav \
       -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -shortest out.mp4
```

**一段模板**（把下面整段发给任何能写代码的 agent；`【】`里换成你的；填写规则全文见 `templates/style_card.md` v0.2）：

```text
用代码做一支 10 秒的 MG 动画（1920×1080，30 帧），网页逐帧渲染，配乐音效也用代码合成、跟画面卡点；先出 6 张关键帧给我看，再做动画，最后逐帧自查。
画风：【名字】。【4-8 条可判定规则：角度/线宽/色数/缓动/过冲幅度/回弹帧数/动作最短时长/同屏颜色数/像素栅格…每一条都必须能被逐帧机械核对，形容词换成数字或物理描述】
内容：【10 秒分镜，含结尾落地文案（收尾字/标题 = 一帧能核对的验收锚点）】
别做成：【3-4 条，每条封堵一个模型默认退化行为：交叉淡化冒充形变 / 默认塑料材质 / 硬阴影 / 运动模糊滥用 / 淡入淡出转场 / 发光字 / 细字体 / 半像素位置 / 互补色 / 多个强调色…】
```

**跑完先看这三样**：① 6 关键帧拼图（3×2，左上→右下按时间）里是不是 6 个不同画面；② 乱序重渲 SHA256 是否全等（§7.1 第 ① 条）；③ 末帧有没有收尾文案（`f0269→f0270` 那种「先 0 像素、后出现并保持」的锚点，`checks.md` §5）。

**来源**：`research/experiments/anim_test_01/checks.md` §2/§5/§9；`templates/style_card.md`（任务头句式、6 关键帧落地）；`research/agent-art/cards/structure.md` §1。

---

## 2. 给 agent 的系统提示词模板

**用法**：把主模板整段粘进系统提示词（或会话第一条消息），紧接风格卡全文。`<…>` 是槽位。卡的四段与 Output 规格块（`templates/style_card.md`）原样附后，不要删 `Signature features` 那一段（作者原话：「像风格那些的话就别动，那个的话是视频的灵魂」，`author_tutorial.md` 第 9 条，t0062–t0066）。

### 2.1 主模板（完整版，直接复制）

```text
你是「代码作画」动画的导演兼实现者。任务：把 <风格卡全文> 变成一支 10.000 s / 300 帧的 MG 动画
（1920×1080 @ 30 fps，H.264 MP4 + 立体声 AAC；规格以卡内 Output 段为准）。

# 工作流程（不许合并、不许跳步）
1. 读卡：复述画风段每条规则，并给每条规则配一句「怎么被逐帧自查」的计划。
2. 关键帧先行：只实现 6 个关键状态（0/45/90/150/225/285 帧），渲 6 张 PNG，拼 3×2 contact sheet；
   到此暂停等我确认（人类评审点是硬停，不许直接做全片）。
3. 全片实现：补间/物理全部表达为帧号的纯函数 f(frame)；音轨用代码合成，事件表与画面共用一张 cue 表。
4. 机械自查（先机械后人工，顺序不许倒）：帧数=300、时长=10.000000 s、画风段的量化项（色数/块结构/网格）、
   乱序重渲 SHA256 全等、无意外静止段、响度 ≈ −14 LUFS ±1 且真峰 ≤ −1 dBTP。
5. 交付：video.mp4 ｜ 6 关键帧 + 3×2 contact sheet ｜ cue 表 ｜ 全部源码 ｜ CREDITS.md（每项素材来源与许可）
   ｜ 自查报告（命令 + 结果原样粘贴）｜ 短报告（概念两句话 + 每条画风规则的落点 + 自评 top-3 弱点）。

# 硬条款（确定性，逐条执行）
Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only;
physics and particles precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions.
A reliable route: a web page that can draw any time t on request, captured frame by frame with a headless
browser and encoded with ffmpeg (or a Blender script that renders a PNG sequence).
展开条款（C1–C10）与自查命令：见附后的确定性契约（templates/determinism_contract.md）。

# 自查义务（stop 条件）
任何一条自查没跑过 = 未完成。报告里只许写你真跑过的命令；没跑过的标 [UNVERIFIED]。缺 CREDITS.md 或缺自查报告 = 未交付。

# 禁止
Date.now / performance.now / requestAnimationFrame 参与动画时钟；Math.random（只用播种 PRNG，如 mulberry32）；
状态触发的 CSS 过渡；录制音频冒充「代码合成」；真实品牌商标（编造名字）；不可商用素材（未记入 CREDITS.md 的素材 = 不许用）。
```

### 2.2 压缩版（短上下文 / 小模型用，功能等价）

```text
你负责做一支 10 秒 MG 动画（1920×1080@30fps，300 帧，H.264+AAC）。规则：
① 帧=时间的纯函数：页面暴露 window.renderAt(t)（或 window.seek(frame)），禁 Date.now/performance.now/rAF 时钟、禁 Math.random。
② 先渲 6 关键帧（0/45/90/150/225/285）给我看，通过才做全片；末帧必须含收尾文案。
③ 音频代码合成，和画面共用一张 cue 表（事件时间 = 帧号/30）。
④ 完成后必跑并贴出：帧数=300、时长=10.000000s、乱序重渲同帧 SHA256 全等、色数/块结构符合画风段。
⑤ 没跑过的检查标 [UNVERIFIED]；缺自查报告 = 未交付。
画风规则与内容（照抄，不许改风格段）：<粘贴卡的画风段 + 内容段 + 别做成段>
```

**要点说明**（为什么这样写）
- 「自查义务 = stop 条件」来自 vsc 的验收工程：把「自查」从口号变成 agent 的停止条件，「不跑不算完成」（`video_shotcraft.md` 借 5；`style_card.md`「缺自查报告 = 未交付」）。
- 「先机械后人工」的顺序来自 `determinism_contract.md` §3 末行；关键帧硬停来自 15 卡任务头原文（`structure.md` §1）。
- 写死「300 帧 / 10.000000 s」是因为这是统一比较单位；卡内声明了别的规格（24 fps、竖屏）以卡内为准，但「exactly 10.000 s」与响度/真峰两条不放松（`style_card.md` 输出规格块注）。
- 短上下文模型：一次只喂一张卡（单卡 7.4–8.2 KB，`handbook` §1.1），用完即弃，别把 15 张一起塞（渐进披露，vsc SKILL.md 路由表思路）。

**来源**：`research/agent-art/cards/video_shotcraft.md` §4（借 5）；`templates/determinism_contract.md` §1；`templates/style_card.md`（确定性条款、输出规格块）；`research/agent-art/cards/author_tutorial.md` §3 第 9 条。

---

## 3. 两智能体分工模板（A 导演改写 / B 执行出片）

**分工图**（作者方法论原文：智能体 A「听懂你的业务 / 重写提示词」，智能体 B「跑命令 / 直接出片」——`author_tutorial.md` §4.1 卡 t0042、§3 第 5 条）：

```
你的业务信息 ──(三句话)──► 智能体 A（对话型，可不跑命令：扮演导演，重写提示词）
                                     │ 重写稿（只换内容，不动骨架）
                                     ▼
                            智能体 B（能跑命令的 agent，如 Codex / Claude Code / Hermes）
                                     │ 按 §2 工作流程出片 + 自查
                                     ▼
                                成片 + 自查报告 ──► 人类评审 / §7 独立评审
```

### 3.1 三句话填空（发给 A 的第一段，直接复制）

```text
① 我是做什么的：<业务 / 产品 / 身份，一句话讲清楚>
② 这支片子给谁看：<受众 + 场景，一句话讲清楚>
③ 手上有什么物料：<文件 / 图片 / 文档 / 现成文案，列路径或内容>
```

（作者原话逐字：① 你是做什么的——业务讲清楚；② 这个视频给谁看——场景讲清楚；③ 手上有什么物料——文件/图片/文档。`author_tutorial.md` §4.1 t0050。）

### 3.2 智能体 A · 导演改写提示词（直接复制）

```text
你扮演导演。上面三句话是我的业务信息。
任务：把下面的《原风格卡》重写成「我的业务版」提示词。
铁律——只换内容，不动骨架：
  ✅ 可换：Creative seed —— 故事 · 品牌（编造的名字）· 文案 · 配色
  🔒 不动：Signature features（风格骨架 = 视频的灵魂）、Output 规格、Rules 确定性条款、别做成（反约束）段
输出：① 重写稿全文（可直接投喂给执行方，不许留占位符）；② 一张「换 / 不动」对照表，逐条列出你改了什么、为什么；
③ 若某条反约束与新内容冲突（例如新配色撞上「同屏 ≤3 色」），标明冲突并给出你的处置。

《原风格卡》：
<粘贴卡全文：任务头 + 画风段 + 内容段 + 别做成 + 输出规格块 + 确定性条款>
```

### 3.3 智能体 B · 执行出片提示词（直接复制）

```text
你负责执行出片。输入：一份重写好的提示词（见下），环境：Node + Chrome(headless) + ffmpeg。
按「§2 工作流程」执行：读卡 → 6 关键帧（先给我看，硬停）→ 全片 → 机械自查 → 交付清单。
额外要求：每完成一步，把命令与输出原样贴回；6 关键帧未经我确认，不许开始全片渲染。
不许改动重写稿里的风格段 / 规格段 / 反约束段（要改必须先说明理由并等我确认）。

《重写稿》：
<粘贴 A 的输出>
```

**「只换内容，不动骨架」对照表**（作者卡片逐字，`author_tutorial.md` §4.1 t0064）：

| | 换 | 不动 |
|---|---|---|
| 术语 | Creative seed | Signature features |
| 内容 | 故事 · 品牌 · 文案 · 配色 | 风格骨架（一眼认出这种风格的依据） |
| 本体系对应 | 卡的第 3 段「内容段」 | 第 2 段「画风段」+ 第 4 段「反约束段」+ Output/Rules |

**作者为什么强调二次开发**：6000 字英文原稿「拿在手里 ≠ 会用」（t0092）——迁移指南的意义就是把「重写成业务版」变成模板化动作。核对依据：`author_tutorial.md` §3 第 12 条；`research/agent-art/cards/mg-styles-15_compare.md` §3（15/15 同源，MIT 边界）。

**来源**：`research/agent-art/cards/author_tutorial.md`（§3 第 5/7/8/9/10/12 条，帧号 t0042–t0092）；`templates/style_card.md`（四段结构与「内容段=可换」）。

---

## 4. 确定性契约最小集（必须条款 vs 可选条款）

**级别判定表**（条款全文见 `templates/determinism_contract.md` §1；「机械自查」列 = 该条款能否不靠人眼验证）：

| 条款 | 级别 | 为什么 | 机械自查方式 | 来源 |
|---|---|---|---|---|
| C1 READY/DEMO/renderAt | **必须** | 没有这个接口就没有「逐帧」可谈 | 页面全局量存在 + `__ready` 在字体就绪后置位 | contract §1/§4 |
| C2 帧 = 时间的纯函数 | **必须** | 一切重渲/回归的基础 | 乱序重渲 SHA256 全等 | contract §3①b；checks.md §6 |
| C3 禁壁钟 | **必须** | rAF 帧率随机器变（60/75/120/144 Hz） | 代码审计：grep `Date.now`/`performance.now`/`requestAnimationFrame` | workflow §1（MDN） |
| C4 播种随机 | **必须** | 未播种随机 = 每次出片不同 | grep `Math.random` 命中数 = 0 | prompts/01 Rules |
| C5 CSS/WAAPI 可 seek | **必须**（用了 CSS 动画时） | 状态触发过渡不可复现 | 捕获端统一 `pause(); currentTime = t*1000` | render.mjs `seek()` |
| C6 单表双读（cue 表） | **有音频则必须** | 音画同源卡点；1470 采样/帧整数对齐 | cues.json 存在且画面/声音两处消费 | prompts/01:57；workflow §3 |
| C6′ 音频「代码合成」 | 可选（路线） | 15 卡口径；CC0 采样库/录制音效库（记许可）亦成片 | — | handbook §3.5；vsc §3.7 |
| C7 输出规格 | **必须**（10.000 s / 300 帧 / 可解码）；分辨率/帧率按卡 | 统一比较单位 | `ffprobe -count_frames`=300；`duration`=10.000000 | template.md |
| C8 素材许可 / 无真品牌 / CREDITS | **必须** | 法务 + 封堵「AI 模板感」 | CREDITS.md 存在；grep 真实商标 | prompts/01 Rules 2–3 |
| C8′ 许可白名单（CC0/OFL/Apache…） | 推荐收紧 | 本项目口径；可放宽为「可商用 + 记录」 | 逐条核对 CREDITS.md | 同上 |
| C9 Blender 等价条款 | 可选（路线） | 仅 3D/物理/材质卡用 | 帧序列 + 物理数据文件存在 | compare §3.2 |
| C10 关键帧先行 | **必须**（流程） | 低成本早期检查点 | 6 张 PNG + 拼图存在，且两两不同 | 15 卡任务头 |
| ①b 乱序重渲 | **必须**（自查） | 同序重渲漏跨帧状态泄漏（f0150 实测差 158 源像素） | 倒序/随机抽帧重渲 → SHA256 全等 | contract §3①b；checks.md §6 |
| 运动模糊（MB× 时间超采样） | 可选 | 成本 ×MB；确定性做法 | — | handbook §2.4 |

### 4.1 最小条款块（英文，直接粘进提示词；从 C1–C10 截取）

```text
Deterministic rendering contract (minimum set, mandatory):
C1. Page contract (READY/DEMO): before setting window.__ready = true, the page defines
    window.DEMO = { width, height, fps, duration }   // optional overrides of the CLI defaults
    window.renderAt = async (t) => { ... }           // draw the frame for time t (seconds)
    and sets window.__ready = true only after assets and fonts are loaded (document.fonts.ready).
C2. Every frame is a pure function of time t: the same t must produce the same pixels, any run, any machine.
C3. No real-time clocks: Date.now / performance.now / requestAnimationFrame must never drive the animation.
    The only time source is the frame number: t = frame / fps.
C4. Seeded randomness only (e.g. mulberry32): never Math.random(); physics and particles are precomputed or
    closed-form, never integrated against a wall-clock dt.
C5. No state-triggered CSS transitions; CSS animations / WAAPI must be seekable: pause() each animation, then
    set currentTime = t * 1000 (the capture harness does this automatically for anything not driven by renderAt).
C7. Output spec: 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz),
    mastered to −14 LUFS integrated, true peak ≤ −1 dBTP. Final file: video.mp4.
C10. Stills before motion: render the 6 key times first, the last still contains the end copy; full render only
    after the stills pass human review.
```

### 4.2 P0 自查块（乱序重渲，跑不过不算完成）

```bash
node render.js --rerun 299,150,0     # 逆序重渲 3 帧 → checks/rerun/
python checks/selfcheck.py           # 比对 SHA256：f0000/f0150/f0299 必须 IDENTICAL
# 全片版本（可选）：两次全渲后
ffmpeg -i out.mp4 -i out_rerun.mp4 -lavfi "psnr=stats_file=checks/psnr.log;ssim=stats_file=checks/ssim.log" -f null -
```

**为什么必须乱序**：B-07 实测——`drawCloud()` 把打包整数赋给 `ctx.fillStyle`，非法值被浏览器静默忽略、沿用上一帧状态；同序重渲看不出来，逆序重渲 f0150 差 158 源像素。修法：颜色改 `HEX.*` 字符串 + `seek()` 开头显式重置 `fillStyle`。修后 3/3 帧 IDENTICAL（`checks.md` §6）。

**来源**：`templates/determinism_contract.md` §1–§4；`research/experiments/anim_test_01/checks.md` §6/§12；`research/agent-art/html/workflow.md` §5；`research/agent-art/cards/mg-styles-15_handbook.md` §2.1。

---

## 5. 常见坑清单（开工前读一遍，出问题先查这里）

| # | 坑 | 现象 | 处置 | 证据（路径 + 数字） |
|---|---|---|---|---|
| 1 | 同序重渲 ≠ 确定性 | 同序重渲一致，乱序不一致 | P0 必须**乱序重渲**（倒序/随机抽帧）+ SHA256 | `checks.md` §6：f0150 差 158 源像素 |
| 2 | 非连续帧号拼图 | `-i key/k%04d.png` 只读第 1 帧 → 拼出 1 格图 | 连续编号，或 `-f concat -safe 0 -i list.txt`（`file`+`duration 1` 交替，末行重复最后一个 file） | `style_card.md`「6 关键帧落地」；`checks.md` §4 |
| 3 | image2 缺省 25 fps | 300 帧被拉成 12 s | 显式 `-framerate 30` | `workflow.md` §2（ffmpeg 文档原文 defaults to 25） |
| 4 | `-pattern_type glob` 不可用 | 报 `globbing is not supported by this libavformat build` | 别用 glob；用连续编号或 concat | `determinism_contract.md` 附录 B2 |
| 5 | 浏览器字体抗锯齿破坏色数 | 调色板外冒出大量灰阶 → 16-32 色硬指标失败 | 自绘点阵字（16×16 GLYPH 表）或像素字体 | `checks.md` §5/§12-B4；`handbook` §6.3-3 |
| 6 | 色数口径混淆 | 拿 h264 成片解码帧数色（上万色）去比源帧 PNG（24 色） | 只对无损源帧数色；与参考片对照必须注明口径 | `checks.md` §10 第 1 条 |
| 7 | 色数计数范围 | 材质/高光层把「≤N 色」撑爆 | N6 口径：色数上限只约束**平涂色块层**；金属/高光层单列、≤5% 画面、卡内声明 | `style_card.md` 组合卡注记 N6 |
| 8 | 半像素 / 插值放大 | 最近邻 ×6 放大暴露 12px 双色块 | 所有坐标取整；`imageSmoothingEnabled=false`；`deviceScaleFactor=1`；`--disable-lcd-text` | `workflow.md` §1；`checks.md` §3 块结构 200/200 |
| 9 | ffmpeg n9 无 `-vsync` | 旧命令直接报错 | 改 `-fps_mode` | `checks.md` §4 |
| 10 | PowerShell `%` 歧义 | `f%04d.png` 被当别名解析 | 用 bash/cmd，或给文件名加引号 | `workflow.md` §2 注 |
| 11 | 参考 harness 默认 Chrome 路径是 macOS | Windows 找不到浏览器 | 仓库 harness 用 `MG_CHROME`；本地骨架用 `CHROME_BIN` | `handbook` §6.2-1；`render.js:16` |
| 12 | 跨机器不承诺 | 同帧跨机/跨 Chrome 版本像素不同（GPU 光栅/颜色管理） | 锁浏览器版本 + `--disable-gpu`；P0 只承诺同机同参 | `checks.md` §11；`workflow.md` §5-B1（WEAKENED） |
| 13 | 把 10 Hz 离散当卡帧 | `freezedetect` 报「静止段」 | 那是「每秒 8-12 张、不做补间」的正常外观；改用零差分帧分布核对 | `checks.md` §7/§12-B5（40% hold 设计使然） |
| 14 | 音频位级复现期望 | 重跑 LUFS/波形微差 | 验收按 QC 数值（LUFS/真峰/onset），不按位级一致 | `handbook` §3.4（README:134，11/15 有差异） |
| 15 | 字体本体不在参考库 | `assets/fonts/` 只有 44 个路径，无字体文件 | 自备字体并逐条核许可（OFL 等） | `handbook` §6.2-3 |
| 16 | 凭卡名重写参数 | 调校过的数值全丢，回到模型默认 | 三读链：解析卡名 → 读卡全文 → 读准确 demo 源码 → copy；「已知坑/命门」参数只升不降 | `video_shotcraft.md` 借 3 |
| 17 | 改截图糊弄 | 关键帧没过就美化截图 | 不过就改 `seek()` 重渲，不许改截图 | `workflow.md` §4 |

**贴给 agent 的坑位清单**（直接复制，接在 §2 模板之后）：

```text
出片前牢记这 7 条（其余见 transfer_guide.md §5）：
1. 拼图/序列合成：image2 缺省 25fps，必须 -framerate 30；非连续帧号拼图用 concat 清单，别用 %04d。
2. 确定性 P0 = 乱序重渲（倒序/随机抽帧）SHA256 全等；同序重渲会漏跨帧状态泄漏。
3. 像素风文案用自绘点阵字；浏览器字体抗锯齿会产生调色板外灰阶。
4. 色数只数无损源帧 PNG；色数上限只约束平涂色块层（材质/高光单列 ≤5% 并声明）。
5. 所有坐标取整 + 最近邻放大 + deviceScaleFactor=1；半像素会被放大暴露成双色块。
6. Windows：MG_CHROME / CHROME_BIN 必须显式指向 chrome.exe；PowerShell 里 % 要用引号。
7. 10 Hz 离散动画出现连续重复帧是设计使然，不是丢帧，不要「修」它。
```

**来源**：`research/experiments/anim_test_01/checks.md` §3/§4/§5/§6/§7/§10/§11/§12；`research/agent-art/html/workflow.md` §1/§2/§4/§5；`templates/style_card.md`（6 关键帧落地、组合卡注记）；`templates/determinism_contract.md` 附录；`research/agent-art/cards/video_shotcraft.md` §3.4/§4。

---

## 6. 模型适配矩阵：能力档 → 退化路径与替代方案

**判定两个轴**：会不会**读图**（能看图/截图/contact sheet）｜会不会**跑命令**（有 shell/文件系统，能执行 Node/ffmpeg）。四档及路线：

| 能力档 | 典型环境 | 可行路线 | 退化路径（能力缺什么就换什么） | 替代方案 / 补强 |
|---|---|---|---|---|
| **T1 会读图 + 会跑命令 + 会写文件** | Claude Code / Codex / omp 带视觉 | 全循环：写码 → 渲关键帧 → 看图改 → 全片 → 机械自查 → 自审 contact sheet | 无能力退化；风险只在审美与细节 | 判例式规则 + 参考实现 copy（vsc 借 1/3）；本档是 B-07 验证过的档位 |
| **T2 会读图，不会跑命令** | 网页对话（可传图） | agent 写**全部源码 + runbook**；人类跑命令、把图与输出贴回 | 「agent 跑自查」→「人类跑、agent 判」 | 用 §6b 回传协议；机械数字由人类粘回，agent 只做判读 |
| **T3 不会读图 + 会跑命令** | 纯文本编码 agent | 用**数字断言代替看图**（§6a）；审美判断外包给人类或 T1 评审 | 不能自评构图/美丑；只能保「机械达标」 | 关键帧交人类看图；选机械可查的卡（像素类）；评审委托（§7） |
| **T4 都不会** | 纯文本对话 | 产出重写稿 + 源码 + runbook；**全部标 [UNVERIFIED]** | agent 无法验证任何东西 | 两智能体分工（§3）：T4 干 A 的活，B 用 T1/T3 出片 |

**退化策略三条**（[归纳]，依据见各来源）
1. **能力越弱，越选「机械可查」的风格**：像素卡（块结构/色数/点阵字/离散姿态全部可数）是 B-07 已证的最稳档位；液体/玻璃/材质类需要视觉判断的卡留给 T1/T2（`checks.md` §3/§7；`structure.md` §1 渲染器二选一）。
2. **调校积累放代码资产，不放模型记忆**：卡指向参考实现；换任何模型都吃同一份真相（`video_shotcraft.md` 借 3；`handbook` §6.1-1）。
3. **预算前置**：单卡 7.4–8.2 KB、harness 约 17 KB、全片逐帧截图 ≈ 60 ms/帧（300 帧 ≈ 18 s + 浏览器启动）（`handbook` §1.1；`checks.md` §9）——T2/T4 档一次只处理一张卡、一段管线。

### 6a. 「不会读图」的机械断言清单（直接复制；替代「用眼睛看」）

```text
我没有眼睛，用数字代替看图。每支片完成后必须全部跑过并贴出：
- 帧数：ffprobe -count_frames → 必须 300
- 时长：format=duration → 必须 10.000000
- 块结构：每 6×6 输出块单色（抽样 200 块全过）→ 证明是最近邻放大而非插值
- 色数：全片并集落在画风段声明的区间内（像素卡示例 [16,32]）且「调色板外颜色 = 0」
- 关键帧两两不同：6 张两两差异像素数均 > 0（证明不是同一帧复制）
- 文案锚点：末帧文案 bbox 内非底色像素数 > 0，且出现前为 0（例：f0269=0 → f0270 起出现并保持）
- 乱序重渲：3 帧 SHA256 全等
任一不达标 → 不许说完成；不达标项写进报告，不许静默跳过。
```

### 6b. 「不会跑命令」的回传协议（直接复制；给人类操作者）

```text
我不在你的机器上执行命令。请你按顺序跑以下命令，并把输出原样贴回：
1) node render.js --keys            → 贴回 key/ 的 6 张图 + 拼图 keyframes_sheet.png
2) node render.js --frames && node render_audio.js
3) ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 out.mp4
4) python checks/selfcheck.py       → 贴回全文（含 SHA256 比对结果）
5) node render.js --rerun 299,150,0 → 贴回输出 JSON（确认 3 帧重渲无报错）
我依据你贴回的数字与图做判断；我给出的每条结论都会注明「基于第 N 条输出」；
未贴回的检查我一律标 [UNVERIFIED]，不猜。
```

**来源**：`research/agent-art/cards/video_shotcraft.md` §3.2/§3.5/§4（借 3/5/8）；`research/agent-art/cards/author_tutorial.md` §3 第 5/10 条（A=对话型 / B=能跑命令）；`research/experiments/anim_test_01/checks.md` §3/§5/§6/§9；`research/agent-art/cards/mg-styles-15_handbook.md` §1.1/§2.2。

---

## 7. 验收与迭代（6 关键帧 → 片 → 乱序重渲 → contact sheet → 独立评审）

**顺序不许倒**：先机械后人工（`determinism_contract.md` §3 末行）；每轮改动后整片重渲再回看（vsc 阶段 5 做法）。

### 7.1 验收命令清单（直接复制）

```bash
# ① 确定性 P0（乱序重渲！）
node render.js --rerun 299,150,0
python checks/selfcheck.py     # 块结构 / 色数 / 关键帧两两差异 / 文案锚点 / SHA256

# ② 规格
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 out.mp4  # 期望 300
ffprobe -v error -show_entries format=duration -of csv=p=0 out.mp4                                          # 期望 10.000000
ffmpeg -i out.mp4 -af loudnorm=print_format=json -f null -                                                   # input_i ≈ −14±1；input_tp ≤ −1

# ③ 审片 contact sheet（300 帧 → 每秒 6 帧 → 10×5 网格）
ffmpeg -i out.mp4 -vf "fps=6,scale=384:-1,tile=10x5:padding=4:color=#101010" -frames:v 1 checks/sheet.png

# ④ 意外静止段（对连续动画；离散 10Hz 动画改用「零差分帧分布」核对，见 §5 坑 13）
ffmpeg -i out.mp4 -vf "freezedetect=n=-60dB:d=0.5" -map 0:v -f null -
```

### 7.2 独立评审（另开会话；完整提示词直接复制 `review_rubric.md` §1）

```text
你是一位资深动态设计评委（对标：Motionographer 编辑、Buck / ManvsMachine 创意总监、抖音/B站顶级设计账号主理人）。
片子不是你做的。请严厉且精确地评审，目标是入围奖项 / 高端商业水准。客气无用，具体才是一切。
成片：<video.mp4 路径>；它用的提示词：<粘贴风格卡>；制作方的机械自查报告：<粘贴 7.1 的输出>。
1. 先认真看片：contact sheet（每 0.5 s 一帧）、最快/最重要动作段 filmstrip、5–8 个关键时刻的全分辨率帧。
2. 核规格：恰好 10.00 s / 分辨率帧率 / −14 LUFS ±1 / ≤ −1 dBTP / 无意外静止段 / 命中点与音频 onset 对齐。
3. 7 维 1–10（5=学生、6=模板、7=专业、8=一线、9=入围、10=最强；首轮大多 5–7，Do not inflate）：
   style_fidelity / concept_wow / motion_craft / design_typography / finish_texture / sound_sync / technical。
4. 给 5–10 条按时码排序的修复（现象 + 为什么重要 + 具体怎么做）；至少一条抬 wow 因子。
5. critical 一票先修：generic/AI 模板感、中文文案不自然、fallback 字体/豆腐块、规格失败。
输出：评分表、critical 问题、修复清单。
```

### 7.3 修改轮（贴回制作会话，直接复制）

```text
一位独立评委评审了你的片子，完整评审如下：<粘贴评审>
把片子提升到入围奖项水准（每个维度目标 ≥9）：
- 先把当前成片与源码存为版本 N。
- 逐条落实 critical 与高影响修复；更好的解法可替换清单里的做法，但必须说明理由。
- 评委列为优点的地方不许回退；清单之外看到更大的升级（尤其 wow）也做。
- 全分辨率重渲，重核规格与 7.1 全部命令，直到修复真正落地。
- 报告落实 / 跳过了哪些修复，以及为什么。
```

### 7.4 迭代留痕规则（防「重来一遍」）

- **验收帧写死在计划里**：每个关键状态/镜头预先写死 1–2 个验收帧号，做完立刻静帧核对（vsc 阶段 5；本体系 = 6 关键帧 + 末帧文案锚点）。
- **版本 N 存档 + 落实/跳过报告**：每轮评审修改前存档，修改后报告逐条落实状态（`review_rubric.md` §3；`handbook` §5.2）。
- **判例回流**：某条规则被违反过，就按「规则 + 判例（用户原话/返工经过）+ 自检问题」三要素记一条，编号只追加不重排（`video_shotcraft.md` §3.4 判例式规则）。
- **节奏默认放慢**：「节奏宁慢勿快」有实证——vsc 全片六次独立反馈全部指向放慢，从未有一次「太慢了」（`video_shotcraft.md` §3.4 R3）；帧预算先划 hold 再排动效（同文借 7）。
- **首轮评分别膨胀**：首轮成片大多 5–7 分是正常区间（`review_rubric.md` §2 锚点）。

**来源**：`templates/determinism_contract.md` §3；`research/experiments/anim_test_01/checks.md` §2/§3/§5/§6；`research/agent-art/cards/review_rubric.md` §1–§4；`research/agent-art/cards/video_shotcraft.md` §3.4/§3.5/§4（借 5/7）；`research/agent-art/html/workflow.md` §4/§5。

---

## 附录 A · 来源路径索引（回查用）

| 路径 | 一句话内容 |
|---|---|
| `templates/determinism_contract.md` | C1–C10 条款 + ①b 乱序重渲 + 自查命令清单 + 条款↔来源对照 |
| `templates/style_card.md` | 四段卡模板 v0.2：任务头/画风/内容/反约束 + 输出规格块 + 评审步骤 + 6 关键帧落地 + 组合卡注记 N1/N3/N6 |
| `research/agent-art/cards/structure.md` | 15 卡骨架蒸馏：为什么「量化规则 + 反约束 + 三段流程」有效 |
| `research/agent-art/cards/mg-styles-15_handbook.md` | 参考实现管线手册：render.mjs 契约、音频引擎、Blender 6 步、抄/不抄清单、实测坑 |
| `research/agent-art/cards/author_tutorial.md` | 第三方教程拆解：两智能体分工、三句话、只换内容不动骨架（帧号可回查） |
| `research/agent-art/cards/video_shotcraft.md` | 同作者另一条产品线：判例式规则、镜头卡格式、验收工程、技能包打包（借 1–9） |
| `research/agent-art/html/workflow.md` | HTML/WebGL 逐帧管线：seek 化骨架、捕获三路径、ffmpeg 合成、自查五件套 |
| `research/experiments/anim_test_01/checks.md` | B-07 端到端实测：300 帧/24 色/乱序重渲抓 bug/耗时与命令 |
| `research/agent-art/cards/review_rubric.md` | 7 维评审表（评审 + 修改两段提示词，可直接复制） |

## 附录 B · 自审四段（LOOP 协议）

**A · 早产出**
先读齐 9 份来源（并行 read 分批）→ 直接落盘全文 v1.0（7 节 + 附录 A）→ 再跑回查命令补附录 B 的 C 段原样输出。中途核对：`render.js`/`package.json` 实读（确认 §1 三条命令的 CLI 真实存在）；`key/list.txt` 实读（确认 concat 清单格式为 `file`+`duration 1` 交替、末行重复）。

**B · 反驳**（逐条试推翻，命令与输出见 C）
1. 「§1 三条命令是本机真跑过的」→ 试推翻：命令来自 `checks.md` §9 转录，非本轮实跑（渲染工程归 AnimTest01，本轮不重跑）。→ **WEAKENED（已标注）**：改为「数字为 B-07 实测」并在 §1 注明出处；CLI 形式由 `render.js` 实读交叉验证（`--keys/--frames/--rerun` 与 `KEY_FRAMES` 数组均存在）。
2. 「乱序重渲差 158 像素」→ 试推翻：去 `checks.md` 与 `determinism_contract.md` 两处交叉 grep。→ **CONFIRMED**（两文件均命中，见 C-1）。
3. 「6 关键帧锚点 = 0/45/90/150/225/285」→ 试推翻：B-07 实际用 0/50/100/150/200/250（`render.js` `KEY_FRAMES`），与 style_card 推荐锚点不同。→ **WEAKENED（已在 §1 并列写明两套锚点）**；「末帧必须含收尾文案」在 B-07 由独立验收补上（f0269=0 → f0270 起出现）。
4. 「B-07 交付物确实 300 帧」→ 试推翻：直接数盘上文件。→ **CONFIRMED**（`frames/f*.png` = 300；`key/*.png` 现为 13 = 6 原始 + 6 带标签 + 1 拼图，与 `checks.md` §2 当时记录的 7 张（无 lbl_*）之差已核对为后续补的标签图，见 C-3）。
5. 「§6 四档矩阵的分档依据」→ 试推翻：A/B 两智能体「对话型 vs 能跑命令」是作者原话（t0042/t0072），「会读图」轴为本指南新增划分。→ **CONFIRMED（作者原话）+ [归纳]（读图轴为本指南归纳，已在正文标注）**。

**C · 机械验证**（原样输出，2026-10-15）

```
C-1 乱序重渲 158 像素双源交叉（grep 原样输出）：
$ grep -n "158" templates/determinism_contract.md research/experiments/anim_test_01/checks.md
templates/determinism_contract.md:94:- ①b 乱序重渲（必做，属 P0）：同序重渲会漏「跨帧状态泄漏」（如 `fillStyle` 被赋非法值 → 浏览器静默忽略 → 沿用上一帧状态）；乱序抽帧重渲（如 `--rerun 299,150,0`）逐帧比 SHA256 期望全一致——B-07 实测 f0150 曾差 158 源像素，修复后 3/3 帧一致（2026-10-15）。
research/experiments/anim_test_01/checks.md:148:- **这条检查抓到了一个真 bug（本次实验最重要的实测收获）**：`drawCloud()` 里曾把打包好的 `PAL32` 整数直接赋给 `ctx.fillStyle`——非法 CSS 值会被浏览器静默忽略、沿用上一次的样式，于是云的配色取决于**上一帧**遗留状态：同序重渲看起来一致，逆序/乱序重渲就变色（实测 f0150 差 158 个源像素）。修法两条：① 云的配色改用 `HEX.*` 字符串；② `seek()` 开头显式 `g.fillStyle = HEX.ink0` 清状态。修完 3 帧全 IDENTICAL。→ 回填 `workflow.md` §5 的建议：**P0 检查必须乱序重渲**，同序重渲会漏掉状态泄漏类 bug。

C-2 CLI 交叉验证（grep render.js 原样输出，节选）：
$ grep -n "KEY_FRAMES\|--rerun\|--keys" research/experiments/anim_test_01/render.js
5:     node render.js --keys              # 6 张关键帧 0/50/100/150/200/250 -> key/
8:     node render.js --rerun 0,150,299   # 重渲同帧 -> checks/rerun/（确定性 P0 检查）
18:const KEY_FRAMES = [0, 50, 100, 150, 200, 250];
$ grep -n "CHROME_BIN" research/experiments/anim_test_01/render.js
16:const EXE = process.env.CHROME_BIN ||

C-3 盘上文件计数（独立重 derive B-07 关键数字）：
$ ls research/experiments/anim_test_01/frames/f*.png | wc -l
300
$ ls research/experiments/anim_test_01/key/*.png | wc -l
13          （= 6 张原始关键帧 k*.png + 6 张带标签 lbl_*.png + 1 张 keyframes_sheet.png）
$ stat -c %s research/experiments/anim_test_01/out.mp4
2140784

C-4 环境（本机）：
$ node --version
v24.19.0
$ ffmpeg -version | sed -n '1p'
ffmpeg version n9.0.1-11-ge47273f4d9-20260828 Copyright (c) 2000-2026 the FFmpeg developers

C-5 本文块结构计数：
$ grep -c '^```' research/agent-art/transfer_guide.md
34          （= 17 个可复制块：text/bash 围栏各计一对）
$ grep -c '^## ' research/agent-art/transfer_guide.md
9           （7 节 + 附录 A + 附录 B）

C-6 验收口径「抽 2 个来源路径回查」的两次实抽（grep 原样输出，节选）：
$ grep -n "0 / 45 / 90 / 150 / 225 / 285" templates/style_card.md
67:- 锚点帧（10 s / 30fps）：`0 / 45 / 90 / 150 / 225 / 285`（= 0 / 1.5 / 3 / 5 / 7.5 / 9.5 s）；**最后一帧必须含收尾文案**（一帧可核对的验收锚点）。
$ grep -n "f0269" research/experiments/anim_test_01/checks.md
110:frames/f0269.png: white(text) pixels in bbox = 0
133:- 出现时机：f0269 = 0 像素（无文案）→ f0270 起出现（先 1 帧 16px 小字，f0273 起放大 2× = 32px 字面，离散两档、无补间）→ 保持到 f0299（末帧）。
```

**D · 小结**（≤14 行）
1. 已落盘：`transfer_guide.md` v1.0，7 节 + 附录 A/B；每节含 ≥2 个可直接复制的文本块（全文 17 块，`grep -c '^```'` = 34）。
2. 已确立（有出处）：三命令快速开始（B-07 实测数字 + render.js CLI 实读）；最小契约 = C1–C5 + C7 + C10 + ①b（其余按路线）；17 条坑位均有来源与数字。
3. 已确立：乱序重渲 P0 与 158 像素判例在 `checks.md`（:148/:258）、`determinism_contract.md`（:94）多源一致；盘上 300 帧 / key 13 张 PNG / out.mp4 2,140,784 B 与 `checks.md` §1/§2 记录一致。
4. 分档矩阵：A/B 分工是作者原话；「读图轴」为本指南归纳，T2/T3/T4 的退化路径未做端到端实验 → 标 `[归纳]`。
5. 未做：其余 14 张卡的端到端；跨机确定性；T2/T4 档实操验证。缺口即后续实验点（B-07 模式复制到第二张卡）。
6. 回填建议：B-13 手册可收 §4.2 与 §5 的坑位表；B-11 卡模板可加「系统提示词模板」（§2）为配套件。
