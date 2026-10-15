# -*- coding: utf-8 -*-
"""B-07 / anim_test_01 逐帧自查（机械检查器，只读产物）
运行：python checks/selfcheck.py
输出：调色板/色数、关键帧、结尾文案帧、确定性回归、块结构验证
"""
import os, sys, glob, hashlib, subprocess
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CW, CH, S = 320, 180, 6
PAL = {
    'ink0':'#0d0a14','ink1':'#241432','ink2':'#43224a',
    'sky0':'#1c1638','sky1':'#38265c','sky2':'#682c66','sky3':'#a33a5c','sky4':'#d9613b','sky5':'#f59a3f',
    'sun0':'#ffd76e','sun1':'#fff2bd',
    'wat0':'#0e1630','wat1':'#1b2a4e','wat2':'#2f4670','wat3':'#5c3f6e','wat4':'#a8523f',
    'gold0':'#b8732c','gold1':'#edb144','gold2':'#ffe08a',
    'red0':'#cf3a3a','white':'#f8f4e6','pink0':'#e0708c',
    'brn0':'#6d4a2a','brn1':'#9c7340','grn0':'#3f7a52',
}
PALRGB = {tuple(int(v[i:i+2],16) for i in (1,3,5)): k for k,v in PAL.items()}
HEXRGB = {k: tuple(int(v[i:i+2],16) for i in (1,3,5)) for k,v in PAL.items()}

def source_grid(path):
    """1920x1080 -> 320x180（每 6x6 块取中心像素；块结构在下方单独验证）"""
    a = np.asarray(Image.open(path).convert('RGB'))
    return a[3::S, 3::S]

print('=== 1. 帧文件与块结构 ===')
frames = sorted(glob.glob('frames/f*.png'))
print('frames/*.png count =', len(frames))
im0 = np.asarray(Image.open(frames[0]).convert('RGB'))
# 块结构验证：每 6x6 块内是否同色（抽样 200 个块）
bad = 0; checked = 0
rng = np.random.default_rng(0)
for _ in range(200):
    by, bx = int(rng.integers(0, CH)), int(rng.integers(0, CW))
    blk = im0[by*S:(by+1)*S, bx*S:(bx+1)*S].reshape(-1,3)
    checked += 1
    if not np.all(blk == blk[0]): bad += 1
print(f'block uniformity: {checked-bad}/{checked} sampled 6x6 blocks are single-color')

print()
print('=== 2. 唯一色数（全片 300 帧并集） ===')
uni = set(); per = []
for p in frames:
    g = source_grid(p)
    s = set(map(tuple, g.reshape(-1,3)))
    uni |= s; per.append(len(s))
per = np.array(per)
print('unique colors across ALL 300 frames =', len(uni))
print(f'per-frame unique: min={per.min()} max={per.max()} mean={per.mean():.1f}')
outside = sorted(c for c in uni if c not in PALRGB)
print('colors outside declared 25-color palette =', len(outside), outside[:8])
used = sorted(PALRGB[c] for c in uni if c in PALRGB)
print('palette entries actually used =', len(used), used)

print()
print('=== 3. 6 关键帧 ===')
KEYS = [0, 50, 100, 150, 200, 250]
for f in KEYS:
    p = f'key/k{f:04d}.png'
    if not os.path.exists(p):
        print(f'{p}: MISSING'); continue
    im = Image.open(p)
    h = hashlib.sha256(open(p,'rb').read()).hexdigest()[:16]
    print(f'{p}: {im.size[0]}x{im.size[1]} {os.path.getsize(p)}B sha256:{h}')
print('keyframes_sheet.png:', Image.open('key/keyframes_sheet.png').size)
# 关键帧两两不同（防止渲染卡死在同一画面）
gs = [source_grid(f'key/k{f:04d}.png') for f in KEYS]
print('pairwise differing-pixel counts (of 57600):')
for i in range(len(KEYS)):
    row = []
    for j in range(len(KEYS)):
        d = int(np.any(gs[i] != gs[j], axis=2).sum()) if i != j else 0
        row.append(f'{d:5d}')
    print('  k%04d ' % KEYS[i] + ' '.join(row))

print()
print('=== 4. 结尾文案「大丰收！」帧 ===')
def text_pixels(fr):
    g = source_grid(fr)
    box = g[72:72+32, 96:96+128]                     # 4 字 × 32px，x=96..224, y=72..104
    white = np.all(box == np.array(HEXRGB['white']), axis=2)
    return box, int(white.sum())
for fr in ['frames/f0269.png', 'frames/f0270.png', 'frames/f0273.png', 'frames/f0299.png']:
    box, n = text_pixels(fr)
    print(f'{fr}: white(text) pixels in bbox = {n}')
box, n = text_pixels('frames/f0299.png')
white = np.all(box == np.array(HEXRGB['white']), axis=2)
mask = white[0::2, :] | white[1::2, :]     # 每源像素占 2 行，取或（补回被扫描线压暗的行）
print('f0299 文案位图（32px 字面 -> 16x16 字面；左->右：大 丰 收 ！）:')
for r in range(16):
    line = ''
    for gx in range(4):
        for c in range(16):
            line += '#' if mask[r, gx*32 + c*2] else '.'
        line += '  '
    print('  ' + line)

print('=== 5. 确定性回归（同帧两跑，SHA256 比对） ===')
for f in [0, 150, 299]:
    a = f'frames/f{f:04d}.png'; b = f'checks/rerun/f{f:04d}.png'
    if not os.path.exists(b):
        print(f'{b}: MISSING'); continue
    ha = hashlib.sha256(open(a,'rb').read()).hexdigest()
    hb = hashlib.sha256(open(b,'rb').read()).hexdigest()
    print(f'f{f:04d}: {"IDENTICAL" if ha==hb else "DIFFERS"}  {ha[:16]} / {hb[:16]}')
