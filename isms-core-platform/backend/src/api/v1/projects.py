"""Projects API — Library/Project workspace.

GET    /api/v1/projects                                          list projects
POST   /api/v1/projects                                          create project
GET    /api/v1/projects/{id}                                     get project detail
PATCH  /api/v1/projects/{id}                                     update project
DELETE /api/v1/projects/{id}                                     delete project

GET    /api/v1/projects/{id}/library/policies                    browse library policies
GET    /api/v1/projects/{id}/library/implementations             browse library implementations
GET    /api/v1/projects/{id}/library/checklists                  browse library checklists (SCR)

GET    /api/v1/projects/{id}/policies                            list project policies
POST   /api/v1/projects/{id}/policies                            add policy (library or custom)
GET    /api/v1/projects/{id}/policies/{pp_id}                    get single project policy (with custom_content)
PATCH  /api/v1/projects/{id}/policies/{pp_id}                    update project policy
DELETE /api/v1/projects/{id}/policies/{pp_id}                    remove policy from project

GET    /api/v1/projects/{id}/implementations                     list project implementations
POST   /api/v1/projects/{id}/implementations                     add implementation
GET    /api/v1/projects/{id}/implementations/{pi_id}             get single project implementation (with custom_content)
PATCH  /api/v1/projects/{id}/implementations/{pi_id}             update project implementation
DELETE /api/v1/projects/{id}/implementations/{pi_id}             remove implementation from project

GET    /api/v1/projects/{id}/checklists                          list project checklists (summary)
POST   /api/v1/projects/{id}/checklists                          clone library SCR into project
GET    /api/v1/projects/{id}/checklists/{cid}                    get checklist detail with items + N/A overrides
PATCH  /api/v1/projects/{id}/checklists/{cid}/items              toggle N/A on a checklist item
DELETE /api/v1/projects/{id}/checklists/{cid}                    remove checklist from project
"""

import logging
import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query

logger = logging.getLogger(__name__)
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context
from src.database.enums import ProductFamily, UserRole
from src.domain.organisations import Organisation
from src.database.session import get_db
from src.domain.content import Implementation, Policy
from src.domain.control_groups import ControlGroup
from src.domain.assessments import Assessment, AssessmentItem
from src.domain.projects import Project, ProjectChecklist, ProjectImplementation, ProjectPolicy
from src.domain.users import User
from src.schemas.projects import (
    DocVars,
    LibraryChecklistItem,
    LibraryImplItem,
    LibraryPolicyItem,
    ProjectChecklistAdd,
    ProjectChecklistItemPatch,
    ProjectChecklistRead,
    ProjectCreate,
    ProjectImplAdd,
    ProjectImplPatch,
    ProjectImplRead,
    ProjectPatch,
    ProjectPolicyAdd,
    ProjectPolicyPatch,
    ProjectPolicyRead,
    ProjectRead,
    apply_doc_vars,
)

router = APIRouter(prefix="/projects", tags=["projects"])


# ── helpers ──────────────────────────────────────────────────────────────────

def _get_project_or_404(project_id: uuid.UUID, db: DBSession, current_user: User) -> Project:
    p = db.get(Project, project_id)
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    if current_user.role != UserRole.SUPER_ADMIN and p.organisation_id != current_user.organisation_id:
        raise HTTPException(status_code=404, detail="Project not found")
    return p


