"""Probe 8: decisive tests for card-01 requirements.
(a) motion blur with object actually in frame  (b) EEVEE raytracing -> glass refraction
(c) soft-body squash on landing WITH collision modifier  (d) rigid bodies pushing neighbours apart
"""
import bpy, json, time, traceback, os, math
import numpy as np

R = {"steps": []}
def step(name, fn):
    t = time.time()
    try:
        r = fn()
        R["steps"].append({"name": name, "ok": True, "secs": round(time.time()-t, 2), "result": r})
    except Exception as e:
        R["steps"].append({"name": name, "ok": False, "secs": round(time.time()-t, 2),
                           "error": "%s: %s" % (type(e).__name__, e), "tb": traceback.format_exc()[-400:]})

def grab(p):
    im = bpy.data.images.load(p)
    a = np.empty(len(im.pixels), dtype=np.float32); im.pixels.foreach_get(a)
    bpy.data.images.remove(im)
    return a

def base_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    cd = bpy.data.cameras.new("Cam"); co = bpy.data.objects.new("Cam", cd)
    sc.collection.objects.link(co); co.location = (0, -9, 2.2)
    co.rotation_euler = (math.radians(80), 0, 0)
    sc.camera = co
    ld = bpy.data.lights.new("Key", type="AREA"); ld.size = 8.0; ld.energy = 1500
    lo = bpy.data.objects.new("Key", ld); sc.collection.objects.link(lo)
    lo.location = (-5, -6, 8); lo.rotation_euler = (0.7, 0, -0.6)
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 16
    sc.render.resolution_x = 480; sc.render.resolution_y = 270
    sc.render.image_settings.file_format = "PNG"
    sc.render.fps = 30
    return sc

# ---------------- (a) motion blur, object IN FRAME ----------------
def f_mb():
    sc = base_scene()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(-2.0, 0, 1.2))
    ball = bpy.context.active_object; ball.name = "Ball"
    m = bpy.data.materials.new("M"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (1, 0.2, 0.1, 1)
    ball.data.materials.append(m)
    # move across the visible centre in 2 frames
    ball.location = (-2.0, 0, 1.2); ball.keyframe_insert("location", frame=1)
    ball.location = (2.0, 0, 1.2); ball.keyframe_insert("location", frame=2)
    sc.frame_set(2)
    sc.eevee.motion_blur_steps = 16
    res = {}
    for tag, mb in (("off", False), ("on", True)):
        sc.render.use_motion_blur = mb
        p = os.path.abspath("_mb2_%s.png" % tag)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        a = grab(p)
        res[tag] = {"bytes": os.path.getsize(p), "std": round(float(a.std()), 5), "arr": a}
    d = float(np.abs(res["on"]["arr"] - res["off"]["arr"]).mean())
    mx = float(np.abs(res["on"]["arr"] - res["off"]["arr"]).max())
    res["off"].pop("arr"); res["on"].pop("arr")
    return {"off": res["off"], "on": res["on"], "mean_abs_pixel_diff": round(d, 6),
            "max_abs_pixel_diff": round(mx, 5), "motion_blur_changes_image": d > 1e-5}
step("a_motion_blur_in_frame", f_mb)

# ---------------- (b) EEVEE raytracing -> glass refraction ----------------
def f_glass():
    sc = base_scene()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.2, location=(0, 0, 1.2))
    sph = bpy.context.active_object; sph.name = "Glass"
    bpy.ops.object.shade_smooth()
    m = bpy.data.materials.new("Glass"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (1, 1, 1, 1)
    b.inputs["Roughness"].default_value = 0.02
    b.inputs["IOR"].default_value = 1.45
    b.inputs["Transmission Weight"].default_value = 1.0
    sph.data.materials.append(m)
    # a colourful backdrop so refraction is visible
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 6, 1.2), rotation=(math.radians(90), 0, 0))
    bd = bpy.context.active_object
    mb = bpy.data.materials.new("Back"); mb.use_nodes = True
    nt = mb.node_tree
    tex = nt.nodes.new("ShaderNodeTexChecker"); tex.inputs["Scale"].default_value = 6
    tex.inputs["Color1"].default_value = (0.1, 0.3, 0.9, 1)
    tex.inputs["Color2"].default_value = (0.95, 0.75, 0.1, 1)
    nt.links.new(tex.outputs["Color"], nt.nodes["Principled BSDF"].inputs["Base Color"])
    bd.data.materials.append(mb)
    # materials need blend settings for transmission in EEVEE
    try:
        m.surface_render_method = "BLENDED"
        r = {"surface_render_method": m.surface_render_method,
             "options": [i.identifier for i in m.bl_rna.properties["surface_render_method"].enum_items]}
    except Exception as e:
        r = {"surface_render_method_err": str(e)}
    res = {}
    for tag, rt in (("rt_off", False), ("rt_on", True)):
        sc.eevee.use_raytracing = rt
        sc.render.use_motion_blur = False
        p = os.path.abspath("_glass_%s.png" % tag)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        a = grab(p)
        res[tag] = {"bytes": os.path.getsize(p), "arr": a}
    d = float(np.abs(res["rt_on"]["arr"] - res["rt_off"]["arr"]).mean())
    for k in res: res[k].pop("arr")
    r.update({"eevee_raytracing_default": False, "raytracing_off": res["rt_off"], "raytracing_on": res["rt_on"],
              "mean_abs_pixel_diff": round(d, 6), "raytracing_changes_image": d > 1e-5})
    return r
