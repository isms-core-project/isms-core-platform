# ISMS CORE Platform — Canonical Data Model

<!--
Document ID:    ISMS-API-DATA-001
Title:          ISMS CORE Platform Canonical Data Model
Version:        0.3
Date:           2026-02-08
Updated:        2026-03-08
Owner:          Gregory Griffin
Author:         Claude Code (Opus 4.6)
Classification: Internal
Related Docs:   ARCHITECTURE.md, PLAN.md, SCHEMA.md
Change Log:     v0.3 — Added GeneratorDefinition entity (3.16). Added language + source_label
                        to Policy (3.5); language to Implementation (3.7). Updated bottom note
                        to reflect Phases 0–7 in progress. 2026-03-08.
                v0.2 — Added INS to policy_type field. Fixed control_groups.json count (53,
                        not 54 — a.0 removed, foundation group '00' is a permanent DB entity
                        not in the JSON bundle). Updated bottom note to reflect current phase.
-->

---

## 1. Design Principles

1. **Stable identifiers** — Every entity gets a UUID at creation that never changes. Enables upsert, stable URLs, and cross-system references.
2. **Two products, one model** — Framework and Operational are peers, not parent/child. Both share control groups, differ in policy type and workbook structure.
3. **Read-only source** — The platform indexes files from read-only mounts. It never modifies source policies, workbooks, or IMPs.
4. **Relationships are explicit** — Cross-framework mappings, control stacking, and evidence-to-requirement links are first-class entities, not embedded arrays.
5. **JSONB for flexibility** — Structured fields for query-critical data, JSONB for metadata that varies per entity.

---

## 2. Entity Relationship Overview

```
┌──────────────┐    has_many    ┌──────────────────┐
│  Framework   │───────────────►│ FrameworkControl  │
│  (ISO,NIST)  │                │ (A.8.24, SC-13)  │
└──────────────┘                └────────┬─────────┘
                                         │
                    ┌────────────────────┤ maps_to (CrossFrameworkMapping)
                    ▼                    │
         ┌──────────────────┐           │
         │ FrameworkControl  │◄──────────┘
         │ (other framework) │
         └──────────────────┘

┌──────────────┐    contains    ┌──────────────────┐
│ ControlGroup │───────────────►│ FrameworkControl  │
│ (53 groups)  │                │ (ISO 27001 only)  │
└──────┬───────┘                └──────────────────┘
       │
       │ has_many
       ├───────────►┌──────────────┐    defines     ┌──────────────┐
       │            │   Policy     │───────────────►│ Requirement  │
       │            │ (GOV/OP-POL) │                │ ("shall"s)   │
       │            └──────────────┘                └──────┬───────┘
       │                                                    │
       │ has_many                                           │ assessed_by
       ├───────────►┌──────────────┐                       │
       │            │Implementation│                       │
       │            │ (UG/TG docs) │                       │
       │            └──────────────┘                       │
       │                                                    │
       │ has_many                                           ▼
       ├───────────►┌──────────────┐    contains    ┌──────────────┐
       │            │  Assessment  │───────────────►│AssessmentItem│
       │            │ (workbook)   │                │ (row/finding)│
       │            └──────────────┘                └──────────────┘
       │
       │ has_many
       ├───────────►┌──────────────┐
       │            │   Evidence   │
       │            └──────────────┘
       │
       │ has_many
       └───────────►┌──────────────┐
                    │     Gap      │
                    └──────────────┘
```

---

## 3. Entity Definitions

### 3.1 Framework

A reference standard or framework loaded into the platform.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `code` | VARCHAR(50) | Unique code: `ISO27001_2022`, `NIST_CSF_2.0`, `NIST_800_53_R5`, `CIS_V8`, `MITRE_ATTACK_V18`, `OWASP_TOP10_2025`, `OWASP_ASVS_4.0`, `SWISS_NDSG`, `EU_GDPR`, `FINMA`, `NIS2`, `DORA`, `PCI_DSS_4.0.1`, `EU_AI_ACT`, `US_CLOUD_ACT` |
| `name` | VARCHAR(200) | Display name: "ISO/IEC 27001:2022" |
| `version` | VARCHAR(20) | Standard version: "2022", "2.0", "Rev 5" |
| `publisher` | VARCHAR(100) | "ISO/IEC", "NIST", "MITRE", "CIS" |
| `source_url` | TEXT | Official source URL |
| `description` | TEXT | Brief description |
| `controls_count` | INTEGER | Number of controls loaded |
| `loaded_at` | TIMESTAMPTZ | When framework data was imported |
| `bundle_hash` | VARCHAR(64) | SHA-256 of source bundle (detect changes) |
| `metadata` | JSONB | Additional attributes |

**Identifier strategy**: UUID5 derived from `code` (deterministic — same code always produces same UUID).

### 3.2 FrameworkControl

