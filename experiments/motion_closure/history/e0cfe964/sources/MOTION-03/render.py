#!/usr/bin/env python3 -X utf8
"""
MOTION-03 / 03-isometric — deterministic pure-Python isometric raster renderer.

Card 03 (等轴 2.5D / ISO 2.5D), governing text origin/提示词全文.md L76-84:
  画风：没有透视，斜线一律 30°，竖线竖直；每个物体顶、左、右三面用同一色相的
  三档明暗，光始终从同一边来；东西是长出来的：先落地基，再升墙，最后盖顶；
  镜头只平移、不换角度；物体之间用沿网格走的传送带或管道连着，小方块在上面流动。
  内容：【图书馆的还书分拣：书从还书口进来，沿传送带按颜色分到各层书架；最后拉远，
  地面上斜着印出「书归原位」】
  别做成：带透视、三面明暗不统一、转镜头。

render_frame(n, seed) is a PURE function: every pixel is a closed-form integer
function of the frame index n and the frozen integer seed. No wall clock, no RNG,
no inter-frame mutable state, no browser/compositor. t = n / 30 (C2/C3). This is
what makes out-of-order / pause-resume / new-process re-renders byte-identical by
construction and empirically verifiable (determinism.py).

Modes:
  python -X utf8 render.py keys            -> stills/k0..k5.png (6 keyframes FIRST)
  python -X utf8 render.py all            -> 300 frames frames/f0000..f0299.png + frames/frame_hashes.json + keyframe_manifest.json
  python -X utf8 render.py batch n,n,..   -> only those frames into frames/, prints JSON {n: sha256}
"""
import hashlib
import json
import math
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
FRAME_DIR = HERE / "frames"
STILL_DIR = HERE / "stills"

SEED = 20261115
FPS = 30
FRAMES = 300
W, H = 960, 540

# ---- canonical palette: one hue (teal) in THREE shades + paper/ink neutrals ----
# 同屏 <= 1 hue. light from upper-left (fixed). top=bright, left=mid, right=dark,
# all three faces are the SAME hue with three brightness levels (three-face rule).
# The three shades are EXACT integer multiples of one base hue (BASE_TEAL), so
# R:G:B ratio is identical to within rounding for all three faces (provable).
PAPER = (238, 234, 222)        # 纸色 background
INK = (26, 30, 34)            # ink / outlines
BASE_TEAL = (86, 196, 178)
HUE_TOP = tuple(round(x * 1.00) for x in BASE_TEAL)   # (86,196,178) bright
HUE_LEFT = tuple(round(x * 0.74) for x in BASE_TEAL)  # (64,145,132) mid
HUE_RIGHT = tuple(round(x * 0.52) for x in BASE_TEAL) # (45,102,93)  dark
BELT = (200, 198, 186)        # neutral conveyor
BELT_EDGE = (120, 122, 116)   # neutral belt outline
BOOK_RED = (198, 92, 78)      # flowing book blocks (color-sort accents)
BOOK_YELLOW = (222, 184, 70)
BOOK_BLUE = (86, 120, 176)
ACCENTS = [BOOK_RED, BOOK_YELLOW, BOOK_BLUE]

KEYFRAMES = [
    (0,   "GRID_ONLY"),
    (45,  "FOUNDATION"),
    (120, "WALLS_RISING"),
    (180, "ROOF_CAPPED"),
    (240, "PAN_AND_FLOW"),
    (285, "END_COPY_POSTER"),
]

