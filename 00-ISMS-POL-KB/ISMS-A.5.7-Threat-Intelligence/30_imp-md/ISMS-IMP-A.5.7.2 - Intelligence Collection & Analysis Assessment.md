# ISMS-IMP-A.5.7.2
## Intelligence Collection & Analysis Assessment

**Document ID**: ISMS-IMP-A.5.7.2  
**Title**: Intelligence Collection & Analysis Assessment - Implementation Specification  
**Version**: 1.0  
**Date**: [Date]
**Classification**: Internal  
**Owner**: Threat Intelligence Team Lead  
**Status**: Draft

---

## 1. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial consolidated specification (14 sheets) |

**Review Cycle**: Quarterly  
**Next Review Date**: [Date + 3 months] 
**Related Policy**: ISMS-POL-A.5.7-S2 (Threat Intelligence Requirements)

---

## 2. Purpose & Objectives

### 2.1 Purpose

Assess the organization's capability to collect, analyze, and produce actionable threat intelligence across strategic, tactical, and operational levels.

### 2.2 Assessment Objectives

1. **Collection Coverage**: Evaluate breadth/depth of intelligence collection
2. **Analysis Capability**: Assess analytical skills and methodologies
3. **Production Quality**: Measure intelligence output quality and timeliness
4. **Process Maturity**: Benchmark against industry best practices
5. **Integration Effectiveness**: Verify Control 8.8 (Vulnerability Management) linkage
6. **CVSS Integration**: Quantify vulnerability-threat linkages with CVSS scoring
7. **Actor Profiling**: Maintain threat actor knowledge base
8. **Campaign Tracking**: Track and analyze threat campaigns

---

## 3. Scope

### 3.1 In Scope

- Intelligence collection workflows (automated and manual)
- Analysis methodologies (MITRE ATT&CK mapping, diamond model, kill chain)
- Intelligence production (reports, briefings, alerts)
- Analyst training and capability development
- Quality metrics and KPIs
- Integration with vulnerability management (Control 8.8)
- **CVSS-based vulnerability-threat linkage**
- **Threat actor profiling and tracking**
- **Campaign analysis and monitoring**

### 3.2 Out of Scope

- Individual source evaluation (covered in ISMS-IMP-A.5.7.1)
- Dissemination mechanisms (covered in ISMS-IMP-A.5.7.3)
- Incident response procedures (separate ISMS control)

---

## 4. Workbook Structure

### 4.1 Sheet Overview (14 Sheets)

| Sheet # | Sheet Name | Purpose | Links To |
|---------|------------|---------|----------|
| 1 | Instructions | User guide | N/A |
| 2 | Collection_Coverage | Sources mapped to requirements | 5.7.1 |
| 3 | Analysis_Framework | Methodologies and tools used | N/A |
| 4 | Analyst_Capabilities | Skills matrix and training | N/A |
| 5 | Intelligence_Production | Output tracking and quality | Sheet 2, 3 |
| 6 | MITRE_Mapping | ATT&CK technique coverage | Common_Enums |
| 7 | Quality_Metrics | KPIs and performance tracking | Sheet 5 |
| 8 | Vulnerability_Linked_Threats | **Integration with Control 8.8 + CVSS** | VTL Schema |
| 9 | Process_Maturity | Capability maturity assessment | N/A |
| 10 | Action_Items | Capability improvement tasks | Sheets 2-9 |
| 11 | **Analysis_Tools** | Analysis tools and platforms | N/A |
| 12 | **Threat_Actor_Profiles** | Known threat actor knowledge base | Sheet 13 |
| 13 | **Campaign_Tracking** | Threat campaign monitoring | Sheet 8, 12 |
| 14 | Metadata | Workbook generation info | N/A |

---
## 5. Sheet Specifications

### 5.1 Sheet 1: Instructions

**Purpose**: Guide users through the workbook structure and data entry requirements

**Content**:
- Workbook overview (14 sheets)
- Data entry instructions
- CVSS integration in Sheet 8
- Integration points with Control 8.8
- Data validation rules
- Color coding legend
- Contact information for Threat Intelligence Team

---

### 5.2 Sheet 2: Intelligence_Requirements

**Purpose**: Map collection capabilities to intelligence requirements

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Requirement_ID | Text | Auto-generated (REQ-NNN) | Yes | REQ-001 |
| Intelligence_Type | Dropdown | Strategic, Tactical, Operational, Technical | Yes | Tactical |
| Requirement_Description | Text | Free text (max 300 chars) | Yes | APT campaign targeting financial sector |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Target_Sector | Dropdown | Financial, Healthcare, Energy, Government, Technology, Other | No | Financial |
| Target_Region | Dropdown | Global, Europe, Americas, Asia_Pacific, Middle_East, Africa | No | Europe |
| Threat_Category | Dropdown | APT_Campaign, Ransomware, Data_Breach, DDoS, Supply_Chain, Insider, Other | Yes | APT_Campaign |
| Collection_Source_1 | Text | Reference to 5.7.1 | No | SRC-001 |
| Collection_Source_2 | Text | Reference to 5.7.1 | No | SRC-005 |
| Collection_Source_3 | Text | Reference to 5.7.1 | No | N/A |
| Collection_Method | Dropdown | Automated_Feed, Manual_Research, OSINT, Partnership, Internal_Telemetry | Yes | Automated_Feed |
| Coverage_Status | Formula | IF >= 2 sources: Adequate, =1: Minimal, =0: Gap | Auto | Adequate |
| Collection_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| Last_Collected | Date | DD.MM.YYYY | No | 02.01.2025 |
| Gap_Identified | Formula | IF Coverage_Status=Gap: Yes | Auto | No |
| Gap_Remediation | Text | If Gap_Identified=Yes | Conditional | N/A |
| Responsible_Analyst | Text | Email or name | Yes | ti.analyst@example.com |
| Notes | Text | Free text | No | Primary coverage from commercial TI platform |

