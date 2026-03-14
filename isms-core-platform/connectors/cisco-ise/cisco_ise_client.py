"""Cisco ISE REST API client (ERS API + MNT API).

Uses the Cisco ISE External RESTful Services (ERS) API for policy and endpoint data.
Elastic integration reference: github.com/elastic/integrations/tree/main/packages/cisco_ise

Environment variables:
  CISCO_ISE_HOST       — ISE PAN node hostname/IP
  CISCO_ISE_USERNAME   — ERS admin username
  CISCO_ISE_PASSWORD   — ERS admin password
  CISCO_ISE_VERIFY_SSL — "false" to skip cert check (default: true)

ISE ERS API setup:
  Administration → System → Settings → ERS Settings → Enable ERS for Read/Write
  Create an admin user with ERS Admin role.
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)

_ERS_BASE = "ers/config"
_MNT_BASE = "admin/API/mnt"


class CiscoISEClient:
    def __init__(self, **cfg) -> None:
        host = (cfg.get('host') or os.environ["CISCO_ISE_HOST"]).rstrip("/")
        if not host.startswith("http"):
            host = f"https://{host}:9060"
        self._base = host
        self._verify = (cfg.get('verify_ssl') or os.environ.get("CISCO_ISE_VERIFY_SSL", "true")).lower() != "false"
        self._session = requests.Session()
        self._session.auth = (
            cfg.get('username') or os.environ["CISCO_ISE_USERNAME"],
            cfg.get('password') or os.environ["CISCO_ISE_PASSWORD"],
        )
        self._session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })
        if not self._verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _get(self, base: str, path: str, params: dict | None = None) -> dict:
        resp = self._session.get(
            f"{self._base}/{base}/{path.lstrip('/')}",
            params=params or {},
            verify=self._verify,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_all_ers(self, resource: str, page_size: int = 100) -> list[dict]:
        """Paginate through ERS list endpoint."""
        items: list[dict] = []
        page = 1
        while True:
            data = self._get(_ERS_BASE, resource, {"size": page_size, "page": page})
            resources = data.get("SearchResult", {})
            page_items = resources.get("resources", [])
            items.extend(page_items)
            total = resources.get("total", 0)
            if len(items) >= total or not page_items:
                break
            page += 1
        return items

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_network_devices(self) -> list[dict]:
        """Return all network access devices (switches, WLCs) registered in ISE."""
        logger.info("Fetching ISE network devices...")
        try:
            items = self._get_all_ers("networkdevice")
            logger.info("Fetched %d network devices", len(items))
            return items
        except Exception as e:
            logger.error("Failed to fetch network devices: %s", e)
            return []

    def get_endpoints(self) -> list[dict]:
        """Return registered endpoints (MAC + identity data)."""
        logger.info("Fetching ISE endpoints...")
        try:
            items = self._get_all_ers("endpoint")
            logger.info("Fetched %d endpoints", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch endpoints: %s", e)
            return []

    def get_identity_groups(self) -> list[dict]:
        """Return identity groups (user classification)."""
        logger.info("Fetching identity groups...")
        try:
            items = self._get_all_ers("identitygroup")
            logger.info("Fetched %d identity groups", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch identity groups: %s", e)
            return []

    def get_authorization_profiles(self) -> list[dict]:
        """Return RADIUS authorisation profiles (access control policies)."""
        logger.info("Fetching authorisation profiles...")
        try:
            items = self._get_all_ers("authorizationprofile")
            logger.info("Fetched %d authorisation profiles", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch authorisation profiles: %s", e)
            return []

    def get_active_sessions(self) -> list[dict]:
        """Return active RADIUS sessions (MNT API)."""
        logger.info("Fetching active RADIUS sessions...")
        try:
            data = self._get(_MNT_BASE, "Session/ActiveCount")
            count = data.get("count", 0)
            logger.info("Active sessions: %s", count)
            # Return summary only — full session list is very large
            return [{"active_sessions": count}]
        except Exception as e:
            logger.warning("Could not fetch active sessions: %s", e)
            return []

    def get_posture_report(self) -> list[dict]:
        """Return posture compliance summary (NAC endpoint health)."""
        logger.info("Fetching posture report...")
        try:
            data = self._get(_MNT_BASE, "Session/PostureCount")
            return [data]
        except Exception as e:
            logger.warning("Could not fetch posture report: %s", e)
            return []
