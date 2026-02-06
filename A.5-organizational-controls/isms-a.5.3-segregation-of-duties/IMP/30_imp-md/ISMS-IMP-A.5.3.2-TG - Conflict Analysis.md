**ISMS-IMP-A.5.3.2-TG - Conflict Analysis**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.2-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Exploitation Scenario Library](#16-exploitation-scenario-library)
   - [1.7 Evidence Collection](#17-evidence-collection)
   - [1.8 Common Pitfalls](#18-common-pitfalls)
   - [1.9 Quality Checklist](#19-quality-checklist)
   - [1.10 Review and Approval](#110-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Formulas](#24-formulas)
   - [2.5 Integration Points](#25-integration-points)
   - [2.6 Related Documents](#26-related-documents)

---

# Technical Specification

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.3.2_Conflict_Analysis_YYYYMMDD.xlsx` |
| Generator | `generate_a53_2_conflict_analysis.py` |
| Sheets | 8 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Conflict_Register | Master list | 100+ | 9 |
| 3 | Impact_Assessment | Impact analysis | 100+ | 10 |
| 4 | Exploitation_Scenarios | Attack paths | 200+ | 9 |
| 5 | Control_Mapping | Mitigations | 200+ | 8 |
| 6 | Trend_Analysis | Historical | 20+ | 8 |
| 7 | Prioritisation_Matrix | Rankings | 100+ | 8 |
| 8 | Evidence_Register | Documentation | 50+ | 7 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Document Information table | Metadata reference |
| 12-30 | Methodology overview | Guidance for analysts |
| 32-50 | Impact scoring reference | Consistent ratings |

### Sheet 2: Conflict_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Conflict_ID | 15 | Text | None |
| B | Gap_ID | 15 | Text | None |
| C | Conflict_Category | 20 | List | Maker-Checker, Requestor-Approver, Developer-Deployer, Administrator-Auditor, Creator-Reconciler, Custodian-Owner, Other |
| D | Role_A | 25 | Text | None |
| E | Role_B | 25 | Text | None |
| F | Process | 25 | Text | None |
| G | Conflict_Type | 12 | List | X, C, M |
| H | Persons_Affected | 12 | Number | >=0 |
| I | Analysis_Status | 15 | List | Pending, In Progress, Complete |

### Sheet 3: Impact_Assessment

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Conflict_ID | 15 | Text | None |
| B | Financial_Impact | 15 | List | 1, 2, 3, 4, 5 |
| C | Operational_Impact | 18 | List | 1, 2, 3, 4, 5 |
| D | Reputational_Impact | 18 | List | 1, 2, 3, 4, 5 |
| E | Compliance_Impact | 18 | List | 1, 2, 3, 4, 5 |
| F | Data_Impact | 15 | List | 1, 2, 3, 4, 5 |
| G | Overall_Impact | 15 | Formula | `=MAX(B:F)` |
| H | Justification | 50 | Text | None |
| I | Assessor | 20 | Text | None |
| J | Assessment_Date | 15 | Date | None |

### Sheet 4: Exploitation_Scenarios

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Scenario_ID | 15 | Text | None |
| B | Conflict_ID | 15 | Text | None |
| C | Scenario_Name | 30 | Text | None |
| D | Threat_Actor | 25 | List | Insider-Malicious, Insider-Negligent, External-Attacker, Colluding-Parties |
| E | Motivation | 25 | Text | None |
| F | Method | 60 | Text | None |
| G | Detection_Difficulty | 15 | List | Very High, High, Medium, Low, Very Low |
| H | Historical_Precedent | 10 | List | Yes, No, Unknown |
| I | Reference | 40 | Text | None |

### Sheet 5: Control_Mapping

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Mapping_ID | 15 | Text | None |
| B | Conflict_ID | 15 | Text | None |
| C | Control_ID | 15 | Text | None |
| D | Control_Name | 35 | Text | None |
| E | Control_Type | 15 | List | Preventive, Detective, Corrective, Compensating |
| F | Effectiveness | 12 | List | High, Medium, Low |
| G | Implementation_Status | 18 | List | Implemented, Partial, Planned, Not Implemented |
| H | Gap_Notes | 50 | Text | None |

### Sheet 6: Trend_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Period | 12 | Text | e.g., 2026-Q1 |
| B | Total_Conflicts | 15 | Number | None |
| C | Critical_Conflicts | 18 | Number | None |
| D | High_Conflicts | 15 | Number | None |
| E | Resolved_Count | 15 | Number | None |
| F | New_Conflicts | 15 | Number | None |
| G | Resolution_Rate | 15 | Formula | `=E/B*100` |
| H | Trend_Notes | 50 | Text | None |

### Sheet 7: Prioritisation_Matrix

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Conflict_ID | 15 | Text | None |
| B | Impact_Score | 12 | Number | From Impact_Assessment |
| C | Likelihood_Score | 15 | List | 1, 2, 3, 4, 5 |
| D | Control_Effectiveness | 20 | Number | 0.0-1.0 |
| E | Priority_Score | 15 | Formula | `=B*C*(1-D)` |
| F | Priority_Level | 15 | Formula | Based on score thresholds |
| G | Action_Timeline | 25 | Text | Auto from Priority_Level |
| H | Assigned_To | 25 | Text | None |

### Sheet 8: Evidence_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Evidence_ID | 15 | Text | None |
| B | Conflict_ID | 15 | Text | None |
| C | Evidence_Type | 20 | List | Analysis Document, System Export, Interview Notes, Historical Incident, Control Evidence |
| D | Description | 40 | Text | None |
| E | Location | 50 | Text | None |
| F | Date_Collected | 15 | Date | None |
| G | Collected_By | 25 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Impact_Assessment | G:G | =5 | Red fill (#FFC7CE), Bold |
| Impact_Assessment | G:G | =4 | Orange fill (#FABF8F) |
| Impact_Assessment | G:G | =3 | Yellow fill (#FFEB9C) |
| Impact_Assessment | G:G | =2 | Light green fill (#C6EFCE) |
| Exploitation_Scenarios | G:G | ="Very High" | Red fill (#FFC7CE) |
| Exploitation_Scenarios | G:G | ="High" | Orange fill (#FABF8F) |
| Control_Mapping | F:F | ="Low" | Red fill (#FFC7CE) |
| Control_Mapping | F:F | ="Medium" | Yellow fill (#FFEB9C) |
| Control_Mapping | F:F | ="High" | Green fill (#C6EFCE) |
| Control_Mapping | G:G | ="Not Implemented" | Red fill (#FFC7CE) |
| Prioritisation_Matrix | F:F | ="Critical" | Red fill (#FFC7CE), Bold |
| Prioritisation_Matrix | F:F | ="High" | Orange fill (#FABF8F) |
| Prioritisation_Matrix | F:F | ="Medium" | Yellow fill (#FFEB9C) |
| Prioritisation_Matrix | F:F | ="Low" | Green fill (#C6EFCE) |

---

## 2.4 Formulas

**Overall Impact (Impact_Assessment, Column G):**
```
=MAX(B{row},C{row},D{row},E{row},F{row})
```

**Resolution Rate (Trend_Analysis, Column G):**
```
=IF(B{row}>0, E{row}/B{row}*100, 0)
```

**Priority Score (Prioritisation_Matrix, Column E):**
```
=B{row}*C{row}*(1-D{row})
```

**Priority Level (Prioritisation_Matrix, Column F):**
```
=IF(E{row}>=15,"Critical",IF(E{row}>=10,"High",IF(E{row}>=5,"Medium","Low")))
```

**Action Timeline (Prioritisation_Matrix, Column G):**
```
=IF(F{row}="Critical","Immediate (<7 days)",IF(F{row}="High","Short-term (<30 days)",IF(F{row}="Medium","Medium-term (<90 days)","Long-term (<180 days)")))
```

---

## 2.5 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| ISMS-IMP-A.5.3.1 | Gap import | A.5.3.1 -> Conflict_Register |
| Risk Management | Risk ratings | Risk Register <-> Impact_Assessment |
| Control Library | Control catalogue | Control Library -> Control_Mapping |
| Incident Management | Historical incidents | ITSM -> Exploitation_Scenarios |
| A.5.3.4 Dashboard | Metrics aggregation | This workbook -> Dashboard |

---

## 2.6 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.3 | Segregation of Duties | Parent policy |
| ISMS-IMP-A.5.3.1 | SoD Matrix Assessment | Source of conflicts |
| ISMS-IMP-A.5.3.3 | Role-Function Mapping | Role definitions |
| ISMS-IMP-A.5.3.4 | Compliance Dashboard | Reporting consolidation |
| ISMS-IMP-A.5.24-28 | Incident Management | Incident correlation |

---

**END OF SPECIFICATION**

---

*"The price of liberty is eternal vigilance."*
— Thomas Jefferson

<!-- QA_VERIFIED: 2026-02-06 -->