# ---- 30° isometric basis (orthographic, NO perspective, NO vanishing point) ----
# e_x = (cos30, sin30) ~ (0.866, 0.5); e_y = (-cos30, sin30) ~ (-0.866, 0.5).
# To keep the slope EXACTLY 30° while staying in integer pixels we use the
# integer direction pair (866, 500) / (-866, 500) scaled by UNIT/1000, i.e. every
# "iso step" of g grid units moves (g*866/1000*SCALE, g*500/1000*SCALE). The
# tangent of the slope is exactly 500/866 = tan(30°) up to the rational 0.5773.
# For raster determinism we pre-quantize to integer pixel deltas via round().
COS30 = 866   # x-component per 1000 of an iso axis unit
SIN30 = 500   # y-component per 1000 of an iso axis unit
ISO_SCALE = 46  # pixels per grid unit along each iso axis (scales both components)


def iround(v):
    """Deterministic integer rounding (half away from zero, no float banker drift)."""
    return int(math.floor(v + 0.5)) if v >= 0 else -int(math.floor(-v + 0.5))


def iso(u, v, z=0):
    """Project grid coords (u,v) and height z to screen. Diagonals follow exact
    30° slope; vertical edges are pure vertical (z only changes y)."""
    x = iround((u - v) * COS30 * ISO_SCALE / 1000)
    y = iround((u + v) * SIN30 * ISO_SCALE / 1000) - z
    return x, y


def camera_pan(n):
    """镜头只平移、不换角度: ONLY integer translation, basis NEVER changes.
    Linear pan (no overshoot/bounce): -0.30 px/frame in x, +0.10 px/frame in y,
    clamped so the scene stays in frame. Pure integer function of n."""
    dx = -iround(n * 3 / 10)     # -0.30 px/frame
    dy = iround(n * 1 / 10)      # +0.10 px/frame
    return dx, dy


def scene_pan(n):
    """A single global translation applied to ALL vertices (camera pan only)."""
    return camera_pan(n)


def apply(vtx, pan):
    dx, dy = pan
    return [(x + dx, y + dy) for (x, y) in vtx]


def center_offset():
    # place grid origin near horizontal center, lower-middle vertically
    return W // 2, int(H * 0.62)


def P(u, v, z, pan):
    x, y = iso(u, v, z)
    ox, oy = center_offset()
    return (x + ox + pan[0], y + oy + pan[1])


# ---- growth schedule (pre-registered in schedule.json) ----------------------
# per building: foundation appears over a short drop, walls rise by scaleY,
# roof caps ~2 frames AFTER walls finish (顶面延迟 2~3 帧, compare.md §2.1 row3).
# "东西是长出来的：先落地基，再升墙，最后盖顶" — strict order, no overlaps that
# would show a roof before its walls.
BUILDINGS = [
    # (u, v, base_w, base_d, max_h, f_start, accent)
    (-3, -1, 3, 2, 84, 1,   BOOK_RED),
    (0,  -2, 2, 3, 108, 61,  BOOK_YELLOW),
    (2,  2,  3, 2, 72, 121, BOOK_BLUE),
]

FOUND_DUR = 30      # foundation drop-in window
WALL_DUR = 60       # walls rise window
ROOF_DELAY = 2      # roof caps 2 frames after walls complete
ROOF_DUR = 12       # roof settle window


def growth(n, b):
    """Return (phase, frac) for building b at frame n. Deterministic integer math.
    phase: 0=absent 1=foundation 2=walls 3=roof 4=complete.
    frac: 0..1 progress within phase (as float 0..1 from integer ratio)."""
    u, v, bw, bd, max_h, start, accent = b
    t = n - start
    if t < 0:
        return 0, 0.0
    if t < FOUND_DUR:
        return 1, t / FOUND_DUR
    t -= FOUND_DUR
    if t < WALL_DUR:
        return 2, t / WALL_DUR
    t -= WALL_DUR
    if t < ROOF_DELAY:
        return 2, 1.0  # walls fully up, roof not yet (the 2-frame delay)
    t -= ROOF_DELAY
    if t < ROOF_DUR:
        return 3, t / ROOF_DUR
    return 4, 1.0


