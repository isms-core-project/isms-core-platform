<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Platform-2E8B57?style=for-the-badge" alt="ISMS CORE Platform"/>
</p>

<h1 align="center">🎋 ISMS CORE Platform</h1>

<p align="center">
  <strong>Control-Oriented Real-world Engineering — ISO 27001 · ISO 27701 · ISO 27018</strong>
</p>

<p align="center">
  <a href="https://www.iso.org/standard/27001"><img src="https://img.shields.io/badge/ISO_27001-2022-0066CC?style=flat-square" alt="ISO 27001:2022"/></a>
  <a href="https://www.iso.org/standard/71670.html"><img src="https://img.shields.io/badge/ISO_27701-2025-7030A0?style=flat-square" alt="ISO 27701:2025"/></a>
  <a href="https://www.iso.org/standard/76559.html"><img src="https://img.shields.io/badge/ISO_27018-2025-00897B?style=flat-square" alt="ISO 27018:2025"/></a>
  <a href="isms-core-framework/STATUS.md"><img src="https://img.shields.io/badge/Control_Packs-53_of_53-00AA00?style=flat-square" alt="Control Packs"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL_3.0-9400D3?style=flat-square" alt="License"/></a>
</p>

<p align="center">
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/NIST_CSF_2.0-Mapped-FF6600?style=flat-square" alt="NIST CSF"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/MITRE_ATT&CK_v18-Mapped-DC143C?style=flat-square" alt="MITRE ATT&CK"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/GDPR-Mapped-FFD700?style=flat-square" alt="GDPR"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/Swiss_nDSG-Toolkit-FF0000?style=flat-square" alt="Swiss nDSG"/></a>
  <a href="#-framework-integration"><img src="https://img.shields.io/badge/EU_AI_Act-Mapped-0066CC?style=flat-square" alt="EU AI Act"/></a>
</p>

<p align="center">
  <em>Grows fast. Bends, doesn't break. Built to last.</em> 🎋
</p>

---

## 🎯 What is ISMS CORE?

ISMS CORE is a production-grade **control engineering** platform for building and operating an information security and privacy management system. It treats compliance implementation as an **engineering problem** — not a consulting exercise.

> **New here?** Read [PARADIGM.md](PARADIGM.md) first — it explains how ISMS CORE differs from traditional ISMS approaches, how to choose between products, and what to expect.

ISMS CORE covers **three ISO standards** across **four content products**, all served by one Platform:

