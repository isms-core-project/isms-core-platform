# Assessment Frameworks

<!-- ISMS-CORE:USER-MANUAL:07-assessment-frameworks:v1.0:2026-04-16 -->

---

## Overview

The platform includes 29 compliance framework assessment modules. These cover regulatory obligations, industry standards, and sector-specific requirements that organisations running an ISO 27001 ISMS commonly need to demonstrate compliance with alongside their ISO certification.

Framework assessments are global — they are not scoped to a specific project but cover your organisation's overall compliance posture.

Navigate to any framework from the **Compliance** section of the sidebar or from the **Global** group at the bottom of the sidebar.

---

## Available Frameworks

### Regulatory — European Union

| Framework | Module | Scope |
|-----------|--------|-------|
| **NIS2 Directive** | EU 2022/2555 | 10 Art. 21 security measures + 5 Art. 23 reporting obligations. Applies to essential and important entities in the EU. Maturity 0–4. |
| **DORA** | EU 2022/2554 | 25 articles across 4 chapters: ICT Risk Management, Incident Management, Resilience Testing, Third-Party ICT Risk. Applies to financial sector entities. Maturity 0–4. |
| **EU Cyber Resilience Act (CRA)** | EU 2024/2847 | 26 essential cybersecurity requirements across 6 groups. Applies to manufacturers of products with digital elements. Maturity 0–4. |
| **EU AI Act** | EU 2024/1689 | 25 articles across 6 groups: Risk Management, Data Governance, Transparency, Human Oversight, Robustness, Accountability. Applies to providers of high-risk AI systems. Maturity 0–4. |
| **EU Cloud Sovereignty** | Cloud sovereignty framework | 8 requirements for cloud service providers and users. |

### Regulatory — Switzerland

| Framework | Module | Scope |
|-----------|--------|-------|
| **Swiss ISG (SR 128)** | Federal Act on Information Security 2024 | 27 requirements across 8 sections. Mandatory for federal bodies; de facto standard for critical infrastructure. Includes 24h cyberattack reporting to BACS/OFCS (Art. 74e). ISO 27001 crosswalk: 40 mappings. Maturity 0–4. |
| **Swiss nDSG** | Federal Act on Data Protection 2023 | 25 provisions across 6 chapters. Switzerland's revised data protection law, equivalent to GDPR for Swiss-domiciled organisations. Maturity 0–4. |
| **FINMA** | FINMA circulars (08/21, 23/1, 2023) | 19 requirements for Swiss financial institutions. Covers operational risk, outsourcing, ICT security. |
| **CSRM (NCSC CH)** | BACS Cybersecurity Reference Model | Object-centric, binary assessment: IT Protection Objects, 20 NIST CSF 2.0 baseline requirements, 6 Control Objectives. Includes BACS limitation notes from official comparison documents. |

### Regulatory — Country-Specific

| Framework | Module | Scope |
|-----------|--------|-------|
| **CyberFundamentals (BE)** | CCN/CCB Belgium | 41 NIST CSF 2.0-aligned practices. Belgian Cyber Security Centre baseline. ISO 27001 crosswalk: 107 mappings. |
| **BaFin BAIT (DE)** | Rundschreiben 10/2021 | 23 requirements across 12 modules. German banking IT supervisory requirements. ISO 27001 crosswalk: 69 mappings. |
| **CSSF 20-750 (LU)** | CSSF Circulaire 20/750 | 19 requirements across 7 domains. Luxembourg financial sector ICT risk. ISO 27001 crosswalk: 47 mappings. |
| **ACN Guidelines (IT)** | ACN Linee Guida Cyber Risk | 19 guidelines across 4 groups. Italian National Cybersecurity Agency baseline. ISO 27001 crosswalk: 43 mappings. |
| **UK NIS** | UK NIS Regulations 2018 (SI 2018/506) | 13 requirements across 3 objectives. Post-Brexit equivalent of EU NIS. ISO 27001 crosswalk: 51 mappings. |
| **UK Operational Resilience** | FCA/PRA PS21/3 + PS26/2 | 12 requirements across 4 objectives. UK financial sector operational resilience. ISO 27001 crosswalk: 34 mappings. |

### International Standards

