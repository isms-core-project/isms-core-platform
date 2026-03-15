# ISMS CORE Platform — Implementation Plan

<!--
Document ID:    ISMS-API-PLAN-001
Title:          ISMS CORE Platform Implementation Plan
Version:        0.3
Date:           2026-02-08
Updated:        2026-03-10
Owner:          Gregory Griffin
Author:         Claude Code (Opus 4.6)
Classification: Internal
Related Docs:   ARCHITECTURE.md, DATA-MODEL.md, LOG.md
Change Log:     v0.3 — Marked Phases 3, 4, 5 COMPLETE. Added Phase 5.1 (QA/Existence Checker).
                        Added foundation policies (group '00', INS type, 10 docs).
                        Added admin endpoints: sysinfo, orphan scanner, reindex.
                        Added doc ID normalisation notes (A.5.19-23, A.7.1-3, A.8.20-22).
                        Added 118 new crosswalk mappings (MITRE, OWASP ASVS, FINMA). 2026-03-08.
                v0.2 — Added Phase 6 (Assessment Content Bootstrap & Regeneration Pipeline) based on
                        Priority 5/5b architectural decisions recorded 2026-03-01.
                        Updated External Inputs (QA sprint 100% complete).
-->

---

## Overview

Build a Docker-first compliance management platform that ingests ISMS CORE's static files (policies, workbooks, implementation guides) and presents them as a live, correlated compliance system with dashboards, gap analysis, and cross-framework mapping.

**Both products** (Framework + Operational) are first-class citizens.

**Architecture**: FastAPI + PostgreSQL + Redis + OpenSearch + Celery + React (see ARCHITECTURE.md)

**Data Model**: 15 entity types across 3 layers — reference frameworks, ISMS content, and compliance analysis (see DATA-MODEL.md)

---

## Phase Overview

| Phase | Name | Focus | Dependencies |
|-------|------|-------|-------------|
| **0** | Data Model & Datasets | Define canonical model, create reference framework bundles | None |
| **1** | Backend Core | FastAPI app structure, SQLAlchemy models, CRUD API, DB connected | Phase 0 |
| **2** | Importers | Workbook parser, policy parser, IMP indexer, framework loader | Phase 1 |
| **3** | Dashboard API | Compliance endpoints, coverage matrix, gap summary, audit readiness | Phase 2 |
| **4** | React Frontend | Dashboard views, control explorer, gap tracker, framework mapper | Phase 3 |
| **5** | Correlation Engine | Keyword matching, cross-framework QA, score verification | Phase 2 |
| **6** | External Document Support | Third-party / non-ISMS CORE document ingestion with QA analysis + amber banners | Phase 2 |
| **7** | Assessment Content Bootstrap & Regeneration | Import 188 generators → DB; WebUI forms; script + workbook regeneration from DB | Phase 1 |
| **8** | ISMS CORE Compass | AI-powered gap analysis: vector KB from ISMS CORE docs, compares any uploaded doc against Gold Standard | Phase 6 |
| **10** | Privacy Extension Pack | ISO 27701:2025 + ISO 27018:2025 control library in `51-isms-core-privacy/` ✅ POL+platform done, SCR next | Phase 0 (standalone) |

---

## Phase 0: Data Model & Datasets ✓ COMPLETE

**Goal**: Define the canonical ISMS data model and create reference framework JSON bundles that ship with the platform.

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 0.1 | Project structure | Create `docs/`, `datasets/`, `schemas/` folders | DONE |
| 0.2 | Architecture analysis | Write ARCHITECTURE.md (OpenCTI study, design decisions) | DONE |
| 0.3 | Data model spec | Write DATA-MODEL.md (15 entity types, relationships, indexes) | DONE |
| 0.4 | Implementation plan | Write PLAN.md (this document) | DONE |
| 0.5 | Development log | Write LOG.md (session tracking) | DONE |
| 0.6 | ISO 27001 dataset | `raw/iso27001_2022_controls.json` + generator + bundle | DONE |
| 0.7 | Control groups dataset | `raw/control_groups.json` (54 groups) + generator + bundle | DONE |
| 0.8 | NIST CSF 2.0 dataset | 6 functions, 22 categories, 106 subcategories → 134 objects | DONE |
| 0.9 | NIST SP 800-53 dataset | 20 families, 324 controls, 872 enhancements → 1,216 objects | DONE |
| 0.10 | CIS Controls v8 dataset | 18 controls + 153 safeguards → 171 objects | DONE |
| 0.11 | MITRE ATT&CK dataset | 14 tactics + 216 techniques + 475 subtechniques + 44 mitigations → 749 objects | DONE |
| 0.12 | OWASP Top 10:2025 + ASVS 4.0.3 | 10 categories + 14 chapters + 278 requirements → 302 objects | DONE |
| 0.13 | Swiss nFADP/nDSG | 11 articles → 11 objects | DONE |
| 0.14 | EU GDPR | 16 security-relevant articles → 16 objects | DONE |
| 0.15 | FINMA | 3 circulars/guidance, 21 sections → 24 objects | DONE |
| 0.16 | NIS2 Directive | 14 articles (10 measures + 4 reporting) → 14 objects | DONE |
| 0.17 | DORA | 4 chapters, 26 articles → 30 objects | DONE |
| 0.18 | PCI DSS v4.0.1 | 6 objectives + 12 requirements → 18 objects | DONE |
| 0.19 | EU AI Act | 9 high-risk requirement articles → 9 objects | DONE |
| 0.19b | US CLOUD Act | 5 provisions (info/awareness, not mapped) → 5 objects | DONE |
| 0.20 | Cross-framework mappings | 1,898 mappings across 11 axes (6 mapping sources assembled) | DONE |
| 0.21 | Evolved DB schema | `schemas/init_db.sql` — 18 tables, 14 enums, 62 indexes, 3 mat views, 11 triggers (844 lines) | DONE |
| 0.22 | Control dependencies | `raw/control_dependencies.json` + generator + bundle (229 intra-ISO-27001 relationships, 5 types) | DONE |

### Dataset Generation Order

```
TIER 1 — Foundation (everything maps TO these)
0.6  ISO 27001:2022       (93 controls — foundation)                      ✓ DONE
0.7  Control Groups       (54 groups — our stacking model)                ✓ DONE

TIER 2 — Security Frameworks (map FROM ISO, used in cross-framework analysis)
0.8  NIST CSF 2.0         (134 objects — 6 functions, 22 categories, 106 subcategories)          ✓ DONE
0.9  NIST SP 800-53 R5    (1,216 objects — 20 families, 324 controls, 872 enhancements)          ✓ DONE
0.10 CIS Controls v8      (171 objects — 18 controls + 153 safeguards)                           ✓ DONE
0.11 MITRE ATT&CK v18     (749 objects — 14 tactics + 691 techniques + 44 mitigations)           ✓ DONE
0.12 OWASP Top 10 + ASVS  (302 objects — 10 Top 10:2025 + 14 ASVS chapters + 278 reqs)          ✓ DONE

TIER 3 — Regulatory Frameworks (referenced in POLs, required for compliance)
0.13 Swiss nFADP/nDSG     (11 articles — primary jurisdiction)                                    ✓ DONE
0.14 EU GDPR              (16 security-relevant articles)                                         ✓ DONE
0.15 FINMA                (24 objects — 3 circulars/guidance, 21 sections)                         ✓ DONE
0.16 NIS2 Directive       (14 articles — 10 Art.21 measures + 4 Art.23 reporting)                  ✓ DONE
0.17 DORA                 (30 objects — 4 chapters, 26 articles)                                   ✓ DONE
0.18 PCI DSS v4.0.1       (18 objects — 6 objectives + 12 requirements)                            ✓ DONE
0.19 EU AI Act            (9 articles — high-risk AI requirements)                                 ✓ DONE
0.19b US CLOUD Act        (5 provisions — info/awareness, not mapped)                              ✓ DONE

TIER 4 — Integration
0.20 Crosswalk            (1,898 mappings across 11 axes — ties everything together)             ✓ DONE
0.21 Evolved DB schema    (18 tables, 14 enums, 62 indexes, 3 mat views)    ✓ DONE
0.22 Control dependencies (229 intra-ISO-27001 dependency relationships)     ✓ DONE
```

### Deliverables

