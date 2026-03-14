"""Qualys VMDR connector for ISMS CORE v2.0.

Pulls from the Qualys Vulnerability Management, Detection and Response API
and posts evidence to:
  a.8.8  — Management of Technical Vulnerabilities  (vuln counts by severity, scan history)
  a.5.9  — Inventory of Information and Other Associated Assets  (asset count)

Environment variables required:
  ISMS_API_URL      — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN    — connector bearer token from /admin/connectors/register
  QUALYS_URL        — Platform API URL, e.g. https://qualysapi.qg2.apps.qualys.com
  QUALYS_USERNAME   — Qualys username (read-only service account recommended)
  QUALYS_PASSWORD   — Qualys password
  POLL_INTERVAL     — seconds between syncs (default: 86400 = 24h)

Qualys platform URLs by region:
  US1:  https://qualysapi.qualys.com
  US2:  https://qualysapi.qg2.apps.qualys.com
  US3:  https://qualysapi.qg3.apps.qualys.com
  EU1:  https://qualysapi.qualys.eu
  UK1:  https://qualysapi.qg1.apps.qualys.co.uk
  India: https://qualysapi.qg1.apps.qualys.in
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from qualys_client import QualysClient

logger = logging.getLogger(__name__)


class QualysConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.qualys = QualysClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Qualys data represents current state."""
        asset_count = self.qualys.get_asset_count()
        host_summary = self.qualys.get_host_list_summary()
        vuln_counts = self.qualys.get_vuln_counts_by_severity()
        scan_history = self.qualys.get_scan_history()

        return [{
            "_type": "qualys_bundle",
            "asset_count": asset_count,
            "host_summary": host_summary,
            "vuln_counts": vuln_counts,
            "scan_history": scan_history,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        asset_count = bundle["asset_count"]
        host_summary = bundle["host_summary"]
        vuln_counts = bundle["vuln_counts"]
        scan_history = bundle["scan_history"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.8 — Technical vulnerability management ──────────────────────
        total_vulns = vuln_counts.get("total", 0)
        active_vulns = vuln_counts.get("active", 0)

        # Scan coverage
        recent_scans = scan_history[:20]
        completed_scans = [s for s in recent_scans if s.get("status", "").lower() in ("finished", "complete")]
        scanning_ips = host_summary.get("total_hosts", asset_count)

        # Compliance status based on active finding counts
        if total_vulns == 0:
            vuln_status = "compliant"
        elif total_vulns <= 50:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Qualys VMDR vulnerability summary: {total_vulns} active findings "
                f"across {scanning_ips} hosts in scope"
            ),
            source_ref="qualys-vulnerability-summary",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "vulnerabilities": {
                    "total_active": active_vulns,
                },
                "hosts_in_scope": scanning_ips,
                "scan_history": {
                    "total_scans": len(scan_history),
                    "completed_scans": len(completed_scans),
                    "recent_scans": [
                        {
                            "ref": s.get("ref"),
                            "title": s.get("title"),
                            "type": s.get("type"),
                            "status": s.get("status"),
                            "launch_date": s.get("launch_date"),
                            "target": s.get("target"),
                        }
                        for s in recent_scans[:10]
                    ],
                },
            },
        ))

        # ── A.5.9 — Asset inventory ──────────────────────────────────────────
        total_assets = asset_count or host_summary.get("total_hosts", 0)

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"Qualys asset inventory: {total_assets} assets in vulnerability management scope"
            ),
            source_ref="qualys-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "assets": {
                    "total": total_assets,
                    "host_list_total": host_summary.get("total_hosts", 0),
                    "asset_manager_total": asset_count,
                },
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Qualys VMDR connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Qualys sync (last_run=%s)", since or "never")

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
    QualysConnector().run()
