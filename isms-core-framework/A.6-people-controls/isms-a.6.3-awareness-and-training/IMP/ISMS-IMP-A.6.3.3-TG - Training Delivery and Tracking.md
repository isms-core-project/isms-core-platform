<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.3.3-TG:framework:TG:a.6.3.3 -->
**ISMS-IMP-A.6.3.3-TG - Training Delivery and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Training Delivery and Tracking |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.3.3-TG |
| **Related Policy** | ISMS-POL-A.6.3 (Awareness and Training) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.3 (Information Security Awareness, Education and Training) |
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

- ISMS-POL-A.6.3 (Awareness and Training)
- ISMS-IMP-A.6.3.1 (Training Needs Assessment)
- ISMS-IMP-A.6.3.2 (Training Program Design)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a63_3_training_delivery_tracking.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.3.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Personnel Register |
| 3 | Completion Tracking |
| 4 | Assessment Results |
| 5 | Simulation Results |
| 6 | Remediation Tracking |
| 7 | Compliance Summary |
| 8 | Overdue Alerts |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
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
| 1 | Personnel Register |
| 2 | Training Completion |
| 3 | Assessment Results |
| 4 | Employee ID |
| 5 | Full Name |
| 6 | Department |
| 7 | Role Title |
| 8 | Training Tier |
| 9 | Employment Type |
| 10 | Start Date |
| 11 | Status |
| 12 | Manager |
| 13 | Email |
| 14 | Record ID |
| 15 | Employee Name |
| 16 | Module ID |
| 17 | Module Title |
| 18 | Assigned Date |
| 19 | Due Date |
| 20 | Completion Date |
| 21 | Days Overdue |
| 22 | Assessment Score |
| 23 | Pass Fail |
| 24 | Attempts |
| 25 | Certificate ID |
| 26 | Notes |
| 27 | Assessment ID |
| 28 | Assessment Type |
| 29 | Date Taken |
| 30 | Score |
| 31 | Pass Threshold |
| 32 | Attempt Number |
| 33 | Time Taken |
| 34 | Questions Correct |
| 35 | Questions Total |
| 36 | Feedback Provided |
| 37 | Remediation Required |
| 38 | Campaign ID |
| 39 | Campaign Name |
| 40 | Campaign Date |
| 41 | Email Sent |
| 42 | Email Opened |
| 43 | Link Clicked |
| 44 | Credentials Submitted |
| 45 | Reported Suspicious |
| 46 | Time To Click |
| 47 | Time To Report |
| 48 | Remediation Assigned |
| 49 | Remediation Completed |
| 50 | Remediation ID |
| 51 | Trigger Event |
| 52 | Trigger Date |
| 53 | Remediation Level |
| 54 | Remediation Training |
| 55 | Outcome |
| 56 | Manager Notified |
| 57 | HR Notified |
| 58 | Total Personnel |
| 59 | Training Required |
| 60 | Completed |
| 61 | Completion Rate |
| 62 | On Time Rate |
| 63 | Average Score |
| 64 | Overdue Count |
| 65 | Compliance Status |
| 66 | Escalation Level |
| 67 | Last Reminder Sent |
| 68 | Action Required |
| 69 | Evidence ID |
| 70 | Evidence Type |
| 71 | Description |
| 72 | Location / Source |
| 73 | Date Collected |
| 74 | Collected By |
| 75 | Assessment Area |
| 76 | Count |
| 77 | Compliant |
| 78 | Partial |
| 79 | Non-Compliant |
| 80 | N/A |
| 81 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7, Full-Time, Part-Time
Contractor, Consultant, Intern, Active, On Leave, Terminated, Completed
In Progress, Overdue, Not Started, Pass, Fail, N/A, Quiz, Practical
Simulation, Scenario, Tabletop, Yes, No, Failed Assessment, Clicked Phishing
Submitted Credentials, Pattern Failure, Level 1, Level 2, Level 3, Passed
Failed, Escalated, Level 1 (1-7 days), Level 2 (8-14 days)
Level 3 (15-30 days), Level 4 (>30 days), Verified, Pending, Requires update
Not available, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 81 columns, 55 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"I have found a very great number of exceedingly beautiful theorems."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-03-01 -->
