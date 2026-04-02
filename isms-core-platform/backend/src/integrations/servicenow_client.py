"""ServiceNow Table API client — create tasks/incidents and fetch status."""

import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)


class ServiceNowClient:
    def __init__(self, instance_url: str, username: str, password: str, table: str = "task"):
        self.base_url = instance_url.rstrip("/")
        self.table = table
        self._auth = (username, password)

    def _headers(self) -> dict[str, str]:
        return {"Accept": "application/json", "Content-Type": "application/json"}

    def create_task(
        self,
        short_description: str,
        description: str = "",
        assignment_group: str | None = None,
        urgency: int = 3,      # 1=high, 2=medium, 3=low
        impact: int = 3,
    ) -> dict[str, Any]:
        """Create a ServiceNow task and return {sys_id, number, url}."""
        payload: dict[str, Any] = {
            "short_description": short_description,
            "description":       description,
            "urgency":           str(urgency),
            "impact":            str(impact),
        }
        if assignment_group:
            payload["assignment_group"] = assignment_group

        resp = httpx.post(
            f"{self.base_url}/api/now/table/{self.table}",
            auth=self._auth,
            headers=self._headers(),
            json=payload,
            timeout=15,
        )
        resp.raise_for_status()
        result = resp.json()["result"]
        sys_id = result["sys_id"]
        number = result.get("number", sys_id)
        return {
            "id":  sys_id,
            "key": number,
            "url": f"{self.base_url}/nav_to.do?uri=/{self.table}.do?sys_id={sys_id}",
        }

    def get_task_status(self, sys_id: str) -> str:
        """Return the state label of a ServiceNow task."""
        resp = httpx.get(
            f"{self.base_url}/api/now/table/{self.table}/{sys_id}?sysparm_fields=state",
            auth=self._auth,
            headers=self._headers(),
            timeout=10,
        )
        resp.raise_for_status()
        state = resp.json()["result"].get("state", "")
        state_map = {"1": "Open", "2": "In Progress", "3": "On Hold", "6": "Resolved", "7": "Closed"}
        return state_map.get(str(state), str(state))


def from_connector_config(config: dict) -> ServiceNowClient:
    return ServiceNowClient(
        instance_url=config["instance_url"],
        username=config["username"],
        password=config["password"],
        table=config.get("table", "task"),
    )
