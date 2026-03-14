"""Celery tasks for bundle loading and policy importing."""

import logging

from src.database.session import SessionLocal
from src.importers.bundle_loader import BundleLoader
from src.worker import celery_app
from src.core.config import get_settings

logger = logging.getLogger(__name__)


@celery_app.task(name="load_all_bundles", bind=True)
def load_all_bundles(self):
    """Load all dataset bundles into PostgreSQL."""
    settings = get_settings()
    db = SessionLocal()
    try:
        loader = BundleLoader(db, settings.datasets_path)
        stats = loader.load_all()
        logger.info("Bundle load complete: %s", stats)
        return stats
    except Exception as e:
        logger.error("Bundle load failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="import_policies", bind=True)
def import_policies_task(self):
    """Parse POL and OP-POL files into policies + requirements."""
    from src.importers.policy_importer import PolicyImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        importer = PolicyImporter(
            db,
            settings.framework_path,
            settings.operational_path,
            extra_paths=settings.extra_paths,
        )
        stats = importer.import_all()
        db.commit()
        logger.info("Policy import complete: %s", stats)
        return stats
    except Exception as e:
        db.rollback()
        logger.error("Policy import failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="full_sync", bind=True)
def full_sync_task(self):
    """Run all importers in sequence: policies → implementations → operational → privacy/cloud → framework."""
    from src.importers.framework_importer import FrameworkWorkbookImporter
    from src.importers.imp_importer import ImpImporter
    from src.importers.operational_importer import OperationalChecklistImporter
    from src.importers.privacy_checklist_importer import PrivacyChecklistImporter
    from src.importers.policy_importer import PolicyImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        results = {}

        pol = PolicyImporter(
            db,
            settings.framework_path,
            settings.operational_path,
            extra_paths=settings.extra_paths,
        )
        results["policies"] = pol.import_all()
        db.flush()

        imp = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
        results["implementations"] = imp.import_all()
        db.flush()

        op = OperationalChecklistImporter(db, settings.operational_path)
        results["operational"] = op.import_all()
        db.flush()

        extra = [p for p in settings.extra_paths.split(",") if p.strip()]
        priv = PrivacyChecklistImporter(db, extra)
        results["privacy_cloud"] = priv.import_all()
        db.flush()

        fw = FrameworkWorkbookImporter(db, settings.framework_path)
        results["framework_workbooks"] = fw.import_all()

        db.commit()
        logger.info("Full sync complete: %s", results)
        return results
    except Exception as e:
        db.rollback()
        logger.error("Full sync failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="import_framework_workbooks", bind=True)
def import_framework_workbooks_task(self):
    """Parse framework SCR generators into assessments table."""
    from src.importers.framework_importer import FrameworkWorkbookImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        importer = FrameworkWorkbookImporter(db, settings.framework_path)
        stats = importer.import_all()
        db.commit()
        logger.info("Framework workbook import complete: %s", stats)
        return stats
    except Exception as e:
        db.rollback()
        logger.error("Framework workbook import failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="import_operational", bind=True)
def import_operational_task(self):
    """Parse operational checklist scripts into assessments table."""
    from src.importers.operational_importer import OperationalChecklistImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        importer = OperationalChecklistImporter(db, settings.operational_path)
        stats = importer.import_all()
        db.commit()
        logger.info("Operational import complete: %s", stats)
        return stats
    except Exception as e:
        db.rollback()
        logger.error("Operational import failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="import_privacy", bind=True)
def import_privacy_task(self):
    """Parse PRIV + CLD checklist scripts into assessments table."""
    from src.importers.privacy_checklist_importer import PrivacyChecklistImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        extra = [p for p in settings.extra_paths.split(",") if p.strip()]
        importer = PrivacyChecklistImporter(db, extra)
        stats = importer.import_all()
        db.commit()
        logger.info("Privacy/Cloud checklist import complete: %s", stats)
        return stats
    except Exception as e:
        db.rollback()
        logger.error("Privacy/Cloud checklist import failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="archive_evidence_beat", bind=True)
def archive_evidence_beat(self):
    """Nightly sweep: archive connector evidence older than each connector's retention window."""
    from src.services.connector_service import archive_old_evidence
    from src.services.audit_service import log_event, CAT_SYSTEM, SEV_INFO, SEV_WARNING

    db = SessionLocal()
    try:
        archived = archive_old_evidence(db)
        severity = SEV_WARNING if archived > 0 else SEV_INFO
        log_event(
            db,
            event_type="connector.evidence.archived",
            category=CAT_SYSTEM,
            severity=severity,
            description=f"Nightly evidence archive sweep completed: {archived} record(s) archived",
            metadata={"archived_count": archived},
        )
        db.commit()
        logger.info("Nightly archive sweep: %d records archived", archived)
        return {"archived": archived}
    except Exception as e:
        db.rollback()
        logger.error("Nightly archive sweep failed: %s", e)
        raise
    finally:
        db.close()


@celery_app.task(name="import_implementations", bind=True)
def import_implementations_task(self):
    """Parse IMP-UG/TG files into implementations table."""
    from src.importers.imp_importer import ImpImporter

    settings = get_settings()
    db = SessionLocal()
    try:
        importer = ImpImporter(db, settings.framework_path, extra_paths=settings.extra_paths)
        stats = importer.import_all()
        db.commit()
        logger.info("IMP import complete: %s", stats)
        return stats
    except Exception as e:
        db.rollback()
        logger.error("IMP import failed: %s", e)
        raise
    finally:
        db.close()
