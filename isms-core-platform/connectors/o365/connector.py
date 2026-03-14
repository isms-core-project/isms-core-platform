"""Microsoft 365 Security connector for ISMS CORE v2.0.

Pulls from Microsoft Graph Security API and posts evidence to:
  a.5.15-16-18 — Identity and Access Management  (Conditional Access policies)
  a.8.1-7-18-19 — Security Monitoring             (security alerts / incidents / Defender)
  a.8.5        — Authentication Controls          (Secure Score overall + identity controls)
  a.8.7        — Malware Protection               (Defender for Endpoint alerts by category)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  M365_TENANT_ID        — Azure AD tenant ID (falls back to ENTRA_TENANT_ID)
  M365_CLIENT_ID        — App registration client ID (falls back to ENTRA_CLIENT_ID)
  M365_CLIENT_SECRET    — App registration client secret (falls back to ENTRA_CLIENT_SECRET)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

Graph API permissions required (Application):
  SecurityAlert.Read.All
  SecurityEvents.Read.All
  ThreatIndicators.Read.All      (optional — additional intel sources)
  Policy.Read.All                (optional — Conditional Access; 403 handled gracefully)
"""

import logging
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from m365_client import M365Client

logger = logging.getLogger(__name__)

# Secure Score thresholds (percentageScore is 0–100)
_SCORE_COMPLIANT = 70
_SCORE_WARNING = 40

# High-severity alert count thresholds for classification
_ALERT_HIGH_NONCOMPLIANT = 10
_ALERT_HIGH_WARNING = 1


class O365Connector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = M365Client(**cfg)

    # ── fetch — pulls all data from Graph Security (full sync each run) ───────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull Secure Score, alerts, and Conditional Access policies."""
        secure_score = self.client.get_secure_score()
        alerts = self.client.get_alerts(top=200)
        ca_policies = self.client.get_conditional_access_policies()

        return [
            {
                "_type": "o365_bundle",
                "secure_score": secure_score,
                "alerts": alerts,
                "ca_policies": ca_policies,
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        secure_score = bundle["secure_score"]
        alerts = bundle["alerts"]
        ca_policies = bundle["ca_policies"]

        # ── A.8.5 — Secure Score summary ──────────────────────────────────────
        if secure_score:
            current = secure_score.get("currentScore", 0)
            maximum = secure_score.get("maxScore", 0)
            pct = secure_score.get("percentageScore", 0)

            if pct >= _SCORE_COMPLIANT:
                score_classification = "compliant"
            elif pct >= _SCORE_WARNING:
                score_classification = "warning"
            else:
                score_classification = "non_compliant"

            # Top 10 control scores sorted by earned score descending
            control_scores = secure_score.get("controlScores", [])
            top_controls = sorted(
                control_scores,
                key=lambda c: c.get("score", 0),
                reverse=True,
            )[:10]

            items.append(EvidenceItem(
                group_code="a.8.2-3-5",
                title=f"Microsoft 365 Secure Score: {current}/{maximum} ({pct:.1f}%)",
                source_ref="m365-secure-score",
                classification=score_classification,
                status="active",
                raw={
                    "current_score": current,
                    "max_score": maximum,
                    "percentage_score": pct,
                    "created_date_time": secure_score.get("createdDateTime"),
                    "azure_tenant_id": secure_score.get("azureTenantId"),
                    "top_controls": [
                        {
                            "control_name": c.get("controlName"),
                            "control_category": c.get("controlCategory"),
                            "score": c.get("score"),
                            "description": c.get("description"),
                        }
                        for c in top_controls
                    ],
                },
            ))
        else:
            logger.warning("No Secure Score data — skipping a.8.5 evidence")

        # ── A.8.1-7-18-19 — Security alert summary ────────────────────────────
        total_alerts = len(alerts)
        by_severity: dict[str, int] = Counter(
            a.get("severity", "unknown").lower() for a in alerts
        )
        by_status: dict[str, int] = Counter(
            a.get("status", "unknown").lower() for a in alerts
        )
        by_service: dict[str, int] = Counter(
            a.get("serviceSource", "unknown") for a in alerts
        )

        high_count = by_severity.get("high", 0)
        medium_count = by_severity.get("medium", 0)
        open_count = by_status.get("new", 0) + by_status.get("inProgress", 0)

        if high_count >= _ALERT_HIGH_NONCOMPLIANT:
            alert_classification = "non_compliant"
        elif high_count >= _ALERT_HIGH_WARNING:
            alert_classification = "warning"
        else:
            alert_classification = "compliant"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"M365 security alerts: {total_alerts} total "
                f"({high_count} high, {medium_count} medium, {open_count} open)"
            ),
            source_ref="m365-security-alerts",
            classification=alert_classification,
            status="active",
            raw={
                "total": total_alerts,
                "by_severity": dict(by_severity),
                "by_status": dict(by_status),
                "by_service": dict(by_service),
                "recent_alerts": [
                    {
                        "id": a.get("id"),
                        "title": a.get("title"),
                        "severity": a.get("severity"),
                        "status": a.get("status"),
                        "category": a.get("category"),
                        "service_source": a.get("serviceSource"),
                        "created_date_time": a.get("createdDateTime"),
                    }
                    for a in alerts[:20]
                ],
            },
        ))

        # ── A.5.15-16-18 — Conditional Access policies ────────────────────────
        total_ca = len(ca_policies)
        enabled = sum(1 for p in ca_policies if p.get("state") == "enabled")
        disabled = sum(1 for p in ca_policies if p.get("state") == "disabled")
        reporting_only = sum(
            1 for p in ca_policies
            if p.get("state") == "enabledForReportingButNotEnforced"
        )

        ca_classification = "compliant" if enabled > 0 else "warning"

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"Conditional Access: {total_ca} policies "
                f"({enabled} enabled, {disabled} disabled)"
            ),
            source_ref="m365-conditional-access",
            classification=ca_classification,
            status="active",
            raw={
                "total": total_ca,
                "enabled": enabled,
                "disabled": disabled,
                "reporting_only": reporting_only,
                "policies": [
                    {
                        "id": p.get("id"),
                        "display_name": p.get("displayName"),
                        "state": p.get("state"),
                        "created_date_time": p.get("createdDateTime"),
                        "modified_date_time": p.get("modifiedDateTime"),
                    }
                    for p in ca_policies
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("O365 connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting M365 sync (last_run=%s)", since or "never")

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
    O365Connector().run()
