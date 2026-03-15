# ISMS CORE Platform — DB Schema & Data Architecture

<!--
Document ID:    ISMS-API-SCHEMA-001
Title:          ISMS CORE Platform DB Schema and Data Architecture
Version:        0.1
Date:           2026-03-08
Owner:          Gregory Griffin
Author:         Claude Code (Sonnet 4.6) — Task 7.6
Classification: Internal
Related Docs:   DATA-MODEL.md, ARCHITECTURE.md, schemas/init_db.sql
Change Log:     v0.1 — Initial. Documents live schema state post Alembic migrations 001–005.
                        Phase 7 generator_definitions table in detail.
-->

---

## 1. Schema Version & Migration History

The live schema is initialised from `schemas/init_db.sql` (base) and evolved via Alembic migrations.

| Migration | Date | Changes |
|-----------|------|---------|
| `schemas/init_db.sql` | 2026-02-08 | Base: 15 entity tables, 14 enums, 62 indexes, 3 mat views, 11 triggers |
| `001_foundation` | 2026-03-01 | `policy_type` ADD VALUE `'INS'`; seed Foundation Policies control group (group_code `'00'`) |
| `002_phase6_external` | 2026-03-07 | `product_type` ADD VALUE `'external'`; `policies` +`source_label` +`language`; `implementations` +`language` |
| `003_phase7_generators` | 2026-03-07 | CREATE TABLE `generator_definitions` + 2 indexes |
| `004_generator_override` | 2026-03-07 | `generator_definitions` +`user_override BOOLEAN DEFAULT false` |
| `005_phase7_5_sheet_schemas` | 2026-03-07 | `generator_definitions` +`sheet_schemas JSONB DEFAULT '[]'` |

**Current schema state (2026-03-08):** `schemas/init_db.sql` is fully synced — it incorporates all migrations 001–005 for clean installs. Alembic migrations handle upgrades on existing instances.

---

## 2. Live Database State

Counts verified against `isms_db` on 2026-03-08:

| Table | Count | Notes |
|-------|-------|-------|
| `frameworks` | 15 | ISO 27001, NIST CSF 2.0, NIST 800-53, CIS v8, MITRE ATT&CK v18, OWASP Top 10 + ASVS, Swiss nFADP, EU GDPR, FINMA, NIS2, DORA, PCI DSS, EU AI Act, US CLOUD Act |
| `framework_controls` | ~2,850 | All controls across 15 frameworks |
| `cross_framework_mappings` | ~2,127 | 1,898 crosswalk + 229 control dependencies |
| `control_groups` | 54 | 53 ISO Annex A + foundation group `'00'` |
| `policies` | ~143 | 69 POL (EN+DE) + 53 OP-POL + 12 REF + 7 CTX + 1 FORM + foundation INS/REF |
| `requirements` | ~5,266 | "shall"/"should" statements extracted from policies |
| `implementations` | ~376 | 188 UG + 188 TG |
| `generator_definitions` | 189 | 188 Framework SCR + 1 Foundation checklist |
| `assessments` | ~241 | 188 Framework (from SCR scripts) + 53 Operational (from checklists) |
| `assessment_sheets` | ~1,502 | 959 Framework sheets + 543 Operational sheets |
| `assessment_items` | ~2,591 | Operational checklist items (Framework items via WebUI — Phase 7) |
| `correlation_results` | varies | Existence / keyword / semantic / Claude AI QA runs |
| `evidence` | 0 | Populated by users post-deployment |
| `gaps` | 0 | Populated by users post-deployment |

---

## 3. Enum Types

| Enum | Values |
|------|--------|
| `user_role` | `admin`, `isms_manager`, `auditor`, `control_owner`, `viewer` |
| `product_type` | `framework`, `operational`, `external` |
| `policy_type` | `POL`, `OP-POL`, `INS`, `REF`, `CTX`, `FORM` |
| `impl_type` | `UG`, `TG` |
| `compliance_status` | `compliant`, `partial`, `non_compliant`, `not_assessed`, `na` |
| `gap_severity` | `critical`, `high`, `medium`, `low` |
| `gap_status` | `open`, `in_progress`, `closed`, `accepted` |
| `assessment_type` | `detailed`, `checklist` |
| `sheet_type` | `executive_summary`, `dashboard`, `assessment`, `reference`, `config` |
| `evidence_type` | `document`, `screenshot`, `log_extract`, `config_export`, `test_result`, `attestation` |
| `mapping_type` | `maps-to`, `partially-maps-to`, `related-to`, `mitigates`, `detects`, `supports`, `depends-on`, `enables`, `feeds-into`, `implements` |
| `correlation_method` | `existence`, `keyword`, `semantic`, `manual` |
| `qa_status` | `pass`, `warning`, `fail`, `needs_review` |
| `control_group_status` | `complete`, `partial`, `basic`, `incomplete` |

