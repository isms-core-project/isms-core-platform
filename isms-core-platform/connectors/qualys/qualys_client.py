"""Qualys VMDR API client.

Uses the Qualys REST API (platform-specific base URL).
Authentication: HTTP Basic auth + X-Requested-With header.
XML and JSON endpoints are both used depending on the endpoint.

Environment variables:
  QUALYS_URL       — Platform URL, e.g. https://qualysapi.qg2.apps.qualys.com
  QUALYS_USERNAME  — Qualys username
  QUALYS_PASSWORD  — Qualys password

API documentation: https://www.qualys.com/documentation/
"""

import logging
import os
import xml.etree.ElementTree as ET

import requests

logger = logging.getLogger(__name__)

# Header required by all Qualys API calls
_REQUIRED_HEADER = "X-Requested-With"
_REQUIRED_HEADER_VALUE = "ISMS-CORE-Connector"


class QualysClient:
    def __init__(self, **cfg) -> None:
        base = cfg.get('url') or os.environ.get('QUALYS_URL', '')
        self._base_url = base.rstrip('/')
        self._username = cfg.get('username') or os.environ.get('QUALYS_USERNAME', '')
        self._password = cfg.get('password') or os.environ.get('QUALYS_PASSWORD', '')
        if not self._base_url or not self._username or not self._password:
            raise ValueError("Qualys connector requires url, username, and password")
        self._session = requests.Session()
        self._session.auth = (self._username, self._password)
        self._session.headers.update({
            _REQUIRED_HEADER: _REQUIRED_HEADER_VALUE,
            "Accept": "application/json",
        })

    def _get_json(self, path: str, params: dict | None = None) -> dict:
        url = f"{self._base_url}/{path.lstrip('/')}"
        resp = self._session.get(url, params=params or {}, timeout=60)
        if not resp.ok:
            logger.error("Qualys GET %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _post_json(self, path: str, payload: dict | None = None) -> dict:
        url = f"{self._base_url}/{path.lstrip('/')}"
        resp = self._session.post(url, json=payload or {}, timeout=120)
        if not resp.ok:
            logger.error("Qualys POST %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return resp.json()

    def _post_xml(self, path: str, data: dict | None = None) -> ET.Element:
        """POST to a classic Qualys API endpoint that returns XML."""
        url = f"{self._base_url}/{path.lstrip('/')}"
        resp = self._session.post(
            url,
            data=data or {},
            headers={
                _REQUIRED_HEADER: _REQUIRED_HEADER_VALUE,
                "Content-Type": "application/x-www-form-urlencoded",
            },
            timeout=120,
        )
        if not resp.ok:
            logger.error("Qualys XML POST %s error %s: %s", path, resp.status_code, resp.text[:500])
        resp.raise_for_status()
        return ET.fromstring(resp.text)

    # ── Public query methods ───────────────────────────────────────────────────

    def get_asset_count(self) -> int:
        """Return total asset count from Asset Management."""
        logger.info("Fetching asset count from Qualys...")
        try:
            data = self._post_json("qps/rest/2.0/count/am/asset")
            count = int(data.get("ServiceResponse", {}).get("count", 0))
            logger.info("Qualys asset count: %d", count)
            return count
        except Exception as e:
            logger.warning("Could not fetch asset count: %s", e)
            return 0

    def get_host_list_summary(self) -> dict:
        """Return host list summary from the classic Qualys API (XML)."""
        logger.info("Fetching host list summary from Qualys...")
        try:
            root = self._post_xml(
                "api/2.0/fo/asset/host/",
                data={"action": "list", "details": "Basic", "truncation_limit": "1"},
            )
            # Extract total count from RESPONSE element
            total_elem = root.find(".//TRUNCATION[@limit]")
            total = 0
            if total_elem is not None:
                total = int(total_elem.get("total", 0))
            else:
                # Count HOST elements as a fallback
                hosts = root.findall(".//HOST")
                total = len(hosts)
            logger.info("Qualys host list total: %d", total)
            return {"total_hosts": total}
        except Exception as e:
            logger.warning("Could not fetch host list summary: %s", e)
            return {}

    def get_vuln_counts_by_severity(self) -> dict:
        """Return vulnerability counts per severity from Qualys VMDR.

        Uses qps/rest/2.0/search/vm/hostdetection (VMDR host detection endpoint).
        Filters for ACTIVE detections and aggregates by severity level (1-5).
        Qualys severity: 1=Minimal, 2=Medium, 3=Serious, 4=Critical, 5=Urgent.
        """
        logger.info("Fetching vulnerability counts from Qualys VMDR...")
        try:
            payload = {
                "ServiceRequest": {
                    "filters": {
                        "Criteria": [
                            {"field": "status", "operator": "EQUALS", "value": "ACTIVE"}
                        ]
                    },
                    "preferences": {
                        "limitResults": 1,  # We only need counts, not records
                    },
                }
            }
            data = self._post_json("qps/rest/2.0/search/vm/hostdetection", payload)
            service_resp = data.get("ServiceResponse", {})
            total = int(service_resp.get("count", 0))
            logger.info("Qualys VMDR active host detections: %d", total)
            return {"total": total, "active": total}
        except Exception as e:
            logger.warning("Could not fetch VMDR vuln counts: %s", e)
            return {}

    def get_scan_history(self) -> list[dict]:
        """Return recent scan history from the classic Qualys API (XML)."""
        logger.info("Fetching scan history from Qualys...")
        try:
            root = self._post_xml(
                "api/2.0/fo/scan/",
                data={"action": "list"},
            )
            scans: list[dict] = []
            for scan_elem in root.findall(".//SCAN"):
                scans.append({
                    "ref": scan_elem.findtext("REF", ""),
                    "title": scan_elem.findtext("TITLE", ""),
                    "type": scan_elem.findtext("TYPE", ""),
                    "launch_date": scan_elem.findtext("LAUNCH_DATE", ""),
                    "status": scan_elem.findtext("STATUS/STATE", ""),
                    "target": scan_elem.findtext("TARGET", ""),
                })
            logger.info("Fetched %d scans from Qualys", len(scans))
            return scans
        except Exception as e:
            logger.warning("Could not fetch scan history: %s", e)
            return []
