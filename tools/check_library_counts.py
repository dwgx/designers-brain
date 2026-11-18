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
2  structural error (missing file/directory, malformed data, or missing/ambiguous declaration)
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
RIGHTS_SCOPE = (
    "Artwork-level manifest labels and file-level attribution states are separate classifications. "
    "A false attribution flag is a recognized PD/CC0 label with no stated attribution condition; "
    "a jurisdiction-dependent null remains conditional. This recount is not a global legal judgment."
)

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

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

# Strip Markdown bold before matching. Each capture remains attached to its
# semantic declaration; a coincidental number elsewhere cannot satisfy it.
NUMBER = r"(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)"
# Do not salvage the integer tail of a signed/decimal/ASCII numeric token;
# CJK unit/label characters may directly touch a valid count in Japanese.
COUNT = rf"(?<![\dA-Za-z_.,+\-\u2212])({NUMBER})(?![\dA-Za-z_.,])"
README_PATTERNS = {
    "README.md": {
        "dossiers": rf"{COUNT} painter dossiers",
        "modules": rf"{COUNT} composable module cards",
        "mg_cards": rf"{COUNT} motion-graphics style cards",
        "citations": rf"{COUNT} source-linked quotations",
        "images": rf"{COUNT} distributed JPGs",
        "license_pd_cc0": rf"The historical {COUNT}/{NUMBER} split counts artwork-level manifest labels",
        "license_open": rf"The historical {NUMBER}/{COUNT} split counts artwork-level manifest labels",
        "rights_attribution_required": rf"File-level reuse classification:\s*{COUNT} attribution-required",
        "rights_pd_cc0_no_stated_attribution": rf"{COUNT} recognized PD/CC0 labels with no stated attribution condition",
        "rights_jurisdiction_dependent": rf"{COUNT} jurisdiction-dependent case",
        "license_section_attribution_required": rf"{COUNT} files require attribution",
        "license_section_pd_cc0_no_stated_attribution": rf"{COUNT} carry recognized PD/CC0 labels with no stated attribution condition",
    },
    "README.zh-CN.md": {
        "dossiers": rf"{COUNT} 份画家档案",
        "modules": rf"{COUNT} 张可组合模块卡",
        "mg_cards": rf"{COUNT} 张动态图形风格卡",
        "citations": rf"{COUNT} 条带来源引文",
        "images": rf"{COUNT} 个分发 JPG 文件",
        "license_pd_cc0": rf"历史 {COUNT}/{NUMBER} 是作品层 manifest 标签计数",
        "license_open": rf"历史 {NUMBER}/{COUNT} 是作品层 manifest 标签计数",
        "rights_attribution_required": rf"文件级保守分类为：\s*{COUNT} 件需署名",
        "rights_pd_cc0_no_stated_attribution": rf"{COUNT} 件为未列署名条件的已识别 PD/CC0 标签",
        "rights_jurisdiction_dependent": rf"{COUNT} 件取决于司法辖区",
        "license_section_attribution_required": rf"{COUNT} 件需署名；",
        "license_section_pd_cc0_no_stated_attribution": rf"{COUNT} 件带已识别 PD/CC0 标签且未列署名条件",
    },
    "README.ja.md": {
        "dossiers": rf"画家ドシエ\s*{COUNT}\s*件",
        "modules": rf"合成可能なモジュールカード\s*{COUNT}\s*枚",
        "mg_cards": rf"モーショングラフィックスのスタイルカード\s*{COUNT}\s*枚",
        "citations": rf"出典付き引用\s*{COUNT}\s*件",
        "images": rf"配布JPG\s*{COUNT}\s*点",
        "license_pd_cc0": rf"従来の{COUNT}/{NUMBER}は作品レベルのラベル集計",
        "license_open": rf"従来の{NUMBER}/{COUNT}は作品レベルのラベル集計",
        "rights_attribution_required": rf"ファイル単位の保守的分類は、帰属表示必須{COUNT}点",
        "rights_pd_cc0_no_stated_attribution": rf"帰属条件が記載されていない既知のPD/CC0ラベル{COUNT}点",
        "rights_jurisdiction_dependent": rf"法域によって条件が異なる{COUNT}点",
        "license_section_attribution_required": rf"では{COUNT}点が帰属表示必須",
        "license_section_pd_cc0_no_stated_attribution": rf"{COUNT}点が帰属条件の記載のない既知のPD/CC0ラベル",
    },
}

