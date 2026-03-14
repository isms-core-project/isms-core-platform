"""ServiceNow ITSM connector for ISMS CORE v2.0.

Pulls incidents, change requests, and problems from ServiceNow and posts evidence to:
  a.5.25  — Response to information security incidents  (incidents + resolution times)
  a.8.32  — Change management  (change request pipeline + approval states)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  SNOW_INSTANCE         — ServiceNow instance, e.g. mycompany (→ mycompany.service-now.com)
  SNOW_USERNAME         — Service account with itil or readonly role
  SNOW_PASSWORD         — Service account password
  SNOW_LOOKBACK_DAYS    — Days of history to pull (default: 30)
  POLL_INTERVAL         — seconds between syncs (default: 3600 = 1h)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from servicenow_client import ServiceNowClient

logger = logging.getLogger(__name__)

# ServiceNow state codes for incidents: 1=New, 2=InProgress, 3=OnHold, 6=Resolved, 7=Closed
INCIDENT_OPEN_STATES = {"1", "2", "3", "New", "In Progress", "On Hold"}
INCIDENT_CLOSED_STATES = {"6", "7", "Resolved", "Closed"}

# Change request state: -5=New, -4=Assess, -3=Authorize, -2=Scheduled, -1=Implement, 0=Review, 3=Closed
CHANGE_OPEN_STATES = {"-5", "-4", "-3", "-2", "-1", "0",
                       "New", "Assess", "Authorize", "Scheduled", "Implement", "Review"}


class ServiceNowConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.snow = ServiceNowClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        incidents = self.snow.get_incidents()
        changes = self.snow.get_change_requests()
        problems = self.snow.get_problems()

        return [
            {
                "_type": "snow_bundle",
                "incidents": incidents,
                "changes": changes,
                "problems": problems,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        incidents = bundle["incidents"]
        changes = bundle["changes"]
        problems = bundle["problems"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.25 — Incident response ────────────────────────────────────────
        by_state: dict[str, int] = Counter(
            str(i.get("state", {}).get("value", i.get("state", "Unknown")))
            for i in incidents
        )
        by_priority: dict[str, int] = Counter(
            str(i.get("priority", {}).get("display_value", i.get("priority", "Unknown")))
            for i in incidents
        )
        by_category: dict[str, int] = Counter(
            str(i.get("category", {}).get("display_value", i.get("category", "Unknown")))
            for i in incidents
        )

        p1_p2 = sum(
            1 for i in incidents
            if str(i.get("priority", {}).get("value", i.get("priority", ""))) in ("1", "2")
        )
        open_count = sum(
            1 for i in incidents
            if str(i.get("state", {}).get("value", i.get("state", ""))) in INCIDENT_OPEN_STATES
        )

        # Resolution time estimation: look at recently closed incidents
        resolved = [
            i for i in incidents
            if i.get("resolved_at") and i.get("opened_at")
        ]

        incident_status = "compliant"
        if p1_p2 > 5:
            incident_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.5.24-28",
            title=(
                f"ServiceNow incidents ({_lookback_label(self.snow._lookback_days)}): "
                f"{len(incidents)} total, {open_count} open, {p1_p2} P1/P2"
            ),
            source_ref="snow-incident-summary",
            classification="incident",
            status=incident_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "lookback_days": self.snow._lookback_days,
                "total_incidents": len(incidents),
                "open_count": open_count,
                "p1_p2_count": p1_p2,
                "resolved_in_window": len(resolved),
                "by_state": dict(by_state),
                "by_priority": dict(by_priority),
                "by_category": dict(by_category),
                "problems_total": len(problems),
                "recent_incidents": [
                    {
                        "number": i.get("number"),
                        "description": i.get("short_description", ""),
                        "priority": i.get("priority", {}).get("display_value", i.get("priority", "")),
                        "state": i.get("state", {}).get("display_value", i.get("state", "")),
                        "opened": i.get("opened_at"),
                        "resolved": i.get("resolved_at"),
                    }
                    for i in incidents[:50]
                ],
            },
        ))

        # ── A.8.32 — Change management ────────────────────────────────────────
        by_change_state: dict[str, int] = Counter(
            str(c.get("state", {}).get("display_value", c.get("state", "Unknown")))
            for c in changes
        )
        by_type: dict[str, int] = Counter(
            str(c.get("type", {}).get("display_value", c.get("type", "Unknown")))
            for c in changes
        )
        by_risk: dict[str, int] = Counter(
            str(c.get("risk", {}).get("display_value", c.get("risk", "Unknown")))
            for c in changes
        )

        pending_approval = [
            c for c in changes
            if str(c.get("approval", {}).get("value", c.get("approval", ""))) in
            ("requested", "Requested")
        ]
        open_changes = sum(
            1 for c in changes
            if str(c.get("state", {}).get("display_value", c.get("state", ""))) in CHANGE_OPEN_STATES
        )
        high_risk = sum(
            1 for c in changes
            if str(c.get("risk", {}).get("value", c.get("risk", ""))) in ("1", "High")
        )

        change_status = "compliant" if not pending_approval else "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.32",
            title=(
                f"ServiceNow changes ({_lookback_label(self.snow._lookback_days)}): "
                f"{len(changes)} total, {open_changes} in-flight, "
                f"{len(pending_approval)} pending approval, {high_risk} high-risk"
            ),
            source_ref="snow-change-summary",
            classification="change",
            status=change_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "lookback_days": self.snow._lookback_days,
                "total_changes": len(changes),
                "open_changes": open_changes,
                "pending_approval": len(pending_approval),
                "high_risk_count": high_risk,
                "by_state": dict(by_change_state),
                "by_type": dict(by_type),
                "by_risk": dict(by_risk),
                "pending_approval_list": [
                    {
                        "number": c.get("number"),
                        "description": c.get("short_description", ""),
                        "type": c.get("type", {}).get("display_value", c.get("type", "")),
                        "risk": c.get("risk", {}).get("display_value", c.get("risk", "")),
                        "created": c.get("sys_created_on"),
                    }
                    for c in pending_approval[:20]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("ServiceNow connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting ServiceNow sync (last_run=%s)", since or "never")

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


def _lookback_label(days: int) -> str:
    return f"last {days}d"


if __name__ == "__main__":
    ServiceNowConnector().run()
