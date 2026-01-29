# ISMS-POL-A.8.28-S5
## Secure Coding - Annexes Overview

**Document ID**: ISMS-POL-A.8.28-S5
**Title**: Secure Coding - Annexes Overview  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial annexes overview document |

**Review Cycle**: Annual
**Next Review Date**: [Approval Date + 12 months] 
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead

**Distribution**: All developers, Security Team, Security Champions
**Related Documents**: 
- ISMS-POL-A.8.28 (Master Policy)
- ISMS-POL-A.8.28-S1 through S4 (Policy Sections)
- All S5.X Annexes

---

## 1. Introduction

### 1.1 Purpose of Annexes

> *"The worthwhile problems are the ones you can really solve or help solve, the ones you can really contribute something to." - Richard Feynman*

This document serves as the **navigation hub** for all Secure Coding Policy Annexes. Annexes provide **practical, operational guidance** that supplements the policy requirements defined in sections S1 through S4.

**Key Distinction**:
- **Policy Sections (S1-S4)**: Define WHAT must be done (requirements, obligations)
- **Annexes (S5.X)**: Define HOW to do it (procedures, checklists, examples)

Annexes are designed to be:
- **Actionable**: Step-by-step guidance developers can apply immediately
- **Maintainable**: Updated more frequently than core policy as technology evolves
- **Practical**: Real code examples, checklists, templates rather than theoretical discussion

### 1.2 How Annexes Relate to Policy Sections

Annexes operationalize policy requirements:

| Policy Section | Related Annex | Relationship |
|----------------|---------------|--------------|
| S2.2 (Secure Coding Standards) | S5.A (Language Guidelines) | Language-specific implementation of coding standards |
| S2.2 (Secure Coding Standards) | S5.D (Quick Reference) | Developer-friendly summary of key standards |
| S2.3 (Code Review & Testing) | S5.B (Review Checklist) | Actionable checklist operationalizing review requirements |
| S2.3.3 (Vulnerability Management) | S5.C (Vulnerability Response) | Step-by-step procedures for handling vulnerabilities |

### 1.3 When to Use Each Annex

**Daily Development**:
- **S5.D (Quick Reference)**: Keep handy during coding, pre-commit checklist
- **S5.A (Language Guidelines)**: Reference when working with specific languages

**Code Review**:
- **S5.B (Review Checklist)**: Security-focused review criteria for reviewers

**Incident Response**:
- **S5.C (Vulnerability Response)**: Follow when vulnerability discovered

**Onboarding**:
- Read S5.D first (overview), then dive into relevant language-specific S5.A sections

---

## 2. Annex Inventory

### 2.1 Complete Annex List

| Annex ID | Title | Lines | Purpose | Primary Audience |
|----------|-------|-------|---------|------------------|
| **S5** | Annexes Overview | ~300 | Navigation and maintenance guidance | All stakeholders |
| **S5.A** | Language-Specific Guidelines | ~400 | Secure coding patterns per language | Developers (by language) |
| **S5.B** | Code Review Checklist | ~400 | Security-focused review criteria | Code Reviewers, Security Champions |
| **S5.C** | Vulnerability Response Procedures | ~400 | Incident handling step-by-step | Security Team, Developers, Managers |
| **S5.D** | Quick Reference Guide | ~300 | One-page developer cheat sheet | All developers (especially new) |

**Total Annexes Size**: ~1,800 lines (vs. ~3,200 lines for core policy S1-S4)

### 2.2 Detailed Annex Descriptions

#### S5.A - Language-Specific Secure Coding Guidelines

**Purpose**: Translate generic secure coding standards into language-specific guidance

**Content**:
- Common vulnerability patterns per language
- Secure coding practices (input validation, output encoding, cryptography)
- Code examples (correct vs. incorrect patterns)
- Recommended security tools (SAST, linters, dependency scanners)
- References to external standards (OWASP, SEI CERT)

**Coverage**: Python, Java, JavaScript/TypeScript, C#/.NET, Go, PHP (prioritized by organizational usage)

**When to Use**:
- Starting new project in specific language
- Learning secure coding for new language
- Reference during code review
- Investigating SAST findings

