"""On-demand TI feed trigger server — listens on port 9002.

Backend calls:
  POST   /trigger/{feed_name}  → run feed in background thread (200 immediately)
  DELETE /cancel/{feed_name}   → request cancellation of a running feed
  GET    /lookup/ip/{ip}       → synchronous MaxMind + IPInfo enrichment via MMDB/API
"""

import json
import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from feeds.base import clear_cancelled, set_cancelled

logger = logging.getLogger("ti-trigger")

# Populated by scheduler.py before start() is called
_FEED_MAP: dict[str, callable] = {}

# Track which feeds are currently running
_running: dict[str, bool] = {}
_lock = threading.Lock()


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

        with _lock:
            if _running.get(feed_name):
                self._respond(409, b'{"status":"already_running"}')
                return

        threading.Thread(target=self._run, args=(feed_name, fn), daemon=True).start()
        self._respond(200, b'{"status":"triggered"}')

    def do_DELETE(self):
        if not self.path.startswith("/cancel/"):
            self._respond(404, b"Not found")
            return

        feed_name = self.path[len("/cancel/"):]
        with _lock:
            was_running = _running.get(feed_name, False)

        if not was_running:
            self._respond(404, f"Feed {feed_name} is not running".encode())
            return

        set_cancelled(feed_name)
        logger.info("Cancellation requested for TI feed: %s", feed_name)
        self._respond(200, f'{{"status":"cancel_requested","feed":"{feed_name}"}}'.encode())

    def _run(self, name: str, fn) -> None:
        clear_cancelled(name)
        with _lock:
            _running[name] = True
        logger.info("Triggered TI feed: %s", name)
        try:
            fn()
        except Exception as exc:
            logger.error("Triggered TI feed %s failed: %s", name, exc, exc_info=True)
        finally:
            with _lock:
                _running[name] = False
            clear_cancelled(name)

    def _respond(self, code: int, body: bytes) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if not self.path.startswith("/lookup/ip/"):
            self._respond(404, b'{"error":"not found"}')
            return
        ip = self.path[len("/lookup/ip/"):]
        if not ip:
            self._respond(400, b'{"error":"ip required"}')
            return
        try:
            from feeds import ipinfo, maxmind
            mm_data  = maxmind.enrich_batch([ip]).get(ip)
            ipi_data = ipinfo.enrich_batch([ip]).get(ip)
            self._respond(200, json.dumps({"maxmind": mm_data, "ipinfo": ipi_data}).encode())
        except Exception as exc:
            logger.error("IP geo lookup failed for %s: %s", ip, exc)
            self._respond(500, json.dumps({"error": str(exc)}).encode())

    def log_message(self, fmt, *args):
        logger.debug("HTTP %s", fmt % args)


def register(feed_name: str, fn) -> None:
    _FEED_MAP[feed_name] = fn


def start(port: int = 9002) -> None:
    server = HTTPServer(("0.0.0.0", port), _Handler)
    t = threading.Thread(target=server.serve_forever, name="ti-trigger-server", daemon=True)
    t.start()
    logger.info("TI trigger server listening on port %d (feeds: %s)", port, list(_FEED_MAP))
