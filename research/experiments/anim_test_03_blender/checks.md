# checks.md — B-19 端到端验证 #3（Blender 线）《3D 质感 · PLAY》

> 归属：GOALS B-19（AnimTest03Blender，wave6）｜实验日期 2026-10-15｜目录 `research/experiments/anim_test_03_blender/`
> 来源卡：`research/origin_cards/提示词全文.md` 第 1 条「3D 质感」（原文见 §9）
> 管线依据：`research/agent-art/blender/workflow.md`（探针实测）＋ 本目录 `build_scene.py`（可复跑：`blender -b --factory-startup --python build_scene.py`）
> 参考片：`ref/04-3d-render.mp4`（`Vincentwei1021/mg-styles-15` videos/，MIT，2026-10-15 raw 直取）＋ `ref/src/`（作者 Blender 源码，仅作运动设计参考）
> 证据分级：本文件数字全部 = 本机实跑输出（原样粘贴）；推断处标 [推测]。

**结论一行：out.mp4 = 1920×1080 / 30fps / 300 帧 / 10.000s（h264 + 代码合成音轨，-18.91 LUFS / -1.28 dBTP）；机制逐条全部有机械证据（§4：玻璃折射双开关像素差 0.015805、橡胶 SSS 0.000757、软体压缩 1.007→0.53→0.665、刚体挤开 max 2.639 / 45 颗位移 >1.0、波浪公式误差 0.00554、运动模糊 f108 差 0.0100、软阴影宽度 3→235px、浅景深 CoC 13.8px@5m）；乱序重渲 = 视觉一致（EEVEE 采样随机性，最大 5/255、占比 <0.05% 像素）——本线确定性水平 P1，非 P0（详见 §6）。**

## 1. 交付物清单

| 文件 | 说明 |
|---|---|
| `build_scene.py` | 场景脚本：建场（玻璃弹珠 270 + 橡胶 PLAY）→ 脚本波浪 → 刚体解算 → 烘焙全部运动到关键帧 → 剥离物理 → 保存 scene.blend |
| `render_frames.py` | 渲染器（--frames/--range/--pct/--samples/--nomb/--skip），用于测试帧、关键帧、全片、乱序重渲 |
| `scene.blend` | 烘焙后的场景（无物理，纯关键帧 → 渲染确定性由关键帧保证） |
| `frames/f0000.png … f0299.png` | 300 张逐帧 PNG（1920×1080） |
| `key/k0000/k0050/k0100/k0150/k0200/k0250.png` + `key/keyframes_sheet.png` | 6 关键帧 + 3×2 拼图 |
| `out.mp4` | 成片（h264 + aac；音轨 = 代码合成 `audio/score.wav`） |
| `video.mp4` | 无音轨画面版（编码中间产物） |
| `audio/score.wav`（+`score_raw.wav`） | 代码合成音轨（numpy 合成，无采样；`gen_audio.py`；卡点取自 `checks/bake_stats.json` 的接触帧） |
| `checks/` | 自查脚本 + 全部原样输出（build/render/mech/softbody/selfcheck/rerun/accept/loudnorm）+ `bake_stats.json`、`bake_data.npz`、机制渲染图 `mech/`、对照帧 `probe/`、测试帧 `test/` |
| `ref/` | 官方参考片 + 作者 Blender 源码（MIT） |

## 2. 验收命令（原样输出）

```
### ffprobe frame count (out.mp4)
300

### ffprobe streams/format (out.mp4)
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
size=10253026
bit_rate=8202420

### key/ listing
key/k0000.png
key/k0050.png
key/k0100.png
key/k0150.png
key/k0200.png
key/k0250.png

### key sizes + hashes
key/k0000.png 2422238 1abcdb48f4090faa
key/k0050.png 2407073 cc19a592d79f9722
key/k0100.png 2359602 2b43fdef864231f7
key/k0150.png 2326212 4085b99055021746
key/k0200.png 2191054 db023142e87bd663
key/k0250.png 2142511 e06acb3c45738902

### frames count + first/last
300
frames/f0000.png
frames/f0001.png
frames/f0298.png
frames/f0299.png

### audio
codec_name=pcm_s16le
sample_rate=44100
channels=2
duration=10.000000
size=1764078

### video.mp4 (silent intermediate)
codec_name=h264
width=1920
height=1080
r_frame_rate=30/1
duration=10.000000
size=9996930
```

