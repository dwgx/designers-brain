"""checks/selfcheck_frames.py — per-frame luminance / jump stats over frames/ (逐帧自查).
Run: blender -b --factory-startup -P checks/selfcheck_frames.py
"""
import bpy, os, json
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FD = os.path.join(BASE, "frames")
files = sorted(f for f in os.listdir(FD) if f.endswith(".png"))
print("frame count:", len(files), flush=True)

stats = []
prev = None
for i, fn in enumerate(files):
    im = bpy.data.images.load(os.path.join(FD, fn))
    a = np.empty(len(im.pixels), np.float32)
    im.pixels.foreach_get(a)
    w, h = im.size
    a = a.reshape(h, w, im.channels)
    lum = a[::4, ::4, :3].mean(axis=2)
    m = float(lum.mean()); mn = float(lum.min()); mx = float(lum.max())
    d = float(np.abs(lum - prev).mean()) if prev is not None else 0.0
    prev = lum
    stats.append({"file": fn, "w": w, "h": h, "mean": m, "min": mn, "max": mx, "d": d})
    bpy.data.images.remove(im)
    if i % 50 == 0:
        print("..", fn, flush=True)

means = np.array([s["mean"] for s in stats])
ds = np.array([s["d"] for s in stats])
med = float(np.median(ds[1:]))
print("global mean range: %.4f .. %.4f" % (means.min(), means.max()))
print("frame-to-frame mean-lum delta: median %.5f | max %.5f at %s" % (med, ds.max(), stats[int(ds.argmax())]["file"]))
flags = []
for s in stats:
    if s["mean"] < 0.01 or s["mean"] > 0.99:
        flags.append((s["file"], "mean out of range", round(s["mean"], 4)))
    if s["d"] > max(6 * med, 0.004):
        flags.append((s["file"], "large jump", round(s["d"], 5)))
    if s["file"] != files[0] and s["d"] < 0.00005:
        flags.append((s["file"], "frozen?", round(s["d"], 6)))
print("flags:", flags if flags else "none")
top = sorted(stats, key=lambda s: -s["d"])[:8]
print("top jumps:", [(s["file"], round(s["d"], 5)) for s in top])
json.dump({"count": len(stats), "mean_range": [float(means.min()), float(means.max())],
           "d_median": med, "d_max": float(ds.max()), "flags": flags,
           "top_jumps": [(s["file"], float(s["d"])) for s in top]},
          open(os.path.join(BASE, "checks", "selfcheck_stats.json"), "w"), indent=1)
print("SELFCHECK_DONE", flush=True)
