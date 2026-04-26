"""Malpedia feed — malware families and threat actors.

Primary source: Malpedia public API (no key required)
  https://malpedia.caad.fkie.fraunhofer.de/api
  - list/families         → canonical slug list (~5 000 entries)
  - get/family/{slug}     → common_name, alt_names, description, urls
                            (fetched only for families NOT in MISP galaxy)
  - list/actors           → canonical actor slug list (~1 300 entries)
  - get/actor/{slug}      → aliases, country, motivation, malware_families links

Secondary source: MISP galaxy (GitHub, no key required)
  - clusters/malpedia.json      → bulk descriptions + ATT&CK TIDs from refs
  - clusters/threat-actor.json  → country/motivation supplement + IOC-correlation slugs

Pull schedule: weekly (Sunday 03:00 UTC).

Actor slug compatibility:
  MISP IOC events tag actors as misp-galaxy:threat-actor="APT28".
  MISP galaxy value ("APT28") is used as the DB slug for IOC correlation.
  Malpedia API actors not in MISP galaxy use the Malpedia slug (apt28).
"""

import json
import logging
import re
import time
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_MISP_GALAXY_BASE = "https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters"
_MALPEDIA_API    = "https://malpedia.caad.fkie.fraunhofer.de/api"
_API_DELAY       = 0.15   # seconds between individual API calls

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
    """Fetch MISP galaxy cluster (secondary source — bulk descriptions + TID refs)."""
    url = f"{_MISP_GALAXY_BASE}/{cluster}.json"
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        values = resp.json().get("values") or []
        logger.info("MISP galaxy %s: %d entries", cluster, len(values))
        return values
    except Exception as exc:
        logger.error("Failed to fetch MISP galaxy %s: %s", cluster, exc)
        return []


def _malpedia(path: str) -> dict | list | None:
    """GET from Malpedia public API. Returns None on error."""
    try:
        time.sleep(_API_DELAY)
        resp = requests.get(f"{_MALPEDIA_API}/{path}", timeout=30)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        logger.warning("Malpedia API %s: %s", path, exc)
        return None


def _extract_mitre_tids(urls: list) -> list[str]:
    """Extract ATT&CK TIDs from a list of URLs (e.g. attack.mitre.org/techniques/T1055)."""
    tids = set()
    for u in urls or []:
        tids.update(re.findall(r"T\d{4}(?:\.\d{3})?", str(u)))
    return sorted(tids)


def _to_api_slug(misp_value: str) -> str:
    """Convert MISP galaxy actor value to Malpedia API slug format (APT28 → apt28)."""
    return misp_value.lower().replace(" ", "_").replace("-", "_")


