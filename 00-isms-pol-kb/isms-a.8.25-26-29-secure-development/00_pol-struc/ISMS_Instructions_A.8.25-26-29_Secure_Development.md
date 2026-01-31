# PROJECT BRIEF: ISMS Controls A.8.25/26/29 - Secure Development

## Combined Control Approach

You are implementing **THREE related ISO 27001:2022 Annex A controls as a unified framework**:

- **A.8.25 - Secure Development Lifecycle**: Rules for secure development throughout SDLC
- **A.8.26 - Application Security Requirements**: Security requirements specification
- **A.8.29 - Security Testing in Development and Acceptance**: Testing during development

**Why Combined:**
These three controls form the **Secure Software Development Framework**:
- A.8.26 establishes WHAT security requirements applications must meet
- A.8.25 defines HOW to develop securely throughout the lifecycle
- A.8.29 verifies THAT security requirements are met through testing

Attempting to implement them separately would result in:
- Disconnected security requirements and development processes
- Redundant SDLC documentation
- Fragmented security testing approaches
- Inefficient evidence collection

**Reference Implementation**: 
- **Structure model**: ISMS-A.8.20-22-Network-Security (combined controls)
- **Quality level**: ISMS-A.8.23-Web-Filtering
- **Approach**: Unified secure development framework with distinct sections per control

**Integration Note**: This stack integrates with:
- A.8.4 (Access to Source Code) - Code repository security
- A.8.28 (Secure Coding) - Coding standards and practices
- A.8.31 (Environment Separation) - Dev/test/prod isolation
- A.8.32 (Change Management) - Release management

## Context & Approach

You are implementing a comprehensive **Secure Software Development Framework** using Systems Engineering methodology. This framework must be **completely generic** - applicable to any organization's SDLC, regardless of development methodology, technology stack, or team size.

**Implementation Philosophy**: 
- Apply Feynman's "don't fool yourself" principle - no security theater
- System Engineering approach: Requirements → Development → Testing → Evidence
- Think with TWO hats simultaneously:
  * **ISMS Implementer**: Build practical secure development framework
  * **ISMS Auditor**: Verify measurable security effectiveness
- Focus on genuine security improvement, not checkbox compliance

**Applicability**:
- All content must be **completely generic and technology-agnostic**
- Use "[Organization]" as placeholder throughout
- No assumptions about development methodology (Agile, Waterfall, DevOps, etc.)
- No assumptions about technology stack (languages, frameworks, platforms)
- Framework adapts to any SDLC environment

## Core Requirements (Specific to A.8.25/26/29)

### 1. The Secure Development Challenge

**Traditional approach (cargo cult):**
```
"We use HTTPS. Developers take a security training once a year.
We run a security scan before production... sometimes."
[No security requirements, no secure coding standards, no security testing]
```
❌ This is meaningless checkbox compliance.

**What auditors and implementers actually need:**

**For A.8.26 (Application Security Requirements):**
- Security requirements specification process
  - Functional security requirements (authentication, authorization, encryption)
  - Non-functional security requirements (performance under attack, resilience)
  - Data protection requirements (encryption, retention, deletion)
  - Security requirements traceability (requirements → implementation → testing)
- Security requirements by application risk/classification
  - High-risk applications (handles sensitive data, internet-facing, critical business function)
  - Medium-risk applications (internal use, limited data exposure)
  - Low-risk applications (public information, non-critical)
- Security requirements documentation
  - Security requirements specification template
  - Threat modeling requirements
  - Security acceptance criteria
- Security requirements validation
  - Security requirements review process
  - Security architecture review
  - Security requirements sign-off

**For A.8.25 (Secure Development Lifecycle):**
- SDLC security integration framework
  - Security activities in each SDLC phase (requirements, design, development, testing, deployment)
  - Security roles and responsibilities (developers, security champions, security team)
  - Secure development methodology (Agile security, DevSecOps, shift-left)
- Secure coding practices
  - Secure coding standards (OWASP, language-specific guidelines)
  - Code review requirements (peer review, security-focused review)
  - Secure coding training for developers
- Security tools integration
  - Static Application Security Testing (SAST) - analyze source code
  - Software Composition Analysis (SCA) - detect vulnerable dependencies
  - Secret scanning - detect hardcoded credentials
  - IDE security plugins - real-time security feedback
- Secure development environment
  - Developer workstation security baseline
  - Development tool security (IDE, repositories, CI/CD)
  - Source code protection (access control, encryption)