An individual control, category, function, or technique from any framework.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `framework_id` | UUID FK | Parent framework |
| `control_id` | VARCHAR(50) | Native ID: "A.8.24", "PR.DS-01", "SC-13", "T1566", "CIS 1.1" |
| `parent_id` | UUID FK (self) | Hierarchy: subcategory → category → function |
| `title` | VARCHAR(500) | Control title |
| `description` | TEXT | Control description/guidance |
| `control_type` | VARCHAR(50)[] | `[Preventive, Detective, Corrective]` (ISO) |
| `security_properties` | VARCHAR(50)[] | `[Confidentiality, Integrity, Availability]` (ISO) |
| `level` | INTEGER | Hierarchy depth: 0=section, 1=control, 2=sub-control |
| `sort_order` | INTEGER | Display ordering |
| `metadata` | JSONB | Framework-specific attributes (see below) |

**Framework-specific metadata (JSONB)**:

```json
// ISO 27001:2022
{
  "section": "A.8",
  "category": "Technological controls",
  "cybersecurity_concepts": ["Protect"],
  "operational_capabilities": ["System and network security"],
  "security_domains": ["Protection"],
  "iso27002_reference": "8.24"
}

// NIST CSF 2.0
{
  "function": "PR",
  "category": "PR.DS",
  "implementation_examples": ["..."]
}

// NIST SP 800-53 Rev 5
{
  "family": "SC",
  "baseline_low": false,
  "baseline_moderate": true,
  "baseline_high": true,
  "related_controls": ["SC-12", "SC-28"],
  "assessment_method": "Examine"
}

// MITRE ATT&CK
{
  "tactic_ids": ["TA0001", "TA0009"],
  "matrix": "Enterprise",
  "platforms": ["Windows", "Linux", "macOS"],
  "is_subtechnique": false,
  "data_sources": ["Network Traffic", "File Monitoring"],
  "detection": "Monitor for..."
}

// CIS Controls v8
{
  "control_group": 1,
  "safeguard_number": "1.1",
  "asset_type": "Devices",
  "security_function": "Identify",
  "implementation_group": ["IG1", "IG2", "IG3"]
}
```

**Identifier strategy**: UUID5 derived from `framework_code + ":" + control_id`.

### 3.3 CrossFrameworkMapping

Explicit relationship between controls in different frameworks.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `source_control_id` | UUID FK | Source control (e.g., ISO A.8.24) |
| `target_control_id` | UUID FK | Target control (e.g., NIST SC-13) |
| `mapping_type` | VARCHAR(30) | `maps-to`, `partially-maps-to`, `related-to`, `mitigates`, `detects` |
| `confidence` | DECIMAL(3,2) | 0.00–1.00 mapping confidence |
| `source_reference` | VARCHAR(200) | Where this mapping comes from |
| `notes` | TEXT | Mapping rationale |
| `metadata` | JSONB | Additional attributes |

**Identifier strategy**: UUID5 derived from `source_control_id + ":" + target_control_id + ":" + mapping_type`.

**Example mappings**:
```
ISO A.8.24 ──maps-to──► NIST CSF PR.DS-01     (0.90)
ISO A.8.24 ──maps-to──► NIST 800-53 SC-13     (0.95)
ISO A.8.24 ──maps-to──► CIS 3.10              (0.85)
NIST SC-13 ──mitigates──► MITRE T1486          (0.80)
NIST SC-13 ──mitigates──► MITRE T1560          (0.75)
ISO A.8.24 ──maps-to──► GDPR Art.32            (0.70)
ISO A.8.24 ──maps-to──► nDSG Art.8             (0.70)
```

### 3.4 ControlGroup

One of the 53 ISMS CORE control groups (our stacking model).

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `group_code` | VARCHAR(30) | `a.5.1-4`, `a.8.24`, `a.5.15-16-18` |
| `name` | VARCHAR(200) | "Use of Cryptography", "Identity and Access Management" |
| `section` | VARCHAR(10) | `A.5`, `A.6`, `A.7`, `A.8` |
| `section_name` | VARCHAR(50) | "Organisational", "People", "Physical", "Technological" |
| `folder_name` | VARCHAR(100) | `isms-a.8.24-use-of-cryptography` |
| `is_stacked` | BOOLEAN | True if group contains multiple controls |
| `stacked_control_ids` | VARCHAR(10)[] | `[A.5.15, A.5.16, A.5.18]` |
| `has_framework` | BOOLEAN | True if Framework product exists |
| `has_operational` | BOOLEAN | True if Operational product exists |
| `framework_status` | VARCHAR(20) | `complete`, `partial`, `basic`, `incomplete` |
| `operational_status` | VARCHAR(20) | `complete`, `partial`, `basic`, `incomplete` |
| `metadata` | JSONB | Additional attributes |

**Identifier strategy**: UUID5 derived from `group_code`.

### 3.5 Policy

