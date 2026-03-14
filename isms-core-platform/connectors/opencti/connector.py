"""OpenCTI connector for ISMS CORE v2.0.

Pulls threat intelligence from OpenCTI (Filigran XTM) and posts evidence to:
  a.5.7   — Threat intelligence     (indicators, threat actors, ATT&CK coverage)
  a.5.25  — Incident response       (recorded cyber incidents)
  a.8.8   — Technical vulnerability (CVEs with CVSS severity breakdown)

Supports on-premises OpenCTI and OpenCTI Cloud deployments.
Default poll interval: 3600s (1h) — threat intel refreshes frequently.

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  OPENCTI_URL           — OpenCTI instance URL
  OPENCTI_TOKEN         — API token (Profile → API Access → Token)
  OPENCTI_VERIFY_SSL    — "false" for self-signed certs
  POLL_INTERVAL         — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from opencti_client import OpenCTIClient

logger = logging.getLogger(__name__)

# CVSS/severity normalisation
CVSS_SEVERITY_ORDER = ["critical", "high", "medium", "low", "unknown", "none"]


def _cvss_label(sev: str | None) -> str:
    s = str(sev or "").lower()
    return s if s in CVSS_SEVERITY_ORDER else "unknown"


class OpenCTIConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.octi = OpenCTIClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        indicators = self.octi.get_indicators()
        vulns = self.octi.get_vulnerabilities()
        incidents = self.octi.get_incidents()
        threat_actors = self.octi.get_threat_actors()
        attack_patterns = self.octi.get_attack_patterns()

        return [{
            "_type": "opencti_bundle",
            "indicators": indicators,
            "vulns": vulns,
            "incidents": incidents,
            "threat_actors": threat_actors,
            "attack_patterns": attack_patterns,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        indicators = bundle["indicators"]
        vulns = bundle["vulns"]
        incidents = bundle["incidents"]
        threat_actors = bundle["threat_actors"]
        attack_patterns = bundle["attack_patterns"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.7 — Threat intelligence ───────────────────────────────────
        # Indicators by pattern type (ipv4-addr, domain-name, file, url, etc.)
        by_pattern: dict[str, int] = Counter(
            str(i.get("pattern_type", "unknown")).lower() for i in indicators
        )
        # Threat actor types
        actor_types: dict[str, int] = Counter()
        for a in threat_actors:
            for t in (a.get("threat_actor_types") or []):
                actor_types[str(t).lower()] += 1

        # ATT&CK coverage — extract MITRE tactic from kill chain phases
        tactics: set[str] = set()
        mitre_ids: list[str] = []
        for p in attack_patterns:
            mid = p.get("x_mitre_id") or ""
            if mid:
                mitre_ids.append(mid)
            for kcp in (p.get("kill_chain_phases") or []):
                phase = kcp.get("phase_name", "")
                if phase:
                    tactics.add(phase)

        # Average indicator confidence score
        scores = [int(i.get("x_opencti_score") or 0) for i in indicators if i.get("x_opencti_score")]
        avg_score = round(sum(scores) / len(scores)) if scores else 0

        ti_status = "compliant" if indicators else "attention-required"

        items.append(EvidenceItem(
            group_code="a.5.7",
            title=(
                f"OpenCTI threat intelligence: {len(indicators)} indicators "
                f"(avg score {avg_score}), {len(threat_actors)} threat actors, "
                f"{len(mitre_ids)} ATT&CK techniques across {len(tactics)} tactics"
            ),
            source_ref="opencti-threat-intel",
            classification="network",
            status=ti_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "indicators": {
                    "total": len(indicators),
                    "by_pattern_type": dict(by_pattern),
                    "avg_confidence_score": avg_score,
                    "sample": [
                        {
                            "name": i.get("name"),
                            "pattern_type": i.get("pattern_type"),
                            "score": i.get("x_opencti_score"),
                            "valid_until": i.get("valid_until"),
                        }
                        for i in indicators[:20]
                    ],
                },
                "threat_actors": {
                    "total": len(threat_actors),
                    "by_type": dict(actor_types),
                    "names": [a.get("name") for a in threat_actors[:20]],
                },
                "attack_patterns": {
                    "total": len(attack_patterns),
                    "mitre_techniques": len(mitre_ids),
                    "tactics_covered": sorted(tactics),
                    "technique_ids": mitre_ids[:50],
                },
            },
        ))

        # ── A.5.25 — Incident response ────────────────────────────────────
        by_severity: dict[str, int] = Counter(
            str(i.get("severity", "unknown")).lower() for i in incidents
        )
        open_incidents = [
            i for i in incidents
            if not i.get("last_seen") or str(i.get("status", "")).lower() not in ("closed", "resolved")
        ]

        inc_status = "compliant" if not open_incidents else "attention-required"

        items.append(EvidenceItem(
            group_code="a.5.24-28",
            title=(
                f"OpenCTI incidents: {len(incidents)} recorded "
                f"({by_severity.get('high', 0)} high, "
                f"{by_severity.get('critical', 0)} critical)"
            ),
            source_ref="opencti-incidents",
            classification="incident",
            status=inc_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_incidents": len(incidents),
                "by_severity": dict(by_severity),
                "open_count": len(open_incidents),
                "incidents": [
                    {
                        "name": i.get("name"),
                        "severity": i.get("severity"),
                        "first_seen": i.get("first_seen"),
                        "last_seen": i.get("last_seen"),
                        "incident_type": i.get("incident_type"),
                        "description": str(i.get("description") or "")[:200],
                    }
                    for i in incidents[:30]
                ],
            },
        ))

        # ── A.8.8 — Technical vulnerability management ────────────────────
        sev_counts: dict[str, int] = Counter(
            _cvss_label(v.get("x_opencti_cvss_base_severity")) for v in vulns
        )
        critical_count = sev_counts.get("critical", 0)
        high_count = sev_counts.get("high", 0)

        vuln_status = (
            "compliant" if critical_count == 0 and high_count <= 5
            else "attention-required" if critical_count <= 3
            else "non-compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"OpenCTI vulnerability intelligence: {len(vulns)} CVEs tracked "
                f"({critical_count} critical, {high_count} high)"
            ),
            source_ref="opencti-vulnerabilities",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_vulnerabilities": len(vulns),
                "by_severity": dict(sev_counts),
                "vulnerabilities": [
                    {
                        "name": v.get("name"),
                        "cvss_severity": v.get("x_opencti_cvss_base_severity"),
                        "cvss_score": v.get("x_opencti_cvss_base_score"),
                        "description": str(v.get("description") or "")[:200],
                        "created_at": v.get("created_at"),
                    }
                    for v in vulns[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("OpenCTI connector starting (poll_interval=%ds)", self.poll_interval)
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
    OpenCTIConnector().run()
