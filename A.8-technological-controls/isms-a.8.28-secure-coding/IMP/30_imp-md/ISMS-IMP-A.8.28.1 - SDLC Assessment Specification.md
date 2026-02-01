**ISMS-IMP-A.8.28.1 - SDLC Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.1 |
| **Version** | 1.0 |
| **Assessment Area** | Secure Development Lifecycle (SDLC) Integration |
| **Related Policy** | ISMS-POL-A.8.28 Section 2.1 (Pre-Development Requirements), Section 3.1 (Roles & Responsibilities) |
| **Purpose** | Evaluate integration of security practices into SDLC, focusing on pre-development activities and process-level controls that prevent vulnerabilities |
| **Target Audience** | Application Security Lead, Development Managers, Security Architects, Project Managers, Auditors |
| **Assessment Type** | Process & Organizational |
| **Review Cycle** | Quarterly or After Major SDLC Changes |
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

- **Part I:** Assessment users (Application Security Lead, Development Managers, Security Architects, Project Managers)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** Application Security Lead, Development Managers, Security Architects, Project Managers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.28.1 - SDLC Assessment

### What This Assessment Evaluates

This assessment evaluates the **integration of security practices into the Software Development Lifecycle (SDLC)**. The focus is on pre-development activities and process-level controls that prevent vulnerabilities from being introduced into code.

*"An ounce of prevention is worth a pound of cure."* - Benjamin Franklin

**Application to Secure Coding**: Security activities performed before code is written are 10-100x more cost-effective than fixing vulnerabilities post-deployment. This assessment verifies that [Organization] has systematic processes to prevent vulnerabilities rather than relying on reactive patching.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.28: Secure Coding
- ISMS-POL-A.8.28 Section 2.1: Pre-Development Requirements
- ISMS-POL-A.8.28 Section 3.1: Roles & Responsibilities (Development Managers, Security Architects, Security Champions)


Organizations that integrate security into SDLC reduce:

- Post-deployment vulnerability remediation costs by 60-90%
- Security incident frequency by 40-70%
- Time-to-market delays from late-stage security fixes


Organizations without SDLC security integration experience:

- Reactive "security theater" - finding and fixing issues too late
- Developer frustration from last-minute security blockers
- Higher overall security costs (fixing vs. preventing)


### What You'll Document

This assessment captures your ACTUAL practices (not aspirational):

1. **Security Requirements Definition**: How security requirements are identified, documented, and approved for projects
2. **Threat Modeling**: When and how threat modeling is performed, who participates, quality of outputs
3. **Secure Architecture & Design**: Architecture review processes, security-by-design principles applied
4. **Developer Training**: Training completion rates, curriculum effectiveness, Security Champions program
5. **Development Environment Security**: Workstation security, repository controls, CI/CD security
6. **Security Planning**: Integration of security activities into project planning and resource allocation

### Key Principle

**Evidence-Based Assessment**: If you can't demonstrate it with evidence, it doesn't count. This assessment requires:

- Documentation (process descriptions, templates, completed artifacts)
- Records (training completion, review approvals, tool configurations)
- Metrics (coverage percentages, completion rates, effectiveness measurements)


*"The first principle is that you must not fool yourself—and you are the easiest person to fool." - Richard Feynman*

**Application**: Claiming "we do threat modeling" without documented threat models = not compliant. Claiming "developers are trained" without LMS records = not compliant.

### Who Should Complete This Assessment

**Primary Role**: Application Security Lead (coordinates assessment, provides security perspective)

**Required Collaborators**:

- **Development Managers**: Training records, project planning, team practices
- **Security Architects**: Threat modeling, architecture reviews
- **DevOps/Platform Engineers**: Development environment configuration, CI/CD security
- **HR/Training Coordinator**: Training records, LMS data
- **Project Managers**: Security activity integration in project plans


**Time Commitment**: 12-16 hours total (distributed across 2-3 weeks)

- Information gathering: 6-8 hours
- Assessment completion: 4-6 hours
- Evidence collection: 2-3 hours
- Review and approval: 1-2 hours


### Expected Outputs

**Primary Output**: Excel workbook `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`

**Contents**:

- 6 assessment domain sheets (yellow cells completed with status and evidence)
- Summary Dashboard (auto-calculated compliance metrics)
- Evidence Register (documentation links and descriptions)
- Gap Analysis (non-compliant items with remediation plans)
- Approval Sign-Off (stakeholder approvals)


**Deliverables**:

- Completed Excel workbook
- Supporting evidence (uploaded to shared drive or document management system)
- Gap remediation plan with assigned owners and deadlines
- Executive summary (1-page for CISO/management)


---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

**Security Requirements Documentation**:

- [ ] Project initiation templates showing security requirements sections
- [ ] Completed security requirements documents (recent 3-6 projects)
- [ ] Security risk assessment documentation with approval signatures
- [ ] Security acceptance criteria in user stories/requirements
- [ ] Compliance mapping documents (GDPR, PCI-DSS, sector-specific)


**Threat Modeling Artifacts**:

- [ ] Threat modeling methodology documentation (STRIDE, PASTA, Attack Trees)
- [ ] Completed threat models (recent high-risk projects, minimum 3 examples)
- [ ] Architecture diagrams with trust boundaries
- [ ] Threat prioritization and risk ratings
- [ ] Security team review approvals
- [ ] Mitigation strategy documentation


**Architecture Review Documentation**:

- [ ] Architecture review process description
- [ ] Architecture security review checklists
- [ ] Security-by-design principles document
- [ ] Completed architecture diagrams with security controls
- [ ] Architecture review meeting minutes and decisions
- [ ] Security Architect sign-offs


**Training Records**:

- [ ] Developer security training curriculum (course descriptions, syllabi)
- [ ] Training completion records from LMS (last 12 months)
- [ ] Training certificates or attendance logs
- [ ] Security Champions program documentation
- [ ] Language-specific training materials
- [ ] Training effectiveness metrics (if available)


**Development Environment Configuration**:

- [ ] Endpoint security policy and configuration baselines
- [ ] Repository access control configuration (GitHub, GitLab, Bitbucket)
- [ ] MFA enforcement evidence
- [ ] Branch protection rules documentation
- [ ] Pre-commit hook configurations (secret detection)
- [ ] CI/CD pipeline security gate configuration
- [ ] SAST/DAST/SCA tool integration evidence
- [ ] Test data handling procedures


**Project Planning Documentation**:

- [ ] Project plan templates with security activities
- [ ] Sprint planning artifacts showing security stories
- [ ] "Definition of Done" including security criteria
- [ ] Application Security Team engagement logs
- [ ] Budget allocations for security tools and training
- [ ] Security milestone tracking (if available)


## Required Tools

**Software**:

- Microsoft Excel 2016+ or compatible spreadsheet application
- Access to [Organization]'s Learning Management System (LMS)
- Access to source code repository (GitHub, GitLab, Bitbucket, etc.)
- Access to project management tools (Jira, Azure DevOps, etc.)
- Access to document management system (SharePoint, Confluence, Google Drive, etc.)


**Access Permissions**:

- Training records (read access to LMS)
- Repository configurations (read access to admin settings)
- CI/CD pipeline configurations (read access to Jenkins, GitHub Actions, GitLab CI, etc.)
- Project documentation (read access to project folders)
- Budget/resource allocation data (if available)


**Optional Tools** (helpful but not required):

- Screenshot tool (for capturing evidence)
- PDF export tool (for saving evidence)


## Required Skills

**Assessor should have**:

- Understanding of SDLC methodologies (Agile, Waterfall, DevOps)
- Familiarity with secure coding principles (OWASP Top 10 awareness)
- Basic understanding of threat modeling concepts
- Ability to review and interpret process documentation
- Ability to interpret training records and calculate completion rates


**Assessor does NOT need**:

- Deep coding expertise (this is process assessment, not code review)
- Security tool expert-level knowledge
- Architecture design expertise


## Dependencies

**Must Complete BEFORE This Assessment**:

- ISMS-POL-A.8.28 (Secure Coding Policy) approved and published


**Should Have But Not Blocking**:

- Security Champions identified (at least partially)
- SAST/DAST/SCA tools deployed (even if not fully operational)


**Related Assessments** (coordinate timing):

- ISMS-IMP-A.8.28.2 (Standards & Tools) - can be done in parallel
- ISMS-IMP-A.8.28.3 (Code Review & Testing) - can be done in parallel
- ISMS-IMP-A.8.28.4 (Third-Party & OSS) - can be done in parallel
- ISMS-IMP-A.8.28.5 (Compliance Dashboard) - requires IMPs 1-4 completed first


