"""Microsoft Graph API client for the Entra ID connector.

Handles:
  - OAuth2 client_credentials token acquisition + auto-refresh
  - Paginated GET requests ($top / @odata.nextLink)
  - Endpoints used:
      /v1.0/users                                              → A.5.3 / A.5.15 / A.5.18
      /v1.0/groups                                             → A.5.15
      /v1.0/reports/authenticationMethods/userRegistrationDetails  → A.8.5
      /v1.0/roleManagement/directory/roleAssignments           → A.5.18

Required Graph API permissions (Application, not Delegated):
  User.Read.All
  GroupMember.Read.All
  RoleManagement.Read.Directory
  UserAuthenticationMethod.Read.All           (MFA details)
  DeviceManagementManagedDevices.Read.All     (Intune — optional)
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
SCOPE = "https://graph.microsoft.com/.default"

# Fields to select per entity (keeps payload small)
USER_SELECT = "id,displayName,userPrincipalName,accountEnabled,department,jobTitle,mail,createdDateTime,assignedLicenses"
GROUP_SELECT = "id,displayName,description,groupTypes,securityEnabled,mailEnabled"


class GraphClient:
    def __init__(self, **cfg) -> None:
        self.tenant_id = cfg.get('tenant_id') or os.environ["ENTRA_TENANT_ID"]
        self.client_id = cfg.get('client_id') or os.environ["ENTRA_CLIENT_ID"]
        self.client_secret = cfg.get('client_secret') or os.environ["ENTRA_CLIENT_SECRET"]
        self._token: str | None = None
        self._token_expiry: float = 0

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _get_token(self) -> str:
        if self._token and time.time() < self._token_expiry - 60:
            return self._token
        resp = requests.post(
            TOKEN_URL.format(tenant_id=self.tenant_id),
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": SCOPE,
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + data.get("expires_in", 3600)
        logger.info("Graph token acquired (expires in %ds)", data.get("expires_in", 3600))
        return self._token

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self._get_token()}", "Accept": "application/json"}

    # ── Paginated GET ─────────────────────────────────────────────────────────

    def _get_all(self, url: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of a Graph API collection."""
        items = []
        next_url: str | None = url
        req_params = params or {}

        while next_url:
            resp = requests.get(next_url, headers=self._headers(), params=req_params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            items.extend(data.get("value", []))
            next_url = data.get("@odata.nextLink")
            req_params = {}  # nextLink already contains all params

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """All users in the tenant."""
        logger.info("Fetching users…")
        users = self._get_all(
            f"{GRAPH_BASE}/users",
            params={"$select": USER_SELECT, "$top": 999},
        )
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """All groups (security + M365)."""
        logger.info("Fetching groups…")
        groups = self._get_all(
            f"{GRAPH_BASE}/groups",
            params={"$select": GROUP_SELECT, "$top": 999},
        )
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_mfa_registration(self) -> list[dict]:
        """MFA registration status per user (requires UserAuthenticationMethod.Read.All)."""
        logger.info("Fetching MFA registration details…")
        try:
            records = self._get_all(
                f"{GRAPH_BASE}/reports/authenticationMethods/userRegistrationDetails",
                params={"$top": 999},
            )
            logger.info("Fetched MFA details for %d users", len(records))
            return records
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "MFA registration endpoint returned %d — "
                    "ensure UserAuthenticationMethod.Read.All is granted",
                    e.response.status_code,
                )
                return []
            raise

    def get_role_definitions(self) -> dict[str, str]:
        """Return {roleDefinitionId: displayName} for all directory role definitions."""
        logger.info("Fetching role definitions…")
        try:
            defs = self._get_all(
                f"{GRAPH_BASE}/roleManagement/directory/roleDefinitions",
                params={"$select": "id,displayName", "$top": 200},
            )
            return {d["id"]: d["displayName"] for d in defs if "id" in d}
        except Exception as e:
            logger.warning("Could not fetch role definitions: %s", e)
            return {}

    def get_privileged_role_assignments(self) -> list[dict]:
        """Directory role assignments with resolved display names."""
        logger.info("Fetching privileged role assignments…")
        try:
            role_names = self.get_role_definitions()
            assignments = self._get_all(
                f"{GRAPH_BASE}/roleManagement/directory/roleAssignments",
                params={"$expand": "principal", "$top": 999},
            )
            # Inject display name so connector.py transform finds it in roleDefinition.displayName
            for a in assignments:
                role_id = a.get("roleDefinitionId", "")
                a["roleDefinition"] = {"displayName": role_names.get(role_id, role_id)}
            logger.info("Fetched %d role assignments", len(assignments))
            return assignments
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Role assignments endpoint returned %d — "
                    "ensure RoleManagement.Read.Directory is granted",
                    e.response.status_code,
                )
                return []
            raise
