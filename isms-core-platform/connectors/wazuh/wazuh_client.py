"""Wazuh Manager REST API client.

Authentication: POST /security/user/authenticate with Basic auth (username:password).
Returns a JWT token used as Bearer in subsequent requests.

Default Wazuh Manager API port: 55000 (HTTPS).

Environment variables:
  WAZUH_URL      — Base URL, e.g. https://wazuh-manager.corp.local:55000
  WAZUH_USERNAME — API username (default: wazuh-wui or custom)
  WAZUH_PASSWORD — API password

Wazuh alert severity levels:
  1-6   = Low (informational)
  7-11  = Medium
  12-14 = High
  15    = Critical

Minimum Wazuh permissions for the service account:
  - agents:read
  - alerts:read
  - vulnerability_detector:read
  - manager:read
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class WazuhClient:
    """Thin REST wrapper for the Wazuh Manager API."""

    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ.get("WAZUH_URL", "")).rstrip("/")
        if not self._base_url:
            raise ValueError("Wazuh URL not set — provide WAZUH_URL or url config key")
        self._username = cfg.get('username') or os.environ.get("WAZUH_USERNAME", "")
        self._password = cfg.get('password') or os.environ.get("WAZUH_PASSWORD", "")
        if not self._username or not self._password:
            raise ValueError("Provide WAZUH_USERNAME and WAZUH_PASSWORD (or username/password config keys)")

        verify_raw = cfg.get('verify_ssl') or os.environ.get("WAZUH_VERIFY_SSL", "true")
        self._verify_ssl = str(verify_raw).lower() != "false"

        self._jwt: str = ""
        self._session = requests.Session()
        self._session.verify = self._verify_ssl

        if not self._verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.authenticate()

    # ── Auth ──────────────────────────────────────────────────────────────────

    def authenticate(self) -> None:
        """Obtain a JWT token via Basic auth."""
        logger.info("Authenticating to Wazuh API as '%s'...", self._username)
        try:
            resp = self._session.post(
                f"{self._base_url}/security/user/authenticate",
                auth=(self._username, self._password),
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
            self._jwt = data.get("data", {}).get("token", "")
            if not self._jwt:
                raise RuntimeError("Wazuh authentication returned no JWT token")
            self._session.headers.update({
                "Authorization": f"Bearer {self._jwt}",
                "Content-Type": "application/json",
            })
            logger.info("Wazuh authentication successful")
        except requests.HTTPError as e:
            logger.error("Wazuh auth HTTP %s: %s", e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("Wazuh authentication failed: %s", e)
            raise

    def _get(self, path: str, params: dict | None = None) -> dict:
        """Issue an authenticated GET and return the parsed JSON body."""
        try:
            resp = self._session.get(
                f"{self._base_url}/{path.lstrip('/')}",
                params=params or {},
                timeout=30,
            )
            if resp.status_code == 401:
                # Token may have expired — re-authenticate once
                logger.warning("Wazuh 401 — re-authenticating...")
                self.authenticate()
                resp = self._session.get(
                    f"{self._base_url}/{path.lstrip('/')}",
                    params=params or {},
                    timeout=30,
                )
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            logger.error("Wazuh GET %s HTTP %s: %s", path, e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("Wazuh GET %s failed: %s", path, e)
            raise

    # ── Public query methods ──────────────────────────────────────────────────

    def get_agents(self) -> list[dict]:
        """Return agents with status (active, disconnected, pending)."""
        logger.info("Fetching agents from Wazuh...")
        data = self._get("agents", {
            "limit": 500,
            "status": "active,disconnected,pending",
            "select": "id,name,ip,status,os,version,lastKeepAlive",
        })
        agents = (data.get("data") or {}).get("affected_items", [])
        logger.info("Fetched %d agents", len(agents))
        return agents

    def get_alerts_summary(self) -> dict:
        """Return agent overview with alert count summary."""
        logger.info("Fetching alert summary from Wazuh...")
        data = self._get("overview/agents")
        return data.get("data", {})

    def get_vulnerability_summary(self, limit: int = 500) -> list[dict]:
        """Return agents with their vulnerability counts.

        The per-agent endpoint GET /vulnerability/{agent_id} was removed in Wazuh 4.8.
        Replacement: GET /vulnerability/agents returns all agents that have vulnerabilities,
        with their severity breakdown.

        Returns list of dicts like:
          {"agentId": "001", "Critical": 2, "High": 5, "Medium": 10, "Low": 3}
        """
        logger.info("Fetching Wazuh vulnerability summary across all agents...")
        try:
            data = self._get("vulnerability/agents", {"limit": limit})
            return (data.get("data") or {}).get("affected_items", [])
        except Exception as e:
            logger.warning("Could not fetch vulnerability summary: %s", e)
            return []

    def get_agent_os_summary(self) -> dict:
        """Return OS distribution across agents."""
        logger.info("Fetching agent OS summary from Wazuh...")
        try:
            data = self._get("agents/summary/os")
            return data.get("data", {})
        except Exception as e:
            logger.warning("Could not fetch agent OS summary: %s", e)
            return {}

    def get_manager_status(self) -> dict:
        """Return Wazuh manager status (best-effort)."""
        logger.info("Fetching Wazuh manager status...")
        try:
            data = self._get("manager/status")
            return data.get("data", {})
        except Exception as e:
            logger.warning("Could not fetch manager status: %s", e)
            return {}
