**ISMS-IMP-A.8.2-3-5.6 - Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.2, A.8.3, A.8.5: Authentication & Privileged Access

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S6 |
| **Version** | 1.0 |
| **Assessment Area** | Executive Compliance Dashboard & Aggregated Gap Analysis |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Authentication, Privileged Access Rights, Information Access Restriction) |
| **Purpose** | Provide executive-level compliance visibility across all A.8.2-3-5 assessments (S1-S5); aggregate gaps, risks, and remediation tracking into a unified dashboard |
| **Target Audience** | CISO, Executive Management, Security Team, Internal Audit, External Auditors |
| **Assessment Type** | Compliance Aggregation & Executive Reporting |
| **Review Cycle** | Monthly executive review, Quarterly comprehensive update |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial compliance dashboard specification for A.8.2-3-5 control family | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Data Aggregation Guidelines
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Column Definitions
  - Formulas & Calculations
  - Data Import from S1-S5

---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.6 - Compliance Dashboard

**What This Dashboard Does:**

- Aggregates compliance data from all A.8.2-3-5 assessments (S1-S5)
- Provides executive-level compliance score for authentication and privileged access
- Consolidates gaps identified across all assessment workbooks
- Tracks remediation progress and timeline
- Maintains risk register for authentication and privileged access risks
- Provides KPIs and metrics for ongoing compliance monitoring
- Serves as the single source of truth for A.8.2-3-5 compliance status
- Supports ISO 27001 certification audits with consolidated evidence

**What This Dashboard Does NOT Do:**

- Replace individual assessments (S1-S5 remain authoritative for detailed data)
- Perform automated scans or technical assessments
- Generate compliance data (it aggregates existing data)

**Primary ISO 27001 Controls:**

- A.8.2 - Privileged Access Rights
- A.8.3 - Information Access Restriction
- A.8.5 - Secure Authentication

**Related Assessments (Data Sources):**

| Assessment | Name | Data Aggregated |
|------------|------|-----------------|
| S1 | Authentication Inventory | Authentication methods, systems, coverage |
| S2 | MFA Coverage | MFA deployment, gaps, enforcement |
| S3 | Privileged Account Inventory | Privileged accounts, ownership, review |
| S4 | Privileged Monitoring | PAM implementation, session recording |
| S5 | Access Restrictions | Technical access controls, authorization |

**Why a Compliance Dashboard Matters:**

Individual assessments provide detailed technical data. Executives and auditors need:

- Single compliance score (are we compliant?)
- Aggregated gap view (what needs fixing?)
- Risk-based prioritization (what's most important?)
- Remediation tracking (are we making progress?)
- Evidence index (where's the proof?)

## When to Use This Dashboard

**Use this dashboard when:**

- Reporting to executive management (monthly security status)
- Preparing for ISO 27001 certification audits
- Conducting internal audit reviews
- Tracking remediation progress across A.8.2-3-5 controls
- Responding to regulatory inquiries (GDPR Article 32)
- Security committee meetings and board reporting

**Dashboard Frequency:**

- **Monthly**: Executive dashboard review, KPI updates
- **Quarterly**: Comprehensive update (re-aggregate from S1-S5)
- **On-Demand**: Post-incident, pre-audit, significant changes

## Who Completes This Dashboard

**Primary Responsibility:** Security Team (GRC Analyst, Security Manager)

**Supporting Roles:**

- **S1-S5 Assessment Owners**: Provide updated compliance data
- **IT Operations**: Remediation status updates
- **Internal Audit**: Validation and audit evidence review
- **Risk Management**: Risk register input

**Approval Authority:** Chief Information Security Officer (CISO)

## Expected Time Investment

**Initial Dashboard Creation** (first-time setup):

- Data aggregation from S1-S5: 4-6 hours
- Gap consolidation and deduplication: 2-3 hours
- Risk register population: 2-3 hours
- KPI baseline establishment: 1-2 hours
- Evidence register consolidation: 1-2 hours
- Workbook completion: 2-3 hours
- **Total**: 12-19 hours

**Monthly Update**:

- S1-S5 data refresh: 1-2 hours
- Gap and remediation updates: 1 hour
- KPI recalculation: 30 minutes
- Executive summary update: 30 minutes
- **Total**: 3-4 hours per month

**Quarterly Comprehensive Update**:

- Full S1-S5 re-aggregation: 3-4 hours
- Risk register review: 1-2 hours
- Remediation roadmap refresh: 1-2 hours
- Evidence audit: 1-2 hours
- **Total**: 6-10 hours per quarter

---

# Prerequisites

## Required Information

Before creating the dashboard, ensure the following assessments are complete:

**Completed Assessments:**

- [ ] S1 - Authentication Inventory (current, within 90 days)
- [ ] S2 - MFA Coverage (current, within 90 days)
- [ ] S3 - Privileged Account Inventory (current, within 90 days)
- [ ] S4 - Privileged Monitoring (current, within 90 days)
- [ ] S5 - Access Restrictions (current, within 90 days)

**Data to Extract from Each Assessment:**

| Assessment | Data Needed |
|------------|-------------|
| S1 | Total systems, authentication methods, compliance % |
| S2 | MFA coverage %, gaps by system/user type |
| S3 | Privileged account count, orphaned accounts, review status |
| S4 | PAM coverage %, systems without monitoring |
| S5 | Access control compliance %, critical gaps |

**Historical Data (for trend analysis):**

- [ ] Previous dashboard versions (for KPI trends)
- [ ] Historical compliance scores (past 12 months)
- [ ] Closed remediation items (for velocity tracking)

## Required Access

**System Access Needed:**

- [ ] Read access to all S1-S5 assessment workbooks
- [ ] Read access to evidence repository
- [ ] Read access to risk register (if separate system)
- [ ] Read access to remediation tracking system (Jira, ServiceNow, etc.)

**People Access Needed:**

- [ ] S1-S5 assessment owners (for data clarification)
- [ ] Remediation owners (for status updates)
- [ ] CISO (for approval and risk acceptance)

## Required Tools

**Software:**

- [ ] Microsoft Excel 2016 or later
- [ ] Python 3.8+ (if using automated aggregation scripts)
- [ ] Access to S1-S5 workbooks

**Optional Tools:**

- [ ] Power BI or Tableau (for enhanced visualization)
- [ ] GRC platform (ServiceNow GRC, Archer, etc.)
- [ ] Automated aggregation scripts

---

# Assessment Workflow

## Dashboard Process Overview

```
1. COLLECT
   -> Gather current S1-S5 assessment workbooks
   -> Verify assessments are current (within 90 days)
   -> Extract compliance scores and gap data

2. AGGREGATE EXECUTIVE DASHBOARD
   -> Sheet 1: Executive Dashboard
      - Overall A.8.2-3-5 compliance score
      - Component scores (S1-S5)
      - Trend indicators

3. CONSOLIDATE GAPS
   -> Sheet 2: Gap Analysis
      - Import gaps from each assessment
      - Deduplicate overlapping gaps
      - Prioritize by risk

4. BUILD RISK REGISTER
   -> Sheet 3: Risk Register
      - Authentication risks
      - Privileged access risks
      - Risk scoring and treatment

5. CREATE REMEDIATION ROADMAP
   -> Sheet 4: Remediation Roadmap
      - Prioritized remediation plan
      - Timeline and ownership
      - Resource requirements

6. ESTABLISH KPIs
   -> Sheet 5: KPIs & Metrics
      - Define KPIs per control
      - Set targets and thresholds
      - Track trends

7. CONSOLIDATE EVIDENCE
   -> Sheet 6: Evidence Register
      - Index all S1-S5 evidence
      - Map evidence to controls
      - Audit readiness check

8. TRACK ACTIONS
   -> Sheet 7: Action Items & Follow-up
      - Open remediation items
      - Assignment and status
      - Due dates

9. AUDIT LOG
   -> Sheet 8: Audit & Compliance Log
      - Assessment history
      - Audit findings
      - Certification status

10. APPROVAL
    -> Sheet 9: Approval Sign-Off
       - Three-level approval
       - Executive endorsement
```

## Step-by-Step Completion Guide

**Step 1: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_6_compliance_dashboard.py
```
This creates: `ISMS-IMP-A.8.2-3-5.6_Compliance_Dashboard_YYYYMMDD.xlsx`

Option B - Manual:

- Use Excel template
- Save as: `ISMS-IMP-A.8.2-3-5.6_Compliance_Dashboard_[DATE].xlsx`

**Step 2: Complete Sheet 1 - Executive Dashboard**

The Executive Dashboard provides at-a-glance compliance status:

1. **Overall Compliance Score** (Row 5):

   - Calculate weighted average of S1-S5 compliance scores
   - Display as percentage with color indicator
   - Include trend arrow (improving/declining/stable)

2. **Component Scores** (Rows 8-12):

   - S1 Authentication Inventory: % compliant
   - S2 MFA Coverage: % coverage
   - S3 Privileged Account Inventory: % reviewed and current
   - S4 Privileged Monitoring: % systems with PAM
   - S5 Access Restrictions: % compliant

3. **Critical Metrics** (Rows 15-20):

   - Total systems in scope
   - MFA coverage percentage
   - Privileged accounts count
   - Orphaned accounts count
   - Systems without PAM
   - Critical gaps open

4. **Status Indicators**:

   - GREEN (90-100%): Compliant
   - YELLOW (75-89%): Partial, improvement needed
   - RED (<75%): Non-Compliant, immediate action required

**Example Executive Dashboard Data:**
```
Overall A.8.2-3-5 Compliance: 82% [YELLOW]
Trend: Improving (+5% from last quarter)

Component Scores:
- S1 Authentication Inventory: 95% [GREEN]
- S2 MFA Coverage: 78% [YELLOW]
- S3 Privileged Accounts: 85% [YELLOW]
- S4 Privileged Monitoring: 70% [RED]
- S5 Access Restrictions: 82% [YELLOW]

Critical Metrics:
- Total Systems: 156
- MFA Coverage: 78%
- Privileged Accounts: 89
- Orphaned Accounts: 3
- Systems without PAM: 12
- Critical Gaps: 4
```

**Step 3: Complete Sheet 2 - Gap Analysis**

Consolidate gaps from all S1-S5 assessments:

1. **Gap Identification** (Columns A-E):

   - Gap ID: Unique identifier (GAP-001, GAP-002, etc.)
   - Source Assessment: S1, S2, S3, S4, or S5
   - Gap Description: Clear description of the gap
   - Affected Systems: Count or list of affected systems
   - Control Reference: ISO 27001 control (A.8.2, A.8.3, A.8.5)

2. **Risk Assessment** (Columns F-I):

   - Impact: High, Medium, Low
   - Likelihood: High, Medium, Low
   - Risk Score: Calculated (Impact x Likelihood)
   - Priority: Critical, High, Medium, Low

3. **Remediation** (Columns J-M):

   - Remediation Status: Not Started, In Progress, Completed
   - Owner: Assigned team/person
   - Target Date: Planned completion
   - Actual Date: Completed date (if applicable)

**Gap Prioritization Rules:**

| Impact | Likelihood | Priority |
|--------|------------|----------|
| High | High | Critical |
| High | Medium | High |
| High | Low | Medium |
| Medium | High | High |
| Medium | Medium | Medium |
| Medium | Low | Low |
| Low | Any | Low |

**Example Gap Entry:**
```
Gap ID: GAP-003
Source: S2 - MFA Coverage
Description: Legacy ERP system does not support MFA
Affected Systems: 1 (ERP-PROD)
Control: A.8.5
Impact: High (financial data access)
Likelihood: Medium
Risk Score: 6
Priority: High
Status: In Progress
Owner: IT Applications Team
Target: 31.03.2026
```

**Step 4: Complete Sheet 3 - Risk Register**

Document authentication and privileged access risks:

1. **Risk Identification** (Columns A-E):

   - Risk ID: Unique identifier (RISK-001, etc.)
   - Risk Title: Brief title
   - Risk Description: Detailed description
   - Risk Category: Authentication, Privileged Access, Authorization
   - Threat Source: Internal, External, Both

2. **Risk Assessment** (Columns F-J):

   - Asset/Process Affected: What's at risk
   - Inherent Impact: Before controls (1-5)
   - Inherent Likelihood: Before controls (1-5)
   - Inherent Risk Score: Impact x Likelihood
   - Inherent Risk Level: Critical, High, Medium, Low

3. **Control Assessment** (Columns K-N):

   - Current Controls: Existing mitigations
   - Control Effectiveness: Effective, Partially Effective, Ineffective
   - Residual Impact: After controls (1-5)
   - Residual Likelihood: After controls (1-5)
   - Residual Risk Score: Impact x Likelihood

4. **Risk Treatment** (Columns O-R):

   - Treatment Option: Accept, Mitigate, Transfer, Avoid
   - Treatment Plan: Planned actions
   - Owner: Responsible party
   - Review Date: Next review

**Example Risk Entry:**
```
Risk ID: RISK-002
Title: Privileged account compromise
Description: Unauthorized access to privileged accounts due to weak authentication
Category: Privileged Access
Threat Source: External
Inherent Impact: 5 (Critical)
Inherent Likelihood: 3 (Medium)
Inherent Risk: 15 (High)
Current Controls: PAM solution, MFA for admin access
Control Effectiveness: Partially Effective
Residual Impact: 5
Residual Likelihood: 2
Residual Risk: 10 (Medium)
Treatment: Mitigate
Plan: Extend PAM to all privileged accounts, enforce MFA
Owner: Security Team
Review: 30.06.2026
```

**Step 5: Complete Sheet 4 - Remediation Roadmap**

Create prioritized remediation plan:

1. **Remediation Items** (Columns A-E):

   - Item ID: Unique identifier (REM-001, etc.)
   - Related Gap: Gap ID reference
   - Remediation Description: What needs to be done
   - Remediation Type: Technical, Process, Documentation
   - Priority: Critical, High, Medium, Low

2. **Timeline** (Columns F-I):

   - Phase: Phase 1 (0-30 days), Phase 2 (30-90 days), Phase 3 (90+ days)
   - Start Date: Planned start
   - Target Date: Planned completion
   - Actual Completion: Actual date

3. **Resources** (Columns J-L):

   - Owner: Assigned team/person
   - Effort Estimate: Hours/days
   - Budget Required: Cost estimate

4. **Status** (Columns M-O):

   - Status: Not Started, In Progress, Completed, Blocked
   - Blockers: Any impediments
   - Notes: Additional context

**Remediation Phasing:**

| Phase | Timeline | Focus |
|-------|----------|-------|
| Phase 1 | 0-30 days | Critical gaps, quick wins |
| Phase 2 | 30-90 days | High priority, medium complexity |
| Phase 3 | 90+ days | Medium/Low priority, complex projects |

**Step 6: Complete Sheet 5 - KPIs & Metrics**

Establish key performance indicators:

1. **KPI Definition** (Columns A-E):

   - KPI ID: Unique identifier
   - KPI Name: Descriptive name
   - KPI Description: What it measures
   - Related Control: A.8.2, A.8.3, or A.8.5
   - Data Source: S1, S2, S3, S4, or S5

2. **Targets & Thresholds** (Columns F-I):

   - Target: Goal value
   - Green Threshold: Acceptable (e.g., >= 90%)
   - Yellow Threshold: Warning (e.g., 75-89%)
   - Red Threshold: Critical (e.g., < 75%)

3. **Current Values** (Columns J-M):

   - Current Value: Latest measurement
   - Status: Green, Yellow, Red
   - Trend: Improving, Stable, Declining
   - Last Updated: Date of measurement

**Recommended KPIs for A.8.2-3-5:**

| KPI | Description | Target |
|-----|-------------|--------|
| MFA Coverage | % of users with MFA enabled | >= 95% |
| Privileged Account Review | % of accounts reviewed in last 90 days | 100% |
| Orphaned Account Count | Number of accounts without valid owner | 0 |
| PAM Coverage | % of privileged systems with PAM | >= 90% |
| Access Control Compliance | % of systems meeting access control requirements | >= 90% |
| Authentication Method Currency | % of systems using modern authentication | >= 85% |
| Critical Gap Count | Number of open critical gaps | 0 |
| Remediation Velocity | Gaps closed per month | Trend increasing |

**Step 7: Complete Sheet 6 - Evidence Register**

Consolidate evidence from all assessments:

1. **Evidence Identification** (Columns A-E):

   - Evidence ID: Unique identifier
   - Evidence Name: Descriptive name
   - Evidence Type: Screenshot, Report, Configuration, Log
   - Source Assessment: S1, S2, S3, S4, S5
   - Related Control: A.8.2, A.8.3, A.8.5

2. **Evidence Details** (Columns F-I):

   - Evidence Date: When collected
   - Evidence Location: File path or URL
   - Retention Period: How long to keep
   - Next Collection: When to refresh

3. **Audit Mapping** (Columns J-K):

   - Audit Requirement: What it proves
   - Audit Ready: Yes, No (complete and current?)

**Evidence Categories:**

| Category | Examples |
|----------|----------|
| Authentication | MFA enrollment reports, SSO configuration |
| Privileged Access | PAM audit logs, privileged account list |
| Access Control | Permission audits, RBAC configuration |
| Monitoring | Session recordings, alert configurations |
| Review | Certification evidence, access review logs |

**Step 8: Complete Sheet 7 - Action Items & Follow-up**

Track remediation activities:

1. **Action Item Details** (Columns A-F):

   - Action ID: Unique identifier
   - Action Description: What needs to be done
   - Related Gap/Risk: Gap or Risk ID
   - Priority: Critical, High, Medium, Low
   - Category: Technical, Process, Documentation, Training

2. **Assignment** (Columns G-I):

   - Assigned To: Owner
   - Assigned Date: When assigned
   - Due Date: Target completion

3. **Status Tracking** (Columns J-M):

   - Status: Open, In Progress, Completed, Overdue
   - Completion Date: Actual completion
   - Follow-up Required: Yes, No
   - Notes: Comments and updates

**Step 9: Complete Sheet 8 - Audit & Compliance Log**

Maintain audit trail:

1. **Assessment History** (Rows 5-20):

   - Assessment dates for S1-S5
   - Assessment results
   - Assessor names

2. **Audit Findings** (Rows 23-40):

   - Audit date
   - Audit type (Internal, External, Certification)
   - Findings related to A.8.2-3-5
   - Finding status

3. **Certification Status** (Rows 43-50):

   - ISO 27001 certification status
   - Last certification date
   - Next surveillance audit
   - A.8.2-3-5 specific findings

**Step 10: Complete Sheet 9 - Approval & Sign-Off**

Three-level approval process:

1. **Preparer** (Security Team):

   - Aggregated data from S1-S5
   - Verified data accuracy
   - Completed all sheets
   - Date and signature

2. **Reviewer** (Security Manager):

   - Validated compliance scores
   - Verified gap prioritization
   - Confirmed risk assessments
   - Date and signature

3. **Approver** (CISO):

   - Reviewed executive dashboard
   - Approved remediation roadmap
   - Accepted residual risks
   - Date and signature

---

# Data Aggregation Guidelines

## Extracting Data from S1-S5

**From S1 - Authentication Inventory:**

- Total systems inventoried
- Authentication methods distribution
- Systems with compliant authentication
- Compliance percentage
- Open gaps

**From S2 - MFA Coverage:**

- MFA coverage percentage
- Users with MFA enabled
- Systems with MFA enforced
- MFA gaps (systems/users without MFA)
- Exception count

**From S3 - Privileged Account Inventory:**

- Total privileged accounts
- Accounts reviewed in last 90 days
- Orphaned accounts
- Accounts with owners assigned
- Compliance percentage

**From S4 - Privileged Monitoring:**

- Systems with PAM coverage
- PAM coverage percentage
- Session recording enabled count
- Systems requiring PAM but not covered
- Compliance percentage

**From S5 - Access Restrictions:**

- Access control compliance percentage
- Systems with proper authorization
- Critical access control gaps
- Excessive permission findings

## Deduplication Rules

When consolidating gaps, apply these rules:

1. **Same System, Same Issue**: Keep single gap, reference all source assessments
2. **Related Issues**: Link gaps but keep separate if remediation differs
3. **Root Cause**: If gaps share root cause, create parent gap with child items

## Calculation Formulas

**Overall Compliance Score:**
```
Overall = (S1_Score x 0.20) + (S2_Score x 0.25) + (S3_Score x 0.20) +
          (S4_Score x 0.15) + (S5_Score x 0.20)
```

Weighting rationale:

- MFA (S2) weighted highest due to authentication criticality
- S1, S3, S5 equally weighted for foundational controls
- S4 (Monitoring) weighted lower as detective control

---

# Common Pitfalls & How to Avoid Them

## Pitfall 1: Stale Data

**Problem**: Dashboard shows outdated compliance scores because S1-S5 assessments are not current

**Solution**:

- Establish 90-day maximum age for source assessments
- Include "Data Freshness" indicator on dashboard
- Flag when source data exceeds age threshold

## Pitfall 2: Inconsistent Scoring

**Problem**: Different assessors use different criteria for compliance scoring

**Solution**:

- Define clear compliance criteria in each assessment
- Use objective measures (counts, percentages) over subjective
- Validate scoring consistency during aggregation

## Pitfall 3: Gap Duplication

**Problem**: Same gap appears multiple times from different assessments

**Solution**:

- Use deduplication rules consistently
- Assign unique gap IDs
- Cross-reference related gaps

## Pitfall 4: Missing Root Cause Analysis

**Problem**: Gaps listed without understanding underlying cause

**Solution**:

- Include root cause field in gap analysis
- Group gaps by root cause
- Address root causes in remediation roadmap

## Pitfall 5: Unrealistic Remediation Timelines

**Problem**: Remediation targets set without considering resource constraints

**Solution**:

- Validate timelines with remediation owners
- Consider dependencies between items
- Include resource requirements in planning

## Pitfall 6: Evidence Gaps

**Problem**: Evidence register incomplete; audit fails due to missing proof

**Solution**:

- Map every compliance claim to evidence
- Regular evidence freshness review
- Pre-audit evidence validation

## Pitfall 7: Executive Dashboard Too Technical

**Problem**: Dashboard contains technical details; executives don't understand

**Solution**:

- Lead with overall score and trend
- Use traffic light indicators
- Keep technical details in supporting sheets

## Pitfall 8: No Trend Tracking

**Problem**: Dashboard shows point-in-time; no visibility into improvement

**Solution**:

- Maintain historical data (12+ months)
- Include trend arrows and percentages
- Show velocity metrics (gaps closed per month)

## Pitfall 9: Risk Register Disconnect

**Problem**: Risks in register don't align with gaps in analysis

**Solution**:

- Link risks to gaps explicitly
- Ensure gap remediation reduces risk scores
- Review alignment quarterly

## Pitfall 10: Approval Without Action

**Problem**: Dashboard approved but remediation not tracked

**Solution**:

- Approval includes commitment to remediation plan
- Monthly progress reviews
- Escalation process for stalled items

---

# Quality Checklist

Before submitting dashboard for approval, verify:

## Data Quality

- [ ] All S1-S5 assessments are current (within 90 days)
- [ ] Compliance scores extracted correctly
- [ ] Gap data complete and deduplicated
- [ ] Risk scores calculated accurately
- [ ] KPI values current

## Completeness

- [ ] Executive Dashboard complete with all metrics
- [ ] Gap Analysis includes all S1-S5 gaps
- [ ] Risk Register covers all identified risks
- [ ] Remediation Roadmap has all gaps assigned
- [ ] Evidence Register indexes all evidence

## Accuracy

- [ ] Overall compliance score calculation verified
- [ ] Component scores match source assessments
- [ ] Gap priorities align with risk scores
- [ ] Remediation timelines validated with owners

## Presentation

- [ ] Executive Dashboard clear and readable
- [ ] Color coding applied correctly
- [ ] Trend indicators accurate
- [ ] No spelling or formatting errors

## Audit Readiness

- [ ] Evidence complete for each control
- [ ] Evidence dated and current
- [ ] Gaps have remediation plans
- [ ] Risk treatments documented

---

# Interpreting Results

## Understanding Dashboard Metrics

**Overall Compliance Score:**

- **90-100%**: GREEN - Strong compliance posture
- **75-89%**: YELLOW - Acceptable with improvement areas
- **60-74%**: ORANGE - Significant gaps requiring attention
- **<60%**: RED - Non-compliant, immediate action required

**Component Score Interpretation:**

| Component | GREEN | YELLOW | RED |
|-----------|-------|--------|-----|
| S1 Auth Inventory | >= 95% | 80-94% | < 80% |
| S2 MFA Coverage | >= 90% | 75-89% | < 75% |
| S3 Privileged Accounts | >= 95% | 85-94% | < 85% |
| S4 Privileged Monitoring | >= 85% | 70-84% | < 70% |
| S5 Access Restrictions | >= 90% | 75-89% | < 75% |

**Gap Priority Distribution:**

- Healthy: 0 Critical, < 5 High, < 15 Medium
- Concerning: 1-2 Critical, 5-10 High
- Problematic: > 2 Critical, > 10 High

## Executive Reporting Guidelines

**Monthly Report Should Include:**

1. Overall compliance score with trend
2. Critical and high gaps count
3. Top 3 risks
4. Remediation progress (closed vs. open)
5. KPIs trending in wrong direction

**Quarterly Report Should Include:**

1. Full dashboard review
2. Risk register update
3. Remediation roadmap refresh
4. Evidence audit results
5. Recommendations for next quarter

---

# Review & Approval Process

## Approval Workflow

**Level 1 - Preparer (Security Team / GRC Analyst)**:

- Aggregate data from S1-S5 assessments
- Consolidate gaps and deduplicate
- Populate risk register
- Create remediation roadmap
- Compile evidence register
- Calculate KPIs
- Complete all sheets
- Submit for review

**Level 2 - Reviewer (Security Manager / Senior Security Engineer)**:

- Validate data aggregation accuracy
- Verify gap prioritization
- Review risk assessments
- Confirm remediation timelines are realistic
- Verify evidence completeness
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:

- Review executive dashboard
- Validate overall compliance posture
- Approve remediation priorities and resources
- Accept residual risks
- Sign off on assessment
- Authorize executive communication

## Approval Criteria

Dashboard is approved when:

- [ ] All S1-S5 source data is current
- [ ] Data aggregation validated
- [ ] Gap analysis complete and prioritized
- [ ] Risk register current
- [ ] Remediation roadmap resourced and approved
- [ ] Evidence register complete
- [ ] KPIs established with targets

## Post-Approval Actions

After CISO approval:

1. **Distribute Dashboard**: Share with stakeholders per distribution list
2. **Initiate Remediation**: Assign and track remediation items
3. **Schedule Reviews**: Monthly KPI review, quarterly comprehensive update
4. **Archive Version**: Store approved version with date stamp
5. **Update Risk Register**: Feed risks into enterprise risk management

---

# PART II: TECHNICAL SPECIFICATION

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.6_Compliance_Dashboard_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Executive_Dashboard | Overall A.8.2-3-5 compliance score and key metrics | ~50 | Calculated/User |
| 2 | Gap_Analysis | Consolidated gaps from S1-S5 assessments | 153 | User completes |
| 3 | Risk_Register | Authentication and privileged access risks | 53 | User completes |
| 4 | Remediation_Roadmap | Prioritized remediation plan with timeline | 103 | User completes |
| 5 | KPIs_Metrics | Key performance indicators and targets | 53 | User/Calculated |
| 6 | Evidence_Register | Consolidated evidence index from all assessments | 103 | User completes |
| 7 | Action_Items_Followup | Remediation activity tracking | 103 | User completes |
| 8 | Audit_Compliance_Log | Assessment and audit history | 53 | User completes |
| 9 | Approval_Sign_Off | Three-level approval workflow | ~30 | User completes |

**Total Workbook:** 9 sheets, ~700 rows of structured data

## Color Coding & Conditional Formatting

**Compliance Status Colors:**

- GREEN (Compliant): RGB(198, 239, 206) - Meets requirements (>= 90%)
- YELLOW (Partial): RGB(255, 235, 156) - Partial compliance (75-89%)
- ORANGE (Warning): RGB(255, 192, 0) - Significant gaps (60-74%)
- RED (Non-Compliant): RGB(255, 199, 206) - Non-compliant (< 60%)

**Gap Priority Colors:**

- CRITICAL: RGB(255, 0, 0) - Immediate action (0-7 days)
- HIGH: RGB(255, 153, 0) - Within 30 days
- MEDIUM: RGB(255, 255, 0) - Within 90 days
- LOW: RGB(146, 208, 80) - Ongoing improvement

**Risk Level Colors:**

- CRITICAL (15-25): RGB(255, 0, 0)
- HIGH (10-14): RGB(255, 153, 0)
- MEDIUM (5-9): RGB(255, 255, 0)
- LOW (1-4): RGB(146, 208, 80)

---

# Sheet 1: Executive Dashboard

## Layout Structure

**Header Section (Rows 1-4):**
```
Row 1: ISMS-IMP-A.8.2-3-5.6 Compliance Dashboard
Row 2: Authentication & Privileged Access Controls
Row 3: Assessment Date: [Date] | Version: 1.0
Row 4: [Blank separator]
```

**Overall Compliance (Rows 5-7):**

| Col A | Col B | Col C | Col D |
|-------|-------|-------|-------|
| Overall A.8.2-3-5 Compliance | [Score %] | [Status] | [Trend] |

**Component Scores (Rows 9-15):**

| Col A | Col B | Col C | Col D | Col E |
|-------|-------|-------|-------|-------|
| Component | Score | Status | Trend | Last Updated |
| S1 - Authentication Inventory | [%] | [G/Y/R] | [Arrow] | [Date] |
| S2 - MFA Coverage | [%] | [G/Y/R] | [Arrow] | [Date] |
| S3 - Privileged Accounts | [%] | [G/Y/R] | [Arrow] | [Date] |
| S4 - Privileged Monitoring | [%] | [G/Y/R] | [Arrow] | [Date] |
| S5 - Access Restrictions | [%] | [G/Y/R] | [Arrow] | [Date] |

**Key Metrics (Rows 17-28):**

| Col A | Col B | Col C |
|-------|-------|-------|
| Metric | Value | Status |
| Total Systems in Scope | [Number] | - |
| MFA Coverage | [%] | [G/Y/R] |
| Privileged Accounts | [Number] | - |
| Orphaned Accounts | [Number] | [G/Y/R] |
| PAM Coverage | [%] | [G/Y/R] |
| Systems without PAM | [Number] | [G/Y/R] |
| Critical Gaps Open | [Number] | [G/Y/R] |
| High Gaps Open | [Number] | [G/Y/R] |
| Remediation Items Overdue | [Number] | [G/Y/R] |

**Gap Summary (Rows 30-36):**

| Col A | Col B | Col C |
|-------|-------|-------|
| Priority | Count | Target |
| Critical | [N] | 0 |
| High | [N] | < 5 |
| Medium | [N] | < 15 |
| Low | [N] | < 25 |
| Total | [Sum] | - |

## Formulas

**Overall Compliance Score (B5):**
```excel
=(B10*0.20)+(B11*0.25)+(B12*0.20)+(B13*0.15)+(B14*0.20)
```

**Status Indicator (C5):**
```excel
=IF(B5>=90,"GREEN",IF(B5>=75,"YELLOW",IF(B5>=60,"ORANGE","RED")))
```

**Trend Indicator (D5):**
```excel
=IF(B5>PreviousScore,"Improving",IF(B5<PreviousScore,"Declining","Stable"))
```

---

# Sheet 2: Gap Analysis

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Gap ID | 12 | Text | GAP-NNN format | Unique identifier |
| B | Source Assessment | 18 | Dropdown | S1, S2, S3, S4, S5, Multiple | Origin assessment |
| C | Gap Description | 45 | Text | Free text | Clear description |
| D | Affected Systems | 15 | Number | >= 0 | Count of systems |
| E | Control Reference | 12 | Dropdown | A.8.2, A.8.3, A.8.5 | ISO control |
| F | Impact | 10 | Dropdown | High, Medium, Low | Business impact |
| G | Likelihood | 12 | Dropdown | High, Medium, Low | Probability |
| H | Risk Score | 12 | Formula | Auto-calculated | Impact x Likelihood |
| I | Priority | 12 | Formula | Auto: Critical, High, Medium, Low | Based on risk |
| J | Status | 15 | Dropdown | Not Started, In Progress, Completed, Accepted | Remediation status |
| K | Owner | 20 | Text | Free text | Responsible party |
| L | Target Date | 15 | Date | DD.MM.YYYY | Planned completion |
| M | Notes | 30 | Text | Free text | Additional context |

**Total Columns:** 13 (A-M)

## Risk Score Calculation (Column H)

```excel
=IF(AND(F5="High",G5="High"),9,
 IF(AND(F5="High",G5="Medium"),6,
 IF(AND(F5="High",G5="Low"),3,
 IF(AND(F5="Medium",G5="High"),6,
 IF(AND(F5="Medium",G5="Medium"),4,
 IF(AND(F5="Medium",G5="Low"),2,
 IF(AND(F5="Low",G5="High"),3,
 IF(AND(F5="Low",G5="Medium"),2,1))))))))
```

## Priority Calculation (Column I)

```excel
=IF(H5>=9,"Critical",IF(H5>=6,"High",IF(H5>=3,"Medium","Low")))
```

---

# Sheet 3: Risk Register

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Risk ID | 12 | Text | RISK-NNN | Unique identifier |
| B | Risk Title | 25 | Text | Free text | Brief title |
| C | Risk Description | 40 | Text | Free text | Detailed description |
| D | Category | 18 | Dropdown | Authentication, Privileged Access, Authorization | Risk category |
| E | Threat Source | 15 | Dropdown | Internal, External, Both | Threat origin |
| F | Asset Affected | 20 | Text | Free text | What's at risk |
| G | Inherent Impact | 15 | Number | 1-5 | Impact before controls |
| H | Inherent Likelihood | 18 | Number | 1-5 | Likelihood before controls |
| I | Inherent Risk | 15 | Formula | G x H | Inherent score |
| J | Inherent Level | 15 | Formula | Auto-calculated | Risk level |
| K | Current Controls | 30 | Text | Free text | Existing mitigations |
| L | Control Effectiveness | 20 | Dropdown | Effective, Partially Effective, Ineffective | Effectiveness |
| M | Residual Impact | 15 | Number | 1-5 | Impact after controls |
| N | Residual Likelihood | 18 | Number | 1-5 | Likelihood after controls |
| O | Residual Risk | 15 | Formula | M x N | Residual score |
| P | Residual Level | 15 | Formula | Auto-calculated | Risk level |
| Q | Treatment | 15 | Dropdown | Accept, Mitigate, Transfer, Avoid | Treatment option |
| R | Treatment Plan | 30 | Text | Free text | Planned actions |
| S | Owner | 18 | Text | Free text | Risk owner |
| T | Review Date | 15 | Date | DD.MM.YYYY | Next review |

**Total Columns:** 20 (A-T)

## Risk Level Calculation (Column J, P)

```excel
=IF(I5>=15,"Critical",IF(I5>=10,"High",IF(I5>=5,"Medium","Low")))
```

---

# Sheet 4: Remediation Roadmap

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Item ID | 12 | Text | REM-NNN | Unique identifier |
| B | Related Gap | 12 | Text | Gap ID reference | Linked gap |
| C | Description | 40 | Text | Free text | Remediation action |
| D | Type | 15 | Dropdown | Technical, Process, Documentation, Training | Remediation type |
| E | Priority | 12 | Dropdown | Critical, High, Medium, Low | Priority level |
| F | Phase | 12 | Dropdown | Phase 1, Phase 2, Phase 3 | Timeline phase |
| G | Start Date | 15 | Date | DD.MM.YYYY | Planned start |
| H | Target Date | 15 | Date | DD.MM.YYYY | Planned completion |
| I | Actual Date | 15 | Date | DD.MM.YYYY | Actual completion |
| J | Owner | 20 | Text | Free text | Responsible party |
| K | Effort (Hours) | 15 | Number | >= 0 | Estimated effort |
| L | Budget | 15 | Currency | >= 0 | Cost estimate |
| M | Status | 15 | Dropdown | Not Started, In Progress, Completed, Blocked | Current status |
| N | Blockers | 25 | Text | Free text | Impediments |
| O | Notes | 25 | Text | Free text | Additional context |

**Total Columns:** 15 (A-O)

---

# Sheet 5: KPIs & Metrics

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | KPI ID | 10 | Text | KPI-NN | Unique identifier |
| B | KPI Name | 25 | Text | Free text | KPI title |
| C | Description | 35 | Text | Free text | What it measures |
| D | Control Reference | 12 | Dropdown | A.8.2, A.8.3, A.8.5 | Related control |
| E | Data Source | 15 | Dropdown | S1, S2, S3, S4, S5, Calculated | Source assessment |
| F | Unit | 10 | Text | %, Count, Days | Measurement unit |
| G | Target | 12 | Number/% | >= 0 | Goal value |
| H | Green >= | 12 | Number/% | >= 0 | Green threshold |
| I | Yellow >= | 12 | Number/% | >= 0 | Yellow threshold |
| J | Red < | 12 | Number/% | >= 0 | Red threshold |
| K | Current Value | 15 | Number/% | >= 0 | Latest measurement |
| L | Status | 12 | Formula | Auto: Green, Yellow, Red | Current status |
| M | Trend | 12 | Dropdown | Improving, Stable, Declining | Direction |
| N | Last Updated | 15 | Date | DD.MM.YYYY | Measurement date |

**Total Columns:** 14 (A-N)

## Status Calculation (Column L)

```excel
=IF(K5>=H5,"Green",IF(K5>=I5,"Yellow","Red"))
```

## Pre-Populated KPIs

| KPI ID | KPI Name | Target | Green | Yellow | Red |
|--------|----------|--------|-------|--------|-----|
| KPI-01 | MFA Coverage | 95% | >= 90% | >= 75% | < 75% |
| KPI-02 | Privileged Account Review Rate | 100% | >= 95% | >= 85% | < 85% |
| KPI-03 | Orphaned Account Count | 0 | 0 | 1-3 | > 3 |
| KPI-04 | PAM Coverage | 90% | >= 85% | >= 70% | < 70% |
| KPI-05 | Access Control Compliance | 90% | >= 90% | >= 75% | < 75% |
| KPI-06 | Authentication Modernity | 85% | >= 85% | >= 70% | < 70% |
| KPI-07 | Critical Gap Count | 0 | 0 | 1-2 | > 2 |
| KPI-08 | High Gap Count | 5 | <= 5 | 6-10 | > 10 |
| KPI-09 | Remediation Velocity | Trend | Improving | Stable | Declining |
| KPI-10 | Evidence Currency | 90 days | <= 90 | 91-180 | > 180 |

---

# Sheet 6: Evidence Register

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Evidence ID | 12 | Text | EVD-NNN | Unique identifier |
| B | Evidence Name | 30 | Text | Free text | Descriptive name |
| C | Evidence Type | 15 | Dropdown | Screenshot, Report, Configuration, Log, Policy | Type |
| D | Source Assessment | 15 | Dropdown | S1, S2, S3, S4, S5 | Origin |
| E | Control Reference | 12 | Dropdown | A.8.2, A.8.3, A.8.5 | Related control |
| F | Evidence Date | 15 | Date | DD.MM.YYYY | Collection date |
| G | Location | 35 | Text | File path/URL | Storage location |
| H | Retention | 15 | Text | Free text | Retention period |
| I | Next Collection | 15 | Date | DD.MM.YYYY | Refresh date |
| J | Audit Requirement | 25 | Text | Free text | What it proves |
| K | Audit Ready | 12 | Dropdown | Yes, No | Complete/Current? |

**Total Columns:** 11 (A-K)

---

# Sheet 7: Action Items & Follow-up

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Action ID | 12 | Text | ACT-NNN | Unique identifier |
| B | Description | 40 | Text | Free text | Action description |
| C | Related Gap/Risk | 15 | Text | ID reference | Linked item |
| D | Priority | 12 | Dropdown | Critical, High, Medium, Low | Priority level |
| E | Category | 15 | Dropdown | Technical, Process, Documentation, Training | Type |
| F | Assigned To | 20 | Text | Free text | Owner |
| G | Assigned Date | 15 | Date | DD.MM.YYYY | Assignment date |
| H | Due Date | 15 | Date | DD.MM.YYYY | Target date |
| I | Status | 15 | Dropdown | Open, In Progress, Completed, Overdue | Current status |
| J | Completion Date | 15 | Date | DD.MM.YYYY | Actual completion |
| K | Follow-up Required | 15 | Dropdown | Yes, No | Needs follow-up? |
| L | Notes | 30 | Text | Free text | Comments |

**Total Columns:** 12 (A-L)

## Status Calculation

```excel
=IF(J5<>"","Completed",IF(AND(I5<>"Completed",H5<TODAY()),"Overdue",I5))
```

---

# Sheet 8: Audit & Compliance Log

## Section Structure

**Assessment History (Rows 5-20):**

| Col A | Col B | Col C | Col D | Col E |
|-------|-------|-------|-------|-------|
| Assessment | Date | Result | Assessor | Notes |
| S1 - Authentication Inventory | [Date] | [%] | [Name] | [Notes] |
| S2 - MFA Coverage | [Date] | [%] | [Name] | [Notes] |
| S3 - Privileged Accounts | [Date] | [%] | [Name] | [Notes] |
| S4 - Privileged Monitoring | [Date] | [%] | [Name] | [Notes] |
| S5 - Access Restrictions | [Date] | [%] | [Name] | [Notes] |

**Audit Findings (Rows 23-40):**

| Col A | Col B | Col C | Col D | Col E | Col F |
|-------|-------|-------|-------|-------|-------|
| Audit Date | Audit Type | Finding ID | Finding | Status | Resolution |

**Certification Status (Rows 43-50):**

| Col A | Col B |
|-------|-------|
| ISO 27001 Certification Status | [Certified/In Progress/Not Certified] |
| Certification Date | [Date] |
| Certifying Body | [Name] |
| Next Surveillance Audit | [Date] |
| A.8.2-3-5 Audit Findings | [Count] |

---

# Sheet 9: Approval & Sign-Off

## Layout Structure

**Header (Rows 1-3):**
```
ISMS-IMP-A.8.2-3-5.6 Compliance Dashboard
Approval & Sign-Off
```

**Approval Table (Rows 5-20):**

| Col A | Col B | Col C | Col D |
|-------|-------|-------|-------|
| Role | Name | Date | Signature |
| **Level 1: Preparer** | | | |
| Security Analyst/GRC Analyst | [Name] | [Date] | [Signature] |
| Confirmation | Data aggregated from S1-S5 assessments | | |
| | All gaps consolidated and prioritized | | |
| | Evidence register complete | | |
| **Level 2: Reviewer** | | | |
| Security Manager | [Name] | [Date] | [Signature] |
| Confirmation | Data accuracy validated | | |
| | Gap prioritization verified | | |
| | Remediation timelines confirmed | | |
| **Level 3: Approver** | | | |
| CISO | [Name] | [Date] | [Signature] |
| Confirmation | Executive dashboard reviewed | | |
| | Remediation roadmap approved | | |
| | Residual risks accepted | | |

**Distribution List (Rows 22-30):**

| Role | Name | Date Distributed |
|------|------|------------------|
| Executive Management | | |
| IT Management | | |
| Internal Audit | | |
| Risk Management | | |

---

# Python Script Integration

## Script Purpose

**Script:** `generate_a8235_6_compliance_dashboard.py`

**Functions:**

- Creates workbook with all 9 sheets
- Applies formatting and conditional formatting
- Sets up data validation dropdowns
- Implements formulas for calculations
- Pre-populates KPIs and reference data

## Running the Script

```bash
python3 generate_a8235_6_compliance_dashboard.py
```

**Output:** `ISMS-IMP-A.8.2-3-5.6_Compliance_Dashboard_YYYYMMDD.xlsx`

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**END OF ISMS-IMP-A.8.2-3-5.6**

*The dashboard is the window into your security posture. Keep it clean, keep it current, keep it honest.*

*Compliance is a journey, not a destination. The dashboard shows where you are and where you need to go.*

---

**END OF SPECIFICATION**

---

*"In God we trust; all others must bring data."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-01 -->
