"""ServiceNow REST API client (Table API).

Uses the ServiceNow Table API for incidents, change requests, and problems.
Authentication: Basic auth (username/password) or OAuth2 client credentials.

Environment variables:
  SNOW_INSTANCE      — ServiceNow instance name, e.g. mycompany (→ mycompany.service-now.com)
  SNOW_USERNAME      — Service account username (itil or readonly role)
  SNOW_PASSWORD      — Service account password
  SNOW_LOOKBACK_DAYS — How many days back to pull (default: 30)

API: https://<instance>.service-now.com/api/now/table/<table>

Minimum ServiceNow permissions for the service account:
  - itil role (read access to incidents, changes, problems, CMDB)
  - OR custom role with table read access only
"""

import logging
import os
from datetime import datetime, timedelta, timezone

import requests

logger = logging.getLogger(__name__)


class ServiceNowClient:
    def __init__(self, **cfg) -> None:
        instance = (cfg.get('instance') or os.environ["SNOW_INSTANCE"]).replace(".service-now.com", "")
        self._base_url = f"https://{instance}.service-now.com/api/now"
        self._auth = (
            cfg.get('username') or os.environ["SNOW_USERNAME"],
            cfg.get('password') or os.environ["SNOW_PASSWORD"],
        )
        self._lookback_days = int(cfg.get('lookback_days') or os.environ.get("SNOW_LOOKBACK_DAYS", "30"))
        self._session = requests.Session()
        self._session.auth = self._auth
        self._session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _lookback_date(self) -> str:
        """Return a ServiceNow-formatted date for the lookback window."""
        cutoff = datetime.now(timezone.utc) - timedelta(days=self._lookback_days)
        return cutoff.strftime("%Y-%m-%d %H:%M:%S")

    def _get_table(self, table: str, query: str, fields: list[str], limit: int = 1000) -> list[dict]:
        """Paginated GET from ServiceNow Table API."""
        results: list[dict] = []
        offset = 0
        page_size = min(limit, 100)

        while len(results) < limit:
            try:
                resp = self._session.get(
                    f"{self._base_url}/table/{table}",
                    params={
                        "sysparm_query": query,
                        "sysparm_fields": ",".join(fields),
                        "sysparm_limit": page_size,
                        "sysparm_offset": offset,
                        "sysparm_display_value": "true",  # human-readable values
                    },
                    timeout=30,
                )
                resp.raise_for_status()
                page = resp.json().get("result", [])
                results.extend(page)
                if len(page) < page_size:
                    break
                offset += page_size
            except requests.HTTPError as e:
                logger.error("ServiceNow API error %s for table %s: %s",
                             e.response.status_code, table, e.response.text[:200])
                raise
            except Exception as e:
                logger.error("ServiceNow request failed for %s: %s", table, e)
                raise

        return results[:limit]

    # ── Public query methods ──────────────────────────────────────────────────

    def get_incidents(self) -> list[dict]:
        """Return security-relevant incidents from the lookback window."""
        cutoff = self._lookback_date()
        logger.info("Fetching incidents from ServiceNow (since %s)...", cutoff)
        items = self._get_table(
            "incident",
            query=f"sys_created_on>={cutoff}^ORDERBYDESCsys_created_on",
            fields=[
                "number", "short_description", "description", "category",
                "subcategory", "priority", "severity", "state", "impact",
                "urgency", "opened_at", "resolved_at", "closed_at",
                "assigned_to", "assignment_group", "sys_created_on",
            ],
        )
        logger.info("Fetched %d incidents", len(items))
        return items

    def get_change_requests(self) -> list[dict]:
        """Return change requests from the lookback window."""
        cutoff = self._lookback_date()
        logger.info("Fetching change requests from ServiceNow (since %s)...", cutoff)
        items = self._get_table(
            "change_request",
            query=f"sys_created_on>={cutoff}^ORDERBYDESCsys_created_on",
            fields=[
                "number", "short_description", "description", "type",
                "category", "priority", "risk", "state", "approval",
                "start_date", "end_date", "closed_at", "sys_created_on",
                "assigned_to", "assignment_group",
            ],
        )
        logger.info("Fetched %d change requests", len(items))
        return items

    def get_problems(self) -> list[dict]:
        """Return problem records from the lookback window."""
        cutoff = self._lookback_date()
        logger.info("Fetching problems from ServiceNow (since %s)...", cutoff)
        try:
            items = self._get_table(
                "problem",
                query=f"sys_created_on>={cutoff}^ORDERBYDESCsys_created_on",
                fields=[
                    "number", "short_description", "description", "priority",
                    "state", "category", "sys_created_on", "resolved_at",
                    "assigned_to",
                ],
            )
            logger.info("Fetched %d problems", len(items))
            return items
        except Exception as e:
            logger.warning("Could not fetch problems: %s", e)
            return []
