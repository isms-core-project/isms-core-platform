<!-- ISMS-CORE:IMP:CLD-IMP-A.10-UG:cloud:UG:a.10 -->
**CLD-IMP-A.10-UG — Accountability — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Accountability — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | CLD-IMP-A.10-UG |
| **Related Policy** | CLD-POL-A.10 (Accountability) |
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

**Review Cycle**: Annual (or upon significant regulatory or service model change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-POL-A.10 (Accountability — the governing policy)
- CLD-IMP-A.10-TG (Accountability — Technical Guide)
- CLD-POL-A.11 (Information Security — security controls underpinning accountability)
- CLD-POL-A.6 (Use, Retention and Disclosure Limitation — disclosure log cross-reference)
- CLD-POL-A.9 (Individual Participation and Access — data subject rights support)

---

## Purpose of This Guide

This guide explains how [Organisation] evidences and discharges its accountability obligations as a public cloud PII processor — specifically breach notification to PII controllers, management of processing activity records, DPO-level accountability reviews, and the return or secure disposal of PII at the end of a contract. It is the primary operational reference for staff involved in these activities.

**Who this guide is for**: Data Protection Officer (DPO), CISO, Cloud Service Delivery, Cloud Engineering, Legal/Compliance Officer.

**Cloud processor context**: This guide applies to [Organisation] acting as a public cloud PII processor under ISO/IEC 27018:2025. [Organisation]'s accountability obligations under A.10 run to the PII controller, not directly to data subjects or supervisory authorities.

---

## Part 1 — Maintaining Records of Processing Activities (A.10 Principle)

### 1.1 What Records Must Be Kept

[Organisation] SHALL maintain a **Processor Records of Processing Activities (RoPA)** capturing all processing performed on behalf of each PII controller. The RoPA covers the mandatory Article 30(2) GDPR fields and additional ISO 27018 fields. See CLD-IMP-A.10-TG for the full schema.

The DPO is responsible for maintaining the RoPA. Cloud Service Delivery must notify the DPO within **5 business days** of any change to:

- The categories of PII processed for a controller
- The purposes of processing
- Any new or changed sub-processor
- A change to the geographic location of processing (which also triggers CLD-POL-A.12.1 notification)
- Expiry or termination of a controller service agreement

### 1.2 Making Records Available

Upon a controller's request to inspect [Organisation]'s processing records, the DPO SHALL:

1. Retrieve the relevant controller's RoPA entry
2. Review for completeness and current accuracy
3. Provide the record to the controller within **5 business days** of the request (or within any shorter timeframe specified in the service agreement)

The same records SHALL be provided to a competent supervisory authority (e.g., a national DPA) upon official request, in consultation with Legal/Compliance.

### 1.3 Annual DPO Accountability Review

The DPO SHALL conduct an annual review of [Organisation]'s accountability posture as a cloud processor. The review SHALL cover:

1. Completeness of the Processor RoPA — all active controller agreements represented
2. Currency of sub-processor registers — all engaged sub-processors listed with current contract status
3. Document retention compliance — verification that all CLD-POL-A.X policy versions and processing records are retained per the schedule in CLD-POL-A.10.2
4. End-of-contract completions — confirmation that all terminated agreements in the period have received return or disposal confirmations
5. Breach notification review — all PII incidents in the period notified to controllers within 24 hours

The annual review output is a short **Accountability Review Report** (template in CLD-IMP-A.10-TG). The report is retained for 5 years.

---

## Part 2 — Breach Notification to PII Controllers (A.10.1)

### 2.1 Trigger

A PII security incident requiring controller notification is any event in which PII processed on behalf of a PII controller is subject to:

- Unauthorised access (including by [Organisation] staff or sub-processors)
- Accidental or unlawful disclosure, alteration, or destruction
- Ransomware or data loss affecting systems processing PII
- Any event that may engage the controller's own GDPR Article 33 notification obligation

### 2.2 The 24-Hour Notification Procedure

Immediately upon the CISO determining that a security event involves PII:

**Step 1 — Escalate to DPO** (within 2 hours of CISO determination). The DPO takes ownership of the controller notification track.

**Step 2 — Identify affected controllers** (within 4 hours). Using the Processor RoPA and sub-processor agreements, identify which controller(s)' PII may be affected.

**Step 3 — Draft notification** (within 12 hours). Use the breach notification template in CLD-IMP-A.10-TG. Include all available information; mark fields as "pending investigation" where facts are not yet confirmed.

**Step 4 — Issue notification** (within 24 hours of initial incident detection). Deliver via the controller's designated emergency contact channel documented in the service agreement.

**Step 5 — Issue phased updates** as investigation progresses. Provide updates whenever material new information is available, without further undue delay.

**Step 6 — Issue final incident report** (within 15 business days of incident closure). The final report confirms root cause, the full scope of PII affected, and remediation measures implemented.

### 2.3 Documentation

Every breach notification SHALL be logged in [Organisation]'s incident register with:

- Timestamp of initial detection
- Timestamp of CISO determination that PII is involved
- Timestamp of DPO notification to each affected controller
- Confirmation that notification fell within 24 hours
- References to the initial notification, phased updates, and final report

---

## Part 3 — PII Return, Transfer and Disposal at Contract End (A.10.3)

### 3.1 Initiating the End-of-Contract Process

The end-of-contract process begins when a cloud service agreement is confirmed as terminated or expired. Cloud Service Delivery notifies the DPO and CISO within **1 business day** of receiving termination notice or confirmation.

### 3.2 Confirming Controller Instruction

Within **5 business days** of termination notification, Cloud Service Delivery contacts the PII controller to confirm whether the controller requires:

- **Option A — Return**: PII returned in a machine-readable format (JSON, CSV, or agreed database export)
- **Option B — Disposal**: PII securely destroyed with a certificate of destruction provided

Where the service agreement specifies the default instruction (e.g., "disposal on termination unless return requested within 14 days"), follow the agreement.

### 3.3 Executing Return or Disposal

**Return (Option A)**:
1. Cloud Engineering prepares a complete export of the controller's PII from all active stores
2. Deliver the export to the controller via secure channel within **30 calendar days** of termination
3. Confirm delivery in writing and log in the end-of-contract record

**Disposal (Option B)**:
1. Cloud Engineering executes secure deletion of all primary PII stores
2. Initiate backup purge job and confirm with the backup operations team
3. Confirm sub-processor disposal (if sub-processors hold copies of the controller's PII)
4. Issue a **written certificate of destruction** to the controller within **30 calendar days** of termination (see template in CLD-IMP-A.10-TG)

### 3.4 Backup and Replicated Copies

Backup and replicated copies of a controller's PII SHALL be included in the return or disposal process. Where backup rotation cycles mean that purge cannot be completed within 30 days, the DPO SHALL:

1. Notify the controller of the expected purge completion date at the time of the initial return/disposal confirmation
2. Issue a second written confirmation when backup purge is complete

---

## Evidence Checklist

- [ ] Processor RoPA is current and covers all active controller agreements
- [ ] All PII incidents in the period were notified to affected controllers within 24 hours
- [ ] Breach notification records include timestamps confirming the 24-hour obligation was met
- [ ] Annual DPO Accountability Review Report completed and on file
- [ ] All terminated agreements in the period have written return or disposal confirmations on file
- [ ] Certificates of destruction issued for all disposal cases, including confirmation of backup purge
- [ ] Document retention schedule is enforced per CLD-POL-A.10.2 (5-year minimum for policies and processing records)

---

<!-- QA_VERIFIED: [Date] -->
