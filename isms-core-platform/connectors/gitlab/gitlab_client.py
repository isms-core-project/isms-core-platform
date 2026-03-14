"""GitLab REST API client for the GitLab connector.

Handles:
  - Private token or Bearer OAuth auth
  - Paginated GET requests (per_page / X-Next-Page header)
  - Supports GitLab.com and self-managed instances
  - Endpoints used:
      /groups/{group_id}/projects       → A.8.25-26-29
      /projects (membership=true)       → A.8.25-26-29
      /groups/{group_id}/vulnerability_findings → A.8.28
      /groups/{group_id}/security/policies      → A.8.25-26-29
      /groups/{group_id}/members/all    → A.5.3
      /audit_events                     → A.5.3
      /groups/{group_id}/dependencies   → A.8.25-26-29

Config keys: url, token, group_id (optional)
Env vars:    GITLAB_URL, GITLAB_TOKEN, GITLAB_GROUP_ID
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)

GITLAB_DEFAULT = "https://gitlab.com"
PER_PAGE = 100

# GitLab member access levels
ACCESS_LEVEL_NAMES = {
    10: "guest",
    20: "reporter",
    30: "developer",
    40: "maintainer",
    50: "owner",
}


class GitLabClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("GITLAB_URL", GITLAB_DEFAULT)).rstrip("/")
        self.token = cfg.get("token") or os.environ.get("GITLAB_TOKEN", "")
        group_id_raw = cfg.get("group_id") or os.environ.get("GITLAB_GROUP_ID", "")
        self.group_id: str | None = str(group_id_raw) if group_id_raw else None
        if not self.token:
            raise ValueError("GitLab token is required (config key 'token' or GITLAB_TOKEN env var)")

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _headers(self) -> dict:
        return {
            "PRIVATE-TOKEN": self.token,
            "Accept": "application/json",
        }

    # ── Paginated GET (follows X-Next-Page header) ────────────────────────────

    def _get_all(self, path: str, params: dict | None = None) -> list[dict]:
        """Fetch all pages of a GitLab paginated endpoint."""
        items = []
        page = 1
        base_params = dict(params or {})
        base_params["per_page"] = PER_PAGE

        while True:
            req_params = {**base_params, "page": page}
            resp = requests.get(
                f"{self.base_url}{path}",
                headers=self._headers(),
                params=req_params,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                items.extend(data)
                if not data:
                    break
            else:
                break
            next_page = resp.headers.get("X-Next-Page", "")
            if not next_page:
                break
            page = int(next_page)

        return items

    def _get(self, path: str, params: dict | None = None) -> dict | list:
        """Single GET request."""
        resp = requests.get(
            f"{self.base_url}{path}",
            headers=self._headers(),
            params=params,
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_projects(self) -> list[dict]:
        """Projects in the configured group, or all accessible projects."""
        if self.group_id:
            logger.info("Fetching GitLab projects (group_id=%s)...", self.group_id)
            projects = self._get_all(f"/api/v4/groups/{self.group_id}/projects")
        else:
            logger.info("Fetching GitLab projects (membership=true)...")
            projects = self._get_all("/api/v4/projects", params={"membership": "true"})
        logger.info("Fetched %d projects", len(projects))
        return projects

    def get_vulnerabilities(self) -> list[dict]:
        """Detected vulnerability findings for the group."""
        if not self.group_id:
            logger.warning("group_id not set — skipping vulnerability fetch")
            return []
        logger.info("Fetching GitLab vulnerabilities (group_id=%s)...", self.group_id)
        try:
            vulns = self._get_all(
                f"/api/v4/groups/{self.group_id}/vulnerability_findings",
                params={"state": "detected"},
            )
            logger.info("Fetched %d vulnerability findings", len(vulns))
            return vulns
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Vulnerability findings returned %d — requires Ultimate tier and security_dashboard permission",
                    e.response.status_code,
                )
                return []
            raise

    def get_security_policies(self) -> list[dict]:
        """Security policies for the group."""
        if not self.group_id:
            logger.warning("group_id not set — skipping security policy fetch")
            return []
        logger.info("Fetching GitLab security policies (group_id=%s)...", self.group_id)
        try:
            data = self._get(f"/api/v4/groups/{self.group_id}/security/policies")
            policies = data if isinstance(data, list) else []
            logger.info("Fetched %d security policies", len(policies))
            return policies
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Security policies returned %d — requires Ultimate tier",
                    e.response.status_code,
                )
                return []
            raise

    def get_group_members(self) -> list[dict]:
        """All members (including inherited) of the group."""
        if not self.group_id:
            logger.warning("group_id not set — skipping member fetch")
            return []
        logger.info("Fetching GitLab group members (group_id=%s)...", self.group_id)
        members = self._get_all(f"/api/v4/groups/{self.group_id}/members/all")
        logger.info("Fetched %d group members", len(members))
        return members

    def get_audit_events(self, limit: int = 100) -> list[dict]:
        """Instance-level audit events."""
        logger.info("Fetching GitLab audit events (limit=%d)...", limit)
        try:
            events = self._get_all("/api/v4/audit_events", params={"per_page": min(limit, PER_PAGE)})
            logger.info("Fetched %d audit events", len(events))
            return events[:limit]
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Audit events returned %d — requires admin or auditor access",
                    e.response.status_code,
                )
                return []
            raise

    def get_license_compliance(self) -> list[dict]:
        """Dependency/license data for the group."""
        if not self.group_id:
            logger.warning("group_id not set — skipping dependency fetch")
            return []
        logger.info("Fetching GitLab dependencies (group_id=%s)...", self.group_id)
        try:
            deps = self._get_all(f"/api/v4/groups/{self.group_id}/dependencies")
            logger.info("Fetched %d dependencies", len(deps))
            return deps
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Dependencies endpoint returned %d — requires Ultimate tier",
                    e.response.status_code,
                )
                return []
            raise

    @staticmethod
    def access_level_name(level: int) -> str:
        """Convert numeric GitLab access level to human-readable name."""
        return ACCESS_LEVEL_NAMES.get(level, f"level_{level}")
