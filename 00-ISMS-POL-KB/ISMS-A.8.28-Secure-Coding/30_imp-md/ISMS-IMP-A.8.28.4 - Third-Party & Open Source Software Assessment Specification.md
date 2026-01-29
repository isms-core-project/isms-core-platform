# ISMS-IMP-A.8.28.4
## Secure Coding - Third-Party & Open Source Software Assessment Specification

**Document ID**: ISMS-IMP-A.8.28.4  
**Title**: Third-Party & Open Source Software Assessment  
**Version**: 1.0  
**Date**: 07.01.2025  
**Classification**: Internal  
**Owner**: Application Security Lead  
**Status**: Draft  

---

## Document Control

| Version | Date       | Author                    | Changes                          |
|---------|------------|---------------------------|----------------------------------|
| 1.0     | 07.01.2025 | Application Security Lead | Initial specification            |

**Review Cycle**: Annually or upon significant changes to supply chain security requirements

**Approvers**:
- Application Security Lead (Technical Review)
- Chief Information Security Officer (Final Approval)
- Legal Counsel (License Compliance Review)

**Related Documents**:
- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-POL-A.8.28-S2.4 - Third-Party & Open Source Software Management
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment

---

## 1. Assessment Overview

### 1.1 Purpose

This assessment evaluates the organization's management of **third-party dependencies, open source software (OSS), vendor-provided components, and external code integrations**. 

The assessment addresses supply chain security risks that have led to major breaches (SolarWinds, Log4Shell, Codecov) by verifying:
- Vendor security due diligence processes
- OSS inventory and license compliance
- Dependency vulnerability management
- Third-party code security reviews
- Legal risk mitigation for licenses

**Core Philosophy**: As Feynman reminded us, "The first principle is that you must not fool yourself—and you are the easiest person to fool." Having an OSS policy doesn't mean you're managing OSS securely. This assessment focuses on **actual practices** over **documented intentions**.

### 1.2 Scope

**In Scope**:
- Commercial vendor software and services
- Open source libraries and frameworks (direct dependencies)
- Transitive dependencies (dependencies of dependencies)
- Third-party SDKs, APIs, and integrations
- Package managers (npm, pip, Maven, NuGet, etc.)
- Container base images and third-party containers
- License compliance and legal risk
- Supply chain security controls

**Out of Scope**:
- Infrastructure vendor assessments (covered under different control)
- Cloud service provider assessments (separate framework)
- Hardware vendor assessments
- Generic procurement processes unrelated to software security

### 1.3 Assessment Audience

**Primary Stakeholders**:
- **Application Security Team**: Primary assessment coordinators
- **Engineering Managers**: Responsible for team compliance
- **Software Architects**: Design-level dependency decisions
- **Legal/Compliance Team**: License compliance oversight
- **Procurement Team**: Vendor contract security requirements

**Supporting Stakeholders**:
- Development teams (evidence providers)
- Security Champions (departmental coordination)
- DevOps teams (build pipeline integration)
- Third-party vendors (questionnaire responses)

### 1.4 Assessment Frequency

**Initial Assessment**: During policy implementation (Year 1)

**Recurring Assessments**:
- **Quarterly**: High-risk vendor reviews, critical dependency updates
- **Annually**: Comprehensive assessment across all domains
- **Event-Driven**: Following major supply chain incidents (e.g., Log4Shell-level events)

**Continuous Monitoring**:
- Automated SCA scans (daily/per-commit)
- Vendor security alerts (real-time)
- License compliance scans (per-build)

### 1.5 Assessment Output

**Deliverables**:
1. **Completed Assessment Workbook**: Excel file with all domains assessed
2. **Vendor Risk Registry**: Updated inventory of third-party software vendors
3. **OSS Inventory**: Complete list of open source dependencies with licenses
4. **Gap Analysis Report**: Prioritized remediation roadmap
5. **Executive Summary**: High-level findings for CISO review

**Metrics Tracked**:
- Vendor security posture score (% compliant vendors)
- OSS inventory completeness (% tracked dependencies)
- Vulnerability remediation time (mean time to patch dependencies)
- License compliance rate (% compliant licenses)
- Supply chain security controls coverage

