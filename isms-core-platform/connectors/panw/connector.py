"""Palo Alto Networks PAN-OS connector for ISMS CORE v2.0.

Pulls from the PAN-OS XML API and posts evidence to:
  a.8.15  — Logging                   (threat log events)
  a.8.20  — Network security          (security rules, interface status)
  a.8.22  — Configuration of network  (zone segmentation, rule count)
  a.6.7   — Remote working            (IPsec VPN tunnels)

Environment variables required:
  ISMS_API_URL        — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN      — connector bearer token from /admin/connectors/register
  PANW_HOST           — firewall or Panorama hostname/IP
  PANW_API_KEY        — PAN-OS API key
  PANW_VERIFY_SSL     — "false" for self-signed certs
  PANW_VSYS           — virtual system (default: vsys1)
  POLL_INTERVAL       — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from panw_client import PANWClient

logger = logging.getLogger(__name__)


class PanwConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.panw = PANWClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        sys_info = self.panw.get_system_info()
        rules = self.panw.get_security_rules()
        interfaces = self.panw.get_interfaces()
        zones = self.panw.get_zones()
        tunnels = self.panw.get_vpn_tunnels()
        threats = self.panw.get_threat_log()

        return [{"_type": "panw_bundle", "sys_info": sys_info, "rules": rules,
                 "interfaces": interfaces, "zones": zones, "tunnels": tunnels,
                 "threats": threats, "fetched_at": datetime.now(timezone.utc).isoformat()}]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        sys_info = bundle["sys_info"]
        rules = bundle["rules"]
        interfaces = bundle["interfaces"]
        zones = bundle["zones"]
        tunnels = bundle["tunnels"]
        threats = bundle["threats"]
        fetched_at = bundle["fetched_at"]

        hostname = sys_info.get("hostname", "PAN-OS")
        version = sys_info.get("sw-version", "")

        # ── A.8.20 + A.8.22 — Network security + zone segmentation ───────────
        deny_rules = [r for r in rules if r.get("action", "") in ("deny", "drop", "reset-both", "reset-client", "reset-server")]
        allow_rules = [r for r in rules if r.get("action", "") == "allow"]
        logged_rules = [r for r in rules if r.get("log-start") == "yes" or r.get("log-end") == "yes"]

        up_interfaces = [i for i in interfaces if i.get("state", "") == "up"]
        zone_count = len(zones)

        network_status = "compliant"
        if len(logged_rules) < len(rules) * 0.8:  # <80% rules logging
            network_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"{hostname} security policy: {len(rules)} rules "
                f"({len(allow_rules)} allow, {len(deny_rules)} deny) "
                f"— {zone_count} zones, {len(up_interfaces)} interfaces up"
            ),
            source_ref="panw-network-security",
            classification="network",
            status=network_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "os_version": version,
                "rules": {
                    "total": len(rules),
                    "allow": len(allow_rules),
                    "deny": len(deny_rules),
                    "logged": len(logged_rules),
                },
                "zones": [{"name": z.get("name"), "interfaces": z.get("interfaces", [])} for z in zones],
                "interfaces": [{"name": i.get("name"), "state": i.get("state"),
                                 "ip": i.get("ip"), "zone": i.get("zone")} for i in interfaces],
                "rules_list": rules[:50],
            },
        ))

        # ── A.8.15 — Threat logging ───────────────────────────────────────────
        by_severity: dict[str, int] = Counter(t.get("severity", "unknown").lower() for t in threats)
        critical_threats = [t for t in threats if t.get("severity", "").lower() in ("critical", "high")]

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"{hostname} threat log: {len(threats)} events "
                f"({len(critical_threats)} critical/high)"
            ),
            source_ref="panw-threat-log",
            classification="network",
            status="attention-required" if critical_threats else "compliant",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "threat_events": len(threats),
                "by_severity": dict(by_severity),
                "critical_high_count": len(critical_threats),
                "recent_threats": threats[:30],
            },
        ))

        # ── A.6.7 — Remote working (VPN) ─────────────────────────────────────
        active_tunnels = [t for t in tunnels if t.get("state", "").lower() == "active"]

        items.append(EvidenceItem(
            group_code="a.6.7-8",
            title=(
                f"{hostname} IPsec VPN: {len(tunnels)} tunnels "
                f"({len(active_tunnels)} active)"
            ),
            source_ref="panw-vpn-status",
            classification="network",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "total_tunnels": len(tunnels),
                "active_tunnels": len(active_tunnels),
                "tunnels": tunnels[:30],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("PAN-OS connector starting (poll_interval=%ds)", self.poll_interval)
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
    PanwConnector().run()
