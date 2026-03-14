"""Authentik connector for ISMS CORE v2.0.

Pulls from the Authentik REST API and posts evidence to:
  a.5.15-16-18 — Identity and Access Management  (user inventory + MFA devices)
  a.8.2-3-5    — Privileged Access and Auth       (applications + auth flows)
  a.5.3        — Segregation of Duties            (superuser accounts)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  AUTHENTIK_URL         — e.g. https://auth.example.com
  AUTHENTIK_API_TOKEN   — API token (Admin → System → Tokens → API token)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)
"""

import logging
import sys

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from authentik_client import AuthentikClient

logger = logging.getLogger(__name__)


class AuthentikConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = AuthentikClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all Authentik data each run."""
        users = self.client.get_users()
        groups = self.client.get_groups()
        applications = self.client.get_applications()
        outposts = self.client.get_outposts()
        mfa_devices = self.client.get_mfa_devices()
        flows = self.client.get_flows()

        return [
            {
                "_type": "authentik_bundle",
                "users": users,
                "groups": groups,
                "applications": applications,
                "outposts": outposts,
                "mfa_devices": mfa_devices,
                "flows": flows,
                "fetched_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            }
        ]

    # ── transform — bundle pattern (multiple EvidenceItems per run) ───────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        fetched_at = bundle.get("fetched_at")
        users = bundle["users"]
        applications = bundle["applications"]
        mfa_devices = bundle["mfa_devices"]
        flows = bundle["flows"]

        # ── A.5.15-16-18 — User inventory + MFA ─────────────────────────────
        active_users = [u for u in users if u.get("is_active")]
        inactive_users = [u for u in users if not u.get("is_active")]
        mfa_count = len(mfa_devices)

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"Authentik user inventory: {len(users)} accounts "
                f"({len(active_users)} active, {len(inactive_users)} inactive), "
                f"{mfa_count} MFA devices registered"
            ),
            source_ref="authentik-user-inventory",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "total_users": len(users),
                "active_users": len(active_users),
                "inactive_users": len(inactive_users),
                "mfa_device_count": mfa_count,
                "users": [
                    {
                        "pk": u.get("pk"),
                        "username": u.get("username"),
                        "name": u.get("name"),
                        "email": u.get("email"),
                        "is_active": u.get("is_active"),
                        "is_superuser": u.get("is_superuser"),
                        "last_login": u.get("last_login"),
                        "groups": [g.get("name") for g in (u.get("groups_obj") or [])],
                    }
                    for u in users
                ],
            },
        ))

        # ── A.8.2-3-5 — Applications + auth flows ────────────────────────────
        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"Authentik auth configuration: {len(applications)} SSO applications, "
                f"{len(flows)} authentication flows"
            ),
            source_ref="authentik-auth-config",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "application_count": len(applications),
                "auth_flow_count": len(flows),
                "applications": [
                    {
                        "slug": a.get("slug"),
                        "name": a.get("name"),
                        "provider": a.get("provider"),
                        "meta_launch_url": a.get("meta_launch_url"),
                    }
                    for a in applications
                ],
                "flows": [
                    {
                        "slug": f.get("slug"),
                        "name": f.get("name"),
                        "designation": f.get("designation"),
                    }
                    for f in flows
                ],
            },
        ))

        # ── A.5.3 — Superuser accounts (segregation of duties) ───────────────
        superusers = [u for u in users if u.get("is_superuser")]
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"Authentik superuser accounts: {len(superusers)} superusers "
                f"out of {len(users)} total accounts"
            ),
            source_ref="authentik-superuser-accounts",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "superuser_count": len(superusers),
                "total_users": len(users),
                "superusers": [
                    {
                        "pk": u.get("pk"),
                        "username": u.get("username"),
                        "name": u.get("name"),
                        "email": u.get("email"),
                        "last_login": u.get("last_login"),
                    }
                    for u in superusers
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("Authentik connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Authentik sync (last_run=%s)", since or "never")

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
    AuthentikConnector().run()