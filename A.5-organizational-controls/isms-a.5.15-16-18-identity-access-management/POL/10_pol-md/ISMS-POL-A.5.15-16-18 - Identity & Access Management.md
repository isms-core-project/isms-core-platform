**ISMS-POL-A.5.15-16-18 - Identity & Access Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Identity & Access Management Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.15-16-18 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- HR Integration: Chief Human Resources Officer (CHRO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)


**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.15-16-18 (Implementation Guidance Suite)
- ISMS-POL-A.8.2-3-5 (Authentication & Privileged Access)
- ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18


---

## Executive Summary

This policy establishes [Organization]'s requirements for identity and access management controls to ensure appropriate access governance throughout the complete identity lifecycle in accordance with ISO/IEC 27001:2022 Controls A.5.15, A.5.16, and A.5.18.

**Purpose**: Define organizational requirements for identity and access management governance. This policy establishes WHAT IAM controls are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.15-16-18.

**Scope**: This policy applies to all user identities (employees, contractors, vendors, service accounts), all identity systems, and all access types regardless of deployment model or technology.

**Combined Control Approach**: These three controls are implemented as a unified framework because they address inseparable aspects of identity and access governance.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00, including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Controls

**A.5.15 - Access Control**: Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.

**A.5.16 - Identity Management**: The full life cycle of identities should be managed.

**A.5.18 - Access Rights**: Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy and rules for access control.

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **User Types** | Employees, contractors, vendors, service accounts, shared accounts (with approval), emergency accounts |
| **Identity Systems** | Active Directory, Azure AD/Entra ID, Okta, Google Workspace, LDAP, and any identity system used by [Organization] |
| **Access Types** | Application, system, data, network, and administrative/privileged access |
| **Personnel** | IAM Team, Security Team, HR Team, IT Operations, Managers, System Owners, all employees |

**This policy does NOT apply to**:

- Physical access control systems (covered in A.7.2)
- Authentication mechanisms (covered in A.8.5)
- Privileged access management implementation (covered in A.8.2)


## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key IAM Requirements |
|------------|----------------------|
| **Swiss nDSG** | Article 8 - Technical and organizational measures for access control |
| **EU GDPR** | Article 32 - Security of processing including access controls |
| **ISO/IEC 27001:2022** | Controls A.5.15, A.5.16, A.5.18 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

- **FINMA**: If [Organization] holds FINMA license (Circular 2023/1 Margin 50-62)
- **DORA**: If [Organization] is EU financial entity (Articles 6, 28-30)
- **NIS2**: If [Organization] is essential or important entity (Article 21)
- **PCI DSS**: If [Organization] processes payment card data (Requirements 7, 8)


Compliance determination per ISMS-POL-00 (Regulatory Applicability Framework).

---

# Policy Statements

## Access Control Requirements (A.5.15)

### Access Control Principles

[Organization] SHALL implement access controls based on the following principles:

| Principle | Requirement |
|-----------|-------------|
| **Least Privilege** | Users granted minimum access required for job function |
| **Need-to-Know** | Access restricted to documented business need |
| **Segregation of Duties** | Conflicting responsibilities separated to prevent fraud/error |
| **Defense in Depth** | Multiple layers of access control implemented |
| **Deny by Default** | Access denied unless explicitly granted with approval |

### Access Classification

[Organization] SHALL classify access based on:

| Dimension | Classifications |
|-----------|----------------|
| **User Type** | Employee, Contractor (time-bound), Vendor (external), Service Account (non-human), Shared (exceptional), Emergency (break-glass) |
| **System Criticality** | Critical, High, Medium, Low |
| **Data Sensitivity** | Restricted, Confidential, Internal, Public |
| **Access Level** | Read, Write, Admin, Privileged |

Classification criteria defined in ISMS-IMP-A.5.15-16-18.1.

### Business Justification and Approval

All access requests SHALL include documented business justification with approval authority based on access type:

| Access Type | Approval Authority |
|-------------|-------------------|
| **Standard User Access** | Direct manager |
| **Sensitive System Access** | System owner + Manager |
| **Confidential/Restricted Data** | Data owner + CISO |
| **Privileged/Admin Access** | CISO + CIO |
| **Third-Party Vendor Access** | Business sponsor + CISO |
| **Shared Account** (exceptional) | CISO with compensating controls |

### Segregation of Duties

