**ISMS-IMP-A.8.25-26-29.S2-TG - SDLC Security Activities Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | SDLC Security Activities Compliance (A.8.25) |
| **Related Policy** | ISMS-POL-A.8.25-26-29 Section 3 |
| **Purpose** | Assessment of security integration throughout the software development lifecycle, secure coding practices, code review, security tools, and defect management |
| **Target Audience** | Development Managers, Security Champions, DevOps Leads, Security Assessors |
| **Assessment Type** | Application-specific assessment (per application or team) |
| **Review Cycle** | Quarterly for High-Risk applications, Semi-annually for Medium-Risk, Annually for Low-Risk |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial traditional implementation guide | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.25-26-29.S2-UG.

---

# Technical Specification

---

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to PART I (User Completion Guide).

---

# Workbook Overview

## Workbook Metadata

**Filename Format:** `ISMS-A825-SDLC-[APP-ID or TEAM-ID]-[YYYYMMDD].xlsx`

**Example:** `ISMS-A825-SDLC-APP-CUST-PORTAL-20260123.xlsx` or `ISMS-A825-SDLC-TEAM-BACKEND-20260123.xlsx`

**Total Sheets:** 11

**Excel Version:** Excel 2016+ (Office 365 recommended for best formula support)

**File Size Estimate:** 300KB - 1MB depending on metrics and evidence

**Python Script:** `generate_a825_26_29_2_sdlc_security_activities.py`

## Workbook Structure Summary

| Sheet # | Sheet Name | Purpose | User Input | Auto-Calculated | Complexity |
|---------|------------|---------|------------|-----------------|------------|
| 1 | Instructions & Legend | Assessment guidance | None | None | Low |
| 2 | SDLC_Phase_Activities | Security activities by phase | High | Medium | High |
| 3 | Secure_Coding_Standards | Standards compliance | Medium | Medium | Medium |
| 4 | Code_Review_Metrics | Review metrics and quality | Medium | High | High |
| 5 | Security_Tools_Deployment | Tool deployment status | High | Low | Medium |
| 6 | Security_Tools_Usage | Tool usage per application | High | Medium | Medium |
| 7 | Developer_Training | Training completion | Medium | Medium | Medium |
| 8 | Security_Defect_Management | Defect tracking and remediation | Medium | High | High |
| 9 | Compliance_Summary | Overall scoring and gaps | Low | High | High |
| 10 | Evidence_Register | Audit evidence tracking | High | None | Low |
| 11 | Approval_Sign_Off | Stakeholder approval workflow | High | None | Low |

---

# Common Structure Elements

## Standard Column Widths

| Column Type | Width (pixels) | Width (Excel units) |
|-------------|----------------|---------------------|
| ID Column (A) | 60 | 9 |
| Activity/Question | 400-500 | 60-75 |
| Status/Selection | 120-150 | 18-22 |
| Metrics/Numbers | 100-120 | 15-18 |
| Comments/Details | 300-400 | 45-60 |
| Date | 100-120 | 15-18 |

## Standard Row Heights

- **Header Rows:** 30 pixels (auto-adjust for text wrap)
- **Sub-Header Rows:** 25 pixels
- **Data Rows:** 20 pixels (auto-adjust for text wrap)
- **Instruction Rows:** 15 pixels (smaller italic text)

## Standard Colors (Fill)

**Headers:**

- Main Section Header: `RGB(0, 51, 102)` / `#003366` (Dark Blue), Font: White, Bold, 14pt
- Sub-Header: `RGB(68, 114, 196)` / `#4472C4` (Medium Blue), Font: White, Bold, 11pt
- Column Header: `RGB(217, 217, 217)` / `#D9D9D9` (Light Gray), Font: Black, Bold, 10pt

**Input Cells:**

- User Input Required: `RGB(255, 255, 204)` / `#FFFFCC` (Light Yellow)
- Auto-Calculated: `RGB(217, 217, 217)` / `#D9D9D9` (Light Gray) - Protected
- Locked/Read-Only: White background - Protected

**Status Indicators:**

- ✅ Yes/Compliant: `RGB(198, 239, 206)` / `#C6EFCE` (Light Green)
- ⚠️ Partial: `RGB(255, 235, 156)` / `#FFEB9C` (Light Yellow)
- ❌ No/Non-Compliant: `RGB(255, 199, 206)` / `#FFC7CE` (Light Red)
- N/A: `RGB(237, 237, 237)` / `#EDEDED` (Gray)

## Standard Fonts

