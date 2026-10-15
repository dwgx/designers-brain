import bpy, json, os
V = os.environ.get("VAR", "C0")

def build():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    if V == "C5":
        bpy.ops.rigidbody.world_add()
        if V == "C1":
            sc.rigidbody_world.substeps_per_frame = 10
            sc.rigidbody_world.solver_iterations = 10
        bpy.ops.mesh.primitive_plane_add(size=30)
    else:
        bpy.ops.mesh.primitive_plane_add(size=30)
        bpy.ops.rigidbody.world_add()
        if V == "C1":
            sc.rigidbody_world.substeps_per_frame = 10
            sc.rigidbody_world.solver_iterations = 10
    floor = bpy.context.active_object; floor.name = "Floor"
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
    if V == "C4":
        floor.rigid_body.friction = 0.6
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.25, location=(0, 0, 0.25))
    proto = bpy.context.active_object; proto.name = "Proto"
    if V != "C3":
        bpy.context.view_layer.objects.active = proto
        bpy.ops.rigidbody.object_add()
        proto.rigid_body.type = "ACTIVE"; proto.rigid_body.mass = 0.2; proto.rigid_body.restitution = 0.3
    protos = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            o = proto.copy(); o.data = proto.data
            o.location = (i * 0.6, j * 0.6, 0.25)
            sc.collection.objects.link(o); protos.append(o)
            if V == "C3":
                bpy.context.view_layer.objects.active = o
                bpy.ops.rigidbody.object_add()
                o.rigid_body.type = "ACTIVE"; o.rigid_body.mass = 0.2; o.rigid_body.restitution = 0.3
    if V == "C2":
        bpy.data.objects.remove(proto)
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
    dists = [round(((o.matrix_world.translation.x) ** 2 + (o.matrix_world.translation.y) ** 2) ** 0.5, 3) for o in protos]
    return {"block_rest_z": blk_z, "max_radial": max(dists)}

print("VAR", V, "RESULT:", json.dumps(build()))
