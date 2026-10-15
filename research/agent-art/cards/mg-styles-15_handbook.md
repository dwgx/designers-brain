# mg-styles-15 参考实现管线手册（B-13）

> 归属：GOALS B-13（PipelineHandbook）｜状态 v0.1（2026-10-15）｜兄弟文档：`mg-styles-15_compare.md`（B-10 溯源对照）、`structure.md`（15 卡骨架）
> 对象：GitHub 仓 `Vincentwei1021/mg-styles-15`（MIT，866★/139 fork，2026-10-15 API 数据），默认分支 `main`；本次实读的克隆 HEAD = `49052d8 LICENSE: plain MIT text so GitHub detects it`。
> 方法：只读分析——`%TEMP%/mg15/mgrepo` 稀疏克隆（B-10 遗留：384 个受控文件 / 3.2 MB，缺 `demos/*/blender|assets|out`、`lib/audio/samples|tools` 等）＋ `read` 直读 `raw.githubusercontent.com` 补读不在检出里的文件（Blender 5 脚本、lib/audio/README、VCSL 工具等）。**未跑任何构建、渲染、音频导出、ffmpeg**。
> 证据分级：`[实测]`＝本次命令/实读输出 ｜ `[原文]`＝仓库文件原文片段（路径+行号或引号）｜ `[归纳]`＝本次总结 ｜ `[UNVERIFIED]`＝未跑未核。
> 行号基准：稀疏克隆 HEAD（`49052d8`，与 GitHub main 一致）；raw 直读的文件只给引文。字节数为本地检出（CRLF），与 GitHub blob 尺寸略差（如 render.mjs 本地 17,218 B vs API 16,899 B——差值 = 行数）。

## 1. 仓库地图

### 1.1 顶层结构（`git ls-files` 384 个受控文件）[实测]

| 路径 | 文件数 | 内容 |
|---|---|---|
| `prompts/` | 15 | 15 条风格提示词（01-flat-vector … 22-hud），每条 7.4–8.2 KB；六段式（Output / Suggested technical route / Creative seed / Signature features / How to work / Rules / Craft checklist / 自评 / Deliver） |
| `demos/` | 154 | 15 支片全部源码：每 demo 必有 `index.html` + `audio.py` + `cues.json`（15/15/15）[实测]；3 个用 `film.js`（02/09/20）、2 个用 `main.js`（03/12）；`js/` 模块目录（03 八个、07 七个、22 五个、05 两个）；`tools/` 辅助脚本（02/05/08/19）；`04` 另有 `blender/` 5 脚本 + `assets/mesh/` 4 PLY + `out/events.json` |
| `harness/` | 2 | `render.mjs`（逐帧渲染器，319 行）+ `preview.html`（拖动预览页） |
| `lib/audio/mgaudio/` | 21+7 | 音频引擎 21 个 py + `recipes/` 7 个（15 个风格配方 + `STYLES` 映射表） |
| `lib/audio/samples/` | 103 | **102 个 .flac**（15 类乐器/打击采样）+ `index.json`（索引）[实测计数] |
| `lib/audio/tools/` | 4 | `build_samples.py`（VCSL→48k FLAC+索引）、`download_vcsl.sh`、`select_vcsl.py`（VCSL 子集选择器）、`vcsl_list.tsv`（597+ 行下载清单） |
| `assets/` | 12 | 共享 HDRI（studio_small_09_2k.hdr）、纸纹/颗粒/尘埃贴图、`fonts/README.md`（**字体本体不在库内**，列 44 个文件的落盘路径）+ `fonts.css` |
| `docs/readme/` | 20 | README 用封面/流程图/15 支片预览 webp + 中英截图 |
| `site/` | 5 | 展示页：`app.js`、`data.js`（165 KB，15 片的 name/name_en/en/work/about）、`style.css`、vendor highlight.js（BSD-3） |
| `videos/` | 30 | 15 支 mp4 + 15 张封面 jpg（417.6 MiB，未在稀疏检出内）[实测文件数] |
| 根文件 | 10 | `rubric.md`、`template.md`、`index.html`（展示页）、`package.json`、`requirements.txt`、`LICENSE`、`README.md`、`README.zh-CN.md`、`.gitignore`、`.nojekyll` |

### 1.2 关键文件一句话职责 [归纳]（均实读）

