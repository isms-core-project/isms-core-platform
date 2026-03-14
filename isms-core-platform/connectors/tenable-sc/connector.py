"""Tenable Security Center (Tenable.sc) connector for ISMS CORE v2.0.

On-premises vulnerability management. Pulls from the Tenable.sc REST API
and posts evidence to:
  a.8.8  — Management of technical vulnerabilities  (severity breakdown,
             critical/high findings, top vulnerable hosts, CVE list)
  a.8.1  — Inventory of information and other associated assets
             (assets managed by Tenable.sc, total IPs in scope)

Deployment model: on-premises (Model B).
Default poll interval: 86400s (24h) — scan cadence drives the data freshness.

Environment variables required:
  ISMS_API_URL              — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  TENABLE_SC_HOST           — Tenable.sc hostname/IP
  TENABLE_SC_ACCESS_KEY     — API access key (preferred, Tenable.sc 5.13+)
  TENABLE_SC_SECRET_KEY     — API secret key
    OR
  TENABLE_SC_USERNAME       — Username (session auth fallback)
  TENABLE_SC_PASSWORD       — Password
  TENABLE_SC_VERIFY_SSL     — "false" for self-signed certs
  POLL_INTERVAL             — seconds between syncs (default: 86400)
"""

import logging
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from tenable_sc_client import TenableSCClient

logger = logging.getLogger(__name__)

# Severity codes → labels (Tenable.sc internal numbering)
SEVERITY_LABELS = {
    "0": "info",
    "1": "low",
    "2": "medium",
    "3": "high",
    "4": "critical",
}


class TenableSCConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.sc = TenableSCClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        system = self.sc.get_system_info()
        vuln_summary = self.sc.get_vulnerability_summary()
        critical_vulns = self.sc.get_critical_vulnerabilities()
        assets = self.sc.get_assets()
        scan_results = self.sc.get_scan_results()

        return [{
            "_type": "tenable_sc_bundle",
            "system": system,
            "vuln_summary": vuln_summary,
            "critical_vulns": critical_vulns,
            "assets": assets,
            "scan_results": scan_results,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        system = bundle["system"]
        vuln_summary = bundle["vuln_summary"]
        critical_vulns = bundle["critical_vulns"]
        assets = bundle["assets"]
        scan_results = bundle["scan_results"]
        fetched_at = bundle["fetched_at"]

        # Server identity
        sys_info = system.get("response", {})
        server_name = sys_info.get("name", "Tenable.sc")
        version = sys_info.get("version", "")
        server_label = f"{server_name} {version}".strip()

        # ── A.8.8 — Technical vulnerability management ─────────────────────
        # Parse severity breakdown from sumseverity analysis
        sev_rows = vuln_summary.get("response", {}).get("results", [])
        sev_counts: dict[str, int] = {}
        total_vulns = 0
        for row in sev_rows:
            sev_code = str(row.get("severity", {}).get("id", "0"))
            count = int(row.get("count", 0))
            label = SEVERITY_LABELS.get(sev_code, f"sev{sev_code}")
            sev_counts[label] = sev_counts.get(label, 0) + count
            total_vulns += count

        critical_count = sev_counts.get("critical", 0)
        high_count = sev_counts.get("high", 0)
        medium_count = sev_counts.get("medium", 0)

        # Parse critical/high vuln detail rows
        vuln_rows = critical_vulns.get("response", {}).get("results", [])
        total_returned = critical_vulns.get("response", {}).get("totalRecords", len(vuln_rows))

        # Top CVEs from the critical/high findings
        cves: list[str] = []
        top_hosts: dict[str, int] = {}
        for row in vuln_rows:
            ip = str(row.get("ip", ""))
            if ip:
                top_hosts[ip] = top_hosts.get(ip, 0) + 1
            for cve in str(row.get("cve", "")).split(","):
                cve = cve.strip()
                if cve and cve not in cves:
                    cves.append(cve)
            if len(cves) >= 20:
                break

        # Determine status based on critical count
        if critical_count == 0 and high_count <= 10:
            vuln_status = "compliant"
        elif critical_count <= 5:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        # Most-affected hosts (top 10 by vuln count)
        top_affected = sorted(top_hosts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Scan coverage from recent scan results
        scans = scan_results.get("response", {}).get("usable", [])
        completed_scans = [s for s in scans if str(s.get("status", "")).lower() == "completed"]
        total_scanned_ips = sum(int(s.get("completedIPs", 0)) for s in completed_scans[:5])

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"{server_label} vulnerability summary: {total_vulns} total "
                f"({critical_count} critical, {high_count} high, {medium_count} medium)"
            ),
            source_ref="tenable-sc-vuln-summary",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "server": server_label,
                "version": version,
                "vulnerabilities": {
                    "total": total_vulns,
                    "by_severity": sev_counts,
                    "critical_high_findings": int(total_returned),
                },
                "top_cves": cves[:20],
                "most_affected_hosts": [{"ip": ip, "vuln_count": cnt} for ip, cnt in top_affected],
                "scan_coverage": {
                    "recent_completed_scans": len(completed_scans),
                    "total_ips_scanned": total_scanned_ips,
                },
                "high_priority_vulns": [
                    {
                        "severity": SEVERITY_LABELS.get(
                            str(r.get("severity", {}).get("id", "0") if isinstance(r.get("severity"), dict)
                                else r.get("severity", 0)), "unknown"
                        ),
                        "ip": r.get("ip"),
                        "dns_name": r.get("dnsName"),
                        "plugin_name": r.get("pluginName"),
                        "plugin_id": r.get("pluginID"),
                        "cvss_v3": r.get("cvssV3BaseScore"),
                        "cve": r.get("cve"),
                        "last_seen": r.get("lastSeen"),
                    }
                    for r in vuln_rows[:50]
                ],
            },
        ))

        # ── A.8.1 — Asset inventory ────────────────────────────────────────
        asset_list = assets.get("response", {}).get("usable", [])
        total_assets = len(asset_list)

        # Group assets by type
        by_type: dict[str, int] = {}
        total_ips_in_scope = 0
        for a in asset_list:
            atype = str(a.get("type", "unknown"))
            by_type[atype] = by_type.get(atype, 0) + 1
            ip_count = int(a.get("ipCount", 0))
            total_ips_in_scope += ip_count

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"{server_label} asset scope: {total_assets} asset groups, "
                f"{total_ips_in_scope:,} IPs in vulnerability scan scope"
            ),
            source_ref="tenable-sc-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "server": server_label,
                "asset_groups": {
                    "total": total_assets,
                    "by_type": by_type,
                    "total_ips_in_scope": total_ips_in_scope,
                },
                "assets": [
                    {
                        "id": a.get("id"),
                        "name": a.get("name"),
                        "type": a.get("type"),
                        "ip_count": a.get("ipCount"),
                        "description": a.get("description", "")[:120],
                    }
                    for a in asset_list[:50]
                ],
                "recent_scans": [
                    {
                        "name": s.get("name"),
                        "status": s.get("status"),
                        "start_time": s.get("startTime"),
                        "finish_time": s.get("finishTime"),
                        "completed_ips": s.get("completedIPs"),
                        "total_ips": s.get("totalIPs"),
                    }
                    for s in scans[:10]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Tenable.sc connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                bundles = self.fetch(None)
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
            time.sleep(max(0, self.poll_interval - elapsed))


if __name__ == "__main__":
    TenableSCConnector().run()