- Security defect management
  - Security bug tracking and prioritization
  - Vulnerability remediation timelines (critical, high, medium, low)
  - Security technical debt management

**For A.8.29 (Security Testing in Development and Acceptance):**
- Security testing strategy
  - Security testing types (SAST, DAST, IAST, SCA, penetration testing)
  - Security testing frequency (per commit, per sprint, per release)
  - Security testing coverage (code coverage, attack surface coverage)
- Static Application Security Testing (SAST)
  - SAST tool selection and configuration
  - SAST scan frequency (per commit, daily builds)
  - SAST results triage (true positive, false positive)
  - SAST findings remediation workflow
- Dynamic Application Security Testing (DAST)
  - DAST tool selection and configuration
  - DAST scan frequency (per deployment, weekly, monthly)
  - DAST authenticated vs. unauthenticated scans
  - DAST findings remediation workflow
- Software Composition Analysis (SCA)
  - SCA tool selection (dependency scanning)
  - SCA scan frequency (per build, continuous monitoring)
  - Vulnerable dependency remediation (upgrade, patch, accept risk)
  - License compliance checking (open-source license compatibility)
- Interactive Application Security Testing (IAST)
  - IAST tool deployment (if applicable)
  - Runtime security analysis
  - API security testing
- Penetration testing
  - Penetration testing frequency (annually, per major release)
  - Penetration testing scope (applications, APIs, infrastructure)
  - Penetration testing methodology (OWASP Testing Guide, PTES)
  - Penetration testing remediation and retesting
- Security acceptance testing
  - Security test cases in acceptance testing
  - Security regression testing
  - Security sign-off criteria

**Your SE Framework Must Provide:**
- **Security Requirements Framework** - specification and validation of application security requirements
- **Secure Development Methodology** - integration of security throughout SDLC
- **Security Testing Framework** - comprehensive testing strategy and execution
- **Evidence Collection Framework** - security requirements documentation, test results, remediation tracking

### 2. Document Length and Quality Guidelines

**Python Scripts:**
- Scripts should be **as long as required** to meet quality standards
- No arbitrary line limits - focus on correctness, robustness, maintainability
- Secure development assessment requires sophisticated parsing and analysis
- Quality > arbitrary length constraints

**Policy Documents (POLs):**
- Should be **comprehensive but not over-engineered**
- Include everything necessary for implementation and audit
- Avoid excessive theoretical content or academic tangents
- Practical and actionable guidance
- This is a 3-control stack with substantial SDLC integration content
- Expected range: 1,400-1,800 lines total
- "Just right" - not too short (incomplete), not too long (overkill)

**Implementation Guides (IMPs):**
- Should be **practical and focused**
- Step-by-step procedures without unnecessary elaboration
- Include examples and common pitfalls
- Don't repeat policy content - reference it
- Each section: reasonable length for the topic

**Annexes:**
- Technical appendices as needed
- OWASP Top 10 mapping
- Secure coding standards by language
- Security testing tool comparison
- Threat modeling templates

### 3. Document Structure (Adapted for A.8.25/26/29)

```
ISMS-A.8.25-26-29-Secure-Development/
├── 00_pol-struc/
│   └── [Framework planning, how three controls integrate]
├── 10_pol-md/
│   ├── ISMS-POL-A.8.25-26-29-S1-Executive-Control-Alignment.md
│   ├── ISMS-POL-A.8.25-26-29-S2-Security-Requirements-A826.md
│   ├── ISMS-POL-A.8.25-26-29-S3-Secure-Development-Lifecycle-A825.md
│   ├── ISMS-POL-A.8.25-26-29-S4-Security-Testing-A829.md
│   ├── ISMS-POL-A.8.25-26-29-S5-Assessment-Evidence-Framework.md
│   └── ISMS-POL-A.8.25-26-29-Annex-[Topic].md [if needed]
├── 30_imp-md/
│   ├── ISMS-IMP-A.8.25-26-29-S1-Security-Requirements-Process.md
│   ├── ISMS-IMP-A.8.25-26-29-S2-SDLC-Security-Integration.md
│   ├── ISMS-IMP-A.8.25-26-29-S3-Secure-Coding-Practices.md
│   ├── ISMS-IMP-A.8.25-26-29-S4-Security-Testing-Implementation.md
│   ├── ISMS-IMP-A.8.25-26-29-S5-Secure-Development-Assessment.md
│   └── ISMS-IMP-A.8.25-26-29-Annex-[Topic].md [if needed]
└── 50_scripts-excel/
    ├── generate_assessment_1_security_requirements.py
    ├── generate_assessment_2_sdlc_security_activities.py
    ├── generate_assessment_3_security_testing_results.py
    ├── generate_assessment_4_vulnerability_remediation.py
    └── generate_dashboard_secure_development.py
```

