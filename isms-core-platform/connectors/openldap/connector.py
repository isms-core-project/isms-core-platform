"""OpenLDAP connector for ISMS CORE v2.0.

Pulls from an OpenLDAP directory and posts evidence to:
  a.5.3        — Segregation of Duties     (user account roster)
  a.5.15-16-18 — Identity and Access Mgmt  (group inventory / access control)
  a.8.9        — Network device inventory  (computer objects, if present)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  OPENLDAP_SERVER       — LDAP server hostname or IP
  OPENLDAP_PORT         — 389 (LDAP) or 636 (LDAPS). Default: 389
  OPENLDAP_USE_SSL      — "true" for LDAPS. Default: false
  OPENLDAP_BIND_DN      — Bind DN (e.g. cn=svc_isms,dc=example,dc=com)
  OPENLDAP_BIND_PASS    — Bind account password
  OPENLDAP_BASE_DN      — Search base DN (e.g. dc=example,dc=com)
  POLL_INTERVAL         — seconds between syncs (default: 86400 = 24h)

API permissions required:
  LDAP bind account minimum permissions:
  - Read access to the user subtree (inetOrgPerson, person)
  - Read access to the group subtree (groupOfNames, posixGroup)
  - Read access to computer objects (optional)
  - Anonymous bind NOT recommended — use a dedicated service account
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from openldap_client import OpenLDAPClient

logger = logging.getLogger(__name__)


class OpenLDAPConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = OpenLDAPClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — LDAP has no reliable delta; always pull current state."""
        users = self.client.get_users()
        groups = self.client.get_groups()
        computers = self.client.get_computers()
        return [
            {
                "_type": "openldap_bundle",
                "users": users,
                "groups": groups,
                "computers": computers,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        users = bundle["users"]
        groups = bundle["groups"]
        computers = bundle["computers"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.3 — User roster (segregation of duties) ───────────────────────
        # OpenLDAP inetOrgPerson has no enabled/disabled flag by default.
        # Use presence of userPassword as a proxy for active local accounts.
        with_password = [u for u in users if u.get("has_password")]
        without_password = [u for u in users if not u.get("has_password")]

        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"OpenLDAP user roster: {len(users)} person entries "
                f"({len(with_password)} with local password, "
                f"{len(without_password)} without)"
            ),
            source_ref="openldap-user-roster",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_users": len(users),
                "with_local_password": len(with_password),
                "without_local_password": len(without_password),
                "users": [
                    {
                        "uid": u.get("uid"),
                        "cn": u.get("cn"),
                        "sn": u.get("sn"),
                        "mail": u.get("mail"),
                        "ou": u.get("ou"),
                        "has_password": u.get("has_password"),
                    }
                    for u in users[:100]
                ],
            },
        ))

        # ── A.5.15-16-18 — Group inventory (access control) ──────────────────
        # Derive rough size distribution
        large_groups = [g for g in groups if g.get("member_count", 0) > 50]
        empty_groups = [g for g in groups if g.get("member_count", 0) == 0]

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"OpenLDAP group inventory: {len(groups)} groups "
                f"({len(large_groups)} large >50 members, "
                f"{len(empty_groups)} empty)"
            ),
            source_ref="openldap-group-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_groups": len(groups),
                "large_groups_count": len(large_groups),
                "empty_groups_count": len(empty_groups),
                "groups": [
                    {
                        "cn": g.get("cn"),
                        "description": g.get("description"),
                        "member_count": g.get("member_count"),
                    }
                    for g in groups[:100]
                ],
            },
        ))

        # ── A.8.9 — Network device / computer inventory ───────────────────────
        # Only emit this item if computer objects were found; many OpenLDAP
        # deployments do not use objectClass=computer.
        if computers:
            by_os: dict[str, int] = Counter(
                c.get("os") or "unknown" for c in computers
            )
            items.append(EvidenceItem(
                group_code="a.8.9",
                title=(
                    f"OpenLDAP computer objects: {len(computers)} entries "
                    f"({len(by_os)} distinct OS types)"
                ),
                source_ref="openldap-computers",
                classification="asset",
                status="active",
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "total_computers": len(computers),
                    "by_os": dict(by_os),
                    "computers": [
                        {
                            "cn": c.get("cn"),
                            "description": c.get("description"),
                            "os": c.get("os"),
                            "os_version": c.get("os_version"),
                        }
                        for c in computers[:100]
                    ],
                },
            ))
        else:
            logger.info("No computer objects present — skipping a.8.9 evidence item")

        return items

    def run(self) -> None:
        logger.info("OpenLDAP connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting OpenLDAP sync (last_run=%s)", since or "never")

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
    OpenLDAPConnector().run()
