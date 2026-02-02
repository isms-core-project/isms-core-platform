**ISMS-POL-A.7.6-7-14 — Secure Areas and Media Handling**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Secure Areas and Media Handling |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.6-7-14 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Facilities Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.7.1-2-3 (Physical Access Control)
- ISMS-POL-A.7.10 (Storage Media)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-IMP-A.7.6-7-14 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.7.6, A.7.7, A.7.14

---

## Executive Summary

This policy establishes [Organisation]'s requirements for working in secure areas, clear desk and clear screen practices, and secure disposal or re-use of equipment.

**Purpose**: Define requirements for secure area procedures, information protection during work activities, and secure equipment disposal. This policy establishes WHAT security requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.6-7-14.

**Scope**: All personnel working in secure areas, all workspaces where information is processed, and all equipment being disposed of or re-used.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Controls

### Control A.7.6 - Working in Secure Areas

> *Security measures for working in secure areas should be designed and implemented.*

**Control Objective**: Protect information and assets in secure areas by ensuring personnel follow appropriate security procedures.

### Control A.7.7 - Clear Desk and Clear Screen

> *Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities should be defined and appropriately enforced.*

**Control Objective**: Reduce risk of unauthorised access, loss of, or damage to information during and outside normal working hours.

### Control A.7.14 - Secure Disposal or Re-Use of Equipment

> *Items of equipment containing storage media should be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.*

**Control Objective**: Prevent leakage of information from equipment being disposed of or re-used.

**Control Type**: Preventive
**Control Category**: Physical

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Secure Areas** | Server rooms, datacenters, security operations centres, executive offices, R&D facilities |
| **Workspaces** | All desks, meeting rooms, shared spaces, home offices |
| **Equipment** | All devices containing storage media (computers, servers, phones, printers, copiers) |
| **Personnel** | All employees, contractors, visitors accessing secure areas or using organisation equipment |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Article 8 - Technical measures; Article 6 - Data minimisation |
| **EU GDPR** | Article 5(1)(f) - Integrity and confidentiality; Article 32 - Security |
| **ISO/IEC 27001:2022** | Controls A.7.6, A.7.7, A.7.14 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **PCI DSS v4.0** | Payment card processing | Requirement 9 - Physical access restrictions |
| **FINMA** | Swiss financial institution | Information protection requirements |
| **DORA** | EU financial services | ICT security measures |

---

# Policy Statements

## Working in Secure Areas

### Access and Conduct

Personnel working in secure areas should follow these requirements:

**Access Controls**:
- Access to secure areas should be granted only to authorised personnel
- Access should be based on job role and need-to-know principle
- Visitors in secure areas should be escorted at all times
- Access rights should be reviewed quarterly and revoked when no longer required

**Conduct in Secure Areas**:
- Personnel should only be aware of activities within secure areas on a need-to-know basis
- Unsupervised working in secure areas should be avoided for safety and security reasons
- Empty secure areas should be locked and periodically checked
- Photography, video, audio, or other recording should be prohibited unless specifically authorised

**Information Protection**:
- Sensitive information should not be discussed where it may be overheard
- Whiteboards and flipcharts should be erased after meetings
- Sensitive documents should be removed from printers immediately
- Clean desk requirements should be enforced in all secure areas

### Third-Party Access

**Contractor and Visitor Requirements**:
- Third parties should be escorted in secure areas
- Third-party access should be logged and time-limited
- Third parties should sign confidentiality agreements before access
- Third-party equipment should be inspected before entry where appropriate

## Clear Desk and Clear Screen

### Clear Desk Requirements

**During Work Hours**:
- Sensitive documents should be stored securely when not in immediate use
- Documents awaiting printing should be collected immediately
- Only documents actively being worked on should be on desks

**End of Day / Extended Absence**:
- All sensitive documents should be locked in drawers or cabinets
- Removable storage media (USB drives, external drives) should be secured
- Access cards and keys should not be left on desks
- Notebooks and sticky notes with sensitive information should be secured

