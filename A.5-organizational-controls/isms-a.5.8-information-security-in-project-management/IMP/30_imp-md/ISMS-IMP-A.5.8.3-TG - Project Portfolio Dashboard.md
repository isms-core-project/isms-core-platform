**ISMS-IMP-A.5.8.3-TG - Project Portfolio Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.8.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Project Portfolio Security Status & Executive Visibility |
| **Related Policy** | ISMS-POL-A.5.8 (All Sections - Portfolio-Wide View) |
| **Purpose** | Consolidated executive dashboard aggregating security status across all organizational projects, providing portfolio-wide visibility, trend analysis, gap identification, and lessons learned synthesis for strategic decision-making |
| **Target Audience** | CISO, Executive Management, PMO Director, Board of Directors, Internal Auditors, External Auditors |
| **Assessment Type** | Consolidated Dashboard & Portfolio Analysis (Layer 2 - consolidates multiple A.5.8.1 assessments) |
| **Review Cycle** | Quarterly (minimum) or After Major Project Milestones |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Project Portfolio Dashboard workbook | ISMS Implementation Team |

---

# Technical Specification

**Audience:** Workbook Developers, Data Analysts, Python/Power BI Developers

---

# Technical Implementation Options

Three implementation approaches depending on organization size and technical capability:

| Option | Best For | Pros | Cons | Setup Time | Update Time |
|--------|----------|------|------|------------|-------------|
| **A: Manual Excel** | <15 projects | Simple, no coding | Time-consuming, error-prone | 4-8 hours | 2-4 hours/quarter |
| **B: Python Script** | 15-100 projects | Automated, scalable | Requires Python skills | 8-16 hours | 15 min/quarter |
| **C: Power BI** | 100+ projects or real-time needs | Interactive, real-time | Complex setup, licensing costs | 16-40 hours | Auto-refresh |

**Recommended Path:** Start with Option A (manual), transition to Option B (Python) once portfolio >15 projects and process stable.

---

# Option A: Manual Excel Dashboard

## Workbook Structure

**Sheet Layout:**

| # | Sheet Name | Purpose | Source Data |
|---|------------|---------|-------------|
| 1 | Instructions | Usage guide | Manual entry |
| 2 | Project Data Table | Consolidated project data (manually entered from A.5.8.1 workbooks) | Manual extraction |
| 3 | Executive Summary | Component 1 - One-page snapshot | Formulas from Sheet 2 |
| 4 | Project Status | Component 2 - Project-by-project table | Sheet 2 with formatting |
| 5 | Gap Analysis | Component 3 - Common gaps | Manual entry or pivot from Sheet 2 |
| 6 | Trends | Component 4 - QoQ trends | Formulas + manual historical data |
| 7 | Risk Prioritization | Component 5 - Priority matrix | Formulas from Sheet 2 |
| 8 | Lessons Learned | Component 6 - Synthesis | Manual synthesis from projects |
| 9 | Regulatory Compliance | Component 7 - Compliance view | Manual entry |
| 10 | Resources & Budget | Component 8 - Budget analysis | Manual entry from finance data |
| 11 | Charts | All charts for dashboard | Chart objects linked to data sheets |

---

## Sheet 2: Project Data Table - Manual Entry Template

**Purpose:** Central data table where all project data manually entered from A.5.8.1 workbooks

**Table Structure (Columns A-P):**

