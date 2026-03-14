"""Devolutions Server (DVLS) connector for ISMS CORE v2.0.

Pulls from the Devolutions Server REST API and posts evidence to:
  a.8.2-3-5    — Privileged Access and Auth    (stored credentials / connection inventory)
  a.5.15-16-18 — Identity and Access Management (user accounts, groups, roles)
  a.5.3        — Segregation of Duties          (admin/operator user breakdown)
  a.8.15       — Logging                        (session/activity log summary)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  DVLS_URL              — e.g. https://10.0.0.71:5000 (default for local K8s deployment)
  DVLS_APP_KEY          — Application User Key (preferred — create in DVLS > Administration > Application Users)
  DVLS_APP_SECRET       — Application User Secret
    OR
  DVLS_USERNAME         — Admin username (fallback — use only if Application User not available)
  DVLS_PASSWORD         — Admin password
  DVLS_VERIFY_SSL       — true/false (default: false — DVLS typically uses self-signed certs)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

API permissions required (Application User):
  - Users: Read
  - Groups: Read
  - Connections: Read
  - Logs: Read (Activity Logs)
  - Sessions: Read (Gateway Sessions)

Local K8s deployment:
  DVLS_URL = https://10.0.0.71:5000 (MetalLB fixed IP, namespace: dvls-beta)
  Admin credentials stored in K8s secret: dvls-admin-secret (namespace: dvls-beta)
"""

import logging
import os
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from dvls_client import DVLSClient

logger = logging.getLogger(__name__)

# Connection types that indicate privileged/sensitive credentials
PRIVILEGED_CONNECTION_TYPES = {
    "RDPConfigured",
    "SSHShell",
    "SSHKeyEntry",
    "PasswordEntry",
    "PrivilegedAccount",
    "PAMAccount",
    "DatabaseConnection",
    "Credential",
}

# User roles that indicate administrator-level access
ADMIN_ROLES = {"AdministratorDVLS", "Administrator", "Operator", "PAMAdmin"}


class DevolutionsConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = DVLSClient(
            base_url=cfg.get("dvls_url", os.environ.get("DVLS_URL", "https://10.0.0.71:5000")),
            app_key=cfg.get("app_key", os.environ.get("DVLS_APP_KEY", "")),
            app_secret=cfg.get("app_secret", os.environ.get("DVLS_APP_SECRET", "")),
            username=cfg.get("username", os.environ.get("DVLS_USERNAME", "")),
            password=cfg.get("password", os.environ.get("DVLS_PASSWORD", "")),
            verify_ssl=str(cfg.get("verify_ssl", os.environ.get("DVLS_VERIFY_SSL", "false"))).lower() == "true",
        )

    # ── fetch ──────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all DVLS data each run."""
        try:
            self.client.authenticate()
            connections = self.client.get_connections()
            users = self.client.get_users()
            groups = self.client.get_user_groups()
            logs = self.client.get_session_logs(limit=500)
            try:
                active_sessions = self.client.get_active_sessions()
            except Exception as e:
                logger.warning("DVLS: could not fetch active sessions: %s", e)
                active_sessions = []
        finally:
            self.client.logoff()

        return [
            {
                "_type": "dvls_bundle",
                "connections": connections,
                "users": users,
                "groups": groups,
                "logs": logs,
                "active_sessions": active_sessions,
            }
        ]

    # ── transform — bundle pattern ─────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        connections = bundle["connections"]
        users = bundle["users"]
        groups = bundle["groups"]
        logs = bundle["logs"]
        active_sessions = bundle["active_sessions"]

        # ── A.8.2-3-5 — Privileged connection / credential inventory ──────────
        by_type: dict[str, int] = Counter(
            c.get("connectionType") or c.get("type") or "unknown"
            for c in connections
        )
        privileged = [
            c for c in connections
            if (c.get("connectionType") or c.get("type") or "") in PRIVILEGED_CONNECTION_TYPES
        ]

        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"Devolutions Server credential vault: {len(connections)} total connections, "
                f"{len(privileged)} privileged-type entries"
            ),
            source_ref="dvls-connection-inventory",
            classification="asset",
            status="active",
            raw={
                "total_connection_count": len(connections),
                "privileged_count": len(privileged),
                "by_type": dict(by_type),
                "connections": [
                    {
                        "id": c.get("id"),
                        "name": c.get("name") or c.get("Name"),
                        "connection_type": c.get("connectionType") or c.get("type"),
                        "group": c.get("group") or c.get("Group"),
                        "username": c.get("userName") or c.get("username"),
                        "host": c.get("host") or c.get("Host"),
                    }
                    for c in connections[:100]
                ],
            },
        ))

        # ── A.5.15-16-18 — User accounts and group membership ─────────────────
        active_users = [
            u for u in users
            if not (u.get("isDisabled") or u.get("disabled") or u.get("IsDisabled"))
        ]
        mfa_enabled = [
            u for u in users
            if u.get("isTwoFactorEnabled") or u.get("mfaEnabled") or u.get("IsTwoFactorEnabled")
        ]

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"Devolutions Server users: {len(users)} total, "
                f"{len(active_users)} active, "
                f"{len(mfa_enabled)} with MFA enabled"
            ),
            source_ref="dvls-user-directory",
            classification="compliant" if len(mfa_enabled) >= len(active_users) * 0.8 else "warning",
            status="active",
            raw={
                "total_user_count": len(users),
                "active_user_count": len(active_users),
                "disabled_count": len(users) - len(active_users),
                "mfa_enabled_count": len(mfa_enabled),
                "group_count": len(groups),
                "users": [
                    {
                        "id": u.get("id"),
                        "username": u.get("userName") or u.get("username"),
                        "email": u.get("email") or u.get("Email"),
                        "display_name": u.get("displayName") or u.get("name"),
                        "is_disabled": u.get("isDisabled") or u.get("disabled"),
                        "mfa_enabled": u.get("isTwoFactorEnabled") or u.get("mfaEnabled"),
                        "user_type": u.get("userType") or u.get("type"),
                    }
                    for u in users[:100]
                ],
            },
        ))

        # ── A.5.3 — Admin / operator segregation ──────────────────────────────
        admin_users = [
            u for u in users
            if (u.get("role") or u.get("userType") or u.get("Role") or "") in ADMIN_ROLES
        ]
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"Devolutions Server admin users: {len(admin_users)} of {len(users)} "
                f"users have admin/operator role"
            ),
            source_ref="dvls-admin-users",
            classification="compliant" if 0 < len(admin_users) <= max(2, len(users) // 10) else "warning",
            status="active",
            raw={
                "total_user_count": len(users),
                "admin_count": len(admin_users),
                "group_count": len(groups),
                "admin_users": [
                    {
                        "username": u.get("userName") or u.get("username"),
                        "role": u.get("role") or u.get("userType"),
                        "email": u.get("email"),
                    }
                    for u in admin_users[:50]
                ],
                "groups": [
                    {
                        "id": g.get("id"),
                        "name": g.get("name"),
                        "description": g.get("description"),
                        "member_count": g.get("memberCount") or g.get("usersCount"),
                    }
                    for g in groups[:50]
                ],
            },
        ))

        # ── A.8.15 — Activity log / session audit ─────────────────────────────
        log_types: dict[str, int] = Counter(
            l.get("eventType") or l.get("logType") or l.get("type") or "unknown"
            for l in logs
        )
        recent_logs = sorted(
            logs,
            key=lambda l: l.get("logTime") or l.get("createdOn") or l.get("date") or "",
            reverse=True,
        )[:50]

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"Devolutions Server activity log: {len(logs)} recent events, "
                f"{len(active_sessions)} active sessions"
            ),
            source_ref="dvls-activity-log",
            classification="info",
            status="active",
            raw={
                "total_log_count": len(logs),
                "active_session_count": len(active_sessions),
                "event_types": dict(log_types),
                "recent_events": [
                    {
                        "log_time": l.get("logTime") or l.get("createdOn"),
                        "event_type": l.get("eventType") or l.get("logType"),
                        "username": l.get("userName") or l.get("username"),
                        "ip_address": l.get("ipAddress") or l.get("clientIp"),
                        "message": l.get("message") or l.get("description"),
                    }
                    for l in recent_logs
                ],
                "active_sessions": [
                    {
                        "session_id": s.get("id"),
                        "username": s.get("userName") or s.get("username"),
                        "connection_name": s.get("connectionName") or s.get("name"),
                        "started": s.get("startDate") or s.get("openedOn"),
                        "ip_address": s.get("ipAddress"),
                    }
                    for s in active_sessions[:20]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ──────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("Devolutions connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting DVLS sync (url=%s, last_run=%s)",
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
    DevolutionsConnector().run()
