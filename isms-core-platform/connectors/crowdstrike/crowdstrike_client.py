"""CrowdStrike Falcon API client.

Uses the CrowdStrike Falcon REST API.
Authentication: OAuth2 client_credentials — POST to /oauth2/token with
client_id + client_secret in request body; returns access_token.

Environment variables:
  CROWDSTRIKE_CLIENT_ID     — OAuth2 client ID
  CROWDSTRIKE_CLIENT_SECRET — OAuth2 client secret

API base: https://api.crowdstrike.com
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

_TOKEN_URL = "{base_url}/oauth2/token"
_DEFAULT_BASE_URL = "https://api.crowdstrike.com"


class CrowdStrikeClient:
    def __init__(self, **cfg) -> None:
        self._client_id = cfg.get('client_id') or os.environ.get('CROWDSTRIKE_CLIENT_ID', '')
        self._client_secret = cfg.get('client_secret') or os.environ.get('CROWDSTRIKE_CLIENT_SECRET', '')
        self._base_url = (cfg.get('base_url') or os.environ.get('CROWDSTRIKE_BASE_URL', _DEFAULT_BASE_URL)).rstrip('/')
        self._token: str | None = None
        self._token_expires_at: float = 0.0

    def _ensure_token(self) -> None:
        if self._token and time.time() < self._token_expires_at - 60:
            return
        resp = requests.post(
            _TOKEN_URL.format(base_url=self._base_url),
            data={
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            },
            headers={"Accept": "application/json"},
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expires_at = time.time() + data.get("expires_in", 1799)
        logger.info("CrowdStrike token refreshed (expires in %ds)", data.get("expires_in", 1799))

    def _auth_headers(self) -> dict:
        self._ensure_token()
        return {"Authorization": f"Bearer {self._token}", "Accept": "application/json"}

    def _get(self, path: str, params: dict | None = None) -> dict:
        resp = requests.get(
            f"{self._base_url}/{path.lstrip('/')}",
            headers=self._auth_headers(),
            params=params or {},
            timeout=60,
        )
        if not resp.ok:
            logger.error("CrowdStrike API error %s on %s: %s", resp.status_code, path, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, payload: dict) -> dict:
        resp = requests.post(
            f"{self._base_url}/{path.lstrip('/')}",
            headers={**self._auth_headers(), "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        if not resp.ok:
            logger.error("CrowdStrike API error %s on %s: %s", resp.status_code, path, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    # ── Public query methods ──────────────────────────────────────────────────

    def get_devices(self) -> list[dict]:
        """Return all enrolled devices by querying IDs then fetching entity detail in batches."""
        logger.info("Fetching CrowdStrike device IDs...")
        ids: list[str] = []
        offset = 0
        limit = 5000
        while True:
            data = self._get("devices/queries/devices/v1", params={"limit": limit, "offset": offset})
            batch = data.get("resources", [])
            ids.extend(batch)
            meta = data.get("meta", {}).get("pagination", {})
            total = meta.get("total", 0)
            offset += len(batch)
            if not batch or offset >= total:
                break
        logger.info("Fetched %d device IDs; retrieving entity details...", len(ids))

        devices: list[dict] = []
        # Batch fetch entities in groups of 100 (API limit)
        BATCH = 100
        for i in range(0, len(ids), BATCH):
            batch_ids = ids[i : i + BATCH]
            try:
                resp = self._post("devices/entities/devices/v2", {"ids": batch_ids})
                devices.extend(resp.get("resources", []))
            except Exception as e:
                logger.warning("Could not fetch device entities for batch starting %d: %s", i, e)

        logger.info("Fetched %d device records", len(devices))
        return devices

    def get_alerts(self, limit: int = 500) -> list[dict]:
        """Return recent alerts via the Alerts API (replaces deprecated Detects API).

        The Detects API (detections/queries/detections/v1) was deprecated in 2024.
        Alerts API: query composite IDs then fetch full alert entities.
          Query:  GET  alerts/queries/alerts/v2
          Fetch:  POST alerts/entities/alerts/GET/v1  { "composite_ids": [...] }
        """
        logger.info("Fetching CrowdStrike alert IDs...")
        try:
            id_data = self._get("alerts/queries/alerts/v2", params={"limit": limit})
            composite_ids = id_data.get("resources", [])
            if not composite_ids:
                logger.info("No alert IDs returned")
                return []
            logger.info("Fetching entities for %d alerts...", len(composite_ids))
            entity_data = self._post(
                "alerts/entities/alerts/GET/v1",
                {"composite_ids": composite_ids},
            )
            alerts = entity_data.get("resources", [])
            logger.info("Fetched %d alert entities", len(alerts))
            return alerts
        except Exception as e:
            logger.warning("Could not fetch alerts: %s", e)
            return []

    def get_prevention_policies(self) -> list[dict]:
        """Return all prevention policies with platform and enabled status."""
        logger.info("Fetching CrowdStrike prevention policies...")
        try:
            data = self._get("policy/combined/prevention/v1")
            policies = data.get("resources", [])
            logger.info("Fetched %d prevention policies", len(policies))
            return policies
        except Exception as e:
            logger.warning("Could not fetch prevention policies: %s", e)
            return []
