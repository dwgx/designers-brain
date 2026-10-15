# Blender 线 · 来源清单（GOALS B-03）

> 归属：BlenderScript。配套产物：`workflow.md`。
> 全部 URL 于 **2026-10-15** 逐条实测（`curl -L -o /dev/null -w "%{http_code}"`，或 `read` 直读）；状态码与读法见文末「机械验证」节原样输出。
> 编号规则：`S-` = 外部来源；`L-` = 本机实测产物（本地路径，非 URL）。
> 证据分级沿用项目口径：`[自述]` 艺术家/作者原话 · `[史料]` 一手文档 · `[研究]` 分析 · `[归纳]` 我们总结 · `[推测]` 推断。

---

## A · 官方文档（Blender 5.2 LTS Manual / API）

| ID | URL | 用途 | 取用位置 |
|---|---|---|---|
| S-01 | https://docs.blender.org/manual/en/latest/advanced/command_line/render.html | 无头渲染命令。原话：「One advantage of using the command line is that we do not need a graphical display」「Arguments are executed in the order they are given!」「**Always** position `-f` or `-a` as the last arguments.」给出 `-b` / `-f` / `-a` / `-o` / `-F` / `-E` / `-s -e` / `-t` 的语义与大小写敏感提醒 | `workflow.md` §1.1、§1.2 |
| S-02 | https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html | 命令行参数全表（S-01 指向的完整清单） | `workflow.md` §1.2 |
| S-03 | https://docs.blender.org/manual/en/latest/physics/rigid_body/index.html | 刚体章节目录。确认结构：Introduction / Properties(settings·collisions·dynamics) / World / Constraints / Tips | `workflow.md` §2.6、§4.2 |
| S-04 | https://docs.blender.org/manual/en/latest/physics/rigid_body/properties/dynamics.html | 刚体动力学属性（`restitution` / `friction` / 阻尼 / 休眠）的语义 | `workflow.md` §4.1 |
| S-05 | https://docs.blender.org/manual/en/latest/physics/rigid_body/tips.html | 仿真稳定性、与其它仿真共存、缩放注意事项 | `workflow.md` §4.2 |
| S-06 | https://docs.blender.org/manual/en/latest/physics/soft_body/index.html | 软体章节目录。确认 Settings 含 Goal / Edges / Self Collision / Solver，Examples 含「A Bouncing Cube」 | `workflow.md` §2.6、§4.1 |
| S-07 | https://docs.blender.org/manual/en/latest/physics/soft_body/examples.html | 软体「A Bouncing Cube」示例——「掉下压扁」的官方最小案例 | `workflow.md` §4.1 |
| S-08 | https://docs.blender.org/manual/en/latest/render/cameras.html | 相机与景深。原话：「F-Stop ratio that defines the amount of blurring. **Lower values give a strong depth of field effect.**」「the minimum amount of blades to enable the bokeh effect is 3」；Focus Object / Focus Distance / Rotation / Ratio(anamorphic) | `workflow.md` §2.4、§3.6 |
| S-09 | https://docs.blender.org/manual/en/latest/render/eevee/index.html | EEVEE 渲染引擎总览 | `workflow.md` §1.3 |
| S-10 | https://docs.blender.org/manual/en/latest/render/eevee/render_settings/index.html | EEVEE 渲染设置（阴影 / 光线追踪 / 运动模糊所在的设置页） | `workflow.md` §1.3、§3.1、§3.7 |
| S-11 | https://docs.blender.org/manual/en/latest/render/cycles/index.html | Cycles 渲染引擎总览 | `workflow.md` §1.3 |
| S-12 | https://docs.blender.org/api/current/bpy.ops.rigidbody.html | `bpy.ops.rigidbody` API：`object_add` / `world_add` / `bake_to_keyframes` / `constraint_add` / `mass_calculate` | `workflow.md` §2.6、§4.2 |
| S-13 | https://docs.blender.org/api/current/bpy.types.Camera.html | `Camera` / `CameraDOFSettings` API 字段 | `workflow.md` §2.4、§3.6 |

## B · 官方源码 / 插件

