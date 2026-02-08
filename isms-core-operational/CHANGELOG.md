# Changelog — ISMS CORE Operational

All notable changes to ISMS CORE Operational will be documented here.

This project uses a simple versioning approach:
- **Major**: structural or methodology changes
- **Minor**: new control packs, significant expansions
- **Patch**: fixes, QA improvements, clarifications

## [Unreleased]
- TBD

## [1.0] - 2026-02-08
### Added
- **53 Operational Policies (OP-POL)** — one self-contained policy per control group
  - Swiss nFADP aligned, GDPR referenced where applicable
  - PCI DSS gated (opt-in for organisations in scope)
  - All 53 reviewed with Copilot Stage 2 audit criteria
- **53 Compliance Checklist Generators (SCR)** — one per control group
  - Shared engine architecture: `op_checklist_engine.py` (642 lines)
  - Each generator extracts "shall" requirements from the corresponding OP-POL
  - Pattern: Executive Summary + Dashboard + N domain checklist sheets
  - Dashboard with COUNTIF aggregation and traffic-light scoring
- **53 Compliance Checklist Workbooks (WKBK)** — generated Excel output
  - Naming: `ISMS-OP-CHK-A.X.X_Compliance_Checklist_YYYYMMDD.xlsx`
  - Standard colour palette (identical to Framework product)
  - Swiss DD.MM.YYYY date format
- **CONTROLS.md** — full index of all 53 control packs with links
- **README.md** — product overview, quick start, comparison with Framework
- **STATUS.md** — implementation status dashboard
- **CHANGELOG.md** — this file

### Quality
- All 53 generators validated with zero runtime errors
- All 53 OP-POLs Copilot S2 reviewed and findings applied
- Standard palette, date format, and British English across all generators

---

*Where bamboo antennas actually work.* 🎋