- **Headers:** Calibri 14pt Bold, White text
- **Sub-Headers:** Calibri 11pt Bold, White text
- **Column Headers:** Calibri 10pt Bold, Black text
- **Body Text:** Calibri 10pt, Black text
- **Instructions:** Calibri 9pt, Italic, Gray `RGB(128, 128, 128)`
- **Comments/Notes:** Calibri 9pt, Italic, Dark Gray `RGB(89, 89, 89)`

## Data Validation Standards

**Yes/No/Partial Dropdowns:**
```excel
List: Yes,No,Partial,N/A
```

**Yes/No Simple:**
```excel
List: Yes,No,N/A
```

**Execution Status:**
```excel
List: ✅ Executed,⚠️ Partial,❌ Not Executed,N/A
```

**Tool Deployment Status:**
```excel
List: Deployed,Partially Deployed,Not Deployed,Planned
```

**Frequency Dropdowns:**
```excel
List: Per Commit,Daily,Weekly,Per Sprint,Per Release,Ad-hoc,Never
```

**Quality Assessment:**
```excel
List: Excellent,Good,Adequate,Poor,N/A
```

**Severity Dropdowns:**
```excel
List: Critical,High,Medium,Low
```

## Cell Protection

**Protected Sheets:**

- All sheets fully protected
- Password: [Organization-specific]
- Allow: Select unlocked cells, Format cells, AutoFilter

**Unlocked Cells:**

- All yellow input cells (user data entry)
- Comment cells
- Metrics input cells (where user enters counts)

**Locked Cells:**

- All gray auto-calculated cells
- All formulas
- All headers and instructions

---

# Sheet 1: Application/Team Profile

## Sheet Purpose
Document basic information about application or development team being assessed.

## Sheet Structure

### Columns
| Col | Column Name | Width | Format | Input Type | Protection |
|-----|-------------|-------|--------|------------|------------|
| A | Field | 30 | Text, Bold | Read-Only | Locked |
| B | Value | 60 | Text/Dropdown/Date | User Input | Unlocked |
| C | Comments | 45 | Text, Italic | User Input | Unlocked |

### Rows (Data Section)

| Row | Field | Column B Input Type | Column C |
|-----|-------|---------------------|----------|
| 1-2 | Header | "SHEET 1: APPLICATION/TEAM PROFILE" [Merge B1:C1] | - |
| 3 | Instruction | [Merge A3:C3] "Complete basic application/team information" | - |
| 4 | Blank | - | - |
| 5 | Section: Identification | - | - |
| 6 | Application/Team ID | Text | "Unique identifier" |
| 7 | Application/Team Name | Text | "Full name" |
| 8 | Description | Text, Wrap | "Brief description" |
| 9 | Development Manager | Text | "Name, email" |
| 10 | Security Champion | Text | "Name, email (if exists, else N/A)" |
| 11 | Team Size (Developers) | Number | "Active developers count" |
| 12 | Blank | - | - |
| 13 | Section: Development Context | - | - |
| 14 | Development Methodology | Dropdown | See Methodology dropdown |
| 15 | Sprint Length (if Agile) | Dropdown | See Sprint Length dropdown |
| 16 | Release Frequency | Dropdown | See Release Frequency dropdown |
| 17 | Technology Stack | Text, Wrap | "Languages, frameworks, platforms" |
| 18 | Version Control System | Dropdown | See VCS dropdown |
| 19 | CI/CD Platform | Dropdown | See CI/CD dropdown |
| 20 | Blank | - | - |
| 21 | Section: Risk Classification | - | - |
| 22 | Application Risk Level | Dropdown | See Risk Level dropdown |
| 23 | SDLC Security Requirements | Formula | Auto-calculated based on risk |
| 24 | Blank | - | - |
| 25 | Section: Assessment Context | - | - |
| 26 | Assessment Date | Date | "YYYY-MM-DD" |
| 27 | Assessment Period | Text | "e.g., Q4 2025, Last 6 months" |
| 28 | Previous Assessment Date | Date | "YYYY-MM-DD or N/A" |

### Dropdowns

**Development Methodology:**
```excel
List: Waterfall,Agile (Scrum),Agile (Kanban),DevOps,DevSecOps,Hybrid,Other
```

**Sprint Length:**
```excel
List: 1 week,2 weeks,3 weeks,4 weeks,N/A (not Agile)
```

**Release Frequency:**
```excel
List: Continuous (per commit),Daily,Weekly,Bi-weekly,Monthly,Quarterly,Annually,Ad-hoc
```

**Version Control System:**
```excel
List: Git,SVN,Mercurial,Perforce,Other
```

