# Cross-Framework Mapping

<!-- ISMS-CORE:USER-MANUAL:15-cross-framework-mapping:v1.3:2026-10-17 -->

---

## Overview

Most organisations subject to ISO 27001 also have obligations under other frameworks — NIS2, DORA, GDPR, a national standard, or an industry baseline. Managing these as separate silos is expensive and creates inconsistency. Cross-framework mapping lets you use your ISO 27001 compliance work to automatically populate an initial score for other frameworks.

Navigate to **ISMS → Coverage** (the Mapping Matrix and Inferred Coverage tabs) in the sidebar.

---

## What Cross-Framework Mapping Does

The platform ships **5,249 curated crosswalk mappings on 85 framework-pair axes** (4,632 on 60 axes in the core crosswalk, plus the ISO 42001 / ISO 42005 and EU-country mapping files); **3,277** of them are anchored on ISO 27001:2022 controls, the rest connect other pairs such as NIST AI RMF ↔ ISO 42001 or ISO 27701 ↔ GDPR. When you complete your ISO 27001 assessment, the platform uses these mappings to infer coverage for the related frameworks.

This means:

- Your ISO 27001 A.8.8 (vulnerability management) score flows through to the NIS2 vulnerability handling article
- Your A.5.31 (legal requirements) score flows through to GDPR Article 32
- Your A.5.15 (access control) score maps to multiple NIST CSF 2.0 subcategories

You still need to review and adjust the inferred scores — but you start from a populated baseline rather than a blank slate.

---

## The Coverage Matrix

The Coverage Matrix tab shows a grid of ISO 27001 control groups on one axis and external frameworks on the other. Each cell shows:

- Whether a mapping exists for that combination
- Your ISO compliance score for that control
- The inferred coverage score for the external framework control

Green cells have mappings and good ISO scores. Amber cells have mappings but gaps in ISO coverage — addressing those ISO gaps will also improve your regulatory posture.

---

## The Crosswalk Viewer

The Crosswalk Viewer tab lets you browse individual mappings:

1. Select a **source framework** (e.g. ISO 27001:2022)
2. Select a **target framework** (e.g. NIS2)
3. Browse the mapping table showing which source controls map to which target controls

Each mapping shows:
- Source control ID and name
- Target control ID and name
- Mapping confidence (High / Medium — based on domain alignment and editorial review)
- Mapping direction (unidirectional or bidirectional)

---

## Inferred Coverage

The **Inferred Coverage** tab shows the output of the BFS (breadth-first search) inference engine. For NIS2, DORA, and GDPR, the platform automatically calculates what your ISO 27001 coverage implies about your regulatory compliance:

- Select **ISO 27001 → NIS2** to see which NIS2 articles are well-covered by your ISO controls and which have residual gaps
- Select **ISO 27001 → DORA** for the same for DORA
- Select **ISO 27001 → GDPR** for GDPR

This view is a starting point, not a compliance certificate. Inferred scores need human review — a control mapped between frameworks does not mean the implementation is identical.

---

## Mapping Coverage by Framework

| Target framework | Mappings from ISO 27001 | Notes |
|-----------------|---------|-----------|
| NIST SP 800-53 Rev 5 | 443 | |
| BSI IT-Grundschutz | 386 | plus 101 from ISO 27701 and 51 from ISO 27018 (538 in total) |
| CSA AICM v1.1 | 352 | |
| CIS Controls v8 | 295 | |
| NIST CSF 2.0 | 244 | |
| CSA CCM v4.1 | 207 | |
| BSI C5:2026 | 168 | |
| CyberFundamentals BE | 107 | |
| FINMA | 73 | |
| BaFin BAIT | 69 | |
| TISAX | 65 | |
| GDPR | 57 | ISO 27701 → GDPR has 100 more |
| NIS2 | 54 | |
| UK NIS | 51 | |
| DORA | 50 | |
| CSSF 20-750 | 47 | |
| COBIT 2019 | 45 | |
| MITRE ATT&CK v20 / v19 | 45 / 36 | v19 kept alongside v20 |
| ACN (IT) | 43 | |
| Swiss nDSG | 41 | |
| NCSC CAF v4.0 | 41 | |
| PCI DSS v4.0.1 | 39 | |
| UK Operational Resilience | 34 | |
| OWASP Top 10 / ASVS 5.0 | 31 / 22 | |
| EU AI Act | 30 | |
| NIST AI RMF | 28 | |
| Swiss ISG | 27 | |
| BSI C3A | 26 | |
| ISO 42001 | 26 | |
| EU Cyber Resilience Act | 26 | |
| ReCyF (FR NIS2) | 20 | |
| ISO 42001 → NIST AI RMF / EU AI Act / GDPR / Swiss nDSG / OECD AI / ISO 42005 | 32 / 13 / 19 / 21 / 14 / 5 | AI-anchored axes |
| EU country frameworks (CyberFundamentals, BAIT, CSSF, ACN, UK NIS, UK Operational Resilience) | 351 | already counted in the rows above |


---

## Using Mapping Results for Audit Evidence

When demonstrating multi-framework compliance to an auditor:

1. Run the Inferred Coverage report for the relevant framework
2. Export the Crosswalk Viewer for the specific mapping axis
3. Provide the export alongside your ISO 27001 assessment evidence

The crosswalk export shows exactly which ISO controls map to which regulatory requirements and at what confidence level — making it straightforward to argue multi-framework coverage from a single control programme.

---

## Custom Frameworks

If you have an internal framework, sector-specific standard, or a framework not yet in the platform, you can upload it as a **Custom Framework** using a YAML template.

Navigate to **Admin → Custom Frameworks**. Download the YAML template, fill in your framework controls and any ISO 27001 mappings, and upload. The custom framework is then available in the Coverage Matrix and as an assessment module.

---

## Content Coverage Gaps

The **Content Coverage Gaps** section is available on the Coverage page for the **ISMS product only**. It shows which ISO 27001 Annex A control groups are missing artefacts — policies, implementation guides (UG/TG), or assessment checklists.

Two views are available via the FW / OP toggle:

| View | Checks for |
|------|-----------|
| **FW (Framework)** | Policy + UG + TG + assessment checklist |
| **OP (Operational)** | Policy + assessment checklist |

If all control groups have complete artefacts, a green banner confirms full coverage. Otherwise, the gap table lists each control group with the artefact types missing.

This section is not available for Privacy, Cloud, or AI products — those products have their own artefact structures managed separately.

<!-- QA_VERIFIED: 2026-10-17 -->
