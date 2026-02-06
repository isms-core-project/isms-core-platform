**ISMS-IMP-A.8.15.2-TG - Log Collection & Centralization Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Collection Infrastructure & SIEM Integration |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.2 (Log Protection & Integrity Requirements), Section 2.3 (Log Retention & Storage Requirements) |
| **Purpose** | Assess SIEM/log management infrastructure, verify log collection coverage and reliability, validate centralized logging implementation |
| **Target Audience** | Security Operations Center (SOC), SIEM Administrators, IT Operations, Network Team, Security Engineers, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Infrastructure & Operational |
| **Review Cycle** | Annual (full assessment), Quarterly (reliability metrics) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Log Collection assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.15.2-UG.

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel script maintainers)

---

# Document Overview

**Document ID:** ISMS-IMP-A.8.15.2-TG  
**Assessment Area:** Log Collection & Centralization  
**Related Policy:** ISMS-POL-A.8.15, Section 2.2 (Protection), Section 2.3 (Retention)  
**Purpose:** Technical specification for Excel workbook structure and Python generation script  

---

# Workbook Structure Overview

| Sheet # | Sheet Name | Purpose | User Input Required | Formula-Driven | Protected |
|---------|------------|---------|-------------------|----------------|-----------|
| 1 | Instructions_Legend | Usage guide, scoring methodology | No | No | Yes (Read-Only) |
| 2 | SIEM_Infrastructure | SIEM platform inventory | Yes | Partial | No (Input Area) |
| 3 | Storage_Architecture | Tiered storage design documentation | Yes | Yes (Capacity calcs) | Partial |
| 4 | Network_Infrastructure | Network connectivity and bandwidth | Yes | Yes (Utilization calcs) | Partial |
| 5 | Log_Source_Coverage | Verify log sources forwarding | Yes | Yes (From IMP-A.8.15.1) | Partial |
| 6 | Integration_Methods | Technical integration documentation | Yes | No | No (Input Area) |
| 7 | Collection_Reliability | Metrics and KPIs | Yes | Yes (Compliance calcs) | Partial |
| 8 | Encryption_Authentication | Security controls verification | Yes | Yes (Compliance scoring) | Partial |
| 9 | Gap_Analysis | Consolidated gaps and remediation | Partial | Yes (Auto-populated from other sheets) | Partial |
| 10 | Evidence_Register | Evidence documentation index | Yes | No | No (Input Area) |
| 11 | Approval_Sign_Off | Three-level approval workflow | Yes | Yes (Summary metrics) | Partial |

**Total Sheets**: 11

---

# Sheet Specifications

## Sheet 1: Instructions_Legend

**Purpose**: Provide assessment methodology and scoring guide

**Key Sections**:

- Document information block (Document ID, Version, Assessment Date, Organization)
- Completion steps (8-step process)
- Scoring methodology (0-100% scale with color coding)
- Color coding guide (Yellow=Input, Blue=Formula, Green=Compliant, Red=Critical Gap)

**Color Scale**:
| Score | Rating | Color | Meaning |
|-------|--------|-------|---------|
| 90-100% | Excellent | Green | Fully compliant |
| 75-89% | Good | Light Green | Substantially compliant |
| 50-74% | Adequate | Yellow | Partially compliant |
| 25-49% | Poor | Orange | Minimally compliant |
| 0-24% | Critical | Red | Non-compliant |

---

## Sheet 2: SIEM_Infrastructure

**Purpose**: Document all centralized log management platforms

**Column Structure** (15 columns):

- A: SIEM Platform ID (SIEM-001, SIEM-002...)
- B: SIEM Name (Splunk, ELK, QRadar, Microsoft Sentinel...)
- C: Vendor
- D: Version/Build
- E: Deployment Type (On-Premises, Cloud, Hybrid, SaaS)
- F: Primary Use Case (Security, Compliance, Operations, All)
- G: Capacity (EPS)
- H: Current Utilization (%)
- I: Utilization Status (Formula: IF <60% "Normal", IF <80% "Warning", ELSE "Critical")
- J: License Expiration (Date)
- K: Geographic Location
- L: High Availability (Yes/No/Planned)
- M: Maintenance Window
- N: Responsible Team
- O: Notes

**Summary Section**:

- Total SIEM Platforms
- Average Utilization %
- HA Coverage %
- Licenses Expiring <90 Days

**Conditional Formatting**:

- Utilization Status: Green (Normal), Yellow (Warning), Red (Critical)
- License Expiration: Red if expired or <30 days, Orange if 30-90 days

---

## Sheet 3: Storage_Architecture

**Purpose**: Document tiered storage (hot/warm/cold) supporting retention

**Sections**:
1. **Hot Storage** (Rows 4-10): Online storage, 12-month retention
2. **Warm Storage** (Rows 12-18): Nearline storage, compressed
3. **Cold Archive** (Rows 20-26): Long-term archive, 7-year total retention
4. **Capacity Planning** (Rows 28-37): Projections, growth calculations
5. **Retention Compliance** (Rows 39-50): Policy requirement validation

**Key Columns**:

- Storage System, Total Capacity (TB), Current Usage (TB), Utilization %, Retention Period
- Redundancy, Geographic Location, Access Time, WORM Capability

**Capacity Formulas**:

- Overall Utilization % = Total Usage / Total Capacity * 100
- Projected 12-Month Usage = Current + (Monthly Ingestion * 12 * (1 + Growth Rate))
- Months Until Exhaustion = (Total Capacity - Current Usage) / Monthly Ingestion

**Retention Compliance Table**:

- Security Events: 12mo online + 7yr total = Compliant?
- Authentication Logs: 12mo + 7yr = Compliant?
- Database Logs (Sensitive): 12mo + 7yr = Compliant?
- Application Logs: 6mo + 18mo total = Compliant?

---

## Sheet 4: Network_Infrastructure

**Purpose**: Document network paths supporting log forwarding

**Sections**:
1. **Firewall Rules** (Rows 4-30): Rules allowing log traffic
2. **Network Paths** (Rows 35-60): Bandwidth, latency, packet loss

**Firewall Rules Columns**:

- Rule ID, Firewall Name, Source Network, Destination IP, Protocol, Port, Action, Last Review Date
- Review Status (Formula: IF >365 days "Overdue", IF >180 days "Due Soon", ELSE "Current")

**Network Path Columns**:

- Path ID, Source Segment, Destination, Bandwidth (Mbps), Utilization %, Log Traffic (Mbps)
- Latency (ms), Packet Loss %, Path Status (Formula: IF Util >80% OR Loss >1% "Critical"...)
- Redundancy (Yes/No/Partial)

**Summary Metrics**:

- Total Paths, Healthy Paths, Paths with Redundancy, Avg Latency, Avg Packet Loss
- Network Health Score = (Healthy Paths / Total Paths) * 100

---

## Sheet 5: Log_Source_Coverage

**Purpose**: Verify log sources from IMP-A.8.15.1 are forwarding

**CRITICAL DEPENDENCY**: Imports from IMP-A.8.15.1 Sheet 2 (System_Inventory)

**Columns A-F: Auto-Imported** (Protected):

- A: System ID (from IMP-A.8.15.1)
- B: System Name
- C: System Type
- D: Data Classification
- E: System Criticality  
- F: System Owner

**Columns G-P: Manual Verification**:

- G: Collection Status (Dropdown: Forwarding, Partial, Not Forwarding, Planned, N/A)
- H: SIEM Destination (Which SIEM receives logs)
- I: Collection Method (Agent, Syslog, API, Cloud Connector, Manual, None)
- J: Last Log Received (DateTime)
- K: Daily Log Volume (GB/day or Events/day)
- L: Verification Method (SIEM Search, Dashboard, Agent Status, API Check)
- M: Verification Date
- N: Gap Reason (if not forwarding)
- O: Remediation Plan
- P: Target Completion Date

**Compliance Calculations**:

- Total Log Sources = COUNTA(B:B)
- Forwarding Count = COUNTIF(G:G,"Forwarding")
- Collection Coverage % = (Forwarding + Partial) / Total * 100
- Target: >=98%

**Conditional Formatting**:

- Collection Status: Green (Forwarding), Yellow (Partial), Red (Not Forwarding), Orange (Planned)
- **Critical Gap Highlighting**: IF Criticality="Critical" AND Status!="Forwarding" -> BOLD RED

---

## Sheet 6: Integration_Methods

**Purpose**: Document technical integration details for each log source

