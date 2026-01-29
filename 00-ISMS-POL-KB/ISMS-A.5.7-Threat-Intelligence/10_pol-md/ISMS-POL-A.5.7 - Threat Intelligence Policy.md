# ISMS-POL-A.5.7
## Comprehensive Policy & Implementation Framework

**Document ID**: ISMS-POL-A.5.7  
**Title**: Threat Intelligence Policy
**Version**: 1.0
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial draft - Complete policy framework established |

**Review Cycle**: Annual (mandatory in Q4), quarterly light review (metrics only), or upon significant changes  
**Review Month**: Q4 (October-November) to align with budget planning and annual ISMS reviews  
**Next Review Date**: [Date + 1 year]   
**Approvers**: 
- Chief Information Security Officer (CISO)
- Chief Executive Officer (CEO)
- Chief Information Officer (CIO)
- Chief Risk Officer (CRO)
- Legal/Compliance Officer   

**Distribution**: All employees, contractors with access to threat intelligence or security operations  
**Related Standards**: ISO/IEC 27001:2022 Control A.5.7, ISO/IEC 27002:2022 Control 5.7, MITRE ATT&CK, STIX/TAXII, NIST CSF, CVSS 4.0

---

## Executive Summary

This document serves as the **master index** for the organization's threat intelligence control framework, implementing ISO/IEC 27001:2022 Control A.5.7 (Threat Intelligence).

**Purpose**: Establish a comprehensive framework for collecting, analyzing, and disseminating threat intelligence to enable proactive defense, inform risk management, and enhance security operations.

**Scope**: All threat intelligence activities across the organization, including strategic, tactical, and operational intelligence supporting security decision-making at all levels.

**Framework Components**:
- **Policy Layer:** Governance documents defining requirements (~5 documents)
- **Assessment Layer:** Technical evaluation specifications (4 markdown specs)
- **Implementation Layer:** Automated Excel workbook generators (4 Python scripts)
- **Validation Layer:** Quality assurance and checking tools (reused from A.8.24)
- **Integration Layer:** Executive dashboard with consolidated oversight

**Approach:** This framework uses a **system engineering methodology** rather than traditional paperwork-based compliance. All assessments are generated via Python scripts to ensure consistency, repeatability, and maintainability.

**Regulatory Alignment**: This framework complies with ISO/IEC 27001:2022 requirements and aligns with Swiss Federal Data Protection Act (FADP), EU GDPR, and where applicable, NIS2/DORA requirements.

**Expected Outcomes**:
- Risk assessment (Clause 6.1) informed by current threat intelligence (≥3 updates per quarter)
- Vulnerability remediation prioritized based on active exploitation and CVSS severity (when Control A.8.8 implemented)
- Incident response enhanced with threat context and IOCs (≥70% of P1/P2 incidents)
- Security investments justified by threat landscape analysis with quantitative risk scoring
- Compliance with ISO/IEC 27001:2022 Control A.5.7 demonstrated through objective evidence

**Success Metrics**:
- Threat intelligence influences ≥3 risk assessment updates per quarter (Clause 6.1)
- ≥3 documented prevented incidents per quarter with validation evidence
- ≥85% source accuracy rate (validated quarterly)
- ≥70% of P1/P2 incidents enriched with threat intelligence context
- ≥5 security decisions per quarter driven by threat intelligence
- ≥4.0/5.0 stakeholder satisfaction score

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.5.7 - Threat Intelligence**

> *Information relating to information security threats should be collected and analysed to produce threat intelligence.*

This policy framework provides the organizational governance, requirements, roles, and procedures necessary to fulfill Control 5.7 objectives and integrate threat intelligence across the Information Security Management System (ISMS).

---

## 1. Framework Structure

### 1.1 Purpose

Define mandatory requirements for threat intelligence capabilities to enable proactive threat detection, inform risk management decisions, prioritize security investments, and enhance incident response effectiveness.

### 1.2 Scope

This framework applies to:

- All threat intelligence activities (collection, analysis, production, dissemination)
- All intelligence types (strategic, tactical, operational)
- All intelligence sources (commercial platforms, OSINT, government feeds, internal telemetry)
- All stakeholders consuming threat intelligence (executives, SOC, incident response, risk management)
- Optional: Vulnerability management teams (when Control A.8.8 implemented)
- All security tools integrating threat intelligence (SIEM, EDR, firewalls, monitoring systems)

### 1.3 Users

This framework is binding for:

- **Employees** — Must leverage threat intelligence for security decision-making
- **Threat Intelligence Team** — Responsible for collection, analysis, and dissemination
- **Security Operations** — Must integrate intelligence into monitoring and response
- **Management** — Accountable for threat intelligence program effectiveness
- **External parties** — MSSPs, threat intelligence vendors, ISACs/ISAOs must meet contractual obligations
- **Auditors and regulators** — May review for compliance verification

### 1.4 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this threat intelligence framework are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Mandatory Compliance:**
- Swiss Federal Data Protection Act (FADP)
- EU GDPR (where processing EU personal data, including threat intelligence sources)
- ISO/IEC 27001:2022 (Control A.5.7)
- [Additional mandatory regulations per ISMS-POL-00]

