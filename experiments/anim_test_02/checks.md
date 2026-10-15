# checks.md — B-17 端到端实验 #2《一笔画 · 山野骑行》

> 归属：GOALS B-17（AnimTest02，wave5）｜实验日期 2026-10-15｜目录 `experiments/anim_test_02/`
> 来源卡：`knowledge/domains/motion-graphics/origin/提示词全文.md` 第 8 条「一笔画 ONE LINE」（画风段 + 内容段原文见 §5）
> 管线依据：`knowledge/agent-art/html/workflow.md` §1–§5 + `templates/determinism_contract.md`（C1–C10；#1 实测回填的「乱序重渲 P0」）
> 参考片：`ref/02-line-art.mp4`（`Vincentwei1021/mg-styles-15` videos/，MIT，2026-10-15 raw 直取；抽 3 帧 = `ref/ref_1/2/3.png`，另有 12 张研读帧在 `ref/study/`）
> 证据分级：本文件数字全部 = 本机实跑输出（原样粘贴）；推断处标 `[推测]`。

**结论一行：out.mp4 = 1920×1080 / 30fps / 300 帧 / 10.000s（h264 + 代码合成音轨），整片一根线（15 个抽样帧的墨迹全部连通为 1 个分量）、线宽 3.5px 恒定圆头（列切游程全 3px）、笔尖光点从 f0 走到 f266 熄灭、拐弯 4.8px/帧 vs 直线 50.8px/帧（10.6 倍）、徽章圆 f266 闭合后从太阳落点向外填色（面积单调增到 96.8%）、结尾「山野骑行」在 f284 后落定；乱序重渲 5/5 逐字节一致（P0 通过，且本次未出现 #1 的状态泄漏 bug）。**

## 1. 交付物清单

| 文件 | 大小 | 说明 |
|---|---|---|
| `out.mp4` | 631,734 B | 成片（h264 + aac，300 帧 / 10.000s；音轨 +2dB 静态增益后 −17.16 LUFS / −1.17 dBTP） |
| `video.mp4` | 384,363 B | 无音轨画面版（编码中间产物，便于回归比对） |
| `index.html` | 15,207 B / 365 行 | 渲染页：`window.seek(frame)` 纯函数；单折线 2153 顶点 + 成本模型 + sun 组变换 + 填色重描 |
| `cues.js` | 2,066 B / 34 行 | 单表双读（C6）：8 个叙事相位 + 10 个音效卡点（画面与音频同读此表） |
| `render.js` | 3,771 B / 89 行 | puppeteer-core 逐帧截图驱动（`--keys/--frames/--probe/--rerun`） |
| `audio.html` + `render_audio.js` | 8,206 + 1,840 B | OfflineAudioContext 离线合成 → `audio/score.wav`（无采样、无录音、无 Math.random） |
| `frames/f0000.png … f0299.png` | 300 张（14 MB） | 逐帧 PNG（1920×1080） |
| `key/k0000/k0050/k0100/k0150/k0200/k0250.png` + `key/keyframes_sheet.png` | 6+1 张 | 6 关键帧 + 3×2 拼图（带帧号标签；`lbl_*.png` 为标签中间件） |
| `checks/` | — | 自查脚本 + 全部原样输出（selfcheck/rerun/ref_compare/loudnorm/accept/render_meta）+ 探针帧（`probe/` 34 张）+ 对照帧 + 全片审片图（`review_sheet.png`，2fps×20 帧 5×4）+ 成片抽帧（`out_t4.5/7.5/9.6.png`） |
| `ref/` | 35 MB | 官方参考片 + 抽帧（ref_1/2/3 + study/12 帧） |
| `package.json` / `node_modules/` | — | 依赖只装在实验目录内（puppeteer-core，npm 缓存离线装 3s） |

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
size=631734
bit_rate=505387

