"""GitHub REST API client for the GitHub connector.

Handles:
  - Bearer token (PAT) auth
  - Paginated GET requests (per_page / Link header)
  - Supports GitHub.com and GitHub Enterprise Server
  - Endpoints used:
      /orgs/{org}/repos                          → A.8.25-26-29
      /orgs/{org}/secret-scanning/alerts         → A.8.25-26-29
      /orgs/{org}/code-scanning/alerts           → A.8.28
      /orgs/{org}/dependabot/alerts              → A.8.25-26-29
      /orgs/{org}/members                        → A.5.3
      /orgs/{org}                                → A.5.3

Config keys: token, org, url (optional for GHE)
Env vars:    GITHUB_TOKEN, GITHUB_ORG, GITHUB_URL
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

GITHUB_API_DEFAULT = "https://api.github.com"
PER_PAGE = 100


class GitHubClient:
    def __init__(self, **cfg) -> None:
        self.token = cfg.get("token") or os.environ.get("GITHUB_TOKEN", "")
        self.org = cfg.get("org") or os.environ.get("GITHUB_ORG", "")
        raw_url = cfg.get("url") or os.environ.get("GITHUB_URL", "")
        # GitHub Enterprise: base is https://<host>/api/v3
        if raw_url:
            self.api_base = raw_url.rstrip("/")
        else:
            self.api_base = GITHUB_API_DEFAULT
        if not self.token:
            raise ValueError("GitHub token is required (config key 'token' or GITHUB_TOKEN env var)")
        if not self.org:
            raise ValueError("GitHub org is required (config key 'org' or GITHUB_ORG env var)")

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    # ── Paginated GET (follows Link: <url>; rel="next") ───────────────────────

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of a GitHub paginated endpoint."""
        items = []
        url: str | None = f"{self.api_base}{path}"
        req_params = dict(params or {})
        req_params.setdefault("per_page", PER_PAGE)

        while url:
            resp = requests.get(url, headers=self._headers(), params=req_params, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                items.extend(data)
            else:
                # Some endpoints return a wrapper dict
                items.extend(data.get("items", data.get("value", [])))
            # Follow Link header
            url = None
            link_header = resp.headers.get("Link", "")
            for part in link_header.split(","):
                if 'rel="next"' in part:
                    url = part.split(";")[0].strip().strip("<>")
                    break
            req_params = {}  # params are baked into the next URL

        return items

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_repos(self) -> list[dict]:
        """All repositories in the org."""
        logger.info("Fetching GitHub repos (org=%s)...", self.org)
        repos = self._get_all(f"/orgs/{self.org}/repos", params={"type": "all"})
        logger.info("Fetched %d repos", len(repos))
        return repos

    def get_secret_scanning_alerts(self) -> list[dict]:
        """Open secret scanning alerts for the org."""
        logger.info("Fetching GitHub secret scanning alerts...")
        try:
            alerts = self._get_all(
                f"/orgs/{self.org}/secret-scanning/alerts",
                params={"state": "open"},
            )
            logger.info("Fetched %d open secret scanning alerts", len(alerts))
            return alerts
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Secret scanning alerts returned %d — "
                    "requires GitHub Advanced Security and admin:org scope",
                    e.response.status_code,
                )
                return []
            raise

    def get_code_scanning_alerts(self) -> list[dict]:
        """Open SAST (code scanning) alerts for the org."""
        logger.info("Fetching GitHub code scanning alerts...")
        try:
            alerts = self._get_all(
                f"/orgs/{self.org}/code-scanning/alerts",
                params={"state": "open"},
            )
            logger.info("Fetched %d open code scanning alerts", len(alerts))
            return alerts
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Code scanning alerts returned %d — requires GitHub Advanced Security",
                    e.response.status_code,
                )
                return []
            raise

    def get_dependabot_alerts(self) -> list[dict]:
        """Open Dependabot (SCA) alerts for the org."""
        logger.info("Fetching GitHub Dependabot alerts...")
        try:
            alerts = self._get_all(
                f"/orgs/{self.org}/dependabot/alerts",
                params={"state": "open"},
            )
            logger.info("Fetched %d open Dependabot alerts", len(alerts))
            return alerts
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Dependabot alerts returned %d — requires Dependabot enabled and security_events scope",
                    e.response.status_code,
                )
                return []
            raise

    def get_org_members(self) -> list[dict]:
        """All members of the org."""
        logger.info("Fetching GitHub org members...")
        members = self._get_all(f"/orgs/{self.org}/members")
        logger.info("Fetched %d org members", len(members))
        return members

    def get_org_settings(self) -> dict:
        """Org-level settings including two_factor_requirement_enabled."""
        logger.info("Fetching GitHub org settings...")
        try:
            resp = requests.get(
                f"{self.api_base}/orgs/{self.org}",
                headers=self._headers(),
                timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
            logger.info("Fetched org settings (two_factor_requirement_enabled=%s)",
                        data.get("two_factor_requirement_enabled"))
            return data
        except requests.HTTPError as e:
            logger.warning("Org settings returned %d: %s", e.response.status_code, e)
            return {}
