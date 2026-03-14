"""SentinelOne Management Console API client.

Uses the SentinelOne REST API v2.1.
Authentication: API Token in header: Authorization: ApiToken <token>
Pagination: cursor-based via nextCursor in response pagination object.

Environment variables:
  SENTINELONE_URL       — Management console base URL, e.g. https://usea1.sentinelone.net
  SENTINELONE_API_TOKEN — API token generated from the console

API base: <url>/web/api/v2.1
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

_API_VERSION = "v2.1"


class SentinelOneClient:
    def __init__(self, **cfg) -> None:
        self._url = (cfg.get('url') or os.environ.get('SENTINELONE_URL', '')).rstrip('/')
        self._api_token = cfg.get('api_token') or os.environ.get('SENTINELONE_API_TOKEN', '')
        self._base = f"{self._url}/web/api/{_API_VERSION}"

    def _headers(self) -> dict:
        return {
            "Authorization": f"ApiToken {self._api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _get(self, path: str, params: dict | None = None) -> dict:
        resp = requests.get(
            f"{self._base}/{path.lstrip('/')}",
            headers=self._headers(),
            params=params or {},
            timeout=60,
        )
        if not resp.ok:
            logger.error("SentinelOne API error %s on %s: %s", resp.status_code, path, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _get_paginated(self, path: str, params: dict | None = None, limit: int = 1000) -> list[dict]:
        """Cursor-based pagination — collects all pages up to limit records."""
        results: list[dict] = []
        p = dict(params or {})
        p["limit"] = 200  # max page size
        cursor: str | None = None

        while True:
            if cursor:
                p["cursor"] = cursor
            data = self._get(path, p)
            batch = data.get("data", [])
            results.extend(batch)
            pagination = data.get("pagination", {})
            cursor = pagination.get("nextCursor")
            if not cursor or not batch or len(results) >= limit:
                break

        return results[:limit]

    # ── Public query methods ──────────────────────────────────────────────────

    def get_agents(self, limit: int = 1000) -> list[dict]:
        """Return enrolled agents with health and threat status."""
        logger.info("Fetching SentinelOne agents...")
        try:
            agents = self._get_paginated("agents", limit=limit)
            logger.info("Fetched %d agents", len(agents))
            return agents
        except Exception as e:
            logger.warning("Could not fetch agents: %s", e)
            return []

    def get_threats(self, limit: int = 500) -> list[dict]:
        """Return unresolved threats."""
        logger.info("Fetching SentinelOne threats...")
        try:
            threats = self._get_paginated("threats", params={"resolved": "false"}, limit=limit)
            logger.info("Fetched %d unresolved threats", len(threats))
            return threats
        except Exception as e:
            logger.warning("Could not fetch threats: %s", e)
            return []

    def get_exclusions(self) -> list[dict]:
        """Return configured exclusions."""
        logger.info("Fetching SentinelOne exclusions...")
        try:
            data = self._get("exclusions", params={"limit": 1})
            # We only need the count — returned in pagination.totalItems
            total = data.get("pagination", {}).get("totalItems", 0)
            logger.info("SentinelOne reports %d configured exclusions", total)
            # Return a synthetic list with one item holding the count
            return [{"total_exclusions": total}]
        except Exception as e:
            logger.warning("Could not fetch exclusions: %s", e)
            return []
