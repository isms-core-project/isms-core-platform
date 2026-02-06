# ISMS-IMP-A.5.5-6.S5 - External Communications Consolidation Dashboard

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Executive Consolidation

**Document ID:** ISMS-IMP-A.5.5-6.S5
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

This workbook provides a consolidation dashboard that aggregates compliance data from all four A.5.5-6 assessment workbooks into a unified executive view. It enables senior management and auditors to quickly assess the organisation's compliance posture for external communications with authorities and special interest groups.

### 1.2 Scope

The Consolidation Dashboard aggregates data from:

- **Domain 1 (A.5.5-6.1)**: Authority Contacts Register
- **Domain 2 (A.5.5-6.2)**: Special Interest Groups Register
- **Domain 3 (A.5.5-6.3)**: External Communication Procedures
- **Domain 4 (A.5.5-6.4)**: Compliance Dashboard

The consolidation provides:
- Executive-level compliance status
- Cross-domain gap identification
- Unified remediation tracking
- Historical trend analysis
- Evidence traceability for audits

### 1.3 Control Requirements

This dashboard consolidates compliance for both ISO 27001:2022 controls:

**Control A.5.5:**
> *"Appropriate contacts with relevant authorities should be maintained."*

**Control A.5.6:**
> *"Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained."*

### 1.4 Assessment Domains

This workbook is **Domain 5 of 5** in the A.5.5-6 External Communications assessment series:

| Domain | Workbook | Focus |
|--------|----------|-------|
| 1 | Authority Contacts Register | Documenting authority relationships |
| 2 | Special Interest Groups Register | SIG memberships and engagement |
| 3 | External Communication Procedures | Notification and escalation processes |
| 4 | Compliance Dashboard | KPIs and metrics monitoring |
| **5** | **Consolidation Dashboard** | **Executive summary across domains** |

---

## 2. Prerequisites

Before completing this consolidation, ensure you have:

### 2.1 Documentation Requirements

- [ ] **COMPLETED** Authority Contacts Register (A.5.5-6.1)
- [ ] **COMPLETED** Special Interest Groups Register (A.5.5-6.2)
- [ ] **COMPLETED** External Communication Procedures (A.5.5-6.3)
- [ ] **COMPLETED** Compliance Dashboard (A.5.5-6.4)
- [ ] Previous consolidation (if available, for trend analysis)
- [ ] Management review action items

### 2.2 Stakeholder Involvement

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall accountability, executive sign-off |
| **Security Manager** | Data consolidation, accuracy verification |
| **Compliance Officer** | Compliance status validation |
| **Internal Audit** | Independent verification |
| **Executive Sponsor** | Acknowledgement and escalation |

### 2.3 Data Sources

| Dashboard Sheet | Source Workbook | Source Sheet(s) |
|-----------------|-----------------|-----------------|
| Executive_Summary | A.5.5-6.4 | Executive_Summary |
| Domain_Overview | A.5.5-6.1, .2, .3, .4 | All assessment sheets |
| Authority_Compliance | A.5.5-6.1 | Authority_Registry, Verification_Register |
| SIG_Compliance | A.5.5-6.2 | Groups_Registry, Engagement_Log |
| Procedure_Compliance | A.5.5-6.3 | Communication_Scenarios, Templates |
| Cross_Domain_Gaps | A.5.5-6.4 | Gap_Analysis |
| KPI_Summary | A.5.5-6.4 | Authority_KPIs, SIG_KPIs |

---

## 3. Workbook Structure

### 3.1 Sheet Overview

| Sheet | Purpose | Input Required |
|-------|---------|----------------|
| Instructions | Guidance for completing the dashboard | Read only |
| Executive_Summary | High-level compliance across all domains | Manual entry |
| Domain_Overview | Status summary from each workbook | Manual entry |
| Authority_Compliance | Consolidated A.5.5 status | Manual entry |
| SIG_Compliance | Consolidated A.5.6 status | Manual entry |
| Procedure_Compliance | Communication procedure status | Manual entry |
| Cross_Domain_Gaps | Gaps across all domains | Manual entry |
| Remediation_Tracker | Consolidated action items | Manual entry |
| KPI_Summary | Key metrics from all domains | Manual entry |
| Evidence_Index | Cross-reference to source evidence | Manual entry |
| Trend_Dashboard | Historical compliance trends | Manual entry |
| Approval_SignOff | Executive sign-off workflow | Manual entry |

