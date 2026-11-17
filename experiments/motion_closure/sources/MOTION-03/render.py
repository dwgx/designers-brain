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

render_frame(n, seed) is a PURE function: every pixel is a closed-form
function of the frame index n and the frozen integer seed. No wall clock, no RNG,
no inter-frame mutable state, no browser/compositor. t = n / 30 (C2/C3). This is
what makes out-of-order / pause-resume / new-process re-renders byte-identical by
construction and empirically verifiable (determinism.py).

Modes (all accept --outdir DIR; the default DIR is this source directory):
  python -B render.py keys           -> stills/fNNNN.png for six declared keyframes
  python -B render.py all            -> frames/f0000.png through frames/f0299.png
  python -B render.py batch n,n,...  -> only those frames in frames/
Every mode writes DIR/render_manifest.json and prints JSON containing hashes.
This candidate does not write the original frame_hashes/keyframe manifests.
"""
import argparse
import hashlib
import json
import math
import os
import sys
from pathlib import Path
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont, __version__ as PILLOW_VERSION

HERE = Path(__file__).resolve().parent
FRAME_DIR = HERE / "frames"
STILL_DIR = HERE / "stills"

SEED = 20261115
FPS = 30
FRAMES = 300
LOGICAL_W, LOGICAL_H = 960, 540
RASTER_SCALE = 2
W, H = 1920, 1080
ORIGINAL_SOURCE_SHA256 = "d6493df994d176ccc2c60c321cabc273047ef4e6564360313ad6029216138289"
RENDERER_VERSION = "isometric-native-pillow@2.3.0-proposed"
PREVIOUS_NATIVE_SOURCE_SHA256 = "3dc2a0140ff3ec2ca790ae5f4a84e62a13da7842305e2f91661fd479fdb595d4"
SCENE_Y_OFFSET = -80  # logical units; reserve bottom HUD / final-building margin
# This source never creates a low-resolution scene image. Coordinates remain
# continuous in logical space until P() maps each vertex to the native canvas.
# The original seed parameter was unused. We retain that honest interface.
HEADER_FONT = ImageFont.load_default(size=20)
COPY_TEXT = "书归原位"
COPY_FONT_SIZE = 192  # glyph source density exceeds the final ground footprint
COPY_START = (-3.4, 4.4)
COPY_U_SPAN = 4.85
COPY_V_DEPTH = 1.14
FONT_PATH = os.environ.get("MOTION03_FONT")
if FONT_PATH is None:
    FONT_PATH = next((str(p) for p in (
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    ) if p.is_file()), None)
FONT_INDEX = int(os.environ.get("MOTION03_FONT_INDEX", "0"))


@lru_cache(maxsize=1)
def copy_font():
    if not FONT_PATH or not Path(FONT_PATH).is_file():
        raise RuntimeError("A CJK font is required; set MOTION03_FONT. No abstract-glyph fallback.")
    f = ImageFont.truetype(FONT_PATH, COPY_FONT_SIZE, index=FONT_INDEX)
    missing = f.getmask("\U0010ffff")
    fingerprint = (missing.size, bytes(missing))
    for ch in COPY_TEXT:
        mask = f.getmask(ch)
        if (mask.size, bytes(mask)) == fingerprint or not any(bytes(mask)):
            raise RuntimeError("Selected font is missing required CJK glyph: " + ch)
    return f


@lru_cache(maxsize=1)
def font_evidence():
    f = copy_font()
    return {"file_name": Path(FONT_PATH).name, "face_index": FONT_INDEX,
            "name": list(f.getname()), "sha256": hashlib.sha256(Path(FONT_PATH).read_bytes()).hexdigest(),
            "required_text": COPY_TEXT, "missing_required_glyphs": [],
            "glyph_raster_size": COPY_FONT_SIZE, "abstract_fallback_used": False}

# ---- canonical palette: one hue (teal) in THREE shades + paper/ink neutrals ----
# Buildings use one teal hue; books use their declared sorting accents.
# Light from upper-left (fixed). top=bright, left=mid, right=dark,
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
# Quantization happens only in P(), after the logical-to-native transform.
COS30 = 866   # x-component per 1000 of an iso axis unit
SIN30 = 500   # y-component per 1000 of an iso axis unit
ISO_SCALE = 46  # pixels per grid unit along each iso axis (scales both components)


def iround(v):
    """Deterministic integer rounding (half away from zero, no float banker drift)."""
    return int(math.floor(v + 0.5)) if v >= 0 else -int(math.floor(-v + 0.5))


def iso(u, v, z=0):
    """Project grid coords (u,v) and height z to screen. Diagonals follow exact
    30° slope; vertical edges are pure vertical (z only changes y)."""
    x = (u - v) * COS30 * ISO_SCALE / 1000
    y = (u + v) * SIN30 * ISO_SCALE / 1000 - z
    return x, y


def camera_pan(n):
    """Original -0.30/+0.10 logical-pixel pan; quantized only at native P()."""
    dx = -n * 3 / 10
    dy = n / 10
    return dx, dy


def camera_zoom(n):
    """Fixed-angle 6% pull-back over frames 240..285; no integer zoom steps."""
    t = min(1.0, max(0.0, (n - 240) / 45.0))
    smooth = t * t * (3.0 - 2.0 * t)
    return 1.0 - 0.06 * smooth


def scene_pan(n):
    """Explicit scene transform (pan_x, pan_y, uniform_zoom), with fixed angle."""
    return (*camera_pan(n), camera_zoom(n))


def apply(vtx, pan):
    dx, dy = pan[:2]
    return [(x + dx, y + dy) for (x, y) in vtx]


def center_offset():
    # place grid origin near horizontal center, lower-middle vertically
    return LOGICAL_W // 2, int(LOGICAL_H * 0.62) + SCENE_Y_OFFSET


def project_native(u, v, z, pan):
    """Continuous native projection. A legacy two-item pan implies unit zoom."""
    x, y = iso(u, v, z)
    ox, oy = center_offset()
    zoom = pan[2] if len(pan) > 2 else 1.0
    return ((x * zoom + ox + pan[0]) * RASTER_SCALE,
            (y * zoom + oy + pan[1]) * RASTER_SCALE)


def P(u, v, z, pan):
    return tuple(iround(x) for x in project_native(u, v, z, pan))


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
        draw.line([a, b], fill=(214, 210, 198), width=RASTER_SCALE)
        a = P(-G, i, 0, pan)
        b = P(G, i, 0, pan)
        draw.line([a, b], fill=(214, 210, 198), width=RASTER_SCALE)


def quad(draw, pts, fill, outline=INK):
    draw.polygon(pts, fill=fill)
    draw.line(list(pts) + [pts[0]], fill=outline, width=RASTER_SCALE)


def draw_box(draw, u, v, w, d, h, pan, top=HUE_TOP, left=HUE_LEFT, right=HUE_RIGHT,
             z0=0):
    """Axis-aligned iso box with 3 visible faces, SAME hue in 3 tones.
    top face bright, left face mid, right face dark; light fixed from upper-left.
    Vertical edges are pure vertical (z maps to y only)."""
    # 8 corners in grid space
    p000 = P(u,     v,     z0 + h, pan)
    p100 = P(u + w, v,     z0 + h, pan)
    p110 = P(u + w, v + d, z0 + h, pan)
    p010 = P(u,     v + d, z0 + h, pan)
    g000 = P(u,     v,     z0, pan)
    g100 = P(u + w, v,     z0, pan)
    g110 = P(u + w, v + d, z0, pan)
    g010 = P(u,     v + d, z0, pan)
    # top face (bright)
    quad(draw, [p000, p100, p110, p010], top)
    # Near-left face is v=v+d, not the hidden parallel u=u face.
    quad(draw, [p010, p110, g110, g010], left)
    # Near-right face is u=u+w; the two side faces share the front edge.
    quad(draw, [p100, g100, g110, p110], right)


def draw_foundation(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    # foundation slab drops in from z = 20*(1-frac) to 0; thin slab h=10
    z = 20 * (1.0 - frac)
    draw_box(draw, u, v, bw, bd, 10 + z, pan,
             top=(150, 146, 134), left=(120, 118, 108), right=(96, 96, 88))


def draw_walls(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    h = max_h * frac
    if h <= 0:
        return
    draw_box(draw, u, v, bw, bd, h, pan)


def draw_roof(draw, b, frac, pan):
    u, v, bw, bd, max_h, start, accent = b
    h = max_h
    z = 16 * (1.0 - frac)  # logical units; P() transforms before rounding
    draw_box(draw, u, v, bw, bd, h + z + 8, pan,
             top=HUE_TOP, left=HUE_LEFT, right=HUE_RIGHT)


def draw_complete(draw, b, pan):
    u, v, bw, bd, max_h, start, accent = b
    draw_box(draw, u, v, bw, bd, max_h, pan)
    # a thin roof slab (already capped) with a "shelf" accent band per building
    draw_box(draw, u, v, bw, bd, 8, pan, z0=max_h)
    # Shelf slots on the visible near-left face; red's old u=max face was hidden
    # behind the adjacent yellow building. Delivered books sit just in front.
    for k in range(1, 4):
        zz = max_h * k / 5
        a = P(u, v + bd, zz, pan)
        bb = P(u + bw, v + bd, zz, pan)
        draw.line([a, bb], fill=accent, width=RASTER_SCALE)
    # A short, grid-aligned lift connects the floor conveyor to these levels.
    port_u, front_v = shelf_port(b)
    draw.line([P(port_u, front_v, 0, pan),
               P(port_u, front_v, max_h * 3 / 5, pan)],
              fill=BELT_EDGE, width=RASTER_SCALE)
    for level in (1, 3):
        z = max_h * level / 5
        draw.line([P(port_u, front_v, z, pan),
                   P(port_u, v + bd, z, pan)],
                  fill=BELT_EDGE, width=RASTER_SCALE)


# ---- finite color routes: floor belt -> lift -> assigned shelf level ---------
# All floor segments follow u or v, and avoid the solid building footprints.
# Six book deliveries replace the old never-ending shared loop; the building
# growth schedule and camera are unchanged. No inter-frame delivery state.
BOOK_APPROACH = 0.38
BOOK_PORT_FRACTIONS = (0.45, 0.20, 0.45)  # yellow slots stay clear of the near blue roof
BOOK_SIZE = (0.32, 0.22, 10)
BOOK_TRAVEL_FRAMES = 60
BOOK_LIFT_FRAMES = 12
BOOK_DOCK_FRAMES = 6
BOOK_ROUTE_STARTS = (36, 96, 156, 72, 132, 192)
BELT_PATH = [(-4, 3), (1.6, 3), (1.6, 4 + BOOK_APPROACH),
             (4.3, 4 + BOOK_APPROACH)]


def shelf_port(b):
    return (b[0] + b[2] * BOOK_PORT_FRACTIONS[BUILDINGS.index(b)],
            b[1] + b[3] + BOOK_APPROACH)


def book_route(target):
    port = shelf_port(BUILDINGS[target])
    if target == 2:
        return [(-4, 3), (1.6, 3), (1.6, port[1]), port]
    return [(-4, 3), (port[0], 3), port]


def route_position(points, fraction):
    """Closed-form Manhattan interpolation, including the exact endpoint."""
    lengths = [abs(b[0] - a[0]) + abs(b[1] - a[1])
               for a, b in zip(points, points[1:])]
    distance = min(1.0, max(0.0, fraction)) * sum(lengths)
    for a, b, length in zip(points, points[1:], lengths):
        if distance <= length:
            t = 0.0 if length == 0 else distance / length
            return a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
        distance -= length
    return points[-1]


def book_state(n, i):
    """The state actually rendered: color i%3 routes to that building, then stays.

    Two books per color occupy levels 1 and 3. First arrivals are 114/174/234;
    second arrivals 150/210/270, all after their building finishes (105/165/225).
    """
    age = n - BOOK_ROUTE_STARTS[i]
    if age < 0:
        return None
    target, level = i % 3, (1 if i < 3 else 3)
    b = BUILDINGS[target]
    route = book_route(target)
    port_u, front_v = route[-1]
    shelf_z = b[4] * level / 5
    u, v = route_position(route, age / BOOK_TRAVEL_FRAMES)
    z, stage = 0.0, "conveyor"
    if age >= BOOK_TRAVEL_FRAMES:
        lift_age = age - BOOK_TRAVEL_FRAMES
        z = shelf_z * min(1.0, lift_age / BOOK_LIFT_FRAMES)
        stage = "lift"
        if lift_age >= BOOK_LIFT_FRAMES:
            dock_age = lift_age - BOOK_LIFT_FRAMES
            dock = min(1.0, dock_age / BOOK_DOCK_FRAMES)
            # The near face is v+d; keep the cuboid outside it, not inside a
            # solid wall. A short perpendicular slide seats it on the slot.
            v = front_v + (b[1] + b[3] + 0.025 - front_v) * dock
            stage = "docked" if dock >= 1.0 else "dock"
    w, d, h = BOOK_SIZE
    bounds = (u - w / 2, v, z, u + w / 2, v + d, z + h)
    return {"id": i, "target": target, "level": level, "stage": stage,
            "color": ACCENTS[target], "position": (u, v, z), "bounds": bounds}


def draw_belt(draw, pan):
    # belt as a thick neutral line following the iso grid path (not diagonal cuts)
    paths = [BELT_PATH] + [book_route(i) for i in range(3)]
    for points in paths:
        pts = [P(u, v, 0, pan) for (u, v) in points]
        draw.line(pts, fill=BELT_EDGE, width=8 * RASTER_SCALE)
        draw.line(pts, fill=BELT, width=6 * RASTER_SCALE)


def draw_book(draw, state, pan):
    x0, y0, z0, x1, y1, z1 = state["bounds"]
    col = state["color"]
    draw_box(draw, x0, y0, x1 - x0, y1 - y0, z1 - z0, pan,
             top=col, left=tuple(iround(c * 0.74) for c in col),
             right=tuple(iround(c * 0.52) for c in col), z0=z0)


def building_height(n, b):
    phase, frac = growth(n, b)
    if phase == 0:
        return None
    if phase == 1:
        return 10 + 20 * (1 - frac)
    if phase == 2:
        return b[4] * frac
    if phase == 3:
        return b[4] + 16 * (1 - frac) + 8
    return b[4] + 8


def projected_bounds(bounds, pan):
    x0, y0, z0, x1, y1, z1 = bounds
    points = [P(u, v, z, pan) for u in (x0, x1)
              for v in (y0, y1) for z in (z0, z1)]
    return (min(p[0] for p in points), min(p[1] for p in points),
            max(p[0] for p in points), max(p[1] for p in points))


def scene_objects(n, pan):
    objects = []
    for i, b in enumerate(BUILDINGS):
        h = building_height(n, b)
        if h is not None and h > 0:
            bounds = (b[0], b[1], 0, b[0] + b[2], b[1] + b[3], h)
            objects.append({"kind": "building", "id": i, "bounds": bounds})
    for i in range(6):
        state = book_state(n, i)
        if state:
            objects.append({"kind": "book", "id": i,
                            "bounds": state["bounds"], "state": state})
    for obj in objects:
        obj["projected_bounds"] = projected_bounds(obj["bounds"], pan)
    return objects


def ordered_scene(n, pan):
    """Bounded painter order for this nine-box scene, not a general 3D engine.

    View rays point toward increasing u, v and z. For disjoint boxes with
    overlapping projections, a separating coordinate plane supplies a safe
    back-before-front edge. Opposite separations imply no projected overlap;
    their bounding rectangles may still touch and need no edge. Cycles fail
    explicitly; the finite 300-state schedule is checked before delivery.
    """
    objects = scene_objects(n, pan)
    edges = [set() for _ in objects]
    incoming = [0] * len(objects)
    for i, a in enumerate(objects):
        for j in range(i + 1, len(objects)):
            b = objects[j]
            pa, pb = a["projected_bounds"], b["projected_bounds"]
            if pa[2] < pb[0] or pb[2] < pa[0] or pa[3] < pb[1] or pb[3] < pa[1]:
                continue
            aa, bb = a["bounds"], b["bounds"]
            a_behind = any(aa[k + 3] <= bb[k] for k in range(3))
            b_behind = any(bb[k + 3] <= aa[k] for k in range(3))
            if a_behind != b_behind:
                before, after = (i, j) if a_behind else (j, i)
                edges[before].add(after)
                incoming[after] += 1
    queue = [i for i, count in enumerate(incoming) if count == 0]
    result = []
    while queue:
        i = queue.pop(0)
        result.append(objects[i])
        for j in sorted(edges[i]):
            incoming[j] -= 1
            if incoming[j] == 0:
                queue.append(j)
    if len(result) != len(objects):
        raise ValueError("Occlusion cycle in bounded scene at frame %d" % n)
    return result


# ---- real CJK end copy on the same isometric ground plane -------------------
@lru_cache(maxsize=1)
def copy_mask():
    """Rasterize actual font outlines above final density; cache only the glyphs."""
    f = copy_font()
    left, top, right, bottom = f.getbbox(COPY_TEXT)
    mask = Image.new("L", (right - left, bottom - top), 0)
    ImageDraw.Draw(mask).text((-left, -top), COPY_TEXT, font=f, fill=255)
    return mask


def copy_ground_corners(pan):
    u, v = COPY_START
    return [project_native(x, y, 0, pan) for x, y in (
        (u, v), (u + COPY_U_SPAN, v),
        (u + COPY_U_SPAN, v + COPY_V_DEPTH), (u, v + COPY_V_DEPTH))]


def projected_copy_mask(n, pan):
    """Inverse affine map from native output pixels to the high-density glyphs."""
    source = copy_mask()
    reveal = min(1.0, max(0.0, (n - 240) / 30.0))
    if reveal < 1.0:
        source = source.copy()
        cutoff = int(source.width * reveal)
        ImageDraw.Draw(source).rectangle((cutoff, 0, source.width, source.height), fill=0)
    p0, p1, _, p3 = copy_ground_corners(pan)
    a, c = (p1[0] - p0[0]) / source.width, (p1[1] - p0[1]) / source.width
    b, d = (p3[0] - p0[0]) / source.height, (p3[1] - p0[1]) / source.height
    determinant = a * d - b * c
    inverse = (d / determinant, -b / determinant,
               (b * p0[1] - d * p0[0]) / determinant,
               -c / determinant, a / determinant,
               (c * p0[0] - a * p0[1]) / determinant)
    return source.transform((W, H), Image.Transform.AFFINE, inverse,
                            resample=Image.Resampling.BICUBIC, fillcolor=0)


def draw_copy(img, n, pan):
    """Real four-character text, revealed 240..270 on the fixed-angle ground."""
    if n < 240:
        return
    img.paste(INK, (0, 0), projected_copy_mask(n, pan))


def draw_header(draw, n):
    # small fixed HUD label (neutral ink) — pure function, no clock
    draw.text((28, 24), "MOTION-03  ISO 2.5D  /  LIBRARY SORT",
              font=HEADER_FONT, fill=INK)
    draw.text((28, H - 44), "frame %03d / 300   t = %.2fs" % (n, n / FPS),
              font=HEADER_FONT, fill=INK)


def render_frame(n, seed=SEED):
    """Native RGB frame. Seed is retained but UNUSED, as in the frozen source."""
    n = int(n)
    if not 0 <= n < FRAMES:
        raise ValueError("frame index must be in [0, 299]")
    copy_font()  # Fail at the first frame if the declared CJK dependency is absent.
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    pan = scene_pan(n)
    draw_ground(draw, pan)
    draw_belt(draw, pan)
    draw_copy(img, n, pan)  # Ground copy stays below all raised scene objects.
    # Building growth and book motion retain their own clocks. Draw order is
    # geometric, so a ground book cannot be pasted on top of a nearer roof.
    for obj in ordered_scene(n, pan):
        if obj["kind"] == "book":
            draw_book(draw, obj["state"], pan)
            continue
        b = BUILDINGS[obj["id"]]
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
    draw_header(draw, n)
    return img


def frame_path(n):
    return FRAME_DIR / ("f%04d.png" % n)


def sha_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_frame(n, img=None, out_dir=None, seed=SEED):
    target = Path(out_dir) if out_dir is not None else FRAME_DIR
    target.mkdir(parents=True, exist_ok=True)
    if img is None:
        img = render_frame(n, seed)
    output = target / ("f%04d.png" % n)
    img.save(output, format="PNG", compress_level=9, optimize=False)
    return sha_of(output)


def render_metadata(seed=SEED):
    return {
        "renderer": RENDERER_VERSION,
        "source_sha256": sha_of(__file__),
        "original_source_sha256": ORIGINAL_SOURCE_SHA256,
        "previous_native_source_sha256": PREVIOUS_NATIVE_SOURCE_SHA256,
        "logical_resolution": [LOGICAL_W, LOGICAL_H],
        "resolution": [W, H], "fps": FPS, "frames": FRAMES,
        "spatial_generation": "continuous isometric geometry rasterized directly to native canvas",
        "layout_change": {"scene_y_offset_logical": SCENE_Y_OFFSET,
                          "building_growth_schedule_changed": False,
                          "camera_schedule_changed": True,
                          "translation_schedule_changed": False,
                          "uniform_zoom": {"start_frame": 240, "end_frame": 285,
                                           "start_scale": 1.0, "end_scale": 0.94,
                                           "interpolation": "continuous smoothstep before native coordinate rounding"},
                          "reason": "Keep final building and diagonal end-copy inside the frame above bottom HUD"},
        "bounded_scene_repair": {
            "side_faces": "v=max near-left and u=max near-right, closed roof slab",
            "occlusion": "separating-plane painter order for at most 3 buildings and 6 books",
            "conveyor_schedule_changed_from_frozen_original": True,
            "conveyor_schedule_changed_from_previous_native_source": False,
            "delivery_launch_frames": list(BOOK_ROUTE_STARTS),
            "delivery_duration_frames": BOOK_TRAVEL_FRAMES + BOOK_LIFT_FRAMES + BOOK_DOCK_FRAMES,
            "target_by_book": [i % 3 for i in range(6)],
            "levels_by_book": [1, 1, 1, 3, 3, 3],
            "terminal_delivery_frame": 270,
            "seed_behavior_changed": False,
            "end_copy": "Real CJK font outlines projected onto the isometric ground plane",
            "camera": "Original pan plus uniform 6% terminal pull-back; angle fixed, HUD untransformed"
        },
        "seed": seed, "seed_affects_pixels": False,
        "seed_note": "Original renderer did not use seed; no new seed behavior is fabricated.",
        "pillow_version": PILLOW_VERSION,
        "header_font": "Pillow bundled default FreeType font, rendered at 20 native px",
        "cjk_font": font_evidence(),
        "copy_projection": {"source_mask_size": list(copy_mask().size),
                            "logical_ground_start": list(COPY_START),
                            "logical_u_span": COPY_U_SPAN, "logical_v_depth": COPY_V_DEPTH,
                            "reveal_frames": [240, 270],
                            "sampling": "high-density font mask -> inverse affine -> native output"},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("keys", "all", "full", "batch"))
    parser.add_argument("indices", nargs="?", help="comma-separated frame indices for batch")
    parser.add_argument("--outdir", type=Path, default=HERE)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    if args.mode == "batch" and not args.indices:
        parser.error("batch requires comma-separated frame indices")
    indices = ([int(t) for t in args.indices.split(",")] if args.mode == "batch"
               else [n for n, _ in KEYFRAMES] if args.mode == "keys"
               else list(range(FRAMES)))
    if any(not 0 <= n < FRAMES for n in indices):
        parser.error("frame indices must be in [0, 299]")
    directory = args.outdir / ("stills" if args.mode == "keys" else "frames")
    hashes = {"%04d" % n: save_frame(n, out_dir=directory, seed=args.seed) for n in indices}
    report = render_metadata(args.seed)
    report.update({"mode": args.mode, "rendered_frames": len(indices), "hashes": hashes})
    args.outdir.mkdir(parents=True, exist_ok=True)
    (args.outdir / "render_manifest.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"mode": args.mode, "resolution": [W, H], "hashes": hashes,
                      "seed_affects_pixels": False, "ok": True}))


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
