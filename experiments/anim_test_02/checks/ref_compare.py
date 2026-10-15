# -*- coding: utf-8 -*-
"""anim_test_02 / B-17 与官方参考片对照（同系统、不同内容）
对照对象：ref/02-line-art.mp4（Vincentwei1021/mg-styles-15，MIT，2026-10 直取）
本项目：out.mp4
用法：python checks/ref_compare.py > checks/ref_compare_output.txt
"""
import os, subprocess
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def frames_gray(video, w=480, h=270):
    cmd = ['ffmpeg','-v','error','-i',video,'-vf','scale=%d:%d,format=gray'%(w,h),
           '-f','rawvideo','-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (w*h)
    return np.frombuffer(raw[:n*w*h], dtype=np.uint8).reshape(n, h, w).astype(np.int32)

def stats(a, label):
    print('--- %s ---' % label)
    print('frames = %d' % a.shape[0])
    d = np.abs(np.diff(a, axis=0)).mean(axis=(1,2))
    print('mean abs diff per frame: mean=%.3f max=%.3f frames with diff>0.5 = %d' %
          (d.mean(), d.max(), int((d > 0.5).sum())))
    same = int((np.abs(np.diff(a, axis=0)).max(axis=(1,2)) == 0).sum())
    print('identical-to-previous frames = %d/%d' % (same, a.shape[0]-1))
    return d

def probe(video, t, x, y):
    out = os.path.join(ROOT, 'checks', '_probe.png')
    subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',video,'-frames:v','1','-y',out], check=True)
    img = np.asarray(Image.open(out).convert('RGB'))
    os.remove(out)
    return img

def line_runs(img, fixed, axis, thresh):
    """沿 axis=col 扫一列/行，返回亮(或暗)游程长度"""
    if axis == 'col':
        v = img[:, fixed, :].mean(axis=1)
    else:
        v = img[fixed, :, :].mean(axis=1)
    m = (v < thresh) if thresh < 128 else (v > thresh)
    runs, cur = [], 0
    for b in m:
        if b: cur += 1
        elif cur: runs.append(cur); cur = 0
    if cur: runs.append(cur)
    return runs

def main():
    ref = os.path.join(ROOT, 'ref', '02-line-art.mp4')
    ours = os.path.join(ROOT, 'out.mp4')

    print('=== 规格 ===')
    for v, label in [(ref,'官方 02-line-art.mp4'), (ours,'本项目 out.mp4')]:
        r = subprocess.run(['ffprobe','-v','error','-select_streams','v:0',
                            '-show_entries','stream=width,height,r_frame_rate,nb_frames',
                            '-of','csv=p=0', v], capture_output=True, text=True)
        print('%s : %s' % (label, r.stdout.strip()))

    print()
    print('=== 背景色与线条极性（首帧 (100,100) 取样 + 全帧均值） ===')
    for v, label in [(ref,'ref'), (ours,'ours')]:
        img = probe(v, 0.5, 100, 100)
        px = img[100,100]
        print('%s: bg RGB at (100,100) = %s' % (label, tuple(int(x) for x in px)))
    ri = probe(ref, 5.0, 0, 0)
    oi = probe(ours, 5.0, 0, 0)
    print('ref  frame mean RGB = %s' % (tuple(int(x) for x in ri.reshape(-1,3).mean(axis=0)),))
    print('ours frame mean RGB = %s' % (tuple(int(x) for x in oi.reshape(-1,3).mean(axis=0)),))
    lum = ri.mean(axis=2)
    y0, x0 = np.unravel_index(int(np.argmax(lum)), lum.shape)
    row = lum[y0, max(0,x0-8):x0+9].astype(int)
    half = (int(row.max()) + 20) / 2
    print('ref  最亮像素 (%d,%d) RGB=%s；横切灰度=%s' % (x0, y0, tuple(int(v) for v in ri[y0,x0]), list(row)))
    print('ref  该处线宽：核心(>200)=%dpx，FWHM(>%.0f)=%dpx（含辉光）' %
          (int((row > 200).sum()), half, int((row > half).sum())))
    print('ours 线宽（t=5.0 x=660 列扫，暗游程）: %s' % line_runs(oi, 660, 'col', 100))

    print()
    print('=== 运动统计（480x270 灰度，全 300 帧） ===')
    a_ref = frames_gray(ref)
    a_our = frames_gray(ours)
    stats(a_ref, 'ref 02-line-art.mp4')
    stats(a_our, 'ours out.mp4')

if __name__ == '__main__':
    main()
