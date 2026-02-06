**ISMS-IMP-A.8.28.2-TG - Standards & Tools Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Coding Standards & Security Tool Implementation |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.2 (Secure Coding Standards), Section 2.3 (Code Review & Testing) |
| **Purpose** | Evaluate implementation and effectiveness of secure coding standards and security tools - deployment AND actual security improvement |
| **Target Audience** | Application Security Team, Security Architects, Development Managers, DevOps Engineers, Tool Administrators, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Tool Changes |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.28.2-UG.

---

# Technical Specification

**Audience:** Workbook developers (Python/Excel script maintainers)

---

# Excel Workbook Structure

## Sheet Overview

The Standards & Tools Assessment workbook consists of 10 sheets:

| Sheet # | Sheet Name | Purpose | Input Type |
|---------|------------|---------|------------|
| 1 | Instructions | Assessment guidance | Read-only |
| 2 | Coding_Standards_Adoption | Standards documentation and adoption | User input |
| 3 | SAST_SCA_Tools | Static analysis and dependency scanning | User input |
| 4 | DAST_Security_Testing_Tools | Dynamic testing and scanning | User input |
| 5 | IDE_Plugins_Linters | Developer-facing tools | User input |
| 6 | Tool_Effectiveness_Metrics | Metrics and KPIs | User input |
| 7 | Summary_Dashboard | Executive overview | Auto-calculated |
| 8 | Evidence_Register | Supporting documentation | User input |
| 9 | Gap_Analysis | Non-compliant items remediation | Auto-populated + user input |
| 10 | Approval_Sign_Off | Formal approval workflow | User input |

## Common Column Structure (Assessment Sheets 2-6)

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | # | 5 | Question number | Auto-number |
| B | Requirement | 60 | Requirement text | Wrapped text |
| C | Policy Reference | 20 | ISMS-POL-A.8.28 section | Text |
| D | Status | 15 | Compliance status | Dropdown |
| E | Evidence/Comments | 50 | Evidence and justification | Wrapped text, yellow fill |
| F | Evidence ID | 15 | Reference to Evidence Register | Text, yellow fill |
| G | Gap Priority | 15 | Priority if Non-Compliant | Dropdown |
| H | Remediation Owner | 20 | Person responsible | Text, yellow fill |
| I | Target Date | 12 | Remediation deadline | Date picker, yellow fill |

---

# Sheet 1: Instructions

## Header Section

**Row 1**: Title row

- Cell A1: "ISMS-IMP-A.8.28.2 – Standards & Tools Assessment"
- Font: Calibri 16pt bold white
- Fill: #003366 (dark blue)
- Merge: A1:I1

**Row 2**: Subtitle row

- Cell A2: "ISO/IEC 27001:2022 - Control A.8.28: Secure Coding"
- Font: Calibri 12pt white
- Fill: #4472C4 (medium blue)
- Merge: A2:I2

## Document Information Block

```
Assessment Document:        ISMS-IMP-A.8.28.2 - Standards & Tools Assessment
Assessment Area:            Secure Coding Standards & Security Tool Implementation
Related Policy:             ISMS-POL-A.8.28 Section 2.2, Section 2.3
Version:                    1.0
Date:                       24.01.2026
Assessment Period:          [USER INPUT - yellow]
Completed By:               [USER INPUT - yellow]
Organization:               [USER INPUT - yellow]
Review Cycle:               Quarterly
Next Review Date:           [Auto-calc: +3 months]
```

## Instructions Content

**Key Message**: Tool deployment ≠ tool effectiveness. This assessment measures BOTH configuration and actual security improvement.

**Anti-Patterns to Avoid**:

- Cargo cult security: Having tools but not using them effectively
- Ignoring false positive rates
- No remediation tracking
- No continuous improvement

---

# Sheets 2-6: Assessment Domain Sheets

## Sheet 2: Coding_Standards_Adoption (18 requirements)

**Requirements**:
1. Standards documented and accessible
2. References OWASP Top 10
3. References CWE Top 25
4. Input validation coverage
5. Output encoding coverage
6. Authentication/session management coverage
7. Cryptography requirements
8. Error handling and logging standards
9. Developer training on standards
10. Standards annually reviewed
11. Language-specific guidelines (Python, Java, JS, etc.)
12. Code examples (secure vs. insecure patterns)
13. Compliance measured
14. Violations identified in code reviews
15. Exception process exists
16. Standards in performance evaluations
17. Security Champions program
18. Onboarding training includes standards

**Policy Reference**: ISMS-POL-A.8.28 Section 2.2

---

## Sheet 3: SAST_SCA_Tools (18 requirements)

**Requirements**:

**SAST** (1-9):
1. SAST tool deployed
2. Language coverage (all primary languages)
3. Automated scans (CI/CD integration)
4. Security rulesets configured
5. Severity prioritization
6. Quality gates block deployment (Critical/High)
7. False positive suppression process
8. Finding tracking (Jira/issue system)
9. Regular triage and review

**SCA** (10-18):
10. SCA tool deployed
11. Dependency scanning automated
12. CI/CD integration
13. CVE detection working
14. License compliance checking
15. SCA quality gates
16. Remediation guidance (upgrade recommendations)
17. Remediation SLAs defined
18. Metrics tracking (vulnerability trends)

**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.1

---

## Sheet 4: DAST_Security_Testing_Tools (18 requirements)

**Requirements**:

**DAST** (1-7):
1. DAST tool deployed
2. Staging environment scans
3. Pre-release scans (before production)
4. OWASP Top 10 testing
5. Authenticated testing
6. Severity classification
7. Remediation tracking

**API Security** (8-10):
8. API security testing tool
9. Authentication testing
10. Input validation/fuzzing

**Container & IaC** (11-15):
11. Container image scanning
12. Base image vulnerability detection
13. IaC scanning (Terraform, CloudFormation)
14. IaC misconfiguration detection
15. Registry integration

**External Testing** (16-18):
16. Annual penetration testing (critical apps)
17. Bug bounty program (if applicable)
18. External test results tracked

**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.2

---

## Sheet 5: IDE_Plugins_Linters (12 requirements)

**Requirements**:

**IDE Plugins** (1-5):
1. IDE security plugins available (VS Code, IntelliJ, etc.)
2. Plugin catalog published
3. Adoption measured (telemetry or survey)
4. Adoption rate >70%
5. Real-time security feedback working

**Linters** (6-8):
6. Code linters with security rules (ESLint, Pylint, RuboCop)
7. Linters enforce standards
8. Linter failures block merges (CI/CD)

**Pre-Commit Hooks** (9-12):
9. Pre-commit hooks deployed (secret detection)
10. Secret detection working (Gitleaks, TruffleHog)
11. Secrets blocked statistics tracked
12. Developer training on secret management

**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.3

---

## Sheet 6: Tool_Effectiveness_Metrics (15 requirements)

**Requirements**:

**KPI Definition** (1-3):
1. Security tool KPIs defined
2. KPIs tracked quarterly
3. KPIs reported to management

**False Positives** (4-6):
4. False positive rate measured (all tools)
5. FP rate <20% (target)
6. Tuning efforts documented

**Remediation** (7-9):
7. MTTR measured by severity
8. MTTR improving over time
9. Remediation SLA compliance tracked

**Coverage** (10-12):
10. Tool coverage measured (% repos, % apps)
11. Coverage >90% (target)
12. Coverage gaps documented

**ROI & Improvement** (13-15):
13. Tool costs documented
14. Vulnerabilities prevented measured
15. Quarterly effectiveness reviews conducted

**Policy Reference**: ISMS-POL-A.8.28 Section 3.3 (Assessment & Verification)

---

# Sheet 7: Summary_Dashboard

## Purpose
Executive-level overview with auto-calculated compliance metrics.

## Layout

**Overall Compliance Summary** (Rows 4-12):

| Metric | Formula | Format |
|--------|---------|--------|
| Total Requirements | Count all requirements across sheets 2-6 | Number |
| Compliant Items | `=COUNTIF(Coding_Standards_Adoption!$D$4:$D$21,"✅ Compliant") + ...` | Number, green |
| Partial Items | `=COUNTIF(Coding_Standards_Adoption!$D$4:$D$21,"⚠️ Partial") + ...` | Number, yellow |
| Non-Compliant Items | `=COUNTIF(Coding_Standards_Adoption!$D$4:$D$21,"❌ Non-Compliant") + ...` | Number, red |
| Planned Items | `=COUNTIF(Coding_Standards_Adoption!$D$4:$D$21,"🔄 Planned") + ...` | Number, blue |
| N/A Items | `=COUNTIF(Coding_Standards_Adoption!$D$4:$D$21,"N/A") + ...` | Number, gray |
| **Overall Compliance Rate** | `=(Compliant / (Total - N/A)) * 100` | Percentage, bold |

**Domain Compliance Breakdown** (Rows 14-21):

| Domain | Total | Compliant | Partial | Non-Compliant | Compliance % |
|--------|-------|-----------|---------|---------------|--------------|
| Coding Standards Adoption | 18 | [Formula] | [Formula] | [Formula] | [Formula] |
| SAST & SCA Tools | 18 | [Formula] | [Formula] | [Formula] | [Formula] |
| DAST Security Testing Tools | 18 | [Formula] | [Formula] | [Formula] | [Formula] |
| IDE Plugins & Linters | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Tool Effectiveness Metrics | 15 | [Formula] | [Formula] | [Formula] | [Formula] |

**Top Gaps** (Rows 23-30):