<table>
<tr>
<th></th>
<th>🏗️ <a href="isms-core-framework/">Framework</a></th>
<th>⚡ <a href="isms-core-operational/">Operational</a></th>
<th>🔒 <a href="isms-core-privacy/">Privacy</a></th>
<th>☁️ <a href="isms-core-cloud/">Cloud</a></th>
<th>🖥️ <a href="PLATFORM.md">Platform</a></th>
</tr>
<tr>
<td><strong>Standard</strong></td>
<td>ISO 27001:2022</td>
<td>ISO 27001:2022</td>
<td>ISO 27701:2025</td>
<td>ISO 27018:2025</td>
<td>All three</td>
</tr>
<tr>
<td><strong>What</strong></td>
<td>Full SSE engineering product — governance policies, implementation guides, assessment scripts, generated workbooks</td>
<td>Foundation ISMS for SMEs — operational policies with single-sheet compliance checklists</td>
<td>Privacy information management — controller, processor, and shared control groups</td>
<td>PII protection in public cloud — compliance checklists for cloud service providers</td>
<td>API + WebUI — turns all content products into a live compliance management system</td>
</tr>
<tr>
<td><strong>For</strong></td>
<td>Mature security teams, consultants, auditors</td>
<td>SMEs and startups (10–500 people)</td>
<td>Any organisation processing PII as controller or processor</td>
<td>Cloud service providers processing PII on behalf of controllers</td>
<td>Any ISMS CORE user needing dashboards, gap tracking, audit management</td>
</tr>
<tr>
<td><strong>Per control</strong></td>
<td>POL + IMP (UG/TG) + SCR + WKBK + REF + FORM + CTX</td>
<td>OP-POL + SCR + WKBK</td>
<td>PRIV-POL + IMP (UG/TG) + SCR + WKBK</td>
<td>CLD-POL + IMP (UG/TG) + SCR + WKBK</td>
<td>Ingests all products — no content of its own</td>
</tr>
<tr>
<td><strong>Groups</strong></td>
<td>53 control packs / 93 Annex A controls</td>
<td>53 control groups / 93 Annex A controls</td>
<td>21 control groups (8 controller + 5 processor + 8 shared)</td>
<td>12 Annex A control groups</td>
<td>87 total groups across all products</td>
</tr>
<tr>
<td><strong>Artifacts</strong></td>
<td>376 IMP docs, 188 Python scripts, 188 Excel workbooks</td>
<td>53 operational policies, 53 checklist scripts</td>
<td>23 PRIV-POL, 42 IMP docs, 21 checklist scripts</td>
<td>12 CLD-POL, 24 IMP docs, 12 checklist scripts</td>
<td>FastAPI + PostgreSQL + Redis + OpenSearch + React WebUI</td>
</tr>
<tr>
<td><strong>Status</strong></td>
<td><img src="https://img.shields.io/badge/v1.0-Complete-00AA00?style=flat-square" alt="Complete"/></td>
<td><img src="https://img.shields.io/badge/v0.1-Complete-00AA00?style=flat-square" alt="Complete"/></td>
<td><img src="https://img.shields.io/badge/v1.0-Complete-00AA00?style=flat-square" alt="Complete"/></td>
<td><img src="https://img.shields.io/badge/v1.0-Complete-00AA00?style=flat-square" alt="Complete"/></td>
<td><img src="https://img.shields.io/badge/Live_(v2.0)-2E8B57?style=flat-square" alt="Live (v2.0)"/></td>
</tr>
</table>

### 🧭 Who this is for (and not for)

**This is for:**
- Security teams building an ISMS and wanting **repeatable evidence**
- Engineers who prefer **automation + tests** over "security theater"
- SMEs that need **practical, audit-ready policies** without over-engineering
- Organisations processing PII that need **ISO 27701 controller/processor controls**
- Cloud service providers that need **ISO 27018 PII protection compliance**
- Consultants and auditors who need **structured, traceable control packs**

**This is not for:**
- "One-click compliance" expectations
- Legal interpretations of GDPR/DORA/NIS2 (use counsel)
- Running scripts you haven't reviewed (treat this like code)

---

## 📂 Repository Structure