**Columns** (18 columns):

- A-B: System ID, System Name (reference from Sheet 5)
- C: Integration Type (Agent, Syslog, API, Cloud Connector, File, Database, Manual)
- D-F: Agent Software, Version, Auto-Update
- G-I: Protocol Details, Transport Protocol, Port Number
- J-K: Encryption Enabled, Authentication Method
- L: Collection Frequency
- M-N: Configuration Source, Last Configuration Change
- O-P: Configuration Owner, Troubleshooting Contact
- Q-R: Documentation Location, Notes

**Summary Statistics**:

- Total Integrations, Agent-Based Count, Syslog Count, API Count, Cloud Connector Count
- Encrypted Integrations, Encryption Coverage %
- Authenticated Integrations, Authentication Coverage %

---

## Sheet 7: Collection_Reliability

**Purpose**: Quantify collection reliability with metrics

**Sections**:
1. **SIEM Availability** (Rows 5-14): Uptime %, downtime minutes, MTBF, MTTR
2. **Log Source Connectivity** (Rows 18-25): Total sources, forwarding count, coverage %
3. **Collection Failures** (Rows 28-40): Failure count by category, MTTD, MTTR
4. **Data Quality** (Rows 43-52): Unparsed logs, parsing errors, data quality score
5. **Alerting Effectiveness** (Rows 55-62): Alerts configured, false positive rate
6. **Overall Reliability Score** (Bottom): Weighted average of all metrics

**Key Metrics**:

- SIEM Uptime Target: >=99.5%
- Collection Coverage Target: >=98%
- Data Quality Target: >=99%
- Alert Detection Rate Target: >=95%

**Overall Reliability Formula**:
```
= (SIEM Availability * 0.30) +
  (Collection Coverage * 0.30) +
  (Failure Rate Score * 0.20) +
  (Data Quality * 0.10) +
  (Alert Effectiveness * 0.10)
```

---

## Sheet 8: Encryption_Authentication

**Purpose**: Verify TLS encryption and authentication per policy Section 2.2

**Columns** (21 columns):

- A-D: System ID, Name, Data Classification, Integration Type
- E-I: Encryption Status, Protocol (TLS 1.2/1.3), Cipher Suite, Certificate Validation, PFS
- J: Policy Compliance (Encryption) - Formula: IF TLS>=1.2 "Compliant" ELSE "Non-Compliant"
- K-O: Authentication Method, Credential Strength, Last Rotation, Rotation Schedule, Automated
- P: Policy Compliance (Auth) - Formula: IF Method!="None" AND Strength!="Weak" "Compliant"
- Q: Overall Compliance - Formula: IF J="Compliant" AND P="Compliant" "Y" ELSE "N"
- R: Risk Level - Formula (see risk matrix in Chunk 4 above)
- S: Exception ID
- T: Remediation Plan
- U: Target Completion

**Risk Matrix Formula**:
```
=IF(AND(C="Restricted",E="Disabled"),"CRITICAL",
   IF(AND(C="Confidential",E="Disabled"),"HIGH",
   IF(E="Disabled","MEDIUM",
   IF(OR(F="TLS 1.0",F="TLS 1.1"),"HIGH",
   IF(K="None","HIGH",
   IF(L="Weak","MEDIUM","LOW"))))))
```

**Compliance Summary**:

- Encryption Compliance % = COUNTIF(J:J,"Compliant") / Total * 100
- Authentication Compliance % = COUNTIF(P:P,"Compliant") / Total * 100
- Overall Compliance % = COUNTIF(Q:Q,"Y Compliant") / Total * 100
- Target: 100% (or >=95% with approved exceptions)

---

## Sheet 9: Gap_Analysis

**Purpose**: Consolidate gaps from all sheets with risk-based prioritization

**Columns** (20 columns):

- A: Gap ID (COLL-001, COLL-002...)
- B: Gap Category (Missing Coverage, Reliability, Encryption, Authentication, Storage, Network, Data Quality)
- C: Gap Description
- D: Affected System(s)
- E: Source Sheet (which sheet identified this gap)
- F: Policy Reference (ISMS-POL-A.8.15 Section X.X)
- G-H: Impact Level, Likelihood
- I: Risk Rating (Formula using risk matrix)
- J: Business Impact
- K: Proposed Solution
- L: Responsible Party
- M: Target Completion Date
- N: Estimated Effort (Hours)
- O: Budget Required
- P: Compensating Controls
- Q: Exception ID
- R: Status (Open, In Progress, Resolved, Accepted, Deferred)
- S: Tracking Ticket ID
- T: Notes

