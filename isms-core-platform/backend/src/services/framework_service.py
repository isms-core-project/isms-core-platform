import uuid

from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl


def list_frameworks(db: DBSession) -> list[Framework]:
    return db.execute(
        select(Framework).order_by(Framework.code)
    ).scalars().all()


def get_framework(db: DBSession, framework_id: uuid.UUID) -> Framework | None:
    return db.get(Framework, framework_id)


def get_framework_controls(
    db: DBSession, framework_id: uuid.UUID, level: int | None = None,
) -> list[FrameworkControl]:
    stmt = (
        select(FrameworkControl)
        .where(FrameworkControl.framework_id == framework_id)
        .order_by(FrameworkControl.sort_order)
    )
    if level is not None:
        stmt = stmt.where(FrameworkControl.level == level)
    return db.execute(stmt).scalars().all()


def get_framework_mappings(
    db: DBSession, framework_id: uuid.UUID,
) -> list[CrossFrameworkMapping]:
    """Get all cross-framework mappings where the source is this framework."""
    return db.execute(
        select(CrossFrameworkMapping)
        .join(FrameworkControl, CrossFrameworkMapping.source_control_id == FrameworkControl.id)
        .where(FrameworkControl.framework_id == framework_id)
        .order_by(CrossFrameworkMapping.confidence.desc())
    ).scalars().all()
