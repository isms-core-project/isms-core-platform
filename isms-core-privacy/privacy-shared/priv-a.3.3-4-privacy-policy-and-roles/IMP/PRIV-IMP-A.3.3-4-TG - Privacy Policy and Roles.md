<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.3-4-TG:privacy:TG:a.3.3-4 -->
**PRIV-IMP-A.3.3-4-TG — Privacy Policy and Roles — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Policy and Roles — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.3-4-TG |
| **Related Policy** | PRIV-POL-A.3.3-4 (Privacy Policy and Roles) |
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
| 1.0 | [Date to be set] | DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant policy or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.3-4 (Privacy Policy and Roles — the governing policy)
- PRIV-IMP-A.3.3-4-UG (Privacy Policy and Roles — User Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)

---

## Purpose of This Guide

This guide specifies the **technical structures, templates, and configurations** required to implement PRIV-POL-A.3.3-4. It covers:

- PIMS Policy Register structure and mandatory fields
- Privacy Roles Register data specification
- DPO Appointment Record template
- DPO Role Conflict Assessment template
- Policy Acknowledgment Record template
- Document management requirements

**Audience**: DPO, CISO, system administrators responsible for document management and privacy register tooling.

---

## 1. PIMS Policy Register

The PIMS Policy Register is the authoritative list of all current PIMS policy documents. It is owned by the DPO and updated on every policy publication, revision, or retirement.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| Document ID | Text | Unique policy identifier (e.g., PRIV-POL-A.3.3-4) |
| Document Title | Text | Full policy title |
| Version | Text | Current approved version (e.g., 1.0) |
| Status | Enum | Draft / Active / Under Review / Retired |
| Owner | Text | Role responsible for the policy (typically DPO) |
| Approved By | Text | Approving authority (typically Executive Management) |
| Approval Date | Date | Date of most recent approval |
| Review Due Date | Date | Date of next scheduled review |
| Control References | Text | ISO 27701:2025 controls covered |
| Location | URL/Path | Document repository path or URL |
| Notes | Text | Outstanding actions, known issues |

### Minimum Register Contents at First Certification

| Document ID | Document Title |
|-------------|----------------|
| PRIV-POL-00 | Privacy Regulatory Applicability Framework |
| PRIV-POL-01 | Privacy Governance and Decision-Making Framework |
| PRIV-POL-A.3.3-4 | Privacy Policy and Roles |
| PRIV-POL-A.3.5-7 | Information Classification and Transfer |
| PRIV-POL-A.3.8-10 | Identity, Access and Supplier Controls |
| PRIV-POL-A.3.11-12 | Privacy Incident Management |
| PRIV-POL-A.3.13-16 | Compliance, Audit and Review |
| PRIV-POL-A.3.17-19 | Privacy Awareness, NDAs and Clear Desk |
| PRIV-POL-A.3.20-22 | Physical Media and Endpoint Security |
| PRIV-POL-A.3.23-31 | Technical Security Controls for PII |
| PRIV-POL-A.1.2.2-5 | Lawful Basis and Consent |
| PRIV-POL-A.1.2.6-9 | Privacy Governance and Records |
| PRIV-POL-A.1.3.2-4 | Transparency and Information Provision |
| PRIV-POL-A.1.3.5-10 | Data Subject Rights |
| PRIV-POL-A.1.3.11 | Automated Decision Making |
| PRIV-POL-A.1.4.2-5 | Data Minimisation |
| PRIV-POL-A.1.4.6-10 | PII Lifecycle, Retention and Disposal |
| PRIV-POL-A.1.5.2-5 | PII Transfer and Disclosure |
| PRIV-POL-A.2.2.2-7 | Processor Agreements and Obligations |
| PRIV-POL-A.2.3.2 | PII Principal Obligations (Processor) |
| PRIV-POL-A.2.4.2-4 | Processor Lifecycle Controls |
| PRIV-POL-A.2.5.2-6 | Transfer and Disclosure (Processor) |
| PRIV-POL-A.2.5.7-9 | Sub-processor Management |

### Tooling

The register may be maintained in:
- A spreadsheet (minimum viable for first certification)
- A GRC platform with document management capability
- The ISMS CORE API platform (when PRIVACY module is available)

The register must support version history and audit trail (who changed what, when).

---

## 2. Privacy Roles Register

The Privacy Roles Register is the authoritative record of all privacy and security role assignments. It is owned by the DPO and updated on every appointment, change, or vacancy.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| Role ID | Text | Unique identifier (e.g., PRIV-ROLE-DPO-01) |
| Role Title | Text | Standard title per PRIV-POL-A.3.3-4 |
| Role Category | Enum | Privacy Role / Security Role / Management Role |
| Incumbent Name | Text | Full name of current appointee |
| Employee/Contractor ID | Text | HR reference (if applicable) |
| Appointment Date | Date | Date of formal written appointment |
| Appointment Document Ref | Text | Reference to signed appointment letter/record |
| Scope | Text | Processing activities or domains covered |
| Reporting Line | Text | Role to which this role reports |
| Competence Status | Enum | Meets Requirements / In Progress / Gap Identified |
| Review Date | Date | Date of next annual role review |
| Status | Enum | Active / Vacant / Interim / Retired |
| Notes | Text | Interim cover details, outstanding competence gaps |

### Mandatory Roles Minimum Set