[Organisation] SHALL maintain a Segregation of Duties matrix identifying incompatible role combinations (documented in ISMS-IMP-A.5.15-16-18.3 Appendix A or [GRC Platform SoD Module]). SoD violations require CISO-approved exceptions with compensating controls (logged in exception register per Section 4.2).

SoD violation detection SHALL occur monthly (automated via SoD check script) with reporting to Security Team (output in IAM-SoD-Workbook-[YYYY-MM]). Violations SHALL be remediated within 30 business days or logged as exceptions with CISO approval.

### HR Integration

Access control SHALL integrate with HR lifecycle events:

| HR Event | Access Action | Timeline |
|----------|--------------|----------|
| **New Hire** | Trigger joiner process | Access ready by start date |
| **Role Change** | Trigger mover process | Within 2 business days |
| **Termination** | Trigger leaver process | Immediate (for cause) or same business day |
| **Contract End** | Remove contractor access | On contract end date |

HR system designated as authoritative source for identity lifecycle events.

---

## Identity Management Requirements (A.5.16)

### Identity Lifecycle Framework

[Organization] SHALL manage identities through standardized lifecycle processes:

| Process | Trigger | Timeline | Accountability |
|---------|---------|----------|----------------|
| **Joiner** | HR notification of new hire/contractor | Access ready by start date | HR triggers, IAM Team creates, IT provisions |
| **Mover** | HR notification of role change | Within 2 business days | HR triggers, Manager approves, IAM Team updates |
| **Leaver** | HR notification of termination | Immediate to same business day | HR triggers, IAM Team disables, IT verifies |

Detailed procedures documented in ISMS-IMP-A.5.15-16-18.2.

### Account Type Requirements

| Account Type | Requirements |
|--------------|-------------|
| **Employee** | Permanent until termination, individual accountability |
| **Contractor/Vendor** | Time-bound with mandatory expiration (system-enforced via account expiration date set at provisioning), internal sponsor required (renewed quarterly with sponsor approval or auto-deprovisioned) |
| **Service Account** | Documented owner (maintained in [IAM system/GRC platform]), password rotation (quarterly minimum, verified via automated scan or manual attestation), privileged controls per A.8.2, non-compliance flagged in monthly IAM assessment |
| **Shared Account** | CISO approval required (documented in exception register per Section 4.2), compensating controls mandatory (individual usage logging via [SIEM/audit system], privileged access monitoring per A.8.2, quarterly usage review by CISO), strongly discouraged (target: zero shared accounts or formal CISO-approved exception with business justification for each), time-bound approval (annual revalidation required) |
| **Emergency/Break-Glass** | Dormant until disaster scenario, dual authorisation, usage triggers alert (tested semi-annually per BCP procedures, test usage documented) |

### Orphaned Account Management

[Organization] SHALL detect and remediate orphaned accounts:

- **Detection**: Monthly cross-reference of identity systems with HR system
- **Remediation**: Investigation, notification, disable, delete sequence within 30 days
- **Exceptions**: CISO approval required with documented justification


---

## Access Rights Requirements (A.5.18)

### Access Rights Assignment

[Organization] SHALL assign access rights through:

- Documented request and approval workflow
- Role-based access control (RBAC) as preferred method
- Business justification documented for all access grants
- Audit trail maintained (requester, approver, timestamp, justification)


**Provisioning Timeliness**:

| Request Type | SLA |
|--------------|-----|
| **Standard Access** | Within 2 business days |
| **Sensitive Access** | Within 5 business days |
| **Emergency Access** | Within 4 hours |

### Role-Based Access Control

[Organisation] SHALL implement RBAC:

- **Role Catalog**: Maintained by IAM Team in [GRC Platform/IAM System], updated within 10 business days of organisational changes
- **Role Ownership**: Each role assigned to business owner (documented in role definition)
- **Role Lifecycle**: New roles require IAM Team approval, role modifications require business owner approval, deprecated roles archived (not deleted) for audit trail
- Roles mapped to specific access rights (access entitlement matrix documented in ISMS-IMP-A.5.15-16-18.3)
- Target: 80% or greater users assigned via roles versus direct access
- Annual role review by business owners (tracked in [GRC Platform], completion required by Q1 annually)


### Access Review and Recertification

[Organization] SHALL review access rights periodically:

| Classification | Frequency | Reviewer |
|----------------|-----------|----------|
| **Critical Systems / Privileged Access** | Quarterly | CISO + Security Team |
| **High-Risk Systems / Confidential Data** | Semi-Annual | System owners + Managers |
| **Standard Systems / Internal Data** | Annual | Managers |
| **Third-Party/Vendor Access** | Quarterly | Business sponsor + CISO |

