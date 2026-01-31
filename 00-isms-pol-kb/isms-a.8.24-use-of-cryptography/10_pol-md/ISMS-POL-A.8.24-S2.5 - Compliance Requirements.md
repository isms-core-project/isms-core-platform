# Control A.8.24: Use of Cryptography
## POLICY REQUIREMENTS - SECTION 2.5
## Compliance Requirements

---

**Document ID**: ISMS-POL-A.8.24-S2.5  
**Title**: Use of Cryptography - Compliance Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Compliance Manager | Initial regulatory compliance framework |

**Review Cycle**: Annual (or upon regulatory updates/new contractual obligations)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Legal/Compliance Officer (regulatory authority)
- Secondary: Chief Information Security Officer (CISO)
- Technical Review: Security Team Lead (for technical feasibility)
- Business: Chief Financial Officer or Contract Management (for client obligations)
- Final Authority: Executive Management (for strategic risk acceptance)

**Distribution**: Legal/Compliance Teams, CISO Office, Risk Management, Contract Management, External Auditors  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, nFADP (Swiss Data Protection), GDPR, FINMA (conditional), PCI DSS (conditional), SOC 2, industry-specific regulations

---

## 2.5 Compliance Requirements

### Purpose
This section defines requirements for ensuring and demonstrating compliance with cryptographic policies, regulatory obligations, and industry standards.

---

### 2.5.1 Regulatory Compliance

#### General Data Protection Regulation (GDPR)

**Applicability:**
- Applies to organizations processing personal data of EU residents
- Cryptography required for "appropriate technical measures" (Article 32)

**GDPR-Specific Requirements:**
- Encryption REQUIRED for personal data to demonstrate "security by design"
- Encryption REQUIRED for data transfers outside EU/EEA (adequacy mechanism)
- Encryption RECOMMENDED to reduce breach notification obligations (Article 34)
- Pseudonymization techniques SHOULD use cryptographic methods

**Data Subject Rights:**
- Encryption keys for personal data MUST support:
  - Right to erasure (crypto-shredding acceptable method)
  - Data portability (decryption must be possible for export)
- Key management MUST allow for individual data subject key destruction

#### Payment Card Industry Data Security Standard (PCI DSS)

**Applicability:**
- Organizations that store, process, or transmit payment card data

**PCI DSS Cryptographic Requirements:**
- **Requirement 3:** Protect stored cardholder data
  - Strong cryptography REQUIRED (AES-256 minimum)
  - Encryption keys separate from encrypted data
  - Key management per PCI DSS Annex B1
- **Requirement 4:** Encrypt transmission of cardholder data
  - TLS 1.2+ REQUIRED for transmission over public networks
  - Strong cryptography for wireless networks
- **Requirement 8:** Strong cryptographic authentication
  - MFA REQUIRED for remote access
  - Password complexity and hashing requirements

**PCI DSS Key Management:**
- Key custodian roles MUST be defined
- Dual control for key generation/distribution
- Key storage in HSM or encrypted key vault
- Annual key rotation for encryption keys

#### Health Insurance Portability and Accountability Act (HIPAA)

**Applicability:**
- Healthcare organizations and business associates handling Protected Health Information (PHI)

**HIPAA Security Rule Requirements:**
- Encryption ADDRESSABLE for PHI at rest (§164.312(a)(2)(iv))
- Encryption ADDRESSABLE for PHI in transit (§164.312(e)(2)(ii))
- "Addressable" means: implement if reasonable and appropriate, or document alternative

**Implementation Guidance:**
- Encryption STRONGLY RECOMMENDED for all ePHI
- Risk assessment REQUIRED if not implementing encryption
- Compensating controls MUST be documented if encryption not used
- Encryption method MUST meet NIST standards

#### Sarbanes-Oxley Act (SOX)

**Applicability:**
- Publicly traded companies (financial reporting controls)

**SOX Cryptographic Requirements:**
- Financial data integrity protection (digital signatures, audit logs)
- Access controls with strong authentication
- Data retention with integrity verification

