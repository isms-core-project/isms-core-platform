"""Fortinet FortiAnalyzer connector for ISMS CORE v2.0.

Pulls from the FortiAnalyzer JSON-RPC API and posts evidence to:
  a.8.1-7-18-19 — Endpoint security / network devices  (registered FortiGate count)
  a.8.15        — Logging                               (log events in last 24h, processing status)
  a.8.16        — Monitoring of activities              (open incidents by severity)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  FORTI_ANALYZER_HOST       — FortiAnalyzer base URL, e.g. https://forti-analyzer.corp.local
  FORTI_ANALYZER_USERNAME   — Admin username (read-only service account)
  FORTI_ANALYZER_PASSWORD   — Admin password
  FORTI_ANALYZER_VERIFY_SSL — "false" to skip TLS verification for self-signed certs (default: true)
  POLL_INTERVAL             — seconds between syncs (default: 3600)

API permissions required:
  FortiAnalyzer REST API requirements:
  - Create a read-only admin account in System → Administrators
  - Profile: Standard_User or custom profile with Log & Report: Read, Device Manager: Read
  - No write permissions required
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from forti_analyzer_client import FortiAnalyzerClient

logger = logging.getLogger(__name__)

# Severity field values used in FortiAnalyzer incidents
_CRITICAL_SEVERITIES = {"critical", "high"}


class FortiAnalyzerConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.client = FortiAnalyzerClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — FortiAnalyzer state is always current."""
        devices = self.client.get_devices()
        log_events = self.client.get_log_events(hours=24)
        incidents = self.client.get_incidents()

        return [{
            "_type": "forti_analyzer_bundle",
            "devices": devices,
            "log_events": log_events,
            "incidents": incidents,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        log_events = bundle["log_events"]
        incidents = bundle["incidents"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1-7-18-19 — Registered FortiGate devices ─────────────────────
        total_devices = len(devices)
        conn_counter: Counter = Counter(
            str(d.get("conn_status", d.get("connection_status", "unknown"))).lower()
            for d in devices
        )
        connected = conn_counter.get("1", 0) + conn_counter.get("connected", 0)
        disconnected = total_devices - connected

        model_counter: Counter = Counter(
            str(d.get("platform_str", d.get("model", "unknown")))
            for d in devices
        )

        device_status = (
            "non-compliant" if disconnected > 0 and total_devices > 0 and (disconnected / total_devices) > 0.2
            else "attention-required" if disconnected > 0
            else "compliant" if total_devices > 0
            else "attention-required"
        )

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"FortiAnalyzer device inventory: {total_devices} registered FortiGate devices "
                f"({connected} connected, {disconnected} disconnected)"
            ),
            source_ref="forti-analyzer-devices",
            classification="asset",
            status=device_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "devices": {
                    "total": total_devices,
                    "connected": connected,
                    "disconnected": disconnected,
                    "by_model": dict(model_counter.most_common(10)),
                },
                "sample_devices": [
                    {
                        "name": d.get("name", ""),
                        "ip": d.get("ip", ""),
                        "model": d.get("platform_str", d.get("model", "")),
                        "serial": d.get("sn", ""),
                        "conn_status": d.get("conn_status", ""),
                        "os_version": d.get("os_ver", ""),
                    }
                    for d in devices[:30]
                ],
            },
        ))

        # ── A.8.15 — Log processing / logging evidence ────────────────────────
        hours = log_events.get("hours", 24)
        log_error = log_events.get("error")
        entries = log_events.get("entries") or []
        has_error = bool(log_error)
        total_log_entries = len(entries) if isinstance(entries, list) else 0

        log_status = (
            "non-compliant" if has_error and total_devices > 0
            else "compliant" if total_devices > 0
            else "attention-required"
        )

        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"FortiAnalyzer log summary: log collection active across "
                f"{total_devices} devices (last {hours}h)"
                + (f" — API error: {log_error}" if has_error else "")
            ),
            source_ref="forti-analyzer-log-summary",
            classification="network",
            status=log_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "log_collection": {
                    "hours_checked": hours,
                    "devices_registered": total_devices,
                    "api_error": log_error,
                    "log_entries_sampled": total_log_entries,
                },
            },
        ))

        # ── A.8.16 — Open incidents / monitoring activities ───────────────────
        total_incidents = len(incidents)
        sev_counter: Counter = Counter(
            str(i.get("severity", i.get("level", "unknown"))).lower()
            for i in incidents
        )
        critical_incidents = sum(
            sev_counter.get(s, 0) for s in ("critical", "high", "1", "2")
        )
        medium_incidents = sum(
            sev_counter.get(s, 0) for s in ("medium", "3")
        )

        incident_status = (
            "non-compliant" if critical_incidents > 0
            else "attention-required" if total_incidents > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"FortiAnalyzer incidents: {total_incidents} open incidents "
                f"({critical_incidents} critical/high, {medium_incidents} medium)"
            ),
            source_ref="forti-analyzer-incidents",
            classification="incident",
            status=incident_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "incidents": {
                    "total": total_incidents,
                    "critical_high": critical_incidents,
                    "medium": medium_incidents,
                    "by_severity": dict(sev_counter),
                },
                "recent_incidents": [
                    {
                        "id": inc.get("id", inc.get("incid", "")),
                        "name": inc.get("name", inc.get("title", "")),
                        "severity": inc.get("severity", inc.get("level", "")),
                        "status": inc.get("status", ""),
                        "create_time": inc.get("createtime", inc.get("create_time", "")),
                    }
                    for inc in incidents[:30]
                ],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("FortiAnalyzer connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting FortiAnalyzer sync (last_run=%s)", since or "never")
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
    FortiAnalyzerConnector().run()
