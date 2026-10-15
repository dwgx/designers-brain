# mg-styles-15 溯源与逐条对照（B-10）

> 任务：读 GitHub 仓 `Vincentwei1021/mg-styles-15`（MIT，866★），与本地 15 卡（`research/origin_cards/` + `research/agent-art/cards/structure.md`）逐条对照——同源判定、工程体系拆解、MIT 复用评估、缺口。
> 方法：GitHub API（2026-10-15 实测）+ raw.githubusercontent 直读 + `git clone --filter=blob:none --sparse`（仅文本 3.2 MB）到 `%TEMP%` 只读分析；**未跑任何构建/渲染**。
> 证据分级：`[自述]`=仓库/作者自述；`[实测]`=本次 API/raw/克隆实读；`[归纳]`=本次总结；`[推测]`=推断；`[UNVERIFIED]`=未跑未核。
> 本地对照物：`research/origin_cards/提示词全文.md`（15 卡逐字转录，wave1）+ 16 张截图（`01_3D质感.png`…`16_片尾.png`，本次抽看 00/01/07/16）+ `cards/structure.md`（v0.1 结构蒸馏）。

## 0. 结论速览

1. **15/15 同源**：本地 15 卡与仓库 15 个风格一一对应；可判定规则与关键数字（2-3 帧、2-4 帧、8 帧、320×180、16-32 色、8-12 帧/秒、90°、30°、10%、±2px、3-4 版线稿、一拍二=12fps…）逐条吻合。本地卡是这套提示词体系的**中文压缩改写**：本地每卡约 200-280 字，仓库每条提示词 7.4-8.2 KB。`[实测]`
2. **成片不是同一批**：本地视频 15 支成片（《PLAY》《合》《图书馆还书》《午夜电台》《灵感》《3 分》《着陆》《山野骑行》《晴朗》《猫头鹰日报》《大丰收》《早安》《番茄的旅行》《水》《吐司机》）≠ 仓库 15 支成片（soft./drop./ISOPOLIS/NEON DRIVE/morphe./KONSTRUKTION/KESTREL-9/ATELIER LINEA/Aurora/NOGGIN/PIXEL QUEST/手作/popwise/手机元素/喵呜日记）。同风格体系、两次运行、不同 Creative seed。`[实测]`
3. **仓库 = 整条管线**：`prompts/`（15×6 段式提示词）+ `demos/`（15 支全源码，js+html 共 2.3 MB）+ `harness/render.mjs`（headless Chrome 逐帧捕获→ffmpeg）+ `lib/audio`（mgaudio 合成库 + 102 个 flac 采样）+ `rubric.md`（AI 评审两轮，终评 7.57-8.21/10）+ `template.md`（四段模板）+ `site/`（中英展示页）+ `videos/`（15 mp4，417.6 MiB）。`[实测]`
4. **本地 4 段卡 ≈ 仓库模板的压缩映射**：任务头≈Output+Route+How-to-work，画风段≈Signature features，内容段≈Creative seed，别做成≈Rules/Craft checklist 里的反约束（见 §3.3）。`[归纳]`
5. 压缩方向不能从本地证据判定；**视频作者身份未证实**（GitHub 主页只链 X/抖音，视频来自微信视频号）——见 §5 缺口。`[推测]`

## 1. 仓库结构与实测事实

### 1.1 元数据（GitHub API，2026-10-15）

| 项 | 值 |
|---|---|
| full_name | `Vincentwei1021/mg-styles-15` |
| description | 15 motion design styles, each made by Claude Opus 5.5 writing code from one prompt: watch the films, copy the prompts, read the full source. |
| default_branch / license | `main` / MIT（`spdx_id: MIT`，LICENSE 头：`Copyright (c) 2026 Vincentwei1021`） |
| stars / forks | 866 / 139（2026-10-15 实测） |
| size | 567916 KB ≈ 555 MiB（其中 `videos/*.mp4` 合计 417.6 MiB） |
| created / pushed / updated | 2026-10-02T09:43:06Z / 2026-10-05T11:23:17Z / 2026-10-15T07:23:31Z |
| language / homepage | Python / https://vincentwei1021.github.io/mg-styles-15/ |
| commits | 8（2026-10-02 09:43 → 10-05 11:23，中文 commit 信息） |

作者（GitHub API）：`login=Vincentwei1021, name=Yihao, bio="Machine Learning, Computer Science, Mathematics, Music"`；个人主页 README 链 X `@VincentWei93` 与抖音账号，并列出同作者项目 `video-shotcraft`（11,981★）/`anything2explainer`（2,507★）/`video-talkcraft`（1,589★）。`[实测]`

### 1.2 目录（git trees API，461 条，未截断）

| 路径 | 内容 | 规模 [实测] |
|---|---|---|
| `prompts/` | 15 条提示词（01-flat-vector … 22-hud），每条 7.4-8.2 KB，合计 117,453 B | 15 文件 |
| `demos/<slug>/` | 每支片：`index.html`（或 `film.js`+小 index）、`js/` 模块、`audio.py`、`cues.json`、`tools/`；04 还有 `blender/` 4 脚本 | js+html 合计 2.3 MB |
| `harness/` | `render.mjs` 16,899 B（逐帧渲染器）+ `preview.html` 4,403 B（拖动预览） | 2 文件 |
| `lib/audio/mgaudio/` | 21 个 py 模块（`_dsp/core/sfx/synth/drums/mix/fx/filters/fm/osc/pluck/chip/samples/seq/sync/theory/wind/qc/master/__init__`）+ `recipes/` 6 文件 | — |
| `lib/audio/samples/` | 15 类乐器/打击采样，102 个 `.flac` + `index.json`（125 KB） | 102 flac |
| `lib/audio/tools/` | `build_samples.py`、`download_vcsl.sh`、`select_vcsl.py`、`vcsl_list.tsv`（120 KB） | VCSL 采样来源 |
| `assets/` | 共享 HDRI（6.3 MB）、纸纹/颗粒/尘埃贴图、`fonts/README.md`（**字体文件不在库内**，列了 44 个字体文件的落盘路径） | — |
| `rubric.md` / `template.md` | AI 评审提示词 3,676 B / 新风格模板 1,945 B | — |
| `site/` + `index.html` | 中英双语展示页（`site/data.js` 165 KB，含 15 片的 name/name_en/en/work/about）；vendor highlight.js（BSD-3） | — |
| `videos/` | 15 支 mp4 + 封面 jpg；8 支原码率、7 支转码到 <28 Mb/s | 417.6 MiB |
| `docs/readme/` | README 用封面/流程图/15 支 film 预览 webp + 中英截图 | — |

### 1.3 15 个 demo 与编号缺口——作者全套 ≥22 种风格

