# HTML / WebGL 逐帧渲染工作流（B-02）

> 归属：GOALS B-02（HtmlFrameRender）｜状态 v0.1（2026-10-15）｜B-09（逐帧自查自动化）并入本文 §5
> 对齐素材：`knowledge/domains/motion-graphics/origin/提示词全文.md`（15 卡任务头，14/15 张 =「网页逐帧渲染」）
> 证据分级：`[自述]` 本人原话 ｜ `[史料]` ｜ `[研究]` 官方文档/源码（带 URL）｜ `[归纳]` 本项目总结的操作规则 ｜ `[推测]`
> 本机实测环境（2026-10-15）：Node v24.19.0 ✓ ｜ ffmpeg n9.0.1 ✓ ｜ Python 3.14.7 ✓ ｜ ImageMagick **未安装**（`magick -version` → command not found）

## 0. 管线总览

```
storyboard 6 关键帧 ──► seek() 化渲染页 (HTML) ──► 逐帧捕获 (Puppeteer/Playwright)
        │                                              │
        ▼                                              ▼
  contact sheet (tile/montage) ◄── 人审 ──►   frames/f0000.png … f0299.png
        │                                              │
        ▼                                              ▼
  改 seek() 再重渲                    OfflineAudioContext 合成音轨 ──► score.wav
                                                       │
                                                       ▼
                                        ffmpeg 合成 (30fps, 300 帧) ──► out.mp4
                                                       │
                                                       ▼
                                        逐帧自查 (§5) ──► 报告/回归
```

约定（[归纳]）：
- 时间唯一来源 = 帧号；`t = frame / 30`。全程禁用 `requestAnimationFrame` 当渲染时钟、禁用 `performance.now()/Date.now()` 参与动画、禁用未播种随机数。
- 目录：`index.html`（渲染页）｜`render.js`（驱动）｜`frames/`｜`audio/`｜`key/`（关键帧）｜`checks/`（自查产物）。
- 三条硬流程来自 15 卡任务头（原文 [自述]）：**「先出 6 张关键帧给我看，再做动画，最后逐帧自查」**（§4 / §5）；**「配乐音效也用代码合成、跟画面卡点」**（§3）。

## 1. 逐帧确定性渲染

**做法**（[归纳]）
- 渲染页暴露纯函数 `window.seek(frameIndex)`：帧号 → 画面。同一帧号在任何机器、任何次数下必须画出同一画面；补间/物理全部表达为 `f(frame)`，不依赖墙上时钟。
- 捕获方逐帧调用 `seek(f)` 后截图（§2）；页面自己不做循环。
- three.js：`update(t)` 与 `renderer.render(scene, camera)` 分离；`setPixelRatio(1)` + `setSize(W, H, false)`。
- p5.js：`setup()` 里 `noLoop()`，`seek(f){ FRAME = f; redraw(); }`。
- 离屏两条路：页面内 `OffscreenCanvas`（可转移进 Worker）；纯 Node（headless-gl `gl`）。
- 整数像素对齐清单（[归纳]）：① canvas `width/height` 属性 = 输出像素（1920×1080），CSS 尺寸与之相同；② 捕获浏览器 `deviceScaleFactor: 1`；③ 所有坐标 `Math.round`；④ 像素风 `imageSmoothingEnabled = false` + 整数倍放大；⑤ 1-2px 线宽时把坐标落在 `.5` 上或整数格上，避免浏览器抗锯齿糊边。

**依据 URL**
- MDN rAF：回调频率「generally match the display refresh rate」（60/75/120/144Hz），后台暂停；timestamp 最小精度 1ms → rAF 当时钟 = 帧数随机器变。https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame
- MDN OffscreenCanvas：可在 worker 渲染，`transferToImageBitmap()` / `convertToBlob()`。https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas
- three.js WebGLRenderer 源码（dev）：构造参数 `preserveDrawingBuffer = false` 缺省；r163 起仅 WebGL2；`setPixelRatio(value)`；`setSize(width, height, updateStyle=true)`——注释原文「Resizes the output canvas to (width, height) with device pixel ratio taken into account」，内部 `canvas.width = Math.floor(width * _pixelRatio)`。https://github.com/mrdoob/three.js/blob/dev/src/renderers/WebGLRenderer.js
- p5.js noLoop 参考：原文「By default, draw() tries to run 60 times per second. Calling noLoop() stops draw() from repeating… draw() can be run once by calling redraw()」。https://p5js.org/reference/p5/noLoop/
- headless-gl：`npm install gl`，Node 无窗口 WebGL（WebGL 1.0.3），示例用 `preserveDrawingBuffer: true` + `gl.readPixels` 取像素。https://github.com/stackgl/headless-gl
- CCapture.js（v2 重写版）：TimeWarp 劫持 `performance.now / requestAnimationFrame / setTimeout / Date / media currentTime`，「lies to it about what time it is」——保留 rAF 写法时可用它做固定步长；本项目更推荐直接 seek 化（连劫持都不需要）。https://github.com/spite/ccapture.js

