**ISMS-IMP-A.5.7.5 - Threat Intelligence Standalone Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.5 |
| **Version** | 1.0 |
| **Assessment Area** | Standalone Executive Dashboard (Manual Entry, No Dependencies) |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements), Section 3.4 (Policy Governance) |
| **Purpose** | Provide standalone, self-contained executive dashboard for TI program visibility without dependencies on detailed assessment workbooks |
| **Target Audience** | C-Suite Executives, Board Members, External Stakeholders, CISO, Auditors |
| **Assessment Type** | Executive Summary Dashboard |
| **Review Cycle** | Monthly (data entry), Quarterly (executive review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial specification (9 sheets) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Dashboard Overview (Key Differences vs. A.5.7.4)
  - 10-Minute Monthly Update Process
  - Quarterly Summary Workflow
  - Board Presentation Guidelines
  - Evidence Collection (Lightweight)
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (9 sheets)
  - Monthly Data Entry Sheet
  - Auto-Generated Executive Dashboard
  - 12-Month Trend Visualization
  - Quarterly Summary Generation
  - Critical Actions Tracking
  - Risk Summary Format
  - ROI Calculation Methodology


---

# PART I: USER COMPLETION GUIDE

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.5.7.5 - Threat Intelligence Standalone Dashboard

#### What This Dashboard Provides

This is a **STANDALONE, SELF-CONTAINED** executive dashboard for threat intelligence program visibility. It is designed for:

- **Board presentations**: Quarterly TI program updates to board of directors
- **Executive briefings**: Monthly leadership summaries without technical detail
- **External reporting**: Shareable without exposing operational details (no references to internal workbooks)
- **Rapid assessment**: 10-minute monthly updates via manual data entry (no complex workbook dependencies)


#### Key Differences vs. ISMS-IMP-A.5.7.4

| Aspect | A.5.7.4 Comprehensive Dashboard | A.5.7.5 Standalone Dashboard |
|--------|--------------------------------|------------------------------|
| **Data Source** | External references (A.5.7.1/2/3) | **Manual entry** |
| **Update Method** | Automatic (refresh links) | **Manual (10 min/month)** |
| **Sheets** | 12 sheets (detailed) | **9 sheets (executive)** |
| **Audience** | CISO, Security Managers, Auditors | **C-suite, Board, External** |
| **Dependencies** | Requires A.5.7.1/2/3 | **None - standalone** |
| **Use Case** | Internal operations & audits | **Executive briefings & reports** |
| **Detail Level** | Operational | **Strategic** |
| **Shareability** | Internal only | **External-ready** |

**When to Use A.5.7.5 (This Dashboard):**

- ✅ Board presentations
- ✅ Executive monthly updates where detailed workbooks aren't available
- ✅ External stakeholder reporting (regulators, customers, partners)
- ✅ Quick monthly snapshots without workbook dependencies
- ✅ Environments where full assessment workbooks (A.5.7.1/2/3) aren't maintained


**When to Use A.5.7.4 (Comprehensive Dashboard):**

- Use when full operational workbooks (A.5.7.1, A.5.7.2, A.5.7.3) are maintained
- Use for detailed program management and KPI tracking
- Use for audits requiring granular evidence


#### What You'll Document

**Manual Entry (15-20 Key Metrics Monthly):**

- Active intelligence sources
- Intelligence products published
- Stakeholders engaged
- **Prevented incidents** (count and estimated value)
- **Intelligence-driven decisions** (count and impact)
- Tool integration status (basic counts)
- Incident-TI integration rate
- Top 3-5 program risks
- Top 5-10 critical actions requiring executive attention
- Quarterly cost-benefit analysis


**Auto-Generated (From Manual Entries):**

- Executive dashboard (one-page visual summary)
- 12-month trend history
- Quarterly summary reports
- ROI calculations
- Risk and action tracking


---

## Prerequisites

### Information You'll Need

**Minimal Prerequisites (10-Minute Monthly Update):**

- **Sources Count**: How many active threat intelligence sources? (from internal tracking or A.5.7.1 if available)
- **Products Count**: How many intelligence products published this month? (reports, alerts, briefings)
- **Prevention Count**: How many incidents prevented this month? (document at least qualitatively)
- **Decisions Count**: How many executive decisions driven by TI this month/quarter?
- **Incident Integration**: What % of P1/P2 incidents used threat intelligence?
- **Top Risks**: What are the top 3-5 program risks right now?
- **Top Actions**: What are the 5-10 most critical actions needing executive attention?


**Quarterly Prerequisites (Additional 30 Minutes):**

- **Costs**: Total TI program costs this quarter (staffing, tools, services)
- **Benefits**: Estimated value of prevented incidents, decisions, efficiency gains
- **ROI Calculation**: Cost vs. benefit analysis


### Required Tools

- Microsoft Excel (2016 or later)
- Basic understanding of program metrics (no deep technical knowledge required)
- 10 minutes per month for data entry
- 30 minutes per quarter for quarterly summary


### Dependencies

**NONE** - This dashboard is completely standalone.

Optional: Can reference data from A.5.7.1, A.5.7.2, A.5.7.3 if available, but NOT REQUIRED.

---

## Workflow

### 10-Minute Monthly Update Process

**Frequency:** First week of each month

**Time Required:** 10 minutes

**Steps:**

1. **Open Dashboard Workbook**

   - File: `ISMS_A_5_7_5_Standalone_Dashboard_YYYY.xlsx`


2. **Navigate to Sheet 2: Monthly_Data_Entry**

3. **Enter Current Month's Metrics** (one row):

| Metric | Instructions | Example | Time |
|--------|--------------|---------|------|
| **Month** | YYYY-MM | 2026-01 | 10 sec |
| **Active_Sources** | Count of active TI sources | 8 | 20 sec |
| **Products_Published** | Intelligence reports, alerts, briefings published | 12 | 30 sec |
| **IOCs_Deployed** | Indicators deployed to security tools | 450 | 20 sec |
| **Stakeholders_Engaged** | Unique stakeholders receiving intelligence | 35 | 20 sec |
| **Incidents_Prevented** | Count of validated prevented incidents | 2 | 1 min |
| **Prevented_Value_CHF** | Estimated value of prevented incidents | 150000 | 1 min |
| **Decisions_Made** | Intelligence-driven decisions (exec/strategic) | 1 | 30 sec |
| **Decision_Value_CHF** | Estimated value/impact of decisions | 50000 | 30 sec |
| **P1P2_TI_Usage_Percent** | % of P1/P2 incidents using TI | 75 | 30 sec |
| **Tool_Integrations** | Count of security tools integrated with TI | 5 | 20 sec |
| **Analyst_Count** | FTE dedicated to threat intelligence | 2.5 | 10 sec |
| **Training_Hours** | Training hours completed this month | 8 | 20 sec |
| **Top_Risk_1** | Biggest program risk | "Budget constraints limiting source portfolio" | 1 min |
| **Top_Risk_2** | Second biggest risk | "Analyst skill gaps in MITRE ATT&CK" | 30 sec |
| **Top_Risk_3** | Third biggest risk | "SIEM integration not fully automated" | 30 sec |
| **Critical_Action_1** | Most important action | "Approve CHF 50K for additional commercial TI feed" | 1 min |
| **Critical_Action_2** | Second most important | "Hire additional TI analyst (approved, recruiting)" | 30 sec |
| **Notes** | Free text | "Strong month, 2 ransomware incidents prevented" | 1 min |

**TOTAL TIME:** ~10 minutes

4. **Auto-Generated Outputs Update Automatically**:

   - Sheet 3: Executive_Dashboard (refreshes with new data)
   - Sheet 4: Trend_History (appends new month)
   - Charts update automatically


5. **Review Executive Dashboard (Sheet 3)**:

   - Verify data looks correct
   - Check for any errors or anomalies


6. **Save Workbook**

**Deliverable:** Current month's metrics captured, executive dashboard updated

---

### Quarterly Summary Workflow

**Frequency:** Last week of each quarter

**Time Required:** 30-45 minutes (includes monthly update)

**Steps:**

1. **Complete Monthly Update for Quarter-End Month** (10 min)

2. **Navigate to Sheet 6: Quarterly_Summary**

3. **Review Auto-Generated Quarterly Summary**:

   - Quarter-over-quarter comparison
   - Key metrics aggregated
   - Prevention and decision totals calculated


4. **Complete Quarterly-Specific Fields** (manual entry):

| Field | Instructions | Example |
|-------|--------------|---------|
| **Quarter** | YYYY-QX | 2026-Q1 |
| **Program_Costs_CHF** | Total costs for quarter (tools + staff + services) | 250000 |
| **Program_Benefits_CHF** | Total estimated value (prevented + decisions + efficiency) | 800000 |
| **ROI_Ratio** | Benefits / Costs | 3.2 |
| **Maturity_Assessment** | Dropdown: Initial, Repeatable, Defined, Managed, Optimizing | Managed |
| **Key_Achievements** | Top 3-5 achievements this quarter | "1. Prevented 7 incidents (CHF 500K value), 2. Implemented EDR-TI integration, 3. Launched monthly exec briefing" |
| **Key_Challenges** | Top 3-5 challenges | "1. Analyst capacity constraints, 2. Budget approval delays, 3. SIEM automation incomplete" |
| **Next_Quarter_Priorities** | Top priorities for next quarter | "1. Hire additional analyst, 2. Complete SIEM automation, 3. Expand source portfolio" |

5. **Navigate to Sheet 7: Risk_Summary**

6. **Update Quarterly Risk Summary**:

   - Review top risks from monthly entries
   - Consolidate into top 5-10 program risks
   - Document risk mitigation actions
   - Assess risk trend (Increasing, Stable, Decreasing)


7. **Navigate to Sheet 8: ROI_Summary**

8. **Review Auto-Generated ROI Analysis**:

   - Cost breakdown (staffing, tools, services)
   - Benefit breakdown (prevented incidents, decisions, efficiency)
   - ROI calculation and trend
   - Verify calculations accurate


9. **Export Quarterly Summary for Board**:

   - Sheet 6: Quarterly_Summary → Export to PDF
   - Sheet 3: Executive_Dashboard → Export to PowerPoint (screenshot)
   - Prepare 1-slide summary for board deck


10. **CISO/Executive Review & Approval**:

   - CISO reviews quarterly summary
   - Executive/Board approves (if presented)
   - Document approval in workbook


**Deliverable:** Quarterly summary report, board-ready presentation materials, ROI analysis

---

### Board Presentation Guidelines

**Recommended Board Presentation Structure** (Single Slide or 3-Slide Deck):

**Slide 1: Executive Summary** (1 minute)

- Screenshot of Sheet 3: Executive_Dashboard
- Highlights:
  * "7 incidents prevented this quarter (CHF 500K estimated value)"
  * "TI program ROI: 3.2:1 (CHF 800K benefit on CHF 250K investment)"
  * "75% of critical incidents used threat intelligence (target: 70%)"


**Slide 2: Prevented Incidents & Decisions** (Optional, 2 minutes)

- Top 2-3 prevented incidents (brief descriptions)
- Top 2-3 intelligence-driven decisions
- Demonstrates tangible program value


**Slide 3: Program Health & Priorities** (Optional, 2 minutes)

- Top 3 risks and mitigation actions
- Top 3 priorities for next quarter
- Resource requests (if any)


**Total Presentation Time:** 1-5 minutes depending on board engagement

**Key Messages for Board:**

- ✅ "Threat intelligence program prevented X incidents, saving estimated CHF Y"
- ✅ "Program ROI is Z:1, demonstrating strong value"
- ✅ "Intelligence is integrated into incident response (W% usage rate)"
- ✅ "Program is mature and well-managed (Maturity Level: X)"
- ✅ "Seeking approval for [specific resource/decision if applicable]"


---

## Evidence Collection (Lightweight)

**For This Standalone Dashboard, Evidence is Minimal:**

**Monthly:**

- Screenshot of Sheet 3 (Executive_Dashboard) each month
- Save monthly snapshot of workbook


**Quarterly:**

- PDF export of Sheet 6 (Quarterly_Summary)
- Board presentation slides (if presented)
- Evidence of prevention/decisions (brief documentation, not exhaustive)


**Annual:**

- 12-month trend chart from Sheet 4
- Annual ROI summary from Sheet 8
- Progression of maturity level


**Storage:**
```
Evidence/
├── 2026-Q1/
│   ├── Monthly_Snapshots/
│   │   ├── 2026-01_Dashboard.pdf
│   │   ├── 2026-02_Dashboard.pdf
│   │   └── 2026-03_Dashboard.pdf
│   ├── 2026-Q1_Quarterly_Summary.pdf
│   ├── 2026-Q1_Board_Presentation.pptx
│   └── 2026-Q1_Prevention_Examples.pdf (brief)
└── 2026-Q2/
    └── ...
```

**Retention:** 3 years (ISO 27001 requirement)

---

## Review & Approval

### Monthly Review

**Level 1: CISO**

- Reviews monthly data entry for reasonableness
- Approves dashboard for executive distribution
- Timeline: Within 5 business days of month-end


### Quarterly Review

**Level 1: CISO**

- Reviews quarterly summary
- Prepares board presentation (if applicable)
- Approves quarterly report


**Level 2: Executive Management / Board**

- Reviews quarterly summary and dashboard
- Receives board presentation (if applicable)
- Provides feedback or approvals
- Timeline: Within 15 business days of quarter-end


**Approval Documentation:**

- Monthly: CISO initials in Sheet 2 (Monthly_Data_Entry)
- Quarterly: Executive/Board approval in Sheet 6 (Quarterly_Summary)


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_5_Standalone_Dashboard_YYYY.xlsx`

**Example:** `ISMS_A_5_7_5_Standalone_Dashboard_2026.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only yellow cells in Sheet 2 editable)
- Macros: None (VBA-free for security)
- **External Links: NONE** - Completely standalone


