# ISMS CORE Platform — Architecture Analysis

<!--
Document ID:    ISMS-API-ARCH-001
Title:          ISMS CORE Platform Architecture Analysis
Version:        0.3
Date:           2026-02-08
Updated:        2026-03-08
Owner:          Gregory Griffin
Author:         Claude Code (Opus 4.6)
Classification: Internal
Related Docs:   PLAN.md, DATA-MODEL.md, LOG.md
Change Log:     v0.3 — Updated counts (188 generators/376 IMPs, not 253/504). Corrected
                        policy importer stats (143 docs, 5,266 requirements). Replaced stale
                        "What's Missing" section with "Current State" (Phases 0–5 complete,
                        Phase 6 next). Updated service count to 6.
                v0.2 — Added D10 (DB as master source of truth) and D11 (per-organisation
                        governance mode) based on Priority 5/5b decisions recorded 2026-03-01.
                        Updated Current State to reflect completed QA sprint (188 generators).
                        Updated Auth Model with multi-tenancy note.
-->

---

## 1. Context

ISMS CORE is an ISO 27001:2022 compliance platform with **two products**:

| Product | Target | Deliverables per Control Group |
|---------|--------|-------------------------------|
| **Framework** (POL) | Mature organisations, consultants, auditors | POL + IMP-UG + IMP-TG + SCR + WKBK + REF + CTX + FORM |
| **Operational** (OP-POL) | SMEs and startups | OP-POL + SCR + WKBK (compliance checklist) |

Both products cover **53 control groups** mapping to all **93 ISO 27001:2022 Annex A controls**.

### Current State (Pre-Platform)

| Asset | Count | Format |
|-------|-------|--------|
| Governance Policies (POL) | 53 EN + 5 DE | Markdown |
| Operational Policies (OP-POL) | 53 | Markdown |
| Implementation Guides (IMP-UG/TG) | 376 (188 UG + 188 TG) | Markdown |
| Framework SCR Generators | **188** (QA complete 2026-03-01, 307K+ lines) | Python → Excel |
| Operational SCR Generators | 53 | Python → Excel |
| Generated Workbooks | **188** (Framework) + 53 (Operational) | Excel (.xlsx) |
| Reference Framework Data | 18 datasets | JSON bundles |

All of this exists as **static files on disk**. The platform's job is to ingest, correlate, and visualise them as a living compliance system.

### Why Now

