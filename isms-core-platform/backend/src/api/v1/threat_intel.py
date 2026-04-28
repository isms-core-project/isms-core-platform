"""Phase 40 — Threat Intelligence API.

Serves data from the isms-core-threat-intel container (ti_* tables).
All endpoints require authentication. Trigger endpoints require admin.
"""

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Body, Request
from pydantic import BaseModel
from sqlalchemy import func, select, or_, cast, String
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.dependencies import get_current_user, require_admin
from src.database.session import get_db
from src.domain.feeds import FeedRun, TiIoc, TiMalwareFamily, TiActor, TiTool, TiEnrichmentCache

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/threat-intel", tags=["threat-intel"])

_TI_SOURCES = [
    ("circl_misp",       "CIRCL MISP",        "TI_MISP_CIRCL_ENABLED"),
    ("botvrij_misp",     "Botvrij MISP",       "TI_MISP_BOTVRIJ_ENABLED"),
    ("abuseipdb",        "AbuseIPDB",          "TI_ABUSEIPDB_ENABLED"),
    ("urlhaus",          "URLhaus",            "TI_URLHAUS_ENABLED"),
    ("threatfox",        "ThreatFox",          "TI_THREATFOX_ENABLED"),
    ("sslbl",            "SSL Blacklist",      "TI_SSLBL_ENABLED"),
    ("feodotracker",     "Feodo Tracker",      "TI_FEODOTRACKER_ENABLED"),
    ("red_flag_domains", "Red Flag Domains",   "TI_RED_FLAG_DOMAINS_ENABLED"),
    ("stopforumspam",    "Stopforumspam",      "TI_STOPFORUMSPAM_ENABLED"),
    ("malwarebazaar",    "MalwareBazaar",      "TI_MALWAREBAZAAR_ENABLED"),
    ("malpedia",         "Malpedia",           "TI_MALPEDIA_ENABLED"),
]


def _ti_enabled() -> bool:
    return get_settings().threat_intel_enabled


def _require_ti_enabled():
    if not _ti_enabled():
        raise HTTPException(status_code=503, detail="Threat intelligence module not active — enable with --profile threat-intel")


# ── Schemas ────────────────────────────────────────────────────────────────────

class TiSourceStatus(BaseModel):
    source: str
    display_name: str
    enabled: bool
    last_run_at: datetime | None = None
    last_run_status: str | None = None
    ioc_count: int = 0

class TiSummary(BaseModel):
    active: bool
    sources: list[TiSourceStatus]
    total_iocs: int
    total_families: int
    total_actors: int
    total_tools: int = 0

class IocRead(BaseModel):
    id: str
    ioc_type: str
    value: str
    source: str
    confidence: int | None
    tags: list
    mitre_tids: list
    family_slugs: list
    actor_slugs: list
    first_seen: datetime | None
    last_seen: datetime | None

class IocList(BaseModel):
    total: int
    items: list[IocRead]

class MalwareFamilyRead(BaseModel):
    id: str
    slug: str
    name: str
    aliases: list
    description: str | None
    actor_slugs: list
    mitre_tids: list
    updated_at: datetime

class MalwareFamilyList(BaseModel):
    total: int
    items: list[MalwareFamilyRead]

class ActorRead(BaseModel):
    id: str
    slug: str
    name: str
    country: str | None
    motivation: str | None
    description: str | None
    actor_type: str = "threat-actor"
    updated_at: datetime

class ActorList(BaseModel):
    total: int
    items: list[ActorRead]

class ToolRead(BaseModel):
    id: str
    slug: str
    name: str
    aliases: list
    description: str | None
    mitre_tids: list
    updated_at: datetime

class ToolList(BaseModel):
    total: int
    items: list[ToolRead]

class EnrichIpRequest(BaseModel):
    ip: str

class EnrichIpResponse(BaseModel):
    ip: str
    abuseipdb: dict | None = None
    shodan: dict | None = None
    google_dns: dict | None = None
    cached: bool = False
    cache_age_minutes: int | None = None
    ioc_hits: list[IocRead] = []


# ── Summary ────────────────────────────────────────────────────────────────────

