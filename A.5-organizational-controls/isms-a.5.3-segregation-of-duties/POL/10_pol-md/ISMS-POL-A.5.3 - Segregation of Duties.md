**ISMS-POL-A.5.3 — Segregation of Duties**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Segregation of Duties |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.3 |
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
- Secondary: Chief Financial Officer (CFO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.15-16-18 (Identity & Access Management)
- ISMS-POL-A.8.2-3-5 (Authentication & Privileged Access)
- ISMS-IMP-A.5.3 (Implementation Guidance)
- ISO/IEC 27001:2022 Control A.5.3

---

## Executive Summary

This policy establishes [Organization]'s requirements for segregation of duties to reduce the risk of fraud, error, and unauthorized activities by ensuring that conflicting responsibilities are separated across different individuals or systems.

**Scope**: This policy applies to all business processes, information systems, and activities where conflicting duties could lead to fraud, error, or security breaches if performed by a single individual.

**Purpose**: Define organizational requirements for segregation of duties. This policy establishes WHAT segregation is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.3.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss CO, ISO/IEC 27001:2022, and EU GDPR. Conditional sector-specific requirements (FINMA, SOX, PCI DSS) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.5.3**

**ISO/IEC 27001:2022 Annex A.5.3 - Segregation of Duties**

> *Conflicting duties and conflicting areas of responsibility should be segregated.*

**Control Objective**: Reduce the risk of fraud, error, and circumvention of information security controls by separating conflicting duties.

**Control Type**: Preventive
**Control Category**: Organizational

**This Policy Addresses**:

- Identification of conflicting duties requiring segregation
- Segregation principles and requirements by process type
- Compensating controls for small teams
- Exception handling and approval processes
- Monitoring and verification requirements

## What This Policy Does

This policy:

- **Defines** conflicting duty combinations that must be segregated
- **Establishes** minimum segregation standards for critical processes
- **Specifies** compensating controls when segregation cannot be achieved
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.5.3 Implementation Guidance)
- **Define specific duty assignment matrices** (organization-specific, maintained operationally)
- **Provide system configuration procedures** (see ISMS-IMP-A.5.3 Technical Controls)
- **Replace risk assessment** (segregation requirements informed by [Organization]'s risk treatment)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite organizational structure changes
- Flexibility for different system implementations
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All business processes involving financial transactions, approvals, or sensitive operations
- All information systems where conflicting duties could enable fraud or error
- All personnel (employees, contractors, third parties) performing segregated duties
- All access control systems enforcing duty segregation

**Out of Scope**:

- Non-sensitive operational processes with adequate supervision
- Automated processes with built-in segregation controls (where segregation is achieved through automation, the control configuration and audit trails SHALL be validated at least annually and upon material change by Internal Audit or the control owner)
- Temporary emergency access (covered by exception management)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss CO Art. 728** | All Swiss entities | Internal control system including duty segregation |
| **ISO/IEC 27001:2022** | Certification scope | Control A.5.3 - Segregation of duties |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Segregation Requirements |
|-----------|-------------------|--------------------------|
| **EU GDPR Art. 32** | Processing EU personal data | Appropriate technical and organisational measures |
| **FINMA** | Swiss regulated financial institution | Strict segregation in trading, settlement, risk management |
| **SOX Section 404** | US-listed company | Financial controls segregation, internal control attestation |
| **PCI DSS v4.0** | Payment card processing | Requirement 6.4.2 - Separation of development/test/production |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- COSO Internal Control Framework
- ISACA COBIT (Control Objectives for IT)
- NIST SP 800-53 (Access Enforcement AC-5)
- IIA International Standards (Internal Audit segregation)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Segregation Principles

All business processes and information systems SHALL implement segregation of duties where:

**Risk-Based Requirement**:

- Activities involve financial transactions **greater than CHF 10,000**, unless a lower threshold is defined in a department-specific procedure approved by the CFO and CISO based on risk
- Access to sensitive or classified information is required
- System administration privileges are exercised
- Security controls can be bypassed or disabled
- Audit logs or evidence can be modified or deleted

**Minimum Segregation Standards**:

| Process Type | Minimum Segregation |
|-------------|---------------------|
| Financial transactions >CHF 10,000 | Initiator ≠ Approver |
| System access requests | Requestor ≠ Approver ≠ Provisioner |
| Change management | Developer ≠ Tester ≠ Deployer |
| Security monitoring | Administrator ≠ Log Reviewer |
| Backup/Recovery | Operator ≠ Verifier |

## Conflicting Duties Identification

The following duty combinations SHALL be segregated:

**Financial Processes**:

- Initiating payments AND approving payments
- Creating vendor records AND processing payments to vendors
- Recording transactions AND reconciling accounts
- Managing payroll AND approving payroll disbursements

**IT Operations**:

- Developing code AND deploying to production
- Administering systems AND reviewing system logs
- Creating user accounts AND approving access requests
- Managing backups AND authorizing data restoration
- Configuring security controls AND auditing security effectiveness

**Procurement & Contracts**:

- Selecting vendors AND negotiating contracts
- Approving purchases AND receiving goods/services
- Managing contracts AND verifying contract compliance

**Human Resources**:

- Hiring decisions AND background check verification
- Setting compensation AND approving payroll
- Terminating access AND confirming access revocation

## Small Team Considerations

Where segregation cannot be achieved due to limited personnel:

**Compensating Controls Required**:

1. Enhanced monitoring and logging of all activities
2. Management review of all transactions (minimum weekly)
3. Periodic independent review (quarterly minimum)
4. Automated alerts for unusual patterns
5. Post-transaction audit trails with tamper protection

**Documentation Requirement**: Formal risk acceptance by Executive Management with documented compensating controls and review schedule.

**Re-evaluation Trigger**: Compensating control arrangements SHALL be re-evaluated when:

- Additional personnel are hired
- Organisational structure changes
- Risk assessment identifies increased exposure
- Audit findings indicate control weaknesses

## Technical Segregation Controls

Information systems supporting segregated processes SHALL implement:

**Access Control Requirements**:

- Role-based access control (RBAC) enforcing duty separation
- Mutual exclusion constraints preventing conflicting role assignments
- Workflow controls requiring different approvers at each stage
- Privileged access management preventing self-approval

**Audit Trail Requirements**:

- Immutable logging of all segregated activities
- Clear identification of actors at each process stage
- Timestamp and action recording for all approvals
- Protection against log modification or deletion

**Immutable Logging Definition**: Immutable logging SHALL be achieved using approved logging platforms and configurations as defined in ISMS-IMP-A.5.3 and the Logging control (ISMS-POL-A.8.15). Acceptable implementations include: WORM storage, restricted administrator access with separate log reviewer, retention locks, and centralised log aggregation with integrity verification.

## Exception Management

Exceptions to segregation requirements require:

**Emergency Exceptions** (≤24 hours):

- Verbal authorization from Department Head + CISO
- Documented within 4 hours of exception use
- Full review within 24 hours of exception end
- Compensating controls active during exception period

**Planned Exceptions** (>24 hours):

- Formal exception request with business justification
- Risk assessment of exception impact
- Compensating controls documented and approved
- CISO and Executive Management approval
- Maximum duration: 90 days (renewable with re-assessment)

**Not Permissible**:

- Permanent exceptions to financial segregation requirements
- Exceptions that eliminate audit trail capabilities
- Self-approval of segregation exceptions

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

**Exception Record Minimum Content**: Each exception record SHALL include: affected system(s), identity/role(s) granted exception, time window (start/end), approving authority with evidence, compensating controls active during exception, post-exception review outcome, and closure date.

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Segregation Responsibilities |
|------|------------------------------|
| **Executive Management (GL)** | Approve segregation policy, accept residual risks, approve compensating controls |
| **CISO** | Define segregation requirements, monitor compliance, approve exceptions |
| **CFO** | Financial process segregation oversight, approve financial control exceptions |
| **Department Heads** | Implement segregation within departments, identify conflicts, request exceptions |
| **HR** | Maintain organisational structure supporting segregation, role assignments |
| **IT Operations** | Implement technical controls, RBAC configuration, access monitoring |
| **Internal Audit** | Verify segregation effectiveness, report violations, assess compensating controls |

## Escalation Path

- Segregation conflicts identified: Department Head → CISO → Executive Management
- Exception requests: Requestor → Department Head → CISO → Executive Management
- Violation detected: Immediate notification to CISO and Internal Audit

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Segregation matrix review | Annual | CISO | Updated duty matrix |
| Access rights analysis | Quarterly | IT Operations | Access reports |
| Compensating controls review | Quarterly | Internal Audit | Effectiveness assessment |
| Exception register review | Monthly | CISO | Exception log |

**Compliance Monitoring**:

- Access right reviews against duty segregation matrix
- Transaction pattern analysis for segregation violations
- Workflow approval chain verification
- Compensating control effectiveness review

**Governance Metrics**:

- Number of segregation conflicts identified
- Time to remediate conflicts
- Exception requests and approvals
- Compensating control effectiveness scores

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Organisational restructuring, audit findings, regulatory updates, security incidents
- **Reviewers**: CISO, CFO, Internal Audit, HR Director
- **Approval**: Executive Management

## Corrective Action Linkage

Nonconformities related to this policy (e.g., segregation violations, unreviewed exceptions, compensating control failures) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Segregation requirements informed by fraud and error risk assessment
- Compensating controls documented in risk treatment plans
- Residual risks from limited segregation formally accepted

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.5.3 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.15-16-18** | Identity & Access Management - RBAC enforces duty segregation |
| **A.8.2-3-5** | Authentication & Privileged Access - Privileged access segregation |
| **A.8.15** | Logging - Audit trails for segregated activities |

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.3):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.3** | Segregation of Duties Implementation Guide | Duty matrices, technical controls, monitoring procedures |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.5.3 v1.0)
- Recorded approval by CISO, CFO, Executive Management
- Evidence of communication to relevant roles
- Conflicting duties identification documented (Conflicting Duties Identification)
- Segregation principles and minimum standards defined (Segregation Principles)
- Compensating controls requirements specified (Small Team Considerations)
- Exception management process documented (Exception Management)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Duty segregation matrix showing conflicting role combinations
- Access rights reports demonstrating segregation enforcement
- Sample workflow approvals showing multi-party control
- Exception register with approvals and compensating controls
- Quarterly segregation analysis reports
- Internal audit reports on segregation compliance
- Evidence of compensating control monitoring (where segregation not achievable)
- Training records for staff on segregation requirements
- Incident reports related to segregation violations (if any)

---

# Definitions

| Term | Definition |
|------|------------|
| **Segregation of Duties (SoD)** | The practice of dividing tasks and privileges among multiple individuals to prevent any single person from having complete control over a critical process |
| **Conflicting Duties** | Responsibilities that, if combined, would allow an individual to commit and conceal errors or fraud |
| **Compensating Control** | An alternative control measure implemented when primary segregation cannot be achieved |
| **Mutual Exclusion** | A technical control preventing a user from being assigned conflicting roles simultaneously |
| **Four-Eyes Principle** | A requirement that critical actions require approval or verification by at least two authorized individuals |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Financial Officer (CFO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for segregation of duties. Implementation procedures are documented in ISMS-IMP-A.5.3.*

<!-- QA_VERIFIED: 2026-02-04 -->
