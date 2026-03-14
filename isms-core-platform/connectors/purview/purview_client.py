"""Microsoft Purview client for ISMS CORE v2.0.

Uses two API surfaces:
  1. Microsoft Graph — sensitivity labels, retention labels, DLP/IP security alerts
  2. Purview Data Plane (optional) — data catalogue collections, classification summary

Authentication: OAuth2 client_credentials (same App Registration as Entra/Defender/Sentinel).
Requires these Graph API application permissions:
  InformationProtectionPolicy.Read.All  — sensitivity label inventory
  RecordsManagement.Read.All            — retention label inventory
  SecurityEvents.Read.All               — Purview DLP / IP security alerts
  SecurityIncident.Read.All             — DLP incidents (beta)

Purview Data Plane scope (if PURVIEW_ACCOUNT is set):
  https://purview.azure.com/.default    — data map, collections, classification rules

ISO control mappings:
  a.8.10 — Information deletion         (retention labels + lifecycle policies)
  a.8.12 — Data leakage prevention      (DLP policies, sensitivity labels, alerts)
"""

import logging
import os
import time

import requests

logger = logging.getLogger(__name__)

GRAPH_BASE = "https://graph.microsoft.com"
TOKEN_URL = "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
PURVIEW_BASE = "https://{account}.purview.azure.com"


class PurviewClient:
    def __init__(self, **cfg) -> None:
        self.tenant_id     = cfg.get('tenant_id')     or os.environ["PURVIEW_TENANT_ID"]
        self.client_id     = cfg.get('client_id')     or os.environ["PURVIEW_CLIENT_ID"]
        self.client_secret = cfg.get('client_secret') or os.environ["PURVIEW_CLIENT_SECRET"]
        # Optional — enables Purview Data Plane (data catalogue) evidence
        self.purview_account = cfg.get('purview_account') or os.environ.get("PURVIEW_ACCOUNT", "")

        self._graph_token: str | None = None
        self._graph_expiry: float = 0
        self._purview_token: str | None = None
        self._purview_expiry: float = 0

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _get_token(self, scope: str, cache_attr: str, expiry_attr: str) -> str:
        token = getattr(self, cache_attr)
        expiry = getattr(self, expiry_attr)
        if token and time.time() < expiry - 60:
            return token

        resp = requests.post(
            TOKEN_URL.format(tenant_id=self.tenant_id),
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": scope,
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        setattr(self, cache_attr, data["access_token"])
        setattr(self, expiry_attr, time.time() + int(data.get("expires_in", 3600)))
        return data["access_token"]

    def _graph_token_str(self) -> str:
        return self._get_token(
            f"{GRAPH_BASE}/.default",
            "_graph_token", "_graph_expiry",
        )

    def _purview_token_str(self) -> str:
        return self._get_token(
            "https://purview.azure.com/.default",
            "_purview_token", "_purview_expiry",
        )

    def _graph_get(self, path: str, api: str = "v1.0", beta: bool = False) -> dict:
        version = "beta" if beta else api
        resp = requests.get(
            f"{GRAPH_BASE}/{version}{path}",
            headers={"Authorization": f"Bearer {self._graph_token_str()}"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    def _graph_pages(self, path: str, beta: bool = False) -> list[dict]:
        """Paginate through @odata.nextLink responses."""
        results = []
        version = "beta" if beta else "v1.0"
        url = f"{GRAPH_BASE}/{version}{path}"
        while url:
            resp = requests.get(
                url,
                headers={"Authorization": f"Bearer {self._graph_token_str()}"},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            results.extend(data.get("value", []))
            url = data.get("@odata.nextLink")
        return results

    def _purview_get(self, path: str) -> dict:
        if not self.purview_account:
            raise ValueError("PURVIEW_ACCOUNT not set — cannot call Purview Data Plane")
        base = PURVIEW_BASE.format(account=self.purview_account)
        resp = requests.get(
            f"{base}{path}",
            headers={"Authorization": f"Bearer {self._purview_token_str()}"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    # ── Graph — sensitivity labels ─────────────────────────────────────────────

    def get_sensitivity_labels(self) -> list[dict]:
        """List sensitivity labels defined in the tenant.
        Requires: InformationProtectionPolicy.Read.All
        """
        try:
            return self._graph_pages("/informationProtection/sensitivityLabels", beta=True)
        except Exception as e:
            logger.warning("sensitivityLabels unavailable: %s", e)
            return []

    # ── Graph — retention labels ──────────────────────────────────────────────

    def get_retention_labels(self) -> list[dict]:
        """List retention labels (records management).
        Requires: RecordsManagement.Read.All
        """
        try:
            return self._graph_pages("/security/labels/retentionLabels", beta=True)
        except Exception as e:
            logger.warning("retentionLabels unavailable: %s", e)
            return []

    # ── Graph — DLP / Information Protection security alerts ──────────────────

    def get_dlp_alerts(self, max_results: int = 200) -> list[dict]:
        """Fetch security alerts from Microsoft Purview (DLP, Information Protection).
        Requires: SecurityEvents.Read.All
        """
        try:
            alerts = self._graph_pages(
                "/security/alerts_v2"
                "?$filter=serviceSource eq 'microsoftPurview' or serviceSource eq 'office365'"
                f"&$top=50&$orderby=createdDateTime desc"
            )
            return alerts[:max_results]
        except Exception as e:
            logger.warning("DLP alerts unavailable: %s", e)
            return []

    # ── Purview Data Plane — collections ──────────────────────────────────────

    def get_collections(self) -> list[dict]:
        """List Purview data map collections (if PURVIEW_ACCOUNT configured)."""
        if not self.purview_account:
            return []
        try:
            data = self._purview_get("/account/collections?api-version=2019-11-01-preview")
            return data.get("value", [])
        except Exception as e:
            logger.warning("Purview collections unavailable: %s", e)
            return []

    def get_classification_rules(self) -> list[dict]:
        """List custom classification rules from the data map."""
        if not self.purview_account:
            return []
        try:
            data = self._purview_get(
                "/catalog/api/atlas/v2/types/typedefs"
                "?includeTermTemplate=false&type=classification"
            )
            return data.get("classificationDefs", [])
        except Exception as e:
            logger.warning("Classification rules unavailable: %s", e)
            return []