- [x] `docs/ARCHITECTURE.md`
- [x] `docs/DATA-MODEL.md`
- [x] `docs/PLAN.md`
- [x] `docs/LOG.md`
- [x] `datasets/raw/iso27001_2022_controls.json` — 93 controls with ISO 27002 attributes
- [x] `datasets/raw/control_groups.json` — 54 groups (53 ISO + 1 regulatory)
- [x] `datasets/scripts/generate_iso27001.py` — raw → bundle (97 objects, 93 relationships)
- [x] `datasets/scripts/generate_control_groups.py` — raw → bundle (54 objects, 94 relationships)
- [x] `datasets/data/iso27001_2022.json` — generated bundle
- [x] `datasets/data/control_groups.json` — generated bundle
- [x] `datasets/raw/nist_csf_2.0.json` — 6 functions, 22 categories, 106 subcategories
- [x] `datasets/raw/nist_sp800_53r5.json` — 20 families, 1,196 controls (from OSCAL)
- [x] `datasets/raw/cis_controls_v8.json` — 18 controls, 153 safeguards (v8.1)
- [x] `datasets/raw/mitre_attack_v18.json` — 14 tactics, 691 techniques, 44 mitigations (v18.1)
- [x] `datasets/raw/owasp_top10_2025.json` — 10 categories (verified from owasp.org)
- [x] `datasets/raw/owasp_asvs_4.0.3.json` — 14 chapters, 278 requirements
- [x] `datasets/raw/swiss_ndsg.json` — 11 articles
- [x] `datasets/raw/eu_gdpr.json` — 16 articles
- [x] `datasets/raw/finma.json` — 3 circulars/guidance, 21 sections
- [x] `datasets/raw/nis2.json` — 14 articles
- [x] `datasets/raw/dora.json` — 4 chapters, 26 articles
- [x] `datasets/raw/pci_dss_v4.json` — 6 objectives, 12 requirements
- [x] `datasets/raw/eu_ai_act.json` — 9 articles
- [x] `datasets/raw/us_cloud_act.json` — 5 provisions (with USC citations)
- [x] `datasets/scripts/generate_iso27001.py` — 97 objects, 93 relationships
- [x] `datasets/scripts/generate_control_groups.py` — 54 objects, 94 relationships
- [x] `datasets/scripts/generate_nist_csf.py` — 134 objects, 128 relationships
- [x] `datasets/scripts/generate_nist_800_53.py` — 1,216 objects, 1,196 relationships
- [x] `datasets/scripts/generate_cis_v8.py` — 171 objects, 153 relationships
- [x] `datasets/scripts/generate_mitre_attack.py` — 749 objects, 1,362 relationships
- [x] `datasets/scripts/generate_owasp.py` — 302 objects, 278 relationships (Top 10:2025 + ASVS)
- [x] `datasets/scripts/generate_regulatory.py` — 127 objects, 59 relationships (8 frameworks)
- [x] 15 generated bundles in `datasets/data/`
- [x] `datasets/raw/crosswalk_mappings.json` — 1,898 cross-framework mapping relationships
- [x] `datasets/scripts/assemble_crosswalk_raw.py` — assembles 6 sources → raw crosswalk JSON
- [x] `datasets/scripts/generate_crosswalk.py` — raw → crosswalk bundle (1,898 objects)
- [x] `datasets/data/crosswalk.json` — generated crosswalk bundle (1.0 MB)
- [x] `schemas/init_db.sql` — 18 tables, 14 enums, 62 indexes, 3 materialized views, 11 triggers (844 lines)
- [x] `datasets/raw/control_dependencies.json` — 229 intra-ISO-27001 dependency relationships (5 types)
- [x] `datasets/scripts/generate_control_dependencies.py` — raw → bundle (229 objects)
- [x] `datasets/data/control_dependencies.json` — generated control dependencies bundle

---

## Phase 1: Backend Core ✓ COMPLETE

**Goal**: Proper FastAPI application with SQLAlchemy ORM, database connectivity, and CRUD endpoints.

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 1.1 | App structure | `backend/src/{api,core,domain,database,importers}/` | DONE |
| 1.2 | SQLAlchemy models | ORM models matching init_db.sql (18 tables across 8 domain files) | DONE |
| 1.3 | Alembic setup | Schema migration framework (stamp head — init_db.sql is source of truth) | DONE |
| 1.4 | Config management | Pydantic Settings from environment variables | DONE |
| 1.5 | Auth endpoints | JWT login, token refresh, role-based access | DONE |
| 1.6 | Control group CRUD | `/api/v1/controls/` endpoints | DONE |
| 1.7 | Framework CRUD | `/api/v1/frameworks/` endpoints | DONE |
| 1.8 | Assessment CRUD | `/api/v1/assessments/` endpoints | DONE |
| 1.9 | Health + system | `/health`, `/api/v1/admin/system/status` | DONE |
| 1.10 | Framework loader | BundleLoader: 4 bundle types, FK-ordered loading | DONE |
| 1.11 | Docker update | New `docker-compose.yml` + `backend/Dockerfile` | DONE |
| 1.12 | Seed data | Auto-seed on first boot via lifespan hook | DONE |

### Deliverables

- [x] `backend/src/` application package (54 files)
- [x] SQLAlchemy models for all 18 tables
- [x] Alembic config (stamp head, future migrations via autogenerate)
- [x] Working API with Swagger docs at `http://localhost:8000/docs`
- [x] Bundle loader (4 types: single-framework, multi-framework, control-groups, crosswalk)
- [x] `docker-compose.yml` (PostgreSQL 18 + Redis 8 + OpenSearch 3 + Backend + Celery worker)
- [x] All 10 VERIFY.md steps passing (verified end-to-end)

---

## Phase 2: Importers

**Goal**: Parse ISMS files from read-only mounts into the database.

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 2.1 | Policy importer | Parse 5 document types (POL, OP-POL, REF, CTX, FORM) from MD/PDF/DOCX → policies + requirements | **DONE** |
| 2.2 | Workbook importer (Operational) | Parse 53 checklists (uniform engine-generated structure) | **DONE** |
| 2.3 | Workbook importer (Framework) | Parse 188 generator scripts → workbook structure (Assessment + AssessmentSheet, no items — Phase 6) | **DONE** |
| 2.4 | IMP importer | Parse 376 IMP-UG/TG → implementations table + OpenSearch indexing | **DONE** |
| 2.4b | OpenSearch integration | Full-text search: OpenSearch 3.x container, indexing hooks, search API, reindex endpoint | **DONE** |
| 2.5 | Sync endpoint | `POST /api/v1/sync/full` — orchestrate all 4 importers in sequence | **DONE** |
| 2.6 | Change detection | Content hash comparison — skip unchanged files | **DONE** (built into 2.1) |
| 2.7 | Celery worker | Background processing with progress reporting | **DONE** (built into 2.1) |
| 2.8 | Mount configuration | Configurable paths for Framework and Operational mounts | **DONE** (built into 2.1) |
| 2.9 | Remote source sync | Allow sync from a Git URL or ZIP upload — for deployments where Docker host ≠ source file location (deferred, no current blocker) | DEFERRED |

### Parsing Priorities

```
2.1 → Policy importer        (DONE — 143 files, 5,266 requirements, 0 errors)
2.4 → IMP importer           (DONE — 376 files, 0 errors)
2.2 → Operational checklists (DONE — 53 assessments, 543 sheets, 2,591 items, 0 errors)
2.3 → Framework workbooks    (DONE — 188 assessments, 959 sheets, 0 errors)
2.5 → Sync endpoint          (DONE — POST /api/v1/sync/full + /async variant)
```

### Task 2.1 — Policy Importer (DONE)

**Scope**: Parse all document types from both Framework and Operational mounts into `policies` + `requirements` tables.

| Metric | Value |
|--------|-------|
| **Total files imported** | 141 |
| **Total requirements extracted** | 5,201 |
| **Errors** | 0 |
| **Idempotent re-run** | 0 imported, 141 skipped, 0 errors |

**Breakdown by type:**

| Type | Product | Count |
|------|---------|-------|
| POL | framework | 64 EN + 5 DE = 69 |
| OP-POL | operational | 53 |
| REF | framework | 12 |
| CTX | framework | 7 |
| FORM | framework | 1 (GDPR deletion forms) |

**Key features built:**

- **3 parsers**: Markdown (primary), PDF, DOCX — abstract `BasePolicyParser` with `ParsedPolicy` dataclass
- **Watermark system**: `<!-- ISMS-CORE:{TAG}:{doc_id}:{product}:{type}:{group_code} -->` injected by factory script, parsed as primary identification layer with bold-header fallback
- **5 PolicyType enum values**: POL, OP-POL, REF, CTX, FORM
- **DE translation handling**: German files in `de/` subfolders, `-DE` suffix on doc_id
- **Title-slug disambiguation**: REF/CTX/FORM files with shared control number get unique doc_ids via filename slug
- **6-layer group code resolution**: exact → A.0 regulatory fallback → strip suffix → strip sub-part → compact range → also_covers → folder name
- **SHA-256 content hash change detection**: skip unchanged files on re-import
- **Requirement extraction**: "shall" (mandatory) + "should" (recommended) sentences, skipping boilerplate sections
- **Celery async task**: `POST /admin/import-policies/async` returns task_id
- **Sync endpoint**: `POST /admin/import-policies` for testing

**Files created/modified:**

| File | Action |
|------|--------|
| `backend/src/importers/parsers/__init__.py` | Created |
| `backend/src/importers/parsers/base.py` | Created — ABC, ParsedPolicy, Section, helpers |
| `backend/src/importers/parsers/markdown_parser.py` | Created — watermark + bold header + Document Control extraction |
| `backend/src/importers/parsers/pdf_parser.py` | Created — pdfplumber text extraction |
| `backend/src/importers/parsers/docx_parser.py` | Created — python-docx paragraph/table extraction |
| `backend/src/importers/policy_importer.py` | Created — PolicyImporter class (~350 lines) |
| `backend/src/importers/tasks.py` | Modified — added import_policies task |
| `backend/src/api/v1/admin.py` | Modified — added 2 import endpoints |
| `backend/src/database/enums.py` | Modified — added REF, CTX, FORM to PolicyType |
| `backend/src/schemas/policies.py` | Created — PolicyRead, RequirementRead |
| `backend/requirements.txt` | Modified — added python-docx, pdfplumber |
| `backend/src/core/config.py` | Modified — added framework_path, operational_path |
| `docker-compose.yml` | Modified — added volume mounts + env vars |
| `schemas/init_db.sql` | Modified — REF/CTX/FORM enum values, VARCHAR(120) |
| `95-isms-core-factory/inject_policy_watermarks.py` | Created — watermark injector for all 5 doc types |

### Task 2.4 — IMP Importer (DONE)

