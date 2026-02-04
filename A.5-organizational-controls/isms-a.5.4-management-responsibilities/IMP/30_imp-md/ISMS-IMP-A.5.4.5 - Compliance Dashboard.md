# ISMS-IMP-A.5.4.5 - Compliance Dashboard

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.5 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## PART I: USER COMPLETION GUIDE

### 1. Assessment Overview

#### 1.1 Purpose

This compliance dashboard consolidates data from all A.5.4 assessment workbooks into a unified view for compliance monitoring, audit readiness, and executive reporting. It provides a single source of truth for management responsibilities compliance status across the organisation.

#### 1.2 Scope

This dashboard aggregates data from:

| Source Workbook | Assessment Domain | Key Data |
|-----------------|-------------------|----------|
| **A.5.4.1** | Management Commitment Assessment | Manager scores, commitment levels |
| **A.5.4.2** | Compliance Oversight Tracker | Training, violations, access reviews |
| **A.5.4.3** | Leadership Dashboard | Departmental metrics, executive view |
| **A.5.4.4** | Security Culture Survey | Employee perception scores |

#### 1.3 Control Requirement

Per ISO/IEC 27001:2022 Control A.5.4:

> *"Management should require all personnel to apply information security in accordance with the established information security policy, topic-specific policies and procedures of the organisation."*

This dashboard provides consolidated evidence that management actively enforces this requirement through measurable commitment, oversight, leadership, and culture programmes.

#### 1.4 Why This Matters

**The Integration Challenge**: Individual assessment workbooks capture detailed data, but auditors and executives need a unified view:
- How does management commitment translate to actual compliance?
- Are oversight activities achieving desired outcomes?
- Is leadership visible across all departments?
- Does the workforce perceive management's efforts as effective?

**This dashboard solves the integration problem** by:
- Consolidating key metrics from all four A.5.4 workbooks
- Calculating unified compliance scores
- Identifying cross-cutting gaps
- Tracking trends over time
- Preparing evidence for audit readiness

**Real-World Impact**:
- Reduces audit preparation time by 60%
- Enables proactive gap identification before issues become findings
- Provides executives with actionable compliance intelligence
- Demonstrates continuous improvement to certifying bodies

**The ISMS Copilot Connection**: During Stage 2 audits, auditors will request consolidated evidence of management responsibilities implementation. This dashboard provides:
- Overall compliance score with requirement-level detail
- Gap analysis with remediation tracking
- Audit readiness checklist with evidence locations
- Trend analysis showing improvement trajectory

#### 1.5 Assessment Frequency

| Activity | Frequency | Timing |
|----------|-----------|--------|
| Executive Summary update | Monthly | End of month |
| KPI Dashboard refresh | Quarterly | End of quarter |
| Compliance Scorecard review | Quarterly | Before management review |
| Full assessment consolidation | Annual | Before surveillance audit |
| Gap remediation tracking | Ongoing | As gaps identified |

### 2. Prerequisites

Before completing this dashboard, ensure:

- [ ] A.5.4.1 Management Commitment Assessment completed
- [ ] A.5.4.2 Compliance Oversight Tracker current
- [ ] A.5.4.3 Leadership Dashboard populated
- [ ] A.5.4.4 Security Culture Survey conducted (annual)
- [ ] Prior period dashboard available (for trend comparison)
- [ ] Gap register from previous audit (if applicable)

### 3. Workbook Structure

| Sheet | Purpose | When to Complete |
|-------|---------|------------------|
| **Instructions** | Guidance, source workbooks, scoring methodology | Reference |
| **Executive_Summary** | High-level status by assessment domain | Monthly |
| **Compliance_KPIs** | Key performance indicators with targets | Quarterly |
| **Compliance_Scorecard** | Requirement-level implementation scores | Quarterly |
| **Gap_Analysis** | Identified gaps with remediation tracking | Ongoing |
| **Audit_Readiness** | Evidence checklist for audit preparation | Before audits |
| **Trend_Analysis** | Historical compliance trends by quarter | Quarterly |
| **Evidence_Register** | Audit evidence documentation | Ongoing |
| **Approval_SignOff** | Management approval workflow | Each assessment |