**Informational Reference / Best Practice Alignment:**
- NIST Special Publications (SP 800-series)
- MITRE ATT&CK Framework (threat modeling)
- CVSS 4.0 / 3.1 (vulnerability severity scoring)
- ENISA Threat Landscape Reports
- [Other frameworks per ISMS-POL-00]

**United States Federal Requirements:**
References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where the organization has explicit US federal contractual obligations, as defined in **ISMS-POL-00**.

For complete regulatory categorization, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

### 1.5 Integration with Risk Management (Clause 6.1)

Threat intelligence SHALL inform the organization's risk assessment process per ISO 27001:2022 Clause 6.1.

**Mandatory Integration Points:**
- Threat intelligence findings SHALL be reviewed during risk assessment updates
- Emerging threats SHALL trigger risk reassessment when likelihood or impact changes
- Risk register SHALL reference threat intelligence reports supporting likelihood estimates
- **Vulnerability risks SHALL be quantified using CVSS scores (4.0 preferred, 3.1 acceptable) combined with active exploitation intelligence**
- Quarterly: Threat Intelligence Team submits risk assessment update report to Risk Management

**Evidence Requirements:**
- Cross-reference: Threat Intelligence Report ID → Risk Register Entry ID
- Documentation: "How threat intelligence changed risk assessment"
- **CVSS-based vulnerability risk quantification** (when vulnerability-related risks)
- Tracked in: ISMS-IMP-A.5.7.3 Sheet 13 (Risk Assessment Updates)

**Example:** "TI Report 2024-Q4-015 (Ransomware campaign targeting hosting sector) → Risk REG-023 (Data Confidentiality) likelihood updated from 'Medium' to 'High' → Approved by CRO on [date]"

**Example (CVSS-based):** "TI Report 2025-Q1-003 (CVE-2024-56789, CVSS 4.0 Base Score 9.2, active mass exploitation) → Risk REG-047 (System Availability) impact updated to 'Critical', likelihood 'High' → Emergency patching authorized by CRO on [date]"

This integration fulfills ISO 27001:2022 Clause 6.1.2(a) "identify information security risks" and 6.1.2(b) "assess the consequences and realistic likelihood of the information security risks."

**Target:** ≥3 risk assessment updates per quarter driven by threat intelligence.

---

## 2. Policy Documents

### 2.1 Policy Structure

The threat intelligence policy framework consists of the following modular documents:

| Document ID | Title | Purpose | Lines |
|-------------|-------|---------|-------|
| **ISMS-POL-A.5.7** | Master Framework | This document - index and overview | ~900 |
| **ISMS-POL-A.5.7-S1** | Purpose, Scope, Definitions | Foundation and terminology, CVSS definitions | ~350 |
| **ISMS-POL-A.5.7-S2** | Threat Intelligence Requirements | Collection, analysis, dissemination, CVSS scoring | ~400 |
| **ISMS-POL-A.5.7-S3** | Roles and Responsibilities | RACI and accountability | ~300 |
| **ISMS-POL-A.5.7-S4** | Policy Governance | Review, exceptions, compliance | ~250 |
| **ISMS-POL-A.5.7-S5** | Annexes | Supporting materials, expanded CVSS glossary | Variable |
| **ISMS-POL-A.5.7-S5.A** | Threat Intelligence Source Standards | Evaluation criteria, reliability ratings, CVSS support | ~220 |
| **ISMS-POL-A.5.7-S5.B** | Intelligence Report Templates | Strategic, tactical, operational formats | ~150 |
| **ISMS-POL-A.5.7-S5.C** | Threat Intelligence Procedure Summary | Intelligence cycle, workflows | ~200 |
| **ISMS-POL-A.5.7-S5.D** | Quick Reference Guide | Stakeholder cheat sheet | ~100 |
| **ISMS-POL-A.5.7-S5.E** | Glossary and Acronyms | Definitions including CVSS 4.0/3.1 | ~150 |
| **ISMS-POL-A.5.7-S5.F** | Document Relationships | Cross-references and integration | ~100 |

### 2.2 Document Maintenance

Each section document (S1-S5) may be updated independently based on operational needs, regulatory changes, or lessons learned. Major framework changes require updates to this master document and C-suite approval.

**Version synchronization**: When a section document undergoes major revision (version X.0), this master document's version SHALL be reviewed and updated if the changes affect overall framework structure or objectives.

---

## 3. Implementation Specifications

### 3.1 Assessment Workbook Structure

The threat intelligence framework is operationalized through four assessment workbooks, each generated via Python scripts to ensure consistency and audit readiness:

| Workbook ID | Title | Purpose | Sheets | Generator Script |
|-------------|-------|---------|--------|------------------|
| **ISMS-IMP-A.5.7.1** | Threat Intelligence Sources Assessment | Source inventory, vetting, performance tracking | 15 | generate_a57_1_sources.py |
| **ISMS-IMP-A.5.7.2** | Intelligence Collection & Analysis Assessment | Collection processes, analysis quality, VTL records with CVSS | 13 | generate_a57_2_collection_analysis.py |
| **ISMS-IMP-A.5.7.3** | Intelligence Integration & Distribution Assessment | SIEM/EDR integration, stakeholder distribution, effectiveness | 15 | generate_a57_3_integration.py |
| **ISMS-IMP-A.5.7.4** | Effectiveness Dashboard | Consolidated KPIs, executive summary, audit evidence | 9 | generate_a57_4_dashboard.py |