---

## 2. Assessment Domains

### 2.1 Domain 1: Vendor Security Assessment

**Purpose**: Evaluate security due diligence for commercial software vendors and service providers.

**Focus Areas**:
- Vendor security questionnaire process
- Contract security requirements (SLAs, incident response, data protection)
- Vendor access controls and segregation
- Regular vendor security reviews
- Vendor risk classification and tiering
- Vendor incident response coordination

**Key Questions**:
- Do we know which vendors have access to our code/data?
- Are vendors assessed before integration?
- Do contracts include security requirements?
- Are high-risk vendors reviewed regularly?

**Common Anti-Patterns**:
- ❌ Vendor onboarding without security review
- ❌ Contracts without security clauses
- ❌ No vendor risk classification
- ❌ Vendor access without monitoring

**Evidence Required**:
- Vendor security questionnaires (completed)
- Vendor contracts with security terms
- Vendor review meeting notes/reports
- Vendor access control configurations

### 2.2 Domain 2: Open Source Software Management

**Purpose**: Assess OSS approval, tracking, and governance processes.

**Focus Areas**:
- OSS approval workflow (request, review, approve)
- OSS inventory maintenance (Bill of Materials)
- License identification and tracking
- Abandoned/unmaintained OSS detection
- OSS update policies and procedures
- OSS contribution guidelines (if applicable)

**Key Questions**:
- Do we maintain an accurate OSS inventory?
- Is there an approval process before using new OSS?
- Are licenses identified and tracked?
- Do we detect abandoned dependencies?

**Common Anti-Patterns**:
- ❌ "npm install" without review (JavaScript dependency hell)
- ❌ No Software Bill of Materials (SBOM)
- ❌ Stale dependencies (packages not updated in years)
- ❌ Transitive dependencies ignored (dependency of a dependency)
- ❌ Copy-paste from StackOverflow without license check

**Evidence Required**:
- OSS approval records (tickets, forms)
- SBOM exports (CycloneDX, SPDX format)
- OSS policy documentation
- Abandoned dependency reports

### 2.3 Domain 3: Dependency Vulnerability Management

**Purpose**: Evaluate vulnerability detection and remediation for third-party dependencies.

**Focus Areas**:
- SCA tool integration (Software Composition Analysis)
- Vulnerability alerting and notification
- Remediation SLAs for dependency vulnerabilities
- Dependency update policies (patch management)
- Vulnerability triage process (risk assessment)
- Transitive dependency management
- Dependency pinning and lockfile usage

**Key Questions**:
- Are dependencies scanned for known vulnerabilities?
- Is there a defined SLA for patching critical vulnerabilities?
- Are transitive dependencies monitored?
- Are lockfiles used to ensure reproducible builds?

**Common Anti-Patterns**:
- ❌ Ignoring SCA tool alerts ("we'll fix it later")
- ❌ No SLA for patching dependencies (Log4Shell scenarios)
- ❌ Unpinned dependency versions (`package: "^1.0.0"` wildcards)
- ❌ Transitive vulnerabilities ignored
- ❌ False positive fatigue (crying wolf)

**Evidence Required**:
- SCA scan reports (Snyk, Dependabot, WhiteSource)
- Vulnerability triage records
- Remediation tracking (JIRA tickets, patching logs)
- Lockfile examples (package-lock.json, Pipfile.lock)

### 2.4 Domain 4: Third-Party Code Review & Integration

**Purpose**: Assess security review requirements for integrating third-party code and services.

**Focus Areas**:
- Code review requirements for vendor-provided code
- Integration security review process
- Third-party API security assessment
- SDK/library security evaluation
- Code escrow agreements (if applicable)
- Third-party code isolation and sandboxing
- Supply chain attack mitigations (e.g., package signing verification)

**Key Questions**:
- Are third-party integrations security reviewed?
- Are third-party APIs assessed for security risks?
- Is vendor code isolated from critical systems?
- Are packages verified before installation (checksums, signatures)?