**Conditional Formatting**:
- Coverage_Status "Gap" → Red background
- Coverage_Status "Minimal" → Yellow background
- Priority "Critical" + Coverage_Status "Gap" → Bold red background

---

### 5.3 Sheet 3: Collection_Sources

**Purpose**: Document intelligence collection sources and their characteristics

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Text | Auto-generated (SRC-NNN) | Yes | SRC-001 |
| Source_Name | Text | Free text | Yes | CrowdStrike Falcon Intelligence |
| Source_Type | Dropdown | Commercial_Feed, Open_Source, Government, Industry_Partnership, Internal | Yes | Commercial_Feed |
| Data_Format | Dropdown | STIX, JSON, CSV, RSS, API, Email, Portal | Yes | STIX |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| Coverage_Geographic | Text | Comma-separated regions | No | Global |
| Coverage_Sector | Text | Comma-separated sectors | No | All |
| Coverage_Threat_Types | Text | Free text | Yes | APT, Ransomware, Malware, Vulnerabilities |
| Integration_Status | Dropdown | Integrated, Manual, Planned, Deprecated | Yes | Integrated |
| Integration_Platform | Text | TIP name if integrated | No | MISP |
| Cost_Annual | Currency | >= 0, 2 decimals | No | 75000.00 |
| Contract_Expiry | Date | DD.MM.YYYY | No | 31.12.2025 |
| Primary_Contact | Text | Vendor contact | No | support@crowdstrike.com |
| Data_Quality_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Notes | Text | Free text | No | Critical source for APT intelligence |

**Conditional Formatting**:
- Integration_Status "Deprecated" → Gray background
- Contract_Expiry within 60 days → Yellow background
- Data_Quality_Rating "Poor" → Red background

---

### 5.4 Sheet 4: Raw_Intelligence_Log

**Purpose**: Track raw intelligence ingestion for audit trail

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Log_ID | Text | Auto-generated (LOG-YYYYMMDD-NNNN) | Yes | LOG-20250109-0001 |
| Timestamp | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 14:30 |
| Source_ID | Dropdown | From Sheet 3 | Yes | SRC-001 |
| Intelligence_Type | Dropdown | IOC, Vulnerability, Campaign, Threat_Actor, TTP, Malware, Other | Yes | Vulnerability |
| Raw_Data_Summary | Text | Free text (max 500 chars) | Yes | CVE-2024-12345 active exploitation by APT28 |
| Confidence_Level | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Classification | Dropdown | TLP_RED, TLP_AMBER, TLP_GREEN, TLP_WHITE | Yes | TLP_AMBER |
| Priority | Dropdown | Critical, High, Medium, Low, Info | Yes | Critical |
| Processed_Status | Dropdown | Pending, In_Analysis, Completed, Discarded | Yes | Pending |
| Assigned_Analyst | Text | Email | Yes | analyst@example.com |
| Analysis_Deadline | Date | DD.MM.YYYY | No | 10.01.2025 |
| Related_Requirements | Text | Comma-separated REQ IDs | No | REQ-001, REQ-005 |
| Notes | Text | Free text | No | Requires urgent analysis |

**Conditional Formatting**:
- Priority "Critical" + Processed_Status "Pending" → Red background
- Analysis_Deadline overdue → Bold red

---

### 5.5 Sheet 5: Intelligence_Production

**Purpose**: Track intelligence products and quality metrics

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Product_ID | Text | Auto-generated (PROD-YYYYMMDD-NN) | Yes | PROD-20250109-01 |
| Product_Type | Dropdown | Strategic_Report, Tactical_Brief, Technical_Alert, IOC_Feed, Campaign_Analysis, Threat_Profile | Yes | Tactical_Brief |
| Product_Title | Text | Free text | Yes | APT28 Credential Harvesting Campaign Q1 2025 |
| Intelligence_Level | Dropdown | Strategic, Operational, Tactical | Yes | Tactical |
| Production_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Author | Text | Analyst name | Yes | Senior TI Analyst |
| Reviewer | Text | Reviewer name | No | TI Team Lead |
| Target_Audience | Dropdown | Executive, Technical, SOC, IT_Ops, All_Staff | Yes | Technical |
| Distribution_Method | Dropdown | Email, Portal, API, Briefing, Report | Yes | Email |
| Sources_Used | Text | Comma-separated Source IDs | Yes | SRC-001, SRC-003, SRC-007 |
| Requirements_Addressed | Text | Comma-separated REQ IDs | Yes | REQ-001, REQ-004 |
| Timeliness_Target_Hours | Number | Integer >= 0 | Yes | 24 |
| Actual_Production_Hours | Number | Integer >= 0 | Yes | 18 |
| Timeliness_Met | Formula | IF Actual <= Target: Yes | Auto | Yes |
| Quality_Score | Dropdown | Excellent, Good, Acceptable, Poor | No | Excellent |
| Feedback_Received | Dropdown | Positive, Neutral, Negative, None | No | Positive |
| Actionable_Items | Number | Integer >= 0 | Yes | 5 |
| Actions_Implemented | Number | Integer >= 0 | Yes | 4 |
| Impact_Rating | Dropdown | High, Medium, Low, Unknown | No | High |
| Notes | Text | Free text | No | Led to emergency patching of 15 servers |