**IT General Controls (ITGC):**
- Cryptographic controls for financial system access
- Audit trail protection using hashing
- Change management controls for cryptographic configurations

#### Other Regulatory Frameworks

**Industry-Specific:**
- **FISMA** (US Federal): FIPS 140-2 validated cryptography REQUIRED
- **FedRAMP**: FIPS 140-2 modules, specific cipher suite requirements
- **ISO/IEC 27018** (Cloud Privacy): Encryption for PII in cloud
- **NIST Cybersecurity Framework**: Cryptography under "Protect" function

**Geographic/Regional:**
- **EU eIDAS Regulation**: Qualified electronic signatures
- **Swiss DPA (FADP)**: Data protection with appropriate technical measures
- **California CCPA/CPRA**: Encryption reasonable security measure

---

### 2.5.2 Export Control Regulations

#### Cryptography Export Controls

**Applicability:**
- Organizations exporting software or hardware containing cryptography
- Applies to most countries (US, EU, others)

**US Export Administration Regulations (EAR):**
- Strong cryptography subject to export controls (ECCN 5A002, 5D002)
- Certain exemptions available:
  - Mass market software with notification
  - Open source with notification
  - Intra-company transfers
- Registration with BIS (Bureau of Industry and Security) may be required

**EU Dual-Use Regulation:**
- Cryptography on EU Dual-Use List (Category 5 Part 2)
- Export licenses may be required for certain destinations
- General export authorizations available for many scenarios

**Requirements:**
- Classification of cryptographic products REQUIRED
- Export license determination REQUIRED before international distribution
- Export compliance program MUST be documented
- Restricted destinations (embargoed countries) MUST be blocked

#### Cryptography Import Regulations

**Requirements:**
- Some countries require registration/notification for cryptography imports
- Examples: France (declaration), China (product testing), Russia (FSTEC certification)
- Legal review REQUIRED before deploying cryptography in foreign jurisdictions

---

### 2.5.3 Policy Deviations and Exceptions

#### Exception Process

**When Exceptions Are Permitted:**
- Technical impossibility of compliance
- Legacy systems pending replacement
- Specific business requirement with documented justification
- Compensating controls provide equivalent risk mitigation

**Exception Request Requirements:**
- All exceptions MUST use formal Exception Request Form (Appendix B of main policy)
- Exception MUST include:
  - Detailed technical justification
  - Business impact if not granted
  - Risk assessment (likelihood and impact)
  - Compensating controls
  - Remediation plan (if temporary)
  - Requested duration

**Exception Approval Authority:**

| Risk Level | Approval Required |
|------------|-------------------|
| **Low Risk** | IT Manager + Security Team Lead |
| **Medium Risk** | CISO |
| **High Risk** | CISO + Senior Management |
| **Critical Risk** | Executive Committee + Risk Committee |

**Exception Lifecycle:**
- Exceptions MUST have defined expiration date (maximum 1 year)
- Exceptions MUST be reviewed at expiration
- Renewal requires new justification and approval
- Exceptions MUST be tracked in risk register
- Quarterly exception review by security team

#### Compensating Controls

**Requirements for Compensating Controls:**
- Compensating controls MUST provide equivalent risk reduction
- Compensating controls MUST be documented in exception request
- Compensating controls MUST be verified and tested
- Examples of compensating controls:
  - Network segmentation for unencrypted legacy systems
  - Additional monitoring and alerting
  - Enhanced access controls
  - Data minimization (reduce sensitive data exposure)

#### Exception Documentation

**Required Documentation:**
- Exception approval form with signatures
- Risk assessment results
- Compensating control specifications
- Implementation evidence
- Monitoring and review schedule

**Exception Register:**
- Centralized exception register MUST be maintained
- Register MUST include: system, justification, risk level, compensating controls, expiration
- Register MUST be reviewed quarterly
- Non-compliance with exception terms MUST trigger incident response

---

### 2.5.4 Monitoring and Audit

#### Continuous Monitoring

