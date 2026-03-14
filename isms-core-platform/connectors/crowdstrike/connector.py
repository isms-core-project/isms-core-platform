"""CrowdStrike Falcon connector for ISMS CORE v2.0.

Pulls from the CrowdStrike Falcon REST API and posts evidence to:
  a.8.1-7-18-19 — Endpoint Security            (device inventory + detections)
  a.8.8         — Management of Technical Vulnerabilities  (prevention policies)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  CROWDSTRIKE_CLIENT_ID     — OAuth2 client ID
  CROWDSTRIKE_CLIENT_SECRET — OAuth2 client secret
  CROWDSTRIKE_BASE_URL      — optional; default https://api.crowdstrike.com
  POLL_INTERVAL             — seconds between syncs (default: 86400 = 24h)

API permissions required:
  Devices:Read
  Alerts:Read (replaces deprecated Detections:Read)
  Prevention Policies:Read
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from crowdstrike_client import CrowdStrikeClient

logger = logging.getLogger(__name__)


class CrowdStrikeConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.cs = CrowdStrikeClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — CrowdStrike data is always current state."""
        devices = self.cs.get_devices()
        alerts = self.cs.get_alerts()
        prevention_policies = self.cs.get_prevention_policies()

        return [
            {
                "_type": "crowdstrike_bundle",
                "devices": devices,
                "alerts": alerts,
                "prevention_policies": prevention_policies,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        alerts = bundle["alerts"]
        prevention_policies = bundle["prevention_policies"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1-7-18-19 — Device inventory ─────────────────────────────────
        by_platform: dict[str, int] = Counter(
            d.get("platform_name", "Unknown") for d in devices
        )
        reduced_fn = [
            d for d in devices
            if d.get("reduced_functionality_mode") not in (None, "no", "No", False)
        ]
        by_status: dict[str, int] = Counter(
            d.get("status", "Unknown") for d in devices
        )

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"CrowdStrike device inventory: {len(devices)} enrolled devices "
                f"({by_status.get('normal', 0)} normal, "
                f"{len(reduced_fn)} reduced-functionality)"
            ),
            source_ref="crowdstrike-device-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_devices": len(devices),
                "by_platform": dict(by_platform),
                "by_status": dict(by_status),
                "reduced_functionality_count": len(reduced_fn),
                "devices": [
                    {
                        "device_id": d.get("device_id"),
                        "hostname": d.get("hostname"),
                        "platform_name": d.get("platform_name"),
                        "status": d.get("status"),
                        "last_seen": d.get("last_seen"),
                        "reduced_functionality_mode": d.get("reduced_functionality_mode"),
                        "agent_version": d.get("agent_version"),
                        "detection_suppression_status": d.get("detection_suppression_status"),
                    }
                    for d in devices
                ],
            },
        ))

        # ── A.8.1-7-18-19 — Open alerts by severity (Alerts API v2) ──────────
        # Alerts API fields: composite_id, status, severity (string), tactic, technique
        open_alerts = [
            a for a in alerts
            if str(a.get("status", "")).lower() not in ("closed", "false_positive")
        ]
        # Alerts API uses severity as a string: "Critical", "High", "Medium", "Low", "Informational"
        by_severity: dict[str, int] = Counter(
            a.get("severity", "Unknown") for a in open_alerts
        )

        alert_status = "compliant"
        if by_severity.get("Critical", 0) > 0:
            alert_status = "non-compliant"
        elif by_severity.get("High", 0) > 0:
            alert_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"CrowdStrike alerts: {len(open_alerts)} open "
                f"({by_severity.get('Critical', 0)} critical, "
                f"{by_severity.get('High', 0)} high, "
                f"{by_severity.get('Medium', 0)} medium)"
            ),
            source_ref="crowdstrike-alerts",
            classification="incident",
            status=alert_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_alerts": len(alerts),
                "open_alerts": len(open_alerts),
                "by_severity": dict(by_severity),
                "alerts": [
                    {
                        "composite_id": a.get("composite_id"),
                        "status": a.get("status"),
                        "severity": a.get("severity"),
                        "tactic": a.get("tactic"),
                        "technique": a.get("technique"),
                        "timestamp": a.get("timestamp"),
                    }
                    for a in open_alerts[:50]
                ],
            },
        ))

        # ── A.8.8 — Prevention policies ───────────────────────────────────────
        enabled_policies = [p for p in prevention_policies if p.get("enabled")]
        by_platform_pol: dict[str, int] = Counter(
            p.get("platform_name", "Unknown") for p in prevention_policies
        )

        policy_status = "compliant"
        if not prevention_policies:
            policy_status = "non-compliant"
        elif len(enabled_policies) < len(prevention_policies):
            policy_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"CrowdStrike prevention policies: {len(prevention_policies)} configured, "
                f"{len(enabled_policies)} enabled"
            ),
            source_ref="crowdstrike-prevention-policies",
            classification="policy",
            status=policy_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_policies": len(prevention_policies),
                "enabled_policies": len(enabled_policies),
                "disabled_policies": len(prevention_policies) - len(enabled_policies),
                "by_platform": dict(by_platform_pol),
                "policies": [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "platform_name": p.get("platform_name"),
                        "enabled": p.get("enabled"),
                        "groups_count": len(p.get("groups", [])),
                    }
                    for p in prevention_policies
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("CrowdStrike connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting CrowdStrike sync (last_run=%s)", since or "never")

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
    CrowdStrikeConnector().run()