| ID | URL | 用途 | 取用位置 |
|---|---|---|---|
| S-14 | https://github.com/blender/blender | Blender 官方源码。查 API 变更的第一手位置（如 5.2 的 slotted action、`compositing_node_group`） | `workflow.md` §6 #4 |
| S-15 | https://github.com/blender/blender-addons | 官方随附插件源码——学「Blender 自己怎么写 bpy」 | `workflow.md` §6 #5 |
| S-16 | https://projects.blender.org/blender/blender-manual | 手册源码仓库（非 GitHub）。**注**：脚本请求返回 403，浏览器可开 | `workflow.md` §6 未找到说明 |

## C · LLM ↔ Blender 桥（MCP）

| ID | URL | 用途 | 取用位置 |
|---|---|---|---|
| S-17 | https://github.com/ahujasid/mcp-for-blender | 最主流的 Blender↔LLM 桥（原 `blender-mcp`，**30,867★**，GitHub API 实测）。9 工具含 `execute_blender_code` / `look`（viewport·camera·**angles**·**frames**）/ `get_scene_info` / `search_assets` / `import_asset`。README 原话：socket 服务**无认证无加密**「anyone who can reach that port can run Python inside Blender」 | `workflow.md` §5.1、§5.2 |
| S-18 | https://github.com/ahujasid/blender-mcp | 旧仓库名（HTTP 200，指向 mcp-for-blender）。旧配置仍可用，`uvx blender-mcp` 照跑 | `workflow.md` §5.2 |
| S-19 | https://raw.githubusercontent.com/ahujasid/blender-mcp/main/README.md | README 原文（含安装三步、`BLENDER_HOST`/`BLENDER_PORT`/`BLENDER_MCP_SAFE_MODE` 环境变量表、Poly Haven CC0 说明、Poly Pizza 69% CC-BY 说明） | `workflow.md` §5.2 |
| S-20 | https://github.com/dhakalnirajan/blender-open-mcp | 开源权重版 MCP 桥（120★）：Ollama / LM Studio / llama.cpp / OpenAI 兼容后端，运行时可切。单文件 `addon.py` + FastMCP server，TCP 9876 | `workflow.md` §5.1 |
| S-21 | https://pypi.org/project/mcp-for-blender/ | PyPI 包（`uvx mcp-for-blender` 的安装源） | `workflow.md` §5.2 |
| S-22 | https://www.mcp-for-blender.com/ | 官网 / 一键安装脚本托管（`install.ps1` / `install.sh`） | `workflow.md` §5.2 |

## D · 管线 / 脚本库 / 工具

| ID | URL | 用途 | 取用位置 |
|---|---|---|---|
| S-23 | https://github.com/DLR-RM/BlenderProc | 程序化 Blender 管线（`blenderproc run script.py`）。物体摆放/物理/材质/灯光/相机采样，输出 RGB+深度+法线+分割，写 hdf5/COCO/BOP。photorealistic 合成数据的工业级参考 | `workflow.md` §5.1、§6 #3 |
| S-24 | https://github.com/uhlik/bpy | bpy 脚本集合（1,086★）——可当模式库抄写法 | `workflow.md` §6 #6 |
| S-25 | https://github.com/carson-katri/geometry-script | 用 Python 写 Geometry Nodes 的 API 层（342★）——「小球波浪」GN 路线的脚手架 | `workflow.md` §6 #7 |
| S-26 | https://github.com/FreedomIntelligence/BlenderLLM | 专生成 Blender/CAD 脚本的 LLM（309★）——研究「模型怎么学 bpy」的对照物 | `workflow.md` §6 #8 |
| S-27 | https://github.com/TylerGubala/bpy-build | 把 Blender 编成 Python 模块（`import bpy` 脱离 Blender 进程）——CI / 服务器批量渲染路线 | `workflow.md` §6 #9 |
| S-28 | https://github.com/Moo-Ack-Productions/MCprep | 成熟的大型 bpy 插件（386★），含节点/世界/实例化用法，可作代码组织参考 | `workflow.md` §6 #14 |
| S-29 | https://github.com/FFmpeg/FFmpeg | 帧序列→视频 | `workflow.md` §1.5、§6 #10 |
| S-30 | https://github.com/imageio/imageio-ffmpeg | pip 可装的 ffmpeg 轮子，免系统依赖 | `workflow.md` §6 #11 |
| S-31 | https://github.com/ImageMagick/ImageMagick | `montage` 拼 contact sheet（§5.4 备选路线） | `workflow.md` §6 #12 |
| S-32 | https://github.com/Poly-Haven/polyhaven.com | ~2,400 个 CC0 HDRI/贴图/模型。金属「映出周围」的环境光首选 | `workflow.md` §3.3、§6 #13 |
| S-33 | https://polyhaven.com/ | Poly Haven 站点本体（asset 源） | `workflow.md` §3.3 |
| S-34 | https://pypi.org/project/bpy/ | `bpy` 作为独立 PyPI 模块的发行页 | `workflow.md` §6 #9 |
| S-35 | https://www.blender.org/download/ | Blender 官方下载页（迁移安装用） | `workflow.md` §7.4 |

