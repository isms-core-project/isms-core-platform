# 🎋 ISMS CORE Coverage Map (ISO/IEC 27001:2022 Annex A)

<p align="center">
  <img src="https://img.shields.io/badge/Control_Packs-53-0066CC?style=flat-square" alt="53 Control Packs"/>
  <img src="https://img.shields.io/badge/Annex_A_Controls-93_Mapped-32CD32?style=flat-square" alt="93 Annex A Controls"/>
  <img src="https://img.shields.io/badge/ISO_27001-2022-DC143C?style=flat-square" alt="ISO 27001:2022"/>
</p>

This document is the canonical mapping between **ISO/IEC 27001:2022 Annex A controls (93)** and **ISMS CORE control packs (53)**.

ISMS CORE uses *control packs* to implement multiple Annex A controls through a cohesive set of artifacts (POL/IMP/SCR/REF/CTX). Coverage in this file describes which pack provides implementation material and evidence tooling for each Annex A control.

> Note: This repository provides implementation packs and mappings. Certification/compliance depends on your organization's scope, operation, and evidence.

---

## 1) Mapping Legend

**Mapping Strength**
- **P (Primary):** main implementation/evidence home for the control
- **S (Supporting):** supports the control (shared evidence, dependencies, related procedures)
- **R (Referenced):** informational only

**Artifacts**
- **POL** Policy
- **IMP** Implementation guidance and assessments
- **SCR** Scripts/generators/workbooks
- **REF** Reference materials
- **CTX** Context documents
- **FORM** Forms, templates and checklists

---

## 2) Control Pack Index (53)

