**ISMS-IMP-A.5.24-28.S1-TG - Incident Management Framework Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Management Framework Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S1-TG |
| **Assessment Domain** | Domain 1 - Framework & Governance (A.5.24 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial framework assessment specification |

**Review Cycle**: Annual (or after major incident management changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISO/IEC 27002:2022 Control A.5.24
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)

---

# Technical Specification

# Workbook Structure & Technical Details

**Audience:** Workbook developers, Python script maintainers

**This section provides technical specifications for workbook generation and automation.**

---

# Sheet 1: Instructions & Legend

## Header Section

**Title Block (Rows 1-3):**

- Row 1: Document Title - "ISMS-IMP-A.5.24-28.S1 — Incident Management Framework Assessment"
- Row 2: Subtitle - "ISO/IEC 27001:2022 - Control A.5.24: Planning and Preparation"
- Row 3: Empty (spacing)

**Styling:**

- Background: Dark blue (RGB 0, 51, 102 or #003366)
- Font: White, Bold, 18pt (Title), 14pt (Subtitle)
- Alignment: Center, Middle
- Row Height: 40px (Title), 30px (Subtitle)

## Document Information Block (Rows 5-15)

```
Row 5:  Document ID:          ISMS-IMP-A.5.24-28.S1
Row 6:  Assessment Area:      Incident Management Framework & Governance (Domain 1)
Row 7:  Related Policy:       ISMS-POL-A.5.24-28, Section 2.1
Row 8:  Version:              1.0
Row 9:  Assessment Date:      [USER INPUT - yellow cell]
Row 10: Completed By:         [USER INPUT - yellow cell]
Row 11: Organization:         [USER INPUT - yellow cell]
Row 12: Review Cycle:         Annual
Row 13: Next Review Date:     [AUTO-CALCULATE: Assessment Date + 12 months]
```

**Column Widths:**

- Column A: 25 (label)
- Column B: 50 (value)

## Assessment Scope (Rows 17-30)

**Section Title (Row 17):** "Assessment Scope"

- Font: Bold, 14pt
- Background: Light blue (RGB 200, 220, 240)

**Scope Description (Rows 18-30):**

- Multi-line text explaining what's included/excluded in this assessment
- Wrap text enabled
- Bullet points for included items (✅) and excluded items (❌)

## Color Legend (Rows 32-40)

**Legend Title (Row 32):** "Color Legend"

| Color | Meaning | RGB | Usage |
|-------|---------|-----|-------|
| Yellow | User Input Required | 255, 255, 200 | Input cells |
| Light Green | Calculated/Auto-filled | 200, 240, 200 | Formula cells |
| White | Read-Only Information | 255, 255, 255 | Instructions, labels |
| Light Gray | Optional/Not Applicable | 220, 220, 220 | Optional fields |
| Light Red | Gap/Issue Identified | 255, 200, 200 | Risk highlighting |
| Light Blue | Section Header | 200, 220, 240 | Section titles |

## Dropdown Options Reference (Rows 42-60)

**Common Dropdowns:**

- Yes / No / Partial / N/A
- Yes - Comprehensive / Yes - Basic / No
- Critical / High / Medium / Low
- Implemented / Partial / Not Implemented
- [Role-specific dropdowns listed]

## Freeze Panes

**Set freeze at Row 5, Column B** so headers remain visible during scrolling.

---

# Sheet 2: Governance Assessment

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Question_ID | 12 |
| B | Section | 15 |
| C | Question | 50 |
| D | Answer | 20 |
| E | Evidence_Reference | 25 |
| F | Comments | 30 |
| G | Gap_Identified | 10 |

**Header Styling:**

- Background: Dark blue (#003366)
- Font: White, Bold, 11pt
- Borders: All borders, white lines
- Alignment: Center, Middle
- Text wrap: Enabled

## Data Rows (Rows 5-29, 25 questions)

**Question Data Validation:**

Q1 (Policy_Exists): Dropdown

- List: Yes, No, In Draft
- Cell: D5
- Input Message: "Does a documented incident management policy exist?"
- Error Alert: "Please select from dropdown list"

Q2 (Policy_Approval_Date): Date

- Cell: D6
- Format: DD.MM.YYYY
- Data Validation: Date, ≤ TODAY()
- Conditional Formatting: If >730 days old (2 years), background light red

Q3 (Policy_Owner): Text

- Cell: D7
- Input Message: "Name and title of policy owner (typically CISO)"

Q4 (Policy_Review_Frequency): Dropdown

- List: Annually, Bi-Annually, Quarterly, Ad-Hoc, Not Defined
- Cell: D8

Q5 (Last_Policy_Review_Date): Date

- Cell: D9
- Format: DD.MM.YYYY
- Conditional Formatting: If > 365 days old, background light red

[Continue pattern for Q6-Q25]

**Conditional Formatting Rules:**

**Rule 1: Highlight "No" Answers (High Risk)**

- Applies to: Column D (Answer cells)
- Condition: Cell Value = "No"
- Format: Background light red (255, 200, 200)

**Rule 2: Highlight "Partial" Answers (Medium Risk)**

- Condition: Cell Value = "Partial" OR "Yes - Partial" OR "Informal"
- Format: Background light yellow (255, 255, 200)

**Rule 3: Highlight Overdue Dates**

- Applies to: Date cells (Policy Review, Training dates, etc.)
- Condition: Value < TODAY() - 365
- Format: Background light red + Bold red text

**Gap_Identified Column (Column G):**

- Formula: `=IF(OR(D5="No", D5="Partial", D5="Informal"), "Yes", "No")`
- Conditional Formatting: If "Yes", background light red

## Section Headers (Within Rows)

Insert blank rows with section headers:

- Row 5: "Section A: Policy Documentation" (merged A5:G5, light blue background, bold)
- Row 11: "Section B: Procedure Documentation"
- Row 17: "Section C: Authority & Escalation"
- Row 22: "Section D: Regulatory Compliance"
- Row 27: "Section E: Exception Management"
- Row 29: "Section F: Policy Governance"

---

# Sheet 3: Organizational Structure

## Header Row (Row 4)

Same structure as Sheet 2 (Question_ID, Section, Question, Answer, Evidence, Comments, Gap)

## Data Rows (Rows 5-60, 30 questions + role definitions)

**Section A: CSIRT/SOC Model (Q26-Q30)**

Q26 (Incident_Response_Model): Dropdown

- List: Dedicated CSIRT, Virtual CSIRT, Hybrid, Outsourced SOC/MSSP, Coordinated
- Cell: D5

Q27 (CSIRT_Establishment_Date): Date

- Format: MM.YYYY
- Conditional Formatting: Calculate age, color-code maturity

Q28 (CSIRT_Coverage): Dropdown

- List: 24/7/365, Business Hours Only, Extended Hours, On-Call Rotation

Q29 (CSIRT_Staffing_Level): Number

- Data Validation: Whole number, ≥0
- Conditional Formatting: 
  - <2 FTE: Red (understaffed)
  - 2-5 FTE: Yellow (adequate for small org)
  - >5 FTE: Green (well-staffed)

Q30 (CSIRT_Reporting_Structure): Text

- Input Message: "Title/Department (e.g., CISO, CIO, COO)"

**Section B: Role Definitions (Q31-Q45, 15 roles)**

For each role (4 columns per role):

- Role_Exists: Yes/No dropdown
- Role_Definition: Text (brief description)
- Assigned_To: Text (Name or "Vacant")
- RACI_Clarity: Dropdown (Clear, Unclear, Not Documented)

Example for Q31 (Incident_Manager):

- D11 (Role_Exists): Dropdown (Yes / No)
- E11 (Role_Definition): Text
- F11 (Assigned_To): Text
- G11 (RACI_Clarity): Dropdown

[Repeat for 15 roles: Q31-Q45]

**Section C: RACI Matrix (Q46-Q48)**

Q46 (RACI_Matrix_Exists): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q47 (RACI_Clarity_Assessment): Dropdown (Very Clear, Mostly Clear, Some Ambiguity, Significant Confusion)
Q48 (RACI_Last_Updated): Date

**Section D: Staffing Adequacy (Q49-Q52)**

Q49 (Staffing_Adequate): Dropdown (Yes, No, Barely Adequate)
Q50 (Turnover_Rate): Percentage (Data Validation: 0-100%)
Q51 (Succession_Planning): Dropdown (Yes, Informal, No)
Q52 (Skills_Gaps_Identified): Dropdown (Yes - Documented, Informally Identified, No)

**Section E: Management Visibility (Q53-Q55)**

Q53 (Management_Reporting_Frequency): Dropdown (Weekly, Monthly, Quarterly, Ad-Hoc, Never)
Q54 (CSIRT_Performance_Metrics): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q55 (Board_Briefing_Protocol): Dropdown (Yes, Informal, No, N/A)

---

# Sheet 4: Training & Competency

## Header Row (Row 4)

Same structure: Question_ID, Section, Question, Answer, Evidence, Comments, Gap

## Data Rows (Rows 5-35, 25 questions)

**Section A: Training Program (Q56-Q60)**

Q56 (Training_Program_Exists): Dropdown (Yes - Comprehensive, Yes - Basic, No)
Q57 (Annual_Awareness_Training): Dropdown (Yes, Partial, No)
Q58 (Awareness_Training_Completion_Rate): Percentage

  - Conditional Formatting: <95% red, 95-99% yellow, ≥99% green

Q59 (CSIRT_Specialized_Training): Dropdown (Yes - Regular, Yes - Occasional, No)
Q60 (External_Training_Budget): Dropdown (Yes - Adequate, Yes - Limited, No)

**Section B: Tabletop Exercises (Q61-Q65)**

Q61 (Tabletop_Exercise_Frequency): Dropdown (Quarterly, Semi-Annually, Annually, Bi-Annually, Never)
Q62 (Last_Tabletop_Date): Date

  - Conditional Formatting: >365 days = Red

Q63 (Tabletop_Scenario_Variety): Dropdown (Yes - Diverse, Limited Variety, Single Scenario Type)
Q64 (Tabletop_Participants): Checkbox (Multiple)

  - CSIRT, IT Ops, Legal, HR, Management, Executive, Board, External Partners

Q65 (Tabletop_Lessons_Learned): Dropdown (Yes - Systematically, Yes - Informally, No)

**Section C: Simulation & Testing (Q66-Q68)**

Q66 (Full_Scale_Exercises): Dropdown (Yes - Regularly, Yes - Occasionally, No)
Q67 (Breach_Simulation_Tools): Dropdown (Yes, No)
Q68 (Regulatory_Drills): Dropdown (Yes, No)

**Section D: Competency & Certification (Q69-Q72)**

Q69 (Competency_Requirements_Defined): Dropdown (Yes, No)
Q70 (Certification_Tracking): Dropdown (Yes, Informal, No)
Q71 (Certification_Currency): Dropdown (Yes - All Current, Some Expired, Not Tracked)
Q72 (New_Hire_Onboarding): Dropdown (Yes - Formal Program, Informal, No)

**Section E: Training Effectiveness (Q73-Q75)**

Q73 (Training_Effectiveness_Measured): Dropdown (Yes, No)
Q74 (Training_Feedback_Collected): Dropdown (Yes - Systematically, Occasionally, No)
Q75 (Training_Gaps_Identified): Dropdown (Yes - Documented, Informally Identified, No)

---

# Sheet 5: Tools & Technology

## Header Row (Row 4)

Same structure.

## Data Rows (Rows 5-50, 30 questions)

**Section A: Ticketing (Q76-Q79)**

Q76 (Ticketing_System_Exists): Dropdown (Yes - Dedicated IR, Yes - General IT, No)
Q77 (Ticketing_System_Features): Checkbox (Multiple selections)

  - Incident creation, Severity, Timeline, Evidence, Tasks, Collaboration, Escalation, Integration, Reporting, Playbooks

Q78 (Ticket_Retention): Dropdown (1 year, 3 years, 5 years, 7+ years, Indefinitely, Not Defined)
Q79 (Ticket_Access_Control): Dropdown (Yes - Strict, Yes - Moderate, No - Open)

**Section B: SIEM (Q80-Q83)**

Q80 (SIEM_Deployed): Dropdown (Yes - Fully Operational, Yes - Partial, No)
Q81 (SIEM_Log_Sources): Number

  - Conditional Formatting: <20 red, 20-50 yellow, >50 green

Q82 (SIEM_Integration_Ticketing): Dropdown (Yes - Fully Automated, Yes - Semi-Automated, Manual, N/A)
Q83 (SIEM_Playbook_Automation): Dropdown (Yes - Extensive, Yes - Limited, No, N/A)

**Section C: Forensics (Q84-Q87)**

Q84 (Forensic_Tools_Available): Checkbox (Multiple)

  - Disk imaging, Memory acquisition, Memory analysis, Network forensics, Log analysis, Malware analysis, Mobile forensics, Cloud forensics, Commercial suites, None

Q85 (Forensic_Tool_Training): Dropdown (Yes - All Members, Yes - Specialized Roles, Limited, No)
Q86 (Forensic_Workstation): Dropdown (Yes - Dedicated Lab, Yes - Virtual, No)
Q87 (Evidence_Storage): Dropdown (Yes - Dedicated, Yes - General, No)

**Section D: Communication (Q88-Q90)**

Q88 (Internal_Communication_Tools): Checkbox

  - Email, Phone, IM (Slack/Teams), Video, War Room, IR Platform, Encrypted

Q89 (External_Communication_Secure): Dropdown (Yes, No)
Q90 (On_Call_Alerting): Dropdown (PagerDuty, VictorOps, Phone, SMS, Email, No System)

**Section E: Threat Intel (Q91-Q93)**

Q91 (Threat_Intel_Feeds): Dropdown (Yes - Multiple, Yes - Single, No)
Q92 (Threat_Intel_Integration_SIEM): Dropdown (Yes - Automated, Yes - Manual, No, N/A)
Q93 (Threat_Intel_Analyst_Role): Dropdown (Yes - Dedicated, Yes - Part-Time, No - CSIRT Handles)

**Section F: Automation (Q94-Q96)**

Q94 (IR_Automation): Dropdown (High (SOAR), Moderate (Some Playbooks), Low (Mostly Manual), None)
Q95 (Playbook_Count): Number
Q96 (Playbook_Maintenance): Dropdown (Yes - Annually, Yes - After Incidents, No, N/A)

**Section G: Gaps (Q97-Q99)**

Q97 (Critical_Tool_Gaps): Dropdown (Yes - Multiple, Yes - Some, No)
Q98 (Tool_Procurement_Planned): Dropdown (Yes - Funded, Proposed, No)
Q99 (Tool_Integration_Challenges): Dropdown (Yes - Significant, Yes - Moderate, No, N/A)

---

# Sheet 6: Integration Assessment

## Header Row (Row 4)

Same structure.

## Data Rows (Rows 5-35, 25 questions)

**Sections A-F as outlined in Part I:**

- Logging Integration (Q100-Q102)
- Monitoring Integration (Q103-Q105)
- User Reporting Integration (Q106-Q108)
- BC/DR Integration (Q109-Q111)
- Third-Party Coordination (Q112-Q114)
- Legal & Regulatory (Q115-Q117)

Each question follows dropdown or text pattern as defined in Part I.

---

# Sheet 7: Gap Analysis

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Gap_ID | 10 |
| B | Assessment_Section | 15 |
| C | Gap_Description | 40 |
| D | Risk_Level | 10 |
| E | Current_State | 25 |
| F | Target_State | 25 |
| G | Remediation_Action | 35 |
| H | Owner | 15 |
| I | Target_Date | 12 |
| J | Status | 10 |

## Data Rows (Rows 5-64, 60 gap capacity)

**Gap_ID:**

- Format: GAP-001, GAP-002, etc.
- Auto-populate: `="GAP-" & TEXT(ROW()-4, "000")`

**Assessment_Section:** Dropdown

- List: Governance, Structure, Training, Tools, Integration

**Gap_Description:** Text

- Wrap text enabled

**Risk_Level:** Dropdown

- List: Critical, High, Medium, Low
- Conditional Formatting:
  - Critical: Red background
  - High: Orange background
  - Medium: Yellow background
  - Low: Green background

**Current_State, Target_State:** Text

**Remediation_Action:** Text

- Wrap text enabled

**Owner:** Text

**Target_Date:** Date

- Format: DD.MM.YYYY
- Conditional Formatting: If past due, red text

**Status:** Dropdown

- List: Open, In Progress, Resolved, Accepted (risk acceptance)

## Gap Summary (Rows 70-80)

**By Risk Level:**
```
Row 70: Total Gaps:     =COUNTA(A5:A64)
Row 71: Critical:       =COUNTIF(D5:D64, "Critical")
Row 72: High:           =COUNTIF(D5:D64, "High")
Row 73: Medium:         =COUNTIF(D5:D64, "Medium")
Row 74: Low:            =COUNTIF(D5:D64, "Low")
```

**By Status:**
```
Row 76: Open:           =COUNTIF(J5:J64, "Open")
Row 77: In Progress:    =COUNTIF(J5:J64, "In Progress")
Row 78: Resolved:       =COUNTIF(J5:J64, "Resolved")
Row 79: Accepted:       =COUNTIF(J5:J64, "Accepted")
```

---

# Sheet 8: Evidence Register

## Header Row (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence_ID | 12 |
| B | Evidence_Type | 15 |
| C | Description | 35 |
| D | Related_Section | 15 |
| E | Storage_Location | 30 |
| F | Date_Collected | 12 |
| G | Collected_By | 15 |
| H | Verification_Status | 15 |

## Data Rows (Rows 5-104, 100 evidence capacity)

**Evidence_ID:**

- Format: EV-001, EV-002, etc.
- Auto-populate: `="EV-" & TEXT(ROW()-4, "000")`

**Evidence_Type:** Dropdown

- List: Policy Document, Procedure, Org Chart, Job Description, RACI Matrix, Training Record, Exercise Report, Tool Screenshot, Contract/SLA, Metrics Report, Other

**Description:** Text

**Related_Section:** Dropdown

- List: Governance, Structure, Training, Tools, Integration, Multiple

**Storage_Location:** Text

- Format: Filepath or URL

**Date_Collected:** Date

**Collected_By:** Text

**Verification_Status:** Dropdown

- List: Verified, Pending, Needs Review
- Conditional Formatting: Verified = green, Pending = yellow

---

# Sheet 9: Dashboard

## Overall Maturity Score (Rows 6-15)

**Maturity Calculation Formula:**

```excel
Governance_Score (from Sheet2):  
  =COUNTIF(Sheet2!G:G, "No") / COUNTA(Sheet2!G:G) * 100
  (Inverted: 100% - gap percentage = compliance %)

Structure_Score (from Sheet3):
  Similar calculation

Training_Score (from Sheet4):
  Similar calculation

Tools_Score (from Sheet5):
  Similar calculation

Integration_Score (from Sheet6):
  Similar calculation

Overall_Maturity_Score:
  =(Governance*25% + Structure*20% + Training*20% + Tools*20% + Integration*15%)
```

**Maturity Level Determination:**

```excel
=IF(Overall_Score<40, "Level 1 (Initial)", 
  IF(Overall_Score<60, "Level 2 (Developing)",
    IF(Overall_Score<75, "Level 3 (Defined)",
      IF(Overall_Score<90, "Level 4 (Managed)", 
        "Level 5 (Optimizing)"))))
```

## Domain Scores (Rows 20-30)

Table format:
| Domain | Score (%) | Target | Status |
|--------|-----------|--------|--------|
| Governance | [Formula] | 90% | [Green/Yellow/Red] |
| Structure | [Formula] | 85% | [Light] |
| Training | [Formula] | 90% | [Light] |
| Tools | [Formula] | 80% | [Light] |
| Integration | [Formula] | 85% | [Light] |

**Conditional Formatting (Status Column):**

- Green: Score ≥ Target
- Yellow: Score 70-90% of Target
- Red: Score < 70% of Target

## Key Metrics (Rows 35-50)

```
CSIRT Staffing (FTE):              =Sheet3!D29
Coverage Model:                    =Sheet3!D28
Training Completion Rate:          =Sheet4!D8
Tabletop Exercise Frequency:       =Sheet4!D11
Tool Count:                        [Manual count from Sheet5]
Critical Gaps:                     =COUNTIF(Sheet7!D:D, "Critical")
High Gaps:                         =COUNTIF(Sheet7!D:D, "High")
```

## Top 10 Gaps (Rows 55-65)

Extract top 10 gaps by Risk_Level from Sheet 7:

- Sort by: Critical > High > Medium > Low
- Display: Gap_Description, Risk_Level, Owner, Target_Date

**Formula (using FILTER or manual reference):**
```excel
=FILTER(Sheet7!C5:C64, Sheet7!D5:D64="Critical")
```
(Adjust for Excel version if FILTER not available - use manual reference or VBA)

---

# Sheet 10: Approval Sign-Off

## Assessment Summary (Rows 5-20)

```
Assessment Period:          [Start Date] - [End Date]
Completed By:               [Name, Title]
Assessment Date:            [Date]
Overall Maturity Level:     =Sheet9!B10 (reference Dashboard calculation)
Overall Maturity Score:     =Sheet9!B8 (percentage)

Key Findings:
  Strengths:                [Text box, manually entered]
  Critical Gaps:            [Text box, reference Sheet 7]
  Remediation Priority:     [Text box, manually entered]
```

## Approval Workflow (Rows 25-35)

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Assessor (CSIRT Manager) | [Input] | [Input] | [Digital or Manual] | Submitted / Pending |
| Reviewer (CISO) | [Input] | [Input] | [Digital or Manual] | Approved / Revisions Required |
| Next Review Date | - | [Assessment Date + 12 months] | - | - |

**Status Dropdown:**

- Assessor: Submitted / Pending
- Reviewer: Approved / Revisions Required

**Conditional Formatting:**

- Approved: Green highlight
- Revisions Required: Yellow highlight

---

# Cell Styling Reference

## Standard Styles

**User Input Cells:**

- Background: Yellow (255, 255, 200)
- Border: Thin black
- Protection: Unlocked

**Calculated Cells:**

- Background: Light green (200, 240, 200)
- Border: Thin black
- Protection: Locked

**Headers:**

- Background: Dark blue (0, 51, 102)
- Font: White, Bold, 11pt
- Border: White lines
- Alignment: Center, Middle

**Section Headers:**

- Background: Light blue (200, 220, 240)
- Font: Bold, 12pt
- Merge cells across row

**Conditional Formatting Colors:**

- Red (Risk/Gap): RGB 255, 200, 200
- Yellow (Warning): RGB 255, 255, 200
- Green (Good): RGB 200, 240, 200
- Orange (Medium): RGB 255, 220, 180

---

# Data Validation Rules

## Dropdown Lists

Store dropdown lists in a hidden sheet ("Lists"):
```
Sheet: Lists (Hidden)
Column A: Yes_No_Partial = Yes, No, Partial, N/A
Column B: Risk_Levels = Critical, High, Medium, Low
Column C: Status_Options = Open, In Progress, Resolved, Accepted
Column D: [Other dropdown lists as needed]
```

**Apply Named Ranges:**

- Define name "YesNoPartial" for Lists!A:A
- Define name "RiskLevels" for Lists!B:B
- etc.

**Data Validation Formula:**
```excel
=YesNoPartial
```

## Date Validation

**Rule:** Date must be ≤ TODAY()
**Error Message:** "Date cannot be in the future"

**Rule:** Date within reasonable range (e.g., 1990-2030)

## Number Validation

**Percentages:** 0-100, whole number or decimal
**FTE Count:** ≥0, whole number or decimal (0.5 acceptable)
**Tool Count:** ≥0, whole number

---

# Protection Settings

**Sheet Protection:**

- Enable for all sheets except "Instructions & Legend"
- Password: [Set organization-specific password]
- Allow: Select unlocked cells, Format cells (locked and unlocked)
- Disallow: Insert/delete rows, columns

**Unlocked Cells:**

- All yellow (user input) cells
- Evidence Register description cells

**Locked Cells:**

- All calculated cells
- Headers and labels
- Instructions

---

# Formula Examples

## Gap Identification

```excel
='Sheet2'!G5  (Gap_Identified column)
=IF(OR(D5="No", D5="Partial", D5="Informal"), "Yes", "No")
```

## Score Calculation

```excel
='Sheet9'!B8 (Overall Maturity Score)
=(Governance_Score*0.25 + Structure_Score*0.20 + Training_Score*0.20 + Tools_Score*0.20 + Integration_Score*0.15)

Where:
Governance_Score = 100 - (COUNTIF(Sheet2!G:G, "Yes") / COUNTA(Sheet2!G:G) * 100)
```

## Conditional Cell References

```excel
Next Review Date (Sheet10):
=IF(ISBLANK(Sheet10!B8), "", Sheet10!B8 + 365)
(If Assessment Date blank, leave blank; otherwise, add 365 days)
```

---

# File Naming Convention

**Format:** `ISMS-IMP-A.5.24-28.S1_Framework_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.24-28.S1_Framework_Assessment_20260130.xlsx`

---

# Excel Version Compatibility

**Target Version:** Excel 2016 or later (Windows/Mac), Office 365

**Features Used:**

- Data Validation (dropdown lists)
- Conditional Formatting (color scales, rules)
- Named Ranges
- Cell Protection
- Basic formulas (IF, COUNTIF, COUNTA, FILTER if available)

**Compatibility Notes:**

- FILTER function (Excel 365): Provide alternative for Excel 2016 (manual reference or VBA)
- Conditional Formatting: Test in Excel 2016 to ensure compatibility
- No Power Query or Pivot Tables used (keep simple for broad compatibility)

---

# Workbook Generation Script Template

**Python Script:** `generate_a524_28_s1_framework_assessment.py`

**Libraries:**

- `openpyxl` (Excel file creation and manipulation)
- `datetime` (date handling)

**Script Structure:**
1. Create workbook
2. Create sheets (Instructions, Governance, Structure, Training, Tools, Integration, Gaps, Evidence, Dashboard, Approval)
3. Set column widths
4. Create headers with styling
5. Add data validation (dropdowns)
6. Add conditional formatting
7. Add formulas (gap identification, scoring)
8. Protect sheets (leave input cells unlocked)
9. Save workbook with timestamp

**Script Length:** ~400-500 lines (comprehensive header documentation + implementation)

---
**END OF SPECIFICATION**

---

*"I beg to introduce myself to you as a clerk in the Accounts Department... I have no university education... but I have been employing my spare time in mathematics."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