## 3. 6 关键帧（0/50/100/150/200/250）

| 文件 | 大小 | sha256[:16] |
|---|---|---|
| `key/k0000.png` | 2422238 B | 1abcdb48f4090faa |
| `key/k0050.png` | 2407073 B | cc19a592d79f9722 |
| `key/k0100.png` | 2359602 B | 2b43fdef864231f7 |
| `key/k0150.png` | 2326212 B | 4085b99055021746 |
| `key/k0200.png` | 2191054 B | db023142e87bd663 |
| `key/k0250.png` | 2142511 B | e06acb3c45738902 |
| `key/keyframes_sheet.png` | 3978305 B | 6ed0b1fe7f29d87c |

- 6 张全部 1920×1080；分镜对应：k0000 弹珠海（波浪）→ k0050 海面起伏、镜头推近中 → k0100 PLAY 落到珠面（首触帧，sim 接触帧 f100）→ k0150 弹起后回落、弹珠被挤开成坑 → k0200 字母沉入珠堆 → k0250 结尾定格（字母半埋、弹珠围拢）。
- 拼图 `key/keyframes_sheet.png` 由 `make_sheets.py`（numpy + bpy，无 PIL）生成，带帧号标签。

## 4. 机制逐条核验

> 以下 M1–M7 全部为 `blender -b scene.blend -P checks/check_mechanisms.py` 的原样输出（本机实跑）。
> 注：输出中的 `BlenderMCP` 行 = 本机已装插件在后台模式的注册噪音（不启动服务器、不影响渲染，输出可复现）。
> 附：软体专项 `checks/softbody_check.py` 原样输出见 §4.7；刚体/波浪数据见 §4.8/§4.9。

### 4.0 机制检查原样输出（M1–M7）

