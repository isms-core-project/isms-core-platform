<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.3-UG:framework:UG:a.8.28.3 -->
**ISMS-IMP-A.8.28.3-UG - Code Review & Testing Assessment Specification**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Code Review & Testing Assessment Specification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.28.3-UG |
| **Related Policy** | ISMS-POL-A.8.28 (Secure Coding) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.28 (Secure Coding) |
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

- ISMS-POL-A.8.28 (Secure Coding)
- ISMS-IMP-A.8.28.1 (SDLC Assessment Specification)
- ISMS-IMP-A.8.28.2 (Standards & Tools Assessment Specification)
- ISMS-IMP-A.8.28.4 (Third-Party & Open Source Software Assessment Specification)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Code Review Process | Assess the code review process and security coverage |
| 3 | Security Champion Review | Evaluate security champion involvement in code reviews |
| 4 | Unit Integration Testing | Assess security in unit and integration testing |
| 5 | API Application Testing | Evaluate API and application-level security testing |
| 6 | External Testing Validation | Track external penetration testing and validation results |
| 7 | Evidence Register | Store and reference evidence supporting assessments |
| 8 | Gap Analysis | Identify gaps in code review and testing coverage |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## What This Assessment Does

This assessment evaluates whether your code review and security testing practices **actually find and prevent vulnerabilities** before code reaches production.

**Core Question**: "Are we fooling ourselves about the effectiveness of our review and testing processes?"

As Feynman said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

**What We're Assessing**:

- ✅ **Code Review Effectiveness**: Does review actually catch security issues?
- ✅ **Security Testing Coverage**: Are we testing what matters?
- ✅ **External Validation**: What do pentests and bug bounties find?
- ✅ **Process vs. Outcomes**: Are we measuring process or actual security?

**What We're NOT Assessing**:

- ❌ Automated tool scanning (covered in IMP-A.8.28.2)
- ❌ SDLC process design (covered in IMP-A.8.28.1)
- ❌ Production monitoring (different control)
- ❌ Whether you have a process on paper (we care if it WORKS)

## Who Should Complete This Assessment

**Primary Assessor**: Application Security Team or Security Champion  
**Required Participants**:

- Development Team Leads (code review insights)
- QA Managers (testing coverage and effectiveness)
- Security Champions (security review perspective)
- AppSec Team (external testing programs)

**Time Estimate**: 8-12 hours for comprehensive assessment  
**Recommended Approach**: Collaborative session with all stakeholders present

## When to Use This Assessment

**Initial Assessment**: When implementing Control A.8.28  
**Recurring Assessment**: Quarterly  
**Triggered Assessment**:

- Security incidents revealing review/testing gaps
- Major process changes to code review or testing
- New development teams or methodologies
- Post-incident reviews identifying missed vulnerabilities
- Annual compliance audits
- After pentests find issues that should have been caught internally

## Assessment Output

**Generated Workbook**: `ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_YYYYMMDD.xlsx`  
**Python Generator**: `generate_a828_3_code_review_testing.py`

**Workbook Contains**:

- 10 sheets covering all aspects of code review and testing
- 90 assessment questions across 5 domains
- Evidence tracking for audit readiness
- Gap analysis and remediation planning
- Executive summary with compliance metrics

---

# Prerequisites & Preparation

## Data You'll Need

**Code Review Metrics** (last 3 months):

- Total pull requests / merge requests
- Review approval rates and coverage
- Security issues found in review
- Review comments mentioning security
- Reviewer qualifications and training records
- Review tool configuration (GitHub/GitLab/Bitbucket settings)

**Security Testing Data**:

- Security test suite documentation
- Test coverage reports (security-specific)
- Security test execution logs
- Failed security test blocking evidence
- Test case maintenance records
- API security test scenarios

**External Testing Results**:

- Penetration test reports (last 12 months)
- Bug bounty submissions and resolutions
- Responsible disclosure program metrics
- Vulnerability remediation timelines
- Retest results validating fixes

**Security Champion Program**:

- Champion roster and training records
- Champion review logs and approvals
- Architecture review meeting notes
- Threat model documents
- Champion escalation procedures

## Stakeholder Interviews Needed

**Before the assessment session**, conduct brief interviews:

**Development Team Leads** (15-20 minutes each):

- How effective is code review at catching security issues?
- What security review training do reviewers have?
- Sample recent reviews that caught security issues
- Where do security reviews fall short?

**Security Champions** (20-30 minutes):