**代码骨架**（可复现）

```html
<!-- index.html：Canvas2D 版 seek -->
<!doctype html><meta charset="utf-8">
<style>html,body{margin:0;background:#000}canvas{display:block}</style>
<canvas id="c" width="1920" height="1080"></canvas>
<script>
const FPS = 30, DUR = 10;          // 300 帧
const ctx = document.getElementById('c').getContext('2d', { alpha: false });
ctx.imageSmoothingEnabled = false;  // 像素风必开；矢量风可 true

// 固定种子 PRNG（禁 Math.random）——mulberry32
function rng(seed){ return function(){ seed|=0; seed=seed+0x6D2B79F5|0;
  let t=Math.imul(seed^seed>>>15,1|seed); t=t+Math.imul(t^t>>>7,61|t)^t;
  return ((t^t>>>14)>>>0)/4294967296; }; }

function seek(frame){               // 纯函数：帧号 → 画面
  const t = frame / FPS;            // 唯一时间源
  ctx.fillStyle = '#0b0b0e'; ctx.fillRect(0, 0, 1920, 1080);
  const x = Math.round(960 + 300 * Math.sin(2 * Math.PI * t / 2));  // 整数像素
  ctx.fillStyle = '#ffd166'; ctx.fillRect(x - 60, 480, 120, 120);
  if (frame === 299) { ctx.fillStyle = '#fff'; ctx.font = 'bold 96px sans-serif';
    ctx.textAlign = 'center'; ctx.fillText('收尾文案', 960, 980); } // 验收锚点
}
window.seek = seek;
</script>
```

```js
// three.js 版（同一 seek 契约）
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(1);                    // 与 deviceScaleFactor=1 对齐
renderer.setSize(1920, 1080, false);
document.body.appendChild(renderer.domElement);
function seek(frame){
  const t = frame / 30;
  mesh.position.x = Math.round(300 * Math.sin(t));  // 位移取整
  camera.updateMatrixWorld();
  renderer.render(scene, camera);              // 同步调用，无 rAF
}
window.seek = seek;
```

```js
// p5.js 版
let FRAME = 0;
function setup(){ createCanvas(1920, 1080); noLoop(); }
function draw(){
  const t = FRAME / 30;
  background(11);
  rect(Math.round(960 + 300 * Math.sin(t)) - 60, 480, 120, 120);
}
window.seek = (f) => { FRAME = f; redraw(); };
```

## 2. 帧捕获与合成

**做法**（[归纳]）
- 默认路径 A（帧号精确，推荐）：Node 驱动逐帧 `seek(f)` + `page.screenshot()`。
- 备选 B：页面内 `canvas.toDataURL('image/png')` 把帧作为 base64 流回 Node 写盘（少一层浏览器截图管线；但 MDN 警告大图整串在内存、建议 toBlob）。
- 备选 C：CDP `Page.startScreencast` 实时推流（适合"已跑起来的动画"录制，**不是**逐帧管线：帧来自 frame swap、需 ack 流控，官方不承诺帧号/帧率精确）。
- 合成：ffmpeg image2 demuxer，**必须显式 `-framerate 30`**（缺省 25）。

