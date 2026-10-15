# Blender bpy 工作流（GOALS B-03）

> 归属：BlenderScript。目标：把 01 卡「3D 质感」从提示词变成**可跑、可自查**的 bpy 管线。
> 机器：Windows x64，Blender **5.2.1 LTS**（`D:\Software\Blender Foundation\Blender 5.2\blender.exe`）。
> **本文所有带「[实测 2026-10-15]」的数字，都是本机真跑出来的**；探针脚本留在同目录 `_probe*.py`，可复跑。
> 证据分级：`[实测]` = 本机命令输出 · `[史料]` = 官方文档/手册原话 · `[归纳]` = 我们总结的操作规则 · `[推测]` = 未验证推断。
> 兄弟文档：`knowledge/domains/motion-graphics/cards/structure.md`（15 卡骨架）、`templates/style_card.md`。

---

## 0. 一分钟结论

1. 本机 Blender 已装且**无头渲染可用**：EEVEE 1080p 单帧 **3.53 s**，Cycles CPU 1080p 64spp **27.1 s**，RTX 5070 Ti 的 CUDA/OptiX 已被识别。[实测]
2. **Blender 5.2 有三个会咬人的 API 变更**：`Action.fcurves` 已删（改 slotted action）、`Scene.node_tree` 已删（改 `compositing_node_group`）、视频输出必须先设 `image_settings.media_type='VIDEO'`。照抄 4.x 教程的脚本会在这三处炸。[实测]
3. 01 卡「3D 质感」的六项要求**全部有确定实现路径**，且其中五项我做了像素级验证（运动模糊 / 玻璃折射 / 橡胶次表面 / 软阴影 / 压扁回弹）。[实测]
4. **压扁不能用刚体**——刚体是刚性的。压扁 = 软体（Soft Body）+ 地面 Collision 修改器；我刚测出 1.007 → 0.53 的压缩。[实测]
5. 「挤开周围物体」用刚体就够：49 颗弹珠被砸到最远 5.96 单位（初始最远 2.55）。[实测]

---

## 1. 无头渲染

### 1.1 三种调用形态

| 形态 | 命令 | 用途 |
|---|---|---|
| 跑脚本、不渲染 | `blender --background --python script.py` | 建场景 / 导出 / 调试 |
| 渲染已有 .blend | `blender -b file.blend -a` | 纯渲染，不改脚本 |
| 跑脚本并渲染 | `blender -b --python script.py`（脚本里自己调 `bpy.ops.render.render`） | **推荐**：全部逻辑在脚本里，命令行只是壳 |

本机验证过的完整调用 [实测]：

```bash
"D:/Software/Blender Foundation/Blender 5.2/blender.exe" \
  --background --factory-startup --python script.py
```

- `--background`（=`-b`）：无 UI。手册原文：「One advantage of using the command line is that we do not need a graphical display」[史料: Blender 5.2 Manual → Rendering From The Command Line]
- `--factory-startup`：**忽略用户偏好**。agent 必加——否则你的启动文件、插件、快捷键会污染结果，同一脚本在两台机器上跑出不同画面。
- `--python` 后面**不要**再加 `--` 或位置参数；要传参用环境变量或 `--` 分隔后自己解析 `sys.argv`。

### 1.2 参数顺序是硬约束 [史料]

手册原话：「Arguments are executed in the order they are given!」并且「**Always** position `-f` or `-a` as the last arguments.」

```bash
# 错：-o 在 -a 之后，输出路径不生效
blender -b file.blend -a -x 1 -o //render
# 对：
blender -b file.blend -x 1 -o //render -a
```

其他常用参数 [史料]：`-f 10`（只渲第 10 帧）、`-o /path/frame_#####`（五个补零位）、`-F OPEN_EXR`（覆盖格式；**`-F` 与 `-f` 大小写敏感**）、`-E CYCLES`（引擎，`blender -E help` 列全部）、`-s 10 -e 500`（起止帧）、`-t 2`（线程数）。

> ⚠️ `-o` 的 `#####` 只在**命令行**路径里生效。脚本里设 `scene.render.filepath` 时，补零由 `image_settings` 决定，实测输出是 **4 位**：`f_0001.png`。[实测]

### 1.3 EEVEE / Cycles 怎么选

本机引擎枚举实测 [实测]：`bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items` 只列出 `BLENDER_EEVEE`（静态枚举不含插件注册的引擎），但 `scene.render.engine = "CYCLES"` / `"BLENDER_WORKBENCH"` 均赋值成功，`cycles` 插件 `addon_utils.check()` 返回 `(True, True)`。**别用静态枚举判断 Cycles 有没有——要试赋值。**

| 维度 | EEVEE | Cycles |
|---|---|---|
| 本机 1080p 单帧（玻璃球+金属块+橡胶地+面积光+DOF，64 采样） | **3.53 s** [实测] | **27.1 s**（CPU 64spp + 降噪）[实测] |
| 折射/反射 | 屏幕空间，需显式开启（见 §3） | 物理正确，开箱即用 |
| 次表面散射 | 需 `use_sss_translucency` 才更准 | 物理正确 |
| 运动模糊 | 支持，`eevee.motion_blur_steps` 默认 **1**，必须调大 | 支持，`scene.render.use_motion_blur` |
| GPU | 默认走 GPU | 本机识别到 CUDA + OptiX（RTX 5070 Ti Laptop）/ ONEAPI（Intel 核显）[实测] |
| 适合 | **MG 动画**（快、可迭代） | 静帧海报、要真折射/真 SSS |

**默认选择 [归纳]**：10 秒 MG 动画（300 帧）用 **EEVEE**。按 3.53 s/帧估，300 帧 ≈ 17.7 分钟纯渲染；Cycles CPU 同规格 ≈ 135 分钟。等 EEVEE 结果出来后再决定要不要给个别镜头换 Cycles 重渲。

> ⚠️ 上面两个耗时是**同一台机器、同一个场景、只差引擎**的数字，分母是「1920×1080 单帧」。别把它当通用基准——场景复杂度一变数字就变。[实测]

**Cycles 开 GPU 的正确姿势**（本机已识别设备但 `compute_device_type` 默认是 `NONE`）[实测]：

```python
prefs = bpy.context.preferences.addons["cycles"].preferences
prefs.compute_device_type = "OPTIX"          # 或 "CUDA"
for d in prefs.devices:
    d.use = (d.type in {"OPTIX", "CUDA"})
scene.cycles.device = "GPU"
```

### 1.4 1080p / 30fps 输出

```python
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100     # 默认 100，别漏；50 会渲成 960×540
scene.render.fps = 30                        # 出厂默认是 24，必须显式改
scene.render.fps_base = 1.0
scene.frame_start = 1
scene.frame_end = 300                        # 10 秒 × 30fps
```

出厂默认实测 [实测]：分辨率 `1920×1080`、`resolution_percentage=100`、**`fps=24`**。所以 `fps` 是唯一必须改的——01 卡要 30 帧/秒。

### 1.5 帧序列 → ffmpeg 合成

**帧序列是推荐路径 [归纳]**：PNG 序列可断点续渲、可单帧复查、可换帧率重拼，mp4 不行。

```python
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"   # 或 RGB
scene.render.image_settings.color_depth = "8"
scene.render.filepath = r"D:\out\f_"               # 实测输出 f_0001.png …
bpy.ops.render.render(animation=True)
```

实测输出命名 [实测]：`f_0001.png` … `f_0010.png`（4 位补零，`count=10`）。

本机 ffmpeg 位置与版本 [实测]：
```
where ffmpeg            →  D:\Software\ffmpeg\bin\ffmpeg.exe
ffmpeg -version         →  ffmpeg version n9.0.1-11-ge47273f4d9-20260828
```

合成命令（本机 ffmpeg 在 PATH 上，可直接调）[归纳]：

```bash
ffmpeg -y -framerate 30 -start_number 1 -i "D:/out/f_%04d.png" \
       -c:v libx264 -pix_fmt yuv420p -crf 16 -movflags +faststart "D:/out/final.mp4"
```