**Total Assessment Capacity**: 52 worksheets providing comprehensive threat intelligence program documentation and evidence generation.

### 3.2 Key Integration Points

**VulnerabilityThreatLink (VTL) Schema** (ISMS-IMP-A.5.7.2 Sheet 8):
- Links threat intelligence to specific CVEs when active exploitation detected
- **CRITICAL UPDATE (v2.0)**: VTL records now include CVSS 4.0/3.1 scoring
- Enables automated priority escalation in vulnerability management (Control A.8.8 when implemented)
- **Schema fields include**: CVE ID, CVSS Version, CVSS Base Score, CVSS Vector, Exploitation Status, Threat Actor, Criticality
- Bidirectional data flow: A.5.7 (exploitation intel) → A.8.8 (emergency patching), A.8.8 (remediation status) → A.5.7 (tracking)

**Risk Assessment Integration** (ISMS-IMP-A.5.7.3 Sheet 13):
- Documents how threat intelligence updates risk assessments (Clause 6.1 - MANDATORY)
- **CVSS-based risk quantification** for vulnerability-related threats
- Cross-references TI Report IDs to Risk Register Entry IDs
- Target: ≥3 risk assessment updates per quarter

**Prevention Tracking** (ISMS-IMP-A.5.7.3 Sheet 7):
- Objective evidence of prevented incidents with before/after validation
- **CVSS scores** document severity of prevented vulnerability exploitation
- Technical validation evidence (SIEM logs, scan results, EDR telemetry)
- Target: ≥3 validated prevented incidents per quarter

---

## 4. Compliance and Evidence Generation

### 4.1 ISO 27001:2022 Compliance Mapping

This framework fulfills the following ISO 27001:2022 requirements:

**Annex A Control 5.7** (Threat Intelligence):
- Collection from multiple sources (internal, external, commercial, OSINT)
- Analysis and production of actionable intelligence
- **Vulnerability severity assessment using CVSS 4.0/3.1 standards**
- Dissemination to appropriate stakeholders
- Integration with security operations and risk management

**Clause 6.1** (Actions to Address Risks and Opportunities):
- Threat intelligence informs risk identification (6.1.2.a)
- Exploitation intelligence supports likelihood/impact assessment (6.1.2.b)
- **CVSS-based quantitative risk scoring** for vulnerability threats
- Evidence: ISMS-IMP-A.5.7.3 Sheet 13

**Clause 9.1** (Monitoring, Measurement, Analysis and Evaluation):
- Threat intelligence effectiveness metrics (KPIs in ISMS-IMP-A.5.7.4)
- Source accuracy validation (≥85% target)
- Stakeholder satisfaction measurement (≥4.0/5.0 target)

### 4.2 Evidence Types

The threat intelligence framework generates the following categories of audit evidence:

**Category 1: Clause 6.1 Integration Evidence** (Section 4.4.1)
- Quarterly report: "Threat Intelligence Impact on Risk Assessment"
- Cross-reference: TI Report ID → Risk Register Entry ID → Likelihood/Impact Changes
- **CVSS-based vulnerability risk quantification documentation**
- Risk owner approval documentation
- **Target**: ≥3 risk assessment updates per quarter

**Category 2: Prevented Incident Evidence** (Section 4.4.2)
- Prevented incident register with before/after states
- **CVSS scores** demonstrating severity of prevented vulnerability exploits
- Technical validation evidence (scan results, SIEM logs, EDR telemetry)
- SIEM query IDs for reproducibility
- **Target**: ≥3 documented prevented incidents per quarter

**Category 3: Intelligence Accuracy Validation** (Section 4.4.3)
- Quarterly source performance analysis
- Per-source accuracy metrics (Admiralty Code ratings)
- **CVSS accuracy validation** (source-reported vs. actual CVSS scores)
- Source continuation/discontinuation decisions
- **Target**: ≥85% overall accuracy rate

**Category 4: Incident-TI Integration Evidence** (Section 4.4.4)
- Incident register cross-reference: Incident ID → TI Reports Used
- **CVSS context** for vulnerability-related incidents
- Incident handler effectiveness ratings
- Investigation time reduction metrics
- **Target**: ≥70% of P1/P2 incidents use TI

**Category 5: Intelligence-Driven Decisions** (Section 4.4.5)
- Decision register: TI Report → Decision → Implementation → Outcome
- **CVSS-based prioritization decisions** for vulnerability remediation
- Measurable outcomes (incidents prevented, costs avoided, time saved)
- **Target**: ≥5 intelligence-driven decisions per quarter

**Category 6: Business Continuity Evidence** (Section 4.4.6)
- Backup personnel assignments for threat intelligence roles
- Critical source access documentation
- Annual continuity test results
- **Target**: 100% critical roles with trained backup

### 4.3 Assessment Schedule