Third-party access reviews include validation that contractual agreement remains active and access remains necessary per A.5.20.

Reviewers SHALL certify access is appropriate or request removal. Inappropriate access SHALL be removed within 5 business days.

**Access Review Follow-Up**:

If inappropriate access cannot be removed within 5 business days due to technical constraints:

- Manager SHALL document justification and compensating controls in [GRC platform]
- CISO approval required for exceptions >10 business days
- Outstanding removals escalated to CIO after 15 business days
- Prolonged non-compliance (>30 days) flagged as security incident per A.5.24-27

### Access Removal

[Organization] SHALL remove access promptly:

| Trigger | Timeline |
|---------|----------|
| **Termination for cause** | Immediate (within 1 hour) |
| **Voluntary termination** | Same business day |
| **Role change** | Within 2 business days (remove previous role access) |
| **Access review finding** | Within 5 business days |
| **Security incident** | Immediate |

### Privilege Creep Prevention

[Organization] SHALL detect and remediate privilege creep through:

**Detection Methodology**:

| Detection Method | Frequency | Tool/Process | Owner |
|------------------|-----------|--------------|-------|
| **Role-Based Variance Analysis** | Quarterly | [IAM System/GRC Platform] compares actual access vs. role entitlements | IAM Team |
| **Mover Process Audit** | Monthly | Review of role changes to verify previous access removed | Security Team |
| **Access Entitlement Review** | Semi-Annual | Manager review of all direct (non-role) access grants | Managers |
| **Privileged Access Audit** | Quarterly | Analysis of privileged access grants against documented need | CISO |

**Detection Triggers**:

- User has >20% more access entitlements than role definition (flagged for review)
- User retains access from previous role >30 days after mover event
- User has >3 direct access grants outside of role-based assignments
- Service account has access beyond documented scope

**Remediation Process**:

1. Excess access identified and logged in [GRC platform/IAM system]
2. Manager notified with 5 business days to justify or approve removal
3. Unjustified access removed within 10 business days of identification
4. Repeated privilege creep (>2 occurrences) triggers process improvement review

**Reporting**: Privilege creep metrics included in monthly IAM Governance Dashboard (count of findings, average remediation time, repeat offenders by department)


---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Overall IAM program effectiveness, policy approval, resource allocation |
| **CISO** | IAM policy implementation and compliance, exception approval, quarterly metrics review |
| **CIO** | IAM technical infrastructure, technology selection, IT resource allocation |
| **CHRO** | HR system as authoritative identity source, joiner/mover/leaver event triggers |
| **Security Team** | Policy development, compliance monitoring, incident investigation, assessments |
| **IAM Team** | Identity lifecycle processes, identity system maintenance, orphaned account detection |
| **HR Team** | Joiner/mover/leaver notifications, accurate employee data maintenance |
| **IT Operations** | Access provisioning/deprovisioning, technical implementation |
| **Managers** | Access approval for direct reports, access reviews, termination notification |
| **System Owners** | Access requirements definition, system-specific access reviews, approval for sensitive systems |
| **Internal Audit** | IAM control effectiveness verification, compliance testing |
| **All Personnel** | Request access only with business need, use access appropriately, report suspicious activity |

Detailed RACI matrix documented in ISMS-IMP-A.5.15-16-18.1.

---

# Governance & Compliance

## Assessment Framework

[Organisation] SHALL verify IAM control effectiveness through:

| Assessment | Frequency | Owner | Evidence Location |
|------------|-----------|-------|-------------------|
| User Inventory & Lifecycle Compliance | Monthly | IAM Team | IAM-Workbook-[YYYY-MM] (automated) |
| Access Rights Matrix | Monthly | IAM Team | [GRC Platform/IAM System export] |
| Access Review Results | Quarterly | Security Team | [Ticketing System], quarterly summary to CISO |
| Role Compliance & SoD | Quarterly | IAM Team | IAM-SoD-Workbook-[YYYY-MM] (automated) |
| IAM Governance Dashboard | Monthly | Security Team | [Business Intelligence tool/SharePoint] |

**Evidence Generation and Storage**:

- User Inventory & Lifecycle Compliance: Generated by Python script, output stored in IAM-Workbook-[YYYY-MM]
- Access Rights Matrix: Maintained in [GRC Platform/IAM system], exported monthly for Security Team review
- Access Review Results: Tracked in [Ticketing System], quarterly summary report to CISO documenting completion rate and inappropriate access removal
- Role Compliance & SoD: Generated by Python script, violations logged in exception register, output in IAM-SoD-Workbook-[YYYY-MM]
- IAM Governance Dashboard: Updated monthly by Security Team with KPIs (see Governance Metrics below)

