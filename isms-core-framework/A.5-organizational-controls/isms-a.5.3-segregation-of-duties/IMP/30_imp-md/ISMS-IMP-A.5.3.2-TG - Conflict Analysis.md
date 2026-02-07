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

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.3.2-UG.

---

# Technical Specification


> Auto-generated from `generate_a53_2_conflict_analysis.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.3.2` |
| **Output Filename** | `ISMS-IMP-A.5.3.2_Conflict_Analysis_YYYYMMDD.xlsx` |
| **Workbook Title** | Conflict Analysis |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FABF8F | FABF8F | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Conflict_Register

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Conflict_ID |
| B | Gap_ID |
| C | Conflict_Category |
| D | Role_A |
| E | Role_B |
| F | Process |
| G | Conflict_Type |
| H | Persons_Affected |
| I | Analysis_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `category_dv` |
| G | G2:G200 | `type_dv` |
| I | I2:I200 | `status_dv` |

---

## Sheet 3: Impact_Assessment

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Conflict_ID |
| B | Financial_Impact |
| C | Operational_Impact |
| D | Reputational_Impact |
| E | Compliance_Impact |
| F | Data_Impact |
| G | Overall_Impact |
| H | Justification |
| I | Assessor |
| J | Assessment_Date |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B2:F200 | `impact_dv` |

---

## Sheet 4: Exploitation_Scenarios

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Scenario_ID |
| B | Conflict_ID |
| C | Scenario_Name |
| D | Threat_Actor |
| E | Motivation |
| F | Method |
| G | Detection_Difficulty |
| H | Historical_Precedent |
| I | Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D200 | `actor_dv` |
| G | G2:G200 | `detection_dv` |
| H | H2:H200 | `precedent_dv` |

---

## Sheet 5: Control_Mapping

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Mapping_ID |
| B | Conflict_ID |
| C | Control_ID |
| D | Control_Name |
| E | Control_Type |
| F | Effectiveness |
| G | Implementation_Status |
| H | Gap_Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `type_dv` |
| F | F2:F200 | `eff_dv` |
| G | G2:G200 | `status_dv` |

---

## Sheet 6: Trend_Analysis

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Total_Conflicts |
| C | Critical_Conflicts |
| D | High_Conflicts |
| E | Resolved_Count |
| F | New_Conflicts |
| G | Resolution_Rate |
| H | Trend_Notes |

---

## Sheet 7: Prioritisation_Matrix

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Conflict_ID |
| B | Impact_Score |
| C | Likelihood_Score |
| D | Control_Effectiveness |
| E | Priority_Score |
| F | Priority_Level |
| G | Action_Timeline |
| H | Assigned_To |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `likelihood_dv` |

---

## Sheet 8: Evidence_Register

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Conflict_ID |
| C | Evidence_Type |
| D | Description |
| E | Location |
| F | Date_Collected |
| G | Collected_By |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `type_dv` |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `ANALYSIS_STATUSES` | Pending, In Progress, Complete |
| `CONFLICT_CATEGORIES` | Maker-Checker, Requestor-Approver, Developer-Deployer, Administrator-Auditor, Creator-Reconciler,... |
| `CONFLICT_TYPES` | X, C, M |
| `CONTROL_EFFECTIVENESS` | High, Medium, Low |
| `CONTROL_TYPES` | Preventive, Detective, Corrective, Compensating |
| `DETECTION_DIFFICULTY` | Very High, High, Medium, Low, Very Low |
| `EVIDENCE_TYPES` | Analysis Document, System Export, Interview Notes, Historical Incident, Control Evidence |
| `IMPACT_LEVELS` | 1, 2, 3, 4, 5 |
| `IMPLEMENTATION_STATUS` | Implemented, Partial, Planned, Not Implemented |
| `PRIORITY_LEVELS` | Critical, High, Medium, Low |
| `RISK_LEVELS` | Critical, High, Medium, Low |
| `THREAT_ACTORS` | Insider-Malicious, Insider-Negligent, External-Attacker, Colluding-Parties |

---

**END OF SPECIFICATION**

---

*"The price of liberty is eternal vigilance."*
— Thomas Jefferson

<!-- QA_VERIFIED: 2026-02-06 -->
