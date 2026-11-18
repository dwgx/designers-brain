#!/usr/bin/env python3
"""Check per-file image-rights classification against the historical central manifest.

Single source of truth for the project's CONSERVATIVE file-level classification
convention. It reads rights-file-level.json, re-derives every row column-indexed
from the read-only central manifest.md, and FAILS (nonzero) on:

  * count drift: JSON rows / manifest rows / disk JPGs != EXPECTED (default 739);
  * path/license/requires_attribution drift vs the re-derived manifest value;
  * any row classified requires_attribution=false whose manifest license column
    contains CC BY / CC BY-SA / ColBase / NPM-OpenGov / explicit 署名 flag /
    unwaived named-photographer credit, without a documented PD-Art exception.

Convention (NOT a global legal judgment; see the JSON header):
  * Composite JPG that is a modern photo/scan under CC BY/CC BY-SA =>
    requires_attribution=TRUE at file level even if the artwork is PD
    (e.g. qi_baishi/morning_glory_1950.jpg: PD-China painting + CC BY 2.0 photo
    by Jean-Pierre Dalbera).
  * A faithful PD-Art reproduction with a stated digital-file CC license and
    a jurisdiction-dependent exception remains conditional (null) when no
    applicable jurisdiction is selected (e.g. klimt/the_kiss.jpg).
  * CC0 / Public-Domain-Mark / plain PD rows that merely name a photographer are
    NOT attribution-bearing (CC0 waives; PD-Art faithful copies carry no condition).
  * Unknown file terms remain null. A PD-Art exception with unspecified
    jurisdiction is conditional (null), not a blanket no-attribution claim.

Paths resolve relative to this script, so it works from any cwd and in a
relocated/clean checkout. No absolute private locators are embedded.

Usage:
  python tools/check_image_rights.py
  python tools/check_image_rights.py --json TEMP.json --manifest MANIFEST.md \
      --images-dir IMAGES_DIR --expect-rows 739 --skip-disk-check
Negative controls:
  * inject a composite row (PD painting + CC BY photo, requires_attribution=false)
    into a temp JSON copy -> must FAIL with attribute/FALSE-NEGATIVE drift;
  * tamper --expect-rows (or add/remove a JSON row) -> must FAIL with count drift.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_EXPECTED = 739
MORNING_GLORY = "qi_baishi/morning_glory_1950.jpg"
KLIMT_KISS = "klimt/the_kiss.jpg"

SCRIPT_DIR = Path(__file__).resolve().parent
CANDIDATE = SCRIPT_DIR.parent
IMAGES_DIR = CANDIDATE / "knowledge" / "domains" / "painters" / "dossiers" / "_images"
DEFAULT_MANIFEST = IMAGES_DIR / "manifest.md"
DEFAULT_JSON = IMAGES_DIR / "rights-file-level.json"

ATTRIBUTION_PATTERNS = [
    ("CC BY-SA", r"cc\s*by\s*-\s*sa"),
    ("CC BY", r"cc\s*by(?!\s*-\s*sa)"),
    ("ColBase", r"colbase|利用規約|出典\s*[：:]\s*colbase"),
    ("NPM-OpenGov", r"政府資料開放|國立故宮|国立故宫|相容\s*cc\s*by|開放資料"),
    ("explicit-attribution-flag", r"署名要求\s*=\s*是|署名\s*[：:]"),
    ("named-photographer-credit",
     r"摄影|拍攝|翻拍|照片|uploader|上传者|photograph(?:ed)?\s+by"),
]
STRONG = {"CC BY-SA", "CC BY", "ColBase", "NPM-OpenGov", "explicit-attribution-flag"}
PD_ART_MARKERS = ("pd-art", "pd-art-100", "pd_art")
UPLOADER_ADDED_MARKERS = ("上传者附加", "上傳者附加", "uploader-added")


def detect_attribution_tokens(license_str: str) -> list[str]:
    low = (license_str or "").lower()
    return [label for label, pattern in ATTRIBUTION_PATTERNS if re.search(pattern, low)]


def _is_waived(license_str: str) -> bool:
    low = (license_str or "").lower()
    return ("cc0" in low or "public domain mark" in low or "public domain" in low
            or re.search(r"\bpd\b|pd-", low) is not None)


def is_pd_art_uploader_exception(license_str: str) -> bool:
    low = (license_str or "").lower()
    return (any(m in low for m in PD_ART_MARKERS)
            and any(m in low for m in UPLOADER_ADDED_MARKERS))


def classify(license_str: str) -> tuple[bool | None, str]:
    """Derive (True, False or None, reason) from historical manifest terms.

    None preserves either unknown terms or a jurisdiction-dependent condition;
    it must never be displayed as permission-free or attribution-free.
    """
    tokens = set(detect_attribution_tokens(license_str))
    if is_pd_art_uploader_exception(license_str):
        # The source states a digital-file license and a jurisdiction-dependent
        # PD-Art exception. An unspecified jurisdiction cannot yield blanket false.
        return None, "jurisdiction_dependent_pd_art"
    if tokens & STRONG:
        return True, "attribution_license_family:" + "+".join(sorted(tokens & STRONG))
    low = (license_str or "").lower()
    if re.search(r"unknown|unverified|unspecified|pending|待核|未核|不明|未知", low):
        return None, "unverified_file_terms"
    if not tokens:
        if _is_waived(license_str):
            return False, "recognized_pd_or_cc0_no_attribution_token"
        return None, "unrecognized_file_terms"
    if ("named-photographer-credit" in tokens
            and re.search(r"painting|artwork|原作|画作", low)
            and "cc0" not in low):
        return None, "artwork_pd_does_not_resolve_photo_terms"
    if "named-photographer-credit" in tokens and not _is_waived(license_str):
        return True, "named_credit_unwaived"
    return False, "waived_copy_with_photographer_credit"


def parse_manifest(path: Path) -> list[dict]:
    """Parse 总表 data rows, column-indexed. Data row col0 = `artist/file.jpg`."""
    rows = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        m = re.fullmatch(r"`([^`]+\.jpg)`", cells[0])
        if not m:
            continue
        rows.append({
            "line": lineno, "path": m.group(1),
            "artwork": cells[1], "artist": cells[2], "year": cells[3],
            "museum": cells[4], "source_url": cells[5], "license": cells[6],
        })
    return rows


def disk_jpgs(images_dir: Path) -> list[str]:
    return [str(p.relative_to(images_dir)).replace("\\", "/")
            for p in images_dir.rglob("*")
            if p.is_file() and p.suffix.lower() == ".jpg"]


def run_checks(json_path: Path, manifest_path: Path, images_dir: Path,
               expected: int, skip_disk: bool) -> tuple[int, list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []
    if not json_path.exists():
        return 2, [f"JSON file not found: {json_path}"], notes
    if not manifest_path.exists():
        return 2, [f"manifest not found: {manifest_path}"], notes

    data = json.loads(json_path.read_text(encoding="utf-8"))
    files = data.get("files")
    if not isinstance(files, list):
        return 2, ["JSON has no 'files' array"], notes

    mrows = parse_manifest(manifest_path)
    mby_path = {r["path"]: r for r in mrows}
    jby_path = {r.get("path"): r for r in files}

    # A/B. count drift
    if len(files) != expected:
        errors.append(f"JSON row count {len(files)} != expected {expected}")
    if len(mrows) != expected:
        errors.append(f"manifest row count {len(mrows)} != expected {expected}")
    djpgs = []
    if skip_disk:
        notes.append("disk JPG check SKIPPED (--skip-disk-check)")
    else:
        djpgs = disk_jpgs(images_dir)
        if len(djpgs) != expected:
            errors.append(f"disk JPG count {len(djpgs)} != expected {expected}")

    # C. header counts agree with arrays
    counts = data.get("counts") or {}
    for key, actual in (("files_total", len(files)), ("manifest_rows", len(mrows))):
        if key in counts and counts[key] != actual:
            errors.append(f"header counts.{key}={counts[key]} != actual {actual}")
    if not skip_disk and "disk_jpgs" in counts and counts["disk_jpgs"] != len(djpgs):
        errors.append(f"header counts.disk_jpgs={counts['disk_jpgs']} != actual {len(djpgs)}")

    # D. path set equality (missing / extra / duplicate)
    if len(jby_path) != len(files):
        errors.append(f"duplicate paths in JSON: {len(files)} rows, {len(jby_path)} unique")
    missing = sorted(set(mby_path) - set(jby_path))
    extra = sorted(set(jby_path) - set(mby_path))
    if missing:
        errors.append(f"{len(missing)} manifest paths missing from JSON, e.g. {missing[:3]}")
    if extra:
        errors.append(f"{len(extra)} JSON paths not in manifest, e.g. {extra[:3]}")

    if len(mby_path) != len(mrows):
        errors.append(f"duplicate paths in manifest: {len(mrows)} rows, {len(mby_path)} unique")
    if not skip_disk:
        missing_disk = sorted(set(mby_path) - set(djpgs))
        extra_disk = sorted(set(djpgs) - set(mby_path))
        if missing_disk:
            errors.append(f"manifest paths missing on disk: {missing_disk[:5]}")
        if extra_disk:
            errors.append(f"disk JPGs absent from manifest: {extra_disk[:5]}")

    # E/F/G. per-row license + attribute re-derivation and false-negative scan
    attr_rows = []
    state_counts = {"requires_attribution_true": 0, "requires_attribution_false": 0,
                    "requires_attribution_conditional": 0, "requires_attribution_unknown": 0}
    for path, row in jby_path.items():
        mrow = mby_path.get(path)
        if mrow is None:
            continue
        if row.get("license") != mrow["license"]:
            errors.append(f"license drift {path}: JSON={row.get('license')!r} "
                          f"manifest={mrow['license']!r}")
        expected_attr, reason = classify(mrow["license"])
        state_key = ("requires_attribution_true" if expected_attr is True else
                     "requires_attribution_false" if expected_attr is False else
                     "requires_attribution_conditional" if reason == "jurisdiction_dependent_pd_art"
                     else "requires_attribution_unknown")
        state_counts[state_key] += 1
        if "requires_attribution" not in row or row.get("requires_attribution") is not expected_attr:
            errors.append(f"attribute drift {path}: JSON requires_attribution="
                          f"{row.get('requires_attribution')!r} but license re-derives "
                          f"{expected_attr} (reason={reason}; license={mrow['license']!r})")
        if expected_attr:
            attr_rows.append(path)
        if row.get("requires_attribution") is False:
            toks = set(detect_attribution_tokens(row.get("license", "")))
            if (toks & STRONG) and not is_pd_art_uploader_exception(row.get("license", "")):
                errors.append(f"FALSE-NEGATIVE {path}: requires_attribution=false but license "
                              f"contains {sorted(toks & STRONG)}: {row.get('license')!r}")

    for key, actual in state_counts.items():
        if key in counts and counts[key] != actual:
            errors.append(f"header counts.{key}={counts[key]} != re-derived {actual}")
        elif actual and key not in counts:
            errors.append(f"missing nonzero header counts.{key} (re-derived {actual})")

    # H. adjudicated cases
    mg = jby_path.get(MORNING_GLORY)
    if mg is None:
        errors.append(f"missing required counterexample row {MORNING_GLORY}")
    else:
        if mg.get("requires_attribution") is not True:
            errors.append(f"{MORNING_GLORY} must be requires_attribution=true")
        if "Dalb" not in str(mg.get("notes", "")) + str(mg.get("license", "")):
            errors.append(f"{MORNING_GLORY} must record photographer credit (Dalbera)")
        if "CC BY 2.0" not in str(mg.get("license", "")):
            errors.append(f"{MORNING_GLORY} license column must show CC BY 2.0")
    kk = jby_path.get(KLIMT_KISS)
    if kk is None:
        errors.append(f"missing required PD-Art case row {KLIMT_KISS}")
    else:
        exc = kk.get("attribution_exception")
        if not isinstance(exc, dict) or exc.get("type") != "pd_art_faithful_reproduction":
            errors.append(f"{KLIMT_KISS} must carry documented pd_art_faithful_reproduction exception")

    notes.append(f"manifest rows={len(mrows)}; json rows={len(files)}; "
                 f"disk jpgs={len(djpgs) if not skip_disk else 'skipped'}; expected={expected}")
    notes.append(f"requires_attribution=true rows (re-derived)={len(attr_rows)}")
    notes.append(f"attribution-bearing paths={attr_rows}")
    return (1 if errors else 0), errors, notes


def main(argv: list[str] | None = None) -> int:
    # Preserve diagnostic errors on Windows redirected consoles (default cp1252).
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Check file-level image rights classification.")
    ap.add_argument("--json", type=Path, default=DEFAULT_JSON)
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--images-dir", type=Path, default=IMAGES_DIR)
    ap.add_argument("--expect-rows", type=int, default=DEFAULT_EXPECTED)
    ap.add_argument("--skip-disk-check", action="store_true")
    args = ap.parse_args(argv)

    code, errors, notes = run_checks(args.json, args.manifest, args.images_dir,
                                     args.expect_rows, args.skip_disk_check)
    for note in notes:
        print("NOTE:", note)
    for err in errors:
        print("ERROR:", err)
    if code == 0:
        print("RESULT: OK — rights-file-level.json consistent with manifest; no unexpected rows.")
    else:
        print(f"RESULT: FAIL — {len(errors)} problem(s) listed above.")
    return code


if __name__ == "__main__":
    sys.exit(main())
