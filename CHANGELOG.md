# Changelog

All notable changes to ISMS CORE will be documented here.

This project uses a simple versioning approach:
- **Major**: structural or methodology changes that may require migrations
- **Minor**: new control packs, significant expansions
- **Patch**: fixes, QA improvements, clarifications

## [Unreleased]
- TBD

## [4.5] - 2026-02-06
### Added
- IMP UG/TG split: all 252 IMP files split into User Guide (UG) + Technical Specification (TG) pairs (504 total)
- Header normalization across all 504 split files (standard 3-line format)
- POL files updated with UG/TG references (59 files)

### Changed
- IMP document structure: each IMP now exists as two files (-UG and -TG) instead of one combined document
- POL Related Documents sections expanded with individual UG/TG sub-document references
- STATUS.md, README.md, CONTRIBUTING.md updated to reflect UG/TG architecture
- A.8.8 document control headers normalized to standard table format (18 files)

## [4.4] - 2026-02-04
### Added
- COVERAGE.md - canonical mapping of 93 Annex A controls to 53 control packs
- SECURITY.md - vulnerability reporting policy
- CODE_OF_CONDUCT.md - community standards
- CHANGELOG.md - version history

### Changed
- Updated all documentation to use "control packs" terminology (53 packs → 93 controls)
- PHILOSOPHY.md revised with safer language and clearer positioning
- STACKING.md updated with accurate pack counts and removed unverifiable overlap claims
- README.md updated with accurate metrics (456 scripts, 410K+ lines)

## [4.3] - 2026-02-03
### Added
- Completed control pack coverage across A.5–A.8 (53 packs)
- Expanded evidence generation scripts (456 validated)
- IMP QA v4.3 verification pass (250+ documents)

### Changed
- Improved QA gating and promotion workflow
- Refinements to workbook formula validation pipeline

### Fixed
- Documentation consistency fixes across packs
- Script reliability improvements and validations

## [4.2] - 2026-01-15
### Added
- A.8 Technological Controls section completed (22 packs)
- Business continuity and DR pack (A.5.30, A.8.13-14)

### Changed
- Consolidated related controls into unified packs
- Standardized generator script structure

## [4.1] - 2026-01-01
### Added
- Initial A.5 Organizational Controls packs
- Initial A.6 People Controls packs
- Core generator framework

---

*Where bamboo antennas actually work.* 🎋