**Quarterly Assessments** (Operational Review):
- Update all four workbooks (ISMS-IMP-A.5.7.1 through A.5.7.4)
- Validate against sanity check scripts
- Review KPIs against targets
- Document new VTL records with CVSS scores
- Prepare quarterly briefing for CISO

**Annual Assessment** (Strategic Review):
- Comprehensive program evaluation
- Threat landscape analysis and trend identification
- Source portfolio optimization (add/remove sources)
- **CVSS version adoption status** (4.0 migration progress)
- Training needs assessment
- Budget planning for next fiscal year

### 4.4 Quantitative Compliance Targets

**4.4.1 Clause 6.1 Risk Assessment Updates**
- **Target**: ≥3 risk assessment updates per quarter driven by threat intelligence
- **Measurement**: Count of Risk Register entries updated with TI Report ID cross-references
- **CVSS Integration**: Vulnerability-related risk updates SHALL include CVSS scores
- **Evidence**: ISMS-IMP-A.5.7.3 Sheet 13
- **Approval**: Chief Risk Officer (CRO) must approve all TI-driven risk updates

**4.4.2 Prevented Incidents (Validated)**
- **Target**: ≥3 documented prevented incidents per quarter
- **Validation Requirements**:
  - Before-state: Vulnerability existed (scan evidence, asset confirmation)
  - TI alert: Threat intelligence warned of exploitation (report ID, timestamp)
  - Action: Remediation deployed (patch, mitigation, compensating control)
  - After-state: Vulnerability eliminated (re-scan evidence)
  - **CVSS Documentation**: Original CVSS score and vector for prevented vulnerability exploit
  - Validation: Technical evidence (SIEM logs, scan results, EDR telemetry)
- **Evidence**: ISMS-IMP-A.5.7.3 Sheet 7
- **Quality Standard**: Prevented incidents must have reproducible technical evidence, not just analyst claims

**4.4.3 Intelligence Source Accuracy**
- **Target**: ≥85% overall source accuracy rate
- **Validation**: Quarterly validation of intelligence accuracy against ground truth
- **Per-Source Minimum**: ≥80% accuracy to maintain subscription/access
- **CVSS Accuracy**: Validate CVSS scores provided by sources against NVD/vendor advisories
- **False Positive Threshold**: ≤15% across all sources
- **Evidence**: ISMS-IMP-A.5.7.1 Sheet 14
- **Action**: Sources consistently below 80% accuracy SHALL be deprecated

**4.4.4 Incident-TI Integration**
- **Target**: ≥70% of P1/P2 incidents enriched with threat intelligence
- **Measurement**: Incident register cross-reference to TI Report IDs
- **CVSS Context**: For vulnerability-related incidents, document CVSS scores
- **Effectiveness**: Incident handlers rate TI usefulness (5-point scale, target ≥4.0)
- **Evidence**: ISMS-IMP-A.5.7.3 Sheet 14
- **Integration Point**: Mandatory for Controls A.5.24-5.28 (Incident Management)

**4.4.5 Intelligence-Driven Decisions**
- **Target**: ≥5 intelligence-driven security decisions per quarter
- **Categories**: Policy changes, technical controls, security investments, training updates, **CVSS-based vulnerability prioritization**
- **Measurement**: Decision register with TI Report → Decision → Implementation → Outcome
- **Outcome Tracking**: Measurable results (incidents prevented, costs avoided, time saved)
- **Evidence**: ISMS-IMP-A.5.7.3 Sheet 15

**4.4.6 Business Continuity**
- **Target**: 100% of critical threat intelligence roles have trained backup personnel
- **Verification**: Annual continuity test (primary personnel unavailable scenario)
- **Documentation**: Backup assignments, training completion records, test results
- **Critical Sources**: All commercial TI platforms have ≥2 authorized users
- **Evidence**: ISMS-IMP-A.5.7.1 Sheet 15

### 4.5 Audit Preparation Checklist

**T-30 days before certification audit:**
- [ ] Generate all quarterly workbooks (A.5.7.1 through A.5.7.4) for last 4 quarters
- [ ] Validate against sanity check scripts (excel_sanity_check_a57_1 through a57_4.py)
- [ ] Review all KPIs against targets (Section 4.4.1 through 4.4.6)
- [ ] **Verify CVSS data quality** in VTL records (Sheet 8) and prevented incidents (Sheet 7)
- [ ] Document any non-conformances with corrective action plans
- [ ] Prepare executive summary of threat intelligence program effectiveness
- [ ] Compile evidence package (TI reports, risk assessment updates, prevented incidents)

**T-14 days:**
- [ ] CISO review of audit readiness
- [ ] Stakeholder interviews scheduled (sample threat intelligence consumers)
- [ ] **CVSS scoring methodology** documented and ready for auditor questions
- [ ] Technical demonstrations prepared (SIEM integration, VTL workflow, dashboard)
- [ ] Prepare auditor briefing document (framework overview, evidence locations)

**T-7 days:**
- [ ] Final evidence package review
- [ ] Print physical copies if required by audit protocol
- [ ] Ensure all workbook cross-references are valid
- [ ] **Validate CVSS version consistency** across all VTL records
- [ ] Conduct mock audit walkthrough with internal team

