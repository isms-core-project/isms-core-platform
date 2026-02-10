<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S2:framework:GOV-POL:a.5.19-23-s2 -->
**ISMS-POL-A.5.19-23-S2 — Supplier Agreement Requirements**
**Control A.5.20: Addressing Information Security in Supplier Agreements**

---

**Document Control**

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
- ISMS-IMP-A.5.23-2-UG/TG (Vendor Due Diligence & Contracts)
- ISO/IEC 27001:2022 Control A.5.20
- ISO/IEC 27036-2 (Requirements)
- GDPR Article 28 (Processor requirements)

---

# Purpose

This section defines the mandatory information security requirements that shall be included in supplier agreements. It ensures that security obligations are contractually binding and enforceable throughout the supplier relationship.

**Critical Principle - "Contracts Are Your Last Line of Defense"**: Security requirements without contractual enforceability are merely suggestions that suppliers may ignore without consequence. This policy ensures every supplier agreement includes enforceable security clauses, audit rights, incident notification requirements, and liability provisions. Handshake agreements, verbal commitments, or contracts lacking security terms create legal vulnerability and operational risk that no technical control can mitigate after breach occurs.

**ISO/IEC 27001:2022 Control A.5.20 - Addressing Information Security in Supplier Agreements**

> *Relevant information security requirements should be established and agreed upon with each supplier that may access, process, store, communicate or provide IT infrastructure components for the organization's information.*

**Control Objective**: Ensure information security requirements are contractually binding and enforceable throughout the supplier relationship.

**ISO/IEC 27002:2022 Guidance Summary**:

- Information security requirements shall be included in all supplier contracts and agreements
- Requirements shall address confidentiality, integrity, and availability of organizational information
- Contracts shall define access controls, authentication requirements, and authorization procedures
- Data protection and privacy obligations shall be specified per applicable regulations (GDPR Art. 28, nDSG)
- Incident notification and response requirements shall be documented with specific timelines
- Audit rights and compliance verification mechanisms shall be established
- Service level agreements shall include security metrics and performance indicators
- Termination procedures and data return/destruction obligations shall be contractually defined
- Right to audit (on-site or remote) and regulatory cooperation shall be enforceable

---

# Scope

## Applicable Agreements

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

## Agreement Review Responsibility

| Supplier Level | Agreement Review By |
|----------------|---------------------|
| Level 1 (Critical) | Legal + Security + Business Owner + Procurement |
| Level 2 (High) | Legal + Security + Procurement |
| Level 3 (Medium) | Procurement + Security (if data access) |
| Level 4 (Low) | Procurement (standard terms acceptable) |

**Review Timeline**:

- New agreements: Before contract execution
- Renewals: Minimum 60 days before expiration (allows renegotiation)
- Amendments: Before execution of material changes

**Review Documentation**: Security review shall document:

- Clause-by-clause compliance with this policy
- Identified gaps and acceptability assessment
- Risk assessment for missing clauses
- Approval or rejection recommendation

---

# Mandatory Security Clauses

## Clause Requirements by Supplier Level

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

## Confidentiality Obligations

**Required Elements:**

| Element | Requirement |
|---------|-------------|
| Definition of confidential information | Clear scope of what is protected (data, systems, business information) |
| Permitted use | Limited to service delivery only, no other purposes |
| Permitted disclosure | Need-to-know basis, named parties only, with equivalent confidentiality |
| Protection standard | "Reasonable care" minimum, specify controls (encryption, access restrictions) |
| Duration | Survives termination (minimum 3 years, or perpetual for trade secrets) |
| Return/destruction | Upon termination or request, with certification |
| Exceptions | Publicly available, independently developed, legally required (with notice) |

**Model Clause**:
> "Supplier shall treat all [Organization] information as confidential and shall not use, disclose, or reproduce such information except as necessary to perform the services. Supplier shall protect [Organization] information using no less than the same degree of care used to protect its own confidential information of similar sensitivity, and in no event less than reasonable care."

## Data Protection Compliance

**Required Elements:**