**Total Sheets:** 9

**Tab Colors:**

- Instructions (Sheet 1): Blue (#4472C4)
- Data Entry (Sheet 2): Yellow (#FFD966)
- Executive Dashboard (Sheet 3): Green (#70AD47)
- Trend History (Sheet 4): Teal (#00B0F0)
- Critical Actions (Sheet 5): Orange (#FFA500)
- Quarterly Summary (Sheet 6): Purple (#7030A0)
- Risk Summary (Sheet 7): Red (#C00000)
- ROI Summary (Sheet 8): Green (#70AD47)
- Metadata (Sheet 9): Gray (#D9D9D9)


**Key Design Principles:**
1. **Simplicity**: 10-minute monthly data entry (one row per month)
2. **Automation**: All charts, trends, summaries auto-generate from Sheet 2
3. **Visual**: Executive dashboard designed for printing/PDF export (one-page view)
4. **Portability**: No dependencies, shareable externally
5. **Board-Ready**: Quarterly summaries formatted for board presentations

---


## Sheet-by-Sheet Technical Specifications

### Sheet 1: Instructions

**Purpose:** User guide for dashboard

**Content:**

- Dashboard overview and purpose
- Key differences vs. A.5.7.4
- 10-minute monthly update workflow
- Quarterly summary workflow
- Board presentation guidelines
- Data entry instructions for Sheet 2
- How to interpret executive dashboard (Sheet 3)
- Troubleshooting guide


**Protection:** Read-only

---

### Sheet 2: Monthly_Data_Entry

**Purpose:** Single data entry point for all monthly metrics

**Structure:** Table with one row per month, 12 months visible (scroll for history)

**Columns:**

| Column | Type | Validation | Formula | Notes |
|--------|------|------------|---------|-------|
| **Month** | Date (YYYY-MM) | Format: YYYY-MM | Manual entry | First day of month |
| **Active_Sources** | Integer ≥0 | 0-100 range | Manual entry | Count of active TI sources |
| **Products_Published** | Integer ≥0 | 0-1000 range | Manual entry | Reports, alerts, briefings published |
| **IOCs_Deployed** | Integer ≥0 | 0-100000 range | Manual entry | Indicators deployed to security tools |
| **Stakeholders_Engaged** | Integer ≥0 | 0-500 range | Manual entry | Unique stakeholders receiving intelligence |
| **Incidents_Prevented** | Integer ≥0 | 0-50 range | Manual entry | Validated prevented incidents |
| **Prevented_Value_CHF** | Currency ≥0 | - | Manual entry | Estimated value of prevented incidents |
| **Decisions_Made** | Integer ≥0 | 0-20 range | Manual entry | Intelligence-driven decisions (exec/strategic) |
| **Decision_Value_CHF** | Currency ≥0 | - | Manual entry | Estimated value/impact of decisions |
| **P1P2_TI_Usage_Percent** | Percentage 0-100 | 0-100 | Manual entry | % of P1/P2 incidents using TI |
| **Tool_Integrations** | Integer ≥0 | 0-50 range | Manual entry | Count of integrated security tools |
| **Analyst_Count** | Decimal ≥0 | 0-50 (0.5 steps) | Manual entry | FTE dedicated to threat intelligence |
| **Training_Hours** | Integer ≥0 | 0-500 range | Manual entry | Training hours completed this month |
| **Top_Risk_1** | Text | Max 200 chars | Manual entry | Biggest program risk |
| **Top_Risk_2** | Text | Max 200 chars | Manual entry | Second biggest risk |
| **Top_Risk_3** | Text | Max 200 chars | Manual entry | Third biggest risk |
| **Critical_Action_1** | Text | Max 200 chars | Manual entry | Most important action |
| **Critical_Action_2** | Text | Max 200 chars | Manual entry | Second most important action |
| **Critical_Action_3** | Text | Max 200 chars | Manual entry | Third most important action |
| **Notes** | Text | Max 500 chars | Manual entry | Free text commentary |
| **CISO_Initials** | Text | 2-5 chars | Manual entry | CISO approval initials |
| **Quarter** | Text | Auto-calculated | `=TEXT(Month,"YYYY-\QQ")` | Derived from month |
| **Total_Value_CHF** | Currency | Auto-calculated | `=Prevented_Value_CHF + Decision_Value_CHF` | Combined value |

**Protection:** Only yellow cells editable (all metrics columns)

**Conditional Formatting:**

- Incidents_Prevented ≥3 → Green (quarterly target met)
- P1P2_TI_Usage_Percent ≥70 → Green (target met)
- P1P2_TI_Usage_Percent <70 → Orange (below target)
- Any required field blank → Red


**Data Validation:**

- All integer fields: Whole numbers only
- All percentage fields: 0-100 range
- All currency fields: Non-negative
- Text fields: Character limits enforced


---

### Sheet 3: Executive_Dashboard

**Purpose:** One-page visual dashboard auto-generated from Sheet 2

**Layout:** Designed for printing/PDF export (single page, landscape)

**Sections:**

**A. Header (Rows 1-3):**

- Title: "Threat Intelligence Program - Executive Dashboard"
- Current Month: `=TEXT(MAX(Monthly_Data_Entry!Month),"MMMM YYYY")`
- Dashboard Status: "Current" / "Out of Date" (based on last update)


**B. Key Metrics Summary (Rows 4-10, Columns A-D):**

- **This Month:**
  * Incidents Prevented: `=XLOOKUP(MAX(Month), Month, Incidents_Prevented)`
  * Value Prevented: `=TEXT(XLOOKUP(MAX(Month), Month, Prevented_Value_CHF),"CHF #,##0")`
  * Decisions Made: `=XLOOKUP(MAX(Month), Month, Decisions_Made)`
  * Decision Value: `=TEXT(XLOOKUP(MAX(Month), Month, Decision_Value_CHF),"CHF #,##0")`
  * Products Published: `=XLOOKUP(MAX(Month), Month, Products_Published)`
  * Stakeholders Engaged: `=XLOOKUP(MAX(Month), Month, Stakeholders_Engaged)`

- **This Quarter (Columns E-H):**
  * Total Incidents Prevented: `=SUMIFS(Incidents_Prevented, Quarter, current_quarter)`
  * Total Value Prevented: `=TEXT(SUMIFS(Prevented_Value_CHF, Quarter, current_quarter),"CHF #,##0")`
  * Total Decisions: `=SUMIFS(Decisions_Made, Quarter, current_quarter)`
  * Average P1/P2 TI Usage: `=AVERAGE(IF(Quarter=current_quarter, P1P2_TI_Usage_Percent))`


**C. Status Indicators (Rows 4-10, Columns I-J):**

- **Prevention Target:** ≥3/quarter → Green checkmark or Red X
- **P1/P2 TI Usage Target:** ≥70% → Green checkmark or Red X
- **Decision Target:** ≥5/quarter → Green checkmark or Red X


**D. Charts (Rows 11-30):**

- **Chart 1 (Rows 11-20):** 12-Month Trend - Incidents Prevented (Column chart)
- **Chart 2 (Rows 11-20):** 12-Month Trend - Value Prevented (Line chart)
- **Chart 3 (Rows 21-30):** 12-Month Trend - P1/P2 TI Usage % (Line chart with 70% target line)
- **Chart 4 (Rows 21-30):** Quarterly Comparison - Incidents, Decisions, Value (Clustered column)


**E. Top Risks (Rows 31-35):**

- Lists Top_Risk_1, Top_Risk_2, Top_Risk_3 from current month


**F. Critical Actions (Rows 36-40):**

- Lists Critical_Action_1, Critical_Action_2, Critical_Action_3 from current month


**Protection:** Fully protected (read-only, auto-generated)

**Conditional Formatting:**

- Status indicators: Green (✓) if target met, Red (✗) if not met
- Value cells: Green if >0, Gray if 0


---

### Sheet 4: Trend_History

**Purpose:** 12-month rolling history with trend visualization

**Structure:** Table pulling last 12 months from Sheet 2

**Columns:**

- All columns from Sheet 2 (Monthly_Data_Entry)
- Filtered to show last 12 complete months


**Formulas:**

- Uses `=FILTER(Monthly_Data_Entry!A:Z, Monthly_Data_Entry!Month >= TODAY()-365)`
- Sorted by Month descending (most recent first)


**Charts:**

- 12-month trend for each key metric
- Month-over-month change calculations
- Moving averages (3-month)


**Protection:** Read-only (auto-generated)

---

### Sheet 5: Critical_Actions

**Purpose:** Consolidated view of all critical actions from recent months

**Structure:** Table extracting Critical_Action_1/2/3 from last 6 months

**Columns:**
| Column | Source | Formula |
|--------|--------|---------|
| **Month** | Sheet 2 | Month |
| **Action** | Sheet 2 | Critical_Action_1, _2, _3 (unpivoted) |
| **Status** | Manual entry | Dropdown: Open, In Progress, Completed, Cancelled |
| **Owner** | Manual entry | Text |
| **Due_Date** | Manual entry | Date |
| **Notes** | Manual entry | Text |

**Protection:** Yellow cells editable (Status, Owner, Due_Date, Notes)

**Conditional Formatting:**

- Status "Open" + Due_Date overdue → Red
- Status "Completed" → Green


---

### Sheet 6: Quarterly_Summary

**Purpose:** Auto-generated quarterly summary report

**Structure:** One section per quarter (Q1-Q4)

**For Each Quarter:**

**A. Quarter Header:**

- Quarter: "YYYY-QX"
- Date Range: "01.MM.YYYY - DD.MM.YYYY"


**B. Key Metrics (Auto-Calculated from Sheet 2):**
| Metric | Formula |
|--------|---------|
| **Incidents Prevented** | `=SUMIFS(Incidents_Prevented, Quarter, "2026-Q1")` |
| **Value Prevented (CHF)** | `=SUMIFS(Prevented_Value_CHF, Quarter, "2026-Q1")` |
| **Decisions Made** | `=SUMIFS(Decisions_Made, Quarter, "2026-Q1")` |
| **Decision Value (CHF)** | `=SUMIFS(Decision_Value_CHF, Quarter, "2026-Q1")` |
| **Products Published** | `=SUMIFS(Products_Published, Quarter, "2026-Q1")` |
| **Avg Stakeholder Engagement** | `=AVERAGE(IF(Quarter="2026-Q1", Stakeholders_Engaged))` |
| **Avg P1/P2 TI Usage %** | `=AVERAGE(IF(Quarter="2026-Q1", P1P2_TI_Usage_Percent))` |

**C. Target Compliance (Auto-Calculated):**
| Target | Actual | Status |
|--------|--------|--------|
| **Prevention: ≥3/quarter** | `=Incidents_Prevented` | Met / Not Met |
| **P1/P2 TI Usage: ≥70%** | `=Avg P1/P2 TI Usage %` | Met / Not Met |
| **Decisions: ≥5/quarter** | `=Decisions_Made` | Met / Not Met |

**D. Manual Entry Fields (Yellow Cells):**
| Field | Type | Notes |
|-------|------|-------|
| **Program_Costs_CHF** | Currency | Total costs for quarter |
| **Program_Benefits_CHF** | Currency | Total estimated value |
| **ROI_Ratio** | Decimal | Benefits / Costs |
| **Maturity_Assessment** | Dropdown | Initial, Repeatable, Defined, Managed, Optimizing |
| **Key_Achievements** | Text (500 chars) | Top achievements |
| **Key_Challenges** | Text (500 chars) | Top challenges |
| **Next_Quarter_Priorities** | Text (500 chars) | Priorities |
| **Executive_Approval** | Text | Name/signature |
| **Approval_Date** | Date | Date approved |

**Protection:** Only yellow cells editable

---

### Sheet 7: Risk_Summary

**Purpose:** Consolidated quarterly risk summary

**Structure:** Table of top 5-10 program risks with tracking

**Columns:**
| Column | Type | Validation | Notes |
|--------|------|------------|-------|
| **Quarter** | Text | YYYY-QX | Which quarter |
| **Risk_ID** | Text | Auto-generated | RISK-YYYY-QX-NN |
| **Risk_Description** | Text | Max 500 chars | Description of risk |
| **Risk_Impact** | Dropdown | Critical, High, Medium, Low | Potential impact |
| **Risk_Likelihood** | Dropdown | Very Likely, Likely, Possible, Unlikely | Probability |
| **Risk_Score** | Integer | Auto-calc | Impact × Likelihood (1-25 scale) |
| **Risk_Trend** | Dropdown | Increasing, Stable, Decreasing | Trend since last quarter |
| **Mitigation_Action** | Text | Max 500 chars | What's being done |
| **Action_Owner** | Text | - | Who is responsible |
| **Target_Date** | Date | - | When will risk be mitigated |
| **Status** | Dropdown | Open, In Progress, Mitigated, Accepted | Current status |

**Protection:** Yellow cells editable

**Conditional Formatting:**

- Risk_Score ≥20 (Critical × Very Likely) → Red
- Risk_Score 15-19 → Orange
- Risk_Score 8-14 → Yellow
- Status "Mitigated" → Green


---

### Sheet 8: ROI_Summary

**Purpose:** Quarterly and annual ROI analysis

**Structure:** Multi-section layout

**A. Cost Breakdown (Per Quarter):**
| Cost Category | Q1 | Q2 | Q3 | Q4 | Annual |
|---------------|-----|-----|-----|-----|--------|
| **Staff Costs** | Manual | Manual | Manual | Manual | `=SUM(Q1:Q4)` |
| **Tool/Service Costs** | Manual | Manual | Manual | Manual | `=SUM(Q1:Q4)` |
| **Training Costs** | Manual | Manual | Manual | Manual | `=SUM(Q1:Q4)` |
| **Other Costs** | Manual | Manual | Manual | Manual | `=SUM(Q1:Q4)` |
| **Total Costs** | `=SUM(above)` | | | | `=SUM(Q1:Q4)` |

**B. Benefit Breakdown (Per Quarter):**
| Benefit Category | Q1 | Q2 | Q3 | Q4 | Annual |
|------------------|-----|-----|-----|-----|--------|
| **Prevented Incident Value** | From Sheet 6 | | | | `=SUM(Q1:Q4)` |
| **Decision Value** | From Sheet 6 | | | | `=SUM(Q1:Q4)` |
| **Efficiency Gains** | Manual est. | | | | `=SUM(Q1:Q4)` |
| **Risk Reduction Value** | Manual est. | | | | `=SUM(Q1:Q4)` |
| **Total Benefits** | `=SUM(above)` | | | | `=SUM(Q1:Q4)` |

**C. ROI Calculations:**
| Metric | Formula | Notes |
|--------|---------|-------|
| **Quarterly ROI** | `=Benefits_Q / Costs_Q` | Per quarter |
| **Annual ROI** | `=Total_Benefits / Total_Costs` | Annual average |
| **ROI Trend** | Chart | Quarterly ROI over time |
| **Payback Period** | `=Costs / (Benefits/4)` | Months to payback |

**D. ROI Visualization:**

- Chart: Quarterly costs vs. benefits (clustered column)
- Chart: ROI trend over time (line chart)
- Sparklines: Quick ROI trend for executive summary


**Protection:** Yellow cells editable (cost/benefit estimates)

---

### Sheet 9: Metadata

**Purpose:** Document provenance and version control

**Content:**

- Workbook generation date
- Current version number
- Policy framework reference (ISMS-POL-A.5.7)
- IMP specification reference (ISMS-IMP-A.5.7.5 v2.0)
- Total sheets: 9
- Data entry instructions summary
- Change log
- Dependencies: NONE (standalone)


**Protection:** Read-only

---

## Related Documents

**Policy Framework:**

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements)
- **ISMS-POL-A.5.7, Section 3.4** (Policy Governance)


**Implementation Specifications:**

- **ISMS-IMP-A.5.7.1** (Sources Assessment) - Optional reference (not required)
- **ISMS-IMP-A.5.7.2** (Collection & Analysis Assessment) - Optional reference (not required)
- **ISMS-IMP-A.5.7.3** (Integration & Distribution Assessment) - Optional reference (not required)


**Comprehensive Alternative:**

- **ISMS-IMP-A.5.7.4** (Effectiveness Dashboard) - Comprehensive dashboard with external references (use if full workbooks maintained)


**Standards References:**

- ISO/IEC 27001:2022 Annex A Control A.5.7
- ISO/IEC 27002:2022 Control 5.7 Implementation Guidance


---

**END OF SPECIFICATION**

---

*"If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-01-31 -->
