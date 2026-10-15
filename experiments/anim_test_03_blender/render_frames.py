"""render_frames.py — render stills/sequence from the current .blend (used for tests, keys, full render, rerun checks).

Usage:
  blender -b scene.blend -P render_frames.py -- --frames 0,50,100 --pct 50 --samples 32 --out checks/test
  blender -b scene.blend -P render_frames.py -- --range 0:299 --out frames
Args (after --): --frames a,b,c | --range a:b | --pct N | --samples N | --out DIR | --nomb | --mb-steps N | --skip
"""
import bpy, sys, os, time, argparse

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
ap = argparse.ArgumentParser()
ap.add_argument('--frames', default='0')
ap.add_argument('--range', default=None)
ap.add_argument('--pct', type=int, default=100)
ap.add_argument('--samples', type=int, default=0)
ap.add_argument('--out', default='checks/test')
ap.add_argument('--nomb', action='store_true')
ap.add_argument('--mb-steps', type=int, default=0)
ap.add_argument('--skip', action='store_true')
ap.add_argument('--tag', default='')
a = ap.parse_args(argv)

sc = bpy.context.scene
sc.render.resolution_percentage = a.pct
if a.samples:
    sc.eevee.taa_render_samples = a.samples
if a.nomb:
    sc.render.use_motion_blur = False
if a.mb_steps:
    sc.eevee.motion_blur_steps = a.mb_steps

BASE = os.path.dirname(os.path.abspath(__file__))
od = a.out if os.path.isabs(a.out) else os.path.join(BASE, a.out)
os.makedirs(od, exist_ok=True)

if a.range:
    f0, f1 = (int(x) for x in a.range.split(':'))
    frames = list(range(f0, f1 + 1))
else:
    frames = [int(x) for x in a.frames.split(',')]

print("RENDER_START", {"frames": len(frames), "pct": a.pct, "samples": sc.eevee.taa_render_samples,
                       "mb": sc.render.use_motion_blur, "mb_steps": sc.eevee.motion_blur_steps, "out": od}, flush=True)
t_all = time.time()
for i, f in enumerate(frames):
    path = os.path.join(od, "f%04d%s.png" % (f, a.tag))
    if a.skip and os.path.exists(path):
        print("SKIP", f, flush=True)
        continue
    t0 = time.time()
    sc.frame_set(f)
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("FRAME %d %.1fs" % (f, time.time() - t0), flush=True)
print("RENDER_DONE %.1fs for %d frames" % (time.time() - t_all, len(frames)), flush=True)
