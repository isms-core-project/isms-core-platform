**ISMS-IMP-A.7.10.3-TG - Media Lifecycle Tracking Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Media Lifecycle Management, Disposal & Re-use |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.5-2.6 (Disposal & Paper Documents) |
| **Purpose** | Assess organisational compliance with storage media lifecycle management from acquisition through disposal, including secure destruction and re-use procedures |
| **Target Audience** | IT Operations, Asset Management, Procurement, Facilities, Compliance Officers, Auditors |
| **Assessment Type** | Lifecycle Process & Operational Compliance |
| **Review Cycle** | Annual (minimum) or After Regulatory Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Media Lifecycle Tracking assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organisation (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, colour coding | ~60 | Read-only |
| 2 | 2. Acquisition & Procurement | Procurement controls, registration | ~25-50 | 13 data rows |
| 3 | 3. Internal Re-use | Secure erasure, verification | ~25-50 | 13 data rows |
| 4 | 4. Disposal Methods | Destruction by classification | ~25-50 | 13 data rows |
| 5 | 5. Third-Party Disposal | Vendor management, certificates | ~25-50 | 13 data rows |
| 6 | 6. Paper Document Lifecycle | Physical media destruction | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Lifecycle metrics, compliance | ~60 | Formula-driven |
| 8 | Evidence Register | Certificates and documentation | ~110 | 100 data rows |
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

# Sheet 2: Acquisition & Procurement

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Media Category | 25 | Text | Type of media procured |
| B | Procurement Type | 18 | Dropdown | Standard/Non-Standard/Emergency |
| C | Control Description | 35 | Text | Procurement control |
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
| R | Approved Suppliers | 25 | Text | Vendor names |
| S | Registration Required | 18 | Dropdown | Yes/No |
| T | Quality Standards | 22 | Text | Standards required |

## Data Validation Rules

**Column B - Procurement Type:**
```
Dropdown: Standard Purchase, Non-Standard Request, Emergency Purchase, Replacement, Upgrade, N/A
```

**Column F - Status:**
```
Dropdown: Compliant, Partially Compliant, Non-Compliant, Not Assessed, N/A
```

**Column S - Registration Required:**
```
Dropdown: Yes - Automatic (PO), Yes - Manual Entry, No - Track Only, N/A
```

---

# Sheet 3: Internal Re-use

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Re-use Scenario | 25 | Text | Scenario description |
| B | Media Type | 18 | Dropdown | HDD/SSD/USB/Tape/Other |
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
| R | Erasure Method | 25 | Dropdown | Erasure type |
| S | Verification Required | 20 | Dropdown | Verification level |
| T | Documentation | 22 | Dropdown | Documentation type |

## Data Validation Rules

**Column R - Erasure Method:**
```
Dropdown: NIST 800-88 Clear, NIST 800-88 Purge, Cryptographic Erasure, Factory Reset, Full Format, Quick Format, Physical Destruction
```

**Column S - Verification Required:**
```
Dropdown: Full Verification, Sample Verification (10%), Log Review Only, None
```

**Column T - Documentation:**
```
Dropdown: Erasure Certificate, Asset System Log, Manual Log Entry, None Required
```

---

# Sheet 4: Disposal Methods

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Disposal Scenario | 25 | Text | Scenario description |
| B | Classification Level | 18 | Dropdown | Data classification |
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
| R | Destruction Method | 25 | Dropdown | Method type |
| S | Witness Required | 18 | Dropdown | Witness needs |
| T | Certificate Required | 18 | Dropdown | Certificate needs |

## Data Validation Rules

**Column R - Destruction Method:**
```
Dropdown: Physical Shredding, Degaussing, Degaussing + Shredding, Incineration, Secure Overwriting, Cryptographic Erasure, Crushing, Disintegration
```

**Column S - Witness Required:**
```
Dropdown: Yes - Internal Witness, Yes - External Auditor, Yes - Both, No, For Certain Classifications
```

**Column T - Certificate Required:**
```
Dropdown: Yes - Individual Certificate, Yes - Batch Certificate, No Certificate, Vendor Report Only
```

---

# Sheet 5: Third-Party Disposal

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Vendor Name | 25 | Text | Disposal vendor |
| B | Service Type | 18 | Dropdown | Destruction/Collection/Both |
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
| R | Contract Status | 20 | Dropdown | Contract state |
| S | Certifications | 25 | Text | Vendor certifications |
| T | Certificate SLA | 18 | Text | Days to certificate |

## Data Validation Rules

**Column R - Contract Status:**
```
Dropdown: Active Contract, Contract Pending Renewal, Contract Expired, No Contract (Spot Purchase), Under Evaluation
```

---

# Sheet 6: Paper Document Lifecycle

## Column Structure (A-Q Standard, R-T Extended)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Document Category | 25 | Text | Paper type |
| B | Classification | 18 | Dropdown | CONFIDENTIAL/INTERNAL/PUBLIC |
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
| R | Shredding Standard | 22 | Dropdown | DIN standard |
| S | Collection Process | 22 | Dropdown | How collected |
| T | Destruction Frequency | 18 | Dropdown | How often |

## Data Validation Rules

**Column R - Shredding Standard:**
```
Dropdown: DIN 66399 P-4 (Cross-cut), DIN 66399 P-5 (Fine Cross-cut), DIN 66399 P-6 (High Security), DIN 66399 P-7 (Super High Security), Strip Shred, Not Specified
```

**Column S - Collection Process:**
```
Dropdown: Secure Bins (Locked), Secure Bins (Unlocked), On-Demand Shredding, Contractor Collection, Centralised Collection Point
```

**Column T - Destruction Frequency:**
```
Dropdown: Daily, Weekly, Bi-weekly, Monthly, Quarterly, On-Demand, Event-Based
```

---

# Sheet 7: Summary Dashboard

## Dashboard Sections

**Section 1: Lifecycle Metrics (Rows 3-15)**
- Media acquired this period
- Media re-used this period
- Media disposed this period
- Pending disposal count

**Section 2: Disposal Compliance (Rows 17-28)**
- Certificates received %
- Witnessed destructions %
- Vendor compliance %
- Chain of custody complete %

**Section 3: Re-use Compliance (Rows 30-40)**
- Verification completed %
- Documentation complete %
- Appropriate method used %

**Section 4: Vendor Status (Rows 42-52)**
- Active vendors count
- Expiring certifications
- Pending contract renewals
- Performance issues

**Formula Examples:**

**Compliance Percentage:**
```
=COUNTIF('4. Disposal Methods'!$F$4:$F$16,"Compliant")/COUNTA('4. Disposal Methods'!$F$4:$F$16)
```

**Certificate Rate:**
```
=COUNTIF('4. Disposal Methods'!$T$4:$T$16,"Yes*")/COUNTA('4. Disposal Methods'!$T$4:$T$16)
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
| B | Evidence Type | 18 | Dropdown | Certificate/Contract/Report |
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
Dropdown: Certificate of Destruction, Vendor Contract, Erasure Report, Environmental Certificate, Audit Report, Training Record, Policy Document, Procedure Document, Other
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
- Statement: "I confirm this assessment accurately reflects current lifecycle practices."
- Fields: Name, Title, Signature, Date, Comments

**Level 2 Approval:**
- Title: Management Approval
- Statement: "I approve this assessment and the remediation plan."
- Fields: Name, Title, Signature, Date, Comments

**Level 3 Approval:**
- Title: Executive Approval
- Statement: "Executive Management acknowledges the lifecycle compliance status."
- Fields: Name, Title, Signature, Date, Risk Acceptance

**Next Review (Rows 62-70)**
- Scheduled review date
- Review owner
- Review scope

---

**END OF SPECIFICATION**

---

*"Information is the oxygen of the modern age."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