**Common Anti-Patterns**:
- ❌ Vendor code deployed without review (blind trust)
- ❌ API integrations without security assessment
- ❌ No verification of package integrity (typosquatting risk)
- ❌ Third-party code with elevated privileges
- ❌ Cargo cult: "It's from a big company, must be secure"

**Evidence Required**:
- Third-party integration review reports
- API security assessment checklists
- Package verification configurations (GPG signatures, checksums)
- Isolation architecture diagrams

### 2.5 Domain 5: License Compliance & Legal Risk

**Purpose**: Evaluate license identification, compliance tracking, and legal risk mitigation.

**Focus Areas**:
- License identification and categorization
- License compatibility assessment (GPL + proprietary conflicts)
- Copyleft/viral license management (GPL, AGPL)
- License violation detection and remediation
- Legal review process for OSS usage
- Open source attribution (LICENSE files, notices)
- License audit trails

**Key Questions**:
- Are all dependency licenses identified?
- Are incompatible licenses detected (GPL + proprietary)?
- Is there a legal review process for restrictive licenses?
- Are license attributions maintained (NOTICE files)?

**Common Anti-Patterns**:
- ❌ License compliance as afterthought ("legal will figure it out")
- ❌ GPL contamination (mixing GPL code with proprietary)
- ❌ Missing attribution files (license violations)
- ❌ No legal review for AGPL/restrictive licenses
- ❌ Cargo cult: "It's open source, we can do anything with it"

**Evidence Required**:
- License scan reports (FOSSA, Black Duck)
- Legal review records for restrictive licenses
- Attribution files (LICENSE, NOTICE, THIRD_PARTY_LICENSES)
- License compatibility matrix

---

## 3. Assessment Sheet Specifications

### 3.1 Sheet 1: Instructions

**Purpose**: Provide assessment guidance and focus stakeholders on evidence-based evaluation.

**Content**:
- Assessment overview and philosophy
- How to complete each domain
- Evidence requirements and examples
- Common pitfalls and anti-patterns
- **Feynman Reminder**: "Focus on what works, not what's documented"
- **Anti-Cargo-Cult**: Having a vendor questionnaire ≠ vendor is secure
- Scoring guidance and success criteria

**Format**:
- Welcome section with assessment context
- Domain-specific instructions (5 sections)
- Evidence collection tips
- Resources and contacts

### 3.2 Sheet 2: Vendor_Security_Assessment

**Domain**: Vendor Security Assessment (18 requirements)

| ID   | Requirement | Evidence Examples |
|------|-------------|-------------------|
| V-01 | Vendor security assessment policy exists and is approved | Policy document, approval signatures |
| V-02 | Security questionnaire sent to all vendors before onboarding | Questionnaire templates, completed questionnaires |
| V-03 | Vendor risk classification framework implemented (High/Medium/Low) | Risk classification matrix, vendor tier lists |
| V-04 | Contract security requirements defined for all vendors | Contract templates with security clauses |
| V-05 | Data protection requirements specified in vendor contracts | Contract sections on data handling, DPAs |
| V-06 | Incident response coordination requirements in contracts | Incident notification SLAs, contact procedures |
| V-07 | Vendor access controls documented and enforced | Access logs, permission matrices, SSO configs |
| V-08 | Vendor accounts use least privilege principle | Access reviews, role definitions |
| V-09 | Vendor access is reviewed regularly (quarterly for high-risk) | Access review reports, approval records |
| V-10 | High-risk vendors undergo annual security reviews | Review meeting notes, assessment reports |
| V-11 | Vendor security incidents are tracked and reviewed | Incident logs, lessons learned documents |
| V-12 | Vendor security posture is monitored (security ratings, breaches) | Security rating subscriptions, monitoring reports |
| V-13 | Vendor SOC 2 / ISO 27001 compliance verified where applicable | SOC 2 reports, ISO certificates |
| V-14 | Vendor data retention and deletion requirements specified | Contract data handling clauses, deletion procedures |
| V-15 | Vendor security questionnaire responses validated (not just accepted) | Validation notes, follow-up correspondence |
| V-16 | Vendor offboarding process includes security checklist | Offboarding checklists, access revocation logs |
| V-17 | Critical vendors have business continuity plans reviewed | BCP documents, disaster recovery plans |
| V-18 | Vendor security metrics tracked (% compliant vendors, review completion) | Vendor compliance dashboard, metrics reports |

