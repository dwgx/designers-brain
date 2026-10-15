"""make_sheets.py — contact sheets: key/keyframes_sheet.png + checks/review sheets.
Run: blender -b --factory-startup --python make_sheets.py
"""
import bpy, os
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))

FONT = {
 '0': ["01110","10001","10001","10001","10001","10001","01110"],
 '1': ["00100","01100","00100","00100","00100","00100","01110"],
 '2': ["01110","10001","00001","00010","00100","01000","11111"],
 '3': ["11111","00010","00100","00010","00001","10001","01110"],
 '4': ["00010","00110","01010","10010","11111","00010","00010"],
 '5': ["11111","10000","11110","00001","00001","10001","01110"],
 '6': ["00110","01000","10000","11110","10001","10001","01110"],
 '7': ["11111","00001","00010","00100","01000","01000","01000"],
 '8': ["01110","10001","10001","01110","10001","10001","01110"],
 '9': ["01110","10001","10001","01111","00001","00010","01100"],
 'f': ["00110","01000","01000","11100","01000","01000","01000"],
 ':': ["00000","00100","00000","00100","00000","00000","00000"],
}

def draw_text(sheet, text, x, y_top, scale=3, color=0.92):
    """x, y_top in display coords (top-left origin); sheet is bottom-up HxWx4."""
    H = sheet.shape[0]
    w_char = 6 * scale
    h_char = 7 * scale
    # background box
    x1 = x - scale; x2 = x + w_char * len(text) + scale
    y1 = H - y_top - h_char - scale; y2 = H - y_top + scale
    sheet[max(0, y1):y2, max(0, x1):x2, :3] *= 0.25
    for ci, ch in enumerate(text):
        rows = FONT.get(ch)
        if not rows:
            continue
        for ry, row in enumerate(rows):
            for rx, v in enumerate(row):
                if v == '1':
                    px = x + ci * w_char + rx * scale
                    py = H - y_top - (ry + 1) * scale
                    sheet[py:py + scale, px:px + scale, :3] = color
    return sheet

def load_tile(path, stride=1):
    im = bpy.data.images.load(path)
    w, h = im.size
    a = np.empty(w * h * im.channels, dtype=np.float32)
    im.pixels.foreach_get(a)
    a = a.reshape(h, w, im.channels)
    bpy.data.images.remove(im)
    if stride > 1:
        a = a[::stride, ::stride]
    if a.shape[2] == 3:
        a = np.concatenate([a, np.ones((*a.shape[:2], 1), np.float32)], axis=2)
    return a

def sheet_from(files, cols, stride, labels=None, out=None, label_scale=3, label_step=1):
    tiles = [load_tile(f, stride) for f in files]
    h, w, _ = tiles[0].shape
    rows = (len(tiles) + cols - 1) // cols
    sheet = np.zeros((rows * h, cols * w, 4), np.float32)
    sheet[:, :, 3] = 1.0
    for i, a in enumerate(tiles):
        r_top, c = divmod(i, cols)
        r_bot = rows - 1 - r_top
        sheet[r_bot * h:(r_bot + 1) * h, c * w:(c + 1) * w, :] = a
        if labels and (i % label_step == 0):
            draw_text(sheet, labels[i], c * w + 6, r_top * h + 6, scale=label_scale)
    img = bpy.data.images.new("sheet", width=cols * w, height=rows * h, alpha=False)
    img.pixels.foreach_set(sheet.ravel())
    img.filepath_raw = out
    img.file_format = "PNG"
    img.save()
    bpy.data.images.remove(img)
    print("SHEET", out, cols * w, "x", rows * h, "tiles", len(tiles), flush=True)

# key sheet: 6 keyframes at half res, 3x2
kf = [0, 50, 100, 150, 200, 250]
files = [os.path.join(BASE, "key", "k%04d.png" % f) for f in kf]
if all(os.path.exists(f) for f in files):
    sheet_from(files, 3, 2, ["f%04d" % f for f in kf],
               os.path.join(BASE, "key", "keyframes_sheet.png"), label_scale=3)
else:
    print("key frames missing, skip key sheet", flush=True)

# review sheet: every 10th frame (30 tiles @ 320x180), 6x5
fr = sorted(f for f in os.listdir(os.path.join(BASE, "frames")) if f.endswith(".png"))
if fr:
    sel = [os.path.join(BASE, "frames", f) for f in fr[::10]]
    sheet_from(sel, 6, 6, [f[1:5] for f in fr[::10]],
               os.path.join(BASE, "checks", "review_sheet.png"), label_scale=2)

# fine sheet: every 3rd frame (100 tiles @ 192x108), 10x10
if fr:
    sel = [os.path.join(BASE, "frames", f) for f in fr[::3]]
    sheet_from(sel, 10, 10, [f[1:5] for f in fr[::3]],
               os.path.join(BASE, "checks", "review_fine.png"), label_scale=1, label_step=5)
print("SHEETS_DONE")