**依据 URL**
- Puppeteer ScreenshotOptions（v25.14.0）：`path`（扩展名推断格式）、`clip`、`type`（默认 png）、`fromSurface`（默认 true）、`captureBeyondViewport`。https://pptr.dev/api/puppeteer.screenshotoptions
- Puppeteer Viewport：`deviceScaleFactor` 默认 1；`width/height` 为 CSS 像素。https://pptr.dev/api/puppeteer.viewport
- Playwright 截图文档：`page.screenshot({ path })`、buffer 捕获、元素截图。https://playwright.dev/docs/screenshots
- Playwright Page API：screenshot 选项 `animations: "disabled"` ——「stops CSS animations, CSS transitions and Web Animations」；`caret` 可选。https://playwright.dev/docs/api/class-page
- Playwright 启动开关源码：缺省参数含 `--force-color-profile=srgb`（chromiumSwitches.ts 第 80 行）。https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/chromium/chromiumSwitches.ts
- CDP Page 域：`Page.captureScreenshot`（png 默认、clip、fromSurface 默认 true）；`Page.startScreencast`（`everyNthFrame`/`format`/`maxWidth`/`maxHeight`/`quality`，事件 `Page.screencastFrame` 携带 data+metadata{timestamp, monotonicTimestamp}，需 `Page.screencastFrameAck`，`maxFramesInFlight` 默认 3）。https://chromedevtools.github.io/devtools-protocol/tot/Page/
- MDN toDataURL：默认 PNG；**警告**：整图编码进内存字符串，大图有性能问题，建议 `toBlob()`；非同源画布抛 `SecurityError`。https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
- ffmpeg image2 demuxer：`framerate` 选项「Set the frame rate for the video stream. **It defaults to 25**」；`start_number` 默认 0；官方例 `ffmpeg -framerate 10 -i 'img-%03d.jpeg' out.mkv`。https://ffmpeg.org/ffmpeg-formats.html#image2-1
- ffprobe：`-count_frames`「Count the number of frames per stream and report it」。https://ffmpeg.org/ffprobe.html

**代码骨架**（可复现）

```js
// render.js —— Puppeteer 逐帧截图（路径 A）
const puppeteer = require('puppeteer');
const path = require('path');
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
  await page.goto('file:///' + path.resolve('index.html').replace(/\\/g, '/'));
  await page.evaluate(() => document.fonts.ready);      // 字体就绪再开渲
  for (let f = 0; f < 300; f++) {
    await page.evaluate((f) => window.seek(f), f);       // 帧号驱动
    await page.screenshot({ path: `frames/f${String(f).padStart(4, '0')}.png` });
  }
  await browser.close();
})();
```

```js
// 路径 B —— 页面内 toDataURL 流（备选；大图建议换 toBlob）
const b64 = await page.evaluate((f) => { window.seek(f);
  return document.getElementById('c').toDataURL('image/png'); }, f);
require('fs').writeFileSync(`frames/f${String(f).padStart(4,'0')}.png`,
  Buffer.from(b64.split(',')[1], 'base64'));
```

```js
// 路径 C —— CDP screencast（实时录制备选，非逐帧管线）
const client = await page.createCDPSession();
await client.send('Page.startScreencast', { format: 'png', everyNthFrame: 1,
  maxWidth: 1920, maxHeight: 1080 });
let i = 0;
client.on('Page.screencastFrame', async (ev) => {
  require('fs').writeFileSync(`frames/cdp${String(i++).padStart(4,'0')}.png`,
    Buffer.from(ev.data, 'base64'));
  await client.send('Page.screencastFrameAck', { sessionId: ev.sessionId });
});
```

```bash
# 合成（可复现命令）：300 张 PNG → 30fps mp4
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p \
       -crf 18 -movflags +faststart out.mp4
# 像素风（小画布 320×180 整数倍放大）
ffmpeg -framerate 30 -i frames/f%04d.png -vf "scale=1920:1080:flags=neighbor" \
       -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
# 帧数验收：期望 300
ffprobe -v error -count_frames -select_streams v:0 \
        -show_entries stream=nb_read_frames -of csv=p=0 out.mp4
```

> Windows 提示（[归纳]）：以上命令在 bash/cmd 可直接跑；PowerShell 里 `%` 有别名歧义，建议用 bash 或把 `f%04d.png` 用引号包住。

## 3. 音频：代码合成 + 导出 wav + 与画面卡点

**做法**（[归纳]）
- 音轨不录音、不找素材：在 `OfflineAudioContext` 里搭图（oscillator/noise + GainNode 包络，可加 delay/滤波），`startRendering()` 一次性渲染出 `AudioBuffer`，再编码成 wav。
- 卡点按帧做整数规划：帧 → 时间 `t = frame / 30`（秒）；44.1kHz、30fps 下**每帧恰好 1470 采样**（44100 ÷ 30），音画对齐可以精确到帧，无取整误差。
- 两条实现路线：浏览器内渲染（页面里跑 OfflineAudioContext，或 Tone.js `Tone.Offline`）｜纯 Node（`node-web-audio-api`，Rust 实现）。
- 合成：ffmpeg 一条命令把帧序列 + wav 出片；或先出画面再合音（`-c:v copy` 不重编码画面）。