A governance or operational policy document.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Parent control group |
| `product_type` | VARCHAR(15) | `framework` or `operational` |
| `policy_type` | VARCHAR(10) | `POL`, `OP-POL`, `INS`, `REF`, `CTX`, `FORM` |
| `document_id` | VARCHAR(50) | `ISMS-POL-A.8.24-SN` or `ISMS-OP-POL-A.8.24` |
| `title` | VARCHAR(300) | Policy title |
| `file_path` | TEXT | Relative path from mount root |
| `content_hash` | VARCHAR(64) | SHA-256 of file content (change detection) |
| `word_count` | INTEGER | Document size |
| `requirements_count` | INTEGER | Number of "shall" statements extracted |
| `last_parsed` | TIMESTAMPTZ | When last indexed |
| `language` | VARCHAR(5) | Language code: `en`, `de`, `fr`, `it` (default `en`) |
| `source_label` | VARCHAR(200) | Origin label for external docs (e.g. "Acme Corp") — null for ISMS CORE native docs |
| `metadata` | JSONB | Version, date, approval status |

### 3.6 Requirement

A "shall" statement extracted from a policy — the atomic unit of compliance.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `policy_id` | UUID FK | Parent policy |
| `control_group_id` | UUID FK | Parent control group (denormalised for query performance) |
| `requirement_text` | TEXT | The "shall" statement text |
| `section_heading` | VARCHAR(200) | Which policy section it came from |
| `requirement_type` | VARCHAR(15) | `mandatory` ("shall") or `recommended` ("should") |
| `domain_area` | VARCHAR(100) | Functional domain (e.g., "Key Management", "Access Control") |
| `sort_order` | INTEGER | Position within policy |
| `compliance_status` | VARCHAR(20) | `compliant`, `partial`, `non-compliant`, `not-assessed` |
| `evidence_count` | INTEGER | Number of linked evidence items |
| `metadata` | JSONB | Additional context |

**Identifier strategy**: UUID5 derived from `policy_document_id + ":" + sort_order + ":" + hash(requirement_text[:100])`.

### 3.7 Implementation

An implementation guide document (Framework product only).

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Parent control group |
| `impl_type` | VARCHAR(5) | `UG` or `TG` |
| `document_id` | VARCHAR(50) | `ISMS-IMP-A.8.24.1-UG` |
| `title` | VARCHAR(300) | Document title |
| `file_path` | TEXT | Relative path from mount root |
| `content_hash` | VARCHAR(64) | SHA-256 (change detection) |
| `word_count` | INTEGER | Document size |
| `last_parsed` | TIMESTAMPTZ | When last indexed |
| `language` | VARCHAR(5) | Language code: `en`, `de`, `fr`, `it` (default `en`) |
| `metadata` | JSONB | Part structure, related workbook |

### 3.8 Assessment

An Excel workbook containing compliance assessment data.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Parent control group |
| `product_type` | VARCHAR(15) | `framework` or `operational` |
| `assessment_type` | VARCHAR(20) | `detailed` (Framework) or `checklist` (Operational) |
| `document_id` | VARCHAR(50) | `ISMS-IMP-A.8.24.1` or `ISMS-OP-CHK-A.8.24` |
| `workbook_name` | VARCHAR(200) | Human-readable name |
| `file_path` | TEXT | Relative path from mount root |
| `file_hash` | VARCHAR(64) | SHA-256 (change detection) |
| `file_size` | BIGINT | File size in bytes |
| `sheets_count` | INTEGER | Number of sheets |
| `overall_score` | DECIMAL(5,2) | Compliance percentage (0.00–100.00) |
| `items_total` | INTEGER | Total assessment items |
| `items_compliant` | INTEGER | Compliant items |
| `items_partial` | INTEGER | Partially compliant |
| `items_non_compliant` | INTEGER | Non-compliant |
| `items_na` | INTEGER | Not applicable |
| `gaps_count` | INTEGER | Identified gaps |
| `last_generated` | TIMESTAMPTZ | When workbook was generated |
| `last_parsed` | TIMESTAMPTZ | When last indexed by platform |
| `summary` | JSONB | Per-sheet scores, executive summary data |

### 3.9 AssessmentSheet

An individual sheet within a workbook.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `assessment_id` | UUID FK | Parent assessment |
| `sheet_name` | VARCHAR(50) | Sheet tab name |
| `sheet_type` | VARCHAR(20) | `executive_summary`, `dashboard`, `assessment`, `reference`, `config` |
| `row_count` | INTEGER | Data rows (excluding headers) |
| `column_count` | INTEGER | Columns |
| `compliance_score` | DECIMAL(5,2) | Sheet-level compliance (if applicable) |
| `metadata` | JSONB | Column definitions, formula details |

### 3.10 AssessmentItem

An individual row/finding within an assessment sheet — the atomic evidence unit.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `sheet_id` | UUID FK | Parent sheet |
| `assessment_id` | UUID FK | Parent assessment (denormalised) |
| `control_group_id` | UUID FK | Parent control group (denormalised) |
| `row_number` | INTEGER | Source row in Excel |
| `item_text` | TEXT | Requirement/check text |
| `status` | VARCHAR(20) | `compliant`, `partial`, `non_compliant`, `na`, `not_assessed` |
| `evidence_reference` | TEXT | Evidence description/location |
| `owner` | VARCHAR(100) | Responsible person/role |
| `due_date` | DATE | Remediation due date (if non-compliant) |
| `notes` | TEXT | Additional notes |
| `metadata` | JSONB | Additional columns from workbook |

