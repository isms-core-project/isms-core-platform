<!-- ISMS-CORE:IMP:CLD-IMP-A.8-UG:cloud:UG:a.8 -->
**CLD-IMP-A.8-UG — Openness, Transparency and Notice — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Openness, Transparency and Notice — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.8-UG |
| **Related Policy** | CLD-POL-A.8 (Openness, Transparency and Notice) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon sub-processor changes or service model changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.8 (Openness, Transparency and Notice — the governing policy)
- CLD-IMP-A.8-TG (Openness, Transparency and Notice — Technical Guide)
- CLD-POL-A.1 (General — processor relationship and service scope)
- CLD-POL-A.11.12 (Sub-contracted PII processing — security flow-down to sub-processors)
- CLD-POL-A.12 (Privacy Compliance — geographic disclosure of processing locations)

---

## Purpose of This Guide

This guide explains how [Organisation] maintains openness and transparency about its cloud PII processing practices. It covers what [Organisation] must publish about its processing and sub-processor arrangements, how to keep those disclosures current when practices change, and how to make ISO 27018:2025 control documentation available to PII controllers.

**Who this guide is for**: DPO, Legal/Compliance Officer, CISO, Procurement, Cloud Service Delivery.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. Transparency about sub-processors is a mandatory obligation under GDPR Article 28(2) and CH FADP Article 9(3). Failure to disclose sub-processor changes in advance can constitute a material breach of the processor agreement.

---

## Part 1 — What [Organisation] Must Publish About Its PII Processing Practices

### 1.1 Required Public Disclosures

[Organisation] SHALL maintain the following publicly accessible information about its cloud PII processing practices. The DPO is responsible for ensuring these disclosures are current and accessible:

| Disclosure | Location | Minimum Content |
|-----------|----------|----------------|
| Privacy Policy (processor-facing) | [Organisation] website / trust portal | Types of PII processed; processing purposes; sub-processor disclosure; controller rights; DPO contact |
| Sub-Processor List | Trust portal (subscriber-accessible at minimum) | Name, services provided, processing location(s) per sub-processor |
| ISO 27018 Controls Summary | Trust portal (subscriber-accessible) | Summary of controls implemented per ISO/IEC 27018:2025 Annex A |
| Geographic Processing Locations | Trust portal | Countries or regions where PII processing occurs (per CLD-POL-A.12) |
| DPO Contact Details | Website and DPA template | Name or role, contact email, postal address |

The DPO reviews all public disclosures annually and following any material change to processing practices. Each review is recorded with the date and the reviewer's identity.

### 1.2 Controller-Facing Service Documentation

In addition to public disclosures, [Organisation] provides controllers with the following upon request or as part of the service agreement:

- A copy of the current Sub-Processor Register (see CLD-IMP-A.8-TG)
- Evidence of ISO/IEC 27018:2025 certification or assessment (e.g., audit report summary)
- The Data Processing Agreement (DPA) template
- A summary of the security and privacy controls implemented under each CLD-POL

Cloud Service Delivery maintains an index of documentation available to controllers and fulfils requests within 5 business days.

---

## Part 2 — Updating Public Disclosures When Practices Change

### 2.1 Triggers for Disclosure Update

The DPO SHALL initiate a disclosure update whenever:

- A new sub-processor is engaged or an existing sub-processor is replaced (see Part 3)
- A material change occurs to an existing sub-processor's scope or processing location
- [Organisation] adds a new service component that processes a new PII category
- [Organisation] changes the geographic location of PII processing
- A regulatory change affects the content of required disclosures

Changes to the Sub-Processor List and geographic disclosures must be published **before** the change takes effect, following the advance notice process in Part 3.

Changes to the Privacy Policy or ISO 27018 controls summary are published on or before the effective date of the change. The DPO confirms publication and archives the previous version.

### 2.2 Version Control for Public Disclosures

