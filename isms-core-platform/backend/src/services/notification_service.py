"""Notification service — Phase 9.7/9.8.

Celery tasks that render email templates and deliver them via email_service.
Each task is fire-and-forget — failures are logged but never bubble up to the
caller (the business operation must not fail because email is down).

All tasks also write an audit log entry (category=workflow, event_type=email.*).

scan_evidence_expiry is a scheduled beat task (daily 08:00 UTC) that finds
evidence items approaching or past expiry and enqueues notify_evidence_expiry
for each active admin / ISMS manager.

Autodiscovered by Celery via worker.py:
    celery_app.autodiscover_tasks(["src.importers", "src.services"])

Calling convention (from routers / other services):
    from src.services.notification_service import notify_welcome
    notify_welcome.delay(user_id=str(user.id), created_by_email="admin@example.com")
"""

import logging
import uuid
from datetime import date, datetime, timezone

from src.database.session import SessionLocal
from src.services.audit_service import CAT_WORKFLOW, SEV_INFO, log_event
from src.services.email_service import is_enabled, render_template, send_email
from src.worker import celery_app

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _platform_url() -> str:
    from src.core.config import get_settings
    return get_settings().platform_url.rstrip("/")


def _log_email_sent(db, event_type: str, target_id: str | None, description: str) -> None:
    """Write a workflow audit entry for an email notification sent."""
    log_event(
        db,
        event_type=event_type,
        category=CAT_WORKFLOW,
        severity=SEV_INFO,
        target_type="email",
        target_id=target_id,
        description=description,
    )


def _prefs_allow(user, event_type: str) -> bool:
    """Return True if the user has not opted out of this notification type."""
    prefs = user.notification_prefs if user.notification_prefs else {}
    return prefs.get(event_type, True)


# ---------------------------------------------------------------------------
# Task: welcome email
# ---------------------------------------------------------------------------

