"""checks/rerun_check.py — 乱序重渲抽查: re-render 2 frames out of order from scene.blend, compare to frames/.
Run: blender -b scene.blend -P checks/rerun_check.py -- --frames 123,234
Writes checks/rerun/ + prints sha256 comparison (captured to checks/rerun_check.txt).
"""
import bpy, sys, os, hashlib, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
frames = [int(x) for x in (argv[argv.index('--frames') + 1].split(',') if '--frames' in argv else ['123', '234'])]
OD = os.path.join(BASE, "checks", "rerun")
os.makedirs(OD, exist_ok=True)

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()

sc = bpy.context.scene
for f in frames:
    sc.frame_set(f)
    p = os.path.join(OD, "f%04d.png" % f)
    sc.render.filepath = p
    t0 = time.time()
    bpy.ops.render.render(write_still=True)
    ref = os.path.join(BASE, "frames", "f%04d.png" % f)
    a = sha(p)
    b = sha(ref) if os.path.exists(ref) else "MISSING"
    print("frame %d: rerun %s | original %s | %s (%.1fs)" % (
        f, a[:16], b[:16] if b != "MISSING" else b, "MATCH" if a == b else "DIFFER", time.time() - t0), flush=True)
print("RERUN_DONE", flush=True)
