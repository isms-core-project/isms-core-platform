<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.20-22-UG:privacy:UG:a.3.20-22 -->
**PRIV-IMP-A.3.20-22-UG — Physical Media and Endpoint Security — User Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Media and Endpoint Security — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | PRIV-IMP-A.3.20-22-UG |
| **Related Policy** | PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial user guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical or regulatory change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.20-22 (Physical Media and Endpoint Security — the governing policy)
- PRIV-IMP-A.3.20-22-TG (Physical Media and Endpoint Security — Technical Guide)
- PRIV-POL-A.3.5-7 (Information Classification and Transfer — classification scheme applied to media)
- PRIV-POL-A.3.11-12 (Privacy Incident Management — lost/stolen device response)

---

## Purpose of This Guide

This guide explains **how to implement** the media lifecycle, equipment disposal, and endpoint protection requirements of PRIV-POL-A.3.20-22. It covers how to build and maintain the Media Register and Disposal Register, how to execute secure erasure and disposal, and how to manage endpoint devices carrying PII.

**Who this guide is for**: CISO, IT Security Team, DPO, Data Owners, all personnel who use or handle storage media containing PII.

---

## Part 1 — Storage Media Lifecycle for PII (A.3.20)

### 1.1 Media Register — Acquisition and Initial Registration

When any removable or portable storage medium that will or may contain PII is acquired:

1. IT Security Team records the item in the Media Register within 2 business days of acquisition (see PRIV-IMP-A.3.20-22-TG for schema)
2. A unique Media ID is assigned
3. An owner is designated (the team or individual responsible for the medium)
4. Classification is left as "Not Yet Classified" until first use containing PII — the Data Owner confirms classification at first use

**What to register**: USB drives, portable hard drives, SSDs, external backup drives, optical media (DVDs, CDs), backup tapes, SD cards, and any other removable digital storage medium. Printed documents containing PII are managed per clear desk rules (PRIV-POL-A.3.17-19) and disposal rules below — they are not entered in the Media Register.

### 1.2 Media in Active Use

**Handling rules by classification** (classification per PRIV-POL-A.3.5-7):

| Media Classification | Encryption Required | Storage When Unattended | Transport Outside Premises |
|---------------------|--------------------|--------------------------|-----------------------|
| RESTRICTED (special category PII) | Mandatory — always, including within premises | Locked cabinet or locked equipment | Encrypted + secure courier; logged in transportation log |
| CONFIDENTIAL (ordinary PII) | Required for transport; recommended at rest within premises | Locked storage recommended | Encrypted media or secure courier; logged |
| INTERNAL (aggregated non-sensitive PII) | Recommended | Standard locked storage | Logged; standard internal procedures |

**Encryption requirement for RESTRICTED and CONFIDENTIAL media**: If a medium does not support hardware encryption, use software-based encryption (AES-256 minimum). See PRIV-IMP-A.3.20-22-TG for approved encryption standards.

### 1.3 Media Transportation Log

Every time media containing CONFIDENTIAL or RESTRICTED PII is transported outside secure premises:

1. Requester logs the movement in the Media Transportation Log before departure: medium ID, destination, purpose, escort or courier, expected return date
2. On return: confirm return date and that media is intact and returned to secure storage
3. Any failure to return on the expected date: escalate to IT Security Team on the first business day after expected return

**Loss or failure to return**: Treat as a suspected PII incident immediately — report to DPO per PRIV-POL-A.3.11-12.

### 1.4 Media Disposal

When a storage medium is no longer needed or has reached end of life:

1. IT Security Team identifies the medium in the Media Register
2. Confirm PII content (was this medium used for PII? What classification?)
3. Select appropriate erasure method per classification and medium type — see PRIV-IMP-A.3.20-22-TG for approved methods
4. Execute erasure and perform post-erasure verification scan
5. Update Media Register: status = Disposed; erasure method; verification outcome; date; responsible person
6. If using third-party destruction service: obtain certificate of destruction before the medium leaves [Organisation]'s custody; file in Disposal Register

**PII media must never go to standard waste or recycling** — even formatted media may retain recoverable data.

---

## Part 2 — Equipment Disposal and Re-use (A.3.21)

### 2.1 Pre-Disposal Checklist for All Equipment

Before any equipment containing storage media is disposed of or reassigned (whether to another internal user, sold, donated, or sent for recycling), IT Security Team must:

1. **Identify PII status**: Was this device used to store, process, or access PII? Check the Identity Register and Access Rights Register for the device's previous users and their PII access scope
2. **Perform erasure**: If PII was or may have been present, apply the appropriate erasure method per PRIV-IMP-A.3.20-22-TG
3. **Verify erasure**: Run post-erasure verification; document outcome
4. **Remove from active registers**: Update Identity Register (decommission associated accounts); remove from MDM/UEM
5. **Document in Disposal Register**: Asset ID, PII status, erasure method, verification outcome, disposal method, date, person responsible

### 2.2 Erasure Method Selection