### 3.2 Consolidation Flow

```
Source Workbooks
        ↓
   ┌────┼────┬────┐
   ↓    ↓    ↓    ↓
A.5.5-6.1  .2   .3   .4
   ↓    ↓    ↓    ↓
   └────┼────┴────┘
        ↓
Domain_Overview (Consolidate Status)
        ↓
   ┌────┼────┬────┐
   ↓    ↓    ↓    ↓
Authority  SIG  Procedure  KPI
Compliance Compliance  Compliance  Summary
   ↓    ↓    ↓    ↓
   └────┼────┴────┘
        ↓
   ┌────┼────┐
   ↓         ↓
Cross_Domain  Remediation
Gaps          Tracker
   ↓         ↓
   └────┬────┘
        ↓
Executive_Summary (Final Consolidation)
        ↓
   ┌────┼────┐
   ↓         ↓
Evidence   Trend
Index      Dashboard
   ↓         ↓
   └────┬────┘
        ↓
Approval_SignOff (Complete Last)
```

---

## 4. Completion Walkthrough

### 4.1 Executive_Summary Sheet

Top-level compliance view for senior management.

**Reporting Information:**

| Field | Description | Example |
|-------|-------------|---------|
| Reporting Period | Assessment period | Q1 2026 |
| Assessment Date | When consolidation prepared | 2026-04-01 |
| Assessor | Who prepared consolidation | Security Manager |

**Overall Compliance Status:**