**Scope**: Parse all IMP-UG/TG markdown files from Framework mount into the `implementations` table.

| Metric | Value |
|--------|-------|
| **Total files imported** | 510 |
| **UG files** | 254 |
| **TG files** | 254 |
| **Unsplit P3/P4** | 2 (A.8.8.12 continuations) |
| **Errors** | 0 |
| **Idempotent re-run** | 0 imported, 510 skipped, 0 errors |

**Key features built:**

- **BaseImporter refactoring**: Extracted ~130 lines of shared code (group resolution, history tracking, parser setup) from PolicyImporter into shared `BaseImporter` class. Both PolicyImporter and ImpImporter inherit from it.
- **Watermark extension**: Extended `inject_policy_watermarks.py` to handle IMP files with new `IMP` tag and UG/TG type detection
- **IMP group code cleanup**: Strips `-UG`/`-TG` suffix, `.SN` section suffix, and `-PN` continuation suffix before deriving group_code
- **Multi-part disambiguation**: A.8.8.12 P1-P4 files get unique doc_ids via `-PN` suffix (e.g., `ISMS-IMP-A.8.8.12-TG-P1`)
- **impl_type detection**: From watermark `type` field (UG/TG) or `detect_impl_type()` fallback on doc_id
- **Content hash change detection**: SHA-256, skip unchanged files on re-import
- **Celery async task**: `POST /admin/import-implementations/async` returns task_id
- **Sync endpoint**: `POST /admin/import-implementations` for testing

**Files created/modified:**

| File | Action |
|------|--------|
| `backend/src/importers/base_importer.py` | Created — shared BaseImporter class (~170 lines) |
| `backend/src/importers/imp_importer.py` | Created — ImpImporter class (~200 lines) |
| `backend/src/importers/policy_importer.py` | Modified — extends BaseImporter, removed ~130 lines of duplication |
| `backend/src/importers/parsers/base.py` | Modified — added IMP to doc_id pattern, added `detect_impl_type()` |
| `backend/src/importers/parsers/markdown_parser.py` | Modified — added IMP to watermark/doc_id regexes |
| `backend/src/importers/tasks.py` | Modified — added `import_implementations_task` |
| `backend/src/api/v1/admin.py` | Modified — added 2 IMP import endpoints |
| `backend/src/domain/content.py` | Modified — document_id String(50) → String(120) |
| `95-isms-core-factory/inject_policy_watermarks.py` | Modified — extended for IMP discovery + watermarks |

### Task 2.4b — OpenSearch Full-Text Search (DONE)

**Scope**: Add OpenSearch 3.x container to Docker stack, create search service with full-text indexing, hook indexing into both importers, add search API and admin reindex endpoint.

| Metric | Value |
|--------|-------|
| **Docker containers** | 5 (added OpenSearch 3.4.0) |
| **Implementations indexed** | 510 |
| **Policies indexed** | 141 |
| **Total indexed** | 651 |
| **Errors** | 0 |
| **Search indices** | 2 (isms-implementations, isms-policies) |

**Key features built:**

- **OpenSearch 3.4.0 container**: Single-node dev mode, health-checked, persistent volume, security plugin disabled
- **Search service**: Client singleton with retry, graceful degradation (app works without OpenSearch), custom analyzer (standard + lowercase + stop + snowball)
- **Two indices**: `isms-implementations` (510 docs) and `isms-policies` (141 docs) with nested sections/requirements fields
- **Inline indexing**: Both importers call `search_service.index_implementation/policy()` after DB upsert — section content is NOT stored in DB, so indexing must happen during import
- **Search API**: `GET /api/v1/search?q=...` with filters (type, control_group, product, impl_type, policy_type), highlights, pagination
- **Admin endpoints**: `GET /admin/search/status` (cluster health + counts), `POST /admin/reindex` (full re-parse from filesystem)
- **Health integration**: Health endpoint reports OpenSearch status (ok/unavailable)

**Files created/modified:**

| File | Action |
|------|--------|
| `docker-compose.yml` | Modified — added OpenSearch 3.x service + volume + depends_on + OPENSEARCH_URL env |
| `backend/requirements.txt` | Modified — opensearch-py 2.4.2 → 3.1.0 |
| `backend/src/services/search_service.py` | Created — client, index management, indexing, search, status (~330 lines) |
| `backend/src/schemas/search.py` | Created — SearchHit, SearchResponse, SearchStatus |
| `backend/src/api/v1/search.py` | Created — GET /api/v1/search endpoint |
| `backend/src/api/router.py` | Modified — mounted search router |
| `backend/src/importers/base_importer.py` | Modified — added _get_group_name() helper |
| `backend/src/importers/imp_importer.py` | Modified — hooked search_service.index_implementation() |
| `backend/src/importers/policy_importer.py` | Modified — hooked search_service.index_policy() |
| `backend/src/api/v1/admin.py` | Modified — added reindex + search status endpoints |
| `backend/src/app.py` | Modified — OpenSearch ensure_indices() in lifespan |
| `backend/src/schemas/common.py` | Modified — added opensearch field to HealthResponse |
| `backend/src/api/v1/health.py` | Modified — reports OpenSearch status |

### Deliverables

- [x] Working policy parser (POL + OP-POL + REF + CTX + FORM → requirements)
- [x] Working IMP importer (510 IMP-UG/TG → implementations)
- [x] OpenSearch full-text search (651 docs indexed, search API with highlights)
- [ ] Working Operational checklist parser (53 xlsx → assessments + items)
- [ ] Working Framework workbook parser (~200 individual assessment xlsx → assessments + items; consolidation dashboards excluded — see D9)
- [ ] `POST /api/v1/sync/full` endpoint
- [x] Content-hash change detection (SHA-256, built into both importers)
- [x] Celery async tasks (import_policies + import_implementations)
- [x] Mount configuration (framework_path + operational_path in config.py)

---

## Phase 3: Dashboard API

**Goal**: API endpoints that power the compliance dashboards.

### Tasks

| # | Task | Description |
|---|------|-------------|
| 3.1 | ✅ Compliance overview | Overall scores by product, section, control group |
| 3.2 | ✅ Framework coverage | ISO ↔ NIST ↔ MITRE ↔ CIS mapping matrix |
| 3.3 | ✅ Gap analysis | Open gaps by severity, owner, due date, product |
| 3.4 | ✅ Evidence status | Evidence coverage, freshness, missing items |
| 3.5 | ✅ Audit readiness | Composite score: policies + evidence + assessments + gaps |
| 3.6 | ✅ Control detail | Per-control-group deep view (both products) |
| 3.7 | ✅ Search | Full-text search across policies, IMPs, requirements (Task 2.4b) |
| 3.8 | Export | CSV/PDF export of dashboard data |
| 3.9 | Materialized views | Pre-computed aggregations for dashboard performance |
| 3.10 | ✅ Graph API | `GET /api/v1/graph` — control dependency graph with filters (center, depth, edge_types, section) |

### Phase 3 Metrics (2026-03-01)

| Endpoint | Status | Notes |
|----------|--------|-------|
| `GET /api/v1/dashboard/overview` | ✅ Live | 54 controls, 100% framework coverage |
| `GET /api/v1/dashboard/coverage` | ✅ Live | 2,127 mappings across 14 frameworks |
| `GET /api/v1/dashboard/gaps` | ✅ Live | Returns empty until data entry |
| `GET /api/v1/dashboard/evidence` | ✅ Live | Returns empty until data entry |
| `GET /api/v1/dashboard/audit-readiness` | ✅ Live | 79% composite, amber (evidence=0% drags score) |
| `GET /api/v1/graph` | ✅ Live | Nodes+edges, Cytoscape.js ready; center/depth/section/edge_types filters |

**Foundation policies**: `00-foundation-policies` (ISMS-POL-00, ISMS-POL-01, 4× REF, ISMS-INS-POL-00, ISMS-INS-POL-01 + DE variants) imported under the permanent Foundation control group (group_code `00`, name "00 — Foundation Policies"). The old `a.0` regulatory group has been removed; all non-`a.`-prefix group codes resolve to `00`.

### Deliverables

- [x] `/api/v1/dashboard/*` endpoints (5 dashboard views)
- [x] `/api/v1/search` full-text search (delivered in Task 2.4b)
- [x] `/api/v1/controls/{id}` rich detail view (Task 3.6 — DONE)
- [x] `/api/v1/graph` control dependency graph endpoint
- [ ] Materialized views with refresh strategy (Task 3.9 — deferred)
- [ ] Export endpoints (CSV, PDF) (Task 3.8 — deferred)

---

## Phase 4: React Frontend

**Goal**: Web UI with compliance dashboards, control explorer, and gap management.

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 4.1 | React scaffold | Create React 19 + TypeScript + MUI 6 + Vite project | ✅ DONE |
| 4.2 | Layout + navigation | App shell, sidebar nav (Overview/Coverage/Gaps/Controls/Evidence/Search/Graph/Admin) | ✅ DONE |
| 4.3 | Dashboard — compliance | Overview: 6 metric cards, bar+radar charts, audit readiness, section breakdown | ✅ DONE |
| 4.4 | Dashboard — coverage | Framework mapping matrix with framework selector, progress bar, table | ✅ DONE |
| 4.5 | Dashboard — gaps | Gap analysis: severity/status/product filters, metrics, table | ✅ DONE |
| 4.6 | Control explorer | Browse 54 groups grouped by section, search + section + product filters | ✅ DONE |
| 4.7 | Control detail | Tabbed view: Policies / Implementations / Assessments / ISO Mappings / Evidence / Gaps | ✅ DONE |
| 4.8 | Assessment viewer | Sheets table with score/progress/compliance_level inline in Control Detail | ✅ DONE |
| 4.9 | Search | Full-text search with OpenSearch highlights, type filter, graceful offline handling | ✅ DONE |
| 4.10 | Auth | Login page, JWT + localStorage, ProtectedRoute, AuthContext, auto-redirect on 401 | ✅ DONE |
| 4.11 | Evidence tracker | Upload dialog (file+form), list table, download, delete, expiry status | ✅ DONE |
| 4.12 | Audit log | Deferred — no audit_log API endpoint yet |  |
| 4.13 | Control dependency graph | Cytoscape.js graph, cose layout, node type colours, center/depth/section filters | ✅ DONE |

