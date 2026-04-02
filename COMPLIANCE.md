<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Compliance_Assessments-2E8B57?style=for-the-badge" alt="ISMS CORE Compliance Assessments"/>
</p>

<h1 align="center">🎋 ISMS CORE — Compliance Assessment Modules</h1>

<p align="center">
  <strong>Eleven built-in frameworks + custom YAML import. One platform. No separate tools required.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frameworks-10-2E8B57?style=flat-square" alt="10 Frameworks"/>
  <img src="https://img.shields.io/badge/Requirements-500+-0066CC?style=flat-square" alt="500+ Requirements"/>
  <img src="https://img.shields.io/badge/Export-CSV_%7C_XLSX_%7C_PDF-FF6600?style=flat-square" alt="Export"/>
  <img src="https://img.shields.io/badge/Assessment_Collections-Grouping_%26_Reports-2E7D32?style=flat-square" alt="Collections"/>
</p>

---

## Overview

ISMS CORE Platform includes a unified compliance assessment layer covering 11 built-in frameworks across Europe and North America, plus custom YAML import for any sector-specific or proprietary control framework. Each module provides structured self-assessment, maturity scoring (0–4 where applicable), gap tracking, and export.

Assessment results can be grouped into **Assessment Collections** — named bundles that aggregate status across multiple frameworks for reporting or audit purposes, with CSV, XLSX (colour-coded), and PDF (A4) export.

All compliance assessment modules live under the **Compliance Assessments** sidebar group in the Platform WebUI.

---

## Quick Reference