### 4. Policy Content Requirements (Specific to A.8.25/26/29)

**Section 1 (S1): Executive Summary, Control Alignment, Scope**
- ISO 27001:2022 control text for ALL THREE controls (exact quotes)
- Executive summary explaining unified secure development framework
- Scope: Framework covers security requirements, secure SDLC, security testing
- Integration approach: How three controls work together
- Relationship to other SDLC controls (A.8.4, A.8.28, A.8.31, A.8.32)

**Section 2 (S2): Application Security Requirements (A.8.26)**
Focus on **A.8.26 - Application Security Requirements** specifically:
- Security requirements specification process
- Security requirements by application classification (high/medium/low risk)
- Functional security requirements (authentication, authorization, input validation, encryption, logging)
- Non-functional security requirements (secure by default, fail secure, security performance)
- Data protection requirements (encryption, retention, deletion, privacy)
- Security requirements traceability (requirements → design → code → tests)
- Threat modeling requirements
- Security architecture review requirements
- Measurable requirements with audit verification criteria

**Section 3 (S3): Secure Development Lifecycle (A.8.25)**
Focus on **A.8.25 - Secure Development Lifecycle** specifically:
- SDLC security framework (security in each phase)
- Secure coding standards (OWASP, language-specific)
- Code review requirements (peer review, security-focused review)
- Security tools integration (SAST, SCA, secret scanning)
- Secure development environment (workstation security, tool security)
- Security training for developers
- Security defect management
- Security technical debt management
- Measurable requirements with audit verification criteria

**Section 4 (S4): Security Testing in Development (A.8.29)**
Focus on **A.8.29 - Security Testing in Development and Acceptance** specifically:
- Security testing strategy (types, frequency, coverage)
- SAST (static analysis) requirements
- DAST (dynamic analysis) requirements
- SCA (dependency scanning) requirements
- IAST (interactive testing) requirements
- Penetration testing requirements
- Security acceptance testing
- Security test results management
- Vulnerability remediation workflows
- Measurable requirements with audit verification criteria

**Section 5 (S5): Assessment Methodology and Evidence Framework**
- Security requirements documentation assessment
- SDLC security activity assessment
- Security testing results assessment
- Vulnerability remediation tracking
- Evidence collection per control
- Compliance scoring methodology

### 5. Implementation Guidance Requirements

**IMP-S1: Security Requirements Process**
- Security requirements elicitation
- Threat modeling execution
- Security requirements documentation
- Security architecture review

**IMP-S2: SDLC Security Integration**
- Security activities by SDLC phase
- Secure development methodology (Agile, DevSecOps)
- Security training program
- Security champion program

**IMP-S3: Secure Coding Practices**
- Secure coding standards implementation
- Code review process
- Security tools deployment (SAST, SCA, secret scanning)
- IDE security plugin configuration

**IMP-S4: Security Testing Implementation**
- Security testing tool selection
- SAST/DAST/SCA tool configuration
- Penetration testing program
- Security testing automation (CI/CD integration)

**IMP-S5: Secure Development Assessment**
- Security requirements completeness assessment
- SDLC security activity tracking
- Security testing coverage assessment
- Vulnerability remediation compliance

### 6. Assessment Tools (Specific to A.8.25/26/29)

**Assessment Workbook 1: Security Requirements Compliance (A.8.26)**
- Application inventory with risk classification
- Security requirements documentation status
- Threat modeling status
- Security architecture review status
- Requirements traceability compliance

**Assessment Workbook 2: SDLC Security Activities (A.8.25)**
- Security activities by SDLC phase (planned vs. executed)
- Secure coding standard compliance
- Code review completion rate
- Security training completion
- Security tool deployment status

**Assessment Workbook 3: Security Testing Results (A.8.29)**
- SAST scan results (findings by severity)
- DAST scan results
- SCA scan results (vulnerable dependencies)
- Penetration testing results
- Security testing coverage

**Assessment Workbook 4: Vulnerability Remediation Tracking (A.8.29)**
- Open vulnerabilities (by severity, age)
- Remediation SLA compliance
- Vulnerability trends over time
- Security technical debt tracking

**Dashboard: Secure Development Maturity**
- Overall secure development score
- Security requirements coverage
- SDLC security activity completion
- Security testing coverage
- Vulnerability remediation performance
- Trend analysis

