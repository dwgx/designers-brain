import bpy, os, hashlib
BASE = os.path.dirname(os.path.abspath(__file__))
sc = bpy.context.scene
sc.eevee.ray_tracing_options.use_denoise = False
def sha(p):
    h = hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(1<<20), b''): h.update(c)
    return h.hexdigest()
outs = []
for i in range(2):
    p = os.path.join(BASE, 'checks', 'detn_%d.png' % i)
    sc.frame_set(30)
    sc.render.filepath = p
    bpy.ops.render.render(write_still=True)
    outs.append(sha(p))
print("NO-DENOISE f30:", outs[0][:16], outs[1][:16], "MATCH" if outs[0]==outs[1] else "DIFFER")
