"""Cisco ASA / Firepower connector for ISMS CORE v2.0.

Pulls from the Cisco ASA REST API and posts evidence to:
  a.8.20  — Network security          (ACL analysis, interface status)
  a.8.22  — Configuration of network  (NAT rules, network device config)
  a.6.7   — Remote working            (AnyConnect/L2L VPN sessions)

Environment variables required:
  ISMS_API_URL            — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN          — connector bearer token from /admin/connectors/register
  CISCO_ASA_HOST          — ASA hostname/IP
  CISCO_ASA_USERNAME      — ASA admin username
  CISCO_ASA_PASSWORD      — ASA admin password
  CISCO_ASA_VERIFY_SSL    — "false" for self-signed certs
  CISCO_ASA_PORT          — REST API port (default: 443)
  POLL_INTERVAL           — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from cisco_asa_client import CiscoASAClient

logger = logging.getLogger(__name__)


class CiscoASAConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.asa = CiscoASAClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        device_info = self.asa.get_device_info()
        interfaces = self.asa.get_interfaces()
        acls = self.asa.get_acl_list()
        nat_rules = self.asa.get_nat_rules()
        vpn_sessions = self.asa.get_vpn_sessions()

        return [{"_type": "asa_bundle", "device_info": device_info, "interfaces": interfaces,
                 "acls": acls, "nat_rules": nat_rules, "vpn_sessions": vpn_sessions,
                 "fetched_at": datetime.now(timezone.utc).isoformat()}]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        device_info = bundle["device_info"]
        interfaces = bundle["interfaces"]
        acls = bundle["acls"]
        nat_rules = bundle["nat_rules"]
        vpn_sessions = bundle["vpn_sessions"]
        fetched_at = bundle["fetched_at"]

        hostname = device_info.get("asaVersion", "Cisco ASA")
        dev_type = device_info.get("deviceType", "")
        model = device_info.get("hardwareModel", "")

        up_if = [i for i in interfaces if not i.get("managementOnly", False)]
        permit_acls = [a for a in acls if str(a.get("permit", "")).lower() == "true"]
        deny_acls = [a for a in acls if str(a.get("permit", "")).lower() == "false"]

        # ── A.8.20 + A.8.22 — Network security ───────────────────────────────
        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"Cisco ASA {model}: {len(acls)} ACL entries "
                f"({len(permit_acls)} permit, {len(deny_acls)} deny) "
                f"— {len(nat_rules)} NAT rules, {len(up_if)} interfaces"
            ),
            source_ref="cisco-asa-network-security",
            classification="network",
            status="compliant",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "device_type": dev_type,
                "model": model,
                "acls": {"total": len(acls), "permit": len(permit_acls), "deny": len(deny_acls)},
                "nat_rules": len(nat_rules),
                "interfaces": [
                    {"name": i.get("name", i.get("id", "")),
                     "ipAddress": i.get("ipAddress", {}).get("ip", {}).get("value", ""),
                     "securityLevel": i.get("securityLevel")}
                    for i in interfaces[:30]
                ],
                "acl_sample": acls[:30],
            },
        ))

        # ── A.6.7 — Remote working (VPN) ─────────────────────────────────────
        vpn_count = len(vpn_sessions)
        anyconnect = [s for s in vpn_sessions if "anyconnect" in str(s.get("tunnelType", "")).lower()]
        l2l = [s for s in vpn_sessions if "l2l" in str(s.get("tunnelType", "")).lower() or
               "ipsec" in str(s.get("tunnelType", "")).lower()]

        items.append(EvidenceItem(
            group_code="a.6.7-8",
            title=(
                f"Cisco ASA VPN: {vpn_count} active sessions "
                f"({len(anyconnect)} AnyConnect, {len(l2l)} L2L)"
            ),
            source_ref="cisco-asa-vpn-status",
            classification="network",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "model": model,
                "vpn_sessions_total": vpn_count,
                "anyconnect_sessions": len(anyconnect),
                "l2l_sessions": len(l2l),
                "sessions": vpn_sessions[:20],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Cisco ASA connector starting (poll_interval=%ds)", self.poll_interval)
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
    CiscoASAConnector().run()