### 4. Compliance Scoring Methodology

#### 4.1 Overall Compliance Score

The overall score is calculated as a weighted average:

| Assessment Domain | Weight | Rationale |
|-------------------|:------:|-----------|
| Management Commitment (A.5.4.1) | 25% | Foundation - commitment enables everything else |
| Compliance Oversight (A.5.4.2) | 30% | Operations - day-to-day enforcement activities |
| Leadership Metrics (A.5.4.3) | 20% | Visibility - leadership engagement by department |
| Security Culture (A.5.4.4) | 25% | Outcome - employee perception of effectiveness |

#### 4.2 Compliance Status Categories

| Status | Score Range | Indicator | Audit Implication |
|--------|:-----------:|:---------:|-------------------|
| **Compliant** | ≥90% | Green | Ready for audit |
| **Partially Compliant** | 70-89% | Amber | Minor findings likely |
| **Non-Compliant** | <70% | Red | Major findings expected |

#### 4.3 Requirement-Level Scoring

Each requirement in the Compliance Scorecard is scored:

| Implementation Status | Score Percentage |
|-----------------------|:----------------:|
| Fully Implemented | 100% |
| Partially Implemented | 50% |
| Not Implemented | 0% |
| Not Applicable | N/A (excluded) |

### 5. Completion Walkthrough

#### Step 1: Gather Source Data

Collect current data from all source workbooks:

| From A.5.4.1 | Data Required |
|--------------|---------------|
| Summary Scores | Overall commitment score, managers assessed count |
| Individual Assessments | Managers meeting threshold (≥70%) |

| From A.5.4.2 | Data Required |
|--------------|---------------|
| Training Oversight | Teams with ≥90% training compliance |
| Policy Violations | Violations addressed within SLA |
| Access Reviews | Reviews completed on schedule |
| Escalation Triggers | Managers triggering escalation |

| From A.5.4.3 | Data Required |
|--------------|---------------|
| Department Metrics | Departmental compliance scores |
| Executive View | Overall leadership engagement score |

| From A.5.4.4 | Data Required |
|--------------|---------------|
| Response Data | Overall culture score |
| Category Scores | Leadership, Policy, Training, Reporting, Personal |

#### Step 2: Complete Executive Summary

1. Enter **Reporting Period** (e.g., "Q4 2025")
2. Enter **Assessment Date**
3. For each domain, transfer:
   - **Status**: Compliant/Partially Compliant/Non-Compliant
   - **Score %**: From source workbook
   - **Key Issues**: Top 1-2 issues requiring attention
4. Calculate **OVERALL A.5.4** row:
   - Score = Weighted average per methodology
   - Status = Based on score ranges

#### Step 3: Populate Compliance KPIs

For each pre-populated KPI:

1. Enter **Current_Value** from source workbook
2. Determine **Status**:
   - On Target: Meeting or exceeding target
   - At Risk: Within 10% of target
   - Below Target: More than 10% below target
3. Assess **Trend**:
   - Improving: Better than previous quarter
   - Stable: Within ±5% of previous
   - Declining: More than 5% worse than previous
4. Add **Comments** for context on any At Risk or Below Target KPIs

**Pre-Populated KPIs**:

| KPI_ID | KPI Name | Target | Data Source |
|--------|----------|--------|-------------|
| A54-KPI-001 | Management Commitment Score | ≥70% | A.5.4.1 Summary |
| A54-KPI-002 | Manager Assessment Coverage | 100% | A.5.4.1 Inventory |
| A54-KPI-003 | Training Oversight Rate | 100% | A.5.4.2 Training |
| A54-KPI-004 | Violation Response Time | ≤5 days | A.5.4.2 Violations |
| A54-KPI-005 | Access Review Completion | 100% | A.5.4.2 Reviews |
| A54-KPI-006 | Security Culture Score | ≥70% | A.5.4.4 Response |
| A54-KPI-007 | Escalation Trigger Rate | <10% | A.5.4.2 Escalation |

#### Step 4: Complete Compliance Scorecard

