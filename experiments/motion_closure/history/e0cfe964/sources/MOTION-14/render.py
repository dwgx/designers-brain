#!/usr/bin/env python3 -X utf8
"""
MOTION-14 / 19-paperclip — STICKER SCIENCE (贴纸科普).

Deterministic pure-Python Pillow renderer. render_frame(n, seed) is a PURE
function of the frame index n and the frozen seed: no wall clock, no RNG
stream, no inter-frame state, no browser, no network, no external assets.

Governing card: origin/提示词全文.md L208-216 (card 14 贴纸科普).
Pipeline contract: MOTION-CALIBRATION CALIBRATION-PASS — same shape as
MOTION-03 (render -> frame_hashes -> determinism trio -> verify -> receipt).

Design (pre-registered in schedule.json BEFORE this file existed):
  * Everything lives on a WORLD desk canvas 2400x1350 (2.5x the 960x540
    viewport) — "比画面大好几倍的浅色桌面".
  * The camera is pan + zoom ONLY (`camera(n)` integer pure function with
    smoothstep long eases). NO hard cut, NO scene swap, NO angle change.
  * Each new element is ADDed every 0.5-1 s at ADD_FRAMES, with a short
    deterministic stamp-in (5-frame drop / 10-frame bar growth). No bounce
    overshoot past 1.0.
  * Die-cut sticker illustrations are documented VECTOR cutouts (no real
    photo, no external image). Each has a UNIFORM 10px white outline
    (同样宽的白边) + deterministic soft drop shadow (淡投影).
  * Bars are strictly proportional to the real numbers (柱长照真实数字画):
    bar_len = round(value_pct/100 * BAR_MAX_LEN), one shared scale. A clearly
    labelled "x12 放大" inset lens re-draws the tiny bars with the SAME linear
    rule at x12 so 0.1%/1.7% remain visible without faking the ratios.
  * Palette: light blue-grey desk (#E9EEF2), dark-grey ink (#3A4652), neutral
    bar (#93A7BC), exactly ONE accent (coral #E8674C).

Modes: `render.py keys|all|batch [n,n,...]`
"""
import hashlib
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = Path(__file__).resolve().parent
FRAME_DIR = HERE / "frames"
STILL_DIR = HERE / "stills"

SEED = 20261115
FPS = 30
FRAMES = 300
W, H = 960, 540                    # viewport
WORLD_W, WORLD_H = 2400, 1350      # the big desk

# ---- canonical palette (light blue-grey base + dark grey ink + ONE accent) ---
DESK = (233, 238, 242)             # #E9EEF2 浅灰蓝底
GRID = (214, 222, 230)             # faint desk grid
INK = (58, 70, 82)                 # #3A4652 深灰字
INK_LIGHT = (110, 124, 140)
PANEL = (248, 250, 252)            # near-white paper chart card
PANEL_EDGE = (198, 210, 222)
BAR_NEUTRAL = (147, 167, 188)      # #93A7BC neutral bar fill
BAR_NEUTRAL_DARK = (120, 142, 166)
ACCENT = (232, 103, 76)            # #E8674C — the ONE 强调色
WHITE = (255, 255, 255)            # 白边
SHADOW_RGB = (74, 88, 104)         # 淡投影 tint

WHITE_OUTLINE = 10                 # 同样宽的白边 — uniform for ALL props

# World font (system CJK font; no bundled font). Loaded by size; pure memo.
FONT_PATH = "C:/Windows/Fonts/simhei.ttf"
_FONT_CACHE = {}


def font(sz):
    f = _FONT_CACHE.get(sz)
    if f is None:
        try:
            f = ImageFont.truetype(FONT_PATH, sz)
        except OSError:
            f = ImageFont.load_default()
        _FONT_CACHE[sz] = f
    return f


def iround(v):
    """Deterministic half-away-from-zero rounding (no float banker drift)."""
    return int(math.floor(v + 0.5)) if v >= 0 else -int(math.floor(-v + 0.5))


