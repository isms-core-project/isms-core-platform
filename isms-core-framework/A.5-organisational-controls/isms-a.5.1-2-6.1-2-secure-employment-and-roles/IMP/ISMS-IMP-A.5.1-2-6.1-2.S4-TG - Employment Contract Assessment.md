<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.1-2-6.1-2.S4-TG:framework:TG:a.5.1-2-6.1-2 -->
**ISMS-IMP-A.5.1-2-6.1-2.S4-TG - Employment Contract Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.2: Terms and Conditions of Employment

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Employment Contract Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.1-2-6.1-2.S4-TG |
| **Related Policy** | ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.2 (Terms and Conditions of Employment) |
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
- ISMS-IMP-A.5.1-2-6.1-2.S2 (Roles Responsibilities Assessment)
- ISMS-IMP-A.5.1-2-6.1-2.S3 (Screening Vetting Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a5_1_2_6_1_2_s4_employment_contract.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.1-2-6.1-2.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Summary Dashboard |
| 2 | Contract Template Assessment |
| 3 | Required Clause Registry |
| 4 | Personnel Contract Compliance |
| 5 | Confidentiality NDA Tracking |
| 6 | Post Employment Obligations |
| 7 | Contractor Agreement Assessment |
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
| 1 | Template ID |
| 2 | Template Name |
| 3 | Template Type |
| 4 | Personnel Category |
| 5 | Current Version |
| 6 | Version Date |
| 7 | Last Review Date |
| 8 | Next Review Date |
| 9 | Security Clauses Count |
| 10 | Required Clauses Met |
| 11 | Legal Review Date |
| 12 | Legal Approved |
| 13 | Compliance Status |
| 14 | Notes |
| 15 | Clause ID |
| 16 | Clause Category |
| 17 | Clause Title |
| 18 | Clause Description |
| 19 | ISO 27001 Reference |
| 20 | Legal Requirement |
| 21 | Mandatory For |
| 22 | Coverage Status |
| 23 | Templates With Clause |
| 24 | Gap If Missing |
| 25 | Last Verified |
| 26 | Employee ID |
| 27 | Employee Name |
| 28 | Department |
| 29 | Role Title |
| 30 | Employment Type |
| 31 | Start Date |
| 32 | Contract Template Used |
| 33 | Contract Signed |
| 34 | Contract Date |
| 35 | Contract On File |
| 36 | All Clauses Present |
| 37 | Screening Complete |
| 38 | Background Check Date |
| 39 | NDA Type |
| 40 | NDA Version |
| 41 | Date Signed |
| 42 | Expiration Date |
| 43 | Covers IP |
| 44 | Covers Trade Secrets |
| 45 | Covers Post Employment |
| 46 | NDA Status |
| 47 | Renewal Required |
| 48 | Document Location |
| 49 | Former Employee ID |
| 50 | Former Employee Name |
| 51 | Former Department |
| 52 | Former Role |
| 53 | Termination Date |
| 54 | Termination Type |
| 55 | Confidentiality End Date |
| 56 | Non Compete End Date |
| 57 | Non Solicit End Date |
| 58 | IP Assignment Perpetual |
| 59 | Assets Returned |
| 60 | Exit Interview Complete |
| 61 | Obligation Status |
| 62 | Monitoring Required |
| 63 | Contractor ID |
| 64 | Contractor Name |
| 65 | Company Name |
| 66 | Contract Type |
| 67 | Services Provided |
| 68 | Contract Start |
| 69 | Contract End |
| 70 | NDA In Place |
| 71 | Security Clauses Present |
| 72 | Data Access Level |
| 73 | Background Check |
| 74 | Sponsor Manager |
| 75 | Gap ID |
| 76 | Source Sheet |
| 77 | Affected Entity |
| 78 | Gap Category |
| 79 | Gap Description |
| 80 | Risk Level |
| 81 | Impact Assessment |
| 82 | Affected Personnel Count |
| 83 | Remediation Action |
| 84 | Responsible Party |
| 85 | Target Completion Date |
| 86 | Estimated Effort |
| 87 | Dependencies |
| 88 | Status |
| 89 | Completion Evidence |
| 90 | Risk Acceptance |

### Data Validation Values

All dropdown/list values used across sheets:

```
Active, Archived, Superseded, Pending Review, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 90 columns, 12 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

<!-- QA_VERIFIED: 2026-02-06 -->
