"""Probe 3: real headless render test. EEVEE vs Cycles, 1920x1080, one frame each, timed.
Also: view transform enum, compositor new API, GPU info."""
import bpy, json, time, traceback, os, sys

R = {"steps": []}
def step(name, fn):
    t = time.time()
    try:
        r = fn()
        R["steps"].append({"name": name, "ok": True, "secs": round(time.time()-t, 2), "result": r})
    except Exception as e:
        R["steps"].append({"name": name, "ok": False, "secs": round(time.time()-t, 2),
                           "error": "%s: %s" % (type(e).__name__, e), "tb": traceback.format_exc()[-600:]})

# ---- build a tiny scene: glass sphere + metal cube + rubber plane + area light + camera
def build():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene

    # ground
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    ground = bpy.context.active_object; ground.name = "Ground"

    # glass sphere
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(-1.6, 0, 1.0))
    sph = bpy.context.active_object; sph.name = "GlassSphere"
    bpy.ops.object.shade_smooth()

    # metal cube
    bpy.ops.mesh.primitive_cube_add(size=1.6, location=(1.8, 0.4, 0.8))
    cube = bpy.context.active_object; cube.name = "MetalCube"

    # materials via Principled inputs (Blender 4.x/5.x naming)
    def mat(name, **kv):
        m = bpy.data.materials.new(name); m.use_nodes = True
        b = m.node_tree.nodes["Principled BSDF"]
        for k, v in kv.items():
            b.inputs[k].default_value = v
        return m
    glass = mat("Glass", **{"Base Color": (1, 1, 1, 1), "Roughness": 0.03, "IOR": 1.45, "Transmission Weight": 1.0})
    metal = mat("Metal", **{"Base Color": (0.9, 0.75, 0.35, 1), "Metallic": 1.0, "Roughness": 0.18})
    rubber = mat("Rubber", **{"Base Color": (0.85, 0.15, 0.2, 1), "Roughness": 0.75,
                              "Subsurface Weight": 0.6, "Subsurface Radius": (0.4, 0.15, 0.1),
                              "Subsurface Scale": 0.15})
    sph.data.materials.append(glass)
    cube.data.materials.append(metal)
    ground.data.materials.append(rubber)

    # big area light = soft shadow
    ld = bpy.data.lights.new("Key", type="AREA"); ld.size = 8.0; ld.energy = 1200.0
    lo = bpy.data.objects.new("Key", ld); sc.collection.objects.link(lo)
    lo.location = (-6, -7, 9); lo.rotation_euler = (0.75, 0, -0.7)

    # camera with DOF + motion blur ready
    cd = bpy.data.cameras.new("Cam"); cd.dof.use_dof = True; cd.dof.focus_distance = 9.0; cd.dof.aperture_fstop = 2.0
    co = bpy.data.objects.new("Cam", cd); sc.collection.objects.link(co)
    co.location = (0, -11, 3.2); co.rotation_euler = (1.30, 0, 0)
    sc.camera = co

    sc.render.resolution_x = 1920; sc.render.resolution_y = 1080; sc.render.resolution_percentage = 100
    sc.render.fps = 30
    sc.render.use_motion_blur = True; sc.render.motion_blur_shutter = 0.5
    sc.render.image_settings.file_format = "PNG"
    return sc

step("build_scene", build)

def get_gpu():
    import gpu
    try:
        return {"vendor": gpu.platform.vendor_get(), "renderer": gpu.platform.renderer_get(),
                "version": gpu.platform.version_get(), "backend": gpu.platform.backend_type_get()}
    except Exception as e:
        return {"gpu_api_err": "%s: %s" % (type(e).__name__, e)}
step("gpu_platform", get_gpu)

def view_transforms():
    sc = bpy.context.scene
    vs = sc.view_settings
    return {"view_transform_enum": [i.identifier for i in vs.bl_rna.properties["view_transform"].enum_items],
            "current": vs.view_transform, "look_enum": [i.identifier for i in vs.bl_rna.properties["look"].enum_items][:16],
            "display_device": sc.display_settings.display_device,
            "sequencer_colorspace": sc.sequencer_colorspace_settings.name}
step("view_transforms_no_factory_startup", view_transforms)

def eevee_render():
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 64
    sc.eevee.motion_blur_steps = 8
    sc.render.filepath = os.path.abspath("_render_eevee_")
    t = time.time(); bpy.ops.render.render(write_still=True); dt = time.time()-t
    p = os.path.abspath("_render_eevee_.png")
    return {"seconds": round(dt, 2), "file": p, "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else 0}
step("render_eevee_1080p", eevee_render)

def cycles_render():
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.samples = 64
    sc.cycles.use_denoising = True
    sc.cycles.device = "CPU"
    sc.render.filepath = os.path.abspath("_render_cycles_")
    t = time.time(); bpy.ops.render.render(write_still=True); dt = time.time()-t
    p = os.path.abspath("_render_cycles_.png")
    return {"seconds": round(dt, 2), "file": p, "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else 0,
            "device": sc.cycles.device, "denoise": sc.cycles.use_denoising}
step("render_cycles_1080p_64spp", cycles_render)

def cycles_gpu():
    sc = bpy.context.scene
    prefs = bpy.context.preferences.addons["cycles"].preferences
    devs = []
    try:
        prefs.refresh_devices()
        devs = [{"type": d.type, "name": d.name, "use": d.use} for d in prefs.devices]
    except Exception as e:
        devs = [{"err": str(e)}]
    return {"compute_device_type": getattr(prefs, "compute_device_type", "ABSENT"), "devices": devs}
step("cycles_devices", cycles_gpu)

def compositor_new_api():
    sc = bpy.context.scene
    out = {"has_compositing_node_group": hasattr(sc, "compositing_node_group"),
           "value": repr(getattr(sc, "compositing_node_group", None))}
    ng = bpy.data.node_groups.new("CompTest", "CompositorNodeTree")
    sc.compositing_node_group = ng
    n = ng.nodes.new("CompositorNodeGlare")
    out["glare_node_created"] = n.bl_idname
    out["node_tree_assign_ok"] = (sc.compositing_node_group == ng)
    # does use_nodes still toggle?
    sc.use_nodes = True
    out["use_nodes_after"] = sc.use_nodes
    return out
step("compositor_52_api", compositor_new_api)

def ffmpeg_write_video():
    """Try writing a real H.264 mp4 straight from Blender (1 frame, to test container path)."""
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_EEVEE"
    sc.eevee.taa_render_samples = 8
    sc.render.image_settings.file_format = "FFMPEG"
    sc.render.ffmpeg.format = "MPEG4"; sc.render.ffmpeg.codec = "H264"
    sc.render.ffmpeg.constant_rate_factor = "HIGH"
    sc.render.filepath = os.path.abspath("_video_test.mp4")
    sc.frame_start = 1; sc.frame_end = 2
    t = time.time()
    try:
        bpy.ops.render.render(animation=True)
        ok = True; err = None
    except Exception as e:
        ok = False; err = str(e)
    dt = time.time()-t
    p = os.path.abspath("_video_test.mp4")
    return {"ok": ok, "err": err, "seconds": round(dt, 2), "exists": os.path.exists(p),
            "bytes": os.path.getsize(p) if os.path.exists(p) else 0}
step("ffmpeg_direct_mp4", ffmpeg_write_video)

with open("_probe3_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE3_DONE")
