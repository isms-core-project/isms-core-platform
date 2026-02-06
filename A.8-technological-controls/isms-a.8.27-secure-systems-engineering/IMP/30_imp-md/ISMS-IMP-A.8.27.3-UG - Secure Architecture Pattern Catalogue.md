**ISMS-IMP-A.8.27.3-UG - Secure Architecture Pattern Catalogue**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Architecture Pattern Catalogue |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.3-UG |
| **Assessment Domain** | Domain 3 - Architecture Patterns and Standards |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Enterprise Security Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Enterprise Security Architect | Initial pattern catalogue assessment specification |

**Review Cycle**: Annual (or after significant architecture changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-160 Vol. 1 Rev. 1 (Engineering Trustworthy Secure Systems)
- OWASP Security Architecture Cheat Sheet

---

# Assessment Overview

## Purpose

This assessment evaluates [Organisation]'s **secure architecture pattern catalogue and governance**, focusing on the definition, adoption, and effectiveness of approved security patterns as mandated by ISMS-POL-A.8.27.

**What This Assessment Covers:**

- Pattern catalogue completeness and coverage
- Pattern documentation quality
- Pattern governance and lifecycle
- Pattern adoption rates across projects
- Deviation management and exceptions
- Pattern effectiveness and security outcomes
- Integration with architecture review process

**What This Assessment Does NOT Cover:**

- Architecture review process (see ISMS-IMP-A.8.27.1)
- Threat modelling methodology (see ISMS-IMP-A.8.27.2)
- Zero Trust implementation (see ISMS-IMP-A.8.27.4)
- Secure coding standards (see ISMS-IMP-A.8.28)

**Assessment Output:**

- Excel workbook documenting pattern catalogue maturity
- Pattern coverage analysis by domain
- Adoption rate metrics
- Pattern quality ratings
- Gap analysis and improvement plan

## Why This Matters

**ISO/IEC 27001:2022 Control A.8.27 Requirement:**
> *"Principles for engineering secure systems should be established, documented, maintained and applied to any information system development activities."*

**NIST SP 800-160 Vol. 1 Rev. 1 Guidance:**
> *"Security architecture patterns provide reusable solutions to commonly occurring security problems. They capture proven security design knowledge and enable consistent application of security principles across systems."*

**Business Impact of Missing Pattern Catalogue:**

- **Inconsistent Security:** Each project invents its own security approach
- **Repeated Mistakes:** Same vulnerabilities appear across systems
- **Slower Delivery:** Security design decisions made from scratch
- **Review Burden:** Architecture reviews require more effort without patterns
- **Knowledge Loss:** Security expertise not captured for reuse

**This Assessment Addresses:**

- Do we have a catalogue of approved secure architecture patterns?
- Are patterns documented with sufficient detail for implementation?
- Are patterns actively used in new system designs?
- Is there a governance process for pattern lifecycle?
- Do we measure pattern effectiveness?

## Who Should Complete This Assessment

**Primary Responsibility:** Enterprise Security Architect or Security Architecture Lead

**Required Knowledge:**

- [Organisation]'s architecture pattern catalogue
- Pattern documentation standards
- Pattern governance process
- Architecture review integration
- Security architecture principles

**Support Roles:**

- **CISO:** Governance oversight, exception authority
- **Enterprise Architect:** Pattern integration with EA
- **Development Teams:** Pattern adoption feedback
- **Security Engineers:** Pattern implementation experience
- **Cloud Architect:** Cloud-specific patterns

## Time Estimate

**Total Assessment Time:** 8-12 hours

**Breakdown:**

- **Information Gathering:** 3-4 hours
  - Compile pattern catalogue inventory
  - Gather pattern documentation
  - Collect adoption metrics
  - Review exception records

- **Assessment Completion:** 3-4 hours
  - Assess pattern coverage
  - Evaluate documentation quality
  - Analyse adoption rates
  - Review governance effectiveness

- **Evidence Collection:** 1-2 hours
  - Pattern documentation examples
  - Adoption tracking data
  - Exception records
  - Effectiveness metrics

- **Quality Review:** 1-2 hours
  - Gap analysis
  - Remediation planning
  - Stakeholder review

## Connection to Policy

This assessment implements **ISMS-POL-A.8.27, Section 2.2.2 (Secure Architecture Patterns)** which mandates:

**Pattern Categories:**

| Category | Examples |
|----------|----------|
| **Authentication** | SSO integration, MFA implementation, federated identity |
| **Authorisation** | RBAC implementation, attribute-based access, API authorisation |
| **Data Protection** | Encryption at rest, encryption in transit, tokenisation |
| **Network Security** | DMZ architecture, micro-segmentation, API gateway |
| **Integration** | Secure API patterns, message queue security, service mesh |
| **Cloud** | Landing zone architecture, workload isolation, cloud-native security |

**Pattern Governance Requirements:**

- Patterns SHALL be documented with security rationale
- Patterns SHALL be reviewed annually
- Deviations require Security Architect approval
- New patterns validated through threat modelling

---

# Prerequisites

## Required Access

| System/Resource | Purpose | Who Can Provide |
|-----------------|---------|-----------------|
| Pattern catalogue repository | Pattern documentation | Enterprise Architecture |
| Architecture review records | Adoption tracking | Security Architecture |
| Exception register | Deviation records | CISO Office |
| Project architecture docs | Usage evidence | Project teams |

## Pre-Assessment Checklist

✅ Pattern catalogue inventory compiled
✅ Access to pattern documentation confirmed
✅ Adoption metrics available
✅ Exception records accessible
✅ Stakeholder interviews scheduled

---

# Workbook Structure

## Sheet Overview

| Sheet | Purpose | Completion Order |
|-------|---------|------------------|
| **Instructions** | Guide to completing the workbook | Read first |
| **PatternInventory** | Complete pattern catalogue | 1 |
| **PatternQuality** | Documentation quality assessment | 2 |
| **Adoption** | Pattern adoption tracking | 3 |
| **Governance** | Pattern governance assessment | 4 |
| **Deviations** | Deviation and exception tracking | 5 |
| **Effectiveness** | Pattern effectiveness metrics | 6 |
| **Compliance** | Policy compliance scoring | 7 |
| **GapRegister** | Identified gaps and remediation | Last |
| **Dashboard** | Summary view and status | Auto-calculated |

## Sheet Descriptions

### PatternInventory Sheet

Documents the complete pattern catalogue:

| Column | Description | Example |
|--------|-------------|---------|
| Pat-ID | Pattern identifier | PAT-AUTH-001 |
| Category | Pattern category | Authentication |
| Name | Pattern name | SSO Integration Pattern |
| Version | Current version | 2.1 |
| Status | Pattern status | Approved |
| Owner | Pattern owner | Security Architect |
| LastReview | Last review date | 2025-09-15 |
| NextReview | Next review due | 2026-09-15 |
| DocumentRef | Documentation reference | PAT-AUTH-001.docx |

### PatternQuality Sheet

Assesses documentation quality:

| Column | Description | Example |
|--------|-------------|---------|
| Pat-ID | Pattern identifier | PAT-AUTH-001 |
| Element | Documentation element | Problem Statement |
| Present | Is element documented? | Yes |
| Quality | Quality rating (1-5) | 4 |
| Notes | Quality notes | Clear, well-written |

### Adoption Sheet

Tracks pattern adoption:

| Column | Description | Example |
|--------|-------------|---------|
| Pat-ID | Pattern identifier | PAT-AUTH-001 |
| ProjectCount | # projects using pattern | 15 |
| TotalApplicable | # applicable projects | 18 |
| AdoptionRate | Adoption percentage | 83% |
| Trend | Adoption trend | Increasing |

### Governance Sheet

Assesses pattern governance:

| Column | Description | Example |
|--------|-------------|---------|
| Gov-ID | Governance element | GOV-001 |
| Requirement | Governance requirement | Annual pattern review |
| Status | Implementation status | Implemented |
| Evidence | Supporting evidence | Review schedule |

### Deviations Sheet

Tracks pattern deviations:

| Column | Description | Example |
|--------|-------------|---------|
| Dev-ID | Deviation identifier | DEV-001 |
| Pattern | Pattern deviated from | PAT-NET-002 |
| Project | Project name | Legacy Migration |
| Justification | Deviation reason | Technical constraint |
| Approved | Approval status | Yes |
| ApprovedBy | Approving authority | Security Architect |
| Compensating | Compensating controls | Enhanced monitoring |
| Expiry | Exception expiry | 2026-06-30 |

### Effectiveness Sheet

Measures pattern effectiveness:

| Column | Description | Example |
|--------|-------------|---------|
| Pat-ID | Pattern identifier | PAT-AUTH-001 |
| SecurityIncidents | Related security incidents | 0 |
| VulnFindings | Vulnerability findings | 2 (Low) |
| AuditFindings | Audit findings | 0 |
| UserFeedback | User satisfaction | 4.2/5 |
| Effectiveness | Effectiveness rating | High |

---

# Completion Walkthrough

## Step 1: Complete Pattern Inventory

**Navigate to the PatternInventory sheet**

For each pattern category:

1. **List All Patterns:** Document every approved pattern
2. **Record Version:** Current version number
3. **Check Status:** Approved/Draft/Deprecated/Under Review
4. **Identify Owner:** Who maintains the pattern?
5. **Check Review Dates:** When was last review? When is next?
6. **Link Documentation:** Reference to pattern documentation

**Expected Pattern Categories:**

| Category | Minimum Patterns |
|----------|-----------------|
| **Authentication** | SSO, MFA, Service Authentication |
| **Authorisation** | RBAC, API Authorisation, Delegated Admin |
| **Data Protection** | Encryption at Rest, Encryption in Transit, Key Management |
| **Network Security** | DMZ, Micro-segmentation, API Gateway, VPN |
| **Integration** | Secure API, Message Queue, Event-Driven |
| **Cloud** | Landing Zone, Workload Isolation, Serverless Security |
| **Logging/Monitoring** | Centralised Logging, SIEM Integration |
| **Identity** | Identity Lifecycle, Privileged Access, Federation |

## Step 2: Assess Pattern Documentation Quality

**Navigate to the PatternQuality sheet**

For each pattern, assess documentation elements:

**Required Documentation Elements:**

| Element | Description | Rating Criteria |
|---------|-------------|-----------------|
| **Problem Statement** | What problem does pattern solve? | Clear, specific |
| **Context** | When to apply this pattern | Well-defined triggers |
| **Solution** | Pattern architecture/design | Complete, implementable |
| **Security Rationale** | Why is this secure? | Threat-based justification |
| **Implementation Guidance** | How to implement | Step-by-step guidance |
| **Example** | Reference implementation | Working example |
| **Anti-patterns** | What NOT to do | Common mistakes |
| **Related Patterns** | Pattern relationships | Clear connections |
| **Compliance Mapping** | Regulatory alignment | Standards referenced |
| **Threat Model** | Associated threat model | Threats addressed |

**Quality Rating Scale:**

| Rating | Description |
|--------|-------------|
| 1 | Missing or unusable |
| 2 | Present but incomplete |
| 3 | Adequate, basic coverage |
| 4 | Good, comprehensive |
| 5 | Excellent, exemplary |

## Step 3: Analyse Pattern Adoption

**Navigate to the Adoption sheet**

For each pattern:

1. **Count Applicable Projects:** How many projects should use this pattern?
2. **Count Actual Usage:** How many projects actually use it?
3. **Calculate Rate:** Adoption percentage
4. **Assess Trend:** Is adoption increasing, decreasing, or stable?
5. **Identify Barriers:** Why are some projects not adopting?

**Target Adoption Rates:**

| Pattern Status | Target Adoption |
|----------------|-----------------|
| **Mandatory** | 100% |
| **Recommended** | ≥80% |
| **Optional** | Track only |

## Step 4: Assess Pattern Governance

**Navigate to the Governance sheet**

For each governance requirement:

1. **Check Implementation:** Is governance requirement implemented?
2. **Gather Evidence:** What proves implementation?
3. **Identify Gaps:** What is missing?

**Governance Requirements:**

| Requirement | Description |
|-------------|-------------|
| Pattern Ownership | Each pattern has designated owner |
| Annual Review | All patterns reviewed annually |
| Threat Model Link | Patterns linked to threat models |
| Version Control | Pattern versions managed |
| Change Process | Process for pattern updates |
| Deprecation Process | Process for retiring patterns |
| Communication | Pattern changes communicated |
| Training | Pattern training available |
| Exception Process | Process for deviations |
| Effectiveness Review | Pattern effectiveness measured |

## Step 5: Track Deviations

**Navigate to the Deviations sheet**

For each pattern deviation:

1. **Document Deviation:** Which pattern, which project?
2. **Record Justification:** Why was deviation needed?
3. **Check Approval:** Was deviation properly approved?
4. **Note Compensating Controls:** What controls mitigate risk?
5. **Set Expiry:** When does exception expire?
6. **Monitor Status:** Is deviation still active?

**Deviation Categories:**

| Category | Description |
|----------|-------------|
| **Technical Constraint** | Pattern cannot be implemented due to technology |
| **Legacy System** | Pattern incompatible with legacy system |
| **Vendor Limitation** | Third-party doesn't support pattern |
| **Cost/Time** | Temporary deviation for delivery |
| **Performance** | Pattern impacts performance |

## Step 6: Measure Effectiveness

**Navigate to the Effectiveness sheet**

For each pattern:

1. **Security Incidents:** Any incidents related to pattern implementation?
2. **Vulnerability Findings:** Findings in pattern-based implementations?
3. **Audit Findings:** Audit issues with pattern implementations?
4. **User Feedback:** How do implementers rate the pattern?
5. **Rate Effectiveness:** Overall effectiveness rating

**Effectiveness Indicators:**

| Indicator | Good | Concern |
|-----------|------|---------|
| Security Incidents | 0 | Any |
| High/Critical Vulns | 0 | Any |
| Audit Findings | 0 | Any |
| User Satisfaction | ≥4.0/5 | <3.0/5 |
| Adoption Rate | ≥80% | <50% |

## Step 7: Complete Compliance Scoring

**Navigate to the Compliance sheet**

Map and score compliance with ISMS-POL-A.8.27 requirements.

## Step 8: Document Gaps and Remediation

**Navigate to the GapRegister sheet**

Consolidate and track all identified gaps.

---

# Evidence Collection

## Required Evidence

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| **Pattern Catalogue** | Complete pattern inventory | Architecture Repository |
| **Pattern Docs** | Sample pattern documentation | Architecture Repository |
| **Adoption Data** | Pattern usage tracking | Architecture Review Records |
| **Deviation Records** | Approved deviations | Exception Register |
| **Review Records** | Pattern review evidence | Architecture Repository |
| **Effectiveness Data** | Security metrics | ISMS Dashboard |

---

# Common Pitfalls

❌ **MISTAKE:** Creating patterns without security rationale
✅ **CORRECT:** Every pattern must explain WHY it is secure

❌ **MISTAKE:** Patterns too abstract to implement
✅ **CORRECT:** Include implementation guidance and examples

❌ **MISTAKE:** Patterns created but never reviewed
✅ **CORRECT:** Annual review cycle enforced

❌ **MISTAKE:** Deviations approved without compensating controls
✅ **CORRECT:** Require compensating controls for all deviations

❌ **MISTAKE:** Pattern adoption not tracked
✅ **CORRECT:** Measure adoption through architecture reviews

❌ **MISTAKE:** Patterns not linked to threat models
✅ **CORRECT:** Each pattern should reference threat model

❌ **MISTAKE:** Cloud patterns missing from catalogue
✅ **CORRECT:** Modern catalogue must include cloud patterns

❌ **MISTAKE:** Legacy patterns never deprecated
✅ **CORRECT:** Active deprecation process for outdated patterns

❌ **MISTAKE:** Patterns exist only in architects' heads
✅ **CORRECT:** All patterns formally documented

❌ **MISTAKE:** No feedback loop from implementers
✅ **CORRECT:** Collect and act on implementation feedback

---

# Quality Checklist

**Completeness:**

- [ ] All pattern categories represented
- [ ] Each pattern documented in inventory
- [ ] Documentation quality assessed
- [ ] Adoption rates calculated
- [ ] Governance requirements evaluated
- [ ] Deviations documented
- [ ] Effectiveness measured

**Evidence:**

- [ ] Pattern documentation samples collected
- [ ] Adoption tracking evidence
- [ ] Deviation approvals documented
- [ ] Effectiveness metrics captured

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
