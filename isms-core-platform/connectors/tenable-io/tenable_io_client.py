"""Tenable Vulnerability Management (Tenable.io) API client.

Uses the Tenable cloud API at https://cloud.tenable.com.
Authentication: X-ApiKeys header with accessKey and secretKey.

Environment variables:
  TENABLE_ACCESS_KEY  — Tenable.io API access key
  TENABLE_SECRET_KEY  — Tenable.io API secret key

API base: https://cloud.tenable.com
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

_BASE_URL = "https://cloud.tenable.com"

# Poll interval for export status checks (seconds)
_EXPORT_POLL_INTERVAL = 5


class TenableIOClient:
    def __init__(self, **cfg) -> None:
        self._access_key = cfg.get('access_key') or os.environ.get('TENABLE_ACCESS_KEY', '')
        self._secret_key = cfg.get('secret_key') or os.environ.get('TENABLE_SECRET_KEY', '')
        if not self._access_key or not self._secret_key:
            raise ValueError("Tenable.io requires access_key and secret_key")

    def _headers(self) -> dict:
        return {
            "X-ApiKeys": f"accessKey={self._access_key};secretKey={self._secret_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _get(self, path: str, params: dict | None = None) -> dict:
        url = f"{_BASE_URL}/{path.lstrip('/')}"
        resp = requests.get(url, headers=self._headers(), params=params or {}, timeout=60)
        if not resp.ok:
            logger.error("Tenable.io GET %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _get_paginated(self, path: str, params: dict | None = None, result_key: str = "assets") -> list[dict]:
        """Paginated GET — follows offset/limit pagination."""
        results: list[dict] = []
        p = dict(params or {})
        limit = p.get("limit", 1000)
        offset = 0
        while True:
            p["offset"] = offset
            p["limit"] = limit
            data = self._get(path, p)
            page = data.get(result_key, [])
            results.extend(page)
            if len(page) < limit:
                break
            offset += limit
        return results

    # ── Public query methods ───────────────────────────────────────────────────

    def get_assets(self, limit: int = 1000) -> list[dict]:
        """Return assets from the workbench (last 90 days)."""
        logger.info("Fetching assets from Tenable.io workbench...")
        try:
            data = self._get("workbenches/assets", params={"date_range": 90, "limit": limit})
            assets = data.get("assets", [])
            logger.info("Fetched %d assets", len(assets))
            return assets
        except Exception as e:
            logger.warning("Could not fetch assets: %s", e)
            return []

    def get_vulnerabilities_summary(self) -> dict:
        """Return vulnerability counts by severity from the workbench."""
        logger.info("Fetching vulnerability summary from Tenable.io...")
        try:
            data = self._get("workbenches/vulnerabilities")
            logger.info(
                "Fetched vulnerability summary: %d total entries",
                len(data.get("vulnerabilities", [])),
            )
            return data
        except Exception as e:
            logger.warning("Could not fetch vulnerability summary: %s", e)
            return {}

    def get_scan_list(self) -> list[dict]:
        """Return list of configured scans with status and last run time."""
        logger.info("Fetching scan list from Tenable.io...")
        try:
            data = self._get("scans")
            scans = data.get("scans") or []
            logger.info("Fetched %d scans", len(scans))
            return scans
        except Exception as e:
            logger.warning("Could not fetch scan list: %s", e)
            return []