---

# Assessment Workflow

## Step-by-Step Process

**Phase 1: Preparation (Week 1, Days 1-2)**

**Step 1**: Generate Excel workbook

- Run Python script: `python3 generate_a828_1_sdlc_assessment.py`
- Output: `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`
- Save to shared location for collaboration


**Step 2**: Review Instructions sheet

- Read assessment methodology
- Understand status definitions (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / 🔄 Planned / N/A)
- Review compliance scoring approach
- Understand evidence requirements


**Step 3**: Schedule stakeholder meetings

- Development Managers (1 hour): Training, planning, team practices
- Security Architects (1 hour): Threat modeling, architecture reviews
- DevOps/Platform Engineers (30 min): Environment security, CI/CD
- HR/Training (30 min): Training records extraction


**Phase 2: Information Gathering (Week 1-2, Days 3-10)**

**Step 4**: Collect Security Requirements Documentation

- Navigate to project documentation repositories
- Extract recent security requirements documents (3-6 projects)
- Identify security risk assessments with approval signatures
- Document compliance mapping artifacts
- Take screenshots or export PDFs as evidence
- Upload to Evidence Register sheet


**Step 5**: Collect Threat Modeling Artifacts

- Identify high-risk projects requiring threat models
- Gather completed threat model documents
- Collect architecture diagrams with trust boundaries
- Extract threat prioritization and risk ratings
- Verify Security Architect review approvals
- Document mitigation strategies


**Step 6**: Collect Architecture Review Evidence

- Review architecture review process documentation
- Gather security-by-design principles document
- Collect architecture diagrams showing security controls
- Extract architecture review meeting minutes
- Verify Security Architect sign-offs


**Step 7**: Collect Training Records

- Access LMS and export developer training completion reports
- Calculate completion rates (initial training, annual refresher)
- Identify language-specific training availability
- Document Security Champions program structure
- Calculate Security Champion:Developer ratio


**Step 8**: Collect Development Environment Configuration

- Access repository admin settings (GitHub, GitLab, Bitbucket)
- Document MFA enforcement status
- Export branch protection rules
- Review pre-commit hook configurations
- Document CI/CD security gate configuration
- Collect SAST/DAST/SCA tool integration evidence


**Step 9**: Collect Project Planning Documentation

- Review project plan templates
- Extract sprint planning artifacts with security stories
- Review "Definition of Done" criteria
- Document Application Security Team engagement
- Identify security budget allocations


**Phase 3: Assessment Completion (Week 2-3, Days 11-15)**

**Step 10**: Complete Domain 1: Security Requirements

- For each assessment question, select status from dropdown
- Provide justification in Comments column
- Link evidence in Evidence ID column
- Calculate percentage of projects with security requirements


**Step 11**: Complete Domain 2: Threat Modeling

- Document threat modeling methodology
- Calculate percentage of high-risk projects with threat models
- Assess threat model quality and completeness
- Verify Security Architect review process


**Step 12**: Complete Domain 3: Architecture & Design

- Document architecture review process
- Assess security-by-design principle application
- Verify Security Architect participation
- Calculate architecture review coverage


**Step 13**: Complete Domain 4: Training

- Calculate training completion rates
- Assess curriculum comprehensiveness
- Document Security Champions program maturity
- Verify training record retention


**Step 14**: Complete Domain 5: Development Environment

- Assess workstation security baseline compliance
- Document repository access controls
- Verify branch protection enforcement
- Assess CI/CD pipeline security integration


**Step 15**: Complete Domain 6: Security Planning

- Assess security activity integration in project plans
- Verify security story inclusion in sprint backlogs
- Document Application Security Team engagement model
- Assess security resource allocation


**Phase 4: Review and Finalization (Week 3, Days 16-18)**

**Step 16**: Complete Evidence Register

- For each evidence item, provide:
  - Evidence ID (auto-generated)
  - Description (what it proves)
  - Location (file path, URL, document ID)
  - Date collected
  - Collected by


**Step 17**: Review Gap Analysis Sheet

- Verify all ❌ Non-Compliant and ⚠️ Partial items appear
- Assign remediation owners
- Set remediation target dates
- Prioritize gaps (Critical / High / Medium / Low)


**Step 18**: Review Summary Dashboard

- Verify compliance percentages calculated correctly
- Review overall compliance rate
- Identify top gaps requiring attention
- Prepare executive summary


**Step 19**: Internal Review

- Share workbook with Development Managers for validation
- Share with Security Architects for technical accuracy
- Incorporate feedback and corrections


**Step 20**: Approval Process

- Submit to Application Security Lead for review
- Submit to CISO for approval
- Obtain Development Management approval
- Complete Approval Sign-Off sheet


## Timeline Expectations

**Total Duration**: 2-3 weeks (part-time effort)

**Effort Distribution**:

- Preparation: 2 hours
- Information gathering: 6-8 hours (distributed over 1-2 weeks)
- Assessment completion: 4-6 hours
- Evidence collection: 2-3 hours
- Review and finalization: 1-2 hours
- Approval cycle: 3-5 business days


**Critical Path**:

- Training records extraction (may require HR support - plan ahead)
- Threat modeling artifact gathering (may require searching multiple project repositories)
- Repository configuration review (may require admin access provisioning)


## Collaboration Requirements

**Weekly Sync Meeting** (30 minutes):

- Application Security Lead (assessment owner)
- Development Manager representative
- Security Architect (if available)
- Review progress, blockers, questions


**Ad-Hoc Consultations**:

- Development Managers: Training practices, project planning
- Security Architects: Threat modeling quality assessment
- DevOps: CI/CD security configuration
- HR: Training record extraction and interpretation


---

# Question-by-Question Guidance

This section provides detailed guidance for completing each assessment domain. For each question, you'll find:

- **What the question asks** (objective)
- **Where to find evidence** (typical locations)
- **How to answer** (Yes/No/Partial/Planned/N/A criteria)
- **Examples** (compliant vs. non-compliant states)
- **Policy reference** (ISMS-POL-A.8.28 section)


## Domain 1: Security Requirements Definition

**Assessment Question 1.1**: "Are security requirements documented for all new development projects?"

**What This Asks**: Does [Organization] have a systematic process for identifying and documenting security requirements during project initiation?

**Where to Find Evidence**:

- Project initiation templates
- Requirements documents for recent projects (last 6 months)
- Project management tool (Jira, Azure DevOps) - look for security-labeled requirements
- Product backlog - security user stories


**How to Answer**:

- **✅ Compliant**: 100% of new projects (last 6 months) have documented security requirements in project plans or requirements documents
- **⚠️ Partial**: 50-99% of projects have security requirements documented
- **❌ Non-Compliant**: <50% of projects have security requirements, or no systematic process
- **🔄 Planned**: Process being developed, not yet operational
- **N/A**: [Organization] has no new development projects (rare - justify in comments)


**Examples**:

- ✅ **Compliant**: Project "Customer Portal v2" has dedicated security requirements section with 12 documented requirements covering authentication, authorization, data protection, logging
- ❌ **Non-Compliant**: Project "Mobile App" launched without documented security requirements; security issues discovered in production


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.1 (Security Requirements Definition)

---

**Assessment Question 1.2**: "Are security risk assessments conducted for high-risk projects before development begins?"

**What This Asks**: Does [Organization] identify security risks and document threat severity/likelihood before coding starts?

**Where to Find Evidence**:

- Risk assessment documents (often separate from requirements docs)
- Threat model documents (may serve as risk assessment)
- CISO/Security Architect approval signatures
- Risk register entries for projects


**How to Answer**:

- **✅ Compliant**: 100% of high-risk projects (those handling PII, financial data, or critical business functions) have completed security risk assessments with CISO/Security approval
- **⚠️ Partial**: Most high-risk projects assessed, but some gaps (70-99% coverage)
- **❌ Non-Compliant**: <70% of high-risk projects assessed, or no risk assessment process
- **🔄 Planned**: Risk assessment template created, not yet applied to projects
- **N/A**: [Organization] has no high-risk projects (justify - unlikely)


**Examples**:

- ✅ **Compliant**: "Payment Gateway Integration" project has risk assessment dated 15.03.2025, identifying PCI-DSS compliance risk (High), data breach risk (Critical), approved by CISO
- ❌ **Non-Compliant**: "Admin Dashboard" project (high-risk - privileged access) proceeded without risk assessment; discovered authorization bypass in testing


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.1 (Security Requirements Definition - risk assessment required)

---

**Assessment Question 1.3**: "Are security acceptance criteria defined before development begins?"

