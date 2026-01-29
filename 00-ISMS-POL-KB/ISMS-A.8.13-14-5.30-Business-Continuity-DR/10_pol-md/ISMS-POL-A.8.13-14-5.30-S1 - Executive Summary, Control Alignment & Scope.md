# ISMS-POL-A.8.13-14-5.30-S1: Executive Summary, Control Alignment & Scope

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial policy framework for unified BC/DR controls |

---

## Table of Contents

1. [ISO 27001:2022 Control Text](#1-iso-270012022-control-text)
2. [Executive Summary](#2-executive-summary)
3. [Scope and Applicability](#3-scope-and-applicability)
4. [Integration Architecture](#4-integration-architecture)
5. [Regulatory and Compliance Context](#5-regulatory-and-compliance-context)
6. [Roles and Responsibilities](#6-roles-and-responsibilities)
7. [Framework Overview](#7-framework-overview)
8. [Related Documents](#8-related-documents)

---

## 1. ISO 27001:2022 Control Text

This section provides the complete control text from ISO/IEC 27001:2022 for all three controls addressed by this unified Business Continuity and Disaster Recovery Framework.

### 1.1 Control A.8.13 - Information Backup

**Control Type:** Technical  
**Information Security Properties:** Availability  
**Cybersecurity Concepts:** Recover  
**Operational Capabilities:** Business Continuity  
**Security Domains:** Protection

**Control Text:**
> Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy.

**Purpose:**
To ensure that information, software and systems can be recovered in the event of loss, damage, corruption or unavailability.

**ISO 27002:2022 Guidance Summary:**
- Backup copies should be created according to a defined and documented backup policy
- Backups should include all essential information, software, system images and configurations
- Backups should be tested regularly to ensure they can be restored
- Backups should be protected to the same level as the original data
- Multiple generations of backups should be retained
- Backups should be stored in a secure, separate location

### 1.2 Control A.8.14 - Redundancy of Information Processing Facilities

**Control Type:** Technical  
**Information Security Properties:** Availability  
**Cybersecurity Concepts:** Recover  
**Operational Capabilities:** Business Continuity  
**Security Domains:** Protection

**Control Text:**
> Information processing facilities shall be implemented with sufficient redundancy to meet availability requirements.

**Purpose:**
To ensure the availability of information processing facilities in accordance with the organization's requirements.

**ISO 27002:2022 Guidance Summary:**
- Redundancy should be implemented for critical information processing facilities
- Level of redundancy should be determined by availability requirements
- Redundancy can include hardware, software, network, power, and cooling
- Geographic redundancy should be considered to protect against site-wide disasters
- Failover mechanisms should be implemented and tested
- Single Points of Failure (SPOF) should be identified and mitigated

### 1.3 Control A.5.30 - ICT Readiness for Business Continuity

**Control Type:** Organizational  
**Information Security Properties:** Availability  
**Cybersecurity Concepts:** Recover  
**Operational Capabilities:** Business Continuity  
**Security Domains:** Governance & Ecosystem

**Control Text:**
> ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.

**Purpose:**
To ensure that ICT systems are ready to support business continuity in the event of disruptions.

**ISO 27002:2022 Guidance Summary:**
- ICT continuity plans should be developed based on Business Impact Analysis (BIA)
- Plans should define Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO)
- ICT continuity requirements should be aligned with business continuity objectives
- Plans should be tested regularly through exercises and simulations
- Dependencies between ICT systems should be documented
- ICT continuity should be integrated with overall business continuity management
- Communication procedures should be established for crisis situations

---

## 2. Executive Summary

### 2.1 The Business Criticality of BC/DR

Business Continuity and Disaster Recovery (BC/DR) capabilities are not merely compliance requirements—they are fundamental to organizational survival. When critical systems fail or data is lost, the consequences can be catastrophic:

- **Revenue Loss**: Every minute of downtime for critical systems translates directly to lost revenue
- **Operational Impact**: Disrupted business processes affect productivity, customer service, and supply chain operations
- **Reputational Damage**: Inability to maintain services erodes customer trust and brand value
- **Regulatory Penalties**: Non-compliance with data protection and operational resilience regulations
- **Competitive Disadvantage**: Organizations that cannot recover quickly fall behind competitors

In today's digital economy, where business operations are completely dependent on information and communication technology (ICT), the ability to recover from disruptions is existential.

### 2.2 The Unified BC/DR Framework Approach

[Organization] has adopted a **unified framework** approach that integrates three related ISO 27001:2022 controls into a cohesive Business Continuity and Disaster Recovery program:

- **A.8.13 (Information Backup)** provides **data recovery capability** through systematic backup and restore processes
- **A.8.14 (Redundancy)** provides **system availability capability** through redundant infrastructure and failover mechanisms
- **A.5.30 (ICT BC Readiness)** provides **overall BC/DR preparedness** through business impact analysis, planning, testing, and governance

**Why Unified Implementation?**

Attempting to implement these three controls separately would result in:
- Disconnected backup and redundancy strategies that don't align
- BC/DR plans that don't reflect actual technical recovery capabilities
- Redundant assessment efforts and documentation
- Fragmented RPO/RTO requirements across controls
- Missed dependencies between backup, redundancy, and business continuity

By implementing them as a unified framework, [Organization] achieves:
- **Consistent RPO/RTO requirements** derived from Business Impact Analysis and applied across all controls
- **Integrated testing programs** that validate backup, failover, and BC/DR scenarios together
- **Unified evidence collection** that supports compliance across all three controls
- **Holistic recovery capability** where backup + redundancy + preparedness = actual business resilience
- **Efficient resource utilization** by avoiding duplicated efforts

### 2.3 The "Untested Recovery = No Recovery" Principle

This framework is founded on Richard Feynman's principle: **"The first principle is that you must not fool yourself—and you are the easiest person to fool."**

**Cargo Cult BC/DR** says:
- "We have backups running nightly. We're protected."
- "We have redundant systems. We're resilient."
- "We have a BC/DR plan documented. We're compliant."

**Evidence-Based BC/DR** says:
- "We tested recovery last month and restored the production database in 2.3 hours, meeting our 4-hour RTO."
- "We conducted a failover test last quarter and the secondary site took over automatically in 12 minutes, meeting our 15-minute RTO."
- "We ran a full DR simulation last quarter involving 47 systems and identified 8 gaps, all of which are now remediated."

**This framework mandates:**
- Regular restore testing (not just backup success)
- Regular failover testing (not just redundancy existence)
- Regular BC/DR scenario exercises (not just plan documentation)
- Evidence collection for all tests (documented results)
- Gap remediation tracking (identified issues must be fixed)

**Untested recovery capability = No recovery capability.** This is non-negotiable.

### 2.4 Systems Engineering Methodology

This framework applies Systems Engineering principles to BC/DR:

1. **Requirements Definition**: Business Impact Analysis determines RPO/RTO requirements
2. **System Design**: Backup and redundancy architectures designed to meet requirements
3. **Implementation**: Technical capabilities deployed and configured
4. **Verification**: Testing validates that capabilities meet requirements
5. **Continuous Improvement**: Test results drive architecture improvements

This is not a "set and forget" compliance exercise. It is a continuous engineering discipline focused on measurable outcomes.

---

## 3. Scope and Applicability

### 3.1 Framework Scope

This BC/DR Framework covers:

**Information Assets:**
- All business-critical data (customer data, financial records, intellectual property)
- All operational data required for business processes
- System configurations and infrastructure-as-code
- Application software and dependencies
- Security configurations and access controls

**Information Processing Facilities:**
- Physical servers (on-premises datacenters)
- Virtual machines and containers
- Cloud infrastructure (IaaS, PaaS, SaaS)
- Network infrastructure (routers, switches, firewalls)
- Storage systems (SAN, NAS, object storage)
- End-user computing (if business-critical)

**Business Processes:**
- All ICT-dependent business processes
- Critical business functions identified through BIA
- Supporting processes required for critical functions
- Third-party services and dependencies

### 3.2 Technology-Agnostic Approach

This framework is **completely technology-agnostic** and applies regardless of:
- Infrastructure deployment model (on-premises, cloud, hybrid, multi-cloud)
- Backup technology used (any vendor or solution)
- Redundancy architecture (any technology or approach)
- Platform or operating system (Windows, Linux, cloud-native, etc.)

The framework defines **capabilities required**, not specific technologies. [Organization] maintains flexibility to select the most appropriate technologies for its context while ensuring compliance with policy requirements.

### 3.3 Organizational Applicability

This framework applies to:
- All [Organization] business units and departments
- All [Organization] IT infrastructure and systems
- All third-party managed services and cloud providers supporting [Organization]
- All development, staging, and production environments (proportionate to criticality)

This framework scales to organizations of any size. Requirements are **risk-based and business-driven**:
- Critical systems: Highest requirements (shortest RPO/RTO, most redundancy, most frequent testing)
- Important systems: Moderate requirements
- Standard systems: Baseline requirements
- Non-critical systems: Minimal requirements or risk acceptance

### 3.4 Out of Scope

This framework does **not** cover:
- Physical security and building safety (addressed by other controls)
- Personnel safety during disasters (addressed by crisis management)
- Non-ICT business continuity (addressed by overall BCM)
- Financial continuity planning (addressed by finance/treasury)

However, this framework **integrates** with these areas through the overall Business Continuity Management System.

---

## 4. Integration Architecture

### 4.1 How the Three Controls Form a BC/DR Ecosystem

The three controls are not independent—they form an integrated ecosystem:

```
┌─────────────────────────────────────────────────────────────────┐
│                 A.5.30 - ICT BC READINESS                       │
│  (Business Impact Analysis, Strategy, Plans, Governance)        │
│                                                                 │
│  ┌──────────────────────┐    ┌──────────────────────────┐     │
│  │   A.8.13 - BACKUP    │    │  A.8.14 - REDUNDANCY     │     │
│  │  (Data Recovery)     │    │  (System Availability)    │     │
│  │                      │    │                          │     │
│  │  • Backup copies     │    │  • Redundant systems     │     │
│  │  • Restore process   │    │  • Failover capability   │     │
│  │  • RPO alignment     │    │  • RTO alignment         │     │
│  │  • Restore testing   │    │  • Failover testing      │     │
│  └──────────────────────┘    └──────────────────────────┘     │
│            │                             │                     │
│            └─────────────┬───────────────┘                     │
│                          │                                     │
│                 Integrated Testing                             │
│                Evidence Collection                             │
│                  Gap Management                                │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Recovery Capability = Backup + Redundancy + Preparedness

**True recovery capability** requires all three elements:

1. **Backup (A.8.13)**: "We can recover data from 4 hours ago" (RPO = 4 hours)
2. **Redundancy (A.8.14)**: "We can failover to secondary systems in 15 minutes" (RTO = 15 minutes)
3. **Preparedness (A.5.30)**: "We have tested this, documented procedures, trained staff, and integrated with incident management"

Missing any one element compromises recovery:
- Backup without redundancy = Long recovery times (restore from backup takes hours/days)
- Redundancy without backup = No protection against data corruption or logical errors
- Technical capabilities without preparedness = Failures during actual incidents (untested procedures, untrained staff)

### 4.3 RPO/RTO as Unifying Concepts

**Recovery Point Objective (RPO)** and **Recovery Time Objective (RTO)** provide the common language across all three controls:

- **RPO** defines acceptable data loss (measured in time: hours, minutes)
  - Drives A.8.13 backup frequency requirements
  - Influences A.8.14 data replication strategies
  - Determined by A.5.30 Business Impact Analysis

- **RTO** defines acceptable downtime (measured in time: hours, minutes)
  - Drives A.8.14 redundancy and failover requirements
  - Influences A.8.13 restore time capabilities
  - Determined by A.5.30 Business Impact Analysis

**Business Impact Analysis (BIA)** conducted under A.5.30 establishes the RPO/RTO requirements that drive technical implementation under A.8.13 and A.8.14.

### 4.4 Testing as Verification Mechanism

Testing provides evidence that capabilities meet requirements:

| Test Type | Primary Control | What It Verifies | Frequency |
|-----------|----------------|------------------|-----------|
| Backup Restore Test | A.8.13 | Can restore data within RPO/RTO | Monthly-Annual (by criticality) |
| Failover Test | A.8.14 | Can switch to redundant systems within RTO | Quarterly-Annual (by criticality) |
| Tabletop Exercise | A.5.30 | Team knows procedures, communication works | Quarterly |
| Full DR Simulation | A.5.30 + A.8.13 + A.8.14 | End-to-end recovery works as planned | Annual |

Test results feed back into continuous improvement:
- Failed tests → Gaps identified → Remediation → Retest
- Successful tests → Evidence collected → Audit readiness

---

## 5. Regulatory and Compliance Context

### 5.1 ISO 27001:2022 Compliance

This framework directly implements three ISO 27001:2022 Annex A controls. While implemented as a unified framework, each control is **distinctly addressed** to support Statement of Applicability (SoA) requirements:

**Statement of Applicability entries:**
- A.8.13 - Information Backup: **Applicable** - [Organization] requires systematic backup and restore capabilities for all business-critical systems as defined in this framework
- A.8.14 - Redundancy of Information Processing Facilities: **Applicable** - [Organization] requires redundancy for critical systems to meet availability requirements as defined in this framework
- A.5.30 - ICT Readiness for Business Continuity: **Applicable** - [Organization] requires ICT continuity planning, testing, and governance as defined in this framework

Each control has dedicated policy sections (S2, S3, S4) defining specific requirements, ensuring audit traceability.

### 5.2 DORA (Digital Operational Resilience Act)

**Applicability:** EU financial services entities  
**Effective Date:** January 17, 2025 (now in force)

For organizations subject to DORA, this framework supports compliance with **Article 12 - Backup policies and procedures, restoration and recovery procedures and methods**:

**DORA Article 12 Requirements:**
- Regular backups of critical systems and data
- Backup copies must be **restorable to different locations** (physically and logically separated from original)
- Backup data must be protected from **unauthorized access** and stored to prevent **changes or corruption** (immutability)
- Backups must be **tested regularly** to ensure restoration capability
- Backup systems must be **segregated** from production systems
- ICT risk management framework integration

**This Framework Addresses:**
- Section S2 (Backup Requirements) mandates immutable backup copies and offsite/offline storage
- Section S5 (Testing Framework) mandates regular restore testing including restoration to different locations
- Section S2 requires segregated backup infrastructure where feasible
- Assessment workbooks track DORA-specific compliance (immutability, offsite, testing)

Organizations subject to DORA should review Section S2 and ensure backup implementations specifically address Article 12 requirements.

### 5.3 NIS2 (Network and Information Security Directive 2)

**Applicability:** Essential and important entities across 18 EU sectors  
**Transposition Deadline:** October 17, 2024 (now effective)

For organizations subject to NIS2, this framework supports compliance with cybersecurity risk management requirements:

**NIS2 Backup Requirements:**
- Business continuity and disaster recovery plans mandatory
- **Data encryption** (at-rest and in-transit)
- **Backup management and restoration procedures**
- Regular testing of backup and recovery capabilities
- **Supply chain security** (vetting backup vendors)
- **24-hour incident reporting** (early warning)
- **72-hour detailed incident reporting**

**NIS2 Best Practice - 3-2-1 Backup Rule:**
- 3 copies of data (production + 2 backups)
- 2 different media types (disk, cloud, tape)
- 1 offsite copy (geographic separation)

**This Framework Addresses:**
- Section S2 references 3-2-1-1-0 rule (enhanced version of 3-2-1)
- Section S2 mandates encryption requirements
- Section S4 addresses supplier BC arrangements
- Section S4 addresses incident reporting integration (24h/72h timelines)
- Section S5 mandates regular testing of recovery capabilities

Organizations subject to NIS2 should review Sections S2 and S4 and ensure implementations meet directive requirements.

### 5.4 Industry Best Practices - Veeam 3-2-1-1-0 Rule

While not a regulatory requirement, this framework **references** the Veeam 3-2-1-1-0 rule as an industry best practice:

- **3**: Three copies of data (production + 2 backups)
- **2**: Two different media types (disk, cloud, tape)
- **1**: One copy offsite (geographic separation)
- **1**: One copy offline/air-gapped/immutable (ransomware protection)
- **0**: Zero recovery errors (verified recoverability through testing)

This enhanced rule addresses modern threats (ransomware) and emphasizes testing (zero errors).

**Framework Approach:**
- Section S2 explains 3-2-1-1-0 principles
- Organizations are encouraged but not required to adopt this specific rule
- Requirements are business-driven based on BIA, not rule-driven
- Assessment workbooks can track 3-2-1-1-0 compliance for organizations that choose this approach

### 5.5 Framework Flexibility

**Important Note:**
- This framework **supports** DORA, NIS2, and industry best practices
- This framework **does not mandate** compliance with these regulations/standards
- Organizations **not** subject to DORA or NIS2 can still use this framework
- Requirements are **business-driven** based on BIA, not regulation-driven
- Regulatory compliance is achieved through alignment, not prescription

Organizations should:
1. Determine which regulations apply to them
2. Use framework requirements as baseline
3. Enhance requirements where regulations demand more
4. Document regulatory mapping in evidence collection

---

## 6. Roles and Responsibilities

### 6.1 Business Owners

**Responsibilities:**
- Define business requirements for RPO/RTO through Business Impact Analysis participation
- Approve BC/DR strategy and investment decisions
- Participate in BC/DR testing and exercises
- Accept residual risks where capabilities don't meet requirements
- Provide input on business continuity priorities

**Key Deliverables:**
- BIA input (impact assessment, MTPD determination)
- RPO/RTO requirements approval
- Risk acceptance documentation (where applicable)

### 6.2 BC/DR Coordinator

**Responsibilities:**
- Overall BC/DR program management and governance
- Coordinate BIA process across business units
- Develop and maintain BC/DR strategy
- Schedule and facilitate BC/DR testing and exercises
- Track gaps and remediation efforts
- Report BC/DR readiness to management
- Coordinate with incident management during actual events

**Key Deliverables:**
- BC/DR strategy document
- BC/DR testing schedule and results
- Quarterly BC/DR status reports
- Gap remediation roadmap

### 6.3 Technical Teams (IT, DevOps, Infrastructure)

**Responsibilities:**
- Implement backup solutions and configurations (A.8.13)
- Implement redundancy architectures (A.8.14)
- Conduct backup restore testing
- Conduct failover testing
- Maintain recovery procedures documentation
- Monitor backup and redundancy status
- Respond to backup/redundancy failures
- Participate in DR simulations

**Key Deliverables:**
- Backup infrastructure and configurations
- Redundancy infrastructure and configurations
- Recovery procedures documentation
- Test results and evidence
- Monitoring dashboards

### 6.4 Security Operations

**Responsibilities:**
- Ensure backup encryption and security controls
- Monitor backup and recovery events (SIEM integration)
- Conduct security assessments of BC/DR capabilities
- Maintain BC/DR compliance evidence
- Coordinate audits related to BC/DR
- Ensure BC/DR integration with incident management

**Key Deliverables:**
- Security requirements for backups and redundancy
- Compliance assessment results
- Audit evidence packages
- Security monitoring integration

### 6.5 Internal Audit / Compliance

**Responsibilities:**
- Conduct periodic audits of BC/DR compliance
- Verify testing evidence and results
- Assess gap remediation effectiveness
- Report findings to management and audit committee
- Coordinate external audits (ISO 27001, regulatory)

**Key Deliverables:**
- BC/DR audit reports
- Compliance assessment results
- Recommendations for improvement

### 6.6 Executive Management / CISO

**Responsibilities:**
- Approve BC/DR strategy and investment
- Ensure adequate resources for BC/DR program
- Oversee BC/DR governance
- Accept strategic risks related to BC/DR
- Ensure BC/DR integration with overall business continuity
- Report BC/DR readiness to board/executive committee

**Key Deliverables:**
- BC/DR strategy approval
- Budget allocation approval
- Risk acceptance decisions
- Executive reporting

---

## 7. Framework Overview

### 7.1 Policy Sections (ISMS-POL-A.8.13-14-5.30)

This unified policy framework consists of five policy sections and one annex:

| Section | Title | Purpose |
|---------|-------|---------|
| **S1** | Executive Summary, Control Alignment & Scope | This document - overview and integration |
| **S2** | Backup Requirements (A.8.13) | Detailed requirements for information backup |
| **S3** | Redundancy Requirements (A.8.14) | Detailed requirements for system redundancy |
| **S4** | ICT BC Readiness Requirements (A.5.30) | Detailed requirements for BC/DR preparedness |
| **S5** | Testing Methodology & Evidence Framework | Testing approach and evidence collection |
| **Annex-C** | Integration Mapping | Integration with other ISMS controls |

Each section is standalone-readable while maintaining integration with the overall framework.

### 7.2 Implementation Guidance (ISMS-IMP-A.8.13-14-5.30)

Practical implementation guidance consists of five sections:

| Section | Title | Purpose |
|---------|-------|---------|
| **IMP-S1** | BIA and RPO/RTO Process | How to conduct BIA and determine requirements |
| **IMP-S2** | Backup Implementation | How to implement backup capabilities |
| **IMP-S3** | Redundancy Implementation | How to implement redundancy capabilities |
| **IMP-S4** | Recovery Testing Process | How to conduct testing and collect evidence |
| **IMP-S5** | BC/DR Assessment | How to assess compliance and identify gaps |

Implementation guidance provides step-by-step procedures, examples, and common pitfalls.

### 7.3 Assessment Workbooks

Five assessment workbooks support compliance evaluation:

| Workbook | Purpose | Key Features |
|----------|---------|--------------|
| **WB1** | Backup Inventory & Coverage | System inventory, backup status, RPO compliance, 3-2-1-1-0 tracking |
| **WB2** | Redundancy Analysis | Critical systems, SPOF analysis, RTO compliance, failover testing |
| **WB3** | RPO/RTO Compliance Matrix | Business requirements vs. technical capabilities, gap analysis |
| **WB4** | BC/DR Testing Results | Test inventory, test results, issues, lessons learned |
| **Dashboard** | BC/DR Readiness Overview | Consolidated metrics, overall maturity score, gap prioritization |

Assessment workbooks are generated by Python scripts and include:
- Pre-populated example data
- Data validation dropdowns
- Automated formulas (compliance calculations)
- Conditional formatting (red/yellow/green)
- 100-row evidence registers
- 3-level approval workflows

### 7.4 Framework Usage Model

**Quarterly Cycle:**

```
Q1: Conduct BIA → Define/update RPO/RTO requirements → Review technical capabilities
    ↓
Q2: Execute testing (restore tests, failover tests, tabletop exercises)
    ↓
Q3: Complete assessments (WB1-4) → Identify gaps → Prioritize remediation
    ↓
Q4: Remediate gaps → Prepare for annual full DR simulation
    ↓
Annual: Full DR simulation → Executive reporting → Strategy review
```

**Continuous Activities:**
- Backup monitoring (daily)
- Backup execution (per schedule)
- Redundancy monitoring (continuous)
- Incident response (as needed)
- Evidence collection (ongoing)

---

## 8. Related Documents

### 8.1 ISMS Policy Framework

- **ISMS-POL-00**: Regulatory Applicability Framework
- **ISMS-POL-A.8.13-14-5.30-S2**: Backup Requirements (A.8.13)
- **ISMS-POL-A.8.13-14-5.30-S3**: Redundancy Requirements (A.8.14)
- **ISMS-POL-A.8.13-14-5.30-S4**: ICT BC Readiness Requirements (A.5.30)
- **ISMS-POL-A.8.13-14-5.30-S5**: Testing Methodology & Evidence Framework
- **ISMS-POL-A.8.13-14-5.30-Annex-C**: Integration Mapping

### 8.2 Implementation Guidance

- **ISMS-IMP-A.8.13-14-5.30-S1**: BIA and RPO/RTO Process
- **ISMS-IMP-A.8.13-14-5.30-S2**: Backup Implementation
- **ISMS-IMP-A.8.13-14-5.30-S3**: Redundancy Implementation
- **ISMS-IMP-A.8.13-14-5.30-S4**: Recovery Testing Process
- **ISMS-IMP-A.8.13-14-5.30-S5**: BC/DR Assessment

### 8.3 Related ISMS Controls

- **A.5.9**: Asset Inventory (systems requiring backup/redundancy)
- **A.5.24-27**: Incident Management (BC/DR activation during incidents)
- **A.8.6**: Capacity Management (backup storage, redundant capacity)
- **A.8.9**: Configuration Management (backup/redundancy configurations)
- **A.8.15**: Logging (backup/failover events)
- **A.8.16**: Monitoring (backup/redundancy monitoring)
- **A.5.19-23**: Supplier/Cloud Management (cloud provider BC/DR)

### 8.4 External Standards and Regulations

- ISO/IEC 27001:2022 - Information Security Management Systems
- ISO/IEC 27002:2022 - Information Security Controls (Implementation Guidance)
- ISO 22301:2019 - Business Continuity Management Systems
- Regulation (EU) 2022/2554 - Digital Operational Resilience Act (DORA)
- Directive (EU) 2022/2555 - Network and Information Security Directive (NIS2)

---

## Conclusion

This unified BC/DR framework provides [Organization] with a comprehensive, evidence-based approach to ensuring business continuity and disaster recovery capabilities. By integrating A.8.13 (Backup), A.8.14 (Redundancy), and A.5.30 (ICT BC Readiness) into a cohesive framework, [Organization] achieves:

✅ **Business Alignment**: RPO/RTO requirements driven by Business Impact Analysis  
✅ **Technical Excellence**: Backup and redundancy capabilities meeting business requirements  
✅ **Verified Readiness**: Regular testing proving capabilities actually work  
✅ **Regulatory Compliance**: Support for DORA, NIS2, and ISO 27001:2022  
✅ **Continuous Improvement**: Evidence-based gap identification and remediation  
✅ **Audit Readiness**: Comprehensive evidence collection and documentation  

**Next Steps:**
1. Review and approve this executive policy framework
2. Review detailed requirements in Sections S2, S3, S4, S5
3. Conduct or update Business Impact Analysis (IMP-S1)
4. Assess current capabilities against requirements (IMP-S5)
5. Develop remediation roadmap for identified gaps
6. Implement regular testing cadence per Section S5

---

**Document End**

*"The first principle is that you must not fool yourself—and you are the easiest person to fool."* - Richard Feynman

*Untested recovery = No recovery. This framework demands evidence.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| Business Owner Representative | | | |
| IT Operations Manager | | | |
| Compliance Officer | | | |

**Next Review Date:** [One year from approval date]