**Automated Monitoring Requirements:**
- Certificate expiration monitoring (30-day advance alert)
- TLS/SSL configuration scanning (weekly)
- Encryption status verification for endpoints (daily)
- Key rotation compliance tracking (monthly)
- Failed authentication monitoring (real-time)
- Cryptographic algorithm usage detection (monthly)

**Monitoring Tools:**
- Security Information and Event Management (SIEM) integration
- Certificate management platforms
- Vulnerability scanners with crypto checks
- Configuration management tools

**Alerting Requirements:**
- Critical alerts: Certificate expiration within 7 days, use of prohibited algorithms
- High alerts: Certificate expiration within 30 days, key rotation overdue
- Medium alerts: Configuration drift, non-standard cipher suites
- Alert response SLA: Critical (2 hours), High (24 hours), Medium (7 days)

#### Internal Audits

**Audit Frequency:**
- Annual comprehensive cryptography audit
- Quarterly spot checks (sampling approach)
- Ad-hoc audits following security incidents

**Audit Scope:**
- Compliance with policy requirements (Sections 2.1-2.4)
- Key management lifecycle adherence
- Certificate inventory accuracy
- Password hashing implementation verification
- MFA adoption and enforcement
- Service account credential management
- Exception register review

**Audit Methodology:**
- Configuration reviews (TLS/SSL, database encryption, etc.)
- Interviews with system owners
- Technical testing (TLS Labs scans, cipher suite verification)
- Log analysis
- Sampling of encryption implementations

**Audit Reporting:**
- Audit findings MUST be documented
- Risk ratings assigned to findings
- Remediation plans REQUIRED for all findings
- Findings tracked to closure
- Audit results reported to management quarterly

#### External Audits

**ISO 27001 Certification Audits:**
- Control A.8.24 evidence MUST be readily available
- Implementation document (ISMS-IMP-A.8.24) MUST be current
- Evidence of key management procedures
- Certificate inventory and monitoring evidence
- Audit logs demonstrating monitoring

**Third-Party Assessments:**
- Penetration testing MUST include cryptographic controls
- Vulnerability assessments MUST check for weak cryptography
- Code reviews MUST verify secure cryptographic implementations
- Cloud security audits (SOC 2, FedRAMP, etc.) include cryptography

**Regulatory Audits:**
- PCI DSS: Annual Qualified Security Assessor (QSA) review
- HIPAA: Prepare encryption evidence for HHS audits
- Industry-specific: Maintain readiness for regulator inspections

---

### 2.5.5 Cryptographic Posture Assessment

#### Annual Review Requirements

**Comprehensive Annual Assessment:**
- Review of all cryptographic implementations
- Comparison against current industry standards (NIST, BSI, ENISA)
- Evaluation of emerging threats (quantum computing, new attacks)
- Assessment of new technologies and use cases

**Assessment Components:**
- Algorithm and key length review (update deprecation schedule)
- Protocol version review (TLS, SSH, etc.)
- Certificate authority trust review
- Key management process evaluation
- Third-party cryptographic library updates

**Outcome:**
- Updated cryptographic standards (Appendix A)
- Remediation roadmap for deprecated algorithms
- Budget requirements for cryptographic upgrades
- Policy updates if necessary

#### Threat Intelligence Integration

**Requirements:**
- Monitor cryptographic vulnerability disclosures
- Subscribe to security advisories (CERT, vendor bulletins)
- Participate in information sharing communities
- Rapid response process for critical cryptographic vulnerabilities

**Critical Vulnerability Response:**
- Example: Heartbleed, POODLE, BEAST, BREACH, etc.
- Emergency assessment within 24 hours
- Patch/mitigation deployment within 7 days for critical vulnerabilities
- Communication plan for customer impact

---

### 2.5.6 Training and Awareness

#### Role-Based Training Requirements

**All Employees:**
- Annual security awareness training including:
  - Importance of encryption
  - Password security
  - Recognizing secure connections (HTTPS)
  - Reporting suspected cryptographic issues

**IT and Security Staff:**
- Annual cryptography fundamentals training
- Secure implementation practices
- Key management procedures
- Incident response for cryptographic events
- Certificate lifecycle management

