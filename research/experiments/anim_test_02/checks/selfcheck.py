# -*- coding: utf-8 -*-
"""anim_test_02 / B-17 自查脚本
机械检查：帧数尺寸 / 一笔画连通性 / 线宽恒定 / 笔尖光点 / 闭合填色 / 结尾文案 /
         帧间统计 / 音轨包络 / 色数（抽样）
用法：python checks/selfcheck.py > checks/selfcheck_output.txt
"""
import os, sys, wave, hashlib
import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FR   = os.path.join(ROOT, 'frames')

INK  = np.array([0x33,0x2f,0x2a], dtype=np.int32)
DOT  = np.array([0xff,0x9d,0x1f], dtype=np.int32)
SKY  = np.array([0xf6,0xc4,0x53], dtype=np.int32)
MTN  = np.array([0x38,0x68,0x4e], dtype=np.int32)
SUN  = np.array([0xe2,0x66,0x2e], dtype=np.int32)
TEXT = np.array([0x2f,0x5d,0x45], dtype=np.int32)

BADGE = (1050, 500, 270)
TEXT_BBOX = (790, 800, 1310, 980)      # x0,y0,x1,y1（文案区，排除用）
TOL = 60

def load(f):
    p = os.path.join(FR, 'f%04d.png' % f)
    return np.asarray(Image.open(p).convert('RGB')).astype(np.int32)

def near(img, color, tol=TOL):
    d = img - color.reshape(1,1,3)
    return (d*d).sum(axis=2) <= tol*tol