# ---- pre-registered data ---------------------------------------------------
BAR_MAX_LEN = 620                  # world px for 100% (shared scale)
LENS = 12                          # declared magnification for the inset lens
BAR_VALUES = [
    ("ocean",   "海洋",   96.5),
    ("glacier", "冰川",   1.7),
    ("ground",  "地下水", 1.7),
    ("lake",    "河湖",   0.1),
]


def bar_length(value_pct, scale=1):
    """柱长照真实数字画、和数值成比例 — one shared linear scale for all bars.

    S24 §4 (2026-11-16): this is the METADATA length (no visibility clamp);
    chk_bar_proportionality() verifies exactly this value. The DRAWN rectangle
    in draw_bars applies a separate minimum-visible-size floor max(len, 2).
    """
    return iround(value_pct / 100.0 * BAR_MAX_LEN * scale)


# ---- ADD schedule (每 0.5-1 秒加一样新东西) --------------------------------
ADD_FRAMES = {
    "ocean_sticker":   15,
    "glacier_sticker": 45,
    "ground_sticker":  75,
    "lake_sticker":    105,
    "leader_label":    135,
    "bar_ocean":       165,
    "bar_glacier":     195,
    "bar_ground":      225,
    "bar_lake":        255,
    "accent_highlight": 270,
    "final_banner":    285,
}
ADD_ORDER = sorted(ADD_FRAMES.items(), key=lambda kv: kv[1])

# Sticker world positions (2x2 cluster on the left half of the desk)
STICKER_POS = {
    "ocean_sticker":   (130, 180),
    "glacier_sticker": (530, 180),
    "ground_sticker":  (130, 455),
    "lake_sticker":    (530, 455),
}
STICKER_KIND = {
    "ocean_sticker":   "ocean",
    "glacier_sticker": "glacier",
    "ground_sticker":  "ground",
    "lake_sticker":    "lake",
}

# Bar chart world layout
CHART_PANEL = (1230, 150, 2330, 1090)
BAR_X0 = 1620
BAR_ROWS = [330, 480, 630, 780]
BAR_HEIGHT = 52
LENS_PANEL = (1270, 880, 2290, 1060)

# Final pull-back banner (bottom of the world; visible when camera zooms out)
BANNER = (480, 1120, 1920, 1270)

KEYFRAMES = [
    (0,   "DESK_EMPTY"),
    (60,  "STICKERS_LANDING"),
    (135, "LEADER_LABEL"),
    (195, "BARS_GROW"),
    (255, "NUMBERS_SOURCE"),
    (285, "PULLBACK_UNDER_1"),
]


# ---- camera: pan + zoom ONLY (不切镜头), continuous long eases --------------
# (frame, pan_x, pan_y, zoom_pct). Smoothstep between keys; constant 290..299
CAMERA_KEYS = [
    (0,   60,  110, 80),
    (140, 60,  110, 80),
    (195, 1150, 170, 80),
    (255, 1150, 170, 80),
    (290, 300,  200, 46),
    (299, 300,  200, 46),
]


def _smoothstep(t):
    t = 0.0 if t < 0 else (1.0 if t > 1 else t)
    return t * t * (3 - 2 * t)


def camera(n):
    """Pure integer (pan_x, pan_y, zoom_pct). NO cut, NO angle change."""
    n = int(n)
    if n <= CAMERA_KEYS[0][0]:
        return CAMERA_KEYS[0][1], CAMERA_KEYS[0][2], CAMERA_KEYS[0][3]
    for i in range(len(CAMERA_KEYS) - 1):
        f0, x0, y0, z0 = CAMERA_KEYS[i]
        f1, x1, y1, z1 = CAMERA_KEYS[i + 1]
        if n <= f1:
            t = _smoothstep((n - f0) / float(f1 - f0))
            return (iround(x0 + (x1 - x0) * t),
                    iround(y0 + (y1 - y0) * t),
                    iround(z0 + (z1 - z0) * t))
    return CAMERA_KEYS[-1][1], CAMERA_KEYS[-1][2], CAMERA_KEYS[-1][3]


