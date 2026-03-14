"""Fortinet FortiAnalyzer REST API client (JSON-RPC).

Authentication: POST /jsonrpc with method=exec, url=/sys/login/user.
Returns a session token used in all subsequent JSON-RPC calls.

All API calls use: POST /jsonrpc with the session token in the body.

Environment variables:
  FORTI_ANALYZER_HOST     — Base URL, e.g. https://forti-analyzer.corp.local
  FORTI_ANALYZER_USERNAME — Admin username (read-only service account)
  FORTI_ANALYZER_PASSWORD — Admin password

API permissions required (FortiAnalyzer):
  - Create a read-only admin account in System → Administrators
  - Profile: Standard_User or custom profile with:
      Log & Report: Read
      Device Manager: Read
  - No write permissions required
"""

import logging
import os
from datetime import datetime, timezone, timedelta

import requests
import urllib3

logger = logging.getLogger(__name__)


class FortiAnalyzerClient:
    """Thin JSON-RPC wrapper for the FortiAnalyzer REST API."""

    def __init__(self, **cfg) -> None:
        self._host = (cfg.get('host') or os.environ.get("FORTI_ANALYZER_HOST", "")).rstrip("/")
        if not self._host:
            raise ValueError(
                "FortiAnalyzer host not set — provide FORTI_ANALYZER_HOST or host config key"
            )
        self._username = cfg.get('username') or os.environ.get("FORTI_ANALYZER_USERNAME", "")
        self._password = cfg.get('password') or os.environ.get("FORTI_ANALYZER_PASSWORD", "")
        if not self._username or not self._password:
            raise ValueError(
                "Provide FORTI_ANALYZER_USERNAME and FORTI_ANALYZER_PASSWORD "
                "(or username/password config keys)"
            )

        verify_raw = cfg.get('verify_ssl') or os.environ.get("FORTI_ANALYZER_VERIFY_SSL", "true")
        self._verify_ssl = str(verify_raw).lower() != "false"

        self._session = requests.Session()
        self._session.verify = self._verify_ssl
        self._session.headers.update({"Content-Type": "application/json"})

        if not self._verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self._session_token: str = ""
        self._request_id: int = 1
        self.login()

    # ── Auth ──────────────────────────────────────────────────────────────────

    def login(self) -> None:
        """Authenticate and store the session token."""
        logger.info("Authenticating to FortiAnalyzer at %s as '%s'...", self._host, self._username)
        try:
            resp = self._session.post(
                f"{self._host}/jsonrpc",
                json={
                    "id": self._next_id(),
                    "method": "exec",
                    "params": [
                        {
                            "url": "/sys/login/user",
                            "data": {
                                "user": self._username,
                                "passwd": self._password,
                            },
                        }
                    ],
                },
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            result = (data.get("result") or [{}])[0]
            status = result.get("status", {})
            if status.get("code", -1) != 0:
                raise RuntimeError(
                    f"FortiAnalyzer login failed: {status.get('message', 'unknown error')}"
                )
            self._session_token = data.get("session", "")
            if not self._session_token:
                raise RuntimeError("FortiAnalyzer login returned no session token")
            logger.info("FortiAnalyzer authentication successful")
        except requests.HTTPError as e:
            logger.error(
                "FortiAnalyzer auth HTTP %s: %s",
                e.response.status_code,
                e.response.text[:200],
            )
            raise
        except Exception as e:
            logger.error("FortiAnalyzer authentication failed: %s", e)
            raise

    def _next_id(self) -> int:
        rid = self._request_id
        self._request_id += 1
        return rid

    # ── Core RPC ──────────────────────────────────────────────────────────────

    def _call(self, url: str, params: dict | None = None) -> list:
        """Issue an authenticated JSON-RPC GET call. Returns result data list."""
        try:
            body = {
                "id": self._next_id(),
                "method": "get",
                "session": self._session_token,
                "params": [
                    {
                        "url": url,
                        **(params or {}),
                    }
                ],
            }
            resp = self._session.post(
                f"{self._host}/jsonrpc",
                json=body,
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            results = data.get("result") or []
            if results:
                status = results[0].get("status", {})
                if status.get("code", -1) not in (0, 6):
                    # code 6 = object not found (treat as empty, not error)
                    logger.warning(
                        "FortiAnalyzer RPC %s returned status %s: %s",
                        url,
                        status.get("code"),
                        status.get("message", ""),
                    )
                return results[0].get("data", []) or []
            return []
        except requests.HTTPError as e:
            logger.error(
                "FortiAnalyzer RPC %s HTTP %s: %s",
                url,
                e.response.status_code,
                e.response.text[:200],
            )
            raise
        except Exception as e:
            logger.error("FortiAnalyzer RPC %s failed: %s", url, e)
            raise

    # ── Public query methods ──────────────────────────────────────────────────

    def get_devices(self) -> list[dict]:
        """Return registered FortiGate devices from Device Manager."""
        logger.info("Fetching devices from FortiAnalyzer...")
        try:
            items = self._call("/dvmdb/device")
            devices = items if isinstance(items, list) else []
            logger.info("Fetched %d devices", len(devices))
            return devices
        except Exception as e:
            logger.warning("Could not fetch devices: %s", e)
            return []

    def get_log_events(self, hours: int = 24) -> dict:
        """Return log event summary for the past N hours."""
        logger.info("Fetching log events (last %dh) from FortiAnalyzer...", hours)
        try:
            now = datetime.now(timezone.utc)
            start_time = now - timedelta(hours=hours)
            # Use logview/logfields to get a count summary
            result = self._call(
                "/logview/logfields",
                {
                    "filter": [
                        {
                            "field": "itime",
                            "op": ">=",
                            "val": int(start_time.timestamp()),
                        }
                    ],
                    "limit": 1,
                },
            )
            # Normalise — result may be a list or a dict
            if isinstance(result, list):
                return {"entries": result, "hours": hours}
            return {"summary": result, "hours": hours}
        except Exception as e:
            logger.warning("Could not fetch log events: %s", e)
            return {"hours": hours, "error": str(e)}

    def get_log_count(self, hours: int = 24) -> dict:
        """Return log record count summary for the past N hours (best-effort)."""
        logger.info("Fetching log count (last %dh) from FortiAnalyzer...", hours)
        try:
            now = datetime.now(timezone.utc)
            start_time = now - timedelta(hours=hours)
            result = self._call(
                "/report/run/list",
                {
                    "filter": {
                        "start-time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
                        "end-time": now.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                },
            )
            return {"result": result, "hours": hours}
        except Exception as e:
            logger.warning("Could not fetch log count: %s", e)
            return {"hours": hours, "error": str(e)}

    def get_incidents(self) -> list[dict]:
        """Return open incidents from FortiAnalyzer incident management."""
        logger.info("Fetching incidents from FortiAnalyzer...")
        try:
            items = self._call("/incidentmgmt/incidents", {"filter": {"status": "unresolved"}})
            incidents = items if isinstance(items, list) else []
            logger.info("Fetched %d incidents", len(incidents))
            return incidents
        except Exception as e:
            logger.warning("Could not fetch incidents: %s", e)
            return []
