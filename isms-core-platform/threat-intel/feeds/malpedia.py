"""Malpedia feed — malware families, threat actors, ransomware groups, and attacker tools.

Primary source: Malpedia public API (no key required)
  https://malpedia.caad.fkie.fraunhofer.de/api
  - get/families   → ALL families in one request (dict keyed by slug)
  - get/actors     → ALL actors in one request (dict keyed by api_slug)

Secondary source: MISP galaxy (GitHub, no key required)
  - clusters/malpedia.json         → ATT&CK TIDs from refs
  - clusters/threat-actor.json     → IOC-correlation slugs + country/motivation
  - clusters/ransomware-group.json → ransomware groups → ti_actors (actor_type='ransomware')
  - clusters/tool.json             → attacker tooling  → ti_tools

Pull schedule: weekly (Sunday 03:00 UTC).

Actor slug compatibility:
  MISP IOC events tag actors as misp-galaxy:threat-actor="APT28".
  MISP galaxy value ("APT28") is used as DB slug for IOC correlation.
  Actors not in MISP galaxy use the Malpedia API slug (apt28).
"""

import json
import logging
import re
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_MISP_GALAXY_BASE = "https://raw.githubusercontent.com/MISP/misp-galaxy/main/clusters"
_MALPEDIA_API     = "https://malpedia.caad.fkie.fraunhofer.de/api"

_OS_INDEX_FAMILIES  = "ti-malpedia-families"
_OS_INDEX_ACTORS    = "ti-malpedia-actors"
_OS_INDEX_TOOLS     = "ti-malpedia-tools"

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
            "actor_type":  {"type": "keyword"},
            "description": {"type": "text"},
            "updated_at":  {"type": "date"},
        }
    }
}

