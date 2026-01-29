# ISMS-POL-A.8.9-S2
## Configuration Management - Requirements Overview

**Document ID**: ISMS-POL-A.8.9-S2  
**Title**: Configuration Management - Requirements Overview  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Information Security Manager | Initial requirements overview |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: 07.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operations Review: Chief Technology Officer (CTO) / Configuration Manager
- Compliance Review: Information Security Manager

**Distribution**: All personnel responsible for configuration management implementation  
**Related Documents**: ISMS-POL-A.8.9 (Master), ISMS-POL-A.8.9-S1 (Definitions), Sections S2.1 through S2.4 (Detailed Requirements)

---

## 2.1 Overview

This document provides a high-level overview of the configuration management requirements framework. Detailed requirements are specified in subsections S2.1 through S2.4.

**Framework Philosophy**: Configuration management is not about creating perfect documentation that nobody reads. It's about having **usable baselines** that operations teams actually follow, **change controls** that prevent chaos without bureaucracy, **monitoring** that detects drift before it becomes an incident, and **hardening** that reduces attack surface based on evidence, not hope.

**The Cargo Cult Warning**: If your configuration management consists of outdated Word documents, manual change requests that take 3 weeks, and "drift detection" that means noticing when things break – you have configuration management theater, not actual control.

---

## 2.2 Four-Domain Framework

Configuration management is organized into **four complementary domains**. Each domain has:
- Policy requirements (this framework)
- Implementation assessment specification (markdown document)
- Python-generated Excel workbook (for stakeholder assessment)
- Evidence register (100 rows minimum per domain)
- Three-tier approval workflow (Preparer → Reviewer → Approver)

### 2.2.1 Domain 1: Baseline Configuration Management

**Control Objective**: Establish, document, and maintain secure baseline configurations for all asset types.

**Key Activities**:
- Define configuration baselines for each asset type
- Create and manage golden images
- Maintain configuration parameter standards
- Document configurations in CMDB or equivalent
- Manage Infrastructure as Code (IaC) repositories
- Track baseline coverage across asset inventory

**Success Metrics**:
- **Baseline Coverage %**: Percentage of assets with defined baselines
- **Golden Image Availability**: Availability of pre-approved images for rapid deployment
- **Documentation Currency**: Baseline review frequency and last update dates
- **IaC Adoption**: Percentage of infrastructure managed through code

**Detailed Requirements**: ISMS-POL-A.8.9-S2.1  
**Implementation Assessment**: ISMS-IMP-A.8.9.1  
**Excel Workbook**: ISMS-IMP-A.8.9.1_Baseline_Configuration_YYYYMMDD.xlsx

### 2.2.2 Domain 2: Change Control & Configuration Updates

**Control Objective**: Ensure all configuration changes follow approved processes with proper authorization, testing, and documentation.

**Key Activities**:
- Classify changes (standard, normal, emergency)
- Operate Change Advisory Board (CAB)
- Execute approval workflows
- Perform risk and impact assessments
- Implement changes within approved windows
- Test and validate post-implementation
- Execute rollback procedures when needed
- Track change statistics and success rates

**Success Metrics**:
- **Change Success Rate**: Percentage of changes not requiring rollback (target ≥95%)
- **Emergency Change %**: Percentage of emergency changes (target <10%)
- **Rollback Frequency**: Number of changes requiring rollback
- **CAB Effectiveness**: Average approval time, meeting attendance

**Detailed Requirements**: ISMS-POL-A.8.9-S2.2  
**Implementation Assessment**: ISMS-IMP-A.8.9.2  
**Excel Workbook**: ISMS-IMP-A.8.9.2_Change_Control_YYYYMMDD.xlsx

### 2.2.3 Domain 3: Configuration Monitoring & Drift Detection

**Control Objective**: Continuously monitor configurations, detect unauthorized changes, and alert on configuration drift from approved baselines.

**Key Activities**:
- Deploy configuration monitoring tools
- Implement drift detection capabilities
- Configure alerting thresholds
- Track drift incidents
- Execute remediation procedures
- Generate compliance reports
- Integrate with SIEM and incident response

**Success Metrics**:
- **Monitoring Coverage %**: Percentage of assets under continuous monitoring
- **Mean Time to Detect (MTTD)**: Average time to detect drift
- **Mean Time to Remediate (MTTR)**: Average time to restore baseline
- **Alert Accuracy**: True positive vs. false positive ratio
- **SLA Compliance**: Percentage of incidents meeting remediation SLAs

