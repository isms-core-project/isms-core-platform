# Control A.8.24: Use of Cryptography
## APPENDIX C
## Incident Response Framework for Cryptographic Events

---

**Document ID**: ISMS-POL-A.8.24-S5.C  
**Title**: Use of Cryptography - Incident Response for Cryptographic Events  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Incident Response Manager | Initial cryptographic incident response procedures |

**Review Cycle**: Annual (or upon major cryptographic incident/vulnerability disclosure)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Incident Response Manager (operational authority)
- Secondary: Chief Information Security Officer (CISO)
- Technical Review: Security Team Lead / SOC Manager
- Business Continuity: Business Continuity Manager (for DR/BC integration)
- Compliance: Legal/Compliance Officer (for breach notification requirements)

**Distribution**: Incident Response Team, Security Operations Center (SOC), IT Security Team, Management Team, Legal/Compliance  
**Related Standards**: ISO/IEC 27001:2022 Controls A.5.24-A.5.28 (Incident Management), A.8.24, NIST SP 800-61 (Incident Handling), nFADP breach notification, GDPR Art. 33-34

---

## 1. Purpose and Scope

### 1.1 Purpose

This appendix defines the specific incident response procedures for cryptographic failures, compromises, and security events related to cryptographic controls as mandated by Control A.8.24 of ISO 27001:2022.

Cryptographic incidents present unique challenges requiring specialized response procedures due to:
- Potential widespread impact across multiple systems
- Technical complexity requiring cryptographic expertise
- Regulatory notification requirements
- Need for forensic preservation of cryptographic evidence
- Cascading effects on trust relationships and authentication chains

### 1.2 Scope

This framework applies to all cryptographic security incidents including:
- Cryptographic key compromise or suspected compromise
- Certificate authority compromise or unauthorized issuance
- Encryption failures resulting in data exposure
- Cryptographic algorithm vulnerabilities
- Hash collision attacks or weaknesses
- Digital signature forgery or repudiation
- Side-channel attacks on cryptographic implementations
- Cryptographic protocol downgrade attacks
- Random number generator failures
- Hardware security module (HSM) failures or compromise
- Quantum computing threats to existing cryptography

### 1.3 Integration with ISMS Incident Management

This framework operates as a **specialized extension** of the organization's primary ISMS Incident Management Procedure and **MUST** be followed in conjunction with standard incident response processes.

**Relationship hierarchy:**
1. **Primary:** ISMS Incident Management Procedure (ISMS-PROC-IR)
2. **Supplementary:** This Cryptographic Incident Response Framework
3. **Parallel:** ISO 27001:2022 Controls A.5.24, A.5.25, A.5.26

---

## 2. Cryptographic Incident Classification

### 2.1 Incident Severity Levels

Cryptographic incidents **MUST** be classified according to the following severity matrix:

| Severity | Definition | Response Time | Examples |
|----------|------------|---------------|----------|
| **P1 - Critical** | Active exploitation or confirmed compromise with immediate organizational impact | **15 minutes** | - Root CA private key compromise<br>- Production TLS private keys exposed publicly<br>- Encryption master key extracted<br>- Active MITM attack using forged certificates<br>- HSM physical breach |
| **P2 - High** | Confirmed cryptographic weakness with high probability of exploitation | **1 hour** | - Certificate issued to unauthorized party<br>- Weak cipher suite actively negotiated<br>- Password database hashed with broken algorithm<br>- Encryption key stored in plaintext<br>- TLS downgrade attack detected |
| **P3 - Medium** | Cryptographic misconfiguration or potential vulnerability requiring investigation | **4 hours** | - Certificate expiration within 7 days<br>- Non-compliant algorithm in use<br>- Weak key length detected<br>- Improper certificate chain validation<br>- Self-signed certificate in production |
| **P4 - Low** | Policy deviation or cryptographic hygiene issue with minimal immediate risk | **24 hours** | - Certificate expiring in 30 days<br>- Missing certificate monitoring<br>- Incomplete cryptographic documentation<br>- Legacy algorithm present but not used<br>- Certificate deployed without approval |

### 2.2 Impact Assessment Criteria

When classifying incidents, consider:

**Confidentiality Impact:**
- Volume of data potentially exposed
- Data classification level (Public/Internal/Confidential/Restricted)
- Presence of PII, PHI, PCI, or other regulated data
- Duration of potential exposure

**Integrity Impact:**
- Ability to forge or modify data
- Authentication or authorization bypass potential
- Digital signature repudiation risk
- Transaction integrity compromise

**Availability Impact:**
- System or service disruption
- Business process interruption
- Recovery time requirements

**Compliance Impact:**
- Regulatory notification requirements (GDPR, HIPAA, PCI-DSS, etc.)
- Contractual obligations to customers
- Industry-specific regulations

---

## 3. Incident Response Lifecycle

### 3.1 Phase 1: Detection and Identification

#### 3.1.1 Detection Sources

Cryptographic incidents may be detected through:

**Automated Monitoring:**
- Certificate expiration monitoring alerts
- TLS/SSL handshake failure logs
- Cryptographic API error logs
- HSM audit logs and tamper alerts
- Intrusion detection system (IDS) signatures
- Security Information and Event Management (SIEM) correlation rules
- Vulnerability scanners identifying weak ciphers
- Certificate Transparency log monitoring

**Manual Discovery:**
- Security audits and assessments
- Penetration testing findings
- Code review discoveries
- Vendor security advisories
- Threat intelligence reports
- User reports of certificate warnings
- Third-party security researcher disclosure

#### 3.1.2 Initial Assessment Checklist

Upon detection, the first responder **MUST** gather:

```
☐ Date/Time of detection (UTC)
☐ Detection method and source
☐ Systems/applications affected
☐ Cryptographic component involved (key, cert, algorithm, protocol)
☐ Data classification of affected systems
☐ Current business impact (if any)
☐ Evidence of active exploitation (if any)
☐ Related logs and monitoring data
☐ Point of contact for affected system
```

#### 3.1.3 Immediate Notification

**Within detection timeframe based on severity:**

