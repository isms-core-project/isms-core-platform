"""NetBox REST API client.

Authentication: Token auth — Authorization: Token <api_token>

Environment variables:
  NETBOX_URL       — Base URL, e.g. http://netbox.corp.local
  NETBOX_API_TOKEN — NetBox API token for the service account

Minimum NetBox permissions for the service account:
  - Read access to DCIM (devices, interfaces, sites, racks)
  - Read access to IPAM (IP addresses, prefixes, VRFs)
  - No write access required
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)


class NetBoxClient:
    """Thin REST wrapper for the NetBox REST API."""

    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ.get("NETBOX_URL", "")).rstrip("/") + "/api"
        if not self._base_url or self._base_url == "/api":
            raise ValueError("NetBox URL not set — provide NETBOX_URL or url config key")
        api_token = cfg.get('api_token') or os.environ.get("NETBOX_API_TOKEN", "")
        if not api_token:
            raise ValueError("NetBox API token not set — provide NETBOX_API_TOKEN or api_token config key")
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Token {api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _get(self, path: str, params: dict | None = None) -> dict:
        """Issue an authenticated GET and return the parsed JSON body."""
        try:
            resp = self._session.get(
                f"{self._base_url}/{path.lstrip('/')}",
                params=params or {},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            logger.error("NetBox GET %s HTTP %s: %s", path, e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("NetBox GET %s failed: %s", path, e)
            raise

    def _get_list(self, path: str, params: dict | None = None) -> list[dict]:
        """GET a paginated NetBox endpoint and return the results list."""
        data = self._get(path, params)
        return data.get("results", []) if isinstance(data, dict) else []

    # ── Public query methods ──────────────────────────────────────────────────

    def get_devices(self, limit: int = 1000) -> list[dict]:
        """Return devices with name, device_type, site, status, last_updated."""
        logger.info("Fetching devices from NetBox (limit=%d)...", limit)
        devices = self._get_list("dcim/devices/", {"limit": limit})
        logger.info("Fetched %d devices", len(devices))
        return devices

    def get_ip_addresses(self, limit: int = 1000) -> list[dict]:
        """Return IP allocations with address, status, and VRF."""
        logger.info("Fetching IP addresses from NetBox (limit=%d)...", limit)
        addresses = self._get_list("ipam/ip-addresses/", {"limit": limit})
        logger.info("Fetched %d IP addresses", len(addresses))
        return addresses

    def get_prefixes(self) -> list[dict]:
        """Return network prefix allocations."""
        logger.info("Fetching prefixes from NetBox...")
        prefixes = self._get_list("ipam/prefixes/")
        logger.info("Fetched %d prefixes", len(prefixes))
        return prefixes

    def get_interfaces(self, limit: int = 500) -> list[dict]:
        """Return device interfaces for network connectivity evidence."""
        logger.info("Fetching interfaces from NetBox (limit=%d)...", limit)
        interfaces = self._get_list("dcim/interfaces/", {"limit": limit})
        logger.info("Fetched %d interfaces", len(interfaces))
        return interfaces
