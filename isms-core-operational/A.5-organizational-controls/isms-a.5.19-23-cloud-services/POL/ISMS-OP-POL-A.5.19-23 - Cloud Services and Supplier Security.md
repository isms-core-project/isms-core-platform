<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.19-23:operational:OP-POL:a.5.19-23 -->
**ISMS-OP-POL-A.5.19-23 — Cloud Services and Supplier Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Cloud Services and Supplier Security |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.19-23 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 0.1 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Controls A.5.19–A.5.23 — Supplier and Cloud Services Security
- ISO/IEC 27002:2022 Controls 5.19–5.23 — Implementation guidance

**Related Annex A Controls**:

| Control | Relationship to Supplier and Cloud Security |
|---------|----------------------------------------------|
| A.5.9 Inventory of information and assets | Supplier and cloud services tracked in asset inventory |
| A.5.12–13 Information classification and labelling | Data classification drives supplier security requirements |
| A.5.14 Information transfer | Encrypted transfer requirements for supplier data exchange |
| A.5.15–16–18 Identity and access management | Supplier personnel access provisioning and revocation |
| A.5.24–28 Incident management | Supplier incident notification feeds into incident management process |
| A.5.30, A.8.13–14 Business continuity and backup | Supplier disruption scenarios, exit strategy validation, independent backups |
| A.5.31 Legal, statutory, regulatory requirements | Contractual obligations, nFADP/GDPR processor requirements |
| A.5.34 Privacy and PII | Data processing agreements, sub-processor disclosure, cross-border transfers |
| A.8.8 Vulnerability management | Supplier patching commitments, vulnerability disclosure |
| A.8.10 Information deletion | Supplier data destruction verification upon contract exit |
| A.8.24 Use of cryptography | Encryption requirements for supplier data at rest and in transit |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Incident Management Policy
- Information Transfer Policy
- Privacy and Protection of PII Policy
- Business Continuity and Disaster Recovery Policy

---

# Cloud Services and Supplier Security Policy

## Purpose

The purpose of this policy is to manage information security for the use of cloud services and to ensure the data security requirements of third-party suppliers, their sub-contractors, and the supply chain.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) when processed by external suppliers and cloud service providers. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Supplier and cloud service security controls are key measures for demonstrating compliance with data protection obligations under both frameworks.

## Scope

All employees and third-party users.

All third-party suppliers and cloud service providers that process, store, or transmit confidential or personal data.

All cloud services (IaaS, PaaS, SaaS) used by the organisation.

## Principle

Third-party suppliers and cloud service providers shall meet the requirements of the organisation, legislation, and regulation for data security. Supplier trust shall be verified, not assumed — evidence-based validation of supplier security posture is required through systematic due diligence, contractual commitments, and ongoing monitoring.

Cloud service agreements are often pre-defined and not open to negotiation. Where this is the case, the organisation shall assess whether the provider's standard terms meet its security requirements and document any residual risks. Where terms are non-negotiable and do not meet requirements, compensating controls shall be identified or an alternative provider shall be evaluated.

The organisation shall understand and document the shared responsibility model for each cloud service. Security responsibilities are divided between the cloud service provider and the organisation, and this division varies by service model (IaaS, PaaS, SaaS). The organisation remains responsible for the security of its data, identity and access management, and endpoint protection regardless of the service model. The provider is responsible for the security of the underlying infrastructure. Areas of shared responsibility shall be explicitly documented and reviewed.

**Shared responsibility documentation shall include**:

| Responsibility Area | Provider Responsible | Organisation Responsible | Notes |
|---------------------|---------------------|-------------------------|-------|
| Physical data centre security | Yes | | Provider controls physical access |
| Network infrastructure | Yes | | Provider secures underlying network |
| Host infrastructure | Yes (IaaS/PaaS/SaaS) | Yes (IaaS only — OS patching) | For IaaS, organisation manages OS |
| Application security | Yes (SaaS only) | Yes (IaaS/PaaS) | For SaaS, provider responsible |
| Data encryption at rest | Yes (default) | Yes (key management) | Organisation may bring own keys (BYOK) |
| Identity and access management | | Yes | Organisation always responsible |
| Data classification and handling | | Yes | Organisation always responsible |
| Endpoint security | | Yes | Organisation always responsible |

Shared responsibility models shall be documented for each **Critical** cloud service and reviewed annually.

---

## Supplier and Cloud Service Register

All third-party suppliers and cloud services shall be registered and recorded in the **Supplier and Cloud Service Register**.

**Register location**: [GRC platform, procurement system, or dedicated spreadsheet in SharePoint/equivalent]

**Register owner**: [CISO, Procurement Manager, or IT Manager]

**Access**: Register access is restricted to authorised personnel (IT leadership, information security team, procurement). The register is classified as **Internal**.

