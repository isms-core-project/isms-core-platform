<h1 align="center">🎋 ISMS CORE Controls Index</h1>

<p align="center">
  <strong>ISO 27001:2022 Annex A Implementation Framework</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Control_Groups-42-0066CC?style=flat-square" alt="42 Control Groups"/>
  <img src="https://img.shields.io/badge/Individual_Controls-93-32CD32?style=flat-square" alt="93 Controls"/>
  <img src="https://img.shields.io/badge/ISO_27001-2022-DC143C?style=flat-square" alt="ISO 27001:2022"/>
</p>

---

## Repository Structure

```
isms-core/
├── A.5-organizational-controls/     # 17 controls
├── A.6-people-controls/             # 3 controls
├── A.7-physical-controls/           # 1 control
└── A.8-technological-controls/      # 21 controls
```

Each control folder contains:

```
isms-a.X.X-control-name/
├── POL/10_pol-md/        ← Policy documents
├── IMP/30_imp-md/        ← Implementation guides
├── SCR/                  ← Scripts and workbooks
│   ├── 10_generator-master/
│   ├── 90_workbooks/
│   └── ...
├── REF/70_ref-md/        ← Reference materials (if applicable)
└── CTX/80_ctx-md/        ← Context documents (if applicable)
```

---

## A.5 Organizational Controls

<p>
<img src="https://img.shields.io/badge/A.5-Organizational-9400D3?style=flat-square" alt="Organizational"/>
<img src="https://img.shields.io/badge/17_groups-0066CC?style=flat-square" alt="17 groups"/>
</p>

📁 **[A.5-organizational-controls/](A.5-organizational-controls/)**

| Control | Name | Artifacts |
|---------|------|-----------|
| [A.5.1-2, 6.1-2](A.5-organizational-controls/isms-a.5.1-2-6.1-2-secure-employment-and-roles/) | Secure Employment and Roles | POL, IMP, SCR |
| [A.5.4](A.5-organizational-controls/isms-a.5.4-management-responsibilities/) | Management Responsibilities | POL, IMP, SCR |
| [A.5.5-6](A.5-organizational-controls/isms-a.5.5-6-external-communications/) | External Communications | IMP, SCR |
| [A.5.7](A.5-organizational-controls/isms-a.5.7-threat-intelligence/) | Threat Intelligence | POL, IMP, SCR |
| [A.5.8](A.5-organizational-controls/isms-a.5.8-information-security-in-project-management/) | Information Security in Project Management | POL, IMP, SCR |
| [A.5.9](A.5-organizational-controls/isms-a.5.9-inventory-of-information-and-assets/) | Inventory of Information and Assets | IMP, SCR |
| [A.5.10-11](A.5-organizational-controls/isms-a.5.10-11-asset-usage-lifecycle/) | Asset Usage Lifecycle | POL, IMP, SCR |
| [A.5.12-13](A.5-organizational-controls/isms-a.5.12-13-classification-and-labelling/) | Classification and Labelling | IMP, SCR |
| [A.5.14](A.5-organizational-controls/isms-a.5.14-information-transfer/) | Information Transfer | IMP, SCR |
| [A.5.15-16, 18](A.5-organizational-controls/isms-a.5.15-16-18-identity-access-management/) | Identity Access Management | IMP, SCR |
| [A.5.17](A.5-organizational-controls/isms-a.5.17-authentication-information/) | Authentication Information | IMP, SCR |
| [A.5.19-23](A.5-organizational-controls/isms-a.5.19-23-cloud-services/) | Cloud Services | POL, IMP, SCR, REF |
| [A.5.24-28](A.5-organizational-controls/isms-a.5.24-28-incident-management-lifecycle/) | Incident Management Lifecycle | IMP, SCR |
| [A.5.31](A.5-organizational-controls/isms-a.5.31-legal-statutory-regulatory-contractual-requirements/) | Legal, Statutory, Regulatory & Contractual | POL, IMP, SCR |
| [A.5.34](A.5-organizational-controls/isms-a.5.34-privacy-and-pii/) | Privacy and PII | POL, IMP, SCR, REF |
| [A.5.35-36](A.5-organizational-controls/isms-a.5.35-36-compliance-review/) | Compliance Review | POL, IMP, SCR |
| [A.5.37](A.5-organizational-controls/isms-a.5.37-documented-procedures/) | Documented Operating Procedures | POL, IMP, SCR |

---

## A.6 People Controls

<p>
<img src="https://img.shields.io/badge/A.6-People-FF6600?style=flat-square" alt="People"/>
<img src="https://img.shields.io/badge/3_groups-0066CC?style=flat-square" alt="3 groups"/>
</p>

📁 **[A.6-people-controls/](A.6-people-controls/)**

| Control | Name | Artifacts |
|---------|------|-----------|
| [A.6.3](A.6-people-controls/isms-a.6.3-awareness-and-training/) | Awareness and Training | POL, IMP, SCR, REF |
| [A.6.6](A.6-people-controls/isms-a.6.6-confidentiality-nda/) | Confidentiality / NDA | POL, IMP, SCR |
| [A.6.7-8](A.6-people-controls/isms-a.6.7-8-remote-working-and-reporting/) | Remote Working and Reporting | POL, IMP, SCR, REF |

---

## A.7 Physical Controls

<p>
<img src="https://img.shields.io/badge/A.7-Physical-32CD32?style=flat-square" alt="Physical"/>
<img src="https://img.shields.io/badge/1_group-0066CC?style=flat-square" alt="1 group"/>
</p>

