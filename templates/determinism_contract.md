# 确定性渲染契约 v0.1（可直接粘进提示词）

> 版本 v0.1（2026-10-15）｜归属 GOALS B-11（StyleCardTemplates）
> 来源：`knowledge/domains/motion-graphics/cards/mg-styles-15_compare.md` §3.1–3.2（B-10）+ `knowledge/agent-art/html/workflow.md` §1–2、§5（B-02）+ 仓库 `Vincentwei1021/mg-styles-15` raw 直读（`harness/render.mjs`、`prompts/01-flat-vector.md`、`template.md`，2026-10-15）。
> 许可：条款提炼自 mg-styles-15（MIT，Copyright (c) 2026 Vincentwei1021）；引用/再分发保留此署名。
> 用法：新建风格卡时把 §1 条款块整段粘进提示词（任务头/Rules 段）；捕获与合成命令取 §2；完成后按 §3 自查。

## 1. 契约条款块（英文，逐条可查；C1–C10）

```text
Deterministic rendering contract (mandatory; C9/C10 are route-specific):
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
C6. EV / cue sheet: one cue sheet (beats and hit times, e.g. cues.json) is read by BOTH the picture and the
    sound; audio is synthesised in code (OfflineAudioContext or equivalent), never recorded; the event at frame
    n lands at exactly n / fps seconds (44.1 kHz / 30 fps → exactly 1470 samples per frame).
C7. Output spec: 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz),
    mastered to −14 LUFS integrated, true peak ≤ −1 dBTP. Final file: video.mp4.
C8. Assets and copy: only CC0 / public domain / OFL / Apache / free-for-commercial-use; every source and licence
    recorded in CREDITS.md; no real brand trademarks (invent names); on-screen Chinese natural and correctly
    punctuated.
C9. Blender route (equivalent contract): render a PNG sequence from scripts (blender -b --factory-startup -P ...,
    explicit --range 0:239), no live simulation during capture; physics precomputed to data files
    (work/anim.npz, out/events.json) that the composite page reads.
C10. Stills before motion: render the 6 key times first, the last still contains the end copy; full render only
    after the stills pass human review.
```

- C1–C8 直接可粘；C9/C10 按路线取舍（网页/Blender、评审前/后）。每条出处见 §4。

## 2. 捕获与合成命令骨架

**网页路线 · 仓库 harness 基线**（`harness/render.mjs`，compare §3.1；Windows 需 `MG_CHROME` 指向 `chrome.exe`，默认是 macOS 路径）：

```bash
node harness/render.mjs <demo-dir>                              # 全片 → out/video.mp4
node harness/render.mjs <demo-dir> --stills 0,1.5,3,5,7.5,9.5  # 6 关键帧 → out/stills/
node harness/render.mjs <demo-dir> --mb 4 --crf 14              # 运动模糊 = 时间超采样（成本 ×MB）
node harness/render.mjs <demo-dir> --scale 0.5                  # 低清快速预览
```

**网页路线 · 自研骨架**（workflow §1–2）：

```bash
node render.js --keys   # 只渲 KEY = [0,45,90,150,225,285]
node render.js          # 全片 300 帧 → frames/f%04d.png（连续编号）

# 合成：-framerate 30 必须显式写死（image2 缺省 25，300 帧会被拉成 12 s）
ffmpeg -framerate 30 -i frames/f%04d.png -i audio/score.wav \
       -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 192k -shortest final.mp4
# 像素风小画布（内部 320×180 → 整数倍放大）
ffmpeg -framerate 30 -i frames/f%04d.png -vf "scale=1920:1080:flags=neighbor" \
       -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4
```

> Windows 提示：PowerShell 里 `%` 有别名歧义——用 bash/cmd 跑，或给 `f%04d.png` 加引号（workflow §2）。

**Blender 路线**（compare §3.2，6 步）：`make_letters.py`（字形→网格 .ply）→ `sim.py`（物理→`work/anim.npz` + `out/events.json`）→ `scene.py`（`blender -b --factory-startup -P`）→ `render.py`（`--range 0:239`）→ `audio.py` → 回网页合成（文字/颗粒）后走同一条逐帧管线。