**依据 URL**
- MDN OfflineAudioContext.startRendering：返回 `Promise<AudioBuffer>`；构造示例 `new OfflineAudioContext(2, 44100 * 40, 44100)`。https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/startRendering
- audiobuffer-to-wav：`npm install audiobuffer-to-wav`，`encodeWAV(audioBuffer, [opt])` → ArrayBuffer，缺省 16-bit PCM（format 1），`opt.float32` 写 32-bit float；MIT；多声道自动交织。https://github.com/Experience-Monks/audiobuffer-to-wav
- Tone.js `Offline`（源码 JSDoc）：`Tone.Offline(callback, duration, channels=2, sampleRate)` → `Promise<ToneAudioBuffer>`；「rendering much faster than real time in many cases」；回调里可建节点、沿 Transport 排程；输出走 OfflineAudioContext。https://github.com/Tonejs/Tone.js/blob/dev/Tone/core/context/Offline.ts
- Tone.js README：`Tone.now()`、`triggerAttackRelease("C4","8n", now+0.5)` 这类按 AudioContext 时间排程；注意 `Tone.start()` 需要用户手势（**实时播放**才需要，离线渲染不需要）。https://github.com/Tonejs/Tone.js
- node-web-audio-api：Node 版 Web Audio（Rust 内核 + napi-rs），`npm install node-web-audio-api`；示例用 AudioContext/OscillatorNode/GainNode 包络；CI/无音频设备时用 `{ sinkId: { type:'none' } }`。https://github.com/ircam-ismm/node-web-audio-api

**代码骨架**（可复现）

```js
// 音轨合成：120 BPM 底鼓 + 卡点 beep（浏览器页面或 Node 内跑）
const SR = 44100, FPS = 30, DUR = 10;
const off = new OfflineAudioContext(2, SR * DUR, SR);
function blip(tSec, freq, dur = 0.08, gain = 0.4) {
  const o = off.createOscillator(), g = off.createGain();
  o.type = 'triangle'; o.frequency.value = freq;
  g.gain.setValueAtTime(gain, tSec);
  g.gain.exponentialRampToValueAtTime(0.0001, tSec + dur);
  o.connect(g).connect(off.destination);
  o.start(tSec); o.stop(tSec + dur + 0.01);
}
const beatSec = 60 / 120;                       // 0.5s = 15 帧
for (let b = 0; b < 20; b++) blip(b * beatSec, b % 4 === 0 ? 440 : 220);
// 与画面同表：画面动作帧号 n 的音效时间 = n / 30
[45, 90, 150, 225, 285].forEach(f => blip(f / FPS, 880, 0.05, 0.3));

const buffer = await off.startRendering();      // Promise<AudioBuffer>（MDN）
const wav = require('audiobuffer-to-wav')(buffer);   // ArrayBuffer
require('fs').writeFileSync('audio/score.wav', Buffer.from(wav));
```

```js
// Tone.js 路线（离线渲染，不需要用户手势）
const buf = await Tone.Offline(({ transport }) => {
  const osc = new Tone.Oscillator(440, 'sine').toDestination();
  transport.schedule(t => { osc.start(t).stop(t + 0.1); }, 1.5);  // = 45 帧
  transport.start(0);
}, 10);
```

```bash
# 一步出片（帧序列 + wav）
ffmpeg -framerate 30 -i frames/f%04d.png -i audio/score.wav \
       -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -shortest final.mp4
# 或分两步（画面不重编码）
ffmpeg -i out.mp4 -i audio/score.wav -c:v copy -c:a aac -b:a 192k -shortest final.mp4
```

> 备注：WAV 字节格式经典参考 soundfile.sapp.org 本机不可达（已查 2026-10-15，ECONNREFUSED）→ 以 audiobuffer-to-wav 实现 + MDN AudioBuffer 为准（[研究] 口径降级）。

## 4. 6 关键帧流程（对齐 15 卡「先出 6 张关键帧」）

**做法**（[归纳]，锚点为 [自述]）
- 任务头原文 [自述]：「…**先出 6 张关键帧给我看，再做动画，最后逐帧自查**。」（`knowledge/domains/motion-graphics/origin/提示词全文.md`；14/15 张渲染方式 =「网页逐帧渲染」）
- 流程五步：① 写 storyboard 表（6 行：帧号、画面、动作状态、要核对的画风规则）→ ② 只实现 `seek()` 的 6 个关键状态（不做补间）→ ③ 渲染 6 帧 → ④ 拼 contact sheet 交人看 → ⑤ 通过后才做全片（补间/物理/音频）；**不过就改 `seek()` 重渲，不许改截图糊弄**。
- 10 秒片建议锚点帧：`0 / 45 / 90 / 150 / 225 / 285`（= 0s、1.5s、3s、5s、7.5s、9.5s）；**最后一帧必须含收尾文案**（15 卡每条自带收尾字，是"一帧能核对"的验收锚点）。
- 呈现约定：单张 PNG、3×2 网格、左上→右下按时间排序、每格带帧号 label；全片 1920×1080 时每格 640×360。

