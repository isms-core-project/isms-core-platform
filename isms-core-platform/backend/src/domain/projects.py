"""Projects domain models — Library/Project workspace architecture."""

import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import ProductFamily, ProjectStatus


class Project(TimestampMixin, Base):
    """A user's compliance workspace for a specific product family (ISMS/PRIVACY/CLOUD).

    One user can own multiple projects (e.g. "Acme Corp ISMS", "Client X ISMS").
    A project scopes all operational data: assessments, gaps, evidence, checklists.
    Library content (policies, implementations) is referenced from the project via
    project_policies and project_implementations — either as-is or edited copies.
    """

    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    org_name: Mapped[str] = mapped_column(String(255), nullable=False)
    product_family: Mapped[ProductFamily] = mapped_column(
        SAEnum(ProductFamily, name="productfamily", create_type=False), nullable=False
    )
    description: Mapped[str | None] = mapped_column(Text)
    owner_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    status: Mapped[ProjectStatus] = mapped_column(
        SAEnum(ProjectStatus, name="project_status", create_type=False),
        nullable=False,
        server_default="active",
    )
    settings: Mapped[dict] = mapped_column(JSONB, default=dict, server_default="{}")

    # Relationships
    owner: Mapped["User | None"] = relationship()
    policies: Mapped[list["ProjectPolicy"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )
    implementations: Mapped[list["ProjectImplementation"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )
    checklists: Mapped[list["ProjectChecklist"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class ProjectPolicy(TimestampMixin, Base):
    """A policy entry in a project — either a Library reference or a custom upload.

    lib_policy_id is null  → custom document (user import or created from scratch)
    lib_policy_id is set   → sourced from Library
    is_edited = True       → Library source was modified; stale_warning may apply
    stacking_locked = True → stacked control group — structure cannot be changed
    stale_warning = True   → IMP cross-references may no longer be accurate
    """

    __tablename__ = "project_policies"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    lib_policy_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("policies.id", ondelete="SET NULL"),
        nullable=True,
    )
    # Markdown content — null means use library source as-is
    custom_content: Mapped[str | None] = mapped_column(Text)
    is_edited: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    # True when sourced from a stacked control group — structure is locked
    stacking_locked: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    # True when custom_content was edited and linked IMPs may have stale cross-refs
    stale_warning: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="active"
    )

    # Relationships
    project: Mapped["Project"] = relationship(back_populates="policies")
    lib_policy: Mapped["Policy | None"] = relationship()


class ProjectImplementation(TimestampMixin, Base):
    """An implementation guide entry in a project — Library reference or custom.

    stale_warning = True when the linked ProjectPolicy was edited and this IMP
    may contain section references that no longer match the policy content.
    """

    __tablename__ = "project_implementations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    lib_impl_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("implementations.id", ondelete="SET NULL"),
        nullable=True,
    )
    custom_content: Mapped[str | None] = mapped_column(Text)
    is_edited: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    stale_warning: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    status: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="active"
    )

    # Relationships
    project: Mapped["Project"] = relationship(back_populates="implementations")
    lib_impl: Mapped["Implementation | None"] = relationship()


class ProjectChecklist(TimestampMixin, Base):
    """SCR checklist for a control group within a project.

    Always generated from the Library (canonical SCR content).
    applicability_overrides stores item-level N/A toggles + justifications:
      { "<item_id>": { "na": true, "justification": "Not applicable — SaaS only" } }

    For OP/PRIV/CLD: clone_source is set and cloned_content holds the adjusted
    checklist items so users can toggle N/A per item without modifying the Library.

    For FW: clone_source is null — a warning banner explains N/As are expected.
    """

    __tablename__ = "project_checklists"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    project_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    # framework | operational | privacy | cloud
    product_type: Mapped[str] = mapped_column(String(20), nullable=False)
    # Item-level N/A overrides: {item_id: {na: bool, justification: str}}
    applicability_overrides: Mapped[dict] = mapped_column(
        JSONB, default=dict, server_default="{}"
    )
    # Reference to the library Assessment (assessment_type='checklist') used as source
    lib_checklist_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("assessments.id", ondelete="SET NULL"),
        nullable=True,
    )
    # null = library-based (FW), 'op'/'priv'/'cld' = cloned for adjustment
    clone_source: Mapped[str | None] = mapped_column(String(10), nullable=True)
    # Full cloned checklist items for OP/PRIV/CLD adjustable SCRs
    cloned_content: Mapped[list | None] = mapped_column(JSONB, nullable=True)

    # Relationships
    project: Mapped["Project"] = relationship(back_populates="checklists")
    control_group: Mapped["ControlGroup"] = relationship()
