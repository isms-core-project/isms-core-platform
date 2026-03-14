"""Jira / Jira Service Management REST API client.

Supports both Jira Cloud (Atlassian cloud) and Jira Data Center (on-premises).
Authentication: API token (cloud) or basic auth with API token (DC).

Environment variables:
  JIRA_URL         — Base URL, e.g. https://mycompany.atlassian.net (cloud)
                     or https://jira.corp.local (data center)
  JIRA_USERNAME    — Jira account email (cloud) or username (DC)
  JIRA_API_TOKEN   — API token (cloud: from id.atlassian.com; DC: from profile)
  JIRA_JQL         — Optional: extra JQL filter to scope issues (e.g. project=ITSEC)
  JIRA_LOOKBACK_DAYS — Days of history (default: 30)

API: https://developer.atlassian.com/cloud/jira/platform/rest/v3/
     https://developer.atlassian.com/server/jira/platform/rest-apis/ (DC)
"""

import logging
import os
from datetime import datetime, timedelta, timezone

import requests

logger = logging.getLogger(__name__)


class JiraClient:
    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ["JIRA_URL"]).rstrip("/")
        username = cfg.get('username') or os.environ["JIRA_USERNAME"]
        api_token = cfg.get('api_token') or os.environ["JIRA_API_TOKEN"]
        self._auth = (username, api_token)
        self._lookback_days = int(cfg.get('lookback_days') or os.environ.get("JIRA_LOOKBACK_DAYS", "30"))
        self._extra_jql = (cfg.get('jql') or os.environ.get("JIRA_JQL", "")).strip()

        self._session = requests.Session()
        self._session.auth = self._auth
        self._session.headers.update({"Accept": "application/json"})

    def _lookback_jql(self) -> str:
        cutoff = datetime.now(timezone.utc) - timedelta(days=self._lookback_days)
        return cutoff.strftime("%Y-%m-%d")

    def _search(self, jql: str, fields: list[str], max_results: int = 500) -> list[dict]:
        """Paginated search via /rest/api/3/search (Jira Cloud) or /2/search (DC)."""
        results: list[dict] = []
        start_at = 0
        page_size = 50

        # Try v3 first (Cloud), fall back to v2 (DC)
        for api_version in ("3", "2"):
            url = f"{self._base_url}/rest/api/{api_version}/search"
            try:
                resp = self._session.get(url, params={"jql": "project IS NOT EMPTY"}, timeout=10)
                if resp.status_code < 500:
                    break
            except Exception:
                continue

        while len(results) < max_results:
            try:
                resp = self._session.get(
                    url,
                    params={
                        "jql": jql,
                        "startAt": start_at,
                        "maxResults": page_size,
                        "fields": ",".join(fields),
                    },
                    timeout=30,
                )
                resp.raise_for_status()
                data = resp.json()
                page = data.get("issues", [])
                results.extend(page)
                total = data.get("total", 0)
                start_at += len(page)
                if start_at >= total or not page:
                    break
            except requests.HTTPError as e:
                logger.error("Jira API error %s: %s", e.response.status_code, e.response.text[:200])
                raise
            except Exception as e:
                logger.error("Jira request failed: %s", e)
                raise

        return results[:max_results]

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_issues(self, issue_types: list[str] | None = None) -> list[dict]:
        """Return issues from the lookback window, optionally filtered by type."""
        cutoff = self._lookback_jql()
        type_filter = ""
        if issue_types:
            quoted = ", ".join(f'"{t}"' for t in issue_types)
            type_filter = f" AND issuetype in ({quoted})"

        extra = f" AND ({self._extra_jql})" if self._extra_jql else ""
        jql = f"created >= {cutoff}{type_filter}{extra} ORDER BY created DESC"

        logger.info("Fetching Jira issues: %s", jql)
        items = self._search(
            jql,
            fields=[
                "summary", "description", "issuetype", "priority", "status",
                "assignee", "reporter", "created", "updated", "resolutiondate",
                "labels", "components", "project",
            ],
        )
        logger.info("Fetched %d issues", len(items))
        return items

    def get_service_requests(self) -> list[dict]:
        """Return JSM service requests (helpdesk tickets)."""
        cutoff = self._lookback_jql()
        extra = f" AND ({self._extra_jql})" if self._extra_jql else ""
        jql = (
            f"issuetype = \"Service Request\" AND created >= {cutoff}{extra} "
            f"ORDER BY created DESC"
        )
        try:
            logger.info("Fetching JSM service requests...")
            items = self._search(
                jql,
                fields=["summary", "issuetype", "priority", "status", "created", "resolutiondate"],
            )
            logger.info("Fetched %d service requests", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch service requests: %s", e)
            return []
