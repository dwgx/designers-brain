"""Dev API probe for build decisions."""
import bpy, json, math, os
R = {}
def step(name, fn):
    try: R[name] = fn()
    except Exception as e: R[name] = "FAIL %s: %s" % (type(e).__name__, e)

def vt():
    opts = [i.identifier for i in bpy.context.scene.view_settings.bl_rna.properties['view_transform'].enum_items]
    ok = {}
    for v in ('Khronos PBR Neutral','AgX','Standard','Filmic'):
        try:
            bpy.context.scene.view_settings.view_transform = v; ok[v]=True
        except Exception as e: ok[v]=str(e)[:50]
    return {"available": opts, "set_ok": ok}
step("view_transform", vt)

def eevee_attrs():
    sc = bpy.context.scene
    names = [p.identifier for p in sc.eevee.bl_rna.properties if not p.is_readonly]
    rto = [p.identifier for p in sc.eevee.ray_tracing_options.bl_rna.properties if not p.is_readonly] if hasattr(sc.eevee,'ray_tracing_options') else None
    vals = {n: getattr(sc.eevee, n) for n in ('taa_render_samples','taa_samples','motion_blur_steps','motion_blur_max','use_raytracing','shadow_ray_count','shadow_step_count','use_shadows','use_volumetric_shadows','shadow_pool_size') if hasattr(sc.eevee, n)}
    rtv = {n: getattr(sc.eevee.ray_tracing_options, n) for n in (rto or []) if not hasattr(getattr(sc.eevee.ray_tracing_options,n),'__len__') or isinstance(getattr(sc.eevee.ray_tracing_options,n), (int,float,bool,str))}
    return {"eevee_props": names, "vals": vals, "rt_options_props": rto, "rt_options_vals": rtv}
step("eevee_attrs", eevee_attrs)

def rb_attrs():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.mesh.primitive_cube_add()
    ob = bpy.context.active_object
    bpy.ops.rigidbody.object_add()
    rb = ob.rigid_body
    props = [p.identifier for p in rb.bl_rna.properties if not p.is_readonly]
    vals = {}
    for n in ('type','mass','friction','restitution','linear_damping','angular_damping','use_deactivation','deactivate_linear_velocity','deactivate_angular_velocity','kinematic','collision_shape','use_margin','collision_margin','use_start_deactivated','mesh_source','use_dynamic_ccd','ccd_motion_threshold','ccd_swept_sphere_radius'):
        if hasattr(rb, n):
            try: vals[n] = getattr(rb, n)
            except Exception as e: vals[n] = 'ERR'
    return {"props": props, "vals": vals}
step("rigidbody_attrs", rb_attrs)

def slot_override():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.mesh.primitive_uv_sphere_add()
    a = bpy.context.active_object
    bpy.ops.mesh.primitive_uv_sphere_add(location=(3,0,0))
    b = bpy.context.active_object
    m1 = bpy.data.materials.new("m1"); m2 = bpy.data.materials.new("m2")
    a.data.materials.append(m1)
    b.data = a.data
    r = {}
    try:
        b.material_slots[0].link = 'OBJECT'
        b.material_slots[0].material = m2
        r = {"link": b.material_slots[0].link, "mat": b.material_slots[0].material.name, "a_mat": a.material_slots[0].material.name, "shared_mesh": a.data==b.data}
    except Exception as e:
        r = {"err": str(e)}
    return r
step("object_material_slot", slot_override)

def text_mesh():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.object.text_add()
    ob = bpy.context.active_object
    ob.data.body = "PLAY"
    ob.data.extrude = 0.4
    ob.data.bevel_depth = 0.06
    ob.data.bevel_resolution = 3
    ob.data.size = 1.0
    bpy.ops.object.convert(target='MESH')
    ob = bpy.context.active_object
    me = ob.data
    xs = [v.co.x for v in me.vertices]; ys=[v.co.y for v in me.vertices]; zs=[v.co.z for v in me.vertices]
    return {"verts": len(me.vertices), "polys": len(me.polygons), "bbox_x": [round(min(xs),3), round(max(xs),3)], "bbox_y": [round(min(ys),3), round(max(ys),3)], "bbox_z": [round(min(zs),3), round(max(zs),3)]}
step("text_to_mesh", text_mesh)

def comp_check():
    sc = bpy.context.scene
    ng = bpy.data.node_groups.new("Comp","CompositorNodeTree")
    sc.compositing_node_group = ng
    n = ng.nodes.new("CompositorNodeGlare")
    ok = {"glare": n.bl_rna.identifier, "types": [i.identifier for i in n.bl_rna.properties['glare_type'].enum_items] if hasattr(n,'glare_type') else 'n/a'}
    try: sc.render.use_compositing = True; ok['use_comp'] = True
    except Exception as e: ok['use_comp'] = str(e)
    return ok
step("compositor", comp_check)

def sun_area_defaults():
    sc = bpy.context.scene
    ld = bpy.data.lights.new("A", type='AREA')
    return {"energy_default": ld.energy, "size_default": ld.size, "shape": ld.shape,
            "eevee_samples_note": "n/a"}
step("light_defaults", sun_area_defaults)

print("DEV_API_DONE")
json.dump(R, open("_dev_api_out.json","w"), indent=1, default=str)
