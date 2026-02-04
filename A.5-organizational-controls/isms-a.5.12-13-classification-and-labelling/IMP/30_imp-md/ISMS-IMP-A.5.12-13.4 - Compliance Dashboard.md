# ISMS-IMP-A.5.12-13.4 - Compliance Dashboard

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.12-13.4 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.12-13 Classification and Labelling |
| **Parent Policy** | ISMS-POL-A.5.12-13 - Information Classification and Labelling |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# PART I: USER COMPLETION GUIDE

---

## 1.1 Assessment Overview

### Purpose

This workbook provides a comprehensive compliance dashboard for monitoring the organisation's classification and labelling program effectiveness. It delivers executive-level visibility into classification scheme adoption, labelling compliance, and program maturity.

The assessment serves multiple purposes:
- **Monitor**: Track classification and labelling compliance metrics
- **Assess**: Evaluate control implementation against ISO 27001 requirements
- **Measure**: Determine program maturity using CMMI-based model
- **Manage Risk**: Identify and track classification-related risks
- **Report**: Provide executive dashboard for governance oversight

### Scope

The Compliance Dashboard covers:

| Dashboard Area | Coverage | Key Outputs |
|----------------|----------|-------------|
| **Executive Summary** | Overall compliance status | Traffic light status, key metrics |
| **Compliance Metrics** | Detailed KPIs | 10+ metrics with targets |
| **Control Assessment** | A.5.12 and A.5.13 evaluation | Per-requirement compliance |
| **Maturity Assessment** | Program maturity scoring | CMMI levels per domain |
| **Risk Register** | Classification-related risks | Risk ratings, mitigation status |
| **Remediation Tracker** | Action item progress | Open/closed remediation items |

**Inclusions:**
- Classification scheme compliance (A.5.12)
- Labelling procedures compliance (A.5.13)
- Asset classification coverage
- Training and awareness metrics
- Audit findings and remediation
- Risk and exception tracking

**Exclusions:**
- Operational metrics covered by other dashboards
- Individual document-level tracking (covered by A.5.12-13.3)
- Real-time monitoring (use operational tools)

### Business Value

| Value Area | Benefit |
|------------|---------|
| **Executive Visibility** | Management dashboard for governance decisions |
| **Audit Readiness** | Consolidated evidence of control effectiveness |
| **Trend Analysis** | Track improvement over time |
| **Risk Awareness** | Highlight classification-related risks |
| **Resource Justification** | Data-driven case for security investment |

### Assessment Frequency

| Assessment Type | Frequency | Trigger Events |
|-----------------|-----------|----------------|
| Full Dashboard Review | Quarterly | Management review cycle |
| Metric Updates | Monthly | Operational reporting |
| Control Assessment | Annual | Certification audit |
| Maturity Assessment | Annual | Strategic planning |

---

## 1.2 Control Requirements

### ISO 27001:2022 Controls A.5.12 & A.5.13

Per ISO/IEC 27001:2022:

**Control A.5.12:**
> *"Information should be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements."*

**Control A.5.13:**
> *"An appropriate set of procedures for information labelling should be developed and implemented in accordance with the information classification scheme adopted by the organization."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Identify, Protect
**Operational Capabilities:** Asset Management, Information Protection

### Key Compliance Objectives

| Objective | Metric |
|-----------|--------|
| **Classification Coverage** | 100% of assets classified |
| **Labelling Compliance** | ≥95% of CONFIDENTIAL/RESTRICTED assets labelled |
| **Training Completion** | 100% of staff trained |
| **Review Currency** | 100% of classifications current |
| **Exception Management** | <2% exception rate |

### What Auditors Look For

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Monitoring** | Evidence of regular compliance tracking |
| **Metrics** | Defined KPIs with targets and actuals |
| **Trends** | Improvement over time |
| **Risk Management** | Classification risks identified and managed |
| **Remediation** | Actions closed on time |
| **Management Review** | Executive oversight and approval |

---

## 1.3 Prerequisites

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| A.5.12-13.1-3 Workbooks | Source data | Read access |
| GRC Platform | Compliance data | Read access |
| Training System | Completion rates | Read access |
| Audit Reports | Finding status | Read access |

### Required Documents