| Role | Notification Method | P1 | P2 | P3 | P4 |
|------|-------------------|----|----|----|----|
| **Information Security Officer** | Phone + Email | Immediate | 15 min | 1 hour | 4 hours |
| **On-Call Security Engineer** | Pager/Phone | Immediate | 15 min | 1 hour | Next business day |
| **CISO** | Phone + Email | Immediate (P1) | 1 hour | 4 hours | Email only |
| **System Owner** | Phone/Email | 15 min | 30 min | 2 hours | 8 hours |
| **IT Operations** | Ticket + Chat | 15 min | 30 min | 2 hours | 4 hours |

**P1 Critical incidents require immediate conference bridge establishment.**

---

### 3.2 Phase 2: Containment

#### 3.2.1 Immediate Containment Actions

**The incident response team MUST prioritize containment to prevent further damage.**

**For Key/Certificate Compromise:**
```
1. DO NOT immediately revoke without coordination (may alert attacker)
2. Identify all systems using compromised material
3. Prepare replacement keys/certificates
4. Coordinate simultaneous rotation across all systems
5. Revoke compromised material
6. Update Certificate Revocation Lists (CRL) / OCSP
7. Monitor for use of revoked material
```

**For Encryption Failure/Data Exposure:**
```
1. Isolate affected systems from network (if safe to do so)
2. Stop data flow to compromised storage/transmission
3. Preserve forensic evidence (memory dumps, logs)
4. Identify scope of data exposure
5. Document exposed data classifications
6. Secure backup copies
7. Engage legal/compliance for notification requirements
```

**For Algorithm/Protocol Weakness:**
```
1. Identify all systems using vulnerable algorithm/protocol
2. Assess exploitability and active exploitation
3. Implement protocol enforcement (disable weak options)
4. Deploy configuration changes to require strong alternatives
5. Monitor for downgrade attempts
6. Plan migration if no strong alternative available
```

**For HSM Compromise:**
```
1. Physically secure HSM device
2. Initiate HSM tamper response procedures
3. Disable HSM network connectivity
4. Preserve audit logs and tamper logs
5. Engage HSM vendor support
6. Identify all keys stored in HSM
7. Prepare key recovery from backup HSM
8. Assess need for full key rotation
```

#### 3.2.2 Containment Decision Matrix

| Incident Type | Containment Priority | Acceptable Downtime | Coordination Required |
|---------------|---------------------|--------------------|-----------------------|
| **Root CA Compromise** | Immediate full isolation | Extended (days) | PKI team, all cert users, vendors |
| **Production TLS Key Leak** | Immediate rotation | Minimal (minutes) | Load balancer teams, monitoring |
| **Encryption Master Key** | Immediate system isolation | Hours to days | Data owners, backup teams, legal |
| **Weak Algorithm in Use** | Configuration enforcement | None (config change) | System owners, change management |
| **Certificate Expiration** | Renewal and deployment | Minimal (minutes) | Certificate authority, system owners |

---

### 3.3 Phase 3: Eradication

#### 3.3.1 Root Cause Analysis

**The security team MUST identify the root cause:**

**Key Questions:**
- How was the cryptographic material compromised or weakness introduced?
- What vulnerability or misconfiguration enabled this incident?
- Was this a targeted attack or opportunistic exploitation?
- How long has the vulnerability existed?
- What systems/processes failed to prevent or detect this earlier?

**Investigation Areas:**
```
☐ Access controls to cryptographic material
☐ Key management procedures and adherence
☐ Configuration management and change control
☐ Monitoring and alerting effectiveness
☐ Staff training and awareness
☐ Vendor/third-party involvement
☐ Cryptographic library versions and vulnerabilities
☐ Hardware security and physical access
```

#### 3.3.2 Eradication Actions

**Complete removal of compromised/weak cryptographic elements:**

**For Compromised Keys/Certificates:**
1. Revoke all compromised material via CRL and OCSP
2. Remove compromised keys from all key stores
3. Securely delete compromised key material (overwrite, not just delete)
4. Remove trust of compromised CA certificates (if applicable)
5. Clear any cached or stored sessions using compromised material
6. Rotate any keys derived from compromised material
7. Update trust stores across all systems

**For Vulnerable Algorithms/Protocols:**
1. Remove vulnerable cipher suites from all configurations
2. Update cryptographic libraries to patched versions
3. Implement minimum version enforcement
4. Deploy configuration management to prevent reintroduction
5. Update secure development guidelines
6. Scan codebase for hardcoded vulnerable algorithms

**For Configuration Weaknesses:**
1. Correct all identified misconfigurations
2. Implement configuration management/Infrastructure as Code
3. Deploy automated compliance scanning
4. Update configuration baselines and standards
5. Remove any backdoors or test configurations

---

### 3.4 Phase 4: Recovery

#### 3.4.1 Recovery Planning

**Develop and document recovery plan including:**

```
Recovery Plan Components:
┌─────────────────────────────────────────────────┐
│ 1. Service restoration priority order           │
│ 2. Cryptographic material replacement schedule  │
│ 3. System-by-system recovery steps              │
│ 4. Validation and testing procedures            │
│ 5. Rollback procedures if recovery fails        │
│ 6. Communication plan for users/stakeholders    │
│ 7. Success criteria and verification            │
└─────────────────────────────────────────────────┘
```

#### 3.4.2 Recovery Execution

**Phased recovery approach:**

**Phase 1: Core Infrastructure (0-4 hours)**
- Certificate authorities and PKI infrastructure
- Authentication systems (LDAP, AD, SSO)
- Key management systems and HSMs
- DNS and core network services

**Phase 2: Critical Business Systems (4-12 hours)**
- Revenue-generating applications
- Customer-facing services
- Payment processing systems
- External partner integrations

**Phase 3: Internal Systems (12-24 hours)**
- Internal applications and tools
- Development/testing environments
- Administrative systems
- Monitoring and logging systems

**Phase 4: Legacy/Non-Critical (24-48 hours)**
- Archived systems
- Secondary environments
- Development/sandbox systems

#### 3.4.3 Recovery Validation

