<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Operational-FF6600?style=for-the-badge" alt="ISMS CORE Operational"/>
</p>

<h1 align="center">🎋 ISMS CORE Operational</h1>

<p align="center">
  <strong>Operational Policies — Lightweight SME Product</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Operational_Policies-53-FF6600?style=flat-square" alt="53 OP-POLs"/>
  <img src="https://img.shields.io/badge/Annex_A_Controls-93_Covered-32CD32?style=flat-square" alt="93 Controls"/>
  <img src="https://img.shields.io/badge/Swiss_nFADP-Aligned-FF0000?style=flat-square" alt="Swiss nFADP"/>
</p>

---

## What is ISMS CORE Operational?

ISMS CORE Operational provides **one operational policy per control group** — a single, self-contained document that combines policy requirements with enough operational guidance to implement. No multi-layer stacks, no assessment workbooks, no generator scripts.

**Target audience:** SMEs and startups that need practical, audit-ready ISMS policies without the full Framework engineering stack.

---

## What each OP-POL contains

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

---

## Directory Structure

```
isms-core-operational/
├── A.5-organizational-controls/        # 21 control groups
│   └── isms-a.5.X-control-name/
│       └── POL/10_pol-md/
│           └── ISMS-OP-POL-A.5.X - Policy Title.md
├── A.6-people-controls/                # 4 control groups
├── A.7-physical-controls/              # 6 control groups
└── A.8-technological-controls/         # 22 control groups
```

**No IMP, SCR, WKBK, REF, CTX, or FORM folders.** Operational is POL-only by design.

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

All policies are aligned to **Swiss nFADP (revDSG)** as the primary data protection baseline, with GDPR referenced where applicable. Key conversions from the source material:

- UK Data Protection Act 2018 → Swiss nFADP (revDSG)
- ICO → competent data protection authority
- GDPR timelines → applicable legal timeframes
- EEA/UK adequacy decisions → CH transfer assessment process
- Technical standards modernised (TLS 1.2+, 12-char passwords, MFA required)

---

## Relationship to ISMS CORE Framework

ISMS CORE Operational is the **entry-level product**. For organisations that need the full engineering stack, see [ISMS CORE Framework](../isms-core-framework/) — governance policies with implementation guides, assessment scripts, and generated workbooks.

| | Operational | Framework |
|---|---|---|
| **Audience** | SMEs and startups | Mature security teams |
| **Per control group** | One OP-POL | POL + IMP (UG/TG) + SCR + WKBK + REF + CTX |
| **Depth** | Policy + operational guidance | Full assessment workbooks with automated scoring |
| **Effort** | Practical minimum for audit readiness | Comprehensive implementation |

---

<p align="center">
  <em>Part of <a href="../README.md">ISMS CORE Platform</a></em> 🎋
</p>
