**ISMS-IMP-A.5.14.5-UG - Consolidation Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.5-UG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-IMP-A.5.14.4 (Compliance Monitoring Dashboard)

---

## Assessment Overview

### Purpose

The **Consolidation Dashboard** (ISMS-IMP-A.5.14.5) aggregates compliance data from all four A.5.14 assessment workbooks into a unified executive view. This dashboard provides holistic visibility into information transfer control compliance, enabling management reporting, audit preparation, and strategic decision-making.

### Scope

This dashboard consolidates:
- **Domain 1**: Transfer Rules and Procedures (A.5.14.1)
- **Domain 2**: Channel Security Assessment (A.5.14.2)
- **Domain 3**: Transfer Agreements Register (A.5.14.3)
- **Domain 4**: Compliance Monitoring Dashboard (A.5.14.4)

### Business Value

Maintaining this consolidation delivers:
- **Unified compliance view** across all transfer domains
- **Executive reporting** with aggregated metrics
- **Cross-domain gap analysis** identifying systemic issues
- **Audit efficiency** through pre-consolidated evidence
- **Trend visibility** showing compliance over time

### Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

This dashboard provides a consolidated view of A.5.14 compliance across all implementation domains.

---

## Prerequisites

Before completing this dashboard, ensure you have:

### Required Workbooks
- [ ] ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures) — current version
- [ ] ISMS-IMP-A.5.14.2 (Channel Security Assessment) — current version
- [ ] ISMS-IMP-A.5.14.3 (Transfer Agreements Register) — current version
- [ ] ISMS-IMP-A.5.14.4 (Compliance Monitoring Dashboard) — current version

### Required Access
- [ ] All source workbook locations
- [ ] Previous consolidation reports (if available)
- [ ] Management reporting templates
- [ ] Risk register for cross-referencing

### Required Personnel
- [ ] Information Security Officer (consolidation owner)
- [ ] Security Analysts (source workbook owners)
- [ ] Risk Manager (gap prioritisation)
- [ ] Executive Sponsor (final approval)

---

## Completion Walkthrough

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

**Purpose**: Single-page management overview of A.5.14 compliance.

**Section 1: Overall Compliance Status**

| Column | Data Source | Action |
|--------|-------------|--------|
| Domain | Fixed labels | Pre-populated |
| Workbook | Source workbook name | Pre-populated |
| Status | Compliance status | Calculate from source |
| Score % | Percentage score | Calculate from source |
| Critical Gaps | Count of critical gaps | Count from sources |
| Last Updated | Source workbook date | Pull from source |

**How to Calculate Domain Scores**:

| Domain | Calculation Method |
|--------|-------------------|
| Transfer Rules | % of transfer methods with defined policies |
| Channel Security | % of channels rated "Compliant" |
| Agreements | % of agreements current and compliant |
| Monitoring | Weighted average of KPIs at target |
| OVERALL | Weighted average of all domains |

**Section 2: Key Metrics**

| Metric | Source | Target |
|--------|--------|--------|
| Transfer procedures documented | A.5.14.1 | 100% |
| Channels security assessed | A.5.14.2 | 100% |
| Third-party agreements current | A.5.14.3 | 100% |
| Transfer incidents resolved | A.5.14.4 | 100% |

### Sheet 3: Domain_Overview

**Purpose**: Requirement-level compliance for each domain.

**For Each Domain Section**:

| Column | Description | Action |
|--------|-------------|--------|
| Requirement | Specific requirement | Pre-populated |
| Status | Compliance status | Pull from source |
| Evidence Ref | Link to evidence | Reference source |
| Gap Description | What is missing | Document if non-compliant |
| Remediation | Planned fix | Document if non-compliant |

**Domain 1: Transfer Rules (A.5.14.1)**
- Transfer policy documented
- Electronic transfer rules
- Physical transfer rules
- Verbal transfer guidelines

**Domain 2: Channel Security (A.5.14.2)**
- Email security assessed
- Cloud service security
- File transfer security
- Physical channel security

**Domain 3: Agreements (A.5.14.3)**
- Agreement register maintained
- Requirements documented
- Third-party assessments current
- Review schedule maintained

### Sheet 4: Transfer_Compliance

**Purpose**: Consolidated view of transfer method compliance.

**For Each Transfer Method**:

| Column | Source | Description |
|--------|--------|-------------|
| Transfer_Method | A.5.14.1 | Transfer method name |
| Policy_Defined | A.5.14.1 | Is policy documented? |
| Security_Controls | A.5.14.2 | Are controls implemented? |
| Encryption_Status | A.5.14.2 | Is encryption active? |
| Monitoring_Active | A.5.14.4 | Is monitoring in place? |
| Compliance_Status | Calculated | Overall status |
| Gap_Notes | Analysis | Description of gaps |
| Owner | Assigned | Accountable person |

**Standard Transfer Methods**:
- Email (Internal)
- Email (External)
- Cloud Storage
- SFTP/SCP
- USB/Removable Media
- Courier/Physical
- API Integration
- Verbal/Telephone

### Sheet 5: Channel_Compliance

**Purpose**: Consolidated channel security status.

**For Each Channel**:

| Column | Source | Description |
|--------|--------|-------------|
| Channel_Type | A.5.14.2 | Channel category |
| Service/Platform | A.5.14.2 | Specific platform |
| Security_Rating | A.5.14.2 | Assessment rating |
| Last_Assessed | A.5.14.2 | Assessment date |
| Risk_Level | A.5.14.2 | Risk assessment |
| Compliance_Status | Calculated | Overall status |
| Gap_Notes | Analysis | Description of gaps |
| Owner | Assigned | Accountable person |

**Standard Channels**:
- Email - Microsoft 365
- Email - Gateway
- Cloud - SharePoint
- Cloud - OneDrive
- File Transfer - SFTP
- Messaging - Teams
- API Gateway
- VPN Tunnel

### Sheet 6: Agreements_Compliance

**Purpose**: Third-party transfer agreement status.

**For Each Third Party**:

| Column | Source | Description |
|--------|--------|-------------|
| Third_Party | A.5.14.3 | Organisation name |
| Agreement_Type | A.5.14.3 | DSA, DPA, etc. |
| Transfer_Type | A.5.14.3 | Direction |
| Expiry_Date | A.5.14.3 | Agreement expiry |
| Review_Status | A.5.14.3 | Current review status |
| Compliance_Status | Calculated | Overall status |
| Gap_Notes | Analysis | Missing requirements |
| Owner | A.5.14.3 | Relationship owner |

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
| Source_Domain | Where first identified | "A.5.14.2 - Channels" |
| Gap_Description | What is the gap | "No encryption on legacy FTP" |
| Risk_Rating | Impact level | "High" |
| Priority | Remediation priority | "Critical" |
| Affected_Controls | Other domains impacted | "A.5.14.1, A.5.14.4" |
| Root_Cause | Why gap exists | "Legacy system dependency" |
| Remediation_Action | How to fix | "Migrate to SFTP by Q2" |
| Owner | Accountable person | "Infrastructure Lead" |
| Target_Date | Expected completion | "30.06.2026" |

### Sheet 8: Remediation_Tracker

**Purpose**: Consolidated view of all A.5.14 remediation activities.

**Pull and Consolidate From**:
- A.5.14.4 Remediation_Tracker sheet
- Cross-domain gaps identified in this workbook

**For Each Remediation Item**:

| Column | Description |
|--------|-------------|
| Action_ID | Unique identifier |
| Related_Gap | Link to gap |
| Source_Domain | Where identified |
| Action_Description | What needs doing |
| Priority | Urgency level |
| Owner | Accountable person |
| Start_Date | When started |
| Target_Date | Expected completion |
| Status | Current state |
| Progress_% | Completion percentage |
| Notes | Progress updates |

### Sheet 9: KPI_Summary

**Purpose**: Consolidated key performance indicators.

**Pull From A.5.14.4** and present:

| Column | Description |
|--------|-------------|
| KPI | Metric name |
| Target | Expected value |
| Current | Actual value |
| Previous | Last period value |
| Trend | Direction indicator |
| Status | Against target |

**Key Transfer KPIs**:
- % of transfer methods with policies
- % of channels security assessed
- % of agreements current (<12 months)
- Transfer incidents (monthly)
- Mean time to resolve incidents
- Third-party compliance rate

### Sheet 10: Evidence_Index

**Purpose**: Cross-reference to all source assessment evidence.

**For Each Evidence Item**:

| Column | Description |
|--------|-------------|
| Evidence_ID | Unique identifier |
| Source_Workbook | Which workbook |
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
| Transfer Rules % | Domain 1 score |
| Channels % | Domain 2 score |
| Agreements % | Domain 3 score |
| Overall % | Consolidated score |
| Incidents | Count in period |
| Remediation Rate | % items closed |
| Notes | Key events/changes |