```
factory_isms/
├── README.md                           # This file
├── PARADIGM.md                         # Product overview and paradigm shift guide
├── PLATFORM.md                         # Platform architecture and features
├── GETTING-STARTED.md                  # How to run the Platform (Docker setup)
├── CONTRIBUTING.md                     # QA process and standards
├── PHILOSOPHY.md                       # Anti-cargo-cult methodology
├── CODE_OF_CONDUCT.md                  # Community standards
├── SECURITY.md                         # Vulnerability reporting
├── LICENSE                             # AGPL-3.0
│
├── isms-core-framework/                # 🏗️ ISO 27001:2022 — Full Engineering Product
│   ├── README.md
│   ├── CONTROLS.md                     # 53 control pack index
│   ├── COVERAGE.md                     # 93 Annex A → 53 pack mapping
│   ├── STATUS.md                       # Implementation metrics
│   ├── STACKING.md                     # Control grouping methodology
│   ├── CHANGELOG.md
│   ├── 00-foundation-policies/         # Regulatory framework (POL-00, POL-01)
│   ├── A.5-organisational-controls/    # 21 control packs
│   ├── A.6-people-controls/            # 4 control packs
│   ├── A.7-physical-controls/          # 6 control packs
│   └── A.8-technological-controls/     # 22 control packs
│       └── isms-a.X.X-control-name/
│           ├── POL/    ├── IMP/    ├── SCR/    ├── WKBK/
│           ├── REF/    ├── CTX/    └── FORM/
│
├── isms-core-operational/              # ⚡ ISO 27001:2022 — Lightweight SME Product
│   ├── README.md
│   ├── CONTROLS.md
│   ├── STATUS.md
│   ├── CHANGELOG.md
│   ├── 00-checklist-engine/            # Shared checklist generator engine
│   ├── A.5-organisational-controls/    # 21 control groups
│   ├── A.6-people-controls/            # 4 control groups
│   ├── A.7-physical-controls/          # 6 control groups
│   └── A.8-technological-controls/     # 22 control groups
│       └── isms-a.X.X-control-name/
│           ├── POL/    ├── SCR/    └── WKBK/
│
├── isms-core-privacy/                  # 🔒 ISO 27701:2025 — Privacy Extension Pack
│   ├── README.md
│   ├── 00-checklist-engine/            # Shared privacy checklist engine
│   ├── 00-priv-foundation-policies/    # PRIV-POL-00 + PRIV-POL-01
│   ├── privacy-controller/             # 8 controller control groups (a.1.x)
│   ├── privacy-processor/              # 5 processor control groups (a.2.x)
│   └── privacy-shared/                 # 8 shared control groups (a.3.x)
│       └── priv-a.X.X-X-control-name/
│           ├── POL/    ├── IMP/    ├── SCR/    └── WKBK/
│
├── isms-core-cloud/                    # ☁️ ISO 27018:2025 — Cloud Extension Pack
│   ├── README.md
│   └── iso27018-pii-cloud/
│       └── cld-a.X-control-name/       # 12 Annex A control groups
│           ├── POL/    ├── IMP/    ├── SCR/    └── WKBK/
│
├── isms-core-platform/                 # 🖥️ Production Deployment Package
│   ├── .env.example                    # Environment variable template (copy → .env)
│   ├── docker-compose.yml              # 8-service production stack
│   ├── bootstrap.sh                    # First-boot import script
│   ├── backend/                        # FastAPI application
│   ├── frontend/                       # React 19 + MUI 6 UI
│   ├── nginx/                          # Reverse proxy + TLS (A.8.24)
│   ├── datasets/data/                  # 18 JSON reference datasets
│   └── schemas/                        # PostgreSQL init schema
│
└── screenshots/                        # Platform UI screenshots
```

---

## 🚀 Quick Start

### Framework (ISO 27001:2022 — Full SSE Engineering)

1. Browse [isms-core-framework/CONTROLS.md](isms-core-framework/CONTROLS.md) for the control pack index
2. Navigate to a control folder and read POL → IMP-UG → IMP-TG
3. Run a generator to produce an assessment workbook:

```bash
cd isms-core-framework/A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR
python3 generate_a824_1_data_transmission_assessment.py
```

**Prerequisites:** Python 3.11+, `pip install openpyxl`

### Operational (ISO 27001:2022 — Foundation ISMS for SMEs)

1. Browse [isms-core-operational/CONTROLS.md](isms-core-operational/CONTROLS.md)
2. Navigate to a control folder and read the OP-POL
3. Generate the compliance checklist and work through each requirement:

```bash
cd isms-core-operational/A.5-organisational-controls/isms-a.5.1-2-information-security-policies/SCR
python3 generate_op_checklist_a512.py
```

### Privacy (ISO 27701:2025 — Privacy Extension Pack)

1. Browse `isms-core-privacy/` — choose controller, processor, or shared section
2. Read the PRIV-POL for your control group
3. Generate the compliance checklist:

```bash
cd isms-core-privacy/privacy-controller/priv-a.1.2.2-5-lawful-basis-and-consent/SCR
python3 generate_priv_checklist_a1225.py
```

