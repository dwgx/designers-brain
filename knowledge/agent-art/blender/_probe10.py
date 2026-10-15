"""Probe 10: correct penumbra-width measurement; rubber SSS pixel evidence."""
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
    w, h = im.size
    bpy.data.images.remove(im)
    return a.reshape(h, w, 4)

def f_penumbra():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    # big white floor, one box casting a shadow
    bpy.ops.mesh.primitive_plane_add(size=60, location=(0, 0, 0))
    fl = bpy.context.active_object
    mf = bpy.data.materials.new("F"); mf.use_nodes = True
    mf.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.8, 0.8, 0.8, 1)
    mf.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.9
    fl.data.materials.append(mf)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 2.0))
    bx = bpy.context.active_object
    cd = bpy.data.cameras.new("C"); co = bpy.data.objects.new("C", cd); sc.collection.objects.link(co)
    # look straight down so the shadow edge is clean and measurable along X
    co.location = (0, 0, 12); co.rotation_euler = (0, 0, 0); sc.camera = co
    cd.type = "ORTHO"; cd.ortho_scale = 12.0
    ld = bpy.data.lights.new("K", type="AREA"); lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo)
    lo.location = (0, 0, 14); lo.rotation_euler = (0, 0, 0)   # light straight above -> shadow directly under box
    sc.render.engine = "BLENDER_EEVEE"; sc.eevee.taa_render_samples = 32
    sc.render.resolution_x = 512; sc.render.resolution_y = 512
    sc.render.image_settings.file_format = "PNG"
    out = []
    for size in (0.1, 2.0, 8.0):
        ld.size = size
        # keep irradiance constant: energy scales with area
        ld.energy = 200.0 * max(size, 0.1) ** 2 / 4.0
        p = os.path.abspath("_pen_%s.png" % size)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        a = grab(p)
        # image rows are bottom-up; take a horizontal scanline through the middle
        row = a[256, :, 0]
        lo_v, hi_v = float(row.min()), float(row.max())
        lo10 = lo_v + 0.10 * (hi_v - lo_v)
        lo90 = lo_v + 0.90 * (hi_v - lo_v)
        # count pixels in the 10%-90% transition band (per edge); use the left edge
        idx = np.where(row < lo90)[0]
        left = idx[idx < 256]
        band = 0
        if len(left):
            start = left.min()
            j = start
            while j < 512 and row[j] < lo90:
                j += 1
            while j < 512 and row[j] < lo10:
                j += 1
            band = j - start
        out.append({"light_size": size, "bytes": os.path.getsize(p),
                    "row_min": round(lo_v, 4), "row_max": round(hi_v, 4),
                    "penumbra_px_10_90": int(band)})
    return {"scanline": "row 256 of 512, column 0..511", "per_light_size": out,
            "note": "penumbra_px_10_90 = width of the 10%-90% transition band; bigger = softer shadow"}
step("penumbra_width_vs_light_size", f_penumbra)

def f_sss():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0, 0, 1.0))
    sph = bpy.context.active_object; bpy.ops.object.shade_smooth()
    m = bpy.data.materials.new("Rubber"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (0.9, 0.1, 0.15, 1)
    b.inputs["Roughness"].default_value = 0.7
    b.inputs["Subsurface Radius"].default_value = (0.6, 0.2, 0.15)
    b.inputs["Subsurface Scale"].default_value = 0.25
    sph.data.materials.append(m)
    cd = bpy.data.cameras.new("C"); co = bpy.data.objects.new("C", cd); sc.collection.objects.link(co)
    co.location = (0, -5, 1.6); co.rotation_euler = (math.radians(85), 0, 0); sc.camera = co
    ld = bpy.data.lights.new("K", type="AREA"); ld.size = 5; ld.energy = 800
    lo = bpy.data.objects.new("K", ld); sc.collection.objects.link(lo); lo.location = (-3, -3, 5)
    sc.render.engine = "BLENDER_EEVEE"; sc.eevee.taa_render_samples = 32
    sc.render.resolution_x = 480; sc.render.resolution_y = 270
    sc.render.image_settings.file_format = "PNG"
    out = {}
    for tag, w in (("sss_off", 0.0), ("sss_on", 0.9)):
        b.inputs["Subsurface Weight"].default_value = w
        p = os.path.abspath("_sss_%s.png" % tag)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        out[tag] = {"bytes": os.path.getsize(p), "arr": grab(p)}
    d = float(np.abs(out["sss_on"]["arr"] - out["sss_off"]["arr"]).mean())
    for k in out: out[k].pop("arr")
    return {"sss_off": out["sss_off"], "sss_on": out["sss_on"],
            "mean_abs_pixel_diff": round(d, 6), "sss_changes_image": d > 1e-5,
            "eevee_sss_extra_toggle": "material.use_sss_translucency (default False)"}
step("rubber_sss_evidence", f_sss)

with open("_probe10_out.json", "w", encoding="utf-8") as f:
    json.dump(R, f, indent=1, default=str)
print("PROBE10_DONE")
