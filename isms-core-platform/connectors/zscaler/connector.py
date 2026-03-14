"""Zscaler Internet Access (ZIA) connector for ISMS CORE v2.0.

Pulls from the ZIA REST API and posts evidence to:
  a.8.23       — Web Filtering           (URL categories)
  a.8.20-22    — Network Security        (firewall rules + SSL inspection)
  a.5.15-16-18 — Identity and Access Management  (user inventory)

Environment variables required:
  ISMS_API_URL      — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN    — connector bearer token from /admin/connectors/register
  ZSCALER_URL       — Cloud-specific base URL, e.g. https://zsapi.zscalerthree.net/api/v1
  ZSCALER_USERNAME  — ZIA admin username
  ZSCALER_PASSWORD  — ZIA admin password
  ZSCALER_API_KEY   — ZIA API key
  POLL_INTERVAL     — seconds between syncs (default: 86400 = 24h)

ZIA admin role required: read access to URL Filtering, Firewall, SSL Inspection, Users
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from zscaler_client import ZscalerClient

logger = logging.getLogger(__name__)


class ZscalerConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.zia = ZscalerClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — ZIA data is always current state."""
        url_categories = self.zia.get_url_categories()
        firewall_rules = self.zia.get_firewall_rules()
        ssl_inspection_rules = self.zia.get_ssl_inspection_rules()
        users = self.zia.get_users()

        return [
            {
                "_type": "zscaler_bundle",
                "url_categories": url_categories,
                "firewall_rules": firewall_rules,
                "ssl_inspection_rules": ssl_inspection_rules,
                "users": users,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() — bundle produces multiple items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        url_categories = bundle["url_categories"]
        firewall_rules = bundle["firewall_rules"]
        ssl_inspection_rules = bundle["ssl_inspection_rules"]
        users = bundle["users"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.23 — Web Filtering: URL categories ────────────────────────────
        custom_categories = [
            c for c in url_categories
            if c.get("customCategory") or c.get("type") == "URL_CATEGORY_TYPE_CUSTOM"
        ]
        # Blocked: action BLOCK or CAUTION, or category name contains Block/Malware/Adult etc.
        _blocked_keywords = {"block", "malware", "adult", "illegal", "gambling", "hate"}
        blocked_categories = [
            c for c in url_categories
            if any(kw in (c.get("configuredName") or c.get("id", "")).lower()
                   for kw in _blocked_keywords)
        ]

        items.append(EvidenceItem(
            group_code="a.8.23",
            title=(
                f"Zscaler URL categories: {len(url_categories)} total "
                f"({len(custom_categories)} custom, "
                f"{len(blocked_categories)} block-type)"
            ),
            source_ref="zscaler-url-categories",
            classification="policy",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_categories": len(url_categories),
                "custom_category_count": len(custom_categories),
                "blocked_category_count": len(blocked_categories),
                "categories": [
                    {
                        "id": c.get("id"),
                        "configured_name": c.get("configuredName"),
                        "custom_category": c.get("customCategory"),
                        "url_count": len(c.get("urls", [])),
                    }
                    for c in url_categories[:100]
                ],
            },
        ))

        # ── A.8.20-22 — Network Security: Firewall rules ──────────────────────
        active_rules = [
            r for r in firewall_rules
            if r.get("state") in ("ENABLED", "enabled", True) or r.get("state") is True
        ]
        by_action: dict[str, int] = Counter(
            r.get("action", "Unknown") for r in firewall_rules
        )

        firewall_status = "compliant" if active_rules else "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"Zscaler firewall rules: {len(firewall_rules)} configured, "
                f"{len(active_rules)} active"
            ),
            source_ref="zscaler-firewall-rules",
            classification="network",
            status=firewall_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_firewall_rules": len(firewall_rules),
                "active_rules": len(active_rules),
                "by_action": dict(by_action),
                "ssl_inspection_rules": len(ssl_inspection_rules),
                "rules": [
                    {
                        "name": r.get("name"),
                        "action": r.get("action"),
                        "state": r.get("state"),
                        "order": r.get("order"),
                    }
                    for r in firewall_rules
                ],
                "ssl_rules": [
                    {
                        "name": r.get("name"),
                        "action": r.get("action"),
                        "state": r.get("state"),
                    }
                    for r in ssl_inspection_rules
                ],
            },
        ))

        # ── A.5.15-16-18 — Identity and Access Management: User inventory ────
        by_department: dict[str, int] = Counter(
            (u.get("department") or {}).get("name", "Unknown") if isinstance(u.get("department"), dict)
            else str(u.get("department", "Unknown"))
            for u in users
        )

        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=f"Zscaler user inventory: {len(users)} users across {len(by_department)} departments",
            source_ref="zscaler-users",
            classification="user",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_users": len(users),
                "departments": len(by_department),
                "by_department": dict(by_department),
                "users": [
                    {
                        "name": u.get("name"),
                        "email": u.get("email"),
                        "department": (u.get("department") or {}).get("name") if isinstance(u.get("department"), dict)
                                       else u.get("department"),
                    }
                    for u in users
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Zscaler connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Zscaler sync (last_run=%s)", since or "never")

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
    ZscalerConnector().run()
