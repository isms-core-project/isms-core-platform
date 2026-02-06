# ISMS-IMP-A.5.35-36.S3 — Findings and Remediation Management

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S3 |
| **Title** | Findings and Remediation Management |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook provides consolidated tracking of all findings from independent reviews (A.5.35) and compliance assessments (A.5.36), enabling systematic remediation management and closure verification. It ensures management acts on identified inadequacies per ISO 27001 requirements.

**Scope**

This assessment covers:
- Consolidated findings register from all review sources
- Remediation action planning and tracking
- Root cause analysis for significant findings
- Verification and closure management
- Trend analysis of findings over time

**What This Assessment Covers**

| Domain | Assessment Focus |
|--------|-----------------|
| Findings Register | All identified gaps consolidated |
| Remediation Actions | Corrective action tracking |
| Root Cause Analysis | RCA for significant findings |
| Verification Log | Closure verification tracking |
| Trend Analysis | Finding patterns over time |

**Control Requirements**

ISO 27001:2022 A.5.35 states:
> *"If the independent review identifies that the organisation's approach to managing information security or its implementation is inadequate or not compliant, management should consider corrective actions."*

ISO 27001:2022 A.5.36 requires:
> *"If any non-compliance is discovered, managers should take corrective action."*

### Prerequisites

Before completing this assessment:

- [ ] Completed independent review reports (ISMS-IMP-A.5.35-36.S1)
- [ ] Completed compliance assessments (ISMS-IMP-A.5.35-36.S2)
- [ ] Internal/external audit reports
- [ ] Understanding of RCA methodologies
- [ ] Access to corrective action owners
- [ ] Evidence storage capability

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance and metadata | Review before starting |
| Findings_Register | Consolidated findings | Record all findings |
| Remediation_Actions | Action tracking | Plan and track actions |
| Root_Cause_Analysis | RCA documentation | Conduct RCA |
| Verification_Log | Closure verification | Verify remediation |
| Trend_Analysis | Pattern analysis | Analyse trends |
| Evidence_Register | Evidence management | Link evidence |
| Approval_SignOff | Authorisation | Obtain sign-offs |

### Completion Walkthrough

**Step 1: Findings_Register Sheet**

Consolidate all findings from all sources:

1. **Finding_ID** - Unique identifier (FND-YYYY-NNN)
2. **Source** - Independent Review / Compliance Assessment / Internal Audit / External Audit / Incident / Other
3. **Source_Ref** - Reference to source document (e.g., REV-2026-001)
4. **Finding_Date** - Date finding identified
5. **Control_Ref** - ISO 27001 control affected (e.g., A.5.15)
6. **Finding_Title** - Brief title
7. **Finding_Description** - Detailed description of the gap
8. **Severity** - Critical / High / Medium / Low / Observation
9. **Risk_Rating** - Associated risk level if assessed
10. **Affected_Area** - Department/system/process affected
11. **Finding_Owner** - Person accountable for remediation
12. **Target_Resolution** - Deadline for remediation
13. **Status** - Open / In Progress / Remediated / Verified Closed / Risk Accepted
14. **RCA_Required** - Yes / No
15. **RCA_Ref** - Link to Root_Cause_Analysis if conducted
16. **Remediation_Ref** - Link to Remediation_Actions
17. **Notes** - Additional information

**Finding Severity Definitions**:

| Severity | Definition | Resolution Target |
|----------|------------|-------------------|
| Critical | Fundamental control failure; immediate risk to organisation | 30 days |
| High | Significant gap requiring prompt attention | 60 days |
| Medium | Partial implementation requiring improvement | 90 days |
| Low | Minor gap with limited risk impact | Next review cycle |
| Observation | Improvement opportunity, not a compliance gap | Optional |

**RCA Triggers**:

RCA is mandatory for:
- All Critical findings
- All High findings
- Any recurring finding (appeared in 2+ reviews)
- Findings with systemic root cause suspected

**Step 2: Remediation_Actions Sheet**

Plan and track corrective actions:

1. **Action_ID** - Unique identifier (ACT-YYYY-NNN)
2. **Finding_Ref** - Link to Findings_Register
3. **Action_Type** - Corrective / Preventive / Improvement
4. **Action_Description** - Detailed description of action required
5. **Action_Owner** - Person accountable for completing action
6. **Priority** - Critical / High / Medium / Low
7. **Resources_Required** - Budget, personnel, tools needed
8. **Dependencies** - Other actions or factors required first
9. **Start_Date** - When action begins
10. **Target_Date** - Deadline for completion
11. **Actual_Completion** - Actual completion date
12. **Status** - Not Started / In Progress / On Hold / Completed / Cancelled
13. **Percent_Complete** - Progress percentage (0-100%)
14. **Blockers** - Issues preventing progress
15. **Evidence_Ref** - Evidence of completion
16. **Verified** - Yes / No / Pending
17. **Notes** - Progress notes

