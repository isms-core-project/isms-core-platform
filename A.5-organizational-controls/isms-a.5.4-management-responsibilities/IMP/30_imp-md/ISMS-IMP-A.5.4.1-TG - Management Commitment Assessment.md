**ISMS-IMP-A.5.4.1-TG - Management Commitment Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.1-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification

### 10. Workbook Technical Details

#### 10.1 File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.4.1_Management_Commitment_Assessment_YYYYMMDD.xlsx` |
| Generator | `generate_a54_1_management_commitment.py` |
| Sheets | 4 |
| Protected | No (input cells unlocked) |

#### 10.2 Sheet Specifications

**Sheet 1: Instructions**

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Document Information table | Metadata reference |
| 12-25 | Scoring methodology | Guidance for assessors |
| 27-40 | Criteria reference table | Quick reference |
| 42-50 | Threshold definitions | Status guidance |

**Sheet 2: Manager Inventory**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Manager_ID | 12 | Text | None |
| B | Name | 25 | Text | None |
| C | Title | 30 | Text | None |
| D | Department | 20 | Text | None |
| E | Management_Level | 18 | List | Executive, Director, Manager, Team Lead, Supervisor |
| F | Direct_Reports | 12 | Number | ≥0 |
| G | Assessment_Date | 15 | Date | None |
| H | Assessor | 20 | Text | None |
| I | Status | 12 | List | Pending, In Progress, Complete |

**Pre-populated Departments:**
Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support

**Sheet 3: Commitment Assessment**

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Manager_ID | 12 | Text | None |
| B | Category | 18 | Text | Pre-populated |
| C | Criterion | 50 | Text | Pre-populated |
| D | Weight | 8 | Number | Pre-populated |
| E | Score (0-5) | 12 | Number | 0, 1, 2, 3, 4, 5 |
| F | Weighted_Score | 15 | Formula | `=E{row}*D{row}/5` |
| G | Evidence | 35 | Text | None |
| H | Notes | 30 | Text | None |

**Pre-populated Criteria (11 rows per manager):**

| Row | Category | Criterion | Weight |
|:---:|----------|-----------|:------:|
| 1 | Attendance | Attends scheduled ISMS Committee meetings | 10 |
| 2 | Attendance | Participates in security governance forums | 10 |
| 3 | Attendance | Available for security escalations and decisions | 10 |
| 4 | Training | Completes required security awareness training on time | 10 |
| 5 | Training | Ensures direct reports complete mandatory training | 10 |
| 6 | Resource Support | Approves budget for security initiatives | 10 |
| 7 | Resource Support | Provides adequate staffing for security activities | 10 |
| 8 | Operational Engagement | Reviews and acts on security reports/metrics | 10 |
| 9 | Operational Engagement | Responds to security incidents within SLA | 10 |
| 10 | Culture/Enforcement | Demonstrates security-conscious behaviour (no bypasses) | 5 |
| 11 | Culture/Enforcement | Holds personnel accountable for policy compliance | 5 |

**Sheet 4: Summary Scores**

| Column | Header | Width | Type | Formula |
|:------:|--------|:-----:|------|---------|
| A | Manager_ID | 12 | Text | None |
| B | Name | 25 | Text | None |
| C | Management_Level | 18 | Text | None |
| D | Total_Weight | 12 | Number | Fixed: 100 |
| E | Achieved_Score | 15 | Number | SUMIF from Commitment Assessment |
| F | Percentage | 12 | Formula | `=IF(E{row}>0,E{row}/D{row}*100,0)` |
| G | Status | 18 | Formula | See below |
| H | Improvement_Areas | 40 | Text | None |

**Status Formula:**
```
=IF(F{row}>=90,"Exemplary",IF(F{row}>=70,"Adequate",IF(F{row}>=50,"Improvement Needed","Non-Compliant")))
```

#### 10.3 Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| G:G (Status) | ="Exemplary" | Green fill (#C6EFCE) |
| G:G (Status) | ="Adequate" | Light green fill (#E2EFDA) |
| G:G (Status) | ="Improvement Needed" | Yellow fill (#FFEB9C) |
| G:G (Status) | ="Non-Compliant" | Red fill (#FFC7CE) |
| E:E (Score) | =0 | Red fill (#FFC7CE) |
| E:E (Score) | =5 | Green fill (#C6EFCE) |

#### 10.4 Styling

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered, merged |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold, Centered |
| Input cells | Yellow fill (#FFFFCC), thin border |
| Formula cells | Grey fill (#F2F2F2), protected |
| All data cells | Thin black border |

---

### 11. Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| LMS | Training completion data | Export → Assessment input |
| HR System | Manager inventory, reporting structure | Export → Manager Inventory |
| Calendar/Meeting System | ISMS Committee attendance records | Export → Evidence folder |
| ITSM | Incident response participation records | Export → Evidence folder |
| Budget System | Security budget allocation approvals | Export → Evidence folder |
| SharePoint | Evidence storage, workbook archive | Bidirectional |

---

### 12. Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.4 | Management Responsibilities | Parent policy |
| ISMS-IMP-A.5.4.2 | Compliance Oversight Tracker | Complementary assessment |
| ISMS-IMP-A.5.4.3 | Leadership Dashboard | Consolidates results |
| ISMS-IMP-A.5.4.4 | Security Culture Survey | Employee perspective |
| ISMS-IMP-A.6.3 | Awareness and Training | Training metrics source |

---

### 13. Trend Analysis

#### 13.1 Year-over-Year Comparison

Track the following metrics annually:

| Metric | 2024 | 2025 | 2026 | Trend |
|--------|:----:|:----:|:----:|:-----:|
| Average Score (All Managers) | - | - | - | - |
| % Exemplary | - | - | - | - |
| % Adequate | - | - | - | - |
| % Improvement Needed | - | - | - | - |
| % Non-Compliant | - | - | - | - |
| Lowest Category Average | - | - | - | - |

#### 13.2 Improvement Targets

| Current Status | Target for Next Year |
|----------------|---------------------|
| Non-Compliant | Improvement Needed (minimum) |
| Improvement Needed | Adequate |
| Adequate | Maintain or improve |
| Exemplary | Maintain |

---

**END OF SPECIFICATION**

---

*"The quality of a leader is reflected in the standards they set for themselves."*
— Ray Kroc

<!-- QA_VERIFIED: 2026-02-06 -->