### 3.3 Sheet 3: OSS_Management

**Domain**: Open Source Software Management (18 requirements)

| ID   | Requirement | Evidence Examples |
|------|-------------|-------------------|
| O-01 | OSS usage policy exists and is approved | OSS policy document, approval signatures |
| O-02 | OSS approval workflow defined (request → review → approve) | Workflow documentation, JIRA workflows |
| O-03 | OSS approval process enforced before production use | Approval tickets, process audit logs |
| O-04 | OSS inventory maintained (SBOM) for all applications | SBOM exports (CycloneDX, SPDX), inventory databases |
| O-05 | SBOM generated automatically in CI/CD pipeline | CI/CD configs, build logs showing SBOM generation |
| O-06 | OSS components tracked with version numbers | Dependency manifests (package.json, requirements.txt) |
| O-07 | Transitive dependencies identified and tracked | Dependency tree reports, SCA tool outputs |
| O-08 | OSS license information captured in inventory | License scan reports, SBOM license fields |
| O-09 | Abandoned/unmaintained OSS detected and tracked | Dependency staleness reports, EOL tracking |
| O-10 | OSS update policy defines acceptable staleness (e.g., <6 months) | Policy document, staleness thresholds |
| O-11 | OSS components reviewed for security before approval | Security review checklists, approval criteria |
| O-12 | Restricted licenses flagged during approval (GPL, AGPL) | License allowlist/blocklist, flagging rules |
| O-13 | OSS alternatives evaluated before approval (build vs. buy) | Evaluation notes, decision records |
| O-14 | OSS contribution guidelines exist (if organization contributes) | Contribution policy, CLA templates |
| O-15 | OSS forks are minimized and justified | Fork justifications, upstream contribution plans |
| O-16 | OSS components with known high-risk maintainers flagged | Maintainer reputation checks, risk assessments |
| O-17 | OSS inventory reviewed regularly (quarterly minimum) | Inventory review reports, approval records |
| O-18 | OSS metrics tracked (% approved, inventory coverage) | OSS dashboard, compliance metrics |

### 3.4 Sheet 4: Dependency_Vulnerability_Mgmt

**Domain**: Dependency Vulnerability Management (18 requirements)

| ID   | Requirement | Evidence Examples |
|------|-------------|-------------------|
| D-01 | SCA tool deployed and scanning dependencies | SCA tool configs (Snyk, Dependabot, WhiteSource) |
| D-02 | SCA scans run automatically on every build/commit | CI/CD pipeline configs, scan logs |
| D-03 | SCA tool integrated with developer workflow (IDE plugins, PR checks) | IDE plugin configs, PR check results |
| D-04 | Vulnerability alerts delivered to responsible teams | Alert routing configs, notification logs |
| D-05 | Vulnerability remediation SLAs defined by severity | SLA policy, severity definitions |
| D-06 | Critical vulnerabilities have <7 day remediation SLA | SLA policy, tracking metrics |
| D-07 | High vulnerabilities have <30 day remediation SLA | SLA policy, tracking metrics |
| D-08 | Vulnerability triage process documented | Triage workflow, decision criteria |
| D-09 | False positives documented with suppression justification | Suppression records, justification notes |
| D-10 | Dependency update process documented | Update procedures, testing requirements |
| D-11 | Dependency updates tested before production deployment | Test results, staging environment logs |
| D-12 | Transitive dependency vulnerabilities addressed | Transitive vulnerability remediation records |
| D-13 | Dependency pinning used (lockfiles required) | Lockfile examples, policy enforcement |
| D-14 | Dependency version ranges minimized (avoid wildcards like "^1.0.0") | Dependency manifests, policy enforcement |
| D-15 | Emergency patching process for critical vulnerabilities (e.g., Log4Shell) | Emergency response plans, drill records |
| D-16 | Vulnerability remediation tracked with metrics | Remediation dashboards, MTTR metrics |
| D-17 | Unpatched vulnerabilities require risk acceptance | Risk acceptance forms, approval signatures |
| D-18 | SCA tool effectiveness reviewed regularly (false negative testing) | Tool effectiveness reports, benchmark tests |

