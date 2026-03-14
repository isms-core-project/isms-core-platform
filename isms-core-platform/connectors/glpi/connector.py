"""GLPI IT asset management connector for ISMS CORE v2.0.

Queries the GLPI REST API and posts evidence to:
  a.5.9      — Inventory of information and other associated assets  (computer assets)
  a.5.24-28  — Incident management lifecycle  (open ticket pipeline)

Environment variables required:
  ISMS_API_URL    — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN  — connector bearer token from /admin/connectors/register
  GLPI_URL        — GLPI base URL, e.g. http://glpi.corp.local
  GLPI_USER_TOKEN — GLPI user API token (from user profile)
  GLPI_APP_TOKEN  — GLPI application token (from API settings)
  POLL_INTERVAL   — seconds between syncs (default: 86400 = 24h)
  BATCH_SIZE      — items per API call (default: 100)

GLPI service account permissions required (read-only):
  - Read access to Computers, Software, Tickets
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
from glpi_client import GLPIClient

logger = logging.getLogger(__name__)

# GLPI ticket status codes (expand_dropdowns may return labels instead)
TICKET_OPEN_STATUSES = {1, 2, 3, 4, "1", "2", "3", "4",
                         "New", "Assigned", "Planned", "Waiting"}
TICKET_RESOLVED_STATUSES = {5, 6, "5", "6", "Solved", "Closed"}


class GLPIConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.glpi = GLPIClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — GLPI asset state is always current, no delta needed."""
        computers = self.glpi.get_computers(limit=500)
        tickets = self.glpi.get_tickets(status="open", limit=200)
        software = self.glpi.get_software(limit=1000)

        return [
            {
                "_type": "glpi_bundle",
                "computers": computers,
                "tickets": tickets,
                "software": software,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        computers = bundle["computers"]
        tickets = bundle["tickets"]
        software = bundle["software"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.9 — Asset inventory ───────────────────────────────────────────
        # Group by computer type (expand_dropdowns provides human-readable label)
        by_type: Counter = Counter(
            str(c.get("computertypes_id", "Unknown"))
            for c in computers
        )
        # Group by status label
        by_status: Counter = Counter(
            str(c.get("states_id", "Unknown"))
            for c in computers
        )

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"GLPI asset inventory: {len(computers)} computers, "
                f"{len(software)} software records"
            ),
            source_ref="glpi-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "computers": {
                    "total": len(computers),
                    "by_type": dict(by_type),
                    "by_status": dict(by_status),
                },
                "software": {
                    "total": len(software),
                },
                "sample_assets": [
                    {
                        "id": c.get("id"),
                        "name": c.get("name", ""),
                        "type": c.get("computertypes_id", ""),
                        "status": c.get("states_id", ""),
                        "serial": c.get("serial", ""),
                        "location": c.get("locations_id", ""),
                    }
                    for c in computers[:50]
                ],
            },
        ))

        # ── A.5.24-28 — Incident management (ticket pipeline) ─────────────────
        open_count = sum(
            1 for t in tickets
            if t.get("status") in TICKET_OPEN_STATUSES
        )
        resolved_count = sum(
            1 for t in tickets
            if t.get("status") in TICKET_RESOLVED_STATUSES
        )
        by_ticket_status: Counter = Counter(
            str(t.get("status", "Unknown"))
            for t in tickets
        )
        by_ticket_type: Counter = Counter(
            str(t.get("type", "Unknown"))
            for t in tickets
        )
        # GLPI urgency: 1=Very Low, 2=Low, 3=Medium, 4=High, 5=Very High
        high_urgency = sum(
            1 for t in tickets
            if str(t.get("urgency", "0")) in ("4", "5", "High", "Very High")
        )

        ticket_status = (
            "attention-required" if high_urgency > 0 or open_count > 50
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.5.24-28",
            title=(
                f"GLPI tickets: {len(tickets)} total, "
                f"{open_count} open/in-progress, {resolved_count} resolved, "
                f"{high_urgency} high urgency"
            ),
            source_ref="glpi-open-tickets",
            classification="incident",
            status=ticket_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_tickets": len(tickets),
                "open_count": open_count,
                "resolved_count": resolved_count,
                "high_urgency_count": high_urgency,
                "by_status": dict(by_ticket_status),
                "by_type": dict(by_ticket_type),
                "recent_tickets": [
                    {
                        "id": t.get("id"),
                        "name": t.get("name", ""),
                        "status": t.get("status", ""),
                        "urgency": t.get("urgency", ""),
                        "date": t.get("date", ""),
                    }
                    for t in tickets[:30]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("GLPI connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting GLPI sync (last_run=%s)", since or "never")

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
    GLPIConnector().run()
