# ISMS-IMP-A.5.5-6.4 - External Communications Compliance Dashboard

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Compliance Monitoring

**Document ID:** ISMS-IMP-A.5.5-6.4
**Version:** 1.0
**Classification:** Internal Use
**Owner:** CISO
**Last Review:** [Date to be set]
**Next Review:** [Date to be set]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | ISMS Team | Initial release |

---

# PART I: USER COMPLETION GUIDE

## 1. Assessment Overview

### 1.1 Purpose

This workbook provides a comprehensive dashboard for monitoring compliance with ISO 27001:2022 Controls A.5.5 (Contact with Authorities) and A.5.6 (Contact with Special Interest Groups). It aggregates KPIs from the underlying assessment workbooks, tracks gaps, monitors trends, and provides audit readiness status.

### 1.2 Scope

The Compliance Dashboard covers:

- **Executive Summary**: High-level compliance status across both controls
- **Authority KPIs (A.5.5)**: Metrics for authority contact management
- **SIG KPIs (A.5.6)**: Metrics for special interest group engagement
- **Compliance Scorecard**: Detailed requirement-by-requirement assessment
- **Gap Analysis**: Identified gaps with remediation tracking
- **Audit Readiness**: Evidence checklist for certification audits
- **Trend Analysis**: Historical compliance performance

### 1.3 Control Requirements

This dashboard monitors compliance with both controls:

**Control A.5.5:**
> *"Appropriate contacts with relevant authorities should be maintained."*

**Control A.5.6:**
> *"Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained."*

### 1.4 Assessment Domains

This workbook is **Domain 4 of 5** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| 1 | Authority Contacts Register | Documenting authority relationships |
| 2 | Special Interest Groups Register | SIG memberships and engagement |
| 3 | External Communication Procedures | Notification and escalation processes |
| **4** | **Compliance Dashboard** | **KPIs and metrics monitoring** |
| 5 | Consolidation Dashboard | Executive summary across domains |

---

## 2. Prerequisites

Before completing this assessment, ensure you have:

### 2.1 Documentation Requirements

- [ ] Completed Authority Contacts Register (A.5.5-6.1)
- [ ] Completed Special Interest Groups Register (A.5.5-6.2)
- [ ] Completed External Communication Procedures (A.5.5-6.3)
- [ ] Previous compliance assessment results (if available)
- [ ] Internal audit findings related to A.5.5-6
- [ ] Management review records

### 2.2 Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, dashboard review |
| **Security Manager** | Data collection, KPI calculation |
| **Compliance Officer** | Regulatory compliance validation |
| **Internal Audit** | Independent verification |
| **DPO** | Data protection requirements validation |

### 2.3 Data Sources

Map data sources for each metric:

| Metric Category | Data Source |
|-----------------|-------------|
| Authority Contact Metrics | A.5.5-6.1 Authority_Registry, Verification_Register |
| SIG Engagement Metrics | A.5.5-6.2 Groups_Registry, Engagement_Log |
| Procedure Compliance | A.5.5-6.3 Communication_Scenarios, Templates |
| Evidence Availability | All workbook Evidence_Register sheets |

---

## 3. Workbook Structure

### 3.1 Sheet Overview

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance for completing the dashboard | Read only |
| Executive_Summary | High-level compliance status | Manual entry |
| Authority_KPIs | A.5.5 performance metrics | Manual entry |
| SIG_KPIs | A.5.6 performance metrics | Manual entry |
| Compliance_Scorecard | Requirement-level assessment | Manual entry |
| Gap_Analysis | Gap tracking and remediation | Manual entry |
| Audit_Readiness | Evidence checklist | Manual entry |
| Trend_Analysis | Historical performance | Manual entry |
| Evidence_Register | Dashboard evidence | Manual entry |
| Approval_SignOff | Management approval | Manual entry |

### 3.2 Sheet Dependencies