## 3. 自查命令清单（跑过才算完成）

> 标注：[实测] = 2026-10-15 本机跑过（工具存在性或命令结构）；[UNVERIFIED] = 从 workflow §5 转录、本机未跑。

```bash
# ① 确定性回归（P0）：同帧两跑期望 0 差异（pixelmatch 退出码 0=一致；需 npm 装 [UNVERIFIED]）；全片 psnr/ssim 期望满分
pixelmatch frames/f0000.png frames_rerun/f0000.png checks/diff_f0000.png 0.1
ffmpeg -i out.mp4 -i out_rerun.mp4 -lavfi "psnr=stats_file=checks/psnr.log;ssim=stats_file=checks/ssim.log" -f null -   # [实测] 过滤器存在

# ② 帧数验收：期望 300
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 out.mp4   # [实测]

# ③ 卡帧/静止段（no significant change）
ffmpeg -i out.mp4 -vf "freezedetect=n=-60dB:d=0.5" -map 0:v -f null -   # [实测] 过滤器存在

# ④ 色数/色彩漂移（%k 需 ImageMagick，本机未装 → signalstats 平替）
ffmpeg -i out.mp4 -vf "signalstats,metadata=print" -f null -   # [实测] 过滤器存在

# ⑤ 响度/真峰（spec：≈−14 LUFS ±1、≤−1 dBTP；读 input_i / input_tp）
ffmpeg -i final.mp4 -af loudnorm=print_format=json -f null -   # [实测] 本机 exit 0 并输出 JSON

# ⑥ 审片 contact sheet（300 帧 → 10×5）
ffmpeg -i out.mp4 -vf "fps=6,scale=384:-1,tile=10x5:padding=4:color=#101010" -frames:v 1 checks/sheet.png   # [实测] tile 存在
```

- ①b 乱序重渲（必做，属 P0）：同序重渲会漏「跨帧状态泄漏」（如 `fillStyle` 被赋非法值 → 浏览器静默忽略 → 沿用上一帧状态）；乱序抽帧重渲（如 `--rerun 299,150,0`）逐帧比 SHA256 期望全一致——B-07 实测 f0150 曾差 158 源像素，修复后 3/3 帧一致（2026-10-15）。
- ⑦ 运动曲线（hold 拍/切拍/过冲）：`python checks/motion.py frames/`（脚本见 workflow §5 ⑤b）[UNVERIFIED]。
- 顺序 = 先机械后人工：确定性回归 → 帧 diff → contact sheet → 色彩 → 运动。

## 4. 条款 ↔ 来源对照

| 条款 | 出处（raw 直读 2026-10-15） |
|---|---|
| C1 READY/DEMO/renderAt | `harness/render.mjs` 文件头第 4–7 行原文（§5 原样粘贴） |
| C2 纯函数 of t | `prompts/01-flat-vector.md` Rules 第 1 条："every frame is a pure function of time t" |
| C3 禁壁钟 | 同上 "no real-time clocks"；workflow §1（rAF 帧率随机器变，MDN 依据） |
| C4 播种随机 | 同上 "Seeded randomness only; physics and particles precomputed or closed-form"；workflow §1 mulberry32 骨架 |
| C5 CSS/WAAPI seek | `harness/render.mjs` `seek()` 实现：`a.pause(); a.currentTime = t * 1000` |
| C6 EV 单表双读 | `prompts/01-flat-vector.md` How-to-work 第 1 条 "Keep one cue sheet … both the picture and the sound"；workflow §3（1470 采样/帧） |
| C7 输出规格 | `template.md`「Output (fixed)」+ 15 条 prompts 头（compare §3.3） |
| C8 素材/文案 | `prompts/01-flat-vector.md` Rules 第 2–3 条原文 |
| C9 Blender 等价 | compare §3.2（`demos/04-3d-render/README.md` 6 步原文） |
| C10 关键帧先行 | 15 卡任务头原文 + workflow §4；harness `--stills` CLI |