### Phase 4 Stack

| Package | Version | Purpose |
|---------|---------|---------|
| React | 19 | UI framework |
| TypeScript | 5.7 | Type safety |
| MUI | 6 | Component library |
| Vite | 6 | Build tool + dev proxy |
| react-router-dom | 7 | Client-side routing |
| @tanstack/react-query | 5 | Data fetching + cache |
| axios | 1.7 | HTTP client |
| recharts | 2 | Charts (bar, radar, progress) |
| cytoscape | 3.31 | Graph visualisation |
| dayjs | 1.11 | Date formatting |

### Frontend Structure

```
frontend/
├── Dockerfile                 (node:22-alpine, npm install, vite --host)
├── package.json
├── tsconfig.json
├── vite.config.ts             (proxy /api → backend, port 3000)
├── index.html
└── src/
    ├── main.tsx               (QueryClient + ThemeProvider + BrowserRouter + AuthProvider)
    ├── App.tsx                (Routes: / → Layout, /login → Login, protected wrapper)
    ├── theme.ts               (dark theme: #0A0F1E bg, #4472C4 primary, ISMS palette)
    ├── api/
    │   ├── client.ts          (axios instance, JWT interceptor, 401 → /login redirect)
    │   ├── types.ts           (all API response types)
    │   ├── auth.ts            (login — OAuth2 password flow)
    │   ├── dashboard.ts       (overview/coverage/gaps/evidence/audit-readiness)
    │   ├── controls.ts        (list/getById/getByCode)
    │   ├── evidence.ts        (list/get/upload/update/delete/downloadUrl)
    │   ├── graph.ts           (get graph with filters)
    │   ├── search.ts          (full-text search)
    │   └── admin.ts           (users/sync)
    ├── store/
    │   └── AuthContext.tsx    (token + user state, login/logout, localStorage persistence)
    ├── components/
    │   ├── Layout.tsx         (Sidebar + Outlet)
    │   ├── Sidebar.tsx        (220px fixed, nav items, logout)
    │   ├── PageHeader.tsx     (title + subtitle + actions slot)
    │   ├── MetricCard.tsx     (card with icon + value + optional progress bar)
    │   └── StatusChip.tsx     (colour-coded chip: green/amber/red/not_assessed)
    └── pages/
        ├── Login.tsx          (form, JWT storage, redirect)
        ├── Overview.tsx       (6 metrics + bar + radar + readiness + section breakdown)
        ├── Coverage.tsx       (framework selector, matrix table with chips)
        ├── Gaps.tsx           (filters, metrics, table)
        ├── Controls.tsx       (card grid grouped by section)
        ├── ControlDetail.tsx  (tabbed rich view)
        ├── Evidence.tsx       (upload dialog, list table, download/delete)
        ├── Search.tsx         (search bar, highlighted results)
        ├── Graph.tsx          (Cytoscape.js canvas, cose layout, controls)
        └── Admin.tsx          (sync buttons, system info, users table)
```

### Deliverables

- [x] Working React app at `http://localhost:3000`
- [x] Compliance overview dashboard
- [x] Framework coverage matrix (ISO → external)
- [x] Gap analysis view
- [x] Control group explorer (54 groups, card grid)
- [x] Control detail (tabbed: policies/impls/assessments/mappings/evidence/gaps)
- [x] Interactive control dependency graph (Cytoscape.js)
- [x] Evidence upload + management
- [x] Full-text search
- [x] Authentication (JWT, login, protected routes)
- [x] Admin: sync + users table
- [ ] Audit log viewer (Task 4.12 — deferred, no API endpoint yet)

---

## Phase 5: Correlation Engine ✅ COMPLETE (2026-03-04)

**Goal**: Automated QA verification — do ISMS CORE documents actually cover ISO 27001 requirements?

### What Was Built

| # | Feature | Description | Status |
|---|---------|-------------|--------|
| 5.1 | Existence check | POL + IMP + assessment present per control group? | ✅ DONE |
| 5.2 | Keyword correlation | ISO 27001 keyword coverage in UG/TG (OpenSearch + synonym rules) | ✅ DONE |
| 5.3 | Semantic similarity — Mini LLM | Cosine similarity via sentence-transformers (all-MiniLM-L6-v2, CPU) | ✅ DONE |
| 5.4 | Semantic similarity — Claude AI | Anthropic Claude Haiku scores alignment 0–100 with reasoning + gaps | ✅ DONE |
| 5.5 | ISO dataset enrichment | All 93 Annex A controls enriched with ISO 27001:2022/27002 descriptions | ✅ DONE |
| 5.6 | Synonym rules CRUD | Admin-managed keyword synonym table for the keyword engine | ✅ DONE |
| 5.7 | QA legend + audit clarity | Method legend with "informational only" vs "S1 proxy" banners | ✅ DONE |
| 5.8 | Admin Reset & Re-import | Wipe + re-import all POLs/IMPs/assessments in one action | ✅ DONE |

### Audit Relevance Model

| Method | Audit Status | Notes |
|--------|-------------|-------|
| Existence | **S1 proxy** — deterministic | Pass = all artefacts present. Used for Stage 1 readiness. |
| Keyword | Informational only | Quality signal. Does not affect S1/S2. |
| Mini LLM | Informational only | Cosine similarity. Calibrated thresholds: PASS ≥ 0.42 / WARN ≥ 0.28. |
| Claude AI | Informational only | Score 0–100. PASS ≥ 70 / WARN ≥ 45. Stores reasoning + gap chips. |

### Results (2026-03-04)

| Method | Pass | Warning | Fail |
|--------|------|---------|------|
| Existence | 54/54 (100%) | 0 | 0 |
| Keyword | TBD (depends on run) | — | — |
| Mini LLM | 35 | 19 | 0 |
| Claude AI | Requires API key | — | — |

---

## Phase 6: External Document Support ✅ COMPLETE (2026-03-07)

**Goal**: Allow customers to import third-party or custom (non-ISMS CORE) policies and implementation docs, run the full QA analysis against them, and clearly distinguish them from native ISMS CORE content throughout the UI.

### Use Case

A customer has an existing A.5.1 policy from a previous consultant or in-house team. They do not want to replace it with the ISMS CORE version. They want to:
1. Import it into the platform
2. Know how well it covers the ISO 27001 requirements
3. See exactly what's missing (gap chips from keyword + Claude AI checks)

### Design Decisions

- New `ProductType.EXTERNAL` value (alongside `FRAMEWORK` and `OPERATIONAL`)
- Relaxed parser — no ISMS CORE watermark or ID format required; manual group mapping step
- Manual control group assignment on import (UI step: "Which control group does this cover?")
- `source_label` field on Policy: free text e.g. "Acme Corp", "Previous consultant", "ISO 27001 Toolkit"
- Amber "External Document" banner shown everywhere the doc appears (Control Detail, Policies page, QA)
- Existence check: PASS with "⚠ External source" annotation (artefact present but not ISMS CORE)
- Keyword + semantic checks run normally — most useful method for foreign docs
- Coverage dashboard: external docs count toward "covered" but with visual distinction

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 6.1 | `ProductType.EXTERNAL` | Add enum value + Alembic migration | DONE |
| 6.2 | `source_label` field | Add to `policies` table + Alembic migration | DONE |
| 6.3 | Relaxed MD parser | No watermark / no ISMS CORE ID format required; fallback title + group extraction | DONE |
| 6.4 | Manual group mapping | Import UI: file upload → select control group → confirm | DONE |
| 6.5 | External importer | `ExternalDocImporter` class — handles PDF/DOCX/MD, calls relaxed parser | DONE |
| 6.6 | Admin upload endpoint | `POST /admin/import-external` with multipart form (file + group_code + source_label) | DONE |
| 6.7 | OpenSearch indexing | External docs indexed with `product_type=external` for keyword checks | DONE |
| 6.8 | Existence check update | Flag external docs with annotation rather than pure PASS | DONE |
| 6.9 | UI amber banners | "External Document — [source_label]" chip/banner in ControlDetail, Policies, QA | DONE |
| 6.10 | Coverage page | External docs shown with amber distinction; separate count in section breakdown | DONE |
| 6.11 | Policies page upload | Upload external doc button + dialog (file + group + source) | DONE |

### Multi-language Support (6.12–6.16)

Switzerland has three official languages (DE / FR / IT) alongside English. ISMS CORE docs will be translated. The importer currently only discovers German (`de/` subfolder, `-DE` suffix). French and Italian are not handled.

