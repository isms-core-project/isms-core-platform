"""Fortinet FortiManager connector for ISMS CORE v2.0.

Pulls from the FortiManager JSON-RPC API and posts evidence to:
  a.8.1-7-18-19 — Endpoint security / network device inventory  (managed device count, status)
  a.8.20-22     — Network security / segmentation / filtering   (policy package count per ADOM)
  a.8.1-7-18-19 — Firmware compliance                          (firmware template count)

Environment variables required:
  ISMS_API_URL              — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN            — connector bearer token from /admin/connectors/register
  FORTI_MANAGER_HOST        — FortiManager base URL, e.g. https://forti-manager.corp.local
  FORTI_MANAGER_USERNAME    — Admin username (read-only service account)
  FORTI_MANAGER_PASSWORD    — Admin password
  FORTI_MANAGER_VERIFY_SSL  — "false" to skip TLS verification for self-signed certs (default: true)
  FORTI_MANAGER_ADOM        — ADOM to query for policies/templates (default: root)
  POLL_INTERVAL             — seconds between syncs (default: 3600)

API permissions required:
  FortiManager REST API requirements:
  - Create a read-only admin account in System → Administrators
  - Profile: Standard_User with ADOM access (set to specific ADOMs or All ADOMs)
  - Package access: Read
  - Device Manager: Read
"""

import logging
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from forti_manager_client import FortiManagerClient

logger = logging.getLogger(__name__)


class FortiManagerConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "3600"))
        self._adom = os.environ.get("FORTI_MANAGER_ADOM", "root")
        cfg = self._load_config()
        self.client = FortiManagerClient(**cfg)

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — FortiManager state is always current."""
        devices = self.client.get_devices()
        adoms = self.client.get_adoms()
        # Determine ADOMs to query — use configured ADOM + any discovered ones (up to 5)
        adom_names = list({self._adom} | {a.get("name", "") for a in adoms if a.get("name")})
        adom_names = [n for n in adom_names if n][:5]

        policy_packages: dict[str, list] = {}
        firmware_templates: dict[str, list] = {}
        for adom_name in adom_names:
            policy_packages[adom_name] = self.client.get_policy_packages(adom=adom_name)
            firmware_templates[adom_name] = self.client.get_firmware_templates(adom=adom_name)

        return [{
            "_type": "forti_manager_bundle",
            "devices": devices,
            "adoms": adoms,
            "policy_packages": policy_packages,
            "firmware_templates": firmware_templates,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }]

    def transform(self, item: dict) -> EvidenceItem | None:
        """Override run() instead — bundle produces multiple evidence items."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        devices = bundle["devices"]
        adoms = bundle["adoms"]
        policy_packages = bundle["policy_packages"]
        firmware_templates = bundle["firmware_templates"]
        fetched_at = bundle["fetched_at"]

        # ── A.8.1-7-18-19 — Managed device inventory + connection status ──────
        total_devices = len(devices)

        # FortiManager conn_status: 0=unknown, 1=up, 2=down
        conn_counter: Counter = Counter(
            str(d.get("conn_status", d.get("connection_status", "unknown")))
            for d in devices
        )
        # Accept both integer codes and string labels
        up_count = conn_counter.get("1", 0) + conn_counter.get("up", 0) + conn_counter.get("connected", 0)
        down_count = conn_counter.get("2", 0) + conn_counter.get("down", 0) + conn_counter.get("disconnected", 0)
        unknown_count = total_devices - up_count - down_count

        model_counter: Counter = Counter(
            str(d.get("platform_str", d.get("model", "unknown")))
            for d in devices
        )

        down_pct = (down_count / total_devices * 100) if total_devices else 0
        if down_count >= 2 and down_pct > 20:
            device_status = "non-compliant"
        elif down_count > 0:
            device_status = "attention-required"
        elif total_devices == 0:
            device_status = "attention-required"
        else:
            device_status = "compliant"

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"FortiManager device inventory: {total_devices} managed devices "
                f"({up_count} up, {down_count} down, {unknown_count} unknown)"
            ),
            source_ref="forti-manager-device-inventory",
            classification="asset",
            status=device_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "devices": {
                    "total": total_devices,
                    "up": up_count,
                    "down": down_count,
                    "unknown": unknown_count,
                    "down_pct": round(down_pct, 1),
                    "by_model": dict(model_counter.most_common(10)),
                },
                "adoms": [a.get("name", "") for a in adoms],
                "sample_devices": [
                    {
                        "name": d.get("name", ""),
                        "ip": d.get("ip", ""),
                        "model": d.get("platform_str", d.get("model", "")),
                        "serial": d.get("sn", ""),
                        "conn_status": d.get("conn_status", ""),
                        "os_version": d.get("os_ver", ""),
                        "adom": d.get("adom", ""),
                    }
                    for d in devices[:30]
                ],
            },
        ))

        # ── A.8.20-22 — Policy packages (network security / segmentation) ─────
        total_packages = sum(len(pkgs) for pkgs in policy_packages.values())
        pkg_by_adom = {adom: len(pkgs) for adom, pkgs in policy_packages.items()}

        # Deployed vs pending — check install_status field if available
        deployed_count = 0
        pending_count = 0
        for adom_pkgs in policy_packages.values():
            for pkg in adom_pkgs:
                install_status = str(pkg.get("install_status", pkg.get("status", ""))).lower()
                if install_status in ("installed", "1", "deployed"):
                    deployed_count += 1
                else:
                    pending_count += 1

        policy_status = (
            "non-compliant" if total_packages == 0
            else "attention-required" if pending_count > 0
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.20-22",
            title=(
                f"FortiManager policy packages: {total_packages} packages across "
                f"{len(pkg_by_adom)} ADOM(s) "
                f"({deployed_count} deployed, {pending_count} pending)"
            ),
            source_ref="forti-manager-policy-packages",
            classification="policy",
            status=policy_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "policy_packages": {
                    "total": total_packages,
                    "deployed": deployed_count,
                    "pending": pending_count,
                    "by_adom": pkg_by_adom,
                },
                "sample_packages": [
                    {
                        "name": pkg.get("name", ""),
                        "adom": adom,
                        "type": pkg.get("type", ""),
                        "install_status": pkg.get("install_status", pkg.get("status", "")),
                    }
                    for adom, pkgs in policy_packages.items()
                    for pkg in pkgs[:10]
                ][:30],
            },
        ))

        # ── A.8.1-7-18-19 — Firmware templates ───────────────────────────────
        total_templates = sum(len(tmpls) for tmpls in firmware_templates.values())
        templates_by_adom = {adom: len(tmpls) for adom, tmpls in firmware_templates.items()}

        firmware_status = (
            "compliant" if total_templates > 0
            else "attention-required"
        )

        items.append(EvidenceItem(
            group_code="a.8.1-7-18-19",
            title=(
                f"FortiManager firmware templates: {total_templates} device profile(s) "
                f"across {len(templates_by_adom)} ADOM(s)"
            ),
            source_ref="forti-manager-firmware",
            classification="asset",
            status=firmware_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "firmware_templates": {
                    "total": total_templates,
                    "by_adom": templates_by_adom,
                },
                "sample_templates": [
                    {
                        "name": tmpl.get("name", ""),
                        "adom": adom,
                        "type": tmpl.get("type", ""),
                        "description": tmpl.get("description", ""),
                    }
                    for adom, tmpls in firmware_templates.items()
                    for tmpl in tmpls[:10]
                ][:30],
            },
        ))

        return items

    def run(self) -> None:
        logger.info("FortiManager connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting FortiManager sync (last_run=%s)", since or "never")
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
    FortiManagerConnector().run()