---

## 4. Table Reference

### 4.1 Core

**`users`** — Platform user accounts.
```
id UUID PK | email VARCHAR(255) UNIQUE | username VARCHAR(100) UNIQUE | hashed_password VARCHAR(255)
full_name VARCHAR(200) | role user_role DEFAULT 'viewer' | is_active BOOLEAN DEFAULT true
assigned_groups UUID[] DEFAULT '{}' | last_login TIMESTAMPTZ | metadata JSONB
created_at TIMESTAMPTZ | updated_at TIMESTAMPTZ
```

**`sessions`** — Active JWT sessions.
```
id UUID PK | user_id UUID FK→users | token VARCHAR(500) UNIQUE
expires_at TIMESTAMPTZ | ip_address INET | user_agent TEXT | created_at TIMESTAMPTZ
```

---

### 4.2 Reference Frameworks

**`frameworks`** — A reference standard (ISO, NIST, MITRE, etc.).
```
id UUID PK (UUID5 from code) | code VARCHAR(50) UNIQUE | name VARCHAR(200) | version VARCHAR(20)
publisher VARCHAR(100) | source_url TEXT | description TEXT | jurisdiction VARCHAR(10)
controls_count INTEGER DEFAULT 0 | loaded_at TIMESTAMPTZ | bundle_hash VARCHAR(64) | metadata JSONB
```

**`framework_controls`** — Individual control / technique / requirement from any framework.
```
id UUID PK (UUID5 from framework_code:control_id) | framework_id UUID FK→frameworks
control_id VARCHAR(50) | parent_id UUID FK→self (hierarchy) | title VARCHAR(500) | description TEXT
control_type VARCHAR(50)[] | security_properties VARCHAR(50)[] | level INTEGER | sort_order INTEGER
metadata JSONB (framework-specific attributes)
UNIQUE (framework_id, control_id)
```

**`cross_framework_mappings`** — Mapping relationship between any two framework_controls.
```
id UUID PK (UUID5) | source_control_id UUID FK→framework_controls | target_control_id UUID FK→framework_controls
mapping_type mapping_type DEFAULT 'maps-to' | confidence DECIMAL(3,2) CHECK 0.00–1.00
source_reference VARCHAR(200) | notes TEXT | metadata JSONB
UNIQUE (source_control_id, target_control_id, mapping_type)
```

---

### 4.3 Control Groups

**`control_groups`** — One of the 54 ISMS CORE control groups (53 ISO Annex A + foundation `'00'`).
```
id UUID PK (UUID5 from group_code) | group_code VARCHAR(30) UNIQUE | name VARCHAR(200)
section VARCHAR(10) | section_name VARCHAR(50) | folder_name VARCHAR(100)
is_stacked BOOLEAN DEFAULT false | stacked_control_ids VARCHAR(10)[] DEFAULT '{}'
has_framework BOOLEAN DEFAULT true | has_operational BOOLEAN DEFAULT true
framework_status control_group_status DEFAULT 'incomplete'
operational_status control_group_status DEFAULT 'incomplete'
metadata JSONB
```

**`control_group_controls`** — Junction: ISO 27001 framework_controls → control_groups.
```
control_group_id UUID FK→control_groups | framework_control_id UUID FK→framework_controls
PRIMARY KEY (control_group_id, framework_control_id)
```

---

### 4.4 ISMS Content