**Update frequency**: The register shall be reviewed and updated at least **quarterly** or upon any new supplier engagement, contract change, or supplier exit.

Suppliers and cloud services shall be assessed for criticality to the business.

Suppliers and cloud services shall be classified based on the data processed, stored, or transmitted and their criticality to business operations:

| Classification | Criteria | Review Frequency |
|---------------|----------|------------------|
| **Critical** | Access to Confidential/Restricted data, OR core business operations (outage causes immediate business impact), OR processes sensitive personal data (nFADP Art. 5) | Annually |
| **Important** | Access to Internal data but not Confidential, OR supporting services (outage causes moderate disruption within 24–48 hours), OR limited personal data processing | Every two years |
| **Standard** | No data access or Public data only, OR commodity services (easily replaceable, minimal business impact) | On contract renewal |

**Examples**: Critical — cloud hosting provider, payroll processor, backup service, CRM with customer data. Important — marketing automation tool, project management SaaS, collaboration tools. Standard — office supplies vendor, physical security guard services (no data access).

In addition, the following shall be captured as a minimum:

- Supplier or cloud service name and contact details
- What they do for us (service description)
- What data they process, store, or transmit
- Data classification level (Public, Internal, Confidential, Restricted)
- Whether we have a contract and a copy of the contract
- What assurance we have over their data security (certifications, audit reports)
- Data processing and storage locations (country and region)
- Contract expiry date and next review date
- Sub-processors used by the supplier (where known)

## Information Security Requirements

Suppliers and cloud service providers should hold relevant information security certifications that cover the services provided. As a minimum they should have:

- An ISO 27001 certification, **or**
- A SOC 2 Type II report (current, within 12 months)

For cloud service providers handling personal data, ISO 27018 (PII protection in public clouds) or equivalent evidence of PII protection controls is additionally expected.

CSA STAR Level 2 certification (ISO 27001 + Cloud Controls Matrix) is recognised as a strong indicator of cloud-specific security maturity.

Where a supplier cannot provide recognised certification, the organisation shall conduct a documented risk assessment and, if the supplier is engaged, implement compensating controls and obtain risk acceptance from the Information Security Manager and risk owner.

**Potential compensating controls**:

- Enhanced contractual terms with specific security obligations (encryption, access logging, incident notification)
- Security questionnaire completed annually with responses verified against subsequent findings
- Limited data access — restrict supplier to non-personal or non-confidential data only
- Audit rights — right to conduct security audit or penetration test (if contractually achievable)
- Escrow arrangements — code or data escrow for business continuity
- Cyber liability insurance requirements

## Audit and Review

Each supplier and cloud service is subject to audit and review of data security in line with the following risk-based schedule:

| Supplier Classification | Review Frequency | Review Scope |
|------------------------|-----------------|--------------|
| **Critical** (access to Confidential/Restricted data or core operations) | Annually | Full compliance review, SLA performance, certification currency, risk reassessment |
| **Important** (limited data access or supporting services) | Every two years | Compliance validation, contract status, certification check |
| **Standard** (no data access, commodity services) | On contract renewal | Continued business need, basic security check |

The level of audit and review is based on the risk classification of the supplier and the sensitivity of data involved.

Cloud service suppliers are subject to the same audit and review requirements.

### Cloud Service Audit Approach

Major cloud service providers (AWS, Azure, Google Cloud, Microsoft 365, Salesforce, etc.) typically do not permit direct customer audits due to multi-tenancy security and operational scalability constraints.

**Alternative assurance mechanisms** (accepted in lieu of direct audit):

- Independent third-party reports: SOC 2 Type II, ISO 27001 certification, CSA STAR attestation
- Compliance certifications: ISO 27017, ISO 27018, and sector-specific attestations where applicable
- Transparency reports: provider-published security documentation, compliance matrices, sub-processor lists
- Service health dashboards: real-time service availability and incident disclosure

The organisation shall obtain and review the most current independent audit reports (**within 12 months**) for each Critical cloud service annually.

Where a cloud provider does not provide independent third-party reports, the service shall not be used for Confidential or Restricted data without CISO approval and documented residual risk acceptance.

## Risk Management

Every supplier handling confidential or personal data shall be entered onto the Risk Register and managed via the organisation's risk management process.

Cloud service risks shall include assessment of:

- Service availability and business impact of outage
- Data residency and jurisdictional exposure
- Vendor lock-in and exit feasibility
- Concentration risk (dependency on a single provider for critical services) — where a single provider hosts more than 50% of critical services or more than 75% of Confidential data, this shall be flagged in the risk register with a mitigation plan or accepted residual risk. Mitigation options include multi-provider diversification, multi-region deployment within the same provider, and validated exit strategy
- Sub-processor risk (downstream data processing)

