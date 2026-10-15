"""Probe: what does this Blender build's bpy API expose? Run headless."""
import bpy, sys, json

out = {}
out["blender_version"] = bpy.app.version_string
out["bpy_version"] = bpy.app.version
out["python"] = sys.version.split()[0]
out["binary_path"] = bpy.app.binary_path

# render engines available
try:
    out["engines"] = [i.identifier for i in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items]
except Exception as e:
    out["engines_err"] = str(e)

# scene defaults
sc = bpy.context.scene
out["default_engine"] = sc.render.engine
out["default_res"] = [sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage]
out["default_fps"] = sc.render.fps
out["default_fps_base"] = sc.render.fps_base

# ffmpeg video formats available in output
try:
    out["ffmpeg_formats"] = [i.identifier for i in sc.render.image_settings.bl_rna.properties["file_format"].enum_items]
except Exception as e:
    out["ffmpeg_formats_err"] = str(e)

# image format enum
out["image_formats"] = [i.identifier for i in sc.render.image_settings.bl_rna.properties["file_format"].enum_items]

# key modules present
mods = {}
for m in ("mathutils", "bpy_extras", "gpu", "bmesh", "aud", "numpy", "PIL", "requests", "addon_utils"):
    try:
        __import__(m)
        mods[m] = "OK"
    except Exception as e:
        mods[m] = "MISSING: %s" % type(e).__name__
out["modules"] = mods

# physics availability
out["has_rigidbody"] = hasattr(bpy.types, "RigidBodyObject")
out["has_cloth"] = hasattr(bpy.types, "ClothModifier")
out["has_softbody"] = hasattr(bpy.types, "SoftBodySettings")
out["has_fluid"] = hasattr(bpy.types, "FluidModifier")
out["has_particle"] = hasattr(bpy.types, "ParticleSettings")
out["has_geometry_nodes"] = hasattr(bpy.types, "GeometryNodeTree")
# modifier types
try:
    out["modifier_types"] = sorted([i.identifier for i in bpy.types.Modifier.bl_rna.properties["type"].enum_items])
except Exception as e:
    out["modifier_types_err"] = str(e)

# motion blur / DOF properties present?
out["cycles_motion_blur"] = hasattr(bpy.context.scene, "cycles") and hasattr(bpy.context.scene.cycles, "use_motion_blur")
if out["cycles_motion_blur"]:
    out["cycles_motion_blur_default"] = bpy.context.scene.cycles.use_motion_blur
out["eevee_attr_sample"] = [a for a in dir(sc.eevee) if "blur" in a.lower() or "shadow" in a.lower()] if hasattr(sc, "eevee") else "no scene.eevee"

# eevee engine-specific settings container name
out["scene_has_eevee"] = hasattr(sc, "eevee")
if hasattr(sc, "eevee"):
    out["eevee_props"] = sorted([p.identifier for p in sc.eevee.bl_rna.properties if not p.is_readonly])[:40]

# compositor nodes (for DOF/blur post) -- API moved in 5.2; probe defensively
def _probe_compositor():
    r = {}
    r["has_scene_node_tree_attr"] = hasattr(sc, "node_tree")
    r["has_use_nodes_attr"] = hasattr(sc, "use_nodes")
    # candidates for the new home
    for name in ("compositing_node_group", "node_group", "compositor_node_group"):
        if hasattr(sc, name):
            r["new_attr_" + name] = repr(getattr(sc, name))[:120]
    r["node_tree_types_available"] = [n for n in dir(bpy.types) if "Compositor" in n or "NodeGroup" in n][:20]
    # what does bpy.types.Scene expose about nodes?
    r["scene_node_attrs"] = sorted([p.identifier for p in bpy.types.Scene.bl_rna.properties if "node" in p.identifier.lower()])
    return r
try:
    out["compositor"] = _probe_compositor()
except Exception as e:
    out["compositor_err"] = "%s: %s" % (type(e).__name__, e)

with open("_probe_api_out.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1, default=str)
print("PROBE_WROTE_FILE")