### 3.11 Evidence

An artifact proving a requirement is met.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Control group |
| `requirement_id` | UUID FK (nullable) | Linked requirement |
| `assessment_item_id` | UUID FK (nullable) | Linked assessment item |
| `evidence_type` | VARCHAR(30) | `document`, `screenshot`, `log_extract`, `config_export`, `test_result`, `attestation` |
| `title` | VARCHAR(300) | Evidence description |
| `file_path` | TEXT | Location (relative path or URL) |
| `collected_date` | DATE | When evidence was collected |
| `expires_date` | DATE | When evidence becomes stale (nullable) |
| `verified_by` | VARCHAR(100) | Who verified this evidence |
| `verified_date` | DATE | When verified |
| `metadata` | JSONB | Additional attributes |

### 3.12 Gap

A compliance gap or non-conformity.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Control group |
| `requirement_id` | UUID FK (nullable) | Related requirement |
| `assessment_item_id` | UUID FK (nullable) | Source assessment item |
| `product_type` | VARCHAR(15) | `framework`, `operational`, or `both` |
| `gap_description` | TEXT | What's missing |
| `severity` | VARCHAR(10) | `critical`, `high`, `medium`, `low` |
| `status` | VARCHAR(15) | `open`, `in_progress`, `closed`, `accepted` |
| `owner` | VARCHAR(100) | Responsible person/role |
| `due_date` | DATE | Remediation target date |
| `remediation_plan` | TEXT | How to fix |
| `closed_date` | DATE | When closed (nullable) |
| `closed_by` | VARCHAR(100) | Who closed (nullable) |
| `metadata` | JSONB | Risk score, business impact |

### 3.13 CorrelationResult

QA correlation between claimed scores and verified content (from 36_correlation_qa_architecture.md).

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `control_group_id` | UUID FK | Control group |
| `framework_control_id` | UUID FK (nullable) | Framework requirement |
| `document_id` | VARCHAR(50) | Assessed document |
| `correlation_method` | VARCHAR(20) | `existence`, `keyword`, `semantic`, `manual` |
| `correlation_strength` | DECIMAL(3,2) | 0.00–1.00 |
| `claimed_score` | DECIMAL(5,2) | Score from workbook |
| `verified_score` | DECIMAL(5,2) | Score from correlation |
| `qa_status` | VARCHAR(15) | `pass`, `warning`, `fail`, `needs_review` |
| `coverage_keywords` | TEXT[] | Keywords found |
| `missing_keywords` | TEXT[] | Keywords expected but not found |
| `run_date` | TIMESTAMPTZ | When correlation was run |
| `metadata` | JSONB | Additional QA details |

### 3.14 GeneratorDefinition *(Phase 7)*

Structural metadata extracted from each QA'd Python generator script. One row per generator file (one per assessment domain / workbook). The authoritative source for WebUI form rendering and script regeneration.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `document_id` | VARCHAR(80) | Unique key: `ISMS-IMP-A.8.17.1`, `ISMS-IMP-A.5.1-2-6.1-2.S1` |
| `workbook_name` | VARCHAR(200) | Human-readable workbook name |
| `control_id` | VARCHAR(80) | `CONTROL_ID` constant from generator: `A.8.17`, `A.5.1-2-6.1-2` |
| `control_name` | VARCHAR(300) | `CONTROL_NAME` constant from generator |
| `group_code` | VARCHAR(80) | Parsed group code — matches `control_groups.group_code` |
| `control_group_id` | UUID FK (nullable) | FK to `control_groups` — resolved at import time |
| `domain_number` | INTEGER | Assessment domain index (1, 2, 3 …) |
| `domain_total` | INTEGER | Total domains for this control group |
| `is_stacked` | BOOLEAN | True if generator covers multiple ISO 27001 controls |
| `stacked_control_ids` | JSONB | `["A.5.1", "A.5.2", "A.6.1", "A.6.2"]` for stacked generators |
| `sheets` | JSONB | `[{"name": "Inventory", "type": "input"}, ...]` — all sheet definitions |
| `sheet_count` | INTEGER | Number of sheets |
| `sheet_source` | VARCHAR(20) | How sheet names were extracted: `docstring` or `code` |
| `source_file` | TEXT | Relative path from `50-isms-core-framework/` root |
| `parsed_at` | TIMESTAMPTZ | When last parsed from source file |
| `user_override` | BOOLEAN | When true, importer skips this row on re-import (preserves manual edits) |
| `sheet_schemas` | JSONB | Full per-sheet column schema from produced `.xlsx` workbook (Phase 7.5) |

