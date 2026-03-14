"""NetBox network source-of-truth connector for ISMS CORE v2.0.

Queries the NetBox REST API and posts evidence to:
  a.5.9     — Inventory of information and other associated assets  (device inventory by site/type/status)
  a.8.20-22 — Network security  (IP address + prefix inventory)

Environment variables required:
  ISMS_API_URL      — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN    — connector bearer token from /admin/connectors/register
  NETBOX_URL        — NetBox base URL, e.g. http://netbox.corp.local
  NETBOX_API_TOKEN  — NetBox API token for the service account
  POLL_INTERVAL     — seconds between syncs (default: 86400 = 24h)
  BATCH_SIZE        — items per API call (default: 100)

NetBox service account permissions required (read-only):
  - Read access to DCIM (devices, interfaces)
  - Read access to IPAM (IP addresses, prefixes)
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
from netbox_client import NetBoxClient

logger = logging.getLogger(__name__)


class NetBoxConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "86400"))
        cfg = self._load_config()
        self.netbox = NetBoxClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — NetBox source-of-truth is always current, no delta needed."""
        devices = self.netbox.get_devices(limit=1000)
        ip_addresses = self.netbox.get_ip_addresses(limit=1000)
        prefixes = self.netbox.get_prefixes()
        interfaces = self.netbox.get_interfaces(limit=500)

        return [
            {
                "_type": "netbox_bundle",
                "devices": devices,
                "ip_addresses": ip_addresses,
                "prefixes": prefixes,
                "interfaces": interfaces,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        ip_addresses = bundle["ip_addresses"]
        prefixes = bundle["prefixes"]
        interfaces = bundle["interfaces"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.9 — Device inventory by site / type / status ─────────────────
        # NetBox device_type is a nested object: {"display": "...", ...}
        by_site: Counter = Counter(
            (d.get("site") or {}).get("display", "No Site")
            for d in devices
        )
        by_type: Counter = Counter(
            (d.get("device_type") or {}).get("display", "Unknown")
            for d in devices
        )
        by_status: Counter = Counter(
            (d.get("status") or {}).get("label", "Unknown")
            for d in devices
        )

        active_devices = [
            d for d in devices
            if (d.get("status") or {}).get("value") == "active"
        ]

        items.append(EvidenceItem(
            group_code="a.5.9",
            title=(
                f"NetBox device inventory: {len(devices)} devices "
                f"across {len(by_site)} sites "
                f"({len(active_devices)} active)"
            ),
            source_ref="netbox-device-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "devices": {
                    "total": len(devices),
                    "active": len(active_devices),
                    "by_site": dict(by_site),
                    "by_type": dict(by_type),
                    "by_status": dict(by_status),
                },
                "interfaces_total": len(interfaces),
                "sample_devices": [
                    {
                        "id": d.get("id"),
                        "name": d.get("name", ""),
                        "site": (d.get("site") or {}).get("display", ""),
                        "device_type": (d.get("device_type") or {}).get("display", ""),
                        "status": (d.get("status") or {}).get("label", ""),
                        "last_updated": d.get("last_updated", ""),
                    }
                    for d in devices[:50]
                ],
            },
        ))

        # ── A.8.20-22 — Network inventory (IPs + prefixes) ───────────────────
        by_ip_status: Counter = Counter(
            (addr.get("status") or {}).get("label", "Unknown")
            for addr in ip_addresses
        )
        by_vrf: Counter = Counter(
            (addr.get("vrf") or {}).get("display", "Global")
            for addr in ip_addresses
        )
        by_prefix_status: Counter = Counter(
            (p.get("status") or {}).get("label", "Unknown")
            for p in prefixes
        )

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"NetBox network inventory: {len(ip_addresses)} IP addresses, "
                f"{len(prefixes)} prefixes, "
                f"{len(by_vrf)} VRFs"
            ),
            source_ref="netbox-network-inventory",
            classification="network",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "ip_addresses": {
                    "total": len(ip_addresses),
                    "by_status": dict(by_ip_status),
                    "by_vrf": dict(by_vrf),
                },
                "prefixes": {
                    "total": len(prefixes),
                    "by_status": dict(by_prefix_status),
                },
                "sample_prefixes": [
                    {
                        "prefix": p.get("prefix", ""),
                        "status": (p.get("status") or {}).get("label", ""),
                        "vrf": (p.get("vrf") or {}).get("display", "Global"),
                        "site": (p.get("site") or {}).get("display", ""),
                        "description": p.get("description", ""),
                    }
                    for p in prefixes[:50]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("NetBox connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting NetBox sync (last_run=%s)", since or "never")

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
    NetBoxConnector().run()
