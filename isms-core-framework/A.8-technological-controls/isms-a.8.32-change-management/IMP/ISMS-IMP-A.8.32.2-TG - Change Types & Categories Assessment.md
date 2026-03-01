<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.2-TG:framework:TG:a.8.32.2 -->
**ISMS-IMP-A.8.32.2-TG - Change Types & Categories Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Change Types & Categories Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.32.2-TG |
| **Related Policy** | ISMS-POL-A.8.32 (Change Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.32 (Change Management) |
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

- ISMS-POL-A.8.32 (Change Management)
- ISMS-IMP-A.8.32.1 (Change Process Assessment)
- ISMS-IMP-A.8.32.3 (Environment Separation Assessment)
- ISMS-IMP-A.8.32.4 (Testing & Validation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a832_2_change_types.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.32.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Standard Changes Catalog |
| 3 | Normal Change Classification |
| 4 | Emergency Change Procedures |
| 5 | Risk Assessment Matrix |
| 6 | Change Calendar Management |
| 7 | Classification Metrics |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Change ID |
| 2 | Change Title |
| 3 | Description |
| 4 | Category |
| 5 | Frequency |
| 6 | Pre-requisites |
| 7 | Procedure Location |
| 8 | Owner |
| 9 | Approval Date |
| 10 | Review Date |
| 11 | Risk Level |
| 12 | Status |
| 13 | Evidence |
| 14 | Metric |
| 15 | Value |
| 16 | Notes |
| 17 | Criterion |
| 18 | Defined |
| 19 | Documentation Reference |
| 20 | Assessment Method |
| 21 | Responsible Role |
| 22 | Compliance |
| 23 | Risk Category |
| 24 | Impact Category |
| 25 | Approval Authority |
| 26 | CAB Review |
| 27 | Typical Timeline |
| 28 | Success Rate |
| 29 | Documented |
| 30 | Emergency Criterion |
| 31 | Specific Triggers |
| 32 | Escalation Path |
| 33 | Response Time SLA |
| 34 | Requirement |
| 35 | Implemented |
| 36 | Process Description |
| 37 | Exceptions Allowed |
| 38 | Target |
| 39 | Current (Last Quarter) |
| 40 | Impact Level |
| 41 | User Count Affected |
| 42 | Service Downtime Potential |
| 43 | Recovery Time |
| 44 | Data Loss Risk |
| 45 | Financial Impact |
| 46 | Likelihood Level |
| 47 | Failure Probability |
| 48 | Complexity |
| 49 | Dependencies |
| 50 | Testing Maturity |
| 51 | Historical Success Rate |
| 52 | Change Window |
| 53 | Days/Times |
| 54 | Applicable Change Types |
| 55 | Approval Required |
| 56 | Advance Notice |
| 57 | Blackout Period |
| 58 | Start Date |
| 59 | End Date |
| 60 | Reason |
| 61 | Affected Systems/Services |
| 62 | Exception Approver |
| 63 | Current |
| 64 | Period |
| 65 | Trend |
| 66 | Total Changes |
| 67 | Correctly Classified |
| 68 | Misclassified |
| 69 | Accuracy % |
| 70 | Reviewer |
| 71 | Assessment Area |
| 72 | Total Items |
| 73 | Compliant |
| 74 | Partial |
| 75 | Non-Compliant |
| 76 | N/A |
| 77 | Compliance % |
| 78 | Finding |
| 79 | Count |
| 80 | Severity |
| 81 | Action Required |
| 82 | Evidence ID |
| 83 | Evidence Type |
| 84 | Location / Path |
| 85 | Date Collected |
| 86 | Collected By |
| 87 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Infrastructure, Application, Security, Data, Network, Cloud
User Access, Configuration, Other, Daily, Weekly, Monthly, Quarterly, Annual
On-Demand, Rare, Low, Medium, High, Critical, Mandatory, Recommended, Optional
Not Required, Change Manager, CAB, Service Owner, CISO, CIO, Multiple Required
<10 users, 10-50, 50-100, 100-1000, >1000 users, All users, Business-critical
<15 min, 15-60 min, 1-2 hours, 2-8 hours, >8 hours, Irreversible, None
Minimal, Moderate, Simple, Complex, Very Complex, Extensively Tested
Well Tested, Limited Testing, Untested, Conference Call, Video, IM Group
Emergency Hotline, All, Standard Only, Normal Only, Emergency Only, Custom
Financial Close, Holiday Period, Peak Business, Audit, Automated, Manual
Change Request, Policy Document, Process Record, System Screenshot
Configuration Export, Audit Log, Training Record, Test Result, Risk Assessment
Meeting Minutes, To Be Determined, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 87 columns, 90 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Cryptography is a mix of math, computer science, and paranoia."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
