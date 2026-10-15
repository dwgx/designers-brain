"""Why didn't the rigid sim advance? Test variants."""
import bpy, time, json

R = {}
def setup():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.rigidbody.world_add()
    rw = sc.rigidbody_world
    bpy.ops.mesh.primitive_plane_add(size=50)
    fl = bpy.context.active_object
    bpy.context.view_layer.objects.active = fl
    bpy.ops.rigidbody.object_add(); fl.rigid_body.type='PASSIVE'
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0,0,5))
    cube = bpy.context.active_object
    bpy.context.view_layer.objects.active = cube
    bpy.ops.rigidbody.object_add()
    rb = cube.rigid_body
    rb.type='ACTIVE'
    return sc, rw, cube

def probe(name, pre_update, start, n, deact, extra_bake=False):
    sc, rw, cube = setup()
    if deact:
        cube.rigid_body.use_deactivation = True
        cube.rigid_body.deactivate_linear_velocity = 0.12
        cube.rigid_body.deactivate_angular_velocity = 0.2
    sc.frame_start = start; sc.frame_end = start+n
    if pre_update:
        bpy.context.view_layer.update()
    if extra_bake:
        try:
            bpy.ops.ptcache.bake_all(bake=True)
            R[name+"_bake"] = "OK"
        except Exception as e:
            R[name+"_bake"] = str(e)
    zs = []
    t0=time.time()
    for f in range(start, start+n+1):
        sc.frame_set(f)
        bpy.context.view_layer.update()
        zs.append(round(cube.matrix_world.translation.z,3))
    R[name] = {"gravity": list(sc.gravity), "z_series": zs[::max(1,n//8)], "secs": round(time.time()-t0,2),
               "enabled": cube.rigid_body.enabled, "kinematic": cube.rigid_body.kinematic}

probe("v1_default_start1", False, 1, 40, False)
probe("v2_deact_start1", False, 1, 40, True)
probe("v3_deact_start72", False, 72, 40, True)
probe("v4_deact_start72_preupd", True, 72, 40, True)
probe("v5_deact_start72_bake", True, 72, 40, True, extra_bake=True)
probe("v6_default_start72_preupd", True, 72, 40, False)

print("SIMTEST_DONE")
json.dump(R, open("_dev_sim_test_out.json","w"), indent=1, default=str)
