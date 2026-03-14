"""Jira / Jira Service Management connector for ISMS CORE v2.0.

Pulls issues from Jira and posts evidence to:
  a.5.25  — Response to information security incidents  (Bug/Incident issue types)
  a.8.32  — Change management  (Change/Task issue types)

Supports: Jira Cloud (Atlassian) and Jira Data Center (on-premises).

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  JIRA_URL              — e.g. https://mycompany.atlassian.net
  JIRA_USERNAME         — Jira email/username
  JIRA_API_TOKEN        — API token (cloud: from id.atlassian.com)
  JIRA_JQL              — Optional extra JQL filter (e.g. project=ITSEC)
  JIRA_LOOKBACK_DAYS    — Days of history (default: 30)
  POLL_INTERVAL         — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from jira_client import JiraClient

logger = logging.getLogger(__name__)

# Issue types to treat as incidents/security events
INCIDENT_TYPES = {"Bug", "Incident", "Security Incident", "Problem", "Vulnerability"}
# Issue types to treat as change requests
CHANGE_TYPES = {"Change", "Change Request", "Task", "Story", "Epic"}


class JiraConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.jira = JiraClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Fetch all issues from the lookback window."""
        all_issues = self.jira.get_issues()

        return [
            {
                "_type": "jira_bundle",
                "issues": all_issues,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _extract_field(self, issue: dict, field: str) -> str:
        """Safely extract a displayable value from a Jira issue field."""
        fields = issue.get("fields", {})
        val = fields.get(field)
        if val is None:
            return ""
        if isinstance(val, dict):
            # Try common name patterns
            return str(val.get("name") or val.get("displayName") or val.get("value") or "")
        return str(val)

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        issues = bundle["issues"]
        fetched_at = bundle["fetched_at"]

        # Split into incidents vs changes by issue type
        incident_issues = [
            i for i in issues
            if self._extract_field(i, "issuetype") in INCIDENT_TYPES
        ]
        change_issues = [
            i for i in issues
            if self._extract_field(i, "issuetype") in CHANGE_TYPES
        ]
        other_issues = [
            i for i in issues
            if i not in incident_issues and i not in change_issues
        ]

        # ── A.5.25 — Incident management ─────────────────────────────────────
        by_priority: dict[str, int] = Counter(self._extract_field(i, "priority") for i in incident_issues)
        by_status: dict[str, int] = Counter(self._extract_field(i, "status") for i in incident_issues)
        open_incidents = [
            i for i in incident_issues
            if self._extract_field(i, "status").lower() not in ("done", "closed", "resolved", "cancelled")
        ]
        high_prio = sum(
            1 for i in incident_issues
            if self._extract_field(i, "priority").lower() in ("highest", "high", "critical")
        )

        incident_status = "compliant"
        if high_prio > 5:
            incident_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.5.24-28",
            title=(
                f"Jira incidents ({self.jira._lookback_days}d): "
                f"{len(incident_issues)} total, {len(open_incidents)} open, "
                f"{high_prio} high/critical"
            ),
            source_ref="jira-incident-summary",
            classification="incident",
            status=incident_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "lookback_days": self.jira._lookback_days,
                "total_incidents": len(incident_issues),
                "open_count": len(open_incidents),
                "high_priority_count": high_prio,
                "by_priority": dict(by_priority),
                "by_status": dict(by_status),
                "other_issues_count": len(other_issues),
                "recent_incidents": [
                    {
                        "key": i.get("key"),
                        "summary": self._extract_field(i, "summary"),
                        "type": self._extract_field(i, "issuetype"),
                        "priority": self._extract_field(i, "priority"),
                        "status": self._extract_field(i, "status"),
                        "created": i.get("fields", {}).get("created"),
                    }
                    for i in incident_issues[:30]
                ],
            },
        ))

        # ── A.8.32 — Change management ────────────────────────────────────────
        by_change_status: dict[str, int] = Counter(
            self._extract_field(i, "status") for i in change_issues
        )
        by_change_type: dict[str, int] = Counter(
            self._extract_field(i, "issuetype") for i in change_issues
        )
        open_changes = [
            i for i in change_issues
            if self._extract_field(i, "status").lower() not in ("done", "closed", "cancelled")
        ]

        change_status = "compliant" if len(open_changes) < 50 else "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.32",
            title=(
                f"Jira changes ({self.jira._lookback_days}d): "
                f"{len(change_issues)} total, {len(open_changes)} in-progress"
            ),
            source_ref="jira-change-summary",
            classification="change",
            status=change_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "lookback_days": self.jira._lookback_days,
                "total_changes": len(change_issues),
                "open_count": len(open_changes),
                "by_status": dict(by_change_status),
                "by_type": dict(by_change_type),
                "recent_changes": [
                    {
                        "key": i.get("key"),
                        "summary": self._extract_field(i, "summary"),
                        "type": self._extract_field(i, "issuetype"),
                        "status": self._extract_field(i, "status"),
                        "created": i.get("fields", {}).get("created"),
                    }
                    for i in change_issues[:30]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Jira connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Jira sync (last_run=%s)", since or "never")

                bundles = self.fetch(since)
                all_items: list[EvidenceItem] = []
                for bundle in bundles:
                    all_items.extend(self._transform_bundle(bundle))

                logger.info("Transformed %d evidence items", len(all_items))

                if all_items:
                    accepted, skipped, errors = self._post_all(all_items)
                    logger.info("Ingest: accepted=%d skipped=%d errors=%d", accepted, skipped, errors)

                self._save_state({"last_run": datetime.now(timezone.utc).isoformat()})

            except Exception as e:
                logger.error("Sync failed: %s", e, exc_info=True)

            elapsed = time.monotonic() - start
            sleep_for = max(0, self.poll_interval - elapsed)
            logger.info("Next sync in %.0fs", sleep_for)
            self._sleep_with_sync_check(sleep_for)


if __name__ == "__main__":
    JiraConnector().run()