## Supplier and Cloud Service Selection

Suppliers and cloud services shall be selected based on their ability to meet the needs of the business.

Before engaging a supplier or cloud service provider, data security due diligence shall be carried out that includes:

- An acceptable level of data security with identified, recorded, and managed risks
- Appropriate references from existing customers
- Appropriate certifications (ISO 27001, SOC 2 Type II, or equivalent — see Information Security Requirements above)
- Appropriate supplier agreements and contracts that include data security requirements
- Legal and regulatory compliance, including nFADP (revDSG) and GDPR where applicable
- Assessment of data processing and storage locations against the organisation's data residency requirements
- Verification that the provider's standard terms meet the organisation's security requirements (particularly for cloud services with non-negotiable agreements)
- Assessment of exit feasibility: data export capability, supported formats, transition assistance, and alternative providers

## Contracts, Agreements and Data Processing Agreements

An appropriate contract, agreement, and/or Data Processing Agreement shall be in place and enforceable before engaging any supplier or cloud service provider to process, store, or transmit confidential or personal information.

Contracts and agreements shall address, at a minimum:

- Description of the data processed, stored, or transmitted
- Information security requirements and obligations
- Incident notification requirements (see Security Incident Management below)
- Audit rights where appropriate, practicable, and allowable (it is acknowledged that major cloud providers typically do not permit direct audit; independent third-party attestation is accepted as alternative evidence)
- Sub-processor disclosure and approval requirements
- Data return and destruction obligations upon contract termination
- Service level agreements covering availability, support response, and security metrics
- Exit provisions including data export, transition assistance, and termination notice periods

All organisation policies apply to the use of the supplier or cloud service.

### Sub-Contractor and Sub-Processor Requirements

The use by suppliers of sub-contractors or sub-processors shall be approved by the Information Security Manager. Sub-contractors and sub-processors are subject to the same terms and security requirements as the supplier.

**Approval models**:

- **Specific authorisation**: The organisation approves each sub-processor individually (preferred for Critical suppliers processing Confidential or Restricted data)
- **General authorisation with notification**: The organisation grants general permission for sub-processors meeting specified criteria, with at least 30 days' advance notice of changes (acceptable for Important suppliers)

Cloud service providers shall disclose their sub-processor list. The organisation shall be notified of changes to sub-processors **at least 30 days in advance** and shall retain the right to object where contractually achievable. Where objection rights cannot be obtained (as is common with major cloud providers), this limitation shall be documented in the risk register as residual risk with compensating controls (encryption, access monitoring).

### Data Processing Agreements (nFADP/GDPR)

All suppliers processing personal data on behalf of the organisation shall have a Data Processing Agreement in place that meets the requirements of Swiss nFADP (revDSG) Art. 9 and, where applicable, GDPR Art. 28.

The Data Processing Agreement shall address:

- Subject matter and duration of processing
- Nature and purpose of processing
- Type of personal data and categories of data subjects
- Obligations and rights of the controller
- Sub-processor approval requirements (specific or general with notification)
- Data security measures (technical and organisational)
- Assistance with data subject rights requests
- Return or deletion of data upon termination
- Audit and inspection rights

### Cross-Border Data Transfers

Where suppliers or cloud service providers process or store personal data outside Switzerland, the organisation shall verify that adequate data protection exists in the destination country per the Swiss Federal Council's adequacy list (Annex 1 to the Data Protection Ordinance).

For transfers to countries not on the adequacy list, appropriate safeguards shall be in place:

- Standard Contractual Clauses (SCCs) amended for Swiss law compliance, **or**
- Binding Corporate Rules (BCRs) approved by the FDPIC, **or**
- Other recognised transfer mechanisms

For transfers to the United States, the organisation shall verify that the receiving organisation is certified under the Swiss-U.S. Data Privacy Framework. Where the provider is US-headquartered and subject to the US CLOUD Act, a jurisdictional risk assessment shall be documented, including encryption and key management arrangements and the provider's legal challenge commitments.

## Security Incident Management

Suppliers and cloud service providers shall have a security incident management process in place.

Supplier and cloud service security incidents that impact confidential or personal information shall be reported to the organisation within the following timelines:

| Supplier Classification | Notification Timeline | Notes |
|------------------------|----------------------|-------|
| **Critical** | **12 hours** (mandatory) | Must be contractually committed |
| **Important** | **24 hours** (target) | Best-effort where 12 hours is not achievable |
| **Standard** | **72 hours** (acceptable) | Acceptable if no personal data breach involved |

Where a supplier cannot commit to the 12-hour timeline, this shall be documented as a residual risk with compensating controls (more frequent supplier reviews, enhanced monitoring, backup provider).

The notification shall include, at a minimum:

- Description of the incident
- Affected systems and data
- Containment measures taken
- Estimated impact and resolution timeline