**Before declaring recovery complete, verify:**

```
☐ All systems using new cryptographic material
☐ No systems still using compromised/weak material
☐ Certificate validation working correctly
☐ TLS/SSL handshakes completing successfully
☐ No certificate warnings for users
☐ Authentication and authorization functioning
☐ Encrypted data accessible with new keys
☐ Digital signatures validating correctly
☐ Performance within acceptable parameters
☐ Monitoring and alerting operational
☐ Backup systems updated with new material
```

#### 3.4.4 User Communication

**Develop communication plan for:**

**Internal Users:**
- Notification of incident (appropriate detail level)
- Actions users must take (certificate installation, password changes, etc.)
- Timeline for service restoration
- Points of contact for issues

**External Users/Customers:**
- Incident notification (if required by regulation/contract)
- Impact assessment and scope
- Actions customers should take
- Remediation completed
- Preventive measures implemented

**Regulatory Bodies:**
- Incident notification within required timeframes (GDPR 72 hours, etc.)
- Nature and scope of breach
- Data subjects affected
- Measures taken to address the breach
- Measures to mitigate adverse effects

---

### 3.5 Phase 5: Post-Incident Activities

#### 3.5.1 Post-Incident Review (PIR)

**MUST be completed within 5 business days of incident closure.**

**PIR Participants:**
- Incident Commander
- Information Security Officer
- System Owners
- Technical Responders
- CISO (for P1/P2 incidents)

**PIR Agenda:**
1. **Incident Timeline Review**
   - Detection to containment time
   - Containment to eradication time
   - Eradication to recovery time
   - Total incident duration

2. **What Went Well**
   - Effective detection mechanisms
   - Successful containment actions
   - Efficient communication
   - Good coordination between teams

3. **What Went Wrong**
   - Delayed detection
   - Containment challenges
   - Communication breakdowns
   - Resource constraints

4. **Lessons Learned**
   - Technical lessons
   - Process lessons
   - Organizational lessons
   - Training gaps identified

5. **Action Items**
   - Preventive measures to implement
   - Detection improvements needed
   - Process updates required
   - Training to be conducted
   - Tools or resources needed

#### 3.5.2 Documentation Requirements

**Incident report MUST include:**

```markdown
## Cryptographic Incident Report

### Executive Summary
- Incident classification and severity
- Business impact summary
- Root cause (high-level)
- Resolution summary
- Total cost impact

### Incident Details
- Detection date/time and method
- Affected systems and data
- Cryptographic component involved
- Timeline of key events
- Response team members

### Technical Analysis
- Root cause analysis
- Attack vector or vulnerability exploited
- Scope of compromise
- Forensic findings
- Indicators of Compromise (IoCs)

### Response Actions
- Containment measures taken
- Eradication steps completed
- Recovery procedures executed
- Validation performed

### Impact Assessment
- Confidentiality impact
- Integrity impact
- Availability impact
- Compliance/regulatory impact
- Financial impact

### Remediation and Prevention
- Immediate fixes implemented
- Long-term preventive measures
- Policy updates required
- Training needs identified

### Recommendations
- Technical recommendations
- Process improvements
- Organizational changes
- Budget/resource requests

### Appendices
- Detailed timeline
- Forensic evidence
- Configuration changes
- Communication logs
```

#### 3.5.3 Metrics and KPIs

**Track and report:**

| Metric | Target | Purpose |
|--------|--------|---------|
| **Mean Time to Detect (MTTD)** | < 15 minutes (P1)<br>< 1 hour (P2) | Detection effectiveness |
| **Mean Time to Contain (MTTC)** | < 1 hour (P1)<br>< 4 hours (P2) | Containment efficiency |
| **Mean Time to Recover (MTTR)** | < 24 hours (P1)<br>< 48 hours (P2) | Recovery capability |
| **False Positive Rate** | < 10% | Alert accuracy |
| **Incident Recurrence** | 0% (same root cause) | Remediation effectiveness |

#### 3.5.4 Knowledge Base Updates

**Update organizational knowledge:**
- Add incident to incident database
- Update runbooks with lessons learned
- Document new attack patterns
- Share IoCs with threat intelligence platforms
- Update training materials
- Enhance detection signatures/rules

---

## 4. Specific Incident Response Procedures

### 4.1 Certificate Compromise Response

**Scenario:** Private key for certificate has been compromised or suspected compromise.

**Immediate Actions (0-15 minutes):**
```
1. Confirm scope of compromise
   - Single certificate or CA?
   - Number of systems affected?
   - Active exploitation observed?

2. Prepare replacement certificates
   - Generate new key pair
   - Request certificate from CA
   - Stage certificates for deployment

3. Coordinate deployment
   - Identify all systems using certificate
   - Schedule simultaneous rotation
   - Prepare rollback plan

4. Execute rotation
   - Deploy new certificates
   - Update configurations
   - Restart services as needed
   - Verify new certificates in use

5. Revoke compromised certificate
   - Submit revocation request to CA
   - Specify reason: keyCompromise
   - Verify CRL/OCSP updated
   - Monitor for continued use of revoked cert

6. Investigate compromise vector
   - Review access logs
   - Check for unauthorized access to key stores
   - Examine system logs for exfiltration
   - Preserve forensic evidence
```

**Extended Actions (1-24 hours):**
- Update certificate inventory
- Review and strengthen key protection
- Audit other certificates for similar exposure
- Update incident response runbooks
- Conduct post-incident review

**Specific Considerations:**
- **Wildcard Certificates:** May affect dozens of systems, requires extensive coordination
- **CA Certificates:** Catastrophic impact, requires full trust chain replacement
- **Code Signing Certificates:** May require re-signing of software/updates
- **Client Authentication Certs:** May require coordinated user re-enrollment

---

### 4.2 Encryption Key Compromise Response

**Scenario:** Encryption key material has been exposed or compromised.

**Critical Questions:**
1. What data was encrypted with this key?
2. Is the data still encrypted with this key?
3. Can an attacker decrypt historical data?
4. Are there key backups that are also compromised?

**Response Phases:**

