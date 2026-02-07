**ISMS-OP-POL-A.7.6-7-14 — Secure Areas and Media Handling**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Areas and Media Handling |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.6-7-14 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.7.6 — Working in secure areas
- ISO/IEC 27001:2022 Control A.7.7 — Clear desk and clear screen
- ISO/IEC 27001:2022 Control A.7.14 — Secure disposal or re-use of equipment
- ISO/IEC 27002:2022 Sections 7.6, 7.7, 7.14 — Implementation guidance
- NIST SP 800-88 Rev. 2 — Guidelines for Media Sanitization
- IEEE 2883:2022 — Standard for Sanitizing Storage

**Related Annex A Controls**:

| Control | Relationship to Secure Areas and Media Handling |
|---------|-------------------------------------------------|
| A.5.10–11 Acceptable use and return of assets | Defines acceptable use of equipment and asset return at end of lifecycle |
| A.5.12–13 Information classification and labelling | Classification level drives clear desk requirements and disposal method selection |
| A.7.1–2–3 Physical access control | Controls entry to secure areas; this policy governs conduct within them |
| A.7.8–9 Equipment siting and off-premises security | Physical placement and protection of equipment prior to disposal |
| A.7.10 Storage media | Media lifecycle management; this policy handles end-of-life disposal |
| A.8.10 Information deletion | Logical deletion requirements that complement physical disposal methods |

**Related Internal Policies**:

- Physical Access Control Policy
- Information Classification and Handling Policy
- Asset Management Policy
- Endpoint Security Policy

---

# Secure Areas and Media Handling Policy

## Purpose

The purpose of this policy is to ensure the protection of information within secure areas through appropriate working procedures, to prevent unauthorised access to information through clear desk and clear screen practices, and to prevent data leakage from equipment being disposed of or re-used.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) when working in secure areas and during equipment disposal. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Both frameworks require that personal data on equipment be rendered unrecoverable before disposal or re-use.

Controls A.7.6 (Working in Secure Areas), A.7.7 (Clear Desk and Clear Screen), and A.7.14 (Secure Disposal or Re-Use of Equipment) are combined because they address complementary aspects of physical information protection — from day-to-day workplace discipline through to end-of-life asset handling.

## Scope

All employees and third-party users.

All secure areas including server rooms, datacentres, security operations areas, and restricted offices.

All workspaces where information is processed, including desks, meeting rooms, shared spaces, and home offices.

All equipment containing storage media, including computers, servers, mobile devices, printers, copiers, USB drives, and network equipment.

## Principle

Information shall be protected from unauthorised access, disclosure, and recovery through appropriate physical and procedural controls applied throughout the information lifecycle — from creation and handling in secure areas, through daily workplace discipline, to secure disposal at end of life.

Disposal methods shall be proportionate to the sensitivity of the information stored, as determined by the information classification scheme.

Only organisation-approved sanitisation methods and tools shall be used for media disposal. Disposal of equipment containing personal data shall comply with Swiss nFADP requirements for rendering data unrecoverable.

The organisation shall maintain a register of approved sanitisation tools (e.g., [Secure Wipe Tool]) and approved destruction vendors (e.g., [Destruction Vendor]). This register shall be reviewed annually and updated when tools or vendors change.

---

## Working in Secure Areas (A.7.6)

ISO/IEC 27001:2022 Annex A.7.6 states:

> *Security measures for working in secure areas should be designed and implemented.*

### Access and Conduct

Personnel working in secure areas shall follow these requirements:

- Access to secure areas shall be granted only to authorised personnel based on job role and need-to-know principle.
- Personnel shall only be made aware of activities within secure areas on a need-to-know basis.

**Secure area information protection — scope of restriction**:

- **Prohibited disclosures**: Physical security controls (lock types, alarm systems, camera placements, access codes); specific contents of secure areas (equipment makes/models, configurations, data stored); access control procedures (badge types, escort requirements, approval process); vulnerabilities or security gaps in secure areas.
- **Permitted disclosures**: General existence of secure areas (e.g., "we have a server room") — not considered sensitive. High-level purpose (e.g., "it's where our IT infrastructure is") — acceptable for general awareness.
- **Guideline**: Employees should not volunteer detailed information about secure areas to external parties or unauthorised internal parties. If asked by an external party (vendor, visitor, interviewer), refer to Facilities Manager or CISO.
- **Violation scope**: Accidental disclosure of non-sensitive information (e.g., "the server room is on the second floor") is not a violation. Deliberate disclosure of access codes, alarm deactivation procedures, or security vulnerabilities is a violation subject to disciplinary action.
- Personnel shall not work alone in secure areas outside normal business hours unless an approved exception exists with compensating controls in place (e.g., check-in procedure with reception or colleague, CCTV monitoring, or buddy system).
- Empty secure areas shall be physically locked and periodically checked.
- Photography, video, audio, or other recording in secure areas shall be prohibited unless specifically authorised in writing by the Secure Area Owner.
- Mobile phones, cameras, and recording-capable devices shall not be brought into high-security areas (e.g., server rooms) unless authorised.

