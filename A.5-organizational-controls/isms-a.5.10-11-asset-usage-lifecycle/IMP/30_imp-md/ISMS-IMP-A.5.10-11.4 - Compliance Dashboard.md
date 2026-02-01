# ISMS-IMP-A.5.10-11.4 — Compliance Dashboard

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.4 |
| **Title** | Asset Usage Lifecycle Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10-11 |
| **Control Name** | Asset Usage Lifecycle |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This dashboard workbook provides consolidated compliance monitoring for both A.5.10 (Acceptable Use) and A.5.11 (Return of Assets) controls. It aggregates metrics from the other assessment workbooks to provide executive-level visibility into asset usage lifecycle compliance.

**Scope**

This dashboard covers:
- Executive summary of compliance status
- A.5.10 compliance metrics and scoring
- A.5.11 compliance metrics and scoring
- Consolidated gap register
- Remediation tracking
- Trend analysis over time

**What This Dashboard Covers**

| Domain | Dashboard Focus |
|--------|-----------------|
| Executive Summary | High-level compliance overview |
| A.5.10 Compliance | Acceptable use metrics |
| A.5.11 Compliance | Asset return metrics |
| Gap Management | Consolidated gap tracking |
| Remediation | Action item progress |
| Trends | Historical compliance tracking |

**Control Requirements**

ISO 27001:2022 Controls A.5.10 and A.5.11 address the complete asset usage lifecycle from onboarding through offboarding. This dashboard tracks compliance with both controls in a unified view.

### Prerequisites

Before completing this dashboard:

- [ ] Completed ISMS-IMP-A.5.10-11.1 (Acceptable Use Policy Assessment)
- [ ] Completed ISMS-IMP-A.5.10-11.2 (Usage Rules Inventory)
- [ ] Completed ISMS-IMP-A.5.10-11.3 (Asset Return Assessment)
- [ ] Access to compliance metrics from underlying assessments
- [ ] Gap remediation status from responsible parties

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance and metadata | Complete document information |
| Executive_Summary | High-level overview | Enter KPIs, findings |
| A510_Compliance | Acceptable use scoring | Complete compliance checklist |
| A511_Compliance | Asset return scoring | Complete compliance checklist |
| Gap_Register | Consolidated gaps | Track all identified gaps |
| Remediation_Tracker | Action tracking | Monitor remediation progress |
| Trend_Analysis | Historical trends | Record periodic compliance |
| Approval_SignOff | Dashboard approval | Obtain sign-offs |

### Completion Walkthrough

**Step 1: Document Information (Instructions Sheet)**

Complete dashboard metadata including reporting period.

**Step 2: Executive Summary (Executive_Summary Sheet)**

Populate the key metrics section:

1. **Overall Compliance** - Combined score from A.5.10 and A.5.11
2. **A.5.10 Compliance** - Score from Acceptable Use assessment
3. **A.5.11 Compliance** - Score from Return of Assets assessment
4. **Key Metrics Table** - Populate each metric with current values

**Key Metrics to Track**:

| Metric | Source | Target |
|--------|--------|--------|
| AUP Policy Completeness | ISMS-IMP-A.5.10-11.1 | 100% |
| Asset Categories Covered | ISMS-IMP-A.5.10-11.1 | 100% |
| User Acknowledgment Rate | ISMS-IMP-A.5.10-11.1 | 100% |
| Usage Rules Documented | ISMS-IMP-A.5.10-11.2 | 100% |
| Return Process Requirements Met | ISMS-IMP-A.5.10-11.3 | 100% |
| Offboarding Completion Rate | ISMS-IMP-A.5.10-11.3 | 100% |
| Access Revocation SLA Compliance | ISMS-IMP-A.5.10-11.3 | 95%+ |

**Key Findings Section**:
Document critical findings and recommendations with priority, owner, and due date.

**Step 3: A.5.10 Compliance (A510_Compliance Sheet)**

Score each compliance area:

1. **Compliance_Area** - Pre-populated area categories
2. **Requirement** - Specific requirement
3. **Status** - Compliant/Partial/Non-Compliant/Not Assessed
4. **Score** - Numeric score (0, 0.5, or 1)
5. **Evidence_Ref** - Link to supporting evidence

