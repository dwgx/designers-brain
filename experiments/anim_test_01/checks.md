# checks.md — B-07 端到端实验 #1《像素小渔夫 · 大丰收！》

> 归属：GOALS B-07（AnimTest01，wave3）｜实验日期 2026-10-15｜目录 `experiments/anim_test_01/`
> 来源卡：`knowledge/domains/motion-graphics/origin/提示词全文.md` 第 11 条「像素 PIXEL」（画风段 + 内容段原文见 §7）
> 管线依据：`knowledge/agent-art/html/workflow.md` §1-§5（seek 化 + 逐帧截图 + ffmpeg 合成 + 自查五件套）
> 证据分级：本文件全部数字 = 本机实跑输出（原样粘贴）；推断处标 `[推测]`。

**结论一行：out.mp4 = 1920×1080 / 30fps / 300 帧 / 10.000s（含代码合成音轨），全片唯一色数 24（落在画风段要求的 16-32 内），6 张关键帧 + 拼图齐备，结尾「大丰收！」在 f270 起出现并保持到末帧；同帧重渲 SHA256 逐字节一致（且以乱序重渲验证 seek 自洽）。**

## 1. 交付物清单

| 文件 | 大小 | 说明 |
|---|---|---|
| `out.mp4` | 2,140,784 B | 成片（h264 + aac，300 帧 / 10.000s） |
| `video.mp4` | 1,893,113 B | 无音轨画面版（编码中间产物，便于回归比对） |
| `index.html` | 渲染页 | `window.seek(frame)` 纯函数；320×180 内部画布 ×6 放大 |
| `render.js` | 驱动 | puppeteer-core 逐帧截图（`--keys/--frames/--probe/--rerun`） |
| `audio.html` + `render_audio.js` | 音轨 | OfflineAudioContext 合成 → `audio/score.wav` |
| `frames/f0000.png … f0299.png` | 300 张 | 逐帧 PNG（1920×1080） |
| `key/k0000/k0050/k0100/k0150/k0200/k0250.png` + `key/keyframes_sheet.png` | 6+1 张 | 6 关键帧 + 3×2 拼图（带帧号标签） |
| `checks/` | — | 自查脚本、原始输出、探针帧、对照图 |
| `package.json` / `node_modules/` | — | 依赖只装在实验目录内（puppeteer-core 24.43.1） |

## 2. 验收命令（原样输出）

```bash
$ ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 out.mp4
300

$ ffprobe -v error -show_entries stream=index,codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels -show_entries format=duration,size,bit_rate -of default=nw=1 out.mp4
index=0
codec_name=h264
codec_type=video
width=1920
height=1080
r_frame_rate=30/1
nb_frames=300
index=1
codec_name=aac
codec_type=audio
sample_rate=44100
channels=2
r_frame_rate=0/0
nb_frames=432
duration=10.000000
size=2140784
bit_rate=1712627

$ ls key/*.png
key/k0000.png  key/k0050.png  key/k0100.png  key/k0150.png  key/k0200.png  key/k0250.png  key/keyframes_sheet.png

$ ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,sample_rate,channels -of default=nw=1 audio/score.wav
codec_name=pcm_s16le
sample_rate=44100
channels=2
duration=10.000000
size=1764044
```

## 3. 唯一色数（画风段硬指标 16-32 色）

`python checks/selfcheck.py`（脚本：`checks/selfcheck.py`；1920×1080 → 320×180 网格取样，每 6×6 块取中心像素）原样输出：

```
=== 1. 帧文件与块结构 ===
frames/*.png count = 300
block uniformity: 200/200 sampled 6x6 blocks are single-color

=== 2. 唯一色数（全片 300 帧并集） ===
unique colors across ALL 300 frames = 24
per-frame unique: min=23 max=24 mean=23.3
colors outside declared 25-color palette = 0 []
palette entries actually used = 24 ['brn0', 'brn1', 'gold0', 'gold1', 'gold2', 'grn0', 'ink0', 'ink1', 'pink0', 'red0', 'sky0', 'sky1', 'sky2', 'sky3', 'sky4', 'sky5', 'sun0', 'sun1', 'wat0', 'wat1', 'wat2', 'wat3', 'wat4', 'white']
```