- How often are you engaged in security reviews?
- What percentage of high-risk changes get Champion review?
- What security issues are most commonly missed?
- Training needs for the Champion program?

**QA Managers** (15-20 minutes):

- Security test coverage for critical functionality
- How comprehensive are API security tests?
- Test failure response and blocking
- Test maintenance and regression testing

**AppSec Team** (30 minutes):

- Pentest findings analysis (what should have been caught internally?)
- Bug bounty program effectiveness
- Vulnerability trend analysis
- Gaps in internal testing based on external findings

## Configuration Verification

**Before Starting Assessment**:

1. **Code Review Tool Configuration**:

   - Access repository settings (GitHub, GitLab, Bitbucket)
   - Verify branch protection rules
   - Check required reviewer settings
   - Review approval workflow configuration

2. **Testing Infrastructure**:

   - Access CI/CD pipeline configuration
   - Review security test execution logs
   - Verify test failure blocking settings
   - Check test environment configuration

3. **Evidence Access**:

   - Pentest report repository
   - Bug bounty platform access
   - Code review analytics dashboard
   - Security metrics reporting tools

## Common Preparation Mistakes

❌ **Don't Do This**:

- Assessing based on policy documents alone
- Accepting "we have a process" without evidence
- Reviewing only successful cases (ignoring what slips through)
- Focusing on quantity (# of reviews) vs. quality (vulnerabilities caught)

✅ **Do This Instead**:

- Sample actual pull requests and review comments
- Analyze what vulnerabilities reached production (should have been caught)
- Measure effectiveness: vulnerabilities caught vs. vulnerabilities missed
- Focus on outcomes: security improvements, not process compliance

---

# Assessment Workflow (Step-by-Step)

## Step 1: Generate Assessment Workbook

```bash
# Generate fresh assessment workbook
python3 generate_a828_3_code_review_testing.py

# Output: ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_20260125.xlsx
```

**What This Creates**:

- Empty assessment workbook with all sheets
- Pre-configured data validation dropdowns
- Assessment questions and evidence requirements
- Formula-driven compliance calculations

## Step 2: Review Instructions Sheet

**Open workbook → "Instructions" sheet**

Read the complete instructions including:

- Assessment scope and objectives
- How to use dropdown menus
- Evidence documentation requirements
- Completion checklist

**Key Point**: This is NOT a checkbox exercise. Every "Implemented" claim requires evidence.

## Step 3: Assess Code Review Process (Domain 1)

**Sheet**: `Code_Review_Process`  
**Questions**: 18 requirements  
**Focus**: Review governance, coverage, and effectiveness

**Question-by-Question Guidance**:

**Q1.1: "Mandatory code review policy enforced for all production code"**

- **Status**: Implemented / Partial / Not Implemented / N/A
- **What to Check**: Repository branch protection settings
- **Evidence**: Screenshots of GitHub/GitLab protected branch config
- **Anti-Pattern**: Policy exists but exceptions granted regularly
- **Good Practice**: Zero production deployments without review

**Q1.2: "Reviewer qualifications and training documented"**

- **What to Check**: Reviewer skill matrix, training records
- **Evidence**: Training completion certificates, skill assessments
- **Anti-Pattern**: Anyone can approve, no security training
- **Good Practice**: Reviewers complete secure coding training

**Q1.3: "Review coverage measured and tracked (>95% target)"**

- **What to Check**: Review analytics dashboard
- **Evidence**: Last 3 months review coverage metrics
- **Anti-Pattern**: "We review everything" with no metrics
- **Good Practice**: Automated tracking, gaps escalated

**Q1.4: "Security-focused review criteria in checklist"**

- **What to Check**: Review checklist includes security items
- **Evidence**: Checklist template with OWASP Top 10 coverage
- **Anti-Pattern**: Generic checklist, no security focus
- **Good Practice**: Language-specific security checklists

**Q1.5-Q1.18**: Continue through code review governance questions...

**Effectiveness Check**: Don't just verify process exists—sample 10 recent pull requests:

- How many had meaningful security review comments?
- What security issues were caught?
- Were any security issues merged anyway?
- Is there evidence of security thinking?

## Step 4: Assess Security Champion Review (Domain 2)

**Sheet**: `Security_Champion_Review`  
**Questions**: 18 requirements  
**Focus**: Champion program effectiveness and architecture review

**Key Questions Guidance**:

**Q2.1: "Active Security Champion program with trained champions"**

- **What to Check**: Champion roster, training records, activity logs
- **Evidence**: Champion certifications, review participation metrics
- **Effectiveness Test**: Sample high-risk changes—did Champion review?
- **Anti-Pattern**: Champions exist but rarely engaged
- **Good Practice**: Champions review 100% of high-risk changes

**Q2.2: "Champion review trigger criteria defined and followed"**

- **What to Check**: When Champion review is required
- **Evidence**: Criteria documentation, trigger examples
- **Effectiveness Test**: Were criteria actually applied?
- **Anti-Pattern**: Vague criteria, inconsistent application
- **Good Practice**: Automated triggers (API changes, auth code, crypto)

**Q2.3-Q2.6: Architecture Review Requirements**

- **Focus**: New systems, major changes, security-sensitive features
- **Evidence**: Architecture review meeting notes, threat models
- **Effectiveness**: Do threat models actually find design flaws?
- **Anti-Pattern**: Threat modeling is "TBD" or never completed
- **Good Practice**: No deployment without architecture review sign-off

**Q2.7-Q2.12: Champion Availability & Response**

- **Measure**: Champion response time (<48 hours target)
- **Evidence**: Champion request tickets, resolution times
- **Effectiveness**: Are developers waiting on Champions?
- **Anti-Pattern**: Champions unavailable, bottleneck to development
- **Good Practice**: Dedicated Champion time, clear escalation

**Q2.13-Q2.18: Security Consultation & Escalation**

- **Evidence**: Security consultation tickets, escalation procedures
- **Effectiveness**: Complex issues get proper security review
- **Anti-Pattern**: "No escalation path" or escalations ignored
- **Good Practice**: Clear escalation, expert review for complex issues

## Step 5: Assess Unit & Integration Testing (Domain 3)

**Sheet**: `Unit_Integration_Testing`  
**Questions**: 18 requirements  
**Focus**: Security testing at unit and integration levels

**Key Areas**:

**Q3.1-Q3.6: Security-Focused Unit Tests**

- **What to Check**: Test code for input validation, auth, error handling
- **Evidence**: Test suite code examples, coverage reports
- **Effectiveness**: Do tests actually find vulnerabilities?
- **Sample Test**: Input validation tests with malicious inputs
- **Anti-Pattern**: Tests only check "happy path"
- **Good Practice**: Negative tests, edge cases, malicious inputs

**Q3.7-Q3.12: Integration Testing for Security Controls**

- **Focus**: Auth/authz, session management, access control
- **Evidence**: Integration test scenarios, execution logs
- **Effectiveness**: Are security controls properly tested?
- **Anti-Pattern**: Integration tests ignore security
- **Good Practice**: All auth/authz paths tested

**Q3.13-Q3.18: Test Maintenance & Blocking**

- **Critical**: Do failed security tests block deployment?
- **Evidence**: CI/CD logs showing blocked deployments
- **Effectiveness**: How many times have security tests blocked deployment?
- **Anti-Pattern**: Security tests can be skipped or ignored
- **Good Practice**: Security test failures = hard block

**Reality Check**: 

- If no deployments have EVER been blocked by security tests, your tests aren't effective
- Test coverage means nothing if tests don't find issues
- Focus on test quality, not just quantity

## Step 6: Assess API & Application Testing (Domain 4)

**Sheet**: `API_Application_Testing`  
**Questions**: 18 requirements  
**Focus**: Dynamic security testing for APIs and applications

**Key Areas**:

**Q4.1-Q4.6: API Security Testing**

- **Coverage**: REST, GraphQL, gRPC endpoints
- **Test Scenarios**: Auth, authz, input validation, rate limiting
- **Evidence**: API test suites, test execution reports
- **Effectiveness**: Are all API security risks tested?
- **Anti-Pattern**: "We test APIs" without security focus
- **Good Practice**: Comprehensive API security test matrix

**Q4.7-Q4.12: Authentication & Authorisation Testing**

- **Critical**: Every endpoint tested for proper access control
- **Test Cases**: Missing auth, privilege escalation, broken access control
- **Evidence**: Auth test matrix, test results
- **Effectiveness**: Do tests actually find authz bugs?
- **Anti-Pattern**: Testing only "expected" behavior
- **Good Practice**: Negative testing, privilege escalation attempts

**Q4.13-Q4.18: Injection & API Fuzzing**

- **Coverage**: SQL, XSS, XXE, command injection
- **Fuzzing**: API parameter fuzzing, negative testing
- **Evidence**: Fuzzing reports, injection test results
- **Effectiveness**: How many injection bugs found?
- **Anti-Pattern**: "We sanitize inputs" without testing
- **Good Practice**: Automated fuzzing, comprehensive injection testing

**Test Environment Reality Check**:

- Are you testing in production-like environments?
- Is test data realistic (but not production data)?
- Do security headers and CORS get tested?
- Are rate limits actually validated?

## Step 7: Assess External Testing & Validation (Domain 5)

**Sheet**: `External_Testing_Validation`  
**Questions**: 18 requirements  
**Focus**: Pentesting, bug bounty, regression testing

**Key Areas**:

**Q5.1-Q5.5: Penetration Testing Program**

- **Frequency**: Annual minimum, critical apps tested
- **Scope**: Covers production-like environments, realistic scope
- **Evidence**: Pentest reports (last 12 months)
- **Critical Question**: What did pentest find that should have been caught internally?
- **Anti-Pattern**: Limited scope pentest to ensure "clean" report
- **Good Practice**: Realistic scope, prompt remediation, retest validation

**Q5.6-Q5.10: Bug Bounty / Responsible Disclosure**

- **Program Status**: Active, responsive, adequately funded
- **Researcher Relations**: Professional, timely, fair payments
- **Evidence**: Bug bounty dashboard, researcher communications
- **Critical Question**: Are researchers finding simple issues?
- **Anti-Pattern**: Researchers submit findings, no response
- **Good Practice**: Active program, prompt triage, fair rewards

**Q5.11-Q5.18: Regression Testing & Continuous Improvement**

- **Regression Suite**: Tests for previously found vulnerabilities
- **Automation**: Regression tests run in CI/CD
- **Metrics**: Vulnerability trends, testing effectiveness KPIs
- **Evidence**: Regression test suite, historical metrics
- **Critical**: How many regressions occurred (old bugs reintroduced)?
- **Anti-Pattern**: Past vulnerabilities not tested in regression
- **Good Practice**: Every vuln gets regression test, automated execution

**External Testing Reality Check**:
Ask yourself honestly:

- What percentage of pentest findings should have been caught internally?
- Are bug bounty researchers finding issues that basic testing would catch?
- Is the same vulnerability class appearing repeatedly?
- Are we learning and improving, or repeating mistakes?

## Step 8: Review Summary Dashboard

**Sheet**: `Summary_Dashboard`  
**Auto-Calculated**: Based on all domain assessments

**What You'll See**:

- Overall compliance percentage
- Domain-by-domain breakdown
- Traffic light indicators (Green/Yellow/Red)
- Key findings summary
- Emphasis: Vulnerabilities caught vs. reviews performed

**Critical Analysis**:

- Don't celebrate 90% compliance if production incidents reveal gaps
- Focus on effectiveness metrics, not process metrics
- If external testing finds basic issues, internal testing is failing

## Step 9: Document Evidence

**Sheet**: `Evidence_Register`

**For Every "Implemented" Response**:

- Evidence ID (auto-numbered)
- Related requirement ID
- Evidence type (review logs, test results, pentest reports, etc.)
- Description of evidence
- Location/link to evidence
- Collection date
- Collected by (your name)

**Evidence Quality Standards**:

- ✅ Objective, verifiable evidence
- ✅ Recent (last 3-6 months)
- ✅ Representative samples (not cherry-picked successes)
- ❌ "Trust me, we do this"
- ❌ Policy documents without proof of execution
- ❌ Old evidence (2+ years old)

**Audit Perspective**: An auditor will verify your evidence. If it doesn't exist or doesn't support the claim, compliance status drops.

## Step 10: Complete Gap Analysis

**Sheet**: `Gap_Analysis`

**For Every "Partial" or "Not Implemented"**:

- Gap ID (auto-numbered)
- Domain (which assessment domain)
- Requirement ID (specific requirement)
- Gap description (what's missing)
- Current state (what you have now)
- Target state (what you need)
- Priority (Critical/High/Medium/Low)
- Owner (who will fix this)
- Target date (when will it be fixed)
- Status (Planned/In Progress/Complete)

**Priority Guidance**:

- **Critical**: No security review or testing for production code
- **High**: Review/testing exists but low effectiveness (<50% issue detection)
- **Medium**: Gaps in specific areas (e.g., API testing, Champion program)
- **Low**: Process improvements, efficiency gains

**Reality Check**: If you have no gaps, you're probably fooling yourself.

## Step 11: Obtain Approvals

**Sheet**: `Approval_Sign_Off`

**Required Approvers**:
1. **Assessment Completer**: Application Security Analyst (you)
2. **Application Security Lead**: Technical review of findings
3. **Development Manager**: Engineering perspective and commitment
4. **QA Manager**: Testing coverage validation
5. **CISO / Security Director**: Executive approval

**Approval Criteria**:

- All 90 requirements assessed
- Evidence documented for all "Implemented" claims
- Gaps identified and remediation planned
- Realistic assessment (not overly optimistic)
- Improvement plan has committed owners and dates

## Step 12: Archive and Track

**After Approval**:
1. Save final workbook to secure location
2. Schedule quarterly refresh
3. Track gap remediation progress
5. Update evidence register as gaps are closed

---

# Common Pitfalls & How to Avoid Them

## Review Theater (Don't Fool Yourself)

**❌ Anti-Pattern: "LGTM" Reviews**

- Rubber-stamp approvals with no security analysis
- Reviews take <2 minutes for complex changes
- Security checklist filled out perfunctorily
- Reviews never block merges

**✅ Good Practice**:

- Sample reviews for actual security comments
- Measure: vulnerabilities caught per review
- Reviews should take time proportional to risk
- Block problematic code, don't just comment

**How to Assess**:
Pull 10 random recent reviews. Count:

- How many had security-focused comments?
- How many mentioned OWASP Top 10 risks?
- How many caught actual security issues?
- If zero, your review process is theater.

## Test Theater (Tests That Don't Test)

**❌ Anti-Pattern: Fake Security Testing**

- Tests that always pass
- Security tests disabled or skipped
- No testing of authentication/authorisation
- Test coverage metrics without security coverage

**✅ Good Practice**:

- Tests should occasionally find issues (if not, they're not testing)
- Security tests block deployment on failure
- Auth/authz comprehensively tested
- Track security test coverage separately

**How to Assess**:

- When was the last time a security test blocked deployment?
- If answer is "never", your tests are theater
- Sample security test code—does it test malicious inputs?
- Run tests with auth disabled—do they fail?

## External Testing Theater

**❌ Anti-Pattern: Pentest for Show**

- Artificially limited scope to avoid findings
- Pentest findings marked "Won't Fix" or "Accepted Risk"
- Bug bounty with no budget or response
- Researchers ignored or discouraged

**✅ Good Practice**:

- Realistic pentest scope (production-like)
- All critical/high findings remediated
- Active bug bounty, responsive to researchers
- Learn from external findings to improve internal testing

**How to Assess**:

- Read last pentest report: How many findings should have been caught internally?
- Bug bounty stats: Are researchers finding basic issues?
- If external testing finds simple issues, internal testing failed

## Cargo Cult Metrics

**❌ Anti-Pattern: Measuring Process, Not Outcomes**

- "We perform 500 code reviews per month" (but catch zero issues)
- "We have 85% test coverage" (but no security tests)
- "We did a pentest" (but ignored findings)

**✅ Good Practice: Measure What Matters**

- Vulnerabilities caught in review vs. production
- Security test effectiveness (issues found)
- False negative rate (issues that slipped through)
- Remediation timelines
- Regression rate (old bugs reintroduced)

## The "We're Too Busy" Excuse

**❌ Anti-Pattern**: "We'll add security testing later"

- Security review skipped due to deadlines
- Security tests disabled to ship faster
- "We'll fix that after launch"

**✅ Reality**: Security issues cost 10x more to fix in production

**How to Handle**:

- Security review and testing are NOT optional
- Build security into timelines, not as add-ons
- Track cost of production security incidents vs. prevention
- Demonstrate ROI of catching issues early

---

# Interpreting Your Results

## Compliance Scoring

**Overall Compliance** = (Implemented Requirements / Total Applicable Requirements) × 100%

**Domain Scores**:

- Code Review Process: X / 18 requirements
- Security Champion Review: X / 18 requirements
- Unit & Integration Testing: X / 18 requirements
- API & Application Testing: X / 18 requirements
- External Testing & Validation: X / 18 requirements

**Compliance Levels**:

- **90-100%**: Excellent (but verify it's real, not theater)
- **70-89%**: Good (identify and close gaps)
- **50-69%**: Needs Improvement (prioritize critical gaps)
- **<50%**: Critical (major review/testing gaps exist)

## What Good Looks Like

**Effective Code Review & Testing**:

- Security issues caught in review/testing (not production)
- <5% false negative rate (issues slipping through)
- Security regression rate <2%
- Pentest finding severity decreasing over time
- Bug bounty complexity increasing (simple issues caught internally)
- Mean time to detect (MTTD) improving
- Developer confidence in security quality

**Warning Signs**:

- Production incidents revealing review/testing gaps
- Same vulnerability classes appearing repeatedly
- External testing finding basic issues
- No evidence of security tests blocking deployments
- Review coverage claims without supporting data

## Effectiveness vs. Compliance

**Don't Confuse**:

- ❌ "We have a review process" (compliance)
- ✅ "Our reviews catch vulnerabilities" (effectiveness)

**Key Effectiveness Indicators**:
1. **Detection Rate**: What % of vulnerabilities found in review/testing vs. production?
2. **Prevention Rate**: How many deployments blocked by security concerns?
3. **Regression Rate**: How often do old bugs reappear?
4. **External Validation**: What do pentests/bounties find that we should have caught?

**Reality Check Question**: 
"If we removed all security review and testing tomorrow, would our security posture meaningfully change?"

If answer is "no", you have process theater, not effective security.

---

# Next Steps After Assessment

## Immediate Actions

**Within 1 Week**:

- Review findings with all stakeholders
- Prioritize critical gaps (especially "no review" or "no testing")
- Assign gap remediation owners
- Set target dates for gap closure
- Communicate results to CISO/CTO

**Within 1 Month**:

- Close critical gaps (mandatory review, test blocking)
- Begin high-priority gap remediation
- Update policies and procedures as needed
- Provide additional training where gaps identified

## Continuous Improvement

**Quarterly Reviews**:
1. Refresh assessment data
2. Measure gap closure progress
3. Analyze effectiveness trends
4. Update remediation priorities
5. Share results with development teams

**Improvement Focus Areas**:

- Enhanced security review training
- Expanded security test case libraries
- Improved Security Champion program
- Better integration between review and testing
- Automated security checks to assist manual review

## Integration with Other Assessments

**Feed Results Into**:

- **IMP-A.8.28.1 (SDLC)**: SDLC process improvement inputs
- **IMP-A.8.28.2 (Tools)**: Tool effectiveness validation

**Learn From**:

- **IMP-A.8.28.1 (SDLC)**: SDLC context for review/testing
- **IMP-A.8.28.2 (Tools)**: Tool findings should inform manual testing
- **IMP-A.8.28.4 (Third-Party)**: Third-party code review requirements

---

# Quality Checklist (Before Calling It Done)

**Assessment Completeness**:

- [ ] All 90 requirements assessed across 5 domains
- [ ] Every "Implemented" has documented evidence
- [ ] Every "Partial"/"Not Implemented" has gap entry
- [ ] Evidence register complete with locations/links
- [ ] Gap analysis includes owners and target dates

**Evidence Quality**:

- [ ] Evidence is objective and verifiable
- [ ] Evidence is recent (last 3-6 months)
- [ ] Evidence supports the compliance claim
- [ ] Evidence includes effectiveness data (not just process existence)
- [ ] An auditor could verify all evidence independently

**Effectiveness Validation**:

- [ ] Sampled actual pull requests for security review quality
- [ ] Verified security tests actually catch issues
- [ ] Analyzed external testing findings for internal gaps
- [ ] Measured outcomes (vulns caught) not just process (reviews performed)
- [ ] Identified false negatives (issues that slipped through)

**Stakeholder Engagement**:

- [ ] Development managers reviewed and agreed with findings
- [ ] QA team validated testing assessment
- [ ] Security Champions engaged in review assessment
- [ ] AppSec team reviewed external testing analysis
- [ ] All required approvers signed off

**Remediation Planning**:

- [ ] Critical gaps have immediate action plans
- [ ] High-priority gaps have committed owners
- [ ] Target dates are realistic and committed
- [ ] Remediation plans are resourced
- [ ] Progress tracking mechanism established

**Anti-Cargo-Cult Check**:

- [ ] Assessment reflects reality, not wishful thinking
- [ ] "Implemented" claims are based on evidence, not policy
- [ ] Identified areas where we're fooling ourselves
- [ ] Focused on effectiveness, not just compliance
- [ ] Honest about gaps and shortcomings

**If you checked all boxes**: Congratulations, you have a real assessment, not theater.

**If you have unchecked boxes**: That's okay—go back and address them. Better honest gaps than fake compliance.

---

**END OF USER GUIDE**

---

*"Code that has not been reviewed has not been secured; it has merely been written."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
