<!-- ISMS-CORE:REF:CLD-SEC-REF-A.5-A.8:sec:REF:sec-00 -->
**CLD-SEC-REF-A.5-A.8 — Cloud Security Guidance Addendum**
**ISO/IEC 27017:2026 CSC/CSP Guidance for Existing ISO/IEC 27001:2022 Annex A Controls**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Cloud Security Guidance Addendum |
| **Document Type** | Reference |
| **Document ID** | CLD-SEC-REF-A.5-A.8 |
| **Document Creator** | CISO / Cloud Security Manager |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | CISO (Reference document — informs implementation, does not itself impose new obligations) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Cloud Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial addendum for ISO/IEC 27017:2026 Ed. 2 implementation |

**Review Cycle**: Annual (or upon revision of ISO/IEC 27017 or ISO/IEC 27002)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- CLD-SEC-POL-A.5.38, CLD-SEC-POL-A.5.39, CLD-SEC-POL-A.8.35, CLD-SEC-POL-A.8.36 (the 4 standalone Cloud Sec controls)
- `50-isms-core-framework/` — the ISO/IEC 27001:2022 Annex A control packs this addendum layers onto
- ISO/IEC 27017:2026 (full standard)
- ISO/IEC 27002:2022 (Information security controls)

---

## What This Document Is

ISO/IEC 27017:2026 restructures cloud security guidance around the same 93-control clause structure as ISO/IEC 27002:2022 (Organisational 5.1–5.39, People 6.1–6.8, Physical 7.1–7.14, Technological 8.1–8.36). For most of those 93 controls, ISO/IEC 27017:2026 simply states "the guidance in ISO/IEC 27002:2022 applies" with nothing cloud-specific to add. For **38 controls**, however, it adds a genuine cloud-specific layer — a split table of additional guidance for the organisation acting as a **cloud service customer (CSC)** and/or a **cloud service provider (CSP)**.

Those 38 controls are not new controls. Each one is already fully implemented, with its own binding policy and implementation guides, in `50-isms-core-framework/`. This document exists so that the cloud-specific guidance is not lost — but it is captured **once, here**, rather than duplicated into 38 near-identical parallel POL/IMP document sets, which would mostly restate Framework boilerplate that already exists. (The 4 controls that *are* genuinely new — 5.38, 5.39, 8.35, 8.36 — received full standalone POL/IMP/SCR/WKBK treatment; see the Related Documents above.)

**How to use this document**: When implementing or auditing a Framework A.x.xx control for a service that involves cloud computing (as CSC or CSP), consult this addendum for the additional cloud-specific expectations, in addition to — not instead of — the binding Framework POL/IMP for that control. In practice, this happens at four points: during cloud service selection and risk assessment, during supplier due diligence and contracting, during internal audit of a cloud-involved control, and during the Cloud Security Manager's periodic review of Shared Responsibility Matrices under CLD-SEC-POL-A.5.38 — where a row in this addendum is relevant to a specific cloud service relationship, its CSC or CSP guidance is reflected in that service's matrix entry, not tracked as a separate open item. Compliance with the considerations in this addendum is therefore evidenced through the existing Framework, risk assessment, and Shared Responsibility Matrix records, not through separate artefacts unique to this document.

**Source**: ISO/IEC 27017:2026, Clauses 5–8. All guidance below is condensed directly from the standard's own CSC/CSP tables; entries marked "(CSC and CSP)" reflect a single combined guidance cell (ISO/IEC 27017:2026 "Type 2" tables) rather than a CSC/CSP split.

---

# Section 5 — Organisational Controls

