<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.7-8.S4-TG:framework:TG:a.6.7-8 -->
**ISMS-IMP-A.6.7-8.S4-TG - Event Reporting Mechanisms Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Event Reporting Mechanisms Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.7-8.S4-TG |
| **Related Policy** | ISMS-POL-A.6.7-8 (Remote Working and Reporting) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting) |
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

- ISMS-POL-A.6.7-8 (Remote Working and Reporting)
- ISMS-IMP-A.6.7-8.S1 (Remote Work Authorisation Assessment)
- ISMS-IMP-A.6.7-8.S2 (Technical Controls Assessment)
- ISMS-IMP-A.6.7-8.S3 (Endpoint and Physical Security Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a678_s4_event_reporting_mechanisms.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.7-8.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Channel Assessment |
| 3 | Channel Availability |
| 4 | Event Categories |
| 5 | Response Timeframes |
| 6 | Non-Blame Culture |
| 7 | Awareness Training |
| 8 | Sample Events |
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
| 1 | Channel |
| 2 | Description |
| 3 | Requirement |
| 4 | Availability |
| 5 | Implemented |
| 6 | Contact Info |
| 7 | Remote Access |
| 8 | Evidence |
| 9 | Notes |
| 10 | Test Date |
| 11 | Test Type |
| 12 | Business Hours |
| 13 | After Hours |
| 14 | Weekend |
| 15 | Result |
| 16 | Next Test |
| 17 | Category |
| 18 | Documented |
| 19 | Examples Provided |
| 20 | In Training |
| 21 | Personnel Aware |
| 22 | Reports Received |
| 23 | Response Type |
| 24 | SLA |
| 25 | Measured |
| 26 | Compliance Rate |
| 27 | Verification Method |
| 28 | Last Reviewed |
| 29 | Principle |
| 30 | Communicated |
| 31 | Training |
| 32 | Effectiveness Measure |
| 33 | Training Element |
| 34 | Included in Training |
| 35 | Last Updated |
| 36 | Completion Rate |
| 37 | Effectiveness Measured |
| 38 | Event ID |
| 39 | Date Reported |
| 40 | Channel Used |
| 41 | Acknowledged |
| 42 | Ack Time |
| 43 | Resolution Time |
| 44 | Escalated |
| 45 | Gap ID |
| 46 | Area |
| 47 | Impact |
| 48 | Risk |
| 49 | Remediation |
| 50 | Owner |
| 51 | Target |
| 52 | Status |
| 53 | Evidence ID |
| 54 | Evidence Type |
| 55 | Source / Owner |
| 56 | Date Collected |
| 57 | Retention Period |
| 58 | Storage Location |
| 59 | Assessment Area |
| 60 | Total Items |
| 61 | Compliant |
| 62 | Partial |
| 63 | Non-Compliant |
| 64 | N/A |
| 65 | Compliance % |
| 66 | Finding |
| 67 | Count |
| 68 | Severity |
| 69 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Pass, Fail, Available, Unavailable, Not Tested, Channels
Categories, Response, Culture, Training, Critical, High, Medium, Low, Open
In Progress, Resolved, Accepted, Collected, Pending, Not Available, Superseded
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 69 columns, 33 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The first step toward security is recognizing that there's a problem."*
— Security Maxim

<!-- QA_VERIFIED: 2026-03-01 -->
