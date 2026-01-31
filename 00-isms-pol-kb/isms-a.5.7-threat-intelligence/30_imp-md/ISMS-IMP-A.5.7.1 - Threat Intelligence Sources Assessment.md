# ISMS-IMP-A.5.7.1
## Threat Intelligence Sources Assessment

**Document ID**: ISMS-IMP-A.5.7.1  
**Title**: Threat Intelligence Sources Assessment - Implementation Specification  
**Version**: 1.0  
**Date**: [Date]
**Classification**: Internal  
**Owner**: Threat Intelligence Team Lead  
**Status**: Draft

---

## 1. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Implementation Team | Initial consolidated specification (15 sheets) |

**Review Cycle**: Quarterly or upon source portfolio changes  
**Next Review Date**: [Date + 3 months]  
**Related Policy**: ISMS-POL-A.5.7-S2 (Threat Intelligence Requirements), ISMS-POL-A.5.7-S4 Section 4.4.3 (Source Performance Validation), ISMS-POL-A.5.7-S4 Section 4.4.6 (Business Continuity)

---

## 2. Purpose & Objectives

### 2.1 Purpose

This workbook assesses [Organization]'s threat intelligence source portfolio to ensure:
- Comprehensive coverage of relevant threat landscapes
- Reliability and credibility of intelligence sources
- Cost-effectiveness of subscription services
- Compliance with data protection and privacy regulations
CVSS vulnerability scoring capability assessment
Vendor relationship and SLA management
Audit-ready evidence for source validation and business continuity

### 2.2 Assessment Objectives

1. **Inventory Management**: Maintain complete inventory of all TI sources (commercial, OSINT, government, internal)
2. **Quality Evaluation**: Assess source reliability using Admiralty Code methodology
3. **CVSS Capability Assessment**: Track CVSS 4.0/3.1 support and scoring accuracy
4. **Coverage Analysis**: Identify gaps in geographic, sector, or threat type coverage
5. **ROI Analysis**: Evaluate cost vs. value for subscription services
6. **Compliance Verification**: Ensure sources meet legal/regulatory requirements
7. **Vendor Management**: Track integration points, SLAs, and vendor contacts
8. **Audit Evidence**: Document quarterly source validation and business continuity per ISMS-POL-A.5.7-S4

---

## 3. Scope

### 3.1 In Scope

- Commercial threat intelligence platforms (e.g., CrowdStrike, Recorded Future, Mandiant)
- OSINT sources (Twitter feeds, security blogs, GitHub repositories)
- Government/ISAC feeds (CISA, FBI, sector-specific ISACs)
- Internal sources (honeypots, security telemetry, incident data)
- Vendor security advisories
- Peer sharing arrangements
API integration and technical feed capabilities
CVSS scoring accuracy validation
Vendor SLA performance tracking
Business continuity planning for critical TI roles

### 3.2 Out of Scope

- Raw log data (covered in SIEM operations)
- Vulnerability scanning results (covered in Control 8.8)
- Individual analyst research (covered in ISMS-IMP-A.5.7.2)
- Vendor procurement processes (covered in procurement policy)
- Financial contract negotiations (covered in finance policy)

---

## 4. Workbook Structure

### 4.1 Sheet Overview

| Sheet # | Sheet Name | Purpose | Links To | Audit Critical |
|---------|------------|---------|----------|----------------|
| 1 | Instructions | User guide | N/A | No |
| 2 | Source_Inventory | Master list of all TI sources + CVSS capability | Sheets 3-15 | No |
| 3 | Source_Evaluation | Quality assessment + CVSS accuracy tracking | Sheet 2 | No |
| 4 | Coverage_Matrix | Geographic/sector/threat coverage | Sheet 2 | No |
| 5 | Cost_Analysis | ROI and budget tracking | Sheet 2 | No |
| 6 | Compliance_Check | Legal/regulatory compliance | Sheet 2 | No |
| 7 | Action_Items | Remediation tasks | Sheets 3-6, 9-15 | No |
| 8 | Metadata | Workbook generation info | N/A | No |
| **9** | **Integration_Points** | **API/feed technical integration** | **Sheet 2** | **No** |
| **10** | **Update_Frequency** | **SLA compliance tracking** | **Sheet 2** | **No** |
| **11** | **Source_Contacts** | **Vendor escalation contacts** | **Sheet 2** | **No** |
| **12** | **Vendor_SLAs** | **Performance vs. contractual SLAs** | **Sheet 2** | **No** |
| **13** | **API_Integration** | **API health and rate limits** | **Sheet 2** | **No** |
| **14** | **Source_Performance_Validation** | **Quarterly accuracy validation** | **Sheet 2** | **✅ YES** |
| **15** | **Business_Continuity_Plan** | **Role continuity and backup** | **Sheet 2** | **✅ YES** |

**Sheet Categories**:
- **Source Management** (Sheets 2-5): Core source inventory, evaluation, coverage, and cost tracking
- **Compliance & Quality** (Sheets 6-7): Regulatory compliance and action item tracking
- **Vendor Management** (Sheets 9-13): Technical integration, SLA tracking, and vendor relationships
- **Audit Evidence** (Sheets 14-15): Quarterly source validation and business continuity per ISMS-POL-A.5.7-S4 Sections 4.4.3 and 4.4.6
- **Metadata** (Sheet 8): Document control and versioning

### 4.2 Sheet Navigation Guide

**For Initial Setup** (New Deployment):
1. Start with Sheet 1 (Instructions) - read completely
2. Populate Sheet 2 (Source_Inventory) with all sources
3. Complete Sheet 3 (Source_Evaluation) for each source
4. Fill Sheets 4-6 (Coverage, Cost, Compliance)
5. Document technical integration in Sheets 9-13
6. Perform initial validation in Sheet 14
7. Document continuity in Sheet 15
8. Track issues in Sheet 7 (Action_Items)

**For Quarterly Review**:
1. Update Sheet 2 (add/remove sources, update CVSS capabilities)
2. Re-evaluate sources in Sheet 3 (especially CVSS accuracy)
3. Update vendor data in Sheets 9-13
4. **CRITICAL**: Complete Sheet 14 quarterly validation (audit requirement)
5. Review Sheet 15 continuity status
6. Close/create action items in Sheet 7

**For Audits**:
- Primary evidence: Sheets 14-15 (Source_Performance_Validation, Business_Continuity_Plan)
- Supporting evidence: Sheets 2-3 (Source_Inventory, Source_Evaluation)
- Remediation tracking: Sheet 7 (Action_Items)

---

## 5. Sheet Specifications

### 5.1 Sheet 1: Instructions

**Purpose**: Provide completion guidance to stakeholders

**Content**:
- Assessment purpose and scope
- Completion timeline and responsibilities
- Data validation rules explanation
- Definitions of Admiralty Code ratings
CVSS support level definitions
Quarterly validation requirements (Sheet 14)
Business continuity requirements (Sheet 15)
- Contact information for assistance
- Link to policy framework (ISMS-POL-A.5.7)

**Format**: Rich text with hyperlinks, no data entry

**CVSS Support Levels**:
- 4.0 Full: Complete CVSS 4.0 vectors, base scores, temporal metrics
- 4.0 Basic: CVSS 4.0 base scores only, no vectors
- 3.1 Full: Complete CVSS 3.1 vectors, base scores, temporal metrics
- 3.1 Basic: CVSS 3.1 base scores only, no vectors
- 2.0 Only: Legacy CVSS 2.0 scoring (flag for deprecation planning)
- Proprietary: Vendor-specific severity without CVSS
- None: No vulnerability severity assessment

Quarterly Validation Requirement (AUDIT EVIDENCE):
- Sheet 14 must be completed EVERY QUARTER per ISMS-POL-A.5.7-S4 Section 4.4.3
- Minimum sample size: 10 IOCs + 10 CVEs per source
- Target accuracy: ≥85% overall, ≥90% CVSS accuracy
- Validation failure triggers action items in Sheet 7

Business Continuity Requirement (AUDIT EVIDENCE):
- Sheet 15 must document backup personnel for ALL critical roles
- Critical roles require 100% backup training completion
- Annual continuity testing required per ISMS-POL-A.5.7-S4 Section 4.4.6


---

### 5.2 Sheet 2: Source_Inventory

**Purpose**: Master inventory of all threat intelligence sources

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Text | Auto-generated (SRC-YYYY-NNN) | Yes | SRC-2025-001 |
| Source_Name | Text | Free text (max 100 chars) | Yes | CrowdStrike Falcon Intelligence |
| Source_Type | Dropdown | Commercial, OSINT, Government, Internal, Vendor, Peer_Sharing | Yes | Commercial |
| Source_Category | Dropdown | Threat_Feed, ISAC, Vendor_Advisory, Blog, Social_Media, Research_Report, Internal_Telemetry | Yes | Threat_Feed |
| Provider | Text | Free text (max 100 chars) | Yes | CrowdStrike Inc. |
| Contact_Email | Text | Email validation | No | ti-support@crowdstrike.com |
| Contract_Start | Date | DD.MM.YYYY | No | 15.01.2024 |
| Contract_End | Date | DD.MM.YYYY, must be > Contract_Start | No | 14.01.2025 |
| Auto_Renew | Dropdown | Yes, No, Under_Review | No | Yes |
| Status | Dropdown | Active, Inactive, Trial, Pending_Renewal, Cancelled | Yes | Active |
| **CVSS_Support** | **Dropdown** | **4.0 Full, 4.0 Basic, 3.1 Full, 3.1 Basic, 2.0 Only, Proprietary, None** | **Yes** | **4.0 Full** |
| Primary_Owner | Text | Free text (department/person) | Yes | SOC Team Lead |
| Backup_Owner | Text | Free text | No | Threat Analyst 2 |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Review_Date | Date | Auto-calculated (Last_Review + 90 days) | Yes | 02.04.2025 |
| Notes | Text | Free text (max 500 chars) | No | Primary source for APT intelligence |

**NEW - CVSS_Support Column Details**:

**Position**: Column K (after "Status")

**Validation List**:
1. **4.0 Full** - Complete CVSS 4.0 implementation (vectors, base scores, temporal metrics)
2. **4.0 Basic** - CVSS 4.0 base scores only, no detailed vectors
3. **3.1 Full** - Complete CVSS 3.1 implementation (vectors, base scores, temporal metrics)
4. **3.1 Basic** - CVSS 3.1 base scores only, no detailed vectors
5. **2.0 Only** - Legacy CVSS 2.0 scoring (flag for deprecation planning)
6. **Proprietary** - Vendor-specific severity scoring without CVSS
7. **None** - No vulnerability severity assessment capability