**Phase 1: Impact Assessment (0-30 minutes)**
```
☐ Identify all data encrypted with compromised key
☐ Assess data classification and sensitivity
☐ Determine if historical data is at risk
☐ Check for key backups and their security
☐ Evaluate regulatory notification requirements
☐ Assess business continuity impact
```

**Phase 2: Data Protection (30 minutes - 2 hours)**
```
☐ Isolate systems with encrypted data (if feasible)
☐ Stop new data encryption with compromised key
☐ Secure forensic copies before making changes
☐ Generate new encryption key using secure process
☐ Re-encrypt sensitive data with new key
☐ Securely destroy compromised key material
☐ Update all applications to use new key
```

**Phase 3: Historical Data Assessment (2-24 hours)**
```
☐ Inventory all data ever encrypted with key
☐ Assess retention requirements and policies
☐ Determine if re-encryption is required
☐ Prioritize re-encryption by data sensitivity
☐ Execute re-encryption in priority order
☐ Verify data integrity after re-encryption
☐ Maintain chain of custody for forensics
```

**Phase 4: Investigation and Remediation (1-7 days)**
```
☐ Determine how key was compromised
☐ Review key management procedures
☐ Assess need for HSM implementation
☐ Update key handling procedures
☐ Implement enhanced monitoring
☐ Conduct staff training on key handling
☐ Review and update data classification
```

**Regulatory Notification:**
- **GDPR:** Notify within 72 hours if personal data at risk
- **HIPAA:** Notify if PHI is compromised
- **PCI-DSS:** Notify payment brands and acquirer immediately
- **State Breach Laws:** Notify per state requirements

---

### 4.3 Algorithm Vulnerability Response

**Scenario:** Cryptographic algorithm in use has been found vulnerable (e.g., SHA-1 collision, weak cipher).

**Vulnerability Assessment (0-4 hours):**
```
1. Understand the vulnerability
   - Type of attack (collision, preimage, etc.)
   - Computational difficulty
   - Practical exploitability
   - Proof of concept availability

2. Identify organizational exposure
   - Systems using vulnerable algorithm
   - Context of use (signatures, encryption, hashing)
   - Data protected by algorithm
   - Internet-facing vs. internal use

3. Assess urgency
   - Are active exploits observed?
   - Is algorithm use mandated by policy?
   - What is migration complexity?
   - Are alternatives available?
```

**Migration Planning (4-48 hours):**
```
☐ Research approved replacement algorithms
☐ Identify systems requiring updates
☐ Assess compatibility and dependencies
☐ Develop migration plan and timeline
☐ Test replacement in non-production
☐ Prepare rollback procedures
☐ Communicate changes to stakeholders
```

**Migration Execution (Timeline varies):**
```
Priority 1 (0-7 days): Internet-facing systems
- Public web servers
- VPN concentrators
- Email gateways
- External APIs

Priority 2 (7-30 days): Internal production systems
- Internal applications
- Databases
- File servers
- Authentication systems

Priority 3 (30-90 days): Development/test systems
- Testing environments
- Development workstations
- Sandbox systems

Priority 4 (90+ days): Legacy systems with compensating controls
- Systems scheduled for decommission
- Isolated systems with no internet access
- Systems with architectural limitations
```

**Example: SHA-1 to SHA-256 Migration**
```bash
# Identify systems using SHA-1
$ grep -r "SHA1\|SHA-1" /etc/ /opt/

# Update TLS configurations
# Apache
SSLCipherSuite HIGH:!aNULL:!MD5:!SHA1

# Nginx
ssl_ciphers HIGH:!aNULL:!MD5:!SHA1;

# Update certificate signatures
# Request new certificates with SHA-256
# Deploy updated certificates

# Update code signing
# Re-sign applications with SHA-256 certificates

# Update password hashing (if applicable)
# Note: Password hashes typically use SHA-256+ already
# Review authentication systems for SHA-1 use
```

---

### 4.4 HSM Failure or Compromise Response

**Scenario:** Hardware Security Module has failed, been tampered with, or suspected compromise.

**Immediate Response (0-30 minutes):**
```
CRITICAL: HSMs have tamper-detection and may auto-zeroize (erase keys)
DO NOT power cycle or reset HSM without consulting vendor

1. Physical Security
   ☐ Secure HSM location
   ☐ Preserve tamper-evident seals
   ☐ Document physical state (photos)
   ☐ Restrict physical access
   ☐ Review access logs and badge records

2. Logical Security
   ☐ Disable HSM network connectivity (if possible)
   ☐ Export HSM audit logs immediately
   ☐ Review HSM event logs for anomalies
   ☐ Check for unauthorized configuration changes
   ☐ Verify backup HSM status

3. Assessment
   ☐ HSM tamper sensor status
   ☐ Key material status (available/zeroized)
   ☐ Type of failure (hardware/attack/configuration)
   ☐ Impact on dependent systems
   ☐ Backup HSM availability
```

**Failover to Backup HSM (30 minutes - 2 hours):**
```
1. Validate backup HSM
   ☐ Verify backup HSM is operational
   ☐ Confirm key material is current
   ☐ Test cryptographic operations
   ☐ Verify audit logging is functional

2. Redirect operations
   ☐ Update application configurations
   ☐ Update load balancer settings
   ☐ Redirect API calls to backup HSM
   ☐ Monitor for errors during transition

3. Verify operations
   ☐ Test certificate signing
   ☐ Test encryption/decryption operations
   ☐ Test key generation
   ☐ Validate performance
   ☐ Check audit logs
```

**Primary HSM Recovery (2-24 hours):**
```
IF HSM is compromised (tampered):
  1. Engage vendor support for forensic analysis
  2. DO NOT restore keys to potentially compromised HSM
  3. Replace HSM hardware
  4. Consider all keys compromised - initiate key rotation
  5. Restore keys from secure backup to NEW HSM
  6. Update all systems to use new key material

IF HSM failed (non-tamper):
  1. Engage vendor support for RMA/repair
  2. Restore HSM from backup or replace
  3. Test all cryptographic operations
  4. Return to service when validated
  5. Update monitoring for early failure detection
```