- `-framerate 30` **必须在 `-i` 之前**——它是输入帧率，放后面会被当输出帧率，序列会被重定时。
- `%04d` 对应 Blender 的 4 位补零；位数对不上会「只找到 1 帧」。
- 音轨（01 卡要求「配乐音效用代码合成」）用第二路输入 + `-shortest`：
  ```bash
  ffmpeg -y -framerate 30 -i "D:/out/f_%04d.png" -i "D:/out/audio.wav" \
         -c:v libx264 -pix_fmt yuv420p -crf 16 -c:a aac -b:a 192k -shortest "D:/out/final.mp4"
  ```

### 1.6 Blender 自己也能出 mp4（5.2 有坑）

**必须先设 `media_type`，否则报错** [实测]：

```python
scene.render.image_settings.media_type = "VIDEO"      # ← 5.2 新增，默认 "IMAGE"
scene.render.image_settings.file_format = "FFMPEG"    # 不设上一行 → TypeError
scene.render.ffmpeg.format = "MPEG4"
scene.render.ffmpeg.codec = "H264"
scene.render.ffmpeg.constant_rate_factor = "HIGH"
```

跳过 `media_type` 直接设 `file_format="FFMPEG"` 会抛：
`TypeError: enum "FFMPEG" not found in ('AVIF','JPEG','OPEN_EXR','PNG','WEBP','BMP','CINEON','DPX','IRIS','JPEG2000','HDR','TARGA','TARGA_RAW','TIFF')`
——**注意报错列表里没有 FFMPEG，但静态枚举 `bl_rna.properties["file_format"].enum_items` 里却有**（16 项）。这是动态枚举过滤：先设 `media_type` 才解锁。[实测]

`media_type` 枚举实测 [实测]：`IMAGE` / `MULTI_LAYER_IMAGE` / `VIDEO`，默认 `IMAGE`。设完 `is_movie_format` 变 `True`。

实测产物 [实测]：30 帧 640×360 EEVEE，`_video_test.mp4`，**22,706 字节，3.63 s**。

**选择 [归纳]**：交付用 **PNG 序列 → ffmpeg**（可续渲、可自查）；Blender 直出 mp4 只在「快速看个大概」时用。

---

## 2. bpy 脚本结构

一个 agent 能维护的脚本 = **一个 `build()` + 若干 `add_*()` + 一个 `main()`**，全部幂等（从空场景重建，不依赖上一次运行的状态）。

```python
"""10 秒 3D 质感 MG 动画。用法：
blender -b --factory-startup --python build.py
"""
import bpy, math, os, sys
from mathutils import Vector

OUT = os.path.abspath(os.path.dirname(__file__) or ".")

# ---------- 0. 清场（幂等的前提）----------
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
    sc.render.resolution_percentage = 100
    sc.render.fps = 30
    sc.frame_start, sc.frame_end = 1, 300
    return sc
```

### 2.1 几何

```python
def add_primitive(kind, loc, name=None, **kw):
    getattr(bpy.ops.mesh, "primitive_%s_add" % kind)(location=loc, **kw)
    ob = bpy.context.active_object
    if name: ob.name = name
    return ob

sphere = add_primitive("uv_sphere", (0,0,1), "Marble", radius=0.35, segments=32, ring_count=16)
bpy.ops.object.shade_smooth()
```

- **务必 `shade_smooth()`**：否则球是几十个可见的平面。01 卡要「玻璃弹珠」，硬棱一定露馅。[归纳]
- 段数够用就行：半径 0.35 的弹珠 `segments=32, ring_count=16` 已经看不出多边形。段数直接乘渲染时间。[归纳]
- 大量重复物体**共享 mesh data**：`ob2 = ob.copy(); ob2.data = ob.data`。实测 144 个球用共享数据 + 逐帧关键帧，0.04 s 建完。[实测]

### 2.2 材质（Principled BSDF 的 5.2 输入名）

本机实测的完整输入名列表 [实测]（**4.x 教程里的 `Transmission` / `Subsurface` 在 5.2 已改名**）：

```
Base Color · Metallic · Roughness · IOR · Alpha · Thin Wall · Normal · Weight ·
Diffuse Roughness · Subsurface Weight · Subsurface Radius · Subsurface Scale ·
Subsurface IOR · Subsurface Anisotropy · Specular IOR Level · Specular Tint ·
Anisotropic · Anisotropic Rotation · Tangent · Transmission Weight · Coat Weight ·
Coat Roughness · Coat IOR · Coat Tint · Coat Normal · Sheen Weight · Sheen Roughness ·
Sheen Tint · Emission Color · Emission Strength · Thin Film Thickness · Thin Film IOR
```

```python
def mat(name, **kv):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    for k, v in kv.items():
        b.inputs[k].default_value = v      # 名字写错会 KeyError，不是静默失败
    return m
```

### 2.3 灯光

本机实测 [实测]：灯型 `POINT / SUN / SPOT / AREA`；AREA 灯出厂 `size=0.25`、`energy=10.0`、`spread=π`、`shadow_soft_size=0.0`。AREA 的可调属性含 `size` / `size_y` / `shape` / `spread` / `shadow_soft_size` / `shadow_filter_radius`。

```python
ld = bpy.data.lights.new("Key", type="AREA")
ld.size = 8.0            # ← 软阴影的唯一主开关，见 §3
ld.energy = 1200.0
lo = bpy.data.objects.new("Key", ld)
scene.collection.objects.link(lo)
lo.location = (-6, -7, 9); lo.rotation_euler = (0.75, 0, -0.7)
```

> 注意 `bpy.data.lights.new()` 造出来的灯**不在场景里**，必须 `collection.objects.link()`。漏了会「脚本跑通、画面全黑」。[归纳]

### 2.4 相机

本机实测出厂值 [实测]：`lens=50.0 mm`、`sensor_width=36.0`、`dof.use_dof=False`、`dof.focus_distance=10.0`、`dof.aperture_fstop=2.8`、`dof.aperture_blades=0`。

```python
cd = bpy.data.cameras.new("Cam")
cd.dof.use_dof = True
cd.dof.focus_distance = 9.0
cd.dof.aperture_fstop = 2.0
cd.dof.aperture_blades = 9        # ≥3 才有多边形散景
co = bpy.data.objects.new("Cam", cd)
scene.collection.objects.link(co)
scene.camera = co                 # ← 不设这个，渲染直接报 "Cannot render, no camera"
co.location = (0, -11, 3.2); co.rotation_euler = (1.30, 0, 0)
```

### 2.5 关键帧动画 —— ⚠️ 5.2 的 slotted action

**`Action.fcurves` 在 5.2 已被删除。** 实测报错 [实测]：
```
AttributeError: 'Action' object has no attribute 'fcurves'
```
正确路径（实测可读可写）[实测]：
```
action.layers[0].strips[0].channelbags[0].fcurves
```
实测结构 [实测]：`Action` 有 `layers` / `slots` / `is_action_layered` / `is_action_legacy`；`Layer` 只有 `strips`；`Strip` 有 `channelbag`（单数）与 `channelbags`；`Channelbag` 有 `fcurves` / `groups` / `slot`；slot 示例 `identifier="OBSphere"`、`name_display="Sphere"`、`target_id_type="OBJECT"`。

```python
# 写：老写法仍然好用
ob.keyframe_insert(data_path="location", frame=1)
ob.location.z = 3.0
ob.keyframe_insert(data_path="location", frame=30)

# 读/改：5.2 新路径
cb = ob.animation_data.action.layers[0].strips[0].channelbags[0]
fc = cb.fcurves[0]
for kp in fc.keyframe_points:
    kp.interpolation = "BACK"     # 01 卡的「回弹」缓动
    kp.easing = "EASE_OUT"
fc.update()
fc.modifiers.new(type="NOISE")    # 抖动/手持感
```

