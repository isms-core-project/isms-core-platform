import logging
import uuid
import shutil
import tempfile

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy import delete as sql_delete, func, select, text
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_role, require_admin
from src.database.enums import UserRole
from src.database.session import get_db
from src.domain.assessments import Assessment, AssessmentItem, AssessmentSheet
from src.domain.compliance import Evidence, Gap
from src.domain.connectors import ConnectorEvidence
from src.domain.content import Implementation, Policy, Requirement
from src.domain.control_groups import ControlGroup
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl
from src.domain.qa import CorrelationResult
from src.domain.organisations import Organisation
from src.domain.system import AuditLog, DataLoadHistory
from src.domain.users import User
from src.core.config import get_settings
from src.importers.policy_importer import PolicyImporter
from src.importers.imp_importer import ImpImporter
from src.importers.framework_importer import FrameworkWorkbookImporter
from src.importers.external_importer import ExternalDocImporter, SUPPORTED_EXTENSIONS
from src.importers.operational_importer import OperationalChecklistImporter
from src.importers.privacy_checklist_importer import PrivacyChecklistImporter
from src.importers.tasks import (
    import_framework_workbooks_task,
    import_implementations_task,
    import_operational_task,
    import_privacy_task,
    import_policies_task,
)
from src.core.security import hash_password
from src.schemas.search import SearchStatus
from src.schemas.system import AuditLogPage, AuditLogRead, LoadHistoryRead, ServiceHealth, SysInfoResponse, SystemStatus
from src.services import qa_service
from src.services.audit_service import CAT_SECURITY, SEV_INFO, SEV_WARNING, log_event
from src.schemas.users import UserCreate, UserPatch, UserRead
from src.services import search_service
from src.services.loader_service import load_all_bundles

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get(
    "/system/status",
    response_model=SystemStatus,
    dependencies=[Depends(require_admin)],
)
def system_status(db: DBSession = Depends(get_db)):
    def count(model):
        return db.scalar(select(func.count()).select_from(model))

    return SystemStatus(
        frameworks=count(Framework),
        framework_controls=count(FrameworkControl),
        cross_framework_mappings=count(CrossFrameworkMapping),
        control_groups=count(ControlGroup),
        policies=count(Policy),
        requirements=count(Requirement),
        implementations=count(Implementation),
        assessments=count(Assessment),
        evidence=count(Evidence),
        automated_evidence=count(ConnectorEvidence),
        gaps=count(Gap),
        users=count(User),
        load_history_count=count(DataLoadHistory),
    )


@router.get(
    "/sysinfo",
    response_model=SysInfoResponse,
    dependencies=[Depends(require_admin)],
)
def get_sysinfo(db: DBSession = Depends(get_db)):
    """Consolidated system information: service health, DB counts, config, last sync."""
    import time
    from datetime import datetime, timezone

    settings = get_settings()
    services: list[ServiceHealth] = []

    # API — always ok if we're here
    services.append(ServiceHealth(name="api", status="ok", latency_ms=0, detail="FastAPI"))

    # PostgreSQL
    try:
        t0 = time.monotonic()
        db.execute(text("SELECT 1"))
        services.append(ServiceHealth(
            name="database", status="ok",
            latency_ms=int((time.monotonic() - t0) * 1000),
            detail="PostgreSQL",
        ))
    except Exception as e:
        services.append(ServiceHealth(name="database", status="error", detail=str(e)[:120]))

    # Redis
    try:
        import redis as _redis
        t0 = time.monotonic()
        r = _redis.from_url(settings.redis_url, socket_timeout=2)
        r.ping()
        services.append(ServiceHealth(
            name="redis", status="ok",
            latency_ms=int((time.monotonic() - t0) * 1000),
            detail="Redis",
        ))
    except Exception as e:
        services.append(ServiceHealth(name="redis", status="error", detail=str(e)[:120]))

    # Celery Worker
    try:
        from src.worker import celery_app
        inspector = celery_app.control.inspect(timeout=2.0)
        pong = inspector.ping()
        if pong:
            worker_count = len(pong)
            services.append(ServiceHealth(
                name="celery", status="ok",
                detail=f"{worker_count} worker{'s' if worker_count != 1 else ''} active",
            ))
        else:
            services.append(ServiceHealth(
                name="celery", status="unavailable", detail="No workers responding",
            ))
    except Exception:
        services.append(ServiceHealth(name="celery", status="unavailable", detail="Worker unreachable"))

    # OpenSearch
    os_raw = search_service.get_search_status()
    if os_raw.get("available"):
        services.append(ServiceHealth(
            name="opensearch", status="ok",
            detail=f"Cluster: {os_raw.get('cluster_status', 'unknown')}",
        ))
    else:
        services.append(ServiceHealth(
            name="opensearch", status="unavailable",
            detail=str(os_raw.get("error", "Not available"))[:120],
        ))

    # DB counts
    def count(model):
        return db.scalar(select(func.count()).select_from(model))

    db_counts = SystemStatus(
        frameworks=count(Framework),
        framework_controls=count(FrameworkControl),
        cross_framework_mappings=count(CrossFrameworkMapping),
        control_groups=count(ControlGroup),
        policies=count(Policy),
        requirements=count(Requirement),
        implementations=count(Implementation),
        assessments=count(Assessment),
        evidence=count(Evidence),
        automated_evidence=count(ConnectorEvidence),
        gaps=count(Gap),
        users=count(User),
        load_history_count=count(DataLoadHistory),
    )

    # Last sync
    last_history = db.execute(
        select(DataLoadHistory).order_by(DataLoadHistory.created_at.desc()).limit(1)
    ).scalar_one_or_none()

    # Effective AI model (org settings override config default)
    org = db.execute(select(Organisation)).scalar_one_or_none()
    effective_model = (
        (org.settings or {}).get("ai_model") or settings.ai_model
        if org else settings.ai_model
    )

    return SysInfoResponse(
        generated_at=datetime.now(timezone.utc),
        services=services,
        db_counts=db_counts,
        opensearch_cluster_status=os_raw.get("cluster_status"),
        opensearch_indices=os_raw.get("indices"),
        platform="ISMS CORE",
        standard="ISO 27001:2022 · ISO 27701:2025 · ISO 27018:2025 · ISO 42001:2023",
        api_version="v1",
        framework_path=settings.framework_path,
        operational_path=settings.operational_path,
        privacy_path=settings.privacy_path,
        cloud_path=settings.cloud_path,
        ai_path=settings.ai_path,
        sec_path=settings.sec_path,
        ext_path=settings.ext_path,
        datasets_path=settings.datasets_path,
        log_level=settings.log_level,
        debug=settings.debug,
        opensearch_url=settings.opensearch_url,
        last_sync_at=last_history.created_at if last_history else None,
        last_sync_type=last_history.bundle_type if last_history else None,
        last_sync_status=last_history.load_status if last_history else None,
        smtp_enabled=bool(settings.mail_host),
        smtp_host=settings.mail_host or "",
        smtp_port=settings.mail_port,
        smtp_from=settings.mail_from,
        notification_email=settings.notification_email or "",
        platform_url=settings.platform_url,
        ai_model=effective_model,
    )


