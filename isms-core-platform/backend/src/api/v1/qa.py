import logging
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import require_role
from src.database.enums import CorrelationMethod, QAStatus, UserRole
from src.database.session import get_db
from src.domain.control_groups import ControlGroup
from src.domain.qa import CorrelationResult, SynonymRule
from src.schemas.qa import (
    CorrelationResultRead,
    ExistenceRunResult,
    KeywordRunResult,
    QASummary,
    QASummaryBucket,
    SemanticRunResult,
    SynonymRuleCreate,
    SynonymRulePatch,
    SynonymRuleRead,
)
from src.services import qa_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/qa", tags=["qa"])


@router.post(
    "/run-existence",
    response_model=ExistenceRunResult,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def run_existence_check(db: DBSession = Depends(get_db)):
    """Run the existence checker for all control groups.

    Checks that each control group has the required artefacts:
    - Framework: POL + UG + TG + Assessment
    - Operational: OP-POL + Assessment

    Replaces any previous existence check results.
    """
    stats = qa_service.run_existence_check(db)
    return ExistenceRunResult(
        total=stats["total"],
        pass_count=stats["pass"],
        warning_count=stats["warning"],
        fail_count=stats["fail"],
        needs_review_count=stats["needs_review"],
        duration_ms=stats["duration_ms"],
        run_date=datetime.now(timezone.utc).isoformat(),
    )


@router.post(
    "/run-keyword",
    response_model=KeywordRunResult,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def run_keyword_check(db: DBSession = Depends(get_db)):
    """Run the keyword correlation check for all control groups.

    Extracts keywords from ISO 27001 control descriptions and checks whether
    those keywords appear in the UG/TG implementation content in OpenSearch.

    Replaces any previous keyword check results.
    """
    stats = qa_service.run_keyword_check(db)
    return KeywordRunResult(
        total=stats["total"],
        pass_count=stats["pass"],
        warning_count=stats["warning"],
        fail_count=stats["fail"],
        needs_review_count=stats["needs_review"],
        duration_ms=stats["duration_ms"],
        run_date=datetime.now(timezone.utc).isoformat(),
    )


@router.post(
    "/run-semantic",
    response_model=SemanticRunResult,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def run_semantic_check(db: DBSession = Depends(get_db)):
    """Run semantic similarity check using sentence-transformers (all-MiniLM-L6-v2).

    Encodes ISO control text and UG/TG implementation content as embedding vectors,
    then computes cosine similarity. Runs entirely on CPU — no API key required.

    Replaces any previous semantic results.
    """
    try:
        stats = qa_service.run_semantic_mini_check(db)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    return SemanticRunResult(
        total=stats["total"],
        pass_count=stats["pass"],
        warning_count=stats["warning"],
        fail_count=stats["fail"],
        needs_review_count=stats["needs_review"],
        duration_ms=stats["duration_ms"],
        run_date=datetime.now(timezone.utc).isoformat(),
        method="semantic",
    )


@router.post(
    "/run-semantic-claude",
    response_model=SemanticRunResult,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def run_semantic_claude(db: DBSession = Depends(get_db)):
    """Run semantic analysis using Anthropic Claude API.

    Sends ISO control requirements + implementation content to Claude and asks it to
    score alignment (0–100) with reasoning and a list of identified gaps.

    Requires ANTHROPIC_API_KEY to be set. Uses the configured ai_model (default: Haiku).
    Replaces any previous semantic_claude results.
    """
    try:
        stats = qa_service.run_semantic_claude_check(db)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return SemanticRunResult(
        total=stats["total"],
        pass_count=stats["pass"],
        warning_count=stats["warning"],
        fail_count=stats["fail"],
        needs_review_count=stats["needs_review"],
        duration_ms=stats["duration_ms"],
        run_date=datetime.now(timezone.utc).isoformat(),
        method="semantic_claude",
    )


@router.get(
    "/results",
    response_model=list[CorrelationResultRead],
)
def list_results(
    product_type: str | None = None,  # "framework" | "operational"
    status: str | None = None,         # "pass" | "warning" | "fail" | "needs_review"
    method: str = "existence",         # "existence" | "keyword"
    limit: int = 200,
    offset: int = 0,
    db: DBSession = Depends(get_db),
):
    """List correlation results, optionally filtered by method, product type and QA status."""
    try:
        method_enum = CorrelationMethod(method)
    except ValueError:
        method_enum = CorrelationMethod.EXISTENCE

    q = (
        select(CorrelationResult)
        .where(CorrelationResult.correlation_method == method_enum)
        .order_by(CorrelationResult.run_date.desc())
        .limit(limit)
        .offset(offset)
    )
    if status:
        try:
            q = q.where(CorrelationResult.qa_status == QAStatus(status))
        except ValueError:
            pass

    rows = db.execute(q).scalars().all()

    results = []
    for row in rows:
        # Filter by product_type from metadata (no dedicated column)
        pt = (row.metadata_ or {}).get("product_type", "")
        if product_type and pt != product_type:
            continue

        # Resolve control group name
        group = db.get(ControlGroup, row.control_group_id)
        results.append(CorrelationResultRead(
            id=row.id,
            control_group_id=row.control_group_id,
            control_group_code=group.group_code if group else "",
            control_group_name=group.name if group else "",
            document_id=row.document_id,
            product_type=pt,
            correlation_method=row.correlation_method.value,
            correlation_strength=float(row.correlation_strength),
            qa_status=row.qa_status.value,
            coverage_keywords=row.coverage_keywords or [],
            missing_keywords=row.missing_keywords or [],
            run_date=row.run_date,
            metadata=row.metadata_ or {},
        ))
    return results


@router.get(
    "/summary",
    response_model=QASummary,
)
def get_summary(
    method: str = "existence",
    product_type: str | None = None,
    db: DBSession = Depends(get_db),
):
    """Aggregated QA summary: pass/warning/fail counts by product.

    Pass ?method=keyword and optionally ?product_type=framework|operational|privacy|cloud|isms
    to filter the summary to a specific product.
    """
    try:
        method_enum = CorrelationMethod(method)
    except ValueError:
        method_enum = CorrelationMethod.EXISTENCE

    rows = db.execute(
        select(CorrelationResult).where(
            CorrelationResult.correlation_method == method_enum
        )
    ).scalars().all()

    # Filter to a specific product when requested
    if product_type and product_type != "all":
        rows = [r for r in rows if (r.metadata_ or {}).get("product_type", "") == product_type]

    _EMPTY = lambda: {"total": 0, "pass": 0, "warning": 0, "fail": 0, "needs_review": 0}
    last_run: datetime | None = None
    fw  = _EMPTY()
    op  = _EMPTY()
    prv = _EMPTY()
    cld = _EMPTY()

    _BUCKET_MAP = {
        "framework":   fw,
        "isms":        fw,
        "operational": op,
        "privacy":     prv,
        "cloud":       cld,
    }

    for row in rows:
        if last_run is None or row.run_date > last_run:
            last_run = row.run_date
        pt = (row.metadata_ or {}).get("product_type", "")
        bucket = _BUCKET_MAP.get(pt, op)
        bucket["total"] += 1
        bucket[row.qa_status.value] += 1

    def _bucket(b: dict) -> QASummaryBucket:
        total = b["total"] or 1
        return QASummaryBucket(
            total=b["total"],
            pass_count=b["pass"],
            warning_count=b["warning"],
            fail_count=b["fail"],
            needs_review_count=b["needs_review"],
            pass_rate=round(b["pass"] / total, 3),
        )

    all_total = fw["total"] + op["total"] + prv["total"] + cld["total"] or 1
    all_pass  = fw["pass"]  + op["pass"]  + prv["pass"]  + cld["pass"]

    return QASummary(
        last_run=last_run,
        framework=_bucket(fw),
        operational=_bucket(op),
        privacy=_bucket(prv),
        cloud=_bucket(cld),
        overall_pass_rate=round(all_pass / all_total, 3),
    )


# ── Synonym management ────────────────────────────────────────────────────────


@router.get("/synonyms", response_model=list[SynonymRuleRead])
def list_synonyms(db: DBSession = Depends(get_db)):
    """List all synonym rules, ordered alphabetically by keyword."""
    return db.execute(
        select(SynonymRule).order_by(SynonymRule.keyword)
    ).scalars().all()


@router.post(
    "/synonyms",
    response_model=SynonymRuleRead,
    status_code=201,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def create_synonym(body: SynonymRuleCreate, db: DBSession = Depends(get_db)):
    """Add a new synonym rule. Keyword must be unique."""
    existing = db.execute(
        select(SynonymRule).where(SynonymRule.keyword == body.keyword.lower())
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail=f"Synonym rule for '{body.keyword}' already exists.")
    rule = SynonymRule(
        id=uuid.uuid4(),
        keyword=body.keyword.lower(),
        synonyms=[s.lower() for s in body.synonyms],
        notes=body.notes,
    )
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


@router.patch(
    "/synonyms/{rule_id}",
    response_model=SynonymRuleRead,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def update_synonym(rule_id: uuid.UUID, body: SynonymRulePatch, db: DBSession = Depends(get_db)):
    """Update synonyms list or notes for an existing rule."""
    rule = db.get(SynonymRule, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Synonym rule not found.")
    if body.synonyms is not None:
        rule.synonyms = [s.lower() for s in body.synonyms]
    if body.notes is not None:
        rule.notes = body.notes
    db.commit()
    db.refresh(rule)
    return rule


@router.delete(
    "/synonyms/{rule_id}",
    status_code=204,
    dependencies=[Depends(require_role(UserRole.ADMIN, UserRole.ISMS_MANAGER))],
)
def delete_synonym(rule_id: uuid.UUID, db: DBSession = Depends(get_db)):
    """Delete a synonym rule."""
    rule = db.get(SynonymRule, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Synonym rule not found.")
    db.delete(rule)
    db.commit()
