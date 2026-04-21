<p align="center">
  <img src="https://img.shields.io/badge/🎋_ISMS_CORE-Compliance_Assessments-2E8B57?style=for-the-badge" alt="ISMS CORE Compliance Assessments"/>
</p>

<h1 align="center">🎋 ISMS CORE — Compliance Assessment Modules</h1>

<p align="center">
  <strong>Twenty-five built-in frameworks + custom YAML import. One platform. No separate tools required.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Frameworks-25-2E8B57?style=flat-square" alt="25 Frameworks"/>
  <img src="https://img.shields.io/badge/Requirements-700+-0066CC?style=flat-square" alt="700+ Requirements"/>
  <img src="https://img.shields.io/badge/Export-CSV_%7C_XLSX_%7C_PDF-FF6600?style=flat-square" alt="Export"/>
  <img src="https://img.shields.io/badge/Assessment_Collections-Grouping_%26_Reports-2E7D32?style=flat-square" alt="Collections"/>
</p>

---

## Overview

ISMS CORE Platform includes a unified compliance assessment layer covering 25 built-in frameworks across Europe, North America, and globally, plus custom YAML import for any sector-specific or proprietary control framework. Each module provides structured self-assessment, maturity scoring (0–4 where applicable), gap tracking, and export.

Assessment results can be grouped into **Assessment Collections** — named bundles that aggregate status across multiple frameworks for reporting or audit purposes, with CSV, XLSX (colour-coded), and PDF (A4) export.

All compliance assessment modules live under the **Compliance Assessments** sidebar group in the Platform WebUI.

---

## Quick Reference

