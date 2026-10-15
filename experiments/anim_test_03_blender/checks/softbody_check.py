"""checks/softbody_check.py — dedicated verification: 软体压扁 + 地面碰撞 (soft-body squash on collision floor).
Run: blender -b --factory-startup -P checks/softbody_check.py
A: probe9 cube recipe (baseline). B: the film's PLAY letter mesh (subsurf 1) dropped on a collision floor.
"""
import bpy, os, math, json, time
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OD = os.path.join(BASE, "checks", "mech")
os.makedirs(OD, exist_ok=True)

def setup(sc):
    bpy.ops.mesh.primitive_plane_add(size=30)
    floor = bpy.context.active_object
    cm = floor.modifiers.new("Collision", "COLLISION")
    cm.settings.thickness_outer = 0.02
    sc.render.engine = 'BLENDER_EEVEE'
    sc.eevee.taa_render_samples = 16
    sc.render.resolution_x, sc.render.resolution_y = 480, 270
    sc.render.image_settings.file_format = 'PNG'
    cd = bpy.data.cameras.new("C"); co = bpy.data.objects.new("C", cd)
    sc.collection.objects.link(co)
    co.location = (0, -5, 1.9); co.rotation_euler = (math.radians(80), 0, 0)
    sc.camera = co
    ld = bpy.data.lights.new("K", 'AREA'); ld.size = 5; ld.energy = 800
    lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo)
    lo.location = (-3, -3, 5)
    return floor

def softbody(ob, mass=0.5, bend=0.8):
    sb = ob.modifiers.new("SoftBody", "SOFT_BODY")
    st = sb.settings
    st.use_goal = False
    st.mass = mass
    st.friction = 0.9
    st.bend = bend
    st.plastic = 0
    st.ball_stiff = 10.0
    st.ball_damp = 0.5
    st.use_edges = True
    return sb

# ---------------- A. cube baseline
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
setup(sc)
bpy.ops.mesh.primitive_cube_add(size=1.2, location=(0, 0, 1.4))
cube = bpy.context.active_object
bpy.ops.object.modifier_add(type="SUBSURF")
cube.modifiers["Subdivision"].levels = 3
bpy.ops.object.modifier_apply(modifier="Subdivision")
softbody(cube)
sc.frame_start = 1; sc.frame_end = 40
bpy.ops.ptcache.bake_all(bake=True)
samples = []
for f in (1, 6, 10, 14, 20, 30, 40):
    sc.frame_set(f); bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = cube.evaluated_get(dg)
    me = ev.to_mesh()
    zs = [v.co.z for v in me.vertices]
    samples.append({"f": f, "min_z": round(min(zs), 3), "max_z": round(max(zs), 3), "height": round(max(zs) - min(zs), 3)})
    ev.to_mesh_clear()
print("CUBE_SAMPLES:", json.dumps(samples), flush=True)
for f in (1, 20):
    sc.frame_set(f)
    sc.render.filepath = os.path.join(OD, "softbody_cube_f%02d.png" % f)
    bpy.ops.render.render(write_still=True)
print("CUBE_DONE", flush=True)

# ---------------- B. PLAY letter mesh
t0 = time.time()
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
setup(sc)
bpy.ops.object.text_add()
t = bpy.context.active_object
t.data.body = "PLAY"; t.data.size = 1; t.data.extrude = 0.3
t.data.bevel_depth = 0.07; t.data.bevel_resolution = 4
bpy.ops.object.convert(target='MESH')
play = bpy.context.active_object
me = play.data
n = len(me.vertices)
co = np.empty(n * 3, np.float32); me.vertices.foreach_get("co", co); co = co.reshape(-1, 3)
s_ = 2.55 / (co[:, 0].max() - co[:, 0].min())
co[:, 0] = (co[:, 0] - (co[:, 0].min() + co[:, 0].max()) / 2) * s_
co[:, 1] = (co[:, 1] - co[:, 1].min()) * s_
co[:, 2] = (co[:, 2] - (co[:, 2].min() + co[:, 2].max()) / 2) * s_
me.vertices.foreach_set("co", co.ravel()); me.update()
bpy.ops.object.modifier_add(type="SUBSURF")
play.modifiers["Subdivision"].levels = 1
bpy.ops.object.modifier_apply(modifier="Subdivision")
nv = len(play.data.vertices)
play.rotation_euler = (math.pi / 2, 0, 0)
play.location = (0, 0, 2.6)
softbody(play, mass=0.6, bend=1.0)
sc.frame_start = 1; sc.frame_end = 50
bpy.ops.ptcache.bake_all(bake=True)
rows = []
hmin = 1e9; minz = 1e9
for f in range(1, 51):
    sc.frame_set(f); bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = play.evaluated_get(dg)
    mev = ev.to_mesh()
    zs = [v.co.z for v in mev.vertices]
    h = max(zs) - min(zs)
    hmin = min(hmin, h); minz = min(minz, min(zs))
    if f % 5 == 0:
        rows.append({"f": f, "height": round(h, 3), "min_z": round(min(zs), 3)})
    ev.to_mesh_clear()
print("PLAY_VERTS:", nv, "| bake %.1fs" % (time.time() - t0), flush=True)
print("PLAY_SAMPLES:", json.dumps(rows), flush=True)
print("PLAY_MIN_HEIGHT:", round(hmin, 3), "| PLAY_MIN_Z:", round(minz, 3), flush=True)
for f in (1, 22, 36):
    sc.frame_set(f)
    sc.render.filepath = os.path.join(OD, "softbody_play_f%02d.png" % f)
    bpy.ops.render.render(write_still=True)
print("SOFTBODY_DONE", flush=True)