**依据 URL**
- ffmpeg tile 过滤器：`layout`（COLUMNSxROWS，缺省 6x5）、`nb_frames`、`margin`、`padding`、`color`；官方例「Produce 8x8 PNG tiles of all keyframes (-skip_frame nokey)…」。https://ffmpeg.org/ffmpeg-filters.html#tile
- ImageMagick montage：`-tile geometry`（number of tiles per row and column, e.g. `-tile 8x`）、`-geometry`、`-label`。https://imagemagick.org/script/montage.php
- 15 卡转录（本地）：`knowledge/domains/motion-graphics/origin/提示词全文.md`（任务头固定句式、14/15 = 网页逐帧渲染、每条自带收尾文案）。

**代码骨架**（可复现）

```js
// render.js 支持只渲关键帧
const KEY = [0, 45, 90, 150, 225, 285];
const only = process.argv.includes('--keys');
const list = only ? KEY : [...Array(300).keys()];
for (const f of list) { await page.evaluate(f => window.seek(f), f);
  await page.screenshot({ path: `key/k${String(f).padStart(4,'0')}.png` }); }
```

```bash
# 拼 3×2 contact sheet（tile 缺省布局 6x5，必须显式写 3x2）
# 非连续帧号（k0000/k0045/…）不能用 k%04d —— image2 要求序号连续，会只读到第 1 帧；
# 用 concat 清单（AnimTest01/B-07 实测）：list.txt 每行 file 'k0045.png'，按时间序排列
ffmpeg -f concat -safe 0 -i key/list.txt -vf "tile=3x2:padding=8:color=#101010" \
       -frames:v 1 key/keyframes_sheet.png
# 或 ImageMagick（IM7；本机未安装，见 §0 实测）
magick montage key/k*.png -tile 3x2 -geometry +8+8 -background '#101010' \
       key/keyframes_sheet.png
```

## 5. 逐帧自查自动化（B-09 并入）

**做法**（[归纳]）：五类检查，按"先机械后人工"排。

1. **确定性回归（P0）**：同一帧渲两遍 → `pixelmatch` 期望 **0 差异**；全片两遍 → ffmpeg `psnr/ssim` 期望满分。跑不过说明有非确定性源（随机数/时钟/字体/GPU 差异）。
   - **B-07 实测升级（2026-10-15，AnimTest01）**：同序重渲不够，要**乱序重渲**（倒序/随机抽帧重渲再比对）——跨帧状态泄漏（如 `fillStyle` 非法值静默沿用上一帧状态）只在乱序时暴露：f0150 实测差 158 像素；修复后 3/3 帧 SHA256 一致。
2. **帧 diff / 回归**：改一处后与基线比 —— `pixelmatch`（OKLab 感知差、抗锯齿感知、`windowSize` 窗口抗噪）或 `odiff`（SIMD，跨格式）。
3. **Contact sheet 审片**：`tile` 或 `montage`；300 帧审片版用 `fps=6` 缩到 10×5 网格。
4. **色彩统计**：`magick identify -format "%k"` 数唯一色数（像素卡「16-32 色」、玻璃拟态「相邻 2-3 色」）；ffmpeg `signalstats` 出逐帧 YAVG/UAVG/VAVG（平均色/亮度漂移）。
5. **运动统计**：`freezedetect` 抓"意外静止/卡帧"；自写逐帧差分曲线找 hold 拍与切拍（核对「一拍二」「动作不短于 0.6 秒」「卡点」）；过冲/回弹（5-10%、约 8 帧）用主体质心轨迹核对（自写）。