- 24 色 ∈ [16, 32] ✓；单帧最少 23 色、最多 24 色（无帧低于下限）。
- 调色板在 `index.html` 顶部硬编码 25 个 `#rrggbb`（第 12 行起），实测用到 24 个（`ink2` 被随后画的竿身覆盖，未出现在成片像素里）。
- 「块结构」检查 = 每个 6×6 输出块单色，即 ×6 放大是**最近邻**（关平滑）而非插值：抽检 200 块全通过。
- CRT 扫描线（画风段「可以加一点」）：每 3 行压暗 1 行，压暗目标**全部取自同一调色板**（`DIM` 表），故不增加色数 —— 这是把「CRT 扫描线」与「≤32 色」两条约束同时满足的做法 `[归纳]`。

## 4. 6 关键帧抽查（0/50/100/150/200/250）

```
=== 3. 6 关键帧 ===
key/k0000.png: 1920x1080 15508B sha256:ac1b4781b695bdbf
key/k0050.png: 1920x1080 15418B sha256:1ccd665f1a640296
key/k0100.png: 1920x1080 15924B sha256:735c3fbae3cee0ff
key/k0150.png: 1920x1080 16029B sha256:e9c58cf798f26140
key/k0200.png: 1920x1080 15970B sha256:75dfe829d94fbb56
key/k0250.png: 1920x1080 16079B sha256:410f115ba07b199b
keyframes_sheet.png: (1936, 728)
pairwise differing-pixel counts (of 57600):
  k0000     0  1016  1516  2026  1725  2365
  k0050  1016     0  2120  1350  2403  1722
  k0100  1516  2120     0  2251  2112  2294
  k0150  2026  1350  2251     0  1696  1890
  k0200  1725  2403  2112  1696     0  2838
  k0250  2365  1722  2294  1890  2838     0
```

- 6 张全部 1920×1080；两两差异 1016–2838 源像素（每张 57600）→ 6 张确实是 6 个不同画面（不是同一帧复制）。
- 6 个锚点对应的分镜：`k0000` 开场定场 → `k0050` 抛竿挥杆 → `k0100` 等待（鱼线横跨画面）→ `k0150` 浮漂下沉（咬钩）→ `k0200` 大鱼跃出水面 → `k0250` 提鱼在手 + 金币开始落。
- 拼图 `key/keyframes_sheet.png` = 3×2、左上→右下按时间、每格 640×360、带帧号标签（ffmpeg `drawtext` + `tile`）。
  **坑位（StyleCardTemplates 实测转告 + 本机复现）**：`-i key/k%04d.png` 对不连续帧号（0000/0050/…）只读到第 1 帧，拼出 1 格图；本机改用 `-f concat -safe 0 -i list.txt`（`file`+`duration` 交替）才拿到 6 帧。另本机 ffmpeg n9.0.1 已无 `-vsync`（改 `-fps_mode`）。

## 5. 结尾文案「大丰收！」帧

```
=== 4. 结尾文案「大丰收！」帧 ===
frames/f0269.png: white(text) pixels in bbox = 0
frames/f0270.png: white(text) pixels in bbox = 132
frames/f0273.png: white(text) pixels in bbox = 496
frames/f0299.png: white(text) pixels in bbox = 496
f0299 文案位图（32px 字面 -> 16x16 字面；左->右：大 丰 收 ！）:
  ................  ................  ................  ................  
  .......##.......  .......##.......  .####...........  .......##.......  
  .......##.......  .......##.......  ...##.....##....  .......##.......  
  .......##.......  .......##.......  ...##....##.....  .......##.......  
  ..############..  ...##########...  ...##...##......  .......##.......  
  .......##.......  .......##.......  ...##..##.......  .......##.......  
  ......####......  .......##.......  ...##.##########  .......##.......  
  .....##..##.....  .......##.......  ...##...##......  .......##.......  
  ....##....##....  ....########....  ...##....##.....  .......##.......  
  ...##......##...  .......##.......  ...##.....##....  .......##.......  
  ..##........##..  .......##.......  ...##......##...  ................  
  .##..........##.  .......##.......  ...##.......##..  .......##.......  
  ##............##  ..############..  ...##........##.  .......##.......  
  #...............  .......##.......  .###.........##.  ................  
  ................  .......##.......  ................  ................  
  ................  ................  ................  ................  
```

