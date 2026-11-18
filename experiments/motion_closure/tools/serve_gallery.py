#!/usr/bin/env python3
"""Serve this package on localhost with HTTP byte ranges for real MP4 seeking.

The single-range handling follows the actually exercised strict Chrome probe.
This small preview server is not a production server or a browser test.
"""
import argparse
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import mimetypes
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


class RangeHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def __init__(self, *args, root, **kwargs):
        self.root = Path(root).resolve()
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.serve(False)

    def do_GET(self):
        self.serve(True)

    def invalid_range(self, size):
        self.send_response(416)
        self.send_header('Content-Range', f'bytes */{size}')
        self.send_header('Content-Length', '0')
        self.end_headers()

    def serve(self, body):
        requested = unquote(urlsplit(self.path).path)
        if requested == '/':
            requested = '/gallery/index.html'
        path = (self.root / requested.lstrip('/')).resolve()
        if not path.is_relative_to(self.root) or not path.is_file():
            self.send_error(404); return
        size = path.stat().st_size
        start, end, status = 0, size - 1, 200
        header = self.headers.get('Range')
        if header:
            match = re.fullmatch(r'bytes=([0-9]*)-([0-9]*)', header)
            if not match or not (match[1] or match[2]):
                self.invalid_range(size); return
            if match[1]:
                start = int(match[1]); end = min(int(match[2]), size - 1) if match[2] else size - 1
            else:
                suffix = int(match[2])
                if suffix == 0:
                    self.invalid_range(size); return
                start = max(0, size - suffix)
            if start > end or start >= size:
                self.invalid_range(size); return
            status = 206
        self.send_response(status)
        mime = 'video/mp4' if path.suffix.lower() == '.mp4' else mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
        if mime.startswith('text/') or path.suffix in ('.json', '.py', '.js', '.mjs', '.md'):
            mime += '; charset=utf-8'
        self.send_header('Content-Type', mime)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(max(0, end - start + 1)))
        if status == 206:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        if body:
            try:
                with path.open('rb') as f:
                    f.seek(start); remaining = end - start + 1
                    while remaining > 0:
                        block = f.read(min(65536, remaining))
                        if not block:
                            break
                        self.wfile.write(block); remaining -= len(block)
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    handler = partial(RangeHandler, root=root)
    with ThreadingHTTPServer(('127.0.0.1', args.port), handler) as server:
        print(f'http://127.0.0.1:{server.server_address[1]}/gallery/index.html', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
