<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.10.1-TG:framework:TG:a.8.10.1 -->
**ISMS-IMP-A.8.10.1-TG - Retention & Deletion Triggers Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Retention Deletion Triggers |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.10.1-TG |
| **Related Policy** | ISMS-POL-A.8.10 (Data Deletion) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.10 (Information Deletion) |
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

- ISMS-POL-A.8.10 (Data Deletion)
- ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)
- ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)
- ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a810_1_retention_triggers.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.10.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Data Category Registry |
| 3 | 3. Retention Sched. Compliance |
| 4 | 4. Deletion Trigger Config. |
| 5 | 5. Legal Hold Management |
| 6 | 6. Data Subject Requests |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #9C5700 | Custom |
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
| 1 | Data Category / System Name |
| 2 | Data Classification |
| 3 | Business Owner |
| 4 | Retention Period |
| 5 | Legal/Regulatory Basis |
| 6 | Status |
| 7 | Implementation Date |
| 8 | Last Review Date |
| 9 | Next Review Date |
| 10 | Gap Identified |
| 11 | Remediation Plan |
| 12 | Target Completion |
| 13 | Risk Level |
| 14 | Evidence Reference |
| 15 | Notes / Comments |
| 16 | Remediation Owner |
| 17 | Budget Required |
| 18 | Primary Storage Location |
| 19 | Volume/Records |
| 20 | Contains PII/SPI |
| 21 | Retention Calculation Method |
| 22 | Event Trigger Description |
| 23 | Backup Retention Aligned |
| 24 | Trigger Type |
| 25 | Trigger Frequency |
| 26 | Legal Hold Check Integrated |
| 27 | Active Legal Holds |
| 28 | Legal Hold Notification Process |
| 29 | Hold Review Frequency |
| 30 | Average Response Time (Days) |
| 31 | GDPR/FADP Applicable |
| 32 | Request Volume (Last 12 Months) |
| 33 | EXCEPTIONS / DEVIATIONS |
| 34 | Evidence ID |
| 35 | Category |
| 36 | Description |
| 37 | Source Document |
| 38 | Date Collected |
| 39 | Collected By |
| 40 | Notes |
| 41 | Assessment Area |
| 42 | Total Items |
| 43 | Compliant |
| 44 | Partial |
| 45 | Non-Compliant |
| 46 | N/A |
| 47 | Compliance % |
| 48 | Finding |
| 49 | Impact |
| 50 | Recommendation |
| 51 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Public, Internal, Confidential, Restricted, 30 days, 60 days, 90 days
6 months, 1 year, 2 years, 3 years, 5 years, 7 years, 10 years, Permanent
Until Event Occurs, Other (specify in notes), Swiss FADP, EU GDPR
Swiss Code of Obligations (OR), Swiss Tax Law, EU ePrivacy Directive
Industry Standard (specify), Contractual Obligation, Legitimate Interest
Consent, Legal Obligation, Multiple Bases (specify), Critical, High, Medium
Low, Yes, No, Unknown, On-Premise, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS)
Hybrid, Third-Party, Yes - PII, Yes - SPI, Yes - Both, Fixed Period
Event-Based, Partial, N/A, Automatic, Manual, Semi-Automatic, Real-time, Daily
Weekly, Monthly, Quarterly, Annual, Ad-hoc, Yes - Automated, Yes - Manual
Automated, None, GDPR Only, FADP Only, Both, Neither, Verified
Pending verification, Not verified, Requires update, Policy Document
Procedure Document, Screenshot, System Log Export, Configuration File
Email Communication, Meeting Minutes, Audit Report, Certificate
Contract/Agreement, Training Record, Test Result, Other, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 51 columns, 91 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"Data not deleted is data at risk."*
— Information security principle

<!-- QA_VERIFIED: 2026-03-01 -->
