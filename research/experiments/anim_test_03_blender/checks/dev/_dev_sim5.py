import bpy, json
import numpy as np

def f_push():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=30)
    floor = bpy.context.active_object; floor.name = "Floor"
    bpy.ops.rigidbody.world_add()
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
    blk = bpy.context.active_object; blk.name = "PlayBlock"
    bpy.context.view_layer.objects.active = blk
    bpy.ops.rigidbody.object_add()
    blk.rigid_body.type = "ACTIVE"; blk.rigid_body.mass = 8.0; blk.rigid_body.restitution = 0.5
    blk.rigid_body.friction = 0.6
    sc.frame_start = 1; sc.frame_end = 90
    for f in range(1, 91):
        sc.frame_set(f)
        bpy.context.view_layer.update()
    blk_z = round(blk.matrix_world.translation.z, 3)
    dists = []
    for o in protos:
        d = ((o.matrix_world.translation.x) ** 2 + (o.matrix_world.translation.y) ** 2) ** 0.5
        dists.append(round(d, 3))
    return {"block_rest_z": blk_z, "max_radial": max(dists), "n_moved_gt2": sum(1 for d in dists if d>2.0)}
r = f_push()
print("RESULT:", json.dumps(r))
