"""Graylog SIEM/log management connector for ISMS CORE v2.0.

Queries the Graylog REST API and posts evidence to:
  a.8.15  — Logging            (stream count + configured input sources)
  a.8.16  — Monitoring of activities  (active alert/event count)

Environment variables required:
  ISMS_API_URL    — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN  — connector bearer token from /admin/connectors/register
  GRAYLOG_URL     — Graylog base URL, e.g. http://graylog.corp.local:9000
  GRAYLOG_USERNAME — Graylog username (read-only service account)
  GRAYLOG_PASSWORD — Graylog password
  POLL_INTERVAL   — seconds between syncs (default: 3600 = 1h)
  BATCH_SIZE      — items per API call (default: 100)

Graylog service account permissions required (read-only):
  - Read access to streams, inputs, events, indices
  - No write access required
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from graylog_client import GraylogClient

logger = logging.getLogger(__name__)


class GraylogConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.graylog = GraylogClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Graylog log/alert state is always current."""
        streams = self.graylog.get_streams()
        alerts = self.graylog.get_alerts(limit=100)
        inputs = self.graylog.get_inputs()
        message_count = self.graylog.get_message_count()
        indices = self.graylog.get_indices()

        return [
            {
                "_type": "graylog_bundle",
                "streams": streams,
                "alerts": alerts,
                "inputs": inputs,
                "message_count": message_count,
                "indices": indices,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        streams = bundle["streams"]
        alerts = bundle["alerts"]
        inputs = bundle["inputs"]
        message_count = bundle["message_count"]
        indices = bundle["indices"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.15 — Logging evidence (streams + input sources) ───────────────
        enabled_streams = [s for s in streams if not s.get("disabled", False)]
        by_input_type: Counter = Counter(
            str(inp.get("type", "Unknown"))
            for inp in inputs
        )
        # Message count for evidence of log volume
        total_messages = message_count.get("events", 0) if isinstance(message_count, dict) else 0

        # Index stats — number of active indices
        open_indices: list = []
        if isinstance(indices, dict):
            open_indices = indices.get("indices", [])

        logging_status = (
            "compliant" if len(enabled_streams) > 0 and len(inputs) > 0
            else "attention-required" if len(enabled_streams) > 0
            else "non-compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"Graylog log sources: {len(streams)} streams "
                f"({len(enabled_streams)} enabled), "
                f"{len(inputs)} inputs configured"
            ),
            source_ref="graylog-log-sources",
            classification="network",
            status=logging_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "streams": {
                    "total": len(streams),
                    "enabled": len(enabled_streams),
                    "disabled": len(streams) - len(enabled_streams),
                    "list": [
                        {
                            "id": s.get("id"),
                            "title": s.get("title", ""),
                            "disabled": s.get("disabled", False),
                            "matching_type": s.get("matching_type", ""),
                        }
                        for s in streams[:30]
                    ],
                },
                "inputs": {
                    "total": len(inputs),
                    "by_type": dict(by_input_type),
                    "list": [
                        {
                            "id": inp.get("id"),
                            "title": inp.get("title", ""),
                            "type": inp.get("type", ""),
                            "global": inp.get("global", False),
                        }
                        for inp in inputs[:30]
                    ],
                },
                "total_messages": total_messages,
                "open_indices": len(open_indices),
            },
        ))

        # ── A.8.16 — Active alerts / event monitoring ─────────────────────────
        # Alert priority/severity varies by Graylog version — try common fields
        by_priority: Counter = Counter(
            str(a.get("priority", a.get("event", {}).get("priority", "unknown")))
            for a in alerts
        )
        # Resolved vs unresolved (if available)
        unresolved = [
            a for a in alerts
            if not a.get("resolved", False)
        ]

        alert_status = (
            "attention-required" if len(unresolved) > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"Graylog active alerts: {len(alerts)} events, "
                f"{len(unresolved)} unresolved"
            ),
            source_ref="graylog-active-alerts",
            classification="incident",
            status=alert_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "alerts": {
                    "total": len(alerts),
                    "unresolved": len(unresolved),
                    "by_priority": dict(by_priority),
                },
                "recent_alerts": [
                    {
                        "id": a.get("id"),
                        "event_definition_id": (a.get("event") or {}).get("event_definition_id", ""),
                        "message": (a.get("event") or {}).get("message", a.get("message", "")),
                        "priority": a.get("priority", (a.get("event") or {}).get("priority", "")),
                        "timestamp": (a.get("event") or {}).get("timestamp", a.get("timestamp", "")),
                        "resolved": a.get("resolved", False),
                    }
                    for a in alerts[:30]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Graylog connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Graylog sync (last_run=%s)", since or "never")

                bundles = self.fetch(since)
                all_items: list[EvidenceItem] = []
                for bundle in bundles:
                    all_items.extend(self._transform_bundle(bundle))

                logger.info("Transformed %d evidence items", len(all_items))

                if all_items:
                    accepted, skipped, errors = self._post_all(all_items)
                    logger.info("Ingest: accepted=%d skipped=%d errors=%d", accepted, skipped, errors)

                self._save_state({"last_run": datetime.now(timezone.utc).isoformat()})

            except Exception as e:
                logger.error("Sync failed: %s", e, exc_info=True)

            elapsed = time.monotonic() - start
            sleep_for = max(0, self.poll_interval - elapsed)
            logger.info("Next sync in %.0fs", sleep_for)
            self._sleep_with_sync_check(sleep_for)


if __name__ == "__main__":
    GraylogConnector().run()