- Auto-populated from Gap_Analysis (Critical and High priority items)

---

# Sheet 8: Evidence_Register

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Evidence ID | 12 | Auto-generated | `="EV-"&TEXT(ROW()-3,"000")` |
| B | Evidence Description | 50 | What this proves | Wrapped text, yellow |
| C | Related Question | 30 | Which question(s) | Text, yellow |
| D | Evidence Type | 25 | Configuration, Screenshot, Report, etc. | Dropdown, yellow |
| E | Location | 60 | File path or URL | Wrapped text, yellow |
| F | Date Collected | 12 | When captured | Date picker, yellow |
| G | Collected By | 20 | Name of collector | Text, yellow |

**Evidence Type Dropdown**:

- Configuration Export
- Screenshot (Dashboard)
- Tool Report
- Metrics Data
- Documentation
- License File
- Pipeline Config (YAML)
- Other

**Row Count**: 100 rows pre-formatted

---

# Sheet 9: Gap_Analysis

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Gap ID | 10 | Auto-generated | `="GAP-"&TEXT(ROW()-3,"000")` |
| B | Domain | 25 | Assessment domain | Auto-populated |
| C | Requirement | 50 | Requirement text | Auto-populated |
| D | Current Status | 15 | ⚠️ Partial or ❌ Non-Compliant | Auto-populated |
| E | Gap Description | 50 | What's missing | User input, yellow |
| F | Priority | 12 | Critical/High/Medium/Low | Auto-populated |
| G | Remediation Owner | 20 | Person responsible | User input, yellow |
| H | Target Date | 12 | Remediation deadline | Date picker, yellow |
| I | Remediation Status | 18 | Not Started/In Progress/Completed | Dropdown, yellow |
| J | Notes | 40 | Progress updates | User input, yellow |

**Auto-Population**: Scans sheets 2-6, identifies Status = ❌ or ⚠️

---

# Sheet 10: Approval_Sign_Off

## Layout

**Assessment Completed By** (Rows 4-10):
```
Name:               [USER INPUT - yellow]
Role/Title:         [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Signature:          [USER INPUT - yellow]
```

**Reviewed By - Application Security Lead** (Rows 12-19):
**Reviewed By - DevOps/Platform Engineering** (Rows 21-28):
**Approved By - CISO** (Rows 30-37):

(Same structure as ISMS-IMP-A.8.28.1)

**Next Review Details** (Rows 39-43):
```
Next Review Date:          [Auto-calc: +3 months]
Review Responsible:        [USER INPUT - yellow]
```

---

# Cell Styling Reference

(Same styling as ISMS-IMP-A.8.28.1 - headers, input cells, status cells)

---

# Python Script Integration Points

## Script Name
`generate_a828_2_standards_tools.py`

## Key Functions

**create_workbook()**:

- Initialize workbook
- Create all 10 sheets

**create_assessment_sheet(wb, sheet_name, requirements, policy_ref)**:

- Generic function for sheets 2-6
- Parameters: workbook, sheet name, requirements list, policy reference

**create_summary_dashboard(wb)**:

- Auto-calculate compliance metrics
- Domain breakdown
- Top gaps list

## Customization Points

```python
# CUSTOMIZE: Organization name
ORG_NAME = "[Organization]"

# CUSTOMIZE: Tool categories
TOOL_CATEGORIES = [
    "SAST (Static Analysis)",
    "SCA (Dependency Scanning)",
    "DAST (Dynamic Testing)",
    "API Security Testing",
    "Container Scanning",
    "IaC Scanning",
    "IDE Plugin",
    "Linter",
    "Pre-Commit Hook",
    "Other"
]

# CUSTOMIZE: Compliance thresholds
COMPLIANCE_THRESHOLD_GREEN = 90  # >= 90% is green
COMPLIANCE_THRESHOLD_YELLOW = 70  # 70-89% is yellow
# < 70% is red

# CUSTOMIZE: False positive rate target
FP_RATE_TARGET = 20  # Target: <20%

# CUSTOMIZE: Adoption rate target (IDE plugins)
ADOPTION_RATE_TARGET = 70  # Target: >70%
```

---

# File Naming Convention

**Format**: `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`

**Example**: `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_20260124.xlsx`

---

# Quarterly Review Cycle

**Every 3 Months**:
1. Review tool inventory (new tools? deprecated tools?)
2. Update tool configurations (rulesets changed?)
3. Recalculate metrics (false positive rates, MTTR)
4. Update license status (renewals?)
5. Reassess effectiveness (are tools still working?)
6. Review gap remediation progress
7. Obtain fresh approvals

---

**END OF SPECIFICATION**

---

*"The purpose of computing is insight, not numbers."*
— Ron Rivest, after Richard Hamming

<!-- QA_VERIFIED: 2026-02-06 -->
