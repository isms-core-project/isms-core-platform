<!-- ISMS-CORE:POLICY:CLD-POL-A.12:cloud:POL:a.12 -->
**CLD-POL-A.12 — Privacy Compliance**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Public Cloud PII Processor — Privacy Compliance |
| **Document Type** | Policy |
| **Document ID** | CLD-POL-A.12 |
| **Document Creator** | Data Protection Officer (DPO) / CISO |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO / CISO | Initial policy for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory, service footprint, or data residency change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: CISO / Cloud Security Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.5.19-23 (Supplier and Third-Party Relationships)
- CLD-POL-A.1 (General)
- CLD-POL-A.8 (Openness, Transparency — sub-processor disclosure)
- CLD-POL-A.11.12 (Sub-contracted PII processing)
- ISO/IEC 27018:2025 Annex A, Section A.12 and Controls A.12.1–A.12.2
- ISO/IEC 27701:2025 Controls A.2.3.11–A.2.3.12 (processor — transparency on processing locations)
- GDPR Article 28(3)(a) (processor processes only on documented controller instructions); Article 44–49 (transfers to third countries); Article 46 (appropriate safeguards for international transfers)
- CH FADP Article 16–17 (international transfers of personal data); Article 9(3) (processor obligations on sub-processors and locations)

---

## Executive Summary

This policy establishes [Organisation]'s requirements as a public cloud PII processor with regard to privacy compliance — specifically the obligation to disclose the geographical locations at which PII is stored, processed, or transits, to respect data residency requirements imposed by PII controllers, and to document and communicate all intended PII destinations including international transfers and their legal basis — in accordance with ISO/IEC 27018:2025 Annex A, Section A.12 and Controls A.12.1 and A.12.2.

**Scope**: All PII processed by [Organisation] on behalf of PII controllers, across all infrastructure regions, availability zones, and sub-processor locations.

**Combined Control Rationale**: A.12.1 and A.12.2 address the geographic dimension of PII processing transparency. A.12.1 establishes the obligation to disclose where PII resides; A.12.2 establishes the obligation to identify all destinations to which PII may flow and document the legal basis for any transfer outside the controller's jurisdiction. Together these controls enable PII controllers to fulfil their own transfer accountability obligations under GDPR Article 44+ and equivalent national law.

---

# Scope and Applicability

## ISO/IEC 27018:2025 Control Statements

**Section A.12 — Privacy compliance (principle)**
> *The cloud service provider shall maintain and disclose to PII controllers information about the geographic locations at which PII is stored, processed, or transmitted. The provider shall implement mechanisms to enforce data residency requirements, obtain controller consent before relocating PII to new jurisdictions, and document the legal basis and safeguards for all cross-border transfers.*

**Control A.12.1 — Geographical location of PII**
> *The public cloud PII processor shall disclose to the PII controller all countries and regions in which PII is stored, processed, or transits as part of cloud service delivery — including sub-processor locations. Any change to geographic location of PII processing shall require prior controller notification and, where required, consent. Data residency restrictions imposed by the controller in the service agreement shall be technically enforced.*

**Control A.12.2 — Intended destination of PII**
> *The public cloud PII processor shall, upon request or proactively where required, inform the PII controller of all intended destinations to which PII may be transferred, including jurisdictions outside the controller's home country. For each cross-border or cross-jurisdiction transfer, [Organisation] shall document the applicable transfer mechanism (e.g., adequacy decision, standard contractual clauses, binding corporate rules) and make this information available to the controller.*

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 28(3)(a) (processor processes only in accordance with controller instructions, including on location); Articles 44–49 (prohibition on transfers to third countries lacking adequate protection unless appropriate safeguards are in place); Article 46 (standard contractual clauses, binding corporate rules, codes of conduct as transfer mechanisms); Article 30 (records of processing activities including recipients and third countries)
- **CH FADP**: Articles 16–17 (prohibition on transfer of personal data to countries without adequate protection; recognised safeguards); Article 9(3) (processor sub-contracting and location obligations)
- **ISO/IEC 27018:2025**: Controls A.12.1, A.12.2

---

# Policy Statements: Geographical Location of PII (A.12.1)

## Location Disclosure

[Organisation] SHALL maintain a **PII Processing Locations Register** documenting all countries and regions in which PII is stored, processed, or transits as part of cloud service delivery. The register SHALL cover:

- **Primary storage locations**: Data centres and cloud regions where PII at rest resides
- **Processing locations**: Compute regions where PII is actively processed
- **Transit routes**: Regions through which PII may pass during replication, backup, or delivery operations
- **Sub-processor locations**: All geographic locations of sub-processors engaged under CLD-POL-A.11.12

