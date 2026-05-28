import uuid
from datetime import datetime

from pydantic import BaseModel


# ── Document variables ────────────────────────────────────────────────────────
# Stored in project.settings["doc_vars"] — substituted into policy/IMP content
# when items are added to the project.

class DocVars(BaseModel):
    """Project-level document header variables.

    When a policy or IMP is added to the project these values replace the
    corresponding `[Placeholder]` tokens in the library document content.
    The substituted content is stored in project_policies.custom_content so
    the document is ready to use without further editing.
    """
    ciso_name: str | None = None       # replaces [CISO name], [CISO]
    ceo_name: str | None = None        # replaces [CEO Name] in letter/signature templates
    dpo_name: str | None = None        # replaces [DPO name], [DPO Name]
    legal_entity: str | None = None    # replaces [Legal Entity Name], [Entity Name]
    effective_date: str | None = None  # replaces [Date to be set], [Date]  — ISO date string
    review_date: str | None = None     # replaces [Effective Date + 12 months] — Next Review Date
    classification: str | None = None  # replaces [Classification]  — default: Internal


# Canonical substitution map: doc_var key → list of tokens to replace
DOC_VAR_TOKENS: dict[str, list[str]] = {
    # org_name comes from Project.org_name directly — not a DocVars field
    "org_name": [
        "[Organisation]", "[Organisation Name]", "[ORGANIZATION NAME]",
        "[Org]", "[Your Organisation]", "[Our Organisation]",
    ],
    "ciso_name": ["[CISO name]", "[CISO]"],
    "ceo_name":  ["[CEO Name]"],
    "dpo_name":  ["[DPO name]", "[DPO Name]"],
    "legal_entity": ["[Legal Entity Name]", "[Entity Name]"],
    "effective_date": ["[Date to be set]", "[Date]"],
    "review_date": ["[Effective Date + 12 months]"],
    "classification": ["[Classification]"],
}


import re as _re

_ISO_DATE_RE = _re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def _fmt_date(val: str | None) -> str | None:
    """Convert ISO YYYY-MM-DD → CH format DD.MM.YYYY. Other formats pass through unchanged."""
    if not val:
        return val
    m = _ISO_DATE_RE.match(val.strip())
    if m:
        return f"{m.group(3)}.{m.group(2)}.{m.group(1)}"
    return val


def apply_doc_vars(content: str, org_name: str, doc_vars: DocVars | None) -> str:
    """Substitute [Placeholder] tokens in document content using project variables.

    Date fields (effective_date, review_date) stored as ISO YYYY-MM-DD are
    automatically formatted as DD.MM.YYYY (CH/European format) before substitution.
    """
    if not content:
        return content
    result = content
    values: dict[str, str | None] = {
        "org_name": org_name,
        "ciso_name": doc_vars.ciso_name if doc_vars else None,
        "ceo_name": doc_vars.ceo_name if doc_vars else None,
        "dpo_name": doc_vars.dpo_name if doc_vars else None,
        "legal_entity": doc_vars.legal_entity if doc_vars else None,
        "effective_date": _fmt_date(doc_vars.effective_date) if doc_vars else None,
        "review_date": _fmt_date(doc_vars.review_date) if doc_vars else None,
        "classification": doc_vars.classification if doc_vars else None,
    }
    for key, tokens in DOC_VAR_TOKENS.items():
        val = values.get(key)
        if val:
            for token in tokens:
                result = result.replace(token, val)
    return result


# ── Project ──────────────────────────────────────────────────────────────────

class ProjectCreate(BaseModel):
    name: str
    product_family: str          # ISMS | PRIVACY | CLOUD | SEC
    project_subtype: str | None = None  # fw | op (ISMS only)
    description: str | None = None
    doc_vars: DocVars | None = None   # pre-filled document header variables
    organisation_id: uuid.UUID | None = None  # super_admin only — override target org


class ProjectPatch(BaseModel):
    name: str | None = None
    description: str | None = None
    status: str | None = None    # draft | active | inactive | archived
    project_subtype: str | None = None
    doc_vars: DocVars | None = None


