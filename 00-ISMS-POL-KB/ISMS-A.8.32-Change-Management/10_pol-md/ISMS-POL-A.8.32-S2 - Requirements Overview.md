# ISMS-POL-A.8.32-S2
## Change Management - Requirements Overview

**Document ID**: ISMS-POL-A.8.32-S2  
**Title**: Change Management Requirements - Framework Overview  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Information Security Manager | Initial requirements framework |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Change Manager / IT Operations Manager
- Compliance Review: Legal/Compliance Officer

**Distribution**: Change Manager, CAB members, IT operations, system owners, security team  
**Related Documents**: ISMS-POL-A.8.32 (Master), ISMS-POL-A.8.32-S1 (Purpose, Scope, Definitions)

---

## 2.1 Requirements Framework Overview

### 2.1.1 Purpose of This Section

This document provides the high-level framework for change management requirements, organized into four major requirement domains:

1. **Change Process Requirements (S2.1):** Core workflow from initiation through closure
2. **Change Classification Requirements (S2.2):** Standard, normal, and emergency change types
3. **Testing & Validation Requirements (S2.3):** Environment separation and testing procedures
4. **Emergency Change Requirements (S2.4):** Fast-track procedures and post-implementation review

Each requirement domain is detailed in a separate section document to maintain modularity and facilitate targeted updates.

### 2.1.2 ISO/IEC 27002:2022 Mapping

**Control 8.32 specifies nine mandatory change management procedure elements:**

| ISO 27002 Element | Requirement Domain | Section Reference |
|-------------------|--------------------|--------------------|
| **(a) Planning and impact assessment** | Change Process | S2.1 |
| **(b) Authorization** | Change Process | S2.1 |
| **(c) Communication** | Change Process | S2.1 |
| **(d) Testing and acceptance** | Testing & Validation | S2.3 |
| **(e) Implementation** | Change Process | S2.1 |
| **(f) Emergency and contingency** | Emergency Changes | S2.4 |
| **(g) Record keeping** | Change Process | S2.1 |
| **(h) Documentation updates** | Change Process | S2.1 |
| **(i) Continuity plan updates** | Change Process | S2.1 |

**Additional elements from ISO 27002:2022 Attribute Table:**

| Attribute | Organizational Approach |
|-----------|------------------------|
| **Control Type** | Preventive, Detective |
| **Information Security Property** | Availability, Integrity, Confidentiality |
| **Cybersecurity Concept** | Protect, Recover |
| **Operational Capability** | Change management |
| **Security Domain** | Protection |

### 2.1.3 Requirements Hierarchy

```
ISMS-POL-A.8.32-S2 (Requirements Overview) ← You are here
│
├── ISMS-POL-A.8.32-S2.1 (Change Process Requirements)
│   ├── Planning & Impact Assessment Requirements
│   ├── Authorization Requirements
│   ├── Communication Requirements  
│   ├── Implementation Requirements
│   ├── Documentation Requirements
│   └── Record Keeping Requirements
│
├── ISMS-POL-A.8.32-S2.2 (Change Classification Requirements)
│   ├── Standard Change Requirements
│   ├── Normal Change Requirements
│   ├── Emergency Change Requirements
│   └── Risk-Based Categorization Requirements
│
├── ISMS-POL-A.8.32-S2.3 (Testing & Validation Requirements)
│   ├── Environment Separation Requirements (Dev/Test/Prod)
│   ├── Testing Procedure Requirements
│   ├── Acceptance Criteria Requirements
│   ├── Rollback Requirements
│   └── Integration with Control 8.29 (Security Testing)
│
└── ISMS-POL-A.8.32-S2.4 (Emergency Change Requirements)
    ├── Emergency Criteria Requirements
    ├── Fast-Track Approval Requirements
    ├── Risk Acceptance Requirements
    └── Post-Implementation Review Requirements
```

---

## 2.2 Requirements Language

### 2.2.1 Requirement Keywords (RFC 2119)

This framework uses RFC 2119 requirement keywords:

**SHALL / SHALL NOT:**
- Mandatory requirements (absolute requirement)
- Non-compliance constitutes a control failure
- Requires formal exception process to deviate