```
00:00.406  blend            | Read blend: "D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\scene.blend"
BlenderMCP: cannot start server in background mode (blender -b) - commands would never execute
BlenderMCP: run Blender with a GUI, or use a virtual display: xvfb-run -a blender
BlenderMCP addon registered
=== M1. scene data ===
marbles: 270 | unique meshes: {'marble_shared'} | mesh users: 279
strays: 7 | PLAY: True | rigid bodies left: 0 | rb world: None
lights: ['fill', 'key', 'rim', 'spec', 'wall']
--- wave check (row j=8, z at f=0/10/20/30/40) ---
f00: 0.328 0.346 0.395 0.466 0.547 0.623 0.678 0.704 0.694 0.653 0.588 0.514 0.446 0.397 0.377
f10: 0.428 0.363 0.312 0.296 0.299 0.346 0.414 0.495 0.575 0.640 0.676 0.672 0.649 0.590 0.523
f20: 0.576 0.550 0.497 0.428 0.357 0.298 0.265 0.265 0.300 0.362 0.441 0.523 0.591 0.633 0.643
f30: 0.501 0.559 0.594 0.603 0.579 0.525 0.453 0.376 0.306 0.262 0.256 0.270 0.326 0.399 0.477
f40: 0.383 0.413 0.465 0.529 0.588 0.630 0.642 0.622 0.571 0.497 0.415 0.340 0.285 0.261 0.272
max |measured - formula| over rows: 0.00554
m0_0 location key counts per axis: [75, 75, 75]
PLAY fcurves: [('location', 0, 148), ('location', 1, 148), ('location', 2, 148), ('rotation_euler', 0, 148), ('rotation_euler', 1, 148), ('rotation_euler', 2, 148), ('scale', 0, 191), ('scale', 1, 191), ('scale', 2, 191)]
=== M2. glass refraction dual-switch matrix (f150, 480x270, 16spp) ===
glass materials: ['glass_amber', 'glass_aqua', 'glass_clear', 'glass_lime', 'glass_rose', 'glass_sky', 'glass_violet'] | use_raytrace_refraction: True
00:01.500  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\refr_False_False.png'
00:01.703  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\refr_False_True.png'
00:02.015  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\refr_True_False.png'
00:02.250  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\refr_True_True.png'
scene_raytracing=False mat_refraction=False -> {'mean': 0.0, 'max': 0.0, 'frac_gt_002': 0.0}
scene_raytracing=False mat_refraction=True -> {'mean': 9e-06, 'max': 0.02353, 'frac_gt_002': 2e-05}
scene_raytracing=True mat_refraction=False -> {'mean': 0.006857, 'max': 0.38431, 'frac_gt_002': 0.10833}
scene_raytracing=True mat_refraction=True -> {'mean': 0.015805, 'max': 0.39608, 'frac_gt_002': 0.27808}
=== M3. rubber SSS toggle (f250, 480x270) ===
rubber Subsurface Weight = 0.75 | Radius = (0.4000000059604645, 0.15000000596046448, 0.10000000149011612) | Scale = 0.11999999731779099
00:02.500  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\sss_on.png'
00:02.953  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\sss_off.png'
sss on vs off: {'mean': 0.000757, 'max': 0.31373, 'frac_gt_002': 0.01154}
=== M4. metal reflection (chrome vs matte, f250) ===
chrome: Metallic 1.0 Roughness 0.07999999821186066
00:03.218  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\metal_metal.png'
00:03.437  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\metal_matte.png'
chrome vs matte-diffuse: {'mean': 0.001568, 'max': 0.49412, 'frac_gt_002': 0.00955}
=== M5. DOF: gradient energy focus vs background (f250, 960x540) ===
00:04.015  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\dof_f250.png'
gradient energy: focus=0.02336 background=0.02951 near-field=0.00346 | focus/bg ratio=0.79
camera dof: fstop 1.100000023841858 | focus_distance 7.65 | blades 0
=== M6. motion blur on/off (f95 fall, f108 scatter, 480x270) ===
00:04.265  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\mb_off_95.png'
00:04.562  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\mb_on_95.png'
f95 on vs off: {'mean': 0.004306, 'max': 0.60392, 'frac_gt_002': 0.04892}
00:04.797  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\mb_off_108.png'
00:05.078  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\mb_on_108.png'
f108 on vs off: {'mean': 0.010015, 'max': 0.82745, 'frac_gt_002': 0.11908}
=== M7. penumbra width vs light size (mini scene, 512x512) ===
D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\check_mechanisms.py:169: DeprecationWarning: 'Material.use_nodes' is expected to be removed in Blender 6.0
  mf = bpy.data.materials.new("F"); mf.use_nodes = True
00:05.328  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\pen_0.1.png'
BlenderMCP server stopped
BlenderMCP addon unregistered
light size 0.1 -> penumbra 3 px
00:05.437  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\pen_2.0.png'
light size 2.0 -> penumbra 235 px
00:05.562  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\pen_8.0.png'
light size 8.0 -> penumbra 235 px
=== MECH DONE ===
MECH_DONE
Blender 5.2.1 LTS (hash 9e2066aef7ef built 2026-08-25 02:38:20)

Blender quit
```

### 4.5 浅景深（补充测量）

M5 的「梯度能量」指标受内容混淆（字母表面平滑、背景含珠缘），另做两项同内容测量（原样输出：`checks/dof_check2_out.txt` / `checks/dof_check3_out.txt` / `checks/dof_check4_out.txt`）：

- **Laplacian 高频能量（同为弹珠区域）**：focus 0.01276 / mid 0.01871 / near 0.00974 / far 0.00534 → **focus/far = 2.39**（远场细节为焦区的 42%）。
- **光圈对拍（f/22 深焦 vs 交付 f/1.1，f250 帧，960×540）**：近景弹珠像素差 0.03945（强模糊差异）、字母区 0.01761、远景 0.00277、平滑背景 0.00086。
- 相机解析 [计算]：64mm / f1.1 / 对焦 7.65m → 焦深约 7.2–8.1m（±0.45m）；CoC：5m≈13.8px、10m≈6.1px、12m≈9.4px、20m≈16px（1080p）。