**Developers:**
- Secure coding with cryptography
- Cryptographic library usage
- Common mistakes (hard-coded keys, weak random number generation)
- Security testing for cryptographic implementations
- Annual refresher training

**System Administrators:**
- TLS/SSL configuration best practices
- Certificate management procedures
- Encryption implementation for servers and databases
- Key rotation procedures

**Database Administrators:**
- Transparent Data Encryption (TDE) implementation
- Connection encryption configuration
- Backup encryption procedures
- Key management for databases

#### Specialized Training

**Cryptography Specialists:**
- Advanced cryptography courses (recommended annually)
- Industry conferences (RSA Conference, Black Hat, etc.)
- Vendor-specific training (HSM management, KMS administration)
- Certification maintenance (CISSP, CCSP, etc.)

**Training Effectiveness:**
- Training completion tracking REQUIRED
- Knowledge assessments after training
- Practical exercises for technical staff
- Annual training needs assessment

---

### 2.5.7 Incident Response for Cryptographic Events

#### Incident Classification

**Cryptographic Incidents Include:**
- Key or certificate compromise
- Use of prohibited cryptographic algorithms discovered
- Certificate expiration causing service outage
- Cryptographic vulnerability exploitation
- Unauthorized changes to cryptographic configuration
- Loss of cryptographic hardware (HSM, smart cards)

**Severity Classification:**

| Severity | Examples | Response Time |
|----------|----------|---------------|
| **Critical** | Root CA compromise, mass key exposure | Immediate (1 hour) |
| **High** | Production certificate compromise, widespread weak crypto | 4 hours |
| **Medium** | Single system key compromise, certificate expiration | 24 hours |
| **Low** | Non-compliant configuration, approaching expiration | 7 days |

#### Incident Response Procedures

**Detection and Reporting:**
- Monitoring systems MUST alert on cryptographic anomalies
- Staff MUST report suspected cryptographic incidents immediately
- Incident reporting channels MUST be well-known and accessible

**Response Actions:**
- Follow organizational incident response plan
- Specific cryptographic incident procedures (Appendix C of main policy)
- Immediate containment (revoke certificates, isolate systems)
- Evidence preservation for forensics
- Communication to stakeholders

**Post-Incident Activities:**
- Root cause analysis REQUIRED
- Lessons learned documentation
- Policy/procedure updates
- Preventive measures implementation
- Follow-up training if needed

---

### 2.5.8 Vendor and Third-Party Cryptography

#### Third-Party Cryptographic Products

**Requirements:**
- Cryptographic products MUST be from reputable vendors
- Products SHOULD have independent security validation:
  - FIPS 140-2/140-3 validation (for HSMs, cryptographic modules)
  - Common Criteria certification
  - Independent security audits
- Proprietary/custom cryptographic algorithms PROHIBITED

**Vendor Assessment:**
- Vendor cryptographic security practices MUST be evaluated
- Vendor key management MUST be assessed
- Vendor incident response capabilities MUST be verified
- Vendor cryptographic roadmap SHOULD be reviewed

#### Cloud Service Provider Cryptography

**Requirements:**
- CSP cryptographic capabilities MUST meet organizational standards
- CSP MUST provide encryption at rest and in transit
- Customer-managed keys (CMEK) PREFERRED for sensitive data
- CSP MUST support key rotation
- CSP cryptographic compliance certifications REQUIRED (FedRAMP, SOC 2, ISO 27001)

**Due Diligence:**
- Review CSP security documentation
- Verify cryptographic algorithm support
- Understand CSP key management model
- Clarify data recovery procedures
- Verify CSP geographic data residency for encryption keys

#### Open Source Cryptographic Libraries

**Approved Libraries:**
- OpenSSL (with regular updates)
- BoringSSL (Google)
- LibreSSL (OpenBSD)
- Bouncy Castle
- Libsodium
- Microsoft Cryptography API: Next Generation (CNG)
- Java Cryptography Architecture (JCA)