**Compliance Areas for A.5.10**:
- Policy Framework
- Asset Coverage
- User Awareness
- Enforcement
- Monitoring
- Third Parties
- Review

**Step 4: A.5.11 Compliance (A511_Compliance Sheet)**

Score each compliance area:

**Compliance Areas for A.5.11**:
- Process documentation
- Asset return tracking
- Access revocation
- Data security
- Knowledge transfer
- Verification
- Remote workers
- Contractors

**Step 5: Gap Register (Gap_Register Sheet)**

Consolidate gaps from all assessments:

1. **Gap_ID** - Unique identifier
2. **Control** - A.5.10, A.5.11, or Both
3. **Gap_Description** - Clear description of gap
4. **Gap_Type** - Policy/Process/Technical/Documentation/Training
5. **Severity** - Critical/High/Medium/Low
6. **Owner** - Person responsible for remediation
7. **Target_Date** - Remediation deadline
8. **Status** - Open/In Progress/Remediated/Accepted/Closed

**Gap Tracking Rules**:
- Critical/High gaps require remediation plan within 5 business days
- Medium gaps require remediation within 30 days
- Low gaps addressed in next review cycle
- Accepted gaps require CISO approval and risk acceptance

**Step 6: Remediation Tracker (Remediation_Tracker Sheet)**

Track remediation actions:

1. **Remediation_ID** - Unique identifier
2. **Gap_Ref** - Link to Gap_Register
3. **Action_Description** - Specific action required
4. **Priority** - Critical/High/Medium/Low
5. **Owner** - Action owner
6. **Start_Date** - When work began
7. **Target_Date** - Due date
8. **Status** - Not Started/In Progress/On Hold/Completed/Cancelled
9. **% Complete** - Progress percentage

**Step 7: Trend Analysis (Trend_Analysis Sheet)**

Record compliance trends over time:

1. **Assessment_Period** - Quarter/Year
2. **A510_Score** - Acceptable Use compliance score
3. **A510_Change** - Change from previous period
4. **A511_Score** - Return of Assets compliance score
5. **A511_Change** - Change from previous period
6. **Overall_Score** - Combined compliance
7. **Open_Gaps** - Number of open gaps

**Step 8: Approval**

Complete sign-off section with approvals.

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Underlying Assessments | Completed ISMS-IMP-A.5.10-11.1-3 | ISMS Evidence Library |
| Compliance Reports | Generated dashboard exports | ISMS Evidence Library |
| Gap Closure Evidence | Remediation completion proof | ISMS Evidence Library |
| Management Reports | Executive summaries presented | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Using outdated data from underlying assessments
✅ **CORRECT**: Ensure all source assessments are current before updating dashboard

❌ **MISTAKE**: Not tracking trends over time
✅ **CORRECT**: Maintain historical data to show compliance trajectory

❌ **MISTAKE**: Gaps without clear ownership
✅ **CORRECT**: Every gap must have an assigned owner

❌ **MISTAKE**: Vague remediation actions
✅ **CORRECT**: Actions should be specific and verifiable

❌ **MISTAKE**: Not escalating overdue remediations
✅ **CORRECT**: Overdue items escalated per governance process

❌ **MISTAKE**: Inconsistent scoring methodology
✅ **CORRECT**: Apply scoring criteria consistently across assessments

❌ **MISTAKE**: Dashboard not reviewed before management presentation
✅ **CORRECT**: ISM reviews for accuracy before CISO presentation

❌ **MISTAKE**: Missing sign-off on management-presented dashboards
✅ **CORRECT**: All dashboards presented to management should be approved

### Quality Checklist

Before presenting:

- [ ] All source assessments are current (within 30 days)
- [ ] Compliance scores calculated correctly
- [ ] All gaps have owners and target dates
- [ ] Overdue remediations escalated
- [ ] Trends include at least 4 data points
- [ ] Executive summary reflects key messages
- [ ] Evidence linked for compliance claims
- [ ] Approval signatures obtained

### Review & Approval

**Review Workflow**:

1. Assessor compiles dashboard from source assessments
2. ISM verifies accuracy and completeness
3. CISO reviews for management presentation
4. Executive Management receives quarterly briefing

