"""Organisation API — Phase 11 (multi-tenant)."""

import logging
import re
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_admin, require_role
from src.database.enums import UserRole
from src.database.session import get_db
from src.domain.organisations import Organisation
from src.domain.users import User
from src.schemas.organisation import OrganisationCreate, OrganisationRead, OrganisationUpdate

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/organisation", tags=["organisation"])

_require_super_admin = require_role(UserRole.SUPER_ADMIN)


def _get_org_by_id(org_id: uuid.UUID, db: DBSession) -> Organisation:
    """Return the organisation record for the given ID, or 404."""
    org = db.get(Organisation, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organisation not found")
    return org


@router.get("/", response_model=OrganisationRead)
def get_organisation(
    db: DBSession = Depends(get_db),
    org_id: uuid.UUID = Depends(get_org_context),
):
    """Return current organisation settings including governance_mode."""
    return OrganisationRead.model_validate(_get_org_by_id(org_id, db))


@router.patch("/", response_model=OrganisationRead)
def update_organisation(
    body: OrganisationUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(require_admin),
    org_id: uuid.UUID = Depends(get_org_context),
):
    """Update organisation settings (name, governance_mode, description, settings)."""
    org = _get_org_by_id(org_id, db)

    if body.name is not None:
        org.name = body.name
    if body.governance_mode is not None:
        logger.info(
            "Governance mode changed: %s → %s",
            org.governance_mode,
            body.governance_mode,
        )
        org.governance_mode = body.governance_mode
    if body.description is not None:
        org.description = body.description
    if body.settings is not None:
        org.settings = body.settings

    db.commit()
    db.refresh(org)
    return OrganisationRead.model_validate(org)


# ── Super-admin endpoints ──────────────────────────────────────────────────────

@router.get("/all", response_model=list[OrganisationRead])
def list_all_organisations(
    db: DBSession = Depends(get_db),
    _user: User = Depends(_require_super_admin),
):
    """List all organisations on the platform (super_admin only)."""
    orgs = db.execute(select(Organisation).order_by(Organisation.name)).scalars().all()
    return [OrganisationRead.model_validate(o) for o in orgs]


@router.post("/", response_model=OrganisationRead, status_code=201)
def create_organisation(
    body: OrganisationCreate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(_require_super_admin),
):
    """Create a new organisation / tenant (super_admin only)."""
    slug = body.slug.strip().lower()
    if not re.match(r"^[a-z0-9-]+$", slug):
        raise HTTPException(status_code=422, detail="Slug must be lowercase letters, numbers, and hyphens only.")

    existing = db.execute(select(Organisation).where(Organisation.slug == slug)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail=f"Slug '{slug}' is already in use.")

    org = Organisation(
        name=body.name.strip(),
        slug=slug,
        description=body.description,
        governance_mode=body.governance_mode,
        privacy_role=body.privacy_role,
    )
    db.add(org)
    db.commit()
    db.refresh(org)
    logger.info("Created organisation: %s (%s)", org.name, org.slug)
    return OrganisationRead.model_validate(org)
