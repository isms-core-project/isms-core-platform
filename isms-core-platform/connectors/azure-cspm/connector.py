"""Azure CSPM connector for ISMS CORE v2.0 (Defender for Cloud).

Pulls from Azure Resource Manager (ARM) Security APIs and posts evidence to:
  a.8.8        — Vulnerability Management  (security assessments / unhealthy resources)
  a.5.9        — Asset Inventory           (assessment counts by resource type)
  a.8.20-22    — Network Security          (network-related assessments / NSG / firewall)
  a.8.5        — Authentication Controls   (Azure Secure Score + identity assessments)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  AZURE_TENANT_ID           — Azure AD tenant ID (falls back to ENTRA_TENANT_ID)
  AZURE_CLIENT_ID           — App registration client ID (falls back to ENTRA_CLIENT_ID)
  AZURE_CLIENT_SECRET       — App registration client secret (falls back to ENTRA_CLIENT_SECRET)
  AZURE_SUBSCRIPTION_ID     — (optional) single subscription ID; if unset, auto-discovers all
  POLL_INTERVAL             — seconds between full syncs (default: 86400 = 24h)

Required RBAC (on subscription):
  Security Reader            (minimum — read Defender for Cloud data, assessments, alerts)
  Reader                     (for subscription discovery)

Note: When AZURE_SUBSCRIPTION_ID is set, only that subscription is processed.
When unset, all subscriptions accessible to the service principal are processed.
"""

import logging
import os
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from arm_client import ARMClient
from base import EvidenceItem, ISMSConnectorBase

logger = logging.getLogger(__name__)

# Secure Score thresholds (percentage is 0–100)
_SCORE_COMPLIANT = 70
_SCORE_WARNING = 40

# Unhealthy assessment ratio thresholds for classification
_UNHEALTHY_COMPLIANT = 0.10   # < 10% unhealthy → compliant
_UNHEALTHY_WARNING = 0.30     # < 30% unhealthy → warning; else non_compliant

# High alert count threshold
_HIGH_ALERT_THRESHOLD = 1

# Keywords to identify network-related assessments
_NETWORK_KEYWORDS = {"network", "firewall", "nsg", "port", "subnet", "vnet", "vpn", "waf"}


def _is_network_assessment(display_name: str) -> bool:
    """Return True if the assessment display name is network-related."""
    lower = display_name.lower()
    return any(kw in lower for kw in _NETWORK_KEYWORDS)


def _secure_score_classification(pct: float) -> str:
    if pct >= _SCORE_COMPLIANT:
        return "compliant"
    if pct >= _SCORE_WARNING:
        return "warning"
    return "non_compliant"


class AzureCSPMConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = ARMClient(**cfg)
        # Optional fixed subscription ID — avoids discovery API call
        self._fixed_subscription_id: str | None = os.environ.get("AZURE_SUBSCRIPTION_ID")

    # ── fetch — discovers subscriptions and pulls all Defender data ───────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — one bundle per subscription."""
        if self._fixed_subscription_id:
            subscription_ids = [self._fixed_subscription_id]
            sub_names = {self._fixed_subscription_id: self._fixed_subscription_id}
            logger.info(
                "Using configured subscription: %s", self._fixed_subscription_id
            )
        else:
            subs = self.client.get_subscriptions()
            subscription_ids = [s["subscriptionId"] for s in subs if "subscriptionId" in s]
            sub_names = {
                s["subscriptionId"]: s.get("displayName", s["subscriptionId"])
                for s in subs
                if "subscriptionId" in s
            }
            logger.info("Discovered %d subscription(s)", len(subscription_ids))

        bundles = []
        for sub_id in subscription_ids:
            sub_name = sub_names.get(sub_id, sub_id)
            logger.info("Fetching Defender data for subscription: %s (%s)", sub_name, sub_id)

            secure_scores = self.client.get_secure_scores(sub_id)
            assessments = self.client.get_assessments(sub_id)
            alerts = self.client.get_alerts(sub_id)
            regulatory = self.client.get_regulatory_compliance(sub_id)

            bundles.append({
                "_type": "azure_cspm_bundle",
                "subscription_id": sub_id,
                "subscription_name": sub_name,
                "secure_scores": secure_scores,
                "assessments": assessments,
                "alerts": alerts,
                "regulatory_compliance": regulatory,
            })

        return bundles

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        sub_id = bundle["subscription_id"]
        sub_name = bundle["subscription_name"]
        assessments = bundle["assessments"]
        alerts = bundle["alerts"]
        secure_scores = bundle["secure_scores"]

        # ── Classify assessments by health status ─────────────────────────────
        def _status_code(a: dict) -> str:
            props = a.get("properties") or {}
            status = props.get("status") or {}
            return (status.get("code") or "Unknown").lower()

        healthy = [a for a in assessments if _status_code(a) == "healthy"]
        unhealthy = [a for a in assessments if _status_code(a) == "unhealthy"]
        not_applicable = [a for a in assessments if _status_code(a) == "notapplicable"]
        total = len(assessments)

        def _display_name(a: dict) -> str:
            return (a.get("properties") or {}).get("displayName", a.get("name", ""))

        # ── A.8.8 — Vulnerability Management / Assessments ────────────────────
        unhealthy_pct = (len(unhealthy) / total) if total > 0 else 0.0
        if unhealthy_pct < _UNHEALTHY_COMPLIANT:
            assess_classification = "compliant"
        elif unhealthy_pct < _UNHEALTHY_WARNING:
            assess_classification = "warning"
        else:
            assess_classification = "non_compliant"

        # Group unhealthy by resource type for asset inventory context
        by_resource_type: dict[str, int] = Counter(
            (a.get("properties") or {})
            .get("resourceDetails", {})
            .get("Source", "unknown")
            for a in unhealthy
        )

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Azure Defender: {len(unhealthy)}/{total} assessments unhealthy "
                f"in {sub_name}"
            ),
            source_ref=f"azure-cspm-assessments-{sub_id}",
            classification=assess_classification,
            status="active",
            raw={
                "subscription_id": sub_id,
                "subscription_name": sub_name,
                "total_assessments": total,
                "healthy": len(healthy),
                "unhealthy": len(unhealthy),
                "not_applicable": len(not_applicable),
                "unhealthy_pct": round(unhealthy_pct * 100, 1),
                "by_resource_source": dict(by_resource_type),
                "unhealthy_assessments": [
                    {
                        "name": a.get("name"),
                        "display_name": _display_name(a),
                        "status_code": _status_code(a),
                    }
                    for a in unhealthy[:50]
                ],
            },
        ))

        # ── A.8.20-22 — Network security assessments ──────────────────────────
        network_assessments = [a for a in assessments if _is_network_assessment(_display_name(a))]
        network_unhealthy = [a for a in network_assessments if _status_code(a) == "unhealthy"]
        net_total = len(network_assessments)
        net_unhealthy_count = len(network_unhealthy)

        net_classification = "non_compliant" if net_unhealthy_count > 0 else "compliant"

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"Azure network security assessments: {net_unhealthy_count} issues found "
                f"in {sub_name}"
            ),
            source_ref=f"azure-cspm-network-{sub_id}",
            classification=net_classification,
            status="active",
            raw={
                "subscription_id": sub_id,
                "subscription_name": sub_name,
                "total_network_assessments": net_total,
                "unhealthy_network_assessments": net_unhealthy_count,
                "network_issues": [
                    {
                        "name": a.get("name"),
                        "display_name": _display_name(a),
                        "status_code": _status_code(a),
                    }
                    for a in network_unhealthy
                ],
            },
        ))

        # ── A.8.5 — Azure Secure Score ────────────────────────────────────────
        # Use the first score entry (typically "defaultAssessment" / overall score)
        if secure_scores:
            score_entry = secure_scores[0]
            score_props = score_entry.get("properties") or {}
            score_data = score_props.get("score") or {}
            current_score = score_data.get("current", 0)
            max_score = score_data.get("max", 0)
            pct_score = score_data.get("percentage", 0) * 100  # ARM returns 0.0–1.0

            score_classification = _secure_score_classification(pct_score)

            items.append(EvidenceItem(
                group_code="a.8.2-3-5",
                title=(
                    f"Azure Secure Score: {current_score:.1f}/{max_score:.1f} "
                    f"({pct_score:.1f}%) for {sub_name}"
                ),
                source_ref=f"azure-cspm-secure-score-{sub_id}",
                classification=score_classification,
                status="active",
                raw={
                    "subscription_id": sub_id,
                    "subscription_name": sub_name,
                    "current": current_score,
                    "max": max_score,
                    "percentage": round(pct_score, 1),
                    "initiative_name": score_props.get("displayName", score_entry.get("name")),
                },
            ))
        else:
            logger.warning(
                "No Secure Score data for subscription %s — "
                "Defender for Cloud may not be enabled",
                sub_id,
            )

        # ── A.8.8 — Defender for Cloud alerts ────────────────────────────────
        total_alert_count = len(alerts)
        by_severity: dict[str, int] = Counter(
            (a.get("properties") or {}).get("severity", "unknown").lower()
            for a in alerts
        )
        high_count = by_severity.get("high", 0)

        alert_classification = "non_compliant" if high_count >= _HIGH_ALERT_THRESHOLD else "compliant"

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Azure Defender alerts: {total_alert_count} "
                f"({high_count} high) in {sub_name}"
            ),
            source_ref=f"azure-cspm-alerts-{sub_id}",
            classification=alert_classification,
            status="active",
            raw={
                "subscription_id": sub_id,
                "subscription_name": sub_name,
                "total": total_alert_count,
                "by_severity": dict(by_severity),
                "recent_alerts": [
                    {
                        "name": a.get("name"),
                        "display_name": (a.get("properties") or {}).get("alertDisplayName"),
                        "severity": (a.get("properties") or {}).get("severity"),
                        "status": (a.get("properties") or {}).get("status"),
                        "description": (a.get("properties") or {}).get("description", "")[:200],
                    }
                    for a in alerts[:20]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("Azure CSPM connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Azure CSPM sync (last_run=%s)", since or "never")

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
    AzureCSPMConnector().run()
