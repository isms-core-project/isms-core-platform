**ISMS-IMP-A.6.3.3-TG - Training Delivery and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Training Completion Tracking and Effectiveness Measurement |
| **Related Policy** | ISMS-POL-A.6.3, Section 2.5 (Delivery Requirements), Section 2.6 (Competency Assessment) |
| **Purpose** | Track training completion, measure assessment results, manage remediation, and verify competency across all personnel |
| **Target Audience** | HR Training Administrators, LMS Administrators, Department Managers, Information Security Officers |
| **Assessment Type** | Operational Tracking & Compliance Monitoring |
| **Review Cycle** | Continuous tracking + Monthly reporting + Quarterly analysis |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Delivery and Tracking workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Generator Script Developers

---

# Excel Workbook Technical Specification

## Workbook Metadata

```python
DOCUMENT_ID = "ISMS-IMP-A.6.3.3"
WORKBOOK_NAME = "Training_Delivery_Tracking"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
```

## Sheet Specifications

### Sheet 3: Completion_Tracking

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Record_ID | 12 | Text | Unique, auto-increment |
| B | Employee_ID | 12 | Reference | Must exist in Personnel_Register |
| C | Employee_Name | 25 | Lookup | Auto from Personnel_Register |
| D | Module_ID | 15 | Reference | Must exist in Curriculum |
| E | Module_Title | 35 | Lookup | Auto from Curriculum |
| F | Assigned_Date | 12 | Date | Required |
| G | Due_Date | 12 | Date | Required |
| H | Completion_Date | 12 | Date | If completed |
| I | Status | 15 | Formula/Dropdown | Completed, In Progress, Overdue, Not Started |
| J | Days_Overdue | 12 | Formula | =IF(I="Overdue", TODAY()-G, 0) |
| K | Assessment_Score | 15 | Percentage | 0-100% |
| L | Pass_Fail | 10 | Formula | Based on threshold |
| M | Attempts | 10 | Integer | ≥1 |
| N | Certificate_ID | 20 | Text | If issued |
| O | Notes | 40 | Text | Optional |

**Status Formula:**
```excel
=IF(H<>"","Completed",IF(TODAY()>G,"Overdue",IF(F<>"","In Progress","Not Started")))
```

**Conditional Formatting:**
- Overdue: Red background
- Overdue >14 days: Bold red
- Completed: Green background
- Due within 7 days: Yellow background

### Sheet 5: Simulation_Results

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Campaign_ID | 15 | Text |
| B | Campaign_Name | 30 | Text |
| C | Campaign_Date | 12 | Date |
| D | Employee_ID | 12 | Reference |
| E | Email_Sent | 10 | Yes/No |
| F | Email_Opened | 10 | Yes/No |
| G | Link_Clicked | 10 | Yes/No |
| H | Credentials_Submitted | 18 | Yes/No |
| I | Reported_Suspicious | 15 | Yes/No |
| J | Time_To_Click | 15 | Duration (if clicked) |
| K | Time_To_Report | 15 | Duration (if reported) |
| L | Remediation_Assigned | 18 | Yes/No |
| M | Remediation_Completed | 18 | Yes/No |

**Conditional Formatting:**
- Credentials_Submitted = Yes: Red (Critical)
- Link_Clicked = Yes AND Reported_Suspicious = No: Orange (High)
- Link_Clicked = Yes AND Reported_Suspicious = Yes: Yellow (Learning)
- Link_Clicked = No AND Reported_Suspicious = Yes: Green (Ideal)
- Link_Clicked = No AND Reported_Suspicious = No: Gray (Neutral)

### Sheet 6: Remediation_Tracking

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Remediation_ID | 15 | Text | Unique |
| B | Employee_ID | 12 | Reference | Required |
| C | Trigger_Event | 20 | Dropdown | Failed Assessment, Clicked Phishing, Submitted Credentials, Pattern Failure |
| D | Trigger_Date | 12 | Date | Required |
| E | Remediation_Level | 15 | Dropdown | Level 1, Level 2, Level 3 |
| F | Remediation_Training | 35 | Text | Training assigned |
| G | Assigned_Date | 12 | Date | Required |
| H | Due_Date | 12 | Date | Required |
| I | Completion_Date | 12 | Date | When completed |
| J | Outcome | 15 | Dropdown | Passed, Failed, Escalated, In Progress |
| K | Manager_Notified | 15 | Yes/No | Required for Level 2+ |
| L | HR_Notified | 12 | Yes/No | Required for Level 3 |
| M | Notes | 50 | Text | Optional |

### Sheet 7: Compliance_Summary

**Metrics Calculated:**

**By Department:**
```
Completion_Rate = Completed / Total_Assigned
On_Time_Rate = Completed_On_Time / Completed
Average_Score = AVG(Assessment_Score)
Overdue_Count = COUNT(Status="Overdue")
```

**By Training Tier:**
Same metrics grouped by tier

**Dashboard Charts:**
- Completion rate by department (bar)
- Compliance trend over time (line)
- Simulation click rates by campaign (bar)
- Remediation outcomes (pie)

---

## Integration Notes

**LMS Integration:**
- Sheet 3 (Completion_Tracking) can be populated via LMS export
- Consider automated import process for large organizations

**Simulation Platform Integration:**
- Sheet 5 (Simulation_Results) populated from simulation platform export
- Standard fields align with common platforms (KnowBe4, Proofpoint, etc.)

**HRIS Integration:**
- Sheet 2 (Personnel_Register) synced with HR system
- Status updates when employees join/leave

---

## QA Checklist

- [ ] All 11 sheets created
- [ ] Formulas calculate correctly
- [ ] Conditional formatting applied
- [ ] Status formulas working
- [ ] Days overdue calculation accurate
- [ ] Lookup references functional
- [ ] Dashboard charts render

---

# Document Control

**Document ID:** ISMS-IMP-A.6.3.3
**Version:** 1.0
**Classification:** Internal
**Status:** Draft

---

**END OF SPECIFICATION**

---

*"I have found a very great number of exceedingly beautiful theorems."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
