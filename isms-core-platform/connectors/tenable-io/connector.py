"""Tenable Vulnerability Management (Tenable.io) connector for ISMS CORE v2.0.

Pulls from the Tenable cloud API and posts evidence to:
  a.8.8  — Management of Technical Vulnerabilities  (severity breakdown)
  a.5.9  — Inventory of Information and Other Associated Assets  (asset count)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  TENABLE_ACCESS_KEY    — Tenable.io API access key
  TENABLE_SECRET_KEY    — Tenable.io API secret key
  POLL_INTERVAL         — seconds between syncs (default: 86400 = 24h)

API permissions required:
  Can View  — Vulnerability Management, Assets
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from tenable_io_client import TenableIOClient

logger = logging.getLogger(__name__)


class TenableIOConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.tenable = TenableIOClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Tenable.io data represents current state."""
        assets = self.tenable.get_assets()
        vuln_summary = self.tenable.get_vulnerabilities_summary()
        scans = self.tenable.get_scan_list()

        return [{
            "_type": "tenable_io_bundle",
            "assets": assets,
            "vuln_summary": vuln_summary,
            "scans": scans,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        assets = bundle["assets"]
        vuln_summary = bundle["vuln_summary"]
        scans = bundle["scans"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.8 — Technical vulnerability management ──────────────────────
        # Parse severity counts from workbench vulnerability summary
        vuln_list = vuln_summary.get("vulnerabilities", [])
        sev_counts: dict[str, int] = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }
        total_vulns = 0

        for v in vuln_list:
            sev = str(v.get("severity", "")).lower()
            count = int(v.get("count", 0))
            if sev in sev_counts:
                sev_counts[sev] += count
            total_vulns += count

        critical = sev_counts["critical"]
        high = sev_counts["high"]
        medium = sev_counts["medium"]

        # Determine compliance status
        if critical == 0 and high == 0:
            vuln_status = "compliant"
        elif critical == 0 and high <= 10:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        # Scan coverage summary
        completed_scans = [s for s in scans if s.get("status") == "completed"]
        scan_names = [s.get("name", "") for s in completed_scans[:10]]

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Tenable.io vulnerability summary: {total_vulns} total "
                f"({critical} critical, {high} high, {medium} medium)"
            ),
            source_ref="tenable-io-vulnerability-summary",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "vulnerabilities": {
                    "total": total_vulns,
                    "by_severity": sev_counts,
                },
                "scan_coverage": {
                    "total_scans": len(scans),
                    "completed_scans": len(completed_scans),
                    "recent_scan_names": scan_names,
                },
                "top_vulnerabilities": [
                    {
                        "plugin_id": v.get("plugin_id"),
                        "plugin_name": v.get("plugin_name"),
                        "severity": v.get("severity"),
                        "count": v.get("count"),
                    }
                    for v in vuln_list[:30]
                ],
            },
        ))

        # ── A.5.9 — Asset inventory ──────────────────────────────────────────
        total_assets = len(assets)

        # Group by OS family
        os_counter: Counter = Counter()
        for a in assets:
            os_list = a.get("operating_systems") or []
            if os_list:
                os_counter[os_list[0]] += 1
            else:
                os_counter["Unknown"] += 1

        # Last-seen distribution
        seen_today = 0
        seen_week = 0
        seen_older = 0
        for a in assets:
            last_seen = a.get("last_seen", "")
            if last_seen:
                try:
                    ts = datetime.fromisoformat(last_seen.replace("Z", "+00:00"))
                    age_days = (datetime.now(timezone.utc) - ts).days
                    if age_days <= 1:
                        seen_today += 1
                    elif age_days <= 7:
                        seen_week += 1
                    else:
                        seen_older += 1
                except Exception as e:
                    logger.warning("Could not parse last_seen date '%s': %s", last_seen, e)
                    seen_older += 1

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"Tenable.io asset inventory: {total_assets} discovered assets "
                f"({seen_today} seen today, {seen_week} seen this week)"
            ),
            source_ref="tenable-io-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "assets": {
                    "total": total_assets,
                    "seen_today": seen_today,
                    "seen_this_week": seen_week,
                    "seen_older": seen_older,
                    "by_os": dict(os_counter.most_common(20)),
                },
                "sample_assets": [
                    {
                        "id": a.get("id"),
                        "fqdns": (a.get("fqdns") or [])[:3],
                        "ipv4s": (a.get("ipv4s") or [])[:3],
                        "os": (a.get("operating_systems") or ["Unknown"])[:1],
                        "last_seen": a.get("last_seen"),
                        "agent_uuid": a.get("agent_uuid"),
                    }
                    for a in assets[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Tenable.io connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Tenable.io sync (last_run=%s)", since or "never")

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
    TenableIOConnector().run()
