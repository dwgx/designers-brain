"""Probe 5: Blender 5.2 animation API (slotted actions) + sequence render + bake workaround."""
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

def f_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(0, 0, 1.5))
    ball = bpy.context.active_object
    cd = bpy.data.cameras.new("Cam"); co = bpy.data.objects.new("Cam", cd)
    sc.collection.objects.link(co); co.location = (0, -5, 1.5); co.rotation_euler = (1.5708, 0, 0)
    sc.camera = co
    ld = bpy.data.lights.new("K", type="AREA"); ld.size = 3; ld.energy = 300
    lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo); lo.location = (2, -3, 4)
    sc.frame_start = 1; sc.frame_end = 10
    sc.render.fps = 30
    sc.render.resolution_x = 320; sc.render.resolution_y = 180
    return {"objects": [o.name for o in bpy.data.objects]}
step("setup", f_scene)

def f_keyframe():
    ob = bpy.data.objects["Sphere"]
    ob.keyframe_insert(data_path="location", frame=1)
    ob.location.z = 3.0
    ob.keyframe_insert(data_path="location", frame=30)
    ad = ob.animation_data
    act = ad.action
    res = {"action_name": act.name,
           "action_attrs": [a for a in dir(act) if not a.startswith("_")][:60],
           "has_fcurves_attr": hasattr(act, "fcurves"),
           "has_layers": hasattr(act, "layers"),
           "has_slots": hasattr(act, "slots")}
    if hasattr(act, "layers"):
        res["n_layers"] = len(act.layers)
        if len(act.layers):
            lay = act.layers[0]
            res["layer_attrs"] = [a for a in dir(lay) if not a.startswith("_")][:30]
            res["n_strips"] = len(lay.strips)
            if len(lay.strips):
                st = lay.strips[0]
                res["strip_attrs"] = [a for a in dir(st) if not a.startswith("_")][:30]
                # channelbag is the 4.4+ home of fcurves
                try:
                    res["has_channelbags"] = hasattr(st, "channelbags")
                    if hasattr(st, "channelbags"):
                        cbs = st.channelbags
                        res["n_channelbags"] = len(cbs)
                        if len(cbs):
                            cb = cbs[0]
                            res["channelbag_attrs"] = [a for a in dir(cb) if not a.startswith("_")][:30]
                            res["n_fcurves"] = len(cb.fcurves)
                            res["fcurve0"] = cb.fcurves[0].data_path if len(cb.fcurves) else None
                            res["n_keyframes"] = len(cb.fcurves[0].keyframe_points) if len(cb.fcurves) else 0
                            res["interp"] = cb.fcurves[0].keyframe_points[0].interpolation if len(cb.fcurves) else None
                except Exception as e:
                    res["channelbag_err"] = "%s: %s" % (type(e).__name__, e)
        res["n_slots"] = len(act.slots) if hasattr(act, "slots") else "n/a"
        if hasattr(act, "slots") and len(act.slots):
            res["slot0"] = {"identifier": act.slots[0].identifier, "name_display": getattr(act.slots[0], "name_display", None),
                            "target_id_type": getattr(act.slots[0], "target_id_type", None)}
        res["action_slot_attr"] = getattr(ad, "action_slot", "ABSENT") is not None
    return res
step("keyframe_slotted_action_api", f_keyframe)

def f_fcurve_modifiers_and_interp():
    ob = bpy.data.objects["Sphere"]
    cb = ob.animation_data.action.layers[0].strips[0].channelbags[0]
    fc = cb.fcurves[0]
    # add an ease/back interpolation + a noise modifier to demo
    for kp in fc.keyframe_points:
        kp.interpolation = "BACK"
        kp.easing = "EASE_OUT"
    fc.update()
    m = fc.modifiers.new(type="NOISE")
    return {"interpolation_set": [kp.interpolation for kp in fc.keyframe_points],
            "easing": [kp.easing for kp in fc.keyframe_points],
            "modifier_added": m.type,
            "modifier_types_avail": [i.identifier for i in fc.modifiers.bl_rna.properties["type"].enum_items] if hasattr(fc.modifiers, "bl_rna") else "n/a"}