**Conditional Formatting**:
- Timeliness_Met "No" → Yellow background
- Quality_Score "Poor" → Red background
- Impact_Rating "High" + Actions_Implemented > 0 → Green background

---

### 5.6 Sheet 6: Coverage_Matrix

**Purpose**: Map MITRE ATT&CK technique coverage

**Structure**: Matrix format with tactics and techniques

**Columns**:
- MITRE_Tactic (Column A)
- MITRE_Technique_ID (Column B)
- Technique_Name (Column C)
- Coverage_Status (Dropdown: Covered, Partial, Gap)
- Sources_Covering (Text: Comma-separated)
- Detection_Capability (Dropdown: High, Medium, Low, None)
- Last_Seen_In_Wild (Date)
- Priority_For_Coverage (Dropdown: Critical, High, Medium, Low)
- Gap_Remediation_Plan (Text)

**Conditional Formatting**:
- Coverage_Status "Gap" + Priority "Critical" → Red background
- Detection_Capability "None" + Last_Seen_In_Wild < 90 days → Orange background

---

### 5.7 Sheet 7: Quality_Metrics

**Purpose**: Track key performance indicators

**Metrics**:

| Metric | Target | Actual | Status | Notes |
|--------|--------|--------|--------|-------|
| Collection_Sources_Active | Number | Number | Formula | Count from Sheet 3 |
| Average_Intelligence_Timeliness | Hours | Formula | Auto | From Sheet 5 |
| Requirements_Coverage_Percent | % | Formula | Auto | From Sheet 2 |
| VTL_Records_Created_MTD | Number | Formula | Auto | From Sheet 8 |
| Critical_VTL_Response_Time_Hours | Number | Number | Manual | Target < 4 hours |
| Products_Published_MTD | Number | Formula | Auto | From Sheet 5 |
| Analyst_Training_Completion_Percent | % | Formula | Auto | From Sheet 9 |
| MITRE_Technique_Coverage_Percent | % | Formula | Auto | From Sheet 6 |
| Threat_Actor_Profiles_Active | Number | Formula | Auto | From Sheet 12 |
| Campaigns_Tracked_Active | Number | Formula | Auto | From Sheet 13 |

**Conditional Formatting**:
- Status "Below Target" → Red background
- Status "At Target" → Green background

---

### 5.8 Sheet 8: Vulnerability_Linked_Threats (CVSS INTEGRATED)

**PURPOSE**: **CRITICAL INTEGRATION WITH CONTROL 8.8 + CVSS SCORING**

This sheet implements the VulnerabilityThreatLink schema with CVSS integration for quantified risk-based prioritization.

**CVSS Integration**: 
- ✅ Added CVSS_Version column (3)
- ✅ Added CVSS_Base_Score column (4)
- ✅ Added CVSS_Vector column (5)
- ✅ Priority_Score now AUTO-CALCULATED from CVSS + threat factors

**Column Specifications** (24 columns, expanded from 21):

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Link_ID | Text | Auto-generated (VTL-YYYYMMDD-NNNN) | Yes | VTL-20250109-0001 |
| Vulnerability_ID | Text | CVE-YYYY-NNNNN or internal | Yes | CVE-2024-12345 |
| **CVSS_Version** | **Dropdown** | **4.0, 3.1** | **Yes** | **4.0** |
| **CVSS_Base_Score** | **Number** | **0.0-10.0, 1 decimal** | **Yes** | **9.3** |
| **CVSS_Vector** | **Text** | **Max 200 chars** | **Yes** | **CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N** |
| Threat_Actor | Text | Free text | No | APT28 (Fancy Bear) |
| Threat_Actor_Type | Dropdown | Nation-State, Organized_Crime, Hacktivist, Insider, Opportunistic, Unknown | No | Nation-State |
| Exploitation_Status | Dropdown | No_Known_Exploit, PoC_Available, Active_Exploitation, Mass_Exploitation | Yes | Active_Exploitation |
| Intelligence_Source | Text | Source_ID from 5.7.1 | Yes | SRC-001 |
| Confidence_Level | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Discovery_Date | Date | DD.MM.YYYY | Yes | 01.01.2025 |
| Last_Updated | Date | Auto TODAY() | Yes | 09.01.2025 |
| IOCs | Text | Comma-separated | No | 192.0.2.100, malicious.example.com |
| TTPs | Text | Comma-separated MITRE IDs | No | T1190, T1059 |
| Attack_Vector | Text | Free text | No | Network - Remote unauthenticated |
| **Priority_Score** | **Formula** | **AUTO-CALC** | **Auto** | **14.3 → 10.0** |
| Remediation_Urgency | Dropdown | Critical, High, Medium, Low, Info | Yes | Critical |
| Business_Impact | Text | Free text | No | Would expose customer PII database |
| Affected_Systems_Count | Number | Integer >= 0 | No | 47 |
| Critical_Assets_Affected | Dropdown | Yes, No | Yes | Yes |
| Remediation_Status | Dropdown | Open, In_Progress, Patched, Mitigated, Risk_Accepted, Verified | Yes | Open |
| Assigned_To | Text | Email or team | No | Infrastructure Team |
| Related_Incidents | Text | Comma-separated IDs | No | INC-2025-001 |
| Notes | Text | Max 500 chars | No | CISA KEV listing, emergency patching required |

