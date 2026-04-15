# ISMS CORE AI Extension Pack

**Status:** v1.0 Complete (2026-04-15)
**Standards:** ISO/IEC 42001:2023 — Artificial Intelligence Management System (AIMS)
**Prerequisite:** ISMS CORE Framework must be installed

---

## Scope

12 AI control groups across 2 foundation policies and 10 Annex A control families:

| Family | Folder | Groups | ISO 42001:2023 Annex |
|--------|--------|--------|----------------------|
| Foundation | `00-ai-foundation-policies/` | 2 | AI-POL-00, AI-POL-01 |
| AI Governance | `ai-a.2.2-4-ai-policy-framework/` | 1 | A.2 |
| AI Roles | `ai-a.3.2-3-ai-roles-and-responsibilities/` | 1 | A.3 |
| AI Resources | `ai-a.4.2-6-ai-system-resources/` | 1 | A.4 |
| AI Impact | `ai-a.5.2-5-ai-system-impact-assessment/` | 1 | A.5 |
| AI Development Governance | `ai-a.6.1-ai-development-governance/` | 1 | A.6 |
| AI Development Lifecycle | `ai-a.6.2-ai-development-lifecycle/` | 1 | A.6 |
| AI System Operations | `ai-a.7.2-6-ai-system-operations/` | 1 | A.7 |
| AI Information for Interested Parties | `ai-a.8.2-5-information-for-interested-parties/` | 1 | A.8 |
| AI Responsible Use | `ai-a.9.2-4-responsible-use-of-ai-systems/` | 1 | A.9 |
| AI Third-Party & Customer Relationships | `ai-a.10.2-4-third-party-and-customer-relationships/` | 1 | A.10 |

## ISO/IEC 42001:2023

ISO/IEC 42001:2023 specifies requirements for establishing, implementing, maintaining, and continually improving an Artificial Intelligence Management System (AIMS) within the context of an organisation. It provides:

- AI governance and decision-making structure
- AI policy framework and regulatory applicability
- Roles and responsibilities for AI development and deployment
- AI system impact assessment (AISIA) methodology
- Development and deployment lifecycle controls
- Operational controls for AI systems in production
- Responsible use requirements for AI deployers
- Third-party AI supplier and customer relationship governance
- Transparency and information obligations to interested parties

## Relationship to ISMS CORE Framework (ISO 27001:2022)

| Product | Target | Standard |
|---------|--------|----------|
| **AI** (this product) | Organisations developing or deploying AI systems | ISO/IEC 42001:2023 |
| **FRAMEWORK** (`isms-core-framework/`) | All organisations requiring an ISMS | ISO/IEC 27001:2022 |

ISO/IEC 42001:2023 extends ISO 27001:2022 — an AIMS **requires** an ISMS as its foundation. AI security controls (data poisoning, adversarial robustness, model confidentiality) are handled by the ISMS Framework; the AI pack covers AI-specific governance, impact assessment, and responsible use obligations.

## Relationship to Other Extension Packs

| Product | Standard | Overlap |
|---------|----------|---------|
| **PRIVACY** (`isms-core-privacy/`) | ISO 27701:2025 | AISIA outputs feed into DPIA processes; AI systems processing PII require both |
| **CLOUD** (`isms-core-cloud/`) | ISO 27018:2025 | AI systems deployed as cloud services must also satisfy cloud PII controls |

## Document Types

Each AI control group contains:
- **AI-POL** — AIMS policy (WHAT + WHO + WITH WHAT)
- Languages: EN + FR + DE + IT

Checklist generators (SCR/) are present in selected control groups where the `00-checklist-engine/` engine is applicable.

## Standards Reference

- ISO/IEC 42001:2023 — Artificial Intelligence Management System (normative)
- ISO/IEC 42001:2023 Annex A — AIMS controls (normative)
- ISO/IEC 42001:2023 Annex B — Implementation guidance (informative)
- ISO/IEC 27001:2022 — Information Security Management System (prerequisite)
- EU AI Act (Regulation 2024/1689) — Regulatory context for high-risk AI systems
- NIST AI RMF (2023) — Informational reference for AI risk management
