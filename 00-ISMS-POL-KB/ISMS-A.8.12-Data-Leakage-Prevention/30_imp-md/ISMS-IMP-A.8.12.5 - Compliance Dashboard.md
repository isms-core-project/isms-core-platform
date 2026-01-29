# ISMS-IMP-A.8.12.5 - Compliance Dashboard

## DOC CONTROL

| **Attribute**           | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Document ID**         | ISMS-IMP-A.8.12.5                                                          |
| **Document Title**      | DLP Compliance Dashboard - Master Consolidation Workbook                    |
| **Control Reference**   | ISO/IEC 27001:2022 - Control A.8.12 (Data Leakage Prevention)             |
| **Related Policy**      | ISMS-POL-A.8.12 (All DLP Policies - Master Consolidation)                  |
| **Document Type**       | Implementation Assessment Specification                                     |
| **Version**             | 1.0                                                                        |
| **Status**              | Draft                                                                      |
| **Effective Date**      | 2025-01-06                                                                 |
| **Review Cycle**        | Quarterly                                                                  |
| **Document Owner**      | Chief Information Security Officer (CISO)                                  |
| **Approved By**         | CISO, CIO, DPO, Executive Management                                       |
| **Classification**      | Internal Use                                                               |

### Revision History

| **Version** | **Date**   | **Author**        | **Changes**                          |
|-------------|------------|-------------------|--------------------------------------|
| 1.0         | 2025-01-06 | ISMS Project Team | Initial specification for Domain 5   |

### Related Documents

| **Document ID**              | **Title**                                      | **Relationship**        |
|------------------------------|------------------------------------------------|-------------------------|
| ISMS-POL-A.8.12              | Data Leakage Prevention Policy (Master)        | Parent Policy           |
| ISMS-IMP-A.8.12.1            | DLP Infrastructure Assessment                  | Source Domain 1         |
| ISMS-IMP-A.8.12.2            | Data Classification Assessment                 | Source Domain 2         |
| ISMS-IMP-A.8.12.3            | Channel Coverage Assessment                    | Source Domain 3         |
| ISMS-IMP-A.8.12.4            | Monitoring & Response Assessment               | Source Domain 4         |

---

## 1. PURPOSE & SCOPE

### 1.1 Purpose

This document specifies the structure and requirements for the **Compliance Dashboard**, the master consolidation workbook that aggregates data from all 4 DLP assessment domains into a unified executive view.

**Key Assessment Areas:**
- Consolidated compliance scoring across Domains 1-4
- Executive summary (one-page CISO dashboard)
- Consolidated gap analysis and risk register
- Remediation roadmap with prioritization
- Trend analysis for quarterly compliance tracking
- Budget and resource planning

**Critical Principle (Cargo Cult Avoidance):**  
*"A dashboard that shows 100% compliance but can't stop data breaches is security theater. Real compliance means measurable protection."*

### 1.2 Scope

**In Scope:**
- Consolidation of Domains 1-4 compliance scores
- Executive-level KPIs and metrics
- All gaps from Domains 1-4
- DLP-specific risk register
- Prioritized remediation roadmap
- Quarterly trend tracking
- Budget planning and resource allocation

**Out of Scope:**
- Detailed domain assessments (covered in Domains 1-4)
- General IT budget planning (DLP-specific only)
- Non-DLP security controls

### 1.3 Relationship to DLP Framework

Domain 5 is the **master consolidation layer**:
```
ISMS-IMP-A.8.12.1 (Infrastructure) ──┐
ISMS-IMP-A.8.12.2 (Classification) ──┤
ISMS-IMP-A.8.12.3 (Channels) ────────┼──→ ISMS-IMP-A.8.12.5 (Dashboard) → Executive View
ISMS-IMP-A.8.12.4 (Monitoring) ──────┘
```

