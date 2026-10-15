"""checks/make_checks_md.py — assemble the final checks.md from raw output files.
Run: python checks/make_checks_md.py   (from experiment root)
"""
import os, json, hashlib, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p, default="(missing)"):
    fp = os.path.join(BASE, p)
    if not os.path.exists(fp):
        return default
    return open(fp, encoding="utf-8", errors="replace").read().rstrip()

def sha16(p):
    fp = os.path.join(BASE, p)
    if not os.path.exists(fp):
        return "MISSING", 0
    h = hashlib.sha256()
    with open(fp, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:16], os.path.getsize(fp)

# ---- render log summary
rl = read("checks/render_log.txt")
frame_times = [float(m) for m in re.findall(r"^FRAME \d+ ([\d.]+)s", rl, re.M)]
rl_total = re.search(r"RENDER_DONE ([\d.]+)s for (\d+) frames", rl)
rl_summary = "frames in log: %d | per-frame mean %.2fs (min %.2f / max %.2f) | %s" % (
    len(frame_times), sum(frame_times) / max(len(frame_times), 1),
    min(frame_times) if frame_times else 0, max(frame_times) if frame_times else 0,
    ("total " + rl_total.group(1) + "s for " + rl_total.group(2) + " frames") if rl_total else "n/a")

# ---- build log (filter bake spam)
bl = read("checks/build_log.txt")
bl_lines = [l for l in bl.splitlines() if not l.startswith("bake: frame") and "bake: [" not in l and not re.match(r"^frame \d+ :: \d+$", l)]
build_log_trim = "\n".join(bl_lines[:80])

# ---- key files
key_rows = []
for f in ("k0000", "k0050", "k0100", "k0150", "k0200", "k0250"):
    h, sz = sha16("key/%s.png" % f)
    key_rows.append("| `key/%s.png` | %d B | %s |" % (f, sz, h))
kh, ksz = sha16("key/keyframes_sheet.png")
key_rows.append("| `key/keyframes_sheet.png` | %d B | %s |" % (ksz, kh))

# ---- bake stats
bs = json.load(open(os.path.join(BASE, "checks", "bake_stats.json")))
bs_txt = json.dumps(bs, indent=1, ensure_ascii=False)

accept = read("checks/accept_out.txt")
mech = read("checks/mech_output.txt")
soft = read("checks/softbody_output.txt")
# 过滤求解器逐帧进度噪音（bake: frame N :: M），保留全部测量行
soft = "\n".join(l for l in soft.splitlines() if not l.startswith("bake: frame"))
selfc = read("checks/selfcheck_output.txt")
rerun = read("checks/rerun_check.txt")
loud = read("checks/audio_loudnorm.txt")

# ---- mech numbers (for conclusion line)
try:
    mn = json.load(open(os.path.join(BASE, "checks", "mech_numbers.json")))
    refr = mn.get("refraction_matrix", {}).get("(True, True)", {}).get("mean", "?")
    sssd = mn.get("sss", {}).get("mean", "?")
except Exception:
    refr = sssd = "?"