def _enrich_project(p: Project, db: DBSession) -> ProjectRead:
    from sqlalchemy import func as sqlfunc
    pol_count = db.execute(
        select(sqlfunc.count()).select_from(ProjectPolicy).where(
            ProjectPolicy.project_id == p.id,
            ProjectPolicy.status == "active",
        )
    ).scalar() or 0
    impl_count = db.execute(
        select(sqlfunc.count()).select_from(ProjectImplementation).where(
            ProjectImplementation.project_id == p.id,
            ProjectImplementation.status == "active",
        )
    ).scalar() or 0
    checklist_count = db.execute(
        select(sqlfunc.count()).select_from(ProjectChecklist).where(
            ProjectChecklist.project_id == p.id,
        )
    ).scalar() or 0
    settings = p.settings or {}
    raw_dv = settings.get("doc_vars")
    doc_vars = DocVars(**raw_dv) if isinstance(raw_dv, dict) else None
    org_name = p.organisation.name if p.organisation else None
    return ProjectRead(
        id=p.id,
        name=p.name,
        organisation_id=p.organisation_id,
        organisation_name=org_name,
        product_family=p.product_family.value if hasattr(p.product_family, "value") else p.product_family,
        project_subtype=settings.get("project_subtype"),
        description=p.description,
        status=p.status.value if hasattr(p.status, "value") else p.status,
        owner_id=p.owner_id,
        created_at=p.created_at,
        updated_at=p.updated_at,
        doc_vars=doc_vars,
        policy_count=pol_count,
        implementation_count=impl_count,
        checklist_count=checklist_count,
    )


def _enrich_project_policy(pp: ProjectPolicy, db: DBSession) -> ProjectPolicyRead:
    doc_id = title = pol_type = prod_type = cg_code = None
    if pp.lib_policy_id:
        pol = db.get(Policy, pp.lib_policy_id)
        if pol:
            doc_id = pol.document_id
            title = pol.title
            pol_type = pol.policy_type.value if hasattr(pol.policy_type, "value") else pol.policy_type
            prod_type = pol.product_type.value if hasattr(pol.product_type, "value") else pol.product_type
            cg = db.get(ControlGroup, pol.control_group_id)
            cg_code = cg.group_code if cg else None
    return ProjectPolicyRead(
        id=pp.id,
        project_id=pp.project_id,
        lib_policy_id=pp.lib_policy_id,
        document_id=doc_id,
        title=title,
        policy_type=pol_type,
        product_type=prod_type,
        control_group_code=cg_code,
        is_edited=pp.is_edited,
        stacking_locked=pp.stacking_locked,
        stale_warning=pp.stale_warning,
        status=pp.status,
        created_at=pp.created_at,
    )


def _enrich_project_impl(pi: ProjectImplementation, db: DBSession) -> ProjectImplRead:
    doc_id = title = impl_type = cg_code = None
    if pi.lib_impl_id:
        impl = db.get(Implementation, pi.lib_impl_id)
        if impl:
            doc_id = impl.document_id
            title = impl.title
            impl_type = impl.impl_type.value if hasattr(impl.impl_type, "value") else impl.impl_type
            cg = db.get(ControlGroup, impl.control_group_id)
            cg_code = cg.group_code if cg else None
    return ProjectImplRead(
        id=pi.id,
        project_id=pi.project_id,
        lib_impl_id=pi.lib_impl_id,
        document_id=doc_id,
        title=title,
        impl_type=impl_type,
        control_group_code=cg_code,
        is_edited=pi.is_edited,
        stale_warning=pi.stale_warning,
        status=pi.status,
        created_at=pi.created_at,
    )


# ── Projects CRUD ─────────────────────────────────────────────────────────────

@router.get("", response_model=list[ProjectRead])
def list_projects(
    product_family: str | None = Query(None),
    status: str | None = Query(None),
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    org_id: uuid.UUID = Depends(get_org_context),
):
    q = select(Project)
    # super_admin sees all orgs' projects; everyone else is scoped to their own org
    if current_user.role != UserRole.SUPER_ADMIN:
        q = q.where(Project.organisation_id == org_id)
    if product_family:
        q = q.where(Project.product_family == product_family.upper())
    if status:
        q = q.where(Project.status == status)
    q = q.order_by(Project.created_at.desc())
    projects = db.execute(q).scalars().all()
    return [_enrich_project(p, db) for p in projects]


