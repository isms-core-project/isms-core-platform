"""Generic SIEM connector — works with any REST API SIEM by configuring endpoints and auth.

Tested with: Splunk (REST API), IBM QRadar, Elastic SIEM, Logpoint, ArcSight
Use source_system='siem' when registering this connector.

Maps to:
  a.8.15  — Logging and monitoring (alert/event counts)
  a.8.16  — Monitoring activities (active incidents)

Env vars (or config keys via GUI):
  ISMS_API_URL            — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN          — connector bearer token from /admin/connectors/register
  SIEM_BASE_URL           — e.g. https://splunk.corp.local:8089 or https://qradar.corp.local
  SIEM_AUTH_TYPE          — api_key | basic | token_endpoint (default: api_key)
  SIEM_API_KEY            — API key / token
  SIEM_USERNAME           — for basic/token_endpoint auth
  SIEM_PASSWORD           — for basic/token_endpoint auth
  SIEM_TOKEN_URL          — token endpoint for OAuth2 auth
  SIEM_ALERTS_ENDPOINT    — path to alerts (default: /api/alerts)
  SIEM_VERIFY_SSL         — true/false (default: true)
  POLL_INTERVAL           — seconds (default: 3600)
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from siem_client import SIEMClient

logger = logging.getLogger(__name__)

# Field names used by common SIEMs for alert severity
_SEVERITY_FIELDS = ("severity", "priority", "level", "criticality", "risk_level")

# Field names used by common SIEMs for alert status
_STATUS_FIELDS = ("status", "state", "resolution_status", "workflow_status")

# Severity values that map to non_compliant / warning in our classification
_CRITICAL_VALUES = frozenset({"critical", "high", "p1", "p2", "1", "2", "emergency", "alert"})
_HIGH_VALUES = frozenset({"high", "medium-high", "p2", "2", "warning"})


def _get_field(d: dict, candidates: tuple[str, ...], default: str = "") -> str:
    """Return the first matching field value from a dict, lower-cased."""
    for key in candidates:
        val = d.get(key)
        if val is not None:
            return str(val).lower()
    return default


class SIEMConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.client = SIEMClient(
            base_url=cfg.get("base_url", ""),
            auth_type=cfg.get("auth_type", "api_key"),
            api_key=cfg.get("api_key", ""),
            username=cfg.get("username", ""),
            password=cfg.get("password", ""),
            token_url=cfg.get("token_url", ""),
            alerts_endpoint=cfg.get("alerts_endpoint", "/api/alerts"),
            events_endpoint=cfg.get("events_endpoint", "/api/events"),
            verify_ssl=cfg.get("verify_ssl", True),
        )

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — SIEM state is always current."""
        alerts = self.client.get_alerts(200)
        summary = self.client.get_summary()
        return [
            {
                "_type": "siem_bundle",
                "alerts": alerts,
                "summary": summary,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        alerts = bundle["alerts"]
        summary = bundle["summary"]
        fetched_at = bundle["fetched_at"]

        total = len(alerts)

        # ── Severity counts (best-effort across SIEM field name variants) ─────
        by_severity: Counter[str] = Counter(
            _get_field(a, _SEVERITY_FIELDS, "unknown")
            for a in alerts
        )
        critical_count = sum(
            count for sev, count in by_severity.items()
            if sev in _CRITICAL_VALUES
        )
        high_count = sum(
            count for sev, count in by_severity.items()
            if sev in _HIGH_VALUES and sev not in _CRITICAL_VALUES
        )

        # ── Status counts (best-effort across SIEM field name variants) ───────
        by_status: Counter[str] = Counter(
            _get_field(a, _STATUS_FIELDS, "unknown")
            for a in alerts
        )
        # "open" equivalents
        open_count = sum(
            count for st, count in by_status.items()
            if st in ("open", "new", "active", "in_progress", "pending", "unresolved")
        )
        # "resolved" equivalents
        resolved_count = sum(
            count for st, count in by_status.items()
            if st in ("closed", "resolved", "dismissed", "archived", "done", "completed")
        )

        # ── A.8.15 — Logging and monitoring ───────────────────────────────────
        classification_8_15 = "compliant"
        if critical_count > 0:
            classification_8_15 = "non_compliant"
        elif high_count > 0:
            classification_8_15 = "warning"

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"SIEM alert log: {total} alerts "
                f"({critical_count + high_count} high severity)"
            ),
            source_ref="siem-alert-log",
            classification=classification_8_15,
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_alert_count": total,
                "by_severity": dict(by_severity),
                "critical_high_count": critical_count + high_count,
                "critical_count": critical_count,
                "high_count": high_count,
                "recent_alerts": [
                    {
                        "id": a.get("id") or a.get("alert_id") or a.get("incident_id"),
                        "title": a.get("title") or a.get("name") or a.get("description"),
                        "severity": _get_field(a, _SEVERITY_FIELDS),
                        "status": _get_field(a, _STATUS_FIELDS),
                        "timestamp": (
                            a.get("timestamp")
                            or a.get("created_at")
                            or a.get("start_time")
                            or a.get("event_time")
                        ),
                    }
                    for a in alerts[:20]
                ],
            },
        ))

        # ── A.8.16 — Monitoring activities ────────────────────────────────────
        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"SIEM monitoring: {open_count} open / {resolved_count} resolved alerts"
            ),
            source_ref="siem-monitoring-status",
            classification="compliant" if open_count == 0 else ("warning" if open_count < 10 else "non_compliant"),
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_alert_count": total,
                "open_count": open_count,
                "resolved_count": resolved_count,
                "by_status": dict(by_status),
                "summary": summary,
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        logger.info("SIEM connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info(
                    "Starting SIEM sync (base_url=%s, last_run=%s)",
                    self.client.base_url,
                    since or "never",
                )

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
    SIEMConnector().run()
