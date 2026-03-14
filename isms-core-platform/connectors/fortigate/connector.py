"""Fortinet FortiGate connector for ISMS CORE v2.0.

Pulls from the FortiOS REST API and posts evidence to:
  a.8.15  — Logging                   (IPS/threat detections, security events)
  a.8.20  — Network security          (firewall policy analysis, interface status)
  a.8.22  — Configuration of network  (rule count, deny rules, logging enabled)
  a.6.7   — Remote working            (SSL-VPN + IPsec sessions)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  FORTIGATE_HOST        — FortiGate hostname/IP
  FORTIGATE_API_TOKEN   — REST API token
  FORTIGATE_VERIFY_SSL  — "false" for self-signed certs
  FORTIGATE_VDOM        — VDOM name (default: root)
  POLL_INTERVAL         — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from fortigate_client import FortiGateClient

logger = logging.getLogger(__name__)


class FortiGateConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.fg = FortiGateClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        status = self.fg.get_system_status()
        policies = self.fg.get_firewall_policies()
        interfaces = self.fg.get_interfaces()
        vpn_ssl = self.fg.get_vpn_ssl_sessions()
        vpn_ipsec = self.fg.get_vpn_ipsec_tunnels()
        ips_events = self.fg.get_ips_attacks()

        return [{"_type": "fortigate_bundle", "status": status, "policies": policies,
                 "interfaces": interfaces, "vpn_ssl": vpn_ssl, "vpn_ipsec": vpn_ipsec,
                 "ips_events": ips_events, "fetched_at": datetime.now(timezone.utc).isoformat()}]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        policies = bundle["policies"]
        interfaces = bundle["interfaces"]
        vpn_ssl = bundle["vpn_ssl"]
        vpn_ipsec = bundle["vpn_ipsec"]
        ips_events = bundle["ips_events"]
        status = bundle["status"]
        fetched_at = bundle["fetched_at"]

        # Device info for titles
        sys_info = status.get("results", {}) if isinstance(status.get("results"), dict) else {}
        hostname = sys_info.get("hostname", "FortiGate")
        version = sys_info.get("version", "")

        # ── A.8.20 + A.8.22 — Network security + config of network services ────
        enabled = [p for p in policies if str(p.get("status", "enable")) == "enable"]
        deny_rules = [p for p in enabled if str(p.get("action", "")).lower() in ("deny", "block")]
        log_all = [p for p in enabled if str(p.get("logtraffic", "")) in ("all", "utm")]
        no_log = [p for p in enabled if str(p.get("logtraffic", "")) == "disable"]

        by_action: dict[str, int] = Counter(str(p.get("action", "unknown")).lower() for p in enabled)

        active_if = [i for i in interfaces if str(i.get("status", "down")).lower() == "up"]

        network_status = "compliant"
        if len(no_log) > len(enabled) * 0.2:  # >20% rules have no logging
            network_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"{hostname} firewall policies: {len(enabled)} active rules "
                f"({len(deny_rules)} deny, {len(active_if)} interfaces up)"
            ),
            source_ref="fortigate-network-security",
            classification="network",
            status=network_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "firmware_version": version,
                "policies": {
                    "total": len(policies),
                    "enabled": len(enabled),
                    "deny_rules": len(deny_rules),
                    "allow_with_logging": len(log_all),
                    "no_logging": len(no_log),
                    "by_action": dict(by_action),
                },
                "interfaces": {
                    "total": len(interfaces),
                    "up": len(active_if),
                    "list": [{"name": i.get("name"), "ip": i.get("ip"),
                               "zone": i.get("zone"), "status": i.get("status")} for i in interfaces],
                },
                "policy_list": [
                    {"policyid": p.get("policyid"), "name": p.get("name"),
                     "srcintf": p.get("srcintf"), "dstintf": p.get("dstintf"),
                     "action": p.get("action"), "logtraffic": p.get("logtraffic")}
                    for p in enabled[:50]
                ],
            },
        ))

        # ── A.8.15 — Logging (IPS/threat detection evidence) ──────────────────
        by_severity: dict[str, int] = Counter(
            str(e.get("severity", "unknown")).lower() for e in ips_events
        )
        critical_events = [e for e in ips_events if str(e.get("severity", "")).lower() == "critical"]

        log_status = "compliant" if not critical_events else "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"{hostname} security events: {len(ips_events)} IPS detections "
                f"({len(critical_events)} critical)"
            ),
            source_ref="fortigate-security-log",
            classification="network",
            status=log_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "ips_events_total": len(ips_events),
                "by_severity": dict(by_severity),
                "critical_count": len(critical_events),
                "recent_events": ips_events[:30],
            },
        ))

        # ── A.6.7 — Remote working (VPN evidence) ─────────────────────────────
        ssl_count = len(vpn_ssl)
        ipsec_up = sum(1 for t in vpn_ipsec if str(t.get("rgwy", "")).lower() not in ("", "0.0.0.0"))

        items.append(EvidenceItem(
            group_code="a.6.7-8",
            title=(
                f"{hostname} VPN: {ssl_count} active SSL-VPN sessions, "
                f"{len(vpn_ipsec)} IPsec tunnels ({ipsec_up} up)"
            ),
            source_ref="fortigate-vpn-status",
            classification="network",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "hostname": hostname,
                "ssl_vpn_sessions": ssl_count,
                "ipsec_tunnels": len(vpn_ipsec),
                "ipsec_up": ipsec_up,
                "vpn_ssl_users": [
                    {"user": s.get("user_name", s.get("username", "")),
                     "source_ip": s.get("source_ip", s.get("src_ip", ""))}
                    for s in vpn_ssl[:20]
                ],
                "ipsec_tunnel_list": vpn_ipsec[:20],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("FortiGate connector starting (poll_interval=%ds)", self.poll_interval)
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
    FortiGateConnector().run()
