<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.10-11.S4-UG:framework:UG:a.5.10-11 -->
**ISMS-IMP-A.5.10-11.S4-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.10-11

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.S4-UG |
| **Title** | Asset Usage Lifecycle Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10-11 |
| **Control Name** | Asset Usage Lifecycle |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.10-11.S4-TG.

---

### Assessment Overview

**Purpose**

This dashboard workbook provides consolidated compliance monitoring for both A.5.10 (Acceptable Use) and A.5.11 (Return of Assets) controls. It aggregates metrics from the other assessment workbooks to provide executive-level visibility into asset usage lifecycle compliance. The dashboard serves as the primary reporting mechanism for management review and continuous improvement tracking.

**Scope**

This dashboard covers:
- Executive summary of compliance status across both controls
- A.5.10 compliance metrics and scoring (Acceptable Use)
- A.5.11 compliance metrics and scoring (Return of Assets)
- Consolidated gap register from all assessments
- Remediation tracking and progress monitoring
- Trend analysis over time showing compliance trajectory
- Management reporting and executive briefings
- Audit readiness status

**What This Dashboard Covers**

| Domain | Dashboard Focus |
|--------|-----------------|
| Executive Summary | High-level compliance overview with KPI boxes |
| A.5.10 Compliance | Acceptable use policy and enforcement metrics |
| A.5.11 Compliance | Asset return and offboarding metrics |
| Gap Management | Consolidated gap tracking across controls |
| Remediation | Action item progress and SLA compliance |
| Trends | Historical compliance tracking and trajectory |
| Risk Status | Current risk exposure from gaps |

**Dashboard Users**

| User | Dashboard Usage |
|------|-----------------|
| CISO | Executive oversight, risk decisions |
| Information Security Manager | Operational management, reporting |
| IT Manager | Technical compliance verification |
| HR Manager | Offboarding process compliance |
| Internal Audit | Compliance verification |
| External Auditors | Evidence of continuous monitoring |

**Update Frequency**

| Component | Update Frequency |
|-----------|------------------|
| KPI Values | Monthly |
| Gap Register | As changes occur |
| Remediation Status | Weekly |
| Trend Data | Quarterly |
| Full Dashboard | Monthly with quarterly deep-dive |

### Control Requirements

**ISO 27001:2022 A.5.10 - Acceptable Use of Information and Other Associated Assets**

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."

**ISO 27001:2022 A.5.11 - Return of Assets**

> "Personnel and other interested parties as appropriate should return all the organisation's assets in their possession upon change or termination of their employment, contract or agreement."

**Combined Control Objectives**

The dashboard tracks compliance with both controls through the complete asset lifecycle:

| Lifecycle Stage | Control | Dashboard Tracking |
|-----------------|---------|-------------------|
| Onboarding | A.5.10 | Policy acknowledgement, training completion |
| Active Use | A.5.10 | Usage rules compliance, monitoring effectiveness |
| Role Change | Both | Access modification, asset reassignment |
| Offboarding | A.5.11 | Asset return completion, access revocation |

**Compliance Scoring Framework**

| Score Range | Compliance Level | Action Required |
|-------------|------------------|-----------------|
| 90-100% | Strong | Maintain and continuously improve |
| 75-89% | Adequate | Address identified gaps |
| 60-74% | Partial | Develop remediation plan |
| Below 60% | Inadequate | Immediate management attention |

### Prerequisites

Before completing this dashboard, ensure:

**Source Assessment Prerequisites**

- [ ] ISMS-IMP-A.5.10-11.S1 (Acceptable Use Policy Assessment) completed
- [ ] ISMS-IMP-A.5.10-11.S2 (Usage Rules Inventory) completed
- [ ] ISMS-IMP-A.5.10-11.S3 (Asset Return Assessment) completed
- [ ] All source assessments are current (within 30 days)
- [ ] Compliance scores calculated in source assessments

**Data Prerequisites**

- [ ] Access to compliance metrics from underlying assessments
- [ ] Gap remediation status from responsible parties
- [ ] Historical trend data from previous periods
- [ ] Current risk register for gap risk ratings

**Stakeholder Prerequisites**

- [ ] ISM available for dashboard compilation
- [ ] Gap owners contacted for status updates
- [ ] CISO briefing scheduled (for quarterly reviews)

### Key Terminology