| Control | Name | Framework Reference | CSC Guidance | CSP Guidance |
|---------|------|----------------------|---------------|----------------|
| 5.1 | Policies for information security | Framework A.5.1 | Define an information security policy on the use of cloud services as a topic-specific policy, addressing: data subject to CSP access/management, assets maintained in the cloud environment, multi-tenant/virtualized processes, CSU access levels, administrators with privileged access, CSP's geographic locations, and possibility of unauthorised cloud use. | Define rules for cloud service provision addressing: baseline security requirements, multi-tenancy/CSC isolation, virtualisation of resources, CSP personnel access to CSC data, strong authentication for administrative access, CSC account lifecycle management, change communications, and breach/forensics information sharing. |
| 5.2 | Information security roles and responsibilities | Framework A.5.1-2-6.1-2 | Define and document roles/responsibilities for the use of cloud services in topic-specific policies; allocate and communicate to relevant CSUs. | Define and allocate information security roles and responsibilities relating to cloud service provision. See also ISO/IEC 22123-3 for CSC/CSP role and sub-role definitions. |
| 5.7 | Threat intelligence | Framework A.5.7 | Identify information related to security threats on cloud computing environments and use it in threat intelligence activities; the information or its sources can be provided by the CSP. | Make information related to security threats on cloud computing environments available to CSCs to improve their overall threat intelligence. |
| 5.8 | Information security in project management | Framework A.5.8 | Identify its own information security requirements and determine whether the CSP's services address them; periodically evaluate the CSP's relevant capabilities. | Provide the CSC with information about the security capabilities used, informative without disclosing information useful to a malicious actor. |
| 5.9 | Inventory of information and other associated assets | Framework A.5.9 | Ensure the inventory accounts for information/assets stored in the cloud computing environment, indicating where records are maintained (e.g. the cloud service, geographical location). | Explicitly identify CSC data and cloud service derived data in its own asset inventory. |
| 5.11 | Return of assets | Framework A.5.10-11 | Before starting to use a cloud service, confirm whether its own assets (including cloud service derived data) will be returned upon termination. | State clearly to the CSC whether the CSC's assets, including cloud service derived data, will be returned upon termination; return assets when requested per the agreement. See also 8.10 where information deletion (not return) is required. |
| 5.13 | Labelling of information | Framework A.5.12-13 | Label information and other associated assets per its own labelling procedures; adopt CSP-provided labelling functionality where applicable. | Document and disclose any service functionality allowing CSCs to label their information and associated assets. |
| 5.16 | Identity management | Framework A.5.15-16-18 | Verify that CSP-provided user identity management functions and specifications meet its requirements for managing CSU access. | Provide user identity management functions, and specifications for their use, to manage CSU access to the cloud services. Third-party identity/access management technologies (e.g. SSO) can ease integration. |
| 5.17 | Authentication information | Framework A.5.17 | Verify that the CSP's procedure for managing authentication information (passwords, PINs, tokens, OTPs, biometrics) meets its requirements. | Provide information on procedures for managing authentication information, including allocation procedures. |
| 5.18 | Access rights | Framework A.5.15-16-18 | Verify that the CSP's functions and specifications for managing CSU access rights meet its requirements. | Provide functions for managing CSU access rights, and specifications for their use. |
| 5.20 | Addressing information security within supplier agreements | Framework A.5.19-23 | **See Extended Guidance, Section 5.20 below** — materially larger guidance than other rows in this table. | **See Extended Guidance, Section 5.20 below.** |
| 5.21 | Managing information security in the ICT supply chain | Framework A.5.19-23 | (No additional guidance.) | If the CSP itself uses secondary CSPs, ensure information security levels are maintained or exceeded; where cloud services are based on a supply chain, provide security objectives to suppliers and require risk management activities to achieve them. |
| 5.24 | Information security incident management planning and preparation | Framework A.5.24-28 | Request information on the allocation of incident management responsibilities/procedures; verify the scope of incidents reported by the CSP, notification timing, notification procedure, contact information, and available remedies. | Define the allocation of incident management responsibilities/procedures between CSC and CSP as part of service specifications; provide documentation covering scope, disclosure level, notification timing/procedure, contact information, and available remedies. |
| 5.28 | Collection of evidence | Framework A.5.24-28 | (CSC and CSP) Agree upon the procedures to respond to requests for potential digital evidence or other information related to the cloud computing environment. | *(same — combined guidance)* |
| 5.30 | ICT readiness for business continuity | Framework A.5.30-8.13-14 | Ensure the service level for interruption/disruption defined in the cloud SLA meets the RTO determined by its business continuity strategy, and that the cloud service's backup functionality can support the required RPO; consider redundancy across other cloud services or ICT environments. | Provide the CSC with cloud SLA and other agreements, plus information and constraints related to ICT readiness for business continuity. See also the ISO/IEC 19086 series on cloud SLAs. |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Framework A.5.31 | **See Extended Guidance, Section 5.31 below** — materially larger guidance than other rows in this table. | **See Extended Guidance, Section 5.31 below.** |
| 5.32 | Intellectual property rights | Framework A.5.32-33 | Identify cloud-specific licensing requirements before installing licensed software in a cloud service, particularly where the service is elastic/scalable and software can run on more systems or processor cores than the licence permits. | Establish a process for responding to intellectual property rights complaints. |
| 5.33 | Protection of records | Framework A.5.32-33 | Request information from the CSP about the protection of records gathered, stored, and archived in connection with the CSC's use of cloud services. | Provide information to the CSC about the protection of records gathered, stored, and archived in connection with the CSC's use of cloud services. |
| 5.35 | Independent review of information security | Framework A.5.35-36 | Request documented evidence that implementation of controls and guidelines for the cloud service is in line with any claims made by the CSP. | Provide documented evidence substantiating claims of implemented controls. Where individual CSC audits are impractical or increase risk, provide independent evidence (a relevant independent audit is acceptable, or a self-assessment with disclosed process/results if independent audit is impractical). |
| 5.37 | Documented operating procedures | Framework A.5.37 | Document procedures for critical operations where failure can cause unrecoverable damage to assets in the cloud environment (e.g. virtualized resource installation/change/deletion, cryptographic key/certificate management, service termination, backup/restoration); specify what critical operations are monitored. | Provide documentation about critical operating procedures to CSCs who require it (same critical-operation categories as CSC column). |