**Priority_Score Formula** (Column 16):

=MIN(10, 
    [CVSS_Base_Score] 
    + IF([Exploitation_Status]="Mass_Exploitation", 2, 
         IF([Exploitation_Status]="Active_Exploitation", 1, 0))
    + IF([Critical_Assets_Affected]="Yes", 2, 0)
    + IF([Threat_Actor_Type]="Nation-State", 1, 0)
)


**Example Calculations**:
- CVSS 9.3 + Mass Exploitation (2) + Critical Assets (2) + Nation-State (1) = 14.3 → **Capped at 10.0**
- CVSS 6.5 + Active Exploitation (1) + No Critical Assets (0) + Organized Crime (0) = **7.5**
- CVSS 4.2 + PoC Available (0) + Critical Assets (2) + Opportunistic (0) = **6.2**

**Conditional Formatting (CVSS-based)**:
- **CVSS_Base_Score >= 9.0** → Red background (Critical severity)
- **CVSS_Base_Score >= 7.0 AND < 9.0** → Orange background (High severity)
- **CVSS_Base_Score >= 4.0 AND < 7.0** → Yellow background (Medium severity)
- **CVSS_Base_Score < 4.0** → Green background (Low severity)
- **CVSS >= 9.0 AND Exploitation_Status = "Mass_Exploitation"** → **BRIGHT RED + BOLD** (Emergency)
- **CVSS >= 7.0 AND Exploitation_Status = "Active_Exploitation"** → **RED + BOLD** (Emergency)
- Exploitation_Status "Active" + Critical_Assets "Yes" → Bright red background
- Remediation_Status "Verified" → Green background
- Remediation_Status "Open" + Priority >= 8 → Bold red

**Integration Workflow**:
1. TI analyst discovers active exploitation → Creates VTL record with CVSS score
2. Priority_Score auto-calculated from CVSS + threat intelligence factors
3. VTL record automatically flags in Control 8.8 vulnerability workbook
4. High CVSS + active exploitation triggers emergency patching workflow
5. Vulnerability manager updates remediation_status
6. Status syncs back to this sheet for TI tracking
7. Closed-loop validation with quantified risk metrics

---

### 5.9 Sheet 9: Analyst_Capabilities

**Purpose**: Track analyst skills and training

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Analyst_ID | Text | Auto-generated (ANL-NNN) | Yes | ANL-001 |
| Analyst_Name | Text | Free text | Yes | Jane Smith |
| Role | Dropdown | Senior_Analyst, Mid_Analyst, Junior_Analyst, Team_Lead, Manager | Yes | Mid_Analyst |
| Primary_Focus | Dropdown | Tactical_Analysis, Strategic_Analysis, Technical_Analysis, Dissemination | Yes | Tactical_Analysis |
| Hire_Date | Date | DD.MM.YYYY | Yes | 15.03.2022 |
| Certifications | Text | Comma-separated | No | GCTI, GIAC, CISSP |
| Training_Completed | Text | Comma-separated courses | No | MITRE ATT&CK, Threat Hunting |
| Training_Hours_YTD | Number | Integer >= 0 | Yes | 40 |
| Training_Target_Hours_Annual | Number | Integer >= 0 | Yes | 80 |
| Training_On_Track | Formula | IF Actual >= Target: Yes | Auto | Yes |
| Skills_MITRE_ATT&CK | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Skills_Malware_Analysis | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Intermediate |
| Skills_OSINT | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Skills_Scripting | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Intermediate |
| Skills_Reporting | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Workload_Current | Dropdown | Overloaded, High, Normal, Low | Yes | Normal |
| Reports_Authored_MTD | Number | Integer >= 0 | Yes | 5 |
| VTL_Records_Created_MTD | Number | Integer >= 0 | Yes | 12 |
| Quality_Rating_Avg | Dropdown | Excellent, Good, Acceptable, Needs_Improvement | No | Good |
| Notes | Text | Free text | No | Strong OSINT and reporting skills |

**Conditional Formatting**:
- Workload_Current "Overloaded" → Red background
- Training_On_Track "No" → Yellow background
- Quality_Rating "Needs_Improvement" → Orange background

---

### 5.10 Sheet 10: Action_Items

**Purpose**: Track improvement actions from assessments

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Action_ID | Text | Auto-generated (ACT-YYYYMMDD-NN) | Yes | ACT-20250109-01 |
| Action_Type | Dropdown | Process_Improvement, Tool_Integration, Training, Coverage_Gap, Integration, CVSS_Quality, Other | Yes | Coverage_Gap |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Description | Text | Free text (max 500 chars) | Yes | Add threat intelligence source for Asia-Pacific region |
| Source_Sheet | Dropdown | Sheet 2-13 | Yes | Sheet 2 |
| Responsible_Party | Text | Email or role | Yes | TI Team Lead |
| Due_Date | Date | DD.MM.YYYY | Yes | 31.01.2025 |
| Status | Dropdown | Open, In_Progress, Blocked, Completed, Cancelled | Yes | In_Progress |
| Progress_Percent | Number | 0-100% | No | 60% |
| Budget_Required | Currency | >= 0, 2 decimals | No | 5000.00 |
| Budget_Approved | Dropdown | Yes, No, Pending, N/A | No | Yes |
| Completion_Date | Date | DD.MM.YYYY | No | N/A |
| Impact_Expected | Dropdown | High, Medium, Low | Yes | High |
| Notes | Text | Free text | No | Evaluating 3 potential vendors |

