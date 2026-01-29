# ISMS-POL-A.8.9-S5
## Configuration Management - Annexes

**Document ID**: ISMS-POL-A.8.9-S5  
**Title**: Annexes (Index and Overview)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Configuration Manager / CISO | Initial annexes index |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Configuration Manager / Security Architect

**Distribution**: All technical staff, management  
**Related Documents**: All ISMS-POL-A.8.9 sections

---

## 5.1 Purpose

This document serves as an **index and navigation guide** for the Configuration Management Policy annexes. Annexes provide supporting materials, templates, and detailed standards that complement the main policy requirements.

**The Anti-Pattern**: Organizations that bury critical operational guidance in 200-page appendices that nobody can find. Good annexes are quickly accessible and immediately useful.

**The Feynman Standard**: *"If your system administrator can't find the Windows Server baseline in under 30 seconds, your documentation structure failed. Organize for findability, not elegance."*

---

## 5.2 Annex Overview

### 5.2.1 Available Annexes

[Organization]'s Configuration Management Policy includes the following annexes:

| Annex | Title | Purpose | Document ID |
|-------|-------|---------|-------------|
| **A** | Configuration Standards by Asset Type | Detailed hardening standards and baseline guidance for specific technologies | ISMS-POL-A.8.9-S5.A |
| **B** | Change Request Form Template | Standard template for submitting configuration change requests | ISMS-POL-A.8.9-S5.B |
| **C** | Configuration Deviation Procedures | Step-by-step procedures for handling configuration drift and policy deviations | ISMS-POL-A.8.9-S5.C |
| **D** | Quick Reference Guide | One-page summary for common configuration management tasks | ISMS-POL-A.8.9-S5.D |

---

## 5.3 Annex Descriptions

### 5.3.1 Annex A - Configuration Standards by Asset Type

**Purpose**: Provide specific, actionable configuration standards for the most common asset types in [Organization]'s environment.

**Content**:
- Operating system hardening standards (Windows Server, Linux/Unix)
- Network device configuration standards (routers, switches, firewalls)
- Application server standards (web servers, databases, middleware)
- Cloud platform standards (AWS, Azure, GCP)
- Container and orchestration standards (Docker, Kubernetes)
- Mobile device management standards
- References to external standards (CIS Benchmarks, DISA STIGs)

**Primary Audience**: System Administrators, DevOps Engineers, Cloud Architects, Security Engineers

**When to Use**:
- Building new systems (apply baseline during deployment)
- Hardening existing systems (compare current state to standard)
- Defining baselines (use as foundation for organizational baselines)
- Security assessments (verify compliance with standards)
- Incident response (verify if compromised system deviated from standard)

**Update Frequency**: Semi-annually or when major technology changes occur

---

### 5.3.2 Annex B - Change Request Form Template

**Purpose**: Provide a standard template for submitting configuration change requests.

**Content**:
- Change request form structure (all required fields)
- Instructions for completing each field
- Example completed form
- Approval workflow diagram
- Submission process

**Primary Audience**: Anyone submitting configuration change requests (System Administrators, Application Owners, DevOps Engineers, Third-Party Vendors)

**When to Use**:
- Submitting Normal Change requests (not Standard or Emergency)
- Preparing CAB presentations
- Training new staff on change control process

**Update Frequency**: Annually or when change control process changes

---

### 5.3.3 Annex C - Configuration Deviation Procedures

**Purpose**: Define step-by-step procedures for detecting, investigating, and remediating configuration deviations.

**Content**:
- Deviation detection process
- Triage and classification procedures
- Investigation workflow
- Remediation procedures
- Exception request process
- Escalation paths

**Primary Audience**: Configuration Manager, System Administrators, Security Operations Center, IT Operations

**When to Use**:
- Responding to configuration drift alerts
- Investigating unauthorized changes
- Requesting configuration exceptions
- Conducting configuration audits

**Update Frequency**: Annually or when deviation handling process changes

---

### 5.3.4 Annex D - Quick Reference Guide

**Purpose**: Provide a concise, one-page reference for the most common configuration management activities.

**Content**:
- Policy summary
- Decision trees (when to submit change request, who approves, etc.)
- Contact information (Configuration Manager, CAB, Security Team)
- Key procedures in flowchart format
- Frequently asked questions
- Links to detailed documentation

**Primary Audience**: All technical staff

**When to Use**:
- Quick lookups during daily work
- Onboarding new staff
- Refresher for infrequent activities
- Posting in team areas

**Update Frequency**: Annually or when contact information changes

---

## 5.4 How to Use the Annexes

### 5.4.1 Navigation

**Annexes are designed for direct access**, not sequential reading:
- Use table of contents within each annex to jump to relevant section
- Use Ctrl+F / Cmd+F to search for specific technologies or terms
- Bookmark frequently referenced sections

**Cross-Referencing**:
- Main policy sections reference relevant annexes
- Annexes reference main policy for context and authority
- Example: Policy Section 2.4.3.1 (Windows Server Hardening) → Annex A (Windows Server Standards)

---

### 5.4.2 Precedence

**If there is a conflict between main policy and annexes:**
1. Main policy requirements (MUST/SHOULD/MAY) take precedence
2. Annexes provide implementation details and guidance
3. If conflict cannot be resolved, escalate to Configuration Manager and CISO

**Rationale**: Main policy is approved by executive leadership. Annexes are operational guidance that may be updated more frequently by technical teams.

---

### 5.4.3 Customization

**Annexes are intended to be tailored:**
- Annex A standards should be customized to [Organization]'s specific technology stack
- Annex B form template may be adapted to integrate with [Organization]'s change management system
- Annex C procedures should reflect [Organization]'s organizational structure
- Annex D should be updated with [Organization]-specific contact information