**SHOULD / SHOULD NOT:**
- Strongly recommended (recommended requirement)
- Valid reasons may exist to deviate in specific circumstances
- Deviation requires risk assessment and documentation

**MAY:**
- Optional (truly optional)
- Implementation at organization's discretion
- No compliance expectation

**MUST / MUST NOT:**
- Technical necessity (not policy requirement)
- Used for technical constraints, not governance requirements

### 2.2.2 Requirement Structure

Each detailed requirement section (S2.1 through S2.4) follows this structure:

**Requirement Statement:**
- Clear, unambiguous requirement using SHALL/SHOULD/MAY keywords
- Single requirement per statement (no compound requirements)
- Testable/verifiable through assessment or audit

**Rationale:**
- Why this requirement exists
- Risk(s) being mitigated
- Benefit to information security

**Implementation Guidance:**
- How organizations typically implement the requirement
- Technology-agnostic capability descriptions
- Examples (where helpful)

**Assessment Criteria:**
- How compliance is verified
- Evidence expected during audit
- Reference to assessment workbook sheet

**Exceptions:**
- When exceptions may be appropriate
- Exception approval process
- Compensating controls required

---

## 2.3 Requirement Domains Summary

### 2.3.1 Change Process Requirements (S2.1)

**Scope:** End-to-end change workflow from initiation through closure.

**Key Requirements Coverage:**
- Change request submission and documentation standards
- Impact and risk assessment procedures
- Authorization levels and approval workflows
- Communication to stakeholders (timing, content, methods)
- Implementation planning and execution controls
- Documentation updates (operational procedures, runbooks)
- Continuity plan updates (where infrastructure changes affect continuity)
- Record keeping and audit trail requirements
- Change closure and post-implementation review

**Assessment:** ISMS-IMP-A.8.32.1 (Change Process Assessment)

### 2.3.2 Change Classification Requirements (S2.2)

**Scope:** Definition and management of different change types.

**Key Requirements Coverage:**
- Standard change catalog (pre-approved, low-risk changes)
- Standard change approval and logging procedures
- Normal change risk assessment and CAB review
- Emergency change triggers and fast-track process
- Risk matrix and impact/likelihood classification
- Approval authority based on risk level
- Change calendar management (freeze periods, blackout windows)

**Assessment:** ISMS-IMP-A.8.32.2 (Change Types & Categories Assessment)

### 2.3.3 Testing & Validation Requirements (S2.3)

**Scope:** Environment separation and comprehensive testing before production deployment.

**Key Requirements Coverage:**
- Development environment requirements and access controls
- Test/QA environment requirements and data protection
- Production environment protection and change restrictions
- Environment promotion workflow (Dev → Test → Prod)
- Testing procedures (unit, integration, UAT, security, regression)
- Acceptance criteria definition and sign-off
- Rollback procedure requirements
- Production validation testing
- Integration with Control 8.29 (Security Testing)
- Integration with Control 8.33 (Test Information Protection)

**Assessment:** 
- ISMS-IMP-A.8.32.3 (Environment Separation Assessment)
- ISMS-IMP-A.8.32.4 (Testing & Validation Assessment)

### 2.3.4 Emergency Change Requirements (S2.4)

**Scope:** Accelerated procedures for urgent changes while maintaining control.

**Key Requirements Coverage:**
- Emergency change criteria (what qualifies as emergency)
- Emergency CAB (E-CAB) composition and availability
- Fast-track approval procedures
- Accelerated risk assessment
- Communication during emergencies
- Documentation requirements (even under pressure)
- Post-implementation review (mandatory, no exceptions)
- Lessons learned and process improvement
- Prevention of "emergency change abuse"

**Assessment:** ISMS-IMP-A.8.32.2 (Emergency changes section)

---

## 2.4 Requirements Relationship to Implementation

### 2.4.1 Policy → Assessment Flow

