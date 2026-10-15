import bpy, json, math, os
import numpy as np
V = os.environ.get("VAR","X1")

def c0_setup():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=30)
    bpy.ops.rigidbody.world_add()
    floor = bpy.context.active_object
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.25, location=(0, 0, 0.25))
    proto = bpy.context.active_object; proto.name = "Proto"
    bpy.context.view_layer.objects.active = proto
    bpy.ops.rigidbody.object_add()
    proto.rigid_body.type = "ACTIVE"; proto.rigid_body.mass = 0.2; proto.rigid_body.restitution = 0.3
    protos = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            o = proto.copy(); o.data = proto.data
            o.location = (i * 0.6, j * 0.6, 0.25)
            sc.collection.objects.link(o); protos.append(o)
    bpy.ops.mesh.primitive_cube_add(size=1.4, location=(0, 0, 6))
    blk = bpy.context.active_object
    bpy.context.view_layer.objects.active = blk
    bpy.ops.rigidbody.object_add()
    blk.rigid_body.type = "ACTIVE"; blk.rigid_body.mass = 8.0; blk.rigid_body.restitution = 0.5
    blk.rigid_body.friction = 0.6
    return sc, blk, protos

def read(sc, blk, protos):
    blk_z = round(blk.matrix_world.translation.z, 3)
    dists = [round(((o.matrix_world.translation.x)**2 + (o.matrix_world.translation.y)**2)**0.5, 3) for o in protos]
    return {"block_rest_z": blk_z, "max_radial": max(dists)}

if V == "X1":
    sc, blk, protos = c0_setup()
    sc.frame_start = 1; sc.frame_end = 90
    rw = sc.rigidbody_world
    rw.point_cache.frame_start = 1; rw.point_cache.frame_end = 90
    bpy.ops.ptcache.bake_all(bake=True)
    for f in range(1, 91):
        sc.frame_set(f); bpy.context.view_layer.update()
    print("X1 (bake flow):", json.dumps(read(sc, blk, protos)))

if V == "X3":
    # full-scene-like: 165 marbles + text PLAY, scrub from frame 1
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=300)
    bpy.ops.rigidbody.world_add()
    floor = bpy.context.active_object
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"; floor.rigid_body.friction=0.6
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=0.25)
    proto = bpy.context.active_object
    bpy.context.view_layer.objects.active = proto
    bpy.ops.rigidbody.object_add()
    rb = proto.rigid_body; rb.type="ACTIVE"; rb.mass=0.2; rb.friction=0.65; rb.restitution=0.42
    rb.linear_damping=0.08; rb.angular_damping=0.5
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
    rb.mass=8; rb.friction=0.8; rb.restitution=0.5; rb.linear_damping=0.015; rb.angular_damping=0.8
    sc.frame_start=1; sc.frame_end=299
    base = np.array([o.location[:] for o in marbles])
    for f in range(1, 130):
        sc.frame_set(f); bpy.context.view_layer.update()
    disp = max(math.hypot(o.matrix_world.translation.x-base[k,0], o.matrix_world.translation.y-base[k,1]) for k,o in enumerate(marbles))
    print("X3 (full scene scrub):", json.dumps({"play_z": round(play.matrix_world.translation.z,3), "max_disp": round(disp,3)}))
