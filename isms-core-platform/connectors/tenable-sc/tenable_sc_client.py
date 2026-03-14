"""Tenable Security Center (Tenable.sc) REST API client.

On-premises vulnerability management platform. Supports two auth methods:
  - API Key (preferred, Tenable.sc 5.13+): X-APIKey header
  - Session token (legacy): POST /rest/token → X-SecurityCenter header

Elastic integration reference: github.com/elastic/integrations/tree/main/packages/tenable_sc
OpenCTI connector reference:   github.com/OpenCTI-Platform/connectors/tree/master/external-import/tenable-security-center

Environment variables:
  TENABLE_SC_HOST        — Tenable.sc hostname/IP (no trailing slash)
  TENABLE_SC_ACCESS_KEY  — API access key (preferred auth, Tenable.sc 5.13+)
  TENABLE_SC_SECRET_KEY  — API secret key (paired with access key)
  TENABLE_SC_USERNAME    — Username (fallback if no API keys configured)
  TENABLE_SC_PASSWORD    — Password (fallback)
  TENABLE_SC_VERIFY_SSL  — "false" to skip cert check (default: true)
  TENABLE_SC_PORT        — HTTPS port (default: 443)
  TENABLE_SC_VULN_LIMIT  — max vuln details rows to fetch (default: 1000)
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class TenableSCClient:
    """Thin client for the Tenable.sc REST API."""

    def __init__(self, **cfg) -> None:
        host = (cfg.get('host') or os.environ["TENABLE_SC_HOST"]).rstrip("/")
        port = os.environ.get("TENABLE_SC_PORT", "443")
        self.base_url = f"https://{host}:{port}/rest"
        self.verify_ssl = (cfg.get('verify_ssl') or os.environ.get("TENABLE_SC_VERIFY_SSL", "true")).lower() != "false"
        self.vuln_limit = int(os.environ.get("TENABLE_SC_VULN_LIMIT", "1000"))

        # Auth: API key preferred
        self.access_key = cfg.get('access_key') or os.environ.get("TENABLE_SC_ACCESS_KEY", "")
        self.secret_key = cfg.get('secret_key') or os.environ.get("TENABLE_SC_SECRET_KEY", "")
        self.username = cfg.get('username') or os.environ.get("TENABLE_SC_USERNAME", "")
        self.password = cfg.get('password') or os.environ.get("TENABLE_SC_PASSWORD", "")

        if not self.verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for Tenable.sc")

        self._session = requests.Session()
        self._session.verify = self.verify_ssl
        self._session.headers.update({"Accept": "application/json"})

        self._authenticated = False
        self._auth()

    # ── Authentication ────────────────────────────────────────────────────────

    def _auth(self) -> None:
        """Configure session auth. API key takes precedence over session token."""
        if self.access_key and self.secret_key:
            # API key auth (Tenable.sc 5.13+) — stateless, no session needed
            self._session.headers.update({
                "X-APIKey": f"accesskey={self.access_key};secretkey={self.secret_key}",
            })
            self._authenticated = True
            logger.info("Tenable.sc: using API key authentication")
        elif self.username and self.password:
            self._session_auth()
        else:
            raise ValueError(
                "Tenable.sc: set TENABLE_SC_ACCESS_KEY+SECRET_KEY or "
                "TENABLE_SC_USERNAME+PASSWORD"
            )

    def _session_auth(self) -> None:
        """Session token auth for Tenable.sc versions prior to 5.13."""
        resp = self._session.post(
            f"{self.base_url}/token",
            json={"username": self.username, "password": self.password},
            timeout=30,
        )
        resp.raise_for_status()
        token = resp.json()["response"]["token"]
        self._session.headers.update({"X-SecurityCenter": str(token)})
        self._authenticated = True
        logger.info("Tenable.sc: session token acquired")

    # ── API helpers ───────────────────────────────────────────────────────────

    def _get(self, path: str, params: dict | None = None) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self._session.get(url, params=params, timeout=60)
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, body: dict) -> dict:
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self._session.post(url, json=body, timeout=120)
        resp.raise_for_status()
        return resp.json()

    # ── API methods ───────────────────────────────────────────────────────────

    def get_system_info(self) -> dict:
        """GET /rest/system — server info, version, licence."""
        return self._get("/system")

    def get_vulnerability_summary(self) -> dict:
        """POST /rest/analysis — severity breakdown across all assets (cumulative).

        Uses tool=sumseverity which returns counts by severity level:
          severity 0 = Info | 1 = Low | 2 = Medium | 3 = High | 4 = Critical
        """
        return self._post("/analysis", {
            "type": "vuln",
            "sourceType": "cumulative",
            "query": {
                "type": "vuln",
                "tool": "sumseverity",
                "filters": [],
            },
        })

    def get_critical_vulnerabilities(self) -> dict:
        """POST /rest/analysis — individual critical/high vuln details.

        Returns up to TENABLE_SC_VULN_LIMIT rows with plugin name, host, CVE.
        Severity filter: 3 (High) + 4 (Critical).
        """
        return self._post("/analysis", {
            "type": "vuln",
            "sourceType": "cumulative",
            "query": {
                "type": "vuln",
                "tool": "vulndetails",
                "filters": [
                    {"filterName": "severity", "operator": "=", "value": "3,4"},
                ],
                "columns": [
                    {"name": "severity"},
                    {"name": "ip"},
                    {"name": "dnsName"},
                    {"name": "pluginName"},
                    {"name": "pluginID"},
                    {"name": "cvssV3BaseScore"},
                    {"name": "cve"},
                    {"name": "firstSeen"},
                    {"name": "lastSeen"},
                ],
            },
            "startOffset": 0,
            "endOffset": min(self.vuln_limit, 2000),
        })

    def get_assets(self) -> dict:
        """GET /rest/asset — list of all defined asset objects.

        Asset types: static | dynamic | dnsname | dnsnameupload | ldapquery | combination
        """
        return self._get("/asset", params={"fields": "id,name,type,description,ipCount"})

    def get_scan_results(self) -> dict:
        """GET /rest/scanResult — recent completed scan results."""
        return self._get("/scanResult", params={
            "fields": "id,name,status,startTime,finishTime,importStatus,completedIPs,totalIPs",
            "startOffset": 0,
            "endOffset": 50,
        })
