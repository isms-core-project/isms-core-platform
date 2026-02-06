**ISMS-IMP-A.8.33-34.3-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

### ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of Information Systems During Audit Testing

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.33-34.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Consolidated Oversight |
| **Related Policy** | ISMS-POL-A.8.33-34 (All Sections) |
| **Purpose** | Consolidate all domain assessments into executive compliance view with scoring, gap analysis, exception tracking, and audit readiness certification |
| **Target Audience** | CISO, Executive Management, Board of Directors, Internal/External Auditors, ISO 27001 Certification Bodies, Workbook Developers |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Quarterly (synchronized with domain assessments) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial technical specification for Testing and Audit Protection Compliance Dashboard workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.33-34.3-UG.

---

# Technical Specification

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.33-34.3-TG
**Assessment Area:** Compliance Dashboard (Consolidated Oversight)
**Related Policy:** ISMS-POL-A.8.33-34 (Test Information & Audit Protection)
**Purpose:** Consolidate compliance data from both A.8.33-34 assessment workbooks into executive-level dashboard

**CRITICAL DESIGN PRINCIPLE:** This dashboard uses **Excel external workbook references** to pull live data from normalized source workbooks. Dashboard does NOT duplicate data entry - it aggregates and visualizes data from the 2 assessment workbooks.

---

## Source Workbooks

This dashboard consolidates data from these two normalized assessment workbooks:

1. **ISMS-IMP-A.8.33-34.1.xlsx** - Test Data Protection Assessment
2. **ISMS-IMP-A.8.33-34.2.xlsx** - Audit Activity Management Assessment

**Normalization Workflow:**
1. Generate assessment workbooks with dated filenames (Scripts 1-2)
2. Run `normalize_assessment_files_a833-34.py` to create normalized copies
3. Generate this dashboard workbook (Script 3)
4. Place dashboard in same directory as normalized files
5. Open dashboard - Excel prompts "Update Links" - Auto-populates with current data

**External Reference Format:**
```
='[ISMS-IMP-A.8.33-34.1.xlsx]Summary_Dashboard'!B5
=COUNTIF('[ISMS-IMP-A.8.33-34.2.xlsx]Audit_Activity_Register'!G5:G54,"Authorized")
='[ISMS-IMP-A.8.33-34.1.xlsx]Test_Data_Inventory'!F15
```

---

## Workbook Structure

### Sheet 1: Executive_Dashboard

#### Header Section

- **Title:** "ISMS-IMP-A.8.33-34.3 - Testing and Audit Protection Compliance Dashboard"
- **Subtitle:** "ISO/IEC 27001:2022 - Controls A.8.33 & A.8.34: Executive Overview"
- **Styling:** Dark blue header (003366), white text, centered, 50px height

#### Document Information Block (Rows 3-13)
```
Document Information            [Section Header]

Document ID:           ISMS-IMP-A.8.33-34.3
Report Type:           Compliance Summary Dashboard
Related Policy:        ISMS-POL-A.8.33-34 (Test Information & Audit Protection)
Version:               1.0
Report Date:           [USER INPUT - yellow cell]
Reporting Period:      [USER INPUT - yellow cell]
Prepared By:           [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
Last Updated:          [Formula: =TODAY(), gray cell, DD.MM.YYYY format]
```

#### Overall Compliance Summary (Rows 15-22)

**Section Header:** "OVERALL COMPLIANCE SUMMARY"

| Assessment Area | Compliance % | Status | Critical Gaps | Evidence Count | Last Updated |
|-----------------|--------------|--------|---------------|----------------|--------------|
| Test Data Protection (IMP-A.8.33-34.1) | Formula: ='[ISMS-IMP-A.8.33-34.1.xlsx]Summary_Dashboard'!F5 | Formula | Formula | Formula | Formula |
| Audit Activity Management (IMP-A.8.33-34.2) | Formula from A.8.33-34.2 | Formula | Formula | Formula | Formula |
| **OVERALL AVERAGE** | Formula: =AVERAGE(B17:B18) | Conditional | Formula | Formula | Formula |