## 5. 来源验证（read 原样输出，2026-10-15）

URL：`https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/harness/render.mjs:1-8`

```
URL: https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/harness/render.mjs
Content-Type: text/plain
Method: text

---

#!/usr/bin/env node
// Deterministic HTML → video renderer.
//
// A demo page (demos/<slug>/index.html) must define, before setting window.__ready = true:
//   window.DEMO = { width, height, fps, duration }            // optional overrides of CLI defaults
//   window.renderAt = async (t) => { ... }                     // draw the frame for time t (seconds)
// Anything not driven by renderAt (CSS animations, WAAPI) is also seeked to t automatically.
```

（以上为 read 工具输出原样节选；工具自带的 URL/Content-Type/Method 头一并保留。）

---

## 附录 · 自审（LOOP 协议四段，覆盖 B-11 三件产物）

**A · 早产出**：三件按序落盘——`templates/style_card.md`（v0.2 修订）→ 本契约 → `knowledge/cross/review_rubric.md`；每件先落骨架（版本/来源行 + 条款或表格），后补命令与验证。

**B · 反驳**（4 条，命令与输出见 C）：
1. 「workflow §4 的 contact sheet 命令（`-i key/k%04d.png`）可直接用」→ 本机造 3 张非连续关键帧（k0000/k0045/k0090）实跑 → `nb_read_frames=1`，拼出 1 格图 → **OVERTURNED**（style_card v0.2「6 关键帧落地」节已写替代法）。
2. 「`-pattern_type glob` 可作为替代输入」→ 实跑 → "globbing is not supported by this libavformat build" → **OVERTURNED**（已写入禁用注记）。
3. 「契约条款与仓库原文一致」→ `render.mjs:1-8` 与 `prompts/01-flat-vector.md` Rules 段 raw 直读逐字比对 → 吻合 → **CONFIRMED**。
4. 「自查清单的工具在本机可用」→ `ffmpeg -filters` + loudnorm 实跑 → 六个过滤器全在、loudnorm exit 0 → **CONFIRMED**（pixelmatch/odiff/motion.py 未装未跑，已在 §3 标 [UNVERIFIED]）。

**C · 机械验证**（原样输出，2026-10-15）：

```
--- seq pattern frames read:
$ ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 k%04d.png
exit 0
1
--- glob pattern frames read:
$ ffprobe -v error -pattern_type glob -count_frames ... -i k*.png
exit 1
ERR: [image2 @ 0000016b409024c0] Pattern type 'glob' was selected but globbing is not supported by this libavformat build
k*.png: Function not implemented
--- sequential naming + tile:
$ ffmpeg -v error -framerate 1 -i k%d.png -vf tile=3x2:padding=8:color=#101010 -frames:v 1 sheet_ok.png -y
exit 0
$ ffprobe ... sheet_ok.png → 208,80
--- concat fallback:
$ ffmpeg -v error -f concat -safe 0 -i list.txt -vf tile=3x2:... -frames:v 1 sheet_concat.png -y
exit 0 → 208,80
--- filters:
freezedetect -> True  signalstats -> True  tile -> True  psnr -> True  ssim -> True  loudnorm -> True
--- loudnorm:
{ "input_i" : "-21.75", "input_tp" : "-18.06", ... }  (exit 0)
```
（以上为本次会话 eval 输出的原样节选。）

**D · 小结**（≤14 行）
1. 已确立：三件产物落盘（style_card v0.2 / 确定性契约 C1–C10 / 7 维评审表）；契约条款均有 raw 出处；两处 raw URL 原样验证。
2. 已确立：workflow §4 拼图命令对非连续关键帧失效（实测只读 1 帧）；glob 不可用；连续编号或 concat 可用。
3. 已确立：本机 ffmpeg 具备自查所需全部过滤器；loudnorm 可用。
4. 未知/未跑：pixelmatch、odiff、motion.py（需 npm/自写脚本）；仓库 harness 端到端（B-07 负责）。
5. 下一步：B-07 用本契约跑一支 10 s 片回填实测；B-02 可据 B-1 条修正 workflow §4 命令。
