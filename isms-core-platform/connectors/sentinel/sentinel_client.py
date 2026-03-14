"""Microsoft Sentinel REST API client.

Uses the Azure Resource Manager API for Sentinel (Microsoft Security Insights).
Authentication: OAuth2 client_credentials against management.azure.com.

Environment variables:
  SENTINEL_TENANT_ID         — Azure AD tenant ID
  SENTINEL_CLIENT_ID         — App registration client ID
  SENTINEL_CLIENT_SECRET     — App registration client secret
  SENTINEL_SUBSCRIPTION_ID   — Azure subscription ID
  SENTINEL_RESOURCE_GROUP    — Resource group name containing the Sentinel workspace
  SENTINEL_WORKSPACE_NAME    — Log Analytics workspace name

App Registration permissions required:
  Microsoft Sentinel Reader (role assignment on the workspace resource group)
  — OR —
  Microsoft.SecurityInsights/incidents/read
  Microsoft.SecurityInsights/alertRules/read
  Microsoft.OperationalInsights/workspaces/read

API base:
  https://management.azure.com/subscriptions/{sub}/resourceGroups/{rg}/
  providers/Microsoft.OperationalInsights/workspaces/{workspace}/
  providers/Microsoft.SecurityInsights/
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

_TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
_SCOPE = "https://management.azure.com/.default"
_API_VERSION = "2023-02-01"


class SentinelClient:
    def __init__(self, **cfg) -> None:
        self._tenant_id = cfg.get('tenant_id') or os.environ["SENTINEL_TENANT_ID"]
        self._client_id = cfg.get('client_id') or os.environ["SENTINEL_CLIENT_ID"]
        self._client_secret = cfg.get('client_secret') or os.environ["SENTINEL_CLIENT_SECRET"]

        sub = cfg.get('subscription_id') or os.environ["SENTINEL_SUBSCRIPTION_ID"]
        rg = cfg.get('resource_group') or os.environ["SENTINEL_RESOURCE_GROUP"]
        ws = cfg.get('workspace_name') or os.environ["SENTINEL_WORKSPACE_NAME"]

        self._base = (
            f"https://management.azure.com/subscriptions/{sub}"
            f"/resourceGroups/{rg}"
            f"/providers/Microsoft.OperationalInsights/workspaces/{ws}"
            f"/providers/Microsoft.SecurityInsights"
        )

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
        logger.info("Sentinel token refreshed (expires in %ds)", data.get("expires_in", 3600))

    def _get_all(self, resource: str, params: dict | None = None) -> list[dict]:
        """Paginated GET through Azure ARM nextLink pagination."""
        results: list[dict] = []
        url = f"{self._base}/{resource}"
        p = {"api-version": _API_VERSION, **(params or {})}
        while url:
            self._ensure_token()
            resp = requests.get(
                url,
                headers={"Authorization": f"Bearer {self._token}"},
                params=p,
                timeout=60,
            )
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("value", []))
            url = data.get("nextLink", "")
            p = {}  # nextLink already contains all params
        return results

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_incidents(self, top: int = 500) -> list[dict]:
        """Return recent incidents (newest first)."""
        logger.info("Fetching Sentinel incidents...")
        try:
            items = self._get_all("incidents", {
                "$top": top,
                "$orderby": "properties/createdTimeUtc desc",
            })
            logger.info("Fetched %d incidents", len(items))
            return items
        except Exception as e:
            logger.error("Failed to fetch incidents: %s", e)
            return []

    def get_alert_rules(self) -> list[dict]:
        """Return all analytics rules (scheduled + other)."""
        logger.info("Fetching Sentinel alert rules...")
        try:
            items = self._get_all("alertRules")
            logger.info("Fetched %d alert rules", len(items))
            return items
        except Exception as e:
            logger.warning("Failed to fetch alert rules: %s", e)
            return []

    def get_data_connectors(self) -> list[dict]:
        """Return configured data connectors (coverage evidence)."""
        logger.info("Fetching Sentinel data connectors...")
        try:
            items = self._get_all("dataConnectors")
            logger.info("Fetched %d data connectors", len(items))
            return items
        except Exception as e:
            logger.warning("Failed to fetch data connectors: %s", e)
            return []