| Element | Requirement |
|---------|-------------|
| Roles definition | Controller vs. Processor designation per GDPR/nDSG |
| Processing purpose | Limited to specified purposes only |
| Data categories | Types of personal data processed |
| Data subjects | Categories of individuals (employees, customers, etc.) |
| Processing location | Geographic restrictions if applicable (EU, CH, specific jurisdictions) |
| Technical measures | Security controls for personal data (encryption, pseudonymization) |
| Organizational measures | Policies, training, access controls |
| Subprocessor rules | Prior approval required, flow-down requirements |
| Data subject rights | Support for access, rectification, deletion, portability requests |
| Breach notification | Within 24 hours to [Organization], cooperation with authority notification |
| Audit cooperation | Support for regulatory audits, data protection impact assessments |
| International transfers | Standard Contractual Clauses (SCCs) or adequacy mechanisms |

**Note**: For Swiss/EU operations, Data Processing Agreement (DPA) must meet:

- **GDPR Article 28**: Processor obligations and security requirements
- **Swiss nDSG Article 9**: Processor security and confidentiality
- **DORA Article 29** (if applicable): Additional ICT service provider requirements

**Model DPA**: Use standard DPAs that incorporate:

- EU Standard Contractual Clauses (SCCs) - Commission Implementing Decision 2021/914
- Swiss Federal Data Protection and Information Commissioner (FDPIC) approved clauses
- Sector-specific additions for DORA/NIS2 if applicable

## Security Controls Commitment

**Required Contract Language**:

> "Supplier shall implement and maintain administrative, technical, and physical security controls appropriate to the classification of data accessed, consistent with industry standards (ISO/IEC 27001, SOC 2 Trust Service Criteria) and the requirements specified in Appendix [X] (Security Requirements)."

**Security Requirements Appendix shall specify:**

| Control Domain | Requirements |
|----------------|--------------|
| Access management | Authentication (MFA for privileged), authorization (RBAC), access logging |
| Encryption | In-transit (TLS 1.2+), at-rest (AES-256 or equivalent) |
| Network security | Segmentation, firewall, intrusion detection/prevention, monitoring |
| Endpoint security | Malware protection, endpoint detection and response (EDR), patching |
| Personnel security | Background checks, security awareness training, termination procedures |
| Physical security | Facility access controls (if applicable), environmental protections |
| Incident management | Detection, analysis, containment, eradication, recovery, lessons learned |
| Change management | Controlled changes with testing, rollback capability, [Organization] notification |
| Vulnerability management | Scanning, patch management, penetration testing |
| Backup and recovery | Regular backups, offsite storage, restoration testing |

**Certification Requirement**: For Level 1 & 2 suppliers, contract shall require maintenance of:

- ISO/IEC 27001 certification OR
- SOC 2 Type II attestation
- Current within 12 months, covering services provided to [Organization]

---

# Incident Notification Requirements

## Notification Timeframes

| Incident Type | Notification Deadline | Notification To |
|---------------|----------------------|-----------------|
| Confirmed data breach | Within 4 hours of confirmation | CISO + ISO + Business Owner |
| Suspected data breach | Within 24 hours of detection | ISO + Business Owner |
| Security incident (non-breach) | Within 48 hours | Security Team |
| Service disruption (critical) | Within 1 hour | IT Operations + Business Owner |
| Service disruption (non-critical) | Within 24 hours | IT Operations |
| Regulatory inquiry | Within 24 hours | Legal + CISO |
| Subprocessor security incident | Within 24 hours | ISO |

**Enhanced Notification for DORA/NIS2 Entities**:

- **DORA-covered services**: Within 2 hours for critical incidents, include concentration risk impact
- **NIS2-covered services**: Within 4 hours for essential service disruption, enable 24-hour regulatory notification

## Notification Content Requirements

**Initial notification shall include (at minimum)**:

- Date and time of incident discovery
- Nature of the incident (breach, outage, compromise)
- Data/systems potentially affected
- Estimated number of affected records (for data breaches)
- Initial containment actions taken
- Designated incident contact with 24/7 availability
- Expected timeline for follow-up

