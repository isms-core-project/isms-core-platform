"""Devolutions Server (DVLS) REST API client.

Authenticates via Application User (app_key + app_secret) as recommended for API access,
or falls back to username/password admin auth.

DVLS instance: https://10.0.0.71:5000 (MetalLB fixed IP in factory_kubernetes dvls-beta)

API reference: https://docs.devolutions.net/server/web-interface/utilities/api-documentation/
"""

import logging
from typing import Any

import requests
import urllib3

# DVLS often uses self-signed certs on internal deployments
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)

DEFAULT_PAGE_SIZE = 200


class DVLSClient:
    """Thin REST client for Devolutions Server v1 API.

    Supports two auth modes:
      - Application User (preferred): app_key + app_secret → Bearer token
      - Admin: username + password → session token

    Usage:
        client = DVLSClient(base_url="https://10.0.0.71:5000", app_key="...", app_secret="...")
        client.authenticate()
        accounts = client.get_connections()
        client.logoff()
    """

    def __init__(
        self,
        base_url: str,
        app_key: str = "",
        app_secret: str = "",
        username: str = "",
        password: str = "",
        verify_ssl: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.app_key = app_key
        self.app_secret = app_secret
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self._token: str | None = None
        self._session = requests.Session()
        self._session.verify = verify_ssl

    # ── Auth ──────────────────────────────────────────────────────────────────

    def authenticate(self) -> None:
        """Obtain a Bearer token. Uses app_key/app_secret if available, else username/password."""
        if self.app_key and self.app_secret:
            self._auth_application_user()
        elif self.username and self.password:
            self._auth_admin()
        else:
            raise ValueError("DVLS: either (app_key + app_secret) or (username + password) required")
        logger.info("DVLS authenticated (token obtained)")

    def _auth_application_user(self) -> None:
        """POST /api/v1/authenticate/application — Application User auth."""
        resp = self._session.post(
            f"{self.base_url}/api/v1/authenticate/application",
            json={"appKey": self.app_key, "appSecret": self.app_secret},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        # Token may be at .token, .access_token, or .tokenId depending on DVLS version
        self._token = (
            data.get("token")
            or data.get("access_token")
            or data.get("tokenId")
            or data.get("Token")
        )
        if not self._token:
            raise ValueError(f"DVLS auth: no token in response: {list(data.keys())}")
        self._session.headers["Authorization"] = f"Bearer {self._token}"

    def _auth_admin(self) -> None:
        """POST /api/v1/authenticate — admin username/password auth."""
        resp = self._session.post(
            f"{self.base_url}/api/v1/authenticate",
            json={"userName": self.username, "password": self.password},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = (
            data.get("token")
            or data.get("access_token")
            or data.get("tokenId")
            or data.get("Token")
        )
        if not self._token:
            raise ValueError(f"DVLS admin auth: no token in response: {list(data.keys())}")
        self._session.headers["Authorization"] = f"Bearer {self._token}"

    def logoff(self) -> None:
        """POST /api/v1/authenticate/logout — invalidate the session token."""
        if not self._token:
            return
        try:
            self._session.post(f"{self.base_url}/api/v1/authenticate/logout", timeout=10)
        except Exception:
            pass
        self._token = None
        self._session.headers.pop("Authorization", None)

    # ── Users & Groups ────────────────────────────────────────────────────────

    def get_users(self) -> list[dict[str, Any]]:
        """GET /api/v1/users — all user accounts."""
        return self._get_paged("/api/v1/users")

    def get_user_groups(self) -> list[dict[str, Any]]:
        """GET /api/v1/groups — user groups and roles."""
        return self._get_paged("/api/v1/groups")

    # ── Connections / Credentials ─────────────────────────────────────────────

    def get_connections(self) -> list[dict[str, Any]]:
        """GET /api/v1/connections — all connection entries (stored credentials/accounts)."""
        return self._get_paged("/api/v1/connections")

    def get_privileged_accounts(self) -> list[dict[str, Any]]:
        """GET /api/v1/connections with privileged-access filter if available,
        otherwise returns all connections for downstream filtering."""
        return self._get_paged("/api/v1/connections")

    # ── Sessions & Activity ───────────────────────────────────────────────────

    def get_active_sessions(self) -> list[dict[str, Any]]:
        """GET /api/v1/sessions/active — currently open sessions."""
        try:
            return self._get_paged("/api/v1/sessions/active")
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 404:
                logger.debug("DVLS: /sessions/active not available, trying /sessions")
                return self._get_paged("/api/v1/sessions")
            raise

    def get_session_logs(self, limit: int = 500) -> list[dict[str, Any]]:
        """GET /api/v1/logs — activity/audit log entries."""
        try:
            return self._get_paged("/api/v1/logs", max_items=limit)
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 404:
                logger.debug("DVLS: /logs not available, trying /audit/logs")
                return self._get_paged("/api/v1/audit/logs", max_items=limit)
            raise

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _get_paged(self, path: str, max_items: int = 2000) -> list[dict[str, Any]]:
        """Fetch all pages from a list endpoint using page/pageSize pagination."""
        results: list[dict[str, Any]] = []
        page = 1
        while True:
            resp = self._session.get(
                f"{self.base_url}{path}",
                params={"page": page, "pageSize": DEFAULT_PAGE_SIZE},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()

            # DVLS returns either a list directly or {data: [...], totalCount: N}
            if isinstance(data, list):
                batch = data
            elif isinstance(data, dict):
                batch = (
                    data.get("data")
                    or data.get("items")
                    or data.get("value")
                    or data.get("results")
                    or []
                )
            else:
                batch = []

            results.extend(batch)

            if len(batch) < DEFAULT_PAGE_SIZE or len(results) >= max_items:
                break
            page += 1

        return results[:max_items]
