<!-- ISMS-CORE:IMP:CLD-IMP-A.12-TG:cloud:TG:a.12 -->
**CLD-IMP-A.12-TG — Privacy Compliance — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Compliance — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | CLD-IMP-A.12-TG |
| **Related Policy** | CLD-POL-A.12 (Privacy Compliance) |
| **Document Creator** | CISO / Data Protection Officer (DPO) |
| **Document Owner** | CISO / Data Protection Officer (DPO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27018:2025 Ed. 3 implementation |

**Review Cycle**: Annual (or upon significant regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.12 (Privacy Compliance — the governing policy)
- CLD-IMP-A.12-UG (Privacy Compliance — User Guide)
- CLD-POL-A.11 (Information Security — sub-processor and security control obligations)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and templates** for [Organisation]'s ISO/IEC 27018:2025 privacy compliance programme. It covers:

- ISO 27018:2025 Annex A compliance self-assessment matrix (all controls vs implementation status)
- Audit preparation checklist
- Regulatory change impact assessment template
- Transfer destination record schema

**Audience**: CISO, DPO, Cloud Engineering, Legal/Compliance.

---

## 1. ISO/IEC 27018:2025 Annex A Compliance Self-Assessment Matrix

Complete this matrix annually as part of the DPO Annual Privacy Compliance Review. For each control, assess implementation status and record the primary evidence reference. Update after any out-of-cycle review triggered by a regulatory change.

**Assessment date**: \_\_\_\_\_\_\_\_\_\_\_\_ | **Assessed by**: \_\_\_\_\_\_\_\_\_\_\_\_ | **Approved by**: \_\_\_\_\_\_\_\_\_\_\_\_

| Control | Description | Status | Evidence Reference | Gap / Remediation |
|---------|-------------|--------|-------------------|-------------------|
| **A.1 — General** | | | | |
| A.1 (principle) | Public cloud PII processor obligations established | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.1 | |
| **A.2 — Consent and Choice** | | | | |
| A.2.1 | Co-operation for withdrawal of consent / rights | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.2 | |
| **A.3 — Purpose Legitimacy** | | | | |
| A.3 (principle) | Processing only per documented controller instructions | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.3 | |
| **A.4 — Collection Limitation** | | | | |
| A.4 (principle) | PII collection limited to what controllers supply | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.4 | |
| **A.5 — Data Minimisation** | | | | |
| A.5.1 | PII minimised in service delivery | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.5 | |
| A.5.2 | Temporary files erased after use | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.5 | |
| **A.6 — Use, Retention and Disclosure** | | | | |
| A.6.1 | Purpose limitation — no secondary use | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.6 | |
| A.6.2 | No disclosure without controller instruction | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.6 | |
| A.6.3 | Disclosure log maintained | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.6 | |
| A.6.4 | Retention schedule and deletion on expiry | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.6 | |
| **A.7 — Accuracy and Quality** | | | | |
| A.7 (principle) | Rectification and quality mechanisms available | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.7 | |
| **A.8 — Openness, Transparency and Notice** | | | | |
| A.8.1 | Sub-processor list disclosed and maintained | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.8 | |
| A.8.2 | Controller notified of sub-processor changes | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.8 | |
| **A.9 — Individual Participation and Access** | | | | |
| A.9 (principle) | Rights fulfilment capabilities documented and tested | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.9 | |
| **A.10 — Accountability** | | | | |
| A.10.1 | Breach notification within 24 hours of detection | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.10 | |
| A.10.2 | Document retention schedule enforced | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.10 | |
| A.10.3 | PII return / disposal on contract termination | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.10 | |
| **A.11 — Information Security** | | | | |
| A.11.1 | NDAs in place for all personnel with PII access | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.2 | Hardcopy PII restrictions enforced | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.3 | Backup restoration logged and controlled | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.4 | Physical media encrypted or destroyed before leaving premises | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.5 | Unencrypted portable devices prohibited | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.6 | TLS 1.2+ enforced for PII in transit | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.7 | Hardcopy disposal by certified cross-cut shredding | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.8 | Unique user IDs — no shared accounts on PII systems | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.9 | User ID lifecycle managed (provisioning to deactivation) | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.10 | Authorised User Register maintained and attested quarterly | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.11 | Contract measures in all DPAs | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.12 | Sub-processors under equivalent contracts; audited annually | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| A.11.13 | Pre-used storage cryptographically erased before reallocation | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.11 | |
| **A.12 — Privacy Compliance** | | | | |
| A.12.1 | PII Processing Locations Register maintained and disclosed | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.12 | |
| A.12.2 | Transfer destinations documented with valid transfer mechanisms | ☐ Compliant / ☐ Partial / ☐ Gap | CLD-POL-A.12 | |

**Overall compliance rating**: ☐ Compliant | ☐ Minor gaps (remediation tracked) | ☐ Material gaps (remediation required — notify management)

---

## 2. Audit Preparation Checklist

Use this checklist before any scheduled or unscheduled controller audit. The DPO leads preparation; Cloud Engineering and Legal/Compliance provide supporting evidence.

| # | Item | Responsible | Status | Location / Reference |
|---|------|-------------|--------|----------------------|
| 1 | PII Processing Locations Register — current, complete, accessible | DPO | ☐ Ready | |
| 2 | Transfer Destination Records — all non-EEA/non-Swiss destinations documented with transfer mechanism | DPO / Legal | ☐ Ready | |
| 3 | Transfer mechanism instruments on file (SCCs, IDTAs, BCRs, adequacy citations) | Legal | ☐ Ready | |
| 4 | Sub-processor list — current with agreement references and last audit date | CISO / DPO | ☐ Ready | |
| 5 | CLD-POL-A.1 through A.12 — all current policy versions accessible | DPO | ☐ Ready | |
| 6 | ISO 27018:2025 Compliance Self-Assessment (Section 1 above) — current year completed | DPO | ☐ Ready | |
| 7 | Processor RoPA entry for the requesting controller | DPO | ☐ Ready | |
| 8 | Data residency audit results (confirming no out-of-scope processing for controllers with residency constraints) | Cloud Engineering | ☐ Ready | |
| 9 | Breach notification records for the audit period | DPO / CISO | ☐ Ready | |
| 10 | Authorised User Register attestations for the audit period (quarterly) | CISO | ☐ Ready | |
| 11 | Sub-processor audit records for the audit period | CISO | ☐ Ready | |
| 12 | End-of-contract return / disposal confirmations for the audit period | DPO | ☐ Ready | |

**Preparation completed by**: \_\_\_\_\_\_\_\_\_\_\_\_ **Date**: \_\_\_\_\_\_\_\_\_\_\_\_

---

## 3. Regulatory Change Impact Assessment Template

Complete this template whenever Legal/Compliance identifies a regulatory trigger event (new law, adequacy revocation, standards revision, material court ruling).

```
REGULATORY CHANGE IMPACT ASSESSMENT
Reference: RCIA-[YYYY]-[NNN]
Date of trigger event: [Date]
Event description: [Brief description of the regulatory change]
Identified by: [Legal / Compliance / DPO / CISO]
Date notified to DPO: [Date]

IMPACT ASSESSMENT

1. AFFECTED JURISDICTIONS
   [List all jurisdictions where [Organisation] processes PII that are affected by the change]

2. AFFECTED CONTROLS / OBLIGATIONS
   [List A.12 and other CLD-POL-A.X controls affected, and the nature of the impact]

3. AFFECTED TRANSFER MECHANISMS
   [List any transfer mechanisms (SCCs, adequacy decisions, IDTAs) that are affected or invalidated]

4. AFFECTED CONTROLLERS
   [List or describe categories of controllers whose DPAs or residency constraints are affected]

5. REQUIRED ACTIONS
   Action | Owner | Deadline | Status
   -------|-------|----------|-------
   [E.g., implement SCCs for [country] transfers] | Legal | [date] |
   [E.g., notify affected controllers] | DPO | [date] |
   [E.g., update Transfer Destination Records] | DPO | [date] |
   [E.g., update PII Processing Locations Register] | DPO | [date] |

6. ESCALATION REQUIRED
   ☐ No escalation required — gap addressed within normal operations
   ☐ Escalation to Executive Management required — material compliance gap
   ☐ Controller notification required — [date of planned notification]

Assessed by (DPO): _________________________ Date: _________
Reviewed by (Legal): _________________________ Date: _________
Approved by (CISO): _________________________ Date: _________
```

---

## 4. Transfer Destination Record Schema

Maintain one record per transfer destination. Update whenever a new destination is added, a transfer mechanism changes, or an existing record requires review following a regulatory change.

| Field | Type | Description |
|-------|------|-------------|
| `destination_id` | String | Unique reference for this transfer destination record |
| `destination_country` | String | Country or jurisdiction of the transfer destination |
| `destination_entity` | String | Name of the entity receiving the transfer (sub-processor, cloud provider, DR site) |
| `transfer_purpose` | Text | Operational reason (e.g., backup, support access, DR replication) |
| `pii_categories_transferred` | List | Categories of PII included in the transfer |
| `transfer_mechanism` | Enum | Adequacy decision / EC SCCs (2021) / UK IDTA / Swiss SCCs / BCRs / Other |
| `mechanism_instrument_ref` | String | Reference to the legal instrument on file (e.g., DPA annex, SCC addendum reference) |
| `adequacy_decision_ref` | String | Citation of applicable adequacy decision (if mechanism is adequacy) |
| `supplementary_safeguards` | Text | Technical or contractual safeguards supplementing the mechanism (e.g., encryption in transit, DPA clause) |
| `controller_notified` | Boolean | Whether affected controllers have been notified of this destination |
| `last_reviewed` | Date | Date this record was last reviewed for continued validity |
| `reviewed_by` | String | DPO or Legal/Compliance officer who performed the review |
| `status` | Enum | Active / Under review / Suspended / Terminated |
| `notes` | Text | Any relevant context (e.g., TIA reference for high-risk jurisdictions) |

**Retention**: Duration of active engagement + 5 years.

---

<!-- QA_VERIFIED: [Date] -->
