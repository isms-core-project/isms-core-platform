"""GCP Security Command Center (SCC) API client.

Uses the Security Command Center REST API v2 via requests with OAuth2
service account authentication. No google-auth library required —
the service account JWT is constructed manually.

Authentication:
  - Service account JSON key (preferred): set GCP_SERVICE_ACCOUNT_KEY env var
    to the full JSON content of the service account key file.
  - Application Default Credentials fallback: if no key is provided, attempts
    to retrieve a token from the GCE metadata server.

Environment variables:
  GCP_PROJECT_ID           — GCP project ID (used for scoping)
  GCP_ORGANIZATION_ID      — GCP organization ID (numeric, e.g. 123456789012)
  GCP_SERVICE_ACCOUNT_KEY  — Full JSON string of the service account key file

API base: https://securitycenter.googleapis.com/v2
"""

import base64
import json
import logging
import os
import time
from datetime import datetime, timezone

import requests

logger = logging.getLogger(__name__)

_TOKEN_URL = "https://oauth2.googleapis.com/token"
_SCC_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
_SCC_BASE = "https://securitycenter.googleapis.com/v2"
_METADATA_TOKEN_URL = (
    "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
)


def _base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _make_jwt(service_account_info: dict) -> str:
    """Build a signed JWT for the service account OAuth2 flow."""
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
    except ImportError as exc:
        raise ImportError(
            "The 'cryptography' package is required for service account JWT auth. "
            "Add cryptography>=42 to requirements.txt."
        ) from exc

    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT", "kid": service_account_info["private_key_id"]}
    payload = {
        "iss": service_account_info["client_email"],
        "sub": service_account_info["client_email"],
        "aud": _TOKEN_URL,
        "scope": _SCC_SCOPE,
        "iat": now,
        "exp": now + 3600,
    }
    header_b64 = _base64url_encode(json.dumps(header).encode())
    payload_b64 = _base64url_encode(json.dumps(payload).encode())
    signing_input = f"{header_b64}.{payload_b64}".encode()

    private_key_pem = service_account_info["private_key"].encode()
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    signature = private_key.sign(signing_input, padding.PKCS1v15(), hashes.SHA256())
    sig_b64 = _base64url_encode(signature)
    return f"{header_b64}.{payload_b64}.{sig_b64}"


class GCPSCCClient:
    def __init__(self, **cfg) -> None:
        self._project_id = cfg.get('project_id') or os.environ.get('GCP_PROJECT_ID', '')
        self._org_id = cfg.get('organization_id') or os.environ.get('GCP_ORGANIZATION_ID', '')
        raw_key = cfg.get('service_account_key') or os.environ.get('GCP_SERVICE_ACCOUNT_KEY', '')
        self._service_account_info: dict | None = None
        if raw_key:
            try:
                self._service_account_info = json.loads(raw_key)
            except Exception as e:
                logger.warning("Could not parse GCP_SERVICE_ACCOUNT_KEY as JSON: %s", e)
        self._access_token: str | None = None
        self._token_expires_at: float = 0.0

    def _ensure_token(self) -> None:
        if self._access_token and time.time() < self._token_expires_at - 60:
            return
        if self._service_account_info:
            self._refresh_token_via_jwt()
        else:
            self._refresh_token_via_metadata()

    def _refresh_token_via_jwt(self) -> None:
        assert self._service_account_info
        jwt = _make_jwt(self._service_account_info)
        resp = requests.post(
            _TOKEN_URL,
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": jwt,
            },
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        self._token_expires_at = time.time() + data.get("expires_in", 3600)
        logger.info("GCP token refreshed via service account JWT (expires in %ds)", data.get("expires_in", 3600))

    def _refresh_token_via_metadata(self) -> None:
        """Fetch token from GCE metadata server (instance profile)."""
        resp = requests.get(
            _METADATA_TOKEN_URL,
            headers={"Metadata-Flavor": "Google"},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        self._access_token = data["access_token"]
        self._token_expires_at = time.time() + data.get("expires_in", 3600)
        logger.info("GCP token refreshed via metadata server")

    def _get(self, path: str, params: dict | None = None) -> dict:
        self._ensure_token()
        url = f"{_SCC_BASE}/{path.lstrip('/')}"
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {self._access_token}"},
            params=params or {},
            timeout=60,
        )
        if not resp.ok:
            logger.error("GCP SCC GET %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _get_all(self, path: str, params: dict | None = None, result_key: str = "listFindings") -> list[dict]:
        """Paginated GET — follows nextPageToken."""
        results: list[dict] = []
        p = dict(params or {})
        page_token = ""
        while True:
            if page_token:
                p["pageToken"] = page_token
            data = self._get(path, p)
            # SCC v2 returns different keys depending on the resource type
            page_items = (
                data.get("listFindingsResults")
                or data.get("listAssetsResults")
                or data.get("findings")
                or data.get("assets")
                or []
            )
            results.extend(page_items)
            page_token = data.get("nextPageToken", "")
            if not page_token:
                break
        return results

    # ── Public query methods ───────────────────────────────────────────────────

    def get_findings(self, limit: int = 1000) -> list[dict]:
        """Return active findings across all sources in the organisation.

        SCC v2 requires /locations/global/ in the resource path.
        """
        logger.info("Fetching GCP SCC findings for org %s...", self._org_id)
        try:
            path = f"organizations/{self._org_id}/locations/global/sources/-/findings"
            items = self._get_all(path, {
                "filter": 'state="ACTIVE"',
                "pageSize": min(limit, 1000),
            })
            logger.info("Fetched %d findings", len(items))
            return items[:limit]
        except Exception as e:
            logger.warning("Could not fetch findings: %s", e)
            return []

    def get_assets(self, limit: int = 1000) -> list[dict]:
        """Return assets (GCP resources) in the organisation.

        SCC v2 requires /locations/global/ in the resource path.
        """
        logger.info("Fetching GCP SCC assets for org %s...", self._org_id)
        try:
            path = f"organizations/{self._org_id}/locations/global/assets"
            items = self._get_all(path, {"pageSize": min(limit, 1000)})
            logger.info("Fetched %d assets", len(items))
            return items[:limit]
        except Exception as e:
            logger.warning("Could not fetch assets: %s", e)
            return []