**CI/CD Platform:**
```excel
List: Jenkins,GitLab CI,GitHub Actions,Azure DevOps,CircleCI,Travis CI,TeamCity,Bamboo,Other,None
```

**Risk Level:**
```excel
List: High Risk,Medium Risk,Low Risk
```

### Formulas

**Cell B23** (SDLC Security Requirements):
```excel
=IF(B22="High Risk","All security activities mandatory",IF(B22="Medium Risk","Core security activities required",IF(B22="Low Risk","Basic security activities required","Not classified")))
```

### Conditional Formatting

**Cell B22** (Risk Level):

- If "High Risk" → Red background `RGB(255, 199, 206)`, Bold
- If "Medium Risk" → Yellow background `RGB(255, 235, 156)`, Bold
- If "Low Risk" → Green background `RGB(198, 239, 206)`, Bold

---

# Sheet 2: SDLC Phase Security Activities

## Sheet Purpose
Assess security activities integration in each SDLC phase.

## Sheet Structure

### Section Structure

For each of 6 SDLC phases (Requirements, Design, Development, Testing, Deployment, Maintenance), create a section with:

- Phase header
- Security activities list
- Assessment columns: Planned?, Executed?, Evidence?, Comments

### Columns

| Col | Column Name | Width | Format | Input Type | Protection |
|-----|-------------|-------|--------|------------|------------|
| A | # | 5 | Text | Read-Only | Locked |
| B | Security Activity | 50 | Text | Read-Only | Locked |
| C | Planned? | 12 | Dropdown | User Input | Unlocked |
| D | Executed? | 12 | Dropdown | User Input | Unlocked |
| E | Evidence? | 12 | Dropdown | User Input | Unlocked |
| F | Comments | 45 | Text, Wrap | User Input | Unlocked |

### Phase 1: Requirements (Rows 5-10)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 5 | 1.1 | Security requirements identified | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 6 | 1.2 | Initial threat identification | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 7 | 1.3 | Data classification determined | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 8 | 1.4 | Compliance requirements identified | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 9 | 1.5 | Security acceptance criteria defined | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase 2: Design (Rows 12-17)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 12 | 2.1 | Threat modeling conducted | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 13 | 2.2 | Security architecture review | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 14 | 2.3 | Security design patterns applied | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 15 | 2.4 | Third-party component security assessment | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 16 | 2.5 | Security design decisions documented | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase 3: Development (Rows 19-26)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 19 | 3.1 | Secure coding standards followed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 20 | 3.2 | Code review conducted (peer + security) | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 21 | 3.3 | SAST scans executed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 22 | 3.4 | SCA scans executed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 23 | 3.5 | Secret scanning performed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 24 | 3.6 | Security unit tests written | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 25 | 3.7 | Security defects tracked and remediated | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase 4: Testing (Rows 28-33)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 28 | 4.1 | Security test cases executed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 29 | 4.2 | DAST scans performed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 30 | 4.3 | Security acceptance testing | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 31 | 4.4 | Penetration testing (if required) | Yes/No/N/A | ✅/⚠️/❌/N/A | Yes/No/N/A | User comments |
| 32 | 4.5 | Security regression testing | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 33 | 4.6 | Vulnerability remediation verified | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase 5: Deployment (Rows 35-40)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 35 | 5.1 | Production security configuration reviewed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 36 | 5.2 | Deployment security checklist completed | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 37 | 5.3 | Security monitoring configured | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 38 | 5.4 | Security logging enabled | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 39 | 5.5 | Encryption validated | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 40 | 5.6 | Security sign-off obtained | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase 6: Maintenance (Rows 42-47)

| Row | # | Security Activity | Planned? | Executed? | Evidence? | Comments |
|-----|---|------------------|----------|-----------|-----------|----------|
| 42 | 6.1 | Security patches applied within SLA | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 43 | 6.2 | Vulnerability monitoring active | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 44 | 6.3 | Security incidents investigated | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 45 | 6.4 | Threat model updated when app changes | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |
| 46 | 6.5 | Periodic security assessments conducted | Yes/No | ✅/⚠️/❌ | Yes/No | User comments |

### Phase Scoring Section (Rows 49-56)

| Row | Phase | Activities Planned | Activities Executed | Phase Completeness |
|-----|-------|-------------------|--------------------|--------------------|
| 49 | Phase 1: Requirements | [Formula] | [Formula] | [Formula] |
| 50 | Phase 2: Design | [Formula] | [Formula] | [Formula] |
| 51 | Phase 3: Development | [Formula] | [Formula] | [Formula] |
| 52 | Phase 4: Testing | [Formula] | [Formula] | [Formula] |
| 53 | Phase 5: Deployment | [Formula] | [Formula] | [Formula] |
| 54 | Phase 6: Maintenance | [Formula] | [Formula] | [Formula] |
| 55 | Blank | - | - | - |
| 56 | **Overall SDLC Security Integration** | - | - | [Formula: Average] |