**CRITICAL - External Formulas:**  
Domain 5 workbook uses **external formulas** to pull data from Domains 1-4 workbooks using placeholder syntax:
```
=[A812-1]Summary_Dashboard!$B$17  (Domain 1 compliance)
=[A812-2]Summary_Dashboard!$B$17  (Domain 2 compliance)
=[A812-3]Summary_Dashboard!$B$23  (Domain 3 compliance)
=[A812-4]Summary_Dashboard!$B$17  (Domain 4 compliance)
```

Users must perform **Find & Replace** after generating all workbooks to update placeholders with actual filenames.

---

## 2. ASSESSMENT METHODOLOGY

### 2.1 Assessment Approach

**System Engineering Principle:**  
Domain 5 consolidates data, NOT duplicate assessments. All assessment work occurs in Domains 1-4.

**Workflow:**
1. Complete Domains 1-4 assessments first
2. Generate all 5 workbooks with consistent naming (YYYYMMDD timestamp)
3. Place all 5 workbooks in same directory
4. Open Domain 5 workbook
5. Perform Find & Replace (detailed instructions in workbook)
6. Refresh external links
7. Review consolidated metrics

### 2.2 Evidence Requirements

Evidence is collected in Domains 1-4. Domain 5 references evidence IDs from source domains.

### 2.3 Assessment Frequency

- **Initial Assessment:** After completing Domains 1-4 (Month 6)
- **Quarterly Reviews:** Update all domains, refresh Domain 5
- **Annual Audit:** Comprehensive review with updated metrics

---

## 3. WORKBOOK STRUCTURE

### 3.1 Sheet Overview

| **#** | **Sheet Name**              | **Purpose**                                    | **Rows** |
|-------|-----------------------------|------------------------------------------------|----------|
| 1     | Instructions_Legend         | Find & Replace instructions, metadata          | 60       |
| 2     | Executive_Summary           | One-page CISO dashboard (25 KPIs)              | 30       |
| 3     | Domain_Rollup_Summary       | Domains 1-4 compliance scores                  | 20       |
| 4     | Consolidated_Gap_Analysis   | All gaps from Domains 1-4                      | 100      |
| 5     | Risk_Register               | DLP-specific risks (20 pre-defined + custom)   | 40       |
| 6     | Remediation_Roadmap         | Prioritized action plan                        | 50       |
| 7     | Evidence_Master_Index       | All evidence across domains                    | 100      |
| 8     | Trend_Analysis              | Quarterly compliance tracking                  | 20       |
| 9     | KPI_Dashboard               | 25 KPIs with traffic lights                    | 30       |
| 10    | Budget_Planning             | DLP technology costs, staffing                 | 25       |
| 11    | CISO_DPO_Approval           | Final sign-off workflow                        | 15       |
| 12    | Summary_Dashboard           | Master compliance score                        | 25       |

**Total Sheets:** 12 sheets  
**Key Feature:** External formulas linking to Domains 1-4

---

## 4. SHEET SPECIFICATIONS

### 4.1 Sheet: Instructions_Legend

**Purpose:** Provide Find & Replace instructions and workbook metadata.

**Content Sections:**

1. **Document Header**
   - Workbook ID: ISMS-IMP-A.8.12.5
   - Assessment Area: Compliance Dashboard (Master Consolidation)
   - Related Domains: 1, 2, 3, 4
   - Version: 1.0

2. **CRITICAL - Find & Replace Instructions** (Large, bold, colored box)
```
   ⚠️ BEFORE USING THIS WORKBOOK - REQUIRED STEPS ⚠️
   
   This workbook contains external formulas that reference Domains 1-4.
   You MUST perform Find & Replace to update placeholders:
   
   Step 1: Generate all 5 workbooks (same date: YYYYMMDD)
   Step 2: Place all workbooks in the same directory
   Step 3: Open this workbook (Domain 5)
   Step 4: Press Ctrl+H (Find & Replace)
   Step 5: Perform the following replacements:
   
   Find: [A812-1]
   Replace: [ISMS-IMP-A.8.12.1_DLP_Infrastructure_YYYYMMDD.xlsx]
   
   Find: [A812-2]
   Replace: [ISMS-IMP-A.8.12.2_Data_Classification_YYYYMMDD.xlsx]
   
   Find: [A812-3]
   Replace: [ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]
   
   Find: [A812-4]
   Replace: [ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]
   
   Step 6: Save workbook
   Step 7: Close and re-open to refresh links
   Step 8: Click "Enable Content" and "Update Links" if prompted
   
   Example:
   If generated on 2025-01-06, replace [A812-1] with:
   [ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250106.xlsx]
```