_OS_MAPPING_TOOLS = {
    "mappings": {
        "properties": {
            "slug":        {"type": "keyword"},
            "name":        {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "aliases":     {"type": "keyword"},
            "mitre_tids":  {"type": "keyword"},
            "description": {"type": "text"},
            "updated_at":  {"type": "date"},
        }
    }
}


def _fetch_galaxy(cluster: str) -> list[dict]:
    """Fetch MISP galaxy cluster (secondary source)."""
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


def _malpedia_get(path: str) -> dict | list | None:
    """GET from Malpedia public API. Returns None on error."""
    try:
        resp = requests.get(f"{_MALPEDIA_API}/{path}", timeout=60)
        resp.raise_for_status()
        return resp.json()
    except Exception as exc:
        logger.warning("Malpedia API %s: %s", path, exc)
        return None


def _extract_mitre_tids(urls: list) -> list[str]:
    """Extract ATT&CK TIDs from URLs (e.g. attack.mitre.org/techniques/T1055)."""
    tids = set()
    for u in urls or []:
        tids.update(re.findall(r"T\d{4}(?:\.\d{3})?", str(u)))
    return sorted(tids)


def _to_slug(value: str) -> str:
    """Normalise a display name to a DB slug (APT28 → apt28, Cobalt Strike → cobalt_strike)."""
    return value.lower().replace(" ", "_").replace("-", "_")


def run() -> None:
    run_id = start_run("malpedia")
    logger.info("Malpedia pull started (primary: Malpedia API, secondary: MISP galaxy)")

    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()

    # ── 1. MISP galaxy lookup dicts ──────────────────────────────────────────────

    # Family slug → entry (ATT&CK TIDs via refs)
    galaxy_family: dict[str, dict] = {}
    for entry in _fetch_galaxy("malpedia"):
        slug = (entry.get("value") or "").strip()
        if re.match(r"^[a-z]+\.[a-z0-9_]+$", slug):
            galaxy_family[slug] = entry

    # Threat actors: api_slug → entry, value → entry, name/alias → canonical slug
    galaxy_actor_by_api: dict[str, dict] = {}
    galaxy_actor_by_val: dict[str, dict] = {}
    actor_name_to_slug:  dict[str, str]  = {}

    for entry in _fetch_galaxy("threat-actor"):
        value = (entry.get("value") or "").strip()
        if not value:
            continue
        galaxy_actor_by_val[value] = entry
        galaxy_actor_by_api[_to_slug(value)] = entry
        actor_name_to_slug[value.lower()] = value
        for syn in ((entry.get("meta") or {}).get("synonyms") or []):
            if syn:
                actor_name_to_slug[syn.lower()] = value

    # Ransomware groups (→ ti_actors with actor_type='ransomware')
    # MISP galaxy uses "ransomware.json" not "ransomware-group.json"
    galaxy_ransomware: list[dict] = _fetch_galaxy("ransomware")

    # Attacker tools (→ ti_tools)
    galaxy_tools: list[dict] = _fetch_galaxy("tool")

    # ── 2. Malpedia bulk family fetch ────────────────────────────────────────────
    logger.info("Fetching all Malpedia families via /api/get/families …")
    families_raw = _malpedia_get("get/families")
    if not families_raw or not isinstance(families_raw, dict):
        fail_run(run_id, "Empty or invalid response from Malpedia /api/get/families")
        return
    logger.info("Malpedia API returned %d families", len(families_raw))

    # DB cleanup — remove non-slug entries from earlier runs
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM ti_malware_families WHERE slug !~ '^[a-z]+\\.[a-z0-9_]+$'"
                )
                if cur.rowcount:
                    logger.info("Cleaned %d non-slug family entries", cur.rowcount)
    except Exception as exc:
        logger.warning("Family cleanup failed: %s", exc)

    families_upserted = 0
    family_os_docs:    list[dict]           = []
    family_attribution: dict[str, list[str]] = {}
    name_to_slug:       dict[str, str]       = {}

    for slug, fdata in families_raw.items():
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during family phase")
            fail_run(run_id, "Cancelled by user")
            return

        if not re.match(r"^[a-z]+\.[a-z0-9_]+$", slug):
            continue

        common_name = (fdata.get("common_name") or slug)
        name        = common_name[:200]
        alt_names   = fdata.get("alt_names") or []
        aliases     = [a[:200] for a in alt_names if a]
        desc        = (fdata.get("description") or "")[:4000] or None
        api_urls    = fdata.get("urls") or []

        galaxy      = galaxy_family.get(slug)
        galaxy_refs = ((galaxy.get("meta") or {}).get("refs") or []) if galaxy else []
        mitre_tids  = _extract_mitre_tids(api_urls + galaxy_refs)

        attribution = fdata.get("attribution") or []
        if attribution:
            family_attribution[slug] = attribution

        name_to_slug[slug.lower()]        = slug
        name_to_slug[common_name.lower()] = slug
        for alias in aliases:
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
                        (str(uuid4()), slug, name, json.dumps(aliases), desc,
                         json.dumps([]), json.dumps(mitre_tids), now),
                    )
            families_upserted += 1
        except Exception as exc:
            logger.warning("Family upsert failed for %s: %s", slug, exc)

        family_os_docs.append({
            "slug": slug, "name": name, "aliases": aliases,
            "actor_slugs": [], "mitre_tids": mitre_tids,
            "description": desc, "updated_at": now_iso,
            "_os_id": f"family:{slug}",
        })

    logger.info("Malpedia families upserted: %d", families_upserted)

    # ── 3. Resolve attribution → actor_slugs on families ─────────────────────────
    family_actor_links: dict[str, set[str]] = {}
    for fslug, attr_names in family_attribution.items():
        for aname in attr_names:
            actor_slug = actor_name_to_slug.get(aname.lower()) or _to_slug(aname)
            family_actor_links.setdefault(fslug, set()).add(actor_slug)

    links_written = 0
    for fslug, actor_slugs in family_actor_links.items():
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

    # ── 4. Threat actors ─────────────────────────────────────────────────────────
    actors_raw = _malpedia_get("get/actors")
    use_malpedia_actors = isinstance(actors_raw, dict) and len(actors_raw) > 0
    if use_malpedia_actors:
        logger.info("Malpedia API returned %d actors (bulk)", len(actors_raw))
    else:
        logger.info("Malpedia /api/get/actors unavailable — using MISP galaxy actors")

    actors_upserted = 0
    actor_os_docs:   list[dict] = []

    def _iter_actors():
        if use_malpedia_actors:
            for api_slug, adata in actors_raw.items():
                galaxy = galaxy_actor_by_api.get(api_slug)
                slug   = (galaxy.get("value") or api_slug).strip() if galaxy else api_slug
                name   = (adata.get("common_name") or adata.get("name") or slug)[:200]
                meta   = adata.get("meta") or adata.get("metadata") or {}
                country = (
                    meta.get("country") or meta.get("country_code") or
                    ((galaxy.get("meta") or {}).get("country") if galaxy else None) or ""
                )[:5].upper() or None
                motivation = (
                    adata.get("cfr-type-of-incident") or adata.get("type_of_incident") or
                    meta.get("cfr-type-of-incident") or
                    ((galaxy.get("meta") or {}).get("cfr-type-of-incident") if galaxy else None)
                )
                if isinstance(motivation, list):
                    motivation = motivation[0] if motivation else None
                desc = (adata.get("description") or
                        (galaxy.get("description") if galaxy else None) or "")[:4000] or None
                yield slug, name, country, motivation, desc
        else:
            for entry in galaxy_actor_by_val.values():
                slug = (entry.get("value") or "").strip()
                if not slug:
                    continue
                meta       = entry.get("meta") or {}
                name       = slug[:200]
                country    = (meta.get("country") or "")[:5].upper() or None
                motivation = meta.get("cfr-type-of-incident") or meta.get("motive") or None
                if isinstance(motivation, list):
                    motivation = motivation[0] if motivation else None
                desc = (entry.get("description") or "")[:4000] or None
                yield slug, name, country, motivation, desc

    for slug, name, country, motivation, desc in _iter_actors():
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during actor phase")
            fail_run(run_id, "Cancelled by user")
            return
        if not slug:
            continue
        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_actors
                          (id, slug, name, country, motivation, description, actor_type, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,'threat-actor',%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name        = EXCLUDED.name,
                          country     = EXCLUDED.country,
                          motivation  = EXCLUDED.motivation,
                          description = EXCLUDED.description,
                          actor_type  = 'threat-actor',
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (str(uuid4()), slug, name, country, motivation, desc, now),
                    )
            actors_upserted += 1
        except Exception as exc:
            logger.warning("Actor upsert failed for %s: %s", slug, exc)

        actor_os_docs.append({
            "slug": slug, "name": name, "country": country,
            "motivation": motivation, "actor_type": "threat-actor",
            "description": desc, "updated_at": now_iso,
            "_os_id": f"actor:{slug}",
        })

    logger.info("Malpedia actors upserted: %d", actors_upserted)

    # ── 5. Ransomware groups (MISP galaxy ransomware-group.json) ─────────────────
    ransomware_upserted = 0

    for entry in galaxy_ransomware:
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during ransomware phase")
            fail_run(run_id, "Cancelled by user")
            return

        value = (entry.get("value") or "").strip()
        if not value:
            continue

        slug       = _to_slug(value)[:200]
        name       = value[:200]
        meta       = entry.get("meta") or {}
        country    = (meta.get("country") or "")[:5].upper() or None
        motivation = meta.get("cfr-type-of-incident") or meta.get("motive") or "Ransomware"
        if isinstance(motivation, list):
            motivation = motivation[0] if motivation else "Ransomware"
        desc = (entry.get("description") or "")[:4000] or None

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_actors
                          (id, slug, name, country, motivation, description, actor_type, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,'ransomware',%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name        = EXCLUDED.name,
                          country     = EXCLUDED.country,
                          motivation  = EXCLUDED.motivation,
                          description = EXCLUDED.description,
                          actor_type  = 'ransomware',
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (str(uuid4()), slug, name, country, motivation, desc, now),
                    )
            ransomware_upserted += 1
        except Exception as exc:
            logger.warning("Ransomware group upsert failed for %s: %s", slug, exc)

        actor_os_docs.append({
            "slug": slug, "name": name, "country": country,
            "motivation": motivation, "actor_type": "ransomware",
            "description": desc, "updated_at": now_iso,
            "_os_id": f"actor:{slug}",
        })

    logger.info("Ransomware groups upserted: %d", ransomware_upserted)

    # ── 6. Attacker tools (MISP galaxy tool.json) ────────────────────────────────
    tools_upserted = 0
    tool_os_docs:   list[dict] = []

    for entry in galaxy_tools:
        if is_cancelled("malpedia"):
            logger.info("Malpedia cancelled during tools phase")
            fail_run(run_id, "Cancelled by user")
            return

        value = (entry.get("value") or "").strip()
        if not value:
            continue

        slug    = _to_slug(value)[:200]
        name    = value[:200]
        meta    = entry.get("meta") or {}
        aliases = [s[:200] for s in (meta.get("synonyms") or []) if s]
        desc    = (entry.get("description") or "")[:4000] or None
        refs    = meta.get("refs") or []
        mitre_tids = _extract_mitre_tids(refs)

        try:
            with get_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO ti_tools
                          (id, slug, name, aliases, description, mitre_tids, updated_at)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                        ON CONFLICT (slug) DO UPDATE SET
                          name        = EXCLUDED.name,
                          aliases     = EXCLUDED.aliases,
                          description = EXCLUDED.description,
                          mitre_tids  = EXCLUDED.mitre_tids,
                          updated_at  = EXCLUDED.updated_at
                        """,
                        (str(uuid4()), slug, name, json.dumps(aliases), desc,
                         json.dumps(mitre_tids), now),
                    )
            tools_upserted += 1
        except Exception as exc:
            logger.warning("Tool upsert failed for %s: %s", slug, exc)

        tool_os_docs.append({
            "slug": slug, "name": name, "aliases": aliases,
            "mitre_tids": mitre_tids, "description": desc,
            "updated_at": now_iso,
            "_os_id": f"tool:{slug}",
        })

    logger.info("Attacker tools upserted: %d", tools_upserted)

    # ── 7. Sync to OpenSearch ────────────────────────────────────────────────────
    os_client = get_os_client()
    if os_client:
        try:
            for idx, mapping in [
                (_OS_INDEX_FAMILIES, _OS_MAPPING_FAMILIES),
                (_OS_INDEX_ACTORS,   _OS_MAPPING_ACTORS),
                (_OS_INDEX_TOOLS,    _OS_MAPPING_TOOLS),
            ]:
                if not os_client.indices.exists(index=idx):
                    os_client.indices.create(index=idx, body=mapping)
                    logger.info("Created OpenSearch index: %s", idx)
            if family_os_docs:
                os_bulk_upsert(os_client, _OS_INDEX_FAMILIES, family_os_docs, "_os_id")
            if actor_os_docs:
                os_bulk_upsert(os_client, _OS_INDEX_ACTORS, actor_os_docs, "_os_id")
            if tool_os_docs:
                os_bulk_upsert(os_client, _OS_INDEX_TOOLS, tool_os_docs, "_os_id")
        except Exception as exc:
            logger.warning("Malpedia → OpenSearch sync failed: %s", exc)

    total = families_upserted + actors_upserted + ransomware_upserted + tools_upserted
    finish_run(run_id, total)
    logger.info(
        "Malpedia completed: %d families + %d actors + %d ransomware groups + %d tools, %d attribution links",
        families_upserted, actors_upserted, ransomware_upserted, tools_upserted, links_written,
    )