| # | Task | Description | Status |
|---|------|-------------|--------|
| 6.12 | `language` field on Policy | Add `language` VARCHAR(5) column (`en`, `de`, `fr`, `it`) + Alembic migration (same migration as 6.1/6.2) | DONE |
| 6.13 | Importer subfolder discovery | Extend `PolicyImporter` + `ImpImporter` to scan `fr/` and `it/` subfolders (mirrors existing `de/` logic) | DONE |
| 6.14 | Document ID suffix convention | `-FR` and `-IT` suffixes (mirrors `-DE`); detected in importer, stored on `language` field | DONE |
| 6.15 | Language filter in UI | Policies page: language chip filter (`EN` / `DE` / `FR` / `IT`); language badge per non-EN doc | DONE |
| 6.16 | QA language awareness | Keyword/semantic checks run on the correct language version; results grouped by language in QA table | DONE |

### Deliverables

- [x] `ProductType.EXTERNAL` in DB + API
- [x] `language` field on `policies` table
- [x] Relaxed parser + `ExternalDocImporter`
- [x] `POST /admin/import-external` endpoint
- [x] Manual group mapping UI
- [x] Amber "External Document" banners throughout
- [x] QA runs on external docs (keyword + semantic)
- [x] Coverage page handles external docs correctly
- [x] FR + IT subfolder discovery in importers
- [x] Language filter in Policies page + ControlDetail
- [x] QA language awareness (language field in OpenSearch, language-filtered fetch, language badge in QA table)

---

## Phase 7: Assessment Content Bootstrap & Regeneration Pipeline ✅ COMPLETE (2026-03-08)

**Goal**: Import structured assessment content from 188 QA'd generators into PostgreSQL, then regenerate scripts and workbooks from the DB. This makes the DB the permanent master for all control assessment data.

### Architectural Decision (Recorded 2026-03-01)

**The DB is the permanent master source of truth for all control assessment data.**

The 188 QA'd Python generators bootstrap the DB once with accurate, ISO-aligned assessment requirements. Once imported, the DB takes over as master. Scripts become a derived output, not the origin. This applies across all artefact types and both products.

```
Phase 6.1 — Bootstrap (one-time)
──────────────────────────────────────────────────────────────
188 QA'd Python scripts (Framework SCR) + 53 (Operational SCR)
    │
    ▼
Generator Import Pipeline
    │  → Extract: sheets, DVs, validation logic, scoring,
    │             control stacking, assessment areas
    │  → Normalise: deviations discarded, clean schema applied
    │  → Validate: QA gate (rejects controls failing QA thresholds)
    ▼
PostgreSQL DB (canonical, normalised, master)

Phase 6.2 — Platform Operation (ongoing)
──────────────────────────────────────────────────────────────
PostgreSQL DB (master)
    │
    ├──▶ WebUI Forms          (assessment data entry — Option A)
    │
    ├──▶ Workbook Import      (Excel upload — Option B, legacy path)
    │
    └──▶ Script Regeneration  (on-demand, for standalone users)
              │
              ▼
         188 regenerated scripts
         (Golden Standard template × control-specific DB payload)
         Zero structural deviations — fully maintainable
```

This architecture applies to **all artefact types across both products**:

| Artefact | Product | Bootstrap Source | DB Operation | Generated Output |
|----------|---------|-----------------|--------------|-----------------|
| Assessment scripts (.py) | Framework | 188 QA'd SCR generators | Import + normalise | Regenerated .py (Golden Standard template) |
| Assessment scripts (.py) | Operational | 53 QA'd SCR generators | Import + normalise | Regenerated .py (Golden Standard template) |
| Workbooks (.xlsx) | Both | Generated from SCR scripts | Import via bootstrap | Regenerated .xlsx (on demand) |
| Policies (.md) | Framework | 53 POL Markdown files | Import content + structure | Regenerated .md (from DB edits) |
| Policies (.md) | Operational | 53 OP-POL Markdown files | Import content + structure | Regenerated .md (from DB edits) |
| Implementation guides (.md) | Framework | 376 IMP-UG/TG files | Import content + structure | Regenerated .md (from DB edits) |

**Post-launch editing flow** (Platform mode organisations):
```
User edits content in WebUI → DB updated → MD/PY rendered on publish → .md/.py download
```

Git becomes a *publication target* (files pushed from DB on release), not the editing environment.

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 7.1 | Review + update DB schema | Validate `schemas/init_db.sql` against current generator structure (written pre-QA sprint) | **DONE** 2026-03-08 |
| 7.2 | Build generator import parser | `datasets/scripts/parse_generators.py` → `datasets/data/generator_registry.json` (188 records) | **DONE** |
| 7.3 | DB table + migrations | `generator_definitions` table (migrations 003–005): sheets, user_override, sheet_schemas | **DONE** |
| 7.4 | Run bootstrap import | `datasets/scripts/import_generator_registry.py` → 189 rows in DB (188 FW + 1 foundation checklist) | **DONE** |
| 7.5 | Sheet schemas import | `datasets/scripts/import_sheet_schemas.py` → 188 rows with full `sheet_schemas` JSONB | **DONE** |
| 7.6 | Document DB schema | `docs/SCHEMA.md` (ISMS-API-SCHEMA-001) — live DB state, migration history, generator_definitions detail, API→DB map | **DONE** 2026-03-08 |
| 7.7 | Generators API + WebUI | `GET /api/v1/generators/`, `/generators/form/{group_code}`, `/generators/{doc_id}/render`; `Generators.tsx` page | **DONE** |
| 7.8 | Control stacking | Stacked generators identified in registry; stacked_control_ids populated; handled in form renderer | **DONE** |
| 7.9 | QA validation gate | `validate_generator_record()` in `parse_generators.py` → `qa_status`/`qa_issues` per record; `--strict` flag in `import_generator_registry.py` rejects FAIL records. Results: 170 PASS / 18 WARN / 0 FAIL | **DONE** 2026-03-08 |
| 7.10 | Assessment POST endpoints | `POST /api/v1/assessments/` (create), `POST /{id}/rows`, `PATCH /items/{id}`, `DELETE /items/{id}`, `DELETE /{id}` — full CRUD; `create_platform_assessment()` service layer | **DONE** |
| 7.11 | Golden Standard template | `backend/templates/generator.py.j2` — Jinja2 template for script regeneration | **DONE** |
| 7.12 | Regeneration engine | `backend/src/services/generator_service.py` `render_generator()` → `.py` source string | **DONE** |
| 7.13 | QA gate on regenerated output | `validate_rendered_script()` in `generator_service.py` — syntax + constants + functions; `X-QA-Status`/`X-QA-Issues` response headers; CORS `expose_headers` | **DONE** 2026-03-08 |
| 7.14 | Workbook regeneration | `workbook_service.py` `regenerate_workbook()` — render → QA gate → subprocess → .xlsx; `POST /{doc_id}/workbook` endpoint; `_TmpCleanup` background task; template freeze_panes `None` guard | **DONE** 2026-03-08 |
| 7.15 | Governance mode schema | `GovernanceMode` enum; `organisations` table + migration 006; `GET/PATCH /api/v1/organisation/`; seeded with `platform` default | **DONE** 2026-03-08 |
| 7.16 | RBAC implementation | `require_admin` + `require_content_editable` (governance_mode + role) in `dependencies.py`; `is_editable_in_ui` computed field on OrganisationRead; gates on PATCH /organisation/, generators PUT/DELETE, policy DELETE | **DONE** 2026-03-08 |
| 7.17 | Approval workflow | `ContentState` enum (draft/review/approved/published); `content_state` column on `policies` + `implementations` (default: published); `PATCH /{policy_id}/state`; `is_editable_in_ui` guards state changes | **DONE** 2026-03-08 |
| 7.18 | Audit trail | `EditSource` enum (import/webui/api); `edit_source` column on policies + implementations; `audit_service.log_action()`; state transitions write audit log entries with old_state/new_state/edit_source | **DONE** 2026-03-08 |

### Key Principles

- **DB is master — always.** Assessment requirement changes are made in the solution. The DB is never a downstream projection of scripts after bootstrap.
- **Scripts remain available — always.** Standalone users can download regenerated scripts at any time, in sync with the DB.
- **Workbook import is retained — as a legacy path.** Orgs that ran existing assessments can still import from Excel. Both paths feed the same DB.
- **Bootstrap quality gates the DB.** Import pipeline validates against `qa_check_workbooks.py` rules. The QA sprint (February 2026) is the trust foundation for the initial DB state.
- **Control stacking preserved.** Stacked controls (e.g. A.5.32-33, A.8.25-26-29) are modelled as a single assessment unit in the DB, mirroring the generator/workbook structure exactly.

### Governance Mode (Per-Organisation Setting)

One platform flag on the organisation record determines how policy content is managed:

| Mode | Authority | How Policies Managed | Typical User |
|------|-----------|---------------------|-------------|
| **platform** | DB master | Edit in WebUI → DB → MD generated on publish | SMEs, Operational product users |
| **local** | Git/filesystem master | Edit locally → import trigger → DB syncs | Framework users, regulated industries with Git workflows |

**Default recommendations**: Framework → `local` | Operational → `platform`

Schema implications:
- `organisation.governance_mode` field: `platform` | `local`
- `policy.is_editable_in_ui` derived from governance mode
- `policy_version.edit_source` tracked: `webui` | `import`

### Success Criteria

| Gate | Criteria |
|------|----------|
| DB Bootstrap | All 53 control groups imported, 0 QA failures |
| Schema completeness | All DVs, stacking, scoring, validation rules present |
| WebUI parity | Forms cover same assessment areas as workbooks |
| Script regeneration | 188 output scripts pass QA with 0 deviations |
| Round-trip integrity | DB → script → import → DB produces identical data |

---

## Phase 8: ISMS CORE Compass — Policy Knowledge Base ✅ COMPLETE (2026-03-09)

