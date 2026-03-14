"""Palo Alto Networks PAN-OS API client.

Supports both PAN-OS XML API (all versions) and PAN-OS REST API (v10+).
Panorama support: set PANW_PANORAMA=true and provide device serial via PANW_TARGET_DEVICE.

Elastic integration reference: github.com/elastic/integrations/tree/main/packages/panw

Environment variables:
  PANW_HOST          — hostname/IP of firewall or Panorama
  PANW_API_KEY       — PAN-OS API key (generate: GET /api/?type=keygen&user=x&password=y)
  PANW_VERIFY_SSL    — "false" to skip cert verification (default: true)
  PANW_VSYS          — Virtual system (default: vsys1)
  PANW_PANORAMA      — "true" if connecting via Panorama (default: false)
  PANW_TARGET_DEVICE — serial number of managed device (required if PANW_PANORAMA=true)
"""

import logging
import os
import xml.etree.ElementTree as ET

import requests
import urllib3

logger = logging.getLogger(__name__)


class PANWClient:
    def __init__(self, **cfg) -> None:
        host = (cfg.get('host') or os.environ["PANW_HOST"]).rstrip("/")
        if not host.startswith("http"):
            host = f"https://{host}"
        self._base = f"{host}/api/"
        self._key = cfg.get('api_key') or os.environ["PANW_API_KEY"]
        self._vsys = cfg.get('vsys') or os.environ.get("PANW_VSYS", "vsys1")
        self._verify = (cfg.get('verify_ssl') or os.environ.get("PANW_VERIFY_SSL", "true")).lower() != "false"
        self._panorama = (cfg.get('panorama') or os.environ.get("PANW_PANORAMA", "false")).lower() == "true"
        self._target = cfg.get('target_device') or os.environ.get("PANW_TARGET_DEVICE", "")
        self._session = requests.Session()
        if not self._verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _xml_get(self, params: dict) -> ET.Element:
        """Perform an XML API call and return the parsed response element."""
        p = {"key": self._key, **params}
        if self._panorama and self._target:
            p["target"] = self._target
        resp = self._session.get(self._base, params=p, verify=self._verify, timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        if root.attrib.get("status") != "success":
            msg = root.findtext("./msg") or resp.text[:200]
            raise RuntimeError(f"PAN-OS API error: {msg}")
        return root

    def _op(self, cmd: str) -> ET.Element:
        return self._xml_get({"type": "op", "cmd": cmd})

    def _config_get(self, xpath: str) -> ET.Element:
        return self._xml_get({"type": "config", "action": "get", "xpath": xpath})

    def _elem_to_dict(self, elem: ET.Element | None) -> dict:
        """Shallow element → dict (attributes + direct text children)."""
        if elem is None:
            return {}
        result = dict(elem.attrib)
        for child in elem:
            val = child.text or ""
            if child.tag in result:
                existing = result[child.tag]
                result[child.tag] = existing if isinstance(existing, list) else [existing]
                result[child.tag].append(val)
            else:
                result[child.tag] = val
        return result

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_system_info(self) -> dict:
        """Return device model, serial, OS version, hostname."""
        logger.info("Fetching PAN-OS system info...")
        try:
            root = self._op("<show><system><info></info></system></show>")
            si = root.find("./result/system")
            if si is None:
                return {}
            return {tag.tag: tag.text for tag in si}
        except Exception as e:
            logger.warning("Could not fetch system info: %s", e)
            return {}

    def get_security_rules(self) -> list[dict]:
        """Return all security policy rules from running config."""
        logger.info("Fetching PAN-OS security rules...")
        try:
            xpath = f"/config/devices/entry/vsys/entry[@name='{self._vsys}']/rulebase/security/rules"
            root = self._config_get(xpath)
            rules = []
            for entry in root.findall(".//entry"):
                rule = {"name": entry.attrib.get("name", "")}
                for child in entry:
                    if len(child) == 0:
                        rule[child.tag] = child.text or ""
                    else:
                        rule[child.tag] = [m.text for m in child if m.text]
                rules.append(rule)
            logger.info("Fetched %d security rules", len(rules))
            return rules
        except Exception as e:
            logger.error("Failed to fetch security rules: %s", e)
            return []

    def get_interfaces(self) -> list[dict]:
        """Return interface state: name, IP, zone, link status."""
        logger.info("Fetching PAN-OS interfaces...")
        try:
            root = self._op("<show><interface>all</interface></show>")
            interfaces = []
            for hw in root.findall("./result/hw/entry"):
                interfaces.append({
                    "name": hw.findtext("name", ""),
                    "state": hw.findtext("state", ""),
                    "mac": hw.findtext("mac", ""),
                    "speed": hw.findtext("speed", ""),
                })
            for ifnet in root.findall("./result/ifnet/entry"):
                name = ifnet.findtext("name", "")
                for iface in interfaces:
                    if iface["name"] == name:
                        iface["ip"] = ifnet.findtext("ip", "")
                        iface["zone"] = ifnet.findtext("zone", "")
                        iface["vsys"] = ifnet.findtext("vsys", "")
            logger.info("Fetched %d interfaces", len(interfaces))
            return interfaces
        except Exception as e:
            logger.warning("Could not fetch interfaces: %s", e)
            return []

    def get_vpn_tunnels(self) -> list[dict]:
        """Return IPsec tunnel status."""
        logger.info("Fetching IPsec tunnels...")
        try:
            root = self._op("<show><vpn><ipsec></ipsec></vpn></show>")
            tunnels = []
            for entry in root.findall("./result/entry"):
                tunnels.append({
                    "name": entry.findtext("name", ""),
                    "gwid": entry.findtext("gwid", ""),
                    "id": entry.findtext("id", ""),
                    "state": entry.findtext("state", ""),
                    "inner_if": entry.findtext("inner-if", ""),
                    "outer_if": entry.findtext("outer-if", ""),
                })
            logger.info("Fetched %d IPsec tunnels", len(tunnels))
            return tunnels
        except Exception as e:
            logger.warning("Could not fetch VPN tunnels: %s", e)
            return []

    def get_threat_log(self, nlogs: int = 200) -> list[dict]:
        """Return recent threat log entries (requires Threat Prevention licence)."""
        logger.info("Fetching PAN-OS threat log...")
        try:
            root = self._xml_get({
                "type": "log",
                "log-type": "threat",
                "nlogs": nlogs,
            })
            entries = []
            for log in root.findall(".//entry"):
                entries.append({
                    "time": log.findtext("time_generated", ""),
                    "src": log.findtext("src", ""),
                    "dst": log.findtext("dst", ""),
                    "app": log.findtext("app", ""),
                    "threat_name": log.findtext("threatid", ""),
                    "severity": log.findtext("severity", ""),
                    "action": log.findtext("action", ""),
                    "rule": log.findtext("rule", ""),
                })
            logger.info("Fetched %d threat log entries", len(entries))
            return entries
        except Exception as e:
            logger.warning("Could not fetch threat log (check licence): %s", e)
            return []

    def get_zones(self) -> list[dict]:
        """Return security zones (segmentation evidence)."""
        logger.info("Fetching PAN-OS zones...")
        try:
            xpath = f"/config/devices/entry/vsys/entry[@name='{self._vsys}']/zone"
            root = self._config_get(xpath)
            zones = []
            for entry in root.findall(".//entry"):
                zones.append({
                    "name": entry.attrib.get("name", ""),
                    "type": (entry.find("network") or ET.Element("x")).tag,
                    "interfaces": [m.text for m in entry.findall("./network/*/member") if m.text],
                })
            logger.info("Fetched %d zones", len(zones))
            return zones
        except Exception as e:
            logger.warning("Could not fetch zones: %s", e)
            return []
