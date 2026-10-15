"""build_scene.py — anim_test_03_blender: 10s "3D 质感 PLAY" scene (card 01, Blender line).

Pipeline (deterministic): build scene -> scripted marble wave -> rigid-body sim (PLAY falls
into marble field) -> bake ALL motion to keyframes -> strip physics -> save scene.blend.

Run:  "D:/Software/Blender Foundation/Blender 5.2/blender.exe" --background --factory-startup --python build_scene.py

Outputs (in this dir): scene.blend, checks/bake_data.npz, checks/bake_stats.json, build log on stdout.
"""
import bpy, bmesh, math, os, sys, json, time
import numpy as np

T0 = time.time()
BASE = os.path.dirname(os.path.abspath(__file__))
CHK = os.path.join(BASE, "checks")
os.makedirs(CHK, exist_ok=True)

def log(*a):
    print("[build %6.1fs]" % (time.time() - T0), *a, flush=True)

FPS = 30
NF = 300                      # frames 0..299
SIM_START = 78                # frame where rigid sim takes over
PLAY_START_Z = 3.05           # PLAY origin height at SIM_START (falls to impact ~f99)
R_MARBLE = 0.25
SPACING = 0.56
NI, NJ = 15, 18               # marble grid: 270 marbles
WAVE_FADE0, WAVE_FADE1 = 52, 90
PLAY_W = 2.55                 # target PLAY width

# ------------------------------------------------------------------ helpers
def smoothstep(a, b, x):
    u = min(max((x - a) / (b - a), 0.0), 1.0)
    return u * u * (3 - 2 * u)

def hexcol(h, a=1.0):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return (*lin, a)

def wave_offset(i, j, f):
    """height offset above rest for marble (i,j) at frame f (0..)."""
    t = f / FPS
    th1 = 2 * math.pi * 0.70 * t - (i * 0.46 + j * 0.18)
    th2 = 2 * math.pi * 0.50 * t - (i * 0.15 - j * 0.38)
    return 0.32 * (0.5 + 0.5 * math.sin(th1)) + 0.14 * (0.5 + 0.5 * math.sin(th2))

def wave_env(f):
    return 1.0 - smoothstep(WAVE_FADE0, WAVE_FADE1, f)

def _hash01(i, j, k):
    v = math.sin(i * 12.9898 + j * 78.233 + k * 37.719) * 43758.5453
    return v - math.floor(v)

def marble_rest(i, j):
    jx = (_hash01(i, j, 1) * 2 - 1) * 0.020
    jy = (_hash01(i, j, 2) * 2 - 1) * 0.020
    return ((i - (NI - 1) / 2) * SPACING + jx, (j - (NJ - 1) / 2) * SPACING + jy, R_MARBLE)

def marble_scale(i, j):
    return 1.0 + (_hash01(i, j, 3) * 2 - 1) * 0.03

def fcurves_of(ob):
    act = ob.animation_data.action
    if hasattr(act, "layers") and len(act.layers):
        return act.layers[0].strips[0].channelbags[0].fcurves
    return act.fcurves

# ------------------------------------------------------------------ scene reset + settings
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = "BLENDER_EEVEE"
sc.render.resolution_x, sc.render.resolution_y = 1920, 1080
sc.render.resolution_percentage = 100
sc.render.fps = FPS
sc.render.fps_base = 1.0
sc.frame_start, sc.frame_end = 0, NF - 1
sc.render.image_settings.file_format = "PNG"
sc.render.image_settings.color_mode = "RGB"
sc.render.image_settings.color_depth = "8"
sc.render.image_settings.compression = 15
sc.render.dither_intensity = 1.0
sc.render.use_motion_blur = True
sc.render.motion_blur_shutter = 0.5
sc.render.film_transparent = False
try:
    sc.view_settings.view_transform = "Khronos PBR Neutral"
except TypeError:
    sc.view_settings.view_transform = "AgX"
sc.view_settings.look = "None"
sc.view_settings.exposure = 0.0

ee = sc.eevee
ee.taa_render_samples = 64
ee.use_raytracing = True
try:
    ee.ray_tracing_options.resolution_scale = '1'
except Exception as e:
    log("ray resolution_scale set failed:", e)
ee.motion_blur_steps = 16
ee.motion_blur_max = 32
ee.shadow_ray_count = 2
ee.shadow_step_count = 8
ee.use_overscan = True
ee.overscan_size = 4.0
log("eevee:", "samples", ee.taa_render_samples, "rt", ee.use_raytracing,
    "rt_res", ee.ray_tracing_options.resolution_scale, "mb_steps", ee.motion_blur_steps)