#### S5.B - Code Review Checklist Template

**Purpose**: Provide actionable security checklist for code reviewers

**Content**:
- Pre-review checklist (automated checks, risk assessment)
- Core security review items (authentication, input validation, cryptography, etc.)
- Risk-based review guidance (Critical vs. Low risk changes)
- Review outcome actions (approve, request changes, escalate)
- Post-review tracking

**Format**: Checkbox list with guidance notes and policy cross-references

**When to Use**:
- Every pull request/code review
- Security Champion reviews
- Pre-deployment security validation

#### S5.C - Vulnerability Response Procedures

**Purpose**: Step-by-step procedures for handling discovered vulnerabilities

**Content**:
- Vulnerability discovery (internal, external, public sources)
- Triage process (validation, severity assessment, impact analysis)
- Remediation options (patch, workaround, compensating control, risk acceptance)
- Verification procedures
- External reporting (responsible disclosure, bug bounty)
- Emergency response for critical vulnerabilities
- Metrics and lessons learned

**When to Use**:
- Vulnerability discovered by SAST/DAST/SCA
- External security researcher report
- Critical vulnerability in production
- Bug bounty submission

#### S5.D - Quick Reference Guide

**Purpose**: One-page developer security reference for daily use

**Content**:
- Top 10 secure coding principles
- Pre-commit checklist
- Security tools quick reference
- Common vulnerability quick fixes
- Escalation paths
- Key policy references
- Secure development workflow

**When to Use**:
- Daily development (keep visible)
- New developer onboarding
- Pre-commit self-review
- Quick reminder of security basics

---

## 3. Annex Maintenance

### 3.1 Update Philosophy

> *"Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organization of the entire tapestry." - Feynman on consistency*

**Annexes vs. Policy Update Frequency**:
- **Core Policy (S1-S4)**: Annual review cycle (stable requirements)
- **Annexes (S5.X)**: Semi-annual to quarterly review (tactical guidance evolves faster)

**Rationale**: Technology, tools, and threats evolve faster than fundamental security principles. Annexes can be updated more frequently without requiring full policy review cycle.

### 3.2 Annex Update Process

#### 3.2.1 Routine Updates (Quarterly/Semi-Annual)

**Triggers**:
- New language adopted by organization
- Major framework update (e.g., React 19, Django 5)
- OWASP Top 10 updated
- New security tools deployed
- Lessons learned from vulnerability incidents

**Process**:
1. **Propose Update**: Any developer, Security Champion, or Security Team member can propose
2. **Review**: Application Security Lead reviews proposal
3. **Approval**: Application Security Lead approves (CISO notification, not approval)
4. **Update**: Make changes to affected annex
5. **Communication**: Announce update to developers (email, Slack, team meetings)
6. **Training**: Update training materials if significant change

**Approval Authority**: Application Security Lead (faster than full CISO approval for tactical changes)

#### 3.2.2 Emergency Updates

**Triggers**:
- Critical vulnerability affecting organizational code patterns
- Zero-day exploited in wild affecting organization
- Regulatory requirement change

**Process**:
1. **Immediate Update**: Security Team makes urgent update
2. **Notification**: CISO and Development Management notified immediately
3. **Retrospective Approval**: Application Security Lead formally approves within 48 hours
4. **Communication**: Emergency notification to all developers

### 3.3 Technology-Specific Update Triggers

**New Language Adoption** (S5.A update):
- When organization adopts new programming language
- Add new section to S5.A within 30 days of language approval
- Based on OWASP, CERT, and vendor security guides

**Framework Major Version** (S5.A update):
- When major framework version released (e.g., Spring Boot 4.0)
- Review and update relevant section within 90 days
- Focus on security-breaking changes

**Tool Changes** (S5.D update):
- New SAST/SCA tool deployed
- Update quick reference within 30 days
- Include tool usage instructions

**OWASP Top 10 Update** (S5.B update):
- Review code review checklist
- Update within 60 days of OWASP publication
- Add new vulnerability categories if relevant

### 3.4 Version Control

**Annex Versioning**:
- Major version (X.0): Significant restructuring or scope change
- Minor version (1.X): Content updates, new sections added
- Patch version (1.0.X): Corrections, clarifications, small updates

