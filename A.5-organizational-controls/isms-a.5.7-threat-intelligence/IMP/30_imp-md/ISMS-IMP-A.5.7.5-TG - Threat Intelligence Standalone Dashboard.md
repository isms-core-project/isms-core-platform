**ISMS-IMP-A.5.7.5-TG - Threat Intelligence Standalone Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.5-TG |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.7.5-UG.

---

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