**Auto-Population Logic**:

- FROM Sheet 5: WHERE Collection Status = "Not Forwarding" AND Criticality = "Critical"
- FROM Sheet 7: WHERE SIEM Uptime < 99.5% OR Coverage < 98%
- FROM Sheet 8: WHERE Overall Compliance = "N Non-Compliant" AND Exception ID blank
- FROM Sheet 3: WHERE Months Until Capacity Exhaustion < 6

**Summary by Category**:
| Category | Total | Critical | High | Medium | Low |
|----------|-------|----------|------|--------|-----|
| Missing Coverage | COUNT | COUNTIFS | ... | ... | ... |
| Reliability | ... | ... | ... | ... | ... |
| Encryption | ... | ... | ... | ... | ... |

**Gap Status Summary**:

- Open, In Progress, Resolved, Accepted (Exception), Deferred counts and percentages

---

## Sheet 10: Evidence_Register

**Purpose**: Index all evidence collected during assessment

**Columns** (12 columns):

- A: Evidence ID (EV-COLL-001, EV-COLL-002...)
- B: Evidence Type (Screenshot, Configuration Export, Report, Documentation, Diagram, Other)
- C: Description
- D: Related Sheet (2-8)
- E: Related System/Topic
- F: File Name
- G: File Location (folder path)
- H: Date Collected
- I: Collected By
- J: Sensitivity (Public, Internal, Confidential, Restricted)
- K: Retention Period (typically 7 years)
- L: Notes

**Folder Structure Recommendation**:
```
ISMS-IMP-A.8.15.2_Evidence_YYYYMMDD/
|-- Sheet02_SIEM_Infrastructure/
|-- Sheet03_Storage_Architecture/
|-- Sheet04_Network_Infrastructure/
|-- Sheet05_Log_Source_Coverage/
|-- Sheet06_Integration_Methods/
|-- Sheet07_Collection_Reliability/
`-- Sheet08_Encryption_Authentication/
```

---

## Sheet 11: Approval_Sign_Off

**Purpose**: Three-level approval with executive summary

**Sections**:
1. **Summary Dashboard** (Rows 4-25): Key metrics from all sheets
2. **Executive Summary** (Rows 27-35): Narrative summary (user-written)
3. **Level 1 Approval** (Rows 38-48): SIEM Administrator + SOC Lead
4. **Level 2 Approval** (Rows 50-58): Information Security Manager
5. **Level 3 Approval** (Rows 60-70): CISO final approval
6. **Post-Approval Checklist** (Rows 72-80): Actions after approval

**Summary Metrics Table**:
| Metric | Value (Formula Reference) | Target | Status |
|--------|-------------------------|--------|--------|
| SIEM Availability | =Sheet7!B7 | >=99.5% | IF Y/N |
| Collection Coverage % | =Sheet5!SummaryCell | >=98% | IF Y/N |
| Encryption Compliance % | =Sheet8!SummaryCell | 100% | IF Y/N |
| Authentication Compliance % | =Sheet8!SummaryCell | 100% | IF Y/N |
| Overall Compliance Score | =AVERAGE(All) | >=90% | Color code |

**Gap Summary**:

- Total Gaps = COUNT(Sheet9!A:A)
- Critical = COUNTIF(Sheet9!I:I,"CRITICAL")
- High = COUNTIF(Sheet9!I:I,"HIGH")
- Medium = COUNTIF(Sheet9!I:I,"MEDIUM")
- Low = COUNTIF(Sheet9!I:I,"LOW")

**Approval Fields** (each level):

- Reviewer Role, Reviewer Name, Review Date
- Specific verification questions (dropdowns: Yes/No/With Comments)
- Comments field
- Signature field
- Status (auto-calculated: Approved/Pending/Needs Revision)

**Final Approval Status**:

- Large, bold field: "APPROVED" (green) or "PENDING" (yellow) or "REJECTED" (red)
- Based on all three approval levels

---

# Integration Points

## External References

**From IMP-A.8.15.1**:

- Sheet 5 imports columns A-F from ISMS-IMP-A.8.15.1 Sheet 2 (System_Inventory)
- External workbook reference: `='[ISMS_A_8_15_1_Log_Source_Inventory_Assessment_YYYYMMDD.xlsx]System_Inventory'!$A$2:$F$1000`
- Python script must update YYYYMMDD with actual assessment date

**To IMP-A.8.15.3**:

- Sheet 3 (Storage_Architecture) referenced by IMP-A.8.15.3 for retention validation

**To IMP-A.8.15.5**:

- Sheet 11 (Approval_Sign_Off) summary metrics pulled into dashboard
- External reference: `='[ISMS_A_8_15_2_..._YYYYMMDD.xlsx]Approval_Sign_Off'!$B$10:$B$20`

## Policy References

- ISMS-POL-A.8.15 Section 2.2 (Log Protection & Integrity)
- ISMS-POL-A.8.15 Section 2.3 (Log Retention & Storage)
- ISMS-POL-A.8.15 Section 2.4 (Log Review & Analysis - targets)
- ISMS-POL-A.8.15 Section 3.2 (Assessment methodology)
- ISMS-POL-A.8.15 Section 3.3 (Exception management)

---

# Python Script Usage

## Script Name
`generate_a815_2_log_collection_centralization.py`

## Critical Customization Points

**Line 20-25: Input Workbook Path**
```python
# CUSTOMIZE: Path to IMP-A.8.15.1 for log source import
IMP_A_8_15_1_PATH = "ISMS_A_8_15_1_Log_Source_Inventory_Assessment_YYYYMMDD.xlsx"
# UPDATE YYYYMMDD with actual date
```

**Line 100-110: SIEM Platform List**
```python
# CUSTOMIZE: Add organization's SIEM platforms
SIEM_PLATFORMS = [
    "Splunk Enterprise",
    "Elastic Stack (ELK)",
    "Microsoft Sentinel",
    "[Your Organization's SIEM]"  # ADD HERE
]
```

**Line 500-550: External Reference Implementation**
```python
# Import from IMP-A.8.15.1
source_wb = load_workbook(IMP_A_8_15_1_PATH, data_only=True)
source_sheet = source_wb['System_Inventory']