step("b_eevee_raytracing_glass", f_glass)

# ---------------- (c) soft body squash on landing WITH collision ----------------
def f_squash():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=20)
    floor = bpy.context.active_object; floor.name = "Floor"
    cm = floor.modifiers.new("Collision", "COLLISION")
    cm.settings.thickness_outer = 0.02
    # high-poly cube so soft body has enough verts to deform
    bpy.ops.mesh.primitive_cube_add(size=1.2, location=(0, 0, 1.6))
    cube = bpy.context.active_object; cube.name = "Soft"
    bpy.ops.object.modifier_add(type="SUBSURF")
    cube.modifiers["Subdivision"].levels = 3
    bpy.ops.object.modifier_apply(modifier="Subdivision")
    nverts = len(cube.data.vertices)
    sb = cube.modifiers.new("SoftBody", "SOFT_BODY")
    st = sb.settings
    st.use_goal = False
    st.mass = 0.4
    st.friction = 0.8
    st.bend = 0.5
    st.plastic = 0.0
    st.use_edges = True
    sc.frame_start = 1; sc.frame_end = 30
    bpy.ops.ptcache.bake_all(bake=True)
    samples = []
    for f in (1, 8, 12, 16, 22, 30):
        sc.frame_set(f); bpy.context.view_layer.update()
        dg = bpy.context.evaluated_depsgraph_get()
        me = cube.evaluated_get(dg).to_mesh()
        zs = [v.co.z for v in me.vertices]
        samples.append({"f": f, "min_z": round(min(zs), 3), "max_z": round(max(zs), 3),
                        "height": round(max(zs) - min(zs), 3)})
        cube.evaluated_get(dg).to_mesh_clear()
    return {"cube_verts": nverts, "samples": samples,
            "rest_height": 1.2, "note": "height < rest_height right after impact == squash"}
step("c_softbody_squash_on_collision_floor", f_squash)

# ---------------- (d) rigid bodies push neighbours apart ----------------
def f_push():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=30)
    floor = bpy.context.active_object; floor.name = "Floor"
    bpy.ops.rigidbody.world_add()
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
    # grid of marbles
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
    # a heavy PLAY block dropped in the middle
    bpy.ops.mesh.primitive_cube_add(size=1.4, location=(0, 0, 6))
    blk = bpy.context.active_object; blk.name = "PlayBlock"
    bpy.context.view_layer.objects.active = blk
    bpy.ops.rigidbody.object_add()
    blk.rigid_body.type = "ACTIVE"; blk.rigid_body.mass = 8.0; blk.rigid_body.restitution = 0.5
    blk.rigid_body.friction = 0.6
    sc.frame_start = 1; sc.frame_end = 90
    before = {o.name: (round(o.location.x, 3), round(o.location.y, 3)) for o in protos[:5]}
    # manual bake: step frames so the sim evaluates
    for f in range(1, 91):
        sc.frame_set(f)
        bpy.context.view_layer.update()
    after = {o.name: (round(o.location.x, 3), round(o.location.y, 3)) for o in protos[:5]}
    moved = 0
    dists = []
    for o in protos:
        d = ((o.matrix_world.translation.x) ** 2 + (o.matrix_world.translation.y) ** 2) ** 0.5
        dists.append(round(d, 3))
    for o in protos:
        d = ((o.matrix_world.translation.x) ** 2 + (o.matrix_world.translation.y) ** 2) ** 0.5
        if d > 1.0: moved += 1
    blk_z = round(blk.matrix_world.translation.z, 3)
    return {"marbles": len(protos), "block_rest_z": blk_z,
            "sample_before": before, "sample_after": after,
            "marbles_pushed_beyond_1u_radius": moved,
            "max_radial_distance": max(dists)}
step("d_rigidbody_push_neighbours", f_push)

with open("_probe8_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE8_DONE")