**What This Asks**: Are testable security criteria documented that determine when a feature is "done" from a security perspective?

**Where to Find Evidence**:

- User stories with "Acceptance Criteria" sections
- Requirements documents with "Security Acceptance Criteria" sections
- "Definition of Done" checklists including security criteria


**How to Answer**:

- **✅ Compliant**: 90%+ of user stories/requirements have security acceptance criteria defined before implementation
- **⚠️ Partial**: 50-89% have security acceptance criteria
- **❌ Non-Compliant**: <50% have criteria, or criteria are vague ("must be secure")
- **🔄 Planned**: Template updated to include security acceptance criteria, not yet applied
- **N/A**: Not applicable (justify)


**Examples**:

- ✅ **Compliant**: User story "User Registration" has acceptance criteria: "Password must be hashed with bcrypt (cost 12), MFA enrollment prompted, session token HttpOnly/Secure"
- ❌ **Non-Compliant**: Feature "File Upload" has vague criterion "must be secure" without specifics (file type validation? size limits? malware scanning?)


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.1 (Security acceptance criteria required)

---

**Assessment Question 1.4**: "Are regulatory compliance requirements identified and documented for projects?"

**What This Asks**: Does [Organization] identify applicable regulations (GDPR, PCI-DSS, HIPAA, sector-specific) and document compliance obligations?

**Where to Find Evidence**:

- Compliance mapping documents
- Requirements documents with "Regulatory Compliance" sections
- Legal/Compliance team review approvals
- Data classification documentation


**How to Answer**:

- **✅ Compliant**: 100% of projects processing regulated data types (PII, financial, health) have documented compliance requirements with Legal/Compliance review
- **⚠️ Partial**: Most projects documented, but some gaps (70-99%)
- **❌ Non-Compliant**: <70% documented, or no compliance identification process
- **🔄 Planned**: Compliance mapping template created, not yet applied
- **N/A**: [Organization] has no projects processing regulated data (justify - unlikely)


**Examples**:

- ✅ **Compliant**: "Customer CRM" project documented GDPR Article 25 (data protection by design), Article 32 (security of processing), approved by Legal
- ❌ **Non-Compliant**: "Marketing Analytics" project collected PII without GDPR compliance documentation; discovered during data protection audit


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.1 (Regulatory alignment required), ISMS-POL-A.8.28 Section 1.5 (Regulatory Applicability Framework)

---

## Domain 2: Threat Modeling

**Assessment Question 2.1**: "Is threat modeling performed for high-risk applications?"

**What This Asks**: Does [Organization] systematically identify threats during design phase for applications handling sensitive data or critical functions?

**Where to Find Evidence**:

- Completed threat model documents
- Architecture diagrams with trust boundaries
- Threat identification and prioritization lists
- Security Architect review approvals


**How to Answer**:

- **✅ Compliant**: 100% of high-risk applications (PII, financial, critical business functions) have completed threat models
- **⚠️ Partial**: 70-99% of high-risk applications have threat models
- **❌ Non-Compliant**: <70% have threat models, or no threat modeling process
- **🔄 Planned**: Threat modeling methodology selected, training scheduled, not yet applied
- **N/A**: [Organization] has no high-risk applications (justify - rare)


**Examples**:

- ✅ **Compliant**: "Payment API" has threat model using STRIDE methodology, identifying 23 threats (8 High, 12 Medium, 3 Low), mitigation strategies documented
- ❌ **Non-Compliant**: "Admin Portal" (high-risk - privileged access) deployed without threat model; authorization bypass discovered in production


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.2 (Threat Modeling - required for high-risk apps)

---

**Assessment Question 2.2**: "Do threat models include system overview, threat identification, prioritization, and mitigation strategies?"

**What This Asks**: Are threat models comprehensive (not just diagrams), documenting threats and how they'll be addressed?

**Where to Find Evidence**:

- Threat model documents (check table of contents/sections)
- System overview/architecture diagrams
- Threat identification tables (threat, attack vector, impact)
- Mitigation strategy documentation


**How to Answer**:

- **✅ Compliant**: 90%+ of threat models include all required elements: system overview, threat ID, prioritization (CVSS or similar), mitigation strategies
- **⚠️ Partial**: 50-89% complete (some missing sections)
- **❌ Non-Compliant**: <50% complete, or threat models are just diagrams without analysis
- **🔄 Planned**: Threat model template created with required sections, not yet used
- **N/A**: No threat models exist (would be ❌ if high-risk apps exist)


**Examples**:

- ✅ **Compliant**: "API Gateway" threat model has: system diagram (5 components, 3 trust boundaries), 18 identified threats, CVSS scores, mitigation strategies (e.g., "SQL Injection mitigated by parameterized queries")
- ❌ **Non-Compliant**: "Mobile App" threat model is just architecture diagram with no threat identification or mitigation


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.2 (Threat model documentation requirements)

---

**Assessment Question 2.3**: "Are threat models reviewed and approved by Security Architects?"

**What This Asks**: Does a qualified security professional validate threat models for completeness and accuracy?

**Where to Find Evidence**:

- Security Architect approval signatures on threat model documents
- Review comments in threat model documents
- Meeting minutes from threat modeling sessions
- Email approvals (if documented)


**How to Answer**:

- **✅ Compliant**: 100% of threat models have Security Architect review and approval signature
- **⚠️ Partial**: 70-99% reviewed and approved
- **❌ Non-Compliant**: <70% reviewed, or no review process
- **🔄 Planned**: Review process defined, not yet implemented
- **N/A**: No Security Architect role exists AND no threat models (document both gaps)


**Examples**:

- ✅ **Compliant**: "Customer Portal" threat model has signature from Security Architect dated 22.04.2025 with comment "Reviewed - approved with condition: add rate limiting to login endpoint"
- ❌ **Non-Compliant**: "Data Warehouse" threat model created by development team, no security review; data exfiltration risk not identified


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.2 (Security Architect review required)

---

## Domain 3: Secure Architecture & Design

**Assessment Question 3.1**: "Are security-by-design principles documented and applied?"

**What This Asks**: Does [Organization] have documented principles (least privilege, defense in depth, fail securely, etc.) that architects reference?

**Where to Find Evidence**:

- Security-by-design principles document
- Architecture review checklists referencing principles
- Architecture decision records (ADRs) citing principles
- Training materials covering principles


**How to Answer**:

- **✅ Compliant**: Principles documented (at least 8 core principles from ISMS-POL-A.8.28 Section 2.1.3) AND 80%+ of architecture reviews reference them
- **⚠️ Partial**: Principles documented but inconsistently applied (50-79% reference rate)
- **❌ Non-Compliant**: Principles not documented OR rarely applied (<50%)
- **🔄 Planned**: Principles document drafted, not yet published/trained
- **N/A**: Not applicable (justify - unlikely)


**Examples**:

- ✅ **Compliant**: "Secure Architecture Principles v1.2" document defines 10 principles; "API Design Review" checklist references principles; "Microservices Architecture ADR" cites "Principle #3: Least Privilege" for service account design
- ❌ **Non-Compliant**: No documented principles; architects design ad-hoc; inconsistent security decisions across projects


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.3 (Secure Architecture and Design - principles required)

---

**Assessment Question 3.2**: "Are architecture security reviews conducted for new applications?"

**What This Asks**: Is there a systematic review process where security aspects of architecture are evaluated before implementation?

**Where to Find Evidence**:

- Architecture review process documentation
- Architecture review meeting minutes/notes
- Architecture review checklists
- Calendar invites for architecture review meetings
- Review approval records


**How to Answer**:

- **✅ Compliant**: 90%+ of new applications undergo architecture security review with documented outcomes
- **⚠️ Partial**: 50-89% undergo review
- **❌ Non-Compliant**: <50% undergo review, or no formal review process
- **🔄 Planned**: Review process defined, not yet operational
- **N/A**: [Organization] has no new applications (justify - rare)


**Examples**:

- ✅ **Compliant**: "Mobile Banking App" architecture reviewed 10.05.2025, participants: Security Architect, Lead Developer, Product Owner; outcome: "Approved with recommendations (implement certificate pinning, add biometric auth option)"
- ❌ **Non-Compliant**: "Partner Integration API" architecture not reviewed; discovered insecure OAuth implementation post-deployment


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.3 (Architecture review required)

---

## Domain 4: Developer Security Training

**Assessment Question 4.1**: "Do 100% of developers complete initial security training within 30 days of hire?"

**What This Asks**: Is security training part of developer onboarding process with completion tracked?