**Follow-up notification shall include**:

- Root cause analysis (technical and procedural)
- Complete impact assessment (data, systems, business processes)
- Remediation actions taken with evidence
- Preventive measures implemented to prevent recurrence
- Detailed timeline of events
- Recommendations for [Organization] actions if any

## Required Contract Language

**Standard Clause**:
> "Supplier shall notify [Organization] without undue delay, and in no event later than twenty-four (24) hours after becoming aware of any Security Incident affecting [Organization]'s data or systems. Supplier shall cooperate fully with [Organization]'s investigation, provide all reasonably requested information, and take all necessary actions to contain, remediate, and prevent recurrence of the incident."

**Enhanced Clause for Level 1 Suppliers**:
> "For any incident involving [Organization]'s Restricted or Confidential data, or any incident that may trigger regulatory notification requirements, Supplier shall notify [Organization]'s Chief Information Security Officer within four (4) hours of confirmation. Supplier shall preserve all forensic evidence, engage independent forensic investigators if requested by [Organization], and bear reasonable costs of [Organization]'s incident response activities."

---

# Audit Rights

## Audit Rights by Level

| Supplier Level | Audit Rights Required |
|----------------|----------------------|
| Level 1 | Full audit rights (on-site or remote, announced or unannounced) |
| Level 2 | Audit rights or third-party report acceptance |
| Level 3 | Third-party report acceptance |
| Level 4 | Not required |

## Audit Rights Clause Elements

**For Level 1 Suppliers:**

| Element | Requirement |
|---------|-------------|
| Scope | Security controls, processes, facilities, personnel, documentation |
| Frequency | Annual minimum, additional upon cause (incident, material change, regulatory requirement) |
| Notice | Reasonable notice (30 days) for planned audits; immediate for cause-based audits |
| Auditor | [Organization] or appointed third party, qualified auditors |
| Cost | Supplier bears cost for cause-based audits; [Organization] bears cost for routine audits |
| Cooperation | Access to personnel, records, systems, facilities; prompt response to requests |
| Findings | Supplier shall remediate within agreed timeline (typically 30-90 days based on severity) |
| Reporting | Audit report provided to [Organization] within 30 days of completion |
| Regulatory cooperation | Supplier shall cooperate with regulatory audits per DORA Art. 29 if applicable |

**Model Clause for Level 1**:
> "[Organization] shall have the right, upon thirty (30) days' prior written notice (or immediately in the event of a Security Incident or regulatory requirement), to audit Supplier's security controls, processes, and facilities relevant to the services provided. Supplier shall provide reasonable cooperation and access to personnel, documentation, and systems. Audits may be conducted by [Organization] or its appointed third-party auditors."

**Alternative for Level 2 Suppliers**:

> "Supplier shall, upon request and at least annually, provide copies of current third-party audit reports (SOC 2 Type II, ISO/IEC 27001 certification with surveillance audit results, or equivalent) and evidence of remediation for any identified findings. Reports must be current (within 12 months) and scope must cover services provided to [Organization]."

## Third-Party Report Acceptance

Acceptable alternatives to direct audit:

| Report Type | Validity | Scope Requirement | Notes |
|-------------|----------|-------------------|-------|
| SOC 2 Type II | 12 months | Covers services provided | Preferred for US providers |
| ISO/IEC 27001 Certificate | Valid + surveillance | Scope includes relevant services | Must include surveillance audit evidence |
| Penetration Test Report | 12 months | Covers relevant systems | Supplement to certification |
| Vulnerability Assessment | 6 months | Covers relevant infrastructure | Supplement to certification |
| CSA STAR Certification | Valid period | Cloud services | Cloud-specific |

**Report Evaluation Criteria**:

- Certification body or audit firm must be accredited/licensed
- Scope explicitly covers services provided to [Organization]
- No material findings unresolved without acceptable remediation plan
- Report date within validity period

---

# Subcontractor Requirements

## Subcontractor Restrictions

**Level 1 & 2 Suppliers:**