```
┌───────────────────────────────────────────────────┐
│  POLICY LAYER (What is required)                  │
│  ISMS-POL-A.8.32-S2.X documents                   │
│  - Requirements stated as SHALL/SHOULD/MAY        │
│  - Technology-agnostic capabilities               │
│  - Mandatory procedures defined                   │
└───────────────┬───────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  ASSESSMENT LAYER (How it is implemented)         │
│  ISMS-IMP-A.8.32.X Excel workbooks                │
│  - Stakeholders document THEIR implementation     │
│  - Specific tools, workflows, and evidence        │
│  - Gap analysis against policy requirements       │
└───────────────┬───────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────┐
│  EVIDENCE LAYER (Proof of compliance)             │
│  Evidence registers in each workbook              │
│  - Change tickets, approvals, test results        │
│  - Configuration screenshots, logs                │
│  - CAB meeting minutes, PIR documents             │
└───────────────────────────────────────────────────┘
```

### 2.4.2 Technology-Agnostic Policy Principle

**Policy Requirements state WHAT capabilities are required:**

❌ **Wrong:** "Organizations SHALL deploy ServiceNow Change Management module"  
✅ **Right:** "Organizations SHALL implement change management system capable of tracking change requests with full audit trail"

❌ **Wrong:** "All changes SHALL use GitLab CI/CD pipeline"  
✅ **Right:** "All changes SHALL follow documented promotion workflow from development through testing to production"

❌ **Wrong:** "CAB SHALL use Microsoft Teams for meetings"  
✅ **Right:** "CAB meetings SHALL be conducted with documented attendance and decisions"

**Assessment Workbooks document HOW organization implements:**

Organizations document their ACTUAL tools:
- "Our change management system is: ServiceNow"
- "Our version control system is: GitHub Enterprise"
- "Our CI/CD pipeline is: Jenkins + GitLab CI"
- "CAB meetings are held via: Microsoft Teams with recordings in SharePoint"

This approach ensures:
- Policy remains valid regardless of technology changes
- Organizations can use any tools meeting capability requirements
- Assessments reflect reality, not aspirational state
- Audits focus on capabilities achieved, not products deployed

---

## 2.5 Compliance and Enforcement

### 2.5.1 Requirement Compliance Measurement

**Compliance assessed at two levels:**

**Policy Compliance:**
- Are required procedures documented?
- Are roles and responsibilities assigned?
- Are approval workflows defined?
- Is training provided?

**Operational Compliance:**
- Are procedures actually followed?
- Are changes properly documented?
- Are approvals obtained before implementation?
- Are testing requirements met?

**Compliance Metrics:**
- Percentage of changes with proper authorization (target: 100%)
- Percentage of changes with documented risk assessment (target: 100%)
- Percentage of changes with evidence of testing (target: 100% for normal changes)
- Percentage of changes with PIR completed (target: 100%)
- Unauthorized change incidents (target: 0)

**Dashboard Reporting:**
ISMS-IMP-A.8.32.5 (Compliance Dashboard) aggregates compliance metrics across all four requirement domains.

### 2.5.2 Non-Compliance Handling

**Minor Non-Compliance (Process Deviations):**
- Examples: Late PIR, incomplete documentation, minor procedural gaps
- Handled by: Change Manager, corrective action documented
- Escalation: If pattern emerges, escalate to IT Operations Manager

**Major Non-Compliance (Control Failures):**
- Examples: Unauthorized production changes, changes without approval, testing bypassed
- Handled by: Security incident process, Change Manager + CISO involved
- Actions: Root cause analysis, corrective action plan, retraining
- Documentation: Incident report, lessons learned, process updates

**Repeated Non-Compliance:**
- Pattern of violations by individual or team
- Escalation to: IT Operations Manager, CISO, Human Resources
- Actions: Performance management, access restrictions, additional training
- Severe cases: Disciplinary action per organizational HR policies

### 2.5.3 Exception Process

**When Exceptions Are Appropriate:**
- Technical constraints prevent full compliance
- Business circumstances require temporary deviation
- Alternative compensating controls provide equivalent protection
- Emergency situation (formalized via emergency change process)

**Exception Approval Authority:**
- Standard requirement exceptions: Change Manager
- SHALL requirement exceptions: CISO + Risk Owner
- Regulatory requirement exceptions: CISO + Legal/Compliance Officer + Executive Management

