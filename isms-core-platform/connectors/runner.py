"""ISMS CORE Connectors Runner.

Single-container orchestrator for all connectors.

How it works:
  1. Polls GET /api/v1/connectors/worker/all every RUNNER_REFRESH_INTERVAL seconds
  2. For each registered connector whose source_system is supported:
       - Starts a daemon thread running that connector's sync loop
       - Thread is identified by connector_id (UUID)
  3. If a connector is deregistered, its thread exits on next poll cycle
  4. If a connector is newly registered, a thread is started within one refresh interval
  5. Config (credentials) is passed from the worker/all response — no token needed

Environment:
  ISMS_API_URL                  — e.g. http://isms-core-backend:8000
  CONNECTORS_WORKER_SECRET      — shared secret (same value in backend + this container)
  RUNNER_REFRESH_INTERVAL       — seconds between connector list refresh (default: 60)
  POLL_INTERVAL                 — seconds between each connector's sync (default: 86400)
"""

import importlib.util
import logging
import os
import sys
import threading
import time
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
)
logger = logging.getLogger("runner")

API_URL = os.environ["ISMS_API_URL"].rstrip("/")
WORKER_SECRET = os.environ["CONNECTORS_WORKER_SECRET"]
REFRESH_INTERVAL = int(os.environ.get("RUNNER_REFRESH_INTERVAL", "60"))

# Map source_system slug → (path to connector.py, ConnectorClass name)
# Paths are absolute inside the container (/app/<dir>/connector.py)
CONNECTOR_MAP: dict[str, tuple[str, str]] = {
    # ── Microsoft ──────────────────────────────────────────────────────────────
    "entra_id":          ("/app/entra-id/connector.py",          "EntraIDConnector"),
    "defender":          ("/app/defender/connector.py",          "DefenderConnector"),
    "sentinel":          ("/app/sentinel/connector.py",          "SentinelConnector"),
    "intune":            ("/app/intune/connector.py",            "IntuneConnector"),
    "purview":           ("/app/purview/connector.py",           "PurviewConnector"),
    # ── Identity & Access ──────────────────────────────────────────────────────
    "active_directory":  ("/app/active-directory/connector.py",  "ActiveDirectoryConnector"),
    "openldap":          ("/app/openldap/connector.py",          "OpenLDAPConnector"),
    "freeipa":           ("/app/freeipa/connector.py",           "FreeIPAConnector"),
    "authentik":         ("/app/authentik/connector.py",         "AuthentikConnector"),
    "keycloak":          ("/app/keycloak/connector.py",          "KeycloakConnector"),
    # ── PAM ────────────────────────────────────────────────────────────────────
    "cyberark":          ("/app/cyberark/connector.py",          "CyberArkConnector"),
    "devolutions":       ("/app/devolutions/connector.py",       "DevolutionsConnector"),
    "hashicorp_vault":   ("/app/hashicorp-vault/connector.py",   "VaultConnector"),
    # ── Network Security ───────────────────────────────────────────────────────
    "fortigate":         ("/app/fortigate/connector.py",         "FortigateConnector"),
    "forti_analyzer":    ("/app/forti-analyzer/connector.py",    "FortiAnalyzerConnector"),
    "forti_manager":     ("/app/forti-manager/connector.py",     "FortiManagerConnector"),
    "panw":              ("/app/panw/connector.py",              "PANWConnector"),
    "cisco_asa":         ("/app/cisco-asa/connector.py",         "CiscoASAConnector"),
    "cisco_ise":         ("/app/cisco-ise/connector.py",         "CiscoISEConnector"),
    "zscaler":           ("/app/zscaler/connector.py",           "ZscalerConnector"),
    # ── EDR / Endpoint ─────────────────────────────────────────────────────────
    "crowdstrike":       ("/app/crowdstrike/connector.py",       "CrowdStrikeConnector"),
    "sentinelone":       ("/app/sentinelone/connector.py",       "SentinelOneConnector"),
    "wazuh":             ("/app/wazuh/connector.py",             "WazuhConnector"),
    # ── Vulnerability Management ───────────────────────────────────────────────
    "tenable_sc":        ("/app/tenable-sc/connector.py",        "TenableSCConnector"),
    "tenable_io":        ("/app/tenable-io/connector.py",        "TenableIOConnector"),
    "qualys":            ("/app/qualys/connector.py",            "QualysConnector"),
    "openvas":           ("/app/openvas/connector.py",           "OpenVASConnector"),
    # ── ITSM ───────────────────────────────────────────────────────────────────
    "servicenow":        ("/app/servicenow/connector.py",        "ServiceNowConnector"),
    "jira":              ("/app/jira/connector.py",              "JiraConnector"),
    # ── Monitoring & SIEM ──────────────────────────────────────────────────────
    "prtg":              ("/app/prtg/connector.py",              "PRTGConnector"),
    "zabbix":            ("/app/zabbix/connector.py",            "ZabbixConnector"),
    "graylog":           ("/app/graylog/connector.py",           "GraylogConnector"),
    # ── Asset Management ───────────────────────────────────────────────────────
    "glpi":              ("/app/glpi/connector.py",              "GLPIConnector"),
    "netbox":            ("/app/netbox/connector.py",            "NetBoxConnector"),
    # ── Cloud Posture ──────────────────────────────────────────────────────────
    "aws_security_hub":  ("/app/aws-security-hub/connector.py",  "AWSSecurityHubConnector"),
    "azure_cspm":        ("/app/azure-cspm/connector.py",        "AzureCSPMConnector"),
    "gcp_scc":           ("/app/gcp-scc/connector.py",           "GCPSCCConnector"),
    # ── DevSecOps ──────────────────────────────────────────────────────────────
    "github":            ("/app/github/connector.py",            "GitHubConnector"),
    "gitlab":            ("/app/gitlab/connector.py",            "GitLabConnector"),
    # ── Microsoft 365 ──────────────────────────────────────────────────────────
    "o365":              ("/app/o365/connector.py",              "O365Connector"),
    # ── Threat Intelligence ────────────────────────────────────────────────────
    "opencti":           ("/app/opencti/connector.py",           "OpenCTIConnector"),
    "openaev":           ("/app/openaev/connector.py",           "OpenAEVConnector"),
    "threat_intel":      ("/app/threat-intel/connector.py",      "ThreatIntelConnector"),
    # ── Generic ────────────────────────────────────────────────────────────────
    "siem":              ("/app/siem/connector.py",              "SIEMConnector"),
}


