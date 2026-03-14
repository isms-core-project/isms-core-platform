"""GLPI REST API client.

Authentication: POST /initSession with header Authorization: user_token <api_token>
and App-Token: <app_token>. Returns a session_token used in subsequent requests.

Environment variables:
  GLPI_URL        — Base URL, e.g. http://glpi.corp.local
  GLPI_USER_TOKEN — GLPI user API token (generated in user profile)
  GLPI_APP_TOKEN  — GLPI application token (generated in API settings)

Minimum GLPI permissions for the service account:
  - Read access to Computers, Software, Tickets
  - No write access required
"""

import logging
import os

import requests

logger = logging.getLogger(__name__)


class GLPIClient:
    """Thin REST wrapper for the GLPI REST API."""

    def __init__(self, **cfg) -> None:
        self._base_url = (cfg.get('url') or os.environ.get("GLPI_URL", "")).rstrip("/") + "/apirest.php"
        if not self._base_url or self._base_url == "/apirest.php":
            raise ValueError("GLPI URL not set — provide GLPI_URL or url config key")
        self._user_token = cfg.get('user_token') or os.environ.get("GLPI_USER_TOKEN", "")
        self._app_token = cfg.get('app_token') or os.environ.get("GLPI_APP_TOKEN", "")
        if not self._user_token or not self._app_token:
            raise ValueError("Provide GLPI_USER_TOKEN and GLPI_APP_TOKEN (or user_token/app_token config keys)")
        self._session_token: str = ""
        self._session = requests.Session()
        self._init_session()

    # ── Auth ──────────────────────────────────────────────────────────────────

    def _init_session(self) -> None:
        """Obtain a GLPI session token via /initSession."""
        logger.info("Initialising GLPI session...")
        try:
            resp = self._session.post(
                f"{self._base_url}/initSession",
                headers={
                    "Authorization": f"user_token {self._user_token}",
                    "App-Token": self._app_token,
                    "Content-Type": "application/json",
                },
                timeout=15,
            )
            resp.raise_for_status()
            self._session_token = resp.json().get("session_token", "")
            if not self._session_token:
                raise RuntimeError("GLPI initSession returned no session_token")
            self._session.headers.update({
                "Session-Token": self._session_token,
                "App-Token": self._app_token,
                "Content-Type": "application/json",
            })
            logger.info("GLPI session established")
        except requests.HTTPError as e:
            logger.error("GLPI initSession HTTP %s: %s", e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("GLPI initSession failed: %s", e)
            raise

    def _get(self, path: str, params: dict | None = None) -> object:
        """Issue an authenticated GET request and return the parsed JSON body."""
        try:
            resp = self._session.get(
                f"{self._base_url}/{path.lstrip('/')}",
                params=params or {},
                timeout=30,
            )
            resp.raise_for_status()
            return resp.json()
        except requests.HTTPError as e:
            logger.error("GLPI GET %s HTTP %s: %s", path, e.response.status_code, e.response.text[:200])
            raise
        except Exception as e:
            logger.error("GLPI GET %s failed: %s", path, e)
            raise

    # ── Public query methods ──────────────────────────────────────────────────

    def get_computers(self, limit: int = 500) -> list[dict]:
        """Return computer assets with type and status expanded."""
        logger.info("Fetching computers from GLPI (limit=%d)...", limit)
        end = limit - 1
        result = self._get("Computer", {
            "range": f"0-{end}",
            "expand_dropdowns": 1,
        })
        computers = result if isinstance(result, list) else []
        logger.info("Fetched %d computers", len(computers))
        return computers

    def get_tickets(self, status: str = "open", limit: int = 200) -> list[dict]:
        """Return tickets. status='open' fetches new/in-progress tickets (status=1)."""
        logger.info("Fetching %s tickets from GLPI (limit=%d)...", status, limit)
        end = limit - 1
        # GLPI ticket status values: 1=new, 2=assigned, 3=planned, 4=waiting, 5=solved, 6=closed
        result = self._get("Ticket", {
            "range": f"0-{end}",
            "criteria[0][field]": 12,   # field 12 = status
            "criteria[0][searchtype]": "equals",
            "criteria[0][value]": 1,    # status = new
        })
        tickets = result if isinstance(result, list) else []
        logger.info("Fetched %d tickets", len(tickets))
        return tickets

    def get_software(self, limit: int = 1000) -> list[dict]:
        """Return software inventory."""
        logger.info("Fetching software from GLPI (limit=%d)...", limit)
        end = limit - 1
        result = self._get("Software", {
            "range": f"0-{end}",
            "expand_dropdowns": 1,
        })
        software = result if isinstance(result, list) else []
        logger.info("Fetched %d software records", len(software))
        return software
