import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, require_admin, require_content_editable
from src.database.enums import EditSource
from src.database.session import get_db
from src.domain.content import Policy
from src.domain.users import User
from src.schemas.policies import PolicyListRead, PolicyStateUpdate
from src.services.audit_service import log_event
from src.services.policy_service import list_policies

router = APIRouter(prefix="/policies", tags=["policies"])


@router.delete("/{policy_id}", status_code=204)
def delete_policy(
    policy_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(require_admin),
):
    """Delete an external document. Only external product_type policies may be deleted this way."""
    from src.database.enums import ProductType
    policy = db.get(Policy, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    if policy.product_type != ProductType.EXTERNAL:
        raise HTTPException(status_code=403, detail="Only external documents can be deleted via the UI")
    db.delete(policy)
    db.commit()


@router.get("/", response_model=list[PolicyListRead])
def list_all_policies(
    product: str | None = None,
    policy_type: str | None = None,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    return list_policies(db, product=product, policy_type=policy_type)


@router.patch("/{policy_id}/state")
def set_policy_state(
    policy_id: uuid.UUID,
    body: PolicyStateUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(require_content_editable),
):
    """Transition a policy's approval state (draft → review → approved → published)."""
    policy = db.get(Policy, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    old_state = policy.content_state
    policy.content_state = body.state
    policy.edit_source = EditSource.WEBUI
    log_event(
        db,
        event_type="policy.state.changed",
        category="workflow",
        severity="info",
        user_id=_user.id,
        actor_email=_user.email,
        target_type="policy",
        target_id=policy_id,
        description=f"Policy '{policy.document_id}' state changed from {old_state.value if old_state else 'none'} to {body.state.value}",
        metadata={
            "old_state": old_state.value if old_state else None,
            "new_state": body.state.value,
            "edit_source": EditSource.WEBUI.value,
            "document_id": policy.document_id,
        },
    )
    db.commit()
    return {"id": str(policy_id), "content_state": body.state.value, "edit_source": EditSource.WEBUI.value}


@router.get("/{policy_id}/content")
def get_policy_content(
    policy_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    policy = db.get(Policy, policy_id)
    if not policy:
        raise HTTPException(status_code=404, detail="Policy not found")
    path = Path(policy.file_path)
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found on filesystem")
    return {
        "document_id": policy.document_id,
        "title": policy.title,
        "policy_type": policy.policy_type.value if hasattr(policy.policy_type, "value") else str(policy.policy_type),
        "content": path.read_text(encoding="utf-8"),
    }