*(5.3, 5.4, 5.5, 5.6, 5.10, 5.12, 5.14, 5.15, 5.19, 5.22, 5.23, 5.25, 5.26, 5.27, 5.29, 5.34, 5.36 — ISO/IEC 27002:2022 guidance applies as-is with no cloud-specific addition, except 5.34 which points to ISO/IEC 27018 for PII-in-cloud guidance, already addressed by the Cloud PII product pack.)*

---

# Section 6 — People Controls

| Control | Name | Framework Reference | CSC Guidance | CSP Guidance |
|---------|------|----------------------|---------------|----------------|
| 6.3 | Information security awareness, education and training | Framework A.6.3 | Provide awareness/education/training on cloud services to stakeholders (management, supervising managers, business units, cloud service administrators, integrators, CSUs), covering: standards and topic-specific policies for cloud use, information security risks of cloud use and how they are managed, system/network environment risks of cloud use, and applicable legal/regulatory requirements. | Provide awareness/education/training for personnel, and require relevant interested parties to do the same, concerning appropriate handling of CSC data and cloud service derived data (which can be confidential or subject to regulatory access/use restrictions). |
| 6.8 | Information security event reporting | Framework A.6.7-8 | Request information from the CSP about the mechanisms for reporting events to the CSP and tracking reported event status. | Provide mechanisms for the CSC to report an event to the CSP, for the CSP to report an event to the CSC, and for the CSC to track reported event status. |

*(6.1, 6.2, 6.4, 6.5, 6.6, 6.7 — ISO/IEC 27002:2022 guidance applies as-is with no cloud-specific addition.)*

---

# Section 7 — Physical Controls

| Control | Name | Framework Reference | CSC Guidance | CSP Guidance |
|---------|------|----------------------|---------------|----------------|
| 7.14 | Secure disposal or re-use of equipment | Framework A.7.6-7-14 | Request information about the process and methods for secure disposal or reuse of resources (equipment, data storage, files, memory). | Provide the CSC with information about the process and methods for secure disposal or re-use of resources. See also ISO/IEC 27040 for additional secure-disposal guidance. |

*(7.1–7.13 — ISO/IEC 27002:2022 guidance applies as-is with no cloud-specific addition.)*

---

# Section 8 — Technological Controls

