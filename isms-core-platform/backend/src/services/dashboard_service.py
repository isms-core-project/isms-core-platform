"""Dashboard service — coverage, compliance, gap, and audit readiness aggregations.

All functions return plain dicts; the router layer converts to Pydantic models.
"""

import logging

from sqlalchemy import func, select
from sqlalchemy.orm import Session as DBSession

from src.database.enums import (
    ComplianceStatus,
    EvidenceType,
    GapSeverity,
    GapStatus,
    ImplType,
    PolicyType,
    ProductFamily,
    ProductType,
)
from src.domain.assessments import Assessment, AssessmentItem
from src.domain.compliance import Evidence, Gap
from src.domain.content import Implementation, Policy
from src.domain.control_groups import ControlGroup
from src.domain.frameworks import CrossFrameworkMapping, Framework, FrameworkControl

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# 3.1 — Overview
# ---------------------------------------------------------------------------

_ISMS_ONLY = ControlGroup.product_family == ProductFamily.ISMS
_ISMS_PRODUCT_TYPES = (ProductType.FRAMEWORK, ProductType.OPERATIONAL)


def get_overview(db: DBSession) -> dict:
    """Coverage counts by product and section — scoped to ISMS product family."""
    total_controls = db.scalar(
        select(func.count()).select_from(ControlGroup).where(_ISMS_ONLY)
    ) or 0
    # Operational excludes group '00' (Foundation Policies — framework-only by design)
    op_total = db.scalar(
        select(func.count()).select_from(ControlGroup)
        .where(_ISMS_ONLY, ControlGroup.group_code != "00")
    ) or 0

    # Framework coverage
    fw_pol = _count_distinct_groups(db, Policy, Policy.control_group_id,
                                    Policy.product_type == ProductType.FRAMEWORK)
    ug = db.scalar(
        select(func.count(func.distinct(Implementation.control_group_id)))
        .join(ControlGroup, Implementation.control_group_id == ControlGroup.id)
        .where(Implementation.impl_type == ImplType.UG, _ISMS_ONLY)
    ) or 0
    tg = db.scalar(
        select(func.count(func.distinct(Implementation.control_group_id)))
        .join(ControlGroup, Implementation.control_group_id == ControlGroup.id)
        .where(Implementation.impl_type == ImplType.TG, _ISMS_ONLY)
    ) or 0
    fw_assess = _count_distinct_groups(db, Assessment, Assessment.control_group_id,
                                       Assessment.product_type == ProductType.FRAMEWORK)

    # Operational coverage
    op_pol = _count_distinct_groups(db, Policy, Policy.control_group_id,
                                    Policy.product_type == ProductType.OPERATIONAL)
    op_assess = _count_distinct_groups(db, Assessment, Assessment.control_group_id,
                                       Assessment.product_type == ProductType.OPERATIONAL)

    # Assessment item statuses
    item_rows = db.execute(
        select(AssessmentItem.status, func.count(AssessmentItem.id).label("cnt"))
        .group_by(AssessmentItem.status)
    ).all()
    status_map = {s: 0 for s in ComplianceStatus}
    for row in item_rows:
        status_map[row.status] = row.cnt

    # Section breakdown — ISMS only
    section_rows = db.execute(
        select(
            ControlGroup.section,
            ControlGroup.section_name,
            func.count(ControlGroup.id).label("total"),
        )
        .where(_ISMS_ONLY)
        .group_by(ControlGroup.section, ControlGroup.section_name)
        .order_by(ControlGroup.section)
    ).all()

    sections = []
    for row in section_rows:
        fw_cov = db.scalar(
            select(func.count(func.distinct(Policy.control_group_id)))
            .join(ControlGroup, Policy.control_group_id == ControlGroup.id)
            .where(ControlGroup.section == row.section,
                   Policy.product_type == ProductType.FRAMEWORK)
        ) or 0
        op_cov = db.scalar(
            select(func.count(func.distinct(Assessment.control_group_id)))
            .join(ControlGroup, Assessment.control_group_id == ControlGroup.id)
            .where(ControlGroup.section == row.section,
                   Assessment.product_type == ProductType.OPERATIONAL)
        ) or 0
        sections.append({
            "section": row.section,
            "section_name": row.section_name,
            "total_controls": row.total,
            "framework_covered": fw_cov,
            "operational_covered": op_cov,
            "framework_pct": _pct(fw_cov, row.total),
            "operational_pct": _pct(op_cov, row.total),
        })

    # Summary counts — ISMS only
    total_policies = db.scalar(
        select(func.count()).select_from(Policy)
        .where(Policy.product_type.in_(_ISMS_PRODUCT_TYPES))
    ) or 0
    total_implementations = db.scalar(
        select(func.count()).select_from(Implementation)
        .join(ControlGroup, Implementation.control_group_id == ControlGroup.id)
        .where(_ISMS_ONLY)
    ) or 0
    total_assessments = db.scalar(
        select(func.count()).select_from(Assessment)
        .where(Assessment.product_type.in_(_ISMS_PRODUCT_TYPES))
    ) or 0
    total_open_gaps = db.scalar(
        select(func.count()).select_from(Gap).where(Gap.status == GapStatus.OPEN)
    ) or 0
    total_evidence = db.scalar(select(func.count()).select_from(Evidence)) or 0

    return {
        "total_controls": total_controls,
        "sections": sections,
        "framework": {
            "total": total_controls,
            "has_policy": fw_pol,
            "has_ug": ug,
            "has_tg": tg,
            "has_assessment": fw_assess,
            "coverage_pct": _pct(fw_pol, total_controls),
        },
        "operational": {
            "total": op_total,
            "has_policy": op_pol,
            "has_assessment": op_assess,
            "coverage_pct": _pct(op_pol, op_total),
        },
        "items_by_status": {
            "not_assessed": status_map.get(ComplianceStatus.NOT_ASSESSED, 0),
            "compliant": status_map.get(ComplianceStatus.COMPLIANT, 0),
            "partial": status_map.get(ComplianceStatus.PARTIAL, 0),
            "non_compliant": status_map.get(ComplianceStatus.NON_COMPLIANT, 0),
            "na": status_map.get(ComplianceStatus.NA, 0),
        },
        "total_policies": total_policies,
        "total_implementations": total_implementations,
        "total_assessments": total_assessments,
        "total_gaps_open": total_open_gaps,
        "total_evidence": total_evidence,
    }