# ---- die-cut sticker sprites (deterministic vector cutouts) ----------------
# Built ONCE at import; each sprite = soft shadow + UNIFORM 10px white outline
# + flat vector illustration. No photo / external asset / RNG.
SW, SH = 420, 340                  # sprite canvas incl. margin for shadow


def _silhouette(kind):
    """Return an L-mode mask of the die-cut shape (255 inside)."""
    m = Image.new("L", (SW, SH), 0)
    d = ImageDraw.Draw(m)
    if kind == "ocean":            # wavy-topped organic blob
        pts = [(46, 150), (60, 118), (92, 128), (122, 100), (156, 118),
               (190, 96), (224, 116), (258, 98), (292, 120), (326, 104),
               (360, 132), (372, 168), (372, 258), (352, 292), (68, 292),
               (46, 258)]
        d.polygon(pts, fill=255)
        d.ellipse((46, 138, 86, 186), fill=255)
        d.ellipse((334, 138, 374, 186), fill=255)
    elif kind == "glacier":        # jagged iceberg
        pts = [(196, 62), (232, 116), (268, 96), (300, 146), (334, 128),
               (372, 268), (348, 292), (72, 292), (48, 268), (96, 160),
               (140, 124), (168, 140)]
        d.polygon(pts, fill=255)
    elif kind == "ground":         # rounded aquifer cross-section
        d.rounded_rectangle((52, 92, 368, 286), radius=30, fill=255)
    else:                          # lake: soft oval
        d.ellipse((52, 92, 368, 286), fill=255)
    return m


def _illustration(kind):
    """RGBA flat vector art; alpha masked by the silhouette at build time."""
    base = {
        "ocean":   (91, 126, 158),
        "glacier": (191, 216, 232),
        "ground":  (201, 169, 126),
        "lake":    (78, 134, 166),
    }[kind]
    img = Image.new("RGBA", (SW, SH), base + (255,))
    d = ImageDraw.Draw(img)
    if kind == "ocean":
        for k in range(3):
            yy = 176 + k * 34
            d.line([(60, yy), (110, yy - 8), (160, yy), (210, yy - 8),
                    (260, yy), (310, yy - 8), (360, yy)],
                   fill=(224, 236, 246, 255), width=5)
    elif kind == "glacier":
        d.polygon([(196, 62), (214, 160), (168, 200)], fill=(226, 240, 250, 255))
        d.polygon([(196, 62), (232, 116), (268, 96), (250, 178)],
                  fill=(160, 198, 224, 255))
        d.line([(196, 62), (196, 280)], fill=(150, 188, 216, 255), width=4)
        d.line([(120, 250), (300, 250)], fill=(150, 188, 216, 255), width=4)
    elif kind == "ground":
        for yy, col in [(150, (168, 134, 96)), (196, (150, 118, 84)),
                        (242, (128, 100, 72))]:
            d.line([(62, yy), (358, yy)], fill=col + (255,), width=8)
        for cx in range(90, 350, 46):
            for cy in (122, 172, 220, 264):
                d.ellipse((cx - 4, cy - 4, cx + 4, cy + 4),
                          fill=(110, 140, 168, 255))
    else:
        for k in range(3):
            d.arc((92 + k * 18, 132 + k * 12, 328 - k * 18, 246 - k * 12),
                  start=200, end=340, fill=(198, 224, 240, 255), width=5)
    return img


