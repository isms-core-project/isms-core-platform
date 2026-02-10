<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.5-UG:framework:UG:a.5.7.5 -->
**ISMS-IMP-A.5.7.5-UG - Threat Intelligence Standalone Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.5-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.7.5-TG.

---

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