### 4.7 软体压扁 + 地面碰撞（专项场景）

**实现说明（诚实口径）**：成片里 PLAY 的「压扁」用 **squash & stretch 关键帧**（workflow.md §4.1 的 MG 现实选择：软体求解慢且难调，且 Blender 刚体/软体互不相通——刚体弹珠无法被软体推动）。「软体压扁+地面碰撞」机制本身用专项场景核验：立方体基线（probe9 配方）压缩 **1.007 → 0.53（-47%）→ 回弹 0.665**，与 probe9 公开数字一致；**PLAY 字母网格两次软体尝试（subsurf 1 / subsurf 2）均数值发散**（薄壳特征+求解器，见下方输出）——这恰好印证了 workflow §4.1「字母类薄网格用关键帧压扁」的结论。

```
Blender 5.2.1 LTS (hash 9e2066aef7ef built 2026-08-25 02:38:20)
CUBE_SAMPLES: [{"f": 1, "min_z": -0.504, "max_z": 0.504, "height": 1.007}, {"f": 6, "min_z": -0.625, "max_z": 0.382, "height": 1.007}, {"f": 10, "min_z": -0.884, "max_z": 0.123, "height": 1.007}, {"f": 14, "min_z": -1.277, "max_z": -0.27, "height": 1.007}, {"f": 20, "min_z": -1.386, "max_z": -0.856, "height": 0.53}, {"f": 30, "min_z": -1.387, "max_z": -0.722, "height": 0.665}, {"f": 40, "min_z": -1.385, "max_z": -0.722, "height": 0.663}]
00:03.734  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\softbody_cube_f01.png'
00:03.922  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\softbody_cube_f20.png'
CUBE_DONE
PLAY_SAMPLES: [{"f": 5, "height": 0.781, "min_z": -0.391}, {"f": 10, "height": 0.781, "min_z": -0.391}, {"f": 15, "height": 0.781, "min_z": -0.391}, {"f": 20, "height": 314736210083840.4, "min_z": -0.391}, {"f": 25, "height": 410992936747008.4, "min_z": -0.391}, {"f": 30, "height": 691179825922048.5, "min_z": -0.472}, {"f": 35, "height": 843079531626496.5, "min_z": -0.46}, {"f": 40, "height": 1012489751887872.5, "min_z": -0.458}, {"f": 45, "height": 1234167308222464.5, "min_z": -0.611}, {"f": 50, "height": 1345562251100160.5, "min_z": -0.562}]
PLAY_MIN_HEIGHT: 0.781 | PLAY_MIN_Z: -312059505934336.0
06:48.594  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\softbody_play_f01.png'
06:49.125  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\softbody_play_f22.png'
06:49.453  render           | Saved: 'D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\checks\mech\softbody_play_f36.png'
SOFTBODY_DONE
 250

Blender quit
```

字母网格软体第二次尝试（subsurf 2，16964 顶点，放宽刚度）原样输出：

```
PLAY2_VERTS: 16964
PLAY2_SAMPLES: [{"f": 1, "height": 0.781, "min_z": -0.391}, {"f": 10, "height": 204.967, ...}, {"f": 30, "height": 476.599, ...}]
（数值发散：height 爆炸到 1e2 量级 → 软体求解器对薄壳字母网格不稳定）
```

### 4.8 刚体挤开（成片数据）

成片弹珠的横向散射 = **真实 Bullet 刚体解算**（270 颗中中央 195 颗带刚体；外侧 75 颗为无物理装饰行，见 §8），解算后逐帧烘焙为关键帧。`checks/bake_stats.json` 原样摘录：

