"""checks/check_mechanisms.py — per-mechanism verification for anim_test_03.
Run: blender -b scene.blend -P checks/check_mechanisms.py  (capture stdout)
Writes checks/mech/*.png + prints raw numbers (pasted into checks.md).
"""
import bpy, os, math, json, time
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OD = os.path.join(BASE, "checks", "mech")
os.makedirs(OD, exist_ok=True)
sc = bpy.context.scene
R = {}
def log(*a):
    print(*a, flush=True)

def grab(path):
    im = bpy.data.images.load(path)
    a = np.empty(len(im.pixels), np.float32)
    im.pixels.foreach_get(a)
    w, h = im.size
    ch = im.channels
    bpy.data.images.remove(im)
    return a.reshape(h, w, ch)

def render(path, frame, pct=25, samples=16, mb=False, mb_steps=16):
    sc.render.resolution_percentage = pct
    sc.eevee.taa_render_samples = samples
    sc.render.use_motion_blur = mb
    sc.eevee.motion_blur_steps = mb_steps
    sc.frame_set(frame)
    sc.render.filepath = path
    t0 = time.time()
    bpy.ops.render.render(write_still=True)
    return grab(path), time.time() - t0

def diff(a, b):
    d = np.abs(a[..., :3] - b[..., :3])
    return {"mean": round(float(d.mean()), 6), "max": round(float(d.max()), 5),
            "frac_gt_002": round(float((d.max(axis=2) > 0.02).mean()), 5)}

# ---------------------------------------------------------------- M1 scene data
log("=== M1. scene data ===")
import re
marbles = [o for o in bpy.data.objects if re.match(r'^m\d+_\d+$', o.name)]
strays = [o for o in bpy.data.objects if o.name.startswith("stray")]
play = bpy.data.objects.get("PLAY")
meshes = {o.data.name for o in marbles}
rb_count = sum(1 for o in sc.objects if o.rigid_body is not None)
log("marbles:", len(marbles), "| unique meshes:", meshes, "| mesh users:", bpy.data.meshes["marble_shared"].users)
log("strays:", len(strays), "| PLAY:", play is not None, "| rigid bodies left:", rb_count, "| rb world:", sc.rigidbody_world)
log("lights:", sorted([o.name for o in sc.objects if o.type == 'LIGHT']))
R["marbles"] = len(marbles); R["unique_mesh"] = list(meshes); R["rb_left"] = rb_count

# wave: row j=8 z per frame vs formula
log("--- wave check (row j=8, z at f=0/10/20/30/40) ---")
def E(f): 
    u = min(max((f - 52) / (90 - 52), 0.0), 1.0)
    return 1.0 - u * u * (3 - 2 * u)
def wave_z(i, j, f):
    t = f / 30.0
    th1 = 2 * math.pi * 0.70 * t - (i * 0.46 + j * 0.18)
    th2 = 2 * math.pi * 0.50 * t - (i * 0.15 - j * 0.38)
    return 0.25 + E(f) * (0.32 * (0.5 + 0.5 * math.sin(th1)) + 0.14 * (0.5 + 0.5 * math.sin(th2)))
err_max = 0.0
for f in (0, 10, 20, 30, 40):
    row = []
    for i in range(15):
        o = bpy.data.objects["m%d_8" % i]
        fc = None
        for c in o.animation_data.action.layers[0].strips[0].channelbags[0].fcurves:
            if c.data_path == "location" and c.array_index == 2:
                fc = c
        z = fc.evaluate(f)
        row.append(z)
        err_max = max(err_max, abs(z - wave_z(i, 8, f)))
    log("f%02d:" % f, " ".join("%.3f" % z for z in row))
log("max |measured - formula| over rows:", round(err_max, 5))
R["wave_err_max"] = round(err_max, 5)

# keyframe counts
cb = bpy.data.objects["m0_0"].animation_data.action.layers[0].strips[0].channelbags[0]
nkeys = [len(fc.keyframe_points) for fc in cb.fcurves]
log("m0_0 location key counts per axis:", nkeys)
cbp = play.animation_data.action.layers[0].strips[0].channelbags[0]
log("PLAY fcurves:", [(fc.data_path, fc.array_index, len(fc.keyframe_points)) for fc in cbp.fcurves][:12])

# ---------------------------------------------------------------- M2 refraction (dual switch)
log("=== M2. glass refraction dual-switch matrix (f150, 480x270, 16spp) ===")
glass = [m for m in bpy.data.materials if m.name.startswith("glass_")]
log("glass materials:", [m.name for m in glass], "| use_raytrace_refraction:", glass[0].use_raytrace_refraction)
res = {}
for rt in (False, True):
    for refr in (False, True):
        sc.eevee.use_raytracing = rt
        for m in glass:
            m.use_raytrace_refraction = refr
        p = os.path.join(OD, "refr_%s_%s.png" % (rt, refr))
        a, _ = render(p, 150)
        res[(rt, refr)] = a
base = res[(False, False)]
for k, a in res.items():
    d = diff(a, base)
    log("scene_raytracing=%s mat_refraction=%s -> %s" % (k[0], k[1], d))
R["refraction_matrix"] = {str(k): diff(a, base) for k, a in res.items()}
sc.eevee.use_raytracing = True
for m in glass:
    m.use_raytrace_refraction = True

# ---------------------------------------------------------------- M3 rubber SSS
log("=== M3. rubber SSS toggle (f250, 480x270) ===")
rub = bpy.data.materials["rubber"]
b = rub.node_tree.nodes["Principled BSDF"]
w = b.inputs["Subsurface Weight"].default_value
log("rubber Subsurface Weight =", w, "| Radius =", tuple(b.inputs["Subsurface Radius"].default_value),
    "| Scale =", b.inputs["Subsurface Scale"].default_value)