@router.post(
    "/email/test",
    dependencies=[Depends(require_admin)],
)
def send_test_email(body: dict, current_user=Depends(get_current_user)):
    """Send a test email to verify SMTP configuration.

    Body: {"recipient": "user@example.com"}
    """
    from src.services.email_service import is_enabled, render_template, send_email

    recipient = (body.get("recipient") or "").strip()
    if not recipient:
        raise HTTPException(status_code=422, detail="recipient is required")

    if not is_enabled():
        raise HTTPException(
            status_code=503,
            detail="Email is not configured (MAIL_HOST is not set).",
        )

    html = render_template("welcome.html", {
        "full_name": None,
        "email": recipient,
        "role": "admin",
        "platform_url": get_settings().platform_url,
        "created_by": current_user.email,
    })

    ok = send_email(
        to=[recipient],
        subject="ISMS CORE — SMTP Test Email",
        html_body=html,
    )

    if not ok:
        raise HTTPException(status_code=502, detail="Email send failed — check server logs.")

    return {"ok": True, "recipient": recipient}


@router.post("/notification/test", dependencies=[Depends(get_current_user)])
def send_test_notification(body: dict, current_user=Depends(get_current_user)):
    """Send a sample notification email to the calling user to verify a specific event template.

    Body: {"event_type": "email.feed_failure"}
    Sends to current_user.email using realistic placeholder data.
    """
    from src.services.email_service import is_enabled, render_template, send_email

    event_type = (body.get("event_type") or "").strip()
    if not event_type:
        raise HTTPException(status_code=422, detail="event_type is required")

    if not is_enabled():
        raise HTTPException(status_code=503, detail="Email is not configured (MAIL_HOST is not set).")

    settings = get_settings()
    base = settings.platform_url.rstrip("/")
    # Prefer NOTIFICATION_EMAIL override; fall back to the logged-in user's DB email
    recipient = settings.notification_email or current_user.email
    name = current_user.full_name or recipient

    TEMPLATES: dict[str, tuple[str, str, dict]] = {
        "email.gap_assigned": ("gap_assigned.html", "Test: Gap Assigned — ISMS CORE", {
            "full_name": name, "email": recipient,
            "gap_title": "[TEST] Patch management gap — A.8.8",
            "control_ref": "a.8.8", "control_name": "Management of Technical Vulnerabilities",
            "severity": "high", "due_date": "30 Apr 2026",
            "description": "This is a sample gap notification. No action required.",
            "assigned_by": None, "gap_url": f"{base}/gaps",
        }),
        "email.evidence_expiry": ("evidence_expiry.html", "Test: Evidence Expiring — ISMS CORE", {
            "full_name": name, "email": recipient,
            "evidence_title": "[TEST] Vulnerability scan report Q1 2026",
            "control_ref": "a.8.8", "control_name": "Management of Technical Vulnerabilities",
            "expiry_date": "30 Apr 2026", "days_remaining": 14, "expired": False,
            "owner": recipient, "evidence_url": f"{base}/evidence",
        }),
        "email.qa_fail": ("qa_fail.html", "Test: QA Check — ISMS CORE", {
            "full_name": name, "email": recipient,
            "product": "Framework", "checked_at": "19 Apr 2026 08:00 UTC",
            "pass_pct": 72, "fail_count": 2, "warning_count": 1,
            "failures": [
                {"control_ref": "A.8.8", "status": "FAIL", "missing": ["IMP-TG", "SCR"]},
                {"control_ref": "A.8.23", "status": "WARN", "missing": ["REF"]},
            ],
            "qa_url": f"{base}/qa",
        }),
        "email.import_completed": ("import_completed.html", "Test: Import Completed — ISMS CORE", {
            "full_name": name, "email": recipient,
            "import_type": "Policy Import (test)",
            "completed_at": "19 Apr 2026 10:00 UTC",
            "stats": {"policies_found": 12, "policies_imported": 10, "policies_skipped": 2},
            "errors": [],
            "system_url": f"{base}/system",
        }),
        "email.feed_failure": ("feed_failure.html", "Test: Feed Pull Failed — ISMS CORE", {
            "full_name": name, "email": recipient,
            "feed_name": "cisa_kev (test)",
            "error_message": "ConnectionError: Failed to connect to api.cisa.gov — this is a test notification.",
            "run_id": "00000000-0000-0000-0000-000000000001",
            "failed_at": "19 Apr 2026 03:00 UTC",
            "feeds_url": f"{base}/threat-intel",
        }),
        "email.connector_failure": ("connector_failure.html", "Test: Connector Sync Failed — ISMS CORE", {
            "full_name": name, "email": recipient,
            "connector_name": "Test Connector",
            "connector_id": "00000000-0000-0000-0000-000000000001",
            "error_message": "AuthenticationError: API token rejected — this is a test notification.",
            "failed_at": "19 Apr 2026 06:00 UTC",
            "connectors_url": f"{base}/connectors",
        }),
    }

    entry = TEMPLATES.get(event_type)
    if not entry:
        raise HTTPException(status_code=422, detail=f"Unknown event_type: {event_type}")

    template_file, subject, ctx = entry
    html = render_template(template_file, ctx)
    ok = send_email(to=[recipient], subject=subject, html_body=html)

    if not ok:
        raise HTTPException(status_code=502, detail="Email send failed — check server logs.")

    return {"ok": True, "recipient": recipient, "event_type": event_type}


