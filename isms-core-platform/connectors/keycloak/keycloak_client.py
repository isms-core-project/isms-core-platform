"""Keycloak Admin REST API client for the Keycloak connector.

Handles:
  - OAuth2 password-grant token acquisition (admin-cli client) + auto-refresh
  - Paginated GET requests (max / first)
  - Endpoints used:
      /admin/realms/{realm}/users         → A.5.15-16-18
      /admin/realms/{realm}/groups        → A.5.15-16-18
      /admin/realms/{realm}/clients       → A.8.2-3-5
      /admin/realms/{realm}/client-session-stats  → A.8.2-3-5
      /admin/realms/{realm}/events        → A.5.3

Config keys: url, username, password, realm (default: master)
Env vars:    KEYCLOAK_URL, KEYCLOAK_USERNAME, KEYCLOAK_PASSWORD, KEYCLOAK_REALM
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

PAGE_SIZE = 500


class KeycloakClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("KEYCLOAK_URL", "")).rstrip("/")
        self.username = cfg.get("username") or os.environ.get("KEYCLOAK_USERNAME", "")
        self.password = cfg.get("password") or os.environ.get("KEYCLOAK_PASSWORD", "")
        self.realm = cfg.get("realm") or os.environ.get("KEYCLOAK_REALM", "master")
        if not self.base_url:
            raise ValueError("Keycloak URL is required (config key 'url' or KEYCLOAK_URL env var)")
        if not self.username or not self.password:
            raise ValueError("Keycloak username and password are required")
        self._token: str | None = None
        self._token_expiry: float = 0

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 60:
            return self._token
        token_url = f"{self.base_url}/realms/master/protocol/openid-connect/token"
        resp = requests.post(
            token_url,
            data={
                "client_id": "admin-cli",
                "username": self.username,
                "password": self.password,
                "grant_type": "password",
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + data.get("expires_in", 60)
        logger.info("Keycloak token acquired (expires in %ds)", data.get("expires_in", 60))
        return self._token

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self._get_token()}",
            "Accept": "application/json",
        }

    def _admin_url(self, path: str) -> str:
        return f"{self.base_url}/admin/realms/{self.realm}{path}"

    # ── Paginated GET ─────────────────────────────────────────────────────────

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages using first/max pagination."""
        items = []
        first = 0
        base_params = dict(params or {})
        max_per_page = base_params.pop("max", PAGE_SIZE)

        while True:
            req_params = {**base_params, "first": first, "max": max_per_page}
            resp = requests.get(
                self._admin_url(path),
                headers=self._headers(),
                params=req_params,
                timeout=30,
            )
            resp.raise_for_status()
            page = resp.json()
            if not page:
                break
            items.extend(page)
            if len(page) < max_per_page:
                break
            first += max_per_page

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """All realm users. Returns enabled, emailVerified, totp (MFA)."""
        logger.info("Fetching Keycloak users (realm=%s)...", self.realm)
        users = self._get_all("/users")
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """All realm groups."""
        logger.info("Fetching Keycloak groups...")
        groups = self._get_all("/groups")
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_clients(self) -> list[dict]:
        """All SSO clients in the realm."""
        logger.info("Fetching Keycloak clients...")
        clients = self._get_all("/clients")
        logger.info("Fetched %d clients", len(clients))
        return clients

    def get_sessions(self) -> list[dict]:
        """Client session statistics for the realm.

        Keycloak 18+ uses /client-session-stats (replaces deprecated /sessions/stats).
        Returns a list of dicts: [{clientId, active, offline}, ...]
        """
        logger.info("Fetching Keycloak client session stats...")
        try:
            resp = requests.get(
                self._admin_url("/client-session-stats"),
                headers=self._headers(),
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            logger.info("Fetched client session stats (%d clients)", len(data) if isinstance(data, list) else 0)
            return data if isinstance(data, list) else []
        except requests.HTTPError as e:
            logger.warning("Client session stats returned %d: %s", e.response.status_code, e)
            return []

    def get_events(self, type: str = "LOGIN_ERROR", max: int = 100) -> list[dict]:
        """Realm events filtered by type (e.g. LOGIN_ERROR)."""
        logger.info("Fetching Keycloak events (type=%s, max=%d)...", type, max)
        try:
            resp = requests.get(
                self._admin_url("/events"),
                headers=self._headers(),
                params={"type": type, "max": max},
                timeout=30,
            )
            resp.raise_for_status()
            events = resp.json()
            logger.info("Fetched %d events (type=%s)", len(events), type)
            return events
        except requests.HTTPError as e:
            logger.warning("Events endpoint returned %d: %s", e.response.status_code, e)
            return []
