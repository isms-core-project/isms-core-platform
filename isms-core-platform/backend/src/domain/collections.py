import uuid
from datetime import date, datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Table, Text, func
from sqlalchemy import Date as SADate
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base, TimestampMixin

# Junction table
collection_assessments = Table(
    "collection_assessments",
    Base.metadata,
    Column("collection_id", UUID(as_uuid=True), ForeignKey("assessment_collections.id", ondelete="CASCADE"), primary_key=True),
    Column("assessment_id", UUID(as_uuid=True), ForeignKey("assessments.id", ondelete="CASCADE"), primary_key=True),
    Column("added_at", DateTime(timezone=True), server_default=func.now()),
)


class AssessmentCollection(TimestampMixin, Base):
    __tablename__ = "assessment_collections"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    product_family: Mapped[str] = mapped_column(String(20), nullable=False)
    product_type: Mapped[str | None] = mapped_column(String(20))
    due_date: Mapped[date | None] = mapped_column(SADate)
    project_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("projects.id", ondelete="SET NULL"),
        nullable=True,
    )

    assessments: Mapped[list] = relationship(
        "Assessment",
        secondary=collection_assessments,
        backref="collections",
        lazy="select",
    )