## E · 本机实测产物（非 URL，可复跑）

| ID | 路径 | 内容 |
|---|---|---|
| L-01 | `_probe_api.py` + `_probe_api_out.json` | 引擎 / 模块 / 修改器 / 物理能力总览 |
| L-02 | `_probe2.py` + `_probe2_out.json` | Cycles 插件、运动模糊、DOF、物理 ops、ffmpeg 设置、色彩管理、GN、灯光、Principled 输入名 |
| L-03 | `_probe3.py` + `_probe3_out.json` | **真渲染**：EEVEE vs Cycles 1080p 计时、GPU 设备、5.2 合成器 API |
| L-04 | `_probe4.py` + `_probe4_out.json` | build options、ffmpeg 输出路径、刚体仿真+烘焙、图像 numpy API |
| L-05 | `_probe5.py` + `_probe5_out.json` | **slotted action API**、物理手动烘焙、PNG 序列、contact sheet |
| L-06 | `_probe6.py` + `_probe6_out.json` | `media_type` → FFMPEG → 真 mp4、144 实例波浪、GN 节点 |
| L-07 | `_probe7.py` + `_probe7_out.json` | 出厂默认值（刚体/灯/相机/EEVEE）、运动模糊像素证据（**第一版失败**）、软体 |
| L-08 | `_probe8.py` + `_probe8_out.json` | 运动模糊（修正版）、玻璃折射矩阵、软体压扁（**第一版失败**）、刚体挤开 |
| L-09 | `_probe9.py` + `_probe9_out.json` | 材质 EEVEE 属性、折射开关矩阵（结论版）、软体压扁（修正版）、阴影梯度（**指标有误**） |
| L-10 | `_probe10.py` + `_probe10_out.json` | 半影宽度 vs 灯 size（正确指标）、橡胶 SSS 像素证据 |
| L-11 | `_render_eevee_.png` / `_render_cycles_.png` | 1080p 真渲染样张（玻璃球+金属块+橡胶地+面积光+DOF） |
| L-12 | `_video_test.mp4` | Blender 直出 mp4（22,706 字节，30 帧 640×360） |
| L-13 | `_contact_sheet.png` | 6 帧拼图（960×360，106,183 字节） |
| L-14 | `_seq2/` | PNG 帧序列（实测命名 `f_0001.png` … `f_0010.png`）。注：`_seq/` 不存在——probe4 的序列渲染因场景无相机而失败（`RuntimeError: Cannot render, no camera`），该步骤未产出文件 |
| L-15 | `_mb2_off.png` / `_mb2_on.png` | 运动模糊开/关对照帧（**修正版**，球在画面中央） |
| L-16 | `_pen_0.1.png` / `_pen_2.0.png` / `_pen_8.0.png` | 半影宽度对照帧 |
| L-17 | `_sss_sss_off.png` / `_sss_sss_on.png` | 橡胶次表面开/关对照帧 |
| L-18 | `_glass_rt_off.png` / `_glass_rt_on.png` | EEVEE 光线追踪开/关对照帧 |
| L-19 | `_mb_off.png` / `_mb_on.png` · `_shadow_0.25.png` / `_shadow_3.0.png` / `_shadow_12.0.png` · `_g2_False_False.png` / `_g2_False_True.png` / `_g2_True_False.png` / `_g2_True_True.png` | **被推翻的第一版证据**（保留以便复核推翻过程，结论已从正文删除）：`_mb_*` = 球移出取景框导致假阴性（像素差 0.0）；`_shadow_*` = 用「平均梯度」当软阴影指标得到反直觉结果；`_g2_*` = 折射开关四组合矩阵（probe9，结论版，正文采用的就是这组数字） |