$ ls key/*.png
key/k0000.png
key/k0050.png
key/k0100.png
key/k0150.png
key/k0200.png
key/k0250.png
key/keyframes_sheet.png
key/lbl_0000.png
key/lbl_0050.png
key/lbl_0100.png
key/lbl_0150.png
key/lbl_0200.png
key/lbl_0250.png

$ ffprobe -v error -show_entries format=duration,size -show_entries stream=codec_name,sample_rate,channels -of default=nw=1 audio/score.wav
codec_name=pcm_s16le
sample_rate=44100
channels=2
duration=10.000000
size=1764044
```

（完整文件：`checks/accept_out.txt`。）

## 3. 6 关键帧（0/50/100/150/200/250）

```
=== 9. 6 关键帧（key/） ===
key/k0000.png: (1920, 1080) 12400B sha256:4c3801fcb9872641
key/k0050.png: (1920, 1080) 24103B sha256:9ffaff1299adfe4c
key/k0100.png: (1920, 1080) 31470B sha256:8d9c50a142294efb
key/k0150.png: (1920, 1080) 51910B sha256:cf0fa31ad9009d0e
key/k0200.png: (1920, 1080) 69621B sha256:45d7831c7b8cb96b
key/k0250.png: (1920, 1080) 72805B sha256:127fcda1950d3d75
pairwise differing-pixel counts (of 129600, |diff|>10):
               0      50     100     150     200     250
       0       0     543     957    1791    2400    2514
      50     543       0     463    1299    1906    2020
     100     957     463       0     936    1752    1868
     150    1791    1299     936       0    2607    2715
     200    2400    1906    1752    2607       0    2911
     250    2514    2020    1868    2715    2911       0
keyframes_sheet.png: (1936, 728)
```

- 6 张全部 1920×1080；两两差异 463–2911 源像素（每张 129600）→ 6 张是 6 个不同画面。
- 分镜对应：`k0000` 落笔定场（只有笔尖光点）→ `k0050` 后轮 + 座管起笔 → `k0100` 车架成形（后轮/牙盘/座管/坐垫/车把，前轮未合）→ `k0150` 前轮变太阳（射线甩到一半）→ `k0200` 太阳升空 + 山脊左坡 + 牵线 → `k0250` 徽章大回环（太阳已落入山口）。
- 拼图命令（含 #1 的教训：非连续帧号不能用 `-i k%04d.png`，用 concat）：

```bash
ffmpeg -i k0000.png -vf "drawtext=fontfile='C\:/Windows/Fonts/consola.ttf':text='f0000':x=20:y=20:fontsize=64:fontcolor=black@0.8:box=1:boxcolor=white@0.65:boxborderw=10" -y lbl_0000.png   # ×6
{ printf "file 'lbl_0000.png'\nduration 1\n"; …; printf "file 'lbl_0250.png'\n"; } > list.txt
ffmpeg -f concat -safe 0 -i list.txt -vf "scale=640:360,tile=3x2:padding=8:color=#101010" -frames:v 1 keyframes_sheet.png
```

## 4. 一笔画机械验证（本片特有的四件套）

`python checks/selfcheck.py > checks/selfcheck_output.txt`（全文在 `checks/selfcheck_output.txt`；以下为原样节选）。

### 4.1 整片一根线：墨迹连通性（8 连通分量；期望 1）

```
=== 1. 一笔画连通性（墨色 mask → 8 连通分量；期望 1 个主体） ===
f0000 ink_px=      0 comps>50px=0  comps_all=0  max=0
f0030 ink_px=   1569 comps>50px=1  comps_all=1  max=1569
f0063 ink_px=   3448 comps>50px=1  comps_all=1  max=3448
f0100 ink_px=   5058 comps>50px=1  comps_all=1  max=5058
f0126 ink_px=   6391 comps>50px=1  comps_all=1  max=6391
f0150 ink_px=  10279 comps>50px=1  comps_all=1  max=10279
f0182 ink_px=  12577 comps>50px=1  comps_all=1  max=12577
f0200 ink_px=  14018 comps>50px=1  comps_all=1  max=14018
f0230 ink_px=  12277 comps>50px=1  comps_all=1  max=12277
f0250 ink_px=  15028 comps>50px=1  comps_all=1  max=15028
f0266 ink_px=  17160 comps>50px=1  comps_all=1  max=17160
f0275 ink_px=  14032 comps>50px=1  comps_all=1  max=14032
f0284 ink_px=  14140 comps>50px=1  comps_all=1  max=14140
f0290 ink_px=  14140 comps>50px=1  comps_all=1  max=14140
f0299 ink_px=  14140 comps>50px=1  comps_all=1  max=14140
```

- 15 个抽样帧（覆盖全部 8 个相位 + 填色中段 + 文案段）**全部 = 1 个连通分量** → 「整支片子只有一根线，从头到尾不断」在像素级成立。
- f0000 的 ink=0 = 落笔瞬间（只有笔尖光点，未落墨）。
- f0284 起文案阶段：文案区（深绿，非墨色）已在 mask 中排除；文案像素不参与连通性。
- 墨迹占全屏比例：f0266 峰值 17160/2073600 = **0.83%**（「画面大部分留白」的量化下限）。
- 该检查抓到过两个真问题（详见 §6 与 §12B）：① 填色中段重描层的裁剪边缘把墨线切成 2 段；② 笔尖光点画在墨线之上，amber 覆盖墨迹把闭合点切成 2 段。均已修复（重描层裁剪 +3px 重叠；光点改画在墨线之下）。

### 4.2 线宽恒定（腐蚀 + 横切）

```
=== 2. 线宽恒定（5x5 腐蚀两次后残留 = 交叉/结点；直段横切游程） ===
f0063 ink=   3414 after_erode1=  1238 after_erode2=   26
f0126 ink=   6307 after_erode1=  2202 after_erode2=   32
f0200 ink=  13988 after_erode1=  5600 after_erode2=  314
f0250 ink=  14994 after_erode1=  5940 after_erode2=  197
f0126 row y=755 ink runs = [3, 8]
f0126 row y=760 ink runs = [3, 7]
f0126 row y=765 ink runs = [3, 8, 24]
f0126 col x=650 ink runs = [2, 3, 3, 3]
f0126 col x=660 ink runs = [3, 3, 3, 3]
f0299 row y=500 ink runs (x,len) = [(779, 3), (973, 5), (1010, 4), (1025, 9), (1041, 3), (1059, 5), (1066, 3), (1080, 4), (1096, 4), (1103, 3), (1109, 5), (1156, 5), (1318, 3)]
```

- 列切（垂直穿过近水平线）：`x=650/660` 全部 3px 游程 → 线宽 ≈ 3.5px 恒定（含抗锯齿边缘的 mask 读数 3px）。
- 行切：座管 3px；上管 7–8px = 3.5px 线在 23° 斜角下的横切 `3.5/sin23° ≈ 9px`，几何自洽。
- 5×5 腐蚀两次后残留 26–314px（占墨迹 0.2–2.2%）= 只剩交叉点/结点（射线尖端、山脊线交会处）→ 全片无局部加粗段。
- f0299 过徽章圆心横切：左右描边各 3px（`(779,3)` / `(1318,3)`），中段 11 个游程 = 太阳射线 + 山口线 + 太阳盘边缘 → 填色后描边宽度不变。
- 代码级：`ctx.lineWidth = 3.5`（常量）、`lineCap/lineJoin = 'round'`（`window.__meta.lineWidth=3.5, lineCap/lineJoin='round'`）。

### 4.3 笔尖光点（眼睛跟着它走）

```
=== 3. 笔尖光点（近 #ff9d1f；f0-266 在，填色后熄灭） ===
f0000 dot_px= 120 centroid=(444.5, 899.5)
f0060 dot_px= 122 centroid=(486.3, 743.5)
f0126 dot_px= 120 centroid=(639.5, 984.5)
f0150 dot_px= 120 centroid=(760.7, 944.5)
f0200 dot_px= 121 centroid=(1039.1, 562.5)
f0250 dot_px= 123 centroid=(905.5, 271.1)
f0266 dot_px= 121 centroid=(1270.6, 654.5)
f0270 dot_px=  10 centroid=(1270.4, 654.1)
f0280 dot_px=   0
f0299 dot_px=   0
```

- 光点 = 实心 r6.5px（#ff9d1f）+ 半径 34px 软光晕；每帧 ~120px 恒亮。
- 轨迹抽样与路线逐一对应：f0 = 起点 (445,900)；f60 = 座管中段 (486,744)；f126 = 前轮底 (640,985)；f150 = 射线尖端；f200 = 山脊山口；f250 = 徽章圆左上（绕行 56%）；f266 = 闭合点 (1271,655)。
- f266–f278 淡出（f270 只剩 10px），填色开始时熄灭 → 「最后闭合」与「笔离开」同步。

### 4.4 闭合填色（从一点向外）

```
=== 4. 闭合填色（徽章圆内 天空/山体/太阳 色像素数） ===
f0264 fill_px=    576
f0266 fill_px=    576
f0268 fill_px=    904
f0270 fill_px=   5843
f0272 fill_px=  22238
f0274 fill_px=  59694
f0276 fill_px= 119350
f0278 fill_px= 176003
f0280 fill_px= 209367
f0282 fill_px= 221617
f0284 fill_px= 221621
f0299 fill_px= 221621
monotonic_non_decreasing (tol 100px) = True
badge_area = 228977
```

- 徽章圆 f266 闭合（`dot centroid = (1270.6,654.5)` = 闭合点），填色立即从**太阳落点 (1055,560)** 向外扩散（`wipeR: 0 → 340px`，smoothstep）。
- 面积 576 → 221,621 = 徽章圆面积 228,977 的 **96.8%**（余量 = 墨线本身 + 抗锯齿边缘），单调增（容差 100px，实测最大回落 0）。
- 基线 576px（f264/266）= 笔尖光晕内圈像素恰落在天空色容差内（非填色），已在读数口径中说明。

### 4.5 结尾文案

```
=== 5. 结尾文案「山野骑行」（深绿 #2f5d45，文案区内） ===
f0280 text_px=     0
f0284 text_px=     0
f0288 text_px=     0
f0292 text_px= 13227 bbox=(833,842)-(1245,923)
f0299 text_px= 13243 bbox=(833,842)-(1245,923)
```

- f284 起淡入（9 帧 smoothstep），f292 已达全色 → f299 保持。f284/288 读数为 0 是因为淡入中的混色像素未达「纯文案色」容差（口径说明，非未出现）。
- 文案 bbox = (833,842)–(1245,923)：宽 412px / 高 81px，居中于 x=1050（徽章正下方）。
- 文案为浏览器字体（`700 86px "Microsoft YaHei"` + `letterSpacing 26px`），非点阵自绘 —— 与 #1 像素风「必须自绘避抗锯齿」的约束相反（本片无颜色数约束）。跨机器字体差异已在 §11 标注。

### 4.6 帧间统计 + 色数（记录）

```
=== 6. 帧间统计（全 300 帧） ===
identical-to-previous frames = 7/299 (2%)
mean abs diff per frame: mean=0.209 max=1.484 frames with diff>0.5 = 44

=== 7. 色数（抽样 50 帧并集；本片无“限色”约束，仅记录） ===
sampled frames = 50, union colors = 2136, per-frame min=102 max=726
```

- 7 个与前帧逐字节相同的帧 = 文案保持段（f293–299）+ 填色走满后的 1 帧；其余 292 帧都有运动（一笔画是连续推进的，没有 #1 那种 10Hz 离散 hold）。

## 5. 技术规格对照（卡片 08 画风段逐条）

| 画风段原文 | 实现 | 证据 |
|---|---|---|
| 整支片子只有一根线，每个形状的尾巴接着下一个形状的开头，从头到尾不断 | 单折线 2153 顶点：后轮→牙盘→座管→坐垫→上管→车把→头管→前叉→前轮→射线→山脊→徽章圆，逐段相连；唯一两段长直段（前叉 88.6px、山脊连接线 397px）为有意设计（连接线起点属 sun 组，随太阳伸缩） | §4.1 全帧 1 分量；`__selftest.longSegs`（2153 顶点中仅此 2 段 >12px） |
| 线宽不变，圆头 | `lineWidth=3.5` 常量、`lineCap/lineJoin='round'` | §4.2 列切 3px 游程 ×4 + 腐蚀残留 0.2–2.2% |
| 笔尖带一个小光点，眼睛跟着它走 | 实心点 r6.5 + 34px 光晕，位置 = reveal 末端（含 sun 组变换） | §4.3 每帧 ~120px + 7 个采样轨迹 |
| 拐弯慢、直线快，像手腕在转 | 成本模型：`cost = Σ len·(1+2.8·D)`，D = 转角密度（θ>14° 才计，沿路径 σ=35px 高斯平滑）→ 拐弯前后 ±70px 减速 | `__speed`：直线 50.8px/帧 vs 拐弯 4.8px/帧（**10.6×**，最慢点在车把拐角 (595,774)） |
| 最后一个形状闭合时，从一点向外填满颜色 | 徽章圆 f266 闭合；填色 = 从太阳落点 (1055,560) 向外 340px 的径向擦除（clip 半径生长），天空/山体/太阳三层色 + 墨线重描浮回 | §4.4 面积 576→221,621 单调 |
| 画面大部分留白 | 纸色 #f8f5ee 全屏；墨迹峰值占比 0.83% | §4.1 f0266 = 17160/2073600 |
| 别做成：断了重画 | 无第二笔：全片唯一 stroke 调用（`inkPath`），填色后「重描」是同一路径的 z 序回浮，不是新线 | §4.1 1 分量 + 代码结构（`render()` 只有一处 `ctx.stroke()` 画线） |
| 别做成：线宽变化 | 同 §4.2 | §4.2 |
| 别做成：几根线同时画 | reveal 只有一个笔尖位置（单 `posAtCost`），任何时刻只有一条推进中的线 | §4.3 光点唯一 |

内容段对照（【】内为卡片槽位原文）：一根线画出一辆自行车（f0–126）→ 前轮变成太阳（f126–158 甩射线 + f158–182 升起）→ 太阳落进山脊（f182–216 画山脊 + f216–230 落入山口）→ 山脊收拢成一枚徽章（f230–266 大回环闭合）→ 填色后出现「山野骑行」（f266–284 填色 + f284 起文案）。✅ 五拍全在，顺序一致。

`window.__meta`（渲染页自述，`checks/render_meta.json` 原样）：

```json
"meta": { "fps":30, "frames":300, "width":1920, "height":1080,
  "routeVerts":2153, "routePx":11060, "lineWidth":3.5, "lineCap":"round", "lineJoin":"round",
  "phases": [{"name":"bike","f0":0,"f1":126,"draw":true},{"name":"rays","f0":126,"f1":158,"draw":true},
             {"name":"rise","f0":158,"f1":182,"draw":false},{"name":"ridge","f0":182,"f1":216,"draw":true},
             {"name":"fall","f0":216,"f1":230,"draw":false},{"name":"badge","f0":230,"f1":266,"draw":true},
             {"name":"fill","f0":266,"f1":284,"draw":false},{"name":"text","f0":284,"f1":300,"draw":false}],
  "cost": {"bike":5367, "rays":7173, "ridge":9284, "total":11060} },
"selftest": { "ok":true, "maxGap":396.989, "longSegs":[[602,820,640,900,88.6],[640,990,900,690,397]], "sunVerts":781, "verts":2153 },
"speed": { "straightPxPerFrame":50.8, "cornerPxPerFrame":4.8, "ratio":10.6, "cornerAt":[595,774], "cornerDensity":2.81 }
```

## 6. 确定性回归（P0：乱序重渲）

```bash
$ node render.js --rerun 299,266,150,63,0   # 乱序重渲（P0）
{"mode": "rerun", "frames": 5, "dir": "checks/rerun", "errors": [], "seconds": 0.4}

$ sha256 compare (frames/ vs checks/rerun/)
f0299: 69c38ef50e396dca / 69c38ef50e396dca  IDENTICAL
f0266: f0d1a63ad7ffcd73 / f0d1a63ad7ffcd73  IDENTICAL
f0150: cf0fa31ad9009d0e / cf0fa31ad9009d0e  IDENTICAL
f0063: 036ff7f1a98799f2 / 036ff7f1a98799f2  IDENTICAL
f0000: 4c3801fcb9872641 / 4c3801fcb9872641  IDENTICAL
```

- 逆序（299→0）重渲 5 帧，含填色中段（f266）与三个相位边界，**5/5 逐字节一致** → `seek(f)` 不依赖上次调用的画布状态。
- 本次**没有**复现 #1 的 `fillStyle` 状态泄漏类 bug：页面每帧从纸面 `fillRect` 全量重画、无增量状态、无非法样式赋值（全片 `errors: []`）。
- 但本次抓到两个**同类性质**的新问题（都是靠探针帧 + §4 检查发现，见 §12B）：填色裁剪接缝、光点覆盖墨迹 —— 教训相同：**「连续性」类断言必须用全帧像素级检查（连通性），肉眼看不出 1px 接缝**。

## 7. 与官方参考片对照（同系统、不同内容）

```
=== 规格 ===
官方 02-line-art.mp4 : 1920,1080,30/1,300
本项目 out.mp4 : 1920,1080,30/1,300

=== 背景色与线条极性（首帧 (100,100) 取样 + 全帧均值） ===
ref: bg RGB at (100,100) = (5, 11, 19)
ours: bg RGB at (100,100) = (247, 243, 235)
ref  frame mean RGB = (11, 18, 31)
ours frame mean RGB = (245, 241, 233)
ref  最亮像素 (932,507) RGB=(242, 237, 211)；横切灰度=[np.int64(89), np.int64(84), np.int64(83), np.int64(90), np.int64(97), np.int64(100), np.int64(140), np.int64(180), np.int64(230), np.int64(201), np.int64(184), np.int64(158), np.int64(131), np.int64(103), np.int64(92), np.int64(86), np.int64(80)]
ref  该处线宽：核心(>200)=2px，FWHM(>125)=7px（含辉光）
ours 线宽（t=5.0 x=660 列扫，暗游程）: [3, 3, 15, 3, 3]

=== 运动统计（480x270 灰度，全 300 帧） ===
--- ref 02-line-art.mp4 ---
frames = 300
mean abs diff per frame: mean=1.167 max=5.694 frames with diff>0.5 = 240
identical-to-previous frames = 0/299
--- ours out.mp4 ---
frames = 300
mean abs diff per frame: mean=0.213 max=1.516 frames with diff>0.5 = 44
identical-to-previous frames = 0/299
```

（全文：`checks/ref_compare_output.txt`；对照帧：`ref/ref_1.png`(t=0) / `ref_2.png`(t=5.0) / `ref_3.png`(t=9.5)。）

**逐条差异（口径先行，避免误读）：**

1. **画面极性相反（最大差异）**：官方是暗底（近黑藏青 (5,11,19)）+ 亮线（暖白核心 (242,237,211)）；本项目按卡片「画面大部分留白」做**纸底（247,243,235）+ 墨线（51,47,42）**。两者都是「留白/负空间」的一种读法，本项目取了字面（纸面）读法 —— 这是**有意差异**，不是偏离：卡片画风段没有规定底色，但「留白」二字在中文语境默认浅底。
2. **线的光学处理**：官方线带辉光（核心 2px + bloom，FWHM 7px）；本项目线宽 3.5px、无辉光（硬边）。官方更像「发光墨迹」，本项目更像「针管笔」。
3. **笔尖**：官方 = 亮色光点 + 拖尾辉光；本项目 = amber 实心点 + 软光晕（浅底上必须换配色，否则看不见）。
4. **内容不同**：官方成片内容是**藤蔓→房屋→城市天际线→山丘→金太阳盘（带拱形镂空）+ ATELIER LINEA / 始于一线**；卡片 08 的内容槽（自行车→太阳→山脊→徽章→山野骑行）与教程片预览窗「一笔自行车→徽章」一致，但与仓库里这支成片**不是同一段内容** `[史料]`（教程片预览 vs 仓库 videos/02-line-art.mp4，本机抽帧核对）。本项目按卡片内容槽实现。
5. **填色手法**：官方 = 金色圆盘（内含拱形**镂空**，与前面房屋的门拱呼应）+ 文字淡入；本项目 = 从太阳落点向外的**径向擦除**（天空/山体/太阳三层色 + 墨线回浮）。官方的镂空更省事也更有呼应；本项目的径向擦除更贴卡片「从一点向外填满」的字面。
6. **节奏**：官方每帧平均变化 1.167（灰度 480×270 口径），本项目 0.213 —— 官方推进更快（且 h264 噪声抬高基线）；本项目全片 2% 的帧与前帧完全相同（文案保持段），官方 0%（编码噪声）。
7. **结尾文字**：官方 = 字距很开的拉丁字标 + 中文副标（金色）；本项目 = 深绿粗体 CJK 标题「山野骑行」，无拉丁字标。

## 8. 音轨（卡片任务头：配乐音效也用代码合成、跟画面卡点）

- 合成方式：`audio.html` 里 `OfflineAudioContext(2, 44100×10, 44100)` 一次性离线渲染；噪声源用播种 mulberry32（种子 20261015）；无采样、无录音、无 `Math.random`。
- 卡点机制（C6 单表双读）：`cues.js` 同时被画面（phases）与音频（sfx）读取；事件时间 = 帧号/30，44.1kHz 下每帧恰好 1470 采样。
- 事件表（帧号 → 声音）：f0 落笔 / f126 甩射线（五声上行+噪声）/ f158 太阳升起（220→880Hz 滑音）/ f182 山脊起笔（低音 swell）/ f216 下落（880→190Hz）/ **f230 落入山口（60→38Hz 低频冲击）+ 徽章大回环 whoosh** / **f266 闭合钟声 + 填色上行八音** / f284 收尾和弦 + 高音钟。
- 配乐：120 BPM（15 帧/拍），5 小节×2s（A–F#m–D–E–A），三角波琶音 + 正弦垫 + 沙锤；每帧 1470 采样与画面同源。

```
=== 8. 音轨（audio/score.wav 逐秒 RMS/峰值） ===
sr=44100 ch=2 frames=441000 dur=10.000s
  t=0-1s rms=0.035 peak=0.271
  t=1-2s rms=0.019 peak=0.148
  t=2-3s rms=0.034 peak=0.175
  t=3-4s rms=0.019 peak=0.142
  t=4-5s rms=0.047 peak=0.268
  t=5-6s rms=0.035 peak=0.176
  t=6-7s rms=0.067 peak=0.263
  t=7-8s rms=0.104 peak=0.700
  t=8-9s rms=0.086 peak=0.599
  t=9-10s rms=0.110 peak=0.513
```

- 高潮（7–10s：落入山口/闭合/填色/文案）RMS 0.086–0.110 = 全片最高段 → 「跟画面卡点」在包络上成立。
- 响度（成片）：`input_i=-17.16 LUFS / input_tp=-1.17 dBTP / input_lra=11.80`（`checks/loudnorm_out.txt`）。
- 母带过程：WAV 峰值归一化到 0.70 → 成片 mux 时 `-af volume=2dB`（静态 +2dB，峰值 −1.17 dBTP ≤ −1 ✅）。合同 C7 的 −14 LUFS 目标**未达标**（差 3.2dB）；一次 `volume=4.2dB + alimiter` 尝试达到 −14.5 LUFS 但 aac 编码后真峰 +0.1 dBTP（超 0dB），为守住 ≤−1 dBTP 而放弃 —— 见 §11 缺口。

## 9. 耗时与可复现命令

```bash
node render.js --frames          # 300 帧 -> frames/ : 16.5–17.6s（约 17–18 fps 捕获，含浏览器启动）
node render.js --keys            # 6 关键帧 -> key/ : 0.6s
node render.js --rerun 299,266,150,63,0   # 乱序重渲 5 帧 -> checks/rerun/ : 0.4s
node render_audio.js             # OfflineAudioContext -> audio/score.wav : 0.4s（峰值 0.4382 → 增益 1.5975）
ffmpeg -framerate 30 -i frames/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 15 -preset medium -movflags +faststart video.mp4   # 1.5s
ffmpeg -i video.mp4 -i audio/score.wav -af volume=2dB -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4      # 0.3s
python checks/selfcheck.py > checks/selfcheck_output.txt       # 12–29s
python checks/ref_compare.py > checks/ref_compare_output.txt   # 2.3s
```

- 端到端（画面渲染 → 成片）≈ **19s**（不含脚本编写）——与 #1 的 21s 同量级。
- 环境：Windows / Node v24.19.0 / puppeteer-core 24.x + `chrome-headless-shell 153.0.8010.36`（`C:/Users/dwgx1/.cache/puppeteer/…`）/ ffmpeg n9.0.1 / Python 3.14.7 + numpy 2.5.3 + Pillow 12.3.0 + **scipy 1.18.1（新增依赖：连通性 label / 腐蚀）**。
- 浏览器启动参数与 #1 相同：`--force-color-profile=srgb --hide-scrollbars --disable-gpu --disable-lcd-text --force-device-scale-factor=1`（软件光栅，确定性检查通过）。

## 10. 与 #1 的流程对比（可迁移性主结论）

### 10.1 顺：直接复用、零改动的部分

| #1 的资产 | #2 的用法 | 结果 |
|---|---|---|
| puppeteer `seek(f)→screenshot` 驱动骨架（模式 CLI + 同一 chrome-headless-shell 路径 + 同一组启动参数） | 重写为 `render.js`（89 行），结构照搬 | 首次运行即出 16 张探针帧（1.2–1.6s），零调试 |
| ffmpeg 合成命令（`-framerate 30` 写死、libx264/crf/yuv420p、aac mux、`+faststart`） | 原样使用 | 一次成功，无参数坑 |
| 「非连续帧号拼图用 concat」的教训（#1 实测踩过 `-i k%04d.png` 只读 1 帧） | 直接写 concat 方案 | 一次成功，没再踩 |
| OfflineAudioContext + 手写 WAV 编码 + 峰值归一化 | 同构重写（音色/事件全新） | 一次成功（0.4s 出 10.000s WAV） |
| selfcheck 的 numpy/PIL 骨架（帧加载、逐秒 RMS、帧间统计） | 扩展 | 直接可用 |

### 10.2 卡：本片特有的新问题（按发现顺序）

| # | 症状 | 根因 | 抓它的手段 | 修复 |
|---|---|---|---|---|
| 1 | 拐弯几乎不减速（与卡片「拐弯慢」不符） | 成本模型 v1 把转角惩罚记在「角点前那一个 3px 子段」上，慢只慢 3px | `__speed` 速度剖面读数 | 改成转角密度沿路径 σ=35px 高斯平滑（±70px 减速带）→ 直线 50.8 vs 拐弯 4.8 px/帧 |
| 2 | f200 出现两条从太阳拖到地面的「幽灵长线」 | 前叉/山脊连接线被 `seg()` 细分成 3px 点，端点分属不同变换组 → 零长段在太阳升起时被拉成 ~400px | 探针帧肉眼比对 | 两条连接线改为**单段**（不细分），端点跨组伸缩成为有意设计（「牵线」） |
| 3 | 射线段成本暴涨到全程 69%（笔在射线上会一闪而过） | 锯齿尖端的转角惩罚（~150°）在成本模型里被全额计入 | `__meta.cost` 分相位读数 | 射线顶点加低权重 w=0.08（装饰性甩笔不按「手腕拐弯」计费） |
| 4 | 填色中段墨迹连通性断成 2 段（f275） | 重描层 clip 半径 = 填色层半径 → 裁剪边缘 1px 抗锯齿接缝 | §4.1 连通性检查 | 重描层 clip 改 R+3px，与底墨重叠 |
| 5 | 闭合点墨迹断开（f266 起 ~14px 缺口） | 笔尖光点（amber 实心 + 光晕）画在墨线**之上**，把闭合处墨迹覆盖出容差 | §4.1 连通性检查 | 光点改画在墨线之下（线帽压住点心，光晕在纸面） |
| 6 | 文案在 f275 就提前出现 | `drawText` 的 `u=(f-284)/9` 为负 → smoothstep(-1)=5 → alpha 爆炸 | 探针帧肉眼（检查没抓到） | `Math.max(0,…)` 夹紧 |

- 模式：#1 的坑是**状态泄漏**（渲染副作用跨帧残留），#2 的坑是**几何/层序**（变换组边界、clip 接缝、z 序）——同一类「肉眼看不见、必须机械检查」的问题，检查清单要各加一条（#1：乱序重渲；#2：全帧连通性）。
- 本次**所有**新问题都发生在「#1 没做过的机制」上：单折线成本模型、跨组变换、填色重描、光点层序 —— 即**管线骨架可迁移、风格机制必须重写并重新配检查**。

### 10.3 耗时对比（同机、同管线）

| 项 | #1（像素风） | #2（一笔画） |
|---|---|---|
| 300 帧捕获 | 18.3s（16.4 fps） | 16.5–17.6s（17–18 fps） |
| 端到端（渲染→成片） | ≈21s | ≈19s |
| 音轨渲染 | 0.5s | 0.4s |
| 关键帧 | 0.7s | 0.6s |
| 自查脚本 | 5 件套（色数/块结构/文案位图/确定性/对照） | 6 件套（连通性/线宽/光点/填色/文案/确定性/对照） |
| 代码量 | index.html 26.2KB（页面 320×180 内部画布 + 精灵表 + 点阵字） | index.html 15.2KB（单折线几何 + 成本模型 + 变换/填色）；+cues.js 2KB |
| 迭代轮次 | 探针帧 → 改画（鱼形/倒影/云/浮漂）→ 关键帧 | 探针帧 ×5 轮（几何/成本/层序修复）→ 关键帧 |
| 最大耗时项 | 逐帧截图（~60ms/帧） | 同（~55–60ms/帧）；**设计期**（单折线路由 + 5 拍叙事映射）比 #1 长 |

- 结论：**渲染管线成本与风格无关**（瓶颈都是 PNG 截图）；迁移成本集中在「把卡片文字翻译成几何与时间函数」的设计期，以及「为本风格发明机械检查」的验证期。

## 11. 缺口与未做（不假装）

- **自行车是极简一笔解**：无下管（牙盘→头管的斜管）、无链轮细节；后轮→牙盘→座管→上管→车把→前叉即整帧 `[归纳]`。放大看是「能认出是自行车」的程度，不是工程图。
- **官方参考片的辉光/纸纹/暗角未复刻**：本片硬边、无 bloom、无 grain（有意：卡片「留白」+ 确定性优先）。
- **响度未达合同 C7 的 −14 LUFS**（实测 −17.16）：一次 compressor/limiter 尝试在 aac 后真峰超 0dB 被放弃；正确做法是双遍 loudnorm + 真峰限幅器（后续）。
- **文案字体依赖系统字体**（Microsoft YaHei）：跨机器字体回退会改变文案位图 —— 同机确定性成立，跨机器不承诺（与 #1 的「跨机器不承诺」同一口径）。
- **官方参考片的真实内部实现未读**：只对照了成片（抽帧），没读 `demos/02-line-art/film.js`（47KB）——本项目代码全部自写，风格对照以成片为准。
- **`[UNVERIFIED]`**：out.mp4 在其它播放器上的 A/V 同步未逐台核（ffprobe 报两轨均 10.000s）；`[推测]`：官方的 bloom 是 shader 后期（未读其代码）。

## 12. 自审四段（LOOP 协议）

### A 早产出
落盘顺序：官方参考片 + 抽帧研读（`ref/study/` 12 帧）→ `cues.js`（相位表先定）→ `index.html` 骨架 + `render.js` → 16 张探针帧（首次 1.6s 出图）→ 看图修几何/成本/层序 ×5 轮（每轮 1.2–1.5s 重出探针）→ 6 关键帧 + 拼图（第一版）→ 全片 300 帧（第一版）→ 连通性检查抓出层序/接缝问题 → 重渲全片 + 关键帧（终版）→ 音轨 → out.mp4 → 自查脚本 → 本文件。中间产物全程落盘（`checks/probe/`、`ref/study/`、`checks/*_output.txt`）。

### B 反驳（逐条试推翻，命令与输出见 §4/§6/§7）

1. **「整片只有一根线」** → 试推翻：全帧连通性检查。第一次跑：f0150（光点覆盖射线尖端）与 f275（填色接缝）各出现 2 个分量 → **WEAKENED→已修**（光点层序 + 重描 clip +3px），修后 15/15 帧 = 1 分量 → **CONFIRMED**。
2. **「拐弯慢直线快」** → 试推翻：读 `__speed`。首版模型下拐弯只慢 3px（比例 ≈1.2）→ **OVERTURNED（模型缺陷）**；改成转角密度平滑后 10.6× → **CONFIRMED**。
3. **「线宽不变」** → 试推翻：若某处线宽变化，腐蚀两次的残留会成片出现。实测残留 26–314px（0.2–2.2%，全是交叉/结点）+ 列切全 3px → **CONFIRMED**。
4. **「seek 是纯函数（乱序重渲）」** → 试推翻：逆序重渲 5 帧（含填色中段/相位边界）→ 5/5 SHA256 一致 → **CONFIRMED**（#1 的状态泄漏 bug 本次未复现）。
5. **「填色从一点向外」** → 试推翻：填色面积单调性 + 擦除圆心。若从边缘或全屏淡入，面积曲线会跳变/基线非零 → 实测 576→221,621 单调（容差 100px 内无回落），圆心 = 太阳落点 → **CONFIRMED**。
6. **「与官方同规格」** → 试推翻：ffprobe 双方 → 都是 1920×1080/30/300 → **CONFIRMED**。

### C 机械验证（粘原样输出）

- 帧数/时长/规格：§2（`300` / `duration=10.000000` / `r_frame_rate=30/1`）。
- 一笔画四件套（连通性/线宽/光点/填色）：§4（`checks/selfcheck_output.txt` 全文）。
- 确定性：§6（`checks/rerun_check.txt`）。
- 官方对照：§7（`checks/ref_compare_output.txt`）。
- 音轨/响度：§8（`checks/loudnorm_out.txt`）。
- 浏览器控制台错误：每次 `render.js` 运行的 JSON 里 `"errors":[]`、`__selftest.ok=true`。

### D 小结（≤14 行）

- 已确立：一笔画的「一根线」可以做成**像素级可验收**的硬指标（全帧连通性 = 1 分量），「拐弯慢直线快」可以做成**速度剖面可读数**（10.6×），「从一点向外填色」可以做成**面积单调曲线**。
- 已确立：单折线 + 成本模型（转角密度 σ=35px 平滑）+ 变换组（sun 组平移/缩放）+ 填色重描（clip 生长 + 墨线回浮）是「一笔画」的最小可迁移机制组合；跨组连接线必须用**单段**（细分会变幽灵线）。
- 已确立：与 #1 相比，管线骨架（截图/合成/音轨）零改动复用；全部新问题都出在风格机制上（成本模型、跨组变换、层序、clip 接缝）——**可迁移的是管线，必须重写的是风格 + 检查**。
- 被推翻（本轮）：拐弯减速模型 v1（只慢 3px）；「光点在墨线上」的直觉画法（破坏连通性）；「重描 clip 与填色 clip 同半径」的直觉（1px 接缝）。
- 被削弱：与官方的可比性只在「风格语法」层（极性、辉光、内容、填色手法全不同，逐条列在 §7）。
- 未知：跨机器可复现性（字体/GPU）；官方实现的真实技法（未读其源码）。
- 下一步（给 B-08 迁移指南 / B-13 手册）：把「全帧连通性检查」「跨组连接线单段」「光点画在墨线之下」「重描 clip 外扩」四条写成模板级注意事项；并补双遍 loudnorm 母带。
