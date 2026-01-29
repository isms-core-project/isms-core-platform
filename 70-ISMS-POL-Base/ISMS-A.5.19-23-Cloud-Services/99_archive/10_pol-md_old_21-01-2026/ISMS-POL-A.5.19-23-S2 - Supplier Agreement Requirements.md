# ISMS-POL-A.5.19-23-S2 — Supplier Agreement Requirements
## Control A.5.20: Addressing Information Security in Supplier Agreements

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Supplier Agreement Requirements |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S2 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.20 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Procurement: Procurement Director
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-IMP-A.5.23-2 (Vendor Due Diligence & Contracts)
- ISO/IEC 27001:2022 Control A.5.20
- ISO/IEC 27036-2 (Requirements)
- GDPR Article 28 (Processor requirements)

---

## 1. Purpose

This section defines the mandatory information security requirements that shall be included in supplier agreements. It ensures that security obligations are contractually binding and enforceable throughout the supplier relationship.

**Control Objective (ISO 27002:2022):**
> "Relevant information security requirements shall be established and agreed with each supplier based on the type of supplier relationship."

---

## 2. Scope

### 2.1 Applicable Agreements

This section applies to all formal agreements with suppliers including:

| Agreement Type | Description |
|----------------|-------------|
| Master Service Agreements (MSA) | Umbrella contracts governing relationship |
| Service Level Agreements (SLA) | Performance and availability commitments |
| Data Processing Agreements (DPA) | Personal data handling (GDPR, nFADP) |
| Non-Disclosure Agreements (NDA) | Confidentiality commitments |
| Statements of Work (SOW) | Specific project or service scope |
| Software License Agreements | Terms for software use |
| Cloud Service Agreements | Terms for cloud service consumption |

### 2.2 Agreement Review Responsibility

| Supplier Level | Agreement Review By |
|----------------|---------------------|
| Level 1 (Critical) | Legal + Security + Business Owner + Procurement |
| Level 2 (High) | Legal + Security + Procurement |
| Level 3 (Medium) | Procurement + Security (if data access) |
| Level 4 (Low) | Procurement (standard terms acceptable) |

---

## 3. Mandatory Security Clauses

### 3.1 Clause Requirements by Supplier Level

| Security Clause | L1 | L2 | L3 | L4 |
|-----------------|----|----|----|----|
| Confidentiality obligations | ✓ | ✓ | ✓ | ✓ |
| Data protection compliance | ✓ | ✓ | ✓ | — |
| Security controls commitment | ✓ | ✓ | ✓ | — |
| Incident notification | ✓ | ✓ | ✓ | — |
| Audit rights | ✓ | ✓ | — | — |
| Subcontractor restrictions | ✓ | ✓ | — | — |
| Business continuity requirements | ✓ | ✓ | — | — |
| Data return/destruction | ✓ | ✓ | ✓ | — |
| Liability provisions | ✓ | ✓ | ✓ | — |
| Termination rights | ✓ | ✓ | ✓ | ✓ |
| Insurance requirements | ✓ | ✓ | — | — |

### 3.2 Confidentiality Obligations

**Required Elements:**

| Element | Requirement |
|---------|-------------|
| Definition of confidential information | Clear scope of what is protected |
| Permitted use | Limited to service delivery only |
| Permitted disclosure | Need-to-know basis, named parties |
| Protection standard | "Reasonable care" minimum, specify controls |
| Duration | Survives termination (minimum 3 years, or perpetual for trade secrets) |
| Return/destruction | Upon termination or request |
| Exceptions | Publicly available, independently developed, legally required |

### 3.3 Data Protection Compliance

**Required Elements:**

| Element | Requirement |
|---------|-------------|
| Roles definition | Controller vs. Processor designation |
| Processing purpose | Limited to specified purposes |
| Data categories | Types of personal data processed |
| Data subjects | Categories of individuals |
| Processing location | Geographic restrictions if applicable |
| Technical measures | Security controls for personal data |
| Subprocessor rules | Prior approval, flow-down requirements |
| Data subject rights | Support for access, deletion, portability |
| Breach notification | Timeframes and procedures |
| Audit cooperation | Support for regulatory audits |

**Note:** For Swiss/EU operations, ensure DPA meets GDPR Article 28 and nFADP requirements.