**Classification-Specific Requirements**:

| Classification | Clear Desk Requirement |
|----------------|----------------------|
| **CONFIDENTIAL** | Locked storage mandatory when unattended |
| **INTERNAL** | Locked storage at end of day |
| **PUBLIC** | Best practice but not mandatory |

### Clear Screen Requirements

**Screen Lock**:
- Workstations should automatically lock after maximum 5 minutes of inactivity for CONFIDENTIAL data, 10 minutes for INTERNAL data
- Users should manually lock screens (Win+L / Ctrl+Cmd+Q) when leaving workstation
- Password-protected screensavers should be enabled

**Information Display**:
- Sensitive information should not be displayed where it can be viewed by unauthorised persons
- Privacy screens should be used in open-plan offices and public areas
- Projector and screen sharing sessions should be ended immediately after use
- Virtual meeting backgrounds should be used where sensitive information may be visible

**End of Day**:
- All applications should be closed
- Workstations should be logged off or shut down per IT policy
- Sensitive documents should be closed before leaving workstation

### Enforcement

**Verification**:
- Random clear desk audits should be conducted monthly
- Non-compliance should be reported to line managers
- Repeated non-compliance should be escalated to HR

**Evidence Repository**:
- Audit checklists stored in [GRC Platform] - Compliance Module
- Non-compliance records maintained for 12 months

## Secure Disposal or Re-Use of Equipment

### Pre-Disposal Requirements

**Assessment**:
- All equipment should be assessed for sensitive data and licensed software before disposal
- Equipment containing storage media should be identified and handled per this policy
- Asset management records should be updated to reflect disposal

**Data Classification Review**:
- Maximum data classification ever stored on equipment should be determined
- Disposal method should match classification level

### Disposal Methods

**Physical Destruction** (Required for CONFIDENTIAL data):
- Storage media should be physically destroyed (shredding, degaussing, disintegration)
- Destruction should be performed by approved service providers
- Certificate of destruction should be obtained and retained
- Destruction should be witnessed or verified

**Secure Overwriting** (Acceptable for INTERNAL data):
- Data should be overwritten using approved secure deletion tools
- Minimum three-pass overwrite for magnetic media
- Cryptographic erasure for encrypted storage (SSD, flash)
- Verification of successful erasure should be performed

**Standard Deletion** (Acceptable only for PUBLIC data):
- Standard deletion tools may be used
- Format and reinstall acceptable

### Disposal Methods by Equipment Type

| Equipment Type | CONFIDENTIAL | INTERNAL | PUBLIC |
|----------------|--------------|----------|--------|
| Hard Drives (HDD) | Physical destruction | 3-pass overwrite or destruction | Format |
| Solid State Drives (SSD) | Physical destruction | Cryptographic erase or destruction | Secure erase |
| Mobile Devices | Physical destruction | Factory reset + verification | Factory reset |
| USB/Removable Media | Physical destruction | Secure overwrite or destruction | Format |
| Printers/Copiers | HDD removal + destruction | HDD removal + secure wipe | Clear memory |
| Network Equipment | N/A (config wipe) | Config wipe + verification | Config reset |

### Re-Use Requirements

**Internal Re-Use**:
- All data should be securely erased before reassignment
- Licensed software should be transferred or removed per licensing terms
- Asset records should be updated with new assignee
- Equipment should be inspected and refurbished if necessary

**External Re-Use (Donation/Sale)**:
- CONFIDENTIAL equipment should NOT be re-used externally
- INTERNAL equipment should have storage media destroyed or securely wiped
- All organisation identifiers should be removed
- Factory defaults should be restored

### Documentation

**Disposal Records** should include:
- Equipment asset tag and serial number
- Data classification level
- Disposal method used
- Date of disposal
- Person authorising disposal
- Certificate of destruction (where applicable)
- Verification evidence

