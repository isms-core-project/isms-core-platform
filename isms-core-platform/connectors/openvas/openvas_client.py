"""OpenVAS / Greenbone Vulnerability Manager (GVM) API client.

Uses the Greenbone Security Assistant (GSA) REST API available in GVM 22.4+.
Authentication: session token obtained via POST /login.

Older GVM deployments may not have the REST API — in that case the XML-based
Greenbone Management Protocol (GMP) over a Unix socket is the alternative.
This client targets the GSA REST API (JSON).

Environment variables:
  OPENVAS_URL       — GSA base URL, e.g. https://greenbone.corp.local
  OPENVAS_USERNAME  — GVM username (read-only account recommended)
  OPENVAS_PASSWORD  — GVM password
  OPENVAS_VERIFY_SSL — "false" to disable certificate verification (self-signed)

GSA REST API base: /api/v1 (GVM 22.4+)
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class OpenVASClient:
    def __init__(self, **cfg) -> None:
        base = cfg.get('url') or os.environ.get('OPENVAS_URL', '')
        self._base_url = base.rstrip('/')
        self._username = cfg.get('username') or os.environ.get('OPENVAS_USERNAME', '')
        self._password = cfg.get('password') or os.environ.get('OPENVAS_PASSWORD', '')
        verify_raw = cfg.get('verify_ssl', os.environ.get('OPENVAS_VERIFY_SSL', 'true'))
        if isinstance(verify_raw, bool):
            self._verify = verify_raw
        else:
            self._verify = str(verify_raw).lower() != 'false'
        if not self._base_url or not self._username or not self._password:
            raise ValueError("OpenVAS connector requires url, username, and password")
        if not self._verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for %s", self._base_url)
        self._session = requests.Session()
        self._token: str | None = None

    def _ensure_authenticated(self) -> None:
        if self._token:
            return
        resp = self._session.post(
            f"{self._base_url}/api/v1/auth/login",
            json={"username": self._username, "password": self._password},
            verify=self._verify,
            timeout=30,
        )
        if not resp.ok:
            logger.error("OpenVAS login failed %s: %s", resp.status_code, resp.text[:300])
        resp.raise_for_status()
        data = resp.json()
        # GVM returns token in data.token or as a cookie
        self._token = data.get("token") or data.get("data", {}).get("token", "")
        if self._token:
            self._session.headers.update({"Authorization": f"Bearer {self._token}"})
        logger.info("OpenVAS authenticated to %s", self._base_url)

    def _get(self, path: str, params: dict | None = None) -> dict:
        self._ensure_authenticated()
        url = f"{self._base_url}/{path.lstrip('/')}"
        resp = self._session.get(url, params=params or {}, verify=self._verify, timeout=60)
        if not resp.ok:
            logger.error("OpenVAS GET %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    # ── Public query methods ───────────────────────────────────────────────────

    def get_tasks(self) -> list[dict]:
        """Return list of scan tasks."""
        logger.info("Fetching scan tasks from OpenVAS...")
        try:
            data = self._get("api/v1/tasks")
            tasks = data.get("tasks", data.get("data", []))
            if isinstance(tasks, dict):
                tasks = tasks.get("task", [])
            if not isinstance(tasks, list):
                tasks = [tasks] if tasks else []
            logger.info("Fetched %d tasks", len(tasks))
            return tasks
        except Exception as e:
            logger.warning("Could not fetch tasks: %s", e)
            return []

    def get_reports_summary(self, limit: int = 50) -> list[dict]:
        """Return most recent scan reports sorted by date descending."""
        logger.info("Fetching reports from OpenVAS...")
        try:
            data = self._get(
                "api/v1/reports",
                params={"filter": "rows=50 sort-reverse=date"},
            )
            reports = data.get("reports", data.get("data", []))
            if isinstance(reports, dict):
                reports = reports.get("report", [])
            if not isinstance(reports, list):
                reports = [reports] if reports else []
            logger.info("Fetched %d reports", len(reports))
            return reports[:limit]
        except Exception as e:
            logger.warning("Could not fetch reports: %s", e)
            return []

    def get_hosts_summary(self) -> dict:
        """Return host/asset summary from the assets endpoint."""
        logger.info("Fetching hosts from OpenVAS assets...")
        try:
            data = self._get("api/v1/assets/hosts", params={"filter": "rows=1"})
            # Total is often in a meta or filtered_count field
            total = (
                data.get("total_count")
                or data.get("filtered_count")
                or len(data.get("hosts", data.get("data", [])))
            )
            logger.info("OpenVAS total hosts: %s", total)
            return {"total_hosts": int(total)}
        except Exception as e:
            logger.warning("Could not fetch hosts: %s", e)
            return {}
