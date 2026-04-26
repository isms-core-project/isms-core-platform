"""On-demand TI feed trigger server — listens on port 9002.

Backend calls: POST /trigger/{feed_name}
Returns 200 immediately; runs the feed in a background thread.
"""

import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

logger = logging.getLogger("ti-trigger")

# Populated by scheduler.py before start() is called
_FEED_MAP: dict[str, callable] = {}


class _Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if not self.path.startswith("/trigger/"):
            self._respond(404, b"Not found")
            return

        feed_name = self.path[len("/trigger/"):]
        fn = _FEED_MAP.get(feed_name)
        if fn is None:
            self._respond(404, f"Unknown feed: {feed_name}".encode())
            return

        threading.Thread(target=self._run, args=(feed_name, fn), daemon=True).start()
        self._respond(200, b'{"status":"triggered"}')

    def _run(self, name: str, fn) -> None:
        logger.info("Triggered feed: %s", name)
        try:
            fn()
        except Exception as exc:
            logger.error("Triggered feed %s failed: %s", name, exc, exc_info=True)

    def _respond(self, code: int, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        logger.debug("HTTP %s", fmt % args)


def register(feed_name: str, fn) -> None:
    _FEED_MAP[feed_name] = fn


def start(port: int = 9002) -> None:
    server = HTTPServer(("0.0.0.0", port), _Handler)
    t = threading.Thread(target=server.serve_forever, name="ti-trigger-server", daemon=True)
    t.start()
    logger.info("TI trigger server listening on port %d (feeds: %s)", port, list(_FEED_MAP))