已发布 15 个：`01-flat-vector, 02-line-art, 03-isometric, 04-3d-render, 05-cel-boil, 06-collage, 07-liquid, 08-morph, 09-bauhaus, 10-synthwave, 12-aurora-glass, 18-hanazi, 19-paperclip, 20-pixel, 22-hud`。
编号缺口 7 个（11/13/14/15/16/17/21）在 `lib/audio/README.md` 的 recipe 表里按编号被引用——**11 grain、13 图文快闪 text flash、14 sticker journal、15 国潮新中式、16 glitch/故障、17 vaporwave、21 acid graphics**。即作者完整风格集 ≥22 种，仓库只发了 15 种。`[实测]`

### 1.4 每片文件构成（例）

- `demos/01-flat-vector/`：`index.html` 76,739 B（SVG 单文件动画，含 `window.DEMO`/`window.renderAt`）+ `audio.py` 7,610 B + `cues.json` 906 B。
- `demos/04-3d-render/`：`blender/{make_letters,sim,scene,render}.py` + `assets/mesh/glyph_*.ply`（字形网格）+ `out/events.json`（碰撞时间）+ `index.html`（把 Blender 序列帧与文字/颗粒合成）。
- `demos/03-isometric/`：`js/` 8 个模块（`world.js` 80 KB、`title5.js`、`night5.js`…）。
- `demos/05-cel-boil/`：`js/scene.js` 117 KB + `tools/{gen_dust,gen_paper,hitmax}.py`。
- 多数 demo 带 `?v5=1`「reel v5」模式：把片尾/字标换成**中文风格名标题**（「扁平矢量」「线条动画」「等轴 2.5D」「3D渲染」「逐帧手绘」「拼·贴·剪·贴」「液态流动」「形变动画」「几何构成 · 包豪斯」「玻璃拟态」「贴纸人科普」「像素风」…）+ `window.linkAt(t)` 联动元素，供合辑复用（harness `--tmap`/`--links`）。已实测 01/02/03/04/05/06/07/08/09/10/12/19/20/22 的代码里有 v5 路径；`18-hanazi` 未见（该片本就是竖屏综艺花字，可能无需合辑化）。`[实测]`

## 2. 逐条对照

### 2.0 判定口径与同源证据链

- **判定口径**：`同源` = 风格身份（名称/标志特征）+ 可判定规则（数字）来自同一体系，本地为压缩改写；`同族` = 只共享风格大类、规则不吻合；`独立` = 无对应。
- **数字指纹（8 组跨卡命中，独立收敛概率≈0）** `[实测]`：
  1. 液态「晚 2-3 帧到」↔ 仓库 07「次级液滴延迟主体 2~3 帧跟随」；
  2. 扁平矢量「错开 2-4 帧」↔ 01「元素错峰入场（stagger 2~4 帧）」；
  3. 综艺花字「回弹约 8 帧 / 错开 2 帧」↔ 18「pop 0 → 1.15 → 1.0 in ~8 frames / 2-frame stagger」；
  4. 像素「320×180」「16-32 种颜色」↔ 20「Internal 320×180」「PICO-8-like 16–32 colours」；
  5. 手绘线条沸腾「3-4 版线稿，每 2-3 帧轮换」「一拍二，每秒 12 张」↔ 05「画 3~4 张微差线稿循环」「24fps 下'一拍二'（实际12fps）」；
  6. 包豪斯「旋转 90° 的倍数」「一拍只做一个动作」↔ 09「quarter circles rotate 90°」「each beat a module acts」；
  7. 等轴 2.5D「斜线一律 30°」↔ 03「30°等角投影」；
  8. 贴纸科普「柱长照真实数字画」↔ 19「charts are exact (bars to scale, numbers consistent)」。
- **本地卡的 4 段中文文本在仓库中零命中**（grep `画风|别做成|逐帧自查` = 0）→ 同源判定依据是规则数字+结构映射，不是逐字复制。`[实测]`

### 2.1 对照表（15 行）