**Conditional Formatting for CVSS_Support**:
- "4.0 Full" → Green background (#C6EFCE) - Preferred
- "4.0 Basic" → Light green background (#E7F4E4) - Acceptable
- "3.1 Full" → Yellow background (#FFEB9C) - Acceptable but consider upgrade
- "3.1 Basic" → Light yellow background (#FFF4CC) - Plan upgrade path
- "2.0 Only" → Orange background (#FFD966) - Deprecation planning required
- "Proprietary" → Orange background (#FFD966) - Limited interoperability
- "None" → Red background (#FFC7CE) - Not suitable for vulnerability tracking

**Rationale**: CVSS 4.0 provides improved accuracy for vulnerability severity assessment, particularly for OT/IoT environments. Sources with "None" or "Proprietary" scoring cannot integrate with Control 8.8 vulnerability management processes.

**Conditional Formatting** (Existing + New):
- Status "Inactive" or "Cancelled" → Gray background
- Contract_End within 30 days → Orange background
- Contract_End past → Red background
- Next_Review_Date overdue → Yellow background
CVSS_Support conditional formatting as defined above

**Named Ranges**:
- `SourceInventory_Data`: A2:P[LastRow] (expanded from O to P due to new column)
- `ActiveSources`: Filter where Status = "Active"

---

### 5.3 Sheet 3: Source_Evaluation

**Purpose**: Assess reliability and credibility using Admiralty Code + CVSS accuracy

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Evaluation_Date | Date | DD.MM.YYYY, default TODAY() | Yes | 02.01.2025 |
| Evaluator | Text | Free text | Yes | jane.analyst@example.com |
| Reliability_Rating | Dropdown | A-F (Admiralty Code) | Yes | A - Completely Reliable |
| Reliability_Justification | Text | Free text (max 300 chars) | Yes | Consistently accurate, corroborated by incidents |
| Credibility_Rating | Dropdown | 1-6 (Admiralty Code) | Yes | 1 - Confirmed by other sources |
| Credibility_Justification | Text | Free text (max 300 chars) | Yes | Intelligence verified through internal telemetry |
| Timeliness_Score | Number | 1-5 scale | Yes | 5 |
| Timeliness_Notes | Text | Free text | No | Real-time alerts, <1 hour latency |
| Relevance_Score | Number | 1-5 scale | Yes | 4 |
| Relevance_Notes | Text | Free text | No | High relevance for financial sector threats |
| Actionability_Score | Number | 1-5 scale | Yes | 5 |
| Actionability_Notes | Text | Free text | No | Provides IOCs ready for SIEM import |
| Overall_Quality_Score | Formula | =AVERAGE(Timeliness, Relevance, Actionability) | Auto | 4.67 |
| Quality_Rating | Formula | IF Overall >= 4.5: Excellent, >=3.5: Good, >=2.5: Fair, <2.5: Poor | Auto | Excellent |
| False_Positive_Rate | Dropdown | High, Medium, Low, Unknown | No | Low |
| **CVSS_Accuracy_Rate** | **Percentage** | **0-100%, 1 decimal** | **No** | **92.5%** |
| **CVSS_Sample_Size** | **Number** | **Integer >= 0** | **No** | **20** |
| **CVSS_Validation_Date** | **Date** | **DD.MM.YYYY** | **No** | **15.12.2024** |
| Evidence_Link | Text | Hyperlink to supporting docs | No | file://evidence/SRC-2025-001.pdf |
| Recommendation | Dropdown | Continue, Enhance, Review, Discontinue | Yes | Continue |
| Next_Evaluation | Date | Auto-calculated (Evaluation_Date + 90 days) | Yes | 02.04.2025 |

**NEW - CVSS Accuracy Tracking Details**:

**CVSS_Accuracy_Rate**:
- Calculated as: (CVSS scores within ±1.0 point of NVD/vendor reference / CVSS_Sample_Size) × 100
- Minimum acceptable: 90% per ISMS-POL-A.5.7-S4 Section 4.4.3
- Optional for sources with CVSS_Support = "None" or "Proprietary"

**CVSS_Sample_Size**:
- Recommended minimum: 20 CVEs for statistical significance
- Can be derived from Sheet 14 quarterly validation data
- Update after each quarterly validation cycle

**CVSS_Validation_Date**:
- Date of last CVSS accuracy assessment
- Should align with Sheet 14 quarterly validation cycles
- If > 90 days old, flag for re-validation

**Formula Example** (not in Excel, conceptual):

IF(CVSS_Sample_Size > 0, 
   (CVEs_Within_1_Point / CVSS_Sample_Size) * 100, 
   "N/A")

**Conditional Formatting for CVSS Accuracy**:
- CVSS_Accuracy_Rate >= 95% → Dark green background (#006100)
- CVSS_Accuracy_Rate >= 90% → Green background (#00B050)
- CVSS_Accuracy_Rate >= 85% → Yellow background (#FFEB9C)
- CVSS_Accuracy_Rate >= 80% → Orange background (#FFD966)
- CVSS_Accuracy_Rate < 80% → Red background (#FFC7CE) + Action_Required

**Scoring Scales** (Existing):
- **Timeliness**: 5=Real-time, 4=Hourly, 3=Daily, 2=Weekly, 1=Monthly+
- **Relevance**: 5=Highly relevant, 4=Relevant, 3=Moderately, 2=Somewhat, 1=Not relevant
- **Actionability**: 5=Immediately actionable, 4=Actionable with minor work, 3=Requires analysis, 2=Limited actionability, 1=Not actionable

**Conditional Formatting** (Existing + New):
- Quality_Rating "Excellent" → Green
- Quality_Rating "Good" → Light Green
- Quality_Rating "Fair" → Yellow
- Quality_Rating "Poor" → Red
- Recommendation "Discontinue" → Red background
CVSS_Accuracy_Rate conditional formatting as defined above

**Admiralty Code Reference Table** (separate area on sheet):

Reliability (Source):
A = Completely reliable
B = Usually reliable
C = Fairly reliable
D = Not usually reliable
E = Unreliable
F = Reliability cannot be judged

Credibility (Information):
1 = Confirmed by other sources
2 = Probably true
3 = Possibly true
4 = Doubtful
5 = Improbable
6 = Truth cannot be judged

---

### 5.4 Sheet 4: Coverage_Matrix

**Purpose**: Identify coverage gaps across dimensions

**Structure**: Matrix format with multiple sub-tables

**NOTE**: This sheet specification is UNCHANGED from v1.0

#### 5.4.1 Geographic Coverage Sub-Table

| Source_ID | Source_Name | Global | North_America | Europe | Asia_Pacific | Middle_East | Latin_America | Africa |
|-----------|-------------|--------|---------------|--------|--------------|-------------|---------------|--------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

**Coverage Summary Row** (at bottom):
- Count of sources covering each region
- Percentage coverage (# sources / total active sources)
- Gap indicator (if < 2 sources for any region)

#### 5.4.2 Sector Coverage Sub-Table

| Source_ID | Source_Name | Financial | Healthcare | Government | Critical_Infra | Technology | Education | Retail | Manufacturing | All_Sectors |
|-----------|-------------|-----------|------------|------------|----------------|------------|-----------|--------|---------------|-------------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

#### 5.4.3 Threat Type Coverage Sub-Table

| Source_ID | Source_Name | Malware | Phishing | Ransomware | Data_Breach | DDoS | Insider | Supply_Chain | Zero_Day | APT | Vulnerabilities |
|-----------|-------------|---------|----------|------------|-------------|------|---------|--------------|----------|-----|-----------------|
| [Dropdown] | [Formula] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] | [Checkbox] |

#### 5.4.4 MITRE ATT&CK Coverage Sub-Table

**Reference**: MITRE ATT&CK v18.1 (enterpriseattackv18_1.xlsx in project files)

| Source_ID | Source_Name | Tactics_Covered | Techniques_Covered | Coverage_Percentage |
|-----------|-------------|-----------------|--------------------|--------------------|
| [Dropdown] | [Formula] | [Number 0-14] | [Number 0-200] | [Formula: (Techniques/200)*100] |

**MITRE ATT&CK Tactics** (14 total):
- Reconnaissance, Resource Development, Initial Access, Execution
- Persistence, Privilege Escalation, Defense Evasion, Credential Access
- Discovery, Lateral Movement, Collection, Command and Control
- Exfiltration, Impact

**Gap Analysis**:
- Identify techniques with <2 sources
- Prioritize based on organizational threat model
- Generate action items for critical gaps

**Conditional Formatting**:
- Coverage_Percentage >= 70% → Green
- Coverage_Percentage >= 50% → Yellow
- Coverage_Percentage < 50% → Red

---

### 5.5 Sheet 5: Cost_Analysis

**Purpose**: Track costs and calculate ROI for subscription services

**NOTE**: This sheet specification is UNCHANGED from v1.0

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Source_Type | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | Commercial |
| Annual_Cost | Currency | Number >= 0 | No | CHF 50,000 |
| Currency | Dropdown | CHF, EUR, USD | No | CHF |
| Contract_Term | Dropdown | 1_Year, 2_Year, 3_Year, Monthly, Perpetual | No | 1_Year |
| Cost_Per_Month | Formula | =Annual_Cost / 12 | Auto | CHF 4,166.67 |
| Alerts_Per_Month | Number | Integer >= 0 | No | 150 |
| Cost_Per_Alert | Formula | =Cost_Per_Month / Alerts_Per_Month | Auto | CHF 27.78 |
| Incidents_Prevented | Number | Integer >= 0 | No | 2 |
| Avg_Incident_Cost | Currency | Number >= 0 | No | CHF 100,000 |
| Estimated_Savings | Formula | =Incidents_Prevented * Avg_Incident_Cost | Auto | CHF 200,000 |
| ROI_Ratio | Formula | =(Estimated_Savings / Annual_Cost) | Auto | 4.0 |
| ROI_Category | Formula | IF ROI > 5: Excellent, >3: Good, >1: Break-Even, <1: Negative | Auto | Good |
| Budget_Next_Year | Currency | Number >= 0 | No | CHF 55,000 |
| Budget_Change | Formula | =(Budget_Next_Year / Annual_Cost) - 1 | Auto | 10% |
| Cost_Justification | Text | Free text (max 300 chars) | No | Prevents APT incidents, high ROI |

**Summary Dashboard** (separate area):
- Total annual TI spend
- Average cost per source
- Total estimated savings
- Overall program ROI
- Budget variance analysis

**Conditional Formatting**:
- ROI_Category "Excellent" → Green
- ROI_Category "Good" → Light Green
- ROI_Category "Negative" → Red
- Budget_Change > 20% → Orange (requires justification)

---

### 5.6 Sheet 6: Compliance_Check

**Purpose**: Verify legal and regulatory compliance (FADP, GDPR, ISO 27001)

**NOTE**: This sheet specification is UNCHANGED from v1.0

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Provider | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Inc. |
| Data_Contains_PII | Dropdown | Yes, No, Unknown | Yes | Yes |
| FADP_Applicable | Dropdown | Yes, No, Unknown | Yes | Yes |
| FADP_Compliant | Dropdown | Yes, No, In_Progress, Unknown | Conditional | Yes |
| FADP_Verification_Date | Date | DD.MM.YYYY | Conditional | 15.11.2024 |
| GDPR_Applicable | Dropdown | Yes, No, Unknown | Yes | Yes |
| GDPR_Compliant | Dropdown | Yes, No, In_Progress, Unknown | Conditional | Yes |
| GDPR_Verification_Date | Date | DD.MM.YYYY | Conditional | 15.11.2024 |
| DPA_Signed | Dropdown | Yes, No, In_Negotiation, N/A | Yes | Yes |
| DPA_Expiry_Date | Date | DD.MM.YYYY | Conditional | 14.01.2026 |
| DPA_Review_Date | Date | Auto (DPA_Expiry - 90 days) | Auto | 16.10.2025 |
| SCC_Applicable | Dropdown | Yes (EU-CH), Yes (EU-US), No, Unknown | Yes | Yes (EU-CH) |
| SCC_In_Place | Dropdown | Yes, No, In_Negotiation, N/A | Conditional | Yes |
| Data_Location | Text | Free text (countries) | No | Switzerland, Germany |
| Subprocessors | Text | Comma-separated list | No | AWS (Ireland), Azure (Netherlands) |
| ISO27001_Certified | Dropdown | Yes, No, Unknown | No | Yes |
| SOC2_Certified | Dropdown | Yes, No, Unknown | No | Yes |
| Privacy_Policy_Link | Text | URL | No | https://crowdstrike.com/privacy |
| Last_Compliance_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Compliance_Review | Date | Auto (Last_Review + 180 days) | Auto | 01.07.2025 |
| Compliance_Status | Formula | IF all Yes: Compliant, any No: Non-Compliant, any Unknown: Review | Auto | Compliant |
| Risk_Notes | Text | Free text (max 300 chars) | No | All compliance requirements met |

**Conditional Formatting**:
- Compliance_Status "Non-Compliant" → Red background
- Compliance_Status "Review" → Orange background
- DPA_Expiry_Date within 90 days → Yellow
- DPA_Review_Date overdue → Orange
- Any "Unknown" values → Yellow

---

### 5.7 Sheet 7: Action_Items

**Purpose**: Track remediation and improvement actions

**UPDATED**: Now links to new Sheets 9-15 as well

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Action_ID | Text | Auto-generated (ACT-YYYY-NNN) | Yes | ACT-2025-001 |
| Source_ID | Dropdown | From Source_Inventory | Yes | SRC-2025-001 |
| Issue_Type | Dropdown | Quality, Coverage_Gap, Cost, Compliance, Contract, Integration, CVSS_Accuracy, Continuity, Other | Yes | CVSS_Accuracy |
| Issue_Description | Text | Free text (max 300 chars) | Yes | CVSS accuracy below 90% threshold |
| Detected_In_Sheet | Dropdown | Sheet_3, Sheet_4, Sheet_5, Sheet_6, Sheet_9, Sheet_10, Sheet_11, Sheet_12, Sheet_13, Sheet_14, Sheet_15 | Yes | Sheet_14 |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Assigned_To | Text | Email or department | Yes | jane.analyst@example.com |
| Due_Date | Date | DD.MM.YYYY | Yes | 01.02.2025 |
| Status | Dropdown | Open, In_Progress, Blocked, Resolved, Closed | Yes | Open |
| Status_Notes | Text | Free text | No | Vendor contacted, awaiting improved IOC feed |
| Resolution_Date | Date | If Status=Resolved/Closed | Conditional | N/A |
| Evidence_Link | Text | Hyperlink | No | N/A |
| Created_Date | Date | Auto-fill TODAY() | Yes | 02.01.2025 |
| Created_By | Text | Auto-fill USER() | Yes | jane.analyst@example.com |
| Last_Updated | Date | Auto-update on any change | Yes | 02.01.2025 |

**NEW Issue Types**:
- **Integration**: API failures, feed connectivity issues (from Sheets 9, 13)
- **CVSS_Accuracy**: CVSS scoring accuracy below threshold (from Sheets 3, 14)
- **Continuity**: Business continuity gaps (from Sheet 15)

**Conditional Formatting**:
- Priority "Critical" → Red background
- Due_Date overdue → Red text
- Status "Blocked" → Orange background
- Status "Resolved" → Green background

**Summary Dashboard**:
- Count by Priority
- Count by Status
- Overdue actions count
- Completion rate
- Count by Issue_Type (NEW)
- Count by Detected_In_Sheet (NEW)

---

### 5.8 Sheet 8: Metadata

**Purpose**: Workbook generation and version tracking

**UPDATED**: Now tracks 15-sheet structure

**Content**:

| Field | Example Value |
|-------|---------------|
| Workbook_Version | 1.0 |
| Total_Sheets | 15 |
| Generation_Date | 10.01.2025 14:30:00 |
| Generator_Script | generate_a57_1_sources.py |
| Script_Version | 2.0.0 |
| Python_Version | 3.12.1 |
| openpyxl_Version | 3.1.2 |
| Last_Modified_Date | [Auto-updated on save] |
| Last_Modified_By | [Auto-updated USER()] |
| Modification_Count | [Incremented on save] |
| Related_Policy | ISMS-POL-A.5.7 |
| Related_IMP_Spec | ISMS-IMP-A.5.7.1 v1.0 |
| CVSS_Support_Added | v1.0 (10.01.2025) |
| Vendor_Mgmt_Added | v1.0 (10.01.2025) |
| Audit_Evidence_Added | v1.0 (10.01.2025) |

**Validation Rules Applied**:
- List of all data validation rules
- List of all conditional formatting rules
- List of all cross-sheet formula references

**Changelog**:

v1.0 (10.01.2025):
- Expanded from 8 to 15 sheets
- Added CVSS_Support column to Sheet 2
- Added CVSS accuracy tracking to Sheet 3
- Added Sheets 9-13: Vendor management and integration tracking
- Added Sheet 14: Source_Performance_Validation (AUDIT CRITICAL)
- Added Sheet 15: Business_Continuity_Plan (AUDIT CRITICAL)
- Updated Sheet 7 to link to new sheets

v1.0 (Original):
- Initial 8-sheet implementation
- Source inventory, evaluation, coverage, cost, compliance

---

### 5.9 Sheet 9: Integration_Points

**Purpose**: Document technical integration capabilities for each source

**Rationale**: Understanding how sources integrate technically enables automation, reduces manual effort, and ensures consistent data ingestion. This sheet supports operational efficiency and audit evidence for technical controls.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Integration_Type | Dropdown | API, STIX/TAXII, RSS, Email, Manual, Webhook, Syslog | Yes | API |
| Integration_Target_Type | Dropdown | TIP, SIEM, SOAR, Vuln_Scanner, EDR, Ticketing, Firewall, Proxy, Custom | Yes | TIP |
| Integration_Target_Name | Text | Free text (max 100 chars) | Yes | MISP Threat Intelligence Platform |
| API_Endpoint | Text | URL format | No | https://api.crowdstrike.com/intel/v2/indicators |
| Authentication_Method | Dropdown | API_Key, OAuth2, Certificate, Basic_Auth, SAML, None | No | API_Key |
| Data_Format | Dropdown | STIX_2.1, STIX_2.0, JSON, XML, CSV, PDF, HTML, CEF, LEEF | Yes | STIX_2.1 |
| CVSS_In_Feed | Dropdown | Yes_4.0, Yes_3.1, Yes_Both, No | Yes | Yes_Both |
| TLP_Support | Dropdown | Yes, No, Partial | Yes | Yes |
| IOC_Types_Supported | Text | Comma-separated (max 200 chars) | Yes | IP, Domain, URL, Hash_MD5, Hash_SHA256, Email |
| Bidirectional | Dropdown | Yes, No, N/A | No | No |
| Integration_Status | Dropdown | Active, Degraded, Failed, Inactive, Planned | Yes | Active |
| Last_Integration_Test | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Integration_Test | Date | Auto (Last_Test + 90 days) | Auto | 02.04.2025 |
| Integration_Owner | Text | Email or department | Yes | security-ops@example.com |
| Documentation_Link | Text | URL or file path | No | https://docs.crowdstrike.com/api/intel |
| Notes | Text | Max 300 chars | No | Rate limit: 1000 calls/hour, pagination: 1000 records/call |

**Integration_Type Definitions**:
- **API**: RESTful or SOAP API with programmatic access
- **STIX/TAXII**: Structured Threat Information Expression / Trusted Automated eXchange of Intelligence Information
- **RSS**: RSS/Atom feed subscription
- **Email**: Email-based alerts or reports
- **Manual**: Manual download from web portal
- **Webhook**: Push notifications to our endpoint
- **Syslog**: Syslog protocol forwarding

**Integration_Target_Type Definitions**:
- **TIP**: Threat Intelligence Platform (e.g., MISP, ThreatConnect, Anomali)
- **SIEM**: Security Information and Event Management (e.g., Splunk, QRadar, Sentinel)
- **SOAR**: Security Orchestration, Automation, and Response (e.g., Cortex XSOAR, Splunk Phantom)
- **Vuln_Scanner**: Vulnerability scanner (e.g., Qualys, Tenable, Rapid7) - for Control 8.8 integration
- **EDR**: Endpoint Detection and Response (e.g., CrowdStrike Falcon, SentinelOne)
- **Ticketing**: Ticketing system (e.g., Jira, ServiceNow)
- **Firewall**: Next-gen firewall for IOC blocking
- **Proxy**: Web proxy for URL/domain blocking
- **Custom**: Custom integration to proprietary system

**CVSS_In_Feed Definitions**:
- **Yes_4.0**: Feed includes CVSS 4.0 scores/vectors
- **Yes_3.1**: Feed includes CVSS 3.1 scores/vectors
- **Yes_Both**: Feed includes both CVSS 4.0 and 3.1 scores
- **No**: Feed does not include CVSS scoring

**Conditional Formatting**:
- Integration_Status "Failed" → Red background (#FFC7CE)
- Integration_Status "Degraded" → Orange background (#FFD966)
- Integration_Status "Inactive" → Gray background (#D9D9D9)
- CVSS_In_Feed "No" → Yellow background (#FFEB9C)
- Last_Integration_Test > 120 days old → Orange text (overdue)

**Cross-Sheet Integration**:
- Links to Sheet 13 (API_Integration) for API-specific health metrics
- Feeds into Sheet 7 (Action_Items) if Integration_Status = "Failed" or "Degraded"

---

### 5.10 Sheet 10: Update_Frequency

**Purpose**: Track actual update frequency vs. contractual SLA

**Rationale**: Timely intelligence is critical for threat prevention. This sheet validates vendors meet their SLA commitments and identifies sources with degraded timeliness.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Contractual_Frequency | Dropdown | Real_Time, Hourly, Every_4_Hours, Every_12_Hours, Daily, Weekly, Monthly, Quarterly, Ad_Hoc | Yes | Hourly |
| Actual_Avg_Frequency | Text | Free text (describe actual) | Yes | Every 45 minutes |
| Last_Update_Received | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 14:30 |
| Update_Count_Last_30_Days | Number | Integer >= 0 | Yes | 1200 |
| Expected_Update_Count | Number | Formula based on Contractual_Frequency | Auto | 720 |
| Update_Variance | Percentage | Formula: (Actual/Expected - 1) * 100 | Auto | +66.7% |
| SLA_Met | Dropdown | Yes, No, N/A | Yes | Yes |
| SLA_Met_Justification | Text | Free text if SLA_Met = No | Conditional | N/A |
| Outage_Count_Last_Quarter | Number | Integer >= 0 | Yes | 0 |
| Longest_Outage_Duration | Text | Free text (hours/minutes) | No | N/A |
| Average_Outage_Duration | Text | Free text (hours/minutes) | No | N/A |
| Timeliness_Score | Number | 1-5 scale | Yes | 5 |
| Timeliness_Trend | Dropdown | Improving, Stable, Degrading | Yes | Stable |
| Last_SLA_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_SLA_Review | Date | Auto (Last_Review + 90 days) | Auto | 02.04.2025 |
| Notes | Text | Max 300 chars | No | Consistently exceeds SLA, high reliability |

**Expected_Update_Count Formula Logic** (conceptual):

Based on Contractual_Frequency over 30 days:
- Real_Time: 43200 (one per minute)
- Hourly: 720
- Every_4_Hours: 180
- Every_12_Hours: 60
- Daily: 30
- Weekly: 4
- Monthly: 1
- Ad_Hoc: N/A


**Timeliness_Score Scale** (1-5):
- **5**: Always meets or exceeds SLA, no outages
- **4**: Usually meets SLA, minor delays <10%
- **3**: Meets SLA 70-90% of time
- **2**: Frequently misses SLA, significant delays
- **1**: Rarely meets SLA, unreliable

**Conditional Formatting**:
- SLA_Met "No" → Red background (#FFC7CE)
- Outage_Count > 3 → Orange background (#FFD966)
- Timeliness_Score <= 2 → Red text
- Update_Variance < -20% → Yellow background (significantly under SLA)
- Last_Update_Received > 48 hours old → Red background (stale data)

**Integration with Sheet 12** (Vendor_SLAs):
- This sheet provides detailed update frequency data
- Sheet 12 aggregates SLA performance across all metrics
- Discrepancies should trigger action items in Sheet 7

---

### 5.11 Sheet 11: Source_Contacts

**Purpose**: Maintain vendor contact information for escalations and support

**Rationale**: During incidents or integration failures, rapid escalation to the right vendor contact is critical. This sheet ensures contact information is current and accessible.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Contact_Type | Dropdown | Technical_Support, Account_Manager, Emergency_Contact, Billing, Executive, Data_Protection_Officer, Security_Team | Yes | Technical_Support |
| Contact_Name | Text | Free text | Yes | John Smith |
| Contact_Title | Text | Free text | No | Senior Support Engineer |
| Contact_Email | Text | Email validation | Yes | john.smith@crowdstrike.com |
| Contact_Phone | Text | Phone format (flexible) | No | +1-555-123-4567 |
| Contact_Region | Dropdown | Global, EMEA, Americas, APAC, Switzerland, Germany, Austria | No | EMEA |
| Availability | Text | Free text | No | 24/7 for P1/P2 issues, business hours for P3/P4 |
| Escalation_Path | Text | Free text (max 200 chars) | No | L1→L2 (4 hours)→Manager (8 hours)→Director (24 hours) |
| Preferred_Contact_Method | Dropdown | Email, Phone, Portal, Slack, Teams | No | Email |
| Language_Supported | Text | Comma-separated | No | English, German, French |
| Last_Contact_Date | Date | DD.MM.YYYY | No | 15.12.2024 |
| Last_Contact_Reason | Text | Free text (max 200 chars) | No | API rate limit troubleshooting |
| Response_Quality | Number | 1-5 scale | No | 5 |
| Response_Time | Text | Free text | No | <2 hours average |
| Contact_Status | Dropdown | Active, Inactive, Replaced | Yes | Active |
| Replacement_Contact | Text | If Contact_Status = Replaced | Conditional | jane.doe@crowdstrike.com |
| Last_Verified | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Verification | Date | Auto (Last_Verified + 180 days) | Auto | 02.07.2025 |
| Notes | Text | Max 300 chars | No | Escalate API issues to John directly; billing to account manager |

**Contact_Type Definitions**:
- **Technical_Support**: First-line technical troubleshooting
- **Account_Manager**: Commercial relationship, renewals, upsells
- **Emergency_Contact**: 24/7 critical incident escalation
- **Billing**: Invoice and payment issues
- **Executive**: Executive-level escalation (e.g., VP, Director)
- **Data_Protection_Officer**: GDPR/FADP compliance queries
- **Security_Team**: Vendor's security team for security incidents

**Response_Quality Scale** (1-5):
- **5**: Excellent - responsive, knowledgeable, resolves issues quickly
- **4**: Good - generally helpful, minor delays
- **3**: Adequate - meets basic needs, some gaps
- **2**: Poor - slow response, limited knowledge
- **1**: Unacceptable - non-responsive, unhelpful

**Conditional Formatting**:
- Contact_Status "Inactive" → Gray background (#D9D9D9)
- Response_Quality <= 2 → Orange background (#FFD966)
- Last_Verified > 180 days old → Yellow background (#FFEB9C)
- Contact_Type "Emergency_Contact" → Bold font (highlight importance)

**Validation Rules**:
- Each Source_ID must have at least one Technical_Support contact
- Sources marked "Active" in Sheet 2 must have at least one Active contact
- Email format validation enforced

**Usage Notes**:
- Review and verify contacts semi-annually (180 days)
- Update immediately after personnel changes at vendor
- Document all escalations in Last_Contact_Date/Reason for trend analysis
- Poor Response_Quality (<3) should trigger vendor review

---

### 5.12 Sheet 12: Vendor_SLAs

**Purpose**: Track vendor Service Level Agreements and actual performance

**Rationale**: SLAs define the contractual obligations for TI sources. This sheet provides audit evidence that vendors meet their commitments and identifies underperformers requiring contract renegotiation or termination.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| SLA_Record_ID | Text | Auto-generated (SLA-YYYY-NNN) | Yes | SLA-2025-001 |
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(...), "[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| SLA_Metric | Dropdown | Uptime, Response_Time, Update_Frequency, Alert_Latency, False_Positive_Rate, CVSS_Accuracy, Support_Response_Time | Yes | Uptime |
| Contractual_Target | Text | Free text with units | Yes | 99.5% |
| Contractual_Target_Numeric | Number | For calculations | No | 99.5 |
| Actual_Performance | Text | Free text with units | Yes | 99.8% |
| Actual_Performance_Numeric | Number | For calculations | No | 99.8 |
| Performance_Variance | Formula | =Actual - Target | Auto | +0.3% |
| Measurement_Period | Dropdown | Last_30_Days, Last_Quarter, Last_6_Months, Last_Year, MTD, QTD, YTD | Yes | Last_Quarter |
| Measurement_Start_Date | Date | DD.MM.YYYY | Yes | 01.10.2024 |
| Measurement_End_Date | Date | DD.MM.YYYY | Yes | 31.12.2024 |
| SLA_Status | Dropdown | Met, Missed, Exceeded, N/A, Measuring | Yes | Exceeded |
| SLA_Breach_Count | Number | Integer >= 0 | Yes | 0 |
| Penalty_Clause | Dropdown | Yes, No, N/A | No | Yes |
| Penalty_Amount | Currency | Number >= 0 | No | CHF 0 |
| Penalty_Applied | Dropdown | Yes, No, Pending, N/A | No | No |
| Penalty_Application_Date | Date | If Penalty_Applied = Yes | Conditional | N/A |
| Credit_Received | Currency | Number >= 0 | No | CHF 0 |
| Escalated_To_Vendor | Dropdown | Yes, No, N/A | No | No |
| Escalation_Date | Date | If Escalated = Yes | Conditional | N/A |
| Vendor_Response | Text | Max 300 chars | No | N/A |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Review_Date | Date | Auto based on Measurement_Period | Auto | 02.04.2025 |
| Reviewer | Text | Email or name | Yes | jane.analyst@example.com |
| Notes | Text | Max 300 chars | No | Consistently exceeds uptime SLA, excellent performance |

**SLA_Metric Definitions**:
- **Uptime**: Service availability (%, typically 99.5-99.99%)
- **Response_Time**: API response latency (ms, typically <500ms)
- **Update_Frequency**: Intelligence refresh rate (per Sheet 10)
- **Alert_Latency**: Time from threat emergence to alert (hours/minutes)
- **False_Positive_Rate**: Percentage of false positive IOCs (%, typically <5%)
- **CVSS_Accuracy**: CVSS score accuracy vs. NVD (%, per Sheet 14, typically >90%)
- **Support_Response_Time**: Vendor support ticket response time (hours, typically <4 hours P1)

**SLA_Status Logic**:
- **Met**: Actual_Performance meets or marginally exceeds target (within +10%)
- **Missed**: Actual_Performance below contractual target
- **Exceeded**: Actual_Performance significantly exceeds target (>10% better)
- **N/A**: Metric not applicable or not contractually defined
- **Measuring**: Measurement period ongoing, insufficient data

**Conditional Formatting**:
- SLA_Status "Missed" → Red background (#FFC7CE)
- SLA_Status "Exceeded" → Green background (#C6EFCE)
- SLA_Breach_Count > 0 → Orange background (#FFD966)
- Penalty_Applied "Yes" → Orange text (financial impact)
- Performance_Variance < 0 → Red text (underperformance)

**Summary Calculations** (separate area):
- Total SLA metrics tracked
- % SLAs Met vs. Missed
- Total penalty amount YTD
- Total credit received YTD
- Sources with >2 SLA breaches (escalation candidates)

**Integration Points**:
- Sheet 10 (Update_Frequency) → Update_Frequency SLA data
- Sheet 14 (Source_Performance_Validation) → CVSS_Accuracy and False_Positive_Rate SLA data
- Sheet 7 (Action_Items) → Missed SLAs trigger action items

**Audit Evidence**:
This sheet provides contractual compliance evidence for ISO 27001 audits, demonstrating:
- Vendor performance monitoring
- SLA breach identification and remediation
- Financial accountability (penalties/credits)

---

### 5.13 Sheet 13: API_Integration

**Purpose**: Document API-specific integration details and health monitoring

**Rationale**: API-based intelligence feeds are critical infrastructure. This sheet tracks API health, rate limits, authentication status, and error rates to prevent service disruptions.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Dropdown | From Source_Inventory.Source_ID | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(A2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| API_Version | Text | Free text | Yes | v2.1 |
| API_Endpoint_Base | Text | URL | Yes | https://api.crowdstrike.com |
| API_Endpoint_Intel | Text | URL (specific endpoint) | No | /intel/v2/indicators |
| API_Documentation_Link | Text | URL | No | https://docs.crowdstrike.com/api |
| API_Key_Location | Text | Secret storage location | No | HashiCorp Vault: /secret/ti/crowdstrike/api_key |
| API_Key_Rotation_Frequency | Dropdown | Daily, Weekly, Monthly, Quarterly, Annually, On_Demand, Not_Rotated | No | Quarterly |
| Last_Key_Rotation | Date | DD.MM.YYYY | No | 01.10.2024 |
| Next_Key_Rotation | Date | Auto based on frequency | Auto | 01.01.2025 |
| Authentication_Method | Dropdown | API_Key, OAuth2, Bearer_Token, Certificate, Basic_Auth, SAML | Yes | API_Key |
| Authentication_Expiry | Date | DD.MM.YYYY | No | 01.06.2025 |
| Authentication_Status | Dropdown | Valid, Expiring_Soon, Expired, Unknown | Yes | Valid |
| Rate_Limit_Calls | Number | Integer (calls per hour) | Yes | 1000 |
| Rate_Limit_Data | Text | Data volume limit | No | 10 GB/day |
| Current_Usage_Calls | Number | Integer (avg calls/hour) | Yes | 400 |
| Current_Usage_Percentage | Formula | =(Current_Usage / Rate_Limit) * 100 | Auto | 40% |
| Rate_Limit_Status | Dropdown | OK, Warning, Critical | Yes | OK |
| Rate_Limit_Breaches_Last_30_Days | Number | Integer >= 0 | Yes | 0 |
| Last_Successful_Call | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 15:00 |
| Last_Failed_Call | DateTime | DD.MM.YYYY HH:MM | No | N/A |
| Last_Failed_Reason | Text | Free text (max 200 chars) | No | N/A |
| Error_Rate_Last_7_Days | Percentage | 0-100%, 2 decimals | Yes | 0.05% |
| Error_Rate_Last_30_Days | Percentage | 0-100%, 2 decimals | Yes | 0.08% |
| Common_Error_Codes | Text | Comma-separated (max 100 chars) | No | N/A |
| API_Health_Status | Dropdown | Healthy, Degraded, Failed, Maintenance | Yes | Healthy |
| Last_Health_Check | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 15:00 |
| Health_Check_Frequency | Dropdown | Real_Time, Every_5_Min, Every_15_Min, Hourly, Daily | Yes | Every_15_Min |
| Monitoring_Dashboard | Text | URL | No | https://monitor.example.com/crowdstrike |
| Alerting_Enabled | Dropdown | Yes, No | Yes | Yes |
| Alert_Threshold_Error_Rate | Percentage | 0-100% | No | 5% |
| Alert_Contacts | Text | Comma-separated emails | No | security-ops@example.com, jane.analyst@example.com |
| Retry_Policy | Text | Free text (max 200 chars) | No | Exponential backoff: 1s, 2s, 4s, 8s, 16s |
| Timeout_Setting | Text | Free text (seconds) | No | 30s connection, 60s read |
| Pagination_Limit | Number | Records per page | No | 1000 |
| Max_Concurrent_Requests | Number | Integer | No | 5 |
| Integration_Health_Score | Number | 1-5 scale | Yes | 5 |
| Last_Integration_Review | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Next_Integration_Review | Date | Auto (Last_Review + 90 days) | Auto | 02.04.2025 |
| Notes | Text | Max 300 chars | No | Pagination limit: 1000 records/call; use cursor-based pagination |

**Rate_Limit_Status Logic**:
- **OK**: Current_Usage < 70% of Rate_Limit
- **Warning**: Current_Usage 70-90% of Rate_Limit
- **Critical**: Current_Usage > 90% of Rate_Limit

**API_Health_Status Definitions**:
- **Healthy**: Error_Rate < 1%, Last_Successful_Call within expected frequency
- **Degraded**: Error_Rate 1-5%, intermittent failures
- **Failed**: Error_Rate > 5%, or Last_Successful_Call > 2x expected frequency
- **Maintenance**: Vendor-announced planned maintenance

**Integration_Health_Score Scale** (1-5):
- **5**: Healthy, <0.1% error rate, zero rate limit breaches
- **4**: Healthy, <1% error rate, rare rate limit warnings
- **3**: Degraded, 1-5% error rate, occasional issues
- **2**: Poor, >5% error rate, frequent failures
- **1**: Failed, non-functional, requires immediate intervention

**Conditional Formatting**:
- Rate_Limit_Status "Critical" → Red background (#FFC7CE)
- Rate_Limit_Status "Warning" → Orange background (#FFD966)
- API_Health_Status "Failed" → Red background (#FFC7CE)
- API_Health_Status "Degraded" → Orange background (#FFD966)
- Error_Rate_Last_7_Days > 5% → Red text
- Authentication_Status "Expiring_Soon" → Yellow background (#FFEB9C)
- Authentication_Status "Expired" → Red background (#FFC7CE)
- Last_Successful_Call > 24 hours old → Orange text (stale)

**Monitoring Best Practices**:
1. Set up automated health checks (every 15 minutes recommended)
2. Configure alerting for:
   - Error_Rate > 5%
   - Rate_Limit_Status = "Critical"
   - API_Health_Status = "Failed" or "Degraded"
   - Authentication_Expiry within 30 days
3. Review authentication credentials quarterly (minimum)
4. Rotate API keys per vendor recommendations or organizational policy
5. Document all API failures in Last_Failed_Call/Reason for trend analysis

**Integration with Other Sheets**:
- Sheet 9 (Integration_Points) → Links API technical details to integration targets
- Sheet 10 (Update_Frequency) → API health impacts update timeliness
- Sheet 12 (Vendor_SLAs) → Error rates and uptime feed SLA tracking
- Sheet 7 (Action_Items) → Failed or Degraded status triggers action items

**Audit Evidence**:
This sheet demonstrates technical control implementation:
- Secure credential storage (API_Key_Location references Vault)
- Regular authentication rotation (Last/Next_Key_Rotation)
- Continuous monitoring (Health_Check_Frequency, Monitoring_Dashboard)
- Incident response (Alert_Contacts, Retry_Policy)

---

### 5.14 Sheet 14: Source_Performance_Validation ⚠️ **AUDIT CRITICAL**

**Purpose**: Quarterly validation of source accuracy per ISMS-POL-A.5.7-S4 Section 4.4.3

**Audit Requirement**: ISO 27001:2022 Control A.5.7 requires documented evidence that threat intelligence sources are validated for accuracy and reliability. This sheet provides that evidence.

**Policy Reference**: ISMS-POL-A.5.7-S4 Section 4.4.3 mandates:
- Quarterly source validation
- Minimum sample size: 10 IOCs + 10 CVEs per source
- Target accuracy: ≥85% overall, ≥90% CVSS accuracy
- Validation failure triggers remediation actions

**Rationale**: Without systematic validation, organizations cannot demonstrate due diligence in threat intelligence quality assurance. Poor-quality intelligence leads to missed threats or wasted resources on false positives.

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Validation_ID | Text | Auto-generated (VAL-YYYYQQ-NNN) | Yes | VAL-2025Q1-001 |
| Source_ID | Dropdown | From Source_Inventory.Source_ID (Active only) | Yes | SRC-2025-001 |
| Source_Name | Formula | =IFERROR(VLOOKUP(B2,Source_Inventory!A:B,2,FALSE),"[Not Found]") | Auto | CrowdStrike Falcon Intelligence |
| Validation_Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Validation_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Validator | Text | Email or name | Yes | jane.analyst@example.com |
| Validation_Method | Text | Free text (max 200 chars) | Yes | Random sampling with cross-validation against NVD and internal SIEM logs |
| Total_Sample_Size | Number | Integer >= 20 | Yes | 20 |
| IOC_Sample_Size | Number | Integer >= 10 | Yes | 10 |
| IOC_True_Positives | Number | Integer >= 0, <= IOC_Sample_Size | Yes | 9 |
| IOC_False_Positives | Number | Integer >= 0, <= IOC_Sample_Size | Yes | 1 |
| IOC_Accuracy | Percentage | Formula: =(TP / IOC_Sample_Size) * 100 | Auto | 90.0% |
| CVE_Sample_Size | Number | Integer >= 10 | Yes | 10 |
| CVE_Accurate | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 9 |
| CVE_Inaccurate | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 1 |
| CVE_Accuracy | Percentage | Formula: =(Accurate / CVE_Sample_Size) * 100 | Auto | 90.0% |
| CVSS_Accurate_Count | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 9 |
| CVSS_Inaccurate_Count | Number | Integer >= 0, <= CVE_Sample_Size | Yes | 1 |
| CVSS_Accuracy_Rate | Percentage | Formula: =(Accurate / CVE_Sample_Size) * 100 | Auto | 90.0% |
| CVSS_Accuracy_Method | Text | Free text (max 200 chars) | Yes | Compared against NVD CVSS scores; within ±1.0 point considered accurate |
| Overall_Accuracy_Rate | Percentage | Formula: =((IOC_TP + CVE_Accurate) / Total_Sample_Size) * 100 | Auto | 90.0% |
| Admiralty_Code_Source | Dropdown | A, B, C, D, E, F | Yes | A |
| Admiralty_Code_Info | Dropdown | 1, 2, 3, 4, 5, 6 | Yes | 1 |
| Admiralty_Combined | Formula | =CONCATENATE(Source, Info) | Auto | A1 |
| Validation_Pass | Dropdown | Pass, Conditional_Pass, Fail | Yes | Pass |
| Pass_Criteria_Met | Text | Auto-calculated summary | Auto | Overall ≥85% ✓, CVSS ≥90% ✓ |
| Action_Required | Dropdown | None, Review, Improve, Deprecate | Yes | None |
| Action_Notes | Text | Max 500 chars | No | Consistently high accuracy, maintain current usage |
| Action_Item_Created | Dropdown | Yes, No, N/A | Yes | No |
| Action_Item_ID | Text | Reference to Sheet 7 | No | N/A |
| Evidence_Location | Text | File path or URL | No | \\fileserver\ISMS\Evidence\5.7.1\VAL-2025Q1-001\ |
| Reviewed_By | Text | Email or name (supervisor) | Yes | team.lead@example.com |
| Review_Date | Date | DD.MM.YYYY | Yes | 10.01.2025 |
| Next_Validation_Date | Date | Auto: =Validation_Date + 90 days | Auto | 09.04.2025 |

**Critical Validation Rules**:

1. **Sample Size Enforcement**:

   Total_Sample_Size >= 20 (MANDATORY)
   IOC_Sample_Size >= 10 (MANDATORY)
   CVE_Sample_Size >= 10 (MANDATORY)
   Total_Sample_Size = IOC_Sample_Size + CVE_Sample_Size


2. **Accuracy Balance**:

   IOC_True_Positives + IOC_False_Positives = IOC_Sample_Size
   CVE_Accurate + CVE_Inaccurate = CVE_Sample_Size
   CVSS_Accurate_Count + CVSS_Inaccurate_Count = CVE_Sample_Size


3. **Validation_Pass Logic**:

   Pass: Overall_Accuracy >= 85% AND CVSS_Accuracy >= 90%
   Conditional_Pass: Overall_Accuracy >= 80% AND CVSS_Accuracy >= 85% (requires review)
   Fail: Overall_Accuracy < 80% OR CVSS_Accuracy < 85%


4. **Action_Required Logic**:

   None: Validation_Pass = Pass
   Review: Validation_Pass = Conditional_Pass
   Improve: Validation_Pass = Fail AND source has value (can be improved)
   Deprecate: Validation_Pass = Fail AND source cannot be improved or redundant


**Formulas**:

excel
# Column S: IOC_Accuracy
=IFERROR((K2/J2)*100, "N/A")

# Column W: CVE_Accuracy  
=IFERROR((O2/N2)*100, "N/A")

# Column Z: CVSS_Accuracy_Rate
=IFERROR((Q2/N2)*100, "N/A")

# Column AB: Overall_Accuracy_Rate
=IFERROR(((K2+O2)/H2)*100, "N/A")

# Column AE: Admiralty_Combined
=IF(AND(AC2<>"", AD2<>""), CONCATENATE(AC2, AD2), "")

# Column AF: Validation_Pass
=IF(AND(AB2>=85, Z2>=90), "Pass", 
   IF(AND(AB2>=80, Z2>=85), "Conditional_Pass", "Fail"))

# Column AG: Pass_Criteria_Met
=IF(AB2>=85, "Overall ≥85% ✓", "Overall <85% ✗") & ", " & 
 IF(Z2>=90, "CVSS ≥90% ✓", "CVSS <90% ✗")

# Column AH: Action_Required
=IF(AF2="Pass", "None",
   IF(AF2="Conditional_Pass", "Review", 
      IF(AC2="A" OR AC2="B", "Improve", "Deprecate")))


**Conditional Formatting**:

1. **Overall_Accuracy_Rate** (Column AB):
   - >= 95% → Dark green background (#006100), white text
   - >= 90% → Green background (#00B050)
   - >= 85% → Light green background (#C6EFCE)
   - >= 80% → Yellow background (#FFEB9C)
   - < 80% → Red background (#FFC7CE), bold red text

2. **CVSS_Accuracy_Rate** (Column Z):
   - >= 95% → Dark green background (#006100), white text
   - >= 90% → Green background (#00B050)
   - >= 85% → Yellow background (#FFEB9C)
   - < 85% → Red background (#FFC7CE), bold red text

3. **Validation_Pass** (Column AF):
   - "Pass" → Green background (#C6EFCE)
   - "Conditional_Pass" → Orange background (#FFD966)
   - "Fail" → Red background (#FFC7CE), bold text

4. **Action_Required** (Column AH):
   - "Deprecate" → Red background (#FFC7CE), bold text
   - "Improve" → Orange background (#FFD966)
   - "Review" → Yellow background (#FFEB9C)
   - "None" → No special formatting

5. **Next_Validation_Date** (Column AO):
   - Overdue (< TODAY()) → Red background (#FFC7CE)
   - Due within 14 days → Yellow background (#FFEB9C)

**Admiralty Code Integration**:

After validation, update Sheet 3 (Source_Evaluation) with the Admiralty Code assessment:
- A1: Excellent source (Overall ≥95%, CVSS ≥95%)
- B1: Good source (Overall ≥90%, CVSS ≥90%)
- C1-C2: Acceptable source (Overall ≥85%, CVSS ≥85%)
- D4-D5: Questionable source (Overall 80-85% or CVSS 80-90%)
- E5-F6: Poor source (Overall <80% or CVSS <85%, consider deprecation)

**Quarterly Validation Process**:

**Step 1: Sample Selection** (Week 1 of Quarter)
1. Identify all Active sources from Sheet 2
2. For each source, randomly select:
   - 10 IOCs (IP addresses, domains, hashes) from last 90 days
   - 10 CVEs from last 90 days
3. Document sample selection method

**Step 2: IOC Validation** (Week 2 of Quarter)
1. Cross-validate IOCs against:
   - Internal SIEM logs (confirmed malicious activity)
   - VirusTotal / Other TI sources
   - Incident response findings
2. Classify as True Positive or False Positive
3. Document evidence for audit

**Step 3: CVE Validation** (Week 3 of Quarter)
1. For each CVE:
   - Verify CVE exists in NVD
   - Compare CVSS score with NVD (±1.0 point tolerance)
   - Check CVE description accuracy
2. Classify as Accurate or Inaccurate
3. Document discrepancies

**Step 4: Documentation & Review** (Week 4 of Quarter)
1. Complete all columns in Sheet 14
2. Calculate accuracy rates (automated formulas)
3. Assign Admiralty Code (A-F, 1-6)
4. Determine Pass/Fail status
5. Create action items in Sheet 7 if required
6. Supervisor review and approval
7. Archive evidence in designated location

**Audit Trail Requirements**:

For each validation record, maintain:
1. **Sample List**: Spreadsheet with 20 items (10 IOCs + 10 CVEs)
2. **Validation Evidence**: Screenshots, SIEM queries, NVD comparisons
3. **Cross-Validation Results**: Secondary source confirmations
4. **Discrepancy Analysis**: Detailed notes on any inaccuracies
5. **Review Approval**: Email or document with supervisor sign-off

**Evidence Storage**:
- Location: `\\fileserver\ISMS\Evidence\5.7.1\VAL-YYYYQQ-NNN\`
- Retention: 3 years minimum (per ISO 27001 requirements)
- Format: ZIP archive with README.txt explaining contents

**Integration with Other Sheets**:

- **Sheet 2** (Source_Inventory): Source_ID dropdown, Active status filter
- **Sheet 3** (Source_Evaluation): Update CVSS_Accuracy_Rate, Admiralty Code
- **Sheet 7** (Action_Items): Create action items for Fail / Deprecate statuses
- **Sheet 12** (Vendor_SLAs): CVSS_Accuracy feeds SLA tracking

**Audit Interview Questions** (Preparedness):

Auditors will likely ask:
1. "Show me the last 4 quarters of source validation records." → This sheet
2. "How do you ensure statistical validity of samples?" → Sample_Size >= 20, random selection
3. "What happens when a source fails validation?" → Action_Required column → Sheet 7 action items
4. "How do you verify CVSS accuracy?" → CVSS_Accuracy_Method column documents process
5. "Who reviews and approves validations?" → Reviewed_By, Review_Date columns

---

### 5.15 Sheet 15: Business_Continuity_Plan ⚠️ **AUDIT CRITICAL**

**Purpose**: Document business continuity for threat intelligence operations per ISMS-POL-A.5.7-S4 Section 4.4.6

**Audit Requirement**: ISO 27001:2022 Control A.5.7 requires organizations to ensure continuity of threat intelligence operations. This sheet demonstrates:
- Critical roles are identified
- Backup personnel are trained and ready
- Access credentials are documented and accessible
- Continuity testing is performed annually

**Policy Reference**: ISMS-POL-A.5.7-S4 Section 4.4.6 mandates:
- 100% critical roles with trained backup personnel
- Annual continuity testing
- Documented access for critical sources
- Maximum 24-hour recovery time for TI operations

**Rationale**: If the primary threat intelligence analyst is unavailable (illness, departure, vacation), the organization must maintain capability to:
- Monitor critical threat intelligence sources
- Respond to high-severity threats
- Update security controls based on new intelligence
- Coordinate with incident response teams

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Role_ID | Text | Auto-generated (ROLE-NNN) | Yes | ROLE-001 |
| Role_Name | Text | Free text (max 100 chars) | Yes | Threat Intelligence Team Lead |
| Role_Description | Text | Free text (max 300 chars) | Yes | Manages TI program, evaluates sources, coordinates with SOC |
| Role_Category | Dropdown | Critical, Important, Standard | Yes | Critical |
| Primary_Person_Name | Text | Free text | Yes | Jane Analyst |
| Primary_Person_Email | Text | Email validation | Yes | jane.analyst@example.com |
| Primary_Employment_Status | Dropdown | Active, On_Leave, Departed, Other | Yes | Active |
| Primary_Training_Complete | Dropdown | Yes, No, In_Progress | Yes | Yes |
| Primary_Training_Date | Date | DD.MM.YYYY | No | 15.09.2024 |
| Primary_Cert_Valid_Until | Date | DD.MM.YYYY (if applicable) | No | 15.09.2026 |
| Backup_Person_Name | Text | Free text | Yes | John Researcher |
| Backup_Person_Email | Text | Email validation | Yes | john.researcher@example.com |
| Backup_Employment_Status | Dropdown | Active, On_Leave, Departed, Other | Yes | Active |
| Backup_Training_Complete | Dropdown | Yes, No, In_Progress | Yes | Yes |
| Backup_Training_Date | Date | DD.MM.YYYY | No | 20.09.2024 |
| Backup_Cert_Valid_Until | Date | DD.MM.YYYY (if applicable) | No | 20.09.2026 |
| Backup_Ready_Percentage | Number | 0-100% (assessor judgment) | Yes | 90 |
| Critical_Sources_Count | Number | Integer >= 0 | Yes | 5 |
| Critical_Sources_List | Text | Comma-separated Source_IDs | No | SRC-2025-001, SRC-2025-003, SRC-2025-007 |
| Access_Documented | Dropdown | Yes, No, Partial | Yes | Yes |
| Access_Documentation_Location | Text | File path or secret management system | No | HashiCorp Vault: /secret/ti/access_matrix |
| Access_Documentation_Format | Text | Free text | No | Excel spreadsheet with credentials, 2FA backup codes |
| Access_Last_Verified | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Access_Next_Verification | Date | Auto: =Last_Verified + 180 days | Auto | 02.07.2025 |
| Last_Continuity_Test_Date | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Last_Test_Duration | Text | Free text (hours/minutes) | No | 4 hours |
| Last_Test_Scenario | Text | Free text (max 200 chars) | No | Primary unavailable, backup assumes all TI duties for 1 day |
| Last_Test_Result | Dropdown | Pass, Partial_Pass, Fail, Not_Tested | Yes | Pass |
| Last_Test_Issues | Text | Free text (max 300 chars) | No | Minor delay accessing one source (resolved) |
| Last_Test_Evidence | Text | File path or URL | No | \\fileserver\ISMS\Evidence\5.7.1\Continuity\2024-12-15_Test_Report.pdf |
| Next_Test_Date | Date | Auto: =Last_Test + 365 days | Auto | 15.12.2025 |
| Compliance_Status | Formula | Complex logic (see below) | Auto | Compliant |
| Non_Compliance_Reasons | Text | Auto-populated if Non-Compliant | Auto | N/A |
| Remediation_Required | Dropdown | Yes, No | Yes | No |
| Remediation_Action_ID | Text | Reference to Sheet 7 | No | N/A |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 10.01.2025 |
| Next_Review_Date | Date | Auto: =Last_Review + 180 days | Auto | 10.07.2025 |
| Reviewer | Text | Email or name | Yes | ciso@example.com |
| Notes | Text | Max 500 chars | No | Both primary and backup attended external TI training in Q4 2024 |

**Role_Category Definitions**:

**Critical Roles** (100% backup + access required):
- Roles whose absence >24 hours would disrupt TI operations or incident response
- Examples:
  - Threat Intelligence Team Lead
  - Primary Threat Analyst
  - TI Platform Administrator
  - SOC Threat Intelligence Liaison

**Important Roles** (backup recommended but not mandatory):
- Roles whose absence could cause delays but not service disruption
- Examples:
  - Secondary Threat Analysts
  - TI Report Reviewers
  - Integration Specialists
  - Vulnerability Intelligence Analysts

**Standard Roles** (no continuity requirement):
- Read-only consumers of threat intelligence
- Recipients of TI reports
- Management stakeholders

**Compliance_Status Formula Logic**:

excel
=IF(
  AND(
    C2="Critical",
    G2="Active",
    I2="Yes",
    K2="Active",
    N2="Yes",
    Q2>=80,
    S2="Yes",
    Y2="Pass",
    Z2<>"",
    TODAY()-Y2<=365
  ),
  "Compliant",
  IF(
    C2="Critical",
    "Non-Compliant",
    "N/A"
  )
)


**Compliance Criteria for Critical Roles**:
1. Primary_Employment_Status = "Active"
2. Primary_Training_Complete = "Yes"
3. Backup_Employment_Status = "Active"
4. Backup_Training_Complete = "Yes"
5. Backup_Ready_Percentage >= 80%
6. Access_Documented = "Yes"
7. Last_Test_Result = "Pass" (or "Partial_Pass" with justification)
8. Last_Continuity_Test_Date within 365 days

**Non_Compliance_Reasons Formula** (auto-populated):

excel
=IF(
  AG2="Compliant" OR C2<>"Critical",
  "N/A",
  CONCATENATE(
    IF(G2<>"Active", "Primary not active; ", ""),
    IF(I2<>"Yes", "Primary training incomplete; ", ""),
    IF(K2<>"Active", "Backup not active; ", ""),
    IF(N2<>"Yes", "Backup training incomplete; ", ""),
    IF(Q2<80, "Backup readiness <80%; ", ""),
    IF(S2<>"Yes", "Access not documented; ", ""),
    IF(Y2="Fail", "Last test failed; ", ""),
    IF(TODAY()-Y2>365, "Annual test overdue; ", "")
  )
)


**Conditional Formatting**:

1. **Role_Category** (Column C):
   - "Critical" → Bold text, blue background (#D9E1F2)

2. **Primary/Backup_Training_Complete** (Columns I, N):
   - For Critical roles + "No" → Red background (#FFC7CE)
   - For Critical roles + "In_Progress" → Yellow background (#FFEB9C)

3. **Backup_Ready_Percentage** (Column Q):
   - >= 90% → Green background (#C6EFCE)
   - >= 80% → Light green background (#E7F4E4)
   - >= 70% → Yellow background (#FFEB9C)
   - < 70% AND Critical role → Red background (#FFC7CE)

4. **Access_Documented** (Column S):
   - For Critical roles + "No" or "Partial" → Red background (#FFC7CE)

5. **Last_Test_Result** (Column Y):
   - "Pass" → Green background (#C6EFCE)
   - "Partial_Pass" → Orange background (#FFD966)
   - "Fail" → Red background (#FFC7CE), bold text
   - "Not_Tested" AND Critical role → Red background (#FFC7CE)

6. **Next_Test_Date** (Column AA):
   - Overdue (< TODAY()) AND Critical role → Red background (#FFC7CE)
   - Due within 30 days → Yellow background (#FFEB9C)

7. **Compliance_Status** (Column AG):
   - "Compliant" → Green text, bold
   - "Non-Compliant" → Red text, bold, red background (#FFC7CE)
   - "N/A" → Gray text

**Annual Continuity Testing Process**:

**Pre-Test Planning** (30 days before):
1. Schedule test date (avoid peak operational periods)
2. Notify primary and backup personnel
3. Prepare test scenario (e.g., "Primary on unexpected leave")
4. Identify critical tasks backup must perform
5. Gather access credentials and documentation

**Test Execution** (Test Day):
1. Simulate primary unavailability (primary does not participate)
2. Backup assumes all critical role responsibilities:
   - Log into all critical TI sources
   - Retrieve latest threat intelligence
   - Generate sample threat report
   - Escalate mock high-severity threat
   - Update SIEM with new IOCs
3. Time-box test (e.g., 4 hours or full day)
4. Observe backup performance, document issues

**Post-Test Review** (Within 7 days):
1. Debrief with primary, backup, and supervisor
2. Document test results in Sheet 15
3. Identify gaps:
   - Missing credentials
   - Insufficient training
   - Documentation issues
   - Process ambiguities
4. Create action items in Sheet 7 for remediation
5. Update access documentation if needed
6. Archive test report in evidence folder

**Test Result Criteria**:

**Pass**:
- Backup successfully accessed all critical sources
- Backup completed all critical tasks within reasonable time
- No critical failures (minor issues acceptable)
- Evidence: Test report, backup logs, supervisor sign-off

**Partial_Pass**:
- Backup accessed most critical sources (≥80%)
- Backup completed critical tasks with assistance
- Minor failures that did not prevent mission completion
- Action items created for identified gaps

**Fail**:
- Backup could not access critical sources
- Backup unable to complete critical tasks
- Major failures that prevented mission completion
- Immediate remediation required

**Access Documentation Requirements**:

Critical sources (from Sheet 15, Column R) must have documented:
1. **Account Credentials**:
   - Username/email
   - Password location (e.g., Vault path)
   - 2FA backup codes location
   - API keys/tokens location

2. **Access Procedures**:
   - Login URLs
   - VPN requirements
   - Multi-factor authentication steps
   - Emergency contact procedures

3. **Operational Procedures**:
   - How to retrieve intelligence
   - How to escalate urgent threats
   - How to update SIEM/TIP
   - Communication protocols

**Storage**: 
- **Primary**: Secure password manager / secrets vault (e.g., HashiCorp Vault, 1Password, Keeper)
- **Backup**: Encrypted USB drive in secure safe (offline backup for vault failure)
- **Access**: Documented in Column T (Access_Documentation_Location)

**Integration with Other Sheets**:

- **Sheet 2** (Source_Inventory): Critical_Sources_List references Source_IDs
- **Sheet 7** (Action_Items): Failed tests or non-compliance create action items
- **Sheet 11** (Source_Contacts): Backup personnel need vendor contact information

**Audit Interview Questions** (Preparedness):

Auditors will likely ask:
1. "Show me evidence of your last business continuity test." → Last_Test_Evidence column
2. "Can your backup personnel access all critical sources?" → Access_Documented = Yes, test results
3. "What happens if your TI Team Lead departs suddenly?" → Backup_Person fields, training records
4. "How often do you test business continuity?" → Last/Next_Test_Date columns (annually)
5. "What defines a 'critical' role?" → Role_Category definitions above

---

## 6. Assessment Methodology

### 6.1 Admiralty Code Application

**Source Reliability (A-F)**:
- Review historical accuracy of source (Sheet 14 validation data)
- Assess corroboration with other sources
- Evaluate vendor reputation and expertise
- Consider false positive/negative rates
Factor in CVSS accuracy rate (Sheet 14)

**Information Credibility (1-6)**:
- Verify against internal telemetry
- Cross-reference with other TI sources
- Validate IOCs in test environment
- Assess plausibility and context

**Updated Admiralty Code Mapping** (incorporating CVSS accuracy):

| Overall Accuracy | CVSS Accuracy | Admiralty Code | Recommendation |
|------------------|---------------|----------------|----------------|
| ≥95% | ≥95% | A1 | Excellent - primary source |
| ≥90% | ≥90% | B1 | Very good - trusted source |
| ≥85% | ≥90% | B2 | Good - maintain usage |
| ≥85% | ≥85% | C2 | Acceptable - monitor closely |
| 80-85% | 80-85% | D3 | Questionable - review needed |
| <80% | <85% | E5-F6 | Poor - consider deprecation |

### 6.2 Quality Scoring

**Timeliness**: How quickly does the source provide actionable intelligence?  
**Relevance**: How applicable is the intelligence to our threat landscape?  
**Actionability**: Can we immediately operationalize the intelligence?

**Overall Quality**: Average of three scores, weighted equally

**NEW - CVSS Accuracy Assessment**:
- Sample minimum 20 CVEs per quarter
- Compare against NVD CVSS scores
- Tolerance: ±1.0 point considered accurate
- Document methodology in Sheet 14

### 6.3 Coverage Gap Analysis

1. Map current sources to coverage matrix (Sheet 4)
2. Identify categories with <2 sources
3. Prioritize gaps based on organizational risk profile
4. Recommend new sources or enhance existing coverage
5. **NEW**: Ensure CVSS 4.0 support for vulnerability coverage

### 6.4 Vendor Management Assessment

**Integration Health** (Sheets 9, 13):
- API availability and error rates
- Rate limit compliance
- Authentication status
- Data format compatibility

**SLA Compliance** (Sheets 10, 12):
- Update frequency vs. contractual commitments
- Uptime performance
- Support response times
- CVSS accuracy (per Sheet 14)

**Vendor Relationship** (Sheet 11):
- Contact accessibility and responsiveness
- Escalation procedures documented
- Multi-region support availability

### 6.5 Audit Evidence Collection

**Quarterly Validation** (Sheet 14):
- Sample selection methodology
- Cross-validation sources
- Evidence storage and retention
- Supervisor review and approval

**Business Continuity** (Sheet 15):
- Role criticality definitions
- Training completion records
- Annual test execution and results
- Access documentation verification

---

## 7. Integration Points

### 7.1 Internal Integration (ISMS Control A.5.7)

**To ISMS-IMP-A.5.7.2** (Collection & Analysis):
- Sheet 2: Source_Inventory.Source_ID → Analysis input sources
- Sheet 3: Source_Evaluation.Quality_Rating → Intelligence weighting
- Sheet 14: Validation_Quarter data → Quarterly quality trends

**To ISMS-IMP-A.5.7.3** (Integration & Distribution):
- Sheet 9: Integration_Points → TIP/SIEM/SOAR integration status
- Sheet 13: API_Integration → Technical integration health
- Sheet 11: Source_Contacts → Vendor escalation procedures

**To ISMS-IMP-A.5.7.4** (Effectiveness Dashboard):
- All sheets → External references for KPI calculations
- Sheet 7: Action_Items.Status → Program health metrics
- Sheet 14: Overall_Accuracy_Rate → Quality KPIs
- Sheet 15: Compliance_Status → Continuity KPIs

**To ISMS-IMP-A.5.7.5** (Standalone Dashboard):
- Subset of critical KPIs for executive visibility
- Sheet 14: Quarterly validation pass/fail rates
- Sheet 12: SLA compliance summary

### 7.2 External Integration (Other ISMS Controls)

**From Control 8.8** (Management of Technical Vulnerabilities):
- Vulnerability scanner findings → Coverage_Matrix verification
- CVSS 4.0 requirements → Source_Inventory.CVSS_Support filtering
- Emergency patching needs → Update_Frequency SLA validation
- VulnerabilityThreatLink schema → Cross-control data exchange

**To SIEM/SOC Operations**:
- Sheet 2: Active source list → SIEM feed configuration
- Sheet 9: Integration_Points → Feed health monitoring
- Sheet 13: API_Integration → Alert configuration for failures
- Sheet 14: False_Positive_Rate → SIEM tuning data

**From Finance**:
- Invoice data → Sheet 5 (Cost_Analysis) validation
- Budget allocations → Cost_Analysis.Budget_Next_Year
- Vendor payment status → Contract renewal decisions

**To Procurement**:
- Sheet 7: Action_Items (contract-related) → Procurement queue
- Sheet 12: SLA breach data → Vendor performance reviews
- Sheet 5: ROI analysis → Budget justification

**To Legal/Compliance**:
- Sheet 6: Compliance_Check data → DPA renewal tracking
- Sheet 11: Vendor contacts (DPO) → GDPR/FADP inquiries
- Sheet 14: Validation evidence → ISO 27001 audit trail

---

## 8. Evidence Requirements

### 8.1 Required Documentation (All Sources)

**Vendor Contracts & Agreements**:
- Master Service Agreement (MSA)
- Statement of Work (SOW)
- Service Level Agreement (SLA)
- Data Processing Agreement (DPA)
- Standard Contractual Clauses (SCC) if EU/CH data transfer
- Pricing schedules

**Compliance Documentation**:
- Vendor ISO 27001 / SOC 2 certificates
- Privacy policies and security whitepapers
- Subprocessor lists
- Data location certifications
- GDPR/FADP compliance attestations

**Technical Documentation**:
- API documentation
- Integration guides
- Data format specifications (STIX, JSON schemas)
- Authentication procedures
- Rate limit specifications

### 8.2 Evidence Storage

**Primary Location**: `\\fileserver\ISMS\Evidence\5.7.1-Sources\`  

**Folder Structure**:

5.7.1-Sources/
├── Contracts/
│   ├── SRC-2025-001_CrowdStrike_MSA_2024-01-15.pdf
│   ├── SRC-2025-001_CrowdStrike_DPA_2024-01-15.pdf
│   └── ...
├── Validation/
│   ├── VAL-2025Q1-001_CrowdStrike_Evidence.zip
│   ├── VAL-2025Q1-001_CrowdStrike_Report.pdf
│   └── ...
├── Continuity/
│   ├── 2024-12-15_Continuity_Test_Report.pdf
│   ├── 2024-12-15_Continuity_Test_Evidence.zip
│   └── ...
├── SLA_Reports/
│   ├── 2025-Q1_SLA_Compliance_Summary.xlsx
│   └── ...
└── Access_Documentation/
    ├── TI_Access_Matrix.xlsx (encrypted)
    ├── Critical_Sources_Credentials.keepass
    └── ...


**Naming Conventions**:
- Contracts: `[Source_ID]_[Vendor]_[Document_Type]_[Date].pdf`
- Validation: `[Validation_ID]_[Vendor]_[Type].[ext]`
- Tests: `[YYYY-MM-DD]_[Test_Type]_[Result].[ext]`

**Retention**:
- Contracts: Per organizational records management policy (default: 7 years post-termination)
- Validation evidence: 3 years minimum (ISO 27001 requirement)
- Continuity tests: 3 years minimum
- SLA reports: 3 years minimum

### 8.3 Audit-Ready Evidence Checklist

For ISO 27001:2022 Control A.5.7 audits, prepare:

**Source Quality Evidence**:
- [ ] Last 4 quarters of Sheet 14 validation records
- [ ] Sample lists with cross-validation sources
- [ ] Admiralty Code justifications (Sheet 3)
- [ ] Action items created for failed validations

**Business Continuity Evidence**:
- [ ] Current Sheet 15 with all Critical roles documented
- [ ] Last annual continuity test report + evidence
- [ ] Training records for primary and backup personnel
- [ ] Access documentation location and verification

**Vendor Management Evidence**:
- [ ] SLA compliance reports (Sheet 12)
- [ ] API integration health dashboards (Sheet 13)
- [ ] Vendor contact list with verification dates (Sheet 11)
- [ ] Integration status for all active sources (Sheet 9)

**Compliance Evidence**:
- [ ] DPAs for all sources handling PII (Sheet 6)
- [ ] GDPR/FADP compliance attestations
- [ ] SCCs for EU/CH data transfers
- [ ] Privacy policy links and review dates

---

## 9. Completion Instructions

### 9.1 Initial Assessment (New Deployment)

**Estimated Time**: 3-5 days for organization with 15-20 sources

**Phase 1: Core Source Data** (Day 1-2)
1. Populate Sheet 2 (Source_Inventory) with all current sources
   - Include CVSS_Support for each source
   - Verify contract dates and ownership
2. Complete Sheet 3 (Source_Evaluation) for each active source
   - Assign Admiralty Codes
   - Note: Initial CVSS accuracy may be "N/A" until first validation
3. Fill Sheet 4 (Coverage_Matrix) to identify gaps
4. Document costs in Sheet 5 (Cost_Analysis)
5. Verify compliance in Sheet 6 (Compliance_Check)

**Phase 2: Vendor Management** (Day 3)
6. Complete Sheet 9 (Integration_Points) for all sources
7. Fill Sheet 10 (Update_Frequency) with SLA commitments
8. Populate Sheet 11 (Source_Contacts) with current vendor contacts
9. Document SLAs in Sheet 12 (Vendor_SLAs)
10. Configure Sheet 13 (API_Integration) for API-based sources

**Phase 3: Audit Evidence** (Day 4-5)
11. Perform initial validation in Sheet 14 (Source_Performance_Validation)
    - May use historical data if available
    - Otherwise, document as "Baseline - First Validation"
12. Document continuity in Sheet 15 (Business_Continuity_Plan)
    - Identify Critical roles
    - Assign backup personnel
    - Document access locations
    - Schedule first annual test
13. Generate initial action items in Sheet 7 for any issues identified

**Phase 4: Review & Approval**
14. Internal review by TI Team Lead
15. Review by CISO or Security Manager
16. Final approval and baseline establishment

### 9.2 Quarterly Review

**Estimated Time**: 6-8 hours per quarter

**Week 1 of Quarter** (2 hours):
1. Update Sheet 2 (Source_Inventory):
   - Add new sources
   - Update status changes (Active → Inactive, etc.)
   - Update CVSS_Support if vendors upgrade
   - Verify contract renewal dates
2. Quick review of Sheets 9-13:
   - Verify integration status
   - Check for new API issues
   - Update vendor contacts if changed

**Week 2-3 of Quarter** (3-4 hours):
3. **CRITICAL**: Complete Sheet 14 quarterly validation:
   - Sample 10 IOCs + 10 CVEs per source
   - Cross-validate accuracy
   - Calculate accuracy rates (automated formulas)
   - Assign Admiralty Codes
   - Create action items if validation fails
4. Update Sheet 3 with validation results:
   - Update CVSS_Accuracy_Rate from Sheet 14
   - Update Admiralty Code if changed
   - Update Recommendation if needed

**Week 4 of Quarter** (1-2 hours):
5. Review Sheet 12 (Vendor_SLAs):
   - Update actual performance metrics
   - Document any SLA breaches
   - Escalate to vendors if needed
6. Review Sheet 15 (Business_Continuity_Plan):
   - Verify backup personnel still Active
   - Check training expiration dates
   - Update if personnel changes
7. Update/close action items in Sheet 7
8. Quarterly review meeting with stakeholders

### 9.3 Annual Review (Additional Tasks)

**Estimated Time**: 2-3 days annually (in addition to quarterly review)

**Business Continuity Test** (8-16 hours):
1. Execute annual continuity test per Sheet 15 procedures
2. Document test results and evidence
3. Update Sheet 15 with test outcomes
4. Create action items for any gaps

**Strategic Review** (8-12 hours):
5. Comprehensive coverage gap analysis (Sheet 4)
6. Cost-benefit analysis for all commercial sources (Sheet 5)
7. Vendor performance review (Sheets 10, 12)
8. Integration optimization (Sheets 9, 13)
9. Compliance verification (Sheet 6)
10. Source portfolio optimization:
    - Consider new sources for gaps
    - Deprecate underperforming sources
    - Renegotiate contracts based on SLA data

**Documentation Update**:
11. Update ISMS-IMP-A.5.7.1 specification if needed
12. Update generator script if new requirements
13. Archive previous year's evidence
14. Management review and approval

---

## 10. Validation Rules

### 10.1 Automated Validation (Generator Script)

**Data Integrity**:
- Source_ID uniqueness across all sheets
- Date logic (Contract_End > Contract_Start, Next_Review > Last_Review)
- Email format validation
- URL format validation
- Required field completeness

**Cross-Sheet References**:
- Sheet 9-15 Source_ID dropdowns reference Sheet 2
- VLOOKUP formulas include IFERROR wrappers
- Named ranges properly defined
- No broken references

**Formula Validation**:
- Accuracy calculations in Sheet 14
- Compliance status in Sheet 15
- Cost calculations in Sheet 5
- ROI calculations in Sheet 5
- SLA variance in Sheet 12

**Conditional Formatting**:
- All color codes consistent (use standard palette)
- Formatting rules don't conflict
- Performance-friendly (avoid volatile functions)

### 10.2 Business Logic Validation (Manual Review)

**Sheet 2 (Source_Inventory)**:
- All Active sources must have Last_Review_Date within 180 days
- Commercial sources must have Contract_End date
- Sources with Status = "Pending_Renewal" must have Contract_End within 90 days

**Sheet 3 (Source_Evaluation)**:
- All active sources must have evaluation within 90 days
- Sources with CVSS_Support ≠ "None" should have CVSS_Accuracy_Rate populated
- Recommendation "Discontinue" must have action item in Sheet 7

**Sheet 14 (Source_Performance_Validation)**:
- All Active sources must have validation within 90 days
- Sample sizes meet minimums (≥10 IOC, ≥10 CVE)
- Validation_Pass = "Fail" must have Action_Item_Created = "Yes"
- Evidence_Location must be documented for all validations

**Sheet 15 (Business_Continuity_Plan)**:
- All Critical roles must have Compliance_Status = "Compliant"
- Last_Continuity_Test_Date must be within 365 days for Critical roles
- Non-Compliant Critical roles must have Remediation_Action_ID

**Sheet 6 (Compliance_Check)**:
- Sources with PII must have FADP/GDPR compliance documented
- Commercial sources must have DPA if handling PII
- DPA_Expiry_Date must be > TODAY() or have renewal action item

### 10.3 Validation Script

**Script**: `excel_sanity_check_a57_1.py`  
**Validation**: Now validates 15 sheets

**Runs**: 
- On-demand via CLI
- Automated monthly (scheduled task)
- Before management review
- Before audit

**Outputs**: 
- Validation report (JSON, HTML, or text)
- Pass/Fail/Warning status per check
- Detailed error messages with row references
- Suggested remediation actions

**Critical Checks**:
- Sheet 14: Quarterly validation completeness
- Sheet 14: Minimum sample sizes enforced
- Sheet 15: Critical role compliance verification
- Sheet 15: Annual test currency (<365 days)
- All sheets: VLOOKUP error checking
- All sheets: Orphaned Source_IDs (referenced but not in Sheet 2)

---

## 11. Related Documents

**Policy Framework**:
- ISMS-POL-A.5.7 (Threat Intelligence Policy - Master Document)
- ISMS-POL-A.5.7-S1 (Purpose, Scope, Definitions)
- ISMS-POL-A.5.7-S2 (Threat Intelligence Requirements)
- ISMS-POL-A.5.7-S3 (Roles and Responsibilities)
- ISMS-POL-A.5.7-S4 (Policy Governance) - **Sections 4.4.3, 4.4.6 are audit critical**
- ISMS-POL-A.5.7-S5 (Annexes)

**Implementation Specifications**:
- ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment)
- ISMS-IMP-A.5.7.4 (Effectiveness Dashboard)
- ISMS-IMP-A.5.7.5 (Standalone Dashboard)

**Cross-Control Integration**:
- ISMS-IMP-A.8.8 (Management of Technical Vulnerabilities) - CVSS integration
- ISMS-POL-A.8.8 (Vulnerability Management Policy) - VulnerabilityThreatLink schema

**External References**:
- ISO/IEC 27001:2022 Annex A Control A.5.7
- MITRE ATT&CK Framework v18.1
- NIST SP 800-150 (Guide to Cyber Threat Information Sharing)
- Admiralty Code for Intelligence Evaluation
- CVSS 4.0 Specification (FIRST.org)
- STIX 2.1 Specification

**Templates & Tools**:
- Data Protection Impact Assessment (DPIA) template
- Vendor DPA template
- Standard Contractual Clauses (SCC) template
- Business Continuity Test Report template

---

## 12. Appendices

### Appendix A: Admiralty Code Quick Reference


Source Reliability + Information Credibility = Intelligence Grade

Reliability (Source):
A = Completely reliable (≥95% accuracy)
B = Usually reliable (90-95% accuracy)
C = Fairly reliable (85-90% accuracy)
D = Not usually reliable (80-85% accuracy)
E = Unreliable (<80% accuracy)
F = Reliability cannot be judged (insufficient data)

Credibility (Information):
1 = Confirmed by other sources
2 = Probably true
3 = Possibly true
4 = Doubtful
5 = Improbable
6 = Truth cannot be judged

Examples:
Best: A1, B1, A2 (high-confidence intelligence)
Good: B2, C1, C2 (actionable intelligence)
Use with caution: D3, D4, E5 (low-confidence intelligence)
Avoid: F6 (no basis for judgment)

Operational Guidance:
- A1/B1: Use immediately for decision-making
- C2/D3: Corroborate before acting
- E5/F6: Use only for awareness, not action


### Appendix B: CVSS 4.0 vs. 3.1 Comparison

| Aspect | CVSS 4.0 | CVSS 3.1 | Notes |
|--------|----------|----------|-------|
| **Release Date** | Nov 2023 | Jun 2019 | 4.0 is current standard |
| **Score Range** | 0.0-10.0 | 0.0-10.0 | Same range, different calculation |
| **Metrics** | Base, Threat, Environmental, Supplemental | Base, Temporal, Environmental | 4.0 adds Supplemental metrics |
| **OT/IoT Support** | Native support | Limited | 4.0 better for OT environments |
| **Granularity** | Improved (e.g., "Safety" metric) | Standard | 4.0 more nuanced |
| **Adoption** | Growing (2024-2025) | Widespread | 3.1 still dominant in 2025 |

**Recommendation for [Organization]**:
- Prefer sources with "4.0 Full" or "4.0 Basic" support
- Accept "3.1 Full" as current standard (transition period)
- Flag "2.0 Only" for deprecation planning (obsolete)
- Avoid "None" / "Proprietary" for vulnerability tracking

### Appendix C: Sample Cost-Benefit Analysis

**Example: Commercial TI Platform**

| Metric | Value | Calculation |
|--------|-------|-------------|
| Annual Cost | CHF 50,000 | Contract price |
| Alerts Per Month | 150 | From SIEM integration |
| Incidents Prevented | 2 per year | Conservative estimate |
| Avg Incident Cost | CHF 100,000 | Industry benchmark |
| Estimated Savings | CHF 200,000 | 2 × CHF 100,000 |
| ROI Ratio | 4.0 | 200,000 / 50,000 |
| ROI Category | Good | 3.0-5.0 range |

**Sensitivity Analysis**:
- If only 1 incident prevented: ROI = 2.0 (break-even+)
- If 3 incidents prevented: ROI = 6.0 (excellent)
- Cost threshold for "Good" ROI: CHF 66,666 (at 2 incidents)

### Appendix D: Coverage Gap Prioritization Matrix

**Prioritization Framework**: Risk-based approach

| Risk Level | Coverage | Geography | Sector | Threat Type | Action |
|------------|----------|-----------|--------|-------------|--------|
| **Critical** | 0 sources | Switzerland, DACH | Financial | Ransomware, APT | Immediate acquisition |
| **High** | 1 source | Core markets | Critical Infra | Data Breach | Acquire within Q |
| **Medium** | 1 source | Adjacent markets | Other sectors | Phishing, DDoS | Plan for next FY |
| **Low** | 2+ sources | Any | Any | Any | Monitor, no action |

**Decision Criteria**:
1. **Business Impact**: What's the financial/operational impact if we miss a threat?
2. **Threat Likelihood**: How often do threats target this geography/sector?
3. **Current Visibility**: Do we have ANY coverage, or complete blind spot?
4. **Alternative Controls**: Can we compensate with other controls (e.g., EDR, WAF)?

**Example**: 
- Gap: Only 1 source covering Swiss financial sector ransomware
- Risk Level: **High** (critical sector + high likelihood)
- Action: Acquire additional source within Q1 2025
- Budget: Up to CHF 25,000 (half of primary source cost)

### Appendix E: Business Continuity Test Scenarios

**Scenario 1: Primary Analyst Unexpected Leave**
- **Trigger**: Primary TI analyst on medical leave (unplanned)
- **Duration**: 1 week simulation
- **Test Objective**: Backup can perform all critical functions
- **Success Criteria**: All sources accessed, daily report generated, urgent threat escalated

**Scenario 2: Platform Administrator Departure**
- **Trigger**: TI platform admin departs (planned)
- **Duration**: 2 days simulation
- **Test Objective**: Backup can administer TIP, manage integrations
- **Success Criteria**: User accounts managed, feeds reconfigured, no service disruption

**Scenario 3: Team Lead on Vacation**
- **Trigger**: TI Team Lead on vacation (planned)
- **Duration**: 2 weeks actual (not simulation)
- **Test Objective**: Operations continue without escalation to Team Lead
- **Success Criteria**: Routine operations maintained, only critical issues escalated to CISO

**Scenario 4: Disaster Recovery**
- **Trigger**: TIP platform failure, credentials vault inaccessible
- **Duration**: 4 hours simulation
- **Test Objective**: Recover access to critical sources from backup documentation
- **Success Criteria**: Access restored within 4 hours using offline backup

---

## 13. Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification with 15 sheets including CVSS capability assessment, vendor management, and audit evidence requirements | ISMS Implementation Team |

---

**END OF SPECIFICATION v1.0**

**Document Status**: Ready for generator implementation  
**Generator Script**: `generate_a57_1_sources.py`  
**Expected Output**: `ISMS_A_5_7_1_Sources_Assessment_YYYYMMDD.xlsx` (15 sheets)  
**Sanity Check Script**: `excel_sanity_check_a57_1.py`

**Critical Path for Deployment**:
1. ✅ ISMS-IMP-A.5.7.1 specification (this document) - **COMPLETE**
2. ⏳ Update `generate_a57_1_sources.py` generator script
3. ⏳ Update `excel_sanity_check_a57_1.py` validation script
4. ⏳ Generate initial workbook
5. ⏳ Perform sanity check validation
6. ⏳ Populate with [Organization] data
7. ⏳ Internal review and approval
8. ⏳ Production deployment

**ISO 27001 Audit Readiness**:
- Sheet 14 (Source_Performance_Validation): Provides quarterly validation evidence per Control A.5.7 requirements
- Sheet 15 (Business_Continuity_Plan): Demonstrates operational resilience and succession planning
- Cross-references to ISMS-POL-A.5.7-S4 Sections 4.4.3 and 4.4.6 validated