**Conditional Formatting:**

- Compliance % cell: Green if ≥85%, Yellow if 70-84%, Red if <70%
- Status cell: Auto-populate based on compliance %

#### Key Performance Indicators (Rows 24-40)

**Section Header:** "KEY PERFORMANCE INDICATORS"

| KPI | Target | Current | Status | Trend | Source |
|-----|--------|---------|--------|-------|--------|
| **Test Data Domain** | | | | | |
| Data Set Authorization Rate | 100% | Formula from A.8.33-34.1 | Auto | [User] | IMP-A.8.33-34.1 |
| PII Masking Coverage | 100% | Formula from A.8.33-34.1 | Auto | [User] | IMP-A.8.33-34.1 |
| Average Masking Effectiveness | ≥4.0 | Formula from A.8.33-34.1 | Auto | [User] | IMP-A.8.33-34.1 |
| Environment Security Compliance | ≥90% | Formula from A.8.33-34.1 | Auto | [User] | IMP-A.8.33-34.1 |
| Refresh Authorization Rate | 100% | Formula from A.8.33-34.1 | Auto | [User] | IMP-A.8.33-34.1 |
| **Audit Activity Domain** | | | | | |
| Audit Authorization Rate | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |
| Tool Authorization Rate | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |
| Access Approval Rate | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |
| Access Revocation Timeliness | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |
| Critical System Mitigation Coverage | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |
| Evidence Encryption Rate | 100% | Formula from A.8.33-34.2 | Auto | [User] | IMP-A.8.33-34.2 |

#### Control Compliance Mapping (Rows 42-55)

**Section Header:** "ISO 27001:2022 CONTROL COMPLIANCE MAPPING"

| ISO Control | Requirement | Assessment Source | Compliance | Status | Evidence |
|-------------|-------------|-------------------|------------|--------|----------|
| A.8.33 | Test information appropriately protected | IMP-A.8.33-34.1 | Formula | Auto | Link |
| A.8.33 | Production data copied only when authorized | IMP-A.8.33-34.1 | Formula | Auto | Link |
| A.8.33 | Test data masked/anonymized | IMP-A.8.33-34.1 | Formula | Auto | Link |
| A.8.33 | Test environments secured | IMP-A.8.33-34.1 | Formula | Auto | Link |
| A.8.34 | Audit tests planned and agreed | IMP-A.8.33-34.2 | Formula | Auto | Link |
| A.8.34 | Audit tools authorized | IMP-A.8.33-34.2 | Formula | Auto | Link |
| A.8.34 | Auditor access controlled | IMP-A.8.33-34.2 | Formula | Auto | Link |
| A.8.34 | Production systems protected during testing | IMP-A.8.33-34.2 | Formula | Auto | Link |
| A.8.34 | Audit evidence protected | IMP-A.8.33-34.2 | Formula | Auto | Link |

#### Critical Findings Summary (Rows 57-70)

**Section Header (RED):** "CRITICAL FINDINGS REQUIRING IMMEDIATE ATTENTION"

| Domain | Critical Finding | Severity | Count | Assigned To | Target Date | Status |
|--------|------------------|----------|-------|-------------|-------------|--------|
| Test Data | Unauthorized data in test | Critical | Formula | [User] | [User] | ✅/⚠️/❌ |
| Test Data | Unmasked PII | Critical | Formula | [User] | [User] | ✅/⚠️/❌ |
| Audit | Unauthorized audit activity | Critical | Formula | [User] | [User] | ✅/⚠️/❌ |
| Audit | Unauthorized tools | Critical | Formula | [User] | [User] | ✅/⚠️/❌ |
| Audit | Access not revoked | Critical | Formula | [User] | [User] | ✅/⚠️/❌ |

**Column Widths:**
- A: 25, B: 15, C: 12, D: 12, E: 20, F: 12, G: 12

---

### Sheet 2: Test_Data_Compliance