**Retention**: Disposal records should be retained for 7 years.

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy, allocate resources |
| **CISO** | Policy ownership, disposal standards, compliance oversight |
| **Facilities Manager** | Secure area management, clear desk audits |
| **IT Operations** | Equipment disposal execution, secure wipe verification |
| **Line Managers** | Team compliance with clear desk/screen, authorise equipment disposal |
| **All Personnel** | Follow secure area rules, maintain clear desk/screen, report incidents |

**Escalation Path**:
- Clear desk violations: Auditor → Line Manager → HR (repeated violations)
- Disposal questions: IT Operations → CISO
- Secure area incidents: Security → CISO → Executive Management

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Clear desk audits | Monthly | Facilities Manager | Audit checklists |
| Secure area compliance review | Quarterly | Security Team | Access logs, incident reports |
| Equipment disposal audit | Semi-annual | IT Operations | Disposal records, certificates |
| Screen lock compliance | Quarterly | IT Operations | Endpoint management reports |

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Clear desk audit pass rate | >95% | Monthly audit results |
| Screen lock compliance | 100% | Endpoint management data |
| Disposal with certificate | 100% (CONFIDENTIAL) | Disposal records |
| Secure wipe verification | 100% | Wipe logs |
| Secure area incidents | 0 | Incident reports |

## Exception Management

Policy exceptions require:
- Documented business justification
- Risk assessment
- Compensating controls
- CISO approval
- Time-limited approval (maximum 6 months)

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.6 - Working in Secure Areas** | Applicable | This policy, ISMS-IMP-A.7.6-7-14 |
| **A.7.7 - Clear Desk and Clear Screen** | Applicable | This policy, ISMS-IMP-A.7.6-7-14 |
| **A.7.14 - Secure Disposal or Re-Use of Equipment** | Applicable | This policy, ISMS-IMP-A.7.6-7-14 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.7.1-2-3** | Physical access control for secure areas |
| **A.7.10** | Storage media management lifecycle |
| **A.8.10** | Information deletion requirements |
| **A.5.10-11** | Asset lifecycle including disposal |
| **A.5.12-13** | Information classification driving disposal requirements |

---

# Definitions

| Term | Definition |
|------|------------|
| **Secure Area** | A physically protected location with access controls where sensitive information is processed or stored |
| **Clear Desk** | Practice of removing all sensitive materials from desks when not in use |
| **Clear Screen** | Practice of locking or logging off computer screens when unattended |
| **Secure Disposal** | Methods of disposing of equipment that prevent data recovery |
| **Cryptographic Erasure** | Destroying encryption keys to render encrypted data unrecoverable |
| **Degaussing** | Using magnetic fields to erase data from magnetic storage media |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.6-7-14 v1.0)
- ✅ Approval signatures from CISO, Facilities Manager, Executive Management
- ✅ Secure area requirements documented (Section 2.1)
- ✅ Clear desk/screen requirements documented (Section 2.2)
- ✅ Disposal requirements documented (Section 2.3)
- ✅ Roles and responsibilities assigned (Section 3)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Clear desk audit results | [GRC Platform] - Compliance Module | Monthly audits using checklist | Facilities Manager | 3 years |
| Secure area access logs | [Physical Access System] | Automated logging | Security Team | 1 year |
| Equipment disposal records | [Asset Management System] | Per disposal event | IT Operations | 7 years |
| Destruction certificates | [GRC Platform] - Evidence Library | From disposal vendors | IT Operations | 7 years |
| Screen lock compliance | [Endpoint Management Platform] | Monthly automated reports | IT Operations | 1 year |

**Evidence Accessibility**: All evidence SHALL be accessible to auditors upon request within 2 business days.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Facilities Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes [Organisation]'s requirements for secure areas and media handling. Implementation procedures are documented in ISMS-IMP-A.7.6-7-14.*

<!-- QA_VERIFIED: [Date] -->