| Pack ID | Folder | Artifacts |
|---:|---|---|
| P01 | `isms-a.5.1-2-6.1-2-secure-employment-and-roles` | POL, IMP, SCR |
| P02 | `isms-a.5.3-segregation-of-duties` | POL, IMP, SCR |
| P03 | `isms-a.5.4-management-responsibilities` | POL, IMP, SCR |
| P04 | `isms-a.5.5-6-external-communications` | POL, IMP, SCR |
| P05 | `isms-a.5.7-threat-intelligence` | POL, IMP, SCR |
| P06 | `isms-a.5.8-information-security-in-project-management` | POL, IMP, SCR |
| P07 | `isms-a.5.9-inventory-of-information-and-assets` | POL, IMP, SCR |
| P08 | `isms-a.5.10-11-asset-usage-lifecycle` | POL, IMP, SCR |
| P09 | `isms-a.5.12-13-classification-and-labelling` | POL, IMP, SCR |
| P10 | `isms-a.5.14-information-transfer` | POL, IMP, SCR |
| P11 | `isms-a.5.15-16-18-identity-access-management` | POL, IMP, SCR |
| P12 | `isms-a.5.17-authentication-information` | POL, IMP, SCR |
| P13 | `isms-a.5.19-23-cloud-services` | POL, IMP, SCR, REF |
| P14 | `isms-a.5.24-28-incident-management-lifecycle` | POL, IMP, SCR |
| P15 | `isms-a.5.29-security-during-disruption` | POL, IMP, SCR |
| P16 | `isms-a.5.30-8.13-14-business-continuity-dr` | POL, IMP, SCR |
| P17 | `isms-a.5.31-legal-statutory-regulatory-contractual-requirements` | POL, IMP, SCR |
| P18 | `isms-a.5.32-33-information-protection` | POL, IMP, SCR |
| P19 | `isms-a.5.34-privacy-and-pii` | POL, IMP, SCR, CTX |
| P20 | `isms-a.5.35-36-compliance-review` | POL, IMP, SCR |
| P21 | `isms-a.5.37-documented-procedures` | POL, IMP, SCR |
| P22 | `isms-a.6.3-awareness-and-training` | POL, IMP, SCR |
| P23 | `isms-a.6.4-5-employment-exit` | POL, IMP, SCR |
| P24 | `isms-a.6.6-confidentiality-nda` | POL, IMP, SCR |
| P25 | `isms-a.6.7-8-remote-working-and-reporting` | POL, IMP, SCR |
| P26 | `isms-a.7.1-2-3-physical-access-control` | POL, IMP, SCR |
| P27 | `isms-a.7.4-5-11-physical-infrastructure` | POL, IMP, SCR |
| P28 | `isms-a.7.6-7-14-information-media-handling` | POL, IMP, SCR |
| P29 | `isms-a.7.8-9-equipment-location-security` | POL, IMP, SCR |
| P30 | `isms-a.7.10-delivery-and-loading-areas` | POL, IMP, SCR |
| P31 | `isms-a.7.12-13-infrastructure-maintenance` | POL, IMP, SCR |
| P32 | `isms-a.8.1-7-18-19-endpoint-security` | POL, IMP, SCR |
| P33 | `isms-a.8.2-3-5-authentication-privileged-access` | POL, IMP, SCR |
| P34 | `isms-a.8.4-access-to-source-code` | POL, IMP, SCR |
| P35 | `isms-a.8.6-capacity-management` | POL, IMP, SCR |
| P36 | `isms-a.8.8-vulnerability-management` | POL, IMP, SCR |
| P37 | `isms-a.8.9-configuration-management` | POL, IMP, SCR, CTX |
| P38 | `isms-a.8.10-data-deletion` | POL, IMP, SCR, REF, FORM |
| P39 | `isms-a.8.11-data-masking` | POL, IMP, SCR, CTX |
| P40 | `isms-a.8.12-data-leakage-prevention` | POL, IMP, SCR |
| P41 | `isms-a.8.15-logging` | POL, IMP, SCR, REF |
| P42 | `isms-a.8.16-monitoring` | POL, IMP, SCR |
| P43 | `isms-a.8.17-clock-synchronization` | POL, IMP, SCR |
| P44 | `isms-a.8.20-22-network-security` | POL, IMP, SCR |
| P45 | `isms-a.8.23-web-filtering` | POL, IMP, SCR |
| P46 | `isms-a.8.24-use-of-cryptography` | POL, IMP, SCR, CTX |
| P47 | `isms-a.8.25-26-29-secure-development` | POL, IMP, SCR |
| P48 | `isms-a.8.27-secure-systems-engineering` | POL, IMP, SCR |
| P49 | `isms-a.8.28-secure-coding` | POL, IMP, SCR, REF, CTX |
| P50 | `isms-a.8.30-outsourced-development` | POL, IMP, SCR |
| P51 | `isms-a.8.31-environment-separation` | POL, IMP, SCR, REF |
| P52 | `isms-a.8.32-change-management` | POL, IMP, SCR, REF |
| P53 | `isms-a.8.33-34-testing-and-audit-protection` | POL, IMP, SCR |

---

## 3) Annex A Coverage (93 controls → packs)

### 3.1 A.5 Organizational Controls (37)

| Control | Mapping |
|---|---|
| A.5.1 | **P:** P01 |
| A.5.2 | **P:** P01 |
| A.5.3 | **P:** P02 |
| A.5.4 | **P:** P03 |
| A.5.5 | **P:** P04 |
| A.5.6 | **P:** P04 |
| A.5.7 | **P:** P05 |
| A.5.8 | **P:** P06 |
| A.5.9 | **P:** P07 |
| A.5.10 | **P:** P08 |
| A.5.11 | **P:** P08 |
| A.5.12 | **P:** P09 |
| A.5.13 | **P:** P09 |
| A.5.14 | **P:** P10 |
| A.5.15 | **P:** P11 |
| A.5.16 | **P:** P11 |
| A.5.17 | **P:** P12 |
| A.5.18 | **P:** P11 |
| A.5.19 | **P:** P13 |
| A.5.20 | **P:** P13 |
| A.5.21 | **P:** P13 |
| A.5.22 | **P:** P13 |
| A.5.23 | **P:** P13 |
| A.5.24 | **P:** P14 |
| A.5.25 | **P:** P14 |
| A.5.26 | **P:** P14 |
| A.5.27 | **P:** P14 |
| A.5.28 | **P:** P14 |
| A.5.29 | **P:** P15, **S:** P16 |
| A.5.30 | **P:** P16, **S:** P15 |
| A.5.31 | **P:** P17 |
| A.5.32 | **P:** P18 |
| A.5.33 | **P:** P18 |
| A.5.34 | **P:** P19 |
| A.5.35 | **P:** P20 |
| A.5.36 | **P:** P20 |
| A.5.37 | **P:** P21 |