**Detailed Requirements**: ISMS-POL-A.8.9-S2.3  
**Implementation Assessment**: ISMS-IMP-A.8.9.3  
**Excel Workbook**: ISMS-IMP-A.8.9.3_Configuration_Monitoring_YYYYMMDD.xlsx

### 2.2.4 Domain 4: Security Hardening & Compliance

**Control Objective**: Apply industry-standard security hardening configurations and maintain compliance with security benchmarks.

**Key Activities**:
- Select and adopt hardening frameworks (CIS, STIG, vendor guides)
- Apply OS and application hardening
- Configure network device security
- Implement cloud service security
- Validate hardening through scanning
- Perform gap analysis
- Execute remediation plans
- Integrate with vulnerability management

**Success Metrics**:
- **Hardening Compliance %**: Average compliance with selected standards
- **Framework Adoption**: Percentage of asset types with hardening standards
- **Critical Gap Count**: Number of critical hardening gaps outstanding
- **Scan Coverage**: Percentage of assets scanned for hardening compliance
- **Remediation Rate**: Speed of gap closure

**Detailed Requirements**: ISMS-POL-A.8.9-S2.4  
**Implementation Assessment**: ISMS-IMP-A.8.9.4  
**Excel Workbook**: ISMS-IMP-A.8.9.4_Security_Hardening_YYYYMMDD.xlsx

---

## 2.3 Domain Integration

The four domains are **interdependent and mutually reinforcing**:

```
┌─────────────────────────────────────────────────────────────┐
│ Domain 1: Baseline Configuration Management                 │
│ • Defines WHAT configurations should be                      │
│ • Provides reference point for other domains                 │
└────────────┬────────────────────────────────────────────────┘
             │
             ├─────────────────────────────────────────────────┐
             │                                                 │
┌────────────▼──────────────┐      ┌──────────────────────────▼──┐
│ Domain 2: Change Control  │      │ Domain 4: Security Hardening │
│ • Controls HOW configs    │      │ • Defines SECURE configs     │
│   can change               │      │ • Validates security posture │
└────────────┬──────────────┘      └──────────────┬──────────────┘
             │                                     │
             └──────────┬──────────────────────────┘
                        │
           ┌────────────▼────────────────────┐
           │ Domain 3: Monitoring & Drift    │
           │ • Detects WHEN configs change   │
           │ • Validates compliance          │
           └─────────────────────────────────┘
```

**Example Workflow**:
1. **Domain 1**: Windows Server 2022 baseline defined (hardened per CIS Level 1)
2. **Domain 4**: Baseline includes CIS hardening controls
3. **Domain 2**: Change request to modify firewall rules → CAB approval → implementation
4. **Domain 3**: Monitoring detects configuration change → validates against approved change → no alert (authorized)
5. **Domain 3**: Monitoring detects unauthorized service start → alerts SOC → incident investigation
6. **Domain 2**: Emergency change to disable vulnerable service → retrospective CAB review
7. **Domain 1**: Baseline updated to reflect new security configuration

---

## 2.4 Compliance vs. Maturity

### 2.4.1 Compliance Perspective

**ISO 27001 Audit Question**: *"Does the organization have configuration management controls?"*

**Compliance Evidence**:
- [ ] Policy framework exists and is approved
- [ ] Baselines are defined for critical asset types
- [ ] Change management process is documented and followed
- [ ] Configuration monitoring is implemented
- [ ] Hardening standards are applied to internet-facing systems
- [ ] Evidence of periodic reviews and audits

**Minimum Compliance Threshold**:
- 60% baseline coverage for critical assets
- Documented change process with CAB
- Some form of drift detection (even if manual)
- Hardening applied to high-risk systems
- Quarterly self-assessment

**Reality Check**: Minimum compliance gets you through the audit. It doesn't prevent incidents.

### 2.4.2 Maturity Perspective

**Maturity Levels** (adapted from CMMI and NIST frameworks):

**Level 0 - Non-Existent**: No configuration management. "We'll figure it out when it breaks."  
**Level 1 - Initial/Ad Hoc**: Some documentation exists, inconsistently applied. Tribal knowledge dominates.  
**Level 2 - Repeatable**: Baselines defined for major asset types. Manual change process. Reactive monitoring.  
**Level 3 - Defined**: Comprehensive baselines. Structured change process with CAB. Automated drift detection.  
**Level 4 - Managed**: Metrics-driven optimization. Proactive drift prevention. IaC adoption. Continuous compliance.  
**Level 5 - Optimizing**: Full automation. Self-healing configurations. AI-assisted anomaly detection. Zero-touch operations.