**Post-Incident HSM Hardening:**
- Review HSM physical security controls
- Audit HSM administrative access
- Test failover procedures under load
- Update HSM firmware to latest secure version
- Review and update backup procedures
- Implement enhanced monitoring and alerting
- Consider HSM clustering/HA configuration

---

### 4.5 Certificate Expiration Response

**Scenario:** Certificate has expired or is expiring imminently, causing service disruption.

**Critical Distinction:**
- **Already Expired:** Emergency response required (P1/P2)
- **Expiring Soon:** Planned maintenance (P3/P4)

**Emergency Response for Expired Certificate (0-2 hours):**

```
1. Immediate Service Restoration
   ☐ Assess business impact and affected systems
   ☐ Determine if temporary certificate can be used
   ☐ Generate new key pair (if time permits) OR
   ☐ Request emergency certificate for existing key (faster)
   ☐ Deploy certificate as quickly as possible
   ☐ Verify service restoration

2. Root Cause Analysis
   ☐ Why did certificate expire unnoticed?
   ☐ Was monitoring in place?
   ☐ Did alerts fire? Were they acknowledged?
   ☐ Was renewal attempted?
   ☐ What process failed?

3. Immediate Preventive Actions
   ☐ Scan all systems for other expiring certificates
   ☐ Verify monitoring and alerting working
   ☐ Set alerts for 90, 60, 30, 14, 7 days before expiration
   ☐ Update certificate inventory
   ☐ Assign owners to all certificates
```

**Proactive Expiration Management:**

**Certificate Lifecycle Timeline:**
```
Certificate Issued
    |
    ├─ 90 days before expiry: Initial renewal notification
    |                         System owner notified
    |
    ├─ 60 days before expiry: Reminder notification
    |                         Security team cc'd
    |
    ├─ 30 days before expiry: Urgent notification
    |                         Manager notified
    |                         Renewal plan required
    |
    ├─ 14 days before expiry: Critical notification
    |                         Daily reminders begin
    |                         Escalate to senior management
    |
    ├─ 7 days before expiry:  Emergency status (P3)
    |                         CISO notified
    |                         Incident created
    |
    ├─ 1 day before expiry:   Critical status (P2)
    |                         Emergency response activated
    |
    └─ Expiration:            Service outage (P1)
                              Emergency certificate issuance
```

---

### 4.6 Man-in-the-Middle (MITM) Attack Response

**Scenario:** Active MITM attack detected using forged or intercepted cryptographic material.

**Immediate Actions (0-15 minutes):**
```
1. Confirm the attack
   ☐ Validate it's not a false positive
   ☐ Identify affected connections/sessions
   ☐ Determine attack vector (rogue cert, downgrade, etc.)
   ☐ Assess scope (single user, entire subnet, etc.)

2. Isolate affected systems
   ☐ Block attacker IP addresses at firewall
   ☐ Isolate compromised network segment
   ☐ Terminate affected sessions
   ☐ Disable affected services if necessary

3. Preserve evidence
   ☐ Capture network traffic (PCAP)
   ☐ Save certificate chains presented by attacker
   ☐ Document source IP, timing, affected users
   ☐ Save relevant firewall and IDS logs
```

**Investigation Phase (15 minutes - 4 hours):**
```
1. Determine attack method
   ☐ Rogue certificate issued by trusted CA?
   ☐ Certificate with trusted root in user's trust store?
   ☐ SSL stripping or protocol downgrade?
   ☐ DNS hijacking or ARP spoofing?
   ☐ Compromised intermediate proxy?

2. Identify impact
   ☐ What data was transmitted during attack?
   ☐ Were credentials exposed?
   ☐ Was sensitive data intercepted?
   ☐ How long was attack active?

3. Remediation based on attack type:

   IF rogue certificate from trusted CA:
     ☐ Report to CA immediately
     ☐ Request certificate revocation
     ☐ Remove CA from trust store if compromised CA
     ☐ Monitor CT logs for other rogue issuances

   IF protocol downgrade attack:
     ☐ Enforce minimum TLS version (1.2+)
     ☐ Disable weak cipher suites
     ☐ Implement HTTP Strict Transport Security (HSTS)
     ☐ Deploy certificate pinning where appropriate

   IF network-based attack (ARP, DNS):
     ☐ Investigate network infrastructure
     ☐ Enable DNSSEC
     ☐ Implement ARP inspection
     ☐ Review network access controls
```

**User Notification and Remediation:**
```
☐ Notify affected users of potential credential compromise
☐ Force password resets for exposed credentials
☐ Invalidate potentially compromised sessions/tokens
☐ Educate users on certificate warnings
☐ Provide guidance on verifying certificates
☐ Monitor for account takeover attempts
```

---

## 5. Specialized Response Scenarios

### 5.1 Quantum Computing Threat

**Scenario:** Quantum computer breakthrough threatens current cryptographic algorithms.

**NOTE:** This is a **strategic threat** rather than an immediate incident, but requires rapid organizational response.

**Assessment Phase (0-7 days):**
```
1. Understand the threat
   ☐ Which algorithms are affected?
   ☐ What is the timeline to practical exploitation?
   ☐ Are post-quantum alternatives standardized?
   ☐ What guidance has NIST/industry provided?

2. Inventory vulnerable cryptography
   ☐ RSA key exchange (all key sizes vulnerable)
   ☐ Elliptic Curve Cryptography (ECC)
   ☐ Diffie-Hellman key exchange
   ☐ Digital Signature Algorithm (DSA)
   ☐ ECDSA (Elliptic Curve DSA)
   ☐ Systems using these for confidentiality/authentication

3. Assess organizational exposure
   ☐ Long-lived encrypted data (archives, backups)
   ☐ "Harvest now, decrypt later" threat to current traffic
   ☐ Authentication mechanisms dependent on vulnerable algorithms
   ☐ Digital signatures with long validity periods
   ☐ PKI infrastructure and certificate hierarchies
   ☐ VPN and remote access systems
```

**Algorithms Affected by Quantum Computing:**

