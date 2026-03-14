"""Generic SIEM REST API client.

Supports three auth modes:
  api_key        — Authorization: Bearer <api_key>
  basic          — HTTP Basic auth (username + password)
  token_endpoint — POST to token_url with client_id + client_secret, use returned Bearer token
                   (compatible with Splunk, IBM QRadar OAuth2, ArcSight ESM)

Config keys / env vars:
  base_url         / SIEM_BASE_URL          — SIEM API root URL (required)
  auth_type        / SIEM_AUTH_TYPE         — api_key | basic | token_endpoint (default: api_key)
  api_key          / SIEM_API_KEY           — bearer token for api_key mode
  username         / SIEM_USERNAME          — username for basic / token_endpoint
  password         / SIEM_PASSWORD          — password for basic / token_endpoint
  token_url        / SIEM_TOKEN_URL         — OAuth2 token endpoint (token_endpoint mode)
  alerts_endpoint  / SIEM_ALERTS_ENDPOINT   — path for alerts/incidents (default: /api/alerts)
  events_endpoint  / SIEM_EVENTS_ENDPOINT   — path for events/logs (default: /api/events)
  verify_ssl       / SIEM_VERIFY_SSL        — true/false (default: true)
"""

import logging
import os

import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)

_DEFAULT_TIMEOUT = 30


class SIEMClient:
    def __init__(
        self,
        base_url: str = "",
        auth_type: str = "api_key",
        api_key: str = "",
        username: str = "",
        password: str = "",
        token_url: str = "",
        alerts_endpoint: str = "/api/alerts",
        events_endpoint: str = "/api/events",
        verify_ssl: bool = True,
        **kwargs,
    ) -> None:
        self.base_url = (
            base_url or os.environ.get("SIEM_BASE_URL", "")
        ).rstrip("/")
        self.auth_type = (
            auth_type or os.environ.get("SIEM_AUTH_TYPE", "api_key")
        ).lower()
        self.api_key = api_key or os.environ.get("SIEM_API_KEY", "")
        self.username = username or os.environ.get("SIEM_USERNAME", "")
        self.password = password or os.environ.get("SIEM_PASSWORD", "")
        self.token_url = token_url or os.environ.get("SIEM_TOKEN_URL", "")
        self.alerts_endpoint = (
            alerts_endpoint or os.environ.get("SIEM_ALERTS_ENDPOINT", "/api/alerts")
        )
        self.events_endpoint = (
            events_endpoint or os.environ.get("SIEM_EVENTS_ENDPOINT", "/api/events")
        )

        _verify = verify_ssl if isinstance(verify_ssl, bool) else True
        _verify_env = os.environ.get("SIEM_VERIFY_SSL", "")
        if _verify_env:
            _verify = _verify_env.lower() not in ("false", "0", "no")
        self.verify_ssl = _verify

        if not self.base_url:
            raise ValueError(
                "SIEM base URL is required (config key 'base_url' or SIEM_BASE_URL env var)"
            )

        # Cached Bearer token for token_endpoint mode (lazily populated)
        self._bearer_token: str | None = None

        if not self.verify_ssl:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for SIEM client")

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _get_token(self) -> str:
        """Obtain a Bearer token via OAuth2 token_endpoint grant."""
        if not self.token_url:
            raise ValueError(
                "token_url is required for auth_type='token_endpoint' "
                "(config key 'token_url' or SIEM_TOKEN_URL env var)"
            )
        logger.info("Obtaining Bearer token from %s ...", self.token_url)
        resp = requests.post(
            self.token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self.username,
                "client_secret": self.password,
            },
            verify=self.verify_ssl,
            timeout=_DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        data = resp.json()
        token = data.get("access_token") or data.get("token") or data.get("sessionKey", "")
        if not token:
            raise ValueError(
                f"token_endpoint response did not contain access_token: {list(data.keys())}"
            )
        logger.info("SIEM Bearer token acquired")
        return token

    def _headers(self) -> dict:
        """Return auth headers appropriate for the configured auth_type."""
        if self.auth_type == "api_key":
            return {
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json",
            }
        elif self.auth_type == "basic":
            # requests handles Basic auth separately via `auth=` kwarg;
            # we return only content headers here and use _basic_auth() for the auth param.
            return {"Accept": "application/json"}
        elif self.auth_type == "token_endpoint":
            if not self._bearer_token:
                self._bearer_token = self._get_token()
            return {
                "Authorization": f"Bearer {self._bearer_token}",
                "Accept": "application/json",
            }
        else:
            logger.warning("Unknown auth_type '%s' — falling back to Bearer api_key", self.auth_type)
            return {
                "Authorization": f"Bearer {self.api_key}",
                "Accept": "application/json",
            }

    def _basic_auth(self) -> HTTPBasicAuth | None:
        """Return HTTPBasicAuth object when auth_type is 'basic', else None."""
        if self.auth_type == "basic":
            return HTTPBasicAuth(self.username, self.password)
        return None

    def _get(self, path: str, params: dict | None = None) -> requests.Response:
        """Perform a GET request using the configured auth mode."""
        url = f"{self.base_url}{path}"
        resp = requests.get(
            url,
            headers=self._headers(),
            auth=self._basic_auth(),
            params=params or {},
            verify=self.verify_ssl,
            timeout=_DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        return resp

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_alerts(self, limit: int = 200) -> list[dict]:
        """GET {base_url}{alerts_endpoint}?limit=N.

        Returns whatever the SIEM returns as a list of dicts.
        The connector is responsible for normalising field names.
        Returns [] on any HTTP error.
        """
        logger.info("Fetching SIEM alerts (endpoint=%s, limit=%d) ...", self.alerts_endpoint, limit)
        try:
            resp = self._get(self.alerts_endpoint, params={"limit": limit})
            data = resp.json()
            # Most SIEMs wrap results — try common envelope keys, fall back to bare list
            if isinstance(data, list):
                alerts = data
            else:
                alerts = (
                    data.get("alerts")
                    or data.get("incidents")
                    or data.get("events")
                    or data.get("data")
                    or data.get("results")
                    or data.get("value")
                    or []
                )
            logger.info("Fetched %d alerts from SIEM", len(alerts))
            return alerts
        except requests.HTTPError as e:
            logger.error(
                "SIEM alerts fetch failed (HTTP %s): %s",
                e.response.status_code,
                e.response.text[:300],
            )
            return []
        except Exception as e:
            logger.error("SIEM alerts fetch failed: %s", e)
            return []

    def get_summary(self) -> dict:
        """GET {base_url}/api/summary or /api/status.

        Returns whatever the SIEM provides as a summary/health dict.
        Falls back to {} on any error — callers must handle missing keys gracefully.
        """
        for path in ("/api/summary", "/api/status", "/api/health"):
            try:
                resp = self._get(path)
                data = resp.json()
                if isinstance(data, dict):
                    logger.info("SIEM summary fetched from %s", path)
                    return data
            except Exception:
                continue
        logger.debug("SIEM summary endpoint not available — returning {}")
        return {}