```
{
 "contacts": [
  [
   100,
   7.05
  ],
  [
   159,
   2.6
  ]
 ],
 "play_z_f100": 0.517,
 "play_z_f150": 0.481,
 "play_z_f250": 0.0,
 "play_z_f299": 0.0,
 "marbles_moved_gt_03": 54,
 "marbles_moved_gt_10": 45,
 "max_radial_disp": 2.639,
 "max_radial_disp_mid_f150": 0.273,
 "sample_marbles": [
  {
   "name": "m0_2",
   "base": [
    -3.921,
    -3.636,
    0.25
   ],
   "final": [
    -3.936,
    -3.624,
    0.243
   ]
  },
  {
   "name": "m3_11",
   "base": [
    -2.255,
    1.398,
    0.25
   ],
   "final": [
    -2.273,
    1.399,
    0.25
   ]
  },
  {
   "name": "m7_8",
   "base": [
    -0.006,
    -0.296,
    0.25
   ],
   "final": [
    -0.267,
    -1.367,
    0.253
   ]
  },
  {
   "name": "m11_5",
   "base": [
    2.25,
    -1.941,
    0.25
   ],
   "final": [
    2.27,
    -1.969,
    0.254
   ]
  },
  {
   "name": "m14_14",
   "base": [
    3.927,
    3.062,
    0.25
   ],
   "final": [
    3.932,
    3.079,
    0.245
   ]
  }
 ],
 "timing_sim_s": 62.2,
 "build_s": 64.0
}
```

- 接触帧 f100（冲击速度 7.05 m/s）→ 弹珠被挤开：**54 颗位移 >0.3、45 颗 >1.0、最大径向位移 2.639**（初始最大径向 4.8）。
- 备注：竖直方向的「弹跳小波浪」是在解算结果上叠加的脚本层（§8）；横向挤开全部来自解算。

### 4.9 弹珠波浪（实例化）

- M1 输出中「wave check」行：波浪 z 值与闭式公式（双正弦行波）逐行对比，**最大误差 0.00554**（原样输出见 §4.0，5 帧 × 15 列全量比对）；**270 颗弹珠共享 1 个 mesh 数据块（marble_shared）**，实例化 = `ob.copy() + 共享 mesh + 逐对象材质槽覆盖`。
- 波浪 = 双正弦行波（f0–f78 相位随 (i,j) 线性推进，f52–90 平滑退场交给物理），逐帧关键帧由公式直接采样。

## 5. 逐帧自查（300 帧）

```
frame count: 300
.. f0000.png
.. f0050.png
.. f0100.png
.. f0150.png
.. f0200.png
.. f0250.png
global mean range: 0.4805 .. 0.5438
frame-to-frame mean-lum delta: median 0.01085 | max 0.06273 at f0114.png
flags: none
top jumps: [('f0114.png', 0.06273), ('f0113.png', 0.06246), ('f0115.png', 0.06223), ('f0116.png', 0.06202), ('f0112.png', 0.06126), ('f0111.png', 0.05988), ('f0117.png', 0.05822), ('f0081.png', 0.05717)]
SELFCHECK_DONE
Blender 5.2.1 LTS (hash 9e2066aef7ef built 2026-08-25 02:38:20)

Blender quit
```

（完整数据 `checks/selfcheck_stats.json`；审片拼图 `checks/review_sheet.png`（每 10 帧）与 `checks/review_fine.png`（每 3 帧）。）

## 6. 乱序重渲抽查（确定性）

```
frame 123: rerun acde2b2e009aafcc | original 714e2a3e06521ff9 | DIFFER (3.2s)
frame 234: rerun eb44c3b12cf20b97 | original 836177e28af83b4d | DIFFER (2.2s)
RERUN_DONE
```

**确定性说明（重要发现）**：Blender 5.2 EEVEE 在本场景下**不产出逐字节一致的渲染**（同进程连续两次渲同一帧的 sha256 也不同）。已量化（原样输出见 `checks/probe/`、`checks/rerun_pixdiff.txt`）：

- 跨进程重渲 f123/f234：mean 0.000194 / 0.000186，max 5/255 / 1/255，受影响像素 ≤0.05%；
- 跨进程重渲 f10/f30：mean 0.00011 / 0.00013，max ≤2/255，受影响像素 ≤0.05%；
- 同进程双渲 f30：mean 0.000096，max 2/255，占比 0.039%；
- 关掉 raytracing 去噪、关掉运动模糊后仍不同 → 随机性在 EEVEE 采样核心（TAA/光追抖动），不是管线 bug。

