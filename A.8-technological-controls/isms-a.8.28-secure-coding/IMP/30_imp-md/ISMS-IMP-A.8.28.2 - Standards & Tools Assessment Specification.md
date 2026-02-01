**ISMS-IMP-A.8.28.2 - Standards & Tools Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.2 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Question-by-Question Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Formulas & Calculations
  - Python Script Integration Points


**Target Audiences:**

- **Part I:** Assessment users (Application Security Team, Security Architects, Development Managers, DevOps Engineers)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** Application Security Team, Security Architects, Development Managers, DevOps Engineers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.28.2 - Standards & Tools Assessment

### What This Assessment Evaluates

This assessment evaluates the **implementation and effectiveness** of secure coding standards and security tools within the software development lifecycle. It focuses on deployment AND actual security improvement - not just whether tools exist, but whether they're configured properly, integrated into workflows, and actually reducing vulnerabilities.

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled." - Richard Feynman*

**Application**: Having tools deployed but not configured = cargo cult security. This assessment measures BOTH deployment (do we have tools?) AND effectiveness (are they working?).

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.28: Secure Coding
- ISMS-POL-A.8.28 Section 2.2: Secure Coding Standards
- ISMS-POL-A.8.28 Section 2.3: Code Review & Testing Requirements


Organizations with effective security tool implementation see:

- 60-80% reduction in security vulnerabilities reaching production
- 40-60% faster vulnerability remediation (SAST findings vs. production incidents)
- 70-90% reduction in secret leakage incidents (pre-commit hooks)
- Developer productivity maintained or improved (shift-left approach)


Organizations with ineffective tool implementation experience:

- Tools deployed but ignored ("alert fatigue" from false positives)
- Security theater (tools report findings, nothing gets fixed)
- Developer frustration (tools slow workflow without value)
- Wasted budget (tools licensed but not used effectively)


### What You'll Document

This assessment captures ACTUAL tool implementation and effectiveness:

1. **Coding Standards Adoption**: Documentation, training, enforcement, compliance measurement
2. **SAST & SCA Tools**: Deployment, configuration, CI/CD integration, finding remediation
3. **DAST & Testing Tools**: Dynamic testing, API security, container/IaC scanning
4. **IDE Plugins & Linters**: Developer-facing tools, adoption rates, usability
5. **Tool Effectiveness**: KPIs, false positive rates, vulnerability trends, ROI

### Key Principle

**Evidence-Based + Metrics-Driven**: This assessment requires BOTH:

- **Qualitative evidence**: Tool configurations, pipeline integration, documentation
- **Quantitative metrics**: False positive rates, coverage percentages, MTTR, vulnerability trends


If you can't measure effectiveness, you're doing cargo cult security.

### Who Should Complete This Assessment

**Primary Role**: Application Security Lead or Security Architect (owns security tooling strategy)

**Required Collaborators**:

- **DevOps Engineers**: CI/CD pipeline integration, tool configuration
- **Tool Administrators**: License status, deployment details, metrics extraction
- **Development Managers**: Developer adoption rates, tool usability feedback
- **Security Champions**: On-the-ground tool effectiveness observations


**Time Commitment**: 16-20 hours total (distributed across 2-3 weeks)

- Tool inventory and documentation: 4-6 hours
- Configuration review: 4-6 hours
- Metrics extraction and analysis: 4-6 hours
- Evidence collection: 2-3 hours
- Assessment completion: 2-3 hours
- Review and approval: 1-2 hours


### Expected Outputs

**Primary Output**: Excel workbook `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`

**Contents**:

- 5 assessment domain sheets (Standards, SAST/SCA, DAST, IDE Plugins, Effectiveness)
- Tool inventory (what tools deployed, versions, licenses)
- Configuration evidence (rulesets, quality gates, integration)
- Metrics dashboard (false positive rates, coverage, MTTR)
- Gap analysis (gaps with remediation plans)
- Evidence register


**Deliverables**:

- Completed Excel workbook
- Tool configuration exports (pipeline configs, ruleset files)
- Metrics reports (dashboards, trend analysis)
- Executive summary (1-page for CISO/management)


---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

**Secure Coding Standards Documentation**:

- [ ] Published secure coding standards (wiki, PDF, document management system)
- [ ] Language-specific guidelines (Python, Java, JavaScript, etc.)
- [ ] OWASP Top 10 and CWE Top 25 coverage documentation
- [ ] Training materials referencing standards
- [ ] Code review checklists based on standards
- [ ] Standards review/update history (last review date)


**SAST Tool Information**:

- [ ] SAST tool name, vendor, version (e.g., SonarQube 10.4, Checkmarx, Fortify)
- [ ] License information (expiration dates, user limits)
- [ ] Deployment architecture documentation
- [ ] Language coverage configuration (which languages scanned)
- [ ] Ruleset configuration files (what rules enabled)
- [ ] CI/CD integration evidence (pipeline YAML files, Jenkinsfiles)
- [ ] Quality gate configuration (what severity blocks builds)
- [ ] False positive suppression audit trail
- [ ] Finding statistics (last 3-6 months)


**SCA Tool Information**:

- [ ] SCA tool name, vendor, version (e.g., Snyk, WhiteSource, Dependabot)
- [ ] License information
- [ ] Repository integration configuration
- [ ] CVE detection settings
- [ ] License compliance policy configuration
- [ ] Quality gate configuration
- [ ] Vulnerability statistics (last 3-6 months)
- [ ] Remediation tracking (upgrade recommendations, SBOM generation)


**DAST Tool Information**:

- [ ] DAST tool name, vendor, version (e.g., OWASP ZAP, Burp Suite, Acunetix)
- [ ] Scan schedules and coverage (which apps scanned, frequency)
- [ ] Authenticated vs. unauthenticated scan configuration
- [ ] API testing tool configuration (Postman, REST-Assured, SoapUI)
- [ ] Container scanning tool (Trivy, Clair, Anchore Engine)
- [ ] IaC scanning tool (Checkov, tfsec, Terrascan, Snyk Infrastructure as Code)
- [ ] Scan results (last 3-6 months)


**IDE Plugin & Linter Information**:

- [ ] Available IDE security plugins (VS Code, IntelliJ, PyCharm)
- [ ] Plugin adoption metrics (telemetry data, installation counts)
- [ ] Linter configuration files (ESLint, Pylint, RuboCop with security rules)
- [ ] Pre-commit hook configurations (secret detection - Gitleaks, TruffleHog, git-secrets)
- [ ] Secret detection statistics (secrets blocked, false positives)
- [ ] Developer feedback (surveys, usability complaints)


**Tool Effectiveness Metrics**:

- [ ] Vulnerability detection rates by tool (SAST vs. SCA vs. DAST vs. Manual)
- [ ] False positive rates (% of findings marked as false positives)
- [ ] Mean Time to Remediation (MTTR) - from detection to fix deployment
- [ ] Coverage metrics (% of codebase scanned, % of repositories with security gates)
- [ ] Vulnerability trend analysis (are findings decreasing over time?)
- [ ] Tool cost documentation (licenses, support, training)
- [ ] Developer productivity impact (build time increases, workflow delays)


## Required Tools

**Software**:

- Microsoft Excel 2016+ or compatible spreadsheet application
- Access to security tool dashboards (SonarQube, Snyk, etc.)
- Access to CI/CD platform (Jenkins, GitHub Actions, GitLab CI, Azure DevOps)
- Access to code repositories (GitHub, GitLab, Bitbucket)
- Access to issue tracking system (Jira, Azure DevOps, GitHub Issues)


**Access Permissions**:

- Security tool admin or read-only admin access (to export configs and metrics)
- CI/CD pipeline read access (to review pipeline configs)
- Repository admin or read access (to review integrations, pre-commit hooks)
- Issue tracking read access (to review vulnerability remediation tracking)
- Tool license management access (to verify license status and expiration)


**Optional Tools** (helpful but not required):

- Screenshot tool (for capturing dashboard evidence)
- Config export scripts (for exporting tool configurations)
- Metrics visualization tool (for trend analysis)


## Required Skills

**Assessor should have**:

- Understanding of software development lifecycle and tooling
- Familiarity with security tools (SAST, SCA, DAST concepts)
- Ability to review CI/CD pipeline configurations
- Basic understanding of metrics and KPIs
- Ability to interpret tool dashboards and reports


**Assessor does NOT need**:

- Deep security tool expert knowledge (admin-level)
- Development expertise in all languages
- Security researcher-level vulnerability knowledge


## Dependencies

**Must Complete BEFORE This Assessment**:

- ISMS-POL-A.8.28 (Secure Coding Policy) approved and published


**Should Have But Not Blocking**:

- ISMS-IMP-A.8.28.1 (SDLC Assessment) completed (provides context on training, planning)
- At least some security tools deployed (even if partially configured)


**Related Assessments** (coordinate timing):

- ISMS-IMP-A.8.28.3 (Code Review & Testing) - can be done in parallel
- ISMS-IMP-A.8.28.4 (Third-Party & OSS) - overlaps with SCA assessment
- ISMS-IMP-A.8.28.5 (Compliance Dashboard) - requires IMPs 1-4 completed first


---

# Assessment Workflow

## Step-by-Step Process

**Phase 1: Preparation (Week 1, Days 1-2)**

**Step 1**: Generate Excel workbook

- Run Python script: `python3 generate_a828_2_standards_tools.py`
- Output: `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`
- Save to shared location for collaboration


**Step 2**: Review Instructions sheet

- Read assessment methodology
- Understand tool effectiveness focus (not just deployment)
- Review status definitions and compliance scoring
- Understand evidence requirements


**Step 3**: Schedule stakeholder meetings

- DevOps Engineers (2 hours): CI/CD integration, pipeline configs, deployment
- Tool Administrators (1 hour): Licenses, metrics, configuration details
- Development Managers (1 hour): Adoption rates, developer feedback
- Security Champions (30 min): On-the-ground effectiveness observations


**Phase 2: Tool Inventory & Documentation (Week 1, Days 3-5)**

**Step 4**: Document Security Tools Deployed

- Create inventory: Tool name, vendor, version, license expiration
- For each tool category (SAST, SCA, DAST, IDE plugins):
  - Identify all deployed tools
  - Document deployment date and current status (active, pilot, deprecated)
  - Verify license validity


**Step 5**: Collect Tool Configuration Evidence

- SAST: Export ruleset configurations, quality gate settings
- SCA: Export CVE detection policies, license compliance rules
- DAST: Document scan schedules, authentication configs
- CI/CD: Export pipeline YAML files showing tool integration
- Pre-commit hooks: Export hook configurations from repositories


**Step 6**: Extract Tool Metrics

- False positive rates (last quarter): % of findings suppressed/closed as FP
- Coverage metrics: % of repositories with security scans enabled
- Finding statistics: Count by severity (Critical/High/Medium/Low), trend over time
- MTTR: Average days from finding detection to fix deployment
- Developer adoption: % of developers using IDE plugins, pre-commit hooks


**Phase 3: Standards Documentation Review (Week 1-2, Days 3-7)**

**Step 7**: Review Secure Coding Standards

- Locate published standards document
- Verify OWASP Top 10 coverage (all 10 categories addressed)
- Verify CWE Top 25 coverage (at least top 10 addressed)
- Check language-specific guidelines (Python, Java, JavaScript, etc.)
- Verify last review date (should be within 12 months)


**Step 8**: Assess Standards Adoption

- Review training records (% developers trained on standards)
- Review code review checklists (do they reference standards?)
- Interview Security Champions (do developers actually follow standards?)
- Check for documented exceptions (standards too strict/unrealistic?)


**Phase 4: Assessment Completion (Week 2-3, Days 8-15)**

**Step 9**: Complete Domain 1: Coding Standards Adoption

- For each assessment question, select status from dropdown
- Provide evidence (standards doc location, training records, metrics)
- Calculate adoption rates (% developers trained, % code reviews referencing standards)


**Step 10**: Complete Domain 2: SAST & SCA Tools

- Document tool deployment (SAST tool name, version, languages covered)
- Verify CI/CD integration (scan on every build? quality gates configured?)
- Assess finding remediation (are findings tracked? are SLAs met?)
- Calculate false positive rate (target: <20%)


**Step 11**: Complete Domain 3: DAST & Security Testing

- Document DAST tool deployment and scan coverage
- Verify pre-release scanning (scans before production deployment?)
- Assess API security testing (authenticated testing? fuzzing?)
- Document container and IaC scanning