#### Header Section
**Row 1:** "TEST DATA PROTECTION COMPLIANCE"
**Row 2:** "Detailed compliance status from IMP-A.8.33-34.1 Assessment"

#### Test Data Inventory Summary (Rows 4-20)

**Section Header:** "TEST DATA INVENTORY COMPLIANCE"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Data Sets | - | Formula from A.8.33-34.1 | - | - |
| Authorized Data Sets | 100% | Formula | ✅/⚠️/❌ | - |
| Pending Authorization | 0 | Formula | ✅/⚠️/❌ | - |
| Unauthorized Data Sets | 0 | Formula | ✅/⚠️/❌ | Critical if >0 |
| Data Sets with PII | - | Formula | - | - |
| PII Data Sets Masked | 100% | Formula | ✅/⚠️/❌ | - |
| Authorization Rate % | 100% | Formula | ✅/⚠️/❌ | - |

#### Masking Effectiveness Summary (Rows 22-35)

**Section Header:** "DATA MASKING EFFECTIVENESS"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Average Effectiveness Score | ≥4.0 | Formula | ✅/⚠️/❌ | - |
| Score 5 (Excellent) | - | Formula | - | - |
| Score 4 (Good) | - | Formula | - | - |
| Score 3 (Adequate) | - | Formula | - | - |
| Score 2 (Poor) | - | Formula | ⚠️ if >0 | - |
| Score 1 (Inadequate) | - | Formula | ❌ if >0 | - |
| High Re-identification Risk | 0 | Formula | ✅/⚠️/❌ | Critical if >0 |
| Critical Masking Gaps | 0 | Formula | ✅/⚠️/❌ | Critical if >0 |

#### Environment Security Summary (Rows 37-50)

**Section Header:** "TEST ENVIRONMENT SECURITY"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Environments | - | Formula | - | - |
| Security Compliant | 100% | Formula | ✅/⚠️/❌ | - |
| Security Partial | 0% | Formula | ⚠️ if >0 | - |
| Security Non-Compliant | 0 | Formula | ❌ if >0 | - |
| Full Network Isolation | ≥90% | Formula | ✅/⚠️/❌ | - |
| Encryption at Rest | 100% | Formula | ✅/⚠️/❌ | - |
| Reviews Overdue | 0 | Formula | ❌ if >0 | - |

#### Refresh Governance Summary (Rows 52-65)

**Section Header:** "DATA REFRESH GOVERNANCE"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Refresh Schedules | - | Formula | - | - |
| Authorized Refreshes | 100% | Formula | ✅/⚠️/❌ | - |
| Masking at Refresh | 100% | Formula | ✅/⚠️/❌ | - |
| Auto-Purge Enabled | 100% | Formula | ✅/⚠️/❌ | - |

---

### Sheet 3: Audit_Activity_Compliance

#### Header Section
**Row 1:** "AUDIT ACTIVITY MANAGEMENT COMPLIANCE"
**Row 2:** "Detailed compliance status from IMP-A.8.33-34.2 Assessment"

#### Audit Activity Summary (Rows 4-20)

**Section Header:** "AUDIT ACTIVITY AUTHORIZATION"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Audits | - | Formula from A.8.33-34.2 | - | - |
| Approved Audits | 100% | Formula | ✅/⚠️/❌ | - |
| Pending Approval | 0 | Formula | ⚠️ if >0 | - |
| Completed Audits | - | Formula | - | - |
| Total Findings | - | Formula | - | - |
| Critical Findings | 0 | Formula | ❌ if >0 | - |
| Open Follow-ups | - | Formula | - | Track progress |

#### Tool Authorization Summary (Rows 22-35)

**Section Header:** "AUDIT TOOL AUTHORIZATION"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Tools | - | Formula | - | - |
| Authorized Tools | 100% | Formula | ✅/⚠️/❌ | - |
| Pending Authorization | 0 | Formula | ⚠️ if >0 | - |
| Unauthorized Tools | 0 | Formula | ❌ if >0 | Critical |
| High Risk Tools | - | Formula | - | Monitor closely |
| Reviews Overdue | 0 | Formula | ❌ if >0 | - |
| Expired Licenses | 0 | Formula | ❌ if >0 | - |