3. **Organization Metadata** (Yellow input fields)
   - Assessment Date
   - Completed By
   - Organization Name
   - Review Cycle: Quarterly

4. **How to Use This Workbook**
   - Review Executive_Summary first (CISO one-pager)
   - Check Domain_Rollup_Summary (individual domain scores)
   - Review Consolidated_Gap_Analysis (all gaps)
   - Assess Risk_Register (DLP risks)
   - Plan Remediation_Roadmap (prioritized actions)
   - Track trends in Trend_Analysis (quarterly progress)
   - Review budget in Budget_Planning
   - Obtain sign-off in CISO_DPO_Approval

5. **Legend - Compliance Scoring**
   - ✅ Pass: Overall DLP Compliance ≥85%
   - ⚠️ Conditional Pass: 70-84% (gaps must be remediated within 90 days)
   - ❌ Fail: <70% (significant remediation required)

**Layout:** Prominent Find & Replace instructions at top (red/yellow background).

---

### 4.2 Sheet: Executive_Summary

**Purpose:** One-page CISO dashboard with 25 key KPIs.

**Content Sections:**

1. **Header**
   - Title: "DLP PROGRAM - EXECUTIVE SUMMARY"
   - Assessment Period: [Input]
   - Report Date: [Auto-generated]

2. **Overall DLP Compliance Score**

| Metric | Value | Status |
|--------|-------|--------|
| Overall DLP Program Compliance | [Formula: Weighted average] | ✅/⚠️/❌ |
| Domain 1 - Infrastructure | [External formula] | ✅/⚠️/❌ |
| Domain 2 - Classification | [External formula] | ✅/⚠️/❌ |
| Domain 3 - Channels | [External formula] | ✅/⚠️/❌ |
| Domain 4 - Monitoring | [External formula] | ✅/⚠️/❌ |

**Weighted Formula:**
```
Overall_DLP_Score = (
    Domain_1 × 25% +  # Infrastructure foundation
    Domain_2 × 20% +  # Classification supporting
    Domain_3 × 30% +  # Channels operational impact
    Domain_4 × 25%    # Monitoring effectiveness
)
```

3. **Key Metrics by Domain** (Table format)

From Domain 1 (Infrastructure):
- Total DLP technologies deployed: [External formula]
- Endpoint coverage %: [External formula]
- Email DLP coverage %: [External formula]
- SIEM integration rate: [External formula]

From Domain 2 (Classification):
- Data classification completeness %: [External formula]
- Sensitive data categories: [External formula]
- Data owners assigned %: [External formula]
- Regulatory compliance % (FADP/GDPR): [External formula]

From Domain 3 (Channels):
- Overall channel coverage %: [External formula]
- Tier 1 channels coverage (Email/Web/Endpoint): [External formula]
- Unprotected channels count: [External formula]
- Critical channel gaps: [External formula]

From Domain 4 (Monitoring):
- False positive rate %: [External formula]
- MTTD (Mean Time to Detect): [External formula]
- MTTR (Mean Time to Respond): [External formula]
- SLA compliance %: [External formula]
- Alert triage rate %: [External formula]

4. **Consolidated Metrics**

- Total gaps identified: [Formula from Consolidated_Gap_Analysis]
- Critical gaps: [Formula counting Critical risk level]
- Gaps remediated % (closed / total): [Formula]
- High-risk issues count: [Formula from Risk_Register]
- Evidence completeness %: [Formula from Evidence_Master_Index]
- CISO/DPO approval status: [From CISO_DPO_Approval sheet]