# ---------------------------------------------------------------------------
# 3.2 — Framework coverage matrix
# ---------------------------------------------------------------------------

def get_coverage_matrix(
    db: DBSession,
    source_framework: str = "ISO27001",
    target_framework: str | None = None,
    limit: int = 200,
    offset: int = 0,
) -> dict:
    """Source framework controls → cross-framework mappings."""
    src_fw = db.execute(
        select(Framework).where(Framework.code.ilike(f"{source_framework}%"))
    ).scalar_one_or_none()

    all_frameworks = db.execute(
        select(Framework).order_by(Framework.name)
    ).scalars().all()

    # Exclude the source framework from the target list
    src_prefix = source_framework.upper()
    target_fws = [f for f in all_frameworks if not f.code.upper().startswith(src_prefix)]
    fw_names = [f.name for f in target_fws]

    # Leaf level differs per framework: ISO27701 Annex A controls sit at level 2
    leaf_level = 2 if src_prefix.startswith("ISO27701") else 1

    # Counts per target framework (scoped to source framework's controls)
    by_framework: dict[str, int] = {}
    total_mappings = db.scalar(select(func.count()).select_from(CrossFrameworkMapping)) or 0

    for fw in target_fws:
        stmt = (
            select(func.count(CrossFrameworkMapping.id))
            .join(FrameworkControl,
                  CrossFrameworkMapping.target_control_id == FrameworkControl.id)
            .where(FrameworkControl.framework_id == fw.id)
        )
        if src_fw:
            src_ctrl_ids = db.execute(
                select(FrameworkControl.id).where(
                    FrameworkControl.framework_id == src_fw.id,
                    FrameworkControl.level == leaf_level,
                )
            ).scalars().all()
            stmt = stmt.where(CrossFrameworkMapping.source_control_id.in_(src_ctrl_ids))
        by_framework[fw.name] = db.scalar(stmt) or 0

    # Build rows: source framework controls (leaf level only) + their mappings
    src_controls_stmt = select(FrameworkControl)
    if src_fw:
        src_controls_stmt = src_controls_stmt.where(
            FrameworkControl.framework_id == src_fw.id,
            FrameworkControl.level == leaf_level,
        )
    if target_framework:
        # Filter to source controls that have at least one mapping to this target framework
        target_fw = db.execute(
            select(Framework).where(Framework.name.ilike(f"%{target_framework}%"))
        ).scalar_one_or_none()
        if target_fw:
            src_controls_stmt = src_controls_stmt.join(
                CrossFrameworkMapping,
                CrossFrameworkMapping.source_control_id == FrameworkControl.id,
            ).join(
                FrameworkControl.__table__.alias("tfc"),
                CrossFrameworkMapping.target_control_id == FrameworkControl.__table__.alias("tfc").c.id,
            ).where(
                FrameworkControl.__table__.alias("tfc").c.framework_id == target_fw.id
            ).distinct()

    src_controls_stmt = src_controls_stmt.order_by(
        FrameworkControl.sort_order
    ).limit(limit).offset(offset)

    iso_controls = db.execute(src_controls_stmt).scalars().all()

    # Build control_group lookup — only available for ISO 27001
    from src.domain.control_groups import control_group_controls as cgc_table
    cg_map: dict[str, str] = {}
    if src_fw and src_prefix.startswith("ISO27001"):
        cg_rows = db.execute(
            select(FrameworkControl.control_id, ControlGroup.group_code)
            .join(cgc_table, cgc_table.c.framework_control_id == FrameworkControl.id)
            .join(ControlGroup, cgc_table.c.control_group_id == ControlGroup.id)
            .where(FrameworkControl.framework_id == src_fw.id)
        ).all()
        for ctrl_id, grp_code in cg_rows:
            cg_map[ctrl_id] = grp_code

    # Fetch mappings per ISO control
    rows = []
    for ctrl in iso_controls:
        mapping_rows = db.execute(
            select(
                CrossFrameworkMapping.mapping_type,
                CrossFrameworkMapping.confidence,
                FrameworkControl.control_id.label("target_control_id"),
                FrameworkControl.title.label("target_title"),
                Framework.name.label("fw_name"),
                Framework.code.label("fw_code"),
            )
            .join(FrameworkControl,
                  CrossFrameworkMapping.target_control_id == FrameworkControl.id)
            .join(Framework, FrameworkControl.framework_id == Framework.id)
            .where(CrossFrameworkMapping.source_control_id == ctrl.id)
            .order_by(Framework.name, FrameworkControl.control_id)
        ).all()

        mappings = [
            {
                "framework": r.fw_name,
                "framework_code": r.fw_code,
                "control_id": r.target_control_id,
                "control_title": r.target_title,
                "mapping_type": r.mapping_type.value if hasattr(r.mapping_type, "value") else str(r.mapping_type),
                "confidence": float(r.confidence) if r.confidence else 0.85,
            }
            for r in mapping_rows
        ]

        rows.append({
            "iso_control_id": ctrl.control_id,
            "iso_control_title": ctrl.title,
            "control_group_code": cg_map.get(ctrl.control_id),
            "mappings": mappings,
        })

    return {
        "frameworks": fw_names,
        "total_iso_controls": len(iso_controls),
        "total_mappings": total_mappings,
        "by_framework": by_framework,
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# 3.2b — Framework overview (non-ISO27001)
# ---------------------------------------------------------------------------

def _extract_fw_section(control_id: str) -> str:
    """Derive a section key from a framework control_id (non-ISO27001)."""
    parts = control_id.split(".")
    # All-alpha prefix ≥3 chars and not bare "A" (e.g. CLD, CSP, CSC) → keep parts[0]
    if len(parts[0]) >= 3 and parts[0].isalpha() and parts[0] != "A":
        return f"{parts[0]}.{parts[1]}" if len(parts) > 1 else parts[0]
    # A.1.x.x → A.1,  A.x.x → A.x
    return ".".join(parts[:2]) if len(parts) >= 2 else parts[0]


def get_framework_overview(db: DBSession, source_framework: str = "ISO27701") -> dict:
    """Control counts + mapping coverage for a non-ISO27001 framework."""
    src_fw = db.execute(
        select(Framework).where(Framework.code.ilike(f"{source_framework}%"))
    ).scalar_one_or_none()

    src_prefix = source_framework.upper()
    leaf_level = 2 if src_prefix.startswith("ISO27701") else 1

    if not src_fw:
        return {
            "framework_code": source_framework,
            "framework_name": source_framework,
            "total_controls": 0,
            "controls_with_mappings": 0,
            "total_mappings": 0,
            "coverage_pct": 0.0,
            "by_target_framework": {},
            "sections": [],
        }

    leaf_controls = db.execute(
        select(FrameworkControl)
        .where(
            FrameworkControl.framework_id == src_fw.id,
            FrameworkControl.level == leaf_level,
        )
        .order_by(FrameworkControl.sort_order)
    ).scalars().all()

    total_controls = len(leaf_controls)
    leaf_ids = [c.id for c in leaf_controls]

    if not leaf_ids:
        return {
            "framework_code": src_fw.code,
            "framework_name": src_fw.name,
            "total_controls": 0,
            "controls_with_mappings": 0,
            "total_mappings": 0,
            "coverage_pct": 0.0,
            "by_target_framework": {},
            "sections": [],
        }

    total_mappings = db.scalar(
        select(func.count(CrossFrameworkMapping.id))
        .where(CrossFrameworkMapping.source_control_id.in_(leaf_ids))
    ) or 0

    controls_with_mappings = db.scalar(
        select(func.count(func.distinct(CrossFrameworkMapping.source_control_id)))
        .where(CrossFrameworkMapping.source_control_id.in_(leaf_ids))
    ) or 0

    fw_rows = db.execute(
        select(Framework.name, func.count(CrossFrameworkMapping.id).label("cnt"))
        .join(FrameworkControl, CrossFrameworkMapping.target_control_id == FrameworkControl.id)
        .join(Framework, FrameworkControl.framework_id == Framework.id)
        .where(CrossFrameworkMapping.source_control_id.in_(leaf_ids))
        .group_by(Framework.name)
        .order_by(func.count(CrossFrameworkMapping.id).desc())
    ).all()

    by_target = {r.name: r.cnt for r in fw_rows}

    # Section breakdown — one query for all mapped IDs
    mapped_ctrl_ids = set(
        db.execute(
            select(func.distinct(CrossFrameworkMapping.source_control_id))
            .where(CrossFrameworkMapping.source_control_id.in_(leaf_ids))
        ).scalars().all()
    )

    sections_map: dict[str, dict] = {}
    for ctrl in leaf_controls:
        sec = _extract_fw_section(ctrl.control_id)
        if sec not in sections_map:
            sections_map[sec] = {"section": sec, "count": 0, "mapped_count": 0}
        sections_map[sec]["count"] += 1
        if ctrl.id in mapped_ctrl_ids:
            sections_map[sec]["mapped_count"] += 1

    return {
        "framework_code": src_fw.code,
        "framework_name": src_fw.name,
        "total_controls": total_controls,
        "controls_with_mappings": controls_with_mappings,
        "total_mappings": total_mappings,
        "coverage_pct": _pct(controls_with_mappings, total_controls),
        "by_target_framework": by_target,
        "sections": list(sections_map.values()),
    }


# ---------------------------------------------------------------------------
# 3.3 — Gap analysis
# ---------------------------------------------------------------------------

def get_gaps(
    db: DBSession,
    severity: str | None = None,
    status: str | None = None,
    product: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> dict:
    """Open gaps by severity, owner, product."""
    base = (
        select(Gap, ControlGroup.group_code, ControlGroup.name)
        .join(ControlGroup, Gap.control_group_id == ControlGroup.id)
    )
    if severity:
        base = base.where(Gap.severity == GapSeverity(severity))
    if status:
        base = base.where(Gap.status == GapStatus(status))
    if product:
        base = base.where(Gap.product_type == product)

    total = db.scalar(
        select(func.count()).select_from(base.subquery())
    ) or 0

    by_severity = {s.value: 0 for s in GapSeverity}
    for row in db.execute(
        select(Gap.severity, func.count(Gap.id)).group_by(Gap.severity)
    ).all():
        by_severity[row[0].value] = row[1]

    by_status = {s.value: 0 for s in GapStatus}
    for row in db.execute(
        select(Gap.status, func.count(Gap.id)).group_by(Gap.status)
    ).all():
        by_status[row[0].value] = row[1]

    by_product: dict[str, int] = {}
    for row in db.execute(
        select(Gap.product_type, func.count(Gap.id)).group_by(Gap.product_type)
    ).all():
        by_product[row[0]] = row[1]

    rows = db.execute(
        base.order_by(Gap.severity, Gap.created_at.desc())
        .limit(limit).offset(offset)
    ).all()

    items = []
    for gap, group_code, group_name in rows:
        items.append({
            "id": gap.id,
            "control_group_code": group_code,
            "control_group_name": group_name,
            "description": gap.gap_description,
            "severity": gap.severity.value,
            "status": gap.status.value,
            "owner": gap.owner,
            "due_date": gap.due_date,
            "product_type": gap.product_type,
        })

    return {
        "total": total,
        "by_severity": by_severity,
        "by_status": by_status,
        "by_product": by_product,
        "items": items,
    }


# ---------------------------------------------------------------------------
# 3.4 — Evidence status
# ---------------------------------------------------------------------------

def get_evidence_status(db: DBSession) -> dict:
    """Evidence coverage per control group."""
    total = db.scalar(select(func.count()).select_from(Evidence)) or 0

    by_type = {e.value: 0 for e in EvidenceType}
    for row in db.execute(
        select(Evidence.evidence_type, func.count(Evidence.id))
        .group_by(Evidence.evidence_type)
    ).all():
        by_type[row[0].value] = row[1]

    controls_with = db.scalar(
        select(func.count(func.distinct(Evidence.control_group_id)))
        .join(ControlGroup, Evidence.control_group_id == ControlGroup.id)
        .where(_ISMS_ONLY)
    ) or 0
    total_controls = db.scalar(
        select(func.count()).select_from(ControlGroup).where(_ISMS_ONLY)
    ) or 0

    rows = db.execute(
        select(
            ControlGroup.group_code,
            ControlGroup.name,
            func.count(Evidence.id).label("cnt"),
            func.max(Evidence.collected_date).label("latest"),
        )
        .join(Evidence, ControlGroup.id == Evidence.control_group_id, isouter=True)
        .where(_ISMS_ONLY)
        .group_by(ControlGroup.group_code, ControlGroup.name)
        .order_by(ControlGroup.group_code)
    ).all()

    items = [
        {
            "control_group_code": r.group_code,
            "control_group_name": r.name,
            "evidence_count": r.cnt or 0,
            "latest_date": r.latest,
        }
        for r in rows
    ]

    return {
        "total": total,
        "by_type": by_type,
        "controls_with_evidence": controls_with,
        "controls_without_evidence": total_controls - controls_with,
        "items": items,
    }


# ---------------------------------------------------------------------------
# 3.5 — Audit readiness
# ---------------------------------------------------------------------------

def get_audit_readiness(db: DBSession) -> dict:
    """Composite readiness score (0-100) across all artefact types — ISMS only."""
    total = db.scalar(
        select(func.count()).select_from(ControlGroup).where(_ISMS_ONLY)
    ) or 0
    if not total:
        return {
            "policies_pct": 0.0, "ug_pct": 0.0, "tg_pct": 0.0,
            "assessments_pct": 0.0, "evidence_pct": 0.0,
            "gaps_closed_pct": 100.0, "composite_score": 0.0,
            "status": "red", "breakdown": {},
        }

    fw_pol = _count_distinct_groups(
        db, Policy, Policy.control_group_id,
        Policy.product_type == ProductType.FRAMEWORK,
        Policy.policy_type == PolicyType.POL,
    )
    ug = db.scalar(
        select(func.count(func.distinct(Implementation.control_group_id)))
        .join(ControlGroup, Implementation.control_group_id == ControlGroup.id)
        .where(Implementation.impl_type == ImplType.UG, _ISMS_ONLY)
    ) or 0
    tg = db.scalar(
        select(func.count(func.distinct(Implementation.control_group_id)))
        .join(ControlGroup, Implementation.control_group_id == ControlGroup.id)
        .where(Implementation.impl_type == ImplType.TG, _ISMS_ONLY)
    ) or 0
    fw_assess = _count_distinct_groups(db, Assessment, Assessment.control_group_id,
                                       Assessment.product_type == ProductType.FRAMEWORK)
    evidence = db.scalar(
        select(func.count(func.distinct(Evidence.control_group_id)))
        .join(ControlGroup, Evidence.control_group_id == ControlGroup.id)
        .where(_ISMS_ONLY)
    ) or 0

    total_gaps = db.scalar(select(func.count()).select_from(Gap)) or 0
    closed_gaps = db.scalar(
        select(func.count()).select_from(Gap)
        .where(Gap.status.in_([GapStatus.CLOSED, GapStatus.ACCEPTED]))
    ) or 0

    policies_pct = _pct(fw_pol, total)
    ug_pct = _pct(ug, total)
    tg_pct = _pct(tg, total)
    assessments_pct = _pct(fw_assess, total)
    evidence_pct = _pct(evidence, total)
    gaps_closed_pct = _pct(closed_gaps, total_gaps) if total_gaps else 100.0

    # Weighted composite
    # Policies 20% | UG 15% | TG 15% | Assessments 20% | Evidence 20% | Gaps 10%
    composite = round(
        policies_pct * 0.20
        + ug_pct * 0.15
        + tg_pct * 0.15
        + assessments_pct * 0.20
        + evidence_pct * 0.20
        + gaps_closed_pct * 0.10,
        1,
    )
    status = "green" if composite >= 80 else ("amber" if composite >= 50 else "red")

    return {
        "policies_pct": policies_pct,
        "ug_pct": ug_pct,
        "tg_pct": tg_pct,
        "assessments_pct": assessments_pct,
        "evidence_pct": evidence_pct,
        "gaps_closed_pct": gaps_closed_pct,
        "composite_score": composite,
        "status": status,
        "breakdown": {
            "total_controls": total,
            "controls_with_pol": fw_pol,
            "controls_with_ug": ug,
            "controls_with_tg": tg,
            "controls_with_assessment": fw_assess,
            "controls_with_evidence": evidence,
            "total_gaps": total_gaps,
            "gaps_closed": closed_gaps,
        },
    }


# ---------------------------------------------------------------------------
# 3.10 — Control dependency graph
# ---------------------------------------------------------------------------

def get_graph(
    db: DBSession,
    source_framework: str = "ISO27001",
    center: str | None = None,
    depth: int = 2,
    edge_types: list[str] | None = None,
    section: str | None = None,
    max_nodes: int = 300,
) -> dict:
    """Build control dependency graph from CrossFrameworkMappings.

    Nodes: ControlGroup + FrameworkControl (source framework + target frameworks)
    Edges: CrossFrameworkMapping records
    """
    depth = min(depth, 3)  # Safety cap

    src_prefix = source_framework.upper()
    is_iso27001 = src_prefix.startswith("ISO27001")

    # For non-ISO27001 source frameworks, seed directly from FrameworkControl records
    if not is_iso27001:
        src_fw = db.execute(
            select(Framework).where(Framework.code.ilike(f"{source_framework}%"))
        ).scalar_one_or_none()

        nodes: dict[str, dict] = {}
        edges: list[dict] = []
        seen_edges: set[tuple] = set()

        if src_fw:
            leaf_level = 2 if src_prefix.startswith("ISO27701") else 1
            src_ctrl_stmt = select(FrameworkControl).where(
                FrameworkControl.framework_id == src_fw.id,
                FrameworkControl.level == leaf_level,
            ).order_by(FrameworkControl.sort_order)
            if center:
                src_ctrl_stmt = src_ctrl_stmt.where(
                    FrameworkControl.control_id.ilike(f"{center}%")
                )
            if section:
                src_ctrl_stmt = src_ctrl_stmt.where(
                    FrameworkControl.control_id.ilike(f"{section}.%")
                )

            src_controls = db.execute(src_ctrl_stmt).scalars().all()

            for ctrl in src_controls:
                if len(nodes) >= max_nodes:
                    break
                node_id = f"iso:{ctrl.control_id}"
                # Derive section label from control_id (e.g. A.1.3.1 → A.1)
                parts = ctrl.control_id.split(".")
                sec_label = ".".join(parts[:2]) if len(parts) >= 3 else parts[0]
                nodes[node_id] = {
                    "id": node_id,
                    "label": f"{ctrl.control_id}: {ctrl.title[:60]}",
                    "node_type": "iso_control",
                    "framework": src_fw.name,
                    "section": sec_label,
                    "group_code": None,
                }

                if depth >= 2 and len(nodes) < max_nodes:
                    mapping_stmt = select(
                        CrossFrameworkMapping,
                        FrameworkControl.control_id.label("target_ctrl_id"),
                        FrameworkControl.title.label("target_title"),
                        Framework.name.label("fw_name"),
                        Framework.code.label("fw_code"),
                    ).join(
                        FrameworkControl,
                        CrossFrameworkMapping.target_control_id == FrameworkControl.id
                    ).join(
                        Framework,
                        FrameworkControl.framework_id == Framework.id
                    ).where(
                        CrossFrameworkMapping.source_control_id == ctrl.id
                    )
                    if edge_types:
                        mapping_stmt = mapping_stmt.where(
                            CrossFrameworkMapping.mapping_type.in_(edge_types)
                        )

                    for m_row in db.execute(mapping_stmt).all():
                        if len(nodes) >= max_nodes:
                            break
                        target_node_id = f"ext:{m_row.fw_code}:{m_row.target_ctrl_id}"
                        if target_node_id not in nodes:
                            nodes[target_node_id] = {
                                "id": target_node_id,
                                "label": f"{m_row.target_ctrl_id}: {m_row.target_title[:60]}",
                                "node_type": "external_ref",
                                "framework": m_row.fw_name,
                                "section": None,
                                "group_code": None,
                            }
                        edge_key = (node_id, target_node_id)
                        if edge_key not in seen_edges:
                            seen_edges.add(edge_key)
                            mt = m_row.CrossFrameworkMapping.mapping_type
                            edges.append({
                                "source": node_id,
                                "target": target_node_id,
                                "edge_type": mt.value if hasattr(mt, "value") else str(mt),
                                "confidence": float(m_row.CrossFrameworkMapping.confidence)
                                if m_row.CrossFrameworkMapping.confidence else None,
                            })

        node_list = list(nodes.values())
        return {
            "nodes": node_list,
            "edges": edges,
            "total_nodes": len(node_list),
            "total_edges": len(edges),
        }

    # ISO 27001 path: seed from ControlGroups via junction table
    iso_fw = db.execute(
        select(Framework).where(Framework.code.ilike("ISO27001%"))
    ).scalar_one_or_none()

    # Seed control groups
    cg_stmt = select(ControlGroup).order_by(ControlGroup.group_code)
    if center:
        cg_stmt = cg_stmt.where(ControlGroup.group_code.ilike(f"%{center}%"))
    if section:
        cg_stmt = cg_stmt.where(ControlGroup.section == section)

    control_groups = db.execute(cg_stmt).scalars().all()

    # Build node + edge sets
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    seen_edges: set[tuple] = set()

    # Add control group nodes
    for cg in control_groups:
        node_id = f"cg:{cg.group_code}"
        nodes[node_id] = {
            "id": node_id,
            "label": f"{cg.group_code}: {cg.name[:50]}",
            "node_type": "control_group",
            "framework": "ISO 27001",
            "section": cg.section,
            "group_code": cg.group_code,
        }

    # For each control group, find its ISO 27001 framework controls
    if iso_fw:
        from src.domain.control_groups import control_group_controls as cgc_table
        for cg in control_groups:
            iso_ctrls = db.execute(
                select(FrameworkControl)
                .join(cgc_table, cgc_table.c.framework_control_id == FrameworkControl.id)
                .where(
                    cgc_table.c.control_group_id == cg.id,
                    FrameworkControl.framework_id == iso_fw.id,
                )
            ).scalars().all()

            cg_node_id = f"cg:{cg.group_code}"
            for iso_ctrl in iso_ctrls:
                iso_node_id = f"iso:{iso_ctrl.control_id}"
                nodes[iso_node_id] = {
                    "id": iso_node_id,
                    "label": f"{iso_ctrl.control_id}: {iso_ctrl.title[:60]}",
                    "node_type": "iso_control",
                    "framework": "ISO 27001",
                    "section": iso_ctrl.control_id.split(".")[0] if "." in iso_ctrl.control_id else None,
                    "group_code": cg.group_code,
                }
                edge_key = (cg_node_id, iso_node_id)
                if edge_key not in seen_edges:
                    seen_edges.add(edge_key)
                    edges.append({
                        "source": cg_node_id,
                        "target": iso_node_id,
                        "edge_type": "contains",
                        "confidence": None,
                    })

                # If depth >= 2, follow cross-framework mappings
                if depth >= 2 and len(nodes) < max_nodes:
                    mapping_stmt = select(
                        CrossFrameworkMapping,
                        FrameworkControl.control_id.label("target_ctrl_id"),
                        FrameworkControl.title.label("target_title"),
                        Framework.name.label("fw_name"),
                        Framework.code.label("fw_code"),
                    ).join(
                        FrameworkControl,
                        CrossFrameworkMapping.target_control_id == FrameworkControl.id
                    ).join(
                        Framework,
                        FrameworkControl.framework_id == Framework.id
                    ).where(
                        CrossFrameworkMapping.source_control_id == iso_ctrl.id
                    )

                    if edge_types:
                        mapping_stmt = mapping_stmt.where(
                            CrossFrameworkMapping.mapping_type.in_(edge_types)
                        )

                    for m_row in db.execute(mapping_stmt).all():
                        if len(nodes) >= max_nodes:
                            break
                        target_node_id = f"ext:{m_row.fw_code}:{m_row.target_ctrl_id}"
                        if target_node_id not in nodes:
                            nodes[target_node_id] = {
                                "id": target_node_id,
                                "label": f"{m_row.target_ctrl_id}: {m_row.target_title[:60]}",
                                "node_type": "external_ref",
                                "framework": m_row.fw_name,
                                "section": None,
                                "group_code": None,
                            }
                        edge_key = (iso_node_id, target_node_id)
                        if edge_key not in seen_edges:
                            seen_edges.add(edge_key)
                            mt = m_row.CrossFrameworkMapping.mapping_type
                            edges.append({
                                "source": iso_node_id,
                                "target": target_node_id,
                                "edge_type": mt.value if hasattr(mt, "value") else str(mt),
                                "confidence": float(m_row.CrossFrameworkMapping.confidence)
                                if m_row.CrossFrameworkMapping.confidence else None,
                            })

    node_list = list(nodes.values())
    return {
        "nodes": node_list,
        "edges": edges,
        "total_nodes": len(node_list),
        "total_edges": len(edges),
    }


# ---------------------------------------------------------------------------
# Coverage gaps — per-control-group missing artefacts
# ---------------------------------------------------------------------------

def get_coverage_gaps(db: DBSession, product: str) -> list[dict]:
    """Return control groups that are missing artefacts for the given product.

    Framework expects: policy + UG + TG + assessment.
    Operational expects: policy + assessment.
    Returns only controls with at least one missing artefact.
    """
    product_type = ProductType.FRAMEWORK if product == "framework" else ProductType.OPERATIONAL

    # Sets of control_group_ids that have each artefact
    def _ids(model, *conditions):
        stmt = select(func.distinct(model.control_group_id))
        for cond in conditions:
            stmt = stmt.where(cond)
        return {row[0] for row in db.execute(stmt).all()}

    has_policy = _ids(Policy, Policy.product_type == product_type)
    has_assessment = _ids(Assessment, Assessment.product_type == product_type)
    has_ug = _ids(Implementation, Implementation.impl_type == ImplType.UG) if product == "framework" else None
    has_tg = _ids(Implementation, Implementation.impl_type == ImplType.TG) if product == "framework" else None

    # ISMS control groups only, ordered by section + code
    # Exclude group '00' (Foundation Policies) from Operational — it is framework-only by design
    stmt = (
        select(ControlGroup)
        .where(_ISMS_ONLY)
        .order_by(ControlGroup.section, ControlGroup.group_code)
    )
    if product == "operational":
        stmt = stmt.where(ControlGroup.group_code != "00")
    groups = db.execute(stmt).scalars().all()

    result = []
    for cg in groups:
        missing = []
        if cg.id not in has_policy:
            missing.append("policy")
        if product == "framework":
            if cg.id not in has_ug:
                missing.append("UG")
            if cg.id not in has_tg:
                missing.append("TG")
        if cg.id not in has_assessment:
            missing.append("assessment")

        if missing:
            result.append({
                "id": str(cg.id),
                "group_code": cg.group_code,
                "name": cg.name,
                "section": cg.section,
                "section_name": cg.section_name,
                "missing": missing,
            })

    return result


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_home_summary(db: DBSession) -> dict:
    """Per-product group/policy/IMP counts for the platform home page."""
    products = (
        (ProductFamily.ISMS,    "isms"),
        (ProductFamily.PRIVACY, "privacy"),
        (ProductFamily.CLOUD,   "cloud"),
    )
    result = {}
    for family, key in products:
        is_fam = ControlGroup.product_family == family
        groups = db.scalar(select(func.count()).select_from(ControlGroup).where(is_fam)) or 0

        pol_join = (
            select(func.count(Policy.id))
            .join(ControlGroup, ControlGroup.id == Policy.control_group_id)
            .where(is_fam)
        )
        policies = db.scalar(pol_join) or 0

        imp_join = (
            select(func.count(Implementation.id))
            .join(ControlGroup, ControlGroup.id == Implementation.control_group_id)
            .where(is_fam)
        )
        imps = db.scalar(imp_join) or 0

        result[key] = {"groups": groups, "policies": policies, "imps": imps}

    # Add ISMS-specific metrics
    isms_total = result["isms"]["groups"]
    fw_pol = _count_distinct_groups(
        db, Policy, Policy.control_group_id,
        Policy.product_type == ProductType.FRAMEWORK,
        Policy.policy_type == PolicyType.POL,
    )
    op_pol = _count_distinct_groups(
        db, Policy, Policy.control_group_id,
        Policy.product_type == ProductType.OPERATIONAL,
    )
    op_total = db.scalar(
        select(func.count()).select_from(ControlGroup)
        .where(_ISMS_ONLY, ControlGroup.group_code != "00")
    ) or 0
    open_gaps = db.scalar(
        select(func.count()).select_from(Gap)
        .where(Gap.status.in_([GapStatus.OPEN, GapStatus.IN_PROGRESS]))
    ) or 0
    result["isms"]["fw_coverage_pct"] = _pct(fw_pol, isms_total)
    result["isms"]["op_coverage_pct"] = _pct(op_pol, op_total)
    result["isms"]["open_gaps"] = open_gaps

    # Connector summary (platform-level, not product-specific)
    from src.domain.connectors import Connector, ConnectorEvidence
    active_connectors = db.scalar(
        select(func.count()).select_from(Connector).where(Connector.status == "active")
    ) or 0
    total_evidence = db.scalar(select(func.count()).select_from(ConnectorEvidence)) or 0
    result["connectors"] = {
        "active": active_connectors,
        "evidence_items": total_evidence,
    }

    return result


def _pct(n: int, total: int) -> float:
    if not total:
        return 0.0
    return round(n / total * 100, 1)


def _count_distinct_groups(db, model, col, *conditions) -> int:
    stmt = select(func.count(func.distinct(col)))
    for cond in conditions:
        stmt = stmt.where(cond)
    return db.scalar(stmt) or 0