### Third-Party Access

- Third parties (contractors, vendors, visitors) shall be escorted at all times within secure areas.
- Third-party access shall be logged with entry and exit times and shall be time-limited to the duration of the specific task.
- Third parties shall sign a confidentiality or non-disclosure agreement before entering secure areas.
- Third-party equipment shall not be brought into secure areas unless authorised by the Secure Area Owner or Security Team.

**Third-party equipment inspection procedure** (secure areas):

Equipment categories requiring authorisation: Laptops, tablets, smartphones (beyond basic phone for emergency calls); external storage devices (USB drives, external HDDs); recording devices (cameras, audio recorders); wireless devices (Wi-Fi hotspots, Bluetooth devices, IoT gadgets); test equipment (oscilloscopes, network analysers with data logging).

Inspection procedure (by Facilities Manager or Security Team):
1. **Visual inspection**: Verify equipment matches description in authorisation request
2. **Wireless check**: Confirm wireless features disabled if required (aeroplane mode, Wi-Fi off) — visual confirmation or network scanner
3. **Recording check**: Verify no active recording (camera lens covered, audio recorder off)
4. **Logging**: Record equipment type, serial number, visitor name, entry time, exit time, approval reference

**High-risk equipment** (storage media, laptops): Additional step — confirm no connection to organisation network. If connected, disconnect immediately and log as incident. Alternative: organisation provides loaner equipment for work requiring computer access (preferred for extended visits).

**Equipment not authorised**: Denied entry; stored at reception until visitor departure. Visitor notified before entry.