For each requirement:

1. Verify **Evidence_Available**: Yes/Partial/No
2. Assess **Implementation_Status**:
   - Fully Implemented: All aspects in place with evidence
   - Partially Implemented: Some aspects missing
   - Not Implemented: Not addressed
   - Not Applicable: Requirement doesn't apply
3. Assign **Score** based on implementation status
4. Document **Gap_Description** for any gaps identified
5. Set **Remediation_Status**:
   - Not Required: Fully implemented
   - Planned: Remediation scheduled
   - In Progress: Active remediation
   - Completed: Gap closed

**Pre-Populated Requirements** (aligned with ISO 27001:2022 A.5.4):

| REQ | Requirement | Source | Weight |
|-----|-------------|--------|:------:|
| REQ-001 | Management requires personnel to apply security per policies | A.5.4 | 15 |
| REQ-002 | All managers assessed for security commitment | A.5.4.1 | 10 |
| REQ-003 | Manager commitment scores meet minimum threshold | A.5.4.1 | 15 |
| REQ-004 | Training oversight tracked and reported | A.5.4.2 | 10 |
| REQ-005 | Policy violations addressed per escalation triggers | A.5.4.2 | 10 |
| REQ-006 | Access reviews completed by managers | A.5.4.2 | 10 |
| REQ-007 | Leadership metrics tracked by department | A.5.4.3 | 10 |
| REQ-008 | Security culture survey conducted annually | A.5.4.4 | 10 |
| REQ-009 | Culture survey results actioned | A.5.4.4 | 5 |
| REQ-010 | Management commitment evidence available for audit | A.5.4 | 5 |

**Total Weighted Score**: 100 points

#### Step 5: Document Gaps in Gap Analysis

For each gap identified in the Scorecard:

1. Generate **Gap_ID** (format: GAP-A54-NNN)
2. Link to **Requirement_Reference**
3. Describe the **Gap_Description** clearly
4. Assess **Risk_Level**:
   - Critical: Immediate audit finding, regulatory risk
   - High: Likely audit finding
   - Medium: Potential finding if not addressed
   - Low: Minor improvement opportunity
5. Document **Root_Cause** (why the gap exists)
6. Define **Remediation_Action** (specific steps to close)
7. Assign **Owner** (accountable person)
8. Set **Target_Date** (realistic completion date)
9. Track **Status**: Open/In Progress/Closed/Deferred
10. Update **Progress**: 0%/25%/50%/75%/100%
11. Document **Evidence_of_Closure** when complete

#### Step 6: Prepare Audit Readiness Checklist

For each audit check:

1. Verify **Evidence_Location** where the evidence is stored
2. Confirm **Evidence_Available**: Yes/Partial/No
3. Record **Last_Reviewed** date
4. Document **Reviewer** who verified evidence
5. Set **Status**:
   - Ready: Evidence current and accessible
   - Action Required: Evidence missing or outdated
   - Not Applicable: Check doesn't apply

**Pre-Populated Audit Checks**:

| Check | Audit Requirement | Evidence Required |
|-------|-------------------|-------------------|
| AUD-001 | Management commitment policy exists | ISMS-POL-A.5.4 document |
| AUD-002 | Manager assessment records available | A.5.4.1 completed workbooks |
| AUD-003 | Commitment scores calculated and tracked | A.5.4.1 Summary Scores sheet |
| AUD-004 | Training oversight documented | A.5.4.2 Training Oversight sheet |
| AUD-005 | Policy violation handling documented | A.5.4.2 Policy Violations sheet |
| AUD-006 | Access review participation tracked | A.5.4.2 Access Reviews sheet |
| AUD-007 | Escalation process evidence | A.5.4.2 Escalation Triggers sheet |
| AUD-008 | Leadership dashboard maintained | A.5.4.3 workbook |
| AUD-009 | Security culture survey conducted | A.5.4.4 Response Data sheet |
| AUD-010 | Culture improvement actions tracked | A.5.4.4 Action Plan sheet |

#### Step 7: Update Trend Analysis

For the current quarter:

