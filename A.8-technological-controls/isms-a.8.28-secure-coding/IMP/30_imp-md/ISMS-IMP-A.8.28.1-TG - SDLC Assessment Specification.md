**ISMS-IMP-A.8.28.1-TG - SDLC Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Development Lifecycle (SDLC) Integration |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.1 (Pre-Development Requirements), Section 3.1 (Roles & Responsibilities) |
| **Purpose** | Evaluate integration of security practices into SDLC, focusing on pre-development activities and process-level controls that prevent vulnerabilities |
| **Target Audience** | Application Security Lead, Development Managers, Security Architects, Project Managers, Auditors |
| **Assessment Type** | Process & Organizational |
| **Review Cycle** | Quarterly or After Major SDLC Changes |
| **Date** | [Date] |

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial assessment specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Development Manager / Engineering Lead (Engineering Perspective)
- QA Manager / Test Lead (Testing Validation)
- CISO / Security Director (Executive Approval)

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.28.1-UG.

---

# Technical Specification

**Audience:** Workbook developers (Python/Excel script maintainers)

---

# Excel Workbook Structure

## Sheet Overview

The SDLC Assessment workbook consists of 10 sheets:

| Sheet # | Sheet Name | Purpose | Input Type |
|---------|------------|---------|------------|
| 1 | Instructions | Assessment guidance and methodology | Read-only |
| 2 | Security_Requirements_Design | Security requirements and secure design assessment | User input (yellow cells) |
| 3 | Development_Environment | Development environment security controls | User input (yellow cells) |
| 4 | Build_Deployment_Pipeline | Build and deployment pipeline security | User input (yellow cells) |
| 5 | Security_Testing_Integration | Security testing integration assessment | User input (yellow cells) |
| 6 | Release_Change_Management | Release and change management security | User input (yellow cells) |
| 7 | Summary_Dashboard | Executive overview and compliance metrics | Auto-calculated |
| 8 | Evidence_Register | Supporting documentation tracking | User input (yellow cells) |
| 9 | Gap_Analysis | Non-compliant items and remediation plan | Auto-populated + user input |
| 10 | Approval_Sign_Off | Formal approval workflow | User input (yellow cells) |

## Common Column Structure (Assessment Sheets 2-6)

All assessment sheets use consistent column structure:

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | # | 5 | Question number | Auto-number |
| B | Domain | 15 | Domain/category name | Text |
| C | Assessment Question | 60 | Question text | Wrapped text |
| D | Policy Reference | 20 | ISMS-POL-A.8.28 section | Text |
| E | Status | 15 | Compliance status | Dropdown |
| F | Comments/Justification | 40 | Explanation for status | Wrapped text, yellow fill |
| G | Evidence ID | 15 | Reference to Evidence Register | Text, yellow fill |
| H | Gap Priority | 15 | Priority if Non-Compliant | Dropdown |
| I | Remediation Owner | 20 | Person responsible for fixing | Text, yellow fill |
| J | Target Date | 12 | Remediation deadline | Date picker, yellow fill |

**Total columns per assessment sheet**: 10 (A-J)

---

# Sheet 1: Instructions

## Header Section

**Row 1**: Title row

- Cell A1: "ISMS-IMP-A.8.28.1 – SDLC Assessment"
- Font: Calibri 16pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center
- Height: 40px
- Merge: A1:J1

**Row 2**: Subtitle row

- Cell A2: "ISO/IEC 27001:2022 - Control A.8.28: Secure Coding"
- Font: Calibri 12pt white
- Fill: #4472C4 (medium blue)
- Alignment: Center
- Merge: A2:J2

## Document Information Block (Rows 4-14)

```
Assessment Document:        ISMS-IMP-A.8.28.1 - SDLC Assessment
Assessment Area:            Secure Development Lifecycle Integration
Related Policy:             ISMS-POL-A.8.28 Section 2.1, Section 3.1
Version:                    1.0
Date:                       24.01.2026
Assessment Period:          [USER INPUT - yellow cell]
Completed By:               [USER INPUT - yellow cell]
Organization:               [USER INPUT - yellow cell]
Review Cycle:               Quarterly
Next Review Date:           [Auto-calc: +3 months from completion]
```

## Instructions Content (Rows 16+)

**Section**: How to Use This Workbook

- Step-by-step assessment instructions
- Reference to PART I: USER COMPLETION GUIDE for detailed guidance

**Section**: Status Legend