**Emergency exception**: Emergency maintenance equipment (vendor's diagnostic laptop for urgent server repair) may be authorised by CISO with compensating controls (full-time escort, no network connection, work videotaped).

### Information Protection in Secure Areas

- Sensitive information shall not be discussed where it may be overheard by unauthorised persons.
- Sensitive documents shall be collected from printers, copiers, and fax machines immediately after printing.

**Whiteboard and flipchart handling in secure areas**:

| Classification | Handling Requirement |
|----------------|---------------------|
| **CONFIDENTIAL** | Prohibited on whiteboards/flipcharts — use digital presentation only, or printed materials collected afterward. If CONFIDENTIAL information is accidentally written: erase immediately, photograph erased board to verify no ghost image visible. If ghost image persists, board removed from service and replaced. Alternative: single-use paper flipcharts, collected and placed in confidential waste after meeting. |
| **INTERNAL** | Erase immediately after meeting. Meeting organiser verifies no ghost image (visual check). Photographs of whiteboards treated as INTERNAL classification. |
| **PUBLIC** | Best practice to erase; no verification required. |

Secure area meeting rooms: periodic whiteboard replacement (every 2 years) or use of digital whiteboards with no data persistence.
- Deliveries and external maintenance personnel shall have access restricted to the minimum area necessary. Unsupervised access to secure areas shall not be permitted.

### Secure Area Inventory

The organisation shall maintain a register of all designated secure areas, including:

- Location and physical boundaries of each secure area
- Designated Secure Area Owner responsible for access decisions
- Classification level of information typically processed or stored
- Specific additional rules applicable to the area (e.g., no mobile devices, escorted access only)

This register shall be reviewed annually or when organisational changes affect secure area designations.

---

## Clear Desk and Clear Screen (A.7.7)

ISO/IEC 27001:2022 Annex A.7.7 states:

> *Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities should be defined and appropriately enforced.*

### Clear Desk Requirements

**During Work Hours**:

- Sensitive documents shall be stored in locked drawers or cabinets when not in immediate active use.
- Documents awaiting printing shall be collected immediately using secure print release where available.
- Only documents actively being worked on shall be on desks. Accumulation of classified documents on desks is not permitted.

**End of Day / Extended Absence**:

- All sensitive documents shall be locked in drawers, cabinets, or safes.
- Removable storage media (USB drives, external drives, SD cards) shall be secured in locked storage.
- Access cards, keys, and tokens shall not be left unattended on desks.
- Notebooks and sticky notes containing passwords, PINs, or sensitive information shall be secured or destroyed.

**Classification-Specific Requirements**:

| Classification | During Work Hours | End of Day | Enforcement |
|----------------|-------------------|------------|-------------|
| **CONFIDENTIAL** | Locked when unattended (even briefly) | Locked storage mandatory | Mandatory — audit findings reported |
| **INTERNAL** | Face-down or covered when unattended | Locked storage at end of day | Mandatory — included in desk audits |
| **PUBLIC** | No specific restriction | Best practice to tidy | Advisory — best practice |

**Physical Media and Removable Storage**:

- Removable media containing classified information shall be locked away when not in use, regardless of classification level.
- Unmarked documents shall be treated as INTERNAL by default.
- Confidential waste bins shall be provided at workstations or in accessible locations for immediate disposal of sensitive paper documents.

### Clear Screen Requirements

**Screen Lock**:

Screen lock timeout shall be enforced via [Endpoint Management Tool] (Group Policy, MDM, or equivalent) with the following tiered policy:

| Workstation Type | Inactivity Timeout | Rationale |
|------------------|-------------------|-----------|
| **Standard workstations** (office, standard user access) | 5 minutes | General baseline |
| **Privileged workstations** (admin, database, security operations) | 2 minutes | Elevated access risk; immediate manual lock (Win+L / Ctrl+Cmd+Q) required when leaving desk |
| **Workstations in secure areas** (server rooms, SOC, executive offices) | 2 minutes | No exceptions |
| **Remote workers / laptops** | 3 minutes | Balance between security and mobile usability |
| **Public / untrusted locations** (airport, coffee shop) | 1 minute recommended | User discretion; policy-enforced 3-minute maximum |

**Enforcement**: Timeout settings deployed via [Endpoint Management Tool] with compliance monitoring quarterly. Non-compliant devices flagged for remediation within 5 business days.

- Users shall manually lock screens when leaving their workstation, even briefly, using keyboard shortcuts (Win+L on Windows, Ctrl+Cmd+Q on macOS).
- Password-protected screensavers or lock screens shall be enabled on all devices.
- Multi-factor authentication or secure biometric prompts should be used for unlocking active sessions on devices handling CONFIDENTIAL data.

**Privacy and Display**:

**Privacy screen requirements and enforcement**:

- **Mandatory for**: Laptops used outside the office (issued by IT as part of laptop kit); workstations in open-plan offices where CONFIDENTIAL data is regularly accessed (IT issues privacy screens to affected roles); anyone working in public locations (airport, train, coffee shop).
- **Verification**: IT includes privacy screen in laptop deployment checklist (signed by recipient). Annual desk audit includes privacy screen presence check for open-plan workstations handling CONFIDENTIAL data (10% sample). Remote work spot-check (via video call, quarterly, 5% sample): verify privacy screen usage when working outside home office.
- **Non-compliance**: First occurrence — reminder + privacy screen issued if missing. Repeated non-compliance — escalation to manager. Refusal to use issued privacy screen in CONFIDENTIAL-access role — revoke CONFIDENTIAL data access or relocate to enclosed office.
- **Cost**: Organisation-funded for mandatory roles (privileged access, CONFIDENTIAL data handlers). Optional for others (personal purchase).

- Sensitive information shall not be displayed on screens visible to unauthorised persons, including visitors and passers-by.
- Projector and screen sharing sessions shall be ended immediately after use. Presenters shall close sensitive applications before sharing screens.
- Virtual meeting backgrounds should be used where the physical environment may reveal sensitive information (e.g., whiteboards, documents on walls).
- Email and messaging notification pop-ups should be disabled or minimised during presentations and screen-sharing sessions.

**End of Day**:

- All applications containing sensitive data shall be closed.
- Workstations shall be logged off or shut down in accordance with IT policy.
- Remote desktop and VPN sessions shall be disconnected.

**Meeting Rooms**:

- Whiteboards and flipcharts shall be erased before the room is vacated.
- Meeting rooms with persistent displays (e.g., wall-mounted screens) shall not be left showing sensitive content after meetings end.

**Meeting room printed material handling**:

- **Pre-meeting (organiser)**: Handout count logged (number of copies printed); classification marking on each handout.
- **End of meeting (organiser)**: Count handouts collected vs. distributed. Leftover copies collected and either retained by organiser (if re-usable) or placed in confidential waste bin (if meeting-specific).
- **Attendee responsibility**: CONFIDENTIAL handouts returned to organiser or placed in confidential waste (do not take unless authorised). INTERNAL handouts may be retained if needed for work; otherwise return or confidential waste.
- **Meeting room post-meeting check** (daily, facilities/cleaning staff): Visual inspection for leftover documents. Any found documents delivered to [Designated Secure Collection Point] for review by CISO or Facilities Manager. Repeat findings (same meeting room, same organiser) escalated to organiser's manager.
- **Alternative**: Digital-only meetings for CONFIDENTIAL topics (no printed handouts). Presentation shared via secure portal, no downloads.

### Enforcement and Auditing

Clear desk and clear screen audits shall be conducted **monthly** (minimum 1, maximum 2 per month) by the Facilities Manager or designated auditor.

**Randomisation**:
- Audit date randomly selected within the month (1st–28th, varies each month). Audit time randomly selected within business hours (08:00–18:00, varies). No advance notice — employees informed of general monthly audit requirement during onboarding only.
- Audit locations: randomly sample 20% of desks per audit (different desks each month; full coverage over 5 months).

**Audit procedure**:
- Auditor uses standardised checklist (yes/no questions, no subjective scoring).
- Photographic evidence for non-compliant desks (blur sensitive content if visible).
- Second auditor spot-checks 10% of audited desks (quality control).

**Coverage target**: All employees audited at least twice per year. High-risk roles (CONFIDENTIAL data access): audited quarterly.

**Results and escalation**:
- Non-compliance reported to line managers within 2 business days.
- Repeated non-compliance (three or more findings in a 6-month period) escalated to HR for formal action.
- Aggregated results (not individual names) reported to Management Review quarterly.
- Audit results shall be reported as part of the ISMS management review.

---

## Secure Disposal or Re-Use of Equipment (A.7.14)

ISO/IEC 27001:2022 Annex A.7.14 states:

> *Items of equipment containing storage media should be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.*

### Pre-Disposal Assessment

Before any equipment is disposed of or re-used, the following assessment shall be completed:

1. **Data classification review** — Determine the maximum data classification ever stored on the equipment (not just current contents). This determines the required disposal method.
2. **Licensed software audit** — Identify and decommission licensed software per licensing terms. Licence keys shall be recovered or transferred where applicable.
3. **Asset record update** — Update [Asset Management System] to reflect the planned disposal or reassignment, including reason for disposal and proposed method.
4. **Personal data check** — Where equipment may have contained personal data, disposal shall comply with nFADP Art. 8 requirements for rendering data unrecoverable.

### Sanitisation Levels (NIST SP 800-88 Rev. 2)

The organisation adopts the NIST SP 800-88 Rev. 2 framework for media sanitisation, aligned with IEEE 2883:2022 technical recommendations:

| Sanitisation Level | Method | Description | Use Case |
|--------------------|--------|-------------|----------|
| **Clear** | Logical overwrite | Overwrites user-accessible storage locations with non-sensitive data using standard read/write commands. Protects against simple non-invasive data recovery. | PUBLIC data; internal re-use of low-sensitivity equipment |
| **Purge** | Cryptographic erase, block erase, or firmware-level commands | Renders data recovery infeasible using state-of-the-art laboratory techniques. Includes cryptographic erasure (destroying encryption keys on self-encrypting drives) and manufacturer secure erase commands per IEEE 2883. | INTERNAL data; internal re-use; external transfer |
| **Destroy** | Physical destruction | Renders media physically unusable through shredding, disintegration, pulverising, or incineration. Data recovery is infeasible regardless of effort. | CONFIDENTIAL data; all external disposal of sensitive media |

### Disposal Methods by Equipment Type and Classification

| Equipment Type | CONFIDENTIAL | INTERNAL | PUBLIC |
|----------------|--------------|----------|--------|
| **Hard Disk Drives (HDD)** | Physical destruction (shred to <2mm particles or degauss + shred); destruction certificate with serial number required | Purge: Manufacturer secure erase (ATA Secure Erase) per IEEE 2883, OR single-pass overwrite with verification using [Secure Wipe Tool]; physical destruction also acceptable | Clear: Quick format and OS reinstall |
| **Solid State Drives (SSD)** | Physical destruction (shred/disintegrate to <2mm particles) | Cryptographic erasure (self-encrypting drives with verified encryption) or manufacturer secure erase per IEEE 2883; physical destruction if crypto erase unavailable or unverifiable | Secure erase command |
| **Mobile Devices** | Physical destruction, OR if not feasible (leased device): factory reset + remote wipe + MDM disenrollment + CISO risk acceptance | Factory reset via MDM (remote wipe) + device UI wipe (double-wipe) + MDM disenrollment; encryption must have been enabled from deployment (verified via asset record) | Factory reset via device UI |
| **USB / Removable Media** | Physical destruction (shred) | Secure overwrite or physical destruction | Format |
| **Printers / Copiers** | Internal HDD/SSD removal + destruction | Internal HDD/SSD removal + secure wipe | Clear memory / factory reset |
| **Network Equipment** | Config wipe + destruction if flash storage present | Config wipe + verification + factory reset | Config reset |
| **Virtual / Cloud Storage** | Client-side encryption key deletion (organisation-managed keys) + cloud volume deletion + deletion confirmation log | Cryptographic erasure (delete volume + delete KMS keys) + deletion confirmation screenshot/log | Standard deletion via provider |

**HDD disposal rationale**: NIST SP 800-88 Rev. 2 (2023) confirms that a single pass of overwrite is sufficient for modern HDDs (manufactured after 2001); multi-pass overwrite (e.g., "3-pass") is a legacy requirement from older DoD standards and is no longer necessary. For INTERNAL classification, Purge-level methods (manufacturer secure erase or verified single-pass overwrite) are required — simple Clear-level methods are insufficient.

**SSD and flash media — cryptographic erasure verification**: Traditional overwrite methods are unreliable for SSDs due to wear-levelling, over-provisioning, and write amplification. Cryptographic erasure on self-encrypting drives (SEDs) is only effective if: (a) the drive was configured with encryption enabled throughout its lifecycle (verified via asset record), and (b) erasure command completion is verified. The following verification procedure shall be applied:

1. Confirm drive is a self-encrypting drive (check manufacturer documentation, not assumption)
2. Verify encryption was enabled throughout lifecycle (asset record)
3. Issue cryptographic erase command via manufacturer tool or ATA Security Erase
4. Verify command completion (tool reports success)
5. **Verification step**: Attempt data recovery using forensic tool on sample of erased drives (minimum 10% per batch, or all drives if <10 drives). If readable data found → escalate to physical destruction. If no readable data → approve for re-use/disposal.
6. **Risk acceptance**: If verification forensics not feasible (resource/time constraint), default to physical destruction for INTERNAL/CONFIDENTIAL SSDs.

**Mobile device disposal — encryption pre-requisite**: Device encryption shall be mandatory from day of deployment for all mobile devices handling INTERNAL or CONFIDENTIAL data (enforced via [MDM] policy, documented in device enrolment record). If a device was deployed without encryption (legacy, non-compliant): default to physical destruction regardless of data classification, and conduct root cause analysis for MDM policy remediation.

**Virtual and cloud storage**: Major cloud providers (AWS, Azure, GCP) do not issue individual destruction certificates for virtual storage. The organisation relies on provider SOC 2 Type II / ISO 27001 certification and data deletion attestations. Risk acceptance for reliance on provider deletion processes shall be documented annually in Management Review. For highest-sensitivity data: client-side encryption before uploading (organisation controls keys in on-premises HSM or separate KMS); upon disposal, delete organisation-managed keys and then delete cloud data; document key deletion with HSM/KMS audit log.

**IoT and embedded devices**: Devices with embedded storage that cannot be sanitised using standard tools (e.g., IoT sensors, building management controllers, medical devices) shall be physically destroyed if they have stored CONFIDENTIAL or INTERNAL data. Where physical destruction is not feasible, the organisation shall obtain vendor guidance on sanitisation and document the method and any residual risk.

#### IoT and Embedded Device Inventory

As a pre-requisite for disposal, the organisation shall maintain an inventory of IoT and embedded devices with storage:

**In-scope devices**: Building management systems (HVAC controllers, lighting), physical security devices (IP cameras, access controllers, alarm panels), network equipment with embedded storage (switches, routers, firewalls), smart office devices (printers with HDDs, smart displays, IoT sensors), and specialised equipment (medical devices, lab equipment, industrial controllers).

**Inventory requirements** — all in-scope devices recorded in [Asset Management System] with: device type, make, model, serial number; storage type and capacity (if known); data classification of information processed/stored; disposal method (sanitisation procedure or physical destruction); disposal contact (vendor, manufacturer, internal team).

Inventory maintained by Facilities + IT Operations, reviewed annually. Unknown devices found during facility changes shall be escalated to CISO for assessment; default assumption: may contain CONFIDENTIAL data → physical destruction.

### Re-Use Procedures

**Internal Re-Use**:

- All data shall be securely erased using an approved method appropriate to the previous data classification before reassignment.
- Licensed software shall be transferred or removed per licensing terms.
- [Asset Management System] shall be updated with the new assignee, date, and sanitisation record.
- Equipment shall be inspected and refurbished if necessary before redeployment.

**External Re-Use (Donation or Sale)**:

- Equipment that has stored CONFIDENTIAL data shall not be re-used externally. Storage media shall be physically destroyed.
- Equipment that has stored INTERNAL data shall have storage media destroyed or sanitised to Purge level before external transfer.
- All organisation identifiers (asset tags, stickers, etched markings) shall be removed.
- Factory defaults shall be restored.
- A record of the external transfer shall be maintained including recipient, date, and sanitisation evidence.

### Chain of Custody

**Internal Holding**:

- Equipment awaiting sanitisation or destruction shall be stored in a designated secure holding area with access limited to authorised disposal personnel.

**Holding area security requirements**:

- **Location**: Dedicated locked room or cage within IT operations area (not shared with general storage).
- **Physical security (minimum for all classifications)**: Lockable door with key control (keys issued to authorised personnel only — IT Operations Manager, Senior Technician, CISO). Access log maintained (manual sign-in/out or electronic badge reader). Area locked when unattended.
- **Additional security for CONFIDENTIAL equipment**: Holding area within alarmed secure area (server room or datacentre). 24/7 camera surveillance (recording retained 30 days). Two-person access rule (no single-person access to CONFIDENTIAL equipment).
- **Segregation**: CONFIDENTIAL equipment stored separately from lower-classification equipment (separate shelf, separate cage, or clearly marked zone). Equipment in locked anti-static bags or locked cabinets within holding area (additional layer).
- **Maximum holding time**: PUBLIC/INTERNAL — 30 days. CONFIDENTIAL — 10 business days (expedited disposal required). Equipment exceeding maximum holding time escalated to CISO for root cause investigation.
- **Inventory**: Reconciled weekly. Holding area inspected monthly by CISO or delegate.

**Off-Site Destruction**:

When equipment leaves the organisation's premises for destruction by an approved vendor, chain-of-custody documentation shall include:

- Handover date and time
- Asset identifiers (serial numbers, asset tags)
- Quantity and type of items
- Identity of releasing party (organisation representative)
- Identity of receiving party (vendor representative)
- Vendor transport reference or tracking number
- Expected destruction date

Certificates of destruction shall be obtained from the vendor and shall include individual serial numbers for each item destroyed. Certificates shall be matched against the handover record. Any discrepancies shall be escalated immediately and logged as a security event.

**Destruction certificate discrepancy response**:

Discrepancy types: missing items (fewer serial numbers on certificate than on handover record); extra items (serial numbers not on handover record); mismatched items (serial number doesn't match any handover item).

| Step | Action | Timeline |
|------|--------|----------|
| 1 | IT Operations contacts [Destruction Vendor] via account manager (phone + email) | Within 24 hours of discrepancy discovery |
| 2 | Vendor provides clarification (item still in transit, certificate error, etc.) | Within 48 hours |
| 3 | If vendor confirms item not destroyed: Escalate to CISO immediately (potential data breach — equipment with classified data unaccounted for) | Immediate |
| 4 | Vendor required to locate item within 5 business days, or provide sworn statement that item was destroyed (certificate error) | 5 business days |
| 5 | If vendor cannot locate or confirm destruction: Assume equipment lost/stolen (worst case). CISO + DPO determine if personal data was on equipment. Regulatory notification if required (nFADP Art. 24, GDPR Art. 33 where applicable). | Immediate upon determination |

**Vendor consequences**: Unresolved discrepancy triggers vendor removal from approved vendor list pending investigation outcome. All discrepancies documented in Destruction Discrepancy Log, reported to Executive Management quarterly (even if resolved).

### Documentation Requirements

**Disposal records** shall include:

- Equipment asset tag and serial number
- Data classification level (maximum ever stored)
- Sanitisation method and tool used (e.g., [Secure Wipe Tool], physical shredder model)
- Date of sanitisation or destruction
- Operator who performed the sanitisation (name, employee ID)
- **Authentication**: Operator digital signature or logged-in username from [Secure Wipe Tool] (automatic capture). For CONFIDENTIAL assets: second-person verification (witness name, signature, date).
- Completion status and verification result
- Person authorising disposal
- Certificate of destruction (where applicable, for external vendors)
- For CONFIDENTIAL assets: second-person verification of wipe/destruction

**Retention**: Disposal records, including certificates of destruction, shall be retained for **7 years**.

### Destruction Certificates

For all equipment destroyed by external [Destruction Vendor] or specialist suppliers:

- A certificate of destruction shall be obtained for every batch or individual item destroyed.
- Certificates shall reference individual serial numbers, not only batch identifiers.
- The destruction method shall be stated on the certificate (e.g., shredding to particle size, incineration).
- Paper documents containing CONFIDENTIAL or INTERNAL information shall be shredded to a minimum of DIN 66399 Security Level P-4 (or equivalent cross-cut standard).
- Certificates shall be filed with the corresponding disposal record and retained for 7 years.

### Approved Vendor Requirements

The organisation shall only use destruction vendors who:

- Hold relevant certifications (e.g., ISO 14001 for environmental management, EN 15713 for secure destruction services, or equivalent).
- Provide documented sanitisation or destruction procedures aligned with NIST SP 800-88 Rev. 2 or DIN 66399.
- Issue individual certificates of destruction with serial number traceability.
- Are subject to periodic due diligence review (at minimum annually).
- Maintain adequate insurance covering loss or data breach during transport and destruction.

Where on-site destruction is available, it should be preferred over off-site destruction for CONFIDENTIAL media to minimise chain-of-custody risk.

---

## SOC 2 Considerations

### Customer Data Disposal Tracking (CC6.5)

Systems and devices that processed customer data (CRM, application servers, databases, customer support laptops) shall be flagged in [Asset Management System] with a "Customer Data" attribute at deployment. At disposal:

- Disposal record must reference the customer data flag.
- CISO spot-checks 10% of customer-data-flagged disposals quarterly (verify wipe completion, certificate obtained).
- Audit trail: Disposal log filterable by "Customer Data" flag for SOC 2 audit sampling.

### Removable Media Disposal Tracking (CC6.7)

**Organisation-issued removable media** (USB drives, external HDDs issued by IT): Serial numbers recorded in [Asset Management System] at issuance. Employee signs asset acknowledgement (responsible for return or secure disposal at end of use). At employee termination: removable media verified returned (checklist item in offboarding process).

**Personal removable media used for work (BYOD USB)**: Generally prohibited for CONFIDENTIAL/INTERNAL data (per Acceptable Use Policy). If exception granted: user responsible for secure disposal at end of use; organisation provides secure disposal instructions and access to on-site shredder.

**Lost removable media**: Reported immediately (via incident management). If encrypted — low risk (document encryption status in incident report). If unencrypted — data breach assessment required.

### Personnel Security for Disposal Operations (CC6.1)

Roles with disposal responsibilities (IT Operations, Facilities personnel authorised for holding area access) shall be subject to background screening per A.6.1 requirements (minimum Standard level screening). Additional requirement for CONFIDENTIAL equipment disposal: Enhanced screening level (see A.6.1 screening levels table). Documented in role-to-screening-level mapping (maintained by HR + CISO).

---

## Optional: Payment Card Data Controls (PCI DSS)

*Applicable only if payment card data is processed and PCI scope exists.*

If PCI scope exists, the following additional requirements apply:

- Media containing cardholder data shall be physically destroyed when no longer needed for business or legal reasons (PCI DSS Requirement 9.4).
- An inventory of media containing cardholder data shall be maintained and reconciled at least annually.
- Secure disposal of cardholder data media shall be documented with destruction certificates retained per PCI DSS Requirement 9.4.7.

---

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Executive Management** | Approve policy; allocate resources for secure area operations, disposal infrastructure, and vendor contracts |
| **CISO** | Policy ownership; define sanitisation standards; oversee compliance; approve disposal exceptions |
| **Facilities Manager** | Secure area management; conduct monthly clear desk audits; manage secure holding area; coordinate vendor access |
| **IT Operations** | Execute equipment sanitisation; verify wipe completion; maintain disposal records and wipe logs; manage [Secure Wipe Tool] |
| **Line Managers** | Ensure team compliance with clear desk/screen; authorise equipment disposal for their teams; address audit findings |
| **Procurement / Vendor Management** | Manage [Destruction Vendor] contracts; verify vendor certifications; collect destruction certificates |
| **All Personnel** | Follow secure area conduct rules; maintain clear desk and clear screen; report lost or improperly disposed equipment |
| **HR** | Enforce disciplinary action for repeated non-compliance; coordinate clear desk requirements during employee exit |

**Escalation Path**:

- Clear desk violations: Auditor --> Line Manager --> HR (for repeated violations)
- Equipment disposal questions: IT Operations --> CISO
- Secure area incidents: Security / Facilities --> CISO --> Executive Management
- Missing destruction certificates: IT Operations --> Procurement --> CISO

---

## Evidence for This Policy

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | Clear desk and clear screen audit checklists | Facilities Manager | Monthly | 12 months |
| 2 | Secure area access and visitor escort logs | Facilities Manager | Continuous | 12 months |
| 3 | Screen lock compliance reports (endpoint management) | IT Operations | Quarterly | 12 months |
| 4 | Equipment disposal records (asset tag, classification, method, date, operator) | IT Operations | Per disposal event | 7 years |
| 5 | Certificates of destruction from [Destruction Vendor] | Procurement | Per destruction event | 7 years |
| 6 | Secure wipe verification logs (tool output per asset) | IT Operations | Per wipe event | 7 years |
| 7 | Chain-of-custody handover records for off-site destruction | IT Operations | Per transfer event | 7 years |
| 8 | [Asset Management System] disposal status entries | IT Operations | Per disposal event | Life of asset record |
| 9 | Secure area incident reports (unauthorised access, recording, lone working) | CISO | Per event | 3 years |
| 10 | Clear desk audit non-compliance escalation records | Facilities Manager / HR | Per occurrence | 12 months |
| 11 | Vendor due diligence records for destruction service providers | Procurement | Annual review | Duration of contract + 2 years |
| 12 | Policy acknowledgement records (secure area conduct, clear desk) | HR | Annual | Duration of employment + 1 year |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to:

- Monthly clear desk and clear screen audits with documented results.
- Quarterly screen lock timeout compliance checks via endpoint management reporting.
- Semi-annual review of equipment disposal records against the asset register to identify unaccounted disposals.
- Annual review of [Destruction Vendor] contracts, certifications, and destruction certificate completeness.
- Internal and external audits, and feedback to the policy owner.

**Governance Metrics**:

| Metric | Target |
|--------|--------|
| Clear desk audit pass rate | > 95% |
| Screen lock timeout compliance | 100% |
| Disposal with certificate (CONFIDENTIAL) | 100% |
| Secure wipe verification completed | 100% |
| Destruction certificate serial number match rate | 100% |
| Secure area incidents (unauthorised access, recording) | 0 |

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date not exceeding 6 months. Exceptions shall be reported to the Management Review Team.

Permitted exceptions include:

- Extended screen lock timeout for specific operational requirements (e.g., monitoring dashboards), with enhanced physical access controls in place.
- Alternative disposal methods for legacy equipment where standard tools are incompatible, with documented risk acceptance.
- Temporary relaxation of clear desk requirements for project war rooms, with enhanced access controls and time-limited approval.

Exceptions shall not be granted for:

- Eliminating disposal verification for equipment that stored CONFIDENTIAL data.
- Permanent bypass of screen lock requirements.
- Disposal of equipment without documented authorisation.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

Improper disposal of equipment containing personal data may additionally constitute a breach of Swiss nFADP, potentially resulting in regulatory investigation by the Federal Data Protection and Information Commissioner (FDPIC) and, where applicable, EU data protection authorities.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to sanitisation standards (including NIST SP 800-88 updates and IEEE 2883 revisions), new storage technologies (e.g., NVMe, persistent memory), regulatory changes, audit findings, and disposal incidents.

---

# Areas of the ISO 27001 Standard Addressed

Secure Areas and Media Handling Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.1 Actions to address risks | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| Clause 7.5 Documented information | 6.4 Disciplinary process |
| Clause 8.1 Operational planning and control | **7.6 Working in secure areas** |
| Clause 10.2 Nonconformity and corrective action | **7.7 Clear desk and clear screen** |
| | **7.14 Secure disposal or re-use of equipment** |

# Regulatory Framework

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; rendering personal data unrecoverable before disposal |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security including physical protection |
| EU GDPR (where applicable) | Art. 5(1)(f) — Integrity and confidentiality; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Controls 7.6, 7.7, 7.14 |
| ISO/IEC 27002:2022 | Sections 7.6, 7.7, 7.14 — Implementation guidance |
| NIST SP 800-88 Rev. 2 | Guidelines for media sanitisation (Clear, Purge, Destroy) |
| IEEE 2883:2022 | Standard for sanitizing storage — technical methods for drives |
| DIN 66399 | Destruction of data carriers — security levels for physical shredding |

---

<!-- QA_VERIFIED: 2026-02-07 -->