**`policies`** — Governance or operational policy document.
```
id UUID PK | control_group_id UUID FK→control_groups | product_type product_type
policy_type policy_type | document_id VARCHAR(120) UNIQUE | title VARCHAR(300)
file_path TEXT | content_hash VARCHAR(64) | word_count INTEGER | requirements_count INTEGER DEFAULT 0
last_parsed TIMESTAMPTZ | language VARCHAR(5) DEFAULT 'en' | source_label VARCHAR(200) [nullable]
metadata JSONB
```
> `language`: ISO 639-1 code — `en`, `de`, `fr`, `it`. Non-en docs discovered in `de/`, `fr/`, `it/` subfolders.
> `source_label`: set only for `product_type='external'` docs (e.g. "Acme Corp"). Null for native ISMS CORE docs.

**`requirements`** — "Shall" / "should" statement extracted from a policy.
```
id UUID PK | policy_id UUID FK→policies | control_group_id UUID FK→control_groups
requirement_text TEXT | section_heading VARCHAR(200) | requirement_type VARCHAR(15) DEFAULT 'mandatory'
domain_area VARCHAR(100) | sort_order INTEGER DEFAULT 0
compliance_status compliance_status DEFAULT 'not_assessed' | evidence_count INTEGER DEFAULT 0
metadata JSONB
```

**`implementations`** — Implementation guide document (Framework product only).
```
id UUID PK | control_group_id UUID FK→control_groups | impl_type impl_type
document_id VARCHAR(120) UNIQUE | title VARCHAR(300) | file_path TEXT
content_hash VARCHAR(64) | word_count INTEGER | last_parsed TIMESTAMPTZ
language VARCHAR(5) DEFAULT 'en' | metadata JSONB
```

---

### 4.5 Generator Definitions *(Phase 7)*

**`generator_definitions`** — Structural metadata extracted from the 188 QA'd Python generator scripts. One row per generator / assessment domain.

```
id UUID PK | document_id VARCHAR(80) UNIQUE | workbook_name VARCHAR(200)
control_id VARCHAR(80) | control_name VARCHAR(300) | group_code VARCHAR(80)
control_group_id UUID FK→control_groups [nullable]
domain_number INTEGER [nullable] | domain_total INTEGER [nullable]
is_stacked BOOLEAN DEFAULT false | stacked_control_ids JSONB [nullable]
sheets JSONB DEFAULT '[]' | sheet_count INTEGER DEFAULT 0
sheet_source VARCHAR(20) [nullable] | source_file TEXT [nullable]
parsed_at TIMESTAMPTZ [nullable] | user_override BOOLEAN DEFAULT false
sheet_schemas JSONB DEFAULT '[]'
created_at TIMESTAMPTZ | updated_at TIMESTAMPTZ
```

**Key fields:**

| Field | Purpose |
|-------|---------|
| `document_id` | Business key: `ISMS-IMP-A.8.17.1`, `ISMS-IMP-A.5.1-2-6.1-2.S1` |
| `sheets` | All sheet definitions from parser: `[{"name": "Inventory", "type": "input"}, ...]` |
| `sheet_schemas` | Full column schema from live `.xlsx`: status column, DV lists, widths, freeze panes |
| `user_override` | When `true`, importer skips on re-parse (preserves manual edits via UI) |
| `is_stacked` | True if generator covers multiple ISO 27001 controls (A.5.1-2-6.1-2 etc.) |
| `stacked_control_ids` | `["A.5.1", "A.5.2", "A.6.1", "A.6.2"]` — used by form renderer to show all control refs |

**Population pipeline:**
```
50-isms-core-framework/**/SCR/generate_*.py  (188 generator scripts)
    │
    ▼
datasets/scripts/parse_generators.py
    │  → regex + AST: DOCUMENT_ID, WORKBOOK_NAME, CONTROL_ID, CONTROL_NAME
    │  → sheet names from docstring "Generated Workbook Structure:" or code wb.create_sheet()
    │
    ▼
datasets/data/generator_registry.json  (188 records)
    │
    ▼
datasets/scripts/import_generator_registry.py  → generator_definitions table
    │
    ▼                 (separate step)
datasets/scripts/extract_workbook_schema.py  → datasets/data/workbook_schemas.json
    │
    ▼
datasets/scripts/import_sheet_schemas.py  → generator_definitions.sheet_schemas JSONB
```

**Indexes:**
```sql
ix_generator_definitions_group_code
ix_generator_definitions_control_group_id
```

---

### 4.6 Assessments