**给 agent 的兼容写法 [归纳]**（同一份脚本要能跑 4.x 和 5.x）：

```python
def fcurves_of(ob):
    act = ob.animation_data.action
    if hasattr(act, "layers") and len(act.layers):
        return act.layers[0].strips[0].channelbags[0].fcurves
    return act.fcurves                       # 4.x
```

### 2.6 物理

三类，按「要什么形状」选：

| 需求 | 用什么 | 关键点 |
|---|---|---|
| 掉落、回弹、晃动、挤开别人 | **Rigid Body** | 物体**不变形** |
| 压扁、被拉伸、软体弹跳 | **Soft Body** + 地面 Collision | 顶点级形变 |
| 布料、飘动 | **Cloth** | 同理需要 Collision |
| 流体 | **Fluid** 修改器 | 慢，MG 动画一般不用 |

```python
# 刚体
bpy.ops.rigidbody.world_add()
bpy.context.view_layer.objects.active = floor
bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
bpy.context.view_layer.objects.active = ball
bpy.ops.rigidbody.object_add(); ball.rigid_body.type = "ACTIVE"
ball.rigid_body.restitution = 0.6      # ← 出厂 0.0，不设就没有回弹
```

本机实测刚体出厂值 [实测]：
```
type=ACTIVE · mass=1.0 · friction=0.5 · restitution=0.0 ·
linear_damping=0.04 · angular_damping=0.1 · use_deactivation=False ·
deactivate_linear_velocity=0.4 · deactivate_angular_velocity=0.5 ·
collision_shape=CONVEX_HULL · collision_margin=0.04 · use_margin=False
world: substeps_per_frame=10 · solver_iterations=10 · time_scale=1.0
gravity=(0, 0, -9.81)
```

**⚠️ `bpy.ops.rigidbody.bake_to_keyframes()` 在 `--background` 下必失败** [实测]：
```
RuntimeError: Operator bpy.ops.anim.keyframe_insert_by_name.poll() failed, context is incorrect
```
`bpy.context.temp_override(...)` **也救不回来**（实测同样报错）[实测]。它是操作符内部调 `bpy.ops.anim.keyframe_insert_by_name` 时拿不到正确 context。

**替代方案 = 手动烘焙 [实测可用]**：逐帧 `frame_set()` → 读 `matrix_world` → `keyframe_insert()`：

```python
def bake_physics(ob, f0, f1):
    sc = bpy.context.scene
    ob.animation_data_clear()
    for f in range(f0, f1 + 1):
        sc.frame_set(f)
        bpy.context.view_layer.update()
        ob.location = ob.matrix_world.translation.copy()
        ob.keyframe_insert(data_path="location", frame=f)
```

实测：3 条 fcurve、30 个关键帧，0.02 s。[实测]

> **为什么值得烘焙**：物理缓存依赖求解器状态，换个 Blender 版本/机器结果会漂。烘成关键帧后，渲染变成纯确定性的，且能手动改某一帧。这是「同一提示词在不同机器上产出同一支片」的关键一步。[归纳]

### 2.7 粒子 / 实例

本机实测存在 [实测]：`ParticleSettings`、`PARTICLE_SYSTEM` / `PARTICLE_INSTANCE` 修改器、`GeometryNodeTree` 与 `GeometryNodeInstanceOnPoints` / `GeometryNodeMeshGrid` / `GeometryNodeSetPosition` / `GeometryNodeInputPosition` / `GeometryNodeRealizeInstances`。

**两条路 [归纳]**：
- **脚本驱动**（推荐给 agent）：`ob.copy()` + 共享 mesh + 逐帧 `keyframe_insert`。可控、可逐帧自查、不需要理解节点图。实测 144 个球 OK。[实测]
- **Geometry Nodes**：更省内存、可上万个实例，但要用代码搭节点图，且**节点类名会变**（实测 `GeometryNodeMath` / `GeometryNodeSine` 在本机不存在——数学节点复用 `ShaderNodeMath`，Sine 是它的一个 operation）[实测]。

### 2.8 合成器 —— ⚠️ 5.2 又一处变更

**`Scene.node_tree` 在 5.2 已删除** [实测]：
```
AttributeError: 'Scene' object has no attribute 'node_tree'
DeprecationWarning: 'Scene.use_nodes' is expected to be removed in Blender 6.0
```
新家是 `scene.compositing_node_group`（实测可赋值一个 `bpy.data.node_groups.new(name, "CompositorNodeTree")`，并在里面 `nodes.new("CompositorNodeGlare")` 成功）[实测]：

```python
ng = bpy.data.node_groups.new("Comp", "CompositorNodeTree")
scene.compositing_node_group = ng
ng.nodes.new("CompositorNodeGlare")
```

`Scene` 上仅剩的节点相关属性实测为：`compositing_node_group`、`use_nodes`。[实测]

---

## 3. 01 卡「3D 质感」逐条实现路径

01 卡画风段原文 [史料: `knowledge/domains/motion-graphics/origin/提示词全文.md` 01 段]：

> 材质一眼认得出：玻璃会折射，橡胶透一点光，金属映出周围；大面积柔光、软阴影、无缝棚拍背景；浅景深，焦外明显虚化；东西有分量：掉下来压扁、回弹、晃几下才停，还会挤开旁边的东西；一大片一样的小物体像波浪一起起伏；快动作带运动模糊。

逐条拆解：

### 3.1 玻璃折射 —— **两个开关都要开**

| 层 | 属性 | 出厂值 | 必须设成 |
|---|---|---|---|
| 材质 | `Principled BSDF → IOR` | 1.45（默认即玻璃） | 1.45 |
| 材质 | `Principled BSDF → Transmission Weight` | 0.0 | **1.0** |
| 材质 | `Principled BSDF → Roughness` | 0.5 | **0.02**（粗糙度一高就成毛玻璃） |
| 材质 | `material.use_raytrace_refraction` | **False** | **True** |
| 场景 | `scene.eevee.use_raytracing` | **False** | **True** |

**这是 EEVEE 侧最容易漏的一步。** 实测四组开关组合的像素差 [实测]（基准 = 全关）：

| `scene.eevee.use_raytracing` | `material.use_raytrace_refraction` | 相对基准平均像素差 | PNG 字节 |
|---|---|---|---|
| False | False | 0.0 | 141,172 |
| False | True | 0.001681 | 141,369 |
| True | False | 0.000430 | 143,050 |
| **True** | **True** | **0.033982** | **162,566** |

只有**两个都开**才是数量级的变化（平均差 0.034，文件大 15%）。单开任何一个基本等于没开。

选 Cycles 的话这两步不需要——物理光线追踪天然正确。

其他 EEVEE 相关材质属性实测 [实测]：`use_screen_refraction`（默认 False）、`use_transparent_shadow`（True）、`refraction_depth`（0.0）、`thickness_mode`（`SPHERE`）、`show_transparent_back`（True）、`blend_method`（`HASHED`）、`use_sss_translucency`（False）。

### 3.2 橡胶次表面（「透一点光」）

```python
b.inputs["Base Color"].default_value        = (0.85, 0.15, 0.2, 1)
b.inputs["Roughness"].default_value         = 0.75
b.inputs["Subsurface Weight"].default_value = 0.6      # ← 5.2 名字；4.x 叫 "Subsurface"
b.inputs["Subsurface Radius"].default_value = (0.4, 0.15, 0.1)   # 红光透得最远 = 真橡胶
b.inputs["Subsurface Scale"].default_value  = 0.15
```

实测：`Subsurface Weight` 0.0 → 0.9，平均像素差 **0.009706**，PNG 94,126 → 102,709 字节。**改这一个参数画面确实变**。[实测]

EEVEE 额外开关：`material.use_sss_translucency`（默认 `False`）——要「背面透光」的薄橡胶才开。[实测]

**`Subsurface Radius` 的红 > 绿 > 蓝是物理的**（红光在皮肤/橡胶里散射最远）。这是「橡胶一眼认得出」和「塑料」的分界线。[归纳]