| Requirement | Description |
|-------------|-------------|
| Prior approval | Written approval before engaging subcontractors with data access |
| Notification | 30 days advance notice of subcontractor changes for review |
| Flow-down | Security requirements must flow to subcontractors verbatim |
| Liability | Supplier remains fully liable for subcontractor acts and omissions |
| Register | Maintain current list of subcontractors with data access |
| Objection right | [Organization] may object to specific subcontractors within 14 days |
| Audit rights | [Organization]'s audit rights extend to subcontractors |
| Termination | Subcontractor must be removed if [Organization] objects |

**Subcontractor Due Diligence**: Supplier shall perform due diligence on subcontractors equivalent to [Organization]'s requirements in ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals).

## Required Contract Language

**Standard Clause**:
> "Supplier shall not engage any subcontractor to access, process, or store [Organization]'s data without prior written approval from [Organization]. Supplier shall ensure that any approved subcontractor is bound by written obligations no less protective than those in this Agreement. Supplier remains fully liable for acts, omissions, and security failures of its subcontractors."

**Enhanced Clause for DORA-Covered Services**:
> "For ICT services covered by DORA, Supplier shall maintain a register of all sub-outsourcing arrangements and provide advance notice of any intended sub-outsourcing per DORA Article 30. [Organization] reserves the right to require termination of sub-outsourcing arrangements that do not meet security or concentration risk requirements."

---

# Business Continuity Requirements

## BC Requirements by Level

| Requirement | Level 1 | Level 2 | Level 3-4 |
|-------------|---------|---------|-----------|
| Documented BC/DR plan | ✓ Required | ✓ Required | — |
| Annual BC/DR testing | ✓ Required | ✓ Recommended | — |
| Recovery time objective (RTO) | ✓ Defined in SLA | ✓ Defined in SLA | — |
| Recovery point objective (RPO) | ✓ Defined in SLA | ✓ Defined in SLA | — |
| Geographic redundancy | ✓ Risk-based | — | — |
| Test results sharing | ✓ Upon request | ✓ Upon request | — |
| Disaster notification | ✓ Within 1 hour | ✓ Within 4 hours | — |

**DORA-Enhanced Requirements for Critical ICT Providers**:

- Exit strategy documentation with data portability plan
- Alternative provider identification and switching feasibility
- Transition assistance commitment (minimum 6 months)
- Concentration risk mitigation if applicable

## Service Level Requirements

**SLA Elements for Critical/High Suppliers:**

| Element | Description |
|---------|-------------|
| Availability target | Percentage uptime commitment (e.g., 99.9%, 99.95%) |
| Measurement period | Monthly or quarterly measurement |
| Measurement methodology | How uptime is calculated, what counts as downtime |
| Exclusions | Planned maintenance (with advance notice), force majeure |
| Service credits | Financial remedies for failure to meet SLA (e.g., % of monthly fees) |
| Escalation process | Notification tiers and timeframes for degraded service |
| Reporting | Monthly or quarterly performance reports with actual vs. target |
| Service restoration | Maximum time to restore after outage |

**Availability Targets by Service Criticality**:

- **Critical (Tier 1)**: 99.95% or higher (max 4.38 hours downtime/year)
- **High (Tier 2)**: 99.9% (max 8.76 hours downtime/year)
- **Medium (Tier 3)**: 99.5% (max 43.8 hours downtime/year)

**Required SLA Clause**:
> "Supplier commits to maintain [X]% availability measured monthly. In the event of failure to meet this commitment, Supplier shall provide service credits equal to [Y]% of monthly fees for each [Z]% below target. Service credits do not limit [Organization]'s other remedies for material service failures."

---

# Data Return and Destruction

## End-of-Contract Requirements

| Requirement | Description |
|-------------|-------------|
| Data return | Complete export in usable, documented format |
| Return format | Industry-standard (CSV, JSON, XML) or native application format |
| Return timeline | Within 30 days of termination (or shorter if critical) |
| Return completeness | All data, metadata, configurations, audit logs |
| Transition support | Reasonable assistance for migration at agreed rates |
| Data destruction | Secure deletion after return confirmation by [Organization] |
| Destruction method | DOD 5220.22-M, NIST SP 800-88 Rev. 2, or cryptographic erasure |
| Destruction certificate | Written confirmation of destruction with method and date |
| Retention exception | Only if legally required, with written notification and duration |
| Backup destruction | Includes all backup copies and disaster recovery copies |