1. Transfer scores from Executive Summary:
   - **Commitment_Score**: From A.5.4.1
   - **Training_Compliance**: From A.5.4.2
   - **Violation_Response**: Average response days
   - **Access_Review_Rate**: % completed
   - **Culture_Score**: From A.5.4.4
2. Calculate **Overall_Score** (weighted average)
3. Document **Key_Changes** from previous quarter
4. Add **Notes** explaining significant variances

**Target Trends**: All metrics should show "Improving" or "Stable"

#### Step 8: Maintain Evidence Register

For each piece of evidence collected:

1. Generate **Evidence_ID** (format: EV-A54-NNN)
2. Select **Evidence_Type**:
   - Assessment Record
   - Training Record
   - Violation Record
   - Review Record
   - Survey Results
   - Approval Record
   - Other
3. Enter **Description** of what the evidence shows
4. Link to **Related_Requirement**
5. Record **Date_Created** and **Created_By**
6. Document **Storage_Location** (full path or SharePoint link)
7. Set **Retention_Period** (typically 3 years for ISMS evidence)
8. Schedule **Review_Date** (typically annual)
9. Set **Status**: Current/Archived/Pending Review

#### Step 9: Obtain Approval

1. Complete all sheets above
2. Enter **Assessment Period** and **Assessment Date**
3. Enter **Prepared By** (your name)
4. Route for approval:
   - Security Analyst → prepares
   - Security Manager → reviews
   - HR Director → validates HR-related data
   - CISO → final approval
5. Each approver signs with name, date, and comments
6. Confirm declaration checkbox

### 6. Worked Examples

#### Example A: Strong Compliance Status

**Executive Summary**:

| Assessment Domain | Workbook | Status | Score | Key Issues |
|-------------------|----------|--------|:-----:|------------|
| Management Commitment | A.5.4.1 | Compliant | 92% | 2 managers pending re-assessment |
| Compliance Oversight | A.5.4.2 | Compliant | 94% | None |
| Leadership Metrics | A.5.4.3 | Partially Compliant | 85% | Sales department below threshold |
| Security Culture | A.5.4.4 | Compliant | 91% | Training perception at 3.6/5.0 |
| **OVERALL A.5.4** | **Consolidated** | **Compliant** | **91%** | **Ready for audit** |

**Weighted Calculation**:
- Commitment: 92% × 25% = 23.0
- Oversight: 94% × 30% = 28.2
- Leadership: 85% × 20% = 17.0
- Culture: 91% × 25% = 22.75
- **Total: 91.0%** → Compliant

**KPI Snapshot**:

| KPI | Target | Current | Status | Trend |
|-----|--------|---------|--------|-------|
| Manager Commitment Score | ≥70% | 82% | On Target | Improving |
| Assessment Coverage | 100% | 98% | At Risk | Stable |
| Training Oversight Rate | 100% | 100% | On Target | Stable |
| Violation Response Time | ≤5 days | 3.2 days | On Target | Improving |
| Culture Score | ≥70% | 78% | On Target | Improving |

**Gaps Identified**: 2 minor gaps (Sales leadership metrics, 2 manager re-assessments pending)

**Audit Readiness**: 10/10 checks Ready

---

#### Example B: Improvement Required Status

**Executive Summary**:

| Assessment Domain | Workbook | Status | Score | Key Issues |
|-------------------|----------|--------|:-----:|------------|
| Management Commitment | A.5.4.1 | Partially Compliant | 72% | 8 managers below threshold |
| Compliance Oversight | A.5.4.2 | Partially Compliant | 78% | 3 violations exceeded SLA |
| Leadership Metrics | A.5.4.3 | Non-Compliant | 65% | 4 departments without data |
| Security Culture | A.5.4.4 | Partially Compliant | 71% | Reporting culture at 3.0/5.0 |
| **OVERALL A.5.4** | **Consolidated** | **Partially Compliant** | **72%** | **Significant gaps require remediation** |

**Weighted Calculation**:
- Commitment: 72% × 25% = 18.0
- Oversight: 78% × 30% = 23.4
- Leadership: 65% × 20% = 13.0
- Culture: 71% × 25% = 17.75
- **Total: 72.15%** → Partially Compliant