**`sheet_schemas` structure (per sheet):**
```json
{
  "sheet_name": "Inventory",
  "sheet_type": "assessment",
  "position": 2,
  "header_row": 3,
  "data_start_row": 4,
  "freeze_panes": "A4",
  "hide_gridlines": true,
  "status_column_index": 3,
  "status_column_letter": "D",
  "columns": [
    {
      "index": 1, "letter": "A", "header": "Asset ID",
      "width": 15.0, "dv_values": [], "required": false, "is_status_col": false
    },
    {
      "index": 3, "letter": "D", "header": "Compliance Status",
      "width": 22.0,
      "dv_values": ["Compliant", "Partial", "Non-Compliant", "N/A"],
      "required": true, "is_status_col": true
    }
  ]
}
```

**Identifier strategy**: UUID4 (random) — no deterministic UUID needed as `document_id` is the stable business key.

**Population**: `datasets/scripts/parse_generators.py` → `generator_registry.json` → `import_generator_registry.py` → DB. Sheet schemas populated separately via `import_sheet_schemas.py` from `workbook_schemas.json`.

### 3.15 AuditLog

All platform actions for compliance audit trail.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Auto-generated |
| `user_id` | UUID FK | Acting user |
| `action` | VARCHAR(30) | `view`, `download`, `sync`, `import`, `update`, `export`, `login`, `logout` |
| `resource_type` | VARCHAR(30) | `control_group`, `policy`, `assessment`, `gap`, `evidence`, `framework` |
| `resource_id` | UUID | Target resource |
| `ip_address` | INET | Client IP |
| `user_agent` | TEXT | Client user agent |
| `details` | JSONB | Action-specific details |
| `created_at` | TIMESTAMPTZ | Timestamp |

### 3.16 User

Platform user accounts.

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Stable identifier |
| `email` | VARCHAR(255) | Unique email |
| `username` | VARCHAR(100) | Display name |
| `hashed_password` | VARCHAR(255) | bcrypt hash |
| `full_name` | VARCHAR(200) | Full name |
| `role` | VARCHAR(20) | `admin`, `isms_manager`, `auditor`, `control_owner`, `viewer` |
| `is_active` | BOOLEAN | Account active |
| `assigned_groups` | UUID[] | Control groups this user owns (for control_owner role) |
| `last_login` | TIMESTAMPTZ | Last login timestamp |
| `metadata` | JSONB | Preferences, settings |

---

## 4. Materialized Views

Pre-computed for dashboard performance.

### v_control_group_summary

```sql
CREATE MATERIALIZED VIEW v_control_group_summary AS
SELECT
    cg.id,
    cg.group_code,
    cg.name,
    cg.section,
    -- Framework product
    COUNT(DISTINCT p_fw.id) AS framework_policies,
    COUNT(DISTINCT imp.id) AS framework_implementations,
    COUNT(DISTINCT a_fw.id) AS framework_assessments,
    AVG(a_fw.overall_score) AS framework_avg_score,
    -- Operational product
    COUNT(DISTINCT p_op.id) AS operational_policies,
    COUNT(DISTINCT a_op.id) AS operational_assessments,
    AVG(a_op.overall_score) AS operational_avg_score,
    -- Combined
    COUNT(DISTINCT g.id) FILTER (WHERE g.status = 'open') AS open_gaps,
    COUNT(DISTINCT e.id) AS evidence_count,
    COUNT(DISTINCT r.id) AS requirements_count,
    COUNT(DISTINCT r.id) FILTER (WHERE r.compliance_status = 'compliant') AS requirements_met
FROM control_groups cg
LEFT JOIN policies p_fw ON p_fw.control_group_id = cg.id AND p_fw.product_type = 'framework'
LEFT JOIN policies p_op ON p_op.control_group_id = cg.id AND p_op.product_type = 'operational'
LEFT JOIN implementations imp ON imp.control_group_id = cg.id
LEFT JOIN assessments a_fw ON a_fw.control_group_id = cg.id AND a_fw.product_type = 'framework'
LEFT JOIN assessments a_op ON a_op.control_group_id = cg.id AND a_op.product_type = 'operational'
LEFT JOIN gaps g ON g.control_group_id = cg.id
LEFT JOIN evidence e ON e.control_group_id = cg.id
LEFT JOIN requirements r ON r.control_group_id = cg.id
GROUP BY cg.id, cg.group_code, cg.name, cg.section;
```

### v_dashboard_compliance

```sql
CREATE MATERIALIZED VIEW v_dashboard_compliance AS
SELECT
    'framework' AS product,
    cg.section,
    COUNT(*) AS total_groups,
    COUNT(*) FILTER (WHERE cg.framework_status = 'complete') AS complete,
    COUNT(*) FILTER (WHERE cg.framework_status = 'partial') AS partial,
    COUNT(*) FILTER (WHERE cg.framework_status = 'basic') AS basic,
    COUNT(*) FILTER (WHERE cg.framework_status = 'incomplete') AS incomplete,
    ROUND(AVG(a.overall_score), 1) AS avg_compliance_score
FROM control_groups cg
LEFT JOIN assessments a ON a.control_group_id = cg.id AND a.product_type = 'framework'
WHERE cg.has_framework = true
GROUP BY cg.section
UNION ALL
SELECT
    'operational' AS product,
    cg.section,
    COUNT(*) AS total_groups,
    COUNT(*) FILTER (WHERE cg.operational_status = 'complete') AS complete,
    COUNT(*) FILTER (WHERE cg.operational_status = 'partial') AS partial,
    COUNT(*) FILTER (WHERE cg.operational_status = 'basic') AS basic,
    COUNT(*) FILTER (WHERE cg.operational_status = 'incomplete') AS incomplete,
    ROUND(AVG(a.overall_score), 1) AS avg_compliance_score
FROM control_groups cg
LEFT JOIN assessments a ON a.control_group_id = cg.id AND a.product_type = 'operational'
WHERE cg.has_operational = true
GROUP BY cg.section;
```