def draw_ground(draw, pan):
    """Isometric ground grid — all diagonals at 30°, no perspective (parallel)."""
    G = 7
    for i in range(-G, G + 1):
        a = P(i, -G, 0, pan)
        b = P(i, G, 0, pan)
        draw.line([a, b], fill=(214, 210, 198), width=1)
        a = P(-G, i, 0, pan)
        b = P(G, i, 0, pan)
        draw.line([a, b], fill=(214, 210, 198), width=1)


def quad(draw, pts, fill, outline=INK):
    draw.polygon(pts, fill=fill)
    draw.line(list(pts) + [pts[0]], fill=outline, width=1)


def draw_box(draw, u, v, w, d, h, pan, top=HUE_TOP, left=HUE_LEFT, right=HUE_RIGHT):
    """Axis-aligned iso box with 3 visible faces, SAME hue in 3 tones.
    top face bright, left face mid, right face dark; light fixed from upper-left.
    Vertical edges are pure vertical (z maps to y only)."""
    # 8 corners in grid space
    p000 = P(u,     v,     h, pan)
    p100 = P(u + w, v,     h, pan)
    p110 = P(u + w, v + d, h, pan)
    p010 = P(u,     v + d, h, pan)
    g000 = P(u,     v,     0, pan)
    g100 = P(u + w, v,     0, pan)
    g110 = P(u + w, v + d, 0, pan)
    g010 = P(u,     v + d, 0, pan)
    # top face (bright)
    quad(draw, [p000, p100, p110, p010], top)
    # left face (mid): u=const plane -> vertical edges
    quad(draw, [p000, p010, g010, g000], left)
    # right face (dark): v=const plane -> vertical edges
    quad(draw, [p100, g100, g110, p110], right)