**Authorization**: Configuration Manager may update annexes without full policy review, provided:
- Updates do not contradict main policy requirements
- Updates are reviewed by Security Architect (for Annex A) or appropriate subject matter expert
- Updates are communicated to affected personnel
- Updates are documented in version control

---

## 5.5 Annex Maintenance

### 5.5.1 Review Schedule

| Annex | Review Frequency | Review Owner |
|-------|------------------|--------------|
| **A** | Semi-annually | Security Architect + Configuration Manager |
| **B** | Annually | Configuration Manager |
| **C** | Annually | Configuration Manager + SOC Manager |
| **D** | Annually | Configuration Manager |

**Triggered Reviews**: Any annex should be reviewed immediately if:
- New technology is adopted (Annex A)
- Change control process changes (Annex B, C)
- Contact information changes (Annex D)
- Incident reveals gap or error in annex guidance

---

### 5.5.2 Version Control

**Annexes follow the same version control as main policy:**
- Version number (1.0, 1.1, 2.0)
- Document control table
- Change history
- Approval signatures

**Simplified Approval**: Minor annex updates (clarifications, contact updates, reference updates) may use expedited approval:
- Configuration Manager approval (mandatory)
- CISO notification (not requiring signature)
- Communication to affected personnel

**Major Annex Updates** (new standards, process changes) require full approval:
- Configuration Manager + Security Architect review
- CISO approval
- CIO/CTO notification
- Formal communication

---

## 5.6 Annex Access and Distribution

**MUST Requirements**:
- All annexes MUST be published on the same policy portal as main policy documents
- Annexes MUST be clearly labeled and linked from master policy
- Search functionality MUST index annex contents
- Annexes MUST be available to all personnel requiring them

**SHOULD Requirements**:
- Annex A SHOULD be published in multiple formats:
  - PDF for printing
  - Web/HTML for quick reference
  - Machine-readable format (JSON, YAML) for automation tools
- Annex B form SHOULD integrate with change management system
- Annex D SHOULD be printed and posted in IT work areas

---

## 5.7 Related Documents and External References

**Internal References**:
- ISMS-POL-A.8.9: Configuration Management (Master Policy)
- ISMS-POL-A.8.9-S1 through S4: Policy sections
- ISMS-IMP-A.8.9.1 through A.8.9.5: Implementation assessment specifications

**External Standards Referenced in Annexes**:
- **CIS Benchmarks** - Center for Internet Security (https://www.cisecurity.org/cis-benchmarks)
- **DISA STIGs** - Defense Information Systems Agency Security Technical Implementation Guides (https://public.cyber.mil/stigs)
- **NIST Publications** - National Institute of Standards and Technology (https://csrc.nist.gov/publications)
- **Vendor Security Guides** - Microsoft, AWS, Azure, GCP, VMware, Cisco, Red Hat, etc.

**How to Obtain External Standards**:
- CIS Benchmarks: Free download from CIS website (registration required)
- DISA STIGs: Free download from public.cyber.mil
- NIST Publications: Free download from NIST website
- Vendor Guides: Typically available on vendor security portals (may require account)

---

## 5.8 Feedback and Continuous Improvement

**Providing Feedback**:
- Annex errors or ambiguities: Email Configuration Manager
- Suggested improvements: Submit via feedback form or email
- Missing technology standards: Request via Configuration Manager
- Usability issues: Provide input during annual policy review

**Feedback Will Be Used To**:
- Clarify confusing sections
- Add missing technology standards
- Improve navigation and findability
- Enhance templates and examples
- Update contact information

---

## 5.9 Quick Access Guide

**I need to...**

| Task | Annex | Section |
|------|-------|---------|
| Harden a Windows Server | **A** | Windows Server Standards |
| Harden a Linux server | **A** | Linux/Unix Standards |
| Configure a firewall securely | **A** | Firewall Standards |
| Deploy AWS infrastructure | **A** | Cloud Platform Standards - AWS |
| Submit a change request | **B** | Change Request Form Template |
| Respond to configuration drift alert | **C** | Deviation Detection & Triage |
| Request an exception to policy | **C** | Exception Request Process |
| Look up Configuration Manager contact | **D** | Contact Information |
| Understand change approval workflow | **D** | Change Control Flowchart |
| Quickly determine if change needs CAB | **D** | Change Classification Decision Tree |

---

## 5.10 The Feynman Test for Annexes

**Good annex characteristics:**
- ✅ Findable in <30 seconds
- ✅ Actionable (can be used immediately)
- ✅ Specific (no vague "implement security best practices")
- ✅ Up-to-date (reflects current technology)
- ✅ Referenced (people actually use it)

**Bad annex characteristics:**
- ❌ Buried in 200-page document
- ❌ Generic (could apply to any organization)
- ❌ Outdated (references Windows Server 2008)
- ❌ Unused (exists only for auditors)
- ❌ Contradicts main policy

**Question**: Can a system administrator use these annexes to actually do their job better, or are they just audit decoration?

**Answer**: If it's just decoration, rewrite it.

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9: Configuration Management (Master Policy)
- ISMS-POL-A.8.9-S1 through S4: Policy sections
- ISMS-POL-A.8.9-S5.A: Configuration Standards by Asset Type (next)
- ISMS-POL-A.8.9-S5.B: Change Request Form Template
- ISMS-POL-A.8.9-S5.C: Configuration Deviation Procedures
- ISMS-POL-A.8.9-S5.D: Quick Reference Guide

---