## Required Contract Language

**Standard Clause**:
> "Upon termination or expiration of this Agreement, Supplier shall, at [Organization]'s election, either (a) return or (b) securely destroy all [Organization] data within thirty (30) days. For data return, Supplier shall provide data in [specify format] and assist with migration. For data destruction, Supplier shall provide written certification of destruction using methods consistent with NIST SP 800-88 Rev. 2 or equivalent. Supplier shall not retain any copies except as required by law, in which case Supplier shall notify [Organization] in writing."

**Enhanced Clause for Regulated Data**:
> "For personal data subject to GDPR or nDSG, destruction must occur within thirty (30) days and comply with data protection requirements. For data subject to retention regulations, Supplier shall notify [Organization] of retention requirements and duration, maintain data subject to agreement confidentiality obligations, and destroy upon expiration of retention period."

---

# Termination Rights

## Termination Triggers

| Trigger | Notice Period | Applies To |
|---------|---------------|------------|
| Convenience | Per contract (typically 30-90 days) | All levels |
| Material breach (uncured) | Immediate after cure period (typically 30 days) | All levels |
| Security incident (material) | Immediate | Level 1-2 |
| Insolvency or bankruptcy | Immediate | All levels |
| Change of control | 30 days notice or immediate termination right | Level 1-2 |
| Failure to maintain certifications | 30 days to cure or terminate | Level 1-2 |
| Regulatory requirement | As required by regulation | All levels |
| Repeated SLA failures | After 3 consecutive months or 6 months in 12-month period | Level 1-2 |
| Data breach by supplier | Immediate | All levels with data access |

## Termination Assistance

**Level 1 & 2 Suppliers shall provide:**

- Transition planning and project management support
- Knowledge transfer documentation and training
- Data migration and export assistance
- Continued service during transition period (up to 6 months for Level 1, 90 days for Level 2)
- Complete documentation handover (configurations, procedures, credentials)
- Cooperation with replacement supplier onboarding

**Termination Assistance Fees**:

- For convenience termination: Reasonable fees for transition assistance
- For cause termination (supplier breach): No additional fees beyond contracted rates

**Required Clause**:
> "Upon termination, Supplier shall provide reasonable transition assistance to facilitate migration to [Organization] or a replacement supplier. For Level 1 services, Supplier shall continue to provide services at contracted rates for up to six (6) months during transition. Supplier shall cooperate fully with knowledge transfer, data migration, and replacement supplier onboarding."

---

# Liability and Insurance

## Liability Provisions

| Provision | Guidance |
|-----------|----------|
| Liability cap | Negotiate based on risk; 12x annual fees minimum for Level 1 |
| Unlimited liability | Data breach, gross negligence, willful misconduct, IP infringement |
| Indemnification | Third-party claims from supplier breach of security obligations |
| Exclusions | Consequential damages exclusion should not apply to data breach |
| Time limit | Claims must be brought within [X] years of discovery |

**Model Limitation of Liability Clause**:
> "Notwithstanding any limitation of liability in this Agreement, Supplier's liability shall be unlimited for: (a) data breaches or unauthorized disclosure of [Organization]'s Confidential or Restricted data, (b) gross negligence or willful misconduct, (c) violation of data protection laws, (d) breach of confidentiality obligations. For all other claims, Supplier's liability shall not exceed twelve (12) times the monthly fees paid in the twelve (12) months preceding the claim."

## Insurance Requirements (Level 1 & 2)

| Insurance Type | Minimum Coverage | Notes |
|----------------|------------------|-------|
| Cyber liability | €5M minimum for Level 1, €2M for Level 2 | First-party and third-party coverage |
| Professional liability (E&O) | €5M minimum for Level 1, €2M for Level 2 | Covering errors and omissions |
| General liability | €2M per occurrence | Standard commercial coverage |
| Privacy/GDPR | Included in cyber or separate €2M | GDPR fines and defense costs |

