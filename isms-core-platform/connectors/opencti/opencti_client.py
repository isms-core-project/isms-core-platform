"""OpenCTI REST/GraphQL client using the official pycti SDK.

Filigran's open threat intelligence platform (STIX 2.1).
GraphQL API — pycti wraps auth, pagination, and retry logic.

Reference: github.com/OpenCTI-Platform/opencti
Elastic reference: github.com/elastic/integrations/tree/main/packages/ti_opencti

Environment variables:
  OPENCTI_URL          — e.g. https://opencti.corp.local or https://app.opencti.io
  OPENCTI_TOKEN        — API token (user profile → API Access → Token)
  OPENCTI_VERIFY_SSL   — "false" to skip cert check (default: true)
  OPENCTI_INDICATOR_LIMIT   — max indicators to fetch (default: 500)
  OPENCTI_VULN_LIMIT        — max vulnerabilities (default: 500)
  OPENCTI_INCIDENT_LIMIT    — max incidents (default: 200)
"""

import logging
import os

logger = logging.getLogger(__name__)


class OpenCTIClient:
    """Thin wrapper around pycti.OpenCTIApiClient."""

    def __init__(self, **cfg) -> None:
        try:
            from pycti import OpenCTIApiClient
        except ImportError as e:
            raise ImportError("pycti not installed — add it to requirements.txt") from e

        url = (cfg.get('url') or os.environ["OPENCTI_URL"]).rstrip("/")
        token = cfg.get('token') or os.environ["OPENCTI_TOKEN"]
        verify_ssl = (cfg.get('verify_ssl') or os.environ.get("OPENCTI_VERIFY_SSL", "true")).lower() != "false"

        self.indicator_limit = int(cfg.get('indicator_limit') or os.environ.get("OPENCTI_INDICATOR_LIMIT", "500"))
        self.vuln_limit = int(os.environ.get("OPENCTI_VULN_LIMIT", "500"))
        self.incident_limit = int(os.environ.get("OPENCTI_INCIDENT_LIMIT", "200"))

        if not verify_ssl:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for OpenCTI")

        # log_level="ERROR" suppresses pycti's own verbose INFO logging
        self.api = OpenCTIApiClient(url, token, log_level="ERROR", ssl_verify=verify_ssl)
        logger.info("OpenCTI client initialised at %s", url)

    # ── Indicators (active, non-revoked) ─────────────────────────────────────

    def get_indicators(self) -> list[dict]:
        """Active indicators (IPs, domains, hashes, URLs, etc.)."""
        try:
            return self.api.indicator.list(
                first=self.indicator_limit,
                orderBy="created_at",
                orderMode="desc",
                filters={
                    "mode": "and",
                    "filters": [{"key": "revoked", "values": ["false"]}],
                    "filterGroups": [],
                },
                getAll=False,
            )
        except Exception as e:
            logger.warning("Indicators fetch error: %s", e)
            # Fallback without filter (older pycti / older OpenCTI)
            return self.api.indicator.list(
                first=self.indicator_limit,
                orderBy="created_at",
                orderMode="desc",
                getAll=False,
            )

    # ── Vulnerabilities ───────────────────────────────────────────────────────

    def get_vulnerabilities(self) -> list[dict]:
        """CVE-tracked vulnerabilities with CVSS metadata."""
        return self.api.vulnerability.list(
            first=self.vuln_limit,
            orderBy="modified",
            orderMode="desc",
            getAll=False,
        )

    # ── Incidents ─────────────────────────────────────────────────────────────

    def get_incidents(self) -> list[dict]:
        """Recorded cyber incidents."""
        return self.api.incident.list(
            first=self.incident_limit,
            orderBy="created_at",
            orderMode="desc",
            getAll=False,
        )

    # ── Threat actors ─────────────────────────────────────────────────────────

    def get_threat_actors(self) -> list[dict]:
        """Threat actor groups (APTs, criminal organisations)."""
        try:
            return self.api.threat_actor_group.list(
                first=200,
                orderBy="created_at",
                orderMode="desc",
                getAll=False,
            )
        except AttributeError:
            # pycti <6 uses threat_actor (non-grouped)
            return self.api.threat_actor.list(
                first=200,
                orderBy="created_at",
                orderMode="desc",
                getAll=False,
            )

    # ── Attack patterns (MITRE ATT&CK) ───────────────────────────────────────

    def get_attack_patterns(self) -> list[dict]:
        """MITRE ATT&CK techniques and sub-techniques."""
        return self.api.attack_pattern.list(
            first=500,
            getAll=False,
        )