### 3.3 金属反射

```python
b.inputs["Base Color"].default_value = (0.9, 0.75, 0.35, 1)   # 金色
b.inputs["Metallic"].default_value   = 1.0
b.inputs["Roughness"].default_value  = 0.18                    # 0.05–0.3 = 抛光到拉丝
```

**「金属映出周围」需要环境里有东西可映**。金属的观感 90% 来自反射内容，不是参数。[归纳]
- 最省事：给世界加一张 HDRI（blender-mcp 的 `search_assets` 可直接拉 Poly Haven 的 CC0 HDRI）。
- 无网络时：用几块大面积发光板（Emission 材质）+ 一个渐变世界。金属会映出这些板，就有「棚拍」感。

### 3.4 大面积柔光 / 软阴影 —— **灯 size 是唯一主开关**

实测（正交俯视，一个方块在地面上的投影，沿扫描线量 10%–90% 过渡带宽度）[实测]：

| 面积光 `size` | 半影宽度（像素） | PNG 字节 |
|---|---|---|
| 0.1 | **3** | 74,603 |
| 2.0 | **235** | 76,592 |
| 8.0 | 235（整条扫描线都在过渡带内 = 完全漫射） | 156,592 |

**0.1 → 3 px 是刀切；2.0 → 235 px 是柔光。** 差 78 倍。出厂 `size=0.25`，就是「硬阴影」的默认值——这正是 01 卡「别做成：硬阴影」要封堵的东西。

```python
ld.size = 8.0                 # 大面积柔光
ld.energy = 1200.0            # size 变大要同步补 energy，否则整体变暗
```

> ⚠️ 亮度守恒：面积光 `energy` 是总功率，`size` 翻倍 → 辐照度掉到 1/4。我实测时用 `energy ∝ size²` 补偿。[实测]

### 3.5 无缝棚拍背景（cyclorama）

做法 [归纳]：地面 + 后墙 + 转角处倒角（Bevel），三个件同材质、同色、无接缝。

```python
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))        # 地
bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 12, 10),
                                 rotation=(math.radians(90), 0, 0))  # 后墙
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 12, 0.5))       # 转角
cove = bpy.context.active_object
cove.scale = (20, 0.5, 0.5)
b = cove.modifiers.new("Bevel", "BEVEL"); b.width = 0.4; b.segments = 12
```

实测建场成功（6 个对象：Floor / BackWall / Cove / Ball / Cam / Key）[实测]。材质用**哑光中性灰**（`Roughness` 0.8–0.95、`Base Color` 0.5–0.8）——高光会把「无缝」暴露成一块亮斑。[归纳]

### 3.6 浅景深

本机实测出厂值 [实测]：`use_dof=False`、`focus_distance=10.0`、`aperture_fstop=2.8`、`aperture_blades=0`、`focus_object=None`。

```python
cd.dof.use_dof = True
cd.dof.focus_object = hero_obj        # 比 focus_distance 稳：物体一动焦点跟着走
cd.dof.aperture_fstop = 1.4           # 越小越虚
cd.dof.aperture_blades = 9            # ≥3 才有散景形状
```

手册原话 [史料: Blender 5.2 Manual → Cameras → Depth of Field]：「F-Stop ratio that defines the amount of blurring. **Lower values give a strong depth of field effect.**」「the minimum amount of blades to enable the bokeh effect is 3」。另有 `Rotation`（转散景角度）与 `Ratio`（<1 横向拉长 = 变形宽银幕散景）。

**「焦外明显虚化」的两个前提 [归纳]**：① 画面里得有前景/远景——全在焦平面上再大的光圈也不虚；② `focus_object` 指向主体，否则镜头推进时焦点会跑。

### 3.7 运动模糊

| 层 | 属性 | 出厂值 | 设成 |
|---|---|---|---|
| 场景 | `scene.render.use_motion_blur` | **False** | **True** |
| 场景 | `scene.render.motion_blur_shutter` | 0.5 | 0.5（= 半帧，标准电影感） |
| EEVEE | `scene.eevee.motion_blur_steps` | **1** | **8–16** |
| EEVEE | `scene.eevee.motion_blur_max` | 32 | 32（上限，一般不动） |

**`motion_blur_steps` 默认 1 = 几乎看不出模糊**，这是第二个坑。

实测证据（球在画面中央 2 帧内从 x=-2 移到 x=+2，480×270，EEVEE 16 TAA）[实测]：

| | PNG 字节 | 与 off 的平均像素差 | 最大像素差 |
|---|---|---|---|
| `use_motion_blur=False` | 48,347 | — | — |
| `use_motion_blur=True`（steps=16） | 52,383 | **0.004838** | **0.64706** |

平均差 0.0048 看着小，**最大差 0.647 说明局部（球的拖尾）被彻底改写了**——这正是「快动作带运动模糊」要的效果。

> ⚠️ 我第一版测试把球移出了取景框，`mean_abs_pixel_diff = 0.0`、两次渲染字节数完全相同（37,686）。**运动模糊只在物体可见且移动时改变画面**——这个「0 差异」当时差点被我误读成「EEVEE 不支持运动模糊」。[实测]

> 01 卡「别做成」里有「运动模糊」一条，指的是**滥用**（全片都糊）。所以它应该只在「快动作」帧开启，或者用逐帧开关 `scene.render.use_motion_blur` 精确控制。[归纳]

### 3.8 逐条 → 验收对照

| 01 卡要求 | 实现 | 可自查的数字 |
|---|---|---|
| 玻璃会折射 | `Transmission Weight=1` + 场景 raytracing + 材质 raytrace_refraction | 两开关都开后平均像素差 > 0.01 [实测] |
| 橡胶透一点光 | `Subsurface Weight 0.5–0.8` + Radius (0.4,0.15,0.1) | 开关 SSS 前后像素差 > 0.005 [实测 0.0097] |
| 金属映出周围 | `Metallic=1` + `Roughness 0.05–0.3` + 有内容的环境 | 金属区域像素方差 > 阈值（有反射内容才有方差） |
| 大面积柔光/软阴影 | AREA 灯 `size ≥ 3`，`energy ∝ size²` | 半影宽度 > 50 px [实测 0.1→3px / 2.0→235px] |
| 无缝棚拍背景 | 地+墙+倒角，同材质哑光灰 | 背景区域无接缝高光（扫描线无尖峰） |
| 浅景深 | `use_dof` + `focus_object` + `fstop ≤ 2` | 焦外区域高频能量低于焦内 |
| 掉下压扁回弹 | 软体（见 §4.1） | 落地瞬间包围盒高度 < 静置高度 [实测 1.007→0.53] |
| 挤开周围物体 | 刚体 ACTIVE 群 | 邻居位移 > 初始间距 [实测 最大径向 2.55→5.96] |
| 一大片小球波浪 | 实例化 + 脚本 sine | 相邻实例相位差恒定，逐帧 z 可预测 |
| 运动模糊 | `use_motion_blur` + `steps 8–16` | 开/关像素差 > 0 [实测 max 0.647] |

---

## 4. 物理细节

### 4.1 「掉下压扁、回弹、晃几下才停」

**关键认知：刚体压不扁。** 刚体是刚性的，碰撞时形状不变。要「压扁」必须走形变路线。

实测两条路线对比 [实测]：

| 路线 | 结果 |
|---|---|
| 纯刚体 | 球从 z=5 落到 z=0.5 静止（f20→f40），形状始终是球 [实测] |
| 软体 + 地面 Collision | 386 顶点的立方体：静置高度 **1.007** → 落地瞬间 **0.53** → 回弹到 **0.666** [实测] |

**软体配方（实测可跑）** [实测]：

