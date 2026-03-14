"""ISMSConnectorBase — shared base class for all v2.0 ISMS CORE connectors.

Supports two auth modes:
  Worker mode   — single container runs all connectors.
                  CONNECTORS_WORKER_SECRET env var set; connector_id passed at init.
                  All API calls use: Authorization: Bearer <worker_secret>
                                     X-Connector-ID: <uuid>

  Standalone mode — legacy per-connector container (backward compatible).
                    ISMS_API_TOKEN env var set; connector_id not passed.
"""

import json
import logging
import os
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

STATE_DIR = Path("/tmp/connector_states")


def _interval_label(seconds: int) -> str:
    if seconds < 3600:
        return f"{seconds // 60}m"
    if seconds < 86400:
        return f"{seconds // 3600}h"
    return f"{seconds // 86400}d"


@dataclass
class EvidenceItem:
    group_code: str
    title: str
    source_ref: str | None = None
    source_url: str | None = None
    classification: str | None = None   # incident | change | asset | user | vulnerability | network | policy
    status: str | None = None
    event_date: str | None = None       # ISO 8601
    raw: dict = field(default_factory=dict)


class ISMSConnectorBase:
    """Base class for all ISMS CORE connectors."""

    def __init__(
        self,
        connector_id: str | None = None,
        config: dict | None = None,
    ) -> None:
        self.api_url = os.environ["ISMS_API_URL"].rstrip("/")
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        self.batch_size = int(os.environ.get("BATCH_SIZE", "100"))
        self.connector_name = self.__class__.__name__
        self._connector_id = connector_id
        self._config_cache = config  # pre-loaded by runner; None = fetch lazily

        # Auth: worker mode (single container) vs standalone (per-connector)
        worker_secret = os.environ.get("CONNECTORS_WORKER_SECRET", "")
        if worker_secret and connector_id:
            self._auth_headers = {
                "Authorization": f"Bearer {worker_secret}",
                "X-Connector-ID": connector_id,
            }
        else:
            api_token = os.environ.get("ISMS_API_TOKEN", "")
            self._auth_headers = {"Authorization": f"Bearer {api_token}"}

        STATE_DIR.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
        )

    # ── Auth headers (used by all API calls) ──────────────────────────────────

    @property
    def _headers(self) -> dict:
        return self._auth_headers

    # ── Sync-on-demand ────────────────────────────────────────────────────────

    def _check_sync_requested(self) -> bool:
        """Check if an admin triggered a manual sync. Clears the flag on read."""
        try:
            resp = requests.get(
                f"{self.api_url}/api/v1/connectors/me/sync-pending",
                headers=self._headers,
                timeout=5,
            )
            return resp.ok and resp.json().get("sync_requested", False)
        except Exception:
            return False

    def _sleep_with_sync_check(self, sleep_for: float) -> None:
        """Sleep for sleep_for seconds, waking every 30s to check for a sync request."""
        CHECK_INTERVAL = 30.0
        elapsed = 0.0
        while elapsed < sleep_for:
            chunk = min(CHECK_INTERVAL, sleep_for - elapsed)
            time.sleep(chunk)
            elapsed += chunk
            if elapsed < sleep_for and self._check_sync_requested():
                logger.info("Manual sync requested — waking up early")
                break

    # ── GUI config ────────────────────────────────────────────────────────────

    def _load_config(self) -> dict:
        """Return connector credentials.

        In worker mode, config is passed at construction (from /worker/all response).
        In standalone mode, fetches from API on first call then caches.
        Falls back to {} if unavailable (connector uses env vars).

        If the config contains a 'poll_interval' key (set via the UI), it overrides
        the POLL_INTERVAL env-var default so each connector runs on its own cadence.
        """
        if self._config_cache is not None:
            return self._config_cache
        try:
            resp = requests.get(
                f"{self.api_url}/api/v1/connectors/me/config",
                headers=self._headers,
                timeout=10,
            )
            resp.raise_for_status()
            self._config_cache = resp.json().get("config", {})
        except Exception as e:
            logger.warning("Could not fetch config (%s) — falling back to env vars", e)
            self._config_cache = {}

        # Apply poll_interval override from config (set via Connectors UI)
        if "poll_interval" in self._config_cache:
            try:
                override = int(self._config_cache["poll_interval"])
                if override > 0:
                    self.poll_interval = override
                    logger.info("Poll interval set from config: %ds (%s)",
                                override, _interval_label(override))
            except (TypeError, ValueError):
                pass

        return self._config_cache

    # ── State (per-connector file in worker mode) ─────────────────────────────

    def _state_file(self) -> Path:
        if self._connector_id:
            return STATE_DIR / f"{self._connector_id}.json"
        return STATE_DIR / "connector_state.json"

    def _load_state(self) -> dict:
        f = self._state_file()
        if f.exists():
            try:
                return json.loads(f.read_text())
            except Exception:
                pass
        return {}

    def _save_state(self, state: dict) -> None:
        self._state_file().write_text(json.dumps(state))

    # ── ISMS API ──────────────────────────────────────────────────────────────

    def _post_batch(self, items: list[EvidenceItem]) -> dict:
        payload = [
            {
                "group_code": i.group_code,
                "title": i.title,
                "source_ref": i.source_ref,
                "source_url": i.source_url,
                "classification": i.classification,
                "status": i.status,
                "event_date": i.event_date,
                "raw": i.raw,
            }
            for i in items
        ]
        try:
            resp = requests.post(
                f"{self.api_url}/api/v1/connectors/ingest",
                json=payload,
                headers=self._headers,
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            logger.error("ISMS API error %s: %s", e.response.status_code, e.response.text[:300])
            raise
        except Exception as e:
            logger.error("ISMS API request failed: %s", e)
            raise

    def _report_error(self, message: str) -> None:
        """Report a sync failure to the backend so the UI can surface it."""
        try:
            requests.post(
                f"{self.api_url}/api/v1/connectors/me/report-error",
                json={"error": message},
                headers=self._headers,
                timeout=10,
            )
        except Exception as e:
            logger.warning("Could not report error to backend: %s", e)

    def _post_all(self, items: list[EvidenceItem]) -> tuple[int, int, int]:
        accepted = skipped = errors = 0
        for i in range(0, len(items), self.batch_size):
            batch = items[i : i + self.batch_size]
            try:
                result = self._post_batch(batch)
                accepted += result.get("accepted", 0)
                skipped += result.get("skipped", 0)
                errors += result.get("errors", 0)
            except Exception:
                errors += len(batch)
        return accepted, skipped, errors

    # ── Main loop ─────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        raise NotImplementedError

    def transform(self, item: dict) -> EvidenceItem | None:
        raise NotImplementedError

    def run(self) -> None:
        logger.info("%s connector starting (poll_interval=%ds)", self.connector_name, self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")

                logger.info("Fetching from source (since=%s)", since or "beginning")
                raw_items = self.fetch(since)
                logger.info("Fetched %d items", len(raw_items))

                evidence_items = []
                for raw in raw_items:
                    try:
                        item = self.transform(raw)
                        if item:
                            evidence_items.append(item)
                    except Exception as e:
                        logger.warning("transform() error: %s", e)

                if evidence_items:
                    accepted, skipped, errors = self._post_all(evidence_items)
                    logger.info(
                        "Ingest complete: accepted=%d skipped=%d errors=%d",
                        accepted, skipped, errors,
                    )
                else:
                    logger.info("No new items to post")

                self._save_state({"last_run": datetime.now(timezone.utc).isoformat()})

            except Exception as e:
                logger.error("Connector run failed: %s", e, exc_info=True)
                self._report_error(f"{type(e).__name__}: {e}")

            elapsed = time.monotonic() - start
            sleep_for = max(0, self.poll_interval - elapsed)
            logger.info("Next run in %.0fs", sleep_for)
            self._sleep_with_sync_check(sleep_for)
