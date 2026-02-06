**ISMS-IMP-A.5.7.3-TG - Intelligence Integration & Distribution Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Intelligence Integration into Security Operations & Distribution to Stakeholders |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.3 (Intelligence Dissemination Requirements), Section 2.4 (Risk Assessment Integration Requirements), Section 2.5 (Incident Management Integration Requirements), Section 2.7 (Effectiveness Measurement Requirements) |
| **Purpose** | Assess effectiveness of threat intelligence integration with security tools, dissemination to stakeholders, and measurement of operational impact including prevention tracking |
| **Target Audience** | Security Operations Manager, SOC Team, Incident Response, Network Security, Threat Intelligence Team, Risk Management, CISO, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (17 sheets) | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.7.3-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_3_Integration_Distribution_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS_A_5_7_3_Integration_Distribution_Assessment_20260121.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only yellow cells editable)
- Macros: None (VBA-free for security)
- External Links: References to A.5.7.1 sources, A.5.7.2 intelligence products

**Total Sheets:** 15

**Tab Colors:**

- Instructions: Blue (#4472C4)
- Integration (Sheets 2-3): Yellow (#FFD966)
- Dissemination (Sheets 4-6): Orange (#FFA500)
- **Prevention Tracking (Sheet 7): Red (#C00000) - AUDIT CRITICAL**
- Feedback & Metrics (Sheets 8-9): Green (#70AD47)
- Tool Details (Sheets 10-11): Teal (#00B0F0)
- Hunting (Sheet 12): Purple (#7030A0)
- **Risk/Incident/Decisions (Sheets 13-15): Red (#C00000) - AUDIT CRITICAL**
- Metadata: Gray (#D9D9D9)

**CRITICAL AUDIT EVIDENCE SHEETS:**

- **Sheet 7: Prevention_Tracking** - ≥3 prevented incidents per quarter
- **Sheet 13: Risk_Assessment_Updates** - ≥3 risk updates per quarter (ISO 27001 Clause 6.1)
- **Sheet 14: Incident_TI_Integration** - ≥70% P1/P2 incidents use TI (Controls A.5.24-5.28)
- **Sheet 15: Intelligence_Driven_Decisions** - ≥5 decisions per quarter

---

## Sheet-by-Sheet Technical Specifications

# Sheet Specifications

## Sheet 2: Tool_Integration_Matrix

**Purpose**: Document TI integration across security stack

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Tool_ID | Text | Auto-generated (TOOL-NNN) | Yes | TOOL-001 |
| Tool_Category | Dropdown | SIEM, EDR, Firewall, Proxy, Email_Gateway, IDS_IPS, TIP, SOAR, Vuln_Scanner, Other | Yes | SIEM |
| Tool_Name | Text | Free text | Yes | Splunk Enterprise Security |
| Vendor | Text | Free text | Yes | Splunk Inc. |
| Version | Text | Free text | No | 7.2.1 |
| Primary_Owner | Text | Email or team | Yes | SOC Team |
| Integration_Status | Dropdown | Fully_Integrated, Partially_Integrated, Planned, Not_Integrated | Yes | Fully_Integrated |
| Integration_Method | Dropdown | API, Feed, Manual_Import, STIX_TAXII, Syslog, Custom_Script | Yes | API |
| Integration_Direction | Dropdown | Inbound, Outbound, Bidirectional | Yes | Inbound |
| Data_Types_Integrated | Text | Comma-separated: IOCs, TTPs, Reports, Alerts, Context | Yes | IOCs, TTPs, Context |
| Automation_Level | Dropdown | Fully_Automated, Semi_Automated, Manual | Yes | Fully_Automated |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| IOC_Types_Supported | Text | Comma-separated: IP, Domain, URL, Hash, Email, Registry, Mutex | Yes | IP, Domain, URL, Hash |
| Last_Successful_Sync | DateTime | DD.MM.YYYY HH:MM | No | 02.01.2025 14:30 |
| Sync_Errors_Last_30_Days | Number | Integer >= 0 | No | 2 |
| False_Positive_Rate | Dropdown | High, Medium, Low, Unknown | No | Low |
| Effectiveness_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Integration_Challenges | Text | Free text | No | Rate limiting on API calls |
| Improvement_Opportunities | Text | Free text | No | Add TTP mapping to correlation rules |
| Integration_Date | Date | DD.MM.YYYY | No | 15.06.2024 |
| Documentation_Link | Text | Hyperlink | No | https://docs.example.com/siem-ti |
| Notes | Text | Free text | No | Primary IOC ingestion point |

**Integration Maturity Levels**:

Fully_Integrated:

- Automated data flow
- No manual intervention
- Error handling in place
- Documented and monitored

Partially_Integrated:

- Some automation
- Requires manual steps
- Limited error handling
- Basic documentation

Planned:

- Requirements defined
- Resources allocated
- Timeline established

Not_Integrated:

- No integration
- May be future consideration

**Conditional Formatting**:

- Integration_Status "Fully_Integrated" → Green
- Integration_Status "Not_Integrated" → Red
- Sync_Errors > 5 → Yellow background
- Effectiveness_Rating "Poor" → Red text

---

## Sheet 3: IOC_Deployment

**Purpose**: Track IOC deployment and detection effectiveness

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| IOC_ID | Text | Auto-generated (IOC-YYYY-NNN) | Yes | IOC-2025-001 |
| IOC_Type | Dropdown | From common_enums.IOCType | Yes | IP Address |
| IOC_Value | Text | Format validation by type | Yes | 192.0.2.100 |
| Intelligence_Source | Dropdown | From 5.7.1.Source_Inventory | Yes | SRC-2025-001 |
| Related_Product_ID | Dropdown | From 5.7.2.Intelligence_Production | No | PROD-2025-015 |
| Threat_Actor | Text | Free text | No | APT28 |
| Associated_Malware | Text | Free text | No | Cobalt Strike |
| MITRE_Technique | Dropdown | From common_enums | No | T1071 - Application Layer Protocol |
| Confidence_Level | Dropdown | High, Medium, Low | Yes | High |
| Severity | Dropdown | Critical, High, Medium, Low, Info | Yes | High |
| TLP_Classification | Dropdown | TLP:CLEAR, GREEN, AMBER, AMBER+STRICT, RED | Yes | TLP:AMBER |
| Deployment_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Deployed_To_Tools | Text | Comma-separated Tool_IDs | Yes | TOOL-001, TOOL-003 |
| Deployment_Method | Dropdown | Automated, Manual, Hybrid | Yes | Automated |
| Expiration_Date | Date | DD.MM.YYYY | No | 02.04.2025 |
| Status | Dropdown | Active, Expired, Withdrawn, Under_Review | Yes | Active |
| Hits_Last_7_Days | Number | Integer >= 0 | No | 0 |
| Hits_Last_30_Days | Number | Integer >= 0 | No | 3 |
| Hits_Total | Number | Integer >= 0 | No | 12 |
| Last_Hit_Date | Date | DD.MM.YYYY | No | 28.12.2024 |
| False_Positive | Dropdown | Yes, No, Under_Investigation | No | No |
| FP_Investigation_Notes | Text | If FP=Yes or Under_Investigation | Conditional | N/A |
| Action_Taken_On_Hit | Dropdown | Alert, Block, Log_Only, Escalate | No | Block |
| Related_Incidents | Text | Comma-separated incident IDs | No | INC-2024-089 |
| Effectiveness_Rating | Formula | Based on hits, FP rate, incidents | Auto | Effective |
| Notes | Text | Free text | No | Associated with known C2 infrastructure |

**Effectiveness Calculation**:

IF Hits_Total > 0 AND False_Positive = No: "Effective"
ELSE IF Hits_Total > 0 AND False_Positive = Yes: "Ineffective"
ELSE IF Hits_Total = 0 AND Days_Deployed > 30: "Ineffective"
ELSE: "Monitoring"

**IOC Lifecycle Management** (calculated fields):

- Days since deployment
- Days until expiration
- Hit rate (hits per day)
- FP rate (FP hits / total hits)

**Conditional Formatting**:

- Status "Active" + Expiration within 7 days → Orange
- Status "Expired" → Gray background
- False_Positive "Yes" → Red background
- Hits_Last_7_Days > 0 → Green highlight
- Effectiveness_Rating "Ineffective" → Red text

---

## Sheet 4: Dissemination_Channels

**Purpose**: Document intelligence distribution methods

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Channel_ID | Text | Auto-generated (CHAN-NNN) | Yes | CHAN-001 |
| Channel_Name | Text | Free text | Yes | TI Weekly Email |
| Channel_Type | Dropdown | Email_List, Portal, Dashboard, API, Briefing, Chat, Ticketing_System | Yes | Email_List |
| Target_Audience | Dropdown | Executive, CISO, SOC, IR_Team, IT_Ops, Developers, All_Staff | Yes | SOC |
| Intelligence_Types | Text | Comma-separated: Strategic, Tactical, Operational, Technical | Yes | Tactical, Technical |
| Delivery_Frequency | Dropdown | Real-time, Daily, Weekly, Monthly, Ad_Hoc | Yes | Weekly |
| Automation_Level | Dropdown | Fully_Automated, Semi_Automated, Manual | Yes | Semi_Automated |
| Distribution_Method | Text | Free text | Yes | Email via Marketing Platform |
| TLP_Max_Allowed | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Active_Status | Dropdown | Active, Suspended, Deprecated | Yes | Active |
| Subscriber_Count | Number | Integer >= 0 | No | 45 |
| Average_Open_Rate | Number | Percentage 0-100 | No | 78 |
| Average_Engagement_Score | Number | 1-5 scale | No | 4.2 |
| Channel_Owner | Text | Email | Yes | ti.team@example.com |
| Technical_Platform | Text | Free text | No | Microsoft Exchange + Power Automate |
| Launch_Date | Date | DD.MM.YYYY | No | 01.01.2024 |
| Last_Distribution | Date | DD.MM.YYYY | No | 02.01.2025 |
| Effectiveness_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Improvement_Opportunities | Text | Free text | No | Add interactive threat dashboard |
| Notes | Text | Free text | No | Primary dissemination channel for SOC |

**Conditional Formatting**:

- Active_Status "Deprecated" → Gray
- Average_Engagement_Score < 3 → Yellow background
- Effectiveness_Rating "Poor" → Red text
- Average_Open_Rate > 75 → Green highlight

---

## Sheet 5: Stakeholder_Registry

**Purpose**: Manage intelligence consumer database

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Stakeholder_ID | Text | Auto-generated (STK-NNN) | Yes | STK-001 |
| Name | Text | Free text | Yes | John Security |
| Email | Text | Email format | Yes | john.security@example.com |
| Department | Dropdown | Executive, IT, Security, Operations, Legal, Compliance, Other | Yes | Security |
| Role | Text | Free text | Yes | SOC Analyst |
| TLP_Clearance | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Intelligence_Interests | Text | Comma-separated: Threat_Actors, Vulnerabilities, Malware, Industry_Trends, Tactics | Yes | Threat_Actors, Malware |
| Preferred_Channels | Text | Comma-separated Channel_IDs | Yes | CHAN-001, CHAN-003 |
| Engagement_Level | Dropdown | High, Medium, Low, Inactive | No | High |
| Average_Feedback_Rating | Number | 1-5 scale (auto-calc) | Auto | 4.5 |
| Last_Engagement_Date | Date | DD.MM.YYYY (auto-calc) | Auto | 02.01.2025 |
| Onboarding_Date | Date | DD.MM.YYYY | Yes | 15.03.2024 |
| Status | Dropdown | Active, On_Leave, Departed | Yes | Active |
| Contact_Preference | Dropdown | Email, Slack, Teams, Portal | No | Email |
| Time_Zone | Text | Standard TZ | No | Europe/Zurich |
| Language_Preference | Dropdown | English, German, French | No | English |
| Notes | Text | Free text | No | Key stakeholder for ransomware intelligence |

**Conditional Formatting**:

- Status "Departed" → Gray background
- Engagement_Level "Inactive" → Yellow
- Average_Feedback_Rating >= 4.5 → Green highlight

---

## Sheet 6: Distribution_Tracking

**Purpose**: Track intelligence distribution and engagement

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Distribution_ID | Text | Auto-generated (DIST-YYYY-NNN) | Yes | DIST-2025-001 |
| Product_ID | Dropdown | From 5.7.2.Intelligence_Production | Yes | PROD-2025-015 |
| Product_Title | Formula | =VLOOKUP | Auto | APT28 Campaign Analysis |
| Intelligence_Type | Formula | =VLOOKUP | Auto | Tactical |
| Distribution_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 02.01.2025 14:00 |
| Channel_ID | Dropdown | From Dissemination_Channels | Yes | CHAN-001 |
| Channel_Name | Formula | =VLOOKUP | Auto | TI Weekly Email |
| Stakeholder_ID | Dropdown | From Stakeholder_Registry | Yes | STK-001 |
| Stakeholder_Name | Formula | =VLOOKUP | Auto | John Security |
| TLP_Classification | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Delivery_Method | Text | Free text | Yes | Email |
| Delivery_Status | Dropdown | Sent, Delivered, Opened, Failed, Bounced | Yes | Opened |
| Open_Date | DateTime | DD.MM.YYYY HH:MM | No | 02.01.2025 14:15 |
| Click_Through | Dropdown | Yes, No | No | Yes |
| Action_Taken | Dropdown | Yes, No, Unknown | No | Yes |
| Action_Description | Text | Free text | Conditional | Deployed IOCs to SIEM |
| Feedback_Received | Dropdown | Yes, No, Pending | No | Yes |
| Feedback_ID | Text | Link to Feedback_Collection | Conditional | FB-2025-001 |
| Engagement_Score | Formula | Based on open, click, action | Auto | High |
| Distribution_Effectiveness | Formula | Auto-calc | Auto | Effective |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Follow_Up_Notes | Text | Conditional | Conditional | N/A |
| Notes | Text | Free text | No | Stakeholder requested similar analysis for APT29 |

**Effectiveness Calculation**:

IF Action_Taken = Yes AND Feedback_Received = Yes: "Highly_Effective"
ELSE IF Action_Taken = Yes: "Effective"
ELSE IF Opened = Yes: "Delivered_But_No_Action"
ELSE: "Not_Engaged"

**Conditional Formatting**:

- Delivery_Status "Failed" or "Bounced" → Red
- Action_Taken "Yes" → Green highlight
- Engagement_Score "High" → Green
- Engagement_Score "Low" → Yellow

---
## Sheet 7: Prevention_Tracking ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document prevented incidents per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)

**KPI Target**: ≥3 validated prevented incidents per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Prevention_ID | Text | Auto-generated (PREV-YYYYQQ-NNN) | Yes | PREV-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Detection_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| CVE_ID | Text | CVE-YYYY-NNNNN format | Yes | CVE-2024-56789 |
| CVSS_Version | Dropdown | 4.0, 3.1 | Yes | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0, 1 decimal | Yes | 9.3 |
| CVSS_Vector | Text | Max 200 chars | Yes | CVSS:4.0/AV:N/AC:L/PR:N/UI:N/S:C/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H |
| Threat_Source | Text | Source_ID or free text | Yes | CISA KEV, SRC-2025-001 |
| Threat_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-003 |
| Exploitation_Status | Dropdown | PoC Available, Active, Mass Exploitation | Yes | Mass Exploitation |
| Before_State | Text | Max 500 chars | Yes | Vulnerability present on 12 web servers |
| Before_Evidence | Text | File path or reference | Yes | Scan-20250115-WebServers.xlsx |
| TI_Alert_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| TI_Alert_Details | Text | Max 500 chars | Yes | CISA KEV Alert: Mass exploitation detected |
| Action_Taken | Text | Max 500 chars | Yes | Emergency patching deployed within 4 hours |
| Action_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| Action_Owner | Text | Email or name | Yes | infrastructure@example.com |
| After_State | Text | Max 500 chars | Yes | All 12 servers patched, vulnerability eliminated |
| After_Evidence | Text | File path or reference | Yes | Scan-20250116-WebServers-Clean.xlsx |
| Validation_Method | Dropdown | Vulnerability_Scan, SIEM_Logs, EDR_Telemetry, Manual_Verification, Multiple | Yes | Multiple |
| Validation_Evidence | Text | File path or reference | Yes | SIEM logs show 23 blocked exploit attempts during patching |
| SIEM_Query_ID | Text | Free text | No | QUERY-2025-0115-001 |
| Time_to_Remediation | Formula | Hours, 1 decimal | Auto | 4.0 |
| Validated_By | Text | Email or name | Yes | jane.analyst@example.com |
| Validation_Date | Date | DD.MM.YYYY | Yes | 16.01.2025 |
| Cost_Avoidance_Estimate | Currency | >=0, 2 decimals | No | 50000.00 |
| Notes | Text | Max 1000 chars | No | Full evidence package prepared for audit |

**Formulas**:

Time_to_Remediation = (Action_Date + Action_Time) - (TI_Alert_Date + TI_Alert_Time)

Convert to hours with 1 decimal.

**Conditional Formatting**:

- CVSS_Base_Score >= 9.0 → Red background (Critical prevented)
- CVSS_Base_Score >= 7.0 → Orange background (High prevented)
- Validation_Evidence empty → Yellow background (needs validation)
- Time_to_Remediation > 72 hours → Orange background (slow response)

**Validation Rules**:

- After_Date must be >= Action_Date
- Validation_Date must be >= After_Date
- All "Evidence" fields must be non-empty for audit

**Audit Evidence Requirements**:

- **Before_Evidence**: Vulnerability scan showing affected systems
- **TI_Alert_Details**: Documented threat intelligence that triggered action
- **After_Evidence**: Validation that vulnerability was remediated
- **Validation_Evidence**: Proof no exploitation occurred
- **Quarterly Target**: Minimum 3 fully documented preventions

---

## Sheet 8: Feedback_Collection

**Purpose**: Capture and analyze stakeholder feedback

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Feedback_ID | Text | Auto-generated (FB-YYYY-NNN) | Yes | FB-2025-001 |
| Distribution_ID | Dropdown | From Distribution_Tracking | Yes | DIST-2025-001 |
| Product_ID | Formula | =VLOOKUP from Distribution | Auto | PROD-2025-015 |
| Stakeholder_ID | Dropdown | From Stakeholder_Registry | Yes | STK-001 |
| Stakeholder_Name | Formula | =VLOOKUP | Auto | John Security |
| Feedback_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 02.01.2025 15:45 |
| Feedback_Method | Dropdown | Survey, Email_Reply, Meeting, Ticket, Call | Yes | Survey |
| Overall_Rating | Number | 1-5 scale | Yes | 5 |
| Relevance_Rating | Number | 1-5 scale | Yes | 5 |
| Timeliness_Rating | Number | 1-5 scale | Yes | 4 |
| Actionability_Rating | Number | 1-5 scale | Yes | 5 |
| Clarity_Rating | Number | 1-5 scale | No | 4 |
| Intelligence_Used | Dropdown | Yes, Partial, No, Will_Use_Later | Yes | Yes |
| Action_Taken | Text | Free text (max 300 chars) | No | Deployed IOCs to SIEM, created detection rules |
| Action_Result | Text | Free text | No | Detected 3 related events, no true positives yet |
| Improvement_Suggestions | Text | Free text | No | Include more context on threat actor motivations |
| Additional_Requirements | Text | Free text | No | Request similar analysis for APT29 |
| Would_Recommend | Dropdown | Yes, Maybe, No | No | Yes |
| Positive_Comments | Text | Free text | No | Excellent TTPs mapping, very actionable |
| Negative_Comments | Text | Free text | No | Could use more IOCs |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Follow_Up_Notes | Text | If Yes | Conditional | N/A |
| Follow_Up_Complete | Dropdown | Yes, No, N/A | Auto | N/A |
| Notes | Text | Free text | No | Stakeholder is highly engaged, key consumer |

**Feedback Analysis** (summary section):

- Average ratings by category
- Sentiment analysis (positive/negative comments)
- Common improvement themes
- Most engaged stakeholders

---

## Sheet 9: Integration_Metrics

**Purpose**: KPIs for integration and dissemination effectiveness

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Metric_ID | Text | Auto-generated (IM-NNN) | Yes | IM-001 |
| Metric_Name | Text | Free text | Yes | IOC Deployment Rate |
| Metric_Category | Dropdown | Tool_Integration, IOC_Effectiveness, Dissemination, Stakeholder_Engagement, Automation, Prevention, Risk_Management | Yes | IOC_Effectiveness |
| Measurement_Period | Dropdown | Daily, Weekly, Monthly, Quarterly | Yes | Monthly |
| Target_Value | Number | Decimal | Yes | 95 |
| Actual_Value | Number | Decimal | Yes | 98 |
| Unit | Text | Free text | Yes | % |
| Performance_vs_Target | Formula | (Actual/Target - 1) * 100 | Auto | +3.2% |
| Status | Formula | Based on performance | Auto | Exceeds_Target |
| Trend | Dropdown | Improving, Stable, Declining | No | Stable |
| Data_Source | Text | Reference to sheet/cell | Yes | =IOC_Deployment!H:H |
| Owner | Text | Email | Yes | soc.manager@example.com |
| Last_Updated | Date | Auto TODAY() | Yes | 02.01.2025 |
| Notes | Text | Free text | No | Consistently meeting target |

**Standard Metrics**:
1. % of security tools with TI integration
2. IOC deployment success rate
3. Average time from IOC publication to deployment
4. IOC hit rate (hits per 100 IOCs)
5. False positive rate for IOCs
6. Intelligence distribution reach (% of target audience)
7. Average stakeholder engagement score
8. Feedback response rate
9. Intelligence consumption rate (% acted upon)
10. Mean time from intelligence to action
11. **Prevented incidents per quarter (Sheet 7)**
12. **Risk assessments updated per quarter (Sheet 13)**
13. **Incident-TI integration rate (Sheet 14)**
14. **Intelligence-driven decisions per quarter (Sheet 15)**

---

## Sheet 10: SIEM_Integration_Details

**Purpose**: Detailed SIEM integration tracking for primary security tool

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (SIEM-INT-NNN) | Yes | SIEM-INT-001 |
| Tool_ID | Dropdown | From Tool_Integration_Matrix (SIEM category only) | Yes | TOOL-001 |
| Tool_Name | Formula | =VLOOKUP | Auto | Splunk Enterprise Security |
| IOC_Feed_Name | Text | Free text | Yes | STIX Feed - Malware Hashes |
| Feed_Type | Dropdown | STIX_TAXII, CSV_Feed, API, Manual | Yes | STIX_TAXII |
| Feed_URL | Text | URL | No | https://taxii.example.com/collections/malware |
| Authentication_Method | Dropdown | API_Key, OAuth, Certificate, Basic_Auth, None | Yes | API_Key |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly | Yes | Hourly |
| Last_Successful_Pull | DateTime | DD.MM.YYYY HH:MM | No | 09.01.2025 14:00 |
| Last_Error_Date | DateTime | DD.MM.YYYY HH:MM | No | 08.01.2025 23:15 |
| Error_Details | Text | Free text | No | SSL certificate validation failed |
| IOCs_Ingested_Last_24h | Number | Integer >= 0 | No | 487 |
| IOCs_Active_Total | Number | Integer >= 0 | No | 12450 |
| Detection_Rules_Created | Number | Integer >= 0 | No | 23 |
| Correlation_Searches_Updated | Number | Integer >= 0 | No | 15 |
| Alerts_Generated_Last_30d | Number | Integer >= 0 | No | 145 |
| True_Positive_Rate | Number | Percentage 0-100 | No | 78 |
| Integration_Health | Dropdown | Healthy, Degraded, Down, Maintenance | Yes | Healthy |
| Monitoring_Dashboard | Text | URL | No | https://siem.example.com/dashboard/ti-health |
| Owner | Text | Email | Yes | soc.team@example.com |
| Notes | Text | Free text | No | Primary threat feed for malware detection |

**Conditional Formatting**:

- Integration_Health "Down" → Red background
- Integration_Health "Degraded" → Yellow background
- True_Positive_Rate < 50% → Yellow background
- Last_Successful_Pull > 24 hours ago → Orange background

---

## Sheet 11: EDR_Integration_Details

**Purpose**: Detailed EDR integration tracking for endpoint security

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (EDR-INT-NNN) | Yes | EDR-INT-001 |
| Tool_ID | Dropdown | From Tool_Integration_Matrix (EDR category only) | Yes | TOOL-002 |
| Tool_Name | Formula | =VLOOKUP | Auto | CrowdStrike Falcon |
| IOC_Feed_Name | Text | Free text | Yes | Custom Threat Intel Feed |
| Feed_Type | Dropdown | API, Hash_List, Watchlist, Custom_Indicator, Manual | Yes | API |
| Feed_URL | Text | URL | No | https://api.crowdstrike.com/iocs |
| Authentication_Method | Dropdown | API_Key, OAuth, Certificate, Basic_Auth | Yes | OAuth |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly | Yes | Real-time |
| Last_Successful_Push | DateTime | DD.MM.YYYY HH:MM | No | 09.01.2025 14:30 |
| Last_Error_Date | DateTime | DD.MM.YYYY HH:MM | No | N/A |
| Error_Details | Text | Free text | No | N/A |
| IOCs_Deployed_Last_24h | Number | Integer >= 0 | No | 156 |
| IOCs_Active_Total | Number | Integer >= 0 | No | 8920 |
| Endpoints_Protected | Number | Integer >= 0 | Yes | 285 |
| Detections_Last_30d | Number | Integer >= 0 | No | 45 |
| False_Positive_Rate | Number | Percentage 0-100 | No | 12 |
| Quarantine_Actions | Number | Integer >= 0 | No | 8 |
| Block_Actions | Number | Integer >= 0 | No | 37 |
| Integration_Health | Dropdown | Healthy, Degraded, Down, Maintenance | Yes | Healthy |
| Policy_Version | Text | Version number | No | 2.4.1 |
| Last_Policy_Update | Date | DD.MM.YYYY | No | 15.12.2024 |
| Owner | Text | Email | Yes | endpoint.team@example.com |
| Notes | Text | Free text | No | Excellent integration, low FP rate |

**Conditional Formatting**:

- Integration_Health "Down" → Red background
- Integration_Health "Degraded" → Yellow background
- False_Positive_Rate > 20% → Yellow background
- Detections_Last_30d > 0 → Green highlight

---
## Sheet 12: Threat_Hunting_Campaigns

**Purpose**: Track TI-driven proactive threat hunting activities

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Campaign_ID | Text | Auto-generated (HUNT-YYYY-NNN) | Yes | HUNT-2025-001 |
| Campaign_Name | Text | Free text | Yes | APT28 Infrastructure Hunt |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-008 |
| TI_Report_Title | Formula | =VLOOKUP | Auto | APT28 New C2 Infrastructure |
| Threat_Actor | Text | Free text | No | APT28 (Fancy Bear) |
| Start_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| End_Date | Date | DD.MM.YYYY | No | 22.01.2025 |
| Status | Dropdown | Planned, Active, Completed, Suspended | Yes | Completed |
| Hunt_Hypothesis | Text | Max 500 chars | Yes | APT28 may have established persistence in our environment using newly identified C2 domains |
| MITRE_Techniques | Text | Comma-separated | No | T1071.001, T1090, T1102 |
| Data_Sources_Analyzed | Text | Comma-separated | Yes | SIEM, EDR, Firewall logs, DNS logs, Proxy logs |
| Tools_Used | Text | Free text | Yes | Splunk, EDR console, MITRE ATT&CK Navigator |
| Time_Invested_Hours | Number | Hours, 1 decimal | Yes | 16.5 |
| Hunters | Text | Comma-separated names | Yes | jane.analyst@example.com, john.researcher@example.com |
| Outcome | Dropdown | No_Findings, Findings_Benign, Findings_Malicious, Investigation_Ongoing | Yes | No_Findings |
| Findings_Description | Text | Max 1000 chars | Conditional | No APT28 presence detected |
| IOCs_Discovered | Number | Integer >= 0 | No | 0 |
| New_Detection_Rules | Number | Integer >= 0 | No | 2 |
| Suspicious_Activity_Description | Text | Max 500 chars | No | N/A |
| Incidents_Created | Number | Integer >= 0 | Yes | 0 |
| Lessons_Learned | Text | Max 1000 chars | No | No APT28 presence detected. TI intel was accurate but threat did not reach our environment. |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Notes | Text | Max 500 chars | No | Good proactive hunt, validated defensive posture |

**Conditional Formatting**:

- Outcome "Findings_Malicious" → Red background
- Outcome "Findings_Benign" → Yellow background
- Status "Active" → Blue highlight
- Time_Invested_Hours > 40 → Orange (resource intensive)

**Hunt Effectiveness Metrics**:

- Total hunts per quarter
- % hunts with findings
- Average time per hunt
- Detection rules created
- Incidents discovered

---

## Sheet 13: Risk_Assessment_Updates ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document Clause 6.1 integration per ISMS-POL-A.5.7, Section 2.4 (Risk Assessment Integration Requirements)

**KPI Target**: ≥3 risk assessment updates per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Update_ID | Text | Auto-generated (RISK-YYYYQQ-NNN) | Yes | RISK-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Update_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-005 |
| TI_Report_Title | Text | Free text | Yes | Ransomware Targeting Hosting Sector |
| Risk_Register_ID | Text | REG-NNN format | Yes | REG-047 |
| Risk_Name | Text | Free text | Yes | Data Confidentiality - Ransomware |
| Risk_Type | Dropdown | Vulnerability, Threat_Campaign, Threat_Actor, Emerging_Threat, Supply_Chain | Yes | Vulnerability |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | CVE-2024-56789 |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | 9.3 |
| CVSS_Vector | Text | Max 200 chars | No | CVSS:4.0/AV:N/AC:L/PR:N/UI:N/S:C/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H |
| Risk_Before_Likelihood | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | Medium |
| Risk_Before_Impact | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | High |
| Risk_Before_Rating | Formula | Auto-calc | Auto | High |
| Risk_After_Likelihood | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | High |
| Risk_After_Impact | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | Critical |
| Risk_After_Rating | Formula | Auto-calc | Auto | Critical |
| Likelihood_Change_Rationale | Text | Max 500 chars | Yes | Mass exploitation detected per CISA KEV |
| Impact_Change_Rationale | Text | Max 500 chars | Yes | CVSS 9.3 indicates severe impact to confidentiality/integrity/availability |
| CVSS_Risk_Quantification | Text | Max 500 chars | No | CVSS 9.3 (Critical) + Mass Exploitation = Critical risk requiring emergency treatment |
| Risk_Treatment_Change | Dropdown | No_Change, New_Treatment, Accelerated_Treatment, Emergency_Treatment | Yes | Emergency_Treatment |
| Treatment_Plan_ID | Text | PLAN-YYYY-NNN format | Yes | PLAN-2025-005 |
| Treatment_Description | Text | Max 500 chars | Yes | Emergency patching of all vulnerable systems within 24 hours |
| Treatment_Owner | Text | Email | Yes | infrastructure.manager@example.com |
| Treatment_Deadline | Date | DD.MM.YYYY | Yes | 21.01.2025 |
| CRO_Review_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| CRO_Approval_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| CRO_Signature | Text | Name | Yes | John Doe, CRO |
| Treatment_Completion_Date | Date | DD.MM.YYYY | No | 21.01.2025 |
| Treatment_Status | Dropdown | Planned, In_Progress, Completed, Delayed, Cancelled | Yes | Completed |
| Validation_Evidence | Text | File reference | Yes | Vuln-Scan-20250121-Clean.xlsx |
| Notes | Text | Max 1000 chars | No | Emergency patching completed ahead of deadline, threat mitigated |

**Risk Rating Calculation** (simplified matrix):

Impact vs. Likelihood Matrix:

- Critical = Very_High Impact + (High or Very_High Likelihood)
- High = High Impact + (Medium or High Likelihood) OR Very_High Impact + Low Likelihood
- Medium = Medium Impact + Medium Likelihood
- Low = Low Impact or Very_Low Impact with Low/Very_Low Likelihood

**Conditional Formatting**:

- Risk_After_Rating "Critical" → Red background
- CVSS_Base_Score >= 9.0 → Red text
- Treatment_Status "Delayed" → Yellow background
- CRO_Approval_Date missing → Red background (blocking audit)
- Treatment_Completion_Date > Treatment_Deadline → Orange (missed deadline)

**Validation Rules**:

- CRO_Review_Date required for all updates
- CRO_Approval_Date required within 48 hours of Review_Date
- Treatment_Completion_Date required if Status = Completed
- Validation_Evidence required for all Completed treatments

**Audit Evidence Requirements**:

- **TI_Report linkage**: Threat intelligence that triggered update
- **Risk_Rating changes**: Documented rationale with CVSS context
- **CRO approval**: Chief Risk Officer formal sign-off (Clause 6.1 requirement)
- **Treatment evidence**: Proof of risk treatment completion
- **Quarterly target**: Minimum 3 risk updates with full audit trail

---

## Sheet 14: Incident_TI_Integration ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Track TI usage in incident response per ISMS-POL-A.5.7, Section 2.5 (Incident Management Integration Requirements)

**KPI Target**: ≥70% of P1/P2 incidents use threat intelligence

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (INC-TI-YYYY-NNN) | Yes | INC-TI-2025-001 |
| Incident_ID | Text | INC-YYYY-NNN format | Yes | INC-2025-012 |
| Incident_Priority | Dropdown | P1, P2, P3, P4 | Yes | P1 |
| Incident_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 25.01.2025 14:30 |
| Incident_Title | Text | Free text | Yes | Suspicious network activity detected |
| Incident_Category | Dropdown | Malware, Phishing, Data_Breach, DDoS, Insider_Threat, Vulnerability_Exploit, Other | Yes | Malware |
| TI_Used | Dropdown | Yes, No, Partial | Yes | Yes |
| TI_Usage_Timing | Dropdown | During_Detection, During_Investigation, During_Containment, During_Recovery, Post_Incident | Conditional | During_Investigation |
| TI_Reports_Referenced | Text | Comma-separated TI-YYYY-NNN | Conditional | TI-2025-008, TI-2025-012 |
| IOCs_Matched | Text | Comma-separated IOC-YYYY-NNN | No | IOC-2025-045, IOC-2025-098 |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | CVE-2024-98765 |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | 8.7 |
| CVSS_Vector | Text | Max 200 chars | No | CVSS:4.0/AV:N/AC:L/PR:N/UI:R/S:C/VC:H/VI:H/VA:N/SC:L/SI:L/SA:N |
| Threat_Actor_Identified | Text | Free text | No | APT28 |
| MITRE_Techniques_Observed | Text | Comma-separated | No | T1071.001, T1059.001, T1055 |
| TI_Value_Assessment | Dropdown | Critical, High, Medium, Low, None | Conditional | High |
| TI_Impact_Description | Text | Max 500 chars | Conditional | TI provided TTPs that enabled rapid detection of lateral movement attempts |
| Investigation_Duration_Hours | Number | Hours, 1 decimal | Yes | 6.5 |
| Time_Saved_Estimate_Hours | Number | Hours, 1 decimal | No | 18.0 |
| Containment_Actions | Text | Max 500 chars | Yes | Isolated affected host, blocked C2 domains at firewall |
| TI_Driven_Containment | Dropdown | Yes, No, Partial | No | Yes |
| Eradication_Actions | Text | Max 500 chars | Yes | Removed malware, patched vulnerability, reset credentials |
| Recovery_Actions | Text | Max 500 chars | Yes | Restored from clean backup, verified system integrity |
| Lessons_Learned | Text | Max 1000 chars | No | Early TI integration critical for rapid response |
| New_IOCs_Discovered | Number | Integer >= 0 | No | 3 |
| New_Detection_Rules_Created | Number | Integer >= 0 | No | 2 |
| TI_Feedback_Provided_to_Sources | Dropdown | Yes, No | No | Yes |
| Feedback_Details | Text | Max 300 chars | Conditional | Shared newly discovered IOCs with ISAC |
| Incident_Responder | Text | Email | Yes | incident.responder@example.com |
| Incident_Close_Date | Date | DD.MM.YYYY | No | 26.01.2025 |
| Notes | Text | Max 1000 chars | No | Excellent example of TI-driven incident response |

**Formulas**:

Investigation_Duration_Hours = (Incident_Close_Date - Incident_Date) in hours
Time_Saved_Estimate_Hours = Manual estimate by responder

**Conditional Formatting**:

- Incident_Priority "P1" AND TI_Used "No" → Red background (missed opportunity)
- TI_Value_Assessment "Critical" → Green highlight
- CVSS_Base_Score >= 9.0 → Red text
- Time_Saved_Estimate_Hours > 10 → Green highlight (significant value)
- Investigation_Duration_Hours > 48 → Yellow (prolonged investigation)

**Validation Rules**:

- If TI_Used = "Yes" or "Partial": TI_Reports_Referenced required
- If TI_Used = "Yes" or "Partial": TI_Value_Assessment required
- If TI_Used = "Yes" or "Partial": TI_Impact_Description required
- P1/P2 incidents with TI_Used "No" require justification in Notes

**Audit Evidence Requirements**:

- **P1/P2 TI usage tracking**: ≥70% must have TI_Used = "Yes"
- **TI value quantification**: Time saved, faster containment, better eradication
- **IOC matching**: Direct evidence of TI-to-detection pipeline effectiveness
- **Feedback loop**: TI_Feedback_Provided shows bidirectional intelligence flow
- **Quarterly KPI**: Calculate (Count P1/P2 with TI_Used="Yes") / (Total P1/P2) >= 70%

---

## Sheet 15: Intelligence_Driven_Decisions ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document business decisions based on TI per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)

**KPI Target**: ≥5 documented intelligence-driven decisions per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Decision_ID | Text | Auto-generated (DEC-YYYYQQ-NNN) | Yes | DEC-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Decision_Date | Date | DD.MM.YYYY | Yes | 22.01.2025 |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-009 |
| TI_Report_Title | Text | Free text | Yes | Emerging Threat: Supply Chain Attack Vector |
| Decision_Category | Dropdown | Architecture, Tool_Investment, Process_Change, Resource_Allocation, Risk_Treatment, Strategic_Initiative | Yes | Tool_Investment |
| Decision_Title | Text | Free text | Yes | Accelerate EDR deployment to development environment |
| Decision_Description | Text | Max 1000 chars | Yes | Deploy EDR to 45 developer workstations to protect against supply chain attacks targeting dev tools |
| TI_Insight_Summary | Text | Max 500 chars | Yes | TI report shows threat actors targeting developer tools and build pipelines in hosting sector |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | N/A |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | N/A |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | N/A |
| CVSS_Prioritization_Flag | Dropdown | Yes, No | No | No |
| Risk_Addressed | Text | Free text | Yes | Supply chain compromise via developer workstation |
| Business_Impact | Text | Max 500 chars | Yes | Protects critical build infrastructure, reduces risk of malicious code injection |
| Decision_Maker | Text | Name and role | Yes | Jane Smith, CISO |
| Decision_Maker_Level | Dropdown | C-Suite, VP, Director, Manager | Yes | C-Suite |
| Stakeholders_Involved | Text | Comma-separated | Yes | CISO, CTO, Development Manager, Security Operations |
| Investment_Required_CHF | Currency | >=0, 2 decimals | No | 45000.00 |
| Resource_Hours_Required | Number | Hours, 1 decimal | No | 120.0 |
| Implementation_Timeline | Text | Free text | Yes | 4 weeks (01.02.2025 - 28.02.2025) |
| Expected_Benefits | Text | Max 500 chars | Yes | Early detection of dev workstation compromise, protection of build pipeline, reduced supply chain risk |
| ROI_Estimate | Formula | Auto-calc if data present | Auto | 3.5x |
| Implementation_Status | Dropdown | Planned, In_Progress, Completed, On_Hold, Cancelled | Yes | In_Progress |
| Implementation_Start_Date | Date | DD.MM.YYYY | No | 01.02.2025 |
| Implementation_Complete_Date | Date | DD.MM.YYYY | No | N/A |
| Success_Metrics | Text | Max 300 chars | Yes | All 45 dev workstations with EDR, <5% performance impact, zero missed detections |
| Outcome_Assessment | Text | Max 500 chars | No | TBD upon completion |
| Lessons_Learned | Text | Max 500 chars | No | TBD |
| Documentation_Link | Text | URL or file path | No | https://docs.example.com/projects/edr-dev-rollout |
| Board_Presentation | Dropdown | Yes, No, Planned | No | Planned |
| Notes | Text | Max 1000 chars | No | Approved in Q1 CISO review, accelerated based on TI assessment |

**ROI Calculation** (if data present):

ROI_Estimate = (Cost_Avoidance_Estimate) / (Investment_Required_CHF)

Where Cost_Avoidance_Estimate is based on:

- Potential incident costs prevented
- Business disruption avoided
- Reputation protection

**Conditional Formatting**:

- Decision_Maker_Level "C-Suite" → Green highlight (executive buy-in)
- Investment_Required > 100,000 CHF → Yellow (significant investment)
- Implementation_Status "Cancelled" → Gray background
- ROI_Estimate >= 3.0x → Green (strong ROI)
- CVSS_Base_Score >= 9.0 → Red text (critical vulnerability addressed)

**Validation Rules**:

- Decision_Maker_Level "C-Suite" required for Investment > 50,000 CHF
- Implementation_Complete_Date required if Status = "Completed"
- Outcome_Assessment required if Status = "Completed"
- Success_Metrics required for all decisions

**Audit Evidence Requirements**:

- **TI linkage**: Direct connection to threat intelligence report
- **Executive involvement**: Decision_Maker and stakeholder documentation
- **Business justification**: Risk addressed, business impact, expected benefits
- **Outcome tracking**: Implementation status and success metrics
- **Quarterly target**: Minimum 5 documented decisions with full audit trail
- **Strategic value**: Demonstrate TI drives business and security decisions

---

## Sheet 16: Action_Items

**Purpose**: Track identified issues, gaps, and remediation actions from the assessment

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Item_ID | Text | Auto-generated (ACT-NNN) | Yes | ACT-001 |
| Category | Dropdown | Integration_Gap, Process_Improvement, Documentation, Training, Tool_Configuration | Yes | Integration_Gap |
| Description | Text | Free text (max 500 chars) | Yes | EDR integration missing for endpoint group B |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Source_Sheet | Text | Sheet name reference | Yes | Tool_Integration_Matrix |
| Assigned_To | Text | Name/email | Yes | soc.lead@example.com |
| Due_Date | Date | DD.MM.YYYY | Yes | 15.03.2025 |
| Status | Dropdown | Open, In_Progress, Completed, Deferred, Cancelled | Yes | Open |
| Completion_Date | Date | DD.MM.YYYY | No | N/A |
| Resolution_Notes | Text | Max 500 chars | No | N/A |
| Evidence_Link | Text | URL or file path | No | N/A |

**Conditional Formatting**:

- Priority "Critical" + Status "Open" -> Red background
- Due_Date < Today AND Status != "Completed" -> Yellow background
- Status "Completed" -> Green highlight

---

## Sheet 17: Metadata

**Purpose**: Document workbook metadata, version history, and assessment summary

**Content Sections**:

1. **Document Information**
   - Document ID: ISMS-IMP-A.5.7.3
   - Version: 1.0
   - Control Reference: ISO/IEC 27001:2022 Control A.5.7
   - Assessment Type: Integration & Distribution Assessment

2. **Generation Information**
   - Generated Date: [Auto-populated]
   - Generator Version: 1.0
   - Framework Version: 1.0

3. **Assessment Summary**
   - Total Sheets: 17
   - Sheets Completed: [Count]
   - Overall Status: [Draft/In_Review/Approved]
   - Last Modified: [Date]
   - Modified By: [Name]

4. **Approval Workflow**
   - Prepared By: [Name/Date]
   - Reviewed By: [Name/Date]
   - Approved By: [Name/Date]

5. **Related Documents**
   - ISMS-POL-A.5.7
   - ISMS-IMP-A.5.7.1 through A.5.7.5
   - Cross-control references

---

# Assessment Methodology

## Tool Integration Assessment

- Inventory all security tools
- Assess current integration status
- Identify integration gaps
- Prioritize based on business value
- Develop integration roadmap
- Track detailed SIEM/EDR integration (Sheets 10-11)

## IOC Effectiveness Assessment

- Track IOC deployment lifecycle
- Monitor hit rates and false positives
- Correlate IOCs to incidents
- Retire ineffective IOCs
- Continuous quality improvement

## Dissemination Effectiveness Assessment

- Analyze engagement metrics
- Collect stakeholder feedback
- Identify channel performance
- Optimize distribution strategy
- Tailor content to audience

## Prevention Tracking (Sheet 7)

- Document prevented incidents with before/after evidence
- Validate prevention through SIEM/EDR/scanning evidence
- Calculate time-to-remediation metrics
- Achieve quarterly KPI: ≥3 validated preventions
- Prepare full audit evidence packages

## Risk Assessment Integration (Sheet 13)

- Track TI-driven risk register updates (Clause 6.1)
- Document risk rating changes with CVSS quantification
- Obtain CRO approval for all risk treatment changes
- Achieve quarterly KPI: ≥3 risk updates with audit trail
- Link threat intelligence to risk management framework

## Incident Response Integration (Sheet 14)

- Track TI usage in all P1/P2 incidents
- Quantify TI value (time saved, faster containment)
- Document IOC matches and TTP correlations
- Achieve quarterly KPI: ≥70% P1/P2 incidents use TI
- Establish bidirectional TI feedback loop

## Intelligence-Driven Decisions (Sheet 15)

- Document C-suite and VP-level decisions based on TI
- Quantify business impact and ROI
- Track implementation status and success metrics
- Achieve quarterly KPI: ≥5 documented decisions
- Demonstrate strategic value of threat intelligence program

## Threat Hunting (Sheet 12)

- Conduct proactive TI-driven threat hunts
- Document hunt hypotheses and methodologies
- Track outcomes and lessons learned
- Create new detection rules from hunt findings
- Build threat hunting capability

---

# Integration Points

## From Control 5.7.2 (Collection & Analysis)

- Intelligence_Production → Distribution_Tracking.Product_ID
- Intelligence_Production → Prevention_Tracking.Threat_Report_ID
- Intelligence_Production → Risk_Assessment_Updates.TI_Report_ID
- Intelligence_Production → Incident_TI_Integration.TI_Reports_Referenced
- Intelligence_Production → Intelligence_Driven_Decisions.TI_Report_ID
- Intelligence_Production → Threat_Hunting_Campaigns.TI_Report_ID
- VulnerabilityThreatLink → IOC_Deployment (vulnerability-related IOCs)
- VulnerabilityThreatLink → Prevention_Tracking.CVE_ID

## To Control 5.7.1 (Sources)

- IOC effectiveness data → Source quality evaluation
- Feedback on source-specific intelligence → Source ratings
- Prevention tracking → Source value quantification
- Incident TI integration → Source actionability assessment

## To Control 5.7.4 (Dashboard)

- All 15 sheets → External references for program-level KPIs
- Critical evidence sheets (7, 13, 14, 15) → Dashboard KPI tracking

## To Control 8.8 (Vulnerability Management)

- IOCs related to vulnerabilities → 8.8 compromise assessment
- Tool integration status → 8.8 detection capabilities
- Prevention_Tracking → 8.8 emergency patching validation
- Risk_Assessment_Updates → 8.8 vulnerability prioritization

## To Controls A.5.24-5.28 (Incident Management)

- Incident_TI_Integration → A.5.24-5.28 incident response evidence
- IOC matches → Incident detection documentation
- Threat hunting findings → Proactive incident prevention

## To Clause 6.1 (Risk Assessment)

- Risk_Assessment_Updates → Clause 6.1 mandatory risk register updates
- CRO approval tracking → Clause 6.1 governance evidence

---

# Evidence Requirements

## Standard Evidence

- Integration documentation and diagrams
- IOC deployment logs
- Stakeholder feedback surveys
- Engagement analytics reports
- Tool configuration evidence
- Incident correlation reports

## Critical Audit Evidence

**Sheet 7 - Prevention_Tracking**:

- Before-state vulnerability scans
- Threat intelligence alerts that triggered action
- After-state clean scans
- SIEM/EDR validation logs
- Time-to-remediation calculations
- Minimum 3 fully documented preventions per quarter

**Sheet 13 - Risk_Assessment_Updates**:

- Threat intelligence reports triggering risk updates
- Risk rating change calculations with CVSS context
- CRO review and approval signatures
- Risk treatment completion evidence
- Minimum 3 risk updates with CRO approval per quarter

**Sheet 14 - Incident_TI_Integration**:

- Incident records with TI usage documentation
- IOC match evidence
- Time-saved quantification
- P1/P2 incident TI usage rate ≥70%
- Bidirectional TI feedback examples

**Sheet 15 - Intelligence_Driven_Decisions**:

- Executive decision documentation
- Business justification and ROI calculations
- Implementation tracking and success metrics
- Minimum 5 C-suite/VP decisions per quarter
- Strategic TI program value demonstration

---

# Completion Instructions

## Initial Assessment

**Phase 1: Core Integration (Sheets 1-6)** - 2 days
1. Document all Tool_Integration entries (Sheet 2)
2. Load IOC_Deployment data (past 90 days) (Sheet 3)
3. Configure Dissemination_Channels (Sheet 4)
4. Populate Stakeholder_Registry (Sheet 5)
5. Review Distribution_Tracking (past 90 days) (Sheet 6)

**Phase 2: Critical Evidence Sheets (Sheets 7, 13-15)** - 3 days
6. Document Prevention_Tracking (Sheet 7) - past quarter
7. Document Risk_Assessment_Updates (Sheet 13) - past quarter
8. Document Incident_TI_Integration (Sheet 14) - past quarter
9. Document Intelligence_Driven_Decisions (Sheet 15) - past quarter

**Phase 3: Supporting Sheets (Sheets 8-12)** - 2 days
10. Collect and enter Feedback (Sheet 8)
11. Establish baseline Integration_Metrics (Sheet 9)
12. Document SIEM_Integration_Details (Sheet 10)
13. Document EDR_Integration_Details (Sheet 11)
14. Document Threat_Hunting_Campaigns (Sheet 12) - past quarter

**Estimated Total Time**: 5-7 days for comprehensive initial assessment

## Ongoing Management

**Daily**:

- IOC deployment tracking (Sheet 3)
- SIEM/EDR integration health monitoring (Sheets 10-11)

**Weekly**:

- Distribution tracking (Sheet 6)
- Feedback collection (Sheet 8)
- Tool integration status updates (Sheet 2)

**Monthly**:

- Metrics review (Sheet 9)
- Dissemination channel performance (Sheet 4)
- Stakeholder engagement analysis (Sheet 5)

**Quarterly** (CRITICAL for audit):

- Prevention tracking documentation (Sheet 7) - Target: ≥3 preventions
- Risk assessment updates (Sheet 13) - Target: ≥3 updates with CRO approval
- Incident-TI integration assessment (Sheet 14) - Target: ≥70% P1/P2 usage
- Intelligence-driven decisions (Sheet 15) - Target: ≥5 documented decisions
- Threat hunting campaigns (Sheet 12) - Minimum 2 campaigns
- Full assessment workbook review and validation
- Dashboard consolidation (Control 5.7.4)

---

# Validation Rules

## Standard Validation

- All Active IOCs must be deployed to >= 1 tool
- Expired IOCs must have Status updated
- Distribution must match Stakeholder TLP clearance
- Tool integration with "Fully_Integrated" must have automation
- Critical IOCs (Severity=Critical) must deploy within 4 hours

## Critical Evidence Validation

**Sheet 7 - Prevention_Tracking**:

- All Evidence fields (Before, TI Alert, After, Validation) must be non-empty
- Validation_Date >= After_Date >= Action_Date
- Time_to_Remediation must be auto-calculated
- Quarterly count >= 3 validated preventions

**Sheet 13 - Risk_Assessment_Updates**:

- CRO_Review_Date required for ALL updates
- CRO_Approval_Date within 48 hours of Review_Date
- Validation_Evidence required for Completed treatments
- Quarterly count >= 3 updates with CRO signatures

**Sheet 14 - Incident_TI_Integration**:

- P1/P2 incidents with TI_Used="No" require justification in Notes
- TI_Used="Yes" requires: TI_Reports_Referenced, TI_Value_Assessment, TI_Impact_Description
- Quarterly P1/P2 TI usage rate >= 70%

**Sheet 15 - Intelligence_Driven_Decisions**:

- Investment > 50,000 CHF requires Decision_Maker_Level="C-Suite"
- Status="Completed" requires Outcome_Assessment
- Success_Metrics required for ALL decisions
- Quarterly count >= 5 documented decisions

---

# Quarterly KPI Summary

| KPI | Target | Sheet | Audit Criticality |
|-----|--------|-------|-------------------|
| Prevented Incidents | ≥3 per quarter | Sheet 7 | CRITICAL |
| Risk Assessment Updates | ≥3 per quarter with CRO approval | Sheet 13 | CRITICAL (Clause 6.1) |
| P1/P2 Incident TI Usage | ≥70% | Sheet 14 | CRITICAL |
| Intelligence-Driven Decisions | ≥5 per quarter | Sheet 15 | CRITICAL |
| Threat Hunting Campaigns | ≥2 per quarter | Sheet 12 | HIGH |
| Tool Integration Rate | ≥80% fully integrated | Sheet 2 | MEDIUM |
| IOC Deployment Rate | ≥95% | Sheet 3 | MEDIUM |
| Stakeholder Engagement | Avg ≥4.0/5.0 | Sheet 8 | MEDIUM |
| Distribution Reach | ≥90% target audience | Sheet 6 | LOW |

**Audit Readiness**: Sheets 7, 13, 14, 15 are MANDATORY for demonstrating threat intelligence program value and Clause 6.1 compliance.

---

# Related Documents

**Policy Framework**:

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.3** (Intelligence Dissemination Requirements)
- **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration Requirements) - **References Sheet 13**
- **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration Requirements) - **References Sheet 14**
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - **References Sheets 7, 15**
- **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities)

**Implementation Specifications**:

- ISMS-IMP-A.5.7.1 (Threat Intelligence Sources Assessment)
- ISMS-IMP-A.5.7.2 (Intelligence Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.4 (Threat Intelligence Effectiveness Dashboard)

**Cross-Control Integration**:

- ISMS-IMP-A.8.8 (Vulnerability Management) - **Integration with Prevention_Tracking**
- Tool-specific integration guides
- Incident response procedures (A.5.24-5.28)
- Risk management framework (Clause 6.1)

---

---

# Related Documents

**Policy Framework:**

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.3** (Intelligence Dissemination Requirements)
- **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration Requirements) - **References Sheet 13**
- **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration Requirements) - **References Sheet 14**
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - **References Sheets 7, 15**
- **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities)

**Implementation Specifications:**

- **ISMS-IMP-A.5.7.1** (Threat Intelligence Sources Assessment) - Source IDs referenced
- **ISMS-IMP-A.5.7.2** (Intelligence Collection & Analysis Assessment) - VTL records, IOCs, intelligence products consumed
- **ISMS-IMP-A.5.7.4** (Effectiveness Dashboard) - Integration metrics consolidated
- **ISMS-IMP-A.5.7.5** (Standalone Dashboard) - Prevention and decision metrics for executives

**Cross-Control Integration:**

- **ISMS-IMP-A.8.8** (Vulnerability Management) - VTL records feed into prevention tracking
- **ISO 27001:2022 Clause 6.1** (Risk Assessment) - **Sheet 13 MANDATORY integration**
- **ISO 27001:2022 Controls A.5.24-5.28** (Incident Management) - **Sheet 14 MANDATORY integration**

**Standards References:**

- ISO/IEC 27001:2022 Annex A Control A.5.7
- ISO/IEC 27002:2022 Control 5.7 Implementation Guidance
- ISO/IEC 27001:2022 Clause 6.1 (Actions to address risks and opportunities)
- ISO/IEC 27001:2022 Controls A.5.24-5.28 (Incident management)

---

**END OF SPECIFICATION**

---

*"The opposite of a correct statement is a false statement. But the opposite of a profound truth may well be another profound truth."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
