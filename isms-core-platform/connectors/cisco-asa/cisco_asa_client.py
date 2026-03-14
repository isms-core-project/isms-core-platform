"""Cisco ASA / Firepower REST API client.

Uses the Cisco ASA REST API (v1.x) for policy and interface data.
Supports both ASA (standalone) and FMC (Firepower Management Centre).

Elastic integration reference: github.com/elastic/integrations/tree/main/packages/cisco_asa

Environment variables:
  CISCO_ASA_HOST       — HTTPS host, e.g. asa.corp.local
  CISCO_ASA_USERNAME   — ASA username (privilege 15 or read-only)
  CISCO_ASA_PASSWORD   — ASA password
  CISCO_ASA_VERIFY_SSL — "false" to skip cert check (default: true)
  CISCO_ASA_PORT       — REST API port (default: 443; some use 55443)

ASA REST API must be enabled: `rest-api enable` in ASA config.
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class CiscoASAClient:
    def __init__(self, **cfg) -> None:
        host = (cfg.get('host') or os.environ["CISCO_ASA_HOST"]).rstrip("/")
        if not host.startswith("http"):
            host = f"https://{host}"
        port = cfg.get('port') or os.environ.get("CISCO_ASA_PORT", "443")
        if port != "443":
            host = f"{host}:{port}"
        self._base = f"{host}/api"
        self._verify = (cfg.get('verify_ssl') or os.environ.get("CISCO_ASA_VERIFY_SSL", "true")).lower() != "false"
        self._session = requests.Session()
        self._session.auth = (
            cfg.get('username') or os.environ["CISCO_ASA_USERNAME"],
            cfg.get('password') or os.environ["CISCO_ASA_PASSWORD"],
        )
        self._session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "ISMS-CORE-Connector/2.0",
        })
        if not self._verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _get(self, path: str, params: dict | None = None) -> dict:
        resp = self._session.get(
            f"{self._base}/{path.lstrip('/')}",
            params=params or {},
            verify=self._verify,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_all(self, path: str) -> list[dict]:
        """Paginate through all results using offset/limit."""
        items: list[dict] = []
        offset = 0
        limit = 100
        while True:
            data = self._get(path, {"limit": limit, "offset": offset})
            page = data.get("items", [])
            items.extend(page)
            total = data.get("rangeInfo", {}).get("total", len(items))
            offset += len(page)
            if not page or offset >= total:
                break
        return items

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_device_info(self) -> dict:
        """Return ASA device info (model, version, serial)."""
        logger.info("Fetching ASA device info...")
        try:
            return self._get("asa/version")
        except Exception as e:
            logger.warning("Could not fetch device info: %s", e)
            return {}

    def get_interfaces(self) -> list[dict]:
        """Return physical + logical interfaces."""
        logger.info("Fetching interfaces...")
        try:
            items = self._get_all("interfaces/physical")
            return items
        except Exception as e:
            logger.warning("Could not fetch interfaces: %s", e)
            return []

    def get_access_groups(self) -> list[dict]:
        """Return ACL bindings (access-group interface pairings)."""
        logger.info("Fetching access groups...")
        try:
            data = self._get("objects/networkgroups")
            return data.get("items", [])
        except Exception as e:
            logger.warning("Could not fetch access groups: %s", e)
            return []

    def get_nat_rules(self) -> list[dict]:
        """Return NAT rules (network translation evidence)."""
        logger.info("Fetching NAT rules...")
        try:
            items = self._get_all("nat/auto")
            return items
        except Exception as e:
            logger.warning("Could not fetch NAT rules: %s", e)
            return []

    def get_vpn_sessions(self) -> list[dict]:
        """Return active VPN sessions (AnyConnect + L2L)."""
        logger.info("Fetching VPN sessions...")
        try:
            data = self._get("vpn/sessiondb/detail")
            return data.get("items", [])
        except Exception as e:
            logger.warning("Could not fetch VPN sessions: %s", e)
            return []

    def get_acl_list(self) -> list[dict]:
        """Return extended ACLs (firewall rule evidence)."""
        logger.info("Fetching ACLs...")
        try:
            items = self._get_all("acl/extended")
            return items
        except Exception as e:
            logger.warning("Could not fetch ACLs: %s", e)
            return []