**Conditional Formatting**:
- Priority "Critical" + Status "Open" → Red background
- Due_Date overdue + Status != "Completed" → Bold red
- Status "Completed" → Green background

---### 5.11 Sheet 11: Analysis_Tools

**Purpose**: Document threat intelligence analysis tools and platforms

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Tool_ID | Text | Auto-generated (TOOL-NNN) | Yes | TOOL-001 |
| Tool_Name | Text | Free text | Yes | MITRE ATT&CK Navigator |
| Tool_Category | Dropdown | TIP, SIEM, Malware_Analysis, OSINT, Collaboration, Visualization, Scripting, Other | Yes | Visualization |
| Vendor | Text | Free text | No | MITRE Corporation |
| License_Type | Dropdown | Commercial, Open_Source, Freeware, Internal_Developed | Yes | Open_Source |
| Primary_Users | Text | Free text | No | All TI analysts |
| Use_Cases | Text | Max 300 chars | Yes | Mapping adversary TTPs to ATT&CK framework |
| Integration_Status | Dropdown | Integrated, Standalone, Planned, Deprecated | Yes | Integrated |
| Data_Sources | Text | Free text | No | MITRE ATT&CK knowledge base |
| CVSS_Support | Dropdown | Yes, No, N/A | Yes | N/A |
| Last_Updated | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Version | Text | Free text | No | v11.1 |
| Training_Required | Dropdown | Yes, No | Yes | Yes |
| Training_Status | Text | Free text | No | 5/8 analysts trained |
| Cost_Annual | Currency | >= 0, 2 decimals | No | 0.00 |
| Notes | Text | Max 500 chars | No | Free tool from MITRE, essential for TTP mapping |

**Conditional Formatting**:
- Integration_Status "Deprecated" → Gray background
- Training_Required "Yes" + Training_Status shows incomplete (e.g., "3/8") → Yellow background
- CVSS_Support "Yes" → Green background

**Tool Categories Explained**:
- **TIP**: Threat Intelligence Platform (e.g., MISP, OpenCTI, ThreatConnect)
- **SIEM**: Security Information and Event Management (e.g., Splunk, QRadar)
- **Malware_Analysis**: Malware sandboxes and analysis tools (e.g., Cuckoo, ANY.RUN)
- **OSINT**: Open Source Intelligence tools (e.g., Shodan, Maltego, theHarvester)
- **Collaboration**: Team collaboration platforms (e.g., Slack, Microsoft Teams)
- **Visualization**: Data visualization tools (e.g., ATT&CK Navigator, D3.js)
- **Scripting**: Automation and scripting environments (e.g., Python, PowerShell)

---

### 5.12 Sheet 12: Threat_Actor_Profiles

**Purpose**: Maintain profiles of known threat actors targeting organization or sector

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Actor_ID | Text | Auto-generated (ACTOR-NNN) | Yes | ACTOR-001 |
| Actor_Name | Text | Free text | Yes | APT28 (Fancy Bear) |
| Actor_Aliases | Text | Free text | No | Sofacy, Sednit, STRONTIUM |
| Actor_Type | Dropdown | Nation-State, Organized_Crime, Hacktivist, Insider, Opportunistic, Unknown | Yes | Nation-State |
| Attribution_Confidence | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Country_of_Origin | Text | Free text | No | Russia |
| First_Observed | Date | DD.MM.YYYY | No | 01.01.2007 |
| Last_Activity | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Targeting_Our_Sector | Dropdown | Yes, No, Unknown | Yes | Yes |
| Targeting_Our_Org | Dropdown | Confirmed, Suspected, No, Unknown | Yes | Suspected |
| Primary_Motivation | Dropdown | Espionage, Financial, Disruption, Ideology, Unknown | Yes | Espionage |
| Sophistication_Level | Dropdown | Advanced, Moderate, Low | Yes | Advanced |
| Primary_TTPs | Text | Comma-separated MITRE IDs | No | T1566.001, T1059.001, T1053.005 |
| Common_Malware | Text | Free text | No | Sofacy, X-Agent, Zebrocy |
| Infrastructure_Notes | Text | Max 500 chars | No | Uses bulletproof hosting, frequently changes C2 |
| CVEs_Exploited | Text | Comma-separated CVE IDs | No | CVE-2023-23397, CVE-2022-30190 |
| VTL_Records_Count | Number | Integer >= 0 | Yes | 5 |
| Related_Campaigns | Text | Comma-separated CAMP IDs | No | CAMP-2024-015, CAMP-2024-022 |
| Last_Update_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Notes | Text | Max 1000 chars | No | GRU Unit 26165, targets government and defense sectors |