| Algorithm Type | Current Algorithm | Quantum Vulnerability | Post-Quantum Alternative |
|----------------|-------------------|----------------------|-------------------------|
| **Public Key Encryption** | RSA (all sizes) | Shor's Algorithm | CRYSTALS-Kyber (NIST) |
| **Key Exchange** | ECDH, DHE | Shor's Algorithm | Kyber, NTRU |
| **Digital Signatures** | RSA, ECDSA, DSA | Shor's Algorithm | CRYSTALS-Dilithium, SPHINCS+ |
| **Symmetric Encryption** | AES-128 | Grover's Algorithm (weakened) | AES-256 (quantum-resistant) |
| **Hash Functions** | SHA-256 | Grover's Algorithm (weakened) | SHA-384, SHA-512 (quantum-resistant) |

**Strategic Response Plan:**

**Immediate Actions (0-30 days):**
```
☐ Form Quantum Readiness Team (CISO, Security Architects, Infrastructure Leads)
☐ Complete cryptographic inventory across all systems
☐ Prioritize long-lived data for immediate protection
☐ Upgrade symmetric encryption: AES-128 → AES-256
☐ Upgrade hash functions: SHA-256 → SHA-384/512 where feasible
☐ Implement Perfect Forward Secrecy (PFS) on all TLS connections
☐ Begin vendor engagement regarding PQC roadmaps
☐ Document quantum threat in organizational risk register
```

**Migration Roadmap (1-5 years):**

**Phase 1: Foundation (Year 1)**
- Deploy hybrid classical + post-quantum cryptography in test environments
- Pilot NIST-standardized PQC algorithms (Kyber, Dilithium)
- Evaluate performance impact and bandwidth requirements
- Update cryptography standards to include PQC requirements
- Train security team on post-quantum cryptography

**Phase 2: Critical Systems (Years 2-3)**
- Migrate PKI infrastructure to hybrid certificates
- Update authentication systems to quantum-resistant key exchange
- Re-encrypt long-term archives with AES-256 + PQC key wrapping
- Deploy quantum-resistant VPN and TLS configurations
- Implement PQC for API authentication and service mesh

**Phase 3: Full Migration (Years 3-5)**
- Complete organizational transition to PQC algorithms
- Decommission classical-only cryptographic systems
- Achieve compliance with emerging PQC regulations
- Continuous monitoring for new quantum threats

**Compensating Controls During Migration:**
```
☐ Reduce data retention periods where feasible
☐ Enhanced monitoring for bulk data exfiltration
☐ Network segmentation to limit "harvest now, decrypt later" exposure
☐ Implement additional encryption layers for highly sensitive data
☐ Accelerate migration timeline for most critical systems
```

---

### 5.2 Supply Chain Cryptographic Attack

**Scenario:** Cryptographic library or hardware component compromised in supply chain.

**Examples:**
- Backdoor in cryptographic library (OpenSSL, BoringSSL)
- Compromised random number generator in hardware
- Malicious firmware in HSM or cryptographic accelerator
- Trojanized certificate authority software

**Detection Indicators:**
```
☐ Anomalous cryptographic behavior in production
☐ Weak or predictable keys being generated
☐ Unexpected network connections from crypto components
☐ Security researcher disclosure or vendor notification
☐ Intelligence community warning
☐ Unusual entropy patterns in random number generation
```

**Immediate Response (0-4 hours):**
```
1. Isolate affected components
   ☐ Identify all systems using compromised component
   ☐ Network isolate suspected compromised systems
   ☐ Disable affected cryptographic operations if possible
   ☐ Switch to alternative cryptographic implementations

2. Assess compromise scope
   ☐ When was component deployed?
   ☐ What keys/certificates were generated using component?
   ☐ What data was protected by affected cryptography?
   ☐ Is there evidence of exploitation?

3. Evidence preservation
   ☐ Capture memory dumps from affected systems
   ☐ Preserve copies of compromised binaries
   ☐ Document component versions and configurations
   ☐ Save all relevant logs before rotation
```

**Remediation (4-48 hours):**
```
☐ Deploy verified clean version of cryptographic component
☐ Rotate ALL keys/certificates generated by compromised component
☐ Re-encrypt data that may have been compromised
☐ Update software supply chain verification procedures
☐ Implement binary verification and signing for crypto components
☐ Review and strengthen vendor security requirements
☐ Consider source code audit for critical crypto libraries
```

**Long-term Prevention:**
```
☐ Implement reproducible builds for cryptographic components
☐ Verify cryptographic library signatures before deployment
☐ Use multiple independent entropy sources for RNG
☐ Implement continuous cryptographic health monitoring
☐ Maintain diversity in cryptographic implementations (avoid single vendor)
☐ Participate in cryptographic component transparency initiatives
```

---

## 6. Communication and Reporting

### 6.1 Internal Communication Protocols

**Communication Channels by Severity:**

| Severity | Initial Notification | Ongoing Updates | Resolution Notice |
|----------|---------------------|-----------------|-------------------|
| **P1 - Critical** | Phone + Conference Bridge | Every 30 minutes | Email + Meeting |
| **P2 - High** | Phone + Email | Every 2 hours | Email |
| **P3 - Medium** | Email + Ticket | Daily | Ticket Update |
| **P4 - Low** | Ticket | As needed | Ticket Close |

**Stakeholder Notification Matrix:**

```
Executive Leadership (CISO, CIO, CTO):
- P1: Immediate phone notification
- P2: Within 1 hour via phone or email
- P3: Daily summary email
- P4: Weekly summary report

System Owners:
- All severities: Immediate notification via primary contact method
- Provide technical details and expected actions
- Include timeline and impact assessment

IT Operations:
- P1/P2: Immediate via on-call pager
- P3/P4: Email and ticket system
- Coordinate infrastructure changes

Legal/Compliance:
- P1/P2 with data exposure: Immediate notification
- Assess regulatory notification requirements
- Support breach notification process

Customer Success/Support:
- External-facing systems: Immediate notification
- Provide customer communication templates
- Coordinate customer outreach
```

### 6.2 External Communication