### v_framework_coverage

```sql
CREATE MATERIALIZED VIEW v_framework_coverage AS
SELECT
    f.code AS framework_code,
    f.name AS framework_name,
    COUNT(DISTINCT fc.id) AS total_controls,
    COUNT(DISTINCT cfm.id) AS mapped_controls,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence >= 0.80) AS high_confidence,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence < 0.80 AND cfm.confidence >= 0.50) AS medium_confidence,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence < 0.50) AS low_confidence,
    ROUND(COUNT(DISTINCT cfm.id)::NUMERIC / NULLIF(COUNT(DISTINCT fc.id), 0) * 100, 1) AS coverage_pct
FROM frameworks f
JOIN framework_controls fc ON fc.framework_id = f.id
LEFT JOIN cross_framework_mappings cfm ON cfm.target_control_id = fc.id
GROUP BY f.code, f.name;
```

---

## 5. Datasets (Reference Framework Bundles)

Following the OpenCTI datasets pattern: **raw source → generator script → JSON bundle**.

### Bundle Format

Each bundle is a JSON file with stable-ID entities and explicit relationships:

```json
{
  "bundle_id": "bundle--<uuid>",
  "bundle_type": "isms-core-dataset",
  "bundle_version": "1.0",
  "framework": {
    "code": "ISO27001_2022",
    "name": "ISO/IEC 27001:2022",
    "version": "2022",
    "publisher": "ISO/IEC"
  },
  "generated_at": "2026-02-08T12:00:00Z",
  "generator": "generate_iso27001.py",
  "objects_count": 97,
  "objects": [
    {
      "type": "framework_control",
      "id": "fc--a8f2e4c1-...",
      "control_id": "A.8.24",
      "title": "Use of cryptography",
      "description": "A policy on the use of cryptographic controls...",
      "level": 1,
      "sort_order": 8240,
      "metadata": {
        "section": "A.8",
        "category": "Technological controls",
        "control_type": ["Preventive"],
        "security_properties": ["Confidentiality", "Integrity", "Availability"]
      }
    }
  ],
  "relationships": [
    {
      "type": "hierarchy",
      "source_id": "fc--a8f2e4c1-...",
      "target_id": "fc--section-a8-...",
      "relationship_type": "part-of"
    }
  ]
}
```

### Planned Bundles

| Bundle File | Source | Objects | Rels | Status |
|------------|--------|---------|------|--------|
| `iso27001_2022.json` | Manual + ISO reference | 97 (4 sections + 93 controls) | 93 | **DONE** |
| `control_groups.json` | 53-group stacking model (+ foundation group '00' seeded separately) | 53 groups | 94 | **DONE** |
| `nist_csf_2.0.json` | NIST API | 134 (6 functions + 22 categories + 106 subcategories) | 128 | **DONE** |
| `nist_sp800_53r5.json` | GitHub OSCAL | 1,216 (20 families + 324 controls + 872 enhancements) | 1,196 | **DONE** |
| `cis_controls_v8.json` | CIS reference (v8.1) | 171 (18 controls + 153 safeguards) | 153 | **DONE** |
| `mitre_attack_v18.json` | MITRE STIX repo (v18.1) | 749 (14 tactics + 691 techniques + 44 mitigations) | 1,362 | **DONE** |
| `owasp.json` | OWASP Foundation | 302 (10 Top 10:2025 + 14 ASVS chapters + 278 requirements) | 278 | **DONE** |
| `swiss_ndsg.json` | fedlex.admin.ch | 11 articles | 0 | **DONE** |
| `eu_gdpr.json` | EUR-Lex | 16 articles | 0 | **DONE** |
| `finma.json` | finma.ch | 24 (3 circulars + 21 sections) | 21 | **DONE** |
| `nis2.json` | EU Official Journal | 14 articles | 0 | **DONE** |
| `dora.json` | EU Official Journal | 30 (4 chapters + 26 articles) | 26 | **DONE** |
| `pci_dss_v4.json` | PCI SSC (v4.0.1) | 18 (6 objectives + 12 requirements) | 12 | **DONE** |
| `eu_ai_act.json` | EU Official Journal | 9 articles | 0 | **DONE** |
| `us_cloud_act.json` | Congress.gov / Cornell Law | 5 provisions (info/awareness) | 0 | **DONE** |
| `crosswalk.json` | 6 authoritative mapping sources | 1,898 mapping relationships | 0 | **DONE** |
| **TOTALS** | | **4,748 objects** | **3,363** | **16/16 DONE** |