---

## 覆盖度自查

| 车道需求 | 对应来源 |
|---|---|
| §1 无头渲染 | S-01 S-02 S-09 S-10 S-11 S-29 S-30 |
| §2 bpy 脚本结构 | S-12 S-13 S-14 S-15 S-24 S-28 |
| §3 01 卡「3D 质感」 | S-08 S-10 S-32 S-33 + L-03 L-09 L-10 L-11 L-15 L-16 L-17 L-18 |
| §4 物理细节 | S-03 S-04 S-05 S-06 S-07 S-12 + L-07 L-08 L-09 |
| §5 agent 工作流 | S-17 S-18 S-19 S-20 S-21 S-22 S-23 S-31 + L-05 L-06 L-13 |
| §6 repo 清单 | S-14 S-15 S-17 S-20 S-23 S-24 S-25 S-26 S-27 S-28 S-29 S-30 S-31 S-32（14 项，≥8 达标） |
| §7 本机实测 | S-35 + L-01…L-18 |

**缺口 / 未取到**：

- 未找到（已查）：Blender 官方手册的 GitHub 镜像。`https://github.com/blender/blender-manual` → **404**（实测）。手册源码实际在 `projects.blender.org/blender/blender-manual`（该站对脚本请求返回 **403**，浏览器可开）[实测]。
- 未找到（已查）：`https://docs.blender.org/manual/en/latest/physics/rigid_body/usage.html` → **404**。正确路径是 `introduction.html` / `properties/settings.html` / `world.html` / `tips.html`（实测）[实测]。
- 未找到（已查）：`https://docs.blender.org/manual/en/latest/render/output/video.html` → **404**。视频输出设置的实际页面路径本次未定位。
- 未验证：`github.com/princeton-vl/BlenderLLM` → **404**、`github.com/ZhiyuanChen/SceneCraft` → **404**、`github.com/blender/blender-developer-docs` → **404**（均为我最初猜的路径，实际地址见 S-26 与下条）。
- 未取到：`OrangeSodahub/SceneCraft`（245★，NeurIPS 2024 layout-guided 3D scene generation）——与「LLM agent 生成 Blender 代码」不是同一个项目，未纳入正文，避免混淆。
- **搜索通道限流**：本次 `web_search` 全 provider 限流（429 / bot 挑战），未使用。来源全部经 `read` 直读已知 URL + `bash curl` 状态码 + GitHub Search API 取得，不是内容缺口。

---

## 机械验证（原样粘贴）

### 1) 全量 URL 状态码

命令：
```bash
n=0; ok=0
while read -r u; do
  code=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 25 "$u" 2>/dev/null)
  n=$((n+1)); [ "$code" = "200" ] && ok=$((ok+1))
  printf '%s  %s\n' "$code" "$u"
done < urls.txt
echo "----"; echo "TOTAL=$n  HTTP200=$ok"
```