```
Instructions (Read First)
        ↓
Source Workbooks (A.5.5-6.1, .2, .3)
        ↓
   ┌────┼────┐
   ↓    ↓    ↓
Authority  SIG   Compliance
KPIs      KPIs   Scorecard
   ↓    ↓    ↓
   └────┬────┘
        ↓
   ┌────┼────┐
   ↓         ↓
Gap_Analysis  Audit_Readiness
   ↓         ↓
   └────┬────┘
        ↓
Executive_Summary (Consolidate)
        ↓
Trend_Analysis
        ↓
Evidence_Register
        ↓
Approval_SignOff (Complete Last)
```

---

## 4. Completion Walkthrough

### 4.1 Executive_Summary Sheet

High-level compliance view for management.

**Overall Status Section:**

| Control | Status | Score | Trend | Key Issues |
|---------|--------|-------|-------|------------|
| A.5.5 Contact with Authorities | [Dropdown] | [%] | [Dropdown] | [Free text] |
| A.5.6 Contact with Special Interest Groups | [Dropdown] | [%] | [Dropdown] | [Free text] |
| Combined A.5.5-6 Compliance | [Dropdown] | [%] | [Dropdown] | [Free text] |

**Key Metrics Summary:**

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Authority contacts documented | 100% | [%] | [Status] | |
| Contacts verified < 12 months | >= 95% | [%] | [Status] | |
| SIG memberships active | >= 5 | [#] | [Status] | |
| Communication procedures documented | 100% | [%] | [Status] | |
| Notification requirements mapped | 100% | [%] | [Status] | |
| Escalation paths tested | Annual | [Date] | [Status] | |

**Status Values:**
- Compliant (Green): Target met
- Partially Compliant (Amber): 50-99% of target
- Non-Compliant (Red): <50% of target

### 4.2 Authority_KPIs Sheet

Metrics for A.5.5 authority contact management.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| KPI_ID | Unique identifier | AUTH-KPI-001 |
| KPI_Name | Metric name | Register Completeness |
| Description | What the KPI measures | % of required authorities documented |
| Target | Target value | 100% |
| Current_Value | Measured value | [Enter] |
| Measurement_Method | How to calculate | Count documented / Required |
| Frequency | Measurement frequency | Quarterly |
| Data_Source | Source workbook/sheet | Authority Registry |
| Owner | Responsible person | CISO |
| Status | Performance status | [Dropdown] |
| Trend | Direction of change | [Dropdown] |
| Comments | Context and actions | [Free text] |

**Standard Authority KPIs:**

| KPI ID | KPI Name | Target | Measurement |
|--------|----------|--------|-------------|
| AUTH-KPI-001 | Register Completeness | 100% | Documented / Required |
| AUTH-KPI-002 | Contact Currency | >= 95% | Verified <12mo / Total |
| AUTH-KPI-003 | Escalation Path Coverage | 100% | Scenarios with path / Total |
| AUTH-KPI-004 | Communication Log Currency | >= 1/authority/6mo | Count per authority |
| AUTH-KPI-005 | Procedure Test Success | >= 90% | Successful tests / Total |

### 4.3 SIG_KPIs Sheet

Metrics for A.5.6 special interest group engagement.

**Standard SIG KPIs:**

| KPI ID | KPI Name | Target | Measurement |
|--------|----------|--------|-------------|
| SIG-KPI-001 | Active Memberships | >= 5 | Count active memberships |
| SIG-KPI-002 | Engagement Frequency | >= 1/quarter | Engagements / Active memberships |
| SIG-KPI-003 | Intelligence Actionability | >= 60% | Actioned / Received |
| SIG-KPI-004 | Contribution Rate | >= 4/year | Count contributions |
| SIG-KPI-005 | Membership ROI | Positive | Value rating vs cost |

### 4.4 Compliance_Scorecard Sheet

Requirement-by-requirement compliance assessment.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Requirement_ID | Unique identifier | REQ-001 |
| Requirement | Control requirement statement | Authority contacts register maintained |
| Control_Reference | ISO control reference | A.5.5 |
| Weight | Scoring weight | 10 |
| Evidence_Available | Is evidence present | Yes/Partial/No |
| Implementation_Status | Current state | Fully Implemented |
| Score | Points achieved | [Calculated] |
| Max_Score | Maximum points | 10 |
| Gap_Description | If gap exists | [Free text] |
| Remediation_Status | If remediation needed | [Dropdown] |

**Standard Requirements:**

| Req ID | Requirement | Control | Weight |
|--------|-------------|---------|--------|
| REQ-001 | Authority contacts register maintained | A.5.5 | 10 |
| REQ-002 | Contact details verified annually | A.5.5 | 10 |
| REQ-003 | Escalation paths documented | A.5.5 | 8 |
| REQ-004 | Communication procedures defined | A.5.5 | 10 |
| REQ-005 | Regulatory notification requirements mapped | A.5.5 | 10 |
| REQ-006 | SIG membership register maintained | A.5.6 | 8 |
| REQ-007 | SIG engagement logged | A.5.6 | 6 |
| REQ-008 | Intelligence received and actioned | A.5.6 | 8 |
| REQ-009 | Contributions appropriately approved | A.5.6 | 6 |
| REQ-010 | Value assessment conducted | A.5.6 | 6 |

**Scoring Methodology:**

| Implementation Status | Score Multiplier |
|-----------------------|------------------|
| Fully Implemented | 100% |
| Partially Implemented | 50% |
| Not Implemented | 0% |
| Not Applicable | N/A (excluded) |

### 4.5 Gap_Analysis Sheet

Track identified gaps and remediation.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-001 |
| Requirement_Reference | Link to scorecard | REQ-002 |
| Gap_Description | What the gap is | Contact verification overdue for 3 authorities |
| Risk_Level | Impact if not addressed | Medium |
| Root_Cause | Why gap exists | No calendar reminders set |
| Remediation_Action | Planned fix | Implement automated verification reminders |
| Owner | Responsible person | Security Manager |
| Target_Date | Deadline | 2026-03-31 |
| Status | Current state | In Progress |
| Progress | Completion percentage | 50% |
| Evidence_of_Closure | How closure verified | Verification records |
| Notes | Additional context | System automation approved |

**Risk Levels:**
- Critical: Regulatory non-compliance risk
- High: Significant security/operational impact
- Medium: Moderate impact, manageable risk
- Low: Minor impact, improvement opportunity

### 4.6 Audit_Readiness Sheet

Evidence checklist for certification audits.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Check_ID | Unique identifier | AUD-001 |
| Audit_Requirement | What auditor will verify | Authority register maintained |
| Evidence_Required | What evidence needed | Completed Authority Registry workbook |
| Evidence_Location | Where evidence stored | [SharePoint path] |
| Evidence_Available | Is evidence ready | Yes/Partial/No |
| Last_Reviewed | When evidence verified | [Date] |
| Reviewer | Who verified | [Name] |
| Status | Readiness status | Ready/Action Required |
| Notes | Issues or actions | [Free text] |

**Standard Audit Checks:**

| Check ID | Audit Requirement | Evidence Required |
|----------|-------------------|-------------------|
| AUD-001 | Authority register maintained | Authority Registry workbook |
| AUD-002 | Contact verification evidence | Verification Register |
| AUD-003 | Communication log complete | Communication Log entries |
| AUD-004 | SIG membership documentation | Membership certificates |
| AUD-005 | Engagement evidence | Meeting minutes, attendance |
| AUD-006 | Intelligence handling records | Intelligence Received log |
| AUD-007 | Contribution approvals | Contribution Log with approvals |
| AUD-008 | Escalation procedures documented | Escalation Matrix |
| AUD-009 | Notification procedures documented | Notification Requirements |
| AUD-010 | Management approval of registers | Approval SignOff sheets |

### 4.7 Trend_Analysis Sheet

Track historical compliance performance.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Period | Reporting period | Q1 2026 |
| Authority_Compliance_Score | A.5.5 score | 85% |
| SIG_Compliance_Score | A.5.6 score | 78% |
| Combined_Score | Overall score | 82% |
| Key_Changes | What changed | Added 2 authority contacts |
| Notable_Events | Significant occurrences | NCSC engagement initiated |
| Actions_Taken | Improvements made | Automated verification |

**Trend Tracking:**
- Record scores quarterly
- Identify patterns and root causes
- Support management review reporting
- Demonstrate continuous improvement

### 4.8 Evidence_Register Sheet

Document dashboard evidence.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Evidence_ID | Unique identifier | EV-2026-001 |
| Evidence_Type | Category | KPI Report |
| Description | What evidence shows | Q1 2026 compliance dashboard |
| Related_Requirement | Linked requirement | Executive Summary |
| Date_Created | When created | 2026-04-01 |
| Created_By | Who created | Security Manager |
| Storage_Location | Where stored | ISMS Evidence Library |
| Retention_Period | How long to retain | 3 years |
| Review_Date | Next review | 2027-04-01 |
| Status | Current status | Current |
| Notes | Additional context | Approved by CISO |

### 4.9 Approval_SignOff Sheet

Management approval for the dashboard.

**Approval Workflow:**

| Step | Role | Responsibility |
|------|------|----------------|
| 1 | Preparer | Calculate KPIs, compile data |
| 2 | Security Manager | Verify data accuracy |
| 3 | Compliance Officer | Validate compliance status |
| 4 | Internal Audit | Independent review (optional) |
| 5 | CISO | Final approval |

---

## 5. Evidence Collection

### 5.1 Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| KPI Reports | Quarterly KPI calculations | ISMS Evidence Library |
| Gap Reports | Gap analysis documentation | ISMS Evidence Library |
| Trend Reports | Historical analysis | ISMS Evidence Library |
| Audit Checklists | Pre-audit verification | ISMS Evidence Library |
| Approval Records | Management sign-offs | ISMS Evidence Library |

### 5.2 Evidence Storage Guidelines

- Use consistent naming: `A.5.5-6.4-[Type]-[Period].pdf`
- Store in ISMS Evidence Library
- Maintain quarterly archives
- Link to source workbook evidence
- Retain for minimum 3 years

---

## 6. Common Pitfalls

### 6.1 Mistakes to Avoid

❌ **MISTAKE:** Calculating KPIs only before audits
✅ **CORRECT:** Calculate KPIs quarterly and track trends continuously

❌ **MISTAKE:** Setting targets without baseline data
✅ **CORRECT:** Establish baselines first, then set realistic improvement targets

❌ **MISTAKE:** Measuring only what's easy to count
✅ **CORRECT:** Include qualitative measures like intelligence actionability and value

❌ **MISTAKE:** Not linking gaps to root causes
✅ **CORRECT:** Perform root cause analysis; address systemic issues, not just symptoms

❌ **MISTAKE:** Marking gaps closed without verification evidence
✅ **CORRECT:** Require documented evidence before closing gaps; verify effectiveness

❌ **MISTAKE:** Dashboard data inconsistent with source workbooks
✅ **CORRECT:** Establish clear data extraction process; reconcile before reporting

❌ **MISTAKE:** Trend analysis without context
✅ **CORRECT:** Document changes, events, and actions that explain trend movements

❌ **MISTAKE:** Audit readiness checked only before audits
✅ **CORRECT:** Maintain audit-ready state continuously; monthly evidence checks

❌ **MISTAKE:** Different scoring methodologies between periods
✅ **CORRECT:** Document scoring methodology; apply consistently for valid trends

❌ **MISTAKE:** Executive summary too detailed for management consumption
✅ **CORRECT:** Keep executive summary to key metrics and issues; detail in underlying sheets

---

## 7. Quality Checklist

Before submitting for approval, verify:

### 7.1 Data Quality

- [ ] All KPI values calculated from source workbook data
- [ ] KPI calculations documented and repeatable
- [ ] No data more than 90 days old
- [ ] Discrepancies investigated and resolved

### 7.2 Completeness

- [ ] All required KPIs measured
- [ ] Compliance scorecard fully assessed
- [ ] All known gaps documented
- [ ] Audit readiness checklist complete

### 7.3 Accuracy

- [ ] Status indicators consistent with scores
- [ ] Trends reflect actual direction of change
- [ ] Gap remediation status current
- [ ] Evidence references verified

### 7.4 Governance

- [ ] Reporting period clearly stated
- [ ] Preparer identified
- [ ] Required approvals obtained
- [ ] Next review scheduled

---

## 8. Review and Approval

### 8.1 Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Assessment | Quarterly | Scheduled review |
| Trend Update | Monthly | Management reporting |
| Gap Review | Monthly | Remediation tracking |
| Audit Readiness | Before audits | Audit schedule |

### 8.2 Approval Authority

| Action | Approval Required |
|--------|-------------------|
| KPI target changes | CISO |
| Gap closure | Compliance Officer |
| Dashboard publication | CISO |
| Trend report | Security Manager |

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Structure

### 9.1 File Specifications

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.5-6.4 |
| **Workbook Name** | External Communications Compliance Dashboard |
| **File Format** | .xlsx (Excel 2007+) |
| **Generated By** | generate_a55_6_4_compliance_dashboard.py |
| **Sheets** | 10 |

### 9.2 Sheet Specifications

#### 9.2.1 Instructions Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance |
| **Protection** | Read-only recommended |
| **Column A Width** | 90 |

**Content Sections:**
- Document title and identifier
- Purpose statement
- Sheet descriptions
- Key metrics tracked
- Refresh frequency
- Generated date and control reference

#### 9.2.2 Executive_Summary Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Executive_Summary |
| **Purpose** | High-level compliance view |
| **Header Row** | Varies by section |
| **Input Cells** | Yellow fill |
| **Calculated Cells** | Green fill |

**Structure:**
- Title row with merged cells (A1:F1)
- Reporting period and date fields
- Overall Status table (rows 5-8)
- Key Metrics Summary table (rows 11-17)

**Data Validations:**
- Status: "Compliant,Partially Compliant,Non-Compliant"
- Trend: "Improving,Stable,Declining"

#### 9.2.3 Authority_KPIs Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Authority_KPIs |
| **Purpose** | A.5.5 metrics |
| **Header Row** | 1 |
| **Pre-populated** | 5 KPIs |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | KPI_ID | 15 | None |
| B | KPI_Name | 25 | None |
| C | Description | 40 | None |
| D | Target | 12 | None |
| E | Current_Value | 15 | Input |
| F | Measurement_Method | 30 | None |
| G | Frequency | 15 | Dropdown |
| H | Data_Source | 20 | None |
| I | Owner | 18 | None |
| J | Status | 12 | Dropdown |
| K | Trend | 12 | Dropdown |
| L | Comments | 35 | None |

**Data Validations:**
- Frequency: "Monthly,Quarterly,Semi-annual,Annual"
- Status: "On Target,At Risk,Below Target"
- Trend: "Improving,Stable,Declining"

#### 9.2.4 SIG_KPIs Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | SIG_KPIs |
| **Purpose** | A.5.6 metrics |
| **Header Row** | 1 |
| **Pre-populated** | 5 KPIs |
| **Input Cells** | Yellow fill |

**Column Structure:** Same as Authority_KPIs

#### 9.2.5 Compliance_Scorecard Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Compliance_Scorecard |
| **Purpose** | Requirement assessment |
| **Header Row** | 1 |
| **Pre-populated** | 10 requirements |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Requirement_ID | 12 | None |
| B | Requirement | 40 | None |
| C | Control_Reference | 15 | None |
| D | Weight | 8 | None |
| E | Evidence_Available | 18 | Dropdown |
| F | Implementation_Status | 22 | Dropdown |
| G | Score | 8 | Calculated |
| H | Max_Score | 10 | None |
| I | Gap_Description | 40 | None |
| J | Remediation_Status | 18 | Dropdown |

**Data Validations:**
- Evidence_Available: "Yes,Partial,No"
- Implementation_Status: "Fully Implemented,Partially Implemented,Not Implemented,Not Applicable"
- Remediation_Status: "Not Required,In Progress,Planned,Completed"

#### 9.2.6 Gap_Analysis Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Gap_Analysis |
| **Purpose** | Gap tracking |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Gap_ID | 12 | None |
| B | Requirement_Reference | 20 | None |
| C | Gap_Description | 45 | None |
| D | Risk_Level | 12 | Dropdown |
| E | Root_Cause | 35 | None |
| F | Remediation_Action | 45 | None |
| G | Owner | 18 | None |
| H | Target_Date | 15 | Date |
| I | Status | 12 | Dropdown |
| J | Progress | 10 | Dropdown |
| K | Evidence_of_Closure | 30 | None |
| L | Notes | 35 | None |

**Data Validations:**
- Risk_Level: "Critical,High,Medium,Low"
- Status: "Open,In Progress,Closed,Deferred"
- Progress: "0%,25%,50%,75%,100%"

#### 9.2.7 Audit_Readiness Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Audit_Readiness |
| **Purpose** | Evidence checklist |
| **Header Row** | 1 |
| **Pre-populated** | 10 checks |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Check_ID | 12 | None |
| B | Audit_Requirement | 35 | None |
| C | Evidence_Required | 40 | None |
| D | Evidence_Location | 35 | Input |
| E | Evidence_Available | 18 | Dropdown |
| F | Last_Reviewed | 15 | Date |
| G | Reviewer | 18 | None |
| H | Status | 18 | Dropdown |
| I | Notes | 35 | None |

**Data Validations:**
- Evidence_Available: "Yes,Partial,No"
- Status: "Ready,Action Required,Not Applicable"

#### 9.2.8 Trend_Analysis Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Trend_Analysis |
| **Purpose** | Historical tracking |
| **Header Row** | 1 |
| **Pre-populated** | 8 periods |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Period | 12 |
| B | Authority_Compliance_Score | 25 |
| C | SIG_Compliance_Score | 25 |
| D | Combined_Score | 18 |
| E | Key_Changes | 40 |
| F | Notable_Events | 40 |
| G | Actions_Taken | 40 |

#### 9.2.9 Evidence_Register Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Evidence_Register |
| **Purpose** | Audit evidence |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Evidence_ID | 12 | None |
| B | Evidence_Type | 18 | Dropdown |
| C | Description | 40 | None |
| D | Related_Requirement | 20 | None |
| E | Date_Created | 15 | Date |
| F | Created_By | 20 | None |
| G | Storage_Location | 40 | None |
| H | Retention_Period | 15 | None |
| I | Review_Date | 15 | Date |
| J | Status | 15 | Dropdown |
| K | Notes | 35 | None |

**Data Validations:**
- Evidence_Type: "KPI Report,Audit Report,Assessment Record,Approval Record,Trend Analysis,Other"
- Status: "Current,Archived,Pending Review"

#### 9.2.10 Approval_SignOff Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Approval_SignOff |
| **Purpose** | Management approval |
| **Header Row** | 1 |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Approval_ID | 12 | None |
| B | Review_Period | 15 | None |
| C | Review_Date | 15 | Date |
| D | Reviewer_Name | 25 | None |
| E | Reviewer_Role | 20 | Dropdown |
| F | Dashboard_Complete | 18 | Dropdown |
| G | KPIs_Current | 15 | Dropdown |
| H | Gaps_Addressed | 15 | Dropdown |
| I | Approval_Status | 15 | Dropdown |
| J | Signature_Date | 15 | Date |
| K | Next_Review_Date | 18 | Date |
| L | Comments | 40 | None |

**Data Validations:**
- Reviewer_Role: "CISO,Security Manager,DPO,Compliance Officer,Internal Audit,CEO"
- Dashboard_Complete: "Yes,No,Partial"
- KPIs_Current: "Yes,No,Partial"
- Gaps_Addressed: "Yes,No,Partial"
- Approval_Status: "Approved,Rejected,Pending,Conditional"

---

## 10. Styling Specifications

### 10.1 Colour Palette

| Element | Colour | Hex Code |
|---------|--------|----------|
| Header Background | Dark Blue | 2F5496 |
| Metric Header | Navy Blue | 1F4E79 |
| Header Font | White | FFFFFF |
| Input Cells | Light Yellow | FFFFCC |
| Calculated Cells | Light Green | E2EFDA |
| Compliant Status | Green | C6EFCE |
| Partial Status | Amber | FFEB9C |
| Non-Compliant Status | Red | FFC7CE |

### 10.2 Font Specifications

| Element | Font | Size | Style |
|---------|------|------|-------|
| Dashboard Title | Default | 16pt | Bold, White |
| Section Header | Default | 12pt | Bold, Blue |
| Column Headers | Default | 11pt | Bold, White |
| Data Cells | Default | 11pt | Normal |

### 10.3 Border Specifications

- All data cells: Thin border (all sides)
- Header cells: Thin border (all sides)

---

## 11. Integration Points

### 11.1 Related Workbooks

| Workbook | Relationship |
|----------|--------------|
| A.5.5-6.1 Authority Contacts | Source for AUTH-KPIs |
| A.5.5-6.2 SIG Register | Source for SIG-KPIs |
| A.5.5-6.3 Procedures | Source for procedure metrics |
| A.5.5-6.5 Consolidation | Aggregates this dashboard |

### 11.2 Data Flow

```
A.5.5-6.1    A.5.5-6.2    A.5.5-6.3
Authority     SIG         Procedures
Registry     Register
    ↓           ↓            ↓
    └───────────┼────────────┘
                ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
Authority_KPIs  SIG_KPIs   Compliance_
                           Scorecard
    ↓           ↓           ↓
    └───────────┼───────────┘
                ↓
        ┌───────┼───────┐
        ↓       ↓       ↓
   Gap_Analysis  Audit    Executive
                Readiness  Summary
        ↓       ↓       ↓
        └───────┼───────┘
                ↓
        Trend_Analysis
                ↓
        A.5.5-6.5 Consolidation
```

---

## 12. Generator Script Reference

**Script:** `generate_a55_6_4_compliance_dashboard.py`

**Key Functions:**
- `create_instructions_sheet(ws)` - Creates guidance sheet
- `create_executive_summary_sheet(ws)` - Creates high-level summary
- `create_authority_kpis_sheet(ws)` - Creates A.5.5 metrics
- `create_sig_kpis_sheet(ws)` - Creates A.5.6 metrics
- `create_compliance_scorecard_sheet(ws)` - Creates requirement assessment
- `create_gap_analysis_sheet(ws)` - Creates gap tracking
- `create_audit_readiness_sheet(ws)` - Creates evidence checklist
- `create_trend_analysis_sheet(ws)` - Creates historical tracking
- `create_evidence_register_sheet(ws)` - Creates evidence documentation
- `create_approval_signoff_sheet(ws)` - Creates approval workflow

**Output:** `ISMS-IMP-A.5.5-6.4_External_Communications_Compliance_Dashboard_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-04 -->
