"""Wazuh XDR/SIEM connector for ISMS CORE v2.0.

Queries the Wazuh Manager REST API and posts evidence to:
  a.8.1-7-18-19 — Endpoint security / user endpoint devices  (agent inventory)
  a.8.7         — Protection against malware                  (alert count by severity)
  a.8.8         — Management of technical vulnerabilities     (CVE counts via /vulnerability/agents)

Environment variables required:
  ISMS_API_URL     — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN   — connector bearer token from /admin/connectors/register
  WAZUH_URL        — Wazuh Manager API base URL, e.g. https://wazuh.corp.local:55000
  WAZUH_USERNAME   — Wazuh API username
  WAZUH_PASSWORD   — Wazuh API password
  WAZUH_VERIFY_SSL — "false" to skip TLS verification for self-signed certs (default: true)
  POLL_INTERVAL    — seconds between syncs (default: 3600 = 1h)
  BATCH_SIZE       — items per API call (default: 100)

API permissions required:
  Wazuh REST API minimum permissions for the service account:
  - agents:read                 — agent inventory
  - alerts:read                 — alert data
  - vulnerability_detector:read — CVE findings (/vulnerability/agents, 4.8+ compatible)
  - manager:read                — manager info
  Create via Wazuh dashboard: Security → Roles → Add role
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from wazuh_client import WazuhClient

logger = logging.getLogger(__name__)

# Wazuh alert severity thresholds (levels 1-15)
LEVEL_CRITICAL = 15
LEVEL_HIGH_MIN = 12
LEVEL_HIGH_MAX = 14
LEVEL_MEDIUM_MIN = 7
LEVEL_MEDIUM_MAX = 11



class WazuhConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.wazuh = WazuhClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Wazuh agent/alert state is always current."""
        agents = self.wazuh.get_agents()
        alerts_summary = self.wazuh.get_alerts_summary()
        os_summary = self.wazuh.get_agent_os_summary()
        manager_status = self.wazuh.get_manager_status()
        # Use aggregate endpoint (Wazuh 4.8+ compatible — replaces per-agent GET /vulnerability/{id})
        vuln_summary = self.wazuh.get_vulnerability_summary()

        return [
            {
                "_type": "wazuh_bundle",
                "agents": agents,
                "alerts_summary": alerts_summary,
                "os_summary": os_summary,
                "manager_status": manager_status,
                "vuln_summary": vuln_summary,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        agents = bundle["agents"]
        alerts_summary = bundle["alerts_summary"]
        vuln_summary = bundle["vuln_summary"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1-7-18-19 — Endpoint security / agent inventory ──────────────
        by_status: Counter = Counter(
            str(a.get("status", "unknown")).lower()
            for a in agents
        )
        active_count = by_status.get("active", 0)
        disconnected_count = by_status.get("disconnected", 0)
        pending_count = by_status.get("pending", 0)

        # OS distribution from agents
        by_os: Counter = Counter(
            (a.get("os") or {}).get("platform", "unknown")
            for a in agents
        )

        # Non-compliant if many agents are disconnected
        disconnected_pct = (disconnected_count / len(agents) * 100) if agents else 0
        if disconnected_count >= 2 and disconnected_pct > 10:
            agent_status = "non-compliant"
        elif disconnected_count > 0:
            agent_status = "attention-required"
        else:
            agent_status = "compliant"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"Wazuh agent inventory: {len(agents)} agents "
                f"({active_count} active, {disconnected_count} disconnected, {pending_count} pending)"
            ),
            source_ref="wazuh-agent-inventory",
            classification="asset",
            status=agent_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "agents": {
                    "total": len(agents),
                    "active": active_count,
                    "disconnected": disconnected_count,
                    "pending": pending_count,
                    "disconnected_pct": round(disconnected_pct, 1),
                    "by_status": dict(by_status),
                    "by_os_platform": dict(by_os),
                },
                "manager_status": bundle.get("manager_status", {}),
            },
        ))

        # ── A.8.7 — Protection against malware (alert levels) ────────────────
        # alerts_summary from /overview/agents contains agent alert level totals
        # Structure: {"connection": {...}, "agents": [...]}
        # Each agent entry may have alert_level counts — aggregate across all
        agent_summaries = alerts_summary.get("agents", []) if isinstance(alerts_summary, dict) else []

        critical_count = 0
        high_count = 0
        medium_count = 0
        low_count = 0

        for entry in agent_summaries:
            # Wazuh overview format varies by version; try common fields
            for level_key, level_val in (entry.get("alerts", {}) or {}).items():
                try:
                    level = int(level_key)
                    count = int(level_val)
                except (TypeError, ValueError):
                    continue
                if level == LEVEL_CRITICAL:
                    critical_count += count
                elif LEVEL_HIGH_MIN <= level <= LEVEL_HIGH_MAX:
                    high_count += count
                elif LEVEL_MEDIUM_MIN <= level <= LEVEL_MEDIUM_MAX:
                    medium_count += count
                else:
                    low_count += count

        malware_status = (
            "non-compliant" if critical_count > 0
            else "attention-required" if high_count > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"Wazuh alert summary: "
                f"{critical_count} critical, {high_count} high, "
                f"{medium_count} medium, {low_count} low"
            ),
            source_ref="wazuh-alerts",
            classification="incident",
            status=malware_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "alert_levels": {
                    "critical": critical_count,
                    "high": high_count,
                    "medium": medium_count,
                    "low": low_count,
                },
                "agents_sampled": len(agent_summaries),
            },
        ))

        # ── A.8.8 — Vulnerability summary (all agents, /vulnerability/agents) ──
        # vuln_summary: [{"agentId": "001", "Critical": 2, "High": 5, ...}, ...]
        critical_cves = sum(int(a.get("Critical", 0)) for a in vuln_summary)
        high_cves = sum(int(a.get("High", 0)) for a in vuln_summary)
        medium_cves = sum(int(a.get("Medium", 0)) for a in vuln_summary)
        low_cves = sum(int(a.get("Low", 0)) for a in vuln_summary)
        total_cves = critical_cves + high_cves + medium_cves + low_cves

        vuln_status = (
            "non-compliant" if critical_cves > 0
            else "attention-required" if high_cves > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.8",
            title=(
                f"Wazuh vulnerability summary: {total_cves} CVEs across "
                f"{len(vuln_summary)} agents "
                f"({critical_cves} critical, {high_cves} high, {medium_cves} medium)"
            ),
            source_ref="wazuh-vulnerabilities",
            classification="vulnerability",
            status=vuln_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "agents_with_vulns": len(vuln_summary),
                "cves": {
                    "total": total_cves,
                    "critical": critical_cves,
                    "high": high_cves,
                    "medium": medium_cves,
                    "low": low_cves,
                },
                "by_agent": [
                    {
                        "agent_id": a.get("agentId"),
                        "critical": a.get("Critical", 0),
                        "high": a.get("High", 0),
                        "medium": a.get("Medium", 0),
                        "low": a.get("Low", 0),
                    }
                    for a in vuln_summary[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Wazuh connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Wazuh sync (last_run=%s)", since or "never")

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
    WazuhConnector().run()
