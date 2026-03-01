<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.11.1-TG:framework:TG:a.8.11.1 -->
**ISMS-IMP-A.8.11.1-TG - Data Inventory & Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Inventory & Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.11.1-TG |
| **Related Policy** | ISMS-POL-A.8.11 (Data Masking) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.11 (Data Masking) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.11 (Data Masking)
- ISMS-IMP-A.8.11.2 (Masking Technique Selection & Requirements)
- ISMS-IMP-A.8.11.3 (Environment Coverage Assessment)
- ISMS-IMP-A.8.11.4 (Testing & Validation Framework)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a811_1_data_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.11.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | System Inventory |
| 3 | Data Category Reference |
| 4 | Sensitive Data Inventory |
| 5 | Classification Matrix |
| 6 | Regulatory Mapping |
| 7 | Data Owner Assignment |
| 8 | Masking Priority Matrix |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | System ID |
| 2 | System Name |
| 3 | System Type |
| 4 | Environment |
| 5 | Contains Sensitive Data? |
| 6 | Data Categories Present |
| 7 | Hosting Location |
| 8 | Primary Data Owner |
| 9 | System Owner/Admin |
| 10 | Inventory Status |
| 11 | Last Inventory Date |
| 12 | Next Review Date |
| 13 | Record Count (Approx) |
| 14 | Retention Period |
| 15 | Regulatory Scope |
| 16 | Decommission Date |
| 17 | Notes/Comments |
| 18 | Category ID |
| 19 | Category Name |
| 20 | Description |
| 21 | Examples |
| 22 | Sensitivity Level |
| 23 | Masking Priority |
| 24 | Regulatory Driver |
| 25 | Data Element ID |
| 26 | Database/Schema |
| 27 | Table/Collection Name |
| 28 | Field/Column Name |
| 29 | Data Type |
| 30 | Data Category |
| 31 | Specific PII Type |
| 32 | Contains PII? |
| 33 | Masking Required? |
| 34 | Current Masking Status |
| 35 | Data Owner |
| 36 | Discovery Method |
| 37 | Discovery Date |
| 38 | Organisational Class |
| 39 | Typical Sensitivity |
| 40 | Data Categories |
| 41 | Masking Requirement |
| 42 | Count of Fields |
| 43 | Field Name |
| 44 | Organisational Classification |
| 45 | Classification Rationale |
| 46 | Classified By |
| 47 | Classification Date |
| 48 | Last Review Date |
| 49 | Regulation |
| 50 | Applicability |
| 51 | Data Categories in Scope |
| 52 | Field Count |
| 53 | Masking Mandated? |
| 54 | GDPR Applicable? |
| 55 | GDPR Article |
| 56 | FADP Applicable? |
| 57 | HIPAA Applicable? |
| 58 | PCI-DSS Applicable? |
| 59 | Other Regulations |
| 60 | Masking Mandated by Reg? |
| 61 | Regulatory Reference |
| 62 | Compliance Deadline |
| 63 | Notes |
| 64 | Data Owner (Role) |
| 65 | Data Owner (Name) |
| 66 | Backup Owner |
| 67 | Assignment Date |
| 68 | Last Review |
| 69 | System Owner |
| 70 | Data Steward |
| 71 | Business Owner |
| 72 | Data Categories in System |
| 73 | Ownership Documented? |
| 74 | RACI Matrix Reference |
| 75 | Approval Status |
| 76 | Approver |
| 77 | Sensitivity Score (1-5) |
| 78 | Exposure Risk (1-5) |
| 79 | Regulatory Score (1-5) |
| 80 | Volume Score (1-5) |
| 81 | Total Priority Score |
| 82 | Priority Tier |
| 83 | Target Implementation Date |
| 84 | Assigned To |
| 85 | Implementation Status |
| 86 | Blocking Issues |
| 87 | Count |
| 88 | % of Total |
| 89 | Avg Score |
| 90 | Complete |
| 91 | In Progress |
| 92 | Not Started |
| 93 | Gap Category |
| 94 | Risk Level |
| 95 | Remediation Owner |
| 96 | Target Date |
| 97 | Gap ID |
| 98 | Field/Data Element |
| 99 | Gap Description |
| 100 | Impact if Not Remediated |
| 101 | Root Cause |
| 102 | Remediation Action |
| 103 | Target Completion Date |
| 104 | Status |
| 105 | Actual Completion Date |
| 106 | Verification Method |
| 107 | =SUM(B6:B10) |
| 108 | =SUM(C6:C10) |
| 109 | =SUM(D6:D10) |
| 110 | =SUM(E6:E10) |
| 111 | =SUM(F6:F10) |
| 112 | SYSTEM & DATABASE INVENTORY |
| 113 | SENSITIVE DATA CATEGORY REFERENCE |
| 114 | SENSITIVE DATA ELEMENT INVENTORY |
| 115 | DATA CLASSIFICATION MATRIX |
| 116 | REGULATORY REQUIREMENT MAPPING |
| 117 | DATA OWNERSHIP ASSIGNMENT |
| 118 | MASKING PRIORITY & RISK ASSESSMENT |
| 119 | DATA INVENTORY & CLASSIFICATION GAP ANALYSIS |
| 120 | Evidence ID |
| 121 | Category |
| 122 | Source/Location |
| 123 | Date Collected |
| 124 | Collected By |
| 125 | Assessment Area |
| 126 | Total Items |
| 127 | Compliant |
| 128 | Partial |
| 129 | Non-Compliant |
| 130 | N/A |
| 131 | Compliance % |
| 132 | Finding |
| 133 | Impact |
| 134 | Recommendation |
| 135 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Unknown, Partial, Planned, N/A, Conditional, \u2705 Complete
\u26A0\uFE0F Partial, \u274C Missing, \u1F4CB Planned, Database, Application
SaaS, File Share, API, Data Warehouse, Backup System, Archive, Other
Production, Development, Test/QA, UAT, Training, Analytics, DR/Backup
Decommissioned, On-Premises, AWS, Azure, GCP, Multi-Cloud, Hybrid
Third-Party Hosted, String, Integer, Date, Boolean, Binary, JSON, CAT-PII-D
CAT-PII-I, CAT-FIN, CAT-HLT, CAT-CRD, CAT-PRP, CAT-LOC, CAT-BIO, CAT-GEN
CAT-CHD, Name, SSN, Email, Phone, Address, DOB, PAN, Medical Record, Password
IP Address, Critical, High, Medium, Low, Public, Masked, Not Masked
Partially Masked, Encrypted, Automated Scan, Schema Review, Manual Sample
Data Owner Interview, Restricted, Confidential, Internal, Art. 4 (PII)
Art. 9 (Special), Art. 32 (Security), Very High, Very Low, P1, P2, P3, P4
Not Started, In Progress, Complete, Blocked, Inventory Missing
Classification Missing, Ownership Missing, Masking Missing, Regulatory Unknown
Open, Accepted Risk, Data Discovery Report, Schema Documentation, DPIA
Data Flow Diagram, Classification Review, RACI Matrix, Meeting Minutes
Approval Email, Tool Report, Annual, Semi-Annual, Quarterly, As-Needed
Verified, Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Not Approved, Deferred
```

**Extracted:** 12 sheets, 135 columns, 122 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Data is a precious thing and will last longer than the systems themselves."*
— Tim Berners-Lee

<!-- QA_VERIFIED: 2026-02-06 -->
