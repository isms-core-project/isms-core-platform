"""FreeIPA JSON-RPC API client for the FreeIPA connector.

Authentication: Kerberos session cookie via POST /ipa/session/login_password
API: POST /ipa/session/json (JSON-RPC 2.0)

Handles:
  - Form-based login to obtain a session cookie
  - JSON-RPC envelope construction and dispatch
  - Endpoints used:
      /ipa/session/login_password  → authentication
      /ipa/session/json            → all API calls (user_find, group_find, etc.)

Config keys: url, username, password, verify_ssl
Env vars:    FREEIPA_URL, FREEIPA_USERNAME, FREEIPA_PASSWORD
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

# FreeIPA JSON-RPC API version — match the server version when possible
IPA_API_VERSION = "2.251"


class FreeIPAClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("FREEIPA_URL", "")).rstrip("/")
        self.username = cfg.get("username") or os.environ.get("FREEIPA_USERNAME", "")
        self.password = cfg.get("password") or os.environ.get("FREEIPA_PASSWORD", "")
        verify_ssl_raw = cfg.get("verify_ssl", True)
        if isinstance(verify_ssl_raw, str):
            verify_ssl_raw = verify_ssl_raw.lower() not in ("false", "0", "no")
        self.verify_ssl = verify_ssl_raw

        if not self.base_url:
            raise ValueError("FreeIPA URL is required (config key 'url' or FREEIPA_URL env var)")
        if not self.username or not self.password:
            raise ValueError("FreeIPA username and password are required")

        self._session: requests.Session | None = None

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _login(self) -> None:
        """POST /ipa/session/login_password with form data; store session cookie."""
        logger.info("Logging in to FreeIPA (url=%s, user=%s)...", self.base_url, self.username)
        session = requests.Session()
        resp = session.post(
            f"{self.base_url}/ipa/session/login_password",
            data={"user": self.username, "password": self.password},
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": f"{self.base_url}/ipa",
                "Accept": "text/plain",
            },
            verify=self.verify_ssl,
            timeout=15,
        )
        resp.raise_for_status()
        if "ipa_session" not in session.cookies:
            raise RuntimeError(
                f"FreeIPA login succeeded (HTTP {resp.status_code}) "
                "but no ipa_session cookie returned — check credentials"
            )
        self._session = session
        logger.info("FreeIPA session established")

    def _ensure_session(self) -> requests.Session:
        if self._session is None:
            self._login()
        return self._session  # type: ignore[return-value]

    # ── JSON-RPC ──────────────────────────────────────────────────────────────

    def _call(self, method: str, args: list | None = None, options: dict | None = None) -> dict:
        """POST /ipa/session/json with a JSON-RPC 2.0 envelope."""
        session = self._ensure_session()
        payload = {
            "method": method,
            "params": [
                args or [],
                {**(options or {}), "version": IPA_API_VERSION},
            ],
            "id": 0,
        }
        resp = session.post(
            f"{self.base_url}/ipa/session/json",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Referer": f"{self.base_url}/ipa",
            },
            verify=self.verify_ssl,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        error = data.get("error")
        if error:
            raise RuntimeError(f"FreeIPA API error ({method}): {error}")
        return data.get("result", {})

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """user_find — all users with full attribute set."""
        logger.info("Fetching FreeIPA users...")
        result = self._call("user_find", options={"all": True, "sizelimit": 0})
        users = result.get("result", [])
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """group_find — all groups (posix + non-posix)."""
        logger.info("Fetching FreeIPA groups...")
        result = self._call("group_find", options={"all": False, "sizelimit": 0})
        groups = result.get("result", [])
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_hosts(self) -> list[dict]:
        """host_find — enrolled hosts/clients."""
        logger.info("Fetching FreeIPA hosts...")
        try:
            result = self._call("host_find", options={"all": False, "sizelimit": 0})
            hosts = result.get("result", [])
            logger.info("Fetched %d hosts", len(hosts))
            return hosts
        except Exception as e:
            logger.warning("Could not fetch hosts: %s", e)
            return []

    def get_sudo_rules(self) -> list[dict]:
        """sudorule_find — all sudo rules (privileged access evidence)."""
        logger.info("Fetching FreeIPA sudo rules...")
        try:
            result = self._call("sudorule_find", options={"sizelimit": 0})
            rules = result.get("result", [])
            logger.info("Fetched %d sudo rules", len(rules))
            return rules
        except Exception as e:
            logger.warning("Could not fetch sudo rules: %s", e)
            return []
