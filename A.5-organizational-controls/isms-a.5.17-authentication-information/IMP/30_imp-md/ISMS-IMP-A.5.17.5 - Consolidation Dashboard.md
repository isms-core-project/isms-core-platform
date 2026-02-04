# ISMS-IMP-A.5.17.5 — Consolidation Dashboard

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.5 |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.17 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.17 (Authentication Information Policy)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)
- ISMS-IMP-A.5.17.4 (Compliance and Audit Dashboard)

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

The **Consolidation Dashboard** (ISMS-IMP-A.5.17.5) aggregates compliance data from all four A.5.17 assessment workbooks into a unified executive view. This dashboard provides holistic visibility into authentication information control compliance, enabling management reporting, audit preparation, and strategic decision-making.

### 1.2 Scope

This dashboard consolidates:
- **Domain 1**: Authentication Policy and Standards (A.5.17.1)
- **Domain 2**: Credential Lifecycle Management (A.5.17.2)
- **Domain 3**: Password System Assessment (A.5.17.3)
- **Domain 4**: Compliance and Audit Dashboard (A.5.17.4)

### 1.3 Business Value

Maintaining this consolidation delivers:
- **Unified compliance view** across all authentication domains
- **Executive reporting** with aggregated metrics
- **Cross-domain gap analysis** identifying systemic issues
- **Audit efficiency** through pre-consolidated evidence
- **Trend visibility** showing compliance over time

### 1.4 Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.17 — Authentication Information*
>
> "The allocation and management of authentication information should be controlled by a management process, including advising personnel on appropriate handling of authentication information."

This dashboard provides a consolidated view of A.5.17 compliance across all implementation domains.

---

## 2. Prerequisites

Before completing this dashboard, ensure you have:

### 2.1 Required Workbooks
- [ ] ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide) — current version
- [ ] ISMS-IMP-A.5.17.2 (MFA Deployment Assessment) — current version
- [ ] ISMS-IMP-A.5.17.3 (Authentication Management Procedures) — current version
- [ ] ISMS-IMP-A.5.17.4 (Compliance and Audit Dashboard) — current version

### 2.2 Required Access
- [ ] All source workbook locations
- [ ] Previous consolidation reports (if available)
- [ ] Management reporting templates
- [ ] Risk register for cross-referencing

### 2.3 Required Personnel
- [ ] Information Security Officer (consolidation owner)
- [ ] IAM Team Lead (source workbook owner)
- [ ] IT Security Analyst (data compilation)
- [ ] Risk Manager (gap prioritisation)
- [ ] Executive Sponsor (final approval)

---

## 3. Workbook Structure

The workbook contains **12 sheets** organised as follows:

| Sheet | Purpose | Source Data |
|-------|---------|-------------|
| Instructions | Guidance and scoring methodology | N/A |
| Executive_Summary | High-level compliance overview | All domains |
| Domain_Overview | Domain-by-domain compliance | A.5.17.1-4 |
| Policy_Compliance | Policy element compliance | A.5.17.1 |
| Lifecycle_Compliance | Credential lifecycle compliance | A.5.17.2 |
| System_Compliance | System authentication compliance | A.5.17.3 |
| Cross_Domain_Gaps | Gaps spanning multiple domains | Analysis |
| Remediation_Tracker | Consolidated remediation | A.5.17.4 |
| KPI_Summary | Key performance indicators | A.5.17.4 |
| Evidence_Index | Cross-reference to evidence | All domains |
| Trend_Dashboard | Historical compliance trends | Historical |
| Approval_SignOff | Consolidation approval | N/A |

---

## 4. Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Explains consolidation methodology and compliance scoring.

**Compliance Scoring**:

| Score | Range | Colour | Description |
|-------|-------|--------|-------------|
| Compliant | ≥90% | Green | Requirements substantially met |
| Partially Compliant | 50-89% | Amber | Some gaps requiring attention |
| Non-Compliant | <50% | Red | Significant gaps requiring action |

**Consolidation Frequency**: Quarterly or after significant changes

### Sheet 2: Executive_Summary

**Purpose**: Single-page management overview of A.5.17 compliance.

**Section 1: Overall Compliance Status**

