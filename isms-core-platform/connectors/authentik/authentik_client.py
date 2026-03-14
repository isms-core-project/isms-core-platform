"""Authentik REST API client for the Authentik connector.

Handles:
  - Bearer token auth via api_token
  - Paginated GET requests (page/page_size)
  - Endpoints used:
      /api/v3/core/users/            → A.5.15-16-18 / A.5.3
      /api/v3/core/groups/           → A.5.15-16-18
      /api/v3/core/applications/     → A.8.2-3-5
      /api/v3/outposts/instances/    → A.8.2-3-5
      /api/v3/authenticators/all/    → A.5.15-16-18
      /api/v3/flows/instances/       → A.8.2-3-5

Config keys: url, api_token
Env vars:    AUTHENTIK_URL, AUTHENTIK_API_TOKEN
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

PAGE_SIZE = 100


class AuthentikClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("AUTHENTIK_URL", "")).rstrip("/")
        self.api_token = cfg.get("api_token") or os.environ.get("AUTHENTIK_API_TOKEN", "")
        if not self.base_url:
            raise ValueError("Authentik URL is required (config key 'url' or AUTHENTIK_URL env var)")
        if not self.api_token:
            raise ValueError("Authentik API token is required (config key 'api_token' or AUTHENTIK_API_TOKEN env var)")

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_token}",
            "Accept": "application/json",
        }

    # ── Paginated GET ─────────────────────────────────────────────────────────

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of an Authentik paginated collection."""
        items = []
        page = 1
        base_params = dict(params or {})
        base_params["page_size"] = PAGE_SIZE

        while True:
            req_params = {**base_params, "page": page}
            url = f"{self.base_url}{path}"
            resp = requests.get(url, headers=self._headers(), params=req_params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            results = data.get("results", [])
            items.extend(results)
            # Authentik returns pagination metadata in 'pagination'
            pagination = data.get("pagination", {})
            if pagination.get("next") == 0 or not results:
                break
            page += 1

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """All users. Returns username, is_active, is_superuser, groups_obj, last_login."""
        logger.info("Fetching Authentik users...")
        users = self._get_all("/api/v3/core/users/")
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """All groups. Returns name, users_obj count."""
        logger.info("Fetching Authentik groups...")
        groups = self._get_all("/api/v3/core/groups/")
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_applications(self) -> list[dict]:
        """SSO-protected applications."""
        logger.info("Fetching Authentik applications...")
        apps = self._get_all("/api/v3/core/applications/")
        logger.info("Fetched %d applications", len(apps))
        return apps

    def get_outposts(self) -> list[dict]:
        """Proxy/LDAP outposts."""
        logger.info("Fetching Authentik outposts...")
        outposts = self._get_all("/api/v3/outposts/instances/")
        logger.info("Fetched %d outposts", len(outposts))
        return outposts

    def get_mfa_devices(self) -> list[dict]:
        """All MFA devices across all authenticator types."""
        logger.info("Fetching Authentik MFA devices...")
        try:
            devices = self._get_all("/api/v3/authenticators/all/")
            logger.info("Fetched %d MFA devices", len(devices))
            return devices
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "MFA devices endpoint returned %d — check API token permissions",
                    e.response.status_code,
                )
                return []
            raise

    def get_flows(self) -> list[dict]:
        """Authentication flows."""
        logger.info("Fetching Authentik authentication flows...")
        try:
            flows = self._get_all("/api/v3/flows/instances/", params={"designation": "authentication"})
            logger.info("Fetched %d authentication flows", len(flows))
            return flows
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning("Flows endpoint returned %d", e.response.status_code)
                return []
            raise
