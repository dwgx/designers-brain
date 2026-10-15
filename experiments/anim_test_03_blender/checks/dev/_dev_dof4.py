import bpy, os
import numpy as np
BASE = os.path.dirname(os.path.abspath(__file__))
def load(p):
    im = bpy.data.images.load(p)
    a = np.empty(len(im.pixels), np.float32); im.pixels.foreach_get(a)
    w,h = im.size; ch = im.channels
    bpy.data.images.remove(im)
    return a.reshape(h,w,ch)[...,:3]
a = load(os.path.join(BASE, "checks", "mech", "dof_f250_f22.png"))
b = load(os.path.join(BASE, "checks", "mech", "dof_f250.png"))
d = np.abs(a-b).mean(axis=2)
h, w = d.shape
# array row 0 = BOTTOM of displayed image
def reg(r0, r1, c0, c1):
    return float(d[int(h*r0):int(h*r1), int(w*c0):int(w*c1)].mean())
print("f22 vs f1.1 | displayed-bottom(near) %.5f | mid-focus(letters zone) %.5f | upper(far field) %.5f | top(backdrop) %.5f" % (
    reg(0.00, 0.18, 0.10, 0.90), reg(0.42, 0.62, 0.30, 0.70), reg(0.74, 0.88, 0.05, 0.95), reg(0.92, 1.00, 0.05, 0.95)))
