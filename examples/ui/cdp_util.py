"""Small CDP transport shared only by these research-fixture checks.

Uses an owned temporary Chrome process/profile. Prefers websocket-client;
websockets.sync is a supported alternate when already installed. No downloads.
"""
from __future__ import annotations
import json
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path
from chrome_util import find_chrome


class ChromeSession:
    def __init__(self):
        self.tmp = None
        self.proc = None
        self.ws = None
        self.stderr = None
        self.mid = 0
        self.transport = None
        self.version = None

    def __enter__(self):
        try:
            self.tmp = tempfile.TemporaryDirectory(prefix="designers-brain-ui-", ignore_cleanup_errors=True)
            runtime = Path(self.tmp.name)
            profile = runtime / "profile"
            profile.mkdir()
            self.stderr = (runtime / "chrome.log").open("wb")
            self.proc = subprocess.Popen([
                find_chrome(), "--headless=new", "--remote-debugging-port=0",
                "--user-data-dir=" + str(profile), "--no-first-run",
                "--no-default-browser-check", "--disable-gpu", "--no-sandbox",
                "--hide-scrollbars", "--force-device-scale-factor=1", "about:blank",
            ], stdout=subprocess.DEVNULL, stderr=self.stderr)
            portfile = profile / "DevToolsActivePort"
            deadline = time.monotonic() + 20
            port = None
            while time.monotonic() < deadline:
                if self.proc.poll() is not None:
                    raise RuntimeError("owned Chrome exited before its DevTools handshake")
                if portfile.is_file():
                    try:
                        port = int(portfile.read_text().splitlines()[0])
                        break
                    except (ValueError, IndexError):
                        pass
                time.sleep(.1)
            if port is None:
                raise RuntimeError("owned Chrome did not write DevToolsActivePort")
            pages = []
            while time.monotonic() < deadline:
                try:
                    with urllib.request.urlopen("http://127.0.0.1:%d/json/list" % port, timeout=2) as response:
                        pages = [p for p in json.load(response) if p.get("type") == "page"]
                    if pages:
                        break
                except (OSError, ValueError):
                    pass
                time.sleep(.1)
            if not pages:
                raise RuntimeError("owned Chrome has no page target")
            try:
                import websocket
            except ImportError:
                try:
                    from websockets.sync.client import connect
                except ImportError as exc:
                    raise RuntimeError("install websocket-client (or websockets with sync support) in the chosen Python environment") from exc
                self.ws = connect(pages[0]["webSocketDebuggerUrl"], open_timeout=15, max_size=None)
                self.transport = "websockets.sync"
            else:
                self.ws = websocket.create_connection(pages[0]["webSocketDebuggerUrl"], timeout=15, suppress_origin=True)
                self.transport = "websocket-client"
            self.version = self.call("Browser.getVersion")
            self.call("Page.enable")
            self.call("Runtime.enable")
            return self
        except Exception:
            self.__exit__(None, None, None)
            raise

    def call(self, method, params=None):
        self.mid += 1
        wanted = self.mid
        self.ws.send(json.dumps({"id": wanted, "method": method, "params": params or {}}))
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            if self.transport == "websockets.sync":
                message = self.ws.recv(timeout=max(.1, deadline - time.monotonic()))
            else:
                message = self.ws.recv()
            packet = json.loads(message)
            if packet.get("id") == wanted:
                if "error" in packet:
                    raise RuntimeError("CDP %s: %s" % (method, packet["error"]))
                return packet.get("result", {})
        raise TimeoutError("CDP response timeout: " + method)

    def evaluate(self, expression):
        result = self.call("Runtime.evaluate", {"expression": expression, "returnByValue": True, "awaitPromise": True})
        if "exceptionDetails" in result:
            raise RuntimeError("fixture JavaScript exception: " + json.dumps(result["exceptionDetails"]))
        return result.get("result", {}).get("value")

    def navigate(self, fixture: Path, ready):
        self.evaluate("window.__dbPreviousDocument = true")
        result = self.call("Page.navigate", {"url": fixture.resolve().as_uri()})
        if result.get("errorText"):
            raise RuntimeError("fixture navigation failed: " + result["errorText"])
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if self.evaluate("!window.__dbPreviousDocument && document.readyState === 'complete' && (" + ready + ")"):
                self.evaluate("document.fonts.ready.then(() => true)")
                return
            time.sleep(.1)
        raise TimeoutError("fixture did not become ready")

    def key(self, key, code, virtual_key):
        params = {"key": key, "code": code, "windowsVirtualKeyCode": virtual_key,
                  "nativeVirtualKeyCode": virtual_key}
        self.call("Input.dispatchKeyEvent", dict(params, type="rawKeyDown"))
        self.call("Input.dispatchKeyEvent", dict(params, type="keyUp"))

    def __exit__(self, exc_type, exc_value, traceback):
        if self.ws is not None:
            try:
                self.ws.close()
            except Exception:
                pass
        if self.proc is not None and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                self.proc.wait(timeout=5)
        if self.stderr is not None:
            self.stderr.close()
        if self.tmp is not None:
            self.tmp.cleanup()
