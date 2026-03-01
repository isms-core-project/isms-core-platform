<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.4-TG:framework:TG:a.8.15.4 -->
**ISMS-IMP-A.8.15.4-TG - Log Analysis & Review Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Log Analysis & Review Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.15.4-TG |
| **Related Policy** | ISMS-POL-A.8.15 (Logging) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.15 (Logging) |
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

- ISMS-POL-A.8.15 (Logging)
- ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)
- ISMS-IMP-A.8.15.2 (Log Collection & Centralization Assessment)
- ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a815_4_log_analysis_review.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.15.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Log Review Schedule |
| 3 | Alert Management |
| 4 | Investigation Workflow |
| 5 | Analysis Tools & Capabilities |
| 6 | Review Findings |
| 7 | Continuous Monitoring |
| 8 | Performance Metrics |
| 9 | Gap Analysis |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

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
| 1 | Review ID |
| 2 | Review Type |
| 3 | Log Source / Scope |
| 4 | Frequency |
| 5 | Responsible Party |
| 6 | Review Procedure |
| 7 | Last Review Date |
| 8 | Next Review Due |
| 9 | Status |
| 10 | Days Overdue |
| 11 | Completion Rate % |
| 12 | Findings (Last Review) |
| 13 | Actions Taken |
| 14 | Notes |
| 15 | Alert ID |
| 16 | Alert Name |
| 17 | Alert Type |
| 18 | Severity |
| 19 | MITRE ATT&CK Tactic |
| 20 | Detection Logic |
| 21 | Threshold |
| 22 | Alerts/Month |
| 23 | True Positives |
| 24 | False Positives |
| 25 | True Positive Rate % |
| 26 | Tuning Required |
| 27 | Playbook Exists |
| 28 | Last Tuned |
| 29 | Incident ID |
| 30 | Detection Date |
| 31 | Alert Source |
| 32 | Incident Type |
| 33 | Assigned To |
| 34 | MTTD (hours) |
| 35 | MTTR (hours) |
| 36 | Root Cause |
| 37 | Lessons Learned |
| 38 | Tool / Capability |
| 39 | Category |
| 40 | Vendor / Product |
| 41 | Version |
| 42 | Purpose |
| 43 | Users Trained |
| 44 | Usage Frequency |
| 45 | Effectiveness |
| 46 | Integration with SIEM |
| 47 | Last Updated |
| 48 | Finding ID |
| 49 | Review Date |
| 50 | Log Source |
| 51 | Finding Description |
| 52 | Action Required |
| 53 | Due Date |
| 54 | Metric Date |
| 55 | Total Events/Day |
| 56 | Security Alerts Generated |
| 57 | Alerts Investigated |
| 58 | Avg MTTD (hours) |
| 59 | Avg MTTR (hours) |
| 60 | Critical Incidents |
| 61 | Review Completion % |
| 62 | Gap ID |
| 63 | Gap Category |
| 64 | Description |
| 65 | Impact |
| 66 | Policy Requirement |
| 67 | Priority |
| 68 | Remediation Action |
| 69 | Owner |
| 70 | Target Date |
| 71 | Budget Required |
| 72 | Evidence ID |
| 73 | Assessment Area |
| 74 | Evidence Type |
| 75 | Location/Path |
| 76 | Date Collected |
| 77 | Collected By |
| 78 | Verification Status |
| 79 | Total Items |
| 80 | Compliant |
| 81 | Partial |
| 82 | Non-Compliant |
| 83 | N/A |
| 84 | Compliance % |
| 85 | Metric |
| 86 | Value |
| 87 | Target |
| 88 | Finding Type |
| 89 | Risk Level |
| 90 | Associated Sheet |
| 91 | Recommended Action |
| 92 | ISO Clause |

### Data Validation Values

All dropdown/list values used across sheets:

```
Security Event Review, Compliance Review, Administrative Review, Access Review
Error Review, Performance Review, Real-time, Hourly, Daily, Weekly, Monthly
Quarterly, Annual, Ad-hoc, On Schedule, Overdue, Completed, Deferred
Authentication, Authorisation, Malware, Network, Data Exfiltration
Lateral Movement, Privilege Escalation, Reconnaissance, Other, Critical, High
Medium, Low, Informational, Yes, No, Active, Disabled, Testing, Deprecated
Brute Force Attack, Unauthorised Access, DDoS, Phishing, Insider Threat
Configuration Error, New, Investigating, Contained, Resolved, False Positive
SIEM Platform, Log Analysis, Threat Intelligence, Forensics, Visualisation
Automation, As Needed, Rarely, Unknown, Native, API, Manual Export
No Integration, Production, Planned, Policy Violation, Security Event
Performance Issue, Compliance Issue, In Progress, Alert Tuning, Review Process
Tools/Capabilities, Staffing, Training, Documentation, Open, Screenshot
Configuration File, Log Export, Report, Policy Document, SOC Procedure
Meeting Notes, Training Record, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected
```

**Extracted:** 12 sheets, 92 columns, 95 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"We can only see a short distance ahead, but we can see plenty there that needs to be done."*
- Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