@router.get(
    "/load-history",
    response_model=list[LoadHistoryRead],
    dependencies=[Depends(require_admin)],
)
def list_load_history(db: DBSession = Depends(get_db)):
    return (
        db.execute(
            select(DataLoadHistory).order_by(DataLoadHistory.created_at.desc())
        )
        .scalars()
        .all()
    )


@router.post(
    "/load",
    dependencies=[Depends(require_admin)],
)
def trigger_load(db: DBSession = Depends(get_db)):
    stats = load_all_bundles(db)
    qa_service.run_existence_check(db)
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-policies",
    dependencies=[Depends(require_admin)],
)
def trigger_import_policies(db: DBSession = Depends(get_db)):
    """Synchronous policy import from mounted directories."""
    settings = get_settings()
    importer = PolicyImporter(
        db,
        settings.framework_path,
        settings.operational_path,
        extra_paths=settings.extra_paths,
    )
    stats = importer.import_all()
    db.commit()
    qa_service.run_existence_check(db)
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-policies/async",
    dependencies=[Depends(require_admin)],
)
def trigger_import_policies_async():
    """Async policy import via Celery worker."""
    task = import_policies_task.delay()
    return {"status": "queued", "task_id": task.id}


@router.post(
    "/import-framework-workbooks",
    dependencies=[Depends(require_admin)],
)
def trigger_import_framework_workbooks(db: DBSession = Depends(get_db)):
    """Synchronous import of 188 framework workbook structures from SCR generators."""
    settings = get_settings()
    importer = FrameworkWorkbookImporter(db, settings.framework_path)
    stats = importer.import_all()
    db.commit()
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-framework-workbooks/async",
    dependencies=[Depends(require_admin)],
)
def trigger_import_framework_workbooks_async():
    """Async framework workbook import via Celery worker."""
    task = import_framework_workbooks_task.delay()
    return {"status": "queued", "task_id": task.id}


@router.post(
    "/import-operational",
    dependencies=[Depends(require_admin)],
)
def trigger_import_operational(db: DBSession = Depends(get_db)):
    """Synchronous import of 53 operational compliance checklists from SCR scripts."""
    settings = get_settings()
    importer = OperationalChecklistImporter(db, settings.operational_path)
    stats = importer.import_all()
    db.commit()
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-operational/async",
    dependencies=[Depends(require_admin)],
)
def trigger_import_operational_async():
    """Async operational import via Celery worker."""
    task = import_operational_task.delay()
    return {"status": "queued", "task_id": task.id}


@router.post(
    "/import-privacy",
    dependencies=[Depends(require_admin)],
)
def trigger_import_privacy(db: DBSession = Depends(get_db)):
    """Synchronous import of PRIV + CLD compliance checklists from SCR scripts."""
    settings = get_settings()
    extra = [p for p in settings.extra_paths.split(",") if p.strip()]
    importer = PrivacyChecklistImporter(db, extra)
    stats = importer.import_all()
    db.commit()
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-privacy/async",
    dependencies=[Depends(require_admin)],
)
def trigger_import_privacy_async():
    """Async PRIV + CLD checklist import via Celery worker."""
    task = import_privacy_task.delay()
    return {"status": "queued", "task_id": task.id}


@router.post(
    "/import-implementations",
    dependencies=[Depends(require_admin)],
)
def trigger_import_implementations(db: DBSession = Depends(get_db)):
    """Synchronous IMP import from Framework mount."""
    settings = get_settings()
    importer = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
    stats = importer.import_all()
    db.commit()
    qa_service.run_existence_check(db)
    return {"status": "ok", "stats": stats}


@router.post(
    "/import-implementations/async",
    dependencies=[Depends(require_admin)],
)
def trigger_import_implementations_async():
    """Async IMP import via Celery worker."""
    task = import_implementations_task.delay()
    return {"status": "queued", "task_id": task.id}


@router.get(
    "/search/status",
    response_model=SearchStatus,
    dependencies=[Depends(require_admin)],
)
def get_search_status():
    """Return OpenSearch cluster health and index document counts."""
    status = search_service.get_search_status()
    return SearchStatus(**status)


