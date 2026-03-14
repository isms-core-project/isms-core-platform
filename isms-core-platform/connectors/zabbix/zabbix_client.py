"""Zabbix API client (JSON-RPC 2.0).

Authentication: call user.login with username + password to obtain an auth token.
That token is included in all subsequent JSON-RPC calls.

Environment variables:
  ZABBIX_URL      — Base URL, e.g. http://zabbix.corp.local
  ZABBIX_USERNAME — Service account username
  ZABBIX_PASSWORD — Service account password

Minimum Zabbix permissions for the service account:
  - Read-only access to all host groups to be monitored
  - No write access required
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)


class ZabbixClient:
    """Thin JSON-RPC 2.0 wrapper for the Zabbix API."""

    def __init__(self, **cfg) -> None:
        base_url = (cfg.get('url') or os.environ.get("ZABBIX_URL", "")).rstrip("/")
        if not base_url:
            raise ValueError("Zabbix URL not set — provide ZABBIX_URL or url config key")
        self._endpoint = f"{base_url}/api_jsonrpc.php"
        self._username = cfg.get('username') or os.environ.get("ZABBIX_USERNAME", "")
        self._password = cfg.get('password') or os.environ.get("ZABBIX_PASSWORD", "")
        if not self._username or not self._password:
            raise ValueError("Provide ZABBIX_USERNAME and ZABBIX_PASSWORD (or username/password config keys)")
        self._token: str = ""
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})
        self.login()

    # ── Core RPC ──────────────────────────────────────────────────────────────

    def _call(self, method: str, params: dict) -> object:
        """Execute a single JSON-RPC 2.0 call. Returns the result field.

        Zabbix 7.2+ removed the 'auth' field from JSON-RPC — use Authorization: Bearer header.
        Older versions (pre-7.2) require 'auth' in the payload.
        We include both so the client works across all supported versions.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            # Legacy auth field (Zabbix < 7.2). Ignored by 7.2+ but harmless.
            "auth": self._token or None,
            "id": 1,
        }
        headers = {}
        if self._token:
            # Zabbix 7.2+ authentication via Bearer header
            headers["Authorization"] = f"Bearer {self._token}"
        try:
            resp = self._session.post(self._endpoint, json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            body = resp.json()
            if "error" in body:
                err = body["error"]
                raise RuntimeError(
                    f"Zabbix API error {err.get('code')}: {err.get('data', err.get('message', ''))}"
                )
            return body.get("result")
        except requests.HTTPError as e:
            logger.error("Zabbix HTTP %s: %s", e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("Zabbix API request failed (%s): %s", method, e)
            raise

    # ── Auth ──────────────────────────────────────────────────────────────────

    def login(self) -> None:
        """Authenticate and store the session token."""
        logger.info("Authenticating to Zabbix API as '%s'...", self._username)
        # 'username' param introduced in Zabbix 5.4 (replaces old 'user' param)
        result = self._call("user.login", {"username": self._username, "password": self._password})
        if not result:
            raise RuntimeError("Zabbix user.login returned empty token")
        self._token = str(result)
        logger.info("Zabbix authentication successful")

    # ── Public query methods ──────────────────────────────────────────────────

    def get_hosts(self) -> list[dict]:
        """Return all monitored hosts with status and availability."""
        logger.info("Fetching hosts from Zabbix...")
        result = self._call("host.get", {
            "output": ["hostid", "host", "name", "status", "available"],
        })
        hosts = result if isinstance(result, list) else []
        logger.info("Fetched %d hosts", len(hosts))
        return hosts

    def get_problems(self, limit: int = 500) -> list[dict]:
        """Return recent active problems (unresolved events)."""
        logger.info("Fetching active problems from Zabbix (limit=%d)...", limit)
        result = self._call("problem.get", {
            "recent": True,
            "output": "extend",
            "limit": limit,
        })
        problems = result if isinstance(result, list) else []
        logger.info("Fetched %d active problems", len(problems))
        return problems

    def get_triggers_count(self) -> int:
        """Return count of currently-firing (active) triggers."""
        logger.info("Fetching active trigger count from Zabbix...")
        result = self._call("trigger.get", {
            "only_true": 1,
            "output": ["triggerid"],
            "countOutput": True,
        })
        count = int(result) if result is not None else 0
        logger.info("Active triggers: %d", count)
        return count