**Prerequisites:** Python 3.11+, `pip install openpyxl`

### Cloud (ISO 27018:2025 — Cloud Extension Pack)

1. Browse `isms-core-cloud/iso27018-pii-cloud/`
2. Read the CLD-POL for your control group
3. Generate the compliance checklist:

```bash
cd isms-core-cloud/iso27018-pii-cloud/cld-a.11-information-security/SCR
python3 generate_cld_checklist_a11.py
```

### Platform (Live Compliance Dashboard — All Products)

1. Read [PLATFORM.md](PLATFORM.md) — the full deployment guide
2. Ensure Docker 24+ and Docker Compose v2 are installed
3. Copy `.env.example` → `.env`, set all required secrets + `ADMIN_PASSWORD`
4. `docker compose up -d`
5. `bash bootstrap.sh` — run once, imports all content automatically
6. Open `https://{HOST_IP}` — accept self-signed cert (or configure TLS in PLATFORM.md)
7. Login: `ADMIN_EMAIL` / `ADMIN_PASSWORD` from your `.env`

---

## 📸 Platform Screenshots

<table>
<tr>
<td align="center"><strong>Login</strong><br/><img src="screenshots/01_isms-core_logon.png" width="380" alt="Login screen"/></td>
<td align="center"><strong>Home Dashboard</strong><br/><img src="screenshots/02_isms-core_home.png" width="380" alt="Home dashboard — ISMS + Privacy + Cloud product switcher"/></td>
</tr>
<tr>
<td align="center"><strong>Compliance Overview</strong><br/><img src="screenshots/03_isms-core-oveview.png" width="380" alt="Compliance overview — 54 controls, 100% coverage, 77.4% audit readiness"/></td>
<td align="center"><strong>Connectors</strong><br/><img src="screenshots/07_isms-core_connectors.png" width="380" alt="Automated evidence connectors — MS Entra ID, Defender, M365, Azure CSPM"/></td>
</tr>
<tr>
<td align="center"><strong>ISMS Compass (AI Gap Analysis)</strong><br/><img src="screenshots/05_isms-core_compass.png" width="380" alt="ISMS Compass — AI-powered gap analysis against Gold Standard"/></td>
<td align="center"><strong>System Status</strong><br/><img src="screenshots/08_isms-core_system.png" width="380" alt="System status — all services healthy, 87 groups, OpenSearch green"/></td>
</tr>
</table>

---

## 🔗 Framework Integration

<table>
<tr>
<th>Framework / Standard</th>
<th>What ISMS CORE provides</th>
<th>Status</th>
</tr>
<tr>
<td>ISO/IEC 27001:2022</td>
<td>Full Annex A control packs (Framework + Operational)</td>
<td><img src="https://img.shields.io/badge/Complete-0066CC?style=flat-square" alt="Complete"/></td>
</tr>
<tr>
<td>ISO/IEC 27002:2022</td>
<td>Implementation guidance integrated into IMP-TG documents</td>
<td><img src="https://img.shields.io/badge/Integrated-0066CC?style=flat-square" alt="Integrated"/></td>
</tr>
<tr>
<td>ISO/IEC 27701:2025</td>
<td>Full Privacy Extension Pack — controller, processor, and shared controls</td>
<td><img src="https://img.shields.io/badge/Complete-7030A0?style=flat-square" alt="Complete"/></td>
</tr>
<tr>
<td>ISO/IEC 27018:2025</td>
<td>Full Cloud Extension Pack — 12 Annex A control groups for PII in cloud</td>
<td><img src="https://img.shields.io/badge/Complete-00897B?style=flat-square" alt="Complete"/></td>
</tr>
<tr>
<td>NIST CSF 2.0</td>
<td>Control mapping and grouping across all 53 ISMS groups</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>NIST SP 800-53 Rev. 5</td>
<td>Security control cross-mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-FF6600?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>MITRE ATT&CK v18</td>
<td>Threat technique mapping (Enterprise / ICS / Mobile)</td>
<td><img src="https://img.shields.io/badge/v18-DC143C?style=flat-square" alt="v18"/></td>
</tr>
<tr>
<td>EU GDPR / Swiss nDSG</td>
<td>Security and privacy control mapping, operational checklists</td>
<td><img src="https://img.shields.io/badge/Toolkit-FFD700?style=flat-square" alt="Toolkit"/></td>
</tr>
<tr>
<td>DORA / NIS2</td>
<td>Operational resilience mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-FFD700?style=flat-square" alt="Mapped"/></td>
</tr>
<tr>
<td>EU AI Act</td>
<td>AI risk management mapping</td>
<td><img src="https://img.shields.io/badge/Mapped-0066CC?style=flat-square" alt="Mapped"/></td>
</tr>
</table>

