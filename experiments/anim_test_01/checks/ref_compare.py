# -*- coding: utf-8 -*-
"""与官方参考成片 ref/20-pixel.mp4（mg-styles-15，MIT）的机械对照：
   色数、帧更新节奏（零差分帧）、构图三帧目视对照（图在 ref/）
   运行：python checks/ref_compare.py
   前置（ref/all/ 已在跑完后删除以省盘，重跑前先重建）：
     curl -sL -o ref/20-pixel.mp4 https://raw.githubusercontent.com/Vincentwei1021/mg-styles-15/main/videos/20-pixel.mp4
     mkdir -p ref/all && ffmpeg -v error -y -i ref/20-pixel.mp4 -fps_mode passthrough ref/all/r%04d.png
"""
import glob
import numpy as np
from PIL import Image

def grid(p):
    return np.asarray(Image.open(p).convert('RGB'))[3::6, 3::6]

def analyze(name, paths):
    prev = None; zero = 0; tot = 0; uni = set(); per = []; dlist = []
    for p in paths:
        g = grid(p)
        s = set(map(tuple, g.reshape(-1, 3)))
        uni |= s; per.append(len(s))
        if prev is not None:
            d = np.abs(g.astype(np.int16) - prev).mean()
            dlist.append(d); tot += 1
            if d == 0: zero += 1
        prev = g
    per = np.array(per); d = np.array(dlist)
    print(f'--- {name} ---')
    print(f'frames = {len(paths)}')
    print(f'unique colors (union) = {len(uni)}')
    print(f'per-frame unique: min={per.min()} max={per.max()} mean={per.mean():.1f}')
    print(f'identical-to-previous frames (holds) = {zero}/{tot} ({100*zero/tot:.0f}%)')
    print(f'mean abs diff per frame: mean={d.mean():.2f} max={d.max():.2f} '
          f'frames with diff>1.0 = {(d>1.0).sum()}')

analyze('本项目 out.mp4 逐帧 PNG（frames/）', sorted(glob.glob('frames/f*.png')))
print()
analyze('官方 20-pixel.mp4（ref/all/）', sorted(glob.glob('ref/all/r*.png')))
