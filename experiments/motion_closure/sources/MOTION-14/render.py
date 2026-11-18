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
  * The original logical content is 2400x1350; the review candidate adds page
    margins on a 2800x1600 logical desk, rasterized directly at 5600x3200.
    A separate 72-pixel HUD leaves a native 1920x1008 camera scene below it.
  * The camera is pan + zoom ONLY (`camera(n)` continuous pure function with
    smoothstep long eases). NO hard cut, NO scene swap, NO angle change.
  * Each new element is ADDed every 0.5-1 s at ADD_FRAMES, with a short
    deterministic stamp-in (5-frame drop / 10-frame bar growth). No bounce
    overshoot past 1.0.
  * Die-cut sticker illustrations are documented VECTOR cutouts (no real
    photo, no external image). Each has a UNIFORM 10px white outline
    (同样宽的白边) + deterministic soft drop shadow (淡投影).
  * Bars use the USGS table's rounded percentages of TOTAL water. Only four
    selected groups are shown; freshwater lakes + rivers is the approximate
    sum 0.007% + 0.0002% = 0.0072%. Stored water is not usable supply.
    bar_len = round(value_pct/100 * BAR_MAX_LEN), one shared scale. A clearly
    labelled "x12 放大" inset lens re-draws the tiny bars with the SAME linear
    rule at x12. The inherited two-logical-unit visibility floor remains;
    lens bars are clipped to the inset with a visible // truncation mark.
    Neither that floor nor a clipped bar is an exact-proportion claim.
  * Palette: light blue-grey desk (#E9EEF2), dark-grey ink (#3A4652), neutral
    bar (#93A7BC), exactly ONE accent (coral #E8674C).

Modes: `render.py keys|all|batch [n,n,...]`
"""
import argparse
import hashlib
import json
import math
import os
import sys
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, __version__ as PILLOW_VERSION

HERE = Path(__file__).resolve().parent
FRAME_DIR = HERE / "frames"
STILL_DIR = HERE / "stills"

SEED = 20261115
FPS = 30
FRAMES = 300
LOGICAL_W, LOGICAL_H = 960, 540
RASTER_SCALE = 2
W, H = 1920, 1080                 # actual native viewport
WORLD_W, WORLD_H = 2400, 1350      # unchanged logical world / camera space
PAGE_W, PAGE_H = 2800, 1600        # breathing room around the unchanged content
PAGE_OFFSET = (200, 120)
HUD_H = 72                       # actual screen space; never overlays scene pixels
CONTENT_H = H - HUD_H
LOGICAL_CONTENT_H = CONTENT_H // RASTER_SCALE
WORLD_PIXEL_W, WORLD_PIXEL_H = PAGE_W * RASTER_SCALE, PAGE_H * RASTER_SCALE
ORIGINAL_SOURCE_SHA256 = "88a26cf3a72ab47359ee22b1c06596dfbec0ec197a1630a8165959dbacf58d27"
CAMERA_BASE_SOURCE_SHA256 = "01bbd90590d5eca05e688eeb5648985cf3dca45fb5f9992d5e85c1bfe560429c"
RENDERER_VERSION = "sticker-science-native-pillow@2.3.0-usgs-data-correction"

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

# Font bytes are an explicit render dependency. No bitmap/default-font fallback.
# On another host set MOTION14_FONT and, for a collection, MOTION14_FONT_INDEX.
FONT_PATH = os.environ.get("MOTION14_FONT")
if FONT_PATH is None:
    FONT_PATH = next((str(p) for p in (
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    ) if p.is_file()), None)
FONT_INDEX = int(os.environ.get("MOTION14_FONT_INDEX", "0"))
_FONT_CACHE = {}


def font(sz):
    if not FONT_PATH or not Path(FONT_PATH).is_file():
        raise RuntimeError("A CJK font is required; set MOTION14_FONT. No fallback is permitted.")
    sz = int(sz)
    f = _FONT_CACHE.get(sz)
    if f is None:
        f = ImageFont.truetype(FONT_PATH, sz, index=FONT_INDEX)
        _FONT_CACHE[sz] = f
    return f


@lru_cache(maxsize=1)
def font_evidence():
    """Bind the actual font and reject missing glyphs used by this card."""
    f = font(40)
    missing_mask = f.getmask("\U0010ffff")
    missing_fingerprint = (missing_mask.size, bytes(missing_mask))
    required_text = "".join(TEXT.values()) + "".join(label for _, label, _ in BAR_VALUES)
    required_text += "".join(format_percent(value, key == "lake") for key, _, value in BAR_VALUES)
    required = set(char for char in required_text if ord(char) > 127)
    missing = []
    for char in sorted(required):
        mask = f.getmask(char)
        if (mask.size, bytes(mask)) == missing_fingerprint:
            missing.append(char)
    if missing:
        raise RuntimeError("Selected font lacks required CJK glyphs: " + "".join(missing))
    return {"path": str(Path(FONT_PATH).resolve()), "face_index": FONT_INDEX,
            "name": list(f.getname()), "sha256": hashlib.sha256(Path(FONT_PATH).read_bytes()).hexdigest(),
            "required_glyph_count": len(required), "missing_required_glyphs": missing,
            "fallback_used": False}


def iround(v):
    """Deterministic half-away-from-zero rounding (no float banker drift)."""
    return int(math.floor(v + 0.5)) if v >= 0 else -int(math.floor(-v + 0.5))


class GeometryDraw:
    """Transform vector coordinates BEFORE Pillow rasterizes at native density.

    This adapter receives no image pixels and has no resize/blit operation.
    All authored coordinates are logical world units; font sizes are supplied
    already at physical density by T(). The same adapter draws screen-space HUD.
    """
    def __init__(self, image, scale=RASTER_SCALE, offset=(0, 0)):
        self.draw = ImageDraw.Draw(image)
        self.scale = scale
        self.offset = offset

    def coordinates(self, xy):
        if isinstance(xy[0], (int, float)):
            return tuple((v + self.offset[i % 2]) * self.scale for i, v in enumerate(xy))
        return [((x + self.offset[0]) * self.scale,
                 (y + self.offset[1]) * self.scale) for x, y in xy]

    def width(self, value):
        return max(1, iround(value * self.scale))

    def line(self, xy, fill=None, width=1, **kwargs):
        self.draw.line(self.coordinates(xy), fill=fill, width=self.width(width), **kwargs)

    def polygon(self, xy, fill=None, outline=None, **kwargs):
        self.draw.polygon(self.coordinates(xy), fill=fill, outline=outline, **kwargs)

    def ellipse(self, xy, fill=None, outline=None, width=1, **kwargs):
        self.draw.ellipse(self.coordinates(xy), fill=fill, outline=outline,
                          width=self.width(width), **kwargs)

    def rectangle(self, xy, fill=None, outline=None, width=1, **kwargs):
        self.draw.rectangle(self.coordinates(xy), fill=fill, outline=outline,
                            width=self.width(width), **kwargs)

    def rounded_rectangle(self, xy, radius=0, fill=None, outline=None, width=1, **kwargs):
        self.draw.rounded_rectangle(self.coordinates(xy), radius=radius * self.scale,
                                    fill=fill, outline=outline, width=self.width(width), **kwargs)

    def arc(self, xy, start, end, fill=None, width=1):
        self.draw.arc(self.coordinates(xy), start=start, end=end, fill=fill, width=self.width(width))

    def text(self, xy, text, font=None, fill=None, **kwargs):
        self.draw.text(self.coordinates(xy), text, font=font, fill=fill, **kwargs)


# ---- sourced data (values corrected; schedule and geometry preserved) ------
BAR_MAX_LEN = 620                  # world px for 100% (shared scale)
LENS = 12                          # declared magnification for the inset lens
BAR_VALUES = [
    ("ocean",   "海洋",                 96.54),
    ("glacier", "冰盖/冰川/永久积雪",     1.74),
    ("ground",  "地下水(淡+盐)",          1.69),
    ("lake",    "淡水湖+河流",            0.0072),
]
DATA_SOURCE = {
    "publisher": "U.S. Geological Survey, Water Science School",
    "url": "https://www.usgs.gov/water-science-school/science/how-much-water-there-earth",
    "page_title": "How Much Water is There on Earth?",
    "page_date": "2019-11-13",
    "accessed_date_utc": "2026-11-17",
    "basis": "Percent of total water column; rounded estimates of water stored, not freshwater-only percentages or usable supply.",
    "underlying_table_reference": "Igor Shiklomanov, World fresh water resources, in Peter H. Gleick (ed.), Water in Crisis, 1993, Oxford University Press.",
    "selected_groups": {
        "ocean": {"category": "Oceans, seas and bays", "percent_total": "96.54"},
        "glacier": {"category": "Ice caps, glaciers and permanent snow", "percent_total": "1.74"},
        "ground": {"category": "Groundwater, fresh plus saline", "percent_total": "1.69"},
        "lake": {"category": "Freshwater lakes plus rivers", "percent_total_approximate": "0.0072",
                 "derived_from_rounded_percentages": ["0.007", "0.0002"],
                 "derivation": "0.007% + 0.0002% = approximately 0.0072%; sum of already-rounded table percentages, not recalculated from volumes."},
    },
    "coverage": "Four selected groups, not the whole distribution. Saline lakes and other table categories are omitted; values are not normalized to 100%.",
    "rounding": "All source percentages are rounded estimates. Retain two displayed decimals for the first three groups and four for the combined small group, marked approximate.",
    "interpretation_limit": "Stored water quantity does not measure usable water, accessibility, drinking-water safety or sustainable extraction.",
}
TEXT = {
    "leader_title": "引线标注 · 海洋",
    "leader_value": "占全球水量 96.54%",
    "chart_title": "全球水储量 · 四类选摘",
    "chart_subtitle": "占全球总水量 | USGS 约数（非全集）",
    "lens_caption": "小占比 ×12 放大（// 表示截断）",
    "accent_label": "淡水湖+河流占总量",
    "accent_value": "约0.0072%",
    "banner_title": "水的库存，不等于可利用量",
    "banner_subtitle": "仅展示四类；分母为全球总水量 | USGS 四舍五入估计",
    "hud_title": "MOTION-14  STICKER SCIENCE  /  地球上的水",
}


def format_percent(value, approximate=False):
    """Preserve the tiny combined value; one-decimal formatting would hide it."""
    digits = 4 if value < 0.01 else 2
    return ("约" if approximate else "") + f"{value:.{digits}f}%"


def bar_value_label_x(value, approximate=False, scale=RASTER_SCALE):
    """Keep a precise value inside the paper; move only overflowing text."""
    full = bar_length(value)
    external_x = BAR_X0 + full + 18
    label_width = font(34 * scale).getlength(format_percent(value, approximate)) / scale
    if external_x + label_width > CHART_PANEL[2] - 24:
        return BAR_X0 + full - 18 - label_width  # inside-bar right alignment
    return external_x


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
LENS_BAR_X0, LENS_BAR_X1 = 1420, 2260  # reserve 30 logical units inside panel

# Final pull-back banner (bottom of the world; visible when camera zooms out)
BANNER = (480, 1120, 1920, 1270)

KEYFRAMES = [
    (0,   "DESK_EMPTY"),
    (60,  "STICKERS_LANDING"),
    (135, "LEADER_LABEL"),
    (195, "BARS_GROW"),
    (255, "NUMBERS_SOURCE"),
    (285, "PULLBACK_STOCK_NOT_USABLE_SUPPLY"),
]


# ---- camera: pan + zoom ONLY (不切镜头), continuous long eases --------------
# (frame, pan_x, pan_y, zoom_pct). Smoothstep between keys; constant 290..299
# Spatial framing is deliberately wider so the sticker group and chart remain
# complete together. Original key TIMES and smoothstep interpolation are kept.
CAMERA_KEYS = [
    (0,   140, 80, 39),
    (140, 140, 80, 39),
    (195, 200, 100, 40),
    (255, 200, 100, 40),
    (290, 100, 30, 36),
    (299, 100, 30, 36),
]


def _smoothstep(t):
    t = 0.0 if t < 0 else (1.0 if t > 1 else t)
    return t * t * (3 - 2 * t)


def camera(n):
    """Continuous (pan_x, pan_y, zoom_pct); quantize only final raster crop.

    Rounding zoom to whole percentages caused discrete 2.56% jumps even
    though the schedule uses smoothstep. Preserve the analytic easing here.
    """
    n = int(n)
    if n <= CAMERA_KEYS[0][0]:
        return CAMERA_KEYS[0][1], CAMERA_KEYS[0][2], CAMERA_KEYS[0][3]
    for i in range(len(CAMERA_KEYS) - 1):
        f0, x0, y0, z0 = CAMERA_KEYS[i]
        f1, x1, y1, z1 = CAMERA_KEYS[i + 1]
        if n <= f1:
            t = _smoothstep((n - f0) / float(f1 - f0))
            return (x0 + (x1 - x0) * t,
                    y0 + (y1 - y0) * t,
                    z0 + (z1 - z0) * t)
    return CAMERA_KEYS[-1][1], CAMERA_KEYS[-1][2], CAMERA_KEYS[-1][3]


# ---- die-cut sticker sprites (deterministic vector cutouts) ----------------
# Built ONCE at import; each sprite = soft shadow + UNIFORM 10px white outline
# + flat vector illustration. No photo / external asset / RNG.
SW, SH = 420, 340                  # logical sprite bounds
SPRITE_PIXEL_W, SPRITE_PIXEL_H = SW * RASTER_SCALE, SH * RASTER_SCALE


def _silhouette(kind):
    """Return an L-mode mask of the die-cut shape (255 inside)."""
    m = Image.new("L", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), 0)
    d = GeometryDraw(m)
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
    img = Image.new("RGBA", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), base + (255,))
    d = GeometryDraw(img)
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
    dil = m.filter(ImageFilter.MaxFilter(2 * WHITE_OUTLINE * RASTER_SCALE + 1))
    border = ImageChops.subtract(dil, m)
    # soft drop shadow: blurred dilated silhouette, offset (9,11), faint alpha
    sh = ImageChops.offset(dil.filter(ImageFilter.GaussianBlur(8 * RASTER_SCALE)),
                          9 * RASTER_SCALE, 11 * RASTER_SCALE)
    sh = sh.point(lambda a: (a * 90) // 255)

    sprite = Image.new("RGBA", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), (0, 0, 0, 0))
    sh_layer = Image.new("RGBA", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), SHADOW_RGB + (0,))
    sh_layer.putalpha(sh)
    sprite = Image.alpha_composite(sprite, sh_layer)
    wb = Image.new("RGBA", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), WHITE + (0,))
    wb.putalpha(border)
    sprite = Image.alpha_composite(sprite, wb)
    illu = Image.composite(_illustration(kind),
                           Image.new("RGBA", (SPRITE_PIXEL_W, SPRITE_PIXEL_H), (0, 0, 0, 0)), m)
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
    draw.text(xy, text, font=font(size * draw.scale), fill=color)


def draw_desk_grid(draw):
    x0, y0 = -PAGE_OFFSET[0], -PAGE_OFFSET[1]
    for gx in range(x0, PAGE_W + x0 + 1, 80):
        draw.line([(gx, y0), (gx, PAGE_H + y0)], fill=GRID, width=1)
    for gy in range(y0, PAGE_H + y0 + 1, 80):
        draw.line([(x0, gy), (PAGE_W + x0, gy)], fill=GRID, width=1)


def draw_stickers(world, n):
    for prop, (x, y) in STICKER_POS.items():
        add = ADD_FRAMES[prop]
        off = stamp_drop(n, add)
        if off is None:
            continue
        sprite = SPRITES[STICKER_KIND[prop]]
        world.paste(sprite.convert("RGB"), ((x + PAGE_OFFSET[0]) * RASTER_SCALE,
                                           (y + off + PAGE_OFFSET[1]) * RASTER_SCALE),
                    sprite.getchannel("A"))


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
    T(draw, (ex + 14, ey - 22), TEXT["leader_title"], 30, INK)
    T(draw, (ex + 14, ey + 8), TEXT["leader_value"], 22, INK_LIGHT)


def draw_chart_furniture(draw):
    draw.rounded_rectangle(CHART_PANEL, radius=26, fill=PANEL,
                           outline=PANEL_EDGE, width=3)
    T(draw, (1280, 180), TEXT["chart_title"], 46, INK)
    T(draw, (1280, 240), TEXT["chart_subtitle"], 24, INK_LIGHT)
    draw.line([(1280, 282), (2280, 282)], fill=PANEL_EDGE, width=3)
    # inset lens furniture (declared x12 linear magnification)
    draw.rounded_rectangle(LENS_PANEL, radius=16, fill=(240, 244, 248),
                           outline=PANEL_EDGE, width=2)
    T(draw, (1290, 892), TEXT["lens_caption"], 26, INK_LIGHT)


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
        # freshwater lakes+rivers: ideal main span 0.04464 logical units,
        # integer metadata span 0, drawn full-growth span 2. The x12 inset's
        # ideal span is 0.53568, integer span 1, drawn span 2. This inherited
        # visibility FLOOR is not an exact-proportion claim. Larger bars
        # retain the shared scale subject to integer quantization.
        # Labels retain the source precision; the combined value is approximate.
        T(draw, (1290, yy + 6), label, 34, INK)
        draw.rectangle((BAR_X0, yy, BAR_X0 + max(length, 2), yy + BAR_HEIGHT),
                       fill=BAR_NEUTRAL, outline=BAR_NEUTRAL_DARK, width=2)
        T(draw, (bar_value_label_x(value, key == "lake", draw.scale), yy + 6), format_percent(value, key == "lake"), 34, INK)
        # inset lens bar (SAME linear rule, x12) — keeps proportionality honest
        # The same max(...,2) visibility floor applies in the inset.
        ly = 940 + i * 30
        lfull = bar_length(value, LENS)
        llen = (lfull * g) // 10
        if lfull > 0:
            T(draw, (1290, ly), format_percent(value, key == "lake"), 22, INK_LIGHT)
            endpoint = min(LENS_BAR_X0 + max(llen, 2), LENS_BAR_X1)
            draw.rectangle((LENS_BAR_X0, ly + 4, endpoint, ly + 20),
                           fill=BAR_NEUTRAL_DARK)
            if LENS_BAR_X0 + max(llen, 2) > LENS_BAR_X1:
                # The number stays 96.54%; // explicitly says this bar extends
                # beyond the inset. Never present the clipped endpoint as data.
                for slash_x in (LENS_BAR_X1 - 24, LENS_BAR_X1 - 12):
                    draw.line([(slash_x - 4, ly + 24), (slash_x + 6, ly)],
                              fill=PANEL, width=8)
                    draw.line([(slash_x - 4, ly + 24), (slash_x + 6, ly)],
                              fill=INK, width=3)


def draw_accent_highlight(draw, n):
    add = ADD_FRAMES["accent_highlight"]
    off = stamp_drop(n, add)
    if off is None:
        return
    oy = off
    # the ONE accent: a coral marker + "淡水" summary band
    draw.rounded_rectangle((1280, 830 + oy, 2280, 872 + oy), radius=8,
                           fill=ACCENT)
    T(draw, (1296, 832 + oy), TEXT["accent_label"], 28, WHITE)
    T(draw, (1960, 832 + oy), TEXT["accent_value"], 30, WHITE)


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
    T(draw, (x0 + 48, y0 + 22), TEXT["banner_title"], 60, INK)
    T(draw, (x0 + 48, y0 + 100), TEXT["banner_subtitle"],
      26, INK_LIGHT)


# ---- pure frame function ---------------------------------------------------
def crop_geometry(n):
    """Reframed spatial keys, original timing, and a separate screen HUD area."""
    pan_x, pan_y, zoom = camera(n)
    vw = (LOGICAL_W * 100) / zoom
    vh = (LOGICAL_CONTENT_H * 100) / zoom
    pan_x = min(max(pan_x, 0), PAGE_W - vw)
    pan_y = min(max(pan_y, 0), PAGE_H - vh)
    box = tuple(iround(v * RASTER_SCALE) for v in (pan_x, pan_y, pan_x + vw, pan_y + vh))
    physical_size = [box[2] - box[0], box[3] - box[1]]
    if physical_size[0] < W or physical_size[1] < CONTENT_H:
        raise ValueError("Camera would require pixel upsampling; increase world raster density")
    return {"logical_pan": [pan_x, pan_y], "zoom_percent": zoom,
            "logical_view_size": [vw, vh], "physical_crop_box": list(box),
            "physical_crop_size": physical_size,
            "content_screen_rectangle": [0, HUD_H, W, H],
            "resize_direction": "downsample_only"}


def render_frame(n, seed=SEED):
    """Native frame from newly rasterized high-density world; original seed unused."""
    n = int(n)
    if not 0 <= n < FRAMES:
        raise ValueError("frame index must be in [0, 299]")
    font_evidence()  # Fail clearly on a missing font/glyph; never silently fall back.
    world = Image.new("RGB", (WORLD_PIXEL_W, WORLD_PIXEL_H), DESK)
    wd = GeometryDraw(world, offset=PAGE_OFFSET)
    draw_desk_grid(wd)
    draw_stickers(world, n)
    draw_chart_furniture(wd)
    draw_leader_label(wd, n)
    draw_bars(wd, n)
    draw_accent_highlight(wd, n)
    draw_final_banner(wd, n)

    camera_geometry = crop_geometry(n)
    crop = world.crop(camera_geometry["physical_crop_box"])
    content = crop.resize((W, CONTENT_H), Image.Resampling.BILINEAR)
    view = Image.new("RGB", (W, H), (248, 250, 252))
    view.paste(content, (0, HUD_H))

    d = GeometryDraw(view)
    # fixed screen-space HUD strap (a HUD, NOT a scene cut)
    d.line([(0, HUD_H / RASTER_SCALE - 1),
            (LOGICAL_W, HUD_H / RASTER_SCALE - 1)], fill=PANEL_EDGE, width=1)
    T(d, (14, 6), TEXT["hud_title"], 20, INK)
    T(d, (LOGICAL_W - 210, 6), "frame %03d / 300" % min(n, 290), 20, INK_LIGHT)
    return view


def frame_path(n):
    return FRAME_DIR / ("f%04d.png" % n)


def sha_of(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_frame(n, img=None, out_dir=None, seed=SEED):
    out = out_dir or FRAME_DIR
    Path(out).mkdir(parents=True, exist_ok=True)
    if img is None:
        img = render_frame(n, seed)
    p = Path(out) / ("f%04d.png" % n)
    img.save(p, format="PNG", compress_level=9, optimize=False)
    return sha_of(p)


def render_metadata(seed=SEED):
    return {
        "renderer": RENDERER_VERSION,
        "source_sha256": sha_of(__file__),
        "original_source_sha256": ORIGINAL_SOURCE_SHA256,
        "camera_base_source_sha256": CAMERA_BASE_SOURCE_SHA256,
        "data_source": DATA_SOURCE,
        "data_correction_scope": "Values, labels, precision and provenance; only an overflowing value label moves inside its bar. Bar geometry, camera, add schedule and animation timing preserved from the camera baseline.",
        "numeric_label_fit": "Use actual font width; if an external label exceeds the paper's right safe edge, align it inside the full bar with an 18-logical-unit right inset.",
        "logical_resolution": [LOGICAL_W, LOGICAL_H],
        "resolution": [W, H], "fps": FPS, "frames": FRAMES,
        "logical_world": [WORLD_W, WORLD_H],
        "page_size": [PAGE_W, PAGE_H], "page_offset": list(PAGE_OFFSET),
        "physical_world": [WORLD_PIXEL_W, WORLD_PIXEL_H],
        "physical_sprites": [SPRITE_PIXEL_W, SPRITE_PIXEL_H],
        "spatial_generation": "vector geometry rasterized at double world density, camera crop downsampled to native viewport",
        "layout_change": {"hud_height_native": HUD_H,
                          "scene_screen_rectangle": [0, HUD_H, W, H],
                          "camera_spatial_keys_changed": True,
                          "camera_key_times_and_smoothstep_preserved": True,
                          "reason": "Keep both sticker group and chart visible, reserve real HUD space, include end banner"},
        "seed": seed, "seed_affects_pixels": False,
        "seed_note": "Original renderer did not use seed; no new seed behavior is fabricated.",
        "font": font_evidence(), "pillow_version": PILLOW_VERSION,
        "bar_visibility_exception": "Original max(length, 2) logical-unit floor remains disclosed; bars are not universally exact proportional pixels.",
        "lens_clipping_exception": {"logical_x_limits": [LENS_BAR_X0, LENS_BAR_X1],
                                    "clipped_bar_marker": "//",
                                    "visible_caption": TEXT["lens_caption"],
                                    "meaning": "Clipped spans are not exact proportions; numeric labels retain the source value rather than a clipped-length value."},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("keys", "all", "full", "batch", "range", "manifest"))
    parser.add_argument("indices", nargs="?", help="batch list or range start")
    parser.add_argument("end", nargs="?", type=int, help="exclusive range end")
    parser.add_argument("--outdir", type=Path, default=HERE)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    if args.mode == "batch":
        if not args.indices:
            parser.error("batch requires comma-separated frame indices")
        indices = [int(t) for t in args.indices.split(",")]
    elif args.mode == "range":
        if args.indices is None or args.end is None:
            parser.error("range requires start and exclusive end")
        indices = list(range(int(args.indices), args.end))
    elif args.mode == "keys":
        indices = [n for n, _ in KEYFRAMES]
    else:
        indices = list(range(FRAMES))
    if any(not 0 <= n < FRAMES for n in indices):
        parser.error("frame indices must be in [0, 299]")
    directory = args.outdir / ("stills" if args.mode == "keys" else "frames")
    if args.mode == "manifest":
        hashes = {}
        for n in indices:
            p = directory / ("f%04d.png" % n)
            with Image.open(p) as img:
                if img.size != (W, H):
                    raise ValueError("wrong frame dimensions: " + str(p))
            hashes["%04d" % n] = sha_of(p)
    else:
        hashes = {"%04d" % n: save_frame(n, out_dir=directory, seed=args.seed) for n in indices}
    report = render_metadata(args.seed)
    report.update({"mode": args.mode, "rendered_frames": 0 if args.mode == "manifest" else len(indices),
                   "hashes": hashes})
    args.outdir.mkdir(parents=True, exist_ok=True)
    (args.outdir / "render_manifest.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    if len(hashes) == FRAMES:
        (directory / "frame_hashes.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"mode": args.mode, "resolution": [W, H], "hashes": hashes,
                      "seed_affects_pixels": False, "ok": True}))


# ---- exported SEMANTICS for verify.py (verifier uses the REAL shipped funcs) -
def sticker_kinds():
    return list(SPRITES.keys())


def white_outline_width(prop):
    """同样宽的白边 — returns WHITE_OUTLINE for EVERY prop (no exceptions)."""
    return WHITE_OUTLINE


def bars_with_lengths():
    """Metadata lengths = UNclamped proportional bar_length(value) (see
    bar_length docstring). The drawn rectangle in draw_bars adds a separate
    max(...,2) minimum-visible-size floor for the tiny combined group.
    That floor is NOT included here, so this remains a shared-scale metadata
    check rather than a claim that every drawn pixel span is proportional."""
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
