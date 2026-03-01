<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.25-26-29.S2-UG:framework:UG:a.8.25-26-29 -->
**ISMS-IMP-A.8.25-26-29.S2-UG - SDLC Security Activities Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | SDLC Security Activities Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.25-26-29.S2-UG |
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
- ISMS-IMP-A.8.25-26-29.S3 (Security Testing Results Assessment)
- ISMS-IMP-A.8.25-26-29.S4 (Vulnerability Remediation Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.25-26-29-S2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | SDLC Phase Activities | Assess security activities across each SDLC phase |
| 3 | Secure Coding Standards | Document and assess adherence to secure coding standards |
| 4 | Code Review Metrics | Track code review coverage and security findings |
| 5 | Security Tools Deployment | Assess deployment of security tools across the SDLC |
| 6 | Security Tools Usage | Measure effectiveness and usage of security tools |
| 7 | Developer Training | Track security training completion and competency levels |
| 8 | Security Defect Mgmt | Manage and track security defects through to remediation |
| 9 | Evidence Register | Store and reference evidence supporting assessments |
| 10 | Summary Dashboard | Compliance status and key metrics overview |
| 11 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.25-26-29-S2 - SDLC Security Activities Assessment

**What This Assessment Evaluates:**

- Security activities integration in each SDLC phase (Requirements, Design, Development, Testing, Deployment, Maintenance)
- Secure coding standards adoption and compliance
- Code review execution (peer review and security-focused review)
- Security tools deployment and usage (SAST, SCA, secret scanning, IDE plugins)
- Secure development environment configuration
- Developer security training completion and effectiveness
- Security defect management and remediation tracking

**This Assessment is For:**

- Individual applications or development teams
- Evaluating HOW security is integrated into the development process
- Measuring SDLC security maturity
- Identifying process gaps and improvement opportunities

**This Assessment is NOT For:**

- Security requirements specification (see IMP-S1)
- Security testing results (see IMP-S3)
- Vulnerability remediation tracking (see IMP-S4)
- Portfolio-wide status tracked in each workbook's Summary Dashboard (S1–S4)

## Assessment Workbook Structure

**Total Sheets:** 11

**Completion Sequence:**

1. **Instructions & Legend** - Assessment guidance, color legend, and completion instructions
2. **SDLC_Phase_Activities** - Security activities by phase (Requirements → Maintenance)
3. **Secure_Coding_Standards** - Secure coding adoption and adherence
4. **Code_Review_Metrics** - Peer review and security review metrics
5. **Security_Tools_Deployment** - SAST, SCA, secret scanning deployment status
6. **Security_Tools_Usage** - Tool usage metrics per application
7. **Developer_Training** - Training completion and effectiveness
8. **Security_Defect_Management** - Defect tracking and remediation
9. **Compliance_Summary** - Overall SDLC security compliance scores
10. **Evidence_Register** - Centralized audit evidence tracking
11. **Approval_Sign_Off** - Stakeholder review and approval workflow

**Estimated Completion Time:**

- High-Risk Application: 3-5 hours
- Medium-Risk Application: 2-3 hours
- Low-Risk Application: 1-2 hours

## Key Assessment Questions

This assessment answers:

- ✅ Are security activities integrated into each SDLC phase?
- ✅ Are secure coding standards adopted and followed?
- ✅ Is code review conducted systematically (peer + security)?
- ✅ Are security tools deployed and actively used?
- ✅ Have developers completed required security training?
- ✅ Are security defects tracked and remediated within SLAs?
- ✅ What is the overall SDLC security maturity level?
- ✅ What gaps exist and what improvements are needed?

---

# Prerequisites

## Required Information

**Before starting assessment, gather:**

**Application/Team Information:**

- [ ] Application name and ID (or team name)
- [ ] Application risk classification (High/Medium/Low from IMP-S1)
- [ ] Development team size (number of developers)
- [ ] Development methodology (Waterfall, Agile, DevOps)
- [ ] Development Manager contact
- [ ] Security Champion (if exists)

**SDLC Documentation:**

- [ ] SDLC process documentation (development methodology guide)
- [ ] Secure coding standards document (or reference to ISMS-POL-A.8.28)
- [ ] Code review process documentation (guidelines, checklists)
- [ ] Security gate documentation (entry/exit criteria)
- [ ] Sprint/release checklists (if Agile/DevOps)

**Tool Documentation:**

- [ ] SAST tool configuration and scan results access
- [ ] SCA tool configuration and scan results access
- [ ] Secret scanning tool configuration
- [ ] IDE plugin deployment status
- [ ] Version control system access (Git, SVN, etc.)
- [ ] CI/CD pipeline access (Jenkins, GitLab CI, GitHub Actions, etc.)

**Training Records:**

- [ ] Developer training tracking system access
- [ ] Security training completion reports
- [ ] Training certificates/records

**Defect Tracking:**

- [ ] Access to defect tracking system (Jira, Azure DevOps, etc.)
- [ ] Security defect query/filter definitions
- [ ] Defect remediation SLA definitions

**System Access:**

- [ ] Version control system (to review code review records)
- [ ] CI/CD system (to review security tool integration)
- [ ] Training management system
- [ ] Defect tracking system
- [ ] SAST/SCA tool dashboards

## Required Tools

**Excel Workbook:**

- Excel 2016 or later (Office 365 recommended)
- Macros enabled (if using automated workbook features)

**Evidence Collection:**

- Screenshot tool (Snipping Tool, Snagit, etc.)
- Access to document repository
- PDF reader

**Optional:**

- SAST/SCA tool API access (for automated metrics)
- CI/CD pipeline access (for build logs)
- Git CLI (for code review statistics)

## Assessor Skills

**Required:**

- Understanding of ISO 27001:2022 Control A.8.25
- Familiarity with ISMS-POL-A.8.25-26-29 Section 3 (Secure Development Lifecycle policy)
- Understanding of SDLC methodologies (Waterfall, Agile, DevOps)
- Basic software development knowledge
- Understanding of code review processes

**Helpful:**

- Experience with SAST/DAST/SCA tools
- Secure coding knowledge
- CI/CD pipeline experience
- Git/version control experience
- Agile/Scrum experience

## Stakeholder Coordination

**Key Stakeholders to Interview:**

**Development Manager:**

- SDLC process overview
- Security integration approach
- Resource allocation for security activities
- Challenges and blockers

**Security Champion (if exists):**

- Security activities execution
- Code review participation
- Security tool usage
- Developer security awareness

**Developers (sample 2-3):**

- Secure coding practices
- Tool usage experience
- Training effectiveness
- Security culture

**DevOps/Release Manager:**

- CI/CD security integration
- Deployment security gates
- Tool automation status

---

# Assessment Workflow

## Assessment Process Overview

**Phase 1: Preparation** (30-60 minutes)
1. Review ISMS-POL-A.8.25-26-29 Section 3 (Secure Development Lifecycle policy)
2. Gather prerequisites (Section 2.1)
3. Schedule interviews with Development Manager, Security Champion, sample developers
4. Open assessment workbook and review all sheets

**Phase 2: Data Collection** (2-4 hours)
5. Complete Application/Team Profile (Sheet 1)
6. Review SDLC Phase Security Activities (Sheet 2)
7. Assess Secure Coding Standards Compliance (Sheet 3)
8. Review Code Review Execution (Sheet 4)
9. Assess Security Tools Deployment (Sheet 5)
10. Review Developer Security Training (Sheet 6)
11. Review Security Defect Management (Sheet 7)
12. Collect evidence for all findings

**Phase 3: Analysis** (30-60 minutes)
13. Review auto-calculated maturity scores
14. Identify gaps and improvement opportunities
15. Develop recommendations (documented in Sheet 8)

**Phase 4: Review & Approval** (30-60 minutes)
16. Self-review using quality checklist (Section 7)
17. Submit for Development Manager and Security Champion review
18. Submit for Security Architect peer review
19. Address review feedback
20. Obtain final approval

**Phase 5: Follow-Up** (ongoing)
21. Communicate findings and recommendations
22. Track improvement actions
23. Re-assess after improvements
24. Schedule next assessment

## SDLC Methodology Considerations

**For Waterfall Projects:**

- Assess security gates at phase transitions
- Review formal security reviews and sign-offs
- Check security documentation at each phase
- Verify security testing before production

**For Agile/Scrum Projects:**

- Assess security in sprint planning (security user stories)
- Review Definition of Done (DoD) security criteria
- Check security testing within sprints
- Review sprint retrospective security topics

**For DevOps/DevSecOps:**

- Assess CI/CD security automation
- Review security gates in pipeline
- Check automated security testing (SAST, SCA, DAST in pipeline)
- Review deployment security validation

## Assessment Timing

**Best Times to Conduct Assessment:**

- **End of Sprint** (for Agile) - Team has time to reflect, evidence is fresh
- **Post-Release** (for Waterfall) - Full cycle completed, lessons learned available
- **Mid-Quarter** (for ongoing projects) - Allows time for improvements before quarter end
- **After Major Incident** (trigger) - Understand what went wrong in SDLC

**Avoid:**

- Sprint 1 or start of project (insufficient data)
- During crunch time before critical release (team too busy)
- During vacation periods (key stakeholders unavailable)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**Purpose:** Provide assessment guidance, status legend, and completion instructions.

**Completion Time:** 15 minutes

**Key Fields:**

**Application/Team Identification:**

- **Application ID / Team ID:** Unique identifier
- **Application/Team Name:** Full name
- **Application Description:** Brief description (or "Development Team" if team assessment)
- **Development Manager:** Name, email
- **Security Champion:** Name, email (if exists)
- **Team Size:** Number of developers

**Development Context:**

- **Development Methodology:** Waterfall, Agile (Scrum), Agile (Kanban), DevOps, DevSecOps, Hybrid
- **Sprint Length:** (if Agile) - 1 week, 2 weeks, 3 weeks, 4 weeks
- **Release Frequency:** How often deployed to production?
- **Technology Stack:** Primary languages, frameworks, platforms
- **Version Control System:** Git, SVN, Mercurial, etc.
- **CI/CD Platform:** Jenkins, GitLab CI, GitHub Actions, Azure DevOps, etc.

**Risk Classification:**

- **Application Risk Level:** High, Medium, Low (from IMP-S1 assessment)
- **SDLC Security Requirements:** Based on risk level, what is required?
  - High-Risk: All security activities mandatory
  - Medium-Risk: Core security activities required
  - Low-Risk: Basic security activities required

**Assessment Context:**

- **Assessment Date:** When is this assessment conducted?
- **Assessment Period:** What time period does this cover? (e.g., Q4 2025, Last 6 months)
- **Previous Assessment Date:** When was last assessment? (if applicable)

**Completion Tips:**

- Use consistent IDs across all assessments (maintain registry)
- Verify team size and contacts are current
- Note if Security Champion exists (important for maturity scoring)
- Clearly state assessment period for data collection scope

**Common Mistakes:**

- ❌ Assessing too short a period (1 sprint insufficient for trends)
- ❌ Wrong team size (count only active developers, not entire org)
- ❌ Outdated contacts (verify before submission)
- ❌ Not noting previous assessment date (can't track improvement)

## Sheet 2: SDLC_Phase_Activities

**Purpose:** Assess security activities integration in each SDLC phase.

**Completion Time:** 45-60 minutes

**Process:**

For each SDLC phase, assess whether security activities are:

- **Planned:** Documented in SDLC process (should happen)
- **Executed:** Actually performed (does happen)
- **Evidence:** Documented evidence exists (can prove it happened)

**SDLC Phases and Security Activities:**

**Phase 1: Requirements**

- [ ] Security requirements identified and documented
- [ ] Initial threat identification conducted
- [ ] Data classification determined
- [ ] Compliance requirements identified (GDPR, PCI DSS v4.0.1, etc.)
- [ ] Security acceptance criteria defined

**Phase 2: Design**

- [ ] Threat modeling conducted (STRIDE or equivalent)
- [ ] Security architecture review performed
- [ ] Security design patterns applied
- [ ] Third-party component security assessment
- [ ] Security design decisions documented

**Phase 3: Development**

- [ ] Secure coding standards followed
- [ ] Code review conducted (peer + security)
- [ ] SAST scans executed
- [ ] SCA scans executed (dependency vulnerabilities)
- [ ] Secret scanning performed
- [ ] Security unit tests written
- [ ] Security defects tracked and remediated

**Phase 4: Testing**

- [ ] Security test cases executed
- [ ] DAST scans performed
- [ ] Security acceptance testing conducted
- [ ] Penetration testing performed (if required)
- [ ] Security regression testing
- [ ] Vulnerability remediation verified

**Phase 5: Deployment**

- [ ] Production security configuration reviewed
- [ ] Deployment security checklist completed
- [ ] Security monitoring configured
- [ ] Security logging enabled
- [ ] Encryption validated
- [ ] Security sign-off obtained

**Phase 6: Maintenance**

- [ ] Security patches applied within SLA
- [ ] Vulnerability monitoring active
- [ ] Security incidents investigated
- [ ] Threat model updated when application changes
- [ ] Periodic security assessments conducted

**Assessment Approach:**

For each activity, document:

- **Planned?** Yes/No (Is it in SDLC process documentation?)
- **Executed?** Yes/No/Partial (Does team actually do it?)
- **Evidence?** Yes/No (Can you prove it with evidence?)
- **Comments:** Note gaps, partial execution, or blockers

**Scoring:**

For each phase, calculate:
```
Phase Completeness = (Activities Executed / Activities Planned) × 100%
```

Overall SDLC Security Integration:
```
Overall Score = Average of all 6 phase completeness scores
```

**Completion Tips:**

- Interview developers and review actual sprints/releases (don't just read documentation)
- Check version control history (commit messages, pull requests)
- Review CI/CD logs (verify automated activities executed)
- Sample recent releases (last 2-3 releases or last 2 sprints)
- Note if activities are automated vs. manual

**Common Mistakes:**

- ❌ Marking "Executed" based on documentation (verify it actually happens)
- ❌ Not checking recent history (team may have stopped doing activities)
- ❌ Accepting "we plan to do it" as "Planned" (must be documented)
- ❌ Not noting automation (automated activities more reliable)

## Sheet 3: Secure_Coding_Standards

**Purpose:** Assess secure coding standards adoption and adherence.

**Completion Time:** 30-45 minutes

**Key Assessment Areas:**

**A. Secure Coding Standards Existence**

- **Standards Documented?** Yes/No (Is there a secure coding standards document?)
- **Standards Location:** Where are standards documented? (URL, SharePoint, Wiki)
- **Standards Format:** Document, Wiki, Tool Configuration (SonarQube rules), Other
- **Standards Alignment:** OWASP Top 10, CWE Top 25, Language-specific (e.g., Oracle Secure Coding Java), ISMS-POL-A.8.28, Other
- **Last Updated:** When were standards last updated?

**B. Secure Coding Standards Content**

Check if standards address:

- [ ] Input validation (SQL injection, XSS, command injection prevention)
- [ ] Authentication (password hashing, MFA, session management)
- [ ] Authorisation (access control, privilege management)
- [ ] Cryptography (encryption algorithms, key management, TLS)
- [ ] Error handling (secure error messages, no information disclosure)
- [ ] Logging (security event logging, log protection)
- [ ] Data protection (sensitive data handling, PII protection)
- [ ] API security (authentication, authorisation, input validation, rate limiting)
- [ ] Dependency management (third-party component security)
- [ ] Language-specific secure coding (e.g., Java secure coding, Python secure coding)

**C. Developer Awareness**

Sample 2-3 developers:

- **Do developers know standards exist?** Yes/No/Some
- **Have developers read standards?** All/Some/None
- **Do developers reference standards during coding?** Regularly/Sometimes/Rarely/Never
- **Do developers find standards helpful?** Yes/Partially/No

**D. Secure Coding Compliance Verification**

How is compliance verified?

- [ ] Code review (peer review checks secure coding)
- [ ] Security-focused code review (Security Champion or Security Architect review)
- [ ] SAST tool (automatically detects violations)
- [ ] IDE plugins (real-time feedback during coding)
- [ ] Manual security audits (periodic review)
- [ ] No verification (standards exist but not enforced)

**E. Secure Coding Violations Tracking**

- **Are violations tracked?** Yes/No
- **Tracking System:** Jira, Azure DevOps, SAST tool, Other
- **Violation Trends:** Increasing, Stable, Decreasing, Unknown
- **Common Violations:** What are the most frequent violations? (e.g., SQL injection, XSS, hardcoded secrets)

**Scoring:**

Calculate **Secure Coding Standards Maturity Score**:
```
Score = Average of:

- Standards Existence (0-100%)
- Standards Content Completeness (0-100%)
- Developer Awareness (0-100%)
- Compliance Verification (0-100%)
- Violation Tracking (0-100%)

```

**Completion Tips:**

- Review actual secure coding standards document (don't assume it's complete)
- Interview developers (don't just ask manager)
- Check code review records for secure coding comments
- Review SAST tool configurations (rules enabled?)
- Look at recent violations (real examples)

**Common Mistakes:**

- ❌ Marking "Standards Exist" when there's only a generic "code quality" document
- ❌ Not verifying developer awareness (assuming they know because document exists)
- ❌ Accepting "SAST tool" as verification without checking if findings are actually reviewed
- ❌ Not tracking violations (can't improve without metrics)

## Sheet 4: Code_Review_Metrics

**Purpose:** Assess code review execution (peer review and security-focused review).

**Completion Time:** 30-45 minutes

**Key Assessment Areas:**

**A. Peer Code Review Process**

- **Code Review Required?** Yes/No (Is it mandatory before merge?)
- **Code Review Policy:** Where is it documented? (Development guidelines, Wiki, etc.)
- **Review Tool:** GitHub Pull Requests, GitLab Merge Requests, Azure DevOps, Gerrit, Crucible, Other
- **Review Enforcement:** Automated (branch protection), Manual approval, Honor system, None

**B. Peer Review Execution Metrics** (Last 3 months or 10 releases)

- **Total Code Changes:** Number of pull requests/merge requests
- **Code Reviews Completed:** How many were reviewed?
- **Code Review Compliance Rate:** (Reviews Completed / Total Changes) × 100%
- **Average Review Time:** How long from PR creation to approval?
- **Average Comments per Review:** Are reviews substantive or rubber-stamp?

**C. Security-Focused Code Review**

- **Security Review Required?** Yes (for all code), Yes (for high-risk code only), Recommended, No
- **High-Risk Code Defined?** Yes/No (Is there a definition of what requires security review?)
- **Security Reviewer:** Security Champion, Security Architect, Security Team, None

**High-Risk Code Examples** (if defined):

- [ ] Authentication and authorisation logic
- [ ] Cryptography implementation
- [ ] Input validation and sanitization
- [ ] File upload and processing
- [ ] Payment processing
- [ ] PII processing
- [ ] API security controls
- [ ] Database access logic
- [ ] External system integration

**D. Security Review Execution Metrics** (Last 3 months or 10 releases)

- **High-Risk Code Changes:** How many high-risk code changes?
- **Security Reviews Completed:** How many security reviews conducted?
- **Security Review Compliance Rate:** (Security Reviews / High-Risk Changes) × 100%
- **Security Findings:** How many security issues found in review?
- **Findings Remediated:** How many were fixed?

**E. Code Review Quality**

Sample 5-10 recent code reviews:

- **Are security issues identified?** Yes (regularly), Yes (sometimes), Rarely, No
- **Are security comments specific?** Yes/No (e.g., "Fix SQL injection in line 45" vs. "Security issue")
- **Are findings tracked?** Yes/No (e.g., Jira ticket created for security finding)
- **Are findings verified fixed?** Yes/No (reviewer checks fix before closing)

**Scoring:**

Calculate **Code Review Maturity Score**:
```
Score = Average of:

- Peer Review Compliance Rate (0-100%)
- Peer Review Quality (0-100% based on comments, time, substantiveness)
- Security Review Compliance Rate (0-100%)
- Security Review Quality (0-100% based on findings, specificity, tracking)

```

**Completion Tips:**

- Pull actual metrics from version control system (Git, Azure DevOps)
- Sample recent reviews (don't cherry-pick best ones)
- Check branch protection settings (automated enforcement?)
- Interview Security Champion about security review process
- Look at actual review comments (are they meaningful?)

**Common Mistakes:**

- ❌ Relying on manager's statement "all code is reviewed" (verify with data)
- ❌ Not distinguishing peer review from security review (different purposes)
- ❌ Counting empty reviews ("LGTM" with no comments) as quality reviews
- ❌ Not checking if high-risk code is actually identified and security reviewed

## Sheet 5: Security_Tools_Deployment

**Purpose:** Assess security tools deployment and usage (SAST, SCA, secret scanning, IDE plugins).

**Completion Time:** 45-60 minutes

**Key Assessment Areas:**

**A. SAST (Static Application Security Testing)**

**SAST Tool Deployed?** Yes/No

- **Tool Name:** SonarQube, Checkmarx, Fortify, Snyk Code, Semgrep, Other
- **Languages Supported:** Does tool support application's languages?
- **Deployment Location:** CI/CD pipeline, Developer workstations, Both, Manual

**SAST Configuration:**

- **Security Rules Enabled?** Yes/Partial/No
- **Rule Sets:** OWASP Top 10, CWE Top 25, Language-specific, Custom, All
- **Severity Levels Configured?** Yes/No (Critical, High, Medium, Low)
- **False Positive Suppression?** Yes/No (Are false positives managed?)

**SAST Execution:**

- **Scan Frequency:** Per commit, Daily, Per sprint, Per release, Ad-hoc
- **Scan Coverage:** All code, Changed code only
- **Scan Results Reviewed?** Always, Usually, Sometimes, Rarely, Never
- **Findings Triaged?** Yes/No (True positives identified, false positives suppressed)
- **Critical/High Findings Block Build?** Yes/No

**SAST Metrics** (Last 3 months):

- **Total Scans Executed:** Number
- **Critical Findings:** Number
- **High Findings:** Number
- **Medium Findings:** Number
- **Low Findings:** Number
- **False Positive Rate:** (False Positives / Total Findings) × 100%

**B. SCA (Software Composition Analysis)**

**SCA Tool Deployed?** Yes/No

- **Tool Name:** Snyk, Dependabot, WhiteSource, Black Duck, OWASP Dependency-Check, Other
- **Package Managers Supported:** npm, Maven, pip, NuGet, Bundler, Go modules, Other
- **Deployment Location:** CI/CD pipeline, GitHub/GitLab native, Both, Manual

**SCA Configuration:**

- **Vulnerability Databases:** NVD, GitHub Advisory, Vendor advisories, Multiple
- **Severity Thresholds:** Critical, High, Medium, Low
- **License Compliance Checking?** Yes/No
- **Automated Fix PRs?** Yes/No (e.g., Dependabot PRs)

**SCA Execution:**

- **Scan Frequency:** Per build, Daily, Weekly, Per release, Ad-hoc
- **Scan Results Reviewed?** Always, Usually, Sometimes, Rarely, Never
- **Vulnerable Dependencies Updated?** Within SLA, Delayed, Rarely, Never

**SCA Metrics** (Last 3 months):

- **Total Dependencies:** Number
- **Critical Vulnerabilities:** Number
- **High Vulnerabilities:** Number
- **Medium Vulnerabilities:** Number
- **Average Remediation Time:** Days (from detection to fix)

**C. Secret Scanning**

**Secret Scanning Deployed?** Yes/No

- **Tool Name:** GitGuardian, TruffleHog, GitHub Secret Scanning, git-secrets, Other
- **Deployment Location:** Pre-commit hook, CI/CD pipeline, Repository scanning, All

**Secret Scanning Execution:**

- **Scan Frequency:** Per commit, Daily, Weekly, Ad-hoc
- **Secrets Detected (Last 3 months):** Number
- **Secrets Remediated:** Number
- **Commits Blocked:** Number (if pre-commit hook enabled)

**D. IDE Security Plugins**

**IDE Plugins Available?** Yes/No

- **Plugin Name:** SonarLint, Snyk IDE plugin, Other
- **Supported IDEs:** VS Code, IntelliJ IDEA, Visual Studio, Eclipse, Other
- **Plugin Deployment:** Mandatory, Recommended, Optional, Not available

**IDE Plugin Adoption:**

- **Developers with Plugin:** Number / Total developers = X%
- **Plugin Usage:** Active, Occasional, Installed but not used

**Scoring:**

Calculate **Security Tools Deployment Score**:
```
Score = Average of:

- SAST Deployment & Usage (0-100%)
- SCA Deployment & Usage (0-100%)
- Secret Scanning Deployment (0-100%)
- IDE Plugin Adoption (0-100%)

```

**Completion Tips:**

- Check CI/CD pipeline configuration (verify tools are actually integrated)
- Review SAST/SCA dashboards (verify scans are running)
- Check recent scan results (are findings actually reviewed?)
- Interview developers about IDE plugin usage (not just installation)
- Look at vulnerability remediation time (are findings fixed promptly?)

**Common Mistakes:**

- ❌ Marking "Deployed" when tool exists but isn't used
- ❌ Not checking scan frequency (tool installed but scans disabled)
- ❌ Not verifying findings are reviewed (scan runs but nobody looks at results)
- ❌ Assuming IDE plugins are used because they're available

## Sheet 6: Security_Tools_Usage

**Purpose:** Track security tool usage metrics per application.

**Completion Time:** 30 minutes

**Key Assessment Areas:**

**A. Tool Usage Metrics Per Application**

For each application, document:

- **SAST Scans Per Month:** How many SAST scans run monthly?
- **SCA Scans Per Month:** How many SCA scans run monthly?
- **Secret Scanning Enabled?** Is secret scanning enabled (Yes/No)?
- **DAST Scans Per Release:** How many DAST scans per release?
- **Avg Remediation Time (days):** Average days from finding to remediation
- **Tool Integration Score:** Excellent/Good/Adequate/Poor

**B. Usage Compliance Calculation**

Usage compliance score is calculated based on:
- SAST scans ≥4/month = 25%
- SCA scans ≥4/month = 25%
- Secret Scanning enabled = 25%
- DAST scans ≥1/release = 25%

**Completion Tips:**

- Pull scan counts from CI/CD pipeline logs
- Check remediation time from defect tracking system
- Verify integration with development workflow
- Compare usage across applications to identify best practices

**Common Mistakes:**

- ❌ Counting manual ad-hoc scans as regular usage
- ❌ Not checking if scan results are actually reviewed
- ❌ Accepting low scan frequency for high-risk applications
- ❌ Ignoring remediation time when assessing tool effectiveness

## Sheet 7: Developer_Training

**Purpose:** Assess developer security training completion and effectiveness.

**Completion Time:** 30 minutes

**Key Assessment Areas:**

**A. Security Training Requirements**

- **Initial Training Required?** Yes/No (Before writing production code)
- **Annual Refresher Required?** Yes/No
- **Training Duration:** Hours (e.g., 4 hours initial, 2 hours annual)
- **Training Topics:** OWASP Top 10, Secure coding, Tool usage, Threat modeling, Other

**B. Training Delivery**

- **Delivery Method:** Instructor-led, Online/self-paced, Hands-on labs, Mixed
- **Training Provider:** Internal security team, External provider (SANS, OWASP, etc.), Online platform (Pluralsight, Udemy, etc.)
- **Training Content Quality:** Excellent, Good, Adequate, Poor

**C. Training Completion Tracking** (Last 12 months)

- **Total Developers:** Number
- **Completed Initial Training:** Number
- **Completed Annual Refresher:** Number
- **Training Compliance Rate:** (Completed / Total) × 100%
- **Overdue Training:** Number of developers

**D. Training Effectiveness**

- **Assessment/Quiz?** Yes/No (Do trainees take assessment?)
- **Passing Rate:** X% (if assessment exists)
- **Hands-On Exercises?** Yes/No (Do trainees practice secure coding?)

**Developer Feedback** (Sample 2-3 developers):

- **Training Relevant?** Yes/Partially/No
- **Training Practical?** Yes/Partially/No
- **Training Helpful?** Yes/Partially/No
- **Suggestions for Improvement:** [Free text]

**E. Just-in-Time Training**

- **Critical Vulnerability Training?** Yes/No (e.g., Log4Shell training when it emerged)
- **New Tool Training?** Yes/No (e.g., SAST tool usage training)
- **Incident-Based Training?** Yes/No (e.g., training after security incident)

**Scoring:**

Calculate **Developer Training Maturity Score**:
```
Score = Average of:

- Training Completion Rate (0-100%)
- Training Content Quality (0-100%)
- Training Effectiveness (0-100%)
- Just-in-Time Training (0-100%)

```

**Completion Tips:**

- Pull training completion data from HR/training system (don't rely on memory)
- Check for overdue training (developers who joined recently but not trained)
- Interview developers about training quality (not just managers)
- Review training content (is it relevant to technology stack?)
- Check if training is updated for new threats (e.g., Log4Shell added to curriculum)

**Common Mistakes:**

- ❌ Marking "Completed" based on manager statement (verify with records)
- ❌ Not checking training currency (developer trained 5 years ago counts as "trained")
- ❌ Accepting generic "security awareness" as secure coding training
- ❌ Not assessing training effectiveness (completion ≠ effectiveness)

## Sheet 8: Security_Defect_Management

**Purpose:** Assess security defect tracking and remediation.

**Completion Time:** 30-45 minutes

**Key Assessment Areas:**

**A. Security Defect Tracking Process**

- **Security Defects Tracked Separately?** Yes/No (Separate from functional defects)
- **Tracking System:** Jira, Azure DevOps, GitHub Issues, Other
- **Security Labels/Tags:** How are security defects identified? (Label: security, Tag: vulnerability, Priority: security)
- **Severity Classification:** Critical, High, Medium, Low (aligned with vulnerability scoring)

**B. Security Defect Sources**

Security defects identified from:

- [ ] SAST scan findings
- [ ] SCA scan findings (vulnerable dependencies)
- [ ] DAST scan findings
- [ ] Code review findings
- [ ] Penetration testing findings
- [ ] Security incident root cause
- [ ] Threat model updates

**C. Security Defect Remediation SLAs** (From policy)

| Severity | Remediation SLA |
|----------|----------------|
| Critical | 7 days |
| High | 30 days |
| Medium | 90 days |
| Low | 180 days |

**D. Open Security Defects** (Current snapshot)

- **Total Open Defects:** Number
- **Critical Open:** Number
- **High Open:** Number
- **Medium Open:** Number
- **Low Open:** Number
- **Overdue Defects:** Number (past SLA)
- **Average Age (Open Defects):** Days

**E. Security Defect Remediation Metrics** (Last 3 months)

- **Defects Created:** Number
- **Defects Closed:** Number
- **Average Remediation Time (Closed Defects):** Days
- **SLA Compliance Rate:** (Closed within SLA / Total Closed) × 100%

**Critical/High Defects Breakdown:**

- **Critical Defects Created:** Number
- **Critical Defects Closed:** Number
- **Critical Avg Remediation Time:** Days
- **Critical SLA Compliance:** %

- **High Defects Created:** Number
- **High Defects Closed:** Number
- **High Avg Remediation Time:** Days
- **High SLA Compliance:** %

**F. Security Technical Debt**

- **Security Defects Deferred:** Number (accepted as technical debt)
- **Deferred Defect Age:** Average age of deferred defects
- **Remediation Plan?** Yes/No (Is there a plan to fix deferred defects?)

**Scoring:**

Calculate **Security Defect Management Score**:
```
Score = Average of:

- Defect Tracking Process (0-100%)
- SLA Compliance Rate (0-100%)
- Overdue Defects (inverse - fewer overdue = higher score)
- Remediation Speed (0-100% based on avg time vs. SLA)

```

**Completion Tips:**

- Pull defect data from tracking system (Jira query, Azure DevOps query)
- Check for stale defects (open for >1 year)
- Verify severity classification is accurate (not all marked "Low" to avoid SLA)
- Look at remediation trends (improving or worsening?)
- Check if deferred defects have compensating controls

**Common Mistakes:**

- ❌ Not distinguishing security defects from functional defects
- ❌ Accepting inaccurate severity (Critical marked as Low to avoid SLA)
- ❌ Not tracking overdue defects (no visibility into SLA violations)
- ❌ Not checking technical debt (deferred defects accumulate over time)

## Sheet 9: Compliance_Summary

**Purpose:** Calculate overall SDLC security compliance scores and identify gaps.

**Completion Time:** 15-30 minutes (after completing Sheets 2-7)

**Dashboard Components:**

**A. Maturity Scores** (Auto-calculated from Sheets 2-7)

| Assessment Area | Score | Interpretation |
|----------------|-------|----------------|
| SDLC Phase Activities | X% | [Formula from Sheet 2] |
| Secure Coding Standards | X% | [Formula from Sheet 3] |
| Code Review Execution | X% | [Formula from Sheet 4] |
| Security Tools Deployment | X% | [Formula from Sheet 5] |
| Developer Training | X% | [Formula from Sheet 6] |
| Security Defect Management | X% | [Formula from Sheet 7] |
| **Overall SDLC Security Maturity** | **X%** | **[Average of above]** |

**B. Maturity Level Classification**

Based on overall score:

- **90-100%:** Level 4-5 (Quantitatively Managed / Optimizing)
- **70-89%:** Level 3 (Defined)
- **50-69%:** Level 2 (Managed)
- **<50%:** Level 1 (Initial/Ad Hoc)

**C. Gap Summary** (Auto-populated from Sheets 2-7)

Top 5 Gaps (lowest scoring areas):
1. [Gap area] - [Score] - [Brief description]
2. [Gap area] - [Score] - [Brief description]
3. [Gap area] - [Score] - [Brief description]
4. [Gap area] - [Score] - [Brief description]
5. [Gap area] - [Score] - [Brief description]

**D. Improvement Recommendations**

For each gap, provide recommendation:

- **Gap:** [Description]
- **Current State:** [What's missing or inadequate]
- **Target State:** [What should be achieved]
- **Recommendation:** [Specific action]
- **Effort:** Low/Medium/High
- **Priority:** P1/P2/P3/P4

**E. Maturity Roadmap** (Optional)

If current maturity is <Level 3, provide phased roadmap:

**Phase 1 (0-6 months):** Quick wins

- [Action 1]
- [Action 2]
- [Action 3]

**Phase 2 (6-12 months):** Foundation building

- [Action 1]
- [Action 2]
- [Action 3]

**Phase 3 (12-18 months):** Advanced capabilities

- [Action 1]
- [Action 2]
- [Action 3]

**Completion Tips:**

- Review all scores before finalizing (verify they make sense)
- Prioritize gaps by impact and effort (quick wins first)
- Be specific in recommendations (not "improve security")
- Consider dependencies (some improvements require others first)
- Align recommendations with organisational maturity and resources

**Common Mistakes:**

- ❌ Generic recommendations ("improve security processes")
- ❌ Unrealistic roadmap (trying to jump from Level 1 to Level 5 in 3 months)
- ❌ Not prioritizing (recommending 20 actions with no prioritization)
- ❌ Ignoring resource constraints (recommending expensive tools for small team)

## Sheet 10: Evidence_Register

**Purpose:** Centralized register of all SDLC security evidence for audit readiness.

**Completion Time:** 15-30 minutes

**Key Fields:**

- **Evidence Type:** Category of evidence (SDLC Checklist, Code Review Record, SAST Report, Training Certificate, etc.)
- **Application/Team Name:** Which application or team this evidence relates to
- **Document Title/Description:** Brief description of the evidence document
- **Document Location/Link:** File path or URL to access the evidence
- **Last Updated:** Date evidence was last updated
- **Owner:** Person responsible for maintaining this evidence
- **Status:** Current, Outdated, or Missing

**Evidence Types to Track:**

- SDLC security checklists
- Code review records and dashboards
- SAST/SCA/DAST scan reports
- Security training completion certificates
- Security champion meeting minutes
- Threat modeling documents
- Security architecture review reports

**Completion Tips:**

- Maintain a centralized evidence repository (SharePoint, Confluence, etc.)
- Use consistent naming conventions for evidence documents
- Update evidence register whenever new evidence is collected
- Mark outdated evidence clearly and schedule updates

**Common Mistakes:**

- ❌ Storing evidence only on local machines (not accessible for audits)
- ❌ Not updating evidence status when documents become outdated
- ❌ Missing evidence for key activities (especially training)
- ❌ Not linking evidence to specific applications/teams

## Sheet 11: Approval_Sign_Off

**Purpose:** Stakeholder review and approval workflow for the assessment.

**Completion Time:** 10-15 minutes (after obtaining approvals)

**Key Sections:**

**A. Assessment Information**

- Assessment Date
- Assessed By (assessor name)
- Organisation
- Assessment Period (e.g., Q1 2025)
- Total Applications Assessed

**B. Approval Sign-Off**

Required approvers:
1. **Security Architect:** Validates security assessment findings
2. **Development Manager:** Acknowledges development team findings
3. **DevOps Lead:** Confirms CI/CD and tool integration findings
4. **CISO / Security Leadership:** Final approval

**C. Overall Compliance Determination**

- Overall SDLC Compliance Status: ✅ Compliant / ⚠️ Partial Compliance / ❌ Non-Compliant
- Overall Compliance Score: X%

**Completion Tips:**

- Schedule approval meetings in advance
- Share draft findings with approvers before formal review
- Document any disagreements or clarifications in comments
- Obtain all signatures before finalizing assessment

**Common Mistakes:**

- ❌ Submitting for approval without all data completed
- ❌ Not pre-briefing approvers on findings
- ❌ Missing signatures from key stakeholders
- ❌ Not documenting overall compliance status

---

# Evidence Collection

## Evidence Requirements

**Principle:** Every assessment finding must be supported by verifiable evidence.

**Evidence Standards:**

- **Authentic:** Evidence is genuine and from authoritative source
- **Accurate:** Evidence is factually correct and not misleading
- **Complete:** Evidence contains all necessary information
- **Timely:** Evidence is current (not outdated)
- **Relevant:** Evidence directly supports the assessment finding

## Evidence Types by Sheet

**Sheet 2 (SDLC Phase Activities):**

- Sprint retrospective notes (security topics discussed)
- SDLC process documentation with security activities
- Security gate checklists (completed)
- Threat modeling documents
- Security architecture review reports
- Deployment checklists with security sections
- Screenshots of CI/CD pipeline (security steps)

**Sheet 3 (Secure Coding Standards):**

- Secure coding standards document
- Screenshots of SonarQube rules configuration
- Developer interview notes
- Code review comments referencing standards
- SAST tool violation reports

**Sheet 4 (Code Review Execution):**

- Pull request/merge request reports (statistics)
- Branch protection rules screenshot
- Sample code review comments
- Security review checklist (completed examples)
- Git log excerpts showing review activity

**Sheet 5 (Security Tools):**

- SAST tool configuration screenshots
- SCA tool scan results dashboard
- CI/CD pipeline configuration (security steps)
- Tool usage reports (scan frequency, coverage)
- Secret scanning alerts/reports

**Sheet 6 (Developer Training):**

- Training completion reports
- Training certificates
- Training curriculum documentation
- Training feedback surveys
- Training assessment results

**Sheet 7 (Security Defect Management):**

- Jira/Azure DevOps query results (security defects)
- Defect remediation metrics reports
- Sample security defect tickets
- SLA compliance reports
- Technical debt tracking

## Evidence Collection Methods

**System Queries:**

- Git: `git log --grep="security" --since="3 months ago"`
- Jira: Filter security defects by severity, status, creation date
- SonarQube: Export security findings report
- Snyk: Export vulnerability report

**Screenshots:**

- CI/CD pipeline security steps
- SAST/SCA dashboard
- Training completion dashboard
- Branch protection rules
- Tool configuration

**Document Review:**

- SDLC process documentation
- Secure coding standards
- Code review guidelines
- Training materials

**Interviews:**

- Developer interviews (2-3 developers)
- Development Manager interview
- Security Champion interview

## Evidence Storage and Organisation

**Folder Structure:**
```
/Assessments/A825-SDLC-Activities/[APP-ID]/[YYYYMMDD]/
  ├── Documents/
  │   ├── SDLC_Process_Doc.pdf
  │   ├── Secure_Coding_Standards.pdf
  │   └── Training_Curriculum.pdf
  ├── Screenshots/
  │   ├── CICD_Pipeline_Security_Steps.png
  │   ├── SAST_Dashboard.png
  │   ├── SCA_Results.png
  │   └── Training_Completion.png
  ├── Reports/
  │   ├── PR_Statistics_Q4_2025.xlsx
  │   ├── Defect_Metrics_Q4_2025.xlsx
  │   └── SAST_Findings_Summary.pdf
  ├── Interview_Notes/
  │   ├── Developer_Interview_1.docx
  │   ├── Developer_Interview_2.docx
  │   └── DevManager_Interview.docx
  └── Workbook/
      └── ISMS-A825-SDLC-APP-CUST-20260123.xlsx
```

**Retention:** Audit cycle + 1 year minimum

---

# Common Pitfalls

## Mistake 1: Assessing Documentation Instead of Reality

**Problem:** Assessor reviews SDLC process documentation showing "security review required at each phase" and marks all activities as "Executed" without verifying they actually happen.

**Impact:** False compliance. Audit finds documentation exists but activities not performed.

**Solution:** Always verify execution. Check recent sprints/releases. Interview developers. Review actual artifacts (pull requests, defect tickets, scan results).

## Mistake 2: Accepting "We Use Tool X" as Full Compliance

**Problem:** Development Manager says "We use SonarQube" and assessor marks SAST as fully deployed. Tool is installed but scans disabled, findings not reviewed.

**Impact:** Tool exists but provides no security value.

**Solution:** Check tool is actually running (recent scan results). Verify findings are reviewed (sample recent scans). Check if findings are remediated (track defect closure).

## Mistake 3: Sampling Only Recent/Best Examples

**Problem:** Assessor reviews most recent sprint which happened to be excellent, misses that previous 5 sprints had poor security practices.

**Impact:** Assessment shows better maturity than reality.

**Solution:** Sample multiple sprints/releases (last 2-3 months). Look at trends. Don't cherry-pick best examples.

## Mistake 4: Not Distinguishing "Available" from "Used"

**Problem:** IDE security plugins are available for download. Assessor marks as "Deployed" even though only 10% of developers installed them.

**Impact:** Overstates tool adoption.

**Solution:** Check actual adoption metrics. Interview developers about usage. Verify plugin telemetry if available.

## Mistake 5: Trusting Training Completion Without Effectiveness

**Problem:** All developers completed 30-minute "security awareness" video. Assessor marks training as complete. Training was generic, not secure coding specific.

**Impact:** Training compliance looks good but developers lack secure coding skills.

**Solution:** Check training content quality and relevance. Assess effectiveness (quiz results, practical exercises). Interview developers about what they learned.

## Mistake 6: Ignoring Security Champion Absence

**Problem:** Team has no Security Champion. All security activities depend on external security team. Assessor doesn't note this as a gap.

**Impact:** Security activities are bottlenecked. Team lacks security expertise.

**Solution:** Note Security Champion presence/absence. If absent, recommend establishing one. Check if external security team is sufficient.

## Mistake 7: Not Checking SLA Compliance for Defect Remediation

**Problem:** Assessor sees security defects are tracked but doesn't check remediation time. Many defects are 6+ months old, well past SLA.

**Impact:** Defect tracking looks good but remediation is inadequate.

**Solution:** Always check remediation time and SLA compliance. Look for overdue defects. Check trends (is backlog growing?).

## Mistake 8: Accepting Generic "Code Review" as Security Review

**Problem:** Team does peer code review for quality. Assessor marks security code review as complete. Reviews don't actually check for security issues.

**Impact:** Code review exists but doesn't provide security value.

**Solution:** Distinguish peer review (quality) from security review (security). Check if reviewers have security knowledge. Sample reviews for security comments.

## Mistake 9: Not Accounting for SDLC Methodology Differences

**Problem:** Assessor evaluates Agile team using Waterfall security gate criteria. Team doesn't have formal phase gates (it's sprints), marked as non-compliant.

**Impact:** Unfair assessment. Team may be doing security well but differently.

**Solution:** Adapt assessment to SDLC methodology. Agile: Check security in sprints, DoD, retrospectives. Waterfall: Check phase gates, formal reviews.

## Mistake 10: Not Providing Actionable Recommendations

**Problem:** Assessment identifies gaps but recommendations are vague: "Improve security practices", "Enhance tool usage", "Increase training".

**Impact:** Team doesn't know what to do. No improvement happens.

**Solution:** Be specific. "Deploy SAST in CI/CD pipeline with Critical/High findings blocking builds. Target: Within 3 months." Provide effort estimate, priority, and owner.

---

# Quality Checklist

Before submitting assessment for peer review, complete this quality checklist:

## Completeness

**All Sheets:**

- [ ] All 11 sheets completed
- [ ] All required fields populated
- [ ] All yellow input cells completed
- [ ] All dropdowns selected
- [ ] All comment fields used where needed

**Sheet-Specific:**

- [ ] Sheet 1: Application/team profile complete and accurate
- [ ] Sheet 2: All SDLC phases assessed (not just some)
- [ ] Sheet 3: Secure coding standards content checked (not just existence)
- [ ] Sheet 4: Code review metrics pulled from system (not estimated)
- [ ] Sheet 5: All tool types assessed (SAST, SCA, secret scanning, IDE)
- [ ] Sheet 6: Training completion data verified from HR system
- [ ] Sheet 7: Defect metrics pulled from tracking system
- [ ] Sheet 8: Recommendations are specific and actionable

## Accuracy

**Data Accuracy:**

- [ ] Metrics are from actual systems (not estimated)
- [ ] Assessment period is clearly stated
- [ ] Dates are correct
- [ ] Team size is accurate
- [ ] Tool names are correct
- [ ] Evidence locations are correct (links work)

**Assessment Accuracy:**

- [ ] "Executed" based on actual verification (not documentation)
- [ ] Tool "Deployed" means actually used (not just installed)
- [ ] Training "Complete" verified with records
- [ ] Scores match underlying data
- [ ] Gaps identified are real gaps

## Evidence

**Evidence Collection:**

- [ ] Evidence collected for all key findings
- [ ] Evidence stored in centralized repository
- [ ] Screenshots are clear and readable
- [ ] Reports are current (not outdated)
- [ ] Interview notes are documented

**Evidence Quality:**

- [ ] Evidence is authentic (from authoritative source)
- [ ] Evidence is complete (not partial)
- [ ] Evidence is timely (recent)
- [ ] Evidence is relevant
- [ ] Evidence is accessible (not on local machine)

## Consistency

**Internal Consistency:**

- [ ] Sheet 8 dashboard matches Sheets 2-7 findings
- [ ] Recommendations address identified gaps
- [ ] Scores make sense given documented findings
- [ ] Tool deployment (Sheet 5) aligns with SDLC activities (Sheet 2)

**Policy Consistency:**

- [ ] Assessment follows ISMS-POL-A.8.25-26-29 Section 3
- [ ] SDLC phases match policy requirements
- [ ] Defect remediation SLAs match policy
- [ ] Training requirements match policy

## Clarity

**Written Content:**

- [ ] Comments are clear and specific
- [ ] Recommendations are specific (not vague)
- [ ] Technical terms are used correctly
- [ ] No typos or grammar errors

**Professional Presentation:**

- [ ] Formatting is consistent
- [ ] No missing or broken formatting
- [ ] Print preview looks professional
- [ ] No placeholder text remains

## Actionability

**Recommendations:**

- [ ] All gaps have recommendations
- [ ] Recommendations are specific and measurable
- [ ] Effort estimates provided
- [ ] Priorities assigned
- [ ] Owners suggested

## Stakeholder Review Readiness

**Pre-Submission:**

- [ ] Self-review completed (this checklist)
- [ ] Development Manager pre-briefed on findings
- [ ] Security Champion pre-briefed (if exists)
- [ ] Evidence package complete
- [ ] Peer reviewer identified (Security Architect)

---

# Review & Approval

## Stakeholder Review Process

**Step 1: Development Manager Review**

- Share draft findings with Development Manager
- Walk through key findings and gaps
- Address any factual corrections
- Obtain Development Manager acknowledgment

**Step 2: Security Champion Review** (if exists)

- Share draft with Security Champion
- Validate security activities assessment
- Address any factual corrections
- Obtain Security Champion acknowledgment

**Step 3: Security Architect Peer Review**

- Submit for formal peer review
- Security Architect validates findings
- Security Architect validates evidence
- Security Architect provides feedback

**Step 4: Address Feedback**

- Assessor addresses feedback (3-5 business days)
- Updates workbook as needed
- Re-submits for approval

**Step 5: Final Approval**

- Security Architect approves
- Development Manager acknowledges
- Document approval in Sheet 8

## Post-Approval Actions

**Communicate Results:**

- Send assessment summary to Development Manager, Security Champion, team
- Highlight key findings (strengths, gaps, recommendations)
- Provide link to full assessment

**Track Improvements:**

- Create action items for recommendations
- Assign owners and due dates
- Track in team backlog or improvement register
- Schedule follow-up reviews

**Archive Assessment:**

- Move to archive folder
- Ensure evidence package is complete
- Update assessment tracking register

**Schedule Next Assessment:**

- High-Risk: Quarterly
- Medium-Risk: Semi-annually
- Low-Risk: Annually
- Document next assessment date

---

# Conclusion

This completes **PART I: USER COMPLETION GUIDE** for SDLC Security Activities Assessment.

**Key Takeaways:**
1. Assess reality, not documentation - verify activities actually happen
2. Use actual system data - don't estimate or guess
3. Distinguish availability from usage - tools/training must be used, not just available
4. Sample multiple time periods - don't cherry-pick best examples
5. Provide actionable recommendations - be specific, not vague

**Remember:**

- Verify, don't assume - always check actual execution
- Pull metrics from systems - Jira queries, Git stats, tool dashboards
- Interview developers - manager's view may differ from reality
- Focus on effectiveness - compliance ≠ effectiveness
- Be practical - recommendations must be achievable

**Next Steps:**
1. Read the companion Technical Specification (TG)
2. Gather prerequisites for your first assessment
3. Schedule interviews with Development Manager, Security Champion, developers
4. Begin assessment!

Good luck! 📋✅

---

**END OF USER GUIDE**

---

*"Software security is a process, not a feature."*
— Gary McGraw

<!-- QA_VERIFIED: 2026-03-01 -->