- 出现时机：f0269 = 0 像素（无文案）→ f0270 起出现（先 1 帧 16px 小字，f0273 起放大 2× = 32px 字面，离散两档、无补间）→ 保持到 f0299（末帧）。
- 文案是**自绘 16×16 点阵字**（`GLYPH` 表，4 个字：大/丰/收/！），不走浏览器字体渲染 —— 字体渲染会引入抗锯齿灰阶，直接破坏「16-32 色」；点阵字 + 调色板色是同时满足「出现文案」与「色数受限」的唯一做法 `[归纳]`。
- 验收帧 `checks/out_t9.6.png` = 从 `out.mp4` 第 9.6s 抽帧，画面含「大丰收！」+ 提在手里的鱼 + 金币。
- 全程审片图 `checks/review_sheet.png`（每 15 帧抽 1 帧 × 20 张 = 5×4，384×216/格，ffmpeg `concat`+`tile`）：第 1 行开场→挥竿→抛竿，第 2 行等待（鱼线横跨），第 3 行咬钩→拉锯→大鱼跃出，第 4 行提鱼在手→文案出现并保持。分镜与 §7 时间轴一致。

## 6. 确定性回归（P0）

```
=== 5. 确定性回归（同帧两跑，SHA256 比对） ===
f0000: IDENTICAL  ac1b4781b695bdbf / ac1b4781b695bdbf
f0150: IDENTICAL  e9c58cf798f26140 / e9c58cf798f26140
f0299: IDENTICAL  cd62334b4581e3e0 / cd62334b4581e3e0
```

- 命令：`node render.js --frames` 出全片后，`node render.js --rerun 299,150,0` **按逆序**重渲 3 帧 → SHA256 与 `frames/` 逐字节相同。逆序渲染即证明 `seek(frame)` 不依赖上一次调用的画布状态（自洽纯函数），比同序重渲更强。
- **这条检查抓到了一个真 bug（本次实验最重要的实测收获）**：`drawCloud()` 里曾把打包好的 `PAL32` 整数直接赋给 `ctx.fillStyle`——非法 CSS 值会被浏览器静默忽略、沿用上一次的样式，于是云的配色取决于**上一帧**遗留状态：同序重渲看起来一致，逆序/乱序重渲就变色（实测 f0150 差 158 个源像素）。修法两条：① 云的配色改用 `HEX.*` 字符串；② `seek()` 开头显式 `g.fillStyle = HEX.ink0` 清状态。修完 3 帧全 IDENTICAL。→ 回填 `workflow.md` §5 的建议：**P0 检查必须乱序重渲**，同序重渲会漏掉状态泄漏类 bug。

## 7. 技术规格对照（brief 逐条）

| 规格 | 实现 | 证据 |
|---|---|---|
| 1920×1080 | 输出 canvas 1920×1080；截图视口 1920×1080 @ deviceScaleFactor 1 | §2 ffprobe width/height |
| 30fps | `-framerate 30`（image2 缺省 25，必须显式写死） | §2 `r_frame_rate=30/1` |
| 10s = 300 帧 | `NFRAMES=300`，`f = 0..299` | §2 `nb_read_frames=300`、`duration=10.000000` |
| 画布 320×180 整数倍放大、关平滑 | 内部 canvas 320×180，`drawImage` 到 1920×1080（×6，整数）；两处 `imageSmoothingEnabled=false` | §3 块结构 200/200 |
| 全片 16-32 色 | 25 色调色板硬编码；实测 24 色 | §3 |
| 渐变用像素交错抖动 | 天空/水面/倒影用 2×2 Bayer 有序抖动逐像素选色 | §3（抖动可见于 `key/*.png`）；代码 `drawBackground` |
| 角色 8-12 张/秒、离散帧、无补间 | `BEAT=3` → 姿态每 3 帧换一张 = **10 张/秒**；姿态来自 `POSE` 表（10 个命名姿态、身体 sprite 6 张），竿角/手臂按姿态查表 | 代码 `poseName()`；成片「40% 帧与前帧完全相同」= 10Hz 离散的直接后果（§9） |
| 所有位置取整 | 所有绘制入口 `rect/px/line` 均 `|0` 取整，位移/弧度 `Math.round` | §3 块结构（半像素会被最近邻放大暴露成 12px 双色块，实测无） |
| 无运动模糊 | 全片无 blur/filter/alpha 混合，硬边填充 | §3 调色板外颜色 = 0（抗锯齿/混合必然产生新色） |
| 结尾「大丰收！」 | f270 起，点阵字，保持到末帧 | §5 |
| 背景分层整像素滚动 | 云两层：1px/6 帧（远）、1px/3 帧（近） | 代码 `drawClouds()` |
| 可以加一点 CRT 扫描线 | 每 3 行压暗 1 行（调色板内映射，不增色） | §3 |
| 别做成：运动模糊 / 半像素 / 顺滑缓动角色 | 均未使用 | §3 + 代码 `seek()` |