**`assessments`** — Excel workbook record (Framework: 188 from SCR scripts; Operational: 53 from checklists).
```
id UUID PK | control_group_id UUID FK→control_groups | product_type product_type
assessment_type assessment_type | document_id VARCHAR(120) UNIQUE | workbook_name VARCHAR(200)
file_path TEXT | file_hash VARCHAR(64) | file_size BIGINT | sheets_count INTEGER
overall_score DECIMAL(5,2) | items_total INTEGER | items_compliant INTEGER
items_partial INTEGER | items_non_compliant INTEGER | items_na INTEGER | gaps_count INTEGER
last_generated TIMESTAMPTZ | last_parsed TIMESTAMPTZ | summary JSONB
```

**`assessment_sheets`** — One sheet within a workbook.
```
id UUID PK | assessment_id UUID FK→assessments | sheet_name VARCHAR(50)
sheet_type sheet_type DEFAULT 'assessment' | row_count INTEGER | column_count INTEGER
compliance_score DECIMAL(5,2) | metadata JSONB | created_at TIMESTAMPTZ
```

**`assessment_items`** — One row/finding within a sheet.
```
id UUID PK | sheet_id UUID FK→assessment_sheets | assessment_id UUID FK (denorm)
control_group_id UUID FK (denorm) | row_number INTEGER | item_text TEXT
status compliance_status DEFAULT 'not_assessed' | evidence_reference TEXT
owner VARCHAR(100) | due_date DATE | notes TEXT | metadata JSONB
```

---

### 4.7 Compliance

**`evidence`** — Artifact proving a requirement is met.
```
id UUID PK | control_group_id UUID FK | requirement_id UUID FK [nullable]
assessment_item_id UUID FK [nullable] | evidence_type evidence_type
title VARCHAR(300) | file_path TEXT | collected_date DATE | expires_date DATE
verified_by VARCHAR(100) | verified_date DATE | metadata JSONB
```

**`gaps`** — Compliance gap or non-conformity.
```
id UUID PK | control_group_id UUID FK | requirement_id UUID FK [nullable]
assessment_item_id UUID FK [nullable] | product_type VARCHAR(15) DEFAULT 'both'
gap_description TEXT | severity gap_severity DEFAULT 'medium'
status gap_status DEFAULT 'open' | owner VARCHAR(100) | due_date DATE
remediation_plan TEXT | closed_date DATE | closed_by VARCHAR(100) | metadata JSONB
```

---

### 4.8 QA

**`correlation_results`** — QA correlation between claimed scores and verified content.
```
id UUID PK | control_group_id UUID FK | framework_control_id UUID FK [nullable]
document_id VARCHAR(120) | correlation_method correlation_method
correlation_strength DECIMAL(3,2) | claimed_score DECIMAL(5,2) | verified_score DECIMAL(5,2)
qa_status qa_status DEFAULT 'needs_review' | coverage_keywords TEXT[] | missing_keywords TEXT[]
run_date TIMESTAMPTZ | metadata JSONB
```

---

### 4.9 System

**`audit_log`** — All platform actions for compliance audit trail.
```
id UUID PK | user_id UUID FK [nullable] | action VARCHAR(30)
resource_type VARCHAR(30) | resource_id UUID | ip_address INET | user_agent TEXT
details JSONB | created_at TIMESTAMPTZ
```

**`data_load_history`** — Framework bundle import tracking.
```
id UUID PK | bundle_type VARCHAR(50) | bundle_file VARCHAR(100) | framework_code VARCHAR(50)
version VARCHAR(50) | objects_loaded INTEGER | relationships_loaded INTEGER | bundle_hash VARCHAR(64)
load_status VARCHAR(20) DEFAULT 'pending' | load_started TIMESTAMPTZ | load_completed TIMESTAMPTZ
error_message TEXT | created_at TIMESTAMPTZ
```

---

## 5. Materialized Views

| View | Refresh Strategy | Purpose |
|------|-----------------|---------|
| `v_control_group_summary` | `REFRESH MATERIALIZED VIEW CONCURRENTLY` | Per-group compliance summary (dashboard main view) |
| `v_dashboard_compliance` | `REFRESH MATERIALIZED VIEW` (non-concurrent, no unique index) | By-section/product breakdown |
| `v_framework_coverage` | `REFRESH MATERIALIZED VIEW CONCURRENTLY` | Framework mapping coverage percentages |