| Col | Field | Data Type | Source (from A.5.8.1) | Formula/Manual |
|-----|-------|-----------|----------------------|----------------|
| A | Project Name | Text | Sheet 2, Cell B5 | Manual copy |
| B | Classification | Dropdown | Sheet 2, Cell H58 | Manual copy |
| C | Project Manager | Text | Sheet 2, Cell B7 | Manual copy |
| D | Business Owner | Text | Sheet 2, Cell B8 | Manual copy |
| E | Current Phase | Dropdown | Sheet 8, Current Phase cell | Manual copy |
| F | Overall Compliance Score | Percentage (0-100%) | Sheet 8, Compliance Score cell | Manual copy |
| G | Initiation Score | Percentage | Sheet 3, Phase Score | Manual copy (optional, for detailed analysis) |
| H | Planning Score | Percentage | Sheet 4, Phase Score | Manual copy (optional) |
| I | Execution Score | Percentage | Sheet 5, Phase Score | Manual copy (optional) |
| J | Monitoring Score | Percentage | Sheet 6, Phase Score | Manual copy (optional) |
| K | Closure Score | Percentage | Sheet 7, Phase Score | Manual copy (optional) |
| L | Critical Gaps Count | Number | Sheet 8, Critical Gaps count | Manual count |
| M | High Findings Open | Number | Sheet 5, High findings open count | Manual count |
| N | Target Deployment Date | Date | Sheet 2 or project plan | Manual copy |
| O | Last Assessment Date | Date | File date or Sheet metadata | Manual entry |
| P | Notes | Text | Various | Manual notes (issues, blockers) |

**Additional Columns (Optional):**

- Q: Previous Quarter Score (for trend calculation)
- R: Previous Quarter Date
- S: Budget (total project budget)
- T: Security Budget
- U: Regulatory Flags (GDPR Y/N, PCI Y/N, etc.)

**Pre-format 50-100 rows** for projects

**Data Validation:**

- Classification: Dropdown (High, Medium, Low)
- Current Phase: Dropdown (Initiation, Planning, Execution, Monitoring, Closure, Closed)
- Compliance Score: Number validation (0-100)

**Conditional Formatting:**

