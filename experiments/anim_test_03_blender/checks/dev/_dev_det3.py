import bpy, os, hashlib
import numpy as np
BASE = os.path.dirname(os.path.abspath(__file__))
sc = bpy.context.scene
sc.render.use_motion_blur = False
def sha(p):
    h = hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(1<<20), b''): h.update(c)
    return h.hexdigest()
def load(p):
    im = bpy.data.images.load(p)
    a = np.empty(len(im.pixels), np.float32); im.pixels.foreach_get(a)
    w,h = im.size; ch = im.channels
    bpy.data.images.remove(im)
    return a.reshape(h,w,ch)[...,:3]
outs = []
for i in range(2):
    p = os.path.join(BASE, 'checks', 'detm_%d.png' % i)
    sc.frame_set(30)
    sc.render.filepath = p
    bpy.ops.render.render(write_still=True)
    outs.append(sha(p))
print("NO-MB f30:", outs[0][:16], outs[1][:16], "MATCH" if outs[0]==outs[1] else "DIFFER")
# pixel diff of the MB-on same-process pair
a = load(os.path.join(BASE,'checks','det_0.png')); b = load(os.path.join(BASE,'checks','det_1.png'))
d = np.abs(a-b)
print("MB-on pair pixel diff: mean %.8f max %.6f frac>1/255 %.7f" % (d.mean(), d.max(), (d.max(axis=2)>1/255).mean()))