### 3.4 Security Controls Commitment

**Required Contract Language:**

> "Supplier shall implement and maintain administrative, technical, and physical security controls appropriate to the classification of data accessed, consistent with industry standards and the requirements specified in Appendix [X] (Security Requirements)."

**Security Requirements Appendix shall specify:**

| Control Domain | Requirements |
|----------------|--------------|
| Access management | Authentication, authorization, access logging |
| Encryption | In-transit and at-rest requirements |
| Network security | Segmentation, firewall, monitoring |
| Endpoint security | Malware protection, patching |
| Personnel security | Background checks, training, termination |
| Physical security | Facility controls (if applicable) |
| Incident management | Detection, response, reporting |
| Change management | Controlled changes, rollback capability |

---

## 4. Incident Notification Requirements

### 4.1 Notification Timeframes

| Incident Type | Notification Deadline | Notification To |
|---------------|----------------------|-----------------|
| Confirmed data breach | Within 24 hours of confirmation | ISO + Business Owner |
| Suspected data breach | Within 48 hours of detection | ISO |
| Security incident (non-breach) | Within 72 hours | Security Team |
| Service disruption (critical) | Within 1 hour | IT Operations + Business Owner |
| Service disruption (non-critical) | Within 24 hours | IT Operations |

### 4.2 Notification Content Requirements

Initial notification shall include (at minimum):

- Date and time of incident discovery
- Nature of the incident
- Data/systems potentially affected
- Initial containment actions taken
- Designated incident contact

Follow-up notification shall include:

- Root cause analysis
- Complete impact assessment
- Remediation actions taken
- Preventive measures implemented
- Timeline of events

### 4.3 Required Contract Language

> "Supplier shall notify [Organization] without undue delay, and in no event later than [24/48/72] hours after becoming aware of any Security Incident affecting Organization's data or systems. Supplier shall cooperate fully with Organization's investigation and provide all reasonably requested information."

---

## 5. Audit Rights

### 5.1 Audit Rights by Level

| Supplier Level | Audit Rights Required |
|----------------|----------------------|
| Level 1 | Full audit rights (on-site or remote) |
| Level 2 | Audit rights or third-party report acceptance |
| Level 3 | Third-party report acceptance |
| Level 4 | Not required |

### 5.2 Audit Rights Clause Elements

**For Level 1 Suppliers:**

| Element | Requirement |
|---------|-------------|
| Scope | Security controls, processes, facilities |
| Frequency | Annual minimum, additional upon incident |
| Notice | Reasonable notice (14-30 days), immediate for incidents |
| Auditor | Organization or appointed third party |
| Cost | Supplier bears cost for cause-based audits |
| Cooperation | Access to personnel, records, systems |
| Findings | Remediation timeline for identified issues |

**Alternative for Level 2 Suppliers:**

> "Supplier shall, upon request, provide copies of current third-party audit reports (SOC 2 Type II, ISO 27001 certification, or equivalent) and evidence of remediation for any identified findings."

### 5.3 Third-Party Report Acceptance

Acceptable alternatives to direct audit:

| Report Type | Validity | Scope Requirement |
|-------------|----------|-------------------|
| SOC 2 Type II | 12 months | Covers services provided |
| ISO 27001 Certificate | Valid + surveillance | Scope includes relevant services |
| Penetration Test Report | 12 months | Covers relevant systems |
| Vulnerability Assessment | 6 months | Covers relevant infrastructure |

---

## 6. Subcontractor Requirements

### 6.1 Subcontractor Restrictions

**Level 1 & 2 Suppliers:**

| Requirement | Description |
|-------------|-------------|
| Prior approval | Written approval before engaging subcontractors with data access |
| Notification | Inform organization of subcontractor changes |
| Flow-down | Security requirements must apply to subcontractors |
| Liability | Supplier remains liable for subcontractor actions |
| Register | Maintain list of subcontractors with data access |
| Objection right | Organization may object to specific subcontractors |

### 6.2 Required Contract Language

> "Supplier shall not engage any subcontractor to process Organization's data without prior written approval. Supplier shall ensure that any approved subcontractor is bound by obligations no less protective than those in this Agreement. Supplier remains fully liable for acts and omissions of its subcontractors."

---