| Role ID | Role Title | Mandatory Basis |
|---------|-----------|-----------------|
| PRIV-ROLE-DPO | Data Protection Officer | GDPR Art. 37 (where applicable); PRIV-POL-A.3.3-4 |
| PRIV-ROLE-CISO | Chief Information Security Officer | PRIV-POL-A.3.3-4 |
| PRIV-ROLE-PC-[BU] | Privacy Champion — [Business Unit] | PRIV-POL-A.3.3-4 (per BU with material PII activity) |
| PRIV-ROLE-DO-[ACT] | Data Owner — [Processing Activity] | PRIV-POL-A.3.3-4 (per processing activity) |
| PRIV-ROLE-AUD | PIMS Internal Auditor | ISO 27701:2025 Clause 9.2 |

---

## 3. DPO Appointment Record Template

The DPO Appointment Record formalises the DPO appointment and confirms independence. Retain for duration of appointment + 3 years.

```
DPO APPOINTMENT RECORD

Organisation: [Organisation Legal Name]
Date of Appointment: [Date]
Appointee Name: [Full Name]
Appointee Contact: [Email] / [Phone]
Published Contact (external): [DPA registration / website URL]

SCOPE OF APPOINTMENT
This appointment covers the role of Data Protection Officer for [Organisation] in accordance
with EU GDPR Article 37 [and/or CH FADP Article — where applicable].

The DPO is appointed for all processing activities carried out by [Organisation] as
PII Controller and/or PII Processor, as documented in the Record of Processing Activities.

INDEPENDENCE CONFIRMATION
The DPO does not currently hold any of the following roles:
[ ] Chief Executive Officer or equivalent
[ ] Chief Operating Officer or equivalent
[ ] Head of IT / CTO or equivalent
[ ] Head of HR or equivalent
[ ] Head of Marketing or equivalent
[ ] Any other role that determines purposes and/or means of PII processing

Annual DPO Role Conflict Assessment must be completed each year to maintain this confirmation.

REPORTING LINE
The DPO reports directly to: [Executive Management / CEO / Board level]
The DPO has the right to escalate directly to: [Board / CEO]

RESOURCES AND SUPPORT
[Organisation] confirms the DPO has access to:
[ ] Legal/Compliance support as required
[ ] Budget for training and certification
[ ] Access to all PII processing systems and documentation
[ ] Right to attend management meetings where privacy matters are discussed

SIGNED
Appointee: _________________________ Date: ___________
Executive Management: _________________________ Date: ___________
```

---

## 4. DPO Role Conflict Assessment Template

Complete annually. Retain for duration of appointment + 3 years.

```
DPO ROLE CONFLICT ASSESSMENT

DPO Name: [Name]
Assessment Date: [Date]
Assessment Conducted By: [Name — may be DPO themselves or independent reviewer]
Period Covered: [Date] to [Date]

CURRENT ROLES AND RESPONSIBILITIES HELD BY DPO

| Role/Responsibility | Description | Determines Processing Purposes? | Determines Processing Means? | Conflict? |
|---------------------|-------------|--------------------------------|------------------------------|-----------|
| [Role 1]            |             | Yes / No                       | Yes / No                     | Yes / No  |
| [Role 2]            |             | Yes / No                       | Yes / No                     | Yes / No  |

ASSESSMENT CONCLUSION

[ ] No conflict identified — DPO independence confirmed for the assessment period
[ ] Conflict identified — see below

CONFLICT DETAILS (if applicable):
[Describe conflict, affected role, and proposed remediation]

REMEDIATION PLAN (if applicable):
[Action, responsible party, target date]

SIGN-OFF
DPO: _________________________ Date: ___________
Executive Management: _________________________ Date: ___________
```

---

## 5. Policy Acknowledgment Record Template

Used to record that a member of personnel has read and acknowledged a PIMS policy. May be implemented as a spreadsheet row, GRC platform task completion record, or signed form.

### Required Data Fields

| Field | Description |
|-------|-------------|
| Personnel Name | Full name |
| Role | Current role title |
| Policy Document ID | e.g., PRIV-POL-A.3.3-4 |
| Policy Version | e.g., 1.0 |
| Acknowledgment Date | Date of acknowledgment |
| Method | Email confirmation / signed form / platform task completion |
| Recorded By | Name of person who recorded the acknowledgment |

### Acknowledgment Statement (to be presented to personnel)

> *"I confirm that I have read and understood [Policy Title] (version [X.X], effective [date]). I understand my responsibilities under this policy and will comply with its requirements in the course of my work.*
>
> *I understand that failure to comply with this policy may result in disciplinary action."*

---

## 6. Document Management Requirements

PIMS policy documents must be stored in a system that provides:

| Requirement | Minimum Standard |
|-------------|-----------------|
| Access control | Read access for all relevant personnel; edit access restricted to DPO and designated policy authors |
| Version control | Full version history retained; previous versions accessible but clearly marked superseded |
| Audit trail | Record of who approved each version and when |
| Backup | Included in organisational backup policy; recovery tested |
| Availability | Accessible to all relevant personnel during normal working hours; accessible to auditors on request |
| Retention | Retired policies retained for minimum 3 years after retirement date |

Suitable platforms: SharePoint, Confluence, Google Drive with appropriate access controls, dedicated GRC platform, or ISMS CORE API document repository (when PRIVACY module is operational).

---

<!-- QA_VERIFIED: [Date] -->