**依据 URL**
- pixelmatch：`pixelmatch(img1, img2, output, width, height, {threshold})` 返回差异像素数（缺省 threshold 0.1）；CLI 退出码 0=一致 / 66=有差异；`windowSize` 返回窗口内最大差异数；抗锯齿感知 + OKLab + HyAB；ISC，无依赖，Node/浏览器通用。https://github.com/mapbox/pixelmatch
- odiff：CLI `odiff <IMG1> <IMG2> [DIFF]`；Node `compare()` 返回 `{match, reason, diffCount, diffPercentage}`；支持 png/jpeg/webp/tiff；Zig+SIMD；MIT。https://github.com/dmtrKovalenko/odiff
- ffmpeg psnr/ssim：官方例 `ffmpeg -i main.mpg -i ref.mpg -lavfi "ssim;[0:v][1:v]psnr" -f null -`；`psnr` 的 `stats_file`「save the PSNR of each individual frame」；两输入必须同分辨率/像素格式/帧数。https://ffmpeg.org/ffmpeg-filters.html#psnr / https://ffmpeg.org/ffmpeg-filters.html#ssim
- ffmpeg tile：见 §4（`layout`/`padding`/`color`）。https://ffmpeg.org/ffmpeg-filters.html#tile
- ffmpeg signalstats：逐帧元数据 `YMIN/YLOW/YAVG/YHIGH/YMAX`（及 U/V 同构，[0-255]）。https://ffmpeg.org/ffmpeg-filters.html#signalstats
- ffmpeg freezedetect：检测「no significant change in content during a specified duration」，算法 =「mean average absolute difference of all the components」；`noise` 缺省 -60dB/0.001、`duration` 缺省 2s；触发时元数据 `lavfi.freezedetect.freeze_start/freeze_duration/freeze_end`。https://ffmpeg.org/ffmpeg-filters.html#freezedetect
- ImageMagick 转义：`%k` =「CALCULATED: number of unique colors」（长形 `%[colors]`）。https://imagemagick.org/script/escape.php

**代码骨架**（可复现）

```bash
# ① 确定性：同帧两跑比对（退出码 0 = 完全一致）
pixelmatch frames/f0000.png frames_rerun/f0000.png checks/diff_f0000.png 0.1
# 乱序重渲：倒序/随机抽帧重渲后再比对（跨帧状态泄漏只在乱序时暴露，B-07 实测）
pixelmatch frames/f0150.png frames_rev/f0150.png checks/diff_f0150.png 0.1
# 全片两跑（ffmpeg 官方例写法；逐帧日志落 checks/psnr.log）
ffmpeg -i out.mp4 -i out_rerun.mp4 -lavfi "psnr=stats_file=checks/psnr.log;ssim=stats_file=checks/ssim.log" -f null -

# ② 回归 diff（odiff，JSON 里看 diffCount/diffPercentage）
odiff frames/f0150.png baseline/f0150.png checks/diff_f0150.png

# ③ 审片 contact sheet：300 帧 → 每秒 6 帧 → 10×5 缩略图
ffmpeg -i out.mp4 -vf "fps=6,scale=384:-1,tile=10x5:padding=4:color=#101010" \
       -frames:v 1 checks/sheet.png

# ④ 色彩：唯一色数（像素卡 16-32 色验收）；逐帧平均色
magick identify -format "%f %k\n" frames/f0000.png
ffmpeg -i out.mp4 -vf "signalstats,metadata=print" -f null - 2>&1

# ⑤ 运动：卡帧/静止检测（0.5s 阈值，-60dB 噪声底）
ffmpeg -i out.mp4 -vf "freezedetect=n=-60dB:d=0.5" -map 0:v -f null -
```

```python
# ⑤b 自写：逐帧差分曲线（hold 拍 / 切拍 / 意外跳变一眼可见）
#    运行：python checks/motion.py frames/
import sys, glob
import numpy as np
from PIL import Image
files = sorted(glob.glob(sys.argv[1] + '/*.png'))
prev = None
for i, f in enumerate(files):
    a = np.asarray(Image.open(f).convert('L'), dtype=np.int16)
    if prev is not None:
        print(f"{i}\t{abs(a - prev).mean():.3f}")   # 平台=hold，尖峰=切拍
    prev = a
```

> 自写脚本思路（[归纳]，未跑过整段标 [UNVERIFIED]）：hold 检测 = 连续相同帧计数（对「一拍二」应出现 2-3 帧一组）；卡点 = 差分曲线峰值帧号 vs 音轨包络峰值帧号（音轨可离线再算包络：每 1470 采样一帧取 RMS）；过冲 = 对主体色块做质心跟踪，找"越过目标再返回"的幅度与帧数。

## 6. 工具/库/repo 清单（14 项）

> 可用性判断 = 本机实测（2026-10-15）+ 官方文档/README 读到的维护与分发状态。本机：Node v24.19.0 ✓｜ffmpeg n9.0.1 ✓｜Python 3.14.7 ✓｜ImageMagick 未安装。

