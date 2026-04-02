"""Celery tasks for KPI metric computation."""

import logging

from src.worker import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(name="compute_daily_metrics")
def compute_daily_metrics():
    """Daily beat task: compute and store all metrics for all active orgs + projects."""
    from sqlalchemy import select

    from src.database.session import SessionLocal
    from src.domain.organisations import Organisation
    from src.domain.projects import Project
    from src.services.metrics_service import compute_all_metrics

    db = SessionLocal()
    try:
        orgs = db.execute(
            select(Organisation).where(Organisation.is_active.is_(True))
        ).scalars().all()

        for org in orgs:
            # Org-wide (no project scope)
            try:
                compute_all_metrics(db, org.id, project_id=None, store_snapshot=True)
            except Exception:
                logger.exception("Failed org-wide metrics for org %s", org.id)

            # Per-project
            projects = db.execute(
                select(Project).where(
                    Project.organisation_id == org.id,
                    Project.status == 'active',
                )
            ).scalars().all()

            for project in projects:
                try:
                    compute_all_metrics(db, org.id, project_id=project.id, store_snapshot=True)
                except Exception:
                    logger.exception("Failed metrics for project %s", project.id)

        logger.info("Daily metrics computed for %d orgs", len(orgs))
    finally:
        db.close()
