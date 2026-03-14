"""Microsoft Intune connector for ISMS CORE v2.0.

Pulls from the Microsoft Graph API /deviceManagement endpoints and posts evidence to:
  a.8.1   — Inventory of information and other assets  (managed device inventory)
  a.8.9   — Management of configuration  (compliance policies + device compliance state)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  INTUNE_TENANT_ID          — Azure AD tenant ID
  INTUNE_CLIENT_ID          — App registration client ID
  INTUNE_CLIENT_SECRET      — App registration client secret
  POLL_INTERVAL             — seconds between syncs (default: 86400 = 24h)

App Registration permissions required (Application):
  DeviceManagementManagedDevices.Read.All
  DeviceManagementConfiguration.Read.All
"""

import logging
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from intune_client import IntuneClient

logger = logging.getLogger(__name__)


class IntuneConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.intune = IntuneClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — Intune device state is always current."""
        devices = self.intune.get_managed_devices()
        configs = self.intune.get_device_configurations()
        policies = self.intune.get_compliance_policies()
        compliance_overview = self.intune.get_device_compliance_overview()

        return [
            {
                "_type": "intune_bundle",
                "devices": devices,
                "configurations": configs,
                "compliance_policies": policies,
                "compliance_overview": compliance_overview,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        configs = bundle["configurations"]
        policies = bundle["compliance_policies"]
        compliance_overview = bundle["compliance_overview"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1 — Managed device inventory ─────────────────────────────────
        by_os: dict[str, int] = Counter(d.get("operatingSystem", "Unknown") for d in devices)
        by_owner: dict[str, int] = Counter(d.get("managedDeviceOwnerType", "Unknown") for d in devices)
        by_type: dict[str, int] = Counter(d.get("deviceType", "Unknown") for d in devices)

        corporate_devices = [d for d in devices if d.get("managedDeviceOwnerType") == "company"]
        byod = [d for d in devices if d.get("managedDeviceOwnerType") == "personal"]

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"Intune device inventory: {len(devices)} managed devices "
                f"({len(corporate_devices)} corporate, {len(byod)} BYOD)"
            ),
            source_ref="intune-device-inventory",
            classification="asset",
            status="active",
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "total_devices": len(devices),
                "corporate_owned": len(corporate_devices),
                "byod": len(byod),
                "by_os": dict(by_os),
                "by_owner_type": dict(by_owner),
                "by_device_type": dict(by_type),
                "devices": [
                    {
                        "id": d.get("id"),
                        "name": d.get("deviceName"),
                        "os": d.get("operatingSystem"),
                        "os_version": d.get("osVersion"),
                        "owner_type": d.get("managedDeviceOwnerType"),
                        "compliance": d.get("complianceState"),
                        "upn": d.get("userPrincipalName"),
                        "last_sync": d.get("lastSyncDateTime"),
                        "enrolled": d.get("enrolledDateTime"),
                        "manufacturer": d.get("manufacturer"),
                        "model": d.get("model"),
                        "aad_registered": d.get("azureADRegistered"),
                    }
                    for d in devices
                ],
            },
        ))

        # ── A.8.9 — Configuration management + compliance ─────────────────────
        by_compliance: dict[str, int] = Counter(d.get("complianceState", "Unknown") for d in devices)
        non_compliant = by_compliance.get("noncompliant", 0)
        compliant = by_compliance.get("compliant", 0)
        unknown = by_compliance.get("unknown", 0) + by_compliance.get("configManager", 0)

        total = len(devices) or 1
        compliance_pct = round(compliant / total * 100, 1)

        # Compliance overview from the summary endpoint
        ov = compliance_overview
        in_grace = ov.get("inGracePeriodCount", 0)
        error_count = ov.get("errorCount", 0)

        config_status = "compliant"
        if non_compliant > total * 0.1:   # >10% non-compliant
            config_status = "non-compliant"
        elif non_compliant > 0 or in_grace > 0:
            config_status = "attention-required"

        items.append(EvidenceItem(
            group_code="a.8.9",
            title=(
                f"Intune device compliance: {compliance_pct}% compliant "
                f"({compliant}/{total} devices) — "
                f"{len(configs)} config profiles, {len(policies)} compliance policies"
            ),
            source_ref="intune-device-compliance",
            classification="asset",
            status=config_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "compliance_summary": {
                    "total": total,
                    "compliant": compliant,
                    "non_compliant": non_compliant,
                    "unknown": unknown,
                    "in_grace_period": in_grace,
                    "error_count": error_count,
                    "compliance_pct": compliance_pct,
                    "by_state": dict(by_compliance),
                },
                "configuration_profiles": {
                    "total": len(configs),
                    "list": [
                        {"name": c.get("displayName"), "last_modified": c.get("lastModifiedDateTime")}
                        for c in configs
                    ],
                },
                "compliance_policies": {
                    "total": len(policies),
                    "list": [
                        {"name": p.get("displayName"), "last_modified": p.get("lastModifiedDateTime")}
                        for p in policies
                    ],
                },
                "non_compliant_devices": [
                    {
                        "name": d.get("deviceName"),
                        "os": d.get("operatingSystem"),
                        "upn": d.get("userPrincipalName"),
                        "last_sync": d.get("lastSyncDateTime"),
                    }
                    for d in devices
                    if d.get("complianceState") == "noncompliant"
                ][:50],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("Intune connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Intune sync (last_run=%s)", since or "never")

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
    IntuneConnector().run()