**Gap Analysis Generated**:

| Gap_ID | Requirement | Risk | Owner | Target |
|--------|-------------|:----:|-------|--------|
| GAP-A54-001 | Manager commitment threshold | High | HR Director | 60 days |
| GAP-A54-002 | Violation SLA compliance | Medium | Security Mgr | 30 days |
| GAP-A54-003 | Leadership dashboard coverage | High | CISO | 45 days |
| GAP-A54-004 | Reporting culture improvement | Medium | CISO | 90 days |

**Remediation Priority**:
1. Leadership dashboard coverage (closes largest gap)
2. Manager commitment re-assessment programme
3. Violation SLA process improvement
4. Reporting culture targeted training

**Audit Readiness**: 7/10 checks Ready, 3 Action Required

### 7. Evidence Collection

#### 7.1 Required Evidence

| Evidence Type | Description | Location |
|---------------|-------------|----------|
| Completed A.5.4.1-4 workbooks | All source assessments | ISMS Evidence Library/A.5.4/ |
| This dashboard | Consolidated compliance view | ISMS Evidence Library/A.5.4/ |
| Gap remediation records | Closure evidence for gaps | ISMS Evidence Library/A.5.4/Gaps/ |
| Approval records | Signed approval sheets | ISMS Evidence Library/A.5.4/Approvals/ |
| Trend reports | Quarter-over-quarter analysis | ISMS Evidence Library/A.5.4/Trends/ |

#### 7.2 Evidence Storage

All evidence should be stored in the ISMS Evidence Library (SharePoint/Confluence or equivalent):

```
ISMS Evidence Library/
└── A.5.4 Management Responsibilities/
    ├── Assessments/
    │   ├── A.5.4.1 Commitment/
    │   ├── A.5.4.2 Oversight/
    │   ├── A.5.4.3 Leadership/
    │   └── A.5.4.4 Culture/
    ├── Dashboards/
    │   └── [This workbook by period]
    ├── Gaps/
    │   └── [Gap closure evidence]
    ├── Approvals/
    │   └── [Signed approval sheets]
    └── Trends/
        └── [Quarter-over-quarter reports]
```

### 8. Common Pitfalls

❌ **MISTAKE: Using stale source data**
Complete all source workbooks (A.5.4.1-4) before consolidating. Data older than one quarter skews compliance scores.

❌ **MISTAKE: Forgetting to weight the scores**
The overall score is a weighted average, not a simple average. Oversight (30%) and Commitment/Culture (25% each) have higher impact than Leadership (20%).

❌ **MISTAKE: Marking gaps as "Closed" without evidence**
Every gap closure requires documented evidence. "Evidence_of_Closure" column must contain specific reference before setting Status to Closed.

❌ **MISTAKE: Skipping trend analysis**
Auditors look for continuous improvement. A single point-in-time assessment is less valuable than demonstrated improvement trajectory.

❌ **MISTAKE: Not linking gaps to requirements**
Each gap must reference a specific requirement (REQ-XXX). Unlinked gaps cannot be traced to compliance impact.

❌ **MISTAKE: Inconsistent evidence locations**
Use standardised paths in Evidence_Register. "My Desktop" or "Shared Drive" are not acceptable audit evidence locations.

❌ **MISTAKE: Incomplete audit readiness checks**
All 10 pre-populated checks must be verified before declaring audit ready. One "Action Required" status means the control is not audit ready.

❌ **MISTAKE: Missing approval signatures**
The dashboard is not valid without all four approval signatures (Analyst, Manager, HR Director, CISO). Unsigned dashboards cannot be used as audit evidence.

❌ **MISTAKE: Calculating overall score as simple average**
Use the weighted formula: (Commitment × 0.25) + (Oversight × 0.30) + (Leadership × 0.20) + (Culture × 0.25)

❌ **MISTAKE: Not updating after gap remediation**
When gaps are closed, update both Gap_Analysis and Compliance_Scorecard. The overall compliance score should improve as gaps close.

### 9. Quality Checklist

Before submitting the dashboard for approval:

- [ ] All source workbooks (A.5.4.1-4) current and complete
- [ ] Executive Summary reflects actual source data
- [ ] All 7 KPIs have current values entered
- [ ] Compliance Scorecard fully assessed (no blank scores)
- [ ] All identified gaps documented in Gap_Analysis
- [ ] Each gap has owner, target date, and status
- [ ] Audit Readiness checklist 100% complete
- [ ] Evidence Register includes all evidence locations
- [ ] Trend Analysis updated for current quarter
- [ ] Weighted overall score calculated correctly
- [ ] All approval signatures obtained
- [ ] Dashboard saved to ISMS Evidence Library

### 10. Review and Approval

#### 10.1 Review Workflow

| Role | Review Focus | Timeline |
|------|--------------|----------|
| Security Analyst | Data accuracy, calculations | Preparation |
| Security Manager | Gap analysis, remediation | Within 3 days |
| HR Director | Manager assessment validity | Within 5 days |
| CISO | Overall compliance, audit readiness | Within 7 days |

#### 10.2 Approval Authority

- **Monthly Updates**: Security Manager may approve
- **Quarterly Full Assessment**: CISO approval required
- **Pre-Audit Submission**: All four signatures required

---

## PART II: TECHNICAL SPECIFICATION

### 11. Excel Workbook Structure

#### 11.1 Sheet Overview

| # | Sheet Name | Purpose | Rows | Key Features |
|---|------------|---------|------|--------------|
| 1 | Instructions | User guidance | ~40 | Read-only |
| 2 | Executive_Summary | High-level status | ~25 | Domain status table, KPI metrics |
| 3 | Compliance_KPIs | KPI tracking | ~20 | Pre-populated KPIs, data validation |
| 4 | Compliance_Scorecard | Requirement scoring | ~20 | Weighted scoring, gap linkage |
| 5 | Gap_Analysis | Gap remediation | ~30 | Risk levels, progress tracking |
| 6 | Audit_Readiness | Evidence checklist | ~20 | Pre-populated checks |
| 7 | Trend_Analysis | Historical trends | ~10 | Quarterly periods |
| 8 | Evidence_Register | Evidence tracking | ~30 | Storage locations, retention |
| 9 | Approval_SignOff | Approval workflow | ~20 | Signature table, declaration |

### 12. Sheet Specifications

#### 12.1 Instructions Sheet

**Purpose**: Provide user guidance and document metadata

**Content Structure**:
```
Row 1: Document title (ISMS-IMP-A.5.4.5 - Management Responsibilities Compliance Dashboard)
Rows 3-5: Purpose statement
Rows 7-14: Source workbooks listing
Rows 16-25: Sheet descriptions
Rows 27-31: Compliance scoring methodology
Rows 33-36: Refresh frequency guidance
Row 38-39: Document metadata (generated date, control reference)
```

**Formatting**:
- Column A width: 90
- Title: Bold 14pt
- Section headers: Bold 11pt

#### 12.2 Executive_Summary Sheet

**Header Row** (Row 6):

| Column | Header | Width | Notes |
|--------|--------|:-----:|-------|
| A | Assessment Domain | 40 | |
| B | Workbook | 20 | |
| C | Status | 15 | Data validation |
| D | Score % | 18 | Input (yellow) |
| E | Key Issues | 12 | Input (yellow) |

**Pre-Populated Domains** (Rows 7-11):
1. Management Commitment (A.5.4.1)
2. Compliance Oversight (A.5.4.2)
3. Leadership Metrics (A.5.4.3)
4. Security Culture (A.5.4.4)
5. OVERALL A.5.4 (Consolidated) - bold

**Key Metrics Section** (Row 14+):

| Column | Header | Width |
|--------|--------|:-----:|
| A | Metric | 40 |
| B | Target | 20 |
| C | Current | 15 |
| D | Status | 18 |
| E | Trend | 12 |

**Data Validations**:
- Status (C7:C11): "Compliant,Partially Compliant,Non-Compliant"