@router.post("", response_model=ProjectRead, status_code=201)
def create_project(
    body: ProjectCreate,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    org_id: uuid.UUID = Depends(get_org_context),
):
    fam = body.product_family.upper()
    if fam not in ("ISMS", "PRIVACY", "CLOUD", "AI", "SEC"):
        raise HTTPException(status_code=422, detail="product_family must be ISMS, PRIVACY, CLOUD, AI, or SEC")
    # super_admin may override the target organisation
    target_org_id = org_id
    if body.organisation_id is not None:
        if current_user.role != UserRole.SUPER_ADMIN:
            raise HTTPException(status_code=403, detail="Only super_admin may assign a project to a different organisation")
        org = db.get(Organisation, body.organisation_id)
        if not org:
            raise HTTPException(status_code=404, detail="Organisation not found")
        target_org_id = body.organisation_id
    settings: dict = {}
    if body.doc_vars:
        settings["doc_vars"] = body.doc_vars.model_dump(exclude_none=True)
    if body.project_subtype:
        settings["project_subtype"] = body.project_subtype.lower()
    p = Project(
        name=body.name,
        organisation_id=target_org_id,
        product_family=ProductFamily(fam),
        description=body.description,
        owner_id=current_user.id,
        settings=settings or None,
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return _enrich_project(p, db)


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return _enrich_project(_get_project_or_404(project_id, db, current_user), db)


@router.patch("/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: uuid.UUID,
    body: ProjectPatch,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    p = _get_project_or_404(project_id, db, current_user)
    if body.name is not None:
        p.name = body.name
    if body.description is not None:
        p.description = body.description
    if body.status is not None:
        if body.status not in ("draft", "active", "inactive", "archived"):
            raise HTTPException(status_code=422, detail="status must be draft, active, or archived")
        p.status = body.status
    if body.doc_vars is not None:
        settings = dict(p.settings or {})
        settings["doc_vars"] = body.doc_vars.model_dump(exclude_none=True)
        p.settings = settings
    if body.project_subtype is not None:
        settings = dict(p.settings or {})
        settings["project_subtype"] = body.project_subtype.lower()
        p.settings = settings
    db.commit()
    db.refresh(p)
    return _enrich_project(p, db)


@router.delete("/{project_id}", status_code=204)
def delete_project(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    p = _get_project_or_404(project_id, db, current_user)
    db.delete(p)
    db.commit()


# ── Re-apply doc vars ─────────────────────────────────────────────────────────

@router.post("/{project_id}/reapply-doc-vars")
def reapply_doc_vars(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Re-read each library source file and re-apply current doc_vars substitution.

    Use this after updating doc_vars on an existing project to refresh all
    already-imported policies and implementations.
    Custom (non-library) documents are not touched.
    """
    project = _get_project_or_404(project_id, db, current_user)
    settings = project.settings or {}
    raw_dv = settings.get("doc_vars")
    doc_vars = DocVars(**raw_dv) if isinstance(raw_dv, dict) else None

    updated_pol = 0
    updated_impl = 0
    errors: list[str] = []

    for pp in db.execute(
        select(ProjectPolicy).where(
            ProjectPolicy.project_id == project_id,
            ProjectPolicy.lib_policy_id.isnot(None),
        )
    ).scalars():
        lib_pol = db.get(Policy, pp.lib_policy_id)
        if lib_pol and lib_pol.file_path:
            try:
                raw = Path(lib_pol.file_path).read_text(encoding="utf-8")
                pp.custom_content = apply_doc_vars(raw, project.organisation.name if project.organisation else "", doc_vars)
                pp.is_edited = False
                updated_pol += 1
            except OSError as e:
                errors.append(f"policy {lib_pol.document_id}: {e}")

    for pi in db.execute(
        select(ProjectImplementation).where(
            ProjectImplementation.project_id == project_id,
            ProjectImplementation.lib_impl_id.isnot(None),
        )
    ).scalars():
        lib_impl = db.get(Implementation, pi.lib_impl_id)
        if lib_impl and lib_impl.file_path:
            try:
                raw = Path(lib_impl.file_path).read_text(encoding="utf-8")
                pi.custom_content = apply_doc_vars(raw, project.organisation.name if project.organisation else "", doc_vars)
                pi.is_edited = False
                updated_impl += 1
            except OSError as e:
                errors.append(f"impl {lib_impl.document_id}: {e}")

    db.commit()
    return {"status": "ok", "updated_policies": updated_pol, "updated_implementations": updated_impl, "errors": errors}


# ── Library browser ───────────────────────────────────────────────────────────

@router.get("/{project_id}/library/policies", response_model=list[LibraryPolicyItem])
def browse_library_policies(
    project_id: uuid.UUID,
    product_type: str | None = Query(None),
    language: str | None = Query(None),
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return all Library policies for this project's product family.
    Flags which ones are already in the project.
    """
    p = _get_project_or_404(project_id, db, current_user)
    family = p.product_family.value if hasattr(p.product_family, "value") else p.product_family

    # Map product_family → ProductType enum values stored on policies
    from src.database.enums import ProductType
    family_to_types = {
        "ISMS": [ProductType.FRAMEWORK, ProductType.OPERATIONAL],
        "PRIVACY": [ProductType.PRIVACY],
        "CLOUD": [ProductType.CLOUD],
        "AI": [ProductType.AI],
        "SEC": [ProductType.SEC],
    }
    allowed_types = family_to_types.get(family, [])
    if not allowed_types:
        return []

    q = select(Policy).where(Policy.product_type.in_(allowed_types))
    if product_type:
        q = q.where(Policy.product_type == ProductType(product_type))
    if language:
        q = q.where(Policy.language == language.lower())
    q = q.order_by(Policy.document_id)
    policies = db.execute(q).scalars().all()

    # Build set of lib_policy_ids already in this project (exclude soft-deleted)
    existing = set(
        db.execute(
            select(ProjectPolicy.lib_policy_id).where(
                ProjectPolicy.project_id == project_id,
                ProjectPolicy.lib_policy_id.isnot(None),
                ProjectPolicy.status != "removed",
            )
        ).scalars().all()
    )

    result = []
    for pol in policies:
        cg = db.get(ControlGroup, pol.control_group_id)
        result.append(LibraryPolicyItem(
            id=pol.id,
            document_id=pol.document_id,
            title=pol.title,
            policy_type=pol.policy_type.value if hasattr(pol.policy_type, "value") else pol.policy_type,
            product_type=pol.product_type.value if hasattr(pol.product_type, "value") else pol.product_type,
            control_group_code=cg.group_code if cg else "",
            control_group_name=cg.name if cg else "",
            is_stacked=cg.is_stacked if cg else False,
            already_in_project=pol.id in existing,
        ))
    return result


@router.get("/{project_id}/library/implementations", response_model=list[LibraryImplItem])
def browse_library_implementations(
    project_id: uuid.UUID,
    impl_type: str | None = Query(None),
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    p = _get_project_or_404(project_id, db, current_user)
    family = p.product_family.value if hasattr(p.product_family, "value") else p.product_family

    family_map = {
        "ISMS": ProductFamily.ISMS,
        "PRIVACY": ProductFamily.PRIVACY,
        "CLOUD": ProductFamily.CLOUD,
        "AI": ProductFamily.AI,
        "SEC": ProductFamily.SEC,
    }
    pf = family_map.get(family)
    if not pf:
        return []

    q = select(Implementation).join(
        ControlGroup, Implementation.control_group_id == ControlGroup.id
    ).where(ControlGroup.product_family == pf)
    if impl_type:
        q = q.where(Implementation.impl_type == impl_type)
    q = q.order_by(Implementation.document_id)
    impls = db.execute(q).scalars().all()

    existing = set(
        db.execute(
            select(ProjectImplementation.lib_impl_id).where(
                ProjectImplementation.project_id == project_id,
                ProjectImplementation.lib_impl_id.isnot(None),
                ProjectImplementation.status != "removed",
            )
        ).scalars().all()
    )

    result = []
    for impl in impls:
        cg = db.get(ControlGroup, impl.control_group_id)
        result.append(LibraryImplItem(
            id=impl.id,
            document_id=impl.document_id,
            title=impl.title,
            impl_type=impl.impl_type.value if hasattr(impl.impl_type, "value") else impl.impl_type,
            control_group_code=cg.group_code if cg else "",
            control_group_name=cg.name if cg else "",
            already_in_project=impl.id in existing,
        ))
    return result


# ── Project Policies ──────────────────────────────────────────────────────────

@router.get("/{project_id}/policies", response_model=list[ProjectPolicyRead])
def list_project_policies(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    rows = db.execute(
        select(ProjectPolicy)
        .where(ProjectPolicy.project_id == project_id)
        .order_by(ProjectPolicy.created_at)
    ).scalars().all()
    return [_enrich_project_policy(pp, db) for pp in rows]


@router.post("/{project_id}/policies", response_model=ProjectPolicyRead, status_code=201)
def add_project_policy(
    project_id: uuid.UUID,
    body: ProjectPolicyAdd,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = _get_project_or_404(project_id, db, current_user)
    if not body.lib_policy_id and not body.custom_content:
        raise HTTPException(status_code=422, detail="Provide lib_policy_id or custom_content")
    if body.lib_policy_id and not db.get(Policy, body.lib_policy_id):
        raise HTTPException(status_code=404, detail="Library policy not found")

    # Apply doc_vars substitution to library content if project has variables set
    custom_content = body.custom_content
    settings = project.settings or {}
    raw_dv = settings.get("doc_vars")
    doc_vars = DocVars(**raw_dv) if isinstance(raw_dv, dict) else None
    if body.lib_policy_id and (doc_vars or project.organisation.name if project.organisation else ""):
        lib_pol = db.get(Policy, body.lib_policy_id)
        if lib_pol and lib_pol.file_path:
            try:
                raw = Path(lib_pol.file_path).read_text(encoding="utf-8")
                custom_content = apply_doc_vars(raw, project.organisation.name if project.organisation else "", doc_vars)
            except OSError as e:
                logger.warning("Could not read policy file %s: %s", lib_pol.file_path, e)

    pp = ProjectPolicy(
        project_id=project_id,
        lib_policy_id=body.lib_policy_id,
        custom_content=custom_content,
        stacking_locked=body.stacking_locked,
    )
    db.add(pp)
    db.commit()
    db.refresh(pp)
    return _enrich_project_policy(pp, db)


@router.get("/{project_id}/policies/{pp_id}", response_model=ProjectPolicyRead)
def get_project_policy(
    project_id: uuid.UUID,
    pp_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pp = db.execute(
        select(ProjectPolicy).where(
            ProjectPolicy.id == pp_id,
            ProjectPolicy.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pp:
        raise HTTPException(status_code=404, detail="Project policy not found")
    result = _enrich_project_policy(pp, db)
    result.custom_content = pp.custom_content
    return result


@router.patch("/{project_id}/policies/{pp_id}", response_model=ProjectPolicyRead)
def update_project_policy(
    project_id: uuid.UUID,
    pp_id: uuid.UUID,
    body: ProjectPolicyPatch,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pp = db.execute(
        select(ProjectPolicy).where(
            ProjectPolicy.id == pp_id,
            ProjectPolicy.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pp:
        raise HTTPException(status_code=404, detail="Project policy not found")
    if pp.stacking_locked and body.custom_content is not None:
        raise HTTPException(
            status_code=409,
            detail="This policy is part of a stacked control group — structure is locked. "
                   "You can adjust individual fields but cannot replace the document content.",
        )
    if body.custom_content is not None:
        pp.custom_content = body.custom_content
        pp.is_edited = True
        pp.stale_warning = True   # IMP cross-refs may now be stale
    if body.is_edited is not None:
        pp.is_edited = body.is_edited
    if body.stale_warning is not None:
        pp.stale_warning = body.stale_warning
    if body.status is not None:
        pp.status = body.status
    db.commit()
    db.refresh(pp)
    return _enrich_project_policy(pp, db)


@router.delete("/{project_id}/policies/{pp_id}", status_code=204)
def remove_project_policy(
    project_id: uuid.UUID,
    pp_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pp = db.execute(
        select(ProjectPolicy).where(
            ProjectPolicy.id == pp_id,
            ProjectPolicy.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pp:
        raise HTTPException(status_code=404, detail="Project policy not found")
    db.delete(pp)
    db.commit()


# ── Project Implementations ───────────────────────────────────────────────────

@router.get("/{project_id}/implementations", response_model=list[ProjectImplRead])
def list_project_implementations(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    rows = db.execute(
        select(ProjectImplementation)
        .where(ProjectImplementation.project_id == project_id)
        .order_by(ProjectImplementation.created_at)
    ).scalars().all()
    return [_enrich_project_impl(pi, db) for pi in rows]


@router.post("/{project_id}/implementations", response_model=ProjectImplRead, status_code=201)
def add_project_implementation(
    project_id: uuid.UUID,
    body: ProjectImplAdd,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = _get_project_or_404(project_id, db, current_user)
    if not body.lib_impl_id and not body.custom_content:
        raise HTTPException(status_code=422, detail="Provide lib_impl_id or custom_content")
    if body.lib_impl_id and not db.get(Implementation, body.lib_impl_id):
        raise HTTPException(status_code=404, detail="Library implementation not found")

    # Apply doc_vars substitution to library content
    custom_content = body.custom_content
    settings = project.settings or {}
    raw_dv = settings.get("doc_vars")
    doc_vars = DocVars(**raw_dv) if isinstance(raw_dv, dict) else None
    if body.lib_impl_id and (doc_vars or project.organisation.name if project.organisation else ""):
        lib_impl = db.get(Implementation, body.lib_impl_id)
        if lib_impl and lib_impl.file_path:
            try:
                raw = Path(lib_impl.file_path).read_text(encoding="utf-8")
                custom_content = apply_doc_vars(raw, project.organisation.name if project.organisation else "", doc_vars)
            except OSError as e:
                logger.warning("Could not read impl file %s: %s", lib_impl.file_path, e)

    pi = ProjectImplementation(
        project_id=project_id,
        lib_impl_id=body.lib_impl_id,
        custom_content=custom_content,
    )
    db.add(pi)
    db.commit()
    db.refresh(pi)
    return _enrich_project_impl(pi, db)


@router.get("/{project_id}/implementations/{pi_id}", response_model=ProjectImplRead)
def get_project_implementation(
    project_id: uuid.UUID,
    pi_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pi = db.execute(
        select(ProjectImplementation).where(
            ProjectImplementation.id == pi_id,
            ProjectImplementation.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pi:
        raise HTTPException(status_code=404, detail="Project implementation not found")
    result = _enrich_project_impl(pi, db)
    result.custom_content = pi.custom_content
    return result


@router.patch("/{project_id}/implementations/{pi_id}", response_model=ProjectImplRead)
def update_project_implementation(
    project_id: uuid.UUID,
    pi_id: uuid.UUID,
    body: ProjectImplPatch,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pi = db.execute(
        select(ProjectImplementation).where(
            ProjectImplementation.id == pi_id,
            ProjectImplementation.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pi:
        raise HTTPException(status_code=404, detail="Project implementation not found")
    if body.custom_content is not None:
        pi.custom_content = body.custom_content
        pi.is_edited = True
    if body.is_edited is not None:
        pi.is_edited = body.is_edited
    if body.stale_warning is not None:
        pi.stale_warning = body.stale_warning
    if body.status is not None:
        pi.status = body.status
    db.commit()
    db.refresh(pi)
    return _enrich_project_impl(pi, db)


@router.delete("/{project_id}/implementations/{pi_id}", status_code=204)
def remove_project_implementation(
    project_id: uuid.UUID,
    pi_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pi = db.execute(
        select(ProjectImplementation).where(
            ProjectImplementation.id == pi_id,
            ProjectImplementation.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pi:
        raise HTTPException(status_code=404, detail="Project implementation not found")
    db.delete(pi)
    db.commit()


# ── Project Checklists ────────────────────────────────────────────────────────

def _build_checklist_read(pc: ProjectChecklist, db: DBSession, include_items: bool = False) -> ProjectChecklistRead:
    """Build ProjectChecklistRead from a ProjectChecklist row."""
    from src.schemas.projects import ProjectChecklistItem
    cg = db.get(ControlGroup, pc.control_group_id)
    # Count items from cloned_content (if cloned) or from Assessment items
    cloned = pc.cloned_content or []
    overrides: dict = pc.applicability_overrides or {}

    # Find the library assessment title
    title = None
    if pc.lib_checklist_id:
        asmnt = db.get(Assessment, pc.lib_checklist_id)
        if asmnt:
            title = asmnt.workbook_name

    items_out = None
    if include_items:
        items_out = []
        for raw in cloned:
            item_id = str(raw.get("id", ""))
            ov = overrides.get(item_id, {})
            items_out.append(ProjectChecklistItem(
                id=item_id,
                row_number=raw.get("row_number", 0),
                item_text=raw.get("item_text"),
                na=ov.get("na", False),
                justification=ov.get("justification"),
            ))

    na_count = sum(1 for ov in overrides.values() if ov.get("na"))

    return ProjectChecklistRead(
        id=pc.id,
        project_id=pc.project_id,
        control_group_id=pc.control_group_id,
        control_group_code=cg.group_code if cg else "",
        control_group_name=cg.name if cg else "",
        product_type=pc.product_type,
        lib_checklist_id=pc.lib_checklist_id,
        title=title,
        item_count=len(cloned),
        na_count=na_count,
        items=items_out,
        created_at=pc.created_at,
    )


@router.get("/{project_id}/library/checklists", response_model=list[LibraryChecklistItem])
def browse_library_checklists(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return library SCR checklists (assessment_type=checklist) for this project's product family."""
    from src.database.enums import AssessmentType, ProductType
    p = _get_project_or_404(project_id, db, current_user)
    family = p.product_family.value if hasattr(p.product_family, "value") else p.product_family

    family_to_types = {
        "ISMS": [ProductType.FRAMEWORK, ProductType.OPERATIONAL],
        "PRIVACY": [ProductType.PRIVACY],
        "CLOUD": [ProductType.CLOUD],
        "AI": [ProductType.AI],
        "SEC": [ProductType.SEC],
    }
    allowed_types = family_to_types.get(family, [])
    if not allowed_types:
        return []

    q = (
        select(Assessment)
        .where(
            Assessment.assessment_type == AssessmentType.CHECKLIST,
            Assessment.product_type.in_(allowed_types),
        )
        .order_by(Assessment.document_id)
    )
    assessments = db.execute(q).scalars().all()

    # Which control_group_ids are already cloned in this project
    existing_cg_ids = set(
        db.execute(
            select(ProjectChecklist.control_group_id).where(
                ProjectChecklist.project_id == project_id,
            )
        ).scalars().all()
    )

    result = []
    for asmnt in assessments:
        cg = db.get(ControlGroup, asmnt.control_group_id)
        item_count = db.execute(
            select(AssessmentItem).where(AssessmentItem.assessment_id == asmnt.id)
        ).scalars().all()
        result.append(LibraryChecklistItem(
            id=asmnt.id,
            document_id=asmnt.document_id,
            title=asmnt.workbook_name,
            product_type=asmnt.product_type.value if hasattr(asmnt.product_type, "value") else asmnt.product_type,
            control_group_code=cg.group_code if cg else "",
            control_group_name=cg.name if cg else "",
            item_count=len(item_count),
            already_in_project=asmnt.control_group_id in existing_cg_ids,
        ))
    return result


@router.get("/{project_id}/checklists", response_model=list[ProjectChecklistRead])
def list_project_checklists(
    project_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    rows = db.execute(
        select(ProjectChecklist)
        .where(ProjectChecklist.project_id == project_id)
        .order_by(ProjectChecklist.created_at)
    ).scalars().all()
    return [_build_checklist_read(pc, db, include_items=False) for pc in rows]


@router.post("/{project_id}/checklists", response_model=ProjectChecklistRead, status_code=201)
def add_project_checklist(
    project_id: uuid.UUID,
    body: ProjectChecklistAdd,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Clone a library SCR (assessment) into the project, copying all items for N/A toggling."""
    _get_project_or_404(project_id, db, current_user)

    asmnt = db.get(Assessment, body.lib_checklist_id)
    if not asmnt:
        raise HTTPException(status_code=404, detail="Library checklist not found")

    # Prevent duplicates (unique constraint: project_id + control_group_id + product_type)
    existing = db.execute(
        select(ProjectChecklist).where(
            ProjectChecklist.project_id == project_id,
            ProjectChecklist.control_group_id == asmnt.control_group_id,
            ProjectChecklist.product_type == asmnt.product_type.value,
        )
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail="Checklist already in project")

    # Clone items from assessment_items
    items = db.execute(
        select(AssessmentItem)
        .where(AssessmentItem.assessment_id == asmnt.id)
        .order_by(AssessmentItem.row_number)
    ).scalars().all()

    cloned_content = [
        {"id": str(item.id), "row_number": item.row_number, "item_text": item.item_text}
        for item in items
    ]

    pt_val = asmnt.product_type.value if hasattr(asmnt.product_type, "value") else str(asmnt.product_type)
    pc = ProjectChecklist(
        project_id=project_id,
        control_group_id=asmnt.control_group_id,
        product_type=pt_val,
        lib_checklist_id=asmnt.id,
        clone_source=pt_val,
        cloned_content=cloned_content,
        applicability_overrides={},
    )
    db.add(pc)
    db.commit()
    db.refresh(pc)
    return _build_checklist_read(pc, db, include_items=False)


@router.get("/{project_id}/checklists/{cid}", response_model=ProjectChecklistRead)
def get_project_checklist(
    project_id: uuid.UUID,
    cid: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pc = db.execute(
        select(ProjectChecklist).where(
            ProjectChecklist.id == cid,
            ProjectChecklist.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pc:
        raise HTTPException(status_code=404, detail="Project checklist not found")
    return _build_checklist_read(pc, db, include_items=True)


@router.patch("/{project_id}/checklists/{cid}/items", response_model=ProjectChecklistRead)
def patch_checklist_item(
    project_id: uuid.UUID,
    cid: uuid.UUID,
    body: ProjectChecklistItemPatch,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Toggle N/A on a single checklist item."""
    _get_project_or_404(project_id, db, current_user)
    pc = db.execute(
        select(ProjectChecklist).where(
            ProjectChecklist.id == cid,
            ProjectChecklist.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pc:
        raise HTTPException(status_code=404, detail="Project checklist not found")

    overrides = dict(pc.applicability_overrides or {})
    if body.na:
        overrides[body.item_id] = {"na": True, "justification": body.justification}
    else:
        overrides.pop(body.item_id, None)
    pc.applicability_overrides = overrides
    db.commit()
    db.refresh(pc)
    return _build_checklist_read(pc, db, include_items=True)


@router.delete("/{project_id}/checklists/{cid}", status_code=204)
def remove_project_checklist(
    project_id: uuid.UUID,
    cid: uuid.UUID,
    db: DBSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _get_project_or_404(project_id, db, current_user)
    pc = db.execute(
        select(ProjectChecklist).where(
            ProjectChecklist.id == cid,
            ProjectChecklist.project_id == project_id,
        )
    ).scalar_one_or_none()
    if not pc:
        raise HTTPException(status_code=404, detail="Project checklist not found")
    db.delete(pc)
    db.commit()