| Column | Data Source | Action |
|--------|-------------|--------|
| Domain | Fixed label | Pre-populated |
| Workbook | Source workbook name | Pre-populated |
| Status | Compliance status | Calculate from source |
| Score % | Percentage score | Calculate from source |
| Critical Gaps | Count of critical gaps | Count from sources |
| Last Updated | Source workbook date | Pull from source |

**Domain Entries**:
- A.5.17.1: Authentication Policy & Standards
- A.5.17.2: Credential Lifecycle Management
- A.5.17.3: Password System Assessment
- A.5.17.4: Compliance and Audit Dashboard
- OVERALL: Consolidated Assessment

**Section 2: Key Metrics**

| Metric | Target | Track From |
|--------|--------|------------|
| Password policy compliance | 100% | A.5.17.1, A.5.17.3 |
| MFA adoption rate | ≥95% | A.5.17.2 |
| Credential rotation compliance | 100% | A.5.17.2 |
| Systems with secure storage | 100% | A.5.17.3 |

### Sheet 3: Domain_Overview

**Purpose**: Requirement-level compliance for each domain.

**Domain 1: Policy & Standards (A.5.17.1)**
- Password policy documented
- MFA requirements defined
- Credential standards approved
- User responsibilities documented

**Domain 2: Lifecycle Management (A.5.17.2)**
- Allocation process defined
- Change management process
- Recovery process documented
- Revocation process defined

**Domain 3: System Assessment (A.5.17.3)**
- System inventory complete
- Security assessment current
- Storage assessment done
- Integration assessment done

**For Each Requirement**:

| Column | Action |
|--------|--------|
| Requirement | Pre-populated |
| Status | Pull from source workbook |
| Evidence Ref | Reference source evidence |
| Gap Description | Document if non-compliant |
| Remediation | Document if non-compliant |

### Sheet 4: Policy_Compliance

**Purpose**: Consolidated view of authentication policy compliance.

**Policy Elements to Track**:

| Element | Requirement | From |
|---------|-------------|------|
| Password Length | Minimum 12 characters | A.5.17.1 |
| Password Complexity | Upper, lower, number, special | A.5.17.1 |
| Password History | Cannot reuse last 12 | A.5.17.1 |
| Password Expiry | 90 days max / No expiry with MFA | A.5.17.1 |
| MFA Requirement | All privileged + remote access | A.5.17.2 |
| Account Lockout | 5 failed attempts | A.5.17.1 |
| Session Timeout | 15 minutes idle | A.5.17.1 |
| Credential Storage | Hashed + salted (bcrypt/Argon2) | A.5.17.3 |

**For Each Element**:

| Column | Description |
|--------|-------------|
| Policy_Element | Requirement name |
| Requirement | Expected configuration |
| Implementation_Status | Current state |
| Evidence_Ref | Supporting evidence |
| Last_Review | Date last verified |
| Compliance_Status | Compliant/Partial/Non-Compliant |
| Gap_Notes | Description of gaps |
| Owner | Accountable person |

### Sheet 5: Lifecycle_Compliance

**Purpose**: Credential lifecycle process compliance.

**Lifecycle Phases**:
- Initial Allocation
- Password Change (User)
- Password Change (Admin)
- Password Reset (Self-Service)
- Password Reset (Helpdesk)
- MFA Enrollment
- MFA Reset
- Credential Revocation
- Account Deprovisioning

**For Each Phase**:

| Column | Description |
|--------|-------------|
| Lifecycle_Phase | Process name |
| Process_Defined | Yes/No/Partial |
| Automation_Status | Full/Partial/Manual |
| Audit_Trail | Captured/Not Captured |
| SLA_Compliance | Meeting SLAs |
| Compliance_Status | Overall status |
| Gap_Notes | Issues identified |
| Owner | Process owner |

### Sheet 6: System_Compliance

**Purpose**: System-level authentication compliance.

**Systems to Assess**:
- Active Directory
- Azure AD / Entra ID
- Email System
- VPN Gateway
- ERP System
- CRM System
- HR System
- Cloud Applications (SSO)
- Database Servers
- Linux/Unix Systems

**For Each System**:

| Column | Description |
|--------|-------------|
| System_Name | System identifier |
| Auth_Method | Primary authentication method |
| MFA_Enabled | Yes/No/Partial |
| Storage_Security | Compliant/Non-Compliant |
| Last_Assessed | Assessment date |
| Compliance_Status | Overall status |
| Gap_Notes | Issues identified |
| Owner | System owner |

### Sheet 7: Cross_Domain_Gaps

**Purpose**: Identify gaps that span multiple domains.

**Gap Identification Criteria**:
- Same root cause appears in multiple workbooks
- Gap in one domain causes non-compliance in another
- Systemic issues requiring coordinated remediation

**For Each Cross-Domain Gap**:

| Column | Description | Example |
|--------|-------------|---------|
| Gap_ID | Unique identifier | "GAP-001" |
| Source_Domain | Where first identified | "A.5.17.2 - Lifecycle" |
| Gap_Description | What is the gap | "No automated MFA enrollment" |
| Risk_Rating | Impact level | "High" |
| Priority | Remediation priority | "Critical" |
| Affected_Controls | Other domains impacted | "A.5.17.1, A.5.17.4" |
| Root_Cause | Why gap exists | "Legacy IAM system limitations" |
| Remediation_Action | How to fix | "Upgrade IAM platform" |
| Owner | Accountable person | "IAM Manager" |
| Target_Date | Expected completion | "30.06.2026" |

### Sheet 8: Remediation_Tracker

**Purpose**: Consolidated view of all A.5.17 remediation activities.

**Pull and Consolidate From**:
- A.5.17.4 Remediation_Tracker sheet
- Cross-domain gaps identified in this workbook

**Track**:
- Action_ID
- Related_Gap
- Source_Domain
- Action_Description
- Priority
- Owner
- Start_Date
- Target_Date
- Status
- Progress_%
- Notes

### Sheet 9: KPI_Summary

**Purpose**: Consolidated key performance indicators.

**Key Authentication KPIs**:

| KPI | Target |
|-----|--------|
| Password policy compliance rate | 100% |
| MFA adoption rate | ≥95% |
| Systems with compliant storage | 100% |
| Credential rotation on schedule | 100% |
| Failed login attempts (monthly) | <baseline |
| Credential compromise incidents | 0 |

**For Each KPI Track**:
- Target
- Current
- Previous
- Trend (↑ → ↓)
- Status

### Sheet 10: Evidence_Index

**Purpose**: Cross-reference to all source assessment evidence.

**For Each Evidence Item**:

| Column | Description |
|--------|-------------|
| Evidence_ID | Unique identifier |
| Source_Workbook | Which A.5.17.x workbook |
| Source_Sheet | Which sheet |
| Evidence_Type | Category |
| Evidence_Description | What it proves |
| Location/Reference | Where stored |
| Date_Captured | When collected |
| Validation_Status | Current status |

### Sheet 11: Trend_Dashboard

**Purpose**: Historical compliance trends over time.

**Track by Period (Quarterly)**:

| Column | Description |
|--------|-------------|
| Period | Q1 2025, Q2 2025, etc. |
| Policy % | Domain 1 score |
| Lifecycle % | Domain 2 score |
| Systems % | Domain 3 score |
| Overall % | Consolidated score |
| MFA Adoption | MFA enrollment rate |
| Incidents | Credential incidents in period |
| Notes | Key events/changes |

### Sheet 12: Approval_SignOff

**Purpose**: Executive approval of consolidation.

**Complete**:
1. Assessment Period
2. Consolidation Date
3. Approval Workflow:

| Role | Responsibility |
|------|----------------|
| Prepared By | Compiled consolidation |
| Reviewed By | Validated accuracy |
| Approved By (CISO) | Executive approval |
| IT Security Sign-Off | Technical validation |

---

## 5. Evidence Collection

### 5.1 Evidence Sources

| Domain | Source Workbook | Evidence Type |
|--------|-----------------|---------------|
| Policy | A.5.17.1 | Policy documents, config exports |
| Lifecycle | A.5.17.2 | Process documentation, audit logs |
| Systems | A.5.17.3 | Assessment reports, configs |
| Monitoring | A.5.17.4 | Dashboard reports, KPI data |

### 5.2 Evidence Storage

