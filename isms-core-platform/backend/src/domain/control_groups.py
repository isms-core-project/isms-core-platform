import uuid

from sqlalchemy import Boolean, Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, SAEnum, TimestampMixin
from src.database.enums import ControlGroupStatus, ProductFamily


# Junction table: which ISO 27001 framework_controls belong to which control_group
control_group_controls = Table(
    "control_group_controls",
    Base.metadata,
    Column(
        "control_group_id",
        UUID(as_uuid=True),
        ForeignKey("control_groups.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "framework_control_id",
        UUID(as_uuid=True),
        ForeignKey("framework_controls.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class ControlGroup(TimestampMixin, Base):
    __tablename__ = "control_groups"

    # Deterministic UUID5 from bundle — no default
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    group_code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    section: Mapped[str] = mapped_column(String(10), nullable=False)
    section_name: Mapped[str] = mapped_column(String(50), nullable=False)
    folder_name: Mapped[str] = mapped_column(String(100), nullable=False)
    is_stacked: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="false"
    )
    stacked_control_ids: Mapped[list | None] = mapped_column(
        ARRAY(String(10)), server_default="{}"
    )
    has_framework: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true"
    )
    has_operational: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true"
    )
    framework_status: Mapped[ControlGroupStatus] = mapped_column(
        SAEnum(ControlGroupStatus, name="control_group_status", create_type=False),
        nullable=False,
        server_default="incomplete",
    )
    operational_status: Mapped[ControlGroupStatus] = mapped_column(
        SAEnum(ControlGroupStatus, name="control_group_status", create_type=False),
        nullable=False,
        server_default="incomplete",
    )
    product_family: Mapped[ProductFamily] = mapped_column(
        SAEnum(ProductFamily, name="productfamily", create_type=False),
        nullable=False,
        server_default="ISMS",
    )
    metadata_: Mapped[dict] = mapped_column(
        "metadata", JSONB, default=dict, server_default="{}"
    )

    # Relationships
    controls: Mapped[list] = relationship(
        "FrameworkControl", secondary=control_group_controls
    )
    policies: Mapped[list] = relationship("Policy", back_populates="control_group")
    requirements: Mapped[list] = relationship(
        "Requirement", back_populates="control_group"
    )
    implementations: Mapped[list] = relationship(
        "Implementation", back_populates="control_group"
    )
    assessments: Mapped[list] = relationship(
        "Assessment", back_populates="control_group"
    )
    evidence_items: Mapped[list] = relationship(
        "Evidence", back_populates="control_group"
    )
    gaps: Mapped[list] = relationship("Gap", back_populates="control_group")
    correlation_results: Mapped[list] = relationship(
        "CorrelationResult", back_populates="control_group"
    )