| # | 名称 | URL | 用途 | 可用性判断 |
|---|------|-----|------|-----------|
| 1 | three.js | https://github.com/mrdoob/three.js | WebGL2 3D 渲染（r163+ 仅 WebGL2）；`setPixelRatio/setSize/setAnimationLoop/render` 全可控 | 活跃（dev 分支持续提交）；npm `three`；源码 JSDoc 即文档 |
| 2 | p5.js | https://p5js.org/ | 2D canvas 创意编程；`noLoop()+redraw()` 可做单步 seek | 活跃（参考文档 v2.3.3）；npm/CDN；适合 2D 排版卡 |
| 3 | Puppeteer | https://pptr.dev/ | 无头 Chrome 驱动 + 逐帧 `page.screenshot` | 活跃（文档 v25.14.0）；npm `puppeteer` 自带 Chromium；本机未装，可 `npm i` 现取 |
| 4 | Playwright | https://playwright.dev/ | 截图（`animations:'disabled'`）+ 测试视频录制 | 活跃；缺省启动参数含 `--force-color-profile=srgb`；npm |
| 5 | ffmpeg | https://ffmpeg.org/ | image2 合成、tile/psnr/ssim/signalstats/freezedetect、ffprobe | **本机 ✓ n9.0.1**（gyan 系构建，2026-08-28）；Windows 用 gyan.dev/BtbN 构建 |
| 6 | ImageMagick | https://imagemagick.org/ | montage 拼图、`%k` 色数、compare | **本机未安装**（`magick` not found）；需要时 winget/choco 安装；contact sheet 可用 ffmpeg tile 平替 |
| 7 | pixelmatch | https://github.com/mapbox/pixelmatch | 像素级 diff（OKLab+抗锯齿感知），确定性回归 P0 检查 | 7k stars；ISC；零依赖；CLI+Node；`npm i pixelmatch pngjs` |
| 8 | odiff | https://github.com/dmtrKovalenko/odiff | 高速 diff（Zig+SIMD），跨格式，JSON 输出 | 3.3k stars；MIT；`npm i odiff-bin` 或单文件二进制 |
| 9 | audiobuffer-to-wav | https://github.com/Experience-Monks/audiobuffer-to-wav | AudioBuffer → wav（16-bit PCM/float32） | npm 可用；MIT；**维护停滞（仓库仅 1 次提交）**→ 代码短，必要时自 fork |
| 10 | Tone.js | https://github.com/Tonejs/Tone.js | WebAudio 音乐框架；`Tone.Offline` 离线渲染音轨 | 14.8k stars；活跃（dev 分支）；npm `tone` |
| 11 | CCapture.js | https://github.com/spite/ccapture.js | 固定帧率捕获；虚拟时钟劫持（rAF/Date/performance.now） | 已重写为 v2（ES modules/WebCodecs）；npm `ccapture.js`；适合"不想改渲染代码"的场合 |
| 12 | p5.capture | https://github.com/tapioca24/p5.capture | p5 sketch 一键录制（WebM/GIF/MP4/PNG zip） | 313 stars；MIT；CDN/npm `p5.capture@1.6.1`；p5 生态快速出片 |
| 13 | headless-gl (`gl`) | https://github.com/stackgl/headless-gl | Node 无窗口 WebGL（WebGL 1.0.3）；`readPixels` 出帧 | 1.9k stars；Node 20+；Win/mac/Linux 预编译二进制；`npm i gl` |
| 14 | node-web-audio-api | https://github.com/ircam-ismm/node-web-audio-api | Node 版 Web Audio（Rust）；离线合成音轨 | 265 stars；BSD-3；npm；CI 无音频设备需 `sinkId:{type:'none'}` |

## 7. 缺口与未决

- **不可达（已查 2026-10-15）**：soundfile.sapp.org WAV 规范页（ECONNREFUSED）；three.js manual `rendering-on-demand.html`（404）；ffmpeg wiki「Create a video from a sequence of images」（404）→ 均已用等价官方源替代（audiobuffer-to-wav / WebGLRenderer 源码 / ffmpeg-formats image2）。
- **搜索通道**：web_search 全 provider 限流（429/bot 挑战），本文所有来源为 read/curl 直取官方页，未采用二手转述。
- **[UNVERIFIED]**：整条管线未在本机端到端跑过（无现成渲染页）；§5 自写脚本为思路骨架。
- **未评估**：node-canvas（Node 2D canvas）、`puppeteer-screen-recorder`（CDP 录制封装）、OpenCV（运动分析重武器）——留给 B-07 实验按需引入。
- **待办**：B-07 端到端实验时，用本文 §1-§5 骨架真跑一支 10s 片，把实测坑位回填本节。

## 自审（LOOP 协议四段）