5. **Traffic Light Summary**

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ On Target | [Formula] | [%] |
| ⚠️ Close | [Formula] | [%] |
| ❌ Action Needed | [Formula] | [%] |

**Layout:** Designed for printing on 1 page (fit to page).

---

### 4.3 Sheet: Domain_Rollup_Summary

**Purpose:** Detailed breakdown of Domains 1-4 compliance scores.

**Content:** 4 sections (one per domain)

**Section 1: Domain 1 - Infrastructure**

| Metric | Value | Source |
|--------|-------|--------|
| Overall Infrastructure Compliance | [External: =[A812-1]Summary_Dashboard!$B$17] | Domain 1 |
| DLP Technologies Deployed | [External: =[A812-1]Summary_Dashboard!$B$5] | Domain 1 |
| Endpoint Coverage % | [External: =[A812-1]Summary_Dashboard!$B$6] | Domain 1 |
| Network DLP Deployed | [External: =[A812-1]Summary_Dashboard!$B$7] | Domain 1 |
| SIEM Integration Complete | [External: =[A812-1]Summary_Dashboard!$B$8] | Domain 1 |

**Section 2: Domain 2 - Classification**

| Metric | Value | Source |
|--------|-------|--------|
| Overall Classification Compliance | [External: =[A812-2]Summary_Dashboard!$B$17] | Domain 2 |
| Data Classification Complete % | [External: =[A812-2]Summary_Dashboard!$B$5] | Domain 2 |
| Sensitive Data Categories | [External: =[A812-2]Summary_Dashboard!$B$6] | Domain 2 |
| Data Owners Assigned % | [External: =[A812-2]Summary_Dashboard!$B$7] | Domain 2 |
| Regulatory Compliance % | [External: =[A812-2]Summary_Dashboard!$B$8] | Domain 2 |

**Section 3: Domain 3 - Channels**

| Metric | Value | Source |
|--------|-------|--------|
| Overall Channel Coverage Compliance | [External: =[A812-3]Summary_Dashboard!$B$23] | Domain 3 |
| Overall Channel Coverage % | [External: =[A812-3]Summary_Dashboard!$B$5] | Domain 3 |
| Email Channel Coverage % | [External: =[A812-3]Summary_Dashboard!$B$8] | Domain 3 |
| Endpoint Channel Coverage % | [External: =[A812-3]Summary_Dashboard!$B$11] | Domain 3 |
| Unprotected Channels | [External: =[A812-3]Summary_Dashboard!$B$17] | Domain 3 |

**Section 4: Domain 4 - Monitoring**

| Metric | Value | Source |
|--------|-------|--------|
| Overall Monitoring Compliance | [External: =[A812-4]Summary_Dashboard!$B$17] | Domain 4 |
| Logging Complete % | [External: =[A812-4]Summary_Dashboard!$B$8] | Domain 4 |
| SIEM Integration % | [External: =[A812-4]Summary_Dashboard!$B$10] | Domain 4 |
| False Positive Rate % | [External: =[A812-4]Summary_Dashboard!$B$11] | Domain 4 |
| SLA Compliance % | [External: =[A812-4]Summary_Dashboard!$B$12] | Domain 4 |

---

### 4.4 Sheet: Consolidated_Gap_Analysis

**Purpose:** All gaps from Domains 1-4 in one view (manual consolidation).

**Note:** This is NOT auto-populated via external formulas (too complex). Users manually copy gaps from each domain's Gap_Analysis sheet.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Source Domain             | Dropdown     | Domain 1/Domain 2/Domain 3/Domain 4 | 15        |
| B       | Gap ID                    | Text         | User input (from source domain)    | 18        |
| C       | Gap Description           | Text         | User input                         | 40        |
| D       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| E       | Business Impact           | Text         | User input                         | 30        |
| F       | Remediation Plan          | Text         | User input                         | 40        |
| G       | Owner                     | Text         | User input                         | 25        |
| H       | Target Date               | Date         | User input                         | 15        |
| I       | Status                    | Dropdown     | Not Started/In Progress/Complete/Blocked | 15        |
| J       | Evidence ID               | Text         | User input                         | 18        |