```python
# 地面必须有 Collision 修改器，否则物体会直接穿过去
cm = floor.modifiers.new("Collision", "COLLISION")
cm.settings.thickness_outer = 0.02

# 立方体先细分（软体靠顶点形变，顶点太少压不出形状）
bpy.ops.object.modifier_add(type="SUBSURF")
cube.modifiers["Subdivision"].levels = 3
bpy.ops.object.modifier_apply(modifier="Subdivision")     # 实测 386 顶点

sb = cube.modifiers.new("SoftBody", "SOFT_BODY")
st = sb.settings
st.use_goal = False          # 不要目标形状 = 自由落体
st.mass = 0.5
st.friction = 0.9
st.bend = 0.8                # 抗弯刚度：越大越硬
st.plastic = 0               # ⚠️ 必须是 int，写 0.0 会 TypeError
st.ball_stiff = 10.0
st.ball_damp = 0.5
st.use_edges = True
```

实测形变时间线 [实测]（`height` = 局部 z 极差，静置 = 1.007）：

| 帧 | 高度 | 状态 |
|---|---|---|
| 1 | 1.007 | 下落中 |
| 6 | 1.007 | 下落中 |
| 10 | 1.007 | 下落中 |
| 14 | 1.007 | 即将触地 |
| **20** | **0.53** | **压扁（压缩 47%）** |
| 30 | 0.666 | 回弹中 |

**踩过的坑 [实测]**：第一版忘了给地面加 Collision 修改器，软体直接穿过地板掉到 `min_z = -2.325`。**「软体穿地」几乎总是因为地面没有 Collision 修改器。**

**「晃几下才停」= 关闭/收紧休眠** [实测]：
```
use_deactivation          = False      # 出厂 False = 永不自动停
deactivate_linear_velocity  = 0.4
deactivate_angular_velocity = 0.5
```
要「晃几下**才**停」：`use_deactivation = True` 并把阈值调到刚好在晃完后触发（0.2–0.5）；要「永远停不下来」就保持 `False`。

**「回弹」= `restitution`** [实测]：出厂 **0.0**（完全不弹）。要弹起来必须显式设 0.4–0.7。球从 z=5 落到静止用了约 40 帧（restitution=0.6）。[实测]

**MG 动画的现实选择 [归纳]**：软体求解慢且难调。10 秒 MG 动画里，「压扁」用**手动 squash & stretch 关键帧**更可控——在刚体落地的那一帧插一个缩放关键帧（z 压到 0.6、x/y 放大到 1.2），2–3 帧内恢复。经典动画原理，不需要解算器，且逐帧自查容易。软体留给「真的要真实形变」的镜头。

### 4.2 「挤开周围物体」

纯刚体即可。实测场景 [实测]：49 颗弹珠（半径 0.25、间距 0.6、`mass=0.2`、`restitution=0.3`）排成 7×7，中间砸下一个 `mass=8.0` 的方块。

结果 [实测]：
- 方块静止在 **z = 0.7**（方块边长 1.4，正好落地）
- 弹珠最大径向距离从初始 **2.546** 变成 **5.962**
- 49 颗全部位移

```python
proto = ...                                   # 一颗弹珠
bpy.ops.rigidbody.object_add()
proto.rigid_body.type = "ACTIVE"
proto.rigid_body.mass = 0.2
proto.rigid_body.restitution = 0.3
for i in range(-3, 4):
    for j in range(-3, 4):
        o = proto.copy(); o.data = proto.data          # 共享 mesh
        o.location = (i*0.6, j*0.6, 0.25)
        scene.collection.objects.link(o)
```

**要点 [归纳]**：
- 弹珠必须各自是 `ACTIVE` 刚体；`PASSIVE` 的会被穿过。
- 方块 `mass` 要显著大于弹珠（8.0 vs 0.2 = 40×），否则砸不出「挤开」的效果。
- 逐帧 `frame_set()` 让求解器推进；`bpy.ops.ptcache.bake_all(bake=True)` 也可（实测 0.08 s / 90 帧）[实测]。

### 4.3 「一大片一样的小物体像波浪一起起伏」

**脚本驱动 sine（推荐）** [实测可跑]：

```python
import math
N = 12
for i in range(N):
    for j in range(N):
        o = proto.copy(); o.data = proto.data
        o.location = ((i - N/2)*0.5, (j - N/2)*0.5, 0)
        scene.collection.objects.link(o)
        for f in range(1, 61, 5):
            phase = i*0.45 + j*0.45
            z = 0.35*math.sin(2*math.pi*(f/60.0)*1.5 - phase) + 0.35
            o.location.z = z
            o.keyframe_insert(data_path="location", frame=f)
```

实测：144 个对象，0.04 s 建完。[实测]

- **相位差 `phase = i*a + j*b` 就是「波浪」**：同相位 = 整体上下（不是波浪），相位随位置线性增长 = 波纹。
- 相邻实例相位差建议 ≤ 0.5 rad，太大就看不出连续波。
- 共享 mesh data（`o.data = proto.data`）是关键——否则 144 份几何。
- 关键帧不必每帧插：实测每 5 帧一个，贝塞尔插值自动补出平滑正弦。

**Geometry Nodes 备选**：`GeometryNodeInstanceOnPoints` + `GeometryNodeSetPosition`（用 Position 的 x/y 算相位偏移）。本机节点均存在 [实测]，但要用代码搭节点图，且实测 `GeometryNodeMath` / `GeometryNodeSine` 类名不存在（数学节点是 `ShaderNodeMath`，Sine 是其 operation）[实测]。**agent 优先用脚本驱动路线。**

---

## 5. agent 工作流

### 5.1 工具形态对照

| 形态 | 代表 | 通信方式 | 适合 |
|---|---|---|---|
| **MCP 桥**（活会话） | `ahujasid/mcp-for-blender`（原 `blender-mcp`，**30,867★**）[实测: GitHub API] | 插件在 Blender 内起 socket 服务（默认 `localhost:9876`），MCP server 转发 | 交互式建模、来回改、看反馈 |
| **MCP 桥**（开源模型） | `dhakalnirajan/blender-open-mcp`（120★）[实测] | 同样 socket（`localhost:9876`）+ 可切 Ollama/LM Studio/OpenAI 兼容后端 | 全本地、模型可换 |
| **无头脚本** | `blender -b --python` | 一次性进程 | **批量渲染、CI、可复现产物** |
| **库化管线** | `DLR-RM/BlenderProc` | `blenderproc run script.py` | 合成数据集（RGB/深度/法线/分割） |

### 5.2 blender-mcp 的 9 个工具（对 agent 工作流的映射）

README 实测摘录 [史料: `ahujasid/mcp-for-blender` README]：

| 工具 | 作用 | 对应 15 卡流程的哪一步 |
|---|---|---|
| `execute_blender_code` | 在活的 Blender 里跑 Python | 建场景 / 改参数 |
| **`look`** | 从 `viewport` / `camera` / **`angles`**（自动取景多视图拼图）/ **`frames`**（动画条）看结果，可切 `solid`/`material`/`rendered`/`wireframe`/`xray` | **「先出 6 张关键帧给我看」+「逐帧自查」** |
| `get_scene_info` | 一行一个对象的紧凑场景摘要，可 `root`/`query` 下钻 | 自查场景状态 |
| `generate_3d` | Tripo / Hunyuan3D / Hyper3D Rodin 生成并导入 | 补模型 |
| `search_assets` / `import_asset` | Poly Haven（HDRI/贴图/模型，CC0）、Sketchfab、Poly Pizza | **金属「映出周围」需要的 HDRI** |
| `get_addon_status` | Blender 版本、插件版本、开关状态 | 环境自查 |
| `disable_telemetry` / `record_trajectory_feedback` | 数据收集控制 | — |

**关键发现 [归纳]**：`look` 的 `angles`（多视图拼图）和 `frames`（动画条）**就是内置的 contact sheet 自查**——15 卡要求的「先出 6 关键帧」和「逐帧自查」在 blender-mcp 里是一条工具调用，不需要自己写拼图代码。