## 7. Business Continuity Requirements

### 7.1 BC Requirements by Level

| Requirement | Level 1 | Level 2 | Level 3-4 |
|-------------|---------|---------|-----------|
| Documented BC/DR plan | ✓ Required | ✓ Required | — |
| Annual BC/DR testing | ✓ Required | ✓ Recommended | — |
| Recovery time objective (RTO) | ✓ Defined in SLA | ✓ Defined in SLA | — |
| Recovery point objective (RPO) | ✓ Defined in SLA | ✓ Defined in SLA | — |
| Geographic redundancy | ✓ Risk-based | — | — |
| Test results sharing | ✓ Upon request | ✓ Upon request | — |

### 7.2 Service Level Requirements

**SLA Elements for Critical/High Suppliers:**

| Element | Description |
|---------|-------------|
| Availability target | Percentage uptime commitment |
| Measurement period | Monthly, quarterly |
| Exclusions | Planned maintenance, force majeure |
| Service credits | Remedies for failure to meet SLA |
| Escalation process | Notification tiers and timeframes |
| Reporting | Regular performance reports |

---

## 8. Data Return and Destruction

### 8.1 End-of-Contract Requirements

| Requirement | Description |
|-------------|-------------|
| Data return | Complete export in usable format |
| Return format | Industry-standard, documented format |
| Return timeline | Within 30 days of termination |
| Transition support | Reasonable assistance for migration |
| Data destruction | Secure deletion after return confirmation |
| Destruction certificate | Written confirmation of destruction |
| Retention exception | Only if legally required, with notification |

### 8.2 Required Contract Language

> "Upon termination or expiration of this Agreement, Supplier shall (at Organization's election) return or securely destroy all Organization data within thirty (30) days. Supplier shall provide written certification of destruction using methods consistent with industry standards for secure data disposal."

---

## 9. Termination Rights

### 9.1 Termination Triggers

| Trigger | Notice Period | Applies To |
|---------|---------------|------------|
| Convenience | Per contract (typically 30-90 days) | All levels |
| Material breach (uncured) | Immediate after cure period | All levels |
| Security incident (material) | Immediate | Level 1-2 |
| Insolvency | Immediate | All levels |
| Change of control | 30 days | Level 1-2 |
| Failure to maintain certifications | 30 days to cure | Level 1-2 |
| Regulatory requirement | As required | All levels |

### 9.2 Termination Assistance

**Level 1 & 2 Suppliers shall provide:**

- Transition planning support
- Knowledge transfer
- Data migration assistance
- Continued service during transition (up to 6 months)
- Documentation handover

---

## 10. Liability and Insurance

### 10.1 Liability Provisions

| Provision | Guidance |
|-----------|----------|
| Liability cap | Negotiate based on risk; unlimited for data breach recommended |
| Indemnification | For third-party claims arising from supplier breach |
| Exclusions | Gross negligence and willful misconduct carve-out |
| Consequential damages | Negotiate data breach exception to exclusion |

### 10.2 Insurance Requirements (Level 1 & 2)

| Insurance Type | Minimum Coverage |
|----------------|------------------|
| Cyber liability | Appropriate to data volume and sensitivity |
| Professional liability (E&O) | Appropriate to service value |
| General liability | Standard commercial coverage |

---

## 11. Agreement Register

All supplier agreements shall be tracked including:

| Field | Description |
|-------|-------------|
| Agreement reference | Unique identifier |
| Supplier name | Legal entity |
| Agreement type | MSA, SLA, DPA, etc. |
| Effective date | Start date |
| Expiration date | End or renewal date |
| Auto-renewal | Yes/No, notice period |
| Security clauses | Checklist compliance |
| Review date | Last legal/security review |
| Document location | Repository reference |

---

## 12. References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-A.5.19-23 | Parent policy framework |
| ISMS-POL-A.5.19-23-S1 | Supplier classification (determines clause requirements) |
| ISMS-POL-A.5.19-23-S3 | Supply chain (subcontractor requirements) |
| ISMS-IMP-A.5.19-23.3 | Contract review assessment workbook |

---

**Next Document:** ISMS-POL-A.5.19-23-S3 — ICT Supply Chain Security (Control A.5.21)

---

*"A contract without security clauses is just a promise waiting to be broken."*