📁 **[A.7-physical-controls/](A.7-physical-controls/)**

| Control | Name | Artifacts |
|---------|------|-----------|
| [A.7.4-5, 11](A.7-physical-controls/isms-a.7.4-5-11-physical-infrastructure/) | Physical Infrastructure | POL, IMP, SCR |

---

## A.8 Technological Controls

<p>
<img src="https://img.shields.io/badge/A.8-Technological-DC143C?style=flat-square" alt="Technological"/>
<img src="https://img.shields.io/badge/21_groups-0066CC?style=flat-square" alt="21 groups"/>
<img src="https://img.shields.io/badge/100%25_Complete-00AA00?style=flat-square" alt="100% Complete"/>
</p>

📁 **[A.8-technological-controls/](A.8-technological-controls/)**

| Control | Name | Artifacts |
|---------|------|-----------|
| [A.8.1, 7, 18-19](A.8-technological-controls/isms-a.8.1-7-18-19-endpoint-security/) | Endpoint Security | POL, IMP, SCR, REF |
| [A.8.2-3, 5](A.8-technological-controls/isms-a.8.2-3-5-authentication-privileged-access/) | Authentication & Privileged Access | POL, IMP, SCR, REF |
| [A.8.6](A.8-technological-controls/isms-a.8.6-capacity-management/) | Capacity Management | POL, IMP, SCR |
| [A.8.8](A.8-technological-controls/isms-a.8.8-vulnerability-management/) | Vulnerability Management | POL, IMP, SCR |
| [A.8.9](A.8-technological-controls/isms-a.8.9-configuration-management/) | Configuration Management | POL, IMP, SCR, REF |
| [A.8.10](A.8-technological-controls/isms-a.8.10-data-deletion/) | Data Deletion | POL, IMP, SCR |
| [A.8.11](A.8-technological-controls/isms-a.8.11-data-masking/) | Data Masking | POL, IMP, SCR |
| [A.8.12](A.8-technological-controls/isms-a.8.12-data-leakage-prevention/) | Data Leakage Prevention | POL, IMP, SCR |
| [A.8.13-14, 5.30](A.8-technological-controls/isms-a.8.13-14-5.30-business-continuity-dr/) | Business Continuity & DR | POL, IMP, SCR |
| [A.8.15](A.8-technological-controls/isms-a.8.15-logging/) | Logging | POL, IMP, SCR, REF |
| [A.8.16](A.8-technological-controls/isms-a.8.16-monitoring/) | Monitoring | POL, IMP, SCR |
| [A.8.17](A.8-technological-controls/isms-a.8.17-clock-synchronization/) | Clock Synchronization | POL, IMP, SCR |
| [A.8.20-22](A.8-technological-controls/isms-a.8.20-22-network-security/) | Network Security | POL, IMP, SCR |
| [A.8.23](A.8-technological-controls/isms-a.8.23-web-filtering/) | Web Filtering | POL, IMP, SCR, REF |
| [A.8.24](A.8-technological-controls/isms-a.8.24-use-of-cryptography/) | Use of Cryptography | POL, IMP, SCR, CTX |
| [A.8.25-26, 29](A.8-technological-controls/isms-a.8.25-26-29-secure-development/) | Secure Development | POL, IMP, SCR |
| [A.8.28](A.8-technological-controls/isms-a.8.28-secure-coding/) | Secure Coding | POL, IMP, SCR, REF, CTX |
| [A.8.30](A.8-technological-controls/isms-a.8.30-outsourced-development/) | Outsourced Development | POL, IMP, SCR |
| [A.8.31](A.8-technological-controls/isms-a.8.31-environment-separation/) | Environment Separation | POL, IMP, SCR, REF |
| [A.8.32](A.8-technological-controls/isms-a.8.32-change-management/) | Change Management | POL, IMP, SCR, REF |
| [A.8.33-34](A.8-technological-controls/isms-a.8.33-34-testing-and-audit-protection/) | Testing and Audit Protection | POL, IMP, SCR |

---

## Artifact Legend

| Code | Type | Description | Badge |
|------|------|-------------|-------|
| **POL** | Policy | Defines WHAT is required and WHO is accountable | <img src="https://img.shields.io/badge/POL-9400D3?style=flat-square" alt="POL"/> |
| **IMP** | Implementation | Defines HOW to implement with assessment workbooks | <img src="https://img.shields.io/badge/IMP-0066CC?style=flat-square" alt="IMP"/> |
| **SCR** | Scripts | Python generators, validators, and Excel workbooks | <img src="https://img.shields.io/badge/SCR-3776AB?style=flat-square" alt="SCR"/> |
| **REF** | Reference | Regulatory and framework reference materials | <img src="https://img.shields.io/badge/REF-FF6600?style=flat-square" alt="REF"/> |
| **CTX** | Context | Organizational context documents | <img src="https://img.shields.io/badge/CTX-32CD32?style=flat-square" alt="CTX"/> |

---

## Getting Started

1. **Choose a section** - Browse by control category above
2. **Read the policy** - Start with `POL/10_pol-md/` for requirements
3. **Follow implementation** - Use `IMP/30_imp-md/` for step-by-step guidance
4. **Use the workbooks** - Run scripts in `SCR/` or use Excel files in `90_workbooks/`

---

<p align="center">
  <strong>ISMS CORE Framework v1.0</strong> | ISO 27001:2022 Annex A
</p>

<p align="center">
  <em>Where bamboo antennas actually work.</em> 🎋
</p>