@router.post(
    "/reindex",
    dependencies=[Depends(require_admin)],
)
def trigger_reindex(db: DBSession = Depends(get_db)):
    """Full reindex: delete indices, recreate, re-parse all files and index.

    Reads from filesystem mounts (not DB) because section content is not
    stored in the database. Synchronous — takes ~5 seconds for 651 files.
    """
    if not search_service.is_available():
        raise HTTPException(status_code=503, detail="OpenSearch not available")

    # Delete and recreate indices
    search_service.delete_indices()
    search_service.ensure_indices()

    settings = get_settings()
    stats = {"implementations": 0, "policies": 0, "errors": 0}

    # Reindex implementations
    try:
        from src.importers.parsers.base import detect_impl_type

        imp_importer = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
        imp_files = imp_importer._discover_implementations()
        for file_path in imp_files:
            try:
                ext = file_path.suffix.lower()
                parser = imp_importer.parsers.get(ext)
                if not parser:
                    continue
                parsed = parser.parse(file_path)
                group_id = imp_importer._resolve_control_group(parsed.group_code)
                if not group_id:
                    folder_code = imp_importer._group_code_from_path(file_path)
                    if folder_code:
                        group_id = imp_importer._resolve_control_group(folder_code)
                if not group_id:
                    continue
                group_name = imp_importer._get_group_name(group_id) or ""
                # Use canonical DB group_code (not parsed) so stacked controls like
                # ISMS-IMP-A.8.20-22-S1-UG index under "a.8.20-22", not "a.8.20-22-s1-ug"
                db_group_code = imp_importer._get_group_code(group_id) or parsed.group_code
                impl_type = (
                    parsed.policy_type
                    if parsed.policy_type in ("UG", "TG")
                    else detect_impl_type(parsed.document_id)
                )
                search_service.index_implementation(
                    document_id=parsed.document_id,
                    title=parsed.title,
                    impl_type=impl_type,
                    control_group_code=db_group_code,
                    control_group_name=group_name,
                    product_type="framework",
                    sections=[
                        {"heading": s.heading, "body": s.body, "level": s.level}
                        for s in parsed.sections
                    ],
                    word_count=parsed.word_count,
                    file_path=str(file_path),
                    metadata=parsed.metadata,
                )
                stats["implementations"] += 1
            except Exception as e:
                stats["errors"] += 1
                logger.error("Reindex error (impl): %s: %s", file_path.name, e)
    except Exception as e:
        logger.error("Implementation reindex scan failed: %s", e)

    # Reindex policies
    try:
        pol_importer = PolicyImporter(
            db,
            settings.framework_path,
            settings.operational_path,
            extra_paths=settings.extra_paths,
        )
        pol_files = pol_importer._discover_policies()
        for file_path, _hint_product in pol_files:
            try:
                ext = file_path.suffix.lower()
                parser = pol_importer.parsers.get(ext)
                if not parser:
                    continue
                parsed = parser.parse(file_path)
                group_id = pol_importer._resolve_control_group(parsed.group_code)
                if not group_id:
                    folder_code = pol_importer._group_code_from_path(file_path)
                    if folder_code:
                        group_id = pol_importer._resolve_control_group(folder_code)
                if not group_id:
                    continue
                group_name = pol_importer._get_group_name(group_id) or ""
                requirements = pol_importer._extract_requirements(parsed)
                search_service.index_policy(
                    document_id=parsed.document_id,
                    title=parsed.title,
                    policy_type=parsed.policy_type,
                    product_type=parsed.product_type,
                    control_group_code=parsed.group_code,
                    control_group_name=group_name,
                    sections=[
                        {"heading": s.heading, "body": s.body, "level": s.level}
                        for s in parsed.sections
                    ],
                    requirements=[
                        {
                            "text": r["text"],
                            "type": r["type"],
                            "section": r["section"],
                        }
                        for r in requirements
                    ],
                    word_count=parsed.word_count,
                    metadata=parsed.metadata,
                )
                stats["policies"] += 1
            except Exception as e:
                stats["errors"] += 1
                logger.error("Reindex error (policy): %s: %s", file_path.name, e)
    except Exception as e:
        logger.error("Policy reindex scan failed: %s", e)

    return {"status": "ok", "stats": stats}


# ---------------------------------------------------------------------------
# Orphan scanner
# ---------------------------------------------------------------------------


@router.get(
    "/orphans",
    dependencies=[Depends(require_admin)],
)
def scan_orphans(db: DBSession = Depends(get_db)):
    """Scan DB for implementation and policy records whose file_path no longer exists on disk."""
    from pathlib import Path

    orphaned_implementations = []
    orphaned_policies = []

    impls = db.execute(
        select(Implementation.document_id, Implementation.file_path)
        .where(Implementation.file_path.isnot(None))
    ).all()
    for doc_id, file_path in impls:
        if file_path and not Path(file_path).exists():
            orphaned_implementations.append({"document_id": doc_id, "file_path": file_path})

    pols = db.execute(
        select(Policy.document_id, Policy.file_path)
        .where(Policy.file_path.isnot(None))
    ).all()
    for doc_id, file_path in pols:
        if file_path and not Path(file_path).exists():
            orphaned_policies.append({"document_id": doc_id, "file_path": file_path})

    total = len(orphaned_implementations) + len(orphaned_policies)
    logger.info("Orphan scan: %d implementations, %d policies", len(orphaned_implementations), len(orphaned_policies))
    return {
        "total": total,
        "implementations": orphaned_implementations,
        "policies": orphaned_policies,
    }


@router.delete(
    "/orphans",
    dependencies=[Depends(require_admin)],
)
def purge_orphans(db: DBSession = Depends(get_db)):
    """Delete all implementation and policy records whose file_path no longer exists on disk."""
    from pathlib import Path

    impl_ids = []
    pol_ids = []

    impls = db.execute(
        select(Implementation.id, Implementation.document_id, Implementation.file_path)
        .where(Implementation.file_path.isnot(None))
    ).all()
    for row_id, doc_id, file_path in impls:
        if file_path and not Path(file_path).exists():
            impl_ids.append(row_id)

    pols = db.execute(
        select(Policy.id, Policy.document_id, Policy.file_path)
        .where(Policy.file_path.isnot(None))
    ).all()
    for row_id, doc_id, file_path in pols:
        if file_path and not Path(file_path).exists():
            pol_ids.append(row_id)

    if impl_ids:
        db.execute(Implementation.__table__.delete().where(Implementation.id.in_(impl_ids)))
    if pol_ids:
        db.execute(Policy.__table__.delete().where(Policy.id.in_(pol_ids)))
    db.commit()

    deleted = {"implementations": len(impl_ids), "policies": len(pol_ids)}
    logger.info("Orphan purge: deleted %s", deleted)
    return {"status": "ok", "deleted": deleted}