bpy.context.preferences.edit.keyframe_new_interpolation_type = 'LINEAR'

# ------------------------------------------------------------------ materials
def principled(name, **kw):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    for k, v in kw.items():
        b.inputs[k].default_value = v
    return m

GLASS_TINTS = {
    "aqua":   (0.06, 0.50, 0.62, 1.0),
    "rose":   (0.72, 0.06, 0.24, 1.0),
    "amber":  (0.82, 0.38, 0.05, 1.0),
    "lime":   (0.14, 0.52, 0.12, 1.0),
    "violet": (0.30, 0.12, 0.66, 1.0),
    "sky":    (0.05, 0.22, 0.72, 1.0),
}
MATS = {}
for nm, tint in GLASS_TINTS.items():
    m = principled("glass_" + nm, **{
        "Base Color": tint, "Roughness": 0.02, "IOR": 1.45, "Transmission Weight": 1.0})
    m.use_raytrace_refraction = True
    MATS[nm] = m
m = principled("glass_clear", **{
    "Base Color": (1, 1, 1, 1), "Roughness": 0.02, "IOR": 1.45, "Transmission Weight": 1.0})
m.use_raytrace_refraction = True
MATS["clear"] = m
MATS["chrome"] = principled("chrome", **{
    "Base Color": (0.92, 0.92, 0.95, 1), "Metallic": 1.0, "Roughness": 0.08})
MATS["gold"] = principled("gold", **{
    "Base Color": (0.93, 0.72, 0.32, 1), "Metallic": 1.0, "Roughness": 0.18})
MATS["rubber"] = principled("rubber", **{
    "Base Color": (0.85, 0.30, 0.30, 1), "Roughness": 0.5,
    "Subsurface Weight": 0.75, "Subsurface Radius": (0.4, 0.15, 0.1),
    "Subsurface Scale": 0.12, "Specular IOR Level": 0.4,
    "Coat Weight": 0.25, "Coat Roughness": 0.15})
_cyc = principled("cyc", **{"Base Color": hexcol("#B4AEB2"), "Roughness": 0.95, "Specular IOR Level": 0.12})
_nt = _cyc.node_tree
_tc = _nt.nodes.new('ShaderNodeTexCoord')
_sep = _nt.nodes.new('ShaderNodeSeparateXYZ')
_nt.links.new(_tc.outputs['Object'], _sep.inputs[0])
_mr = _nt.nodes.new('ShaderNodeMapRange')
_mr.inputs['From Min'].default_value = -3.0
_mr.inputs['From Max'].default_value = 6.0
_mr.interpolation_type = 'SMOOTHSTEP'
_nt.links.new(_sep.outputs['Y'], _mr.inputs['Value'])
_mx = _nt.nodes.new('ShaderNodeMix')
_mx.data_type = 'RGBA'
_mx.inputs['A'].default_value = hexcol("#A8A2A6")
_mx.inputs['B'].default_value = hexcol("#7E787C")
_nt.links.new(_mr.outputs['Result'], _mx.inputs['Factor'])
_nt.links.new(_mx.outputs['Result'], _nt.nodes["Principled BSDF"].inputs['Base Color'])
_mz = _nt.nodes.new('ShaderNodeMapRange')
_mz.inputs['From Min'].default_value = 1.5
_mz.inputs['From Max'].default_value = 10.0
_mz.interpolation_type = 'SMOOTHSTEP'
_nt.links.new(_sep.outputs['Z'], _mz.inputs['Value'])
_mx2 = _nt.nodes.new('ShaderNodeMix')
_mx2.data_type = 'RGBA'
_mx2.inputs['B'].default_value = hexcol("#6A6468")
_nt.links.new(_mx.outputs['Result'], _mx2.inputs['A'])
_nt.links.new(_mz.outputs['Result'], _mx2.inputs['Factor'])
_nt.links.new(_mx2.outputs['Result'], _nt.nodes["Principled BSDF"].inputs['Base Color'])
MATS["cyc"] = _cyc
log("materials done:", sorted(MATS))

# ------------------------------------------------------------------ cyclorama (floor + cove + wall, one mesh)
prof = []
for y in np.linspace(-34, 8, 40):
    prof.append((y, 0.0))
Rc = 3.0
for a in np.linspace(math.pi, math.pi / 2, 26)[1:]:
    prof.append((11.0 + Rc * math.cos(a), Rc * math.sin(a)))