**安装要点** [史料]：
```bash
# 一键（Windows PowerShell）
powershell -ExecutionPolicy ByPass -c "irm https://www.mcp-for-blender.com/install.ps1 | iex"
# 或手动
uvx mcp-for-blender install-addon      # 装 Blender 插件
# 客户端注册
claude mcp add blender uvx mcp-for-blender
codex mcp add blender -- uvx mcp-for-blender
```
- 前置：Blender ≥ 3.0、Python ≥ 3.10、`uv`（**必须用官方安装器，不要 `pip install uv`**）。
- 环境变量：`BLENDER_HOST`（默认 `localhost`）、`BLENDER_PORT`（默认 `9876`）、`BLENDER_MCP_SAFE_MODE=1`（运行前校验脚本，拦文件/网络/子进程操作）。
- **⚠️ 安全**：README 原话「the addon's socket server has **no authentication or encryption**, so anyone who can reach that port can run Python inside Blender」。**保持 `localhost`，不要对公网开放。**[史料]
- 多实例：`--port 9877` 配第二个 MCP 条目，每个实例在插件面板里设不同端口。

### 5.3 「6 关键帧 → 动画 → 自查」的落地

15 卡的骨架纪律是**三段不许合并** [史料: `cards/structure.md`]。落到 Blender 上：

**第 1 段 · 6 张关键帧**（低成本早期检查点）

```python
KEY_FRAMES = [1, 30, 60, 90, 120, 150]        # 10 秒 300 帧里取 6 个
# 只渲这 6 帧，低采样、半分辨率
scene.render.resolution_percentage = 50
scene.eevee.taa_render_samples = 8
for f in KEY_FRAMES:
    scene.frame_set(f)
    scene.render.filepath = os.path.join(OUT, "key_%04d" % f)
    bpy.ops.render.render(write_still=True)
```

实测：320×180 渲 10 帧 PNG 序列 **2.04 s** [实测]；480×270 单帧 < 1 s [实测]。**6 张关键帧的成本可忽略——没有理由跳过。**

**第 2 段 · 做动画**：设 `frame_start/frame_end`，`render(animation=True)` 出 PNG 序列。

**第 3 段 · 逐帧自查**：见 §5.4。

**给 agent 的提示词骨架（英文）[归纳]**：

```
Build a 10-second 3D motion-graphics animation in Blender via Python
(1920x1080, 30 fps), rendered headless with EEVEE.
Work in three separate phases and DO NOT merge them:
  1. Render 6 key frames at half resolution and show them to me first.
  2. Only after I approve, render the full 300-frame PNG sequence.
  3. Then run a per-frame self-check and report a contact sheet.
Self-check must be mechanical, not descriptive: report frame count, resolution,
fps, mean/percentile pixel luminance per frame, and flag any frame whose
luminance differs from its neighbours by more than N%.
Save frames as PNG; assemble with ffmpeg (-framerate 30 before -i).
```

### 5.4 contact sheet 自查（已实测可跑）

**不需要 PIL**（实测本机 Blender 内置 Python **没有 PIL**）[实测]。用 `numpy` + `bpy.data.images`：

```python
import numpy as np, bpy, os

def contact_sheet(frame_dir, out_png, cols=5, max_frames=None):
    files = sorted(f for f in os.listdir(frame_dir) if f.endswith(".png"))
    if max_frames: files = files[:max_frames]
    tiles = []
    for fn in files:
        im = bpy.data.images.load(os.path.join(frame_dir, fn))
        a = np.empty(len(im.pixels), dtype=np.float32)
        im.pixels.foreach_get(a)                       # 比 im.pixels[:] 快得多
        tiles.append(a.reshape(im.size[1], im.size[0], im.channels))
        bpy.data.images.remove(im)
    h, w, c = tiles[0].shape
    rows = (len(tiles) + cols - 1) // cols
    sheet = np.zeros((rows*h, cols*w, 4), dtype=np.float32)
    for i, a in enumerate(tiles):
        r, cc = divmod(i, cols)
        sheet[r*h:(r+1)*h, cc*w:(cc+1)*w, :] = a
    out = bpy.data.images.new("sheet", width=cols*w, height=rows*h, alpha=True)
    out.pixels.foreach_set(sheet.ravel())
    out.filepath_raw = out_png
    out.file_format = "PNG"
    out.save()
```

实测：6 帧 320×180 → 960×360 拼图，106,183 字节，0.05 s。[实测]

**自查指标（可机械计算）[归纳]**：

| 检查 | 算法 | 通过条件 |
|---|---|---|
| 帧数/分辨率/帧率 | `len(files)`、`im.size`、`scene.render.fps` | == 300 / (1920,1080) / 30 |
| 全黑/全白帧 | 每帧 `a.mean()` | 不在 [0.001, 0.999] 之外 |
| 帧间跳变 | `abs(mean[i] - mean[i-1])` | 无孤立尖峰（> 3× 中位数） |
| 色数上限 | 量化色相直方图 | 符合画风段的色数约束 |
| 运动模糊生效 | 开/关同一帧的像素差 | > 0（实测 max 0.647） |
| 结尾文案出现 | 末帧 OCR 或像素模板匹配 | 命中 |

**外部工具备选 [归纳]**：
- `ffmpeg` 直接拼 contact sheet：
  ```bash
  ffmpeg -y -i "f_%04d.png" -vf "select='not(mod(n,10))',scale=320:180,tile=5x6" -frames:v 1 sheet.png
  ```
- ImageMagick `montage`（本机未验证是否安装）[UNVERIFIED]

### 5.5 无头 agent 的完整闭环

```
写脚本 (bpy)
   ↓
blender -b --factory-startup --python build.py        ← 语法/API 错误在这里暴露
   ↓
渲 6 张关键帧 → contact sheet → 给 Owner/自己看
   ↓  不通过 → 改脚本 → 回到上一步
渲 PNG 序列 (animation=True)
   ↓
逐帧自查（帧数/亮度/跳变/像素差）
   ↓  不通过 → 定位帧号 → 改 → 重渲该区间
ffmpeg 合成 mp4 (+ 音轨)
   ↓
交付
```

**本机实测的典型耗时 [实测]**（分母 = 1920×1080 EEVEE 64 TAA 采样的玻璃球+金属块+橡胶地+面积光+DOF 场景）：

| 环节 | 耗时 |
|---|---|
| Blender 启动 + 建场 | 1.1 s |
| 单帧 1080p EEVEE | 3.53 s |
| 单帧 1080p Cycles CPU 64spp + 降噪 | 27.1 s |
| 10 帧 320×180 EEVEE 4spp 序列 | 2.04 s |
| 6 帧 contact sheet | 0.05 s |

按 EEVEE 3.53 s/帧估，300 帧全片 ≈ **17.7 分钟**。[推测：线性外推，实际帧间复杂度不同会偏离]

---

## 6. 现成脚本 / repo 清单

全部 URL 于 2026-10-15 实测可达（HTTP 200 或 GitHub API 返回条目）[实测]。

