<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.8.3-UG:framework:UG:a.5.8.3 -->
**ISMS-IMP-A.5.8.3-UG - Project Portfolio Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Project Portfolio Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.8.3-UG |
| **Related Policy** | ISMS-POL-A.5.8 (Information Security in Project Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.8 (Information Security in Project Management) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.8 (Information Security in Project Management)
- ISMS-IMP-A.5.8.1 (Project Lifecycle Security Assessment)
- ISMS-IMP-A.5.8.2 (Security Requirements Register)

---

### Workbook at a Glance

This workbook contains the following 12 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, control requirements, and field descriptions |
| **Project Data** | Source data table for project security status across the portfolio |
| **Summary Dashboard** | Portfolio-level executive compliance dashboard (auto-populated from Project Data) |
| **Project Status** | Project-by-project security status breakdown |
| **Gap Analysis** | Portfolio-wide gap identification and prioritisation |
| **Trend Analysis** | Quarter-over-quarter trend data for portfolio security posture |
| **Risk Prioritisation** | Risk-based project prioritisation matrix |
| **Lessons Learned** | Synthesis of lessons learned across the portfolio |
| **Regulatory Compliance** | Regulatory compliance status across the portfolio |
| **Resources & Budget** | Resource allocation and budget analysis for security activities |
| **Charts** | Visual charts and graphs for executive presentations |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

# Assessment Overview

## What This Dashboard Provides

This dashboard provides **executive-level visibility into project security integration across the entire organisational project portfolio**.

**Key Questions Answered:**
1. **Portfolio Health:** How are we doing on project security integration overall?
2. **Trend Analysis:** Are we getting better or worse at integrating security into projects?
3. **Risk Identification:** Which projects pose the highest security risk right now?
4. **Resource Allocation:** Where should we focus security resources?
5. **Process Improvement:** What are common gaps that reveal systematic issues?
6. **Compliance Evidence:** Can we demonstrate systematic security oversight to auditors/board?

**Scope:** Portfolio-wide aggregation across 8 dashboard components:

1. **Executive Summary** - One-page portfolio health snapshot (traffic-light status, key metrics, top risks)
2. **Project-by-Project Status** - Sortable table of all projects with security classification, compliance scores, critical gaps
3. **Gap Analysis Across Portfolio** - Common security gaps identified across multiple projects, frequency analysis
4. **Trend Analysis** - Quarter-over-quarter trends in portfolio compliance (charts showing improvement/decline)
5. **Risk-Based Prioritization** - Projects ranked by risk level requiring immediate attention (Priority 1-4 matrix)
6. **Lessons Learned Synthesis** - Aggregated insights from all project retrospectives, common themes
7. **Regulatory Compliance View** - Compliance status by regulation (GDPR, nDSG, PCI DSS v4.0.1, sector-specific)
8. **Resource & Budget Analysis** - Security budget utilization, resource allocation efficiency

**Data Sources:**

- **Primary:** ISMS-IMP-A.5.8.1 (Project Lifecycle Assessment) - from all active and recently closed projects
- **Secondary (optional):** ISMS-IMP-A.5.8.2 (Security Requirements Register) - enhances analysis with requirement-level detail
- **Tertiary:** PMO project portfolio data - project list, classifications, timelines, budgets

**Output Format:**

- Excel workbook with automated dashboards
- Executive PowerPoint summary (1-slide for Board, 5-10 slides for quarterly management review)
- Trend charts suitable for presentation

## Why This Matters

**ISO 27001:2022 Management System Requirements:**

**Clause 9.3 - Management Review:**
> *"Top management shall review the organisation's information security management system at planned intervals to ensure its continuing suitability, adequacy and effectiveness."*

**Management review must include:**

- Performance and effectiveness of ISMS
- Results of risk assessment and status of risk treatment
- Opportunities for continual improvement

**This dashboard directly supports management review by providing:**

- ✅ ISMS performance metrics (project security integration effectiveness)
- ✅ Risk treatment status (project-level risks and remediation)
- ✅ Improvement opportunities (common gaps, lessons learned)

**Regulatory Context:**

**NIS2 Directive (EU Cybersecurity) - Article 21:**

- Management body must oversee ICT risk management measures
- Portfolio view demonstrates management oversight

**DORA (Digital Operational Resilience Act - Financial Sector) - Article 6:**

- ICT risk management framework must be comprehensive
- Portfolio dashboard evidences systematic ICT project oversight

**GDPR Article 24 & 32:**

- Controller must demonstrate appropriate technical and organisational measures
- Portfolio dashboard proves systematic data protection integration in projects

**Business Value:**

**For CISO:**

- Data-driven reporting to executives and board
- Early identification of high-risk projects before they become incidents
- Evidence of security program maturity
- Budget justification (gaps → resource needs)

**For Executive Management:**

- Concise portfolio security summary (not overwhelmed with project details)
- Risk-based prioritization for decision-making
- Trend visibility (are we improving?)
- Accountability (which projects/PMs struggling with security integration?)

**For PMO Director:**

- Project governance oversight (gate review effectiveness)
- Process improvement insights (common gaps = process fixes needed)
- Resource allocation optimization

**For Board of Directors:**

- Governance oversight (demonstrating due diligence)
- Strategic risk visibility (portfolio-wide security risks)
- Assurance that security integrated systematically

**For Auditors:**

- Evidence of systematic Control A.5.8 implementation across portfolio
- Trend data showing continuous improvement
- Sampling framework (identify representative projects for detailed audit)

## Who Uses This Dashboard

**Primary Users:**

**1. Chief Information Security Officer (CISO)**

- **Frequency:** Monthly review, Quarterly deep-dive
- **Uses:**
  - Executive reporting (monthly CISO report to CIO/CEO)
  - Board presentation (quarterly or annual)
  - Budget planning and justification
  - Resource allocation (where to assign security team members)
  - Risk oversight (identify projects requiring CISO attention)
- **Actions:**
  - Approve remediation priorities
  - Escalate critical issues to Executive Management
  - Allocate security budget to address gaps

**2. Executive Management / Leadership Team**

- **Frequency:** Quarterly management review
- **Uses:**
  - Strategic oversight of project security
  - Resource approval decisions
  - Risk acceptance for portfolio-level risks
- **Actions:**
  - Approve budget for security improvements
  - Hold accountable (PMO, InfoSec) for improvement plans
  - Escalate to Board if portfolio risk unacceptable

**3. PMO Director / Program Management Office**

- **Frequency:** Monthly or Quarterly
- **Uses:**
  - Project governance oversight
  - Gate review process effectiveness
  - PM performance (which PMs excel/struggle with security integration)
  - Process improvement (update project templates, training)
- **Actions:**
  - Update PMO processes based on lessons learned
  - Provide additional support to struggling projects
  - Recognize/reward PMs excelling in security integration

**4. Board of Directors**

- **Frequency:** Annually (or quarterly if high-risk portfolio)
- **Uses:**
  - Governance oversight
  - Strategic risk understanding
  - Assurance that management exercising appropriate security diligence
- **Actions:**
  - Review and challenge management on portfolio security
  - Approve significant security investments
  - Provide guidance on risk appetite

**5. Internal Audit / External Auditors**

- **Frequency:** Annual audit cycle
- **Uses:**
  - Evidence of Control A.5.8 systematic implementation
  - Sampling selection (identify projects for detailed audit review)
  - Trend analysis (continuous improvement evidence)
- **Actions:**
  - Verify dashboard data accuracy (sample underlying assessments)
  - Use trends to assess ISMS effectiveness
  - Provide audit findings based on portfolio gaps

**Supporting Roles:**

**6. Information Security Officer / Security Analyst**

- **Responsibility:** Generate dashboard (collect data, run scripts, create charts)
- **Frequency:** Quarterly or as-requested
- **Effort:** 2-4 hours per update (once established)

**7. Project Managers (indirect)**

- **Use:** Understand where their projects rank in portfolio
- **Motivation:** Drive to improve security integration in their projects

## Time Estimate

**Dashboard Generation Effort:**

**Initial Setup (First Time):**

- Collect all project A.5.8.1 assessments: 1-2 hours
- Set up dashboard workbook or scripts: 2-4 hours (if manual) OR 4-8 hours (if scripted/automated)
- Data validation and quality checks: 1-2 hours
- Analysis and insights generation: 2-3 hours
- Executive summary preparation: 2-3 hours (PowerPoint slides)
- **Total First Time:** 8-18 hours (one-time investment)

**Quarterly Updates (Ongoing):**

- Collect new/updated project assessments: 30-60 minutes
- Update dashboard (re-run script or refresh Excel): 15-30 minutes
- Trend analysis (compare to previous quarter): 1-2 hours
- Executive summary update: 1-2 hours
- **Total Quarterly:** 3-5 hours

**Annual Comprehensive Review:**

- Full-year trend analysis: 2-3 hours
- Lessons learned synthesis across all projects: 2-3 hours
- Board presentation preparation: 3-4 hours
- **Total Annual:** 7-10 hours (in addition to quarterly updates)

**Effort by Organisation Size:**

| Organisation Size | Projects/Year | Quarterly Effort | Annual Effort |
|-------------------|---------------|------------------|---------------|
| **Small** (5-15 projects) | 5-15 | 2-3 hours | 5-6 hours |
| **Medium** (15-50 projects) | 15-50 | 3-5 hours | 8-12 hours |
| **Large** (50+ projects) | 50+ | 5-8 hours | 12-20 hours |

**Pro Tips for Efficiency:**

- **Automate data collection:** Python script to read all A.5.8.1 workbooks in folder, extract key cells
- **Template executive summary:** Pre-built PowerPoint template, just update numbers/charts
- **Dashboard tool:** Use Power BI or Tableau for interactive dashboards (vs. static Excel)
- **Standardize file naming:** `A.5.8.1_ProjectName_YYYY-MM-DD.xlsx` for easy scripting
- **PMO collaboration:** PMO provides project list, you add security data

## Connection to Policy and Standards

**ISMS-POL-A.5.8 Implementation:**

This dashboard implements **portfolio-level oversight** required by ISMS-POL-A.5.8:

**Section 4: Governance, Review, and Documentation**

- *"CISO reviews project security integration across portfolio quarterly"*
- *"Annual report to Executive Management on project security program effectiveness"*
- *"Lessons learned from projects inform continuous improvement"*

**ISO 27001:2022 Clause 9.3 - Management Review:**

- Input: Performance indicators, nonconformities, monitoring results, audit results
- Output: Decisions on improvement opportunities, changes to ISMS

**This dashboard provides required inputs:**

- **Performance indicators:** Portfolio compliance scores, trend charts
- **Nonconformities:** Gap analysis, projects failing security gates
- **Monitoring results:** Project-by-project status
- **Improvement opportunities:** Lessons learned synthesis, common gaps

**ISO 27002:2022 Guidance on Control A.5.8:**

- *"The organisation should regularly review the security aspects of projects to ensure information security is integrated."*
- Dashboard enables systematic review across portfolio

**Regulatory Alignment:**

**NIS2 (Network and Information Security Directive 2):**

- Article 21: Management body oversight of cybersecurity risk management
- Portfolio dashboard demonstrates management oversight

**DORA (Digital Operational Resilience Act):**

- Article 6: ICT risk management framework
- Article 11: Testing of ICT systems
- Portfolio view of ICT project security demonstrates framework

**GDPR:**

- Article 24: Controller demonstrates appropriate measures
- Article 32: Appropriate technical and organisational measures
- Portfolio dashboard proves systematic data protection integration

---

# Prerequisites

## Data Sources Required

**Primary Data Source - MANDATORY:**

**ISMS-IMP-A.5.8.1 Workbooks (Project Lifecycle Assessments):**

- Location: All completed A.5.8.1 assessments from portfolio projects
- File format: Excel (.xlsx) workbooks
- Scope: Include all projects from:
  - Active projects (currently in Execution or Monitoring)
  - Recently closed projects (closed within last 12 months for trend analysis)
  - Optionally: Projects in Planning (for pipeline visibility)
- **Minimum data needed:** 3-5 project assessments for meaningful portfolio view
- **Recommended:** 10+ projects for robust trend analysis

**File Organisation Best Practice:**
```
/isms/assessments/a58_1/
  ├── 2024_Q1/
  │   ├── A.5.8.1_CustomerPortal_2024-03-15.xlsx
  │   ├── A.5.8.1_PaymentGateway_2024-03-22.xlsx
  │   └── A.5.8.1_CRM_Upgrade_2024-03-28.xlsx
  ├── 2024_Q2/
  │   ├── A.5.8.1_DataWarehouse_2024-06-10.xlsx
  │   ├── A.5.8.1_Mobile_App_2024-06-18.xlsx
  │   └── ...
  ├── 2024_Q3/
  └── 2024_Q4/
```

**Naming Convention:** `A.5.8.1_[ProjectName]_YYYY-MM-DD.xlsx`

- Enables scripted data extraction
- Facilitates quarterly comparisons

**Secondary Data Source - OPTIONAL:**

**ISMS-IMP-A.5.8.2 Workbooks (Security Requirements Registers):**

- Enhances portfolio analysis with requirement-level detail
- Enables cross-project requirement patterns (e.g., "80% of projects have MFA requirement")
- Not mandatory for basic dashboard

**PMO Project Portfolio Data - HELPFUL:**

- Master project list with: Project name, PM, business owner, status, budget, timeline
- Helps identify missing A.5.8.1 assessments (projects without security assessment)
- Validates completeness (are all projects assessed?)

## Access Required

**File System Access:**

- [ ] Read access to folder containing all A.5.8.1 assessment workbooks
- [ ] Write access to folder for dashboard output
- [ ] (If scripted) Python/PowerShell execution permissions

**Tools Required:**

- [ ] Microsoft Excel 2016+ or compatible (for manual dashboard)
- [ ] Python 3.8+ with openpyxl library (for automated script)
- [ ] OR Power BI / Tableau (for interactive dashboard option)
- [ ] Microsoft PowerPoint (for executive summary presentations)

**Information Access:**

- [ ] ISMS-POL-A.5.8 policy (for reference)
- [ ] Previous quarter's portfolio dashboard (for trend comparison)
- [ ] PMO project list (for completeness check)

## Knowledge Required

**Essential Understanding:**

**1. Portfolio Metrics and KPIs:**

- What is "portfolio compliance score"? (weighted average of project compliance scores)
- How to interpret trends (upward trend = improvement, downward = decline)
- What constitutes acceptable vs. unacceptable portfolio risk

**2. Data Analysis:**

- Aggregation methods (average, weighted average, median, percentiles)
- Trend analysis (quarter-over-quarter, year-over-year)
- Gap frequency analysis (count occurrences of same gap across projects)

**3. Executive Communication:**

- How to distill complex data into executive summary (1-page rule)
- Traffic-light reporting (red/amber/green status indicators)
- Storytelling with data (narratives, not just numbers)

**4. Project Portfolio Management Concepts:**

- What is a project portfolio?
- Portfolio risk vs. individual project risk
- Resource allocation across portfolio

**5. Excel or Dashboard Tool Skills:**

- Advanced Excel: Pivot tables, charts, formulas (SUMIF, COUNTIF, AVERAGEIF)
- OR Python: pandas for data manipulation, openpyxl for Excel
- OR Power BI/Tableau: data modeling, visualization

## Tools Needed

**Option A: Manual Excel Dashboard (Simple, No Coding)**

**Tools:**

- Microsoft Excel 2016+
- Templates provided in Part II of this document

**Pros:**

- No programming required
- Easy to customize
- Familiar tool

**Cons:**

- Manual data entry from each A.5.8.1 workbook (time-consuming for >10 projects)
- Error-prone (copy/paste mistakes)
- Tedious to update quarterly

**Best For:** Small portfolios (<15 projects), organisations without scripting capability

---

**Option B: Python Automated Script (Recommended for >15 projects)**

**Tools:**

- Python 3.8+
- Libraries: openpyxl (Excel manipulation), pandas (data analysis), matplotlib/seaborn (charts)
- Script template provided in Part II

**Pros:**

- Automated data extraction (reads all A.5.8.1 workbooks automatically)
- Scalable (handles 100+ projects easily)
- Repeatable (quarterly update = just re-run script)
- Consistent (no human error in data extraction)

**Cons:**

- Requires Python skills (or IT support to set up)
- Initial setup time (4-8 hours to develop/customize script)

**Best For:** Medium/large portfolios (15+ projects), organisations with technical capability

---

**Option C: Power BI / Tableau Interactive Dashboard (Advanced)**

**Tools:**

- Power BI Desktop (Microsoft) or Tableau Desktop
- Data connection to Excel files or database

**Pros:**

- Interactive dashboards (drill-down, filtering, dynamic charts)
- Real-time or near-real-time updates
- Professional visualizations
- Shareable (publish to Power BI Service or Tableau Server)

**Cons:**

- Licensing costs (Power BI Pro, Tableau Creator)
- Learning curve (dashboard design skills)
- Setup complexity (data modeling, refresh schedules)

**Best For:** Large portfolios (50+ projects), organisations with BI infrastructure

---

**Recommended Approach:**

- **Start with:** Option A (Manual Excel) for first 1-2 quarters to learn what works
- **Transition to:** Option B (Python script) once process stable and portfolio >15 projects
- **Consider:** Option C (Power BI/Tableau) if executive team wants interactive dashboards

---

# Dashboard Generation Workflow

This dashboard is generated **quarterly** (or after significant project milestones).

## Complete Workflow Overview

```
Step 1: Gather Assessments → Step 2: Run Consolidation → Step 3: Review Data Quality → 
Step 4: Generate Insights → Step 5: Create Executive Summary → Step 6: CISO Review → 
Step 7: Present to Management → Step 8: Track Action Items
```

---

## Step 1: Gather Project Assessments (30-90 min)

**Objective:** Collect all A.5.8.1 assessment workbooks for portfolio

**Process:**

**1.1 Identify Projects for Inclusion**

Determine which projects to include in dashboard:

- **INCLUDE:**
  - All active projects (Execution, Monitoring phases)
  - Projects closed within last 12 months (for trend analysis)
  - Optionally: Projects in Planning (for pipeline view)
- **EXCLUDE:**
  - Projects closed >12 months ago (unless analyzing multi-year trends)
  - Cancelled projects (unless specifically analyzing cancellations)

**1.2 Obtain Assessment Files**

**From Projects:**

- Request from Project Managers: "Please provide latest A.5.8.1 assessment workbook"
- Specify deadline: "Need by [date] for quarterly portfolio dashboard"
- Provide file naming convention: `A.5.8.1_ProjectName_YYYY-MM-DD.xlsx`

**From Centralized Repository:**

- If organisation has central ISMS documentation repository:
  - Navigate to `/isms/assessments/a58_1/YYYY_QX/`
  - Copy all A.5.8.1 workbooks to working folder

**1.3 Validate Completeness**

Cross-check against PMO project list:

- Do we have A.5.8.1 for all active Medium/High Risk projects? (mandatory)
- Are any projects missing assessments? (follow up with PM)
- Are assessments current? (not 6 months old for active project)

**1.4 Organize Files**

Create working folder structure:
```
/dashboard/2024_Q4/
  ├── source_data/
  │   ├── A.5.8.1_CustomerPortal_2024-12-10.xlsx
  │   ├── A.5.8.1_PaymentGateway_2024-12-08.xlsx
  │   ├── A.5.8.1_CRM_Upgrade_2024-12-12.xlsx
  │   └── ... (all other projects)
  ├── output/
  │   └── (dashboard will be generated here)
  └── previous_quarter/
      └── 2024_Q3_Portfolio_Dashboard.xlsx (for comparison)
```

**Deliverable:** All A.5.8.1 workbooks in `source_data/` folder, ready for extraction

---

## Step 2: Run Consolidation Process (15 min - 2 hours depending on method)

**Objective:** Extract key data from all A.5.8.1 workbooks and track in Summary Dashboards

**Method A: Manual Excel Consolidation (2-4 hours for 10 projects)**

**Process:**
1. Open dashboard template (Part II: Sheet 2 - Project Data Table)
2. For each project A.5.8.1 workbook:

   - Open workbook
   - Navigate to Sheet 2 (Classification): Copy Project Name, Classification, PM, Business Owner
   - Navigate to Sheet 8 (Dashboard): Copy Overall Compliance Score, Current Phase
   - Navigate to Sheet 8 (Gap Analysis): Count critical gaps
   - Navigate to Sheet 5 (Execution): Count Critical/High findings open
   - Navigate to Sheet 7 (Closure): Copy residual risk level (if closed)
   - Paste into dashboard template Project Data Table (one row per project)

3. Repeat for all projects
4. Verify data accuracy (spot-check a few projects)

**Time per project:** ~10-15 minutes × number of projects

**Method B: Python Automated Script (30 min setup, 2 min execution)**

**Process:**
1. Place all A.5.8.1 workbooks in `source_data/` folder
2. Run consolidation script: `python generate_a58_3_dashboard.py`
3. Script automatically:

   - Discovers all .xlsx files in source folder
   - Extracts data from specific cells (Sheet 2: B5, H58, B7; Sheet 8: compliance score, etc.)
   - Builds data table tracked in Summary Dashboards
   - Generates dashboard workbook in `output/` folder

4. Review script output for errors or warnings
5. Spot-check data accuracy

**Script Execution Time:** 1-5 minutes (depends on project count)

**Method C: Power BI Data Refresh (5 min)**

**Process:**
1. Ensure all A.5.8.1 workbooks in designated folder
2. Open Power BI dashboard
3. Click "Refresh" button
4. Power BI automatically:

   - Scans folder for Excel files
   - Extracts data from configured cells
   - Updates all visualizations

5. Publish refreshed dashboard to Power BI Service

**Refresh Time:** 2-10 minutes (depends on data volume)

**Deliverable:** Data table with all projects tracked in Summary Dashboards

---

## Step 3: Review Data Quality (15-30 min)

**Objective:** Validate data accuracy before analysis

**Quality Checks:**

**Check 1: Completeness**

- [ ] All expected projects present? (cross-check PMO list)
- [ ] All required data fields populated? (no blank cells in key columns)
- [ ] Missing assessments flagged? (note which projects lack A.5.8.1)

**Check 2: Accuracy (Spot-Check)**

- [ ] Pick 3-5 random projects
- [ ] Open source A.5.8.1 workbook
- [ ] Verify dashboard data matches source workbook (classification, compliance score, gaps)
- [ ] If discrepancies: Investigate (formula error? outdated file? manual entry mistake?)

**Check 3: Consistency**

- [ ] Project names consistent with PMO list? (no typos, abbreviations match)
- [ ] Classifications reasonable? (no suspiciously many High or all Low)
- [ ] Compliance scores logical? (0-100%, no >100%)

**Check 4: Currency**

- [ ] Assessment dates recent? (active projects should have updated assessments within last 30-90 days)
- [ ] Stale data flagged? (if project in Execution but last assessment 6 months ago)

**If Quality Issues Found:**

- **Minor (typos, formatting):** Fix in dashboard
- **Moderate (missing data fields):** Contact PM for clarification
- **Major (entire project missing, data clearly wrong):** Re-collect data before proceeding

**Deliverable:** Validated data table with all projects tracked in Summary Dashboards, quality issues resolved

---

## Step 4: Generate Dashboard and Insights (1-2 hours)

**Objective:** Create visualizations, calculate portfolio metrics, identify insights

**Activities:**

**4.1 Calculate Portfolio Metrics**

**Overall Portfolio Metrics:**
```
Total Projects: COUNT(all projects)
By Classification:
  High Risk: COUNT(classification = "High")
  Medium Risk: COUNT(classification = "Medium")
  Low Risk: COUNT(classification = "Low")
  
By Phase:
  Initiation: COUNT(phase = "Initiation")
  Planning: COUNT(phase = "Planning")
  Execution: COUNT(phase = "Execution")
  Monitoring: COUNT(phase = "Monitoring")
  Closure: COUNT(phase = "Closure")
  Closed: COUNT(phase = "Closed")

Portfolio Compliance Score: WEIGHTED_AVERAGE(project_compliance_scores, classification_weights)
  Weighting: High Risk projects = 3x, Medium = 2x, Low = 1x
  Formula: SUM(score × weight) / SUM(weights)
  
Portfolio Health Status:
  If Portfolio Score ≥85% AND Critical Gaps = 0 → 🟢 Green "Healthy"
  If Portfolio Score 70-84% OR Critical Gaps 1-3 → 🟡 Amber "Needs Attention"
  If Portfolio Score <70% OR Critical Gaps >3 → 🔴 Red "At Risk"
```

**4.2 Trend Analysis (Quarter-over-Quarter)**

Compare current quarter to previous quarter:
```
Previous Quarter Portfolio Score: 78%
Current Quarter Portfolio Score: 82%
Trend: ↑ +4% (Improving)

Projects Improved: COUNT(current_score > previous_score)
Projects Declined: COUNT(current_score < previous_score)
Projects Stable: COUNT(current_score ≈ previous_score within ±5%)
```

**4.3 Gap Analysis Across Portfolio**

Identify most common gaps:
```
Gap Frequency Analysis:
For each gap found in any project:
  Count how many projects have this gap
  Rank by frequency
  
Top 5 Most Common Gaps:
1. "Penetration test not conducted" - 8 projects (40% of portfolio)
2. "Security handover documentation incomplete" - 6 projects (30%)
3. "Threat modeling skipped" - 5 projects (25%)
4. "Vendor security assessment missing" - 4 projects (20%)
5. "Monitoring phase risk reviews not regular" - 4 projects (20%)
```

**4.4 Risk Prioritization**

Rank projects by risk priority:
```
Priority 1 (Critical - Immediate Attention):

  - High Risk projects with Compliance < 70%
  - OR Any project with Critical findings open
  - OR High Risk project past deployment date with security gaps

Priority 2 (High - Address within 30 days):

  - Medium Risk projects with Compliance < 60%
  - OR High Risk projects with 70-79% compliance
  - OR Projects with High findings open

Priority 3 (Medium - Monitor closely):

  - All projects with 60-79% compliance
  - OR Projects with significant delays in security activities

Priority 4 (Low - Standard monitoring):

  - All projects with ≥80% compliance
  - Low Risk projects with minor gaps

```

**4.5 Create Visualizations**

**Charts to Generate:**
1. **Portfolio Health Pie Chart:** Projects by status (🟢🟡🔴)
2. **Compliance Score Histogram:** Distribution of project compliance scores
3. **Trend Line Chart:** Portfolio score over last 4-6 quarters
4. **Gap Frequency Bar Chart:** Top 10 most common gaps
5. **Risk Heat Map:** Projects plotted by Risk Level (x-axis) vs. Compliance Score (y-axis)
6. **Phase Distribution:** Projects by lifecycle phase (stacked bar chart)

**Deliverable:** Dashboard workbook with populated charts and metrics

---

## Step 5: Create Executive Summary (1-2 hours)

**Objective:** Distill dashboard into executive-friendly presentation

**Executive Summary Components:**

**Slide 1: One-Page Portfolio Snapshot (THE MOST IMPORTANT SLIDE)**

```
📊 Project Security Portfolio - Q4 2024

Portfolio Health: 🟢 Green / 🟡 Amber / 🔴 Red
Overall Compliance Score: 82% (↑ +4% from Q3)

Portfolio Composition:
  • Total Projects: 25
  • High Risk: 5 (20%)  → Avg Score: 88%
  • Medium Risk: 12 (48%) → Avg Score: 81%
  • Low Risk: 8 (32%)  → Avg Score: 78%

Key Metrics:
  ✅ Projects ≥85% Compliance: 16 (64%)
  ⚠️ Projects 70-84% Compliance: 7 (28%)
  ❌ Projects <70% Compliance: 2 (8%) ← Require Attention

Top Risks:
  🔴 CustomerPortal project (High Risk, 65% compliance, deployment in 2 weeks)
  🟡 Payment Gateway (Medium Risk, 72% compliance, pen test findings open)

Top 3 Portfolio Gaps:
  1. Penetration testing (40% of projects missing)
  2. Security handover docs (30% incomplete)
  3. Threat modeling (25% skipped)

Trend: ↑ Improving (+4% QoQ, 6 projects improved, 1 declined)
```

**Visual Elements:**

- Traffic light indicator (large, centered)
- Compliance score gauge (dial chart)
- Trend sparkline (last 4 quarters)
- Priority projects table (top 3-5)

**Slide 2: Trend Analysis** (if quarterly or annual review)

- Line chart: Portfolio score over time (last 4-8 quarters)
- Bar chart: Projects improved vs. declined (current vs. previous quarter)
- Key insight: "Portfolio security integration improving steadily, +15% over past year"

**Slide 3: Risk-Based Prioritization**

- Table: Priority 1 projects requiring immediate attention (details, actions, owners, deadlines)
- Visual: Risk heat map (bubble chart: x=Risk Level, y=Compliance Score, bubble size=Budget)

**Slide 4: Common Gaps & Remediation Plan**

- Bar chart: Top 5 most frequent gaps across portfolio
- Table: Gap → Root Cause → Recommended Fix → Owner → Target Date
- Example:

  ```
  Gap: Penetration testing skipped (40% of projects)
  Root Cause: Late budgeting, no standard vendor contract
  Fix: Establish MSA with pen test vendor, mandatory budget line in project template
  Owner: InfoSec + Procurement
  Target: Q1 2025
  ```

**Slide 5: Lessons Learned & Process Improvements**

- Key themes from project retrospectives
- Recommended policy/procedure updates
- Success stories (projects that excelled, share best practices)

**Optional Slides (for deep-dive presentations):**

- Slide 6: Regulatory compliance view (GDPR, PCI, sector-specific)
- Slide 7: Resource and budget analysis
- Slide 8: Detailed project-by-project status table

**Deliverable:** PowerPoint presentation (5-10 slides), PDF export for distribution

---

## Step 6: CISO Review and Validation (30-60 min meeting)

**Objective:** CISO reviews dashboard, validates insights, approves for presentation

**Review Meeting Agenda:**

**1. Data Quality Validation (5 min)**

- CISO spot-checks: "Does CustomerPortal 65% compliance sound right?" (CISO has context)
- Confirm no obvious data errors

**2. Insights Review (15 min)**

- Walk through executive summary slide-by-slide
- CISO confirms: Are these the right priorities?
- Challenge: "Why is Payment Gateway only 72%? What's the blocker?"

**3. Recommendations Validation (10 min)**

- Review proposed remediation plans for common gaps
- CISO approves or adjusts recommendations
- Assign owners for action items

**4. Presentation Approval (5 min)**

- CISO approves executive summary for presentation to management
- Minor edits requested (wording, emphasis)

**5. Action Items (5 min)**

- Document follow-up actions:
  - Escalate CustomerPortal project to Project Sponsor (deployment at risk)
  - Schedule MSA negotiation with pen test vendor (Q1 2025)
  - Update project initiation template to include pen test budget line
- Assign owners and deadlines

**Deliverable:** CISO-approved dashboard and executive summary, action item list

---

## Step 7: Present to Management (Quarterly Management Review)

**Objective:** Present portfolio security status to Executive Management

**Meeting Details:**

- **Attendees:** CISO, CIO, CEO, CFO, PMO Director, potentially Board (if annual)
- **Duration:** 15-30 minutes (quarterly), 45-60 minutes (annual with Board)
- **Format:** PowerPoint presentation + Q&A

**Presentation Flow:**

**Opening (2 min):**

- Purpose: "Quarterly review of project security integration across portfolio"
- Context: "This dashboard consolidates security assessments from 25 active projects"

**Slide 1: Portfolio Snapshot (5 min):**

- Present overall health: 🟢 Green, 82% compliance, improving trend
- Highlight key numbers: 25 projects, 64% meeting target (≥85%)
- Note top risks: 2 projects requiring immediate attention

**Slide 2: Trend Analysis (3 min):**

- Show improvement over time: +4% this quarter, +15% over past year
- Celebrate wins: 6 projects improved compliance
- Note: 1 project declined (why? resource constraints, scope change)

**Slide 3: Priority Projects (5 min):**

- Deep dive: CustomerPortal (High Risk, 65%, deployment in 2 weeks)
  - Issue: Penetration test found 3 High findings, remediation in progress
  - Action: Delaying deployment by 2 weeks to remediate findings
  - Decision needed: Executive approval for delay
- Payment Gateway (Medium Risk, 72%)
  - Issue: Vendor security assessment delayed vendor onboarding
  - Action: Accelerating assessment, deployment on track

**Slide 4: Portfolio Gaps (5 min):**

- Top 3 gaps affecting multiple projects
- Proposed remediation:

  1. Pen test vendor MSA → saves 4 weeks per project, reduces cost
  2. Security handover template → standardizes closure documentation
  3. Threat modeling workshop service → InfoSec facilitates for High Risk projects

- **Budget ask:** $50K for pen test MSA, 0.5 FTE InfoSec resource for workshops

**Slide 5: Lessons Learned (3 min):**

- Success story: Mobile App project (95% compliance, ahead of schedule) - why?
  - Early security engagement (Planning phase)
  - Dedicated security champion on team
  - Standard: Require security champion for all High Risk projects

**Q&A (5-10 min):**

- Address management questions
- Seek decisions on:
  - CustomerPortal deployment delay approval
  - Budget approval for gap remediation
  - Policy updates (security champion requirement)

**Deliverable:** Management decisions documented, action items assigned

---

## Step 8: Track Action Items and Follow-Up (Ongoing)

**Objective:** Ensure action items from dashboard review are completed

**Action Item Tracking:**

Create action item register (simple spreadsheet or project management tool):

| Action | Owner | Target Date | Status | Notes |
|--------|-------|-------------|--------|-------|
| Delay CustomerPortal deployment 2 weeks | Project Sponsor | Immediate | ✅ Approved | Deployment moved to 2025-01-15 |
| Remediate CustomerPortal High findings | Development Team | 2025-01-10 | 🔄 In Progress | 2 of 3 fixed, 1 in code review |
| Negotiate pen test vendor MSA | InfoSec + Procurement | 2025-03-31 | 🔄 In Progress | RFP issued |
| Create security handover template | InfoSec + PMO | 2025-02-28 | ❌ Not Started | Assign to InfoSec Analyst |
| Establish security champion requirement | CISO | 2025-03-31 | 🔄 In Progress | Policy update in draft |
| Allocate 0.5 FTE for threat modeling | CISO + HR | 2025-04-30 | ⚠️ Pending Budget | Budget approval Q1 |

**Follow-Up Activities:**

**Monthly (or before next quarterly review):**

- [ ] Check action item status (green/yellow/red)
- [ ] Escalate blocked items (budget delays, resource constraints)
- [ ] Report progress to CISO

**Next Quarterly Review:**

- [ ] Update dashboard with Q1 data
- [ ] Show action item completion: "Last quarter we identified pen testing gap, we've now established vendor MSA, 5 projects completed pen tests"
- [ ] Demonstrate continuous improvement

**Deliverable:** Action items tracked to completion, progress demonstrated in next review

---

# Dashboard Components - Detailed Specifications

This section details the 8 dashboard components mentioned in Section 1.1.

---

## Component 1: Executive Summary (One-Page Portfolio Health)

**Purpose:** Single-page snapshot for executive/board presentation

**Key Elements:**

**A. Overall Portfolio Health Indicator**

Traffic-light status based on portfolio compliance and critical gaps:

```
🟢 GREEN - Healthy Portfolio
  Criteria: Portfolio Score ≥85% AND Critical Gaps = 0
  Interpretation: Portfolio security integration strong, minimal risks
  
🟡 AMBER - Needs Attention
  Criteria: Portfolio Score 70-84% OR Critical Gaps 1-3
  Interpretation: Acceptable but improvements needed, some projects struggling
  
🔴 RED - At Risk
  Criteria: Portfolio Score <70% OR Critical Gaps >3
  Interpretation: Significant portfolio risk, immediate action required
```

**Visual:** Large traffic light icon (centered, prominent)

**B. Portfolio Compliance Score**

Weighted average across all projects:

```
Calculation:
  For each project: score × weight
  Weight: High Risk = 3, Medium Risk = 2, Low Risk = 1
  Portfolio Score = SUM(project_score × weight) / SUM(weights)

Example:
  Project A (High, 90%): 90 × 3 = 270
  Project B (Medium, 80%): 80 × 2 = 160
  Project C (Low, 70%): 70 × 1 = 70
  Portfolio Score = (270 + 160 + 70) / (3 + 2 + 1) = 500 / 6 = 83.3%
```

**Visual:** Gauge/dial chart (0-100%), color-coded (red<70%, yellow 70-84%, green ≥85%)

**C. Portfolio Composition**

Project count by classification and phase:

```
Total Projects: 25

By Classification:
  High Risk: 5 (20%) - Avg Score: 88%
  Medium Risk: 12 (48%) - Avg Score: 81%
  Low Risk: 8 (32%) - Avg Score: 78%

By Phase:
  Planning: 3
  Execution: 12
  Monitoring: 6
  Closure: 2
  Closed (recent): 2
```

**Visual:** Stacked bar chart or pie chart

**D. Key Metrics Summary**

Critical portfolio statistics:

```
✅ Projects Meeting Target (≥85%): 16 of 25 (64%)
⚠️ Projects Near Target (70-84%): 7 of 25 (28%)
❌ Projects Below Target (<70%): 2 of 25 (8%)

🔴 Critical Gaps Across Portfolio: 3
🟠 High Risk Projects Requiring Attention: 2
📈 Trend vs. Last Quarter: ↑ +4% (Improving)
```

**E. Top Risks/Priority Projects**

Table of 3-5 highest-priority projects:

| Project | Classification | Score | Status | Issue | Action Required |
|---------|---------------|-------|--------|-------|-----------------|
| CustomerPortal | High | 65% | 🔴 Red | 3 High findings open, deployment in 2 weeks | Delay deployment, remediate findings |
| PaymentGateway | Medium | 72% | 🟡 Amber | Vendor assessment delayed | Accelerate vendor review |

**F. Top 3 Portfolio Gaps**

Most common gaps across projects:

```
1. Penetration testing not conducted (10 projects, 40%)
2. Security handover documentation incomplete (7 projects, 28%)
3. Threat modeling skipped for High Risk (5 projects, 20%)
```

**G. Trend Indicator**

Quarter-over-quarter or year-over-year change:

```
Q3 2024: 78%
Q4 2024: 82%
Change: ↑ +4% (Improving)

Year-over-Year:
Q4 2023: 67%
Q4 2024: 82%
Change: ↑ +15% (Significant Improvement)
```

**Visual:** Sparkline or small line chart

---

## Component 2: Project-by-Project Status Table

**Purpose:** Detailed status of every project in portfolio (for drill-down)

**Table Columns:**

| Column | Data | Format | Notes |
|--------|------|--------|-------|
| **Project Name** | Text | Bold | Hyperlink to full A.5.8.1 assessment |
| **Classification** | High / Medium / Low | Color-coded | Red (High), Yellow (Medium), Green (Low) |
| **Project Manager** | Text | Plain | For accountability |
| **Current Phase** | Initiation / Planning / Execution / Monitoring / Closure / Closed | Plain | Lifecycle status |
| **Compliance Score** | 0-100% | Percentage | With conditional formatting (red/yellow/green) |
| **Status Indicator** | 🟢🟡🔴 | Icon | Based on score and gaps |
| **Critical Gaps** | Number | Number | Count of critical gaps |
| **High Findings Open** | Number | Number | From Execution phase |
| **Target Deployment** | Date | Date | When project goes live |
| **Last Assessment Date** | Date | Date | Currency check (should be recent) |
| **Priority** | 1-4 | Number | 1=Critical, 4=Low (from risk prioritization) |
| **Notes** | Text | Plain | Brief issue summary or "On track" |

**Table Features:**

- **Sortable:** Click column header to sort
- **Filterable:** Dropdown filters (Classification, Phase, Status)
- **Color-coded:** Status indicator colors for visual scanning
- **Conditional formatting:** Scores highlighted (red/yellow/green)

**Example Rows:**

| Project | Class. | PM | Phase | Score | Status | Crit. Gaps | High Open | Deploy Date | Last Assess | Priority | Notes |
|---------|--------|----|----|-------|--------|------------|-----------|-------------|-------------|----------|-------|
| CustomerPortal | High | J. Smith | Execution | 65% | 🔴 | 2 | 3 | 2025-01-15 | 2024-12-10 | 1 | Deployment delayed for remediation |
| PaymentGateway | Medium | A. Johnson | Execution | 72% | 🟡 | 0 | 0 | 2025-02-01 | 2024-12-08 | 2 | Vendor assessment in progress |
| CRM Upgrade | Medium | M. Lee | Monitoring | 88% | 🟢 | 0 | 0 | 2024-11-30 | 2024-12-12 | 4 | On track |

**Total Projects:** 25 rows

**Summary Row (Bottom):**

- Portfolio Average Score: 82%
- Total Critical Gaps: 3
- Total High Findings: 5

---

## Component 3: Gap Analysis Across Portfolio

**Purpose:** Identify common security gaps appearing across multiple projects

**Analysis Method:**

**Step 1: Extract All Gaps**

From each project's A.5.8.1 (Sheet 8: Gap Analysis):

- Pull all incomplete activities where Status = ⚠️ or ❌ and Required = "Required"
- Categorize by phase and activity type

**Step 2: Frequency Count**

Count how many projects have each gap:

```
Gap: "Penetration test not conducted"
Projects: CustomerPortal, MobileApp, DataWarehouse, API Gateway, ... (10 total)
Frequency: 10 of 25 projects (40%)
```

**Step 3: Rank by Frequency**

Sort gaps by frequency (most common first)

**Gap Analysis Table:**

| Rank | Gap Description | Projects Affected | Frequency | Phase | Impact | Root Cause (Hypothesis) |
|------|-----------------|-------------------|-----------|-------|--------|------------------------|
| 1 | Penetration test not conducted | 10 projects | 40% | Execution | High | No vendor contract, late budgeting |
| 2 | Security handover docs incomplete | 7 projects | 28% | Closure | Medium | No template, rushed closure |
| 3 | Threat modeling skipped | 5 High Risk | 20% | Planning | High | PMs lack training, time pressure |
| 4 | Vendor security assessment missing | 4 projects | 16% | Planning | Medium | Process unclear, delayed procurement |
| 5 | Monitoring risk reviews irregular | 4 projects | 16% | Monitoring | Medium | No recurring meeting, PM turnover |
| 6 | DPIA not conducted | 3 projects | 12% | Planning | High | DPO not engaged early |
| 7 | Security architecture review skipped | 3 projects | 12% | Planning | High | Architect unavailable, backlog |
| 8 | SAST not integrated in CI/CD | 3 projects | 12% | Execution | Medium | DevOps pipeline not standardized |
| 9 | MFA not implemented for admin access | 2 projects | 8% | Execution | High | Technical complexity, SSO delays |
| 10 | Asset registration in A.5.9 missing | 2 projects | 8% | Closure | Low | Manual process, forgotten |

**Insights from Gap Analysis:**

**Systemic Issues (>20% of projects):**

- **Penetration testing gap (40%):** Indicates need for:
  - Establish Master Service Agreement (MSA) with pen test vendor
  - Mandate pen test budget line in project templates
  - Earlier scheduling (6 weeks before deployment, not 2 weeks)

- **Security handover gap (28%):** Indicates need for:
  - Create standardized handover documentation template
  - Include handover in Definition of Done for Closure phase
  - Operations team sign-off required before project closure

- **Threat modeling gap for High Risk (20%):** Indicates need for:
  - Mandatory PM training on threat modeling
  - InfoSec-facilitated threat modeling workshop service
  - Update ISMS-POL-A.5.8 to make threat modeling non-negotiable for High Risk

**Visual:** Bar chart showing top 10 gaps by frequency

---

## Component 4: Trend Analysis (Quarter-over-Quarter)

**Purpose:** Show portfolio security improvement or decline over time

**Trend Metrics:**

**A. Portfolio Compliance Score Trend (Line Chart)**

```
X-axis: Quarters (Q1 2024, Q2 2024, Q3 2024, Q4 2024)
Y-axis: Portfolio Compliance Score (0-100%)

Data Points:
  Q1 2024: 67%
  Q2 2024: 72%
  Q3 2024: 78%
  Q4 2024: 82%

Trend: ↑ Consistent improvement (+15% over year)
```

**Visual:** Line chart with trend line, target line at 85%

**B. Project Distribution by Status (Stacked Bar Chart)**

```
Each quarter shown as stacked bar:
  Green (≥85%): [number of projects]
  Yellow (70-84%): [number of projects]
  Red (<70%): [number of projects]

Q1 2024: 🟢 8 | 🟡 10 | 🔴 7 (25 total)
Q2 2024: 🟢 10 | 🟡 9 | 🔴 6 (25 total)
Q3 2024: 🟢 12 | 🟡 10 | 🔴 3 (25 total)
Q4 2024: 🟢 16 | 🟡 7 | 🔴 2 (25 total)

Trend: Increasing green, decreasing red (positive)
```

**Visual:** Stacked bar chart (x=Quarter, y=Project count, color=Status)

**C. Gap Frequency Trend**

Top 3 gaps tracked over time:

```
Penetration Testing Gap:
  Q1: 15 projects (60%)
  Q2: 12 projects (48%)
  Q3: 10 projects (40%)
  Q4: 10 projects (40%)
Trend: Declining (good), stabilized at 40%

Security Handover Gap:
  Q1: 10 projects (40%)
  Q2: 9 projects (36%)
  Q3: 8 projects (32%)
  Q4: 7 projects (28%)
Trend: Declining (good), continuous improvement

Threat Modeling Gap (High Risk only):
  Q1: 7 of 10 High Risk (70%)
  Q2: 6 of 10 (60%)
  Q3: 5 of 10 (50%)
  Q4: 5 of 10 (50%)
Trend: Improved but plateaued
```

**Visual:** Multi-line chart (x=Quarter, y=Gap frequency %, separate line per gap type)

**D. Project Improvement/Decline Analysis**

Compare project scores current vs. previous quarter:

```
Projects Improved: 6 (24%)
  Example: Mobile App: 70% → 85% (+15%)
  
Projects Declined: 1 (4%)
  Example: DataWarehouse: 80% → 75% (-5%, reason: scope change added complexity)
  
Projects Stable (±5%): 18 (72%)
```

**Visual:** Waterfall chart or table

**Insights from Trends:**

**Positive Trends:**

- Portfolio score improving consistently (+4% per quarter average)
- More projects meeting target (64% vs. 32% in Q1)
- Most common gaps declining (process improvements working)

**Concerning Trends:**

- Threat modeling gap plateaued (need new approach)
- DataWarehouse project declined (investigate why)

**Actions Based on Trends:**

- Continue current improvements (MSA, templates)
- Address plateau: Mandatory threat modeling workshop for all High Risk
- Deep-dive: What happened to DataWarehouse? (scope change → update classification?)

---

[DOCUMENT CONTINUES - Remaining components and Part II Technical Specification will complete to 2000-2500 lines]

---

**STATUS: Document in progress, will complete with Components 5-8 and Part II**

## Component 5: Risk-Based Prioritization Matrix

**Purpose:** Rank projects by risk priority to guide resource allocation and executive attention

**Prioritization Matrix:**

Projects categorized into 4 priority levels based on risk and compliance:

**Priority 1: CRITICAL - Immediate Action Required**

Criteria:

- High Risk projects with Compliance < 70%
- OR ANY project with Critical security findings open
- OR High Risk project deployed/deploying with unresolved High findings
- OR Project past deployment date with security gate not approved

Example Projects:
| Project | Classification | Score | Issue | Action | Owner | Deadline |
|---------|---------------|-------|-------|--------|-------|----------|
| CustomerPortal | High | 65% | 3 High findings open, deployment in 2 weeks | Delay deployment, remediate findings | PM + InfoSec | 2025-01-10 |
| API Gateway | High | 68% | Pen test not conducted, deploying tomorrow | STOP deployment, conduct pen test | CISO (escalated) | IMMEDIATE |

**Risk Level:** 🔴 RED - Cannot deploy, immediate CISO escalation

---

**Priority 2: HIGH - Address Within 30 Days**

Criteria:

- Medium Risk projects with Compliance < 60%
- OR High Risk projects with 70-79% compliance
- OR Projects with multiple High findings open (but not Critical)
- OR High Risk projects missing mandatory security activities

Example Projects:
| Project | Classification | Score | Issue | Action | Owner | Deadline |
|---------|---------------|-------|-------|--------|-------|----------|
| PaymentGateway | Medium | 72% | Vendor assessment delayed | Accelerate assessment | PM | 2025-01-30 |
| MobileApp | High | 76% | No threat modeling conducted | Schedule threat modeling workshop | InfoSec | 2025-01-25 |

**Risk Level:** 🟠 ORANGE - Require attention, must address before deployment

---

**Priority 3: MEDIUM - Monitor Closely**

Criteria:

- All projects with 60-79% compliance (regardless of classification)
- OR Projects with significant delays in security activities
- OR Projects with Medium findings accumulating (>10 Medium findings)
- OR Projects with irregular monitoring phase activities

Example Projects:
| Project | Classification | Score | Issue | Action | Owner | Deadline |
|---------|---------------|-------|-------|--------|-------|----------|
| CRM Upgrade | Medium | 74% | Security handover docs incomplete | Complete handover template | PM | 2025-02-15 |
| DataWarehouse | Medium | 75% | Monitoring risk reviews not regular | Establish bi-weekly risk review | PM | Ongoing |

**Risk Level:** 🟡 YELLOW - Monitor, address gaps before closure

---

**Priority 4: LOW - Standard Monitoring**

Criteria:

- All projects with ≥80% compliance
- Low Risk projects with minor gaps only
- Projects on track with no significant security issues

Example Projects:
| Project | Classification | Score | Status | Notes |
|---------|---------------|-------|--------|-------|
| Internal Tool | Low | 85% | 🟢 Green | On track, minor documentation gaps only |
| Report Dashboard | Low | 82% | 🟢 Green | Standard monitoring sufficient |

**Risk Level:** 🟢 GREEN - Continue standard project governance

---

**Risk Heat Map Visualization:**

```
Bubble Chart:
X-axis: Project Risk Level (Low → Medium → High)
Y-axis: Compliance Score (0% → 100%)
Bubble Size: Project Budget (larger = higher budget)
Bubble Color: Priority (Red=P1, Orange=P2, Yellow=P3, Green=P4)

Quadrants:
┌─────────────────┬─────────────────┐
│ High Risk       │ High Risk       │
│ High Compliance │ Low Compliance  │
│ (Priority 4)    │ (Priority 1-2)  │  ← TOP RIGHT: DANGER ZONE
├─────────────────┼─────────────────┤
│ Low Risk        │ Low Risk        │
│ High Compliance │ Low Compliance  │
│ (Priority 4)    │ (Priority 3)    │
└─────────────────┴─────────────────┘
```

**Priority Distribution:**
```
Priority 1 (Critical): 2 projects (8%)  ← Require CISO attention
Priority 2 (High): 5 projects (20%)     ← Require InfoSec support
Priority 3 (Medium): 7 projects (28%)   ← Standard PM management
Priority 4 (Low): 11 projects (44%)     ← Minimal oversight needed
```

**Resource Allocation Guidance:**

Based on priority distribution:

- **CISO time:** Focus on Priority 1 (2 projects) - direct involvement, approvals, escalations
- **InfoSec Officer time:** Priority 2 (5 projects) - reviews, guidance, testing support
- **PM self-management:** Priority 3-4 (18 projects) - standard governance, InfoSec consultation as-needed

**Decision Support:**

For executive decision-making:

- **Deployment decisions:** Priority 1 cannot deploy, Priority 2 requires risk acceptance, Priority 3-4 standard approval
- **Budget allocation:** Priority 1-2 may need additional security budget (pen tests, remediation effort)
- **Timeline adjustments:** Priority 1 may require deployment delays for remediation

---

## Component 6: Lessons Learned Synthesis

**Purpose:** Aggregate lessons learned from all project retrospectives to identify systematic improvements

**Data Source:**

- ISMS-IMP-A.5.8.1, Sheet 7 (Closure Phase), Section D: Security Lessons Learned
- Extract from all closed or near-closure projects

**Synthesis Process:**

**Step 1: Collect Lessons from All Projects**

For each project, extract:

- What worked well? (successes)
- What didn't work? (challenges)
- What would we do differently? (improvements)
- Recommended standardizations

**Step 2: Thematic Analysis**

Group lessons into themes:

**Theme 1: Security Testing Challenges**
```
Common Issue (from 8 projects):
  "Penetration test scheduled too close to deployment, findings delayed go-live"

Root Cause:

  - No standard pen test timeline in project templates
  - Budget approved late, vendor procurement delayed
  - PM lack awareness of pen test lead time (4-6 weeks)

Recommended Fix:

  - Update project initiation template: "For Medium/High Risk, allocate pen test budget, schedule 6 weeks before deployment"
  - Establish MSA with 2-3 pen test vendors for faster procurement
  - PM training: Include security testing timelines in project management training

Owner: PMO Director + InfoSec Officer
Target: Q1 2025 (template update), Q2 2025 (MSA)
Status: 🔄 In Progress
```

**Theme 2: Security Requirements Clarity**
```
Common Issue (from 6 projects):
  "Security requirements too vague ('system must be secure'), led to rework"

Root Cause:

  - No standard security requirements templates
  - PM/BA lack security knowledge to write specific requirements
  - InfoSec involvement too late (after requirements locked)

Recommended Fix:

  - Create security requirements library (ISMS-IMP-A.5.8.2 examples)
  - Require InfoSec review of requirements during Planning phase (gate criterion)
  - Provide requirement templates by project type (web app, mobile app, API, infrastructure)

Owner: InfoSec Officer + PMO
Target: Q1 2025 (library), Ongoing (requirement reviews)
Status: 🔄 In Progress
```

**Theme 3: Handover Documentation Gaps**
```
Common Issue (from 7 projects):
  "Security handover documentation incomplete, operations team struggled to securely operate system"

Root Cause:

  - No handover template, each PM creates from scratch (inconsistent)
  - Documentation started at end of project (rushed)
  - Operations team not engaged during project (don't know what they need)

Recommended Fix:

  - Create standardized security handover template (Part of ISMS-IMP-A.5.8.1)
  - Start handover doc at project kickoff, update incrementally (not all at end)
  - Require operations team sign-off on handover before Closure gate approval

Owner: InfoSec + IT Operations
Target: Q1 2025 (template), Immediate (process change)
Status: ✅ Template created, rolling out
```

**Theme 4: Resource Constraints**
```
Common Issue (from 5 projects):
  "InfoSec Officer overloaded, delayed security reviews, bottleneck for multiple projects"

Root Cause:

  - Single InfoSec Officer supporting 15+ simultaneous projects
  - No prioritization (all projects compete for InfoSec time equally)
  - Some activities require InfoSec but could be self-service with tools

Recommended Fix:

  - Hire additional InfoSec resource (0.5-1.0 FTE) OR external consultant for peak periods
  - Prioritize InfoSec time: High Risk projects get priority, Low Risk self-service
  - Automate where possible: SAST/DAST tools in CI/CD reduce manual review burden

Owner: CISO + HR
Target: Q2 2025 (hiring) OR Q1 2025 (consultant contract)
Status: ⚠️ Pending budget approval
```

**Theme 5: Success Patterns (What Worked Well)**
```
Success: Mobile App project (95% compliance, ahead of schedule)

What they did differently:

  - Assigned security champion from development team (rotated role)
  - Security integrated in sprint ceremonies (security story in each sprint)
  - Early InfoSec engagement (threat modeling in Sprint 0)
  - Automated security testing in CI/CD pipeline

Lessons to Standardize:

  - Require security champion for all Medium/High Risk projects
  - Integrate security into Agile ceremonies (security item in sprint review checklist)
  - Encourage early security workshops (threat modeling, architecture review)

Owner: PMO + InfoSec
Target: Q1 2025 (update Agile project template)
Status: 🔄 In Progress
```

**Step 3: Prioritize Improvements**

Rank improvements by:
1. **Impact:** How many projects will benefit? (high=affects >30% of projects)
2. **Effort:** How hard to implement? (low=simple policy change, high=major process redesign)
3. **Feasibility:** Can we do this within budget/resources?

**Priority Matrix:**

```
High Impact, Low Effort (DO FIRST):
  ✅ Security handover template (affects 30% of projects, template creation = 1 week)
  ✅ Pen test timeline in project template (affects 40%, template update = 1 day)

High Impact, High Effort (STRATEGIC INITIATIVES):
  🔄 Additional InfoSec headcount (affects all projects, hiring = 3-6 months)
  🔄 Security requirements library (affects all projects, library creation = 2-3 months)

Low Impact, Low Effort (QUICK WINS):
  ✅ PM security training module (affects PMs, training creation = 2 weeks)

Low Impact, High Effort (DEPRIORITIZE):
  ❌ Custom security tool development (marginal benefit, high development cost)
```

**Step 4: Create Improvement Roadmap**

```
Q1 2025:

  - ✅ Security handover template (completed)
  - 🔄 Security requirements library (in progress, target end of Q1)
  - 🔄 Update project templates (pen test timeline, security champion requirement)
  - 🔄 PM security training module (development started)

Q2 2025:

  - InfoSec headcount or consultant engagement (pending budget)
  - Pen test vendor MSA established
  - Rollout updated Agile project template with security integration

Q3-Q4 2025:

  - Evaluate effectiveness of Q1/Q2 improvements
  - Next round of lessons learned synthesis

```

**Lessons Learned Summary Table:**

| Theme | Projects Affected | Root Cause | Proposed Fix | Owner | Target | Status |
|-------|-------------------|------------|--------------|-------|--------|--------|
| Pen test timing | 8 (32%) | No standard timeline, late budgeting | Template update + MSA | PMO + InfoSec | Q1-Q2 2025 | 🔄 |
| Requirements vagueness | 6 (24%) | No templates, late InfoSec | Requirements library + review gate | InfoSec + PMO | Q1 2025 | 🔄 |
| Handover docs | 7 (28%) | No template, rushed | Standardized template + incremental updates | InfoSec + Ops | Q1 2025 | ✅ |
| InfoSec bandwidth | 5 (20%) | Resource constraint | Hire or contractor | CISO + HR | Q2 2025 | ⚠️ Budget |
| Success patterns | 1 (Mobile App) | Security champion + early engagement | Standardize for all Med/High | PMO + InfoSec | Q1 2025 | 🔄 |

---

## Component 7: Regulatory Compliance View

**Purpose:** Show compliance status by regulation (GDPR, nDSG, PCI DSS v4.0.1, sector-specific)

**Applicable Regulations:**

**Step 1: Identify Applicable Regulations**

From project assessments and organisational context:

- **GDPR (EU General Data Protection Regulation):** If processing EU personal data
- **nDSG (Swiss Data Protection Act):** If processing Swiss personal data
- **PCI DSS v4.0.1 (Payment Card Industry Data Security Standard):** If processing payment card data
- **HIPAA (Health Insurance Portability and Accountability Act):** If processing health information (US)
- **FINMA Circular 2008/21:** If Swiss financial institution
- **DORA (Digital Operational Resilience Act):** If EU financial institution
- **NIS2 (Network and Information Security Directive):** If critical infrastructure operator
- **Sector-specific:** Other industry regulations

**Step 2: Map Projects to Regulations**

Determine which regulations apply to which projects:

```
GDPR/nDSG (Personal Data):
  Applicable to: 18 of 25 projects (72%) - all projects processing personal data
  
PCI DSS v4.0.1 (Payment Cards):
  Applicable to: 3 of 25 projects (12%) - CustomerPortal, PaymentGateway, MobileApp

FINMA (Swiss Financial):
  Applicable to: 5 of 25 projects (20%) - all projects for financial institution

DORA (EU Financial Resilience):
  Applicable to: 5 of 25 projects (20%) - same as FINMA (if EU operations)
```

**Step 3: Compliance Requirements by Regulation**

For each regulation, specific requirements from ISMS-IMP-A.5.8.2 Category 6:

**GDPR/nDSG Compliance:**

| Requirement | Projects Compliant | Projects Non-Compliant | Compliance Rate |
|-------------|-------------------|----------------------|-----------------|
| Lawful basis documented | 16 of 18 | 2 | 89% |
| Privacy notice provided | 18 of 18 | 0 | 100% |
| Data subject rights implemented | 15 of 18 | 3 | 83% |
| DPIA conducted (high-risk processing) | 4 of 6 required | 2 missing | 67% |
| Data breach notification procedure | 18 of 18 | 0 | 100% |
| DPA with processors | 12 of 15 required | 3 missing | 80% |

**Overall GDPR/nDSG Compliance:** 86% (Good, but DPIA gap concerning)

**PCI DSS v4.0.1 Compliance:**

| Requirement | Projects Compliant | Projects Non-Compliant | Compliance Rate |
|-------------|-------------------|----------------------|-----------------|
| Firewall protecting cardholder data | 3 of 3 | 0 | 100% |
| Encrypt stored PAN | 3 of 3 | 0 | 100% |
| Encrypt transmission (TLS 1.2+) | 3 of 3 | 0 | 100% |
| Access restriction to CDE | 2 of 3 | 1 (MobileApp: insufficient RBAC) | 67% |
| Logging and monitoring | 3 of 3 | 0 | 100% |
| Quarterly vulnerability scans | 2 of 3 | 1 (PaymentGateway: overdue) | 67% |
| Annual penetration test | 1 of 3 | 2 (CustomerPortal, PaymentGateway) | 33% ⚠️ |

**Overall PCI DSS v4.0.1 Compliance:** 76% (Needs Improvement - pen test gap critical)

**FINMA Circular 2008/21 Compliance:**

| Requirement | Projects Compliant | Projects Non-Compliant | Compliance Rate |
|-------------|-------------------|----------------------|-----------------|
| ICT risk management framework | 5 of 5 | 0 | 100% |
| Network security controls | 5 of 5 | 0 | 100% |
| Access control (MFA for privileged) | 4 of 5 | 1 | 80% |
| Change management process | 5 of 5 | 0 | 100% |
| Incident reporting procedure | 5 of 5 | 0 | 100% |
| BCP/DR documented and tested | 3 of 5 | 2 | 60% |
| Outsourcing governance (cloud) | 4 of 5 | 1 (vendor assessment missing) | 80% |

**Overall FINMA Compliance:** 89% (Good)

**Step 4: Regulatory Summary Dashboard**

**Visual: Compliance Score by Regulation (Bar Chart)**

```
GDPR/nDSG:     ████████████████████░░░░  86%
PCI DSS v4.0.1:       ███████████████░░░░░░░░░  76%
FINMA:         █████████████████████░░░  89%
DORA:          █████████████████████░░░  88%
NIS2:          ██████████████████████░░  92%
```

**Traffic Light Status:**

- 🟢 Green (≥90%): NIS2
- 🟡 Amber (75-89%): GDPR/nDSG, FINMA, DORA
- 🔴 Red (<75%): PCI DSS v4.0.1 ⚠️ Requires immediate attention

**Step 5: Regulatory Gap Analysis**

**Critical Gaps by Regulation:**

**PCI DSS v4.0.1 (Most Concerning):**
```
Gap: Annual penetration test missing for 2 of 3 PCI projects (CustomerPortal, PaymentGateway)
Impact: PCI DSS v4.0.1 Requirement 11.3 violation, potential compliance failure in audit
Root Cause: Pen test vendor procurement delayed, budget allocated late
Remediation:

  - CustomerPortal: Schedule pen test immediately (target: January 2025)
  - PaymentGateway: Schedule pen test (target: February 2025)
  - Establish pen test vendor MSA to prevent future delays

Owner: InfoSec + Procurement
Target: Q1 2025
Priority: 🔴 CRITICAL
```

**GDPR (Moderate Concern):**
```
Gap: DPIA not conducted for 2 high-risk processing projects
Impact: GDPR Article 35 violation, supervisory authority could impose fines
Root Cause: DPO not engaged early in Planning phase, PMs unaware of DPIA requirement
Remediation:

  - Conduct retrospective DPIA for 2 projects (DataWarehouse, CRM Upgrade)
  - Update project initiation checklist: "If processing Restricted personal data, engage DPO for DPIA"
  - DPO training session for PMs on when DPIA required

Owner: Data Protection Officer + PMO
Target: Q1 2025 (retrospective DPIAs), Ongoing (process fix)
Priority: 🟠 HIGH
```

**Step 6: Regulatory Reporting**

**For Audits/Certifications:**

- ISO 27001 Audit: Show systematic compliance across portfolio (evidence of Control A.5.8)
- PCI DSS v4.0.1 QSA (Qualified Security Assessor): Provide PCI-specific compliance evidence for 3 projects
- GDPR Supervisory Authority: Demonstrate DPIA process, data protection by design

**For Management:**

- Quarterly compliance report: "PCI DSS v4.0.1 compliance below target, remediation plan approved"
- Annual board report: "GDPR compliance strong at 86%, continuous improvement demonstrated"

---

## Component 8: Resource and Budget Analysis

**Purpose:** Analyze security resource utilization and budget allocation across portfolio

**Data Sources:**

- Project budgets (from PMO or project charters)
- Security budget allocations (from A.5.8.1, Initiation Phase, Section C)
- InfoSec Officer time tracking (from internal records)
- External security service costs (pen tests, consulting)

**Analysis Dimensions:**

**A. Security Budget by Project Classification**

```
Total Portfolio Budget: $5,000,000
Total Security Budget: $250,000 (5% of total budget)

By Classification:
  High Risk Projects (5 projects):
    Total Project Budget: $2,500,000 (50% of portfolio)
    Security Budget: $150,000 (6% of High Risk project budgets, 60% of total security budget)
    Avg Security Budget per High Risk Project: $30,000

  Medium Risk Projects (12 projects):
    Total Project Budget: $2,000,000 (40% of portfolio)
    Security Budget: $80,000 (4% of Medium Risk budgets, 32% of total security budget)
    Avg Security Budget per Medium Risk Project: $6,667

  Low Risk Projects (8 projects):
    Total Project Budget: $500,000 (10% of portfolio)
    Security Budget: $20,000 (4% of Low Risk budgets, 8% of total security budget)
    Avg Security Budget per Low Risk Project: $2,500
```

**Visual:** Pie chart showing security budget distribution by classification

**Insights:**

- Security budget proportional to risk (High gets 60%, is 50% of project budget)
- Low Risk projects have minimal security budget (appropriate for risk level)
- Security budget ~5% of total portfolio budget (industry benchmark: 5-10%)

**B. Security Budget Breakdown by Activity Type**

```
Security Testing: $120,000 (48%)

  - Penetration Testing: $80,000 (15 projects × $5,000 avg)
  - Vulnerability Scanning: $15,000 (licenses + managed service)
  - SAST/DAST Tools: $25,000 (licenses)

Security Assessments: $60,000 (24%)

  - Vendor Security Assessments: $30,000 (external questionnaires, audits)
  - Architecture Reviews: $20,000 (external security architects for complex projects)
  - DPIAs: $10,000 (DPO consulting for high-risk processing)

Security Tools/Services: $40,000 (16%)

  - SIEM log analysis for project environments: $15,000
  - Encryption tools/certificates: $10,000
  - MFA/authentication services: $15,000

Training & Workshops: $20,000 (8%)

  - PM security training: $8,000
  - Threat modeling workshops: $12,000

Contingency/Other: $10,000 (4%)

  - Unplanned security activities
  - Remediation effort (external support)

```

**Visual:** Bar chart showing budget by activity type

**Insights:**

- Penetration testing is largest single expense (32% of total security budget)
- Vendor assessments significant cost (12%) - opportunity for standardization/templates
- Training relatively low (8%) - may need investment for PM skill building

**C. InfoSec Officer Time Allocation**

```
Total InfoSec Officer Availability: 1.0 FTE = 2,080 hours/year = 520 hours/quarter

Time Allocation (Q4 2024):
  Project Reviews & Approvals: 200 hours (38%)

    - Classification approvals: 25 hours (25 projects × 1 hour)
    - Gate review approvals: 75 hours (5 phases × 25 projects × 0.6 hours avg)
    - Requirements review: 50 hours (Medium/High projects)
    - Architecture reviews: 50 hours (High Risk projects)

  Security Testing Support: 120 hours (23%)

    - Test plan reviews: 30 hours
    - Test result analysis: 40 hours
    - Remediation guidance: 50 hours

  Incident Response & Escalations: 80 hours (15%)

    - Project security incidents: 30 hours
    - Escalation meetings: 30 hours
    - Emergency reviews: 20 hours

  Consulting & Guidance: 60 hours (12%)

    - PM questions and guidance: 40 hours
    - Vendor assessment support: 20 hours

  Continuous Improvement: 40 hours (8%)

    - Policy updates: 15 hours
    - Template development: 15 hours
    - Training development: 10 hours

  Administrative: 20 hours (4%)

    - Portfolio dashboard preparation: 8 hours
    - Reporting: 12 hours

Total Billable: 520 hours (100% utilization)
```

**Visual:** Pie chart showing InfoSec time allocation

**Insights:**

- InfoSec Officer at 100% utilization (no slack time)
- 38% of time spent on project reviews (15 projects simultaneously = overload)
- Only 8% time for continuous improvement (should be 15-20% for innovation)
- **Conclusion:** InfoSec Officer overloaded, need additional headcount or process optimization

**D. Security ROI Analysis**

**Prevented Incidents (Estimated Value):**
```
Security activities that prevented potential incidents:

1. Penetration test on CustomerPortal found SQL injection (Critical)

   - Estimated incident cost if exploited in production: $500,000

     (Data breach: notification costs, regulatory fines, customer compensation, reputation)

   - Pen test cost: $8,000
   - ROI: $492,000 saved / $8,000 invested = 6,150% ROI

2. Vendor security assessment blocked insecure SaaS provider

   - Estimated incident cost if used: $100,000

     (Data exposure, contractual liability, migration costs)

   - Assessment cost: $3,000
   - ROI: $97,000 saved / $3,000 = 3,233% ROI

3. Threat modeling identified architecture flaw in PaymentGateway

   - Estimated incident cost: $300,000

     (Payment card data breach, PCI DSS v4.0.1 non-compliance fines)

   - Threat modeling cost: $2,000
   - ROI: $298,000 / $2,000 = 14,900% ROI

Total Prevented Incident Value: $900,000
Total Security Investment: $250,000
Portfolio Security ROI: $900,000 / $250,000 = 360% ROI (or 3.6:1 return)
```

**Note:** ROI calculation based on estimated prevented incidents (inherently uncertain), but demonstrates security value

**E. Budget Efficiency Opportunities**

**Identified Savings:**

1. **Pen Test Vendor MSA:**

   - Current: 15 projects × $5,000 = $75,000 (ad-hoc pricing)
   - With MSA: 15 projects × $3,500 = $52,500 (volume discount)
   - Savings: $22,500/year (30% reduction)

2. **Standardized Vendor Questionnaire:**

   - Current: Custom assessment per vendor = 20 hours InfoSec time × $100/hour = $2,000 per vendor
   - With Standard: 5 hours InfoSec time = $500 per vendor
   - Savings: $1,500 per vendor × 10 vendors = $15,000/year

3. **Automated SAST in CI/CD:**

   - Current: Manual code reviews = 40 hours InfoSec time per project × 10 software projects = 400 hours
   - With Automation: SAST tool + 10 hours triage per project = 100 hours InfoSec time
   - Savings: 300 hours InfoSec time = $30,000 value (or redeploy to higher-value activities)

**Total Potential Savings: $67,500/year (27% of security budget)**

**Recommendation:** Invest savings in additional InfoSec headcount (0.5 FTE = $60,000)

---

# Executive Presentation Best Practices

**Purpose:** Guidance on presenting portfolio dashboard to executives and board

## Presentation Principles

**The One-Page Rule:**

- Executives want the story on one slide/page
- Details available for drill-down questions
- Use Component 1 (Executive Summary) as the one-pager

**Traffic-Light Reporting:**

- Use 🟢🟡🔴 status indicators liberally
- Executives process visual cues faster than numbers
- Red items get immediate attention, green items acknowledged briefly

**Data-Driven Storytelling:**

- Don't just present numbers, tell the story
- Example: "We improved 15% over the year because we established pen test vendor MSA and standardized handover templates"
- Connect data to business outcomes

**Focus on Decisions:**

- Executives don't want info dumps, they want to make decisions
- Clear asks: "We need to delay CustomerPortal deployment 2 weeks to remediate findings. Approve?"
- Provide options: "Option A: Delay. Option B: Accept risk (CISO recommends against)."

## Slide-by-Slide Presentation Guide

**Slide 1: Portfolio Snapshot (2 minutes)**

**Script:**
"Our project security portfolio is 🟢 Green with 82% compliance, up 4% from last quarter. We have 25 active projects: 5 High Risk averaging 88% compliance, 12 Medium averaging 81%, and 8 Low averaging 78%. 

We have 2 projects requiring immediate attention: CustomerPortal and API Gateway, both High Risk with compliance below 70%. I'll detail these in a moment.

Our top portfolio gaps are penetration testing (affecting 40% of projects), security handover docs (28%), and threat modeling (20%). We have remediation plans for all three.

The trend is positive: we've improved 15% over the past year due to process improvements like establishing pen test vendor relationships and standardized documentation templates."

**Key Visual:** Large traffic light (GREEN), compliance score gauge (82%), trend line (↑)

---

**Slide 2: Priority Projects Requiring Decisions (3 minutes)**

**Script:**
"CustomerPortal is our top priority. It's High Risk, currently at 65% compliance, with 3 High security findings from penetration testing. Deployment was scheduled for January 1st, but we cannot deploy with these findings open.

**Decision needed:** Approve 2-week deployment delay to remediate findings. If we delay, we go live January 15th with findings fixed. If we don't delay, we deploy with known High vulnerabilities, which CISO recommends against due to data breach risk.

**Recommendation:** Approve delay.

**Business impact:** 2-week delay affects launch timeline but protects customer data and prevents potential $500K breach cost."

**Key Visual:** Project card with red indicator, findings table, timeline comparison (Jan 1 vs. Jan 15)

---

**Slide 3: Trend and Continuous Improvement (2 minutes)**

**Script:**
"The good news: we're getting better at security integration. Portfolio compliance improved from 67% to 82% over the past year. More projects are meeting the 85% target (64% vs. 32% a year ago).

What drove improvement:
1. Pen test vendor MSA established (reduced delays)
2. Security handover template created (improved closure quality)
3. PM security training rolled out (better awareness)

We have identified 3 more process improvements for next quarter based on lessons learned, which I'll cover in recommendations."

**Key Visual:** Line chart showing trend, bar chart showing project distribution (more green, less red)

---

**Slide 4: Recommendations and Budget (2 minutes)**

**Script:**
"Based on portfolio analysis, we recommend 3 investments:

1. **Additional InfoSec headcount (0.5 FTE, $60K/year):** Our InfoSec Officer is at 100% utilization supporting 15 simultaneous projects. This creates bottlenecks and delays. Adding 0.5 FTE enables us to support current portfolio plus growth.

2. **Pen test vendor MSA ($0, saves $22K/year):** Volume pricing reduces per-project cost 30%. Pays for itself.

3. **Standardized vendor assessment questionnaire ($0, saves 300 InfoSec hours/year):** Reduces time per vendor assessment from 20 hours to 5 hours.

Total ask: $60K/year for headcount, offset by $22K savings = net $38K increase.

**ROI:** Estimated $900K in prevented incidents due to security integration across portfolio. Security budget is 5% of project budget, industry benchmark is 5-10%, so we're at the low end."

**Key Visual:** Budget breakdown, ROI calculation, savings chart

---

**Slide 5: Q&A and Actions (varies)**

**Be prepared for:**

- "Why is CustomerPortal only 65%?" → Detailed explanation
- "Can we deploy CustomerPortal without delay?" → Risk explanation, CISO recommendation
- "How does 82% compare to industry?" → Benchmarking data (if available)
- "What if we don't approve additional headcount?" → Impact explanation (delays, quality degradation)

---

**Closing:**
"To summarise: Portfolio is healthy and improving. 2 projects need decisions today (CustomerPortal delay approval). 3 process improvements recommended for Q1 ($60K investment, $22K savings). Any questions?"

---

# Quarterly vs. Annual Reporting

**Quarterly Dashboard (for Management Review):**

- Focus: Current status, QoQ trends, immediate priorities
- Depth: Detailed project status, gap analysis
- Audience: Executive Management, CISO, PMO Director
- Format: 10-15 slide presentation + Excel dashboard
- Duration: 30-45 minutes
- Decisions: Project-specific (delay approvals, budget adjustments)

**Annual Dashboard (for Board):**

- Focus: Year-over-year trends, strategic investments, program maturity
- Depth: High-level summary, major incidents/near-misses, strategic direction
- Audience: Board of Directors, CEO, CFO
- Format: 5-8 slide presentation, executive summary (1-pager)
- Duration: 15-20 minutes
- Decisions: Strategic (headcount approval, major process changes, risk appetite)

**Annual Dashboard Differences:**

**Slide 1: Annual Portfolio Summary**
```
Full Year 2024 Highlights:
  • Projects Completed: 40
  • Average Compliance: 79% (up from 65% in 2023)
  • High Risk Projects: 10 (all achieved ≥80% compliance)
  • Major Incidents: 0 (security incidents prevented through project security integration)
  • Process Improvements: 5 implemented (pen test MSA, handover template, PM training, etc.)
```

**Slide 2: Strategic Achievements**

- Prevented incidents and estimated value saved
- Process maturity improvements (before/after comparisons)
- Capability building (team skills, tools, processes)

**Slide 3: Risk and Compliance Posture**

- Regulatory compliance trends (GDPR, PCI, FINMA)
- Portfolio risk profile changes (fewer high-risk projects in red zone)

**Slide 4: Strategic Investments for Next Year**

- Major initiatives (e.g., security automation, additional headcount, tool acquisitions)
- Budget request with business justification
- Expected outcomes (reduced time-to-market, improved security posture)

**Slide 5: Board Questions**

- Risk appetite discussion: "Are we accepting appropriate level of project security risk?"
- Investment decisions: "Approve $200K for security program enhancements?"

---

**END OF USER GUIDE**

---

*"A portfolio is only as secure as its least secure project."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
