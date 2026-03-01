<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.2-TG:framework:TG:a.5.7.2 -->
**ISMS-IMP-A.5.7.2-TG - Intelligence Collection & Analysis Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Intelligence Collection & Analysis Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.7.2-TG |
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
- ISMS-IMP-A.5.7.3 (Intelligence Integration & Distribution Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a57_2_collection_analysis.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.7.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Intelligence Requirements |
| 3 | Collection Sources |
| 4 | Raw Intelligence Log |
| 5 | Intelligence Production |
| 6 | MITRE Mapping |
| 7 | Quality Metrics |
| 8 | Process Maturity |
| 9 | Action Items |
| 10 | Analysis Tools |
| 11 | Threat Actor Profiles |
| 12 | Campaign Tracking |
| 13 | Evidence Register |
| 14 | Summary Dashboard |
| 15 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FF0000 | Red (Critical/Alert) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Requirement ID |
| 2 | Intelligence Type |
| 3 | Requirement Description |
| 4 | Priority |
| 5 | Target Sector |
| 6 | Target Region |
| 7 | Threat Category |
| 8 | Collection Source 1 |
| 9 | Collection Source 2 |
| 10 | Collection Source 3 |
| 11 | Collection Method |
| 12 | Coverage Status |
| 13 | Collection Frequency |
| 14 | Last Collected |
| 15 | Gap Identified |
| 16 | Gap Remediation |
| 17 | Responsible Analyst |
| 18 | Notes |
| 19 | Source ID |
| 20 | Source Name |
| 21 | Source Type |
| 22 | Data Format |
| 23 | Update Frequency |
| 24 | Coverage Geographic |
| 25 | Coverage Sector |
| 26 | Coverage Threat Types |
| 27 | Integration Status |
| 28 | Integration Platform |
| 29 | Cost Annual |
| 30 | Contract Expiry |
| 31 | Primary Contact |
| 32 | Data Quality Rating |
| 33 | Last Review Date |
| 34 | Analyst ID |
| 35 | Analyst Name |
| 36 | Email |
| 37 | Role |
| 38 | Team |
| 39 | Years Experience TI |
| 40 | Years Experience InfoSec |
| 41 | Primary Focus Area |
| 42 | Secondary Focus Area |
| 43 | Skill OSINT |
| 44 | Skill Malware Analysis |
| 45 | Skill MITRE ATTACK |
| 46 | Skill Scripting Python |
| 47 | Skill Threat Modeling |
| 48 | Skill Report Writing |
| 49 | Skill Briefing Presentation |
| 50 | Certifications |
| 51 | Training Planned 2025 |
| 52 | Training Budget 2025 |
| 53 | Last Performance Review |
| 54 | Capability Gap Identified |
| 55 | Product ID |
| 56 | Product Type |
| 57 | Product Title |
| 58 | Primary Author |
| 59 | Contributors |
| 60 | Publication Date |
| 61 | TLP Classification |
| 62 | Confidence Level |
| 63 | Target Audience |
| 64 | Stakeholder Feedback Rating |
| 65 | Consumption Rate |
| 66 | Actionability Score |
| 67 | Time to Produce Hours |
| 68 | Status |
| 69 | Technique ID |
| 70 | Tactic |
| 71 | Technique Name |
| 72 | Sub Technique |
| 73 | Priority for Org |
| 74 | Coverage Level |
| 75 | Intelligence Sources |
| 76 | Last Intelligence Update |
| 77 | Detection Capability |
| 78 | Use Cases Identified |
| 79 | Gap Analysis |
| 80 | KPI ID |
| 81 | KPI Name |
| 82 | Description |
| 83 | Target Value |
| 84 | Current Value |
| 85 | Last Month Value |
| 86 | Measurement Period |
| 87 | Performance vs Target |
| 88 | Trend |
| 89 | Data Source |
| 90 | Owner |
| 91 | Last Updated |
| 92 | Log ID |
| 93 | Date Received |
| 94 | Time Received |
| 95 | Initial Triage Priority |
| 96 | Brief Description |
| 97 | Raw Data Location |
| 98 | Assigned Analyst |
| 99 | Processing Status |
| 100 | Date Processed |
| 101 | Linked Product ID |
| 102 | Quality Score |
| 103 | Process Area |
| 104 | Current Level |
| 105 | Target Level |
| 106 | Gap |
| 107 | Evidence |
| 108 | Action Plan |
| 109 | Target Date |
| 110 | Action ID |
| 111 | Related Sheet |
| 112 | Issue Description |
| 113 | Assigned To |
| 114 | Due Date |
| 115 | Progress Percentage |
| 116 | Completion Date |
| 117 | Outcome |
| 118 | Lessons Learned |
| 119 | Tool ID |
| 120 | Tool Name |
| 121 | Tool Category |
| 122 | Vendor |
| 123 | License Type |
| 124 | Primary Users |
| 125 | Use Cases |
| 126 | Data Sources |
| 127 | CVSS Support |
| 128 | Version |
| 129 | Training Required |
| 130 | Training Status |
| 131 | Actor ID |
| 132 | Actor Name |
| 133 | Actor Aliases |
| 134 | Actor Type |
| 135 | Attribution Confidence |
| 136 | Country of Origin |
| 137 | First Observed |
| 138 | Last Activity |
| 139 | Targeting Our Sector |
| 140 | Targeting Our Org |
| 141 | Primary Motivation |
| 142 | Sophistication Level |
| 143 | Primary TTPs |
| 144 | Common Malware |
| 145 | Infrastructure Notes |
| 146 | CVEs Exploited |
| 147 | VTL Records Count |
| 148 | Related Campaigns |
| 149 | Last Update Date |
| 150 | Campaign ID |
| 151 | Campaign Name |
| 152 | Campaign Start Date |
| 153 | Campaign End Date |
| 154 | Campaign Status |
| 155 | Target Sectors |
| 156 | Target Geographies |
| 157 | Our Sector Targeted |
| 158 | Our Org Targeted |
| 159 | Primary Objective |
| 160 | Attack Vectors |
| 161 | TTPs Used |
| 162 | CVEs CVSS Max |
| 163 | IOCs Count |
| 164 | VTL Records Created |
| 165 | Incidents Our Org |
| 166 | Threat Level |
| 167 | Monitoring Status |
| 168 | Evidence ID |
| 169 | Assessment Area |
| 170 | Evidence Type |
| 171 | Location / Path |
| 172 | Date Collected |
| 173 | Collected By |
| 174 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Strategic, Tactical, Operational, Technical, Critical, High, Medium, Low
Automated_Feed, Manual_Research, OSINT, Partnership, Internal_Telemetry
Real-time, Hourly, Daily, Weekly, On_Demand, Threat_Model, Analysis_Method
Taxonomy, Tool, Threat_Profiling, IOC_Analysis, Campaign_Tracking, Reporting
Integration, Fully_Implemented, Partially_Implemented, Planned, Not_Used, Yes
No, Optional, Excellent, Good, Fair, Poor, Lead_Analyst, Senior_Analyst
Analyst, Junior_Analyst, Intern, Expert, Advanced, Intermediate, Beginner
None, Strategic_Report, Tactical_Brief, Operational_Alert, Technical_Analysis
IOC_Package, Threat_Profile, Draft, Review, Published, Archived, Unconfirmed
TLP:CLEAR, TLP:GREEN, TLP:AMBER, TLP:AMBER+STRICT, TLP:RED, Full, Partial
Limited, Nation-State, Criminal_Syndicate, Hacktivist, Insider_Threat
Script_Kiddie, Unknown, Not_Exploited, PoC_Exists, Active_Exploitation
Widespread, Info, Open, In_Progress, Patched, Mitigated, Risk_Accepted
Verified, 1 - Initial, 2 - Managed, 3 - Defined, 4 - Quantitatively Managed
5 - Optimizing, Blocked, Resolved, Closed, TIP, SIEM, Malware_Analysis
Collaboration, Visualization, Scripting, Other, Commercial, Open_Source
Freeware, Internal_Developed, N/A, Confirmed, Suspected, Espionage, Financial
Disruption, Ideology, Moderate, Active, Concluded, Dormant, Data_Theft
Ransomware, Credential_Harvesting, Active_Monitoring, Passive_Monitoring, 4.0
3.1, Integrated, Standalone, Deprecated, Config File, Screenshot, Report
Log File, Test Result, Policy Document, Contract, Diagram, \u2705 Verified
Pending, \u274c Not Verified, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 15 sheets, 174 columns, 142 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"How wonderful that we have met with a paradox. Now we have some hope of making progress."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