**Trend Analysis**:
- Identify improving or declining areas
- Correlate trends with initiatives
- Set improvement targets

### Sheet 12: Approval_SignOff

**Purpose**: Executive approval of consolidation.

**Complete**:
1. **Assessment Period**: Specify quarter covered
2. **Consolidation Date**: When compiled
3. **Approval Workflow**:

| Role | Responsibility |
|------|----------------|
| Prepared By | Compiled consolidation |
| Reviewed By | Validated accuracy |
| Approved By (CISO) | Executive approval |
| Data Owner Sign-Off | Domain owners confirm |

---

## Evidence Collection

### Evidence Sources

| Domain | Source Workbook | Evidence Type |
|--------|-----------------|---------------|
| Transfer Rules | A.5.14.1 | Policy documents, matrices |
| Channel Security | A.5.14.2 | Assessment reports, configs |
| Agreements | A.5.14.3 | Signed agreements, certificates |
| Monitoring | A.5.14.4 | Incident records, KPI data |

### Evidence Storage

Store consolidation evidence in:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.5-Consolidation/
│   ├── Dashboard-Reports/
│   ├── Trend-Data/
│   ├── Gap-Analysis/
│   └── Approval-Records/
```

### Evidence Naming

Format: `EV-514-CON-[Type]-[Period]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-CON-Dashboard-Q1-2026-20260401.pdf`
- `EV-514-CON-Trends-2025-20260101.xlsx`
- `EV-514-CON-GapAnalysis-Q4-2025-20260115.docx`

---

## Common Pitfalls

### ❌ MISTAKE: Consolidating without updated source workbooks
✅ CORRECT: Verify all source workbooks are current before consolidating

### ❌ MISTAKE: Calculating scores differently than source workbooks
✅ CORRECT: Use consistent methodology; document calculation methods

### ❌ MISTAKE: Missing cross-domain gap analysis
✅ CORRECT: Actively look for gaps that span multiple domains

### ❌ MISTAKE: Presenting raw data without executive summary
✅ CORRECT: Always include Executive_Summary for management audiences

### ❌ MISTAKE: Not tracking trends over time
✅ CORRECT: Maintain historical data in Trend_Dashboard for analysis

### ❌ MISTAKE: Duplicate evidence entries from source workbooks
✅ CORRECT: Reference source evidence; don't duplicate in consolidation

### ❌ MISTAKE: Consolidation done only before audits
✅ CORRECT: Maintain quarterly consolidation for continuous visibility

### ❌ MISTAKE: No clear owner for cross-domain gaps
✅ CORRECT: Assign single accountable owner even for cross-domain issues

### ❌ MISTAKE: Omitting remediation items from source workbooks
✅ CORRECT: Include all open remediation items in consolidated tracker

### ❌ MISTAKE: Using outdated compliance scores
✅ CORRECT: Recalculate scores from current source data each period

---

## Quality Checklist

Before submitting the consolidation, verify:

### Data Currency
- [ ] All source workbooks updated within 30 days
- [ ] Scores recalculated from current data
- [ ] Last updated dates accurate
- [ ] Period covered clearly stated

### Executive Summary
- [ ] All domains have status and score
- [ ] Key metrics populated
- [ ] Critical gaps identified
- [ ] Overall score calculated correctly

### Domain Details
- [ ] Each domain section complete
- [ ] Status consistent with source workbooks
- [ ] Gap descriptions specific and actionable
- [ ] Evidence references valid

### Cross-Domain Analysis
- [ ] Cross-domain gaps identified
- [ ] Root causes documented
- [ ] Remediation actions assigned
- [ ] Owners and dates set

### Trends and KPIs
- [ ] Historical data complete
- [ ] Trends calculated correctly
- [ ] KPIs aligned with monitoring dashboard
- [ ] Status reflects target comparison

### Evidence and Approval
- [ ] Evidence index complete
- [ ] All evidence locations valid
- [ ] All approvals obtained
- [ ] Distribution list current

---

## Review and Approval

### Consolidation Schedule
- **Frequency**: Quarterly
- **Timing**: First week after quarter end
- **Triggers**: Major changes, pre-audit preparation

### Approval Workflow
1. **Security Analyst** compiles data from sources
2. **Domain Owners** validate their sections
3. **ISO** reviews overall consolidation
4. **CISO** provides executive approval

### Post-Approval Actions
- Distribute to executive stakeholders
- Present at management review
- Archive for audit trail
- Update risk register with findings
- Schedule next consolidation

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
