"""Shared DB connection and helpers for the feeds container."""

import logging
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from uuid import uuid4

import psycopg2
import psycopg2.extras

try:
    import requests as _requests
except ImportError:
    _requests = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)

DATABASE_URL = os.environ["DATABASE_URL"]


@contextmanager
def get_conn():
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = False
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def start_run(feed_name: str) -> str:
    """Insert a feed_run row with status=running, return its UUID."""
    run_id = str(uuid4())
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO feed_runs (id, feed_name, status, started_at)
                VALUES (%s, %s, 'running', %s)
                """,
                (run_id, feed_name, datetime.now(timezone.utc)),
            )
    return run_id


def finish_run(run_id: str, item_count: int) -> None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE feed_runs
                SET status='success', finished_at=%s, item_count=%s
                WHERE id=%s
                """,
                (datetime.now(timezone.utc), item_count, run_id),
            )


def _notify_backend_feed_failure(feed_name: str, error: str, run_id: str) -> None:
    """Best-effort POST to backend to queue a failure notification email."""
    if _requests is None:
        return
    api_url = os.environ.get("ISMS_API_URL", "")
    secret = os.environ.get("CONNECTORS_WORKER_SECRET", "")
    if not api_url or not secret:
        return
    try:
        _requests.post(
            f"{api_url}/api/v1/feeds/internal/notify-failure",
            json={"feed_name": feed_name, "error_message": error, "run_id": run_id},
            headers={"Authorization": f"Bearer {secret}"},
            timeout=5,
        )
    except Exception as exc:
        logger.warning("Could not notify backend of feed failure: %s", exc)


def fail_run(run_id: str, error: str) -> None:
    feed_name = "unknown"
    with get_conn() as conn:
        with conn.cursor() as cur:
            # Resolve the feed name from the run record
            cur.execute("SELECT feed_name FROM feed_runs WHERE id=%s", (run_id,))
            row = cur.fetchone()
            if row:
                feed_name = row[0]
            cur.execute(
                """
                UPDATE feed_runs
                SET status='error', finished_at=%s, error_message=%s
                WHERE id=%s
                """,
                (datetime.now(timezone.utc), error[:2000], run_id),
            )
    _notify_backend_feed_failure(feed_name, error, run_id)


def get_platform_setting(key: str, default: str = "") -> str:
    """Read a value from platform_settings. Returns default if missing or on error."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT value FROM platform_settings WHERE key = %s", (key,)
                )
                row = cur.fetchone()
                return row[0] if row else default
    except Exception:
        return default