@router.get("/summary", response_model=TiSummary)
def get_ti_summary(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
):
    """Feed health and record counts per source."""
    active = _ti_enabled()
    sources: list[TiSourceStatus] = []

    for source_key, display_name, env_var in _TI_SOURCES:
        enabled = os.environ.get(env_var, "true").lower() == "true"

        last_run = db.scalars(
            select(FeedRun)
            .where(FeedRun.feed_name.like(f"{source_key}%"))
            .order_by(FeedRun.started_at.desc())
            .limit(1)
        ).first()

        if source_key == "malpedia":
            ioc_count = (
                (db.scalar(select(func.count()).select_from(TiMalwareFamily)) or 0)
                + (db.scalar(select(func.count()).select_from(TiActor)) or 0)
                + (db.scalar(select(func.count()).select_from(TiTool)) or 0)
            )
        else:
            ioc_count = db.scalar(
                select(func.count()).select_from(TiIoc).where(TiIoc.source == source_key)
            ) or 0

        sources.append(TiSourceStatus(
            source=source_key,
            display_name=display_name,
            enabled=enabled,
            last_run_at=last_run.started_at if last_run else None,
            last_run_status=last_run.status if last_run else None,
            ioc_count=ioc_count,
        ))

    total_iocs     = db.scalar(select(func.count()).select_from(TiIoc)) or 0
    total_families = db.scalar(select(func.count()).select_from(TiMalwareFamily)) or 0
    total_actors   = db.scalar(select(func.count()).select_from(TiActor)) or 0
    total_tools    = db.scalar(select(func.count()).select_from(TiTool)) or 0

    return TiSummary(
        active=active,
        sources=sources,
        total_iocs=total_iocs,
        total_families=total_families,
        total_actors=total_actors,
        total_tools=total_tools,
    )


# ── IOC Stats ─────────────────────────────────────────────────────────────────

@router.get("/ioc-stats")
def get_ioc_stats(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
):
    """IOC breakdown by type, source totals, and top malware families — for TI charts."""
    _require_ti_enabled()
    from sqlalchemy import text

    type_rows = db.execute(
        select(TiIoc.ioc_type, func.count().label("cnt"))
        .group_by(TiIoc.ioc_type)
        .order_by(func.count().desc())
    ).all()

    source_rows = db.execute(
        select(TiIoc.source, func.count().label("cnt"))
        .group_by(TiIoc.source)
        .order_by(func.count().desc())
    ).all()

    family_rows = db.execute(
        text("""
            SELECT slug, COUNT(*) AS cnt
            FROM ti_iocs, jsonb_array_elements_text(family_slugs) AS slug
            WHERE slug <> ''
            GROUP BY slug
            ORDER BY cnt DESC
            LIMIT 12
        """)
    ).all()

    return {
        "type_breakdown": [{"type": r.ioc_type, "count": r.cnt} for r in type_rows],
        "source_totals":  [{"source": r.source,  "count": r.cnt} for r in source_rows],
        "top_families":   [{"family": r.slug,    "count": r.cnt} for r in family_rows],
    }


# ── IOC Explorer ───────────────────────────────────────────────────────────────

@router.get("/iocs", response_model=IocList)
def list_iocs(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
    q: Annotated[str | None, Query(max_length=500)] = None,
    ioc_type: Annotated[str | None, Query()] = None,
    source: Annotated[str | None, Query()] = None,
    family_slug: Annotated[str | None, Query()] = None,
    actor_slug: Annotated[str | None, Query()] = None,
    mitre_tid: Annotated[str | None, Query()] = None,
    skip: int = 0,
    limit: int = 50,
):
    """Paginated IOC search. Filters: q (value contains), ioc_type, source, family_slug, actor_slug, mitre_tid."""
    _require_ti_enabled()

    stmt = select(TiIoc)

    if q:
        stmt = stmt.where(TiIoc.value.ilike(f"%{q}%"))
    if ioc_type:
        stmt = stmt.where(TiIoc.ioc_type == ioc_type)
    if source:
        stmt = stmt.where(TiIoc.source == source)
    if family_slug:
        stmt = stmt.where(TiIoc.family_slugs.contains([family_slug]))
    if actor_slug:
        stmt = stmt.where(TiIoc.actor_slugs.contains([actor_slug]))
    if mitre_tid:
        stmt = stmt.where(TiIoc.mitre_tids.contains([mitre_tid]))

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    rows = db.scalars(stmt.order_by(TiIoc.last_seen.desc()).offset(skip).limit(min(limit, 200))).all()

    return IocList(
        total=total or 0,
        items=[
            IocRead(
                id=str(r.id),
                ioc_type=r.ioc_type,
                value=r.value,
                source=r.source,
                confidence=r.confidence,
                tags=r.tags or [],
                mitre_tids=r.mitre_tids or [],
                family_slugs=r.family_slugs or [],
                actor_slugs=r.actor_slugs or [],
                first_seen=r.first_seen,
                last_seen=r.last_seen,
            )
            for r in rows
        ],
    )


# ── Malware Atlas ─────────────────────────────────────────────────────────────

