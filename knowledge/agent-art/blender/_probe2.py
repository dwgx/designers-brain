"""Probe 2: engine availability, motion blur, DOF, physics ops. All wrapped so one failure can't abort."""
import bpy, sys, json, traceback, time, os

out = {"steps": []}
def step(name, fn):
    t = time.time()
    try:
        r = fn()
        out["steps"].append({"name": name, "ok": True, "secs": round(time.time()-t, 2), "result": r})
    except Exception as e:
        out["steps"].append({"name": name, "ok": False, "secs": round(time.time()-t, 2),
                             "error": "%s: %s" % (type(e).__name__, e), "tb": traceback.format_exc()[-400:]})

# 1. Is Cycles addon present?
def f_cycles():
    import addon_utils
    mods = [(m.__name__, m.bl_info.get("name"), addon_utils.check(m.__name__)) for m in addon_utils.modules() if "cycl" in m.__name__.lower() or "eevee" in m.__name__.lower()]
    return {"addon_modules_matching": mods,
            "enabled_addons": sorted([a for a in bpy.context.preferences.addons.keys()])}
step("cycles_addon", f_cycles)

# 2. engine enum via bpy.ops render.engine items (dynamic)
def f_engine_enum():
    items = [i.identifier for i in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
    sc = bpy.context.scene
    res = {"enum": items}
    for eng in ("CYCLES", "BLENDER_EEVEE", "BLENDER_WORKBENCH"):
        try:
            sc.render.engine = eng
            res["set_" + eng] = "OK"
        except Exception as e:
            res["set_" + eng] = "FAIL %s" % e
    return res
step("engine_enum", f_engine_enum)

# 3. motion blur locations
def f_mb():
    sc = bpy.context.scene
    r = {"scene.render.use_motion_blur": getattr(sc.render, "use_motion_blur", "ABSENT"),
         "scene.render.motion_blur_shutter": getattr(sc.render, "motion_blur_shutter", "ABSENT"),
         "has_scene.cycles": hasattr(sc, "cycles")}
    if hasattr(sc, "cycles"):
        r["cycles_attrs_motion"] = [p for p in dir(sc.cycles) if "motion" in p.lower() or "blur" in p.lower()]
    r["eevee_motion"] = {k: getattr(sc.eevee, k, "ABSENT") for k in ("motion_blur_max", "motion_blur_steps", "motion_blur_depth_scale")}
    return r
step("motion_blur", f_mb)

# 4. camera DOF
def f_dof():
    cam = bpy.data.cameras.new("C")
    return {"dof_attrs": sorted([p.identifier for p in cam.bl_rna.properties if "dof" in p.identifier.lower()]),
            "dof_defaults": {"use_dof": cam.dof.use_dof, "focus_distance": cam.dof.focus_distance,
                             "aperture_fstop": cam.dof.aperture_fstop, "aperture_blades": cam.dof.aperture_blades}}
step("camera_dof", f_dof)

# 5. physics ops exist?
def f_phys():
    ops = [o for o in dir(bpy.ops.rigidbody)] + [o for o in dir(bpy.ops.object)]
    return {"rigidbody_ops": sorted([o for o in dir(bpy.ops.rigidbody) if not o.startswith("_")]),
            "has_rigidbody_object_add": hasattr(bpy.ops.rigidbody, "object_add"),
            "has_rigidbody_world_add": hasattr(bpy.ops.rigidbody, "world_add"),
            "has_cloth_ops": hasattr(bpy.ops.cloth, "preset_add") if hasattr(bpy.ops, "cloth") else False,
            "object_modifier_add": hasattr(bpy.ops.object, "modifier_add"),
            "has_sim_physics_bake": hasattr(bpy.ops.ptcache, "bake") if hasattr(bpy.ops, "ptcache") else False}
step("physics_ops", f_phys)

# 6. ffmpeg output settings
def f_ffmpeg():
    sc = bpy.context.scene
    ff = sc.render.ffmpeg
    return {"format": ff.format, "codec": ff.codec,
            "formats": [i.identifier for i in ff.bl_rna.properties["format"].enum_items],
            "codecs": [i.identifier for i in ff.bl_rna.properties["codec"].enum_items],
            "container": getattr(ff, "container", "ABSENT"),
            "constant_rate_factor": getattr(ff, "constant_rate_factor", "ABSENT")}
step("ffmpeg_settings", f_ffmpeg)

# 7. color management / view transforms
def f_cm():
    vs = bpy.context.scene.view_settings
    return {"view_transform_enum": [i.identifier for i in vs.bl_rna.properties["view_transform"].enum_items],
            "look_enum": [i.identifier for i in vs.bl_rna.properties["look"].enum_items][:12]}
step("color_management", f_cm)

# 8. geometry nodes + instancing
def f_gn():
    return {"has_geometry_node_tree": hasattr(bpy.types, "GeometryNodeTree"),
            "gn_node_types_sample": sorted([n for n in dir(bpy.types) if n.startswith("GeometryNode")])[:30],
            "has_instance_on_points": hasattr(bpy.types, "GeometryNodeInstanceOnPoints")}
step("geometry_nodes", f_gn)

# 9. light types + area light size (soft shadow control)
def f_lights():
    l = bpy.data.lights.new("L", type="AREA")
    return {"light_types": [i.identifier for i in l.bl_rna.properties["type"].enum_items],
            "area_attrs": sorted([p.identifier for p in l.bl_rna.properties if any(k in p.identifier.lower() for k in ("size","shape","spread","radius"))]),
            "size": l.size, "shape": l.shape}
step("lights", f_lights)

# 10. Principled BSDF input names (material paths for glass/rubber/metal)
def f_bsdf():
    m = bpy.data.materials.new("M"); m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    ins = [i.name for i in bsdf.inputs] if bsdf else "no principled node"
    return {"principled_inputs": ins,
            "material_node_types_sample": sorted([n for n in dir(bpy.types) if n.startswith("ShaderNodeBsdf")])}
step("principled_bsdf", f_bsdf)

# 11. render write + engine timing measured separately in probe3; here: output path API
def f_out():
    sc = bpy.context.scene
    return {"filepath": sc.render.filepath, "image_settings_file_format": sc.render.image_settings.file_format,
            "color_mode": sc.render.image_settings.color_mode, "color_depth": sc.render.image_settings.color_depth,
            "has_use_overwrite": hasattr(sc.render, "use_overwrite"),
            "resolution_percentage": sc.render.resolution_percentage}
step("output_settings", f_out)

with open("_probe2_out.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, default=str)
print("PROBE2_DONE")
