"""Abuse.ch URLhaus feed — currently active malicious URLs.

Source: https://urlhaus.abuse.ch/downloads/csv_online/
Pull schedule: daily (03:00 UTC). No API key required.

CSV columns: id,dateadded,url,url_status,last_online,threat,tags,urlhaus_link,reporter
Rows starting with '#' are comments and are skipped.
"""

import csv
import io
import json
import logging
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_URL      = "https://urlhaus.abuse.ch/downloads/csv_online/"
_OS_INDEX = "ti-urlhaus"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "url":        {"type": "keyword"},
            "url_status": {"type": "keyword"},
            "threat":     {"type": "keyword"},
            "tags":       {"type": "keyword"},
            "date_added": {"type": "date"},
            "indexed_at": {"type": "date"},
        }
    }
}


def run() -> None:
    run_id = start_run("urlhaus")
    logger.info("URLhaus pull started")

    try:
        resp = requests.get(_URL, headers={"User-Agent": "ISMS-CORE-TI/1.0"}, timeout=120)
        resp.raise_for_status()
        text = resp.text
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("URLhaus download failed: %s", exc)
        return

    # CSV rows starting with '#' are comment/header lines — skip them
    reader = csv.reader(filter(lambda row: not row.startswith("#"), io.StringIO(text)))
    rows = list(reader)
    if not rows:
        logger.info("URLhaus: no active URLs in feed")
        finish_run(run_id, 0)
        return

    logger.info("URLhaus: %d active URLs to process", len(rows))

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
            for row in rows:
                if is_cancelled("urlhaus"):
                    logger.info("URLhaus cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                # id,dateadded,url,url_status,last_online,threat,tags,urlhaus_link,reporter
                if len(row) < 3:
                    continue
                url_val    = row[2].strip()
                url_status = row[3].strip() if len(row) > 3 else ""
                threat     = row[5].strip() if len(row) > 5 else ""
                tags_raw   = row[6].strip() if len(row) > 6 else ""
                date_s     = row[1].strip() if len(row) > 1 else ""

                if not url_val:
                    continue

                tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []
                if threat:
                    tags = list(dict.fromkeys([threat] + tags))

                family_slugs = [threat.lower().replace(" ", "_")] if threat else []

                try:
                    first_seen = datetime.strptime(date_s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc) if date_s else now
                except Exception:
                    first_seen = now

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at, raw)
                    VALUES (%s,'url',%s,'urlhaus',90,%s,'[]'::jsonb,%s,'[]'::jsonb,'[]'::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      tags         = COALESCE((
                          SELECT jsonb_agg(DISTINCT elem)
                          FROM jsonb_array_elements(ti_iocs.tags || EXCLUDED.tags) elem
                      ), '[]'::jsonb),
                      family_slugs = COALESCE((
                          SELECT jsonb_agg(DISTINCT elem)
                          FROM jsonb_array_elements(ti_iocs.family_slugs || EXCLUDED.family_slugs) elem
                      ), '[]'::jsonb),
                      last_seen    = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen),
                      raw          = EXCLUDED.raw
                    """,
                    (
                        str(uuid4()), url_val,
                        json.dumps(tags),
                        json.dumps(family_slugs),
                        first_seen, now, now,
                        json.dumps({"status": url_status, "threat": threat}),
                    ),
                )
                upserted += 1

                os_docs.append({
                    "url":        url_val,
                    "url_status": url_status,
                    "threat":     threat,
                    "tags":       tags,
                    "date_added": first_seen.isoformat(),
                    "indexed_at": now_iso,
                    "_os_id":     f"urlhaus:{url_val[:400]}",
                })

                if len(os_docs) >= 1000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("URLhaus completed: %d URLs upserted", upserted)
