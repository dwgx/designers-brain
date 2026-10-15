import bpy, math, time, json
import numpy as np

def build(deact, fric_m, fric_p, rest_m, rest_p):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    bpy.ops.rigidbody.world_add()
    rw = sc.rigidbody_world
    rw.substeps_per_frame = 12; rw.solver_iterations = 12
    bpy.ops.mesh.primitive_plane_add(size=300)
    fl = bpy.context.active_object
    bpy.context.view_layer.objects.active = fl
    bpy.ops.rigidbody.object_add(); fl.rigid_body.type='PASSIVE'; fl.rigid_body.friction=0.6
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=0.25)
    proto = bpy.context.active_object
    NI, NJ = 15, 11; SP=0.56
    marbles=[]
    for i in range(NI):
        for j in range(NJ):
            o = proto.copy(); o.data=proto.data
            o.location = ((i-7)*SP, (j-5)*SP, 0.25)
            sc.collection.objects.link(o)
            bpy.context.view_layer.objects.active=o
            bpy.ops.rigidbody.object_add()
            rb=o.rigid_body; rb.type='ACTIVE'; rb.collision_shape='SPHERE'
            rb.mass=0.2; rb.friction=fric_m; rb.restitution=rest_m
            rb.linear_damping=0.08; rb.angular_damping=0.5
            if deact:
                rb.use_deactivation=True; rb.deactivate_linear_velocity=0.12; rb.deactivate_angular_velocity=0.2
            marbles.append((o,i,j))
    bpy.data.objects.remove(proto)
    bpy.ops.object.text_add()
    t = bpy.context.active_object
    t.data.body="PLAY"; t.data.size=1; t.data.extrude=0.3; t.data.bevel_depth=0.07; t.data.bevel_resolution=4
    bpy.ops.object.convert(target='MESH')
    play = bpy.context.active_object
    me = play.data
    n=len(me.vertices); co=np.empty(n*3,np.float32); me.vertices.foreach_get("co",co); co=co.reshape(-1,3)
    s = 2.55/(co[:,0].max()-co[:,0].min())
    co[:,0]=(co[:,0]-(co[:,0].min()+co[:,0].max())/2)*s
    co[:,1]=(co[:,1]-co[:,1].min())*s
    co[:,2]=(co[:,2]-(co[:,2].min()+co[:,2].max())/2)*s
    me.vertices.foreach_set("co",co.ravel()); me.update()
    play.rotation_euler=(math.pi/2,0,0); play.location=(0,0,4.2)
    bpy.context.view_layer.objects.active=play
    bpy.ops.rigidbody.object_add()
    rb=play.rigid_body; rb.type='ACTIVE'; rb.collision_shape='CONVEX_HULL'
    rb.mass=8; rb.friction=fric_p; rb.restitution=rest_p; rb.linear_damping=0.015; rb.angular_damping=0.8
    if deact:
        rb.use_deactivation=True; rb.deactivate_linear_velocity=0.2; rb.deactivate_angular_velocity=0.3
    sc.frame_start=72; sc.frame_end=299
    rw.point_cache.frame_start=72; rw.point_cache.frame_end=299
    bpy.ops.ptcache.bake_all(bake=True)
    FRS=list(range(72,300))
    playz=[]; disp=[]
    base = np.array([((i-7)*SP,(j-5)*SP,0.25) for o,i,j in marbles])
    for f in FRS:
        sc.frame_set(f); bpy.context.view_layer.update()
        playz.append(play.matrix_world.translation.z)
        d = [ (o.matrix_world.translation.x-base[k,0])**2 + (o.matrix_world.translation.y-base[k,1])**2 for k,(o,i,j) in enumerate(marbles)]
        disp.append(max(d)**0.5)
    return {"playz": [round(float(z),3) for z in playz[::4]], "max_disp_final": round(float(disp[-1]),3),
            "max_disp_all": round(float(max(disp)),3), "disp_series": [round(float(x),3) for x in disp[::12]]}

R={}
R["A_deact_on"] = build(True, 0.65, 0.8, 0.42, 0.5)
R["B_deact_off"] = build(False, 0.65, 0.8, 0.42, 0.5)
R["C_deact_off_softfric"] = build(False, 0.45, 0.6, 0.42, 0.5)
R["D_deact_off_bouncy"] = build(False, 0.5, 0.6, 0.6, 0.65)
json.dump(R, open("_dev_sim3_out.json","w"), indent=1)
print("SIM3_DONE")