| Control | Name | Framework Reference | CSC Guidance | CSP Guidance |
|---------|------|----------------------|---------------|----------------|
| 8.2 | Privileged access rights | Framework A.8.2-3-5 | Use appropriate authentication techniques for elevated privileges (e.g. MFA) when authenticating its cloud service administrators. | Provide sufficient authentication techniques for elevated privileges when authenticating CSC administrators to a cloud service's administrative capabilities, according to identified risk (e.g. CSP-provided MFA or support for third-party MFA mechanisms). |
| 8.3 | Information access restriction | Framework A.8.2-3-5 | Ensure access to information in the cloud service can be restricted per its topic-specific access control policy, covering: the cloud services, the cloud service functions, and CSC data maintained in the service. | Provide the capabilities and information regarding access controls that allow the CSC to restrict access to the cloud services, cloud service functions, and CSC data. Zero-trust architecture principles (see ISO/IEC 27002:2022, 8.27) can apply to distributed multi-cloud resources. |
| 8.6 | Capacity management | Framework A.8.6 | Ensure the capacity provided by the CSP meets its requirements; monitor resource usage and forecast capacity needs; have access to data on resource usage over time periods and maximum usage levels; notify the CSP of additional capacity requirements where a request process exists. | Provide the CSC with data for monitoring resource usage (tools/APIs) and a process for responding to additional capacity requirements. |
| 8.8 | Management of technical vulnerabilities | Framework A.8.8 | Request information from the CSP about management of technical vulnerabilities that can affect the cloud services; define its own process for managing those vulnerabilities and determine which are expected to be addressed. | Make available to the CSC information about the management of technical vulnerabilities that can affect the cloud services provided. |
| 8.9 | Configuration management | Framework A.8.9 | Define responsibilities for configuration management of the cloud service; define/implement configuration management processes and tools considering documented secure-configuration information availability, availability of CSP-provided configuration management capabilities, ability to continuously monitor conformance to its own topic-specific policy, and ability to customise CSP standard templates. | Provide information about secure configuration, functions/tools supporting CSC configuration management, and standard templates for the cloud service. See also Annex B (monitoring of cloud services). |
| 8.10 | Information deletion | Framework A.8.10 | Document the process for termination of the service agreement, covering removal of the CSC's assets followed by deletion of all copies from the CSP's systems, listing all assets (including CSC data and cloud service derived data), and the scheduled termination timeline. | Provide information about the arrangements for removal of the CSC's assets upon termination, documented in the agreement and performed in a timely manner, specifying assets to be removed or kept and the scheduled termination date. See also 5.11 for return-of-assets. |
| 8.11 | Data masking | Framework A.8.11 | Confirm whether required data masking can be performed using the cloud service in compliance with its topic-specific data masking policy; implement its own masking where the CSP's function does not meet the policy. | Where data masking capability is delivered as part of the service, provide information about that capability. |
| 8.13 | Information backup | Framework A.5.30-8.13-14 | Where the CSP provides backup capability, verify it meets the CSC's requirements; implement its own backup capability where the CSP's does not meet requirements (responsibility for backups is often unclear, particularly in IaaS/PaaS). | Provide the specifications of its backup capabilities: scope/schedule, methods/formats (incl. encryption), retention periods, integrity-verification procedures, restoration procedures/timescales, testing procedures, and storage location. |
| 8.15 | Logging | Framework A.8.15 | Define its logging requirements and verify the cloud service meets them, or implement additional logging capability; where a privileged operation is delegated to the CSC, ensure it is logged (by CSP or CSC capability). | Provide capabilities and information regarding logging to the CSC (responsibilities vary by service model — e.g. for IaaS, CSP logging can be limited to infrastructure components while the CSC logs its own VMs/applications). |
| 8.16 | Monitoring activities | Framework A.8.16 | Request information from the CSP on available service monitoring capabilities; can use CSP or third-party monitoring tools. | Provide capabilities and description enabling the CSC to monitor security aspects of the service's operation, including detecting use of the service to attack others or abnormal traffic behaviour, with access controls limiting visibility to the CSC's own instances. See also Annex B. |
| 8.17 | Clock synchronisation | Framework A.8.17 | Request information about the CSP's system clock synchronisation. | Provide information regarding its own clock synchronisation and how the CSC can synchronise local clocks with the cloud service clock. |
| 8.18 | Use of privileged utility programs | Framework A.8.1-7-18-19 | Identify the utility programs it expects to use and ensure they do not interfere with the cloud service's controls. | Identify requirements for any utility programs the CSC is authorized to operate; ensure any utility program provided as part of the service is adequately secure. |
| 8.20 | Network security | Framework A.8.20-22 | (No additional guidance.) | Define and document a topic-specific policy on virtual network configuration consistent with the physical network policy; ensure the virtual network configuration matches that policy regardless of the means used to create it. |
| 8.24 | Use of cryptography | Framework A.8.24 | **See Extended Guidance, Section 8.24 below** — materially larger guidance than other rows in this table. | **See Extended Guidance, Section 8.24 below.** |
| 8.25 | Secure development life cycle | Framework A.8.25-26-29 | Request information from the CSP about its use of secure development procedures and practices. | Provide information about its use of secure development procedures/practices, to the extent compatible with its disclosure policy — can be critical for SaaS. |
| 8.32 | Change management | Framework A.8.32 | Its change management process should account for the impact of CSP-made changes in correlation with CSC-made changes. | Provide the CSC with information on changes that can adversely affect the service (categories of change, planned timing, technical description, notification of start/completion); where a secondary CSP is involved, inform the CSC of changes caused by that secondary CSP. |

