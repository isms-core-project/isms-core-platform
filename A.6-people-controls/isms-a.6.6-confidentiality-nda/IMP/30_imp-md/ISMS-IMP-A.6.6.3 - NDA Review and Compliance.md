# ISMS-IMP-A.6.6.3 — NDA Review and Compliance

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.3 |
| **Title** | NDA Review and Compliance |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook enables periodic review of NDA adequacy and compliance, ensuring NDAs remain current, appropriate, and properly executed as required by ISO 27001:2022.

**Scope**

- Periodic review scheduling and tracking
- Template adequacy assessment
- Coverage analysis (who should have NDAs vs. who does)
- Compliance verification
- Gap identification and remediation

**Control Requirements**

ISO 27001:2022 Control A.6.6 requires NDAs be "regularly reviewed."

### Prerequisites

- [ ] Completed ISMS-IMP-A.6.6.1 (Template Registry)
- [ ] Completed ISMS-IMP-A.6.6.2 (Execution Tracking)
- [ ] HR headcount data by category
- [ ] Vendor/contractor lists

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance | Review before starting |
| Periodic_Review | Review scheduling | Track review activities |
| Template_Adequacy | Template assessment | Assess template sufficiency |
| Coverage_Analysis | Coverage verification | Verify all required have NDAs |
| Compliance_Check | NDA compliance | Verify currency and appropriateness |
| Gap_Register | Gap tracking | Document gaps |
| Evidence_Register | Evidence tracking | Link evidence |
| Approval_SignOff | Authorisation | Obtain approvals |

### Completion Walkthrough

**Step 1: Periodic_Review Sheet**

Schedule and track reviews:

1. **Review_ID** - Unique identifier
2. **Review_Type** - Annual Full/Quarterly Check/Triggered
3. **Review_Scope** - What is being reviewed
4. **Planned_Date** - Target date
5. **Actual_Date** - When completed
6. **Reviewer** - Who conducted review
7. **Findings_Count** - Number of findings
8. **Gaps_Identified** - Number of gaps
9. **Status** - Scheduled/In Progress/Completed
10. **Next_Review** - Next scheduled review

**Review Frequency**:

| Review Type | Frequency |
|-------------|-----------|
| Annual Full Review | Once per year |
| Quarterly Check | Every 3 months |
| Template Update Review | When templates change |
| Triggered Review | After incidents or regulatory changes |

**Step 2: Template_Adequacy Sheet**

Assess template sufficiency:

1. **Template_ID** - Link to registry
2. **Template_Name** - Template name
3. **Last_Legal_Review** - Date of last review
4. **Regulatory_Current** - Meets current regulations
5. **Covers_All_Info_Types** - Covers all classifications
6. **Post_Term_Adequate** - Post-termination periods adequate
7. **Remedies_Adequate** - Breach remedies included
8. **Jurisdiction_Correct** - Correct governing law
9. **Overall_Adequacy** - Overall assessment
10. **Action_Required** - If any updates needed

**Step 3: Coverage_Analysis Sheet**

Verify NDA coverage:

1. **Stakeholder_Category** - Employee/Contractor/Vendor/etc.
2. **Total_Count** - Total persons in category
3. **NDA_Required** - How many require NDA
4. **NDA_Signed** - How many have signed
5. **Coverage_Rate** - Percentage covered
6. **Expired_NDAs** - How many expired
7. **Missing_NDAs** - Gap count
8. **Gap_Status** - No Gap/Gap Identified/Remediation In Progress
9. **Remediation_Owner** - Who is fixing gaps

**Coverage Targets**:

| Category | Target |
|----------|--------|
| Employees | 100% |
| Contractors | 100% |
| Vendors with data access | 100% |
| Partners | 100% |
| Visitors (sensitive) | 100% |

**Step 4: Compliance_Check Sheet**

Verify individual NDA compliance:

1. **NDA_ID** - Link to execution tracking
2. **Counterparty** - Party name
3. **Correctly_Executed** - Properly signed
4. **Within_Validity** - Not expired
5. **Appropriate_Template** - Right template used
6. **All_Parties_Signed** - All required signatures
7. **Securely_Stored** - Properly stored
8. **Overall_Compliance** - Compliant/Partial/Non-Compliant
9. **Issues_Found** - Any problems
10. **Action_Required** - Remediation needed

**Step 5: Gap_Register Sheet**

Track identified gaps:

1. **Gap_ID** - Unique identifier
2. **Gap_Type** - Missing/Expired/Inadequate/etc.
3. **Description** - Gap details
4. **Affected_Area** - Who/what affected
5. **Severity** - Critical/High/Medium/Low
6. **Identified_Date** - When found
7. **Owner** - Who is responsible
8. **Remediation_Action** - What to do
9. **Target_Date** - When to fix by
10. **Status** - Open/In Progress/Remediated/Verified

**Gap Severity**:

| Severity | Definition | Target Resolution |
|----------|------------|-------------------|
| Critical | Person with access has no NDA | 5 days |
| High | NDA expired, relationship ongoing | 30 days |
| Medium | Wrong template used | 60 days |
| Low | Minor clause missing | 90 days |

### Evidence Collection

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Review Reports | Completed review documentation | ISMS Evidence Library |
| Coverage Analysis | Analysis spreadsheets/reports | ISMS Evidence Library |
| Gap Remediation | Evidence of gap closure | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Reviews not conducted regularly
✅ **CORRECT**: Annual full review plus quarterly checks

❌ **MISTAKE**: Coverage analysis against outdated headcount
✅ **CORRECT**: Use current HR/vendor data

❌ **MISTAKE**: Gaps identified but not remediated
✅ **CORRECT**: Track all gaps to verified closure

❌ **MISTAKE**: Template review without legal involvement
✅ **CORRECT**: Legal Counsel reviews template adequacy

❌ **MISTAKE**: No ownership of gaps
✅ **CORRECT**: Every gap has assigned owner

❌ **MISTAKE**: Compliance check only on sample
✅ **CORRECT**: Check all NDAs annually

❌ **MISTAKE**: No trend analysis of gaps
✅ **CORRECT**: Track gap trends over time

❌ **MISTAKE**: Reviews not documented
✅ **CORRECT**: Formal review records with findings

### Quality Checklist

- [ ] Periodic review schedule established
- [ ] All templates assessed for adequacy
- [ ] Coverage analysis complete for all categories
- [ ] Compliance check performed on all NDAs
- [ ] All gaps documented with owners
- [ ] Remediation targets set
- [ ] Approval sign-offs obtained

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.6.6.3_NDA_Review_and_Compliance_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Review_Type | Annual Full Review, Quarterly Check, Template Update Review, Triggered Review, Ad-hoc Review |
| Review_Status | Scheduled, In Progress, Completed, Overdue, Cancelled |
| Adequacy | Adequate, Partially Adequate, Inadequate, Not Assessed |
| Gap_Type | Missing NDA, Expired NDA, Inadequate Template, Unsigned, Wrong Template, Storage Issue, Other |
| Gap_Severity | Critical, High, Medium, Low |
| Gap_Status | Open, In Progress, Remediated, Verified Closed, Risk Accepted |
| Compliance_Status | Compliant, Partially Compliant, Non-Compliant |

### Generator Reference

**Script**: `generate_a66_3_nda_review_compliance.py`

**Location**: `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"In God we trust; all others must bring data."*
— W. Edwards Deming

<!-- QA_VERIFIED: 2026-02-01 -->