**harness/**
- `harness/render.mjs` — 逐帧渲染器：本地 http 服务器 + puppeteer-core 逐帧截图 → PNG 流进 ffmpeg → 分段 ffv1 mkv → concat+音频 → x264 mp4；含运动模糊超采样、tmap 时间重映射、links 轨迹记录、stills 关键帧。
- `harness/preview.html` — 浏览器内拖动/播放预览：iframe 载 demo，`renderAt(t)` 驱动，帧量化 `Math.floor(x*fps+1e-6)/fps`；有 `out/audio.wav` 就播。

**lib/audio/mgaudio/（21 模块）**
- `core.py` — `SR=48000`、`Sound`（buffer + sync point）、包络/噪声/增益工具。
- `mix.py` — `Mix`/`Grid`/`Track`：轨道、总线、duck、region FX、`export()`（默认 `lufs=-14 tp=-1`，`:534`）。
- `master.py` — 母带链：HPF→单声道低音→glue→(warmth/tilt/air/width)→线性相位 LP→淡入淡出→响度归一+真峰限幅（`master()`:97）。
- `sfx.py` — 12 族 SFX 合成（全部响度归一化 ≈ −18 dB 短时 K-RMS）。
- `samples.py` — VCSL 采样引擎 `inst()/hit()`（见 §3.5）。
- `recipes/` — 15 个风格配方 + `STYLES` 表（22 个 demo slug → 配方/kwargs/替代/SFX 建议，`__init__.py:22`）。
- `qc.py` — `analyze()`（LUFS/真峰/频段/相位/onset/warnings）+ spectrogram + `python3 -m mgaudio` CLI（`__main__.py`）。
- `sync.py` — `frame/snap/fit_bpm/grid_report/place/load_cues`：把画面命中时刻对到节拍网格。
- `seq.py` / `theory.py` — 音符/音阶/和弦/琶音/欧几里得节奏。
- `filters.py` / `fx.py` — SVF/ladder/EQ；reverb/delay/chorus/saturate/tape/bitcrush/widen…（Haas 明示「NOT mono-safe」）。
- `synth.py` / `fm.py` / `pluck.py` / `chip.py` / `wind.py` / `drums.py` / `osc.py` — 各合成器族（含 guzheng 筝、dizi 笛、taiko 大鼓等中式乐器）。
- `_dsp.py` — numba 加速内核；`__init__.py` — 公共导出。

**lib/audio/tools/**
- `select_vcsl.py` — 按 RULES 表（42 个 key：folder 子串 + 文件名正则）从 VCSL 仓库 tree JSON 选子集，写 `key\tpath\turl` 清单。
- `download_vcsl.sh` — 按清单 curl 下载到 `/tmp/vcsl_raw/<key>/`（幂等：已存在且非空则跳过）。
- `build_samples.py` — 把 `/tmp/vcsl_raw` 的 wav 转成 48 kHz 修剪版 FLAC + `index.json`（音名→midi 正则、力度层映射、`MAXDUR` 裁剪表）。
- `vcsl_list.tsv` — 生成的下载清单（URL 指向 `sgossner/VCSL` raw）。

其余 demo 文件职责在 §2/§4 逐条展开。

### 1.3 每支 demo 的构成模式 [实测+归纳]

- **三件套恒定**：`index.html`（渲染页，暴露契约）+ `audio.py`（配乐，读同一 cues.json）+ `cues.json`（音画共享节拍表）。15/15 全有。
- **渲染页形态**：单文件（01/04/07/10/18/19/22 把动画写进 index.html）、`film.js` 外置（02/09/20）、`main.js`+`js/` 模块（03/12）。
- 目录内还有 `assets/`（贴图/贴纸/字形）、`tools/`（生成素材的 py）、`out/`（产物，通常不在库里；04 的 `out/events.json` 例外，是给 audio.py 与 index.html 读的数据）。
- **reel v5 模式**（`?v5=1`）：14/15 个 demo 实现 `window.linkAt(t)`（全部除 18-hanazi），把片尾字标换成中文风格名供合辑复用 [实测 grep]。`renderAt` 15/15、`__ready` 15/15。

## 2. 渲染管线（harness/render.mjs）

### 2.1 契约：DEMO / renderAt(t) / __ready / linkAt / EV

render.mjs 文件头原文（`render.mjs:4-7`）：
```
// A demo page (demos/<slug>/index.html) must define, before setting window.__ready = true:
//   window.DEMO = { width, height, fps, duration }            // optional overrides of CLI defaults
//   window.renderAt = async (t) => { ... }                     // draw the frame for time t (seconds)
// Anything not driven by renderAt (CSS animations, WAAPI) is also seeked to t automatically.
```
逐项实现（示例行号）：
- **DEMO（含 DUR）**：`window.DEMO = { width, height, fps, duration, motionBlur: { samples, shutter } }` —— `01/index.html:11`（samples 1）、`02/film.js:9-10`（v5 时 `DUR = 11`）、`09/film.js:7`（samples 8）、`04/index.html:96`（fps 24）、`18/index.html:40`（1080×1920 竖屏）。`duration` 即 CLI `--duration` 的缺省（`render.mjs:213`）。
- **renderAt(t)**：帧=时间的纯函数。`01/index.html:697`（`async (t) => {…}` 画完即返回）；`09/film.js:600`（`const tc = snap(t), k = shutK(t); t = tc + (t-tc)*k; renderPlates(t); present(t,k)`——内部把 t 量化到帧再按快门开度外推，供片内 shader 超采样用）；`04/index.html:126`（`await loadFrame(round(t*24))` 后叠加 DOM 文字层）。规范条款（提示词原文，`prompts/01-flat-vector.md:71-74`）：「Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only; physics and particles precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions.」
- **READY（`__ready`）**：资源就绪后才置位——字体加载完（`04/index.html:207-209` `document.fonts.load(...)` + `ready`）、首帧预画（`await window.renderAt(0)`；`01:709-710`、`04:211-212`、`09:696-697`）、模块异步加载完（`20-pixel/index.html:15-16` `await import('/demos/20-pixel/film.js'); window.__ready = true;`）。渲染器等它：`render.mjs:92` `waitForFunction('window.__ready === true', {timeout: 300000, polling: 100})`，再等 `document.fonts.ready`（`:93`）。
- **linkAt(t)（v5 联动）**：14 个 demo 定义 `window.linkAt(t)`，返回 1920×1080 帧坐标下的元素数组 `[{id,type,x,y,r,…}]`；`render.mjs:104-106` 的 `linkAt()` 在「帧中心源时刻」采样，写 `--links track.json`（`render.mjs:291`）。
- **EV（事件表，demo 侧）**：由 cues.json 派生。`09/film.js:16`：`const EV = Object.fromEntries(cues.events.map(e => [e.id, e]));`——之后全片用 `EV.circle_land.t`、`EV.tri_flip.t0` 这类名字取时间（同表在 `09/audio.py:9-10` 原样重建：`EV = {e['id']: e for e in C['events']}`，见 §3.1）。注：`EV`/`DUR` 是 demo 内部命名，不是 harness 全局（全库无 `window.DUR/READY/EV`）。

seek（渲染器侧，`render.mjs:95-101`）：先暂停页内所有 Web Animations 并设 `currentTime = t*1000`，再调 `renderAt(t)`：
```js
for (const a of document.getAnimations()) { try { a.pause(); a.currentTime = t * 1000; } catch {} }
if (typeof window.renderAt === 'function') await window.renderAt(t);
```
——即「CSS/WAAPI 动画也被 seek 到 t」，是契约里『Anything not driven by renderAt … is also seeked』的实现。

### 2.2 headless Chrome 逐帧捕获 [实测 render.mjs]

1. **本地 http server**（`:73-89`）：node `http.createServer` 服务仓库根（依赖 `/assets`、`/node_modules` 的绝对路径）；MIME 表覆盖 html/js/css/json/图片/字体/hdr/glb/ktx2 等；`Cache-Control: no-store`、`Access-Control-Allow-Origin: *`；目录→`index.html`；越出 ROOT 返回 403。端口随机（`listen(0)`）。
2. **Chrome 启动**（`:29,31-34,196-201`）：puppeteer-core，`executablePath: process.env.MG_CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'`（默认 macOS 路径）；headless + `protocolTimeout: 600000`；GPU flags 按平台——macOS `['--use-angle=metal']`，其他 `['--use-gl=angle','--use-angle=gl-egl','--no-sandbox','--disable-gpu-watchdog','--disable-gpu-process-crash-limit']`（注释自述 NVIDIA via EGL：「verified: hardware WebGL2, ~38–51 dB PSNR vs the Mac renders」）；另有 `--enable-gpu --ignore-gpu-blocklist --enable-unsafe-webgpu --font-render-hinting=none --disable-lcd-text --force-color-profile=srgb --disable-gpu-vsync --disable-frame-rate-limit --disable-background-timer-throttling --autoplay-policy=no-user-gesture-required --hide-scrollbars --mute-audio` 等。
3. **探针页**（`:206-210`）：先开一个 page 载 demo，等 `__ready`，`evaluate(() => window.DEMO || {})` 取配置后关掉；CLI 覆盖优先：`W = args.w || cfg.width || 1920`、`FPS = args.fps || cfg.fps || 30`、`DUR = args.duration || cfg.duration || 10`、`MB = max(1, args.mb || cfg.motionBlur?.samples || 1)`、`SHUTTER = args.shutter ?? cfg.motionBlur?.shutter ?? 0.5`（`:212-214`）。
4. **帧循环**：每 worker 一个浏览器（注释原文 `:256`：「One browser per worker: pages inside a single browser share one compositor and don't parallelize.」）；worker 数 `Math.max(1, Math.min(+(args.workers || cfg.workers || 1), f1 - f0))`（`:241`，**默认 1**）；帧区间均分 `chunk = ceil((f1-f0)/WORKERS)`（`:247`）；`setViewport({width,height,deviceScaleFactor:SCALE})`（`--scale 0.5` 出低清预览，布局仍按 W×H CSS px）。
5. **截图**（`:109-111`）：`page.screenshot({type:'png', clip:{0,0,W,H}, optimizeForSpeed:true, captureBeyondViewport:false})`，PNG Buffer 直接 `writeAsync` 进 ffmpeg stdin。

### 2.3 ffmpeg 合成：逐帧管道 + 终编码 [实测 render.mjs]

**分段（每 worker 一段无损 mkv，`:260-264`）**：
```js
const vf = MB > 1
  ? `tmix=frames=${MB},select='eq(mod(n\\,${MB})\\,${MB - 1})',setpts=N/(${FPS}*TB)`
  : 'null';
const ff = ffmpeg(['-f', 'image2pipe', '-framerate', String(FPS * MB), '-c:v', 'png', '-i', '-',
  '-vf', vf, '-r', String(FPS), '-c:v', 'ffv1', '-level', '3', '-threads', '2', '-pix_fmt', 'bgr0', seg]);
```
**收尾（`:292-308`）**：concat 分段（`-f concat -safe 0 -i list.txt`）→ 可选混入音频（`out/audio.wav` 存在即用，或 `--audio` 指定、`--noaudio` 关；`-af apad -c:a aac -b:a 320k -ar 48000 -shortest`）→ 终编码：
```
-vf scale=out_color_matrix=bt709:out_range=tv:flags=lanczos+accurate_rnd+full_chroma_int,format=yuv420p
-c:v libx264 -threads 4 -preset slow -crf 14 -profile:v high -x264-params aq-mode=3
-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv -r 30 -movflags +faststart
```
**其他模式**：`--stills 0.5,2,4.25` → 逐时点 PNG 存 `out/stills/t<秒>.png`（`:220-234`；`--links` 时另写 `links.json`；**stills 不占渲染槽**，`:179` 只在非 stills 时 `acquireSlot()`）；`--mkv` → 只 concat 无损 ffv1 输出（`:294-298`）；`--tmap map.json` → 单调三次（Fritsch–Carlson）分段重映射（`loadTmap`，`:137-167`），段边界是硬切、MB 子样本永远用帧中心所在段（不跨切点）；`--from/--to` 帧区间；`--page/--query` 换页/传参。

### 2.4 运动模糊：MB× 时间超采样 + tmix [实测 render.mjs]

- 每输出帧渲染 `MB` 个子样本，子样本时间（`:267`）：`t = Math.max(0, (f + SHUTTER * ((s + 0.5) / MB - 0.5)) / FPS)`，`s ∈ [0, MB)`。SHUTTER=0.5（默认）时窗口 = 帧 ±0.25 帧，即 180° 快门；子样本按 `(s+0.5)/MB` 均匀铺在窗口内。
- 编码侧：PNG 流按 `FPS×MB` 帧率喂 ffmpeg（每 PNG = 一个子样本），`tmix=frames=MB` 把连续 MB 帧平均，`select=eq(mod(n,MB),MB-1)` 只保留每组最后一帧，`setpts=N/(FPS*TB)` 重定时到输出帧率 → 每组 MB 个子样本合成 1 输出帧（`:260-263`）。**成本 = 帧数 × MB**。
- 各 demo 默认 MB（`window.DEMO.motionBlur.samples`，`--mb` 可覆盖）[实测 grep]：`09-bauhaus` 8、`02-line-art`/`08-morph` 4、其余 12 个 1；shutter 全部 0.5。demo 还可**片内**用同一参数做 shader 级切片（`09/film.js:9` `const MB = +(Q.get('mb') || window.DEMO.motionBlur.samples);`；`:587` `gl.uniform1f(U('slice'), k * (window.DEMO.motionBlur.shutter / 30) / MB);`）。
- 与 `--tmap` 组合：子样本时间经段函数映射后再渲染（`:269`），并 clamp 到 `[0, duration-1e-3]`。

### 2.5 辅助机制

- **机器级并发槽**（`:124-140`）：`/tmp/mg-render-slots/slot0..N`（目录即锁，内含 pid；`MG_RENDER_SLOTS` 默认 3；死 pid 或 mtime>30 s 判陈旧并回收；`process.on('exit'/'SIGINT'…)` 释放）。注释原文：「captures are GPU-serialized anyway; this bounds RAM use.」
- **进度**（`:276-280`）：每 30 帧打印 `n/total frames · 秒 · 秒/帧`；结束打印 `done → out.mp4 (秒数, with audio …)`。
- **preview.html**：`?demo=01-flat-vector` 载 iframe；拖动条量化到帧（`Math.floor(x*D.fps+1e-6)/D.fps`）；播放「as fast as the page can draw」（重页面掉帧，渲染器则每帧必采）；`out/audio.wav` 存在则同步播放。

## 3. 音频管线

### 3.1 cues.json：单表双读（画面 + 声音 + 有时还有物理）

提示词把这条写成硬流程（`prompts/01-flat-vector.md:57`）：「Keep one cue sheet (beats and hit times) that both the picture and the sound read from.」15/15 个 demo 都有 `cues.json`，三种表形 [实测]：

**表形 A｜帧号表（01-flat-vector 等）**：`{"fps":30,"bpm":120,"key":"F","mode":"major","build":4.0,"drop":6.0,"outro":8.0,"frames":{"impact1":15,"launch":31,"sunLand":40,…,"letters":243,…}}`。画面侧 `01/index.html:61-62`：`const cues = await (await fetch('/demos/01-flat-vector/cues.json')).json(); const FR = cues.frames; const F = n => n/30; const T = k => FR[k]/30;`；声音侧 `01/audio.py:8-9`：`cues = json.load(open(...'cues.json')); FR = cues['frames']; T = lambda k: FR[k]/30.0; F = lambda n: n/30.0`——同一数字两种读法（帧号÷fps），且 `bpm/key/build/drop/outro` 直接喂配方（`audio.py:11` `recipes.pop(bpm=cues['bpm'], key=cues['key'], build=cues['build'], drop=cues['drop'], outro=cues['outro'])`）。

**表形 B｜秒表 + 附属块（09-bauhaus 等）**：顶层 `bpm/beat/M/gridY0/drop/freeze/end` + `events:[{id,t,t0,until,sfx,x,gx,gy,note}]`（t0=预备动作起点、until=状态保持终点、x/gx/gy=屏幕坐标给声像用）+ `ripples`（R1–R4 转场描述）+ `letters/ticker/trim/labels`。画面 `09/film.js:16` 与声音 `09/audio.py:9-10` 各自 `Object.fromEntries(events.map(...))` 出同一张 `EV` 表；声音侧逐条 `m.sfx(..., at=EV['circle_land']['t'], pan=pan_x(720))`（`09/audio.py:31-60`）。

**表形 C｜具名时间字段（04-3d-render）**：`fps:24` + `camA/sweep1/ping/drops/hop_air/build/counter_sweep/camB/tremble/ball_enter/hang/ball_contact/hero/shock_speed/camC/tagline/end_hold/lifts/crown_hang`；且 `_derived` 字段明写：「exact contact / rebound / hop / capsule-landing times are written by blender/sim.py to out/events.json (**audio.py reads both**)」——Blender 物理算出的接触时刻经 `out/events.json` 回流给音画两侧（`04/audio.py:2` 注释「Timing from cues.json + out/events.json」；`:13` 读 cues）。

### 3.2 audio.py 用法（以 01 为例）[实测]

- 读表 → 选配方 → 加 SFX → 导出：`01/audio.py:8-11`（读表+`recipes.pop`）、`:43` `m.sfx(sfx.whoosh(0.42,'swish',direction=1,peak=0.4), at=F(7), gain=-16, pan=-0.2)`、`:106` `res = m.export('out/audio.wav', lufs=-14, tp=-2.2, spectrogram='out/audio_spec.png')`。
- SFX 时间**永远给视觉事件时间**，不给预补偿（sync point 由合成器负责：whoosh 的 sync=掠过峰值、riser/reverse cymbal=末点即命中，mgaudio README §1）。
- 声画同步细节：`sync.place(..., early_frames=1, fps=30)` 让瞬态读在命中帧上；01 还做了「pre-hit suck」——音乐总线在每个视觉运动峰值前 ~60 ms 下潜 9 dB、命中瞬间回弹（`01/audio.py:96-100`：`pts += [(h-0.095,0),(h-0.055,-9),(h-0.006,-9),(h,0)]` 后 `m.group('music').automate('gain', pts…)`）。
- 第二轮修订留痕：源码内 `# R2:` 注释（如 `01/audio.py:25`「R2: the 4.0 ping sits 5 dB lower, no plate send」）。

### 3.3 mgaudio：recipes / SFX / sync point [实测]

- **规模**：48 kHz float 立体声，numpy+numba（PolyBLEP 振荡器、TPT ladder/SVF、Karplus-Strong、FM），pedalboard 效果；README 自述「10 秒整混音 3–8 秒出」「Everything is deterministic (seeded)」。
- **概念**（README §1 原文要点）：「Sound = buffer + `sync` point」；「Levels by construction」（每个 `sfx.*` ≈ −18 dB 短时 K-RMS、峰值 ≤ −1 dBFS，`gain` 只表意图）；music/sfx 两组总线，音乐在每个 SFX 点自动 3 dB duck；「Mono-compatible stereo」（M/S 展宽，禁用 Haas 延迟法；VCSL 立体声采样加载时通道对齐）；form 锚定 `bar 0 = drop`，`chord_at(t)` 让调性 SFX 不跑调。
- **recipes**：15 个（synthwave/darksynth/vaporwave/chiptune/techno/acid/pop/future_bass/trap/glitch_hop/lofi/ambient/guofeng/variety/explainer）；`STYLES` 把 **22 个 demo slug** 映射到配方（`recipes/__init__.py:22-47`，含 7 个未发布风格 11/13/14/15/16/17/21）；`for_style('13-text-flash', drop=3.2)`（`:55`）。`bpm=None + hits=[…]` 时自动挑最贴命中点的速度（`m.form.fit_err` 报最大误差）。
- **SFX 12 族**（README §3 表）：motion / tension-hits / UI / liquid / paper-desk / glitch / retro-media / sci-fi-HUD / magic / 8-bit / cartoon-综艺 / text，全部归一化、`seed=` 可出变体。
- **Mix/Track API**：`track.add(sound, at)`、`loop(fn, pattern)`、`automate('gain'|'lpf'…)`、`duck(by='kick')`、`region('stutter'|'tape_stop'|'mute'|…)`、`m.bus(name, fn)`（room/plate/hall/delay…）、`m.master_kw.update(...)`、`export(path, lufs=-14, tp=-1, spectrogram=…)`（`mix.py:534`）。
- **QC**：`analyze()` 返回 `{duration, lufs, true_peak, stereo_corr, bands, onsets(±5 ms), warnings…}`；warnings 含「duration ≠ 10.000 s、LUFS 偏差 >0.6、TP > −1、DC、clipping、sub > 45 %、presence > 7 %、silence gap > 0.6 s」等（README §7）；`spectrogram(marks=hits)` 出频谱图人核。

### 3.4 母带链与 −14 LUFS [实测 master.py]

`master()`（`master.py:97-153`）逐步：`HPF 28 Hz(4 阶)` → 去 DC → **120 Hz 以下转单声道**（`mono_bass=120`）→ 可选 tilt/air/width → glue comp（ratio 2、目标 1.5 dB GR）→ 可选 tape warmth → **20 kHz 线性相位 FIR 低通**（`_fir_lp`:44，去掉 20–24 kHz 让限幅器可预测）→ `4 ms 淡入 / 250 ms 淡出` → 响度归一：目标 `lufs=-14`（pyloudnorm，BS.1770-4；`lufs()`:16），用 4x 过采样检测的 lookahead 限幅器（`limiter()`:66，ceiling 起点 `tp-0.25`）迭代逼近 ±0.08 LU，再用**理想带限（FFT 8x）真峰**（`true_peak()`:26，注释原文「the strictest reading, ≥ any BS.1770 4x meter (ffmpeg ebur128)」）复核，超限则收紧 ceiling 重跑（最多 3 轮），最后 `tp-0.1` 安全增益。写盘 `PCM_24`（`write()`:155）。
- 交付口径（README 首段原文）：「Output: 24-bit WAV, exactly 10.000 s, -14 LUFS integrated, true peak <= -1.1 dBTP on the strict ideal (band-limited FFT) reading (≈ -1.2 on a BS.1770 4x meter such as ffmpeg `ebur128=peak=true`).」
- 重跑一致性（README:134 原文）：「Rerun with the versions in `requirements.txt`, **4 of them match the films' audio (within the least significant bit) and the other 11 differ in places**, probably because of changes in the numerical libraries.」→ 11/15 非位级可复现 [原文]。

### 3.5 102 个 flac 的来源：VCSL（CC0）[实测]

- **来源链**：`select_vcsl.py` 从 VCSL（Versilian Studios Community Samples，`sgossner/VCSL`）的 GitHub tree JSON 里按 42 条 RULES（folder 子串 + 正则）挑子集 → 写 `vcsl_list.tsv`（每行 `key\tpath\turl`，url 形如 `https://raw.githubusercontent.com/sgossner/VCSL/master/Chordophones/Zithers/Dan%20Tranh/FX/FX_01.wav`）→ `download_vcsl.sh` curl 到 `/tmp/vcsl_raw/<key>/` → `build_samples.py` 重采样到 48 kHz、按 `MAXDUR` 裁剪、写 FLAC + `index.json`（音名→midi 正则、力度层映射）。
- **库内实存**：`lib/audio/samples/` 共 103 个文件 = **102 个 .flac + index.json**，15 类 [实测 `git ls-files` 计数]：piano 39、kalimba 13、glock 9、marimba 9、harp 6、vibraphone 6、woodblock 5、timpani 4、crash 3、slapstick 3、cabasa 1、guiro 1、suscymbal 1、vibraslap 1、wineglass 1。（README:29/117 自述「103 recorded instrument samples」——按文件数含 `index.json` 恰为 103；102 flac 为精确计数。）
- **许可**：README:140 原文「The instrument samples (VCSL), the HDRI, the paper texture, the photos and the HUD film's map data (Natural Earth) are CC0 or public domain.」；mgaudio README 首段亦写「CC0 VCSL samples」；`samples.py` docstring：「Sample engine for the bundled CC0 VCSL subset (see SAMPLES.md).」

## 4. Blender 支线（04-3d-render）6 步流程

### 4.1 六步命令（README 原文）[原文]

`demos/04-3d-render/README.md`（raw 直读，全文见 §7.3 原样输出）：
```bash
python3 blender/make_letters.py                          # 字形 → 充气字母网格 assets/mesh/*.ply（已附带）
python3 blender/sim.py                                   # 全部运动 → work/anim.npz，碰撞时间 → out/events.json（已附带）
blender -b --factory-startup -P blender/scene.py         # 搭场景 → work/scene.blend
blender -b work/scene.blend -P blender/render.py -- --range 0:239   # 240 帧 → out/frames/（macOS 用 Metal；NVIDIA 设 MG_DEVICE=OPTIX）
python3 audio.py                                         # 配乐 → out/audio.wav
cd ../.. && node harness/render.mjs demos/04-3d-render   # 合成 → out/video.mp4
```
分工（README 原文）：「画面由 Blender（5.1，Cycles）渲染成序列帧，`index.html` 再把帧、文字和颗粒合成，最后和别的片子一样用渲染脚本出片。」

### 4.2 逐脚本拆解 [实测 raw 直读]

**① make_letters.py（系统 Python）**：字形→网格。管线（docstring 原文）：「Fredoka (OFL) wght 700 glyph -> hi-res mask -> signed distance -> pillow heightfield -> implicit volume |z| - h(x,y) -> marching cubes -> PLY per glyph (units: x-height = 1.0).」关键常数：光栅 `PX=1000`、`HI=2`；体素 `VOX=1/170`；圆管剖面 `R=0.22`、最大半厚 `H=0.23`、宽处鼓包 `PUFF=0.05`；14 轮 Taubin 平滑（λ=0.55/−0.58，抗 marching-cubes 台阶痕，docstring 注「no shrink」）；导出二进制 PLY + `glyphs.json`（xmin/xmax/zmax/advance/verts/faces/vol）。v5 模式换 ResourceHanRounded Heavy 的 3/D/渲/染。

**② sim.py（系统 Python，非 Blender）**：确定性运动。docstring 原文：「Deterministic motion for 'soft.' — every value is a closed-form / precomputed function of time.」要素：
- 常数：`G=16.0`（统一重力）、`rng = default_rng(7)`、`fr = arange(-PAD, NF+PAD)`（PAD=3 帧给运动模糊子帧留边界；`common.py` 里 `FPS=24, NF=240, PAD=3`）。
- 药丸阵列：六角栅格 `PITCH=0.228`；颜色/倾角/缩放用低频 value-noise + 逐粒随机抖动；`STRAY`（近场 1/40、其余 1/200）躺倒药丸。
- 字母动力学：**1-D 接触 ODE**（`bed_force` 指数刚度弹簧 + 阻尼；`letter_track` dt=1/2400）出底部高度 z(t) 与果冻压缩 s(t)（阻尼振子被床面减速度踢出）；四种下落旋转 `drop_rot`；接触后顶部弯曲振荡 + 待机呼吸。
- 球（铬点）：Hermite 关键段（快入→悬停 5.80–5.93→1 帧内砸下）+ 触地后同一 ODE（重参数 A=1.0/λ=0.033/Cd=62：陨坑 ~0.28D、一次小跳、静沉 12 %）。
- 药丸场：连续高度场 `wave_height` = 扫掠带（`sweep`）+ 接触涟漪（`ring` 阻尼余弦波包）+ 字母/球接触半径；`R(t)` 让「皇冠悬停」段场时钟 0.35x、后段 ~1.35x 追平（r2 修订）。
- 相机：5 个关键位姿（macro/establish/3-4 right/frontal）+ `expo_out` 长尾缓动（docstring：「k=7.2 -> 80 % of the travel in the first 20 % of the time」）+ 命中后阻尼晃动；焦点独立追踪。
- **产物**：`np.savez_compressed(work/anim.npz, …)` 全量逐帧数组（LOC/ROT/SCL 每帧 N×3、CAM/CAMROT/FOC、球与字母通道）；`json.dump(out/events.json)` 接触时刻表（`letter_contacts`/`ball_contacts`/`hops`/`lift`…，事件=（时间, 撞击速度）对；已提交，头 40 行实读）。

**③ scene.py（Blender python）**：读 `work/anim.npz` 搭场景存 `work/scene.blend`。要点：`--factory-startup` 从空场景建；Cycles GPU（`MG_DEVICE` 默认 METAL，渲染机 OPTIX/CUDA）；`samples=24` + 自适应 0.035 + OIDN 降噪 + `use_persistent_data`；1920×1080、`use_motion_blur=True`、`motion_blur_shutter=0.5`；view transform 依次尝试 Khronos PBR Neutral→AgX→Standard，`exposure=-1.2`；世界=studio HDRI（`assets/hdri/studio_small_09_2k.hdr`）+ 彩色化/提亮 + 「glossy ray 看明亮渐变天空、diffuse 用暗 HDRI」的光路分离；材质四件（自发光 cyc 背景、双色药丸体=GN instancer 属性 fx + AO、SSS 果冻 Burley、镜面铬球）；几何=cyc 曲面 + 药丸原型 + **每帧 shape-key 的 3 顶点/粒 field data 网格**（`dme.vertices.add(3*N)` + `pack(k)`）。

**④ render.py（Blender python）**：`blender -b work/scene.blend -P blender/render.py -- --range 0:239`。CLI：`--frames/--range/--pct/--samples/--thresh/--out/--nomb(关运动模糊)/--skip(断点续渲)/--shutter 'f=val,f=val'(逐帧快门覆盖)/--nolink(v5 无点渲染)`；`sc.frame_set(f)` 后逐帧渲染 PNG，**先写 `.tmp.png` 再 `os.replace` 原子换名**（注释：「atomic: a killed render never leaves a half-written plate」），每帧打印 `FRAME f 秒数`。

**⑤ audio.py**：同 15 支片的音频流程（§3），04 用 cues 表形 C。

**⑥ 网页合成（04/index.html）**：`loadFrame(i)` 载 `out/frames/%04d.png`（`:118`，双 plate 交叉淡入开场分级）；`renderAt(t)`（`:126`）叠 DOM 文字层（英文行逐词上浮+去模糊+字距、规则线 scaleX、中文行、椭圆 scrim、前景渐进虚化 dofl）；**hero punch**（帧 144 起 6 帧 1.035→1.0 + 4 帧 2/−1.5/1/−0.5 px 抖）、**end-hold creep**（8.4 s 后 ~1.2 % 持续推进防死停）、**grain boil**（每帧换种子哈希位移）；然后同一条 harness 管线出片（Blender 帧是「底」，文字/颗粒/暗角是「面」——文字不进 Blender）。

### 4.3 关键设计 [归纳]

- **物理先算成数据、渲染只读数据**：`sim.py` 一次算出全片逐帧数组（npz）+ 事件表（json），Blender 场景与网页合成都只消费这两份产物；接触时刻还能回流给 audio.py 卡点（`04/cues.json` 的 `_derived` 字段）。
- **中间产物全落盘可复核**：PLY（字形网格）→ npz（运动）→ events.json（时刻）→ blend（场景）→ frames/*.png（画面）→ audio.wav → video.mp4，每步独立可重跑（`--skip` 续渲、`--frames` 单帧抽渲）。
- **240 帧 = 24 fps × 10 s**（`common.py` `NF=240`），与其余 14 支的 30 fps 不同（本地卡统一写 30 帧的差异见 B-10 §3.3 注记）。

## 5. rubric.md 两段式评审流程

文件开头原文（`rubric.md`）：「原片都是这样迭代出来的：制作 → 独立评审 → 按评审修改 → 再评审。下面两段提示词可以直接用。」

### 5.1 第一段：评审（另开一个 AI 会话）[原文]

- **身份**：「You are a senior motion-design jury member (think: Motionographer editor, Buck/ManvsMachine creative director, a 抖音/B站 top design-account lead for the Chinese styles). You did NOT make this film. Judge it harshly and precisely… Kindness is useless here; specificity is everything.」
- **先看片**：「extract a contact sheet (a frame every 0.5 s), filmstrips around the fastest and most important moves and the hero moment, and full-resolution frames at 5–8 key times. Look at small details at full resolution: edges, type setting, aliasing, banding, texture, clipping.」
- **核 spec**：「exactly 10.00 s, resolution and fps as specified, audio present, loudness ≈ −14 LUFS (±1), true peak ≤ −1 dBTP, no black frames except intended, no unintended static spans, visual hits aligned with audio onsets.」
- **7 维 1–10 打分**，锚点原文：「5 = competent student work; 6 = decent template level; 7 = solid professional; 8 = high-end agency work; 9 = award shortlist; 10 = best in the world. **Most first renders deserve 5–7. Do not inflate.**」
  1. `style_fidelity`（风格识别度：signature feature 全在场且正确）
  2. `concept_wow`（0.5 s 内有钩子、明确 hero moment、满足的收尾帧）
  3. `motion_craft`（缓动/间距/重叠/预备-跟随/弧线/转场/运动模糊）
  4. `design_typography`（构图/层级/网格/中西文字排/配色/留白）
  5. `finish_texture`（光感/纹理/颗粒/辉光；无 banding/aliasing）
  6. `sound_sync`（音乐性/风格正确/音效/同步/混音母带）
  7. `technical`（spec 达标、字体加载、无 glitch/clipping/popping）
- **5–10 条按影响力排序的修复**：「Each: timecode(s), what is wrong (observable), why it matters, and a concrete how-to (technique and numbers: easing curve, frame counts, px, colours, font, layout change). Prefer a few big upgrades over many nitpicks. At least one fix must raise the wow factor, not just polish.」
- **critical 旗标**：「anything that reads as generic or AI-template, unnatural Chinese copy, fallback fonts or tofu, and any spec failure.」
- 返回：「the score table, the critical issues, and the fix list.」

### 5.2 第二段：修改（回到制作会话）[原文]

「Raise the film to award level (**target ≥ 9 in every dimension**)」；先存版本 N；逐条落实或说明替换理由（「You may substitute a better solution for a listed fix if you are confident; say why」）；「Go beyond the list where you see a bigger upgrade, especially for the wow factor. Do not regress anything the jury listed as a strength.」；「Re-render at full resolution, re-check the spec and look at the frames until the fixes have truly landed. Report which fixes you applied or skipped, and why.」

### 5.3 终评分级（15 支实测分）[实测]

`prompts/*.md` 头部「**原片**…AI 评审终评 X / 10」15 条：8.21 NEON DRIVE（10-synthwave，最高）、8.14 NOGGIN（06）、8.07×3（05 手作 / 12 Aurora / 20 PIXEL QUEST）、8.00 ISOPOLIS（03）、7.93 KESTREL-9（22）、7.71×3（04 soft. / 09 KONSTRUKTION / 19 手机元素）、7.64×4（01 popwise / 02 ATELIER LINEA / 08 一形万象 / 18 喵呜日记）、**7.57 drop.（07-liquid，最低）**。全部落在「7=professional」档（7.57–8.21，均值 ≈7.86 [归纳]）。README 自述「Each film went through two rounds of review and revision」。

## 6. 抄什么 / 不抄什么（映射 B-02 / B-03 / B-07）

### 6.1 抄（仓库件 → 拿到什么 → 映射）

| # | 仓库件（路径） | 抄什么 | 映射 |
|---|---|---|---|
| 1 | `harness/render.mjs` 契约（`:4-7,92-101`） | `DEMO{width,height,fps,duration,motionBlur}` + `renderAt(t)` + `__ready` + `seek()` 化 CSS/WAAPI 的**确定性渲染契约最小可执行定义**；B-02 的 `window.seek(frameIndex)` 契约可补秒制变体 `renderAt(t)`（互转：`t=frame/fps`） | **B-02** §1；B-11 契约条款 |
| 2 | `render.mjs --stills 0.5,2,4.25`（`:220-234`） | 「先出 6–10 张关键帧」的**现成实现**（PNG 落盘 + `--links` 记元素轨迹） | **B-02** §4、**B-07**（关键帧步骤可直接复用） |
| 3 | 运动模糊 = MB× 时间超采样 + `tmix`（`:260-267`） | 不依赖后期模糊的确定性做法：子样本时间公式 + ffmpeg 滤镜串，可原样抄 | **B-02** §2 |
| 4 | `cues.json` 单表双读（§3.1） | 音画同源**数据结构**：一份事件表两处消费；三种表形任选 | **B-02** §3、**B-07** |
| 5 | `lib/audio/mgaudio`（全库） | 逐帧片配乐引擎：recipes+SFX+母带+QC 一条龙；「sync point」「levels by construction」「mono-safe」三条设计原则 | **B-02** §3、**B-07**（音频侧现成解） |
| 6 | `master.py` 链（`:97-153`） | −14 LUFS/−1 dBTP 可抄实现：理想带限真峰读数 + 限幅复核收紧循环；交付口径可直接引用 | **B-07**（交付验收）、B-02 §3 |
| 7 | Blender 6 步（§4.1） | 「物理先算数据（npz/events.json）→ 场景只读数据」的分层；`--factory-startup`、原子写帧、`--skip` 续渲、`--shutter` 逐帧覆盖 | **B-03**（blender/workflow.md 对照：本机 5.2.1 已实测无头渲染，仓库为 5.1.x；步骤结构一致） |
| 8 | `rubric.md`（全） | AI 评审 rubric 完整文本：7 维锚点句（「6=template level…Do not inflate」）+ critical 旗标 + 两段式闭环 | **B-11**（评审 rubric）、**B-07**（评分口径） |
| 9 | `template.md` + `prompts/*.md` Rules 三条 | 四段模板（Output/Route/Seed/Signature）+ 硬条款（确定性/素材许可/中文文案）；「Keep one cue sheet」进流程 | **B-11**、**B-08**（迁移指南） |
| 10 | `package.json`/`requirements.txt` 版本钉法 | 依赖全钉死（puppeteer-core 25.12.0 / numpy 2.4.6 / numba 0.66.0…）＋ README:134 对「重跑非位级一致」的坦白——给 B-07 一个「可复现性声明」模板 | **B-07** |

### 6.2 不抄 / 要改 [归纳，理由带证据]

1. **`MG_CHROME` 默认值**（macOS 路径，`render.mjs:29`）：Windows 必须显式指向 `chrome.exe`；同理 `/tmp/mg-render-slots`（`:125`）在 Windows 需换路径。
2. **GPU flags 默认**（`:31-34`）：本机（RTX 5070 Ti Laptop / Windows）两套默认都不适用——用 `MG_GPU_ARGS` 覆盖或先做 PSNR 对照。
3. **字体**：`assets/fonts/README.md` 只列 44 个字体文件的落盘路径，**字体本体不在库内**——不抄字体，自备并自核许可（OFL 等）。
4. **体积**：整仓 555 MiB（`videos/` 417.6 MiB）；只读分析用稀疏克隆（本次 3.2 MB），不要把 videos/samples 全量拉进本项目树。
5. **音频位级复现期望**：README:134 自述 11/15 重跑有差异（数值库漂移）——验收按听感/QC 数值（LUFS/TP/onsets），不按位级一致。
6. **v5 辅助脚本缺口**：`04/index.html:168` 引用 `blender/dot_track.py -> out/v5/dot_track.json`，但 `dot_track.py` 不在仓库（`git ls-files` 无）——v5 联动元素链路不可完整复刻；抄 linkAt 机制即可。
7. **24 fps 例外**：04/05 是 24 fps、18 是 1080×1920；从仓库抄 demo 时逐片对齐 fps/分辨率，别被「统一 30 帧」的本地卡误导（B-10 §3.3 同注）。
8. **`site/` 展示层**（vendor highlight.js BSD-3、`data.js` 165 KB）：与渲染/音频管线无关，本项目不做展示站，不抄。

### 6.3 实测坑位（B-07 端到端回填，2026-10-15）[B-07 实测，经 Main 回填]

1. **跨帧状态泄漏只有乱序重渲才能抓到**：给 `fillStyle` 赋非法值时浏览器不报错、静默沿用上一帧的值，同序重渲看不见，须打乱帧序重渲一遍——正是本仓契约「every frame is a pure function of time t」（§2.1）要防的那类 bug。
2. **非连续帧号拼图须用 `-f concat`**：ffmpeg 的 `k%04d` 图像序列模式只读第 1 帧，帧号不连续时必须显式列清单（本仓 harness 走 image2pipe 流式喂帧，天然规避此坑，§2.3）。
3. **像素风文字建议自绘点阵字体**：浏览器字体抗锯齿会引入调色板外灰阶、破坏 16–32 色硬约束（仓库 20-pixel 用像素字体 `'Fusion Pixel 12'` 属同思路，`20-pixel/index.html:9`）。

## 7. 缺口：读不到 / 没跑的部分

### 7.1 读不到（明确列出；「未读到」≠「不存在」）

1. `videos/*.mp4`（15 支，417.6 MiB）与封面 jpg：未下载，未做任何帧级对照（延续 B-10 §5.7 的缺口）。
2. `lib/audio/samples/*.flac` 与 `index.json` 本体：稀疏克隆未检出（只经 `git ls-files` 计数 102 flac + 15 类；未听任何采样）。
3. `assets/` 二进制（HDRI 6.3 MB、纸纹/尘埃 PNG、grain）：未读，未核分辨率/许可细节（README 自述 CC0）。
4. `demos/06-collage/assets/gen/*`（19 个生成素材）、`18-hanazi/assets/*`（15 个）、`19-paperclip/assets/stickers/*`（8 个）、`02-line-art/tools/*` 等 demo 素材与工具脚本：未逐一实读。
5. `site/data.js`（165 KB）：只知结构（name/name_en/en/work/about），未逐条读。
6. 15 条提示词只精读 01、04（+07 头部）；其余 12 条未逐条读（B-10 已做规则数字对照，本文不重复）。
7. `lib/audio/mgaudio/` 21 个模块只精读 `master.py`（+ `__init__/__main__/core/samples` 头部、`recipes/__init__`）；`mix.py/sfx.py/qc.py/sync.py` 等只读到 README 级 API 说明。
8. `blender/dot_track.py`：被引用但**不在仓库**（§6.2-6）；`work/anim.npz`、`work/scene.blend`、`out/frames/*` 均为运行期产物、未提交（`out/events.json` 例外，已提交并读到头 40 行）。

### 7.2 没跑（全部结论来自静态阅读）

- 未跑 `node harness/render.mjs`（未装 repo 依赖/未指向 Chrome）；未跑任何 ffmpeg 命令；未跑 `blender` 脚本；未跑 `python audio.py`（numba 0.66.0 对 Python 3.14 的兼容性未核，见 B-10 §4.3）。
- 因此**渲染时长、MB 成本、PSNR、音频听感、LUFS 实测值**均未在本次验证；文中一切性能数字都是「代码里的常数/注释」而非本机测量。
- 未验证 15 支成片与源码的一致性（B-10 §2.2 已做截图级对照；本文不做重复）。

### 7.3 机械验证（原样输出）

**检查器**：`read` 工具直读 raw URL（2026-10-15 实测可达）。抽 2 条：

**URL 1**：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/demos/04-3d-render/README.md`，read 输出（原样）：

````
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/demos/04-3d-render/README.md
Content-Type: text/plain
Method: text

---

# 04-3d-render 的制作步骤

画面由 Blender（5.1，Cycles）渲染成序列帧，`index.html` 再把帧、文字和颗粒合成，最后和别的片子一样用渲染脚本出片。在这个目录里依次运行：

```bash
python3 blender/make_letters.py                          # 字形 → 充气字母网格 assets/mesh/*.ply（已附带）
python3 blender/sim.py                                   # 全部运动 → work/anim.npz，碰撞时间 → out/events.json（已附带）
blender -b --factory-startup -P blender/scene.py         # 搭场景 → work/scene.blend
blender -b work/scene.blend -P blender/render.py -- --range 0:239   # 240 帧 → out/frames/（macOS 用 Metal；NVIDIA 设 MG_DEVICE=OPTIX）
python3 audio.py                                         # 配乐 → out/audio.wav
cd ../.. && node harness/render.mjs demos/04-3d-render   # 合成 → out/video.mp4
```
````

**URL 2**：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/lib/audio/tools/download_vcsl.sh`，read 输出（原样）：

```
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/lib/audio/tools/download_vcsl.sh
Content-Type: text/plain
Method: text

---

#!/bin/bash
# args: key path url
key="$1"; path="$2"; url="$3"
fn=$(basename "$path")
mkdir -p "/tmp/vcsl_raw/$key"
out="/tmp/vcsl_raw/$key/$fn"
if [ ! -s "$out" ]; then
  curl -s -f -L --retry 3 -m 300 -o "$out" "$url" || echo "FAIL $url"
fi
```

**辅助计数（原样输出）**：
```
$ git ls-files lib/audio/samples | grep -c '\.flac$'
102
$ git ls-files demos | wc -l
154
$ git ls-files | wc -l
384
$ grep -h "终评" prompts/*.md | wc -l
15
```

## 自审四段（LOOP 协议）

**A · 早产出**：骨架先落盘、逐节填充（§1→§7），§7.3 的 raw 输出为实读原样粘贴；全文引用均带「路径:行号」或原文引号。

**B · 反驳**（挑 5 条最强结论试推翻）：
1. 「契约 = DEMO/renderAt/__ready/linkAt/EV」→ 试推翻：全库 grep `window.DUR|window.READY|window.EV` → 无此三个全局；`EV` 仅存于 demo 内部（`09/film.js:16`）、`DUR` 是 demo 内部常数（`02/film.js:9`）、READY 实为 `__ready` → **CONFIRMED**（brief 里的 DUR/READY/EV 对应 demo 侧命名，非 harness 全局）。
2. 「15/15 都有 cues.json 且音画双读」→ 试推翻：`git ls-files 'demos/*/cues.json'` = 15/15；抽 01/09/04 三形各验画面侧与声音侧读表代码 → **CONFIRMED**。
3. 「102 flac 全来自 VCSL」→ 试推翻：`vcsl_list.tsv` 头 5 行 URL 全指 `sgossner/VCSL`；`select_vcsl.py` 生成逻辑；`samples.py` docstring 自述 CC0 VCSL → **CONFIRMED**（未逐条核 102 个文件的 URL 来源，属抽样证实；README「103 samples」与 102 flac 的差异按「103=文件数含 index.json」解释，标 **WEAKENED** 待逐条核）。
4. 「Blender 只渲底、文字回网页合成」→ 试推翻：`04/index.html:126-166` renderAt 只叠 DOM 层 + 载帧；Blender 脚本无文字渲染逻辑 → **CONFIRMED**。
5. 「rubric 两段式闭环有效（15 支全部终评 ≥7.57）」→ 试推翻：分数来自 prompts 头部自述，非独立复算；R2 修订注释（audio.py）与「two rounds」自述互证但无第三方证据 → **WEAKENED**（可证流程存在，不能证分数可信度）。