#### 12.3 Compliance_KPIs Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | KPI_ID | 15 | |
| B | KPI_Name | 28 | |
| C | Description | 45 | |
| D | Target | 12 | |
| E | Current_Value | 15 | ✓ |
| F | Measurement_Method | 35 | |
| G | Frequency | 12 | |
| H | Data_Source | 25 | |
| I | Owner | 18 | |
| J | Status | 12 | ✓ |
| K | Trend | 12 | ✓ |
| L | Comments | 30 | ✓ |

**Pre-Populated KPIs** (Rows 2-8):
- A54-KPI-001 through A54-KPI-007 as specified in Section 5

**Data Validations**:
- Status (J2:J20): "On Target,At Risk,Below Target"
- Trend (K2:K20): "Improving,Stable,Declining"
- Frequency (G2:G20): "Monthly,Quarterly,Semi-annual,Annual"

#### 12.4 Compliance_Scorecard Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Requirement_ID | 12 | |
| B | Requirement | 50 | |
| C | Source | 10 | |
| D | Weight | 8 | |
| E | Evidence_Available | 18 | ✓ |
| F | Implementation_Status | 22 | ✓ |
| G | Score | 8 | ✓ |
| H | Max_Score | 10 | |
| I | Gap_Description | 35 | ✓ |
| J | Remediation_Status | 18 | ✓ |

**Pre-Populated Requirements** (Rows 2-11):
- REQ-001 through REQ-010 as specified in Section 5

**Data Validations**:
- Evidence_Available (E2:E20): "Yes,Partial,No"
- Implementation_Status (F2:F20): "Fully Implemented,Partially Implemented,Not Implemented,Not Applicable"
- Remediation_Status (J2:J20): "Not Required,In Progress,Planned,Completed"

#### 12.5 Gap_Analysis Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Gap_ID | 10 | ✓ |
| B | Requirement_Reference | 18 | ✓ |
| C | Gap_Description | 40 | ✓ |
| D | Risk_Level | 10 | ✓ |
| E | Root_Cause | 30 | ✓ |
| F | Remediation_Action | 40 | ✓ |
| G | Owner | 18 | ✓ |
| H | Target_Date | 12 | ✓ |
| I | Status | 12 | ✓ |
| J | Progress | 10 | ✓ |
| K | Evidence_of_Closure | 25 | ✓ |
| L | Notes | 30 | ✓ |

**Data Validations**:
- Risk_Level (D2:D30): "Critical,High,Medium,Low"
- Status (I2:I30): "Open,In Progress,Closed,Deferred"
- Progress (J2:J30): "0%,25%,50%,75%,100%"

#### 12.6 Audit_Readiness Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Check_ID | 10 | |
| B | Audit_Requirement | 38 | |
| C | Evidence_Required | 35 | |
| D | Evidence_Location | 30 | ✓ |
| E | Evidence_Available | 18 | ✓ |
| F | Last_Reviewed | 15 | ✓ |
| G | Reviewer | 18 | ✓ |
| H | Status | 18 | ✓ |
| I | Notes | 30 | ✓ |

**Pre-Populated Checks** (Rows 2-11):
- AUD-001 through AUD-010 as specified in Section 5

**Data Validations**:
- Evidence_Available (E2:E20): "Yes,Partial,No"
- Status (H2:H20): "Ready,Action Required,Not Applicable"

#### 12.7 Trend_Analysis Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Period | 12 | |
| B | Commitment_Score | 18 | ✓ |
| C | Training_Compliance | 20 | ✓ |
| D | Violation_Response | 20 | ✓ |
| E | Access_Review_Rate | 18 | ✓ |
| F | Culture_Score | 15 | ✓ |
| G | Overall_Score | 15 | ✓ |
| H | Key_Changes | 35 | ✓ |
| I | Notes | 30 | ✓ |

**Pre-Populated Periods** (Rows 2-9):
- Q1 2025 through Q4 2026

#### 12.8 Evidence_Register Sheet

**Header Row** (Row 1):

