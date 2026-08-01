# ISMS CORE Cloud Extension Pack

**Status:** v1.0 Complete (2026-03-09) — Cloud Sec added 2026-08-01
**Standards:** ISO/IEC 27018:2025 (Ed. 3) — PII Protection in Public Cloud · ISO/IEC 27017:2026 (Ed. 2) — Cloud Security Controls
**Prerequisite:** ISMS CORE Framework must be installed

---

## Scope

Two standalone families, 16 control groups total:

| Family | Folder | Groups | Standard |
|--------|--------|--------|----------|
| PII Cloud Controls | `iso27018-pii-cloud/` | 12 | ISO 27018:2025 Annex A |
| Cloud Security Controls | `iso27017-sec-cloud/` | 4 | ISO 27017:2026 (4 standalone extension controls) |

## ISO 27018:2025

ISO 27018:2025 (Ed. 3) specifies controls for public cloud service providers (PII processors) acting on behalf of their customers. It provides 12 Annex A control groups covering:

- PII consent and purpose legitimacy
- Data collection limitation and minimisation
- Data subject access and correction rights
- Accountability, transparency, and information security for PII

## ISO 27017:2026

ISO/IEC 27017:2026 Edition 2 was published 2026-07-29, cancelling and replacing the 2015 first edition. The Cloud Sec content pack covers the 4 controls that are genuinely standalone extensions to ISO 27001 Annex A — everything else in ISO 27017 maps onto an existing ISMS-CORE Framework control and is covered by the guidance addendum instead of being duplicated:

- **A.5.38** — Shared roles and responsibilities in a cloud environment
- **A.5.39** — Agreement on cloud service partner roles and responsibilities
- **A.8.35** — Segregation in virtual computing environments
- **A.8.36** — Detection and prevention of unauthorised use of cloud services

Plus a guidance addendum (`cld-sec-guidance-addendum/`) covering how the remaining 38 existing Annex A controls apply in a cloud context.

## Relationship to ISMS CORE Privacy (ISO 27701:2025)

| Product | Target | Standard |
|---------|--------|----------|
| **CLOUD** (this product) | Cloud service providers processing PII | ISO 27018:2025 |
| **PRIVACY** (`isms-core-privacy/`) | PII controllers and processors generally | ISO 27701:2025 |

Both are standalone standards (neither requires ISO 27001 certification), though both complement and are commonly implemented alongside an ISO 27001:2022 ISMS. If your organisation is both a cloud PII processor **and** needs a full PIMS, use both products together.

## Standards Reference

- ISO/IEC 27018:2025 (Ed. 3) — PII in Public Cloud (Annex A)
- ISO/IEC 27001:2022 — Information Security Management System (complements; not a prerequisite)
- ISO/IEC 27017:2026 (Ed. 2) — Cloud Security Controls; cancels and replaces the 2015 first edition. Standalone SEC product, see `iso27017-sec-cloud/` above
- GDPR (EU 2016/679) — Mandatory for EU-scope organisations
