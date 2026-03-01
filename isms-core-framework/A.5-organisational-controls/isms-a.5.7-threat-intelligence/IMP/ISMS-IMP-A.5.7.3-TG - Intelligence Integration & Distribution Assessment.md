<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.3-TG:framework:TG:a.5.7.3 -->
**ISMS-IMP-A.5.7.3-TG - Intelligence Integration & Distribution Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Intelligence Integration & Distribution Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.7.3-TG |
| **Related Policy** | ISMS-POL-A.5.7 (Threat Intelligence) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.7 (Threat Intelligence) |
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

- ISMS-POL-A.5.7 (Threat Intelligence)
- ISMS-IMP-A.5.7.1 (Threat Intelligence Sources Assessment)
- ISMS-IMP-A.5.7.2 (Intelligence Collection & Analysis Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a57_3_integration.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.7.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Tool Integration Matrix |
| 3 | IOC Deployment |
| 4 | Dissemination Channels |
| 5 | Stakeholder Registry |
| 6 | Distribution Tracking |
| 7 | Feedback Collection |
| 8 | Integration Metrics |
| 9 | Action Items |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #0066CC | Custom |
| #4472C4 | Medium Blue (Sub-headers) |
| #9C0006 | Dark Red (Error) |
| #C65911 | Brown/Orange (Overdue) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Tool ID |
| 2 | Tool Category |
| 3 | Tool Name |
| 4 | Vendor |
| 5 | Version |
| 6 | Primary Owner |
| 7 | Integration Status |
| 8 | Integration Method |
| 9 | Integration Direction |
| 10 | Data Types Integrated |
| 11 | Automation Level |
| 12 | Update Frequency |
| 13 | IOC Types Supported |
| 14 | Last Successful Sync |
| 15 | Sync Errors Last 30 Days |
| 16 | Effectiveness Rating |
| 17 | IOC ID |
| 18 | IOC Type |
| 19 | IOC Value |
| 20 | Intelligence Source |
| 21 | Threat Actor |
| 22 | Associated Malware |
| 23 | Confidence Level |
| 24 | Severity |
| 25 | TLP Classification |
| 26 | Deployment Date |
| 27 | Deployed To Tools |
| 28 | Deployment Method |
| 29 | Expiration Date |
| 30 | Status |
| 31 | Hits Last 7 Days |
| 32 | Hits Last 30 Days |
| 33 | Hits Total |
| 34 | Last Hit Date |
| 35 | False Positive |
| 36 | Channel ID |
| 37 | Channel Name |
| 38 | Channel Type |
| 39 | Target Audience |
| 40 | Intelligence Types |
| 41 | Frequency |
| 42 | Delivery Method |
| 43 | TLP Max Classification |
| 44 | Active Subscribers |
| 45 | Avg Engagement Rate |
| 46 | Owner |
| 47 | Last Distribution |
| 48 | Notes |
| 49 | Stakeholder ID |
| 50 | Full Name |
| 51 | Email |
| 52 | Role Title |
| 53 | Department |
| 54 | Stakeholder Type |
| 55 | TLP Clearance |
| 56 | Subscribed Channels |
| 57 | Engagement Level |
| 58 | Last Feedback Date |
| 59 | Distribution ID |
| 60 | Product ID |
| 61 | Product Title |
| 62 | Distribution Date |
| 63 | Recipients Count |
| 64 | Views Count |
| 65 | Downloads Count |
| 66 | Feedback Received |
| 67 | Action Taken Count |
| 68 | Engagement Rate |
| 69 | Effectiveness |
| 70 | Feedback ID |
| 71 | Stakeholder Name |
| 72 | Feedback Date |
| 73 | Feedback Method |
| 74 | Overall Rating |
| 75 | Relevance Rating |
| 76 | Timeliness Rating |
| 77 | Actionability Rating |
| 78 | Clarity Rating |
| 79 | Intelligence Used |
| 80 | Action Taken |
| 81 | Improvement Suggestions |
| 82 | Would Recommend |
| 83 | Positive Comments |
| 84 | Negative Comments |
| 85 | Follow Up Required |
| 86 | Metric ID |
| 87 | Metric Name |
| 88 | Metric Category |
| 89 | Measurement Period |
| 90 | Target Value |
| 91 | Actual Value |
| 92 | Unit |
| 93 | Performance vs Target |
| 94 | Trend |
| 95 | Data Source |
| 96 | Last Updated |
| 97 | Action ID |
| 98 | Issue Type |
| 99 | Issue Description |
| 100 | Priority |
| 101 | Assigned To |
| 102 | Due Date |
| 103 | Status Notes |
| 104 | Resolution Date |
| 105 | Evidence Link |
| 106 | Created Date |
| 107 | Created By |
| 108 | Evidence ID |
| 109 | Assessment Area |
| 110 | Evidence Type |
| 111 | Description |
| 112 | Location / Path |
| 113 | Date Collected |
| 114 | Collected By |
| 115 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
SIEM, EDR, Firewall, Proxy, Email_Gateway, IDS_IPS, TIP, SOAR, Vuln_Scanner
Other, Fully_Integrated, Partially_Integrated, Planned, Not_Integrated, API
Feed, Manual_Import, STIX_TAXII, Syslog, Custom_Script, Inbound, Outbound
Bidirectional, Fully_Automated, Semi_Automated, Manual, Real-time, Hourly
Daily, Weekly, On_Demand, IP_Address, Domain, URL, File_Hash, Email_Address
Registry_Key, Mutex, Certificate, High, Medium, Low, Critical, Info, TLP:CLEAR
TLP:GREEN, TLP:AMBER, TLP:AMBER+STRICT, TLP:RED, Active, Expired, Withdrawn
Under_Review, Yes, No, Unknown, Under_Investigation, Excellent, Good, Fair
Poor, Open, In_Progress, Blocked, Resolved, Closed, Automated, Hybrid
Email_List, Portal, Dashboard, Briefing, Chat, Ticketing_System, Executive
CISO, SOC, IR_Team, IT_Ops, Developers, All_Staff, Monthly, Quarterly, Email
Web_Portal, Mobile_App, PDF_Report, Presentation, Slack, Teams, Inactive
Pilot, Deprecated, Manager, Analyst, Operator, Developer, External_Partner
Vendor, None, On_Leave, Departed, Survey, Email_Reply, Meeting, Ticket, Call
Partial, Will_Use_Later, Maybe, Tool_Integration, IOC_Effectiveness
Dissemination, Stakeholder_Engagement, Automation, Improving, Stable
Declining, IOC_Quality, Process, Config File, Screenshot, Report, Log File
Test Result, Policy Document, Contract, Diagram, \u2705 Verified, Pending
\u274c Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 115 columns, 139 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"The opposite of a correct statement is a false statement. But the opposite of a profound truth may well be another profound truth."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
