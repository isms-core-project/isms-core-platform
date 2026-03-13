<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Platform-2E8B57?style=for-the-badge" alt="ISMS CORE Platform"/>
</p>

<h1 align="center">🎋 ISMS CORE Platform</h1>

<p align="center">
  <strong>The API and WebUI layer on top of all four ISMS CORE products</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Live_(Phase_8)-00AA00?style=for-the-badge" alt="Live"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI_+_PostgreSQL-0066CC?style=flat-square" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Frontend-React_19_+_MUI_6-61DAFB?style=flat-square" alt="React"/>
  <img src="https://img.shields.io/badge/Deployment-Docker_Compose-2496ED?style=flat-square" alt="Docker"/>
</p>

<p align="center">
  <em>Four products. One platform. All live.</em>
</p>

---

## What is ISMS CORE Platform?

ISMS CORE Platform is the **API and WebUI layer** that transforms all four ISMS CORE products (Framework, Operational, Privacy, Cloud) into a live compliance management system. The policies, assessment workbooks, and implementation guides are the content — Platform is the engine that ingests, correlates, and presents them as a unified operational dashboard covering ISO 27001:2022, ISO 27701:2025, and ISO 27018:2025.

**Without Platform:** You have policy files + Excel workbooks on disk. Excellent paperwork.

**With Platform:** You have a live compliance system — searchable, scored, gap-tracked, evidence-linked, and audit-ready across all three ISO standards.

> **Important:** Platform is additive. All four products work perfectly without it. Platform is the operational layer for teams who need continuous compliance management rather than periodic file reviews.

---

## Architecture

