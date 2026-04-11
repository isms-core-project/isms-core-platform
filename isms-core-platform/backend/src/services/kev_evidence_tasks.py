"""Phase 26 Track B — Daily KEV evidence sync Celery task.

Checks for CISA KEV entries added in the last 90 days that do not yet have
a corresponding threat_intel evidence record for control A.8.8.
Creates pending_review evidence items so control owners can attach remediation proof.

This gives auditors a complete A.8.8 (Management of Technical Vulnerabilities)
audit trail: CVE disclosed → platform notified → evidence task created → remediated.
"""

import logging
import uuid
from datetime import date, datetime, timedelta, timezone

from celery import shared_task
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import EvidenceStatus, EvidenceType
from src.database.session import SessionLocal
from src.domain.compliance import Evidence
from src.domain.control_groups import ControlGroup
from src.domain.feeds import CisaKevEntry

logger = logging.getLogger(__name__)

# Only auto-create evidence for KEV entries added within this window
KEV_LOOKBACK_DAYS = 90
# The control this evidence is linked to
TARGET_CONTROL_CODE = "a.8.8"


def _get_a88_control_group(db: DBSession) -> ControlGroup | None:
    """Look up the A.8.8 control group."""
    return db.scalars(
        select(ControlGroup).where(
            ControlGroup.group_code == TARGET_CONTROL_CODE
        ).limit(1)
    ).first()


@shared_task(name="kev_evidence_sync")
def kev_evidence_sync() -> dict:
    """Create pending evidence items for recent CISA KEV entries.

    Runs daily at 04:30 UTC (30 minutes after KEV feed pull at 04:00).
    Only processes entries added in the last 90 days.
    Skips entries that already have a kev_cve_id evidence record.
    """
    db = SessionLocal()
    created = 0
    skipped = 0

    try:
        control_group = _get_a88_control_group(db)
        if not control_group:
            logger.warning("A.8.8 control group not found — skipping KEV evidence sync")
            return {"created": 0, "skipped": 0, "error": "A.8.8 control group not found"}

        cutoff = date.today() - timedelta(days=KEV_LOOKBACK_DAYS)
        now = datetime.now(timezone.utc)

        # Get recent KEV entries
        recent_entries = db.scalars(
            select(CisaKevEntry).where(
                CisaKevEntry.date_added >= cutoff
            )
        ).all()

        # Get existing kev_cve_ids already in evidence table (avoid duplicates)
        existing_kev_ids: set[str] = set(
            db.scalars(
                select(Evidence.kev_cve_id).where(Evidence.kev_cve_id.isnot(None))
            ).all()
        )

        for entry in recent_entries:
            if entry.cve_id in existing_kev_ids:
                skipped += 1
                continue

            ransomware_note = " ⚠ Known ransomware campaign." if entry.known_ransomware else ""
            due_note = f" Due: {entry.due_date.isoformat()}." if entry.due_date else ""

            title = f"[KEV] {entry.cve_id}"
            if entry.vulnerability_name:
                title += f" — {entry.vulnerability_name[:180]}"

            evidence = Evidence(
                id=uuid.uuid4(),
                control_group_id=control_group.id,
                evidence_type=EvidenceType.THREAT_INTEL,
                evidence_status=EvidenceStatus.PENDING_REVIEW,
                title=title,
                file_path="",
                collected_date=entry.date_added,
                kev_cve_id=entry.cve_id,
                metadata_={
                    "source": "cisa_kev",
                    "cve_id": entry.cve_id,
                    "vendor_project": entry.vendor_project or "",
                    "product": entry.product or "",
                    "date_added": entry.date_added.isoformat() if entry.date_added else None,
                    "due_date": entry.due_date.isoformat() if entry.due_date else None,
                    "required_action": entry.required_action or "",
                    "known_ransomware": entry.known_ransomware,
                    "notes": (
                        f"Auto-created from CISA KEV.{ransomware_note}{due_note} "
                        f"Attach remediation proof (patch ticket, scan result) and approve."
                    ),
                    "original_filename": "",
                    "file_size": 0,
                    "file_ext": "",
                    "content_hash": "",
                    "word_count": 0,
                    "text_preview": entry.short_description or "",
                },
            )
            db.add(evidence)
            created += 1

        db.commit()
        logger.info("KEV evidence sync: %d created, %d skipped", created, skipped)
        return {"created": created, "skipped": skipped}

    except Exception as exc:
        db.rollback()
        logger.error("KEV evidence sync failed: %s", exc, exc_info=True)
        return {"created": 0, "skipped": 0, "error": str(exc)}
    finally:
        db.close()