### Formulas

**Cell C49** (Phase 1 Activities Planned):
```excel
=COUNTIF(C5:C9,"Yes")
```

**Cell D49** (Phase 1 Activities Executed):
```excel
=COUNTIF(D5:D9,"✅ Executed")
```

**Cell E49** (Phase 1 Completeness):
```excel
=IF(C49>0, ROUND((D49/C49)*100, 1) & "%", "N/A")
```

*Repeat pattern for rows 50-54 (Phases 2-6)*

**Cell E56** (Overall SDLC Security Integration):
```excel
=ROUND(AVERAGE(VALUE(LEFT(E49,LEN(E49)-1)), VALUE(LEFT(E50,LEN(E50)-1)), VALUE(LEFT(E51,LEN(E51)-1)), VALUE(LEFT(E52,LEN(E52)-1)), VALUE(LEFT(E53,LEN(E53)-1)), VALUE(LEFT(E54,LEN(E54)-1))), 1) & "%"
```

### Conditional Formatting

**Cells E49:E54** (Phase Completeness):

- If ≥90% → Green background
- If 70-89% → Yellow background
- If <70% → Red background

**Cell E56** (Overall Score):

- If ≥90% → Green background, Bold
- If 70-89% → Yellow background, Bold
- If <70% → Red background, Bold

---

# Sheet 3: Secure Coding Standards Compliance

## Sheet Purpose
Assess secure coding standards adoption and adherence.

## Sheet Structure

### Section A: Standards Existence (Rows 5-10)

| Row | Field | Column B Input Type |
|-----|-------|---------------------|
| 5 | Standards Documented? | Dropdown: Yes,No |
| 6 | Standards Location | Text (URL) |
| 7 | Standards Format | Dropdown: Document,Wiki,Tool Config,Other |
| 8 | Standards Alignment | Dropdown: OWASP Top 10,CWE Top 25,Language-specific,POL-A.8.28,Multiple |
| 9 | Last Updated | Date |

### Section B: Standards Content (Rows 12-22)

| Row | # | Content Area | Addressed? | Comments |
|-----|---|--------------|------------|----------|
| 12 | 1 | Input validation | Yes/No/Partial | User comments |
| 13 | 2 | Authentication | Yes/No/Partial | User comments |
| 14 | 3 | Authorization | Yes/No/Partial | User comments |
| 15 | 4 | Cryptography | Yes/No/Partial | User comments |
| 16 | 5 | Error handling | Yes/No/Partial | User comments |
| 17 | 6 | Logging | Yes/No/Partial | User comments |
| 18 | 7 | Data protection | Yes/No/Partial | User comments |
| 19 | 8 | API security | Yes/No/Partial | User comments |
| 20 | 9 | Dependency management | Yes/No/Partial | User comments |
| 21 | 10 | Language-specific secure coding | Yes/No/Partial | User comments |

### Section C: Developer Awareness (Rows 24-28)

| Row | Question | Response | Comments |
|-----|----------|----------|----------|
| 24 | Developers know standards exist? | All/Some/None | User comments |
| 25 | Developers have read standards? | All/Some/None | User comments |
| 26 | Developers reference during coding? | Regularly/Sometimes/Rarely/Never | User comments |
| 27 | Developers find standards helpful? | Yes/Partially/No | User comments |

### Section D: Compliance Verification (Rows 30-36)

| Row | # | Verification Method | Used? | Comments |
|-----|---|-------------------|-------|----------|
| 30 | 1 | Code review (peer) | Yes/No | User comments |
| 31 | 2 | Security-focused code review | Yes/No | User comments |
| 32 | 3 | SAST tool | Yes/No | User comments |
| 33 | 4 | IDE plugins | Yes/No | User comments |
| 34 | 5 | Manual security audits | Yes/No | User comments |
| 35 | 6 | No verification | Yes/No | User comments |

### Section E: Violation Tracking (Rows 38-42)

| Row | Field | Response | Comments |
|-----|-------|----------|----------|
| 38 | Violations tracked? | Yes/No | User comments |
| 39 | Tracking system | Text | User enters system name |
| 40 | Violation trends | Increasing/Stable/Decreasing/Unknown | User selects |
| 41 | Common violations | Text, Wrap | User lists top 3-5 |

### Section F: Scoring (Rows 44-50)