**Action Types**:

| Type | Purpose |
|------|---------|
| Corrective | Fix the identified gap |
| Preventive | Prevent recurrence |
| Improvement | Enhance beyond compliance |

**Priority Alignment**:

| Finding Severity | Action Priority | Update Frequency |
|------------------|-----------------|------------------|
| Critical | Critical | Daily |
| High | High | Weekly |
| Medium | Medium | Bi-weekly |
| Low | Low | Monthly |

**Step 3: Root_Cause_Analysis Sheet**

Document RCA for significant findings:

1. **RCA_ID** - Unique identifier (RCA-YYYY-NNN)
2. **Finding_Ref** - Link to Findings_Register
3. **RCA_Date** - Date RCA conducted
4. **RCA_Lead** - Person leading the RCA
5. **RCA_Participants** - Team members involved
6. **Methodology** - 5 Whys / Fishbone / Fault Tree / FMEA / Other
7. **Problem_Statement** - Clear statement of the problem
8. **Immediate_Cause** - Direct cause of the finding
9. **Contributing_Factors** - Factors that enabled the problem
10. **Root_Cause** - Fundamental underlying cause
11. **Why_1** - First why (for 5 Whys method)
12. **Why_2** - Second why
13. **Why_3** - Third why
14. **Why_4** - Fourth why
15. **Why_5** - Fifth why (root cause)
16. **Corrective_Actions** - Actions to fix the issue
17. **Preventive_Actions** - Actions to prevent recurrence
18. **Systemic_Issues** - Broader organisational issues identified
19. **Lessons_Learned** - Key takeaways
20. **Approval** - RCA approved by
21. **Approval_Date** - Date approved

**RCA Methodologies**:

| Method | When to Use |
|--------|-------------|
| 5 Whys | Simple to moderate complexity |
| Fishbone (Ishikawa) | Multiple potential cause categories |
| Fault Tree Analysis | Technical/system failures |
| FMEA | Process-related failures |

**Step 4: Verification_Log Sheet**

Track remediation verification:

1. **Verification_ID** - Unique identifier (VER-YYYY-NNN)
2. **Action_Ref** - Link to Remediation_Actions
3. **Finding_Ref** - Link to Findings_Register
4. **Verification_Type** - Self-Attestation / Peer Review / Independent Verification
5. **Verification_Date** - Date verified
6. **Verifier** - Person conducting verification
7. **Verifier_Independence** - Independent / Not Independent
8. **Verification_Method** - Document Review / Testing / Interview / Observation
9. **Evidence_Reviewed** - Evidence examined
10. **Outcome** - Verified / Failed / Partial
11. **Issues_Found** - Any issues during verification
12. **Retest_Required** - Yes / No
13. **Retest_Date** - If retest needed, target date
14. **Final_Status** - Open / Verified Closed
15. **Notes** - Verification notes

**Verification Requirements by Severity**:

| Finding Severity | Verification Requirement |
|------------------|-------------------------|
| Critical | Independent verification by qualified assessor |
| High | Independent verification by qualified assessor |
| Medium | Verification by Information Security team member |
| Low | Self-attestation with evidence |

**Step 5: Trend_Analysis Sheet**

Track finding patterns over time:

1. **Period** - Assessment period (e.g., Q1 2026)
2. **Period_Start** - Start date of period
3. **Period_End** - End date of period
4. **Total_Findings** - Total findings in period
5. **Critical_Count** - Critical findings count
6. **High_Count** - High findings count
7. **Medium_Count** - Medium findings count
8. **Low_Count** - Low findings count
9. **Observation_Count** - Observation count
10. **Closed_in_Period** - Findings closed during period
11. **Overdue_at_Period_End** - Findings past target date
12. **Average_Resolution_Days** - Mean time to remediate
13. **Top_Control_Area** - Control with most findings
14. **Top_Department** - Department with most findings
15. **Recurring_Findings** - Count of repeat findings
16. **Trend_vs_Prior** - Better / Same / Worse
17. **Notes** - Analysis commentary

**Trend Indicators**:

| Indicator | Good | Warning | Poor |
|-----------|------|---------|------|
| Closure Rate | >90% | 70-90% | <70% |
| Overdue Findings | <5% | 5-15% | >15% |
| Critical MTTR | <30 days | 30-45 days | >45 days |
| Recurring Findings | Decreasing | Stable | Increasing |

**Step 6: Evidence_Register Sheet**

Link all supporting evidence:

1. **Evidence_ID** - Unique identifier
2. **Related_Type** - Finding / Action / RCA / Verification
3. **Related_Ref** - Reference to parent record
4. **Evidence_Type** - Report / Screenshot / Email / Approval / Other
5. **Description** - Brief description
6. **Storage_Location** - File path or reference
7. **Collected_Date** - When collected
8. **Collected_By** - Who collected
9. **Retention_Until** - Retention period end

**Step 7: Approval_SignOff Sheet**

Obtain management approval:

1. **Approval_Type** - Findings Register / RCA / Action Plan / Closure
2. **Related_Ref** - Reference to approved item
3. **Prepared_By** - Preparer name and date
4. **Reviewed_By** - Reviewer name and date
5. **Approved_By** - Approver name and date
6. **Comments** - Conditions or notes

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Source Reports | Original review/audit reports | ISMS Evidence Library |
| RCA Documentation | Completed RCA worksheets | ISMS Evidence Library |
| Action Evidence | Proof of remediation completion | ISMS Evidence Library |
| Verification Records | Verification outcomes and evidence | ISMS Evidence Library |
| Closure Approvals | Sign-off on closed findings | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Findings tracked in multiple systems without consolidation
✅ **CORRECT**: Single consolidated register for all findings

❌ **MISTAKE**: Generic corrective actions that don't address root cause
✅ **CORRECT**: Specific actions linked to RCA findings

❌ **MISTAKE**: RCA skipped for high-severity findings
✅ **CORRECT**: Mandatory RCA for all Critical and High findings

❌ **MISTAKE**: Self-attestation used for Critical finding closure
✅ **CORRECT**: Independent verification required for Critical/High

❌ **MISTAKE**: Findings marked closed without evidence
✅ **CORRECT**: All closures require evidence reference

❌ **MISTAKE**: Overdue findings not escalated
✅ **CORRECT**: Escalation at 30, 60, 90 days overdue

❌ **MISTAKE**: No trend analysis to identify patterns
✅ **CORRECT**: Quarterly trend review to spot systemic issues

❌ **MISTAKE**: Actions tracked by multiple owners without accountability
✅ **CORRECT**: Single owner accountable for each action

### Quality Checklist

Before submitting:

- [ ] All findings from all sources consolidated
- [ ] Severity correctly assigned per definitions
- [ ] Owners assigned for all open findings
- [ ] RCA completed for all Critical/High findings
- [ ] Corrective actions defined for all findings
- [ ] Target dates set and achievable
- [ ] Verification appropriate to severity
- [ ] Trend analysis updated quarterly
- [ ] Evidence linked throughout
- [ ] Approval sign-offs obtained

### Review & Approval

**Review Workflow**:

1. Findings consolidated from all sources
2. ISM reviews completeness and severity
3. RCA conducted where required
4. Action plans developed with owners
5. Progress tracked per frequency
6. Verification conducted on completion
7. CISO approves closure for Critical/High

**Escalation Requirements**:

| Days Overdue | Escalation To |
|--------------|---------------|
| 30 days | Department Head |
| 60 days | CISO |
| 90 days | Executive Management |

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.35-36.S3_Findings_and_Remediation_Management_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Sheet Specifications

#### Findings_Register Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Finding_ID | 14 | Auto-format FND-YYYY-NNN |
| B | Source | 18 | Data validation |
| C | Source_Ref | 16 | User input |
| D | Finding_Date | 14 | Date field |
| E | Control_Ref | 12 | ISO control reference |
| F | Finding_Title | 35 | User input |
| G | Finding_Description | 50 | User input |
| H | Severity | 12 | Data validation |
| I | Risk_Rating | 12 | User input |
| J | Affected_Area | 22 | User input |
| K | Finding_Owner | 22 | User input |
| L | Target_Resolution | 14 | Date field |
| M | Status | 16 | Data validation |
| N | RCA_Required | 10 | Data validation |
| O | RCA_Ref | 14 | User input |
| P | Remediation_Ref | 14 | User input |
| Q | Notes | 30 | User input |

