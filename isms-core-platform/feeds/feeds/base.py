"""Shared DB connection and helpers for the feeds container."""

import logging
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from uuid import uuid4

import psycopg2
import psycopg2.extras

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


def fail_run(run_id: str, error: str) -> None:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE feed_runs
                SET status='error', finished_at=%s, error_message=%s
                WHERE id=%s
                """,
                (datetime.now(timezone.utc), error[:2000], run_id),
            )