@router.get("/malware", response_model=MalwareFamilyList)
def list_malware_families(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
    q: Annotated[str | None, Query(max_length=200)] = None,
    actor_slug: Annotated[str | None, Query()] = None,
    mitre_tid: Annotated[str | None, Query()] = None,
    skip: int = 0,
    limit: int = 50,
):
    """Malware family list from Malpedia. Filter by name, actor, or ATT&CK TID."""
    _require_ti_enabled()

    stmt = select(TiMalwareFamily)
    if q:
        stmt = stmt.where(
            or_(
                TiMalwareFamily.name.ilike(f"%{q}%"),
                cast(TiMalwareFamily.aliases, String).ilike(f"%{q}%"),
            )
        )
    if actor_slug:
        stmt = stmt.where(TiMalwareFamily.actor_slugs.contains([actor_slug]))
    if mitre_tid:
        stmt = stmt.where(TiMalwareFamily.mitre_tids.contains([mitre_tid]))

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    rows = db.scalars(stmt.order_by(TiMalwareFamily.name).offset(skip).limit(min(limit, 200))).all()

    return MalwareFamilyList(
        total=total or 0,
        items=[
            MalwareFamilyRead(
                id=str(r.id),
                slug=r.slug,
                name=r.name,
                aliases=r.aliases or [],
                description=r.description,
                actor_slugs=r.actor_slugs or [],
                mitre_tids=r.mitre_tids or [],
                updated_at=r.updated_at,
            )
            for r in rows
        ],
    )


# ── Threat Actors ─────────────────────────────────────────────────────────────

@router.get("/actors", response_model=ActorList)
def list_actors(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
    q: Annotated[str | None, Query(max_length=200)] = None,
    country: Annotated[str | None, Query(max_length=5)] = None,
    actor_type: Annotated[str | None, Query()] = None,
    skip: int = 0,
    limit: int = 50,
):
    """Threat actor / ransomware group list. Filter by name, country, or actor_type."""
    _require_ti_enabled()

    stmt = select(TiActor)
    if q:
        stmt = stmt.where(TiActor.name.ilike(f"%{q}%"))
    if country:
        stmt = stmt.where(TiActor.country == country.upper())
    if actor_type:
        stmt = stmt.where(TiActor.actor_type == actor_type)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    rows = db.scalars(stmt.order_by(TiActor.name).offset(skip).limit(min(limit, 200))).all()

    return ActorList(
        total=total or 0,
        items=[
            ActorRead(
                id=str(r.id),
                slug=r.slug,
                name=r.name,
                country=r.country,
                motivation=r.motivation,
                description=r.description,
                actor_type=getattr(r, "actor_type", "threat-actor"),
                updated_at=r.updated_at,
            )
            for r in rows
        ],
    )


# ── Attacker Tools ─────────────────────────────────────────────────────────────

@router.get("/tools", response_model=ToolList)
def list_tools(
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
    q: Annotated[str | None, Query(max_length=200)] = None,
    mitre_tid: Annotated[str | None, Query()] = None,
    skip: int = 0,
    limit: int = 50,
):
    """Attacker tooling from MISP galaxy. Filter by name or ATT&CK TID."""
    _require_ti_enabled()

    stmt = select(TiTool)
    if q:
        stmt = stmt.where(
            or_(
                TiTool.name.ilike(f"%{q}%"),
                cast(TiTool.aliases, String).ilike(f"%{q}%"),
            )
        )
    if mitre_tid:
        stmt = stmt.where(TiTool.mitre_tids.contains([mitre_tid]))

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    rows = db.scalars(stmt.order_by(TiTool.name).offset(skip).limit(min(limit, 200))).all()

    return ToolList(
        total=total or 0,
        items=[
            ToolRead(
                id=str(r.id),
                slug=r.slug,
                name=r.name,
                aliases=r.aliases or [],
                description=r.description,
                mitre_tids=r.mitre_tids or [],
                updated_at=r.updated_at,
            )
            for r in rows
        ],
    )


# ── IP Enrichment ─────────────────────────────────────────────────────────────