---

## ✈️ Philosophy: Not Cargo Cult

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
> — Richard Feynman

ISMS CORE avoids **cargo-cult compliance** where formal structures exist without verifiable effectiveness:

| | Cargo Cult | ISMS CORE |
|---|---|---|
| ❌ | Impressive policies nobody reads | ✅ Controls that **actually work** |
| ❌ | Made-up compliance numbers | ✅ Evidence that **proves effectiveness** |
| ❌ | Security theater for audits | ✅ Metrics that **measure real security** |
| ❌ | PowerPoints instead of controls | ✅ Automation that **enforces compliance** |

See [PHILOSOPHY.md](PHILOSOPHY.md) for the full methodology.

---

## 🔬 Quality Assurance

Every control pack undergoes a structured multi-stage validation process before promotion to this repository:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────────┐
│  Claude Code     │────▶│  ISMS QA Engine  │────▶│   The ISMS Core Project    │
│  (Build + QA)    │     │  (Existence +    │     │   (Final Approval)   │
│                  │     │   Keyword +      │     │                      │
└──────────────────┘     │   Semantic)      │     └──────────────────────┘
   Implementation        └──────────────────┘          Final gate
   + Code Review           3-layer QA check
```

All 188 Framework generators, 53 Operational policies, 21 Privacy control groups, and 12 Cloud control groups carry `QA_VERIFIED` markers confirming they have passed the full QA process.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed QA standards.

---

## 📊 Status

### ISO 27001:2022 — ISMS Framework

| Metric | Value | Status |
|--------|-------|--------|
| Control packs | **53 of 53** | ![100%](https://img.shields.io/badge/100%25-00AA00?style=flat-square) |
| Annex A controls mapped | **93 of 93** | ![Mapped](https://img.shields.io/badge/Mapped-32CD32?style=flat-square) |
| Python generators | **188** (307K+ lines) | ![Validated](https://img.shields.io/badge/Validated-0066CC?style=flat-square) |
| IMP documents | **376** (188 UG + 188 TG) | ![Complete](https://img.shields.io/badge/Complete-0066CC?style=flat-square) |

### ISO 27001:2022 — ISMS Operational

| Metric | Value | Status |
|--------|-------|--------|
| Control groups | **53 of 53** | ![100%](https://img.shields.io/badge/100%25-00AA00?style=flat-square) |
| Operational policies | **53** | ![Complete](https://img.shields.io/badge/Complete-00AA00?style=flat-square) |
| Checklist generators | **53** | ![Complete](https://img.shields.io/badge/Complete-00AA00?style=flat-square) |

### ISO 27701:2025 — Privacy Extension Pack

| Metric | Value | Status |
|--------|-------|--------|
| Control groups | **21 of 21** | ![100%](https://img.shields.io/badge/100%25-7030A0?style=flat-square) |
| Controller groups | **8** (a.1.x) | ![Complete](https://img.shields.io/badge/Complete-7030A0?style=flat-square) |
| Processor groups | **5** (a.2.x) | ![Complete](https://img.shields.io/badge/Complete-7030A0?style=flat-square) |
| Shared groups | **8** (a.3.x) | ![Complete](https://img.shields.io/badge/Complete-7030A0?style=flat-square) |
| PRIV-POL documents | **23** (21 + 2 foundation) | ![Complete](https://img.shields.io/badge/Complete-7030A0?style=flat-square) |
| IMP documents | **42** (21 UG + 21 TG) | ![Complete](https://img.shields.io/badge/Complete-7030A0?style=flat-square) |

### ISO 27018:2025 — Cloud Extension Pack

| Metric | Value | Status |
|--------|-------|--------|
| Control groups | **12 of 12** | ![100%](https://img.shields.io/badge/100%25-00897B?style=flat-square) |
| CLD-POL documents | **12** | ![Complete](https://img.shields.io/badge/Complete-00897B?style=flat-square) |
| IMP documents | **24** (12 UG + 12 TG) | ![Complete](https://img.shields.io/badge/Complete-00897B?style=flat-square) |

### Platform

| Metric | Value | Status |
|--------|-------|--------|
| Platform (API + WebUI) | v1.0 live — 44 connectors | ![Live](https://img.shields.io/badge/Live-2E8B57?style=flat-square) |
| Products integrated | ISMS + Privacy + Cloud | ![v2.0](https://img.shields.io/badge/v2.0-2E8B57?style=flat-square) |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [PARADIGM.md](PARADIGM.md) | 🧭 Product overview and paradigm shift guide |
| [PLATFORM.md](PLATFORM.md) | 🖥️ Platform architecture, features, and design decisions |
| [GETTING-STARTED.md](GETTING-STARTED.md) | 🚀 How to run the Platform (Docker Compose setup guide) |
| [isms-core-framework/CONTROLS.md](isms-core-framework/CONTROLS.md) | 📋 Framework control pack index (53 packs) |
| [isms-core-framework/COVERAGE.md](isms-core-framework/COVERAGE.md) | 🗺️ 93 Annex A controls → 53 pack mapping |
| [isms-core-framework/STATUS.md](isms-core-framework/STATUS.md) | 📊 Framework metrics |
| [isms-core-framework/STACKING.md](isms-core-framework/STACKING.md) | 🔗 Control grouping methodology |
| [isms-core-operational/CONTROLS.md](isms-core-operational/CONTROLS.md) | 📋 Operational control group index (53 groups) |
| [isms-core-operational/STATUS.md](isms-core-operational/STATUS.md) | 📊 Operational metrics |
| [PHILOSOPHY.md](PHILOSOPHY.md) | ✈️ Anti-cargo-cult methodology |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 🔧 QA process and standards |
| [SECURITY.md](SECURITY.md) | 🔒 Vulnerability reporting policy |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 🤝 Community standards |

---

## 🔒 Security

- **Vulnerability reporting:** Please report security issues to **info@isms-core.com** (include "ISMS CORE Security" in the subject).
- **Safe usage:** Review scripts before execution. Run in a virtual environment. Treat generated artifacts as sensitive until proven otherwise.
- **No secrets:** Do not commit credentials, tokens, private keys, or customer data to this repository or to generated workbooks.

---

## 📜 License

**Dual-licensed:**
- **AGPL-3.0** for open-source use (see [LICENSE](LICENSE))
- **Commercial license** available for organisations that cannot (or do not want to) comply with AGPL obligations

Commercial licensing: **info@isms-core.com**

---

## 📞 Contact

<p align="center">
  <strong>The ISMS Core Project</strong>
</p>

<p align="center">
  <a href="mailto:info@isms-core.com"><img src="https://img.shields.io/badge/Email-info@isms--core.com-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/isms-core-project"><img src="https://img.shields.io/badge/GitHub-isms--core--project-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

---

<p align="center">
  <strong>Copyright © 2025–2026 The ISMS Core Project. All rights reserved.</strong>
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