def load_connector_class(source_system: str):
    """Dynamically load a connector class from its file path."""
    entry = CONNECTOR_MAP.get(source_system)
    if not entry:
        return None
    path, class_name = entry
    if not Path(path).exists():
        logger.warning("Connector file not found: %s", path)
        return None
    try:
        connector_dir = str(Path(path).parent)
        if connector_dir not in sys.path:
            sys.path.insert(0, connector_dir)
        spec = importlib.util.spec_from_file_location(f"conn_{source_system}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name, None)
    except Exception as e:
        logger.error("Failed to load connector %s: %s", source_system, e)
        return None


class ConnectorThread(threading.Thread):
    """Thread that runs a single connector's sync loop."""

    def __init__(self, connector_id: str, source_system: str, config: dict):
        name = f"{source_system}:{connector_id[:8]}"
        super().__init__(name=name, daemon=True)
        self.connector_id = connector_id
        self.source_system = source_system
        self.config = config
        self._stop = threading.Event()

    def run(self) -> None:
        cls = load_connector_class(self.source_system)
        if cls is None:
            logger.warning("[%s] No connector class found — skipping", self.name)
            return
        try:
            logger.info("[%s] Starting", self.name)
            instance = cls(connector_id=self.connector_id, config=self.config)
            instance.run()
        except Exception as e:
            logger.error("[%s] Crashed: %s", self.name, e, exc_info=True)


def fetch_connector_list() -> list[dict]:
    """GET /api/v1/connectors/worker/all — returns registered connectors + configs."""
    try:
        resp = requests.get(
            f"{API_URL}/api/v1/connectors/worker/all",
            headers={"Authorization": f"Bearer {WORKER_SECRET}"},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        logger.error("Failed to fetch connector list: %s", e)
        return []


def main() -> None:
    logger.info("ISMS CORE Connectors Runner starting")
    logger.info("API: %s | Refresh: %ds", API_URL, REFRESH_INTERVAL)

    # Wait for backend to be ready
    for attempt in range(30):
        try:
            r = requests.get(f"{API_URL}/health", timeout=5)
            if r.ok:
                logger.info("Backend ready")
                break
        except Exception:
            pass
        logger.info("Waiting for backend... (%d/30)", attempt + 1)
        time.sleep(5)
    else:
        logger.error("Backend not ready after 150s — aborting")
        sys.exit(1)

    threads: dict[str, ConnectorThread] = {}  # connector_id → thread

    while True:
        connectors = fetch_connector_list()
        active_ids = set()

        for c in connectors:
            cid = c["id"]
            system = c["source_system"]
            config = c.get("config", {})
            active_ids.add(cid)

            if system not in CONNECTOR_MAP:
                # Planned / not yet built
                continue

            existing = threads.get(cid)
            if existing and existing.is_alive():
                # Already running — nothing to do
                continue

            if existing and not existing.is_alive():
                logger.warning("[%s:%s] Thread died — restarting", system, cid[:8])

            t = ConnectorThread(cid, system, config)
            t.start()
            threads[cid] = t
            logger.info("[%s:%s] Thread started", system, cid[:8])

        # Log any threads for connectors that were deregistered
        dead_ids = set(threads.keys()) - active_ids
        for cid in dead_ids:
            logger.info("Connector %s deregistered — thread will exit naturally", cid[:8])
            del threads[cid]

        live = sum(1 for t in threads.values() if t.is_alive())
        logger.info("Status: %d registered, %d threads running", len(active_ids), live)

        time.sleep(REFRESH_INTERVAL)


if __name__ == "__main__":
    main()
