"""Probe 4: ffmpeg output path in 5.2, motion blur config, rigidbody sim + bake, keyframes, contact sheet API."""
import bpy, json, time, traceback, os

R = {"steps": []}
def step(name, fn):
    t = time.time()
    try:
        r = fn()
        R["steps"].append({"name": name, "ok": True, "secs": round(time.time()-t, 2), "result": r})
    except Exception as e:
        R["steps"].append({"name": name, "ok": False, "secs": round(time.time()-t, 2),
                           "error": "%s: %s" % (type(e).__name__, e), "tb": traceback.format_exc()[-500:]})

def f_build():
    return {"build_options_ffmpeg": getattr(bpy.app.build_options, "codec_ffmpeg", "ABSENT"),
            "build_options": [a for a in dir(bpy.app.build_options) if not a.startswith("_")],
            "image_settings_rna_id": bpy.context.scene.render.image_settings.bl_rna.identifier}
step("build_options", f_build)

def f_ffmpeg_probe():
    sc = bpy.context.scene
    iset = sc.render.image_settings
    # static enum (what probe1 read)
    static = [i.identifier for i in iset.bl_rna.properties["file_format"].enum_items]
    # dynamic: use the actual runtime filter by checking the prop's enum items via bpy.types after context
    res = {"static_enum_has_FFMPEG": "FFMPEG" in static, "static_len": len(static)}
    # try setting in default scene
    try:
        iset.file_format = "FFMPEG"
        res["set_on_scene_render"] = "OK -> " + iset.file_format
        res["ffmpeg_format_after"] = sc.render.ffmpeg.format
        res["ffmpeg_codec_after"] = sc.render.ffmpeg.codec
    except Exception as e:
        res["set_on_scene_render"] = "FAIL: %s" % e
    # alternative homes for video output?
    res["has_render_ffmpeg"] = hasattr(sc.render, "ffmpeg")
    # is there a separate "output format" for video in 5.2?
    res["render_attrs_with_video"] = [p.identifier for p in sc.render.bl_rna.properties if "video" in p.identifier.lower() or "movie" in p.identifier.lower()]
    res["scene_attrs_with_video"] = [p.identifier for p in bpy.types.Scene.bl_rna.properties if "video" in p.identifier.lower() or "movie" in p.identifier.lower()]
    return res
step("ffmpeg_output", f_ffmpeg_probe)

def f_ffmpeg_after_use_nodes():
    """maybe FFMPEG appears only when scene.use_nodes / compositing disabled? or after setting frame_end>1"""
    sc = bpy.context.scene
    sc.frame_end = 60
    try:
        sc.render.image_settings.file_format = "FFMPEG"
        return {"after_frame_end_60": "OK"}
    except Exception as e:
        return {"after_frame_end_60": "FAIL: %s" % e}
step("ffmpeg_retry", f_ffmpeg_after_use_nodes)

def f_motion_blur_cycles():
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    attrs = [p.identifier for p in sc.cycles.bl_rna.properties if not p.is_readonly]
    return {"cycles_motion_related": [a for a in attrs if "motion" in a.lower() or "blur" in a.lower() or "shutter" in a.lower() or "rolling" in a.lower()],
            "render_use_motion_blur": sc.render.use_motion_blur,
            "render_motion_blur_shutter": sc.render.motion_blur_shutter,
            "eevee_only_attrs": [a for a in dir(sc.eevee) if "motion" in a.lower()]}
step("motion_blur_detail", f_motion_blur_cycles)

def f_rigidbody():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    # floor
    bpy.ops.mesh.primitive_plane_add(size=10)
    floor = bpy.context.active_object
    # falling sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 5))
    ball = bpy.context.active_object
    # rigid body world
    bpy.ops.rigidbody.world_add()
    # make floor passive
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add()
    floor.rigid_body.type = "PASSIVE"
    floor.rigid_body.friction = 0.8
    # make ball active
    bpy.context.view_layer.objects.active = ball
    bpy.ops.rigidbody.object_add()
    ball.rigid_body.type = "ACTIVE"
    ball.rigid_body.restitution = 0.6
    ball.rigid_body.mass = 1.0
    # bake + check
    sc.frame_start = 1; sc.frame_end = 90
    t = time.time()
    bpy.ops.ptcache.bake_all(bake=True)
    dt = time.time()-t
    # sample ball z over frames
    zs = []
    for f in (1, 20, 40, 60, 80, 90):
        sc.frame_set(f)
        zs.append(round(ball.matrix_world.translation.z, 3))
    return {"bake_secs": round(dt, 2), "ball_z_by_frame": dict(zip((1,20,40,60,80,90), zs)),
            "rb_attrs": sorted([p.identifier for p in ball.rigid_body.bl_rna.properties if not p.is_readonly])[:40]}
step("rigidbody_sim_bake", f_rigidbody)

def f_bake_to_keyframes():
    sc = bpy.context.scene
    o = bpy.data.objects.get("Sphere") or [x for x in bpy.data.objects if x.rigid_body][0]
    bpy.context.view_layer.objects.active = o
    n_before = len(o.animation_data.action.fcurves) if (o.animation_data and o.animation_data.action) else 0
    bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end=90)
    n_after = len(o.animation_data.action.fcurves) if (o.animation_data and o.animation_data.action) else 0
    return {"fcurves_before": n_before, "fcurves_after": n_after, "action": o.animation_data.action.name if o.animation_data and o.animation_data.action else None}
step("bake_physics_to_keyframes", f_bake_to_keyframes)

def f_keyframes_api():
    ob = bpy.data.objects[0]
    ob.keyframe_insert(data_path="location", frame=1)
    ob.location.z = 3
    ob.keyframe_insert(data_path="location", frame=30)
    fc = ob.animation_data.action.fcurves
    interp = [kp.interpolation for f in fc for kp in f.keyframe_points]
    return {"fcurve_count": len(fc), "interpolations": interp,
            "has_fcurve_modifiers": len(fc[0].modifiers) if fc else 0,
            "action_slots_api": hasattr(ob.animation_data, "action_slot")}
step("keyframe_api", f_keyframes_api)

def f_render_frame_sequence():
    """Render a 5-frame PNG sequence and check filenames."""
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 4
    sc.render.resolution_x = 320; sc.render.resolution_y = 180
    sc.render.image_settings.file_format = "PNG"
    sc.frame_start = 1; sc.frame_end = 5
    sc.render.filepath = os.path.abspath("_seq/f_")
    bpy.ops.render.render(animation=True)
    files = sorted(os.listdir(os.path.abspath("_seq")))
    return {"files": files, "count": len(files)}
step("render_png_sequence", f_render_frame_sequence)

def f_image_api():
    """How to load + combine images without PIL (contact sheet)."""
    import numpy as np
    p = os.path.abspath("_render_eevee_.png")
    img = bpy.data.images.load(p)
    px = np.array(img.pixels[:], dtype=np.float32)
    return {"size": list(img.size), "channels": img.channels, "array_len": int(px.size),
            "numpy_ok": True, "has_foreach_get": hasattr(img.pixels, "foreach_get"),
            "image_new_api": hasattr(bpy.data.images, "new"),
            "has_image_save": hasattr(img, "save_render") or hasattr(img, "save")}
step("image_api_numpy", f_image_api)

with open("_probe4_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE4_DONE")
