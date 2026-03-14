"""GitLab connector for ISMS CORE v2.0.

Pulls from the GitLab REST API and posts evidence to:
  a.8.28       — Secure Coding                  (vulnerability findings / SAST)
  a.8.25-26-29 — Secure Development Framework   (project security scanning coverage)
  a.5.3        — Segregation of Duties          (member access level distribution)

Supports GitLab.com and self-managed instances.

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  GITLAB_URL            — e.g. https://gitlab.com or https://gitlab.example.com
  GITLAB_TOKEN          — Personal Access Token or OAuth token
  GITLAB_GROUP_ID       — Group ID to scope queries (recommended)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

API permissions required:
  GitLab Personal Access Token (PAT) scopes required:
  - read_api — all API reads
  - read_user — member list
  For security findings (Ultimate tier required):
  - security_dashboard — vulnerability findings
  - audit_events — audit log access (admin or Auditor role)
"""

import logging
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from gitlab_client import GitLabClient

logger = logging.getLogger(__name__)


class GitLabConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = GitLabClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all GitLab security data each run."""
        projects = self.client.get_projects()
        vulnerabilities = self.client.get_vulnerabilities()
        security_policies = self.client.get_security_policies()
        members = self.client.get_group_members()

        return [
            {
                "_type": "gitlab_bundle",
                "projects": projects,
                "vulnerabilities": vulnerabilities,
                "security_policies": security_policies,
                "members": members,
                "group_id": self.client.group_id,
                "fetched_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        fetched_at = bundle.get("fetched_at")
        projects = bundle["projects"]
        vulnerabilities = bundle["vulnerabilities"]
        security_policies = bundle["security_policies"]
        members = bundle["members"]
        group_id = bundle["group_id"] or "all"

        # ── A.8.28 — Vulnerability findings ──────────────────────────────────
        vuln_by_severity: dict[str, int] = Counter(
            v.get("severity", "unknown").lower()
            for v in vulnerabilities
        )
        critical_vulns = sum(
            1 for v in vulnerabilities
            if v.get("severity", "").lower() in ("critical", "high")
        )
        items.append(EvidenceItem(
            group_code="a.8.28",
            title=(
                f"GitLab vulnerability findings (group={group_id}): "
                f"{len(vulnerabilities)} detected ({critical_vulns} critical/high)"
            ),
            source_ref="gitlab-vulnerabilities",
            classification="vulnerability",
            status="attention-required" if critical_vulns > 0 else "compliant",
            event_date=fetched_at,
            raw={
                "group_id": group_id,
                "total_count": len(vulnerabilities),
                "critical_high_count": critical_vulns,
                "by_severity": dict(vuln_by_severity),
                "findings": [
                    {
                        "id": v.get("id"),
                        "name": v.get("name"),
                        "severity": v.get("severity"),
                        "state": v.get("state"),
                        "scanner": (v.get("scanner") or {}).get("name"),
                        "project": (v.get("project") or {}).get("full_path"),
                        "detected_at": v.get("detected_at"),
                    }
                    for v in vulnerabilities[:50]
                ],
            },
        ))

        # ── A.8.25-26-29 — Project security coverage ─────────────────────────
        # Check which projects have security scanning attributes set
        archived_count = sum(1 for p in projects if p.get("archived"))
        active_projects = [p for p in projects if not p.get("archived")]

        items.append(EvidenceItem(
            group_code="a.8.25-26-29",
            title=(
                f"GitLab project inventory (group={group_id}): "
                f"{len(projects)} projects ({len(active_projects)} active, "
                f"{len(security_policies)} security policies)"
            ),
            source_ref="gitlab-projects",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "group_id": group_id,
                "total_project_count": len(projects),
                "active_project_count": len(active_projects),
                "archived_count": archived_count,
                "security_policy_count": len(security_policies),
                "projects": [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "path_with_namespace": p.get("path_with_namespace"),
                        "visibility": p.get("visibility"),
                        "archived": p.get("archived"),
                        "default_branch": p.get("default_branch"),
                    }
                    for p in projects[:50]
                ],
                "security_policies": [
                    {
                        "name": sp.get("name"),
                        "type": sp.get("type"),
                        "enabled": sp.get("enabled"),
                    }
                    for sp in security_policies
                ],
            },
        ))

        # ── A.5.3 — Member access level distribution ──────────────────────────
        access_by_level: dict[str, int] = Counter(
            GitLabClient.access_level_name(m.get("access_level", 0))
            for m in members
        )
        owner_count = access_by_level.get("owner", 0)
        maintainer_count = access_by_level.get("maintainer", 0)
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"GitLab group access levels (group={group_id}): "
                f"{len(members)} members — "
                f"{owner_count} owners, {maintainer_count} maintainers"
            ),
            source_ref="gitlab-access-levels",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "group_id": group_id,
                "total_members": len(members),
                "by_access_level": dict(access_by_level),
                "members": [
                    {
                        "id": m.get("id"),
                        "username": m.get("username"),
                        "name": m.get("name"),
                        "access_level": m.get("access_level"),
                        "access_level_name": GitLabClient.access_level_name(m.get("access_level", 0)),
                        "expires_at": m.get("expires_at"),
                    }
                    for m in members
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("GitLab connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting GitLab sync (group_id=%s, last_run=%s)",
                            self.client.group_id or "all", since or "never")

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
    GitLabConnector().run()