#### Access Control Summary (Rows 37-55)

**Section Header:** "AUDITOR ACCESS CONTROL"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Total Access Grants | - | Formula | - | - |
| Active Access | - | Formula | - | Monitor |
| Approved Access | 100% | Formula | ✅/⚠️/❌ | - |
| Pending Approval | 0 | Formula | ⚠️ if >0 | - |
| Admin Access Count | Minimize | Formula | Monitor | High risk |
| Restricted Data Access | - | Formula | - | Monitor |
| NDA Coverage | 100% | Formula | ✅/⚠️/❌ | - |
| Access Logging | 100% | Formula | ✅/⚠️/❌ | - |
| MFA Required | 100% | Formula | ✅/⚠️/❌ | - |
| Overdue Revocations | 0 | Formula | ❌ if >0 | Critical |

#### Disruption Mitigation Summary (Rows 57-70)

**Section Header:** "DISRUPTION MITIGATION COVERAGE"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Critical Systems | - | Formula | - | - |
| With Mitigation Plans | 100% | Formula | ✅/⚠️/❌ | - |
| Rollback Tested (12 mo) | 100% | Formula | ✅/⚠️/❌ | - |
| Reviews Overdue | 0 | Formula | ❌ if >0 | - |

#### Evidence Protection Summary (Rows 72-85)

**Section Header:** "AUDIT EVIDENCE PROTECTION"

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Evidence Categories | - | Formula | - | - |
| Encryption at Rest | 100% | Formula | ✅/⚠️/❌ | - |
| Encryption in Transit | 100% | Formula | ✅/⚠️/❌ | - |
| Access Reviews Current | 100% | Formula | ✅/⚠️/❌ | - |

---

### Sheet 4: Gap_Analysis

#### Header Section
**Row 1:** "CONSOLIDATED GAP ANALYSIS"
**Row 2:** "Gaps identified across all Testing and Audit Protection assessments"

#### Test Data Protection Gaps (Rows 4-50)

**Section Header:** "TEST DATA PROTECTION GAPS (IMP-A.8.33-34.1)"

| Gap ID | Gap Description | Area | Severity | Current State | Target State | Owner | Target Date | Status | Evidence |
|--------|-----------------|------|----------|---------------|--------------|-------|-------------|--------|----------|
| Formula: Auto-populate from A.8.33-34.1 | Formula | Text | Formula | Formula | Text | Text | Date | Formula | Text |

**[50 rows - Reference gaps from ISMS-IMP-A.8.33-34.1.xlsx]**

#### Audit Activity Management Gaps (Rows 52-100)

**Section Header:** "AUDIT ACTIVITY MANAGEMENT GAPS (IMP-A.8.33-34.2)"

| Gap ID | Gap Description | Area | Severity | Current State | Target State | Owner | Target Date | Status | Evidence |
|--------|-----------------|------|----------|---------------|--------------|-------|-------------|--------|----------|
| Formula: Auto-populate from A.8.33-34.2 | Formula | Text | Formula | Formula | Text | Text | Date | Formula | Text |

**[50 rows - Reference gaps from ISMS-IMP-A.8.33-34.2.xlsx]**

#### Gap Statistics (Rows 102-120)

**Section Header:** "GAP ANALYSIS STATISTICS"

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Gaps Identified | Formula | 100% |
| Critical Priority | Formula | % |
| High Priority | Formula | % |
| Medium Priority | Formula | % |
| Low Priority | Formula | % |
| Status - Open | Formula | % |
| Status - In Progress | Formula | % |
| Status - Closed | Formula | % |
| Overdue Gaps | Formula | % |

---

### Sheet 5: Exception_Register

#### Header Section
**Row 1:** "EXCEPTION REGISTER"
**Row 2:** "Approved exceptions to testing and audit protection requirements"

#### Column Specification (Row 4 headers, data starts Row 5)

