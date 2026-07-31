<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Repository_Structure-2E8B57?style=for-the-badge" alt="ISMS CORE Repository Structure"/>
</p>

<h1 align="center">📂 Repository Structure</h1>

<p align="center">
  <em>Complete map of all folders, files, and artifact types in this repository.</em>
</p>

---

## Artifact Types — What's Inside Each Control Pack

Before reading the folder tree, understand what each artifact type is:

| Artifact | Format | What it is | Who uses it |
|----------|--------|------------|-------------|
| **POL** | Markdown | Governance policy — what the control requires, who owns it, applicable standards. Ready to sign and issue after filling in org name / CISO / effective date. | ISMS Manager → Board / Staff |
| **IMP-UG** | Markdown | Implementation User Guide — how the ISMS Manager implements and operates the control. Roles, process steps, KPIs, review cycles. | ISMS Manager |
| **IMP-TG** | Markdown | Implementation Technical Guide — step-by-step for the engineer. Commands, configs, vendor notes, hardening checklists. | Security Engineer |
| **SCR** | Python 3.11+ | Assessment generator — `python3 generate_*.py` produces a structured Excel compliance workbook. Single dependency: `openpyxl`. | ISMS Manager → Auditor |
| **WKBK** | Excel (.xlsx) | Generated compliance workbook — per-control assessment items, evidence status, scoring, auditor notes. Output of the SCR generator. | Auditor / Control Owner |
| **REF** | Markdown | Reference extracts from the ISO standard text mapped to this control. Cross-references to adjacent Annex A controls. | ISMS Manager / Auditor |
| **CTX** | Markdown | Context document linking this control pack to adjacent and dependent packs — for control stacking and dependency mapping. | ISMS Manager |
| **FORM** | Markdown | Ready-to-use templates: evidence forms, meeting agendas, approval records, risk acceptance forms. | ISMS Manager / Control Owner |

**Operational product:** POL + SCR + WKBK only (no IMP-UG/TG — simpler by design)

**Privacy / Cloud / AI:** POL + IMP-UG + IMP-TG + SCR + WKBK

---

## Top-Level Repository

```
factory_isms/
│
├── README.md                  # Project overview and quick start
├── PARADIGM.md                # Product overview and paradigm shift guide
├── PLATFORM.md                # Platform architecture, features, and full deployment guide (setup instructions included)
├── STRUCTURE.md               # This file
├── COMPLIANCE.md              # 29 compliance assessment modules — coverage notes
├── CONTRIBUTING.md            # QA process and standards
├── PHILOSOPHY.md              # Anti-cargo-cult methodology
├── CODE_OF_CONDUCT.md         # Community standards
├── SECURITY.md                # Vulnerability reporting policy
├── LICENSE                    # AGPL-3.0 — governs the content packs below (dual-licensed, see README §License)
│
├── isms-core-framework/       # 🏗️ ISO 27001:2022 — Full Engineering Product
├── isms-core-operational/     # ⚡ ISO 27001:2022 — Lightweight SME Product
├── isms-core-privacy/         # 🔒 ISO 27701:2025 — Privacy Extension Pack
├── isms-core-cloud/           # ☁️ ISO 27018:2025 — Cloud Extension Pack
├── isms-core-ai/              # 🤖 ISO 42001:2023 — AI Extension Pack
├── isms-core-platform/        # 🖥️ Platform Deployment Package — own LICENSE (Apache 2.0)
├── USER_MANUAL/               # 📖 Full user manual (21 chapters) — served in-app at /docs/user-manual.md
├── COMPLIANCE.md              # 📋 Assessment module coverage
└── screenshots/               # Platform UI screenshots
```

---

## 🏗️ isms-core-framework/ — ISO 27001:2022 Full Engineering

53 control packs covering all 93 Annex A controls. Each pack contains the full artifact set (POL, IMP-UG, IMP-TG, SCR, WKBK, REF, CTX, FORM).

```
isms-core-framework/
│
├── README.md                              # Product overview
├── CONTROLS.md                            # 53 control pack index — start here
├── COVERAGE.md                            # 93 Annex A controls → 53 pack mapping
├── STATUS.md                              # Implementation metrics
├── STACKING.md                            # Control grouping and stacking methodology
├── CHANGELOG.md                           # Version history
│
├── 00-foundation-policies/                # Regulatory framework baseline
│   ├── isms-pol-00-regulatory-framework/
│   │   └── POL/                           # ISMS-POL-00 (EN + FR + DE + IT)
│   └── isms-pol-01-isms-scope/
│       └── POL/                           # ISMS-POL-01 (EN + FR + DE + IT)
│
├── A.5-organisational-controls/           # 21 control packs
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # Governance policy (EN + fr/ + de/ + it/)
│       ├── IMP/
│       │   ├── IMP-UG/                    # User Guide — ISMS Manager
│       │   └── IMP-TG/                    # Technical Guide — Engineer
│       ├── SCR/                           # Python assessment generator(s)
│       ├── WKBK/                          # Generated Excel workbook(s)
│       ├── REF/                           # ISO standard reference extracts
│       ├── CTX/                           # Control context + dependency map
│       └── FORM/                          # Templates and forms
│
├── A.6-people-controls/                   # 4 control packs (same structure)
├── A.7-physical-controls/                 # 6 control packs (same structure)
└── A.8-technological-controls/            # 22 control packs (same structure)
```

