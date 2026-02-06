**ISMS-POL-A.5.37 — Documented Operating Procedures**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Documented Operating Procedures |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.37 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.32 (Change Management)
- ISMS-POL-A.5.1-2-6.1-2 (Information Security Policies)
- ISMS-IMP-A.5.37.1-UG/TG (Procedure Inventory Assessment)
- ISMS-IMP-A.5.37.2-UG/TG (Procedure Quality Assessment)
- ISMS-IMP-A.5.37.3-UG/TG (Procedure Review and Update Tracking)
- ISMS-IMP-A.5.37.4-UG/TG (Compliance Dashboard)
- ISO/IEC 27001:2022 Control A.5.37
- ISO/IEC 27001:2022 Clause 7.5 (Documented Information)

---

## Executive Summary

This policy establishes [Organization]'s requirements for documenting and maintaining operating procedures for information processing facilities, ensuring consistent, secure, and auditable operations.

**Scope**: This policy applies to all operating procedures for information processing facilities, systems, applications, and security controls operated by or on behalf of [Organization].

**Purpose**: Define organisational requirements for procedure documentation. This policy establishes WHAT procedures must be documented and WHO is responsible for maintaining them. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.37 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022 and quality management principles. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.5.37**

**ISO/IEC 27001:2022 Annex A.5.37 - Documented Operating Procedures**

> *Operating procedures for information processing facilities should be documented and made available to personnel who need them.*

**Control Objectives**:

- Ensure correct and secure operation of information processing facilities
- Maintain consistent operational practices through documented procedures
- Enable knowledge transfer and business continuity
- Support audit and compliance requirements

**Control Type**: Preventive
**Control Category**: Organisational

**This Policy Addresses**:

- Mandatory documented procedure categories
- Documentation standards and quality requirements
- Accessibility and availability requirements
- Review and maintenance requirements
- Training and competence requirements

## What This Policy Does

This policy:

- **Defines** categories of procedures requiring documentation
- **Establishes** documentation standards and mandatory elements
- **Specifies** review, testing, and maintenance requirements
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define strategic policy documents** (see ISMS-POL-A.5.1-2-6.1-2)
- **Specify change management procedures** (see ISMS-POL-A.8.32)
- **Provide procedure templates** (see ISMS-IMP-A.5.37)
- **Document business processes outside ISMS scope** (unless security-relevant)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite operational changes
- Flexibility for different documentation tools
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All information processing systems (servers, networks, databases, applications)
- All operational procedures (security, system, administrative)
- All environments (production, test, development, DR/BC)
- All personnel operating information processing facilities

**Out of Scope**:

- Strategic policy documents (covered by A.5.1)
- Change management procedures (covered by A.8.32)
- Business process documentation not related to security

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.37, Clause 7.5 - Documented information |
| **ISO/IEC 27002:2022** | Implementation guidance | Operating procedure documentation guidance |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **FINMA** | Swiss regulated financial institution | Documented operational procedures |
| **DORA** | EU financial services entity | ICT operational procedures documented |
| **NIS2** | Essential/important entity (EU) | Security operational procedures |
| **ISO 9001** | Quality certification | Quality management system documentation |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ITIL Service Management documentation standards
- COBIT IT governance framework
- NIST SP 800-53 documentation requirements
- Industry runbook best practices

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent documentation requirements apply where multiple regulations overlap.

---

# Policy Statements

## Documentation Requirements

### Mandatory Documented Procedures

[Organisation] SHALL document operating procedures for:

**Security Operations**:

| Procedure Category | Examples |
|--------------------|----------|
| **Access Management** | User provisioning, access review, emergency access |
| **Incident Response** | Detection, triage, escalation, communication |
| **Vulnerability Management** | Scanning, assessment, remediation |
| **Backup/Recovery** | Backup execution, verification, restoration |
| **Monitoring** | Log review, alert response, escalation |
| **Patch Management** | Assessment, testing, deployment |

**System Operations**:

| Procedure Category | Examples |
|--------------------|----------|
| **Startup/Shutdown** | System startup, graceful shutdown, emergency shutdown |
| **Batch Processing** | Job scheduling, monitoring, failure handling |
| **Error Handling** | Error detection, logging, escalation |
| **Media Handling** | Storage, transport, disposal |
| **System Maintenance** | Routine maintenance, housekeeping |

**Administrative Operations**:

| Procedure Category | Examples |
|--------------------|----------|
| **User Support** | Request handling, problem resolution |
| **Change Implementation** | Pre-change, execution, post-change verification |
| **Disaster Recovery** | DR invocation, recovery, return to normal |

### Documentation Standards

All operating procedures SHALL include:

**Mandatory Elements**:

| Element | Requirement |
|---------|-------------|
| **Document ID** | Unique identifier following naming convention |
| **Title** | Clear, descriptive title |
| **Version** | Version number and date |
| **Owner** | Designated procedure owner |
| **Approval** | Approver name and date |
| **Purpose** | Why the procedure exists |
| **Scope** | What the procedure covers |
| **Prerequisites** | Required conditions, access, tools |
| **Steps** | Sequential, numbered steps |
| **Verification** | How to confirm successful completion |
| **Rollback** | Recovery steps if procedure fails |
| **References** | Related documents, contacts |

**Quality Requirements**:

- Written clearly for target audience skill level
- Sufficient detail for unfamiliar operator to execute
- Free of ambiguity and assumptions
- Tested before production use
- Includes expected outputs/results at key steps

### Procedure Categories and Ownership

| Category | Owner | Approver | Review Frequency |
|----------|-------|----------|------------------|
| **Security Procedures** | CISO | CIO (or Executive Management for high-impact security runbooks) | Annual |
| **Infrastructure Procedures** | IT Operations Manager | CIO | Annual |
| **Application Procedures** | Application Owner | IT Operations Manager | Annual |
| **Support Procedures** | Service Desk Manager | IT Operations Manager | Annual |

## Accessibility and Availability

### Procedure Access

[Organisation] SHALL ensure procedures are available to authorised personnel:

**Accessibility Requirements**:

- Procedures SHALL be stored in the Authoritative Procedure Repository: [Repository Name/URL]. This repository is the single source of truth for operating procedures. Local copies and duplicates are prohibited except approved offline emergency copies as defined below
- Access controlled based on need-to-know and job function
- Searchable by title, keyword, system, process
- Available offline for critical/emergency procedures (printed runbooks)
- Mobile access for on-call personnel

**Availability Requirements**:

| Procedure Type | Availability Requirement |
|----------------|-------------------------|
| **Emergency/DR** | Printed copies + offline digital, tested quarterly |
| **Critical Operations** | Available 24/7 with redundant access |
| **Standard Operations** | Available 24/7 where supporting customer-facing infrastructure; otherwise business hours minimum |
| **Reference** | Available on demand |

**Emergency/Offline Procedure Pack**: For critical services, [Organisation] SHALL maintain an offline pack containing at minimum: DR invocation, break-glass/emergency access, core network access, and backup restore procedures for critical systems. The pack SHALL be stored at designated secure location(s) (documented in ISMS-IMP-A.5.37). Custodian: IT Operations Manager. Currency SHALL be verified quarterly with a recorded checklist stored in the Evidence Register; verification includes confirming version alignment with authoritative repository.

### Version Control

[Organisation] SHALL maintain version control for all procedures:

- Single authoritative version (no duplicate copies in personal folders)
- Previous versions archived (not deleted) for audit trail
- Version history documenting changes
- Notification of updates to affected personnel
- Grace period for transition to new versions

## Review and Maintenance

### Scheduled Reviews

[Organisation] SHALL review operating procedures regularly:

| Review Type | Frequency | Scope |
|-------------|-----------|-------|
| **Scheduled Review** | Annual minimum | All procedures |
| **Post-Incident Review** | After relevant incident | Affected procedures |
| **Change-Triggered Review** | After system changes | Affected procedures |
| **Regulatory Review** | After regulatory changes | Affected procedures |

**Review Activities**:

- Verify accuracy against current systems and processes
- Update for technology changes, personnel changes
- Improve based on user feedback and lessons learned
- Align with current security requirements
- Update references to related documents

### Procedure Testing

[Organisation] SHALL test critical procedures:

| Procedure Type | Testing Requirement |
|----------------|---------------------|
| **Disaster Recovery** | Annual full test, quarterly tabletop |
| **Incident Response** | Semi-annual exercise |
| **Backup/Restore** | Monthly restore test |
| **Emergency Access** | Annual break-glass test |
| **Critical Operations** | After significant changes |

**Testing Documentation**:

- Test date and participants
- Test scenario
- Results (success, partial, failure)
- Issues identified
- Remediation actions

## Training and Competence

### Operator Training

[Organisation] SHALL ensure personnel are trained on relevant procedures:

**Training Requirements**:

- New personnel trained before performing procedures independently
- Training records maintained
- Competence verified (observation, assessment, sign-off)
- Refresher training when procedures significantly updated
- Cross-training for critical procedures (no single points of failure)

**Competence Evidence**:

- Training completion records
- Supervisor sign-off on competence
- Observation records for critical procedures
- Regular assessment for safety-critical operations

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Procedure Documentation Responsibilities |
|------|-----------------------------------------|
| **Executive Management** | Approve procedure documentation policy, resource allocation |
| **CISO** | Security procedure standards, approval of security procedures |
| **CIO** | Overall operational procedure framework |
| **IT Operations Manager** | Infrastructure procedure ownership, coordination |
| **Procedure Owners** | Accuracy, currency, and quality of owned procedures |
| **Quality Manager** | Procedure template standards, review tracking |
| **All Technical Personnel** | Follow procedures, report issues, suggest improvements |

## Escalation Path

