# ISMS-POL-A.8.10-S2
## Information Deletion Requirements — Overview

---

**Document ID**: ISMS-POL-A.8.10-S2  
**Title**: Information Deletion Requirements — Overview  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial requirements framework |

**Review Cycle**: Semi-annual (or upon significant regulatory/organizational changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Privacy: Data Protection Officer (DPO)
- Technical: IT Operations Manager
- Compliance: Legal/Compliance Officer

**Distribution**: Security team, IT operations, data governance, legal, DPO office  
**Related Documents**: ISMS-POL-A.8.10-S2.1 through S2.4 (specific requirements)

---

## 2.1 Introduction

This document provides an overview of information deletion requirements established to implement ISO/IEC 27001:2022 Control A.8.10. Detailed requirements are organized into four functional domains, each documented in separate policy sections to support granular change management and stakeholder accountability.

Information deletion requirements balance multiple organizational objectives:

- **Security**: Prevent unauthorized disclosure by removing data no longer needed
- **Compliance**: Meet legal, regulatory, and contractual deletion obligations
- **Privacy**: Honor data subject rights including the right to erasure
- **Risk Reduction**: Minimize exposure in case of breach by limiting retained data
- **Operational Efficiency**: Reduce storage costs and management burden from unnecessary data
- **Legal Protection**: Limit scope of legal discovery and reduce litigation risk

---

## 2.2 Requirements Framework

Information deletion requirements are organized into four domains:

### 2.2.1 Retention & Deletion Triggers (S2.1)

**Objective**: Define when deletion must occur based on retention periods and triggering events.

**Scope**: Requirements for:
- Data category identification and classification
- Retention period determination (legal, regulatory, contractual, business)
- Deletion trigger events (expiry, request, contract end, purpose completion)
- Legal hold management and suspension of deletion
- Automated vs. manual deletion processes
- Retention schedule maintenance and governance

**Primary Stakeholders**: Data Governance, Legal/Compliance, DPO  
**Detailed Requirements**: ISMS-POL-A.8.10-S2.1

### 2.2.2 Deletion Methods by Media Type (S2.2)

**Objective**: Ensure appropriate deletion methods are used based on storage media characteristics and data sensitivity.

**Scope**: Requirements for:
- Sanitization method selection (Clear, Purge, Destroy, Cryptographic Erasure)
- Media-specific deletion procedures (HDD, SSD, tape, cloud, paper, mobile)
- Tool approval and validation
- Physical destruction processes and chain of custody
- Cryptographic erasure implementation
- Verification of deletion effectiveness

**Primary Stakeholders**: IT Operations, Security Team, Physical Security  
**Detailed Requirements**: ISMS-POL-A.8.10-S2.2

**Note**: NIST SP 800-88 Rev. 1 provides authoritative guidance on sanitization methods. Organizations should align deletion procedures with this standard while adapting to their specific technology environment.

### 2.2.3 Verification & Evidence Requirements (S2.3)

**Objective**: Ensure deletion activities are documented and verifiable for compliance and audit purposes.

**Scope**: Requirements for:
- Deletion logging and audit trails
- Certificates of destruction (internal and third-party)
- Data subject request tracking and response documentation
- Evidence retention and accessibility
- Chain of custody documentation
- Verification procedures and sampling

**Primary Stakeholders**: Security Team, DPO, Compliance/Audit  
**Detailed Requirements**: ISMS-POL-A.8.10-S2.3

### 2.2.4 Third-Party & Cloud Deletion (S2.4)

**Objective**: Ensure deletion obligations are met for data stored with external providers.

**Scope**: Requirements for:
- Cloud provider deletion capabilities assessment
- Contractual deletion clauses (DPA, SLA)
- Deletion verification from third parties
- Sub-processor deletion obligations
- Service termination data handling
- Multi-tenant environment considerations

**Primary Stakeholders**: Vendor Management, Legal, IT Operations  
**Detailed Requirements**: ISMS-POL-A.8.10-S2.4

---

## 2.3 Risk-Based Approach

Information deletion requirements follow a risk-based methodology:

1. **Identify Data**: Catalog data categories, locations, and retention requirements
2. **Assess Risk**: Evaluate exposure risk from retained data vs. business need
3. **Define Controls**: Establish deletion methods proportionate to data sensitivity
4. **Implement Processes**: Deploy technical and procedural deletion capabilities
5. **Verify Effectiveness**: Confirm deletion occurred and maintain evidence
6. **Review Periodically**: Reassess retention needs and deletion procedures

Requirements are **not one-size-fits-all**. Organizations must:
- Consider data sensitivity and classification levels
- Balance deletion obligations with retention requirements
- Comply with applicable legal and regulatory frameworks
- Document risk-based decisions (e.g., extended retention justifications)
- Accept residual risk where immediate deletion is not feasible

### Risk Factors Influencing Deletion Priority:

| Factor | Higher Priority | Lower Priority |
|--------|-----------------|----------------|
| **Data Sensitivity** | PII, Restricted, Confidential | Public, non-sensitive |
| **Regulatory Exposure** | GDPR/FADP personal data | Non-regulated data |
| **Breach Impact** | High (financial, reputational) | Low |
| **Data Subject Rights** | Active erasure requests | No requests pending |
| **Retention Status** | Past retention period | Within retention period |

---

## 2.4 Technology Neutrality

All requirements in this framework are **vendor-agnostic** and **technology-independent**. Requirements specify:

- **Capabilities** that must be achieved (WHAT)
- **Outcomes** that must be demonstrated (WHY)

Requirements do **NOT** specify:
- Specific vendor products or deletion tools (HOW)
- Particular cloud providers or services
- Implementation architectures or technical configurations

Organizations may satisfy requirements using any technology solution(s) appropriate to their environment, provided the solution demonstrably meets stated requirements.

**Provider Reference**: ISMS-REF-A.5.23 (Cloud Service Provider Registry) provides a standardized list of common providers for assessment purposes without mandating specific vendors.

---

## 2.5 Relationship to Implementation

Policy requirements (this document and S2.1-S2.4) define **WHAT** must be achieved. Implementation specifications (ISMS-IMP-A.8.10.x) define **HOW** compliance is assessed and demonstrated.

**Mapping**:

| Policy Section | Implementation Assessment | Purpose |
|----------------|--------------------------|---------|
| S2.1 (Retention & Triggers) | IMP-A.8.10.1 | Document data categories, retention periods, and triggers |
| S2.2 (Deletion Methods) | IMP-A.8.10.2 | Document media inventory and deletion capabilities |
| S2.3 (Verification & Evidence) | IMP-A.8.10.4 | Document deletion certificates, logs, and audit trails |
| S2.4 (Third-Party & Cloud) | IMP-A.8.10.3 | Document provider capabilities and contractual compliance |
| All Sections | IMP-A.8.10.5 | Consolidated compliance dashboard and gap analysis |

Implementation assessments provide evidence that policy requirements are met, using quantifiable metrics and documented artifacts.

---

## 2.6 Compliance Verification

Compliance with information deletion requirements shall be verified through:

- **Retention Audits**: Verification that data is deleted per retention schedules
- **Media Inventory Reviews**: Confirmation that all media types have defined deletion procedures
- **Certificate Collection**: Gathering of deletion certificates and destruction confirmations
- **Request Tracking**: Monitoring of data subject erasure request response times
- **Provider Assessments**: Verification of third-party deletion compliance
- **Log Analysis**: Review of deletion logs and audit trails
- **Gap Identification**: Documentation of deletion failures or delays
- **Third-Party Audits**: External validation during ISO 27001 certification audits

Evidence of compliance shall be documented in implementation assessment workbooks (ISMS-IMP-A.8.10.x) and retained per organizational record retention policies.

---

## 2.7 Requirement Prioritization

Where resource constraints prevent simultaneous implementation of all requirements, organizations should prioritize:

### Critical (Must Implement):
- Data subject erasure request handling (GDPR Art. 17 / FADP compliance)
- Deletion of PII beyond retention period
- Secure disposal of media leaving organizational control
- Basic deletion logging for audit trail

### Important (Should Implement):
- Comprehensive retention schedule for all data categories
- Automated deletion for systems supporting it
- Third-party deletion verification
- Certificate of destruction collection

### Beneficial (May Implement):
- Advanced deletion verification (recovery testing)
- Real-time retention compliance monitoring
- Automated data subject request workflows
- Deletion analytics and reporting

Prioritization decisions must be documented with risk justification and approved by the CISO and DPO.

---

## 2.8 Regulatory Alignment

### GDPR Article 17 — Right to Erasure

The right to erasure applies when:
- Data is no longer necessary for original purpose
- Data subject withdraws consent
- Data subject objects to processing
- Data was unlawfully processed
- Legal obligation requires erasure
- Data was collected from a child

**Exceptions** (deletion not required):
- Freedom of expression and information
- Legal obligation requiring retention
- Public health purposes
- Archiving in public interest, scientific/historical research
- Establishment, exercise, or defense of legal claims

### Swiss FADP (nDSG)

- Data minimization principle (Art. 6)
- Purpose limitation — deletion when purpose achieved
- Data subject rights including correction/deletion
- Proportionality in data retention

### Sector-Specific Requirements

Organizations must identify and document additional deletion requirements from:
- Financial services regulations (transaction retention, then deletion)
- Healthcare regulations (medical record retention periods)
- Telecommunications regulations (traffic data retention limits)
- Employment law (personnel record retention)

---

## 2.9 Document Structure

The complete Information Deletion Requirements framework consists of:

| Document | Title | Lines |
|----------|-------|-------|
| **ISMS-POL-A.8.10-S2** | This overview document | ~220 |
| **ISMS-POL-A.8.10-S2.1** | Retention & Deletion Triggers | ~350 |
| **ISMS-POL-A.8.10-S2.2** | Deletion Methods by Media Type | ~350 |
| **ISMS-POL-A.8.10-S2.3** | Verification & Evidence Requirements | ~300 |
| **ISMS-POL-A.8.10-S2.4** | Third-Party & Cloud Deletion | ~300 |

Each section is independently versionable. Changes to one section do not require re-approval of other sections unless dependencies exist.

---

**END OF DOCUMENT**