Store consolidation evidence in:
```
/ISMS/Evidence/A.5.17-Authentication/
├── A.5.17.5-Consolidation/
│   ├── Dashboard-Reports/
│   ├── Trend-Data/
│   ├── Gap-Analysis/
│   └── Approval-Records/
```

---

## 6. Common Pitfalls

### ❌ MISTAKE: Consolidating without updated source workbooks
✅ CORRECT: Verify all source workbooks are current before consolidating

### ❌ MISTAKE: Calculating scores differently than source workbooks
✅ CORRECT: Use consistent methodology; document calculation methods

### ❌ MISTAKE: Missing cross-domain gap analysis
✅ CORRECT: Actively look for gaps that span multiple domains

### ❌ MISTAKE: Not tracking MFA adoption trends
✅ CORRECT: MFA is a critical metric; track adoption over time

### ❌ MISTAKE: Omitting legacy systems from system compliance
✅ CORRECT: Legacy systems often have the biggest gaps; include them all

### ❌ MISTAKE: Not correlating credential incidents with control gaps
✅ CORRECT: Use incidents to validate/identify control weaknesses

### ❌ MISTAKE: Duplicate evidence entries from source workbooks
✅ CORRECT: Reference source evidence; don't duplicate

### ❌ MISTAKE: No clear owner for cross-domain gaps
✅ CORRECT: Assign single accountable owner even for cross-domain issues

### ❌ MISTAKE: Consolidation done only before audits
✅ CORRECT: Maintain quarterly consolidation for continuous visibility

### ❌ MISTAKE: Not presenting executive summary to leadership
✅ CORRECT: Use Executive_Summary for board/management reporting

---

## 7. Quality Checklist

Before submitting the consolidation, verify:

### Data Currency
- [ ] All source workbooks updated within 30 days
- [ ] Scores recalculated from current data
- [ ] Last updated dates accurate

### Executive Summary
- [ ] All domains have status and score
- [ ] Key metrics populated
- [ ] Critical gaps identified
- [ ] Overall score calculated correctly

### Domain Details
- [ ] Each domain section complete
- [ ] Status consistent with source workbooks
- [ ] Gap descriptions specific
- [ ] Evidence references valid

### Cross-Domain Analysis
- [ ] Cross-domain gaps identified
- [ ] Root causes documented
- [ ] Remediation actions assigned
- [ ] Owners and dates set

### Trends and KPIs
- [ ] Historical data complete
- [ ] Trends calculated correctly
- [ ] KPIs aligned with A.5.17.4

### Approval
- [ ] All approvals obtained
- [ ] Distribution list current

---

## 8. Review and Approval

### 8.1 Consolidation Schedule
- **Frequency**: Quarterly
- **Timing**: First week after quarter end
- **Triggers**: Major changes, pre-audit preparation

### 8.2 Approval Workflow
1. **Security Analyst** compiles data
2. **Domain Owners** validate their sections
3. **ISO** reviews overall consolidation
4. **CISO** provides executive approval

### 8.3 Post-Approval Actions
- Distribute to executive stakeholders
- Present at management review
- Archive for audit trail
- Update risk register with findings

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Details