#### Remediation_Actions Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Action_ID | 14 | Auto-format ACT-YYYY-NNN |
| B | Finding_Ref | 14 | Link to Findings_Register |
| C | Action_Type | 14 | Data validation |
| D | Action_Description | 45 | User input |
| E | Action_Owner | 22 | User input |
| F | Priority | 12 | Data validation |
| G | Resources_Required | 30 | User input |
| H | Dependencies | 25 | User input |
| I | Start_Date | 14 | Date field |
| J | Target_Date | 14 | Date field |
| K | Actual_Completion | 14 | Date field |
| L | Status | 14 | Data validation |
| M | Percent_Complete | 12 | Percentage |
| N | Blockers | 30 | User input |
| O | Evidence_Ref | 16 | User input |
| P | Verified | 10 | Data validation |
| Q | Notes | 30 | User input |

#### Root_Cause_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | RCA_ID | 14 | Auto-format RCA-YYYY-NNN |
| B | Finding_Ref | 14 | Link to Findings_Register |
| C | RCA_Date | 14 | Date field |
| D | RCA_Lead | 22 | User input |
| E | RCA_Participants | 35 | User input |
| F | Methodology | 16 | Data validation |
| G | Problem_Statement | 45 | User input |
| H | Immediate_Cause | 40 | User input |
| I | Contributing_Factors | 40 | User input |
| J | Root_Cause | 45 | User input |
| K | Why_1 | 35 | User input |
| L | Why_2 | 35 | User input |
| M | Why_3 | 35 | User input |
| N | Why_4 | 35 | User input |
| O | Why_5 | 35 | User input |
| P | Corrective_Actions | 45 | User input |
| Q | Preventive_Actions | 45 | User input |
| R | Systemic_Issues | 40 | User input |
| S | Lessons_Learned | 40 | User input |
| T | Approval | 22 | User input |
| U | Approval_Date | 14 | Date field |

#### Verification_Log Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Verification_ID | 14 | Auto-format VER-YYYY-NNN |
| B | Action_Ref | 14 | Link to Remediation_Actions |
| C | Finding_Ref | 14 | Link to Findings_Register |
| D | Verification_Type | 18 | Data validation |
| E | Verification_Date | 14 | Date field |
| F | Verifier | 22 | User input |
| G | Verifier_Independence | 16 | Data validation |
| H | Verification_Method | 18 | Data validation |
| I | Evidence_Reviewed | 35 | User input |
| J | Outcome | 14 | Data validation |
| K | Issues_Found | 35 | User input |
| L | Retest_Required | 10 | Data validation |
| M | Retest_Date | 14 | Date field |
| N | Final_Status | 14 | Data validation |
| O | Notes | 30 | User input |

#### Trend_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Period | 14 | User input |
| B | Period_Start | 14 | Date field |
| C | Period_End | 14 | Date field |
| D | Total_Findings | 12 | Numeric |
| E | Critical_Count | 12 | Numeric |
| F | High_Count | 12 | Numeric |
| G | Medium_Count | 12 | Numeric |
| H | Low_Count | 12 | Numeric |
| I | Observation_Count | 14 | Numeric |
| J | Closed_in_Period | 14 | Numeric |
| K | Overdue_at_Period_End | 14 | Numeric |
| L | Average_Resolution_Days | 14 | Numeric |
| M | Top_Control_Area | 20 | User input |
| N | Top_Department | 20 | User input |
| O | Recurring_Findings | 14 | Numeric |
| P | Trend_vs_Prior | 12 | Data validation |
| Q | Notes | 40 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Source | Independent Review, Compliance Assessment, Internal Audit, External Audit, Incident, Regulatory, Other |
| Severity | Critical, High, Medium, Low, Observation |
| Finding_Status | Open, In Progress, Remediated, Verified Closed, Risk Accepted |
| RCA_Required | Yes, No |
| Action_Type | Corrective, Preventive, Improvement |
| Priority | Critical, High, Medium, Low |
| Action_Status | Not Started, In Progress, On Hold, Completed, Cancelled |
| Verified | Yes, No, Pending |
| Methodology | 5 Whys, Fishbone, Fault Tree, FMEA, Other |
| Verification_Type | Self-Attestation, Peer Review, Independent Verification |
| Verifier_Independence | Independent, Not Independent |
| Verification_Method | Document Review, Testing, Interview, Observation, Combined |
| Verification_Outcome | Verified, Failed, Partial |
| Retest_Required | Yes, No |
| Final_Status | Open, Verified Closed |
| Trend_vs_Prior | Better, Same, Worse |

### Generator Reference

**Script**: `generate_a535_36_3_findings_remediation.py`

**Location**: `10-isms-scr-base/isms-a.5.35-36-compliance-review/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-01 -->
