"""Microsoft Purview connector for ISMS CORE v2.0.

Pulls from Microsoft Graph (Information Protection + Records Management) and
optionally from the Purview Data Plane, then posts evidence to:

  a.8.10 — Information deletion          (retention labels + lifecycle settings)
  a.8.12 — Data leakage prevention       (DLP alerts, sensitivity label coverage)

Required Graph application permissions (same App Registration as other Microsoft connectors):
  InformationProtectionPolicy.Read.All   — sensitivity label inventory
  RecordsManagement.Read.All             — retention labels
  SecurityEvents.Read.All                — Purview DLP / IP security alerts

Optional (for data catalogue evidence — requires PURVIEW_ACCOUNT):
  Purview Data Curator role on the Purview account
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from purview_client import PurviewClient

logger = logging.getLogger(__name__)


class PurviewConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))  # 24h
        cfg = self._load_config()
        self.purview = PurviewClient(**cfg)

    # ── fetch — all data in one bundle ───────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        sensitivity_labels = self.purview.get_sensitivity_labels()
        retention_labels   = self.purview.get_retention_labels()
        dlp_alerts         = self.purview.get_dlp_alerts()
        collections        = self.purview.get_collections()
        classification_rules = self.purview.get_classification_rules()

        return [
            {
                "_type": "purview_bundle",
                "sensitivity_labels":   sensitivity_labels,
                "retention_labels":     retention_labels,
                "dlp_alerts":           dlp_alerts,
                "collections":          collections,
                "classification_rules": classification_rules,
                "fetched_at":           datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        sensitivity_labels   = bundle["sensitivity_labels"]
        retention_labels     = bundle["retention_labels"]
        dlp_alerts           = bundle["dlp_alerts"]
        collections          = bundle["collections"]
        classification_rules = bundle["classification_rules"]
        fetched_at           = bundle["fetched_at"]

        # ── A.8.12 — Sensitivity labels (DLP evidence) ───────────────────────
        if sensitivity_labels:
            published = [l for l in sensitivity_labels if l.get("isActive", True)]
            items.append(EvidenceItem(
                group_code="a.8.12",
                title=(
                    f"Purview sensitivity labels: {len(sensitivity_labels)} defined "
                    f"({len(published)} active)"
                ),
                source_ref="purview-sensitivity-labels",
                classification="policy",
                status="compliant" if sensitivity_labels else "non-compliant",
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "total_labels": len(sensitivity_labels),
                    "active_labels": len(published),
                    "labels": [
                        {
                            "id": l.get("id"),
                            "name": l.get("name"),
                            "description": l.get("description", ""),
                            "sensitivity_order": l.get("sensitivityOrder"),
                            "is_active": l.get("isActive", True),
                            "tooltip": l.get("tooltip", ""),
                        }
                        for l in sensitivity_labels
                    ],
                },
            ))
        else:
            logger.warning("No sensitivity labels returned (check InformationProtectionPolicy.Read.All)")

        # ── A.8.12 — DLP alerts ───────────────────────────────────────────────
        if dlp_alerts is not None:
            open_alerts   = [a for a in dlp_alerts if a.get("status", "").lower() not in ("resolved", "dismissed")]
            high_alerts   = [a for a in dlp_alerts if a.get("severity", "").lower() in ("high", "critical")]
            alert_status  = (
                "non-compliant" if high_alerts
                else "attention-required" if open_alerts
                else "compliant"
            )
            items.append(EvidenceItem(
                group_code="a.8.12",
                title=(
                    f"Purview DLP alerts: {len(dlp_alerts)} total "
                    f"({len(open_alerts)} open, {len(high_alerts)} high/critical)"
                ),
                source_ref="purview-dlp-alerts",
                classification="incident",
                status=alert_status,
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "total_alerts": len(dlp_alerts),
                    "open_alerts": len(open_alerts),
                    "high_critical_alerts": len(high_alerts),
                    "alerts": [
                        {
                            "id": a.get("id"),
                            "title": a.get("title"),
                            "severity": a.get("severity"),
                            "status": a.get("status"),
                            "service_source": a.get("serviceSource"),
                            "category": a.get("category"),
                            "created_datetime": a.get("createdDateTime"),
                        }
                        for a in dlp_alerts[:100]
                    ],
                },
            ))

        # ── A.8.10 — Retention labels (information lifecycle) ─────────────────
        if retention_labels:
            # Categorise by retention action
            auto_apply    = [l for l in retention_labels if l.get("labelToBeApplied") == "autoApply"]
            record_labels = [l for l in retention_labels if l.get("isRecordLabel", False)]
            items.append(EvidenceItem(
                group_code="a.8.10",
                title=(
                    f"Purview retention labels: {len(retention_labels)} defined "
                    f"({len(record_labels)} record labels, {len(auto_apply)} auto-apply)"
                ),
                source_ref="purview-retention-labels",
                classification="policy",
                status="compliant" if retention_labels else "non-compliant",
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "total_labels": len(retention_labels),
                    "record_labels": len(record_labels),
                    "auto_apply_labels": len(auto_apply),
                    "labels": [
                        {
                            "id": l.get("id"),
                            "display_name": l.get("displayName"),
                            "description": l.get("descriptionForUsers", ""),
                            "retention_trigger": l.get("retentionTrigger"),
                            "retention_duration": l.get("retentionDuration"),
                            "behavior_during_retention": l.get("behaviorDuringRetentionPeriod"),
                            "action_after_retention": l.get("actionAfterRetentionPeriod"),
                            "is_record_label": l.get("isRecordLabel", False),
                        }
                        for l in retention_labels
                    ],
                },
            ))
        else:
            logger.warning("No retention labels returned (check RecordsManagement.Read.All)")

        # ── A.8.12 — Purview Data Catalogue (if configured) ───────────────────
        if collections:
            items.append(EvidenceItem(
                group_code="a.8.12",
                title=(
                    f"Purview data catalogue: {len(collections)} collections, "
                    f"{len(classification_rules)} classification rules"
                ),
                source_ref="purview-data-catalogue",
                classification="asset",
                status="active",
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "collections": [
                        {
                            "name": c.get("name"),
                            "friendly_name": c.get("friendlyName"),
                            "description": c.get("description", ""),
                            "parent_collection": c.get("parentCollection", {}).get("referenceName"),
                        }
                        for c in collections
                    ],
                    "classification_rules": len(classification_rules),
                },
            ))

        return items

    def run(self) -> None:
        logger.info("Purview connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Purview sync (last_run=%s)", since or "never")

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
    PurviewConnector().run()
