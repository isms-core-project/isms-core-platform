"""Audit log service — Phase 9.

Provides log_event() for writing structured entries to the audit_log table.

category values : 'security' | 'workflow' | 'system'
severity values : 'info' | 'warning' | 'error' | 'critical'

Security events (login.*, user.*, role.*, api.unauthorized) are always persisted
regardless of caller.  Workflow and system events may be suppressed in future via
notification prefs (Phase 9.11) but are always logged.

Usage:
    log_event(
        db,
        event_type="policy.state.changed",
        category="workflow",
        severity="info",
        user_id=current_user.id,
        actor_email=current_user.email,
        target_type="policy",
        target_id=policy_id,
        description="Policy 'ISMS-POL-A.5.1' state changed from draft to review",
        metadata={"old_state": "draft", "new_state": "review"},
    )
    db.commit()   # caller is responsible
"""

import logging
import uuid
from typing import Any

from sqlalchemy.orm import Session as DBSession

from src.domain.system import AuditLog

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Category and severity constants — use these rather than bare strings
# ---------------------------------------------------------------------------
CAT_SECURITY = "security"
CAT_WORKFLOW = "workflow"
CAT_SYSTEM   = "system"

SEV_INFO     = "info"
SEV_WARNING  = "warning"
SEV_ERROR    = "error"
SEV_CRITICAL = "critical"


def log_event(
    db: DBSession,
    event_type: str,
    category: str = CAT_SYSTEM,
    severity: str = SEV_INFO,
    user_id: uuid.UUID | None = None,
    actor_email: str | None = None,
    target_type: str | None = None,
    target_id: uuid.UUID | str | None = None,
    description: str | None = None,
    ip_address: str | None = None,
    user_agent: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Write one audit log entry.

    Does NOT commit — the caller must commit after their own mutations so that
    the audit entry and the business change land in the same transaction.

    Args:
        db:          SQLAlchemy session.
        event_type:  Dot-notation string, e.g. "login.success", "gap.overdue".
        category:    'security' | 'workflow' | 'system'  (default: 'system').
        severity:    'info' | 'warning' | 'error' | 'critical'  (default: 'info').
        user_id:     UUID of the acting user (None for system events).
        actor_email: Email of the acting user — denormalised for log display.
        target_type: Entity type affected, e.g. "policy", "gap", "user".
        target_id:   UUID of the affected record.
        description: Human-readable one-liner.
        ip_address:  Client IP (from request; optional).
        user_agent:  Client User-Agent header (optional).
        metadata:    Arbitrary JSONB payload (old/new values, document IDs, …).
    """
    if isinstance(target_id, str):
        try:
            target_id = uuid.UUID(target_id)
        except ValueError:
            target_id = None

    entry = AuditLog(
        event_type=event_type[:60],
        category=category[:20],
        severity=severity[:10],
        user_id=user_id,
        actor_email=actor_email,
        target_type=target_type[:50] if target_type else None,
        target_id=target_id,
        description=description,
        ip_address=ip_address,
        user_agent=user_agent,
        metadata_=metadata or {},
    )
    db.add(entry)
    # Caller is responsible for db.commit() after their own changes
