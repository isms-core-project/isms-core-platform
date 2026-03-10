<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.8-10-UG:privacy:UG:a.3.8-10 -->
**PRIV-IMP-A.3.8-10-UG — Identity, Access and Supplier Controls — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Identity, Access and Supplier Controls — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.8-10-UG |
| **Related Policy** | PRIV-POL-A.3.8-10 (Identity, Access and Supplier Controls) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.8-10 (Identity, Access and Supplier Controls — the governing policy)
- PRIV-IMP-A.3.8-10-TG (Identity, Access and Supplier Controls — Technical Guide)
- PRIV-POL-A.3.23-31 (Technical Security Controls for PII — authentication standards)
- PRIV-POL-A.2.2.2-7 (Processor Agreements and Obligations — processor contract content)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management — ISMS framework parallel)

---

## Purpose of This Guide

This guide explains **how to implement** the identity lifecycle, access rights, and supplier security requirements of PRIV-POL-A.3.8-10 from an operational perspective. It covers:

- How to provision, modify, and decommission identities with PII access
- How to manage access rights to PII and associated assets
- How to categorise suppliers and establish PII security requirements in agreements
- Timelines, approval flows, and review processes

**Who this guide is for**: IT Security Team, Data Owners, DPO, Line Management, Procurement, Legal/Compliance.

---

## Part 1 — Identity Lifecycle Management for PII (A.3.8)

### 1.1 Provisioning a New Identity with PII Access

When a new employee, contractor, or service account requires access to PII or PII processing systems:

**Step 1 — Justify**: Line manager submits an access request documenting:
- The role and its PII processing responsibilities
- The specific PII datasets or systems requiring access
- The business purpose for PII access
- Duration (permanent or time-limited)

**Step 2 — Approve**: Data Owner for the relevant PII dataset reviews and approves the access scope. Where multiple Data Owners are involved, each approves their dataset. DPO is notified for privileged access (see 1.4).

**Step 3 — Provision**: IT Security Team provisions the identity:
- Human identity: create account per ISMS identity management procedures; apply PII access scope as approved; register in Identity Register
- Non-human identity (service account): create dedicated service account (not shared); assign human owner; register in Identity Register with owner and purpose

**Step 4 — Record**: IT Security Team records the provisioning in the Access Rights Register (see PRIV-IMP-A.3.8-10-TG) with approval reference, access scope, and date.

**Step 5 — Notify**: Line manager receives confirmation of provisioned access. For time-limited access, the expiry date is communicated at provisioning.

### 1.2 Modifying Access on Role Change

When an individual changes role, moves to a different business unit, or their responsibilities change such that their current PII access scope no longer matches their role:

1. Line manager notifies IT Security Team and Data Owner within **1 business day** of the role change effective date
2. IT Security Team reviews current PII access rights against new role requirements
3. Rights no longer required are removed within **3 business days** of notification
4. New rights required by the new role follow the provisioning process (1.1)
5. Access Rights Register is updated to reflect the change

Do not wait for the annual access rights review to address role change access modifications — act immediately.

### 1.3 Decommissioning Access on Departure

When an employee or contractor leaves the organisation, or when a service account's purpose is discontinued:

| Scenario | Timeline |
|----------|----------|
| Planned departure (resignation, contract end) | Access removed on or before last working day |
| Immediate termination (dismissal, security incident) | Access suspended within 1 hour of HR notification |
| Contractor engagement end | Access removed on contract end date |
| Service account purpose discontinued | Access suspended immediately; decommissioning completed within 5 business days |

Process:
1. HR notifies IT Security Team of departure date (or immediately for terminations)
2. IT Security Team suspends all PII access on the last authorised day
3. Identity decommissioning is completed within the timeline above
4. Decommissioning is recorded in the Identity Register with date and method
5. Data Owner is notified of decommissioning for their PII dataset

If decommissioning is technically delayed: **suspend first, decommission later**. A suspended identity has no active access but the record is preserved for investigation and audit purposes.

### 1.4 Privileged PII Access

Privileged access to PII processing systems (database administrator, bulk data access, backup and recovery, system administration for PII environments) requires additional controls:

1. Requestor submits privileged access request to CISO with business justification
2. **DPO is notified** and confirms no privacy concerns with the privileged scope
3. **Data Owner approves** the privileged access scope for their dataset
4. IT Security Team provisions a **separate privileged identity** — never combine privileged PII access with a standard user identity
5. Enhanced audit logging is configured for all privileged sessions involving PII (see PRIV-IMP-A.3.8-10-TG)
6. Privileged access is reviewed every **6 months** (more frequent than standard annual review)
7. Any indication of misuse: revoke immediately and notify DPO

### 1.5 Annual Non-Human Identity Review

Each year, IT Security Team and Data Owners conduct a review of all non-human identities (service accounts) with PII access:

1. IT Security Team produces a list of all registered service accounts with PII access from the Identity Register
2. For each service account: contact the accountable human owner to confirm it is still required
3. Service accounts no longer required: decommission within 10 business days of confirmation
4. Service accounts where the owner has departed: reassign or decommission
5. Review results are documented and retained

---

## Part 2 — Access Rights Review for PII (A.3.9)

### 2.1 Annual Access Rights Certification

Once per year, Data Owners certify the access rights to their PII datasets:

**Process**:
1. IT Security Team generates a current access rights report per dataset/system from the Access Rights Register
2. Report is sent to the relevant Data Owner for review
3. Data Owner reviews each identity and access scope:
   - **Confirm**: identity still requires this access for a current business purpose → access continues
   - **Modify**: access scope has changed → flag for adjustment
   - **Remove**: identity no longer requires access → flag for removal
4. IT Security Team implements modifications and removals within **5 business days** of the Data Owner's certification
5. Removed rights are recorded in the Access Rights Register with removal date and reason
6. Data Owner signs off on the completed certification

**Scope**: All identities with access to PII datasets and systems must be covered in the annual certification. Non-human identities are reviewed in the same exercise.

### 2.2 Trigger-Based Access Review

In addition to the annual certification, access rights for PII must be reviewed when:

- An employee changes role (within 3 business days — see 1.2)
- A business unit is restructured or a processing purpose changes
- A privacy incident involved unauthorised or excessive PII access (review all access to affected dataset within 5 business days of incident closure)
- The Data Owner requests a review
- A DPIA identifies access control gaps

Trigger-based reviews are documented with the trigger event, scope, findings, and actions taken.

### 2.3 Time-Limited Access Expiry

Where access was provisioned with a defined expiry date:
- IT Security Team configures the system to automatically expire or flag the access at the expiry date
- If automatic expiry is not technically available: IT Security Team maintains an expiry calendar and manually removes access on the expiry date
- Extension requests are treated as new provisioning requests (see 1.1) and require Data Owner re-approval

---

## Part 3 — Supplier Security for PII (A.3.10)

### 3.1 Categorising a New Supplier for PII Requirements

Before signing any new supplier agreement where the supplier may have access to PII or PII processing systems, Procurement must complete a supplier PII categorisation:

**Step 1 — Assess**:

| Question | If Yes... |
|----------|----------|
| Will the supplier process PII on our behalf (under our instruction, for our purposes)? | Category: PII Processor |
| Will the supplier have access to our systems or environments that contain PII, even if not directly processing it? | Category: PII-Adjacent Supplier |
| Will the supplier have no access to PII or PII processing systems? | Category: No PII Access |

**Step 2 — Document**: Record the categorisation in the Supplier Agreement Inventory (see PRIV-IMP-A.3.8-10-TG) before agreement signature.

**Step 3 — Engage DPO/Legal**:
- PII Processor: engage DPO and Legal — a processor agreement (DPA) per GDPR Article 28 is required
- PII-Adjacent Supplier: engage DPO to confirm required clauses; Legal to draft or review
- No PII Access: standard ISMS supplier process applies (ISMS-POL-A.5.19-23) — no PII addendum needed

### 3.2 Mandatory PII Clauses for Supplier Agreements

For **PII Processor** and **PII-Adjacent Supplier** categories, the following clauses must be present in the agreement before signature. DPO and Legal confirm each clause is adequately addressed:

| Clause | Required For |
|--------|-------------|
| Security obligation (TOMs equivalent to ours) | Both categories |
| PII processing only on instruction | PII Processor |
| Prohibition on own-purpose use of PII | Both categories |
| Personnel confidentiality obligation (survives termination) | Both categories |
| Incident notification within agreed window (max 24 hours for breach risk) | Both categories |
| Sub-processor / subcontractor prior written consent + flow-down | PII Processor |
| Audit rights or third-party assessment acceptance | PII Processor |
| Return or secure deletion of PII on termination + written confirmation | Both categories |
| Regulatory compliance acknowledgment (GDPR/FADP) | Both categories |

For **PII Processor** agreements, additionally confirm all GDPR Article 28(3) mandatory elements are present (see PRIV-POL-A.2.2.2-7 for the full Article 28(3) checklist).

### 3.3 Annual Supplier Agreement Review

Each year, or upon contract renewal, DPO and Procurement review all active PII supplier agreements:

1. Procurement produces the current Supplier Agreement Inventory list for PII-categorised suppliers
2. For each active agreement: DPO confirms PII security clauses remain adequate given any changes to:
   - The nature or volume of PII processed
   - Applicable regulatory requirements
   - Supplier's security posture (based on audit reports, incidents, or certification status)
3. Agreements requiring update are flagged for renegotiation with a target timeline
4. Review is documented in the Supplier Agreement Inventory with outcome and next review date

### 3.4 Supplier PII Incidents

If a supplier reports a PII security incident (or if you become aware of one):
1. Notify DPO immediately
2. DPO activates the Privacy Incident Management procedure (PRIV-POL-A.3.11-12)
3. DPO reviews whether regulatory breach notification obligations apply
4. After incident resolution: DPO reviews the supplier's PII security clause compliance and determines whether agreement remediation or termination is warranted

---

## Evidence Checklist

- [ ] Identity Register — all human and non-human identities with PII access recorded
- [ ] Access Rights Register — current access rights per identity, dataset and system
- [ ] Annual access rights certification records (Data Owner sign-off)
- [ ] Role change access modification records (within required timeframes)
- [ ] Departure/decommissioning records (within required timeframes)
- [ ] Privileged access approval records (DPO notification + Data Owner approval)
- [ ] Supplier Agreement Inventory — all suppliers categorised for PII
- [ ] Signed supplier agreements with PII security clauses (for PII Processor and PII-Adjacent)
- [ ] Annual supplier agreement review records

---

<!-- QA_VERIFIED: [Date] -->
