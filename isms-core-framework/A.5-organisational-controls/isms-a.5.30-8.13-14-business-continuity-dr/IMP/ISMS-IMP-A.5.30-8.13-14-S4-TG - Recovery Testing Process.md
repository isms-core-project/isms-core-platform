<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.30-8.13-14-S4-TG:framework:TG:a.5.30-8.13-14-s4 -->
**ISMS-IMP-A.5.30-8.13-14-S4-TG - Recovery Testing Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Recovery Testing Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S4-TG |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14-S4 (Business Continuity Dr) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.13 (Information Backup) |
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

- ISMS-POL-A.5.30-8.13-14-S4 (Business Continuity Dr)
- ISMS-IMP-A.5.30-8.13-14-S1 (BIA and RPO:RTO Process)
- ISMS-IMP-A.5.30-8.13-14-S2 (Backup Implementation)
- ISMS-IMP-A.5.30-8.13-14-S3 (Redundancy Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a530_4_testing_results.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.30.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Summary Dashboard |
| 2 | Test Schedule |
| 3 | Test Results Log |
| 4 | Issue Remediation |
| 5 | Testing Compliance |
| 6 | Evidence Register |
| 7 | Approval Sign-Off |
| 8 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
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
| 1 | Test ID |
| 2 | System Name |
| 3 | Test Type |
| 4 | Criticality |
| 5 | Required Frequency |
| 6 | Scheduled Date |
| 7 | Test Owner |
| 8 | Notes / Prerequisites |
| 9 | Result ID |
| 10 | Test ID (Schedule) |
| 11 | Test Date |
| 12 | Result |
| 13 | Actual Duration (hrs) |
| 14 | Tested By |
| 15 | Issues Found |
| 16 | Detailed Notes |
| 17 | Issue ID |
| 18 | Related Test (Result ID) |
| 19 | Issue Description |
| 20 | Root Cause |
| 21 | Severity |
| 22 | Status |
| 23 | Remediation Plan |
| 24 | Target Resolution Date |
| 25 | Last Test Date |
| 26 | Days Since Last Test |
| 27 | Compliance Status |
| 28 | Next Test Due |
| 29 | Evidence ID |
| 30 | Evidence Type |
| 31 | Description |
| 32 | Related Sheet / Row |
| 33 | Location / Path |
| 34 | Date Collected |
| 35 | Collected By |
| 36 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Backup Restore, Failover Test, Full DR Scenario, Tabletop Exercise
Component Test, Integration Test, Tier 1 - Critical, Tier 2 - Important
Tier 3 - Standard, Tier 4 - Low, Quarterly, Semi-Annual, Annual, Ad-Hoc
Not Required, [!] Critical, [~] High, [.] Medium, [ ] Low, Test Report
Screenshot, Log File, Video Recording, Configuration File, Runbook
Issue Ticket, Sign-Off, Other, Draft, Under Review, Final
Requires Remediation, Approved, Approved with Conditions, Rejected
Requires Rework, Approve, Approve with Conditions, Reject, Require Rework
Re-assessment required, Deferred
```

**Extracted:** 8 sheets, 36 columns, 42 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Strive not to be a success, but rather to be of value."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