- **Operational product**: 100% complete (53/53 OP-POLs + 53/53 checklists)
- **Framework product**: **100% complete** (53/53 packs, 93/93 controls, 188 QA'd generators — QA sprint closed 2026-03-01)
- **External validation**: Previous CISO (GRC professional) reviewing A.5.19-23, A.8.24, and POL-00
- **PowerBI abandoned**: Not scriptable, too much manual work
- **Dashboard workbooks**: Built per-control aggregation, but still static files
- **OpenCTI experience**: Production deployment (32 services, 23 connectors, 12 dashboards) provides architectural reference

---

## 2. OpenCTI Architecture Study

### What OpenCTI Does

OpenCTI is a threat intelligence platform that **ingests data from 128+ sources**, correlates it using **STIX 2.1** as a canonical data model, and presents it through **dashboards, knowledge graphs, and entity management**.

| Component | OpenCTI Choice | Notes |
|-----------|---------------|-------|
| Backend | Node.js + TypeScript | Single process with 15+ internal managers |
| API | GraphQL (Apollo Server 5) | 15,885-line schema, Relay pagination |
| Primary Store | Elasticsearch/OpenSearch | NOT a relational DB — search-first design |
| Cache | Redis | Sessions, pub/sub, distributed locks, stream state |
| Message Queue | RabbitMQ | Connector/worker communication |
| Object Storage | MinIO (S3) | File uploads, exports |
| Frontend | React 19 + Relay 20 + MUI 6 | Co-located GraphQL fragments, compile-time query optimisation |
| Workers | Python (separate process) | Consumes STIX bundles from RabbitMQ |
| Connectors | Python (separate containers) | 128+ external, 55+ enrichment, 6 export, 6 import, 27+ stream |
| Data Model | STIX 2.1 | 200+ entity types, deterministic IDs |
| Auth | Passport.js (8 providers) | Capability-based (KNOWLEDGE_KNUPDATE etc.) + marking-based access |
| Reference Data | datasets repo | Raw → generator → STIX bundle (3-layer pipeline) |

### Architectural Patterns Worth Adopting

**1. Canonical Data Model (STIX equivalent)**

OpenCTI's strength is that everything — whether from MITRE, CISA, or CrowdStrike — becomes a STIX object with a stable ID. Deduplication, correlation, and enrichment all work because there's one language.

**ISMS CORE equivalent**: A compliance data model where controls, requirements, evidence, assessments, and gaps all have stable UUIDs and typed relationships. Every importer converts to this model.

**2. Datasets Pattern (Reference Data Packaging)**

OpenCTI ships reference data (sectors, geography, companies) as:
```
raw/sectors.json → scripts/sectors.py → data/sectors.json (STIX bundle)
```
- Raw source is human-editable (CSV/JSON)
- Generator script transforms to distribution format
- Output has stable IDs (UUIDs assigned in raw source, never change)
- Connector polls GitHub URL on schedule, upserts via stable IDs
- No versioning beyond git history — ship full bundle, let receiver deduplicate

**ISMS CORE equivalent**: Ship ISO 27001, NIST CSF, NIST 800-53, CIS Controls, and MITRE ATT&CK as pre-generated JSON bundles. Loaded on first boot. Updated by re-running generators.

**3. Connector Architecture (Separation of Concerns)**

Each OpenCTI connector has four layers:
- `settings.py` — Pydantic-typed configuration
- `api_client.py` — HTTP interaction with external source
- `converter_to_stix.py` — Transform source data → STIX 2.1
- `connector.py` — Orchestrate: fetch → convert → send bundle

**ISMS CORE equivalent**: Importers with the same separation, but as Celery tasks (not separate containers). Converter layer transforms Excel/Markdown → ISMS compliance model.

**4. Capability-Based Auth with Marking Access**

OpenCTI enforces `@auth(for: ["KNOWLEDGE"])` at the schema level. Every endpoint requires explicit authorisation. Marking definitions (TLP) control data visibility.

**ISMS CORE equivalent**: Roles (Admin/ISMS Manager/Auditor/Control Owner/Viewer) with per-control-group access. Classification levels (Internal/Confidential/Restricted) control document visibility.

**5. Manager Pattern (Background Jobs)**

OpenCTI runs 15+ managers as cron-based or stream-based tasks with distributed locking (Redis Redlock) to prevent duplicate execution across instances.

**ISMS CORE equivalent**: Celery beat scheduler for periodic tasks (workbook re-sync, compliance score recalculation, evidence expiry checks, SLA monitoring).

### What NOT to Copy

| OpenCTI Choice | Why Not for ISMS CORE | Better Alternative |
|----------------|----------------------|-------------------|
| **Elasticsearch as primary store** | ISMS data is structured compliance data (scores, dates, statuses, FK relationships). Search is secondary. | PostgreSQL (primary) + OpenSearch (full-text search only) |
| **GraphQL + Relay** | 27 tables, not 200+ STIX types. GraphQL adds complexity for no gain. | FastAPI + REST + Pydantic models |
| **Node.js backend** | You already have FastAPI skeleton. Python ecosystem (openpyxl, pandas) is critical for workbook parsing. | FastAPI (keep what you have) |
| **RabbitMQ** | Overkill for internal importers. OpenCTI needs it because connectors are separate containers. | Celery + Redis (already in requirements.txt) |
| **Separate connector containers** | Your importers are internal (parse local files), not third-party plugins requiring isolation. | Celery tasks inside the backend container |
| **Module self-registration** | You have 53 control groups, not 200+ entity types that need runtime discovery. | Direct endpoint routing |
| **15,885-line schema** | Compilation overhead, learning curve, Relay complexity. | REST endpoints with Swagger/OpenAPI auto-docs |

---

## 3. Recommended Architecture

### Stack

| Layer | Technology | Justification |
|-------|-----------|---------------|
| **Frontend** | React 19 + MUI 6 + Recharts + Cytoscape.js | Modern, well-supported. Recharts for compliance dashboards. Cytoscape.js for interactive control dependency graph. |
| **Web Server** | Nginx (Alpine) | Reverse proxy, static files, API proxy, gzip, security headers. Already configured. |
| **API** | FastAPI 0.109+ | Async Python, auto-generated OpenAPI docs, Pydantic validation. Already started. |
| **ORM** | SQLAlchemy 2.0 + Alembic | Async ORM, schema migrations. Already in requirements. |
| **Primary Store** | PostgreSQL 18 (Alpine) | Structured compliance data. 18 tables, 14 enums, 62 indexes, 3 mat views. JSONB for flexible metadata. |
| **Cache + Queue** | Redis 8 (Alpine) | Session cache, assessment cache, Celery task broker. |
| **Full-Text Search** | OpenSearch 2.11 | Document content search (policies, IMPs). Already configured. |
| **Task Queue** | Celery 5.3 + Redis | Async workbook parsing, framework import, compliance recalculation. Already in requirements. |
| **Excel I/O** | openpyxl + pandas | Parse workbooks, generate reports. Already in requirements. |
| **Deployment** | Docker Compose | Self-contained stack. Already configured with 6 services. |

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      ISMS CORE Platform                          │
│                                                                  │
│  ┌──────────────┐    ┌──────────────────┐    ┌───────────────┐  │
│  │  React 19     │◄──│  FastAPI          │──►│  PostgreSQL   │  │
│  │  + MUI 6      │    │  REST API         │    │  18 (Alpine)  │  │
│  │  + Recharts   │    │  /api/v1/*        │    │               │  │
│  │  + Cytoscape  │    │                   │    │  18 tables    │  │
│  │               │    │  Pydantic models  │    │  3 mat. views │  │
│  │  Dashboards   │    │  SQLAlchemy 2.0   │    │  JSONB meta   │  │
│  │  Control view │    │  Alembic migrate  │    └───────────────┘  │
│  │  Gap analysis │    │                   │                       │
│  │  Evidence     │    │  Celery tasks ──►┌┴───────────────┐      │
│  │  Audit trail  │    │                  │  Redis 8        │      │
│  └──────────────┘    │                  │  (broker+cache) │      │
│                       │                  └────────────────┘      │
│                       │                                          │
│                       │──────────────────►┌────────────────┐     │
│                       │                   │  OpenSearch     │     │
│                       │                   │  2.11           │     │
│                       │                   │  (full-text)    │     │
│  ┌────────────────────┘                   └────────────────┘     │
│  │                                                               │
│  │  Importers (Celery tasks inside backend container):           │
│  │  ├── policy_importer  ✓    143 docs → 5,266 requirements     │
│  │  │   └── parsers: MD (primary) + PDF + DOCX                  │
│  │  │   └── watermark detection + bold-header fallback           │
│  │  │   └── 5 types: POL, OP-POL, REF, CTX, FORM           │
│  │  ├── workbook_importer     Parse 306 Excel workbooks          │
│  │  ├── imp_importer          Index IMP-UG/TG documents          │
│  │  ├── framework_loader  ✓   Load ISO/NIST/MITRE/CIS bundles   │
│  │  └── correlator            Cross-framework mapping + QA       │
│  │                                                               │
│  │  Scheduled Tasks (Celery beat):                               │
│  │  ├── Nightly workbook re-sync                                 │
│  │  ├── Compliance score recalculation                           │
│  │  ├── Evidence freshness check                                 │
│  │  └── Gap SLA monitoring                                       │
│  └───────────────────────────────────────────────────────────────│
│                                                                   │
│  📁 Read-Only Mounts (from host):                                │
│  ├── /app/isms-framework/   → 50-isms-core-framework/            │
│  ├── /app/isms-operational/ → 10-isms-core-operational/          │
│  └── /app/datasets/         → datasets/ (reference frameworks)   │
└──────────────────────────────────────────────────────────────────┘
```

### Data Flow

```
                    First Boot
                    ─────────
datasets/data/*.json ──► framework_loader ──► PostgreSQL
                                              (ISO, NIST, MITRE, CIS tables)

                    Initial Sync
                    ────────────
/app/isms-framework/   ──► policy_importer ──► PostgreSQL
/app/isms-operational/      (POL, OP-POL)   (policies, requirements)
                       ──► imp_importer    ──► PostgreSQL + OpenSearch
                            (IMP-UG/TG)          (implementations, full-text index)
                       ──► workbook_importer ──► PostgreSQL
                            (Excel .xlsx)          (assessments, sheets, items)

                    Correlation
                    ───────────
PostgreSQL ──► correlator ──► PostgreSQL
               (keyword match,    (correlation_analysis,
                cross-framework,    qa_scores,
                score verification) gap_analysis)

                    Serve
                    ─────
PostgreSQL ──► FastAPI ──► React
               /api/v1/*    (dashboards, explorer, reports)
```

### Both Products as First-Class Citizens

The platform must treat **Framework** and **Operational** equally:

| Aspect | Framework | Operational |
|--------|-----------|-------------|
| **Policy type** | POL (governance) | OP-POL (operational) |
| **Policy depth** | Detailed, multi-section, "with what" methodology | Self-contained, single document |
| **Implementation** | IMP-UG + IMP-TG (188 + 188 = 376 docs) | None (guidance is inline) |
| **Workbooks** | 188 individual assessment workbooks + 53 consolidation dashboards (not imported — see D9) | 53 compliance checklists (exec summary + dashboard + domain sheets) |
| **Generators** | 188 Python scripts | 53 Python scripts (shared engine) |
| **Supplementary** | REF + CTX + FORM (12 + 7 + 1 = 20 docs, imported) | None |
| **Translations** | 5 DE POLs + 1 DE CTX (in `de/` subfolders) | None |

The data model handles this via:
- `product_type` field on control groups (`framework`, `operational`, `both`)
- `policy_type` enum on policies: `POL`, `OP-POL`, `REF`, `CTX`, `FORM`
- **Watermark identification**: `<!-- ISMS-CORE:{TAG}:{doc_id}:{product}:{type}:{group_code} -->` injected by factory script, parsed as primary ID layer with bold-header fallback
- Different importer logic for Framework workbooks (individual assessments only, skip consolidation dashboards) vs Operational checklists (engine-generated, uniform structure)
- **Timestamped workbooks for trend tracking**: Framework assessment workbooks use `_YYYYMMDD.xlsx` suffix. Multiple versions of the same assessment (e.g., quarterly runs) are tracked as versioned assessments, enabling compliance trend analysis over time
- Dashboard views that can filter by product or show unified compliance

### Docker Deployment Model

```yaml
# Customer experience:
# 1. Clone/download
# 2. Mount your ISMS files
# 3. docker compose up -d
# 4. Open http://localhost:3000

services:
  postgres:     # Primary data store
  redis:        # Cache + task broker
  opensearch:   # Full-text search (optional for small deployments)
  backend:      # FastAPI + Celery worker
  frontend:     # React SPA via Nginx
```

**Why Docker-first**: "Not everybody will setup a server for his ISMS." A customer downloads the product, mounts their policies/workbooks folder, and runs `docker compose up -d`. No Kubernetes, no cloud dependencies, no server setup.

For users who want just the static files (policies + workbooks), they don't need the platform at all — the files are the product. The platform is the **premium layer** that adds correlation, dashboards, and audit management.

---

## 4. API Design

### Endpoint Structure

```
/api/v1/
├── /health                          Health check
├── /auth/
│   ├── POST /login                  JWT authentication
│   └── POST /refresh                Token refresh
│
├── /controls/
│   ├── GET /                        List all 53 control groups
│   ├── GET /{group_id}              Control group detail
│   ├── GET /{group_id}/policies     Policies for this group
│   ├── GET /{group_id}/assessments  Assessment results
│   ├── GET /{group_id}/gaps         Identified gaps
│   └── GET /{group_id}/evidence     Evidence items
│
├── /frameworks/
│   ├── GET /                        List loaded frameworks
│   ├── GET /{framework_id}          Framework detail + controls
│   └── GET /{framework_id}/mappings Cross-framework mappings
│
├── /assessments/
│   ├── GET /                        All assessments (filterable)
│   ├── GET /{id}                    Assessment detail (sheets, items)
│   └── GET /{id}/download           Download original Excel
│
├── /dashboard/
│   ├── GET /compliance              Overall compliance status
│   ├── GET /coverage                Framework coverage matrix
│   ├── GET /gaps                    Gap analysis summary
│   ├── GET /evidence                Evidence status
│   └── GET /audit-readiness         Audit readiness score
│
├── /graph/
│   └── GET /?center=...             Control dependency graph (nodes + edges, filterable)
│
├── /search/
│   └── GET /?q=...                  Full-text search (OpenSearch)
│
├── /sync/
│   ├── POST /full                   Full re-sync from mounted files
│   ├── POST /workbooks              Re-parse all workbooks
│   └── POST /policies               Re-parse all policies
│
└── /admin/
    ├── GET /audit-log               Audit trail
    ├── POST /frameworks/import      Import framework data
    └── GET /system/status           System health + sync status
```

### Auth Model

| Role | Capabilities |
|------|-------------|
| **Admin** | Full access — edit POL/IMP content, user management, system config, sync triggers, trigger script regeneration, manage review/approval workflows, configure per-org settings |
| **ISMS Manager** | All controls, assessments, gaps, evidence. Cannot manage users. |
| **Auditor** | Read-only access to everything. Can export reports. |
| **Control Owner** | Read/write on assigned control groups only. |
| **Viewer** | Read-only on non-confidential items. |

**Multi-tenancy note**: Admin is a platform-level role. User-facing roles (ISMS Manager, Auditor, Control Owner, Viewer) are organisation-scoped. A consultant may be Admin for their own org and ISMS Manager in a client org simultaneously.

---

## 5. Key Design Decisions

### Decision 1: PostgreSQL as Primary Store (not Elasticsearch)

OpenCTI uses Elasticsearch as primary because threat intelligence is fundamentally a search problem (find indicators, traverse graphs). ISMS compliance is fundamentally a **structured data** problem (scores, statuses, dates, foreign key relationships, aggregations).

PostgreSQL gives us:
- **Referential integrity** (control → requirement → evidence chain)
- **ACID transactions** (compliance scores are authoritative)
- **Aggregation queries** (dashboard rollups, compliance percentages)
- **JSONB** for flexible metadata without schema changes
- **Materialized views** for pre-computed dashboard data

OpenSearch handles only full-text search over document content (policies, IMPs).

### Decision 2: REST, not GraphQL

GraphQL excels when:
- Clients need wildly different data shapes (mobile vs web vs widget)
- The schema has 200+ types with deep nesting
- You use Relay for compile-time query optimization

ISMS CORE has:
- One client (React web app)
- ~30 entity types
- Predictable query patterns (dashboards, control detail, gap list)

REST with Pydantic response models and auto-generated OpenAPI docs is simpler, faster to build, and easier to maintain.

### Decision 3: Celery Tasks, not Connector Containers

OpenCTI needs separate connector containers because:
- 128+ connectors from different vendors with different dependencies
- Each connector has its own lifecycle (restart, scale, version independently)
- Untrusted third-party code needs isolation

ISMS CORE importers:
- Are internal (parse local files on read-only mounts)
- Share the same dependencies (openpyxl, pandas, markdown)
- Don't need isolation from each other
- Need access to the database (not via API round-trips)

Celery tasks inside the backend container are simpler and more efficient.

### Decision 4: File-First, Platform-Second

The ISMS products (policies, workbooks, guides) work **without the platform**. A customer can use just the files. The platform adds value on top:

| Without Platform | With Platform |
|-----------------|---------------|
| Read policies as files | Search across all policies |
| Open individual workbooks | See aggregated compliance dashboard |
| Manually track gaps | Automated gap detection and tracking |
| No cross-framework view | ISO → NIST → MITRE → CIS mapping |
| Manual evidence collection | Evidence management with freshness alerts |
| No audit trail | Full audit log of who did what when |

This means the platform must never **modify** the source files. Read-only mounts are non-negotiable.

### Decision 5: Stable UUIDs from Day One

Following the OpenCTI datasets pattern, every entity gets a UUID assigned at creation that **never changes**:

- Control groups: UUID derived from `group_code` (deterministic)
- Framework controls: UUID derived from `framework_code + control_id`
- Cross-framework mappings: UUID derived from `source_id + target_id + mapping_type`
- Policies, assessments, requirements: Random UUID assigned on first parse, stored in DB

This enables:
- **Upsert semantics** (re-import without duplicates)
- **Stable URLs** (bookmarkable control pages)
- **Cross-system references** (link from external tools)

### Decision 6: Both Products, One Platform

The platform is not "Framework with Operational bolted on." Both products are peers:

```
Dashboard
├── [Toggle: Framework | Operational | Unified]
├── Compliance Score: 78% (Framework) / 85% (Operational)
├── Controls: 53 groups
│   ├── A.5.1-4 → POL + OP-POL + 3 assessments + 1 checklist
│   ├── A.8.24  → POL + OP-POL + 4 assessments + 1 checklist
│   └── ...
└── Gap Analysis: 12 critical (Framework), 3 critical (Operational)
```

A control group page shows **both** products side-by-side:
- Left: Framework view (POL, IMP-UG/TG, detailed assessments)
- Right: Operational view (OP-POL, compliance checklist)
- Bottom: Unified gap analysis, evidence tracker, framework mappings

### Decision 7: Cytoscape.js for Control Dependency Graph

ISO 27001 controls have ~229 intra-framework dependency relationships (depends-on, enables, feeds-into, supports, implements). Visualising these helps a CISO understand which controls are foundational (A.5.9 Asset Inventory, A.5.12 Classification) and which are dependent (A.8.12 DLP depends on classification).

**Cytoscape.js** chosen over ReactFlow because:
- Canvas-based renderer handles 2000+ nodes without DOM overhead
- Built-in graph algorithms (shortest path, centrality, PageRank)
- Compound nodes for grouping controls by section (A.5, A.6, A.7, A.8)
- CSS-like selectors for edge type filtering (`edge[type="depends-on"]`)

### Decision 8: Control Dependencies as Crosswalk Data

Intra-ISO-27001 control dependencies reuse the existing `cross_framework_mappings` table. Both source and target are `framework_controls` where `framework_id` is ISO 27001. This avoids a new table and leverages the existing crosswalk loader. New `mapping_type` enum values (`depends-on`, `enables`, `feeds-into`, `implements`) distinguish them from inter-framework mappings.

### Decision 10: DB as Permanent Master Source of Truth (Recorded 2026-03-01)

**The DB is master for all control assessment data — always.**

The 188 QA'd Python generators are the *initial* source. They bootstrap the DB with accurate, ISO-aligned assessment requirements (sheets, data validation values, scoring logic, control stacking). Once imported, the DB takes over. Scripts become a derived output, not the origin.

This is a deliberate, permanent architectural decision:

```
Bootstrap (one-time):
  188 generators → Import Pipeline (normalise + QA gate) → PostgreSQL

Platform Operation (ongoing):
  PostgreSQL → WebUI forms (assessment data entry)
             → Workbook import (Excel upload, legacy path)
             → Script regeneration (on-demand, for standalone users)
```

**Why this matters for import pipeline design**: The generator importer (Phase 6) is not a workbook parser — it extracts structured schema data (sheets, DV lists, column layouts, assessment areas) from Python source code. Output is a normalised control schema stored in the DB, not raw file content.

**Key properties**:
- Import pipeline validates against `qa_check_workbooks.py` rules. Controls that fail QA do not import.
- Regenerated scripts are structurally identical (Golden Standard Jinja2 template × DB payload). Zero deviations.
- Workbook import (Phase 2.2/2.3) and WebUI entry (Phase 6.7-6.9) both feed the same DB tables — same schema, same validation rules, regardless of entry path.
- Control stacking (e.g. A.5.32-33, A.8.25-26-29) is preserved as a single assessment unit in the DB schema.

### Decision 11: Per-Organisation Governance Mode (Recorded 2026-03-01)

Policy and implementation content authority is configurable per organisation at onboarding. One flag on the organisation record:

| Mode | Authority | Content Management | Typical User |
|------|-----------|-------------------|-------------|
| **platform** | DB master | Edit in WebUI → DB → MD generated on publish | SMEs, Operational product users |
| **local** | Git/filesystem master | Edit locally → import trigger → DB syncs | Framework users, regulated industries |

**Default recommendations**: Framework product → `local` | Operational product → `platform`

**Platform mode flow**:
```
Admin edits in WebUI → draft saved to DB → formal review + approval → publish → .md generated
```

**Local mode flow**:
```
Admin edits .md locally (IDE/Git) → review via Git PR → import trigger → DB syncs
```

**Schema implications** (must be defined before schema finalisation):
- `organisation.governance_mode`: `platform` | `local`
- `policy.is_editable_in_ui`: derived from governance mode
- `policy_version.edit_source`: `webui` | `import` (audit trail for every change)
- Publishing workflow: approval step in Platform mode; import step in Local mode

### Decision 9: Skip Framework Consolidation Dashboard Workbooks

Each Framework control group has ~4-5 individual assessment workbooks (S1–S5) plus one consolidation/dashboard workbook that aggregates scores from the individual workbooks via normalization scripts.

**The platform imports only individual assessment workbooks (~200), not consolidation dashboards (~53).**

| Reason | Detail |
|--------|--------|
| **Platform replaces consolidation** | Phase 3 dashboard API (Task 3.1) aggregates scores across all control groups in real-time — better than a static Excel rollup |
| **No unique data** | Every data point in the consolidation workbook originates from the individual S1–S5 workbooks |
| **Complex to parse** | Cross-workbook references, normalization formulas, and formula-driven cells add parsing complexity for zero unique data |
| **Quarterly trend tracking** | Individual workbooks use `_YYYYMMDD.xlsx` timestamps. Multiple versions of the same assessment (e.g., quarterly runs) are tracked as versioned assessments, giving compliance trend analysis that the static dashboard never could |

**Operational checklists** include their own dashboard sheet (engine-generated, uniform structure) — these are imported as-is because the dashboard is self-contained within the single workbook.

---

## 6. Comparison with Existing Skeleton

### What to Keep

| File | Decision | Reason |
|------|----------|--------|
| `11_docker_compose.yml` | **Keep + evolve** | Solid foundation, all services correct |
| `20_init_db.sql` | **Replace** with evolved schema (see DATA-MODEL.md) |
| `21_init_frameworks_db.sql` | **Keep mostly** — framework tables are well-designed |
| `30_backend_requirements.txt` | **Keep + update** versions |
| `31_backend_dockerfile` | **Keep + evolve** |
| `31_backend_main.py` | **Replace** with proper FastAPI app structure |
| `32_import_frameworks.py` | **Refactor** into Celery tasks |
| `36_correlation_qa_architecture.md` | **Keep as reference** — methodology is sound |
| `41_frontend_dockerfile` | **Keep** |
| `42_frontend_nginx.conf` | **Keep** |
| `10_env_example` | **Keep + extend** |
| `99_dockerignore` | **Keep** |

### Current Build State (2026-03-08)

| Phase | Name | Status |
|-------|------|--------|
| **0** | Data Model & Datasets | ✅ COMPLETE — 16 framework bundles, 4,748 objects, evolved DB schema |
| **1** | Backend Core | ✅ COMPLETE — FastAPI + SQLAlchemy + Alembic + Auth + CRUD |
| **2** | Importers | ✅ COMPLETE — Policy (143 docs), IMP (376 docs), Workbooks (241 assessments), OpenSearch |
| **3** | Dashboard API | ✅ COMPLETE — Compliance, coverage, gaps, evidence, audit readiness endpoints |
| **4** | React Frontend | ✅ COMPLETE — Dashboard, control explorer, policies, assessments, gaps, evidence, QA, admin, system |
| **5** | Correlation Engine | ✅ COMPLETE — Existence checker (Phase 5.1), keyword + semantic correlation framework |
| **6** | External Document Support | 🔜 NEXT — `ProductType.EXTERNAL`, relaxed parser, amber banners |
| **7** | Assessment Content Bootstrap | 🔜 PLANNED — 188 generators → DB schema import; WebUI forms; script regeneration |
| **8** | ISMS Compass | 🔜 PLANNED — AI gap analysis against Gold Standard (depends on pgvector + Anthropic API key) |

**Key admin endpoints added (beyond PLAN.md v0.2):**
- `GET /admin/sysinfo` — service health, DB counts, OpenSearch index stats, platform config
- `GET /admin/orphans` + `DELETE /admin/orphans` — scan/purge DB records whose file_path no longer exists
- `POST /admin/reindex` — rebuild OpenSearch indices from DB content
- `GET /admin/orphans` — orphan scanner (use after IMP/POL renames)

---

## 7. Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Scope creep** — trying to build OpenCTI-level complexity | High | Minimum viable dashboard first. No GraphQL, no connector marketplace. |
| **Workbook parsing complexity** — ~200 Framework generators produce different structures | Medium | Import only individual assessment workbooks (~200), skip consolidation dashboards (~53). Platform dashboard replaces consolidation. Parse common patterns (headers, status columns, score cells). |
| **Framework data licensing** — ISO text is copyrighted | Medium | Use control IDs + short descriptions only. Link to ISO store. Reference NIST/CIS/MITRE (public). |
| **Two-product complexity** — Framework and Operational have different structures | Medium | Shared control group model with product-specific metadata. Single dashboard with product toggle. |
| **Performance** — parsing ~253 workbooks on sync | Low | Celery async + content hash (skip unchanged files). Incremental sync after first full import. |

---

*This architecture is designed to be built incrementally. Each phase delivers usable value. The platform works with whatever ISMS content exists — it doesn't require 100% completion to be useful.*
