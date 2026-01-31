# ISMS-IMP-A.5.15-16-18.S5 - IAM Governance Compliance Dashboard
## Part I: User Completion Guide
### ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18: Consolidated IAM Compliance

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S5 |
| **Version** | 1.0 |
| **Assessment Area** | IAM Governance Compliance Dashboard - Executive Summary |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Consolidate metrics from all 4 IAM assessments into executive dashboard for IAM maturity monitoring and compliance reporting |
| **Target Audience** | CISO, Executive Management, IAM Team Lead, Security Operations, Internal Audit |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Monthly (Dashboard Update), Quarterly (Executive Review), Annual (Strategic Planning) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IAM Governance Dashboard | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

This dashboard consolidates metrics from all 4 IAM assessments into a single executive view, providing:

- **Overall IAM Maturity Score**: Weighted average across all IAM controls (A.5.15, A.5.16, A.5.18)
- **Control-Specific Compliance**: Individual scores for A.5.15 (Access Control), A.5.16 (Identity Management), A.5.18 (Access Rights)
- **Consolidated Gaps**: All gaps from 4 assessments prioritized by risk
- **Trend Analysis**: Month-over-month and quarter-over-quarter improvements
- **Executive Summary**: One-page overview for CISO and management

### Dashboard Data Sources

This dashboard **PULLS data from** all 4 IAM assessment workbooks:

| Source | Metrics Retrieved | Usage |
|--------|------------------|-------|
| **IMP.1** (User Inventory & Lifecycle) | Provisioning %, Deprovisioning %, Orphaned accounts | A.5.16 compliance score |
| **IMP.2** (Access Rights Matrix) | Access documentation %, Privileged access count | A.5.18 compliance score |
| **IMP.3** (Access Review Results) | Review completion %, Access removal rate | A.5.15 + A.5.18 scores |
| **IMP.4** (Role & SoD Compliance) | RBAC adoption %, SoD violations, Role review % | A.5.15 + A.5.18 scores |

### Key Outputs

Upon completion, you will have:

1. ✅ **Executive Summary Dashboard**: One-page IAM maturity overview
2. ✅ **Control-Specific Scores**: A.5.15, A.5.16, A.5.18 compliance (0-100)
3. ✅ **Overall IAM Maturity**: Weighted average across all controls
4. ✅ **Consolidated Gap Analysis**: All gaps prioritized by severity
5. ✅ **Trend Charts**: Historical improvement tracking (if data available)
6. ✅ **Evidence Summary**: Evidence count by assessment
7. ✅ **Monthly Executive Report**: CISO presentation-ready summary

---

## Prerequisites

### Data Sources Required

Before starting this dashboard, you must have completed:

1. **ISMS-IMP-A.5.15-16-18.S1** (User Inventory & Lifecycle Compliance)
   - File: `ISMS-IMP-A.5.15-16-18.S1_UserInventory_YYYY-MM.xlsx`
   - Required Sheets: `Lifecycle_Compliance_Dashboard` (Sheet 7)

2. **ISMS-IMP-A.5.15-16-18.S2** (Access Rights Matrix)
   - File: `ISMS-IMP-A.5.15-16-18.S2_AccessRights_YYYY-MM.xlsx`
   - Required Sheets: `Access_Rights_Dashboard` (Sheet 7)

3. **ISMS-IMP-A.5.15-16-18.S3** (Access Review Results)
   - File: `ISMS-IMP-A.5.15-16-18.S3_AccessReview_YYYY-MM.xlsx`
   - Required Sheets: `Review_Compliance_Dashboard` (Sheet 6)

4. **ISMS-IMP-A.5.15-16-18.S4** (Role & SoD Compliance)
   - File: `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx`
   - Required Sheets: `RBAC_Metrics` (Sheet 7)

### File Organization

**Recommended folder structure**:
```
SharePoint/IAM_Assessments/2025-10/
├── ISMS-IMP-A.5.15-16-18.S1_UserInventory_2025-10.xlsx
├── ISMS-IMP-A.5.15-16-18.S2_AccessRights_2025-10.xlsx
├── ISMS-IMP-A.5.15-16-18.S3_AccessReview_2025-10.xlsx
├── ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2025-10.xlsx
└── ISMS-IMP-A.5.15-16-18.S5_Dashboard_2025-10.xlsx (this file)
```

All 5 files should be in the same folder for easy cross-workbook referencing.

### Time Commitment

- **Initial dashboard setup**: 3-4 hours (establish cross-workbook links)
- **Monthly dashboard update**: 30-60 minutes (refresh links, update charts)
- **Quarterly executive review**: 1-2 hours (trend analysis, presentation prep)
- **Annual strategic planning**: 2-3 hours (maturity roadmap, investment planning)

---

## Workflow

### Dashboard Update Flow

```
1. COMPLETE ALL 4 ASSESSMENTS (IMP.1, IMP.2, IMP.3, IMP.4)
   ↓
2. ESTABLISH CROSS-WORKBOOK LINKS (Sheet 3, 4, 5, 6)
   ↓
3. REFRESH DATA (Update links from source workbooks)
   ↓
4. CALCULATE CONTROL SCORES (Sheet 8)
   ↓
5. CONSOLIDATE GAPS (Sheet 7)
   ↓
6. UPDATE DASHBOARD (Sheet 2)
   ↓
7. GENERATE EXECUTIVE SUMMARY (Sheet 2)
   ↓
8. REVIEW & APPROVE (Sheet 10)
```

### Phase 1: Source Assessment Completion (Varies)

**Objective**: Complete all 4 prerequisite assessments

**Steps**:
1. Complete ISMS-IMP-A.5.15-16-18.S1 (User Inventory)
2. Complete ISMS-IMP-A.5.15-16-18.S2 (Access Rights Matrix)
3. Complete ISMS-IMP-A.5.15-16-18.S3 (Access Review Results)
4. Complete ISMS-IMP-A.5.15-16-18.S4 (Role & SoD Compliance)
5. Ensure all 4 files are approved (CISO sign-off)
6. Save all 4 files in same folder

**Deliverable**: 4 completed assessment workbooks with CISO approval

**Quality Check**:
- ✓ All 4 assessments completed
- ✓ All approvals obtained (three-level sign-off)
- ✓ All files in same folder
- ✓ File naming consistent (ISMS-IMP-A.5.15-16-18.X_Name_YYYY-MM.xlsx)

### Phase 2: Dashboard Setup (3-4 hours - First Time Only)

**Objective**: Establish cross-workbook links to source assessments

**Steps**:
1. Open dashboard workbook (ISMS-IMP-A.5.15-16-18.S5)
2. **Sheet 3** (Identity Lifecycle Metrics):
   - Link to IMP.1 `Lifecycle_Compliance_Dashboard` (Sheet 7)
   - Pull: Provisioning %, Deprovisioning %, Orphaned accounts, Lifecycle maturity score
3. **Sheet 4** (Access Rights Metrics):
   - Link to IMP.2 `Access_Rights_Dashboard` (Sheet 7)
   - Pull: Total access grants, Privileged access count, Documentation %, Access rights score
4. **Sheet 5** (Access Review Metrics):
   - Link to IMP.3 `Review_Compliance_Dashboard` (Sheet 6)
   - Pull: Review completion %, Overdue reviews, Access removal rate, Review compliance score
5. **Sheet 6** (Role & SoD Metrics):
   - Link to IMP.4 `RBAC_Metrics` (Sheet 7)
   - Pull: RBAC adoption %, SoD violations, Role review %, RBAC maturity score
