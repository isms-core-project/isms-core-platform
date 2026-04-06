"""Phase 25 — Threat Intelligence & Vulnerability Feeds API."""

import logging
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.feeds import CisaKevEntry, EpssScore, FeedRun, MitreTechnique
from src.domain.users import User
from src.schemas.feeds import (
    CisaKevList,
    CisaKevRead,
    CisaKevStats,
    EpssScoreList,
    EpssScoreRead,
    FeedStatusItem,
    FeedStatusResponse,
    MitreAttackStats,
    MitreTechniqueList,
    MitreTechniqueRead,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/feeds", tags=["feeds"])

# Canonical feed names and display labels
_FEEDS = [
    ("mitre_attack_v18", "MITRE ATT&CK v18",  "FEEDS_MITRE_ENABLED"),
    ("mitre_atlas",      "MITRE ATLAS",         "FEEDS_ATLAS_ENABLED"),
    ("cisa_kev",         "CISA KEV",            "FEEDS_KEV_ENABLED"),
    ("epss",             "FIRST EPSS",          "FEEDS_EPSS_ENABLED"),
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