### 3.5 Sheet 5: Third_Party_Code_Review

**Domain**: Third-Party Code Review & Integration (18 requirements)

| ID   | Requirement | Evidence Examples |
|------|-------------|-------------------|
| T-01 | Third-party code integration policy exists | Integration policy document, approval records |
| T-02 | Security review required for all third-party integrations | Review checklist, approval workflow |
| T-03 | Third-party APIs assessed for security risks | API security assessments, risk ratings |
| T-04 | API authentication mechanisms reviewed (OAuth, API keys) | Authentication config reviews, security notes |
| T-05 | API authorization controls verified (least privilege) | Authorization testing results, access reviews |
| T-06 | Third-party API rate limiting and abuse prevention assessed | Rate limiting configs, abuse detection logs |
| T-07 | SDK/library source code reviewed where feasible | Code review reports, static analysis results |
| T-08 | Third-party container images scanned for vulnerabilities | Container scan reports (Trivy, Clair) |
| T-09 | Container base images from trusted sources only | Image provenance records, registry configs |
| T-10 | Package integrity verified before installation (checksums, signatures) | Package verification configs (GPG, SHA256) |
| T-11 | Package manager security features enabled (e.g., npm audit, pip audit) | Package manager configs, audit logs |
| T-12 | Typosquatting protection implemented (package name validation) | Package allowlists, validation rules |
| T-13 | Third-party code isolated from critical systems (sandboxing) | Architecture diagrams, isolation configs |
| T-14 | Vendor-provided code deployed with least privilege | Permission configs, role definitions |
| T-15 | Code escrow agreements in place for critical vendors (optional) | Escrow agreements, documentation |
| T-16 | Third-party integration monitoring in place | Integration logs, monitoring dashboards |
| T-17 | Supply chain attack mitigations documented | Mitigation strategies, security controls |
| T-18 | Third-party integration security reviewed regularly (annual) | Integration review reports, approval records |

### 3.6 Sheet 6: License_Compliance

**Domain**: License Compliance & Legal Risk (18 requirements)

| ID   | Requirement | Evidence Examples |
|------|-------------|-------------------|
| L-01 | License compliance policy exists and is approved | Policy document, legal approval records |
| L-02 | License scanning tool deployed (FOSSA, Black Duck, etc.) | License scan tool configs |
| L-03 | License scans run automatically on every build | CI/CD configs, scan logs |
| L-04 | All dependency licenses identified and tracked | License scan reports, SBOM license data |
| L-05 | License allowlist and blocklist defined | Allowlist/blocklist documents, approval criteria |
| L-06 | Copyleft licenses flagged for legal review (GPL, AGPL, MPL) | Flagging rules, legal review records |
| L-07 | License compatibility assessed (GPL + proprietary conflicts) | Compatibility matrix, conflict reports |
| L-08 | Viral license contamination prevented (GPL/AGPL isolation) | Isolation strategies, architecture reviews |
| L-09 | Commercial licenses tracked with usage limits | License tracking, usage reports |
| L-10 | License violation detection automated | Violation detection rules, alert configs |
| L-11 | License violations remediated with documented plan | Remediation plans, resolution records |
| L-12 | Legal review required for restrictive licenses (AGPL, SSPL) | Legal review requests, approval records |
| L-13 | Open source attribution maintained (LICENSE, NOTICE files) | Attribution files, automated generation |
| L-14 | Third-party license notices included in distributions | Distribution packages, license bundling |
| L-15 | License compliance verified before production release | Release checklists, compliance sign-offs |
| L-16 | License audit trails maintained | Audit logs, compliance history |
| L-17 | License compliance training provided to developers | Training records, completion certificates |
| L-18 | License compliance metrics tracked (% compliant, violations) | Compliance dashboards, metrics reports |

### 3.7 Sheet 7: Summary_Dashboard