## 8. 音轨（画风段：配乐音效也用代码合成、跟画面卡点）

- 合成方式：`audio.html` 里 `OfflineAudioContext(2, 44100*10, 44100)` 一次性离线渲染（无采样、无录音、无 Math.random —— 噪声源用播种 mulberry32）。
- 卡点机制：所有事件时间 = `帧号 / 30`，与画面同一张帧表；44.1kHz 下每帧恰好 1470 采样。
- 事件表（帧号 → 声音）：f45 挥杆风声 / f63 入水水花+咕咚 / f100 竿尖轻点 / f144 咬钩前上扬 / f150 浮漂一沉闷响 / f156 惊觉 / **f166–194 收线棘轮每 3 帧一击（与 10Hz 姿态同拍）** / f196 大鱼跃出（大水花+弹起）/ f212 落水 / f216 起竿 / f240 钟声 / **f250–298 金币声 ×9（每 6 帧一枚）** / f270 文案砸下（低频冲击）/ f272 收尾钟。
- 配乐：120 BPM、2s/小节 ×5（Am-F-C-G-C），三角波低音+和弦垫+八分方波琶音+噪声沙锤，第 3-5 小节加五声旋律。
- 渲染输出：

```json
{"wav":"...\\audio\\score.wav","bytes":1764044,"samples":441000,"sampleRate":44100,"channels":2,"peakBeforeLimit":0.5856,"limitGain":1,"errors":[],"seconds":0.5}
```

- 峰值 0.5856 < 1 → 未触发软限幅（`limitGain=1`），无削波。
- 逐秒包络（`wave` 读回 wav 实算，验证「不是哑轨」且高潮落在结尾）：

```
wav frames 441000 sr 44100 dur 10.0
  t=0-1s rms=0.032 peak=0.206
  t=1-2s rms=0.026 peak=0.204
  t=2-3s rms=0.036 peak=0.341
  t=3-4s rms=0.024 peak=0.177
  t=4-5s rms=0.036 peak=0.319
  t=5-6s rms=0.038 peak=0.431
  t=6-7s rms=0.042 peak=0.342
  t=7-8s rms=0.028 peak=0.191
  t=8-9s rms=0.061 peak=0.552
  t=9-10s rms=0.079 peak=0.586
```

## 9. 耗时与可复现命令

```bash
node render.js --frames      # 300 帧 -> frames/      : 18.3s（16.4 fps 捕获，含浏览器启动）
node render.js --keys        # 6 关键帧 -> key/       : 0.7s
node render.js --rerun 299,150,0   # 乱序重渲 3 帧 -> checks/rerun/ : 0.4s
node render_audio.js         # OfflineAudioContext -> audio/score.wav : 0.5s
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 15 -preset medium -movflags +faststart video.mp4   # 1.37s
ffmpeg -i video.mp4 -i audio/score.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4                     # 0.30s
python checks/selfcheck.py > checks/selfcheck_output.txt
```

- 端到端（画面渲染 → 成片）≈ **21s**（不含脚本编写）。逐帧截图是本管线的瓶颈：1920×1080 PNG 每帧约 60ms。
- 环境：Windows / Node v24.19.0 / puppeteer-core 24.43.1 + `chrome-headless-shell 153.0.8010.36`（`C:/Users/dwgx1/.cache/puppeteer/…`，未额外下载浏览器）/ ffmpeg n9.0.1 / Python 3.14.7 + numpy 2.5.3 + Pillow 12.3.0。
- 浏览器启动参数：`--force-color-profile=srgb --hide-scrollbars --disable-gpu --disable-lcd-text --force-device-scale-factor=1`（`--disable-gpu` 走软件光栅，配合确定性检查实测通过）。