| # | 名称 | URL | 用途 |
|---|---|---|---|
| 1 | **ahujasid/mcp-for-blender**（原 `blender-mcp`，30,867★） | https://github.com/ahujasid/mcp-for-blender | 最主流的 Blender↔LLM 桥。9 个工具，`execute_blender_code` + `look`（多视图/动画条）就是「关键帧→动画→自查」的现成实现。含 Poly Haven/Sketchfab/Poly Pizza 资产导入。 |
| 2 | **dhakalnirajan/blender-open-mcp**（120★） | https://github.com/dhakalnirajan/blender-open-mcp | 开源权重版 MCP 桥：Ollama / LM Studio / llama.cpp / OpenAI 兼容后端，运行时可切。全本地路线首选。 |
| 3 | **DLR-RM/BlenderProc** | https://github.com/DLR-RM/BlenderProc | 程序化 Blender 管线（`blenderproc run`）：物体摆放/物理/材质/灯光/相机采样，输出 RGB+深度+法线+分割。photorealistic 合成数据的工业级参考。 |
| 4 | **blender/blender** | https://github.com/blender/blender | 官方源码。查 API 变更（如 5.2 的 slotted action、`compositing_node_group`）的第一手位置。 |
| 5 | **blender/blender-addons** | https://github.com/blender/blender-addons | 官方随附插件源码。学「Blender 自己怎么写 bpy」的最短路径。 |
| 6 | **uhlik/bpy**（1,086★） | https://github.com/uhlik/bpy | 大量 bpy 脚本集合。可当模式库抄写法。 |
| 7 | **carson-katri/geometry-script**（342★） | https://github.com/carson-katri/geometry-script | 用 Python 写 Geometry Nodes 的 API 层。做「一大片小球波浪」的 GN 路线的脚手架。 |
| 8 | **FreedomIntelligence/BlenderLLM**（309★） | https://github.com/FreedomIntelligence/BlenderLLM | 专门生成 Blender/CAD 脚本的 LLM。研究「模型怎么学 bpy」的对照物。 |
| 9 | **TylerGubala/bpy-build**（41★） | https://github.com/TylerGubala/bpy-build | 把 Blender 编成 Python 模块（`import bpy` 脱离 Blender 进程）。CI / 服务器批量渲染路线。 |
| 10 | **FFmpeg/FFmpeg** | https://github.com/FFmpeg/FFmpeg | 帧序列→视频。本机已装 n9.0.1。 |
| 11 | **imageio/imageio-ffmpeg** | https://github.com/imageio/imageio-ffmpeg | pip 可装的 ffmpeg 轮子，免系统依赖。Python 侧合成视频的轻量路线。 |
| 12 | **ImageMagick/ImageMagick** | https://github.com/ImageMagick/ImageMagick | `montage` 拼 contact sheet。§5.4 的 Blender 内方案之外的备选。 |
| 13 | **Poly-Haven/polyhaven.com** | https://github.com/Poly-Haven/polyhaven.com | ~2,400 个 CC0 HDRI/贴图/模型，无需 API key。金属「映出周围」的环境光首选。 |
| 14 | **Moo-Ack-Productions/MCprep**（386★） | https://github.com/Moo-Ack-Productions/MCprep | 一个成熟的大型 bpy 插件，含节点/世界/实例化用法，可作代码组织参考。 |

**官方文档入口**（同样实测可达）[实测]：

| 文档 | URL |
|---|---|
| 命令行渲染 | https://docs.blender.org/manual/en/latest/advanced/command_line/render.html |
| 命令行参数全表 | https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html |
| 刚体 | https://docs.blender.org/manual/en/latest/physics/rigid_body/index.html |
| 软体 | https://docs.blender.org/manual/en/latest/physics/soft_body/index.html |
| 相机（含 DOF） | https://docs.blender.org/manual/en/latest/render/cameras.html |
| EEVEE | https://docs.blender.org/manual/en/latest/render/eevee/index.html |
| Cycles | https://docs.blender.org/manual/en/latest/render/cycles/index.html |
| `bpy.ops.rigidbody` API | https://docs.blender.org/api/current/bpy.ops.rigidbody.html |
| `bpy.types.Camera` API | https://docs.blender.org/api/current/bpy.types.Camera.html |

> 未找到（已查）：Blender 官方手册的 GitHub 镜像（`github.com/blender/blender-manual` → 404）。手册源码在 `projects.blender.org/blender/blender-manual`（该站对脚本请求返回 403，浏览器可开）。[实测]

---

## 7. 本机环境实测 [实测 2026-10-15]

### 7.1 Blender

```
where blender
→ INFO: Could not find files for the given pattern(s).        ← 不在 PATH 上
```

**已装**，但不在 PATH，需用绝对路径：

```
D:\Software\Blender Foundation\Blender 5.2\blender.exe
```

`"D:/Software/Blender Foundation/Blender 5.2/blender.exe" --version` 原样输出：

```
Blender 5.2.1 LTS
	build date: 2026-08-25
	build time: 02:38:20
	build commit date: 2026-08-24
	build commit time: 16:50
	build hash: 9e2066aef7ef
	build branch: blender-v5.2-release
	build platform: Windows
	build type: Release
```

| 项 | 实测值 |
|---|---|
| 版本 | **Blender 5.2.1 LTS** |
| 构建日期 | 2026-08-25 |
| 安装目录 | `D:\Software\Blender Foundation\Blender 5.2\` |
| 可执行文件 | `blender.exe`（另有 `blender-launcher.exe`） |
| 内置 Python | **3.13.13** |
| `where blender` | 找不到（**不在 PATH**） |
| 用户数据目录 | `C:\Users\dwgx1\AppData\Roaming\Blender Foundation\` 与 `...\Local\Blender Foundation\` 均存在 |
| 默认引擎 | `BLENDER_EEVEE` |
| 可用引擎 | EEVEE（默认）、**Cycles**（插件 `(True, True)`，赋值成功）、Workbench |
| 默认分辨率/帧率 | 1920×1080 / **24 fps**（01 卡要 30，需显式改） |
| 色彩管理 | view transform 默认 **AgX**，display device sRGB |
| 内置模块 | numpy ✓ · requests ✓ · bmesh ✓ · gpu ✓ · mathutils ✓ · **PIL ✗（ModuleNotFoundError）** |
| 物理能力 | 刚体 ✓ · 软体 ✓ · 布料 ✓ · 流体 ✓ · 粒子 ✓ · Geometry Nodes ✓ |

**GPU / Cycles 设备**（`prefs.refresh_devices()` 后）[实测]：

```
compute_device_type = NONE          ← 默认，需显式设 CUDA/OPTIX 才走 GPU
CUDA    NVIDIA GeForce RTX 5070 Ti Laptop GPU   use=True
OPTIX   NVIDIA GeForce RTX 5070 Ti Laptop GPU   use=True
CPU     Intel Core Ultra 9 275HX                use=False
ONEAPI  Intel(R) Graphics                       use=True
```

**渲染实测**（场景 = 玻璃球 + 金属方块 + 橡胶地面 + 面积光 + DOF，1920×1080）[实测]：

| 引擎 | 设置 | 单帧耗时 | 产物 |
|---|---|---|---|
| EEVEE | 64 TAA samples | **3.53 s** | PNG 1,675,668 字节 |
| Cycles | CPU 64 spp + 降噪 | **27.1 s** | PNG 1,824,829 字节 |

**视频输出实测** [实测]：640×360 EEVEE，30 帧 → `_video_test.mp4`，**22,706 字节，3.63 s**（须先设 `image_settings.media_type="VIDEO"`）。

**⚠️ 本机 Blender 5.2 的三处 API 变更**（照抄旧教程会炸）[实测]：

| 旧写法 | 5.2 现状 | 替代 |
|---|---|---|
| `action.fcurves` | **已删除**（`AttributeError`） | `action.layers[0].strips[0].channelbags[0].fcurves` |
| `scene.node_tree` | **已删除**（`AttributeError`） | `scene.compositing_node_group` |
| `scene.use_nodes` | 弃用，将在 6.0 移除 | 同上 |
| `image_settings.file_format = "FFMPEG"` | 需先设 `media_type` | 先 `image_settings.media_type = "VIDEO"` |
| `bpy.ops.rigidbody.bake_to_keyframes()` | **无头下必失败**（poll context） | 手动逐帧 `frame_set` + `matrix_world` + `keyframe_insert` |

### 7.2 ffmpeg

```
where ffmpeg        →  D:\Software\ffmpeg\bin\ffmpeg.exe        ← 在 PATH 上
ffmpeg -version     →  ffmpeg version n9.0.1-11-ge47273f4d9-20260828
                       built with gcc 15.2.0 (crosstool-NG 1.28.0.23_185f348)