- [ ] ISMS-IMP-A.5.12-13.1 - Classification Scheme Definition (completed)
- [ ] ISMS-IMP-A.5.12-13.2 - Labelling Procedures (completed)
- [ ] ISMS-IMP-A.5.12-13.3 - Asset Classification Inventory (completed)
- [ ] Prior compliance dashboards (if applicable)
- [ ] Internal/external audit reports
- [ ] Risk register entries for classification

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Assessment Lead** | Compile dashboard data | 6-8 hours |
| **CISO** | Review and approve | 2-3 hours |
| **Internal Audit** | Validate metrics | 2-4 hours |
| **Risk Manager** | Risk register input | 2-3 hours |
| **Compliance Officer** | Regulatory compliance | 2-3 hours |

---

## 1.4 Workbook Structure

### Sheet Overview

| Sheet | Purpose | Assessor Action |
|-------|---------|-----------------|
| **Executive_Summary** | High-level status | Complete key metrics |
| **Compliance_Metrics** | Detailed KPIs | Populate all metrics |
| **Control_Assessment** | A.5.12/A.5.13 evaluation | Assess each requirement |
| **Maturity_Assessment** | Program maturity | Score each domain |
| **Risk_Register** | Classification risks | Document risks |
| **Remediation_Tracker** | Action tracking | Track remediation |
| **Evidence_Register** | Audit evidence | Document evidence |
| **Approval_SignOff** | Authorisation | Obtain signatures |

### Data Flow

```
A.5.12-13.1 (Scheme) ────────┐
                             │
A.5.12-13.2 (Labelling) ────►│──► Compliance_Metrics
                             │          │
A.5.12-13.3 (Inventory) ────┘          ▼
                                  Executive_Summary
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
        ▼                              ▼                              ▼
Control_Assessment           Maturity_Assessment              Risk_Register
        │                              │                              │
        └──────────────────────────────┼──────────────────────────────┘
                                       ▼
                              Remediation_Tracker
                                       │
                                       ▼
                              Evidence_Register
                                       │
                                       ▼
                              Approval_SignOff
```

---

## 1.5 Completion Walkthrough

### Step 1: Complete Executive Summary

**Time allocation:** 1-2 hours

**Purpose:** Provide high-level compliance status for management.

**Overall Compliance Status Items:**

| Status Item | Target | What to Assess |
|-------------|--------|----------------|
| Classification Scheme Defined | Complete | A.5.12-13.1 approved and published |
| Labelling Procedures Documented | Complete | A.5.12-13.2 approved and published |
| Asset Inventory Coverage | 100% | % of assets with classification |
| Staff Awareness Training | 100% | Training completion rate |
| Automated Labelling Deployed | 90%+ | Tool coverage of asset types |
| Periodic Review Conducted | Complete | Annual review completed |

**Key Metrics:**

| Metric | Target | Source |
|--------|--------|--------|
| Total Assets Classified | 100% | A.5.12-13.3 |
| Assets Properly Labelled | 95% | A.5.12-13.3 |
| Classification Review Currency | 100% | A.5.12-13.3 (reviews within policy period) |
| Labelling Tool Coverage | 90% | A.5.12-13.2 (automation status) |
| Training Completion Rate | 100% | LMS records |
| Exception Requests (Open) | <5 | Exception register |

### Step 2: Populate Compliance Metrics

**Time allocation:** 2-3 hours

**Purpose:** Document detailed KPIs with targets and actuals.

**Metrics to Track:**

| Metric ID | Metric Name | Target | Measurement Method |
|-----------|-------------|--------|-------------------|
| M-CL-001 | Classification Coverage | 100% | Asset inventory count |
| M-CL-002 | Labelling Compliance | 95% | Labelling audit |
| M-CL-003 | Classification Currency | 100% | Review date tracking |
| M-CL-004 | Reclassification Timeliness | <5 days | Request tracking |
| M-CL-005 | Training Completion | 100% | LMS records |
| M-CL-006 | Automation Coverage | 90% | Tool inventory |
| M-CL-007 | Exception Rate | <2% | Exception register |
| M-CL-008 | Incident Rate | 0/quarter | Incident tracking |
| M-CL-009 | Audit Findings | 0 | Audit reports |
| M-CL-010 | Policy Acknowledgment | 100% | HR records |

**For Each Metric:**

| Field | Description | Example |
|-------|-------------|---------|
| Metric_ID | Unique identifier | M-CL-001 |
| Metric_Name | Descriptive name | Classification Coverage |
| Description | What it measures | % of assets with assigned classification |
| Measurement_Method | How to measure | Asset inventory count |
| Target | Goal value | 100% |
| Current | Actual value | 97% |
| Trend | Direction | Improving/Stable/Declining |
| Owner | Accountable person | InfoSec |
| Status | RAG status | On Target/At Risk/Below Target |