for z in np.linspace(3.0, 26.0, 9)[1:]:
    prof.append((11.0, z))
xs = np.linspace(-48, 48, 49)
me = bpy.data.meshes.new("cyc")
bm = bmesh.new()
grid = [[bm.verts.new((x, y, z)) for (y, z) in prof] for x in xs]
for a in range(len(xs) - 1):
    for b in range(len(prof) - 1):
        bm.faces.new((grid[a][b], grid[a + 1][b], grid[a + 1][b + 1], grid[a][b + 1]))
bm.to_mesh(me)
bm.free()
for p in me.polygons:
    p.use_smooth = True
cyc = bpy.data.objects.new("cyc", me)
sc.collection.objects.link(cyc)
me.materials.append(MATS["cyc"])
log("cyc done, verts", len(me.vertices))

# ------------------------------------------------------------------ rigid world + physics floor (created BEFORE rb objects, proven order)
bpy.ops.rigidbody.world_add()
rw = sc.rigidbody_world
rw.substeps_per_frame = 16
rw.solver_iterations = 12

# invisible physics floor (exact plane; the visual cyc stays a plain mesh)
bpy.ops.mesh.primitive_plane_add(size=300, location=(0, 0, 0))
floor_phys = bpy.context.active_object
floor_phys.name = "floor_phys"
floor_phys.hide_render = True
bpy.context.view_layer.objects.active = floor_phys
bpy.ops.rigidbody.object_add()
floor_phys.rigid_body.type = 'PASSIVE'
floor_phys.rigid_body.friction = 0.6

# ------------------------------------------------------------------ marble field (shared mesh, per-object material slots)
# Blender 5.2 rigid-body gotcha (probed): the working pattern is rb-on-proto -> copies INHERIT ->
# keep the proto object alive (moving it far away is fine). Per-copy `object_add` or removing the
# proto makes contacts resolve as soft/creep (no scatter). See checks.md §gotchas.
bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=R_MARBLE)
proto = bpy.context.active_object
proto.name = "marble_proto"
mesh = proto.data
mesh.name = "marble_shared"
mesh.materials.append(MATS["aqua"])          # base slot; per-object override below
mesh.polygons.foreach_set("use_smooth", np.ones(len(mesh.polygons), dtype=bool))
mesh.update()

bpy.context.view_layer.objects.active = proto
bpy.ops.rigidbody.object_add()
_prb = proto.rigid_body
_prb.type = 'ACTIVE'
_prb.collision_shape = 'CONVEX_HULL'         # proven in probe8d
_prb.mass = 0.2
_prb.friction = 0.48
_prb.restitution = 0.5
_prb.linear_damping = 0.04
_prb.angular_damping = 0.1
_prb.use_deactivation = False                # deactivation freezes the bed (probed)

SPECIALS = {(4, 2): "chrome", (10, 6): "chrome", (12, 2): "gold",
            (7, 5): "clear", (2, 8): "clear", (13, 8): "clear", (6, 2): "clear"}
TINTS = list(GLASS_TINTS.keys())
bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=R_MARBLE)
proto_deco = bpy.context.active_object
proto_deco.data = mesh
marbles = []          # (obj, i, j)  -- physics field (central rows)
deco = []             # (obj, i, j)  -- decorative outer rows (no rigid body)
for i in range(NI):
    for j in range(NJ):
        src = proto if 2 <= j <= 14 else proto_deco
        o = src.copy()
        o.data = mesh
        x, y, z = marble_rest(i, j)
        o.location = (x, y, z)
        o.scale = (marble_scale(i, j),) * 3
        sc.collection.objects.link(o)
        o.name = "m%d_%d" % (i, j)
        o.material_slots[0].link = 'OBJECT'
        key = SPECIALS.get((i, j)) or TINTS[int(_hash01(i, j, 7) * 6) % 6]
        o.material_slots[0].material = MATS[key]
        if 2 <= j <= 14:
            marbles.append((o, i, j))
        else:
            deco.append((o, i, j))
# keep protos alive (5.2 quirk): park them far below and hide from render
proto.location = (0, 0, -60)
proto.hide_render = True
proto_deco.location = (0.5, 0, -60)
proto_deco.hide_render = True
log("marbles:", len(marbles), "+ deco:", len(deco), "| shared mesh users:", mesh.users)

