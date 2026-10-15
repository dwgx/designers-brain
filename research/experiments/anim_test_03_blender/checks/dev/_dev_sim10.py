import bpy, json, math, os
import numpy as np
V = os.environ.get("VAR","Y1")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
bpy.ops.mesh.primitive_plane_add(size=300)
bpy.ops.rigidbody.world_add()
floor = bpy.context.active_object
bpy.context.view_layer.objects.active = floor
bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"; floor.rigid_body.friction=0.6

fric_m, rest_m, ld_m, ad_m = (0.65, 0.42, 0.08, 0.5)
spacing = 0.56
NI, NJ = 15, 11
use_cube = False
proto_park = True
if V == "Y1": fric_m, rest_m, ld_m, ad_m = (0.5, 0.3, 0.04, 0.1)
if V == "Y2": spacing = 0.62
if V == "Y3": use_cube = True
if V == "Y4": proto_park = False
if V == "Y5":
    sc.rigidbody_world.substeps_per_frame = 40; sc.rigidbody_world.solver_iterations = 40

bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.25)
proto = bpy.context.active_object
bpy.context.view_layer.objects.active = proto
bpy.ops.rigidbody.object_add()
rb = proto.rigid_body; rb.type="ACTIVE"; rb.mass=0.2; rb.friction=fric_m; rb.restitution=rest_m
rb.linear_damping=ld_m; rb.angular_damping=ad_m
marbles=[]
for i in range(NI):
    for j in range(NJ):
        o = proto.copy(); o.data = proto.data
        o.location = ((i-(NI-1)/2)*spacing, (j-(NJ-1)/2)*spacing, 0.25)
        sc.collection.objects.link(o); marbles.append(o)
if proto_park:
    proto.location = (0,0,-60)
    proto.hide_render=True

if use_cube:
    bpy.ops.mesh.primitive_cube_add(size=1.4, location=(0,0,4.2))
    play = bpy.context.active_object
else:
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
rb.mass=8; rb.friction=0.8; rb.restitution=0.5; rb.linear_damping=0.015; rb.angular_damping=0.8

sc.frame_start=1; sc.frame_end=299
base = np.array([o.location[:] for o in marbles])
for f in range(1, 130):
    sc.frame_set(f); bpy.context.view_layer.update()
disp = max(math.hypot(o.matrix_world.translation.x-base[k,0], o.matrix_world.translation.y-base[k,1]) for k,o in enumerate(marbles))
print("VAR", V, json.dumps({"play_z": round(play.matrix_world.translation.z,3), "max_disp": round(disp,3)}))