All assessment evidence SHALL be retained for minimum 24 months per A.5.33 (Protection of Records).

**Failure Mode Detection**:

- **Missed Access Reviews**: IAM Team tracks review completion in [GRC platform], escalates overdue reviews to CISO after 10 business days
- **Orphaned Accounts Not Detected**: Security Team samples monthly orphaned account reports for quality assurance (10% sample minimum)
- **SoD Violations Not Remediated**: Exception register tracks open SoD violations, quarterly review by CISO flags stale items (>90 days without progress)
- **Provisioning/Deprovisioning SLA Breaches**: [Ticketing system] automatically flags SLA violations, monthly report to CIO with root cause analysis for recurring breaches
- **Service Account Password Age Non-Compliance**: Automated scan flags accounts with passwords >90 days old, report to IAM Team for remediation within 15 business days

Control failure events SHALL be logged as incidents per ISMS-POL-A.5.24-27 (Incident Management) when they create security risk.

**Gap Remediation Tracking**:

IAM assessment findings (orphaned accounts, access review deficiencies, SoD violations, provisioning delays, service account non-compliance) SHALL be:

- Logged in [central gap register/GRC platform] within 5 business days of identification
- Assigned to accountable owner (IAM Team, Manager, System Owner per finding type)
- Tracked with target remediation dates based on risk:
  - Critical (immediate security risk): 5 business days
  - High (control failure): 15 business days
  - Medium (control weakness): 30 business days
  - Low (optimisation opportunity): 90 business days
- Reviewed monthly by Security Team for closure verification
- Escalated to CISO if remediation is overdue by >30 days beyond target date

**IAM Governance Metrics (Monthly Dashboard)**:

- Orphaned account count and average remediation timeline (target: <10 accounts, <30 days to remediate)
- Access review completion rate by type (target: 100% within review period)
- Provisioning/deprovisioning SLA compliance rate (target: >95%)
- RBAC adoption rate (percentage of users assigned via roles vs. direct access, target: >80%)
- SoD violation count and exception approval status (target: <5 open violations, all with CISO-approved exceptions)
- Service account password age compliance rate (target: >95% rotated within 90 days)
- IAM gap remediation status (open findings by age and risk level)

Metrics reviewed monthly by Security Team, quarterly by CISO, incorporated into management review per Clause 9.3.

Assessment procedures documented in ISMS-IMP-A.5.15-16-18.5.

## Exception Management

IAM policy exceptions require:

- Documented business justification
- Security Team risk assessment
- CISO approval with compensating controls
- Documentation in exception register
- Annual review for continued necessity


Exception request procedures documented in ISMS-IMP-A.5.15-16-18.1.

## Incident Response

IAM-related incidents (account compromise, orphaned account exploitation, privilege escalation) SHALL be managed per ISMS-POL-A.5.24-27 (Incident Management).

Emergency deprovisioning SHALL occur within 1 hour for security incidents.

## Policy Review

This policy SHALL be reviewed:

- **Annually** (mandatory)
- **When triggered** by regulatory changes, organizational changes, technology changes, audit findings, risk assessment changes, or incident lessons learned


Policy changes require CISO approval; major revisions require Executive Management approval.

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.5.15 - Access Control** | Applicable | Section 2.1, ISMS-IMP-A.5.15-16-18.1 |
| **A.5.16 - Identity Management** | Applicable | Section 2.2, ISMS-IMP-A.5.15-16-18.2 |
| **A.5.18 - Access Rights** | Applicable | Section 2.3, ISMS-IMP-A.5.15-16-18.3/4 |

## Related Controls

- **A.8.2** (Privileged Access Rights): IAM defines privileged users, A.8.2 implements PAM
- **A.8.5** (Secure Authentication): IAM creates identities, A.8.5 authenticates them
- **A.5.24-27** (Incident Management): Account compromise incidents managed per incident framework


## Implementation Resources

| Document | Purpose |
|----------|---------|
| **ISMS-IMP-A.5.15-16-18.1** | Access Control Governance |
| **ISMS-IMP-A.5.15-16-18.2** | Identity Lifecycle Process |
| **ISMS-IMP-A.5.15-16-18.3** | Role Definition and Assignment |
| **ISMS-IMP-A.5.15-16-18.4** | Access Review Process |
| **ISMS-IMP-A.5.15-16-18.5** | IAM Assessment Procedures |