DECLARATION_MEASURES = {
    "license_section_attribution_required": "rights_attribution_required",
    "license_section_pd_cc0_no_stated_attribution": "rights_pd_cc0_no_stated_attribution",
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
    """Artwork-level PD / CC0 / OPEN labels; not file-level reuse permission."""
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


def count_file_rights(root: Path) -> tuple[dict[str, int], set[str]]:
    """Recount actual file rows, not the JSON summary or worldwide legal status."""
    p = root / PAINTERS / "dossiers" / "_images" / "rights-file-level.json"
    if not p.is_file():
        die(f"missing {p}")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        die(f"rights-file-level.json: malformed JSON ({exc})")
    if not isinstance(data, dict) or not isinstance(data.get("files"), list):
        die("rights-file-level.json: missing files array")
    counts = {
        "rights_attribution_required": 0,
        "rights_pd_cc0_no_stated_attribution": 0,
        "rights_jurisdiction_dependent": 0,
        "rights_unknown": 0,
        "rights_rows_total": 0,
    }
    paths: set[str] = set()
    for index, row in enumerate(data["files"]):
        if not isinstance(row, dict) or not isinstance(row.get("path"), str) or not row["path"]:
            die(f"rights-file-level.json: files[{index}] has no valid path")
        if row["path"] in paths:
            die(f"rights-file-level.json: duplicate path {row['path']!r}")
        paths.add(row["path"])
        if "requires_attribution" not in row:
            die(f"rights-file-level.json: {row['path']}: missing requires_attribution")
        state = row["requires_attribution"]
        if state is True:
            key = "rights_attribution_required"
        elif state is False:
            key = "rights_pd_cc0_no_stated_attribution"
        elif state is None:
            key = "rights_jurisdiction_dependent" if row.get("attribution_state") == "jurisdiction_dependent" else "rights_unknown"
        else:
            die(f"rights-file-level.json: {row['path']}: requires_attribution must be true/false/null")
        counts[key] += 1
        counts["rights_rows_total"] += 1
    return counts, paths


def parse_readme(root: Path, name: str) -> dict[str, int]:
    p = root / name
    if not p.is_file():
        die(f"missing {p}")
    text = p.read_text(encoding="utf-8").replace("**", "")
    out: dict[str, int] = {}
    for key, pattern in README_PATTERNS[name].items():
        matches = re.findall(pattern, text)
        if len(matches) != 1:
            die(f"{name}: declaration missing or ambiguous for {key!r} (matches={len(matches)})")
        out[key] = int(matches[0].replace(",", ""))
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
    measured["license_pd_cc0"] = measured["license_pd"] + measured["license_cc0"]
    measured["license_open"] = license_counts.get("OPEN", 0)
    measured["license_total"] = sum(license_counts.values())
    rights_counts, rights_paths = count_file_rights(root)
    measured.update(rights_counts)
    image_root = root / PAINTERS / "dossiers" / "_images"
    image_paths = {
        p.relative_to(image_root).as_posix()
        for p in image_root.rglob("*")
        if p.is_file() and p.suffix.lower() in IMAGE_EXTS
    }

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

    for name, declarations in declared.items():
        for field, expected in declarations.items():
            key = DECLARATION_MEASURES.get(field, field)
            add(field, measured[key], expected, name, key)
    add("license rows total", measured["license_total"], measured["images"], "manifest vs files")
    add("manifest rows", len(licenses), measured["images"], "manifest vs files")
    add("rights rows total", measured["rights_rows_total"], measured["images"], "file-level rights vs files")
    add("rights path differences", len(rights_paths ^ image_paths), 0, "file-level rights vs files")
    add("rights_unknown", measured["rights_unknown"], 0, "README three-state classification coverage")

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
        "rights_scope": RIGHTS_SCOPE,
        "ignore": ignore,
        "pass": not failed,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("== Designers_Brain public-count audit (read-only) ==")
        print(f"root: {root}")
        print()
        print(f"{'source:field':70} {'measured':>9} {'declared':>9} {'baseline':>9}  verdict")
        for c in checks:
            item = f"{c['source']}:{c['item']}"
            base = c.get("baseline")
            base_s = str(base) if base is not None else "-"
            verdict = "OK" if c["ok"] else "DRIFT"
            print(f"{item:70} {c['measured']:>9} {c['declared']:>9} {base_s:>9}  {verdict}")
        print()
        print(
            "artwork-level manifest label split: "
            f"PD {measured['license_pd']} / CC0 {measured['license_cc0']} / open {measured['license_open']} "
            f"(audit baseline {BASELINE['license_pd']}/{BASELINE['license_cc0']}/{BASELINE['license_open']})"
        )
        print(
            "file-level attribution states: "
            f"required {measured['rights_attribution_required']} / "
            f"recognized PD/CC0 label without stated attribution {measured['rights_pd_cc0_no_stated_attribution']} / "
            f"jurisdiction-dependent {measured['rights_jurisdiction_dependent']} / unknown {measured['rights_unknown']}"
        )
        print(RIGHTS_SCOPE)
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
