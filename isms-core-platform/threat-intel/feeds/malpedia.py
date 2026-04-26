"""Malpedia feed — malware families and threat actors.

Primary source: MISP galaxy (GitHub, no key required)
  - https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters/malpedia.json
    → 3,600+ malware families with slugs (win.emotet format), aliases, descriptions
  - https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters/threat-actor.json
    → 900+ threat actors with country, motivation, aliases

The Malpedia API (malpedia.caad.fkie.fraunhofer.de/api) is invite-only and not used.

Pull schedule: weekly (Sunday 03:00 UTC) — static knowledge base, rarely changes.

What we do:
  1. GET MISP galaxy malpedia.json    → malware family list (slug, name, aliases, description)
  2. GET MISP galaxy threat-actor.json → actor list (name, country, motivation, description)
  3. Upsert everything into ti_malware_families + ti_actors
  4. Sync to ti-malpedia-families + ti-malpedia-actors OpenSearch indices

Slug formats (must match MISP galaxy tags in IOC correlation):
  families  → win.emotet, elf.mirai, android.banker  (Malpedia slug format)
  actors    → APT28, Lazarus Group, Fancy Bear        (galaxy value as-is)
"""

import json
import logging
import re
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, get_os_client, os_bulk_upsert, start_run

logger = logging.getLogger(__name__)

_MISP_GALAXY_BASE = "https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters"
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


def _fetch_galaxy(cluster: str) -> list[dict]:
    url = f"{_MISP_GALAXY_BASE}/{cluster}.json"
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        values = data.get("values") or []
        logger.info("MISP galaxy %s: %d entries fetched", cluster, len(values))
        return values
    except Exception as exc:
        logger.error("Failed to fetch MISP galaxy %s: %s", cluster, exc)
        return []


def _extract_mitre_tids_from_refs(refs: list) -> list[str]:
    """Extract ATT&CK TIDs from reference URLs (e.g. attack.mitre.org/techniques/T1055)."""
    tids = set()
    for ref in refs or []:
        tids.update(re.findall(r"T\d{4}(?:\.\d{3})?", str(ref)))
    return sorted(tids)


def run() -> None:
    run_id = start_run("malpedia")
    logger.info("Malpedia pull started (source: MISP galaxy)")

    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    # ── 1. Fetch and upsert actors (threat-actor galaxy) ────────────────────
    actor_entries = _fetch_galaxy("threat-actor")
    actors_upserted = 0
    actor_os_docs: list[dict] = []

    for entry in actor_entries:
        slug = (entry.get("value") or "").strip()
        if not slug:
            continue

        name = slug[:200]
        meta = entry.get("meta") or {}
        country = (meta.get("country") or "")[:5].upper() or None
        motivation = meta.get("cfr-type-of-incident") or meta.get("motive") or None
        if isinstance(motivation, list):
            motivation = motivation[0] if motivation else None
        desc = (entry.get("description") or "")[:4000] or None

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_actors (id, slug, name, country, motivation, description, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name        = EXCLUDED.name,
                          country     = EXCLUDED.country,
                          motivation  = EXCLUDED.motivation,
                          description = EXCLUDED.description,
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (str(uuid4()), slug, name, country, motivation, desc, now),
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

    # ── 2. Fetch and upsert families (malpedia galaxy) ──────────────────────
    family_entries = _fetch_galaxy("malpedia")
    if not family_entries:
        fail_run(run_id, "Empty family list from MISP galaxy")
        return

    families_upserted = 0
    family_os_docs: list[dict] = []

    for entry in family_entries:
        slug = (entry.get("value") or "").strip()
        if not slug:
            continue

        meta = entry.get("meta") or {}
        name = slug[:200]
        aliases = [a[:200] for a in (meta.get("synonyms") or []) if a]
        desc = (entry.get("description") or "")[:4000] or None
        mitre_tids = _extract_mitre_tids_from_refs(meta.get("refs") or [])

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
                          mitre_tids  = EXCLUDED.mitre_tids,
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (
                            str(uuid4()), slug, name,
                            json.dumps(aliases), desc,
                            json.dumps([]),
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
            "actor_slugs": [],
            "mitre_tids":  mitre_tids,
            "description": desc,
            "updated_at":  now_iso,
            "_os_id":      f"family:{slug}",
        })

    logger.info("Malpedia families upserted: %d", families_upserted)

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