**结论：本线确定性水平 = P1（视觉一致），不是 P0（逐字节一致）**——与 HTML 线（#1/#2 达到 P0）不同，Blender 线应以「像素级容差比对」为验收口径。运动/几何本身是确定的（烘焙关键帧；`build_scene.py` 的 post-bake check = 0.000000）。

## 7. 性能与预算（原样数据）

- 全片渲染日志（`checks/render_log.txt`）：frames in log: 300 | per-frame mean 2.53s (min 2.20 / max 4.30) | total 757.8s for 300 frames
- 预算口径：任务给定 EEVEE ~3.5s/帧 → 300 帧 ≈ 18 min；超 90 min 才降级。实测全片渲染 **未超 90 min，300 帧完整交付**（实际总时长见上；含并发自查竞争，比静置单帧慢）。
- 单帧静置测速（key 帧，满设置 64spp + MB16）：2.5–3.6s/帧。
- 构建（sim+bake）总耗时：64.0s，其中刚体解算 62.2s。

## 8. 已知限制与诚实说明

1. **压扁实现**：squash & stretch 关键帧（非软体求解），理由与核验见 §4.7；压缩峰值 33%（sy 0.67）、含二次落地补压与阻尼震荡（"晃几下才停"）。
2. **竖直弹跳层**：弹珠的竖直「蹦跳波浪」为脚本叠加（闭式 sin² 抛物线，作者式做法），横向挤开为纯解算——原因：实测平底重块压密排床只产生横向挤压（max |dz|=0.094）。
3. **装饰行**：270 颗弹珠中 75 颗（最外 2 排 + 最里 3 排）无刚体（仅波浪 + 落点退场 + 微弹跳脚本），中央 195 颗全程物理——原因是全 270 颗参与时解算退化为「蠕动」（max 位移 1.14→0.84），拆分后恢复爆开（2.639）。
4. **字母最终沉入珠面**（play_z f299 = 0.0）：重块把珠层压开后的自然结果，视觉为「砸进珠堆半埋」。
5. **EEVEE 折射为屏幕空间**：玻璃弹珠的折射是屏幕空间近似（双开关已开）；个别角度可能有轻微非物理，属 EEVEE 限制（workflow §3.1 已注明）。
6. **音轨不在验收硬指标内**（验收只要求 out.mp4 存在），但按卡要求合成并卡点（冲击 f100=3.33s、二次落地 f159=5.30s）。
7. **Blender 5.2 刚体两个实测坑**（本线新增发现，已影响本片构建方式）：
   - 手动 `frame_set` 推进刚体解算在无头流程中会「冻结」（从非 1 帧开始）；必须用 `point_cache.frame_start/end` + `ptcache.bake_all` 再读；
   - 刚体「原型拷贝」模式有坑：逐拷贝 `object_add`、或拷贝后删除源对象，会让接触求解退化为「软/蠕动」（无散射）；可用模式 = 源对象先加刚体 → 拷贝继承 → 保留源对象（远移 + hide_render）。
8. **后处理**：合成器仅加了轻度 Bloom（阈值 1.5 / 强度 0.08）。

## 9. 提示词原文（卡 01「3D 质感」）

> 用代码做一支 10 秒的 3D 动画（1920×1080，30 帧），用 Blender 的 Python 脚本搭场景、渲染，配乐音效用代码合成、跟画面卡点；先出 6 张关键帧给我看，再做动画，最后逐帧自查。
>
> 画风：3D 质感。材质一眼认得出：玻璃会折射，橡胶透一点光，金属映出周围；大面积柔光、软阴影、无缝棚拍背景；浅景深，焦外明显虚化；东西有分量：掉下来压扁、回弹、晃几下才停，还会挤开旁边的东西；一大片一样的小物体像波浪一起起伏；快动作带运动模糊。
>
> 内容：【一片彩色玻璃弹珠像海浪一样起伏，一个橡胶做的「PLAY」掉进去，压扁、弹起、挤开弹珠，镜头慢慢推近】
>
> 别做成：默认的塑料材质、硬阴影、全画面都清楚。

## 10. 附录

### 10.1 构建日志（`checks/build_log.txt`，去掉逐帧 bake 进度行）

