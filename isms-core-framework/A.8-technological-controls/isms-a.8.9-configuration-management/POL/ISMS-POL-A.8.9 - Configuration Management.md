<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.9:framework:GOV-POL:a.8.9 -->
**ISMS-POL-A.8.9 – Configuration Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Configuration Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.9 |
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
| 1.0 | [Date] | CISO / Configuration Manager | Initial consolidated policy for ISO 27001:2022 certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Technical: Chief Information Officer (CIO)
- Operations: Chief Technology Officer (CTO)
- Governance: Configuration Manager
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.9.1-UG/TG (Baseline Configuration Assessment)
- ISMS-IMP-A.8.9.2-UG/TG (Change Control Assessment)
- ISMS-IMP-A.8.9.3-UG/TG (Configuration Monitoring Assessment)
- ISMS-IMP-A.8.9.4-UG/TG (Security Hardening Assessment)
- ISMS-IMP-A.8.9.5-UG/TG (Compliance Dashboard)
- ISMS-CTX-A.8.9 (Configuration Management Reference - NOT ISMS)
- ISO/IEC 27001:2022 Control A.8.9

---

## Executive Summary

This policy establishes [Organization]'s requirements for configuration management controls in accordance with ISO/IEC 27001:2022 Control A.8.9.

**Scope**: This policy applies to all IT assets requiring configuration management (compute infrastructure, network devices, storage systems, cloud services, applications, security tools, IoT/OT systems) across all environments (production, non-production, cloud, on-premises) and all lifecycle stages (deployment, operation, change, decommissioning).

**Purpose**: Define organizational requirements for configuration management. This policy establishes WHAT must be configured, WHEN changes require approval, WHO is accountable, and WHICH standards apply. Implementation procedures (HOW) are in ISMS-IMP-A.8.9. Technical reference is in ISMS-CTX-A.8.9 (NOT ISMS).

**Regulatory Alignment**: This policy addresses mandatory compliance per ISMS-POL-00, including Swiss nDSG, EU GDPR (where applicable), and ISO/IEC 27001:2022. Conditional requirements (PCI DSS v4.0.1, HIPAA, FINMA, DORA, NIS2) apply where [Organization]'s activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.9

**ISO/IEC 27001:2022 Annex A.8.9 - Configuration Management**

> *"Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed."*

**German (SN EN ISO/IEC 27001:2023):**

> *"Konfigurationen, einschließlich Sicherheitskonfigurationen, von Hardware, Software, Diensten und Netzwerken müssen festgelegt, dokumentiert, umgesetzt, überwacht und überprüft werden."*

**Control Objective**: Establish secure baseline configurations, prevent unauthorized changes, detect configuration drift, enforce security hardening, and enable rapid recovery while supporting business operations.

**This Policy Addresses**:

- Baseline configuration establishment and documentation
- Change control and approval workflows
- Configuration monitoring and drift detection
- Security hardening and compliance verification
- Roles and responsibilities for configuration management
- Exception and incident management
- Integration with risk assessment processes

## What This Policy Does

This policy:

- **Defines** configuration management requirements aligned with asset criticality
- **Establishes** governance framework for configuration decisions
- **Specifies** mandatory baseline, change, monitoring, and hardening requirements
- **References** regulatory requirements per ISMS-POL-00
- **Identifies** roles and responsibilities

## What This Policy Does NOT Do

This policy does NOT:

- **Specify tools or vendors** (selection based on [Organization]'s assessment)
- **Define system-specific baselines** (see ISMS-CTX-A.8.9 for technical standards)
- **Provide step-by-step procedures** (see ISMS-IMP-A.8.9 assessments)
- **Replace asset management** (builds on A.5.9 asset inventory)
- **Define change system workflows** (organizations adapt to existing ITIL/ServiceNow/Jira)

**Rationale**: Policy stability despite evolving technologies; technical agility without policy revision; clear governance vs execution separation; focused audit scope; adaptability across contexts.

## Scope

**Asset Types**: Compute & infrastructure, network & connectivity, storage & backup, cloud & SaaS, applications & middleware, security & identity, IoT & OT systems

**Environments**: Production, non-production (dev/test/QA/staging), disaster recovery, training, sandbox

**Lifecycle Stages**: Baseline definition, deployment, operational changes, monitoring, decommissioning

**Organizational**: All [Organization] personnel, contractors, third parties, cloud providers

**Out of Scope**: BYOD not managed by [Organization], public systems requiring no security, temporary systems <24h lifecycle (unless processing sensitive data), risk-assessed exclusions with CISO approval

## Regulatory Applicability

Per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory** (Always Applicable)

| Regulation | Requirements |
|------------|--------------|
| ISO/IEC 27001:2022 | Control A.8.9 implementation |
| Swiss nDSG | Art. 8 - Data security through configuration management |
| EU GDPR | Art. 32 - Security of processing (if processing EU data) |

**Tier 2: Conditional** (IF Triggered)

| Regulation | Trigger | Requirements |
|------------|---------|--------------|
| PCI DSS v4.0.1 | Payment card processing | Req. 1-4, 6, 11: Configuration standards |
| HIPAA | US healthcare data | §164.308(a)(8), §164.310: Configuration controls |
| FINMA | Swiss financial services | Risk-based configuration management |
| DORA | EU critical financial | Art. 9, 21: ICT risk & incident management |
| NIS2 | EU essential/important entities | Art. 21: Cybersecurity risk measures |

**Tier 3: Informational**

NIST SP 800-53/128, CIS Controls v8.1, ITIL 4, COBIT 2019, CIS Benchmarks, DISA STIGs

---

# Configuration Management Requirements

## Four-Domain Framework

[Organization] implements configuration management through **four domains**:

1. **Baseline Configuration** - Define secure baselines
2. **Change Control** - Approve configuration changes
3. **Configuration Monitoring** - Detect unauthorized changes
4. **Security Hardening** - Enforce security standards

Each domain has policy requirements (this document), implementation assessment (ISMS-IMP-A.8.9.X), Excel workbooks, evidence registers (100+ rows), and three-tier approval.

## Baseline Configuration Management

[Organization] establishes, documents, and maintains secure baseline configurations.

**2.2.1 Baseline Definition**

**Coverage**:

[Organization] SHALL define baselines for:

- Asset types in active use (not individual assets)
- Critical system configurations
- Network security devices
- Identity and access systems
- Security tooling

**Granularity**: Asset-type level (e.g., "Windows Server 2022 DC Baseline"), NOT individual asset level

**Rationale**: Scalability (100 servers ≠ 100 baselines), compliance verification, rapid deployment, simplified maintenance

**Components**:

Baselines SHALL document:

- OS configurations (security settings, services, registry, kernel parameters)
- Application configurations
- Network configurations (IP, routing, firewall rules, ACLs)
- Security configurations (authentication, encryption, logging, audit)
- Hardening standards applied (CIS, STIG, vendor guides)
- Exceptions and deviations with justification
- Validation criteria

**2.2.2 Approval**

**Workflow**: Three-tier

- Tier 1: Technical Lead validates accuracy/feasibility
- Tier 2: Security Architect validates hardening/compliance
- Tier 3: Configuration Manager/CISO approves

**Criteria**: Technical accuracy, security hardening, regulatory compliance, operational feasibility, complete documentation

**Timeline**:

- New baselines: **14 days**
- Updates: **7 days**
- Emergency: **24 hours**

**2.2.3 Golden Images**

Golden images SHALL:

- Implement approved baselines
- Be tested in non-production
- Contain approved/licensed software only
- Include current security patches
- Be versioned and tracked
- Be refreshed quarterly

**Approval**: Created by authorized personnel, validated by Security, approved by Configuration Manager

**2.2.4 Documentation**

Baselines SHALL be documented with:

- Baseline ID (e.g., "BASE-WIN2022-DC-v1.2")
- Asset type, version, date, approval status
- Configuration parameters and values
- Security rationale
- Testing validation
- Deviation procedures

**Repository**: Version-controlled, access-controlled, backed up weekly, audit-logged

**Review**: Annually (minimum), quarterly (critical systems), ad-hoc (technology/vulnerability/regulatory changes)

**2.2.4.1 Baseline Inventory Status**

[Organization] maintains baseline documentation for production asset types:

- **Baseline Coverage Target**: ≥90% of production asset types
- **Critical Systems** (Tier 1/2): Priority baselines for OS, network devices, cloud services, security tools
- **Repository Location**: Version-controlled repository (referenced in ISMS-IMP-A.8.9.1)
- **Last Audit**: Configuration Manager reviews baseline inventory quarterly

**Detailed Inventory**: Maintained in ISMS-IMP-A.8.9.1 Baseline Configuration Assessment workbook.

**2.2.4.2 Baseline Deprecation**

When asset type is decommissioned or replaced:
- Baseline marked "DEPRECATED" with effective date
- Retained in repository for 3 years for historical reference
- Removed from active compliance monitoring
- Replacement baseline (if applicable) linked in version control

**2.2.5 Infrastructure as Code**

[Organization] SHOULD adopt IaC where feasible:

- Define baselines as code (Terraform, Ansible, CloudFormation, Kubernetes)
- Store in version control (Git)
- Implement review workflows (pull requests, automated testing)
- Use for automated deployment (CI/CD)
- Scan for misconfigurations

**Governance**: IaC SHALL require code review, branch protection, automated testing, change control integration

# ISMS-POL-A.8.9 – Configuration Management (Part 2)

**[CONTINUATION FROM PART 1]**

## Change Control & Configuration Updates

[Organization] ensures all configuration changes follow approved processes with authorization, testing, and documentation.

**2.3.1 Change Classification**

**Change Types**:

| Type | Definition | Approval | Testing | Examples |
|------|------------|----------|---------|----------|
| **Standard** | Pre-approved, low-risk, repeatable | Pre-approved (SOP) | Per SOP | Password resets, standard patches, certificate renewals |
| **Normal** | Requires assessment and approval | CAB approval | Required (test environment) | System upgrades, firewall rules, baseline changes |
| **Emergency** | Urgent for incidents/vulnerabilities | Expedited (CIO/CISO) | Abbreviated/waived | Security exploits, critical outages, critical bugs |

**Classification Criteria**: Impact (users/systems affected), risk (likelihood × consequence), urgency (business timeline), complexity (implementation difficulty), reversibility (rollback ease)

**Emergency Changes**:

- MUST have genuine urgency justification
- MUST NOT be used for convenience or poor planning
- Emergency classification MUST be reviewed post-implementation
- Target: <10% of all changes should be Emergency

**2.3.1.1 Emergency Change Review Process**

All Emergency Changes SHALL undergo post-implementation review within **5 business days**:

1. **Retrospective CAB Review**: CAB validates emergency classification was appropriate
2. **Classification Challenge**: If CAB determines change was not genuine emergency:
   - **First Offense**: Change requester receives training on proper classification
   - **Repeat Offense**: Escalated to CIO/CISO, may result in change privileges restriction
3. **Trend Analysis**: Configuration Manager reports emergency change rate monthly
4. **Threshold Alert**: If emergency rate exceeds 15% in any month, triggers process audit

**Rationale**: Prevents "emergency change" from becoming shortcut for poor planning.

**2.3.2 Change Advisory Board (CAB)**

**Composition**:

- **CAB Chair**: Configuration Manager or senior IT leader (decision authority)
- **Core Members**: Security Architect, Network Manager, Application Owner representatives
- **Variable Members**: Service Owners, Vendor representatives, Compliance Officer (as needed)

**Responsibilities**:

- Review and approve/reject/defer Normal Changes
- Assess change impact and risk
- Verify testing and rollback plans
- Prioritize changes when conflicts exist
- Conduct post-implementation reviews for Emergency Changes
- Identify change trends and process improvements

**Operations**:

- **Regular meetings**: Weekly or bi-weekly (based on change volume)
- **Emergency sessions**: Ad hoc for critical changes
- **Virtual reviews**: Email approval for low-risk changes
- **Documentation**: Meeting minutes, attendance, decisions with rationale

**2.3.2.1 CAB Operational Evidence**

CAB operations SHALL be evidenced through:

1. **Meeting Minutes**: Documented for all sessions, including meeting date, duration, attendees (quorum verification), changes reviewed (Change IDs, requesters), decisions (approve/reject/defer) with rationale, action items and owners

2. **Attendance Tracking**: Core member participation tracked to verify ≥80% target

3. **Decision Register**: All CAB approvals/rejections logged in Change Management System

4. **Retention**: CAB records retained minimum **3 years** for audit

**Minimum Meeting Cadence**: As defined above; if no changes pending, meeting may be cancelled with cancellation documented; emergency approvals documented retrospectively within 24 hours

**Approval Criteria**: Business justification valid, risk assessment complete and acceptable, testing plan adequate, rollback plan exists, implementation window appropriate, required resources available, dependencies coordinated

**2.3.3 Approval Workflows**

**Approval Tiers by Risk**:

| Risk Level | Approval Tiers | Approvers | Timeline |
|------------|----------------|-----------|----------|
| **Standard** | None (pre-approved) | N/A | Immediate execution |
| **Low Risk** | Single-tier | Technical Lead / System Owner | 1-2 business days |
| **Medium Risk** | Two-tier | Technical Lead + Service Owner | 3-5 business days |
| **High Risk** | Three-tier | Technical Lead + Service Owner + CAB | 5-10 business days |
| **Emergency** | Expedited | CIO or CISO (verbal/email) | <4 hours; retro CAB within 5 days |

**Emergency Workflow**:

- Immediate verbal approval by CIO/CISO/CAB Chair
- Implementation under supervision
- Documentation within **24 hours**
- Retrospective CAB review within **5 business days**

**2.3.4 Testing and Validation**

**Testing Requirements**:

Normal Changes SHALL be tested:

- **Dev/Test Environment**: Non-production testing mandatory
- **Validation Criteria**: Success criteria defined before testing
- **Test Documentation**: Results and issues documented
- **Performance Testing**: Verify no unacceptable degradation
- **Security Testing**: Verify no vulnerabilities introduced

**Testing Exemptions**:

- Standard Changes (following pre-tested procedure)
- Emergency Changes (critical urgency, risk accepted by approving authority)
- Low-Risk Changes (Configuration Manager pre-approved exemption)

**Post-Implementation Validation**: Functionality check, impact verification, performance check, security check, rollback capability verification

**Go/No-Go Decision**: Before production, formal decision considering test results, rollback readiness, business readiness, communication completion

**2.3.5 Rollback and Recovery**

**Rollback Planning**:

Changes SHALL include rollback plan documenting:

- **Trigger criteria**: When to execute (specific failure conditions)
- **Procedure**: Step-by-step instructions
- **Timeline**: How long rollback takes
- **Data loss risk**: Any unrecoverable data
- **Backup verification**: Confirm backup exists before change

**Rollback Testing**: High-risk changes SHALL test rollback in non-production, document results, verify before production, executable within defined RTO

**Rollback Triggers**: Change fails validation, unacceptable performance degradation, security vulnerability introduced, business functionality impaired, approving authority directs rollback

**Rollback Authority**:

- CAB Chair or CIO: Major production changes
- Service Owner: Service-specific changes
- On-call Engineer: After-hours emergencies (with management notification)

**2.3.6 Change Success Metrics**

**KPIs**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Change Success Rate** | ≥95% | % of changes not requiring rollback |
| **Emergency Change Rate** | <10% | % classified as Emergency |
| **Approval SLA** | ≥90% | % approved within timeline |
| **CAB Attendance** | ≥80% | Average required member attendance |
| **PIR Completion** | 100% | % with completed PIR within 5 days |

**Reporting**: Calculated monthly, reported to CISO/CIO, analyzed quarterly, process improvements for declining metrics

## Configuration Monitoring & Drift Detection

[Organization] continuously monitors configurations and detects unauthorized changes.

**2.4.1 Continuous Monitoring**

**Coverage Targets**:

| Tier | Coverage Target | Frequency | Acceptable Gap |
|------|----------------|-----------|----------------|
| **Tier 1 (Critical)** | 100% | Real-time or hourly | 0% |
| **Tier 2 (High)** | ≥95% | Daily | <5% |
| **Tier 3 (Medium)** | ≥85% | Weekly | <15% |
| **Tier 4 (Low)** | ≥70% | Monthly | <30% |

**Monitoring Capabilities**:

Monitoring tools MUST:

- Be deployed for Tier 1 and Tier 2 assets
- Compare actual configuration against approved baseline
- Generate alerts for configuration deviations
- Retain results for audit (minimum 90 days)

Monitoring SHOULD:

- Be automated (agent-based or agentless)
- Cover OS settings, applications, network devices, security tools
- Integrate with SIEM for centralized alerting
- Align frequency with asset criticality

**Tool Selection**: [Organization] selects tools based on technical environment and risk assessment; tools MUST support baseline comparison and drift detection

**2.4.1.1 Monitoring Tool Implementation Status**

[Organization] has implemented configuration monitoring for:
- **Tier 1 Assets**: Target 100% coverage with real-time or hourly monitoring
- **Tier 2 Assets**: Target ≥95% coverage with daily monitoring

**Coverage Gaps**: Asset types not yet under automated monitoring SHALL be documented with:
- Planned deployment date
- Interim controls (manual quarterly audits)
- Risk acceptance by CISO (documented in Risk Register)

**Operational Metrics**: Monitoring deployment status and alert volume SHALL be reported monthly to Configuration Manager and quarterly to CISO.

**2.4.2 Drift Detection and Alerting**

**Drift Classification**:

| Severity | Definition | Response SLA | Example |
|----------|------------|--------------|---------|
| **Critical** | Security control disabled | <1 hour | Firewall disabled, unauthorized admin account, encryption off |
| **High** | Security-relevant change | <4 hours | Password policy weakened, logging disabled, unauthorized service |
| **Medium** | Non-security drift | <24 hours | Service port changed, non-critical setting, documentation mismatch |
| **Low** | Informational drift | <5 business days | Cosmetic changes, non-functional settings |

**Alerting Requirements**:

Critical drift MUST:

- Trigger immediate SOC alert
- Include: asset ID, detected change, baseline expected value, actual value, timestamp
- Be tracked until resolution

Alert routing:

- Critical/High: SOC + Configuration Manager + System Owner
- Medium: Configuration Manager + System Owner
- Low: Configuration Manager (daily consolidated report)

**2.4.3 Drift Remediation**

**Remediation Workflow**:
1. **Detection**: Automated monitoring detects drift
2. **Triage**: Configuration Manager investigates cause
3. **Classification**: Authorized, unauthorized, or false positive
4. **Action**:

   - Authorized: Update baseline, close incident
   - Unauthorized: Remediate to baseline, investigate root cause, close incident
   - False positive: Tune monitoring, close incident

**Remediation Timeline**:

| Severity | Remediation SLA | Escalation |
|----------|----------------|------------|
| **Critical** | <4 hours | Escalate to CISO if not resolved |
| **High** | <24 hours | Escalate to Configuration Manager |
| **Medium** | <5 business days | Escalate to IT Operations Manager |
| **Low** | <30 days | Best effort |

**Tracking**: All drift incidents logged in incident management, tracked until closure, recurring drift triggers root cause analysis, trends analyzed monthly

**2.4.3.1 Drift Remediation Escalation Authority**

If drift remediation SLA is not met:

**Step 1**: Configuration Manager escalates to System Owner's manager
**Step 2**: If still unresolved after 48 hours, CISO reviews and may:
- **Option A**: Grant exception with compensating controls (maximum 30 days)
- **Option B**: Invoke emergency change to force remediation
- **Option C**: Isolate non-compliant system from production (if risk unacceptable)

**Final Authority**: CISO has authority to remove systems from production for unresolved Critical drift that creates unacceptable risk.

**Documentation**: All escalations and resolutions documented in drift incident record.

## Security Hardening & Compliance

[Organization] applies industry-standard security hardening and maintains compliance.

**2.5.1 Hardening Standard Selection**

**Selection Criteria**: Asset type/technology, regulatory requirements (per ISMS-POL-00), industry best practices, organizational risk appetite, operational feasibility

**Recognized Standards** (Examples):

| Standard | Provider | Usage |
|----------|----------|-------|
| **CIS Benchmarks** | Center for Internet Security | Primary reference for common platforms |
| **DISA STIGs** | Defense Information Systems Agency | High-security, government/defense |
| **Vendor Guides** | Microsoft, AWS, Azure, GCP, etc. | Cloud and vendor platforms |
| **NIST Baselines** | NIST SP 800-53, 800-128 | Framework alignment |

**Prioritization**: Regulatory-mandated → Industry-specific → CIS Benchmarks → Vendor guides → Custom standards

**2.5.2 Hardening Implementation**

**Implementation Requirements**:

All production assets SHALL:

- Be hardened per applicable standards before production deployment
- Implement critical security controls at ≥95% compliance
- Have hardening verified before production placement
- Document and risk-assess hardening gaps

Hardening SHOULD:

- Be automated (golden images, IaC, configuration management tools)
- Be validated in non-production first
- Be re-verified after significant changes

**Coverage Targets**:

| Tier | Critical Controls | Overall Compliance | Acceptable Gaps |
|------|-------------------|--------------------|--------------------|
| **Tier 1** | 100% | ≥95% | 0 critical gaps |
| **Tier 2** | ≥95% | ≥90% | <5 critical gaps |
| **Tier 3** | ≥90% | ≥80% | <10 critical gaps |
| **Tier 4** | ≥80% | ≥70% | Best effort |

**Critical Controls**: Defined per standard (authentication, encryption, logging, access control, patch management)

**2.5.3 Compliance Verification**

**Verification Requirements**:

Hardening compliance SHALL:

- Be assessed at least annually for all production systems
- Use automated scanning tools where available
- Document compliance rate per standard
- Identify gaps and recommend remediation

**Automated Scanning Frequency**:

| Asset Tier | Scan Frequency | Manual Verification (if automation unavailable) |
|------------|----------------|------------------------------------------------|
| **Tier 1 (Critical)** | Quarterly (automated) | Semi-annually (manual) |
| **Tier 2 (High)** | Semi-annually (automated) | Annually (manual) |
| **Tier 3/4 (Medium/Low)** | Annually (automated) | Annually (manual) |

**Implementation Status**: As of policy version date, automated scanning coverage and any interim manual assessments SHALL be documented in ISMS-IMP-A.8.9.4

**Verification Tools**: OpenSCAP, Nessus, Qualys, Tenable, cloud-native tools, vendor assessment tools

**Compliance Reporting**: Reports SHALL show overall compliance %, critical gaps, high-risk gaps, remediation recommendations; retained for audit (minimum 3 years)

**2.5.4 Gap Remediation**

**Remediation Prioritization**:

| Gap Risk | Timeline | Exception Approval Authority |
|----------|----------|------------------------------|
| **Critical** | <30 days | CISO only |
| **High** | <90 days | Configuration Manager + Security Architect |
| **Medium** | <180 days | Configuration Manager |
| **Low** | Best effort | Configuration Manager |

**Remediation Process**: Gap identification → Risk assessment → Remediation planning → Implementation → Verification → Exception management (if not feasible)

**Tracking**: All gaps in remediation register, assigned to System Owner with timeline, status reported monthly to CISO, overdue triggers escalation

---

# Roles and Responsibilities

[Organization] defines clear accountability for configuration management.

**3.1 RACI Matrix**

| Activity | CISO | CIO/CTO | Config Mgr | Sec Architect | Sys Owner | Sys Admin | CAB | Auditor |
|----------|------|---------|------------|---------------|-----------|-----------|-----|---------|
| **Policy approval** | A | C | R | C | I | I | I | I |
| **Baseline definition** | C | I | A | R | C | R | I | I |
| **Baseline approval** | A | C | R | R | C | I | I | I |
| **Change approval (Normal)** | I | I | A | C | C | R | R | I |
| **Change implementation** | I | I | C | I | A | R | I | I |
| **Monitoring configuration** | C | I | A | R | C | R | I | I |
| **Drift remediation** | I | I | C | C | A | R | I | I |
| **Hardening implementation** | C | I | C | A | C | R | I | I |
| **Compliance assessment** | A | C | R | R | C | C | I | R |
| **Audit support** | C | I | R | C | C | C | I | A |

**Legend**: R = Responsible, A = Accountable, C = Consulted, I = Informed

**3.2 Role Descriptions**

**Chief Information Security Officer (CISO)**:

- **Accountable** for configuration management policy and program
- Approves baselines, hardening standards, and exceptions
- Reviews compliance metrics and authorizes remediation priorities
- Final escalation point for configuration incidents

**Chief Information Officer (CIO) / Chief Technology Officer (CTO)**:

- **Consulted** on policy and baseline decisions
- Approves Emergency Changes
- Provides resources for configuration management program
- Reviews change success metrics

**Configuration Manager**:

- **Accountable** for day-to-day configuration management operations
- Chairs CAB
- Manages baseline repository and version control
- Coordinates monitoring and remediation activities
- Reports metrics to CISO/CIO

**Security Architect**:

- **Responsible** for hardening standard selection
- Reviews baselines for security compliance
- Defines security requirements for configurations
- Validates security controls in changes

**System Owner**:

- **Accountable** for configuration compliance of owned systems
- Approves changes affecting owned systems
- Ensures timely drift remediation
- Provides resources for hardening implementation

**System Administrator / DevOps Engineer**:

- **Responsible** for implementing baselines and changes
- Performs configuration monitoring setup
- Executes approved changes
- Triages drift alerts
- Documents configuration state

**Change Advisory Board (CAB)**:

- **Accountable** for change approval decisions
- Reviews Normal Changes for impact and risk
- Validates testing and rollback plans
- Conducts post-implementation reviews

**Internal/External Auditor**:

- **Responsible** for independent verification
- Audits compliance with policy
- Reviews evidence and documentation
- Reports findings to management

---

# Policy Governance

**4.1 Policy Lifecycle**

**Review Schedule**: Annual review (minimum); triggered reviews for regulatory changes, security incidents, technology changes

**Review Process**: Configuration Manager coordinates, subject matter experts provide input, CISO approves updates, Executive Management ratifies major changes

**Version Control**: All policy versions retained for **3 years**; change history documented; stakeholders notified of updates

**4.2 Exception Management**

**Exception Request Process**:

Exceptions to configuration requirements SHALL:

- Be requested in writing with business justification
- Include risk assessment and compensating controls
- Be reviewed by Security Architect
- Be approved by appropriate authority (per Section 2.5.4)
- Have defined expiration date (maximum 12 months)
- Be reviewed annually for renewal or revocation

**Exception Tracking**: All exceptions in exception register, reviewed quarterly, expired exceptions trigger remediation or renewal

**4.3 Compliance Measurement**

**Compliance Metrics**:

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| **Baseline Coverage** | ≥90% of asset types | Monthly | Configuration Manager |
| **Change Success Rate** | ≥95% | Monthly | CAB Chair |
| **Emergency Change Rate** | <10% of all changes | Monthly | CAB Chair |
| **CAB Meeting Compliance** | 100% documented | Monthly | CAB Chair |
| **Drift Remediation SLA** | ≥90% within SLA | Monthly | Configuration Manager |
| **Hardening Compliance** | ≥90% critical controls | Quarterly | Security Architect |
| **CAB Attendance** | ≥80% core members | Monthly | CAB Chair |
| **Exception Review Compliance** | 100% reviewed annually | Quarterly | Configuration Manager |
| **Failed Change RCA Completion** | 100% | Monthly | CAB Chair |

**Note**: All changes requiring rollback SHALL have root cause analysis completed within 10 business days, presented to CAB, and remediation actions tracked.

**Reporting**: Metrics dashboard reviewed monthly by CISO, quarterly by Executive Management

**4.4 Non-Compliance Consequences**

**Progressive Enforcement**:

- **First Violation**: Warning and corrective action plan
- **Repeated Violations**: Management escalation and performance review
- **Severe Violations**: Disciplinary action per HR policy
- **Systemic Non-Compliance**: Program audit and process improvement

**Severe Violations**: Unauthorized changes to Tier 1 systems, disabling security controls, bypassing change control, concealing configuration drift

**4.5 Continuous Improvement**

**Improvement Sources**:

- Incident lessons learned
- Change trend analysis
- Audit findings
- Industry best practices
- Technology evolution

**Improvement Process**: Identify opportunities, assess feasibility, pilot changes, implement improvements, measure effectiveness

---

# Definitions

**Baseline Configuration**: Documented set of security and operational configuration parameters for an asset type, serving as reference for deployment and compliance verification.

**Change Advisory Board (CAB)**: Cross-functional team responsible for assessing, approving, and reviewing configuration changes to minimize risk and ensure coordination.

**Change Success Rate**: Percentage of implemented changes that achieve intended outcome without requiring rollback, used to measure change process effectiveness.

**Configuration Drift**: Deviation of actual system configuration from approved baseline, potentially indicating unauthorized changes or baseline documentation gaps.

**Configuration Item (CI)**: Asset, service, or component managed through configuration management, tracked in CMDB with defined attributes and relationships.

**Configuration Management Database (CMDB)**: Repository storing configuration baselines, golden images, asset configurations, change history, and relationships between CIs.

**Emergency Change**: Urgent configuration change required to resolve critical security incident, service outage, or vulnerability, following expedited approval process with retrospective review.

**Golden Image**: Pre-configured system image implementing approved baseline configuration, used for rapid consistent deployment of new systems.

**Hardening**: Process of securing system configurations by implementing recognized security standards (CIS Benchmarks, DISA STIGs) and removing unnecessary services, accounts, and features.

**Infrastructure as Code (IaC)**: Practice of managing configuration baselines and infrastructure provisioning through machine-readable code stored in version control systems.

**Normal Change**: Configuration change requiring individual assessment and CAB approval, following standard change control process with testing and rollback planning.

**Rollback**: Process of reversing configuration change to restore system to pre-change state, executed when change fails validation criteria or introduces unacceptable risk.

**Standard Change**: Pre-approved, low-risk, repeatable configuration change following documented procedure, executable without individual CAB review.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Technology Officer (CTO)** | [Name] | [Date] |
| **Configuration Manager** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.9 (UG/TG). Technical reference information is provided in ISMS-CTX-A.8.9 (NOT ISMS).*

<!-- QA_VERIFIED: 2026-02-02 -->