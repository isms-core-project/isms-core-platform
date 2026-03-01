<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.25-26-29.S3-UG:framework:UG:a.8.25-26-29 -->
**ISMS-IMP-A.8.25-26-29.S3-UG - Security Testing Results Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Testing Results Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.25-26-29.S3-UG |
| **Related Policy** | ISMS-POL-A.8.25-26-29 (Secure Development) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.25 (Secure Development Life Cycle) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.25-26-29 (Secure Development)
- ISMS-IMP-A.8.25-26-29.S1 (Security Requirements Assessment)
- ISMS-IMP-A.8.25-26-29.S2 (SDLC Security Activities Assessment)
- ISMS-IMP-A.8.25-26-29.S4 (Vulnerability Remediation Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.25-26-29-S3-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Security Testing Coverage | Assess coverage of security testing across applications |
| 3 | SAST Scan Results | Static application security testing results and findings |
| 4 | DAST Scan Results | Dynamic application security testing results and findings |
| 5 | SCA Scan Results | Software composition analysis scan results and findings |
| 6 | Penetration Testing Results | Penetration testing engagement findings and remediation status |
| 7 | Security Acceptance Testing | Security acceptance testing criteria and results |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.25-26-29-S3 - Security Testing Results Assessment

**What This Assessment Evaluates:**

- SAST (Static Application Security Testing) execution and results
- DAST (Dynamic Application Security Testing) execution and results
- SCA (Software Composition Analysis) execution and results
- IAST (Interactive Application Security Testing) execution and results (if applicable)
- Penetration testing execution and results
- Security acceptance testing execution
- Overall security testing coverage and effectiveness
- Finding severity distribution and remediation

**This Assessment is For:**

- Individual applications (assessing security testing coverage)
- Development teams (assessing testing practices)
- Evaluating WHAT testing was done and WHAT was found
- Measuring security testing effectiveness

**This Assessment is NOT For:**

- Security requirements specification (see IMP-S1)
- SDLC security activities process (see IMP-S2)
- Vulnerability remediation tracking (see IMP-S4 - this focuses on remediation workflow)
- Portfolio-wide status tracked in each workbook's Summary Dashboard (S1–S4)

## Assessment Workbook Structure

**Total Sheets:** 10

**Completion Sequence:**

1. **Instructions & Legend** - Assessment guidance, color legend, and completion instructions
2. **Security_Testing_Coverage** - Testing coverage status per application
3. **SAST_Scan_Results** - Static analysis scan results and findings
4. **DAST_Scan_Results** - Dynamic analysis scan results and findings
5. **SCA_Scan_Results** - Dependency vulnerability scan results
6. **Penetration_Testing_Results** - Penetration testing and interactive testing results
7. **Security_Acceptance_Testing** - Security test cases and acceptance criteria
8. **Compliance_Summary** - Overall testing compliance scores
9. **Evidence_Register** - Centralized audit evidence tracking
10. **Approval_Sign_Off** - Stakeholder review and approval workflow

**Estimated Completion Time:**

- High-Risk Application: 3-4 hours
- Medium-Risk Application: 2-3 hours
- Low-Risk Application: 1-2 hours

## Key Assessment Questions

This assessment answers:

- ✅ What security testing was performed? (SAST, DAST, SCA, pen test, etc.)
- ✅ How often is security testing executed?
- ✅ What vulnerabilities were found? (severity distribution)
- ✅ What is the testing coverage? (code coverage, attack surface coverage)
- ✅ Are findings triaged and remediated?
- ✅ What is the overall security posture based on testing results?
- ✅ What testing gaps exist?

---

# Prerequisites

## Required Information

**Before starting assessment, gather:**

**Application Information:**

- [ ] Application name and ID
- [ ] Application risk classification (from IMP-S1)
- [ ] Application technology stack
- [ ] Application owner contact
- [ ] Security testing requirements (based on risk level)

**Testing Period:**

- [ ] Assessment period (e.g., Q4 2025, Last 6 months)
- [ ] Number of releases/sprints in period
- [ ] Testing milestones (when were tests executed?)

**SAST Tool Access:**

- [ ] SAST tool name (SonarQube, Checkmarx, Fortify, etc.)
- [ ] Access to SAST dashboard
- [ ] Latest SAST scan results
- [ ] Historical SAST scan data
- [ ] SAST finding export/reports

**DAST Tool Access:**

- [ ] DAST tool name (OWASP ZAP, Burp Suite, Acunetix, etc.)
- [ ] Access to DAST dashboard
- [ ] Latest DAST scan results
- [ ] DAST finding export/reports

**SCA Tool Access:**

- [ ] SCA tool name (Snyk, Dependabot, WhiteSource, etc.)
- [ ] Access to SCA dashboard
- [ ] Vulnerable dependency list
- [ ] SCA finding export/reports

**Penetration Testing:**

- [ ] Pen test reports (if conducted in assessment period)
- [ ] Pen test executive summary
- [ ] Pen test findings list
- [ ] Remediation evidence

**Security Test Cases:**

- [ ] Security test plan (if exists)
- [ ] Security test case repository (Jira, TestRail, etc.)
- [ ] Security acceptance criteria documentation
- [ ] Test execution results

## Required Tools

**Excel Workbook:**

- Excel 2016 or later (Office 365 recommended)

**Evidence Collection:**

- Screenshot tool
- Access to testing tool dashboards
- PDF reader (for pen test reports)

**Optional:**

- API access to SAST/DAST/SCA tools (for automated metric extraction)
- CI/CD pipeline access (to verify automated testing)

## Assessor Skills

**Required:**

- Understanding of ISO 27001:2022 Control A.8.29
- Familiarity with ISMS-POL-A.8.25-26-29 Section 4 (Security Testing policy)
- Understanding of SAST, DAST, SCA, IAST concepts
- Ability to interpret security testing results
- Understanding of vulnerability severity ratings (CVSS, tool-specific)

**Helpful:**

- Experience with specific testing tools (SonarQube, Snyk, etc.)
- Penetration testing knowledge
- OWASP Top 10 knowledge
- CWE/CVE familiarity

---

# Assessment Workflow

## Assessment Process Overview

**Phase 1: Preparation** (30 minutes)
1. Review ISMS-POL-A.8.25-26-29 Section 4 (Security Testing policy)
2. Gather prerequisites (Section 2.1)
3. Obtain access to testing tools and dashboards
4. Define assessment period clearly

**Phase 2: Data Collection** (2-3 hours)
5. Complete Application Profile (Sheet 1)
6. Collect SAST results (Sheet 2)
7. Collect DAST results (Sheet 3)
8. Collect SCA results (Sheet 4)
9. Review IAST and Pen Test results (Sheet 5)
10. Review Security Acceptance Testing (Sheet 6)
11. Export reports and take screenshots (evidence)

**Phase 3: Analysis** (30-60 minutes)
12. Review auto-calculated coverage scores
13. Analyze finding severity distribution
14. Identify testing gaps
15. Compare against policy requirements

**Phase 4: Review & Approval** (30 minutes)
16. Self-review using quality checklist (Section 7)
17. Submit for Security Engineer/Architect review
18. Address feedback
19. Obtain final approval

**Phase 5: Follow-Up** (ongoing)
20. Communicate findings to Application Owner and Development Team
21. Track remediation in IMP-S4 (Vulnerability Remediation Assessment)
22. Schedule next assessment

## Assessment Period Selection

**Best Practice:** Assess testing results over a meaningful period with multiple test cycles.

**Recommended Periods:**

- **High-Risk Applications:** Last 3 months (quarterly assessment)
- **Medium-Risk Applications:** Last 6 months (semi-annual assessment)
- **Low-Risk Applications:** Last 12 months (annual assessment)

**Why Multiple Cycles Matter:**

- Single scan may not be representative
- Trends are more meaningful than point-in-time
- Shows improvement (or degradation) over time

## Testing Tool Data Extraction

**SAST Tools:**

- Export latest scan results (CSV, JSON, PDF)
- Pull key metrics: total findings, severity distribution, code coverage
- Note scan date and version scanned

**DAST Tools:**

- Export latest scan results
- Pull key metrics: vulnerabilities found, severity distribution
- Note scan configuration (authenticated vs. unauthenticated)

**SCA Tools:**

- Export vulnerable dependencies list
- Pull metrics: critical/high/medium/low vulnerabilities
- Note direct vs. transitive dependencies

**Manual Export vs. API:**

- Manual: Login to tool dashboard, export reports
- API: Use tool API for automated metric extraction (faster, more accurate)

---

# Completing Each Sheet

## Sheet 1: Application Profile & Testing Context

**Purpose:** Document application info and define testing assessment period.

**Completion Time:** 10 minutes

**Key Fields:**

**Application Identification:**

- **Application ID:** Unique identifier
- **Application Name:** Full name
- **Application Risk Level:** High, Medium, Low (from IMP-S1)
- **Technology Stack:** Languages, frameworks
- **Application Owner:** Name, email

**Testing Context:**

- **Assessment Period:** Start date → End date
- **Number of Releases/Sprints in Period:** Count
- **Testing Milestones:** Major testing events (e.g., pre-release pen test, quarterly DAST scan)

**Testing Requirements (from Policy):**
Based on risk level, what testing is required?

| Risk Level | Required Testing |
|-----------|------------------|
| High-Risk | SAST (per sprint/release), DAST (per release), SCA (continuous), Pen test (annually) |
| Medium-Risk | SAST (per release), DAST (semi-annually), SCA (per release), Pen test (optional) |
| Low-Risk | SAST (optional), DAST (annually if internet-facing), SCA (optional) |

**Testing Tools Used:**

- **SAST Tool:** Name and version
- **DAST Tool:** Name and version
- **SCA Tool:** Name and version
- **IAST Tool:** Name and version (if used)
- **Pen Test Provider:** Company name (if external)

**Completion Tips:**

- Clearly define assessment period (affects all subsequent sheets)
- Verify tool versions (different versions may have different vulnerability databases)
- Note if tools changed during assessment period (affects trend analysis)

**Common Mistakes:**

- ❌ Vague assessment period ("recent" instead of "2025-10-01 to 2025-12-31")
- ❌ Not noting tool version changes
- ❌ Incorrect risk level (must match IMP-S1)

## Sheet 2: SAST Results

**Purpose:** Assess SAST execution and analyse scan results.

**Completion Time:** 30-45 minutes

**Key Assessment Areas:**

**A. SAST Execution**

- **SAST Tool:** Name (from Sheet 1)
- **Scans Executed in Period:** Count
- **Scan Frequency:** Per commit, Daily, Per sprint, Per release, Ad-hoc
- **Last Scan Date:** Date of most recent scan
- **Code Coverage:** % of codebase scanned (if available)

**B. SAST Configuration**

- **Languages Scanned:** Which languages does tool scan?
- **Security Rule Sets Enabled:** OWASP Top 10, CWE Top 25, Language-specific, All
- **Severity Levels:** Critical, High, Medium, Low, Info
- **False Positive Handling:** Are false positives suppressed?

**C. SAST Findings Summary (Latest Scan)**

| Severity | Count | % of Total |
|----------|-------|------------|
| Critical | X | X% |
| High | X | X% |
| Medium | X | X% |
| Low | X | X% |
| Info | X | X% |
| **Total** | **X** | **100%** |

**D. SAST Findings by Category (Top 5)**

List top 5 vulnerability categories found:
1. SQL Injection (CWE-89) - X findings
2. Cross-Site Scripting (CWE-79) - X findings
3. Hardcoded Credentials (CWE-798) - X findings
4. Path Traversal (CWE-22) - X findings
5. Insecure Deserialization (CWE-502) - X findings

**E. SAST Trend Analysis** (if multiple scans in period)

| Metric | First Scan | Latest Scan | Change |
|--------|-----------|-------------|--------|
| Total Findings | X | X | ↑↓ X% |
| Critical | X | X | ↑↓ X |
| High | X | X | ↑↓ X |
| Medium | X | X | ↑↓ X |

**F. SAST Build Integration**

- **Integrated in CI/CD?** Yes/No
- **Build Fails on Critical/High?** Yes/No/Partial
- **Developer Feedback?** Immediate (IDE/PR), Daily report, Weekly report, Manual

**G. SAST False Positive Rate**

- **Total Findings:** X
- **False Positives:** X
- **False Positive Rate:** X%
- **False Positives Suppressed?** Yes/No

**Completion Tips:**

- Export latest SAST scan results (CSV or PDF)
- Take screenshots of SAST dashboard (severity distribution charts)
- Check tool configuration (which rules are enabled?)
- Compare first vs. latest scan in period (trend)
- Note if scan failed or was incomplete

**Common Mistakes:**

- ❌ Only reporting latest scan (no trend analysis)
- ❌ Not noting code coverage (partial scans misleading)
- ❌ Including Info-level findings in critical count (severity matters)
- ❌ Not checking false positive rate (high FP rate = tool not useful)

## Sheet 3: DAST Results

**Purpose:** Assess DAST execution and analyse scan results.

**Completion Time:** 30-45 minutes

**Key Assessment Areas:**

**A. DAST Execution**

- **DAST Tool:** Name (from Sheet 1)
- **Scans Executed in Period:** Count
- **Scan Frequency:** Per release, Monthly, Quarterly, Ad-hoc
- **Last Scan Date:** Date of most recent scan
- **Scan Type:** Authenticated, Unauthenticated, Both

**B. DAST Scan Configuration**

- **Target URL(s):** Which URLs/endpoints were scanned?
- **Scan Profile:** Full scan, Quick scan, Custom
- **Authentication:** Configured for authenticated scan? Yes/No
- **Scan Duration:** Hours (typical)
- **Coverage:** % of application scanned (if available)

**C. DAST Findings Summary (Latest Scan)**

| Severity | Count | % of Total |
|----------|-------|------------|
| Critical | X | X% |
| High | X | X% |
| Medium | X | X% |
| Low | X | X% |
| Info | X | X% |
| **Total** | **X** | **100%** |

**D. DAST Findings by Category (Top 5)**

List top 5 vulnerability categories found:
1. SQL Injection - X findings
2. Cross-Site Scripting (XSS) - X findings
3. Missing Security Headers - X findings
4. Insecure Cookie Attributes - X findings
5. Sensitive Data Exposure - X findings

**E. DAST Trend Analysis** (if multiple scans in period)

| Metric | First Scan | Latest Scan | Change |
|--------|-----------|-------------|--------|
| Total Findings | X | X | ↑↓ X% |
| Critical | X | X | ↑↓ X |
| High | X | X | ↑↓ X |

**F. DAST vs. SAST Correlation**

- **Vulnerabilities found in BOTH SAST and DAST?** Yes/No/Unknown
- **Examples:** (e.g., SQL injection found by both)
- **DAST-Only Findings:** X (runtime vulnerabilities, configuration issues)
- **SAST-Only Findings:** X (code-level issues DAST can't detect)

**G. DAST False Positive Rate**

- **Total Findings:** X
- **False Positives:** X
- **False Positive Rate:** X%

**Completion Tips:**

- Export latest DAST scan results
- Take screenshots of DAST dashboard
- Note scan type (authenticated scans find more vulnerabilities)
- Check scan coverage (did scan timeout before completing?)
- Identify DAST-specific findings (configuration issues, runtime issues)

**Common Mistakes:**

- ❌ Only running unauthenticated scans (misses many vulnerabilities)
- ❌ Not checking scan coverage (partial scans incomplete)
- ❌ Not correlating SAST and DAST findings (same vuln found by both?)
- ❌ Ignoring "Info" findings (may indicate misconfigurations)

## Sheet 4: SCA Results

**Purpose:** Assess SCA execution and vulnerable dependency analysis.

**Completion Time:** 30 minutes

**Key Assessment Areas:**

**A. SCA Execution**

- **SCA Tool:** Name (from Sheet 1)
- **Scans Executed in Period:** Count
- **Scan Frequency:** Per build, Daily, Weekly, Per release
- **Last Scan Date:** Date of most recent scan
- **Package Managers Scanned:** npm, Maven, pip, NuGet, etc.

**B. Dependency Inventory**

- **Total Dependencies:** X
- **Direct Dependencies:** X
- **Transitive Dependencies:** X
- **Outdated Dependencies:** X (not latest version)

**C. SCA Findings Summary (Latest Scan)**

| Severity | Count | % of Total |
|----------|-------|------------|
| Critical | X | X% |
| High | X | X% |
| Medium | X | X% |
| Low | X | X% |
| **Total** | **X** | **100%** |

**D. Top Vulnerable Dependencies (Top 5)**

List top 5 most vulnerable dependencies:
1. **Package Name:** log4j-core **Version:** 2.14.1 **CVEs:** CVE-2021-44228 (Log4Shell), CVE-2021-45046 **Severity:** Critical
2. **Package Name:** spring-core **Version:** 5.2.0 **CVEs:** CVE-2022-22965 (Spring4Shell) **Severity:** Critical
3. [...]

**E. SCA Remediation Metrics**

- **Vulnerabilities Remediated in Period:** X
- **Average Remediation Time:** X days
- **Critical Vulnerabilities Outstanding:** X
- **High Vulnerabilities Outstanding:** X

**F. License Compliance** (if tool supports)

- **License Issues Found:** X
- **Restricted Licenses:** X (e.g., GPL in proprietary software)
- **Unknown Licenses:** X

**G. Dependency Update Strategy**

- **Automated Dependency Updates?** Yes (Dependabot/Renovate), No
- **Update Frequency:** Daily, Weekly, Monthly, Manual
- **Breaking Changes Handled?** Yes/No (how are major version updates tested?)

**Completion Tips:**

- Export SCA scan results (vulnerable dependency list)
- Take screenshots of SCA dashboard
- Identify critical/high vulnerabilities (prioritize remediation)
- Check for known high-profile CVEs (Log4Shell, Spring4Shell, etc.)
- Note if dependencies are outdated (may have unpatched vulnerabilities)

**Common Mistakes:**

- ❌ Only checking direct dependencies (transitive dependencies also matter)
- ❌ Not correlating CVE severity with CVSS score (tool severity may differ)
- ❌ Ignoring license compliance (legal risk)
- ❌ Not checking dependency update frequency (stale dependencies = more vulnerabilities)

## Sheet 5: IAST & Penetration Testing

**Purpose:** Assess IAST and penetration testing execution and results.

**Completion Time:** 30-45 minutes

**Section A: IAST Results** (if IAST tool used)

**A. IAST Execution**

- **IAST Tool:** Name (Contrast Security, Seeker, Hdiv, etc.)
- **IAST Used?** Yes/No
- **Deployment Model:** Agent-based, Network-based
- **Testing Environment:** Development, QA, Staging
- **Execution Period:** Dates IAST was active

**B. IAST Findings Summary**

| Severity | Count |
|----------|-------|
| Critical | X |
| High | X |
| Medium | X |
| Low | X |
| **Total** | **X** |

**C. IAST vs. SAST/DAST**

- **Unique IAST Findings:** X (found only by IAST, not SAST/DAST)
- **Runtime Vulnerabilities:** X (only detectable at runtime)
- **IAST Advantages Noted:** [List specific examples]

**Section B: Penetration Testing**

**A. Penetration Test Execution**

- **Pen Test Conducted in Period?** Yes/No
- **Pen Test Date:** Date conducted
- **Pen Test Type:** Black box, Gray box, White box
- **Pen Test Scope:** Web app, Mobile app, API, Network, All
- **Pen Test Provider:** Internal team, External provider (name)
- **Pen Test Methodology:** OWASP Testing Guide, PTES, Custom

**B. Penetration Test Findings Summary**

| Severity | Count |
|----------|-------|
| Critical | X |
| High | X |
| Medium | X |
| Low | X |
| Info | X |
| **Total** | **X** |

**C. Penetration Test Key Findings (Top 5)**

List top 5 most critical findings:
1. **Finding:** Unauthenticated API access **Severity:** Critical **Impact:** [Description]
2. **Finding:** SQL Injection in login form **Severity:** Critical **Impact:** [Description]
3. [...]

**D. Penetration Test Remediation**

- **Findings Remediated:** X
- **Findings Outstanding:** X
- **Retest Conducted?** Yes/No
- **Retest Date:** [Date]
- **Retest Result:** All findings fixed, Some findings remain, New findings discovered

**E. Penetration Test Report**

- **Report Location:** URL or file path
- **Executive Summary Available?** Yes/No
- **Technical Details Available?** Yes/No
- **Remediation Recommendations Provided?** Yes/No

**Completion Tips:**

- Obtain pen test report (full technical report, not just executive summary)
- Verify all critical/high findings have been remediated (or documented as accepted risk)
- Check if retest was conducted (validates remediation)
- Note any findings that were NOT found by SAST/DAST (shows value of pen testing)

**Common Mistakes:**

- ❌ Not conducting pen tests for High-Risk applications (policy violation)
- ❌ Only reading executive summary (miss technical details)
- ❌ Not tracking remediation (findings identified but not fixed)
- ❌ Not conducting retest (can't verify findings fixed)

## Sheet 6: Security Acceptance Testing

**Purpose:** Assess security test cases and acceptance criteria execution.

**Completion Time:** 20-30 minutes

**Key Assessment Areas:**

**A. Security Test Plan**

- **Security Test Plan Exists?** Yes/No
- **Test Plan Location:** URL or file path
- **Test Plan Last Updated:** Date
- **Test Cases Documented?** Yes/No/Partial

**B. Security Test Case Coverage**

For each security requirement category, assess test case coverage:

| Category | Test Cases Defined? | Test Cases Executed? | Pass Rate |
|----------|-------------------|---------------------|-----------|
| Authentication | Yes/No | Yes/No | X% |
| Authorisation | Yes/No | Yes/No | X% |
| Input Validation | Yes/No | Yes/No | X% |
| Cryptography | Yes/No | Yes/No | X% |
| Session Management | Yes/No | Yes/No | X% |
| Error Handling | Yes/No | Yes/No | X% |
| Logging | Yes/No | Yes/No | X% |
| API Security | Yes/No/N/A | Yes/No/N/A | X% |

**C. Security Acceptance Criteria**

- **Security Acceptance Criteria Defined?** Yes/No
- **Example Criteria:** (e.g., "All Critical SAST findings remediated", "Pen test completed with no High findings")
- **Acceptance Criteria Met?** Yes/No/Partial
- **Security Sign-Off Obtained?** Yes/No

**D. Security Regression Testing**

- **Security Regression Tests?** Yes/No
- **Regression Test Frequency:** Per release, Quarterly, Ad-hoc
- **Last Regression Test Date:** Date
- **Regression Test Pass Rate:** X%

**E. Test Automation**

- **Security Tests Automated?** Yes/No/Partial
- **Automation Framework:** Selenium, Postman, Burp Suite, Custom, Other
- **Automated Tests in CI/CD?** Yes/No
- **Automated Test Coverage:** X% of security test cases

**Completion Tips:**

- Review security test plan document
- Check test management system (Jira, TestRail) for security test cases
- Verify test execution records (not just test case definitions)
- Calculate pass rate (executed and passed / total executed)
- Note automation level (automated tests more reliable)

**Common Mistakes:**

- ❌ Confusing test case definition with execution (defined ≠ executed)
- ❌ Not checking pass rate (executed but failed = not compliant)
- ❌ Not verifying security acceptance criteria (may exist but not enforced)
- ❌ Not tracking regression testing (security may regress over time)

## Sheet 7: Testing Coverage Dashboard

**Purpose:** Calculate overall security testing coverage and identify gaps.

**Completion Time:** 15-20 minutes (after completing Sheets 2-6)

**Dashboard Components:**

**A. Testing Execution Summary** (Auto-calculated)

| Test Type | Required? | Executed? | Frequency | Findings (Critical/High) |
|-----------|-----------|-----------|-----------|-------------------------|
| SAST | Yes/No | Yes/No | [From Sheet 2] | X / X |
| DAST | Yes/No | Yes/No | [From Sheet 3] | X / X |
| SCA | Yes/No | Yes/No | [From Sheet 4] | X / X |
| IAST | Yes/No | Yes/No | [From Sheet 5] | X / X |
| Pen Test | Yes/No | Yes/No | [From Sheet 5] | X / X |
| Acceptance Testing | Yes/No | Yes/No | [From Sheet 6] | N/A |

**B. Overall Testing Coverage Score** (Auto-calculated)

```
Coverage Score = (Tests Executed / Tests Required) × 100%
```

**Interpretation:**

- **100%:** All required tests executed
- **75-99%:** Most tests executed, minor gaps
- **50-74%:** Significant testing gaps
- **<50%:** Major testing deficiencies

**C. Vulnerability Severity Distribution** (Aggregated from Sheets 2-5)

| Severity | SAST | DAST | SCA | IAST | Pen Test | Total |
|----------|------|------|-----|------|----------|-------|
| Critical | X | X | X | X | X | X |
| High | X | X | X | X | X | X |
| Medium | X | X | X | X | X | X |
| Low | X | X | X | X | X | X |
| **Total** | **X** | **X** | **X** | **X** | **X** | **X** |

**D. Testing Gaps Identified**

List all testing gaps:
1. **Gap:** [Description] **Impact:** [Risk if not addressed]
2. **Gap:** [Description] **Impact:** [Risk if not addressed]
[...]

**Common Gaps:**

- DAST not executed (missing runtime vulnerability detection)
- Pen test not conducted (High-Risk app without pen test)
- SCA not automated (vulnerable dependencies not tracked)
- Security acceptance testing not defined (no go/no-go criteria)

**E. Recommendations**

For each gap, provide recommendation:

- **Gap:** [Description]
- **Recommendation:** [Specific action]
- **Priority:** P1/P2/P3/P4
- **Effort:** Low/Medium/High
- **Owner:** [Suggested owner]

**Completion Tips:**

- Review all previous sheets (Sheets 2-6) before completing dashboard
- Verify auto-calculated scores are correct
- Prioritize gaps by risk (High-Risk apps without pen test = P1)
- Be specific in recommendations (not "improve testing")

**Common Mistakes:**

- ❌ Not aggregating findings across all test types (SAST + DAST + SCA + Pen test)
- ❌ Not comparing against policy requirements (what's required vs. what was done)
- ❌ Generic recommendations ("do more testing")
- ❌ Not prioritizing gaps (all gaps treated equally)

## Sheet 8: Compliance_Summary

**Purpose:** Calculate overall security testing compliance score and maturity level.

**Completion Time:** 10-15 minutes (auto-calculated from previous sheets)

**Metrics Calculated:**

**A. Testing Compliance Score** (%)

- Percentage of required testing activities executed
- Based on: Testing types required vs. actually performed
- Interpretation: ≥80% = Compliant, 50-79% = Partial, <50% = Non-compliant

**B. Finding Severity Distribution** (%)

- Breakdown of Critical, High, Medium, Low severity findings
- Overall vulnerability density (findings per 1000 lines of code, if available)

**C. Remediation Status** (%)

- Percentage of findings resolved vs. open
- Average time to remediation by severity

**D. Compliance Score by Control:**

- A.8.25 (Secure Development) - Testing component score
- A.8.26 (Security Defect Management) - Defect remediation from testing
- A.8.29 (Security Testing) - Direct compliance score

**Key Inputs:**

- Data from Sheets 2-7 (all testing sheets and dashboard)
- Risk classification from Sheet 1

**Completion Tips:**

- Review all auto-calculations
- Ensure severity distributions sum to 100%
- Validate compliance scores align with testing coverage

## Sheet 9: Evidence_Register

**Purpose:** Centralized tracking of all audit evidence supporting the assessment.

**Completion Time:** 20-30 minutes (ongoing throughout assessment)

**Key Columns:**

- **Evidence ID:** Unique identifier (e.g., EV-S3-001)
- **Sheet:** Reference to source sheet (2-7)
- **Finding:** Description of what evidence supports
- **Source:** Tool output (SAST tool name, DAST tool name, etc.)
- **Attachment:** Filename or link to evidence file
- **Collection Date:** When evidence was captured
- **Expiry:** When evidence should be re-collected
- **Status:** Collected, Verified, Archived

**Types of Evidence:**

- SAST tool scan reports (JSON, XML, or exported PDF)
- DAST tool scan reports
- SCA scan results
- Penetration testing reports
- Test case documentation
- Screenshots of tool dashboards

**Storage Location:**

- All evidence files should be stored in: `[Assessment Folder]/Evidence/`
- Use consistent naming: `EV-S3-001_[Tool]_[Date].pdf`

**Completion Tips:**

- Update Evidence Register as you collect evidence
- Link to actual files (not manual descriptions)
- Include collection date for audit trail
- Archive old evidence when superseded

## Sheet 10: Approval_Sign_Off

**Purpose:** Document stakeholder review, approval, and change control.

**Completion Time:** 10-15 minutes (final step)

**Review Workflow:**

**Step 1: Self-Review (Assessor)**

- [ ] All required sheets completed
- [ ] Evidence register fully populated
- [ ] Auto-calculations verified
- [ ] Recommendations are specific and actionable
- [ ] No contradictions between sheets

**Step 2: Peer Technical Review (Security Engineer)**

- [ ] Findings are accurate and evidence-based
- [ ] Severity ratings are appropriate
- [ ] Recommendations align with findings
- [ ] Assessment period clearly documented

**Step 3: Stakeholder Review (Testing Lead / DevOps Manager)**

- [ ] Testing practices accurately represented
- [ ] Tool configurations correctly assessed
- [ ] Recommendations are feasible
- [ ] Timeline for improvements is realistic

**Step 4: Security Architect Approval**

- [ ] Assessment methodology followed
- [ ] Conclusions are justified
- [ ] Compliance scoring is accurate
- [ ] Ready for executive communication

**Approval Sign-Off:**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Assessor | [Name] | [Date] | [Signature] |
| Technical Reviewer | [Name] | [Date] | [Signature] |
| Stakeholder (QA Lead/DevOps) | [Name] | [Date] | [Signature] |
| Security Architect | [Name] | [Date] | [Signature] |

**Document Control:**

- **Assessment Version:** 1.0
- **Approved Date:** [Date]
- **Next Review Date:** [Date + 6/12 months per risk level]
- **Distribution List:** [List approved recipients]

**Completion Tips:**

- Get all signatures before distribution
- Document any major issues raised during review
- Plan follow-up assessment before approval
- Archive approved version with evidence

---

# Evidence Collection

## Evidence Requirements

**Principle:** Every testing metric must be supported by tool reports or screenshots.

**Evidence Standards:**

- **Authentic:** From actual testing tools
- **Accurate:** Metrics match tool outputs
- **Complete:** Include all testing types assessed
- **Timely:** From assessment period
- **Relevant:** Directly supports assessment findings

## Evidence Types by Sheet

**Sheet 2 (SAST Results):**

- SAST scan report export (PDF, CSV, JSON)
- SAST dashboard screenshot (severity distribution)
- SAST trend graph screenshot
- SAST rule configuration screenshot

**Sheet 3 (DAST Results):**

- DAST scan report export
- DAST dashboard screenshot
- DAST scan configuration screenshot (authenticated vs. unauthenticated)
- DAST finding details (sample critical/high findings)

**Sheet 4 (SCA Results):**

- SCA vulnerable dependency list export
- SCA dashboard screenshot
- Top vulnerable dependencies screenshot
- SCA remediation metrics

**Sheet 5 (IAST & Pen Test):**

- IAST scan results (if applicable)
- Penetration testing report (full technical report)
- Pen test executive summary
- Pen test remediation evidence (retest report)

**Sheet 6 (Security Acceptance Testing):**

- Security test plan document
- Test case execution report
- Test pass/fail summary
- Security acceptance criteria checklist

## Evidence Storage and Organisation

**Folder Structure:**
```
/Assessments/A829-Security-Testing/[APP-ID]/[YYYYMMDD]/
  ├── SAST/
  │   ├── SonarQube_Scan_Report_20260115.pdf
  │   ├── SAST_Dashboard_Screenshot.png
  │   └── SAST_Trend_Graph.png
  ├── DAST/
  │   ├── OWASP_ZAP_Scan_Report_20260120.html
  │   ├── DAST_Dashboard_Screenshot.png
  │   └── DAST_Findings_Sample.pdf
  ├── SCA/
  │   ├── Snyk_Vulnerable_Dependencies_20260123.csv
  │   ├── SCA_Dashboard_Screenshot.png
  │   └── Top_Vulnerable_Dependencies.xlsx
  ├── PenTest/
  │   ├── PenTest_Report_Q4_2025.pdf
  │   ├── PenTest_Executive_Summary.pdf
  │   └── Retest_Results_20260125.pdf
  ├── Acceptance_Testing/
  │   ├── Security_Test_Plan_v2.0.docx
  │   └── Test_Execution_Report_Q4_2025.xlsx
  └── Workbook/
      └── ISMS-A829-Testing-APP-CUST-20260123.xlsx
```

---

# Common Pitfalls

## Mistake 1: Only Reporting Latest Scan, No Trend Analysis

**Problem:** Assessor reports only latest SAST scan results. No comparison to previous scans. Can't tell if security is improving or degrading.

**Impact:** No visibility into trends. May miss gradual degradation.

**Solution:** Always compare first vs. latest scan in assessment period. Calculate change (↑↓ X%). Note trends.

## Mistake 2: Not Checking DAST Scan Type (Authenticated vs. Unauthenticated)

**Problem:** DAST scan executed but unauthenticated. Assessor marks DAST as "complete". Misses many vulnerabilities only detectable when logged in.

**Impact:** False sense of security. Authenticated vulnerabilities not found.

**Solution:** Always check DAST scan type. For applications requiring authentication, unauthenticated scans are insufficient. Require authenticated DAST.

## Mistake 3: Ignoring False Positive Rate

**Problem:** SAST tool reports 500 findings. Assessor reports "500 vulnerabilities found". Tool has 70% false positive rate. Only 150 real issues.

**Impact:** Inflated vulnerability count. Team overwhelmed. Tool loses credibility.

**Solution:** Always check false positive rate. If high (>50%), note this as a finding. Recommend tool tuning or replacement.

## Mistake 4: Not Correlating Findings Across Tools

**Problem:** SAST finds SQL injection. DAST also finds SQL injection in same location. Assessor counts as 2 separate findings.

**Impact:** Inflated vulnerability count. Same issue counted twice.

**Solution:** Correlate findings across tools (SAST, DAST, SCA, Pen test). Note when same vulnerability found by multiple tools (validates finding).

## Mistake 5: Accepting Pen Test "Not Required" Without Verification

**Problem:** Application is High-Risk but Development Manager says "pen test not required". Assessor accepts this without checking policy.

**Impact:** Policy violation. High-Risk app without pen test.

**Solution:** Always verify testing requirements against policy (Sheet 1). High-Risk applications MUST have penetration testing (per policy Section 4.7).

## Mistake 6: Not Checking SCA Transitive Dependencies

**Problem:** SCA tool scans direct dependencies only. Transitive dependencies (dependencies of dependencies) not checked. Many vulnerabilities in transitive dependencies.

**Impact:** Vulnerable transitive dependencies missed.

**Solution:** Ensure SCA tool scans both direct AND transitive dependencies. Check tool configuration.

## Mistake 7: Confusing Test Case Definition with Execution

**Problem:** Security test plan exists with 100 test cases defined. Assessor marks security testing as "complete". Test cases were never executed.

**Impact:** False compliance. Tests defined but not run = not tested.

**Solution:** Distinguish test case definition from execution. Verify test execution records exist (not just test plan).

## Mistake 8: Not Verifying Penetration Test Remediation

**Problem:** Pen test found 10 critical vulnerabilities. Assessor notes findings but doesn't check if they were fixed.

**Impact:** Vulnerabilities identified but not remediated.

**Solution:** Always check remediation status. For critical/high pen test findings, verify remediation AND retest results.

## Mistake 9: Accepting Old Scan Results as Current

**Problem:** SAST scan from 6 months ago. Assessor uses this for quarterly assessment. Application has changed significantly since scan.

**Impact:** Stale results. Current vulnerabilities not reflected.

**Solution:** Always check scan date. For quarterly assessments, scans should be within last 3 months. For annual assessments, within last 12 months.

## Mistake 10: Not Documenting Testing Gaps

**Problem:** DAST not executed because tool license expired. Assessor notes "DAST: No" but doesn't document gap or recommend remediation.

**Impact:** Gap identified but not addressed. No improvement.

**Solution:** Document ALL gaps in Sheet 7 (Dashboard) with specific recommendations, priority, and owner.

---

# Quality Checklist

## Completeness

- [ ] All 7 sheets completed
- [ ] All required fields populated
- [ ] All testing types assessed (SAST, DAST, SCA, IAST, Pen test, Acceptance)
- [ ] Trend analysis included (first vs. latest scan)

## Accuracy

- [ ] Scan results match tool exports
- [ ] Severity counts verified
- [ ] Assessment period clearly defined
- [ ] Tool names and versions accurate

## Evidence

- [ ] Tool reports exported (SAST, DAST, SCA)
- [ ] Dashboard screenshots captured
- [ ] Pen test report obtained (if applicable)
- [ ] Evidence stored in repository

## Consistency

- [ ] Dashboard (Sheet 7) matches Sheets 2-6
- [ ] Testing requirements match policy (based on risk level)
- [ ] Gaps documented with recommendations

## Clarity

- [ ] Findings clearly described
- [ ] Recommendations specific and actionable
- [ ] No typos or errors

---

# Review & Approval

**Process:**
1. Self-review (quality checklist)
2. Security Engineer review (validate metrics)
3. Security Architect peer review
4. Address feedback
5. Final approval

---

**END OF USER GUIDE**

---

*"Every bug found before release is a breach prevented."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
