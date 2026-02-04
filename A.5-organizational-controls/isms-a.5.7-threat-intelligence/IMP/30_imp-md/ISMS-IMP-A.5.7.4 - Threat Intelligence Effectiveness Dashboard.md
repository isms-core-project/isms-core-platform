**ISMS-IMP-A.5.7.4 - Threat Intelligence Effectiveness Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.4 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Program Effectiveness Dashboard with Automated Data Refresh |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements), Section 3.2 (Exception Management), Section 3.4 (Policy Governance) |
| **Purpose** | Provide executive and management-level visibility into threat intelligence program effectiveness by aggregating data from all A.5.7 workbooks |
| **Target Audience** | CISO, Security Managers, Executive Management, Board, Auditors |
| **Assessment Type** | Aggregated Dashboard |
| **Review Cycle** | Monthly (data refresh), Quarterly (full review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification (12 sheets) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview
  - Prerequisites (Dependencies on A.5.7.1, A.5.7.2, A.5.7.3)
  - Data Refresh Workflow
  - Monthly Reporting Process
  - Quarterly Reporting Process
  - Evidence Package for Audits
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (12 sheets)
  - External References Configuration
  - Automated Data Aggregation Formulas
  - Executive Summary Layout
  - KPI Definitions
  - Trend Analysis Methodology

---

# PART I: USER COMPLETION GUIDE

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.5.7.4 - Threat Intelligence Effectiveness Dashboard

#### What This Dashboard Provides

This dashboard **CONSOLIDATES** data from all operational Control A.5.7 workbooks into a single executive view. It answers:

- How effective is our threat intelligence program overall?
- Are we meeting policy targets across all KPIs?
- What trends are emerging (month-over-month, quarter-over-quarter)?
- Where are the program gaps requiring attention?
- **CRITICAL**: What prevented incidents demonstrate program value? (from A.5.7.3)
- **CRITICAL**: What intelligence-driven decisions show executive engagement? (from A.5.7.3)
- What is our audit evidence status?

#### Key Principle

This is an **AUTOMATED AGGREGATION DASHBOARD**. It uses Excel external references to pull data from:

- ISMS-IMP-A.5.7.1 (Sources Assessment)
- ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment)

**Data flows automatically when source workbooks are updated and this dashboard is refreshed.**

#### What You'll Document

**Automated (External References):**

- Program KPIs from all three assessments
- Source portfolio metrics
- Intelligence operations metrics
- Integration status metrics
- Stakeholder engagement metrics
- **Prevention tracking** (from A.5.7.3 Sheet 7)
- **Risk assessment updates** (from A.5.7.3 Sheet 13)
- **Incident-TI integration** (from A.5.7.3 Sheet 14)
- **Intelligence-driven decisions** (from A.5.7.3 Sheet 15)

**Manual Entry:**

- Risk indicators (program health warnings)
- Executive comments/notes
- Action item priorities
- Approval signatures

#### Target Audience & Usage

| Audience | Primary Use Case | Frequency |
|----------|-----------------|-----------|
| **CISO** | Program oversight, KPI tracking | Weekly |
| **Security Managers** | Operational effectiveness, gap identification | Bi-weekly |
| **Executive Management** | Strategic value demonstration, investment justification | Monthly |
| **Board** | Risk posture, program maturity, prevented incidents | Quarterly |
| **Auditors** | Compliance evidence, effectiveness measurement | Annual + quarterly |

---

## Prerequisites

### Source Workbooks Required (DEPENDENCIES)

**This dashboard CANNOT function without:**

1. ✅ **ISMS-IMP-A.5.7.1** - Sources Assessment workbook (current version)
2. ✅ **ISMS-IMP-A.5.7.2** - Collection & Analysis Assessment workbook (current version)
3. ✅ **ISMS-IMP-A.5.7.3** - Integration & Distribution Assessment workbook (current version)

**File Location Requirements:**

- All three source workbooks must be in same directory as dashboard OR
- Update external reference paths to correct locations

**Version Requirements:**

- Source workbooks must be current (within 30 days for monthly reporting)
- Quarterly reviews require source workbooks updated within quarter

### Information You'll Need

- Access to all three source workbooks
- Understanding of external references in Excel (how to refresh)
- Executive feedback on program performance
- Risk assessment for program health indicators

### Required Tools

- Microsoft Excel (2016 or later) with external data connections enabled
- File system access to source workbooks
- Screen capture tools for executive summary export (PDF/PowerPoint)

---

## Workflow

### High-Level Process

```
MONTHLY CYCLE:
1. Update Source Workbooks (A.5.7.1, A.5.7.2, A.5.7.3)
2. Open Dashboard (A.5.7.4)
3. Refresh External Data Connections
4. Review Auto-Populated Metrics
5. Update Risk Indicators (manual)
6. Generate Monthly Report (Sheet 10)
7. CISO Review & Approval

QUARTERLY CYCLE:
1. Complete Monthly Cycle Steps
2. Review Trends (Sheet 7)
3. Review Compliance Evidence (Sheet 9)
4. Generate Quarterly Report (Sheet 11)
5. Prepare Board Package
6. Executive/Board Presentation
7. Executive Approval
```

### Monthly Reporting Process (2-3 hours)

**Step 1: Update Source Workbooks (Week 1 of month)**

- Complete monthly updates to A.5.7.1 (if source changes occurred)
- Complete monthly updates to A.5.7.2 (intelligence production, VTL records, campaigns)
- Complete monthly updates to A.5.7.3 (IOC deployment, distribution tracking)
- **CRITICAL**: Ensure A.5.7.3 Sheet 7 (Prevention) updated with any incidents prevented
- Save all source workbooks

