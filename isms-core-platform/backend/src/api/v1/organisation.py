"""Organisation API — Phase 11 (multi-tenant)."""

import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, get_org_context, require_admin
from src.database.session import get_db
from src.domain.organisations import Organisation
from src.domain.users import User
from src.schemas.organisation import OrganisationRead, OrganisationUpdate

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/organisation", tags=["organisation"])


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