**Regulatory Notification Requirements:**

| Regulation | Notification Trigger | Timeline | Authority |
|------------|---------------------|----------|-----------|
| **GDPR** | Personal data breach | 72 hours | Data Protection Authority |
| **HIPAA** | PHI compromise | 60 days | HHS Office for Civil Rights |
| **PCI-DSS** | Cardholder data exposure | Immediate | Payment brands + acquirer |
| **State Breach Laws** | PII exposure (varies) | Varies by state | State AG, affected individuals |
| **SEC** | Material breach (public cos) | 4 business days | SEC, public disclosure |

**Customer Notification Template:**

```
Subject: Security Incident Notification - [Brief Description]

Dear [Customer],

We are writing to inform you of a security incident that may affect [service/data].

WHAT HAPPENED:
[Concise description of cryptographic incident without excessive technical detail]

WHAT INFORMATION WAS INVOLVED:
[Specific data types that may have been exposed]

WHAT WE ARE DOING:
[Actions taken to remediate and prevent recurrence]

WHAT YOU CAN DO:
[Specific actions customers should take, if any]
- Change passwords
- Monitor accounts
- Review access logs

FOR MORE INFORMATION:
Contact: [email/phone]
Reference Number: [incident ID]

We take the security of your data seriously and sincerely apologize for this incident.

Sincerely,
[Name, Title]
```

### 6.3 Incident Documentation

**Required Documentation:**

```
1. Incident Timeline (detailed)
   - Detection timestamp
   - All significant actions with timestamps
   - Decision points and rationale
   - Resolution timestamp

2. Technical Analysis
   - Root cause analysis
   - Attack vector or vulnerability description
   - Affected systems and data inventory
   - Forensic findings and evidence

3. Impact Assessment
   - Data exposed (volume, classification, types)
   - Systems affected and downtime
   - Business impact (financial, operational, reputational)
   - Compliance/regulatory impact

4. Response Actions
   - Containment measures
   - Eradication steps
   - Recovery procedures
   - Validation performed

5. Lessons Learned
   - What worked well
   - What could be improved
   - Process or tool gaps identified
   - Recommendations for future prevention

6. Appendices
   - Forensic reports
   - Log excerpts
   - Configuration changes
   - Communication records
```

---

## 7. Training and Awareness

### 7.1 Incident Response Team Training

**Required Training for IR Team:**

```
Annual Training Requirements:
☐ Cryptographic incident response procedures (this document)
☐ Cryptographic fundamentals and common vulnerabilities
☐ Incident response tabletop exercises (quarterly)
☐ Forensic evidence handling and chain of custody
☐ Communication during security incidents
☐ Legal and regulatory requirements
☐ Tool-specific training (HSM, PKI, monitoring tools)

Specialized Training:
☐ Post-quantum cryptography fundamentals
☐ Certificate lifecycle management
☐ Cryptographic protocol analysis (TLS, IPsec, etc.)
☐ Key management best practices
☐ Hardware security module operations
```

### 7.2 Tabletop Exercises

**Conduct quarterly tabletop exercises covering:**

**Scenario 1: Certificate Authority Compromise**
- Test coordination across multiple teams
- Practice certificate revocation and replacement
- Evaluate communication effectiveness

**Scenario 2: Encryption Key Exposure**
- Test data classification and impact assessment
- Practice regulatory notification procedures
- Evaluate re-encryption capabilities

**Scenario 3: Algorithm Vulnerability Disclosure**
- Test vulnerability assessment process
- Practice migration planning
- Evaluate vendor coordination

**Scenario 4: HSM Failure During Business Hours**
- Test failover procedures
- Practice business continuity
- Evaluate backup and recovery processes

**Exercise Evaluation Criteria:**
```
☐ Detection time acceptable?
☐ Containment effective?
☐ Communication clear and timely?
☐ Technical procedures followed correctly?
☐ Documentation adequate?
☐ Stakeholders properly engaged?
☐ Regulatory requirements understood?
```

---

## 8. Tools and Resources

### 8.1 Incident Response Tools

**Required Tools:**

```
Detection and Monitoring:
☐ Certificate monitoring (Cert-manager, Venafi, etc.)
☐ TLS/SSL scanner (SSLyze, testssl.sh, Qualys SSL Labs)
☐ Cryptographic vulnerability scanner (Nmap with SSL scripts)
☐ SIEM with cryptographic event correlation rules
☐ Network traffic analysis (Wireshark, tcpdump)
☐ Certificate Transparency log monitoring

Forensics and Analysis:
☐ Memory forensics tools (Volatility, Rekall)
☐ Disk forensics tools (Autopsy, FTK)
☐ Log analysis tools (ELK stack, Splunk)
☐ Cryptographic analysis tools (OpenSSL, cryptsetup)
☐ HSM audit log analysis tools

Response and Remediation:
☐ Certificate management platform
☐ Configuration management (Ansible, Terraform)
☐ Key rotation automation scripts
☐ Emergency certificate issuance process
☐ Backup HSM or software-based crypto as failover
```

### 8.2 Reference Materials

**Keep readily accessible:**

```
Technical References:
☐ Approved cryptographic standards (this policy)
☐ Certificate chain diagrams for your PKI
☐ HSM operational procedures
☐ Key management procedures
☐ Vendor support contact information
☐ System architecture diagrams

Regulatory References:
☐ GDPR breach notification requirements
☐ HIPAA breach notification rules
☐ PCI-DSS incident response requirements
☐ Industry-specific regulations
☐ Contractual notification obligations

Contact Lists:
☐ Incident response team roster with 24/7 contacts
☐ Vendor technical support (HSM, CA, crypto libraries)
☐ Legal counsel
☐ Public relations/communications
☐ Regulatory authority contacts
☐ Law enforcement (if applicable)
```

---

## 9. Continuous Improvement

### 9.1 Incident Metrics and Trends

**Track and analyze:**