| Row | Metric | Score | Interpretation |
|-----|--------|-------|----------------|
| 44 | Standards Existence | [Formula: 0-100%] | - |
| 45 | Standards Content Completeness | [Formula: 0-100%] | - |
| 46 | Developer Awareness | [Formula: 0-100%] | - |
| 47 | Compliance Verification | [Formula: 0-100%] | - |
| 48 | Violation Tracking | [Formula: 0-100%] | - |
| 49 | Blank | - | - |
| 50 | **Secure Coding Standards Maturity** | [Formula: Average] | [Formula] |

### Formulas

**Cell B44** (Standards Existence):
```excel
=IF(B5="Yes", 100, 0) & "%"
```

**Cell B45** (Standards Content Completeness):
```excel
=ROUND((COUNTIF(C12:C21,"Yes") / COUNTA(C12:C21)) * 100, 1) & "%"
```

**Cell B46** (Developer Awareness):
```excel
=IF(B24="All",100,IF(B24="Some",50,IF(B24="None",0,0))) & "%"
```
*(Simplified - actual formula would weight all awareness questions)*

**Cell B47** (Compliance Verification):
```excel
=ROUND((COUNTIF(C30:C35,"Yes") / 5) * 100, 1) & "%"
```
*(Divide by 5, not 6, because "No verification" should count against score)*

**Cell B48** (Violation Tracking):
```excel
=IF(B38="Yes", 100, 0) & "%"
```

**Cell B50** (Overall Maturity):
```excel
=ROUND(AVERAGE(VALUE(LEFT(B44,LEN(B44)-1)), VALUE(LEFT(B45,LEN(B45)-1)), VALUE(LEFT(B46,LEN(B46)-1)), VALUE(LEFT(B47,LEN(B47)-1)), VALUE(LEFT(B48,LEN(B48)-1))), 1) & "%"
```

---

# Sheet 4: Code Review Execution

## Sheet Purpose
Assess code review execution (peer review and security-focused review).

## Sheet Structure

### Section A: Peer Review Process (Rows 5-10)

| Row | Field | Response |
|-----|-------|----------|
| 5 | Code review required? | Yes/No |
| 6 | Policy documented? | Text (location) |
| 7 | Review tool | Dropdown: GitHub,GitLab,Azure DevOps,Gerrit,Crucible,Other |
| 8 | Enforcement | Dropdown: Automated,Manual,Honor System,None |

### Section B: Peer Review Metrics (Rows 12-18)

| Row | Metric | Value | Comments |
|-----|--------|-------|----------|
| 12 | Assessment period | Text | e.g., "Last 3 months" |
| 13 | Total code changes (PRs/MRs) | Number | User enters count |
| 14 | Code reviews completed | Number | User enters count |
| 15 | Code review compliance rate | Formula | Auto-calculated |
| 16 | Average review time (hours) | Number | User enters |
| 17 | Average comments per review | Number | User enters |

### Section C: Security-Focused Review (Rows 20-25)

| Row | Field | Response |
|-----|-------|----------|
| 20 | Security review required? | Dropdown: Yes (all code),Yes (high-risk only),Recommended,No |
| 21 | High-risk code defined? | Yes/No |
| 22 | Security reviewer | Dropdown: Security Champion,Security Architect,Security Team,None |

### Section D: Security Review Metrics (Rows 27-32)

| Row | Metric | Value | Comments |
|-----|--------|-------|----------|
| 27 | High-risk code changes | Number | User enters |
| 28 | Security reviews completed | Number | User enters |
| 29 | Security review compliance rate | Formula | Auto-calculated |
| 30 | Security findings identified | Number | User enters |
| 31 | Findings remediated | Number | User enters |

### Section E: Review Quality Assessment (Rows 34-38)

| Row | Question | Response | Comments |
|-----|----------|----------|----------|
| 34 | Security issues identified in reviews? | Regularly/Sometimes/Rarely/No | User selects |
| 35 | Security comments specific? | Yes/No | User selects |
| 36 | Findings tracked? | Yes/No | User selects |
| 37 | Findings verified fixed? | Yes/No | User selects |

### Section F: Scoring (Rows 40-45)

| Row | Metric | Score | Interpretation |
|-----|--------|-------|----------------|
| 40 | Peer Review Compliance | [Formula] | - |
| 41 | Peer Review Quality | [Formula] | - |
| 42 | Security Review Compliance | [Formula] | - |
| 43 | Security Review Quality | [Formula] | - |
| 44 | Blank | - | - |
| 45 | **Code Review Maturity Score** | [Formula] | [Formula] |

### Formulas