### 7. Python Scripts Approach

Scripts should:
- Parse security requirements documentation
- Parse security testing tool outputs (SAST, DAST, SCA)
- Calculate coverage metrics
- Track vulnerability remediation
- Generate compliance dashboards

**No arbitrary line limits** - comprehensive error handling and data integration is critical.

### 8. Key Integration Points

**Integrates with:**
- A.8.4 (Source Code Access) - Repository security
- A.8.28 (Secure Coding) - Coding standards
- A.8.31 (Environment Separation) - Dev/test/prod
- A.8.32 (Change Management) - Release process
- A.5.24-27 (Incident Management) - Security vulnerabilities
- A.8.8 (Vulnerability Management) - Production vulnerabilities

### 9. Quality Checks

- [ ] All THREE control texts quoted correctly
- [ ] Each control's requirements distinctly addressed
- [ ] Framework works for any SDLC methodology
- [ ] No assumptions about technology stack
- [ ] Assessment workbooks cover all three controls
- [ ] Security testing types comprehensively covered
- [ ] OWASP alignment documented

### 10. Regulatory Framework (per ISMS-POL-00)

**Mandatory Compliance (Tier 1):**
- ISO/IEC 27001:2022: Controls A.8.25, A.8.26, A.8.29

**Conditional Compliance (Tier 2):**
- **FINMA** (if Swiss financial institution):
  - FINMA Circular 2023/1 Margin 50-62: Information security includes secure development
- **DORA** (if EU financial entity):
  - Article 9: ICT risk management includes secure development
- **NIS2** (if essential/important entity):
  - Article 21(2): Security measures include secure development practices

**Informational Reference (Tier 3):**
- OWASP SAMM (Software Assurance Maturity Model)
- NIST SP 800-218 (Secure Software Development Framework)
- BSI APP.3.1 (Web Applications)
- OWASP ASVS (Application Security Verification Standard)
- OWASP Testing Guide

For complete regulatory categorization, refer to ISMS-POL-00.

### 11. Special Considerations

**SDLC Methodology Diversity:**
- Waterfall: Security gates at phase transitions
- Agile: Security in each sprint
- DevOps/DevSecOps: Security automation in CI/CD
- Framework must work for all

**Technology Stack Diversity:**
- Languages: Java, Python, C#, JavaScript, Go, etc.
- Frameworks: Spring, Django, .NET, React, etc.
- Platforms: Web, mobile, desktop, embedded, cloud-native
- Framework must be generic

**Security Testing Tool Diversity:**
- SAST: SonarQube, Checkmarx, Fortify, Snyk Code, Semgrep
- DAST: OWASP ZAP, Burp Suite, Acunetix, AppScan
- SCA: Snyk, Dependabot, WhiteSource, Black Duck
- Framework must be vendor-neutral

**Open Source vs. Commercial Development:**
- Internal development (proprietary)
- Open source contribution (public repositories)
- Third-party component integration
- Framework must address all models

### 12. Autonomous Work Requirements

**READ Phase:**
- Review reference implementations
- Understand secure development context
- Identify SDLC security patterns

**UPDATE Phase:**
- Adapt to secure development context
- Ensure all three controls distinctly addressed
- Maintain quality

**TEST Phase:**
- Fix UTF-8 encoding proactively
- Keep emojis in Excel workbooks
- Test formulas carefully
- Verify conditional formatting
- Test scripts mentally

**PRESENT Phase:**
- Deliver complete sections
- Self-assess against checklist
- Flag uncertainties

### 13. Deliverable Sequence

1. **Structure Plan** - Confirm approach, sections, workbooks
2. **Policy Sections** (S1→S2→S3→S4→S5) - Wait for approval between each
3. **Implementation Sections** (S1→S2→S3→S4→S5) - Wait for approval
4. **Assessment Scripts** - Test thoroughly before delivery
5. **Quality Review** - Self-assessment

---

## Your Mission for A.8.25/26/29

Create the **Secure Software Development Framework** that provides:
- Systematic security requirements specification (A.8.26)
- Comprehensive secure development lifecycle integration (A.8.25)
- Rigorous security testing throughout development (A.8.29)
- Unified secure development evidence collection
- Technology and methodology-agnostic principles

Use Systems Engineering methodology for **systematic secure development assessment**.

Make it completely generic - works for any SDLC, any technology, any organization.

Think like a security architect AND an auditor.

**Ready? Let's start with the structure plan.**