# ---------------------------------------------------------------------------
# Content reset
# ---------------------------------------------------------------------------


@router.post(
    "/reset-content",
    dependencies=[Depends(require_admin)],
)
def reset_content(db: DBSession = Depends(get_db)):
    """Wipe all imported content (POLs, IMPs, Assessments, QA results) and re-import from source.

    Deletes: Policy, Requirement, Implementation, Assessment (+ sheets/items), CorrelationResult.
    Preserves: ControlGroups, Frameworks, FrameworkControls, CrossFrameworkMappings, Users, Evidence, Gaps.
    Then re-runs: import-policies, import-implementations, import-framework-workbooks, existence check.
    Also clears and rebuilds OpenSearch indices.
    """
    settings = get_settings()

    # 1 — Delete imported content in dependency order
    deleted: dict[str, int] = {}

    for model, label in [
        (AssessmentItem, "assessment_items"),
        (AssessmentSheet, "assessment_sheets"),
        (Assessment, "assessments"),
        (Requirement, "requirements"),
        (Policy, "policies"),
        (Implementation, "implementations"),
        (CorrelationResult, "qa_results"),
    ]:
        result = db.execute(
            model.__table__.delete()  # type: ignore[attr-defined]
        )
        deleted[label] = result.rowcount
    db.commit()
    logger.info("reset-content: deleted %s", deleted)

    # 2 — Clear OpenSearch indices
    if search_service.is_available():
        try:
            search_service.delete_indices()
            search_service.ensure_indices()
            logger.info("reset-content: OpenSearch indices rebuilt")
        except Exception as e:
            logger.warning("reset-content: OpenSearch reset failed: %s", e)

    # 3 — Re-import policies
    stats_pol: dict = {}
    try:
        pol_importer = PolicyImporter(
            db,
            settings.framework_path,
            settings.operational_path,
            extra_paths=settings.extra_paths,
        )
        stats_pol = pol_importer.import_all()
        db.commit()
    except Exception as e:
        logger.error("reset-content: policy import failed: %s", e)
        stats_pol = {"error": str(e)}

    # 4 — Re-import implementations
    stats_imp: dict = {}
    try:
        imp_importer = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
        stats_imp = imp_importer.import_all()
        db.commit()
    except Exception as e:
        logger.error("reset-content: IMP import failed: %s", e)
        stats_imp = {"error": str(e)}

    # 5 — Re-import framework workbooks (assessment structures)
    stats_wkbk: dict = {}
    try:
        wkbk_importer = FrameworkWorkbookImporter(db, settings.framework_path)
        stats_wkbk = wkbk_importer.import_all()
        db.commit()
    except Exception as e:
        logger.error("reset-content: workbook import failed: %s", e)
        stats_wkbk = {"error": str(e)}

    # 5b — Re-import operational checklists
    stats_op: dict = {}
    try:
        op_importer = OperationalChecklistImporter(db, settings.operational_path)
        stats_op = op_importer.import_all()
        db.commit()
    except Exception as e:
        logger.error("reset-content: operational import failed: %s", e)
        stats_op = {"error": str(e)}

    # 5c — Re-import privacy + cloud checklists
    stats_priv: dict = {}
    try:
        extra = [p for p in settings.extra_paths.split(",") if p.strip()]
        priv_importer = PrivacyChecklistImporter(db, extra)
        stats_priv = priv_importer.import_all()
        db.commit()
    except Exception as e:
        logger.error("reset-content: privacy/cloud import failed: %s", e)
        stats_priv = {"error": str(e)}

    # 6 — Re-run existence check
    try:
        qa_service.run_existence_check(db)
    except Exception as e:
        logger.warning("reset-content: existence check failed: %s", e)

    return {
        "status": "ok",
        "deleted": deleted,
        "reimport": {
            "policies": stats_pol,
            "implementations": stats_imp,
            "workbooks": stats_wkbk,
            "operational": stats_op,
            "privacy_cloud": stats_priv,
        },
    }


# ---------------------------------------------------------------------------
# External document import
# ---------------------------------------------------------------------------


@router.post(
    "/import-external",
    dependencies=[Depends(require_admin)],
)
async def import_external_doc(
    file: UploadFile = File(...),
    group_code: str = Form(...),
    source_label: str = Form(...),
    language: str = Form("en"),
    db: DBSession = Depends(get_db),
):
    """Upload a third-party document (MD/PDF/DOCX) and import it as ProductType.EXTERNAL.

    - file: the document to import
    - group_code: the ISO 27001 control group it covers (e.g. "a.5.1")
    - source_label: free-text origin (e.g. "Acme Corp", "Previous consultant")
    - language: ISO 639-1 code — en, de, fr, it (default: en)
    """
    ext = "." + (file.filename or "").rsplit(".", 1)[-1].lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported file type '{ext}'. Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}",
        )

    if language not in ("en", "de", "fr", "it"):
        raise HTTPException(status_code=422, detail=f"Unsupported language '{language}'. Use: en, de, fr, it")

    # Write upload to a temp file (UploadFile is a stream)
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path_str = tmp.name

    from pathlib import Path
    try:
        importer = ExternalDocImporter(db)
        result = importer.import_file(
            file_path=Path(tmp_path_str),
            group_code=group_code.lower().strip(),
            source_label=source_label.strip(),
            language=language,
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        logger.error("import-external failed: %s", e)
        raise HTTPException(status_code=500, detail=f"Import failed: {e}")
    finally:
        Path(tmp_path_str).unlink(missing_ok=True)

    return {"status": "ok", **result}


# ---------------------------------------------------------------------------
# User management
# ---------------------------------------------------------------------------

@router.get("/users", response_model=list[UserRead])
def list_users(
    db: DBSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.SUPER_ADMIN)),
):
    """List users. super_admin sees all; admin sees only their org."""
    from src.schemas.users import UserRead as _UserRead
    q = select(User).order_by(User.created_at)
    if current_user.role != UserRole.SUPER_ADMIN:
        q = q.where(User.organisation_id == current_user.organisation_id)
    users = db.execute(q).scalars().all()
    return [_UserRead.from_orm_with_org(u) for u in users]