- Compliance Score (Column F):
  - ≥85%: Green background (#C6EFCE)
  - 70-84%: Yellow background (#FFEB9C)
  - <70%: Red background (#FFC7CE)

---

## Sheet 3: Executive Summary - Formulas

**Component 1 Implementation**

**Section A: Portfolio Health (Rows 5-15)**

| Row | Label | Cell | Formula |
|-----|-------|------|---------|
| 7 | Portfolio Health Status | C7 | `=IF(AND(C10>=85%,C15=0),"🟢 Green",IF(OR(C10<70%,C15>3),"🔴 Red","🟡 Amber"))` |
| 10 | Portfolio Compliance Score | C10 | `=SUMPRODUCT(ProjectData!$F$2:$F$50,ProjectData!$B$2:$B$50="High")*3 + SUMPRODUCT(ProjectData!$F$2:$F$50,ProjectData!$B$2:$B$50="Medium")*2 + SUMPRODUCT(ProjectData!$F$2:$F$50,ProjectData!$B$2:$B$50="Low")*1) / (COUNTIF(ProjectData!$B$2:$B$50,"High")*3 + COUNTIF(ProjectData!$B$2:$B$50,"Medium")*2 + COUNTIF(ProjectData!$B$2:$B$50,"Low")*1)` |
| 12 | Total Projects | C12 | `=COUNTA(ProjectData!$A$2:$A$50)` |
| 13 | High Risk Projects | C13 | `=COUNTIF(ProjectData!$B$2:$B$50,"High")` & " (" & TEXT(C13/C12,"0%") & ")" |
| 14 | Medium Risk Projects | C14 | `=COUNTIF(ProjectData!$B$2:$B$50,"Medium")` |
| 15 | Low Risk Projects | C15 | `=COUNTIF(ProjectData!$B$2:$B$50,"Low")` |

**Section B: Key Metrics (Rows 18-25)**

| Row | Metric | Formula |
|-----|--------|---------|
| 20 | Projects ≥85% | `=COUNTIF(ProjectData!$F$2:$F$50,">=85%")` & " of " & Total |
| 21 | Projects 70-84% | `=COUNTIFS(ProjectData!$F$2:$F$50,">=70%",ProjectData!$F$2:$F$50,"<85%")` |
| 22 | Projects <70% | `=COUNTIF(ProjectData!$F$2:$F$50,"<70%")` |
| 23 | Critical Gaps | `=SUM(ProjectData!$L$2:$L$50)` |
| 24 | QoQ Trend | `=C10-PreviousQuarterScore` & IF(C10>Prev,"↑","↓") |

**Section C: Top Priority Projects (Table, Rows 28-35)**

Use FILTER or manual table showing projects with:

- Classification = "High" AND Score < 70%
- OR Critical Gaps > 0
- OR High Findings Open > 0

**Section D: Top 3 Gaps (Manual Entry, Rows 38-45)**

From gap analysis (manual synthesis):
```
1. [Gap description] - [X] projects ([%])
2. [Gap description] - [X] projects ([%])
3. [Gap description] - [X] projects ([%])
```

---

## Sheet 4: Project Status Table

**Simply copy Sheet 2 (Project Data Table) with enhanced formatting:**

- Add Status Indicator column (formula based on score + gaps)
- Add Priority column (formula: 1=Critical, 2=High, 3=Medium, 4=Low)
- Format as Table with AutoFilter
- Apply conditional formatting
- Freeze top row (headers)
- Add total/summary row at bottom

**Status Indicator Formula:**
```excel
=IF(AND([@Classification]="High",[@[Compliance Score]]<70%),"🔴",
  IF(OR([@[Critical Gaps]]>0,[@[High Findings]]>0),"🔴",
  IF([@[Compliance Score]]<70%,"🔴",
  IF([@[Compliance Score]]<85%,"🟡","🟢"))))
```

**Priority Formula:**
```excel
=IF(AND([@Classification]="High",[@[Compliance Score]]<70%),1,
  IF(OR([@[Critical Gaps]]>0,[@[High Findings]]>3),1,
  IF(OR([@[Compliance Score]]<60%,AND([@Classification]="High",[@[Compliance Score]]<80%)),2,
  IF([@[Compliance Score]]<80%,3,4))))
```

---

## Sheet 6: Trends

**Historical Data Table:**

Manually maintain historical quarterly data:

| Quarter | Portfolio Score | High Avg | Medium Avg | Low Avg | Total Projects | Green | Yellow | Red |
|---------|----------------|----------|------------|---------|----------------|-------|--------|-----|
| Q1 2024 | 67% | 72% | 65% | 70% | 25 | 8 | 10 | 7 |
| Q2 2024 | 72% | 78% | 70% | 72% | 25 | 10 | 9 | 6 |
| Q3 2024 | 78% | 84% | 76% | 75% | 25 | 12 | 10 | 3 |
| Q4 2024 | 82% | 88% | 81% | 78% | 25 | 16 | 7 | 2 |

**Charts:**
1. **Line Chart:** Portfolio Score Trend (X=Quarter, Y=Score %)
2. **Stacked Bar Chart:** Project Distribution (X=Quarter, Y=Count, Stack=Green/Yellow/Red)

**Manual Update Process:**

- Each quarter: Add new row with current quarter data
- Update charts (data range auto-extends if table formatted)

---

## Sheet 7: Risk Prioritization

**Priority Matrix Table:**

Use formulas to auto-categorize projects:

**Priority 1 (Critical):**
```excel
Filter: =FILTER(ProjectData!A:P, (ProjectData!$B:$B="High")*(ProjectData!$F:$F<70%) + (ProjectData!$L:$L>0) + (ProjectData!$M:$M>3) > 0)
```

Displays only projects matching criteria.

**Alternative (Manual):** Create 4 tables, manually copy projects from Sheet 4 into appropriate priority section.

**Risk Heat Map Chart:**

- Bubble chart: X=Classification (categorical: Low/Medium/High), Y=Compliance Score (0-100%), Bubble Size=Budget
- Color by Priority (Red/Orange/Yellow/Green)

---

## Sheet 11: Charts Collection

**All Charts for Dashboard:**

Create chart objects linked to data sheets:

1. **Portfolio Health Gauge** - Dial chart showing compliance score (0-100%) with color zones
2. **Portfolio Composition Pie Chart** - Projects by classification (High/Medium/Low)
3. **Compliance Score Histogram** - Distribution of project scores (bins: <60%, 60-69%, 70-84%, 85-100%)
4. **Trend Line Chart** - Portfolio score over time (from Sheet 6)
5. **Status Distribution Stacked Bar** - Green/Yellow/Red over time (from Sheet 6)
6. **Gap Frequency Bar Chart** - Top 10 gaps (manual data entry)
7. **Risk Heat Map** - Bubble chart (from Sheet 7)

**Chart Placement:**

- Small versions in individual component sheets (for detail view)
- Large versions in Charts sheet (for copy/paste to PowerPoint)

---

# Option B: Python Automated Script

## Script Architecture

**Script:** `generate_a58_3_portfolio_dashboard.py`

**Purpose:** Automatically read all A.5.8.1 workbooks, extract data, generate dashboard workbook

**Key Libraries:**

- `openpyxl`: Read Excel (.xlsx) files, write dashboard workbook
- `pandas`: Data manipulation, aggregation, analysis
- `matplotlib` / `seaborn`: Chart generation (optional - can use Excel charts)
- `pathlib`: File path handling
- `argparse`: Command-line arguments

## Script Flow

```python
import openpyxl
import pandas as pd
from pathlib import Path
import datetime

def main(source_folder, output_file, previous_dashboard=None):
    # Step 1: Discover all A.5.8.1 workbooks in source folder
    workbooks = discover_workbooks(source_folder)
    
    # Step 2: Extract data from each workbook
    project_data = []
    for wb_path in workbooks:
        data = extract_project_data(wb_path)
        project_data.append(data)
    
    # Step 3: Create consolidated DataFrame
    df = pd.DataFrame(project_data)
    
    # Step 4: Calculate portfolio metrics
    metrics = calculate_portfolio_metrics(df)
    
    # Step 5: Perform gap analysis
    gaps = analyze_gaps(workbooks)  # Re-read for gap details
    
    # Step 6: Calculate trends (if previous dashboard provided)
    if previous_dashboard:
        trends = calculate_trends(df, previous_dashboard)
    else:
        trends = None
    
    # Step 7: Generate dashboard workbook
    create_dashboard_workbook(df, metrics, gaps, trends, output_file)
    
    print(f"✅ Dashboard generated: {output_file}")

def discover_workbooks(folder):
    """Find all A.5.8.1 workbooks in folder."""
    folder_path = Path(folder)
    workbooks = list(folder_path.glob("A.5.8.1_*.xlsx"))
    print(f"Found {len(workbooks)} A.5.8.1 workbooks")
    return workbooks

def extract_project_data(wb_path):
    """Extract key data from one A.5.8.1 workbook."""
    wb = openpyxl.load_workbook(wb_path, data_only=True, read_only=True)
    
    # Sheet 2: Classification
    sheet2 = wb['Project Classification']
    project_name = sheet2['B5'].value
    classification = sheet2['H58'].value  # Final Classification
    pm = sheet2['B7'].value
    business_owner = sheet2['B8'].value
    
    # Sheet 8: Dashboard
    sheet8 = wb['Compliance Dashboard']
    compliance_score = sheet8['B_COMPLIANCE_SCORE_CELL'].value  # Adjust cell ref
    current_phase = sheet8['B_CURRENT_PHASE_CELL'].value
    critical_gaps = sheet8['B_CRITICAL_GAPS_CELL'].value
    
    # Sheet 5: Execution
    sheet5 = wb['Execution Phase']
    high_findings = count_findings(sheet5, severity="High")  # Custom function
    
    wb.close()
    
    return {
        'Project Name': project_name,
        'Classification': classification,
        'PM': pm,
        'Business Owner': business_owner,
        'Current Phase': current_phase,
        'Compliance Score': compliance_score,
        'Critical Gaps': critical_gaps,
        'High Findings': high_findings,
        'Source File': wb_path.name,
        'Extract Date': datetime.date.today()
    }

def calculate_portfolio_metrics(df):
    """Calculate portfolio-level metrics."""
    # Weighted average compliance score
    weights = {'High': 3, 'Medium': 2, 'Low': 1}
    df['Weight'] = df['Classification'].map(weights)
    portfolio_score = (df['Compliance Score'] * df['Weight']).sum() / df['Weight'].sum()
    
    # Counts by classification
    counts = df['Classification'].value_counts()
    
    # Projects by status
    df['Status'] = df['Compliance Score'].apply(lambda x: 
        '🟢 Green' if x >= 85 else '🟡 Amber' if x >= 70 else '🔴 Red')
    status_counts = df['Status'].value_counts()
    
    return {
        'Portfolio Score': portfolio_score,
        'Total Projects': len(df),
        'High Risk': counts.get('High', 0),
        'Medium Risk': counts.get('Medium', 0),
        'Low Risk': counts.get('Low', 0),
        'Green Projects': status_counts.get('🟢 Green', 0),
        'Amber Projects': status_counts.get('🟡 Amber', 0),
        'Red Projects': status_counts.get('🔴 Red', 0),
        'Critical Gaps Total': df['Critical Gaps'].sum()
    }

def analyze_gaps(workbooks):
    """Extract all gaps from all projects, count frequency."""
    all_gaps = []
    
    for wb_path in workbooks:
        wb = openpyxl.load_workbook(wb_path, data_only=True, read_only=True)
        sheet8 = wb['Compliance Dashboard']
        
        # Extract gap descriptions (assuming table in Sheet 8)
        # This would need specific row/column logic
        # Simplified example:
        gaps = extract_gaps_from_sheet(sheet8)  # Custom function
        for gap in gaps:
            all_gaps.append({
                'Project': wb_path.stem,
                'Gap Description': gap['description'],
                'Phase': gap['phase'],
                'Impact': gap['impact']
            })
        
        wb.close()
    
    # Count gap frequency
    df_gaps = pd.DataFrame(all_gaps)
    gap_frequency = df_gaps['Gap Description'].value_counts()
    
    return gap_frequency.head(10)  # Top 10 gaps

def create_dashboard_workbook(df, metrics, gaps, trends, output_file):
    """Generate dashboard Excel workbook."""
    wb = openpyxl.Workbook()
    
    # Sheet 1: Project Data
    ws_data = wb.active
    ws_data.title = "Project Data"
    # Write DataFrame to sheet
    write_dataframe_to_sheet(df, ws_data)
    
    # Sheet 2: Executive Summary
    ws_summary = wb.create_sheet("Executive Summary")
    write_executive_summary(ws_summary, metrics, gaps)
    
    # Sheet 3: Project Status (formatted table)
    ws_status = wb.create_sheet("Project Status")
    write_project_status_table(df, ws_status)
    
    # Additional sheets...
    
    wb.save(output_file)

# Helper functions...

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate A.5.8.3 Portfolio Dashboard")
    parser.add_argument("source_folder", help="Folder containing A.5.8.1 workbooks")
    parser.add_argument("-o", "--output", default="Portfolio_Dashboard.xlsx", help="Output file")
    parser.add_argument("-p", "--previous", help="Previous quarter dashboard for trend comparison")
    
    args = parser.parse_args()
    main(args.source_folder, args.output, args.previous)
```

**Script Usage:**
```bash
python generate_a58_3_dashboard.py /path/to/source_data/ -o Portfolio_Dashboard_2024_Q4.xlsx -p Portfolio_Dashboard_2024_Q3.xlsx
```

**Estimated Script Size:** 1,500-2,000 lines (full implementation with all sheets, charts, error handling)

---

# Option C: Power BI Dashboard

## Data Model

**Data Tables:**

**1. Projects Table** (from A.5.8.1 workbooks)
```
Columns:

  - Project Name (text)
  - Classification (text: High/Medium/Low)
  - PM (text)
  - Business Owner (text)
  - Current Phase (text)
  - Compliance Score (decimal 0-1)
  - Critical Gaps (integer)
  - High Findings (integer)
  - Source File (text)
  - Extract Date (date)

```

**2. Historical Scores Table** (for trends)
```
Columns:

  - Project Name (text, relationship key)
  - Quarter (date)
  - Compliance Score (decimal)

```

**3. Gaps Table** (from gap analysis)
```
Columns:

  - Project Name (text, relationship key)
  - Gap Description (text)
  - Phase (text)
  - Impact (text: High/Medium/Low)

```

**4. Date Table** (for time intelligence)
```
Columns:

  - Date (date)
  - Quarter (text: Q1 2024, Q2 2024, etc.)
  - Month (text)
  - Year (integer)

```

**Relationships:**

- Projects[Project Name] → Historical Scores[Project Name] (1:Many)
- Projects[Project Name] → Gaps[Project Name] (1:Many)
- Historical Scores[Quarter] → Date[Date] (Many:1)

## DAX Measures

**Portfolio Metrics:**

```DAX
Portfolio Compliance Score = 
CALCULATE(
    SUMX(
        Projects,
        Projects[Compliance Score] * 
        SWITCH(
            Projects[Classification],
            "High", 3,
            "Medium", 2,
            "Low", 1,
            1
        )
    ) / 
    SUMX(
        Projects,
        SWITCH(
            Projects[Classification],
            "High", 3,
            "Medium", 2,
            "Low", 1,
            1
        )
    )
)

Total Projects = COUNTROWS(Projects)

High Risk Projects = CALCULATE(COUNTROWS(Projects), Projects[Classification] = "High")

Green Projects = CALCULATE(COUNTROWS(Projects), Projects[Compliance Score] >= 0.85)

Red Projects = CALCULATE(COUNTROWS(Projects), Projects[Compliance Score] < 0.70)

Critical Projects = 
CALCULATE(
    COUNTROWS(Projects),
    OR(
        AND(Projects[Classification] = "High", Projects[Compliance Score] < 0.70),
        Projects[Critical Gaps] > 0
    )
)
```

**Trend Measures:**

```DAX
Previous Quarter Score = 
CALCULATE(
    [Portfolio Compliance Score],
    DATEADD(Date[Date], -1, QUARTER)
)

QoQ Change = [Portfolio Compliance Score] - [Previous Quarter Score]

YoY Change = 
CALCULATE(
    [Portfolio Compliance Score],
    SAMEPERIODLASTYEAR(Date[Date])
) - [Portfolio Compliance Score]
```

## Dashboard Pages

**Page 1: Executive Summary**

- Card visuals: Portfolio Score, Total Projects, Portfolio Health Status (conditional formatting)
- Gauge: Portfolio Score (0-100% with color zones)
- Donut chart: Projects by Classification
- Table: Top 5 Priority Projects

**Page 2: Project Details**

- Table: All projects with filters
- Matrix: Projects × Phases with compliance scores
- Slicers: Classification, PM, Current Phase

**Page 3: Trends**

- Line chart: Portfolio Score over time
- Stacked bar chart: Projects by status (Green/Amber/Red) over time
- Waterfall chart: QoQ change breakdown

**Page 4: Gaps**

- Bar chart: Top 10 gaps by frequency
- Table: Gap details with projects affected
- Matrix: Gaps × Phase

**Page 5: Risk Prioritization**

- Scatter plot: Classification (x) × Compliance Score (y), bubble size = budget
- Table: Priority 1-2 projects with action items
- Card: Count of critical priority projects

## Data Refresh

**Manual Refresh:**
1. Update source folder with latest A.5.8.1 workbooks
2. Open Power BI Desktop
3. Click "Refresh" button
4. Publish to Power BI Service

**Scheduled Refresh (Power BI Pro):**
1. Configure data source connection (folder path or SharePoint)
2. Set refresh schedule (e.g., weekly Monday 8am)
3. Power BI Service auto-refreshes dashboard

---

# Integration with A.5.8.1 and A.5.8.2

## Data Extraction Cell Mapping

**Critical Cells to Extract from ISMS-IMP-A.5.8.1:**

| Sheet | Cell Reference | Field | Notes |
|-------|---------------|-------|-------|
| Sheet 2 | B5 | Project Name | Primary key |
| Sheet 2 | H58 | Final Classification | High/Medium/Low |
| Sheet 2 | B7 | Project Manager | Name |
| Sheet 2 | B8 | Business Owner | Name |
| Sheet 8 | [Compliance Score Cell] | Overall Compliance Score | Percentage (0-100%) |
| Sheet 8 | [Current Phase Cell] | Current Phase | Initiation/Planning/Execution/Monitoring/Closure |
| Sheet 8 | [Critical Gaps Cell] | Critical Gaps Count | Integer |
| Sheet 5 | [High Findings Cell] | High Findings Open | Integer from findings table |
| Sheet 7 | [Residual Risk Cell] | Residual Risk Level | If closed: Low/Medium/High |

**Note:** Exact cell references depend on A.5.8.1 workbook structure. Script must use named ranges or fixed cell references consistently across all A.5.8.1 workbooks.

**Integration with A.5.8.2 (Optional):**

- Extract requirement counts (total, by category, by priority)
- Extract implementation rates
- Enables portfolio-level requirement analysis: "What % of projects have MFA requirement?"

---

# Maintenance and Updates

## Quarterly Update Procedure

**Week Before Management Review:**

**Day 1-2: Data Collection**
1. Request latest A.5.8.1 assessments from all active projects
2. Deadline: [Date] for inclusion in quarterly dashboard
3. Validate completeness (check against PMO project list)

**Day 3: Dashboard Generation**
1. Run consolidation process (manual, script, or Power BI refresh)
2. Validate data quality (spot-check 3-5 projects)
3. Generate initial dashboard workbook

**Day 4: Analysis and Insights**
1. Calculate portfolio metrics
2. Identify trends vs. previous quarter
3. Conduct gap analysis (frequency count)
4. Determine priority projects
5. Draft insights and recommendations

**Day 5: Executive Summary Creation**
1. Create PowerPoint presentation (5-10 slides)
2. Write executive narrative
3. Prepare supporting data tables
4. Create charts/visualizations

**Day 6: CISO Review**
1. Present draft dashboard to CISO
2. Validate insights and priorities
3. Refine recommendations
4. Approve for management presentation

**Day 7: Final Preparation**
1. Incorporate CISO feedback
2. Finalize presentation
3. Distribute to management review attendees (1 day before meeting)

**Management Review Day:**
1. Present dashboard (30-45 min)
2. Q&A and discussion
3. Document decisions and action items

**Post-Review:**
1. Publish approved dashboard to shared repository
2. Create action item tracker
3. Update historical data (add current quarter to trend table)

## Annual Comprehensive Review

**In Addition to Quarterly Updates:**

**Q4 Review (Annual Summary):**
1. Full-year trend analysis (compare Q1 vs. Q2 vs. Q3 vs. Q4)
2. Year-over-year comparison (2024 vs. 2023)
3. Lessons learned synthesis (all projects closed in year)
4. Strategic recommendations for next year
5. Board presentation preparation (5-8 slides, very high-level)

**Board Presentation (Annual):**

- Focus: Strategic (not operational details)
- Metrics: Year-over-year trends, program maturity, major achievements
- Decisions: Strategic investments, risk appetite confirmation, multi-year initiatives

## Dashboard Template Version Control

**Template Versioning:**

- Version 1.0 (2025): Initial dashboard template
- Version 1.1 (2025 Q2): Added regulatory compliance view
- Version 2.0 (2026): Redesigned for Power BI (breaking change)

**Version Control Best Practices:**
1. Maintain dashboard template in version control (Git or SharePoint versioning)
2. Tag quarterly releases: `v1.0-Q4-2024`
3. Document changes in VERSION_HISTORY.md
4. Test new template versions with previous quarter's data before rollout
5. Communicate template changes to dashboard users

---

# Troubleshooting Common Issues

## Issue 1: Inconsistent Data from Projects

**Problem:** Project A.5.8.1 workbook has different structure, script extraction fails

**Cause:** A.5.8.1 workbooks not standardized (manual edits, different versions)

**Solution:**

- Enforce use of official A.5.8.1 template (generated from script)
- Validate A.5.8.1 workbook structure before accepting into portfolio dashboard
- Document required cell references in script comments

## Issue 2: Missing Projects in Dashboard

**Problem:** PMO says we have 30 projects, dashboard shows 22

**Cause:** 8 projects missing A.5.8.1 assessments (not submitted or not completed)

**Solution:**

- Cross-reference dashboard against PMO project list
- Flag missing assessments in dashboard: "8 projects without security assessment (30% of portfolio)"
- Follow up with PMs for missing assessments

## Issue 3: Stale Data in Dashboard

**Problem:** Dashboard shows Project X at 65%, but PM says they're now at 80%

**Cause:** Dashboard using old A.5.8.1 workbook (from 3 months ago)

**Solution:**

- Check "Last Assessment Date" column in dashboard
- Request updated A.5.8.1 from PM
- Set policy: Active projects must update A.5.8.1 monthly or at phase gates

## Issue 4: Trend Data Missing

**Problem:** First-time dashboard creation, no historical data for trends

**Cause:** This is first quarterly dashboard, no previous quarters to compare

**Solution:**

- Generate current quarter data
- Note in dashboard: "Baseline quarter, trends will be available Q1 2025"
- Manually backfill historical data if previous quarters' data available (from PMO or InfoSec records)

## Issue 5: Gap Analysis Incomplete

**Problem:** Gap frequency analysis incomplete, many projects show "No gaps recorded"

**Cause:** Projects didn't complete gap analysis in A.5.8.1 Sheet 8

**Solution:**

- Manual gap extraction required (review each project, identify gaps)
- Update A.5.8.1 template to mandate gap documentation (cannot mark Complete without gap section filled)
- Train PMs on importance of gap documentation for lessons learned

---

# Key Success Factors

**For Dashboard Effectiveness:**

1. **Data Quality:** Garbage in = garbage out. Ensure A.5.8.1 assessments are complete, accurate, and current.

2. **Executive Buy-In:** CISO must present dashboard to management and use it for decision-making. If dashboard not used, teams will stop maintaining it.

3. **Actionable Insights:** Dashboard must drive decisions and actions, not just be an information dump. Every red/amber item should have an owner and action plan.

4. **Continuous Improvement:** Use lessons learned to improve security processes, not just report problems.

5. **Automation:** For portfolios >15 projects, automate data extraction to reduce manual effort and errors.

6. **Consistency:** Generate dashboard same time every quarter (e.g., first week after quarter end). Consistency enables trend analysis.

7. **Communication:** Tailor presentation to audience (executives want high-level, InfoSec wants details). Use Executive Summary for Board/executives, detailed sheets for operational teams.

---

**END OF SPECIFICATION**

---

*"A physicist is just an atom's way of looking at itself."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