STRAYS = [(-2.6, 6.6, "amber"), (1.7, 6.9, "aqua"), (3.2, 6.3, "rose"),
          (-1.4, 7.0, "lime"), (4.6, 6.6, "sky"), (-3.9, 6.8, "clear"), (0.2, 7.2, "violet")]
strays = []
for k, (sx, sy, col) in enumerate(STRAYS):
    o = bpy.data.objects.new("stray%d" % k, mesh)
    o.location = (sx, sy, R_MARBLE)
    sc.collection.objects.link(o)
    o.material_slots[0].link = 'OBJECT'
    o.material_slots[0].material = MATS[col]
    strays.append(o)
log("strays:", len(strays))

# ------------------------------------------------------------------ PLAY (text -> mesh, rubber)
bpy.ops.object.text_add(location=(0, 0, 0))
txt = bpy.context.active_object
txt.data.body = "PLAY"
txt.data.size = 1.0
txt.data.extrude = 0.30
txt.data.bevel_depth = 0.07
txt.data.bevel_resolution = 4
bpy.ops.object.convert(target='MESH')
play = bpy.context.active_object
play.name = "PLAY"
me = play.data
me.name = "PLAY_mesh"
n = len(me.vertices)
co = np.empty(n * 3, np.float32)
me.vertices.foreach_get("co", co)
co = co.reshape(-1, 3)
# center x, bottom y, center z; scale to PLAY_W
x0, x1 = co[:, 0].min(), co[:, 0].max()
y0, y1 = co[:, 1].min(), co[:, 1].max()
z0, z1 = co[:, 2].min(), co[:, 2].max()
s = PLAY_W / (x1 - x0)
co[:, 0] = (co[:, 0] - (x0 + x1) / 2) * s
co[:, 1] = (co[:, 1] - y0) * s
co[:, 2] = (co[:, 2] - (z0 + z1) / 2) * s
me.vertices.foreach_set("co", co.ravel())
me.update()
me.polygons.foreach_set("use_smooth", np.ones(len(me.polygons), dtype=bool))
me.update()
me.materials.clear()
me.materials.append(MATS["rubber"])
play.rotation_euler = (math.pi / 2, 0, 0)
play.location = (0, 0, PLAY_START_Z)
log("PLAY: verts %d, bbox w %.3f h %.3f t %.3f" % (
    n, (co[:, 0].max() - co[:, 0].min()), (co[:, 1].max() - co[:, 1].min()),
    (co[:, 2].max() - co[:, 2].min())))

# ------------------------------------------------------------------ lights
def area(name, loc, target, size, power, color, shape='DISK', size_y=None, spread=None):
    ld = bpy.data.lights.new(name, 'AREA')
    ld.energy = power
    ld.color = color[:3]
    ld.shape = shape
    ld.size = size
    if size_y:
        ld.size_y = size_y
    if spread is not None:
        ld.spread = math.radians(spread)
    ob = bpy.data.objects.new(name, ld)
    sc.collection.objects.link(ob)
    ob.location = loc
    d = np.array(target, float) - np.array(loc, float)
    ob.rotation_euler = __import__('mathutils').Vector(d).to_track_quat('-Z', 'Y').to_euler()
    return ob

area("key",  (-6.5, -4.5, 7.0), (0.3, 0, 0.5), 5.5, 2200, (1.0, 0.97, 0.93), 'DISK', spread=75)
area("fill", (6.5, -8.5, 3.2),  (0, 0, 0.4),   8.0,  550, (0.88, 0.90, 1.0), 'DISK')
area("rim",  (1.0, 6.8, 3.6),   (0, 0, 0.7),   6.0, 2000, (1.0, 0.90, 0.92), 'RECTANGLE', size_y=1.6)
area("wall", (0.0, 7.0, 3.2),   (0, 18, 12.0), 10.0, 220, (1.0, 0.95, 0.97), 'DISK')
area("spec", (2.6, -5.2, 6.2),  (0.0, 0, 0.6),  0.7,  260, (1.0, 1.0, 1.0), 'DISK')
log("lights done")

# ------------------------------------------------------------------ world (soft studio gradient)
world = bpy.data.worlds.new("World")
sc.world = world
wt = world.node_tree
for nd in list(wt.nodes):
    wt.nodes.remove(nd)