**Key files:**
- `CONTROLS.md` — indexed list of all 53 packs with control names and Annex A references
- `COVERAGE.md` — maps the 93 ISO 27001:2022 Annex A controls to the 53 packs (some packs cover multiple controls)
- `STACKING.md` — explains how packs can be stacked for mature organisations

---

## ⚡ isms-core-operational/ — ISO 27001:2022 SME Edition

53 control groups with a lighter artifact set (POL + SCR + WKBK). No implementation guides — the operational policies are designed to be complete and self-contained.

```
isms-core-operational/
│
├── README.md
├── CONTROLS.md                            # 53 control group index
├── STATUS.md
├── CHANGELOG.md
│
├── 00-checklist-engine/                   # Shared checklist generator engine
│
├── A.5-organisational-controls/           # 21 control groups
│   └── isms-a.5.X-X-control-name/
│       ├── POL/                           # OP-POL (EN + fr/ + de/ + it/)
│       ├── SCR/                           # Python compliance checklist generator
│       └── WKBK/                          # Generated Excel checklist
│
├── A.6-people-controls/                   # 4 control groups
├── A.7-physical-controls/                 # 6 control groups
└── A.8-technological-controls/            # 22 control groups
```

---

## 🔒 isms-core-privacy/ — ISO 27701:2025 Privacy Extension Pack

21 control groups across three scopes: controller (a.1.x), processor (a.2.x), and shared (a.3.x).

```
isms-core-privacy/
│
├── README.md
├── 00-checklist-engine/                   # Shared privacy checklist engine
│
├── 00-priv-foundation-policies/           # Foundation policies
│   ├── priv-pol-00-privacy-regulatory-framework/
│   │   └── POL/                           # PRIV-POL-00 (EN + fr/ + de/ + it/)
│   └── priv-pol-01-privacy-governance/
│       └── POL/                           # PRIV-POL-01 (EN + fr/ + de/ + it/)
│
├── privacy-controller/                    # 8 controller control groups (a.1.x)
│   └── priv-a.1.X.X-X-control-name/
│       ├── POL/                           # PRIV-POL (EN + fr/ + de/ + it/)
│       ├── IMP/
│       │   ├── IMP-UG/
│       │   └── IMP-TG/
│       ├── SCR/
│       └── WKBK/
│
├── privacy-processor/                     # 5 processor control groups (a.2.x)
│   └── priv-a.2.X.X-X-control-name/      # Same structure as controller
│
└── privacy-shared/                        # 8 shared control groups (a.3.x)
    └── priv-a.3.X.X-X-control-name/      # Same structure as controller
```

---

## ☁️ isms-core-cloud/ — ISO 27018:2025 Cloud Extension Pack

12 control groups covering PII protection requirements for cloud service providers.

```
isms-core-cloud/
│
├── README.md
└── iso27018-pii-cloud/
    └── cld-a.X-control-name/              # 12 Annex A control groups
        ├── POL/                           # CLD-POL (EN + fr/ + de/ + it/)
        ├── IMP/
        │   ├── IMP-UG/
        │   └── IMP-TG/
        ├── SCR/
        └── WKBK/
```

---

## 🤖 isms-core-ai/ — ISO 42001:2023 AI Extension Pack

12 AI control groups (2 foundation + 10 Annex A) covering AI governance, impact assessment, responsible use, and third-party AI relationships.

```
isms-core-ai/
│
├── README.md
├── 00-checklist-engine/                   # Shared AI checklist engine
│
├── 00-ai-foundation-policies/             # Foundation policies
│   ├── ai-pol-00-ai-regulatory-applicability/
│   │   └── POL/                           # AI-POL-00 (EN + fr/ + de/ + it/)
│   └── ai-pol-01-aims-governance-and-decision-making/
│       └── POL/                           # AI-POL-01 (EN + fr/ + de/ + it/)
│
└── ai-a.X.X-X-control-name/              # 10 Annex A control groups
    ├── POL/                               # AI-POL (EN + fr/ + de/ + it/)
    ├── IMP/
    │   ├── IMP-UG/                        # User Guide — ISMS Manager
    │   └── IMP-TG/                        # Technical Guide — Engineer
    └── SCR/                               # Python compliance checklist generator
```

