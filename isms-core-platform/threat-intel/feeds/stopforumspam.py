"""Stopforumspam feed — spam/bot IP addresses (90-day combined IPv4+IPv6 list).

Source: https://www.stopforumspam.com/downloads/listed_ip_90_ipv46_all.gz
Pull schedule: daily (05:30 UTC). No API key required.
"""

import gzip
import logging
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_URL      = "https://www.stopforumspam.com/downloads/listed_ip_90_ipv46_all.gz"
_OS_INDEX = "ti-stopforumspam"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ip":         {"type": "ip"},
            "indexed_at": {"type": "date"},
        }
    }
}


def run() -> None:
    run_id = start_run("stopforumspam")
    logger.info("Stopforumspam pull started")

    try:
        resp = requests.get(_URL, timeout=120)
        resp.raise_for_status()
        lines = gzip.decompress(resp.content).decode("utf-8", errors="ignore").splitlines()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("Stopforumspam download failed: %s", exc)
        return

    # File format: "ip","frequency","lastseen" — parse all three fields
    entries: list[tuple[str, int, datetime]] = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip().strip('"') for p in line.split(",")]
        ip = parts[0] if parts else ""
        if not ip:
            continue
        try:
            freq = int(parts[1]) if len(parts) > 1 else 1
        except ValueError:
            freq = 1
        try:
            last = datetime.fromisoformat(parts[2].replace(" ", "T")) if len(parts) > 2 else None
            if last and last.tzinfo is None:
                last = last.replace(tzinfo=timezone.utc)
        except (ValueError, AttributeError):
            last = None
        entries.append((ip, freq, last))

    if not entries:
        fail_run(run_id, "Empty Stopforumspam response")
        return

    logger.info("Stopforumspam: %d IPs to process", len(entries))

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
            for ip, freq, last_seen_dt in entries:
                if is_cancelled("stopforumspam"):
                    logger.info("Stopforumspam cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                if not ip or len(ip) > 45:
                    continue

                # Confidence derived from sighting frequency (Wilson-style proxy)
                if freq >= 50:
                    confidence = 85
                elif freq >= 10:
                    confidence = 70
                elif freq >= 3:
                    confidence = 50
                else:
                    confidence = 30

                last_seen = last_seen_dt or now

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at)
                    VALUES (%s,'ip',%s,'stopforumspam',%s,
                            '["spam","botnet"]'::jsonb,'[]'::jsonb,
                            '[]'::jsonb,'[]'::jsonb,'[]'::jsonb,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      confidence = GREATEST(ti_iocs.confidence, EXCLUDED.confidence),
                      last_seen  = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (str(uuid4()), ip, confidence, now, last_seen, now),
                )
                upserted += 1

                os_docs.append({
                    "ip":         ip,
                    "indexed_at": now_iso,
                    "_os_id":     f"sfs:{ip}",
                })

                if len(os_docs) >= 2000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("Stopforumspam completed: %d IPs upserted", upserted)
