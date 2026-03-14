"""Windows Active Directory connector for ISMS CORE v2.0.

Queries Active Directory via LDAP/LDAPS and posts evidence to:
  a.5.3   — Segregation of duties  (user account roster)
  a.5.15  — Access control         (security group inventory)
  a.5.18  — Access rights          (privileged group memberships)
  a.8.2   — Privileged access mgmt (password policy compliance)

Environment variables required:
  ISMS_API_URL    — e.g. http://10.0.0.110:8000
  ISMS_API_TOKEN  — connector bearer token from /admin/connectors/register
  AD_SERVER       — LDAP server hostname or IP (e.g. dc01.corp.local)
  AD_PORT         — 389 (LDAP) or 636 (LDAPS). Default: 389
  AD_USE_SSL      — "true" for LDAPS. Default: false
  AD_BIND_DN      — Service account DN (e.g. CN=svc_isms,CN=Users,DC=corp,DC=local)
  AD_BIND_PASS    — Service account password
  AD_BASE_DN      — Search base DN (e.g. DC=corp,DC=local)
  POLL_INTERVAL   — seconds between syncs (default: 86400 = 24h)
  BATCH_SIZE      — items per API call (default: 100)

Minimum AD permissions for the bind account:
  - Read access to Users, Groups, Computers containers
  - Read access to domain root object (password policy)
  - No write access required (read-only connector)
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from ldap_client import LDAPClient

logger = logging.getLogger(__name__)


class ActiveDirectoryConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.ldap = LDAPClient(**cfg)

    # ── fetch — pulls all data from AD (full sync each run) ──────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — LDAP has no reliable delta without tombstone queries."""
        users = self.ldap.get_users()
        groups = self.ldap.get_groups()
        priv_memberships = self.ldap.get_privileged_group_members(groups)
        password_policy = self.ldap.get_password_policy()

        return [
            {
                "_type": "ad_bundle",
                "users": users,
                "groups": groups,
                "privileged_memberships": priv_memberships,
                "password_policy": password_policy,
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        users = bundle["users"]
        groups = bundle["groups"]
        priv_memberships = bundle["privileged_memberships"]
        password_policy = bundle["password_policy"]

        # ── A.5.3 — User roster (segregation of duties evidence) ─────────────
        enabled_count = sum(1 for u in users if u.get("account_enabled"))
        disabled_count = len(users) - enabled_count

        # Stale accounts: enabled but no logon in 90+ days
        from datetime import timedelta
        cutoff = (datetime.now(timezone.utc) - timedelta(days=90)).isoformat()
        stale = [
            u for u in users
            if u.get("account_enabled")
            and u.get("last_logon")
            and u["last_logon"] < cutoff
        ]
        no_logon = [u for u in users if u.get("account_enabled") and not u.get("last_logon")]

        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"AD user roster: {len(users)} accounts "
                f"({enabled_count} enabled, {disabled_count} disabled, "
                f"{len(stale)} stale >90d, {len(no_logon)} never logged in)"
            ),
            source_ref="ad-user-roster",
            classification="user",
            status="active",
            raw={
                "total_users": len(users),
                "enabled": enabled_count,
                "disabled": disabled_count,
                "stale_90d": len(stale),
                "never_logged_in": len(no_logon),
                "users": [
                    {
                        "sam": u["sam"],
                        "display_name": u["display_name"],
                        "department": u["department"],
                        "title": u["title"],
                        "account_enabled": u["account_enabled"],
                        "last_logon": u["last_logon"],
                        "pwd_last_set": u["pwd_last_set"],
                        "created": u["created"],
                    }
                    for u in users
                ],
            },
        ))

        # ── A.5.15 — Security group inventory (access control evidence) ───────
        security_groups = [g for g in groups if g.get("is_security")]
        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"AD group inventory: {len(groups)} total "
                f"({len(security_groups)} security groups)"
            ),
            source_ref="ad-group-inventory",
            classification="asset",
            status="active",
            raw={
                "total_groups": len(groups),
                "security_groups": len(security_groups),
                "groups": [
                    {
                        "name": g["name"],
                        "description": g["description"],
                        "is_security": g["is_security"],
                        "member_count": g["member_count"],
                        "is_privileged": g["is_privileged"],
                    }
                    for g in groups
                ],
            },
        ))

        # ── A.5.18 — Privileged group memberships (access rights evidence) ────
        if priv_memberships:
            high_priv_count = sum(1 for m in priv_memberships if m["is_high_privilege"])
            unique_members = len({m["member_dn"] for m in priv_memberships})
            items.append(EvidenceItem(
                group_code="a.5.15-16-18",
                title=(
                    f"AD privileged group memberships: {len(priv_memberships)} assignments "
                    f"({unique_members} unique principals, {high_priv_count} high-privilege)"
                ),
                source_ref="ad-privileged-memberships",
                classification="user",
                status="active",
                raw={
                    "total_assignments": len(priv_memberships),
                    "unique_principals": unique_members,
                    "high_privilege_count": high_priv_count,
                    "assignments": priv_memberships,
                },
            ))
        else:
            logger.info("No privileged group memberships found — check bind account read access")

        # ── A.8.2 — Password policy (privileged access management evidence) ───
        if password_policy:
            min_len = password_policy.get("min_pwd_length") or 0
            max_age = password_policy.get("max_pwd_age_minutes")
            lockout = password_policy.get("lockout_threshold") or 0
            history = password_policy.get("pwd_history_length") or 0

            # Simplified compliance check against common baselines
            issues = []
            if min_len < 12:
                issues.append(f"min password length {min_len} < 12 characters")
            if max_age and max_age > 129600:  # 90 days in minutes
                issues.append(f"max password age {max_age // 1440}d > 90d")
            if lockout == 0:
                issues.append("account lockout disabled (threshold = 0)")
            elif lockout > 10:
                issues.append(f"lockout threshold {lockout} attempts > 10")
            if history < 12:
                issues.append(f"password history {history} < 12 passwords")

            compliance = "compliant" if not issues else "non-compliant"
            items.append(EvidenceItem(
                group_code="a.8.2-3-5",
                title=(
                    f"AD password policy: min_len={min_len} chars, "
                    f"max_age={max_age // 1440 if max_age else 'unlimited'}d, "
                    f"lockout={lockout} attempts — {compliance}"
                ),
                source_ref="ad-password-policy",
                classification="policy",
                status="active",
                raw={
                    **password_policy,
                    "compliance_status": compliance,
                    "compliance_issues": issues,
                },
            ))
        else:
            logger.warning("No password policy retrieved — skipping a.8.2 evidence")

        return items

    # ── Override run() to use bundle pattern ──────────────────────────────────

    def run(self) -> None:
        logger.info("Active Directory connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting full AD sync (last_run=%s)", since or "never")

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
    ActiveDirectoryConnector().run()