| Column | Header | Width | Input |
|--------|--------|:-----:|:-----:|
| A | Evidence_ID | 12 | ✓ |
| B | Evidence_Type | 20 | ✓ |
| C | Description | 40 | ✓ |
| D | Related_Requirement | 18 | ✓ |
| E | Date_Created | 15 | ✓ |
| F | Created_By | 20 | ✓ |
| G | Storage_Location | 40 | ✓ |
| H | Retention_Period | 15 | ✓ |
| I | Review_Date | 15 | ✓ |
| J | Status | 15 | ✓ |
| K | Notes | 30 | ✓ |

**Data Validations**:
- Evidence_Type (B2:B50): "Assessment Record,Training Record,Violation Record,Review Record,Survey Results,Approval Record,Other"
- Status (J2:J50): "Current,Archived,Pending Review"

#### 12.9 Approval_SignOff Sheet

**Title Section** (Row 1):
- Merged A1:F1
- Title: "A.5.4 Compliance Dashboard - Approval & Sign-Off"
- Dark blue fill, white bold 16pt font

**Assessment Details** (Rows 3-5):
- Assessment Period (B3)
- Assessment Date (B4)
- Prepared By (B5)

**Approval Table** (Row 8+):

| Column | Header | Width |
|--------|--------|:-----:|
| A | Role | 35 |
| B | Name | 25 |
| C | Date | 15 |
| D | Signature | 20 |
| E | Comments | 40 |

**Pre-Populated Roles**:
1. Prepared By (Security Analyst)
2. Reviewed By (Security Manager)
3. Validated By (HR Director)
4. Approved By (CISO)

**Declaration** (Below approval table):
Merged cells with declaration text confirming accuracy and completeness.

### 13. Styling Specifications

#### 13.1 Colour Palette

| Element | Hex Code | RGB | Usage |
|---------|----------|-----|-------|
| Header Fill | #2F5496 | 47,84,150 | Column headers |
| Title Fill | #1F4E79 | 31,78,121 | Sheet titles |
| Input Fill | #FFFFCC | 255,255,204 | User input cells |
| Calculated Fill | #E2EFDA | 226,239,218 | Formula cells |
| Compliant Fill | #C6EFCE | 198,239,206 | Green status |
| Partial Fill | #FFEB9C | 255,235,156 | Amber status |
| Non-Compliant Fill | #FFC7CE | 255,199,206 | Red status |

#### 13.2 Font Specifications

| Element | Font | Size | Style | Colour |
|---------|------|:----:|-------|--------|
| Title | Calibri | 16pt | Bold | White |
| Section Header | Calibri | 12pt | Bold | #1F4E79 |
| Column Header | Calibri | 11pt | Bold | White |
| Data Cell | Calibri | 11pt | Regular | Black |
| Instructions | Calibri | 11pt | Regular | Black |

#### 13.3 Border Style

All data cells use thin black borders on all sides.

### 14. Generator Script Reference

**Script**: `generate_a54_5_compliance_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.4-management-responsibilities/10_generator-master/`

**Output**: `ISMS-IMP-A.5.4.5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.4-management-responsibilities/10_generator-master
python3 generate_a54_5_compliance_dashboard.py
mv *.xlsx ../90_workbooks/
```

**Dependencies**:
- Python 3.8+
- openpyxl

### 15. Integration Points

#### 15.1 Source Workbook Dependencies

| Source | Sheet | Data Extracted |
|--------|-------|----------------|
| A.5.4.1 | Summary_Scores | Overall commitment score |
| A.5.4.1 | Manager_Assessments | Managers meeting threshold |
| A.5.4.2 | Training_Oversight | Compliance percentages |
| A.5.4.2 | Policy_Violations | Response times |
| A.5.4.2 | Access_Reviews | Completion rates |
| A.5.4.2 | Escalation_Triggers | Trigger counts |
| A.5.4.3 | Department_Metrics | Departmental scores |
| A.5.4.4 | Response_Data | Culture scores by category |

#### 15.2 Downstream Consumers

| Consumer | Usage |
|----------|-------|
| Management Review | Quarterly compliance reporting |
| Internal Audit | Pre-audit evidence verification |
| External Audit | Stage 2 audit evidence |
| CISO Dashboard | Executive compliance summary |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-04 -->
