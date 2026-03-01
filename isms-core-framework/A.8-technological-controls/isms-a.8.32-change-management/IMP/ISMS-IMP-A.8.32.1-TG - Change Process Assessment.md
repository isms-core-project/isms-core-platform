<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.1-TG:framework:TG:a.8.32.1 -->
**ISMS-IMP-A.8.32.1-TG - Change Process Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Change Process Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.32.1-TG |
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
- ISMS-IMP-A.8.32.2 (Change Types & Categories Assessment)
- ISMS-IMP-A.8.32.3 (Environment Separation Assessment)
- ISMS-IMP-A.8.32.4 (Testing & Validation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a832_1_change_process.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.32.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Change Process Workflow |
| 3 | Approval Authority Matrix |
| 4 | CAB Operations |
| 5 | Communication |
| 6 | Documentation Records |
| 7 | Tool Capabilities |
| 8 | Metrics KPIs |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

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
| 1 | Stage |
| 2 | Stage Name |
| 3 | Description |
| 4 | Process Owner |
| 5 | Standard Duration |
| 6 | Tool/System Used |
| 7 | Status |
| 8 | Evidence |
| 9 | Requirement |
| 10 | Implemented |
| 11 | Documentation Type |
| 12 | Template Available |
| 13 | Location |
| 14 | Responsible Role |
| 15 | Capability |
| 16 | Automated |
| 17 | Semi-Automated |
| 18 | Manual |
| 19 | Tool/System |
| 20 | Notes |
| 21 | Standard Change Type |
| 22 | Pre-Approved |
| 23 | Self-Service Allowed |
| 24 | Approver (if required) |
| 25 | Approval SLA |
| 26 | Risk Level |
| 27 | Impact Level |
| 28 | Required Approvers |
| 29 | CAB Review Required |
| 30 | Approval Threshold |
| 31 | Typical SLA |
| 32 | Emergency Criteria |
| 33 | E-CAB Members |
| 34 | Minimum Approvers |
| 35 | Approval Method |
| 36 | Documented |
| 37 | Metric |
| 38 | Target |
| 39 | Current |
| 40 | Role |
| 41 | Name |
| 42 | Department |
| 43 | Authority Level |
| 44 | Mandatory/Optional |
| 45 | Delegate |
| 46 | Contact |
| 47 | Meeting Type |
| 48 | Frequency |
| 49 | Day/Time |
| 50 | Duration |
| 51 | Quorum Required |
| 52 | Minutes Owner |
| 53 | Agenda Deadline |
| 54 | Responsibility |
| 55 | Owner |
| 56 | Documented? |
| 57 | Evidence Reference |
| 58 | Stakeholder Group |
| 59 | Role/Description |
| 60 | Notification Trigger |
| 61 | Communication Method |
| 62 | Responsible Party |
| 63 | Template Type |
| 64 | Purpose |
| 65 | Content Includes |
| 66 | Approval Required |
| 67 | Format |
| 68 | Maintained |
| 69 | Channel |
| 70 | Available |
| 71 | Primary Use |
| 72 | Audience Reach |
| 73 | Reliability |
| 74 | Documentation Item |
| 75 | Required |
| 76 | Retention Period |
| 77 | Storage Location |
| 78 | Compliant |
| 79 | Special Requirements |
| 80 | Record Type |
| 81 | Disposal Method |
| 82 | Regulatory Requirement |
| 83 | Integration with Primary |
| 84 | User Count |
| 85 | Integration Point |
| 86 | Source System |
| 87 | Target System |
| 88 | Integration Type |
| 89 | Data Exchanged |
| 90 | Security Control |
| 91 | Details |
| 92 | Metric Name |
| 93 | Current Value |
| 94 | Data Source |
| 95 | Report Name |
| 96 | Audience |
| 97 | Delivery Method |
| 98 | Assessment Area |
| 99 | Total Items |
| 100 | Partial |
| 101 | Non-Compliant |
| 102 | N/A |
| 103 | Compliance % |
| 104 | Value |
| 105 | Category |
| 106 | Finding |
| 107 | Count |
| 108 | Severity |
| 109 | Action Required |
| 110 | Evidence ID |
| 111 | Evidence Type |
| 112 | Location / Path |
| 113 | Date Collected |
| 114 | Collected By |
| 115 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Partial, Automated, Semi-Automated, Manual, Standard, Normal
Emergency, Low, Medium, High, Critical, Virtual Meeting, Phone, Email Chain
Instant Messaging, Other, Submission, Approval, 24h Before, At Implementation
Completion, All, Email, Portal, IM, SMS, All Users, IT Staff, Management
Selective, Mandatory, Optional, Electronic, Paper, Both, Secure Delete
Archive, Destruction, Cloud SaaS, On-Premises, Hybrid, Self-Hosted, API
File Transfer, Webhook, Active, Expiring Soon, Expired, 24/7, Business Hours
Community, None, Change Request, Policy Document, Process Record
System Screenshot, Configuration Export, Audit Log, Training Record
Test Result, Risk Assessment, Meeting Minutes, To Be Determined, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 115 columns, 74 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The enemy knows the system. Security through obscurity is not security at all."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
