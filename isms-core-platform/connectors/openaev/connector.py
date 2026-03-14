"""OpenAEV connector for ISMS CORE v2.0.

Pulls adversary emulation and purple team exercise results from OpenAEV
(Filigran XTM) and posts evidence to:
  a.5.25  — Incident response    (exercise results: detection/prevention/response rates,
                                   inject pass/fail per ATT&CK technique)
  a.6.3   — Security awareness   (completed exercises as training evidence,
                                   participant engagement, scenario coverage)
  a.5.36  — Compliance testing   (security control effectiveness validated through
                                   adversary simulation, findings and remediation)

OpenAEV is tightly integrated with OpenCTI — scenarios are threat-intel-driven
and security coverage metrics feed back into OpenCTI via STIX bundles.

Default poll interval: 86400s (24h) — exercise results change slowly.

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  OPENAEV_URL           — OpenAEV instance URL
  OPENAEV_TOKEN         — API token (Profile → API key)
  OPENAEV_VERIFY_SSL    — "false" for self-signed certs
  OPENAEV_MAX_EXERCISES — max exercises to pull (default: 20)
  POLL_INTERVAL         — seconds between syncs (default: 86400)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from openaev_client import OpenAEVClient

logger = logging.getLogger(__name__)


def _pct(numerator: int, denominator: int) -> float:
    return round(numerator / denominator * 100, 1) if denominator else 0.0


class OpenAEVConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.aev = OpenAEVClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        exercises = self.aev.get_exercises()
        findings = self.aev.get_findings()

        # Enrich first N exercises with results + ATT&CK pattern data
        enriched: list[dict] = []
        for ex in exercises[:10]:
            ex_id = str(ex.get("id", ""))
            if not ex_id:
                continue
            results = self.aev.get_exercise_results(ex_id)
            attack_patterns = self.aev.get_exercise_attack_patterns(ex_id)
            reports = self.aev.get_exercise_reports(ex_id)
            enriched.append({
                "exercise": ex,
                "results": results,
                "attack_patterns": attack_patterns,
                "reports": reports,
            })

        return [{
            "_type": "openaev_bundle",
            "exercises": enriched,
            "all_exercises_meta": exercises,
            "findings": findings,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        enriched = bundle["exercises"]
        all_exercises_meta = bundle["all_exercises_meta"]
        findings = bundle["findings"]
        fetched_at = bundle["fetched_at"]

        total_exercises = len(all_exercises_meta)

        # Aggregate metrics across all enriched exercises
        total_injects = 0
        total_prevented = 0
        total_detected = 0
        total_responded = 0
        total_failed = 0
        all_tactics: set[str] = set()
        all_technique_ids: list[str] = []

        exercise_summaries: list[dict] = []

        for item_data in enriched:
            ex = item_data["exercise"]
            results = item_data["results"]
            patterns = item_data["attack_patterns"]

            ex_name = ex.get("name", ex.get("exercise_name", "Unknown"))
            ex_date = ex.get("exercise_start_date") or ex.get("start_date") or ""

            # Results can come back in different shapes depending on OpenAEV version
            # Try common field names
            prevented = int(results.get("exercise_inject_prevention") or results.get("prevented", 0))
            detected = int(results.get("exercise_inject_detection") or results.get("detected", 0))
            responded = int(results.get("exercise_inject_human_response") or results.get("responded", 0))
            total_ex = int(results.get("exercise_inject_total") or results.get("total", 0))
            failed_ex = total_ex - prevented - detected - responded if total_ex > 0 else 0

            total_injects += total_ex
            total_prevented += prevented
            total_detected += detected
            total_responded += responded
            total_failed += max(0, failed_ex)

            # ATT&CK coverage from inject patterns
            for p in patterns:
                technique = str(p.get("inject_attack_pattern", {}).get("x_mitre_id") or
                                p.get("attack_pattern_id") or "")
                if technique:
                    all_technique_ids.append(technique)
                tactic = str(p.get("inject_attack_pattern", {}).get("kill_chain_phases", [{}])[0].get(
                    "phase_name", "") if isinstance(p.get("inject_attack_pattern", {}).get(
                    "kill_chain_phases"), list) else "")
                if tactic:
                    all_tactics.add(tactic)

            exercise_summaries.append({
                "name": ex_name,
                "date": ex_date,
                "total_injects": total_ex,
                "prevented": prevented,
                "detected": detected,
                "responded": responded,
                "prevent_rate": _pct(prevented, total_ex),
                "detect_rate": _pct(detected, total_ex),
                "respond_rate": _pct(responded, total_ex),
            })

        # Overall rates
        overall_detect_rate = _pct(total_detected + total_prevented, total_injects)
        overall_respond_rate = _pct(total_responded, total_injects)

        # ── A.5.25 — Incident response (exercise evidence) ────────────────
        ir_status = (
            "compliant" if total_exercises > 0 and overall_detect_rate >= 70
            else "attention-required" if total_exercises > 0
            else "incomplete"
        )

        items.append(EvidenceItem(
            group_code="a.5.24-28",
            title=(
                f"OpenAEV exercises: {total_exercises} completed simulations, "
                f"{overall_detect_rate}% detection rate across {total_injects} test scenarios"
            ),
            source_ref="openaev-incident-response",
            classification="incident",
            status=ir_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_exercises": total_exercises,
                "enriched_exercises": len(enriched),
                "aggregate": {
                    "total_injects": total_injects,
                    "total_prevented": total_prevented,
                    "total_detected": total_detected,
                    "total_responded": total_responded,
                    "total_missed": total_failed,
                    "overall_detection_rate_pct": overall_detect_rate,
                    "overall_response_rate_pct": overall_respond_rate,
                },
                "exercises": exercise_summaries,
            },
        ))

        # ── A.6.3 — Security awareness (training evidence) ────────────────
        # Exercises serve as practical security training for defenders
        reports_total = sum(len(e["reports"]) for e in enriched)

        items.append(EvidenceItem(
            group_code="a.6.3",
            title=(
                f"OpenAEV security training: {total_exercises} adversary emulation "
                f"exercises completed, {reports_total} exercise reports generated"
            ),
            source_ref="openaev-security-awareness",
            classification="policy",
            status="compliant" if total_exercises > 0 else "incomplete",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "completed_exercises": total_exercises,
                "reports_generated": reports_total,
                "exercise_names": [e["exercise"].get("name", e["exercise"].get("exercise_name", ""))
                                   for e in enriched],
                "exercise_dates": [
                    e["exercise"].get("exercise_start_date") or e["exercise"].get("start_date", "")
                    for e in enriched
                ],
            },
        ))

        # ── A.5.36 — Compliance testing (security control effectiveness) ──
        # Findings represent gaps identified during exercises
        by_finding_type: dict[str, int] = Counter(
            str(f.get("finding_type") or f.get("type", "unknown")).lower() for f in findings
        )
        open_findings = [
            f for f in findings
            if str(f.get("finding_status") or f.get("status", "")).lower() not in
            ("closed", "resolved", "fixed")
        ]

        unique_techniques = len(set(all_technique_ids))

        items.append(EvidenceItem(
            group_code="a.5.35-36",
            title=(
                f"OpenAEV security coverage: {unique_techniques} ATT&CK techniques tested "
                f"across {len(all_tactics)} tactics, {len(findings)} findings "
                f"({len(open_findings)} open)"
            ),
            source_ref="openaev-compliance-testing",
            classification="policy",
            status="compliant" if len(open_findings) == 0 else "attention-required",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "attack_coverage": {
                    "tactics": sorted(all_tactics),
                    "unique_techniques": unique_techniques,
                    "technique_ids": list(set(all_technique_ids))[:50],
                },
                "findings": {
                    "total": len(findings),
                    "open": len(open_findings),
                    "by_type": dict(by_finding_type),
                    "sample": [
                        {
                            "title": f.get("finding_name") or f.get("title") or f.get("name", ""),
                            "type": f.get("finding_type") or f.get("type", ""),
                            "status": f.get("finding_status") or f.get("status", ""),
                            "exercise": f.get("exercise", {}).get("name", "") if isinstance(
                                f.get("exercise"), dict) else "",
                        }
                        for f in findings[:20]
                    ],
                },
            },
        ))

        return items

    def run(self) -> None:
        logger.info("OpenAEV connector starting (poll_interval=%ds)", self.poll_interval)
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
    OpenAEVConnector().run()