**Goal**: AI-powered gap analysis that tells users exactly what their documents are missing — and why — compared to the ISO 27001:2022 Gold Standard. The first tool in the market that shows what *good* looks like, not just a pass/fail score.

### Problem Being Solved

Today, a junior compliance officer writing an A.5.1 policy has no reference point. They write three paragraphs, think they're done, and the tool says "FAIL" with no explanation. What's missing is:
- **What does a complete A.5.1 policy look like?**
- **Which specific topics are you missing?**
- **Here's the relevant ISO 27002:2022 guidance.**

### Design

A vector knowledge base built from ISMS CORE's 53 POLs + 188 IMPs (the Gold Standard). When any document is uploaded — ISMS CORE native or external — ISMS Compass:

1. Embeds the uploaded document
2. Retrieves the most relevant ISMS CORE reference sections (RAG)
3. Sends both to Claude AI with a structured gap-analysis prompt
4. Returns: coverage score, specific gaps, example text from Gold Standard, ISO 27002 guidance

### Mandatory Disclaimer

Every Compass response carries a permanent banner:

> *"This analysis is based on ISO 27001:2022 requirements and ISMS CORE reference content. It is provided for guidance only and does not guarantee audit compliance. Independent review by a qualified ISMS practitioner is recommended."*

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 8.1 | Vector store | OpenSearch BM25 (145 policies + 378 IMPs indexed) | ✅ |
| 8.2 | RAG retrieval | `_fetch_reference_content()` in compass_service.py — BM25 by group_code | ✅ |
| 8.3 | Gap analysis prompt | Full structured prompt → JSON schema enforced | ✅ |
| 8.4 | Gap report schema | `coverage_score`, `gaps[]`, `strengths[]` — Pydantic + TS types | ✅ |
| 8.5 | Compass API | `POST /api/v1/compass/analyse` + `GET /compass/status` | ✅ |
| 8.6 | Compass UI | Full page: score gauge, gap cards by severity, strengths | ✅ |
| 8.7 | Inline Compass | "Analyse with Compass" button in ControlDetail → `/compass?group=X` | ✅ |
| 8.8 | Disclaimer system | Permanent non-dismissable Alert on all Compass outputs | ✅ |
| 8.9 | Rebuild KB trigger | `POST /admin/reindex` (admin-only) — full OpenSearch rebuild | ✅ |

**Notes:**
- Model upgraded from `claude-haiku-4-5-20251001` → `claude-sonnet-4-6` (2026-03-09)
- Using OpenSearch BM25 retrieval (not pgvector) — adequate for group-scoped retrieval
- ANTHROPIC_API_KEY configured in `.env`

### Dependencies

- Phase 6 (External docs) — Compass should work for external docs too
- ANTHROPIC_API_KEY configured
- pgvector extension or dedicated vector DB in Docker stack

---

---

## Phase 9: Audit Logging + Email Notifications ✅ COMPLETE (2026-03-09)

**Goal**: Full audit trail for ISO 27001 A.8.15 (Logging) + A.8.17 (Clock sync) compliance, plus email notifications for ISMS workflow events.

### SMTP Architecture

Pluggable via `MAIL_HOST` / `MAIL_PORT` env vars — backend sends to plain port 25, doesn't know what's behind it:

| Mode | Container | Notes |
|------|-----------|-------|
| **Dev (Mac/ARM)** | `mailhog` — catches all, web UI :8025 | ARM-compatible, no rebuild needed |
| **Prod on-prem** | Internal Postfix relay | Pure LAN, zero cloud |
| **Prod M365** | `SmtpToGraphBridge` Docker Compose service | Adapted from `factory_kubernetes/kube_smtp_kubernetes`. Existing `.NET 8` image needs ARM rebuild for Mac dev; K8s image (`neige/docker_kubernetes:smtp-gateway-cluster-framework-net10`) works as-is on NUC (x86). Pass `GRAPH_CLIENT_ID`, `GRAPH_CLIENT_SECRET`, `GRAPH_TENANT_ID`. |

Graph API bridge is a cloud dependency for *delivery only* — ISMS CORE itself stays fully self-contained. Per-deployment choice via env var.

### Audit Events

**Security (ISO A.8.15 — always logged, never deleted):**
`login.success`, `login.failure`, `login.locked`, `logout`, `password.changed`, `user.created`, `user.modified`, `user.deleted`, `role.changed`, `api.unauthorized`

**ISMS workflow (logged + optional email notification):**
`evidence.expiring` (≤30 days), `evidence.expired`, `gap.assigned`, `gap.overdue`, `assessment.status_changed`, `qa.check_completed` (fails only), `user.welcome`, `import.completed`

### Tasks

| # | Task | Description | Status |
|---|------|-------------|--------|
| 9.1 | `audit_log` table | Alembic migration: `id, event_type, category, severity, user_id, actor_email, target_type, target_id, description, ip_address, user_agent, metadata_, created_at` | ✅ |
| 9.2 | `audit_service.py` | `log_event()` helper — called from auth router, admin router, gap/evidence mutations | ✅ |
| 9.3 | Audit log API | `GET /api/v1/admin/audit-log` — paginated, filterable by category/severity/user/date | ✅ |
| 9.4 | Audit log UI | System page: new "Audit Log" tab — table with category badge, severity colour, actor, description, timestamp | ✅ |
| 9.5 | `email_service.py` | `smtplib.SMTP(MAIL_HOST, MAIL_PORT)` wrapper — graceful no-op if `MAIL_HOST` unset | ✅ |
| 9.6 | Email templates | Jinja2 HTML templates per event type (welcome, gap assigned, evidence expiry, QA fail, etc.) | ✅ |
| 9.7 | `notification_service.py` | Celery tasks per event type — called by service layer after state changes | ✅ |
| 9.8 | Evidence expiry scanner | Celery beat daily job — finds evidence expiring ≤30 days or already expired, enqueues notifications | ✅ |
| 9.9 | Docker Compose: Mailpit | Dev: add `axllent/mailpit` service (ARM+amd64), ports 1025+8025 web UI | ✅ |
| 9.10 | SMTP config + test email | System page SMTP card; `POST /admin/email/test` endpoint | ✅ |
| 9.11 | Notification prefs | Per-user email opt-in/out per event category — sidebar dialog + admin user edit | ✅ |
| 9.12 | ISO 27001:2022/Amd.1:2024 | Update dataset + version string for Amendment 1:2024 (climate change clauses 4.1/4.2) | ✅ |

### Dependencies

- Phase 4 (auth + user model) — COMPLETE
- Docker Compose additions (mailhog / SmtpToGraphBridge)
- ARM rebuild of SmtpToGraphBridge for Mac dev (separate task — rebuild `SmtpToGraphBridge_v10` for `linux/arm64`)

---

## Maybe / Future — Ideas Backlog

Ideas captured from market research and user sessions. Not committed to any phase.

| Idea | Source | Notes |
|------|--------|-------|
| **ISO 27017** Cloud Services Security | Session 2026-03-07 | 7 new cloud controls + guidance overlay. Map to ISO 27001:2022 Annex A. ✅ DONE |
| **ISO 27018** PII in Public Cloud | Session 2026-03-07 | 16 PII controls for cloud processors. Map to ISO 27001:2022 + GDPR. ✅ DONE |
| **ISO 27701** Privacy Information Management | Session 2026-03-07 | PIMS extension to ISO 27001/27002. PII controllers (7.x) + processors (8.x). Map to GDPR + ISO 27001. ✅ DONE |
| ISO 27015 Financial Services | Session 2026-03-07 | Guidance doc only (no control list) — not mappable |
| ISO 27016 Organisational Economics | Session 2026-03-07 | Theoretical economics standard — not mappable |
| NIS2 phased implementation programme (2026–2028) | cyber-assistant.com | Structured NIS2 roadmap as a guided workflow — complements our NIS2 dataset already in DB |
| Risk analysis wizard | cyber-assistant.com | 8-step wizard: CIA classification → 24 questions → 35 automated recommendations. Simpler version of Compass gap analysis |
| Maturity radar chart | cyber-assistant.com | Executive KPI dashboard with maturity radar per section — could extend our Overview page |
| **Sign-out button in WebUI** | Session 2026-03-09 | Sidebar has logout in AuthContext but no visible sign-out button for users — add to header or sidebar user menu |
| Audit trail log viewer | Task 4.12 (deferred) | Already planned, no API endpoint yet |
| PDF / HTML export | Task 3.8 (deferred) | Already planned, dashboard data export |
| "Offline / no data leaves device" mode | cyber-assistant.com | Relevant for public sector clients — not current target but worth tracking if we add a local-only deployment mode |

---

## Dependencies

```
Phase 0 ──► Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4
                │         │
                │         └──► Phase 5 ✅ (complete)
                │
                ├──► Phase 6 ✅ (External docs — complete)
                │
                ├──► Phase 7 (Assessment Bootstrap — after Phase 6)
                │
                ├──► Phase 8 (ISMS Compass — after Phase 6, needs vector store)
                │
                └──► Phase 9 (Audit Logging + Email — independent, any time after Phase 4)
```

Phase 6 unlocks Phase 8 (Compass needs external doc support to be fully useful).

---

## Risk Register

