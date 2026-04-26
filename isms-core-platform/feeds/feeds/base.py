"""Shared DB connection and helpers for the feeds container."""

import logging
import os
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from uuid import uuid4

# ── Cancellation flags (set by trigger_server, checked by feed loops) ─────────

_cancel_flags: dict[str, threading.Event] = {}
_cancel_lock = threading.Lock()


def get_cancel_flag(feed_name: str) -> threading.Event:
    with _cancel_lock:
        return _cancel_flags.setdefault(feed_name, threading.Event())


def is_cancelled(feed_name: str) -> bool:
    return _cancel_flags.get(feed_name, threading.Event()).is_set()


def set_cancelled(feed_name: str) -> None:
    get_cancel_flag(feed_name).set()


def clear_cancelled(feed_name: str) -> None:
    flag = _cancel_flags.get(feed_name)
    if flag:
        flag.clear()

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
        logger.warning("Feed failure notification skipped: requests library not available")
        return
    api_url = os.environ.get("ISMS_API_URL", "")
    secret = os.environ.get("CONNECTORS_WORKER_SECRET", "")
    if not api_url:
        logger.warning("Feed failure notification skipped: ISMS_API_URL not set")
        return
    if not secret:
        logger.warning("Feed failure notification skipped: CONNECTORS_WORKER_SECRET not set")
        return
    try:
        resp = _requests.post(
            f"{api_url}/api/v1/feeds/internal/notify-failure",
            json={"feed_name": feed_name, "error_message": error, "run_id": run_id},
            headers={"Authorization": f"Bearer {secret}"},
            timeout=10,
        )
        if resp.status_code == 200:
            logger.info("Feed failure notification queued for %s (run %s)", feed_name, run_id)
        else:
            logger.warning(
                "Feed failure notification rejected by backend: HTTP %s — %s",
                resp.status_code, resp.text[:200],
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


def has_successful_run(feed_name_prefix: str) -> bool:
    """Return True if at least one successful run exists for this feed (prefix match)."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT 1 FROM feed_runs WHERE feed_name LIKE %s AND status='success' LIMIT 1",
                    (feed_name_prefix + "%",),
                )
                return cur.fetchone() is not None
    except Exception:
        return False


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
