"""Path-independent Chrome discovery for the UI research fixtures.

No absolute local path is stored here. Resolution order:
  1. Environment override UI_CHROME (full path to a Chrome/Chromium executable).
  2. Executables on PATH (chrome, chrome.exe, google-chrome, chromium, ...).
  3. Per-platform standard install locations (Windows Program Files, Linux,
     macOS). These are *platform conventions*, not a captured machine path.

Raises FileNotFoundError with an actionable message if nothing is found.
This module is part of a research fixture, not a production launcher.
"""
from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def find_chrome() -> str:
    override = os.environ.get("UI_CHROME")
    if override:
        p = Path(override).expanduser()
        if p.is_file():
            return str(p)
        raise FileNotFoundError(
            "UI_CHROME is set but not a file: %s" % override)

    names = ("chrome", "chrome.exe", "google-chrome", "google-chrome-stable",
             "chromium", "chromium-browser", "chrome-headless-shell",
             "chrome-headless-shell.exe")
    for name in names:
        found = shutil.which(name)
        if found:
            return found

    candidates: list[Path] = []
    if sys.platform == "win32":
        for env in ("ProgramFiles", "ProgramFiles(x86)", "LOCALAPPDATA"):
            root = os.environ.get(env)
            if not root:
                continue
            candidates += [
                Path(root) / "Google" / "Chrome" / "Application" / "chrome.exe",
                Path(root) / "Chromium" / "Application" / "chrome.exe",
            ]
    elif sys.platform == "linux":
        candidates += [
            Path("/usr/bin/google-chrome"), Path("/usr/bin/chromium"),
            Path("/usr/bin/chromium-browser"),
        ]
    elif sys.platform == "darwin":
        candidates += [
            Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
        ]
    for p in candidates:
        if p.is_file():
            return str(p)

    raise FileNotFoundError(
        "Chrome/Chromium not found. Install Chrome or set UI_CHROME to the "
        "executable path (e.g. UI_CHROME=/path/to/chrome). No machine-specific "
        "path is embedded in this fixture.")
