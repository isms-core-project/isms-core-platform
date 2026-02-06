**ISMS-IMP-A.5.32-33.S4-TG - Information Protection Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.32-33: Intellectual Property Rights & Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Monitoring for IP Rights and Records Protection |
| **Related Policy** | ISMS-POL-A.5.32-33 (Full Policy) |
| **Purpose** | Provide executive-level visibility into IP protection, records protection, and retention compliance |
| **Target Audience** | CISO, Legal Counsel, Records Manager, Executive Management, Internal Audit, Compliance Officers |
| **Assessment Type** | Executive Reporting & Compliance Monitoring |
| **Review Cycle** | Quarterly or After Significant Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Information Protection Compliance Dashboard | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.32-33.S4-UG.

---

# Technical Specification

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.S4_Information_Protection_Compliance_Dashboard_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_4_compliance_dashboard.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance | ~50 |
| 2 | Executive_Summary | High-level status | ~30 |
| 3 | Compliance_Metrics | KPIs and targets | 30+ |
| 4 | Control_Assessment | A.5.32-33 evaluation | 30+ |
| 5 | Maturity_Assessment | CMMI scoring | ~15 |
| 6 | Risk_Register | Current risks | 20+ |
| 7 | Remediation_Tracker | Gap closure | 30+ |
| 8 | Trend_Analysis | Period comparison | 20+ |
| 9 | Evidence_Register | Audit evidence | 30+ |
| 10 | Approval_SignOff | Formal approval | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 2: Executive_Summary

### Layout
- Row 1: Merged header
- Row 2: Merged subheader
- Rows 4-6: Assessment period and dates
- Rows 8-12: Overall status indicators
- Rows 14-18: Key achievements
- Rows 20-24: Key concerns

### Status Fields

| Cell | Field | Data Validation |
|------|-------|-----------------|
| B4 | Assessment Period | - |
| B5 | Review Date | Date |
| B6 | Next Review Date | Date |
| B9 | Overall Status | List: Compliant, Partial, Non-Compliant |
| B10 | IP Protection Status | List: Effective, Partial, Ineffective |
| B11 | Records Protection Status | List: Effective, Partial, Ineffective |
| B12 | Retention Compliance Status | List: Compliant, At Risk, Non-Compliant |

## Sheet 3: Compliance_Metrics

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Metric ID | 12 | - |
| B | Category | 15 | List: IP Protection, Records Protection, Retention/Disposal |
| C | Metric Name | 30 | - |
| D | Description | 40 | - |
| E | Target | 12 | - |
| F | Current Value | 12 | - |
| G | Previous Value | 15 | - |
| H | Trend | 12 | List: Improving, Stable, Declining, New |
| I | Status | 15 | List: On Target, At Risk, Below Target |
| J | Owner | 20 | - |
| K | Notes | 30 | - |