Refresh triggered by `refresh_materialized_views()` function, called from:
- After any sync import completes
- `POST /api/v1/admin/reindex`
- On-demand via Admin page

---

## 6. Seed Data (Clean Install)

Applied at the end of `schemas/init_db.sql`:

**Admin user:**
```sql
email: admin@isms-core.dev | username: admin | role: admin
password: admin123 (bcrypt hash — CHANGE ON FIRST LOGIN)
```

**Foundation Policies control group:**
```sql
id: d811cb3b-959f-5d42-923d-100714c192ec  (UUID5: NAMESPACE_DNS + 'isms-core.control-group.00-foundation')
group_code: '00' | name: 'Foundation Policies' | section: '00'
folder_name: '00-foundation-policies' | has_framework: true | has_operational: false
framework_status: 'complete'
```

> Note: The Foundation group is NOT in `datasets/raw/control_groups.json` (53 ISO groups only). It is always seeded directly by `init_db.sql` and Alembic migration 001.

---

## 7. Key API → DB Mapping

| Endpoint | Primary Table | Notes |
|----------|--------------|-------|
| `GET /api/v1/controls/` | `control_groups` | Optional `?section=`, `?product=` filters |
| `GET /api/v1/controls/{id}` | `control_groups` + joins | Policies / IMPs / assessments / mappings |
| `GET /api/v1/frameworks/` | `frameworks` | 15 loaded frameworks |
| `GET /api/v1/frameworks/{id}/controls` | `framework_controls` | `?level=1` for Annex A controls |
| `GET /api/v1/frameworks/{id}/mappings` | `cross_framework_mappings` | Via framework_controls FK |
| `GET /api/v1/dashboard/overview` | `v_control_group_summary` | Mat view |
| `GET /api/v1/dashboard/coverage` | `v_framework_coverage` | Mat view |
| `GET /api/v1/generators/` | `generator_definitions` | `?section=`, `?stacked=` filters |
| `GET /api/v1/generators/form/{group_code}` | `generator_definitions.sheet_schemas` | Input sheets only — WebUI form renderer |
| `GET /api/v1/generators/{doc_id}/render` | `generator_definitions` | Jinja2 → Python script download |
| `GET /api/v1/qa/` | `correlation_results` | QA results with filters |
| `GET /api/v1/search` | OpenSearch indices | Full-text (isms-policies, isms-implementations) |
| `GET /api/v1/admin/sysinfo` | All tables | Live counts + service health |
| `GET /api/v1/admin/orphans` | `policies`, `implementations` | Documents in DB but not on filesystem |

---

## 8. OpenSearch Indices

| Index | Count | Document Fields |
|-------|-------|-----------------|
| `isms-implementations` | ~376 | `document_id`, `title`, `impl_type`, `control_group_id`, `language`, `sections[].heading/content` |
| `isms-policies` | ~143 | `document_id`, `title`, `policy_type`, `product_type`, `language`, `source_label`, `requirements[].text` |

Custom analyser: `standard + lowercase + stop(english) + snowball`. Indexing triggered inline during import — section content is NOT stored in PostgreSQL.

---

## 9. SQLAlchemy ORM Files

| File | Models |
|------|--------|
| `backend/src/domain/users.py` | `User` |
| `backend/src/domain/frameworks.py` | `Framework`, `FrameworkControl`, `CrossFrameworkMapping` |
| `backend/src/domain/control_groups.py` | `ControlGroup`, `ControlGroupControl` |
| `backend/src/domain/content.py` | `Policy`, `Requirement`, `Implementation`, `GeneratorDefinition` |
| `backend/src/domain/assessments.py` | `Assessment`, `AssessmentSheet`, `AssessmentItem` |
| `backend/src/domain/compliance.py` | `Evidence`, `Gap` |
| `backend/src/domain/qa.py` | `CorrelationResult` |
| `backend/src/domain/system.py` | `AuditLog`, `DataLoadHistory` |
| `backend/src/database/enums.py` | All 14 enum types |
| `backend/src/database/base.py` | `Base`, `TimestampMixin`, `SAEnum` helper |

---

*Schema version: 2026-03-08 (migrations 001–005). See `schemas/init_db.sql` for full DDL.*
