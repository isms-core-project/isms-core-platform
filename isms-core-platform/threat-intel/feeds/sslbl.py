"""Abuse.ch SSL Blacklist — SSL certificate fingerprints used by C2 servers.

Source: https://sslbl.abuse.ch/blacklist/sslblacklist.csv
Pull schedule: daily (04:00 UTC). No API key required.

CSV format (after # comment lines):
  Listingdate,SHA1,Reason
~300K entries — SHA1 fingerprints of TLS certificates observed on C2 servers.
"""

import json
import logging
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_URL      = "https://sslbl.abuse.ch/blacklist/sslblacklist.csv"
_OS_INDEX = "ti-sslbl"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "sha1":       {"type": "keyword"},
            "reason":     {"type": "keyword"},
            "listed_at":  {"type": "date"},
            "indexed_at": {"type": "date"},
        }
    }
}


def run() -> None:
    run_id = start_run("sslbl")
    logger.info("SSL Blacklist pull started")

    try:
        resp = requests.get(
            _URL,
            headers={"User-Agent": "ISMS-CORE-TI/1.0"},
            timeout=60,
        )
        resp.raise_for_status()
        text = resp.text
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("SSLBL download failed: %s", exc)
        return

    # Filter comment/empty lines — data lines: Listingdate,SHA1,Reason
    data_lines = [l for l in text.splitlines() if l and not l.startswith("#")]
    if not data_lines:
        logger.info("SSLBL: no entries in current blacklist (raw head: %.120s)", text)
        finish_run(run_id, 0)
        return

    logger.info("SSLBL: %d certificate fingerprints to process", len(data_lines))

    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    upserted = 0
    os_docs: list[dict] = []

    os_client = get_os_client()
    if os_client:
        try:
            if not os_client.indices.exists(index=_OS_INDEX):
                os_client.indices.create(index=_OS_INDEX, body=_OS_MAPPING)
                logger.info("Created OpenSearch index: %s", _OS_INDEX)
        except Exception as exc:
            logger.warning("OpenSearch index setup failed: %s", exc)
            os_client = None

    with get_conn() as conn:
        with conn.cursor() as cur:
            for line in data_lines:
                if is_cancelled("sslbl"):
                    logger.info("SSLBL cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                parts = line.split(",")
                if len(parts) < 2:
                    continue

                date_s = parts[0].strip()
                sha1   = parts[1].strip().lower()
                reason = parts[2].strip() if len(parts) > 2 else ""

                if not sha1 or len(sha1) != 40:
                    continue

                try:
                    listed_at = datetime.strptime(date_s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                except Exception:
                    listed_at = now

                family_slugs = [reason.lower().replace(" ", "_")] if reason else []
                tags = ["c2-certificate", "ssl-blacklist"] + ([reason] if reason else [])

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at, raw)
                    VALUES (%s,'sha1',%s,'sslbl',75,%s,'[]'::jsonb,%s,'[]'::jsonb,'[]'::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      last_seen = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (str(uuid4()), sha1,
                     json.dumps(tags), json.dumps(family_slugs),
                     listed_at, now, now,
                     json.dumps({"reason": reason})),
                )
                upserted += 1

                os_docs.append({
                    "sha1":       sha1,
                    "reason":     reason or None,
                    "listed_at":  listed_at.isoformat(),
                    "indexed_at": now_iso,
                    "_os_id":     f"sslbl:{sha1}",
                })

                if len(os_docs) >= 2000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("SSL Blacklist completed: %d SHA1 fingerprints upserted", upserted)
