<!-- ISMS-CORE:IMP:CLD-IMP-A.12-UG:cloud:UG:a.12 -->
**CLD-IMP-A.12-UG — Privacy Compliance — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Compliance — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.12-UG |
| **Related Policy** | CLD-POL-A.12 (Privacy Compliance) |
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

**Review Cycle**: Annual (or upon significant regulatory, service footprint, or data residency change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.12 (Privacy Compliance — the governing policy)
- CLD-IMP-A.12-TG (Privacy Compliance — Technical Guide)
- CLD-POL-A.8 (Openness, Transparency — sub-processor disclosure cross-reference)
- CLD-POL-A.11.12 (Sub-contracted PII Processing — sub-processor location obligations)
- CLD-POL-A.1 (General — foundational processor obligations)

---

## Purpose of This Guide

This guide explains how [Organisation] monitors and maintains compliance with its ISO/IEC 27018:2025 obligations, manages the annual privacy compliance review cycle, responds to changes in applicable law or standard revisions, and prepares for customer and controller audits. It is the primary operational reference for the DPO and CISO in discharging the A.12 principle.

**Who this guide is for**: Data Protection Officer (DPO), CISO, Cloud Engineering, Legal/Compliance Officer, Cloud Service Delivery.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. A.12 compliance requires active monitoring of geographic processing locations, transfer mechanisms, and the regulatory landscape — not merely a one-time implementation.

---

## Part 1 — Maintaining and Disclosing PII Processing Locations (A.12.1)

### 1.1 The PII Processing Locations Register

The DPO owns and maintains a **PII Processing Locations Register** covering all countries and regions where [Organisation] stores, processes, or transmits PII as part of cloud service delivery. The register must be kept current at all times.

The register covers:
- Primary storage locations (data centres and cloud regions where PII at rest resides)
- Processing (compute) regions
- Transit routes through which PII may pass during replication, backup, or delivery
- Sub-processor geographic locations (each must be named)

Cloud Engineering notifies the DPO within **5 business days** of any change to PII processing geography, including:
- Opening a new service region
- Adding a new sub-processor in a new jurisdiction
- Relocating backup storage
- Any infrastructure change that moves PII to a jurisdiction not currently in the register

The DPO updates the register within 5 business days of receiving notification of the change.

### 1.2 Controller Access to the Register

The PII Processing Locations Register is available to PII controllers on request. The DPO provides the register (or the relevant controller-specific subset) within **5 business days** of a controller request. For controllers operating under general authorisation, the register is linked from [Organisation]'s trust portal or provided as an annex to the DPA.

### 1.3 Enforcing Data Residency Constraints

Where a controller's service agreement specifies a geographic residency requirement (e.g., "EU-only storage", "Switzerland only"):

1. Cloud Engineering implements the technical residency constraint (regional infrastructure configuration, geo-fencing, storage policy rules) before PII processing begins under that agreement
2. The DPO documents the technical mechanism used and attaches the documentation to the relevant controller's service file
3. Cloud Engineering audits residency compliance at least annually, confirming that no PII has been stored or processed outside the agreed regions
4. Audit results are reported to the DPO within 10 business days of completion

If an audit identifies a residency violation, escalate to the CISO and DPO immediately and notify the affected controller within **24 hours**.

### 1.4 Location Change Notification

Before changing the geographic location of PII processing, the DPO must:

1. Identify all affected controllers (those whose PII will be stored or processed in the new location)
2. Issue advance notice to affected controllers with a minimum **30 days' notice** (unless the service agreement specifies a longer period)
3. Obtain prior consent from controllers whose agreements require explicit consent (not merely general authorisation) for location changes
4. Update the PII Processing Locations Register within 5 business days of the change taking effect

For **emergency location changes** (e.g., data centre failure, force majeure): notify affected controllers without undue delay, even if the change has already occurred. Document the retroactive justification in the change record.

---

## Part 2 — Annual Privacy Compliance Review (A.12 Monitoring)

### 2.1 The Annual Review Cycle

The DPO conducts an **annual ISO 27018:2025 Compliance Review** covering the full Annex A control set. The review assesses [Organisation]'s compliance posture as a cloud processor and identifies gaps requiring remediation.

The review SHALL be completed within the first quarter of each calendar year (or within 12 months of the prior review). The output is a **Compliance Self-Assessment Report** (structure in CLD-IMP-A.12-TG).

The review covers:
- Full ISO 27018:2025 Annex A control self-assessment (all A.1–A.12 controls and sub-controls)
- Review of the PII Processing Locations Register for completeness and currency
- Review of transfer mechanism instruments (SCCs, IDTAs, Swiss clauses) for continued validity
- Review of adequacy decision status for all third countries to which PII is transferred
- Review of sub-processor compliance records (audit results, agreements, locations)
- Identification of any regulatory changes (new laws, court decisions, adequacy revocations) affecting [Organisation]'s compliance position

### 2.2 Handling Gaps Identified in the Review

For each gap identified:

1. Assign a remediation owner (CISO, DPO, Legal/Compliance, or Cloud Engineering as appropriate)
2. Set a target remediation date (30 days for critical gaps; 90 days for significant gaps; next review cycle for minor gaps)
3. Track remediation in the compliance gap register
4. Report material gaps to Executive Management

If a gap represents a current compliance deficiency affecting controller PII (e.g., an expired transfer mechanism, a residency violation), notify the affected controller(s) within **5 business days** of identification.

---

## Part 3 — Responding to Changes in Applicable Law or Standards (A.12)

### 3.1 Monitoring for Regulatory Changes

Legal/Compliance is responsible for monitoring changes to applicable law and ISO standards relevant to [Organisation]'s processor obligations. Triggers for a compliance review outside the annual cycle include:

- A new or amended data protection law applicable to any jurisdiction where [Organisation] processes PII
- Revocation of an EU or Swiss adequacy decision affecting a current transfer destination
- Publication of a new version of ISO/IEC 27018 or ISO/IEC 27701
- A material court ruling affecting standard contractual clauses or other transfer mechanisms (e.g., equivalent to Schrems II)

When a trigger event is identified, Legal/Compliance notifies the DPO within **5 business days**. The DPO assesses the impact on [Organisation]'s current compliance posture and determines whether:

- Transfer mechanisms for specific destinations must be updated
- The PII Processing Locations Register must be revised
- Controllers must be notified of changes to their DPA
- An out-of-cycle compliance assessment is required

### 3.2 Adequacy Decision Revocation

If an adequacy decision is revoked for a country to which [Organisation] currently transfers PII:

1. Legal/Compliance notifies the DPO within **5 business days** of the revocation taking effect
2. Legal/Compliance implements or confirms alternative transfer mechanisms (SCCs, IDTAs, BCRs) within **30 days**
3. Where no alternative mechanism can be implemented within 30 days, the DPO notifies affected controllers immediately and suspends transfers to that destination until a mechanism is in place
4. The Transfer Destination Records (CLD-IMP-A.12-TG) are updated with the new mechanism within **5 business days** of implementation

---

## Part 4 — Preparing for Controller and Customer Audits

### 4.1 Types of Controller Audit

Controllers may audit [Organisation]'s compliance with their DPA and with ISO 27018:2025 obligations. Audit types include:

- **Document review**: Controller requests copies of policies, control documentation, and evidence records
- **Questionnaire audit**: Controller sends a standardised questionnaire (e.g., based on CAIQ, ISO 27001 controls, or custom DPA questions)
- **On-site audit**: Controller or appointed external auditor conducts an on-site review

The DPO co-ordinates all controller audits. Cloud Engineering and Legal/Compliance provide technical and legal support as required.

### 4.2 Audit Preparation Checklist

Use the checklist in CLD-IMP-A.12-TG (Audit Preparation Checklist) before each scheduled or unscheduled controller audit. At a minimum, verify that the following are current and available for inspection:

1. PII Processing Locations Register (complete, current)
2. Transfer Destination Records with valid transfer mechanism instruments
3. Sub-processor list with agreement references and last audit date
4. CLD-POL-A.X policy set (all 12 policies, current versions)
5. ISO 27018:2025 Annex A Compliance Self-Assessment Report (current year)
6. Processor RoPA entry for the requesting controller (per CLD-IMP-A.10-TG)
7. Residency audit results confirming no out-of-scope processing
8. Breach notification records for the audit period

### 4.3 Responding to Audit Findings

If a controller audit identifies non-conformities:

1. The DPO acknowledges the finding to the controller within **5 business days**
2. The CISO assesses technical findings; Legal/Compliance assesses contractual findings
3. A remediation plan is shared with the controller within **15 business days**
4. Remediation progress is reported to the controller at agreed intervals

---

## Evidence Checklist

- [ ] PII Processing Locations Register is current, complete, and reflects all active regions and sub-processor locations
- [ ] Data residency constraints are technically enforced; annual residency audit completed
- [ ] All location changes in the period were notified to affected controllers with 30 days' advance notice
- [ ] Annual ISO 27018:2025 Compliance Self-Assessment Report completed and on file
- [ ] Transfer mechanism instruments (SCCs, IDTAs, etc.) reviewed and current for all non-EEA/non-Swiss destinations
- [ ] Adequacy decision status checked for all third-country transfer destinations
- [ ] Regulatory change monitoring process active; any trigger events in the period assessed and documented
- [ ] Audit preparation checklist completed before any controller audit in the period

---

<!-- QA_VERIFIED: [Date] -->