**Certificate of Insurance**: Supplier shall provide certificate of insurance naming [Organization] as additional insured, with 30 days notice of cancellation or material change.

**Required Clause**:
> "Supplier shall maintain insurance coverage as specified in Appendix [X] with reputable insurers, and shall provide certificates of insurance upon request. Supplier shall notify [Organization] immediately of any insurance cancellation or reduction below required coverage."

---

# Agreement Register

All supplier agreements shall be tracked in the contract management system including:

| Field | Description |
|-------|-------------|
| Agreement reference | Unique identifier in contract management system |
| Supplier name | Legal entity name |
| Agreement type | MSA, SLA, DPA, NDA, SOW |
| Effective date | Commencement date |
| Expiration date | End or renewal date |
| Auto-renewal | Yes/No, notice period required to prevent renewal |
| Security clauses | Checklist compliance status per Section 3.1 |
| Review date | Last legal/security review date |
| Next review | Scheduled review (annual or before renewal) |
| Document location | Repository location or document management system reference |
| Business owner | Internal relationship owner |
| Approval status | Draft, Under Review, Approved, Executed |

**Register Maintenance**:

- Updated within 10 business days of agreement execution or amendment
- Quarterly review for upcoming renewals and required reviews
- Annual completeness audit by Legal and Security

---

# Regulatory-Specific Requirements

## DORA ICT Third-Party Service Providers

For suppliers providing ICT services subject to DORA, agreements must include:

**Article 29 - Key Contractual Provisions**:

- Full cooperation with competent authorities (access, inspection, audit rights)
- Right to issue instructions to ICT third-party service provider
- Right to terminate arrangements where necessary
- Clear description of services provided
- Service locations and data processing locations
- Notification of changes affecting service performance
- Business continuity and disaster recovery commitments
- Exit strategies with data portability and transition assistance

**Article 30 - Sub-outsourcing**:

- Register of all sub-outsourcing arrangements
- Prior notice of sub-outsourcing (30 days minimum)
- Right to object to sub-outsourcing arrangements
- Audit rights extending to subcontractors

**Implementation**: DORA-covered agreements use specialized template incorporating all Article 28-31 requirements.

## NIS2 Supply Chain Security

For suppliers to NIS2-covered entities, agreements must address:

**Article 21 - Security Measures**:

- Supply chain security policies and procedures
- Supplier security assessment documentation
- Incident notification to enable 24-hour regulatory reporting
- Supply chain risk assessment participation

**Implementation**: NIS2 addendum added to standard agreements for suppliers to essential/important entities.

## GDPR Data Processing Agreements

For suppliers processing personal data, Data Processing Agreement (DPA) must include:

**Article 28 Requirements**:

- Processing only on documented instructions
- Confidentiality commitments from personnel
- Technical and organizational security measures
- Sub-processor requirements and approval process
- Data subject rights support (access, deletion, portability)
- Deletion or return at end of services
- Audit and inspection rights
- Assistance with regulatory compliance

**Standard Contractual Clauses (SCCs)**: For non-EU/EEA suppliers, incorporate EU Commission SCCs (Decision 2021/914) or Swiss-approved equivalents.

---

# References

| Document | Relationship |
|----------|--------------|
| **ISMS-POL-A.5.19-23** | Parent policy framework |
| **ISMS-POL-A.5.19-23-S1** | Supplier classification (determines clause requirements) |
| **ISMS-POL-A.5.19-23-S3** | Supply chain security (subcontractor requirements) |
| **ISMS-IMP-A.5.23-2-UG/TG** | Contract review assessment workbook |
| **ISO/IEC 27036-2:2022** | Information security for supplier relationships - Requirements |

---

**Next Document:** ISMS-POL-A.5.19-23-S3 — ICT Supply Chain Security (Control A.5.21)

---

*"A contract without security clauses is an invitation to breach."*
<!-- QA_VERIFIED: 2026-02-01 -->