class ProjectRead(BaseModel):
    id: uuid.UUID
    name: str
    organisation_id: uuid.UUID
    organisation_name: str | None = None   # populated from organisation relationship
    product_family: str
    project_subtype: str | None = None
    description: str | None
    status: str
    owner_id: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
    doc_vars: DocVars | None = None
    # Derived counts — populated by the router
    policy_count: int = 0
    implementation_count: int = 0
    checklist_count: int = 0
    assessment_count: int = 0

    model_config = {"from_attributes": True}


# ── Project Policy ────────────────────────────────────────────────────────────

class ProjectPolicyAdd(BaseModel):
    """Add a Library policy or a custom document to the project."""
    lib_policy_id: uuid.UUID | None = None   # null → custom import
    custom_content: str | None = None         # markdown, used when lib_policy_id is null
    stacking_locked: bool = False


class ProjectPolicyPatch(BaseModel):
    custom_content: str | None = None
    is_edited: bool | None = None
    stale_warning: bool | None = None
    status: str | None = None


class ProjectPolicyRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    lib_policy_id: uuid.UUID | None
    # Resolved from lib_policy if not custom
    document_id: str | None = None
    title: str | None = None
    policy_type: str | None = None
    product_type: str | None = None
    control_group_code: str | None = None
    is_edited: bool
    stacking_locked: bool
    stale_warning: bool
    status: str
    created_at: datetime
    # Only populated in single-item GET, not the list
    custom_content: str | None = None

    model_config = {"from_attributes": True}


# ── Project Implementation ────────────────────────────────────────────────────

class ProjectImplAdd(BaseModel):
    lib_impl_id: uuid.UUID | None = None
    custom_content: str | None = None


class ProjectImplPatch(BaseModel):
    custom_content: str | None = None
    is_edited: bool | None = None
    stale_warning: bool | None = None
    status: str | None = None


class ProjectImplRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    lib_impl_id: uuid.UUID | None
    document_id: str | None = None
    title: str | None = None
    impl_type: str | None = None
    control_group_code: str | None = None
    is_edited: bool
    stale_warning: bool
    status: str
    created_at: datetime
    # Only populated in single-item GET, not the list
    custom_content: str | None = None

    model_config = {"from_attributes": True}


# ── Project Checklist ────────────────────────────────────────────────────────

class ProjectChecklistItem(BaseModel):
    """A single item from a cloned SCR checklist."""
    id: str           # str(AssessmentItem.id)
    row_number: int
    item_text: str | None
    na: bool = False
    justification: str | None = None


class ProjectChecklistAdd(BaseModel):
    lib_checklist_id: uuid.UUID   # assessments.id where assessment_type=checklist


class ProjectChecklistItemPatch(BaseModel):
    item_id: str
    na: bool
    justification: str | None = None


class ProjectChecklistRead(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    control_group_id: uuid.UUID
    control_group_code: str
    control_group_name: str
    product_type: str
    lib_checklist_id: uuid.UUID | None
    title: str | None = None
    item_count: int = 0
    na_count: int = 0
    # Only populated in single-item GET
    items: list[ProjectChecklistItem] | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


# ── Library list items (read-only, for the browser) ──────────────────────────

class LibraryPolicyItem(BaseModel):
    id: uuid.UUID
    document_id: str
    title: str
    policy_type: str
    product_type: str
    control_group_code: str
    control_group_name: str
    is_stacked: bool = False
    already_in_project: bool = False

    model_config = {"from_attributes": True}


class LibraryImplItem(BaseModel):
    id: uuid.UUID
    document_id: str
    title: str
    impl_type: str
    control_group_code: str
    control_group_name: str
    already_in_project: bool = False

    model_config = {"from_attributes": True}


class LibraryChecklistItem(BaseModel):
    """A library SCR (Assessment with assessment_type='checklist') available to clone."""
    id: uuid.UUID
    document_id: str
    title: str
    product_type: str
    control_group_code: str
    control_group_name: str
    item_count: int = 0
    already_in_project: bool = False

    model_config = {"from_attributes": True}
