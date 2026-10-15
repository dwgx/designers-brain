import bpy, os, math, json
import numpy as np
BASE = os.path.dirname(os.path.abspath(__file__))
OD = os.path.join(BASE, "checks", "mech")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
bpy.ops.mesh.primitive_plane_add(size=30)
floor = bpy.context.active_object
cm = floor.modifiers.new("Collision", "COLLISION")
cm.settings.thickness_outer = 0.02

bpy.ops.object.text_add()
t = bpy.context.active_object
t.data.body = "PLAY"; t.data.size = 1; t.data.extrude = 0.3
t.data.bevel_depth = 0.07; t.data.bevel_resolution = 4
bpy.ops.object.convert(target='MESH')
play = bpy.context.active_object
me = play.data
n = len(me.vertices)
co = np.empty(n*3, np.float32); me.vertices.foreach_get("co", co); co = co.reshape(-1,3)
s_ = 2.55/(co[:,0].max()-co[:,0].min())
co[:,0]=(co[:,0]-(co[:,0].min()+co[:,0].max())/2)*s_
co[:,1]=(co[:,1]-co[:,1].min())*s_
co[:,2]=(co[:,2]-(co[:,2].min()+co[:,2].max())/2)*s_
me.vertices.foreach_set("co", co.ravel()); me.update()
bpy.ops.object.modifier_add(type="SUBSURF")
play.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_apply(modifier="Subdivision")
nv = len(play.data.vertices)
play.rotation_euler = (math.pi/2, 0, 0)
play.location = (0, 0, 2.4)
sb = play.modifiers.new("SoftBody", "SOFT_BODY")
st = sb.settings
st.use_goal = False
st.mass = 1.5
st.friction = 0.9
st.bend = 3.0
st.plastic = 0
st.ball_stiff = 3.0
st.ball_damp = 1.0
st.use_edges = True
sc.frame_start = 1; sc.frame_end = 30
bpy.ops.ptcache.bake_all(bake=True)
rows = []
for f in range(1, 31):
    sc.frame_set(f); bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = play.evaluated_get(dg)
    mev = ev.to_mesh()
    zs = [v.co.z for v in mev.vertices]
    if f % 5 == 0 or f in (1, 2):
        rows.append({"f": f, "height": round(max(zs)-min(zs),3), "min_z": round(min(zs),3)})
    ev.to_mesh_clear()
print("PLAY2_VERTS:", nv)
print("PLAY2_SAMPLES:", json.dumps(rows))
