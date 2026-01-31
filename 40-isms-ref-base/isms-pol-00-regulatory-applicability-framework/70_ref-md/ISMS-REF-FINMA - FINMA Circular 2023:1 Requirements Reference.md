**ISMS-REF-FINMA — FINMA Circular 2023/1 Requirements Reference**
**Swiss Financial Institution Information Security Requirements (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | FINMA Circular 2023/1 Requirements Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-FINMA |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | CISO (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Legal/Compliance | Initial technical reference for Swiss financial institutions |

**Review Cycle**: Annual (or upon FINMA circular updates)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Legal/Compliance / CISO (technical reference, no ISMS approval required)

**Distribution**: Compliance team, CISO, Legal counsel (for organizations subject to FINMA supervision)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory requirements unless [Organization] is a FINMA-regulated entity.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs for non-regulated entities.
- This document does NOT mandate the adoption of FINMA requirements for organizations not subject to FINMA supervision.
- This document does NOT override or extend any ISMS policy.


**Applicability Determination**:
FINMA requirements apply ONLY IF [Organization]:

- Holds a FINMA license (bank, securities dealer, insurance, fund management, payment services)
- Is subject to FINMA supervision
- Operates as a Swiss financial institution


For all other organizations, this document serves solely as:

- Technical reference for potential FINMA requirements
- Context for service provider relationships with Swiss financial institutions
- Awareness of Swiss financial sector security standards
- **This document must not be used as audit evidence unless [Organization] is FINMA-regulated**


Use of this document does not imply FINMA applicability, compliance obligations, or regulatory status.

**Critical Positioning Statement**:
This document intentionally provides regulatory detail beyond what applies to most organizations. Its purpose is awareness only for organizations that MAY become subject to FINMA supervision, or that provide services to FINMA-regulated entities. No auditor conclusions shall be drawn from the presence, absence, or implementation status of any FINMA requirement listed herein unless [Organization] is explicitly FINMA-regulated.

---

# Document Purpose and Scope

## Purpose

This document provides a technical overview of Swiss Financial Market Supervisory Authority (FINMA) information security requirements as defined in FINMA Circular 2023/1 "Operational risks and resilience - banks" (effective June 1, 2024). It is intended to support:

- Awareness of FINMA requirements for Swiss financial institutions
- Understanding of FINMA margin structure and key requirements
- Context for organizations providing services to Swiss financial institutions
- Potential future applicability assessment
- Mapping FINMA requirements to ISO 27001:2022 controls


## What This Document Is NOT

This document does NOT:

- Establish mandatory requirements for non-FINMA-regulated organizations
- Define [Organization]'s compliance obligations (see POL-00 for regulatory applicability)
- Create audit criteria unless [Organization] is FINMA-regulated
- Replace legal or compliance counsel interpretation
- Constitute legal advice on FINMA compliance
- Establish implementation procedures or verification processes


## Relationship to ISMS

This document is a **non-binding technical reference** UNLESS [Organization] is subject to FINMA supervision (as determined in ISMS-POL-00 Section 3.1).

**If [Organization] IS FINMA-regulated:**

- FINMA requirements become Tier 1 (Mandatory Compliance) per POL-00
- This document provides implementation guidance
- ISMS controls must demonstrate FINMA compliance
- Annual FINMA compliance attestation required


**If [Organization] IS NOT FINMA-regulated:**

- FINMA remains Tier 3 (Informational Reference) per POL-00
- This document is for awareness only
- No FINMA compliance obligations exist
- ISMS controls follow ISO 27001:2022 only


## Content Organization

This reference organizes FINMA requirements by:

- FINMA Circular 2023/1 margin structure
- Information security requirements (Margins 50-62)
- Logging and monitoring requirements (Margins 63-72)
- Business continuity requirements (Margins 73-87)
- Outsourcing requirements (FINMA 2008/7 and 2018/3)
- Mapping to ISO 27001:2022 Annex A controls


---

# FINMA Overview and Applicability

## What is FINMA?

**Eidgenössische Finanzmarktaufsicht (FINMA)** is the Swiss Financial Market Supervisory Authority responsible for supervising banks, insurance companies, stock exchanges, securities dealers, and other financial intermediaries in Switzerland.

**Primary Legal Basis**:

- Financial Market Supervision Act (FINSA)
- Banking Act (BA)
- Insurance Supervision Act (ISA)
- Financial Institutions Act (FinIA)


**Enforcement Authority**:

- Licensing and authorization
- On-site examinations
- Off-site supervision
- Enforcement actions (fines, license revocation)
- Incident reporting requirements


## FINMA Circulars

**Circular Structure**:
FINMA issues "circulars" that provide binding minimum standards for supervised institutions. Key circulars for information security:

**FINMA Circular 2023/1** - Operational risks and resilience (banks):

- Effective: June 1, 2024
- Applies to: Banks and securities dealers
- Scope: Operational risk management, business continuity, information security, outsourcing
- **Margin 50-62**: Information Security Requirements
- **Margin 63-72**: Logging and Monitoring Requirements
- **Margin 73-87**: Business Continuity and Resilience Requirements


**FINMA Circular 2008/7** - Outsourcing (banks):

- Risk management in outsourcing relationships
- Due diligence and contractual requirements
- Data protection and confidentiality
- Business continuity in outsourcing


**FINMA Circular 2018/3** - Outsourcing (insurers):

- Similar requirements adapted for insurance sector
- Supervisory authority notification requirements


## Applicability Determination

**FINMA applies to [Organization] IF**:

| Criteria | Status | Evidence |
|----------|--------|----------|
| Holds FINMA banking license | ⬜ Yes ⬜ No | [License number / N/A] |
| Holds FINMA securities dealer license | ⬜ Yes ⬜ No | [License number / N/A] |
| Holds FINMA insurance license | ⬜ Yes ⬜ No | [License number / N/A] |
| Holds FINMA fund management license | ⬜ Yes ⬜ No | [License number / N/A] |
| Holds FINMA payment services license | ⬜ Yes ⬜ No | [License number / N/A] |
| Subject to FINMA supervision | ⬜ Yes ⬜ No | [Supervisory determination] |

**If ANY "Yes"**: FINMA requirements are **Tier 1 (Mandatory Compliance)** per POL-00 Section 3.1

**If ALL "No"**: FINMA requirements remain **Tier 3 (Informational Reference)** per POL-00

**Service Provider Status**:
If [Organization] provides services TO FINMA-regulated entities:

- FINMA 2008/7 or 2018/3 outsourcing requirements may apply
- Customer contracts may impose FINMA-equivalent controls
- Right-to-audit clauses may require FINMA compliance demonstration
- Consider as contractual requirements (Tier 1 if contractually mandated)


---

# FINMA Circular 2023/1 - Information Security Requirements

## Overview (Margins 50-62)

FINMA Circular 2023/1 Margins 50-62 establish information security requirements for Swiss banks and securities dealers.

**Key Principle**:
Organizations must implement **risk-based** information security measures appropriate to:

- Nature and scope of business activities
- Complexity of IT systems
- Sensitivity of data processed
- Threat landscape and risk assessment


FINMA does NOT prescribe specific technical controls but requires "appropriate organizational and technical measures."

## Margin 50-55: Information Security Framework

**Margin 50: Information Security Strategy**

**Requirement**:
Banks must define and implement an information security strategy aligned with:

- Business strategy and risk appetite
- IT strategy and architecture
- Regulatory requirements
- Industry best practices


**ISO 27001:2022 Mapping**:

- Clause 5.2: Policy
- Clause 6.2: Information security objectives
- A.5.1: Policies for information security


**Implementation Considerations**:

- Board-level approval of information security strategy
- Annual review and update
- Integration with enterprise risk management
- Clear roles and responsibilities (CISO, IT management, business units)


---

**Margin 51: Information Security Organization**

**Requirement**:
Clear organizational structure for information security with:

- Defined roles and responsibilities
- Segregation of duties (development, operations, security)
- Independent security function with sufficient authority
- Escalation paths to senior management and board


**ISO 27001:2022 Mapping**:

- Clause 5.3: Organizational roles, responsibilities and authorities
- A.5.2: Information security roles and responsibilities


**Key Roles** (FINMA expectation):

- Chief Information Security Officer (CISO) or equivalent
- Information Security Committee
- System Owners
- Security Architects
- Security Operations Team


---

**Margin 52: Risk Assessment**

**Requirement**:
Regular information security risk assessments covering:

- Identification of information assets
- Threat and vulnerability assessment
- Risk evaluation and prioritization
- Risk treatment decisions
- Residual risk acceptance


**ISO 27001:2022 Mapping**:

- Clause 6.1.2: Information security risk assessment
- Clause 6.1.3: Information security risk treatment
- Clause 8.2: Information security risk assessment
- Clause 8.3: Information security risk treatment


**FINMA Expectations**:

- Annual risk assessment minimum
- Triggered assessments for major changes
- Board reporting on key risks
- Documentation of risk decisions


---

**Margin 53: Security Policies and Standards**

**Requirement**:
Comprehensive information security policies and standards covering:

- Information classification
- Access control
- Cryptography
- Physical security
- Incident management
- Business continuity


**ISO 27001:2022 Mapping**:

- A.5.1: Policies for information security
- A.5.10: Acceptable use of information and other associated assets
- A.5.12: Classification of information


**Documentation Requirements**:

- Policy hierarchy (strategy → policy → standards → procedures)
- Regular review and update
- Communication and awareness
- Management approval


---

**Margin 54: Security Awareness and Training**

**Requirement**:
Information security awareness and training program ensuring:

- All personnel understand security obligations
- Role-specific training for security responsibilities
- Regular awareness campaigns
- Testing and validation of awareness effectiveness


**ISO 27001:2022 Mapping**:

- A.6.3: Information security awareness, education and training


**FINMA Expectations**:

- Annual mandatory training for all personnel
- Specialized training for privileged users
- Phishing simulation and testing
- Training completion tracking and metrics


---

**Margin 55: Third-Party Risk Management**

**Requirement**:
Risk-based approach to third-party security including:

- Vendor security assessments
- Contractual security requirements
- Ongoing monitoring of supplier performance
- Right to audit and information access


**ISO 27001:2022 Mapping**:

- A.5.19: Information security in supplier relationships
- A.5.20: Addressing information security within supplier agreements
- A.5.21: Managing information security in the ICT supply chain


**FINMA-Specific**:

- FINMA Circular 2008/7 applies to outsourcing relationships
- Material outsourcing requires FINMA notification
- Exit strategies and transition planning mandatory


---

## Margin 56: Authentication and Access Control

**Requirement**:
Implement strong authentication and access control mechanisms:

- User identification and authentication
- Unique user accounts (no shared accounts)
- Multi-factor authentication for critical systems
- Least privilege access
- Regular access reviews


**Specific Requirements**:

**Authentication**:

- Strong authentication for all users
- Multi-factor authentication (MFA) for:
  - Remote access
  - Privileged accounts
  - Access to sensitive data
- Password complexity and rotation policies
- Account lockout after failed attempts


**Access Control**:

- Role-based access control (RBAC)
- Principle of least privilege
- Regular access certification (at least annually)
- Automated provisioning and de-provisioning
- Privileged access management (PAM) for administrators


**ISO 27001:2022 Mapping**:

- A.5.15: Access control
- A.5.16: Identity management
- A.5.17: Authentication information
- A.5.18: Access rights
- A.8.2: Privileged access rights
- A.8.3: Information access restriction
- A.8.5: Secure authentication


**Implementation Guidance**:

- Identity and Access Management (IAM) platform
- Single Sign-On (SSO) with MFA
- Privileged Access Management (PAM) solution
- Automated access reviews and recertification
- Joiners/Movers/Leavers (JML) process automation


---

## Margin 58: Segregation of Duties

**Requirement**:
Define and implement segregation of duties to prevent conflicts of interest and reduce fraud risk:

- Identify critical business processes requiring SoD
- Define incompatible roles and activities
- Implement controls to prevent SoD violations
- Monitor and detect SoD conflicts
- Compensating controls where SoD not feasible


**Critical Segregation Examples**:

- Development vs. Production access
- Change initiator vs. Change approver
- Payment initiator vs. Payment approver
- Security administrator vs. System administrator
- Backup administrator vs. Restore requestor


**ISO 27001:2022 Mapping**:

- A.5.15: Access control (segregation of duties principle)
- A.5.18: Access rights (role-based separation)
- A.8.2: Privileged access rights (administrative separation)


**Implementation Approaches**:

- Role-based access control (RBAC) with SoD rules
- Automated SoD conflict detection (e.g., SAP GRC, Oracle GRC)
- Regular SoD violation reporting and remediation
- Compensating controls documentation (e.g., enhanced monitoring, dual authorization)


**FINMA Expectations**:

- SoD matrix documenting incompatible activities
- Automated SoD monitoring where possible
- Quarterly SoD violation reporting to management
- Board-level awareness of critical SoD gaps


---

## Margin 62: Encryption

**Requirement**:
Implement cryptography to protect sensitive data:

- Data encryption at rest and in transit
- Encryption key management
- Alignment with current encryption standards
- Regular cryptographic review


**Specific Requirements**:

**Data in Transit**:

- TLS 1.2 minimum (TLS 1.3 preferred)
- Strong cipher suites (no deprecated algorithms)
- Certificate management and rotation
- Secure protocols for all sensitive data transmission


**Data at Rest**:

- Full disk encryption for endpoints (laptops, mobile devices)
- Database encryption for sensitive data
- File/folder encryption for confidential documents
- Backup encryption


**Key Management**:

- Centralized key management system
- Separation of key management from data access
- Key rotation and lifecycle management
- Secure key storage (Hardware Security Module preferred)
- Key backup and recovery procedures


**Encryption Standards**:

- AES-256 for symmetric encryption
- RSA 2048-bit minimum or ECC 256-bit for asymmetric encryption
- SHA-256 minimum for hashing
- No use of deprecated algorithms (DES, 3DES, MD5, SHA-1)


**ISO 27001:2022 Mapping**:

- A.8.24: Use of cryptography


**Implementation Guidance**:

- Microsoft BitLocker / FileVault for endpoint encryption
- Azure Key Vault / AWS KMS for cloud key management
- Hardware Security Module (HSM) for high-value keys
- Certificate lifecycle management (Let's Encrypt, DigiCert, etc.)
- Regular cryptographic inventory and compliance scanning


---

## Margins 63-72: Logging and Monitoring

**Margin 63-65: Security Event Logging**

**Requirement**:
Comprehensive logging of security-relevant events:

- User authentication and authorization
- Privileged operations
- System changes and configurations
- Security incidents and alerts
- Data access (especially sensitive data)


**Log Content Requirements**:

- Who: User identification
- What: Action performed
- When: Timestamp (synchronized)
- Where: System/application/IP address
- Result: Success or failure


**Log Retention**:

- Security logs: 12 months minimum (FINMA expectation)
- Audit logs: 10 years (depending on data type)
- Backup logs for long-term retention


**ISO 27001:2022 Mapping**:

- A.8.15: Logging
- A.8.16: Monitoring activities


---

**Margin 66-68: Centralized Log Management**

**Requirement**:
Centralized collection, storage, and analysis of security logs:

- SIEM (Security Information and Event Management) or equivalent
- Real-time log collection from all critical systems
- Log integrity protection (immutable logs)
- Secure log storage with access controls


**SIEM Capabilities**:

- Log aggregation from multiple sources
- Correlation and analysis
- Alerting and notification
- Reporting and dashboards
- Integration with incident response


**ISO 27001:2022 Mapping**:

- A.8.15: Logging (centralized log management)
- A.8.16: Monitoring activities (SIEM correlation)


**Implementation Examples**:

- Splunk Enterprise Security
- Microsoft Sentinel (Azure)
- Elastic Security (ELK Stack)
- IBM QRadar
- LogRhythm


---

**Margin 69-72: Real-Time Monitoring and Alerting**

**Requirement**:
Continuous monitoring and real-time alerting for security events:

- 24/7 security monitoring (SOC or equivalent)
- Automated alerting for critical security events
- Defined escalation procedures
- Integration with incident response


**Alert Categories**:

- Critical: Immediate response required (within 15 minutes)
- High: Response within 1 hour
- Medium: Response within 4 hours
- Low: Response within 24 hours


**Monitored Events**:

- Failed authentication attempts (brute force)
- Privileged account usage
- Unauthorized access attempts
- Malware detection
- Data exfiltration indicators
- System configuration changes
- Security control failures


**ISO 27001:2022 Mapping**:

- A.8.16: Monitoring activities
- A.5.24: Information security incident management planning and preparation
- A.5.25: Assessment and decision on information security events


**Implementation Approaches**:

- Internal SOC (Security Operations Center)
- Managed Security Service Provider (MSSP)
- Co-managed SOC (hybrid model)


---

## Margins 73-87: Business Continuity and Resilience

**Overview**:
FINMA Circular 2023/1 Margins 73-87 establish comprehensive business continuity and disaster recovery requirements for Swiss financial institutions.

**Margin 73-75: Business Impact Analysis (BIA)**

**Requirement**:
Conduct regular Business Impact Analysis to:

- Identify critical business processes
- Define Recovery Time Objectives (RTO)
- Define Recovery Point Objectives (RPO)
- Assess financial and operational impact


**ISO 27001:2022 Mapping**:

- Clause 8.1: Operational planning and control (business continuity context)
- A.5.29: Information security during disruption
- A.5.30: ICT readiness for business continuity


**FINMA Expectations**:

- RTO for critical processes: typically 2-4 hours
- RPO for critical data: typically 15 minutes to 1 hour
- Annual BIA review and update
- Board approval of RTO/RPO targets


---

**Margin 76-80: Business Continuity Plans (BCP)**

**Requirement**:
Documented and tested business continuity plans including:

- Incident response procedures
- Crisis management structure
- Communication plans (internal and external)
- Alternate processing sites
- Data backup and recovery procedures


**Plan Components**:

- Roles and responsibilities (Crisis Management Team)
- Activation criteria and escalation
- Communication protocols (FINMA notification requirements)
- Recovery procedures (step-by-step)
- Vendor and supplier coordination
- Return to normal operations


**ISO 27001:2022 Mapping**:

- A.5.29: Information security during disruption
- A.5.30: ICT readiness for business continuity
- A.8.13: Information backup
- A.8.14: Redundancy of information processing facilities


---

**Margin 81-84: Testing and Validation**

**Requirement**:
Regular testing of business continuity and disaster recovery capabilities:

- Annual full-scale DR test (minimum)
- Partial tests quarterly or semi-annually
- Tabletop exercises
- Component testing (backup restoration, failover)


**Test Types**:

- **Tabletop Exercise**: Discussion-based, no system activation
- **Partial Test**: Test specific components (e.g., database failover)
- **Full DR Test**: Complete failover to alternate site
- **Surprise Test**: Unannounced activation to test readiness


**ISO 27001:2022 Mapping**:

- A.5.30: ICT readiness for business continuity (testing requirement)


**FINMA Expectations**:

- Annual full-scale DR test documented and reported
- Test results reviewed by board
- Identified gaps remediated within defined timeframe
- Third-party involvement tested (outsourcing partners)


---

**Margin 85-87: Incident Management and Reporting**

**Requirement**:
Formal incident management process including:

- Incident classification and severity levels
- Escalation procedures
- FINMA notification requirements
- Root cause analysis
- Lessons learned and continuous improvement


**FINMA Incident Reporting**:
Banks must notify FINMA of:

- **Immediately**: Major incidents affecting critical business processes
- **Within 24 hours**: Security breaches, data leaks, significant outages
- **Post-incident**: Detailed incident report within defined timeframe


**Reporting Content**:

- Incident description and timeline
- Impact assessment (customers, operations, financial)
- Root cause analysis
- Remediation actions taken
- Measures to prevent recurrence


**ISO 27001:2022 Mapping**:

- A.5.24: Information security incident management planning and preparation
- A.5.25: Assessment and decision on information security events
- A.5.26: Response to information security incidents
- A.5.27: Learning from information security incidents
- A.5.28: Collection of evidence


---

# FINMA Circular 2008/7 - Outsourcing (Banks)

## Overview

FINMA Circular 2008/7 establishes requirements for banks outsourcing business functions or IT services to third-party providers.

**Applicability**:

- Applies to banks and securities dealers
- Covers outsourcing of material functions
- Includes both domestic and cross-border outsourcing
- Cloud services are considered outsourcing


## Key Requirements

**Risk Assessment**:

- Comprehensive risk assessment before outsourcing
- Evaluation of service provider capabilities
- Assessment of concentration risk
- Data residency and sovereignty considerations


**Contractual Requirements**:

- Clear definition of services and SLAs
- Security and confidentiality obligations
- Right to audit and information access
- Subcontracting restrictions
- Data protection clauses
- Business continuity requirements
- Exit strategy and transition provisions


**Ongoing Monitoring**:

- Regular service provider performance reviews
- Periodic security assessments and audits
- Incident reporting requirements
- Annual compliance attestation (e.g., SOC 2 Type II)


**ISO 27001:2022 Mapping**:

- A.5.19: Information security in supplier relationships
- A.5.20: Addressing information security within supplier agreements
- A.5.21: Managing information security in the ICT supply chain
- A.5.22: Monitoring, review and change management of supplier services
- A.5.23: Information security for use of cloud services


---

# ISO 27001:2022 to FINMA Mapping

## Control Mapping Matrix

| FINMA Requirement | FINMA Margin | ISO 27001:2022 Control | Implementation Priority |
|-------------------|--------------|------------------------|-------------------------|
| Information Security Strategy | 50 | Clause 5.2, A.5.1 | Critical |
| Security Organization | 51 | Clause 5.3, A.5.2 | Critical |
| Risk Assessment | 52 | Clause 6.1.2, 6.1.3, 8.2, 8.3 | Critical |
| Security Policies | 53 | A.5.1, A.5.10, A.5.12 | Critical |
| Awareness and Training | 54 | A.6.3 | High |
| Third-Party Risk | 55 | A.5.19, A.5.20, A.5.21 | Critical |
| Authentication & Access Control | 56 | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 | Critical |
| Segregation of Duties | 58 | A.5.15, A.5.18, A.8.2 | Critical |
| Encryption | 62 | A.8.24 | Critical |
| Security Logging | 63-65 | A.8.15 | Critical |
| Centralized Log Management | 66-68 | A.8.15, A.8.16 | Critical |
| Monitoring and Alerting | 69-72 | A.8.16, A.5.24, A.5.25 | Critical |
| Business Impact Analysis | 73-75 | A.5.29, A.5.30 | Critical |
| Business Continuity Plans | 76-80 | A.5.29, A.5.30, A.8.13, A.8.14 | Critical |
| BC/DR Testing | 81-84 | A.5.30 | Critical |
| Incident Management | 85-87 | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 | Critical |
| Outsourcing (FINMA 2008/7) | N/A | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 | Critical |

## Gap Analysis Approach

For organizations subject to FINMA:

**Step 1**: Confirm FINMA applicability status
**Step 2**: Conduct ISO 27001:2022 compliance baseline assessment
**Step 3**: Identify FINMA-specific requirements beyond ISO 27001
**Step 4**: Document gaps and develop remediation plan
**Step 5**: Prioritize FINMA critical margins (56, 58, 62, 63-72)
**Step 6**: Implement controls with FINMA compliance evidence
**Step 7**: Conduct internal audit with FINMA focus
**Step 8**: Prepare for potential FINMA examination

## Compliance Evidence Requirements

FINMA expects documented evidence of:

- Policies and procedures approved by management
- Risk assessments and treatment decisions
- Access control configurations and reviews
- Log retention and monitoring capabilities
- BC/DR test results and remediation actions
- Incident reports and lessons learned
- Third-party risk assessments and contracts
- Audit reports (internal and external)


---

# Implementation Considerations

## FINMA Compliance Timeline

**If [Organization] becomes FINMA-regulated**:

**Month 1-3: Gap Assessment**

- Confirm FINMA applicability determination
- Document current ISO 27001 compliance status
- Identify FINMA-specific gaps
- Prioritize remediation activities


**Month 4-6: Critical Controls Implementation**

- Authentication and access control (Margin 56)
- Segregation of duties (Margin 58)
- Encryption (Margin 62)
- Logging infrastructure (Margins 63-68)


**Month 7-9: Monitoring and Resilience**

- SIEM implementation and tuning (Margins 69-72)
- Business continuity enhancement (Margins 73-80)
- Incident response procedures (Margins 85-87)


**Month 10-12: Testing and Validation**

- Internal audit with FINMA focus
- BC/DR testing (Margin 81-84)
- Compliance evidence documentation
- Management and board reporting


**Ongoing**: Annual cycle of testing, assessment, and improvement

## Resource Requirements

**Personnel**:

- CISO or equivalent (required by FINMA)
- Compliance Officer with FINMA expertise
- Security Operations Team (SOC)
- Business Continuity Manager
- Internal Audit with IT security expertise


**Technology**:

- Identity and Access Management (IAM) platform
- Privileged Access Management (PAM)
- SIEM platform with 24/7 monitoring
- Encryption key management (HSM or cloud KMS)
- Business continuity tools and alternate site


**External Support**:

- Legal counsel with FINMA experience
- External auditors familiar with FINMA requirements
- Managed Security Service Provider (MSSP) if needed


## Cost Implications

FINMA compliance typically requires:

- Enhanced security technology (IAM, PAM, SIEM, HSM)
- Increased staffing (CISO, SOC, compliance)
- External audit and consulting fees
- Business continuity infrastructure (DR site)
- Ongoing training and awareness programs


Estimated additional cost: 15-25% increase over base ISO 27001 compliance for small-to-medium financial institutions.

---

# Common Pitfalls and Lessons Learned

## Common FINMA Compliance Challenges

**Challenge 1: Underestimating FINMA Rigor**

- FINMA examinations are thorough and evidence-based
- Documentation must be comprehensive and current
- Policies alone are insufficient; evidence of implementation required


**Challenge 2: Insufficient Segregation of Duties**

- SoD violations common in small institutions
- Compensating controls must be robust and documented
- Automated SoD monitoring strongly recommended


**Challenge 3: Inadequate Logging and Monitoring**

- Log retention often shorter than FINMA expectation (12 months minimum)
- SIEM not tuned for financial institution use cases
- SOC staffing inadequate for 24/7 coverage


**Challenge 4: BC/DR Testing Gaps**

- Full-scale DR tests not conducted annually
- Test results not documented adequately
- Gaps not remediated in timely manner


**Challenge 5: Outsourcing Risk Management**

- Cloud services treated as "technology" rather than outsourcing
- FINMA notification requirements missed
- Right-to-audit clauses absent from contracts


## Best Practices

**Practice 1**: Engage FINMA-experienced auditors early
**Practice 2**: Conduct quarterly internal FINMA compliance reviews
**Practice 3**: Maintain comprehensive compliance evidence repository
**Practice 4**: Integrate FINMA requirements into change management
**Practice 5**: Train board and senior management on FINMA expectations
**Practice 6**: Establish direct communication channel with FINMA supervisor

---

# References and Resources

## FINMA Publications

**Primary Sources**:

- FINMA Circular 2023/1: Operational risks and resilience - banks
- FINMA Circular 2008/7: Outsourcing - banks
- FINMA Circular 2018/3: Outsourcing - insurers
- FINMA Guidance 05/2023: Cloud Outsourcing


**FINMA Website**: https://www.finma.ch/  
**FINMA Circulars**: https://www.finma.ch/en/documentation/finma-circulars/

## Related Standards and Frameworks

**ISO Standards**:

- ISO/IEC 27001:2022: Information Security Management
- ISO/IEC 27002:2022: Information Security Controls
- ISO/IEC 27017:2015: Cloud Services Security
- ISO/IEC 27018:2019: PII Protection in Public Cloud


**NIST Publications**:

- NIST SP 800-53: Security and Privacy Controls (informational reference)
- NIST Cybersecurity Framework (informational reference)


**Industry Guidance**:

- Swiss Banking Association: IT Security Guidelines
- EBA Guidelines on ICT and Security Risk Management (EU context)


## Legal and Compliance Resources

**Swiss Federal Acts**:

- Financial Market Supervision Act (FINSA)
- Banking Act (BA)
- Data Protection Act (FADP / nDSG)


**Compliance Consulting**:
Organizations subject to FINMA supervision should engage:

- Legal counsel with Swiss financial regulatory expertise
- Auditors experienced with FINMA examinations
- Compliance consultants familiar with FINMA requirements


---

# Appendix A: FINMA Compliance Self-Assessment Checklist

This checklist supports initial gap assessment for organizations subject to FINMA supervision:

## Information Security Framework (Margins 50-55)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Information security strategy documented and board-approved | ⬜ Yes ⬜ No ⬜ Partial | | |
| CISO or equivalent role established | ⬜ Yes ⬜ No | | |
| Annual information security risk assessment conducted | ⬜ Yes ⬜ No | | |
| Comprehensive security policies documented | ⬜ Yes ⬜ No ⬜ Partial | | |
| Annual security awareness training for all staff | ⬜ Yes ⬜ No | | |
| Third-party risk assessment process established | ⬜ Yes ⬜ No ⬜ Partial | | |

## Authentication and Access Control (Margin 56)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| MFA implemented for remote access | ⬜ Yes ⬜ No ⬜ Partial | | |
| MFA implemented for privileged accounts | ⬜ Yes ⬜ No ⬜ Partial | | |
| Role-based access control (RBAC) implemented | ⬜ Yes ⬜ No ⬜ Partial | | |
| Annual access recertification conducted | ⬜ Yes ⬜ No | | |
| Privileged Access Management (PAM) implemented | ⬜ Yes ⬜ No ⬜ Partial | | |

## Segregation of Duties (Margin 58)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| SoD matrix documented | ⬜ Yes ⬜ No ⬜ Partial | | |
| Automated SoD monitoring implemented | ⬜ Yes ⬜ No | | |
| SoD violations reported quarterly | ⬜ Yes ⬜ No | | |
| Compensating controls documented for unavoidable SoD conflicts | ⬜ Yes ⬜ No ⬜ Partial | | |

## Encryption (Margin 62)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| TLS 1.2+ for all data in transit | ⬜ Yes ⬜ No ⬜ Partial | | |
| Full disk encryption for endpoints | ⬜ Yes ⬜ No ⬜ Partial | | |
| Database encryption for sensitive data | ⬜ Yes ⬜ No ⬜ Partial | | |
| Centralized key management system | ⬜ Yes ⬜ No | | |
| No use of deprecated encryption algorithms | ⬜ Yes ⬜ No | | |

## Logging and Monitoring (Margins 63-72)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Comprehensive security event logging | ⬜ Yes ⬜ No ⬜ Partial | | |
| Log retention 12+ months | ⬜ Yes ⬜ No | | |
| Centralized log management (SIEM) | ⬜ Yes ⬜ No | | |
| 24/7 security monitoring (SOC) | ⬜ Yes ⬜ No | | |
| Real-time alerting for critical events | ⬜ Yes ⬜ No ⬜ Partial | | |

## Business Continuity (Margins 73-87)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Business Impact Analysis (BIA) conducted | ⬜ Yes ⬜ No | | |
| RTO/RPO defined and board-approved | ⬜ Yes ⬜ No | | |
| Business continuity plans documented | ⬜ Yes ⬜ No ⬜ Partial | | |
| Annual full-scale DR test conducted | ⬜ Yes ⬜ No | | |
| Incident response procedures documented | ⬜ Yes ⬜ No ⬜ Partial | | |
| FINMA incident reporting process established | ⬜ Yes ⬜ No | | |

## Outsourcing (FINMA 2008/7)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Material outsourcing arrangements notified to FINMA | ⬜ Yes ⬜ No ⬜ N/A | | |
| Service provider risk assessments conducted | ⬜ Yes ⬜ No ⬜ Partial | | |
| Contracts include right-to-audit clauses | ⬜ Yes ⬜ No ⬜ Partial | | |
| Annual SOC 2 Type II reports obtained from providers | ⬜ Yes ⬜ No ⬜ Partial | | |
| Exit strategies documented for critical providers | ⬜ Yes ⬜ No ⬜ Partial | | |

---

# Appendix B: FINMA Notification Template

**Subject**: Notification of [Incident Type] - [Organization Name]

**To**: FINMA Supervision Team  
**From**: [CISO / Compliance Officer Name]  
**Date**: [Date]  
**Organization**: [Legal Entity Name]  
**FINMA License Number**: [Number]

**Incident Summary**:

- **Incident Type**: [Security breach / System outage / Data loss / Other]
- **Discovery Date/Time**: [ISO 8601 format]
- **Incident Start Date/Time**: [ISO 8601 format]
- **Current Status**: [Ongoing / Contained / Resolved]


**Impact Assessment**:

- **Critical Business Processes Affected**: [List]
- **Customer Impact**: [Number of customers, service disruption]
- **Data Impact**: [Types and volume of data affected]
- **Financial Impact**: [Estimated if known]


**Root Cause** (preliminary if incident ongoing):
[Brief description]

**Remediation Actions Taken**:
1. [Action 1 - date/time]
2. [Action 2 - date/time]
3. [Action 3 - date/time]

**Ongoing Actions**:

- [Action with expected completion date]


**External Parties Notified**:

- [Customers: Yes/No/Planned]
- [Data Protection Authority: Yes/No/N/A]
- [Other regulators: Specify]


**Next Update**: [Date/time of next update to FINMA]

**Contact Information**:

- **Primary Contact**: [Name, Title, Phone, Email]
- **Alternate Contact**: [Name, Title, Phone, Email]


---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports potential FINMA compliance requirements as determined in ISMS-POL-00. All regulatory applicability determinations and binding requirements are defined in ISMS-POL-00 and approved ISMS policy documents.*

*For organizations NOT subject to FINMA supervision, this document is for informational awareness only and does NOT create compliance obligations.*