out = wt.nodes.new('ShaderNodeOutputWorld')
bg = wt.nodes.new('ShaderNodeBackground')
bg.inputs['Color'].default_value = hexcol('#EDEAEE')
tc = wt.nodes.new('ShaderNodeTexCoord')
sep = wt.nodes.new('ShaderNodeSeparateXYZ')
wt.links.new(tc.outputs['Generated'], sep.inputs[0])
mr = wt.nodes.new('ShaderNodeMapRange')
mr.inputs['From Min'].default_value = -0.05
mr.inputs['From Max'].default_value = 0.75
mr.inputs['To Min'].default_value = 0.42
mr.inputs['To Max'].default_value = 0.75
mr.interpolation_type = 'SMOOTHSTEP'
wt.links.new(sep.outputs['Z'], mr.inputs['Value'])
wt.links.new(mr.outputs['Result'], bg.inputs['Strength'])
wt.links.new(bg.outputs['Background'], out.inputs['Surface'])
log("world done")

# ------------------------------------------------------------------ camera (push-in + focus + kick)
cd = bpy.data.cameras.new("cam")
cam = bpy.data.objects.new("cam", cd)
sc.collection.objects.link(cam)
sc.camera = cam
cd.sensor_width = 36
cd.sensor_fit = 'HORIZONTAL'
cd.lens = 64.0
cd.dof.use_dof = True
cd.dof.aperture_fstop = 1.1
cd.dof.aperture_blades = 0
cd.clip_start = 0.05
cd.clip_end = 200

POS0 = np.array([0.0, -9.6, 2.35])
POS1 = np.array([0.0, -7.6, 1.5])
TGT0 = np.array([0.0, 0.1, 1.0])
TGT1 = np.array([0.0, 0.0, 0.9])

# ------------------------------------------------------------------ physics: PLAY rigid body
# (world + floor + marble bodies already created above)

bpy.context.view_layer.objects.active = play
bpy.ops.rigidbody.object_add()
rb = play.rigid_body
rb.type = 'ACTIVE'
rb.collision_shape = 'CONVEX_HULL'
rb.mass = 30.0
rb.friction = 0.6
rb.restitution = 0.5
rb.linear_damping = 0.015
rb.angular_damping = 0.8
rb.use_deactivation = False
log("physics set: world + %d marbles + PLAY" % len(marbles))

# initial marble positions = wave at SIM_START (wave env ensures they are low, settling in sim)
for o, i, j in marbles:
    x, y, z = marble_rest(i, j)
    o.location = (x, y, z + wave_offset(i, j, SIM_START) * wave_env(SIM_START))
bpy.context.view_layer.update()

# ------------------------------------------------------------------ run sim f=SIM_START..NF-1, record
# NOTE: manual frame_set scrubbing does NOT advance Bullet in this headless flow
# (probe: frames freeze). Proven path: set point-cache range explicitly, ptcache.bake_all,
# then read transforms per frame (values come from the baked cache).
sim_t = time.time()
sc.frame_start = SIM_START
sc.frame_end = NF - 1
rw.point_cache.frame_start = SIM_START
rw.point_cache.frame_end = NF - 1
bpy.ops.ptcache.bake_all(bake=True)
log("rigid bake done in %.1fs (pc range %d..%d)" % (time.time() - sim_t,
    rw.point_cache.frame_start, rw.point_cache.frame_end))
FRS = list(range(SIM_START, NF))
rec = np.zeros((len(FRS), len(marbles), 3), np.float32)
rec_play = np.zeros((len(FRS), 3), np.float32)
for k, f in enumerate(FRS):
    sc.frame_set(f)
    bpy.context.view_layer.update()
    for mi, (o, i, j) in enumerate(marbles):
        t = o.matrix_world.translation
        rec[k, mi] = (t.x, t.y, t.z)
    t = play.matrix_world.translation
    rec_play[k] = (t.x, t.y, t.z)
sim_dur = time.time() - sim_t
log("sim done in %.1fs" % sim_dur)
log("pz coarse:", [round(float(v), 2) for v in rec_play[::4, 2]])

# ------------------------------------------------------------------ strip physics (deterministic keyframe render)
def try_strip():
    for o in list(sc.objects):
        if o.rigid_body is not None:
            bpy.context.view_layer.objects.active = o
            try:
                bpy.ops.rigidbody.object_remove()
            except Exception as e:
                log("object_remove failed for", o.name, e)
    try:
        bpy.ops.rigidbody.world_remove()
    except Exception as e:
        log("world_remove failed:", e)
try_strip()
n_rb = len([o for o in sc.objects if o.rigid_body is not None])
log("physics stripped; remaining rigid bodies:", n_rb, "| world:", sc.rigidbody_world)