## 10. 与官方参考成片对照（同系统、不同种子）

参考：`ref/20-pixel.mp4`（`Vincentwei1021/mg-styles-15`，MIT，1920×1080 / 30fps / 300 帧 / 10.000s，与本案同规格）。抽 3 帧 = `ref/ref_1.png`（f0）/`ref_2.png`（f150）/`ref_3.png`（f299）。

```
--- 本项目 out.mp4 逐帧 PNG（frames/） ---
frames = 300
unique colors (union) = 24
per-frame unique: min=23 max=24 mean=23.3
identical-to-previous frames (holds) = 119/299 (40%)
mean abs diff per frame: mean=0.92 max=5.25 frames with diff>1.0 = 116

--- 官方 20-pixel.mp4（ref/all/） ---
frames = 300
unique colors (union) = 464735
per-frame unique: min=74 max=25663 mean=18386.2
identical-to-previous frames (holds) = 0/299 (0%)
mean abs diff per frame: mean=7.16 max=171.70 frames with diff>1.0 = 190
```

> 说明：`ref/all/`（300 张参考帧）在跑完后已删除以省盘，重建命令见 `checks/ref_compare.py` 头注释。

差异与解读（避免误读，逐条给口径）：

1. **色数不可直接比**：参考是 h264 有损成片，任何一帧解码后都有上万色（编解码噪声）；本项目比的是**渲染源帧 PNG**，24 色是硬数。若要同口径，应对参考做「解码后量化再数」`[推测]`。**能确定的**：官方样片走的不是「PNG 逐帧 16-32 色」的自查口径，而本项目按画风段字面把 16-32 色做成了可机械验收的硬指标。
2. **构图/内容不同（不同种子）**：参考 f150 是「神秘宝箱/欢迎来」平台跳跃场景（对话框、宝箱、小人、圆角黑边框 CRT 造型），本项目是湖边夕阳钓鱼。两者只在**风格语法**上可比：都用抖动渐变天空、暖色云底、硬像素边、带黑描边的点阵中文大字 —— 这几条本项目都命中。
3. **内部像素栅格**：参考的像素块约 4px（内部 ≈480×270），本项目 6px（内部 320×180，画风段举的例子）。两者都是「小画布整数倍放大」。
4. **帧更新节奏不可直接比**：参考的 holds=0 是 h264 噪声导致（任何相邻帧都有差异），不能据此说参考「无 hold」。本项目的 40% hold 来自 10Hz 离散姿态 + 10Hz 水纹（一段安静等待里 3 帧一拍的 2 帧与前帧相同）——这正是画风段「每秒 8-12 张、不做补间」的直接后果。
5. 参考片有一条本项目没有的：**圆角黑边框（CRT 屏幕造型）**。画风段只提「可以加一点 CRT 扫描线」，本项目做了扫描线、没做外框 `[归纳]`（可选，未做）。

## 11. 缺口与未做（不假装）

- **未做**：参考片的圆角 CRT 外框；参考片里那种「对话框/UI 元件」元素（本片内容段不需要）。
- **口径限制**：`seek()` 的「同一帧号 → 同一画面」在本机同参数下逐字节成立；跨机器/跨 Chrome 版本不承诺（GPU 光栅化、颜色管理差异真实存在，与 `workflow.md` §5 的 WEAKENED 结论一致）。`--disable-gpu` 是本次锁定的条件之一。
- **未测**：pixelmatch/odiff 未引入（本机用 SHA256 全等 + 源像素差分替代，够用且零依赖）；`freezedetect` 未跑（自写「零差分帧」统计已覆盖同一目的，且对 10Hz 离散动画更准）。
- **音质**：合成音轨是「够用的卡点音效 + 极简配乐」，不是编曲级成品；未做母带/多轨混音。
- **`[UNVERIFIED]`**：`out.mp4` 在其它播放器上的 A/V 同步未逐台核（本机 ffprobe 报两轨均 10.000s）。

