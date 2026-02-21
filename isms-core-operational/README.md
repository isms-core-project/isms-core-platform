<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Operational-FF6600?style=for-the-badge" alt="ISMS CORE Operational"/>
</p>

<h1 align="center">🎋 ISMS CORE Operational</h1>

<p align="center">
  <strong>Foundation ISMS for SMEs — Operational Policies + Compliance Checklists</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Operational_Policies-53-FF6600?style=flat-square" alt="53 OP-POLs"/>
  <img src="https://img.shields.io/badge/Compliance_Checklists-53-3776AB?style=flat-square" alt="53 Checklists"/>
  <img src="https://img.shields.io/badge/Annex_A_Controls-93_Covered-32CD32?style=flat-square" alt="93 Controls"/>
  <img src="https://img.shields.io/badge/Swiss_nFADP-Aligned-FF0000?style=flat-square" alt="Swiss nFADP"/>
</p>

---

## What is ISMS CORE Operational?

ISMS CORE Operational (Foundation ISMS for SMEs) is a **complete, practical ISMS** for small and mid-size companies. Each of the 53 control groups gets:

1. **One operational policy (OP-POL)** — a self-contained document that combines policy requirements with enough operational guidance to implement
2. **One compliance checklist workbook (WKBK)** — a single-sheet Excel checklist that extracts every "shall" requirement from the policy, ready to track compliance status and evidence
3. **One generator script (SCR)** — a Python script that produces the checklist workbook from the policy, keeping it in sync as policies evolve

No multi-layer stacks, no 10-sheet assessment workbooks, no implementation guides — just what an SME needs to **get certified and stay certified**.

**Target audience:** Small and mid-size companies (10–500 people) that need practical, audit-ready ISMS documentation without the overhead of a full governance framework.

---

## What You Get Per Control Group

<table>
<tr>
<td align="center"><strong>📜 OP-POL</strong><br/>Operational Policy</td>
<td align="center"><strong>🐍 SCR</strong><br/>Generator Script</td>
<td align="center"><strong>📊 WKBK</strong><br/>Compliance Checklist</td>
</tr>
<tr>
<td>Requirements, guidance,<br/>roles, evidence expectations</td>
<td>Python script that extracts<br/>"shall" requirements → Excel</td>
<td>Single-sheet checklist:<br/>Requirement / Status / Evidence / Owner</td>
</tr>
</table>

### OP-POL Structure

Every operational policy follows a consistent structure:

| Section | Purpose |
|---------|---------|
| **Document Version Control** | Version tracking |
| **Purpose** | Why this policy exists (includes Swiss nFADP alignment) |
| **Scope** | What and who it covers |
| **Principle** | Core security principles |
| **Domain sections** | Specific requirements and operational guidance |
| **Definitions** | Key terms |
| **Roles and Responsibilities** | RACI-style accountability |
| **Evidence of Compliance** | What proves implementation |
| **Policy Compliance** | Measurement, exceptions, non-compliance, continual improvement |
| **ISO 27001 Controls Mapping** | ISO 27001:2022 + ISO 27002:2022 + NIST CSF 2.0 + CIS v8 |
| **Regulatory Framework** | Swiss nFADP, GDPR (where applicable), SOC 2 mapping |

### Compliance Checklist Columns

| Column | Purpose |
|--------|---------|
| **Requirement** | What the OP-POL says you shall do |
| **Status** | Compliant / Partial / Non-Compliant / N/A |
| **Evidence** | What proves it |
| **Owner** | Who's responsible |
| **Notes** | Gaps, actions, dates |

---

## Directory Structure

```
isms-core-operational/
├── A.5-organizational-controls/        # 21 control groups
│   └── isms-a.5.X-control-name/
│       ├── POL/
│       │   └── ISMS-OP-POL-A.5.X - Policy Title.md
│       ├── SCR/
│       │   └── generate_op_checklist_a5X.py
│       └── WKBK/
│           └── ISMS-OP-CHK-A.5.X_Compliance_Checklist_YYYYMMDD.xlsx
├── A.6-people-controls/                # 4 control groups
├── A.7-physical-controls/              # 6 control groups
└── A.8-technological-controls/         # 22 control groups
```

---

## Quick Start

### 1) Read the policy
Navigate to a control group and read the OP-POL. It tells you what's required, who's responsible, and what evidence you need.

### 2) Generate the checklist
```bash
cd isms-core-operational/A.8-technological-controls/isms-a.8.24-use-of-cryptography/SCR
python3 generate_op_checklist_a824.py
```

**Prerequisites:** Python 3.11+, `pip install openpyxl`

### 3) Work through the checklist
Open the generated Excel workbook and assess each requirement:
- Mark status (Compliant / Partial / Non-Compliant / N/A)
- Record your evidence
- Assign owners for gaps
- Track remediation in the Notes column

That's your audit evidence.

---

## Control Coverage

All 53 ISO 27001:2022 Annex A control groups are covered:

| Section | Control Groups | Annex A Controls |
|---------|---------------|-----------------|
| **A.5** Organisational Controls | 21 | 37 |
| **A.6** People Controls | 4 | 8 |
| **A.7** Physical Controls | 6 | 14 |
| **A.8** Technological Controls | 22 | 34 |
| **Total** | **53** | **93** |

---

## Regulatory Alignment

All policies are aligned to **Swiss nFADP (revDSG)** as the primary data protection baseline, with GDPR referenced where applicable. Key design decisions:

- **Swiss nFADP** as primary data protection framework
- **GDPR** referenced where applicable (cross-border, EU customers)
- **SOC 2** trust service criteria mapped where relevant
- **Technical standards** updated to reflect current industry best practices
- **PCI DSS** gated or removed from baseline (opt-in for organisations in scope)

---

## Documentation

| Document | Description |
|----------|-------------|
| [CONTROLS.md](CONTROLS.md) | Control pack index with all 53 packs |
| [STATUS.md](STATUS.md) | Current progress and metrics |
| [CHANGELOG.md](CHANGELOG.md) | Version history and release notes |

---

## Relationship to ISMS CORE Framework (SSE)

ISMS CORE Operational is the **foundation ISMS product** — everything an SME needs, nothing it doesn't. For organisations that need the full SSE engineering stack (multi-sheet assessment workbooks, implementation guides, technical specifications), see [ISMS CORE Framework (SSE)](../isms-core-framework/).

| | Operational (Foundation ISMS) | Framework (SSE) |
|---|---|---|
| **Audience** | SMEs and startups (10–500 people) | Mature security teams and consultants |
| **Per control group** | OP-POL + SCR + WKBK | POL + IMP (UG/TG) + SCR + WKBK + REF + CTX |
| **Policy style** | Self-contained — requirements + guidance in one document | Governance policy (what/who) separated from implementation (how) |
| **Checklist** | Single-sheet compliance checklist | Multi-sheet assessment workbooks with automated scoring |
| **Effort to implement** | Weeks | Months |
| **Upgrade path** | Migrate to Framework (SSE) when you outgrow Operational | — |

### When to use which

**Start with Operational if:**
- You're building your first ISMS
- Your security team is 1–3 people
- You need to get certified in months, not years
- You want practical policies your team will actually read

**Start with Framework (SSE) if:**
- You already have a GRC programme
- You manage multiple compliance frameworks (ISO + GDPR + DORA + NIS2)
- You need detailed assessment evidence with automated scoring
- You have dedicated compliance or audit staff

---

<p align="center">
  <em>Part of <a href="../README.md">ISMS CORE Platform</a></em> 🎋
</p>