### 3.2 A.6 People Controls (8)

| Control | Mapping |
|---|---|
| A.6.1 | **P:** P01 |
| A.6.2 | **P:** P01 |
| A.6.3 | **P:** P22 |
| A.6.4 | **P:** P23, **S:** P01 |
| A.6.5 | **P:** P23, **S:** P01 |
| A.6.6 | **P:** P24 |
| A.6.7 | **P:** P25 |
| A.6.8 | **P:** P25, **S:** P14 |

### 3.3 A.7 Physical Controls (14)

| Control | Mapping |
|---|---|
| A.7.1 | **P:** P26 |
| A.7.2 | **P:** P26 |
| A.7.3 | **P:** P26 |
| A.7.4 | **P:** P27 |
| A.7.5 | **P:** P27 |
| A.7.6 | **P:** P28 |
| A.7.7 | **P:** P28 |
| A.7.8 | **P:** P29 |
| A.7.9 | **P:** P29 |
| A.7.10 | **P:** P30 |
| A.7.11 | **P:** P27 |
| A.7.12 | **P:** P31 |
| A.7.13 | **P:** P31 |
| A.7.14 | **P:** P28 |

### 3.4 A.8 Technological Controls (34)

| Control | Mapping |
|---|---|
| A.8.1 | **P:** P32 |
| A.8.2 | **P:** P33 |
| A.8.3 | **P:** P33 |
| A.8.4 | **P:** P34 |
| A.8.5 | **P:** P33 |
| A.8.6 | **P:** P35 |
| A.8.7 | **P:** P32 |
| A.8.8 | **P:** P36, **S:** P42 |
| A.8.9 | **P:** P37 |
| A.8.10 | **P:** P38 |
| A.8.11 | **P:** P39 |
| A.8.12 | **P:** P40 |
| A.8.13 | **P:** P16 |
| A.8.14 | **P:** P16 |
| A.8.15 | **P:** P41, **S:** P42 |
| A.8.16 | **P:** P42, **S:** P41 |
| A.8.17 | **P:** P43 |
| A.8.18 | **P:** P32 |
| A.8.19 | **P:** P32 |
| A.8.20 | **P:** P44 |
| A.8.21 | **P:** P44 |
| A.8.22 | **P:** P44 |
| A.8.23 | **P:** P45 |
| A.8.24 | **P:** P46, **S:** P12 |
| A.8.25 | **P:** P47, **S:** P52 |
| A.8.26 | **P:** P47 |
| A.8.27 | **P:** P48, **S:** P47 |
| A.8.28 | **P:** P49, **S:** P47 |
| A.8.29 | **P:** P47, **S:** P53 |
| A.8.30 | **P:** P50 |
| A.8.31 | **P:** P51 |
| A.8.32 | **P:** P52, **S:** P47 |
| A.8.33 | **P:** P53 |
| A.8.34 | **P:** P53 |

---

## 4) Change Control

Any change that affects naming, stacking, mapping, or counts must update:
- `COVERAGE.md` (this file)
- `CONTROLS.md` (index)
- `STATUS.md` (metrics)
- `STACKING.md` (grouping narrative)

---

## 5) Changelog

| Date | Change | Author |
|---|---|---|
| 2026-02-04 | Initial coverage map created from current pack list (53 packs) | Gregory Griffin |

---

*Where bamboo antennas actually work.* 🎋
