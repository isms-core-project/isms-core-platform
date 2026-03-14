import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import ComplianceStatus, ContentState, EditSource, ImplType, PolicyType, ProductType


class Policy(TimestampMixin, Base):
    __tablename__ = "policies"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    product_type: Mapped[ProductType] = mapped_column(
        SAEnum(ProductType, name="product_type", create_type=False), nullable=False
    )
    policy_type: Mapped[PolicyType] = mapped_column(
        SAEnum(PolicyType, name="policy_type", create_type=False), nullable=False
    )
    document_id: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    content_hash: Mapped[str | None] = mapped_column(String(64))
    word_count: Mapped[int | None] = mapped_column(Integer)
    requirements_count: Mapped[int | None] = mapped_column(
        Integer, server_default="0"
    )
    last_parsed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    language: Mapped[str] = mapped_column(String(5), nullable=False, server_default="en")
    source_label: Mapped[str | None] = mapped_column(String(200), nullable=True)
    content_state: Mapped[ContentState] = mapped_column(
        SAEnum(ContentState, name="content_state", create_type=False),
        nullable=False,
        server_default="published",
    )
    edit_source: Mapped[EditSource] = mapped_column(
        SAEnum(EditSource, name="edit_source", create_type=False),
        nullable=False,
        server_default="import",
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    control_group: Mapped["ControlGroup"] = relationship(back_populates="policies")
    requirements: Mapped[list["Requirement"]] = relationship(
        back_populates="policy", cascade="all, delete-orphan"
    )


class Requirement(TimestampMixin, Base):
    __tablename__ = "requirements"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    policy_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("policies.id", ondelete="CASCADE"),
        nullable=False,
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    requirement_text: Mapped[str] = mapped_column(Text, nullable=False)
    section_heading: Mapped[str | None] = mapped_column(String(200))
    # CHECK (requirement_type IN ('mandatory', 'recommended'))
    requirement_type: Mapped[str] = mapped_column(
        String(15), nullable=False, server_default="mandatory"
    )
    domain_area: Mapped[str | None] = mapped_column(String(100))
    sort_order: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0"
    )
    compliance_status: Mapped[ComplianceStatus] = mapped_column(
        SAEnum(ComplianceStatus, name="compliance_status", create_type=False),
        nullable=False,
        server_default="not_assessed",
    )
    evidence_count: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0"
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    policy: Mapped["Policy"] = relationship(back_populates="requirements")
    control_group: Mapped["ControlGroup"] = relationship(back_populates="requirements")


class Implementation(TimestampMixin, Base):
    __tablename__ = "implementations"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    control_group_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        nullable=False,
    )
    impl_type: Mapped[ImplType] = mapped_column(
        SAEnum(ImplType, name="impl_type", create_type=False), nullable=False
    )
    document_id: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    file_path: Mapped[str] = mapped_column(Text, nullable=False)
    content_hash: Mapped[str | None] = mapped_column(String(64))
    word_count: Mapped[int | None] = mapped_column(Integer)
    last_parsed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    language: Mapped[str] = mapped_column(String(5), nullable=False, server_default="en")
    content_state: Mapped[ContentState] = mapped_column(
        SAEnum(ContentState, name="content_state", create_type=False),
        nullable=False,
        server_default="published",
    )
    edit_source: Mapped[EditSource] = mapped_column(
        SAEnum(EditSource, name="edit_source", create_type=False),
        nullable=False,
        server_default="import",
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    control_group: Mapped["ControlGroup"] = relationship(
        back_populates="implementations"
    )


class GeneratorDefinition(TimestampMixin, Base):
    """Structural metadata extracted from each generator script (Phase 7.1).

    One row per generator file (one per assessment domain / workbook).
    Stores sheet definitions, stacked control refs, domain info.
    Used by Phase 7.3 WebUI form renderer and Phase 7.4 script regeneration.
    """

    __tablename__ = "generator_definitions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    # Unique key — ISMS-IMP-A.8.17.1, ISMS-IMP-A.5.1-2-6.1-2.S1, etc.
    document_id: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    workbook_name: Mapped[str] = mapped_column(String(200), nullable=False)
    # CONTROL_ID constant from the generator (e.g. "A.8.17", "A.5.1-2-6.1-2")
    control_id: Mapped[str] = mapped_column(String(80), nullable=False)
    control_name: Mapped[str] = mapped_column(String(300), nullable=False)
    # Parsed group code (matches control_groups.group_code where possible)
    group_code: Mapped[str] = mapped_column(String(80), nullable=False)
    # FK resolved at import time — nullable if group_code not in DB
    control_group_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="SET NULL"),
        nullable=True,
    )
    domain_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    domain_total: Mapped[int | None] = mapped_column(Integer, nullable=True)
    is_stacked: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    # ["A.5.1", "A.5.2", ...] for stacked generators; null for simple ones
    stacked_control_ids: Mapped[list | None] = mapped_column(JSONB, nullable=True)
    # [{"name": "Time Sources", "type": "input"}, ...]
    sheets: Mapped[list] = mapped_column(JSONB, nullable=False, server_default="[]")
    sheet_count: Mapped[int] = mapped_column(Integer, nullable=False, server_default="0")
    # "docstring" or "code" — how sheet names were extracted
    sheet_source: Mapped[str | None] = mapped_column(String(20), nullable=True)
    # Product: framework | operational | privacy | cloud
    product_type: Mapped[str] = mapped_column(
        String(20), nullable=False, server_default="framework"
    )
    # Relative path from product root (FRAMEWORK_PATH / OPERATIONAL_PATH / etc.)
    source_file: Mapped[str | None] = mapped_column(Text, nullable=True)
    parsed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    # When True, the importer will not overwrite this record on re-import
    user_override: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default="false")
    # Full workbook schema extracted from produced .xlsx (Phase 7.5)
    # [{sheet_name, sheet_type, position, header_row, data_start_row, freeze_panes,
    #   hide_gridlines, status_column_index, status_column_letter,
    #   columns: [{index, letter, header, header_raw, width, dv_values, required, is_status_col}]}]
    sheet_schemas: Mapped[list] = mapped_column(JSONB, nullable=False, server_default="[]")

    # Relationship
    control_group: Mapped["ControlGroup | None"] = relationship()
