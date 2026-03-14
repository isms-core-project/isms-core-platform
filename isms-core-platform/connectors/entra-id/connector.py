"""Entra ID connector for ISMS CORE v2.0.

Pulls from Microsoft Graph API and posts evidence to:
  a.5.3        — Segregation of duties           (users + role assignments)
  a.5.15-16-18 — Identity and Access Management  (group memberships + role assignments)
  a.8.2-3-5    — Privileged Access and Auth       (MFA registration status)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  ENTRA_TENANT_ID       — Azure AD tenant ID
  ENTRA_CLIENT_ID       — App registration client ID
  ENTRA_CLIENT_SECRET   — App registration client secret
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

Graph API permissions required (Application):
  User.Read.All
  GroupMember.Read.All
  RoleManagement.Read.Directory
  UserAuthenticationMethod.Read.All
"""

import logging
import os
import sys

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from graph_client import GraphClient

logger = logging.getLogger(__name__)

# Privileged role display names to flag as high-privilege
PRIVILEGED_ROLES = {
    "Global Administrator",
    "Privileged Role Administrator",
    "User Administrator",
    "Security Administrator",
    "Exchange Administrator",
    "SharePoint Administrator",
    "Compliance Administrator",
    "Authentication Administrator",
    "Conditional Access Administrator",
}


class EntraIDConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.graph = GraphClient(**cfg)

    # ── fetch — pulls all data from Graph (full sync each run) ───────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Entra ID has no reliable delta for all endpoints we need."""
        users = self.graph.get_users()
        groups = self.graph.get_groups()
        mfa_records = self.graph.get_mfa_registration()
        role_assignments = self.graph.get_privileged_role_assignments()

        # Index MFA by userPrincipalName for O(1) lookup
        mfa_by_upn = {r.get("userPrincipalName", "").lower(): r for r in mfa_records}

        return [
            {
                "_type": "entra_bundle",
                "users": users,
                "groups": groups,
                "mfa_by_upn": mfa_by_upn,
                "role_assignments": role_assignments,
            }
        ]

    # ── transform — one bundle → multiple EvidenceItems ──────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        users = bundle["users"]
        groups = bundle["groups"]
        mfa_by_upn = bundle["mfa_by_upn"]
        role_assignments = bundle["role_assignments"]

        # ── A.5.3 — User list (segregation of duties evidence) ───────────────
        enabled_count = sum(1 for u in users if u.get("accountEnabled"))
        disabled_count = len(users) - enabled_count
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=f"Entra ID user roster: {len(users)} accounts ({enabled_count} enabled, {disabled_count} disabled)",
            source_ref="entra-user-roster",
            classification="user",
            status="active",
            raw={
                "total_users": len(users),
                "enabled": enabled_count,
                "disabled": disabled_count,
                "users": [
                    {
                        "upn": u.get("userPrincipalName"),
                        "display_name": u.get("displayName"),
                        "department": u.get("department"),
                        "job_title": u.get("jobTitle"),
                        "account_enabled": u.get("accountEnabled"),
                    }
                    for u in users
                ],
            },
        ))

        # ── A.5.15-16-18 — Group inventory (access control evidence) ─────────
        security_groups = [g for g in groups if g.get("securityEnabled")]
        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=f"Entra ID groups: {len(groups)} total ({len(security_groups)} security-enabled)",
            source_ref="entra-group-inventory",
            classification="asset",
            status="active",
            raw={
                "total_groups": len(groups),
                "security_groups": len(security_groups),
                "groups": [
                    {
                        "id": g.get("id"),
                        "display_name": g.get("displayName"),
                        "security_enabled": g.get("securityEnabled"),
                        "group_types": g.get("groupTypes", []),
                    }
                    for g in groups
                ],
            },
        ))

        # ── A.5.15-16-18 — Privileged role assignments ────────────────────────
        privileged = []
        for ra in role_assignments:
            role_def = ra.get("roleDefinition", {}) or {}
            role_name = role_def.get("displayName", ra.get("roleDefinitionId", "Unknown"))
            principal = ra.get("principal", {}) or {}
            privileged.append({
                "principal_upn": principal.get("userPrincipalName") or principal.get("displayName"),
                "principal_type": principal.get("@odata.type", "").replace("#microsoft.graph.", ""),
                "role": role_name,
                "is_high_privilege": role_name in PRIVILEGED_ROLES,
                "assignment_id": ra.get("id"),
            })

        high_priv_count = sum(1 for p in privileged if p["is_high_privilege"])
        if privileged:
            items.append(EvidenceItem(
                group_code="a.5.15-16-18",
                title=f"Privileged role assignments: {len(privileged)} ({high_priv_count} high-privilege)",
                source_ref="entra-role-assignments",
                classification="user",
                status="active",
                raw={
                    "total_assignments": len(privileged),
                    "high_privilege_count": high_priv_count,
                    "assignments": privileged,
                },
            ))

        # ── A.8.2-3-5 — MFA registration (Privileged Access and Authentication) ─
        if mfa_by_upn:
            mfa_registered = sum(1 for r in mfa_by_upn.values() if r.get("isMfaRegistered"))
            mfa_capable = sum(1 for r in mfa_by_upn.values() if r.get("isMfaCapable"))
            total = len(mfa_by_upn)
            items.append(EvidenceItem(
                group_code="a.8.2-3-5",
                title=(
                    f"MFA registration: {mfa_registered}/{total} registered "
                    f"({mfa_capable} capable) — "
                    f"{round(mfa_registered / total * 100) if total else 0}%"
                ),
                source_ref="entra-mfa-status",
                classification="user",
                status="active",
                raw={
                    "total_users": total,
                    "mfa_registered": mfa_registered,
                    "mfa_capable": mfa_capable,
                    "pct_registered": round(mfa_registered / total * 100, 1) if total else 0,
                    "users": [
                        {
                            "upn": upn,
                            "mfa_registered": r.get("isMfaRegistered"),
                            "mfa_capable": r.get("isMfaCapable"),
                            "default_method": r.get("defaultMfaMethod"),
                            "methods": r.get("methodsRegistered", []),
                        }
                        for upn, r in mfa_by_upn.items()
                    ],
                },
            ))
        else:
            logger.warning("No MFA data — skipping a.8.5 evidence (check UserAuthenticationMethod.Read.All permission)")

        return items

    # ── Override run() to handle the bundle pattern ───────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("Entra ID connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting full sync (last_run=%s)", since or "never")

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
    EntraIDConnector().run()