*(8.1, 8.4, 8.5, 8.7, 8.12, 8.14, 8.19, 8.21, 8.22, 8.23, 8.26, 8.27, 8.28, 8.29, 8.30, 8.31, 8.33, 8.34 — ISO/IEC 27002:2022 guidance applies as-is with no cloud-specific addition, except 8.29 which notes system acceptance testing guidance applies to the CSC's use of a cloud service.)*

---

# Extended Guidance — Materially Larger Cloud-Specific Content

## 5.20 — Addressing Information Security within Supplier Agreements

**Framework Reference**: `ISMS-POL-A.5.19-23-S2 - Supplier Agreement Requirements.md`

**CSC Guidance**: The service agreement should include the information security roles and responsibilities relating to the cloud service, covering at minimum: authentication and access control; identity and access management; protection against malware; vulnerability management; backup; collection, maintenance, and protection of evidence (including logs and audit trails); continuous monitoring; cryptographic control; security testing; incident management; technical compliance review; auditing; and protection of information upon termination of the service agreement.

**CSP Guidance**: Specify as part of the agreement the relevant information security measures implemented, which can vary by cloud service type. The CSP should describe the information security roles and responsibilities related to the service in the agreement, covering the same list as the CSC column above.

## 5.31 — Legal, Statutory, Regulatory and Contractual Requirements

**Framework Reference**: `ISMS-POL-A.5.31.2 - Legal, Statutory, Regulatory and Contractual Requirements.md` (part of the 4-document ISMS-POL-A.5.31.1–4 group: Executive Control Alignment, Legal/Statutory/Regulatory/Contractual Requirements, Requirements Extraction & Control Mapping Framework, Change Management & Evidence Framework)

**CSC Guidance**: Identify laws and regulations governing the cloud service and evaluate consistency with its own obligations. Request evidence of the CSP's compliance with relevant laws, regulations, and standards — assessment reports or third-party conformity certifications are acceptable evidence. Verify that the CSP's cryptographic controls comply with applicable agreements, legislation, and regulations.

**CSP Guidance**: Provide the CSC with: legal requirement information where appropriate; evidence of current compliance with applicable legislation and contractual requirements; descriptions of implemented cryptographic controls; information on legal jurisdictions governing the service; and geographical locations of the CSP's organisation and the countries where CSC data and cloud service derived data can be stored/processed. Conduct a legal assessment of any authority investigation request to determine whether an applicable and legally valid basis exists, and what additional steps are required. Inform affected CSCs about investigation requests unless legally prohibited or where clear indications of illegal activity exist. Grant access to or disclose CSC data to authorities only after the legal assessment confirms a valid basis, limiting access strictly to the scope of the investigation request — not by default to all CSCs' data.

## 8.24 — Use of Cryptography

**Framework Reference**: `ISMS-POL-A.8.24 - Use of Cryptography.md`

**CSC Guidance**: Where the CSP offers cryptography, review CSP-supplied information to confirm the cryptographic capabilities: meet the CSC's information security requirements; are compatible with any other cryptographic protection the CSC uses; and apply to data at rest and in transit, to/from/within the cloud service. Where the CSP provides key management functionality for CSC use, request information on: the type of keys; specifications of the key management system, including procedures for each key lifecycle stage (generating, changing/updating, storing, retiring, retrieving, retaining, destroying); and recommended key management procedures for CSC use. In certain cases, the CSC may need to operate its own key management for part of its assets — in which case it should review CSP-provided constraints/tooling and employ or build appropriate cryptographic tooling.

**CSP Guidance**: Provide information regarding the circumstances in which cryptography is used to protect processed information, the procedures used to manage keys related to the cloud service, and any capabilities that can assist the CSC in applying its own cryptographic protection.

---

# Usage and Maintenance

This addendum is a living reference, not a one-time deliverable. The Cloud Security Manager SHALL:

- Consult it during cloud service intake and risk assessment, supplier due diligence and contracting, internal audit of any cloud-involved control, and the periodic Shared Responsibility Matrix review under CLD-SEC-POL-A.5.38
- Reflect any row relevant to a specific cloud service relationship in that service's Shared Responsibility Matrix entry, so the guidance is tracked as part of existing ISMS records rather than a parallel tracking system
- Review this addendum annually, or sooner if ISO/IEC 27017 or ISO/IEC 27002 is revised, or if a Framework A.x.xx control referenced here is materially changed

---

<!-- QA_VERIFIED: 2026-08-01 -->