- Procedure clarification: Operator → Procedure Owner → IT Operations Manager
- Procedure quality issues: Quality Manager → CISO/CIO
- Outdated procedure identified: Operator → Procedure Owner → Quality Manager

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Procedure Inventory Audit | Annual | Quality Manager | Complete inventory with currency status |
| Procedure Quality Assessment | Annual | Quality Manager | Sample review against standards |
| Review Completion Tracking | Quarterly | Quality Manager | Review due dates, completion status |
| Procedure Test Results | Per testing schedule | Procedure Owners | Test documentation |

**Governance Metrics**:

- Procedures within review period (target: 100%)
- Procedures meeting quality standards (target: >95%)
- Critical procedures with trained personnel (target: 100%)
- Procedure test pass rate (target: >95%)
- Outstanding procedure gaps (target: 0 critical)

**Metric Sources**: Metrics are derived from Procedure Inventory Workbook (ISMS-IMP-A.5.37.1 outputs) generated weekly; Quality Manager reviews quarterly; dashboard output provided as input to Clause 9.3 management review. Internal audit sampling (Clause 9.2) uses procedure criticality ratings from the inventory to select samples.

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Audit findings, technology changes, operational failures, regulatory updates
- **Reviewers**: CISO, CIO, IT Operations Manager, Quality Manager
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- New systems: Temporary exception (max 90 days) for procedures pending documentation
- Legacy systems: Exception with risk acceptance if documentation cost exceeds value
- Third-party systems: Reference to vendor documentation acceptable if comprehensive

**Exception Process**:

1. Document business justification
2. Risk assessment of undocumented procedure
3. CISO/CIO approval
4. Time-limited approval (maximum 90 days, renewable)
5. Compensating controls documented

**Not Permissible**:

- Critical procedures without documentation
- Security procedures without CISO approval
- Production procedures without testing

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

**Exception Record Requirements**: Exception entries SHALL include: procedure/system scope, business justification, risk owner, risk assessment reference, compensating controls, approver, start date, expiry date, and closure evidence. Exceptions that increase information security risk SHALL be linked to the ISMS risk register and approved via documented risk acceptance. Expired exceptions not renewed or closed require immediate remediation or formal extension.

## Corrective Action Linkage

Nonconformities related to this policy (e.g., outdated procedures, missing documentation, failed procedure tests, training gaps) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Procedure gaps identified in risk assessment
- Undocumented procedures represent operational risk
- Risk treatment plans address procedure documentation

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.5.37 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **Clause 7.5** | ISMS documented information requirements |
| **A.5.1** | Policies - Procedures implement policy requirements |
| **A.8.32** | Change Management - Procedures updated via change process |
| **A.6.3** | Training - Personnel trained on procedures |
| **A.5.24-28** | Incident Management - Incident procedures documented |

**Stacked Control Integration**:

A.5.37 (Documented Operating Procedures) stacks with related controls:

| Stacked Control | Integration Point | A.5.37 Contribution |
|-----------------|-------------------|---------------------|
| **Clause 7.5** (Documented Information) | ISMS documentation | A.5.37 extends to operational procedures |
| **A.5.24-28** (Incident Management) | Incident procedures | A.5.37 defines documentation standards; A.5.24-28 defines incident process |
| **A.8.32** (Change Management) | Procedure updates | A.5.37 defines standards; A.8.32 controls changes |

Assessment of A.5.37 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.37 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.37.1-UG/TG** | Procedure Inventory Assessment | Identify and track all procedures |
| **ISMS-IMP-A.5.37.2-UG/TG** | Procedure Quality Assessment | Verify documentation standards |
| **ISMS-IMP-A.5.37.3-UG/TG** | Review Tracking Assessment | Monitor review compliance |
| **ISMS-IMP-A.5.37.4-UG/TG** | Compliance Dashboard | Consolidated reporting |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.5.37 v1.0)
- Recorded approval by CISO, CIO, Executive Management
- Evidence of communication to relevant roles
- Mandatory procedure categories defined (Documentation Requirements)
- Documentation standards specified (Documentation Standards)
- Accessibility requirements defined (Accessibility and Availability)
- Review and testing requirements documented (Review and Maintenance)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Procedure inventory with metadata and currency status
- Sample procedures meeting documentation standards
- Review completion records
- Procedure test results (DR tests, restore tests, incident exercises)
- Training records for procedure operators
- Version control evidence from repository
- Accessibility verification (offline procedures, mobile access)

---

# Definitions

| Term | Definition |
|------|------------|
| **Operating Procedure** | Documented set of instructions for performing a specific operational task |
| **Runbook** | Collection of procedures for operating a system or service |
| **Playbook** | Collection of procedures for responding to specific scenarios (e.g., security incidents) |
| **Procedure Owner** | Individual accountable for accuracy and currency of a procedure |
| **Standard Operating Procedure (SOP)** | Formal procedure document with approval and version control |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for documented operating procedures. Implementation procedures are documented in ISMS-IMP-A.5.37 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
