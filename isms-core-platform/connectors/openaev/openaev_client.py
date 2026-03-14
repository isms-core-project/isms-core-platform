"""OpenAEV REST API client (Filigran adversary emulation platform).

OpenAEV (Open Adversary Emulation & Validation) is the third product in the
Filigran XTM suite. It plans and runs purple team / tabletop exercises with
MITRE ATT&CK-mapped scenarios.

REST API: Spring Boot backend, OpenAPI spec at /v3/api-docs on a running instance.
Auth: Authorization: bearer <token>  (note: lowercase 'bearer')

Reference: github.com/OpenAEV-Platform/openaev

Environment variables:
  OPENAEV_URL          — e.g. https://openaev.corp.local
  OPENAEV_TOKEN        — API token (Profile → API key)
  OPENAEV_VERIFY_SSL   — "false" to skip cert check (default: true)
  OPENAEV_MAX_EXERCISES — max completed exercises to fetch (default: 20)
"""

import logging
import os

import requests
import urllib3

logger = logging.getLogger(__name__)


class OpenAEVClient:
    """REST client for the OpenAEV API."""

    def __init__(self, **cfg) -> None:
        self.base_url = (cfg.get('url') or os.environ["OPENAEV_URL"]).rstrip("/")
        self.token = cfg.get('token') or os.environ["OPENAEV_TOKEN"]
        self.verify_ssl = (cfg.get('verify_ssl') or os.environ.get("OPENAEV_VERIFY_SSL", "true")).lower() != "false"
        self.max_exercises = int(os.environ.get("OPENAEV_MAX_EXERCISES", "20"))

        if not self.verify_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for OpenAEV")

        self._session = requests.Session()
        self._session.verify = self.verify_ssl
        # OpenAEV uses lowercase 'bearer'
        self._session.headers.update({
            "Authorization": f"bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    # ── API helpers ───────────────────────────────────────────────────────────

    def _get(self, path: str, params: dict | None = None) -> dict | list:
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        resp = self._session.get(url, params=params, timeout=60)
        resp.raise_for_status()
        return resp.json()

    def _post(self, path: str, body: dict) -> dict | list:
        url = f"{self.base_url}/api/{path.lstrip('/')}"
        resp = self._session.post(url, json=body, timeout=60)
        resp.raise_for_status()
        return resp.json()

    # ── Exercises ─────────────────────────────────────────────────────────────

    def get_exercises(self) -> list[dict]:
        """GET /api/exercises — list completed simulation exercises."""
        # Spring Data pagination: page=0, size=N
        result = self._get("exercises", params={
            "status": "FINISHED",
            "page": 0,
            "size": self.max_exercises,
            "sort": "exercise_start_date,desc",
        })
        # Spring returns {content: [...], totalElements: N, ...} or just a list
        if isinstance(result, dict):
            return result.get("content") or result.get("exercises") or []
        return result if isinstance(result, list) else []

    def get_exercise_results(self, exercise_id: str) -> dict:
        """GET /api/exercises/{id}/results — scores and metrics."""
        try:
            result = self._get(f"exercises/{exercise_id}/results")
            return result if isinstance(result, dict) else {}
        except Exception as e:
            logger.warning("Could not fetch results for exercise %s: %s", exercise_id, e)
            return {}

    def get_exercise_attack_patterns(self, exercise_id: str) -> list[dict]:
        """GET /api/exercises/{id}/injects/results-by-attack-patterns — MITRE mapping."""
        try:
            result = self._get(f"exercises/{exercise_id}/injects/results-by-attack-patterns")
            return result if isinstance(result, list) else []
        except Exception as e:
            logger.warning("Could not fetch ATT&CK patterns for exercise %s: %s", exercise_id, e)
            return []

    def get_exercise_reports(self, exercise_id: str) -> list[dict]:
        """GET /api/exercises/{id}/reports — attached reports."""
        try:
            result = self._get(f"exercises/{exercise_id}/reports")
            return result if isinstance(result, list) else []
        except Exception as e:
            logger.warning("Could not fetch reports for exercise %s: %s", exercise_id, e)
            return []

    def get_findings(self) -> list[dict]:
        """GET /api/findings — findings across all exercises."""
        try:
            result = self._get("findings", params={"page": 0, "size": 200})
            if isinstance(result, dict):
                return result.get("content") or []
            return result if isinstance(result, list) else []
        except Exception as e:
            logger.warning("Could not fetch findings: %s", e)
            return []