## 12. 自审四段（LOOP 协议）

### A 早产出
先落盘可跑的最小链路（`index.html` + `render.js` 出 9 张探针帧）→ 看图改画（鱼形、太阳倒影、云、浮漂）→ 再出 6 关键帧 + 拼图 → 全片 300 帧 → 音轨 → 成片 → 自查脚本。中间产物全程落盘（`checks/probe/`、`checks/*_output.txt`）。

### B 反驳（逐条试推翻）

1. **「逐帧截图管线是确定性的」** → 试推翻：`--rerun` 逆序重渲，f0150 差 158 源像素。**OVERTURNED（已修）**：根因是 `fillStyle` 被赋非法值后静默沿用上一帧状态。修法见 §6；修后 3/3 IDENTICAL。命令：`node render.js --rerun 299,150,0` + `python checks/selfcheck.py`。
2. **「色数 24 是渲染出来的，不是取样假象」** → 试推翻：若放大用了插值，块结构检查会失败；若调色板外有颜色，`outside=0` 会失败。**CONFIRMED**：200/200 块单色 + 调色板外 0 色。
3. **「320×180 内部画布 ×6 = 输出 1920×1080」** → 试推翻：若 CSS 又缩了一次或 deviceScaleFactor≠1，块结构/尺寸都会露馅。**CONFIRMED**：ffprobe 1920×1080 + 6×6 块单色 + 视口 deviceScaleFactor=1。
4. **「文案是浏览器字体画的」** → 试推翻：字体抗锯齿会产生大量灰阶，与 24 色矛盾。**CONFIRMED（反向）**：文案是自绘点阵（`GLYPH` 16×16 表），§5 的位图即从成片帧反读出来的字面。
5. **「40% 帧与前帧完全相同 = 渲染卡帧 bug」** → 试推翻：若卡帧，`frames/` 会连续重复且动作不进位；实测重复帧严格按 3 帧节拍分布且每拍姿态确实换了一张（§7 姿态表 + 关键帧两两差异）。**WEAKENED→CONFIRMED（设计使然）**：这是 10Hz 离散动画的正常外观，不是丢帧。

### C 机械验证（粘原样输出）

- 帧数/时长/规格：见 §2（`300` / `duration=10.000000` / `r_frame_rate=30/1`）。
- 色数/关键帧/文案/确定性：见 §3–§6（`checks/selfcheck_output.txt` 全文）。
- 与官方参考对照：见 §10（`checks/ref_compare_output.txt` 全文）。
- 浏览器控制台错误：每次 `render.js` 运行的 JSON 里 `"errors":[]`、`"selftest":"ok"`（sprite/字面行宽自检在页面内先跑，行宽不符会抛异常并被 `pageerror` 捕获）。

### D 小结（≤14 行）

- 已确立：seek 化（帧号唯一时间源）+ 320×180×6 最近邻 + 自绘点阵字 + 调色板内扫描线压暗 —— 这四件合起来才能同时满足「像素画风段」的量化约束；16-32 色在本机做成了**可机械验收**的硬指标（实测 24）。
- 已确立：`image2` 缺省 25fps、非连续帧号拼图只读 1 帧、ffmpeg n9 无 `-vsync` —— 三个坑都在本机复现并写进 §4/§9。
- 被推翻（最重要）：同序重渲不足以证明确定性；**乱序重渲**才抓到 `fillStyle` 状态泄漏 bug。建议回填 `workflow.md` §5 P0 检查。
- 被削弱：与官方样片的色数/节奏对照只能给口径差异，不能给「谁更对」的结论（有损 vs 无损、不同内容）。
- 未知：跨机器可复现性；参考片真实内部栅格与真实帧更新率（只有 h264 成品可查）。
- 下一步（给 B-13 手册 / B-08 迁移指南）：把「乱序重渲 P0」「非连续帧号拼图用 concat」「字面自绘避抗锯齿」三条写成模板级注意事项。
- 我仍赌错的可能：10Hz 离散在长等待段是否显得过静（40% hold）——这取决于审美，Owner 看片后可让水纹/云提速到 15-30Hz（背景层允许连续滚动），代码里只改一个 `beatOf` 的粒度。