```
[build    0.0s] eevee: samples 64 rt True rt_res 1 mb_steps 16
D:\Project\Designers_Brain\research\experiments\anim_test_03_blender\build_scene.py:115: DeprecationWarning: 'Material.use_nodes' is expected to be removed in Blender 6.0
  m.use_nodes = True
[build    0.0s] materials done: ['amber', 'aqua', 'chrome', 'clear', 'cyc', 'gold', 'lime', 'rose', 'rubber', 'sky', 'violet']
[build    0.0s] cyc done, verts 3577
[build    0.1s] marbles: 195 + deco: 75 | shared mesh users: 272
[build    0.1s] strays: 7
[build    0.1s] PLAY: verts 1148, bbox w 2.550 h 0.872 t 0.781
[build    0.1s] lights done
[build    0.1s] world done
[build    0.1s] physics set: world + 195 marbles + PLAY
Blender 5.2.1 LTS (hash 9e2066aef7ef built 2026-08-25 02:38:20)
[build   62.3s] sim done in 62.2s
[build   62.3s] pz coarse: [3.05, 2.96, 2.7, 2.26, 1.65, 0.87, 0.68, 0.89, 0.92, 0.77, 0.52, 0.57, 0.52, 0.52, 0.5, 0.5, 0.49, 0.49, 0.48, 0.47, 0.45, 0.4, 0.31, 0.25, 0.18, 0.07, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[build   63.4s] physics stripped; remaining rigid bodies: 0 | world: None
[build   63.4s] contacts: [(100, 7.05), (159, 2.6)]
[build   63.4s] pop layer: max hop = 0.899
[build   63.9s] marble keys done in 0.4s (168 keys each)
[build   64.0s] deco keys done
[build   64.0s] squash: max |s| = 0.373 at t=3.40s
[build   64.0s] PLAY keys done (c1=100)
[build   64.0s] camera keys done; c1=100
[build   64.0s] compositor done {'Type': 'Bloom', 'Quality': 'High', 'Threshold': 1.5, 'Strength': 0.08, 'Size': 0.4}
[build   64.0s] post-bake check: marble0 delta at f200 = 0.000000
Info: Saved as "scene.blend"
[build   64.0s] saved scene.blend; stats: {"contacts": [[100, 7.05], [159, 2.6]], "play_z_f100": 0.517, "play_z_f150": 0.481, "play_z_f250": 0.0, "play_z_f299": 0.0, "marbles_moved_gt_03": 54, "marbles_moved_gt_10": 45, "max_radial_disp": 2.639, "max_radial_disp_mid_f150": 0.273, "sample_marbles": [{"name": "m0_2", "base": [-3.921, -3.636, 0.25], "final": [-3.936, -3.624, 0.243]}, {"name": "m3_11", "base": [-2.255, 1.398, 0.25], "final": 
BUILD_DONE

Blender quit
```

### 10.2 渲染日志摘要

```
frames in log: 300 | per-frame mean 2.53s (min 2.20 / max 4.30) | total 757.8s for 300 frames
```

### 10.3 音轨响度（ffmpeg loudnorm 原样输出）

```
    Metadata:
      encoder         : Lavc63.1.101 pcm_s16le
[Parsed_loudnorm_0 @ 0000028d77a4a840] 
{
	"input_i" : "-18.91",
	"input_tp" : "-1.28",
	"input_lra" : "5.50",
	"input_thresh" : "-29.18",
	"output_i" : "-16.48",
	"output_tp" : "-1.50",
	"output_lra" : "4.40",
	"output_thresh" : "-26.66",
	"normalization_type" : "dynamic",
	"target_offset" : "0.48"
}
[out#0/null @ 0000028d779d38c0] video:0KiB audio:7500KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown
size=N/A time=00:00:10.00 bitrate=N/A speed=35.2x elapsed=0:00:00.28
```

### 10.4 复跑方法