**C · 机械验证**：见 §7.3（两条 raw URL 原样输出 + 4 条计数命令）。另：本文件所有行号引用取自稀疏克隆 HEAD `49052d8`，与 GitHub main 一致（克隆即 main）。

**D · 小结**（≤14 行）
1. 仓库 = 一条完整可跑的管线：契约化渲染页 → puppeteer 逐帧 → ffmpeg（MB 超采样+tmix）→ mp4；音画共享 cues.json 一张表。
2. 渲染契约 5 件：`DEMO`（含 duration/motionBlur）、`renderAt(t)`、`__ready`、`linkAt(t)`（v5，14/15）、demo 内部 `EV`（cues.events 索引表）。
3. 运动模糊 = 「渲染侧超采样 + ffmpeg tmix」，成本×MB；09 用 8、02/08 用 4、其余 12 个用 1。
4. 音频 = mgaudio（48k/确定性/recipes 15+SFX 12 族/母带 −14 LUFS −1 dBTP/QC）+ 102 个 VCSL(CC0) flac。
5. Blender 支线（仅 04）= 6 步：字形网格→物理 npz+events→场景→240 帧→配乐→网页合成；物理数据先落盘是全链核心。
6. rubric = 两段式（独立评审 7 维锚点 → 回炉 ≥9），15 支终评 7.57–8.21。
7. 抄：契约/--stills/超采样/cues 单表/mgaudio/rubric/Blender 分层（→B-02/B-03/B-07/B-11）；不抄：macOS 默认路径、字体、videos 体积、v5 dot_track 缺口、位级复现期望。
8. 未跑：一切构建/渲染/音频（静态阅读）；缺口集中在二进制资产与运行期产物。
9. 下一步：B-07 以本仓 harness 为候选栈，先跑 01-flat-vector 标定成本（配 MG_CHROME + 字体）；B-11 抄 rubric 全文与「Keep one cue sheet」条款。