| Framework | Type | Requirements | Grouping | Scoring | Audience |
|-----------|------|-------------|----------|---------|----------|
| [NIST CSF 2.0](#nist-csf-20) | NIST | 106 subcategories | 6 Functions | Tier 1–4 | Any sector |
| [NIS2](#nis2-directive-eu-20222555) | EU Directive | 15 requirements | 2 Articles | 0–4 | EU essential/important entities |
| [DORA](#dora-eu-20222554) | EU Regulation | 25 articles | 4 Chapters | 0–4 | EU financial sector |
| [CIS Controls v8](#cis-critical-security-controls-v8) | Best Practice | 153 safeguards | 18 Controls | 0–4 | Any sector |
| [BSI IT-Grundschutz](#bsi-it-grundschutz-kompendium) | German standard | 68 Bausteine | 10 Layers | 0–4 | Germany / DACH / IT-Grundschutz cert |
| [CSRM (NCSC CH)](#csrm-swiss-ncsc-2025) | Swiss NCSC | 20 baseline requirements | 5 CSF Functions | Binary | Swiss critical infrastructure |
| [TISAX](#tisaxvida-isa-60) | VDA/ENX | 53 requirements | 12 Domains | 0–4 | Automotive supply chain |
| [Swiss nDSG](#swiss-ndsg-2023) | Swiss law | 25 provisions | 6 Chapters | 0–4 | Organisations processing Swiss personal data |
| [EU Cyber Resilience Act](#eu-cyber-resilience-act-20242847) | EU Regulation | 26 requirements | 6 Groups | 0–4 | EU product manufacturers |
| [EU AI Act](#eu-ai-act-20241689) | EU Regulation | 25 articles | 6 Groups | 0–4 | EU AI system providers/deployers |
| [EU Cloud Sovereignty Framework](#eu-cloud-sovereignty-framework-v121) | EC DG DIGIT | 8 Sovereignty Objectives | 1 Group (SEAL) | SEAL 0–4 | EU institutions / public sector cloud procurement |
| [Custom (YAML)](#custom-frameworks-yaml-import) | User-defined | User-defined | User-defined | User-defined | All |

---

## Maturity Scale (used by 9 of 11 frameworks)

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Non-compliant | Not implemented |
| 1 | Partial | Ad hoc or incomplete |
| 2 | Developing | Documented but inconsistent |
| 3 | Defined | Consistent and managed |
| 4 | Optimised | Measured, improving, embedded |

CSRM uses a different model — see [CSRM section](#csrm-swiss-ncsc-2025).

---

## Assessment Collections

**Assessment Collections** are named groups of assessments that aggregate compliance status across frameworks. Useful for:

- Grouping assessments by year or audit cycle
- Reporting on a specific regulatory perimeter (e.g. "EU regulatory stack 2025")
- Comparing progress across frameworks over time

Each collection shows derived statistics: completion %, compliance %, per-status counts, status rollup (a collection is "compliant" only when all member assessments are compliant).

**Export formats:** CSV (flat), XLSX (colour-coded by status, one sheet per assessment), PDF (A4, per-assessment scores + non-compliant items listed).

---

## Framework Modules

### NIST CSF 2.0

**Source:** NIST Cybersecurity Framework version 2.0 (2024)
**Scope:** 106 subcategories across 6 functions: Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), Recover (RC)
**Scoring:** Tier 1–4 per subcategory (Partial → Adaptive), plus current vs target tier
**Audience:** Any sector and size — widely used as a baseline for maturity assessment globally

**Platform features:**
- Named profiles (create multiple assessments / track over time)
- Radar chart and bar chart report page per profile
- XLSX import from the official NIST CSF 2.0 Excel template
- XLSX and CSV export

**Coverage notes:**
- Full 106-subcategory coverage including GV (Govern) — the function added in CSF 2.0 that is absent from CSF 1.1
- ISO 27001 ↔ NIST CSF 2.0 crosswalk available in the Crosswalk Viewer

---

### NIS2 Directive (EU 2022/2555)

**Source:** Directive (EU) 2022/2555 — Network and Information Security 2
**Scope:** 15 requirements — 10 Article 21(2) technical/organisational security measures + 5 Article 23 incident reporting obligations
**Scoring:** Maturity 0–4
**Audience:** EU essential entities (energy, transport, banking, health, water, digital infrastructure) and important entities; national transposition varies by member state — verify applicability under your jurisdiction's implementing law

**Coverage notes:**
- Article 21(2) measures mapped (a) through (j)
- Article 23 reporting timeline and content obligations
- Does not cover Articles 22–24 (supply chain, registration, disclosure) — self-assessment of technical measures only
- NIS2 crosswalk to ISO 27001 available in the Crosswalk Viewer

---

### DORA (EU 2022/2554)

**Source:** Regulation (EU) 2022/2554 — Digital Operational Resilience Act
**Scope:** 25 articles across 4 chapters: ICT Risk Management (10 articles), ICT Incident Management (6), Digital Operational Resilience Testing (5), ICT Third-Party Risk Management (4)
**Scoring:** Maturity 0–4
**Audience:** EU financial entities (banks, investment firms, insurance, crypto-asset service providers, payment institutions) and their critical ICT third-party providers

**Coverage notes:**
- Covers the core operational resilience obligations of DORA
- Does not replace engagement with your national competent authority (NCA) under DORA
- Level-1 articles covered — does not include all RTS/ITS delegated acts (ongoing regulatory development as of 2025)

---

### CIS Critical Security Controls v8

**Source:** Center for Internet Security, CIS Controls v8 (2021)
**Scope:** 153 safeguards across 18 controls
**Scoring:** Maturity 0–4
**Audience:** Any organisation — particularly strong for SMEs and those without a primary framework. Three implementation groups (IG1/IG2/IG3) support prioritisation.

**Coverage notes:**
- All 153 safeguards assessable regardless of implementation group
- CIS Controls v8 to ISO 27001 crosswalk available in the Crosswalk Viewer

---

### BSI IT-Grundschutz Kompendium

**Source:** Bundesamt für Sicherheit in der Informationstechnik — IT-Grundschutz Kompendium
**Scope:** 68 Bausteine (building blocks) across 10 Schichten (layers): ISMS, ORP (Organisation), CON (Concepts), OPS (Operations), DER (Detection), APP (Applications), SYS (Systems), IND (Industrial), NET (Networks), INF (Infrastructure)
**Scoring:** Maturity 0–4
**Audience:** German public sector (mandatory), organisations pursuing dual ISO 27001 / IT-Grundschutz certification, DACH-region organisations

**Crosswalk:**
- ISO 27001:2022 ↔ BSI IT-Grundschutz: 115 mappings
- ISO 27701:2025 ↔ BSI IT-Grundschutz: 103 mappings
- ISO 27018:2025 ↔ BSI IT-Grundschutz: 51 mappings
- Total: 269 cross-standard mappings — visible in the Crosswalk Viewer

**Coverage notes:**
- Based on publicly available Kompendium structure; exact requirement text from the full BSI Kompendium (bsi.bund.de)
- Coverage focuses on core Bausteine — some sector-specific modules may not be included

---

### CSRM (Swiss NCSC, 2025)

**Source:** Methode CSRM 2025 — Cyber Security Risk Method, published by the Swiss National Cyber Security Centre (NCSC / BACS), 2025
**Scope:** 20 mandatory baseline requirements, 6 Control Objectives for reporting
**Scoring:** Binary — `met` / `partial` / `not_met` / `exception` (not maturity 0–4)
**Audience:** Swiss critical infrastructure operators — energy, transport, water, healthcare, finance, government

> **Important:** CSRM is a fundamentally different model from all other modules. Read this section carefully before using it.

#### How CSRM works

CSRM is **object-centric**. You do not assess a list of requirements globally — you:

1. Define **IT Protection Objects** — aggregated groups of systems, applications, and data that share the same protection requirements (not individual assets)
2. Assess each protection object against 20 baseline requirements drawn from NIST CSF 2.0 functions (GV, ID, PR, DE, RS)
3. Identify **elevated protection objects** (higher criticality) and record additional Technical and Organisational Measures (TOMs)
4. Map results to 6 Control Objectives for structured reporting

The 5-step CSRM methodology is:
1. Define scope and protection objects
2. Categorise protection objects (standard / elevated)
3. Apply 20 baseline requirements per object
4. Define additional TOMs for elevated objects
5. Report via 6 Control Objectives

#### NIST CSF 2.0 alignment

CSRM 2025 is aligned to **NIST CSF 2.0** — specifically, the 20 baseline requirements map to GV (Govern), ID (Identify), PR (Protect), DE (Detect), and RS (Respond). The ISMS CORE implementation uses CSF 2.0 function codes throughout.

> **Note:** The NCSC's own comparison document (*Vergleich-Managementsysteme EN*, 2025) uses CSF **1.1** codes in its cross-reference table — because Switzerland's ICT Minimum Standard is still based on CSF 1.1. The CSRM method itself references CSF 2.0, and ISMS CORE reflects the correct version.

#### BACS self-critique — known limitations

The NCSC's own comparison document is unusually candid about CSRM's limitations. The following gaps are surfaced directly in the Platform UI as disclaimers:

- **IEC 62443 alignment pending** — industrial control systems coverage not yet finalised
- **10 ICT Minimum Standard requirements have no CSRM equivalent** — these are not gaps in the ISMS CORE implementation; they are gaps in CSRM itself (acknowledged in the comparison document, p. 12–13)
- **"No policies" label is misleading** — CSRM does not mandate policies as a document type, but expects governance and organisational measures within its Control Objectives
- **Parallel ISMS implementation = duplication risk** — organisations running both an ISO 27001 ISMS and CSRM should map shared controls to avoid maintaining two parallel control sets

**Source documents (official BACS/NCSC):**
- CSRM 2025 method: https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Methode-CSRM-2025-EN.pdf
- Management system comparison: https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infras/Vergleich-Managementsysteme_EN.pdf

---

### TISAX / VDA ISA 6.0

**Source:** Trusted Information Security Assessment Exchange — VDA Information Security Assessment (ISA) version 6.0
**Scope:** 53 requirements across 12 domains: Information Security, HR, Physical Security, Identity & Access, Cryptography, Communications, Third Parties, Compliance, Prototype/Vehicle Protection, Connected Systems, Development, and Cloud
**Scoring:** Maturity 0–4
**Audience:** Automotive industry suppliers, OEM partners, and subcontractors handling sensitive data (especially prototype and vehicle data) — participation in TISAX certification is a supply chain requirement for most major OEMs (BMW, VW Group, Mercedes, Stellantis, etc.)

**Coverage notes:**
- Based on VDA ISA 6.0 domain structure and assessment criteria
- Full TISAX assessment and label issuance requires engagement with an ENX-accredited auditor
- This module is a self-assessment tool for readiness preparation, not a substitute for official TISAX assessment
- Assessment labels (TISAX, AL1/AL2/AL3) are only issued through ENX-accredited assessment service providers

---

### Swiss nDSG 2023

**Source:** Bundesgesetz über den Datenschutz (nDSG) / Federal Act on Data Protection, Switzerland — entered into force 1 September 2023
**Scope:** 25 key provisions across 6 chapters: Scope & Principles, Data Subject Rights, Controller Obligations, Special Cases, Data Transfers, Enforcement
**Scoring:** Maturity 0–4
**Audience:** Any organisation that processes personal data of Swiss residents or is established in Switzerland

**Coverage notes:**
- The nDSG is Switzerland's counterpart to the EU GDPR (broadly similar scope, different legal basis)
- This module covers the core compliance obligations — legal interpretation should involve Swiss data protection counsel
- Swiss organisations subject to both nDSG and GDPR (e.g. processing EU resident data) should use both this module and the GDPR crosswalk

---

### EU Cyber Resilience Act (2024/2847)

**Source:** Regulation (EU) 2024/2847 — Cyber Resilience Act
**Scope:** 26 essential requirements across 6 groups: Essential Cybersecurity Requirements, Vulnerability Handling, Conformity Assessment, Market Surveillance, Coordinated Disclosure, Incident Reporting
**Scoring:** Maturity 0–4
**Audience:** Manufacturers and importers of products with digital elements (hardware and software) sold in the EU market

**Coverage notes:**
- The CRA is phased: market surveillance provisions apply from mid-2025, vulnerability/incident reporting from late 2025, full application from late 2027
- Essential requirements in Annex I (Part I and Part II) are the primary compliance target — this module covers both
- Conformity assessment route depends on product criticality class (Class I, II, or critical product) — self-declaration vs. third-party assessment
- This module provides a readiness self-assessment; formal conformity assessment involves a notified body for Class II and critical products

---

### EU AI Act (2024/1689)

**Source:** Regulation (EU) 2024/1689 — Artificial Intelligence Act
**Scope:** 25 articles across 6 groups: Risk Management System, Data Governance, Technical Documentation, Transparency & User Information, Human Oversight, Robustness & Accuracy
**Scoring:** Maturity 0–4
**Audience:** Providers and deployers of AI systems in the EU — obligations vary by risk classification (unacceptable risk/prohibited, high-risk, limited-risk, minimal-risk)

**Coverage notes:**
- This module covers Chapter 3 obligations for **high-risk AI systems** — the most substantive compliance tier
- Prohibited AI practices (Article 5) are not an assessment target; they require absolute avoidance
- General-purpose AI model obligations (Title VIII) are not covered in this module version
- The AI Act is phased: prohibited practices apply from February 2025; high-risk obligations in stages through 2026–2027
- Formal conformity assessment for high-risk AI systems involves notified bodies or self-assessment with standardised testing

---

### EU Cloud Sovereignty Framework (v1.2.1)

**Source:** European Commission — DG DIGIT, EU Cloud Sovereignty Framework v1.2.1 (October 2025)
**Scope:** 8 Sovereignty Objectives (SOV-1 to SOV-8) assessed via SEAL-0 to SEAL-4 scale. Weighted Sovereignty Score (weights sum to 100%): SOV-1 Strategic 15% · SOV-2 Legal & Jurisdictional 10% · SOV-3 Data & AI 10% · SOV-4 Operational 15% · SOV-5 Supply Chain 20% · SOV-6 Technology 15% · SOV-7 Security & Compliance 10% · SOV-8 Environmental 5%
**Scoring:** SEAL-0 (No Sovereignty) → SEAL-1 (Jurisdictional) → SEAL-2 (Data) → SEAL-3 (Digital Resilience) → SEAL-4 (Full Digital Sovereignty)
**Audience:** EU institutions, public sector bodies, and regulated entities evaluating cloud service providers under EU procurement and digital sovereignty requirements. Draws on Gaia-X, ENISA/NIS2/DORA, CIGREF Trusted Cloud Referential v2, France Cloud de Confiance, and Germany Souveräner Cloud strategies.

**Coverage notes:**
- The framework defines **minimum assurance levels** per procurement tier — this module supports self-assessment and gap analysis against those levels
- SEAL ratings are qualitative judgements; formal procurement decisions require vendor audit evidence and contractual commitments
- SOV-5 Supply Chain assessment requires visibility into sub-supplier chains — depth of evidence may vary by vendor transparency
- Environmental Sustainability (SOV-8) scoring is indicative; formal green procurement may require certified energy/carbon data

---

### Custom Frameworks (YAML Import)

Upload any custom, sector-specific, or proprietary control framework via YAML. Once imported, the platform maps each control against ISO 27001:2022 via `iso_mappings` fields and shows inferred coverage in the Coverage page.

**YAML format:**
```yaml
name: "My Framework"
short_code: "MY_FW"
version: "1.0"
description: "Optional"
controls:
  - id: "MY.1.1"
    title: "Control title"
    category: "Access Control"
    iso_mappings: ["A.5.15", "A.8.2"]
    tags: ["identity"]
```

**Key fields per control:** `id` (required), `title` (required), `category`, `subcategory`, `priority` (HIGH/MEDIUM/LOW), `iso_mappings` (list of ISO 27001:2022 Annex A refs), `tags`.

**Coverage display:** After import, the Coverage page Mapping Matrix tab shows a custom framework coverage section with percentage, progress bar, and per-control breakdown.

**Admin only:** Import and deletion require admin or super_admin role.

---

## Crosswalk Integration

All compliance assessment modules benefit from the Platform's Crosswalk Viewer, which shows cross-framework mappings between:

- ISO 27001:2022 ↔ NIST CSF 2.0
- ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5
- ISO 27001:2022 ↔ MITRE ATT&CK v18
- ISO 27001:2022 ↔ DORA
- ISO 27001:2022 ↔ NIS2
- ISO 27001:2022 ↔ CIS Controls v8
- ISO 27001:2022 ↔ BSI IT-Grundschutz (115 mappings)
- ISO 27701:2025 ↔ BSI IT-Grundschutz (103 mappings)
- ISO 27018:2025 ↔ BSI IT-Grundschutz (51 mappings)

Total: **2,730+ cross-framework mappings** available in the Crosswalk Viewer.

---

## Limitations and Disclaimers

**All compliance assessment modules:**
- Are self-assessment tools for internal readiness evaluation
- Do not constitute legal advice or regulatory opinions
- Do not replace engagement with competent authorities, notified bodies, or accredited auditors where mandatory assessment applies
- Cover requirements as of the publication date of the relevant regulation/standard — regulatory updates (delegated acts, RTS, ITS, implementing decisions) may introduce new obligations not yet reflected here

**Specific:** CSRM baseline requirements and BACS limitation notes are based on the publicly available NCSC documents from 2025. TISAX labels require ENX-accredited assessment. CIS Controls safeguard text is based on CIS v8 (2021). BSI IT-Grundschutz full requirement text is available from bsi.bund.de.

---

*Part of [ISMS CORE Project](README.md) — ISO 27001 · ISO 27701 · ISO 27018*