### Generator Scripts

```
datasets/
├── raw/                                  # Human-editable source data (16 files)
│   ├── iso27001_2022_controls.json       # 93 controls ✓
│   ├── control_groups.json               # 53 groups ✓ (+ foundation group '00' seeded via DB init)
│   ├── nist_csf_2.0.json                 # NIST CSF 2.0 (6 functions, 106 subcategories) ✓
│   ├── nist_sp800_53r5.json              # NIST SP 800-53 Rev 5 (1,196 controls from OSCAL) ✓
│   ├── cis_controls_v8.json              # CIS Controls v8.1 (153 safeguards) ✓
│   ├── mitre_attack_v18.json             # MITRE ATT&CK v18.1 (691 techniques) ✓
│   ├── owasp_top10_2025.json             # OWASP Top 10:2025 (verified from owasp.org) ✓
│   ├── owasp_asvs_4.0.3.json            # OWASP ASVS 4.0.3 (278 requirements) ✓
│   ├── swiss_ndsg.json                   # Swiss nFADP/nDSG (11 articles) ✓
│   ├── eu_gdpr.json                      # EU GDPR (16 articles) ✓
│   ├── finma.json                        # FINMA (3 circulars, 21 sections) ✓
│   ├── nis2.json                         # NIS2 Directive (14 articles) ✓
│   ├── dora.json                         # DORA (26 articles) ✓
│   ├── pci_dss_v4.json                   # PCI DSS v4.0.1 (12 requirements) ✓
│   ├── eu_ai_act.json                    # EU AI Act (9 articles) ✓
│   ├── us_cloud_act.json                 # US CLOUD Act (5 provisions, info only) ✓
│   └── crosswalk_mappings.json           # 1,898 cross-framework mappings ✓
├── scripts/                              # Generator scripts (raw → bundle, 11 scripts)
│   ├── generate_iso27001.py              # → 97 objects, 93 relationships ✓
│   ├── generate_control_groups.py        # → 54 objects, 94 relationships ✓
│   ├── generate_nist_csf.py              # → 134 objects, 128 relationships ✓
│   ├── generate_nist_800_53.py           # → 1,216 objects, 1,196 relationships ✓
│   ├── generate_cis_v8.py               # → 171 objects, 153 relationships ✓
│   ├── generate_mitre_attack.py          # → 749 objects, 1,362 relationships ✓
│   ├── generate_owasp.py                 # → 302 objects, 278 relationships ✓
│   ├── generate_regulatory.py            # → 127 objects, 59 relationships (8 frameworks) ✓
│   ├── assemble_crosswalk_raw.py         # 6 sources → raw crosswalk JSON ✓
│   ├── generate_crosswalk.py             # → 1,898 mapping objects ✓
│   ├── NIST_CSF2_to_ISO27001_2022_mapping.csv     # Research data ✓
│   ├── CIS_v8_to_ISO27001_2022_mapping.csv        # Research data ✓
│   └── MITRE_ATTaCK_to_NIST80053_mapping.csv      # Research data ✓
└── data/                                 # Generated JSON bundles (16 files, ~3.5 MB)
    ├── iso27001_2022.json                # ✓ (98K)
    ├── control_groups.json               # ✓ (54K)
    ├── nist_csf_2.0.json                 # ✓ (93K)
    ├── nist_sp800_53r5.json              # ✓ (961K)
    ├── cis_controls_v8.json              # ✓ (165K)
    ├── mitre_attack_v18.json             # ✓ (668K)
    ├── owasp.json                        # ✓ (320K)
    ├── swiss_ndsg.json                   # ✓ (6K)
    ├── eu_gdpr.json                      # ✓ (8K)
    ├── finma.json                        # ✓ (19K)
    ├── nis2.json                         # ✓ (7K)
    ├── dora.json                         # ✓ (20K)
    ├── pci_dss_v4.json                   # ✓ (13K)
    ├── eu_ai_act.json                    # ✓ (5K)
    ├── us_cloud_act.json                 # ✓ (6K)
    └── crosswalk.json                    # ✓ (1,072K)
```

---

## 6. Operational vs Framework Workbook Parsing

The two products have different workbook structures that require different parsing strategies.

### Framework Workbooks (188 generators, diverse structures)

Each Framework generator creates a unique workbook with:
- Variable number of sheets (2–15+)
- Different column layouts per generator
- Mix of assessment, reference, and configuration sheets
- Compliance scores embedded in summary cells or calculated via formulas

**Parsing strategy**: Pattern-based extraction.
1. Find "Executive Summary" or "Summary" sheet → extract overall score
2. Find assessment sheets (contain Status/Compliance/Result columns) → extract items
3. Identify status values (`Compliant`, `Partial`, `Non-Compliant`, `N/A`, or colour-coded)
4. Extract evidence references (typically "Evidence" or "Notes" column)

