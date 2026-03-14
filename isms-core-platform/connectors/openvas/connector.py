"""OpenVAS / Greenbone Vulnerability Manager connector for ISMS CORE v2.0.

Pulls from the Greenbone Security Assistant (GSA) REST API and posts evidence to:
  a.8.8  — Management of Technical Vulnerabilities  (scan results, severity counts)
  a.5.9  — Inventory of Information and Other Associated Assets  (hosts discovered)

Targets GVM 22.4+ with the GSA REST API (/api/v1).
For older deployments without the REST API, the GMP XML protocol over a
Unix socket is the alternative (not implemented here).

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  OPENVAS_URL           — GSA base URL, e.g. https://greenbone.corp.local
  OPENVAS_USERNAME      — GVM username
  OPENVAS_PASSWORD      — GVM password
  OPENVAS_VERIFY_SSL    — "false" for self-signed certificates (default: true)
  POLL_INTERVAL         — seconds between syncs (default: 86400 = 24h)
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from openvas_client import OpenVASClient

logger = logging.getLogger(__name__)

# Severity label normalisation (GVM uses Critical/High/Medium/Low/Log)
_SEVERITY_NORM = {
    "critical": "critical",
    "high": "high",
    "medium": "medium",
    "low": "low",
    "log": "info",
    "false_positive": "info",
}


class OpenVASConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.openvas = OpenVASClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — OpenVAS data represents current scan state."""
        tasks = self.openvas.get_tasks()
        reports = self.openvas.get_reports_summary()
        hosts = self.openvas.get_hosts_summary()

        return [{
            "_type": "openvas_bundle",
            "tasks": tasks,
            "reports": reports,
            "hosts": hosts,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        tasks = bundle["tasks"]
        reports = bundle["reports"]
        hosts = bundle["hosts"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.8 — Technical vulnerability management ──────────────────────
        # Aggregate severity counts across all recent reports
        sev_counts: dict[str, int] = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }
        total_results = 0
        latest_report_date = ""

        for report in reports:
            # GVM report structure varies — try common paths
            report_data = report.get("report", report)
            counts = report_data.get("result_count", report_data.get("counts", {}))

            # Try the severity_counts sub-key
            sev_data = counts.get("severity", counts) if isinstance(counts, dict) else {}

            for raw_sev, norm_sev in _SEVERITY_NORM.items():
                cnt = int(sev_data.get(raw_sev, sev_data.get(raw_sev.capitalize(), 0)))
                sev_counts[norm_sev] = sev_counts.get(norm_sev, 0) + cnt
                total_results += cnt

            # Capture latest report timestamp
            ts = report_data.get("modification_time", report_data.get("timestamp", ""))
            if ts and (not latest_report_date or ts > latest_report_date):
                latest_report_date = ts

        # Avoid double-counting total
        total_vulns = sev_counts["critical"] + sev_counts["high"] + sev_counts["medium"] + sev_counts["low"]

        critical = sev_counts["critical"]
        high = sev_counts["high"]
        medium = sev_counts["medium"]

        # Scan task summary
        done_tasks = [t for t in tasks if str(t.get("status", "")).lower() in ("done", "stopped")]
        running_tasks = [t for t in tasks if str(t.get("status", "")).lower() == "running"]

        # Compliance status
        if critical == 0 and high == 0:
            vuln_status = "compliant"
        elif critical == 0 and high <= 5:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"OpenVAS scan results: {total_vulns} findings "
                f"({critical} critical, {high} high, {medium} medium) "
                f"across {len(reports)} reports"
            ),
            source_ref="openvas-scan-results",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "latest_report_date": latest_report_date,
                "vulnerabilities": {
                    "total": total_vulns,
                    "by_severity": sev_counts,
                },
                "scan_tasks": {
                    "total": len(tasks),
                    "done": len(done_tasks),
                    "running": len(running_tasks),
                    "tasks": [
                        {
                            "name": t.get("name"),
                            "status": t.get("status"),
                            "progress": t.get("progress"),
                            "last_report": t.get("last_report", {}).get("timestamp", ""),
                        }
                        for t in tasks[:20]
                    ],
                },
                "recent_reports": [
                    {
                        "id": r.get("id"),
                        "name": r.get("name", r.get("report", {}).get("name", "")),
                        "timestamp": r.get("modification_time", r.get("timestamp", "")),
                    }
                    for r in reports[:10]
                ],
            },
        ))

        # ── A.5.9 — Asset inventory ──────────────────────────────────────────
        total_hosts = hosts.get("total_hosts", 0)

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"OpenVAS asset inventory: {total_hosts} hosts discovered in vulnerability scanning scope"
            ),
            source_ref="openvas-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "assets": {
                    "total_hosts": total_hosts,
                },
                "scan_tasks": len(tasks),
                "reports_analysed": len(reports),
            },
        ))

        return items

    def run(self) -> None:
        logger.info("OpenVAS connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting OpenVAS sync (last_run=%s)", since or "never")

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
    OpenVASConnector().run()