- ✅ Compliant (Green): Control fully implemented, evidence verified
- ⚠️ Partial (Yellow): Control partially implemented, gaps identified
- ❌ Non-Compliant (Red): Control not implemented or insufficient
- 🔄 Planned (Blue): Implementation in progress, timeline set
- N/A (Gray): Not applicable (with justification required)

**Section**: Evidence Requirements

- Documentation types accepted
- Where to upload evidence
- Evidence naming conventions

**Section**: Compliance Scoring

- Formula: (Compliant items / Total applicable items) × 100
- Total applicable = Total questions - N/A questions
- Domain scores and overall score calculation

**Section**: Assessment Workflow

- Preparation → Information Gathering → Assessment Completion → Review → Approval

---

# Sheets 2-6: Assessment Domain Sheets

## Sheet 2: Security_Requirements_Design

**Purpose**: Assess security requirements and secure design practices

**Questions** (15 total):
1. Are security requirements documented for all new development projects?
2. Are security risk assessments conducted for high-risk projects before development begins?
3. Are security acceptance criteria defined before development begins?
4. Are regulatory compliance requirements identified and documented for projects?
5. Are security requirements reviewed and approved by Application Security Team?
6. Is threat modeling performed for high-risk applications?
7. Do threat models include system overview, threat identification, and mitigation strategies?
8. Are threat models reviewed and approved by Security Architects?
9. Are security-by-design principles documented and applied?
10. Are architecture security reviews conducted for new applications?
11. Are secure design patterns documented and promoted?
12. Is developer security training provided within 30 days of hire?
13. Do 90%+ of developers complete annual security refresher training?
14. Is Security Champions program established?
15. Are training completion metrics reported to management?

**Column D (Policy Reference)**: References ISMS-POL-A.8.28 Section 2.1

**Column E (Status)**: Dropdown validation

- List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 🔄 Planned, N/A

**Conditional Formatting (Column E)**:

- ✅ Compliant → Fill: #C6EFCE (light green)
- ⚠️ Partial → Fill: #FFEB9C (light yellow)
- ❌ Non-Compliant → Fill: #FFC7CE (light red)
- 🔄 Planned → Fill: #B4C7E7 (light blue)
- N/A → Fill: #D9D9D9 (light gray)

**Column H (Gap Priority)**: Dropdown validation (appears if Status = ❌ or ⚠️)

- List: Critical, High, Medium, Low

---

## Sheet 3: Development_Environment

**Purpose**: Assess development environment security controls

**Questions** (12 total):
1. Is MFA enforced for all source code repository access?
2. Are branch protection rules enforced requiring code review before merge?
3. Are pre-commit hooks deployed to detect and block secrets?
4. Is developer workstation security baseline defined and enforced?
5. Are developer workstations encrypted (full disk encryption)?
6. Is antivirus/EDR deployed on developer workstations?
7. Are repository access controls configured (RBAC, least privilege)?
8. Are development environments isolated from production?
9. Is source code backed up and recoverable?
10. Are secrets managed via secret manager (no hardcoded credentials)?
11. Is developer security baseline audit performed periodically?
12. Is test data security managed (production data not used without approval)?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.5

---

## Sheet 4: Build_Deployment_Pipeline

**Purpose**: Assess build and deployment pipeline security

**Questions** (12 total):
1. Are CI/CD pipelines secured (no secrets in logs, RBAC applied)?
2. Are SAST tools integrated into CI/CD pipelines?
3. Are DAST tools integrated into CI/CD pipelines?
4. Are SCA tools integrated into CI/CD pipelines?
5. Are security gates configured in pipelines (fail build on Critical/High findings)?
6. Are container images scanned for vulnerabilities before deployment?
7. Are IaC templates scanned for misconfigurations?
8. Is pipeline configuration version-controlled and audited?
9. Are pipeline secrets managed securely (secret managers, not hardcoded)?
10. Are deployment approvals required for production?
11. Is rollback capability tested and documented?
12. Are pipeline audit logs retained per policy?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.3

---

## Sheet 5: Security_Testing_Integration

**Purpose**: Assess security testing integration practices

**Questions** (12 total):
1. Is security testing included in sprint planning?
2. Are security test cases maintained alongside functional test cases?
3. Is penetration testing performed before major releases?
4. Are security findings tracked in issue tracking system?
5. Are security testing SLAs defined and monitored?
6. Is API security testing performed?
7. Are authentication and authorization tests automated?
8. Are input validation tests comprehensive?
9. Is fuzz testing performed for critical components?
10. Are security test results reviewed by Security team?
11. Are regression tests run for previously found vulnerabilities?
12. Is security testing coverage measured and reported?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.3

