# sources.md — B-02 HTML/WebGL 逐帧渲染工作流 · 来源全量

> 对应 `workflow.md`（同目录）。全部 URL 于 **2026-10-15** 在本机实测：
> **可达 31 条 / 不可达 3 条**（不可达均有等价替代，见文末）。获取方式：`read`（含 MDN 专用通道、jina 渲染）或 `curl` 直取原文后检索。
> 本机 web_search 当日全 provider 限流（429/bot 挑战），故全部来源为直取官方页，无二手转述。

## §1 逐帧确定性渲染

| # | URL | 用途 | 状态 |
|---|-----|------|------|
| 1 | https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame | rAF 频率随显示器刷新率/后台暂停/时间戳精度 1ms —— 不能当时钟 | 可达（read） |
| 2 | https://developer.mozilla.org/en-US/docs/Web/API/OffscreenCanvas | 离屏渲染、worker、transferToImageBitmap/convertToBlob | 可达（read） |
| 3 | https://github.com/mrdoob/three.js/blob/dev/src/renderers/WebGLRenderer.js | setPixelRatio/setSize/preserveDrawingBuffer 默认值、r163 仅 WebGL2 | 可达（read raw 原文） |
| 4 | https://p5js.org/reference/p5/noLoop/ | draw 默认 60 次/秒；noLoop()+redraw() 单步 | 可达（read） |
| 5 | https://github.com/stackgl/headless-gl | Node 无窗口 WebGL；readPixels 取帧；`npm install gl` | 可达（read） |
| 6 | https://github.com/spite/ccapture.js | 虚拟时钟（TimeWarp 劫持 rAF/Date/performance.now）固定步长捕获 | 可达（read） |

## §2 帧捕获与合成

| # | URL | 用途 | 状态 |
|---|-----|------|------|
| 7 | https://pptr.dev/api/puppeteer.page.screenshot | Puppeteer 截图 API（Promise<string>，encoding 选项） | 可达（read） |
| 8 | https://pptr.dev/api/puppeteer.screenshotoptions | path/clip/type/fromSurface/captureBeyondViewport 全选项 | 可达（read） |
| 9 | https://pptr.dev/api/puppeteer.viewport | deviceScaleFactor 缺省 1（整数像素对齐依据） | 可达（read） |
| 10 | https://playwright.dev/docs/screenshots | Playwright 截图（path/buffer/元素） | 可达（read） |
| 11 | https://playwright.dev/docs/api/class-page | screenshot `animations:'disabled'` 选项原文 | 可达（curl 下载 975KB + 检索） |
| 12 | https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/chromium/chromiumSwitches.ts | 缺省启动参数含 `--force-color-profile=srgb`（第 80 行） | 可达（curl 原文 + 检索） |
| 13 | https://chromedevtools.github.io/devtools-protocol/tot/Page/ | captureScreenshot / startScreencast / screencastFrame / Ack 全参数 | 可达（read） |
| 14 | https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL | toDataURL 行为 + 大图警告 + SecurityError | 可达（read） |
| 15 | https://ffmpeg.org/ffmpeg-formats.html#image2-1 | image2 demuxer：`-framerate` 缺省 25、start_number、官方例 | 可达（read + curl 全文 5911 行） |
| 16 | https://ffmpeg.org/ffprobe.html | `-count_frames` 帧数统计 | 可达（curl 原文 + 检索） |

## §3 音频（代码合成 / wav 导出 / 卡点）