**Conditional Formatting**:
- Targeting_Our_Org "Confirmed" → Red background
- Targeting_Our_Org "Suspected" + Targeting_Our_Sector "Yes" → Orange background
- Sophistication_Level "Advanced" + Targeting_Our_Sector "Yes" → Yellow background
- Last_Activity within 90 days + Targeting_Our_Sector "Yes" → Bold

**Integration with Other Sheets**:
- **Sheet 8 (VTL)**: Threat_Actor field can reference Actor_Name from this sheet
- **Sheet 13 (Campaign_Tracking)**: Actor_ID used for VLOOKUP

---

### 5.13 Sheet 13: Campaign_Tracking

**Purpose**: Track and analyze threat campaigns over time

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Campaign_ID | Text | Auto-generated (CAMP-YYYY-NNN) | Yes | CAMP-2024-015 |
| Campaign_Name | Text | Free text | Yes | Winter Vivern Credential Harvesting |
| Actor_ID | Dropdown | From Sheet 12 | No | ACTOR-001 |
| Actor_Name | Formula | =IFERROR(VLOOKUP(Actor_ID, Sheet12, 2, FALSE), "Unknown") | Auto | APT28 (Fancy Bear) |
| Campaign_Start_Date | Date | DD.MM.YYYY | Yes | 15.10.2024 |
| Campaign_End_Date | Date | DD.MM.YYYY or "Ongoing" | No | Ongoing |
| Campaign_Status | Dropdown | Active, Concluded, Dormant, Unknown | Yes | Active |
| Target_Sectors | Text | Free text | Yes | Government, Defense, Think Tanks |
| Target_Geographies | Text | Free text | Yes | Europe, North America |
| Our_Sector_Targeted | Dropdown | Yes, No, Unknown | Yes | No |
| Our_Org_Targeted | Dropdown | Confirmed, Suspected, No, Unknown | Yes | No |
| Primary_Objective | Dropdown | Espionage, Data_Theft, Disruption, Ransomware, Credential_Harvesting, Other | Yes | Credential_Harvesting |
| Attack_Vectors | Text | Free text | Yes | Spearphishing with malicious links |
| TTPs_Used | Text | Comma-separated MITRE IDs | No | T1566.002, T1204.001, T1056.001 |
| CVEs_Exploited | Text | Comma-separated CVE IDs | No | CVE-2023-38831 |
| CVEs_CVSS_Max | Formula | Max CVSS from VTL records | Auto | 7.8 |
| IOCs_Count | Number | Integer >= 0 | Yes | 47 |
| VTL_Records_Created | Number | Integer >= 0 | Yes | 2 |
| Incidents_Our_Org | Number | Integer >= 0 | Yes | 0 |
| Intelligence_Sources | Text | Comma-separated Source IDs | No | SRC-001, SRC-005 |
| Threat_Level | Dropdown | Critical, High, Medium, Low | Yes | Medium |
| Monitoring_Status | Dropdown | Active_Monitoring, Passive_Monitoring, Concluded | Yes | Active_Monitoring |
| Last_Update_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Notes | Text | Max 1000 chars | No | Targeting webmail, using Mockbin for exfiltration |

**CVEs_CVSS_Max Formula** (Column 16):

=IFERROR(
    MAXIFS(
        'Vulnerability_Linked_Threats'!D:D,  # CVSS_Base_Score column
        'Vulnerability_Linked_Threats'!B:B,  # Vulnerability_ID column
        CVEs_Exploited                        # Match any CVE in this campaign
    ), 
    0.0
)

*Note: This is a simplified representation; actual implementation may require array formulas or helper columns*

**Conditional Formatting**:
- Campaign_Status "Active" + Our_Org_Targeted "Confirmed" → Red background
- Campaign_Status "Active" + Our_Org_Targeted "Suspected" → Orange background
- Threat_Level "Critical" → Red text, bold
- Incidents_Our_Org > 0 → Orange background
- CVEs_CVSS_Max >= 9.0 → Red background (Critical vulnerabilities)

**Integration with Other Sheets**:
- **Sheet 8 (VTL)**: CVE data flows to calculate CVEs_CVSS_Max
- **Sheet 12 (Threat_Actor_Profiles)**: Actor_ID VLOOKUP for Actor_Name
- **Sheet 3 (Collection_Sources)**: Intelligence_Sources reference

---

### 5.14 Sheet 14: Metadata

**Purpose**: Workbook generation and versioning information

**Content**:
- Workbook version: 2.0
- Generation date
- Generator script version
- Total sheets: 14
- CVSS integration: Enabled
- Control references: A.5.7, A.8.8
- Review schedule
- Contact information

---

## 6. Data Validation Rules

### 6.1 Standard Dropdowns

**Priority Levels**:
- Critical
- High
- Medium
- Low
- Info (where applicable)

**Status Values**:
- Open
- In_Progress
- Completed
- Blocked
- Cancelled
- Verified

**Confidence Levels**:
- High
- Medium
- Low
- Unconfirmed

**Yes/No/Unknown**:
- Yes
- No
- Unknown
- N/A (where applicable)

**CVSS Versions**:
- 4.0
- 3.1

**Exploitation Status**:
- No_Known_Exploit
- PoC_Available
- Active_Exploitation
- Mass_Exploitation

**Threat Actor Types**:
- Nation-State
- Organized_Crime
- Hacktivist
- Insider
- Opportunistic
- Unknown

---

## 7. Integration Points

### 7.1 Control 5.7 Internal Links

