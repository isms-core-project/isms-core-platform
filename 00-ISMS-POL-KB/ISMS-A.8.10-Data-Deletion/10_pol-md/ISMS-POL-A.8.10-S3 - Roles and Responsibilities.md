# ISMS-POL-A.8.10-S3
## Information Deletion - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.10-S3
**Title**: Information Deletion - Roles and Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Data Protection Officer / HR | Initial roles and responsibilities definition |

**Review Cycle**: Annually (or upon organizational structure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- HR Review: Human Resources Director
- Legal Review: Data Protection Officer (DPO)

**Distribution**: All staff (awareness), management (accountability), DPO, HR, IT operations  
**Related Documents**: ISMS-POL-A.8.10 (Master Policy), ISMS-POL-A.8.10-S2.1 through S2.4 (Requirements)

---

## 3.1 Purpose and Scope

This section defines **roles, responsibilities, and accountabilities** for information deletion activities throughout the data lifecycle. Clear role definition ensures accountability, prevents "someone else's job" syndrome, and enables effective implementation of deletion requirements.

**In Scope**: Organizational roles, decision rights, escalation paths, RACI matrix  
**Primary Stakeholders**: All staff, management, DPO, CISO  
**Key Principle**: "Accountability cannot be delegated, but responsibility can be shared."

---

## 3.2 RACI Framework Overview

### 3.2.1 RACI Definitions

Organizations **SHALL** use the RACI model to define deletion roles:

| Letter | Role | Definition | Typical Count |
|--------|------|------------|---------------|
| **R** | Responsible | Person(s) who perform the work | Multiple OK |
| **A** | Accountable | Person ultimately answerable (owns decision) | **ONE only** |
| **C** | Consulted | Subject matter experts providing input | Multiple OK |
| **I** | Informed | People kept updated on progress | Multiple OK |

**Critical Rule**: Every activity has **exactly ONE Accountable** person. Multiple Accountable = nobody is actually accountable.

### 3.2.2 Application to Deletion Activities

For information deletion, RACI applies to:

- **Policy creation and maintenance** (this policy)
- **Retention schedule definition** (deciding how long to keep data)
- **Deletion trigger identification** (recognizing when deletion is required)
- **Deletion execution** (actually performing deletion)
- **Verification and evidence collection** (proving deletion occurred)
- **Data subject request handling** (GDPR Article 17 requests)
- **Third-party deletion coordination** (managing cloud/vendor deletions)
- **Audit and compliance reporting** (demonstrating compliance)

---

## 3.3 Core Roles

### 3.3.1 Data Protection Officer (DPO)

**Accountability**: Overall compliance with data protection laws (GDPR, Swiss FADP) including deletion requirements

**Responsibilities**:
- **Policy governance**: Maintain and update information deletion policies
- **Data subject requests**: Oversee handling of GDPR Article 17 erasure requests
- **Compliance monitoring**: Verify deletion activities comply with legal requirements
- **Regulatory liaison**: Communicate with data protection authorities
- **Training oversight**: Ensure staff understand deletion obligations
- **Exception approval**: Approve deviations from standard deletion procedures (for personal data)
- **Incident management**: Lead response to deletion-related data protection incidents
- **Audit coordination**: Facilitate internal/external audits of deletion processes

**Authority**:
- **Approve/deny** data subject erasure requests
- **Approve/deny** exceptions to retention schedules (personal data)
- **Escalate** non-compliance to senior management
- **Directly report** to highest management level (GDPR Article 38)

**Reporting**: Reports to CEO/Board (independent from IT/Operations)

**Qualifications**: 
- Expert knowledge of data protection law (GDPR, Swiss FADP)
- Understanding of technical deletion methods
- Legal or compliance background preferred
- CIPP/E, CIPM, or equivalent certification recommended

**Note**: The DPO is **the** critical role for A.8.10 due to GDPR Article 17 (right to erasure) requirements. Organizations without a DPO must designate equivalent role.

### 3.3.2 Chief Information Security Officer (CISO)

**Accountability**: Information security aspects of deletion (ensuring deleted data cannot be recovered by unauthorized parties)

**Responsibilities**:
- **Security policy ownership**: Maintain ISMS-POL-A.8.10 master policy
- **Deletion method approval**: Approve technical deletion methods and tools
- **Security verification**: Ensure deletion methods are cryptographically/physically secure
- **Vendor security assessment**: Evaluate third-party deletion capabilities
- **Incident response**: Lead security incidents involving deletion failures
- **Access control**: Ensure only authorized personnel perform deletions
- **Cryptographic erasure**: Oversee encryption key management for crypto-erase
- **Risk management**: Assess and accept residual risks related to deletion

**Authority**:
- **Approve/deny** deletion tools and methods
- **Approve/deny** exceptions to deletion procedures (security reasons)
- **Mandate** security controls for deletion processes
- **Halt** deletion activities if security risks identified

**Reporting**: Reports to CIO or CEO

**Qualifications**:
- CISSP, CISM, or equivalent certification
- Deep understanding of data sanitization (NIST SP 800-88)
- Experience with cryptographic controls

### 3.3.3 Data Owner (Business Department Head)

**Accountability**: Business decisions regarding data retention and deletion for specific data categories

**Responsibilities**:
- **Retention schedule definition**: Define retention periods for data under their ownership
- **Business justification**: Document business/legal need for retention
- **Deletion approval**: Approve deletion of business-critical data
- **Exception requests**: Request exceptions to retention schedules when justified
- **Data classification**: Classify data sensitivity (drives deletion method selection)
- **Budget allocation**: Fund deletion activities for their data
- **User communication**: Inform business users of deletion activities

**Authority**:
- **Define** retention periods (within legal/policy constraints)
- **Approve** deletion of data they own
- **Request** exceptions to standard procedures

**Reporting**: Reports to business unit leadership (CFO, COO, CHRO, etc.)

**Examples**:
- **CFO** = Data Owner for financial records
- **CHRO** = Data Owner for employee/HR data
- **CMO** = Data Owner for marketing/customer data
- **CTO** = Data Owner for technical/product data

**Note**: Data Owners are **business roles**, not IT. They decide WHAT and WHEN to delete; IT decides HOW.

### 3.3.4 IT Operations / System Administrators

**Accountability**: Technical execution of deletion activities

**Responsibilities**:
- **Execute deletions**: Perform deletion operations on systems/storage
- **Tool operation**: Operate deletion tools (DBAN, cloud APIs, shredders)
- **Logging**: Generate deletion logs and evidence
- **Verification**: Conduct technical verification (forensic testing, API checks)
- **Backup management**: Delete data from backup systems
- **Incident reporting**: Report deletion failures to InfoSec/DPO
- **Procedure compliance**: Follow documented deletion procedures
- **Automation**: Implement and maintain automated deletion systems

**Authority**:
- **Execute** approved deletion requests
- **Escalate** technical issues preventing deletion
- **Recommend** process improvements

**Reporting**: Reports to IT Director/CIO

**Qualifications**:
- System administration experience
- Understanding of storage technologies (HDD, SSD, cloud)
- Familiarity with deletion tools

### 3.3.5 Records Manager / Information Governance

**Accountability**: Retention schedule maintenance and compliance

**Responsibilities**:
- **Retention schedule**: Maintain master retention schedule
- **Policy updates**: Update retention schedules per regulatory changes
- **Deletion coordination**: Coordinate scheduled deletions across organization
- **Legal hold management**: Implement and release legal holds
- **Compliance tracking**: Monitor adherence to retention schedules
- **Training**: Educate staff on retention requirements
- **Documentation**: Maintain deletion evidence repository

**Authority**:
- **Update** retention schedules (with Data Owner approval)
- **Implement** legal holds (with Legal approval)
- **Trigger** scheduled deletions

**Reporting**: Reports to DPO or Legal/Compliance

**Note**: In smaller organizations, this role may be combined with DPO or Legal.

### 3.3.6 Legal Counsel

**Accountability**: Legal compliance and litigation hold management

**Responsibilities**:
- **Legal hold authority**: Issue and release legal holds (litigation, investigations)
- **Retention requirement validation**: Confirm legal basis for retention periods
- **Regulatory interpretation**: Advise on applicable deletion laws
- **Contract review**: Review deletion clauses in vendor contracts
- **Data subject request review**: Assess legal grounds to deny erasure requests
- **Incident legal support**: Provide legal guidance on deletion incidents
- **Regulatory liaison**: Communicate with regulators (with DPO) on legal matters

**Authority**:
- **Issue** legal holds (suspends normal deletion)
- **Release** legal holds (resumes deletion)
- **Approve/deny** retention exceptions (legal requirements)
- **Advise** on legal risks of deletion decisions

**Reporting**: Reports to General Counsel or CEO

**Qualifications**:
- Licensed attorney/legal counsel
- Knowledge of data protection, evidence preservation, regulatory compliance

### 3.3.7 Internal Audit

**Accountability**: Independent verification of deletion program effectiveness

**Responsibilities**:
- **Audit planning**: Develop annual deletion audit program
- **Audit execution**: Conduct compliance audits (process, evidence, technical)
- **Finding reporting**: Document non-conformances and recommendations
- **Remediation tracking**: Verify corrective actions implemented
- **Management reporting**: Report audit results to Board/Audit Committee
- **External audit coordination**: Support external auditors and regulators

**Authority**:
- **Access** all deletion records and systems
- **Interview** any staff regarding deletion practices
- **Report** findings directly to Audit Committee (independent of management)

**Reporting**: Reports to Audit Committee (Board)

**Note**: Internal Audit is **independent** — does not perform deletions, only audits them.

### 3.3.8 Vendor/Procurement Manager

**Accountability**: Vendor contract management for deletion obligations

**Responsibilities**:
- **Contract negotiation**: Ensure deletion clauses in vendor contracts
- **Vendor assessment**: Evaluate vendor deletion capabilities (pre-engagement)
- **Vendor monitoring**: Track vendor deletion performance (SLAs, certificates)
- **Vendor audit coordination**: Arrange vendor deletion audits
- **Contract termination**: Manage data deletion during service termination
- **Certificate collection**: Obtain Certificates of Destruction from vendors
- **Escalation**: Escalate vendor deletion failures to DPO/CISO

**Authority**:
- **Negotiate** deletion terms in contracts
- **Withhold payment** for deletion SLA breaches (if contractually permitted)
- **Terminate** vendor relationships for persistent deletion failures

**Reporting**: Reports to CFO or COO

### 3.3.9 Asset Manager

**Accountability**: Physical asset tracking for media deletion

**Responsibilities**:
- **Asset inventory**: Track all storage media (HDDs, tapes, laptops, servers)
- **Chain of custody**: Document media transfers to deletion vendors
- **Secure storage**: Store media awaiting deletion in secure area
- **Destruction coordination**: Schedule media destruction with vendors
- **Certificate validation**: Verify destruction certificates match inventory
- **Asset disposal**: Coordinate end-of-life disposal (recycling, landfill)

**Authority**:
- **Track** assets from deployment to destruction
- **Release** assets to destruction vendors
- **Report** discrepancies (missing assets, incomplete destruction)

**Reporting**: Reports to IT Director or Operations

### 3.3.10 All Employees

**Responsibilities**:
- **Awareness**: Understand deletion policies applicable to their role
- **Compliance**: Follow deletion procedures (don't circumvent)
- **Data minimization**: Avoid hoarding unnecessary data
- **Reporting**: Report suspected retention violations or deletion failures
- **Training participation**: Complete mandatory deletion awareness training

**Authority**:
- **Escalate** concerns to manager, DPO, or CISO

**Note**: While all employees have responsibilities, they are not Accountable for deletion program success.

---

## 3.4 RACI Matrix - Information Deletion Activities

Organizations **SHALL** use the following RACI matrix to clarify accountability:

| Activity | DPO | CISO | Data Owner | IT Ops | Records Mgr | Legal | Audit | Procurement | Asset Mgr | Employees |
|----------|-----|------|------------|--------|-------------|-------|-------|-------------|-----------|-----------|
| **Policy Creation & Maintenance** | A | C | C | I | C | C | I | I | I | I |
| **Retention Schedule Definition** | C | C | A | I | R | C | I | I | I | I |
| **Deletion Tool Selection** | C | A | I | R | I | I | I | I | I | - |
| **Scheduled Deletion Execution** | I | I | C | R/A | R | I | I | I | I | - |
| **Data Subject Erasure Request** | A/R | C | I | R | C | C | I | I | I | I |
| **Legal Hold Implementation** | C | I | I | R | R | A | I | I | I | I |
| **Legal Hold Release** | C | I | I | R | R | A | I | I | I | - |
| **Third-Party Deletion Coordination** | C | C | I | R | I | I | I | A | I | - |
| **Physical Media Destruction** | I | C | I | R | I | I | I | I | A/R | - |
| **Deletion Verification** | C | C | I | A/R | I | I | I | I | I | - |
| **Certificate Collection** | C | I | I | I | R | I | I | A | R | - |
| **Deletion Logging** | I | C | I | A/R | C | I | I | I | I | - |
| **Evidence Retention** | C | C | I | R | A | I | I | I | I | - |
| **Exception Approval (Personal Data)** | A | C | C | I | I | C | I | I | I | I |
| **Exception Approval (Security)** | C | A | C | I | I | I | I | I | I | I |
| **Deletion Incident Response** | A | C | I | R | C | C | I | I | I | I |
| **Compliance Reporting** | A | C | C | I | R | I | I | I | I | - |
| **Internal Audit** | I | I | I | I | I | I | A/R | I | I | I |
| **Regulatory Inquiry Response** | A | C | I | I | R | C | I | I | I | - |
| **Training & Awareness** | A | C | I | I | C | I | I | I | I | R |
| **Vendor Deletion SLA Monitoring** | C | C | I | I | I | I | I | A/R | I | - |

**Legend**:
- **R** = Responsible (does the work)
- **A** = Accountable (owns the decision, only ONE per activity)
- **C** = Consulted (provides input)
- **I** = Informed (kept updated)
- **-** = Not involved

**Notes**:
- **A/R** indicates the same person/role is both Accountable and Responsible
- Activities with **no A** must have one assigned by the organization
- Multiple **R** is common (shared execution)

---

## 3.5 Decision Rights

### 3.5.1 Deletion Approval Authority

Organizations **SHALL** define approval authority based on data sensitivity and deletion type:

| Deletion Type | Data Sensitivity | Required Approver(s) | Timeline |
|---------------|------------------|---------------------|----------|
| **Scheduled/Automated** | Low/Medium | IT Operations (via automation) | Immediate |
| **Scheduled/Automated** | High/Restricted | IT Ops + Data Owner notification | Immediate |
| **Manual (routine)** | Low/Medium | IT Operations | <24 hours |
| **Manual (business-critical)** | High | Data Owner + IT Operations | <5 days |
| **Data Subject Request** | Any (personal data) | DPO | <30 days (GDPR) |
| **Legal Hold Release** | Any | Legal Counsel | Per hold release |
| **Third-Party/Cloud** | Any | Procurement (contracts) + IT Ops (execution) | <30 days |
| **Emergency/Incident** | Any | CISO + DPO | <24 hours |
| **Exception to Policy** | Personal data | DPO + CISO | <14 days |
| **Exception to Policy** | Non-personal | CISO (or Data Owner) | <14 days |

### 3.5.2 Escalation Paths

Organizations **SHALL** define escalation procedures:

**Deletion Failure Escalation**:
1. **Level 1** (0-24 hours): IT Operations → IT Manager
2. **Level 2** (24-48 hours): IT Manager → CISO + DPO
3. **Level 3** (48-72 hours): CISO/DPO → CIO + General Counsel
4. **Level 4** (>72 hours): CIO/Counsel → CEO (if regulatory/legal impact)

**Data Subject Request Escalation** (approaching 30-day GDPR deadline):
1. **Day 20**: DPO → CISO (status review)
2. **Day 25**: DPO → General Counsel (if complex/denial considered)
3. **Day 28**: DPO → CEO (if deadline will be missed)

**Vendor Deletion Failure Escalation**:
1. **Level 1**: Procurement → Vendor Account Manager
2. **Level 2**: Procurement + DPO → Vendor Executive Sponsor
3. **Level 3**: DPO + CISO + Legal → Vendor Executive + Contract Enforcement

---

## 3.6 Segregation of Duties

### 3.6.1 Mandatory Segregation

To prevent conflicts of interest and fraud, organizations **SHALL** segregate:

| Function 1 | Function 2 | Reason for Segregation | Exception Process |
|------------|------------|------------------------|-------------------|
| **Deletion execution** | **Deletion verification** | Prevent falsified verification | Small orgs: independent sampling by Audit |
| **Legal hold issuance** | **Legal hold release** | Ensure proper legal review | Must be same person (Legal) with DPO oversight |
| **Retention schedule definition** | **Retention schedule audit** | Independence of audit function | N/A - never combine |
| **Data subject request receipt** | **Data subject request fulfillment verification** | Prevent incomplete deletions | DPO oversight of both acceptable |
| **Vendor selection** | **Vendor performance monitoring** | Prevent favoritism | Procurement does both, but Audit reviews |

### 3.6.2 Small Organization Considerations

For organizations with limited staff, **minimum viable segregation**:

- **DPO** must be independent from IT Operations (can be external/part-time)
- **Audit function** must be independent from deletion execution (can be external)
- **Legal hold authority** must be separate from routine deletion authority

**Compensating controls** when full segregation is infeasible:
- Increased audit frequency (quarterly vs. annual)
- External audit review
- Management oversight (CEO/Board review of deletion logs)
- Enhanced logging and monitoring

---

## 3.7 Training and Competency Requirements

### 3.7.1 Role-Specific Training

Organizations **SHALL** provide role-specific training:

| Role | Training Topics | Frequency | Assessment |
|------|----------------|-----------|------------|
| **DPO** | GDPR Art. 17, deletion verification, incident response | Annual + updates | Certification maintenance |
| **CISO** | NIST SP 800-88, crypto erasure, forensic verification | Annual | Knowledge test |
| **Data Owners** | Retention requirements, deletion triggers, exceptions | Annual | Acknowledgment |
| **IT Operations** | Deletion tools, procedures, logging, troubleshooting | Onboarding + annual | Practical assessment |
| **Records Manager** | Retention schedules, legal holds, compliance tracking | Annual | Knowledge test |
| **Legal** | GDPR, eDiscovery, legal holds, deletion compliance | Annual | CLE credits (if applicable) |
| **Procurement** | Contract clauses, vendor assessment, SLA monitoring | Biennial | Acknowledgment |
| **All Employees** | Deletion awareness, data minimization, reporting | Annual | Completion certificate |

### 3.7.2 Competency Assessment

Organizations **SHOULD** assess competency through:

- **Knowledge tests**: For DPO, CISO, Records Manager (80% pass rate)
- **Practical assessments**: For IT Operations (perform test deletion)
- **Case studies**: For Legal, DPO (analyze deletion scenarios)
- **Completion certificates**: For general staff (awareness training)

**Remediation**: Staff failing competency assessment receive additional training and re-assessment within 30 days.

---

## 3.8 Succession Planning and Business Continuity

### 3.8.1 Critical Role Backup

Organizations **SHALL** designate backup/deputy for critical roles:

| Primary Role | Backup/Deputy | Trigger for Activation |
|--------------|---------------|------------------------|
| **DPO** | Deputy DPO or external DPO service | Absence >5 days, data subject requests |
| **CISO** | Deputy CISO or InfoSec Manager | Absence >3 days, security incidents |
| **Legal Counsel** | Alternate attorney or external counsel | Legal hold decisions, absence >5 days |
| **IT Operations Lead** | Senior System Admin or external MSP | Absence >2 days, scheduled deletions |

**Documentation**: Backup personnel have **read access** to deletion systems/logs even when not actively performing duties (maintains awareness).

### 3.8.2 Knowledge Transfer

Organizations **SHALL** maintain:

- **Role handbooks**: Step-by-step procedures for each role
- **Cross-training**: Primary and backup personnel trained together
- **Documentation repository**: Centralized access to policies, procedures, contacts
- **Emergency contacts**: 24/7 contact list for deletion incidents

---

## 3.9 Performance Evaluation and Accountability

### 3.9.1 Individual Performance Metrics

Organizations **SHOULD** include deletion responsibilities in performance evaluations:

| Role | Performance Metric | Target |
|------|-------------------|--------|
| **DPO** | Data subject requests handled within deadline | 100% |
| **DPO** | Policy review and updates completed on schedule | 100% |
| **CISO** | Deletion tool assessments completed | Annual |
| **Data Owners** | Retention schedules reviewed annually | 100% |
| **IT Operations** | Deletion success rate | >99% |
| **IT Operations** | Deletion logs complete and accurate | >95% |
| **Records Manager** | Legal holds implemented within 2 days | 100% |
| **Procurement** | Vendor certificates collected | 100% |

### 3.9.2 Consequences of Non-Performance

Organizations **SHALL** address persistent non-performance:

**Progressive Discipline**:
1. **First occurrence**: Coaching and additional training
2. **Second occurrence**: Formal performance improvement plan (30-60 days)
3. **Third occurrence**: Reassignment or termination (per HR policy)

**Immediate Actions** for:
- Intentional data retention violations (disciplinary action, potential termination)
- Falsification of deletion evidence (termination, legal referral)
- Unauthorized disclosure of deletion activities (disciplinary action)

**Note**: Accountability must be real. If roles have responsibilities without consequences for failure, the program will not succeed.

---

## 3.10 Continuous Improvement

### 3.10.1 Role Evolution

Organizations **SHALL** review roles annually and update when:

- **Organizational restructuring** occurs (mergers, divestitures, reorganizations)
- **New technologies** are adopted (cloud providers, deletion tools)
- **Regulatory changes** impose new responsibilities (GDPR updates, new laws)
- **Audit findings** identify gaps in accountability

### 3.10.2 Feedback Mechanisms

Organizations **SHOULD** collect feedback from:

- **Role incumbents**: "Is this role definition realistic and achievable?"
- **Cross-functional teams**: "Are handoffs and interfaces clear?"
- **Audit findings**: "Are accountabilities driving compliance?"
- **Incident reviews**: "Did role clarity help or hinder response?"

**Action**: Feedback reviewed by DPO + CISO, resulting in role definition updates within 60 days.

---

**END OF DOCUMENT**

*"Accountability is the glue that ties commitment to results."* — Bob Proctor (and every auditor who's ever asked "But WHO is responsible for this?")