**Presentation Cadence**:
- Monthly: Update metrics and track remediations
- Quarterly: Full dashboard review with CISO
- Annual: Comprehensive review with Executive Management

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.10-11.4_Asset_Usage_Lifecycle_Compliance_Dashboard_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Sheet Specifications

#### Executive_Summary Sheet

**KPI Boxes**:
- Overall Compliance (merged cells A3:B5)
- A.5.10 Compliance (merged cells D3:E5)
- A.5.11 Compliance (merged cells G3:H5)

**Key Metrics Table**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Metric | 35 | Pre-populated metrics |
| B | Value | 18 | User input |
| C | Target | 12 | Pre-populated targets |
| D | Status | 14 | Data validation |
| E | Control | 12 | Pre-populated (A.5.10/A.5.11/Both) |

**Findings Table**:

| Column | Header | Width |
|--------|--------|-------|
| A-C | Finding/Recommendation | 60 (merged) |
| D | Priority | 14 |
| E | Owner | 20 |
| F | Due Date | 14 |

#### A510_Compliance Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Compliance_Area | 35 | Pre-populated areas |
| B | Requirement | 45 | Pre-populated requirements |
| C | Status | 16 | Data validation |
| D | Score | 12 | User input (0, 0.5, 1) |
| E | Max_Score | 12 | Pre-populated (1) |
| F | Evidence_Ref | 18 | User input |
| G | Last_Assessed | 14 | Date field |
| H | Assessor | 20 | User input |
| I | Gap_Notes | 35 | User input |
| J | Remediation_Ref | 16 | Link to Remediation_Tracker |

**Pre-populated Requirements**: 19 compliance requirements

**Summary Row**: Total score calculation with percentage

#### A511_Compliance Sheet

Similar structure to A510_Compliance with 20 requirements specific to A.5.11.

#### Gap_Register Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Gap_ID | 12 | Auto-generated (GAP-001) |
| B | Control | 12 | Data validation: A.5.10/A.5.11/Both |
| C | Gap_Description | 45 | User input |
| D | Gap_Type | 18 | Data validation |
| E | Severity | 14 | Data validation |
| F | Risk_Rating | 14 | User input |
| G | Identified_Date | 14 | Date field |
| H | Owner | 22 | User input |
| I | Target_Date | 14 | Date field |
| J | Status | 16 | Data validation |
| K | Remediation_Ref | 16 | Link to Remediation_Tracker |
| L | Notes | 30 | User input |

#### Remediation_Tracker Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Remediation_ID | 14 | Auto-generated (REM-001) |
| B | Gap_Ref | 14 | Link to Gap_Register |
| C | Action_Description | 45 | User input |
| D | Control | 12 | A.5.10/A.5.11/Both |
| E | Priority | 12 | Data validation |
| F | Owner | 22 | User input |
| G | Start_Date | 14 | Date field |
| H | Target_Date | 14 | Date field |
| I | Status | 16 | Data validation |
| J | % Complete | 12 | User input (0-100) |
| K | Completion_Date | 14 | Date field |
| L | Notes | 30 | User input |

#### Trend_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Assessment_Period | 18 | Pre-populated (Q1 2025, etc.) |
| B | A510_Score | 14 | User input |
| C | A510_Change | 14 | Formula (current - previous) |
| D | A511_Score | 14 | User input |
| E | A511_Change | 14 | Formula (current - previous) |
| F | Overall_Score | 14 | User input |
| G | Open_Gaps | 14 | User input |
| H | Notes | 40 | User input |

**Pre-populated Periods**: Q1 2025 through Q4 2026

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Compliance Status | Compliant, Partial, Non-Compliant, Not Assessed |
| KPI Status | On Track, At Risk, Behind |
| Finding Priority | Critical, High, Medium, Low |
| Control | A.5.10, A.5.11, Both |
| Gap_Type | Policy Gap, Process Gap, Technical Gap, Documentation Gap, Training Gap |
| Gap Severity | Critical, High, Medium, Low |
| Gap Status | Open, In Progress, Remediated, Accepted, Closed |
| Remediation Status | Not Started, In Progress, On Hold, Completed, Cancelled |

### Generator Reference

**Script**: `generate_a510_11_4_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-01 -->
