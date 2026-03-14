"""CyberArk PAS connector for ISMS CORE v2.0.

Pulls from the CyberArk PVWA REST API and posts evidence to:
  a.8.2-3-5    — Privileged Access and Auth       (privileged account inventory)
  a.5.15-16-18 — Identity and Access Management   (safe + account status breakdown)
  a.5.3        — Segregation of Duties            (CyberArk admin user count)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  CYBERARK_URL          — e.g. https://pvwa.example.com (no /PasswordVault suffix)
  CYBERARK_USERNAME     — PVWA username
  CYBERARK_PASSWORD     — PVWA password
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

API permissions required:
  CyberArk PVWA permissions for the service account:
  - Safes: List Safes, View Safe Details
  - Accounts: List Accounts, View Account Details
  - Users: List Users
"""

import logging
import sys
from collections import Counter

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from cyberark_client import CyberArkClient

logger = logging.getLogger(__name__)

# User types that indicate administrator-level access in CyberArk
ADMIN_USER_TYPES = {"EPVUser", "BasicUser", "CPM", "PSM"}  # CPM/PSM are privileged service accounts


class CyberArkConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = CyberArkClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all CyberArk data each run."""
        try:
            self.client.logon()
            safes = self.client.get_safes()
            accounts = self.client.get_accounts()
            users = self.client.get_users()
        finally:
            self.client.logoff()

        return [
            {
                "_type": "cyberark_bundle",
                "safes": safes,
                "accounts": accounts,
                "users": users,
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
        safes = bundle["safes"]
        accounts = bundle["accounts"]
        users = bundle["users"]

        # ── A.8.2-3-5 — Privileged account inventory ─────────────────────────
        by_platform: dict[str, int] = Counter(
            a.get("platformId") or a.get("PlatformID") or "unknown"
            for a in accounts
        )
        by_safe: dict[str, int] = Counter(
            a.get("safeName") or a.get("SafeName") or "unknown"
            for a in accounts
        )
        # Status field varies by PVWA version: 'secretVersions', 'status', etc.
        active_accounts = [
            a for a in accounts
            if str(a.get("status") or a.get("Status") or "active").lower() in ("active", "")
        ]

        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"CyberArk privileged accounts: {len(accounts)} total "
                f"across {len(set(by_safe.keys()))} safes, "
                f"{len(set(by_platform.keys()))} platforms"
            ),
            source_ref="cyberark-privileged-accounts",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "total_account_count": len(accounts),
                "active_account_count": len(active_accounts),
                "by_platform": dict(by_platform),
                "by_safe": dict(by_safe),
                "accounts": [
                    {
                        "id": a.get("id"),
                        "username": a.get("userName") or a.get("UserName"),
                        "address": a.get("address") or a.get("Address"),
                        "platform_id": a.get("platformId") or a.get("PlatformID"),
                        "safe_name": a.get("safeName") or a.get("SafeName"),
                        "status": a.get("status") or a.get("Status"),
                    }
                    for a in accounts[:100]
                ],
            },
        ))

        # ── A.5.15-16-18 — Vault (safe) and account status inventory ─────────
        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"CyberArk vault inventory: {len(safes)} safes, "
                f"{len(accounts)} privileged accounts"
            ),
            source_ref="cyberark-vault-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "safe_count": len(safes),
                "account_count": len(accounts),
                "safes": [
                    {
                        "safe_name": s.get("SafeName") or s.get("safeName"),
                        "description": s.get("Description") or s.get("description"),
                        "location": s.get("Location") or s.get("location"),
                        "number_of_days_retention": s.get("NumberOfDaysRetention"),
                        "number_of_versions_retention": s.get("NumberOfVersionsRetention"),
                    }
                    for s in safes[:100]
                ],
            },
        ))

        # ── A.5.3 — CyberArk admin users (segregation of duties) ─────────────
        # userType field identifies admin/service accounts in CyberArk
        admin_users = [
            u for u in users
            if (u.get("userType") or u.get("UserType") or "EPVUser") in ADMIN_USER_TYPES
        ]
        suspended_users = [
            u for u in users
            if u.get("suspended") or u.get("Suspended")
        ]

        items.append(EvidenceItem(
            group_code="a.5.3",
            title=(
                f"CyberArk admin users: {len(users)} total CyberArk accounts, "
                f"{len(admin_users)} privileged-type, {len(suspended_users)} suspended"
            ),
            source_ref="cyberark-admin-users",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "total_user_count": len(users),
                "admin_type_count": len(admin_users),
                "suspended_count": len(suspended_users),
                "users": [
                    {
                        "id": u.get("id"),
                        "username": u.get("username") or u.get("Username"),
                        "user_type": u.get("userType") or u.get("UserType"),
                        "first_name": u.get("firstName") or u.get("FirstName"),
                        "last_name": u.get("lastName") or u.get("LastName"),
                        "suspended": u.get("suspended") or u.get("Suspended"),
                        "last_successful_login_date": u.get("lastSuccessfulLoginDate"),
                    }
                    for u in users[:100]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("CyberArk connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting CyberArk sync (url=%s, last_run=%s)",
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
    CyberArkConnector().run()