@celery_app.task(name="notify_welcome", bind=True, max_retries=2)
def notify_welcome(self, user_id: str, created_by_email: str = "system") -> bool:
    """Send a welcome email to a newly created user.

    Args:
        user_id:          UUID string of the new user.
        created_by_email: Email of the admin who created the account.
    """
    if not is_enabled():
        return False

    db = SessionLocal()
    try:
        from src.domain.users import User
        user = db.get(User, uuid.UUID(user_id))
        if not user:
            logger.warning("notify_welcome: user %s not found", user_id)
            return False

        html = render_template("welcome.html", {
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role,
            "platform_url": _platform_url(),
            "created_by": created_by_email,
        })

        ok = send_email(
            to=[user.email],
            subject="Welcome to ISMS CORE",
            html_body=html,
        )

        if ok:
            _log_email_sent(db, "email.welcome", user_id, f"Welcome email sent to {user.email}")
            db.commit()

        return ok

    except Exception as e:
        db.rollback()
        logger.error("notify_welcome failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Task: gap assigned
# ---------------------------------------------------------------------------

@celery_app.task(name="notify_gap_assigned", bind=True, max_retries=2)
def notify_gap_assigned(self, gap_id: str, assignee_user_id: str) -> bool:
    """Send a notification when a gap is assigned to a user.

    Args:
        gap_id:            UUID string of the gap.
        assignee_user_id:  UUID string of the user assigned to the gap.
    """
    if not is_enabled():
        return False

    db = SessionLocal()
    try:
        from src.domain.compliance import Gap
        from src.domain.control_groups import ControlGroup
        from src.domain.users import User

        gap = db.get(Gap, uuid.UUID(gap_id))
        assignee = db.get(User, uuid.UUID(assignee_user_id))
        if not gap or not assignee:
            logger.warning("notify_gap_assigned: gap or user not found")
            return False

        if not _prefs_allow(assignee, "email.gap_assigned"):
            logger.debug("notify_gap_assigned: user %s has opted out", assignee.email)
            return False

        cg = db.get(ControlGroup, gap.control_group_id) if gap.control_group_id else None
        base = _platform_url()

        html = render_template("gap_assigned.html", {
            "full_name": assignee.full_name,
            "email": assignee.email,
            "gap_title": gap.title,
            "control_ref": cg.group_code if cg else "—",
            "control_name": cg.name if cg else "—",
            "severity": gap.severity or "low",
            "due_date": gap.due_date.strftime("%d %b %Y") if gap.due_date else None,
            "description": gap.description,
            "assigned_by": None,
            "gap_url": f"{base}/gaps",
        })

        ok = send_email(
            to=[assignee.email],
            subject=f"Gap Assigned: {gap.title}",
            html_body=html,
        )

        if ok:
            _log_email_sent(db, "email.gap_assigned", gap_id, f"Gap assignment email sent to {assignee.email}")
            db.commit()

        return ok

    except Exception as e:
        db.rollback()
        logger.error("notify_gap_assigned failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Task: evidence expiry
# ---------------------------------------------------------------------------

@celery_app.task(name="notify_evidence_expiry", bind=True, max_retries=2)
def notify_evidence_expiry(self, evidence_id: str, recipient_email: str, days_remaining: int) -> bool:
    """Send an evidence expiry warning/alert to a recipient.

    Args:
        evidence_id:       UUID string of the evidence item.
        recipient_email:   Email address to notify (owner or ISMS manager).
        days_remaining:    Days until expiry; 0 or negative = already expired.
    """
    if not is_enabled():
        return False

    db = SessionLocal()
    try:
        from src.domain.compliance import Evidence
        from src.domain.control_groups import ControlGroup

        evidence = db.get(Evidence, uuid.UUID(evidence_id))
        if not evidence:
            logger.warning("notify_evidence_expiry: evidence %s not found", evidence_id)
            return False

        # Check recipient's notification prefs if they're a known user
        from src.domain.users import User as _User
        recipient_user = db.query(_User).filter(_User.email == recipient_email).first()
        if recipient_user and not _prefs_allow(recipient_user, "email.evidence_expiry"):
            logger.debug("notify_evidence_expiry: %s has opted out", recipient_email)
            return False

        expired = days_remaining <= 0
        cg = db.get(ControlGroup, evidence.control_group_id) if evidence.control_group_id else None
        base = _platform_url()

        html = render_template("evidence_expiry.html", {
            "full_name": None,
            "email": recipient_email,
            "evidence_title": evidence.title,
            "control_ref": cg.group_code if cg else "—",
            "control_name": cg.name if cg else "—",
            "expiry_date": evidence.expires_date.strftime("%d %b %Y") if evidence.expires_date else "—",
            "days_remaining": max(0, days_remaining),
            "expired": expired,
            "owner": evidence.verified_by,
            "evidence_url": f"{base}/evidence",
        })

        subject = (
            f"Evidence Expired: {evidence.title}"
            if expired
            else f"Evidence Expiring in {days_remaining} Day{'s' if days_remaining != 1 else ''}: {evidence.title}"
        )

        ok = send_email(to=[recipient_email], subject=subject, html_body=html)

        if ok:
            _log_email_sent(
                db, "email.evidence_expiry", evidence_id,
                f"Evidence expiry email sent to {recipient_email} — {days_remaining}d remaining",
            )
            db.commit()

        return ok

    except Exception as e:
        db.rollback()
        logger.error("notify_evidence_expiry failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Task: QA check failed
# ---------------------------------------------------------------------------

@celery_app.task(name="notify_qa_fail", bind=True, max_retries=2)
def notify_qa_fail(
    self,
    product: str,
    checked_at: str,
    pass_pct: int,
    fail_count: int,
    warning_count: int,
    failures: list,
    recipient_email: str,
) -> bool:
    """Send a QA failure summary to an admin/ISMS manager.

    Args:
        product:        'framework' or 'operational'.
        checked_at:     ISO datetime string of when the check ran.
        pass_pct:       Pass percentage (0-100).
        fail_count:     Number of FAIL results.
        warning_count:  Number of WARNING results.
        failures:       List of dicts: [{control_ref, status, missing[]}].
        recipient_email: Email to send to.
    """
    if not is_enabled():
        return False

    db = SessionLocal()
    try:
        from src.domain.users import User as _User
        recipient_user = db.query(_User).filter(_User.email == recipient_email).first()
        if recipient_user and not _prefs_allow(recipient_user, "email.qa_fail"):
            logger.debug("notify_qa_fail: %s has opted out", recipient_email)
            return False

        base = _platform_url()

        html = render_template("qa_fail.html", {
            "full_name": None,
            "email": recipient_email,
            "product": product.title(),
            "checked_at": checked_at,
            "pass_pct": pass_pct,
            "fail_count": fail_count,
            "warning_count": warning_count,
            "failures": failures,
            "qa_url": f"{base}/qa",
        })

        ok = send_email(
            to=[recipient_email],
            subject=f"QA Check — {fail_count} failure{'s' if fail_count != 1 else ''} ({product.title()})",
            html_body=html,
        )

        if ok:
            _log_email_sent(
                db, "email.qa_fail", None,
                f"QA fail email sent to {recipient_email} — {fail_count} failures in {product}",
            )
            db.commit()

        return ok

    except Exception as e:
        db.rollback()
        logger.error("notify_qa_fail failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Task: import completed
# ---------------------------------------------------------------------------

@celery_app.task(name="notify_import_completed", bind=True, max_retries=2)
def notify_import_completed(
    self,
    import_type: str,
    stats: dict,
    errors: list,
    recipient_email: str,
) -> bool:
    """Send an import completion summary to the triggering admin.

    Args:
        import_type:     Human-readable import name, e.g. 'Policy Import'.
        stats:           Dict of stat name → count from the importer.
        errors:          List of error strings (empty = clean run).
        recipient_email: Email to notify.
    """
    if not is_enabled():
        return False

    db = SessionLocal()
    try:
        from src.domain.users import User as _User
        recipient_user = db.query(_User).filter(_User.email == recipient_email).first()
        if recipient_user and not _prefs_allow(recipient_user, "email.import_completed"):
            logger.debug("notify_import_completed: %s has opted out", recipient_email)
            return False

        base = _platform_url()

        html = render_template("import_completed.html", {
            "full_name": None,
            "email": recipient_email,
            "import_type": import_type,
            "completed_at": datetime.now(timezone.utc).strftime("%d %b %Y %H:%M UTC"),
            "stats": stats,
            "errors": errors,
            "system_url": f"{base}/system",
        })

        status = "with errors" if errors else "successfully"
        ok = send_email(
            to=[recipient_email],
            subject=f"Import {status.title()}: {import_type}",
            html_body=html,
        )

        if ok:
            _log_email_sent(
                db, "email.import_completed", None,
                f"Import completed email sent to {recipient_email} — {import_type}",
            )
            db.commit()

        return ok

    except Exception as e:
        db.rollback()
        logger.error("notify_import_completed failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=60)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Scheduled task: evidence expiry scanner  (Celery beat — daily 08:00 UTC)
# ---------------------------------------------------------------------------

# Days-before-expiry at which we send a notification.
# We also notify for up to 7 days after expiry (to catch items that slipped through).
_NOTIFY_AT_DAYS = frozenset({30, 14, 7, 3, 1})
_NOTIFY_EXPIRED_WINDOW = 7  # days post-expiry


def _should_notify(days_remaining: int) -> bool:
    if days_remaining in _NOTIFY_AT_DAYS:
        return True
    if -_NOTIFY_EXPIRED_WINDOW <= days_remaining <= 0:
        return True
    return False


@celery_app.task(name="scan_evidence_expiry", bind=True, max_retries=1)
def scan_evidence_expiry(self) -> dict:
    """Daily scanner — finds evidence items approaching or past expiry and
    enqueues notify_evidence_expiry for each active admin / ISMS manager.

    Triggered by Celery beat at 08:00 UTC.  Safe to run manually at any time.

    Returns a summary dict: {scanned, notified, skipped}.
    """
    db = SessionLocal()
    try:
        from sqlalchemy import and_, not_
        from src.domain.compliance import Evidence
        from src.domain.users import User
        from src.database.enums import UserRole

        today = date.today()

        # All evidence with a non-null expires_date
        items = (
            db.query(Evidence)
            .filter(Evidence.expires_date.isnot(None))
            .all()
        )

        # Active admin / ISMS manager recipients
        recipients = (
            db.query(User.email)
            .filter(
                User.is_active.is_(True),
                User.role.in_([UserRole.ADMIN, UserRole.ISMS_MANAGER]),
            )
            .all()
        )
        recipient_emails = [r.email for r in recipients]

        if not recipient_emails:
            logger.info("scan_evidence_expiry: no admin/manager recipients — skipping")
            return {"scanned": len(items), "notified": 0, "skipped": len(items)}

        notified = 0
        skipped = 0

        for ev in items:
            days_remaining = (ev.expires_date - today).days
            if not _should_notify(days_remaining):
                skipped += 1
                continue

            for email in recipient_emails:
                notify_evidence_expiry.delay(
                    evidence_id=str(ev.id),
                    recipient_email=email,
                    days_remaining=days_remaining,
                )
                notified += 1

        summary = {"scanned": len(items), "notified": notified, "skipped": skipped}
        logger.info("scan_evidence_expiry: %s", summary)

        log_event(
            db,
            event_type="evidence.expiry_scan",
            category=CAT_WORKFLOW,
            severity=SEV_INFO,
            description=(
                f"Evidence expiry scan complete — {notified} notifications queued "
                f"({len(items)} items scanned, {skipped} skipped)"
            ),
        )
        db.commit()
        return summary

    except Exception as e:
        db.rollback()
        logger.error("scan_evidence_expiry failed: %s", e, exc_info=True)
        raise self.retry(exc=e, countdown=300)
    finally:
        db.close()