```

配置含 `--enable-gpl --enable-libx264`（H.264 可用）。可直接用 §1.5 的合成命令。[实测]

### 7.3 探针脚本（可复跑）

同目录下留了 10 个探针，全部是「跑一遍就知道本机 Blender 能不能做某件事」：

| 文件 | 测什么 |
|---|---|
| `_probe_api.py` | 引擎/模块/修改器/物理能力总览 |
| `_probe2.py` | Cycles 插件、运动模糊、DOF、物理 ops、ffmpeg 设置、色彩管理、GN、灯光、BSDF 输入名 |
| `_probe3.py` | **真渲染**：EEVEE vs Cycles 1080p 计时、GPU 设备、5.2 合成器 API |
| `_probe4.py` | build options、ffmpeg 输出路径、刚体仿真+烘焙、图像 numpy API |
| `_probe5.py` | **slotted action API**、物理手动烘焙、PNG 序列、contact sheet |
| `_probe6.py` | `media_type` → FFMPEG → 真 mp4、144 实例波浪、GN 节点 |
| `_probe7.py` | 刚体/灯/相机/EEVEE 出厂默认值、运动模糊像素证据（第一版，失败）、软体 |
| `_probe8.py` | 运动模糊（修正版）、玻璃折射矩阵、软体压扁（第一版，失败）、刚体挤开 |
| `_probe9.py` | 材质 EEVEE 属性、折射开关矩阵（结论版）、软体压扁（修正版）、阴影梯度（指标有误） |
| `_probe10.py` | 半影宽度 vs 灯 size（正确指标）、橡胶 SSS 像素证据 |

跑法：
```bash
cd "D:/Project/Designers_Brain/knowledge/agent-art/blender"
"D:/Software/Blender Foundation/Blender 5.2/blender.exe" --background --python _probe10.py
cat _probe10_out.json
```

### 7.4 未装 / 未验证

- **Blender 不在 PATH**：每次调用写全路径，或自己把 `D:\Software\Blender Foundation\Blender 5.2\` 加进 PATH（本文不代为修改环境变量）。
- **uv 未验证是否安装**（blender-mcp 的前置）。[UNVERIFIED]
- **ImageMagick 未验证是否安装**（`montage` 备选路线）。[UNVERIFIED]
- **Blender 5.2 之后的 API 稳定性未知**：本文所有 API 结论只对 5.2.1 负责。[推测]

**若要在别的机器上装 Blender**（本机已装，此节供迁移参考）[史料/归纳]：

| 方式 | 命令 | 说明 |
|---|---|---|
| winget | `winget install BlenderFoundation.Blender` | 官方包，版本随仓库 |
| 官网 | https://www.blender.org/download/ | 可选 LTS 版本；Windows 有 installer / portable zip 两种 |
| Steam / Microsoft Store | — | 自动更新，但路径不固定，脚本里不好写死 |

装完用 `blender --version` 确认，再决定要不要加 PATH。

---

## 自审

### A · 早产出

- 边测边落盘：10 个探针脚本 + 各自的 `_probeN_out.json` 原始输出全部留在同目录，任何人可复跑复现本文每个数字。
- 本文档本身在探针跑完后一次写成，未占用「先写骨架」的额度（探针即骨架）。

### B · 反驳（挑 5 条最强结论逐条试推翻）

| # | 结论 | 反驳尝试 | 判定 |
|---|---|---|---|
| 1 | 「EEVEE 1080p 单帧 3.53 s」 | 换个更重的场景会不会翻几倍？→ 承认：3.53 s 只对这个场景成立。已把场景成分写进正文（玻璃球+金属块+橡胶地+面积光+DOF，64 TAA）。也试了 Cycles 同场景 27.1 s 作为对照。 | **WEAKENED**（数字保留但必须带分母，已带） |
| 2 | 「EEVEE 玻璃折射要两个开关都开」 | 只开一个是不是也有微弱效果？→ 实测数据：单开 0.0004 / 0.0017，双开 0.034（**20–80 倍**）。单开≈噪声级。 | **CONFIRMED** |
| 3 | 「软体压扁 1.007 → 0.53」 | 会不会是我的测量口径错（读的是局部坐标）？→ 确认读的是 `to_mesh()` 的**局部** z，所以绝对值带物体位移偏移；但 **高度差（max_z - min_z）与坐标系无关**，1.007 → 0.53 的压缩是真实的。已在正文标注。 | **CONFIRMED**（口径已澄清） |
| 4 | 「运动模糊生效」 | 第一版测试得到 `mean_abs_pixel_diff = 0.0`、两次渲染字节数完全相同 → 差点判成「EEVEE 不支持」。重查发现球移出了取景框。修正版（球在画面中央）得到 max 像素差 0.647。 | **OVERTURNED → 重建**（第一版结论「不生效」已废弃，正文只留修正版，并把翻车过程写进 §3.7） |
| 5 | 「灯 size 越大阴影越软」 | 第一版用「平均梯度」当指标，得到**反直觉结果**（size 越大梯度越大）。重查发现指标测的是「梯度总量」不是「边缘锐度」。换成半影宽度（10%–90% 过渡带像素数）后：0.1 → 3 px、2.0 → 235 px，符合物理。 | **OVERTURNED → 重建**（错误指标已废弃，正文用半影宽度） |
| 6 | 「Cycles 可用」 | 静态引擎枚举只列出 `BLENDER_EEVEE`，看起来像「没装 Cycles」。→ 试赋值 `engine="CYCLES"` 成功 + `addon_utils.check("cycles") == (True, True)` + 真渲出 27.1 s 的结果。**静态枚举会骗人。** | **CONFIRMED** |

### C · 机械验证

检查器：数 `sources.md` 的 URL 条数 + 逐条 HTTP 状态码。

（见 `sources.md` 末尾「机械验证」节，原样粘贴输出。）

另外本文档内部数字的机械核对：

```bash
cd "D:/Project/Designers_Brain/knowledge/agent-art/blender"
ls _probe*.py | wc -l
ls _probe*_out.json | wc -l
```

输出（原样）：
```
10
10
```

**10 个探针脚本，10 份原始 JSON 输出**（`_probe_api.py` → `_probe_api_out.json`，其余 `_probeN.py` → `_probeN_out.json`，N=2..10）。

3 条来源 URL 的 `read` 直读验证（含原样输出）见 `sources.md`「机械验证」§2。

### D · 小结（≤14 行）

- **已确立**：本机 Blender 5.2.1 LTS 在 `D:\Software\Blender Foundation\Blender 5.2\`，不在 PATH；无头 EEVEE 1080p 单帧 3.53 s、Cycles CPU 27.1 s；RTX 5070 Ti 的 CUDA/OptiX 已识别。
- **已确立**：01 卡六项要求全部有确定实现路径，其中五项做了像素级验证（折射 0.034 / SSS 0.0097 / 运动模糊 max 0.647 / 半影 3→235 px / 压扁 1.007→0.53 / 挤开 2.55→5.96）。
- **已确立**：Blender 5.2 五处会炸旧脚本的变更（`action.fcurves`、`scene.node_tree`、`media_type`、`bake_to_keyframes`、`GeometryNodeMath`）。
- **被推翻**：① 「EEVEE 不支持运动模糊」——是我把球移出画面导致的假阴性；② 「灯 size 越大阴影边缘梯度越大」——指标选错，改用半影宽度后反转。
- **被削弱**：渲染耗时数字只对「玻璃球+金属块+橡胶地+面积光+DOF」这一个场景成立，不是通用基准。
- **未知**：uv 是否已装；ImageMagick 是否已装；Cycles GPU 实际渲染速度（只验了设备被识别，没跑 OptiX 渲染计时）；软体解算在大规模（>100 个形变体）下的性能。
- **下一步**：① 跑一次完整的 300 帧 EEVEE 端到端（含音轨合成），拿到真实全片耗时；② 用 OptiX 重测 Cycles 单帧，决定是否给关键镜头换 Cycles；③ 把 §5.3 的英文提示词骨架做成 `templates/` 里的 Blender 卡。
- **我仍赌错的是什么**：我赌「面积光 size 是软阴影的唯一主开关」——但在有多个光源或 HDRI 环境光的场景里，阴影软硬由**所有**光源共同决定，size 只是可控的那一项；如果 01 卡的场景实际用 HDRI 打底，这条要重写。
