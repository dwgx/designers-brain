import bpy, os
import numpy as np
BASE = os.path.dirname(os.path.abspath(__file__))
def load(p):
    im = bpy.data.images.load(p)
    a = np.empty(len(im.pixels), np.float32); im.pixels.foreach_get(a)
    w,h = im.size; ch = im.channels
    bpy.data.images.remove(im)
    return a.reshape(h,w,ch)[...,:3]
for f in (123, 234):
    a = load(os.path.join(BASE,'checks','rerun','f%04d.png' % f))
    b = load(os.path.join(BASE,'frames','f%04d.png' % f))
    d = np.abs(a-b)
    print('f%d: mean %.8f | max %.6f | frac>1/255 %.8f' % (f, d.mean(), d.max(), (d.max(axis=2)>1/255).mean()))