**Cell B15** (Code Review Compliance Rate):
```excel
=IF(B13>0, ROUND((B14/B13)*100, 1) & "%", "N/A")
```

**Cell B29** (Security Review Compliance Rate):
```excel
=IF(B27>0, ROUND((B28/B27)*100, 1) & "%", "N/A")
```

**Cell B40** (Peer Review Compliance Score):
```excel
=VALUE(LEFT(B15,LEN(B15)-1))
```
*(Extracts percentage value)*

**Cell B41** (Peer Review Quality - simplified):
```excel
=IF(AND(B16<=24, B17>=3), 100, IF(AND(B16<=48, B17>=2), 70, IF(B17>=1, 50, 0))) & "%"
```
*(Quality based on review time <24hrs and comments ≥3)*

**Cell B42** (Security Review Compliance):
```excel
=VALUE(LEFT(B29,LEN(B29)-1))
```

**Cell B43** (Security Review Quality - simplified):
```excel
=IF(AND(B34="Regularly", B35="Yes", B36="Yes", B37="Yes"), 100, IF(B34="Sometimes", 70, IF(B34="Rarely", 40, 0))) & "%"
```

**Cell B45** (Overall Code Review Maturity):
```excel
=ROUND(AVERAGE(VALUE(LEFT(B40,LEN(B40)-1)), VALUE(LEFT(B41,LEN(B41)-1)), VALUE(LEFT(B42,LEN(B42)-1)), VALUE(LEFT(B43,LEN(B43)-1))), 1) & "%"
```

---

# Sheet 5: Security Tools Deployment

## Sheet Purpose
Assess security tools deployment and usage.

## Sheet Structure

*(Similar detailed structure for SAST, SCA, Secret Scanning, IDE Plugins sections)*

**Key Sections:**

- A. SAST Tool (Rows 5-25)
- B. SCA Tool (Rows 27-45)
- C. Secret Scanning (Rows 47-55)
- D. IDE Security Plugins (Rows 57-62)
- E. Scoring (Rows 64-70)

**Each tool section includes:**

- Tool deployed? (Yes/No)
- Tool name
- Configuration details
- Execution frequency
- Metrics (scans, findings, remediation)
- Deployment score

---

# Sheet 6: Security Tools Usage

## Sheet Purpose
Track security tool usage metrics per application.

## Sheet Structure

### Columns
| Col | Column Name | Width | Format | Input Type | Protection |
|-----|-------------|-------|--------|------------|------------|
| A | Application Name | 25 | Text | Read-Only/User | Unlocked |
| B | SAST Scans Per Month | 20 | Number | User Input | Unlocked |
| C | SCA Scans Per Month | 20 | Number | User Input | Unlocked |
| D | Secret Scanning Enabled? | 20 | Dropdown | User Input | Unlocked |
| E | DAST Scans Per Release | 20 | Number | User Input | Unlocked |
| F | Avg Remediation Time (days) | 20 | Number | User Input | Unlocked |
| G | Tool Integration Score | 20 | Dropdown | User Input | Unlocked |
| H | Usage Compliance (%) | 20 | Formula | Auto-Calculated | Locked |

### Data Validation

**Column D (Secret Scanning Enabled?):**
```excel
List: Yes,No
```

**Column G (Tool Integration Score):**
```excel
List: Excellent,Good,Adequate,Poor
```

### Formulas

**Column H (Usage Compliance %):**
```excel
=(IF(B{row}>=4,25,0)+IF(C{row}>=4,25,0)+IF(D{row}="Yes",25,0)+IF(E{row}>=1,25,0))
```
- SAST ≥4 scans/month = 25%
- SCA ≥4 scans/month = 25%
- Secret Scanning enabled = 25%
- DAST ≥1 scan/release = 25%

### Sample Data

| Application Name | SAST | SCA | Secrets | DAST | Remediation | Integration | Compliance |
|-----------------|------|-----|---------|------|-------------|-------------|------------|
| Customer Portal | 20 | 20 | Yes | 2 | 5.5 | Excellent | 100% |
| Internal HR System | 8 | 8 | Yes | 1 | 12.0 | Good | 100% |
| Marketing Website | 16 | 16 | Yes | 4 | 3.2 | Excellent | 100% |

---

# Sheet 7: Developer_Training

## Sheet Purpose
Assess developer security training completion and effectiveness.

## Sheet Structure

**Key Sections:**

- A. Training Requirements (Rows 5-10)
- B. Training Delivery (Rows 12-16)
- C. Training Completion Tracking (Rows 18-24)
- D. Training Effectiveness (Rows 26-32)
- E. Just-in-Time Training (Rows 34-38)
- F. Scoring (Rows 40-46)

