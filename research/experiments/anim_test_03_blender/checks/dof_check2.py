"""checks/dof_check2.py — cleaner DOF measurement: same content (marbles) at different depths.
Run: blender -b --factory-startup -P checks/dof_check2.py
"""
import bpy, os
import numpy as np
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
im = bpy.data.images.load(os.path.join(BASE, "frames", "f0250.png"))
a = np.empty(len(im.pixels), np.float32); im.pixels.foreach_get(a)
w, h = im.size; ch = im.channels
bpy.data.images.remove(im)
lum = a.reshape(h, w, ch)[..., :3].mean(axis=2)
lap = np.abs(4 * lum[1:-1, 1:-1] - lum[:-2, 1:-1] - lum[2:, 1:-1] - lum[1:-1, :-2] - lum[1:-1, 2:])
def reg(r0, r1, c0, c1):
    return float(lap[int(h*r0):int(h*r1), int(w*c0):int(w*c1)].mean())
# note: image rows are bottom-up in Blender pixel buffers -> row 0 = BOTTOM of image
# regions chosen on the LEFT-CENTER strip where marbles fill all depths:
focus  = reg(0.42, 0.62, 0.30, 0.70)   # around the letters (in focus, ~7.6m)
mid    = reg(0.20, 0.38, 0.10, 0.90)   # mid-field marbles (~9-10m, mild blur)
near   = reg(0.02, 0.18, 0.10, 0.90)   # nearest marbles (~5m, strong blur)
far    = reg(0.62, 0.78, 0.05, 0.95)   # far field marbles (~11-12m, blurred)
print("laplacian mean: focus=%.5f mid=%.5f near=%.5f far=%.5f" % (focus, mid, near, far))
print("ratios: focus/near=%.2f focus/far=%.2f mid/near=%.2f" % (focus/max(near,1e-9), focus/max(far,1e-9), mid/max(near,1e-9)))
print("DOF2_DONE")
