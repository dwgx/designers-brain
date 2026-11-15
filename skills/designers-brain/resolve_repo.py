#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""designers-brain skill — portable REPO locator (G7-S2, 2026-11-16).

Implements the rule documented in SKILL.md §frontmatter:
    REPO = dirname(dirname(SKILL.md))   # SKILL.md lives at <repo>/skills/designers-brain/
No hardcoded machine paths; fails loudly if the skill is detached from the repo.

Usage:
    python resolve_repo.py            # print REPO + sanity checks
    python resolve_repo.py --json     # machine-readable
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # <repo>/skills/designers-brain
REPO = HERE.parent.parent                        # dirname(dirname(SKILL.md))


def resolve() -> Path:
    if HERE.name != "designers-brain" or HERE.parent.name != "skills":
        raise RuntimeError(
            f"SKILL locator broken: expected <repo>/skills/designers-brain/, got {HERE}"
        )
    for probe in ("knowledge/cross/conflicts.md", "skills/designers-brain/SKILL.md"):
        p = REPO / probe
        if not p.is_file():
            raise RuntimeError(
                f"REPO resolve failed: {p} missing — skill detached from its repo; "
                "refusing to fall back to any hardcoded path (SKILL.md §仓库根)."
            )
    return REPO


def main() -> int:
    try:
        repo = resolve()
    except RuntimeError as e:
        print(json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False))
        return 2
    probe = repo / "knowledge/cross/conflicts.md"
    sha = hashlib.sha256(probe.read_bytes()).hexdigest()
    out = {
        "ok": True,
        "skill_dir": str(HERE),
        "repo": str(repo),
        "probe": "knowledge/cross/conflicts.md",
        "probe_sha256": sha,
        "modules_dir_exists": (repo / "knowledge/domains/painters/modules").is_dir(),
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