**Example**:
- S5.A v1.0: Initial language guidelines
- S5.A v1.1: Added Go language section
- S5.A v1.1.1: Corrected Python cryptography example
- S5.A v2.0: Complete restructuring to framework-based approach

**Change Log**: Each annex maintains version history in Document Control section

---

## 4. Relationship to External Standards

### 4.1 Standards Mapping

Annexes operationalize guidance from industry-recognized standards:

| External Standard | Annex Application | How We Use It |
|-------------------|-------------------|---------------|
| **OWASP Top 10** | S5.B (Checklist), S5.D (Quick Ref) | Vulnerability categories in review checklist |
| **OWASP ASVS** | S5.B (Checklist) | Security requirement verification approach |
| **OWASP Cheat Sheet Series** | S5.A (Language Guidelines) | Language-specific secure coding patterns |
| **SEI CERT Coding Standards** | S5.A (Language Guidelines) | Authoritative language security rules |
| **CWE Top 25** | S5.B (Checklist), S5.C (Response) | Vulnerability classification and prioritization |
| **CVSS 3.1** | S5.C (Response) | Vulnerability severity scoring |
| **NIST 800-218 (SSDF)** | S5.D (Quick Ref) | Secure development lifecycle workflow |

### 4.2 Standard Update Integration

**When external standard updates**:
1. **Monitor**: Security Team monitors standard updates (OWASP, NIST, CERT)
2. **Assess**: Application Security Lead assesses impact on annexes
3. **Update**: Relevant annexes updated per Section 3.2 process
4. **Communicate**: Changes communicated to developers with rationale

**Example**:
- OWASP Top 10 2025 published
- New category "AI Security Risks" added
- S5.B updated within 60 days to include AI-specific review items
- Developers notified via security newsletter

### 4.3 Vendor-Specific Guidance Integration

For vendor technologies organization uses:

**Microsoft Security Development Lifecycle (SDL)**:
- Applied to .NET/C# guidance in S5.A
- Code review practices influence S5.B

**Oracle Secure Coding Guidelines**:
- Applied to Java guidance in S5.A
- Database security patterns in S5.A

**Python Packaging Authority (PyPA) Security**:
- Dependency management guidance in S5.A (Python section)

**Node.js Security Best Practices**:
- JavaScript/TypeScript guidance in S5.A

---

## 5. Usage Guidance

### 5.1 Integration with Development Workflow

#### 5.1.1 Daily Development

**Developers**:
- Keep **S5.D (Quick Reference)** visible (printed, pinned in IDE, second monitor)
- Reference **S5.A (Language Guidelines)** when working with specific languages
- Use pre-commit checklist from S5.D before submitting code

**Recommended Workflow**:
```
1. Design → Reference S5.A for language-specific security patterns
2. Code → S5.D visible for quick checks
3. Pre-commit → S5.D pre-commit checklist
4. Submit PR → Ready for review
```

#### 5.1.2 Code Review

**Code Reviewers**:
- Use **S5.B (Code Review Checklist)** for every security-relevant PR
- Reference **S5.A (Language Guidelines)** for language-specific patterns
- Escalate to Security Champion if checklist unclear

**Security Champions**:
- Use S5.B for all high-risk reviews
- Contribute feedback to improve S5.B based on real reviews

#### 5.1.3 Incident Response

**Security Team**:
- Follow **S5.C (Vulnerability Response)** step-by-step for all vulnerabilities
- Use S5.C templates for tracking and communication

**Development Teams**:
- Remediate per S5.C guidance
- Reference S5.A for secure fix patterns

### 5.2 Contributing Improvements

> *"The only way to have real success in science is to describe the evidence very carefully without regard to the way you feel it should be." - Feynman on honest feedback*

**Developer Feedback Process**:
1. **Identify Gap**: Annex unclear, missing content, or incorrect
2. **Document Feedback**: Specific issue and suggested improvement
3. **Submit**: Via security feedback channel (email, Slack, JIRA)
4. **Review**: Application Security Lead reviews within 5 business days
5. **Decision**: Accept (update annex), decline (explain rationale), or defer (needs more research)
6. **Communication**: Contributor notified of decision