**Exception Documentation:**
- Specific requirement being excepted
- Business/technical justification
- Risk assessment of exception
- Compensating controls (if any)
- Exception duration (temporary exceptions should have expiration)
- Review schedule
- Approval signatures

**Exception Management:**
- Exceptions tracked in Change Management Compliance Dashboard
- Quarterly review of all active exceptions
- Annual comprehensive exception review
- Exceptions automatically expire unless renewed

---

## 2.6 Continuous Improvement

### 2.6.1 Requirements Evolution

**This framework is not static.**

Requirements SHALL be reviewed and updated based on:
- Failed changes (what went wrong, what requirement could have prevented it)
- Audit findings (gaps identified during internal/external audits)
- Incident analysis (changes that caused or contributed to incidents)
- Technology evolution (new tools, methodologies, practices)
- Regulatory changes (new compliance requirements)
- Industry best practices (emerging standards, lessons from other organizations)

**Change Manager is responsible for:**
- Collecting feedback on requirement effectiveness
- Analyzing change failure patterns
- Proposing requirement updates
- Facilitating periodic requirements review workshops

### 2.6.2 Metrics-Driven Improvement

**Key questions to track over time:**
- Is change success rate improving?
- Is emergency change percentage decreasing?
- Is average change implementation time acceptable?
- Are changes causing incidents?
- Is compliance with requirements improving?

**Dashboard Analytics:**
ISMS-IMP-A.8.32.5 provides trend analysis, helping identify:
- Problematic change types (candidates for process improvement)
- Teams with low compliance (candidates for training)
- Recurring failure modes (candidates for new requirements)
- Successful practices (candidates for standardization)

---

## 2.7 Document Maintenance

### 2.7.1 Section Updates

**This overview document SHALL be updated when:**
- New requirement sections are added (e.g., S2.5 if needed)
- Existing requirement sections are restructured
- ISO/IEC 27002:2022 guidance is updated for Control 8.32
- Major regulatory changes affect requirement framework
- Assessment workbook structure changes significantly

**Minor updates (not requiring version change):**
- Clarifications to existing content
- Example additions
- Formatting improvements
- Cross-reference corrections

### 2.7.2 Integration with Master Policy

This requirements overview document is part of the modular policy framework defined in ISMS-POL-A.8.32 (Master).

**Version coordination:**
- Major changes to requirements framework SHALL trigger master policy review
- Master policy version reflects overall framework state
- Individual sections can have independent minor versions
- Annual review ensures alignment across all sections

---

## 2.8 Navigation Guide

### 2.8.1 Reading Path for Different Audiences

**Change Managers / CAB Members:**
→ Start here (S2)
→ Read S2.1 (Change Process)
→ Read S2.2 (Change Classification)  
→ Review S2.4 (Emergency Changes)
→ Reference S3 (Roles & Responsibilities)

**Technical Implementers:**
→ Read S2.1 (Change Process) for workflow understanding
→ Read S2.3 (Testing & Validation) in detail
→ Reference S2.2 for standard change catalog
→ Reference S5.D (Quick Reference Guide) for day-to-day use

**Security Team:**
→ Read S1 (Purpose, Scope, Definitions)
→ Read S2.3 (Testing & Validation) - security testing integration
→ Read S2.4 (Emergency Changes) - security incident remediation
→ Review all sections for security implications

**Auditors:**
→ Read S1 (Purpose, Scope, Definitions) for context
→ Read S2 (this overview) for requirement framework
→ Read S2.1-S2.4 for detailed requirements
→ Review implementation workbooks (IMP-A.8.32.1 through IMP-A.8.32.5)
→ Sample evidence registers for compliance verification

**Executive Management:**
→ Read Master Policy (ISMS-POL-A.8.32) Executive Summary
→ Review S2 (this overview) for requirement framework
→ Review Compliance Dashboard (IMP-A.8.32.5) for metrics
→ Focus on risk mitigation and business value

---

**END OF SECTION 2**

*"Science is the belief in the ignorance of experts."  
— Richard Feynman*

*Requirements frameworks should be questioned, tested, and improved based on evidence. If a requirement doesn't prevent failures or improve security, we should change it—not worship it.* 🔬