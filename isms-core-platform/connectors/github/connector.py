"""GitHub Advanced Security connector for ISMS CORE v2.0.

Pulls from the GitHub REST API and posts evidence to:
  a.8.25-26-29 — Secure Development Framework  (secret scanning, Dependabot SCA)
  a.8.28       — Secure Coding                  (code scanning / SAST alerts)
  a.5.3        — Segregation of Duties          (org membership + 2FA enforcement)

Supports GitHub.com and GitHub Enterprise Server.

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  GITHUB_TOKEN          — Personal Access Token (scopes: read:org, security_events)
  GITHUB_ORG            — GitHub organisation slug
  GITHUB_URL            — GitHub Enterprise base URL (optional; omit for GitHub.com)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)
"""

import logging
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from github_client import GitHubClient

logger = logging.getLogger(__name__)


class GitHubConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = GitHubClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all GitHub security data each run."""
        repos = self.client.get_repos()
        secret_alerts = self.client.get_secret_scanning_alerts()
        code_alerts = self.client.get_code_scanning_alerts()
        dependabot_alerts = self.client.get_dependabot_alerts()
        members = self.client.get_org_members()
        org_settings = self.client.get_org_settings()

        return [
            {
                "_type": "github_bundle",
                "repos": repos,
                "secret_alerts": secret_alerts,
                "code_alerts": code_alerts,
                "dependabot_alerts": dependabot_alerts,
                "members": members,
                "org_settings": org_settings,
                "org": self.client.org,
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
        repos = bundle["repos"]
        secret_alerts = bundle["secret_alerts"]
        code_alerts = bundle["code_alerts"]
        dependabot_alerts = bundle["dependabot_alerts"]
        members = bundle["members"]
        org_settings = bundle["org_settings"]
        org = bundle["org"]

        # ── A.8.25-26-29 — Secret scanning alerts ────────────────────────────
        secret_by_type: dict[str, int] = Counter(
            a.get("secret_type_display_name") or a.get("secret_type", "unknown")
            for a in secret_alerts
        )
        items.append(EvidenceItem(
            group_code="a.8.25-26-29",
            title=(
                f"GitHub secret scanning (org={org}): "
                f"{len(secret_alerts)} open alerts across {len(repos)} repos"
            ),
            source_ref="github-secret-scanning",
            classification="vulnerability",
            status="attention-required" if secret_alerts else "compliant",
            event_date=fetched_at,
            raw={
                "org": org,
                "open_alert_count": len(secret_alerts),
                "by_type": dict(secret_by_type),
                "repo_count": len(repos),
                "alerts": [
                    {
                        "number": a.get("number"),
                        "state": a.get("state"),
                        "secret_type": a.get("secret_type"),
                        "secret_type_display_name": a.get("secret_type_display_name"),
                        "repository": (a.get("repository") or {}).get("full_name"),
                        "created_at": a.get("created_at"),
                    }
                    for a in secret_alerts[:50]
                ],
            },
        ))

        # ── A.8.28 — Code scanning (SAST) alerts ─────────────────────────────
        code_by_severity: dict[str, int] = Counter(
            (a.get("rule") or {}).get("severity", "unknown")
            for a in code_alerts
        )
        critical_sast = sum(
            1 for a in code_alerts
            if (a.get("rule") or {}).get("severity") in ("critical", "high", "error")
        )
        items.append(EvidenceItem(
            group_code="a.8.28",
            title=(
                f"GitHub code scanning / SAST (org={org}): "
                f"{len(code_alerts)} open alerts ({critical_sast} critical/high)"
            ),
            source_ref="github-code-scanning",
            classification="vulnerability",
            status="attention-required" if critical_sast > 0 else "compliant",
            event_date=fetched_at,
            raw={
                "org": org,
                "open_alert_count": len(code_alerts),
                "critical_high_count": critical_sast,
                "by_severity": dict(code_by_severity),
                "alerts": [
                    {
                        "number": a.get("number"),
                        "state": a.get("state"),
                        "rule_id": (a.get("rule") or {}).get("id"),
                        "rule_severity": (a.get("rule") or {}).get("severity"),
                        "tool": (a.get("tool") or {}).get("name"),
                        "repository": (a.get("repository") or {}).get("full_name"),
                        "created_at": a.get("created_at"),
                    }
                    for a in code_alerts[:50]
                ],
            },
        ))

        # ── A.8.25-26-29 — Dependabot / SCA alerts ───────────────────────────
        dep_by_severity: dict[str, int] = Counter(
            (a.get("security_advisory") or {}).get("severity", "unknown")
            for a in dependabot_alerts
        )
        critical_dep = sum(
            1 for a in dependabot_alerts
            if (a.get("security_advisory") or {}).get("severity") in ("critical", "high")
        )
        items.append(EvidenceItem(
            group_code="a.8.25-26-29",
            title=(
                f"GitHub Dependabot / SCA (org={org}): "
                f"{len(dependabot_alerts)} open alerts ({critical_dep} critical/high)"
            ),
            source_ref="github-dependabot",
            classification="vulnerability",
            status="attention-required" if critical_dep > 0 else "compliant",
            event_date=fetched_at,
            raw={
                "org": org,
                "open_alert_count": len(dependabot_alerts),
                "critical_high_count": critical_dep,
                "by_severity": dict(dep_by_severity),
                "alerts": [
                    {
                        "number": a.get("number"),
                        "state": a.get("state"),
                        "severity": (a.get("security_advisory") or {}).get("severity"),
                        "cve_id": (a.get("security_advisory") or {}).get("cve_id"),
                        "package": ((a.get("dependency") or {}).get("package") or {}).get("name"),
                        "repository": (a.get("repository") or {}).get("full_name"),
                        "created_at": a.get("created_at"),
                    }
                    for a in dependabot_alerts[:50]
                ],
            },
        ))

        # ── A.5.3 — Org members + 2FA enforcement ────────────────────────────
        two_fa_required = org_settings.get("two_factor_requirement_enabled", False)
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"GitHub org members (org={org}): "
                f"{len(members)} members, "
                f"2FA enforcement={'enabled' if two_fa_required else 'DISABLED'}"
            ),
            source_ref="github-org-members",
            classification="user",
            status="compliant" if two_fa_required else "attention-required",
            event_date=fetched_at,
            raw={
                "org": org,
                "member_count": len(members),
                "two_factor_required": two_fa_required,
                "org_plan": (org_settings.get("plan") or {}).get("name"),
                "members": [
                    {
                        "login": m.get("login"),
                        "id": m.get("id"),
                        "type": m.get("type"),
                        "site_admin": m.get("site_admin"),
                    }
                    for m in members[:100]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("GitHub connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting GitHub sync (org=%s, last_run=%s)", self.client.org, since or "never")

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
    GitHubConnector().run()