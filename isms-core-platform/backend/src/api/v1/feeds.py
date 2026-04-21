"""Phase 25 — Threat Intelligence & Vulnerability Feeds API."""

import logging
import os
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone

from fastapi import APIRouter, Body, Depends, Query, Request
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession
from src.core.dependencies import get_current_user, require_admin
from src.database.session import get_db
from src.domain.feeds import (
    CisaKevEntry, EpssScore, FeedRun, MitreTechnique,
    MitreGroup, MitreSoftware, MitreCampaign, MitreRelationship,
)
from src.domain.system import PlatformSetting
from src.domain.users import User
from src.schemas.feeds import (
    CisaKevList,
    CisaKevRead,
    CisaKevStats,
    EpssScoreList,
    EpssScoreRead,
    FeedSettings,
    FeedStatusItem,
    FeedStatusResponse,
    KevAuditEntry,
    KevAuditReport,
    MitreAttackStats,
    MitreTechniqueList,
    MitreTechniqueRead,
    MitreGroupRead, MitreGroupList, MitreGroupStats,
    MitreSoftwareRead, MitreSoftwareList, MitreSoftwareStats,
    MitreCampaignRead, MitreCampaignList,
    MitreHeatmapTechnique, MitreHeatmapResponse,
    NvdCpeEntry,
    NvdCpeList,
    NvdCpeStats,
    NvdCveEntry,
    NvdCveList,
    NvdCveStats,
    NvdIndexStats,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/feeds", tags=["feeds"])

# Canonical feed names and display labels
_FEEDS = [
    ("mitre_attack_v18", "MITRE ATT&CK v18",  "FEEDS_MITRE_ENABLED"),
    ("mitre_atlas",      "MITRE ATLAS",         "FEEDS_ATLAS_ENABLED"),
    ("cisa_kev",         "CISA KEV",            "FEEDS_KEV_ENABLED"),
    ("epss",             "FIRST EPSS",          "FEEDS_EPSS_ENABLED"),
    ("nist_cve",         "NVD CVE",             "FEEDS_CVE_ENABLED"),
    ("nist_cpe",         "NVD CPE (KEV-vendor)","FEEDS_CPE_FULL"),
]


# ── Feed status ────────────────────────────────────────────────────────────────

@router.get("/status", response_model=FeedStatusResponse)
def get_feed_status(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    """Return the last run status for each configured feed."""
    import os

    result_items: list[FeedStatusItem] = []

    for feed_name, display_name, env_var in _FEEDS:
        enabled = os.environ.get(env_var, "true").lower() == "true"

        # Latest run for this feed
        stmt = (
            select(FeedRun)
            .where(FeedRun.feed_name == feed_name)
            .order_by(FeedRun.started_at.desc())
            .limit(1)
        )
        run = db.scalars(stmt).first()

        result_items.append(FeedStatusItem(
            feed_name=feed_name,
            display_name=display_name,
            enabled=enabled,
            last_run=run.started_at if run else None,
            last_status=run.status if run else None,
            item_count=run.item_count if run else None,
            error_message=run.error_message if run else None,
        ))

    return FeedStatusResponse(feeds=result_items)


# ── MITRE ATT&CK ──────────────────────────────────────────────────────────────

@router.get("/mitre/attack", response_model=MitreTechniqueList)
def list_attack_techniques(
    source: str = Query("attack_v18", description="attack_v18 | attack_v19"),
    tactic: str | None = Query(None),
    search: str | None = Query(None),
    subtechniques: bool = Query(True),
    deprecated: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(MitreTechnique).where(MitreTechnique.source == source)
    if not subtechniques:
        stmt = stmt.where(MitreTechnique.is_subtechnique.is_(False))
    if not deprecated:
        stmt = stmt.where(MitreTechnique.deprecated.is_(False))
    if tactic:
        stmt = stmt.where(MitreTechnique.tactics.contains([tactic]))
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            MitreTechnique.name.ilike(q) | MitreTechnique.technique_id.ilike(q)
        )
    stmt = stmt.order_by(MitreTechnique.technique_id)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return MitreTechniqueList(
        items=[MitreTechniqueRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


@router.get("/mitre/attack/stats", response_model=MitreAttackStats)
def get_attack_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    # Collect all non-deprecated techniques across all attack sources
    rows = db.scalars(
        select(MitreTechnique).where(
            MitreTechnique.source.like("attack_%"),
            MitreTechnique.deprecated.is_(False),
        )
    ).all()

    tactic_counts: Counter = Counter()
    platform_counts: Counter = Counter()
    sources: set[str] = set()

    for t in rows:
        for tac in (t.tactics or []):
            tactic_counts[tac] += 1
        for plat in (t.platforms or []):
            platform_counts[plat] += 1
        sources.add(t.source)

    total = len(rows)
    sub_count = sum(1 for t in rows if t.is_subtechnique)
    dep_count = db.scalar(
        select(func.count(MitreTechnique.id)).where(
            MitreTechnique.source.like("attack_%"),
            MitreTechnique.deprecated.is_(True),
        )
    ) or 0

    return MitreAttackStats(
        total_techniques=total - sub_count,
        total_subtechniques=sub_count,
        deprecated_count=dep_count,
        tactic_counts=dict(tactic_counts.most_common()),
        platform_counts=dict(platform_counts.most_common(10)),
        sources=sorted(sources),
    )


# ── MITRE ATLAS ───────────────────────────────────────────────────────────────

@router.get("/mitre/atlas", response_model=MitreTechniqueList)
def list_atlas_techniques(
    tactic: str | None = Query(None),
    search: str | None = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(MitreTechnique).where(MitreTechnique.source == "atlas")
    if tactic:
        stmt = stmt.where(MitreTechnique.tactics.contains([tactic]))
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            MitreTechnique.name.ilike(q) | MitreTechnique.technique_id.ilike(q)
        )
    stmt = stmt.order_by(MitreTechnique.technique_id)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return MitreTechniqueList(
        items=[MitreTechniqueRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


@router.get("/mitre/atlas/stats")
def get_atlas_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    rows = db.scalars(
        select(MitreTechnique).where(MitreTechnique.source == "atlas")
    ).all()
    tactic_counts: Counter = Counter()
    for t in rows:
        for tac in (t.tactics or []):
            tactic_counts[tac] += 1

    return {
        "total_techniques": len(rows),
        "tactic_counts": dict(tactic_counts.most_common()),
    }


# ── MITRE Groups (Phase 28) ───────────────────────────────────────────────────

@router.get("/mitre/groups", response_model=MitreGroupList)
def list_mitre_groups(
    source: str = Query("attack_v18", description="attack_v18 | attack_v19"),
    search: str | None = Query(None),
    deprecated: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(MitreGroup).where(MitreGroup.source == source)
    if not deprecated:
        stmt = stmt.where(MitreGroup.deprecated.is_(False))
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            MitreGroup.name.ilike(q) | MitreGroup.group_id.ilike(q)
        )
    stmt = stmt.order_by(MitreGroup.group_id)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return MitreGroupList(
        items=[MitreGroupRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


@router.get("/mitre/groups/stats", response_model=MitreGroupStats)
def get_mitre_group_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    rows = db.scalars(select(MitreGroup)).all()
    sources: set[str] = set()
    for g in rows:
        sources.add(g.source)
    total = len(rows)
    dep = sum(1 for g in rows if g.deprecated)
    return MitreGroupStats(
        total_groups=total - dep,
        deprecated_count=dep,
        sources=sorted(sources),
    )


# ── MITRE Software (Phase 28) ──────────────────────────────────────────────────

@router.get("/mitre/software", response_model=MitreSoftwareList)
def list_mitre_software(
    source: str = Query("attack_v18", description="attack_v18 | attack_v19"),
    software_type: str | None = Query(None, description="malware | tool"),
    search: str | None = Query(None),
    deprecated: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(MitreSoftware).where(MitreSoftware.source == source)
    if not deprecated:
        stmt = stmt.where(MitreSoftware.deprecated.is_(False))
    if software_type:
        stmt = stmt.where(MitreSoftware.software_type == software_type)
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            MitreSoftware.name.ilike(q) | MitreSoftware.software_id.ilike(q)
        )
    stmt = stmt.order_by(MitreSoftware.software_id)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return MitreSoftwareList(
        items=[MitreSoftwareRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


@router.get("/mitre/software/stats", response_model=MitreSoftwareStats)
def get_mitre_software_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    rows = db.scalars(select(MitreSoftware)).all()
    sources: set[str] = set()
    for s in rows:
        sources.add(s.source)
    dep = sum(1 for s in rows if s.deprecated)
    malware = sum(1 for s in rows if s.software_type == "malware" and not s.deprecated)
    tool = sum(1 for s in rows if s.software_type == "tool" and not s.deprecated)
    return MitreSoftwareStats(
        total_software=malware + tool,
        malware_count=malware,
        tool_count=tool,
        deprecated_count=dep,
        sources=sorted(sources),
    )


# ── MITRE Campaigns (Phase 28) ─────────────────────────────────────────────────

@router.get("/mitre/campaigns", response_model=MitreCampaignList)
def list_mitre_campaigns(
    source: str = Query("attack_v18", description="attack_v18 | attack_v19"),
    search: str | None = Query(None),
    deprecated: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(MitreCampaign).where(MitreCampaign.source == source)
    if not deprecated:
        stmt = stmt.where(MitreCampaign.deprecated.is_(False))
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            MitreCampaign.name.ilike(q) | MitreCampaign.campaign_id.ilike(q)
        )
    stmt = stmt.order_by(MitreCampaign.campaign_id)

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return MitreCampaignList(
        items=[MitreCampaignRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


# ── MITRE Heatmap (Phase 28) ──────────────────────────────────────────────────

# Canonical ATT&CK tactic order (Enterprise)
_TACTIC_ORDER = [
    "reconnaissance", "resource-development", "initial-access", "execution",
    "persistence", "privilege-escalation", "defense-evasion", "credential-access",
    "discovery", "lateral-movement", "collection", "command-and-control",
    "exfiltration", "impact",
]


@router.get("/mitre/heatmap", response_model=MitreHeatmapResponse)
def get_mitre_heatmap(
    source: str = Query("attack_v18", description="attack_v18 | attack_v19"),
    group_ids: str | None = Query(None, description="Comma-separated group IDs (e.g. G0001,G0016). Empty = all groups."),
    include_software: bool = Query(True, description="Also include malware/tool → technique relationships"),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    """Return technique usage heatmap data for selected threat actor groups.

    When group_ids is empty, aggregates across all groups in the source.
    usage_count = number of distinct actors (groups + software if enabled)
    that have a 'uses' relationship to each technique.
    """
    from collections import defaultdict

    # ── Build actor maps ──────────────────────────────────────────────────────
    group_rows = db.scalars(
        select(MitreGroup).where(MitreGroup.source == source, MitreGroup.deprecated.is_(False))
    ).all()
    group_stix_map: dict[str, str] = {g.stix_id: g.name for g in group_rows}  # stix_id → name

    selected_ids = [gid.strip() for gid in group_ids.split(",")] if group_ids else []
    if selected_ids:
        active_group_stix = {g.stix_id for g in group_rows if g.group_id in selected_ids}
    else:
        active_group_stix = set(group_stix_map.keys())

    software_stix_map: dict[str, str] = {}
    if include_software:
        sw_rows = db.scalars(
            select(MitreSoftware).where(MitreSoftware.source == source, MitreSoftware.deprecated.is_(False))
        ).all()
        software_stix_map = {s.stix_id: s.name for s in sw_rows}

    actor_stix_ids = active_group_stix | set(software_stix_map.keys())

    # ── Fetch all 'uses' → attack-pattern relationships for this source ────────
    rels = db.scalars(
        select(MitreRelationship).where(
            MitreRelationship.source == source,
            MitreRelationship.relationship_type == "uses",
            MitreRelationship.target_type == "attack-pattern",
        )
    ).all()

    # ── Aggregate: target_ref → set[actor_name] ───────────────────────────────
    tech_actors: dict[str, set[str]] = defaultdict(set)
    for r in rels:
        if r.source_ref not in actor_stix_ids:
            continue
        name = group_stix_map.get(r.source_ref) or software_stix_map.get(r.source_ref, "")
        if name:
            tech_actors[r.target_ref].add(name)

    # ── Load all non-deprecated techniques ────────────────────────────────────
    techniques = db.scalars(
        select(MitreTechnique).where(
            MitreTechnique.source == source,
            MitreTechnique.deprecated.is_(False),
        )
    ).all()

    stix_to_tech: dict[str, MitreTechnique] = {t.stix_id: t for t in techniques}

    # ── Build response: include all techniques, coverage from relationships ────
    result: list[MitreHeatmapTechnique] = []
    for t in techniques:
        actors = tech_actors.get(t.stix_id, set())
        result.append(MitreHeatmapTechnique(
            technique_id=t.technique_id,
            stix_id=t.stix_id,
            name=t.name,
            tactics=t.tactics or [],
            is_subtechnique=bool(t.is_subtechnique),
            usage_count=len(actors),
            used_by=sorted(actors)[:30],
        ))

    covered = sum(1 for r in result if r.usage_count > 0)

    return MitreHeatmapResponse(
        tactic_order=_TACTIC_ORDER,
        techniques=result,
        covered=covered,
        total_techniques=len(techniques),
        selected_actors=len(active_group_stix) + (len(software_stix_map) if include_software else 0),
    )


# ── CISA KEV ──────────────────────────────────────────────────────────────────

@router.get("/kev", response_model=CisaKevList)
def list_kev(
    search: str | None = Query(None),
    ransomware_only: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = select(CisaKevEntry)
    if ransomware_only:
        stmt = stmt.where(CisaKevEntry.known_ransomware.is_(True))
    if search:
        q = f"%{search.lower()}%"
        stmt = stmt.where(
            CisaKevEntry.cve_id.ilike(q)
            | CisaKevEntry.vulnerability_name.ilike(q)
            | CisaKevEntry.vendor_project.ilike(q)
            | CisaKevEntry.product.ilike(q)
        )
    stmt = stmt.order_by(CisaKevEntry.date_added.desc().nullsfirst())

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return CisaKevList(
        items=[CisaKevRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


@router.get("/kev/stats", response_model=CisaKevStats)
def get_kev_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    total = db.scalar(select(func.count(CisaKevEntry.id))) or 0
    ransomware = db.scalar(
        select(func.count(CisaKevEntry.id)).where(CisaKevEntry.known_ransomware.is_(True))
    ) or 0

    cutoff = date.today() - timedelta(days=30)
    recent = db.scalar(
        select(func.count(CisaKevEntry.id)).where(CisaKevEntry.date_added >= cutoff)
    ) or 0

    # Monthly counts for the last 24 months
    rows = db.scalars(
        select(CisaKevEntry.date_added).where(CisaKevEntry.date_added.isnot(None))
    ).all()

    by_month: dict[str, int] = defaultdict(int)
    for d in rows:
        key = d.strftime("%Y-%m")
        by_month[key] += 1

    # Sort and limit to last 24 months
    sorted_months = sorted(by_month.items(), key=lambda x: x[0])[-24:]

    return CisaKevStats(
        total_entries=total,
        ransomware_count=ransomware,
        recent_30d=recent,
        by_month=[{"month": m, "count": c} for m, c in sorted_months],
    )


# ── EPSS ───────────────────────────────────────────────────────────────────────

@router.post(
    "/kev/index-corpus",
    dependencies=[Depends(require_admin)],
)
def index_kev_corpus(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    """Re-index all CISA KEV entries into the OpenSearch QA reference corpus.

    Makes KEV vulnerability descriptions searchable in the QA engine
    for controls A.8.8 and A.8.28. Admin only.
    """
    from src.services import kev_reference_service
    result = kev_reference_service.index_from_db(db)
    if "error" in result:
        from fastapi import HTTPException
        raise HTTPException(status_code=503, detail=result["error"])
    return result


@router.get("/epss", response_model=EpssScoreList)
def list_epss(
    min_score: float = Query(0.0, ge=0.0, le=1.0),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    stmt = (
        select(EpssScore)
        .where(EpssScore.score >= min_score)
        .order_by(EpssScore.score.desc())
    )

    total = db.scalar(select(func.count()).select_from(stmt.subquery()))
    items = db.scalars(stmt.offset((page - 1) * per_page).limit(per_page)).all()

    return EpssScoreList(
        items=[EpssScoreRead.model_validate(i) for i in items],
        total=total or 0,
        page=page,
        per_page=per_page,
    )


# ── KEV Audit Report (Phase 26 Task 26.7) ─────────────────────────────────────

@router.get("/kev/audit-report", response_model=KevAuditReport)
def get_kev_audit_report(
    months: int = Query(12, ge=1, le=36, description="Look-back window in months"),
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    """Return all CISA KEV entries from the last N months with their evidence status.

    For each KEV entry, report the most recent linked evidence item (via kev_cve_id).
    Entries without any evidence are flagged 'no_evidence'.
    """
    from src.domain.compliance import Evidence

    cutoff = date.today() - timedelta(days=months * 30)

    kev_entries = db.scalars(
        select(CisaKevEntry)
        .where(CisaKevEntry.date_added >= cutoff)
        .order_by(CisaKevEntry.date_added.desc().nullsfirst())
    ).all()

    # Build a map of cve_id → most recent evidence
    cve_ids = [e.cve_id for e in kev_entries]
    evidence_map: dict[str, Evidence] = {}
    if cve_ids:
        ev_rows = db.scalars(
            select(Evidence)
            .where(Evidence.kev_cve_id.in_(cve_ids))
            .order_by(Evidence.created_at.desc())
        ).all()
        for ev in ev_rows:
            if ev.kev_cve_id not in evidence_map:
                evidence_map[ev.kev_cve_id] = ev

    entries: list[KevAuditEntry] = []
    covered = 0
    ransomware_uncovered = 0

    for kev in kev_entries:
        ev = evidence_map.get(kev.cve_id)
        status = ev.evidence_status.value if ev else "no_evidence"
        if ev:
            covered += 1
        elif kev.known_ransomware:
            ransomware_uncovered += 1

        entries.append(KevAuditEntry(
            cve_id=kev.cve_id,
            vulnerability_name=kev.vulnerability_name,
            vendor_project=kev.vendor_project,
            product=kev.product,
            date_added=kev.date_added,
            due_date=kev.due_date,
            known_ransomware=bool(kev.known_ransomware),
            evidence_status=status,
            evidence_id=str(ev.id) if ev else None,
            evidence_title=ev.title if ev else None,
        ))

    total = len(entries)
    return KevAuditReport(
        total=total,
        covered=covered,
        uncovered=total - covered,
        ransomware_uncovered=ransomware_uncovered,
        months=months,
        generated_at=datetime.now(timezone.utc).isoformat(),
        entries=entries,
    )


# ── NVD CVE (Phase 27) ────────────────────────────────────────────────────────

def _os_client():
    """Get OpenSearch client via search_service."""
    from src.services import search_service
    return search_service.get_client()


def _hit_to_cve(hit: dict) -> NvdCveEntry:
    s = hit.get("_source", {})
    return NvdCveEntry(
        cve_id           = s.get("cve_id", hit.get("_id", "")),
        published        = s.get("published"),
        last_modified    = s.get("last_modified"),
        vuln_status      = s.get("vuln_status"),
        description      = s.get("description"),
        cvss_v4_score    = s.get("cvss_v4_score"),
        cvss_v4_severity = s.get("cvss_v4_severity"),
        cvss_v4_vector   = s.get("cvss_v4_vector"),
        cvss_v3_score    = s.get("cvss_v3_score"),
        cvss_v3_severity = s.get("cvss_v3_severity"),
        cvss_v3_vector   = s.get("cvss_v3_vector"),
        cvss_v2_score    = s.get("cvss_v2_score"),
        cwe_ids          = s.get("cwe_ids") or [],
        cpe_affected     = s.get("cpe_affected") or [],
        in_kev           = bool(s.get("in_kev", False)),
        epss_score       = s.get("epss_score"),
        references       = s.get("references") or [],
    )


def _hit_to_cpe(hit: dict) -> dict:
    s = hit.get("_source", {})
    return dict(
        cpe_uri = s.get("cpe_uri", hit.get("_id", "")),
        part    = s.get("part"),
        vendor  = s.get("vendor"),
        product = s.get("product"),
        version = s.get("version"),
        title   = s.get("title"),
        in_kev  = bool(s.get("in_kev", False)),
        source  = s.get("source"),
    )


@router.get("/cve/stats", response_model=NvdCveStats)
def get_cve_stats(
    _current_user: User = Depends(get_current_user),
):
    """Return CVE index stats for the banner."""
    import os as _os
    from src.services import search_service
    client = _os_client()
    if not client:
        return NvdCveStats(total=0, critical=0, high=0, medium=0, low=0,
                           in_kev=0, with_epss=0, last_indexed=None)

    def _count(query):
        try:
            return client.count(index=search_service.IDX_NVD_CVE, body={"query": query}).get("count", 0)
        except Exception:
            return 0

    def _sev_count(sev: str) -> int:
        return _count({"bool": {"should": [
            {"term": {"cvss_v4_severity": sev}},
            {"term": {"cvss_v3_severity": sev}},
        ], "minimum_should_match": 1}})

    total     = _count({"match_all": {}})
    critical  = _sev_count("CRITICAL")
    high      = _sev_count("HIGH")
    medium    = _sev_count("MEDIUM")
    low       = _sev_count("LOW")
    in_kev    = _count({"term": {"in_kev": True}})
    with_epss = _count({"exists": {"field": "epss_score"}})

    # Last indexed_at
    last_indexed = None
    try:
        r = client.search(
            index=search_service.IDX_NVD_CVE,
            body={"query": {"match_all": {}}, "sort": [{"indexed_at": "desc"}], "_source": ["indexed_at"], "size": 1},
        )
        hits = r.get("hits", {}).get("hits", [])
        if hits:
            last_indexed = hits[0].get("_source", {}).get("indexed_at")
    except Exception:
        pass

    return NvdCveStats(total=total, critical=critical, high=high, medium=medium,
                       low=low, in_kev=in_kev, with_epss=with_epss, last_indexed=last_indexed)


@router.get("/cve/index-stats", response_model=NvdIndexStats)
def get_nvd_index_stats(
    db: DBSession = Depends(get_db),
    _current_user: User = Depends(get_current_user),
):
    """Combined stats for the CVE Explorer info banner (CVE + CPE + KEV totals)."""
    from src.services import search_service

    nvd = search_service.get_nvd_stats()
    kev_total = db.scalar(select(func.count(CisaKevEntry.id))) or 0

    def _last_run(feed_name: str) -> str | None:
        stmt = (
            select(FeedRun.started_at)
            .where(FeedRun.feed_name == feed_name, FeedRun.status == "success")
            .order_by(FeedRun.started_at.desc())
            .limit(1)
        )
        row = db.scalars(stmt).first()
        return row.isoformat() if row else None

    return NvdIndexStats(
        cve_total               = nvd.get("cve_total", 0),
        cpe_total               = nvd.get("cpe_total", 0),
        kev_total               = kev_total,
        last_cve_sync           = _last_run("nist_cve"),
        last_cpe_sync           = _last_run("nist_cpe"),
        nist_api_key_configured = bool(os.environ.get("NIST_API_KEY", "").strip()),
        cpe_full_enabled        = _cpe_full_enabled(db),
    )


def _cpe_full_enabled(db: DBSession) -> bool:
    """DB setting takes precedence over env var."""
    row = db.get(PlatformSetting, "feeds_cpe_full")
    if row is not None:
        return row.value.lower() == "true"
    return os.environ.get("FEEDS_CPE_FULL", "false").lower() == "true"


@router.get("/cve", response_model=NvdCveList)
def list_cve(
    search: str | None = Query(None),
    severity: str | None = Query(None, description="CRITICAL|HIGH|MEDIUM|LOW"),
    kev_only: bool = Query(False),
    min_epss: float = Query(0.0, ge=0.0, le=1.0),
    year: int | None = Query(None, ge=1999, le=2099),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    _current_user: User = Depends(get_current_user),
):
    from src.services import search_service
    client = _os_client()
    if not client:
        return NvdCveList(items=[], total=0, page=page, per_page=per_page)

    must: list[dict] = []
    filter_: list[dict] = []

    if search:
        must.append({"multi_match": {"query": search, "fields": ["description", "cve_id", "cwe_ids"]}})
    if severity:
        filter_.append({"bool": {"should": [
            {"term": {"cvss_v4_severity": severity.upper()}},
            {"term": {"cvss_v3_severity": severity.upper()}},
        ], "minimum_should_match": 1}})
    if kev_only:
        filter_.append({"term": {"in_kev": True}})
    if min_epss > 0:
        filter_.append({"range": {"epss_score": {"gte": min_epss}}})
    if year:
        filter_.append({"range": {"published": {"gte": f"{year}-01-01", "lte": f"{year}-12-31"}}})

    query = {"bool": {"must": must or [{"match_all": {}}], "filter": filter_}}
    # Sort: prefer CVSS 4.0 score when available, fallback to v3
    sort = [
        {"cvss_v4_score": {"order": "desc", "missing": "_last"}},
        {"cvss_v3_score": {"order": "desc", "missing": "_last"}},
        {"published": {"order": "desc"}},
    ]

    try:
        result = client.search(
            index=search_service.IDX_NVD_CVE,
            body={"query": query, "sort": sort, "from": (page - 1) * per_page, "size": per_page},
        )
    except Exception:
        return NvdCveList(items=[], total=0, page=page, per_page=per_page)

    total = result.get("hits", {}).get("total", {})
    total = total.get("value", 0) if isinstance(total, dict) else int(total)
    items = [_hit_to_cve(h) for h in result.get("hits", {}).get("hits", [])]

    return NvdCveList(items=items, total=total, page=page, per_page=per_page)


@router.get("/cve/{cve_id}", response_model=NvdCveEntry)
def get_cve(
    cve_id: str,
    _current_user: User = Depends(get_current_user),
):
    from src.services import search_service
    from fastapi import HTTPException
    client = _os_client()
    if not client:
        raise HTTPException(status_code=503, detail="OpenSearch unavailable")
    try:
        doc = client.get(index=search_service.IDX_NVD_CVE, id=cve_id)
        return _hit_to_cve(doc)
    except Exception:
        raise HTTPException(status_code=404, detail=f"{cve_id} not found")


# ── NVD CPE (Phase 27) ────────────────────────────────────────────────────────

@router.get("/cpe/stats", response_model=NvdCpeStats)
def get_cpe_stats(
    _current_user: User = Depends(get_current_user),
):
    from src.services import search_service
    client = _os_client()
    if not client:
        return NvdCpeStats(total=0, kev_vendor=0, cve_config=0,
                           applications=0, operating_systems=0, hardware=0)

    def _count(query):
        try:
            return client.count(index=search_service.IDX_NVD_CPE, body={"query": query}).get("count", 0)
        except Exception:
            return 0

    return NvdCpeStats(
        total            = _count({"match_all": {}}),
        kev_vendor       = _count({"term": {"source": "kev_vendor"}}),
        cve_config       = _count({"term": {"source": "cve_config"}}),
        applications     = _count({"term": {"part": "a"}}),
        operating_systems= _count({"term": {"part": "o"}}),
        hardware         = _count({"term": {"part": "h"}}),
    )


@router.get("/cpe", response_model=NvdCpeList)
def list_cpe(
    search: str | None = Query(None),
    vendor: str | None = Query(None),
    product: str | None = Query(None),
    part: str | None = Query(None, description="a=application, o=os, h=hardware"),
    source: str | None = Query(None, description="cve_config|kev_vendor"),
    kev_only: bool = Query(False),
    page: int = Query(1, ge=1),
    per_page: int = Query(50, ge=1, le=200),
    _current_user: User = Depends(get_current_user),
):
    from src.services import search_service
    client = _os_client()
    if not client:
        return NvdCpeList(items=[], total=0, page=page, per_page=per_page)

    must: list[dict] = []
    filter_: list[dict] = []

    if search:
        must.append({"multi_match": {"query": search, "fields": ["title", "vendor", "product", "cpe_uri"]}})
    if vendor:
        filter_.append({"term": {"vendor": vendor.lower()}})
    if product:
        filter_.append({"term": {"product": product.lower()}})
    if part:
        filter_.append({"term": {"part": part}})
    if source:
        filter_.append({"term": {"source": source}})
    if kev_only:
        filter_.append({"term": {"in_kev": True}})

    query = {"bool": {"must": must or [{"match_all": {}}], "filter": filter_}}

    try:
        result = client.search(
            index=search_service.IDX_NVD_CPE,
            body={"query": query, "sort": [{"in_kev": {"order": "desc"}}, "_score"], "from": (page - 1) * per_page, "size": per_page},
        )
    except Exception:
        return NvdCpeList(items=[], total=0, page=page, per_page=per_page)

    total = result.get("hits", {}).get("total", {})
    total = total.get("value", 0) if isinstance(total, dict) else int(total)
    items = [NvdCpeEntry(**_hit_to_cpe(h)) for h in result.get("hits", {}).get("hits", [])]

    return NvdCpeList(items=items, total=total, page=page, per_page=per_page)


# ── Feed settings (admin toggle) ───────────────────────────────────────────────

_CPE_FULL_KEY = "feeds_cpe_full"


@router.get("/settings", response_model=FeedSettings, dependencies=[Depends(require_admin)])
def get_feed_settings(db: DBSession = Depends(get_db)):
    """Return current platform feed settings."""
    row = db.get(PlatformSetting, _CPE_FULL_KEY)
    cpe_full = (row.value.lower() == "true") if row else False
    return FeedSettings(feeds_cpe_full=cpe_full)


@router.post("/trigger/{feed_name}", dependencies=[Depends(require_admin)])
def trigger_feed(
    feed_name: str,
    mode: str = Query("full", description="full|delta — only applies to nist_cve"),
):
    """Trigger a feed run immediately. Admin only. Returns 202 if started, 409 if already running."""
    import requests as _req
    from fastapi import HTTPException

    feeds_host = os.environ.get("FEEDS_HOST", "http://isms-core-feeds:8001")
    url = f"{feeds_host}/trigger/{feed_name}"
    if feed_name == "nist_cve":
        url += f"?mode={mode}"

    try:
        resp = _req.post(url, timeout=5)
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Feeds container unreachable: {exc}")

    if resp.status_code == 202:
        return {"status": "triggered", "feed": feed_name, "mode": mode if feed_name == "nist_cve" else None}
    if resp.status_code == 409:
        raise HTTPException(status_code=409, detail=f"Feed '{feed_name}' is already running")
    raise HTTPException(status_code=502, detail=f"Feeds container returned {resp.status_code}: {resp.text}")


@router.patch("/settings", response_model=FeedSettings, dependencies=[Depends(require_admin)])
def patch_feed_settings(
    payload: FeedSettings = Body(...),
    db: DBSession = Depends(get_db),
):
    """Toggle platform feed settings. Changes take effect on the next scheduled run."""
    from datetime import datetime, timezone
    row = db.get(PlatformSetting, _CPE_FULL_KEY)
    if row:
        row.value = "true" if payload.feeds_cpe_full else "false"
        row.updated_at = datetime.now(timezone.utc)
    else:
        row = PlatformSetting(
            key=_CPE_FULL_KEY,
            value="true" if payload.feeds_cpe_full else "false",
        )
        db.add(row)
    db.commit()
    return FeedSettings(feeds_cpe_full=payload.feeds_cpe_full)


# ── Internal: feed failure notification (called by feeds container) ────────────

@router.post("/internal/notify-failure", include_in_schema=False)
def internal_notify_feed_failure(
    request: Request,
    payload: dict = Body(...),
):
    """Called by the feeds container when a pull fails. Queues a notification email.

    Authenticated via CONNECTORS_WORKER_SECRET (shared secret, same as connectors runner).
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

    from src.services.notification_service import notify_feed_failure
    notify_feed_failure.delay(
        feed_name=feed_name,
        error_message=error_message,
        run_id=run_id,
    )
    logger.info("Queued feed failure notification for %s", feed_name)
    return {"queued": True, "feed_name": feed_name}