def main():
    out = []
    P = out.append

    # ---- 0. 帧文件与尺寸 ----
    fs = sorted(os.listdir(FR))
    P('=== 0. 帧文件 ===')
    P('frames/*.png count = %d' % len(fs))
    im0 = Image.open(os.path.join(FR, 'f0000.png'))
    P('frame size = %dx%d' % im0.size)

    # ---- 1. 一笔画：整片一根线（连通性） ----
    P('')
    P('=== 1. 一笔画连通性（墨色 mask → 8 连通分量；期望 1 个主体） ===')
    probe = [0, 30, 63, 100, 126, 150, 182, 200, 230, 250, 266, 275, 284, 290, 299]
    for f in probe:
        img = load(f)
        m = near(img, INK)
        if f >= 284:                    # 文案阶段：排除文案区（文案非“线”）
            x0,y0,x1,y1 = TEXT_BBOX
            m[y0:y1, x0:x1] = False
        lab, n = ndimage.label(m, structure=np.ones((3,3), int))
        sizes = np.bincount(lab.ravel())[1:]
        big = int((sizes > 50).sum())
        P('f%04d ink_px=%7d comps>50px=%d  comps_all=%d  max=%d' %
          (f, int(m.sum()), big, int(n), int(sizes.max()) if n else 0))

    # ---- 2. 线宽恒定（腐蚀 + 直段横切） ----
    P('')
    P('=== 2. 线宽恒定（5x5 腐蚀两次后残留 = 交叉/结点；直段横切游程） ===')
    for f in [63, 126, 200, 250]:
        img = load(f)
        m = near(img, INK)
        e1 = ndimage.binary_erosion(m, iterations=1)
        e2 = ndimage.binary_erosion(m, iterations=2)
        P('f%04d ink=%7d after_erode1=%6d after_erode2=%5d' %
          (f, int(m.sum()), int(e1.sum()), int(e2.sum())))
    # 直段横切：f126 上管（近似直线 y=760 附近）与座管
    img = load(126)
    m = near(img, INK)
    for y in [755, 760, 765]:
        row = m[y]
        runs, cur = [], 0
        for v in row:
            if v: cur += 1
            elif cur: runs.append(cur); cur = 0
        if cur: runs.append(cur)
        P('f0126 row y=%d ink runs = %s' % (y, runs))
    for x in [650, 660]:
        col = m[:, x]
        runs, cur = [], 0
        for v in col:
            if v: cur += 1
            elif cur: runs.append(cur); cur = 0
        if cur: runs.append(cur)
        P('f0126 col x=%d ink runs = %s' % (x, runs))
    # 徽章圆描边宽度（f299 过圆心横切：期望左右各 3-4px）
    img = load(299)
    m = near(img, INK)
    row = m[500]
    runs, cur, pos, rr = [], 0, 0, []
    for i, v in enumerate(row):
        if v: cur += 1
        elif cur: rr.append((pos, cur)); cur = 0
        if not v: pos = i+1
    P('f0299 row y=500 ink runs (x,len) = %s' % rr)

    # ---- 3. 笔尖光点 ----
    P('')
    P('=== 3. 笔尖光点（近 #ff9d1f；f0-266 在，填色后熄灭） ===')
    for f in [0, 60, 126, 150, 200, 250, 266, 270, 280, 299]:
        img = load(f)
        m = near(img, DOT, 40)
        cnt = int(m.sum())
        if cnt:
            ys, xs = np.nonzero(m)
            P('f%04d dot_px=%4d centroid=(%.1f, %.1f)' % (f, cnt, xs.mean(), ys.mean()))
        else:
            P('f%04d dot_px=%4d' % (f, cnt))

    # ---- 4. 闭合填色（从一点向外，面积单调增） ----
    P('')
    P('=== 4. 闭合填色（徽章圆内 天空/山体/太阳 色像素数） ===')
    cx, cy, r = BADGE
    yy, xx = np.mgrid[0:1080, 0:1920]
    inside = (xx-cx)**2 + (yy-cy)**2 <= r*r
    prev = -1
    mono = True
    for f in list(range(264, 285, 2)) + [299]:
        img = load(f)
        m = (near(img, SKY, 40) | near(img, MTN, 40) | near(img, SUN, 40)) & inside
        cnt = int(m.sum())
        if cnt < prev - 100: mono = False     # 容差 100px：填色边缘抗锯齿 ±<100
        prev = cnt
        P('f%04d fill_px=%7d' % (f, cnt))
    P('monotonic_non_decreasing (tol 100px) = %s' % mono)
    P('badge_area = %d' % int(inside.sum()))

    # ---- 5. 结尾文案 ----
    P('')
    P('=== 5. 结尾文案「山野骑行」（深绿 #2f5d45，文案区内） ===')
    x0,y0,x1,y1 = TEXT_BBOX
    for f in [280, 284, 288, 292, 299]:
        img = load(f)
        m = near(img, TEXT)
        box = np.zeros_like(m); box[y0:y1, x0:x1] = True
        mm = m & box
        cnt = int(mm.sum())
        if cnt > 200:
            ys, xs = np.nonzero(mm)
            P('f%04d text_px=%6d bbox=(%d,%d)-(%d,%d)' % (f, cnt, xs.min(), ys.min(), xs.max(), ys.max()))
        else:
            P('f%04d text_px=%6d' % (f, cnt))

    # ---- 6. 帧间统计（holds / 平均差） ----
    P('')
    P('=== 6. 帧间统计（全 300 帧） ===')
    hashes = []
    for f in range(300):
        with open(os.path.join(FR, 'f%04d.png' % f), 'rb') as fh:
            hashes.append(hashlib.sha256(fh.read()).hexdigest())
    holds = sum(1 for i in range(1, 300) if hashes[i] == hashes[i-1])
    P('identical-to-previous frames = %d/299 (%.0f%%)' % (holds, 100*holds/299))
    grays = []
    for f in range(300):
        g = Image.open(os.path.join(FR, 'f%04d.png' % f)).convert('L').resize((480, 270))
        grays.append(np.asarray(g, dtype=np.int16))
    diffs = [float(np.abs(grays[i].astype(np.int32) - grays[i-1].astype(np.int32)).mean()) for i in range(1, 300)]
    diffs = np.array(diffs)
    P('mean abs diff per frame: mean=%.3f max=%.3f frames with diff>0.5 = %d' %
      (diffs.mean(), diffs.max(), int((diffs > 0.5).sum())))

    # ---- 7. 色数（抽样：每 6 帧取 1 帧） ----
    P('')
    P('=== 7. 色数（抽样 50 帧并集；本片无“限色”约束，仅记录） ===')
    union = set()
    per = []
    for f in range(0, 300, 6):
        img = load(f)
        cols = set(map(tuple, img.reshape(-1,3)[::7]))
        union |= cols
        per.append(len(cols))
    P('sampled frames = 50, union colors = %d, per-frame min=%d max=%d' %
      (len(union), min(per), max(per)))

    # ---- 8. 音轨包络 ----
    P('')
    P('=== 8. 音轨（audio/score.wav 逐秒 RMS/峰值） ===')
    with wave.open(os.path.join(ROOT, 'audio', 'score.wav'), 'rb') as w:
        sr = w.getframerate(); n = w.getnframes(); ch = w.getnchannels()
        data = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float64)/32768.0
        data = data.reshape(-1, ch)
        P('sr=%d ch=%d frames=%d dur=%.3fs' % (sr, ch, n, n/sr))
        for s in range(10):
            seg = data[s*sr:(s+1)*sr]
            P('  t=%d-%ds rms=%.3f peak=%.3f' % (s, s+1, float(np.sqrt((seg**2).mean())), float(np.abs(seg).max())))

    # ---- 9. 6 关键帧 ----
    P('')
    P('=== 9. 6 关键帧（key/） ===')
    keys = [0, 50, 100, 150, 200, 250]
    imgs = []
    for f in keys:
        p = os.path.join(ROOT, 'key', 'k%04d.png' % f)
        b = open(p, 'rb').read()
        P('key/k%04d.png: %s %dB sha256:%s' % (f, Image.open(p).size, len(b), hashlib.sha256(b).hexdigest()[:16]))
        imgs.append(np.asarray(Image.open(p).convert('L').resize((480,270)), dtype=np.int32))
    P('pairwise differing-pixel counts (of 129600, |diff|>10):')
    hdr = '        ' + ''.join('%8d' % f for f in keys)
    P(hdr)
    for i, f in enumerate(keys):
        row = '%8d' % f
        for j in range(len(keys)):
            d = int((np.abs(imgs[i] - imgs[j]) > 10).sum()) if i != j else 0
            row += '%8d' % d
        P(row)
    sp = os.path.join(ROOT, 'key', 'keyframes_sheet.png')
    P('keyframes_sheet.png: %s' % (Image.open(sp).size,))

    # ---- 10. 官方参考帧 ----
    P('')
    P('=== 10. 官方参考帧（ref/02-line-art.mp4 抽取） ===')
    for n in ['ref_1', 'ref_2', 'ref_3']:
        p = os.path.join(ROOT, 'ref', n + '.png')
        P('%s.png: %s sha256:%s' % (n, Image.open(p).size, hashlib.sha256(open(p,'rb').read()).hexdigest()[:16]))

    print('\n'.join(out))

if __name__ == '__main__':
    main()