@router.post("/enrich/ip", response_model=EnrichIpResponse)
def enrich_ip(
    body: EnrichIpRequest,
    db: DBSession = Depends(get_db),
    _current_user=Depends(get_current_user),
):
    """
    On-demand IP enrichment: AbuseIPDB check + Shodan InternetDB/API.
    Results cached 24h in ti_enrichment_cache. Also returns existing IOC hits for this IP.
    """
    _require_ti_enabled()
    ip = body.ip.strip()

    # Validate basic IP format
    import ipaddress
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Invalid IP address: {ip}")

    # Check cache
    now = datetime.now(timezone.utc)
    cached_row = db.get(TiEnrichmentCache, ip)
    is_cached = False
    cache_age_minutes: int | None = None

    if cached_row and (now - cached_row.cached_at) < timedelta(hours=24):
        is_cached = True
        cache_age_minutes = int((now - cached_row.cached_at).total_seconds() / 60)
        abuseipdb_result = cached_row.abuseipdb
        shodan_result = cached_row.shodan
        google_dns_result = cached_row.google_dns
    else:
        abuseipdb_result = _call_abuseipdb(ip)
        shodan_result = _call_shodan(ip)
        google_dns_result = _call_google_dns(ip)

        # Persist to cache
        if cached_row:
            cached_row.abuseipdb = abuseipdb_result
            cached_row.shodan = shodan_result
            cached_row.google_dns = google_dns_result
            cached_row.cached_at = now
        else:
            db.add(TiEnrichmentCache(
                ip=ip,
                abuseipdb=abuseipdb_result,
                shodan=shodan_result,
                google_dns=google_dns_result,
                cached_at=now,
            ))
        db.commit()

    # IOC hits for this IP in our TI tables
    ioc_hits = db.scalars(
        select(TiIoc)
        .where(TiIoc.ioc_type == "ip", TiIoc.value == ip)
        .order_by(TiIoc.last_seen.desc())
        .limit(20)
    ).all()

    return EnrichIpResponse(
        ip=ip,
        abuseipdb=abuseipdb_result,
        shodan=shodan_result,
        google_dns=google_dns_result,
        cached=is_cached,
        cache_age_minutes=cache_age_minutes,
        ioc_hits=[
            IocRead(
                id=str(r.id), ioc_type=r.ioc_type, value=r.value, source=r.source,
                confidence=r.confidence, tags=r.tags or [], mitre_tids=r.mitre_tids or [],
                family_slugs=r.family_slugs or [], actor_slugs=r.actor_slugs or [],
                first_seen=r.first_seen, last_seen=r.last_seen,
            )
            for r in ioc_hits
        ],
    )


