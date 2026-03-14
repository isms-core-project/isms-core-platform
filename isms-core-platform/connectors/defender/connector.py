"""Microsoft Defender for Endpoint connector for ISMS CORE v2.0.

Pulls from the Defender for Endpoint API and posts evidence to:
  a.8.1-7-18-19 — Endpoint Security            (endpoint inventory + AV health)
  a.8.8         — Management of Technical Vulnerabilities  (CVE counts + severity)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  DEFENDER_TENANT_ID        — Azure AD tenant ID
  DEFENDER_CLIENT_ID        — App registration client ID
  DEFENDER_CLIENT_SECRET    — App registration client secret
  POLL_INTERVAL             — seconds between syncs (default: 86400 = 24h)

App Registration permissions required (Application):
  Machine.Read.All
  Vulnerability.Read.All
  Alert.Read.All
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from defender_client import DefenderClient, SEVERITY_WEIGHT

logger = logging.getLogger(__name__)


class DefenderConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.defender = DefenderClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Defender data is always current state."""
        machines = self.defender.get_machines()
        alerts = self.defender.get_alerts()
        recommendations = self.defender.get_recommendations()

        return [
            {
                "_type": "defender_bundle",
                "machines": machines,
                "alerts": alerts,
                "recommendations": recommendations,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        machines = bundle["machines"]
        alerts = bundle["alerts"]
        recommendations = bundle["recommendations"]
        fetched_at = bundle["fetched_at"]

        active_machines = [m for m in machines if m.get("onboardingStatus") == "Onboarded"]

        # ── A.8.1-7-18-19 — Endpoint inventory ───────────────────────────────
        by_os: dict[str, int] = Counter(m.get("osPlatform", "Unknown") for m in active_machines)
        by_health: dict[str, int] = Counter(m.get("healthStatus", "Unknown") for m in active_machines)
        by_risk: dict[str, int] = Counter(m.get("riskScore", "None") for m in active_machines)

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"Defender endpoint inventory: {len(active_machines)} onboarded devices "
                f"({by_health.get('Active', 0)} active, "
                f"{by_health.get('Inactive', 0)} inactive)"
            ),
            source_ref="defender-endpoint-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_machines": len(machines),
                "onboarded": len(active_machines),
                "by_os": dict(by_os),
                "by_health_status": dict(by_health),
                "by_risk_score": dict(by_risk),
                "machines": [
                    {
                        "id": m.get("id"),
                        "name": m.get("computerDnsName"),
                        "os": m.get("osPlatform"),
                        "health": m.get("healthStatus"),
                        "risk": m.get("riskScore"),
                        "exposure": m.get("exposureLevel"),
                        "last_seen": m.get("lastSeen"),
                        "group": m.get("groupName"),
                        "aad_joined": m.get("isAadJoined"),
                    }
                    for m in active_machines
                ],
            },
        ))

        # ── A.8.1-7-18-19 — Protection against malware (endpoint health) ──────
        inactive = by_health.get("Inactive", 0)
        misconfigured = by_health.get("ImpairedCommunication", 0) + by_health.get("SensorDataMissing", 0)
        high_risk = by_risk.get("High", 0)
        critical_risk = by_risk.get("Critical", 0)

        open_alerts = [a for a in alerts if a.get("status") not in ("Resolved", "Suppressed")]
        malware_alerts = [
            a for a in open_alerts
            if a.get("category") in ("Malware", "UnwantedSoftware", "Ransomware")
        ]
        by_alert_severity: dict[str, int] = Counter(a.get("severity", "Unknown") for a in open_alerts)

        health_status = "compliant"
        if critical_risk > 0 or malware_alerts:
            health_status = "non-compliant"
        elif inactive > 0 or high_risk > 0 or misconfigured > 0:
            health_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"Defender endpoint health: {len(active_machines)} endpoints — "
                f"{inactive} inactive, {misconfigured} misconfigured, "
                f"{len(open_alerts)} open alerts ({len(malware_alerts)} malware)"
            ),
            source_ref="defender-endpoint-health",
            classification="asset",
            status=health_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_onboarded": len(active_machines),
                "inactive_count": inactive,
                "misconfigured_count": misconfigured,
                "risk_distribution": dict(by_risk),
                "high_risk_count": high_risk,
                "critical_risk_count": critical_risk,
                "open_alerts_total": len(open_alerts),
                "malware_alerts": len(malware_alerts),
                "alerts_by_severity": dict(by_alert_severity),
                "malware_alert_list": [
                    {
                        "title": a.get("title"),
                        "severity": a.get("severity"),
                        "machine": a.get("computerDnsName"),
                        "category": a.get("category"),
                        "created": a.get("alertCreationTime"),
                    }
                    for a in malware_alerts[:20]
                ],
            },
        ))

        # ── A.8.8 — Vulnerability management ─────────────────────────────────
        # Use recommendations as proxy for CVE exposure
        # (vuln summary endpoint requires separate query)
        active_recs = [r for r in recommendations if r.get("status") == "Active"]
        by_sev: dict[str, int] = Counter(r.get("severity", "Unknown") for r in active_recs)
        critical_recs = [r for r in active_recs if r.get("severity") == "Critical"]
        exposed_machines: set = set()
        for r in active_recs:
            count = r.get("exposedMachinesCount", 0)
            if count:
                exposed_machines.add(r.get("id"))

        vuln_status = "compliant"
        if critical_recs:
            vuln_status = "non-compliant"
        elif by_sev.get("High", 0) > 0:
            vuln_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Defender vulnerability status: {len(active_recs)} active recommendations "
                f"({by_sev.get('Critical', 0)} critical, "
                f"{by_sev.get('High', 0)} high, "
                f"{by_sev.get('Medium', 0)} medium)"
            ),
            source_ref="defender-vulnerability-status",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_recommendations": len(active_recs),
                "by_severity": dict(by_sev),
                "critical_recommendations": [
                    {
                        "name": r.get("recommendationName"),
                        "exposed_machines": r.get("exposedMachinesCount"),
                        "remediation_type": r.get("remediationType"),
                    }
                    for r in critical_recs[:20]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Defender connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Defender sync (last_run=%s)", since or "never")

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
    DefenderConnector().run()