# ------------------------------------------------------------------ contact detection (PLAY bottom z)
pz = rec_play[:, 2]                    # origin z per frame (FRS index)
def detect_contacts():
    """local minima with a real preceding apex; speed from energy conservation."""
    contacts = []
    prev_k = -100
    for k in range(4, len(FRS) - 4):
        f = FRS[k]
        if f < 80 or f > 270:
            continue
        z = pz[k]
        if z < 1.25 and z == min(pz[max(0, k - 4):k + 5]):
            seg = pz[max(0, prev_k + 1):k]
            if len(seg) == 0:
                continue
            z_apex = float(seg.max())
            if z_apex - z < 0.10:          # creep, not a bounce
                continue
            if not contacts or f - contacts[-1][0] > 8:
                v = math.sqrt(max(2 * 9.81 * (z_apex - z), 0.0))
                v_local = (pz[max(0, k - 4)] - z) / 4 * FPS
                if v_local >= 2.5:
                    contacts.append((f, round(v, 3)))
                    prev_k = k
    # soft landing after the first bounce (no clean local min - it merges into the sink)
    if contacts:
        c1f = contacts[0][0]
        seg = [(f, float(pz[f - SIM_START])) for f in range(c1f + 15, min(c1f + 60, NF))]
        soft = min(seg, key=lambda t: t[1])
        if soft[1] < 0.5:
            contacts.append((soft[0], 2.6))
    return contacts
contacts = detect_contacts()
log("contacts:", contacts)

# scripted vertical pop layer (author-style stylized shockwave hop).
# Lateral scatter = genuine rigid-body sim; the vertical pops are choreography on top,
# because a flat heavy slab pressing a dense bed produces lateral-only squeeze (measured).
rec2 = rec.copy()
t_imp = (contacts[0][0] if contacts else 100) / FPS
for mi, (o, i, j) in enumerate(marbles):
    bx, by, _ = marble_rest(i, j)
    r = math.hypot(bx, by)
    h = min(0.9, 0.9 * math.exp(-max(r - 0.4, 0.0) / 1.7) + 0.05)
    if h < 0.04:
        continue
    t_i = t_imp + max(r - 0.45, 0.0) / 5.5
    T_i = 0.55 + 0.15 * _hash01(i, j, 9)
    for k, f in enumerate(FRS):
        t = f / FPS
        if t_i <= t <= t_i + T_i:
            rec2[k, mi, 2] += h * math.sin(math.pi * (t - t_i) / T_i)
pop_max = float((rec2[:, :, 2] - rec[:, :, 2]).max())
log("pop layer: max hop = %.3f" % pop_max)
np.savez_compressed(os.path.join(CHK, "bake_data.npz"), frames=np.array(FRS),
                    marbles=rec2, marbles_raw=rec, play=rec_play,
                    marble_base=np.array([marble_rest(i, j) for o, i, j in marbles], np.float32))

# ------------------------------------------------------------------ bake keyframes
bake_t = time.time()
wave_frames = list(range(0, SIM_START + 1, 4))
sim_frames = [f for f in FRS if f <= 150] + [f for f in range(152, NF - 1, 2)] + [NF - 1]
all_frames = sorted(set(wave_frames + sim_frames))
for mi, (o, i, j) in enumerate(marbles):
    x, y, z0 = marble_rest(i, j)
    for f in all_frames:
        if f <= SIM_START:
            o.location = (x, y, z0 + wave_offset(i, j, f) * wave_env(f))
        else:
            k = f - SIM_START
            o.location = (float(rec2[k, mi, 0]), float(rec2[k, mi, 1]), float(rec2[k, mi, 2]))
        o.keyframe_insert(data_path="location", frame=f)
    for fc in fcurves_of(o):
        for kp in fc.keyframe_points:
            kp.interpolation = 'BEZIER' if kp.co.x <= SIM_START else 'LINEAR'
        fc.update()
log("marble keys done in %.1fs (%d keys each)" % (time.time() - bake_t, len(all_frames)))

