"""Probe 7: physics + light + render defaults; verify motion blur changes pixels; soft body; seamless backdrop."""
import bpy, json, time, traceback, os, math

R = {"steps": []}
def step(name, fn):
    t = time.time()
    try:
        r = fn()
        R["steps"].append({"name": name, "ok": True, "secs": round(time.time()-t, 2), "result": r})
    except Exception as e:
        R["steps"].append({"name": name, "ok": False, "secs": round(time.time()-t, 2),
                           "error": "%s: %s" % (type(e).__name__, e), "tb": traceback.format_exc()[-400:]})

def f_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    # seamless studio backdrop: a big curved cyclorama (plane with bevel) + area light
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
    floor = bpy.context.active_object; floor.name = "Floor"
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 12, 10), rotation=(math.radians(90), 0, 0))
    back = bpy.context.active_object; back.name = "BackWall"
    # bezier-ish: add a cube and bevel for the cove
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 12, 0.5))
    cove = bpy.context.active_object; cove.name = "Cove"
    cove.scale = (20, 0.5, 0.5)
    b = cove.modifiers.new("Bevel", "BEVEL"); b.width = 0.4; b.segments = 12
    # marble
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.35, location=(0, 0, 3))
    ball = bpy.context.active_object; ball.name = "Ball"
    # camera
    cd = bpy.data.cameras.new("Cam"); co = bpy.data.objects.new("Cam", cd)
    sc.collection.objects.link(co); co.location = (0, -9, 2.2); co.rotation_euler = (math.radians(78), 0, 0)
    sc.camera = co
    # light
    ld = bpy.data.lights.new("Key", type="AREA"); lo = bpy.data.objects.new("Key", ld)
    sc.collection.objects.link(lo); lo.location = (-5, -6, 8)
    return {"objects": [o.name for o in bpy.data.objects], "camera_lens_mm": cd.lens, "sensor_width": cd.sensor_width}
step("setup_scene", f_scene)

def f_defaults():
    sc = bpy.context.scene
    ball = bpy.data.objects["Ball"]
    bpy.ops.rigidbody.world_add()
    bpy.context.view_layer.objects.active = ball
    bpy.ops.rigidbody.object_add()
    rb = ball.rigid_body
    r = {k: getattr(rb, k) for k in ("type","mass","friction","restitution","linear_damping","angular_damping",
        "use_deactivation","deactivate_linear_velocity","deactivate_angular_velocity","collision_shape","collision_margin","use_margin")}
    r["world_attrs"] = sorted([p.identifier for p in sc.rigidbody_world.bl_rna.properties if not p.is_readonly])[:25]
    r["world"] = {k: getattr(sc.rigidbody_world, k, "ABSENT") for k in ("time_scale","substeps_per_frame","solver_iterations","use_split_impulse")}
    r["gravity"] = list(sc.gravity)
    # light defaults
    ld = bpy.data.lights["Key"]
    r["light"] = {"type": ld.type, "size": ld.size, "shape": ld.shape, "energy": ld.energy,
                  "shadow_soft_size": ld.shadow_soft_size, "spread": ld.spread}
    # camera dof
    r["cam_dof"] = {"use_dof": sc.camera.data.dof.use_dof, "focus_distance": sc.camera.data.dof.focus_distance,
                    "aperture_fstop": sc.camera.data.dof.aperture_fstop, "aperture_blades": sc.camera.data.dof.aperture_blades,
                    "focus_object": sc.camera.data.dof.focus_object}
    # eevee
    r["eevee"] = {k: getattr(sc.eevee, k, "ABSENT") for k in
                  ("taa_render_samples","use_shadows","use_raytracing","use_fast_gi","shadow_ray_count","shadow_step_count","motion_blur_steps","motion_blur_max")}
    r["render_mb"] = {"use_motion_blur": sc.render.use_motion_blur, "motion_blur_shutter": sc.render.motion_blur_shutter}
    r["render"] = {"film_transparent": sc.render.film_transparent, "filter_size": sc.render.filter_size,
                   "use_simplify": sc.render.use_simplify, "threads_mode": sc.render.threads_mode}
    return r
step("physics_light_cam_eevee_defaults", f_defaults)

def f_motion_blur_pixel_test():
    """Render the same fast-moving frame with MB off and on; compare PNG bytes + pixel diff."""
    import numpy as np
    sc = bpy.context.scene
    ball = bpy.data.objects["Ball"]
    # strong horizontal motion so blur is visible
    ball.location = (-6, 0, 1.0); ball.keyframe_insert("location", frame=1)
    ball.location = (6, 0, 1.0); ball.keyframe_insert("location", frame=2)
    # remove rigid body so it doesn't fight the keys
    bpy.context.view_layer.objects.active = ball
    try: bpy.ops.rigidbody.object_remove()
    except Exception: pass
    sc.frame_set(2)
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 16
    sc.eevee.motion_blur_steps = 16
    sc.render.resolution_x = 480; sc.render.resolution_y = 270
    sc.render.image_settings.file_format = "PNG"
    out = {}
    for tag, mb in (("off", False), ("on", True)):
        sc.render.use_motion_blur = mb
        p = os.path.abspath("_mb_%s.png" % tag)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        im = bpy.data.images.load(p)
        a = np.empty(len(im.pixels), dtype=np.float32); im.pixels.foreach_get(a)
        bpy.data.images.remove(im)
        out[tag] = {"bytes": os.path.getsize(p), "mean": float(a.mean()), "arr": a}
    d = float(np.abs(out["on"]["arr"] - out["off"]["arr"]).mean())
    out["off"].pop("arr"); out["on"].pop("arr")
    return {"off": out["off"], "on": out["on"], "mean_abs_pixel_diff": round(d, 6),
            "motion_blur_changes_image": d > 1e-5}
step("motion_blur_pixel_evidence", f_motion_blur_pixel_test)

def f_soft_body():
    bpy.ops.mesh.primitive_cube_add(size=1.2, location=(0, 0, 4))
    cube = bpy.context.active_object; cube.name = "SoftCube"
    bpy.ops.object.shade_smooth()
    m = cube.modifiers.new("SoftBody", "SOFT_BODY")
    sb = cube.modifiers["SoftBody"].settings
    sb.use_goal = False
    sb.use_edges = True
    attrs = sorted([p.identifier for p in sb.bl_rna.properties if not p.is_readonly])
    sc = bpy.context.scene
    sc.frame_start = 1; sc.frame_end = 20
    # bake soft body
    try:
        bpy.ops.ptcache.bake_all(bake=True)
        baked = "OK"
    except Exception as e:
        baked = "FAIL: %s" % e
    zs = []
    for f in (1, 10, 20):
        sc.frame_set(f); bpy.context.view_layer.update()
        dg = bpy.context.evaluated_depsgraph_get()
        ev = cube.evaluated_get(dg)
        me = ev.to_mesh()
        zs.append({"frame": f, "verts": len(me.vertices), "min_z": round(min(v.co.z for v in me.vertices), 3),
                   "max_z": round(max(v.co.z for v in me.vertices), 3)})
        ev.to_mesh_clear()
    return {"bake": baked, "settings_sample": attrs[:22], "deformed_over_time": zs,
            "note": "min_z/max_z span shows the mesh deforming (squash) — soft body deforms geometry, rigid body cannot"}
step("soft_body_squash", f_soft_body)

with open("_probe7_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE7_DONE")