**T-0 (Audit Day):**
- [ ] All assessment workbooks accessible to auditor
- [ ] ISMS-POL-A.5.7 and all section documents (S1-S5) available
- [ ] Subject matter experts (Threat Intelligence Team Lead, SOC Manager) available
- [ ] Live demonstration capability (SIEM queries, dashboard access)
- [ ] **CVSS scoring examples** prepared for vulnerability-based TI

---

## 5. Validation Scripts

### 5.1 Sanity Check Scripts

Four Python validation scripts ensure data quality and completeness before assessment workbooks are used for decision-making or audit evidence:

| Script | Workbook | Validation Focus |
|--------|----------|------------------|
| **excel_sanity_check_a57_1.py** | WB1 (Sources) | Source inventory completeness, Admiralty Code compliance, CVSS support tracking |
| **excel_sanity_check_a57_2.py** | WB2 (Collection & Analysis) | VTL schema compliance with CVSS fields, mandatory fields, confidence levels |
| **excel_sanity_check_a57_3.py** | WB3 (Integration) | Cross-reference integrity, KPI calculations, evidence completeness |
| **excel_sanity_check_a57_4.py** | WB4 (Dashboard) | KPI thresholds, aggregation accuracy, executive summary quality |

**Usage Pattern**:
```bash
python excel_sanity_check_a57_1.py ISMS_A_5_7_1_Sources_Assessment_20250109.xlsx
python excel_sanity_check_a57_2.py ISMS_A_5_7_2_Collection_Analysis_20250109.xlsx
python excel_sanity_check_a57_3.py ISMS_A_5_7_3_Integration_Distribution_20250109.xlsx
python excel_sanity_check_a57_4.py ISMS_A_5_7_4_Effectiveness_Dashboard_20250109.xlsx
```

**Validation Categories**:
- **Structural**: Required sheets present, column headers correct
- **Data Quality**: No blank cells in mandatory columns, valid data types
- **Business Rules**: CVSS scores in valid range (0.0-10.0), exploitation status consistent with criticality
- **Cross-References**: TI Report IDs link to Risk Register, VTL records link to CVEs
- **Calculations**: KPI formulas correct, aggregations match source data

### 5.2 Quality Gates

Assessment workbooks SHALL NOT be used for decision-making or audit evidence until:
1. All applicable sanity check scripts pass without errors
2. Warnings reviewed and justified (e.g., "No VTL records this quarter" if no active exploitation detected)
3. CISO or delegate signs off on assessment quality

---

## 6. Tool Integration Architecture

### 6.1 Integration Overview

Threat intelligence integrates with the following organizational security tools and systems:

**Detection & Response Layer**:
- Security Information and Event Management (SIEM) - IOC ingestion, correlation rules, threat hunting queries
- Endpoint Detection and Response (EDR) - Malware signatures, behavioral indicators, threat actor TTPs
- Intrusion Detection/Prevention Systems (IDS/IPS) - Exploit signatures, network-based IOCs
- Email Security Gateway - Phishing indicators, malicious domains, sender reputation
- Web Proxy / Content Filtering - Malicious URLs, C2 infrastructure, threat actor domains

**Vulnerability Management Layer** (Control A.8.8 - OPTIONAL when implemented):
- Vulnerability scanners - **CVSS-based prioritization** informed by active exploitation intelligence
- Patch management systems - Emergency patching triggers for actively exploited CVEs
- **VulnerabilityThreatLink (VTL) data flow** - Bidirectional integration between A.5.7 and A.8.8
- Asset management - Critical asset identification for vulnerability prioritization

**Incident Response Layer** (Controls A.5.24-5.28 - MANDATORY):
- Incident ticketing systems - Automatic TI enrichment for new incidents
- Forensic analysis tools - Threat actor attribution, campaign correlation
- Threat hunting platforms - Proactive searches based on tactical intelligence
- Security orchestration (SOAR) - Automated response playbooks for known threats

**Risk Management Layer** (Clause 6.1 - MANDATORY):
- Risk register - Threat intelligence updates likelihood/impact assessments
- **CVSS-based risk quantification** for vulnerability-related threats
- Risk treatment tracking - TI-driven security investment decisions

### 6.2 Data Formats and Standards

Threat intelligence SHALL be shared and integrated using industry-standard formats where possible:

**Structured Threat Information Expression (STIX) 2.1**:
- Primary format for threat intelligence exchange
- Supports indicators, threat actors, TTPs, campaigns, malware

**Trusted Automated Exchange of Indicator Information (TAXII) 2.1**:
- Transport protocol for STIX data
- Enables automated intelligence sharing with ISACs/ISAOs

**Common Vulnerability Scoring System (CVSS)**:
- **CVSS 4.0** (preferred) - Current standard for vulnerability severity assessment
- **CVSS 3.1** (legacy) - Supported for backward compatibility
- **Migration timeline**: 12 months from policy approval for full CVSS 4.0 adoption
- **VTL schema**: Supports both versions with explicit version tagging

**MITRE ATT&CK**:
- Framework for describing adversary TTPs
- Tactical intelligence mapped to ATT&CK techniques
- Detection and mitigation strategies organized by ATT&CK

