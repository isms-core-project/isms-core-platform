"""Azure Resource Manager client for the Azure CSPM connector (Defender for Cloud).

Handles:
  - OAuth2 client_credentials token acquisition + auto-refresh (ARM scope)
  - ARM nextLink pagination
  - Endpoints used:
      /subscriptions                                                    → subscription discovery
      /subscriptions/{id}/providers/Microsoft.Security/secureScores    → A.8.5
      /subscriptions/{id}/providers/Microsoft.Security/assessments     → A.8.8 / A.8.20-22
      /subscriptions/{id}/providers/Microsoft.Security/alerts          → A.8.8
      /subscriptions/{id}/providers/Microsoft.Security/regulatoryComplianceStandards → A.5.9

Required RBAC (on subscription):
  Security Reader     (minimum — read Defender for Cloud data)
  Reader              (for subscription discovery and resource metadata)
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

ARM_BASE = "https://management.azure.com"
TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
ARM_SCOPE = "https://management.azure.com/.default"


class ARMClient:
    def __init__(self, **cfg) -> None:
        # Accept AZURE_* env vars with fallback to ENTRA_* for shared service principals
        self.tenant_id = (
            cfg.get("tenant_id")
            or os.environ.get("AZURE_TENANT_ID")
            or os.environ["ENTRA_TENANT_ID"]
        )
        self.client_id = (
            cfg.get("client_id")
            or os.environ.get("AZURE_CLIENT_ID")
            or os.environ["ENTRA_CLIENT_ID"]
        )
        self.client_secret = (
            cfg.get("client_secret")
            or os.environ.get("AZURE_CLIENT_SECRET")
            or os.environ["ENTRA_CLIENT_SECRET"]
        )
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
                "scope": ARM_SCOPE,
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + data.get("expires_in", 3600)
        logger.info("ARM token acquired (expires in %ds)", data.get("expires_in", 3600))
        return self._token

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self._get_token()}", "Accept": "application/json"}

    # ── ARM pagination (uses nextLink at top level, not @odata.nextLink) ──────

    def _get_paged(self, url: str, api_version: str) -> list[dict]:
        """Fetch all pages of an ARM collection via nextLink."""
        items = []
        next_url: str | None = url
        req_params: dict = {"api-version": api_version}

        while next_url:
            resp = requests.get(next_url, headers=self._headers(), params=req_params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            items.extend(data.get("value", []))
            # ARM uses 'nextLink' (no @ prefix) at the top level of the response
            next_url = data.get("nextLink")
            req_params = {}  # nextLink already encodes api-version and all other params

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_subscriptions(self) -> list[dict]:
        """All subscriptions accessible to the service principal.

        GET https://management.azure.com/subscriptions?api-version=2020-01-01
        Returns: [{subscriptionId, displayName, state, ...}]
        """
        logger.info("Fetching subscriptions…")
        subs = self._get_paged(f"{ARM_BASE}/subscriptions", api_version="2020-01-01")
        # Filter to enabled subscriptions only
        enabled = [s for s in subs if s.get("state") == "Enabled"]
        logger.info("Fetched %d subscriptions (%d enabled)", len(subs), len(enabled))
        return enabled

    def get_secure_scores(self, subscription_id: str) -> list[dict]:
        """Secure Score initiatives for a subscription.

        GET /subscriptions/{id}/providers/Microsoft.Security/secureScores?api-version=2020-01-01
        Returns: [{id, name, properties: {displayName, score: {current, max, percentage}, weight}}]
        """
        logger.info("Fetching Secure Scores for subscription %s…", subscription_id)
        url = (
            f"{ARM_BASE}/subscriptions/{subscription_id}"
            f"/providers/Microsoft.Security/secureScores"
        )
        try:
            scores = self._get_paged(url, api_version="2020-01-01")
            logger.info("Fetched %d Secure Score(s) for %s", len(scores), subscription_id)
            return scores
        except requests.HTTPError as e:
            logger.error("Secure Scores fetch failed for %s: %s", subscription_id, e)
            return []

    def get_assessments(self, subscription_id: str, top: int = 500) -> list[dict]:
        """Security assessments (recommendations) for a subscription.

        GET /subscriptions/{id}/providers/Microsoft.Security/assessments?api-version=2021-06-01
        Returns: [{id, name, properties: {displayName, status: {code}, resourceDetails: {...}}}]
        Uses nextLink pagination.
        """
        logger.info("Fetching security assessments for subscription %s…", subscription_id)
        url = (
            f"{ARM_BASE}/subscriptions/{subscription_id}"
            f"/providers/Microsoft.Security/assessments"
        )
        try:
            assessments = self._get_paged(url, api_version="2021-06-01")
            logger.info(
                "Fetched %d assessments for %s", len(assessments), subscription_id
            )
            return assessments
        except requests.HTTPError as e:
            logger.error("Assessments fetch failed for %s: %s", subscription_id, e)
            return []

    def get_alerts(self, subscription_id: str, top: int = 200) -> list[dict]:
        """Defender for Cloud security alerts for a subscription.

        GET /subscriptions/{id}/providers/Microsoft.Security/alerts?api-version=2022-01-01
        Returns: [{id, name, properties: {alertDisplayName, severity, status, description, ...}}]
        """
        logger.info("Fetching Defender alerts for subscription %s…", subscription_id)
        url = (
            f"{ARM_BASE}/subscriptions/{subscription_id}"
            f"/providers/Microsoft.Security/alerts"
        )
        try:
            alerts = self._get_paged(url, api_version="2022-01-01")
            logger.info("Fetched %d alerts for %s", len(alerts), subscription_id)
            return alerts
        except requests.HTTPError as e:
            logger.error("Alerts fetch failed for %s: %s", subscription_id, e)
            return []

    def get_regulatory_compliance(self, subscription_id: str) -> list[dict]:
        """Regulatory compliance standards assessment for a subscription.

        GET /subscriptions/{id}/providers/Microsoft.Security/regulatoryComplianceStandards
            ?api-version=2019-01-01
        Returns: [{id, name, properties: {state, passedControls, failedControls,
                   skippedControls, ...}}]
        """
        logger.info("Fetching regulatory compliance for subscription %s…", subscription_id)
        url = (
            f"{ARM_BASE}/subscriptions/{subscription_id}"
            f"/providers/Microsoft.Security/regulatoryComplianceStandards"
        )
        try:
            standards = self._get_paged(url, api_version="2019-01-01")
            logger.info(
                "Fetched %d compliance standard(s) for %s", len(standards), subscription_id
            )
            return standards
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                logger.warning(
                    "Regulatory compliance endpoint returned 404 for %s — "
                    "Defender for Cloud may not be enabled on this subscription",
                    subscription_id,
                )
                return []
            logger.error("Regulatory compliance fetch failed for %s: %s", subscription_id, e)
            return []