Each public disclosure document is version-controlled. The DPO maintains an archive of previous versions with the effective date of each version. This archive is available to controllers on request and is required for demonstrating compliance during audits.

### 2.3 Notifying Controllers of Material Changes

For material changes to processing practices (beyond sub-processor changes), the DPO sends a notification to all affected controllers via their designated data protection contact. Notification is sent at minimum 14 days before the change takes effect, or earlier if required by the service agreement.

---

## Part 3 — Sub-Processor Change Management

### 3.1 Advance Notice of Sub-Processor Changes

Before engaging a new sub-processor, replacing an existing sub-processor, or making a material change to an existing sub-processor's scope or location, the DPO SHALL:

1. Confirm with Procurement and Legal/Compliance that the proposed sub-processor has been assessed and meets [Organisation]'s security and privacy requirements
2. Update the draft Sub-Processor Register with the proposed change
3. Send advance notice to all affected PII controllers a minimum of **30 days** before the change is implemented (or the period specified in the service agreement if longer)
4. Record the notification in the Controller Advance Notice log (see CLD-IMP-A.8-TG)

Notice is delivered via the channel specified in the service agreement (e.g., email to the controller's data protection contact, trust portal announcement with subscriber alert).

### 3.2 Handling Controller Objections

A PII controller may object to a proposed sub-processor change during the 30-day notice period. The DPO's procedure upon receiving an objection:

1. Acknowledge the objection in writing within 3 business days
2. Contact the controller to understand the specific grounds for objection (e.g., jurisdiction concern, sector conflict, security posture)
3. Assess whether an alternative processing arrangement can accommodate the objection
4. If the objection can be upheld: implement the alternative arrangement before proceeding with the change; notify the controller
5. If the objection cannot be accommodated: notify the controller in writing; allow contract termination on reasonable terms without penalty if the controller cannot accept the change

Controllers who do not object within the notice period are deemed to have accepted the change. The DPO documents this for each controller in the Controller Advance Notice log.

### 3.3 Emergency Sub-Processor Changes

Where [Organisation] must engage a replacement sub-processor urgently (e.g., sub-processor insolvency, security incident, or regulatory action against the sub-processor):

1. The DPO notifies affected controllers without undue delay, providing written justification for the emergency change
2. Cloud Engineering confirms that equivalent security and privacy controls are applied to the replacement sub-processor before any PII is transferred
3. The Sub-Processor Register is updated within 5 business days of the emergency change
4. Legal/Compliance confirms the replacement sub-processor agreement includes equivalent contractual obligations (GDPR Article 28(4) flow-down)

### 3.4 Making ISO 27018 Control Documentation Available to Controllers

Controllers conducting due diligence or preparing for certification audits may request access to [Organisation]'s ISO 27018 control documentation. Cloud Service Delivery handles these requests as follows:

1. Confirm the controller's identity and the service agreement in force
2. Provide the ISO 27018 Transparency Disclosure (see CLD-IMP-A.8-TG) and any available certification evidence
3. For detailed control evidence requests (e.g., audit reports, penetration test summaries): route to CISO and DPO for approval; disclosure subject to confidentiality agreement if required
4. Record the disclosure in the Controller Documentation Request log

---

## Evidence Checklist

- [ ] Sub-Processor Register — current, complete, all mandatory fields populated
- [ ] Published Sub-Processor List — timestamped copies at each version on trust portal
- [ ] Controller Advance Notice records — evidence of 30-day advance notice for all sub-processor changes
- [ ] Controller Objection records — any objections received, response, and resolution
- [ ] Public disclosure version archive — DPO-maintained archive of previous privacy policy and ISO 27018 disclosure versions with effective dates
- [ ] Annual disclosure review records — DPO sign-off confirming all public disclosures are current
- [ ] Controller documentation request log — record of ISO 27018 documentation requests and responses

---

<!-- QA_VERIFIED: [Date] -->