| Domain | Workbook | Status | Score % | Critical Gaps | Last Updated |
|--------|----------|--------|---------|---------------|--------------|
| A.5.5 | Authority Contacts Register | [Dropdown] | [%] | [#] | [Date] |
| A.5.6 | Special Interest Groups Register | [Dropdown] | [%] | [#] | [Date] |
| A.5.5-6 | Communication Procedures | [Dropdown] | [%] | [#] | [Date] |
| A.5.5-6 | Compliance Dashboard | [Dropdown] | [%] | [#] | [Date] |
| **OVERALL** | **Consolidated Assessment** | [Dropdown] | [%] | [#] | [Date] |

**Key Metrics Summary:**

| Metric | Target | Actual | Status | Trend |
|--------|--------|--------|--------|-------|
| Authority contacts documented | 100% | [%] | [Status] | [Trend] |
| Contacts verified within 12 months | 100% | [%] | [Status] | [Trend] |
| SIG memberships with value assessment | 100% | [%] | [Status] | [Trend] |
| Communication procedures documented | 100% | [%] | [Status] | [Trend] |
| Notification requirements covered | 100% | [%] | [Status] | [Trend] |
| Evidence availability for audit | 100% | [%] | [Status] | [Trend] |

**Executive Sign-Off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | [Name] | [Signature] | [Date] |
| Compliance Manager | [Name] | [Signature] | [Date] |
| Legal Counsel | [Name] | [Signature] | [Date] |

### 4.2 Domain_Overview Sheet

Detailed compliance status from each source workbook.

**Structure:**
- **Domain 1: Authority Contacts (A.5.5-6.1)**
  - Requirement-level compliance status
  - Gap summary
  - Remediation status

- **Domain 2: Special Interest Groups (A.5.5-6.2)**
  - Membership compliance status
  - Engagement status
  - Value assessment status

- **Domain 3: Communication Procedures (A.5.5-6.3)**
  - Procedure documentation status
  - Template availability
  - Escalation matrix status

**Per-Domain Fields:**

| Requirement | Status | Evidence Ref | Gap Description | Remediation |
|-------------|--------|--------------|-----------------|-------------|
| [Requirement text] | [Dropdown] | [Reference] | [Description] | [Status] |

### 4.3 Authority_Compliance Sheet

Consolidated view of A.5.5 compliance.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Authority_Type | Category of authority | Data Protection Authority |
| Authority_Name | Specific authority | FDPIC |
| Contact_Status | Documentation status | Complete |
| Last_Verified | Verification date | 2026-01-15 |
| Next_Review | Scheduled review | 2026-07-15 |
| Compliance_Status | Assessment status | Compliant |
| Gap_Notes | Any gaps identified | None |
| Action_Required | Remediation needed | None |
| Owner | Responsible person | DPO |

**Authority Types to Cover:**

| Type | Example Authorities |
|------|---------------------|
| Law Enforcement - Local | Cantonal Police |
| Law Enforcement - National | Fedpol |
| Data Protection Authority | FDPIC |
| Financial Regulator | FINMA |
| Industry Regulator | OFCOM |
| Emergency Services - Fire | Local fire brigade |
| Emergency Services - Medical | Emergency medical services |
| Cyber Security Agency | NCSC |
| Government Security Centre | Federal Security Service |

### 4.4 SIG_Compliance Sheet

Consolidated view of A.5.6 compliance.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| SIG_Category | Type of group | ISAC |
| Group_Name | Specific group | FS-ISAC |
| Membership_Status | Current status | Active |
| Value_Rating | Assessed value | High |
| Last_Engagement | Recent activity | 2026-01-20 |
| Intelligence_Received | Intel received | Yes |
| Compliance_Status | Assessment status | Compliant |
| Gap_Notes | Any gaps | None |
| Owner | Responsible person | CISO |

**SIG Categories to Cover:**

| Category | Examples |
|----------|----------|
| ISAC - Financial | FS-ISAC |
| ISAC - Healthcare | H-ISAC |
| ISAC - Critical Infrastructure | WaterISAC, E-ISAC |
| Security Forum - National | National CERT forums |
| Security Forum - Industry | Sector-specific groups |
| Professional Association | ISACA, (ISC)², ISSA |
| Vendor Security Group | Microsoft security community |
| Academic Research Group | University research partnerships |

### 4.5 Procedure_Compliance Sheet

Communication procedure completeness.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Procedure_Type | Category | Incident Notification |
| Procedure_Name | Specific procedure | Data Breach Notification Procedure |
| Status | Documentation status | Documented |
| Last_Reviewed | Review date | 2026-01-10 |
| Compliance_Status | Assessment status | Compliant |
| Gap_Description | Any gaps | None |
| Remediation_Action | Actions needed | None |
| Owner | Responsible person | DPO |

**Procedures to Cover:**

| Type | Procedures |
|------|------------|
| Incident Notification | Security incident reporting, data breach notification |
| Regulatory Reporting | Compliance reporting, annual security report |
| Media Communication | Media response, crisis communication |
| Escalation | External contact escalation matrix |
| Templates | Authority templates, regulatory submission templates |

### 4.6 Cross_Domain_Gaps Sheet

Gaps identified across all domains.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Gap_ID | Unique identifier | GAP-001 |
| Source_Domain | Which workbook | A.5.5-6.1 Authority Contacts |
| Gap_Description | What the gap is | Two authority contacts not verified |
| Risk_Rating | Impact level | Medium |
| Priority | Remediation priority | High |
| Affected_Controls | Controls impacted | A.5.5 |
| Root_Cause | Why gap exists | Resource constraints |
| Remediation_Action | Planned fix | Schedule verification calls |
| Owner | Responsible person | Security Manager |
| Target_Date | Deadline | 2026-03-15 |

### 4.7 Remediation_Tracker Sheet

Consolidated action items with status.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Action_ID | Unique identifier | ACT-001 |
| Related_Gap | Link to gap | GAP-001 |
| Source_Domain | Origin workbook | A.5.5-6.1 |
| Action_Description | What must be done | Verify authority contacts |
| Priority | Urgency level | High |
| Owner | Responsible person | Security Manager |
| Start_Date | When started | 2026-02-01 |
| Target_Date | Deadline | 2026-03-15 |
| Status | Current status | In Progress |
| Progress_% | Completion | 50% |
| Notes | Additional context | 3 of 6 contacts verified |

### 4.8 KPI_Summary Sheet

Key metrics from all domains.

**Authority Contact KPIs (A.5.5):**

| KPI | Target | Current | Previous | Trend | Status |
|-----|--------|---------|----------|-------|--------|
| % of required authorities documented | 100% | [%] | [%] | [Trend] | [Status] |
| % of contacts verified (<12 months) | 100% | [%] | [%] | [Trend] | [Status] |
| Average days since last verification | <180 | [Days] | [Days] | [Trend] | [Status] |
| % with defined communication protocol | 100% | [%] | [%] | [Trend] | [Status] |

**SIG Engagement KPIs (A.5.6):**

| KPI | Target | Current | Previous | Trend | Status |
|-----|--------|---------|----------|-------|--------|
| % of SIG memberships with value assessment | 100% | [%] | [%] | [Trend] | [Status] |
| Intelligence items received (quarterly) | >10 | [#] | [#] | [Trend] | [Status] |
| Contributions made (quarterly) | >2 | [#] | [#] | [Trend] | [Status] |
| % of memberships actively engaged | ≥80% | [%] | [%] | [Trend] | [Status] |

**Procedure KPIs:**

| KPI | Target | Current | Previous | Trend | Status |
|-----|--------|---------|----------|-------|--------|
| % of communication procedures documented | 100% | [%] | [%] | [Trend] | [Status] |
| % of procedures reviewed (<12 months) | 100% | [%] | [%] | [Trend] | [Status] |
| % of notification requirements covered | 100% | [%] | [%] | [Trend] | [Status] |
| Template availability score | 100% | [%] | [%] | [Trend] | [Status] |

### 4.9 Evidence_Index Sheet

Cross-reference to source workbook evidence.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Evidence_ID | Unique identifier | EV-001 |
| Source_Workbook | Origin workbook | A.5.5-6.1 Authority Contacts |
| Source_Sheet | Specific sheet | Evidence_Register |
| Evidence_Type | Category | Verification Record |
| Evidence_Description | What it proves | Authority contact verification |
| Location/Reference | Where stored | SharePoint/ISMS/A.5.5-6/Evidence |
| Date_Captured | When created | 2026-01-15 |
| Validation_Status | Verification status | Validated |

### 4.10 Trend_Dashboard Sheet

Historical compliance trends.

**Required Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Period | Reporting period | Q1 2025 |
| A.5.5_Authority_% | Authority compliance | 85% |
| A.5.6_SIG_% | SIG compliance | 78% |
| Procedures_% | Procedure compliance | 90% |
| Overall_% | Combined score | 84% |
| Critical_Gaps | Gap count | 2 |
| Remediation_Rate | Closure rate | 75% |
| Notes | Context | New ISAC membership added |

### 4.11 Approval_SignOff Sheet

Executive sign-off workflow.

**Assessment Details:**

| Field | Value |
|-------|-------|
| Assessment Period | [Period] |
| Consolidation Date | [Date] |
| Prepared By | [Name] |

**Approval Workflow:**

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| Prepared By (Analyst) | [Name] | [Date] | [Signature] | [Comments] |
| Reviewed By (Security Manager) | [Name] | [Date] | [Signature] | [Comments] |
| Validated By (Compliance Officer) | [Name] | [Date] | [Signature] | [Comments] |
| Approved By (CISO) | [Name] | [Date] | [Signature] | [Comments] |
| Acknowledged By (Executive Sponsor) | [Name] | [Date] | [Signature] | [Comments] |

**Declaration:**
> I confirm that this consolidation dashboard accurately represents the current compliance status of ISO 27001:2022 Controls A.5.5 and A.5.6 based on the source assessment workbooks. All gaps and remediation actions have been identified and assigned to responsible owners.

---

## 5. Evidence Collection

### 5.1 Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Source Workbooks | Completed A.5.5-6.1 through .4 | ISMS Evidence Library |
| Consolidation Report | This completed dashboard | ISMS Evidence Library |
| Trend Analysis | Historical comparison | ISMS Evidence Library |
| Sign-off Records | Approval documentation | ISMS Evidence Library |
| Audit Reports | Internal/external audit findings | ISMS Evidence Library |

### 5.2 Evidence Storage Guidelines

- Use consistent naming: `A.5.5-6.5-Consolidation-[Period].xlsx`
- Store in ISMS Evidence Library
- Maintain quarterly archives
- Keep source workbooks linked
- Retain for minimum 3 years

---

## 6. Common Pitfalls

### 6.1 Mistakes to Avoid

❌ **MISTAKE:** Consolidating before source workbooks are complete
✅ **CORRECT:** Verify all four source workbooks are signed off before consolidation

❌ **MISTAKE:** Data in consolidation doesn't match source workbooks
✅ **CORRECT:** Establish data extraction process; verify all data traces back to sources

❌ **MISTAKE:** Treating consolidation as a one-time annual activity
✅ **CORRECT:** Update quarterly; keep current between audits

❌ **MISTAKE:** Executive summary too detailed for management
✅ **CORRECT:** Keep executive summary to key metrics; drill-down detail in other sheets

❌ **MISTAKE:** Gaps listed but not assigned to owners
✅ **CORRECT:** Every gap must have owner, target date, and remediation action

❌ **MISTAKE:** Trend data not comparable between periods
✅ **CORRECT:** Use consistent methodology; note any changes affecting comparability

❌ **MISTAKE:** Evidence index doesn't link to actual evidence
✅ **CORRECT:** Verify all evidence references are valid; update locations if moved

❌ **MISTAKE:** Missing executive sign-off before audit
✅ **CORRECT:** Complete approval workflow before presenting to auditors

❌ **MISTAKE:** Remediation tracker shows closed items without evidence
✅ **CORRECT:** Require documented evidence of closure before marking complete

❌ **MISTAKE:** KPI summary shows different values than source dashboard
✅ **CORRECT:** KPIs should be identical; reconcile any differences before publishing

---

## 7. Quality Checklist

Before submitting for approval, verify:

### 7.1 Source Data

- [ ] All four source workbooks completed and approved
- [ ] Data extracted correctly from each source
- [ ] No stale data (all within 90 days)
- [ ] Discrepancies investigated and resolved

### 7.2 Completeness

- [ ] Executive summary reflects all domains
- [ ] All authority types covered
- [ ] All SIG categories covered
- [ ] All procedure types covered
- [ ] All gaps tracked
- [ ] All KPIs reported

### 7.3 Accuracy

- [ ] Compliance scores match source calculations
- [ ] Gap counts reconcile with source workbooks
- [ ] Remediation status current
- [ ] Evidence index references valid

### 7.4 Governance

- [ ] Reporting period clearly stated
- [ ] Assessor identified
- [ ] All approval signatures obtained
- [ ] Next review scheduled

---

## 8. Review and Approval

### 8.1 Review Frequency

| Review Type | Frequency | Triggered By |
|-------------|-----------|--------------|
| Full Consolidation | Quarterly | Scheduled review |
| Trend Update | Quarterly | After source workbook updates |
| Pre-Audit Review | Before audits | Audit schedule |
| Ad-hoc Update | As needed | Significant changes |

### 8.2 Approval Authority

| Action | Approval Required |
|--------|-------------------|
| Consolidation publication | CISO |
| Gap closure verification | Compliance Officer |
| Trend analysis | Security Manager |
| Executive presentation | Executive Sponsor acknowledgement |

---

# PART II: TECHNICAL SPECIFICATION

## 9. Workbook Technical Structure

### 9.1 File Specifications

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.5-6.S5 |
| **Workbook Name** | Consolidation Dashboard |
| **File Format** | .xlsx (Excel 2007+) |
| **Generated By** | generate_a55_6_5_consolidation_dashboard.py |
| **Sheets** | 12 |

### 9.2 Sheet Specifications

#### 9.2.1 Instructions Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance |
| **Protection** | Read-only recommended |
| **Column A Width** | 95 |

**Content Sections:**
- Document title and identifier
- Purpose statement
- Source workbook descriptions
- Sheet descriptions
- Data entry guidance
- Compliance scoring methodology
- Generated date and control reference

#### 9.2.2 Executive_Summary Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Executive_Summary |
| **Purpose** | High-level compliance view |
| **Title Row** | Merged A1:H1 |
| **Input Cells** | Yellow fill |

**Structure:**
- Title with merged cells
- Reporting period/date/assessor fields
- Overall compliance status table (5 domains)
- Key metrics summary table (6 metrics)
- Executive sign-off section (3 roles)

**Column Widths:**
| Column | Width |
|--------|-------|
| A | 35 |
| B | 35 |
| C | 20 |
| D | 12 |
| E | 15 |
| F | 15 |
| G | 15 |
| H | 20 |

#### 9.2.3 Domain_Overview Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Domain_Overview |
| **Purpose** | Domain-by-domain status |
| **Title Row** | Merged A1:J1 |
| **Input Cells** | Yellow fill |

**Structure:**
- Title with merged cells
- Domain 1 section: Authority Contacts (rows 3-9)
- Domain 2 section: Special Interest Groups (rows 11-17)
- Domain 3 section: Communication Procedures (rows 19-25)

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Requirement | 40 |
| B | Status | 18 |
| C | Evidence_Ref | 15 |
| D | Gap_Description | 35 |
| E | Remediation | 35 |

#### 9.2.4 Authority_Compliance Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Authority_Compliance |
| **Purpose** | A.5.5 consolidated status |
| **Title Row** | Merged A1:I1 |
| **Pre-populated** | 9 authority types |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Authority_Type | 25 | None |
| B | Authority_Name | 30 | Input |
| C | Contact_Status | 15 | Input |
| D | Last_Verified | 15 | Date |
| E | Next_Review | 15 | Date |
| F | Compliance_Status | 18 | Dropdown |
| G | Gap_Notes | 30 | None |
| H | Action_Required | 25 | None |
| I | Owner | 20 | None |

**Data Validations:**
- Compliance_Status: "Compliant,Partially Compliant,Non-Compliant,Not Assessed"

#### 9.2.5 SIG_Compliance Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | SIG_Compliance |
| **Purpose** | A.5.6 consolidated status |
| **Title Row** | Merged A1:I1 |
| **Pre-populated** | 8 SIG categories |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | SIG_Category | 25 |
| B | Group_Name | 30 |
| C | Membership_Status | 18 |
| D | Value_Rating | 15 |
| E | Last_Engagement | 18 |
| F | Intelligence_Received | 20 |
| G | Compliance_Status | 18 |
| H | Gap_Notes | 30 |
| I | Owner | 20 |

#### 9.2.6 Procedure_Compliance Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Procedure_Compliance |
| **Purpose** | Procedure status |
| **Title Row** | Merged A1:H1 |
| **Pre-populated** | 9 procedures |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Procedure_Type | 22 |
| B | Procedure_Name | 40 |
| C | Status | 15 |
| D | Last_Reviewed | 15 |
| E | Compliance_Status | 18 |
| F | Gap_Description | 35 |
| G | Remediation_Action | 30 |
| H | Owner | 20 |

#### 9.2.7 Cross_Domain_Gaps Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Cross_Domain_Gaps |
| **Purpose** | Consolidated gaps |
| **Title Row** | Merged A1:J1 |
| **Pre-populated** | 15 gap rows |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Gap_ID | 10 | Pre-filled |
| B | Source_Domain | 25 | Dropdown |
| C | Gap_Description | 40 | None |
| D | Risk_Rating | 12 | Dropdown |
| E | Priority | 10 | Dropdown |
| F | Affected_Controls | 20 | None |
| G | Root_Cause | 30 | None |
| H | Remediation_Action | 35 | None |
| I | Owner | 18 | None |
| J | Target_Date | 15 | Date |

**Data Validations:**
- Source_Domain: "A.5.5-6.1 Authority Contacts,A.5.5-6.2 SIG Membership,A.5.5-6.3 Procedures,A.5.5-6.4 Dashboard,Cross-Domain"
- Risk_Rating: "Critical,High,Medium,Low"
- Priority: "Critical,High,Medium,Low"

#### 9.2.8 Remediation_Tracker Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Remediation_Tracker |
| **Purpose** | Action tracking |
| **Title Row** | Merged A1:K1 |
| **Pre-populated** | 20 action rows |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Action_ID | 10 | Pre-filled |
| B | Related_Gap | 12 | None |
| C | Source_Domain | 22 | None |
| D | Action_Description | 40 | None |
| E | Priority | 10 | Dropdown |
| F | Owner | 18 | None |
| G | Start_Date | 12 | Date |
| H | Target_Date | 12 | Date |
| I | Status | 12 | Dropdown |
| J | Progress_% | 10 | None |
| K | Notes | 30 | None |

**Data Validations:**
- Status: "Not Started,In Progress,On Hold,Completed,Cancelled"
- Priority: "Critical,High,Medium,Low"

#### 9.2.9 KPI_Summary Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | KPI_Summary |
| **Purpose** | Aggregated metrics |
| **Title Row** | Merged A1:H1 |
| **Input Cells** | Yellow fill |

**Structure:**
- Authority KPIs section (rows 3-8)
- SIG KPIs section (rows 10-15)
- Procedure KPIs section (rows 17-22)

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | KPI | 45 |
| B | Target | 12 |
| C | Current | 12 |
| D | Previous | 12 |
| E | Trend | 10 |
| F | Status | 15 |

#### 9.2.10 Evidence_Index Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Evidence_Index |
| **Purpose** | Evidence cross-reference |
| **Title Row** | Merged A1:H1 |
| **Pre-populated** | 20 evidence rows |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width | Validation |
|--------|--------|-------|------------|
| A | Evidence_ID | 12 | Pre-filled |
| B | Source_Workbook | 25 | Dropdown |
| C | Source_Sheet | 25 | None |
| D | Evidence_Type | 18 | None |
| E | Evidence_Description | 40 | None |
| F | Location/Reference | 30 | None |
| G | Date_Captured | 15 | Date |
| H | Validation_Status | 18 | Dropdown |

**Data Validations:**
- Source_Workbook: "A.5.5-6.1 Authority Contacts,A.5.5-6.2 SIG Register,A.5.5-6.3 Procedures,A.5.5-6.4 Dashboard"
- Validation_Status: "Validated,Pending,Invalid"

#### 9.2.11 Trend_Dashboard Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Trend_Dashboard |
| **Purpose** | Historical trends |
| **Title Row** | Merged A1:H1 |
| **Pre-populated** | 8 periods |
| **Input Cells** | Yellow fill |

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Period | 12 |
| B | A.5.5_Authority_% | 18 |
| C | A.5.6_SIG_% | 15 |
| D | Procedures_% | 15 |
| E | Overall_% | 12 |
| F | Critical_Gaps | 15 |
| G | Remediation_Rate | 18 |
| H | Notes | 35 |

#### 9.2.12 Approval_SignOff Sheet

| Attribute | Specification |
|-----------|---------------|
| **Sheet Name** | Approval_SignOff |
| **Purpose** | Executive approval |
| **Title Row** | Merged A1:F1 |
| **Input Cells** | Yellow fill |

**Structure:**
- Assessment details section (rows 3-5)
- Approval workflow table (rows 7-14)
- Declaration section (rows 16-18)

**Column Structure:**

| Column | Header | Width |
|--------|--------|-------|
| A | Role | 35 |
| B | Name | 25 |
| C | Date | 15 |
| D | Signature | 20 |
| E | Comments | 40 |

---

## 10. Styling Specifications

### 10.1 Colour Palette

| Element | Colour | Hex Code |
|---------|--------|----------|
| Title Background | Dark Navy | 002060 |
| Header Background | Navy Blue | 1F4E79 |
| Header Font | White | FFFFFF |
| Section Header | Blue (text) | 1F4E79 |
| Input Cells | Light Yellow | FFFFCC |
| Calculated Cells | Light Green | E2EFDA |
| Compliant | Green | C6EFCE |
| Partial | Amber | FFEB9C |
| Non-Compliant | Red | FFC7CE |

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
| A.5.5-6.1 Authority Contacts | Data source |
| A.5.5-6.2 SIG Register | Data source |
| A.5.5-6.3 Procedures | Data source |
| A.5.5-6.4 Compliance Dashboard | Data source |

### 11.2 Data Flow

```
A.5.5-6.1      A.5.5-6.2      A.5.5-6.3      A.5.5-6.4
Authority       SIG          Procedures     Compliance
Registry       Register                      Dashboard
    ↓             ↓              ↓              ↓
    └─────────────┼──────────────┼──────────────┘
                  ↓
         ┌────────┼────────┐
         ↓        ↓        ↓
    Authority    SIG    Procedure
    Compliance  Compliance  Compliance
         ↓        ↓        ↓
         └────────┼────────┘
                  ↓
         ┌────────┼────────┐
         ↓        ↓        ↓
    Cross_Domain  KPI    Evidence
        Gaps     Summary   Index
         ↓        ↓        ↓
         └────────┼────────┘
                  ↓
         Executive_Summary
                  ↓
         Trend_Dashboard
                  ↓
         Approval_SignOff
```

---

## 12. Generator Script Reference

**Script:** `generate_a55_6_5_consolidation_dashboard.py`

**Key Functions:**
- `create_instructions_sheet(ws)` - Creates guidance sheet
- `create_executive_summary_sheet(ws)` - Creates high-level summary
- `create_domain_overview_sheet(ws)` - Creates domain status
- `create_authority_compliance_sheet(ws)` - Creates A.5.5 view
- `create_sig_compliance_sheet(ws)` - Creates A.5.6 view
- `create_procedure_compliance_sheet(ws)` - Creates procedure status
- `create_cross_domain_gaps_sheet(ws)` - Creates consolidated gaps
- `create_remediation_tracker_sheet(ws)` - Creates action tracking
- `create_kpi_summary_sheet(ws)` - Creates metrics summary
- `create_evidence_index_sheet(ws)` - Creates evidence cross-reference
- `create_trend_dashboard_sheet(ws)` - Creates historical trends
- `create_approval_signoff_sheet(ws)` - Creates executive approval

**Output:** `ISMS-IMP-A.5.5-6.S5_Consolidation_Dashboard_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"The whole is greater than the sum of its parts."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-04 -->