| Column | Header | Width | Data Type | Validation | Description |
|--------|--------|-------|-----------|------------|-------------|
| A | Exception ID | 12 | Text | Auto-generated | EXC-001, EXC-002, etc. |
| B | Exception Title | 35 | Text | Required | Brief description |
| C | Policy Requirement | 35 | Text | Required | Requirement being excepted |
| D | Assessment Source | 25 | Dropdown | Required | IMP-A.8.33-34.1 or IMP-A.8.33-34.2 |
| E | Business Justification | 50 | Text | Required | Why exception needed |
| F | Risk Assessment | 40 | Text | Required | Impact of exception |
| G | Compensating Controls | 50 | Text | Required | Alternative controls |
| H | Requested By | 25 | Text | Required | Who requested |
| I | Request Date | 12 | Date | Required | DD.MM.YYYY |
| J | Approval Status | 18 | Dropdown | Required | Approved, Pending, Denied, Expired |
| K | Approved By | 25 | Text | If J=Approved | Approver |
| L | Approval Date | 12 | Date | If J=Approved | DD.MM.YYYY |
| M | Expiration Date | 12 | Date | Required | DD.MM.YYYY |
| N | Renewal Required | 12 | Dropdown | Formula | Yes/No based on expiration |
| O | Risk Level | 15 | Dropdown | Required | High, Medium, Low |
| P | Risk Owner | 25 | Text | Required | Who accepts risk |
| Q | Review Date | 12 | Date | Required | Last review DD.MM.YYYY |
| R | Next Review | 12 | Date | Formula | =Q+90 |
| S | Evidence Reference | 20 | Text | Required | Documentation link |
| T | Notes | 40 | Text | Optional | Additional info |

**Data Rows:** 30 rows (5-34)

#### Exception Statistics (Rows 36-50)

| Metric | Formula | Target |
|--------|---------|--------|
| Total Exceptions | =COUNTA(B5:B34) | Minimize |
| Approved Exceptions | =COUNTIF(J5:J34,"Approved") | - |
| Pending Exceptions | =COUNTIF(J5:J34,"Pending") | 0 |
| Expired Exceptions | =COUNTIF(J5:J34,"Expired") | 0 |
| High Risk Exceptions | =COUNTIF(O5:O34,"High") | 0 |
| Expiring in 30 Days | =COUNTIFS(M5:M34,"<="&TODAY()+30,J5:J34,"Approved") | Monitor |
| Overdue Reviews | =COUNTIF(R5:R34,"<"&TODAY()) | 0 |

---

### Sheet 6: KPIs_and_Metrics

#### Header Section
**Row 1:** "KEY PERFORMANCE INDICATORS & METRICS"
**Row 2:** "Detailed tracking with historical trends"

#### Test Data KPIs (Rows 4-20)

**Section Header:** "TEST DATA PROTECTION KPIs"

| KPI | Target | Q1 | Q2 | Q3 | Q4 | Current | Status | Trend |
|-----|--------|----|----|----|----|---------|--------|-------|
| Data Set Authorization Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| PII Masking Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Average Masking Effectiveness | ≥4.0 | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Environment Security Compliance | ≥90% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Refresh Authorization Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| High Re-identification Risk Count | 0 | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |

#### Audit Activity KPIs (Rows 22-40)

**Section Header:** "AUDIT ACTIVITY MANAGEMENT KPIs"

| KPI | Target | Q1 | Q2 | Q3 | Q4 | Current | Status | Trend |
|-----|--------|----|----|----|----|---------|--------|-------|
| Audit Authorization Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Tool Authorization Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Access Approval Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Access Revocation Timeliness | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| NDA Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Access Logging Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| MFA Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Critical System Mitigation Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Evidence Encryption Rate | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Audit Follow-up Closure Rate | ≥90% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |

#### Combined KPIs (Rows 42-55)

**Section Header:** "COMBINED COMPLIANCE KPIs"

