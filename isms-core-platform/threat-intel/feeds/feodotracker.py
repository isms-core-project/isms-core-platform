"""Abuse.ch Feodo Tracker — active botnet C2 server IPs.

Source: https://feodotracker.abuse.ch/downloads/ipblocklist.csv
Pull schedule: every 6 hours. No API key required.

CSV format (after # comment lines):
  first_seen_utc,dst_ip,dst_port,c2_status,last_online,malware
~1,000–3,000 active C2 IPs with malware family attribution.
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

_URL      = "https://feodotracker.abuse.ch/downloads/ipblocklist.csv"
_OS_INDEX = "ti-feodotracker"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ip":           {"type": "ip"},
            "port":         {"type": "integer"},
            "c2_status":    {"type": "keyword"},
            "malware":      {"type": "keyword"},
            "first_seen":   {"type": "date"},
            "last_online":  {"type": "date"},
            "indexed_at":   {"type": "date"},
        }
    }
}


def run() -> None:
    run_id = start_run("feodotracker")
    logger.info("Feodo Tracker pull started")

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
        logger.error("Feodo Tracker download failed: %s", exc)
        return

    clean_lines = [l for l in text.splitlines() if l and not l.startswith("#") and not l.startswith("first_seen_utc")]
    if not clean_lines:
        logger.info("Feodo Tracker: no entries in current blocklist")
        finish_run(run_id, 0)
        return

    rows = list(csv.reader(io.StringIO("\n".join(clean_lines))))
    logger.info("Feodo Tracker: %d C2 IPs to process", len(rows))

    now      = datetime.now(timezone.utc)
    now_iso  = now.isoformat()
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
            for parts in rows:
                if is_cancelled("feodotracker"):
                    logger.info("Feodo Tracker cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                if len(parts) < 2:
                    continue

                first_seen_s  = parts[0].strip()
                ip            = parts[1].strip()
                port_s        = parts[2].strip() if len(parts) > 2 else ""
                c2_status     = parts[3].strip() if len(parts) > 3 else ""
                last_online_s = parts[4].strip() if len(parts) > 4 else ""
                malware       = parts[5].strip() if len(parts) > 5 else ""

                if not ip or not ip[0].isdigit():
                    continue

                try:
                    port = int(port_s) if port_s else None
                except ValueError:
                    port = None

                try:
                    first_seen = datetime.strptime(first_seen_s, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
                except Exception:
                    first_seen = now

                try:
                    last_online = datetime.strptime(last_online_s, "%Y-%m-%d").replace(tzinfo=timezone.utc) if last_online_s else None
                except Exception:
                    last_online = None

                family_slugs = [malware.lower().replace(" ", "_").replace("-", "_")] if malware else []
                tags = ["c2", "botnet", "feodo-tracker"] + ([malware] if malware else []) + ([c2_status] if c2_status else [])

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at, raw)
                    VALUES (%s,'ip',%s,'feodotracker',85,%s,'[]'::jsonb,%s,'[]'::jsonb,'[]'::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      tags         = COALESCE((
                          SELECT jsonb_agg(DISTINCT elem)
                          FROM jsonb_array_elements(ti_iocs.tags || EXCLUDED.tags) elem
                      ), '[]'::jsonb),
                      family_slugs = COALESCE((
                          SELECT jsonb_agg(DISTINCT elem)
                          FROM jsonb_array_elements(ti_iocs.family_slugs || EXCLUDED.family_slugs) elem
                      ), '[]'::jsonb),
                      last_seen    = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (str(uuid4()), ip,
                     json.dumps(tags), json.dumps(family_slugs),
                     first_seen, now, now,
                     json.dumps({"port": port, "c2_status": c2_status, "malware": malware})),
                )
                upserted += 1

                os_doc: dict = {
                    "ip":         ip,
                    "c2_status":  c2_status or None,
                    "malware":    malware or None,
                    "first_seen": first_seen.isoformat(),
                    "indexed_at": now_iso,
                    "_os_id":     f"feodo:{ip}",
                }
                if port:
                    os_doc["port"] = port
                if last_online:
                    os_doc["last_online"] = last_online.isoformat()
                os_docs.append(os_doc)

                if len(os_docs) >= 1000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("Feodo Tracker completed: %d C2 IPs upserted", upserted)
