"""Microsoft Sentinel connector for ISMS CORE v2.0.

Pulls from the Sentinel REST API and posts evidence to:
  a.5.7   — Threat intelligence  (incident tactics + threat categories)
  a.8.16  — Monitoring of activities  (analytics rules coverage + incident volume)

Environment variables required:
  ISMS_API_URL                — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN              — connector bearer token from /admin/connectors/register
  SENTINEL_TENANT_ID          — Azure AD tenant ID
  SENTINEL_CLIENT_ID          — App registration client ID
  SENTINEL_CLIENT_SECRET      — App registration client secret
  SENTINEL_SUBSCRIPTION_ID    — Azure subscription ID
  SENTINEL_RESOURCE_GROUP     — Resource group containing the Sentinel workspace
  SENTINEL_WORKSPACE_NAME     — Log Analytics workspace name
  POLL_INTERVAL               — seconds between syncs (default: 3600 = 1h)

Required role: Microsoft Sentinel Reader on the workspace resource group.
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from sentinel_client import SentinelClient

logger = logging.getLogger(__name__)

# Incident severity ordering
SEVERITY_WEIGHT = {"High": 3, "Medium": 2, "Low": 1, "Informational": 0}


class SentinelConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))  # 1h default for SIEM
        cfg = self._load_config()
        self.sentinel = SentinelClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Sentinel state is always current."""
        incidents = self.sentinel.get_incidents()
        alert_rules = self.sentinel.get_alert_rules()
        data_connectors = self.sentinel.get_data_connectors()

        return [
            {
                "_type": "sentinel_bundle",
                "incidents": incidents,
                "alert_rules": alert_rules,
                "data_connectors": data_connectors,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        incidents = bundle["incidents"]
        alert_rules = bundle["alert_rules"]
        data_connectors = bundle["data_connectors"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.16 — Monitoring coverage ──────────────────────────────────────
        enabled_rules = [
            r for r in alert_rules
            if r.get("properties", {}).get("enabled", False)
        ]
        disabled_rules = len(alert_rules) - len(enabled_rules)

        open_incidents = [
            i for i in incidents
            if i.get("properties", {}).get("status") not in ("Closed", "Dismissed")
        ]
        by_severity: dict[str, int] = Counter(
            i.get("properties", {}).get("severity", "Unknown")
            for i in open_incidents
        )

        high_count = by_severity.get("High", 0)
        medium_count = by_severity.get("Medium", 0)

        monitoring_status = "compliant"
        if high_count > 0:
            monitoring_status = "attention-required"
        if disabled_rules > len(enabled_rules) // 2:  # >50% rules disabled
            monitoring_status = "non-compliant"

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"Sentinel monitoring: {len(enabled_rules)}/{len(alert_rules)} rules active, "
                f"{len(open_incidents)} open incidents "
                f"({high_count} high, {medium_count} medium)"
            ),
            source_ref="sentinel-monitoring-status",
            classification="incident",
            status=monitoring_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "monitoring_status": monitoring_status,
                "alert_rules": {
                    "total": len(alert_rules),
                    "enabled": len(enabled_rules),
                    "disabled": disabled_rules,
                },
                "data_connectors": {
                    "total": len(data_connectors),
                    "names": [
                        c.get("properties", {}).get("connectorUiConfig", {}).get("title", c.get("name", ""))
                        for c in data_connectors
                    ],
                },
                "open_incidents": {
                    "total": len(open_incidents),
                    "by_severity": dict(by_severity),
                },
                "all_incidents_total": len(incidents),
            },
        ))

        # ── A.5.7 — Threat intelligence (incident tactics) ────────────────────
        # Extract MITRE ATT&CK tactics from all incidents
        all_tactics: list[str] = []
        for i in incidents:
            props = i.get("properties", {})
            tactics = props.get("tactics", [])
            all_tactics.extend(tactics)

        tactic_counts: dict[str, int] = Counter(all_tactics)
        high_severity_incidents = [
            i for i in incidents
            if i.get("properties", {}).get("severity") == "High"
        ]

        # Threat intelligence status
        ti_status = "active"
        if tactic_counts:
            ti_status = "attention-required" if high_severity_incidents else "active"

        items.append(EvidenceItem(
            group_code="a.5.7",
            title=(
                f"Sentinel threat intelligence: {len(incidents)} incidents, "
                f"{len(tactic_counts)} distinct ATT&CK tactics observed, "
                f"{len(high_severity_incidents)} high severity"
            ),
            source_ref="sentinel-threat-intelligence",
            classification="incident",
            status=ti_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_incidents": len(incidents),
                "high_severity_incidents": len(high_severity_incidents),
                "tactic_distribution": dict(tactic_counts),
                "top_incidents": [
                    {
                        "title": i.get("properties", {}).get("title"),
                        "severity": i.get("properties", {}).get("severity"),
                        "status": i.get("properties", {}).get("status"),
                        "tactics": i.get("properties", {}).get("tactics", []),
                        "created": i.get("properties", {}).get("createdTimeUtc"),
                    }
                    for i in high_severity_incidents[:20]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Sentinel connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Sentinel sync (last_run=%s)", since or "never")

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
    SentinelConnector().run()