```bash
cd research/experiments/anim_test_03_blender
"D:/Software/Blender Foundation/Blender 5.2/blender.exe" --background --factory-startup --python build_scene.py
"D:/Software/Blender Foundation/Blender 5.2/blender.exe" -b scene.blend -P render_frames.py -- --range 0:299 --out frames --skip
python gen_audio.py
ffmpeg -y -framerate 30 -start_number 0 -i frames/f%04d.png -i audio/score.wav -c:v libx264 -pix_fmt yuv420p -crf 16 -c:a aac -b:a 192k -shortest -movflags +faststart out.mp4
```

## 11. 自审四段

### A. 早产出
6 张关键帧 + 拼图在场景冻结前先行产出（构图/材质/速度确认），成片 300 帧一次性渲染（757.8s），无返工重渲；测试帧（f1/f22/f36/f50/f100/f150/f250/f299）先于全片。

### B. 反驳（对最强结论逐条试推翻）

1. 「玻璃折射需双开关」：试推翻——材质开关单独开是否足够？`scene_raytracing=False mat_refraction=True` → mean 9e-06（无效）；`True_False` → 0.0069；`True_True` → 0.0158。**CONFIRMED**（双开关必要；注意场景开关贡献更大，0.0069 来自光追全局效果而非折射本身）。
2. 「乱序重渲视觉一致（P1）」：试推翻——换帧重渲是否出现大差异？抽查 f10/f30/f123/f234 共 4 帧，max 5/255、受影响像素 ≤0.05%。**CONFIRMED（抽样范围内）**；样本 4/300 帧，未做全片重渲（成本 ~13 min），结论限定于抽样。
3. 「挤开来自解算而非脚本」：试推翻——位移是否来自脚本 pop 层？pop 层只改 Z；bake_stats 采样弹珠的 XY 位移（如 m7_8：(-0.006,-0.296)→(-0.267,-1.367)，横向 1.10m）与 f150 中间态 max_radial_mid=0.273（渐进爆开）均来自 Bullet 解算输出。**CONFIRMED**。
4. 「波浪公式误差 0.00554」：试推翻——是否自证循环（检查脚本与 build 用同一公式）？是同一闭式公式，该数字只证明「关键帧采样保真」，不证明波浪审美；后者由 §4.0 数值表（行波推进：波峰 f0 在 i≈7 → f20 在 i≈14）与关键帧拼图佐证。**CONFIRMED（限定口径）**。
5. 「渲染未超预算」：试推翻——per-frame 2.53s 是否超过任务给的 ~3.5s/帧？2.53 < 3.5；总 757.8s ≈ 12.6 min < 90 min（降级线）。**CONFIRMED**。

### C. 机械验证（原样输出，详见上文各节）
```
scene_raytracing=True mat_refraction=True -> mean 0.015805 / max 0.39608 / frac 0.27808
light size 0.1 -> penumbra 3 px | light size 2.0 -> penumbra 235 px | light size 8.0 -> penumbra 235 px
max |measured - formula| over rows: 0.00554
global mean range: 0.4805 .. 0.5438 | flags: none
ffprobe -count_frames out.mp4 -> 300
```

### D. 小结
- 交付：`out.mp4`（1920×1080/30fps/300 帧/10.000s，h264+aac）+ 300 PNG + 6 关键帧 + 拼图 + 本 `checks.md`，全部齐备。
- 管线：`build_scene.py` 一键建场→波浪→刚体解算（62.2s）→烘焙关键帧→剥离物理→存 blend；渲染纯读关键帧（post-bake delta 0.000000）。
- 机制：折射/SSS/金属/软阴影/浅景深/运动模糊/压扁/挤开/波浪 9 项全部有像素级或数据级机械证据（§4）。
- 确定性：EEVEE 非逐字节确定（P1 视觉一致，max 5/255、≤0.05% 像素）；运动数据本身确定。
- 诚实缺口：字母软体两试均发散（改关键帧压扁，如实记录）；竖直弹跳为脚本层；75/270 弹珠为装饰行；结尾字母沉入珠面。
- 预算：全片渲染 12.6 min（预算 90 min 的 14%）；构建 64.0s；音轨 −18.91 LUFS。
- 交接：无阻塞项；若后续做双线（HTML+Blender）合并验收，建议按本线 P1 口径设计像素容差比对。