**Purpose**: Aggregate compliance metrics across all domains.

**Layout**:
```
Row 1-3: Title and metadata
Row 5: Assessment Summary
Row 7-11: Domain Compliance Table
    - Domain Name
    - Total Requirements (18 per domain)
    - Implemented Count
    - Partially Implemented Count
    - Not Implemented Count
    - N/A Count
    - Compliance % (formula)
    - Status (Traffic Light: Green/Yellow/Red)

Row 13-17: Overall Statistics
    - Total Requirements: 90
    - Overall Compliance %
    - Critical Gaps Count
    - High Priority Gaps Count
    - Evidence Completeness %

Row 19-25: Risk Summary
    - Vendor Security Risks
    - OSS Management Risks
    - Dependency Vulnerability Risks
    - Third-Party Integration Risks
    - License Compliance Risks

Row 27+: Executive Recommendations
```

**Formulas**:
- Compliance % = (Implemented + Partially Implemented*0.5) / (Total - N/A) * 100
- Status = IF(Compliance% >= 80, "Green", IF(Compliance% >= 50, "Yellow", "Red"))

### 3.8 Sheet 8: Evidence_Register

**Purpose**: Centralized evidence tracking for all requirements.

**Columns**:
- Requirement ID (V-01, O-01, etc.)
- Requirement Description
- Evidence Type (Document, Screenshot, Report, Configuration, URL, Recording, Other)
- Evidence Location (File path, URL, SharePoint location)
- Evidence Date (DD.MM.YYYY)
- Evidence Owner (Contact name)
- Verification Status (Pending, Verified, Rejected)
- Verifier Name
- Verification Date (DD.MM.YYYY)
- Notes

**Purpose**: Ensures audit trail and evidence traceability.

### 3.9 Sheet 9: Gap_Analysis

**Purpose**: Track identified gaps and remediation plans.

**Columns**:
- Gap ID (Auto-increment: GAP-001, GAP-002...)
- Domain (Dropdown: Vendor Security, OSS Management, etc.)
- Requirement ID (V-01, O-01, etc.)
- Gap Description (Text)
- Current State (Text)
- Target State (Text)
- Risk Level (Critical, High, Medium, Low)
- Remediation Plan (Text)
- Owner (Text - responsible person)
- Target Date (DD.MM.YYYY)
- Status (Open, In Progress, Resolved, Closed, Deferred)
- Actual Closure Date (DD.MM.YYYY)
- Notes

**Conditional Formatting**: Overdue items highlighted in red.

### 3.10 Sheet 10: Approval_Sign_Off

**Purpose**: Formal approval and acceptance of assessment results.

**Content**:
- Assessment Metadata (Date, Assessor, Scope)
- Assessment Summary (Compliance %, Key Findings)
- Approval Roles Table:
  - Application Security Lead (Technical Review)
  - Chief Information Security Officer (CISO Approval)
  - Legal Counsel (License Compliance Approval)
  - Procurement Lead (Vendor Management Approval)
- Each role has:
  - Name field
  - Signature field (manual or digital)
  - Date field (DD.MM.YYYY)
  - Decision (Approved, Approved with Conditions, Rejected, Pending Review)
  - Comments field

---

## 4. Assessment Methodology

### 4.1 Pre-Assessment Preparation

**1. Identify Assessment Scope**:
- Determine which applications/projects to assess
- Identify vendor contracts in scope
- Pull OSS inventory (SBOM) from repositories
- Access SCA tool reports
- Gather license scan reports

**2. Assemble Assessment Team**:
- Application Security Lead (coordinator)
- Development representatives (evidence providers)
- Legal counsel (license compliance expert)
- Procurement representative (vendor contracts)

**3. Prepare Evidence Collection**:
- Review evidence requirements for each domain
- Set up evidence storage locations (SharePoint, wiki)
- Schedule interviews with stakeholders
- Request access to tools and systems

### 4.2 Assessment Execution

**Phase 1: Vendor Security Assessment (Domain 1)**
1. Review vendor contracts for security requirements
2. Collect vendor security questionnaires
3. Verify vendor access controls
4. Review vendor security ratings (if available)
5. Interview procurement and security teams
6. Document findings in Vendor_Security_Assessment sheet

