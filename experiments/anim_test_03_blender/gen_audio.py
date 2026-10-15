"""gen_audio.py — code-synthesized soundtrack for anim_test_03 (no samples, deterministic).
Reads checks/bake_stats.json contacts to lock hits to the picture.
Run: python gen_audio.py   (or blender -b --factory-startup -P gen_audio.py)
Out: audio/score.wav  (44100 Hz, 16-bit stereo, 10.000 s)
"""
import numpy as np, wave, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
SR = 44100
DUR = 10.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(7)

L = np.zeros(N); R = np.zeros(N)

def add(sig, t0, pan=0.0, gain=1.0):
    i0 = int(round(t0 * SR))
    n = min(len(sig), N - i0)
    if n <= 0 or i0 < 0:
        return
    gl = 0.5 * (1 - pan) * gain
    gr = 0.5 * (1 + pan) * gain
    L[i0:i0 + n] += sig[:n] * gl
    R[i0:i0 + n] += sig[:n] * gr

def decay_env(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))

def sine_sweep(f0, f1, dur, amp=1.0):
    n = int(dur * SR)
    f = np.linspace(f0, f1, n)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return amp * np.sin(ph)

def noise(n, seed=0):
    r = np.random.default_rng(seed)
    return r.standard_normal(n)

def lowpass(x, k):
    """simple moving-average lowpass (k samples)"""
    c = np.cumsum(np.concatenate([[0.0], x]))
    y = (c[k:] - c[:-k]) / k
    return np.concatenate([np.zeros(k - 1), y])[:len(x)]

# ---------------- read contacts for sync
contacts = []
try:
    stats = json.load(open(os.path.join(BASE, "checks", "bake_stats.json")))
    contacts = [(c[0] / 30.0, c[1]) for c in stats.get("contacts", [])]
except Exception as e:
    print("no bake_stats:", e)
if not contacts:
    contacts = [(3.30, 8.6), (4.10, 3.2), (4.70, 1.6)]
print("contacts for audio:", contacts)

# ---------------- 1. soft pad (whole track)
def pad():
    sig = np.zeros(N)
    for f, a in ((110.0, 0.030), (220.0, 0.022), (277.18, 0.018), (329.63, 0.016), (440.0, 0.010)):
        sig += a * np.sin(2 * np.pi * f * t + f * 0.01)
    trem = 0.85 + 0.15 * np.sin(2 * np.pi * 0.12 * t)
    sw = np.clip(t / 1.5, 0, 1) * np.clip((DUR - t) / 1.0, 0, 1)
    return sig * trem * sw

add(pad(), 0.0)

# ---------------- 2. sea noise (waves phase)
sea = lowpass(noise(N, 11), 2500)
sea /= (np.abs(sea).max() + 1e-9)
sea *= 0.055 * (0.65 + 0.35 * np.sin(2 * np.pi * 0.16 * t + 1.0)) * np.clip((2.6 - t) / 0.8, 0, 1) * np.clip(t / 1.0, 0, 1)
add(sea, 0.0)

# ---------------- 3. fall whoosh (2.55 -> first contact)
t_c1 = contacts[0][0]
wf = t_c1 - 0.85
n_w = int(0.9 * SR)
w = noise(n_w, 12)
w = lowpass(w, 300)
w /= (np.abs(w).max() + 1e-9)
env_w = (np.arange(n_w) / n_w) ** 2.2
whoosh = w * env_w * 0.28
swp = sine_sweep(560, 230, 0.9, 0.10) * env_w
add(whoosh + swp, wf, pan=0.0)

# ---------------- 4. impacts (thump + click + jelly boing) at contacts
def thump(t0, amp, f0=95, f1=48, dur=0.55):
    s = sine_sweep(f0, f1, dur, 1.0) * decay_env(int(dur * SR), 0.13) * amp
    n = int(dur * SR)
    click = noise(n, 21) * decay_env(n, 0.004) * amp * 0.5
    body = np.sin(2 * np.pi * 180 * np.arange(n) / SR) * decay_env(n, 0.07) * amp * 0.35
    return s + click + body

def boing(t0, amp):
    n = int(0.6 * SR)
    tt = np.arange(n) / SR
    f = 235 * (1 + 0.05 * np.sin(2 * np.pi * 12 * tt))
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * decay_env(n, 0.16) * amp

for i, (tc, v) in enumerate(contacts[:3]):
    amp = (0.55, 0.28, 0.16)[i]
    add(thump(tc, amp), tc, pan=0.0)
    add(boing(tc + 0.03, 0.10 * amp / 0.55), tc + 0.03, pan=0.05)

# ---------------- 5. marble scatter ticks (glass clicks)
tick_t0 = t_c1 + 0.02
tick_span = 1.9
n_t = 52
for i in range(n_t):
    u = i / (n_t - 1)
    tt = tick_t0 + tick_span * (u ** 0.72)
    amp = (0.14 * np.exp(-2.4 * u) + 0.02)
    n = int(0.05 * SR)
    tick = noise(n, 100 + i) * decay_env(n, 0.0035) * amp
    f = 1500 + 1900 * ((i * 0.37) % 1.0)
    tick += np.sin(2 * np.pi * f * np.arange(n) / SR) * decay_env(n, 0.012) * amp * 0.7
    pan = 0.55 * np.sin(i * 2.4)
    add(tick, tt, pan=pan)

# ---------------- 6. settle ticks
for i in range(8):
    tt = 5.7 + 1.5 * (i / 7.0) ** 0.8
    amp = 0.05 * (1 - i / 9.0)
    n = int(0.04 * SR)
    tick = noise(n, 300 + i) * decay_env(n, 0.004) * amp
    add(tick, tt, pan=0.4 * np.sin(i * 1.7))

# ---------------- 7. end chime
def chime(t0):
    sig = np.zeros(int(2.2 * SR))
    for f, a, d in ((523.25, 0.070, 1.8), (659.25, 0.050, 1.6), (783.99, 0.040, 1.5),
                    (1046.5, 0.026, 1.3), (1318.5, 0.014, 1.1)):
        n = int(d * SR)
        sig[:n] += a * np.sin(2 * np.pi * f * np.arange(n) / SR) * decay_env(n, d / 4)
    return sig
add(chime(8.35), 8.35, pan=0.0)

# ---------------- master: soft clip + fades + normalize
def softclip(x):
    return np.tanh(1.25 * x) / np.tanh(1.25)

mixL = softclip(L); mixR = softclip(R)
peak = max(np.abs(mixL).max(), np.abs(mixR).max())
g = 0.89 / (peak + 1e-9)
mixL *= g; mixR *= g
fade = np.ones(N)
fade[:int(0.15 * SR)] = np.linspace(0, 1, int(0.15 * SR))
fade[-int(0.25 * SR):] = np.linspace(1, 0, int(0.25 * SR))
mixL *= fade; mixR *= fade

out = np.stack([mixL, mixR], axis=1)
pcm = np.clip(out * 32767.0, -32768, 32767).astype(np.int16)

od = os.path.join(BASE, "audio")
os.makedirs(od, exist_ok=True)
p = os.path.join(od, "score.wav")
with wave.open(p, "wb") as wf_:
    wf_.setnchannels(2)
    wf_.setsampwidth(2)
    wf_.setframerate(SR)
    wf_.writeframes(pcm.tobytes())
print("WROTE", p, os.path.getsize(p), "bytes, peak", round(float(g * peak), 3))