def _call_abuseipdb(ip: str) -> dict | None:
    key = os.environ.get("ABUSEIPDB_API_KEY", "")
    if not key:
        return None
    try:
        import requests
        resp = requests.get(
            "https://api.abuseipdb.com/api/v2/check",
            headers={"Key": key, "Accept": "application/json"},
            params={"ipAddress": ip, "maxAgeInDays": 90},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json().get("data")
    except Exception as exc:
        logger.warning("AbuseIPDB enrichment failed for %s: %s", ip, exc)
        return None


def _call_shodan(ip: str) -> dict | None:
    key = os.environ.get("SHODAN_API_KEY", "")
    try:
        import requests
        if key:
            resp = requests.get(
                f"https://api.shodan.io/shodan/host/{ip}",
                params={"key": key},
                timeout=10,
            )
            if resp.status_code == 200:
                raw = resp.json()
                return {
                    "source": "shodan_api", "ports": raw.get("ports", []),
                    "hostnames": raw.get("hostnames", []), "org": raw.get("org"),
                    "asn": raw.get("asn"), "country": raw.get("country_code"),
                    "cves": list(raw.get("vulns", {}).keys()),
                    "last_update": raw.get("last_update"),
                }
        # InternetDB fallback (always available, no key required)
        resp = requests.get(f"https://internetdb.shodan.io/{ip}", timeout=8)
        if resp.status_code == 404:
            return {"source": "shodan_internetdb", "not_found": True}
        if resp.status_code == 200:
            raw = resp.json()
            return {
                "source": "shodan_internetdb", "ports": raw.get("ports", []),
                "hostnames": raw.get("hostnames", []), "cpes": raw.get("cpes", []),
                "cves": raw.get("vulns", []), "tags": raw.get("tags", []),
            }
    except Exception as exc:
        logger.warning("Shodan enrichment failed for %s: %s", ip, exc)
    return None


def _call_google_dns(ip: str) -> dict | None:
    """Reverse DNS (PTR) lookup via Google DNS-over-HTTPS. No API key required."""
    try:
        import ipaddress
        import requests

        addr = ipaddress.ip_address(ip)
        if isinstance(addr, ipaddress.IPv4Address):
            reversed_name = ".".join(reversed(ip.split("."))) + ".in-addr.arpa"
        else:
            # IPv6: expand, reverse nibbles
            full = addr.exploded.replace(":", "")
            reversed_name = ".".join(reversed(full)) + ".ip6.arpa"

        resp = requests.get(
            "https://dns.google/resolve",
            params={"name": reversed_name, "type": "PTR"},
            headers={"Accept": "application/dns-json"},
            timeout=8,
        )
        if resp.status_code != 200:
            return {"ptr": [], "status": resp.status_code}

        data = resp.json()
        status = data.get("Status", -1)  # 0 = NOERROR, 3 = NXDOMAIN
        answers = data.get("Answer") or []
        ptr_records = [
            a["data"].rstrip(".") for a in answers if a.get("type") == 12
        ]
        return {"ptr": ptr_records, "status": status}
    except Exception as exc:
        logger.warning("Google DNS enrichment failed for %s: %s", ip, exc)
        return None


# ── Admin: trigger feed ───────────────────────────────────────────────────────

_TRIGGER_MAP = {
    "circl_misp":       "circl_misp",
    "botvrij_misp":     "botvrij_misp",
    "abuseipdb":        "abuseipdb_blacklist",
    "malpedia":         "malpedia",
    "urlhaus":          "urlhaus",
    "threatfox":        "threatfox",
    "sslbl":            "sslbl",
    "feodotracker":     "feodotracker",
    "red_flag_domains": "red_flag_domains",
    "stopforumspam":    "stopforumspam",
    "malwarebazaar":    "malwarebazaar",
}

@router.post("/feeds/trigger", dependencies=[Depends(require_admin)])
def trigger_ti_feed(
    body: Annotated[dict, Body()],
    _current_user=Depends(get_current_user),
):
    """Admin: trigger a specific TI feed now via the trigger server."""
    _require_ti_enabled()
    source = body.get("source", "")
    if source not in _TRIGGER_MAP:
        raise HTTPException(status_code=422, detail=f"Unknown TI source: {source}. Valid: {list(_TRIGGER_MAP)}")

    # The threat-intel container runs its own trigger server on port 9002
    ti_trigger_url = os.environ.get("TI_TRIGGER_URL", "http://isms-core-threat-intel:9002")
    try:
        import requests
        resp = requests.post(
            f"{ti_trigger_url}/trigger/{_TRIGGER_MAP[source]}",
            timeout=5,
        )
        if resp.status_code == 200:
            return {"status": "triggered", "source": source}
        return {"status": "error", "detail": resp.text[:200]}
    except Exception as exc:
        logger.warning("TI trigger failed for %s: %s", source, exc)
        raise HTTPException(status_code=503, detail=f"TI trigger server unreachable: {exc}")


@router.delete("/feeds/cancel/{source}", dependencies=[Depends(require_admin)])
def cancel_ti_feed(source: str):
    """Admin: request cancellation of a running TI feed."""
    if source not in _TRIGGER_MAP:
        raise HTTPException(status_code=422, detail=f"Unknown TI source: {source}. Valid: {list(_TRIGGER_MAP)}")
    _require_ti_enabled()
    ti_trigger_url = os.environ.get("TI_TRIGGER_URL", "http://isms-core-threat-intel:9002")
    try:
        import requests
        resp = requests.delete(
            f"{ti_trigger_url}/cancel/{_TRIGGER_MAP[source]}",
            timeout=5,
        )
        if resp.status_code == 200:
            return {"status": "cancel_requested", "source": source}
        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Feed '{source}' is not running")
        raise HTTPException(status_code=502, detail=f"TI container returned {resp.status_code}: {resp.text[:200]}")
    except HTTPException:
        raise
    except Exception as exc:
        logger.warning("TI cancel failed for %s: %s", source, exc)
        raise HTTPException(status_code=503, detail=f"TI trigger server unreachable: {exc}")


@router.post("/internal/notify-failure", include_in_schema=False)
def internal_notify_ti_feed_failure(
    request: Request,
    payload: dict = Body(...),
):
    """Called by the threat-intel container when a feed fails. Queues a TI failure notification.

    Authenticated via CONNECTORS_WORKER_SECRET.
    Body: {feed_name: str, error_message: str, run_id: str | null}
    """
    ws = os.environ.get("CONNECTORS_WORKER_SECRET", "")
    if not ws:
        raise HTTPException(status_code=503, detail="Worker mode not configured")
    token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
    if token != ws:
        raise HTTPException(status_code=401, detail="Invalid worker secret")

    feed_name = payload.get("feed_name", "unknown")
    error_message = payload.get("error_message", "")
    run_id = payload.get("run_id")

    from src.services.notification_service import notify_ti_feed_failure
    notify_ti_feed_failure.delay(
        feed_name=feed_name,
        error_message=error_message,
        run_id=run_id,
    )
    logger.info("Queued TI feed failure notification for %s", feed_name)
    return {"queued": True, "feed_name": feed_name}