| KPI | Target | Q1 | Q2 | Q3 | Q4 | Current | Status | Trend |
|-----|--------|----|----|----|----|---------|--------|-------|
| Overall Compliance Rate | ≥85% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Critical Gaps Open | 0 | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| High Gaps Open | 0 | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Evidence Coverage | 100% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |
| Exception Count | Minimize | [User] | [User] | [User] | [User] | Formula | Monitor | ↑/→/↓ |
| Audit Readiness Score | ≥85% | [User] | [User] | [User] | [User] | Formula | ✅/⚠️/❌ | ↑/→/↓ |

---

### Sheet 7: Remediation_Roadmap

#### Header Section
**Row 1:** "REMEDIATION ROADMAP"
**Row 2:** "Structured plan to address identified gaps"

#### Timeline Overview (Rows 4-10)

| Phase | Timeline | Focus Areas | Expected Outcome |
|-------|----------|-------------|------------------|
| Phase 1 - Critical (0-30 days) | [User Input] | Critical gaps | All critical gaps closed |
| Phase 2 - High Priority (31-90 days) | [User Input] | High priority gaps | Major risks mitigated |
| Phase 3 - Medium Priority (91-180 days) | [User Input] | Medium priority gaps | Full compliance achieved |
| Phase 4 - Continuous Improvement (Ongoing) | [User Input] | Low priority and enhancements | Best practice adoption |

#### Remediation Actions (Rows 12-70)

| Action ID | Description | Priority | Source | Owner | Start | Target | Status | Progress | Dependencies | Notes |
|-----------|-------------|----------|--------|-------|-------|--------|--------|----------|--------------|-------|
| RA-001 | Text | Critical/High/Medium/Low | IMP-A.8.33-34.X | Text | Date | Date | ✅/⚠️/❌/📋 | 0-100% | Text | Text |

**[60 rows for remediation actions]**

#### Progress Summary (Rows 72-85)

| Metric | Count | Percentage | Target | Status |
|--------|-------|------------|--------|--------|
| Total Actions | Formula | 100% | N/A | - |
| Completed | Formula | % | Text | Auto |
| In Progress | Formula | % | Text | Auto |
| Not Started | Formula | % | Text | Auto |
| Overdue | Formula | % | <10% | Auto |
| Critical Remaining | Formula | % | 0% | Auto |
| Average Progress | Formula | N/A | ≥70% | Auto |

---

### Sheet 8: Evidence_Consolidation

#### Header Section
**Row 1:** "CONSOLIDATED EVIDENCE REGISTER"
**Row 2:** "Evidence from both Testing and Audit Protection assessments (200 entries)"

#### Evidence Inventory (Rows 4-203)

**Structure:**
- Rows 5-104: Evidence from IMP-A.8.33-34.1 (100 entries)
- Rows 105-204: Evidence from IMP-A.8.33-34.2 (100 entries)

| Evidence ID | Source Assessment | Evidence Type | Description | Location | Date Collected | Collected By | Verification Status | Auditor Notes |
|-------------|-------------------|---------------|-------------|----------|----------------|--------------|-------------------|---------------|
| Formula from A.8.33-34.1 | IMP-A.8.33-34.1 | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

#### Evidence Statistics (Rows 206-220)

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Evidence | Formula | 100% |
| From Test Data Assessment | Formula | % |
| From Audit Assessment | Formula | % |
| Verified | Formula | % |
| Pending Verification | Formula | % |
| Evidence by Type - Policy | Formula | % |
| Evidence by Type - Technical | Formula | % |
| Evidence by Type - Authorization | Formula | % |
| Evidence by Type - Other | Formula | % |

---

### Sheet 9: CISO_Certification

#### Header Section
**Row 1:** "CISO COMPLIANCE CERTIFICATION"
**Row 2:** "Formal attestation of Testing and Audit Protection compliance status"