**Step 2: Open Dashboard & Refresh Data (Week 1 of month)**
1. Open ISMS-IMP-A.5.7.4 dashboard workbook
2. Excel will prompt: "This workbook contains links to other data sources"
3. Click **"Update"** to refresh all external references
4. Verify no broken references (#REF! errors)
5. If broken references: Fix file paths in Formulas → Edit Links

**Step 3: Review Auto-Populated Metrics (Week 1 of month)**

- **Sheet 1: Executive_Summary** - Verify all metrics populated
- **Sheet 2: Program_KPIs** - Verify calculations correct
- **Sheet 3: Source_Portfolio** - Verify source counts accurate
- **Sheet 4: Intelligence_Operations** - Verify production metrics
- **Sheet 5: Integration_Status** - Verify tool integration data
- **Sheet 6: Stakeholder_Engagement** - Verify distribution metrics

**Step 4: Update Risk Indicators (Week 1 of month)**

- **Sheet 8: Risk_Indicators** - Manual entry required
  * Identify any program health warnings (KPIs below target, critical gaps, resource constraints)
  * Document risk indicator severity (Critical, High, Medium, Low)
  * Document mitigation actions
  * Update risk indicator status

**Step 5: Generate Monthly Report (Week 2 of month)**

- **Sheet 10: Monthly_Report** - Auto-generated from other sheets
  * Review report completeness
  * Add executive commentary (manual text box or comments)
  * Export to PDF for distribution
  * Distribute to CISO, Security Managers

**Step 6: CISO Review & Approval (Week 2 of month)**

- CISO reviews dashboard and monthly report
- CISO provides feedback or approval
- Document approval in metadata

**Deliverable:** Monthly dashboard with current data, monthly report distributed

---

### Quarterly Reporting Process (4-6 hours)

**Step 1-6: Complete Monthly Reporting Process**

**Step 7: Review Quarterly Trends (Week 1 of quarter-end month)**

- **Sheet 7: Trend_Analysis**
  * Review 3-month trends for all KPIs
  * Identify improving vs. declining metrics
  * Document trend analysis commentary
  * Highlight significant changes for executive attention

**Step 8: Review Compliance Evidence (Week 1 of quarter-end month)**

- **Sheet 9: Compliance_Evidence**
  * Verify all MANDATORY audit evidence present:
    - Prevention tracking (A.5.7.3 Sheet 7): ≥3 per quarter
    - Risk assessment updates (A.5.7.3 Sheet 13): ≥3 per quarter
    - Incident-TI integration (A.5.7.3 Sheet 14): ≥70% P1/P2
    - Intelligence-driven decisions (A.5.7.3 Sheet 15): ≥5 per quarter
  * Document compliance status (Met, Not Met, Partial)
  * Prepare evidence package for auditors

**Step 9: Generate Quarterly Report (Week 2 of quarter-end month)**

- **Sheet 11: Quarterly_Report**
  * Auto-generated summary of quarter
  * Quarter-over-quarter comparison
  * Key achievements highlighted
  * Gaps and action items documented
  * Export to PDF/PowerPoint for board

**Step 10: Prepare Board Package (Week 2-3 of quarter-end month)**

- Create board-ready presentation from quarterly report
- Include:
  * Executive summary (1 slide)
  * Prevented incidents (demonstrates value)
  * Intelligence-driven decisions (shows executive engagement)
  * Program maturity trends
  * Key risks and mitigations
  * Budget/resource requests (if applicable)

**Step 11: Executive/Board Presentation (Quarter-end)**

- Present quarterly results to executive team or board
- Gather feedback
- Document decisions or approvals
- Update dashboard with feedback

**Step 12: Executive Approval (Quarter-end)**

- Executive or board approves quarterly report
- Document approval in metadata
- Archive quarterly report and evidence package

**Deliverable:** Quarterly report approved, board presentation delivered, compliance evidence package ready for audit

---

## Evidence Package for Audits

### What Auditors Need from This Dashboard

**Audit Objective:** Verify threat intelligence program effectiveness and compliance with policy requirements

**Evidence Required:**

1. **Program KPIs (Sheet 2):**

   - Quarterly snapshots showing KPI tracking
   - Evidence of targets met or gaps addressed
   - Trend analysis showing continuous improvement

2. **Compliance Evidence (Sheet 9):**

   - **CRITICAL**: Prevention tracking summary (≥3 per quarter)
   - **CRITICAL**: Risk assessment updates summary (≥3 per quarter - ISO 27001 Clause 6.1)
   - **CRITICAL**: Incident-TI integration summary (≥70% P1/P2 - Controls A.5.24-5.28)
   - **CRITICAL**: Intelligence-driven decisions summary (≥5 per quarter)
   - Links to detailed evidence in source workbooks (A.5.7.1, A.5.7.2, A.5.7.3)

3. **Monthly Reports (Sheet 10):**

   - Monthly reports for entire audit period (typically 12 months)
   - CISO approval documented

4. **Quarterly Reports (Sheet 11):**

   - Quarterly reports for audit period
   - Executive/board approval documented

5. **Risk Indicators (Sheet 8):**

   - Program health tracking
   - Risk mitigation actions documented and completed

**How to Prepare for Audit:**

1. **3 Months Before Audit:**

   - Review all quarterly reports for completeness
   - Ensure all MANDATORY evidence present (Sheets 7, 13, 14, 15 from A.5.7.3)
   - Fill any evidence gaps

2. **1 Month Before Audit:**

   - Generate compliance evidence package (from Sheet 9)
   - Create audit evidence index (what's where)
   - Export key sheets to PDF for auditor review

3. **During Audit:**

   - Provide dashboard (Sheet 1: Executive_Summary) as program overview
   - Walk through Sheet 9 (Compliance_Evidence) showing MANDATORY requirements met
   - Drill into source workbooks for detailed evidence
   - Demonstrate data flow (external references showing real operational data)

**Audit Success Criteria:**

- ✓ All MANDATORY quarterly targets met (Sheets 7, 13, 14, 15 from A.5.7.3)
- ✓ Monthly and quarterly reporting consistent throughout audit period
- ✓ KPI targets from policy met or gaps documented with action items
- ✓ CISO/Executive approvals documented
- ✓ Traceability from policy requirements → dashboard → source workbooks

---

## Review & Approval

### Monthly Review

**Level 1: CISO**

- Reviews monthly dashboard and report
- Verifies KPIs against targets
- Approves monthly report for distribution
- Timeline: Within 5 business days of month-end

### Quarterly Review

**Level 1: CISO**

- Reviews quarterly dashboard and report
- Verifies compliance evidence complete
- Reviews trend analysis
- Prepares for executive/board presentation

**Level 2: Executive Management / Board**

- Reviews quarterly report and dashboard summary
- Reviews prevented incidents (demonstrates value)
- Reviews intelligence-driven decisions (shows engagement)
- Approves program continuation or directs changes
- Timeline: Within 15 business days of quarter-end

**Approval Documentation:**

- Monthly: CISO signature in Sheet 10 (Monthly_Report)
- Quarterly: Executive/Board signature in Sheet 11 (Quarterly_Report)

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_4_Effectiveness_Dashboard_YYYYMM.xlsx`

**Example:** `ISMS_A_5_7_4_Effectiveness_Dashboard_202601.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only designated cells editable)
- Macros: None (VBA-free for security)
- **External Links: YES** - References to A.5.7.1, A.5.7.2, A.5.7.3

**Total Sheets:** 12

**Tab Colors:**

- Executive Summary (Sheet 1): Blue (#4472C4)
- Aggregated Data (Sheets 2-6): Green (#70AD47)
- Analysis (Sheet 7): Purple (#7030A0)
- Management (Sheet 8): Orange (#FFA500)
- Audit (Sheet 9): Red (#C00000)
- Reports (Sheets 10-11): Teal (#00B0F0)
- Metadata: Gray (#D9D9D9)

**External References Configuration:**

```excel
// Example external reference formulas
// Assumes source workbooks in same directory

// From A.5.7.1 (Sources):
='[ISMS_A_5_7_1_Sources_Assessment_20260121.xlsx]Source_Inventory'!$B$2:$B$100

// From A.5.7.2 (Collection):
='[ISMS_A_5_7_2_Collection_Analysis_Assessment_20260121.xlsx]Quality_Metrics'!$B$5

// From A.5.7.3 (Integration):
='[ISMS_A_5_7_3_Integration_Distribution_Assessment_20260121.xlsx]Prevention_Tracking'!$A$2:$Z$100
```

**Data Refresh Strategy:**

- Manual refresh required when source workbooks updated
- Excel prompts on workbook open: "Update" = Refresh all external data
- Alternative: Data → Refresh All (forces refresh)
- Best practice: Close source workbooks before opening dashboard (faster refresh)

---

# Sheet Specifications

## Sheet 1: Executive_Summary

**Purpose**: Single-page executive dashboard (designed for printing/PDF export)

**Layout**: Fixed dashboard format with charts and key metrics

**Sections**:

### Header Section

- Organization name and logo placeholder
- Report title: "Threat Intelligence Program - Executive Summary"
- Reporting period: [Month YYYY]
- Generation date
- Classification: [Per org policy]

### Program Health Score (Top Center)

- **Overall Score**: 1-5 scale (calculated composite score)
- **Visual**: Large gauge chart
- **Color Coding**: 
  - 4.5-5.0: Dark Green (Excellent)
  - 3.5-4.4: Light Green (Good)
  - 2.5-3.4: Yellow (Fair)
  - 1.5-2.4: Orange (Poor)
  - 0.0-1.4: Red (Critical)

**Score Calculation**:

Weighted Average:

- Source Quality (20%)
- Intelligence Production (20%)
- Stakeholder Satisfaction (20%)
- Integration Effectiveness (20%)
- Operational Efficiency (20%)

### Key Metrics (4 Boxes - Top Row)

**Box 1: Intelligence Production**

- Products this month: [Number]
- vs. last month: [% change]
- vs. target: [% vs target]
- Mini trend chart (last 6 months)

**Box 2: Stakeholder Satisfaction**

- Average rating: [1-5]
- Response rate: [%]
- Consumption rate: [%]
- Mini trend chart

**Box 3: IOC Effectiveness**

- IOCs deployed: [Number]
- Hit rate: [%]
- False positive rate: [%]
- Mini trend chart

**Box 4: Source Portfolio**

- Active sources: [Number]
- Average quality: [1-5]
- Coverage gaps: [Number]
- Mini trend chart

### CVSS Metrics Summary

**CVSS Program Health Indicators**:

| Metric | Target | Actual | Status | Trend |
|--------|--------|--------|--------|-------|
| **CVSS 4.0 Adoption Rate** | ≥75% by Q4 2026 | =CALCULATED | =STATUS_FORMULA | [Chart Ref] |
| **Avg CVSS Score (Prevented CVEs)** | N/A (tracking only) | =CALCULATED | - | [Chart Ref] |
| **High CVSS + Active Exploitation (Open)** | 0 (all patched) | =CALCULATED | =EMERGENCY_STATUS | [Chart Ref] |
| **CVSS Accuracy Rate (All Sources)** | ≥90% | =CALCULATED | =STATUS_FORMULA | [Chart Ref] |

**Formula Specifications**:

```excel
CVSS_4_Adoption_Rate = 
  COUNTIFS([A.5.7.2]Sheet_8.CVSS_Version,"4.0") / 
  COUNTA([A.5.7.2]Sheet_8.CVSS_Version) * 100

Avg_CVSS_Prevented = 
  AVERAGE([A.5.7.3]Sheet_7.CVSS_Base_Score)

High_CVSS_Active_Exploitation_Open = 
  COUNTIFS([A.5.7.2]Sheet_8.CVSS_Base_Score,">=7.0",
           [A.5.7.2]Sheet_8.Exploitation_Status,{"Active Exploitation","Mass Exploitation"},
           [A.5.7.2]Sheet_8.Remediation_Status,"Open")

CVSS_Accuracy_Overall = 
  AVERAGE([A.5.7.1]Sheet_14.CVSS_Accuracy_Rate)

STATUS_FORMULA = 
  IF(Actual >= Target, "✅ Met", "❌ Missed")

EMERGENCY_STATUS = 
  IF(High_CVSS_Active_Exploitation_Open = 0, 
     "✅ Compliant", 
     "❌ EMERGENCY ACTION REQUIRED")
```

**Conditional Formatting**:

- High_CVSS_Active_Exploitation_Open > 0 → RED BACKGROUND, WHITE BOLD TEXT
- CVSS_4_Adoption_Rate < 50% → YELLOW BACKGROUND
- CVSS_Accuracy_Overall < 85% → ORANGE BACKGROUND

**Chart: CVSS Severity Distribution (Prevented Incidents)**

- **Type**: Pie chart or horizontal bar chart
- **Title**: "Prevented Incidents by CVSS Severity"
- **Data Source**: IMP-A.5.7.3 Sheet 7 (Prevention_Tracking)
- **Categories**:
  - Critical (9.0-10.0): Red (#DC3545)
  - High (7.0-8.9): Orange (#FD7E14)
  - Medium (4.0-6.9): Yellow (#FFC107)
  - Low (0.1-3.9): Green (#28A745)

### Integration Status (Middle Left)

- **Pie Chart**: Security tools with TI integration
  - Fully Integrated: [%]
  - Partially Integrated: [%]
  - Planned: [%]
  - Not Integrated: [%]

### Control 8.8 Linkage (Middle Center)

- **Bar Chart**: Vulnerability-threat links by urgency
  - Critical: [Count]
  - High: [Count]
  - Medium: [Count]
  - Low: [Count]

### Top Threats This Month (Middle Right)

- **Table**: Top 5 threats by impact
  - Threat name
  - Category
  - Priority
  - Status

### Coverage Heat Map (Bottom Left)

- **Matrix**: Geographic + Sector coverage
- Color-coded: Green (adequate), Yellow (minimal), Red (gap)

### Action Items Summary (Bottom Center)

- Open critical actions: [Number]
- Overdue actions: [Number]
- Completed this month: [Number]
- **Mini Chart**: Actions by priority

### Compliance Status (Bottom Right)

- ISO 27001:2022 Control 5.7 compliance: [%]
- Outstanding evidence items: [Number]
- Last audit date: [Date]
- Next audit: [Date]

---

## Sheet 2: Program_KPIs

**Purpose**: Detailed KPI tracking with targets and thresholds

**Column Specifications**:

| Column | Data Type | Formula/Source | Required | Example |
|--------|-----------|----------------|----------|---------|
| KPI_ID | Text | Manual entry | Yes | KPI-TI-001 |
| KPI_Category | Dropdown | Source_Management, Collection, Analysis, Production, Integration, Dissemination | Yes | Production |
| KPI_Name | Text | Free text | Yes | Intelligence Products per Month |
| Description | Text | Free text | Yes | Count of formal intelligence products published |
| Unit | Text | Free text | Yes | Reports |
| Measurement_Frequency | Dropdown | Daily, Weekly, Monthly, Quarterly | Yes | Monthly |
| Data_Source | Text | Excel reference | Yes | =[5.7.2]Intelligence_Production!A:A |
| Target_Value | Number | Manual entry | Yes | 20 |
| Warning_Threshold | Number | Manual entry | Yes | 16 (80% of target) |
| Critical_Threshold | Number | Manual entry | Yes | 12 (60% of target) |
| Current_Value | Number | Formula from data_source | Auto | 23 |
| Last_Month_Value | Number | Historical lookup | Auto | 21 |
| Month_over_Month_Change | Formula | (Current - Last) / Last * 100 | Auto | +9.5% |
| Performance_vs_Target | Formula | (Current / Target - 1) * 100 | Auto | +15% |
| Status | Formula | IF Current >= Target: "On Track", >= Warning: "Caution", else: "At Risk" | Auto | On Track |
| Trend | Formula | Based on last 3 months | Auto | Improving |
| Owner | Text | Email or role | Yes | TI Team Lead |
| Last_Updated | Date | Auto TODAY() | Auto | 2025-01-02 |
| Notes | Text | Free text | No | Exceeded target due to increased APT activity |

**Standard KPIs List**:

**Source Management (5.7.1)**:
1. Number of active sources
2. Average source quality score
3. Source coverage gaps
4. Annual cost per source
5. ROI rating distribution

**Collection & Analysis (5.7.2)**:
6. Intelligence products produced per month
7. Average time to produce intelligence (hours)
8. Stakeholder feedback rating (1-5)
9. Intelligence consumption rate (%)
10. MITRE ATT&CK technique coverage (%)
11. Analyst training completion rate (%)
12. Vulnerability-threat links created

**Integration & Distribution (5.7.3)**:
13. Security tools with TI integration (%)
14. IOCs deployed per month
15. IOC hit rate (%)
16. IOC false positive rate (%)
17. Average time from IOC publication to deployment (hours)
18. Stakeholder engagement score (1-5)
19. Intelligence distribution reach (% of target audience)
20. Mean time from intelligence to action (hours)

**CVSS Framework Health (Cross-Control)**:
21. CVSS 4.0 Adoption Rate (%) - Target: ≥75% by Q4 2026
22. CVSS Accuracy Rate (All Sources, %) - Target: ≥90%
23. High CVSS + Active Exploitation (Open Count) - Target: 0
24. Average CVSS Score (Prevented Incidents) - Tracking only
25. Risk Updates with CVSS Quantification (%) - Target: 100% for vuln risks

**Conditional Formatting**:

- Status "On Track" → Green
- Status "Caution" → Yellow
- Status "At Risk" → Red
- Trend "Declining" → Orange text

**KPI Dashboard** (charts):

- Current vs. target sparklines
- Trend charts (last 12 months)
- Performance distribution (pie chart by status)

---

## Sheet 3: Source_Portfolio

**Purpose**: Aggregated source performance from 5.7.1

**Data Sources**:

- External reference: `=[5.7.1]Source_Inventory!$A:$O`
- External reference: `=[5.7.1]Source_Evaluation!$A:$T`
- External reference: `=[5.7.1]Cost_Analysis!$A:$S`

**Summary Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| Total Active Sources | COUNTIF(Status="Active") | 15-25 | [Auto] |
| Commercial Sources | COUNTIF(Type="Commercial") | 5-10 | [Auto] |
| OSINT Sources | COUNTIF(Type="OSINT") | 5-15 | [Auto] |
| Government Sources | COUNTIF(Type="Government") | 2-5 | [Auto] |
| Average Quality Score | AVERAGE(Overall_Quality_Score) | >= 4.0 | [Auto] |
| Sources Rated "Excellent" | COUNTIF(Quality="Excellent") | >= 50% | [Auto] |
| Total Annual Cost | SUM(Annual_Cost) | Per budget | [Auto] |
| Cost per Active Source | Total_Cost / Active_Sources | Optimize | [Auto] |
| Coverage Gaps | COUNT(Coverage_Status="Gap") | 0 | [Auto] |
| Compliance Issues | COUNT(Compliance_Status="Non-Compliant") | 0 | [Auto] |
| Contracts Expiring <90 Days | COUNTIF(Contract_End < TODAY()+90) | Monitor | [Auto] |
| **Overall CVSS Accuracy** | **AVERAGE(CVSS_Accuracy_Rate)** | **≥90%** | **[Auto]** |
| **Sources with ≥90% CVSS Accuracy** | **COUNTIF(CVSS_Accuracy_Rate≥90%)** | **Majority** | **[Auto]** |
| **Sources with <85% CVSS Accuracy** | **COUNTIF(CVSS_Accuracy_Rate<85%)** | **0** | **[Auto]** |

**Charts**:
1. **Source Distribution** (Pie): By Source_Type
2. **Quality Distribution** (Bar): Count by Quality_Rating
3. **Cost Distribution** (Pie): Annual cost by Source_Type
4. **Coverage Heat Map**: Imported from 5.7.1
5. **Source Reliability** (Bar): Count by Admiralty Code rating

**Top/Bottom Lists**:

- Top 5 sources by quality score
- Top 5 sources by cost
- Sources requiring action (gaps, compliance, renewals)

---

## Sheet 4: Intelligence_Operations

**Purpose**: Collection and analysis effectiveness from 5.7.2

**Data Sources**:

- External reference: `=[5.7.2]Intelligence_Production!$A:$W`
- External reference: `=[5.7.2]Quality_Metrics!$A:$N`
- External reference: `=[5.7.2]Analyst_Capabilities!$A:$U`

**Summary Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| Products This Month | COUNT(Publication_Date in current month) | 20 | [Auto] |
| Products by Type | COUNT by Product_Type | Balanced | [Auto] |
| Average Time to Produce | AVERAGE(Time_To_Produce_Hours) | <= 8 hrs | [Auto] |
| Average Feedback Rating | AVERAGE(Feedback_Rating) | >= 4.0 | [Auto] |
| Consumption Rate | % with Intelligence_Consumed="Yes" | >= 75% | [Auto] |
| Mean Time to Action | AVERAGE(Time_To_Action_Hours) | <= 24 hrs | [Auto] |
| MITRE Coverage | % techniques with >= Partial coverage | >= 80% | [Auto] |
| Vulnerability-Threat Links | COUNT from Vulnerability_Linked_Threats | Monitor | [Auto] |
| Critical VT Links | COUNT where Priority >= 8 | Monitor | [Auto] |
| Team Size | COUNT(Analyst_Capabilities) | Monitor | [Auto] |
| Average Team Experience | AVERAGE(Years_Experience_TI) | >= 3 years | [Auto] |
| Training Completion Rate | % with required training complete | 100% | [Auto] |
| **VTL Records Created** | **COUNT(VTL_ID)** | **≥50/quarter** | **[Auto]** |
| **VTL with CVSS 4.0** | **COUNTIF(CVSS_Version="4.0")** | **≥75% of VTL** | **[Auto]** |
| **VTL with CVSS 3.1** | **COUNTIF(CVSS_Version="3.1")** | **≤25% of VTL** | **[Auto]** |
| **VTL Missing CVSS** | **COUNTBLANK(CVSS_Version)** | **0** | **[Auto]** |
| **Avg CVSS Score (VTL)** | **AVERAGE(CVSS_Base_Score)** | **N/A (tracking)** | **[Auto]** |
| **CVSS 4.0 Adoption Rate** | **(VTL_4.0/VTL_Total)*100** | **≥75% by Q4 2026** | **[Auto]** |

**Charts**:
1. **Production Volume** (Line): Products per month (last 12 months)
2. **Product Type Mix** (Pie): Distribution by Product_Type
3. **Quality Trends** (Line): Average feedback rating over time
4. **Intelligence Lifecycle** (Funnel):

   - Products published
   - Products distributed
   - Products consumed
   - Actions taken

5. **Analyst Skills Heat Map**: Skills matrix from 5.7.2

**VT Link Analysis Section**:

- **Table**: Top 10 critical vulnerability-threat links
  - Vulnerability_ID
  - Threat_Actor
  - Exploitation_Status
  - Priority_Score
  - Remediation_Status
- **Chart**: VT links by Remediation_Urgency
- **Metric**: % Critical VT links remediated within SLA

---

## Sheet 5: Integration_Status

**Purpose**: Security tool integration and IOC effectiveness from 5.7.3

**Data Sources**:

- External reference: `=[5.7.3]Tool_Integration_Matrix!$A:$T`
- External reference: `=[5.7.3]IOC_Deployment!$A:$X`

**Summary Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| Tools with TI Integration | COUNT where Integration_Status != "Not_Integrated" | All critical tools | [Auto] |
| Fully Integrated Tools | COUNT(Status="Fully_Integrated") | >= 80% | [Auto] |
| Integration Coverage by Category | % by Tool_Category | Balanced | [Auto] |
| Automated Integrations | COUNT(Automation_Level="Fully_Automated") | >= 70% | [Auto] |
| Integration Errors Last 30 Days | SUM(Sync_Errors_Last_30_Days) | < 5 | [Auto] |
| IOCs Deployed This Month | COUNT(Deployment_Date in month) | Monitor | [Auto] |
| Active IOCs | COUNT(Status="Active") | Monitor | [Auto] |
| IOCs with Hits Last 30 Days | COUNT(Hits_Last_30_Days > 0) | Monitor | [Auto] |
| Overall IOC Hit Rate | (IOCs with hits / Total IOCs) * 100 | >= 5% | [Auto] |
| False Positive Rate | (FP IOCs / IOCs with hits) * 100 | <= 10% | [Auto] |
| Average IOC Lifespan | AVERAGE(Days_Active) | 90 days | [Auto] |
| Blocked Threats | SUM where Action="Block" and Hits>0 | Monitor | [Auto] |

**Charts**:
1. **Integration Status** (Pie): Distribution by Integration_Status
2. **Tool Category Coverage** (Bar): Integration by Tool_Category
3. **IOC Deployment Trend** (Line): IOCs deployed per month
4. **IOC Hit Rate** (Line): Hit rate over time
5. **IOC Effectiveness** (Funnel):

   - IOCs deployed
   - IOCs with hits
   - IOCs with blocks
   - Incidents prevented

**Integration Maturity Assessment**:

- **Scorecard**: Maturity level by tool category
- **Gap Analysis**: Tools requiring integration
- **Automation Progress**: Trend toward full automation

---

## Sheet 6: Stakeholder_Engagement

**Purpose**: Dissemination effectiveness and stakeholder satisfaction from 5.7.3

**Data Sources**:

- External reference: `=[5.7.3]Stakeholder_Registry!$A:$T`
- External reference: `=[5.7.3]Distribution_Tracking!$A:$T`
- External reference: `=[5.7.3]Feedback_Collection!$A:$V`

**Summary Metrics**:

| Metric | Calculation | Target | Current |
|--------|-------------|--------|---------|
| Total Active Stakeholders | COUNT(Status="Active") | Growth | [Auto] |
| Stakeholder Distribution | COUNT by Department | Balanced | [Auto] |
| Distributions This Month | COUNT(Distribution_Date in month) | Per cadence | [Auto] |
| Total Recipients Reached | SUM(Recipient_Count) | Maximize | [Auto] |
| Average Open Rate | AVERAGE(Open_Rate) | >= 70% | [Auto] |
| Average Click Rate | AVERAGE(Click_Rate) | >= 40% | [Auto] |
| Feedback Response Rate | AVERAGE(Feedback_Rate) | >= 10% | [Auto] |
| Average Stakeholder Rating | AVERAGE(Overall_Rating) | >= 4.0 | [Auto] |
| Intelligence Consumption Rate | % with Intelligence_Used="Yes" | >= 75% | [Auto] |
| Action Taken Rate | AVERAGE(Action_Rate) | >= 25% | [Auto] |
| Highly Engaged Stakeholders | COUNT(Engagement_Score >= 4) | Maximize | [Auto] |
| Distribution Effectiveness | % distributions rated "High" | >= 60% | [Auto] |

**Charts**:
1. **Stakeholder Growth** (Line): Active stakeholders over time
2. **Engagement Distribution** (Bar): Count by Engagement_Score
3. **Channel Performance** (Bar): Engagement metrics by channel
4. **Audience Reach** (Pie): Distribution by department/role
5. **Feedback Trends** (Line): Average ratings over time
6. **Action Impact** (Funnel):

   - Intelligence distributed
   - Intelligence opened
   - Feedback provided
   - Actions taken

**Top Stakeholders Table**:

- Top 10 most engaged stakeholders
- Top 5 departments by engagement
- Stakeholders requiring re-engagement

---

## Sheet 7: Trend_Analysis

**Purpose**: Historical trends and forecasting

**Data Collection**:

- Monthly snapshots of key metrics
- Rolling 12-month history
- Seasonal pattern analysis

**Trend Metrics**:

| Metric | 3-Month Trend | 6-Month Trend | 12-Month Trend | Forecast Next Quarter |
|--------|---------------|---------------|----------------|----------------------|
| Intelligence Production | [% change] | [% change] | [% change] | [Predicted value] |
| Stakeholder Satisfaction | [% change] | [% change] | [% change] | [Predicted value] |
| IOC Hit Rate | [% change] | [% change] | [% change] | [Predicted value] |
| Source Quality | [% change] | [% change] | [% change] | [Predicted value] |
| Integration Coverage | [% change] | [% change] | [% change] | [Predicted value] |
| Overall Program Health | [% change] | [% change] | [% change] | [Predicted value] |

**Visualizations**:
1. **Multi-line Trend Chart**: All key metrics on single timeline
2. **Seasonal Decomposition**: Identify patterns in intelligence production
3. **Forecast Charts**: Predicted values with confidence intervals
4. **Correlation Analysis**: Relationships between metrics
5. **Anomaly Detection**: Significant deviations from trends

**Statistical Analysis**:

- Moving averages (3-month, 6-month)
- Standard deviations
- Correlation coefficients
- Regression analysis for forecasting

**CVSS Framework Trends**:

**Chart: CVSS 4.0 Adoption Over Time**

- **Type**: Line chart with target trajectory
- **Title**: "CVSS 4.0 Adoption Progress (Target: 75% by Q4 2026)"
- **Data Series**:

  1. Actual Adoption (solid blue line) - Historical CVSS 4.0 adoption rate per quarter
  2. Target Trajectory (dashed red line) - Linear progression to 75% by Q4 2026
  3. Industry Average (dotted gray line) - Optional benchmark if available

- **Conditional Formatting**:
  - Actual below Target → RED marker
  - Actual meets/exceeds Target → GREEN marker

**Chart: CVSS Severity Distribution Over Time**

- **Type**: Stacked bar chart
- **Title**: "Prevented Incidents by CVSS Severity (Quarterly)"
- **Stacked Categories**:
  - Critical (9.0-10.0) - Red
  - High (7.0-8.9) - Orange
  - Medium (4.0-6.9) - Yellow
  - Low (0.1-3.9) - Green
- **Purpose**: Shows both prevention volume AND severity distribution trends

---

## Sheet 8: Risk_Indicators

**Purpose**: Early warning system for program degradation

**Risk Categories**:

**1. Source Portfolio Risks**:

- Coverage gaps in critical areas
- Single-source dependencies
- Contracts expiring without renewal plan
- Quality degradation trends
- Cost overruns

**2. Operational Risks**:

- Production volume decline
- Increasing time-to-produce
- Analyst skill gaps
- Training backlog
- Burnout indicators

**3. Integration Risks**:

- Integration failures
- Rising false positive rates
- IOC deployment delays
- Tool coverage gaps
- Automation failures

**4. Stakeholder Risks**:

- Declining engagement
- Negative feedback trends
- Consumption rate decrease
- Distribution failures
- Stakeholder attrition

**5. Compliance Risks**:

- Missing evidence
- Policy violations
- Audit findings
- SLA breaches
- Data protection issues

**Risk Indicator Table**:

| Risk_ID | Risk_Category | Indicator | Threshold | Current_Value | Status | Trend | Owner | Mitigation_Plan |
|---------|---------------|-----------|-----------|---------------|--------|-------|-------|----------------|
| [Auto] | [Dropdown] | [Text] | [Number] | [Formula] | [Formula] | [Formula] | [Text] | [Text] |

**Risk Status Calculation**:

IF Current_Value > Critical_Threshold: "Critical"
ELSE IF Current_Value > Warning_Threshold: "Warning"
ELSE: "Normal"

**Risk Dashboard**:

- **Heat Map**: Risks by category and severity
- **Trend Indicators**: Risk levels over time
- **Top Risks Table**: Highest priority items
- **Mitigation Tracker**: Action plan status

**CVSS-Based Risk Quantification Tracking**:

**Table: Risk Assessment CVSS Integration**

| Quarter | Total Risk Updates | Vulnerability-Related | Risks with CVSS | CVSS Quantification Rate | Avg CVSS (Risks) | Status |
|---------|-------------------|----------------------|-----------------|--------------------------|------------------|--------|
| 2025-Q1 | =COUNT | =COUNT_VULN | =COUNT_CVSS | =PERCENTAGE | =AVERAGE | =STATUS |
| 2024-Q4 | =COUNT | =COUNT_VULN | =COUNT_CVSS | =PERCENTAGE | =AVERAGE | =STATUS |
| 2024-Q3 | =COUNT | =COUNT_VULN | =COUNT_CVSS | =PERCENTAGE | =AVERAGE | =STATUS |

**Formulas**:
```excel
CVSS_Quantification_Rate = 
  IF(Vulnerability_Related=0, "N/A", (Risks_With_CVSS / Vulnerability_Related) * 100)

STATUS = 
  IF(CVSS_Quantification_Rate >= 100, "✅ Compliant",
     IF(CVSS_Quantification_Rate >= 90, "âš  Needs Attention",
        "❌ Non-Compliant"))
```

**Target**: 100% of vulnerability-related risks have CVSS quantification

**Risk Indicator**: Missing CVSS in Vulnerability Risks

- **Alert Threshold**: Any vulnerability-related risk without CVSS score
- **Alert Message**: "CRITICAL: {count} vulnerability risks lack CVSS quantification. This blocks accurate risk rating per ISO 27001 Clause 6.1."

---

## Sheet 9: Compliance_Evidence

**Purpose**: Audit artifact generation for ISO 27001:2022 Control 5.7

**Evidence Inventory**:

| Evidence_ID | Control_Requirement | Evidence_Type | Location | Last_Updated | Status | Notes |
|-------------|---------------------|---------------|----------|--------------|--------|-------|
| EV-5.7-001 | Source inventory maintained | Excel Workbook | 5.7.1 Sheet 2 | [Auto] | [Auto] | Active sources documented |
| EV-5.7-002 | Source quality assessed | Excel Workbook | 5.7.1 Sheet 3 | [Auto] | [Auto] | Admiralty Code applied |
| EV-5.7-003 | Coverage gaps identified | Excel Workbook | 5.7.1 Sheet 4 | [Auto] | [Auto] | Heat map analysis |
| EV-5.7-004 | Intelligence production tracked | Excel Workbook | 5.7.2 Sheet 5 | [Auto] | [Auto] | Monthly output logged |
| EV-5.7-005 | MITRE mapping maintained | Excel Workbook | 5.7.2 Sheet 6 | [Auto] | [Auto] | Technique coverage |
| EV-5.7-006 | Vulnerability linkage | Excel Workbook | 5.7.2 Sheet 8 | [Auto] | [Auto] | VTL schema implemented |
| EV-5.7-007 | Tool integration documented | Excel Workbook | 5.7.3 Sheet 2 | [Auto] | [Auto] | Security stack mapped |
| EV-5.7-008 | IOC deployment tracked | Excel Workbook | 5.7.3 Sheet 3 | [Auto] | [Auto] | Lifecycle managed |
| EV-5.7-009 | Stakeholder engagement | Excel Workbook | 5.7.3 Sheet 7 | [Auto] | [Auto] | Feedback collected |
| EV-5.7-010 | Program KPIs measured | Excel Workbook | 5.7.4 Sheet 2 | [Auto] | [Auto] | Performance tracked |

**Compliance Status**:

- % of evidence items current (< 90 days old)
- Outstanding evidence gaps
- Evidence quality assessment
- Audit readiness score

**Audit Preparation**:

- Pre-populated audit responses
- Evidence cross-reference matrix
- Control effectiveness statement
- Continuous improvement log

**CVSS Framework Compliance Evidence**:

| Compliance Item | Evidence Location | Status | Notes |
|-----------------|-------------------|--------|-------|
| CVSS 4.0 Adoption Progress | Sheet 2 KPI-CVSS-001, Sheet 7 Trend Chart | =STATUS | Target: 75% by Q4 2026 |
| CVSS Accuracy (Sources) | Sheet 3 CVSS_Accuracy_Rate, Sheet 2 KPI-CVSS-002 | =STATUS | Target: ≥90% |
| CVSS in Risk Quantification | Sheet 8 CVSS Quantification Rate | =STATUS | Clause 6.1 requirement |
| CVSS in Incident Response | See Incident Context section below | =STATUS | Controls A.5.24-5.28 |
| Emergency Response (High CVSS) | Sheet 2 KPI-CVSS-003 | =EMERGENCY | Must be 0 |

**CVSS Context in Incident Response**:

| Metric | This Quarter | Last Quarter | Change | Target |
|--------|--------------|--------------|--------|--------|
| **Total Incidents (P1/P2)** | =COUNT | =COUNT_PREV | =CHANGE | N/A |
| **Vulnerability-Related Incidents** | =COUNT_VULN | =COUNT_VULN_PREV | =CHANGE | N/A |
| **Vuln Incidents with CVSS Context** | =COUNT_CVSS | =COUNT_CVSS_PREV | =CHANGE | 100% |
| **CVSS Context Rate** | =PERCENTAGE | =PERCENTAGE_PREV | =CHANGE | 100% |
| **Avg CVSS Score (Vuln Incidents)** | =AVERAGE | =AVERAGE_PREV | =CHANGE | N/A |

**Formulas**:
```excel
CVSS_Context_Rate = 
  IF(Vuln_Related_Incidents=0, "N/A", 
     (Incidents_With_CVSS / Vuln_Related_Incidents) * 100)
```

---

## Sheet 10: Monthly_Report

**Purpose**: Auto-generated monthly report for distribution

**Report Sections**:

1. **Executive Summary** (from Sheet 1)
2. **Program Health Score** (composite)
3. **Key Achievements This Month**:

   - High-impact intelligence products
   - Major integrations completed
   - Critical threats detected

4. **Performance vs. Targets**:

   - KPIs on track / at risk
   - Top performers
   - Areas needing attention

5. **Source Portfolio Update**:

   - New sources added
   - Sources retired
   - Quality improvements

6. **Operational Highlights**:

   - Production volume
   - Stakeholder feedback summary
   - IOC effectiveness

7. **Integration Progress**:

   - Tools integrated this month
   - Automation improvements
   - Hit rate performance

8. **Upcoming Activities**:

   - Planned improvements
   - Contract renewals
   - Training events

9. **Action Items**:

   - Critical actions
   - Overdue items
   - Completed this month

10. **CVSS-Based Prevention Value**:

   - Prevented incidents by CVSS severity
   - Total cost avoidance this month
   - Average CVSS score of prevented threats
   - ROI multiplier (TI cost vs. cost avoidance)

**Format**: Print-ready, PDF-exportable

**CVSS-Based Cost Avoidance Table**:

| CVSS Severity Range | Prevented Count | Avg Cost Avoidance/Incident | Total Cost Avoidance | % of Total |
|---------------------|-----------------|----------------------------|----------------------|------------|
| Critical (9.0-10.0) | =COUNT_CRIT | 150,000 CHF | =TOTAL_CRIT | =PERCENT |
| High (7.0-8.9) | =COUNT_HIGH | 75,000 CHF | =TOTAL_HIGH | =PERCENT |
| Medium (4.0-6.9) | =COUNT_MED | 25,000 CHF | =TOTAL_MED | =PERCENT |
| Low (0.1-3.9) | =COUNT_LOW | 5,000 CHF | =TOTAL_LOW | =PERCENT |
| **TOTAL** | =SUM | =WEIGHTED_AVG | =GRAND_TOTAL | **100%** |

**Note**: Cost estimates use industry averages where actual data unavailable.

---

## Sheet 11: Quarterly_Report

**Purpose**: Comprehensive quarterly review for executive leadership

**Report Sections**:

1. **Quarterly Executive Summary**
2. **Strategic Threat Landscape** (key trends observed)
3. **Program Maturity Assessment** (from 5.7.2 Sheet 9)
4. **Quarterly KPI Performance**
5. **Source Portfolio ROI Analysis** (including CVSS-based prevention value)
6. **CVSS Framework Adoption Progress** (4.0 adoption rate, accuracy metrics)
7. **Control 8.8 Integration Review** (VT links, remediation, CVSS quantification)
8. **Stakeholder Engagement Trends**
9. **Compliance Status** (ISO 27001, GDPR, CVSS in risk assessments)
10. **Budget vs. Actual**
11. **Next Quarter Priorities**

**Format**: Presentation-ready, executive briefing style

---

## Sheet 12: Metadata

[Standard metadata sheet with dashboard generation details]

---

# Data Refresh Strategy

## Automated Refresh

**Excel External References**:

- Auto-update on workbook open: **Yes**
- Refresh frequency: **On-demand** (manual refresh button)
- Background refresh: **Enabled** for large datasets

**Refresh Workflow**:
1. Open dashboard workbook
2. Excel prompts to update external links
3. Click "Update" to pull latest data
4. Charts and metrics automatically recalculate
5. Review for anomalies

## Manual Data Entry

**Minimal manual entry required**:

- Target values in Program_KPIs
- Risk thresholds in Risk_Indicators
- Commentary in Monthly/Quarterly reports

## Data Validation

**Automated checks**:

- External reference integrity
- Broken link detection
- Data type validation
- Calculation error detection

---

# Integration Points

## Source Workbooks (Read-Only External References)

- **5.7.1 (Sources)**: Source_Inventory, Source_Evaluation, Cost_Analysis, Compliance_Check
- **5.7.2 (Collection & Analysis)**: Intelligence_Production, Quality_Metrics, Vulnerability_Linked_Threats, Analyst_Capabilities
- **5.7.3 (Integration & Distribution)**: Tool_Integration_Matrix, IOC_Deployment, Distribution_Tracking, Feedback_Collection

## Dashboard to Control 8.8

- VT link summary → 8.8 dashboard for joint reporting
- Integration status → 8.8 detection capability assessment

---

# Evidence Requirements

**This dashboard itself serves as evidence** for:

- ISO 27001:2022 Control 5.7 implementation
- Program governance and oversight
- Continuous monitoring and improvement
- Management review inputs

**Supporting Evidence**:

- Monthly reports (12 per year)
- Quarterly reports (4 per year)
- Executive briefing presentations
- Audit responses

---

# Completion Instructions

## Initial Setup

1. Ensure all source workbooks (5.7.1, 5.7.2, 5.7.3) exist
2. Run dashboard generator script
3. Update external reference paths to source workbooks
4. Set target values in Program_KPIs
5. Configure risk thresholds in Risk_Indicators
6. Test data refresh
7. Validate calculations
8. Generate initial Monthly_Report

**Estimated Time**: 4-6 hours

## Monthly Refresh

1. Open dashboard workbook
2. Refresh external references
3. Review Executive_Summary for anomalies
4. Update Program_KPIs targets if needed
5. Review Risk_Indicators for alerts
6. Generate Monthly_Report
7. Distribute to stakeholders
8. File for audit evidence

**Estimated Time**: 1-2 hours

## Quarterly Review

1. Perform monthly refresh steps
2. Conduct deep-dive Trend_Analysis
3. Update Program Maturity assessment
4. Generate Quarterly_Report
5. Prepare executive briefing
6. Present to leadership
7. Capture feedback and action items

**Estimated Time**: 4-6 hours

---

# Validation Rules

- All external references must resolve (no #REF! errors)
- KPI current values must update with source data refresh
- Charts must auto-update when data changes
- Executive_Summary calculations must match detail sheets
- Risk status must auto-calculate based on thresholds
- Report generation must complete without errors

---

# Related Documents

**Policy Framework**:

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - KPIs and audit evidence
- **ISMS-POL-A.5.7, Section 3.2** (Exception Management)
- **ISMS-POL-A.5.7, Section 3.4** (Policy Governance)

**Implementation Specifications**:

- ISMS-IMP-A.5.7.1 (Sources Assessment)
- ISMS-IMP-A.5.7.2 (Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.3 (Integration & Distribution Assessment)

**Standards References**:

- ISO/IEC 27001:2022 Annex A Control 5.7

---

# Related Documents

**Policy Framework:**

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - KPIs and audit evidence
- **ISMS-POL-A.5.7, Section 3.2** (Exception Management)
- **ISMS-POL-A.5.7, Section 3.4** (Policy Governance)

**Implementation Specifications (DATA SOURCES):**

- **ISMS-IMP-A.5.7.1** (Sources Assessment) - External reference for source metrics
- **ISMS-IMP-A.5.7.2** (Collection & Analysis Assessment) - External reference for production metrics
- **ISMS-IMP-A.5.7.3** (Integration & Distribution Assessment) - External reference for integration & MANDATORY audit evidence

**Standalone Alternative:**

- **ISMS-IMP-A.5.7.5** (Standalone Dashboard) - Manual-entry executive dashboard (no external references)

**Standards References:**

- ISO/IEC 27001:2022 Annex A Control A.5.7
- ISO/IEC 27002:2022 Control 5.7 Implementation Guidance

---

**END OF SPECIFICATION**

---

*"Every great and deep difficulty bears in itself its own solution."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-01-31 -->
