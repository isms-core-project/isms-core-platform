"""PRTG Network Monitor REST API client.

PRTG exposes a JSON API at /api/table.json for all object types.
Authentication: API token (recommended) or username + password hash.

Environment variables:
  PRTG_URL        — Base URL, e.g. https://prtg.corp.local
  PRTG_API_TOKEN  — API token from ISMS service account (preferred)
  PRTG_USERNAME   — Username (used if no API token)
  PRTG_PASSWORD   — Password (used if no API token)
  PRTG_VERIFY_SSL — "false" to skip cert verification for self-signed certs (default: true)

PRTG device status codes:
  1=Unknown  2=Scanning  3=Up  4=Warning  5=Down  6=No Probe
  7=Paused(User)  8=Paused(Dependency)  9=Paused(Schedule)
  10=Unusual  11=Not Licensed  12=Paused Until  13=Down Ack  14=Down Partial
"""

import logging
import os
from datetime import datetime, timezone

import requests
import urllib3

logger = logging.getLogger(__name__)

# Status codes that mean the device/sensor is reachable
STATUS_OK = {2, 3, 10}       # Scanning, Up, Unusual (data anomaly but reachable)
STATUS_WARNING = {4, 13, 14}  # Warning, Down Acknowledged, Down Partial
STATUS_DOWN = {1, 5, 6}       # Unknown, Down, No Probe
STATUS_PAUSED = {7, 8, 9, 11, 12}  # Any paused variant


def _parse_status(status_raw: str | int) -> str:
    """Normalise PRTG integer or string status to up/warning/down/paused."""
    try:
        code = int(status_raw)
    except (TypeError, ValueError):
        return "unknown"
    if code in STATUS_OK:
        return "up"
    if code in STATUS_WARNING:
        return "warning"
    if code in STATUS_DOWN:
        return "down"
    if code in STATUS_PAUSED:
        return "paused"
    return "unknown"


class PRTGClient:
    """Thin REST wrapper for the PRTG Network Monitor JSON API."""

    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get('url') or os.environ["PRTG_URL"]).rstrip("/")
        self.verify_ssl = (cfg.get('verify_ssl') or os.environ.get("PRTG_VERIFY_SSL", "true")).lower() != "false"

        self._api_token = cfg.get('api_token') or os.environ.get("PRTG_API_TOKEN", "")
        self._username = cfg.get('username') or os.environ.get("PRTG_USERNAME", "")
        self._password = cfg.get('password') or os.environ.get("PRTG_PASSWORD", "")

        if not self._api_token and not (self._username and self._password):
            raise ValueError("Provide PRTG_API_TOKEN or both PRTG_USERNAME and PRTG_PASSWORD")

        self._session = requests.Session()
        self._session.verify = self.verify_ssl

        if not self.verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _auth_params(self) -> dict:
        if self._api_token:
            return {"apitoken": self._api_token}
        return {"username": self._username, "password": self._password}

    def _get_table(self, content: str, columns: list[str], count: int = 50000) -> list[dict]:
        """Generic table query — returns rows as plain dicts."""
        params = {
            "content": content,
            "columns": ",".join(columns),
            "count": count,
            "output": "json",
            **self._auth_params(),
        }
        try:
            resp = self._session.get(
                f"{self.base_url}/api/table.json",
                params=params,
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get(content, [])
        except requests.HTTPError as e:
            logger.error("PRTG API HTTP %s: %s", e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("PRTG API request failed: %s", e)
            raise

    # ── Public methods ─────────────────────────────────────────────────────────

    def get_devices(self) -> list[dict]:
        """Return all monitored devices with status."""
        logger.info("Fetching devices from PRTG...")
        rows = self._get_table(
            "devices",
            ["objid", "device", "host", "active", "status", "status_raw", "message_raw",
             "location", "group", "probe"],
        )
        devices = []
        for r in rows:
            devices.append({
                "id": r.get("objid"),
                "name": r.get("device", ""),
                "host": r.get("host", ""),
                "active": r.get("active", True),
                "status": _parse_status(r.get("status_raw", r.get("status", 0))),
                "status_raw": r.get("status_raw"),
                "message": r.get("message_raw", ""),
                "location": r.get("location", ""),
                "group": r.get("group", ""),
                "probe": r.get("probe", ""),
            })
        logger.info("Fetched %d devices", len(devices))
        return devices

    def get_sensors(self) -> list[dict]:
        """Return all sensors with status."""
        logger.info("Fetching sensors from PRTG...")
        rows = self._get_table(
            "sensors",
            ["objid", "sensor", "device", "status", "status_raw", "message_raw",
             "priority", "lastvalue_raw", "group"],
        )
        sensors = []
        for r in rows:
            sensors.append({
                "id": r.get("objid"),
                "name": r.get("sensor", ""),
                "device": r.get("device", ""),
                "group": r.get("group", ""),
                "status": _parse_status(r.get("status_raw", r.get("status", 0))),
                "status_raw": r.get("status_raw"),
                "message": r.get("message_raw", ""),
                "priority": r.get("priority", 3),
                "last_value": r.get("lastvalue_raw"),
            })
        logger.info("Fetched %d sensors", len(sensors))
        return sensors

    def get_active_alarms(self) -> list[dict]:
        """Return currently active/acknowledged alarms."""
        logger.info("Fetching active alarms from PRTG...")
        try:
            rows = self._get_table(
                "alarms",
                ["objid", "sensor", "device", "status", "status_raw", "message_raw",
                 "priority", "datetime"],
            )
        except Exception:
            logger.warning("Could not fetch alarms — returning empty list")
            return []

        alarms = []
        for r in rows:
            alarms.append({
                "id": r.get("objid"),
                "sensor": r.get("sensor", ""),
                "device": r.get("device", ""),
                "status": _parse_status(r.get("status_raw", r.get("status", 0))),
                "message": r.get("message_raw", ""),
                "priority": r.get("priority", 3),
                "datetime": r.get("datetime", ""),
            })
        logger.info("Fetched %d active alarms", len(alarms))
        return alarms

    def get_server_info(self) -> dict:
        """Return PRTG server version info (best-effort)."""
        try:
            params = {"output": "json", **self._auth_params()}
            resp = self._session.get(f"{self.base_url}/api/status.json", params=params, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            logger.warning("Could not fetch PRTG server info: %s", e)
            return {}
