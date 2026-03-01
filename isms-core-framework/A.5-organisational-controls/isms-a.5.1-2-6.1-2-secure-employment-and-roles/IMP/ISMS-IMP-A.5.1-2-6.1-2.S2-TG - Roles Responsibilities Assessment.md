<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S2-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S2-TG - Roles & Responsibilities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.2: Information Security Roles and Responsibilities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Roles Responsibilities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S2-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.2 (Information Security Roles and Responsibilities) |
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

- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles)
- ISMS-IMP-A.5.1-2-6.1-2.S1 (Policy Framework Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening Vetting Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S4 (Employment Contract Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5_1_2_6_1_2_s2_roles_responsibilities.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.1-2-6.1-2.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Summary Dashboard |
| 2 | Role Inventory |
| 3 | Role Definition Assessment |
| 4 | RACI Matrix Assessment |
| 5 | Role Assignment Verification |
| 6 | Training Assessment |
| 7 | Access Alignment Review |
| 8 | Gap Analysis |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |
| 11 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Role ID |
| 2 | Role Title |
| 3 | Role Category |
| 4 | Role Type |
| 5 | Department |
| 6 | Reports To |
| 7 | Security Clearance Required |
| 8 | ISO Control Mapping |
| 9 | Role Created Date |
| 10 | Last Review Date |
| 11 | Role Status |
| 12 | Criticality |
| 13 | Backup Required |
| 14 | Backup Role ID |
| 15 | Role Description |
| 16 | Notes |
| 17 | Responsibilities Documented |
| 18 | Authority Level Defined |
| 19 | Reporting Lines Clear |
| 20 | Competency Requirements |
| 21 | Training Requirements |
| 22 | Access Requirements |
| 23 | Accountability Defined |
| 24 | Segregation of Duties |
| 25 | Definition Documentation |
| 26 | Definition Compliance Rating |
| 27 | Gap Description |
| 28 | Evidence Reference |
| 29 | Activity ID |
| 30 | Security Activity |
| 31 | Activity Category |
| 32 | Responsible Role |
| 33 | Accountable Role |
| 34 | Consulted Roles |
| 35 | Informed Roles |
| 36 | Responsible Assigned |
| 37 | Accountable Assigned |
| 38 | Multiple Accountables |
| 39 | RACI Documented |
| 40 | RACI Score |
| 41 | RACI Status |
| 42 | RACI Conflict |
| 43 | Current Holder Name |
| 44 | Current Holder Employee ID |
| 45 | Assignment Date |
| 46 | Assignment Documentation |
| 47 | Formal Acceptance |
| 48 | Background Check Status |
| 49 | Assignment Status |
| 50 | Backup Holder Name |
| 51 | Backup Assignment Status |
| 52 | Last Verification Date |
| 53 | Role Holder Name |
| 54 | Required Training 1 |
| 55 | Training 1 Status |
| 56 | Training 1 Date |
| 57 | Required Training 2 |
| 58 | Training 2 Status |
| 59 | Training 2 Date |
| 60 | Required Training 3 |
| 61 | Training 3 Status |
| 62 | Training Expiry Status |
| 63 | Training Records Available |
| 64 | Training Compliance Rating |
| 65 | Defined Access Level |
| 66 | Actual Access Level |
| 67 | Systems Access Defined |
| 68 | Systems Access Actual |
| 69 | Excess Privileges |
| 70 | Missing Access |
| 71 | Access Review Date |
| 72 | SoD Conflict |
| 73 | Access Documentation |
| 74 | Access Alignment Status |
| 75 | Gap ID |
| 76 | Gap Category |
| 77 | Risk Level |
| 78 | Impact Assessment |
| 79 | Affected Stakeholders |
| 80 | Remediation Action |
| 81 | Responsible Party |
| 82 | Target Completion Date |
| 83 | Estimated Effort |
| 84 | Dependencies |
| 85 | Status |
| 86 | Completion Evidence |
| 87 | Risk Acceptance |

### Data Validation Values

All dropdown/list values used across sheets:

```
Active, Archived, Superseded, Pending Review, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 87 columns, 12 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The price of greatness is responsibility."*
— Winston Churchill

<!-- QA_VERIFIED: 2026-02-06 -->