The PII Processing Locations Register SHALL be made available to PII controllers upon request and SHALL be publicly accessible for controllers operating under general authorisation (e.g., linked from [Organisation]'s trust portal or DPA annex).

## Data Residency Enforcement

Where a PII controller specifies data residency requirements in the service agreement (e.g., "EU-only storage", "Switzerland only"), [Organisation] SHALL:

- **Technically enforce** the residency constraint through infrastructure configuration (regional restrictions, geo-fencing, storage policy rules)
- **Document** the technical mechanism used to enforce the constraint and make this documentation available to the controller upon request
- **Audit** residency compliance at least annually and upon significant infrastructure changes, confirming that no PII has been stored or processed outside the agreed regions

## Change Notification

Before changing the geographic location of PII processing — including opening a new service region, adding a sub-processor in a new jurisdiction, or relocating backup storage — [Organisation] SHALL:

1. Notify the relevant PII controller in advance, with a minimum **30 days' notice** (unless the service agreement specifies a longer period)
2. Identify the new location and explain the operational reason for the change
3. Obtain prior consent from controllers whose service agreements require specific consent (not merely general authorisation) for location changes
4. Update the PII Processing Locations Register within 5 business days of the change taking effect

Emergency location changes (e.g., due to data centre failure or force majeure) SHALL be notified to affected controllers without undue delay, with retroactive documentation of the change and its justification.

---

# Policy Statements: Intended Destination of PII (A.12.2)

## Transfer Documentation

[Organisation] SHALL maintain documented records of all **intended destinations** to which PII may be transferred as part of cloud service delivery, including cross-border or cross-jurisdiction flows to:

- Sub-processors (whether within the EEA or outside)
- Backup and disaster recovery sites in third countries
- Cloud provider infrastructure in jurisdictions outside the controller's home country
- Support or operations personnel accessing PII remotely from outside the processing region

For each identified destination, [Organisation] SHALL document:

| Element | Description |
|---------|-------------|
| **Destination country/region** | Jurisdiction of the intended recipient or processing location |
| **Transfer purpose** | Operational reason for the transfer (backup, support access, replication, etc.) |
| **Transfer mechanism** | Legal basis for the transfer (adequacy decision, SCCs, BCRs, derogation — see below) |
| **Safeguards in place** | Technical and contractual protections applied (encryption in transit, DPA/addendum, sub-processor agreement) |
| **Controller notification status** | Whether the controller has been informed of this destination |

## Transfer Mechanisms

For transfers of PII to countries outside the EEA or Switzerland that lack an adequacy decision, [Organisation] SHALL implement one of the following approved transfer mechanisms:

- **Standard Contractual Clauses (SCCs)**: EC-approved SCCs (2021 set) incorporated into sub-processor and data processing agreements
- **UK International Data Transfer Agreement (IDTA)**: For transfers to/from the United Kingdom
- **Swiss Standard Data Protection Clauses**: For transfers subject to CH FADP
- **Adequacy decision**: Where the destination country has an EU or Swiss adequacy decision in force at the time of transfer
- **Binding Corporate Rules (BCRs)**: Where applicable for intra-group transfers

[Organisation] SHALL NOT transfer PII to a third country unless one of the above mechanisms is in place and documented. Where the adequacy status of a destination country changes, [Organisation] SHALL review and implement alternative mechanisms within 30 days of the change taking effect.

## Controller Information

[Organisation] SHALL make transfer documentation available to PII controllers upon request. Where requested by a controller to support the controller's own GDPR Article 30 record of processing activities or transfer impact assessments, [Organisation] SHALL provide:

- The complete list of transfer destinations for the controller's PII
- The transfer mechanism and relevant legal instrument reference (e.g., SCCs clause reference, adequacy decision citation) for each destination
- A summary of supplementary technical safeguards applied for transfers to high-risk jurisdictions

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Owns the PII Processing Locations Register and transfer documentation; advises on adequacy assessments and transfer mechanism selection; manages controller notification for location changes; reviews transfer mechanisms annually |
| **CISO / Cloud Security Manager** | Implements and audits technical data residency enforcement controls; oversees sub-processor location monitoring; manages emergency location change notifications |
| **Legal/Compliance Officer** | Maintains SCCs, IDTAs, and Swiss standard clauses templates; advises on third-country adequacy status; reviews transfer documentation for regulatory compliance |
| **Cloud Engineering** | Implements geographic data constraints and residency enforcement mechanisms; configures regional isolation for customer workloads; audits residency compliance |
| **Procurement** | Ensures sub-processor locations are captured before contract signature; triggers DPO review for new or changed sub-processor locations |

---

# Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| PII Processing Locations Register | Complete register of all PII storage, processing, and transit locations including sub-processors | Current + previous versions for 5 years |
| Data Residency Configuration Records | Technical documentation of residency enforcement mechanisms per controller | Duration of agreement + 5 years |
| Residency Audit Results | Annual audit results confirming no out-of-scope PII processing | 5 years |
| Location Change Notifications | Records of advance notices sent to controllers for location changes | 5 years |
| Transfer Destination Records | Complete transfer destination documentation per controller | Duration of agreement + 5 years |
| Transfer Mechanism Instruments | Copies of SCCs, IDTAs, BCRs, and adequacy decision citations relied upon | Duration of engagement + 5 years |
| Transfer Impact Assessment Records | Documented TIAs or equivalent assessments for transfers to high-risk jurisdictions | 5 years |

---

# Audit Considerations

Auditors verifying compliance with CLD-POL-A.12 should expect to find:

- A current PII Processing Locations Register covering all storage, processing, and transit locations including sub-processors — consistent with the published sub-processor list (CLD-POL-A.8.1)
- Technical evidence that data residency controls are implemented and enforced for all controllers with residency requirements
- Records of advance notification to controllers for any location changes occurring in the audit period
- Transfer destination records with documented transfer mechanisms for all non-EEA/non-Swiss processing locations — including SCCs or equivalent instruments for each third-country destination
- No undocumented PII transfers to third countries lacking an approved transfer mechanism

---

<!-- QA_VERIFIED: [Date] -->
