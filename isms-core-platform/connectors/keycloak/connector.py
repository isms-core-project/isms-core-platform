"""Keycloak connector for ISMS CORE v2.0.

Pulls from the Keycloak Admin REST API and posts evidence to:
  a.5.15-16-18 — Identity and Access Management  (user inventory + MFA status)
  a.8.2-3-5    — Privileged Access and Auth       (SSO clients)
  a.5.3        — Segregation of Duties            (recent login failure count)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  KEYCLOAK_URL          — e.g. https://sso.example.com
  KEYCLOAK_USERNAME     — admin username
  KEYCLOAK_PASSWORD     — admin password
  KEYCLOAK_REALM        — realm to query (default: master)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)
"""

import logging
import sys

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from keycloak_client import KeycloakClient

logger = logging.getLogger(__name__)


class KeycloakConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = KeycloakClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all Keycloak data each run."""
        users = self.client.get_users()
        groups = self.client.get_groups()
        clients = self.client.get_clients()
        sessions = self.client.get_sessions()
        login_failures = self.client.get_events(type="LOGIN_ERROR", max=100)

        return [
            {
                "_type": "keycloak_bundle",
                "users": users,
                "groups": groups,
                "clients": clients,
                "sessions": sessions,
                "login_failures": login_failures,
                "realm": self.client.realm,
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        users = bundle["users"]
        clients = bundle["clients"]
        login_failures = bundle["login_failures"]
        realm = bundle["realm"]

        # ── A.5.15-16-18 — User inventory + MFA (totp) ───────────────────────
        enabled_users = [u for u in users if u.get("enabled")]
        mfa_users = [u for u in users if u.get("totp")]

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"Keycloak user inventory (realm={realm}): {len(users)} accounts, "
                f"{len(enabled_users)} enabled, {len(mfa_users)} with TOTP MFA"
            ),
            source_ref="keycloak-user-inventory",
            classification="user",
            status="active",
            raw={
                "realm": realm,
                "total_users": len(users),
                "enabled_count": len(enabled_users),
                "mfa_totp_count": len(mfa_users),
                "pct_mfa": round(len(mfa_users) / len(users) * 100, 1) if users else 0,
                "users": [
                    {
                        "id": u.get("id"),
                        "username": u.get("username"),
                        "email": u.get("email"),
                        "enabled": u.get("enabled"),
                        "email_verified": u.get("emailVerified"),
                        "totp": u.get("totp"),
                        "created_timestamp": u.get("createdTimestamp"),
                    }
                    for u in users
                ],
            },
        ))

        # ── A.8.2-3-5 — SSO client inventory ─────────────────────────────────
        public_clients = [c for c in clients if c.get("publicClient")]
        confidential_clients = [c for c in clients if not c.get("publicClient") and not c.get("bearerOnly")]
        enabled_clients = [c for c in clients if c.get("enabled")]

        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"Keycloak SSO client inventory (realm={realm}): "
                f"{len(clients)} clients ({len(enabled_clients)} enabled, "
                f"{len(confidential_clients)} confidential, {len(public_clients)} public)"
            ),
            source_ref="keycloak-client-inventory",
            classification="asset",
            status="active",
            raw={
                "realm": realm,
                "total_clients": len(clients),
                "enabled_count": len(enabled_clients),
                "confidential_count": len(confidential_clients),
                "public_count": len(public_clients),
                "clients": [
                    {
                        "id": c.get("id"),
                        "client_id": c.get("clientId"),
                        "name": c.get("name"),
                        "enabled": c.get("enabled"),
                        "public_client": c.get("publicClient"),
                        "bearer_only": c.get("bearerOnly"),
                        "standard_flow_enabled": c.get("standardFlowEnabled"),
                    }
                    for c in clients
                ],
            },
        ))

        # ── A.5.3 — Login failures (segregation of duties evidence) ──────────
        # Recent login failures indicate account probing or misconfigured access
        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"Keycloak login failures (realm={realm}): "
                f"{len(login_failures)} LOGIN_ERROR events (last 100)"
            ),
            source_ref="keycloak-login-failures",
            classification="incident",
            status="active",
            raw={
                "realm": realm,
                "login_failure_count": len(login_failures),
                "recent_failures": [
                    {
                        "time": e.get("time"),
                        "type": e.get("type"),
                        "ip_address": e.get("ipAddress"),
                        "client_id": e.get("clientId"),
                        "user_id": e.get("userId"),
                        "details": e.get("details", {}),
                    }
                    for e in login_failures[:30]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("Keycloak connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Keycloak sync (last_run=%s)", since or "never")

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
    KeycloakConnector().run()