### Step 3: Complete Control Assessment

**Time allocation:** 2-3 hours

**Purpose:** Evaluate compliance with specific A.5.12 and A.5.13 requirements.

**A.5.12 Classification Assessment:**

| Requirement | Implementation | Evidence | Gap | Score |
|-------------|---------------|----------|-----|-------|
| Classification scheme defined based on CIA needs | | | | |
| Classification considers legal/regulatory requirements | | | | |
| Information owners assigned and trained | | | | |
| Classification review process established | | | | |
| Reclassification procedures documented | | | | |
| Cross-organisation classification alignment | | | | |

**A.5.13 Labelling Assessment:**

| Requirement | Implementation | Evidence | Gap | Score |
|-------------|---------------|----------|-----|-------|
| Labelling procedures reflect classification scheme | | | | |
| Labels applied to physical and digital assets | | | | |
| Labels easily recognisable | | | | |
| Metadata tagging implemented | | | | |
| Labelling guidance for transmission | | | | |
| Staff trained on labelling procedures | | | | |

**Scoring Scale:**
- 5 - Optimised: Continuous improvement, automated, metrics-driven
- 4 - Managed: Measured and controlled, consistent performance
- 3 - Defined: Documented, standardised across organisation
- 2 - Developing: Reactive, informal, department-specific
- 1 - Initial: Ad hoc, unpredictable, poorly controlled
- 0 - Non-existent: No awareness, no processes

### Step 4: Complete Maturity Assessment

**Time allocation:** 2-3 hours

**Purpose:** Assess program maturity across key domains.

**Maturity Domains:**

| Domain | Current Level | Target Level | Gap | Priority |
|--------|--------------|--------------|-----|----------|
| Policy & Governance | | | | |
| Classification Scheme | | | | |
| Labelling Standards | | | | |
| Asset Inventory | | | | |
| Automation & Tools | | | | |
| Training & Awareness | | | | |
| Monitoring & Metrics | | | | |
| Incident Response | | | | |
| **OVERALL MATURITY** | | | | |

**Maturity Scale:**
- Level 5: Optimised - Continuous improvement, fully automated
- Level 4: Managed - Measured and controlled
- Level 3: Defined - Documented and standardised
- Level 2: Developing - Reactive and informal
- Level 1: Initial - Ad hoc and unpredictable
- Level 0: Non-existent - No awareness

### Step 5: Document Classification Risks

**Time allocation:** 1-2 hours

**Purpose:** Identify and track risks related to classification and labelling.

**Common Classification Risks:**

| Risk | Category | Typical Mitigation |
|------|----------|-------------------|
| Unclassified sensitive data exposed | Data Breach | Auto-classification |
| Inconsistent labelling leads to mishandling | Compliance | Standardised tools |
| Staff unaware of classification requirements | Human Error | Training program |
| Classification not reviewed as data ages | Data Lifecycle | Automated reminders |
| Third-party systems cannot apply labels | Integration | Compensating controls |

**Risk Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Risk_ID | Unique identifier | RSK-CL-001 |
| Risk_Description | What could happen | Unclassified sensitive data exposed |
| Risk_Category | Type of risk | Data Breach |
| Likelihood | Probability (1-5) | 3 - Possible |
| Impact | Consequence (1-5) | 4 - Major |
| Risk_Score | Likelihood x Impact | 12 |
| Mitigation | Control measure | Implement auto-classification |
| Owner | Responsible person | InfoSec |
| Status | Current state | In Progress |
| Review_Date | Next review | 2026-04-01 |

### Step 6: Track Remediation Actions

**Time allocation:** 1-2 hours

**Purpose:** Consolidate and track all remediation actions.

**Remediation Sources:**
- Audit findings
- Risk assessments
- Gap analyses
- Incident investigations
- Self-assessments
- Regulatory requirements

**Remediation Record Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Action_ID | Unique identifier | ACT-CL-001 |
| Description | What needs to be done | Deploy MIP to remaining workstations |
| Source | Where it came from | Gap Analysis |
| Priority | Urgency level | High |
| Owner | Responsible person | IT Operations |
| Due_Date | Deadline | 2026-03-31 |
| Progress | % complete | 50% |
| Status | Current state | In Progress |
| Notes | Additional detail | Pilot complete, rollout in progress |