#### Certification Summary (Rows 4-18)
```
CERTIFICATION SUMMARY

Dashboard Document:        ISMS-IMP-A.8.33-34.3 - Compliance Dashboard
Certification Period:      [USER INPUT]
Overall Compliance Rate:   [Formula from Executive_Dashboard]
Critical Gaps:             [Formula]
High Gaps:                 [Formula]
Active Exceptions:         [Formula]
Assessment 1 Status:       [Formula from A.8.33-34.1]
Assessment 2 Status:       [Formula from A.8.33-34.2]
Total Evidence:            [Formula]
Audit Readiness:           [Formula based on compliance]
Certification Status:      [Dropdown: ✅ Certified/⚠️ Certified with Conditions/❌ Not Certified]
```

#### CISO Attestation (Rows 20-40)
```
CISO ATTESTATION

I, _________________________________ (CISO Name), certify that:

1. Assessment Accuracy
   [ ] I have reviewed the source assessments (IMP-A.8.33-34.1 and IMP-A.8.33-34.2)
   [ ] I confirm the data in this dashboard accurately reflects our compliance status
   [ ] Assessment methodologies are appropriate and consistently applied

2. Gap Understanding
   [ ] I understand all identified gaps and their business impact
   [ ] Critical gaps have approved remediation plans with adequate resources
   [ ] High-priority gaps are being actively addressed

3. Exception Acceptance
   [ ] I have reviewed all active exceptions
   [ ] I accept the residual risk associated with each exception
   [ ] Compensating controls are adequate and monitored

4. Risk Acceptance
   [ ] I accept the residual risk documented in this assessment
   [ ] Risk levels are within organizational risk appetite
   [ ] Additional risk treatment is not required at this time

5. Audit Readiness
   [ ] The organization is/is not ready for ISO 27001 audit of Controls A.8.33-34
   [ ] Evidence is complete and accessible
   [ ] Personnel are prepared for audit interviews

Certification Decision:     [Dropdown: ✅ Certified/⚠️ Certified with Conditions/❌ Not Certified]

Conditions (if applicable): [Text area - merged cells]
_____________________________________________________________

CISO Signature:            _________________________________
Date:                      [USER INPUT - DD.MM.YYYY]

Certification Valid Until: [Formula: Date + 90 days]
Next Certification Due:    [Formula: Date + 90 days]
```

#### Certification History (Rows 42-55)

| Certification ID | Date | CISO | Status | Overall Compliance | Critical Gaps | Conditions | Valid Until |
|-----------------|------|------|--------|-------------------|---------------|------------|-------------|
| CERT-001 | [User] | [User] | [User] | [User] | [User] | [User] | [User] |

**[10 rows for certification history]**

---

### Sheet 10: Approval_Sign_Off

#### Header Section
**Row 1:** "DASHBOARD APPROVAL & SIGN-OFF"
**Row 2:** "Executive approval workflow for compliance dashboard"

#### Dashboard Summary (Rows 4-18)
```
DASHBOARD SUMMARY

Document ID:              ISMS-IMP-A.8.33-34.3
Report Type:              Compliance Summary Dashboard
Reporting Period:         [USER INPUT]
Overall Compliance:       [Formula]
Test Data Compliance:     [Formula]
Audit Activity Compliance:[Formula]
Critical Findings:        [Formula]
Active Exceptions:        [Formula]
Evidence Entries:         [Formula]
Dashboard Status:         [Dropdown: ✅ Final/⚠️ Requires Action/📋 Draft]
```

#### Prepared By (Rows 20-28)
```
PREPARED BY

Name:               [USER INPUT]
Role/Title:         [USER INPUT]
Department:         [USER INPUT]
Email:              [USER INPUT]
Date Prepared:      [USER INPUT - DD.MM.YYYY]
Signature:          [USER INPUT]
```

#### Reviewed By (Rows 30-40)
```
REVIEWED BY

Name:                   [USER INPUT]
Role/Title:             Security Manager / Compliance Officer
Review Date:            [USER INPUT - DD.MM.YYYY]
Review Notes:           [Text area]
Data Accuracy:          [Dropdown: ✅ Confirmed/⚠️ Minor Issues/❌ Major Issues]
Recommendation:         [Dropdown: ✅ Approve/⚠️ Approve with Conditions/❌ Reject]
Conditions:            [Text area]
Signature:              [USER INPUT]
```