Supplier and cloud service security incidents shall be managed as part of the organisation's incident management process, in accordance with the Incident Management Policy.

Where a supplier incident involves a personal data breach, the organisation shall assess notification obligations under nFADP (notification to the FDPIC as soon as possible) and, where applicable, GDPR Art. 33 (notification to the supervisory authority within 72 hours).

Where appropriate, the supplier's incident management process shall be followed in coordination with the organisation's own procedures.

## End of Contract

At the end of the contract, the supplier or cloud service provider shall confirm in writing that it has met its contractual and legal obligations for the destruction of organisation confidential and personal information.

Where appropriate, practicable, and relevant (acknowledging limitations with cloud services), the following shall be completed:

- All organisation data is returned in a usable format or securely destroyed, as directed by the organisation
- Written confirmation of data destruction is provided, including method used
- All access to organisation systems and information is revoked
- All organisation assets (physical and logical) are returned
- Certificates of destruction are obtained where data was classified as Confidential or Restricted

## Changes to Cloud Service Supplier

Changes to a cloud service supplier require the formal, written, documented approval of the CEO or delegated authority.

Changes shall follow the Change Management Policy and change management process.

Changes to cloud suppliers are significant changes and shall not be taken lightly. Such changes shall be treated as a project with appropriate resources, risk management, project management, and stakeholder communication.

The organisation shall maintain an exit strategy for each **Critical** cloud service to ensure that a transition or exit can be executed in a controlled manner if required.

**Exit strategy minimum components**:

- **Data export capability**: documented data export process and supported formats (CSV, JSON, API, backup restoration)
- **Transition timeline**: estimated time to migrate to an alternative provider (assume worst case: forced exit)
- **Alternative providers**: at least one pre-identified alternative provider evaluated
- **Transition costs**: estimated cost (licences, professional services, data migration)
- **Dependencies**: identified integrations and dependencies that would require reconfiguration
- **Exit testing**: verification that data export works (test performed annually for Critical services)

Exit strategies shall be reviewed **annually** or upon contract renewal.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Supplier and Cloud Service Register** — complete, current, with data classification and review dates; *reviewed quarterly*
- **Signed contracts and Data Processing Agreements** — for all suppliers handling confidential or personal data; *contract register maintained by [Procurement/Legal]*
- **Supplier certifications on file** — ISO 27001, SOC 2 Type II, CSA STAR (current within 12 months); *reviewed annually for Critical suppliers*
- **Supplier review meeting minutes** and performance reports — *annual reviews for Critical, biennial for Important*
- **Risk Register entries** — for suppliers handling confidential or personal data; *reviewed quarterly*
- **Incident notification records** from suppliers — *tracked in incident management system*
- **Data Processing Agreements** with nFADP/GDPR-compliant terms — *reviewed upon contract renewal or regulatory change*
- **Cross-border transfer assessments** — adequacy verification, SCCs, or DPF certification; *documented for each cross-border supplier/cloud service*
- **Exit strategy documentation** for Critical cloud services — *reviewed annually; exit testing performed for top Critical services*
- **Sub-processor registers** and change notification records — *maintained per DPA terms*
- **Data destruction confirmations** upon contract termination — *certificates of destruction or written confirmation retained for 2 years*
- **Shared responsibility model documentation** — for each Critical cloud service; *reviewed annually*

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, supplier register reviews, contract audits, certification checks, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance and compensating controls. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to supplier risk landscape, cloud service market developments, regulatory changes (including nFADP, GDPR, and emerging frameworks), supply chain threat developments, and lessons learned from supplier incidents.

---

# Areas of the ISO 27001 Standard Addressed

Cloud Services and Supplier Security Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.19 Information security in supplier relationships |
| Clause 7.3 Awareness | 5.20 Addressing information security within supplier agreements |
| Clause 8.1 Operational planning and control | 5.21 Managing information security in the ICT supply chain |
| | 5.22 Monitoring, review and change management of supplier services |
| | **5.23 Information security for use of cloud services** |
| | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.30 Outsourced development |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 9 — Processor agreements and sub-processor requirements |
| Swiss DPO (Data Protection Ordinance) | Annex 1 — Adequate countries list for cross-border transfers |
| EU GDPR (where applicable) | Art. 28 — Processor obligations; Art. 44–50 — International transfers |
| Swiss-U.S. Data Privacy Framework | Adequacy mechanism for transfers to certified US organisations |
| ISO/IEC 27001:2022 | Annex A Controls 5.19–5.23 |
| ISO/IEC 27002:2022 | Sections 5.19–5.23 — Implementation guidance |
| ISO/IEC 27017:2015 | Cloud security controls (informational) |
| ISO/IEC 27018:2025 | Cloud PII protection guidelines (informational) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