**Requirements:**
- Open source libraries MUST be from trusted sources
- Libraries MUST be regularly updated (security patches)
- Vulnerability monitoring REQUIRED (CVE tracking)
- Custom modifications to libraries PROHIBITED without security review

---

### 2.5.9 Documentation and Record Keeping

#### Required Documentation

**Policy and Procedures:**
- This cryptography policy (all sections)
- Implementation procedures for key management
- Certificate lifecycle procedures
- Incident response procedures for cryptographic events
- Exception approval procedures

**Operational Records:**
- Certificate inventory
- Key management logs
- Key rotation records
- MFA enrollment records
- Exception register
- Audit findings and remediation tracking

**Evidence for Compliance:**
- TLS/SSL scan results
- Encryption verification reports
- Training completion records
- Audit reports (internal and external)
- Risk assessments for exceptions

#### Record Retention

**Retention Periods:**

| Record Type | Retention Period | Justification |
|-------------|------------------|---------------|
| **Policy versions** | Permanent | Regulatory/audit |
| **Audit reports** | 7 years | Legal/compliance |
| **Key management logs** | 7 years | Forensics/compliance |
| **Certificate records** | Certificate life + 2 years | Audit trail |
| **Exception approvals** | Exception life + 2 years | Compliance |
| **Training records** | Employment + 3 years | HR/compliance |
| **Incident reports** | 7 years | Legal/lessons learned |

**Storage Requirements:**
- Records MUST be stored securely
- Access to records MUST be controlled and logged
- Backup of records REQUIRED
- Records MUST be available for audit upon request

---

### 2.5.10 Metrics and Key Performance Indicators (KPIs)

#### Compliance KPIs

**Mandatory KPIs to Track:**

| KPI | Target | Measurement Frequency |
|-----|--------|----------------------|
| **Certificate expiration incidents** | 0 per quarter | Monthly |
| **TLS 1.3 adoption rate** | >80% by [year] | Quarterly |
| **MFA coverage (privileged accounts)** | 100% | Monthly |
| **MFA coverage (all accounts)** | >90% | Quarterly |
| **Key rotation compliance** | >95% | Monthly |
| **Endpoint encryption compliance** | >98% | Monthly |
| **Prohibited algorithm detection** | 0 | Monthly |
| **Security training completion** | 100% | Quarterly |
| **Remediation plan on-track %** | >85% | Quarterly |
| **Critical vulnerability patching** | <7 days | Per incident |

#### Reporting Requirements

**Monthly Reports:**
- Certificate expiration forecast
- Key rotation compliance status
- MFA adoption metrics
- Critical findings summary

**Quarterly Reports:**
- Comprehensive cryptographic posture
- KPI dashboard
- Gap remediation progress
- Exception register review
- Training completion status

**Annual Reports:**
- Cryptographic posture assessment results
- Policy compliance summary
- Audit findings and remediation
- Strategic recommendations
- Budget requirements for next year

**Report Distribution:**
- CISO: All reports
- IT Management: Monthly and quarterly operational reports
- Executive Management: Quarterly summary and annual assessment
- Audit Committee: Annual compliance report

---

## Compliance Verification

**This section SHALL be verified through:**
- Quarterly compliance KPI review
- Annual regulatory compliance assessment
- Internal audit of exception process
- External audit readiness review
- Training completion verification
- Documentation and record keeping audit

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Section 1: Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1** - Use of Cryptographic Controls
- **ISMS-POL-A.8.24-S2.2** - Data Transmission Requirements
- **ISMS-POL-A.8.24-S2.3** - Data Storage Requirements
- **ISMS-POL-A.8.24-S2.4** - Authentication Requirements
- **ISMS-IMP-A.8.24** - Implementation & Compliance Status
- **ISMS Risk Register**
- **ISMS Incident Response Plan**

---

**End of Section 2.5 - Compliance Requirements**

**This completes the Policy Requirements portion (Section 2) of ISMS-POL-A.8.24**

*"Compliance is what you do. Security is what happens."*  
*— The First Law of Security Engineering*