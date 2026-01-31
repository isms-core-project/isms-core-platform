**ISMS-IMP-A.8.25-26-29-S2 - SDLC Security Activities Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.25-26-29-S2 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (Separate section)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formulas & Calculations
  - Data Validation & Conditional Formatting


---

# PART I: USER COMPLETION GUIDE

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
- Portfolio-wide dashboard (see IMP-S5)


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
- [ ] Compliance requirements identified (GDPR, PCI DSS, etc.)
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
- [ ] Authorization (access control, privilege management)
- [ ] Cryptography (encryption algorithms, key management, TLS)
- [ ] Error handling (secure error messages, no information disclosure)
- [ ] Logging (security event logging, log protection)
- [ ] Data protection (sensitive data handling, PII protection)
- [ ] API security (authentication, authorization, input validation, rate limiting)
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

- [ ] Authentication and authorization logic
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
- Align recommendations with organizational maturity and resources


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
- Organization
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


## Evidence Storage and Organization

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
1. Read PART II: Technical Specification
2. Gather prerequisites for your first assessment
3. Schedule interviews with Development Manager, Security Champion, developers
4. Begin assessment!

Good luck! 📋✅

---

**END OF PART I: USER COMPLETION GUIDE**

**PART II: TECHNICAL SPECIFICATION** will be provided in the next section with detailed Excel workbook structure, column definitions, formulas, data validation rules, and Python script integration guidance.
# ISMS-IMP-A.8.25-26-29-S2 - SDLC Security Activities Assessment
# PART II: TECHNICAL SPECIFICATION

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
*Where bamboo antennas actually work.* 🎋