- Sheet 2 (Intelligence_Requirements) ↔ Sheet 3 (Collection_Sources)
- Sheet 3 (Collection_Sources) ↔ Sheet 5 (Intelligence_Production)
- Sheet 4 (Raw_Intelligence_Log) → Sheet 5 (Intelligence_Production)
- Sheet 5 (Intelligence_Production) → Sheet 7 (Quality_Metrics)
- **Sheet 8 (VTL) ↔ Sheet 12 (Threat_Actor_Profiles)**
- **Sheet 8 (VTL) ↔ Sheet 13 (Campaign_Tracking)**
- Sheet 9 (Analyst_Capabilities) → Sheet 7 (Quality_Metrics)
- **Sheet 11 (Analysis_Tools) → Sheet 9 (Analyst_Capabilities)**
- All sheets → Sheet 10 (Action_Items)
- All sheets → Sheet 14 (Metadata)

### 7.2 External Integration: Control 8.8 (Vulnerability Management)

**Bidirectional Data Flow via Sheet 8 (VTL)**:

**5.7 → 8.8 (Threat Context)**:
- Vulnerability_ID (with CVSS)
- CVSS_Version, CVSS_Base_Score, CVSS_Vector
- Threat_Actor
- Exploitation_Status
- Intelligence_Source
- Confidence_Level
- IOCs
- TTPs
- Priority_Score (auto-calculated from CVSS)
- Business_Impact

**8.8 → 5.7 (Remediation Status)**:
- Remediation_Status
- Remediation_Urgency
- Assigned_To
- Affected_Systems_Count
- Related_Incidents

**Emergency Patching Trigger**:
- IF CVSS_Base_Score >= 9.0 AND Exploitation_Status = "Mass_Exploitation"
- IF CVSS_Base_Score >= 7.0 AND Exploitation_Status = "Active_Exploitation" AND Critical_Assets_Affected = "Yes"
- Auto-escalates to Control 8.8 emergency patching workflow

### 7.3 External Integration: Control 5.7.1 (Source Assessment)

- Sheet 3 (Collection_Sources) references Source_IDs from 5.7.1
- Sheet 8 (VTL) Intelligence_Source field references 5.7.1 sources
- Sheet 13 (Campaign_Tracking) Intelligence_Sources references 5.7.1

---

## 8. Formulas Reference

### 8.1 Priority_Score Auto-Calculation (Sheet 8, Column 16)

**Excel Formula**:
excel
=MIN(10, 
    D5 +                                    # CVSS_Base_Score
    IF(H5="Mass_Exploitation", 2, 
       IF(H5="Active_Exploitation", 1, 0)) +  # Exploitation bonus
    IF(T5="Yes", 2, 0) +                    # Critical assets bonus
    IF(G5="Nation-State", 1, 0)             # Nation-state bonus
)


**Components**:
1. **Base**: CVSS_Base_Score (0.0-10.0)
2. **+2**: Mass Exploitation detected
3. **+1**: Active Exploitation detected
4. **+2**: Critical Assets Affected = Yes
5. **+1**: Threat Actor Type = Nation-State
6. **Cap**: MIN(result, 10.0)

**Rationale**:
- Quantifies risk using industry-standard CVSS
- Adds context-specific threat intelligence factors
- Caps at 10.0 to maintain consistency
- Auto-updates when any input changes

### 8.2 Coverage_Status (Sheet 2, Column 12)

excel
=IF(COUNTA(H5:J5)>=2, "Adequate", 
    IF(COUNTA(H5:J5)=1, "Minimal", "Gap"))


### 8.3 Timeliness_Met (Sheet 5, Column 14)

excel
=IF(M5<=L5, "Yes", "No")


### 8.4 Actor_Name VLOOKUP (Sheet 13, Column 4)

excel
=IFERROR(VLOOKUP(C5, 'Threat_Actor_Profiles'!A:B, 2, FALSE), "Unknown")


### 8.5 CVEs_CVSS_Max (Sheet 13, Column 16)

excel
# Simplified - actual implementation may vary
=IFERROR(MAX(
    IF(ISNUMBER(SEARCH(O5, 'Vulnerability_Linked_Threats'!B:B)), 
       'Vulnerability_Linked_Threats'!D:D, 0)
), 0.0)


---

## 9. Conditional Formatting Rules

### 9.1 CVSS-Based Severity (Sheet 8)

