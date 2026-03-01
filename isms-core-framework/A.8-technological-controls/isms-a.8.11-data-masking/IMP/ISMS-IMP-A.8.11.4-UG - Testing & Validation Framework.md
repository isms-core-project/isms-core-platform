<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.11.4-UG:framework:UG:a.8.11.4 -->
**ISMS-IMP-A.8.11.4-UG - Testing & Validation Framework**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Testing & Validation Framework |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.11.4-UG |
| **Related Policy** | ISMS-POL-A.8.11 (Data Masking) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.11 (Data Masking) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.11 (Data Masking)
- ISMS-IMP-A.8.11.1 (Data Inventory & Classification Assessment)
- ISMS-IMP-A.8.11.2 (Masking Technique Selection & Requirements)
- ISMS-IMP-A.8.11.3 (Environment Coverage Assessment)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Testing Procedures | Define and document masking test procedures |
| 3 | PreDeployment Tests | Pre-deployment masking verification tests |
| 4 | PostDeployment Validation | Post-deployment masking validation |
| 5 | Completeness Testing | Test masking completeness across data fields |
| 6 | Format Preservation | Verify masking preserves data format integrity |
| 7 | Referential Integrity | Test referential integrity after masking |
| 8 | ReIdentification Risk | Assess re-identification risk from masked data |
| 9 | Data Utility Validation | Validate masked data utility for intended use |
| 10 | Performance Testing | Assess masking performance impact |
| 11 | Ongoing Monitoring | Track ongoing masking effectiveness |
| 12 | Gap Analysis | Identify testing and validation gaps |
| 13 | Evidence Register | Store and reference evidence supporting assessments |
| 14 | Summary Dashboard | Compliance status and key metrics overview |
| 15 | Approval Sign-Off | Management review sign-off and certification |

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.11.4  
**Assessment Area:** Masking Effectiveness Testing & Validation  
**Related Policy:** ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) - Testing & Validation Requirements  
**Purpose:** Document and track testing procedures that verify data masking works effectively

**Scope:** This assessment evaluates:

- Pre-deployment masking tests
- Post-deployment validation procedures
- Completeness testing (100% field coverage)
- Re-identification risk assessment
- Data utility validation (applications still work)
- Performance impact measurement
- Schema drift detection
- Ongoing monitoring and continuous validation

**Assessment Philosophy:**

- **Test Everything:** Assume nothing - verify masking actually works
- **Quantify Risk:** Measure re-identification risk, don't just claim "it's masked"
- **Continuous Validation:** Masking degrades over time (schema changes, updates)
- **Evidence-Based:** Document test results, link to Evidence Register
- **No Cargo Cult:** Having a masking tool ≠ having effective masking

---

## Standard Column Structure

### Base Columns (A-Q, 17 columns) - Used across test sheets

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Test ID | 15 | Text | Free text (e.g., "TEST-001") |
| B | Test Name/Description | 30 | Text | Free text |
| C | Environment Tested | 20 | Dropdown | Production, Development, Testing, UAT, Analytics, Cloud, Other |
| D | Data Category Tested | 20 | Dropdown | PII, Financial, Health, Credentials, Proprietary, Mixed |
| E | Test Type | 20 | Dropdown | Pre-Deployment, Post-Deployment, Completeness, Re-ID, Utility, Performance |
| F | Test Date | 15 | Date | Date picker |
| G | Tester Name | 20 | Text | Free text |
| H | Test Method | 25 | Dropdown | Manual, Automated, Hybrid |
| I | Test Result | 18 | Dropdown | ✅ Pass, ❌ Fail, âš ï¸ Partial, Blocked, N/A |
| J | Pass Criteria | 30 | Text | Free text (what defines success) |
| K | Actual Outcome | 30 | Text | Free text (what actually happened) |
| L | Issues Found | 30 | Text | Free text (describe any failures) |
| M | Remediation Required? | 15 | Dropdown | Yes, No, N/A |
| N | Remediation Status | 18 | Dropdown | Not Started, In Progress, Completed, Blocked |
| O | Retest Date | 15 | Date | Date picker (if remediation needed) |
| P | Notes/Comments | 30 | Text | Free text |
| Q | Evidence ID | 15 | Text | Link to Evidence Register |

