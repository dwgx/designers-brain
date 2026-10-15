import bpy, json, math, os
import numpy as np
V = os.environ.get("VAR","Z1")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
bpy.ops.mesh.primitive_plane_add(size=300)
bpy.ops.rigidbody.world_add()
floor = bpy.context.active_object
bpy.context.view_layer.objects.active = floor
bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"; floor.rigid_body.friction=0.6

m_mass = 0.2
fric_m, rest_m, ld_m, ad_m = (0.5, 0.35, 0.04, 0.1)
b_mass = 8.0
sub = it = 10
if V == "Z2": sub = it = 40
if V == "Z3": b_mass = 30.0
if V == "Z4": m_mass = 0.05
if V == "Z5": sub = it = 40; b_mass = 30.0
sc.rigidbody_world.substeps_per_frame = sub; sc.rigidbody_world.solver_iterations = it

bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.25)
proto = bpy.context.active_object
bpy.context.view_layer.objects.active = proto
bpy.ops.rigidbody.object_add()
rb = proto.rigid_body; rb.type="ACTIVE"; rb.mass=m_mass; rb.friction=fric_m; rb.restitution=rest_m
rb.linear_damping=ld_m; rb.angular_damping=ad_m
marbles=[]
for i in range(15):
    for j in range(11):
        o = proto.copy(); o.data = proto.data
        o.location = ((i-7)*0.56, (j-5)*0.56, 0.25)
        sc.collection.objects.link(o); marbles.append(o)
proto.location = (0,0,-60); proto.hide_render=True
bpy.ops.object.text_add()
t = bpy.context.active_object
t.data.body="PLAY"; t.data.size=1; t.data.extrude=0.3; t.data.bevel_depth=0.07; t.data.bevel_resolution=4
bpy.ops.object.convert(target='MESH')
play = bpy.context.active_object
me=play.data; n=len(me.vertices); co=np.empty(n*3,np.float32); me.vertices.foreach_get("co",co); co=co.reshape(-1,3)
s=2.55/(co[:,0].max()-co[:,0].min())
co[:,0]=(co[:,0]-(co[:,0].min()+co[:,0].max())/2)*s; co[:,1]=(co[:,1]-co[:,1].min())*s; co[:,2]=(co[:,2]-(co[:,2].min()+co[:,2].max())/2)*s
me.vertices.foreach_set("co",co.ravel()); me.update()
play.rotation_euler=(math.pi/2,0,0); play.location=(0,0,4.2)
bpy.context.view_layer.objects.active=play
bpy.ops.rigidbody.object_add()
rb=play.rigid_body; rb.type='ACTIVE'; rb.collision_shape='CONVEX_HULL'
rb.mass=b_mass; rb.friction=0.6; rb.restitution=0.5; rb.linear_damping=0.015; rb.angular_damping=0.8

sc.frame_start=1; sc.frame_end=299
base = np.array([o.location[:] for o in marbles])
for f in range(1, 130):
    sc.frame_set(f); bpy.context.view_layer.update()
disp = np.array([math.hypot(o.matrix_world.translation.x-base[k,0], o.matrix_world.translation.y-base[k,1]) for k,o in enumerate(marbles)])
print("VAR", V, json.dumps({"play_z": round(play.matrix_world.translation.z,3), "max_disp": round(float(disp.max()),3),
                            "n>0.5": int((disp>0.5).sum()), "n>0.2": int((disp>0.2).sum())}))