### Operational Checklists (53 generators, uniform structure)

All Operational generators use the shared engine (`op_checklist_engine.py`) and produce:
- Sheet 1: Executive Summary (control info, date, version)
- Sheet 2: Dashboard (COUNTIF aggregation, traffic-light scoring)
- Sheets 3–N: Domain checklists (Requirement | Status | Evidence | Owner | Due | Notes)

**Parsing strategy**: Structured extraction (uniform format).
1. Read Dashboard sheet → extract overall compliance score and per-domain scores
2. Read each domain sheet → extract all rows as AssessmentItems
3. Map Status column → compliance_status enum
4. Map Evidence column → evidence_reference text

---

## 7. Database Schema — `schemas/init_db.sql`

The evolved schema replaces both `20_init_db.sql` (core ISMS) and `21_init_frameworks_db.sql` (per-framework tables) with a unified model.

**Key architectural change**: Instead of per-framework tables (iso27001_controls, nist_csf_functions, nist_800_53_controls, mitre_attack_techniques, etc.), we use the unified `frameworks` + `framework_controls` pattern with JSONB metadata for framework-specific attributes. This matches our bundle format and is extensible to any future framework.

### Schema Summary

| Category | Tables | Purpose |
|----------|--------|---------|
| Core | `users`, `sessions` | Authentication & session management |
| Reference | `frameworks`, `framework_controls`, `cross_framework_mappings` | All loaded standards (unified) |
| Groups | `control_groups`, `control_group_controls` | 53 control groups + ISO control mapping |
| Content | `policies`, `requirements`, `implementations` | ISMS documents & extracted "shall" statements |
| Generator | `generator_definitions` | Phase 7: 188 QA'd generator scripts → DB (form renderer + regen engine) |
| Assessment | `assessments`, `assessment_sheets`, `assessment_items` | Workbook data (granular) |
| Compliance | `evidence`, `gaps` | Proof & non-conformities |
| QA | `correlation_results` | Score verification & cross-framework QA |
| System | `audit_log`, `data_load_history` | Audit trail & import tracking |

### Schema Stats

| Metric | Count |
|--------|-------|
| **Tables** | 19 (16 entity + sessions + junction + data_load_history) |
| **Enum types** | 14 (user_role, product_type, compliance_status, etc.) |
| **Indexes** | 64 (B-tree, GIN trigram, GIN tsvector, GIN JSONB) |
| **Materialized views** | 3 (control_group_summary, dashboard_compliance, framework_coverage) |
| **Triggers** | 12 (auto updated_at on all mutable tables incl. generator_definitions) |
| **Functions** | 3 (update_updated_at, refresh_materialized_views, get_control_mappings) |
| **Alembic migrations** | 5 (001 foundation; 002 external docs; 003–005 generator_definitions) |

---

## 8. Index Strategy

### PostgreSQL Indexes

```sql
-- Control groups
CREATE INDEX idx_control_groups_section ON control_groups(section);
CREATE INDEX idx_control_groups_group_code ON control_groups(group_code);

-- Policies
CREATE INDEX idx_policies_control_group ON policies(control_group_id);
CREATE INDEX idx_policies_product_type ON policies(product_type);

-- Requirements
CREATE INDEX idx_requirements_policy ON requirements(policy_id);
CREATE INDEX idx_requirements_control_group ON requirements(control_group_id);
CREATE INDEX idx_requirements_status ON requirements(compliance_status);

-- Assessments
CREATE INDEX idx_assessments_control_group ON assessments(control_group_id);
CREATE INDEX idx_assessments_product_type ON assessments(product_type);

-- Assessment items
CREATE INDEX idx_assessment_items_sheet ON assessment_items(sheet_id);
CREATE INDEX idx_assessment_items_status ON assessment_items(status);

-- Gaps
CREATE INDEX idx_gaps_control_group ON gaps(control_group_id);
CREATE INDEX idx_gaps_status ON gaps(status);
CREATE INDEX idx_gaps_severity ON gaps(severity);

-- Cross-framework mappings
CREATE INDEX idx_cfm_source ON cross_framework_mappings(source_control_id);
CREATE INDEX idx_cfm_target ON cross_framework_mappings(target_control_id);

-- Full-text search (PostgreSQL)
CREATE INDEX idx_policies_content_search ON policies USING gin(to_tsvector('english', title));
CREATE INDEX idx_requirements_text_search ON requirements USING gin(to_tsvector('english', requirement_text));
```

### OpenSearch Indexes

```
isms-policies       → Full policy document content (for cross-document search)
isms-implementations → IMP-UG/TG document content
isms-requirements   → Requirement text (for semantic search in Phase 5)
```

---

*Phases 0–6 complete; Phase 7 (Assessment Content Bootstrap) in progress (2026-03-08). All entity types defined in `schemas/init_db.sql` and implemented in SQLAlchemy ORM. `GeneratorDefinition` table populated with 189 rows (188 Framework + 1 foundation checklist); sheet_schemas JSONB populated for 188. See SCHEMA.md for live DB state and migration history.*
