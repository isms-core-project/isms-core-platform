**ISMS-IMP-A.7.10.2-TG - Media Handling Procedures Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Media Handling, Transportation & Access Controls |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.3-2.4 (Transportation & Storage) |
| **Purpose** | Assess organisational compliance with storage media handling procedures, transportation security, and access controls throughout the media lifecycle |
| **Target Audience** | IT Operations, Physical Security, Logistics, Compliance Officers, Business Unit Managers, Auditors |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Semi-annual (minimum) or After Security Incidents |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Media Handling Procedures assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organisation (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, colour coding | ~60 | Read-only |
| 2 | 2. Media Access Controls | Access requirements by zone/classification | ~25-50 | 13 data rows |
| 3 | 3. Transportation Security | Courier, transport, chain of custody | ~25-50 | 13 data rows |
| 4 | 4. Physical Storage Controls | Storage locations, environmental | ~25-50 | 13 data rows |
| 5 | 5. Media Use Procedures | Operational handling procedures | ~25-50 | 13 data rows |
| 6 | 6. Incident Response | Lost/stolen media procedures | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Compliance metrics overview | ~60 | Formula-driven |
| 8 | Evidence Register | Supporting documentation | ~110 | 100 data rows |
| 9 | Approval Sign-Off | Three-level approval workflow | ~75 | Text entry |

---

# Sheet 1: Instructions & Legend

## Layout Structure

**Header Section (Rows 1-5)**
- Document title and ID
- Assessment date and version
- Organisation name placeholder

**Purpose Section (Rows 7-15)**
- Assessment objectives
- Scope definition
- Related policy reference

**Legend Section (Rows 17-35)**
- Status dropdown values and meanings
- Colour coding explanation
- Column header definitions

**Completion Guidelines (Rows 37-55)**
- Step-by-step workflow
- Time estimates
- Support contacts

**Column Width Specifications:**
| Column | Width | Content |
|--------|-------|---------|
| A | 15 | Section headers |
| B | 60 | Description text |
| C | 15 | Status/Values |

---

# Sheet 2: Media Access Controls

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Zone/Location | 25 | Text | Storage area identifier |
| B | Classification Stored | 18 | Dropdown | CONFIDENTIAL/INTERNAL/PUBLIC |
| C | Control Description | 35 | Text | Access control description |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Not Started/In Progress/Complete |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Access Control Type | 22 | Dropdown | Key Lock / Card Access / Biometric / Combination |
| S | Authorised Personnel | 25 | Text | Roles or named individuals |
| T | Review Frequency | 18 | Dropdown | Monthly / Quarterly / Semi-annual / Annual |

## Data Validation Rules

**Column B - Classification:**
```
Dropdown: CONFIDENTIAL, INTERNAL, PUBLIC, MIXED, N/A
```

**Column F - Status:**
```
Dropdown: Compliant, Partially Compliant, Non-Compliant, Not Assessed, N/A
```

**Column K - Risk Level:**
```
Dropdown: Critical, High, Medium, Low, N/A
```

**Column O - Remediation Status:**
```
Dropdown: Not Started, In Progress, On Hold, Complete, Verified
```

**Column R - Access Control Type:**
```
Dropdown: Key Lock, Card Access, Biometric, Combination Lock, Multi-Factor, PIN Code, None
```

**Column T - Review Frequency:**
```
Dropdown: Monthly, Quarterly, Semi-annual, Annual, Ad-hoc
```

## Conditional Formatting

**Status Column (F):**
- Compliant: Green fill (#C6EFCE)
- Partially Compliant: Yellow fill (#FFEB9C)
- Non-Compliant: Red fill (#FFC7CE)
- Not Assessed: Grey fill (#D9D9D9)

**Risk Level Column (K):**
- Critical: Dark red fill (#8B0000), white text
- High: Red fill (#FF0000)
- Medium: Orange fill (#FFA500)
- Low: Yellow fill (#FFFF00)

---

# Sheet 3: Transportation Security

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Transportation Scenario | 30 | Text | Scenario description |
| B | Classification Level | 18 | Dropdown | Media classification |
| C | Control Description | 35 | Text | Required controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Transport Method | 22 | Dropdown | Transport type |
| S | Chain of Custody Required | 20 | Dropdown | Yes/No/Partial |
| T | Packaging Requirement | 25 | Dropdown | Packaging type |

## Data Validation Rules

**Column R - Transport Method:**
```
Dropdown: Secure Courier, Standard Courier, Personal Transport, Internal Mail, Hand Delivery, Digital Transfer, N/A
```

**Column S - Chain of Custody Required:**
```
Dropdown: Yes - Full Documentation, Yes - Basic Log, No, N/A
```

**Column T - Packaging Requirement:**
```
Dropdown: Tamper-Evident Packaging, Sealed Container, Locked Case, Standard Packaging, N/A
```

---

# Sheet 4: Physical Storage Controls

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Storage Location | 25 | Text | Location identifier |
| B | Classification Stored | 18 | Dropdown | Classification level |
| C | Control Description | 35 | Text | Storage controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Storage Type | 22 | Dropdown | Cabinet/Safe/Vault |
| S | Environmental Monitoring | 22 | Dropdown | Monitoring type |
| T | Fire Suppression | 20 | Dropdown | Suppression type |

## Data Validation Rules

**Column R - Storage Type:**
```
Dropdown: Locked Cabinet, Fire-Rated Safe, Secure Vault, Server Room, Archive Room, Standard Shelf, Secure Disposal Bin
```

**Column S - Environmental Monitoring:**
```
Dropdown: Temperature Only, Humidity Only, Temperature + Humidity, Full Environmental, None
```

**Column T - Fire Suppression:**
```
Dropdown: Gas Suppression, Wet Sprinkler, Dry Sprinkler, Fire Extinguisher, None
```

---

# Sheet 5: Media Use Procedures

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Use Procedure | 30 | Text | Procedure description |
| B | Procedure Type | 18 | Dropdown | Data Transfer/Receipt/Return/Archive |
| C | Control Description | 35 | Text | Required controls |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Applicable Media Type | 22 | Dropdown | Media type |
| S | Procedure Owner | 20 | Text | Role responsible |
| T | Training Required | 18 | Dropdown | Training needs |

## Data Validation Rules

**Column R - Applicable Media Type:**
```
Dropdown: Removable Media, Fixed Storage, Cloud Storage, Paper Documents, All Media Types
```

**Column T - Training Required:**
```
Dropdown: Yes - Initial Only, Yes - Annual Refresh, Yes - Quarterly, No, Role-Specific
```

---

# Sheet 6: Incident Response

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Incident Scenario | 30 | Text | Scenario description |
| B | Incident Type | 18 | Dropdown | Lost/Stolen/Damaged/Breach |
| C | Control Description | 35 | Text | Response requirements |
| D | Requirement Reference | 15 | Text | Policy reference |
| E | Assessment Criteria | 30 | Text | How compliance measured |
| F | Status | 15 | Dropdown | Compliant/Partial/Non-Compliant/N/A |
| G | Assessor | 15 | Text | Who assessed |
| H | Assessment Date | 12 | Date | When assessed |
| I | Evidence Reference | 15 | Text | Evidence ID |
| J | Gap Description | 30 | Text | If non-compliant |
| K | Risk Level | 12 | Dropdown | Critical/High/Medium/Low |
| L | Remediation Action | 30 | Text | Planned fix |
| M | Remediation Owner | 15 | Text | Who responsible |
| N | Target Date | 12 | Date | Planned completion |
| O | Remediation Status | 15 | Dropdown | Status |
| P | Verification | 20 | Text | How verified |
| Q | Notes | 25 | Text | Additional comments |
| R | Response Procedure | 25 | Text | Procedure reference |
| S | Escalation Path | 25 | Text | Escalation contacts |
| T | Notification Required | 22 | Dropdown | Notification needs |

## Data Validation Rules

**Column B - Incident Type:**
```
Dropdown: Lost Media, Stolen Media, Damaged Media, Unauthorised Access, Data Breach, Multiple
```

**Column T - Notification Required:**
```
Dropdown: Regulatory (GDPR/FINMA), Internal Only, Both Internal + Regulatory, None, To Be Determined
```

---

# Sheet 7: Summary Dashboard

## Dashboard Sections

**Section 1: Control Status Overview (Rows 3-12)**
- Access controls assessed
- Transportation controls assessed
- Storage controls assessed
- Use procedures assessed
- Incident procedures assessed

**Section 2: Compliance Metrics (Rows 14-25)**
- Procedures with documentation %
- Procedures with training %
- Procedures tested/exercised %
- Gap remediation in progress

**Section 3: Risk Distribution (Rows 27-35)**
- Critical gaps count
- High-risk gaps count
- Medium-risk gaps count
- Low-risk gaps count

**Section 4: Key Indicators (Rows 37-50)**
- Chain of custody compliance %
- Approved courier usage %
- Environmental monitoring coverage %
- Incident response tested (date)

**Formula Examples:**

**Compliance Percentage:**
```
=COUNTIF('2. Media Access Controls'!$F$4:$F$16,"Compliant")/COUNTA('2. Media Access Controls'!$F$4:$F$16)
```

**Risk Count:**
```
=COUNTIF('2. Media Access Controls'!$K$4:$K$16,"Critical")
```

## Dashboard Styling

**Header Row:**
- Font: Calibri 14pt Bold
- Fill: Navy Blue (#003366)
- Text: White

**Metric Labels:**
- Font: Calibri 11pt
- Fill: Light Grey (#F2F2F2)

**Metric Values:**
- Font: Calibri 12pt Bold
- Conditional formatting by threshold

---

# Sheet 8: Evidence Register

## Column Structure

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 12 | Text | Unique identifier (EV-001) |
| B | Evidence Type | 18 | Dropdown | Document/Screenshot/Photo/Log |
| C | Description | 35 | Text | What evidence shows |
| D | Related Control | 15 | Text | Control reference |
| E | Source Sheet | 15 | Text | Assessment sheet |
| F | Date Collected | 12 | Date | Collection date |
| G | Collected By | 15 | Text | Who collected |
| H | File Name | 25 | Text | Document name |
| I | Location | 30 | Text | Storage location/link |
| J | Retention | 12 | Text | Retention period |
| K | Notes | 25 | Text | Additional context |

## Data Validation

**Column B - Evidence Type:**
```
Dropdown: Policy Document, Procedure Document, Screenshot, Photograph, System Log, Certificate, Training Record, Audit Report, Other
```

---

# Sheet 9: Approval Sign-Off

## Layout Structure

**Document Control (Rows 3-12)**
- Assessment title and ID
- Assessment date
- Period covered
- Prepared by

**Assessment Summary (Rows 14-25)**
- Overall compliance status
- Critical findings
- Key recommendations

**Approval Section (Rows 27-60)**

**Level 1 Approval:**
- Title: Technical/Operational Approval
- Statement: "I confirm this assessment accurately reflects current handling practices."
- Fields: Name, Title, Signature, Date, Comments

**Level 2 Approval:**
- Title: Management Approval
- Statement: "I approve this assessment and the remediation plan."
- Fields: Name, Title, Signature, Date, Comments

**Level 3 Approval:**
- Title: Executive Approval
- Statement: "Executive Management acknowledges the handling compliance status."
- Fields: Name, Title, Signature, Date, Risk Acceptance

**Next Review (Rows 62-70)**
- Scheduled review date
- Review owner
- Review scope

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-06 -->