| # | URL | 用途 | 状态 |
|---|-----|------|------|
| 17 | https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext/startRendering | 离线渲染 → Promise<AudioBuffer>；构造参数 | 可达（read） |
| 18 | https://github.com/Experience-Monks/audiobuffer-to-wav | AudioBuffer→wav（16-bit PCM/float32；MIT；1 commit） | 可达（read） |
| 19 | https://github.com/Tonejs/Tone.js/blob/dev/Tone/core/context/Offline.ts | Tone.Offline 源码 JSDoc（比实时快；Transport 排程） | 可达（read raw 原文） |
| 20 | https://github.com/Tonejs/Tone.js | Tone.js 总览：时间排程、Tone.start 手势要求 | 可达（read） |
| 21 | https://github.com/ircam-ismm/node-web-audio-api | Node 版 WebAudio（Rust）；CI sinkId 坑 | 可达（read） |
| 22 | http://soundfile.sapp.org/doc/WaveFormat/ | WAV 字节格式经典参考 | **不可达（ECONNREFUSED）** → 替代：#18 源码 / MDN AudioBuffer |

## §4 6 关键帧流程

| # | URL | 用途 | 状态 |
|---|-----|------|------|
| 23 | https://ffmpeg.org/ffmpeg-filters.html#tile | tile 过滤器（layout 缺省 6x5、padding、官方 keyframes 例） | 可达（curl 全文 1.7MB + 定位） |
| 24 | https://imagemagick.org/script/montage.php | montage：-tile geometry/-geometry/-label | 可达（read） |
| 25 | https://imagemagick.org/script/escape.php | `%k` = 唯一色数（CALCULATED）；`%[colors]` | 可达（read） |

## §5 逐帧自查自动化

| # | URL | 用途 | 状态 |
|---|-----|------|------|
| 26 | https://github.com/mapbox/pixelmatch | 像素 diff API/CLI/退出码/windowSize（ISC，无依赖） | 可达（read） |
| 27 | https://github.com/dmtrKovalenko/odiff | SIMD diff；JSON 输出 diffCount/diffPercentage | 可达（read） |
| 28 | https://ffmpeg.org/ffmpeg-filters.html#psnr | PSNR 过滤（stats_file 逐帧；两输入同规格） | 可达（curl + 定位 25304 行） |
| 29 | https://ffmpeg.org/ffmpeg-filters.html#ssim | SSIM 过滤；官方 `"ssim;[0:v][1:v]psnr"` 例 | 可达（curl + 定位 28429 行） |
| 30 | https://ffmpeg.org/ffmpeg-filters.html#signalstats | 逐帧 YMIN/YLOW/YAVG/YHIGH/YMAX 等元数据 | 可达（curl + 定位 27765 行） |
| 31 | https://ffmpeg.org/ffmpeg-filters.html#freezedetect | 冻结检测；noise 缺省 -60dB/0.001；duration 缺省 2s | 可达（curl + 定位 18920 行） |
| 32 | https://playwright.dev/docs/videos | Playwright 视频录制（800×800 缩放、context 关闭后落盘） | 可达（read） |

## 不可达清单（已查 2026-10-15，均给替代）

| URL | 结果 | 替代 |
|-----|------|------|
| http://soundfile.sapp.org/doc/WaveFormat/ | ECONNREFUSED | #18 audiobuffer-to-wav 实现 + MDN AudioBuffer |
| https://threejs.org/manual/en/rendering-on-demand.html | HTTP 404 | #3 WebGLRenderer 源码 JSDoc |
| https://trac.ffmpeg.org/wiki/Create%20a%20video%20from%20a%20sequence%20of%20images | HTTP 404 | #15 ffmpeg-formats image2 章节 |

## 本地来源（非 URL，仅供追溯）

- `research/origin_cards/提示词全文.md` —— 15 卡任务头原文、14/15 张「网页逐帧渲染」、收尾文案清单（[自述]）
- `research/agent-art/cards/structure.md` —— 15 卡结构蒸馏（主脑）
- `templates/style_card.md` —— 卡模板与自查表（任务头/画风/内容/反约束四段）

## 计数（机械核对用）

- 实测（2026-10-15，python `re.findall(r'https?://…')` 于本文件）：**出现 35 次，唯一 URL 34 条**（可达 31 + 不可达 3；soundfile 在 §3 与不可达清单各出现 1 次）。
- 可达 31 = §1(6) + §2(10) + §3(5) + §4(3) + §5(7)。