输出（原样，35 条）：
```
200  https://docs.blender.org/manual/en/latest/advanced/command_line/render.html
200  https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
200  https://docs.blender.org/manual/en/latest/physics/rigid_body/index.html
200  https://docs.blender.org/manual/en/latest/physics/rigid_body/properties/dynamics.html
200  https://docs.blender.org/manual/en/latest/physics/rigid_body/tips.html
200  https://docs.blender.org/manual/en/latest/physics/soft_body/index.html
200  https://docs.blender.org/manual/en/latest/physics/soft_body/examples.html
200  https://docs.blender.org/manual/en/latest/render/cameras.html
200  https://docs.blender.org/manual/en/latest/render/eevee/index.html
200  https://docs.blender.org/manual/en/latest/render/eevee/render_settings/index.html
200  https://docs.blender.org/manual/en/latest/render/cycles/index.html
200  https://docs.blender.org/api/current/bpy.ops.rigidbody.html
200  https://docs.blender.org/api/current/bpy.types.Camera.html
200  https://github.com/blender/blender
200  https://github.com/blender/blender-addons
403  https://projects.blender.org/blender/blender-manual
200  https://github.com/ahujasid/mcp-for-blender
200  https://github.com/ahujasid/blender-mcp
200  https://raw.githubusercontent.com/ahujasid/blender-mcp/main/README.md
200  https://github.com/dhakalnirajan/blender-open-mcp
200  https://pypi.org/project/mcp-for-blender/
200  https://www.mcp-for-blender.com/
200  https://github.com/DLR-RM/BlenderProc
200  https://github.com/uhlik/bpy
200  https://github.com/carson-katri/geometry-script
200  https://github.com/FreedomIntelligence/BlenderLLM
200  https://github.com/TylerGubala/bpy-build
200  https://github.com/Moo-Ack-Productions/MCprep
200  https://github.com/FFmpeg/FFmpeg
200  https://github.com/imageio/imageio-ffmpeg
200  https://github.com/ImageMagick/ImageMagick
200  https://github.com/Poly-Haven/polyhaven.com
200  https://polyhaven.com/
200  https://pypi.org/project/bpy/
200  https://www.blender.org/download/
----
TOTAL=35  HTTP200=34
```

**35 条中 34 条 HTTP 200；唯一非 200 是 `projects.blender.org/blender/blender-manual`（403）——该站对脚本请求一律 403，浏览器可开，已在正文 §6 与本节「缺口」注明。**

### 2) 抽 3 条 URL 用 `read` 直读验证

**验证 1 — S-01（命令行渲染手册）**

`read https://docs.blender.org/manual/en/latest/advanced/command_line/render.html`

原样输出（节选，含标题与关键原话）：
```
title: Rendering From The Command Line - Blender 5.2 LTS Manual
---
# Rendering From The Command Line
In some situations we want to increase the render speed,
access Blender remotely to render something or build scripts that use the command line.
One advantage of using the command line is that we do not need a graphical display
(no need for X server on Linux for example)
and consequently we can render via a remote shell (typically SSH).
Note
Arguments are executed in the order they are given!
...
**Always** position `-f` or `-a` as the last arguments.
```

**验证 2 — S-17（mcp-for-blender README，经 raw.githubusercontent 直读）**

`read https://raw.githubusercontent.com/ahujasid/blender-mcp/main/README.md`

原样输出（节选）：
```
# MCP for Blender
**Connect Blender to any LLM**
*formerly `blender-mcp` — the PyPI package is now [`mcp-for-blender`](https://pypi.org/project/mcp-for-blender/).*
**Disclaimer:** This is a third-party integration and not made by Blender
Prompt-assisted 3D modeling, scene creation, and manipulation — driven by AI.
```

**验证 3 — S-08（相机手册，DOF 节）**

`read https://docs.blender.org/manual/en/latest/render/cameras.html`

原样输出（节选）：
```
title: Cameras - Blender 5.2 LTS Manual
### Depth of Field
Real-world cameras transmit light through a lens that bends and focuses it onto the sensor.
...
F-Stop
F-Stop ratio that defines the amount of blurring.
Lower values give a strong depth of field effect.
Blades
Total number of polygonal blades used to alter the shape of the blurred objects
in the render, and render preview. As with the viewport, the minimum amount of
blades to enable the bokeh effect is 3, resulting in a triangular-shaped blur.
```

### 3) 条数

命令：
```bash
cd "D:/Project/Designers_Brain/research/agent-art/blender"
echo "S- rows: $(grep -c '^| S-' sources.md)"
echo "L- rows: $(grep -c '^| L-' sources.md)"
echo "unique URLs: $(grep -oE 'https?://[^ )|>]+' sources.md | sort -u | wc -l)"
echo "workflow sections: $(grep -cE '^## [0-9]\.' workflow.md)"
```

输出（原样）：
```
S- rows: 35
L- rows: 19
unique URLs: 41
workflow sections: 8
```

**S- 外部来源 35 条（要求 ≥15，达标）；L- 本机实测产物 19 条；sources.md 内去重 URL 41 个；workflow.md 顶层编号节 8 个（§0 一分钟结论 + §1–§7 要求的 7 节）。**
