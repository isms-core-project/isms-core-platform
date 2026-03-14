"""SentinelOne connector for ISMS CORE v2.0.

Pulls from the SentinelOne Management Console REST API and posts evidence to:
  a.8.1-7-18-19 — Endpoint Security  (agent inventory + open threats)

Environment variables required:
  ISMS_API_URL             — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN           — connector bearer token from /admin/connectors/register
  SENTINELONE_URL          — Management console URL, e.g. https://usea1.sentinelone.net
  SENTINELONE_API_TOKEN    — API token generated from the console
  POLL_INTERVAL            — seconds between syncs (default: 86400 = 24h)

API permissions required:
  Endpoints View
  Threats View
  Exclusions View
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from sentinelone_client import SentinelOneClient

logger = logging.getLogger(__name__)


class SentinelOneConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.s1 = SentinelOneClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — SentinelOne data is always current state."""
        agents = self.s1.get_agents()
        threats = self.s1.get_threats()
        exclusions = self.s1.get_exclusions()

        return [
            {
                "_type": "sentinelone_bundle",
                "agents": agents,
                "threats": threats,
                "exclusions": exclusions,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        agents = bundle["agents"]
        threats = bundle["threats"]
        exclusions = bundle["exclusions"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1-7-18-19 — Agent inventory ──────────────────────────────────
        active_agents = [a for a in agents if a.get("isActive") and not a.get("isDecommissioned")]
        infected_agents = [a for a in agents if a.get("infected")]
        decommissioned = [a for a in agents if a.get("isDecommissioned")]
        by_os: dict[str, int] = Counter(a.get("osName", "Unknown") for a in agents)

        agent_status = "compliant"
        if infected_agents:
            agent_status = "non-compliant"
        elif decommissioned:
            agent_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"SentinelOne agent inventory: {len(agents)} total "
                f"({len(active_agents)} active, "
                f"{len(infected_agents)} infected, "
                f"{len(decommissioned)} decommissioned)"
            ),
            source_ref="sentinelone-agent-inventory",
            classification="asset",
            status=agent_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_agents": len(agents),
                "active_agents": len(active_agents),
                "infected_agents": len(infected_agents),
                "decommissioned_agents": len(decommissioned),
                "by_os": dict(by_os),
                "agents": [
                    {
                        "id": a.get("id"),
                        "computer_name": a.get("computerName"),
                        "network_status": a.get("networkStatus"),
                        "active_threats": a.get("activeThreats"),
                        "is_active": a.get("isActive"),
                        "infected": a.get("infected"),
                        "is_decommissioned": a.get("isDecommissioned"),
                        "os_name": a.get("osName"),
                        "agent_version": a.get("agentVersion"),
                    }
                    for a in agents
                ],
            },
        ))

        # ── A.8.1-7-18-19 — Open threats ─────────────────────────────────────
        by_classification: dict[str, int] = Counter(
            t.get("classification", "Unknown") for t in threats
        )
        by_mitigation: dict[str, int] = Counter(
            t.get("mitigationStatus", "Unknown") for t in threats
        )

        threat_status = "compliant"
        if threats:
            threat_status = "non-compliant" if len(threats) > 10 else "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"SentinelOne threats: {len(threats)} unresolved "
                f"({by_classification.get('Malware', 0)} malware, "
                f"{by_classification.get('Ransomware', 0)} ransomware)"
            ),
            source_ref="sentinelone-threats",
            classification="incident",
            status=threat_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_open_threats": len(threats),
                "by_classification": dict(by_classification),
                "by_mitigation_status": dict(by_mitigation),
                "threats": [
                    {
                        "agent_computer_name": t.get("agentComputerName"),
                        "classification": t.get("classification"),
                        "confidence_level": t.get("confidenceLevel"),
                        "mitigation_status": t.get("mitigationStatus"),
                        "created_at": t.get("createdAt"),
                    }
                    for t in threats[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("SentinelOne connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting SentinelOne sync (last_run=%s)", since or "never")

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
    SentinelOneConnector().run()
