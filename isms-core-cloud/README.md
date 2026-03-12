# ISMS CORE Cloud Extension Pack

**Status:** v1.0 Complete (2026-03-09)
**Standards:** ISO/IEC 27018:2025 (Ed. 3) — PII Protection in Public Cloud
**Prerequisite:** ISMS CORE Framework must be installed

---

## Scope

12 control groups across 1 cloud privacy family:

| Family | Folder | Groups | ISO 27018:2025 Annex |
|--------|--------|--------|----------------------|
| PII Cloud Controls | `iso27018-pii-cloud/` | 12 | A.1–A.12 |

The `iso27017-sec-cloud/` folder is reserved for the future ISO 27017:2025 SEC product (not yet built).

## ISO 27018:2025

ISO 27018:2025 (Ed. 3) specifies controls for public cloud service providers (PII processors) acting on behalf of their customers. It provides 12 Annex A control groups covering:

- PII consent and purpose legitimacy
- Data collection limitation and minimisation
- Data subject access and correction rights
- Accountability, transparency, and information security for PII

## Relationship to ISMS CORE Privacy (ISO 27701:2025)

| Product | Target | Standard |
|---------|--------|----------|
| **CLOUD** (this product) | Cloud service providers processing PII | ISO 27018:2025 |
| **PRIVACY** (`isms-core-privacy/`) | PII controllers and processors generally | ISO 27701:2025 |

Both extend ISO 27001:2022 ISMS. If your organisation is both a cloud PII processor **and** needs a full PIMS, use both products together.

## Standards Reference

- ISO/IEC 27018:2025 (Ed. 3) — PII in Public Cloud (Annex A)
- ISO/IEC 27001:2022 — Information Security Management System (prerequisite)
- ISO/IEC 27017:2019 — Cloud Security Controls (Tier 3 informational reference)
- GDPR (EU 2016/679) — Mandatory for EU-scope organisations