**Phase 2: OSS Management Assessment (Domain 2)**
1. Export SBOM from repositories
2. Review OSS approval workflow (JIRA, ServiceNow)
3. Analyze OSS policy compliance
4. Check for abandoned dependencies
5. Interview development teams about OSS practices
6. Document findings in OSS_Management sheet

**Phase 3: Dependency Vulnerability Management (Domain 3)**
1. Review SCA tool configurations
2. Analyze vulnerability remediation metrics (MTTR)
3. Check for SLA compliance
4. Review vulnerability triage process
5. Examine lockfile usage across projects
6. Document findings in Dependency_Vulnerability_Mgmt sheet

**Phase 4: Third-Party Code Review & Integration (Domain 4)**
1. Review third-party integration architecture
2. Assess API security controls
3. Verify package integrity checks
4. Review container image scanning
5. Check isolation and sandboxing
6. Document findings in Third_Party_Code_Review sheet

**Phase 5: License Compliance (Domain 5)**
1. Review license scan reports
2. Identify license conflicts (GPL + proprietary)
3. Verify attribution files (LICENSE, NOTICE)
4. Check legal review records for restrictive licenses
5. Interview legal team on compliance processes
6. Document findings in License_Compliance sheet

**Phase 6: Evidence Collection & Validation**
1. Populate Evidence_Register with all evidence
2. Verify evidence authenticity and completeness
3. Request missing evidence from stakeholders
4. Mark evidence verification status

**Phase 7: Gap Analysis & Reporting**
1. Identify gaps (Not Implemented, Partially Implemented)
2. Populate Gap_Analysis sheet with remediation plans
3. Assign owners and target dates
4. Prioritize gaps by risk level
5. Generate Summary_Dashboard metrics

**Phase 8: Approval & Sign-Off**
1. Review findings with Application Security Lead
2. Present to CISO and stakeholders
3. Obtain Legal Counsel approval on license compliance
4. Complete Approval_Sign_Off sheet
5. Archive assessment workbook

### 4.3 Supply Chain Security Evaluation

**Focus on Real-World Attack Vectors**:

**1. Dependency Confusion Attacks**:
- Verify internal package registries configured correctly
- Check for namespace squatting protection
- Review package source priority (internal before public)

**2. Typosquatting Protection**:
- Check for package name validation
- Review allowlists for critical dependencies
- Verify package manager security settings

**3. Compromised Package Attacks (e.g., event-stream, ua-parser-js)**:
- Review SCA tool malware detection capabilities
- Check for behavioral analysis of dependencies
- Verify package integrity verification (signatures, checksums)

**4. Supply Chain Compromise (e.g., SolarWinds)**:
- Assess vendor security posture
- Review vendor access controls
- Verify vendor code escrow (if applicable)

**5. Abandoned Dependency Risk**:
- Identify dependencies not updated in >12 months
- Assess maintainer activity levels
- Plan migrations for abandoned libraries

### 4.4 Common Anti-Patterns to Avoid

**❌ Cargo Cult Anti-Patterns**:

1. **"We have a vendor questionnaire"** ≠ Vendors are secure
   - Reality check: Do you validate questionnaire answers?
   - Are questionnaires tailored to vendor risk level?
   - Follow-up questions asked?

2. **"We scan for vulnerabilities"** ≠ Vulnerabilities are fixed
   - Reality check: What's your mean time to remediate?
   - Are SLAs actually met?
   - Are false positives just ignored en masse?

3. **"We track licenses"** ≠ License compliance
   - Reality check: Do you remediate violations?
   - Is legal involved in restrictive license decisions?
   - Are attribution files actually maintained?

4. **"We have an OSS policy"** ≠ OSS is managed
   - Reality check: Is the approval process enforced?
   - Do teams bypass it?
   - Is the SBOM accurate and complete?

5. **"We use package signing"** ≠ Supply chain is secure
   - Reality check: Do you actually verify signatures?
   - Are unverified packages blocked?
   - Is the verification process automated?