### Six-Service Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                      ISMS CORE Platform                         │
│                                                                  │
│  ┌──────────────────┐   ┌──────────────────┐   ┌─────────────┐  │
│  │   React 19       │◄──│   FastAPI        │──►│ PostgreSQL  │  │
│  │   + MUI 6        │   │   REST API       │   │ 18 Alpine   │  │
│  │   + Recharts     │   │   /api/v1/*      │   │             │  │
│  │   + Cytoscape.js │   │                  │   │ 18 tables   │  │
│  │                  │   │   SQLAlchemy 2.0 │   │ 3 mat views │  │
│  │   Dashboard      │   │   Alembic        │   │ JSONB meta  │  │
│  │   Control view   │   │                  │   └─────────────┘  │
│  │   Gap analysis   │   │   Celery tasks ─►┌───────────────┐    │
│  │   Evidence       │   │                  │  Redis 8       │    │
│  │   Audit trail    │   │                  │  broker+cache  │    │
│  └──────────────────┘   └──────────────────┘   └───────────────┘  │
│                                           │                       │
│                                           ▼                       │
│                                   ┌───────────────┐              │
│                                   │  OpenSearch   │              │
│                                   │  full-text    │              │
│                                   │  search       │              │
│                                   └───────────────┘              │
└─────────────────────────────────────────────────────────────────┘
```

| Service | Technology | Role |
|---------|-----------|------|
| **Backend API** | FastAPI 0.109+ | REST API, auth, business logic, import orchestration |
| **Database** | PostgreSQL 18 (Alpine) | Primary store — all compliance data, structured and relational |
| **Cache + Queue** | Redis 8 (Alpine) | Session cache, Celery task broker |
| **Search** | OpenSearch 3.x | Full-text search over policy and IMP document content |
| **Worker** | Celery 5.3 | Background tasks — import, sync, compliance recalculation |
| **Frontend** | React 19 + Vite | WebUI — dashboards, control explorer, evidence management |

### Data Model

The platform's canonical data model covers:

| Entity | Description |
|--------|-------------|
| **Control Groups** | 87 groups — 54 ISMS (ISO 27001), 21 Privacy (ISO 27701), 12 Cloud (ISO 27018) |
| **Policies** | POL, OP-POL, PRIV-POL, CLD-POL, INS, REF, CTX, FORM — typed, product-tagged, state-tracked |
| **Implementations** | IMP-UG/TG documents, indexed into OpenSearch for full-text search |
| **Assessments** | Excel workbook contents: sheets, items, compliance status per item; Framework, Operational, Privacy, and Cloud checklists |
| **Gaps** | Identified compliance gaps with severity, owner, SLA, remediation tracking |
| **Evidence** | Evidence items linked to control groups, requirements, and/or assessment items |
| **Frameworks** | 18 reference datasets: ISO 27001, NIST CSF 2.0, MITRE ATT&CK v18, GDPR, DORA, NIS2... |
| **Crosswalk Mappings** | Cross-framework relationships: 1,500+ mappings across all loaded frameworks |
| **Audit Log** | Immutable trail of every action (who, what, when, resource) |

### Governance Modes

Platform supports two content authority models, set per organisation at onboarding:

| Mode | Authority | Workflow |
|------|-----------|---------|
| **platform** | DB is master | Edit in WebUI → draft → review → approved → published |
| **local** | Filesystem is master | Edit .md locally → Git PR → import trigger → DB syncs |

**Recommended defaults:** Framework product users → `local` | Operational product users → `platform`

---

## Features

### Current (Phases 0–8 complete as of 2026-03-09)

| Feature | Description |
|---------|-------------|
| **Control Explorer** | Browse all 87 control groups (ISMS + Privacy + Cloud) with compliance scores, policy status, assessment history |
| **Compliance Dashboard** | Aggregated scores across all four products with section breakdown; ISMS / Privacy / Cloud product switcher |
| **Coverage Heatmap** | Policy and assessment coverage by control group and section |
| **Policy Manager** | Browse, filter, preview, and manage all POL/OP-POL/PRIV-POL/CLD-POL/INS/REF/CTX documents |
| **Assessment Tracker** | Framework (188 workbooks), Operational (53 checklists), Privacy (21 checklists), Cloud (12 checklists) with per-item compliance status |
| **Gap Management** | Full gap lifecycle: create, assign, track, close with severity and SLA monitoring |
| **Evidence Tracker** | Evidence items with expiry tracking, verification status, and freshness alerts |
| **Crosswalk Viewer** | Cross-framework mappings: ISO 27001 ↔ NIST CSF ↔ MITRE ATT&CK ↔ GDPR ↔ DORA and more |
| **QA / Existence Checker** | Validate that all expected artifacts are present (Framework, Operational, Privacy, Cloud) |
| **Audit Trail** | Full audit log of all platform actions |
| **Admin Panel** | User management (CRUD), system info, service health, DB stats |
| **Full-Text Search** | Search across all policy and IMP document content via OpenSearch (product-filtered) |
| **RBAC** | Role-based access: Admin / ISMS Manager / Auditor / Control Owner / Viewer |
| **Approval Workflow** | Content state lifecycle: draft → review → approved → published |
| **Privacy Product** | 21 ISO 27701:2025 control groups — 23 PRIV-POL + 42 PRIV-IMP (UG/TG) imported; 21 SCR generators; compliance checklists in Assessments |
| **Cloud Product** | 12 ISO 27018:2025 control groups — 12 CLD-POL + 24 CLD-IMP (UG/TG) imported; 12 SCR generators; compliance checklists in Assessments |
| **ISMS Compass** | AI gap analysis against Gold Standard (Anthropic API — Phase 8) |

### Planned

| Feature | Phase | Description |
|---------|-------|-------------|
| **Script Regeneration** | Phase 10 | Jinja2 template × DB payload → .py per control group |

---

## Data Sources

The platform ingests from two sources:

**1. Content files (read-only mounts):**
```
/app/isms-framework/    → isms-core-framework/   (POL, IMP, SCR, WKBK, REF, CTX, FORM)
/app/isms-operational/  → isms-core-operational/ (OP-POL, SCR, WKBK)
/app/isms-privacy/      → isms-core-privacy/     (PRIV-POL, SCR, WKBK)
/app/isms-cloud/        → isms-core-cloud/       (CLD-POL, SCR, WKBK)
```

**2. Reference datasets (bundled):**
```
/app/datasets/    → 18 JSON bundles (ISO 27001, NIST CSF 2.0, MITRE ATT&CK v18,
                    NIST 800-53, CIS Controls, GDPR, DORA, NIS2, PCI DSS, FINMA,
                    OWASP ASVS, OWASP Top 10, EU AI Act, Swiss nDSG, CIS Benchmarks,
                    SOC 2, ISO 27002, MITRE D3FEND)
```

Content files are **never modified** by the platform. All edits flow through the API and are stored in PostgreSQL. Script/workbook regeneration produces new files — it does not overwrite the mounted originals.

---

## RBAC — Roles and Permissions

| Role | Capabilities |
|------|-------------|
| **Admin** | Full access — user management, system config, governance mode, sync triggers, content approval |
| **ISMS Manager** | All controls, assessments, gaps, evidence. Cannot manage users or system config. |
| **Auditor** | Read-only access to everything. Can export reports. |
| **Control Owner** | Read/write on assigned control groups only. |
| **Viewer** | Read-only on non-confidential items. |

---

## Design Decisions

**DB as master** — The PostgreSQL database is the permanent source of truth for all compliance data. The 188 QA'd generators bootstrap the DB once; after that, the DB drives everything. Scripts and workbooks become derived outputs.

**File-first, platform-second** — FRAMEWORK and OPERATIONAL work without Platform. Source files are mounted read-only. Platform adds correlation, dashboards, and audit management on top. It never locks you in.

**REST over GraphQL** — 30 entity types, one client, predictable query patterns. REST with Pydantic + auto-generated OpenAPI docs is simpler and faster to maintain than GraphQL + Relay for this use case.

**Celery inside backend** — Importers are internal (parse local files), share the same Python dependencies, and don't need container isolation from each other. Celery tasks are simpler and more efficient than separate connector containers.

**Docker-first deployment** — Self-contained, runs on a NUC. No Kubernetes, no cloud dependencies. `docker compose up -d` and it works.

---

## Getting Started

See [GETTING-STARTED.md](GETTING-STARTED.md) for full setup and launch instructions.

**Quick summary:**
1. Install Docker 24+ and Docker Compose v2
2. Clone this repository
3. Copy `.env.example` → `.env`, fill in three secrets
4. `docker compose up -d`
5. Open `http://localhost:3000`
6. Login: `admin@isms-core.dev` / `admin123` — **change on first login**
7. Run initial import via Admin → System → Import

---

## Repository Layout (Platform code)

The Platform source lives in the `platform/` directory (to be added when released):

```
platform/
├── backend/                  # FastAPI application
│   ├── src/
│   │   ├── api/v1/          # Route handlers (controls, policies, gaps, evidence...)
│   │   ├── domain/          # SQLAlchemy models
│   │   ├── schemas/         # Pydantic request/response models
│   │   ├── services/        # Business logic
│   │   ├── importers/       # Policy/IMP/workbook parsers + framework loader
│   │   └── core/            # Auth, dependencies, config
│   └── alembic/             # DB migrations
├── frontend/                 # React 19 + Vite
│   └── src/
│       └── pages/           # Dashboard, Controls, Policies, Gaps, Evidence...
├── schemas/
│   └── init_db.sql          # Full DB schema (reference)
├── datasets/
│   └── data/                # 18 reference framework JSON bundles
├── docker-compose.yml
└── .env.example
```

---

<p align="center">
<strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
<em>Where bamboo antennas actually work.</em> 🎋
</p>
