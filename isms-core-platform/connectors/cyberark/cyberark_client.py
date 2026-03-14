"""CyberArk PVWA REST API client for the CyberArk connector.

Handles:
  - Session token auth via POST /API/Auth/CyberArk/Logon
  - Session cleanup via POST /API/Auth/Logoff
  - Paginated GET requests (limit/offset)
  - Endpoints used:
      /API/Auth/CyberArk/Logon    → authentication
      /API/Safes                  → A.5.15-16-18
      /API/Accounts               → A.8.2-3-5 / A.5.15-16-18
      /API/Users                  → A.5.3
      /API/Auth/Logoff            → session cleanup

Config keys: url, username, password, verify_ssl
Env vars:    CYBERARK_URL, CYBERARK_USERNAME, CYBERARK_PASSWORD
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

PAGE_LIMIT = 500


class CyberArkClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("CYBERARK_URL", "")).rstrip("/")
        self.username = cfg.get("username") or os.environ.get("CYBERARK_USERNAME", "")
        self.password = cfg.get("password") or os.environ.get("CYBERARK_PASSWORD", "")
        self.verify_ssl = cfg.get("verify_ssl", True)
        if isinstance(self.verify_ssl, str):
            self.verify_ssl = self.verify_ssl.lower() not in ("false", "0", "no")
        if not self.base_url:
            raise ValueError("CyberArk URL is required (config key 'url' or CYBERARK_URL env var)")
        if not self.username or not self.password:
            raise ValueError("CyberArk username and password are required")
        self._session_token: str | None = None

    # ── Auth ──────────────────────────────────────────────────────────────────

    def logon(self) -> None:
        """Authenticate and store the session token."""
        logger.info("Logging on to CyberArk PVWA (url=%s, user=%s)...", self.base_url, self.username)
        resp = requests.post(
            f"{self.base_url}/PasswordVault/API/Auth/CyberArk/Logon",
            json={"username": self.username, "password": self.password},
            verify=self.verify_ssl,
            timeout=15,
        )
        resp.raise_for_status()
        # PVWA returns the token as a quoted string
        token = resp.json()
        if isinstance(token, str):
            self._session_token = token.strip('"')
        else:
            self._session_token = token.get("token") or str(token)
        logger.info("CyberArk session token acquired")

    def logoff(self) -> None:
        """Terminate the session."""
        if not self._session_token:
            return
        try:
            requests.post(
                f"{self.base_url}/PasswordVault/API/Auth/Logoff",
                headers=self._headers(),
                verify=self.verify_ssl,
                timeout=10,
            )
            logger.info("CyberArk session terminated")
        except Exception as e:
            logger.warning("Logoff failed (non-critical): %s", e)
        finally:
            self._session_token = None

    def _headers(self) -> dict:
        if not self._session_token:
            self.logon()
        return {
            "Authorization": self._session_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    # ── Paginated GET ─────────────────────────────────────────────────────────

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages using limit/offset pagination."""
        items = []
        offset = 0
        base_params = dict(params or {})
        limit = base_params.pop("limit", PAGE_LIMIT)

        while True:
            req_params = {**base_params, "limit": limit, "offset": offset}
            resp = requests.get(
                f"{self.base_url}/PasswordVault{path}",
                headers=self._headers(),
                params=req_params,
                verify=self.verify_ssl,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            # PVWA wraps results in 'value' or 'Safes' or 'Users' etc.
            page = (
                data.get("value")
                or data.get("Safes")
                or data.get("Users")
                or data.get("Accounts")
                or []
            )
            items.extend(page)
            total = data.get("count", data.get("Total", None))
            if total is not None and offset + limit >= total:
                break
            if not page or len(page) < limit:
                break
            offset += limit

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_safes(self) -> list[dict]:
        """All vaults/safes."""
        logger.info("Fetching CyberArk safes...")
        safes = self._get_all("/API/Safes")
        logger.info("Fetched %d safes", len(safes))
        return safes

    def get_accounts(self) -> list[dict]:
        """All privileged accounts. Returns username, address, platformId, safeName, status."""
        logger.info("Fetching CyberArk accounts...")
        accounts = self._get_all("/API/Accounts")
        logger.info("Fetched %d accounts", len(accounts))
        return accounts

    def get_users(self) -> list[dict]:
        """CyberArk platform users."""
        logger.info("Fetching CyberArk users...")
        users = self._get_all("/API/Users")
        logger.info("Fetched %d users", len(users))
        return users