### Step 7: Obtain Approvals

**Time allocation:** 1-2 hours

**Purpose:** Secure formal approval of compliance dashboard.

**Required Approvals:**

| Approver | What They Approve | Criteria |
|----------|-------------------|----------|
| **CISO** | Overall compliance status | Accurate and complete |
| **Internal Audit** | Metric accuracy | Validated against source |
| **Compliance Officer** | Regulatory compliance | Requirements addressed |
| **DPO** | Data protection status | GDPR/nDSG compliance |

---

## 1.6 Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| This dashboard workbook | Generated | 7 years |
| Source workbooks (A.5.12-13.1-3) | Related assessments | 7 years |
| Audit reports | Internal/external audit | 7 years |
| Training records | LMS | Duration + 2 years |
| Risk assessments | Risk register | 3 years |
| Remediation completion evidence | Change tickets | 3 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.12-13/Compliance-Dashboard/[Year]/`

**Folder Structure:**
```
A.5.12-13/
|-- Compliance-Dashboard/
|   |-- 2026/
|   |   |-- Q1/
|   |   |   |-- ISMS-IMP-A.5.12-13.4_Compliance_Dashboard_20260204.xlsx
|   |   |-- Q2/
|   |   |-- Q3/
|   |   |-- Q4/
|   |   |-- Annual/
|   |   |-- Evidence/
|   |   |   |-- Audit-Reports/
|   |   |   |-- Training-Records/
|   |   |   |-- Risk-Assessments/
|   |   |   |-- Approvals/
```

---

## 1.7 Common Pitfalls

Avoid these common mistakes when completing the compliance dashboard:

### Metrics Pitfalls

❌ **MISTAKE**: Using old or unvalidated data for metrics
✅ **CORRECT**: Source metrics from current data; document data collection date

❌ **MISTAKE**: Metrics without clear targets
✅ **CORRECT**: Every metric needs a defined target for meaningful assessment

❌ **MISTAKE**: Metrics that cannot be measured consistently
✅ **CORRECT**: Define measurement method and ensure it can be repeated

❌ **MISTAKE**: Too many metrics (information overload)
✅ **CORRECT**: Focus on 10-15 key metrics aligned with control objectives

### Assessment Pitfalls

❌ **MISTAKE**: Self-assessing as fully compliant without evidence
✅ **CORRECT**: Support every compliance claim with documented evidence

❌ **MISTAKE**: Skipping maturity assessment ("we're not mature enough")
✅ **CORRECT**: Maturity assessment identifies improvement areas; do it honestly

❌ **MISTAKE**: Not linking risks to controls
✅ **CORRECT**: Every classification risk should trace to A.5.12 or A.5.13

### Remediation Pitfalls

❌ **MISTAKE**: Remediation items without owners
✅ **CORRECT**: Every action must have a named owner

❌ **MISTAKE**: Perpetually "in progress" items with no movement
✅ **CORRECT**: Set realistic due dates; escalate overdue items

❌ **MISTAKE**: Closing items without completion evidence
✅ **CORRECT**: Document evidence of completion before marking done

### Reporting Pitfalls

❌ **MISTAKE**: Dashboard shows only good news
✅ **CORRECT**: Include gaps, risks, and areas for improvement

❌ **MISTAKE**: No trend data (single point in time)
✅ **CORRECT**: Include previous period comparison where available

---

## 1.8 Quality Checklist

Before submitting the dashboard, verify:

### Executive Summary Checks

- [ ] All status items have current assessment
- [ ] Key metrics populated with targets and actuals
- [ ] Assessment period clearly stated
- [ ] Next review date set

### Metrics Checks

- [ ] All defined metrics populated
- [ ] Targets specified for each metric
- [ ] Current values from recent data
- [ ] Trends calculated where applicable
- [ ] Owners assigned
- [ ] RAG status accurate

### Control Assessment Checks

- [ ] All A.5.12 requirements assessed
- [ ] All A.5.13 requirements assessed
- [ ] Evidence documented for each
- [ ] Gaps identified
- [ ] Scores assigned per maturity scale

### Maturity Assessment Checks

- [ ] All domains assessed
- [ ] Current and target levels specified
- [ ] Gaps calculated
- [ ] Priorities assigned
- [ ] Overall maturity calculated

### Risk and Remediation Checks

- [ ] Risks identified and scored
- [ ] Mitigations documented
- [ ] Remediation actions tracked
- [ ] Overdue items escalated
- [ ] Closed items have evidence

---

## 1.9 Review and Approval

### Review Workflow

```
Assessment Lead Compiles Dashboard
        │
        ▼
