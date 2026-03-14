import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class ExistenceRunResult(BaseModel):
    total: int
    pass_count: int
    warning_count: int
    fail_count: int
    needs_review_count: int
    duration_ms: int
    run_date: str


class KeywordRunResult(BaseModel):
    total: int
    pass_count: int
    warning_count: int
    fail_count: int
    needs_review_count: int
    duration_ms: int
    run_date: str


class SemanticRunResult(BaseModel):
    total: int
    pass_count: int
    warning_count: int
    fail_count: int
    needs_review_count: int
    duration_ms: int
    run_date: str
    method: str   # "semantic" | "semantic_claude"


class CorrelationResultRead(BaseModel):
    id: uuid.UUID
    control_group_id: uuid.UUID
    control_group_code: str
    control_group_name: str
    document_id: str
    product_type: str        # "framework" | "operational"
    correlation_method: str
    correlation_strength: float
    qa_status: str           # "pass" | "warning" | "fail" | "needs_review"
    coverage_keywords: list[str]
    missing_keywords: list[str]
    run_date: datetime
    metadata: dict

    model_config = {"from_attributes": True}


class QASummaryBucket(BaseModel):
    total: int
    pass_count: int
    warning_count: int
    fail_count: int
    needs_review_count: int
    pass_rate: float         # 0.0 – 1.0


class QASummary(BaseModel):
    last_run: datetime | None
    framework: QASummaryBucket
    operational: QASummaryBucket
    privacy: QASummaryBucket
    cloud: QASummaryBucket
    overall_pass_rate: float


class SynonymRuleRead(BaseModel):
    id: uuid.UUID
    keyword: str
    synonyms: list[str]
    notes: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SynonymRuleCreate(BaseModel):
    keyword: str = Field(..., min_length=2, max_length=100)
    synonyms: list[str] = Field(..., min_length=1)
    notes: str | None = None


class SynonymRulePatch(BaseModel):
    synonyms: list[str] | None = None
    notes: str | None = None