**Traffic Light Protocol (TLP)**:
- Information sharing classifications (CLEAR, GREEN, AMBER, AMBER+STRICT, RED)
- Ensures proper handling of sensitive intelligence

### 6.3 Integration Maintenance

**Quarterly Review**:
- Validate that all integrations are operational
- Review IOC ingestion rates and detection coverage
- **Verify CVSS scores are flowing correctly** to vulnerability management (when A.8.8 implemented)
- Test VTL data exchange (A.5.7 → A.8.8, A.8.8 → A.5.7)
- Update integration documentation for any changes

**Annual Assessment**:
- Evaluate integration effectiveness (detection rates, false positives, time to operationalize)
- Identify gaps in tool coverage or intelligence types
- **CVSS version migration progress** review
- Plan integration improvements for next fiscal year

---

## 7. Cross-Control Integration

### 7.1 Mandatory Integrations

**Clause 6.1 - Actions to Address Risks and Opportunities** (ISO 27001:2022):
- Threat intelligence MUST inform risk assessment
- **CVSS-based vulnerability risk quantification** required for vulnerability-related threats
- Target: ≥3 risk assessment updates per quarter
- Evidence: ISMS-IMP-A.5.7.3 Sheet 13
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.1

**Controls A.5.24-5.28 - Incident Management**:
- Threat intelligence MUST support incident investigation and response
- Target: ≥70% of P1/P2 incidents use threat intelligence
- **CVSS context** for vulnerability-related incidents
- Evidence: ISMS-IMP-A.5.7.3 Sheet 14
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.2

**Control A.8.16 - Monitoring Activities**:
- Threat intelligence provides detection signatures (IOCs, YARA rules, Sigma rules)
- IOCs deployed to SIEM, EDR, IDS/IPS, email gateway, web proxy
- Monitoring telemetry feeds threat intelligence (internal source data)
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.3

### 7.2 Optional Integrations

**Control A.8.8 - Management of Technical Vulnerabilities** (OPTIONAL when implemented):
- **VulnerabilityThreatLink (VTL) schema** enables automated data exchange
- **CVSS 4.0/3.1 scoring** bridges threat intelligence and vulnerability management
- Active exploitation intelligence triggers emergency patching
- Bidirectional flow: A.5.7 (exploitation) → A.8.8 (priority), A.8.8 (remediation status) → A.5.7 (tracking)
- Without A.8.8: Basic TI consumption (CISA KEV, vendor advisories, no VTL)
- With A.8.8: Full VTL integration with automated priority escalation
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.4

**Controls A.5.19-5.22 - Supplier Security Management**:
- Threat intelligence includes supply chain threats
- Supplier vulnerabilities and compromises tracked
- Responsible disclosure coordination with suppliers
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.5

**Control A.5.23 - Cloud Security**:
- Cloud-specific threat intelligence collected
- Cloud provider intelligence feeds integrated
- Multi-cloud threat visibility
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.6

**Control A.8.23 - Web Filtering**:
- Threat intelligence feeds malicious URL/domain blocklists
- Web filtering telemetry informs threat intelligence (blocked access attempts)
- Integration documented in ISMS-POL-A.5.7-S4 Section 4.7

---

## 8. Training and Awareness

### 8.1 Threat Intelligence Team Training

**Initial Training** (New Threat Intelligence Analysts):
- Threat intelligence fundamentals (intelligence cycle, analysis methodologies)
- MITRE ATT&CK framework and adversary TTPs
- **CVSS 4.0/3.1 scoring methodology** and vulnerability severity assessment
- Tool-specific training (TIP platform, SIEM, analysis tools)
- Information sharing protocols (TLP, STIX/TAXII)
- Organizational context (industry threats, risk profile, critical assets)

**Ongoing Professional Development**:
- Annual threat intelligence conference attendance or equivalent training
- **CVSS updates** and vulnerability assessment best practices
- Threat actor research and adversary tracking techniques
- Advanced analysis tradecraft and cognitive bias mitigation
- Industry certifications (GIAC GCTI, SANS FOR578, or equivalent)

### 8.2 Stakeholder Training

**Security Operations Center (SOC) Analysts**:
- How to consume threat intelligence for alert triage and investigation
- **Understanding CVSS scores** in vulnerability-related incidents
- Using IOCs and TTPs for threat hunting
- TI platform access and query techniques

**Incident Response Team**:
- Integrating threat intelligence into incident investigations
- **CVSS-based prioritization** for vulnerability-related incidents
- Leveraging TI for attribution and campaign correlation
- Providing feedback to improve future intelligence

**Vulnerability Management Team** (when Control A.8.8 implemented):
- **VulnerabilityThreatLink (VTL) workflow** and exploitation intelligence
- **CVSS 4.0/3.1 scoring interpretation** and prioritization methodology
- Emergency patching procedures for actively exploited CVEs
- Remediation status reporting back to threat intelligence

**Executive Leadership**:
- Strategic threat intelligence briefings (quarterly)
- **CVSS-based risk quantification** for vulnerability threats
- Threat landscape trends affecting organizational risk profile
- TI-informed security investment decisions

### 8.3 General Security Awareness

**All Employees**:
- Phishing and social engineering threat awareness
- Reporting suspicious activity to security team
- Understanding TLP classifications when handling shared intelligence
- Basic cyber threat landscape awareness