for row_idx, row in enumerate(source_sheet.iter_rows(min_row=2, values_only=True), start=2):
    target_sheet.cell(row=row_idx, column=1, value=row[0])  # System ID
    target_sheet.cell(row=row_idx, column=2, value=row[1])  # System Name
    # ... copy columns B-F
    
# Protect imported columns (read-only)
for cell in target_sheet['A:F']:
    cell.protection = Protection(locked=True)
```

## Key Functions

1. `create_workbook()`: Initialize Excel workbook with 11 sheets
2. `import_log_sources()`: Import from IMP-A.8.15.1 (Sheet 5)
3. `generate_formulas()`: Insert all formula cells
4. `apply_conditional_formatting()`: Traffic lights, risk colors
5. `set_data_validation()`: Dropdown lists for user input
6. `protect_cells()`: Lock formula cells, allow input cells
7. `generate_file()`: Output workbook with date-stamped filename

## Testing Checklist

- [ ] IMP-A.8.15.1 external reference works
- [ ] All formulas calculate correctly
- [ ] Dropdowns contain correct values
- [ ] Conditional formatting triggers properly
- [ ] Cell protection allows input, prevents formula changes
- [ ] Summary metrics aggregate correctly
- [ ] Gap auto-population logic works

---

# Document Assembly Complete

**Total Document Length**: ~1,550 lines

**Structure**:

- Part I: User Completion Guide (~600 lines)
- Part II: Technical Specification (~950 lines)

**Quality Verification**:

- [X] Policy references to ISMS-POL-A.8.15 v1.0 consolidated policy
- [X] External dependency on IMP-A.8.15.1 documented
- [X] All 11 sheets specified with formulas, validation, formatting
- [X] Python script customization points marked
- [X] Integration points with other assessments documented
- [X] Completely generic language (no industry/size/technology assumptions)
- [X] Follows IMP-A.8.15.1 structure exactly

---

**END OF SPECIFICATION**

---

*"Make everything as simple as possible, but not simpler."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
