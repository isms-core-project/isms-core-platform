# Cross-Framework Mapping

<!-- ISMS-CORE:USER-MANUAL:15-cross-framework-mapping:v1.0:2026-04-16 -->

---

## Overview

Most organisations subject to ISO 27001 also have obligations under other frameworks — NIS2, DORA, GDPR, a national standard, or an industry baseline. Managing these as separate silos is expensive and creates inconsistency. Cross-framework mapping lets you use your ISO 27001 compliance work to automatically populate an initial score for other frameworks.

Navigate to **Analytics → Cross-Framework Mapping** in the sidebar.

---

## What Cross-Framework Mapping Does

The platform contains 3,915 pre-built, curated crosswalk mappings between ISO 27001:2022 controls and other frameworks. When you complete your ISO 27001 assessment, those scores are automatically inferred into the mapped frameworks.

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

| Target framework | Mappings | Key source |
|-----------------|---------|-----------|
| NIST CSF 2.0 | ~350 | ISO 27001 → NIST (bidirectional) |
| MITRE ATT&CK v19 | ~220 | ISO 27001 → ATT&CK techniques |
| NIS2 | ~90 | ISO 27001 → NIS2 Article 21 |
| DORA | ~80 | ISO 27001 → DORA chapters |
| GDPR | ~60 | ISO 27001 → GDPR articles |
| BSI IT-Grundschutz | 269 | ISO 27001/27701/27018 → BSI Bausteine |
| CyberFundamentals BE | 107 | ISO 27001 → CCB practices |
| BaFin BAIT | 69 | ISO 27001 → BAIT modules |
| CIS Controls v8 | ~90 | ISO 27001 → CIS safeguards |
| OWASP ASVS | ~60 | ISO 27001 → ASVS requirements |
| ISO 42001 → NIST AI RMF | 32 | ISO 42001 → NIST AI RMF |
| ISO 42001 → EU AI Act | 31 | ISO 42001 → AI Act articles |
| ISO 42001 → EU GDPR | 19 | ISO 42001 → GDPR articles (Art. 5/24/25/28/30/35/36/44) |
| ISO 42001 → CH nDSG | 21 | ISO 42001 → Swiss nDSG provisions |
| ISO 42001 → OECD AI | 14 | ISO 42001 → OECD AI Principles |
| ISO 42001 → ISO 42005 | 5 | ISO 42001 → ISO 42005 |
| EU country frameworks | 351 | ISO 27001 → AT/BE/DE/FR/IT/LU/GB |

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

Navigate to **Tools → Custom Frameworks**. Download the YAML template, fill in your framework controls and any ISO 27001 mappings, and upload. The custom framework is then available in the Coverage Matrix and as an assessment module.

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

<!-- QA_VERIFIED: 2026-04-16 -->
