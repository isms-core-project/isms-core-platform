"""Feed trigger server — runs on port 8001 inside the feeds container.

The backend calls POST /trigger/{feed_name} to start a feed immediately
without restarting the container. Each feed runs in a background thread.
A 409 is returned if the feed is already running.

Endpoints:
  POST /trigger/nist_cve?mode=full   — NVD CVE full pull
  POST /trigger/nist_cve?mode=delta  — NVD CVE delta pull
  POST /trigger/mitre_attack         — MITRE ATT&CK
  POST /trigger/mitre_atlas          — MITRE ATLAS
  POST /trigger/cisa_kev             — CISA KEV
  POST /trigger/epss                 — FIRST EPSS
  POST /trigger/nist_cpe             — NVD CPE (Option B)
"""

import logging
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from feeds import cisa_kev, epss, mitre_atlas, mitre_attack, nist_cpe, nist_cve

logger = logging.getLogger(__name__)

_TRIGGERS: dict[str, callable] = {
    "nist_cve_full":  nist_cve.run_full,
    "nist_cve_delta": nist_cve.run_delta,
    "mitre_attack":   mitre_attack.run,
    "mitre_atlas":    mitre_atlas.run,
    "cisa_kev":       cisa_kev.run,
    "epss":           epss.run,
    "nist_cpe":       nist_cpe.run,
}

_running: dict[str, bool] = {}
_lock = threading.Lock()


def _run_in_thread(feed_name: str, fn) -> bool:
    with _lock:
        if _running.get(feed_name):
            return False
        _running[feed_name] = True

    def target():
        try:
            logger.info("Triggered feed: %s", feed_name)
            fn()
        except Exception as exc:
            logger.error("Triggered feed %s failed: %s", feed_name, exc, exc_info=True)
        finally:
            with _lock:
                _running[feed_name] = False

    threading.Thread(target=target, daemon=True).start()
    return True


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        logger.debug("trigger-server: " + format, *args)

    def do_POST(self):
        parsed = urlparse(self.path)
        parts = [p for p in parsed.path.strip("/").split("/") if p]

        if len(parts) < 2 or parts[0] != "trigger":
            self._send(404, "Not found")
            return

        feed_name = parts[1]
        if feed_name == "nist_cve":
            qs = parse_qs(parsed.query)
            mode = (qs.get("mode") or ["full"])[0]
            feed_name = f"nist_cve_{mode}"

        fn = _TRIGGERS.get(feed_name)
        if not fn:
            self._send(404, f"Unknown feed: {feed_name}")
            return

        if _run_in_thread(feed_name, fn):
            self._send(202, f"Feed {feed_name} triggered")
        else:
            self._send(409, f"Feed {feed_name} already running")

    def _send(self, code: int, msg: str):
        body = msg.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def start(port: int = 8001) -> None:
    server = HTTPServer(("0.0.0.0", port), _Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    logger.info("Feed trigger server listening on :%d", port)