---

# Definitions

| Term | Definition |
|------|------------|
| **Identity** | Digital representation of user (person, service, device) with unique identifier |
| **Access Control** | Security technique regulating who can view or use resources |
| **RBAC** | Access control model where permissions assigned to roles rather than individuals |
| **Least Privilege** | Principle requiring minimum access necessary for job function |
| **Segregation of Duties** | Practice of dividing critical tasks to prevent fraud and error |
| **Joiner Process** | Onboarding of new users including account creation and access provisioning |
| **Mover Process** | Handling of user role changes including access adjustment |
| **Leaver Process** | Offboarding including account disablement and access removal |
| **Orphaned Account** | Account without valid business owner requiring remediation |
| **Privilege Creep** | Accumulation of excess access rights over time during role changes |
| **Service Account** | Non-human account used for automated processes |
| **Break-Glass Account** | Emergency privileged account for disaster scenarios |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Human Resources Officer (CHRO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.5.15-16-18 v1.0)
- ✅ Approval signatures from CISO, CIO, CHRO, Legal/Compliance Officer, Executive Management (Approval Record)
- ✅ Access control principles and classification framework defined (Section 2.1)
- ✅ Identity lifecycle framework (Joiner/Mover/Leaver) documented (Section 2.2)
- ✅ Account type requirements specified (employee, contractor, service, shared, emergency) (Section 2.2)
- ✅ Access rights assignment and RBAC framework documented (Section 2.3)
- ✅ Access review frequency and criteria specified (Section 2.3)
- ✅ Segregation of Duties requirements defined (Section 2.1)
- ✅ Privilege creep detection methodology documented (Section 2.3)
- ✅ Roles and responsibilities assigned with RACI reference (Section 3)
- ✅ Governance framework with assessment schedule defined (Section 4)
- ✅ Integration with related controls documented (Section 5)

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- **User Inventory Reports**: Monthly IAM-Workbook-[YYYY-MM] showing active identities, account types, and lifecycle status
- **Access Review Completion Records**: Quarterly/semi-annual/annual review logs in [Ticketing System] showing reviewer, decision, timestamp for all in-scope access
- **Joiner/Mover/Leaver Process Records**: HR-triggered workflow tickets demonstrating SLA compliance (access ready by start date, 2-day mover, same-day leaver)
- **Orphaned Account Remediation Logs**: Monthly detection reports with investigation, disable, delete timestamps showing <30 day remediation
- **Segregation of Duties Reports**: IAM-SoD-Workbook-[YYYY-MM] showing SoD checks, violations identified, and exception approvals
- **Privilege Creep Analysis**: Quarterly variance reports comparing actual vs. role entitlements, with remediation tracking
- **IAM Governance Dashboard**: Monthly metrics (orphan count, review completion %, SLA compliance, RBAC adoption %, SoD violations, password compliance)
- **Exception Register**: Documented exceptions with business justification, CISO approval, compensating controls, and annual revalidation
- **Service Account Compliance**: Quarterly attestation showing documented owners and password rotation compliance (>95% within 90 days)
- **Access Removal Verification**: Deprovisioning audit trail showing termination-to-disable timestamps meeting policy SLAs
- **Third-Party Access Reviews**: Quarterly sponsor attestations confirming continued business need and active contractual agreements
- **Assessment Workbook Outputs**: Completed ISMS-IMP-A.5.15-16-18.5 assessment workbooks demonstrating control effectiveness testing

## Clarification on Compliance Evidence

This policy establishes **identity and access management governance requirements** covering access control principles, identity lifecycle processes, and access rights management for all user types and systems.

It does **NOT** establish:
- **Physical access controls** (addressed in ISMS-POL-A.7.2 - Physical Entry)
- **Authentication mechanisms** (addressed in ISMS-POL-A.8.5 - Secure Authentication)
- **Privileged access management implementation** (addressed in ISMS-POL-A.8.2 - Privileged Access Rights)
- **Specific identity system configurations** (organisational technology decisions, documented in IMP procedures)

The boundary is: **This policy defines WHO gets WHAT access, WHEN, and HOW it is governed** → Technical policies (A.8.x) define HOW access is authenticated and privileged access is protected → Implementation procedures (IMP) document system-specific configurations.

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.5.15-16-18.*

<!-- QA_VERIFIED: 2026-02-02 -->