**Where to Find Evidence**:

- LMS training completion reports
- HR onboarding checklist
- Training certificates
- Email confirmations of training completion


**How to Answer**:

- **✅ Compliant**: 100% of developers hired in last 12 months completed initial security training within 30 days (verify in LMS)
- **⚠️ Partial**: 80-99% completed within 30 days
- **❌ Non-Compliant**: <80% completed, or no initial training requirement
- **🔄 Planned**: Training procured, onboarding process updated, not yet implemented
- **N/A**: No developers hired in last 12 months (verify with HR)


**Examples**:

- ✅ **Compliant**: LMS report shows 15 developers hired Jan-Dec 2025; all 15 completed "Secure Coding Fundamentals" (average: 18 days post-hire)
- ❌ **Non-Compliant**: 8 of 12 developers hired in 2025 never completed security training; 4 completed after 60+ days


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.4 (Developer training - initial within 30 days)

---

**Assessment Question 4.2**: "Do 90%+ of developers complete annual security refresher training?"

**What This Asks**: Is security knowledge reinforced annually through refresher training?

**Where to Find Evidence**:

- LMS training completion reports (filter: last 12 months)
- Training reminder emails
- Training completion certificates


**How to Answer**:

- **✅ Compliant**: 90%+ of active developers completed annual refresher in last 12 months
- **⚠️ Partial**: 70-89% completed refresher
- **❌ Non-Compliant**: <70% completed, or no annual refresher requirement
- **🔄 Planned**: Refresher training procured, not yet launched
- **N/A**: [Organization] was founded <12 months ago (no annual cycle yet)


**Examples**:

- ✅ **Compliant**: LMS report: 45 of 48 active developers (93.75%) completed "Security Refresher 2025"; 3 on extended leave
- ❌ **Non-Compliant**: 20 of 50 developers (40%) completed refresher; no follow-up enforcement


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.4 (Annual refresher training required)

---

## Domain 5: Development Environment Security

**Assessment Question 5.1**: "Is MFA enforced for all source code repository access?"

**What This Asks**: Can developers access code repositories (GitHub, GitLab, Bitbucket) without multi-factor authentication?

**Where to Find Evidence**:

- Repository admin settings screenshot (GitHub: Settings > Security > Authentication)
- MFA enforcement policy configuration
- User access audit logs showing MFA status
- IT/Security policy requiring MFA


**How to Answer**:

- **✅ Compliant**: MFA enforced at repository platform level (cannot be disabled by users), 100% of developer accounts have MFA enabled
- **⚠️ Partial**: MFA encouraged but not enforced (70-99% adoption)
- **❌ Non-Compliant**: MFA not enforced (<70% adoption) OR not available
- **🔄 Planned**: MFA enforcement scheduled, not yet active
- **N/A**: [Organization] has no source code repositories (justify - very rare)


**Examples**:

- ✅ **Compliant**: GitHub Enterprise settings show "Require two-factor authentication for everyone in the organization" enabled; user audit confirms 100% compliance
- ❌ **Non-Compliant**: GitLab allows password-only access; 35% of developers use MFA voluntarily; repository compromised via stolen password


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.5 (Development environment security - MFA required)

---

**Assessment Question 5.2**: "Are branch protection rules enforced requiring code review before merge?"

**What This Asks**: Can code be merged to protected branches (main, master, production) without peer review?

**Where to Find Evidence**:

- Branch protection rules configuration (GitHub: Settings > Branches)
- Pull request/merge request settings
- PR approval logs
- Policy documentation


**How to Answer**:

- **✅ Compliant**: Protected branches require at least 1 approval before merge; rules enforced (cannot be bypassed)
- **⚠️ Partial**: Rules exist but can be bypassed by admins, OR not all critical branches protected
- **❌ Non-Compliant**: No branch protection, or protection not enforced
- **🔄 Planned**: Branch protection rules drafted, not yet applied
- **N/A**: No version-controlled code (justify - extremely rare)


**Examples**:

- ✅ **Compliant**: GitHub branch protection on `main`: "Require pull request reviews before merging" (1 approval), "Dismiss stale approvals", "Include administrators" (no bypass)
- ❌ **Non-Compliant**: No branch protection; developers commit directly to `main`; introduced vulnerability bypassed review


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.5 (Code review enforcement)

---

## Domain 6: Security Planning & Resource Allocation

**Assessment Question 6.1**: "Are security activities included in project plans and timelines?"

**What This Asks**: Are security tasks (threat modeling, security testing, architecture review) scheduled and tracked like other project activities?

**Where to Find Evidence**:

- Project plan templates with security milestones
- Project schedules (Gantt charts, Jira roadmaps) showing security tasks
- Sprint planning notes with security stories
- Project status reports mentioning security activities


**How to Answer**:

- **✅ Compliant**: 90%+ of projects have security activities in project plans with dedicated time/resources
- **⚠️ Partial**: 50-89% of projects include security activities
- **❌ Non-Compliant**: <50% include security, or security activities are "fit in if time permits"
- **🔄 Planned**: Project planning templates updated to include security, not yet applied
- **N/A**: No projects (justify - rare)


**Examples**:

- ✅ **Compliant**: "E-commerce Platform" project plan includes: "Threat Modeling" (Week 3, 16 hours), "SAST Setup" (Week 5, 8 hours), "Penetration Test" (Week 14, 40 hours)
- ❌ **Non-Compliant**: "Internal Dashboard" project plan has no security tasks; DAST testing delayed launch by 2 weeks (unplanned)


**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.6 (Security planning and resource allocation)

---

## Interpreting Status Dropdown Options

For every assessment question, you'll select from these status options:

**✅ Compliant (Green)**:

- Control fully implemented
- Evidence available and verified
- Meets or exceeds policy requirements
- No remediation needed


**⚠️ Partial (Yellow)**:

- Control partially implemented
- Some evidence exists but gaps remain
- Remediation planned with realistic timeline
- Acceptable interim state with risk acceptance


**❌ Non-Compliant (Red)**:

- Control not implemented OR
- Implementation insufficient (<50% coverage) OR
- No evidence available
- Immediate remediation required


**🔄 Planned (Blue)**:

- Control implementation in progress
- Timeline and resources allocated
- Not yet operational
- Evidence: project plan, budget approval, tool procurement


**N/A (Gray)**:

- Control not applicable to [Organization]
- Must provide justification in Comments column
- Rare - most controls apply to all organizations


---

# Evidence Collection

## Evidence Types

**Documentation**:

- Process descriptions (how we do threat modeling)
- Templates (security requirements template, threat model template)
- Completed artifacts (filled-in threat models, requirements docs)
- Policies and standards
- Approval records (signatures, emails)


**Records**:

- Training completion reports (LMS exports)
- Access logs (MFA status, repository access)
- Configuration exports (branch protection rules, CI/CD configs)
- Tool reports (SAST scan results, SCA vulnerability reports)
- Meeting minutes (architecture reviews, threat modeling sessions)


**Metrics**:

- Coverage percentages (% projects with threat models)
- Completion rates (% developers trained)
- Compliance scores (% repositories with branch protection)
- Effectiveness measurements (vulnerability reduction trends)


## Where Evidence Typically Resides

| Evidence Type | Typical Location | Access Required |
|---------------|------------------|-----------------|
| **Security Requirements** | Project docs (SharePoint, Confluence, Google Drive) | Read access to project folders |
| **Threat Models** | Security shared drive, Confluence, project repos | Security team access |
| **Architecture Diagrams** | Technical documentation wikis, design docs | Developer access |
| **Training Records** | Learning Management System (LMS) | HR/Training admin OR manager access |
| **Repository Configs** | GitHub/GitLab/Bitbucket admin settings | Repository admin OR read-only admin access |
| **CI/CD Configs** | Jenkins, GitHub Actions, GitLab CI, Azure DevOps | DevOps access |
| **Project Plans** | Jira, Azure DevOps, MS Project, Asana | Project manager OR developer access |
| **Meeting Minutes** | Email, Calendar (meeting notes), Confluence | Participant access |

## How to Capture Evidence

**Screenshots**:

- Use snipping tool or screenshot utility
- Capture full context (include page title, date, URL if applicable)
- Annotate if needed (highlight relevant sections)
- Save with descriptive filename: `Evidence_5-2_BranchProtection_Main_20260124.png`


**Document Exports**:

- Export PDFs (not Word docs - PDFs are tamper-evident)
- Include metadata (creation date, author)
- Save with descriptive filename


**Spreadsheet/Report Exports**:

- Export from LMS, repository tools, CI/CD platforms
- Include column headers
- Include export date/time
- Save as CSV or Excel


**Email Evidence**:

- Forward approval emails to yourself
- Save as PDF (Print > Save as PDF)
- Or save .eml file


## Evidence Register Population

For each evidence item in the Evidence Register sheet:

**Evidence ID**: Auto-generated (EV-001, EV-002, etc.)

**Evidence Description**: Brief description of what this proves

- Example: "GitHub branch protection configuration for main branch requiring code review"


**Related Assessment Question**: Which question(s) this evidence supports

- Example: "5.2 Branch Protection Enforcement"


**Evidence Type**: Select from dropdown

- Document, Screenshot, Report, Configuration Export, Email, Meeting Minutes, Other


**Location**: Where evidence is stored

- Example: "/Security/Evidence/ISMS-A.8.28/BranchProtection_Main.png"
- Or: "Google Drive > ISMS Evidence > A.8.28 > Screenshot 2026-01-24.png"


**Date Collected**: Date evidence was captured

- Format: DD.MM.YYYY


**Collected By**: Name of person who captured evidence

- Example: "J. Smith, Application Security Lead"


## Evidence Quality Standards

**Good Evidence**:

- Objective (not subjective opinions)
- Time-stamped (date visible or metadata preserved)
- Attributable (who created, who approved)
- Sufficient to demonstrate compliance (auditor would accept)
- Maintained per retention policy (minimum: duration of SDLC)


**Poor Evidence**:

- Verbal claims without documentation
- Screenshots with no context (cropped too tightly, no date/URL)
- Draft documents (not approved versions)
- Expired evidence (training records from 3 years ago when annual required)


---

# Common Pitfalls

Learn from others' mistakes. Here are the 10 most common errors in SDLC assessments:

## Mistake 1: Documenting Aspirational State Instead of Current State

**Problem**: Marking "✅ Compliant" based on planned or desired state, not actual implementation.

**Example**: Marking "We do threat modeling" as Compliant because threat modeling template exists, but zero actual threat models completed.

**Solution**: Answer based on CURRENT REALITY. If implementation is in progress, mark "🔄 Planned". Provide evidence: completed artifacts, not just templates.

---

## Mistake 2: Marking "Yes" Without Evidence

**Problem**: Answering questions based on belief or memory without verifying evidence exists.

**Example**: Answering "Developers complete annual training" as Compliant without checking LMS records; actual completion rate is 55%.

**Solution**: Gather evidence FIRST, then answer questions. If you can't find evidence, it's ❌ Non-Compliant (or at best ⚠️ Partial if some evidence exists).

---

## Mistake 3: Confusing "Planned" with "Partial"

**Problem**: Using "🔄 Planned" when partial implementation exists.

**Example**: 3 of 10 high-risk projects have threat models; assessor marks "Planned". Correct: ⚠️ Partial (30% coverage).

**Solution**:

- **Planned** = Not yet started but resources allocated, timeline set
- **Partial** = Some implementation exists, working toward full coverage


---

## Mistake 4: Not Documenting Gap Remediation Timelines

**Problem**: Marking items ❌ Non-Compliant or ⚠️ Partial without remediation plans in Gap Analysis sheet.

**Example**: Repository MFA marked Non-Compliant, but no remediation plan; remains unaddressed for 6 months.

**Solution**: For every ❌ or ⚠️, complete Gap Analysis sheet: What's the gap? Who's responsible? When will it be fixed? What's the priority?

---

## Mistake 5: Skipping N/A Justifications

**Problem**: Marking questions N/A without explaining WHY they don't apply.

**Example**: "Threat modeling for high-risk apps" marked N/A; auditor questions whether [Organization] truly has zero high-risk applications.

**Solution**: If marking N/A, provide justification in Comments: "[Organization] develops only internal documentation tools; no PII, financial data, or critical business functions processed. Confirmed with CISO on DD.MM.YYYY."

---

## Mistake 6: Insufficient Threat Model Documentation

**Problem**: Counting architecture diagrams without threat analysis as "threat models".

**Example**: "API Gateway" has Visio diagram with 5 components; marked Compliant for threat modeling. Missing: threat identification, prioritization, mitigation.

**Solution**: Verify threat models include ALL required elements: system overview, threat identification, prioritization (CVSS/DREAD), mitigation strategies, approval. Diagram alone ≠ threat model.

---

## Mistake 7: Training Records Not Verified

**Problem**: Trusting developer self-reporting without checking LMS records.

**Example**: Development Manager says "everyone's trained"; LMS shows 60% completion.

**Solution**: Always verify training with LMS exports. Trust but verify.

---

## Mistake 8: Not Involving Development Managers in Assessment

**Problem**: Application Security Lead completes assessment without Development Manager input; answers questions inaccurately.

**Example**: Assessor marks "Security stories included in sprints" as Compliant; Development Manager clarifies: "Only if Security Champion flags them; not systematic."

**Solution**: Schedule stakeholder meetings (Dev Managers, Security Architects, DevOps). Validate answers before finalizing.

---

## Mistake 9: Assessing Only Pilot Projects, Not Organization-Wide Practices

**Problem**: Documenting security practices from single exemplary project; claiming organization-wide compliance.

**Example**: "Project A" has excellent threat model; assessor marks Compliant org-wide. Reality: Only Project A (1 of 20 projects) has threat model.

**Solution**: Calculate coverage percentages. Question asks "Are threat models performed?" Answer based on % of applicable projects (e.g., 1 of 20 high-risk projects = 5% = ❌ Non-Compliant).

---

## Mistake 10: Missing Approval Sign-Offs

**Problem**: Completing assessment but not obtaining required approvals; assessment not valid for audit.

**Example**: Assessment completed, Evidence Register populated, but Approval Sign-Off sheet blank. Auditor rejects assessment.

**Solution**: Follow approval workflow. Obtain signatures from Application Security Lead, Development Management, CISO. No shortcuts.

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


**Domain 1: Security Requirements**:

- [ ] Project count calculated (how many projects assessed)
- [ ] Percentage coverage calculated (% projects with security requirements)
- [ ] Recent projects evidence (last 6 months minimum)
- [ ] Compliance mapping documentation provided for regulated data


**Domain 2: Threat Modeling**:

- [ ] High-risk project count calculated
- [ ] Threat model coverage percentage calculated
- [ ] Sample threat models reviewed for completeness
- [ ] Security Architect approval verified


**Domain 3: Architecture & Design**:

- [ ] Security-by-design principles document referenced
- [ ] Architecture review process documented
- [ ] Architecture review coverage calculated


**Domain 4: Training**:

- [ ] LMS report obtained (last 12 months)
- [ ] Initial training completion rate calculated
- [ ] Annual refresher completion rate calculated
- [ ] Security Champions program maturity assessed


**Domain 5: Development Environment**:

- [ ] Repository configuration screenshots captured
- [ ] MFA enforcement verified
- [ ] Branch protection rules documented
- [ ] CI/CD security gate configuration verified


**Domain 6: Security Planning**:

- [ ] Project plan templates reviewed
- [ ] Sprint planning artifact examples provided
- [ ] Security activity integration coverage calculated


## Evidence Register

- [ ] All evidence items have descriptions
- [ ] All evidence items have locations (file path or URL)
- [ ] All evidence items have collection dates
- [ ] All evidence items have collector names
- [ ] Evidence physically exists at documented locations
- [ ] Evidence is accessible to auditors (permissions set correctly)


## Gap Analysis

- [ ] All ❌ Non-Compliant items appear in Gap Analysis sheet
- [ ] All ⚠️ Partial items appear in Gap Analysis sheet
- [ ] Gap descriptions clear and specific
- [ ] Remediation owners assigned (name, not role)
- [ ] Remediation target dates realistic
- [ ] Priority assigned (Critical/High/Medium/Low)
- [ ] Remediation status tracked (Not Started/In Progress/Completed)


## Summary Dashboard