Data Validation (Internal Audit)
        │
        ▼
Risk Review (Risk Manager)
        │
        ▼
Compliance Review (Compliance Officer)
        │
        ▼
CISO Review and Approval
        │
        ▼
Executive Presentation
        │
        ▼
Dashboard Approved
```

### Approval Signatures

The Approval_SignOff sheet requires:

1. **Assessment Lead Certification:**
   - Confirms data accuracy
   - Confirms complete coverage
   - Date and signature

2. **Internal Audit Validation:**
   - Confirms metrics validated
   - Confirms evidence reviewed
   - Date and signature

3. **Compliance Officer Review:**
   - Confirms regulatory alignment
   - Confirms risk coverage
   - Date and signature

4. **CISO Approval:**
   - Approves overall dashboard
   - Accepts compliance status
   - Date and signature

---

# PART II: TECHNICAL SPECIFICATION

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.12-13.4_Compliance_Dashboard_YYYYMMDD.xlsx` |
| Generator | `generate_a512_13_4_compliance_dashboard.py` |
| Sheets | 8 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Executive_Summary | High-level status | 30 | 8 |
| 2 | Compliance_Metrics | Detailed KPIs | 30 | 9 |
| 3 | Control_Assessment | A.5.12/A.5.13 eval | 30 | 6 |
| 4 | Maturity_Assessment | Maturity scoring | 30 | 6 |
| 5 | Risk_Register | Risk tracking | 30 | 10 |
| 6 | Remediation_Tracker | Action tracking | 40 | 9 |
| 7 | Evidence_Register | Audit evidence | 30 | 8 |
| 8 | Approval_SignOff | Authorisation | 20 | 6 |

---

## 2.2 Sheet Specifications

### Sheet 1: Executive_Summary

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Status_Item / Metric | 35 | Text | Pre-populated |
| B | Status / Value | 20 | Text/Number | Input |
| C | Target | 15 | Text | Pre-populated |
| D | Status | 18 | List | Complete, In Progress, Not Started, N/A |

**Sections:**
- Overall Compliance Status (rows 5-10)
- Key Metrics (rows 14-20)
- Assessment Period (rows 23-27)

### Sheet 2: Compliance_Metrics

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Metric_ID | 12 | Text | None |
| B | Metric_Name | 22 | Text | None |
| C | Description | 35 | Text | None |
| D | Measurement_Method | 22 | Text | None |
| E | Target | 12 | Text | None |
| F | Current | 12 | Number/% | Input |
| G | Trend | 12 | List | Improving, Stable, Declining, New |
| H | Owner | 12 | Text | None |
| I | Status | 15 | List | On Target, At Risk, Below Target, N/A |

### Sheet 3: Control_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Requirement | 45 | Text | Pre-populated |
| B | Implementation | 30 | Text | Input |
| C | Evidence | 25 | Text | Input |
| D | Gap | 25 | Text | Input |
| E | Score | 18 | List | 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| F | Status | 15 | List | Compliant, Partial, Non-Compliant, N/A |

**Sections:**
- A.5.12: Classification of Information (rows 5-11)
- A.5.13: Labelling of Information (rows 15-21)

### Sheet 4: Maturity_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Domain | 25 | Text | Pre-populated |
| B | Current_Level | 18 | List | 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| C | Target_Level | 18 | List | Same as above |
| D | Gap | 10 | Formula | Auto-calculated |
| E | Priority | 12 | List | Critical, High, Medium, Low, N/A |
| F | Notes | 35 | Text | Input |

### Sheet 5: Risk_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Risk_ID | 12 | Text | None |
| B | Risk_Description | 35 | Text | None |
| C | Risk_Category | 15 | Text | None |
| D | Likelihood | 18 | List | 5 - Almost Certain, 4 - Likely, 3 - Possible, 2 - Unlikely, 1 - Rare |
| E | Impact | 18 | List | 5 - Catastrophic, 4 - Major, 3 - Moderate, 2 - Minor, 1 - Insignificant |
| F | Risk_Score | 12 | Formula | Auto-calculated |
| G | Mitigation | 30 | Text | None |
| H | Owner | 12 | Text | None |
| I | Status | 15 | List | Mitigated, In Progress, Open, Accepted, Transferred |
| J | Review_Date | 12 | Date | None |

