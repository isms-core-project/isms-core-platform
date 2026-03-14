"""Fortinet FortiManager REST API client (JSON-RPC).

Authentication: POST /jsonrpc with method=exec, url=/sys/login/user.
Returns a session token used in all subsequent JSON-RPC calls.

Same JSON-RPC pattern as FortiAnalyzer.

Environment variables:
  FORTI_MANAGER_HOST     — Base URL, e.g. https://forti-manager.corp.local
  FORTI_MANAGER_USERNAME — Admin username (read-only service account)
  FORTI_MANAGER_PASSWORD — Admin password

API permissions required (FortiManager):
  - Create a read-only admin account in System → Administrators
  - Profile: Standard_User with ADOM access (specific ADOMs or All ADOMs)
  - Package access: Read
  - Device Manager: Read
  - No write permissions required
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class FortiManagerClient:
    """Thin JSON-RPC wrapper for the FortiManager REST API."""

    def __init__(self, **cfg) -> None:
        self._host = (cfg.get('host') or os.environ.get("FORTI_MANAGER_HOST", "")).rstrip("/")
        if not self._host:
            raise ValueError(
                "FortiManager host not set — provide FORTI_MANAGER_HOST or host config key"
            )
        self._username = cfg.get('username') or os.environ.get("FORTI_MANAGER_USERNAME", "")
        self._password = cfg.get('password') or os.environ.get("FORTI_MANAGER_PASSWORD", "")
        if not self._username or not self._password:
            raise ValueError(
                "Provide FORTI_MANAGER_USERNAME and FORTI_MANAGER_PASSWORD "
                "(or username/password config keys)"
            )

        verify_raw = cfg.get('verify_ssl') or os.environ.get("FORTI_MANAGER_VERIFY_SSL", "true")
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
        logger.info("Authenticating to FortiManager at %s as '%s'...", self._host, self._username)
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
                    f"FortiManager login failed: {status.get('message', 'unknown error')}"
                )
            self._session_token = data.get("session", "")
            if not self._session_token:
                raise RuntimeError("FortiManager login returned no session token")
            logger.info("FortiManager authentication successful")
        except requests.HTTPError as e:
            logger.error(
                "FortiManager auth HTTP %s: %s",
                e.response.status_code,
                e.response.text[:200],
            )
            raise
        except Exception as e:
            logger.error("FortiManager authentication failed: %s", e)
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
                        "FortiManager RPC %s returned status %s: %s",
                        url,
                        status.get("code"),
                        status.get("message", ""),
                    )
                return results[0].get("data", []) or []
            return []
        except requests.HTTPError as e:
            logger.error(
                "FortiManager RPC %s HTTP %s: %s",
                url,
                e.response.status_code,
                e.response.text[:200],
            )
            raise
        except Exception as e:
            logger.error("FortiManager RPC %s failed: %s", url, e)
            raise

    # ── Public query methods ──────────────────────────────────────────────────

    def get_devices(self) -> list[dict]:
        """Return managed FortiGate device inventory."""
        logger.info("Fetching devices from FortiManager...")
        try:
            items = self._call("/dvmdb/device")
            devices = items if isinstance(items, list) else []
            logger.info("Fetched %d devices", len(devices))
            return devices
        except Exception as e:
            logger.warning("Could not fetch devices: %s", e)
            return []

    def get_policy_packages(self, adom: str = "root") -> list[dict]:
        """Return policy packages for the given ADOM."""
        logger.info("Fetching policy packages for ADOM '%s' from FortiManager...", adom)
        try:
            items = self._call(f"/pm/config/adom/{adom}/pkg")
            packages = items if isinstance(items, list) else []
            logger.info("Fetched %d policy packages", len(packages))
            return packages
        except Exception as e:
            logger.warning("Could not fetch policy packages for ADOM '%s': %s", adom, e)
            return []

    def get_firmware_templates(self, adom: str = "root") -> list[dict]:
        """Return device profiles / firmware templates for the given ADOM."""
        logger.info("Fetching firmware templates for ADOM '%s' from FortiManager...", adom)
        try:
            items = self._call(f"/pm/config/adom/{adom}/devprof")
            templates = items if isinstance(items, list) else []
            logger.info("Fetched %d firmware templates", len(templates))
            return templates
        except Exception as e:
            logger.warning("Could not fetch firmware templates for ADOM '%s': %s", adom, e)
            return []

    def get_adoms(self) -> list[dict]:
        """Return list of configured ADOMs (best-effort)."""
        logger.info("Fetching ADOMs from FortiManager...")
        try:
            items = self._call("/dvmdb/adom")
            adoms = items if isinstance(items, list) else []
            logger.info("Fetched %d ADOMs", len(adoms))
            return adoms
        except Exception as e:
            logger.warning("Could not fetch ADOMs: %s", e)
            return []
