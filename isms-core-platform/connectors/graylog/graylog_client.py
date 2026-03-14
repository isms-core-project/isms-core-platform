"""Graylog REST API client.

Authentication: HTTP Basic auth (username + password).
All requests also include the mandatory header: X-Requested-By: ISMS-CORE

Environment variables:
  GRAYLOG_URL      — Base URL, e.g. http://graylog.corp.local:9000
  GRAYLOG_USERNAME — Graylog username (admin or read-only service account)
  GRAYLOG_PASSWORD — Graylog password

Minimum Graylog permissions for the service account:
  - Read access to streams, inputs, events, indices
  - No write access required
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

# Mandatory header for all Graylog API requests
_GRAYLOG_REQUIRED_HEADER = "ISMS-CORE"


class GraylogClient:
    """Thin REST wrapper for the Graylog REST API."""

    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ.get("GRAYLOG_URL", "")).rstrip("/") + "/api"
        if not self._base_url or self._base_url == "/api":
            raise ValueError("Graylog URL not set — provide GRAYLOG_URL or url config key")
        username = cfg.get('username') or os.environ.get("GRAYLOG_USERNAME", "")
        password = cfg.get('password') or os.environ.get("GRAYLOG_PASSWORD", "")
        if not username or not password:
            raise ValueError("Provide GRAYLOG_USERNAME and GRAYLOG_PASSWORD (or username/password config keys)")
        self._session = requests.Session()
        self._session.auth = (username, password)
        self._session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Requested-By": _GRAYLOG_REQUIRED_HEADER,
        })

    def _get(self, path: str, params: dict | None = None) -> dict:
        """Issue an authenticated GET and return the parsed JSON body."""
        try:
            resp = self._session.get(
                f"{self._base_url}/{path.lstrip('/')}",
                params=params or {},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            logger.error("Graylog GET %s HTTP %s: %s", path, e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("Graylog GET %s failed: %s", path, e)
            raise

    # ── Public query methods ──────────────────────────────────────────────────

    def get_cluster_health(self) -> dict:
        """Return system metric data for cluster health (best-effort)."""
        logger.info("Fetching Graylog cluster health...")
        try:
            return self._get("system/metrics/namespace/org.graylog2.inputs")
        except Exception as e:
            logger.warning("Could not fetch cluster health: %s", e)
            return {}

    def get_streams(self) -> list[dict]:
        """Return configured log streams."""
        logger.info("Fetching streams from Graylog...")
        data = self._get("streams")
        streams = data.get("streams", []) if isinstance(data, dict) else []
        logger.info("Fetched %d streams", len(streams))
        return streams

    def get_alerts(self, limit: int = 100) -> list[dict]:
        """Return recent event alerts."""
        logger.info("Fetching alerts from Graylog (limit=%d)...", limit)
        try:
            data = self._get("events/events", {"per_page": limit, "page": 1})
            events = data.get("events", []) if isinstance(data, dict) else []
            logger.info("Fetched %d alerts", len(events))
            return events
        except Exception as e:
            logger.warning("Could not fetch alerts: %s", e)
            return []

    def get_inputs(self) -> list[dict]:
        """Return configured log inputs (sources sending logs to Graylog)."""
        logger.info("Fetching inputs from Graylog...")
        data = self._get("system/inputs")
        inputs = data.get("inputs", []) if isinstance(data, dict) else []
        logger.info("Fetched %d inputs", len(inputs))
        return inputs

    def get_message_count(self) -> dict:
        """Return total message count across all indices."""
        logger.info("Fetching message count from Graylog...")
        try:
            return self._get("count/messages")
        except Exception as e:
            logger.warning("Could not fetch message count: %s", e)
            return {}

    def get_indices(self) -> dict:
        """Return Elasticsearch/OpenSearch index stats for Graylog."""
        logger.info("Fetching index stats from Graylog...")
        try:
            return self._get("system/indexer/indices")
        except Exception as e:
            logger.warning("Could not fetch index stats: %s", e)
            return {}
