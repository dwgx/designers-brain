# Playable gallery

From the package root run `python tools/serve_gallery.py`, then open the printed local URL. A default `python -m http.server` does not guarantee the Range behavior used by the strict browser audit. On deployment, require `Accept-Ranges: bytes`, valid `206 Content-Range` responses, and `video/mp4` MIME type. Contact sheets are regenerated from each pinned MP4 at decoded frame indices 0, 120, 233 and 299.