| Term | Definition |
|------|------------|
| **KPI** | Key Performance Indicator - measurable value demonstrating compliance effectiveness |
| **Gap** | Identified deficiency between current state and control requirements |
| **Remediation** | Action taken to close a gap and achieve compliance |
| **Trend** | Compliance score change over time |
| **Target** | Expected or required value for a metric |
| **Variance** | Difference between actual and target values |
| **SLA** | Service Level Agreement - target timeframe for actions |
| **Risk Acceptance** | Documented approval to accept residual risk from unresolved gap |
| **Aggregation** | Combining data from multiple sources into summary metrics |

### Dashboard Architecture

**Dashboard Hierarchy**

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXECUTIVE SUMMARY                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │   Overall   │  │   A.5.10    │  │   A.5.11    │              │
│  │ Compliance  │  │ Compliance  │  │ Compliance  │              │
│  │    85%      │  │    88%      │  │    82%      │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│  Key Findings | Open Gaps | Overdue Remediations                │
└─────────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ A.5.10 Detail   │  │ Gap Register    │  │ A.5.11 Detail   │
│ - Policy        │  │ - All gaps      │  │ - Process       │
│ - Coverage      │  │ - Severity      │  │ - Return rate   │
│ - Awareness     │  │ - Status        │  │ - Revocation    │
│ - Enforcement   │  │ - Owners        │  │ - Data wipe     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │                    │
         └──────────────┬─────┴────────────────────┘
                        ▼
              ┌─────────────────────┐
              │  Remediation        │
              │  Tracker            │
              │  - Actions          │
              │  - Progress         │
              │  - SLA compliance   │
              └─────────────────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │  Trend Analysis     │
              │  - Historical       │
              │  - Trajectory       │
              │  - Predictions      │
              └─────────────────────┘
```

**Data Flow**

| Source | Data | Destination |
|--------|------|-------------|
| ISMS-IMP-A.5.10-11.S1 | Policy compliance scores | A510_Compliance, Executive_Summary |
| ISMS-IMP-A.5.10-11.S2 | Usage rules coverage | A510_Compliance, Executive_Summary |
| ISMS-IMP-A.5.10-11.S3 | Return/revocation metrics | A511_Compliance, Executive_Summary |
| All assessments | Identified gaps | Gap_Register |
| Gap_Register | Gap details | Remediation_Tracker |
| All sheets | Current scores | Trend_Analysis |

### Key Performance Indicators

**Executive KPIs**

| KPI | Formula | Target | Source |
|-----|---------|--------|--------|
| Overall Compliance | (A.5.10 Score + A.5.11 Score) / 2 | ≥85% | Calculated |
| A.5.10 Compliance | Sum of A.5.10 requirements met / Total | ≥85% | A510_Compliance |
| A.5.11 Compliance | Sum of A.5.11 requirements met / Total | ≥85% | A511_Compliance |

**A.5.10 Operational KPIs**

| KPI | Definition | Target | Measurement |
|-----|------------|--------|-------------|
| AUP Policy Completeness | % of required policy elements documented | 100% | Policy assessment score |
| Asset Category Coverage | % of asset types with defined usage rules | 100% | Inventory coverage |
| User Acknowledgment Rate | % of users who have signed AUP | 100% | Acknowledgment records |
| Training Completion | % of users completing security awareness | 95%+ | LMS records |
| Violation Rate | # of AUP violations per 1000 users | <5 | Incident records |
| Third-Party Compliance | % of third parties with AUP agreements | 100% | Contract records |

**A.5.11 Operational KPIs**

| KPI | Definition | Target | Measurement |
|-----|------------|--------|-------------|
| Return Process Requirements | % of process requirements implemented | 100% | Process assessment |
| Offboarding Completion Rate | % of offboardings fully completed | 100% | Tracking records |
| Asset Return Rate | Assets returned / Assets assigned | 100% | Inventory records |
| Access Revocation SLA | % revoked within SLA (24 hours) | 95%+ | Revocation logs |
| Data Wipe Completion | % of devices wiped after return | 100% | Wipe certificates |
| Overdue Returns | Count of returns past deadline | 0 | Tracking records |

**Gap and Remediation KPIs**

| KPI | Definition | Target |
|-----|------------|--------|
| Open Gaps | Count of gaps not yet closed | Decreasing trend |
| Critical/High Open | Count of Critical/High severity gaps | 0 |
| Remediation On-Time | % of remediations completed by due date | 90%+ |
| Average Gap Age | Mean days gaps remain open | <30 days |
| Accepted Gaps | Count of gaps with risk acceptance | Minimise |

### Data Aggregation Framework

**Score Aggregation Rules**

| Compliance Status | Score Value |
|-------------------|-------------|
| Compliant | 1.0 |
| Partial | 0.5 |
| Non-Compliant | 0.0 |
| Not Assessed | Excluded from calculation |

**Compliance Score Calculation**

```
Control Score = (Sum of Requirement Scores / Number of Assessed Requirements) × 100

