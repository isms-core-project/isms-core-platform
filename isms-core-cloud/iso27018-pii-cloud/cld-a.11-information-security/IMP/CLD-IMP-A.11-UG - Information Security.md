<!-- ISMS-CORE:IMP:CLD-IMP-A.11-UG:cloud:UG:a.11 -->
**CLD-IMP-A.11-UG — Information Security — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Security — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.11-UG |
| **Related Policy** | CLD-POL-A.11 (Information Security) |
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

**Review Cycle**: Annual (or upon significant infrastructure, technology, or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.11 (Information Security — the governing policy)
- CLD-IMP-A.11-TG (Information Security — Technical Guide)
- CLD-POL-A.10 (Accountability — breach notification triggered by security incidents)
- CLD-POL-A.5 (Data Minimisation — temporary file erasure alignment)
- CLD-POL-A.8 (Openness, Transparency — sub-processor disclosure)

---

## Purpose of This Guide

This guide explains how [Organisation] implements and documents the 13 security controls required by ISO/IEC 27018:2025 Section A.11 within its cloud services. It covers the operational responsibilities for encryption, access control, incident response, and processor agreement security provisions — and explains how these controls are documented for controller assurance.

**Who this guide is for**: CISO, Cloud Engineering, IT/Identity Management, Legal/Compliance, Data Protection Officer (DPO), HR (for onboarding/departure controls).

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. The 13 A.11 controls establish the information security floor for all PII processing. Gaps in any control represent potential GDPR Article 32 deficiencies and must be escalated to the CISO and DPO.

---

## Part 1 — Confidentiality, Hardcopy, and Media Controls (A.11.1–A.11.2, A.11.4–A.11.5, A.11.7)

### 1.1 Confidentiality and NDA Management (A.11.1)

Every individual who receives access to any [Organisation] system processing PII must have a signed NDA in place before access is granted. HR owns the NDA signing process on onboarding. The CISO maintains the NDA register.

If an individual requires access to PII systems and the NDA register does not show a current signed NDA, IT SHALL NOT provision that access. Escalate to HR and the DPO before proceeding.

NDAs must be re-confirmed on any significant role change and remain in force after departure. HR triggers NDA confirmation at offboarding and ensures departed personnel are reminded of their continuing obligation.

### 1.2 Restricting and Controlling Hardcopy PII (A.11.2)

Printing PII is the exception, not the default. Before printing any PII:

1. Confirm there is no digital alternative for the required purpose
2. Obtain written authorisation from your team lead (and DPO notation for large-volume prints)
3. Collect printed material immediately from the printer — do not leave PII unattended in shared printer trays
4. Apply secure desk procedures: lock away or shred at end of day; never leave PII visible on desks in shared spaces

All hardcopy PII must be disposed of per the secure disposal procedure in section 1.4 below.

### 1.3 Physical Media Leaving Premises (A.11.4)

Storage media (drives, tapes, removable media) containing PII may not leave [Organisation]'s facilities unless:

- Encryption is verified (full-disk or volume encryption per ISMS-POL-A.8.24), or
- The media has been physically destroyed to NIST SP 800-88 or equivalent standard

Any media movement must be authorised by the CISO or Cloud Security Manager in advance and logged in the media movement register. Track each item to its final destination (return or certified destruction facility).

If media is lost in transit, treat the event as a PII security incident immediately and notify the DPO.

### 1.4 Unencrypted Portable Devices (A.11.5)

Unencrypted USB drives, external hard drives, laptops, tablets, and mobile phones may not be used to store or transfer PII. This is an absolute prohibition.

For authorised portable devices: confirm with IT that full-disk encryption (AES-256 minimum) is active before any PII is transferred to the device. Remote wipe must be enabled for mobile devices.

Loss or theft of a portable device potentially containing PII: report to the CISO and DPO immediately. The event will be treated as a PII security incident under CLD-POL-A.10.1.

### 1.5 Secure Disposal of Hardcopy PII (A.11.7)

- **Individual disposal**: Use the cross-cut shredder (DIN 66399 Level P-4 or equivalent) available in each work area
- **Bulk disposal**: Use the designated locked bins; [Organisation]'s certified destruction partner collects and provides a certificate of destruction
- Retain certificates of destruction for 3 years

Do not place hardcopy PII in general waste or open recycling bins.

---

## Part 2 — Encryption and Transmission Security (A.11.6)

### 2.1 PII in Transit

All PII transmitted over public networks (including the internet, customer-facing APIs, and inter-region replication) must be encrypted using TLS 1.2 as an absolute minimum. TLS 1.3 is required for all new implementations.

HTTPS is mandatory on all web interfaces and API endpoints that handle PII. HTTP must redirect to HTTPS automatically. Unencrypted transmission (plain HTTP, FTP without TLS, SMTP without STARTTLS) of PII is prohibited.

Cloud Engineering reviews and documents cipher suite configurations annually. Weak ciphers (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) must be disabled. See CLD-IMP-A.11-TG for the encryption specification and current approved cipher suites.

### 2.2 TLS Certificate Management

TLS certificates must be issued by a trusted certificate authority. Certificates must be renewed before expiry; automated renewal (e.g., Let's Encrypt / ACME, or cloud-native certificate manager) is preferred to eliminate manual renewal gaps. Certificate expiry must be monitored with alerts set at 30 days and 7 days before expiry.

---

## Part 3 — Access Control and User Identity Management (A.11.8–A.11.10)

### 3.1 Unique User IDs (A.11.8)

Every individual with access to PII systems must have their own unique user identifier. Shared, generic, or role-based accounts are not permitted on systems where PII is processed or stored.

Service accounts (non-human accounts) are the only exception and require CISO approval plus enhanced controls (privileged access management, session recording). Submit a service account exception request to the CISO before provisioning.

### 3.2 User ID Lifecycle (A.11.9)

Follow the access lifecycle procedure for all PII system accounts:

| Lifecycle Stage | Action Required |
|-----------------|-----------------|
| New access request | Obtain documented authorisation from the user's manager and the system owner before requesting IT provisioning |
| Role change | Notify IT of the change within 1 business day; IT updates access within 1 business day of notification |
| Departure | HR notifies IT at confirmed departure; IT deactivates the account within 4 hours |
| Dormant account | IT flags accounts inactive for 90 days; team lead confirms business justification within 5 days or account is deleted |

Managers are responsible for notifying IT promptly on all role changes. Failure to notify on departure is a policy violation.

### 3.3 Authorised User Register (A.11.10)

The CISO or delegated system owner maintains an Authorised User Register for each PII system. The register is reviewed and attested quarterly. System owners must confirm or flag changes at each quarterly review.

Controllers may request a copy of the Authorised User Register for access to their PII at any time. The DPO coordinates this on request, providing only the access entries relevant to the requesting controller's data.

---

## Part 4 — Backup Restoration, Data Remanence, and Storage Controls (A.11.3, A.11.13)

### 4.1 Controlled Backup Restoration (A.11.3)

Restoring PII from backup or archive is a controlled operation. Before initiating any restoration:

1. Obtain documented authorisation from the team lead or incident commander
2. Log the restoration in the backup restoration log (see CLD-IMP-A.11-TG) before starting
3. Complete the restoration under the supervision of the authorised operator

Do not attempt self-service or ad-hoc restorations of PII data. Unplanned restoration attempts will be treated as security events.

The CISO reviews restoration logs quarterly.

### 4.2 Pre-used Storage Space — Data Remanence Prevention (A.11.13)

When storage is decommissioned or reallocated between customer workloads, Cloud Engineering must verify that prior data cannot be accessed. The standard method for cloud storage is cryptographic erasure (deletion of the encryption key for the prior volume). Physical overwrite is used where cryptographic erasure is not available.

Every decommissioning or reallocation event must be logged. Cloud Engineering tests the procedure annually by sampling reallocated storage and confirming no residual data. Multi-tenant PII isolation depends on this control; any failure is a potential PII incident.

---

## Part 5 — Processor Agreements and Sub-processor Obligations (A.11.11–A.11.12)

### 5.1 What Must Be in Every Processor Agreement (A.11.11)

Legal/Compliance maintains the standard processor agreement template. Every DPA between [Organisation] and a PII controller must include provisions covering:

- Scope and documented purpose of processing
- Security obligations (GDPR Article 32 alignment, reference to CLD-POL-A.11 controls)
- Breach notification (24-hour controller notification per CLD-POL-A.10.1)
- Data subject rights assistance (CLD-POL-A.2.1 and CLD-POL-A.9)
- Audit rights for the controller or appointed auditor
- Sub-processor approval and notification obligations
- PII return or deletion on termination (CLD-POL-A.10.3)
- Applicable law and jurisdiction

If a controller presents a non-standard DPA that omits any of these provisions, escalate to Legal/Compliance before signature.

### 5.2 Sub-processor Obligations (A.11.12)

Sub-processors must be bound by a written contract imposing obligations equivalent to the full CLD-POL-A.X suite. Key requirements that must appear in every sub-processor agreement:

- Mirror the controller's data protection obligations
- Require prior written consent from [Organisation] before any further sub-processing
- Require breach notification to [Organisation] within 12 hours of detection
- Require PII return or disposal on termination
- Include [Organisation]'s audit rights over the sub-processor

The CISO maintains a sub-processor audit programme. Each active sub-processor is audited at least annually (questionnaire, document review, or on-site). Audit results are documented and made available to controllers upon request.

[Organisation] remains fully accountable to PII controllers for sub-processor compliance failures. If a sub-processor fails an audit, escalate to the DPO and the relevant controller immediately.

---

## Evidence Checklist

- [ ] NDA register current — all individuals with PII system access have signed NDAs on file
- [ ] Print authorisation log maintained for the audit period
- [ ] Media movement register maintained with all physical media movements logged
- [ ] Backup restoration log maintained with authorisation records for all restoration events
- [ ] TLS configuration reviewed annually — weak ciphers disabled, TLS 1.2+ enforced
- [ ] Authorised User Register for each PII system attested quarterly
- [ ] Sub-processor audit records on file for the audit period (at least one audit per sub-processor)
- [ ] Storage decommissioning records maintained for all storage reallocations in the period

---

<!-- QA_VERIFIED: [Date] -->