---

# Sheet 7: Security Defect Management

## Sheet Purpose
Assess security defect tracking and remediation.

## Sheet Structure

**Key Sections:**

- A. Defect Tracking Process (Rows 5-10)
- B. Defect Sources (Rows 12-18)
- C. Remediation SLAs (Rows 20-24)
- D. Open Defects Snapshot (Rows 26-34)
- E. Remediation Metrics (Rows 36-48)
- F. Security Technical Debt (Rows 50-54)
- G. Scoring (Rows 56-62)

**Key Formulas:**

- SLA compliance rate
- Average remediation time by severity
- Overdue defect count
- Technical debt age

---

# Sheet 9: Compliance_Summary

## Sheet Purpose
Calculate overall SDLC security compliance scores and identify gaps.

## Sheet Structure

### Section A: Maturity Scores (Rows 5-14)

| Row | Assessment Area | Score (from other sheets) | Interpretation |
|-----|----------------|---------------------------|----------------|
| 5 | SDLC Phase Activities | =Sheet2!E56 | [Formula] |
| 6 | Secure Coding Standards | =Sheet3!B50 | [Formula] |
| 7 | Code Review Execution | =Sheet4!B45 | [Formula] |
| 8 | Security Tools Deployment | =Sheet5!B70 | [Formula] |
| 9 | Developer Security Training | =Sheet6!B46 | [Formula] |
| 10 | Security Defect Management | =Sheet7!B62 | [Formula] |
| 11 | Blank | - | - |
| 12 | **Overall SDLC Security Maturity** | [Formula: Average] | [Formula] |

### Formulas

**Cell B12** (Overall Maturity):
```excel
=ROUND(AVERAGE(VALUE(LEFT(B5,LEN(B5)-1)), VALUE(LEFT(B6,LEN(B6)-1)), VALUE(LEFT(B7,LEN(B7)-1)), VALUE(LEFT(B8,LEN(B8)-1)), VALUE(LEFT(B9,LEN(B9)-1)), VALUE(LEFT(B10,LEN(B10)-1))), 1) & "%"
```

**Cell C12** (Interpretation):
```excel
=IF(VALUE(LEFT(B12,LEN(B12)-1))>=90,"Level 4-5: Quantitatively Managed/Optimizing",IF(VALUE(LEFT(B12,LEN(B12)-1))>=70,"Level 3: Defined",IF(VALUE(LEFT(B12,LEN(B12)-1))>=50,"Level 2: Managed","Level 1: Initial/Ad Hoc")))
```

### Section B: Gap Summary (Rows 16-22)

Auto-populated with lowest 5 scoring areas from Sheets 2-7.

### Section C: Improvement Recommendations (Rows 24-50)

Table structure for recommendations with columns:

- Gap Area
- Current State
- Target State
- Recommendation
- Effort (Low/Medium/High)
- Priority (P1/P2/P3/P4)

---

# Sheet 10: Evidence_Register

## Sheet Purpose
Centralized register of all SDLC security evidence for audit readiness.

## Sheet Structure

### Columns
| Col | Column Name | Width | Format | Input Type | Protection |
|-----|-------------|-------|--------|------------|------------|
| A | Evidence Type | 25 | Text | User Input | Unlocked |
| B | Application/Team Name | 25 | Text | User Input | Unlocked |
| C | Document Title/Description | 35 | Text, Wrap | User Input | Unlocked |
| D | Document Location/Link | 45 | Text/Hyperlink | User Input | Unlocked |
| E | Last Updated | 15 | Date | User Input | Unlocked |
| F | Owner | 20 | Text | User Input | Unlocked |
| G | Status | 15 | Dropdown | User Input | Unlocked |

### Data Validation

**Column G (Status):**
```excel
List: Current,Outdated,Missing
```

### Evidence Types
- SDLC Checklist
- Code Review Record
- SAST Report
- SCA Report
- Training Certificate
- Security Champion Meeting
- Threat Model
- Security Architecture Review

### Sample Data

| Type | Application | Title | Location | Updated | Owner | Status |
|------|-------------|-------|----------|---------|-------|--------|
| SDLC Checklist | Customer Portal | Sprint Security Checklist | /docs/sdlc/APP-001-checklist.xlsx | 2025-01-14 | Dev Lead | Current |
| Code Review Record | Customer Portal | GitLab MR Dashboard | https://gitlab.com/app-001/merge_requests | 2025-01-15 | Dev Team | Current |
| SAST Report | Customer Portal | SonarQube Security Report | /reports/sast/APP-001-202412.pdf | 2024-12-31 | Security Team | Current |