# deco rows: wave keys then settle fade + scripted pop hop (no physics)
E78 = wave_env(SIM_START)
for o, i, j in deco:
    x, y, z0 = marble_rest(i, j)
    r = math.hypot(x, y)
    h = min(0.9, 0.9 * math.exp(-max(r - 0.4, 0.0) / 1.7) + 0.05)
    t_i = t_imp + max(r - 0.45, 0.0) / 5.5
    T_i = 0.55 + 0.15 * _hash01(i, j, 9)
    for f in range(0, NF, 4):
        z = z0 + wave_offset(i, j, f) * wave_env(f)
        if f > SIM_START:
            fade = 1.0 - smoothstep(SIM_START, 92, f)
            z = z0 + wave_offset(i, j, SIM_START) * E78 * fade
            t = f / FPS
            if h >= 0.04 and t_i <= t <= t_i + T_i:
                z += h * math.sin(math.pi * (t - t_i) / T_i)
        o.location = (x, y, z)
        o.keyframe_insert(data_path="location", frame=f)
    for fc in fcurves_of(o):
        for kp in fc.keyframe_points:
            kp.interpolation = 'BEZIER'
        fc.update()
log("deco keys done")

# PLAY: location + rotation + scale
c1 = contacts[0][0] if contacts else 100
t_imp = c1 / FPS
play_sim_frames = [f for f in FRS if f <= 150] + [f for f in range(152, NF - 1, 2)] + [NF - 1]

# squash curve: damped oscillator kicked at contacts (jelly), plus pre-impact stretch
def squash_curve():
    dt = 1 / 2400.0
    t_end = NF / FPS
    ws = 2 * math.pi * 3.1
    zeta = 0.5
    K = 1.9
    kicks = [(c / FPS, v) for c, v in contacts]
    ts = np.arange(0, t_end + 0.1, dt)
    s = 0.0; sv = 0.0
    out = np.zeros(len(ts))
    ki = 0
    for idx, t in enumerate(ts):
        if ki < len(kicks) and t >= kicks[ki][0]:
            sv -= K * kicks[ki][1]
            ki += 1
        sa = -ws * ws * s - 2 * zeta * ws * sv
        sv += sa * dt
        s += sv * dt
        if s < -0.42:
            s = -0.42
        out[idx] = s
    return ts, out

ts_sq, s_sq = squash_curve()
log("squash: max |s| = %.3f at t=%.2fs" % (abs(s_sq).max(), ts_sq[abs(s_sq).argmax()]))

def play_scale(f):
    t = f / FPS
    s = float(np.interp(t, ts_sq, s_sq))
    if f < c1:
        s = max(s, 0.05 * smoothstep(88, c1 - 2, f))     # gentle pre-impact stretch
    ky = 1.0 + s
    kxz = 1.0 / math.sqrt(max(ky, 0.4))
    return (kxz, ky, kxz)

scale_frames = sorted(set(list(range(0, NF, 2)) + list(range(max(0, c1 - 8), min(NF, c1 + 44), 1))
                          + list(range(max(0, (contacts[1][0] if len(contacts) > 1 else 999) - 6),
                                       min(NF, (contacts[1][0] if len(contacts) > 1 else 999) + 24), 1))))
for f in play_sim_frames:
    k = f - SIM_START
    play.location = (float(rec_play[k, 0]), float(rec_play[k, 1]), float(rec_play[k, 2]))
    play.keyframe_insert(data_path="location", frame=f)
    # rotation: fixed upright + decay wobble after impact
    tau = max(0.0, (f - c1) / FPS)
    wob_x = 0.030 * math.exp(-tau / 0.5) * math.sin(2 * math.pi * tau / 0.55 + 0.8)
    wob_y = 0.018 * math.exp(-tau / 0.5) * math.sin(2 * math.pi * tau / 0.62 + 2.1)
    wob_z = 0.045 * (1.0 - smoothstep(SIM_START, c1 - 1, f)) + 0.020 * math.exp(-tau / 0.4) * math.sin(2 * math.pi * tau / 0.7)
    play.rotation_euler = (math.pi / 2 + wob_x, wob_y, wob_z)
    play.keyframe_insert(data_path="rotation_euler", frame=f)
for f in scale_frames:
    play.scale = play_scale(f)
    play.keyframe_insert(data_path="scale", frame=f)
for fc in fcurves_of(play):
    for kp in fc.keyframe_points:
        kp.interpolation = 'BEZIER'
    fc.update()
play.rotation_euler = (math.pi / 2, 0, 0)
play.scale = (1, 1, 1)
log("PLAY keys done (c1=%d)" % c1)