| Framework | Module | Scope |
|-----------|--------|-------|
| **NIST CSF 2.0** | NIST Cybersecurity Framework 2.0 | 106 subcategories across 6 Functions (GV, ID, PR, DE, RS, RC). Tiered profiles (1–4), radar + bar chart report, XLSX import from official NIST template, XLSX/CSV export. |
| **NIST AI RMF 1.0** | NIST AI 100-1 | 72 subcategories across 4 Functions (GOVERN, MAP, MEASURE, MANAGE). Maturity 0–4. ISO 42001 crosswalk: 32 mappings. EU AI Act crosswalk: 72 mappings. |
| **NIST SP 800-53 Rev 5** | NIST SP 800-53r5 | 324 base controls across 20 families. Assessed at base-control level. Maturity 0–4. |
| **CIS Controls v8** | CIS Critical Security Controls v8 | 153 safeguards across 18 controls. Industry standard baseline for technical security hygiene. Maturity 0–4. |
| **CSA CCM v4.1** | Cloud Security Alliance CCM | 207 controls across 17 domains. Cloud-specific security controls for cloud service providers and customers. |
| **CSA AICM v1.0.3** | Cloud Security Alliance AI Controls Matrix | 243 controls across 18 domains. AI-specific security controls overlay. |
| **COBIT 2019** | ISACA COBIT 2019 | 40 governance and management objectives. IT governance capability scoring (0–4). |
| **TISAX** | VDA ISA 6.0 | 53 requirements across 12 domains: Information Security, Physical Security, Prototype Protection, and more. Automotive industry standard (VDA/ENX). Maturity 0–4. |
| **BSI IT-Grundschutz** | BSI Kompendium | 68 Bausteine across 10 layers. German Federal Office for Information Security baseline. ISO 27001 + ISO 27701 + ISO 27018 crosswalk: 269 total mappings. |
| **BSI C5:2026** | BSI Cloud Computing Compliance Criteria Catalogue 2026 | 130+ criteria across 17 domains. German Federal Office for Information Security cloud security standard, 2026 edition. Successor to BSI C5:2020. |
| **BSI C3A** | BSI Cybersecurity and Cloud Criteria for AI 2025 | AI-specific cloud security criteria overlaying BSI C5. For cloud-based AI deployments. |
| **PCI DSS v4.0.1** | PCI SSC Payment Card Industry Data Security Standard | 12 requirements across 323 sub-requirements with 6 prioritised milestones. Applies to organisations that handle cardholder data. Maturity 0–4. |

---

## Using a Framework Assessment

The experience is consistent across all 29 frameworks.

### Opening an Assessment

Navigate to the framework page from the sidebar. The page shows:

- Framework metadata (standard number, version, issuing body)
- Overall compliance score and completion percentage
- Assessment items grouped by chapter/domain/function

### Scoring Items

Each item has a maturity scale:

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Not implemented | No measure in place |
| 1 | Initial | Ad hoc, not systematically implemented |
| 2 | Managed | Implemented but not formally managed |
| 3 | Defined | Formally documented and implemented |
| 4 | Optimising | Continuously monitored and improved |

For binary frameworks (CSRM), items are: Met / Partial / Not Met / Exception.

Set the score, add a comment, and optionally link to evidence items. Changes are auto-saved.

### NIST CSF 2.0 — Special Features

The NIST CSF 2.0 module has additional capabilities:

- **Tiered profile assessment** — rate each of the 106 subcategories at tier 1–4
- **Radar chart report** — per-function scoring shown visually
- **XLSX import** — import scores from the official NIST CSF 2.0 Excel template
- **XLSX/CSV export** — export your scores in spreadsheet format

### BSI IT-Grundschutz — Special Features

The BSI module maps to three ISO standards simultaneously. The crosswalk viewer shows which Bausteine map to which ISO 27001, ISO 27701, and ISO 27018 controls — useful for organisations running a combined ISO + BSI programme.

---

## Assessment Collections

Group framework assessments into named collections for reporting. A collection can contain assessments from multiple frameworks — for example, combining your NIS2, DORA, and ISO 27001 assessments into a single "Regulatory Compliance Package" report.

See [Compliance Assessments → Assessment Collections](06-compliance-assessments.md#assessment-collections) for how to create and export collections.

---

## Cross-Framework Inferred Coverage

When you complete your ISO 27001 framework assessment, the platform automatically infers coverage for NIS2, DORA, and GDPR using the built-in crosswalk mappings. This means you do not need to manually duplicate your ISO 27001 assessment work to get an initial NIS2 or DORA score.

See [Cross-Framework Mapping](15-cross-framework-mapping.md) for detail.

<!-- QA_VERIFIED: 2026-04-16 -->
