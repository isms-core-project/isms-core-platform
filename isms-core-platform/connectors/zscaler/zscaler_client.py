"""Zscaler Internet Access (ZIA) API client.

Uses the ZIA REST API with session-cookie authentication.
Authentication: POST /authenticatedSession with username, password, and apiKey.
The session cookie (JSESSIONID) is maintained by a requests.Session for
subsequent calls.

Environment variables:
  ZSCALER_URL      — Cloud-specific base URL, e.g. https://zsapi.zscalerthree.net/api/v1
  ZSCALER_USERNAME — ZIA admin username
  ZSCALER_PASSWORD — ZIA admin password
  ZSCALER_API_KEY  — ZIA API key (raw value; obfuscation handled internally)

API base: <url>/api/v1
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)


def _obfuscate_api_key(api_key: str) -> tuple[str, str]:
    """Return (obfuscated_key, timestamp) per ZIA authentication docs.

    The ZIA API requires the API key to be obfuscated before sending:
    1. Record the current epoch time in milliseconds as a string.
    2. Take the last six digits of the timestamp.
    3. Reverse them.
    4. For each digit d in the reversed string: use api_key[d] if d >= 0, else api_key[d+10].
    5. For the last six digits of the timestamp: shift each digit by +2.

    Returns the obfuscated key and the timestamp string used.
    """
    now_ms = str(int(time.time() * 1000))
    n = now_ms[-6:]
    r = n[::-1]
    key = ""
    for c in r:
        key += api_key[int(c)]
    for c in n:
        key += api_key[int(c) + 2]
    return key, now_ms


class ZscalerClient:
    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ.get('ZSCALER_URL', '')).rstrip('/')
        self._username = cfg.get('username') or os.environ.get('ZSCALER_USERNAME', '')
        self._password = cfg.get('password') or os.environ.get('ZSCALER_PASSWORD', '')
        self._api_key = cfg.get('api_key') or os.environ.get('ZSCALER_API_KEY', '')
        self._session = requests.Session()
        self._authenticated = False

    def _authenticate(self) -> None:
        """Establish a ZIA session."""
        obfuscated_key, timestamp = _obfuscate_api_key(self._api_key)
        payload = {
            "username": self._username,
            "password": self._password,
            "apiKey": obfuscated_key,
            "timestamp": timestamp,
        }
        resp = self._session.post(
            f"{self._base_url}/authenticatedSession",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        if not resp.ok:
            logger.error("ZIA authentication failed %s: %s", resp.status_code, resp.text[:300])
        resp.raise_for_status()
        self._authenticated = True
        logger.info("ZIA session established")

    def _ensure_session(self) -> None:
        if not self._authenticated:
            self._authenticate()

    def _get(self, path: str, params: dict | None = None) -> dict | list:
        self._ensure_session()
        resp = self._session.get(
            f"{self._base_url}/{path.lstrip('/')}",
            params=params or {},
            headers={"Accept": "application/json"},
            timeout=60,
        )
        if resp.status_code == 401:
            # Session may have expired — re-authenticate once
            logger.warning("ZIA session expired, re-authenticating...")
            self._authenticated = False
            self._authenticate()
            resp = self._session.get(
                f"{self._base_url}/{path.lstrip('/')}",
                params=params or {},
                headers={"Accept": "application/json"},
                timeout=60,
            )
        if not resp.ok:
            logger.error("ZIA API error %s on %s: %s", resp.status_code, path, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _logout(self) -> None:
        try:
            self._session.delete(
                f"{self._base_url}/authenticatedSession",
                timeout=10,
            )
            logger.info("ZIA session terminated")
        except Exception as e:
            logger.warning("ZIA logout failed: %s", e)
        self._authenticated = False

    # ── Public query methods ──────────────────────────────────────────────────

    def get_url_categories(self) -> list[dict]:
        """Return all URL categories (custom + predefined)."""
        logger.info("Fetching ZIA URL categories...")
        try:
            data = self._get("urlCategories")
            categories = data if isinstance(data, list) else []
            logger.info("Fetched %d URL categories", len(categories))
            return categories
        except Exception as e:
            logger.warning("Could not fetch URL categories: %s", e)
            return []

    def get_firewall_rules(self) -> list[dict]:
        """Return all firewall filtering rules."""
        logger.info("Fetching ZIA firewall rules...")
        try:
            data = self._get("firewallFilteringRules")
            rules = data if isinstance(data, list) else []
            logger.info("Fetched %d firewall rules", len(rules))
            return rules
        except Exception as e:
            logger.warning("Could not fetch firewall rules: %s", e)
            return []

    def get_ssl_inspection_rules(self) -> list[dict]:
        """Return all SSL inspection rules."""
        logger.info("Fetching ZIA SSL inspection rules...")
        try:
            data = self._get("sslInspectionRules")
            rules = data if isinstance(data, list) else []
            logger.info("Fetched %d SSL inspection rules", len(rules))
            return rules
        except Exception as e:
            logger.warning("Could not fetch SSL inspection rules: %s", e)
            return []

    def get_users(self) -> list[dict]:
        """Return all ZIA users (paginated by pageSize=1000)."""
        logger.info("Fetching ZIA users...")
        try:
            data = self._get("users", params={"pageSize": 1000})
            users = data if isinstance(data, list) else []
            logger.info("Fetched %d users", len(users))
            return users
        except Exception as e:
            logger.warning("Could not fetch users: %s", e)
            return []