---

## 🖥️ isms-core-platform/ — Platform Deployment Package

The Docker Compose deployment package. **Images-only distribution** — this directory ships no application source, only what's needed to *run* the stack. `docker-compose.yml` pulls pre-built images (`isms-core-backend`, `-frontend`, `-nginx`, `-opensearch`, `-connectors`, `-feeds`, `-threat-intel`, `-smtp-bridge`, plus one-shot setup/data images) from GHCR, Docker Hub, and a private registry. Full application source (backend, frontend, connectors, feeds, threat-intel, smtp-bridge, nginx, opensearch, datasets) lives in the private `factory_isms_project` working repo and is built into those images — it is not part of this public repo.

```
isms-core-platform/
│
├── .env.example                           # Environment variable template → copy to .env
├── backup.env.example                     # Backup-service environment template
├── docker-compose.yml                     # Multi-service production stack (profile-based, image: not build:)
├── bootstrap.sh                           # First-boot import script (idempotent, safe to re-run)
├── LICENSE                                # Apache 2.0 — governs this directory only (see README §License)
├── .gitignore
│
├── garage/                                # Garage S3 object store (optional profile) — upstream image, config only
│   └── garage.toml                        # Garage configuration, bind-mounted into dxflrs/garage
│
├── schemas/
│   └── init_db.sql                        # PostgreSQL initial schema, bind-mounted into postgres:18-alpine
│
└── certs/                                 # TLS certificate mount point (gitignored — runtime only)
    ├── cert.pem                           # Custom cert (optional — auto-generated if absent)
    └── key.pem                            # Private key (optional)
```

**Services started by `docker-compose.yml`:**

| Container | Role |
|-----------|------|
| `isms-core-nginx` | TLS termination + reverse proxy |
| `isms-core-backend` | FastAPI REST API |
| `isms-core-frontend` | Angular 21 + Material 3 WebUI |
| `isms-core-postgres` | PostgreSQL 18 — primary data store |
| `isms-core-redis` | Redis 8 — session cache + Celery broker |
| `isms-core-opensearch` | OpenSearch 3.x — full-text search + threat intelligence |
| `isms-core-worker` | Celery worker — background import and sync tasks |
| `isms-core-beat` | Celery Beat — nightly evidence archive (02:00 UTC), daily KPI snapshot (06:00 UTC) |
| `isms-core-feeds` | Threat intelligence scheduler — MITRE ATT&CK, ATLAS, CISA KEV, EPSS, NVD CVE/CPE, ENISA EUVD |
| `isms-core-connectors` | Automated evidence runner — 44 connectors, runs continuously |
| `isms-core-dashboards-setup` | One-shot OpenSearch Dashboards provisioning — imports 19 automated dashboards at startup |

Optional profiles (add to deploy command as needed):
- `--profile opensearch-single` — **required** for standard deployment (starts OpenSearch)
- `--profile threat-intel` — OSINT IOC feeds (CIRCL MISP, Botvrij, AbuseIPDB, URLhaus, ThreatFox, SSLBL, AlienVault OTX, Feodo Tracker, RFD, Stopforumspam, MalwareBazaar, Malpedia); requires `THREAT_INTEL_ENABLED=true` in `.env`
- `--profile opensearch-cluster` — 3-node OpenSearch cluster (enterprise)
- `--profile dashboards` — OpenSearch Dashboards UI on port 5601
- `--profile garage` — Garage S3 object store
- `--profile mailpit` — local email catcher (dev)
- `--profile smtp-bridge` — Microsoft 365 / OAuth email relay

---

## 📁 Translation Subdirectories

All POL documents (across all five products) are available in English and three additional languages. The English document lives in `POL/` directly. Translations live in language subdirectories:

```
POL/
├── ISMS-POL-A.5.1 - Information Security Policies.md     # English (canonical)
├── fr/
│   └── ISMS-POL-A.5.1 - Politique de Sécurité de l'Information - FR.md
├── de/
│   └── ISMS-POL-A.5.1 - Informationssicherheitsrichtlinie - DE.md
└── it/
    └── ISMS-POL-A.5.1 - Politica di Sicurezza delle Informazioni - IT.md
```

The same pattern applies to OP-POL, PRIV-POL, CLD-POL, and AI-POL files.

---

## 📋 Screenshots/

Platform UI screenshots referenced in README.md and PLATFORM.md. `light/` and `dark/` subfolders, named `NN_isms_core_feature_name_<theme>.png`. Docs use light only.

---

<p align="center">
  <strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>
