"""Round 2: point_cache range + bake variants."""
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
    cube.rigid_body.type='ACTIVE'
    return sc, rw, cube

def read_zs(sc, cube, start, n, step=5):
    zs = []
    for f in range(start, start+n+1, step):
        sc.frame_set(f)
        bpy.context.view_layer.update()
        zs.append(round(cube.matrix_world.translation.z,3))
    return zs

# v7: set point_cache range, no bake, scrub
sc, rw, cube = setup()
sc.frame_start=72; sc.frame_end=112
rw.point_cache.frame_start = 72; rw.point_cache.frame_end = 112
R["v7_pc_range_scrub"] = {"pc": [rw.point_cache.frame_start, rw.point_cache.frame_end], "z": read_zs(sc,cube,72,40)}

# v8: set point_cache range + bake_all, then read
sc, rw, cube = setup()
sc.frame_start=72; sc.frame_end=112
rw.point_cache.frame_start = 72; rw.point_cache.frame_end = 112
try:
    bpy.ops.ptcache.bake_all(bake=True); R["v8_bake"]="OK"
except Exception as e:
    R["v8_bake"]=str(e)
R["v8_pc_range_bake"] = {"z": read_zs(sc,cube,72,40)}

# v9: like v8 but read from 72..112 every 5 incl first frames
sc, rw, cube = setup()
sc.frame_start=72; sc.frame_end=112
rw.point_cache.frame_start = 72; rw.point_cache.frame_end = 112
try:
    bpy.ops.ptcache.bake_all(bake=True); R["v9_bake"]="OK"
except Exception as e:
    R["v9_bake"]=str(e)
zs = []
for f in range(72, 113):
    sc.frame_set(f); bpy.context.view_layer.update()
    zs.append(round(cube.matrix_world.translation.z,3))
R["v9_z_all"] = zs

# v10: no pc change; bake_all only (default range), start scene at 72
sc, rw, cube = setup()
sc.frame_start=72; sc.frame_end=112
try:
    bpy.ops.ptcache.bake_all(bake=True); R["v10_bake"]="OK"
except Exception as e:
    R["v10_bake"]=str(e)
R["v10_z"] = read_zs(sc,cube,72,40)
R["v10_pc"] = [rw.point_cache.frame_start, rw.point_cache.frame_end]

print("SIMTEST2_DONE")
json.dump(R, open("_dev_sim_test2_out.json","w"), indent=1, default=str)
