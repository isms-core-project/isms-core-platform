"""AWS Security Hub connector for ISMS CORE v2.0.

Pulls from AWS Security Hub via boto3 and posts evidence to:
  a.8.8     — Management of Technical Vulnerabilities  (finding counts by severity)
  a.8.20-22 — Network Security  (compliance score per Security Hub standard)

Supports explicit credentials, IAM role assumption, and instance profile.

Environment variables required:
  ISMS_API_URL             — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN           — connector bearer token from /admin/connectors/register
  AWS_DEFAULT_REGION       — AWS region, e.g. eu-west-2
  AWS_ACCESS_KEY_ID        — AWS access key (optional if using instance profile)
  AWS_SECRET_ACCESS_KEY    — AWS secret access key
  AWS_ROLE_ARN             — IAM role to assume (optional, for cross-account)
  POLL_INTERVAL            — seconds between syncs (default: 86400 = 24h)

Requires: boto3>=1.34 — add to requirements.txt
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from aws_security_hub_client import AWSSecurityHubClient
from base import EvidenceItem, ISMSConnectorBase

logger = logging.getLogger(__name__)

# Standards ARN → friendly short name
_STANDARDS_NAMES = {
    "cis-aws-foundations-benchmark": "CIS AWS Foundations",
    "aws-foundational-security-best-practices": "AWS FSBP",
    "nist-800-53": "NIST 800-53",
    "pci-dss": "PCI DSS",
    "gdpr": "GDPR",
    "iso-27001": "ISO 27001",
}


def _friendly_standard_name(arn: str) -> str:
    lower = arn.lower()
    for key, name in _STANDARDS_NAMES.items():
        if key in lower:
            return name
    # Fall back to last segment of the ARN path
    return arn.rsplit("/", 1)[-1]


class AWSSecurityHubConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.hub = AWSSecurityHubClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Security Hub data represents current state."""
        findings_summary = self.hub.get_findings_summary()
        standards = self.hub.get_standards_summary()
        insights = self.hub.get_insights(limit=10)

        return [{
            "_type": "aws_security_hub_bundle",
            "findings_summary": findings_summary,
            "standards": standards,
            "insights": insights,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        findings_summary = bundle["findings_summary"]
        standards = bundle["standards"]
        insights = bundle["insights"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.8 — Technical vulnerability management ──────────────────────
        total_findings = findings_summary.get("total", 0)
        by_sev = findings_summary.get("by_severity", {})
        critical = by_sev.get("CRITICAL", 0)
        high = by_sev.get("HIGH", 0)
        medium = by_sev.get("MEDIUM", 0)
        low = by_sev.get("LOW", 0)

        if critical == 0 and high == 0:
            vuln_status = "compliant"
        elif critical == 0 and high <= 20:
            vuln_status = "attention-required"
        else:
            vuln_status = "non-compliant"

        # Top insight names
        insight_names = [i.get("Name", "") for i in insights[:5]]

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"AWS Security Hub findings: {total_findings} active "
                f"({critical} critical, {high} high, {medium} medium, {low} low)"
            ),
            source_ref="aws-security-hub-findings",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "findings": {
                    "total_active": total_findings,
                    "by_severity": by_sev,
                },
                "top_insights": insight_names,
            },
        ))

        # ── A.8.20-22 — Network Security (compliance standards) ─────────────
        # Report compliance score per subscribed Security Hub standard
        if standards:
            # Overall composite score (average across all standards)
            scored = [s for s in standards if s.get("total_controls", 0) > 0]
            overall_score = (
                round(sum(s["compliance_score_pct"] for s in scored) / len(scored), 1)
                if scored else 0.0
            )

            # Determine status from worst-performing standard
            min_score = min((s["compliance_score_pct"] for s in scored), default=100.0)
            if min_score >= 90:
                compliance_status = "compliant"
            elif min_score >= 70:
                compliance_status = "attention-required"
            else:
                compliance_status = "non-compliant"

            standards_detail = [
                {
                    "name": _friendly_standard_name(s["standards_arn"]),
                    "arn": s["standards_arn"],
                    "status": s["status"],
                    "passed": s["passed"],
                    "failed": s["failed"],
                    "disabled": s["disabled"],
                    "total_controls": s["total_controls"],
                    "compliance_score_pct": s["compliance_score_pct"],
                }
                for s in standards
            ]

            items.append(EvidenceItem(
                group_code="a.8.20-22",
                title=(
                    f"AWS Security Hub compliance: overall {overall_score}% "
                    f"across {len(standards)} standard(s) "
                    f"({', '.join(_friendly_standard_name(s['standards_arn']) for s in standards[:3])})"
                ),
                source_ref="aws-security-hub-compliance",
                classification="compliance",
                status=compliance_status,
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "overall_compliance_score_pct": overall_score,
                    "standards": standards_detail,
                },
            ))
        else:
            logger.warning("No Security Hub standards subscriptions found — skipping compliance evidence")

        return items

    def run(self) -> None:
        logger.info("AWS Security Hub connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting AWS Security Hub sync (last_run=%s)", since or "never")

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
    AWSSecurityHubConnector().run()