### Sheet 6: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Action_ID | 12 | Text | None |
| B | Description | 40 | Text | None |
| C | Source | 18 | List | Audit Finding, Risk Assessment, Gap Analysis, Incident, Self-Assessment, Regulatory, Other |
| D | Priority | 12 | List | Critical, High, Medium, Low |
| E | Owner | 15 | Text | None |
| F | Due_Date | 12 | Date | None |
| G | Progress | 12 | List | 0%, 25%, 50%, 75%, 100% |
| H | Status | 15 | List | Complete, In Progress, Not Started, On Hold, Cancelled |
| I | Notes | 30 | Text | None |

### Sheet 7: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Description | 40 | Text | None |
| C | Evidence_Type | 20 | List | Policy document, Procedure, Configuration, Screenshot, Training record, Audit report, Assessment, Metrics report, Other |
| D | Related_Control | 15 | List | A.5.12, A.5.13, Both |
| E | Location | 30 | Text | None |
| F | Collected_Date | 15 | Date | None |
| G | Collected_By | 15 | Text | None |
| H | Verification_Status | 18 | List | Verified, Pending Review, Not Verified, Expired |

### Sheet 8: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 35 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Signature | 20 | Text | Input |
| D | Date | 15 | Date | Input |
| E | Decision | 22 | List | Approved, Approved with conditions, Rejected, Pending |
| F | Comments | 30 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Executive_Summary | D:D | ="Complete" | Green fill (#C6EFCE) |
| Executive_Summary | D:D | ="In Progress" | Yellow fill (#FFEB9C) |
| Executive_Summary | D:D | ="Not Started" | Red fill (#FFC7CE) |
| Compliance_Metrics | I:I | ="On Target" | Green fill (#C6EFCE) |
| Compliance_Metrics | I:I | ="At Risk" | Yellow fill (#FFEB9C) |
| Compliance_Metrics | I:I | ="Below Target" | Red fill (#FFC7CE) |
| Compliance_Metrics | G:G | ="Improving" | Green text |
| Compliance_Metrics | G:G | ="Declining" | Red text |
| Control_Assessment | F:F | ="Compliant" | Green fill (#C6EFCE) |
| Control_Assessment | F:F | ="Partial" | Yellow fill (#FFEB9C) |
| Control_Assessment | F:F | ="Non-Compliant" | Red fill (#FFC7CE) |
| Maturity_Assessment | D:D | >0 | Red fill (#FFC7CE) |
| Maturity_Assessment | D:D | =0 | Green fill (#C6EFCE) |
| Risk_Register | I:I | ="Open" | Red fill (#FFC7CE) |
| Risk_Register | I:I | ="In Progress" | Yellow fill (#FFEB9C) |
| Risk_Register | I:I | ="Mitigated" | Green fill (#C6EFCE) |
| Remediation_Tracker | H:H | ="Complete" | Green fill (#C6EFCE) |
| Remediation_Tracker | H:H | ="Not Started" | Red fill (#FFC7CE) |
| Remediation_Tracker | H:H | ="In Progress" | Yellow fill (#FFEB9C) |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| A.5.12-13.1 Workbook | Scheme compliance | A.5.12-13.1 -> Control_Assessment |
| A.5.12-13.2 Workbook | Labelling compliance | A.5.12-13.2 -> Control_Assessment |
| A.5.12-13.3 Workbook | Inventory metrics | A.5.12-13.3 -> Compliance_Metrics |
| A.5.12-13.5 Workbook | Consolidation | This workbook -> A.5.12-13.5 |
| GRC Platform | Compliance data | Bidirectional |
| Risk Register | Risk data | ISMS-REG-RISK -> Risk_Register |
| Training System | Completion rates | LMS -> Compliance_Metrics |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.12-13 | Information Classification and Labelling | Parent policy |
| ISMS-IMP-A.5.12-13.1 | Classification Scheme Definition | Scheme source |
| ISMS-IMP-A.5.12-13.2 | Labelling Procedures and Standards | Labelling source |
| ISMS-IMP-A.5.12-13.3 | Asset Classification Inventory | Inventory source |
| ISMS-IMP-A.5.12-13.5 | Consolidation Dashboard | Executive consolidation |
| ISMS-REG-RISK | Risk Register | Risk integration |

---

**END OF SPECIFICATION**

---

*"Without data, you're just another person with an opinion."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-04 -->
