"""Microsoft Intune (Graph API) client.

Uses the Microsoft Graph API /deviceManagement endpoints.
Authentication: OAuth2 client_credentials (same App Registration as Entra ID).

Environment variables:
  INTUNE_TENANT_ID     — Azure AD tenant ID
  INTUNE_CLIENT_ID     — App registration client ID
  INTUNE_CLIENT_SECRET — App registration client secret

App Registration permissions required (Application):
  DeviceManagementManagedDevices.Read.All   — device inventory + compliance state
  DeviceManagementConfiguration.Read.All    — configuration profiles
  DeviceManagementApps.Read.All             — app inventory (optional)
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

_TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
_SCOPE = "https://graph.microsoft.com/.default"
_BASE_URL = "https://graph.microsoft.com/v1.0"


class IntuneClient:
    def __init__(self, **cfg) -> None:
        self._tenant_id = cfg.get('tenant_id') or os.environ["INTUNE_TENANT_ID"]
        self._client_id = cfg.get('client_id') or os.environ["INTUNE_CLIENT_ID"]
        self._client_secret = cfg.get('client_secret') or os.environ["INTUNE_CLIENT_SECRET"]
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
        logger.info("Intune token refreshed (expires in %ds)", data.get("expires_in", 3600))

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Paginated GET via @odata.nextLink."""
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
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("value", []))
            url = data.get("@odata.nextLink", "")
            p = {}
        return results

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_managed_devices(self) -> list[dict]:
        """Return all Intune-enrolled devices."""
        logger.info("Fetching managed devices from Intune...")
        items = self._get_all("deviceManagement/managedDevices", {
            "$select": (
                "id,deviceName,operatingSystem,osVersion,managedDeviceOwnerType,"
                "complianceState,enrolledDateTime,lastSyncDateTime,managementAgent,"
                "manufacturer,model,userPrincipalName,azureADRegistered,"
                "deviceEnrollmentType"
            )
        })
        logger.info("Fetched %d managed devices", len(items))
        return items

    def get_device_configurations(self) -> list[dict]:
        """Return all device configuration profiles."""
        logger.info("Fetching device configurations from Intune...")
        try:
            items = self._get_all("deviceManagement/deviceConfigurations", {
                "$select": "id,displayName,description,createdDateTime,lastModifiedDateTime,version"
            })
            logger.info("Fetched %d device configurations", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch device configurations: %s", e)
            return []

    def get_compliance_policies(self) -> list[dict]:
        """Return all device compliance policies."""
        logger.info("Fetching compliance policies from Intune...")
        try:
            items = self._get_all("deviceManagement/deviceCompliancePolicies", {
                "$select": "id,displayName,description,createdDateTime,lastModifiedDateTime,version"
            })
            logger.info("Fetched %d compliance policies", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch compliance policies: %s", e)
            return []

    def get_device_compliance_overview(self) -> dict:
        """Return device compliance state summary."""
        try:
            self._ensure_token()
            resp = requests.get(
                f"{_BASE_URL}/deviceManagement/deviceCompliancePolicyDeviceStateSummary",
                headers={"Authorization": f"Bearer {self._token}"},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.warning("Could not fetch compliance overview: %s", e)
            return {}