| # | Risk | Impact | Likelihood | Mitigation |
|---|------|--------|-----------|------------|
| R1 | Scope creep toward OpenCTI complexity | High | Medium | Strict phase boundaries. No GraphQL, no connector marketplace. |
| R2 | Framework data licensing (ISO text) | Medium | Low | Use control IDs + short descriptions. Reference public frameworks (NIST, CIS, MITRE). |
| R3 | Workbook parsing fails on edge cases | Medium | Low | Start with Operational (uniform). Framework: import only individual assessment workbooks (~188), skip consolidation dashboards (~53). Platform dashboard replaces consolidation logic. |
| R4 | Two-product model adds UI complexity | Medium | Medium | Product toggle (Framework/Operational/Unified). Shared control group navigation. |
| R5 | Performance on initial sync (~241 workbooks) | Low | Low | Celery async. Content hash (skip unchanged). Materialized views for dashboards. |
| R6 | CISO review feedback requires changes | Low | Medium | External validation strengthens quality. Feedback incorporated before platform launch. |
| R7 | Pilot customer (bank) requires features not planned | Medium | Medium | Phase boundaries protect scope. Custom requirements tracked separately. |
| R8 | Static volume mounts fail in remote deployments | Medium | Medium | Current docker-compose.yml mounts local filesystem paths. If containers run on a remote server/cloud host, ISMS source files won't be available. Mitigation: Task 2.9 — add Git URL sync (preferred, files already in `factory_isms`) or ZIP bundle upload via WebUI. No blocker while running locally. |

---

## Success Criteria

### Phase 0 Complete When:
- [x] All 15 reference framework bundles generated (2,850 objects, 3,363 relationships)
- [x] Cross-framework crosswalk with 1,898 mappings across 11 axes
- [x] Control dependencies with 229 intra-ISO-27001 relationships (5 types)
- [x] DATA-MODEL.md finalised and reviewed
- [x] Evolved DB schema matches data model (18 tables, 844 lines)

### Phase 1 Complete When:
- [x] `docker compose up -d` produces working stack (PostgreSQL 18 + Redis 8 + Backend + Worker)
- [x] All 54 control groups loaded with both products
- [x] All 15 reference frameworks loaded with 1,898 cross-mappings
- [x] 143 policy documents parsed with 5,266 requirements extracted
- [x] All 10 VERIFY.md steps passing

### Platform MVP (Phase 3 Complete) When:
- [x] `docker compose up -d` produces working stack
- [x] All 54 control groups loaded with both products
- [x] All reference frameworks loaded with cross-mappings
- [ ] All ~253 workbooks parsed and indexed (53 Operational + ~200 Framework individual assessments)
- [x] All 141 policy documents parsed with 5,201 requirements extracted
- [x] All 510 IMP-UG/TG files parsed into implementations table
- [ ] 5 dashboard API endpoints returning real data
- [x] Full-text search working (651 docs indexed, OpenSearch 3.4.0)

### Production-Ready (Phase 4 Complete) When:
- [ ] React frontend with all dashboard views
- [ ] Authentication and role-based access
- [ ] Evidence and gap management
- [ ] Export capabilities (CSV, PDF)
- [ ] Audit logging

---

## External Inputs

| Input | Source | Impact | Timeline |
|-------|--------|--------|----------|
| **CISO review** (A.5.19-23, A.8.24, OP-POL-00) | Former CISO (GRC professional) | Validates control quality, may trigger content updates | In progress |
| **Pilot opportunity** (bank) | Previous customer | May drive priority of specific features (banking regulations, FINMA) | After CISO validation |
| **Framework completion** | Completed 2026-03-01 | **100% complete** — 53/53 packs, 93/93 controls, 188 QA'd generators ready for Phase 6 bootstrap | ✓ Done |

---

*This plan is designed to deliver value incrementally. Each phase produces something usable. The platform works with whatever ISMS content exists — it doesn't require 100% completion.*

---

## v2.0 — Extension Packs (Future, Post-v1.0 Launch)

> **Prerequisite:** ISO PDFs purchased (27701:2025, 27018:2025) ✓. 27017:2025 not yet published.

### Product Architecture (LOCKED 2026-03-09)

Three products — each with its own full navigation context in the UI:

| Product | Standards | Folder | Groups |
|---------|-----------|--------|--------|
| **ISMS** | ISO 27001:2022 | `50-isms-core-framework/` + `10-isms-core-operational/` | 53 |
| **PRIVACY** | ISO 27701:2025 + ISO 27018:2025 Annex A | `51-isms-core-privacy/` | 21 + 27018 overlay |
| **CLOUD** | ISO 27017:2025 (when published) | `52-isms-core-cloud/` | TBD |

**Bundling rationale:**
- 27018:2025 is a *privacy* standard for cloud processors — belongs in PRIVACY, not CLOUD
- 27018 Annex A (25 controls) = overlay on PRIVACY processor packs, not standalone
- CLOUD = 27017 only (cloud *security* extension of 27001 Annex A)

### Folder Structure

```
10-isms-core-operational/   ← ISO 27001 simplified — unchanged
50-isms-core-framework/     ← ISO 27001:2022 (53 groups) — unchanged
51-isms-core-privacy/       ← ISO 27701:2025 + ISO 27018:2025 Annex A (21 groups)
52-isms-core-cloud/         ← ISO 27017:2025 only — when published (future)
```

### DB Changes (migration 013)

```python
# ProductType enum additions
ProductType.PRIVACY = "PRIVACY"   # 51-isms-core-privacy
ProductType.CLOUD   = "CLOUD"     # 52-isms-core-cloud (future)

# organisations table additions
active_products: JSON          # ["ISMS", "PRIVACY"] — all visible, no gating
privacy_role: Enum             # CONTROLLER | PROCESSOR | BOTH (default: BOTH)
                               # drives coverage denominator — not just a UI filter
```

**`privacy_role` semantics:**
- `CONTROLLER`: only A.1.x (8 groups) + A.3.x (8 shared groups) = 16 groups in scope
- `PROCESSOR`: only A.2.x (5 groups) + A.3.x (8 shared groups) = 13 groups in scope
- `BOTH`: all 21 groups in scope (default)
- Coverage % calculated against the in-scope denominator — wrong to score a processor-only org on controller controls

### Platform UI — 3 Big Product Switcher (LOCKED 2026-03-09)

**Navigation model:** Product switcher in sidebar header. Each product has its own full navigation context. All products always visible (no licensing gate).

```
Sidebar:
  ● ISMS  ○ PRIVACY  ○ CLOUD    ← top-level switcher

Per product — own routes:
  Dashboard | Controls | Policies | Coverage | Assessments | QA

Always visible (cross-product):
  Gaps | Evidence | Reports | Admin
```

**Route scheme:**
```
/isms/dashboard            /privacy/dashboard         /cloud/dashboard
/isms/controls             /privacy/controls          /cloud/controls
/isms/controls/:groupCode  /privacy/controls/:groupCode
/isms/policies             /privacy/policies
/isms/coverage             /privacy/coverage
/isms/qa                   /privacy/qa

/gaps                      ← shared (evidence can link to controls in any product)
/evidence                  ← shared
/reports                   ← shared (report builder selects which products to include)
/admin                     ← shared
```

Legacy routes (`/controls`, `/policies`) redirect to `/isms/controls`, `/isms/policies` — no broken bookmarks for existing ISMS users.