### A 早产出
先落盘骨架（§0-§2）再补 §3-§4、§5-§7；`sources.md` 同步建立；关键帧流程与自查清单均已成节。中间产物 = 本文件 + `sources.md`（同目录）。

### B 反驳（逐条试推翻）

1. **「逐帧截图 = 像素级可复现」** → 试推翻：Playwright 缺省加 `--force-color-profile=srgb`（chromiumSwitches.ts:80），说明跨环境颜色本不保证一致；GPU 光栅化差异真实存在。**WEAKENED**：同机同参数下可复现（须用 §5-P0 证明而非假设），跨机不承诺。命令：grep `chromiumSwitches.ts` → 命中第 80 行 `'--force-color-profile=srgb',`。
2. **「ffmpeg 按文件名序号自动按 30fps 合成」** → 试推翻：image2 文档 `framerate` 选项「defaults to 25」——不写 `-framerate 30` 时 300 帧会变 12s 片（30→25fps 拉伸）。**CONFIRMED（作为坑位）**：命令必须显式带 `-framerate 30`。命令：read ffmpeg-formats.html §3.14 原文（见 §2 依据）。
3. **「canvas.toDataURL 是逐帧导出的主路径」** → 试推翻：MDN 明确警告「encodes the whole image in an in-memory string… prefer toBlob()」，且非同源画布抛 SecurityError。**WEAKENED**：降级为备选 B，主路径改 Puppeteer 截图。
4. **「CDP screencast 可当逐帧渲染管线」** → 试推翻：CDP 文档中 screencast 是 frame-swap 推送 + `screencastFrameAck` 流控（`maxFramesInFlight` 默认 3），无帧号语义。**OVERTURNED**：改判为"实时录制备选"，不是逐帧管线（§2 已按此改写）。
5. **「p5.js 直接数 draw 调用就是帧数」** → 试推翻：noLoop 文档「draw() tries to run 60 times per second」，循环不关就没有"帧号"概念。**CONFIRMED**：骨架强制 `noLoop()+redraw()` 单步化（§1）。

### C 机械验证

**① URL 抽检 3 条（2026-10-15 用 `read` 复读，原样节选）**

- 抽 #4 `https://p5js.org/reference/p5/noLoop/`：
  > "By default, draw() tries to run 60 times per second. Calling `noLoop()` stops draw() from repeating. The draw loop can be restarted by calling `loop()`. draw() can be run once by calling `redraw()`."
  > （页脚源码链接指向 `src/core/structure.js` v2.3.3）
- 抽 #5 `https://github.com/stackgl/headless-gl`：
  > "`gl` lets you create a WebGL context in Node.js without making a window or loading a full browser environment."
  > "npm install gl" ｜ "Prebuilt binaries are generally available for LTS node versions (e.g. 20, 22, 24)" ｜ Stars: 1899
- 抽 #24 `https://imagemagick.org/script/montage.php`：
  > "[-tile geometry] number of tiles per row and column (e.g. -tile 8x)"
  > "[-geometry geometry] preferred size or location of the image"

**② sources.md URL 计数（python `re.findall` 实测）**
```
occurrences: 35 | unique: 34
```
（可达 31 + 不可达 3；≥15 条要求满足）

**③ 本机工具链实测（bash）**
```
v24.19.0
ffmpeg version n9.0.1-11-ge47273f4d9-20260828 Copyright (c) 2000-2026 the FFmpeg developers
Exiting with exit code 0
error: command not found: magick
Python 3.14.7
```
（ffmpeg 的 configuration 行较长已截断；`magick` 缺失 → §6 第 6 项"可用性判断"据此写明"本机未安装"）

### D 小结（≤14 行）
- 已确立：seek 化（帧号唯一时间源）是整套管线的地基；捕获三路径的取舍有官方依据；ffmpeg `-framerate 30` 与 image2 缺省 25 是必须写死的坑；音画对齐在 44.1k/30fps 下有整数关系（1470 采样/帧）。
- 已确立：自查五件套全部有现成工具（pixelmatch/odiff/ffmpeg 四过滤器/ImageMagick %k），无需从零造。
- 被推翻：CDP screencast 不是逐帧管线（改判实时录制备选）。
- 被削弱：toDataURL 主路径（降级备选）；"像素级可复现"限同机同参。
- 未知：整管线端到端实测（留给 B-07）；本机无 ImageMagick 的替代已给（ffmpeg tile）。
- 下一步：B-07 用本文骨架真做一支 10s 片回填坑位。
- 我仍赌错的可能：Chrome 无头在不同版本间截图仍有细微差异（字体栅格化/GPU），P0 检查可能发现需锁 Chrome 版本。