# ------------------------------------------------------------------ camera keys (every 2 frames)
for f in list(range(0, NF, 2)) + [NF - 1]:
    u = smoothstep(10, 260, f)
    pos = POS0 + (POS1 - POS0) * u
    tgt = TGT0 + (TGT1 - TGT0) * u
    # kick after impact
    if f > c1:
        tau = (f - c1) / FPS
        pos = pos + np.array([0.013 * math.exp(-tau / 0.15) * math.sin(2 * math.pi * 5.8 * tau + 1.2),
                              0.0,
                              0.020 * math.exp(-tau / 0.15) * math.sin(2 * math.pi * 6.6 * tau + 0.4)])
    cam.location = tuple(pos)
    d = np.array(tgt, float) - pos
    cam.rotation_euler = __import__('mathutils').Vector(d).to_track_quat('-Z', 'Y').to_euler()
    # focus: track the PLAY centre while falling, then the settled pile
    if f < SIM_START:
        fz = 0.9
    else:
        k = min(max(f - SIM_START, 0), len(FRS) - 1)
        fz = min(max(float(rec_play[k, 2]) + 0.4, 0.75), 4.0)
    foc = float(np.linalg.norm(np.array([0.0, 0.0, fz]) - pos))
    cam.keyframe_insert(data_path="location", frame=f)
    cam.keyframe_insert(data_path="rotation_euler", frame=f)
    cd.dof.focus_distance = foc
    cd.dof.keyframe_insert(data_path="focus_distance", frame=f)
log("camera keys done; c1=%d" % c1)

# ------------------------------------------------------------------ compositor: gentle bloom
ng = bpy.data.node_groups.new("Comp", "CompositorNodeTree")
sc.compositing_node_group = ng
ng.interface.new_socket('Image', in_out='OUTPUT', socket_type='NodeSocketColor')
rl = ng.nodes.new('CompositorNodeRLayers')
glare = ng.nodes.new('CompositorNodeGlare')
glare_set = {}
for k, v in (('Type', 'Bloom'), ('Quality', 'High'), ('Threshold', 1.5), ('Strength', 0.08), ('Size', 0.4)):
    try:
        glare.inputs[k].default_value = v
        glare_set[k] = v
    except Exception as e:
        log("glare input fail:", k, e)
outn = ng.nodes.new('NodeGroupOutput')
ng.links.new(rl.outputs['Image'], glare.inputs['Image'])
ng.links.new(glare.outputs['Image'], outn.inputs['Image'])
sc.render.use_compositing = True
log("compositor done", glare_set)

# ------------------------------------------------------------------ stats + save
stats = {
    "contacts": [[int(c), round(float(v), 3)] for c, v in contacts],
    "play_z_f100": round(float(rec_play[100 - SIM_START, 2]), 3) if 100 >= SIM_START else None,
    "play_z_f150": round(float(rec_play[150 - SIM_START, 2]), 3),
    "play_z_f250": round(float(rec_play[250 - SIM_START, 2]), 3),
    "play_z_f299": round(float(rec_play[NF - 1 - SIM_START, 2]), 3),
}
base = np.array([marble_rest(i, j) for o, i, j in marbles], np.float32)
d_final = np.linalg.norm(rec[-1, :, :2] - base[:, :2], axis=1)
d_max_mid = np.linalg.norm(rec[150 - SIM_START, :, :2] - base[:, :2], axis=1)
stats["marbles_moved_gt_03"] = int((d_final > 0.3).sum())
stats["marbles_moved_gt_10"] = int((d_final > 1.0).sum())
stats["max_radial_disp"] = round(float(d_final.max()), 3)
stats["max_radial_disp_mid_f150"] = round(float(d_max_mid.max()), 3)
# sample table: a few marbles before/after
sample = []
for mi in (0, 48, 97, 146, 194):
    o, i, j = marbles[mi]
    sample.append({"name": o.name, "base": [round(float(x), 3) for x in base[mi]],
                   "final": [round(float(x), 3) for x in rec[-1, mi]]})
stats["sample_marbles"] = sample
stats["timing_sim_s"] = round(sim_dur, 1)
stats["build_s"] = round(time.time() - T0, 1)
json.dump(stats, open(os.path.join(CHK, "bake_stats.json"), "w"), indent=1)

# post-bake verification: keyframes (not physics) drive the scene now
sc.frame_set(200)
bpy.context.view_layer.update()
m0 = marbles[0][0]
k200 = 200 - SIM_START
dv = (__import__('mathutils').Vector(rec[k200, 0]) - m0.location).length
log("post-bake check: marble0 delta at f200 = %.6f" % dv)
sc.frame_start = 0
sc.frame_end = NF - 1
sc.frame_set(0)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(BASE, "scene.blend"), compress=True)
log("saved scene.blend; stats:", json.dumps(stats)[:400])
print("BUILD_DONE")