- [ ] Overall compliance percentage calculated correctly
- [ ] Domain compliance percentages calculated correctly
- [ ] Formulas not broken (no #REF!, #VALUE! errors)
- [ ] Top gaps list populated
- [ ] Critical gaps count accurate


## Approval Sign-Off

- [ ] Completed By section filled (name, role, date, signature)
- [ ] Reviewed By section prepared (ready for Application Security Lead)
- [ ] Approved By section prepared (ready for CISO)
- [ ] Next Review Date calculated (+3 months from completion)


## File Quality

- [ ] Filename follows convention: `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`
- [ ] File saved to shared location (not local drive only)
- [ ] File permissions set (reviewers and approvers have access)
- [ ] Evidence files uploaded to evidence repository
- [ ] Evidence file naming consistent and descriptive


---

# Review & Approval

## Internal Review (Before Submission)

**Self-Review**:
1. Complete Quality Checklist (Section 7) - verify all items checked
2. Review Summary Dashboard - do numbers make sense?
3. Review Gap Analysis - are priorities realistic?
4. Spot-check evidence links - do they work?

**Peer Review** (Optional but Recommended):
1. Share workbook with Security Champion or peer
2. Request 30-minute review meeting
3. Walk through domain assessments
4. Incorporate feedback

**Stakeholder Validation**:
1. Share relevant sections with Development Managers

   - Domain 4 (Training) - verify completion rates accurate
   - Domain 6 (Planning) - verify security integration claims

2. Share with Security Architects

   - Domain 2 (Threat Modeling) - verify quality assessment
   - Domain 3 (Architecture) - verify review process accuracy

3. Incorporate feedback and corrections

## Formal Approval Workflow

**Step 1: Submit to Application Security Lead**

**When**: After internal review complete  
**How**: Email workbook with subject "ISMS-IMP-A.8.28.1 SDLC Assessment - Review Requested"  
**Timeline**: Application Security Lead reviews within 5 business days  

**Application Security Lead Reviews**:

- Technical accuracy (security practices correctly assessed)
- Evidence sufficiency (claims supported by evidence)
- Gap remediation plans (realistic and prioritized)
- Compliance with policy (ISMS-POL-A.8.28 requirements met)


**Possible Outcomes**:

- **Approve**: No changes needed, proceed to CISO approval
- **Approve with Minor Revisions**: Clarifications needed, can proceed in parallel with CISO review
- **Return for Revision**: Significant issues, re-submit after corrections


---

**Step 2: Submit to Development Management (CTO/VP Engineering)**

**When**: After Application Security Lead approval  
**How**: Email workbook with executive summary (1 page)  
**Timeline**: Development Management reviews within 5 business days  

**Development Management Reviews**:

- Operational feasibility (remediation plans realistic for dev teams)
- Resource allocation (budgets and timelines align with capacity)
- Organizational accuracy (training and planning claims correct)


**Possible Outcomes**: Same as Application Security Lead review

---

**Step 3: Submit to CISO**

**When**: After Application Security Lead AND Development Management approval  
**How**: Email workbook + executive summary + risk summary  
**Timeline**: CISO reviews within 5 business days  

**CISO Reviews**:

- Risk posture (gaps acceptable or require escalation)
- Compliance status (audit readiness)
- Strategic alignment (security initiatives aligned with business)
- Residual risk acceptance (Non-Compliant items with long remediation timelines)


**Possible Outcomes**:

- **Approve**: Assessment complete, publish results
- **Approve with Conditions**: Specific gap remediation acceleration required
- **Reject**: Insufficient evidence or critical gaps not addressed


---

## Approval Timeline

**Total Approval Cycle**: 10-15 business days

| Step | Duration | Cumulative |
|------|----------|------------|
| Self-review & stakeholder validation | 3-5 days | 3-5 days |
| Application Security Lead review | 5 days | 8-10 days |
| Development Management review | 5 days | 13-15 days |
| CISO review | 5 days | 18-20 days |

**Parallel processing possible**: Application Security Lead and Development Management reviews can occur simultaneously (saves 5 days).

**Expedited review**: For urgent assessments (audit deadline), request expedited review (2-3 days per step).

---

## Post-Approval Actions

**Publication**:
1. Save approved workbook to ISMS document repository
2. Update ISMS assessment register (assessment complete, date, compliance rate)
3. Publish executive summary to management portal

**Communication**:
1. Email summary to Development Managers
2. Present results to Security Champions (15-minute standup)
3. Add to CISO monthly report

**Remediation Tracking**:
1. Create tickets for each gap in Gap Analysis (Jira, Azure DevOps, ServiceNow)
2. Assign owners and due dates
3. Add to Security Team backlog for tracking
4. Schedule 30-day, 60-day, 90-day follow-ups

**Schedule Next Assessment**:
1. Calendar reminder for next quarterly assessment (+3 months)
2. Assign owner for next assessment cycle

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers (Python/Excel script maintainers)

---

# Excel Workbook Structure

## Sheet Overview

The SDLC Assessment workbook consists of 10 sheets:

| Sheet # | Sheet Name | Purpose | Input Type |
|---------|------------|---------|------------|
| 1 | Instructions | Assessment guidance and methodology | Read-only |
| 2 | Security_Requirements_Design | Security requirements and secure design assessment | User input (yellow cells) |
| 3 | Development_Environment | Development environment security controls | User input (yellow cells) |
| 4 | Build_Deployment_Pipeline | Build and deployment pipeline security | User input (yellow cells) |
| 5 | Security_Testing_Integration | Security testing integration assessment | User input (yellow cells) |
| 6 | Release_Change_Management | Release and change management security | User input (yellow cells) |
| 7 | Summary_Dashboard | Executive overview and compliance metrics | Auto-calculated |
| 8 | Evidence_Register | Supporting documentation tracking | User input (yellow cells) |
| 9 | Gap_Analysis | Non-compliant items and remediation plan | Auto-populated + user input |
| 10 | Approval_Sign_Off | Formal approval workflow | User input (yellow cells) |

## Common Column Structure (Assessment Sheets 2-6)

All assessment sheets use consistent column structure:

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | # | 5 | Question number | Auto-number |
| B | Domain | 15 | Domain/category name | Text |
| C | Assessment Question | 60 | Question text | Wrapped text |
| D | Policy Reference | 20 | ISMS-POL-A.8.28 section | Text |
| E | Status | 15 | Compliance status | Dropdown |
| F | Comments/Justification | 40 | Explanation for status | Wrapped text, yellow fill |
| G | Evidence ID | 15 | Reference to Evidence Register | Text, yellow fill |
| H | Gap Priority | 15 | Priority if Non-Compliant | Dropdown |
| I | Remediation Owner | 20 | Person responsible for fixing | Text, yellow fill |
| J | Target Date | 12 | Remediation deadline | Date picker, yellow fill |

**Total columns per assessment sheet**: 10 (A-J)

---

# Sheet 1: Instructions

## Header Section

**Row 1**: Title row

- Cell A1: "ISMS-IMP-A.8.28.1 – SDLC Assessment"
- Font: Calibri 16pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center
- Height: 40px
- Merge: A1:J1


**Row 2**: Subtitle row

- Cell A2: "ISO/IEC 27001:2022 - Control A.8.28: Secure Coding"
- Font: Calibri 12pt white
- Fill: #4472C4 (medium blue)
- Alignment: Center
- Merge: A2:J2


## Document Information Block (Rows 4-14)

```
Assessment Document:        ISMS-IMP-A.8.28.1 - SDLC Assessment
Assessment Area:            Secure Development Lifecycle Integration
Related Policy:             ISMS-POL-A.8.28 Section 2.1, Section 3.1
Version:                    1.0
Date:                       24.01.2026
Assessment Period:          [USER INPUT - yellow cell]
Completed By:               [USER INPUT - yellow cell]
Organization:               [USER INPUT - yellow cell]
Review Cycle:               Quarterly
Next Review Date:           [Auto-calc: +3 months from completion]
```

## Instructions Content (Rows 16+)

**Section**: How to Use This Workbook

- Step-by-step assessment instructions
- Reference to PART I: USER COMPLETION GUIDE for detailed guidance


**Section**: Status Legend

- ✅ Compliant (Green): Control fully implemented, evidence verified
- ⚠️ Partial (Yellow): Control partially implemented, gaps identified
- ❌ Non-Compliant (Red): Control not implemented or insufficient
- 🔄 Planned (Blue): Implementation in progress, timeline set
- N/A (Gray): Not applicable (with justification required)


**Section**: Evidence Requirements

- Documentation types accepted
- Where to upload evidence
- Evidence naming conventions


**Section**: Compliance Scoring

- Formula: (Compliant items / Total applicable items) × 100
- Total applicable = Total questions - N/A questions
- Domain scores and overall score calculation


**Section**: Assessment Workflow

- Preparation → Information Gathering → Assessment Completion → Review → Approval


---

# Sheets 2-6: Assessment Domain Sheets

## Sheet 2: Security_Requirements_Design

**Purpose**: Assess security requirements and secure design practices

**Questions** (15 total):
1. Are security requirements documented for all new development projects?
2. Are security risk assessments conducted for high-risk projects before development begins?
3. Are security acceptance criteria defined before development begins?
4. Are regulatory compliance requirements identified and documented for projects?
5. Are security requirements reviewed and approved by Application Security Team?
6. Is threat modeling performed for high-risk applications?
7. Do threat models include system overview, threat identification, and mitigation strategies?
8. Are threat models reviewed and approved by Security Architects?
9. Are security-by-design principles documented and applied?
10. Are architecture security reviews conducted for new applications?
11. Are secure design patterns documented and promoted?
12. Is developer security training provided within 30 days of hire?
13. Do 90%+ of developers complete annual security refresher training?
14. Is Security Champions program established?
15. Are training completion metrics reported to management?

**Column D (Policy Reference)**: References ISMS-POL-A.8.28 Section 2.1

**Column E (Status)**: Dropdown validation

- List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, 🔄 Planned, N/A


**Conditional Formatting (Column E)**:

- ✅ Compliant → Fill: #C6EFCE (light green)
- ⚠️ Partial → Fill: #FFEB9C (light yellow)
- ❌ Non-Compliant → Fill: #FFC7CE (light red)
- 🔄 Planned → Fill: #B4C7E7 (light blue)
- N/A → Fill: #D9D9D9 (light gray)


**Column H (Gap Priority)**: Dropdown validation (appears if Status = ❌ or ⚠️)

- List: Critical, High, Medium, Low


---

## Sheet 3: Development_Environment

**Purpose**: Assess development environment security controls

**Questions** (12 total):
1. Is MFA enforced for all source code repository access?
2. Are branch protection rules enforced requiring code review before merge?
3. Are pre-commit hooks deployed to detect and block secrets?
4. Is developer workstation security baseline defined and enforced?
5. Are developer workstations encrypted (full disk encryption)?
6. Is antivirus/EDR deployed on developer workstations?
7. Are repository access controls configured (RBAC, least privilege)?
8. Are development environments isolated from production?
9. Is source code backed up and recoverable?
10. Are secrets managed via secret manager (no hardcoded credentials)?
11. Is developer security baseline audit performed periodically?
12. Is test data security managed (production data not used without approval)?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.5

---

## Sheet 4: Build_Deployment_Pipeline

**Purpose**: Assess build and deployment pipeline security

**Questions** (12 total):
1. Are CI/CD pipelines secured (no secrets in logs, RBAC applied)?
2. Are SAST tools integrated into CI/CD pipelines?
3. Are DAST tools integrated into CI/CD pipelines?
4. Are SCA tools integrated into CI/CD pipelines?
5. Are security gates configured in pipelines (fail build on Critical/High findings)?
6. Are container images scanned for vulnerabilities before deployment?
7. Are IaC templates scanned for misconfigurations?
8. Is pipeline configuration version-controlled and audited?
9. Are pipeline secrets managed securely (secret managers, not hardcoded)?
10. Are deployment approvals required for production?
11. Is rollback capability tested and documented?
12. Are pipeline audit logs retained per policy?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.3

---

## Sheet 5: Security_Testing_Integration

**Purpose**: Assess security testing integration practices

**Questions** (12 total):
1. Is security testing included in sprint planning?
2. Are security test cases maintained alongside functional test cases?
3. Is penetration testing performed before major releases?
4. Are security findings tracked in issue tracking system?
5. Are security testing SLAs defined and monitored?
6. Is API security testing performed?
7. Are authentication and authorization tests automated?
8. Are input validation tests comprehensive?
9. Is fuzz testing performed for critical components?
10. Are security test results reviewed by Security team?
11. Are regression tests run for previously found vulnerabilities?
12. Is security testing coverage measured and reported?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.3

---

## Sheet 6: Release_Change_Management

**Purpose**: Assess release and change management security

**Questions** (12 total):
1. Are security activities included in project plans and timelines?
2. Are security stories included in sprint backlogs for all projects?
3. Is Application Security Team engaged for threat modeling and architecture reviews?
4. Are security activities budgeted and resourced appropriately?
5. Is "Definition of Done" including security criteria (SAST passing, code reviewed)?
6. Are security milestones tracked in project status reporting?
7. Are security delays/blockers escalated to management?
8. Is security debt tracked and prioritized in technical debt backlog?
9. Are security sign-offs required before production release?
10. Are change management procedures followed for security-sensitive changes?
11. Are emergency changes reviewed for security impact?
12. Is post-release security monitoring in place?

**Column structure**: Same as Sheet 2
**Policy Reference**: ISMS-POL-A.8.28 Section 2.1.6

---

# Sheet 7: Summary_Dashboard

## Purpose
Provide executive-level overview of SDLC security maturity with auto-calculated compliance metrics.

## Layout

**Header** (Rows 1-2): Same as other sheets

**Overall Compliance Summary** (Rows 4-10):

| Metric | Formula | Format |
|--------|---------|--------|
| Total Assessment Items | `=COUNTA(Security_Requirements_Design!$C$4:$C$18) + COUNTA(Development_Environment!$C$4:$C$15) + ...` | Number |
| Compliant Items (✅) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"✅ Compliant") + ...` | Number, green |
| Partial Items (⚠️) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"⚠️ Partial") + ...` | Number, yellow |
| Non-Compliant Items (❌) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"❌ Non-Compliant") + ...` | Number, red |
| Planned Items (🔄) | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"🔄 Planned") + ...` | Number, blue |
| N/A Items | `=COUNTIF(Security_Requirements_Design!$E$4:$E$18,"N/A") + ...` | Number, gray |
| **Overall Compliance Rate** | `=(Compliant / (Total - N/A)) * 100` | Percentage, bold |