### 9.1 File Information

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.17.5 |
| **Generated Filename** | `ISMS-IMP-A.5.17.5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| **Generator Script** | `generate_a517_5_consolidation_dashboard.py` |
| **Sheet Count** | 12 |
| **Primary Control** | A.5.17 (Authentication Information) |

### 9.2 Sheet Specifications

#### Sheet 1: Instructions
- **Content**: Purpose, methodology, scoring
- **Column width**: A=90

#### Sheet 2: Executive_Summary
- **Row 1**: Title banner (merged A1:H1)
- **Rows 3-5**: Reporting period
- **Rows 6-11**: Domain compliance table
- **Rows 13+**: Key metrics table
- **Column widths**: A=35, B=35, C=18, D=12, E=15, F=15

#### Sheet 3: Domain_Overview
- **Row 1**: Title banner (merged A1:F1)
- **Sections**: Three domain sections with headers
- **Column widths**: A=40, B=18, C=15, D=35, E=35

#### Sheet 4: Policy_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Policy element entries
- **Column widths**: A=22, B=30, C=20, D=15, E=15, F=18, G=30, H=18

#### Sheet 5: Lifecycle_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Lifecycle phase entries
- **Column widths**: A=28, B=18, C=18, D=15, E=15, F=18, G=30, H=18

#### Sheet 6: System_Compliance
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: System entries
- **Column widths**: A=25, B=18, C=15, D=18, E=15, F=18, G=30, H=18

#### Sheet 7: Cross_Domain_Gaps
- **Row 1**: Title banner (merged A1:J1)
- **Row 3**: Column headers (10 columns)
- **Rows 4+**: Gap entries (15 rows)
- **Column widths**: A=10, B=22, C=40, D=12, E=10, F=18, G=30, H=35, I=18, J=15

#### Sheet 8: Remediation_Tracker
- **Row 1**: Title banner (merged A1:K1)
- **Row 3**: Column headers (11 columns)
- **Rows 4+**: Action entries (15 rows)
- **Column widths**: A=10, B=12, C=20, D=40, E=10, F=18, G=12, H=12, I=12, J=10, K=30

#### Sheet 9: KPI_Summary
- **Row 1**: Title banner (merged A1:F1)
- **Row 3**: Column headers (6 columns)
- **Rows 4+**: KPI entries
- **Column widths**: A=42, B=15, C=12, D=12, E=10, F=15

#### Sheet 10: Evidence_Index
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Evidence entries (15 rows)
- **Column widths**: A=12, B=25, C=22, D=18, E=40, F=30, G=15, H=18

#### Sheet 11: Trend_Dashboard
- **Row 1**: Title banner (merged A1:H1)
- **Row 3**: Column headers (8 columns)
- **Rows 4+**: Period entries (8 quarters)
- **Column widths**: A=12, B=12, C=14, D=12, E=12, F=14, G=12, H=35

#### Sheet 12: Approval_SignOff
- **Row 1**: Title banner (merged A1:E1)
- **Rows 3-5**: Document information
- **Rows 6+**: Approval table
- **Column widths**: A=30, B=25, C=15, D=20, E=40

### 9.3 Styling Specifications

| Style Element | Specification |
|--------------|---------------|
| Title Fill | Dark Navy (#002060) |
| Header Fill | Navy (#1F4E79) |
| Section Font | Blue Bold (#1F4E79) |
| Input Fill | Light Yellow (#FFFFCC) |
| Border | Thin black all sides |

---

## 10. Integration Points

### 10.1 Source Workbook Dependencies

| Source | Data Pulled |
|--------|-------------|
| A.5.17.1 | Password policy compliance |
| A.5.17.2 | MFA adoption, lifecycle compliance |
| A.5.17.3 | System assessment results |
| A.5.17.4 | KPIs, incidents, remediation |

### 10.2 Data Flow

```
A.5.17.1 (Password Policy) ─────┐
                                │
A.5.17.2 (MFA/Lifecycle) ───────┼──► A.5.17.5 (This Consolidation)
                                │           │
A.5.17.3 (System Assessment) ───┤           │
                                │           ▼
A.5.17.4 (Compliance) ──────────┘    Executive Reports
                                     Audit Evidence
                                     Management Review
```

---

## 11. Generator Script Reference

**Script**: `generate_a517_5_consolidation_dashboard.py`

**Location**: `10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master/`

**Key Functions**:
- `create_instructions_sheet()`: Methodology guidance
- `create_executive_summary_sheet()`: Management overview
- `create_domain_overview_sheet()`: Domain breakdown
- `create_policy_compliance_sheet()`: Policy element compliance
- `create_lifecycle_compliance_sheet()`: Lifecycle process compliance
- `create_system_compliance_sheet()`: System authentication
- `create_cross_domain_gaps_sheet()`: Gap analysis
- `create_remediation_tracker_sheet()`: Action tracking
- `create_kpi_summary_sheet()`: KPI consolidation
- `create_evidence_index_sheet()`: Evidence cross-reference
- `create_trend_dashboard_sheet()`: Historical trends
- `create_approval_signoff_sheet()`: Executive approval

**Execution**:
```bash
cd 10-isms-scr-base/isms-a.5.17-authentication-information/10_generator-master
python3 generate_a517_5_consolidation_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Identity is the new perimeter."*
— John Kindervag

<!-- QA_VERIFIED: 2026-02-04 -->