**Maturity Assessment**: Each implementation workbook includes maturity scoring. Executive dashboard aggregates overall maturity level.

**The Feynman Maturity Test**: *"Can you recover a critical server from nothing but your documentation in under 1 hour? If not, your documentation is fiction."*

---

## 2.5 Policy Applicability Matrix

Not all requirements apply equally to all asset types. This matrix provides guidance:

### 2.5.1 Applicability by Asset Criticality

| Requirement Category | Critical Assets | High Assets | Medium Assets | Low Assets |
|---------------------|----------------|-------------|---------------|-----------|
| Baseline Definition | MUST | MUST | SHOULD | MAY |
| Golden Image | SHOULD | SHOULD | MAY | MAY |
| Change CAB Approval | MUST | MUST | SHOULD | MAY |
| Automated Monitoring | MUST | SHOULD | SHOULD | MAY |
| Hardening Standards | MUST (CIS L2) | MUST (CIS L1) | SHOULD | MAY |
| Quarterly Review | MUST | SHOULD | SHOULD | MAY |

**Asset Criticality Definitions**:
- **Critical**: Business failure if unavailable >4 hours. Contains highly sensitive data. Internet-facing.
- **High**: Significant business impact if unavailable >24 hours. Contains sensitive data. Internal production.
- **Medium**: Moderate business impact. Standard business data. Internal non-production or support systems.
- **Low**: Minimal business impact. Public data. Development/test environments.

### 2.5.2 Applicability by Asset Type

| Requirement Category | Servers | Network | Endpoints | Cloud | Applications | IoT/OT |
|---------------------|---------|---------|-----------|-------|--------------|--------|
| OS Baseline | ✅ | ✅ | ✅ | ✅ | N/A | ✅* |
| App Baseline | N/A | N/A | N/A | ✅ | ✅ | N/A |
| Network Baseline | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Hardening Standards | ✅ | ✅ | ✅ | ✅ | ✅ | ✅* |
| Drift Detection | ✅ | ✅ | ✅** | ✅ | ✅ | ✅* |
| IaC Eligibility | ✅ | ✅ | N/A | ✅ | ✅ | ✅* |

**Legend**:
- ✅ = Applicable
- ✅* = Applicable with OT-specific considerations (safety, availability priority)
- ✅** = Applicable but may use endpoint management tools (SCCM, Intune, etc.)
- N/A = Not Applicable to this asset type

### 2.5.3 Requirement Prioritization

**Immediate Priority** (first 90 days):
- Baseline definition for critical assets
- Change control process documentation
- Asset inventory in CMDB
- Hardening for internet-facing systems

**Short-Term Priority** (90-180 days):
- Automated drift detection for critical assets
- Golden image creation for standard builds
- CAB establishment and workflow implementation
- Hardening compliance scanning

**Medium-Term Priority** (180-365 days):
- Baseline expansion to high-priority assets
- IaC adoption for infrastructure
- Comprehensive monitoring deployment
- Quarterly compliance reporting

**Long-Term Priority** (ongoing):
- Maturity advancement (automation, optimization)
- Coverage expansion to medium/low-priority assets
- Process refinement based on metrics
- Continuous improvement initiatives

---

## 2.6 Exception Management Philosophy

### 2.6.1 When Exceptions Are Appropriate

**Technical Limitations**:
- Legacy system cannot support current hardening standards
- Third-party application requires non-standard configuration
- Hardware/software incompatibility with baseline

**Business Justification**:
- Operational requirement conflicts with security baseline
- Cost of compliance exceeds risk
- Temporary exception during migration/transition

**Risk-Accepted Scenarios**:
- Known gap with documented compensating controls
- Residual risk accepted by senior management
- Exception documented with remediation timeline

### 2.6.2 When Exceptions Are NOT Appropriate

**Invalid Justifications**:
- "Too much work" → This is a resourcing issue, not an exception
- "We've always done it this way" → Inertia is not risk management
- "The vendor says it's secure" → Verify, don't trust
- "Nobody will attack this" → Threat modeling is required, not assumptions

**Exception Process**: See ISMS-POL-A.8.9-S5.C (Configuration Deviation Procedures)

### 2.6.3 Compensating Controls

When standard configurations cannot be applied, compensating controls MUST provide equivalent protection:

**Example Scenarios**:

**Scenario 1**: Legacy application requires administrative privileges  
**Standard Control**: Least-privilege execution  
**Compensating Controls**:
- Application whitelisting to prevent unauthorized code
- Enhanced monitoring and alerting on privileged actions
- Isolated network segment with restricted access
- Frequent security audits

**Scenario 2**: Database requires outdated protocol for vendor integration  
**Standard Control**: Modern encryption protocols (TLS 1.3)  
**Compensating Controls**:
- VPN tunnel or encrypted network link
- Network segmentation isolating legacy traffic
- IDS/IPS monitoring for exploitation attempts
- Documented plan to migrate vendor integration within 12 months

**Compensating Control Validation**: Documented, risk-assessed, approved by CISO, reviewed quarterly.

---

## 2.7 Relationship Between Domains

### 2.7.1 Domain Dependencies

**Sequential Dependencies** (must be completed in order):
1. Domain 1 (Baselines) must be defined before:
   - Domain 2 can control changes to baselines
   - Domain 3 can detect drift from baselines
   - Domain 4 can validate hardening compliance

**Parallel Implementation** (can proceed simultaneously):
- Domain 2 (Change Control) and Domain 3 (Monitoring) are independent
- Domain 4 (Hardening) can inform Domain 1 (Baselines) iteratively

**Continuous Feedback Loops**:
- Domain 3 drift incidents trigger Domain 2 change reviews
- Domain 4 hardening gaps update Domain 1 baselines
- Domain 2 change failures improve Domain 1 baseline quality

### 2.7.2 Workflow Example: Server Deployment

**Step 1 (Domain 1)**: Select "Windows Server 2022 - Application Server" baseline  
**Step 2 (Domain 4)**: Baseline includes CIS Level 1 hardening  
**Step 3 (Domain 1)**: Deploy golden image based on baseline  
**Step 4 (Domain 2)**: Record deployment as approved change in change management system  
**Step 5 (Domain 3)**: Enable automated monitoring and drift detection  
**Step 6 (Domain 3)**: First baseline scan validates compliance  
**Step 7 (Domain 4)**: Weekly hardening scans ensure continued compliance  
**Step 8 (Domain 2)**: Future configuration changes require CAB approval  
**Step 9 (Domain 3)**: Monitoring alerts on any unauthorized drift  

---

## 2.8 Metrics & Key Performance Indicators

Each domain tracks specific KPIs. The executive dashboard (ISMS-IMP-A.8.9.5) aggregates across domains.

**Domain 1 (Baselines)**:
- Baseline Coverage % (target: 100% for critical, 80% overall)
- Golden Image Availability (target: 100% for standard builds)
- Baseline Age (target: reviewed within 180 days)

**Domain 2 (Change Control)**:
- Change Success Rate (target: ≥95%)
- Emergency Change % (target: <10% of total)
- Rollback Rate (target: <5%)
- Average Approval Time (target: <5 business days for normal changes)

**Domain 3 (Monitoring)**:
- Monitoring Coverage % (target: 100% for critical, 80% overall)
- Mean Time to Detect - MTTD (target: <24 hours)
- Mean Time to Remediate - MTTR (target: <72 hours for critical)
- False Positive Rate (target: <10%)

**Domain 4 (Hardening)**:
- Average Hardening Compliance % (target: ≥90%)
- Critical Gap Count (target: 0 critical gaps outstanding >30 days)
- Scan Coverage (target: 100% for critical assets)

**Overall Maturity Score**: Weighted average across all domains (0-100%)

---

## 2.9 Implementation Roadmap

**Week 1-4: Foundation**
- Review policy framework
- Conduct asset inventory
- Classify asset criticality
- Identify existing baselines

**Week 5-8: Domain 1 Baseline**
- Define baselines for critical asset types
- Create initial golden images
- Document in CMDB
- Generate Domain 1 assessment workbook

**Week 9-12: Domain 2 Change Control**
- Document change process
- Establish CAB membership
- Define change categories
- Generate Domain 2 assessment workbook

**Week 13-16: Domain 3 Monitoring**
- Deploy monitoring tools
- Configure drift detection
- Test alerting workflows
- Generate Domain 3 assessment workbook

**Week 17-20: Domain 4 Hardening**
- Select hardening standards
- Perform initial scans
- Conduct gap analysis
- Generate Domain 4 assessment workbook

**Week 21-24: Integration & Optimization**
- Complete all evidence registers
- Obtain three-tier approvals
- Generate executive dashboard
- Conduct lessons learned
- Plan quarterly reassessment

---

**END OF DOCUMENT**