**Frequency**: Annual security awareness training with quarterly threat bulletins highlighting current campaigns and defensive measures.

---

## 9. Policy Governance

### 9.1 Policy Review and Updates

**Annual Review** (Mandatory - Q4):
- Comprehensive review of all policy sections (Master + S1-S5)
- Assessment of policy effectiveness based on:
  - Audit findings and recommendations
  - Incident lessons learned (TI gaps that contributed to incidents)
  - Threat landscape evolution (new adversary TTPs, attack vectors)
  - **CVSS version adoption progress** and vulnerability scoring effectiveness
  - Regulatory changes (new compliance requirements)
  - Technology changes (new intelligence platforms, integration capabilities)
- Stakeholder feedback (TI consumers, analysts, management)
- KPI performance against targets (Section 4.4)

**Quarterly Light Review**:
- Metrics-only review (no policy changes unless critical)
- KPI dashboard review (Section 4.4 targets)
- VTL integration effectiveness (when A.8.8 implemented)
- Source performance validation (Admiralty Code ratings)

**Triggered Reviews**:
- Major incident revealing TI gaps or failures
- Significant regulatory changes
- **Major CVSS version updates** (e.g., CVSS 5.0 release)
- Organizational restructuring affecting TI roles
- Technology changes (new intelligence platforms, integration capabilities)
- Audit findings requiring policy updates

### 9.2 Version Control

**Major Version (X.0):** Structural changes, scope modifications, new regulatory requirements, **CVSS version updates**  
**Minor Version (X.Y):** Content updates, clarifications, additions without structural change

**Master Framework Versioning:**
- This master document version reflects overall framework state
- Individual section versions (S1-S5) may increment independently
- Major framework changes require master document version update

**Current Version**: 2.0 (Added CVSS 4.0/3.1 vulnerability scoring requirements)

### 9.3 Change Process

**Standard Changes:**
1. Change request submitted to Policy Owner (CISO)
2. Impact assessment (affected stakeholders, systems, processes, sources)
3. Stakeholder consultation (Threat Intelligence Team, SOC, Risk Management, Vulnerability Management)
4. Draft revision prepared
5. Review and approval by CISO and required stakeholders
6. Communication plan executed (training updates, policy portal)
7. Implementation tracking (30/60/90 day checkpoints)

**Emergency Changes:**
- Critical threats or regulatory deadlines may require expedited process
- Emergency approval by CISO with retrospective stakeholder review
- Documentation of justification for emergency process

### 9.4 Communication

**Policy Updates Communicated Via:**
- Policy portal (central repository)
- Email notifications to all relevant stakeholders
- Security awareness training updates
- Team meetings (Threat Intelligence, SOC, Incident Response, Vulnerability Management)
- Quarterly CISO briefings to Executive Management
- Intelligence sharing community notifications (ISACs/ISAOs)

---

## 10. Reference Documents

### 10.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.5.7 (this document) + Sections S1 through S5.F (See Section 2)

**Assessment Layer:**
- ISMS-IMP-A.5.7.1 — Threat Intelligence Sources Assessment (Markdown + Excel)
- ISMS-IMP-A.5.7.2 — Intelligence Collection & Analysis Assessment (Markdown + Excel) - **Includes CVSS fields in VTL schema**
- ISMS-IMP-A.5.7.3 — Intelligence Integration & Distribution Assessment (Markdown + Excel)
- ISMS-IMP-A.5.7.4 — Effectiveness Dashboard (Markdown + Excel)

**Automation Layer:**
- Generator Scripts (4 Python files) - **Updated for CVSS 4.0/3.1 support**
- Validation Scripts (4 Python files) - **Updated for CVSS field validation**

**Related ISMS Policies (Integration documented in S4):**
- ISMS-POL-Clause 6.1 - Risk Assessment (MANDATORY integration, **CVSS-based risk quantification**)
- ISMS-POL-A.5.24-5.28 - Incident Management (MANDATORY integration)
- ISMS-POL-A.8.16 - Monitoring Activities (MANDATORY integration)  
- ISMS-POL-A.8.8 - Vulnerability Management (OPTIONAL - when Control A.8.8 implemented, **CVSS/VTL integration**)
- ISMS-POL-A.5.19-5.22 - Supplier Security (OPTIONAL)
- ISMS-POL-A.5.23 - Cloud Security (OPTIONAL)
- ISMS-POL-A.8.23 - Web Filtering (OPTIONAL)

### 10.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 — Information Security Management Systems
- ISO/IEC 27002:2022 — Information Security Controls (Control 5.7 guidance)
- ISO/IEC 27005:2022 — Information Security Risk Management

**Vulnerability Scoring:**
- **CVSS 4.0** — Common Vulnerability Scoring System (Current Standard, Nov 2023)
- **CVSS 3.1** — Common Vulnerability Scoring System (Legacy Support)
- CVSS User Guide and Specification Documents (FIRST.org)

**Threat Intelligence Frameworks:**
- MITRE ATT&CK Framework — Adversary tactics and techniques
- STIX/TAXII — Structured Threat Information Expression / Trusted Automated Exchange
- Traffic Light Protocol (TLP) — Information sharing markings
- Diamond Model — Intrusion analysis methodology
- Cyber Kill Chain — Attack lifecycle framework

