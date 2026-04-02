"""Jira REST API v3 client — create issues and fetch status."""

import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

# Jira issue type map: our severity/priority → Jira issue type name
DEFAULT_ISSUE_TYPE = "Task"


class JiraClient:
    def __init__(self, url: str, email: str, api_token: str, project_key: str):
        self.base_url = url.rstrip("/")
        self.project_key = project_key
        self._auth = (email, api_token)

    def _headers(self) -> dict[str, str]:
        return {"Accept": "application/json", "Content-Type": "application/json"}

    def create_issue(
        self,
        summary: str,
        description: str = "",
        issue_type: str = DEFAULT_ISSUE_TYPE,
        priority: str | None = None,
        labels: list[str] | None = None,
    ) -> dict[str, Any]:
        """Create a Jira issue and return {id, key, url}."""
        fields: dict[str, Any] = {
            "project":   {"key": self.project_key},
            "summary":   summary,
            "issuetype": {"name": issue_type},
            "description": {
                "type":    "doc",
                "version": 1,
                "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}],
            },
        }
        if priority:
            fields["priority"] = {"name": priority.capitalize()}
        if labels:
            fields["labels"] = labels

        resp = httpx.post(
            f"{self.base_url}/rest/api/3/issue",
            auth=self._auth,
            headers=self._headers(),
            json={"fields": fields},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        return {
            "id":  data["id"],
            "key": data["key"],
            "url": f"{self.base_url}/browse/{data['key']}",
        }

    def get_issue_status(self, issue_key: str) -> str:
        """Return the status name of a Jira issue."""
        resp = httpx.get(
            f"{self.base_url}/rest/api/3/issue/{issue_key}?fields=status",
            auth=self._auth,
            headers=self._headers(),
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()["fields"]["status"]["name"]


def from_connector_config(config: dict) -> JiraClient:
    return JiraClient(
        url=config["url"],
        email=config["email"],
        api_token=config["api_token"],
        project_key=config.get("project_key", "ISMS"),
    )
