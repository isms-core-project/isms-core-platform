# ISMS CORE Platform — Development Log

<!--
Document ID:    ISMS-API-LOG-001
Title:          ISMS CORE Platform Development Log
Version:        0.2
Date:           2026-02-08
Updated:        2026-03-08
Owner:          Gregory Griffin
Author:         Claude Code (Opus 4.6)
Classification: Internal
Related Docs:   PLAN.md, ARCHITECTURE.md, DATA-MODEL.md
-->

---

## Log Format

Each entry records: date, session focus, decisions made, deliverables, and next steps.

---

## 2026-02-08 — Session 1: Project Kickoff & Architecture

### Context

The ISMS CORE Platform API (`60-isms-core-api/`) has existed as a deferred skeleton since early February 2026. The original decision (Option D — defer) was made when the Framework product was at 67.3% completion. Today's session re-evaluates that decision and starts Phase 0.

**Why starting now is viable:**
1. **Operational product is 100% complete** — 53/53 OP-POLs written, reviewed (S2), and 53/53 compliance checklist generators built and running.
2. **Framework Section 8 is 100%** — all 22 technological control groups are done.
3. **External validation underway** — Former CISO (GRC professional, previous employer) is reviewing Framework controls A.5.19-23 (Supplier Management), A.8.24 (Cryptography), and POL-00 (regulatory control). Potential pilot deployment at a bank (previous customer).
4. **OpenCTI production experience** — Greg runs a 32-service OpenCTI deployment with 23 connectors and 12 custom dashboards. This provides first-hand architectural knowledge.
5. **PowerBI path abandoned** — Not scriptable, too much manual work. Dashboard workbooks provide per-control aggregation but remain static files.

### Research Conducted

Comprehensive study of OpenCTI architecture across four repositories:

| Repo | What We Learned |
|------|-----------------|
| [opencti](https://github.com/OpenCTI-Platform/opencti) | Platform architecture: Node.js + GraphQL + Elasticsearch primary store + Redis + RabbitMQ. Module registration pattern. Capability-based auth. Manager pattern for background jobs. |
| [connectors](https://github.com/OpenCTI-Platform/connectors) | 128+ external import, 55+ enrichment, 6 export, 6 import, 27+ stream connectors. Four-layer separation: settings/client/converter/connector. STIX 2.1 as interchange format. |
| [datasets](https://github.com/OpenCTI-Platform/datasets) | Three-layer pipeline: raw source → generator script → STIX bundle. Stable UUIDs. Git-hosted distribution. Full-bundle upsert (no incremental diffs). |
| Greg's OpenCTI deployment | 32 services, 4-node ES cluster, 6 workers, 23 connectors (NIST, MITRE, Microsoft, Tenable, MISP, OTX), 12 custom dashboards. Split compose pattern. |

Also reviewed:
- Existing `60-isms-core-api/` skeleton (18 files: Docker infra, DB schemas, FastAPI stub, framework importer)
- Docker workspace (`factory_docker/workspace_isms_core/`) — mirror of API skeleton
- `36_correlation_qa_architecture.md` — three-tier QA methodology (existence → keyword → semantic)

### Key Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **PostgreSQL as primary store** (not Elasticsearch) | ISMS data is structured (scores, statuses, FK relationships). Search is secondary need. |
| D2 | **REST, not GraphQL** | 27 tables, one client, predictable queries. REST + Pydantic + OpenAPI auto-docs is simpler. |
| D3 | **Celery tasks, not connector containers** | Importers are internal (parse local files). Don't need container isolation or RabbitMQ. |
| D4 | **Both products as peers** | Framework and Operational share control groups but differ in policy type and workbook structure. Product toggle in UI. |
| D5 | **Docker-first deployment** | "Not everybody will setup a server." Customer mounts files, runs `docker compose up -d`. |
| D6 | **Read-only source mounts** | Platform never modifies source policies/workbooks. Ingest only. |
| D7 | **Datasets pattern from OpenCTI** | Ship reference frameworks as JSON bundles: raw → generator → data. Stable UUIDs. |
| D8 | **15 entity types** | ControlGroup, Framework, FrameworkControl, CrossFrameworkMapping, Policy, Requirement, Implementation, Assessment, AssessmentSheet, AssessmentItem, Evidence, Gap, CorrelationResult, AuditLog, User. |

### Deliverables

| File | Lines | Content |
|------|-------|---------|
| `docs/ARCHITECTURE.md` | ~450 | OpenCTI analysis, design decisions, recommended architecture, API design, risk assessment |
| `docs/DATA-MODEL.md` | ~550 | 15 entity types with attributes, relationships, UUID strategy, materialized views, index strategy, bundle format |
| `docs/PLAN.md` | ~300 | 6-phase plan, Phase 0 detailed with 13 tasks, risk register, success criteria, external inputs |
| `docs/LOG.md` | — | This file |

### Folder Structure Created

```
60-isms-core-api/
├── docs/           # Project documentation (NEW)
│   ├── ARCHITECTURE.md
│   ├── DATA-MODEL.md
│   ├── PLAN.md
│   └── LOG.md
├── datasets/       # Reference framework data (NEW)
│   ├── raw/        # Human-editable source
│   ├── scripts/    # Generator scripts
│   └── data/       # Generated JSON bundles
├── schemas/        # Data model schemas (NEW)
└── (18 existing files from original skeleton)
```

### External Context

- **CISO Review**: Former CISO reviewing A.5.19-23 (Supplier Management), A.8.24 (Cryptography), and POL-00 (regulatory). GRC professional with whom Greg has an excellent relationship beyond employer/employee. If validation is positive, potential pilot at a bank (former customer of Greg's).
- **Current employer**: CISO rejected the project for use in their ISMS setup. This redirected efforts to independent development and external validation.

### Next Steps

1. **Phase 0 execution**: Create ISO 27001 raw dataset → generator → bundle (Task 0.6)
2. **Control groups dataset**: Map all 53 groups with stable UUIDs (Task 0.7)
3. **NIST CSF 2.0 dataset**: Download from NIST API and generate bundle (Task 0.8)
4. **Continue sequentially** through Tasks 0.9–0.13

---

*End of Session 1*

---

## 2026-02-08 — Session 2: Phase 0 Dataset Execution

### Context

Continuing Phase 0 execution. Session 1 produced architecture docs. This session builds the actual datasets.

### Framework Scope Expanded

User added regulatory and security frameworks during Session 1 that must be included in the platform. Total framework count grew from 7 to 17:

| Tier | Frameworks | Rationale |
|------|-----------|-----------|
| **Foundation** | ISO 27001:2022, ISMS CORE Control Groups | Everything maps TO these |
| **Security** | NIST CSF 2.0, NIST 800-53, CIS v8, MITRE ATT&CK, OWASP (Top 10 + ASVS) | Cross-framework analysis, referenced in POLs |
| **Regulatory** | Swiss nFADP, EU GDPR, FINMA (3 circulars), NIS2, DORA, PCI DSS v4.0.1, EU AI Act | Referenced in POLs and OP-POLs, required for compliance |

### Deliverables

| File | Content | Status |
|------|---------|--------|
| `datasets/raw/iso27001_2022_controls.json` | 93 controls with full ISO 27002:2022 attributes | DONE |
| `datasets/raw/control_groups.json` | 54 groups (53 ISO + 1 regulatory A.0) | DONE |
| `datasets/scripts/generate_iso27001.py` | Raw → bundle (97 objects, 93 relationships) | DONE |
| `datasets/scripts/generate_control_groups.py` | Raw → bundle (54 objects, 94 relationships) | DONE |
| `datasets/data/iso27001_2022.json` | Generated bundle with stable UUIDs | DONE |
| `datasets/data/control_groups.json` | Generated bundle with ISO cross-references | DONE |
| Updated `docs/PLAN.md` | Expanded from 13 to 21 Phase 0 tasks | DONE |
| Updated `docs/DATA-MODEL.md` | Added 8 new frameworks to bundle list | DONE |

### Key Findings

1. **Control group count is 54, not 53**: The project consistently says "53 control groups" (ISO Annex A only). Including A.0 (regulatory, ISMS CORE-specific), the actual count is 54. Operational has 53 folders (no A.0), Framework has 54.
2. **A.6 coverage**: A.6.1 (Screening) and A.6.2 (Terms and conditions) are absorbed by the A.5.1-2 group. A.6 section only has 4 dedicated groups (A.6.3–A.6.8).
3. **Cross-section stacking**: A.5.30-8.13-14 (Business Continuity & DR) stacks controls from both A.5 and A.8 sections.
4. **PCI DSS version**: Updated to v4.0.1 (current version per PCI SSC document library).

### Next Steps

1. **NIST CSF 2.0 dataset** (Task 0.8) — download from NIST API
2. **NIST SP 800-53 R5 dataset** (Task 0.9) — download from GitHub OSCAL
3. **Continue through remaining Tier 2 and Tier 3 datasets**

---

*End of Session 2*

---

## 2026-02-08 — Session 3: Complete All Datasets (Tier 2 + Tier 3)

### Context

Continuing from Session 2 which completed Tier 1 (ISO 27001 + Control Groups) and started Tier 2. This session picks up with OWASP data quality issues flagged by the user and completes all remaining datasets.

### OWASP Top 10:2025 Correction

The user flagged that the OWASP data was wrong. Thorough online research (Feynman's Principle — verify from primary sources) revealed:

| Issue | Before | After |
|-------|--------|-------|
| **Version** | Mix of 2021/2025 data | Verified 2025 from owasp.org (RC1: Nov 2025, confirmed Jan 2026) |
| **A01:2025** | Missing SSRF absorption note | Now documents SSRF (CWE-918) consolidation from A10:2021 |
| **A02:2025** | Was "Cryptographic Failures" | Corrected: Security Misconfiguration (moved up from #5) |
| **A03:2025** | "Software Supply Chain Failures" | Verified as new category replacing A06:2021 (6 CWEs, 215K occurrences) |
| **A10:2025** | Described as "replaces SSRF" | Corrected: Entirely new "Mishandling of Exceptional Conditions" (24 CWEs) |
| **Statistics** | Missing | Added: cwes_mapped, total_occurrences, total_cves, incidence rates |
| **CWE mappings** | Missing | Added: notable_cwes per category |
| **Generator** | Referenced 2021 version, bundle metadata wrong | Fixed: version=2025, source_url updated |

### CLOUD Act Deep Verification

The CLOUD Act raw dataset had significant legal citation errors:

| Issue | Before | After |
|-------|--------|-------|
| **Section references** | `S2713(a)`, `S2713(b)`, `S2713(c)` | Section 2713 has NO subsections. Fixed: `18USC2713`, `18USC2703h2`, `18USC2703h3` |
| **Motion to quash** | Attributed to §2713 | Actually in §2703(h)(2) — different USC section |
| **Comity analysis** | 5 factors listed (included wrong "minimisation") | Corrected to 8 statutory factors per §2703(h)(3)(A)-(H) |
| **Executive agreements** | Informal ID "EXEC" | Added proper USC citation: 18 U.S.C. §2523 |
| **Signed agreements** | Not mentioned | Added UK (in force 2022-10-03) and Australia (in force 2024-01-31) |
| **Switzerland status** | Not mentioned | "No agreement exists, none in negotiation as of 2026" |
| **Enacted as** | Not documented | Division V of H.R. 1625, P.L. 115-141 |

### Other Regulatory Corrections

Verified all 8 regulatory datasets against primary sources. Fixed:
- **DORA**: Added missing Art. 21-23 (centralisation of reporting, supervisory feedback, payment-related incidents)
- **EU AI Act**: Added missing Art. 12 (Record-keeping)
- **EU GDPR**: Fixed Art. 5 title (added "of personal data")
- **Swiss nFADP, FINMA, NIS2, PCI DSS**: All verified correct

### Deliverables

| Tier | Bundles | Objects | Relationships |
|------|---------|---------|---------------|
| **Tier 1 (Foundation)** | 2 (ISO 27001 + Control Groups) | 151 | 187 |
| **Tier 2 (Security)** | 5 (NIST CSF + 800-53 + CIS + MITRE + OWASP) | 2,572 | 3,117 |
| **Tier 3 (Regulatory)** | 8 (nFADP + GDPR + FINMA + NIS2 + DORA + PCI DSS + AI Act + CLOUD Act) | 127 | 59 |
| **TOTAL** | **15 bundles** | **2,850** | **3,363** |

Generator scripts: 8 total (7 individual + 1 shared regulatory handling all 8 frameworks)

Raw datasets: 16 files (14 frameworks + control groups + ASVS)

### Key Verification Methodology (Feynman's Principle)

Every dataset was verified against primary sources, not assumed correct:
- OWASP: Scraped all 10 official category pages from owasp.org
- CLOUD Act: Verified against 18 U.S.C. §2713, §2703(h), §2523 on Cornell Law
- DORA: Cross-referenced against digital-operational-resilience-act.com full article list
- EU AI Act: Verified against ai-act-service-desk.ec.europa.eu
- FINMA: Confirmed all 3 documents on finma.ch
- PCI DSS: Verified v4.0.1 on pcisecuritystandards.org
- NIS2: Checked against nis-2-directive.com official text
- GDPR/nFADP: Cross-referenced gdpr-info.eu and fedlex.admin.ch

### Next Steps

1. **Cross-framework crosswalk** (Task 0.20) — ~1000+ mapping relationships
2. **Evolved DB schema** (Task 0.21) — `init_db.sql` matching DATA-MODEL.md
3. **Phase 1: Backend Core** — FastAPI app structure, SQLAlchemy models, CRUD API

---

*End of Session 3*

---

## 2026-02-08 — Session 4: Cross-Framework Crosswalk (Task 0.20)

### Context

Continuing from Session 3 which completed all 15 individual framework bundles (2,850 objects, 3,363 relationships). This session builds the cross-framework crosswalk — the mapping layer that ties everything together.

### Research Phase

Launched 4 parallel research agents to gather authoritative mapping data from primary sources:

| Agent | Mapping Axis | Source | Result |
|-------|-------------|--------|--------|
| **ISO ↔ NIST CSF 2.0** | 106 subcategories → Annex A | Official NIST Informative References (OLIR catalog, referenceId=154) | 244 mappings (70/93 ISO controls covered) |
| **ISO ↔ NIST 800-53 R5** | 93 ISO → NIST controls | NIST CSRC `sp800-53r5-to-iso-27001-mapping.docx` (Table 2) | 443 mappings (92/93 covered; A.6.7 only gap) |
| **CIS v8 + MITRE ATT&CK** | CIS safeguards → ISO; MITRE techniques → NIST | CIS v8.1 published mapping; CTID Mappings Explorer | CIS: 295 (153 safeguards → 58 ISO), MITRE: 614 (160 techniques → 15 NIST) |
| **ISO ↔ Regulatory** | 6 regulatory frameworks | DataGuard, NQA, ENISA, Ceeyu, ISACA published guides | 271 mappings (GDPR:57, nFADP:41, NIS2:54, DORA:50, PCI:39, AI Act:30) |

Plus inline OWASP Top 10:2025 → ISO mapping (31 mappings, 10 OWASP categories → Annex A controls).

### Data Quality

- **CIS CSV bug found and fixed**: CIS safeguard 12.5 title "Centralize Network Authentication, Authorization, and Auditing (AAA)" contained commas that broke CSV parsing. Fixed by quoting the field. All 153 rows validated after fix.
- **MITRE CSV validated**: All 160 technique IDs start with 'T', all 15 NIST controls are valid families (AC, CA, CM, CP, IA, RA, SC, SI).
- **NIST 800-53 "All XX-1" expansion**: 6 ISO controls map to all 20 XX-1 policy controls. Expanded in assembler with confidence=0.70 for policy controls, 0.85 for specific controls.
- **Partial mapping notation**: NIST asterisk (*) notation preserved as `partially-maps-to` mapping type with confidence lowered to 0.75.

### Deliverables

| File | Content |
|------|---------|
| `datasets/scripts/assemble_crosswalk_raw.py` | Assembler: reads 3 CSVs + inline NIST/regulatory/OWASP → raw JSON |
| `datasets/scripts/NIST_CSF2_to_ISO27001_2022_mapping.csv` | 106 CSF subcategories with Annex A + clause mappings |
| `datasets/scripts/CIS_v8_to_ISO27001_2022_mapping.csv` | 153 CIS safeguards → ISO controls (all 18 CIS Controls) |
| `datasets/scripts/MITRE_ATTaCK_to_NIST80053_mapping.csv` | 160 techniques (104 parent + 56 sub) → NIST controls |
| `datasets/raw/crosswalk_mappings.json` | Unified raw file: 1,898 mapping records (632 KB) |
| `datasets/data/crosswalk.json` | Generated crosswalk bundle: 1,898 objects (1,072 KB) |
| Updated `docs/PLAN.md` | Task 0.20 marked DONE, crosswalk deliverables checked off |
| Updated `docs/DATA-MODEL.md` | Bundle table + generator tree + data directory updated |

### Crosswalk Summary

```
Axis                                        Mappings
────────────────────────────────────────────────────
ISO27001_2022 → NIST_CSF_2.0                   244
ISO27001_2022 → NIST_800_53_R5                 443
ISO27001_2022 → CIS_V8                         295
NIST_800_53_R5 → MITRE_ATTACK_V18              614
ISO27001_2022 → EU_GDPR                         57
ISO27001_2022 → SWISS_NDSG                      41
ISO27001_2022 → NIS2                             54
ISO27001_2022 → DORA                             50
ISO27001_2022 → PCI_DSS_4.0.1                   39
ISO27001_2022 → EU_AI_ACT                        30
ISO27001_2022 → OWASP_TOP10_2025                 31
────────────────────────────────────────────────────
TOTAL                                         1,898
```

### Complete Phase 0 Status

| Metric | Value |
|--------|-------|
| **Bundles** | 16 (15 frameworks + 1 crosswalk) |
| **Total objects** | 4,748 |
| **Total relationships** | 3,363 |
| **Total data size** | 3.5 MB |
| **Raw data files** | 17 |
| **Generator scripts** | 11 (9 framework + 1 assembler + 1 crosswalk) |
| **Research CSVs** | 3 |

### Next Steps

1. **Evolved DB schema** (Task 0.21) — `init_db.sql` matching DATA-MODEL.md
2. **Phase 1: Backend Core** — FastAPI app structure, SQLAlchemy models, CRUD API
3. **Framework loader** — Celery task to load all 16 bundles into PostgreSQL

---

*End of Session 4*

---

## 2026-02-08 — Session 5: Evolved DB Schema (Task 0.21) — Phase 0 Complete

### Context

Final Phase 0 task. The existing SQL files (`20_init_db.sql` with 265 lines, `21_init_frameworks_db.sql` with 521 lines) used per-framework tables (20+ tables for individual frameworks). The evolved schema unifies everything into the DATA-MODEL.md pattern.

### Key Design Decision: Unified Framework Storage

**Old approach** (21_init_frameworks_db.sql):
- `iso27001_controls` table (1 table)
- `nist_csf_functions` + `nist_csf_categories` + `nist_csf_subcategories` + `nist_csf_informative_references` (4 tables)
- `nist_800_53_families` + `nist_800_53_controls` + `nist_800_53_assessment_procedures` (3 tables)
- `mitre_attack_tactics` + `mitre_attack_techniques` + `mitre_attack_technique_tactics` + `mitre_attack_mitigations` + `mitre_attack_technique_mitigations` + `mitre_attack_software` (6 tables)
- `swiss_ndsg_requirements` + `swiss_finma_requirements` (2 tables)
- `eu_gdpr_requirements` + `eu_dora_requirements` + `eu_nis2_requirements` (3 tables)
- `framework_mappings` (1 wide table with per-framework FK columns)
- Total: 20 tables, each with framework-specific columns

**New approach** (schemas/init_db.sql):
- `frameworks` (1 table — any standard/framework)
- `framework_controls` (1 table — any control/category/technique/article, with JSONB metadata)
- `cross_framework_mappings` (1 table — normalised many-to-many, any-to-any)
- Total: 3 tables, extensible to any future framework without schema changes

This matches the bundle format exactly — the framework loader can insert bundle objects directly.

### Deliverables

| File | Content |
|------|---------|
| `schemas/init_db.sql` | 844 lines, 18 tables, 14 enums, 62 indexes, 3 mat views, 11 triggers |

### Schema Breakdown

| Category | Tables | Rows in Schema |
|----------|--------|---------------|
| Core (users, sessions) | 2 | ~40 |
| Reference (frameworks, framework_controls, cross_framework_mappings) | 3 | ~75 |
| Groups (control_groups, control_group_controls) | 2 | ~40 |
| Content (policies, requirements, implementations) | 3 | ~75 |
| Assessment (assessments, assessment_sheets, assessment_items) | 3 | ~85 |
| Compliance (evidence, gaps) | 2 | ~60 |
| QA (correlation_results) | 1 | ~30 |
| System (audit_log, data_load_history) | 2 | ~40 |
| Indexes | — | ~100 |
| Materialized views | 3 | ~120 |
| Functions, triggers, enums, seed data | — | ~180 |

### Phase 0 — COMPLETE

All tasks done:

| # | Task | Status |
|---|------|--------|
| 0.1–0.5 | Project structure + docs | DONE |
| 0.6–0.7 | Tier 1: ISO 27001 + Control Groups | DONE (151 objects, 187 rels) |
| 0.8–0.12 | Tier 2: Security frameworks | DONE (2,572 objects, 3,117 rels) |
| 0.13–0.19b | Tier 3: Regulatory frameworks | DONE (127 objects, 59 rels) |
| 0.20 | Tier 4: Cross-framework crosswalk | DONE (1,898 mappings) |
| 0.21 | Evolved DB schema | DONE (844 lines, 18 tables) |

**Phase 0 totals**: 16 bundles, 4,748 objects, 3,363 relationships, 3.5 MB data, 844-line schema.

### Next Steps

**Phase 1: Backend Core** — see Session 6.

---

*End of Session 5*

---

## 2026-02-08 — Session 6: Phase 1 Backend Core — COMPLETE

### Context

Phase 0 complete (16 bundles, 4,748 objects, 844-line schema). This session implements the full FastAPI backend in 7 implementation waves.

### Implementation Waves

| Wave | Focus | Files |
|------|-------|-------|
| **1** | Foundation | `config.py`, `requirements.txt`, 11 `__init__.py` |
| **2** | Database layer | `enums.py` (14 enums), `base.py` (DeclarativeBase), `session.py` (Engine) |
| **3** | Domain models | 8 domain model files (18 SQLAlchemy tables matching init_db.sql) |
| **4** | Bundle loader | `bundle_types.py` (detection), `bundle_loader.py` (4-type loader) |
| **5** | Auth + security | `security.py` (JWT/bcrypt), `dependencies.py` (guards), `exceptions.py` |
| **6** | API routes | 6 Pydantic schema files + 5 service files + 6 route handlers + router + app factory |
| **7** | Celery + Docker | `worker.py`, `tasks.py`, `Dockerfile`, `docker-compose.yml`, Alembic config |

### Key Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Sync SQLAlchemy** (not async) | Simpler, debuggable, adequate at this scale. Uses psycopg2. |
| D2 | **Alembic stamps, doesn't create** | init_db.sql runs via Docker initdb (handles extensions, enums, mat views, functions, triggers). Alembic starts from that state with `stamp head`. |
| D3 | **Auto-seed on first boot** | Lifespan hook checks if frameworks table is empty → loads all 16 bundles synchronously. |
| D4 | **`metadata_` Python attribute** | Avoids SQLAlchemy internal clash. DB column stays `metadata` via `mapped_column("metadata", JSONB)`. |
| D5 | **`create_type=False`** for PG enums | init_db.sql already creates them. SQLAlchemy just references. |
| D6 | **Deterministic UUIDs** for bundle entities | Framework, FrameworkControl, CrossFrameworkMapping, ControlGroup use UUID5 from bundles. App-generated entities use uuid4. |
| D7 | **4 bundle types** | single-framework (12 files), multi-framework (owasp.json), control-groups, crosswalk. Loaded in FK-dependency order. |

### File Inventory

```
backend/                                    54 files total
├── Dockerfile
├── requirements.txt
├── alembic.ini
├── alembic/
│   ├── env.py
│   └── script.py.mako
├── src/
│   ├── __init__.py
│   ├── main.py                             (uvicorn entrypoint)
│   ├── app.py                              (FastAPI factory + lifespan hook)
│   ├── worker.py                           (Celery app)
│   ├── core/
│   │   ├── config.py                       (Pydantic Settings)
│   │   ├── security.py                     (JWT + bcrypt)
│   │   ├── dependencies.py                 (get_current_user, require_role)
│   │   └── exceptions.py
│   ├── database/
│   │   ├── enums.py                        (14 Python enums)
│   │   ├── base.py                         (DeclarativeBase + TimestampMixin)
│   │   └── session.py                      (Engine + SessionLocal + get_db)
│   ├── domain/
│   │   ├── __init__.py                     (model registry)
│   │   ├── users.py                        (User, Session)
│   │   ├── frameworks.py                   (Framework, FrameworkControl, CrossFrameworkMapping)
│   │   ├── control_groups.py               (ControlGroup + junction table)
│   │   ├── content.py                      (Policy, Requirement, Implementation)
│   │   ├── assessments.py                  (Assessment, AssessmentSheet, AssessmentItem)
│   │   ├── compliance.py                   (Evidence, Gap)
│   │   ├── qa.py                           (CorrelationResult)
│   │   └── system.py                       (AuditLog, DataLoadHistory)
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── common.py                       (HealthResponse, PaginatedResponse)
│   │   ├── frameworks.py
│   │   ├── control_groups.py
│   │   ├── assessments.py
│   │   └── system.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── framework_service.py
│   │   ├── control_service.py
│   │   ├── assessment_service.py
│   │   └── loader_service.py
│   ├── api/
│   │   ├── router.py                       (mounts all v1 routers)
│   │   └── v1/
│   │       ├── health.py                   (GET /health)
│   │       ├── auth.py                     (POST /login, /refresh)
│   │       ├── controls.py                 (GET /controls/)
│   │       ├── frameworks.py               (GET /frameworks/)
│   │       ├── assessments.py              (GET /assessments/)
│   │       └── admin.py                    (GET /admin/system/status, POST /admin/load)
│   └── importers/
│       ├── bundle_types.py                 (4-type detection)
│       ├── bundle_loader.py                (BundleLoader class)
│       └── tasks.py                        (Celery tasks)
└── tests/
    └── __init__.py

docker-compose.yml                          (PostgreSQL + Redis + Backend + Worker)
```

### API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/health` | No | DB ping + status |
| POST | `/api/v1/auth/login` | No | Email/password → JWT pair |
| POST | `/api/v1/auth/refresh` | No | Refresh token → new pair |
| GET | `/api/v1/controls/` | Yes | List 54 control groups (?section, ?product) |
| GET | `/api/v1/controls/{id}` | Yes | Control group detail |
| GET | `/api/v1/frameworks/` | Yes | List loaded frameworks |
| GET | `/api/v1/frameworks/{id}` | Yes | Framework detail |
| GET | `/api/v1/frameworks/{id}/controls` | Yes | Framework control tree (?level) |
| GET | `/api/v1/frameworks/{id}/mappings` | Yes | Cross-framework mappings |
| GET | `/api/v1/assessments/` | Yes | List assessments (?product) |
| GET | `/api/v1/assessments/{id}` | Yes | Assessment detail |
| GET | `/api/v1/admin/system/status` | Admin | Table counts, load history |
| GET | `/api/v1/admin/load-history` | Admin | Load history records |
| POST | `/api/v1/admin/load` | Admin | Trigger bundle loading |

### Bundle Loader Design

```
Detection:  "frameworks" key (list) → multi-framework
            "framework" key (dict) → single-framework
            "dataset" + objects[0].type == "control_group" → control-groups
            "dataset" + objects[0].type == "cross_framework_mapping" → crosswalk

Load order: 1. All frameworks (single + multi) — Framework + FrameworkControl
            2. Control groups — ControlGroup + junction rows
            3. Crosswalk — CrossFrameworkMapping (requires all FK targets)

Skip logic: content_hash comparison (bundle hash vs stored bundle_hash)
Upsert:     db.merge() (INSERT or UPDATE by PK)
Ordering:   Objects sorted by level (0→1→2) for self-referential FK in framework_controls
Junction:   control_group_controls populated from stacked_control_ids + also_covers
History:    DataLoadHistory record per bundle (status: pending → running → success/failed)
```

### Docker Stack

| Service | Image | Port | Notes |
|---------|-------|------|-------|
| isms-core-postgres | postgres:15-alpine | 5432 | init_db.sql via docker-entrypoint-initdb.d |
| isms-core-redis | redis:7-alpine | 6379 | AOF persistence, password auth |
| isms-core-backend | backend/Dockerfile | 8000 | uvicorn src.main:app |
| isms-core-worker | backend/Dockerfile | — | celery -A src.worker.celery_app worker |

### Next Steps

1. **Test**: `docker compose up -d` and verify all services healthy
2. **Verify**: GET /health → 200, POST /login → JWT, GET /frameworks/ → 15 loaded
3. **Phase 2**: Importers (policy parser, workbook parser, IMP indexer)

---

*End of Session 6*

---

## 2026-02-09 — Session 7: Docker Debugging & Phase 1 Verification

### Context

Session 6 wrote the entire backend codebase (54 files). This session built, debugged, and fully verified the Docker stack.

### Docker Stack Issues Fixed

| Issue | Symptom | Fix |
|-------|---------|-----|
| **email-validator** | ImportError on startup | Pinned `email-validator==2.1.0` in requirements.txt |
| **SQLAlchemy Enum** | `SAEnum` import error | Changed from `sqlalchemy.Enum` alias to explicit `sqlalchemy.Enum` usage |
| **Crosswalk FK violations** | 2,800+ framework_controls loaded but crosswalk mappings failed FK constraint | Fixed `generate_crosswalk.py`: use `framework_code:control_id` composite format matching what bundle_loader stores |
| **PostgreSQL version** | 15-alpine | Upgraded to **18-alpine** for latest features |
| **Redis version** | 7-alpine | Upgraded to **8-alpine** |

### Crosswalk Data Quality Fix

The crosswalk bundle referenced framework controls by `control_id` alone (e.g., `A.5.1`), but the DB `framework_controls` table uses `framework_code:control_id` composite keys (e.g., `iso27001_2022:A.5.1`). This caused all 1,898 mappings to fail FK constraint.

**Fix**: Updated `generate_crosswalk.py` to emit `source_framework_control_id` and `target_framework_control_id` in composite format. Regenerated bundle. Result: **1,898/1,898 mappings loaded, 0 orphans**.

### VERIFY.md — All 10 Steps Passing

| Step | Test | Result |
|------|------|--------|
| 1 | Docker containers healthy | 4/4 healthy |
| 2 | GET /health | 200 OK |
| 3 | POST /auth/login | JWT pair returned |
| 4 | GET /admin/system/status | 15 frameworks, 2800+ controls, 54 groups, 1898 crosswalk |
| 5 | GET /controls/ | 54 control groups listed |
| 6 | GET /frameworks/ | 15 frameworks listed |
| 7 | GET /frameworks/{id}/controls | Control tree returned |
| 8 | GET /frameworks/{id}/mappings | Cross-framework mappings returned |
| 9 | GET /assessments/ | Empty list (no workbooks imported yet) |
| 10 | Celery worker | Connected, task routing working |

### Phase 1 — COMPLETE

All backend infrastructure verified and operational. Ready for Phase 2 importers.

---

*End of Session 7*

---

## 2026-02-09 — Session 8: Task 2.1 — Policy Importer (COMPLETE)

### Context

Phase 1 backend verified. This session implements Task 2.1: parse all policy and supplementary documents from both Framework and Operational mounts into the `policies` and `requirements` tables.

### Scope Expanded During Session

Original spec: parse POL and OP-POL markdown only. During implementation:

1. **User request**: "We also have REF, CTX, FORM files" / "They belong to the POLs" → extended to all 5 document types
2. **User request**: "Maybe we create a subfolder for them so they are not in root where the english version is?" → created `de/` subfolders for 6 German translation files
3. **Watermark system**: User's idea to inject invisible HTML comment watermarks as machine-parseable identification layer

### Architecture: 3-Parser Abstraction

```
backend/src/importers/
├── parsers/
│   ├── base.py               # ABC: BasePolicyParser + ParsedPolicy dataclass
│   ├── markdown_parser.py    # Primary — watermark + bold header + Document Control
│   ├── pdf_parser.py         # pdfplumber text extraction
│   └── docx_parser.py        # python-docx paragraph/table extraction
├── policy_importer.py        # PolicyImporter orchestrator (~350 lines)
└── tasks.py                  # Celery task: import_policies
```

**ParsedPolicy** intermediate representation:
- `document_id`, `title`, `product_type`, `policy_type`, `group_code`
- `content_hash` (SHA-256), `word_count`, `sections[]`, `metadata{}`

### Watermark System

Factory-side injection script (`95-isms-core-factory/inject_policy_watermarks.py`) stamps all document markdown files with an invisible HTML comment:

```html
<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.1-4:framework:POL:a.5.1-4 -->
<!-- ISMS-CORE:REF:ISMS-REF-DORA-digital-operational-resilience-act-requi:framework:REF:dora -->
```

Tags: `POLICY` (POL + OP-POL), `REF`, `CTX`, `FORM`.

The markdown parser checks watermark first (most reliable), falls back to bold header pattern, then filename. This eliminates the regex fragility of parsing document headers.

### DE Translation Handling

6 German translation files moved to `de/` subfolders to prevent doc_id collisions:
- 5 DE POL files (A.0, A.8.17, A.8.20-22, A.8.23, A.8.24)
- 1 DE CTX file (A.8.24 Kryptographische Landschaft)

Files in `de/` subfolders get `-DE` appended to their doc_id (e.g., `ISMS-POL-A.8.24-DE`).

### REF/CTX/FORM Disambiguation

Multiple REF/CTX docs can exist per control group (e.g., two `ISMS-REF-A.8.31` files about different topics). Disambiguation via title-slug from filename:
- `ISMS-REF-A.8.31-ict-readiness-for-business-continuity`
- `ISMS-REF-A.8.31-disaster-recovery-best-practices`

Smart skip: doc_ids that already contain descriptive content (e.g., `ISMS-CTX-A.8.9-Evidence-Collection`) are not double-slugged.

### Group Code Resolution (6-Layer Fallback)

```
1. Exact match:     "a.5.1-4" → control_groups.group_code
2. A.0 regulatory:  "dora", "nis2" → A.0 group (non-"a." prefix)
3. Strip suffix:    "a.5.1-4" → "a.5.1"
4. Strip sub-part:  "a.5.1" → "a.5"
5. Compact range:   "a.5.24-28" → matches "a.5.24-28" in also_covers
6. Folder name:     parse from file path
```

### Issues Fixed During Session

| Issue | Symptom | Fix |
|-------|---------|-----|
| **5 regulatory REF errors** | DORA, NIS2, etc. group codes ("dora", "nis2") had no DB match | Added A.0 regulatory fallback for non-"a." group codes |
| **VARCHAR(50) too short** | Slugified doc_ids exceeded 50 chars | ALTER TABLE to VARCHAR(120), updated init_db.sql |
| **Title reads watermark** | `_extract_title()` parsed watermark HTML as first line | Strip watermark before content parsing |
| **14 re-imports per run** | 7 doc_id collisions (DE + REF duplicates) | `de/` subfolders + `-DE` suffix + title-slug disambiguation |
| **Double-slugging** | `ISMS-CTX-A.8.9-Evidence-Collection-evidence-collection` | Smart regex skip for already-descriptive doc_ids |
| **Stale DB records** | Old non-disambiguated records persisted | Targeted DELETE cleanup |

### Final State

```
$ curl /admin/import-policies
{
  "policies": 141,
  "requirements": 5201,
  "skipped": 0,
  "errors": 0
}

$ curl /admin/import-policies   (re-run)
{
  "policies": 0,
  "requirements": 0,
  "skipped": 141,
  "errors": 0
}
```

| Type | Product | Count |
|------|---------|-------|
| POL | framework | 69 (64 EN + 5 DE) |
| OP-POL | operational | 53 |
| REF | framework | 12 |
| CTX | framework | 7 |
| FORM | framework | 1 |
| **Total** | | **141 docs, 5,201 requirements** |

### Next Steps

1. **Task 2.4**: IMP importer — same patterns as 2.1 → see Session 9
2. **Task 2.2**: Workbook importer (Operational) — parse 53 compliance checklists
3. **Task 2.3**: Workbook importer (Framework) — parse 253 assessment workbooks

---

*End of Session 8*

---

## 2026-02-09 — Session 9: Task 2.4 — IMP Importer (COMPLETE)

### Context

Task 2.1 (Policy Importer) complete with 141 files and 5,201 requirements. User chose Task 2.4 next because it reuses the same patterns — watermarks, markdown parser, group code resolution, content hash change detection, upsert. The IMP importer targets 510 IMP-UG/TG markdown files in the Framework mount.

### Architecture: BaseImporter Refactoring

Extracted ~130 lines of shared code from PolicyImporter into a new `BaseImporter` class to avoid duplication:

```
backend/src/importers/
├── base_importer.py         # NEW — shared base class (~170 lines)
│   ├── _resolve_control_group()    # 6-layer fallback resolution
│   ├── _group_code_from_path()     # Folder name extraction
│   ├── _compact_range()            # Range normalisation
│   ├── _start/_finish/_fail_history()  # DataLoadHistory tracking
│   └── parsers dict setup          # MD/PDF/DOCX parser registry
├── policy_importer.py       # REFACTORED — extends BaseImporter
│   ├── _discover_policies()        # Framework + Operational + extra paths
│   ├── _import_single()            # Parse → upsert policy + requirements
│   └── _extract_requirements()     # shall/should sentence extraction
├── imp_importer.py          # NEW — ImpImporter class (~200 lines)
│   ├── _discover_implementations() # Framework only (Phase 1 + Phase 2 scan)
│   └── _import_single()            # Parse → upsert implementation (no requirements)
├── parsers/
│   ├── base.py              # MODIFIED — added IMP to doc_id pattern + detect_impl_type()
│   └── markdown_parser.py   # MODIFIED — added IMP to watermark/doc_id regexes
└── tasks.py                 # MODIFIED — added import_implementations_task
```

### Watermark Extension for IMP Files

Extended `inject_policy_watermarks.py` to discover and watermark IMP files:

```html
<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.24-28.S1-UG:framework:UG:a.5.24-28 -->
```

**IMP-specific group code cleanup:**
- Strip `-UG`/`-TG` suffix
- Strip `.SN` section suffix (multi-section IMPs)
- Strip `-PN` continuation suffix (multi-part A.8.8.12)

### Multi-Part Disambiguation (A.8.8.12)

A.8.8.12 has 6 IMP files (P1–P4: P1/P2 are split UG/TG, P3/P4 are unsplit continuations). Without disambiguation, multiple files would share the same doc_id.

**Fix**: Regex `r" - (P\d+) - "` on filename, appends `-PN` suffix:
- `ISMS-IMP-A.8.8.12-UG-P1`, `ISMS-IMP-A.8.8.12-UG-P2`
- `ISMS-IMP-A.8.8.12-TG-P1`, `ISMS-IMP-A.8.8.12-TG-P2`
- `ISMS-IMP-A.8.8.12-P3`, `ISMS-IMP-A.8.8.12-P4` (unsplit, classified as TG)

### API Endpoints Added

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/api/v1/admin/import-implementations` | Admin | Synchronous IMP import |
| POST | `/api/v1/admin/import-implementations/async` | Admin | Async IMP import via Celery |

### Issues Fixed

| Issue | Symptom | Fix |
|-------|---------|-----|
| **NameError: DBSession** | PolicyImporter init failed after BaseImporter refactoring | Re-added `from sqlalchemy.orm import Session as DBSession` import |
| **A.8.8.12 doc_id collision** | 6 IMP files sharing 2 doc_ids | Multi-part `-PN` suffix disambiguation |
| **ORM String(50) too short** | IMP doc_ids (e.g., `ISMS-IMP-A.8.8.12-TG-P1`) exceeded 50 chars | Changed to String(120) on both Policy and Implementation models |

### Final State

```
$ curl /admin/system/status
{
  "frameworks": 15,
  "framework_controls": 2800,
  "cross_framework_mappings": 1898,
  "control_groups": 54,
  "policies": 141,
  "requirements": 5201,
  "implementations": 510,
  "assessments": 0,
  "evidence": 0,
  "gaps": 0,
  "users": 1,
  "load_history_count": 39
}

$ curl /admin/import-implementations   (re-run)
{
  "implementations_imported": 0,
  "implementations_skipped": 510,
  "errors": 0
}

$ curl /admin/import-policies   (regression check)
{
  "policies_imported": 0,
  "policies_skipped": 141,
  "errors": 0
}
```

| Metric | Value |
|--------|-------|
| **IMP files imported** | 510 (254 UG + 254 TG + 2 unsplit P3/P4) |
| **Errors** | 0 |
| **Idempotent re-run** | 0 imported, 510 skipped |
| **Policy regression** | 0 imported, 141 skipped, 0 errors (BaseImporter refactoring clean) |

### Next Steps

1. **Task 2.2**: Workbook importer (Operational) — parse 53 compliance checklists
2. **Task 2.3**: Workbook importer (Framework) — parse 253 assessment workbooks
3. **Task 2.5**: Sync endpoint — orchestrate all importers

---

*End of Session 9*

---

## 2026-02-09 — Session 10: Task 2.4b — OpenSearch Full-Text Search (COMPLETE)

### Context

Task 2.4 (IMP Importer) complete with 510 files and 0 errors. User pointed out the original Task 2.4 spec also included OpenSearch indexing. This session adds OpenSearch 3.x to the Docker stack with full-text search capabilities.

### Docker Stack: 4 → 5 Containers

Added OpenSearch 3.4.0 as the 5th container:

| Service | Image | Port | Purpose |
|---------|-------|------|---------|
| isms-core-postgres | postgres:18-alpine | 5432 | Primary store |
| isms-core-redis | redis:8-alpine | 6379 | Celery broker + cache |
| isms-core-opensearch | opensearchproject/opensearch:3 | 9200 | Full-text search |
| isms-core-backend | backend/Dockerfile | 8000 | FastAPI app |
| isms-core-worker | backend/Dockerfile | — | Celery worker |

OpenSearch config: single-node, security plugin disabled, 512MB heap, persistent volume, health-checked.

### Search Service Architecture

Created `search_service.py` (~330 lines) as a stateless module with:

- **Client singleton** with retry: `get_client()` validates connection on each call, reconnects on failure
- **Two indices**: `isms-implementations` and `isms-policies` with custom `isms_analyzer` (standard + lowercase + stop + snowball)
- **Nested fields**: `sections` (heading/body/level) for granular search, `requirements` (text/type/section) for policy-specific search
- **Graceful degradation**: All functions return `False`/empty dict on failure — OpenSearch is optional

### Indexing Strategy

Section content from `ParsedPolicy` is available during import but NOT stored in the DB (only metadata is stored). Therefore:

1. **Inline indexing**: Both importers hook `search_service.index_*()` after DB upsert
2. **Idempotent**: Uses `document_id` as OpenSearch `_id` — re-indexing overwrites
3. **Reindex endpoint**: `POST /admin/reindex` re-parses all 651 files from filesystem mounts (bypasses DB entirely)

### API Endpoints Added

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/api/v1/search` | User | Full-text search with filters + highlights |
| GET | `/api/v1/admin/search/status` | Admin | Cluster health + index doc counts |
| POST | `/api/v1/admin/reindex` | Admin | Full re-parse + reindex from filesystem |

### Issues Fixed

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Client caching failure** | `opensearch: unavailable` after startup | Removed pessimistic `_client_checked` flag; `get_client()` retries on every call with `info()` ping |
| **307 redirect** | `GET /api/v1/search?q=...` redirected to trailing slash | Changed route from `@router.get("/")` to `@router.get("")` |
| **opensearch-py 2.x incompatible** | OpenSearch 3.x requires opensearch-py 3.x | Upgraded from 2.4.2 to 3.1.0 |

### Verification

```
$ curl /admin/reindex
{"status":"ok","stats":{"implementations":510,"policies":141,"errors":0}}

$ curl /api/v1/search?q=cryptography&limit=3
{
  "total": 123,
  "hits": [
    {"document_id": "ISMS-POL-A.8.24", "title": "Use of Cryptography", "score": 6.634, ...},
    {"document_id": "ISMS-OP-POL-A.8.24", "title": "Use of Cryptography", "score": 6.634, ...},
    {"document_id": "ISMS-CTX-A.8.24-cryptographic-landscape-reference", "score": 5.271, ...}
  ],
  "took_ms": 226,
  "available": true
}

$ curl /health
{"status":"ok","database":"ok","opensearch":"ok","version":"1.0.0"}

$ curl /admin/search/status
{"available":true,"cluster_status":"green","indices":{"isms-implementations":510,"isms-policies":141}}
```

### Files Created/Modified

| File | Action | Lines |
|------|--------|-------|
| `docker-compose.yml` | Modified | +20 (OpenSearch service + volume + env) |
| `backend/requirements.txt` | Modified | opensearch-py 2.4.2 → 3.1.0 |
| `backend/src/services/search_service.py` | Created | ~330 |
| `backend/src/schemas/search.py` | Created | ~30 |
| `backend/src/api/v1/search.py` | Created | ~55 |
| `backend/src/api/router.py` | Modified | +1 (search import + mount) |
| `backend/src/importers/base_importer.py` | Modified | +12 (_get_group_name) |
| `backend/src/importers/imp_importer.py` | Modified | +20 (search indexing hook) |
| `backend/src/importers/policy_importer.py` | Modified | +25 (search indexing hook) |
| `backend/src/api/v1/admin.py` | Modified | +135 (reindex + search status) |
| `backend/src/app.py` | Modified | +10 (OpenSearch in lifespan) |
| `backend/src/schemas/common.py` | Modified | +1 (opensearch field) |
| `backend/src/api/v1/health.py` | Modified | +3 (OpenSearch health) |

### Next Steps

1. **Task 2.2**: Workbook importer (Operational) — parse 53 compliance checklists
2. **Task 2.3**: Workbook importer (Framework) — parse 253 assessment workbooks
3. **Task 2.5**: Sync endpoint — orchestrate all importers

---

*End of Session 10*

---

## 2026-02-09 — Session 11: Task 0.22 — Control Dependencies Dataset + Graph Feature Planning

### Context

Task 2.4b (OpenSearch) complete. User asked about adding a relational graph view showing how ISO 27001 controls are interconnected — e.g., A.5.19-23 (Supplier Management) linked to A.5.30-8.13-14 (BC/DR), or A.8.24 (Cryptography) used across many controls. This is valuable for CISOs understanding control interdependencies.

### Research Phase

Launched 2 parallel research agents:

| Agent | Focus | Result |
|-------|-------|--------|
| **ISO 27001 inter-control dependencies** | ISO 27002:2022 cross-references, operational capability groupings, practitioner implementation ordering | ~300 relationships identified across 5 types: depends-on, enables, feeds-into, supports, implements |
| **Graph visualization best practices** | GRC platform analysis, library comparison | Cytoscape.js recommended over ReactFlow (canvas renderer, 2000+ nodes, built-in graph algorithms, compound nodes) |

### Design Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | **Reuse cross_framework_mappings table** | Both source and target are ISO 27001 framework_controls. No new tables needed — just new mapping_type enum values. |
| D2 | **4 new mapping_type enum values** | `depends-on`, `enables`, `feeds-into`, `implements` added to both PostgreSQL and Python enums. `supports` already existed. |
| D3 | **Cytoscape.js over ReactFlow** | Canvas-based rendering handles 2000+ nodes. Built-in graph algorithms (shortest path, centrality). Compound nodes for control groups. CSS-like selectors for filtering. |
| D4 | **Bundle loader supports N crosswalk bundles** | Changed `xw_bundle` (single tuple) to `xw_bundles` (list) so both `crosswalk.json` and `control_dependencies.json` load. |
| D5 | **Build dataset now, defer API + frontend** | Dataset is a Phase 0 extension (Task 0.22). Graph API is Phase 3 (Task 3.10). Cytoscape.js frontend is Phase 4 (Task 4.13). |

### High-Impact Cross-Cutting Controls

Analysis of the dependency graph reveals these controls as the most connected nodes:

| Control | Role | Inbound | Outbound |
|---------|------|---------|----------|
| **A.5.1** (Policies) | Foundation | 2 | 0 |
| **A.5.9** (Asset Inventory) | Foundation | 12 | 8 |
| **A.5.12** (Classification) | Hub | 10 | 8 |
| **A.5.15** (Access Control) | Hub | 12 | 5 |
| **A.8.15** (Logging) | Hub | 6 | 8 |
| **A.8.24** (Cryptography) | Cross-cutting | 4 | 11 |
| **A.8.9** (Config Mgmt) | Foundation | 7 | 6 |
| **A.5.31** (Legal) | Foundation | 4 | 3 |

### Deliverables

| File | Action | Content |
|------|--------|---------|
| `datasets/raw/control_dependencies.json` | Created | 229 curated dependencies (88 depends-on, 26 enables, 22 feeds-into, 90 supports, 3 implements) |
| `datasets/scripts/generate_control_dependencies.py` | Created | Raw → bundle generator (same UUID strategy as crosswalk) |
| `datasets/data/control_dependencies.json` | Generated | Bundle with 229 cross_framework_mapping objects |
| `backend/src/database/enums.py` | Modified | Added 4 MappingType values: DEPENDS_ON, ENABLES, FEEDS_INTO, IMPLEMENTS |
| `schemas/init_db.sql` | Modified | Added 4 mapping_type enum values |
| `backend/src/importers/bundle_loader.py` | Modified | `xw_bundle` → `xw_bundles` (list), loop over N crosswalk bundles |
| `docs/PLAN.md` | Modified | Task 0.22 added, Phase 3 Task 3.10 (Graph API), Phase 4 Task 4.13 (Cytoscape.js) |
| `docs/ARCHITECTURE.md` | Modified | ReactFlow → Cytoscape.js, added /graph/ endpoint |

### Dependency Type Distribution

```
Type                Count
────────────────────────────
depends-on             88
supports               90
enables                26
feeds-into             22
implements              3
────────────────────────────
TOTAL                 229
```

### Graph API Endpoint (Phase 3, Task 3.10)

Planned endpoint shape:

```
GET /api/v1/graph?center=A.5.15&depth=2&edge_types=depends-on,enables&section=A.8
```

Response: `{ nodes: [...], edges: [...], stats: {...} }` — Cytoscape.js-compatible format.

### Next Steps

1. **Task 2.2**: Workbook importer (Operational) — parse 53 compliance checklists
2. **Task 2.3**: Workbook importer (Framework) — parse 253 assessment workbooks
3. **Task 2.5**: Sync endpoint — orchestrate all importers

---

*End of Session 11*

---

## 2026-02-09 to 2026-03-08 — Sessions 12–42: Platform Build (Phases 2–6)

> Note: Detailed per-session entries for Sessions 1–11 are above. Sessions 12–42 are recorded here as a consolidated summary due to the volume of work. See PLAN.md for full task-level detail per phase.

### Phase 2 Completion (Sessions 12–18, Feb 2026)

| Task | Deliverable | Sessions |
|------|------------|---------|
| 2.2 Operational Workbook Importer | Parse 53 checklists → 543 sheets, 2,591 items | 12–13 |
| 2.3 Framework Workbook Importer | Parse 188 assessment workbooks → 959 sheets (generator script parsing) | 14–15 |
| 2.5 Sync endpoint | `POST /api/v1/sync/full` + `/async` variant | 15 |
| 2.1 Policy importer fixes | Title parser hardened; `-DE` suffix; 6-layer group code resolution; INS type added | 16–17 |
| Foundation group | `00 — Foundation Policies` ControlGroup seeded permanently; `a.0` fake group removed | 17 |
| 118 new crosswalk mappings | 36 MITRE ATT&CK, 22 OWASP ASVS 4.0, 60 FINMA | 18 |

**Phase 2 final stats**: 143 policies, 376 IMPs, 241 assessments (188 Framework + 53 Operational), 0 errors.

### Phase 3 — Dashboard API (Sessions 19–23, Feb 2026)

All dashboard endpoints built and live:
- `GET /dashboard/overview` — compliance overview, 6 metric cards, audit readiness
- `GET /dashboard/coverage` — framework mapping matrix (2,127 mappings, 14 frameworks)
- `GET /dashboard/gaps` — gap analysis by severity/status/product
- `GET /dashboard/evidence` — evidence coverage + freshness
- `GET /dashboard/audit-readiness` — composite score: policies + evidence + assessments + gaps
- `GET /controls/{id}` — rich control detail view (both products side-by-side)
- `GET /graph` — control dependency graph (Cytoscape.js-ready, center/depth/section/edge_types filters)

### Phase 4 — React Frontend (Sessions 24–32, Feb–Mar 2026)

Full React 19 + MUI 6 + Vite frontend built. Pages: Login, Overview, Controls, Control Detail (tabbed), Policies, Assessments, Coverage, Gaps, Evidence, Search, Graph, QA, Admin, System.

Key additions in later sessions:
- **DocPreviewDrawer**: click any POL/INS/IMP card → rendered markdown in right drawer
- **Coverage Gaps section**: Framework/Operational toggle, clickable rows → controls
- **Gaps page**: full CRUD (create, inline edit, delete with confirm, status/severity/product filters, overdue detection)
- **Admin page**: user CRUD (Add User dialog, Edit User dialog with role/active/password, Delete button)
- **Evidence expiry banner**: client-side alert (error=expired, warning=≤30 days)
- **System page** (`System.tsx`): 5 service health cards, DB record counts, OpenSearch index stats, platform config, last sync, orphan scanner widget

### Phase 5 — Correlation Engine (Sessions 33–36, Mar 2026)

| Task | Deliverable |
|------|------------|
| 5.1 Existence checker | `qa_service.py` + `GET/POST /api/v1/qa/*` + `QA.tsx` page |
| 5.2 Keyword correlation | ISO keyword coverage via OpenSearch + synonym rules |
| 5.3 Semantic (Mini LLM) | Cosine similarity via sentence-transformers (all-MiniLM-L6-v2) |
| 5.4 Semantic (Claude AI) | Claude Haiku alignment scoring with reasoning + gap chips |
| 5.5 ISO dataset enrichment | All 93 Annex A controls enriched with ISO 27002 descriptions |
| 5.6 Synonym rules CRUD | Admin-managed keyword synonym table |

Results: Framework 54/54 PASS (100%), Operational 53/53 WARNING (assessments present, no OP-POL re-imported yet).

### Phase 6 — External Document Support (Sessions 37–41, Mar 2026)

Complete external/third-party document ingestion:
- `ProductType.EXTERNAL` enum value + Alembic migration
- `source_label` + `language` fields on `policies` table
- `ExternalDocImporter` with relaxed parser (no watermark required)
- `POST /admin/import-external` upload endpoint + Policies page upload dialog
- Amber "External Document — [source]" banners in ControlDetail, Policies, QA
- FR + IT subfolder discovery (extends existing DE support)
- Language filter in Policies page + QA table
- ISO 27017, 27018, 27701 added to framework datasets

### New Admin Endpoints (across sessions, not in PLAN.md v0.2)

| Endpoint | Added | Purpose |
|----------|-------|---------|
| `GET /admin/sysinfo` | Session 36 | Service health, DB counts, OpenSearch stats, platform config |
| `GET /admin/orphans` | Session 39 | Scan DB for records whose file_path no longer exists on disk |
| `DELETE /admin/orphans` | Session 39 | Purge those orphan records |
| `POST /admin/reindex` | Session 35 | Rebuild OpenSearch indices from DB |
| `POST /admin/reset-content` | Session 34 | Wipe + re-import all policies/IMPs/assessments |

### IMP/POL Document ID Normalisations (Mar 2026)

Three stacked controls had inconsistent naming in IMP files and POLs. Corrected:

| Control | Old ID pattern | Correct ID pattern |
|---------|---------------|-------------------|
| A.5.19–23 Cloud Services | `ISMS-IMP-A.5.23.SN-{type}` | `ISMS-IMP-A.5.19-23.SN-{type}` |
| A.7.1–3 Physical Access | `ISMS-IMP-A.7.1-2-3-SN-{type}` | `ISMS-IMP-A.7.1-3.SN-{type}` |
| A.8.20–22 Network Security | `ISMS-IMP-A.8.20-21-22.SN-{type}` | `ISMS-IMP-A.8.20-22.SN-{type}` |

All 24 IMP files renamed, watermarks corrected, POL cross-references updated, WKBK xlsx renamed, SCR generators updated, folder names corrected (A.7 only — was `isms-a.7.1-2-3-*`, now `isms-a.7.1-3-*`). Orphan DB records purged after each rename via the new orphan scanner.

---

*Sessions 12–42 summary complete. Next: Phase 7 (Assessment Content Bootstrap).*

---

## 2026-03-10 — Phase 7 Validation: Script Regeneration End-to-End Confirmed

### Milestone

Full round-trip pipeline validated in production:

1. **Original "manual" generators** (`SCR_N/generate_*.py`) — 188 hand-crafted Python scripts, QA'd and promoted Feb–Mar 2026
2. **Workbook import** — 188 workbooks parsed into PostgreSQL (sheets, columns, DV values, compliance items, scores)
3. **Jinja2 Gold Standard template** — rebuilt to faithfully reproduce the SCR_N generator structure (sheet layout, formulas, formatting, openpyxl patterns)
4. **Script regeneration** — `<>` button in Assessment Form Drawer downloads a `.py` generated from DB via Jinja2
5. **Local execution** — regenerated script run on macOS produces correct `.xlsx` with identical structure to original manual generator

**Test case:** `ISMS-IMP-A.5.23.S1` — Cloud Service Inventory & Classification
- Regenerated script: `generate_isms_imp_a_5_23_s1.py` (68 KB)
- Output workbook: `ISMS-IMP-A.5.23.S1_Cloud_Service_Inventory_&_Classification_20260310.xlsx` (50 KB, 10 sheets)
- Result: matches original manual generator output — all sheets present, correct structure

**Significance:** Phase 7 script regeneration is production-validated. The platform can now regenerate any of the 188 generator scripts from DB data, closing the loop between static files and live platform.

Archive location: `96-isms-core-audit-qa-reports/isms-core-framework/scr-qa-03-2026/`

---

## 2026-03-09 — Sessions 43–46: Phase 10 — Privacy & Cloud Platform Integration

### Context

Phase 10 content (PRIV-POL + CLD-POL) was complete. Goal: integrate Privacy (ISO 27701:2025, 21 groups) and Cloud (ISO 27018:2025, 12 groups) into the live platform end-to-end — DB, API, QA, and frontend.

### Deliverables

**Database Migrations**
- `014_cloud_groups` — 12 ISO 27018 control groups (`product_family='CLOUD'`, codes `cld-a.1` through `cld-a.12`)
- `015_privacy_groups` — 21 ISO 27701 control groups (`product_family='PRIVACY'`, codes `priv-a.1.x` through `priv-a.3.x`)

**Backend Fixes**
- `control_service.py` — `list_control_groups()` accepts and filters by `product_family`
- `qa_service.py` — Existence check covers all 3 product families; Keyword/Semantic restricted to `ProductFamily.ISMS` (no ISO 27001 keywords/UG-TG for privacy/cloud); product label stored in metadata
- `dashboard_service.py` — All dashboard metrics (`get_overview`, `get_audit_readiness`, `get_coverage_gaps`, `get_evidence_status`) filter to `_ISMS_ONLY` via `ControlGroup.product_family == ProductFamily.ISMS`
- `schemas/qa.py` — Added `privacy: QASummaryBucket` and `cloud: QASummaryBucket` to `QASummary`
- `api/v1/qa.py` — 4-bucket summary (framework/operational/privacy/cloud); `_BUCKET_MAP` dict for correct routing; `product_type` filter param

**Policy Import**
- 23 PRIV-POL + 12 CLD-POL imported into DB + OpenSearch via `POLICY_EXTRA_PATHS` volume mounts
- `docker-compose.yml` — Added `../51-isms-core-privacy:/app/isms-privacy:ro` + `../52-isms-core-cloud:/app/isms-cloud:ro` + `POLICY_EXTRA_PATHS` env var

**Frontend**
- `Controls.tsx` — Always passes explicit `product_family` (ISMS/PRIVACY/CLOUD) to prevent section code pollution (ISO 27018 uses A.6/A.7/A.8 codes that overlap with ISMS)
- `controls.ts` — Param renamed `product_type` → `product` to match backend
- `Search.tsx` — Product filter dropdown (All/ISMS Framework/ISMS Operational/Privacy/Cloud)
- `QA.tsx` — Keyword subtitle mentions all 3 standards; product filter re-enabled for keyword/semantic; 4 summary cards; chip colours per product
- `Sidebar.tsx` — Product switcher dims on platform pages; nav highlight uses fixed neutral colour `#6B7A99` for platform pages
- `App.tsx` — Login subtitle updated to list all 3 covered standards

**QA Results After Integration**
- Existence: 140/140 PASS (54 ISMS FW + 53 ISMS OP + 21 PRIVACY + 12 CLOUD)
- Keyword: 54/54 PASS (ISMS framework only)

---

## 2026-03-10 — Session 47: UI Product-Scoping Fixes (All 3 ISOs)

### Context

Post-integration QA: several pages still showed ISMS-specific content (Framework/Operational cards, ISMS control groups) when switched to PRIVACY or CLOUD.

### Fixes Applied

**Search — moved to Platform nav**
- Removed from `PRODUCT_NAV` (per-ISO); added to `NAV_PLATFORM` (platform-wide)
- Added `/search` to `PLATFORM_PATHS` so product switcher dims correctly
- Home page: prominent search bar navigates to `/search?q=…`; `Search.tsx` reads `?q=` on load via `useSearchParams`

**QA (`QA.tsx`)**
- `METHOD_SUBTITLES` for keyword updated to mention all 3 standards
- `PRODUCT_TYPE_COLOR` map covers `isms`/`privacy`/`cloud` product_type values
- Product filter reset to `'all'` on method switch (was hardcoded to `'framework'`)

**System page (`System.tsx`)**
- Import Policies description updated to include PRIV-POL/CLD-POL
- Removed step number circles from all 5 import items
- Removed hardcoded document counts from descriptions

**Report page (`Report.tsx`)**
- Added ISO product selector (ISMS / Privacy / Cloud toggle buttons)
- Privacy/Cloud: Executive Summary with composite score (policy% + IMP% / 2) + per-group coverage table grouped by section

**Gaps page (`Gaps.tsx`)**
- `CreateGapDialog` — control group dropdown now filtered to active `product_family`

**Evidence page (`Evidence.tsx`)**
- `UploadDialog` — Product options scoped per active ISO: Framework + Operational for ISMS; single Privacy or Cloud option for others

**Policies page (`Policies.tsx`)**
- Metric cards: ISMS shows Framework + Operational; PRIVACY shows Privacy card; CLOUD shows Cloud card
- Subtitle shows correct standard (ISO 27701:2025 / 27018:2025) per active product
- Type filter dropdown: ISMS shows POL/OP-POL/INS/REF/CTX/FORM; PRIVACY shows PRIV-POL; CLOUD shows CLD-POL; resets on product switch
- `productChipStyle()` — correct colours for privacy/cloud chips

**Assessments page (`Assessments.tsx`)**
- New Assessment dialog: hides Framework/Operational type cards for PRIVACY/CLOUD; shows single product card with correct standard label
- Control group dropdown in dialog: uses `product_family` filter (ISMS groups for ISMS, etc.)
- `assessmentsApi.list()` — scoped by `product_family`; query key includes `product` to refetch on switch
- Platform Assessments + Workbook Library scoped to active product (no cross-product pollution)
- Chip colours fixed for privacy/cloud product types in both Platform cards and Library table
- Workbook Library count chip shows `filteredLibrary.length` (not total `library.length`)

**Backend**
- `assessment_service.py` — `list_assessments()` accepts `product_family` param; filters via `ControlGroup.product_family == ProductFamily(value.upper())`
- `api/v1/assessments.py` — exposes `product_family` query param
- `assessmentsApi.ts` — `list()` signature updated to `{ product?, product_family? }`

### Key Bug Fixed
`ProductFamily` is `str, enum.Enum`. SQLAlchemy requires comparison via `ProductFamily(value.upper())` enum member — raw string comparison silently returns zero rows.

---

## 2026-03-10 — Session 48: Dashboard Stats Audit + Doc Updates

### Context

Full stats audit of the ISMS compliance dashboard following visual anomalies spotted in the Coverage Radar, Maturity Profile, and Section Breakdown charts. Multiple overcounting bugs found and fixed across `dashboard_service.py` and `Overview.tsx`.

### Bugs Found and Fixed

**1. Section coverage percentage > 100% (backend)**
`fw_cov` in `get_overview()` section loop was counting `func.count(Policy.id)` — total policies per section. Groups with multiple policy files (POL + REF + CTX + INS) gave counts above the number of control groups → A.0 = 1100%, A.5 = 152%, A.8 = 182%.
Fix: `func.count(Policy.id)` → `func.count(func.distinct(Policy.control_group_id))`

**2. Coverage Radar '00' spike (frontend)**
Radar filter used `s.section !== 'A.0'` but the foundation group's section code in the DB is `'00'`, not `'A.0'`. Foundation group (1 control, 11 policies → 1100% framework coverage) was included in the radar, collapsing the entire chart.
Fix: `filter((s) => !['A.0', '00'].includes(s.section))` — applied to radar data, bar data, and Section Breakdown table.

**3. LinearProgress overflow (frontend)**
Section Breakdown used `value={s.framework_pct}` directly on `LinearProgress`. MUI's LinearProgress does not clamp > 100 values visually.
Fix: `value={Math.min(100, s.framework_pct)}` for both framework and operational bars.

**4. UG/TG counting all 87 groups instead of 54 ISMS (backend)**
`_count_distinct_groups()` helper has no join — UG/TG queries counted distinct `control_group_id` across all implementations regardless of product family. With 87 groups having UG/TG records: 87/54 = 161%.
Fix: Replaced `_count_distinct_groups` calls for UG/TG with explicit JOIN to `ControlGroup` + `_ISMS_ONLY` filter — in both `get_overview()` and `get_audit_readiness()`.

**5. Implementations metric card showing 444 (backend)**
`total_implementations = select(func.count()).from(Implementation)` — no product family filter. 444 = 378 ISMS + 66 privacy/cloud implementations.
Fix: Added JOIN to `ControlGroup` + `_ISMS_ONLY` filter → now shows 378.

**6. Evidence queries not scoped to ISMS (backend)**
`get_evidence_status()` and `get_audit_readiness()` evidence counts used `select(func.count(func.distinct(Evidence.control_group_id)))` with no product family filter. Evidence items on privacy/cloud groups would pollute ISMS coverage %.
Fix: Added JOIN to `ControlGroup` + `_ISMS_ONLY` to both evidence count queries. `get_evidence_status()` rows query also filtered to ISMS groups only.

### Doc/Content Updates

- `factory_isms/PARADIGM.md` — Updated TL;DR, "What Is ISMS CORE" section, and variant comparison to reflect all four products (Framework, Operational, Privacy, Cloud) and three ISO standards (27001, 27701, 27018)
- `factory_isms/PLATFORM.md` — Status Live (Phase 8); control groups 53→87; PRIV/CLD IMP docs + SCR generators moved from Planned to Current; all data sources listed; only Script Regeneration remains Planned
- `factory_isms/GETTING-STARTED.md` — Privacy + Cloud volume mounts; import-privacy step; all four mount troubleshooting checks; `POLICY_EXTRA_PATHS` env var

### Generator Bugs Fixed (factory_claude_ai)

**A.7.10 (×3 generators):** `sys.exit(True)` = exit code 1. Fixed `return True/False` → `return 0/1`.
**A.8.9 (×3 generators):** Post-write verification used `FILENAME` (with `_Assessment_` suffix) but file saved as `OUTPUT_FILENAME` — `FileNotFoundError` in `os.path.getsize()`. Fixed to use `OUTPUT_FILENAME` consistently.

### Workbooks Regenerated

All 188 framework workbooks regenerated with `_20260310` date stamp. Old `_20260301` and `_20260307` files cleaned from `factory_isms`. All 188 generators ran OK (6 false subprocess failures — all files created correctly, root cause fixed in A.7.10 generators above).

### DB State After Session

| Entity | Count |
|--------|-------|
| control_groups | 87 (54 ISMS + 21 PRIVACY + 12 CLOUD) |
| policies | 181 (93 framework + 53 op + 23 privacy + 12 cloud) |
| implementations | 444 total (378 ISMS + 66 privacy/cloud) |
| assessments | 286 (199 fw + 54 op + 21 privacy + 12 cloud) |

### Next Session

- ISMS Copilot gap analysis — run all 35 PRIV + CLD policies through Compass
- SCR generators for 21 PRIV control groups (next build sprint)

---

## 2026-03-11 — Session 49: Fresh Deploy Validation + Importer Cross-Product Fix

### Context

Full fresh deploy test (docker compose down -v → up from scratch) revealed a critical importer bug causing silent misrouting of all ISMS content to CLOUD/PRIVACY control groups.

### Root Cause

`_resolve_control_group()` in `base_importer.py` had no product-family awareness. On first deploy, ISMS control groups are not in the DB until `/admin/load` runs. If content importers ran before `/admin/load`, the sub-part fallback stripped suffixes from ISMS group codes (e.g. `a.5.14` → `a.5`) and matched CLOUD groups (ISO 27018 has an `a.5` group). All 42 policies, 12 implementations, and 175 assessments were misrouted to non-ISMS groups. Subsequent import runs skipped these files (same content hash), leaving 26 ISMS control groups with no framework policies in the dashboard.

### Fix: Proper architectural solution

**`base_importer.py`:** `_resolve_control_group()` now accepts `preferred_family: ProductFamily | None`. On cache build, creates per-family sub-caches alongside the global cache. All resolution steps (exact, section-strip, sub-part, compact-range, also-covers) try the preferred family first — global cache only as last resort.

**All five importers (policy, imp, framework, operational, privacy):** Pass explicit `preferred_family` (ISMS/PRIVACY/CLOUD) to all `_resolve_control_group()` calls. Added pre-flight guard: each importer now raises `RuntimeError` if ISMS control groups aren't seeded yet, giving a clear actionable error instead of silent misrouting.

### Correct bootstrap order (fresh deploy)

```
1. docker compose up -d
2. docker exec isms-core-backend alembic upgrade head
3. POST /api/v1/admin/load                    ← MUST be first (seeds ISMS groups)
4. POST /api/v1/admin/import-policies
5. POST /api/v1/admin/import-implementations
6. POST /api/v1/admin/import-operational
7. POST /api/v1/admin/import-privacy
8. POST /api/v1/admin/import-framework-workbooks
9. POST /api/v1/admin/reindex
```

### DB State After Session

| Entity | Count |
|--------|-------|
| control_groups | 87 (54 ISMS + 21 PRIVACY + 12 CLOUD) |
| policies | 180 (92 framework + 53 op + 23 privacy + 12 cloud) |
| implementations | 444 total (378 ISMS + 66 privacy/cloud) |
| assessments | 275 (ISMS+PRIVACY+CLOUD) |

### Dashboard stats (verified clean after fix)

| Metric | Value |
|--------|-------|
| Controls | 54 |
| Policies | 145 (ISMS only) |
| Implementations | 378 (ISMS only) |
| Assessments | 242 (FW+OP) |
| FW has_policy | 54/54 |
| FW UG/TG | 54/54 |
| FW coverage | 100% |
| Audit readiness | 80% (green) |

### Commit

`e6eb44b6` — fix(importers): prevent cross-product group misrouting on fresh deploy

---

## 2026-03-14 — Sessions 50–51: v2.0 Connector Build Sprint + System Infrastructure

### Context

Two sessions focused on: (1) completing the connector library build sprint, and (2) hardening the platform infrastructure for test and production deployments.

### Connector Build Sprint

#### Phase 3g — Extended Connector Library

Built 24 additional connectors completing the full v2.0 connector library. All connectors follow the shared `runner.py` single-container orchestrator pattern — one runner container loads all connector modules dynamically, no per-connector Docker build required.

**Connectors added this sprint:**

| Connector | Controls Covered |
|-----------|-----------------|
| Microsoft 365 (o365) | a.5.15 / a.5.16 / a.5.18 / a.8.1-7-18-19 / a.8.5 / a.8.7 |
| Azure CSPM | a.8.8 / a.5.9 / a.8.20-22 / a.8.5 |
| Generic SIEM | a.8.15 / a.8.16 |
| Threat Intelligence Feed | a.8.16 / a.5.7 |
| Devolutions Server | a.8.2-3-5 / a.5.15-16-18 / a.5.3 / a.8.15 |
| Wazuh XDR | a.8.1-7-18-19 / a.8.7 / a.8.8 |
| Graylog | a.8.15 / a.8.16 |
| AWS Security Hub | a.8.8 / a.8.20-22 |
| GCP Security Command Centre | a.8.8 / a.5.9 |
| Microsoft Purview | a.8.10 / a.8.12 |
| NetBox | a.5.9 / a.8.20-22 |
| GLPI | a.5.9 / a.5.24-28 |
| Zabbix | a.8.16 |
| SentinelOne | a.8.1-7-18-19 |
| OpenVAS / Greenbone | a.8.8 / a.5.9 |
| Tenable.io (cloud) | a.8.8 / a.5.9 |
| Qualys VMDR | a.8.8 / a.5.9 |
| CrowdStrike Falcon | a.8.1-7-18-19 / a.8.8 |
| CyberArk PAS | a.8.2-3-5 |
| HashiCorp Vault | a.8.2-3-5 |
| Keycloak | a.5.15 / a.5.18 |
| Authentik | a.5.15 / a.5.18 |
| OpenLDAP | a.5.15 / a.5.18 |
| FreeIPA | a.5.15 / a.5.18 |
| Fortinet FortiAnalyzer | a.8.15 / a.8.16 |
| Fortinet FortiManager | a.8.20 / a.8.22 |
| GitHub | a.8.32 / a.8.25 |
| GitLab | a.8.32 / a.8.25 |
| Zscaler | a.6.7 / a.8.20 |

Total connector library: **39+ systems** across identity, endpoint, network, vulnerability, ITSM, SIEM, cloud posture, and threat intelligence categories.

#### EvidenceDetailView

Added `EvidenceDetailView` component to `ControlDetail.tsx` Automated Evidence tab for o365, azure-cspm, siem, and threat-intel connectors. Shows connector evidence items with: source label, classification chip, status chip, raw JSON viewer, OpenInNew link. Auto-refreshes every 60s.

#### Celery Beat — Nightly Evidence Archive

Added `archive_evidence_beat` Celery task in `backend/src/importers/tasks.py`:
- Schedule: `crontab(hour=2, minute=0)` (02:00 UTC nightly)
- Calls `connector_service.archive_old_evidence()`
- Writes result to `audit_log` with `category='system'` (SEV_INFO or SEV_WARNING if records archived)
- Registered in `worker.py` beat schedule as `evidence-archive-nightly`

#### System Event Log

Added System Event Log section to `frontend/src/pages/System.tsx`:
- Queries `GET /api/v1/admin/audit-log?category=system&page_size=30`
- Displays time, event_type, severity chip, description
- Auto-refreshes every 60s alongside existing container status

#### Connector Audit Logging

Added `log_event()` calls throughout `backend/src/api/v1/connectors.py` for: `trigger_sync`, `report_error`, `ingest_evidence`, `run_archive`, `purge_archived`. All use `category=CAT_SYSTEM`, appropriate severity.

### Infrastructure: NUC-01 Test Deployment

Deployed v2.0 stack to NUC-01 (`61-isms-core-api-test`, `/home/srv_admin/isms-core-test`).

#### entrypoint.sh — Alembic Auto-Stamp Fix

Root cause of perpetual fresh-deploy failure: `init_db.sql` (Postgres Docker entrypoint) creates the full schema through migration 009 but doesn't seed `alembic_version`. Every `alembic upgrade head` tried to re-apply already-existing columns → `DuplicateColumn` errors.

**Fix:** `backend/entrypoint.sh` auto-detects empty `alembic_version`, stamps at `009_audit_log_phase9`, then runs `alembic upgrade head`. Only migrations 010–021 are applied on fresh deploy. No manual intervention ever needed.

```bash
CURRENT=$(alembic current 2>/dev/null | grep -Eo '[a-z0-9_]+' | head -1 || echo "")
if [ -z "$CURRENT" ]; then
    alembic stamp 009_audit_log_phase9
fi
alembic upgrade head
exec uvicorn src.main:app --host 0.0.0.0 --port 8000
```

`backend/Dockerfile` updated: `CMD ["/entrypoint.sh"]` replaces bare uvicorn CMD.

#### Admin Credentials via Environment Variables

Moved admin bootstrap from hardcoded defaults to env-driven seeder in `app.py` lifespan startup:
- Reads `settings.admin_email` / `settings.admin_password` from `config.py`
- Creates or updates admin user on every startup (idempotent)
- `docker-compose.yml` for both test and prod: `ADMIN_EMAIL` / `ADMIN_PASSWORD` env vars
- `bootstrap.sh` reads `${ADMIN_EMAIL:-admin@isms-core.dev}` / `${ADMIN_PASSWORD:-admin123}`

#### Beat Container Healthcheck Fix

`isms-core-beat` inherits the backend Dockerfile `HEALTHCHECK` (`curl -f http://localhost:8000/health`) but runs no web server → perpetual "unhealthy" in Portainer.

Fix: `docker-compose.yml` beat service: `healthcheck: disable: true`.

### DB State After Sessions 50–51

| Entity | Count |
|--------|-------|
| control_groups | 87 (54 ISMS + 21 PRIVACY + 12 CLOUD) |
| policies | 180 |
| implementations | 444 (378 ISMS + 66 privacy/cloud) |
| assessments | 275 |

---

## 2026-03-14 — Session 52: Production Deployment (NUC-02) + nginx TLS

### Context

Deployed the platform to NUC-02 (`62-isms-core-api-prod`, `/home/srv_admin/isms-core-prod`). Key architectural decision: ISO 27001 A.8.24 compliance requires TLS — running the ISMS compliance platform without encryption would create a direct gap against the control it monitors.

### nginx TLS Reverse Proxy

Added `isms-core-nginx` service to `62-isms-core-api-prod/docker-compose.yml`. Automatically resolves TLS certificate on first boot — no manual configuration required ("automate it for the monkeys").

**Three-mode certificate resolution (first match wins):**

| Mode | Trigger | Certificate Source |
|------|---------|-------------------|
| 1 — Let's Encrypt | `FQDN` env set + `/etc/letsencrypt/live/$FQDN/` exists | certbot pre-run via `setup-letsencrypt.sh` |
| 2 — Custom cert | `./certs/cert.pem` + `./certs/key.pem` present | local CA or purchased cert dropped in by operator |
| 3 — Self-signed (default) | no cert found | auto-generated RSA 2048 with SAN (IP + DNS), 10yr validity |

**nginx routes:**
- `HTTPS /health` → `backend:8000/health` (direct, for health checks)
- `HTTPS /api/` → `backend:8000` (FastAPI)
- `HTTPS /` → `frontend:3000` (React + WebSocket upgrade)
- `HTTP /` → 301 redirect to HTTPS

**Security headers:** HSTS (2yr, includeSubDomains), X-Frame-Options SAMEORIGIN, X-Content-Type-Options nosniff, Referrer-Policy strict-origin-when-cross-origin.

**New files:**
- `nginx/Dockerfile` — extends `nginx:alpine`, adds `openssl` + `gettext`
- `nginx/entrypoint.sh` — three-mode TLS resolver + `envsubst` config render
- `nginx/nginx.conf.template` — HTTPS proxy config with security headers
- `nginx/scripts/setup-letsencrypt.sh` — certbot automation + crontab renewal instructions

### Production docker-compose.yml

Key differences from test:
- No live code volume mounts
- PG/Redis/OpenSearch: internal only (no external ports)
- `VITE_BACKEND_URL=https://${HOST_IP}` (frontend calls via nginx)
- `ADMIN_PASSWORD` has no default fallback (must be set in `.env`)
- Email: both `mailpit` and `smtp-bridge` as optional profiles
- `PLATFORM_URL` / `CORS_ORIGINS` use `https://`

### bootstrap.sh Updates

- Health check: `curl -sfk https://localhost/health` (through nginx, `-k` for self-signed)
- All admin API calls: `-k` flag for self-signed cert
- Wait loop: 60 iterations × 2s = 120s total (backend 40s + nginx 15s start period)
- Summary output: shows `https://${HOST_IP}`, TLS upgrade path instructions

### NUC-02 Deployment Result

All 8 containers healthy on first run:

| Container | Status |
|-----------|--------|
| isms-core-nginx | healthy (0.0.0.0:80+443) |
| isms-core-backend | healthy |
| isms-core-worker | healthy |
| isms-core-beat | up (healthcheck disabled) |
| isms-core-frontend | up |
| isms-core-postgres | healthy |
| isms-core-redis | healthy |
| isms-core-opensearch | healthy |

Bootstrap stats: 54 controls, 145 policies, 378 implementations, 100% FW coverage.

Platform live at: **https://10.0.0.112**

### Environment Summary

| Environment | Host | IP | Workdir | Notes |
|-------------|------|----|---------|-------|
| Factory (dev) | local | localhost | `60-isms-core-api-factory/` | v2.0 development |
| Test | NUC-01 | 10.0.0.110 | `/home/srv_admin/isms-core-test` | v1.0 reference + bug fixes |
| Production | NUC-02 | 10.0.0.112 | `/home/srv_admin/isms-core-prod` | live, nginx TLS, A.8.24 ✅ |
