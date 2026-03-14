"""Sync endpoints — orchestrate all importers in sequence.

POST /api/v1/sync/full       — run all 4 importers synchronously
POST /api/v1/sync/full/async — queue full sync via Celery worker

Import order:
  1. Policies        (POL, OP-POL, REF, CTX, FORM → policies + requirements)
  2. Implementations (IMP-UG/TG → implementations + OpenSearch)
  3. Operational     (53 checklist scripts → assessments + items)
  4. Framework       (188 generator scripts → assessments + sheets)
"""

import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.core.dependencies import require_role
from src.database.enums import UserRole
from src.database.session import get_db
from src.importers.framework_importer import FrameworkWorkbookImporter
from src.importers.imp_importer import ImpImporter
from src.importers.operational_importer import OperationalChecklistImporter
from src.importers.policy_importer import PolicyImporter
from src.importers.tasks import full_sync_task

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/sync", tags=["sync"])


@router.post(
    "/full",
    dependencies=[Depends(require_role(UserRole.ADMIN))],
)
def trigger_full_sync(db: DBSession = Depends(get_db)):
    """Run all importers in sequence: policies → implementations → operational → framework."""
    settings = get_settings()
    results = {}

    # 1 — Policies
    policy_importer = PolicyImporter(
        db,
        settings.framework_path,
        settings.operational_path,
        extra_paths=settings.extra_paths,
    )
    results["policies"] = policy_importer.import_all()
    db.flush()

    # 2 — Implementations (IMP-UG/TG)
    imp_importer = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
    results["implementations"] = imp_importer.import_all()
    db.flush()

    # 3 — Operational checklists
    op_importer = OperationalChecklistImporter(db, settings.operational_path)
    results["operational"] = op_importer.import_all()
    db.flush()

    # 4 — Framework workbooks
    fw_importer = FrameworkWorkbookImporter(db, settings.framework_path)
    results["framework_workbooks"] = fw_importer.import_all()

    db.commit()

    total_errors = sum(
        r.get("errors", 0) for r in results.values()
    )

    logger.info("Full sync complete: errors=%d results=%s", total_errors, results)
    return {
        "status": "ok" if total_errors == 0 else "completed_with_errors",
        "results": results,
    }


@router.post(
    "/full/async",
    dependencies=[Depends(require_role(UserRole.ADMIN))],
)
def trigger_full_sync_async():
    """Queue full sync via Celery worker. Returns task_id for polling."""
    task = full_sync_task.delay()
    return {"status": "queued", "task_id": task.id}