| # | 本地卡（名 / 渲染） | 仓库对应（slug / 名 / 路线原文） | 规则原文对照（本地 ↔ 仓库） | 结尾文案（本地 ↔ 仓库） | 判定 |
|---|---|---|---|---|---|
| 1 | 01 3D 质感 / Blender | `04-3d-render` 3D 渲染 / 「Blender 5.1.2 CLI (bpy script → Cycles…)」 | 「玻璃会折射，橡胶透一点光，金属映出周围」↔「质感三件套：SSS 次表面散射（软胶感）+ AO + HDRI 三点布光」；「一大片一样的小物体像波浪一起起伏」↔「Cloner 克隆器 + Random/Plain Effector 做群体波浪式动画」；「掉下来压扁、回弹、晃几下才停，还会挤开旁边的东西」↔「squash-and-stretch jiggle (damped spring), collides with and displaces the cloner field」；「浅景深」「快动作带运动模糊」↔「shallow DOF (f/1.8 feel), real motion blur」 | 《PLAY》↔ soft.「柔软着陆」 | **同源**（强） |
| 2 | 02 液态 / 网页 | `07-liquid` 液态流动 / 「HTML WebGL2 fragment shader: 2D SDF metaballs (smooth-min)」 | 「用 WebGL 着色器把几团液体做成能融合的距离场：靠近就融成一团，接口是圆润的颈」↔「metaball 融合…两球靠近即自动'粘连'」「拉丝-断裂-回弹：主形离开时留一条细颈」；「动作是甩出去的，起步快、停得慢」↔「缓动前快后慢 cubic-bezier(0.22,1,0.36,1)，液体只会被'甩'出去不会匀速」；「小液滴，晚 2-3 帧到」↔「次级液滴延迟主体 2~3 帧跟随」 | 「合」↔ drop.「万物始于一滴」 | **同源**（强） |
| 3 | 03 等轴 2.5D / 网页 | `03-isometric` 等轴 2.5D / 「Three.js OrthographicCamera at true isometric angle」 | 「没有透视，斜线一律 30°，竖线竖直」↔「30°等角投影, 无透视灭点」；「先落地基，再升墙，最后盖顶」↔「楼房'生长'：底面先落位，立面用 scaleY 从 0 拉起 + 顶面延迟 2~3 帧盖上」；「镜头只平移、不换角度」↔「运镜是整组平移（无旋转）」；「传送带或管道…小方块流动」↔「a little train, drones carrying packets, glowing data streams」 | 「书归原位」↔ ISOPOLIS | **同源**（强-中：本地「三面三档明暗」未在提示词命中） |
| 4 | 04 复古未来 / 网页 | `10-synthwave` 复古 Synthwave / 「HTML WebGL (perspective grid, sun, mountains shader) + canvas chrome text…; VHS pass」 | 「带横条缺口的渐变太阳」↔「striped retro sun (horizontal band cut-outs)」；「网格线带一亮一淡两层光」↔「Double glow (tight ~4px + wide ~30px)」；「金属铬字，砸下来时一道光扫过」↔「CHROME title…star glint sweeping across…lens flare」；「扫描线、红蓝通道错开一两个像素、偶尔跳一帧」↔「RGB split（红蓝通道各偏 1~2px）→ 扫描线…随机 glitch 抽帧」 | 「午夜电台 FM 88.8」↔ NEON DRIVE | **同源**（强） |
| 5 | 05 形变 / 网页 | `08-morph` 形变动画 / 「SVG + flubber or GSAP MorphSVGPlugin (tune shapeIndex)」 | 「两个复杂形状之间先收成圆或胶囊，再展开」↔「复杂 A→B 不直接变：先收敛为中介简形（圆/胶囊）再展开」；「轮廓…不打结」↔「路径对齐是前提…否则会打结」；「背景色跟着换」↔「Background color fields change with each morph (clean color-block wipes)」 | 「灵感」↔ morphe. | **同源**（强） |
| 6 | 06 包豪斯 / 网页 | `09-bauhaus` 几何构成 包豪斯 / 「SVG/Canvas + GSAP on a strict modular grid, beat grid at 120 BPM」 | 「只用红、黄、蓝、黑加纸色」↔「红黄蓝黑限定色」；「位移整格，旋转是 90° 的倍数」↔「位移距离=网格模数整数倍…quarter circles rotate 90°」；「匀速或对称缓入缓出，不回弹、不过冲」↔「禁用 overshoot——机械感是特征不是缺陷」；「一拍只做一个动作」↔「一拍一个动作」 | 「3 分」海报 ↔ KONSTRUKTION | **同源**（强） |
| 7 | 07 科幻 HUD / 网页 | `22-hud` 赛博朋克 HUD / 「SVG/Canvas FUI layers + Three.js wireframe hologram; seeded random data」 | 「一种冷色…状态一变整体换成一种暖色」↔「cyan #00E5FF linework with orange/red #FF6A00 alert state」；「线是画出来的，不是淡入，外圈先出、里圈后出」↔「线框生长：stroke-dasharray 描边动画，元素按层级错帧展开」；「数字乱跳几帧再停在结果上」↔「随机数快速跳变 3~5 帧后落定真实值」；「锁定框从大缩到目标上」↔「锁定框：四角括号…scale 1.4→1.0」 | 「着陆成功」↔ KESTREL-9 目标锁定 | **同源**（强；本地「1-2 像素」只与 demo 代码吻合：`hud.js:45 st(c,w=1)`） |
| 8 | 08 一笔画 / 网页 | `02-line-art` 线条动画 / 「SVG paths + stroke-dashoffset (getTotalLength) + GSAP; a virtual camera that follows the pen tip」 | 「整支片子只有一根线，每个形状的尾巴接着下一个形状的开头」↔「'一笔画'叙事：上一图形的尾线即下一图形的起线」；「线宽不变，圆头」↔「线宽全片恒定（2~4px）…round cap」；「笔尖带一个小光点，眼睛跟着它走」↔「a softly glowing pen tip that leads the draw」「camera…follows the pen tip」；「拐弯慢、直线快」↔「Draw speed eases into corners」；「闭合时，从一点向外填满颜色」↔「LINE-TO-FILL moment」 | 「山野骑行」徽章 ↔ ATELIER LINEA | **同源**（强） |
| 9 | 09 玻璃拟态 / 网页 | `12-aurora-glass` 弥散渐变 玻璃拟态 / 「WebGL: aurora mesh-gradient shader + glass refraction + DOM/CSS backdrop-filter」 | 「几团又大又虚的彩色光缓缓飘、互相融合」↔「4–5 aurora blobs…drifting on bezier paths, blending into a mesh gradient」；「只用色环上相邻的 2-3 种颜色」↔「adjacent hues only」；「毛玻璃：透出后面虚化的光，一圈细亮边，大圆角」↔「backdrop blur ~30px, 5–10% white fill, 1px 30% white inner highlight, large radius」；「全片只有一次高光扫过」↔「WOW: a Liquid-Glass lens…glides across」 | 「晴朗」天气 App ↔ Aurora | **同源**（强-中：本地「动作不短于 0.6 秒」未在提示词命中） |
| 10 | 10 拼贴 / 网页 | `06-collage` 拼贴剪贴 / 「DOM/Canvas with PNG cutouts…stepped 12 fps (render 30 fps, hold motion on 12 fps grid)」 | 「剪刀剪的白边或撕纸毛边」↔「抠图后加 2~4px 白描边（剪刀剪出来的感觉）」；「一秒只更新 8-12 次，每次随机抖一两个像素」↔「主体运动 12fps 甚至 6fps…位置加 ±2px 随机抖动」；「嘴换两三张剪纸」↔「嘴巴用两三张替换帧开合」；「一张纸翻过来盖住画面」↔「转场用…整页翻纸」；「比例故意不对：大头小身子」↔「比例失衡的超现实拼装」 | 「猫头鹰日报」↔ NOGGIN 脑洞季刊 | **同源**（强） |
| 11 | 11 像素 / 网页 | `20-pixel` 像素风 / 「Canvas at 320×180 internal resolution, integer-scaled ×6 with nearest-neighbour」 | 「在小画布上画（比如 320×180），整数倍放大、关掉平滑」↔ 逐字同数；「全片 16-32 种颜色」↔「PICO-8-like 16–32 colours」；「每秒 8-12 张，不做补间」↔「6–8 frame run cycle at ~10–12 fps」「stepped timing (no smooth easing)」；「渐变用像素交错的抖动」↔「dithered sky gradient」；「背景几层…整像素滚动」↔「parallax layers…moving by whole pixels」 | 「大丰收」↔ PIXEL QUEST | **同源**（强） |
| 12 | 12 手绘线条沸腾 / 网页 | `05-cel-boil` 逐帧手绘 线条沸腾 / 「Canvas2D: custom variable-width brush renderer (centreline + pressure → outline polygon), boil = 3–4 jitter variants cycled every 2 frames」 | 「每张画备 3-4 版略有不同的线稿，每 2-3 帧轮换」↔ 逐字同数；「动作一拍二，每秒 12 张」↔「24fps 下'一拍二'（实际12fps）」；「线条两头细、中间粗」↔「variable-width brush…centreline + pressure」；「快动作插 1 帧拉长的残影」↔「smear frame…只保留 1 帧」；「全画面铺一层淡纸纹」↔「整体叠纸纹（multiply 10~15%）」 | 「早安」↔ 手作 HAND MADE | **同源**（强） |
| 13 | 13 扁平矢量 / 网页 | `01-flat-vector` 扁平矢量 / 「SVG + GSAP (CustomEase/CustomBounce/MorphSVG); motion blur mb=4」 | 「只用纯色，不用渐变和纹理」↔「strictly flat (no gradients)」；「进场冲过头 5-10% 再弹回，落地压扁约 10%」↔「弹性缓动…overshoot」「squash&stretch ~10%」；「同一时刻只有一个主角做大动作，其余错开 2-4 帧跟上」↔「元素错峰入场（stagger 2~4 帧），同一时刻只让一个主体动」；「转场靠画面里的东西带」↔「element-driven transitions (an object flies out and carries the cut)」 | 「番茄意面」↔ popwise One Dot | **同源**（强） |
| 14 | 14 贴纸科普 / 网页 | `19-paperclip` 贴纸风 科普 / 「one huge canvas (e.g. 6000×3000 px) with a camera transform (long eases), SVG charts, photo stickers with 10px white outline」 | 「比画面大好几倍的浅色桌面…镜头只平移和缩放，不切镜头」↔「超宽大画布布局，摄像机层做平移/缩放（ease 长曲线）」；「实物照片抠图，加同样宽的白边和淡投影」↔「素材照片抠图 + 8~12px 白描边」；「柱长照真实数字画、和数值成比例」↔「charts are exact (bars to scale, numbers consistent)」；「浅灰蓝底、深灰字，只用一个强调色」↔「Calm blue-grey/off-white canvas (#E9EEF2 + slate), 2–3 colours + one accent」 | 「不到 1% 的水」↔ 一部手机里藏着多少种元素 | **同源**（强-中：本地「每 0.5-1 秒加一样新东西」为本地量化） |
| 15 | 15 综艺花字 / 网页 | `18-hanazi` 综艺花字 / 「DOM/SVG: multi-layer text-stroke 花字 + spring pops + SVG burst/sweat/sparkle over a pet-vlog footage layer」 | 「里白外彩至少两层描边，再加一道硬投影」↔「字体三层结构：填充色+粗白描边+彩色外描边/投影」；「弹出时放大过头再回弹（约 8 帧），或逐字弹、错开 2 帧，停着时轻轻晃」↔「pop 0 → 1.15 → 1.0 in ~8 frames, per-character bounce with 2-frame stagger…gentle wiggle while holding」；「惊讶配爆炸框和放射线，尴尬配汗珠」↔「惊讶用放射线爆炸框、尴尬用汗滴符号」；「字比节拍晚 2-3 帧落下」↔「比语音晚 2~3 帧更自然」 | 「完美早餐/烫烫烫」↔ 喵呜日记 EP.07 | **同源**（强） |

### 2.2 本地视频 vs 仓库成片：同体系、异成片 `[实测]`

| 本地卡 | 本地成片（截图/转录） | 仓库成片（film 预览/`videos/`） | 差异性质 |
|---|---|---|---|
| 01 3D 质感 | 《PLAY》玻璃弹珠海浪 + 橡胶 PLAY（`01_3D质感.png`） | soft.「柔软着陆」粉色软胶 SOFT + 铬球 + 球阵（`videos/04-3d-render.jpg`） | 同签名（克隆阵+软体+字标），不同文案/配色 |
| 02 液态 | 液态金属聚成「合」 | drop. 渐变液态字标 | 同上 |
| 07 科幻 HUD | 《着陆》高度 0200m/速度 08.9m/s（`07_科幻HUD.png`） | 隼眼-9 · 目标锁定 | 同上 |
| 其余 12 支 | 图书馆还书 / 午夜电台 / 铅笔→星星 / 篮球 3 分 / 一笔自行车 / 天气 App / 猫头鹰日报 / 像素渔夫 / 闹钟 / 番茄 / 水 / 吐司机（`16_片尾.png` 缩略图网格） | ISOPOLIS / NEON DRIVE / morphe. / KONSTRUKTION / ATELIER LINEA / Aurora / NOGGIN / PIXEL QUEST / 手作 / popwise / 手机元素 / 喵呜日记 | 同风格签名，不同故事与收尾文案 |

本地视频页头/片尾另证：卡头「Claude Code · Opus 5.5」与仓库 README「made with Claude Opus 5.5」同口径；片尾「15 种画风 · 15 段提示词 / 截图存好，【】里换成你的内容」对应仓库「copy its prompt and make a film of your own」。`[实测]`

### 2.3 名称对照（三方）

| 本地卡名 | 仓库中文名（site `name`） | 仓库 v5 合辑中文标题（demo 代码） | 本地卡英文标（视频卡头） |
|---|---|---|---|
| 3D 质感 | 3D 渲染 | 3D渲染 | 3D MATERIAL |
| 液态 | 液态流动 | 液态流动 | LIQUID |
| 等轴 2.5D | 等轴 2.5D | 等轴 2.5D | ISO 2.5D |
| 复古未来 | 复古 Synthwave | — | RETRO FUTURE |
| 形变 | 形变动画 | 形变动画 | MORPH |
| 包豪斯 | 几何构成 包豪斯 | 几何构成 · 包豪斯 | BAUHAUS |
| 科幻 HUD | 赛博朋克 HUD | — | SCI-FI HUD |
| 一笔画 | 线条动画 | 线条动画 | ONE LINE |
| 玻璃拟态 | 弥散渐变 玻璃拟态 | 玻璃拟态 / 弥散渐变 | GLASSMORPHISM |
| 拼贴 | 拼贴剪贴 | 拼·贴·剪·贴 | COLLAGE |
| 像素 | 像素风 | 像素风 | PIXEL |
| 手绘线条沸腾 | 逐帧手绘（Line Boil=线条沸腾） | 逐帧手绘 | HAND-DRAWN |
| 扁平矢量 | 扁平矢量 | 扁平矢量 | FLAT VECTOR |
| 贴纸科普 | 贴纸风 科普 | 贴纸人科普 | STICKER SCIENCE |
| 综艺花字 | 综艺花字 | — | VARIETY TEXT |

本地英文标与仓库 site `en` 字段仅 `FLAT VECTOR` 完全一致（其余为本地自拟短标）→ 本地视频不是对仓库展示页的录屏，是独立制作的一版。`[实测]`

## 3. 工程体系拆解

### 3.1 逐帧渲染 harness（`harness/render.mjs`，16,899 B）`[实测]`

**契约**（文件头注释原文）：
- demo 页在 `window.__ready = true` 之前定义 `window.DEMO = { width, height, fps, duration }`（可选覆盖 CLI）与 `window.renderAt = async (t) => {…}`——**每一帧是时间 t 的纯函数**；「Anything not driven by renderAt (CSS animations, WAAPI) is also seeked to t automatically」（`seek()`：`a.pause(); a.currentTime = t*1000` 再 `renderAt(t)`）。
- 确定性条款在提示词 Rules 里同义出现：「every frame is a pure function of time t. Seeded randomness only; physics and particles precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions」。

**管线**：
1. 起本地 http server 服务仓库根（`/assets`、`/node_modules` 路径依赖根目录）；puppeteer-core 连 Chrome（`MG_CHROME` 指定路径，默认 macOS 路径），`waitForFunction('window.__ready === true')` + `document.fonts.ready`。
2. 逐帧 `seek(page,t)` → `page.screenshot({type:'png', clip})` → PNG 流管道进 ffmpeg，每 worker 一段无损 `ffv1` mkv。
3. **运动模糊 = 时间超采样**：`MB=samples` 时对每帧渲染 MB 个子样本 `t=(f+SHUTTER*((s+0.5)/MB-0.5))/FPS`，编码帧率 FPS×MB，再 `tmix=frames=MB,select=eq(mod(n,MB),MB-1)` 合成一帧（成本×MB）。
4. 收尾：concat 分段 → 混入 `out/audio.wav`（`apad`，AAC 320k/48 kHz）→ `libx264 -preset slow -crf 14`（可调）、`aq-mode=3`、bt709 色彩标记、`+faststart`。
5. 并行：每 worker 一个浏览器实例（同浏览器内多页共享 compositor 不并行）；机器级并发槽 `MG_RENDER_SLOTS`（默认 3，`/tmp/mg-render-slots` pid 锁）。
6. CLI 开关：`--stills 0.5,2,4.25`（**出关键帧**，对应「先出 6 张关键帧」工作流）、`--tmap`（时间重映射，把片子塞进合辑槽位，单调三次曲线+硬切）、`--links`（记录联动元素轨迹）、`--mkv`（无损交付）、`--scale 0.5`（低清快速预览）、`--from/--to`、`--query k=v`、`--workers`。
7. GPU：macOS 默认 `--use-angle=metal`；Linux 默认 ANGLE/GL-EGL（注释自述「verified: hardware WebGL2, ~38–51 dB PSNR vs the Mac renders」）；`MG_GPU_ARGS` 可覆盖。

### 3.2 Blender 侧（仅 `04-3d-render`）`[实测]`

`demos/04-3d-render/README.md` 步骤原文（6 步）：`make_letters.py`（字形→充气字母网格 `.ply`）→ `sim.py`（运动模拟→`work/anim.npz`，碰撞时间→`out/events.json`）→ `scene.py`（`blender -b --factory-startup -P` 搭场景→`work/scene.blend`）→ `render.py`（`--range 0:239`，240 帧=24fps×10s；macOS Metal / NVIDIA `MG_DEVICE=OPTIX`）→ `audio.py`（配乐）→ `node harness/render.mjs demos/04-3d-render`（index.html 把序列帧+文字+颗粒合成后再走同一条逐帧管线）。
关键设计：**物理量在 Blender 侧先算成确定性数据（npz/events.json），网页侧只读数据合成**——与本地卡 01「Blender 的 Python 脚本搭场景、渲染」对应，比「直接渲成片」多一层可复核的中间产物。

### 3.3 四段模板：仓库 `template.md` ↔ 本地 4 段卡

仓库模板自述（原文）：「每份风格提示词都由「通用部分」和「风格专属部分」组成。通用部分（开头的角色设定，以及 How to work / Rules / Craft checklist / 自评 / Deliver）所有风格都一样…要写一种新风格，只需要填下面四段」——四段=**Output (fixed) / Suggested technical route / Creative seed / Signature features**。

| 仓库段 | 本地卡段 | 映射证据 `[归纳]` |
|---|---|---|
| 角色设定（导演/动设/工程/声音四合一）+ 质量锚（Buck/ManvsMachine…「A clean, template-looking result is a fail」） | 页头「提示词　暂停截图，【】里换成你的」+ 任务头语气 | 本地把「谁来做」压缩成卡片外说明 |
| Output (fixed)：1920×1080/30fps/10.000s/H.264/−14 LUFS/−1 dBTP | 任务头「（1920×1080，30 帧）…配乐音效也用代码合成、跟画面卡点」 | 本地删掉响度/编码细节，保留时长/尺寸/帧率/音画同源 |
| Suggested technical route | 任务头「`<渲染器>`」二选一（Blender / 网页逐帧） | 本地只留渲染器名词，删掉 shader 级细节 |
| Creative seed（按秒分镜+配色+Sound） | 内容段【10 秒分镜+收尾文案】 | 【】槽位=「改 Creative seed 里的故事、品牌名、文案和配色」 |
| Signature features（视觉特征/关键技法，数字级） | 画风段（4-8 条可判定规则） | 本地逐条压成短句，数字保留（见 §2.0 指纹） |
| How to work 1-6（Treatment→关键帧→动画→声音→终检→自评） | 任务头「先出 6 张关键帧给我看，再做动画，最后逐帧自查」 | 对应仓库「Key frames before motion…render stills at 6–10 key times」「Step through the fastest moves frame by frame」 |
| Rules（确定性渲染/素材许可/中文文案） | （并入任务头「用代码」与别做成） | 确定性条款在本地被压缩掉，是最大的信息损失 |
| Craft checklist + 自评（1-10 目标 9） | 别做成（3-4 条反约束） | 本地把 checklist 转成负向禁令（「交叉淡化冒充形变」↔「transitions carried by elements, not crossfades」） |

差异注记：本地卡**统一写 30 帧**，仓库 `04-3d-render`/`05-cel-boil` 实为 **24 fps**（240 帧）、`18-hanazi` 为 **1080×1920 竖屏**；本地模板是均一化的。`[实测]`

### 3.4 AI 评审 rubric（`rubric.md`，3,676 B）`[实测]`

两段式（原文）：「制作 → 独立评审 → 按评审修改 → 再评审。下面两段提示词可以直接用」：
- **第一段（评审）**：另开 AI 会话，身份=「senior motion-design jury member（Motionographer editor、Buck/ManvsMachine CD、抖音/B站 top 账号 lead）」；先看片（contact sheet 每 0.5s 一帧 + 关键段 filmstrip + 5-8 张全分辨率帧）、核 spec（10.00s/−14 LUFS/−1 dBTP/无黑帧/无静止段/视觉命中与音频 onset 对齐）；**7 维 1-10 打分**（style_fidelity / concept_wow / motion_craft / design_typography / finish_texture / sound_sync / technical），锚点「5=学生 6=模板 7=专业 8=一线 9=入围 10=世界最强」「Most first renders deserve 5–7. Do not inflate」；**5-10 条按影响力排序的修复**（时码+可观察现象+带数字的做法）；critical 旗标=generic/AI-template、中文文案不自然、fallback 字体/豆腐块、spec 失败。
- **第二段（修改）**：把评审贴回制作会话，「Raise the film to award level (target ≥ 9)」，先存版本 N，逐条落实/说明替换理由，重渲复核。
- 结果（prompts 头部与 README 自述）：15 支终评 **7.57（liquid）→ 8.21（synthwave）**；04 3D 7.71、05 手作 8.07、22 HUD 7.93；「Each film went through two rounds of review and revision」；`audio.py` 源码内留有 `R2:`（第二轮）修订注释（如 01-flat-vector：「R2: the 4.0 ping sits 5 dB lower」「R2: the dot contact cracks the grid open」）。`[实测]`

### 3.5 音频体系（`lib/audio`）`[实测]`

- **mgaudio**：48 kHz float 立体声，numpy+numba（band-limited PolyBLEP 振荡器、TPT ladder/SVF、Karplus-Strong、FM）、pedalboard 效果；10 秒整混音 3-8 秒出；输出 24-bit WAV、恰好 10.000 s、−14 LUFS、真峰 ≤−1.1 dBTP。`lib/audio/README.md` 自述「Everything is deterministic (seeded)」。
- **核心概念**（README §1）：每个声音=缓冲+**sync point**（`m.sfx(s, at=视觉事件时间)`，whoosh=掠过峰值、riser/lock_on=末点即命中，不许手算偏移）；**levels by construction**（SFX 归一化到 ≈−18 dB 短时 K-RMS，`gain` 只表意图）；music/sfx 两组总线 + 音乐在 SFX 点自动 3 dB 侧链；母带=28 Hz HPF+120 Hz 以下单声道+glue+20 kHz 线性相位 LPF+真峰限幅+响度归一+4ms/250ms 淡入淡出；**mono-safe** 立体声（M/S 展宽，禁用 Haas 延迟法——手机外放单声道是抖音/B站投放目标）；form 锚定在 drop（`bar 0 = drop`），`chord_at(t)` 让调性 SFX 不跑调。
- **recipes 按风格预制**（表里按 demo 编号标注）：synthwave→10、darksynth→22 HUD、chiptune→20 pixel、techno→09 Bauhaus、pop→01/04、future_bass→07 liquid/08 morph、lofi→11 grain/05 cel/06 collage、ambient→12 aurora/02 line art、variety→18 花字/14 sticker journal、explainer→19 回形针/03 isometric…；`recipes.for_style('13-text-flash', drop=3.2)`。
- **SFX 家族**（12 类，全归一化）：motion/tension/UI/liquid/paper-desk/glitch/retro-media/sci-fi-HUD/magic/8-bit/cartoon-综艺/text。
- **采样**：102 个 flac（README 自述 103 个采样，差 1 未核）+ `samples/index.json`（125 KB）+ `tools/download_vcsl.sh`（来源 VCSL=CC0）；`samples.inst('piano'|'harp'|'marimba'|…)`。
- **cues.json**：音画共享节拍表（示例 01：`fps/bpm/key/mode/build/drop/outro` + 40+ 事件帧号 `impact1:15, launch:31, sunLand:40, ping:120, wipe:150, burst1:180, merge:240, logoWipe:240, letters:243…`）；`audio.py` 与 `index.html` 同读这一张表——「Keep one cue sheet (beats and hit times) that both the picture and the sound read from」（提示词 How-to-work 第 1 条）。
- 重跑一致性（README 自述）：同环境重跑「4 of them match the films' audio (within the least significant bit) and the other 11 differ in places, probably because of changes in the numerical libraries」→ 11/15 非位级可复现。

### 3.6 逐项「值得抄什么」→ B-02 / B-03 / B-07 映射

| 仓库件 | 值得抄什么 | 映射 |
|---|---|---|
| `harness/render.mjs` 契约（`window.DEMO`/`renderAt(t)`/`__ready`+CSS/WAAPI seek） | **确定性渲染契约**的最小可执行定义：单页可对任意 t 出帧 → 逐帧可核、可重渲任意区间 | **B-02**（html/workflow.md §确定性帧）+ **B-11**（确定性渲染契约条款进 templates） |
| harness CLI（`--stills`/`--tmap`/`--links`/`--mkv`/`--scale`） | 「先出关键帧」有现成实现；合辑时间重映射与联动元素轨迹是成品级补丁 | **B-02**、**B-07**（测试栈候选） |
| 运动模糊=时间超采样（MB×渲染+tmix） | 不依赖后期模糊的确定性做法，成本可标定 | **B-02** |
| `cues.json` 单表双读（画面+声音） | 音画同源的**数据结构**：一份事件帧号表两处消费 | **B-02**、**B-07** |
| Blender 侧 6 步（字形网格→物理 npz→场景→渲染→合成） | 中间产物全部落盘、可复核；Blender 只渲画面、文字/颗粒回网页合成 | **B-03**（blender/workflow.md 对照） |
| `rubric.md` 两段式（评审→修改）+ 7 维锚点 + critical 旗标 | **AI 评审 rubric** 的完整可抄文本；锚点语句（「6=template level, 8=high-end agency, 9=award shortlist」「Do not inflate」）可直接进 B-11 的 templates | **B-11**（AI 评审 rubric）、**B-07**（对照实验的评分口径） |
| `template.md` 四段 + 通用部分复用 | 与本地 `templates/style_card.md` 逐段对表（§3.3）；「Signature features 要可检验」的写法可直接引用 | **B-11**、`templates/style_card.md` 修订 |
| mgaudio（recipes/SFX/母带/QC） | 音效与画面同源于一张 cue 表；响度/真峰/单声道兼容的工程标准（−14 LUFS、−1 dBTP、M/S 展宽） | **B-02**（音频合成段）、**B-07** |
| `prompts/*.md` 的 Rules 三条（确定性/素材许可/中文文案正确） | 把「不许用实时时钟」「素材只用 CC0/OFL」「中文标点正确」写进模板硬条款 | **B-11**（模板条款）、**B-08**（迁移指南） |
| `site/`（中英切换+提示词折叠+源码浏览+复制按钮） | 交付形态参考：卡=成片+风格说明+提示词+源码四件套一页装 | 展示层，非当前目标 |

## 4. 复用评估（MIT）

### 4.1 许可边界 `[实测]`

- `LICENSE`：MIT，`Copyright (c) 2026 Vincentwei1021`——**代码、提示词、文档、为项目制作的成片**均 MIT（README 明示）；引用/衍生需保留版权声明，可商用、可改。
- 第三方各自许可（README 自述）：VCSL 乐器采样、HDRI、纸纹、照片、Natural Earth 地图数据 = CC0/公有领域；`site/vendor/highlight.min.js` = BSD-3-Clause；`demos/04-3d-render/assets/mesh/` 与 `demos/08-morph/glyphs.json` 的字形轮廓来自 OFL 字体，保持 OFL。
- **字体文件不在库内**（授权各异、中文字体大）；`assets/fonts/README.md` 列 44 个文件（Alibaba PuHuiTi、HarmonyOS Sans SC、Resource Han Rounded、Noto Sans SC、Fredoka、Sora、Press Start 2P…）及落盘路径。缺字体时浏览器回退系统字体、字形与成片不同。
- 结论：**文本/代码/提示词可直接复用**（保留 MIT 声明）；复刻画面质量需自备字体；VCSL 采样可直接用（CC0，可用 `lib/audio/tools/download_vcsl.sh` 复建）。

### 4.2 可直接用的清单（按优先级）

1. `harness/render.mjs` + `harness/preview.html`（B-02 的现成基线实现，替代自研）。
2. `rubric.md`（B-11 的 AI 评审 rubric 原样落地）。
3. `template.md` 与 §3.3 映射表（修订 `templates/style_card.md`）。
4. `cues.json` 结构 + `audio.py` 用法（音画同源数据契约）。
5. `lib/audio/mgaudio`（B-07 测试片的音轨引擎；本地卡「配乐音效用代码合成」的现成解）。
6. `prompts/*.md` 15 条（风格规则的英文完整版；本地卡的中文压缩版可与之互补）。
7. `demos/*/js` 参考实现（每风格的具体画法：SDF 液面、SSR 等轴面、线稿 boil 变体、CRT 后处理…）。

### 4.3 跑通代价 `[UNVERIFIED]`（未跑；下列为依赖与预期，标 [UNVERIFIED]）

- 依赖（README「Run the source」+ `package.json`/`requirements.txt` 实测）：Node ≥22.12 + Chrome + ffmpeg + Python ≥3.11；npm 6 包（`puppeteer-core 25.12.0, three 0.186.1, d3 7.9.0, opentype.js 2.0.0, simplex-noise, topojson-client`）；pip 13 包（`numpy==2.4.6, scipy, soundfile, numba 0.66.0, pedalboard, pyloudnorm, matplotlib, librosa` + 素材脚本用 `pillow, fonttools, scikit-image, opencv-python, rembg`）；3D 片另需 Blender。
- 运行成本（读代码推算，[UNVERIFIED]）：每片 300 帧（24fps 片 240 帧）；`--mb 4` 时 1200 次 seek+screenshot；`MG_RENDER_SLOTS` 默认 3 并行；仓库体积 555 MiB（视频 417 MiB），整仓克隆在网络差时是主要成本——**本项目建议只稀疏克隆文本**（本次 3.2 MB / 数秒）。
- 本机环境对照（2026-10-15 实测记录于 GOALS「环境实测」）：node v24.19.0 ✓（≥22.12）、npm 11.17.0 ✓、ffmpeg n9.0.1 ✓、Python 3.14.7（**numba 0.66.0 对 3.14 的兼容未核 [UNVERIFIED]**，必要时装 3.12 venv）、Blender 5.2.1（仓库 3D 片用 5.1.x，API 差异未核）、ImageMagick 未装（本仓不需要）、Chrome 需 `MG_CHROME` 指向 Windows `chrome.exe`（harness 默认 macOS 路径）、字体未装（44 个文件清单在手）。
- 若只借 rubric/template/cues 结构（不跑渲染），成本≈0——这是本次评估的最低风险路径。

### 4.4 风险清单

1. 字体缺失 → 字形/排版与成片不同（不可用 MIT 覆盖）。
2. 音频 11/15 非位级复现（数值库漂移，作者自述）。
3. 仓库默认 macOS Chrome 路径与 GPU flags；Windows 需改环境变量。
4. 视频/采样体积大：整仓克隆 555 MiB，不适合本项目的「只读分析」模式（用稀疏克隆或 raw 直读）。
5. 「同一提示词每次出片不同」为作者自述——用其提示词不等于复现其成片。

## 5. 缺口节

1. **源视频本体仍未回捞（A-13）**：`10cd03a4d43ec624cdbb96bbc0ec1f6d.mp4` 不在盘上；本次只用了 wave1 的转录与 16 张截图。已查：仓库文件/commits/site/README（无 视频号 字样）、作者 GitHub 主页（链 X @VincentWei93 与抖音，无视频号）。`[已查]`
2. **本地视频的作者身份未证实**：卡头「Claude Code · Opus 5.5」与仓库口径一致、15/15 风格集一致、数字指纹一致，但本地英文标≠仓库 site `en`、本地成片≠仓库成片、4 段中文文本仓库零命中——**同源（同体系）成立；「作者本人 vs 第三方改编」无法从本地证据判定**。`[推测]`（视频平台为微信视频号；web_search 全 provider 限流，本次不可用）
3. **本地卡 5 处数字未在仓库提示词命中**：玻璃「动作不短于 0.6 秒」、花字「同屏 ≤3 色」、贴纸「每 0.5-1 秒加一样新东西」、等轴「三面同一色相三档明暗」、HUD「1-2 像素细线框」。其中 HUD 的 1/2 px 只与 demo 源码吻合（`js/hud.js:45` `st(c,w=1)`）；其余可能藏于 2.3 MB demo 源码/成片，或为本地卡作者新增——**未逐一穷尽核**。`[UNVERIFIED]`
4. **未跑任何构建/渲染**：§4.3 全部为静态推算，产物一致性、渲染时长、PSNR 等均未实测。
5. **7 个未发布风格**（11/13/14/15/16/17/21）只有 recipe 名称与编号，无提示词、无源码（作者未发布）。
6. **字体文件缺失**：44 个字体文件需自备（清单已存 `%TEMP%\mg15\mgrepo\assets\fonts\README.md`，非本仓路径，属临时分析副本）。
7. **未做逐帧像素对照**（D-03 依赖源视频）：本地成片 vs 仓库成片的同风格差异只做了截图级对照（§2.2），未做帧对齐测量。
8. 采样数 102 flac vs README 自述 103，差 1 未核。

## 6. 机械验证（原样输出）

### 6.1 三条 GitHub raw URL（`read` 工具实测可达，2026-10-15）

URL 1：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/rubric.md:1-8`，read 输出（原样）：

```
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/rubric.md
Content-Type: text/plain
Method: text

---

# 评审提示词：让另一个 AI 当评委，再拿评审意见改一轮

原片都是这样迭代出来的：制作 → 独立评审 → 按评审修改 → 再评审。下面两段提示词可以直接用。

## 第一步：评审（另开一个 AI 会话，把成片路径告诉它）
```

URL 2：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/template.md:1-9`，read 输出（原样）：

```
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/template.md
Content-Type: text/plain
Method: text

---

# 写一种新风格的提示词

每份风格提示词都由「通用部分」和「风格专属部分」组成。通用部分（开头的角色设定，以及 How to work / Rules / Craft checklist /
自评 / Deliver）所有风格都一样，可以直接从任意一份 `prompts/*.md` 里复制。要写一种新风格，只需要填下面四段：
```

URL 3：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/prompts/07-liquid.md:1-6`，read 输出（原样）：

```
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/prompts/07-liquid.md
Content-Type: text/plain
Method: text

---

# 液态流动 Liquid Motion

**原片**：drop.「万物始于一滴」 · 1920×1080 · 30 fps · 10 秒 · AI 评审终评 7.57 / 10
```

### 6.2 GitHub API（原样输出，2026-10-15）

```
full_name = Vincentwei1021/mg-styles-15
description = 15 motion design styles, each made by Claude Opus 5.5 writing code from one prompt: watch the films, copy the prompts, read the full source.
default_branch = main
license = {'key': 'mit', 'name': 'MIT License', 'spdx_id': 'MIT', 'url': 'https://api.github.com/licenses/mit', 'node_id': 'MDc6TGljZW5zZTEz'}
stargazers_count = 866
forks_count = 139
size = 567916
created_at = 2026-10-02T09:43:06Z
updated_at = 2026-10-15T07:23:31Z
pushed_at = 2026-10-05T11:23:17Z
language = Python
homepage = https://vincentwei1021.github.io/mg-styles-15/
```

### 6.3 数字指纹 grep（原样输出，节选；命令见本文件撰写过程）

```
--- glass 0.6s? ---
(no 0.6)
--- liquid 晚2-3帧 / 甩 ---
30:HTML WebGL2 fragment shader: 2D SDF metaballs (smooth-min) + fake 3D lighting from field gradient normals, text SDF for the logo
36:- 0–2s: droplets fall and splash with squash on landing; 2–4s: blobs merge via metaball fusion — stretched necks, snap, 2–3 frame rebound; secondary droplets follow 2–3 frames late;
38:- 6–8.5s: the liquid coalesces into a wordmark (e.g. "FLUX") — text SDF blended with the metaballs;
47:视觉特征 波浪边缘转场, 拉丝与滴落, metaball融合, 次级液滴跟随, 有机曲线永不直线
50:拉丝-断裂-回弹：主形离开时留一条细颈，断裂瞬间两端各回弹 2~3 帧
51:缓动前快后慢 cubic-bezier(0.22,1,0.36,1)，液体只会被'甩'出去不会匀速
52:次级液滴延迟主体 2~3 帧跟随（follow-through），落地做扁平化 squash
--- flat vector 2-4帧/10%/5-10% ---
36:- 1.2–3.0s: the circle becomes the sun; a flat city pops up building-by-building with 2–4 frame stagger (each with its own mini overshoot), clouds slide, birds flap.
40:Rules: one hero moves at a time; squash&stretch ~10%; secondary action & follow-through; element-driven transitions (an object flies out and carries the cut); strictly flat (no gradients), bold 5–6 color palette (…)
50:元素错峰入场（stagger 2~4 帧），同一时刻只让一个主体动
51:30fps 居多；位移动画带 10% 左右 squash&stretch 增加弹性
```

（对照：本地 02 液态卡「主体后面跟几颗小液滴，晚 2-3 帧到」；本地 13 扁平矢量卡「其余错开 2-4 帧跟上」——数字逐条命中；`(no 0.6)` 即本地 09 的「0.6 秒」未在提示词命中，记入 §5 缺口第 3 条。第 40 行括号内 `#2B2BFF, coral #FF5A4E, sunflower #FFC62B, mint #2EE6A8, cream #FFF6E9, ink #151433` 为省行用省略号替换，其余逐字。）

### 6.4 稀疏克隆（原样输出，两次）

第一次（cone 模式带通配失败）：

```
Cloning into 'mgrepo'...
fatal: specify directories rather than patterns.  If your directory really has any of '*?[]\' in it, pass --skip-checks
157K    .
ls: cannot access 'demos/': No such file or directory
```

第二次（`--no-cone` 成功）：

```
3.2M    .
139
01-flat-vector
02-line-art
03-isometric
04-3d-render
05-cel-boil
06-collage
07-liquid
08-morph
09-bauhaus
10-synthwave
12-aurora-glass
18-hanazi
19-paperclip
20-pixel
22-hud
```

（`139` = 检出文件数；demos 15 个目录全在。仅文本、只读分析，未跑构建。）

## 7. 自审四段

**A · 早产出**：本文件即产物；方法=API/raw/稀疏克隆三路取证，先骨架后逐节填，最后复读校验一遍。§2 对照表 15 行全部有原文片段；§3 五小节逐件拆解；§4/§5 齐。

**B · 反驳**（挑 5 条最强结论试推翻，命令见 §6）：
1. 「15/15 同源」→ 试推翻：找本地卡文本在仓库逐字命中 → grep `画风|别做成|逐帧自查` 全仓 0 命中；但 8 组数字指纹全命中、15 行结构映射成立 → **CONFIRMED**（同源指体系/规则，非逐字）。
2. 「本地成片≠仓库成片」→ 试推翻：比对本地 01/02/07 截图与仓库 04/07/22 预览帧 → PLAY≠soft.、合≠drop.、着陆≠隼眼-9 → **CONFIRMED**。
3. 「仓库=完整工程体系（含 AI 评审两轮）」→ 试推翻：查 rubric.md（两段式）+ README 自述 + prompts 头部终评分数 + audio.py `R2:` 注释 → **CONFIRMED**。
4. 「本地 4 段=仓库四段模板的压缩」→ 试推翻：仓库 template.md 四段=Output/Route/Seed/Signature，本地=任务头/画风/内容/别做成；「别做成」在仓库散在 Rules/Craft checklist，不是独立段 → **WEAKENED**（映射成立、段数不完全对齐；已在 §3.3 注明「本地把 checklist 转成负向禁令」）。
5. 「本地视频作者=仓库作者」→ 试推翻：无任何直接证据（无视频号链接、英文标不同、成片不同）→ **OVERTURNED 为不可判定**（§0 第 5 条与 §5 缺口第 2 条均按「未证实」表述，未按同作者落盘）。

**C · 机械验证**：§6.1 三条 raw URL 由 `read` 工具实读并原样粘贴；§6.2 API 输出；§6.3 grep 输出；§6.4 克隆输出。另有本机抽看截图三张（`00_片头倒计时.png`=5.5 片头、`01_3D质感.png`=PLAY 卡、`07_科幻HUD.png`=《着陆》卡，均与转录一致）。

**D · 小结**（≤14 行）
1. 已确立：15/15 同源（规则数字+结构映射）；仓库全管线实态（harness 契约/CLI、Blender 6 步、rubric 两段式、mgaudio、cues 单表双读）；MIT 边界与可直接用清单；本地卡=中文压缩版（统一 30 帧、删确定性条款）。
2. 已确立：成片是两次运行（本地新 seed：PLAY/合/着陆… vs 仓库 soft./drop./KESTREL-9…）。
3. 被推翻/降级：本地视频作者身份不可判定（不可当同作者引用）；本地 4 段与仓库四段的段数对齐为 WEAKENED。
4. 未知：源视频本体（A-13）；5 处本地数字的出处；7 个未发布风格；跑通实测数据。
5. 下一步（建议）：① B-11 用 rubric.md 原文 + §3.3 映射修订 `templates/style_card.md`（加「确定性渲染契约」条款）；② B-07 以本仓 harness 为候选栈之一，先跑 01-flat-vector 做成本标定（配好 MG_CHROME/字体）；③ A-13 沿作者 X/抖音账号线索回捞视频，做 D-03 帧对照。
