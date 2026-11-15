#!/usr/bin/env python3
"""Read-only recount of Designers_Brain's public numbers.

Why this exists
---------------
Recompute every public count with the same denominators as the library audit
and compare the result with the declarations in README.md / README.zh-CN.md /
README.ja.md.  Pure checking logic only; contains no private prompt/session
content.  (The original private working copy lives in the archived
_agent-history/ directory and is left untouched.)

It also reports whether `_agent-history/` is covered by .gitignore.  That is
a warning only; use --strict-ignore to make an uncovered directory a non-zero
exit.

Exit codes
----------
0  every measured count matches the README declaration
1  at least one count drifted from its declaration
2  structural error (missing file or directory)
3  --strict-ignore and `_agent-history/` is not ignored

Usage
-----
    python tools/check_library_counts.py
    python tools/check_library_counts.py --json
    python tools/check_library_counts.py --strict-ignore
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

PAINTERS = Path("knowledge/domains/painters")
MOTION = Path("knowledge/domains/motion-graphics")
META_DOSSIERS = {"_index.md", "_review.md", "_crosscheck.md", "expansion.md"}
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

# Audit baseline, ops/AUDIT-2026-10-26.md section 1.  Reference only: the
# pass/fail comparison is measured-vs-README, so a deliberate update of both
# does not fail the script.
BASELINE = {
    "dossiers": 76,
    "modules": 76,
    "citations": 2044,
    "images": 735,
    "mg_cards": 15,
    "license_pd": 568,
    "license_cc0": 129,
    "license_open": 38,
}

README_PATTERNS = {
    "README.md": {
        "dossiers": r"\*\*(\d+) painter dossiers\*\*",
        "modules": r"\*\*(\d+) composable module cards\*\*",
        "mg_cards": r"\*\*(\d+) motion-graphics style cards\*\*",
        "citations": r"(\d+) sourced quotes",
        "images": r"(\d+) sourced artworks",
        "license_pd_cc0": r"(\d+) public-domain/CC0 images",
        "license_open": r"(\d+) openly licensed images",
    },
    "README.zh-CN.md": {
        "dossiers": r"\*\*(\d+) 份画家档案\*\*",
        "modules": r"\*\*(\d+) 张可组合模块卡\*\*",
        "mg_cards": r"\*\*(\d+) 张动态图形风格卡\*\*",
        "citations": r"(\d+) 条带来源引文",
        "images": r"(\d+) 件来源图像",
        "license_pd_cc0": r"(\d+) 件公有领域 / CC0",
        "license_open": r"(\d+) 件开放许可",
    },
    "README.ja.md": {
        "dossiers": r"画家ドシエ（資料ファイル）(\d+) 件",
        "modules": r"モジュールカード (\d+) 枚",
        "mg_cards": r"スタイルカード (\d+) 枚",
        "citations": r"出典付き引用 (\d+) 件",
        "images": r"出典付き作品画像 (\d+) 点",
        "license_pd_cc0": r"パブリックドメイン / CC0 が (\d+) 点",
        "license_open": r"オープンライセンス画像 (\d+) 点",
    },
}


def die(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(2)


def count_dossiers(root: Path) -> int:
    d = root / PAINTERS / "dossiers"
    if not d.is_dir():
        die(f"missing {d}")
    return sum(1 for p in d.glob("*.md") if p.name not in META_DOSSIERS)


def count_modules(root: Path) -> int:
    d = root / PAINTERS / "modules"
    if not d.is_dir():
        die(f"missing {d}")
    return sum(1 for p in d.glob("*.md") if p.name != "README.md")


def count_citations(root: Path) -> tuple[int, int]:
    d = root / PAINTERS / "dossiers" / "_corpus"
    if not d.is_dir():
        die(f"missing {d}")
    total = files = 0
    for p in sorted(d.glob("*.md")):
        if p.name == "INDEX.md":
            continue
        files += 1
        with p.open(encoding="utf-8") as fh:
            total += sum(1 for line in fh if line.startswith("### "))
    return total, files


def count_images(root: Path) -> int:
    d = root / PAINTERS / "dossiers" / "_images"
    if not d.is_dir():
        die(f"missing {d}")
    return sum(1 for p in d.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS)


def count_mg_cards(root: Path) -> int:
    p = root / MOTION / "origin" / "提示词全文.md"
    if not p.is_file():
        die(f"missing {p}")
    text = p.read_text(encoding="utf-8")
    return len(re.findall(r"^## \d{2} / 15", text, re.MULTILINE))


def manifest_licenses(root: Path) -> list[str]:
    p = root / PAINTERS / "dossiers" / "_images" / "manifest.md"
    if not p.is_file():
        die(f"missing {p}")
    lines = p.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines) if line.strip() == "## 总表"), None)
    if start is None:
        die("manifest.md has no '## 总表' section")
    licenses: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7:
            licenses.append(cells[-1])
    return licenses


def classify_license(license_text: str) -> str:
    """PD / CC0 / OPEN, reproducing ops/AUDIT-2026-10-26.md section 3."""
    s = license_text.replace("*", "").replace("`", "").strip()
    if s.startswith("摄影"):
        s = s[2:].strip()
    first = s.split()[0].upper() if s.split() else ""
    if first.startswith("CC0"):
        return "CC0"
    if first.startswith("PD-") or first.startswith("PUBLIC") or first.startswith("{{PD"):
        return "PD"
    upper = s.upper()
    if "CC0" in upper:
        return "CC0"
    if "public domain" in s.lower() or "{{PD" in s:
        return "PD"
    return "OPEN"


def parse_readme(root: Path, name: str) -> dict[str, int]:
    p = root / name
    if not p.is_file():
        die(f"missing {p}")
    text = p.read_text(encoding="utf-8")
    out: dict[str, int] = {}
    for key, pattern in README_PATTERNS[name].items():
        m = re.search(pattern, text)
        if not m:
            die(f"{name}: declaration pattern not found for {key!r} ({pattern!r})")
        out[key] = int(m.group(1))
    return out


def git_ignore_state(root: Path) -> dict[str, object]:
    state: dict[str, object] = {"gitignore_has_entry": False, "check_ignore": "unknown", "untracked": 0}
    gitignore = root / ".gitignore"
    if gitignore.is_file():
        text = gitignore.read_text(encoding="utf-8")
        state["gitignore_has_entry"] = bool(re.search(r"(?m)^\s*/?_agent-history/?\s*$", text))
    try:
        cp = subprocess.run(
            ["git", "check-ignore", "-v", "_agent-history/HANDOFF.md"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        state["check_ignore"] = "ignored" if cp.returncode == 0 else ("not ignored" if cp.returncode == 1 else f"error rc={cp.returncode}")
        if cp.stdout.strip():
            state["check_ignore_rule"] = cp.stdout.strip()
        st = subprocess.run(
            ["git", "status", "--porcelain", "-uall"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        state["untracked"] = sum(1 for line in st.stdout.splitlines() if line.startswith("?? _agent-history/"))
    except FileNotFoundError:
        state["check_ignore"] = "git not found"
    return state


def main() -> int:
    ap = argparse.ArgumentParser(description="Read-only recount of Designers_Brain public numbers.")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent), help="project root")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--strict-ignore", action="store_true", help="exit 3 when _agent-history/ is not ignored")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        die(f"root not found: {root}")

    measured = {
        "dossiers": count_dossiers(root),
        "modules": count_modules(root),
        "mg_cards": count_mg_cards(root),
    }
    measured["citations"], corpus_files = count_citations(root)
    measured["images"] = count_images(root)

    licenses = manifest_licenses(root)
    license_counts = Counter(classify_license(x) for x in licenses)
    measured["license_pd"] = license_counts.get("PD", 0)
    measured["license_cc0"] = license_counts.get("CC0", 0)
    measured["license_open"] = license_counts.get("OPEN", 0)
    measured["license_total"] = sum(license_counts.values())

    declared = {name: parse_readme(root, name) for name in README_PATTERNS}

    checks: list[dict[str, object]] = []

    def add(item: str, value: int, expected: int, source: str, baseline_key: str | None = None) -> None:
        checks.append(
            {
                "item": item,
                "measured": value,
                "declared": expected,
                "source": source,
                "baseline": BASELINE.get(baseline_key) if baseline_key else None,
                "ok": value == expected,
            }
        )

    en = declared["README.md"]
    add("dossiers", measured["dossiers"], en["dossiers"], "README.md", "dossiers")
    add("module cards", measured["modules"], en["modules"], "README.md", "modules")
    add("citations", measured["citations"], en["citations"], "README.md", "citations")
    add("public images", measured["images"], en["images"], "README.md", "images")
    add("motion-graphics cards", measured["mg_cards"], en["mg_cards"], "README.md", "mg_cards")
    add("license PD+CC0", measured["license_pd"] + measured["license_cc0"], en["license_pd_cc0"], "README.md")
    add("license open", measured["license_open"], en["license_open"], "README.md", "license_open")
    add("license rows total", measured["license_total"], measured["images"], "manifest vs files")
    add("manifest rows", len(licenses), measured["images"], "manifest vs files")

    # zh/ja must at least carry the same headline numbers as the English README.
    for name in ("README.zh-CN.md", "README.ja.md"):
        text = (root / name).read_text(encoding="utf-8")
        for key in ("dossiers", "modules", "mg_cards", "citations", "images"):
            token = str(measured[key])
            found = re.search(rf"(?<!\d){re.escape(token)}(?!\d)", text) is not None
            checks.append({"item": f"{name}:{key}", "measured": measured[key], "declared": measured[key], "source": name, "ok": found})

    ignore = git_ignore_state(root)
    ignore_ok = bool(ignore["gitignore_has_entry"]) or ignore["check_ignore"] == "ignored"

    failed = [c for c in checks if not c["ok"]]
    result = {
        "root": str(root),
        "measured": measured,
        "baseline": BASELINE,
        "declared": declared,
        "checks": checks,
        "corpus_files": corpus_files,
        "ignore": ignore,
        "pass": not failed,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("== Designers_Brain public-count audit (read-only) ==")
        print(f"root: {root}")
        print()
        print(f"{'item':28} {'measured':>9} {'declared':>9} {'baseline':>9}  verdict")
        for c in checks:
            item = str(c["item"])
            if item.startswith("README."):
                verdict = "OK" if c["ok"] else "MISSING NUMBER"
                print(f"{item:28} {c['measured']:>9} {'-':>9} {'-':>9}  {verdict}")
                continue
            base = c.get("baseline")
            base_s = str(base) if base is not None else "-"
            verdict = "OK" if c["ok"] else "DRIFT"
            print(f"{item:28} {c['measured']:>9} {c['declared']:>9} {base_s:>9}  {verdict}")
        print()
        print(
            "license split: "
            f"PD {measured['license_pd']} / CC0 {measured['license_cc0']} / open {measured['license_open']} "
            f"(audit baseline {BASELINE['license_pd']}/{BASELINE['license_cc0']}/{BASELINE['license_open']})"
        )
        print("git hygiene (warning-only)")
        print(f"  .gitignore has _agent-history/: {ignore['gitignore_has_entry']}")
        print(f"  git check-ignore: {ignore['check_ignore']}")
        print(f"  untracked entries under _agent-history/: {ignore['untracked']}")
        if not ignore_ok:
            print("  RISK: `git add -A` would stage the private _agent-history/ directory.")
            print("  fix: add `_agent-history/` to .gitignore.")
        print()
        print(f"RESULT: {'PASS' if not failed else 'FAIL'} ({len(checks) - len(failed)}/{len(checks)} checks match; ignore {'ok' if ignore_ok else 'RISK'})")

    if failed:
        return 1
    if args.strict_ignore and not ignore_ok:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
