"""Cisco ISE connector for ISMS CORE v2.0.

Pulls from the Cisco ISE ERS API and posts evidence to:
  a.5.15  — Access control            (NAD inventory, authorisation profiles)
  a.8.20  — Network security          (registered endpoints, posture compliance)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  CISCO_ISE_HOST        — ISE PAN hostname/IP
  CISCO_ISE_USERNAME    — ERS admin username
  CISCO_ISE_PASSWORD    — ERS admin password
  CISCO_ISE_VERIFY_SSL  — "false" for self-signed certs
  POLL_INTERVAL         — seconds between syncs (default: 3600)
"""

import logging
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from cisco_ise_client import CiscoISEClient

logger = logging.getLogger(__name__)


class CiscoISEConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        import os
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        cfg = self._load_config()
        self.ise = CiscoISEClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        devices = self.ise.get_network_devices()
        endpoints = self.ise.get_endpoints()
        identity_groups = self.ise.get_identity_groups()
        auth_profiles = self.ise.get_authorization_profiles()
        sessions = self.ise.get_active_sessions()
        posture = self.ise.get_posture_report()

        return [{"_type": "ise_bundle", "devices": devices, "endpoints": endpoints,
                 "identity_groups": identity_groups, "auth_profiles": auth_profiles,
                 "sessions": sessions, "posture": posture,
                 "fetched_at": datetime.now(timezone.utc).isoformat()}]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        endpoints = bundle["endpoints"]
        identity_groups = bundle["identity_groups"]
        auth_profiles = bundle["auth_profiles"]
        sessions = bundle["sessions"]
        posture = bundle["posture"]
        fetched_at = bundle["fetched_at"]

        active_sessions = sessions[0].get("active_sessions", 0) if sessions else 0

        # ── A.5.15 — Access control (NAD + auth profiles) ─────────────────────
        items.append(EvidenceItem(
            group_code="a.5.15-16-18",
            title=(
                f"Cisco ISE access control: {len(devices)} network devices, "
                f"{len(auth_profiles)} authorisation profiles, "
                f"{active_sessions} active RADIUS sessions"
            ),
            source_ref="cisco-ise-access-control",
            classification="network",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "network_devices_count": len(devices),
                "auth_profiles_count": len(auth_profiles),
                "identity_groups_count": len(identity_groups),
                "active_sessions": active_sessions,
                "auth_profiles": [{"name": p.get("name"), "description": p.get("description")} for p in auth_profiles[:30]],
                "identity_groups": [{"name": g.get("name")} for g in identity_groups[:30]],
                "network_devices": [{"name": d.get("name"), "description": d.get("description")} for d in devices[:30]],
            },
        ))

        # ── A.8.20 — Network security (endpoint inventory + posture) ──────────
        posture_data = posture[0] if posture else {}
        compliant_count = int(posture_data.get("compliantDevicesCount", 0))
        non_compliant_count = int(posture_data.get("nonCompliantDevicesCount", 0))
        unknown_count = int(posture_data.get("unknownDevicesCount", 0))
        total_posture = compliant_count + non_compliant_count + unknown_count

        posture_pct = round(compliant_count / total_posture * 100, 1) if total_posture else 0
        posture_status = "compliant" if non_compliant_count == 0 else (
            "attention-required" if non_compliant_count < total_posture * 0.1 else "non-compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"Cisco ISE endpoint inventory: {len(endpoints)} registered endpoints "
                f"— posture: {posture_pct}% compliant "
                f"({compliant_count}/{total_posture or len(endpoints)})"
            ),
            source_ref="cisco-ise-endpoint-posture",
            classification="network",
            status=posture_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "endpoints_registered": len(endpoints),
                "posture_summary": {
                    "compliant": compliant_count,
                    "non_compliant": non_compliant_count,
                    "unknown": unknown_count,
                    "total": total_posture,
                    "compliance_pct": posture_pct,
                },
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Cisco ISE connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                bundles = self.fetch(None)
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
            time.sleep(max(0, self.poll_interval - elapsed))


if __name__ == "__main__":
    CiscoISEConnector().run()
