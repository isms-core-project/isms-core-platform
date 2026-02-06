**ISMS-IMP-A.5.35-36.S2-TG - Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S2-TG |
| **Title** | Compliance Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.36 |
| **Control Name** | Compliance with Policies, Rules and Standards |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.35-36.S2_Compliance_Assessment_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Sheet Specifications

#### Policy_Compliance Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Policy_ID | 18 | Policy document ID |
| B | Policy_Title | 35 | Policy name |
| C | Policy_Version | 12 | Version number |
| D | Last_Review_Date | 14 | Date field |
| E | Compliance_Status | 16 | Data validation |
| F | Score | 10 | Numeric (0, 0.5, 1) |
| G | Key_Requirement_1 | 35 | User input |
| H | Req_1_Status | 14 | Data validation |
| I | Key_Requirement_2 | 35 | User input |
| J | Req_2_Status | 14 | Data validation |
| K | Key_Requirement_3 | 35 | User input |
| L | Req_3_Status | 14 | Data validation |
| M | Evidence_Ref | 16 | User input |
| N | Assessor | 20 | User input |
| O | Assessment_Date | 14 | Date field |
| P | Notes | 30 | User input |

#### Control_Compliance Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Control_ID | 14 | ISO control reference |
| B | Control_Name | 35 | Control title |
| C | Control_Objective | 40 | User input |
| D | Implementation_Status | 18 | Data validation |
| E | Operating_Effectiveness | 18 | Data validation |
| F | Compliance_Score | 14 | Numeric |
| G | Evidence_of_Implementation | 40 | User input |
| H | Evidence_of_Effectiveness | 40 | User input |
| I | Evidence_Ref | 16 | User input |
| J | Gap_Description | 35 | User input |
| K | Assessor | 20 | User input |
| L | Assessment_Date | 14 | Date field |

#### Department_Assessment Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Department | 25 | User input |
| B | Manager | 22 | User input |
| C | Assessment_Period | 14 | User input |
| D | Assessment_Date | 14 | Date field |
| E | Security_Awareness | 14 | Data validation |
| F | Policy_Knowledge | 14 | Data validation |
| G | Training_Compliance | 14 | Percentage |
| H | Incident_Reporting | 14 | Data validation |
| I | Asset_Management | 14 | Data validation |
| J | Access_Control | 14 | Data validation |
| K | Data_Handling | 14 | Data validation |
| L | Physical_Security | 14 | Data validation |
| M | Overall_Status | 16 | Data validation |
| N | Key_Issues | 40 | User input |
| O | Actions_Planned | 40 | User input |
| P | Notes | 30 | User input |

#### NonCompliance_Register Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | NC_ID | 14 | Auto-format |
| B | Source | 18 | Data validation |
| C | Related_Ref | 16 | User input |
| D | Description | 45 | User input |
| E | Severity | 12 | Data validation |
| F | Area_Affected | 22 | User input |
| G | Root_Cause | 35 | User input |
| H | Identified_Date | 14 | Date field |
| I | Owner | 22 | User input |
| J | Corrective_Action | 40 | User input |
| K | Target_Date | 14 | Date field |
| L | Status | 14 | Data validation |
| M | Closure_Date | 14 | Date field |
| N | Verification_By | 20 | User input |
| O | Notes | 30 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Compliance_Status | Compliant, Partial, Non-Compliant, Not Applicable |
| Requirement_Status | Met, Partially Met, Not Met, Not Applicable |
| Implementation_Status | Implemented, Partially Implemented, Not Implemented, Not Applicable |
| Operating_Effectiveness | Effective, Partially Effective, Ineffective |
| Awareness_Level | High, Medium, Low |
| Department_Overall | Compliant, Partial, Non-Compliant |
| NC_Source | Policy Assessment, Control Assessment, Department Assessment, Audit, Other |
| Severity | Critical, High, Medium, Low |
| NC_Status | Open, In Progress, Remediated, Verified, Risk Accepted |

### Generator Reference

**Script**: `generate_a535_36_2_compliance_assessment.py`

**Location**: `10-isms-scr-base/isms-a.5.35-36-compliance-review/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"Compliance is not about checking boxes; it's about doing the right thing."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
