"""FIRST EPSS (Exploit Prediction Scoring System) feed.

Source: https://api.first.org/data/v1/epss?limit=5000&order=!epss

Stores the top 5 000 CVEs by EPSS score.  Scores are updated daily by FIRST.
"""

import logging
from datetime import date, datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

EPSS_URL = "https://api.first.org/data/v1/epss?limit=5000&order=!epss"


def run() -> None:
    run_id = start_run("epss")
    logger.info("FIRST EPSS pull started")

    try:
        resp = requests.get(EPSS_URL, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("EPSS download failed: %s", exc)
        return

    items = (payload.get("data") or [])
    if not items:
        fail_run(run_id, "Empty data in EPSS response")
        return

    # Date of the score set (included in response header as X-EPSS-Updated)
    score_date: date | None = None
    try:
        ts = payload.get("timestamp")
        if ts:
            score_date = datetime.fromisoformat(ts[:10]).date()
    except Exception:
        score_date = date.today()

    now = datetime.now(timezone.utc)
    upserted = 0

    with get_conn() as conn:
        with conn.cursor() as cur:
            for item in items:
                cve_id = item.get("cve") or ""
                if not cve_id:
                    continue
                try:
                    score = float(item.get("epss", 0))
                    percentile = float(item.get("percentile", 0))
                except (ValueError, TypeError):
                    continue

                cur.execute(
                    """
                    INSERT INTO epss_scores
                      (id, cve_id, score, percentile, score_date, created_at, updated_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (cve_id) DO UPDATE SET
                      score      = EXCLUDED.score,
                      percentile = EXCLUDED.percentile,
                      score_date = EXCLUDED.score_date,
                      updated_at = EXCLUDED.updated_at
                    """,
                    (str(uuid4()), cve_id, score, percentile, score_date, now, now),
                )
                upserted += 1

    finish_run(run_id, upserted)
    logger.info("FIRST EPSS completed: %d scores upserted", upserted)
