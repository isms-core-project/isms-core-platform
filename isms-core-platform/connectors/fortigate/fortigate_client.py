"""Fortinet FortiGate REST API client (FortiOS v7.x+).

Uses the FortiOS REST API v2 for policy, interface, VPN, and threat data.
Elastic integration reference: github.com/elastic/integrations/tree/main/packages/fortinet_fortigate

Environment variables:
  FORTIGATE_HOST       — HTTPS host, e.g. fortigate.corp.local or 192.168.1.1
  FORTIGATE_API_TOKEN  — REST API token (System → Administrators → REST API Admin)
  FORTIGATE_VERIFY_SSL — "false" to skip cert verification (self-signed, default: true)
  FORTIGATE_VDOM       — VDOM name (default: root)

FortiGate REST API token: create a REST API Administrator profile in
System → Administrators → Create New → REST API Admin (read-only profile sufficient).
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class FortiGateClient:
    def __init__(self, **cfg) -> None:
        host = (cfg.get('host') or os.environ["FORTIGATE_HOST"]).rstrip("/")
        if not host.startswith("http"):
            host = f"https://{host}"
        self._base = f"{host}/api/v2"
        self._token = cfg.get('api_token') or os.environ["FORTIGATE_API_TOKEN"]
        self._vdom = cfg.get('vdom') or os.environ.get("FORTIGATE_VDOM", "root")
        self._verify = (cfg.get('verify_ssl') or os.environ.get("FORTIGATE_VERIFY_SSL", "true")).lower() != "false"
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        })
        if not self._verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _get(self, path: str, params: dict | None = None) -> dict:
        p = {"vdom": self._vdom, **(params or {})}
        resp = self._session.get(
            f"{self._base}/{path.lstrip('/')}",
            params=p,
            verify=self._verify,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_list(self, path: str, params: dict | None = None) -> list[dict]:
        data = self._get(path, params)
        return data.get("results", [])

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_system_status(self) -> dict:
        """Return device info: hostname, serial, firmware version, uptime."""
        logger.info("Fetching FortiGate system status...")
        try:
            return self._get("monitor/system/status")
        except Exception as e:
            logger.warning("Could not fetch system status: %s", e)
            return {}

    def get_firewall_policies(self) -> list[dict]:
        """Return firewall security policy rules."""
        logger.info("Fetching firewall policies...")
        try:
            return self._get_list("cmdb/firewall/policy", {"format": "name|policyid|srcintf|dstintf|action|status|logtraffic|nat"})
        except Exception as e:
            logger.error("Failed to fetch firewall policies: %s", e)
            return []

    def get_interfaces(self) -> list[dict]:
        """Return network interfaces with IP, zone, and status."""
        logger.info("Fetching interfaces...")
        try:
            return self._get_list("cmdb/system/interface", {"format": "name|ip|type|status|zone|alias|vdom"})
        except Exception as e:
            logger.warning("Could not fetch interfaces: %s", e)
            return []

    def get_vpn_ssl_sessions(self) -> list[dict]:
        """Return active SSL-VPN sessions."""
        logger.info("Fetching SSL-VPN sessions...")
        try:
            data = self._get("monitor/vpn/ssl")
            return data.get("results", {}).get("users", [])
        except Exception as e:
            logger.warning("Could not fetch SSL-VPN sessions: %s", e)
            return []

    def get_vpn_ipsec_tunnels(self) -> list[dict]:
        """Return IPsec VPN tunnels with status."""
        logger.info("Fetching IPsec tunnels...")
        try:
            return self._get_list("monitor/vpn/ipsec")
        except Exception as e:
            logger.warning("Could not fetch IPsec tunnels: %s", e)
            return []

    def get_ips_attacks(self) -> list[dict]:
        """Return recent IPS/threat detections (last 100)."""
        logger.info("Fetching IPS threat events...")
        try:
            data = self._get("monitor/ips/anomaly", {"count": 100})
            return data.get("results", [])
        except Exception as e:
            logger.warning("Could not fetch IPS events (check IPS licence): %s", e)
            return []

    def get_system_performance(self) -> dict:
        """Return CPU, memory, and session counts."""
        try:
            return self._get("monitor/system/performance/status")
        except Exception as e:
            logger.warning("Could not fetch performance stats: %s", e)
            return {}
