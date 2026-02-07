**ISMS-IMP-A.8.2-3-5.S6-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2, A.8.3, A.8.5: Authentication & Privileged Access

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S6-TG |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S6-UG.

---

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