---

## Cell Styling Reference

### Header Styles

- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Centered
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Centered
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Centered

### Input Cell Styles

- **Fill:** FFFFCC (light yellow) - User must fill
- **Alignment:** Left for text, center for dropdowns, wrapped
- **Border:** Thin black on all sides

### Status Color Coding

- **Pass:** C6EFCE (light green)
- **Fail:** FFC7CE (light red)
- **Partial:** FFEB9C (light yellow)
- **Blocked:** D3D3D3 (light gray)

---

## Sheet 1: Instructions_Legend

### Header Section
**Title:** "ISMS Control A.8.11.4 - Testing & Validation Framework"  
**Subtitle:** "ISO/IEC 27001:2022 - Data Masking Effectiveness Verification"  
**Styling:** Dark blue header (003366), white text, centered, 40px height

### Document Information Block
```
Document ID:           ISMS-IMP-A.8.11.4
Assessment Area:       Masking Testing & Validation
Related Policy:        ISMS-POL-A.8.11, Section 2.4 (Testing and Validation)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organisation:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

### How to Use This Workbook (10 instructions)
1. Document ALL masking tests performed (pre-deployment, post-deployment, ongoing)
2. Complete Testing_Procedures sheet first to document your test methodology
3. For each masked environment, complete relevant test sheets
4. Record test results with Pass/Fail/Partial status
5. Calculate masking coverage % (target: 100% of sensitive fields)
6. Perform re-identification testing and document risk level
7. Validate data utility (applications still work with masked data)
8. Measure performance impact (target: <10% degradation)
9. Link all test results to Evidence Register
10. Review Summary Dashboard for overall testing compliance status

### Testing Philosophy
**Core Principles from Policy S2.4:**
1. 🎯 **Assume Nothing:** Just because masking is configured doesn't mean it works
2. 🔍 **Test Everything:** Every masking technique, every environment, every data flow
3. 🔄 **Validate Continuously:** Masking effectiveness degrades over time (schema changes, updates)
4. 📊 **Quantify Risk:** Don't just say "it's masked" — measure re-identification risk
5. 🚫 **No Cargo Cult:** Having a masking tool is not the same as having effective masking

### Testing Dimensions Table

| Dimension | Key Question | Success Criteria | Target |
|-----------|--------------|------------------|--------|
| Effectiveness | Is data actually masked? | Original data not visible | 100% fields masked |
| Completeness | Are ALL sensitive fields masked? | Coverage = 100% | 100% |
| Re-identification Risk | Can original data be inferred? | Re-ID attempts fail | 0% re-ID rate |
| Data Utility | Does masked data still work? | Apps function correctly | ≥95% utility |
| Performance | Does masking slow things down? | Acceptable impact | <10% degradation |

---

## Sheet 2: Testing_Procedures

### Header
**Title:** "TESTING PROCEDURES DOCUMENTATION"  
**Policy Reference:** "Testing procedures must be documented and followed consistently (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 3)"

### Assessment Question (Row 3)
**"Are formal testing procedures documented for validating masking effectiveness?"**

Response: [Dropdown: Yes / No / Partial / In Progress] (yellow cell B3)

### Column Headers (Row 6)

| Column | Header | Width |
|--------|--------|-------|
| A | Procedure ID | 15 |
| B | Procedure Name | 30 |
| C | Test Type | 20 |
| D | When Performed | 25 |
| E | Responsible Role | 20 |
| F | Test Method | 20 |
| G | Tools Used | 25 |
| H | Pass Criteria | 30 |
| I | Frequency | 15 |
| J | Documentation Required | 30 |
| K | Procedure Status | 18 |
| L | Last Updated | 15 |
| M | Notes | 30 |

### Data Entry Rows (8-27)

- **20 rows** for testing procedures
- Yellow-highlighted cells for user input

### Compliance Checklist (Starting Row 30)

**TESTING PROCEDURES CHECKLIST** (15 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Pre-deployment testing procedure documented | [Dropdown] | |
| ☐ | Post-deployment validation procedure documented | [Dropdown] | |
| ☐ | Completeness testing procedure documented | [Dropdown] | |
| ☐ | Re-identification testing procedure documented | [Dropdown] | |
| ☐ | Data utility validation procedure documented | [Dropdown] | |
| ☐ | Performance testing procedure documented | [Dropdown] | |
| ☐ | Schema drift detection procedure documented | [Dropdown] | |
| ☐ | Testing roles and responsibilities assigned | [Dropdown] | |
| ☐ | Testing tools identified and available | [Dropdown] | |
| ☐ | Pass/fail criteria defined for each test type | [Dropdown] | |
| ☐ | Test frequency specified (per deployment, monthly, quarterly) | [Dropdown] | |
| ☐ | Testing procedures reviewed annually | [Dropdown] | |
| ☐ | Test evidence retention requirements documented | [Dropdown] | |
| ☐ | Failed test escalation process defined | [Dropdown] | |
| ☐ | Continuous monitoring procedures in place | [Dropdown] | |

---

## Sheet 3: PreDeployment_Tests

### Header
**Title:** "PRE-DEPLOYMENT TESTING"  
**Policy Reference:** "Before deploying masked data, verify effectiveness through visual inspection, automated validation, and comparison testing (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 4.1)"

### Assessment Question (Row 3)
**"Are pre-deployment tests performed BEFORE masked data is deployed to target environments?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 22 columns (A-V)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Visual Inspection Done? | 15 | Dropdown | Yes, No, N/A |
| S | Automated Validation Done? | 15 | Dropdown | Yes, No, N/A |
| T | Comparison Test Done? | 15 | Dropdown | Yes, No, N/A |
| U | Sample Size Tested | 15 | Text | Free text (e.g., "1000 records") |
| V | Approval to Deploy? | 15 | Dropdown | Approved, Rejected, Pending |

### Data Entry Rows (8-37)

- **30 rows** for pre-deployment tests

### Compliance Checklist (Starting Row 40)

**PRE-DEPLOYMENT CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Visual inspection performed on sample masked records | [Dropdown] | |
| ☐ | No plaintext PII visible in masked data | [Dropdown] | |
| ☐ | Automated validation scripts executed | [Dropdown] | |
| ☐ | 100% of identified sensitive fields masked | [Dropdown] | |
| ☐ | No NULL values where masking expected | [Dropdown] | |
| ☐ | Format validation passed (emails, phones, dates, etc.) | [Dropdown] | |
| ☐ | Comparison test: NO matching values with production | [Dropdown] | |
| ☐ | Referential integrity preserved (if required) | [Dropdown] | |
| ☐ | Test results documented | [Dropdown] | |
| ☐ | Failed tests remediated before deployment | [Dropdown] | |
| ☐ | Approval obtained to deploy masked data | [Dropdown] | |
| ☐ | Deployment blocked if ANY test fails | [Dropdown] | |

---

## Sheet 4: PostDeployment_Validation

### Header
**Title:** "POST-DEPLOYMENT VALIDATION"  
**Policy Reference:** "After deploying masked data, immediate validation (within 24 hours) and periodic validation (monthly/quarterly) required (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 4.2)"

### Assessment Question (Row 3)
**"Is post-deployment validation performed to verify masking effectiveness in the target environment?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 22 columns (A-V)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Validation Timing | 18 | Dropdown | Immediate (<24h), Periodic (Monthly), Periodic (Quarterly), Ad-hoc |
| S | Schema Change Impact? | 15 | Dropdown | Yes, No, Unknown |
| T | User Feedback Reviewed? | 15 | Dropdown | Yes, No, N/A |
| U | Issues Reported by Users? | 15 | Dropdown | Yes, No, N/A |
| V | Next Validation Date | 15 | Date | Date picker |

### Data Entry Rows (8-37)

- **30 rows** for post-deployment validation

### Compliance Checklist (Starting Row 40)

**POST-DEPLOYMENT CHECKLIST** (10 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Immediate validation performed within 24 hours of deployment | [Dropdown] | |
| ☐ | Masking verified in target environment | [Dropdown] | |
| ☐ | Application functionality tested (if applicable) | [Dropdown] | |
| ☐ | User feedback reviewed for masking issues | [Dropdown] | |
| ☐ | No reports of visible PII from users | [Dropdown] | |
| ☐ | Periodic validation scheduled (monthly/quarterly) | [Dropdown] | |
| ☐ | Schema change impact assessed after every schema update | [Dropdown] | |
| ☐ | Monitoring logs reviewed for masking failures | [Dropdown] | |
| ☐ | Failed validations escalated to ISO | [Dropdown] | |
| ☐ | Re-testing performed after remediation | [Dropdown] | |

---

## Sheet 5: Completeness_Testing

### Header
**Title:** "COMPLETENESS TESTING & COVERAGE VALIDATION"  
**Policy Reference:** "100% of identified sensitive fields must be masked. Schema drift detection required. (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 5)"

### Assessment Question (Row 3)
**"Is masking completeness tested to ensure 100% of sensitive fields are masked?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Total Sensitive Fields | 15 | Number | Free text |
| S | Masked Fields Count | 15 | Number | Free text |
| T | Coverage % | 12 | Percentage | Calculated: (S/R)*100 |
| U | Unmasked Fields Found | 15 | Number | Free text |
| V | Schema Drift Detected? | 15 | Dropdown | Yes, No, N/A |
| W | New Columns Added? | 15 | Dropdown | Yes, No, N/A |
| X | Masking Rules Updated? | 15 | Dropdown | Yes, No, Pending, N/A |

### Data Entry Rows (8-37)

- **30 rows** for completeness testing

### Compliance Checklist (Starting Row 40)

**COMPLETENESS CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Sensitive fields inventory maintained | [Dropdown] | |
| ☐ | Coverage calculated: (Masked Fields / Total Sensitive Fields) × 100 | [Dropdown] | |
| ☐ | Coverage target: 100% (with documented exceptions only) | [Dropdown] | |
| ☐ | Schema comparison performed before every data refresh | [Dropdown] | |
| ☐ | New columns detected and assessed for sensitivity | [Dropdown] | |
| ☐ | Masking rules updated within 5 days for new sensitive columns | [Dropdown] | |
| ☐ | Re-testing performed after masking rule updates | [Dropdown] | |
| ☐ | Unmasked sensitive fields flagged for remediation | [Dropdown] | |
| ☐ | Coverage gaps escalated to Data Owner and ISO | [Dropdown] | |
| ☐ | Coverage metrics tracked over time | [Dropdown] | |
| ☐ | Automated schema drift detection in place | [Dropdown] | |
| ☐ | Coverage audit performed quarterly | [Dropdown] | |

---

## Sheet 6: Format_Preservation

### Header
**Title:** "FORMAT & TYPE PRESERVATION VALIDATION"  
**Policy Reference:** "Masked data must maintain correct format (email, phone, date, etc.) per validation requirements (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 7.3)"

### Assessment Question (Row 3)
**"Is format preservation validated to ensure masked data matches expected data types/formats?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 22 columns (A-V)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Field Data Type | 18 | Dropdown | Email, Phone, CC, SSN, Date, ZIP, Custom |
| S | Format Validation Method | 20 | Dropdown | Regex, Luhn, Date Parse, Custom Script |
| T | Expected Format | 25 | Text | Free text (e.g., "999-999-9999") |
| U | Format Pass Rate % | 12 | Percentage | Free text |
| V | Format Failures Count | 15 | Number | Free text |

### Data Entry Rows (8-37)

- **30 rows** for format validation tests

### Compliance Checklist (Starting Row 40)

**FORMAT PRESERVATION CHECKLIST** (10 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Email format validation: Masked emails match email regex | [Dropdown] | |
| ☐ | Phone format validation: Masked phones match phone format | [Dropdown] | |
| ☐ | Credit card format validation: Masked cards pass Luhn (if required) | [Dropdown] | |
| ☐ | Date format validation: Masked dates are valid dates | [Dropdown] | |
| ☐ | ZIP code format validation: Masked ZIPs are valid format | [Dropdown] | |
| ☐ | SSN format validation: Masked SSNs match SSN format | [Dropdown] | |
| ☐ | Custom format validation performed (domain-specific) | [Dropdown] | |
| ☐ | Format failures logged and remediated | [Dropdown] | |
| ☐ | Format pass rate target: ≥99% | [Dropdown] | |
| ☐ | Automated format validation scripts in place | [Dropdown] | |

---

## Sheet 7: Referential_Integrity

### Header
**Title:** "REFERENTIAL INTEGRITY TESTING"  
**Policy Reference:** "Foreign key constraints and data consistency must be preserved across related tables (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 7.2)"

### Assessment Question (Row 3)
**"Is referential integrity validated to ensure relationships preserved after masking?"**

Response: [Dropdown: Yes / No / Partial / N/A] (yellow cell B3)

### Column Headers (Row 6) - Extended to 22 columns (A-V)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Parent Table | 20 | Text | Free text |
| S | Child Table | 20 | Text | Free text |
| T | Foreign Key Field | 20 | Text | Free text |
| U | FK Violations Found | 15 | Number | Free text |
| V | Consistency Maintained? | 15 | Dropdown | Yes, No, Partial, N/A |

### Data Entry Rows (8-37)

- **30 rows** for referential integrity tests

### Compliance Checklist (Starting Row 40)

**REFERENTIAL INTEGRITY CHECKLIST** (8 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Foreign key constraints validated after masking | [Dropdown] | |
| ☐ | Related records can be joined correctly | [Dropdown] | |
| ☐ | Consistent masking across related tables (same ID → same masked value) | [Dropdown] | |
| ☐ | Database integrity checks executed | [Dropdown] | |
| ☐ | Zero foreign key violations | [Dropdown] | |
| ☐ | Orphaned records identified and remediated | [Dropdown] | |
| ☐ | Automated integrity validation scripts in place | [Dropdown] | |
| ☐ | Integrity failures block data deployment | [Dropdown] | |

---

## Sheet 8: ReIdentification_Risk

### Header
**Title:** "RE-IDENTIFICATION RISK ASSESSMENT"  
**Policy Reference:** "Re-identification testing must be performed to verify masked data cannot be re-identified. Target: 0% re-ID rate. (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 6)"

### Assessment Question (Row 3)
**"Is re-identification risk testing performed to verify masked data cannot be re-identified?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Re-ID Technique Used | 22 | Dropdown | Direct Matching, Quasi-ID Combo, Statistical, External Correlation |
| S | Re-ID Attempts | 15 | Number | Free text |
| T | Successful Re-IDs | 15 | Number | Free text |
| U | Re-ID Success Rate % | 12 | Percentage | Calculated: (T/S)*100 |
| V | Risk Level | 12 | Dropdown | Low (0%), Medium (1-5%), High (>5%) |
| W | K-Anonymity Value | 12 | Number | Free text (optional) |
| X | Mitigation Required? | 15 | Dropdown | Yes, No, N/A |

### Data Entry Rows (8-37)

- **30 rows** for re-identification tests

### Compliance Checklist (Starting Row 40)

**RE-IDENTIFICATION CHECKLIST** (15 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Direct matching test: No matches between masked and production | [Dropdown] | |
| ☐ | Quasi-identifier combination test performed | [Dropdown] | |
| ☐ | Statistical inference test performed | [Dropdown] | |
| ☐ | External data correlation test performed | [Dropdown] | |
| ☐ | Re-identification success rate calculated | [Dropdown] | |
| ☐ | Re-ID rate target: 0% (zero successful re-identifications) | [Dropdown] | |
| ☐ | If 1-5% re-ID rate: Mitigation applied (additional masking/aggregation) | [Dropdown] | |
| ☐ | If >5% re-ID rate: Immediate remediation (re-design masking) | [Dropdown] | |
| ☐ | K-anonymity assessment performed (optional but recommended) | [Dropdown] | |
| ☐ | K-anonymity value: k ≥ 5 (if applicable) | [Dropdown] | |
| ☐ | Quasi-identifiers documented | [Dropdown] | |
| ☐ | Re-ID test scenarios documented | [Dropdown] | |
| ☐ | Re-ID test results documented with evidence | [Dropdown] | |
| ☐ | High re-ID risk escalated to CISO and DPO | [Dropdown] | |
| ☐ | Re-ID testing performed quarterly | [Dropdown] | |

### Reference Table: Re-ID Risk Scoring (Starting Row 60)

| Re-identification Success Rate | Risk Level | Action Required |
|-------------------------------|------------|-----------------|
| 0% | Low | Acceptable - continue monitoring |
| 1-5% | Medium | Mitigate: Apply additional masking or aggregation |
| >5% | High | Remediate immediately: Re-design masking approach |

---

## Sheet 9: Data_Utility_Validation

### Header
**Title:** "DATA UTILITY VALIDATION"  
**Policy Reference:** "Masked data must support intended use cases. Target: ≥95% utility. (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 7)"

### Assessment Question (Row 3)
**"Is data utility validated to ensure applications/analytics work correctly with masked data?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Use Case Type | 22 | Dropdown | Application Testing, Analytics, ML/AI, Reporting, Training |
| S | Test Suite Executed? | 15 | Dropdown | Yes, No, N/A |
| T | Tests Passed Count | 12 | Number | Free text |
| U | Tests Failed Count | 12 | Number | Free text |
| V | Utility Score % | 12 | Percentage | Calculated: (T/(T+U))*100 |
| W | Expected Failures? | 15 | Dropdown | Yes (documented), No, N/A |
| X | Acceptable? | 15 | Dropdown | Yes (≥95%), No (<95%), N/A |

### Data Entry Rows (8-37)

- **30 rows** for utility validation tests

### Compliance Checklist (Starting Row 40)

**DATA UTILITY CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Application test suite executed with masked data | [Dropdown] | |
| ☐ | All critical tests pass (or expected failures documented) | [Dropdown] | |
| ☐ | Performance testing with masked data acceptable | [Dropdown] | |
| ☐ | UAT completed successfully with masked data | [Dropdown] | |
| ☐ | Training exercises work with masked data | [Dropdown] | |
| ☐ | Statistical analysis results comparable (±acceptable margin) | [Dropdown] | |
| ☐ | ML model accuracy acceptable when trained on masked data | [Dropdown] | |
| ☐ | Reports render correctly with masked data | [Dropdown] | |
| ☐ | Aggregations produce valid results | [Dropdown] | |
| ☐ | Utility score calculated: % of use cases that work correctly | [Dropdown] | |
| ☐ | Utility score target: ≥95% | [Dropdown] | |
| ☐ | Utility failures documented and remediated | [Dropdown] | |

---

## Sheet 10: Performance_Testing

### Header
**Title:** "PERFORMANCE IMPACT TESTING"  
**Policy Reference:** "Masking performance impact must be measured. Target: <10% degradation. (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 8)"

### Assessment Question (Row 3)
**"Is performance impact tested to ensure masking overhead is acceptable?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 24 columns (A-X)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Metric Type | 20 | Dropdown | Query Time, Data Load Time, Report Gen Time, API Response Time |
| S | Baseline (Unmasked) | 15 | Text | Free text (e.g., "2.5 sec") |
| T | With Masking | 15 | Text | Free text (e.g., "2.7 sec") |
| U | Performance Impact % | 12 | Percentage | Calculated |
| V | Acceptable? | 15 | Dropdown | Yes (<10%), No (≥10%), N/A |
| W | Optimization Needed? | 15 | Dropdown | Yes, No, N/A |
| X | Optimization Applied? | 15 | Dropdown | Yes, No, Pending, N/A |

### Data Entry Rows (8-37)

- **30 rows** for performance tests

### Compliance Checklist (Starting Row 40)

**PERFORMANCE CHECKLIST** (10 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Baseline performance measured (without masking) | [Dropdown] | |
| ☐ | Performance measured with masking enabled | [Dropdown] | |
| ☐ | Performance impact calculated: ((Masked - Baseline) / Baseline) × 100 | [Dropdown] | |
| ☐ | Performance impact target: <10% degradation | [Dropdown] | |
| ☐ | Query performance tested | [Dropdown] | |
| ☐ | Data load/refresh performance tested | [Dropdown] | |
| ☐ | Report generation performance tested | [Dropdown] | |
| ☐ | If impact ≥10%: Optimization strategies implemented | [Dropdown] | |
| ☐ | Performance re-tested after optimization | [Dropdown] | |
| ☐ | Performance metrics tracked over time | [Dropdown] | |

---

## Sheet 11: Ongoing_Monitoring

### Header
**Title:** "ONGOING MONITORING & CONTINUOUS VALIDATION"  
**Policy Reference:** "Continuous monitoring and periodic re-testing required to detect masking degradation (ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) Section 9)"

### Assessment Question (Row 3)
**"Is ongoing monitoring in place to continuously validate masking effectiveness?"**

Response: [Dropdown: Yes / No / Partial / Planned] (yellow cell B3)

### Column Headers (Row 6) - Extended to 22 columns (A-V)

Base columns A-Q, plus:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Monitoring Type | 20 | Dropdown | Automated, Manual, Hybrid |
| S | Monitoring Frequency | 15 | Dropdown | Real-time, Daily, Weekly, Monthly, Quarterly |
| T | Alert Configured? | 15 | Dropdown | Yes, No, N/A |
| U | Incidents Detected | 12 | Number | Free text |
| V | Incident Response Time | 15 | Text | Free text (e.g., "2 hours") |

### Data Entry Rows (8-37)

- **30 rows** for ongoing monitoring

### Compliance Checklist (Starting Row 40)

**ONGOING MONITORING CHECKLIST** (12 items)

| Item | Requirement | Status | Notes |
|------|-------------|--------|-------|
| ☐ | Automated monitoring enabled for masking failures | [Dropdown] | |
| ☐ | Alerts configured for masking rule violations | [Dropdown] | |
| ☐ | Monitoring logs reviewed regularly (daily/weekly) | [Dropdown] | |
| ☐ | Schema change alerts configured | [Dropdown] | |
| ☐ | Periodic re-testing scheduled (monthly/quarterly) | [Dropdown] | |
| ☐ | Re-testing performed after every data refresh | [Dropdown] | |
| ☐ | Re-testing performed after every schema change | [Dropdown] | |
| ☐ | Incident response time tracked (target: <24 hours) | [Dropdown] | |
| ☐ | Masking failures escalated to ISO | [Dropdown] | |
| ☐ | Root cause analysis performed for failures | [Dropdown] | |
| ☐ | Monitoring metrics tracked over time | [Dropdown] | |
| ☐ | Annual comprehensive masking audit performed | [Dropdown] | |

---

## Sheet 12: Gap_Analysis

### Header
**Title:** "TESTING GAP ANALYSIS & REMEDIATION PLAN"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 12 |
| B | Test Type | 20 |
| C | Gap Description | 35 |
| D | Current State | 25 |
| E | Target State | 25 |
| F | Risk Level | 12 |
| G | Impact | 25 |
| H | Remediation Action | 35 |
| I | Owner | 20 |
| J | Target Date | 15 |
| K | Status | 15 |
| L | Evidence ID | 15 |

### Data Entry Rows (5-44)

- **40 rows** for gap analysis

---

## Sheet 13: Evidence_Register

### Header
**Title:** "EVIDENCE REGISTER"  
**Subtitle:** "Supporting documentation for all testing and validation activities"

### Column Headers (Row 3)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 20 |
| C | Description | 35 |
| D | Related Test | 25 |
| E | Document Name/Link | 30 |
| F | Date Created | 15 |
| G | Owner | 20 |
| H | Retention Period | 15 |
| I | Location | 25 |
| J | Notes | 30 |

### Data Entry Rows (5-104)

- **100 rows** for evidence documentation

---

## Sheet 14: Summary_Dashboard

### Header
**Title:** "TESTING & VALIDATION - EXECUTIVE SUMMARY DASHBOARD"

### Section 1: Test Compliance Summary (Rows 3-12)

| Test Area | Total Tests | Passed | Failed | Partial | Blocked | Pass Rate % |
|-----------|-------------|--------|--------|---------|---------|-------------|
| Pre-Deployment Tests | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Post-Deployment Validation | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Completeness Testing | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Format Preservation | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Referential Integrity | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Re-Identification Risk | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Data Utility Validation | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| Performance Testing | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |
| **OVERALL TOTAL** | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] | [Formula] |

### Section 2: Key Performance Indicators (Starting Row 16)

| KPI | Current Value | Target | Status |
|-----|---------------|--------|--------|
| Masking Coverage % | [Formula] | 100% | [Conditional Format] |
| Re-Identification Risk Rate % | [Formula] | 0% | [Conditional Format] |
| Data Utility Score % | [Formula] | ≥95% | [Conditional Format] |
| Performance Impact % | [Formula] | <10% | [Conditional Format] |
| Pre-Deployment Test Pass Rate % | [Formula] | 100% | [Conditional Format] |
| Post-Deployment Validation Rate % | [Formula] | 100% | [Conditional Format] |
| Schema Drift Detection Rate | [Formula] | 100% | [Conditional Format] |
| Failed Tests Remediated % | [Formula] | 100% | [Conditional Format] |
| Testing Procedures Documented | [Formula] | 100% | [Conditional Format] |
| Evidence Documentation Rate % | [Formula] | 100% | [Conditional Format] |

### Section 3: Critical Test Failures (Starting Row 30)

| Priority | Test Type | Failure Description | Risk Level | Owner | Target Date | Status |
|----------|-----------|---------------------|------------|-------|-------------|--------|
| P1 | [Auto from Gap Analysis] | [Auto] | [Auto] | [Auto] | [Auto] | [Auto] |
| ... | ... | ... | ... | ... | ... | ... |

(Top 10 failures auto-populated)

### Section 4: Testing Trend Analysis (Starting Row 45)

| Month | Total Tests | Pass Rate % | Re-ID Risk % | Utility % | Performance Impact % |
|-------|-------------|-------------|--------------|-----------|---------------------|
| [Manual] | [Manual] | [Manual] | [Manual] | [Manual] | [Manual] |
| ... | ... | ... | ... | ... | ... |

(6-month trend tracking)

### Section 5: Overall Testing Score (Starting Row 55)

**Weighted Testing Compliance Score:**

- Pre-Deployment Testing (20%): [Formula]
- Completeness Coverage (20%): [Formula]
- Re-ID Risk (20%): [Formula]
- Data Utility (15%): [Formula]
- Performance Impact (10%): [Formula]
- Ongoing Monitoring (15%): [Formula]

**TOTAL SCORE: [Weighted Average Formula] / 100**

---

## Implementation Notes

### Python Generator Requirements

1. **Sheet Creation:** All 14 sheets with exact names
2. **Styling:** Consistent color scheme (dark blue headers, yellow input cells)
3. **Data Validation:** Dropdowns for all specified columns
4. **Formulas:** Summary Dashboard formulas linking to test sheets
5. **Freeze Panes:** Freeze at row 7 (assessment sheets), row 4 (dashboard)
6. **Row Counts:**

   - Testing Procedures: 20 rows
   - All test sheets: 30 rows each (8 sheets × 30 = 240 test entries)
   - Gap Analysis: 40 rows
   - Evidence Register: 100 rows

### Assessment Totals

- **Total checklist items:** ~106 items across all sheets
- **Test capacity:** 240+ test entries
- **Evidence tracking:** 100 evidence entries
- **Gap tracking:** 40 gap entries

---

**END OF SPECIFICATION**

---

**END OF USER GUIDE**

---

*"A masking technique untested is a masking technique unproven."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