---

# Sheet 11: Approval_Sign_Off

## Sheet Purpose
Stakeholder review and approval workflow for the assessment.

## Sheet Structure

### Section A: Assessment Information (Rows 4-8)

| Row | Field | Input Type |
|-----|-------|------------|
| 4 | Assessment Date | Date (User Input) |
| 5 | Assessed By | Text (User Input) |
| 6 | Organization | Text (User Input) |
| 7 | Assessment Period | Text (e.g., Q1 2025) |
| 8 | Total Applications Assessed | Number |

### Section B: Approval Sign-Off Table

**Columns:**
| Col | Column Name | Width | Input Type |
|-----|-------------|-------|------------|
| A | Approver Name | 30 | User Input |
| B | Role/Title | 30 | Read-Only |
| C | Date | 15 | User Input |
| D | Signature | 25 | User Input |
| E | Comments | 40 | User Input |

**Required Approvers:**
1. Security Architect
2. Development Manager
3. DevOps Lead
4. CISO / Security Leadership

### Section C: Overall Compliance Determination

| Field | Input Type |
|-------|------------|
| Overall SDLC Compliance Status | Dropdown: ✅ Compliant, ⚠️ Partial Compliance, ❌ Non-Compliant |
| Overall Compliance Score | Percentage (X%) |

### Cell Formatting
- All user input cells: Yellow fill `RGB(255, 255, 204)`
- Role/Title column: White background (pre-filled)
- Headers: Standard subheader style

---

# Python Script Integration Notes

## Script Name
`generate_a825_26_29_2_sdlc_security_activities.py`

## Key Script Functions

1. **create_workbook()**: Initialize Excel workbook with 11 sheets
2. **apply_common_formatting()**: Apply standard colors, fonts, borders
3. **add_data_validation()**: Add all dropdowns and validation rules
4. **add_formulas()**: Add all calculated fields
5. **apply_conditional_formatting()**: Add all conditional formatting rules
6. **protect_sheets()**: Lock all sheets
7. **save_workbook()**: Save with proper filename format

## Critical Implementation Notes

**UTF-8 Encoding:**

- Use `openpyxl` library with UTF-8 encoding
- Test emoji rendering (✅⚠️❌)
- Verify special characters display correctly

**Formula Testing:**

- Test all percentage calculations
- Verify cross-sheet references work (Sheet2!E56, Sheet3!B50, etc.)
- Test average formulas with VALUE() and LEFT() string manipulation
- Verify conditional logic (IF statements)

**Data Validation:**

- Verify all dropdowns work
- Test that invalid entries are rejected
- Check dropdown lists are complete

**Conditional Formatting:**

- Verify color rules apply correctly
- Test that formatting updates when cells change
- Check thresholds (90%, 70%, 50%)

**Sheet Protection:**

- Verify only yellow cells are unlocked
- Test that formulas cannot be edited
- Confirm password protection works

**Performance:**

- Workbook should generate in <10 seconds
- File size should be <1MB
- Opening workbook should be fast (<5 seconds)

---

# Quality Assurance Checklist

## Pre-Deployment QA

**Workbook Structure:**

- [ ] All 8 sheets present and named correctly
- [ ] All headers formatted consistently
- [ ] All column widths set appropriately
- [ ] No hidden rows or columns

**Data Validation:**

- [ ] All dropdowns functional
- [ ] Dropdown lists complete and accurate
- [ ] Invalid entries rejected

**Formulas:**

- [ ] All formulas calculate correctly
- [ ] No #REF!, #VALUE!, #DIV/0! errors
- [ ] Cross-sheet references work
- [ ] Percentage calculations display correctly

**Conditional Formatting:**

- [ ] All status indicators display correct colors
- [ ] Score thresholds trigger correct colors
- [ ] Formatting persists when cells updated

**Protection:**

- [ ] All sheets protected
- [ ] Only yellow cells unlocked
- [ ] Formulas locked and protected
- [ ] Password protection works

**Usability:**

- [ ] Instructions clear
- [ ] No placeholder text remains
- [ ] Professional appearance
- [ ] Print preview looks good

**Testing:**

- [ ] Complete full assessment with test data
- [ ] Verify all calculations accurate
- [ ] Test on Windows and Mac
- [ ] Test in Excel 2016 and Office 365

---

**END OF SPECIFICATION**

---

*"Mathematics is the queen of the sciences and number theory is the queen of mathematics."*
— Attributed to Ramanujan, after Gauss

<!-- QA_VERIFIED: 2026-02-06 -->
