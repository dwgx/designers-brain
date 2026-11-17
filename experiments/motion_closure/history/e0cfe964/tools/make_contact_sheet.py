#!/usr/bin/env python3
"""Build a small contact sheet (<=8 keyframes) from a delivered MP4.

Decodes the mp4, samples 8 evenly spaced frames, downsizes to thumbnails and lays
them out in a 4x2 grid with a small index label. Saves a compact JPEG. This proves
the delivered bytes produce visibly distinct, non-static frames.

Usage: python make_contact_sheet.py <mp4> <out.jpg> [thumb_w]
"""
import os
import sys
import cv2
from PIL import Image, ImageDraw

NTHUMBS = 8


def main():
    mp4, out = sys.argv[1], sys.argv[2]
    tw = int(sys.argv[3]) if len(sys.argv) > 3 else 320
    th = tw * 9 // 16
    cap = cv2.VideoCapture(mp4)
    total = 0
    while True:
        ok, _ = cap.read()
        if not ok:
            break
        total += 1
    cap.release()
    idxs = [round(i * (total - 1) / (NTHUMBS - 1)) for i in range(NTHUMBS)]
    cap = cv2.VideoCapture(mp4)
    thumbs = []
    for target in idxs:
        frame = None
        while total and cap.get(cv2.CAP_PROP_POS_FRAMES) <= target:
            ok, frame = cap.read()
            if not ok:
                break
        if frame is None:
            ok, frame = cap.read()
        if frame is None:
            thumbs.append(Image.new("RGB", (tw, th), (0, 0, 0)))
            continue
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        thumbs.append(Image.fromarray(rgb).resize((tw, th), Image.Resampling.BILINEAR))
    cap.release()

    label_h = 18
    sheet = Image.new("RGB", (tw * 4, (th + label_h) * 2), (30, 30, 30))
    d = ImageDraw.Draw(sheet)
    for k, (im, n) in enumerate(zip(thumbs, idxs)):
        x = (k % 4) * tw
        y = (k // 4) * (th + label_h)
        sheet.paste(im, (x, y + label_h))
        d.text((x + 4, y + 3), "f%03d" % n, fill=(255, 255, 255))
    sheet.save(out, "JPEG", quality=70, optimize=True)
    print("contact_sheet=%s sampled=%s bytes=%d" %
          (os.path.basename(out), ",".join(str(i) for i in idxs), os.path.getsize(out)))


if __name__ == "__main__":
    main()
