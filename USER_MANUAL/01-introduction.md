# Introduction

<!-- ISMS-CORE:USER-MANUAL:01-introduction:v1.0:2026-04-16 -->

---

## What Is ISMS CORE Platform?

ISMS CORE Platform is a compliance management system for ISO 27001:2022 and its extension standards. It takes the policies, implementation guides, and assessment workbooks produced by the ISMS CORE content factory and turns them into a live, operational system — searchable, scored, evidence-linked, and continuously updated through automated connectors.

The platform does not replace your ISMS. It *is* your ISMS — the operational layer where you manage controls, track gaps, collect evidence, assess compliance against multiple frameworks, and demonstrate audit readiness on any given day.

---

## What the Platform Is Not

**It is not a document generator.** The policies and implementation guides were authored by information security practitioners and are loaded into the platform as content. You read, customise, and track them here — you do not generate them here.

**It is not a ticketing system.** It integrates with Jira and ServiceNow for that purpose.

**It is not a SIEM.** It integrates with your SIEM as an evidence source.

**It is not a one-time audit tool.** It is designed for continuous compliance management — not sprint-and-forget.

---

## The Five Products

The platform hosts five product families, each covering a different ISO standard. You can activate one or all five depending on your organisation's scope.

### ISMS Framework

The core product. Covers all 54 ISO 27001:2022 Annex A control groups with full documentation: policy (POL), implementation guides for users (IMP-UG) and technical teams (IMP-TG), self-assessment scorecard (SCR), and assessment workbook (WKBK). Available in EN, FR, DE, and IT.

### ISMS Operational

A lightweight policy set for smaller organisations or those who need a faster path to ISO 27001 readiness. 53 operational policies (OP-POL) with self-assessment checklists. Uses the same control structure as the Framework but with streamlined documentation.

### Privacy Extension (ISO 27701:2025)

21 control groups covering the ISO 27701:2025 Privacy Information Management System extension. Split into controller, processor, and shared controls. Designed to complement the ISMS Framework — not replace it.

### Cloud Extension (ISO 27018:2025)

12 control groups covering PII protection in public cloud environments under ISO 27018:2025. Relevant for any organisation processing personal data using IaaS, PaaS, or SaaS cloud services.

### AI Extension (ISO 42001:2023 + ISO 42005:2025)

10 control groups covering the AI Management System standard (ISO 42001:2023) with integrated ISO 42005:2025 AI risk assessment content. Covers AI system inventory, risk management, impact assessment, transparency, human oversight, and supplier AI governance.

---

## How the Platform Fits Your ISMS Lifecycle

```
Design            →  Control Library, Projects Workspace
Implement         →  Policies, Implementation Guides, Document Editor
Assess            →  Assessment Checklists, 23 Compliance Frameworks
Monitor           →  Evidence Connectors, KPI Dashboard, Threat Intelligence
Review            →  Gap Management, Risk Register, EBIOS RM
Improve           →  Remediation Tracking, TPRM, BIA
Audit             →  QA Engine, Cross-Framework Mapping, Reports & Exports
```

Every stage of the ISO 27001 Plan-Do-Check-Act cycle has a corresponding platform capability.

---

## How Content Gets Into the Platform

Content is loaded by the platform administrator using the bootstrap script or the Admin import panel. Once loaded, it is available to all users with appropriate permissions. You do not need to upload or configure content yourself — it is pre-structured and ready to use.

When your administrator updates the platform (for example, when new control versions or translations are released), they re-run the import. Existing work — your project documents, gap records, evidence, assessments — is preserved.

---

## Supported Languages

Policy and implementation documents are available in:

- **English (EN)** — all five products
- **French (FR)** — all five products
- **German (DE)** — all five products
- **Italian (IT)** — all five products

The platform interface is in English. Document language is set per-product at import time and displayed as loaded.

---

## Country Localisation

ISMS CORE includes jurisdiction-aware policy rendering. When your organisation's country is configured, regulatory references, data protection authority names, and relevant legislation are automatically substituted into policy documents to reflect your jurisdiction.

Supported jurisdictions: Switzerland (default), Austria, Belgium, France, Germany, Italy, Luxembourg, United Kingdom.

This is configured by your administrator in **Admin → Organisation**.

---

## Next Steps

Start with [Getting Started](02-getting-started.md) to orient yourself in the platform — the dashboard, navigation, and the product switcher.

<!-- QA_VERIFIED: 2026-04-16 -->