**Feynman's Wisdom**: "What I cannot create, I do not understand."
- If you can't demonstrate the process working, you don't have the process.
- If you can't show vulnerability remediation metrics, you're not managing vulnerabilities.
- If you can't produce an accurate SBOM, you don't know what you're running.

---

## 5. Success Criteria

**Minimum Acceptable Compliance**:
- **Overall Compliance**: ≥ 70% across all domains
- **Domain-Specific Minimums**:
  - Vendor Security Assessment: ≥ 65% (contracts take time)
  - OSS Management: ≥ 75% (foundational requirement)
  - Dependency Vulnerability Mgmt: ≥ 80% (critical for security)
  - Third-Party Code Review: ≥ 65% (depends on integration complexity)
  - License Compliance: ≥ 70% (legal requirement)

**Target Maturity**:
- **Year 1 (Initial Implementation)**: 70-75% overall compliance
- **Year 2 (Optimization)**: 80-85% overall compliance
- **Year 3+ (Mature State)**: 90%+ overall compliance

**Critical Requirements** (Must be "Implemented" regardless of overall score):
- O-04: OSS inventory maintained (SBOM)
- D-02: SCA scans run automatically
- D-06: Critical vulnerabilities <7 day SLA
- L-04: All dependency licenses identified
- L-07: License compatibility assessed

**Red Flags** (Immediate escalation to CISO):
- No OSS inventory (SBOM) exists
- No SCA tool deployed
- Critical vulnerabilities >30 days unpatched
- GPL contamination (GPL + proprietary code)
- Vendor breach involving company data

---

## 6. Integration with Other Assessments

**ISMS-IMP-A.8.28.1 (SDLC Assessment)**:
- SDLC "Requirements Phase" should include OSS approval
- SDLC "Build Phase" should include SCA scans
- SDLC "Testing Phase" should include dependency testing
- Cross-reference: SDLC requirements for dependency management

**ISMS-IMP-A.8.28.2 (Standards & Tools Assessment)**:
- SCA tools effectiveness assessed here
- License scanning tools assessed here
- Tool integration with developer workflow
- Cross-reference: Tool deployment vs. effectiveness

**ISMS-IMP-A.8.28.3 (Code Review & Testing Assessment)**:
- Third-party code should be reviewed with same rigor
- Dependency updates should be tested
- Security Champions involved in OSS approval
- Cross-reference: Review process for vendor code

**ISMS-IMP-A.8.28.5 (Compliance Dashboard)**:
- Supply chain security metrics feed into dashboard
- Vendor risk aggregated at organization level
- OSS inventory completeness tracked
- Cross-reference: Domain 4 of Dashboard

---

## 7. Continuous Improvement

**Quarterly Reviews**:
- Update vendor risk classifications
- Review OSS inventory completeness
- Assess SCA tool effectiveness
- Track vulnerability remediation trends

**Annual Reviews**:
- Comprehensive re-assessment across all domains
- Update policies based on lessons learned
- Benchmark against industry standards (e.g., SLSA, SSDF)
- Review and update legal risk guidance

**Incident-Driven Reviews**:
- Following major supply chain incidents (e.g., Log4Shell, SolarWinds)
- After vendor security breach
- After license compliance violation
- After abandoned dependency incident

**Metrics to Track Over Time**:
- Vendor security posture trend (% compliant vendors increasing)
- OSS inventory accuracy (% dependencies tracked)
- Vulnerability remediation speed (MTTR decreasing)
- License compliance rate (% violations decreasing)
- Supply chain attack mitigations (controls deployed)

**Benchmarking**:
- Compare against SLSA (Supply-chain Levels for Software Artifacts) framework
- Align with NIST SSDF (Secure Software Development Framework)
- Review OWASP Dependency-Check effectiveness
- Monitor industry supply chain incidents for lessons learned

---

**END OF SPECIFICATION**

**Document Status**: Ready for review and approval  
**Next Steps**: Python script generation (`generate_a828_4_third_party_oss.py`)  
**Estimated Script Complexity**: ~1,850 lines (5 domains × 18 requirements + supporting sheets)