**PRIVACY product — sub-navigation:**
- Section pills: `Controller (A.1)` | `Processor (A.2)` | `Shared (A.3)` | `All`
- Filtered by org `privacy_role` (a CONTROLLER-only org never sees Processor controls)
- UI also provides a per-session role focus toggle (doesn't affect scoring, just narrows the list)

**PRIVACY ControlDetail:**
- Standard tabs: Overview | Policies | Implementations | Assessments | Evidence
- Extra tab: `ISMS Crosswalk` → which 27001 Annex A controls this 27701 group maps to
- For processor groups: `ISO 27018 Overlay` tab → applicable Annex A controls from 27018:2025

**ISMS ControlDetail:**
- Existing tabs unchanged
- Extra tab (when PRIVACY product active): `Privacy Overlay` → relevant 27701 control groups

**Coverage dashboard:**
- Per-product coverage card — never a combined score
- PRIVACY coverage respects `privacy_role` denominator
- CLOUD shows "Coming soon" state until content imported

### Content Scope

| Standard | Control Groups | Doc Pairs (POL+UG+TG) | Status |
|----------|---------------|----------------------|--------|
| ISO 27701:2025 | 21 | 21 POLs + 42 IMP pairs | ✅ Content complete (2026-03-09) |
| ISO 27018:2025 Annex A | overlay on PRIVACY | no separate POL — overlay tabs | Pending (Phase 10.7) |
| ISO 27017:2025 | TBD | TBD | Not yet published |

---

## Phase 10: Privacy Extension Pack

**Status:** PARTIALLY COMPLETE (2026-03-10) — POL content + full platform integration done; SCR generators next
**Working directory:** `51-isms-core-privacy/`
**Standards:** ISO/IEC 27701:2025 (Ed. 2, standalone PIMS) + ISO/IEC 27018:2025 (Annex A overlay)
**Prerequisite:** ISO PDFs purchased ✓ (97-isms-core-iso-regulatory/)

---

### Architectural Decisions (Locked)

**27701:2025 — Fully standalone control packs**
ISO 27701:2025 (Ed. 2) is a standalone PIMS standard, NOT an extension of ISO 27001.
21 control groups built fully from scratch in `51-isms-core-privacy/`.

**27018:2025 — Annex A overlay only (25 controls)**
ISO 27018:2025 body = ISO 27002 cloud guidance (not duplicated — absurd to do so).
Only the 25 genuinely new Annex A PII-specific controls are built.
Delivered as a crosswalk extension layered onto 27701 A.2 processor packs, not standalone.

**27017 — Not in scope for Phase 10**
ISO 27017:2019 is a cloud *security* standard (not privacy). Referenced in PRIV-POL-00 as Tier 3 informational.
ISO 27017:2025 not yet published — placeholder entry in PRIV-POL-00: adopt on publication.

---

### Control Group Summary

| Family | Groups | ISO 27701 Annex | Controls |
|--------|--------|-----------------|---------|
| Privacy-Controller | 8 | A.1.x | 31 |
| Privacy-Processor | 5 | A.2.x | 18 |
| Privacy-Shared | 8 | A.3.x | 29 |
| **Total** | **21** | | **78** |

Plus 2 foundation policy documents (PRIV-POL-00, PRIV-POL-01).

---

### Folder Structure

```
51-isms-core-privacy/
├── 00-priv-foundation-policies/
│   ├── priv-pol-00-privacy-regulatory-applicability-framework/
│   │   └── POL/   PRIV-POL-00 — Privacy Regulatory Applicability Framework.md
│   └── priv-pol-01-privacy-governance-and-decision-making/
│       └── POL/   PRIV-POL-01 — Privacy Governance and Decision-Making Framework.md
│
├── privacy-controller/            ← ISO 27701:2025 Annex A.1 (31 controls → 8 groups)
│   ├── priv-a.1.2.2-5-lawful-basis-and-consent/
│   ├── priv-a.1.2.6-9-privacy-governance-and-records/
│   ├── priv-a.1.3.2-4-transparency-and-information-provision/
│   ├── priv-a.1.3.5-10-data-subject-rights/
│   ├── priv-a.1.3.11-automated-decision-making/    ← standalone (GDPR Art.22)
│   ├── priv-a.1.4.2-5-data-minimisation/
│   ├── priv-a.1.4.6-10-pii-lifecycle-retention-and-disposal/
│   └── priv-a.1.5.2-5-pii-transfer-and-disclosure/
│
├── privacy-processor/             ← ISO 27701:2025 Annex A.2 (18 controls → 5 groups)
│   ├── priv-a.2.2.2-7-processor-agreements-and-obligations/
│   ├── priv-a.2.3.2-pii-principal-obligations-processor/   ← standalone
│   ├── priv-a.2.4.2-4-processor-lifecycle-controls/
│   ├── priv-a.2.5.2-6-transfer-and-disclosure-processor/
│   └── priv-a.2.5.7-9-sub-processor-management/           ← ISO 27018 Annex A overlay here
│
└── privacy-shared/                ← ISO 27701:2025 Annex A.3 (29 controls → 8 groups)
    ├── priv-a.3.3-4-privacy-policy-and-roles/
    ├── priv-a.3.5-7-information-classification-and-transfer/
    ├── priv-a.3.8-10-identity-access-and-supplier-controls/
    ├── priv-a.3.11-12-privacy-incident-management/         ← split from A.3.11-16
    ├── priv-a.3.13-16-compliance-audit-and-review/         ← split from A.3.11-16
    ├── priv-a.3.17-19-people-security-and-clear-desk/
    ├── priv-a.3.20-22-physical-media-and-endpoint-security/
    └── priv-a.3.23-31-technical-controls-auth-crypto-dev/
```

Each group folder: `POL/ | IMP/ | SCR/ | WKBK/`
Note: CTX/, REF/, SCR_ORG/ folders deleted 2026-03-10 — not needed for privacy product.

---

### PRIV-POL-00 Regulatory Tiers

| Tier | Standard/Regulation | Notes |
|------|---------------------|-------|
| Tier 1 — Mandatory | GDPR (EU 2016/679), CH-nDSG/FADP | Legal obligation for CH/EU scope |
| Tier 2 — Conditional | ISO 27701:2025, ISO 27018:2025 | Applies under certification/in-scope |
| Tier 3 — Informational | ISO 27017:2019 | Cloud security baseline supporting 27018 |
| Forthcoming | ISO 27017:2025 (not yet published) | Adopt on publication — placeholder |

---

### Phase 10 Task List

| # | Task | Status |
|---|------|--------|
| 10.0 | Create `51-isms-core-privacy/` folder structure (21 groups + foundation) | ✅ DONE |
| 10.1 | PRIV-POL-00 — Privacy Regulatory Applicability Framework | ✅ DONE |
| 10.2 | PRIV-POL-01 — Privacy Governance Framework | ✅ DONE |
| 10.3a | All 21 POL documents (A.1 + A.2 + A.3 control groups) | ✅ DONE (2026-03-09) |
| 10.3b | All 21 IMP pairs (42 UG + 42 TG = 84 documents) | ✅ DONE (2026-03-09) |
| 10.4 | SCR generators — 21 control groups (Python → Excel, same format as 27001) | 🔜 NEXT |
| 10.5 | ISO 27018 Annex A overlay (25 controls — overlay tabs on processor packs) | TODO |
| 10.6 | DB migrations 014 + 015: CLOUD + PRIVACY control groups in PostgreSQL | ✅ DONE (2026-03-09) |
| 10.7 | Platform importer: PRIV-POL + CLD-POL imported via POLICY_EXTRA_PATHS volume mounts | ✅ DONE (2026-03-09) |
| 10.8 | Frontend — 3 Big Product Switcher + per-ISO navigation context | ✅ DONE (2026-03-10) |
| 10.9 | QA sprint (21 packs, same methodology as 27001 v1.0) | TODO (after SCR generators) |
| 10.10 | Promote to factory_isms | TODO |

### Build Order

1. ✅ PRIV-POL-00 + PRIV-POL-01 (foundation)
2. ✅ privacy-shared A.3 (cross-role — best reference point)
3. ✅ privacy-controller A.1 (largest family)
4. ✅ privacy-processor A.2 + 27018 overlay (smallest; overlay last)
5. ✅ DB migrations 014/015 + PRIV-POL/CLD-POL import into platform
6. ✅ Frontend 3 Big Product Switcher + full per-ISO scoping (2026-03-10)
7. 🔜 SCR generators × 21 groups (next session)
8. QA sprint + promote

---

### UI Design — 3 Big Product Switcher (LOCKED 2026-03-09)

#### Navigation Structure

Product switcher sits in the sidebar header. Switching product changes the full navigation context. All three products always visible — no licensing gate.

```
Sidebar header:  ● ISMS  ○ PRIVACY  ○ CLOUD

ISMS context:    Dashboard | Controls | Policies | Coverage | Assessments | QA
PRIVACY context: Dashboard | Controls | Policies | Coverage | Assessments | QA
CLOUD context:   Dashboard | Controls | Policies | Coverage | Assessments | QA

Always shown:    Gaps | Evidence | Reports | Admin
```

#### Route Scheme

```
/isms/dashboard            /privacy/dashboard
/isms/controls             /privacy/controls
/isms/controls/:groupCode  /privacy/controls/:groupCode
/isms/policies             /privacy/policies
/isms/coverage             /privacy/coverage
/isms/assessments          /privacy/assessments
/isms/qa                   /privacy/qa
/cloud/...                 (Phase 11 — CLOUD content TBD)

/gaps                      ← cross-product (links to control in any product)
/evidence                  ← cross-product
/reports                   ← cross-product (report builder selects products)
/admin                     ← shared
```

Legacy routes (`/controls` → `/isms/controls`) redirect for backwards compatibility.

#### PRIVACY-Specific UI Behaviour

**Sub-navigation (Controls page):**
Section pills: `All` | `Controller (A.1)` | `Processor (A.2)` | `Shared (A.3)`
Filtered by `organisations.privacy_role` — a CONTROLLER-only org never sees A.2 groups.

**ControlDetail extra tabs:**
- `ISMS Crosswalk` — which 27001 Annex A controls this 27701 group maps to
- `ISO 27018 Overlay` (processor groups only) — applicable Annex A controls from 27018:2025

**ISMS ControlDetail extra tab** (when PRIVACY product loaded):
- `Privacy Overlay` — relevant 27701 control groups that relate to this 27001 group

**Coverage calculation:**
- Denominator driven by `organisations.privacy_role`
  - CONTROLLER: 16 in-scope groups (8 A.1 + 8 A.3)
  - PROCESSOR: 13 in-scope groups (5 A.2 + 8 A.3)
  - BOTH: 21 groups
- Never a combined ISMS+PRIVACY score — separate coverage cards per product

#### DB Migration 013 (migration_013_product_privacy.py)

```python
# 1. Extend ProductType enum
op.execute("ALTER TYPE producttype ADD VALUE 'PRIVACY'")
op.execute("ALTER TYPE producttype ADD VALUE 'CLOUD'")

# 2. Extend privacy_role on organisations
op.execute("CREATE TYPE privacyrole AS ENUM ('CONTROLLER', 'PROCESSOR', 'BOTH')")
op.add_column('organisations',
    sa.Column('privacy_role', sa.Enum('CONTROLLER', 'PROCESSOR', 'BOTH',
              name='privacyrole'), nullable=False, server_default='BOTH'))

# 3. Add product_family to control_groups
op.execute("CREATE TYPE productfamily AS ENUM ('ISMS', 'PRIVACY', 'CLOUD')")
op.add_column('control_groups',
    sa.Column('product_family', sa.Enum('ISMS', 'PRIVACY', 'CLOUD',
              name='productfamily'), nullable=False, server_default='ISMS'))
```

**Import-time assignment:**
- PRIV control groups → `product = "PRIVACY"`, `product_family = "PRIVACY"`
- Group code format: `a.1.2.2-5` / `a.2.3.2` / `a.3.17-19` (matches folder names exactly)
- Section field: `"controller"` / `"processor"` / `"shared"` (drives sub-navigation)
