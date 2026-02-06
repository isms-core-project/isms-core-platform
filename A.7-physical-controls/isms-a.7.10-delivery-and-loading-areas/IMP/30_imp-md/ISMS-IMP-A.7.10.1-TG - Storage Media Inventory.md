**ISMS-IMP-A.7.10.1-TG - Storage Media Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Storage Media Inventory & Classification |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.2 (Removable Media Management) |
| **Purpose** | Assess organisational compliance with storage media inventory, registration, and classification requirements across the media lifecycle |
| **Target Audience** | IT Operations, Asset Management, Information Security Officers, Physical Security, Compliance Officers, Auditors |
| **Assessment Type** | Asset Inventory & Operational Compliance |
| **Review Cycle** | Quarterly (minimum) or After Significant Media Acquisitions |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Storage Media Inventory assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organisation (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, colour coding, definitions | ~60 | Read-only |
| 2 | 2. Digital Storage Media | HDD, SSD, USB, tape, optical inventory | ~25-50 | 13 data rows |
| 3 | 3. Removable Media Registry | Authorised removable devices | ~25-50 | 13 data rows |
| 4 | 4. Fixed Storage Assets | Servers, NAS, SAN inventory | ~25-50 | 13 data rows |
| 5 | 5. Cloud Storage Mapping | Cloud storage locations | ~25-50 | 13 data rows |
| 6 | 6. Physical Documents | Paper, microfilm, archive storage | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Inventory metrics, compliance overview | ~60 | Formula-driven |
| 8 | Evidence Register | Links to supporting documentation | ~110 | 100 data rows |
| 9 | Approval Sign-Off | Three-level approval workflow | ~75 | Text entry |

**Total Data Entry Points:** ~150-200 (depending on media inventory size)

---

# Sheet 2: Digital Storage Media

## Purpose
Document complete inventory of all digital storage devices.

## Column Definitions (17 standard + 3 extended = 20 total)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Media ID / Asset Tag | 20 | Text | Unique identifier (e.g., "USB-001", "HDD-SRV-001") |
| B | Media Type | 18 | Dropdown | HDD / SSD / USB / SD Card / Tape / Optical / Other |
| C | Data Classification | 18 | Dropdown | Public / Internal / Confidential / Restricted |
| D | Serial Number | 25 | Text | Manufacturer serial number |
| E | Assigned Custodian | 20 | Text | Person responsible for media |
| F | Status | 18 | Dropdown | Registered / Unregistered / Pending Disposal |
| G | Acquisition Date | 12 | Date | When media was acquired |
| H | Last Audit Date | 12 | Date | Most recent inventory verification |
| I | Next Audit Date | 12 | Date | Scheduled next verification |
| J | Gap Identified | 25 | Text | If not compliant, describe issue |
| K | Remediation Plan | 25 | Text | How gap will be addressed |
| L | Target Completion | 12 | Date | Remediation deadline |
| M | Risk Level | 12 | Dropdown | Critical / High / Medium / Low |
| N | Evidence Reference | 20 | Text | Link to Evidence Register (EV-XXX) |
| O | Notes / Comments | 25 | Text | Additional context |
| P | Remediation Owner | 18 | Text | Person responsible for fix |
| Q | Budget Required | 15 | Dropdown | Yes / No / Unknown |
| R | Physical Location | 22 | Text | Building/Room/Cabinet location |
| S | Encryption Status | 18 | Dropdown | Encrypted / Not Encrypted / N/A |
| T | Capacity (GB) | 15 | Number | Storage capacity |

## Data Validation Rules

**Column B - Media Type:**
```
Dropdown: HDD, SSD, USB Flash Drive, SD Card, Backup Tape, Optical Media, Other
```

**Column C - Data Classification:**
```
Dropdown: Public, Internal, Confidential, Restricted
```

**Column F - Status:**
```
Dropdown: Registered, Unregistered, Pending Disposal, In Transit, Lost/Stolen
```

**Column S - Encryption Status:**
```
Dropdown: Encrypted (AES-256), Encrypted (Hardware), Not Encrypted, N/A, Unknown
```

---

# Sheet 3: Removable Media Registry

## Purpose
Register all authorised removable media with approval documentation.

## Extended Columns (R-T) - Registry-Specific

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Authorisation Reference | 22 | Text | Approval ticket/form number |
| S | Authorised User(s) | 22 | Text | Personnel permitted to use |
| T | Permitted Use Cases | 30 | Text | Approved usage scenarios |

## Data Validation Rules (Extended Columns)

**Column R - Authorisation Reference:**
```
Text: Reference to approval (e.g., "REQ-2026-001", "IT-APPROVE-123")
```

---

# Sheet 4: Fixed Storage Assets

## Purpose
Inventory all fixed storage systems (servers, NAS, SAN).

## Extended Columns (R-T) - Fixed Storage-Specific

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | System Type | 18 | Dropdown | Server / NAS / SAN / Archive / Backup |
| S | Total Capacity (TB) | 18 | Number | Total storage capacity |
| T | Utilisation (%) | 15 | Number | Current capacity used |

## Data Validation Rules (Extended Columns)

**Column R - System Type:**
```
Dropdown: Physical Server, Virtual Server, NAS, SAN, Archive System, Backup Appliance
```

---

# Sheet 5: Cloud Storage Mapping

## Purpose
Document all cloud storage locations and configurations.

## Extended Columns (R-T) - Cloud-Specific

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Cloud Type | 18 | Dropdown | IaaS / PaaS / SaaS / Hybrid |
| S | Provider Name | 22 | Text | Cloud service provider |
| T | Data Residency | 22 | Dropdown | EU / Switzerland / US / Other |

## Data Validation Rules (Extended Columns)

**Column R - Cloud Type:**
```
Dropdown: IaaS, PaaS, SaaS, Hybrid, Multi-Cloud
```

**Column T - Data Residency:**
```
Dropdown: Switzerland, EU, US, UK, APAC, Multiple Regions, Unknown
```

---

# Sheet 6: Physical Documents

## Purpose
Inventory physical document storage containing sensitive information.

## Extended Columns (R-T) - Physical-Specific

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Document Type | 18 | Dropdown | Paper / Microfilm / Microfiche / Archive Box |
| S | Storage Location | 25 | Text | Building/room/cabinet identifier |
| T | Access Control | 22 | Dropdown | Key Lock / Combination / Card Access / Biometric |

## Data Validation Rules (Extended Columns)

**Column R - Document Type:**
```
Dropdown: Paper Documents, Microfilm, Microfiche, Archive Boxes, Mixed Media
```

**Column T - Access Control:**
```
Dropdown: Key Lock, Combination Lock, Card Access, Biometric, Multi-Factor, None
```

---

# Sheet 7: Summary Dashboard

## Purpose
Provide inventory metrics and compliance overview.

## Dashboard Sections

**Section 1: Inventory Totals (Rows 3-15)**
- Total digital media items
- Total removable media items
- Total fixed storage systems
- Total cloud storage locations
- Total physical storage locations

**Section 2: Classification Distribution (Rows 17-25)**
- CONFIDENTIAL media count and percentage
- INTERNAL media count and percentage
- PUBLIC media count and percentage

**Section 3: Compliance Metrics (Rows 27-40)**
- Registered media percentage
- Encryption compliance percentage
- Authorisation compliance (removable)
- Items requiring remediation

**Section 4: Key Performance Indicators (Rows 42-55)**
- Overdue audits count
- Expired authorisations count
- Unencrypted CONFIDENTIAL media
- Lost/stolen media incidents

---

# Sheet 8: Evidence Register

## Purpose
Document all evidence supporting inventory assessment.

## Column Structure

| Column | Header | Width | Purpose |
|--------|--------|-------|---------|
| A | Evidence ID | 12 | Unique identifier (EV-001) |
| B | Assessment Sheet | 20 | Related sheet reference |
| C | Related Media/System | 30 | Media item or system name |
| D | Evidence Type | 20 | Document category |
| E | Evidence Title/Description | 35 | Brief description |
| F | File Location/Link | 40 | Storage path or URL |
| G | Date Created/Collected | 12 | Evidence date |
| H | Retention Period | 15 | How long to retain |
| I | Next Review Date | 12 | Scheduled review |
| J | Owner/Custodian | 20 | Evidence owner |
| K | Notes | 30 | Additional context |

---

# Sheet 9: Approval Sign-Off

## Purpose
Three-level approval workflow for assessment validation.

## Approval Structure

**Level 1: Technical/Operational**
- Role: IT Operations Manager / Asset Management Lead
- Validates: Inventory accuracy, completeness
- Statement: "I confirm this assessment accurately reflects our storage media inventory."

**Level 2: Management**
- Role: CISO / IT Director
- Validates: Compliance posture, remediation plans
- Statement: "I approve the remediation plans and resource allocation."

**Level 3: Executive**
- Role: COO / CRO / Executive Management
- Validates: Overall posture, risk acceptance
- Statement: "Executive leadership acknowledges media inventory status and risks."

---

**END OF SPECIFICATION**

---

*"The price of reliability is the pursuit of the utmost simplicity."*
- C.A.R. Hoare

<!-- QA_VERIFIED: 2026-02-06 -->
