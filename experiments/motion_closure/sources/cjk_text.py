"""Rasterize named text at its final pixel size with an existing local font.

No fonts or glyph assets are bundled. The exact font bytes and Pillow version
are part of the render dependency, not an assertion of cross-font identity.
"""
from pathlib import Path
import base64, hashlib, json, os, sys
from PIL import Image, ImageDraw, ImageFont, __version__ as PILLOW_VERSION

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
request = json.load(sys.stdin)
selected = os.environ.get("MOTION_CJK_FONT")
if not selected:
    selected = next((str(p) for p in (
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    ) if p.is_file()), None)
if not selected or not Path(selected).is_file():
    raise RuntimeError("Set MOTION_CJK_FONT to an installed CJK font; no bitmap fallback.")
index = int(os.environ.get("MOTION_CJK_FONT_INDEX", "0"))
glyphs = {}
for item in request:
    font = ImageFont.truetype(selected, int(item["size"]), index=index)
    absent = font.getmask("\U0010ffff")
    missing = (absent.size, bytes(absent))
    for ch in item["text"]:
        mask = font.getmask(ch)
        if not ch.isspace() and (mask.size, bytes(mask)) == missing:
            raise RuntimeError("CJK glyph missing: " + ch)
    x0, y0, x1, y1 = font.getbbox(item["text"])
    width, height = x1-x0, y1-y0
    if width <= 0 or height <= 0:
        raise RuntimeError("Empty text raster")
    im = Image.new("L", (width, height), 0)
    ImageDraw.Draw(im).text((-x0, -y0), item["text"], font=font, fill=255)
    glyphs[item["id"]] = {"width": width, "height": height,
        "alpha": base64.b64encode(im.tobytes()).decode("ascii"),
        "text": item["text"], "size": item["size"]}
print(json.dumps({"glyphs": glyphs, "evidence": {
    "font_file": Path(selected).name, "font_sha256": hashlib.sha256(Path(selected).read_bytes()).hexdigest(),
    "face_index": index, "font_family": list(font.getname()), "pillow_version": PILLOW_VERSION,
    "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "requests": request, "missing_glyphs": [], "fallback_used": False,
    "rasterization": "Font outlines rasterized directly at final output pixel size; no scene upscaling"
}}, ensure_ascii=False))