#### Approved By - Executive (Rows 42-52)
```
APPROVED BY - EXECUTIVE

Name:                   [USER INPUT]
Role/Title:             CISO / CRO / CEO
Approval Date:          [USER INPUT - DD.MM.YYYY]
Approval Decision:      [Dropdown: ✅ Approved/⚠️ Approved with Conditions/❌ Rejected]
Conditions/Notes:       [Text area]
Signature:              [USER INPUT]
```

#### Next Review (Rows 54-60)
```
NEXT REVIEW

Next Review Date:       [Formula: Approval Date + 90 days]
Review Responsibility:  [USER INPUT]
Focus Areas:           [USER INPUT]
Distribution List:     [USER INPUT]
```

---

## External Workbook Reference Summary

### Reference Pattern

**Format for external references:**
```excel
='[Normalized-Filename.xlsx]SheetName'!CellRange
```

**Examples:**
```excel
='[ISMS-IMP-A.8.33-34.1.xlsx]Summary_Dashboard'!B5
='[ISMS-IMP-A.8.33-34.2.xlsx]Audit_Activity_Register'!K5:K54
=COUNTIF('[ISMS-IMP-A.8.33-34.1.xlsx]Test_Data_Inventory'!I5:I104,"Authorized")
```

### Key Reference Points by Source Workbook

**A.8.33-34.1 (Test Data Protection):**

- Summary_Dashboard: Compliance %, Status, Critical gaps
- Test_Data_Inventory: Authorization rates, PII counts
- Data_Masking_Assessment: Effectiveness scores, gaps
- Test_Environment_Registry: Security compliance
- Data_Refresh_Schedule: Authorization rates
- Evidence_Register: All 100 evidence entries

**A.8.33-34.2 (Audit Activity Management):**

- Summary_Dashboard: Compliance %, Status, Critical gaps
- Audit_Activity_Register: Authorization rates, findings
- Audit_Tool_Authorization: Tool compliance
- Audit_Access_Tracking: Access control metrics
- Disruption_Mitigation_Plans: Coverage metrics
- Audit_Evidence_Protection: Encryption rates
- Evidence_Register: All 100 evidence entries

---

## Integration & Usage Notes

### File Placement Requirements

1. **All 3 files in SAME directory:**
   - ISMS-IMP-A.8.33-34.1.xlsx (normalized)
   - ISMS-IMP-A.8.33-34.2.xlsx (normalized)
   - ISMS-IMP-A.8.33-34.3_Compliance_Dashboard_YYYYMMDD.xlsx (this dashboard)

2. **First Open Behavior:**
   - Excel prompts: "This workbook contains links to other data sources"
   - Click "Update" to pull current data from source workbooks
   - Click "Don't Update" to keep cached values

3. **Updating Data:**
   - Open dashboard - Excel prompts - Click "Update"
   - Or: Data tab - Edit Links - Update Values
   - Dashboard auto-refreshes with current assessment data

### Workflow Summary

**PHASE 1 - Assessment:**
1. Complete 2 assessment workbooks (Scripts 1-2 generate dated files)
2. Document test data, masking, environments, audit activities, tools, access
3. Document evidence, compliance status, gaps

**PHASE 2 - Normalization:**
4. Run `normalize_assessment_files_a833-34.py`
5. Creates normalized copies (no dates in filenames)
6. Generates audit manifest for traceability

**PHASE 3 - Dashboard:**
7. Generate this dashboard (Script 3)
8. Place dashboard in same directory as normalized files
9. Open dashboard - Update Links - Auto-populated with current data
10. Review Executive_Dashboard, Gap_Analysis, Exception_Register
11. Populate user-input fields (KPIs trends, historical data)
12. Obtain CISO certification
13. Obtain executive approval via Approval_Sign_Off

**PHASE 4 - Continuous Monitoring:**
14. Update source assessment workbooks as changes occur
15. Open dashboard - Update Links - See refreshed data
16. Track remediation progress
17. Quarterly reviews and recertifications

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
