"""METRIC-PILOT implemented metric families (F1 luminance histogram, F3 Laplacian variance).

Pure stdlib. These are the ONLY two families implemented in this lane; F2 (edge
chain) is `proposed` and F4 (direction families) is `manual-only` and therefore
have NO code here. See ../metric-spec.md for the full operational spec.

`implemented` means: a runnable numeric function + synthetic positive/negative
fixtures that pin the computation's meaning and its failure mode. It does NOT
mean the dossier thresholds were validated on real artwork or renders, and does
NOT confer aesthetic validity.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


class EmptyMaskError(ValueError):
    """Raised when a mask selects no usable samples. Treated as FAIL, never 0/skip."""


# ---- color pipeline: sRGB 8-bit (0-255) -> linear Y -> CIE L* in [0,100] ----
def srgb8_to_Lstar(v255):
    """One sRGB 8-bit code value (0-255, equal on R=G=B so gray) -> L* in [0,100]."""
    c = v255 / 255.0
    lin = c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return 116.0 * lin ** (1.0 / 3.0) - 16.0 if lin > 0.008856 else 903.3 * lin


def _validate_grid(L, mask):
    H = len(L)
    W = len(L[0]) if H else 0
    assert len(mask) == H, "mask height mismatch"
    for r in range(H):
        assert len(L[r]) == W and len(mask[r]) == W, "ragged grid/mask"
        for v in L[r]:
            assert 0.0 <= v <= 100.0, "L* out of [0,100]"
    return H, W


def _masked_values(L, mask):
    H, W = _validate_grid(L, mask)
    return [L[r][c] for r in range(H) for c in range(W) if mask[r][c]]


# ---- F1: luminance histogram ----
def lum_hist(L, mask, bins=10, lo=0.0, hi=100.0):
    """Equal-width L* histogram. Returns bin_counts, max_bin_share, and the two
    dossier-related shares. Empty mask -> EmptyMaskError (FAIL)."""
    vals = _masked_values(L, mask)
    N = len(vals)
    if N == 0:
        raise EmptyMaskError("F1 empty mask: no selected pixels -> FAIL (not 0, not skip)")
    width = (hi - lo) / bins
    counts = [0] * bins
    for v in vals:
        k = int((v - lo) / width)
        if k >= bins:
            k = bins - 1
        if k < 0:
            k = 0
        counts[k] += 1
    return {
        "N": N,
        "bin_counts": counts,
        "max_bin_share": max(counts) / N,
        "midtone_share": sum(1 for v in vals if 40.0 <= v <= 70.0) / N,
        "black_white_share": sum(1 for v in vals if v < 8.0 or v > 92.0) / N,
    }


# ---- F3: Laplacian variance ----
def lap_var(L, mask):
    """Population variance of 3x3 cross-kernel Laplacian responses over interior
    pixels whose 4-neighbours are all inside the mask. Boundary pixels excluded.
    Empty / no interior -> EmptyMaskError (FAIL)."""
    H, W = _validate_grid(L, mask)
    resp = []
    for r in range(1, H - 1):
        for c in range(1, W - 1):
            if not mask[r][c]:
                continue
            if not (mask[r - 1][c] and mask[r + 1][c] and mask[r][c - 1] and mask[r][c + 1]):
                continue
            resp.append(L[r - 1][c] + L[r + 1][c] + L[r][c - 1] + L[r][c + 1] - 4.0 * L[r][c])
    N = len(resp)
    if N == 0:
        raise EmptyMaskError("F3 empty mask / no interior -> FAIL (not 0, not skip)")
    mean = sum(resp) / N
    var = sum((x - mean) ** 2 for x in resp) / N
    return {"N": N, "responses": resp, "mean": mean, "variance": var}


def _mask(h, w, val=True):
    return [[val] * w for _ in range(h)]


def load_fixtures():
    return json.loads((HERE / "fixtures.json").read_text(encoding="utf-8"))
