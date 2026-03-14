"""PRTG Network Monitor connector for ISMS CORE v2.0.

Queries the PRTG JSON REST API and posts evidence to:
  a.8.16  — Monitoring of activities  (monitoring coverage + alarm summary)
  a.8.20  — Network security          (monitored network device inventory)

Environment variables required:
  ISMS_API_URL    — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN  — connector bearer token from /admin/connectors/register
  PRTG_URL        — PRTG base URL, e.g. https://prtg.corp.local
  PRTG_API_TOKEN  — PRTG API token (preferred over username/password)
  PRTG_USERNAME   — PRTG username (if no API token)
  PRTG_PASSWORD   — PRTG password (if no API token)
  PRTG_VERIFY_SSL — "false" to skip TLS verification for self-signed certs
  POLL_INTERVAL   — seconds between syncs (default: 3600 = 1h)
  BATCH_SIZE      — items per API call (default: 100)

PRTG service account permissions required (read-only):
  - Access to all device groups to be monitored
  - Read access to alarms and sensors
  - No write access required
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from prtg_client import PRTGClient

logger = logging.getLogger(__name__)

# PRTG sensor/device priority levels: 1=None, 2=Low, 3=Medium, 4=High, 5=Priority
PRIORITY_LABELS = {1: "none", 2: "low", 3: "medium", 4: "high", 5: "priority"}


class PRTGConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # PRTG is typically polled more frequently (monitoring data changes often)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))  # 1h default
        cfg = self._load_config()
        self.prtg = PRTGClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — PRTG monitoring state is always current, no delta needed."""
        devices = self.prtg.get_devices()
        sensors = self.prtg.get_sensors()
        alarms = self.prtg.get_active_alarms()
        server_info = self.prtg.get_server_info()

        return [
            {
                "_type": "prtg_bundle",
                "devices": devices,
                "sensors": sensors,
                "alarms": alarms,
                "server_info": server_info,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        sensors = bundle["sensors"]
        alarms = bundle["alarms"]
        fetched_at = bundle["fetched_at"]

        active_devices = [d for d in devices if d.get("active")]

        # ── A.8.16 — Monitoring coverage + alarm summary ──────────────────────
        dev_up = sum(1 for d in active_devices if d["status"] == "up")
        dev_warning = sum(1 for d in active_devices if d["status"] == "warning")
        dev_down = sum(1 for d in active_devices if d["status"] == "down")
        dev_paused = sum(1 for d in active_devices if d["status"] == "paused")

        sen_up = sum(1 for s in sensors if s["status"] == "up")
        sen_warning = sum(1 for s in sensors if s["status"] == "warning")
        sen_down = sum(1 for s in sensors if s["status"] == "down")

        high_prio_alarms = [a for a in alarms if int(a.get("priority", 3)) >= 4]

        coverage_pct = round(dev_up / len(active_devices) * 100, 1) if active_devices else 0
        monitoring_status = (
            "compliant" if dev_down == 0 and not high_prio_alarms
            else "attention-required" if dev_warning > 0 or high_prio_alarms
            else "non-compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"PRTG monitoring: {len(active_devices)} devices "
                f"({dev_up} up, {dev_warning} warning, {dev_down} down, {dev_paused} paused) "
                f"— {len(sensors)} sensors, {len(alarms)} active alarms"
            ),
            source_ref="prtg-monitoring-status",
            classification="network",
            status=monitoring_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "monitoring_coverage_pct": coverage_pct,
                "monitoring_status": monitoring_status,
                "devices": {
                    "total": len(devices),
                    "active": len(active_devices),
                    "up": dev_up,
                    "warning": dev_warning,
                    "down": dev_down,
                    "paused": dev_paused,
                },
                "sensors": {
                    "total": len(sensors),
                    "up": sen_up,
                    "warning": sen_warning,
                    "down": sen_down,
                },
                "alarms": {
                    "total": len(alarms),
                    "high_priority": len(high_prio_alarms),
                    "list": alarms[:50],  # cap at 50 for storage
                },
                "devices_down": [
                    d for d in active_devices if d["status"] == "down"
                ],
            },
        ))

        # ── A.8.20 — Network device inventory ────────────────────────────────
        # Group devices by probe/location for inventory report
        by_group: dict[str, list] = {}
        for d in active_devices:
            grp = d.get("group") or "Ungrouped"
            by_group.setdefault(grp, []).append(d)

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"PRTG network inventory: {len(active_devices)} monitored devices "
                f"across {len(by_group)} groups"
            ),
            source_ref="prtg-network-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_devices": len(active_devices),
                "groups": {
                    grp: [
                        {
                            "name": d["name"],
                            "host": d["host"],
                            "location": d["location"],
                            "status": d["status"],
                            "probe": d["probe"],
                        }
                        for d in devs
                    ]
                    for grp, devs in by_group.items()
                },
            },
        ))

        return items

    def run(self) -> None:
        logger.info("PRTG connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting PRTG sync (last_run=%s)", since or "never")

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
    PRTGConnector().run()