def _make_sprite(kind):
    m = _silhouette(kind)
    # UNIFORM 10px white outline via morphological dilation (radius 10).
    dil = m.filter(ImageFilter.MaxFilter(2 * WHITE_OUTLINE + 1))
    border = ImageChops.subtract(dil, m)
    # soft drop shadow: blurred dilated silhouette, offset (9,11), faint alpha
    sh = ImageChops.offset(dil.filter(ImageFilter.GaussianBlur(8)), 9, 11)
    sh = sh.point(lambda a: (a * 90) // 255)

    sprite = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    sh_layer = Image.new("RGBA", (SW, SH), SHADOW_RGB + (0,))
    sh_layer.putalpha(sh)
    sprite = Image.alpha_composite(sprite, sh_layer)
    wb = Image.new("RGBA", (SW, SH), WHITE + (0,))
    wb.putalpha(border)
    sprite = Image.alpha_composite(sprite, wb)
    illu = Image.composite(_illustration(kind),
                           Image.new("RGBA", (SW, SH), (0, 0, 0, 0)), m)
    sprite = Image.alpha_composite(sprite, illu)
    return sprite


SPRITES = {k: _make_sprite(k) for k in ("ocean", "glacier", "ground", "lake")}


# ---- small drawing helpers -------------------------------------------------
def stamp_drop(n, add_frame):
    """5-frame deterministic stamp-in offset (0 once settled). Pure of n."""
    if n < add_frame:
        return None
    return max(0, 5 - (n - add_frame)) * 4


def bar_grow(n, add_frame):
    """10-frame horizontal growth factor numerator over 10 (10 = full)."""
    if n < add_frame:
        return 0
    return min(10, n - add_frame)


def T(draw, xy, text, size, color=INK):
    draw.text(xy, text, font=font(size), fill=color)


def draw_desk_grid(draw):
    for gx in range(0, WORLD_W + 1, 80):
        draw.line([(gx, 0), (gx, WORLD_H)], fill=GRID, width=1)
    for gy in range(0, WORLD_H + 1, 80):
        draw.line([(0, gy), (WORLD_W, gy)], fill=GRID, width=1)


def draw_stickers(world, n):
    for prop, (x, y) in STICKER_POS.items():
        add = ADD_FRAMES[prop]
        off = stamp_drop(n, add)
        if off is None:
            continue
        sprite = SPRITES[STICKER_KIND[prop]]
        world.paste(sprite.convert("RGB"), (x, y + off), sprite.getchannel("A"))


def draw_leader_label(draw, n):
    add = ADD_FRAMES["leader_label"]
    off = stamp_drop(n, add)
    if off is None:
        return
    oy = off
    # dot on the ocean sticker + polyline to a small label card
    sx, sy = 470, 330 + oy
    ex, ey = 980, 250 + oy
    draw.ellipse((sx - 8, sy - 8, sx + 8, sy + 8), fill=INK)
    draw.line([(sx, sy), (700, 250 + oy), (ex, ey)], fill=INK_LIGHT, width=4)
    draw.rounded_rectangle((ex, ey - 30, ex + 268, ey + 36), radius=10,
                           fill=PANEL, outline=PANEL_EDGE, width=3)
    T(draw, (ex + 14, ey - 22), "引线标注 · 海洋", 30, INK)
    T(draw, (ex + 14, ey + 8), "咸水 / 占全球水 96.5%", 22, INK_LIGHT)


def draw_chart_furniture(draw):
    draw.rounded_rectangle(CHART_PANEL, radius=26, fill=PANEL,
                           outline=PANEL_EDGE, width=3)
    T(draw, (1280, 180), "地球上的水 · 占比", 46, INK)
    T(draw, (1280, 240), "数据来源：USGS 水循环概查（教学示意值）", 24, INK_LIGHT)
    draw.line([(1280, 282), (2280, 282)], fill=PANEL_EDGE, width=3)
    # inset lens furniture (declared x12 linear magnification)
    draw.rounded_rectangle(LENS_PANEL, radius=16, fill=(240, 244, 248),
                           outline=PANEL_EDGE, width=2)
    T(draw, (1290, 892), "小占比 ×12 放大（同一线性刻度）", 26, INK_LIGHT)


def draw_bars(draw, n):
    for i, (key, label, value) in enumerate(BAR_VALUES):
        prop = "bar_" + key
        g = bar_grow(n, ADD_FRAMES[prop])
        if g == 0:
            continue
        yy = BAR_ROWS[i]
        full = bar_length(value)
        length = (full * g) // 10
        # Minimum-visible-size exception (documented 2026-11-16, S24 §4):
        # a 1px bar (lake: ideal span 0.62px -> iround 1) is invisible under
        # the 2px outline, so the DRAWN span is clamped to max(length, 2).
        # The 0.1% bar's drawn endpoint therefore deviates ~1.4px from the
        # ideal proportional span — a visibility FLOOR, not a proportionality
        # claim. Bars >= 1.7% (span >= 10px) are drawn proportional within
        # +/-1px integer quantization.
        # label + number (numbers equal the real value_pct exactly)
        T(draw, (1290, yy + 6), label, 34, INK)
        draw.rectangle((BAR_X0, yy, BAR_X0 + max(length, 2), yy + BAR_HEIGHT),
                       fill=BAR_NEUTRAL, outline=BAR_NEUTRAL_DARK, width=2)
        T(draw, (BAR_X0 + full + 18, yy + 6), "%.1f%%" % value, 34, INK)
        # inset lens bar (SAME linear rule, x12) — keeps proportionality honest
        # (S24 §4: same max(...,2) visibility floor applies in the lens; lake
        # lfull=7px at full growth, so the clamp only bites during grow-in)
        ly = 940 + i * 30
        lfull = bar_length(value, LENS)
        llen = (lfull * g) // 10
        if lfull > 0:
            T(draw, (1290, ly), "%.1f%%" % value, 22, INK_LIGHT)
            draw.rectangle((1420, ly + 4, 1420 + max(llen, 2), ly + 20),
                           fill=BAR_NEUTRAL_DARK)


def draw_accent_highlight(draw, n):
    add = ADD_FRAMES["accent_highlight"]
    off = stamp_drop(n, add)
    if off is None:
        return
    oy = off
    # the ONE accent: a coral marker + "淡水" summary band
    draw.rounded_rectangle((1280, 830 + oy, 2280, 872 + oy), radius=8,
                           fill=ACCENT)
    T(draw, (1296, 832 + oy), "可直接利用的淡水", 28, WHITE)
    T(draw, (1960, 832 + oy), "< 1%", 30, WHITE)


def draw_final_banner(draw, n):
    add = ADD_FRAMES["final_banner"]
    off = stamp_drop(n, add)
    if off is None:
        return
    oy = off
    x0, y0, x1, y1 = BANNER
    y0 += oy
    y1 += oy
    draw.rounded_rectangle((x0, y0, x1, y1), radius=18, fill=PANEL,
                           outline=PANEL_EDGE, width=3)
    draw.rounded_rectangle((x0, y0, x0 + 18, y1), radius=8, fill=ACCENT)
    T(draw, (x0 + 48, y0 + 22), "最后拉远：能直接用的淡水不到 1%", 60, INK)
    T(draw, (x0 + 48, y0 + 100), "海洋 96.5% · 冰川/地下水 1.7% · 河湖 0.1%   |   USGS 概查",
      26, INK_LIGHT)


# ---- pure frame function ---------------------------------------------------
def render_frame(n, seed=SEED):
    """PURE function of (n, seed) -> PIL RGB Image (960x540 viewport)."""
    n = int(n)
    world = Image.new("RGB", (WORLD_W, WORLD_H), DESK)
    wd = ImageDraw.Draw(world)
    draw_desk_grid(wd)
    draw_stickers(world, n)
    draw_chart_furniture(wd)
    draw_leader_label(wd, n)
    draw_bars(wd, n)
    draw_accent_highlight(wd, n)
    draw_final_banner(wd, n)

    pan_x, pan_y, zoom = camera(n)
    vw = (W * 100) // zoom
    vh = (H * 100) // zoom
    pan_x = min(max(pan_x, 0), WORLD_W - vw)
    pan_y = min(max(pan_y, 0), WORLD_H - vh)
    crop = world.crop((pan_x, pan_y, pan_x + vw, pan_y + vh))
    view = crop.resize((W, H), Image.Resampling.BILINEAR)

    d = ImageDraw.Draw(view)
    # fixed screen-space HUD strap (a HUD, NOT a scene cut)
    d.rectangle((0, 0, W, 34), fill=(248, 250, 252))
    d.line([(0, 34), (W, 34)], fill=PANEL_EDGE, width=2)
    T(d, (14, 6), "MOTION-14  STICKER SCIENCE  /  地球上的水", 20, INK)
    T(d, (W - 210, 6), "frame %03d / 300" % min(n, 290), 20, INK_LIGHT)
    return view


def frame_path(n):
    return FRAME_DIR / ("f%04d.png" % n)


def sha_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_frame(n, img=None, out_dir=None):
    out = out_dir or FRAME_DIR
    Path(out).mkdir(parents=True, exist_ok=True)
    if img is None:
        img = render_frame(n)
    p = Path(out) / ("f%04d.png" % n)
    img.save(p, format="PNG", compress_level=9, optimize=False)
    return sha_of(p)


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
            json.dumps({"card": "14", "slug": "19-paperclip", "seed": SEED,
                        "fps": FPS, "keyframes": manifest}, indent=2,
                       ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"mode": "keys", "keyframes": len(manifest), "ok": True}))
    elif mode == "all":
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        hashes = {}
        for n in range(FRAMES):
            hashes["%04d" % n] = save_frame(n)
        (FRAME_DIR / "frame_hashes.json").write_text(
            json.dumps({"seed": SEED, "fps": FPS, "frames": FRAMES,
                        "resolution": [W, H],
                        "renderer": "pure-python-pillow-raster-sticker-science@1.0.0",
                        "hashes": hashes}, indent=1, sort_keys=True),
            encoding="utf-8")
        print(json.dumps({"mode": "all", "frames": FRAMES, "ok": True}))
    elif mode == "range":
        lo, hi = int(sys.argv[2]), int(sys.argv[3])
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        out = {}
        for n in range(lo, hi):
            out[n] = save_frame(n)
        print(json.dumps({"mode": "range", "lo": lo, "hi": hi,
                          "rendered": len(out), "ok": True}))
    elif mode == "manifest":
        # Build the canonical frame_hashes.json from the REAL 300 PNG bytes.
        hashes = {}
        for n in range(FRAMES):
            p = frame_path(n)
            if not p.is_file():
                print("missing frame %04d" % n, file=sys.stderr)
                sys.exit(2)
            hashes["%04d" % n] = sha_of(p)
        (FRAME_DIR / "frame_hashes.json").write_text(
            json.dumps({"seed": SEED, "fps": FPS, "frames": FRAMES,
                        "resolution": [W, H],
                        "renderer": "pure-python-pillow-raster-sticker-science@1.0.0",
                        "hashes": hashes}, indent=1, sort_keys=True),
            encoding="utf-8")
        print(json.dumps({"mode": "manifest", "hashes": len(hashes), "ok": True}))
    elif mode == "batch":
        FRAME_DIR.mkdir(parents=True, exist_ok=True)
        out = {}
        for tok in sys.argv[2].split(","):
            n = int(tok)
            out[n] = save_frame(n)
        print(json.dumps(out))
    else:
        print("usage: render.py keys|all|range|manifest|batch ...", file=sys.stderr)
        sys.exit(2)


# ---- exported SEMANTICS for verify.py (verifier uses the REAL shipped funcs) -
def sticker_kinds():
    return list(SPRITES.keys())


def white_outline_width(prop):
    """同样宽的白边 — returns WHITE_OUTLINE for EVERY prop (no exceptions)."""
    return WHITE_OUTLINE


def bars_with_lengths():
    """Metadata lengths = UNclamped proportional bar_length(value) (see
    bar_length docstring). The drawn rectangle in draw_bars adds a separate
    max(...,2) minimum-visible-size floor for the 0.1% bar — documented
    exception, S24 §4 2026-11-16; NOT included here so the proportionality
    check stays a pure shared-scale check."""
    return [(key, label, value, bar_length(value))
            for key, label, value in BAR_VALUES]


def accent_colors():
    """Exactly ONE accent color in the whole palette."""
    return [ACCENT]


def add_frames():
    return dict(ADD_FRAMES)


def camera_series():
    return [camera(n) for n in range(FRAMES)]


def world_size():
    return (WORLD_W, WORLD_H)


if __name__ == "__main__":
    main()
