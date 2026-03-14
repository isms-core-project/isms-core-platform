"""Microsoft Graph API client for the M365 Security connector.

Handles:
  - OAuth2 client_credentials token acquisition + auto-refresh
  - Paginated GET requests ($top / @odata.nextLink)
  - Endpoints used:
      /v1.0/security/secureScores                          → A.8.5
      /v1.0/security/alerts_v2                             → A.8.1-7-18-19 / A.8.7
      /v1.0/security/secureScoreControlProfiles            → A.8.5
      /v1.0/identity/conditionalAccess/policies            → A.5.15-16-18

Required Graph API permissions (Application, not Delegated):
  SecurityAlert.Read.All
  SecurityEvents.Read.All
  ThreatIndicators.Read.All      (optional — for additional alert sources)
  Policy.Read.All                (optional — for conditional access; 403 handled gracefully)
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
SCOPE = "https://graph.microsoft.com/.default"


class M365Client:
    def __init__(self, **cfg) -> None:
        # Accept M365_* env vars with fallback to ENTRA_* for shared service principals
        self.tenant_id = (
            cfg.get("tenant_id")
            or os.environ.get("M365_TENANT_ID")
            or os.environ["ENTRA_TENANT_ID"]
        )
        self.client_id = (
            cfg.get("client_id")
            or os.environ.get("M365_CLIENT_ID")
            or os.environ["ENTRA_CLIENT_ID"]
        )
        self.client_secret = (
            cfg.get("client_secret")
            or os.environ.get("M365_CLIENT_SECRET")
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
                "scope": SCOPE,
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expiry = time.time() + data.get("expires_in", 3600)
        logger.info("M365 Graph token acquired (expires in %ds)", data.get("expires_in", 3600))
        return self._token

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self._get_token()}", "Accept": "application/json"}

    # ── Paginated GET ─────────────────────────────────────────────────────────

    def _get_all(self, url: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of a Graph API collection via @odata.nextLink."""
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

    def get_secure_score(self) -> dict | None:
        """Most recent Secure Score for the tenant.

        GET /v1.0/security/secureScores?$top=1&$orderby=createdDateTime desc
        Returns: {id, azureTenantId, createdDateTime, currentScore, maxScore,
                  percentageScore, controlScores: [...]}
        """
        logger.info("Fetching Secure Score…")
        try:
            resp = requests.get(
                f"{GRAPH_BASE}/security/secureScores",
                headers=self._headers(),
                params={"$top": 1, "$orderby": "createdDateTime desc"},
                timeout=30,
            )
            resp.raise_for_status()
            scores = resp.json().get("value", [])
            if scores:
                logger.info(
                    "Secure Score fetched: %.1f / %.1f (%.1f%%)",
                    scores[0].get("currentScore", 0),
                    scores[0].get("maxScore", 0),
                    scores[0].get("percentageScore", 0),
                )
                return scores[0]
            logger.warning("Secure Score API returned empty value list")
            return None
        except requests.HTTPError as e:
            logger.error("Secure Score fetch failed: %s", e)
            return None

    def get_alerts(self, top: int = 200) -> list[dict]:
        """Security alerts from the unified alerts_v2 endpoint.

        GET /v1.0/security/alerts_v2?$top=N&$orderby=createdDateTime desc
        Returns: [{id, title, severity, status, category, serviceSource, createdDateTime, ...}]
        """
        logger.info("Fetching security alerts (top=%d)…", top)
        try:
            alerts = self._get_all(
                f"{GRAPH_BASE}/security/alerts_v2",
                params={"$top": top, "$orderby": "createdDateTime desc"},
            )
            logger.info("Fetched %d security alerts", len(alerts))
            return alerts
        except requests.HTTPError as e:
            logger.error("Alert fetch failed: %s", e)
            return []

    def get_secure_score_controls(self) -> list[dict]:
        """Secure Score control profiles (definition + current score per control).

        GET /v1.0/security/secureScoreControlProfiles?$top=999
        Returns: [{id, controlName, controlCategory, maxScore, rank, ...}]
        """
        logger.info("Fetching Secure Score control profiles…")
        try:
            controls = self._get_all(
                f"{GRAPH_BASE}/security/secureScoreControlProfiles",
                params={"$top": 999},
            )
            logger.info("Fetched %d Secure Score control profiles", len(controls))
            return controls
        except requests.HTTPError as e:
            logger.error("Secure Score controls fetch failed: %s", e)
            return []

    def get_conditional_access_policies(self) -> list[dict]:
        """Conditional Access policies for the tenant.

        GET /v1.0/identity/conditionalAccess/policies
        Returns: [{id, displayName, state, createdDateTime, ...}]
        Returns [] gracefully if Policy.Read.All is not granted (403).
        """
        logger.info("Fetching Conditional Access policies…")
        try:
            policies = self._get_all(f"{GRAPH_BASE}/identity/conditionalAccess/policies")
            logger.info("Fetched %d Conditional Access policies", len(policies))
            return policies
        except requests.HTTPError as e:
            if e.response.status_code == 403:
                logger.warning(
                    "Conditional Access policies returned 403 — "
                    "Policy.Read.All permission not granted; skipping"
                )
                return []
            logger.error("Conditional Access policies fetch failed: %s", e)
            return []
        except Exception as e:
            logger.error("Conditional Access policies fetch error: %s", e)
            return []