### Conditional Formatting
- Status "On Target": Green fill (#C6EFCE)
- Status "At Risk": Yellow fill (#FFEB9C)
- Status "Below Target": Red fill (#FFC7CE)

## Sheet 4: Control_Assessment

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Control | 12 | - |
| B | Requirement | 40 | - |
| C | Implementation | 35 | - |
| D | Evidence | 30 | - |
| E | Gap | 30 | - |
| F | Score | 12 | List: 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| G | Status | 15 | List: Compliant, Partial, Non-Compliant |

## Sheet 5: Maturity_Assessment

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Domain | 30 | - |
| B | Current Level | 18 | List: 5 - Optimised, 4 - Managed, 3 - Defined, 2 - Developing, 1 - Initial, 0 - Non-existent |
| C | Target Level | 18 | Same as B |
| D | Gap | 8 | Number |
| E | Priority | 12 | List: Critical, High, Medium, Low |
| F | Key Actions | 40 | - |
| G | Notes | 30 | - |

## Sheet 6: Risk_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Risk ID | 12 | - |
| B | Risk Description | 40 | - |
| C | Risk Category | 15 | List: IP Protection, Records Protection, Compliance |
| D | Likelihood | 18 | List: 5 - Almost Certain, 4 - Likely, 3 - Possible, 2 - Unlikely, 1 - Rare |
| E | Impact | 18 | List: 5 - Catastrophic, 4 - Major, 3 - Moderate, 2 - Minor, 1 - Insignificant |
| F | Risk Score | 12 | Formula |
| G | Current Mitigation | 35 | - |
| H | Residual Risk | 12 | List: High, Medium, Low |
| I | Owner | 20 | - |
| J | Status | 15 | List: Open, Mitigated, Accepted, Transferred |
| K | Review Date | 12 | Date |

### Formulas
- Column F (Risk Score): `=VALUE(LEFT(D[row],1))*VALUE(LEFT(E[row],1))`

## Sheet 7: Remediation_Tracker

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Action ID | 12 | - |
| B | Source | 20 | List: A.5.32-33.1, A.5.32-33.2, A.5.32-33.3, Risk Assessment, Audit Finding |
| C | Description | 45 | - |
| D | Priority | 12 | List: Critical, High, Medium, Low |
| E | Owner | 20 | - |
| F | Due Date | 12 | Date |
| G | Progress | 12 | List: 0%, 25%, 50%, 75%, 100% |
| H | Status | 15 | List: Open, In Progress, Complete, Overdue, On Hold |
| I | Blocker | 25 | - |
| J | Notes | 25 | - |

### Conditional Formatting
- Status "Complete": Green fill (#C6EFCE)
- Status "In Progress": Yellow fill (#FFEB9C)
- Status "Overdue": Red fill (#FFC7CE)

## Sheet 8: Trend_Analysis

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Metric | 30 | - |
| B | Q1 | 10 | - |
| C | Q2 | 10 | - |
| D | Q3 | 10 | - |
| E | Q4 | 10 | - |
| F | YoY Change | 12 | - |
| G | Trend | 12 | List: Improving, Stable, Declining |
| H | Target | 10 | - |
| I | On Track | 10 | List: Yes, No, At Risk |

## Sheet 9: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Evidence ID | 12 | - |
| B | Description | 40 | - |
| C | Evidence Type | 18 | List: Assessment, Report, Metrics, Approval, Other |
| D | Related Item | 20 | - |
| E | Storage Location | 35 | - |
| F | Collected Date | 12 | Date |
| G | Collected By | 20 | - |
| H | Verification Status | 18 | List: Verified, Pending, Expired |

## Sheet 10: Approval_SignOff

### Approver Roles
1. Chief Information Security Officer
2. Legal Counsel
3. Records Manager
4. Compliance Officer
5. Internal Audit Representative
6. Executive Management Representative

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | Usage |
|------------|----------|-------|
| Header Fill | #1F4E79 | Sheet headers |
| Subheader Fill | #2E75B6 | Secondary headers |
| Column Header | #D6DCE4 | Table headers |
| Input Cell | #FFFFCC | User input |
| Good/Compliant | #C6EFCE | Positive status |
| Warning/At Risk | #FFEB9C | Attention needed |
| Bad/Non-Compliant | #FFC7CE | Negative status |
| High Risk | #FF6B6B | High priority |
| Medium Risk | #FFA94D | Medium priority |
| Low Risk | #69DB7C | Low priority |

---

# Integration Points

## Source Assessments

| Assessment | Metrics Provided |
|------------|------------------|
| A.5.32-33.1 | IP asset count, protection status, third-party compliance, license compliance |
| A.5.32-33.2 | Records count, protection effectiveness, integrity results, access control status |
| A.5.32-33.3 | Retention compliance, disposal completion, exception count |

## Related ISMS Controls

| Control | Relationship |
|---------|--------------|
| A.5.12-13 | Classification scheme alignment |
| A.5.34 | Privacy requirements for records |
| A.8.10 | Secure deletion alignment |
| A.8.12 | DLP for IP protection |
| A.8.13 | Backup for records availability |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
-- Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
