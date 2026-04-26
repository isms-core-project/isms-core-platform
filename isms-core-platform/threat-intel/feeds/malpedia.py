"""Malpedia feed — malware families and threat actors.

Source: https://malpedia.caad.fkie.fraunhofer.de/api/
Requires: MALPEDIA_API_KEY (free registration)

Pull schedule: weekly (Sunday 03:00 UTC) — static knowledge base, rarely changes.

What we do:
  1. GET /api/list/families     → full family slug list
  2. GET /api/get/family/{slug} → details (aliases, description, actors, ATT&CK TIDs)
  3. GET /api/list/actors       → actor list with metadata
  4. Upsert everything into ti_malware_families + ti_actors
  5. Sync to ti-malpedia-families + ti-malpedia-actors OpenSearch indices
"""

import json
import logging
import os
import time
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, get_os_client, os_bulk_upsert, start_run

logger = logging.getLogger(__name__)

_API_BASE = "https://malpedia.caad.fkie.fraunhofer.de/api"
_OS_INDEX_FAMILIES = "ti-malpedia-families"
_OS_INDEX_ACTORS   = "ti-malpedia-actors"

_OS_MAPPING_FAMILIES = {
    "mappings": {
        "properties": {
            "slug":        {"type": "keyword"},
            "name":        {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "aliases":     {"type": "keyword"},
            "actor_slugs": {"type": "keyword"},
            "mitre_tids":  {"type": "keyword"},
            "description": {"type": "text"},
            "updated_at":  {"type": "date"},
        }
    }
}

_OS_MAPPING_ACTORS = {
    "mappings": {
        "properties": {
            "slug":        {"type": "keyword"},
            "name":        {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "country":     {"type": "keyword"},
            "motivation":  {"type": "keyword"},
            "description": {"type": "text"},
            "updated_at":  {"type": "date"},
        }
    }
}


def _api_key() -> str | None:
    return os.environ.get("MALPEDIA_API_KEY") or None


def _headers() -> dict:
    key = _api_key()
    return {"Authorization": f"apitoken {key}"} if key else {}


def _get(path: str, retries: int = 3) -> dict | list | None:
    for attempt in range(retries):
        try:
            resp = requests.get(f"{_API_BASE}{path}", headers=_headers(), timeout=30)
            if resp.status_code == 401:
                logger.error("Malpedia: invalid API key")
                return None
            if resp.status_code == 429:
                wait = 60 * (attempt + 1)
                logger.warning("Malpedia rate limit — waiting %ds", wait)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as exc:
            logger.warning("Malpedia request failed (attempt %d): %s", attempt + 1, exc)
            if attempt < retries - 1:
                time.sleep(10)
    return None


def _extract_mitre_tids(family_detail: dict) -> list[str]:
    """Extract ATT&CK TIDs from Malpedia family detail (several possible locations)."""
    import re
    tids = set()
    # Common_Code_Snippets / ATT&CK section
    for entry in family_detail.get("cfr-suspected-victims", []) or []:
        pass  # not a TID source
    # Direct attack_id list
    for tid in family_detail.get("attack_id", []) or []:
        tids.add(tid)
    # Free-text description
    desc = family_detail.get("description") or ""
    tids.update(re.findall(r"T\d{4}(?:\.\d{3})?", desc))
    return sorted(tids)


def run() -> None:
    run_id = start_run("malpedia")
    logger.info("Malpedia pull started")

    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    # ── 1. Fetch actor list ──────────────────────────────────────────────────
    actor_data = _get("/list/actors") or {}
    actors_upserted = 0
    actor_os_docs: list[dict] = []

    for slug, meta in actor_data.items() if isinstance(actor_data, dict) else []:
        name = meta.get("value") or slug
        country = (meta.get("country") or "")[:5].upper() or None
        motivation = (meta.get("motivation") or [None])[0] if isinstance(meta.get("motivation"), list) else meta.get("motivation")
        desc = (meta.get("description") or "")[:4000] or None

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_actors (id, slug, name, country, motivation, description, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name = EXCLUDED.name,
                          country = EXCLUDED.country,
                          motivation = EXCLUDED.motivation,
                          description = EXCLUDED.description,
                          updated_at = EXCLUDED.updated_at
                        """,
                        (str(uuid4()), slug, name[:200], country, motivation, desc, now),
                    )
            actors_upserted += 1
        except Exception as exc:
            logger.warning("Actor upsert failed for %s: %s", slug, exc)

        actor_os_docs.append({
            "slug":        slug,
            "name":        name,
            "country":     country,
            "motivation":  motivation,
            "description": desc,
            "updated_at":  now_iso,
            "_os_id":      f"actor:{slug}",
        })

    logger.info("Malpedia actors upserted: %d", actors_upserted)

    # ── 2. Fetch family list ─────────────────────────────────────────────────
    family_list = _get("/list/families")
    if not isinstance(family_list, (list, dict)):
        fail_run(run_id, "Invalid family list response")
        return

    # API can return list of slugs or dict of {slug: meta}
    family_slugs = list(family_list.keys()) if isinstance(family_list, dict) else family_list

    families_upserted = 0
    family_os_docs: list[dict] = []

    for i, slug in enumerate(family_slugs):
        detail = _get(f"/get/family/{slug}")
        if not detail:
            continue

        name = (detail.get("common_name") or detail.get("name") or slug)[:200]
        aliases = [a[:200] for a in (detail.get("alt_names") or []) if a]
        desc = (detail.get("description") or "")[:4000] or None
        mitre_tids = _extract_mitre_tids(detail)
        # Actor slugs associated with this family
        fam_actor_slugs = [a if isinstance(a, str) else a.get("slug", "") for a in (detail.get("cfr-suspected-state-sponsor") or []) + (detail.get("actors") or [])]
        fam_actor_slugs = [a for a in fam_actor_slugs if a]

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_malware_families
                          (id, slug, name, aliases, description, actor_slugs, mitre_tids, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name        = EXCLUDED.name,
                          aliases     = EXCLUDED.aliases,
                          description = EXCLUDED.description,
                          actor_slugs = EXCLUDED.actor_slugs,
                          mitre_tids  = EXCLUDED.mitre_tids,
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (
                            str(uuid4()), slug, name,
                            json.dumps(aliases), desc,
                            json.dumps(fam_actor_slugs),
                            json.dumps(mitre_tids),
                            now,
                        ),
                    )
            families_upserted += 1
        except Exception as exc:
            logger.warning("Family upsert failed for %s: %s", slug, exc)

        family_os_docs.append({
            "slug":        slug,
            "name":        name,
            "aliases":     aliases,
            "actor_slugs": fam_actor_slugs,
            "mitre_tids":  mitre_tids,
            "description": desc,
            "updated_at":  now_iso,
            "_os_id":      f"family:{slug}",
        })

        # Rate limit — Malpedia free tier: be polite
        if (i + 1) % 50 == 0:
            logger.info("Malpedia: %d/%d families processed", i + 1, len(family_slugs))
            time.sleep(2)

    # ── 3. Sync to OpenSearch ────────────────────────────────────────────────
    os_client = get_os_client()
    if os_client:
        try:
            for idx, mapping in [(_OS_INDEX_FAMILIES, _OS_MAPPING_FAMILIES), (_OS_INDEX_ACTORS, _OS_MAPPING_ACTORS)]:
                if not os_client.indices.exists(index=idx):
                    os_client.indices.create(index=idx, body=mapping)
                    logger.info("Created OpenSearch index: %s", idx)
            if family_os_docs:
                os_bulk_upsert(os_client, _OS_INDEX_FAMILIES, family_os_docs, "_os_id")
            if actor_os_docs:
                os_bulk_upsert(os_client, _OS_INDEX_ACTORS, actor_os_docs, "_os_id")
        except Exception as exc:
            logger.warning("Malpedia → OpenSearch sync failed: %s", exc)

    total = families_upserted + actors_upserted
    finish_run(run_id, total)
    logger.info("Malpedia completed: %d families + %d actors upserted", families_upserted, actors_upserted)
