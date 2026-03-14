"""Microsoft Defender for Endpoint API client.

Uses the Defender for Endpoint REST API (securitycenter.microsoft.com).
Authentication: OAuth2 client_credentials flow (same App Registration as Entra ID).

Environment variables:
  DEFENDER_TENANT_ID     — Azure AD tenant ID
  DEFENDER_CLIENT_ID     — App registration client ID
  DEFENDER_CLIENT_SECRET — App registration client secret

App Registration permissions required (Application):
  Machine.Read.All          — device inventory + health status
  Vulnerability.Read.All    — CVE data per device
  Alert.Read.All            — security alerts
  Software.Read.All         — software inventory (optional)

API base: https://api.securitycenter.microsoft.com/api/
"""

import logging
import os
import time
from datetime import datetime, timezone

import requests

logger = logging.getLogger(__name__)

_TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
_SCOPE = "https://api.securitycenter.microsoft.com/.default"
_BASE_URL = "https://api.securitycenter.microsoft.com/api"

# Severity → numeric weight for sorting
SEVERITY_WEIGHT = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1, "Informational": 0}


class DefenderClient:
    def __init__(self, **cfg) -> None:
        self._tenant_id = cfg.get('tenant_id') or os.environ["DEFENDER_TENANT_ID"]
        self._client_id = cfg.get('client_id') or os.environ["DEFENDER_CLIENT_ID"]
        self._client_secret = cfg.get('client_secret') or os.environ["DEFENDER_CLIENT_SECRET"]
        self._token: str | None = None
        self._token_expires_at: float = 0.0

    def _ensure_token(self) -> None:
        if self._token and time.time() < self._token_expires_at - 60:
            return
        resp = requests.post(
            _TOKEN_URL.format(tenant_id=self._tenant_id),
            data={
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "scope": _SCOPE,
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expires_at = time.time() + data.get("expires_in", 3600)
        logger.info("Defender token refreshed (expires in %ds)", data.get("expires_in", 3600))

    def _get(self, path: str, params: dict | None = None) -> dict:
        self._ensure_token()
        resp = requests.get(
            f"{_BASE_URL}/{path.lstrip('/')}",
            headers={"Authorization": f"Bearer {self._token}"},
            params=params or {},
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Paginated GET — follows OData @odata.nextLink."""
        results: list[dict] = []
        url = f"{_BASE_URL}/{path.lstrip('/')}"
        p = params or {}
        while url:
            self._ensure_token()
            resp = requests.get(
                url,
                headers={"Authorization": f"Bearer {self._token}"},
                params=p,
                timeout=60,
            )
            if not resp.ok:
                logger.error("Defender API error %s: %s", resp.status_code, resp.text[:500])
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("value", []))
            url = data.get("@odata.nextLink", "")
            p = {}  # params are embedded in nextLink
        return results

    # ── Public query methods ──────────────────────────────────────────────────

    def get_machines(self) -> list[dict]:
        """Return all enrolled endpoints with health and OS info."""
        logger.info("Fetching machines from Defender...")
        items = self._get_all("machines")
        logger.info("Fetched %d machines", len(items))
        return items

    def get_vulnerabilities_summary(self) -> dict:
        """Return CVE counts by severity (aggregate query)."""
        logger.info("Fetching vulnerability summary from Defender...")
        try:
            data = self._get("vulnerabilities/machinesVulnerabilities/summarize")
            return data
        except Exception as e:
            logger.warning("Could not fetch vulnerability summary: %s", e)
            return {}

    def get_alerts(self, limit: int = 500) -> list[dict]:
        """Return recent security alerts (last 500, newest first)."""
        logger.info("Fetching alerts from Defender...")
        try:
            items = self._get_all("alerts", {
                "$top": limit,
                "$orderby": "alertCreationTime desc",
                "$select": (
                    "id,title,severity,status,category,alertCreationTime,"
                    "machineId,computerDnsName,description,classification"
                ),
            })
            logger.info("Fetched %d alerts", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch alerts: %s", e)
            return []

    def get_recommendations(self) -> list[dict]:
        """Return security recommendations (top remediation actions)."""
        logger.info("Fetching security recommendations from Defender...")
        try:
            items = self._get_all("recommendations", {"$top": 200})
            logger.info("Fetched %d recommendations", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch recommendations: %s", e)
            return []

    def get_software_vulnerabilities_per_machine(self, machine_ids: list[str]) -> dict[str, list]:
        """Return CVEs per machine for the given machine IDs (top 50 most-exposed)."""
        result: dict[str, list] = {}
        # Limit to 50 to avoid excessive API calls
        for mid in machine_ids[:50]:
            try:
                data = self._get(f"machines/{mid}/vulnerabilities", {"$top": 50})
                result[mid] = data.get("value", [])
            except Exception as e:
                logger.warning("Could not fetch vulns for machine %s: %s", mid, e)
        return result
