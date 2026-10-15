import bpy, os
import numpy as np
BASE = os.path.dirname(os.path.abspath(__file__))
sc = bpy.context.scene
sc.render.resolution_percentage = 50
sc.eevee.taa_render_samples = 32
sc.render.use_motion_blur = False
cd = sc.camera.data
cd.dof.aperture_fstop = 22.0
sc.frame_set(250)
p = os.path.join(BASE, "checks", "mech", "dof_f250_f22.png")
sc.render.filepath = p
bpy.ops.render.render(write_still=True)
def load(p):
    im = bpy.data.images.load(p)
    a = np.empty(len(im.pixels), np.float32); im.pixels.foreach_get(a)
    w,h = im.size; ch = im.channels
    bpy.data.images.remove(im)
    return a.reshape(h,w,ch)[...,:3]
a = load(p)
b = load(os.path.join(BASE, "checks", "mech", "dof_f250.png"))
d = np.abs(a-b).mean(axis=2)
h, w = d.shape
def reg(r0, r1, c0, c1):  # rows from top
    return float(d[int(h*r0):int(h*r1), int(w*c0):int(w*c1)].mean())
print("f22 vs f1.1 diff: focus(45-65%%) %.5f | near(80-100%%) %.5f | far(30-40%%) %.5f | full %.5f" % (
    reg(0.45, 0.65, 0.30, 0.70), reg(0.80, 1.00, 0.10, 0.90), reg(0.30, 0.40, 0.05, 0.95), float(d.mean())))
print("DOF3_DONE")
