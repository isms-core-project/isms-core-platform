"""FreeIPA connector for ISMS CORE v2.0.

Pulls from the FreeIPA JSON-RPC API and posts evidence to:
  a.5.3        — Segregation of Duties     (user roster, enabled vs disabled)
  a.5.15-16-18 — Identity and Access Mgmt  (group inventory / access control)
  a.8.2-3-5    — Privileged Access and Auth (sudo rules = privileged access grants)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  FREEIPA_URL           — e.g. https://ipa.example.com (no trailing slash)
  FREEIPA_USERNAME      — FreeIPA service account username
  FREEIPA_PASSWORD      — FreeIPA service account password
  POLL_INTERVAL         — seconds between syncs (default: 86400 = 24h)

API permissions required:
  FreeIPA service account minimum permissions:
  - User Read: user_find, user_show
  - Group Read: group_find, group_show
  - Host Read: host_find (for inventory)
  - Sudo Rule Read: sudorule_find
  Create a dedicated service account in FreeIPA admin panel
  (Admin -> Users -> Add User, then User Groups -> ipausers)
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from freeipa_client import FreeIPAClient

logger = logging.getLogger(__name__)


def _attr(obj: dict, key: str) -> str:
    """FreeIPA returns attribute values as lists; extract first element safely."""
    val = obj.get(key)
    if isinstance(val, list):
        return str(val[0]) if val else ""
    return str(val) if val is not None else ""


def _attr_bool(obj: dict, key: str) -> bool:
    """Extract a boolean-ish attribute value."""
    val = obj.get(key)
    if isinstance(val, list):
        val = val[0] if val else False
    if isinstance(val, bool):
        return val
    return str(val).lower() in ("true", "1", "yes")


class FreeIPAConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = FreeIPAClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — FreeIPA API always returns current state."""
        users = self.client.get_users()
        groups = self.client.get_groups()
        hosts = self.client.get_hosts()
        sudo_rules = self.client.get_sudo_rules()
        return [
            {
                "_type": "freeipa_bundle",
                "users": users,
                "groups": groups,
                "hosts": hosts,
                "sudo_rules": sudo_rules,
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
        hosts = bundle["hosts"]
        sudo_rules = bundle["sudo_rules"]
        fetched_at = bundle["fetched_at"]

        # ── A.5.3 — User roster (segregation of duties) ───────────────────────
        # nsAccountLock=True means disabled; krbLoginExpirationTime expired = locked
        disabled_users = [
            u for u in users
            if _attr_bool(u, "nsaccountlock")
        ]
        enabled_users = [u for u in users if not _attr_bool(u, "nsaccountlock")]

        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"FreeIPA user roster: {len(users)} accounts "
                f"({len(enabled_users)} enabled, {len(disabled_users)} disabled/locked)"
            ),
            source_ref="freeipa-user-roster",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_users": len(users),
                "enabled_count": len(enabled_users),
                "disabled_count": len(disabled_users),
                "users": [
                    {
                        "uid": _attr(u, "uid"),
                        "cn": _attr(u, "cn"),
                        "mail": _attr(u, "mail"),
                        "title": _attr(u, "title"),
                        "ou": _attr(u, "ou"),
                        "disabled": _attr_bool(u, "nsaccountlock"),
                        "last_krblogin": _attr(u, "krblastsuccessfulauth"),
                    }
                    for u in users[:100]
                ],
            },
        ))

        # ── A.5.15-16-18 — Group inventory (access control) ──────────────────
        # FreeIPA distinguishes POSIX groups (gidnumber present) from non-POSIX
        posix_groups = [g for g in groups if g.get("gidnumber")]
        non_posix_groups = [g for g in groups if not g.get("gidnumber")]

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"FreeIPA group inventory: {len(groups)} groups "
                f"({len(posix_groups)} POSIX, {len(non_posix_groups)} non-POSIX)"
            ),
            source_ref="freeipa-group-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_groups": len(groups),
                "posix_group_count": len(posix_groups),
                "non_posix_group_count": len(non_posix_groups),
                "groups": [
                    {
                        "cn": _attr(g, "cn"),
                        "description": _attr(g, "description"),
                        "gid": _attr(g, "gidnumber"),
                        "member_count": len(g.get("member_user", []) or []),
                    }
                    for g in groups[:100]
                ],
            },
        ))

        # ── A.8.2-3-5 — Sudo rules (privileged access evidence) ───────────────
        enabled_rules = [r for r in sudo_rules if _attr_bool(r, "ipaenabledflag") is not False]
        # Rules that apply to all hosts or all commands are high-risk
        all_host_rules = [
            r for r in sudo_rules
            if "!" not in _attr(r, "hostcategory") and _attr(r, "hostcategory") == "all"
        ]
        all_cmd_rules = [
            r for r in sudo_rules
            if _attr(r, "cmdcategory") == "all"
        ]

        sudo_status = "compliant"
        if all_host_rules and all_cmd_rules:
            sudo_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"FreeIPA sudo rules: {len(sudo_rules)} total "
                f"({len(enabled_rules)} enabled, "
                f"{len(all_cmd_rules)} grant ALL commands)"
            ),
            source_ref="freeipa-sudo-rules",
            classification="policy",
            status=sudo_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_sudo_rules": len(sudo_rules),
                "enabled_count": len(enabled_rules),
                "all_hosts_count": len(all_host_rules),
                "all_commands_count": len(all_cmd_rules),
                "enrolled_host_count": len(hosts),
                "sudo_rules": [
                    {
                        "cn": _attr(r, "cn"),
                        "description": _attr(r, "description"),
                        "host_category": _attr(r, "hostcategory"),
                        "cmd_category": _attr(r, "cmdcategory"),
                        "enabled": not _attr_bool(r, "ipaenabledflag") is False,
                    }
                    for r in sudo_rules
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("FreeIPA connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting FreeIPA sync (url=%s, last_run=%s)",
                            self.client.base_url, since or "never")

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
    FreeIPAConnector().run()