**Step 12**: Complete Domain 4: IDE Plugins & Linters

- Document available IDE plugins (which IDEs supported?)
- Calculate adoption rate (% developers using plugins - target: >70%)
- Verify pre-commit hook deployment (secret detection working?)
- Assess developer usability feedback


**Step 13**: Complete Domain 5: Tool Effectiveness & Metrics

- Document KPIs (false positive rate, MTTR, coverage, vulnerability trends)
- Assess effectiveness measurement (are KPIs tracked quarterly?)
- Verify continuous improvement (are tools tuned based on metrics?)
- Calculate ROI (vulnerabilities prevented vs. tool cost)


**Phase 5: Review and Finalization (Week 3, Days 16-18)**

**Step 14**: Complete Evidence Register

- For each evidence item, provide:
  - Evidence ID (auto-generated)
  - Description (tool config export, metrics dashboard, scan results)
  - Location (file path, URL, tool dashboard link)
  - Date collected
  - Collected by


**Step 15**: Complete Tool Inventory Sheet

- List all security tools with details (vendor, version, license expiration)
- Mark status (Active, Pilot, Deprecated, Planned)
- Link to evidence for each tool


**Step 16**: Review Gap Analysis Sheet

- Verify all ❌ Non-Compliant and ⚠️ Partial items appear
- Assign remediation owners (who will fix the gap?)
- Set remediation target dates (realistic timelines)
- Prioritize gaps (Critical / High / Medium / Low)


**Step 17**: Review Summary Dashboard

- Verify compliance percentages calculated correctly
- Review overall compliance rate
- Identify top gaps requiring attention (Critical/High priority)
- Prepare executive summary


**Step 18**: Internal Review

- Share workbook with DevOps for validation (CI/CD integration accurate?)
- Share with Tool Administrators for accuracy (tool configs correct?)
- Incorporate feedback and corrections


**Step 19**: Approval Process

- Submit to Application Security Lead for review
- Submit to CISO for approval
- Obtain Development Management concurrence (if tools impact workflows)
- Complete Approval Sign-Off sheet


## Timeline Expectations

**Total Duration**: 2-3 weeks (part-time effort)

**Effort Distribution**:

- Preparation: 2 hours
- Tool inventory and documentation: 6-8 hours
- Configuration review and export: 4-6 hours
- Metrics extraction and analysis: 4-6 hours
- Assessment completion: 4-6 hours
- Evidence collection: 2-3 hours
- Review and finalization: 2-3 hours
- Approval cycle: 3-5 business days


**Critical Path**:

- Tool admin access (may require provisioning - plan ahead)
- Metrics extraction (may require custom queries or reports)
- Developer adoption metrics (may require telemetry data analysis)


## Collaboration Requirements

**Weekly Sync Meeting** (30 minutes):

- Application Security Lead (assessment owner)
- DevOps representative (CI/CD integration)
- Tool Administrator (tool configs, metrics)
- Review progress, blockers, questions


**Ad-Hoc Consultations**:

- DevOps Engineers: Pipeline integration, quality gate configuration
- Tool Administrators: Metrics extraction, dashboard access
- Development Managers: Developer adoption rates, usability feedback
- Security Champions: Tool effectiveness observations


---

# Question-by-Question Guidance

This section provides detailed guidance for completing each assessment domain.

## Domain 1: Coding Standards Adoption

**Assessment Question 1.1**: "Are secure coding standards documented and accessible to all developers?"

**What This Asks**: Does [Organization] have published, accessible secure coding standards that developers can reference?

**Where to Find Evidence**:

- Internal wiki (Confluence, SharePoint, Google Sites)
- Document management system
- Developer onboarding materials
- Code review templates referencing standards


**How to Answer**:

- **✅ Compliant**: Standards documented, published to accessible location (wiki, portal), referenced in onboarding and code reviews
- **⚠️ Partial**: Standards exist but difficult to find, or partially documented (only some languages)
- **❌ Non-Compliant**: No standards document, or standards not accessible to developers
- **🔄 Planned**: Standards being developed, not yet published
- **N/A**: Not applicable (justify - very rare)


**Examples**:

- ✅ **Compliant**: "Secure Coding Standards v2.1" published to developer wiki, linked from onboarding checklist, 95% of developers report knowing where to find standards (annual survey)
- ❌ **Non-Compliant**: Standards document exists as draft on security team drive; developers unaware of its existence


**Policy Reference**: ISMS-POL-A.8.28 Section 2.2.1 (Secure coding standards required)

---

**Assessment Question 1.2**: "Do standards cover OWASP Top 10 and CWE Top 25?"

**What This Asks**: Are the most common vulnerability categories addressed in standards?

**Where to Find Evidence**:

- Standards document table of contents
- Standards document sections mapped to OWASP Top 10 and CWE Top 25
- Training materials covering these vulnerabilities


**How to Answer**:

- **✅ Compliant**: Standards explicitly address all OWASP Top 10 (2021 or later) and at least top 10 CWE vulnerabilities
- **⚠️ Partial**: Standards address most (7-9 of OWASP Top 10) but missing some critical categories
- **❌ Non-Compliant**: Standards address <7 OWASP Top 10 categories, or no coverage of CWE
- **🔄 Planned**: Standards update in progress to add missing coverage
- **N/A**: Not applicable (justify)


**Examples**:

- ✅ **Compliant**: Standards Section 3 "Input Validation" addresses A03:2021 (Injection), Section 5 "Authentication" addresses A07:2021 (ID & Auth Failures), all 10 categories covered
- ❌ **Non-Compliant**: Standards only cover SQL injection and XSS; missing 8 OWASP Top 10 categories


**Policy Reference**: ISMS-POL-A.8.28 Section 2.2.1 (OWASP/CWE coverage required)

---

**Assessment Question 1.3**: "Are language-specific secure coding guidelines provided?"

**What This Asks**: Do standards include language-specific guidance (e.g., Python SQL injection prevention differs from Java)?

**Where to Find Evidence**:

- Language-specific sections in standards document
- ISMS-CTX-A.8.28 (Language-Specific Guidelines) if separated
- Language-specific training modules


**How to Answer**:

- **✅ Compliant**: Guidelines exist for all primary languages used by [Organization] (80%+ of codebase)
- **⚠️ Partial**: Guidelines for some languages (50-79% of codebase), missing others
- **❌ Non-Compliant**: Generic guidelines only (<50% language-specific coverage), or no language-specific guidance
- **🔄 Planned**: Language-specific guidelines being developed
- **N/A**: [Organization] only uses one programming language (specify which - rare)


**Examples**:

- ✅ **Compliant**: [Organization] primary languages: Python (50%), JavaScript (30%), Java (20%); standards include Python SQL parameterization examples, JavaScript XSS prevention (DOMPurify, React auto-escaping), Java PreparedStatement usage
- ❌ **Non-Compliant**: [Organization] uses Python, Java, Go; standards are generic ("use parameterized queries") without language-specific examples


**Policy Reference**: ISMS-POL-A.8.28 Section 2.2.2 (Language-specific guidance required), ISMS-CTX-A.8.28 (technical reference)

---

## Domain 2: SAST & SCA Tools

**Assessment Question 2.1**: "Is SAST tool deployed and integrated into CI/CD pipelines?"

**What This Asks**: Does [Organization] have Static Application Security Testing automated in build process?

**Where to Find Evidence**:

- Tool license documentation (SonarQube, Checkmarx, Fortify, Snyk Code)
- CI/CD pipeline configuration files (Jenkinsfile, .gitlab-ci.yml, GitHub Actions)
- Build logs showing SAST execution
- Tool dashboard showing scan history


**How to Answer**:

- **✅ Compliant**: SAST deployed for all primary languages, automated scans on every commit/PR, integrated into CI/CD
- **⚠️ Partial**: SAST deployed but not all languages covered (70-99%), or manual scans only (not automated)
- **❌ Non-Compliant**: No SAST tool, or SAST deployed but not used (<70% coverage)
- **🔄 Planned**: SAST tool procured, integration in progress
- **N/A**: Not applicable (justify - very rare for development organizations)


**Examples**:

- ✅ **Compliant**: SonarQube 10.4 deployed, integrated into GitHub Actions for Python/Java/JavaScript repos, scans on every PR, 98% of repositories have SAST enabled
- ❌ **Non-Compliant**: Checkmarx license purchased 2 years ago, never configured; no scans performed


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.1 (SAST required)

---

**Assessment Question 2.2**: "Are SAST quality gates configured to block deployment of Critical/High severity findings?"

**What This Asks**: Do security findings actually prevent insecure code from being deployed?

**Where to Find Evidence**:

- Quality gate configuration (SonarQube Quality Gate, Checkmarx policies)
- Pipeline configuration showing build failures on security findings
- Build logs with examples of blocked deployments
- Exception/override audit trail (if quality gates can be bypassed)


**How to Answer**:

- **✅ Compliant**: Quality gates configured to block on Critical/High, enforced (cannot be bypassed by developers), audit trail of any overrides
- **⚠️ Partial**: Quality gates configured but can be bypassed, OR only blocking Critical (not High)
- **❌ Non-Compliant**: No quality gates, or gates not enforced (findings reported but don't block deployment)
- **🔄 Planned**: Quality gates being configured, not yet enforced
- **N/A**: SAST not deployed (would be ❌ in Q2.1)


**Examples**:

- ✅ **Compliant**: SonarQube Quality Gate: "Block if Critical or High severity findings present", pipeline configuration fails build, 12 deployments blocked last quarter (all resolved before re-deployment)
- ❌ **Non-Compliant**: SAST runs but reports only; developers can merge PRs with Critical findings; 45 Critical findings deployed to production last quarter


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.1 (Quality gates required)

---

**Assessment Question 2.3**: "Is false positive rate measured and kept below 20%?"

**What This Asks**: Are SAST findings accurate, or is the tool generating excessive false alarms?

**Where to Find Evidence**:

- SAST dashboard showing total findings vs. suppressed/closed as false positive
- False positive triage logs
- Quarterly effectiveness reviews


**How to Answer**:

- **✅ Compliant**: False positive rate measured quarterly, consistently below 20%, tuning efforts documented
- **⚠️ Partial**: False positive rate 20-40%, improvement efforts underway
- **❌ Non-Compliant**: False positive rate >40%, or not measured
- **🔄 Planned**: Starting to track false positive rate, baseline not yet established
- **N/A**: SAST not deployed


**Examples**:

- ✅ **Compliant**: Q4 2025 metrics: 1,247 SAST findings, 178 marked false positive (14.3%), ruleset tuning reduced FP rate from 28% (Q3) to 14% (Q4)
- ❌ **Non-Compliant**: Developers complain "SAST is useless, all noise"; spot check shows 65% false positive rate; tool ignored


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.1 (Effectiveness measurement required)

---

**Assessment Question 2.4**: "Is SCA tool deployed to detect vulnerable dependencies?"

**What This Asks**: Does [Organization] scan third-party libraries and dependencies for known vulnerabilities (CVEs)?

**Where to Find Evidence**:

- SCA tool license (Snyk, WhiteSource/Mend, Dependabot, GitHub Advanced Security)
- Repository integrations (pull request comments, dependency scan results)
- CVE detection reports
- Vulnerability remediation tracking


**How to Answer**:

- **✅ Compliant**: SCA deployed for all primary languages, automated scans on every build, CVE detection working
- **⚠️ Partial**: SCA deployed for some languages (70-99%), or manual scans only
- **❌ Non-Compliant**: No SCA tool, or SCA not effective (<70% coverage)
- **🔄 Planned**: SCA tool procured, integration in progress
- **N/A**: [Organization] has no third-party dependencies (justify - extremely rare)


**Examples**:

- ✅ **Compliant**: Snyk integrated into GitHub repos, scans on every PR and nightly, detects CVEs in npm/PyPI/Maven dependencies, 95% of repositories monitored
- ❌ **Non-Compliant**: No SCA tool; Log4Shell vulnerability (CVE-2021-44228) discovered in production 3 weeks after public disclosure


**Policy Reference**: ISMS-POL-A.8.28 Section 2.4.1 (SCA required)

---

## Domain 3: DAST & Security Testing Tools

**Assessment Question 3.1**: "Are DAST scans performed before production releases?"

**What This Asks**: Does [Organization] perform dynamic (runtime) security testing before deploying to production?

**Where to Find Evidence**:

- DAST tool deployment (OWASP ZAP, Burp Suite, Acunetix)
- Release checklist showing DAST scan requirement
- Scan reports for recent releases
- Staging environment scan schedules


**How to Answer**:

- **✅ Compliant**: DAST scans mandatory for all production releases, scan results reviewed before deployment, Critical/High findings block release
- **⚠️ Partial**: DAST scans performed for most releases (70-99%), or scans don't block releases
- **❌ Non-Compliant**: No DAST scans, or scans <70% of releases
- **🔄 Planned**: DAST tool procured, integration in progress
- **N/A**: [Organization] has no web applications (justify - rare)


**Examples**:

- ✅ **Compliant**: OWASP ZAP scans staging environment before every production deployment; last 8 releases all scanned; 2 releases delayed due to High severity findings
- ❌ **Non-Compliant**: Burp Suite license purchased; used once for pilot project 18 months ago; no scans since


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.2 (DAST required)

---

**Assessment Question 3.2**: "Are container images scanned for vulnerabilities before deployment?"

**What This Asks**: If using containers (Docker, Kubernetes), are images scanned for OS/library vulnerabilities?

**Where to Find Evidence**:

- Container scanning tool (Trivy, Clair, Anchore, Snyk Container, AWS ECR scanning)
- CI/CD pipeline integration (scan on image build)
- Container registry showing scan results
- Quality gate configuration (block vulnerable images)


**How to Answer**:

- **✅ Compliant**: All container images scanned before deployment, Critical/High vulnerabilities block deployment, scan results retained
- **⚠️ Partial**: Most images scanned (70-99%), or scans don't block deployment
- **❌ Non-Compliant**: No container scanning, or <70% coverage
- **🔄 Planned**: Container scanning being implemented
- **N/A**: [Organization] doesn't use containers (verify - increasingly rare)


**Examples**:

- ✅ **Compliant**: Trivy integrated into Docker build pipeline, scans all images before push to ECR, images with Critical CVEs rejected, 100% of production images scanned
- ❌ **Non-Compliant**: Running containers in production with no vulnerability scanning; discovered vulnerable base image (OS CVE) during incident response


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.2 (Container scanning required if applicable)

---

## Domain 4: IDE Plugins & Linters

**Assessment Question 4.1**: "Are IDE security plugins available and promoted to developers?"

**What This Asks**: Can developers get real-time security feedback in their development environment?

**Where to Find Evidence**:

- Plugin catalog (internal wiki listing recommended plugins)
- Plugin installation guides
- Developer onboarding materials mentioning plugins
- Plugin adoption metrics (telemetry data, if available)


**How to Answer**:

- **✅ Compliant**: Security plugins available for all primary IDEs (VS Code, IntelliJ, PyCharm), promoted in onboarding, adoption >70%
- **⚠️ Partial**: Plugins available but adoption 40-69%, or not all IDEs supported
- **❌ Non-Compliant**: No security plugins, or adoption <40%
- **🔄 Planned**: Plugin evaluation in progress, rollout planned
- **N/A**: [Organization] doesn't use IDEs (justify - very rare)


**Examples**:

- ✅ **Compliant**: VS Code "SonarLint" plugin recommended in onboarding, 78% of developers have installed (telemetry data), provides real-time feedback on code quality and security
- ❌ **Non-Compliant**: No plugin recommendations; developers discover security issues only during PR review or SAST scan (days later)


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.3 (Developer tools encouraged)

---

**Assessment Question 4.2**: "Are pre-commit hooks deployed to detect and block secrets?"

**What This Asks**: Are developers prevented from accidentally committing secrets (API keys, passwords) to repositories?

**Where to Find Evidence**:

- Pre-commit hook configuration files (.pre-commit-config.yaml, .git/hooks/)
- Secret detection tool (Gitleaks, TruffleHog, git-secrets, GitHub Secret Scanning)
- Blocked commit logs (secrets detected and prevented)
- Secret detection statistics (how many secrets blocked per month)


**How to Answer**:

- **✅ Compliant**: Pre-commit hooks deployed to all repositories, secrets detection working, statistics tracked (e.g., 15 secrets blocked last month)
- **⚠️ Partial**: Hooks deployed to most repos (70-99%), or optional (can be bypassed)
- **❌ Non-Compliant**: No pre-commit hooks, or <70% coverage
- **🔄 Planned**: Pre-commit hook deployment in progress
- **N/A**: [Organization] has no secrets in code (justify - very unlikely)


**Examples**:

- ✅ **Compliant**: Gitleaks pre-commit hook deployed org-wide via template repository, 12 API keys blocked from commit last quarter, developer training on secret management provided
- ❌ **Non-Compliant**: No secret detection; AWS access key committed to public GitHub repo, discovered via external security researcher, credential rotation emergency


**Policy Reference**: ISMS-POL-A.8.28 Section 2.2.4 (Secret management - pre-commit hooks recommended)

---

## Domain 5: Tool Effectiveness & Metrics

**Assessment Question 5.1**: "Are security tool KPIs defined and tracked quarterly?"

**What This Asks**: Does [Organization] measure whether security tools are actually working?

**Where to Find Evidence**:

- KPI definition document (what metrics tracked)
- Quarterly security metrics reports
- Dashboard screenshots
- Trend analysis (are metrics improving over time?)


**How to Answer**:

- **✅ Compliant**: KPIs defined (false positive rate, MTTR, coverage, vulnerability trends), tracked quarterly, reported to management
- **⚠️ Partial**: Some KPIs tracked (e.g., finding counts) but not comprehensive, or tracked irregularly
- **❌ Non-Compliant**: No KPI tracking, or KPIs not reviewed
- **🔄 Planned**: KPI framework being developed
- **N/A**: Not applicable (justify - unlikely)


**Examples**:

- ✅ **Compliant**: Q4 2025 Security Metrics Report: SAST FP rate 14% (target <20% ✅), SCA MTTR 12 days (target <14d ✅), DAST coverage 95% (target >90% ✅), presented to CISO monthly
- ❌ **Non-Compliant**: Tools deployed for 2 years; no one knows if they're effective; no metrics tracked


**Policy Reference**: ISMS-POL-A.8.28 Section 3.3 (Assessment and verification - metrics required)

---

**Assessment Question 5.2**: "Is Mean Time to Remediation (MTTR) measured and improving over time?"

**What This Asks**: How quickly are security findings fixed, and is the organization getting faster?

**Where to Find Evidence**:

- MTTR calculation methodology (days from finding detection to fix deployment)
- MTTR statistics (last 4 quarters)
- Trend analysis chart
- Remediation SLA documentation


**How to Answer**:

- **✅ Compliant**: MTTR measured for all severity levels, tracked quarterly, trend showing improvement (or consistent performance within SLA)
- **⚠️ Partial**: MTTR measured but not consistently tracked, or no improvement over time
- **❌ Non-Compliant**: MTTR not measured, or consistently missing SLAs
- **🔄 Planned**: MTTR tracking being implemented
- **N/A**: No security findings (justify - very unlikely)


**Examples**:

- ✅ **Compliant**: Critical MTTR: Q1=18d, Q2=14d, Q3=10d, Q4=8d (improving); High MTTR: Q1=45d, Q2=38d, Q3=32d, Q4=28d (improving); SLAs: Critical <14d, High <30d (met in Q4)
- ❌ **Non-Compliant**: Critical findings sit unresolved for months; no tracking; discovered 187 unresolved Critical findings dating back 18 months


**Policy Reference**: ISMS-POL-A.8.28 Section 2.3.1 (Remediation SLAs required), ISMS-POL-A.8.28 Annex A (Vulnerability Response)

---

**Assessment Question 5.3**: "Is tool ROI measured (vulnerabilities prevented vs. cost)?"

**What This Asks**: Are security tools cost-effective, or just expensive overhead?

**Where to Find Evidence**:

- Tool cost documentation (licenses, support, training costs)
- Vulnerability prevention statistics (findings detected and fixed pre-production vs. post-production)
- ROI calculation (cost per vulnerability prevented, cost of production incident avoided)
- Cost-benefit analysis


**How to Answer**:

- **✅ Compliant**: ROI calculated annually, tools demonstrably cost-effective (vulnerabilities prevented > cost)
- **⚠️ Partial**: Costs tracked but ROI not formally calculated, or unclear cost-effectiveness
- **❌ Non-Compliant**: ROI not measured, or tools clearly not cost-effective (high cost, low impact)
- **🔄 Planned**: ROI framework being developed
- **N/A**: Not applicable (justify - uncommon)


**Examples**:

- ✅ **Compliant**: SAST cost: $50K/year, 487 vulnerabilities detected pre-production (prevented), estimated production incident cost: $150K each, ROI: 10x (even if only 1 incident prevented)
- ❌ **Non-Compliant**: $200K/year SAST license, 12 findings last year (all false positives or duplicates), 8 production security incidents (tool missed them), negative ROI


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.6 (Security planning and resource allocation - effectiveness measurement)

---

# Evidence Collection

## Evidence Types

**Tool Documentation**:

- Tool licenses (PDF contracts, license keys, expiration dates)
- Deployment architecture diagrams (where tools deployed, network access)
- Configuration files (ruleset configs, quality gate definitions)
- User guides and admin documentation


**Configuration Evidence**:

- CI/CD pipeline YAML files (GitHub Actions, GitLab CI, Jenkinsfile)
- Tool configuration exports (SonarQube quality profiles, Snyk policies)
- Pre-commit hook files (.pre-commit-config.yaml, git hooks)
- IDE plugin lists (org-wide plugin catalog)


**Metrics & Reports**:

- Tool dashboards (screenshots showing metrics)
- Finding statistics (CSV exports, PDF reports)
- Trend analysis charts (vulnerability trends over time)
- False positive analysis (FP rate calculations)


**Process Documentation**:

- Secure coding standards (PDF, wiki pages)
- Code review checklists
- Training materials
- Remediation SLA policies


## Where Evidence Typically Resides

| Evidence Type | Typical Location | Access Required |
|---------------|------------------|-----------------|
| **Tool Licenses** | Procurement system, contracts folder | Procurement admin OR finance |
| **Tool Dashboards** | SonarQube, Snyk, Checkmarx web UI | Tool admin OR read-only admin |
| **CI/CD Configs** | Repository root (.github/workflows/, .gitlab-ci.yml) | Repository read access |
| **Pre-commit Hooks** | Repository .git/hooks/ or .pre-commit-config.yaml | Repository read access |
| **Standards Docs** | Wiki (Confluence, SharePoint), document management | Developer access |
| **Metrics Reports** | Security team shared drive, dashboards | Security team access |
| **Training Records** | LMS (for standards training) | HR/Training admin |
| **Finding Statistics** | Tool reporting features, issue tracking (Jira) | Tool access + Jira access |

## How to Capture Evidence

**Tool Configuration Exports**:
```bash
# SonarQube quality profile export
curl -u admin:password "https://sonarqube.org/api/qualityprofiles/backup?qualityProfile=Sonar%20way" > sonarqube_profile.xml

# GitHub Actions workflow files
cp .github/workflows/security-scan.yml evidence/github_actions_sast.yml

# Pre-commit config
cp .pre-commit-config.yaml evidence/precommit_config.yaml
```

**Dashboard Screenshots**:

- Capture full context (include URL, date, page title)
- Highlight relevant sections (use annotation tools)
- Save with descriptive filename: `Evidence_2-1_SonarQube_Dashboard_20260124.png`


**Metrics Exports**:
```bash
# Export SonarQube metrics (example)
curl -u admin:password "https://sonarqube.org/api/measures/component?component=project_key&metricKeys=vulnerabilities,bugs,code_smells" > sonarqube_metrics.json

# Export Snyk vulnerability report
snyk test --json > snyk_vulnerabilities.json
```

**PDF Reports**:

- Export from tool dashboards (most tools have PDF export)
- Include report generation date, report parameters
- Save with descriptive filename


## Evidence Register Population

For each evidence item in the Evidence Register sheet:

**Evidence ID**: Auto-generated (EV-001, EV-002, etc.)

**Evidence Description**: Brief description of what this proves

- Example: "SonarQube quality gate configuration showing Critical/High findings block builds"


**Related Assessment Question**: Which question(s) this evidence supports

- Example: "2.2 SAST Quality Gates"


**Evidence Type**: Select from dropdown

- Configuration Export, Screenshot, Report, Metrics Data, Document, License, Other


**Location**: Where evidence is stored

- Example: "/Security/Evidence/ISMS-A.8.28.2/SonarQube_QualityGate_Config.pdf"
- Or: "SonarQube UI > Quality Gates > [Organization] Gate > Screenshot"


**Date Collected**: Date evidence was captured

- Format: DD.MM.YYYY


**Collected By**: Name of person who captured evidence

- Example: "A. Smith, Application Security Lead"


## Evidence Quality Standards

**Good Evidence**:

- Objective (configuration files, metrics, not opinions)
- Current (captured within assessment period, not 2 years old)
- Attributable (who configured, who approved)
- Verifiable (auditor can access and verify)
- Sufficient (proves the claim being made)


**Poor Evidence**:

- Verbal claims ("we use SonarQube") without documentation
- Screenshots without context (no date, no URL, cropped too tightly)
- Expired evidence (license from 2 years ago when current status requested)
- Cherry-picked evidence (one good scan report when asking for quarterly trend)


---

# Common Pitfalls

Learn from others' mistakes. Here are the 10 most common errors in Standards & Tools assessments:

## Mistake 1: Confusing Tool Deployment with Tool Effectiveness

**Problem**: Marking "SAST deployed" as ✅ Compliant without verifying configuration, integration, and actual usage.

**Example**: SonarQube installed on server 2 years ago, but no projects configured, no scans running, license expired. Assessor marks "SAST deployed" as Compliant.

**Solution**: For EVERY tool, verify:
1. License active and valid
2. Configured for [Organization]'s languages and frameworks
3. Integrated into CI/CD (automated scans)
4. Quality gates enforced (findings block deployment)
5. Findings tracked and remediated
6. Metrics showing effectiveness (findings detected, FP rate, MTTR)

Deployment without effectiveness = cargo cult security = ❌ Non-Compliant.

---

## Mistake 2: Not Measuring False Positive Rates

**Problem**: Assuming SAST/SCA tools are accurate without measuring false positive rate.

**Example**: Developers complain "SAST is useless, generates too many false alarms". Assessor marks tool as Compliant without investigating. Reality: 70% false positive rate; tool ignored by developers.

**Solution**: **Always** calculate false positive rate:
```
FP Rate = (Findings suppressed/closed as FP) / (Total findings) × 100
```
Target: <20%. If FP rate >40%, tool is ineffective (needs tuning or replacement).

---

## Mistake 3: Missing CI/CD Integration Evidence

**Problem**: Claiming "tools integrated into CI/CD" without pipeline configuration evidence.

**Example**: Assessor says "SAST runs in CI/CD" based on developer verbal confirmation. Reality: SAST installed on separate server, manual scans only, no pipeline integration.

**Solution**: Provide **concrete evidence**:

- Pipeline YAML file showing SAST step
- Build logs showing SAST execution
- Quality gate configuration blocking builds
- Screenshots of blocked PRs due to SAST findings


Verbal claims ≠ evidence.

---

## Mistake 4: Ignoring Developer Adoption Rates

**Problem**: Marking IDE plugins as Compliant because they're "available" without checking if developers actually use them.

**Example**: Security team publishes plugin catalog; assessor marks ✅ Compliant. Reality: 5% adoption rate; developers don't know plugins exist.

**Solution**: Measure adoption:

- Telemetry data (if available): "342 of 480 developers (71%) have SonarLint installed"
- Survey data: "Annual developer survey: 68% report using security IDE plugins"
- Interview Security Champions: "Most developers I talk to use the VS Code security plugin"


Target: >70% adoption. <40% adoption = ❌ Non-Compliant (tool not effective if not used).

---

## Mistake 5: Not Tracking Remediation

**Problem**: Tools detect findings, but no process to ensure findings get fixed.

**Example**: SonarQube reports 487 Critical findings; all still open after 6 months; no remediation tracking. Assessor marks SAST as Compliant because "tool is running".

**Solution**: Verify remediation process:

- Findings tracked in issue tracking system (Jira, Azure DevOps)
- Remediation SLAs defined (Critical <7d, High <30d)
- MTTR measured and reported
- Overdue findings escalated to management


Detection without remediation = ineffective security.

---

## Mistake 6: Overlooking License Expiration

**Problem**: Assessing tool as Compliant when license expired months ago.

**Example**: DAST tool license expired 4 months ago; scans failing; assessor unaware.

**Solution**: **Always verify license status**:

- Check license expiration dates (tool admin dashboard, procurement records)
- Verify support contract active (can you get help if tool breaks?)
- Check user limits (is team within licensed user count?)


Expired license = ❌ Non-Compliant (tool not available).

---

## Mistake 7: No Standards Enforcement Measurement

**Problem**: Secure coding standards exist but no measurement of developer compliance.

**Example**: Beautiful 50-page standards document; zero measurement of whether developers follow it. Could be 100% compliant or 0% compliant - assessor doesn't know.

**Solution**: Measure compliance via:

- SAST findings mapped to standards violations (e.g., "42 SQL injection findings = standard Section 3.2 not followed")
- Code review checklists referencing standards (e.g., "87% of code reviews reference standards checklist")
- Developer assessments (e.g., "Annual developer quiz: average score 82%")
- Security Champions feedback (e.g., "Champions report most developers follow standards")


Standards without enforcement measurement = ⚠️ Partial at best.

---

## Mistake 8: Cherry-Picking Evidence

**Problem**: Providing evidence for best-performing project, claiming organization-wide compliance.

**Example**: "Project A" has 98% SAST coverage, all findings remediated within SLA. Assessor marks SAST as ✅ Compliant org-wide. Reality: Project A is pilot; 80% of projects have no SAST.

**Solution**: Calculate **coverage percentages**:

- % of repositories with SAST enabled
- % of production deployments with DAST scans
- % of developers using IDE plugins


Assess organization-wide reality, not showcase projects.

---

## Mistake 9: Forgetting Container & IaC Scanning

**Problem**: Focusing on application code scanning (SAST, SCA) while forgetting infrastructure.

**Example**: All application code scanned; Kubernetes deployments with vulnerable base images and insecure configurations go undetected.

**Solution**: If [Organization] uses containers or IaC:

- Container image scanning (Trivy, Snyk Container, ECR scanning)
- IaC scanning (Checkov, tfsec, Terrascan for Terraform/CloudFormation)
- Kubernetes security scanning (kubesec, kube-bench)


Infrastructure is code too - scan it.

---

## Mistake 10: No Continuous Improvement

**Problem**: Tools deployed, metrics tracked, but no action taken to improve.

**Example**: False positive rate 35% for 2 years; MTTR consistently missing SLAs; no tuning efforts, no tool changes.

**Solution**: Demonstrate continuous improvement:

- Quarterly tool effectiveness reviews
- Tuning actions documented (ruleset adjustments, FP reduction efforts)
- Trend showing improvement (FP rate decreasing, MTTR decreasing)
- Tool changes when tools underperform (switch vendors if needed)


Static metrics = stagnant security posture.

---

# Quality Checklist

Before submitting the assessment for approval, verify:

## Assessment Completion

**General**:

- [ ] All yellow cells completed (no blank cells in assessment sheets)
- [ ] Status selected from dropdown for every question (no manual text entry)
- [ ] Comments provided for all N/A, Partial, and Non-Compliant items
- [ ] Evidence ID referenced for Compliant and Partial items
- [ ] No placeholder text ([TBD], [Date], TODO) remaining


**Domain 1: Coding Standards**:

- [ ] Standards document located and reviewed
- [ ] OWASP Top 10 coverage verified
- [ ] CWE Top 25 coverage verified
- [ ] Language-specific guidelines verified for primary languages
- [ ] Training records reviewed
- [ ] Standards adoption measurement documented


**Domain 2: SAST & SCA Tools**:

- [ ] SAST tool identified (name, vendor, version)
- [ ] SAST license status verified (expiration date)
- [ ] CI/CD integration verified (pipeline configs provided)
- [ ] Quality gate configuration verified
- [ ] False positive rate calculated
- [ ] SCA tool identified and verified
- [ ] CVE detection working (sample reports provided)


**Domain 3: DAST & Testing Tools**:

- [ ] DAST tool identified (if applicable)
- [ ] Pre-release scanning verified
- [ ] Container scanning verified (if using containers)
- [ ] IaC scanning verified (if using IaC)
- [ ] API testing verified (if applicable)


**Domain 4: IDE Plugins & Linters**:

- [ ] IDE plugins documented (which plugins, which IDEs)
- [ ] Adoption rate calculated (target: >70%)
- [ ] Pre-commit hooks verified (secret detection working)
- [ ] Developer feedback collected


**Domain 5: Tool Effectiveness**:

- [ ] KPIs defined and documented
- [ ] False positive rates calculated for all tools
- [ ] MTTR calculated and trended
- [ ] Coverage metrics calculated
- [ ] ROI assessed (at least qualitatively)


## Tool Inventory

- [ ] All deployed security tools listed
- [ ] Tool vendor, version, license expiration documented
- [ ] Tool status (Active, Pilot, Deprecated, Planned) marked
- [ ] Evidence linked for each tool


## Evidence Register

- [ ] All evidence items have descriptions
- [ ] All evidence items have locations (file path or URL)
- [ ] All evidence items have collection dates
- [ ] All evidence items have collector names
- [ ] Evidence physically exists at documented locations
- [ ] Evidence is accessible to auditors


## Gap Analysis

- [ ] All ❌ Non-Compliant items appear
- [ ] All ⚠️ Partial items appear
- [ ] Gap descriptions clear and specific
- [ ] Remediation owners assigned (name, not role)
- [ ] Remediation target dates realistic
- [ ] Priority assigned (Critical/High/Medium/Low)


## Summary Dashboard

- [ ] Overall compliance percentage calculated correctly
- [ ] Domain compliance percentages calculated correctly
- [ ] Formulas not broken (no #REF!, #VALUE! errors)
- [ ] Top gaps list populated
- [ ] Critical gaps count accurate


## Approval Sign-Off

- [ ] Completed By section filled (name, role, date, signature)
- [ ] Reviewed By sections prepared
- [ ] Next Review Date calculated (+3 months)


## File Quality

- [ ] Filename follows convention: `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`
- [ ] File saved to shared location
- [ ] File permissions set (reviewers have access)
- [ ] Evidence files uploaded to evidence repository


---

# Review & Approval

## Internal Review (Before Submission)

**Self-Review**:
1. Complete Quality Checklist (Section 7)
2. Review Summary Dashboard - do metrics make sense?
3. Spot-check evidence links - do they work?
4. Verify false positive rates calculated correctly

**Peer Review** (Optional but Recommended):
1. Share with Security Architect or DevOps lead
2. Request 30-minute review meeting
3. Validate tool configurations and metrics
4. Incorporate feedback

**Stakeholder Validation**:
1. Share Tool Inventory with Tool Administrators - accuracy check
2. Share metrics with Development Managers - do adoption rates match their observations?
3. Share with Security Champions - does effectiveness assessment match their experience?
4. Incorporate feedback

## Formal Approval Workflow

**Step 1: Submit to Application Security Lead**

**When**: After internal review complete  
**Timeline**: 5 business days  

**Application Security Lead Reviews**:

- Tool configuration accuracy
- Metrics accuracy
- Effectiveness assessment realistic
- Gap remediation plans feasible


**Possible Outcomes**:

- Approve
- Approve with Minor Revisions
- Return for Revision


---

**Step 2: Submit to DevOps/Platform Engineering Lead**

**When**: After Application Security Lead approval  
**Timeline**: 5 business days  

**DevOps Reviews**:

- CI/CD integration accuracy
- Pipeline configuration correctness
- Operational feasibility


---

**Step 3: Submit to CISO**

**When**: After Application Security Lead AND DevOps approval  
**Timeline**: 5 business days  

**CISO Reviews**:

- Risk posture
- Tool investment ROI
- Strategic alignment
- Budget implications (tool renewals, new tools)


**Possible Outcomes**:

- Approve
- Approve with Conditions
- Reject


## Post-Approval Actions

**Publication**:
1. Save approved workbook to ISMS document repository
2. Update ISMS assessment register
3. Publish executive summary

**Communication**:
1. Email summary to Development Managers
2. Present to Security Champions
3. Add to CISO monthly report

**Remediation Tracking**:
1. Create tickets for gaps
2. Assign owners and due dates
3. Track to closure

**Schedule Next Assessment**:
1. Calendar reminder (+3 months)
2. Assign owner for next cycle

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

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

<!-- QA_VERIFIED: 2026-01-31 -->
