import bpy, json, os
V = os.environ.get("VAR", "C0")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
bpy.ops.mesh.primitive_plane_add(size=30)
bpy.ops.rigidbody.world_add()
floor = bpy.context.active_object
bpy.context.view_layer.objects.active = floor
bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
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

def rbinfo(o):
    rb = o.rigid_body
    if rb is None: return "NO_RB"
    return {"en": rb.enabled, "type": rb.type, "kin": rb.kinematic, "mass": round(rb.mass,3),
            "shape": rb.collision_shape, "deact": rb.use_deactivation, "start_deact": rb.use_start_deactivated,
            "hv": o.hide_viewport, "hr": o.hide_render}

rw = sc.rigidbody_world
col = rw.collection
print("VAR", V)
print("  rw.collection objects:", len(col.objects) if col else None, sorted([o.name for o in col.objects])[:6] if col else None)
print("  proto exists:", "Proto" in bpy.data.objects)
print("  proto rb:", rbinfo(bpy.data.objects["Proto"]) if "Proto" in bpy.data.objects else "gone")
print("  marble.001 rb:", rbinfo(bpy.data.objects["Proto.001"]))
print("  marble.002 rb:", rbinfo(bpy.data.objects["Sphere.002"]))

print("  rw:", {k: getattr(rw,k) for k in ("substeps_per_frame","solver_iterations","time_scale","use_split_impulse","friction_collection") if hasattr(rw,k)})
# quick sim check
sc.frame_start = 1; sc.frame_end = 90
for f in range(1, 91):
    sc.frame_set(f); bpy.context.view_layer.update()
print("  after: Proto.001 xy:", [round(v,3) for v in bpy.data.objects["Proto.001"].matrix_world.translation[:2]],
      "| Proto.025 xy:", [round(v,3) for v in bpy.data.objects["Proto.025"].matrix_world.translation[:2]])
