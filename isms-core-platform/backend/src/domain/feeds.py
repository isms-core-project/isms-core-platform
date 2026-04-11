"""SQLAlchemy models for Phase 25/28 — Threat Intelligence & Vulnerability Feeds."""

import uuid
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Float, Integer, String, Text, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class FeedRun(Base):
    __tablename__ = "feed_runs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    feed_name: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="running")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    item_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)


class MitreTechnique(Base):
    __tablename__ = "mitre_techniques"
    __table_args__ = (
        UniqueConstraint("stix_id", "source", name="uq_mitre_techniques_stix_source"),
        Index("ix_mitre_techniques_source", "source"),
        Index("ix_mitre_techniques_technique_id", "technique_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stix_id: Mapped[str] = mapped_column(String(100), nullable=False)
    technique_id: Mapped[str] = mapped_column(String(20), nullable=False)
    source: Mapped[str] = mapped_column(String(30), nullable=False)   # attack_v18 | attack_v19 | atlas
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    tactics: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    platforms: Mapped[list] = mapped_column(JSONB, nullable=False, default=list)
    is_subtechnique: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    deprecated: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class CisaKevEntry(Base):
    __tablename__ = "cisa_kev_entries"
    __table_args__ = (
        Index("ix_cisa_kev_date_added", "date_added"),
        Index("ix_cisa_kev_known_ransomware", "known_ransomware"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cve_id: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    vendor_project: Mapped[str | None] = mapped_column(String(255), nullable=True)
    product: Mapped[str | None] = mapped_column(String(255), nullable=True)
    vulnerability_name: Mapped[str | None] = mapped_column(String(512), nullable=True)
    date_added: Mapped[date | None] = mapped_column(Date, nullable=True)
    short_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    required_action: Mapped[str | None] = mapped_column(Text, nullable=True)
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    known_ransomware: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class MitreGroup(Base):
    """Phase 28 — MITRE ATT&CK intrusion-set objects (threat actor groups)."""
    __tablename__ = "mitre_groups"
    __table_args__ = (
        UniqueConstraint("stix_id", "source", name="uq_mitre_groups_stix_source"),
        Index("ix_mitre_groups_source",   "source"),
        Index("ix_mitre_groups_group_id", "group_id"),
    )

    id: Mapped[uuid.UUID]    = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stix_id: Mapped[str]     = mapped_column(String(100), nullable=False)
    source: Mapped[str]      = mapped_column(String(30),  nullable=False)
    group_id: Mapped[str]    = mapped_column(String(20),  nullable=False)
    name: Mapped[str]        = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    aliases: Mapped[list]    = mapped_column(JSONB, nullable=False, default=list)
    deprecated: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    url: Mapped[str | None]  = mapped_column(String(512), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class MitreSoftware(Base):
    """Phase 28 — MITRE ATT&CK malware + tool objects."""
    __tablename__ = "mitre_software"
    __table_args__ = (
        UniqueConstraint("stix_id", "source", name="uq_mitre_software_stix_source"),
        Index("ix_mitre_software_source",      "source"),
        Index("ix_mitre_software_software_id", "software_id"),
        Index("ix_mitre_software_type",        "software_type"),
    )

    id: Mapped[uuid.UUID]         = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stix_id: Mapped[str]          = mapped_column(String(100), nullable=False)
    source: Mapped[str]           = mapped_column(String(30),  nullable=False)
    software_id: Mapped[str]      = mapped_column(String(20),  nullable=False)
    name: Mapped[str]             = mapped_column(String(255), nullable=False)
    software_type: Mapped[str]    = mapped_column(String(20),  nullable=False)  # malware | tool
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    aliases: Mapped[list]         = mapped_column(JSONB, nullable=False, default=list)
    platforms: Mapped[list]       = mapped_column(JSONB, nullable=False, default=list)
    deprecated: Mapped[bool]      = mapped_column(Boolean, nullable=False, default=False)
    url: Mapped[str | None]       = mapped_column(String(512), nullable=True)
    created_at: Mapped[datetime]  = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime]  = mapped_column(DateTime(timezone=True), nullable=False)


class MitreCampaign(Base):
    """Phase 28 — MITRE ATT&CK campaign objects."""
    __tablename__ = "mitre_campaigns"
    __table_args__ = (
        UniqueConstraint("stix_id", "source", name="uq_mitre_campaigns_stix_source"),
        Index("ix_mitre_campaigns_source",      "source"),
        Index("ix_mitre_campaigns_campaign_id", "campaign_id"),
    )

    id: Mapped[uuid.UUID]    = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stix_id: Mapped[str]     = mapped_column(String(100), nullable=False)
    source: Mapped[str]      = mapped_column(String(30),  nullable=False)
    campaign_id: Mapped[str] = mapped_column(String(20),  nullable=False)
    name: Mapped[str]        = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    aliases: Mapped[list]    = mapped_column(JSONB, nullable=False, default=list)
    first_seen: Mapped[date | None] = mapped_column(Date, nullable=True)
    last_seen: Mapped[date | None]  = mapped_column(Date, nullable=True)
    deprecated: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    url: Mapped[str | None]  = mapped_column(String(512), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


class MitreRelationship(Base):
    """Phase 28 — MITRE ATT&CK relationship objects (group→technique, software→technique, etc.)."""
    __tablename__ = "mitre_relationships"
    __table_args__ = (
        UniqueConstraint("stix_id", "source", name="uq_mitre_relationships_stix_source"),
        Index("ix_mitre_rel_source",     "source"),
        Index("ix_mitre_rel_type",       "relationship_type"),
        Index("ix_mitre_rel_source_ref", "source_ref"),
        Index("ix_mitre_rel_target_ref", "target_ref"),
    )

    id: Mapped[uuid.UUID]            = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stix_id: Mapped[str]             = mapped_column(String(100), nullable=False)
    source: Mapped[str]              = mapped_column(String(30),  nullable=False)
    relationship_type: Mapped[str]   = mapped_column(String(50),  nullable=False)
    source_ref: Mapped[str]          = mapped_column(String(100), nullable=False)
    target_ref: Mapped[str]          = mapped_column(String(100), nullable=False)
    source_type: Mapped[str]         = mapped_column(String(50),  nullable=False)
    target_type: Mapped[str]         = mapped_column(String(50),  nullable=False)
    description: Mapped[str | None]  = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime]     = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime]     = mapped_column(DateTime(timezone=True), nullable=False)


class EpssScore(Base):
    __tablename__ = "epss_scores"
    __table_args__ = (
        Index("ix_epss_scores_score", "score"),
        Index("ix_epss_scores_score_date", "score_date"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cve_id: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    percentile: Mapped[float] = mapped_column(Float, nullable=False)
    score_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