| Framework | Type | Requirements | Grouping | Scoring | Audience |
|-----------|------|-------------|----------|---------|----------|
| [NIST CSF 2.0](#nist-csf-20) | NIST | 106 subcategories | 6 Functions | Tier 1–4 | Any sector |
| [NIST AI RMF 1.0](#nist-ai-rmf-10-ai-100-1) | NIST | 72 subcategories | 4 Functions (GOV/MAP/MSR/MNG) | 0–4 | AI system providers and operators — any sector |
| [NIS2](#nis2-directive-eu-20222555) | EU Directive | 15 requirements | 2 Articles | 0–4 | EU essential/important entities |
| [DORA](#dora-eu-20222554) | EU Regulation | 25 articles | 4 Chapters | 0–4 | EU financial sector |
| [CIS Controls v8](#cis-critical-security-controls-v8) | Best Practice | 153 safeguards | 18 Controls | 0–4 | Any sector |
| [BSI IT-Grundschutz](#bsi-it-grundschutz-kompendium) | German standard | 68 Bausteine | 10 Layers | 0–4 | Germany / DACH / IT-Grundschutz cert |
| [CSRM (NCSC CH)](#csrm-swiss-ncsc-2025) | Swiss NCSC | 20 baseline requirements | 5 CSF Functions | Binary | Swiss critical infrastructure |
| [Swiss ISG (SR 128)](#swiss-isg-sr-128) | Swiss law | 27 requirements | 8 Sections | 0–4 | Swiss federal bodies & critical infrastructure operators |
| [TISAX](#tisaxvida-isa-60) | VDA/ENX | 53 requirements | 12 Domains | 0–4 | Automotive supply chain |
| [Swiss nDSG](#swiss-ndsg-2023) | Swiss law | 25 provisions | 6 Chapters | 0–4 | Organisations processing Swiss personal data |
| [EU Cyber Resilience Act](#eu-cyber-resilience-act-20242847) | EU Regulation | 26 requirements | 6 Groups | 0–4 | EU product manufacturers |
| [EU AI Act](#eu-ai-act-20241689) | EU Regulation | 25 articles | 6 Groups | 0–4 | EU AI system providers/deployers |
| [EU Cloud Sovereignty Framework](#eu-cloud-sovereignty-framework-v121) | EC DG DIGIT | 8 Sovereignty Objectives | 1 Group (SEAL) | SEAL 0–4 | EU institutions / public sector cloud procurement |
| [CyberFundamentals (BE)](#cyberfundamentals-ccncertbe) | Belgian regulation | 41 practices | 6 CSF Functions | 0–4 | Belgian organisations / CCN/CCB certification |
| [BaFin BAIT (DE)](#bafin-bait-rundschreiben-102021) | German BaFin | 23 requirements | 12 Modules | 0–4 | German financial sector (banks, investment firms) |
| [CSSF Circulaire 20-750 (LU)](#cssf-circulaire-20-750-lu) | Luxembourg CSSF | 19 requirements | 7 Domains | 0–4 | Luxembourg financial sector |
| [ACN Cyber Risk Management (IT)](#acn-cyber-risk-management-it) | Italian ACN | 19 guidelines | 4 Groups | 0–4 | Italian organisations / critical infrastructure |
| [UK NIS Regulations](#uk-nis-regulations-2018) | UK law | 13 requirements | 3 Objectives | 0–4 | UK network and information systems operators |
| [UK Operational Resilience (FCA/PRA)](#uk-operational-resilience-fcapra) | UK FCA/PRA | 12 requirements | 4 Objectives | 0–4 | UK financial sector — banks, insurers, FMIs |
| [COBIT 2019 (ISACA)](#cobit-2019-isaca) | ISACA EGIT | 40 objectives | 5 Domains (EDM/APO/BAI/DSS/MEA) | 0–4 | Enterprise IT governance, audit, CISM/CISA/CGEIT holders |
| [NIST SP 800-53 R5](#nist-sp-800-53-rev-5) | NIST | 20 control families | 3 Classes (Technical/Operational/Management) | 0–4 | US federal agencies, contractors, and any organisation seeking comprehensive security controls |
| [CSA CCM v4.1](#csa-cloud-controls-matrix-v41) | CSA | 197 control specifications | 17 Domains | 0–4 | Cloud service providers, cloud consumers — any sector |
| [CSA AICM v1.0.3](#csa-ai-controls-matrix-v103) | CSA | 72 controls | 7 Domains | 0–4 | Organisations developing, deploying, or procuring AI systems |
| [NCSC CAF v4.0 (UK)](#ncsc-caf-v40-uk) | NCSC UK | 41 Contributing Outcomes | 14 Principles / 4 Objectives | 0/2/4 | UK operators of essential services / CNI |
| [ReCyF v2.5 — France NIS2](#recyf-v25--france-nis2-anssi) | ANSSI | 20 Security Objectives | 4 Pillars | 0–4 | French NIS2 entities (EI & EE) — Loi 2024-449 |
| [Custom (YAML)](#custom-frameworks-yaml-import) | User-defined | User-defined | User-defined | User-defined | All |

---

## Maturity Scale (used by most frameworks)

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

### NIST AI RMF 1.0 (AI 100-1)

**Source:** NIST AI Risk Management Framework 1.0 (NIST AI 100-1), January 2023
**Scope:** 72 subcategory-level practices across 4 core functions — GOVERN (GOV), MAP (MAP), MEASURE (MSR), MANAGE (MNG) — divided into 19 Categories
**Scoring:** Maturity 0–4 per subcategory
**Audience:** AI system providers, developers, deployers, and operators — any sector. Voluntary, jurisdiction-neutral.

**Function structure:**
- **GOVERN (19 subcategories)** — organisational AI risk culture, policies, accountability structures, workforce practices
- **MAP (21 subcategories)** — context and risk framing: intended purposes, categorisation, benefits, costs, societal impacts
- **MEASURE (19 subcategories)** — quantitative, qualitative, and mixed-method tools to analyse, benchmark, and monitor AI risk
- **MANAGE (13 subcategories)** — risk treatment, residual risk, incident response, post-market surveillance

**Platform features:**
- 72 subcategory practices grouped by Category (GOV-1 through MNG-4), maturity 0–4
- EU AI Act ↔ NIST AI RMF 1.0 crosswalk in the Crosswalk Viewer (72 mappings)
- Assessment Collections — group AI RMF assessments alongside EU AI Act assessments

**Coverage notes:**
- Subcategory descriptions sourced from the official NIST AI RMF Playbook (72 suggested actions)
- No ISO 27001 ↔ AI RMF official crosswalk exists — EU AI Act crosswalk is the primary mapping path
- Framework is voluntary — not a regulatory compliance requirement in any jurisdiction
- Related: NIST CSF 2.0 GOVERN function directly mirrors AI RMF GOVERN structure

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

### Swiss ISG (SR 128)

**Source:** Bundesgesetz über die Informationssicherheit beim Bund (ISG) / Federal Act on Information Security (LSI), Switzerland — SR 128, in force 1 January 2024; cyberattack reporting obligation (Art. 74a–74h) in force 1 April 2025
**Scope:** 27 assessable requirements across 8 sections: Information Security Principles (Art. 6–10a), Information Classification (Art. 11–15), ICT Security (Art. 16–19), Personnel & Access (Art. 20–21), Physical Security (Art. 22–23), Personnel Security Checks (Art. 27–30, 43), Cyberattack Reporting Obligation (Art. 74a–74h), ISMS Organisation (Art. 81, 85)
**Scoring:** Maturity 0–4
**Audience:** Swiss federal bodies (mandatory); critical infrastructure operators subject to the cyberattack reporting obligation under Art. 74b (energy, water, finance, transport, health, ICT); private organisations voluntarily aligning with Swiss federal security standards

**Key obligations:**
- **24-hour cyberattack reporting** — mandatory report to BACS/OFCS within 24 hours of detecting a cyberattack that jeopardises operations, involves data manipulation/exfiltration, was undetected for a prolonged period, or involves extortion (Art. 74d–74e)
- **Information classification** — three-level scheme: internal / confidential / secret, with need-to-know access controls (Art. 11–14)
- **ICT security categories** — baseline / elevated / very high, each with corresponding minimum security measures (Art. 17–18)
- **Personnel security checks (PSC)** — base and extended clearance for sensitive functions; periodic repetition (Art. 27–43)
- **ISB/RSSI appointment** — formal information security officer with advisory, directive, and compliance monitoring responsibility (Art. 81)
- **Administrative sanction** — failure to report a cyberattack: up to CHF 100,000 (Art. 74h)

**ISO 27001 crosswalk:** 40 mappings — ISO 27001:2022 controls map directly to ISG requirements; ISO 27001 is the recognised implementation vehicle for ISG compliance in practice.

**Coverage notes:**
- This module is relevant primarily to Swiss federal bodies and operators of critical infrastructure listed in Art. 74b
- Private-sector organisations not subject to Art. 74b are not legally required to comply but may voluntarily adopt the framework as a Swiss security baseline
- The cyberattack reporting obligation (Art. 74a–74h) is the most immediate compliance action for critical infrastructure operators — it entered into force 1 April 2025

> **Note:** This module is a self-assessment tool. Official compliance determination requires review by a qualified Swiss information security practitioner.

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

### CyberFundamentals (CCN/CERT.be)

**Source:** Centre for Cybersecurity Belgium (CCB/CCN) — CyberFundamentals Framework v2025
**Scope:** 41 practices aligned to NIST CSF 2.0 functions: Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), Recover (RC)
**Scoring:** Maturity 0–4
**Audience:** Belgian organisations seeking CCN/CCB CyberFundamentals certification; NIS2-in-scope entities in Belgium; any organisation using NIST CSF 2.0 with Belgian regulatory context

**Coverage notes:**
- CyberFundamentals uses NIST CSF 2.0 control IDs (GV.OC-01, ID.AM-01, etc.) — the ISMS CORE crosswalk leverages existing ISO→NIST CSF mappings
- Three certification levels: Basic, Important, Essential (aligned to Belgian NIS2 transposition)
- Crosswalk: ISO 27001:2022 ↔ CyberFundamentals — 107 mappings

---

### BaFin BAIT (Rundschreiben 10/2021)

**Source:** Bundesanstalt für Finanzdienstleistungsaufsicht — Bankaufsichtliche Anforderungen an die IT (BAIT), Rundschreiben 10/2021
**Scope:** 23 requirements across 12 modules: IT Strategy, IT Governance, Information Risk Management, Information Security, IT Projects, Application Development, IT Operations, IT Outsourcing, IT Emergency Management, IAM, Cryptography, BCM
**Scoring:** Maturity 0–4
**Audience:** German banks and financial institutions supervised by BaFin; applies in conjunction with MaRisk and DORA for EU-regulated entities

**Coverage notes:**
- BAIT is the primary IT supervisory circular for German-supervised banks; VAIT (insurance) and KAIT (capital management) share the same structure
- Replaces the 2017 BAIT circular; includes MaRisk alignment and cloud-specific guidance
- Crosswalk: ISO 27001:2022 ↔ BaFin BAIT — 69 mappings

---

### CSSF Circulaire 20-750 (LU)

**Source:** Commission de Surveillance du Secteur Financier (CSSF), Luxembourg — Circulaire CSSF 20/750
**Scope:** 19 requirements across 7 ICT risk domains: Governance, Risk Management, ICT Security, Business Continuity, Third-Party Management, Incident Management, Audit
**Scoring:** Maturity 0–4
**Audience:** Luxembourg financial sector entities regulated by CSSF — banks, investment firms, payment institutions, fund administrators

**Coverage notes:**
- CSSF 20/750 is the primary ICT risk management circular for CSSF-regulated entities, aligned to EBA/ESMA guidelines
- Entities subject to DORA (from January 2025) should use both this module and the DORA module
- Crosswalk: ISO 27001:2022 ↔ CSSF 20/750 — 47 mappings

---

### ACN Cyber Risk Management (IT)

**Source:** Agenzia per la Cybersicurezza Nazionale (ACN) — Linee Guida per la Gestione del Rischio Cyber, 2024
**Scope:** 19 guidelines across 4 groups: Governance & Risk, Asset Management, Technical Controls, Incident & BCM
**Scoring:** Maturity 0–4
**Audience:** Italian organisations — public administration, critical infrastructure operators, NIS2-in-scope entities in Italy

**Coverage notes:**
- ACN is the Italian National Cybersecurity Agency; these guidelines align with NIS2 Italian transposition (D.Lgs. 138/2024)
- Organisations subject to both ACN guidelines and NIS2 can use both modules
- Crosswalk: ISO 27001:2022 ↔ ACN Guidelines — 43 mappings

---

### UK NIS Regulations 2018

**Source:** The Network and Information Systems (NIS) Regulations 2018 (SI 2018/506) — UK implementation of EU NIS Directive
**Scope:** 13 requirements across 3 objectives: Governance, Risk Management & Security, Operational Capability
**Scoring:** Maturity 0–4
**Audience:** UK operators of essential services (OES) in energy, transport, health, water, digital infrastructure; relevant digital service providers (RDSPs)

**Coverage notes:**
- UK NIS Regulations remain in force post-Brexit as domestic law; the Cyber Security and Resilience Bill (2025, pending Royal Assent) will update and expand scope
- NCSC's Cyber Assessment Framework (CAF) is the recommended tool for OES compliance — this module covers the core NIS obligations
- Crosswalk: ISO 27001:2022 ↔ UK NIS Regulations — 51 mappings

---

### UK Operational Resilience (FCA/PRA)

**Source:** FCA Policy Statement PS21/3 + PS26/2; PRA Supervisory Statement SS1/21; Bank of England operational resilience policy
**Scope:** 12 requirements across 4 objectives: Important Business Services, Impact Tolerances, Scenario Testing, Self-Assessment
**Scoring:** Maturity 0–4
**Audience:** UK financial sector — banks, building societies, PRA-designated investment firms, insurers, financial market infrastructures (FMIs), payment systems operators

**Coverage notes:**
- UK Op. Resilience requirements came into full effect March 2025 (PS21/3 deadline); PS26/2 extended scope to more entities
- Entities subject to both UK Op. Resilience and DORA should use both modules
- Focus is on important business services (IBS) and impact tolerances — not a substitute for formal FCA/PRA supervisory engagement
- Crosswalk: ISO 27001:2022 ↔ UK Operational Resilience — 34 mappings

---

### COBIT 2019 (ISACA)

**Source:** ISACA — COBIT 2019 Framework: Governance and Management Objectives (November 2018)
**Scope:** 40 governance and management objectives across 5 domains: EDM (Evaluate, Direct and Monitor), APO (Align, Plan and Organise), BAI (Build, Acquire and Implement), DSS (Deliver, Service and Support), MEA (Monitor, Evaluate and Assess)
**Scoring:** Capability levels 0–4 (Incomplete → Performed → Managed → Established → Optimizing)
**Audience:** Enterprise IT governance programmes, internal audit functions, IT strategy and board-level oversight. Particularly relevant for CISM, CISA, and CGEIT certification holders.

**Coverage notes:**
- EDM objectives (EDM01–EDM05) are governance-level — intended for board/executive oversight; APO, BAI, DSS, MEA are management-level
- APO13 (Managed Security) and DSS05 (Managed Security Services) map directly to ISO 27001:2022 Annex A information security controls
- COBIT 2019 aligns to ISO/IEC 27001, ISO/IEC 38500, ITIL, NIST CSF, and PMBOK/PRINCE2
- Full COBIT capability scale runs 0–5 (level 5: Optimizing with quantitative management); the platform uses a 0–4 scale consistent with all other assessment modules
- Replaces COBIT 5 (2012); key changes include design factors, focus areas, and alignment with NIST CSF 2.0 concepts

---

### NIST SP 800-53 Rev. 5

**Source:** NIST Special Publication 800-53 Revision 5 — Security and Privacy Controls for Information Systems and Organizations (September 2020)
**Scope:** 20 control families covering the full security and privacy control catalogue for federal information systems. Families include Access Control (AC), Audit and Accountability (AU), Configuration Management (CM), Identification and Authentication (IA), Incident Response (IR), System and Communications Protection (SC), and more.
**Scoring:** Maturity levels 0–4 (Not Implemented → Initial → Managed → Defined → Optimizing)
**Audience:** US federal agencies and contractors required under FISMA; organisations seeking FedRAMP authorization; any sector wanting a comprehensive, baseline-driven control framework. Cross-referenced against ISO 27001:2022 Annex A.

**Coverage notes:**
- Control families map directly to ISO 27001:2022 Annex A domains — 474+ individual controls condensed to 20 scored families on the platform
- NIST SP 800-53 Rev. 5 integrates privacy controls (previously separate in 800-53A) for the first time
- ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5 crosswalk available in the Crosswalk Viewer
- Baseline tailoring (Low/Moderate/High) is not automated — the platform scores all 20 families uniformly

---

### CSA Cloud Controls Matrix v4.1

**Source:** Cloud Security Alliance — Cloud Controls Matrix v4.1 (March 2023)
**Scope:** 197 control specifications across 17 security domains: Application & Interface Security (AIS), Audit Assurance & Compliance (AAC), Business Continuity Management & Operational Resilience (BCR), Change Control & Configuration Management (CCC), Cryptography, Encryption & Key Management (CEK), Data Center Security (DCS), Data Security & Privacy Lifecycle Management (DSP), Governance, Risk & Compliance (GRC), Human Resources (HRS), Identity & Access Management (IAM), Infrastructure & Virtualization Security (IVS), Interoperability & Portability (IPY), Logging & Monitoring (LOG), Security Incident Management, E-Discovery, & Cloud Forensics (SEF), Supply Chain Management, Transparency & Accountability (STA), Threat & Vulnerability Management (TVM), Universal Endpoint Management (UEM).
**Scoring:** Maturity levels 0–4
**Audience:** Cloud service providers seeking CSA STAR certification; cloud consumers performing vendor due diligence; organisations with multi-cloud or hybrid environments.

**Coverage notes:**
- CCM v4.1 is the definitive cloud security control framework — aligned to ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, NIST SP 800-53, CIS Controls v8, and GDPR
- CSA STAR (Security, Trust, Assurance, and Risk) Level 1 uses CCM self-assessment; Level 2 uses third-party audit
- ISO 27018:2025 (Cloud product) and CCM v4.1 are complementary — CCM is broader; ISO 27018 focuses specifically on PII protection

---

### CSA AI Controls Matrix v1.0.3

**Source:** Cloud Security Alliance — AI Controls Matrix (AICM) v1.0.3 (2024)
**Scope:** 72 controls across 7 domains: AI Governance & Accountability (AGA), Data Management & Privacy (DMP), Model Development & Validation (MDV), Security & Resilience (SAR), Transparency & Explainability (TEX), Human Oversight & Control (HOC), Regulatory Compliance & Legal (RCL).
**Scoring:** Maturity levels 0–4
**Audience:** Organisations developing, deploying, or procuring AI systems; AI governance teams; cloud providers offering AI/ML services; teams managing EU AI Act or ISO 42001 compliance.

**Coverage notes:**
- AICM is designed as a companion to CCM v4.1 — focuses exclusively on AI system security and governance
- Aligned to EU AI Act, ISO/IEC 42001:2023, NIST AI RMF 1.0, and OECD AI Principles
- ISO 42001 (AI product) and AICM are complementary — ISO 42001 is a management system standard; AICM provides detailed technical controls
- Particularly useful alongside the platform's ISO 42001 crosswalk mappings (NIST AI RMF: 32, EU AI Act: 31, OECD AI: 14)

---

### NCSC CAF v4.0 (UK)

**Source:** UK National Cyber Security Centre — Cyber Assessment Framework v4.0 (2024)
**Scope:** 41 Contributing Outcomes across 14 Principles and 4 Objectives (A: Managing Security Risk, B: Protecting Against Cyber Attack, C: Detecting Cyber Security Events, D: Minimising the Impact of Incidents).
**Scoring:** 3-column model for most outcomes: Not Achieved (0) / Partially Achieved (2) / Achieved (4). Nine outcomes use 2-column model (Not Achieved / Achieved only).
**Audience:** UK Operators of Essential Services (energy, transport, health, water, digital infrastructure), Relevant Digital Service Providers, public sector bodies subject to the UK NIS Regulations 2018.

**Coverage notes:**
- CAF v4.0 (2024) introduced Objective D (Minimising the Impact) and restructured several outcomes from v3.1 — platform implements v4.0 only
- 65 ISO 27001:2022 crosswalk mappings available in the Crosswalk Viewer (ISO27001_2022 → NCSC_CAF axis)
- Organisations subject to both NIS Regulations and CAF should maintain both modules — NIS provides the legal baseline, CAF provides the technical assessment methodology

---

### ReCyF v2.5 — France NIS2 (ANSSI)

**Source:** ANSSI — Agence nationale de la sécurité des systèmes d'information. Référentiel de Cybersécurité France v2.5 (17/03/2026).
**Scope:** 20 Security Objectives (OS-01 to OS-20) structured across 4 pillars: Gouvernance, Protection, Défense, Résilience. 152 requirements (Moyens acceptables de conformité). OS-01–15 apply to both Entités Importantes (EI) and Entités Essentielles (EE). OS-16–20 apply to EE only.
**Scoring:** Maturity levels 0–4
**Audience:** French organisations subject to the NIS2 transposition: Entités Importantes (EI) and Entités Essentielles (EE) as classified under Loi n° 2024-449 (PJL Art. 14 / NIS2 transposition). Covers all NIS2 sectors: énergie, transport, santé, eau, infrastructures numériques, services numériques, administrations publiques.

**Coverage notes:**
- Document de travail ANSSI version 2.5 (17/03/2026) — subject to revision before final adoption
- 50 ISO 27001:2022 crosswalk mappings available in the Crosswalk Viewer (ISO27001_2022 → FR_NIS2_RECYF axis)
- EE-only objectives (OS-16 to OS-20) are included in the assessment and clearly labelled; EI-only organisations may use them as an aspirational target
- Assessment interface uses official ANSSI French terminology throughout

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
- NIST AI RMF 1.0 ↔ EU AI Act (72 mappings)
- ISO 27001:2022 ↔ NIST SP 800-53 Rev. 5
- ISO 27001:2022 ↔ MITRE ATT&CK v18
- ISO 27001:2022 ↔ DORA
- ISO 27001:2022 ↔ NIS2
- ISO 27001:2022 ↔ CIS Controls v8
- ISO 27001:2022 ↔ BSI IT-Grundschutz (115 mappings)
- ISO 27701:2025 ↔ BSI IT-Grundschutz (103 mappings)
- ISO 27018:2025 ↔ BSI IT-Grundschutz (51 mappings)
- ISO 27001:2022 ↔ CyberFundamentals BE (107 mappings)
- ISO 27001:2022 ↔ BaFin BAIT DE (69 mappings)
- ISO 27001:2022 ↔ CSSF 20-750 LU (47 mappings)
- ISO 27001:2022 ↔ ACN Guidelines IT (43 mappings)
- ISO 27001:2022 ↔ UK NIS Regulations (51 mappings)
- ISO 27001:2022 ↔ UK Operational Resilience (34 mappings)
- ISO 27001:2022 ↔ NCSC CAF v4.0 (65 mappings)
- ISO 27001:2022 ↔ ReCyF v2.5 / FR NIS2 (50 mappings)

Total: **3,315 crosswalk objects across 41 axes** available in the Crosswalk Viewer.

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
