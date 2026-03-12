# ISMS CORE Privacy Extension Pack

**Status:** v1.0 Complete (2026-03-09)
**Standards:** ISO/IEC 27701:2025 (Ed. 2) + ISO/IEC 27018:2025 (Annex A overlay)
**Prerequisite:** ISMS CORE Framework (50-isms-core-framework/) must be installed

---

## Scope

21 control groups across 3 privacy families:

| Family | Folder | Groups | ISO 27701 Annex |
|--------|--------|--------|-----------------|
| Privacy-Controller | `privacy-controller/` | 8 | A.1.x (31 controls) |
| Privacy-Processor | `privacy-processor/` | 5 | A.2.x (18 controls) |
| Privacy-Shared | `privacy-shared/` | 8 | A.3.x (29 controls) |

Plus 2 foundation policy documents in `00-priv-foundation-policies/`.

## ISO 27018:2025

The 25 Annex A PII-specific controls from ISO 27018:2025 are delivered as a crosswalk
overlay on `priv-a.2.4-pii-processing-security` and adjacent processor packs.
The 93 body controls of 27018 are ISO 27002 content and are not duplicated.

## Standards Reference

- ISO/IEC 27701:2025 (Ed. 2) — Privacy Information Management System
- ISO/IEC 27018:2025 (Ed. 3) — PII in Public Cloud (Annex A)
- ISO/IEC 27017:2019 — Cloud Security Controls (Tier 3 informational reference)
- GDPR (EU 2016/679) — Mandatory for EU-scope organisations
- CH-nDSG/FADP — Mandatory for Swiss-scope organisations