**Encouraged Feedback**:
- Real code examples from your projects
- SAST false positive patterns to document
- Language-specific security patterns missing from S5.A
- Checklist items unclear or difficult to apply

**Feedback Metrics**: Track feedback volume and implementation rate to ensure annexes stay relevant

### 5.3 Integration with Tooling

#### 5.3.1 IDE Integration

**Goal**: Make annexes accessible in developer flow

**Approaches**:
- IDE snippets/templates based on S5.A patterns
- Linter rules referencing S5.A standards
- Pre-commit hooks enforcing S5.D checklist items

**Example**: PyCharm custom inspection referencing Python S5.A section

#### 5.3.2 CI/CD Integration

**Goal**: Automate annex enforcement where possible

**Approaches**:
- SAST rules aligned with S5.A standards
- PR templates incorporating S5.B checklist items
- Automated checks for S5.D pre-commit items (secret scanning, formatting)

**Note**: Automation supplements, not replaces, human judgment from annexes

#### 5.3.3 Knowledge Base Integration

**Goal**: Make annexes searchable and linkable

**Approaches**:
- Annexes published in internal wiki/knowledge base
- Deep links to specific sections (e.g., S5.B #authentication-checks)
- Search functionality across all policy and annexes
- Referenced in vulnerability tracking tickets

---

## 6. Training and Onboarding

### 6.1 New Developer Onboarding

**Week 1 - Security Basics**:
- Read **S5.D (Quick Reference)** - 15 minutes
- Overview of **S5** (this document) - 10 minutes
- Watch secure coding training video (references annexes)

**Week 2 - Deep Dive**:
- Read **S5.A section** for primary language - 30 minutes
- Shadow code review using **S5.B** - 1 hour
- Complete secure coding quiz (based on S5.D and S5.A)

**Month 1-3 - Practical Application**:
- Apply S5.D pre-commit checklist on all commits
- Participate in code reviews using S5.B
- Reference S5.A during development

### 6.2 Ongoing Training

**Quarterly Security Workshops**:
- Review recent vulnerabilities (S5.C lessons learned)
- Update on annex changes
- Hands-on exercises using S5.B checklist

**Annual Secure Coding Refresher**:
- S5.D principles review
- New vulnerabilities from OWASP Top 10
- Policy and annex updates

**Just-in-Time Training**:
- When new language adopted (S5.A new section)
- When vulnerability discovered (S5.C process)
- When tool changes (S5.D update)

---

## 7. Governance

### 7.1 Ownership and Accountability

| Role | Responsibility |
|------|----------------|
| **CISO** | Overall policy ownership, approves S5 overview changes |
| **Application Security Lead** | Annex content ownership, approves all annex updates |
| **Security Champions** | Contribute feedback from development teams, pilot annex changes |
| **Development Managers** | Ensure teams trained on annexes, enforce usage |
| **Developers** | Apply annexes daily, provide feedback |

### 7.2 Compliance Monitoring

**Metrics Tracked**:
- Code review checklist (S5.B) usage rate (target: 100% for high-risk PRs)
- Vulnerability response SLA compliance (S5.C) (target: 95%)
- Developer feedback volume (indicates engagement)
- Training completion rates

**Reporting**:
- Monthly annex usage metrics to Application Security Lead
- Quarterly annex effectiveness review (CISO + Application Security Lead)
- Annual annex update recommendations to CISO

---

## 8. Document History

| Date | Version | Change Summary | Author |
|------|---------|----------------|--------|
| [Approval Date] | 1.0 | Initial annexes overview document creation | Application Security Lead |

---

## 9. Appendix: Annex Quick Navigation

**For Developers**:
- Daily work → **S5.D** (Quick Reference)
- Language-specific → **S5.A** (Language Guidelines)
- Code review → **S5.B** (Review Checklist)

**For Security Team**:
- Vulnerability handling → **S5.C** (Vulnerability Response)
- Policy overview → **S5** (this document)

**For Managers**:
- Training planning → **S5** (this document) + **S5.D** (Quick Reference)
- Incident response → **S5.C** (Vulnerability Response)

---

**END OF DOCUMENT**