a_on, _ = render(os.path.join(OD, "sss_on.png"), 250)
b.inputs["Subsurface Weight"].default_value = 0.0
a_off, _ = render(os.path.join(OD, "sss_off.png"), 250)
b.inputs["Subsurface Weight"].default_value = w
R["sss"] = diff(a_on, a_off)
log("sss on vs off:", R["sss"])

# ---------------------------------------------------------------- M4 metal
log("=== M4. metal reflection (chrome vs matte, f250) ===")
chr_ = bpy.data.materials["chrome"]
bb = chr_.node_tree.nodes["Principled BSDF"]
log("chrome: Metallic", bb.inputs["Metallic"].default_value, "Roughness", bb.inputs["Roughness"].default_value)
a_m, _ = render(os.path.join(OD, "metal_metal.png"), 250)
bb.inputs["Metallic"].default_value = 0.0
bb.inputs["Roughness"].default_value = 0.9
a_d, _ = render(os.path.join(OD, "metal_matte.png"), 250)
bb.inputs["Metallic"].default_value = 1.0
bb.inputs["Roughness"].default_value = 0.08
R["metal"] = diff(a_m, a_d)
log("chrome vs matte-diffuse:", R["metal"])

# ---------------------------------------------------------------- M5 DOF
log("=== M5. DOF: gradient energy focus vs background (f250, 960x540) ===")
a, _ = render(os.path.join(OD, "dof_f250.png"), 250, pct=50, samples=32)
h, w = a.shape[:2]
lum = a[..., :3].mean(axis=2)
gx = np.abs(np.diff(lum, axis=1)); gy = np.abs(np.diff(lum, axis=0))
g = gx[:-1, :] + gy[:, :-1]
def region(r0, r1, c0, c1):
    return float(g[int(h*r0):int(h*r1), int(w*c0):int(w*c1)].mean())
focus = region(0.40, 0.65, 0.30, 0.70)
bg = region(0.03, 0.15, 0.05, 0.95)
near = region(0.78, 0.97, 0.15, 0.85)
log("gradient energy: focus=%.5f background=%.5f near-field=%.5f | focus/bg ratio=%.2f" % (focus, bg, near, focus / max(bg, 1e-9)))
cd = sc.camera.data
log("camera dof: fstop", cd.dof.aperture_fstop, "| focus_distance", round(cd.dof.focus_distance, 2), "| blades", cd.dof.aperture_blades)
R["dof"] = {"focus": round(focus, 5), "bg": round(bg, 5), "near": round(near, 5), "ratio": round(focus / max(bg, 1e-9), 2)}

# ---------------------------------------------------------------- M6 motion blur
log("=== M6. motion blur on/off (f95 fall, f108 scatter, 480x270) ===")
R["mb"] = {}
for f in (95, 108):
    a_off, _ = render(os.path.join(OD, "mb_off_%d.png" % f), f, mb=False)
    a_on, _ = render(os.path.join(OD, "mb_on_%d.png" % f), f, mb=True, mb_steps=16)
    R["mb"][str(f)] = diff(a_on, a_off)
    log("f%d on vs off:" % f, R["mb"][str(f)])

# ---------------------------------------------------------------- M7 soft shadow penumbra (probe10-style mini scene)
log("=== M7. penumbra width vs light size (mini scene, 512x512) ===")
bpy.ops.wm.read_factory_settings(use_empty=True)
sc2 = bpy.context.scene
bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 0, 0))
fl = bpy.context.active_object
mf = bpy.data.materials.new("F"); mf.use_nodes = True
mf.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.8, 0.8, 0.8, 1)
mf.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.9
fl.data.materials.append(mf)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 2.0))
bx = bpy.context.active_object
cd2 = bpy.data.cameras.new("C"); co2 = bpy.data.objects.new("C", cd2)
sc2.collection.objects.link(co2)
co2.location = (0, 0, 12); co2.rotation_euler = (0, 0, 0); sc2.camera = co2
cd2.type = "ORTHO"; cd2.ortho_scale = 12.0
ld2 = bpy.data.lights.new("K", type="AREA"); lo2 = bpy.data.objects.new("K", ld2)
sc2.collection.objects.link(lo2)
lo2.location = (0, 0, 14); lo2.rotation_euler = (0, 0, 0)
sc2.render.engine = "BLENDER_EEVEE"; sc2.eevee.taa_render_samples = 32
sc2.render.resolution_x = 512; sc2.render.resolution_y = 512
sc2.render.image_settings.file_format = "PNG"
pen = []
for size in (0.1, 2.0, 8.0):
    ld2.size = size
    ld2.energy = 200.0 * max(size, 0.1) ** 2 / 4.0
    p = os.path.join(OD, "pen_%s.png" % size)
    sc2.render.filepath = p
    bpy.ops.render.render(write_still=True)
    a = grab(p)
    row = a[256, :, 0]
    lo_v, hi_v = float(row.min()), float(row.max())
    lo10 = lo_v + 0.10 * (hi_v - lo_v)
    lo90 = lo_v + 0.90 * (hi_v - lo_v)
    idx = np.where(row < lo90)[0]
    left = idx[idx < 256]
    band = 0
    if len(left):
        start = left.min()
        j = start
        while j < 512 and row[j] < lo90:
            j += 1
        while j < 512 and row[j] < lo10:
            j += 1
        band = j - start
    pen.append({"light_size": size, "penumbra_px_10_90": int(band), "bytes": os.path.getsize(p)})
    log("light size %s -> penumbra %d px" % (size, band))
R["penumbra"] = pen

json.dump(R, open(os.path.join(BASE, "checks", "mech_numbers.json"), "w"), indent=1)
log("=== MECH DONE ===")
print("MECH_DONE")