**Regulatory:**
- Swiss Federal Act on Data Protection (FADP/nDSG)
- EU General Data Protection Regulation (GDPR) — where applicable
- NIS2 Directive — Network and Information Security (EU)
- DORA — Digital Operational Resilience Act (EU financial services)

**Industry Guidelines:**
- FIRST (Forum of Incident Response and Security Teams) — Information sharing guidelines, **CVSS governance**
- ENISA — Threat Landscape Reports
- SANS Internet Storm Center — Threat intelligence resources
- OWASP — Web application threat intelligence

---

## Appendix A: Philosophy & Methodology

### A.1 Evidence Over Theater

> "The first principle is that you must not fool yourself—and you are the easiest person to fool."  
*— Richard Feynman, Nobel Prize-winning physicist*

This framework is designed to prevent **cargo cult threat intelligence** — the practice of subscribing to threat intelligence platforms without actually collecting, analyzing, or operationalizing intelligence. Saying "we have threat intelligence" without knowing source quality, integration status, or operational effectiveness is self-deception.

**The assessment workbooks force specificity:**
- **What** sources are subscribed to? (inventory with Admiralty Code ratings, **CVSS support verification**)
- **How** is intelligence analyzed? (frameworks, methodologies, analyst capabilities, **CVSS scoring**)
- **Where** is intelligence integrated? (SIEM, EDR, risk assessment, incident response, **VTL workflow**)
- **Who** consumes intelligence? (stakeholder registry, distribution tracking)
- **Proof** of effectiveness? (KPIs, metrics, stakeholder feedback, prevented incidents with **CVSS documentation**)

If these questions cannot be answered with quantitative evidence, the organization does not have threat intelligence — it has threat intelligence theater.

### A.2 System Engineering Approach

This framework applies **engineering discipline** to security governance:

**Traditional Compliance:**
- Policy documents describe ideal state
- Auditors ask questions, check boxes
- Actual implementation state unknown until incident occurs
- Gap analysis is subjective and incomplete

**System Engineering Compliance:**
- Policy documents define measurable requirements
- Python scripts generate standardized assessment workbooks
- Threat Intelligence Team documents actual capabilities with evidence
- Validation scripts ensure data quality and completeness
- Dashboard aggregates quantitative metrics (source reliability, production volume, integration coverage, **CVSS-based vulnerability tracking**)
- Gap analysis is objective, prioritized, and actionable

**Benefits:**
- Repeatable assessments (run quarterly, compare trends)
- Maintainable over time (scripts, not manual documents)
- Audit-ready from day one (structured evidence, clear metrics)
- Stakeholder efficiency (fill yellow cells, not create documents from scratch)

### A.3 Intelligence-Driven Security

Threat intelligence is not an end in itself — it is a means to:

**Strategic Level:**
- Inform executive risk decisions (board briefings, budget prioritization)
- Guide security strategy and roadmap
- Support M&A due diligence (threat actor targeting, sector risks)
- **CVSS-based vulnerability risk quantification** for portfolio risk assessment

**Tactical Level:**
- Prioritize vulnerability remediation (**CVSS + exploitation intelligence**)
- Tune detection rules (reduce false positives, improve accuracy)
- Guide threat hunting campaigns (adversary TTPs, infrastructure)

**Operational Level:**
- Enrich security alerts (context, attribution, severity, **CVSS scores**)
- Accelerate incident response (known IOCs, playbooks, containment strategies)
- Support forensic investigations (timeline correlation, artifact identification)

**The value of threat intelligence is measured by its impact on security outcomes, not by the volume of IOCs collected or CVSS scores tracked.**

### A.4 CVSS Integration Rationale

**Why CVSS 4.0 + 3.1 Dual Support:**
- **CVSS 4.0** is the current standard (Nov 2023), offering improved severity assessment
- **CVSS 3.1** remains widely deployed in legacy systems and databases
- **12-month transition period** allows gradual migration without disruption
- **VTL schema** supports both versions with explicit version tagging
- **Backward compatibility** ensures historical data remains valid

**CVSS in Threat Intelligence Context:**
- **Exploitation + Severity = Priority**: A CVSS 6.5 vulnerability with mass exploitation may be higher priority than a CVSS 9.0 vulnerability with no known exploits
- **Risk Quantification**: CVSS enables objective, quantitative risk assessment for vulnerability-related threats (Clause 6.1)
- **Automated Prioritization**: VTL schema uses CVSS scores to trigger emergency patching workflows (when A.8.8 implemented)
- **Audit Evidence**: CVSS scores in prevented incidents demonstrate severity of avoided risk

**Common Mistake to Avoid:**
- ❌ **Using CVSS alone** for prioritization (ignores exploitation reality)
- ✅ **Using CVSS + Active Exploitation** for intelligent prioritization (evidence-based)

---

## Appendix B: Document Version History

| Version | Date | Sections Changed | Summary of Changes |
|---------|------|------------------|-------------------|
| 1.0 | [Date] | All | Initial framework established |

---

**END OF MASTER DOCUMENT**