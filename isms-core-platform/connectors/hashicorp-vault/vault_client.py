"""HashiCorp Vault HTTP API client for the Vault connector.

Handles:
  - Vault token auth via X-Vault-Token header
  - Optional namespace support (Vault Enterprise)
  - Endpoints used:
      /v1/sys/seal-status    → cluster state
      /v1/sys/health         → health check
      /v1/sys/policies/acl   → A.8.2-3-5
      /v1/sys/mounts         → A.8.2-3-5
      /v1/sys/auth           → A.5.17
      /v1/sys/audit          → A.8.15
      /v1/sys/leases/lookup/ → A.8.2-3-5

Config keys: url, token, namespace (optional)
Env vars:    VAULT_URL, VAULT_TOKEN, VAULT_NAMESPACE
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)


class VaultClient:
    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get("url") or os.environ.get("VAULT_URL", "")).rstrip("/")
        self.token = cfg.get("token") or os.environ.get("VAULT_TOKEN", "")
        self.namespace = cfg.get("namespace") or os.environ.get("VAULT_NAMESPACE", "")
        if not self.base_url:
            raise ValueError("Vault URL is required (config key 'url' or VAULT_URL env var)")
        if not self.token:
            raise ValueError("Vault token is required (config key 'token' or VAULT_TOKEN env var)")

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _headers(self) -> dict:
        h = {
            "X-Vault-Token": self.token,
            "Accept": "application/json",
        }
        if self.namespace:
            h["X-Vault-Namespace"] = self.namespace
        return h

    def _get(self, path: str, params: dict | None = None) -> dict:
        """Single authenticated GET to the Vault API."""
        resp = requests.get(
            f"{self.base_url}{path}",
            headers=self._headers(),
            params=params,
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json()

    def _list(self, path: str) -> list[str]:
        """Vault LIST operation — returns key names."""
        resp = requests.request(
            "LIST",
            f"{self.base_url}{path}",
            headers=self._headers(),
            timeout=15,
        )
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", {}).get("keys", [])

    # ── Data fetches ──────────────────────────────────────────────────────────

    def get_seal_status(self) -> dict:
        """Seal/unseal and HA status — does NOT require auth."""
        logger.info("Fetching Vault seal status...")
        try:
            resp = requests.get(
                f"{self.base_url}/v1/sys/seal-status",
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json()
            logger.info("Vault sealed=%s, ha_enabled=%s", data.get("sealed"), data.get("ha_enabled"))
            return data
        except Exception as e:
            logger.warning("Could not fetch seal status: %s", e)
            return {}

    def get_health(self) -> dict:
        """Cluster health. Returns 200 (active), 429 (standby), 472/473 (DR/perf standby)."""
        logger.info("Fetching Vault health...")
        try:
            # Use standby_ok and perfstandbyok to avoid non-200 on standbys
            resp = requests.get(
                f"{self.base_url}/v1/sys/health",
                params={"standbyok": "true", "perfstandbyok": "true"},
                timeout=10,
            )
            # Health endpoint uses non-200 to indicate state — parse regardless
            data = resp.json()
            logger.info("Vault health: initialized=%s, sealed=%s, version=%s",
                        data.get("initialized"), data.get("sealed"), data.get("version"))
            return data
        except Exception as e:
            logger.warning("Could not fetch Vault health: %s", e)
            return {}

    def get_policies(self) -> list[str]:
        """List ACL policy names."""
        logger.info("Fetching Vault ACL policies...")
        try:
            policies = self._list("/v1/sys/policies/acl")
            logger.info("Fetched %d ACL policies", len(policies))
            return policies
        except Exception as e:
            logger.warning("Could not fetch policies: %s", e)
            return []

    def get_secret_engines(self) -> dict:
        """Mounted secret engines. Returns the mounts dict keyed by path."""
        logger.info("Fetching Vault secret engines...")
        try:
            data = self._get("/v1/sys/mounts")
            # Response may wrap in 'data' for newer API versions
            mounts = data.get("data", data)
            # Filter out sys/* paths that are not secret engines
            engines = {k: v for k, v in mounts.items() if isinstance(v, dict) and "type" in v}
            logger.info("Fetched %d secret engines", len(engines))
            return engines
        except Exception as e:
            logger.warning("Could not fetch secret engines: %s", e)
            return {}

    def get_auth_methods(self) -> dict:
        """Configured auth methods. Returns dict keyed by path."""
        logger.info("Fetching Vault auth methods...")
        try:
            data = self._get("/v1/sys/auth")
            methods = data.get("data", data)
            auth_methods = {k: v for k, v in methods.items() if isinstance(v, dict) and "type" in v}
            logger.info("Fetched %d auth methods", len(auth_methods))
            return auth_methods
        except Exception as e:
            logger.warning("Could not fetch auth methods: %s", e)
            return {}

    def get_audit_devices(self) -> dict:
        """Configured audit devices. Returns dict keyed by path."""
        logger.info("Fetching Vault audit devices...")
        try:
            data = self._get("/v1/sys/audit")
            devices = data.get("data", data)
            audit_devices = {k: v for k, v in devices.items() if isinstance(v, dict)}
            logger.info("Fetched %d audit devices", len(audit_devices))
            return audit_devices
        except requests.HTTPError as e:
            if e.response.status_code in (403, 404):
                logger.warning(
                    "Audit devices returned %d — requires root or sudo capability on sys/audit",
                    e.response.status_code,
                )
                return {}
            raise

    def list_leases(self, prefix: str = "auth/") -> list[str]:
        """List active lease IDs under the given prefix."""
        logger.info("Listing Vault leases (prefix=%s)...", prefix)
        try:
            path = f"/v1/sys/leases/lookup/{prefix.strip('/')}"
            keys = self._list(path)
            logger.info("Found %d leases under %s", len(keys), prefix)
            return keys
        except Exception as e:
            logger.warning("Could not list leases: %s", e)
            return []