Overall Score = (A.5.10 Score + A.5.11 Score) / 2
```

**Gap Severity Weighting**

| Severity | Weight | Impact on Risk Score |
|----------|--------|---------------------|
| Critical | 4 | Significantly increases risk |
| High | 3 | Moderately increases risk |
| Medium | 2 | Minor increase to risk |
| Low | 1 | Minimal impact |

**Risk Score Calculation**

```
Gap Risk Score = Σ (Gap Severity Weight × Gap Count by Severity)

Risk Status:
- Low: Risk Score < 5
- Medium: Risk Score 5-10
- High: Risk Score 11-20
- Critical: Risk Score > 20
```

### Completion Walkthrough

**Step 1: Document Information (Instructions Sheet)**

Complete dashboard metadata:

| Field | Input Required |
|-------|----------------|
| Dashboard Title | Pre-populated |
| Document ID | Pre-populated (ISMS-IMP-A.5.10-11.S4) |
| Control Reference | Pre-populated (A.5.10-11) |
| Reporting Period | Start and end dates |
| Compiled By | Person compiling dashboard |
| Compilation Date | Date of compilation |
| Version | Dashboard version number |

**Step 2: Executive Summary (Executive_Summary Sheet)**

**2a. KPI Boxes**
Populate the three KPI boxes at the top:

| Box | Content | Source |
|-----|---------|--------|
| Overall Compliance | Combined score percentage | Calculated from below |
| A.5.10 Compliance | Acceptable Use score | A510_Compliance total |
| A.5.11 Compliance | Return of Assets score | A511_Compliance total |

**2b. Key Metrics Table**
Enter current values for each tracked metric:

| Metric | Source Assessment | Target | Current Value |
|--------|-------------------|--------|---------------|
| AUP Policy Completeness | ISMS-IMP-A.5.10-11.S1 | 100% | [Enter] |
| Asset Categories Covered | ISMS-IMP-A.5.10-11.S1 | 100% | [Enter] |
| User Acknowledgment Rate | ISMS-IMP-A.5.10-11.S1 | 100% | [Enter] |
| Usage Rules Documented | ISMS-IMP-A.5.10-11.S2 | 100% | [Enter] |
| Return Process Requirements | ISMS-IMP-A.5.10-11.S3 | 100% | [Enter] |
| Offboarding Completion Rate | ISMS-IMP-A.5.10-11.S3 | 100% | [Enter] |
| Access Revocation SLA | ISMS-IMP-A.5.10-11.S3 | 95%+ | [Enter] |

**2c. Key Findings**
Document critical findings and recommendations:

| Column | Content |
|--------|---------|
| Finding/Recommendation | Concise description of issue or recommendation |
| Priority | Critical/High/Medium/Low |
| Owner | Person responsible for addressing |
| Due Date | Target completion date |

**Step 3: A.5.10 Compliance (A510_Compliance Sheet)**

Score each compliance requirement:

1. **Compliance_Area** - Pre-populated category
2. **Requirement** - Specific requirement description
3. **Status** - Compliant/Partial/Non-Compliant/Not Assessed
4. **Score** - Numeric score (0, 0.5, or 1)
5. **Evidence_Ref** - Link to supporting evidence
6. **Last_Assessed** - Date of last assessment
7. **Assessor** - Person who performed assessment
8. **Gap_Notes** - Notes on any gaps identified
9. **Remediation_Ref** - Link to Remediation_Tracker if applicable

**A.5.10 Compliance Areas (19 Requirements)**

| Area | Requirements Covered |
|------|---------------------|
| Policy Framework | AUP exists, approved, published |
| Asset Coverage | All asset types covered |
| User Awareness | Training, acknowledgement |
| Enforcement | Violation handling, consequences |
| Monitoring | Compliance checking, reporting |
| Third Parties | Contractor/vendor coverage |
| Review | Policy currency, updates |

**Step 4: A.5.11 Compliance (A511_Compliance Sheet)**

Score each compliance requirement (same column structure):

**A.5.11 Compliance Areas (20 Requirements)**

| Area | Requirements Covered |
|------|---------------------|
| Process Documentation | Procedures documented |
| Asset Return Tracking | Inventory linkage, checklists |
| Access Revocation | Network, application, physical |
| Data Security | Data wipe, verification |
| Knowledge Transfer | Handover requirements |
| Verification | Completion confirmation |
| Remote Workers | Remote return process |
| Contractors | Third-party offboarding |

**Step 5: Gap Register (Gap_Register Sheet)**

Consolidate gaps from all assessments:

1. **Gap_ID** - Auto-generated identifier (GAP-001, etc.)
2. **Control** - A.5.10, A.5.11, or Both
3. **Source_Assessment** - Which assessment identified the gap
4. **Gap_Description** - Clear description of gap
5. **Gap_Type** - Policy/Process/Technical/Documentation/Training
6. **Severity** - Critical/High/Medium/Low
7. **Risk_Rating** - Associated risk score
8. **Identified_Date** - When gap was identified
9. **Owner** - Person responsible for remediation
10. **Target_Date** - Remediation deadline
11. **Status** - Open/In Progress/Remediated/Accepted/Closed
12. **Remediation_Ref** - Link to Remediation_Tracker
13. **Closure_Date** - Date gap was closed
14. **Notes** - Additional comments

**Gap Status Definitions**

| Status | Definition |
|--------|------------|
| Open | Gap identified, not yet addressed |
| In Progress | Remediation underway |
| Remediated | Fix implemented, awaiting verification |
| Accepted | Risk accepted by management |
| Closed | Gap verified as resolved |

**Step 6: Remediation Tracker (Remediation_Tracker Sheet)**

Track remediation actions:

1. **Remediation_ID** - Auto-generated identifier (REM-001, etc.)
2. **Gap_Ref** - Link to Gap_Register
3. **Action_Description** - Specific action required
4. **Control** - A.5.10/A.5.11/Both
5. **Priority** - Critical/High/Medium/Low
6. **Owner** - Action owner
7. **Assigned_Date** - When action was assigned
8. **Start_Date** - When work began
9. **Target_Date** - Due date
10. **Status** - Not Started/In Progress/On Hold/Completed/Cancelled
11. **% Complete** - Progress percentage
12. **Completion_Date** - Actual completion date
13. **Verification** - How completion was verified
14. **Notes** - Additional comments

**Remediation SLAs**

| Priority | Response Time | Resolution Time |
|----------|---------------|-----------------|
| Critical | 1 business day | 5 business days |
| High | 3 business days | 15 business days |
| Medium | 5 business days | 30 business days |
| Low | 10 business days | 60 business days |

**Step 7: Trend Analysis (Trend_Analysis Sheet)**

Record compliance trends over time:

1. **Assessment_Period** - Quarter/Year (Q1 2025, etc.)
2. **A510_Score** - Acceptable Use compliance score
3. **A510_Change** - Change from previous period
4. **A511_Score** - Return of Assets compliance score
5. **A511_Change** - Change from previous period
6. **Overall_Score** - Combined compliance score
7. **Overall_Change** - Overall change from previous
8. **Open_Gaps** - Number of open gaps
9. **Critical_High_Gaps** - Count of Critical/High gaps
10. **Notes** - Commentary on period changes

**Pre-populated Periods**: Q1 2025 through Q4 2026

**Step 8: Approval (Approval_SignOff Sheet)**

Complete sign-off section:

| Role | Scope | Signature Required |
|------|-------|-------------------|
| Compiler | Data accuracy | Yes |
| Information Security Manager | Completeness, accuracy | Yes |
| CISO | Management approval | Yes (quarterly) |

### Gap Management Framework

**Gap Identification Sources**

| Source | Gap Types Typically Found |
|--------|---------------------------|
| ISMS-IMP-A.5.10-11.S1 | Policy gaps, coverage gaps |
| ISMS-IMP-A.5.10-11.S2 | Documentation gaps, process gaps |
| ISMS-IMP-A.5.10-11.S3 | Process gaps, technical gaps |
| Internal Audit | All types |
| Incident Analysis | Process gaps, control failures |

**Gap Severity Criteria**

| Severity | Criteria |
|----------|----------|
| Critical | Immediate security risk; regulatory non-compliance; potential data breach |
| High | Significant compliance gap; audit finding; material weakness |
| Medium | Notable gap requiring attention; process improvement needed |
| Low | Minor gap; improvement opportunity; optimisation |

**Gap Lifecycle**

```
Identified → Open → In Progress → Remediated → Verified → Closed
                 ↓
              Accepted (with CISO approval)
