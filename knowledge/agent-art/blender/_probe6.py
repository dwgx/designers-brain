"""Probe 6: media_type video path -> real mp4; instancing wave; DOF sanity."""
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

def f_media_type():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    iset = sc.render.image_settings
    res = {"has_media_type": hasattr(iset, "media_type")}
    if hasattr(iset, "media_type"):
        res["media_type_enum"] = [i.identifier for i in iset.bl_rna.properties["media_type"].enum_items]
        res["default"] = iset.media_type
        iset.media_type = "VIDEO"
        res["after_set_VIDEO"] = iset.media_type
        try:
            iset.file_format = "FFMPEG"
            res["file_format_after"] = iset.file_format
            res["is_movie_format"] = sc.render.is_movie_format
        except Exception as e:
            res["file_format_err"] = str(e)
        # now what ffmpeg sub-options exist
        ff = sc.render.ffmpeg
        res["ffmpeg"] = {"format": ff.format, "codec": ff.codec,
                         "formats": [i.identifier for i in ff.bl_rna.properties["format"].enum_items],
                         "codecs": [i.identifier for i in ff.bl_rna.properties["codec"].enum_items],
                         "crf_enum": [i.identifier for i in ff.bl_rna.properties["constant_rate_factor"].enum_items],
                         "attrs": sorted([p.identifier for p in ff.bl_rna.properties if not p.is_readonly])}
    return res
step("media_type_video", f_media_type)

def f_build_and_render_mp4():
    sc = bpy.context.scene
    # minimal scene
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.6, location=(0, 0, 1.2))
    ball = bpy.context.active_object
    cd = bpy.data.cameras.new("Cam"); co = bpy.data.objects.new("Cam", cd)
    sc.collection.objects.link(co); co.location = (0, -5, 1.2); co.rotation_euler = (1.5708, 0, 0)
    sc.camera = co
    ld = bpy.data.lights.new("K", type="AREA"); ld.size = 3; ld.energy = 400
    lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo); lo.location = (2, -3, 4)
    # animate ball up/down
    ball.keyframe_insert(data_path="location", frame=1)
    ball.location.z = 2.4; ball.keyframe_insert(data_path="location", frame=15)
    ball.location.z = 1.2; ball.keyframe_insert(data_path="location", frame=30)
    sc.render.engine = "BLENDER_EEVEE"; sc.eevee.taa_render_samples = 8
    sc.render.resolution_x = 640; sc.render.resolution_y = 360
    sc.render.fps = 30; sc.frame_start = 1; sc.frame_end = 30
    sc.render.image_settings.media_type = "VIDEO"
    sc.render.image_settings.file_format = "FFMPEG"
    sc.render.ffmpeg.format = "MPEG4"; sc.render.ffmpeg.codec = "H264"
    sc.render.ffmpeg.constant_rate_factor = "HIGH"
    p = os.path.abspath("_video_test.mp4")
    sc.render.filepath = p
    t = time.time(); bpy.ops.render.render(animation=True); dt = time.time()-t
    return {"seconds": round(dt, 2), "file": p, "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else 0}
step("blender_direct_mp4_30f", f_build_and_render_mp4)

def f_instancing_wave():
    """Prove the '一大片小球像波浪起伏' pattern: instanced spheres + script-driven sine wave."""
    import math
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    mesh = bpy.data.meshes.new("dot")
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, segments=12, ring_count=8)
    base = bpy.context.active_object
    base.name = "DotProto"
    N = 12
    made = 0
    for i in range(N):
        for j in range(N):
            o = base.copy(); o.data = base.data
            o.location = ((i - N/2) * 0.5, (j - N/2) * 0.5, 0)
            sc.collection.objects.link(o)
            for f in range(1, 61, 5):
                ph = (i * 0.45 + j * 0.45)
                z = 0.35 * math.sin(2*math.pi*(f/60.0)*1.5 - ph) + 0.35
                o.location.z = z
                o.keyframe_insert(data_path="location", frame=f)
            made += 1
    sc.frame_end = 60
    return {"instances": made, "method": "object.copy() + shared mesh data + keyframed location",
            "note": "same mesh data shared -> cheap; 144 objects"}
step("instancing_wave_144_objects", f_instancing_wave)

def f_gn_instance_wave():
    """Geometry-nodes alternative: instance on points grid + sine offset. Just verify node types exist."""
    types = ["GeometryNodeInstanceOnPoints", "GeometryNodeMeshGrid", "GeometryNodeSetPosition",
             "GeometryNodeInputPosition", "GeometryNodeMath", "GeometryNodeSine", "GeometryNodeRealizeInstances"]
    return {t: hasattr(bpy.types, t) for t in types}
step("gn_nodes_available", f_gn_instance_wave)

def f_dof_check():
    sc = bpy.context.scene
    cam = sc.camera
    cam.data.dof.use_dof = True
    cam.data.dof.focus_distance = 5.0
    cam.data.dof.aperture_fstop = 1.4
    cam.data.dof.aperture_blades = 9
    return {"use_dof": cam.data.dof.use_dof, "focus_distance": cam.data.dof.focus_distance,
            "fstop": cam.data.dof.aperture_fstop, "blades": cam.data.dof.aperture_blades,
            "has_focus_object": hasattr(cam.data.dof, "focus_object")}
step("dof_config", f_dof_check)

with open("_probe6_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE6_DONE")
