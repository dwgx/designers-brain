"""Probe 9: material-level EEVEE refraction toggle; soft-body squash fixed; soft shadow via light size."""
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

def f_mat_props():
    m = bpy.data.materials.new("M"); m.use_nodes = True
    keys = ("raytrace", "refract", "transmission", "transparent", "shadow", "sss", "subsurface", "blend", "thickness", "volume", "displacement")
    props = [p.identifier for p in m.bl_rna.properties if not p.is_readonly
             and any(k in p.identifier.lower() for k in keys)]
    vals = {p: repr(getattr(m, p))[:60] for p in props}
    return {"eevee_relevant_material_props": props, "defaults": vals}
step("material_eevee_props", f_mat_props)

def f_glass2():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    cd = bpy.data.cameras.new("Cam"); co = bpy.data.objects.new("Cam", cd)
    sc.collection.objects.link(co); co.location = (0, -9, 2.2); co.rotation_euler = (math.radians(80), 0, 0)
    sc.camera = co
    ld = bpy.data.lights.new("Key", type="AREA"); ld.size = 8.0; ld.energy = 1500
    lo = bpy.data.objects.new("Key", ld); sc.collection.objects.link(lo); lo.location = (-5, -6, 8)
    sc.render.engine = "BLENDER_EEVEE"; sc.eevee.taa_render_samples = 16
    sc.render.resolution_x = 480; sc.render.resolution_y = 270
    sc.render.image_settings.file_format = "PNG"
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.2, location=(0, 0, 1.2))
    sph = bpy.context.active_object; bpy.ops.object.shade_smooth()
    m = bpy.data.materials.new("Glass"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Roughness"].default_value = 0.02
    b.inputs["IOR"].default_value = 1.45
    b.inputs["Transmission Weight"].default_value = 1.0
    sph.data.materials.append(m)
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 6, 1.2), rotation=(math.radians(90), 0, 0))
    bd = bpy.context.active_object
    mb = bpy.data.materials.new("Back"); mb.use_nodes = True
    nt = mb.node_tree
    tex = nt.nodes.new("ShaderNodeTexChecker"); tex.inputs["Scale"].default_value = 6
    tex.inputs["Color1"].default_value = (0.1, 0.3, 0.9, 1)
    tex.inputs["Color2"].default_value = (0.95, 0.75, 0.1, 1)
    nt.links.new(tex.outputs["Color"], nt.nodes["Principled BSDF"].inputs["Base Color"])
    bd.data.materials.append(mb)
    res = {"mat_has_use_raytrace_refraction": hasattr(m, "use_raytrace_refraction"),
           "mat_has_use_transparent_shadow": hasattr(m, "use_transparent_shadow")}
    combos = []
    for rt in (False, True):
        for refr in (False, True):
            sc.eevee.use_raytracing = rt
            if hasattr(m, "use_raytrace_refraction"): m.use_raytrace_refraction = refr
            p = os.path.abspath("_g2_%s_%s.png" % (rt, refr))
            sc.render.filepath = p
            bpy.ops.render.render(write_still=True)
            combos.append({"scene_raytracing": rt, "mat_raytrace_refraction": refr,
                           "bytes": os.path.getsize(p), "arr": grab(p)})
    base = combos[0]["arr"]
    for c in combos:
        c["mean_abs_diff_vs_first"] = round(float(np.abs(c["arr"] - base).mean()), 6)
        c.pop("arr")
    res["combos"] = combos
    return res
step("glass_refraction_toggle_matrix", f_glass2)

def f_squash():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=20)
    floor = bpy.context.active_object; floor.name = "Floor"
    cm = floor.modifiers.new("Collision", "COLLISION")
    cm.settings.thickness_outer = 0.02
    bpy.ops.mesh.primitive_cube_add(size=1.2, location=(0, 0, 1.4))
    cube = bpy.context.active_object; cube.name = "Soft"
    bpy.ops.object.modifier_add(type="SUBSURF")
    cube.modifiers["Subdivision"].levels = 3
    bpy.ops.object.modifier_apply(modifier="Subdivision")
    nverts = len(cube.data.vertices)
    sb = cube.modifiers.new("SoftBody", "SOFT_BODY")
    st = sb.settings
    st.use_goal = False
    st.mass = 0.5
    st.friction = 0.9
    st.bend = 0.8
    st.plastic = 0            # int
    st.ball_stiff = 10.0
    st.ball_damp = 0.5
    st.use_edges = True
    sc.frame_start = 1; sc.frame_end = 30
    bpy.ops.ptcache.bake_all(bake=True)
    samples = []
    for f in (1, 6, 10, 14, 20, 30):
        sc.frame_set(f); bpy.context.view_layer.update()
        dg = bpy.context.evaluated_depsgraph_get()
        ev = cube.evaluated_get(dg)
        me = ev.to_mesh()
        zs = [v.co.z for v in me.vertices]
        samples.append({"f": f, "min_z": round(min(zs), 3), "max_z": round(max(zs), 3),
                        "height": round(max(zs) - min(zs), 3)})
        ev.to_mesh_clear()
    return {"cube_verts": nverts, "rest_height": 1.2, "samples": samples,
            "note": "height < 1.2 == squashed"}
step("softbody_squash_fixed", f_squash)

def f_soft_shadow():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_plane_add(size=30)
    fl = bpy.context.active_object
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.7, location=(0, 0, 0.7))
    sph = bpy.context.active_object
    bpy.ops.object.shade_smooth()
    cd = bpy.data.cameras.new("C"); co = bpy.data.objects.new("C", cd); sc.collection.objects.link(co)
    co.location = (0, -6, 4.5); co.rotation_euler = (math.radians(58), 0, 0); sc.camera = co
    ld = bpy.data.lights.new("K", type="AREA"); lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo)
    lo.location = (3, -3, 7); lo.rotation_euler = (0.6, 0.4, 0.2)
    sc.render.engine = "BLENDER_EEVEE"; sc.eevee.taa_render_samples = 16
    sc.render.resolution_x = 480; sc.render.resolution_y = 270
    sc.render.image_settings.file_format = "PNG"
    res = []
    for size in (0.25, 3.0, 12.0):
        ld.size = size
        ld.energy = 10.0 * (size ** 2) / 1.0  # keep brightness roughly constant as size grows
        p = os.path.abspath("_shadow_%s.png" % size)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        res.append({"light_size": size, "bytes": os.path.getsize(p), "arr": grab(p)})
    # measure shadow edge softness: gradient magnitude on the floor region (lower half)
    stats = []
    for r in res:
        a = r["arr"].reshape(270, 480, 4)[:110, :, :3]
        g = np.abs(np.diff(a.mean(axis=2), axis=1))
        stats.append({"light_size": r["light_size"], "bytes": r["bytes"],
                      "mean_edge_gradient": round(float(g.mean()), 6),
                      "p99_edge_gradient": round(float(np.percentile(g, 99)), 6)})
        r.pop("arr")
    return {"per_light_size": stats, "note": "bigger light size -> softer (lower-contrast) shadow edge"}
step("soft_shadow_vs_light_size", f_soft_shadow)

with open("_probe9_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE9_DONE")