---

## Sheet 6: Release_Change_Management

**Purpose**: Assess release and change management security

**Questions** (12 total):
1. Are security activities included in project plans and timelines?
2. Are security stories included in sprint backlogs for all projects?
3. Is Application Security Team engaged for threat modeling and architecture reviews?
4. Are security activities budgeted and resourced appropriately?
5. Is "Definition of Done" including security criteria (SAST passing, code reviewed)?
6. Are security milestones tracked in project status reporting?
7. Are security delays/blockers escalated to management?
8. Is security debt tracked and prioritized in technical debt backlog?
9. Are security sign-offs required before production release?
10. Are change management procedures followed for security-sensitive changes?
11. Are emergency changes reviewed for security impact?
12. Is post-release security monitoring in place?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.6

---

# Sheet 7: Summary_Dashboard

## Purpose
Provide executive-level overview of SDLC security maturity with auto-calculated compliance metrics.

## Layout

**Header** (Rows 1-2): Same as other sheets

**Overall Compliance Summary** (Rows 4-10):

| Metric | Formula | Format |
|--------|---------|--------|
| Total Assessment Items | `=COUNTA(Security_Requirements_Design!$C$4:$C$18) + COUNTA(Development_Environment!$C$4:$C$15) + ...` | Number |
| Compliant Items (✅) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"✅ Compliant") + ...` | Number, green |
| Partial Items (⚠️) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"⚠️ Partial") + ...` | Number, yellow |
| Non-Compliant Items (❌) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"❌ Non-Compliant") + ...` | Number, red |
| Planned Items (🔄) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"🔄 Planned") + ...` | Number, blue |
| N/A Items | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"N/A") + ...` | Number, gray |
| **Overall Compliance Rate** | `=(Compliant / (Total - N/A)) * 100` | Percentage, bold |

**Domain Compliance Breakdown** (Rows 12-18):

| Domain | Total Items | Compliant | Partial | Non-Compliant | Compliance % |
|--------|-------------|-----------|---------|---------------|--------------|
| Security Requirements & Design | 15 | [Formula] | [Formula] | [Formula] | [Formula] |
| Development Environment | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Build & Deployment Pipeline | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Security Testing Integration | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Release & Change Management | 12 | [Formula] | [Formula] | [Formula] | [Formula] |

**Top Gaps Requiring Attention** (Rows 20-28):

- Auto-populated list of ❌ Non-Compliant items with Priority = Critical or High
- Pulled from Gap_Analysis sheet

**Visual Indicators**:

- Compliance Rate >= 90%: Green fill
- Compliance Rate 70-89%: Yellow fill
- Compliance Rate < 70%: Red fill

---

# Sheet 8: Evidence_Register

## Purpose
Track all evidence supporting assessment claims.

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Evidence ID | 12 | Auto-generated ID | `="EV-"&TEXT(ROW()-3,"000")` |
| B | Evidence Description | 50 | What this evidence proves | Wrapped text, yellow fill |
| C | Related Assessment Question | 30 | Which question(s) this supports | Text, yellow fill |
| D | Evidence Type | 20 | Document, Screenshot, Report, etc. | Dropdown, yellow fill |
| E | Location | 60 | File path or URL | Wrapped text, yellow fill |
| F | Date Collected | 12 | When evidence was captured | Date picker, yellow fill |
| G | Collected By | 20 | Name of collector | Text, yellow fill |

**Evidence Type Dropdown**:

- Document
- Screenshot
- Configuration Export
- Report (LMS, Tool)
- Email
- Meeting Minutes
- Other

**Row Count**: 100 rows pre-formatted (evidence items EV-001 through EV-100)

---

# Sheet 9: Gap_Analysis

## Purpose
Consolidated view of all non-compliant and partial items requiring remediation.

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Gap ID | 10 | Auto-generated ID | `="GAP-"&TEXT(ROW()-3,"000")` |
| B | Domain | 20 | Which assessment domain | Auto-populated from source sheets |
| C | Assessment Question | 50 | Question text | Auto-populated, wrapped |
| D | Current Status | 15 | ⚠️ Partial or ❌ Non-Compliant | Auto-populated |
| E | Gap Description | 50 | What's missing or insufficient | User input, yellow fill |
| F | Priority | 12 | Critical/High/Medium/Low | Auto-populated from assessment sheets |
| G | Remediation Owner | 20 | Person responsible | User input, yellow fill |
| H | Target Date | 12 | Remediation deadline | Date picker, yellow fill |
| I | Remediation Status | 15 | Not Started/In Progress/Completed | Dropdown, yellow fill |
| J | Notes | 40 | Progress updates | User input, yellow fill |

**Auto-Population Logic**:

- Scans all assessment sheets (2-7)
- Identifies rows where Status = ❌ or ⚠️
- Populates Gap_Analysis with domain, question, status, priority
- User fills in Gap Description, Owner, Target Date, Status, Notes

---

# Sheet 10: Approval_Sign_Off

## Purpose
Document formal approval workflow.

## Layout

**Assessment Completed By** (Rows 4-10):
```
Name:               [USER INPUT - yellow]
Role/Title:         [USER INPUT - yellow]
Department:         [USER INPUT - yellow]
Email:              [USER INPUT - yellow]
Date:               [USER INPUT - date picker - yellow]
Signature:          [USER INPUT - yellow]
```

**Reviewed By - Application Security Lead** (Rows 12-19):
```
Name:               [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Review Notes:       [Text area - merged cells - yellow]
Recommendation:     [Dropdown: Approve / Approve with Conditions / Return for Revision]
```

**Reviewed By - Development Management** (Rows 21-28):
```
Name:               [USER INPUT - yellow]
Role/Title:         [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Review Notes:       [Text area - merged cells - yellow]
Recommendation:     [Dropdown: Approve / Approve with Conditions / Return for Revision]
```

**Approved By - CISO** (Rows 30-37):
```
Name:               [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Approval Decision:  [Dropdown: Approved / Approved with Conditions / Rejected]
Conditions/Notes:   [Text area - merged cells - yellow]
```

**Next Review Details** (Rows 39-43):
```
Next Review Date:          [Auto-calc: Completion Date + 3 months]
Review Responsible:        [USER INPUT - yellow]
Special Considerations:    [Text area - merged cells - yellow]
```

---

# Cell Styling Reference

## Header Styles

**Main Header** (Sheet titles):

- Font: Calibri 16pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center, middle
- Height: 40px
- Border: None

**Subheader** (Sheet subtitles):

- Font: Calibri 12pt white
- Fill: #4472C4 (medium blue)
- Alignment: Center, middle
- Height: 25px
- Border: None

**Column Header** (Assessment sheets):

- Font: Calibri 10pt bold black
- Fill: #D9D9D9 (light gray)
- Alignment: Center, wrapped
- Height: 30px
- Border: Thin black all sides

## Input Cell Styles

**Yellow Cells** (User input required):

- Fill: #FFFFCC (light yellow)
- Alignment: Left (text) or Center (dropdown), wrapped
- Border: Thin black all sides
- Font: Calibri 10pt regular black

## Status Cell Conditional Formatting

**Status Column (E) in Assessment Sheets**:

| Status Value | Fill Color | Font Color |
|--------------|------------|------------|
| ✅ Compliant | #C6EFCE (light green) | #006100 (dark green) |
| ⚠️ Partial | #FFEB9C (light yellow) | #9C6500 (dark yellow) |
| ❌ Non-Compliant | #FFC7CE (light red) | #9C0006 (dark red) |
| 🔄 Planned | #B4C7E7 (light blue) | #0C5BA0 (dark blue) |
| N/A | #D9D9D9 (light gray) | #7F7F7F (dark gray) |

**Conditional Formatting Rules** (apply to columns E4:E100 in each assessment sheet):
```excel
Rule 1: =E4="✅ Compliant" → Format: Fill #C6EFCE, Font #006100
Rule 2: =E4="⚠️ Partial" → Format: Fill #FFEB9C, Font #9C6500
Rule 3: =E4="❌ Non-Compliant" → Format: Fill #FFC7CE, Font #9C0006
Rule 4: =E4="🔄 Planned" → Format: Fill #B4C7E7, Font #0C5BA0
Rule 5: =E4="N/A" → Format: Fill #D9D9D9, Font #7F7F7F
```

## Freeze Panes

**All Assessment Sheets** (2-7):

- Freeze at: Row 4, Column A
- Effect: Headers (rows 1-3) remain visible when scrolling

**Summary_Dashboard**:

- Freeze at: Row 4, Column A

**Evidence_Register, Gap_Analysis**:

- Freeze at: Row 4, Column A

**Approval_Sign_Off**:

- Freeze at: Row 3, Column A

---

# Python Script Integration Points

## Script Name
`generate_a828_1_sdlc_assessment.py`

## Key Functions

**create_workbook()**:

- Initialize workbook
- Create all 11 sheets
- Return workbook object

**setup_styles()**:

- Define all cell styles (header, input, status)
- Return style dictionary

**create_instructions_sheet(wb)**:

- Populate Instructions sheet with assessment guidance
- **CUSTOMIZE**: Update organizational branding, contact information

**create_assessment_sheet(wb, sheet_name, questions, policy_ref)**:

- Generic function to create assessment sheets
- Parameters:
  - `wb`: Workbook object
  - `sheet_name`: Sheet name (e.g., "Security_Requirements")
  - `questions`: List of question texts
  - `policy_ref`: ISMS-POL-A.8.28 section reference
- Sets up headers, columns, data validation, conditional formatting

**create_summary_dashboard(wb)**:

- Create Summary_Dashboard sheet
- Calculate compliance percentages
- Generate top gaps list
- **CUSTOMIZE**: Adjust compliance thresholds (90% green, 70% yellow, <70% red)

**create_evidence_register(wb)**:

- Create Evidence_Register sheet
- 100 pre-formatted rows
- Auto-generate Evidence IDs

**create_gap_analysis(wb)**:

- Create Gap_Analysis sheet
- Auto-populate from assessment sheets (Status = ❌ or ⚠️)

**create_approval_signoff(wb)**:

- Create Approval_Sign_Off sheet
- User input fields for approval workflow

## Customization Points

Mark customization points in script with comments:

```python
# CUSTOMIZE: Organization name
ORG_NAME = "[Organization]"

# CUSTOMIZE: CISO name and email
CISO_NAME = "Chief Information Security Officer"
CISO_EMAIL = "ciso@organization.com"

# CUSTOMIZE: Compliance thresholds
COMPLIANCE_THRESHOLD_GREEN = 90  # >= 90% is green
COMPLIANCE_THRESHOLD_YELLOW = 70  # 70-89% is yellow
# < 70% is red

# CUSTOMIZE: Status dropdown options (if organization uses different terminology)
STATUS_OPTIONS = [
    "✅ Compliant",
    "⚠️ Partial",
    "❌ Non-Compliant",
    "🔄 Planned",
    "N/A"
]

# CUSTOMIZE: Priority dropdown options
PRIORITY_OPTIONS = ["Critical", "High", "Medium", "Low"]
```

## Quality Assurance

**Script Testing Checklist**:

- [ ] Workbook generates without errors
- [ ] All 11 sheets present and correctly named
- [ ] Data validation dropdowns work (Status, Priority, Evidence Type)
- [ ] Conditional formatting applies correctly (Status colors)
- [ ] Formulas calculate correctly (Summary_Dashboard percentages)
- [ ] Auto-population works (Gap_Analysis pulls from assessment sheets)
- [ ] Freeze panes set correctly
- [ ] File saves with correct naming convention

**Manual Testing** (generate workbook and verify):
1. Open workbook in Excel
2. Navigate to each sheet - no errors?
3. Test dropdown in Status column - options appear?
4. Enter "✅ Compliant" - cell turns green?
5. Enter "❌ Non-Compliant" - cell turns red?
6. Check Summary_Dashboard - percentages calculated?
7. Check Gap_Analysis - non-compliant items appear?
8. Save and re-open - no corruption warnings?

---

# File Naming Convention

**Format**: `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`

**Example**: `ISMS-IMP-A.8.28.1_SDLC_Assessment_20260124.xlsx`

**Components**:

- `ISMS-IMP-A.8.28.1`: Document ID
- `SDLC_Assessment`: Assessment type
- `YYYYMMDD`: Date generated (ISO format for sorting)
- `.xlsx`: Excel format

---

# Quarterly Review Cycle

**Every 3 Months**:
1. Generate new workbook with current date
2. Copy Evidence Register from previous assessment (continuity)
3. Re-assess all domains (don't assume unchanged)
4. Compare to previous quarter:

   - Compliance rate improved/declined?
   - Gaps remediated as planned?
   - New gaps introduced?

5. Update Gap Analysis with progress
6. Obtain fresh approvals
7. Archive previous quarter's assessment
8. Schedule next review (+3 months)

---

**END OF SPECIFICATION**

---

*"Security is a process, not a product. It's also not a destination but a journey."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
