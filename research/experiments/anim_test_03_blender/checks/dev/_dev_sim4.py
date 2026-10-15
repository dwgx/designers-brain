import bpy, math, json
import numpy as np

def read_zs(sc, objs, frames):
    out = []
    for f in frames:
        sc.frame_set(f); bpy.context.view_layer.update()
        out.append(objs.matrix_world.translation.z)
    return out

def make_world(sub=10, it=10):
    bpy.ops.rigidbody.world_add()
    rw = bpy.context.scene.rigidbody_world
    rw.substeps_per_frame = sub; rw.solver_iterations = it
    return rw

def floor_passive():
    bpy.ops.mesh.primitive_plane_add(size=50)
    fl = bpy.context.active_object
    bpy.context.view_layer.objects.active = fl
    bpy.ops.rigidbody.object_add(); fl.rigid_body.type='PASSIVE'
    return fl

def marble_at(o, mass=0.2, fric=0.5, rest=0.3, ld=0.04, ad=0.1):
    bpy.context.view_layer.objects.active = o
    bpy.ops.rigidbody.object_add()
    rb = o.rigid_body; rb.type='ACTIVE'; rb.mass=mass; rb.friction=fric; rb.restitution=rest
    rb.linear_damping=ld; rb.angular_damping=ad
    return rb

R={}

# ---------- S1: probe8d exact (49 marbles 7x7 spacing .6, cube 1.4 mass 8 from z=6), bake flow
def s1(bake=True, sub=10, it=10):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    make_world(sub, it); floor_passive()
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.25)
    proto = bpy.context.active_object
    for i in range(-3,4):
        for j in range(-3,4):
            o = proto.copy(); o.data=proto.data; o.location=(i*0.6, j*0.6, 0.25)
            sc.collection.objects.link(o); marble_at(o)
    bpy.data.objects.remove(proto)
    bpy.ops.mesh.primitive_cube_add(size=1.4, location=(0,0,6))
    blk = bpy.context.active_object
    bpy.context.view_layer.objects.active = blk
    bpy.ops.rigidbody.object_add()
    rb=blk.rigid_body; rb.type='ACTIVE'; rb.mass=8.0; rb.restitution=0.5; rb.friction=0.6
    sc.frame_start=1; sc.frame_end=90
    if bake:
        rw = sc.rigidbody_world
        rw.point_cache.frame_start=1; rw.point_cache.frame_end=90
        bpy.ops.ptcache.bake_all(bake=True)
        zs = read_zs(sc, blk, [10,30,50,70,90])
    else:
        zs = []
        for f in range(1,91):
            sc.frame_set(f); bpy.context.view_layer.update()
        zs = [round(blk.matrix_world.translation.z,3)]
    # max radial of marbles
    ds=[]
    for o in sc.objects:
        if o.name.startswith("Sphere"):
            ds.append(math.hypot(o.matrix_world.translation.x, o.matrix_world.translation.y))
    return {"block_z_samples": [round(z,3) for z in zs], "max_radial": round(max(ds),3)}

R["S1_probe8d_bake"] = s1(True)
R["S2_probe8d_scrub"] = s1(False)

# ---------- S3: my scenario, scrub from frame 1
def s3():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    make_world(12,12); floor_passive()
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, radius=0.25)
    proto = bpy.context.active_object
    marbles=[]
    for i in range(15):
        for j in range(11):
            o = proto.copy(); o.data=proto.data; o.location=((i-7)*0.56,(j-5)*0.56,0.25)
            sc.collection.objects.link(o); marble_at(o, 0.2, 0.65, 0.42, 0.08, 0.5)
            marbles.append(o)
    bpy.data.objects.remove(proto)
    bpy.ops.object.text_add()
    t = bpy.context.active_object
    t.data.body="PLAY"; t.data.size=1; t.data.extrude=0.3; t.data.bevel_depth=0.07; t.data.bevel_resolution=4
    bpy.ops.object.convert(target='MESH')
    play = bpy.context.active_object
    me=play.data; n=len(me.vertices); co=np.empty(n*3,np.float32); me.vertices.foreach_get("co",co); co=co.reshape(-1,3)
    s=2.55/(co[:,0].max()-co[:,0].min())
    co[:,0]=(co[:,0]-(co[:,0].min()+co[:,0].max())/2)*s; co[:,1]=(co[:,1]-co[:,1].min())*s; co[:,2]=(co[:,2]-(co[:,2].min()+co[:,2].max())/2)*s
    me.vertices.foreach_set("co",co.ravel()); me.update()
    play.rotation_euler=(math.pi/2,0,0); play.location=(0,0,4.2)
    bpy.context.view_layer.objects.active=play
    bpy.ops.rigidbody.object_add()
    rb=play.rigid_body; rb.type='ACTIVE'; rb.mass=8; rb.friction=0.8; rb.restitution=0.5; rb.linear_damping=0.015; rb.angular_damping=0.8
    sc.frame_start=1; sc.frame_end=299
    base = np.array([o.location[:] for o in marbles])
    zs=[]; disp=[]
    for f in range(1,300):
        sc.frame_set(f); bpy.context.view_layer.update()
        if f%30==0 or f in (92,94,96,98,100,102,104,106,110,120):
            zs.append((f, round(play.matrix_world.translation.z,3)))
        d = max(math.hypot(o.matrix_world.translation.x-base[k,0], o.matrix_world.translation.y-base[k,1]) for k,o in enumerate(marbles))
        disp.append(round(d,3))
    return {"playz": zs, "disp_every30": disp[::30], "max_disp": max(disp)}

R["S3_mine_scrub_from1"] = s3()
json.dump(R, open("_dev_sim4_out.json","w"), indent=1, default=str)
print("SIM4_DONE")
