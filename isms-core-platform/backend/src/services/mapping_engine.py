"""Cross-framework coverage inference engine.

Given a set of covered ISO 27001 ControlGroup IDs (from a project's assessments),
computes inferred compliance coverage across any target framework using the existing
CrossFrameworkMapping crosswalk data.

No new DB tables — computed from:
  ControlGroup → control_group_controls → FrameworkControl (ISO 27001)
    → CrossFrameworkMapping → FrameworkControl (target)
"""

import logging
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.domain.control_groups import ControlGroup, control_group_controls as cgc_table
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl

logger = logging.getLogger(__name__)

# Known framework code prefixes → display names (fallback to DB name)
KNOWN_FRAMEWORKS = {
    'NIS2':      'NIS2 Directive',
    'DORA':      'DORA',
    'GDPR':      'EU GDPR',
    'FINMA':     'FINMA',
    'NFADP':     'Swiss nFADP',
    'NIST':      'NIST CSF 2.0',
    'CIS':       'CIS Controls v8',
    'ISO27701':  'ISO 27701:2019',
    'ISO27018':  'ISO 27018:2019',
}


def get_covered_fc_ids(db: DBSession, covered_cg_ids: set) -> set:
    """Map ControlGroup IDs → ISO 27001 FrameworkControl IDs via association table."""
    if not covered_cg_ids:
        return set()
    rows = db.execute(
        select(cgc_table.c.framework_control_id)
        .where(cgc_table.c.control_group_id.in_(covered_cg_ids))
    ).scalars().all()
    return set(rows)


def get_project_covered_cg_ids(db: DBSession, project_id: str | None, org_id: str) -> set:
    """Return ControlGroup IDs that have at least one Assessment for the given project."""
    from src.domain.assessments import Assessment
    stmt = select(Assessment.control_group_id)
    if project_id:
        stmt = stmt.where(Assessment.project_id == project_id)
    else:
        # Org-wide: any assessment regardless of project
        stmt = stmt.join(ControlGroup, Assessment.control_group_id == ControlGroup.id)
    return set(db.scalars(stmt).all())


def infer_single_framework(
    db: DBSession,
    covered_fc_ids: set,
    target_fw: Framework,
) -> dict[str, Any]:
    """Compute inferred coverage for one target framework."""
    total = db.scalar(
        select(func.count(FrameworkControl.id))
        .where(FrameworkControl.framework_id == target_fw.id)
    ) or 0

    if total == 0:
        return _empty(target_fw, 0)

    if not covered_fc_ids:
        return _empty(target_fw, total)

    covered = db.scalar(
        select(func.count(func.distinct(CrossFrameworkMapping.target_control_id)))
        .join(FrameworkControl, CrossFrameworkMapping.target_control_id == FrameworkControl.id)
        .where(
            CrossFrameworkMapping.source_control_id.in_(covered_fc_ids),
            FrameworkControl.framework_id == target_fw.id,
        )
    ) or 0

    pct = round(covered / total * 100, 1) if total else 0
    return {
        'framework':          target_fw.name,
        'framework_code':     target_fw.code,
        'total_controls':     total,
        'covered_controls':   covered,
        'uncovered_controls': total - covered,
        'coverage_pct':       pct,
    }


def _empty(fw: Framework, total: int) -> dict[str, Any]:
    return {
        'framework':          fw.name,
        'framework_code':     fw.code,
        'total_controls':     total,
        'covered_controls':   0,
        'uncovered_controls': total,
        'coverage_pct':       0.0,
    }


def get_all_target_frameworks(db: DBSession) -> list[Framework]:
    """All frameworks except ISO 27001 (the source)."""
    return db.execute(
        select(Framework)
        .where(~Framework.code.ilike('ISO27001%'))
        .order_by(Framework.name)
    ).scalars().all()


def compute_multi_framework(
    db: DBSession,
    covered_fc_ids: set,
    framework_codes: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Compute coverage for multiple target frameworks."""
    if framework_codes:
        fws = db.execute(
            select(Framework).where(
                Framework.code.in_(framework_codes) |
                Framework.code.ilike_any(framework_codes)
            )
        ).scalars().all()
        if not fws:
            # Fallback: prefix match
            fws = []
            for code in framework_codes:
                fw = db.execute(
                    select(Framework).where(Framework.code.ilike(f'{code}%'))
                ).scalar_one_or_none()
                if fw:
                    fws.append(fw)
    else:
        fws = get_all_target_frameworks(db)

    return [infer_single_framework(db, covered_fc_ids, fw) for fw in fws]


def compute_gap_map(
    db: DBSession,
    covered_fc_ids: set,
    target_fw: Framework,
) -> list[dict[str, Any]]:
    """Return target framework controls NOT covered, with the ISO 27001 controls that would cover them."""
    # All target controls
    all_target = db.execute(
        select(FrameworkControl)
        .where(FrameworkControl.framework_id == target_fw.id)
        .order_by(FrameworkControl.sort_order)
    ).scalars().all()

    # Covered target control IDs
    covered_target_ids: set = set()
    if covered_fc_ids:
        covered_target_ids = set(db.scalars(
            select(func.distinct(CrossFrameworkMapping.target_control_id))
            .join(FrameworkControl, CrossFrameworkMapping.target_control_id == FrameworkControl.id)
            .where(
                CrossFrameworkMapping.source_control_id.in_(covered_fc_ids),
                FrameworkControl.framework_id == target_fw.id,
            )
        ).all())

    # For each uncovered control, find what ISO 27001 controls map to it
    gap_map = []
    for tc in all_target:
        if tc.id in covered_target_ids:
            continue
        # Find source ISO controls that map here
        iso_sources = db.execute(
            select(
                FrameworkControl.control_id.label('iso_id'),
                FrameworkControl.title.label('iso_title'),
            )
            .join(CrossFrameworkMapping, CrossFrameworkMapping.source_control_id == FrameworkControl.id)
            .where(CrossFrameworkMapping.target_control_id == tc.id)
            .order_by(FrameworkControl.control_id)
        ).all()

        gap_map.append({
            'target_control_id':    tc.control_id,
            'target_control_title': tc.title,
            'iso_controls_needed':  [{'id': r.iso_id, 'title': r.iso_title} for r in iso_sources],
        })

    return gap_map