def draw_foundation(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    # foundation slab drops in from z = 20*(1-frac) to 0; thin slab h=10
    z = iround(20 * (1.0 - frac))
    draw_box(draw, u, v, bw, bd, 10 + z, pan,
             top=(150, 146, 134), left=(120, 118, 108), right=(96, 96, 88))


def draw_walls(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    h = iround(max_h * frac)
    if h <= 0:
        return
    draw_box(draw, u, v, bw, bd, h, pan)


def draw_roof(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    h = max_h
    z = iround(16 * (1.0 - frac))  # roof settles down 16px onto the walls
    draw_box(draw, u, v, bw, bd, h + z + 8, pan,
             top=HUE_TOP, left=HUE_LEFT, right=HUE_RIGHT)


def draw_complete(draw, b, pan):
    u, v, bw, bd, max_h, start, accent = b
    draw_box(draw, u, v, bw, bd, max_h, pan)
    # a thin roof slab (already capped) with a "shelf" accent band per building
    top = P(u, v, max_h + 8, pan)
    p100 = P(u + bw, v, max_h + 8, pan)
    p110 = P(u + bw, v + bd, max_h + 8, pan)
    p010 = P(u, v + bd, max_h + 8, pan)
    quad(draw, [top, p100, p110, p010], HUE_TOP)
    # shelf slits (color-sort bins) on the front-right face, accent hue per building
    for k in range(1, 4):
        zz = iround(max_h * k / 5)
        a = P(u + bw, v, zz, pan)
        bb = P(u + bw, v + bd, zz, pan)
        draw.line([a, bb], fill=accent, width=1)


# ---- conveyor belt along the iso grid + flowing small blocks -----------------
# Path follows iso grid axes ONLY (沿网格走). u,v waypoints on the grid.
BELT_PATH = [(-4, 3), (-1, 3), (-1, 0), (1, 0), (1, 3), (4, 3)]


def belt_pos(s):
    """Position along the polyline belt at arc-length fraction s in [0,1).
    Returns (grid_u, grid_v) on grid-aligned segments. Deterministic."""
    segs = []
    total = 0.0
    for i in range(len(BELT_PATH) - 1):
        a, b = BELT_PATH[i], BELT_PATH[i + 1]
        L = abs(b[0] - a[0]) + abs(b[1] - a[1])  # grid Manhattan length
        segs.append((a, b, L))
        total += L
    d = (s % 1.0) * total
    for (a, b, L) in segs:
        if d <= L or (a, b, L) is segs[-1]:
            f = 0.0 if L == 0 else d / L
            return a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f
        d -= L
    return BELT_PATH[-1]


def draw_belt(draw, pan):
    # belt as a thick neutral line following the iso grid path (not diagonal cuts)
    pts = [P(u, v, 0, pan) for (u, v) in BELT_PATH]
    draw.line(pts, fill=BELT_EDGE, width=8)
    draw.line(pts, fill=BELT, width=6)


def draw_flow(draw, n, pan):
    """小方块在上面流动: small colored book-blocks flow along the belt at
    integer-derived positions. Pure function of n (no state)."""
    for i in range(6):
        # each block advances by a constant speed; s = (n*speed + phase) / span
        s = ((n * 0.0042) + i / 6.0) % 1.0
        u, v = belt_pos(s)
        col = ACCENTS[i % len(ACCENTS)]
        # small iso cube sitting on the belt
        z0 = 2
        draw_box(draw, u - 0.16, v - 0.16, 0.32, 0.32, z0 + 10, pan,
                 top=col, left=col, right=col)


# ---- end copy 「书归原位」 drawn diagonally on the ground (iso plane) --------
# 最后拉远，地面上斜着印出「书归原位」: 4 CJK glyphs as documented 9x9 bitmaps,
# laid along the 30° iso direction (each glyph shifted along e_x). Appears
# (pre-registered) from frame 240; no bundled font, no external asset.
# Each glyph is a 9x9 bitmap (1 = ink pixel). Documented, deterministic.
GLYPHS = {
    "书": [
        "000100000", "000100000", "011111100", "000100000", "000100010",
        "000101010", "000100100", "000100000", "001111000"],
    "归": [
        "000100010", "000100010", "011111110", "010010010", "010010010",
        "010101010", "010100100", "010000000", "001111000"],
    "原": [
        "001111100", "001000000", "001000000", "011111110", "010100010",
        "010100010", "010100010", "010011100", "001000000"],
    "位": [
        "000010000", "000111100", "001000010", "011111110", "001000010",
        "001000010", "001111100", "001000010", "001000010"],
}
COPY_TEXT = "书归原位"


def draw_copy(draw, n, pan):
    """Diagonal ground text along the 30° iso axis. Appears from frame 240,
    drawn with integer iso steps so the baseline of the text follows e_x."""
    if n < 240:
        return
    # fade-in is NOT a cross-dissolve of shapes; the glyphs are simply stamped
    # with growing ink coverage (still pure integer function of n), no alpha.
    grow = min(1.0, (n - 240) / 30.0)
    start_u, start_v = -3.2, 4.4
    glyph_w = 1.05  # grid units between glyph origins along e_x
    px = 5          # pixels per bitmap cell (scaled on the iso ground)
    for gi, ch in enumerate(COPY_TEXT):
        rows = GLYPHS[ch]
        u0 = start_u + gi * glyph_w
        for r, row in enumerate(rows):
            for c, bit in enumerate(row):
                if bit != "1":
                    continue
                # stagger columns by coverage grow (mechanical, not opacity)
                if (r * 9 + c) / 81.0 > grow:
                    continue
                # each bitmap cell maps to a small iso ground quad
                du = c * 0.11
                dv = r * 0.11
                gx = P(u0 + du, start_v + dv, 0, pan)
                gy = P(u0 + du + 0.08, start_v + dv, 0, pan)
                gz = P(u0 + du + 0.08, start_v + dv + 0.08, 0, pan)
                gw = P(u0 + du, start_v + dv + 0.08, 0, pan)
                draw.polygon([gx, gy, gz, gw], fill=INK)


def draw_header(draw, n):
    # small fixed HUD label (neutral ink) — pure function, no clock
    draw.text((14, 12), "MOTION-03  ISO 2.5D  /  LIBRARY SORT", fill=INK)
    draw.text((14, H - 22), "frame %03d / 300   t = %.2fs" % (n, n / FPS), fill=INK)


def render_frame(n, seed=SEED):
    """PURE function of (n, seed). Returns a PIL Image. No clock/RNG/state."""
    n = int(n)
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    pan = scene_pan(n)
    draw_ground(draw, pan)
    draw_belt(draw, pan)
    # buildings in strict growth order (foundation -> walls -> roof -> complete)
    for b in BUILDINGS:
        phase, frac = growth(n, b)
        if phase == 1:
            draw_foundation(draw, b, frac, pan)
        elif phase == 2:
            draw_walls(draw, b, frac, pan)
        elif phase == 3:
            # walls fully drawn, then roof settles
            draw_walls(draw, b, 1.0, pan)
            draw_roof(draw, b, frac, pan)
        elif phase == 4:
            draw_complete(draw, b, pan)
    draw_flow(draw, n, pan)
    draw_copy(draw, n, pan)
    draw_header(draw, n)
    return img


def frame_path(n):
    return FRAME_DIR / ("f%04d.png" % n)


def sha_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_frame(n, img=None):
    FRAME_DIR.mkdir(parents=True, exist_ok=True)
    if img is None:
        img = render_frame(n)
    img.save(frame_path(n), format="PNG", compress_level=9, optimize=False)
    return sha_of(frame_path(n))


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode == "keys":
        STILL_DIR.mkdir(parents=True, exist_ok=True)
        manifest = []
        for i, (n, slug) in enumerate(KEYFRAMES):
            p = STILL_DIR / ("k%d.png" % i)
            render_frame(n).save(p, format="PNG", compress_level=9, optimize=False)
            manifest.append({"keyframe": slug, "index": i, "frame": n,
                             "t_seconds": n / FPS, "path": "stills/k%d.png" % i,
                             "sha256": sha_of(p)})
        (HERE / "keyframe_manifest.json").write_text(
            json.dumps({"card": "03", "slug": "03-isometric", "seed": SEED,
                        "fps": FPS, "keyframes": manifest}, indent=2, ensure_ascii=False),
            encoding="utf-8")
        print(json.dumps({"mode": "keys", "keyframes": len(manifest), "ok": True}))
    elif mode == "all":
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        hashes = {}
        for n in range(FRAMES):
            hashes["%04d" % n] = save_frame(n)
        (FRAME_DIR / "frame_hashes.json").write_text(
            json.dumps({"seed": SEED, "fps": FPS, "frames": FRAMES,
                        "resolution": [W, H],
                        "renderer": "pure-python-pillow-raster-isometric@1.0.0",
                        "hashes": hashes}, indent=1, sort_keys=True),
            encoding="utf-8")
        print(json.dumps({"mode": "all", "frames": FRAMES, "ok": True}))
    elif mode == "batch":
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        out = {}
        for tok in sys.argv[2].split(","):
            n = int(tok)
            out[n] = save_frame(n)
        print(json.dumps(out))
    else:
        print("usage: render.py keys|all|batch [n,n,..]", file=sys.stderr)
        sys.exit(2)


# ---- exported semantics for verify.py (verifier diffs the REAL shipped funcs) ----
def iso_basis():
    """The two 30° diagonal basis directions (per iso-axis step), in pixel units
    for a unit grid step. Slopes are exactly +sin30/cos30 and -sin30/cos30."""
    return (COS30, SIN30), (-COS30, SIN30)


def growth_order():
    """Strict phase order enforced by the renderer: foundation, walls, roof."""
    return ["foundation", "walls", "roof", "complete"]


def face_palette():
    return {"top": HUE_TOP, "left": HUE_LEFT, "right": HUE_RIGHT}


if __name__ == "__main__":
    main()
