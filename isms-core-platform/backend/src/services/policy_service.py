from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.domain.content import Policy
from src.domain.control_groups import ControlGroup
from src.schemas.policies import PolicyListRead


def list_policies(
    db: DBSession,
    product: str | None = None,
    policy_type: str | None = None,
) -> list[PolicyListRead]:
    stmt = (
        select(Policy, ControlGroup.group_code, ControlGroup.name)
        .join(ControlGroup, Policy.control_group_id == ControlGroup.id)
        .order_by(ControlGroup.group_code, Policy.product_type, Policy.document_id)
    )
    if product:
        stmt = stmt.where(Policy.product_type == product)
    if policy_type:
        stmt = stmt.where(Policy.policy_type == policy_type)
    rows = db.execute(stmt).all()
    result = []
    for policy, group_code, group_name in rows:
        d = {
            "id": policy.id,
            "control_group_id": policy.control_group_id,
            "group_code": group_code,
            "group_name": group_name,
            "product_type": policy.product_type.value if hasattr(policy.product_type, "value") else str(policy.product_type),
            "policy_type": policy.policy_type.value if hasattr(policy.policy_type, "value") else str(policy.policy_type),
            "document_id": policy.document_id,
            "title": policy.title,
            "word_count": policy.word_count,
            "requirements_count": policy.requirements_count,
            "last_parsed": policy.last_parsed,
            "content_state": policy.content_state,
        }
        result.append(PolicyListRead.model_validate(d))
    return result