@router.post(
    "/users",
    response_model=UserRead,
    status_code=201,
    dependencies=[Depends(require_admin)],
)
def create_user(
    body: UserCreate,
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
):
    """Create a new user."""
    from sqlalchemy.exc import IntegrityError

    if db.execute(select(User).where(User.email == body.email)).scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Email already registered")
    if db.execute(select(User).where(User.username == body.username)).scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Username already taken")

    try:
        role = UserRole(body.role)
    except ValueError:
        raise HTTPException(status_code=422, detail=f"Invalid role: {body.role}")

    user = User(
        email=body.email,
        username=body.username,
        full_name=body.full_name,
        hashed_password=hash_password(body.password),
        role=role,
        is_active=True,
        organisation_id=org_id,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="User already exists")
    db.refresh(user)
    log_event(db, event_type="user.created", category=CAT_SECURITY, severity=SEV_INFO,
              target_type="user", target_id=str(user.id),
              description=f"User {user.email} created with role {user.role.value}")
    db.commit()
    from src.schemas.users import UserRead as _UserRead
    return _UserRead.from_orm_with_org(user)


@router.patch(
    "/users/{user_id}",
    response_model=UserRead,
)
def update_user(
    user_id: str,
    body: UserPatch,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.SUPER_ADMIN)),
):
    """Update user role, active status, full_name, or password."""
    import uuid as _uuid
    from src.schemas.users import UserRead as _UserRead

    try:
        uid = _uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid user ID")

    user = db.get(User, uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.role != UserRole.SUPER_ADMIN and user.organisation_id != current_user.organisation_id:
        raise HTTPException(status_code=404, detail="User not found")

    if body.full_name is not None:
        user.full_name = body.full_name or None
    if body.role is not None:
        try:
            user.role = UserRole(body.role)
        except ValueError:
            raise HTTPException(status_code=422, detail=f"Invalid role: {body.role}")
    if body.is_active is not None:
        user.is_active = body.is_active
    if body.password is not None:
        user.hashed_password = hash_password(body.password)
    if body.notification_prefs is not None:
        from src.schemas.users import NOTIFICATION_EVENTS
        valid_types = {ev["event_type"] for ev in NOTIFICATION_EVENTS}
        unknown = set(body.notification_prefs) - valid_types
        if unknown:
            raise HTTPException(status_code=422, detail=f"Unknown notification event type(s): {', '.join(sorted(unknown))}")
        stored = dict(user.notification_prefs or {})
        stored.update(body.notification_prefs)
        user.notification_prefs = stored
    if body.organisation_id is not None:
        if current_user.role != UserRole.SUPER_ADMIN:
            raise HTTPException(status_code=403, detail="Only super_admin can reassign users to a different organisation.")
        org = db.get(Organisation, body.organisation_id)
        if not org:
            raise HTTPException(status_code=404, detail="Target organisation not found.")
        user.organisation_id = body.organisation_id

    log_event(db, event_type="user.updated", category=CAT_SECURITY, severity=SEV_INFO,
              user_id=current_user.id, actor_email=current_user.email,
              target_type="user", target_id=user_id,
              description=f"User {user.email} updated by {current_user.email}")
    db.commit()
    db.refresh(user)
    return _UserRead.from_orm_with_org(user)


@router.delete(
    "/users/{user_id}",
    status_code=204,
)
def delete_user(
    user_id: str,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.SUPER_ADMIN)),
):
    """Delete a user account."""
    import uuid as _uuid

    try:
        uid = _uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid user ID")

    user = db.get(User, uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.role != UserRole.SUPER_ADMIN and user.organisation_id != current_user.organisation_id:
        raise HTTPException(status_code=404, detail="User not found")

    email = user.email
    db.delete(user)
    log_event(db, event_type="user.deleted", category=CAT_SECURITY, severity=SEV_WARNING,
              user_id=current_user.id, actor_email=current_user.email,
              target_type="user", target_id=user_id,
              description=f"User {email} deleted by {current_user.email}")
    db.commit()


@router.delete(
    "/users/{user_id}/mfa",
    status_code=204,
)
def reset_user_mfa(
    user_id: str,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(require_role(UserRole.ADMIN, UserRole.SUPER_ADMIN)),
):
    """Reset (disable) MFA for a user. Admin can only affect their own org."""
    import uuid as _uuid

    try:
        uid = _uuid.UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=422, detail="Invalid user ID")

    user = db.get(User, uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.role != UserRole.SUPER_ADMIN and user.organisation_id != current_user.organisation_id:
        raise HTTPException(status_code=403, detail="Cannot reset MFA for users in a different organisation")

    user.mfa_enabled = False
    user.mfa_secret = None
    user.mfa_backup_codes = []
    log_event(db, event_type="user.mfa_reset", category=CAT_SECURITY, severity=SEV_WARNING,
              user_id=current_user.id, actor_email=current_user.email,
              target_type="user", target_id=user_id,
              description=f"MFA reset for {user.email} by admin {current_user.email}")
    db.commit()


# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------

@router.get(
    "/audit-log",
    response_model=AuditLogPage,
    dependencies=[Depends(require_admin)],
)
def get_audit_log(
    db: DBSession = Depends(get_db),
    page: int = 1,
    page_size: int = 50,
    category: str | None = None,
    severity: str | None = None,
    event_type: str | None = None,
    actor_email: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
):
    """Return paginated audit log entries, newest first.

    Filters (all optional, combinable):
      category     — 'security' | 'workflow' | 'system'
      severity     — 'info' | 'warning' | 'error' | 'critical'
      event_type   — exact match or prefix, e.g. 'login' matches 'login.success'
      actor_email  — substring match
      date_from    — ISO 8601 date string, e.g. '2026-01-01'
      date_to      — ISO 8601 date string, e.g. '2026-12-31'
    """
    from datetime import datetime, timezone
    from sqlalchemy import and_, desc

    q = select(AuditLog)
    conditions = []

    if category:
        conditions.append(AuditLog.category == category)
    if severity:
        conditions.append(AuditLog.severity == severity)
    if event_type:
        conditions.append(AuditLog.event_type.ilike(f"{event_type}%"))
    if actor_email:
        conditions.append(AuditLog.actor_email.ilike(f"%{actor_email}%"))
    if date_from:
        try:
            dt = datetime.fromisoformat(date_from).replace(tzinfo=timezone.utc)
            conditions.append(AuditLog.created_at >= dt)
        except ValueError:
            pass
    if date_to:
        try:
            dt = datetime.fromisoformat(date_to).replace(tzinfo=timezone.utc)
            conditions.append(AuditLog.created_at <= dt)
        except ValueError:
            pass

    if conditions:
        q = q.where(and_(*conditions))

    total = db.execute(select(func.count()).select_from(q.subquery())).scalar_one()

    page = max(1, page)
    page_size = min(max(1, page_size), 200)
    offset = (page - 1) * page_size

    items = db.execute(
        q.order_by(desc(AuditLog.created_at)).offset(offset).limit(page_size)
    ).scalars().all()

    import math
    return AuditLogPage(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
        pages=math.ceil(total / page_size) if total else 1,
    )


# ── OpenSearch operational detail (Phase 7) ───────────────────────────────────

@router.get("/opensearch", tags=["admin"])
def get_opensearch_detail(
    _user=Depends(require_admin),
):
    """
    Return OpenSearch operational status: cluster health, ISM policies,
    ISM managed index states, SM snapshot policies, snapshot repos,
    and per-org evidence index sizes.
    """
    from src.services import opensearch_service

    return {
        "ism_policies":      opensearch_service.get_ism_policies(),
        "ism_managed":       opensearch_service.get_ism_managed_indices(),
        "sm_policies":       opensearch_service.get_sm_policies(),
        "snapshot_repos":    opensearch_service.get_snapshot_repos(),
        "evidence_indices":  opensearch_service.get_evidence_indices(),
    }


# ---------------------------------------------------------------------------
# Logs — Feed Runs (Phase 39)
# ---------------------------------------------------------------------------

@router.get("/logs/feed-runs", tags=["admin"])
def get_feed_runs(
    feed_name: str | None = None,
    status: str | None = None,
    limit: int = 200,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    """Return recent feed run history, newest first.

    Filters (all optional):
      feed_name — exact match, e.g. 'nist_cve' | 'cisa_kev' | 'euvd'
      status    — 'success' | 'error' | 'running'
      limit     — max rows to return (default 200, max 1000)
    """
    from datetime import timezone
    from sqlalchemy import and_, desc
    from src.domain.feeds import FeedRun

    limit = min(max(1, limit), 1000)

    q = select(FeedRun)
    conditions = []
    if feed_name:
        conditions.append(FeedRun.feed_name == feed_name)
    if status:
        conditions.append(FeedRun.status == status)
    if conditions:
        q = q.where(and_(*conditions))

    rows = db.execute(q.order_by(desc(FeedRun.started_at)).limit(limit)).scalars().all()

    items = []
    for r in rows:
        duration = None
        if r.finished_at and r.started_at:
            duration = round((r.finished_at - r.started_at).total_seconds(), 1)
        items.append({
            "id":               str(r.id),
            "feed_name":        r.feed_name,
            "status":           r.status,
            "started_at":       r.started_at.isoformat() if r.started_at else None,
            "finished_at":      r.finished_at.isoformat() if r.finished_at else None,
            "duration_seconds": duration,
            "item_count":       r.item_count,
            "error_message":    r.error_message,
        })
    return items


# ---------------------------------------------------------------------------
# Logs — Connector Runs (Phase 39)
# ---------------------------------------------------------------------------

@router.get("/logs/connector-runs", tags=["admin"])
def get_connector_runs(
    connector_id: uuid.UUID | None = None,
    status: str | None = None,
    limit: int = 200,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    """Return recent connector run history, newest first.

    Tries OpenSearch connector-runs index first; falls back to last-run
    snapshot from the connectors table when OpenSearch is unavailable.

    Filters (all optional):
      connector_id — UUID of the connector
      status       — 'success' | 'error'
      limit        — max rows to return (default 200, max 1000)
    """
    from src.domain.connectors import Connector

    limit = min(max(1, limit), 1000)

    # ── OpenSearch path ───────────────────────────────────────────────────────
    try:
        from opensearchpy import OpenSearch
        s = get_settings()
        client = OpenSearch(hosts=[s.opensearch_url], use_ssl=False, verify_certs=False, timeout=5)
        if client.ping():
            body: dict = {
                "sort": [{"started_at": {"order": "desc"}}],
                "size": limit,
            }
            must = []
            if connector_id:
                must.append({"term": {"connector_id": str(connector_id)}})
            if status:
                must.append({"term": {"status": status}})
            if must:
                body["query"] = {"bool": {"must": must}}
            res = client.search(index="connector-runs", body=body)
            items = [hit["_source"] for hit in res["hits"]["hits"]]
            # strip any sensitive fields that may have been indexed
            for item in items:
                item.pop("api_token_hash", None)
                item.pop("config_encrypted", None)
            return items
    except Exception as exc:
        logger.debug("OpenSearch connector-runs query failed, using postgres fallback: %s", exc)

    # ── Postgres fallback — last-run snapshot per connector ───────────────────
    from sqlalchemy import desc as _desc

    q = select(Connector)
    conditions = []
    if connector_id:
        conditions.append(Connector.id == connector_id)
    if status:
        # map requested status to postgres last_error presence
        if status == "error":
            conditions.append(Connector.last_error.isnot(None))
        elif status == "success":
            conditions.append(Connector.last_error.is_(None))
    if conditions:
        from sqlalchemy import and_
        q = q.where(and_(*conditions))

    rows = db.execute(q.order_by(_desc(Connector.last_run)).limit(limit)).scalars().all()

    return [
        {
            "connector_name":  c.name,
            "connector_id":    str(c.id),
            "started_at":      c.last_run.isoformat() if c.last_run else None,
            "finished_at":     None,
            "evidence_count":  c.last_item_count,
            "status":          "error" if c.last_error else "success",
            "error_message":   c.last_error,
            "history_limited": True,
        }
        for c in rows
    ]


# ---------------------------------------------------------------------------
# Sessions (Phase 39 — B.5)
# ---------------------------------------------------------------------------

@router.get("/sessions", tags=["admin"])
def list_sessions(
    user_id: uuid.UUID | None = None,
    include_expired: bool = False,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    """Return active sessions for the organisation. Excludes expired by default."""
    from datetime import timezone, datetime as _dt
    from src.domain.users import Session

    stmt = (
        select(Session)
        .join(User, Session.user_id == User.id)
        .where(User.organisation_id == _user.organisation_id)
    )
    if user_id:
        stmt = stmt.where(Session.user_id == user_id)
    if not include_expired:
        stmt = stmt.where(Session.expires_at > _dt.now(timezone.utc))
    stmt = stmt.order_by(Session.created_at.desc()).limit(500)

    rows = db.execute(stmt).scalars().all()

    user_ids = list({r.user_id for r in rows})
    user_map: dict[uuid.UUID, User] = {}
    if user_ids:
        users = db.execute(select(User).where(User.id.in_(user_ids))).scalars().all()
        user_map = {u.id: u for u in users}

    now = _dt.now(timezone.utc)
    return [
        {
            "id":            str(r.id),
            "user_id":       str(r.user_id),
            "user_email":    user_map[r.user_id].email    if r.user_id in user_map else None,
            "user_username": user_map[r.user_id].username if r.user_id in user_map else None,
            "expires_at":    r.expires_at.isoformat(),
            "ip_address":    r.ip_address,
            "user_agent":    r.user_agent,
            "created_at":    r.created_at.isoformat(),
            "is_expired":    r.expires_at <= now,
        }
        for r in rows
    ]


@router.delete("/sessions/user/{target_user_id}", tags=["admin"])
def revoke_user_sessions(
    target_user_id: uuid.UUID,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    """Revoke all sessions for a given user (same organisation only)."""
    from src.domain.users import Session

    target = db.get(User, target_user_id)
    if not target or target.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=404, detail="User not found")
    result = db.execute(sql_delete(Session).where(Session.user_id == target_user_id))
    db.commit()
    return {"ok": True, "deleted": result.rowcount}


@router.delete("/sessions/{session_id}", tags=["admin"])
def revoke_session(
    session_id: uuid.UUID,
    _user=Depends(require_admin),
    db: DBSession = Depends(get_db),
):
    """Revoke a single session."""
    from src.domain.users import Session

    s = db.get(Session, session_id)
    if not s:
        raise HTTPException(status_code=404, detail="Session not found")
    owner = db.get(User, s.user_id)
    if not owner or owner.organisation_id != _user.organisation_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(s)
    db.commit()
    return {"ok": True}


# ---------------------------------------------------------------------------
# Evidence Indices diagnostic (Phase 39a)
# ---------------------------------------------------------------------------

_EVIDENCE_INDICES = [
    "evidence-entra-id",
    "evidence-o365",
    "evidence-defender",
    "evidence-sentinel",
    "evidence-intune",
    "evidence-crowdstrike",
    "evidence-sentinelone",
    "evidence-tenable",
    "evidence-qualys",
]


@router.get("/evidence-indices", tags=["admin"])
def evidence_indices(_user=Depends(require_admin)):
    """Return doc counts for each per-source evidence index in OpenSearch."""
    try:
        from opensearchpy import OpenSearch
        from src.core.config import get_settings
        client = OpenSearch(
            hosts=[get_settings().opensearch_url],
            use_ssl=False, verify_certs=False, timeout=10,
        )
        if not client.ping():
            return {"available": False, "indices": []}
    except Exception as exc:
        return {"available": False, "error": str(exc), "indices": []}

    result = []
    for idx in _EVIDENCE_INDICES:
        try:
            exists = client.indices.exists(index=idx)
            if exists:
                stats = client.count(index=idx)
                count = stats.get("count", 0)
            else:
                count = None
            result.append({"index": idx, "exists": exists, "doc_count": count})
        except Exception as exc:
            result.append({"index": idx, "exists": False, "doc_count": None, "error": str(exc)})

    return {"available": True, "indices": result}