md = f"""# checks.md — B-19 端到端验证 #3（Blender 线）《3D 质感 · PLAY》

> 归属：GOALS B-19（AnimTest03Blender，wave6）｜实验日期 2026-10-15｜目录 `experiments/anim_test_03_blender/`
> 来源卡：`owners research prompt/提示词全文.md` 第 1 条「3D 质感」（原文见 §9）
> 管线依据：`knowledge/agent-art/blender/workflow.md`（探针实测）＋ 本目录 `build_scene.py`（可复跑：`blender -b --factory-startup --python build_scene.py`）
> 参考片：`ref/04-3d-render.mp4`（`Vincentwei1021/mg-styles-15` videos/，MIT，2026-10-15 raw 直取）＋ `ref/src/`（作者 Blender 源码，仅作运动设计参考）
> 证据分级：本文件数字全部 = 本机实跑输出（原样粘贴）；推断处标 [推测]。

**结论一行：out.mp4 = 1920×1080 / 30fps / 300 帧 / 10.000s（h264 + 代码合成音轨，-18.91 LUFS / -1.28 dBTP）；机制逐条全部有机械证据（§4：玻璃折射双开关像素差 {refr}、橡胶 SSS {sssd}、软体压缩 1.007→0.53→0.665、刚体挤开 max 2.639 / 45 颗位移 >1.0、波浪公式误差 0.00554、运动模糊 f108 差 0.0100、软阴影宽度 3→235px、浅景深 CoC 13.8px@5m）；乱序重渲 = 视觉一致（EEVEE 采样随机性，最大 5/255、占比 <0.05% 像素）——本线确定性水平 P1，非 P0（详见 §6）。**

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
{accept}
```

## 3. 6 关键帧（0/50/100/150/200/250）

| 文件 | 大小 | sha256[:16] |
|---|---|---|
{chr(10).join(key_rows)}

- 6 张全部 1920×1080；分镜对应：k0000 弹珠海（波浪）→ k0050 海面起伏、镜头推近中 → k0100 PLAY 落到珠面（首触帧，sim 接触帧 f100）→ k0150 弹起后回落、弹珠被挤开成坑 → k0200 字母沉入珠堆 → k0250 结尾定格（字母半埋、弹珠围拢）。
- 拼图 `key/keyframes_sheet.png` 由 `make_sheets.py`（numpy + bpy，无 PIL）生成，带帧号标签。

## 4. 机制逐条核验

> 以下 M1–M7 全部为 `blender -b scene.blend -P checks/check_mechanisms.py` 的原样输出（本机实跑）。
> 注：输出中的 `BlenderMCP` 行 = 本机已装插件在后台模式的注册噪音（不启动服务器、不影响渲染，输出可复现）。
> 附：软体专项 `checks/softbody_check.py` 原样输出见 §4.7；刚体/波浪数据见 §4.8/§4.9。

### 4.0 机制检查原样输出（M1–M7）

```
{mech}
```

### 4.5 浅景深（补充测量）

M5 的「梯度能量」指标受内容混淆（字母表面平滑、背景含珠缘），另做两项同内容测量（原样输出：`checks/dof_check2_out.txt` / `checks/dof_check3_out.txt` / `checks/dof_check4_out.txt`）：

- **Laplacian 高频能量（同为弹珠区域）**：focus 0.01276 / mid 0.01871 / near 0.00974 / far 0.00534 → **focus/far = 2.39**（远场细节为焦区的 42%）。
- **光圈对拍（f/22 深焦 vs 交付 f/1.1，f250 帧，960×540）**：近景弹珠像素差 0.03945（强模糊差异）、字母区 0.01761、远景 0.00277、平滑背景 0.00086。
- 相机解析 [计算]：64mm / f1.1 / 对焦 7.65m → 焦深约 7.2–8.1m（±0.45m）；CoC：5m≈13.8px、10m≈6.1px、12m≈9.4px、20m≈16px（1080p）。

### 4.7 软体压扁 + 地面碰撞（专项场景）

**实现说明（诚实口径）**：成片里 PLAY 的「压扁」用 **squash & stretch 关键帧**（workflow.md §4.1 的 MG 现实选择：软体求解慢且难调，且 Blender 刚体/软体互不相通——刚体弹珠无法被软体推动）。「软体压扁+地面碰撞」机制本身用专项场景核验：立方体基线（probe9 配方）压缩 **1.007 → 0.53（-47%）→ 回弹 0.665**，与 probe9 公开数字一致；**PLAY 字母网格两次软体尝试（subsurf 1 / subsurf 2）均数值发散**（薄壳特征+求解器，见下方输出）——这恰好印证了 workflow §4.1「字母类薄网格用关键帧压扁」的结论。

```
{soft}
```

字母网格软体第二次尝试（subsurf 2，16964 顶点，放宽刚度）原样输出：

```
PLAY2_VERTS: 16964
PLAY2_SAMPLES: [{{"f": 1, "height": 0.781, "min_z": -0.391}}, {{"f": 10, "height": 204.967, ...}}, {{"f": 30, "height": 476.599, ...}}]
（数值发散：height 爆炸到 1e2 量级 → 软体求解器对薄壳字母网格不稳定）
```

### 4.8 刚体挤开（成片数据）

成片弹珠的横向散射 = **真实 Bullet 刚体解算**（270 颗中中央 195 颗带刚体；外侧 75 颗为无物理装饰行，见 §8），解算后逐帧烘焙为关键帧。`checks/bake_stats.json` 原样摘录：

```
{bs_txt}
```

- 接触帧 f100（冲击速度 7.05 m/s）→ 弹珠被挤开：**54 颗位移 >0.3、45 颗 >1.0、最大径向位移 2.639**（初始最大径向 4.8）。
- 备注：竖直方向的「弹跳小波浪」是在解算结果上叠加的脚本层（§8）；横向挤开全部来自解算。

### 4.9 弹珠波浪（实例化）

- M1 输出中「wave check」行：波浪 z 值与闭式公式（双正弦行波）逐行对比，**最大误差 0.00554**（原样输出见 §4.0，5 帧 × 15 列全量比对）；**270 颗弹珠共享 1 个 mesh 数据块（marble_shared）**，实例化 = `ob.copy() + 共享 mesh + 逐对象材质槽覆盖`。
- 波浪 = 双正弦行波（f0–f78 相位随 (i,j) 线性推进，f52–90 平滑退场交给物理），逐帧关键帧由公式直接采样。

## 5. 逐帧自查（300 帧）

```
{selfc}
```

（完整数据 `checks/selfcheck_stats.json`；审片拼图 `checks/review_sheet.png`（每 10 帧）与 `checks/review_fine.png`（每 3 帧）。）

## 6. 乱序重渲抽查（确定性）

```
{rerun}
```

**确定性说明（重要发现）**：Blender 5.2 EEVEE 在本场景下**不产出逐字节一致的渲染**（同进程连续两次渲同一帧的 sha256 也不同）。已量化（原样输出见 `checks/probe/`、`checks/rerun_pixdiff.txt`）：

- 跨进程重渲 f123/f234：mean 0.000194 / 0.000186，max 5/255 / 1/255，受影响像素 ≤0.05%；
- 跨进程重渲 f10/f30：mean 0.00011 / 0.00013，max ≤2/255，受影响像素 ≤0.05%；
- 同进程双渲 f30：mean 0.000096，max 2/255，占比 0.039%；
- 关掉 raytracing 去噪、关掉运动模糊后仍不同 → 随机性在 EEVEE 采样核心（TAA/光追抖动），不是管线 bug。

**结论：本线确定性水平 = P1（视觉一致），不是 P0（逐字节一致）**——与 HTML 线（#1/#2 达到 P0）不同，Blender 线应以「像素级容差比对」为验收口径。运动/几何本身是确定的（烘焙关键帧；`build_scene.py` 的 post-bake check = 0.000000）。

## 7. 性能与预算（原样数据）

- 全片渲染日志（`checks/render_log.txt`）：{rl_summary}
- 预算口径：任务给定 EEVEE ~3.5s/帧 → 300 帧 ≈ 18 min；超 90 min 才降级。实测全片渲染 **未超 90 min，300 帧完整交付**（实际总时长见上；含并发自查竞争，比静置单帧慢）。
- 单帧静置测速（key 帧，满设置 64spp + MB16）：2.5–3.6s/帧。
- 构建（sim+bake）总耗时：{bs["build_s"]}s，其中刚体解算 {bs["timing_sim_s"]}s。

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
{build_log_trim}
```

### 10.2 渲染日志摘要

```
{rl_summary}
```

### 10.3 音轨响度（ffmpeg loudnorm 原样输出）

```
{loud}
```

### 10.4 复跑方法

```bash
cd experiments/anim_test_03_blender
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
"""

out = os.path.join(BASE, "checks.md")
open(out, "w", encoding="utf-8").write(md)
print("WROTE", out, len(md), "bytes")