def run() -> None:
    run_id = start_run("malpedia")
    logger.info("Malpedia pull started (primary: Malpedia API, secondary: MISP galaxy)")

    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    # ── 1. Secondary: MISP galaxy lookup dicts ───────────────────────────────
    # Families: slug → entry (for bulk descriptions + ATT&CK TIDs)
    galaxy_family: dict[str, dict] = {}
    for entry in _fetch_galaxy("malpedia"):
        slug = (entry.get("value") or "").strip()
        if re.match(r"^[a-z]+\.[a-z0-9_]+$", slug):
            galaxy_family[slug] = entry

    # Actors: api_slug → MISP value (for IOC-correlation slug and country/motivation)
    galaxy_actor_by_api: dict[str, dict] = {}   # api_slug   → entry
    galaxy_actor_by_val: dict[str, dict] = {}   # misp_value → entry
    for entry in _fetch_galaxy("threat-actor"):
        value = (entry.get("value") or "").strip()
        if value:
            galaxy_actor_by_val[value] = entry
            galaxy_actor_by_api[_to_api_slug(value)] = entry

    # ── 2. Primary: Malpedia family list ─────────────────────────────────────
    family_slugs: list[str] = _malpedia("list/families") or []
    if not family_slugs:
        fail_run(run_id, "Empty family list from Malpedia API")
        return
    logger.info("Malpedia API families: %d slugs", len(family_slugs))

    # DB cleanup — remove non-slug entries from earlier runs
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM ti_malware_families WHERE slug !~ '^[a-z]+\\.[a-z0-9_]+$'"
                )
                if cur.rowcount:
                    logger.info("Cleaned %d non-slug family entries from DB", cur.rowcount)
    except Exception as exc:
        logger.warning("Family cleanup failed: %s", exc)

    families_upserted = 0
    family_os_docs: list[dict] = []
    # Build reverse map (common_name/alias → slug) for actor→family link resolution
    name_to_slug: dict[str, str] = {}

    for slug in family_slugs:
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during family phase")
            fail_run(run_id, "Cancelled by user")
            return

        galaxy = galaxy_family.get(slug)
        if galaxy:
            # MISP galaxy has this family — use its data (has ATT&CK TIDs via refs)
            meta     = galaxy.get("meta") or {}
            name     = slug[:200]
            aliases  = [a[:200] for a in (meta.get("synonyms") or []) if a]
            desc     = (galaxy.get("description") or "")[:4000] or None
            mitre_tids = _extract_mitre_tids(meta.get("refs") or [])
        else:
            # Not in MISP galaxy — fetch individual from Malpedia API
            data       = _malpedia(f"get/family/{slug}") or {}
            common     = (data.get("common_name") or slug)
            name       = common[:200]
            aliases    = [a[:200] for a in (data.get("alt_names") or []) if a]
            desc       = (data.get("description") or "")[:4000] or None
            mitre_tids = _extract_mitre_tids(data.get("urls") or [])

        # Build name→slug reverse map for actor→family link resolution
        name_to_slug[slug.lower()] = slug
        for alias in aliases:
            if alias:
                name_to_slug[alias.lower()] = slug

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

    # ── 3. Primary: Malpedia actor list ──────────────────────────────────────
    actor_api_slugs: list[str] = _malpedia("list/actors") or []
    logger.info("Malpedia API actors: %d slugs", len(actor_api_slugs))

    actors_upserted = 0
    actor_os_docs: list[dict] = []
    # family_slug → set of actor slugs (canonical, for DB update)
    family_actor_map: dict[str, set[str]] = {}

    for api_slug in actor_api_slugs:
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during actor phase")
            fail_run(run_id, "Cancelled by user")
            return

        data = _malpedia(f"get/actor/{api_slug}") or {}

        # Canonical slug: use MISP galaxy value for IOC correlation, else Malpedia slug
        galaxy = galaxy_actor_by_api.get(api_slug)
        if galaxy:
            slug = (galaxy.get("value") or api_slug).strip()
        else:
            slug = api_slug

        # Name: try multiple field names the API may use
        name = (
            data.get("common_name") or
            data.get("actor_name") or
            data.get("name") or
            slug
        )[:200]

        # Aliases
        aliases = data.get("aliases") or data.get("synonyms") or []
        if galaxy:
            galaxy_meta = galaxy.get("meta") or {}
            for a in (galaxy_meta.get("synonyms") or []):
                if a and a not in aliases:
                    aliases.append(a)

        # Country: Malpedia nests in attribution or metadata, MISP galaxy is flat
        attribution = data.get("attribution") or {}
        if isinstance(attribution, dict):
            country = (attribution.get("country") or "")[:5].upper() or None
        else:
            country = None
        if not country and galaxy:
            galaxy_meta = galaxy.get("meta") or {}
            country = (galaxy_meta.get("country") or "")[:5].upper() or None

        # Motivation
        motivation = (
            data.get("type_of_incident") or
            data.get("cfr-type-of-incident") or
            (attribution.get("cfr_type_of_incident") if isinstance(attribution, dict) else None)
        )
        if not motivation and galaxy:
            galaxy_meta = galaxy.get("meta") or {}
            motivation = galaxy_meta.get("cfr-type-of-incident") or galaxy_meta.get("motive") or None
        if isinstance(motivation, list):
            motivation = motivation[0] if motivation else None

        # Description
        desc = (data.get("description") or "")[:4000] or None
        if not desc and galaxy:
            desc = (galaxy.get("description") or "")[:4000] or None

        # Actor→family links: Malpedia returns {platform: [common_names]}
        malware_families = data.get("malware_families") or {}
        if isinstance(malware_families, dict):
            for platform_names in malware_families.values():
                for fname in (platform_names or []):
                    fslug = name_to_slug.get(fname.lower())
                    if fslug:
                        family_actor_map.setdefault(fslug, set()).add(slug)

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

    # ── 4. Write actor→family links ──────────────────────────────────────────
    links_written = 0
    for fslug, actor_slugs in family_actor_map.items():
        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE ti_malware_families SET actor_slugs=%s WHERE slug=%s",
                        (json.dumps(sorted(actor_slugs)), fslug),
                    )
            links_written += 1
        except Exception as exc:
            logger.warning("Actor→family link update failed for %s: %s", fslug, exc)
    logger.info("Actor→family links written: %d families updated", links_written)

    # ── 5. Sync to OpenSearch ─────────────────────────────────────────────────
    os_client = get_os_client()
    if os_client:
        try:
            for idx, mapping in [
                (_OS_INDEX_FAMILIES, _OS_MAPPING_FAMILIES),
                (_OS_INDEX_ACTORS,   _OS_MAPPING_ACTORS),
            ]:
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
    logger.info(
        "Malpedia completed: %d families + %d actors upserted, %d actor→family links",
        families_upserted, actors_upserted, links_written,
    )
