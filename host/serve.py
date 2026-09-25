"""Serve the PS4 jailbreak host with the correct MIME type for AppCache.

PS4 browser refuses to cache a manifest that is not served as
text/cache-manifest. Plain `python -m http.server` sends
.manifest/.appcache as text/plain, so the cache page loops on
"error" forever and nothing is stored offline.

Usage:  python serve.py [port, default 8000]
Then on PS4 open: http://<pc-ip>:8000/index.html
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".manifest": "text/cache-manifest",
        ".appcache": "text/cache-manifest",
    }


if __name__ == "__main__":
    with ThreadingHTTPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving {PORT}, manifests as text/cache-manifest")
        httpd.serve_forever()