| CVSS Range | Color | Severity |
|------------|-------|----------|
| >= 9.0 | Red (#DC143C) | Critical |
| 7.0 - 8.9 | Orange (#FF8C00) | High |
| 4.0 - 6.9 | Yellow (#FFD700) | Medium |
| 0.0 - 3.9 | Green (#90EE90) | Low |

**Emergency Highlight**:
- CVSS >= 9.0 + Exploitation = "Mass_Exploitation" → **BRIGHT RED + BOLD**
- CVSS >= 7.0 + Exploitation = "Active_Exploitation" → **RED + BOLD**

### 9.2 Status-Based Formatting

| Condition | Format | Applies To |
|-----------|--------|------------|
| Status = "Completed" | Green background | All action/task sheets |
| Status = "Overdue" | Bold red | All sheets with dates |
| Priority = "Critical" + Status = "Open" | Red background | All sheets |
| Coverage_Status = "Gap" | Red background | Sheet 2 |
| Threat_Level = "Critical" | Red text, bold | Sheets 8, 13 |

---

## 10. Quality Assurance

### 10.1 Validation Checks

**Pre-Deployment**:
1. ✅ All 14 sheets present
2. ✅ Sheet 8 has 24 columns (including 3 CVSS columns)
3. ✅ Priority_Score formula correct (column 16, Sheet 8)
4. ✅ CVSS conditional formatting applied (Sheet 8)
5. ✅ All dropdowns functional
6. ✅ VLOOKUP formulas have IFERROR wrappers
7. ✅ Sheets 11-13 present with correct structures
8. ✅ Integration references correct (Sheet 13 → Sheet 12)
9. ✅ Python generator script produces error-free workbook
10. ✅ Sanity check script passes

**Post-Generation**:
1. Open workbook in Excel
2. Verify no formula errors (#REF!, #VALUE!, #N/A)
3. Test all dropdowns
4. Verify conditional formatting displays correctly
5. Test CVSS score calculation (enter test data in Sheet 8)
6. Verify VLOOKUP (Sheet 13 Actor_Name from Sheet 12)
7. Check merge cells display properly
8. Verify protected cells cannot be edited
9. Test workbook saves without corruption warnings

---

## 11. Change History

### v1.0 ([Date])

**Initial Release**:
1. 14-sheet workbook covering intelligence collection and analysis
2. CVSS-integrated vulnerability-threat linkage (Sheet 8)
3. Threat actor profiling (Sheet 12)
4. Campaign tracking (Sheet 13)
5. Analysis tools inventory (Sheet 11)
6. Automated priority scoring using CVSS + threat context
7. Bidirectional integration with Control 8.8 (Management of Technical Vulnerabilities)

---

## 12. Usage Guidelines

### 12.1 Data Entry Workflow

1. **Initial Setup**:
   - Sheet 2: Define intelligence requirements
   - Sheet 3: Document collection sources
   - Sheet 11: Document analysis tools
   - Sheet 12: Build threat actor profiles

2. **Daily Operations**:
   - Sheet 4: Log raw intelligence
   - Sheet 8: Create VTL records (with CVSS)
   - Sheet 13: Track campaigns

3. **Regular Production**:
   - Sheet 5: Document intelligence products
   - Sheet 9: Update analyst capabilities
   - Sheet 10: Track action items

4. **Periodic Review**:
   - Sheet 6: MITRE coverage assessment
   - Sheet 7: Quality metrics review
   - Sheet 9: Process maturity assessment

### 12.2 CVSS Data Entry (Sheet 8)

**Required Fields**:
1. Vulnerability_ID (CVE or internal)
2. **CVSS_Version** (4.0 or 3.1)
3. **CVSS_Base_Score** (0.0-10.0, one decimal)
4. **CVSS_Vector** (full vector string)
5. Exploitation_Status
6. Critical_Assets_Affected
7. Threat_Actor_Type (if known)

**Priority_Score Auto-Calculates** - do NOT enter manually!

**CVSS Vector Examples**:
- **CVSS 4.0**: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`
- **CVSS 3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

**Source for CVSS Scores**:
- NVD (National Vulnerability Database): https://nvd.nist.gov
- Vendor security advisories
- Commercial threat intelligence feeds
- CISA KEV (Known Exploited Vulnerabilities): https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### 12.3 Maintenance Schedule

**Daily**:
- Update Sheet 4 (Raw Intelligence Log)
- Update Sheet 8 (VTL) for new exploitations
- Monitor Sheet 13 (Campaign Tracking) for active campaigns

**Weekly**:
- Review Sheet 7 (Quality Metrics)
- Update Sheet 10 (Action Items) progress
- Review Sheet 8 for remediation status updates

**Monthly**:
- Review Sheet 2 (Intelligence Requirements) coverage
- Assess Sheet 9 (Process Maturity)
- Update Sheet 12 (Threat Actor Profiles)

**Quarterly**:
- Complete Sheet 6 (MITRE Mapping) assessment
- Review Sheet 3 (Collection Sources) contracts
- Update Sheet 11 (Analysis Tools) inventory

---

## 13. Audit Evidence

This workbook provides audit evidence for:

**ISO 27001:2022 Control A.5.7**:
- Intelligence requirements documentation (Sheet 2)
- Collection capabilities (Sheet 3)
- Analysis methodologies (Sheet 6)
- Quality metrics (Sheet 7)
- Process maturity (Sheet 9)

**Control A.5.7 ↔ A.8.8 Integration**:
- Vulnerability-threat linkage (Sheet 8 with CVSS)
- Quantified risk scoring (Priority_Score formula)
- Emergency patching triggers (CVSS + exploitation)
- Remediation tracking (bidirectional data flow)

**Key Features**:
- CVSS-based prioritization evidence
- Threat actor intelligence maintenance
- Campaign tracking and analysis
- Tool inventory and training records

---

## 14. Support & Contact

**Workbook Issues**:
- Threat Intelligence Team Lead
- Email: ti-team@[organization].com

**Technical Issues**:
- ISMS Implementation Team
- Email: isms@[organization].com

**Policy Questions**:
- Information Security Manager
- Refer to: ISMS-POL-A.5.7 (Threat Intelligence Policy)

---

**Document Status**: Production  
**Last Updated**: 09.01.2025  
**Next Review**: 09.04.2025