```
Quarterly Metrics:
- Number of cryptographic incidents by severity
- Mean Time to Detect (MTTD)
- Mean Time to Contain (MTTC)
- Mean Time to Recover (MTTR)
- Incident recurrence rate
- False positive rate for cryptographic alerts

Annual Analysis:
- Trending incident types
- Root cause patterns
- Effectiveness of preventive controls
- Gaps in detection capabilities
- Training effectiveness
- Cost of incidents
```

### 9.2 Policy and Procedure Updates

**This appendix MUST be reviewed and updated:**

```
☐ Annually as part of policy review cycle
☐ After each P1 or P2 cryptographic incident
☐ When new cryptographic technologies are adopted
☐ When new regulations take effect
☐ When significant organizational changes occur
☐ After tabletop exercises identify gaps
```

### 9.3 Integration with Broader ISMS

**Ensure alignment with:**

```
☐ ISO 27001:2022 Control A.5.24 (Information security incident management planning and preparation)
☐ ISO 27001:2022 Control A.5.25 (Assessment and decision on information security events)
☐ ISO 27001:2022 Control A.5.26 (Response to information security incidents)
☐ ISO 27001:2022 Control A.5.27 (Learning from information security incidents)
☐ Organizational Business Continuity Plan
☐ Disaster Recovery Plan
☐ Crisis Communication Plan
```

---

## 10. Approval and Revision History

| Version | Date | Author | Changes | Approved By |
|---------|------|--------|---------|-------------|
| 1.0 | DD.MM.YYYY | [Name] | Initial version | [CISO] |
| | | | | |

## Appendices

### Appendix A: Incident Response Checklist (Quick Reference)

```
CRYPTOGRAPHIC INCIDENT RESPONSE - QUICK CHECKLIST

☐ DETECT & ASSESS (0-15 min)
  ☐ Classify severity (P1/P2/P3/P4)
  ☐ Identify affected systems and data
  ☐ Assess business impact
  ☐ Notify incident response team

☐ CONTAIN (15 min - 2 hours)
  ☐ Isolate affected systems if necessary
  ☐ Prevent further compromise
  ☐ Preserve forensic evidence
  ☐ Implement compensating controls

☐ ERADICATE (2-24 hours)
  ☐ Identify and remove root cause
  ☐ Rotate compromised cryptographic material
  ☐ Deploy patches or configuration changes
  ☐ Validate effectiveness

☐ RECOVER (24-48 hours)
  ☐ Restore systems with new crypto material
  ☐ Validate all systems functioning correctly
  ☐ Monitor for anomalies
  ☐ Communicate with stakeholders

☐ POST-INCIDENT (5 days)
  ☐ Conduct post-incident review
  ☐ Document lessons learned
  ☐ Update procedures as needed
  ☐ Implement preventive measures
```

### Appendix B: Cryptographic Incident Severity Matrix (Quick Reference)

| Factor | P1 - Critical | P2 - High | P3 - Medium | P4 - Low |
|--------|---------------|-----------|-------------|----------|
| **Scope** | Root CA or widespread compromise | Multiple production systems | Single production system | Isolated component or non-production |
| **Exploitation** | Active exploitation confirmed | High probability, exploit available | Possible exploitation, no active threats | Unlikely, theoretical only |
| **Data Impact** | Restricted data exposed or accessible | Confidential data at immediate risk | Internal data potentially affected | Public data or minimal sensitivity |
| **Business Impact** | Revenue loss, service outage, regulatory breach | Major service disruption, potential breach | Moderate disruption, degraded service | Minimal impact, no user visibility |
| **Compliance Impact** | Mandatory breach notification required | Regulatory reportable event likely | May require documentation | No regulatory impact |
| **Recovery Complexity** | Requires emergency coordination, widespread rotation | Multiple teams, coordinated changes | Standard change process, single team | Simple fix, minimal coordination |
| **Response Time** | **15 minutes** | **1 hour** | **4 hours** | **24 hours** |
| **Update Frequency** | Every 30 minutes | Every 2 hours | Daily | As needed |
| **Approval Required** | CISO + Senior Management | CISO or Security Manager | Security Team Lead | IT Manager |

**Severity Classification Examples:**

**P1 - Critical Examples:**
- Root CA private key compromised
- Production TLS/SSL private keys exposed publicly
- Encryption master key extracted by attacker
- Active MITM attack using forged certificates in production
- HSM physical breach with tamper evidence
- Widespread use of completely broken algorithm (e.g., MD5 for signatures)

**P2 - High Examples:**
- Certificate issued to unauthorized party
- Production system using SSLv3 or TLS 1.0 with active downgrade attacks
- Password database using broken hash (MD5, SHA-1 without salt)
- Encryption keys stored in plaintext in accessible location
- Multiple expired certificates causing authentication failures
- Key management system misconfiguration exposing keys

**P3 - Medium Examples:**
- Production certificate expiring within 7 days
- Non-compliant cipher suite in use (weak but not broken)
- Weak RSA key length detected (1024-bit in production)
- Missing certificate validation in internal application
- Self-signed certificate deployed in production without approval
- Incomplete certificate chain causing trust warnings

**P4 - Low Examples:**
- Certificate expiring in 30-90 days (within renewal window)
- Legacy algorithm present in configuration but not actively used
- Missing documentation for cryptographic implementation
- Non-production system using outdated TLS version
- Certificate monitoring alert not configured
- Cosmetic certificate issues (missing SAN, wrong order)

**Escalation Triggers:**

Incidents **MUST** be escalated to next higher severity if:
- Scope expands beyond initial assessment
- Evidence of active exploitation discovered
- Data classification higher than initially assessed
- Regulatory notification threshold crossed
- Containment unsuccessful within expected timeframe
- Public disclosure or media attention occurs

**De-escalation Criteria:**

Incidents **MAY** be de-escalated to lower severity if:
- Containment successful with no evidence of exploitation
- Scope smaller than initially assessed
- Effective compensating controls verified
- Data impact less severe than initially believed
- Business impact minimal after assessment

---

**End of Appendix C - Incident Response Framework for Cryptographic Events** 

*"In cryptography, broken is broken. There is no 'partially secure' or 'secure enough' when the algorithm fails."*  
*— The Binary Nature of Cryptographic Failure*