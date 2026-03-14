import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import MappingType


class Framework(TimestampMixin, Base):
    __tablename__ = "frameworks"

    # Deterministic UUID5 from bundle — no default
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    version: Mapped[str | None] = mapped_column(String(20))
    publisher: Mapped[str | None] = mapped_column(String(100))
    source_url: Mapped[str | None] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text)
    jurisdiction: Mapped[str | None] = mapped_column(String(10))
    controls_count: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0"
    )
    loaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    bundle_hash: Mapped[str | None] = mapped_column(String(64))
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    controls: Mapped[list["FrameworkControl"]] = relationship(
        back_populates="framework", cascade="all, delete-orphan"
    )


class FrameworkControl(TimestampMixin, Base):
    __tablename__ = "framework_controls"
    __table_args__ = (
        UniqueConstraint("framework_id", "control_id", name="framework_controls_framework_id_control_id_key"),
    )

    # Deterministic UUID5 from bundle — no default
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    framework_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("frameworks.id", ondelete="CASCADE"),
        nullable=False,
    )
    control_id: Mapped[str] = mapped_column(String(50), nullable=False)
    parent_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("framework_controls.id", ondelete="SET NULL"),
    )
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    control_type: Mapped[list | None] = mapped_column(
        ARRAY(String(50)), server_default="{}"
    )
    security_properties: Mapped[list | None] = mapped_column(
        ARRAY(String(50)), server_default="{}"
    )
    level: Mapped[int] = mapped_column(Integer, nullable=False, server_default="1")
    sort_order: Mapped[int] = mapped_column(
        Integer, nullable=False, server_default="0"
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    framework: Mapped["Framework"] = relationship(back_populates="controls")
    parent: Mapped["FrameworkControl | None"] = relationship(
        remote_side=[id], foreign_keys=[parent_id]
    )
    children: Mapped[list["FrameworkControl"]] = relationship(
        foreign_keys=[parent_id]
    )
    source_mappings: Mapped[list["CrossFrameworkMapping"]] = relationship(
        foreign_keys="CrossFrameworkMapping.source_control_id",
        back_populates="source_control",
    )
    target_mappings: Mapped[list["CrossFrameworkMapping"]] = relationship(
        foreign_keys="CrossFrameworkMapping.target_control_id",
        back_populates="target_control",
    )


class CrossFrameworkMapping(Base):
    __tablename__ = "cross_framework_mappings"
    __table_args__ = (
        UniqueConstraint(
            "source_control_id", "target_control_id", "mapping_type",
            name="cross_framework_mappings_source_control_id_target_control_id_key",
        ),
    )

    # Deterministic UUID5 from bundle — no default
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    source_control_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("framework_controls.id", ondelete="CASCADE"),
        nullable=False,
    )
    target_control_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("framework_controls.id", ondelete="CASCADE"),
        nullable=False,
    )
    mapping_type: Mapped[MappingType] = mapped_column(
        SAEnum(MappingType, name="mapping_type", create_type=False),
        nullable=False,
        server_default="maps-to",
    )
    confidence: Mapped[Decimal] = mapped_column(
        Numeric(3, 2), nullable=False, server_default="0.85"
    )
    source_reference: Mapped[str | None] = mapped_column(String(200))
    notes: Mapped[str | None] = mapped_column(Text)
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    # Relationships
    source_control: Mapped["FrameworkControl"] = relationship(
        foreign_keys=[source_control_id], back_populates="source_mappings"
    )
    target_control: Mapped["FrameworkControl"] = relationship(
        foreign_keys=[target_control_id], back_populates="target_mappings"
    )
