# ISMS-POL-A.8.28 – Secure Coding
## Comprehensive Policy & Implementation Framework

---

**Document ID**: ISMS-POL-A.8.28  
**Title**: Secure Coding Policy  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Application Security Manager | Initial policy framework |

**Review Cycle**: Annual (or upon significant organizational/regulatory/threat landscape changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Chief Technology Officer (CTO) or VP Engineering
- Legal/Compliance Officer (for regulatory alignment)
- Executive Management / Board (for strategic approval)

**Distribution**: All developers, security team, architects, QA engineers, DevOps, third-party development vendors  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.28, ISO/IEC 27002:2022 Control 8.28, OWASP ASVS, NIST SP 800-218 SSDF, CWE Top 25

---

## Executive Summary

This document serves as the **master index** for the organization's secure coding control framework, implementing ISO/IEC 27001:2022 Control A.8.28. The framework consists of:

- **Policy Layer:** Governance documents defining requirements (~14 documents)
- **Assessment Layer:** Technical evaluation specifications (5 markdown specs)
- **Implementation Layer:** Automated Excel workbook generators (5 Python scripts)
- **Validation Layer:** Quality assurance and checking tools
- **Integration Layer:** Executive dashboard with consolidated oversight

**Approach:** This framework uses a **system engineering methodology** rather than traditional paperwork-based compliance. All assessments are generated via Python scripts to ensure consistency, repeatability, and maintainability.

**Control Objective (ISO/IEC 27002:2022 Control 8.28):**
> *Principles for secure coding should be applied in software development.*

**Purpose:** Ensure software is developed securely throughout the entire development lifecycle, reducing security vulnerabilities, preventing common coding errors, and maintaining compliance with security standards and regulatory requirements while enabling rapid, high-quality software delivery.

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.8.28 - Secure Coding**

This policy framework provides the organizational governance, requirements, roles, and procedures necessary to fulfill Control 8.28 objectives and integrate secure coding practices across the Software Development Lifecycle (SDLC) within the Information Security Management System (ISMS).

**Regulatory Alignment**: This framework complies with ISO/IEC 27001:2022 requirements and aligns with Swiss Federal Data Protection Act (FADP), EU GDPR where applicable, and industry-specific regulations (financial services, healthcare, etc.) as relevant to the organization.

---

## 1. Framework Structure

### 1.1 Purpose

Define mandatory requirements for secure software development practices to minimize security vulnerabilities, prevent exploitation of software weaknesses, protect organizational data and systems, and maintain compliance with legal, statutory, regulatory, and contractual security requirements throughout the software development lifecycle.

### 1.2 Scope

This framework applies to:

- **Development Activities:** All software development including new development, maintenance, enhancements, and bug fixes
- **Development Types:** Internal development, outsourced development, acquired software customization
- **Application Types:** Web applications, mobile applications, desktop applications, APIs, microservices, embedded systems
- **Development Phases:** Requirements, design, implementation, testing, deployment, and maintenance
- **Third-Party Components:** Open-source libraries, commercial frameworks, vendor SDKs, code libraries
- **Development Environments:** All development, testing, staging, and production environments
- **Programming Languages:** All languages used by the organization (Java, C#, Python, JavaScript, C/C++, Go, etc.)

### 1.3 Users

This framework is binding for:

- **Developers** – Must follow secure coding standards and practices
- **Security Champions** – Provide security expertise and guidance within development teams
- **Code Reviewers** – Conduct security-focused code reviews
- **QA Engineers** – Execute security testing procedures
- **DevOps/Platform Teams** – Maintain secure development tooling and CI/CD pipelines
- **Architects** – Design secure system architectures and perform threat modeling
- **Development Managers** – Ensure team compliance with secure coding requirements
- **Third-Party Vendors** – Must meet contractual security obligations for outsourced development
- **Auditors and Regulators** – May review for compliance verification

### 1.4 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this secure coding framework are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Mandatory Compliance:**
* Swiss Federal Data Protection Act (FADP)
* EU GDPR (where processing EU personal data)
* ISO/IEC 27001:2022 (Control A.8.28)
* [Additional mandatory regulations per ISMS-POL-00]

**Informational Reference / Best Practice Alignment:**
* OWASP Top 10 & ASVS (Application Security Verification Standard)
* NIST SP 800-218 Secure Software Development Framework (SSDF)
* CWE Top 25 Most Dangerous Software Weaknesses
* SANS Top 25 Most Dangerous Software Errors
* [Other frameworks per ISMS-POL-00]

**United States Federal Requirements:**
References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where the organization has explicit US federal contractual obligations, as defined in **ISMS-POL-00**.

For complete regulatory categorization, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

---

## 2. Policy Documents

### 2.1 Policy Structure

The secure coding policy framework consists of the following modular documents:

| Document ID | Title | Purpose | Lines |
|-------------|-------|---------|-------|
| **ISMS-POL-A.8.28** | Master Framework | This document - index and overview | ~400 |
| **ISMS-POL-A.8.28-S1** | Purpose, Scope, Definitions | Foundation and terminology | ~400 |
| **ISMS-POL-A.8.28-S2** | Requirements Overview | Requirements framework structure | ~300 |
| **ISMS-POL-A.8.28-S2.1** | Pre-Development Requirements | Threat modeling, design, architecture, training | ~400 |
| **ISMS-POL-A.8.28-S2.2** | Secure Coding Standards | Language-agnostic and specific coding standards | ~400 |
| **ISMS-POL-A.8.28-S2.3** | Code Review & Testing Requirements | Peer review, SAST, DAST, penetration testing | ~400 |
| **ISMS-POL-A.8.28-S2.4** | Third-Party & OSS Management | Component security, SCA, license compliance | ~400 |
| **ISMS-POL-A.8.28-S3** | Roles & Responsibilities | RACI and accountability | ~400 |
| **ISMS-POL-A.8.28-S4** | Policy Governance | Review, exceptions, compliance monitoring | ~400 |
| **ISMS-POL-A.8.28-S5** | Annexes | Supporting materials | ~300 |
| **ISMS-POL-A.8.28-S5.A** | Language-Specific Guidelines | Java, C#, Python, JavaScript, C/C++, Go, etc. | ~400 |
| **ISMS-POL-A.8.28-S5.B** | Code Review Checklist Template | Security-focused review checklist | ~400 |
| **ISMS-POL-A.8.28-S5.C** | Vulnerability Response Procedures | Discovery, classification, remediation | ~400 |
| **ISMS-POL-A.8.28-S5.D** | Quick Reference Guide | Developer quick-start guide | ~300 |

**Total Policy Layer:** ~14 documents, approximately 5,100 lines

**Design Philosophy**: Each document is independently versionable (maximum 300-400 lines) to enable granular change management, targeted stakeholder reviews, and clear audit trails.

### 2.2 Document Hierarchy
```
ISMS-POL-A.8.28 (Master) ← You are here
├── ISMS-POL-A.8.28-S1 (Purpose, Scope, Definitions)
├── ISMS-POL-A.8.28-S2 (Requirements Overview)
│   ├── ISMS-POL-A.8.28-S2.1 (Pre-Development Requirements)
│   ├── ISMS-POL-A.8.28-S2.2 (Secure Coding Standards)
│   ├── ISMS-POL-A.8.28-S2.3 (Code Review & Testing Requirements)
│   └── ISMS-POL-A.8.28-S2.4 (Third-Party & OSS Management)
├── ISMS-POL-A.8.28-S3 (Roles & Responsibilities)
├── ISMS-POL-A.8.28-S4 (Policy Governance)
└── ISMS-POL-A.8.28-S5 (Annexes)
    ├── ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines)
    ├── ISMS-POL-A.8.28-S5.B (Code Review Checklist Template)
    ├── ISMS-POL-A.8.28-S5.C (Vulnerability Response Procedures)
    └── ISMS-POL-A.8.28-S5.D (Quick Reference Guide)

Implementation Layer (Separate Documents):
├── ISMS-IMP-A.8.28.1 (SDLC Assessment)
├── ISMS-IMP-A.8.28.2 (Standards & Tools Assessment)
├── ISMS-IMP-A.8.28.3 (Code Review & Testing Assessment)
├── ISMS-IMP-A.8.28.4 (Third-Party & OSS Assessment)
└── ISMS-IMP-A.8.28.5 (Compliance Dashboard)
```

---

## 3. Assessment & Implementation Documents

### 3.1 Assessment Specifications (Markdown)

The framework includes **5 comprehensive assessment specifications** defining the structure and requirements for Excel workbook generation:

| Document ID | Title | Purpose | Sheets |
|-------------|-------|---------|--------|
| **ISMS-IMP-A.8.28.1** | SDLC Assessment | Evaluate secure development lifecycle maturity and controls | ~10 |
| **ISMS-IMP-A.8.28.2** | Standards & Tools Assessment | Document coding standards, development tools, CI/CD security | ~10 |
| **ISMS-IMP-A.8.28.3** | Code Review & Testing Assessment | Assess code review processes and security testing coverage | ~10 |
| **ISMS-IMP-A.8.28.4** | Third-Party & OSS Assessment | Evaluate component security, SCA, license compliance | ~10 |
| **ISMS-IMP-A.8.28.5** | Compliance Dashboard | Executive summary with KPIs and gap analysis | ~9 |

**Key Features:**
- Technology-independent (assess ANY development environment)
- Evidence-based (yellow cells require proof)
- Quantitative metrics (compliance percentages, vulnerability counts)
- Audit-ready (built-in evidence register, approval workflow)

### 3.2 Assessment Domains

#### Domain 1: Secure Development Lifecycle (SDLC)
**Focus:** Development process maturity, security integration at each phase, training, governance

**Assessment Areas:**
- Development lifecycle phase security integration
- Threat modeling and risk assessment processes
- Development environment security controls
- Developer training and competency management
- SDLC documentation and governance maturity

**Primary Stakeholders:** Development Managers, Security Champions, Architects

#### Domain 2: Coding Standards & Development Tools
**Focus:** Coding standards documentation, IDE security configuration, version control, CI/CD pipeline security

**Assessment Areas:**
- Language-specific secure coding standards
- Development tool security configuration
- Source code repository and version control security
- Build and CI/CD pipeline security controls
- Documentation and knowledge management

**Primary Stakeholders:** Developers, DevOps Teams, Platform Engineers

#### Domain 3: Code Review & Security Testing
**Focus:** Peer review processes, SAST/DAST tools, penetration testing, vulnerability management

**Assessment Areas:**
- Peer code review process and security checklist
- Static Application Security Testing (SAST) implementation
- Dynamic Application Security Testing (DAST) implementation
- Penetration testing frequency and coverage
- Security testing metrics and effectiveness

**Primary Stakeholders:** Security Team, QA Engineers, Code Reviewers

#### Domain 4: Third-Party & Open Source Management
**Focus:** Component inventory, vulnerability scanning (SCA), license compliance, vendor assessment

**Assessment Areas:**
- Software Bill of Materials (SBOM) generation and maintenance
- Software Composition Analysis (SCA) tool deployment
- Open-source license compliance verification
- Vendor security assessment for outsourced development
- Supply chain security controls

**Primary Stakeholders:** Security Team, Legal/Compliance, Procurement

#### Domain 5: Compliance Dashboard & Metrics
**Focus:** Executive visibility, KPI tracking, gap analysis, risk prioritization

**Assessment Areas:**
- Overall compliance summary across domains 1-4
- SDLC maturity trending
- Code quality and security metrics
- Third-party risk indicators
- Board-level reporting and resource planning

**Primary Stakeholders:** CISO, CTO, Executive Management, Board

---

## 4. Scripts & Automation

### 4.1 Python Generator Scripts (5 Scripts)

Each assessment domain has a dedicated Python script generating a comprehensive Excel workbook:

| Script Name | Purpose | Output Workbook | Sheets |
|-------------|---------|-----------------|--------|
| `generate_a828_1_sdlc_assessment.py` | Generate SDLC assessment workbook | ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx | 9 |
| `generate_a828_2_standards_tools.py` | Generate standards/tools assessment | ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx | 9 |
| `generate_a828_3_code_review_testing.py` | Generate code review/testing assessment | ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_YYYYMMDD.xlsx | 9 |
| `generate_a828_4_third_party_oss.py` | Generate third-party/OSS assessment | ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx | 9 |
| `generate_a828_5_compliance_dashboard.py` | Generate compliance dashboard | ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx | 9 |

**Standard Workbook Structure (each script generates):**
- Sheet 1: Instructions & Legend (how to complete, status definitions, evidence examples)
- Sheets 2-6: Assessment Sheets (5 domain-specific assessments with checklists + reference tables)
- Sheet 7: Summary Dashboard (compliance metrics, gap analysis, KPIs)
- Sheet 8: Evidence Register (100 rows for audit evidence tracking)
- Sheet 9: Approval Sign-Off (3-level approval workflow)

**Technical Requirements:**
- Python 3.8+
- openpyxl library (`sudo apt install python3-openpyxl`)
- Generates .xlsx format (Excel 2010+)
- Filename includes generation date (YYYYMMDD format)

### 4.2 Validation Script

**Script:** `excel_sanity_check_a828.py`

**Purpose:** Validate generated Excel workbooks for structural integrity, formula correctness, data validation setup

**Checks:**
- All required sheets present
- Column structure matches specification
- Data validations properly configured
- Formulas calculate correctly
- Styling consistent across workbook
- Evidence register has 100 rows
- Approval workflow complete

**Usage:**
```bash
python3 excel_sanity_check_a828.py ISMS-IMP-A.8.28.1_SDLC_Assessment_20260105.xlsx
```

---

## 5. Stakeholder Guide

### 5.1 For Developers

**What You Need to Know:**
- **S2.2 (Secure Coding Standards):** Your daily coding requirements
- **S5.A (Language-Specific Guidelines):** Standards for your programming language
- **S5.D (Quick Reference Guide):** One-page cheat sheet

**What You Need to Do:**
- Follow secure coding standards for your language
- Participate in peer code reviews with security focus
- Complete security training annually
- Report security vulnerabilities discovered
- Use approved development tools and configurations

**Assessment Participation:**
- None directly (your manager/security champion completes assessments)

### 5.2 For Security Champions

**What You Need to Know:**
- **Entire policy framework** (all sections)
- **S2.3 (Code Review & Testing):** Your primary responsibility area
- **S5.B (Code Review Checklist):** Review guidance

**What You Need to Do:**
- Conduct security-focused code reviews
- Provide secure coding guidance to team
- Escalate security concerns
- Participate in threat modeling
- Track security metrics for your team

**Assessment Participation:**
- Contribute to IMP-A.8.28.1 (SDLC) and IMP-A.8.28.3 (Code Review & Testing)

### 5.3 For Application Security Team

**What You Need to Know:**
- **Entire policy framework** (policy owner perspective)
- **All S2 sections** (requirements you enforce)
- **S4 (Policy Governance):** Exception management, compliance monitoring

**What You Need to Do:**
- Own and maintain this policy framework
- Configure and manage security testing tools (SAST, DAST, SCA)
- Review and approve exceptions
- Monitor compliance metrics
- Conduct security assessments and audits
- Provide security training to developers

**Assessment Participation:**
- Complete all 5 IMP assessments (or coordinate completion)
- Own IMP-A.8.28.5 (Compliance Dashboard)

### 5.4 For Development Managers

**What You Need to Know:**
- **S1 (Purpose, Scope, Definitions):** Framework overview
- **S2 (Requirements Overview):** What your team must do
- **S3 (Roles & Responsibilities):** Your accountability

**What You Need to Do:**
- Ensure team follows secure coding standards
- Allocate time for security activities (reviews, testing, training)
- Support security champion role in your team
- Review and act on security metrics
- Escalate resource or timeline concerns affecting security

**Assessment Participation:**
- Contribute to IMP-A.8.28.1 (SDLC) and IMP-A.8.28.2 (Standards & Tools)

### 5.5 For Architects

**What You Need to Know:**
- **S2.1 (Pre-Development Requirements):** Threat modeling, secure design
- **S2.2 (Secure Coding Standards):** Architecture patterns and anti-patterns
- **S5.A (Language-Specific Guidelines):** Framework recommendations

**What You Need to Do:**
- Conduct threat modeling for new systems
- Define secure architecture patterns
- Review high-risk design decisions
- Approve technology and framework choices
- Document security design decisions

**Assessment Participation:**
- Contribute to IMP-A.8.28.1 (SDLC) - threat modeling and architecture sections

### 5.6 For QA Engineers

**What You Need to Know:**
- **S2.3 (Code Review & Testing):** Security testing requirements
- **S5.C (Vulnerability Response):** Bug reporting and tracking

**What You Need to Do:**
- Execute security test cases
- Validate security control effectiveness
- Report security defects with appropriate severity
- Verify vulnerability remediation
- Maintain security testing documentation

**Assessment Participation:**
- Contribute to IMP-A.8.28.3 (Code Review & Testing)

### 5.7 For DevOps/Platform Teams

**What You Need to Know:**
- **S2.1 (Pre-Development Requirements):** Development environment security
- **S2.2 (Secure Coding Standards):** CI/CD pipeline security requirements

**What You Need to Do:**
- Maintain secure development tooling
- Secure CI/CD pipelines
- Integrate security scanning tools
- Manage secrets and credentials securely
- Monitor pipeline security events

**Assessment Participation:**
- Contribute to IMP-A.8.28.2 (Standards & Tools)

### 5.8 For Third-Party Development Vendors

**What You Need to Know:**
- **S1 (Purpose, Scope, Definitions):** Framework applicability to vendors
- **S2.2 (Secure Coding Standards):** Standards you must follow
- **S2.4 (Third-Party & OSS Management):** Vendor obligations
- **S5.A (Language-Specific Guidelines):** Standards for your language

**What You Need to Do:**
- Follow all secure coding requirements in contract
- Provide SBOMs for delivered software
- Report security vulnerabilities discovered
- Participate in security assessments and audits
- Maintain current security training for your developers

**Assessment Participation:**
- Complete vendor security questionnaires
- Provide evidence for IMP-A.8.28.4 (Third-Party & OSS)

### 5.9 For Auditors

**What You Need to Know:**
- **Entire policy framework** (audit scope)
- **All IMP documents** (evidence structure)
- **Section 8 of this document** (Audit & Compliance guidance)

**What You Review:**
- Policy completeness and approval
- Assessment workbook completion and evidence quality
- Gap remediation tracking
- Compliance metrics and trends
- Incident response to security vulnerabilities

**Assessment Artifacts:**
- All 5 completed IMP workbooks with evidence register populated
- Evidence artifacts (SAST reports, code review records, training certificates)
- Compliance Dashboard showing metrics and gaps

---

## 6. Regulatory Compliance

### 6.1 ISO/IEC 27001:2022 Control A.8.28 Mapping

**ISO 27002:2022 Guidance - Key Requirements:**

**Pre-Development Planning:**
- Organization-specific secure coding principles
- Common vulnerability patterns and historical lessons
- Development tool configuration for security
- Vendor guideline compliance
- Current tool maintenance
- Developer security qualification
- Secure design and threat modeling
- Secure programming standards
- Controlled development environments

**During Development:**
- Language-specific secure coding practices
- Secure programming techniques (pair programming, peer review, refactoring)
- Structured programming techniques
- Code documentation and error elimination
- Prohibition of insecure patterns (hardcoded credentials, etc.)

**Governance & Continuous Improvement:**
- Organization-wide secure coding governance
- Minimum security baseline
- Extension to third-party and open-source components
- Real threat and vulnerability monitoring
- Continuous improvement processes

**Framework Coverage:**
This policy framework addresses ALL ISO 27002:2022 guidance for Control 8.28 through:
- **S2.1:** Pre-development planning requirements
- **S2.2:** Secure coding standards (language-specific)
- **S2.3:** Code review and testing (peer review, SAST, DAST)
- **S2.4:** Third-party and open-source governance
- **S4:** Policy governance and continuous improvement

### 6.2 OWASP Alignment

**OWASP Top 10 (2021) Coverage:**

This framework addresses all OWASP Top 10 risks through secure coding practices:

| OWASP Risk | Policy Coverage | Implementation Assessment |
|------------|-----------------|---------------------------|
| A01:2021 Broken Access Control | S2.2 (access control patterns) | IMP-A.8.28.2, IMP-A.8.28.3 |
| A02:2021 Cryptographic Failures | S2.2 (crypto requirements) | IMP-A.8.28.2 |
| A03:2021 Injection | S2.2 (input validation) | IMP-A.8.28.2, IMP-A.8.28.3 |
| A04:2021 Insecure Design | S2.1 (threat modeling) | IMP-A.8.28.1 |
| A05:2021 Security Misconfiguration | S2.1 (dev environment), S2.2 (CI/CD) | IMP-A.8.28.1, IMP-A.8.28.2 |
| A06:2021 Vulnerable Components | S2.4 (third-party/OSS) | IMP-A.8.28.4 |
| A07:2021 Authentication Failures | S2.2 (authentication patterns) | IMP-A.8.28.2 |
| A08:2021 Software/Data Integrity | S2.2 (CI/CD security) | IMP-A.8.28.2 |
| A09:2021 Logging/Monitoring Failures | S2.2 (error handling/logging) | IMP-A.8.28.2 |
| A10:2021 SSRF | S2.2 (input validation) | IMP-A.8.28.2, IMP-A.8.28.3 |

**OWASP ASVS Integration:**
- Assessment checklists map to ASVS verification requirements
- Language-specific guidelines reference ASVS levels (L1, L2, L3)
- Testing requirements align with ASVS testing methodology

### 6.3 CWE Top 25 Coverage

**CWE (Common Weakness Enumeration) Top 25 Most Dangerous Software Weaknesses:**

Addressed through:
- **S5.A (Language-Specific Guidelines):** Language-specific vulnerability patterns
- **S5.B (Code Review Checklist):** CWE-focused review items
- **IMP-A.8.28.3:** SAST tool configuration for CWE detection

**Key CWE Categories Covered:**
- CWE-79 (Cross-site Scripting)
- CWE-89 (SQL Injection)
- CWE-20 (Improper Input Validation)
- CWE-78 (OS Command Injection)
- CWE-787 (Out-of-bounds Write)
- CWE-22 (Path Traversal)
- CWE-352 (CSRF)
- CWE-434 (Unrestricted File Upload)
- [All Top 25 CWEs addressed]

### 6.4 NIST Secure Software Development Framework (SSDF)

**NIST SP 800-218 Practice Mapping:**

| SSDF Practice | Policy Section | Assessment |
|---------------|----------------|------------|
| PO.1: Define security requirements | S2.1 | IMP-A.8.28.1 |
| PO.2: Implement security controls | S2.2 | IMP-A.8.28.2 |
| PO.3: Produce well-secured software | S2.2, S2.3 | IMP-A.8.28.2, IMP-A.8.28.3 |
| PO.4: Respond to vulnerabilities | S5.C | IMP-A.8.28.3 |
| PS.1: Protect software from unauthorized changes | S2.2 | IMP-A.8.28.2 |
| PS.2: Provide verifiable artifacts | S2.4 | IMP-A.8.28.4 |
| PS.3: Archive and protect artifacts | S2.2 | IMP-A.8.28.2 |
| PW.1: Design secure software | S2.1 | IMP-A.8.28.1 |
| PW.2: Review design | S2.1 | IMP-A.8.28.1 |
| [All SSDF practices mapped] | | |

---

## 7. Exception Management

### 7.1 Exception Types

**Acceptable Exceptions (with approval):**
- **Temporary Deviation:** Specific code requiring exception pending refactoring (with deadline)
- **Legacy System:** Older system where remediation cost exceeds risk (with compensating controls)
- **Technology Limitation:** Tool or language constraint preventing full compliance (with documented limitation)
- **Business Criticality:** Immediate business need requiring expedited deployment (with follow-up plan)

**Unacceptable Exceptions:**
- Critical security vulnerabilities (CVSS 9.0+)
- Legal/regulatory non-compliance
- Customer data protection failures
- Authentication/authorization bypasses
- Hardcoded credentials or secrets

### 7.2 Exception Process

**Request Submission:**
1. Developer/Manager submits exception request via designated process
2. Request includes: description, justification, risk assessment, compensating controls, remediation plan
3. Security team reviews technical feasibility and risk
4. Risk owner (CISO or delegate) approves or denies

**Exception Tracking:**
- All exceptions tracked in IMP assessment workbooks (Exception/Deviation sections)
- Quarterly exception review
- Automatic escalation if remediation deadline missed
- Annual exception portfolio review by CISO

**Exception Expiration:**
- Temporary exceptions: Maximum 90 days, renewable once
- Legacy system exceptions: Annual review, must justify continued acceptance
- All exceptions automatically expire at next major release

---

## 8. Metrics & Reporting

### 8.1 Key Performance Indicators (KPIs)

**SDLC Maturity Metrics:**
- % of projects with completed threat models
- % of developers with current security training
- Development environment security compliance score
- SDLC documentation completeness score

**Code Quality Metrics:**
- Code review coverage (% of commits reviewed)
- SAST scan frequency and coverage
- DAST scan frequency and coverage
- Vulnerability density (vulns per 1000 lines of code)
- Remediation velocity (average time to fix by severity)

**Third-Party Risk Metrics:**
- % of dependencies with known CVEs
- Critical vulnerability exposure window (days)
- SBOM generation compliance rate
- License compliance rate

**Training & Awareness Metrics:**
- % of developers with current secure coding training
- Security champion coverage (% of teams with champion)
- Security training completion rate

**Vulnerability Management Metrics:**
- Mean Time to Detect (MTTD) vulnerabilities
- Mean Time to Remediate (MTTR) by severity
- Vulnerability backlog age
- Vulnerability recurrence rate

### 8.2 Dashboard & Reporting

**IMP-A.8.28.5 (Compliance Dashboard) Provides:**
- Executive summary (one-page compliance status)
- Trend analysis (quarter-over-quarter comparison)
- Gap analysis (prioritized remediation roadmap)
- Risk heat map (likelihood vs. impact)
- Resource planning (security team workload, budget needs)

**Reporting Frequency:**
- **Monthly:** Security team internal review
- **Quarterly:** Executive management reporting (CISO to CTO/Board)
- **Annual:** Comprehensive compliance assessment for ISO 27001 audit

**Reporting Audience:**
- **Operational:** Development teams, Security team
- **Management:** CTO, VP Engineering, CISO
- **Executive:** Board of Directors (quarterly)
- **External:** ISO 27001 auditors, regulators (upon request)

---

## 9. Audit & Compliance

### 9.1 Audit Artifacts

**Policy Documentation:**
- All 14 policy documents (POL-A.8.28 + sections S1-S5.D)
- Document approval records
- Version history and change logs

**Assessment Workbooks:**
- All 5 completed IMP assessment workbooks
- Evidence register with supporting documentation
- Approval sign-offs

**Technical Evidence:**
- SAST/DAST/SCA scan reports
- Code review records (peer reviews, security reviews)
- Threat model documents
- Penetration test reports
- Training completion certificates
- SBOM (Software Bill of Materials) files
- Vulnerability tracking reports
- Remediation verification records

**Governance Evidence:**
- Exception requests and approvals
- Compliance metrics dashboards
- Incident response records (security vulnerabilities)
- Policy violation and remediation records

### 9.2 Audit Methodology

**Recommended Audit Approach:**

1. **Document Review:** Verify policy completeness, approval, and distribution
2. **Stakeholder Interviews:** Developers, Security Champions, Security Team, Architects
3. **Technical Assessment:** Review SAST/DAST/SCA tool configurations, sample scan reports
4. **Code Sampling:** Select code repositories for manual security review
5. **Tool Validation:** Verify security testing tools are operational and current
6. **Evidence Validation:** Cross-reference assessment workbooks with technical evidence
7. **Gap Analysis:** Compare actual vs. required state, assess remediation plans
8. **Remediation Review:** Validate gap closure timelines and progress

**Audit Scope Sampling:**
- Minimum 3 applications (low/medium/high criticality)
- Minimum 2 development teams
- All programming languages in use
- All phases of SDLC (design through deployment)
- Third-party and open-source components

**Audit Frequency:**
- **Internal Audit:** Annual (minimum)
- **External Audit:** As required by ISO 27001 certification body
- **Regulatory Audit:** As required by applicable regulations
- **Self-Assessment:** Quarterly (using IMP assessment workbooks)

---

## 10. Policy Maintenance

### 10.1 Review Schedule

**Annual Review:** Comprehensive review of all policy sections (recommended Q4)

**Triggered Reviews:** Major events requiring immediate policy review:
- Significant regulatory changes (new laws, updated standards)
- Major security incidents (data breach, vulnerability exploitation)
- Technology stack changes (new languages, frameworks, tools)
- Organizational changes (mergers, acquisitions, major restructuring)
- Threat landscape shifts (new attack patterns, widespread campaigns)
- Audit findings requiring policy updates
- Major OWASP Top 10 or CWE Top 25 updates

### 10.2 Version Control

**Major Version (X.0):** Structural changes, scope modifications, new regulatory requirements  
**Minor Version (X.Y):** Content updates, clarifications, additions without structural change

**Master Framework Versioning:**
- This master document version reflects overall framework state
- Individual section versions (S1-S5) may increment independently
- Major framework changes require master document version update

### 10.3 Change Process

**Standard Changes:**
1. Change request submitted to Policy Owner (CISO / Application Security Manager)
2. Impact assessment (affected stakeholders, systems, processes)
3. Stakeholder consultation (Development, Security, Architecture, Legal)
4. Draft revision prepared
5. Review and approval by CISO and required stakeholders
6. Communication plan executed (training updates, developer portal)
7. Implementation tracking (30/60/90 day checkpoints)

**Emergency Changes:**
- Critical security threats or regulatory deadlines may require expedited process
- Emergency approval by CISO with retrospective stakeholder review
- Documentation of justification for emergency process
- Minimum 48-hour notification to all developers

### 10.4 Communication

**Policy Updates Communicated Via:**
- Developer portal (central documentation repository)
- Email notifications to all developers
- Security training updates
- Team meetings (Security Team, Development Teams, Architecture Review Board)
- Quarterly CISO briefings to Executive Management
- Slack/Teams channels (security announcements)

---

## 11. Reference Documents

### 11.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.8.28 (this document) + Sections S1 through S5.D (See Section 2)

**Assessment Layer:**
- ISMS-IMP-A.8.28.1 – SDLC Assessment (Markdown + Excel)
- ISMS-IMP-A.8.28.2 – Standards & Tools Assessment (Markdown + Excel)
- ISMS-IMP-A.8.28.3 – Code Review & Testing Assessment (Markdown + Excel)
- ISMS-IMP-A.8.28.4 – Third-Party & OSS Assessment (Markdown + Excel)
- ISMS-IMP-A.8.28.5 – Compliance Dashboard (Markdown + Excel)

**Automation Layer:**
- Generator Scripts (5 Python files)
- Validation Script (excel_sanity_check_a828.py)

**Related ISMS Policies:**
- ISMS-POL-00 – Regulatory Applicability Framework
- ISMS-POL-A.8.25 – Secure Development Lifecycle (if separate)
- ISMS-POL-A.8.26 – Application Security Requirements
- ISMS-POL-A.8.27 – Secure System Architecture
- ISMS-POL-A.8.29 – Security Testing in Development/Acceptance
- ISMS-POL-A.5.8 – Information Security in Project Management
- ISMS Incident Management Procedure
- ISMS Change Management Policy
- ISMS Asset Management Policy

### 11.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 – Information Security Management Systems
- ISO/IEC 27002:2022 – Information Security Controls (Control 8.28 guidance)
- ISO/IEC 27034 – Application Security (all parts)
- ISO/IEC 27005:2022 – Information Security Risk Management

**Regulatory:**
- Swiss Federal Act on Data Protection (FADP/nDSG)
- EU General Data Protection Regulation (GDPR) – where applicable
- Industry-specific regulations (as applicable to organization)

**Framework Alignment:**
- NIST SP 800-218 – Secure Software Development Framework (SSDF)
- NIST SP 800-53 Rev. 5 – Security and Privacy Controls
- OWASP ASVS – Application Security Verification Standard
- OWASP SAMM – Software Assurance Maturity Model
- CIS Controls Version 8

**Technical References:**
- OWASP Top 10 (2021) – Web Application Security Risks
- OWASP Mobile Top 10 – Mobile Application Security Risks
- OWASP API Security Top 10 – API Security Risks
- CWE Top 25 – Most Dangerous Software Weaknesses
- SANS Top 25 – Most Dangerous Software Errors
- MITRE ATT&CK Framework – Adversarial Tactics and Techniques
- SEI CERT Coding Standards (C, C++, Java, Perl, Android)

---

## Appendix A: Philosophy & Methodology

### A.1 Evidence Over Theater

> "The first principle is that you must not fool yourself—and you are the easiest person to fool."  
*— Richard Feynman, Nobel Prize-winning physicist*

This framework is designed to prevent **cargo cult compliance** – the practice of implementing security controls that appear legitimate but provide no genuine protection. Saying "we do secure coding" without knowing what standards are followed, what testing is performed, and whether vulnerabilities are actually prevented is self-deception.

**The assessment workbooks force specificity:**
- **What** secure coding standards are followed? (documented and evidenced)
- **Where** in the SDLC are security controls applied? (process mapped and verified)
- **How** effective are the controls? (metrics, vulnerability trends, incidents)
- **Proof** of implementation? (SAST reports, code reviews, test results, training records)

If these questions cannot be answered with quantitative evidence, the organization does not have secure coding – it has secure coding theater.

### A.2 System Engineering Approach

This framework applies **engineering discipline** to security governance:

**Traditional Compliance:**
- Policy documents describe ideal state
- Auditors ask questions, check boxes
- Actual implementation state unknown until incident occurs
- Gap analysis is subjective and incomplete
- Developers confused about requirements

**System Engineering Compliance:**
- Policy documents define measurable requirements
- Python scripts generate standardized assessment workbooks
- Stakeholders document actual implementation with evidence
- Validation scripts ensure data quality and completeness
- Dashboard aggregates quantitative compliance metrics
- Gap analysis is objective, prioritized, and actionable
- Developers have clear, actionable standards

**Benefits:**
- Repeatable assessments (run quarterly, compare trends)
- Maintainable over time (scripts, not manual documents)
- Audit-ready from day one (structured evidence, clear metrics)
- Stakeholder efficiency (fill yellow cells, not create documents from scratch)
- Developer clarity (clear standards, not vague guidance)

### A.3 Vendor Agnostic by Design

This framework deliberately avoids naming specific products, tools, or vendors in policy documents. Organizations may use:
- **Languages:** Java, C#, Python, JavaScript, Go, C/C++, Ruby, PHP, Swift, etc.
- **SAST Tools:** SonarQube, Checkmarx, Veracode, Fortify, Snyk Code, etc.
- **DAST Tools:** OWASP ZAP, Burp Suite, Acunetix, Netsparker, etc.
- **SCA Tools:** Snyk, Black Duck, WhiteSource, Dependabot, etc.
- **IDEs:** IntelliJ IDEA, Visual Studio, VS Code, Eclipse, PyCharm, etc.

**The policy defines capabilities, not brands:**
- "Organizations SHALL implement static code analysis capable of detecting OWASP Top 10 vulnerabilities" ✅
- "Organizations SHALL deploy Checkmarx SAST" ❌

This ensures policy longevity and organizational flexibility while maintaining compliance rigor.

### A.4 Practical Security, Not Perfection

> "Perfect security is the enemy of good security."

This framework recognizes that:
- **Not all code requires the same security rigor** (risk-based approach)
- **Legacy systems may have technical debt** (exception management)
- **Business needs sometimes require pragmatic decisions** (with compensating controls)
- **Developers are not security experts** (provide clear, actionable guidance)
- **Security must enable, not block, business** (balance security with velocity)

**The goal is continuous improvement, not perfection:**
- Establish baseline (where are we?)
- Set realistic targets (where should we be?)
- Track progress (are we improving?)
- Adjust approach (what's working, what's not?)
- Iterate quarterly (small improvements compound over time)

---

**END OF MASTER DOCUMENT**