```

**Escalation Rules**

| Condition | Escalate To | Timeline |
|-----------|-------------|----------|
| Critical gap identified | CISO | Immediately |
| High gap not addressed in 5 days | ISM | Day 6 |
| Medium gap overdue | ISM | Target date +7 |
| Any gap overdue >30 days | CISO | Day 31 |

### Remediation Management

**Remediation Planning**

Each remediation action should include:

| Element | Requirement |
|---------|-------------|
| Clear Description | Specific, actionable task |
| Owner | Named individual (not team) |
| Resources | Identified resources needed |
| Dependencies | Other actions required first |
| Success Criteria | How completion is verified |

**Progress Tracking**

| % Complete | Meaning |
|------------|---------|
| 0% | Not started |
| 25% | Planning complete, work beginning |
| 50% | Midway through implementation |
| 75% | Implementation complete, testing |
| 100% | Verified complete |

**Status Definitions**

| Status | Definition |
|--------|------------|
| Not Started | Action assigned but work not begun |
| In Progress | Active work underway |
| On Hold | Paused due to dependency or decision |
| Completed | Work finished and verified |
| Cancelled | Action no longer required |

### Trend Analysis Framework

**Data Points Required**

Minimum 4 quarterly data points for meaningful trend analysis.

**Trend Interpretation**

| Trend | Interpretation | Action |
|-------|----------------|--------|
| ↑ Improving (>5%) | Positive progress | Continue current approach |
| → Stable (±5%) | Maintenance mode | Review for improvement opportunities |
| ↓ Declining (>5%) | Regression | Investigate root cause; corrective action |

**Trend Calculations**

| Metric | Formula |
|--------|---------|
| Period Change | Current Score - Previous Score |
| Change % | (Current - Previous) / Previous × 100 |
| 4-Quarter Average | Sum of 4 periods / 4 |
| Trend Direction | Compare current to 4-quarter average |

### Reporting and Export

**Report Types**

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| Executive Summary | CISO, Executives | Quarterly | KPIs, key findings, trends |
| Operational Report | ISM, Managers | Monthly | Detailed metrics, gap status |
| Audit Report | Auditors | As needed | Full evidence, compliance scores |
| Board Report | Board | Annual | High-level compliance status |

**Export Formats**

| Format | Use Case |
|--------|----------|
| PDF | Executive presentations, formal reports |
| Excel | Data analysis, detailed review |
| PowerPoint | Management presentations |

**Dashboard Distribution**

| Version | Recipients | Classification |
|---------|------------|----------------|
| Full Dashboard | ISM, CISO, Auditors | Internal |
| Executive Summary | Executive team, Board | Internal |
| Sanitised Version | External auditors | Confidential |

### Evidence Collection

**Required Evidence**

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Source Assessments | Completed ISMS-IMP-A.5.10-11.S1-3 | ISMS Evidence Library |
| Compliance Reports | Generated dashboard exports | ISMS Evidence Library |
| Gap Closure Evidence | Remediation completion proof | ISMS Evidence Library |
| Management Reports | Executive summaries presented | ISMS Evidence Library |
| Approval Records | Sign-off documentation | ISMS Evidence Library |
| Trend Reports | Historical compliance data | ISMS Evidence Library |

**Evidence Requirements**

| Requirement | Specification |
|-------------|---------------|
| Retention | 7 years minimum |
| Format | PDF for reports; native for workbooks |
| Access | Restricted to authorised personnel |
| Backup | Included in ISMS backup procedures |

**Evidence Naming Convention**

```
ISMS-IMP-A.5.10-11.S4_[Report_Type]_[Period]_[Date].[ext]
```

Example: `ISMS-IMP-A.5.10-11.S4_Executive_Summary_Q4-2025_20251215.pdf`

### Common Pitfalls

❌ **MISTAKE**: Using outdated data from underlying assessments
✅ **CORRECT**: Ensure all source assessments are current (within 30 days) before updating dashboard

❌ **MISTAKE**: Not tracking trends over time
✅ **CORRECT**: Maintain historical data to show compliance trajectory; minimum 4 quarters

❌ **MISTAKE**: Gaps without clear ownership
✅ **CORRECT**: Every gap must have an assigned owner (named individual, not team)

❌ **MISTAKE**: Vague or unmeasurable remediation actions
✅ **CORRECT**: Actions should be specific, actionable, and have clear completion criteria

❌ **MISTAKE**: Not escalating overdue remediations
✅ **CORRECT**: Overdue items escalated per governance process to ISM/CISO

❌ **MISTAKE**: Inconsistent scoring methodology across assessments
✅ **CORRECT**: Apply scoring criteria consistently; document any deviations

❌ **MISTAKE**: Dashboard not reviewed before management presentation
✅ **CORRECT**: ISM reviews for accuracy and completeness before CISO presentation

❌ **MISTAKE**: Missing sign-off on management-presented dashboards
✅ **CORRECT**: All dashboards presented to management must be formally approved

❌ **MISTAKE**: Calculating overall score incorrectly
✅ **CORRECT**: Use weighted average accounting for number of requirements per control

❌ **MISTAKE**: Not linking gaps to remediation actions
✅ **CORRECT**: Every open gap should have corresponding remediation in tracker

❌ **MISTAKE**: Accepting gaps without proper authorisation
✅ **CORRECT**: Risk acceptance requires documented CISO approval and risk assessment

❌ **MISTAKE**: Focusing only on compliance scores, ignoring gap severity
✅ **CORRECT**: Track both score and gap severity; one Critical gap is worse than many Low gaps

❌ **MISTAKE**: Not documenting data sources for metrics
✅ **CORRECT**: Each metric should have traceable source reference

❌ **MISTAKE**: Presenting dashboard without context
✅ **CORRECT**: Include narrative explaining significant changes and planned actions

❌ **MISTAKE**: Quarterly updates only
✅ **CORRECT**: Monthly metric updates; quarterly full reviews; continuous gap tracking

❌ **MISTAKE**: Not archiving previous versions
✅ **CORRECT**: Maintain historical dashboard versions for audit trail

### Quality Checklist

Before presenting this dashboard:

**Data Quality**
- [ ] All source assessments current (within 30 days)
- [ ] Compliance scores verified against source data
- [ ] All metrics have documented sources
- [ ] Calculations verified (spot-check at minimum)

**Gap Management**
- [ ] All gaps have assigned owners
- [ ] All gaps have target dates
- [ ] Gap statuses are current
- [ ] Overdue gaps identified and escalated
- [ ] Accepted gaps have documented approval

**Remediation Tracking**
- [ ] All open gaps have remediation actions
- [ ] Remediation owners assigned
- [ ] Progress percentages current
- [ ] Overdue remediations escalated

**Trend Analysis**
- [ ] Current period data entered
- [ ] Change calculations correct
- [ ] Minimum 4 data points present
- [ ] Trend commentary added for significant changes

**Presentation Readiness**
- [ ] Executive summary reflects key messages
- [ ] Key findings are actionable
- [ ] Evidence linked for compliance claims
- [ ] Dashboard reviewed by ISM
- [ ] Approval signatures obtained

### Review & Approval

**Review Workflow**

1. **Compilation** - Assessor compiles dashboard from source assessments
2. **ISM Review** - Information Security Manager verifies accuracy and completeness
3. **CISO Review** - CISO reviews for management presentation (quarterly)
4. **Presentation** - Executive Management receives briefing

**Presentation Cadence**

| Review Type | Frequency | Attendees | Focus |
|-------------|-----------|-----------|-------|
| Metric Update | Monthly | ISM | KPI tracking, gap status |
| Full Review | Quarterly | ISM, CISO | Comprehensive compliance status |
| Annual Review | Annual | ISM, CISO, Executives | Strategic assessment, resource planning |
| Audit Review | As scheduled | ISM, Auditors | Evidence verification |

**Approval Requirements**

| Dashboard Type | Required Approvals |
|----------------|-------------------|
| Monthly Update | ISM |
| Quarterly Review | ISM + CISO |
| Annual Review | ISM + CISO + CFO/CEO |
| Audit Submission | ISM + CISO |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
