**ISMS-IMP-A.5.35-36.S3-TG - Findings and Remediation Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35-36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S3-TG |
| **Title** | Findings and Remediation Management |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.35-36.S3_Findings_and_Remediation_Management_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 8

### Sheet Specifications

#### Findings_Register Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Finding_ID | 14 | Auto-format FND-YYYY-NNN |
| B | Source | 18 | Data validation |
| C | Source_Ref | 16 | User input |
| D | Finding_Date | 14 | Date field |
| E | Control_Ref | 12 | ISO control reference |
| F | Finding_Title | 35 | User input |
| G | Finding_Description | 50 | User input |
| H | Severity | 12 | Data validation |
| I | Risk_Rating | 12 | User input |
| J | Affected_Area | 22 | User input |
| K | Finding_Owner | 22 | User input |
| L | Target_Resolution | 14 | Date field |
| M | Status | 16 | Data validation |
| N | RCA_Required | 10 | Data validation |
| O | RCA_Ref | 14 | User input |
| P | Remediation_Ref | 14 | User input |
| Q | Notes | 30 | User input |

#### Remediation_Actions Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Action_ID | 14 | Auto-format ACT-YYYY-NNN |
| B | Finding_Ref | 14 | Link to Findings_Register |
| C | Action_Type | 14 | Data validation |
| D | Action_Description | 45 | User input |
| E | Action_Owner | 22 | User input |
| F | Priority | 12 | Data validation |
| G | Resources_Required | 30 | User input |
| H | Dependencies | 25 | User input |
| I | Start_Date | 14 | Date field |
| J | Target_Date | 14 | Date field |
| K | Actual_Completion | 14 | Date field |
| L | Status | 14 | Data validation |
| M | Percent_Complete | 12 | Percentage |
| N | Blockers | 30 | User input |
| O | Evidence_Ref | 16 | User input |
| P | Verified | 10 | Data validation |
| Q | Notes | 30 | User input |

#### Root_Cause_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | RCA_ID | 14 | Auto-format RCA-YYYY-NNN |
| B | Finding_Ref | 14 | Link to Findings_Register |
| C | RCA_Date | 14 | Date field |
| D | RCA_Lead | 22 | User input |
| E | RCA_Participants | 35 | User input |
| F | Methodology | 16 | Data validation |
| G | Problem_Statement | 45 | User input |
| H | Immediate_Cause | 40 | User input |
| I | Contributing_Factors | 40 | User input |
| J | Root_Cause | 45 | User input |
| K | Why_1 | 35 | User input |
| L | Why_2 | 35 | User input |
| M | Why_3 | 35 | User input |
| N | Why_4 | 35 | User input |
| O | Why_5 | 35 | User input |
| P | Corrective_Actions | 45 | User input |
| Q | Preventive_Actions | 45 | User input |
| R | Systemic_Issues | 40 | User input |
| S | Lessons_Learned | 40 | User input |
| T | Approval | 22 | User input |
| U | Approval_Date | 14 | Date field |

#### Verification_Log Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Verification_ID | 14 | Auto-format VER-YYYY-NNN |
| B | Action_Ref | 14 | Link to Remediation_Actions |
| C | Finding_Ref | 14 | Link to Findings_Register |
| D | Verification_Type | 18 | Data validation |
| E | Verification_Date | 14 | Date field |
| F | Verifier | 22 | User input |
| G | Verifier_Independence | 16 | Data validation |
| H | Verification_Method | 18 | Data validation |
| I | Evidence_Reviewed | 35 | User input |
| J | Outcome | 14 | Data validation |
| K | Issues_Found | 35 | User input |
| L | Retest_Required | 10 | Data validation |
| M | Retest_Date | 14 | Date field |
| N | Final_Status | 14 | Data validation |
| O | Notes | 30 | User input |

#### Trend_Analysis Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Period | 14 | User input |
| B | Period_Start | 14 | Date field |
| C | Period_End | 14 | Date field |
| D | Total_Findings | 12 | Numeric |
| E | Critical_Count | 12 | Numeric |
| F | High_Count | 12 | Numeric |
| G | Medium_Count | 12 | Numeric |
| H | Low_Count | 12 | Numeric |
| I | Observation_Count | 14 | Numeric |
| J | Closed_in_Period | 14 | Numeric |
| K | Overdue_at_Period_End | 14 | Numeric |
| L | Average_Resolution_Days | 14 | Numeric |
| M | Top_Control_Area | 20 | User input |
| N | Top_Department | 20 | User input |
| O | Recurring_Findings | 14 | Numeric |
| P | Trend_vs_Prior | 12 | Data validation |
| Q | Notes | 40 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Source | Independent Review, Compliance Assessment, Internal Audit, External Audit, Incident, Regulatory, Other |
| Severity | Critical, High, Medium, Low, Observation |
| Finding_Status | Open, In Progress, Remediated, Verified Closed, Risk Accepted |
| RCA_Required | Yes, No |
| Action_Type | Corrective, Preventive, Improvement |
| Priority | Critical, High, Medium, Low |
| Action_Status | Not Started, In Progress, On Hold, Completed, Cancelled |
| Verified | Yes, No, Pending |
| Methodology | 5 Whys, Fishbone, Fault Tree, FMEA, Other |
| Verification_Type | Self-Attestation, Peer Review, Independent Verification |
| Verifier_Independence | Independent, Not Independent |
| Verification_Method | Document Review, Testing, Interview, Observation, Combined |
| Verification_Outcome | Verified, Failed, Partial |
| Retest_Required | Yes, No |
| Final_Status | Open, Verified Closed |
| Trend_vs_Prior | Better, Same, Worse |

### Generator Reference

**Script**: `generate_a535_36_3_findings_remediation.py`

**Location**: `10-isms-scr-base/isms-a.5.35-36-compliance-review/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