**Data Rows:** 100 rows (consolidate all gaps from 4 domains)

**Instructions at top:**
```
Copy gaps from:
- Domain 1: Gap_Analysis sheet → Paste here with "Domain 1" in Column A
- Domain 2: Gap_Analysis sheet → Paste here with "Domain 2" in Column A
- Domain 3: Gap_Analysis sheet → Paste here with "Domain 3" in Column A
- Domain 4: Gap_Analysis sheet → Paste here with "Domain 4" in Column A
```

---

### 4.5 Sheet: Risk_Register

**Purpose:** DLP-specific risk register (20 pre-defined + 20 custom).

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Risk ID                   | Text         | Auto (RISK-A812-###)               | 15        |
| B       | Risk Description          | Text         | User input                         | 40        |
| C       | Risk Category             | Dropdown     | Insider Threat/External Attack/Compliance/Operational/Technical | 20        |
| D       | Likelihood                | Dropdown     | Very High/High/Medium/Low/Very Low | 15        |
| E       | Impact                    | Dropdown     | Critical/High/Medium/Low           | 15        |
| F       | Risk Score                | Formula      | Likelihood × Impact                | 12        |
| G       | Current Controls          | Text         | User input (existing mitigations)  | 35        |
| H       | Residual Risk             | Dropdown     | Critical/High/Medium/Low           | 15        |
| I       | Mitigation Plan           | Text         | User input (additional actions)    | 35        |
| J       | Owner                     | Text         | User input                         | 20        |

**Data Rows:** 40 rows (20 pre-populated examples + 20 blank)

**Pre-Populated DLP Risk Examples:**

1. **Insider Threat - Departing Employee Data Theft**
   - Category: Insider Threat
   - Likelihood: High
   - Impact: Critical
   - Controls: DLP alerting, user monitoring
   - Residual Risk: Medium

2. **Unencrypted Email Transmission of PII**
   - Category: Compliance
   - Likelihood: Medium
   - Impact: High
   - Controls: Email DLP, encryption policies
   - Residual Risk: Low

3. **USB Device Data Exfiltration**
   - Category: Insider Threat
   - Likelihood: High
   - Impact: High
   - Controls: Endpoint DLP, USB blocking
   - Residual Risk: Medium

4. **Cloud Storage (Dropbox/Drive) Data Upload**
   - Category: External Attack / Shadow IT
   - Likelihood: Very High
   - Impact: High
   - Controls: Web DLP, CASB
   - Residual Risk: Medium

5. **Source Code Leak to GitHub**
   - Category: Operational
   - Likelihood: Medium
   - Impact: Critical
   - Controls: Web DLP, code repo monitoring
   - Residual Risk: Low

... (15 more pre-defined risks)

---

### 4.6 Sheet: Remediation_Roadmap

**Purpose:** Prioritized action plan for gap remediation.

**Columns:**

| **Col** | **Header**                | **Type**     | **Validation**                     | **Width** |
|---------|---------------------------|--------------|------------------------------------|-----------|
| A       | Priority                  | Number       | 1, 2, 3... (auto-sort)             | 10        |
| B       | Gap/Risk ID               | Text         | Reference to gap or risk           | 18        |
| C       | Action Description        | Text         | User input                         | 40        |
| D       | Domain                    | Dropdown     | Domain 1/2/3/4/Cross-Domain        | 15        |
| E       | Risk Level                | Dropdown     | Critical/High/Medium/Low           | 15        |
| F       | Effort (Days)             | Number       | User input                         | 12        |
| G       | Cost (CHF)                | Number       | User input                         | 15        |
| H       | Owner                     | Text         | User input                         | 20        |
| I       | Target Date               | Date         | User input                         | 15        |
| J       | Status                    | Dropdown     | Not Started/In Progress/Complete/Blocked | 15        |
| K       | Dependencies              | Text         | User input (other actions)         | 30        |

**Data Rows:** 50 rows

**Prioritization Guidance (in sheet header):**
```
Priority Calculation:
1. Critical Risk + High Impact = Priority 1
2. Critical Risk + Medium Impact = Priority 2
3. High Risk + High Impact = Priority 2
4. High Risk + Medium Impact = Priority 3
5. Medium Risk = Priority 4
6. Low Risk = Priority 5
```

---

### 4.7 Sheet: Evidence_Master_Index

**Purpose:** Consolidated index of all evidence from Domains 1-4.

**Note:** Manual consolidation (copy evidence IDs from each domain).

**Columns:**

| **Col** | **Header**                | **Type**     | **Width** |
|---------|---------------------------|--------------|-----------|
| A       | Source Domain             | Dropdown     | 15        |
| B       | Evidence ID               | Text         | 18        |
| C       | Evidence Type             | Dropdown     | 20        |
| D       | Description               | Text         | 35        |
| E       | Location/Link             | Text         | 30        |
| F       | Date Collected            | Date         | 15        |
| G       | Collected By              | Text         | 20        |
| H       | Verification Status       | Dropdown     | 15        |

**Data Rows:** 100 rows

---

### 4.8 Sheet: Trend_Analysis

**Purpose:** Track quarterly compliance progress.

**Content:** Historical compliance scores (4 quarters)

**Table:**

| Quarter | Domain 1 % | Domain 2 % | Domain 3 % | Domain 4 % | Overall DLP % | Total Gaps | Gaps Closed |
|---------|------------|------------|------------|------------|---------------|------------|-------------|
| Q4 2024 | [Input]    | [Input]    | [Input]    | [Input]    | [Formula]     | [Input]    | [Input]     |
| Q1 2025 | [Input]    | [Input]    | [Input]    | [Input]    | [Formula]     | [Input]    | [Input]     |
| Q2 2025 | [Input]    | [Input]    | [Input]    | [Input]    | [Formula]     | [Input]    | [Input]     |
| Q3 2025 | [Input]    | [Input]    | [Input]    | [Input]    | [Formula]     | [Input]    | [Input]     |

**Trend Chart:** Line chart showing progress over time.

---

### 4.9 Sheet: KPI_Dashboard

**Purpose:** 25 KPIs with traffic light indicators.

**Content:** All KPIs from Executive_Summary with detailed formulas.

(Detailed KPI list same as Executive_Summary section 2)

---

### 4.10 Sheet: Budget_Planning

**Purpose:** DLP technology costs and staffing requirements.

**Content Sections:**

1. **Technology Costs (Annual)**

| Item | Vendor | License Cost | Support Cost | Total Annual | Notes |
|------|--------|--------------|--------------|--------------|-------|
| Network DLP | [Input] | [Input] | [Input] | [Formula] | |
| Endpoint DLP | [Input] | [Input] | [Input] | [Formula] | |
| Email DLP | [Input] | [Input] | [Input] | [Formula] | |
| CASB / Cloud DLP | [Input] | [Input] | [Input] | [Formula] | |
| SIEM Integration | [Input] | [Input] | [Input] | [Formula] | |
| **TOTAL** | | | | [Formula] | |

2. **Staffing Requirements**

| Role | FTE | Annual Cost (CHF) | Notes |
|------|-----|-------------------|-------|
| DLP Administrator | [Input] | [Input] | |
| SOC Analysts (DLP) | [Input] | [Input] | |
| Data Privacy Officer | [Input] | [Input] | |
| Compliance Specialist | [Input] | [Input] | |
| **TOTAL** | [Formula] | [Formula] | |

3. **Total DLP Program Cost**

| Category | Annual Cost (CHF) |
|----------|-------------------|
| Technology | [Formula from section 1] |
| Staffing | [Formula from section 2] |
| Training | [Input] |
| Consulting | [Input] |
| **TOTAL** | [Formula] |

---

### 4.11 Sheet: CISO_DPO_Approval

**Purpose:** Final sign-off workflow.

**Content:**

1. **Compliance Statement**
```
   The DLP Program has been assessed across 4 domains:
   - Domain 1: Infrastructure
   - Domain 2: Data Classification
   - Domain 3: Channel Coverage
   - Domain 4: Monitoring & Response
   
   Overall DLP Compliance Score: [Formula from Summary_Dashboard]
   
   Assessment Result: [Formula: ✅ Pass / ⚠️ Conditional / ❌ Fail]
```

2. **Approval Workflow**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| DLP Administrator | [Input] | [Input] | [Input] | [Input] |
| Information Security Manager | [Input] | [Input] | [Input] | [Input] |
| CISO | [Input] | [Input] | [Input] | [Input] |
| DPO | [Input] | [Input] | [Input] | [Input] |
| CIO | [Input] | [Input] | [Input] | [Input] |
| Executive Management | [Input] | [Input] | [Input] | [Input] |

---

### 4.12 Sheet: Summary_Dashboard

**Purpose:** Master compliance score and key findings.

**Content:**

1. **Workbook Metadata**
   - Assessment Date: [Input]
   - Completed By: [Input]
   - Approved By: [Input]
   - Next Review: [Formula: +90 days]

2. **Overall DLP Program Compliance**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Domain 1 - Infrastructure | [External formula] | 85% | ✅/⚠️/❌ |
| Domain 2 - Classification | [External formula] | 85% | ✅/⚠️/❌ |
| Domain 3 - Channels | [External formula] | 85% | ✅/⚠️/❌ |
| Domain 4 - Monitoring | [External formula] | 85% | ✅/⚠️/❌ |
| **Overall DLP Compliance** | [Weighted formula] | >85% | ✅/⚠️/❌ |

3. **Key Findings**
   - Total gaps: [Formula from Consolidated_Gap_Analysis]
   - Critical gaps: [Formula]
   - High-risk issues: [Formula from Risk_Register]
   - Remediation progress %: [Formula]
   - Evidence completeness: [Formula]

---

## 5. ASSESSMENT CRITERIA & SCORING

### 5.1 Weighted Scoring Formula
```
Overall_DLP_Score = (
    Domain_1_Infrastructure × 25% +
    Domain_2_Classification × 20% +
    Domain_3_Channels × 30% +
    Domain_4_Monitoring × 25%
)
```

**Rationale:**
- Infrastructure (25%): Foundation of DLP program
- Classification (20%): Essential but supporting
- Channels (30%): Highest operational impact
- Monitoring (25%): Operational effectiveness

### 5.2 Pass/Fail Criteria

- **Pass:** Overall DLP Compliance ≥ 85%
- **Conditional Pass:** 70-84% (gaps addressed within 90 days)
- **Fail:** <70% (significant remediation required)

---

## 6. COMPLIANCE MAPPING

### 6.1 ISO/IEC 27001:2022 Mapping

Domain 5 consolidates compliance across all ISO controls addressed in Domains 1-4.

### 6.2 Regulatory Mapping

Domain 5 consolidates FADP and GDPR compliance across all domains.

---

## 7. EVIDENCE REQUIREMENTS

Evidence collected in Domains 1-4. Domain 5 provides consolidated view via Evidence_Master_Index.

---

## 8. APPROVAL & SIGN-OFF

### 8.1 Approval Workflow

1. Complete Domains 1-4
2. Consolidate gaps and risks in Domain 5
3. Review Executive_Summary (CISO)
4. Obtain sign-offs in CISO_DPO_Approval sheet
5. Present to Executive Management

### 8.2 Sign-Off Requirements

Minimum 4 signatures: CISO, DPO, CIO, Executive Management

---

**END OF DOCUMENT**

*"The difference between a dashboard and a vanity metric: A dashboard shows gaps. A vanity metric shows only success. Choose the dashboard."*  
*— Feynman-inspired ISMS Wisdom* 🎯