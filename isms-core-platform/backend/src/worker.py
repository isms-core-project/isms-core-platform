"""Celery worker application."""

from celery import Celery
from celery.schedules import crontab

from src.core.config import get_settings

settings = get_settings()

celery_app = Celery(
    "isms_core",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_default_queue="isms",
    beat_schedule={
        # Evidence expiry scanner — runs daily at 08:00 UTC
        "evidence-expiry-scan-daily": {
            "task": "scan_evidence_expiry",
            "schedule": crontab(hour=8, minute=0),
        },
        # Connector evidence archive sweep — runs nightly at 02:00 UTC
        "evidence-archive-nightly": {
            "task": "archive_evidence_beat",
            "schedule": crontab(hour=2, minute=0),
        },
    },
)

# Discover tasks: importers via autodiscover (has tasks.py), notification service explicitly
celery_app.autodiscover_tasks(["src.importers"])
celery_app.conf.include = ["src.services.notification_service"]
