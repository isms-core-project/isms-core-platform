"""Threat Intelligence Feed connector — polls TAXII 2.1, MISP, or generic JSON threat feeds.

Maps to:
  a.8.16  — Monitoring activities (threat indicator counts + IOC summary)
  a.5.7   — Threat intelligence (feed coverage and freshness)

Supported feed types:
  taxii21  — TAXII 2.1 collections (STIX 2.1) — standard for commercial TI feeds
  misp     — MISP instance REST API
  json     — Generic JSON array of indicators

Env vars (or config keys via GUI):
  ISMS_API_URL                — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN              — connector bearer token from /admin/connectors/register
  THREAT_INTEL_FEED_URL       — feed endpoint URL
  THREAT_INTEL_AUTH_TYPE      — api_key | basic (default: api_key)
  THREAT_INTEL_API_KEY        — API key
  THREAT_INTEL_USERNAME       — for basic auth
  THREAT_INTEL_PASSWORD       — for basic auth
  THREAT_INTEL_FEED_TYPE      — taxii21 | misp | json (default: json)
  THREAT_INTEL_COLLECTION     — TAXII collection ID (for taxii21 feeds)
  THREAT_INTEL_VERIFY_SSL     — true/false (default: true)
  POLL_INTERVAL               — seconds (default: 3600)
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from taxii_client import ThreatIntelClient

logger = logging.getLogger(__name__)

# Field names to look for when identifying an indicator's type
_TYPE_FIELDS = ("type", "indicator_type", "category", "ioc_type", "object_type")

# Field names to look for when identifying the most recent update timestamp
_DATE_FIELDS = ("valid_from", "created", "created_at", "date", "first_seen", "timestamp", "modified")

# How many days before we consider a feed "stale"
_WARN_DAYS = 7
_CRITICAL_DAYS = 30


def _get_field(d: dict, candidates: tuple[str, ...], default: str = "") -> str:
    for key in candidates:
        val = d.get(key)
        if val is not None:
            return str(val)
    return default


def _parse_date(s: str) -> datetime | None:
    """Parse an ISO 8601 datetime string. Returns None on failure."""
    if not s:
        return None
    # Strip trailing Z, handle +00:00, accept partial dates
    s = s.strip()
    for fmt in (
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ):
        try:
            dt = datetime.strptime(s[:26], fmt[:len(fmt)])
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


class ThreatIntelConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.client = ThreatIntelClient(
            feed_url=cfg.get("feed_url", ""),
            auth_type=cfg.get("auth_type", "api_key"),
            api_key=cfg.get("api_key", ""),
            username=cfg.get("username", ""),
            password=cfg.get("password", ""),
            feed_type=cfg.get("feed_type", "json"),
            collection_id=cfg.get("collection_id", ""),
            verify_ssl=cfg.get("verify_ssl", True),
        )

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — fetch all current indicators from the configured feed."""
        indicators = self.client.get_indicators(500)
        summary = self.client.get_summary()
        return [
            {
                "_type": "threat_intel_bundle",
                "indicators": indicators,
                "summary": summary,
                "feed_url": self.client.feed_url,
                "feed_type": self.client.feed_type,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        indicators = bundle["indicators"]
        summary = bundle["summary"]
        feed_url = bundle["feed_url"]
        feed_type = bundle["feed_type"]
        fetched_at = bundle["fetched_at"]

        total = len(indicators)

        # ── Type distribution (best-effort across type field name variants) ───
        by_type: Counter[str] = Counter(
            _get_field(ind, _TYPE_FIELDS, "unknown").lower()
            for ind in indicators
        )

        # Aggregate well-known categories
        ip_count = sum(v for k, v in by_type.items() if "ip" in k or "ipv4" in k or "ipv6" in k)
        domain_count = sum(v for k, v in by_type.items() if "domain" in k or "hostname" in k or "fqdn" in k)
        hash_count = sum(v for k, v in by_type.items() if "hash" in k or "file" in k or "md5" in k or "sha" in k)
        url_count = sum(v for k, v in by_type.items() if "url" in k or "uri" in k)

        # ── A.5.7 — Threat intelligence (feed coverage) ───────────────────────
        items.append(EvidenceItem(
            group_code="a.5.7",
            title=(
                f"Threat intelligence: {total} indicators "
                f"({ip_count} IPs, {domain_count} domains, "
                f"{hash_count} hashes, {url_count} URLs)"
            ),
            source_ref="threat-intel-feed-coverage",
            classification="info",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total": total,
                "by_type": dict(by_type),
                "aggregated": {
                    "ip_count": ip_count,
                    "domain_count": domain_count,
                    "hash_count": hash_count,
                    "url_count": url_count,
                },
                "feed_url": feed_url,
                "feed_type": feed_type,
                "summary": summary,
            },
        ))

        # ── A.8.16 — Feed freshness (monitoring activities) ───────────────────
        # Find the most recent timestamp across all indicators
        most_recent_dt: datetime | None = None
        most_recent_str: str = ""
        for ind in indicators:
            for field in _DATE_FIELDS:
                raw_date = ind.get(field, "")
                if not raw_date:
                    continue
                dt = _parse_date(str(raw_date))
                if dt and (most_recent_dt is None or dt > most_recent_dt):
                    most_recent_dt = dt
                    most_recent_str = str(raw_date)
                break  # use first matching date field per indicator

        now = datetime.now(timezone.utc)
        days_since: int | None = None
        freshness_classification = "compliant"
        if most_recent_dt is not None:
            delta = now - most_recent_dt
            days_since = delta.days
            if days_since > _CRITICAL_DAYS:
                freshness_classification = "non_compliant"
            elif days_since > _WARN_DAYS:
                freshness_classification = "warning"
        else:
            # Cannot determine freshness — treat as warning
            freshness_classification = "warning"

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"Threat feed freshness: {total} active indicators, "
                f"most recent: {most_recent_str or 'unknown'}"
            ),
            source_ref="threat-intel-feed-freshness",
            classification=freshness_classification,
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total": total,
                "most_recent_date": most_recent_str,
                "days_since_update": days_since,
                "freshness_thresholds": {
                    "warn_days": _WARN_DAYS,
                    "critical_days": _CRITICAL_DAYS,
                },
                "recent_sample": [
                    {
                        "type": _get_field(ind, _TYPE_FIELDS),
                        "value": str(ind.get("value", "")),
                        "threat_type": str(ind.get("threat_type", "")),
                        "valid_from": str(ind.get("valid_from", "")),
                        "confidence": ind.get("confidence", 0),
                    }
                    for ind in indicators[:10]
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        logger.info("ThreatIntel connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info(
                    "Starting ThreatIntel sync (feed_url=%s, feed_type=%s, last_run=%s)",
                    self.client.feed_url,
                    self.client.feed_type,
                    since or "never",
                )

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
    ThreatIntelConnector().run()