**Domain Compliance Breakdown** (Rows 12-18):

| Domain | Total Items | Compliant | Partial | Non-Compliant | Compliance % |
|--------|-------------|-----------|---------|---------------|--------------|
| Security Requirements & Design | 15 | [Formula] | [Formula] | [Formula] | [Formula] |
| Development Environment | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Build & Deployment Pipeline | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Security Testing Integration | 12 | [Formula] | [Formula] | [Formula] | [Formula] |
| Release & Change Management | 12 | [Formula] | [Formula] | [Formula] | [Formula] |

**Top Gaps Requiring Attention** (Rows 20-28):

- Auto-populated list of ❌ Non-Compliant items with Priority = Critical or High
- Pulled from Gap_Analysis sheet


**Visual Indicators**:

- Compliance Rate >= 90%: Green fill
- Compliance Rate 70-89%: Yellow fill
- Compliance Rate < 70%: Red fill


---

# Sheet 8: Evidence_Register

## Purpose
Track all evidence supporting assessment claims.

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Evidence ID | 12 | Auto-generated ID | `="EV-"&TEXT(ROW()-3,"000")` |
| B | Evidence Description | 50 | What this evidence proves | Wrapped text, yellow fill |
| C | Related Assessment Question | 30 | Which question(s) this supports | Text, yellow fill |
| D | Evidence Type | 20 | Document, Screenshot, Report, etc. | Dropdown, yellow fill |
| E | Location | 60 | File path or URL | Wrapped text, yellow fill |
| F | Date Collected | 12 | When evidence was captured | Date picker, yellow fill |
| G | Collected By | 20 | Name of collector | Text, yellow fill |

**Evidence Type Dropdown**:

- Document
- Screenshot
- Configuration Export
- Report (LMS, Tool)
- Email
- Meeting Minutes
- Other


**Row Count**: 100 rows pre-formatted (evidence items EV-001 through EV-100)

---

# Sheet 9: Gap_Analysis

## Purpose
Consolidated view of all non-compliant and partial items requiring remediation.

## Column Structure

| Column | Header | Width | Purpose | Format |
|--------|--------|-------|---------|--------|
| A | Gap ID | 10 | Auto-generated ID | `="GAP-"&TEXT(ROW()-3,"000")` |
| B | Domain | 20 | Which assessment domain | Auto-populated from source sheets |
| C | Assessment Question | 50 | Question text | Auto-populated, wrapped |
| D | Current Status | 15 | ⚠️ Partial or ❌ Non-Compliant | Auto-populated |
| E | Gap Description | 50 | What's missing or insufficient | User input, yellow fill |
| F | Priority | 12 | Critical/High/Medium/Low | Auto-populated from assessment sheets |
| G | Remediation Owner | 20 | Person responsible | User input, yellow fill |
| H | Target Date | 12 | Remediation deadline | Date picker, yellow fill |
| I | Remediation Status | 15 | Not Started/In Progress/Completed | Dropdown, yellow fill |
| J | Notes | 40 | Progress updates | User input, yellow fill |

**Auto-Population Logic**:

- Scans all assessment sheets (2-7)
- Identifies rows where Status = ❌ or ⚠️
- Populates Gap_Analysis with domain, question, status, priority
- User fills in Gap Description, Owner, Target Date, Status, Notes


---

# Sheet 10: Approval_Sign_Off

## Purpose
Document formal approval workflow.

## Layout

**Assessment Completed By** (Rows 4-10):
```
Name:               [USER INPUT - yellow]
Role/Title:         [USER INPUT - yellow]
Department:         [USER INPUT - yellow]
Email:              [USER INPUT - yellow]
Date:               [USER INPUT - date picker - yellow]
Signature:          [USER INPUT - yellow]
```

**Reviewed By - Application Security Lead** (Rows 12-19):
```
Name:               [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Review Notes:       [Text area - merged cells - yellow]
Recommendation:     [Dropdown: Approve / Approve with Conditions / Return for Revision]
```

**Reviewed By - Development Management** (Rows 21-28):
```
Name:               [USER INPUT - yellow]
Role/Title:         [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Review Notes:       [Text area - merged cells - yellow]
Recommendation:     [Dropdown: Approve / Approve with Conditions / Return for Revision]
```

**Approved By - CISO** (Rows 30-37):
```
Name:               [USER INPUT - yellow]
Date:               [USER INPUT - yellow]
Approval Decision:  [Dropdown: Approved / Approved with Conditions / Rejected]
Conditions/Notes:   [Text area - merged cells - yellow]
```

**Next Review Details** (Rows 39-43):
```
Next Review Date:          [Auto-calc: Completion Date + 3 months]
Review Responsible:        [USER INPUT - yellow]
Special Considerations:    [Text area - merged cells - yellow]
```

---

# Cell Styling Reference

## Header Styles

**Main Header** (Sheet titles):

- Font: Calibri 16pt bold white
- Fill: #003366 (dark blue)
- Alignment: Center, middle
- Height: 40px
- Border: None


**Subheader** (Sheet subtitles):

- Font: Calibri 12pt white
- Fill: #4472C4 (medium blue)
- Alignment: Center, middle
- Height: 25px
- Border: None


**Column Header** (Assessment sheets):

- Font: Calibri 10pt bold black
- Fill: #D9D9D9 (light gray)
- Alignment: Center, wrapped
- Height: 30px
- Border: Thin black all sides


## Input Cell Styles

**Yellow Cells** (User input required):

- Fill: #FFFFCC (light yellow)
- Alignment: Left (text) or Center (dropdown), wrapped
- Border: Thin black all sides
- Font: Calibri 10pt regular black


## Status Cell Conditional Formatting

**Status Column (E) in Assessment Sheets**:

| Status Value | Fill Color | Font Color |
|--------------|------------|------------|
| ✅ Compliant | #C6EFCE (light green) | #006100 (dark green) |
| ⚠️ Partial | #FFEB9C (light yellow) | #9C6500 (dark yellow) |
| ❌ Non-Compliant | #FFC7CE (light red) | #9C0006 (dark red) |
| 🔄 Planned | #B4C7E7 (light blue) | #0C5BA0 (dark blue) |
| N/A | #D9D9D9 (light gray) | #7F7F7F (dark gray) |

**Conditional Formatting Rules** (apply to columns E4:E100 in each assessment sheet):
```excel
Rule 1: =E4="✅ Compliant" → Format: Fill #C6EFCE, Font #006100
Rule 2: =E4="⚠️ Partial" → Format: Fill #FFEB9C, Font #9C6500
Rule 3: =E4="❌ Non-Compliant" → Format: Fill #FFC7CE, Font #9C0006
Rule 4: =E4="🔄 Planned" → Format: Fill #B4C7E7, Font #0C5BA0
Rule 5: =E4="N/A" → Format: Fill #D9D9D9, Font #7F7F7F
```

## Freeze Panes

**All Assessment Sheets** (2-7):

- Freeze at: Row 4, Column A
- Effect: Headers (rows 1-3) remain visible when scrolling


**Summary_Dashboard**:

- Freeze at: Row 4, Column A


**Evidence_Register, Gap_Analysis**:

- Freeze at: Row 4, Column A


**Approval_Sign_Off**:

- Freeze at: Row 3, Column A


---

# Python Script Integration Points

## Script Name
`generate_a828_1_sdlc_assessment.py`

## Key Functions

**create_workbook()**:

- Initialize workbook
- Create all 11 sheets
- Return workbook object


**setup_styles()**:

- Define all cell styles (header, input, status)
- Return style dictionary


**create_instructions_sheet(wb)**:

- Populate Instructions sheet with assessment guidance
- **CUSTOMIZE**: Update organizational branding, contact information


**create_assessment_sheet(wb, sheet_name, questions, policy_ref)**:

- Generic function to create assessment sheets
- Parameters:
  - `wb`: Workbook object
  - `sheet_name`: Sheet name (e.g., "Security_Requirements")
  - `questions`: List of question texts
  - `policy_ref`: ISMS-POL-A.8.28 section reference
- Sets up headers, columns, data validation, conditional formatting


**create_summary_dashboard(wb)**:

- Create Summary_Dashboard sheet
- Calculate compliance percentages
- Generate top gaps list
- **CUSTOMIZE**: Adjust compliance thresholds (90% green, 70% yellow, <70% red)


**create_evidence_register(wb)**:

- Create Evidence_Register sheet
- 100 pre-formatted rows
- Auto-generate Evidence IDs


**create_gap_analysis(wb)**:

- Create Gap_Analysis sheet
- Auto-populate from assessment sheets (Status = ❌ or ⚠️)


**create_approval_signoff(wb)**:

- Create Approval_Sign_Off sheet
- User input fields for approval workflow


## Customization Points

Mark customization points in script with comments:

```python
# CUSTOMIZE: Organization name
ORG_NAME = "[Organization]"

# CUSTOMIZE: CISO name and email
CISO_NAME = "Chief Information Security Officer"
CISO_EMAIL = "ciso@organization.com"

# CUSTOMIZE: Compliance thresholds
COMPLIANCE_THRESHOLD_GREEN = 90  # >= 90% is green
COMPLIANCE_THRESHOLD_YELLOW = 70  # 70-89% is yellow
# < 70% is red

# CUSTOMIZE: Status dropdown options (if organization uses different terminology)
STATUS_OPTIONS = [
    "✅ Compliant",
    "⚠️ Partial",
    "❌ Non-Compliant",
    "🔄 Planned",
    "N/A"
]

# CUSTOMIZE: Priority dropdown options
PRIORITY_OPTIONS = ["Critical", "High", "Medium", "Low"]
```

## Quality Assurance

**Script Testing Checklist**:

- [ ] Workbook generates without errors
- [ ] All 11 sheets present and correctly named
- [ ] Data validation dropdowns work (Status, Priority, Evidence Type)
- [ ] Conditional formatting applies correctly (Status colors)
- [ ] Formulas calculate correctly (Summary_Dashboard percentages)
- [ ] Auto-population works (Gap_Analysis pulls from assessment sheets)
- [ ] Freeze panes set correctly
- [ ] File saves with correct naming convention


**Manual Testing** (generate workbook and verify):
1. Open workbook in Excel
2. Navigate to each sheet - no errors?
3. Test dropdown in Status column - options appear?
4. Enter "✅ Compliant" - cell turns green?
5. Enter "❌ Non-Compliant" - cell turns red?
6. Check Summary_Dashboard - percentages calculated?
7. Check Gap_Analysis - non-compliant items appear?
8. Save and re-open - no corruption warnings?

---

# File Naming Convention

**Format**: `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`

**Example**: `ISMS-IMP-A.8.28.1_SDLC_Assessment_20260124.xlsx`

**Components**:

- `ISMS-IMP-A.8.28.1`: Document ID
- `SDLC_Assessment`: Assessment type
- `YYYYMMDD`: Date generated (ISO format for sorting)
- `.xlsx`: Excel format


---

# Quarterly Review Cycle

**Every 3 Months**:
1. Generate new workbook with current date
2. Copy Evidence Register from previous assessment (continuity)
3. Re-assess all domains (don't assume unchanged)
4. Compare to previous quarter:

   - Compliance rate improved/declined?
   - Gaps remediated as planned?
   - New gaps introduced?

5. Update Gap Analysis with progress
6. Obtain fresh approvals
7. Archive previous quarter's assessment
8. Schedule next review (+3 months)

---

**END OF SPECIFICATION**

---

*"Security is a process, not a product. It's also not a destination but a journey."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-01-31 -->
