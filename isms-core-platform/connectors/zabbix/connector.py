"""Zabbix monitoring connector for ISMS CORE v2.0.

Queries the Zabbix JSON-RPC 2.0 API and posts evidence to:
  a.8.16  — Monitoring of activities  (host inventory + active problem summary)

Environment variables required:
  ISMS_API_URL    — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN  — connector bearer token from /admin/connectors/register
  ZABBIX_URL      — Zabbix base URL, e.g. http://zabbix.corp.local
  ZABBIX_USERNAME — Zabbix service account username
  ZABBIX_PASSWORD — Zabbix service account password
  POLL_INTERVAL   — seconds between syncs (default: 3600 = 1h)
  BATCH_SIZE      — items per API call (default: 100)

Zabbix service account permissions required (read-only):
  - Read access to all host groups
  - Read access to problems and triggers
  - No write access required
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from zabbix_client import ZabbixClient

logger = logging.getLogger(__name__)

# Zabbix problem severity: 0=Not classified, 1=Information, 2=Warning, 3=Average, 4=High, 5=Disaster
SEVERITY_LABELS = {
    "0": "not_classified",
    "1": "information",
    "2": "warning",
    "3": "average",
    "4": "high",
    "5": "disaster",
}

# Zabbix host availability: 0=Unknown, 1=Available, 2=Unavailable
AVAILABILITY_LABELS = {
    "0": "unknown",
    "1": "available",
    "2": "unavailable",
}


class ZabbixConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.zabbix = ZabbixClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Zabbix monitoring state is always current, no delta needed."""
        hosts = self.zabbix.get_hosts()
        problems = self.zabbix.get_problems(limit=500)
        active_trigger_count = self.zabbix.get_triggers_count()

        return [
            {
                "_type": "zabbix_bundle",
                "hosts": hosts,
                "problems": problems,
                "active_trigger_count": active_trigger_count,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        hosts = bundle["hosts"]
        problems = bundle["problems"]
        active_trigger_count = bundle["active_trigger_count"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.16 — Host inventory + monitoring coverage ─────────────────────
        by_availability: Counter = Counter(
            AVAILABILITY_LABELS.get(str(h.get("available", "0")), "unknown")
            for h in hosts
        )
        # Zabbix host status: 0=enabled/monitored, 1=disabled
        enabled = [h for h in hosts if str(h.get("status", "0")) == "0"]
        disabled = [h for h in hosts if str(h.get("status", "0")) != "0"]

        host_available = by_availability.get("available", 0)
        host_unavailable = by_availability.get("unavailable", 0)
        host_unknown = by_availability.get("unknown", 0)

        monitoring_status = (
            "compliant" if host_unavailable == 0 and len(problems) == 0
            else "attention-required" if host_unavailable > 0 or len(problems) > 0
            else "non-compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"Zabbix monitoring: {len(hosts)} hosts "
                f"({host_available} available, {host_unavailable} unavailable, {host_unknown} unknown) "
                f"— {len(enabled)} enabled, {len(disabled)} disabled"
            ),
            source_ref="zabbix-host-inventory",
            classification="network",
            status=monitoring_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hosts": {
                    "total": len(hosts),
                    "enabled": len(enabled),
                    "disabled": len(disabled),
                    "available": host_available,
                    "unavailable": host_unavailable,
                    "unknown": host_unknown,
                },
                "active_triggers": active_trigger_count,
            },
        ))

        # ── A.8.16 — Active problems by severity ──────────────────────────────
        by_severity: Counter = Counter(
            SEVERITY_LABELS.get(str(p.get("severity", "0")), "not_classified")
            for p in problems
        )
        disaster_count = by_severity.get("disaster", 0)
        high_count = by_severity.get("high", 0)

        problem_status = (
            "non-compliant" if disaster_count > 0
            else "attention-required" if high_count > 0 or len(problems) > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"Zabbix active problems: {len(problems)} total "
                f"({disaster_count} disaster, {high_count} high, "
                f"{by_severity.get('average', 0)} average, "
                f"{by_severity.get('warning', 0)} warning)"
            ),
            source_ref="zabbix-active-problems",
            classification="network",
            status=problem_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_problems": len(problems),
                "by_severity": dict(by_severity),
                "active_triggers": active_trigger_count,
                "recent_problems": [
                    {
                        "eventid": p.get("eventid"),
                        "name": p.get("name", ""),
                        "severity": SEVERITY_LABELS.get(str(p.get("severity", "0")), "not_classified"),
                        "clock": p.get("clock"),
                        "acknowledged": p.get("acknowledged", "0"),
                    }
                    for p in problems[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Zabbix connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Zabbix sync (last_run=%s)", since or "never")

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
    ZabbixConnector().run()