| Scenario | Approved Method |
|----------|----------------|
| Standard HDD — PII present | Software overwrite (NIST SP 800-88 "Clear" level minimum); or physical destruction for RESTRICTED PII |
| SSD / Flash storage — PII present | Cryptographic erasure (where full-disk encryption confirmed throughout life) or physical destruction — software overwrite is NOT reliable on SSDs due to wear levelling |
| RESTRICTED PII on any media | Physical destruction of storage media (shredding, degaussing) — document destruction method and confirm no PII recovery is possible |
| Encrypted media (confirmed FDE active throughout life) | Cryptographic erasure — destroy or re-key the encryption key; document key destruction |
| Printer with internal storage | Factory reset to clear stored jobs and PII cache; verify using manufacturer documentation |

**When in doubt**: Choose physical destruction over software erasure — it is always more certain.

### 2.3 Internal Re-use (Reassignment)

When a device is reassigned from one user to another within [Organisation]:

1. Previous user's profile, files, and credentials removed — device imaged or reset to baseline configuration
2. PII erasure completed per step 2.2 (as if disposing externally, then re-imaging)
3. New user access provisioned per PRIV-POL-A.3.8-10
4. Update Identity Register: previous user decommissioned; new user provisioned
5. Record in Disposal Register: Asset ID; reassignment type (internal); previous user; new user; erasure method; date

### 2.4 Third-Party Disposal — Obtaining Certificates of Destruction

When equipment is sent to a third-party recycler or disposal service:

1. **Before handover**: Confirm the third party provides certified data destruction services (ISO 27001 certified or equivalent)
2. **At handover**: Obtain written commitment to provide a certificate of destruction per device or batch
3. **After destruction**: Certificate of destruction received, filed in Disposal Register, and retained for 5 years

**RESTRICTED PII equipment**: Physical destruction of storage media must be confirmed before equipment changes hands — do not rely on the third party's destruction as the sole safeguard. Where possible, remove and physically destroy the storage media on-site before shipping the equipment shell.

---

## Part 3 — Endpoint Device Protection for PII (A.3.22)

### 3.1 Provisioning Corporate Endpoints with PII Access

When provisioning a new corporate endpoint device that will access PII:

1. **Encrypt**: Confirm full-disk encryption (FDE) is enabled before the device is issued. IT Security Team verifies in the MDM/UEM console.
2. **Enrol**: Enrol device in corporate MDM/UEM solution — this enables remote wipe, policy enforcement, and patching compliance.
3. **Configure**: Apply screen lock, patch management, and endpoint protection policies per PRIV-IMP-A.3.20-22-TG minimum configuration standards.
4. **Register remote wipe**: Confirm remote wipe capability is active and registered in the endpoint management system.
5. **Test annually**: Remote wipe capability tested on a test device at minimum annually. Document test results.

### 3.2 Handling BYOD Requests for PII Access

Where a user requests PII access on a personal (BYOD) device:

1. DPO and CISO assess whether BYOD is appropriate for the PII category involved (RESTRICTED PII: strong presumption against BYOD unless exceptional circumstances)
2. If approved: user must sign the BYOD PII Agreement (see PRIV-IMP-A.3.20-22-TG for template) before PII access is granted
3. Device enrolled in MDM containerisation — PII workspace segregated from personal data
4. Confirm user understands: the organisation has the right to remotely wipe the managed workspace; this does not affect personal data outside the container
5. Record enrolment in the Endpoint Inventory

### 3.3 Bulk PII Downloads to Endpoints

Bulk download or local storage of PII from applications or databases onto endpoint devices is restricted:

| Scenario | Requirement |
|----------|-------------|
| Routine access — user views or edits individual PII records | No additional approval required — standard endpoint controls apply |
| Bulk download — export of >500 records for offline work | Data Owner approval required before download; must be encrypted at rest; deleted from endpoint when no longer needed; approval recorded |
| RESTRICTED PII stored locally | DPO notification required; encrypted container required; documented and time-limited |

### 3.4 Responding to Lost or Stolen Endpoints

**Immediate steps** (to be completed within 4 hours of confirmed loss):

1. Personnel report loss/theft to IT Security Team and line manager immediately on discovery — do not delay to investigate whether PII was present
2. IT Security Team initiates remote wipe or lock on the device via MDM/UEM
3. IT Security Team notifies DPO simultaneously — breach assessment begins
4. Credentials associated with the device are revoked (MDM certificates, cached credentials)
5. Remote wipe completion confirmed — logged in Disposal Register
6. DPO completes Personal Data Breach Assessment per PRIV-POL-A.3.11-12 (was PII accessible on the device? Was it encrypted? What categories? How many data subjects?)

**If device is subsequently recovered**: IT Security Team assesses whether it was accessed while lost; DPO updates breach assessment based on forensic findings.

---

## Evidence Checklist

- [ ] Media Register — all PII-bearing removable media registered, owned, classified
- [ ] Media Transportation Log — all external movements of PII media recorded
- [ ] Disposal Register — all equipment disposal and re-use actions documented, including erasure method and verification
- [ ] Certificates of Destruction — filed for all third-party equipment disposal
- [ ] Endpoint encryption status report — all corporate devices confirmed encrypted
- [ ] MDM/UEM enrolment records — all devices with PII access enrolled
- [ ] Remote wipe test record — capability tested within last 12 months
- [ ] BYOD PII Agreements — signed agreements on file for all BYOD devices with PII access
- [ ] Lost/stolen device records — response actions and breach assessment for any incidents

---

<!-- QA_VERIFIED: [Date] -->
