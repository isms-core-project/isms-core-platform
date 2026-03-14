"""GCP Security Command Center connector for ISMS CORE v2.0.

Pulls from the Google Cloud Security Command Center REST API v2 and posts
evidence to:
  a.8.8  — Management of Technical Vulnerabilities  (finding counts by severity)
  a.5.9  — Inventory of Information and Other Associated Assets  (GCP asset count)

Authentication: service account JSON key or GCE instance metadata.

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  GCP_PROJECT_ID            — GCP project ID
  GCP_ORGANIZATION_ID       — GCP organization ID (numeric)
  GCP_SERVICE_ACCOUNT_KEY   — Full JSON string of the service account key file
                              (omit if running on GCE with adequate instance permissions)
  POLL_INTERVAL             — seconds between syncs (default: 86400 = 24h)

IAM roles required on the organisation:
  roles/securitycenter.findingsViewer
  roles/securitycenter.assetsViewer  (or roles/securitycenter.viewer)

Requires: cryptography>=42 (for service account JWT auth — see requirements.txt)
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from gcp_scc_client import GCPSCCClient

logger = logging.getLogger(__name__)

# SCC severity label normalisation
_SEVERITY_MAP = {
    "CRITICAL": "critical",
    "HIGH": "high",
    "MEDIUM": "medium",
    "LOW": "low",
    "SEVERITY_UNSPECIFIED": "info",
}


class GCPSCCConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.scc = GCPSCCClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — SCC data represents current state."""
        findings = self.scc.get_findings(limit=5000)
        assets = self.scc.get_assets(limit=5000)

        return [{
            "_type": "gcp_scc_bundle",
            "findings": findings,
            "assets": assets,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        findings = bundle["findings"]
        assets = bundle["assets"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.8 — Technical vulnerability management ──────────────────────
        # SCC finding structure: listFindingsResults items contain a 'finding' sub-key
        sev_counts: dict[str, int] = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }
        category_counter: Counter = Counter()
        resource_types: Counter = Counter()

        for item_wrapper in findings:
            # v2 API wraps finding in listFindingsResults[].finding
            finding = item_wrapper.get("finding", item_wrapper)
            raw_sev = finding.get("severity", "SEVERITY_UNSPECIFIED")
            norm_sev = _SEVERITY_MAP.get(raw_sev, "info")
            sev_counts[norm_sev] = sev_counts.get(norm_sev, 0) + 1
            category_counter[finding.get("category", "UNKNOWN")] += 1
            resource_types[finding.get("resourceName", "").split("/")[2] if "/" in finding.get("resourceName", "") else "unknown"] += 1

        total_findings = sum(sev_counts.values())
        critical = sev_counts["critical"]
        high = sev_counts["high"]
        medium = sev_counts["medium"]

        if critical == 0 and high == 0:
            vuln_status = "compliant"
        elif critical == 0 and high <= 10:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        top_categories = category_counter.most_common(10)

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"GCP SCC findings: {total_findings} active "
                f"({critical} critical, {high} high, {medium} medium)"
            ),
            source_ref="gcp-scc-findings",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "findings": {
                    "total_active": total_findings,
                    "by_severity": sev_counts,
                    "top_categories": [
                        {"category": cat, "count": cnt}
                        for cat, cnt in top_categories
                    ],
                },
                "sample_findings": [
                    {
                        "name": f.get("finding", f).get("name", ""),
                        "category": f.get("finding", f).get("category", ""),
                        "severity": f.get("finding", f).get("severity", ""),
                        "resource": f.get("finding", f).get("resourceName", ""),
                        "event_time": f.get("finding", f).get("eventTime", ""),
                    }
                    for f in findings[:30]
                ],
            },
        ))

        # ── A.5.9 — Asset inventory ──────────────────────────────────────────
        total_assets = len(assets)

        # Group by GCP resource type
        asset_type_counter: Counter = Counter()
        for item_wrapper in assets:
            asset = item_wrapper.get("asset", item_wrapper)
            security_marks = asset.get("securityMarks", {})
            resource_props = asset.get("resourceProperties", {})
            resource_type = asset.get("name", "").split("/")[-2] if asset.get("name") else "unknown"
            asset_type_counter[resource_type] += 1

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"GCP SCC asset inventory: {total_assets} GCP resources discovered "
                f"across the organisation"
            ),
            source_ref="gcp-scc-asset-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "assets": {
                    "total": total_assets,
                    "by_type": dict(asset_type_counter.most_common(20)),
                },
                "sample_assets": [
                    {
                        "name": a.get("asset", a).get("name", ""),
                        "resource_type": a.get("asset", a).get("resourceProperties", {}).get("resourceType", ""),
                        "update_time": a.get("asset", a).get("updateTime", ""),
                    }
                    for a in assets[:30]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("GCP SCC connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting GCP SCC sync (last_run=%s)", since or "never")

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
    GCPSCCConnector().run()