step("fcurve_interp_and_modifiers", f_fcurve_modifiers_and_interp)

def f_bake_physics_with_override():
    """bake_to_keyframes failed with context error; try temp_override."""
    bpy.ops.mesh.primitive_plane_add(size=8)
    floor = bpy.context.active_object
    bpy.ops.rigidbody.world_add()
    bpy.context.view_layer.objects.active = floor
    bpy.ops.rigidbody.object_add(); floor.rigid_body.type = "PASSIVE"
    ball = bpy.data.objects["Sphere"]
    bpy.context.view_layer.objects.active = ball
    if not ball.rigid_body:
        bpy.ops.rigidbody.object_add()
    ball.rigid_body.type = "ACTIVE"; ball.rigid_body.restitution = 0.7
    bpy.context.scene.frame_set(1)
    r = {}
    try:
        with bpy.context.temp_override(object=ball, active_object=ball, selected_objects=[ball]):
            bpy.ops.rigidbody.bake_to_keyframes(frame_start=1, frame_end=10)
        r["temp_override"] = "OK"
    except Exception as e:
        r["temp_override"] = "FAIL: %s" % e
    ad = ball.animation_data
    if ad and ad.action and hasattr(ad.action, "layers") and len(ad.action.layers):
        cb = ad.action.layers[0].strips[0].channelbags[0]
        r["fcurves_after_bake"] = [f.data_path for f in cb.fcurves]
    return r
step("bake_to_keyframes_temp_override", f_bake_physics_with_override)

def f_manual_bake():
    """Manual alternative: step frames, read matrix_world, keyframe_insert."""
    ball = bpy.data.objects["Sphere"]
    sc = bpy.context.scene
    ball.animation_data_clear()
    for f in range(1, 11):
        sc.frame_set(f)
        bpy.context.view_layer.update()
        m = ball.matrix_world.copy()
        ball.location = m.translation
        ball.keyframe_insert(data_path="location", frame=f)
    ad = ball.animation_data
    cb = ad.action.layers[0].strips[0].channelbags[0]
    n = sum(len(fc.keyframe_points) for fc in cb.fcurves)
    zs = []
    for f in (1, 5, 10):
        sc.frame_set(f); zs.append(round(ball.matrix_world.translation.z, 3))
    return {"fcurves": len(cb.fcurves), "total_keyframes": n, "z_by_frame": zs}
step("manual_physics_bake", f_manual_bake)

def f_seq_render():
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 4
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = os.path.abspath("_seq2/f_")
    bpy.ops.render.render(animation=True)
    d = os.path.abspath("_seq2")
    files = sorted(os.listdir(d)) if os.path.exists(d) else []
    return {"dir": d, "files": files[:12], "count": len(files)}
step("png_sequence_render", f_seq_render)

def f_contact_sheet():
    """Build a contact sheet from the rendered PNGs using numpy + bpy.data.images (no PIL)."""
    import numpy as np
    d = os.path.abspath("_seq2")
    files = sorted(os.listdir(d))[:6]
    imgs = []
    for fn in files:
        im = bpy.data.images.load(os.path.join(d, fn))
        a = np.empty(len(im.pixels), dtype=np.float32)
        im.pixels.foreach_get(a)
        imgs.append(a.reshape(im.size[1], im.size[0], im.channels))
        bpy.data.images.remove(im)
    h, w, c = imgs[0].shape
    cols = 3; rows = (len(imgs) + cols - 1) // cols
    sheet = np.zeros((rows*h, cols*w, 4), dtype=np.float32)
    for i, a in enumerate(imgs):
        r, cc = divmod(i, cols)
        sheet[r*h:(r+1)*h, cc*w:(cc+1)*w, :] = a
    out = bpy.data.images.new("sheet", width=cols*w, height=rows*h, alpha=True)
    out.pixels.foreach_set(sheet.ravel())
    p = os.path.abspath("_contact_sheet.png")
    out.filepath_raw = p; out.file_format = "PNG"; out.save()
    return {"sheet_size": [cols*w, rows*h], "frames": len(imgs), "out": p, "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else 0}
step("contact_sheet_numpy", f_contact_sheet)

with open("_probe5_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE5_DONE")
