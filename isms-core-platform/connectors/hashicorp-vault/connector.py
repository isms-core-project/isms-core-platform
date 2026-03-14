"""HashiCorp Vault connector for ISMS CORE v2.0.

Pulls from the Vault HTTP API and posts evidence to:
  a.8.2-3-5 — Privileged Access and Auth  (secret engines + active leases)
  a.5.17    — Authentication information   (auth methods configured)
  a.8.15    — Logging                      (audit device configuration)

Environment variables required:
  ISMS_API_URL          — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN        — connector bearer token from /admin/connectors/register
  VAULT_URL             — e.g. https://vault.example.com:8200
  VAULT_TOKEN           — Vault token (requires sys/mounts, sys/auth, sys/audit read)
  VAULT_NAMESPACE       — Vault Enterprise namespace (optional)
  POLL_INTERVAL         — seconds between full syncs (default: 86400 = 24h)

API permissions required:
  Vault token capabilities required (create a dedicated policy):
  - sys/policies/acl/*: read, list
  - sys/mounts: read
  - sys/auth: read
  - sys/audit: read, list (requires root or sudo)
  - sys/seal-status: no auth required
  - sys/health: no auth required
  - sys/leases/lookup/*: list, read
"""

import logging
import sys

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase
from vault_client import VaultClient

logger = logging.getLogger(__name__)


class HashiCorpVaultConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        cfg = self._load_config()
        self.client = VaultClient(**cfg)

    # ── fetch ─────────────────────────────────────────────────────────────────

    def fetch(self, since: str | None) -> list[dict]:
        """Full sync — pull all Vault configuration data each run."""
        seal_status = self.client.get_seal_status()
        health = self.client.get_health()
        policies = self.client.get_policies()
        secret_engines = self.client.get_secret_engines()
        auth_methods = self.client.get_auth_methods()
        audit_devices = self.client.get_audit_devices()
        auth_leases = self.client.list_leases(prefix="auth/")

        return [
            {
                "_type": "vault_bundle",
                "seal_status": seal_status,
                "health": health,
                "policies": policies,
                "secret_engines": secret_engines,
                "auth_methods": auth_methods,
                "audit_devices": audit_devices,
                "auth_leases": auth_leases,
            }
        ]

    # ── transform — bundle pattern ────────────────────────────────────────────

    def transform(self, item: dict) -> EvidenceItem | None:
        """Not used — bundle pattern via _transform_bundle."""
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        seal_status = bundle["seal_status"]
        policies = bundle["policies"]
        secret_engines = bundle["secret_engines"]
        auth_methods = bundle["auth_methods"]
        audit_devices = bundle["audit_devices"]
        auth_leases = bundle["auth_leases"]

        vault_version = bundle["health"].get("version", "unknown")
        is_sealed = seal_status.get("sealed", True)
        ha_enabled = seal_status.get("ha_enabled", False)

        # ── A.8.2-3-5 — Secret engines (privileged secrets management) ────────
        engine_types = sorted({v.get("type", "unknown") for v in secret_engines.values()})
        kv_engines = [k for k, v in secret_engines.items() if v.get("type") in ("kv", "kv-v2")]

        items.append(EvidenceItem(
            group_code="a.8.2-3-5",
            title=(
                f"HashiCorp Vault secret engines: {len(secret_engines)} mounted "
                f"({len(kv_engines)} KV stores) — version {vault_version}, "
                f"sealed={is_sealed}, HA={ha_enabled}"
            ),
            source_ref="vault-secret-engines",
            classification="asset",
            status="attention-required" if is_sealed else "active",
            raw={
                "vault_version": vault_version,
                "is_sealed": is_sealed,
                "ha_enabled": ha_enabled,
                "secret_engine_count": len(secret_engines),
                "engine_types": engine_types,
                "kv_engine_count": len(kv_engines),
                "acl_policy_count": len(policies),
                "active_auth_lease_count": len(auth_leases),
                "engines": [
                    {
                        "path": path,
                        "type": meta.get("type"),
                        "description": meta.get("description"),
                        "accessor": meta.get("accessor"),
                    }
                    for path, meta in secret_engines.items()
                ],
                "acl_policies": policies,
            },
        ))

        # ── A.5.17 — Authentication methods ──────────────────────────────────
        auth_types = sorted({v.get("type", "unknown") for v in auth_methods.values()})
        items.append(EvidenceItem(
            group_code="a.5.17",
            title=(
                f"HashiCorp Vault auth methods: {len(auth_methods)} configured "
                f"({', '.join(auth_types)})"
            ),
            source_ref="vault-auth-methods",
            classification="asset",
            status="active",
            raw={
                "auth_method_count": len(auth_methods),
                "auth_types": auth_types,
                "methods": [
                    {
                        "path": path,
                        "type": meta.get("type"),
                        "description": meta.get("description"),
                        "accessor": meta.get("accessor"),
                    }
                    for path, meta in auth_methods.items()
                ],
            },
        ))

        # ── A.8.15 — Audit logging ────────────────────────────────────────────
        audit_enabled = len(audit_devices) > 0
        audit_types = sorted({v.get("type", "unknown") for v in audit_devices.values()})
        items.append(EvidenceItem(
            group_code="a.8.15",
            title=(
                f"HashiCorp Vault audit logging: "
                f"{'ENABLED' if audit_enabled else 'NOT CONFIGURED'} — "
                f"{len(audit_devices)} device(s) "
                f"({', '.join(audit_types) if audit_types else 'none'})"
            ),
            source_ref="vault-audit-config",
            classification="policy",
            status="compliant" if audit_enabled else "attention-required",
            raw={
                "audit_enabled": audit_enabled,
                "audit_device_count": len(audit_devices),
                "audit_types": audit_types,
                "devices": [
                    {
                        "path": path,
                        "type": meta.get("type"),
                        "description": meta.get("description"),
                        "options": meta.get("options", {}),
                    }
                    for path, meta in audit_devices.items()
                ],
            },
        ))

        return items

    # ── Override run() for bundle pattern ─────────────────────────────────────

    def run(self) -> None:
        import time
        from datetime import datetime, timezone

        logger.info("HashiCorp Vault connector starting (poll_interval=%ds)", self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Vault sync (url=%s, last_run=%s)",
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
    HashiCorpVaultConnector().run()