6. Test all links (ensure no #REF errors)
7. Save workbook

**Deliverable**: Dashboard with functional cross-workbook links

**Quality Check**:
- ✓ All cross-workbook links established
- ✓ No #REF or #VALUE errors
- ✓ Data populates correctly when source files open
- ✓ Links update when source data changes

**Note**: Cross-workbook links require source files to be in same folder and accessible.

### Phase 3: Monthly Dashboard Refresh (30-60 minutes)

**Objective**: Update dashboard with latest assessment data

**Steps**:
1. Open all 5 files (4 source assessments + dashboard)
2. **Data → Refresh All** (Excel will update all links)
3. Verify data populated correctly:
   - Sheet 3: Lifecycle metrics updated
   - Sheet 4: Access rights metrics updated
   - Sheet 5: Access review metrics updated
   - Sheet 6: Role & SoD metrics updated
4. **Sheet 7** (Consolidated Gap Analysis):
   - Review gaps from all 4 assessments
   - Update gap status (Open → In Progress → Closed)
   - Add new gaps if identified
5. **Sheet 8** (Compliance Scoring):
   - Formulas auto-calculate control scores (A.5.15, A.5.16, A.5.18)
   - Verify overall IAM maturity score
6. **Sheet 2** (Executive Summary Dashboard):
   - All charts auto-update
   - Review key findings
   - Update executive summary text
7. Save dashboard

**Deliverable**: Updated dashboard with current month data

**Quality Check**:
- ✓ All metrics reflect latest assessment data
- ✓ No stale data (dates match current month)
- ✓ Gaps updated (status reflects remediation progress)
- ✓ Charts updated (visual representations current)

### Phase 4: Control Score Calculation (Auto - Verify 15 minutes)

**Objective**: Calculate compliance scores for each control

**Steps**:
1. **Sheet 8** (Compliance Scoring Matrix)
2. Formulas auto-calculate:
   - **A.5.15 Score** (Access Control):
     - = Average(Access Review Score, Role & SoD Score)
     - Components: Review completion, SoD compliance
   - **A.5.16 Score** (Identity Management):
     - = Lifecycle Score
     - Components: Provisioning %, Deprovisioning %, Orphaned accounts
   - **A.5.18 Score** (Access Rights):
     - = Average(Access Rights Score, Review Score, RBAC Score)
     - Components: Documentation %, Review completion, RBAC adoption
   - **Overall IAM Maturity**:
     - = (A.5.16 × 30%) + (A.5.18 × 40%) + (A.5.15 × 30%)
3. Verify calculations (spot check formulas)
4. Assign maturity rating (Excellent/Very Good/Good/Fair/Poor)

**Deliverable**: Calculated control scores with maturity rating

**Quality Check**:
- ✓ A.5.15 score calculated correctly (access control + SoD)
- ✓ A.5.16 score calculated correctly (lifecycle compliance)
- ✓ A.5.18 score calculated correctly (access rights + reviews + RBAC)
- ✓ Overall maturity score weighted correctly (30/40/30)
- ✓ Maturity rating assigned (Excellent >= 90, Very Good 80-89, etc.)

### Phase 5: Consolidated Gap Analysis (30 minutes)

**Objective**: Consolidate gaps from all 4 assessments

**Steps**:
1. **Sheet 7** (Consolidated Gap Analysis)
2. Import gaps from all 4 source assessments:
   - IMP.1 Sheet 8 (Gap Analysis)
   - IMP.2 Sheet 8 (Gap Analysis)
   - IMP.3 Sheet 7 (Gap Analysis)
   - IMP.4 Sheet 8 (Gap Analysis)
3. For each gap:
   - Gap ID, Source (which assessment)
   - Gap Type, Severity (Critical/High/Medium/Low)
   - Description, Current State, Target State
   - Owner, Remediation Plan, Target Date, Status
4. Prioritize by severity:
   - Critical gaps first (unresolved SoD, orphaned accounts)
   - High gaps second (low RBAC adoption, missing reviews)
   - Medium/Low gaps last
5. Update gap status (Open → In Progress → Closed)
6. Track gap closure trend

**Deliverable**: Consolidated gap list prioritized by risk

**Quality Check**:
- ✓ All gaps from 4 assessments included
- ✓ Gaps prioritized by severity (Critical → High → Medium → Low)
- ✓ Gap status updated (reflects remediation progress)
- ✓ Owners assigned (accountability)
- ✓ Target dates tracked (overdue gaps flagged)

### Phase 6: Executive Dashboard Update (30 minutes)

**Objective**: Update Sheet 2 (Executive Summary Dashboard)

**Steps**:
1. **Sheet 2** (Executive_Summary_Dashboard)
2. Review auto-populated sections:
   - **Overall IAM Maturity Score**: 0-100 (from Sheet 8)
   - **Control-Specific Scores**: A.5.15, A.5.16, A.5.18 (from Sheet 8)
   - **Critical Gaps Count**: Count from Sheet 7
   - **Trend Charts**: Month-over-month (if historical data)
3. Update **Key Findings** (text section):
   - Summarize top 3-5 findings (1-2 sentences each)
   - Example: "RBAC adoption increased from 65% to 72% (+7%)"
   - Example: "2 critical SoD violations remediated this month"
4. Update **Recommended Actions** (text section):
   - Top 5 priorities for next month
   - Example: "1. Remediate remaining SoD violation (User123)"
   - Example: "2. Create 3 new roles to increase RBAC adoption"
5. Update **Executive Summary** (text section):
   - 3-4 paragraph overview (suitable for CISO presentation)
   - Overall maturity, key improvements, remaining gaps, next steps

**Deliverable**: Executive-ready dashboard (Sheet 2)

**Quality Check**:
- ✓ All metrics current (reflect latest data)
- ✓ Key findings accurate (spot check against source assessments)
- ✓ Recommended actions prioritized (top 5 most important)
- ✓ Executive summary concise (3-4 paragraphs, no jargon)
- ✓ Charts updated (visual representations current)

### Phase 7: Evidence Summary (15 minutes)

**Objective**: Summarize evidence from all 4 assessments

**Steps**:
1. **Sheet 9** (Evidence Summary)
2. Count evidence items from each assessment:
   - IMP.1 Sheet 9 (Evidence Register): Count evidence items
   - IMP.2 Sheet 9 (Evidence Register): Count evidence items
   - IMP.3 Sheet 8 (Evidence Register): Count evidence items
   - IMP.4 Sheet 9 (Evidence Register): Count evidence items
3. Calculate totals:
   - Total evidence items (sum across all 4)
   - Evidence by type (Documents, Exports, Approvals, etc.)
   - Evidence by control (A.5.15, A.5.16, A.5.18)
4. Verify audit readiness:
   - All evidence accessible?
   - Evidence recent (within assessment period)?
   - Evidence retention documented?

**Deliverable**: Evidence summary with audit readiness indicator

**Quality Check**:
- ✓ Evidence count accurate (matches source assessments)
- ✓ Evidence categorized (by type and control)
- ✓ Audit readiness verified (all evidence accessible)

### Phase 8: Review & Approval (30 minutes)

**Objective**: Complete Sheet 10 (Approval and Sign-Off)

**Steps**:
1. **Monthly Dashboard Review** (IAM Team Lead):
   - Verify data accuracy (spot check against source assessments)
   - Review key findings (reasonable?)
   - Review recommended actions (priorities correct?)
   - Approve or request revisions
   - Document review date and sign-off

2. **Quarterly Executive Review** (CISO):
   - Review overall IAM maturity (acceptable?)
   - Review control-specific scores (concerns?)
   - Review critical gaps (remediation on track?)
   - Review trend (improving over time?)
   - Approve dashboard
   - Schedule next quarterly review

3. **Annual Strategic Review** (Executive Management):
   - Review annual IAM maturity trend
   - Assess strategic alignment (IAM maturity supports business goals?)
   - Identify technology investments (IAM platforms, automation)
   - Approve IAM strategic plan
   - Allocate budget for IAM improvements

**Deliverable**: Approved dashboard with executive sign-off

**Quality Check**:
- ✓ Monthly review completed (IAM Team Lead sign-off)
- ✓ Quarterly review completed (CISO sign-off)
- ✓ Annual review completed (Executive Management sign-off)
- ✓ Next review dates scheduled
- ✓ Approved dashboard archived

---

## Completing Each Sheet

### Sheet 1: Instructions and Legend

**Purpose**: Document control, how to use dashboard, data sources

**Key Sections**:
1. **Document Control**: Dashboard ID, version, assessment period, prepared by
2. **Dashboard Overview**: Purpose, data sources, how to read dashboard
3. **Data Source Registry**: List of 4 source assessment files
4. **Refresh Procedures**: How to update dashboard (Data → Refresh All)
5. **Status Legends**: Red/Yellow/Green indicators
6. **Maturity Rating Scale**: Excellent (90-100), Very Good (80-89), Good (70-79), Fair (60-69), Poor (<60)

### Sheet 2: Executive_Summary_Dashboard

**Purpose**: One-page executive view of IAM maturity

**Key Sections**:

1. **Overall IAM Maturity Score** (Top Center):
   - Large number: 0-100 (from Sheet 8)
   - Maturity rating: Excellent/Very Good/Good/Fair/Poor
   - Color-coded: Green (>= 80), Yellow (60-79), Red (< 60)

2. **Control-Specific Scores** (Top Row):
   - A.5.15 (Access Control): 0-100 (from Sheet 8)
   - A.5.16 (Identity Management): 0-100 (from Sheet 8)
   - A.5.18 (Access Rights): 0-100 (from Sheet 8)
   - Each with color-coded background

3. **Critical Gaps Indicator** (Top Right):
   - Count of Critical + High gaps (from Sheet 7)
   - 🚨 Red if Critical > 0
   - ⚠️ Orange if High > 5
   - ✅ Green if Critical = 0 and High <= 5

4. **Key Metrics Grid** (Middle Section):
   | Metric | Value | Target | Status |
   |--------|-------|--------|--------|
   | RBAC Adoption | 78% | >= 80% | Yellow |
   | Lifecycle Compliance | 92% | >= 90% | Green |
   | Review Completion | 87% | >= 95% | Yellow |
   | SoD Violations (Unresolved) | 1 | 0 | Red |
   | Orphaned Accounts | 3 | 0 | Red |
   | Direct Access % | 22% | < 20% | Yellow |

5. **Trend Charts** (Bottom Left):
   - Overall IAM Maturity Trend (last 6 months)
   - Control-Specific Score Trends (A.5.15, A.5.16, A.5.18)
   - Gap Count Trend (Critical, High, Medium, Low)

6. **Key Findings** (Bottom Center):
   - Top 3-5 findings (bullet points)
   - Example: "RBAC adoption increased 7% month-over-month"
   - Example: "2 critical SoD violations remediated"
   - Example: "Orphaned account count reduced from 8 to 3"

7. **Recommended Actions** (Bottom Right):
   - Top 5 priorities for next month (numbered list)
   - Example: "1. Remediate remaining SoD violation (User123)"
   - Example: "2. Create 3 new roles (Sales, Support, Marketing)"
   - Example: "3. Complete overdue access reviews (5 systems)"

8. **Executive Summary** (Separate Section):
   - 3-4 paragraph overview
   - Overall assessment, key improvements, remaining gaps, next steps
   - Suitable for CISO presentation to executive management

### Sheet 3: Identity_Lifecycle_Metrics (from IMP.1)

**Purpose**: Lifecycle compliance metrics (A.5.16)

**Data Source**: ISMS-IMP-A.5.15-16-18.S1 `Lifecycle_Compliance_Dashboard` (Sheet 7)

**Key Metrics**:
- Total Users (Active)
- Provisioning Compliance Rate (%)
- Deprovisioning Compliance Rate (%)
- Orphaned Account Count
- Inactive Account Count (90+ days no login)
- Lifecycle Maturity Score (0-100)

**Cross-Workbook Formulas**:
```
='[ISMS-IMP-A.5.15-16-18.S1_UserInventory_2025-10.xlsx]Lifecycle_Compliance_Dashboard'!B4
```

**Quality Check**:
- ✓ All metrics populate (no #REF errors)
- ✓ Values reasonable (spot check against source file)
- ✓ Date matches current assessment period

### Sheet 4: Access_Rights_Metrics (from IMP.2)

**Purpose**: Access rights documentation and management (A.5.18)

**Data Source**: ISMS-IMP-A.5.15-16-18.S2 `Access_Rights_Dashboard` (Sheet 7)

**Key Metrics**:
- Total Access Grants
- Access by Data Sensitivity (Restricted, Confidential, Internal, Public)
- Privileged Access Count
- Contractor/Vendor Access Count
- Access Rights Documentation Completeness (%)
- Access Rights Score (0-100)

**Cross-Workbook Formulas**:
```
='[ISMS-IMP-A.5.15-16-18.S2_AccessRights_2025-10.xlsx]Access_Rights_Dashboard'!B4
```

**Quality Check**:
- ✓ All metrics populate
- ✓ Values reasonable
- ✓ Date matches assessment period

### Sheet 5: Access_Review_Metrics (from IMP.3)

**Purpose**: Access review completion and effectiveness (A.5.15 + A.5.18)

**Data Source**: ISMS-IMP-A.5.15-16-18.S3 `Review_Compliance_Dashboard` (Sheet 6)

**Key Metrics**:
- Review Completion Rate (%)
- Overdue Reviews (Count)
- Access Removal Rate (%)
- Reviewer Accountability (%)
- Review Frequency Compliance (%)
- Review Compliance Score (0-100)

**Cross-Workbook Formulas**:
```
='[ISMS-IMP-A.5.15-16-18.S3_AccessReview_2025-10.xlsx]Review_Compliance_Dashboard'!B4
```

**Quality Check**:
- ✓ All metrics populate
- ✓ Values reasonable
- ✓ Date matches assessment period

### Sheet 6: Role_and_SoD_Metrics (from IMP.4)

**Purpose**: RBAC maturity and SoD compliance (A.5.15 + A.5.18)

**Data Source**: ISMS-IMP-A.5.15-16-18.S4 `RBAC_Metrics` (Sheet 7)

**Key Metrics**:
- RBAC Adoption Rate (%)
- SoD Violations (Total, Unresolved, Justified, Remediated)
- Role Review Compliance (%)
- Role Catalog Health (Active, Obsolete, Unused roles)
- Role Accuracy Score (%)
- RBAC Maturity Score (0-100)

**Cross-Workbook Formulas**:
```
='[ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2025-10.xlsx]RBAC_Metrics'!B7
```

**Quality Check**:
- ✓ All metrics populate
- ✓ Values reasonable
- ✓ Date matches assessment period

### Sheet 7: Consolidated_Gap_Analysis

**Purpose**: All gaps from 4 assessments prioritized by risk

**Data Sources**:
- IMP.1 Sheet 8 (Gap Analysis)
- IMP.2 Sheet 8 (Gap Analysis)
- IMP.3 Sheet 7 (Gap Analysis)
- IMP.4 Sheet 8 (Gap Analysis)

**Column Structure**:
- Gap_ID, Source_Assessment (IMP.1/2/3/4)
- Gap_Type, Severity (Critical/High/Medium/Low)
- Description, Current_State, Target_State
- Owner, Remediation_Plan, Target_Date, Status
- Audit_Impact (Finding, Observation, No Impact)

**How to Complete**:
1. Copy all gaps from IMP.1 Sheet 8 (rows 2-X)
2. Copy all gaps from IMP.2 Sheet 8 (rows 2-X)
3. Copy all gaps from IMP.3 Sheet 7 (rows 2-X)
4. Copy all gaps from IMP.4 Sheet 8 (rows 2-X)
5. Sort by Severity (Critical → High → Medium → Low)
6. Update Status monthly (Open → In Progress → Closed)
7. Track gap closure trend

**Summary Metrics**:
- Total Gaps (All assessments)
- Critical Gaps, High Gaps, Medium Gaps, Low Gaps
- Open Gaps, In Progress, Closed Gaps
- Overdue Gaps (Target_Date < TODAY)
- Gap Closure Rate (%) = Closed / Total

**Quality Check**:
- ✓ All gaps from 4 assessments included
- ✓ No duplicate gaps
- ✓ Severity prioritization correct
- ✓ Status updated monthly
- ✓ Overdue gaps flagged (red)

### Sheet 8: Compliance_Scoring_Matrix

**Purpose**: Calculate control-specific scores and overall IAM maturity

**Control Score Formulas**:

1. **A.5.15 Score (Access Control)**:
   ```
   = (Access_Review_Metrics!B50 × 50%) +    [Review compliance]
     (Role_and_SoD_Metrics!B50 × 50%)       [SoD compliance]
   ```
   Components:
   - Access review completion (IMP.3)
   - SoD compliance (IMP.4)

2. **A.5.16 Score (Identity Management)**:
   ```
   = Identity_Lifecycle_Metrics!B60         [Lifecycle maturity]
   ```
   Components:
   - Provisioning compliance (IMP.1)
   - Deprovisioning compliance (IMP.1)
   - Orphaned account management (IMP.1)

3. **A.5.18 Score (Access Rights)**:
   ```
   = (Access_Rights_Metrics!B40 × 30%) +    [Access rights documentation]
     (Access_Review_Metrics!B50 × 35%) +    [Review completion]
     (Role_and_SoD_Metrics!B7 × 35%)        [RBAC adoption]
   ```
   Components:
   - Access rights documentation (IMP.2)
   - Access review completion (IMP.3)
   - RBAC adoption (IMP.4)

4. **Overall IAM Maturity Score**:
   ```
   = (A.5.16_Score × 30%) +                 [Identity lifecycle weight]
     (A.5.18_Score × 40%) +                 [Access rights weight]
     (A.5.15_Score × 30%)                   [Access control weight]
   ```

5. **Maturity Rating**:
   ```
   =IF(Overall_Score>=90, "Excellent",
      IF(Overall_Score>=80, "Very Good",
        IF(Overall_Score>=70, "Good",
          IF(Overall_Score>=60, "Fair", "Poor"))))
   ```

**Benchmark Comparisons**:
| Score | Rating | IAM Maturity |
|-------|--------|--------------|
| 90-100 | Excellent | World-class IAM governance |
| 80-89 | Very Good | Strong IAM governance, minor gaps |
| 70-79 | Good | Solid IAM governance, some improvements needed |
| 60-69 | Fair | Basic IAM governance, significant gaps |
| <60 | Poor | Weak IAM governance, major gaps |

**Quality Check**:
- ✓ A.5.15 score calculated correctly
- ✓ A.5.16 score calculated correctly
- ✓ A.5.18 score calculated correctly
- ✓ Overall maturity weighted correctly (30/40/30)
- ✓ Maturity rating assigned (Excellent/Very Good/Good/Fair/Poor)

### Sheet 9: Evidence_Summary

**Purpose**: Evidence count by assessment and audit readiness

**Data Sources**:
- IMP.1 Sheet 9 (Evidence Register)
- IMP.2 Sheet 9 (Evidence Register)
- IMP.3 Sheet 8 (Evidence Register)
- IMP.4 Sheet 9 (Evidence Register)

**Summary Metrics**:
- Total Evidence Items (Sum across all 4 assessments)
- Evidence by Assessment (IMP.1, IMP.2, IMP.3, IMP.4)
- Evidence by Type (Documents, Exports, Screenshots, Approvals, Meeting Minutes)
- Evidence by Control (A.5.15, A.5.16, A.5.18)
- Audit Readiness Indicator (All evidence accessible? Recent? Retention documented?)

**Audit Readiness Checklist**:
- [ ] All evidence accessible (not on individual laptops)
- [ ] Evidence recent (within assessment period)
- [ ] Evidence retention documented (3 years typical)
- [ ] Evidence categorized (by control)
- [ ] Evidence count >= 60 (15+ per assessment)

**Quality Check**:
- ✓ Evidence count accurate (matches source assessments)
- ✓ Evidence categorized correctly
- ✓ Audit readiness verified

### Sheet 10: Approval_and_Sign_Off

**Purpose**: Monthly, quarterly, and annual approval workflow

**Three Approval Levels**:

1. **Monthly Dashboard Review** (IAM Team Lead):
   - Review Date, Reviewer Name, Title
   - Data Accuracy Verified? (Yes/No)
   - Key Findings Reasonable? (Yes/No)
   - Recommended Actions Prioritized? (Yes/No)
   - Approval Status (Approved, Revisions Required)
   - Comments/Feedback
   - Signature/Approval, Approval Date

2. **Quarterly Executive Review** (CISO):
   - Review Date, Reviewer Name, Title
   - Overall IAM Maturity Acceptable? (Yes/No)
   - Control Scores Acceptable? (Yes/No)
   - Critical Gaps Reviewed? (Yes/No)
   - Trend Improving? (Yes/No)
   - Approval Status (Approved, Revisions Required)
   - Comments/Recommendations
   - Next Quarterly Review Date
   - Signature/Approval, Approval Date

3. **Annual Strategic Review** (Executive Management):
   - Review Date, Reviewer Name, Title
   - Annual IAM Maturity Trend Acceptable? (Yes/No)
   - Strategic Alignment Confirmed? (Yes/No)
   - Technology Investments Identified? (Yes/No)
   - Budget Allocation Approved? (Yes/No)
   - Approval Status (Approved, Revisions Required)
   - Strategic Recommendations
   - Next Annual Review Date
   - Signature/Approval, Approval Date

**Quality Check**:
- ✓ Monthly review completed (IAM Team Lead sign-off)
- ✓ Quarterly review completed (CISO sign-off)
- ✓ Annual review completed (Executive Management sign-off)
- ✓ Next review dates scheduled
- ✓ All feedback addressed

---

## Common Pitfalls & Solutions

### Pitfall 1: Source Files Not Accessible

**Problem**: Cross-workbook links show #REF errors because source files are not in same folder or not open.

**Solution**:
1. Ensure all 5 files in same folder
2. Open all 5 files simultaneously
3. Data → Refresh All (Excel will update links)
4. If #REF errors persist: Edit links (Data → Edit Links) and update file paths

### Pitfall 2: Stale Dashboard Data

**Problem**: Dashboard shows old data because links not refreshed.

**Solution**:
1. Open all 5 files (4 source assessments + dashboard)
2. Data → Refresh All (update all links)
3. Verify dates match current assessment period
4. Save dashboard after refresh

### Pitfall 3: Missing Historical Trend Data

**Problem**: Trend charts show only 1 month because no historical data.

**Solution**:
1. **Month 1**: Create baseline dashboard
2. **Month 2**: Copy previous month scores to historical table (Sheet 2)
3. **Month 3+**: Continue adding monthly scores
4. Trend charts will populate as historical data accumulates
5. Minimum 3 months data needed for meaningful trends

### Pitfall 4: Inconsistent Assessment Periods

**Problem**: 4 source assessments have different assessment periods (September vs. October).

**Solution**:
1. Standardize assessment periods across all 4 assessments
2. Complete all 4 assessments in same month
3. Dashboard assessment period = same as source assessments
4. If assessments must stagger: Note which assessment is which period in dashboard

### Pitfall 5: Gap Duplication

**Problem**: Same gap appears in multiple source assessments, gets counted twice in consolidated gap analysis.

**Solution**:
1. Review gaps during consolidation (Sheet 7)
2. Identify duplicates (same gap, different assessment)
3. Keep one instance (from most relevant assessment)
4. Delete duplicate
5. Note in Description: "Consolidated from IMP.X and IMP.Y"

### Pitfall 6: Overloading Dashboard with Detail

**Problem**: Dashboard too detailed (not executive-friendly).

**Solution**:
1. **Sheet 2** (Executive Summary) should be ONE PAGE
2. Details in Sheets 3-9 (for those who want to drill down)
3. Executive Summary: 3-4 paragraphs max
4. Key Findings: 3-5 bullet points max
5. Recommended Actions: Top 5 priorities max
6. Use visuals (charts) over tables where possible

### Pitfall 7: No Action on Dashboard Findings

**Problem**: Dashboard created monthly but gaps never remediated.

**Solution**:
1. Dashboard is not the goal - gap remediation is the goal
2. Schedule monthly IAM governance meeting (30 minutes)
3. Review dashboard findings (top 5 priorities)
4. Assign owners for gap remediation
5. Track progress month-over-month
6. Celebrate improvements (positive reinforcement)

---

## Quality Checklist

### Prerequisites
- [ ] IMP.1 (User Inventory) completed and approved
- [ ] IMP.2 (Access Rights Matrix) completed and approved
- [ ] IMP.3 (Access Review Results) completed and approved
- [ ] IMP.4 (Role & SoD Compliance) completed and approved
- [ ] All 4 source files in same folder
- [ ] File naming consistent (ISMS-IMP-A.5.15-16-18.X_Name_YYYY-MM.xlsx)

### Sheet 2: Executive Summary Dashboard
- [ ] Overall IAM Maturity Score calculated (0-100)
- [ ] Maturity rating assigned (Excellent/Very Good/Good/Fair/Poor)
- [ ] Control-specific scores displayed (A.5.15, A.5.16, A.5.18)
- [ ] Critical gaps indicator updated (count from Sheet 7)
- [ ] Key metrics grid populated (6-8 key metrics)
- [ ] Trend charts updated (if historical data available)
- [ ] Key findings summarized (3-5 bullet points)
- [ ] Recommended actions prioritized (top 5)
- [ ] Executive summary written (3-4 paragraphs)
- [ ] Dashboard is ONE PAGE (executive-friendly)

### Sheet 3: Identity Lifecycle Metrics
- [ ] Cross-workbook links established (to IMP.1)
- [ ] All metrics populate (no #REF errors)
- [ ] Values reasonable (spot check against IMP.1)
- [ ] Date matches current assessment period

### Sheet 4: Access Rights Metrics
- [ ] Cross-workbook links established (to IMP.2)
- [ ] All metrics populate (no #REF errors)
- [ ] Values reasonable (spot check against IMP.2)
- [ ] Date matches current assessment period

### Sheet 5: Access Review Metrics
- [ ] Cross-workbook links established (to IMP.3)
- [ ] All metrics populate (no #REF errors)
- [ ] Values reasonable (spot check against IMP.3)
- [ ] Date matches current assessment period

### Sheet 6: Role and SoD Metrics
- [ ] Cross-workbook links established (to IMP.4)
- [ ] All metrics populate (no #REF errors)
- [ ] Values reasonable (spot check against IMP.4)
- [ ] Date matches current assessment period

### Sheet 7: Consolidated Gap Analysis
- [ ] All gaps from IMP.1 included
- [ ] All gaps from IMP.2 included
- [ ] All gaps from IMP.3 included
- [ ] All gaps from IMP.4 included
- [ ] No duplicate gaps
- [ ] Gaps prioritized by severity (Critical → High → Medium → Low)
- [ ] Gap status updated monthly (Open → In Progress → Closed)
- [ ] Overdue gaps flagged (Target_Date < TODAY)
- [ ] Summary metrics calculated (total, by severity, by status)

### Sheet 8: Compliance Scoring Matrix
- [ ] A.5.15 score calculated correctly (access control + SoD)
- [ ] A.5.16 score calculated correctly (lifecycle compliance)
- [ ] A.5.18 score calculated correctly (access rights + reviews + RBAC)
- [ ] Overall IAM maturity score weighted correctly (30/40/30)
- [ ] Maturity rating assigned (Excellent >= 90, Very Good 80-89, etc.)
- [ ] Benchmark comparisons included
- [ ] Formulas verified (no errors)

### Sheet 9: Evidence Summary
- [ ] Evidence count accurate (matches source assessments)
- [ ] Evidence by assessment (IMP.1, IMP.2, IMP.3, IMP.4)
- [ ] Evidence by type (Documents, Exports, Approvals, etc.)
- [ ] Evidence by control (A.5.15, A.5.16, A.5.18)
- [ ] Audit readiness verified (all evidence accessible, recent, retention documented)

### Sheet 10: Approval and Sign-Off
- [ ] Monthly review completed (IAM Team Lead sign-off)
- [ ] Quarterly review completed (CISO sign-off - if quarterly)
- [ ] Annual review completed (Executive Management sign-off - if annual)
- [ ] All feedback addressed
- [ ] Next review dates scheduled
- [ ] Approved dashboard archived

### General Quality
- [ ] No #REF or #VALUE errors (all formulas work)
- [ ] No stale data (dates match current assessment period)
- [ ] Conditional formatting works (green/yellow/red)
- [ ] Charts updated (visual representations current)
- [ ] File naming correct (ISMS-IMP-A.5.15-16-18.S5_Dashboard_YYYY-MM.xlsx)
- [ ] Dashboard executive-friendly (Sheet 2 is one page)

---

## Continuous Improvement

### Monthly Dashboard Refresh (30-60 minutes)

**Frequency**: Monthly (after completing IMP.1/2/3/4 for that month)

**Tasks**:
1. Open all 5 files (4 source assessments + dashboard)
2. Data → Refresh All (update cross-workbook links)
3. Verify all metrics populated correctly
4. Update Sheet 7 (Consolidated Gap Analysis): Status, new gaps, remediation progress
5. Review Sheet 2 (Executive Summary Dashboard): Key findings, recommended actions
6. Update executive summary text (3-4 paragraphs)
7. Save dashboard
8. Schedule monthly IAM governance meeting (review dashboard with team)

**Output**: Updated dashboard with current month data

---

### Quarterly Executive Review (1-2 hours)

**Frequency**: Quarterly (Q1, Q2, Q3, Q4)

**Tasks**:
1. Prepare quarterly dashboard presentation (PowerPoint or PDF from Sheet 2)
2. **Trend Analysis** (Quarter-over-Quarter):
   - Overall IAM maturity trend (improving? stagnant?)
   - Control-specific trends (A.5.15, A.5.16, A.5.18)
   - Gap closure trend (gaps closed vs. new gaps)
   - Key metrics trend (RBAC adoption, lifecycle compliance, etc.)
3. **Gap Remediation Progress**:
   - Gaps closed this quarter
   - Gaps still open (why?)
   - Gaps overdue (escalation needed?)
4. **Key Achievements**:
   - Top 3-5 improvements this quarter
   - Example: "RBAC adoption increased from 65% to 78%"
5. **Remaining Challenges**:
   - Top 3-5 gaps still open
   - Example: "1 critical SoD violation requires CISO decision"
6. **Next Quarter Priorities**:
   - Top 5 priorities for next quarter
   - Resource needs (budget, tools, people)
7. **CISO Review Meeting**:
   - Present quarterly dashboard
   - Discuss challenges and priorities
   - Obtain CISO approval
   - Document feedback and action items

**Output**: Quarterly dashboard presentation with CISO approval

---

### Annual Strategic Review (2-3 hours)

**Frequency**: Annual (typically Q4)

**Tasks**:
1. **Annual Trend Analysis** (Year-over-Year):
   - Overall IAM maturity trajectory (12-month trend)
   - Control-specific maturity (A.5.15, A.5.16, A.5.18)
   - Gap closure effectiveness (total gaps closed in year)
   - Investment effectiveness (did technology investments improve maturity?)

2. **IAM Maturity Roadmap** (Next 12 Months):
   - Current maturity: X (e.g., 75 - "Good")
   - Target maturity: Y (e.g., 85 - "Very Good")
   - Gap: Y - X (e.g., +10 points improvement needed)
   - **Initiatives to close gap**:
     - Increase RBAC adoption (65% → 85%) [+8 points]
     - Achieve zero SoD violations [+5 points]
     - Improve lifecycle compliance (88% → 95%) [+3 points]
     - Total improvement potential: +16 points (exceeds +10 gap)

3. **Technology Investments**:
   - **Current gaps that require technology**:
     - Example: "Manual access provisioning causing slow joiner/mover/leaver"
     - Example: "No automated SoD violation detection"
     - Example: "Access reviews done in spreadsheets (inefficient)"
   - **Technology solutions**:
     - Identity Governance & Administration (IGA) platform (SailPoint, Saviynt)
     - Automated provisioning (ServiceNow, Okta Workflows)
     - Role mining tools (identify role patterns from access data)
   - **Business case**:
     - Cost: $X (licensing, implementation)
     - Benefit: +Y maturity points, -Z hours manual work per month
     - ROI: Payback in N months

4. **Budget Planning**:
   - IAM platform licensing (if applicable)
   - Implementation services (if applicable)
   - Training (IAM team, role owners)
   - Staffing (additional IAM resources if needed)

5. **Executive Presentation**:
   - Present annual IAM maturity review
   - Present IAM maturity roadmap (next 12 months)
   - Present technology investment business case
   - Obtain executive approval
   - Allocate budget

**Output**: IAM strategic plan with executive approval and budget allocation

---

## Integration with Other ISMS Controls

### Upstream Dependencies

**This dashboard consolidates data from IAM controls (A.5.15/16/18), which depend on**:

- **A.5.9 (Asset Inventory)**: IAM needs to know what systems exist (to manage access to them)
- **A.5.10 (Acceptable Use)**: Users must acknowledge AUP before receiving access
- **A.5.14 (Secure Information Transfer)**: Privileged access credentials must be transferred securely

### Downstream Dependencies

**IAM controls (A.5.15/16/18) feed into**:

- **A.8.2-3-5 (Authentication-Privileged-Access)**: IAM creates users → Authentication authenticates them
- **A.8.16 (Monitoring)**: User activity must be monitored (IAM defines who users are)
- **A.5.7 (Threat Intelligence)**: Compromised credentials from threat intel (IAM must revoke)
- **A.5.24-27 (Incident Management)**: Account compromise incidents (IAM must respond)

### Dashboard Benefits for Other Controls

This IAM dashboard provides valuable metrics for:

- **Internal Audit**: Evidence of IAM governance maturity
- **Compliance**: Regulatory compliance (FINMA, GDPR, NIS2)
- **Risk Management**: IAM risk assessment (low RBAC adoption = high risk)
- **Executive Management**: Strategic IAM planning and investment decisions

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Workbook Metadata

| Attribute | Value |
|-----------|-------|
| **Filename** | ISMS-IMP-A.5.15-16-18.S5_Dashboard_YYYY-MM.xlsx |
| **Total Sheets** | 10 |
| **File Format** | Excel Workbook (.xlsx) |
| **Excel Version** | Excel 2016 or later (cross-workbook formulas) |
| **Macros** | None (formulas only) |
| **External Links** | Yes (links to IMP.1, IMP.2, IMP.3, IMP.4) |

### Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|-----------|---------|-------------|
| 1 | Instructions_and_Legend | Document control, data sources, refresh procedures | 60 |
| 2 | Executive_Summary_Dashboard | One-page executive view (main dashboard) | 80 |
| 3 | Identity_Lifecycle_Metrics | Lifecycle metrics from IMP.1 | 40 |
| 4 | Access_Rights_Metrics | Access rights metrics from IMP.2 | 40 |
| 5 | Access_Review_Metrics | Review metrics from IMP.3 | 40 |
| 6 | Role_and_SoD_Metrics | RBAC and SoD metrics from IMP.4 | 40 |
| 7 | Consolidated_Gap_Analysis | All gaps from 4 assessments | 42-82 (40-80 gaps) |
| 8 | Compliance_Scoring_Matrix | Control scores and overall maturity | 50 |
| 9 | Evidence_Summary | Evidence count by assessment | 30 |
| 10 | Approval_and_Sign_Off | Monthly/Quarterly/Annual approval | 80 |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions_and_Legend

**Purpose**: Document control, data sources, how to use dashboard

**Layout**:
- **Rows 1-15**: Document Control
- **Rows 17-30**: Dashboard Overview
- **Rows 32-50**: Data Source Registry
- **Rows 52-70**: Refresh Procedures
- **Rows 72-85**: Maturity Rating Scale

#### Document Control Section (Rows 1-15)

| Cell | Label | Value | Format |
|------|-------|-------|--------|
| A1 | Title | "ISMS-IMP-A.5.15-16-18.S5 - IAM Governance Compliance Dashboard" | Bold, 14pt, Navy |
| A3 | Document ID | "ISMS-IMP-A.5.15-16-18.S5" | Normal |
| A4 | Version | "1.0" | Normal |
| A5 | Assessment Period | "[Start Date] to [End Date]" | Date format |
| A6 | Prepared By | "[Name, Title]" | Normal |
| A7 | Preparation Date | [Date] | Date format |
| A8 | Last Refresh Date | [Date] | Date format |
| A9 | Next Review | [Date] (Monthly/Quarterly/Annual) | Date format |
| A10 | Status | Dropdown: Draft, In Review, Approved | Conditional format |

#### Data Source Registry (Rows 32-50)

| Row | Source Assessment | Filename | Sheet Referenced | Location |
|-----|------------------|----------|------------------|----------|
| 33 | IMP.1 (User Inventory) | `ISMS-IMP-A.5.15-16-18.S1_UserInventory_YYYY-MM.xlsx` | Lifecycle_Compliance_Dashboard (Sheet 7) | Same folder |
| 34 | IMP.2 (Access Rights) | `ISMS-IMP-A.5.15-16-18.S2_AccessRights_YYYY-MM.xlsx` | Access_Rights_Dashboard (Sheet 7) | Same folder |
| 35 | IMP.3 (Access Review) | `ISMS-IMP-A.5.15-16-18.S3_AccessReview_YYYY-MM.xlsx` | Review_Compliance_Dashboard (Sheet 6) | Same folder |
| 36 | IMP.4 (Role & SoD) | `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx` | RBAC_Metrics (Sheet 7) | Same folder |

#### Refresh Procedures (Rows 52-70)

**Steps to Update Dashboard**:
1. Complete all 4 source assessments (IMP.1, IMP.2, IMP.3, IMP.4) for current month
2. Ensure all 4 source files approved (CISO sign-off)
3. Save all 5 files (4 sources + dashboard) in same folder
4. Open all 5 files simultaneously
5. In dashboard file: Data → Refresh All (update all cross-workbook links)
6. Verify all metrics populated (no #REF errors)
7. Update Sheet 7 (Consolidated Gap Analysis): Status, new gaps
8. Review Sheet 2 (Executive Summary Dashboard): Key findings, recommended actions
9. Save dashboard
10. Schedule monthly IAM governance meeting

#### Maturity Rating Scale (Rows 72-85)

| Score Range | Rating | Description | Color Code |
|-------------|--------|-------------|------------|
| 90-100 | Excellent | World-class IAM governance, minimal gaps | Dark Green |
| 80-89 | Very Good | Strong IAM governance, minor gaps | Light Green |
| 70-79 | Good | Solid IAM governance, some improvements needed | Yellow |
| 60-69 | Fair | Basic IAM governance, significant gaps | Orange |
| <60 | Poor | Weak IAM governance, major gaps | Red |

---

### Sheet 2: Executive_Summary_Dashboard

**Purpose**: One-page executive view (main dashboard)

**Layout**: 
- Designed to fit on ONE PAGE (print or PDF)
- Heavy use of conditional formatting (color-coded)
- Mix of metrics (numbers) and visuals (charts)
- Executive-friendly language (no jargon)

#### Section 1: Overall IAM Maturity Score (Rows 1-10, Columns A-F)

**Layout**:
```
┌─────────────────────────────────────────────┐
│  Overall IAM Maturity Score                │
│         82                                  │
│    [Very Good]                             │
└─────────────────────────────────────────────┘
```

| Cell | Content | Formula | Format |
|------|---------|---------|--------|
| A1-F1 | "Overall IAM Maturity Score" | Merged cell | Bold, 18pt, Navy, Center |
| A3-F3 | Score (0-100) | `=Compliance_Scoring_Matrix!B40` | Bold, 48pt, Center, CF: Green >= 80, Yellow 60-79, Red < 60 |
| A5-F5 | Rating | `=Compliance_Scoring_Matrix!B42` | Bold, 18pt, Center, CF: Green = Excellent/Very Good, Yellow = Good/Fair, Red = Poor |

**Conditional Formatting** (Cell A3-F3):
```
Rule 1: =A3>=80
Format: Dark Green background, White text

Rule 2: =AND(A3>=60, A3<80)
Format: Yellow background, Black text

Rule 3: =A3<60
Format: Red background, White text
```

#### Section 2: Control-Specific Scores (Rows 12-20, Columns A-F)

**Layout**:
```
┌────────────┬────────────┬────────────┐
│  A.5.15    │  A.5.16    │  A.5.18    │
│    78      │    92      │    85      │
│ [Good]     │ [Excellent]│ [Very Good]│
└────────────┴────────────┴────────────┘
```

| Cell Range | Control | Score Formula | Rating Formula | Format |
|------------|---------|---------------|----------------|--------|
| A12-B12 | "A.5.15 Access Control" | `=Compliance_Scoring_Matrix!B10` | `=IF(A13>=90,"Excellent",IF(A13>=80,"Very Good",IF(A13>=70,"Good",IF(A13>=60,"Fair","Poor"))))` | Bold, 14pt |
| A13-B13 | Score | Formula | - | Bold, 24pt, CF based on value |
| A14-B14 | Rating | - | Formula | Bold, 12pt, CF based on rating |
| C12-D12 | "A.5.16 Identity Management" | `=Compliance_Scoring_Matrix!B20` | Similar | Bold, 14pt |
| C13-D13 | Score | Formula | - | Bold, 24pt, CF based on value |
| C14-D14 | Rating | - | Formula | Bold, 12pt, CF based on rating |
| E12-F12 | "A.5.18 Access Rights" | `=Compliance_Scoring_Matrix!B30` | Similar | Bold, 14pt |
| E13-F13 | Score | Formula | - | Bold, 24pt, CF based on value |
| E14-F14 | Rating | - | Formula | Bold, 12pt, CF based on rating |

#### Section 3: Critical Gaps Indicator (Rows 12-20, Columns G-H)

**Layout**:
```
┌──────────────────┐
│ Critical Gaps    │
│       1          │
│   🚨 ACTION     │
└──────────────────┘
```

| Cell | Content | Formula | Format |
|------|---------|---------|--------|
| G12-H12 | "Critical Gaps" | Merged | Bold, 14pt, Navy |
| G13-H13 | Count | `=COUNTIF(Consolidated_Gap_Analysis!C:C,"Critical")` | Bold, 36pt, Red |
| G14-H14 | Indicator | `=IF(G13>0,"🚨 ACTION REQUIRED",IF(COUNTIF(Consolidated_Gap_Analysis!C:C,"High")>5,"⚠️ ATTENTION","✅ ACCEPTABLE"))` | Bold, 12pt, CF based on text |

#### Section 4: Key Metrics Grid (Rows 22-35, Columns A-F)

**Layout**:
```
┌────────────────────┬───────┬────────┬────────┐
│ Metric             │ Value │ Target │ Status │
├────────────────────┼───────┼────────┼────────┤
│ RBAC Adoption      │ 78%   │ >= 80% │ Yellow │
│ Lifecycle Complian │ 92%   │ >= 90% │ Green  │
│ Review Completion  │ 87%   │ >= 95% │ Yellow │
│ SoD Violations     │ 1     │ 0      │ Red    │
│ Orphaned Accounts  │ 3     │ 0      │ Red    │
│ Direct Access %    │ 22%   │ < 20%  │ Yellow │
└────────────────────┴───────┴────────┴────────┘
```

**Table Structure**:

| Row | Column A | Column B | Column C | Column D |
|-----|----------|----------|----------|----------|
| 22 | "Metric" | "Value" | "Target" | "Status" |
| 23 | "RBAC Adoption" | `=Role_and_SoD_Metrics!B7` | ">= 80%" | `=IF(B23>=0.8,"Green",IF(B23>=0.6,"Yellow","Red"))` |
| 24 | "Lifecycle Compliance" | `=Identity_Lifecycle_Metrics!B60` | ">= 90%" | `=IF(B24>=0.9,"Green",IF(B24>=0.8,"Yellow","Red"))` |
| 25 | "Review Completion" | `=Access_Review_Metrics!B7` | ">= 95%" | `=IF(B25>=0.95,"Green",IF(B25>=0.85,"Yellow","Red"))` |
| 26 | "SoD Violations (Unresolved)" | `=Role_and_SoD_Metrics!B46` | "0" | `=IF(B26=0,"Green","Red")` |
| 27 | "Orphaned Accounts" | `=Identity_Lifecycle_Metrics!B8` | "0" | `=IF(B27=0,"Green",IF(B27<=5,"Yellow","Red"))` |
| 28 | "Direct Access %" | `=Direct_Access_Users!A47/100` | "< 20%" | `=IF(B28<0.2,"Green",IF(B28<0.3,"Yellow","Red"))` |

**Conditional Formatting** (Column D):
```
Rule 1: =D23="Green"
Format: Green background, White text

Rule 2: =D23="Yellow"
Format: Yellow background, Black text

Rule 3: =D23="Red"
Format: Red background, White text
```

#### Section 5: Trend Charts (Rows 22-50, Columns G-N)

**Chart 1: Overall IAM Maturity Trend (Rows 22-35, Columns G-J)**
- **Chart Type**: Line chart
- **X-Axis**: Month (last 6 months)
- **Y-Axis**: Maturity Score (0-100)
- **Data Source**: Historical_Trends table (Rows 80-90)
- **Title**: "IAM Maturity Trend (6 Months)"

**Chart 2: Control-Specific Trends (Rows 22-35, Columns K-N)**
- **Chart Type**: Multi-line chart
- **X-Axis**: Month (last 6 months)
- **Y-Axis**: Control Score (0-100)
- **Lines**: A.5.15 (Blue), A.5.16 (Green), A.5.18 (Orange)
- **Data Source**: Historical_Trends table
- **Title**: "Control Scores Trend"

**Chart 3: Gap Count Trend (Rows 37-50, Columns G-J)**
- **Chart Type**: Stacked column chart
- **X-Axis**: Month (last 6 months)
- **Y-Axis**: Gap Count
- **Series**: Critical (Red), High (Orange), Medium (Yellow), Low (Green)
- **Data Source**: Historical_Gaps table (Rows 92-98)
- **Title**: "Gap Count by Severity"

**Historical Trends Table** (Hidden, Rows 80-90):

| Row | Month | Overall Maturity | A.5.15 | A.5.16 | A.5.18 |
|-----|-------|-----------------|--------|--------|--------|
| 81 | May-25 | 72 | 68 | 80 | 75 |
| 82 | Jun-25 | 75 | 72 | 85 | 78 |
| 83 | Jul-25 | 77 | 74 | 88 | 80 |
| 84 | Aug-25 | 79 | 76 | 90 | 82 |
| 85 | Sep-25 | 81 | 77 | 91 | 84 |
| 86 | Oct-25 | 82 | 78 | 92 | 85 |

**Note**: Initial dashboard (Month 1) will have only 1 data point. Trends populate as monthly data accumulates.

#### Section 6: Key Findings (Rows 37-50, Columns K-N)

**Layout** (Text box or merged cells):
```
┌──────────────────────────────────────┐
│ Key Findings (Current Month)         │
│                                      │
│ • RBAC adoption increased 7% MoM    │
│ • 2 critical SoD violations         │
│   remediated                        │
│ • Orphaned accounts reduced from 8  │
│   to 3                              │
│ • Access review completion improved │
│   from 81% to 87%                   │
│ • 1 remaining SoD violation requires│
│   CISO decision                      │
└──────────────────────────────────────┘
```

| Cell Range | Content | Format |
|-----------|---------|--------|
| K37-N50 | Key Findings (5 bullet points) | Manual entry, Bullet format, 11pt, Wrap text |

**Instructions for Completing**:
1. Review control scores (A.5.15, A.5.16, A.5.18)
2. Identify top 3-5 changes month-over-month
3. Write 5 bullet points (1-2 sentences each)
4. Focus on: Improvements, Remaining gaps, Notable changes

#### Section 7: Recommended Actions (Rows 52-65, Columns A-F)

**Layout**:
```
┌──────────────────────────────────────┐
│ Recommended Actions (Next Month)     │
│                                      │
│ 1. Remediate remaining SoD violation │
│    (User123) - Target: Nov 15        │
│ 2. Create 3 new roles (Sales,       │
│    Support, Marketing) to increase  │
│    RBAC adoption to 85%              │
│ 3. Complete 5 overdue access reviews│
│    (ERP, CRM, File Shares, Email,   │
│    VPN)                              │
│ 4. Remediate 3 orphaned accounts    │
│    (disable or justify)              │
│ 5. Schedule role review meetings    │
│    with Finance, HR, Engineering    │
└──────────────────────────────────────┘
```

| Cell Range | Content | Format |
|-----------|---------|--------|
| A52-F65 | Recommended Actions (5 priorities) | Manual entry, Numbered list, 11pt, Wrap text |

**Instructions for Completing**:
1. Review Sheet 7 (Consolidated Gap Analysis)
2. Identify top 5 priorities (by severity and impact)
3. Write 5 numbered action items
4. Each action: What to do, Why, Target date (if applicable)

#### Section 8: Executive Summary (Rows 52-65, Columns G-N)

**Layout** (Text box or merged cells):
```
┌──────────────────────────────────────────────────────────────┐
│ Executive Summary (CISO Presentation)                       │
│                                                             │
│ [Paragraph 1: Overall Assessment]                          │
│ BitHawk's IAM maturity score is 82 (Very Good), reflecting │
│ strong progress in identity lifecycle management (92) and  │
│ access rights governance (85). Access control maturity (78)│
│ remains an area for improvement due to RBAC adoption below │
│ target.                                                     │
│                                                             │
│ [Paragraph 2: Key Improvements This Month]                 │
│ Significant improvements include RBAC adoption increasing  │
│ 7% month-over-month to 78%, 2 critical SoD violations     │
│ remediated, orphaned accounts reduced from 8 to 3, and    │
│ access review completion improved from 81% to 87%.         │
│                                                             │
│ [Paragraph 3: Remaining Gaps]                              │
│ One critical SoD violation remains (User123 with Developer │
│ + Production Admin roles), requiring CISO decision on      │
│ justification vs. remediation. RBAC adoption (78%) remains │
│ below target (80%), with 22 users still on direct access. │
│ Three orphaned accounts require investigation.              │
│                                                             │
│ [Paragraph 4: Next Steps]                                  │
│ Priority actions for next month include remediating the    │
│ remaining SoD violation, creating 3 new roles to increase  │
│ RBAC adoption, completing 5 overdue access reviews, and   │
│ scheduling role review meetings with Finance, HR, and      │
│ Engineering. Target: 85 maturity score by December 2025.   │
└──────────────────────────────────────────────────────────────┘
```

| Cell Range | Content | Format |
|-----------|---------|--------|
| G52-N65 | Executive Summary (3-4 paragraphs) | Manual entry, Paragraph format, 11pt, Wrap text |

**Instructions for Completing**:
1. **Paragraph 1**: Overall IAM maturity, control scores, high-level assessment
2. **Paragraph 2**: Key improvements this month (3-5 highlights)
3. **Paragraph 3**: Remaining gaps (critical and high priority)
4. **Paragraph 4**: Next steps (top 5 priorities, target maturity score)

**Total Executive Summary Length**: 3-4 paragraphs, ~300-400 words

---

### Sheet 3: Identity_Lifecycle_Metrics

**Purpose**: Lifecycle compliance metrics from IMP.1

**Data Source**: `ISMS-IMP-A.5.15-16-18.S1_UserInventory_YYYY-MM.xlsx` Sheet 7 (Lifecycle_Compliance_Dashboard)

**Column Structure**:

| Row | Metric | Formula (Cross-Workbook Link) | Format |
|-----|--------|-------------------------------|--------|
| 1 | **Identity Lifecycle Metrics (A.5.16)** | Header | Bold, 14pt, Navy |
| 2 | Data Source | `ISMS-IMP-A.5.15-16-18.S1_UserInventory_YYYY-MM.xlsx` | Italic |
| 3 | Assessment Period | `='[...1_UserInventory...]'!Instructions!B5` | Date |
| 5 | Total Users (Active) | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B4` | Number |
| 6 | Provisioning Compliance Rate (%) | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B20` | Percent |
| 7 | Provisioning On-Time Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B18` | Number |
| 8 | Provisioning Late Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B19` | Number |
| 10 | Deprovisioning Compliance Rate (%) | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B30` | Percent |
| 11 | Deprovisioning On-Time Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B28` | Number |
| 12 | Deprovisioning Late Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B29` | Number |
| 14 | Orphaned Account Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B35` | Number |
| 15 | Inactive Account Count (90+ days) | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B36` | Number |
| 17 | Contractor Account Count | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B40` | Number |
| 18 | Contractor Accounts Expired | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B41` | Number |
| 20 | **Lifecycle Maturity Score (0-100)** | `='[...1_UserInventory...]'!Lifecycle_Compliance_Dashboard'!B60` | Bold, Number, CF |

**Conditional Formatting** (Row 20, Column B - Lifecycle Maturity Score):
```
Rule 1: =B20>=90
Format: Dark Green background, White text

Rule 2: =AND(B20>=80, B20<90)
Format: Light Green background, Black text

Rule 3: =AND(B20>=70, B20<80)
Format: Yellow background, Black text

Rule 4: =B20<70
Format: Red background, White text
```

**Cross-Workbook Formula Example**:
```
='[ISMS-IMP-A.5.15-16-18.S1_UserInventory_2025-10.xlsx]Lifecycle_Compliance_Dashboard'!B60
```

**Notes**:
- Formula references full workbook filename (including path if different folder)
- Excel requires source workbook to be open for formulas to update
- Data → Refresh All updates all cross-workbook links
- If source file moves: Data → Edit Links → Update file path

---

### Sheet 4: Access_Rights_Metrics

**Purpose**: Access rights metrics from IMP.2

**Data Source**: `ISMS-IMP-A.5.15-16-18.S2_AccessRights_YYYY-MM.xlsx` Sheet 7 (Access_Rights_Dashboard)

**Column Structure**:

| Row | Metric | Formula (Cross-Workbook Link) | Format |
|-----|--------|-------------------------------|--------|
| 1 | **Access Rights Metrics (A.5.18)** | Header | Bold, 14pt, Navy |
| 2 | Data Source | `ISMS-IMP-A.5.15-16-18.S2_AccessRights_YYYY-MM.xlsx` | Italic |
| 3 | Assessment Period | `='[...2_AccessRights...]'!Instructions!B5` | Date |
| 5 | Total Access Grants | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B4` | Number |
| 6 | Users with Access | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B5` | Number |
| 7 | Systems with Access Managed | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B6` | Number |
| 9 | Access by Data Sensitivity | | Bold |
| 10 | - Restricted Access Grants | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B10` | Number |
| 11 | - Confidential Access Grants | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B11` | Number |
| 12 | - Internal Access Grants | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B12` | Number |
| 13 | - Public Access Grants | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B13` | Number |
| 15 | Privileged Access Count | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B16` | Number |
| 16 | Contractor/Vendor Access Count | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B17` | Number |
| 18 | Access Rights Documentation Completeness (%) | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B25` | Percent |
| 19 | - Access with Business Justification | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B21` | Number |
| 20 | - Access with Approver Documented | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B22` | Number |
| 22 | **Access Rights Score (0-100)** | `='[...2_AccessRights...]'!Access_Rights_Dashboard'!B40` | Bold, Number, CF |

**Conditional Formatting** (Row 22, Column B - Access Rights Score):
```
Similar to Sheet 3 (Green >= 90, Light Green 80-89, Yellow 70-79, Red < 70)
```

---

### Sheet 5: Access_Review_Metrics

**Purpose**: Access review metrics from IMP.3

**Data Source**: `ISMS-IMP-A.5.15-16-18.S3_AccessReview_YYYY-MM.xlsx` Sheet 6 (Review_Compliance_Dashboard)

**Column Structure**:

| Row | Metric | Formula (Cross-Workbook Link) | Format |
|-----|--------|-------------------------------|--------|
| 1 | **Access Review Metrics (A.5.15 + A.5.18)** | Header | Bold, 14pt, Navy |
| 2 | Data Source | `ISMS-IMP-A.5.15-16-18.S3_AccessReview_YYYY-MM.xlsx` | Italic |
| 3 | Assessment Period | `='[...3_AccessReview...]'!Instructions!B5` | Date |
| 5 | Total Reviews Scheduled | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B4` | Number |
| 6 | Reviews Completed | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B5` | Number |
| 7 | Review Completion Rate (%) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B7` | Percent |
| 9 | Overdue Reviews | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B10` | Number |
| 10 | Reviews In Progress | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B11` | Number |
| 12 | Review Findings | | Bold |
| 13 | - Users Reviewed | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B15` | Number |
| 14 | - Access Confirmed (Appropriate) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B16` | Number |
| 15 | - Access Removed (Inappropriate) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B17` | Number |
| 16 | - Access Justified (Documented Exception) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B18` | Number |
| 18 | Access Removal Rate (%) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B22` | Percent |
| 20 | Reviewer Accountability (%) | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B30` | Percent |
| 21 | - Reviewers Completed On-Time | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B28` | Number |
| 22 | - Reviewers Overdue | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B29` | Number |
| 24 | **Review Compliance Score (0-100)** | `='[...3_AccessReview...]'!Review_Compliance_Dashboard'!B50` | Bold, Number, CF |

---

### Sheet 6: Role_and_SoD_Metrics

**Purpose**: RBAC and SoD metrics from IMP.4

**Data Source**: `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx` Sheet 7 (RBAC_Metrics)

**Column Structure**:

| Row | Metric | Formula (Cross-Workbook Link) | Format |
|-----|--------|-------------------------------|--------|
| 1 | **Role & SoD Metrics (A.5.15 + A.5.18)** | Header | Bold, 14pt, Navy |
| 2 | Data Source | `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx` | Italic |
| 3 | Assessment Period | `='[...4_RoleCompliance...]'!Instructions!B5` | Date |
| 5 | Total Users | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B4` | Number |
| 6 | Users with Roles | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B5` | Number |
| 7 | RBAC Adoption Rate (%) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B7` | Percent |
| 9 | Role Usage | | Bold |
| 10 | - Total Roles (Active) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B33` | Number |
| 11 | - Obsolete Roles | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B34` | Number |
| 12 | - Average Roles per User | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B31` | Number, 2 decimals |
| 14 | SoD Violations | | Bold |
| 15 | - Total Violations Detected | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B45` | Number |
| 16 | - Unresolved Violations | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B46` | Number, CF: Red if > 0 |
| 17 | - Justified Violations (with Controls) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B47` | Number |
| 18 | - Remediated Violations | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B48` | Number |
| 20 | SoD Compliance Rate (%) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B50` | Percent |
| 22 | Role Review Compliance | | Bold |
| 23 | - Total Roles | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B60` | Number |
| 24 | - Roles Reviewed (Last 12 Months) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B61` | Number |
| 25 | - Role Review Compliance (%) | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B62` | Percent |
| 27 | **RBAC Maturity Score (0-100)** | `='[...4_RoleCompliance...]'!RBAC_Metrics'!B80` | Bold, Number, CF |

**Conditional Formatting** (Row 16 - Unresolved SoD Violations):
```
Rule 1: =B16>0
Format: Red background, White text (Critical: unresolved violations)

Rule 2: =B16=0
Format: Green background, White text (Compliant: zero violations)
```

---

### Sheet 7: Consolidated_Gap_Analysis

**Purpose**: All gaps from 4 assessments prioritized by risk

**Data Sources**:
- IMP.1 Sheet 8 (Gap Analysis)
- IMP.2 Sheet 8 (Gap Analysis)
- IMP.3 Sheet 7 (Gap Analysis)
- IMP.4 Sheet 8 (Gap Analysis)

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | Gap_ID | Text | 15 | Copied from source assessments | None |
| B | Source_Assessment | Text | 12 | Manual: IMP.1, IMP.2, IMP.3, IMP.4 | None |
| C | Severity | Text | 12 | Copied from source | Red = Critical/High, Orange = Medium |
| D | Gap_Type | Text | 25 | Copied from source | None |
| E | Description | Text | 40 | Copied from source | None |
| F | Current_State | Text | 25 | Copied from source | None |
| G | Target_State | Text | 25 | Copied from source | None |
| H | Owner | Text | 20 | Copied from source | Red if blank |
| I | Remediation_Plan | Text | 40 | Copied from source | Red if blank |
| J | Target_Date | Date | 15 | Copied from source | Red if past and Status = Open |
| K | Status | Dropdown | 15 | Updated monthly | Red = Open, Yellow = In Progress, Green = Closed |
| L | Audit_Impact | Text | 15 | Copied from source | Red = Finding, Yellow = Observation |

**How to Populate**:

1. **Phase 1: Initial Setup (First Time)**
   - Copy all gaps from IMP.1 Sheet 8 (Gap Analysis), rows 2-X
   - Paste starting at Row 2 in this sheet
   - Add "IMP.1" in Column B (Source_Assessment)
   - Copy all gaps from IMP.2 Sheet 8, append below IMP.1 gaps
   - Add "IMP.2" in Column B
   - Copy all gaps from IMP.3 Sheet 7, append below IMP.2 gaps
   - Add "IMP.3" in Column B
   - Copy all gaps from IMP.4 Sheet 8, append below IMP.3 gaps
   - Add "IMP.4" in Column B
   - Sort by Column C (Severity): Critical → High → Medium → Low

2. **Phase 2: Monthly Updates**
   - Review all gaps (Rows 2-X)
   - Update Column K (Status): Open → In Progress → Closed
   - Add new gaps from monthly assessments (if any)
   - Remove duplicate gaps (same gap, multiple assessments)
   - Re-sort by Severity if new gaps added

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Gaps | `=COUNTA(A2:A81)-COUNTIF(A2:A81,"")` | Cell A83 |
| Critical Gaps | `=COUNTIF(C2:C81,"Critical")` | Cell A84 |
| High Gaps | `=COUNTIF(C2:C81,"High")` | Cell A85 |
| Medium Gaps | `=COUNTIF(C2:C81,"Medium")` | Cell A86 |
| Low Gaps | `=COUNTIF(C2:C81,"Low")` | Cell A87 |
| Open Gaps | `=COUNTIF(K2:K81,"Open")` | Cell A88 |
| In Progress Gaps | `=COUNTIF(K2:K81,"In Progress")` | Cell A89 |
| Closed Gaps | `=COUNTIF(K2:K81,"Closed")` | Cell A90 |
| Gap Closure Rate (%) | `=(A90/A83)*100` | Cell A91 |
| Overdue Gaps | `=COUNTIFS(J2:J81,"<"&TODAY(), K2:K81,"<>Closed")` | Cell A92 |

**Conditional Formatting Rules**:

1. **Column C (Severity)**:
   ```
   Rule 1: =OR(C2="Critical", C2="High")
   Format: Red text, Red background
   
   Rule 2: =C2="Medium"
   Format: Orange text, Yellow background
   
   Rule 3: =C2="Low"
   Format: Black text
   ```

2. **Column K (Status)**:
   ```
   Rule 1: =K2="Open"
   Format: Red background, White text
   
   Rule 2: =K2="In Progress"
   Format: Yellow background, Black text
   
   Rule 3: =K2="Closed"
   Format: Green background, White text
   ```

3. **Column J (Target_Date)**:
   ```
   Rule 1: =AND(J2<TODAY(), K2<>"Closed")
   Format: Red background (overdue)
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2

---

### Sheet 8: Compliance_Scoring_Matrix

**Purpose**: Calculate control-specific scores and overall IAM maturity

**Layout**:
- **Rows 1-15**: A.5.15 (Access Control) Score Calculation
- **Rows 17-30**: A.5.16 (Identity Management) Score Calculation
- **Rows 32-45**: A.5.18 (Access Rights) Score Calculation
- **Rows 47-60**: Overall IAM Maturity Score Calculation
- **Rows 62-75**: Benchmark Comparisons

#### A.5.15 Score Calculation (Rows 1-15)

| Row | Component | Formula | Weight | Format |
|-----|-----------|---------|--------|--------|
| 1 | **A.5.15 - Access Control** | Header | | Bold, 14pt, Navy |
| 3 | Access Review Completion (%) | `=Access_Review_Metrics!B7` | 50% | Percent |
| 4 | SoD Compliance Rate (%) | `=Role_and_SoD_Metrics!B20` | 50% | Percent |
| 6 | **Component 1 (Review)** | `=B3*0.50` | | Number, 2 decimals |
| 7 | **Component 2 (SoD)** | `=B4*0.50` | | Number, 2 decimals |
| 9 | **A.5.15 Score (0-100)** | `=B6+B7` | | Bold, Number, 1 decimal, CF |
| 11 | Rating | `=IF(B9>=90,"Excellent",IF(B9>=80,"Very Good",IF(B9>=70,"Good",IF(B9>=60,"Fair","Poor"))))` | | Bold, CF based on rating |

**Conditional Formatting** (Row 9, Column B):
```
Rule 1: =B9>=80
Format: Green background, White text

Rule 2: =AND(B9>=60, B9<80)
Format: Yellow background, Black text

Rule 3: =B9<60
Format: Red background, White text
```

#### A.5.16 Score Calculation (Rows 17-30)

| Row | Component | Formula | Weight | Format |
|-----|-----------|---------|--------|--------|
| 17 | **A.5.16 - Identity Management** | Header | | Bold, 14pt, Navy |
| 19 | Lifecycle Maturity Score | `=Identity_Lifecycle_Metrics!B20` | 100% | Number, 1 decimal |
| 21 | **A.5.16 Score (0-100)** | `=B19` | | Bold, Number, 1 decimal, CF |
| 23 | Rating | `=IF(B21>=90,"Excellent",IF(B21>=80,"Very Good",IF(B21>=70,"Good",IF(B21>=60,"Fair","Poor"))))` | | Bold, CF based on rating |

**Note**: A.5.16 score = Lifecycle Maturity Score (directly from IMP.1)

#### A.5.18 Score Calculation (Rows 32-45)

| Row | Component | Formula | Weight | Format |
|-----|-----------|---------|--------|--------|
| 32 | **A.5.18 - Access Rights** | Header | | Bold, 14pt, Navy |
| 34 | Access Rights Documentation (%) | `=Access_Rights_Metrics!B18` | 30% | Percent |
| 35 | Access Review Completion (%) | `=Access_Review_Metrics!B7` | 35% | Percent |
| 36 | RBAC Adoption Rate (%) | `=Role_and_SoD_Metrics!B7` | 35% | Percent |
| 38 | **Component 1 (Documentation)** | `=B34*0.30` | | Number, 2 decimals |
| 39 | **Component 2 (Review)** | `=B35*0.35` | | Number, 2 decimals |
| 40 | **Component 3 (RBAC)** | `=B36*0.35` | | Number, 2 decimals |
| 42 | **A.5.18 Score (0-100)** | `=B38+B39+B40` | | Bold, Number, 1 decimal, CF |
| 44 | Rating | `=IF(B42>=90,"Excellent",IF(B42>=80,"Very Good",IF(B42>=70,"Good",IF(B42>=60,"Fair","Poor"))))` | | Bold, CF based on rating |

#### Overall IAM Maturity Score (Rows 47-60)

| Row | Component | Formula | Weight | Format |
|-----|-----------|---------|--------|--------|
| 47 | **Overall IAM Maturity** | Header | | Bold, 14pt, Navy |
| 49 | A.5.15 Score | `=B9` | 30% | Number, 1 decimal |
| 50 | A.5.16 Score | `=B21` | 30% | Number, 1 decimal |
| 51 | A.5.18 Score | `=B42` | 40% | Number, 1 decimal |
| 53 | **Component 1 (A.5.15)** | `=B49*0.30` | | Number, 2 decimals |
| 54 | **Component 2 (A.5.16)** | `=B50*0.30` | | Number, 2 decimals |
| 55 | **Component 3 (A.5.18)** | `=B51*0.40` | | Number, 2 decimals |
| 57 | **Overall IAM Maturity Score (0-100)** | `=B53+B54+B55` | | Bold, 24pt, CF |
| 59 | Maturity Rating | `=IF(B57>=90,"Excellent",IF(B57>=80,"Very Good",IF(B57>=70,"Good",IF(B57>=60,"Fair","Poor"))))` | | Bold, 18pt, CF based on rating |

**Conditional Formatting** (Row 57, Column B - Overall Maturity):
```
Rule 1: =B57>=90
Format: Dark Green background, White text, Bold

Rule 2: =AND(B57>=80, B57<90)
Format: Light Green background, Black text, Bold

Rule 3: =AND(B57>=70, B57<80)
Format: Yellow background, Black text, Bold

Rule 4: =AND(B57>=60, B57<70)
Format: Orange background, Black text, Bold

Rule 5: =B57<60
Format: Red background, White text, Bold
```

#### Benchmark Comparisons (Rows 62-75)

| Row | Metric | Excellent | Very Good | Good | Fair | Poor | Actual | Format |
|-----|--------|-----------|-----------|------|------|------|--------|--------|
| 63 | **Benchmark Comparisons** | Header | | | | | | Bold, 14pt |
| 65 | Overall Maturity | >= 90 | 80-89 | 70-79 | 60-69 | < 60 | `=B57` | Number, CF |
| 66 | A.5.15 (Access Control) | >= 90 | 80-89 | 70-79 | 60-69 | < 60 | `=B9` | Number, CF |
| 67 | A.5.16 (Identity Mgmt) | >= 90 | 80-89 | 70-79 | 60-69 | < 60 | `=B21` | Number, CF |
| 68 | A.5.18 (Access Rights) | >= 90 | 80-89 | 70-79 | 60-69 | < 60 | `=B42` | Number, CF |

**Conditional Formatting** (Column G - Actual Values):
```
Rule 1: =G65>=90
Format: Dark Green background

Rule 2: =AND(G65>=80, G65<90)
Format: Light Green background

Rule 3: =AND(G65>=70, G65<80)
Format: Yellow background

Rule 4: =AND(G65>=60, G65<70)
Format: Orange background

Rule 5: =G65<60
Format: Red background
```

---

### Sheet 9: Evidence_Summary

**Purpose**: Evidence count by assessment and audit readiness

**Column Structure**:

| Row | Metric | Formula/Data Source | Format |
|-----|--------|-------------------|--------|
| 1 | **Evidence Summary** | Header | Bold, 14pt, Navy |
| 3 | **Evidence Count by Assessment** | Subheader | Bold, 12pt |
| 4 | IMP.1 (User Inventory) Evidence | `='[...1_UserInventory...]'!Evidence_Register'!A33` | Number |
| 5 | IMP.2 (Access Rights) Evidence | `='[...2_AccessRights...]'!Evidence_Register'!A33` | Number |
| 6 | IMP.3 (Access Review) Evidence | `='[...3_AccessReview...]'!Evidence_Register'!A33` | Number |
| 7 | IMP.4 (Role & SoD) Evidence | `='[...4_RoleCompliance...]'!Evidence_Register'!A33` | Number |
| 8 | **Total Evidence Items** | `=SUM(B4:B7)` | Bold, Number |
| 10 | **Evidence by Type** | Subheader | Bold, 12pt |
| 11 | Documents | `=SUMIF([all assessments Evidence_Type],"Document")` | Number |
| 12 | Exports | `=SUMIF([all assessments Evidence_Type],"Export")` | Number |
| 13 | Screenshots | `=SUMIF([all assessments Evidence_Type],"Screenshot")` | Number |
| 14 | Emails | `=SUMIF([all assessments Evidence_Type],"Email")` | Number |
| 15 | Approvals | `=SUMIF([all assessments Evidence_Type],"Approval")` | Number |
| 16 | Meeting Minutes | `=SUMIF([all assessments Evidence_Type],"Meeting Minutes")` | Number |
| 18 | **Evidence by Control** | Subheader | Bold, 12pt |
| 19 | A.5.15 (Access Control) | `=COUNTIF([all assessments Audit_Relevance],"A.5.15")` | Number |
| 20 | A.5.16 (Identity Management) | `=COUNTIF([all assessments Audit_Relevance],"A.5.16")` | Number |
| 21 | A.5.18 (Access Rights) | `=COUNTIF([all assessments Audit_Relevance],"A.5.18")` | Number |
| 23 | **Audit Readiness Checklist** | Subheader | Bold, 12pt |
| 24 | All evidence accessible? | Dropdown: Yes, No, Partial | CF: Green = Yes, Red = No |
| 25 | Evidence recent (within assessment period)? | Dropdown: Yes, No, Partial | CF: Green = Yes, Red = No |
| 26 | Evidence retention documented? | Dropdown: Yes, No, Partial | CF: Green = Yes, Red = No |
| 27 | Evidence categorized by control? | Dropdown: Yes, No, Partial | CF: Green = Yes, Red = No |
| 28 | Evidence count >= 60 (15+ per assessment)? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 30 | **Audit Readiness Status** | `=IF(COUNTIF(B24:B28,"No")>0,"NOT READY",IF(COUNTIF(B24:B28,"Partial")>0,"PARTIAL","READY"))` | Bold, 14pt, CF |

**Conditional Formatting** (Row 30, Column B - Audit Readiness):
```
Rule 1: =B30="READY"
Format: Green background, White text

Rule 2: =B30="PARTIAL"
Format: Yellow background, Black text

Rule 3: =B30="NOT READY"
Format: Red background, White text
```

---

### Sheet 10: Approval_and_Sign_Off

**Purpose**: Monthly, quarterly, and annual approval workflow

**Layout** (Similar to other assessments but adapted for dashboard):

#### Section 1: Monthly Dashboard Review (Rows 1-25) - IAM Team Lead

| Row | Field | Value/Formula | Format |
|-----|-------|---------------|--------|
| 1 | **Monthly Dashboard Review (IAM Team Lead)** | Header | Bold, 14pt, Navy |
| 3 | Reviewer Name | [Manual entry] | Normal |
| 4 | Reviewer Title | [Manual entry] | Normal |
| 5 | Review Date | [Date] | Date format |
| 7 | Data Accuracy Verified? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 8 | Key Findings Reasonable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 9 | Recommended Actions Prioritized? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 10 | Charts and Metrics Updated? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 12 | Comments/Feedback | [Manual entry] | Text, Wrap text |
| 16 | Approval Status | Dropdown: Approved, Revisions Required | CF: Green = Approved, Red = Revisions |
| 18 | Signature/Approval | [Manual entry] | Normal |
| 19 | Approval Date | [Date] | Date format |
| 21 | Next Monthly Review | [Date] (30 days from Approval Date) | Date format |

#### Section 2: Quarterly Executive Review (Rows 27-55) - CISO

| Row | Field | Value/Formula | Format |
|-----|-------|---------------|--------|
| 27 | **Quarterly Executive Review (CISO)** | Header | Bold, 14pt, Navy |
| 29 | Reviewer Name | [Manual entry] | Normal |
| 30 | Reviewer Title | [Manual entry] | Normal |
| 31 | Review Date | [Date] | Date format |
| 33 | Overall IAM Maturity Acceptable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 34 | Control Scores Acceptable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 35 | Critical Gaps Reviewed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 36 | Trend Improving? | Dropdown: Yes, No, Stable | CF: Green = Yes, Yellow = Stable, Red = No |
| 37 | Gap Remediation On Track? | Dropdown: Yes, No, Partial | CF: Green = Yes, Yellow = Partial, Red = No |
| 39 | Comments/Recommendations | [Manual entry] | Text, Wrap text |
| 43 | Approval Status | Dropdown: Approved, Revisions Required | CF: Green = Approved, Red = Revisions |
| 45 | Signature/Approval | [Manual entry] | Normal |
| 46 | Approval Date | [Date] | Date format |
| 48 | Next Quarterly Review | [Date] (90 days from Approval Date) | Date format |

#### Section 3: Annual Strategic Review (Rows 57-85) - Executive Management

| Row | Field | Value/Formula | Format |
|-----|-------|---------------|--------|
| 57 | **Annual Strategic Review (Executive Management)** | Header | Bold, 14pt, Navy |
| 59 | Reviewer Name | [Manual entry] | Normal |
| 60 | Reviewer Title | [Manual entry] | Normal |
| 61 | Review Date | [Date] | Date format |
| 63 | Annual IAM Maturity Trend Acceptable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 64 | Strategic Alignment Confirmed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 65 | Technology Investments Identified? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 66 | Budget Allocation Approved? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 67 | IAM Roadmap Approved? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 69 | Strategic Recommendations | [Manual entry] | Text, Wrap text |
| 73 | Approval Status | Dropdown: Approved, Revisions Required | CF: Green = Approved, Red = Revisions |
| 75 | Signature/Approval | [Manual entry] | Normal |
| 76 | Approval Date | [Date] | Date format |
| 78 | Next Annual Review | [Date] (365 days from Approval Date) | Date format |

---

## Cell Styling Reference

**Same color palette and styling as other IAM assessments (IMP.1-4)**

**Dashboard-Specific Styling**:

- **Large Numbers** (Overall Maturity Score): 48pt, Bold, Center-aligned
- **Control Scores**: 24pt, Bold, Center-aligned
- **Metric Values**: 18pt, Bold
- **Chart Titles**: 12pt, Bold, Navy
- **Executive Summary Text**: 11pt, Justified, Wrap text

---

## Freeze Panes Configuration

**All Sheets**:
- Freeze Panes: Row 2 (header row always visible)
- Exception: Sheet 2 (Executive Summary Dashboard) - No freeze panes (designed as single-page view)

---

## File Naming Convention

**Format**: `ISMS-IMP-A.5.15-16-18.S5_Dashboard_YYYY-MM.xlsx`

**Examples**:
- `ISMS-IMP-A.5.15-16-18.S5_Dashboard_2025-10.xlsx` (October 2025)
- `ISMS-IMP-A.5.15-16-18.S5_Dashboard_2026-Q1.xlsx` (Q1 2026 quarterly)
- `ISMS-IMP-A.5.15-16-18.S5_Dashboard_2025-Annual.xlsx` (2025 annual)

---

## Cross-Workbook Link Management

### Initial Setup

**Step 1: File Organization**
- Place all 5 files in same folder
- Use consistent naming: `ISMS-IMP-A.5.15-16-18.X_Name_YYYY-MM.xlsx`

**Step 2: Establish Links**
- Open all 5 files simultaneously
- In dashboard: Create formulas with cross-workbook references
- Example: `='[ISMS-IMP-A.5.15-16-18.S1_UserInventory_2025-10.xlsx]Lifecycle_Compliance_Dashboard'!B60`

**Step 3: Test Links**
- Data → Refresh All
- Verify all metrics populate (no #REF errors)
- Save dashboard

### Monthly Refresh Procedure

**Steps**:
1. Complete IMP.1, IMP.2, IMP.3, IMP.4 for current month
2. Ensure all 4 source files approved
3. Save all 4 source files (same folder as dashboard)
4. Open all 5 files (4 sources + dashboard)
5. In dashboard: Data → Refresh All
6. Verify all sheets populated correctly (Sheets 3-6)
7. Update Sheet 7 (Consolidated Gap Analysis)
8. Review Sheet 2 (Executive Summary Dashboard)
9. Save dashboard

### Troubleshooting Cross-Workbook Links

**Problem: #REF Errors**

**Causes**:
- Source file not in same folder
- Source file renamed
- Source file not open
- Sheet name changed in source file

**Solutions**:
1. Verify source files exist in same folder
2. Verify source file names match formula references
3. Open all source files
4. Data → Edit Links → Update Source (if file moved)
5. If sheet renamed: Find/Replace formula references

**Problem: Stale Data**

**Causes**:
- Links not refreshed
- Source files contain old data

**Solutions**:
1. Open all 5 files
2. Data → Refresh All
3. Verify source files contain current month data
4. Verify dates match assessment period

---

## Integration Points

### Data Flow

```
IMP.1 (User Inventory)       ─────┐
                                   │
IMP.2 (Access Rights Matrix) ─────┤
                                   ├──→ IMP.5 (Dashboard)
IMP.3 (Access Review Results)─────┤
                                   │
IMP.4 (Role & SoD Compliance)─────┘
```

### Key Metrics Flow

| Metric | Source Assessment | Source Sheet | Target Sheet (Dashboard) |
|--------|------------------|--------------|-------------------------|
| Lifecycle Maturity | IMP.1 | Lifecycle_Compliance_Dashboard (Sheet 7) | Sheet 3 (Identity_Lifecycle_Metrics) |
| Access Rights Score | IMP.2 | Access_Rights_Dashboard (Sheet 7) | Sheet 4 (Access_Rights_Metrics) |
| Review Compliance | IMP.3 | Review_Compliance_Dashboard (Sheet 6) | Sheet 5 (Access_Review_Metrics) |
| RBAC Maturity | IMP.4 | RBAC_Metrics (Sheet 7) | Sheet 6 (Role_and_SoD_Metrics) |
| All Gaps | IMP.1/2/3/4 | Gap_Analysis (Sheet 8/7) | Sheet 7 (Consolidated_Gap_Analysis) |

---

**END OF PART II: TECHNICAL SPECIFICATION**
