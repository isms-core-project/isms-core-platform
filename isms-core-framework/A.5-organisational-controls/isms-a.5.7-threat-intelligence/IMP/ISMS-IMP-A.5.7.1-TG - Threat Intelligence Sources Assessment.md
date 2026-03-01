<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.1-TG:framework:TG:a.5.7.1 -->
**ISMS-IMP-A.5.7.1-TG - Threat Intelligence Sources Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Threat Intelligence Sources Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.7.1-TG |
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
- ISMS-IMP-A.5.7.2 (Intelligence Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Intelligence Integration & Distribution Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a57_1_sources.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.7.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Source Inventory |
| 3 | Source Evaluation |
| 4 | Coverage Matrix |
| 5 | Cost Analysis |
| 6 | Compliance Check |
| 7 | Action Items |
| 8 | Metadata |
| 9 | Update Frequency |
| 10 | Source Contacts |
| 11 | Vendor SLAs |
| 12 | Source Performance Validation |
| 13 | Evidence Register |
| 14 | Summary Dashboard |
| 15 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #006100 | Dark Green (Pass) |
| #0066CC | Custom |
| #00B050 | Custom |
| #4472C4 | Medium Blue (Sub-headers) |
| #9C0006 | Dark Red (Error) |
| #C65911 | Brown/Orange (Overdue) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | Light Gray (Column Headers) |
| #E7F4E4 | Custom |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFF4CC | Custom |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Source ID |
| 2 | Source Name |
| 3 | Source Type |
| 4 | Source Category |
| 5 | Provider |
| 6 | Contact Email |
| 7 | Contract Start |
| 8 | Contract End |
| 9 | Auto Renew |
| 10 | Status |
| 11 | CVSS Support |
| 12 | Primary Owner |
| 13 | Backup Owner |
| 14 | Last Review Date |
| 15 | Next Review Date |
| 16 | Notes |
| 17 | Evaluation Date |
| 18 | Evaluator |
| 19 | Reliability Rating |
| 20 | Reliability Justification |
| 21 | Credibility Rating |
| 22 | Credibility Justification |
| 23 | Timeliness Score |
| 24 | Timeliness Notes |
| 25 | Relevance Score |
| 26 | Relevance Notes |
| 27 | Actionability Score |
| 28 | Actionability Notes |
| 29 | Overall Quality Score |
| 30 | Quality Rating |
| 31 | False Positive Rate |
| 32 | CVSS Accuracy Rate |
| 33 | CVSS Sample Size |
| 34 | CVSS Validation Date |
| 35 | Evidence Link |
| 36 | Recommendation |
| 37 | Next Evaluation |
| 38 | Source_ID |
| 39 | Source_Name |
| 40 | Global |
| 41 | North_America |
| 42 | Europe |
| 43 | Asia_Pacific |
| 44 | Middle_East |
| 45 | Latin_America |
| 46 | Africa |
| 47 | Financial |
| 48 | Healthcare |
| 49 | Government |
| 50 | Critical_Infra |
| 51 | Technology |
| 52 | Education |
| 53 | Retail |
| 54 | Manufacturing |
| 55 | All_Sectors |
| 56 | Malware |
| 57 | Phishing |
| 58 | Ransomware |
| 59 | Data_Breach |
| 60 | DDoS |
| 61 | Insider |
| 62 | Supply_Chain |
| 63 | Zero_Day |
| 64 | APT |
| 65 | Vulnerabilities |
| 66 | Annual Cost CHF |
| 67 | Implementation Cost |
| 68 | Operational Cost Annual |
| 69 | Total Cost |
| 70 | Alerts Per Month |
| 71 | Cost Per Alert |
| 72 | Actionable Alerts Pct |
| 73 | Value Rating |
| 74 | ROI Assessment |
| 75 | Budget Next Year |
| 76 | Renewal Date |
| 77 | Handles PII |
| 78 | GDPR Applicable |
| 79 | FADP Applicable |
| 80 | DPA In Place |
| 81 | DPA Signed Date |
| 82 | DPA Review Date |
| 83 | SCC Required |
| 84 | SCC In Place |
| 85 | Compliance Status |
| 86 | Validation ID |
| 87 | Validation Quarter |
| 88 | Validation Date |
| 89 | Validator |
| 90 | Validation Method |
| 91 | Total Sample Size |
| 92 | IOC Sample Size |
| 93 | IOC True Positives |
| 94 | IOC False Positives |
| 95 | IOC Accuracy |
| 96 | CVE Sample Size |
| 97 | CVE Accurate |
| 98 | CVE Inaccurate |
| 99 | CVE Accuracy |
| 100 | CVSS Accurate Count |
| 101 | CVSS Inaccurate Count |
| 102 | CVSS Accuracy Method |
| 103 | Overall Accuracy Rate |
| 104 | Admiralty Code Source |
| 105 | Admiralty Code Info |
| 106 | Admiralty Combined |
| 107 | Validation Pass |
| 108 | Pass Criteria Met |
| 109 | Action Required |
| 110 | Action Notes |
| 111 | Action Item Created |
| 112 | Action Item ID |
| 113 | Evidence Location |
| 114 | Reviewed By |
| 115 | Review Date |
| 116 | Next Validation Date |
| 117 | Contractual Frequency |
| 118 | Actual Avg Frequency |
| 119 | Last Update Received |
| 120 | Update Count Last 30 Days |
| 121 | Expected Update Count |
| 122 | Update Variance |
| 123 | SLA Met |
| 124 | SLA Met Justification |
| 125 | Outage Count Last Quarter |
| 126 | Longest Outage Duration |
| 127 | Average Outage Duration |
| 128 | Timeliness Trend |
| 129 | Last SLA Review |
| 130 | Next SLA Review |
| 131 | Contact Type |
| 132 | Contact Name |
| 133 | Contact Title |
| 134 | Contact Phone |
| 135 | Contact Region |
| 136 | Availability |
| 137 | Escalation Path |
| 138 | Preferred Contact Method |
| 139 | Language Supported |
| 140 | Last Contact Date |
| 141 | Last Contact Reason |
| 142 | Response Quality |
| 143 | Response Time |
| 144 | Contact Status |
| 145 | Replacement Contact |
| 146 | Last Verified |
| 147 | Next Verification |
| 148 | SLA Record ID |
| 149 | SLA Metric |
| 150 | Contractual Target |
| 151 | Contractual Target Numeric |
| 152 | Actual Performance |
| 153 | Actual Performance Numeric |
| 154 | Performance Variance |
| 155 | Measurement Period |
| 156 | Measurement Start Date |
| 157 | Measurement End Date |
| 158 | SLA Status |
| 159 | SLA Breach Count |
| 160 | Penalty Clause |
| 161 | Penalty Amount |
| 162 | Penalty Applied |
| 163 | Penalty Application Date |
| 164 | Credit Received |
| 165 | Escalated To Vendor |
| 166 | Escalation Date |
| 167 | Vendor Response |
| 168 | Reviewer |
| 169 | Action ID |
| 170 | Issue Type |
| 171 | Issue Description |
| 172 | Detected In Sheet |
| 173 | Priority |
| 174 | Assigned To |
| 175 | Due Date |
| 176 | Status Notes |
| 177 | Resolution Date |
| 178 | Created Date |
| 179 | Created By |
| 180 | Last Updated |
| 181 | Evidence ID |
| 182 | Assessment Area |
| 183 | Evidence Type |
| 184 | Description |
| 185 | Location / Path |
| 186 | Date Collected |
| 187 | Collected By |
| 188 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Commercial, OSINT, Government, Internal, Vendor, Peer_Sharing, Threat_Feed
ISAC, Vendor_Advisory, Blog, Social_Media, Research_Report, Internal_Telemetry
Active, Inactive, Trial, Pending_Renewal, Cancelled, 4.0 Full, 4.0 Basic
3.1 Full, 3.1 Basic, 2.0 Only, Proprietary, None, A - Completely Reliable
B - Usually Reliable, C - Fairly Reliable, D - Not Usually Reliable
E - Unreliable, F - Cannot Judge, 1 - Confirmed, 2 - Probably True
3 - Possibly True, 4 - Doubtful, 5 - Improbable, 6 - Cannot Judge, Critical
High, Medium, Low, Yes, No, N/A, ✅ Compliant, ❌ Non_Compliant, ⚠️ Under_Review
➖ Not_Applicable, API, STIX/TAXII, RSS, Email, Manual, Webhook, Syslog, TIP
SIEM, SOAR, Vuln_Scanner, EDR, Ticketing, Firewall, Proxy, Custom, Degraded
Failed, Planned, Yes_4.0, Yes_3.1, Yes_Both, Partial, Real_Time, Hourly
Every_4_Hours, Every_12_Hours, Daily, Weekly, Monthly, Quarterly, Ad_Hoc, Met
Missed, Exceeded, Measuring, Healthy, Maintenance, OK, Warning, Pass
Conditional_Pass, Fail, Review, Improve, Deprecate, A, B, C, D, E, F, 1, 2, 3
4, 5, 6, Partial_Pass, Not_Tested, Important, Standard, On_Leave, Departed
Other, In_Progress, Under Review, Unknown, Continue, Enhance, Discontinue
Excellent, Good, Fair, Poor, High_Value, Good_Value, Acceptable, Reconsider
\u2705 Compliant, \u274c Non_Compliant, \u26a0 Under_Review
\u2014 Not_Applicable, Technical Support, Account Manager, Emergency Contact
Billing, Executive, Data Protection Officer, Security Team, Disputed, Waived
Quality, Coverage Gap, Cost, Compliance, Contract, Integration, CVSS Accuracy
Continuity, Source Evaluation, Coverage Matrix, Cost Analysis
Compliance Check, Update Frequency, Source Contacts, Vendor SLAs
Source Performance Validation, Open, In Progress, Blocked, Resolved, Closed
Config File, Screenshot, Report, Log File, Test Result, Policy Document
Diagram, \u2705 Verified, Pending, \u274c Not Verified, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 15 sheets, 188 columns, 179 validation values, 16 colors

---

**END OF SPECIFICATION**


---

*"An expert is a person who has made all the mistakes that can be made in a very narrow field."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
