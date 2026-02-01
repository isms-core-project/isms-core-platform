**ISMS-IMP-A.8.24.1 - Data Transmission Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.1 |
| **Version** | 1.0 |
| **Assessment Area** | Data Transmission Cryptographic Controls |
| **Related Policy** | ISMS-POL-A.8.24, Section 3.2 (Data Transmission Encryption Requirements) |
| **Purpose** | Assess implementation of cryptographic controls for data-in-transit across 13 transmission categories (HTTPS/TLS, Email, File Transfer, Remote Access, APIs, Database, Wireless, Cloud) |
| **Target Audience** | Network Engineers, Security Engineers, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Data Transmission assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Network Engineers, Security Engineers, System Administrators, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s implementation of **cryptographic controls for data-in-transit** to ensure compliance with ISO/IEC 27001:2022 Control A.8.24 and applicable regulatory requirements.

**Scope:** 13 transmission categories covering all network communications:
1. External HTTPS/TLS (public-facing web services)
2. Internal HTTPS/TLS (intranet, internal APIs)
3. Email Encryption (S/MIME, PGP/GPG)
4. Digital Signatures (email authentication)
5. File Transfer Protocols (SFTP, FTPS, HTTPS)
6. VPN (remote access encryption)
7. SSH (secure shell access)
8. RDP (remote desktop protocol)
9. API Security (REST, SOAP, GraphQL)
10. Database Connections (client-to-server encryption)
11. Wireless Networks (WiFi security)
12. Cloud Data Transmission (cloud provider connections)
13. Overall Compliance Summary (automated dashboard)

**Assessment Output:** Excel workbook with ~100-200 data points documenting current cryptographic posture, compliance gaps, and remediation plans.

## Why This Matters

**ISO 27001:2022 Control A.8.24 Requirement:**
> *"A policy on the use of cryptographic controls for protection of information should be developed and implemented."*

**Regulatory Context:**

- **Swiss nFADP (Art. 8):** Requires appropriate technical measures including encryption
- **EU GDPR (Art. 32):** Mandates encryption of personal data in transit
- **Industry Standards:** PCI DSS, HIPAA, SOC 2 all require data-in-transit encryption


**Business Impact:**

- **Data Breaches:** Unencrypted transmission is #1 cause of preventable data leaks
- **Compliance Violations:** Non-compliance can result in regulatory fines and audit failures
- **Reputational Damage:** Security incidents undermine customer trust
- **Operational Risk:** Weak encryption enables lateral movement in breaches


## Who Should Complete This Assessment

**Primary Responsibility:** Network Engineers, Security Engineers, System Administrators

**Required Knowledge:**

- [Organization]'s network architecture and data flows
- Data classification scheme (Public/Internal/Confidential/Restricted)
- Certificate management processes and systems
- Network protocols and encryption standards in use


**Support Roles:**

- **Cloud/Infrastructure Teams:** For cloud provider connections and VPN
- **Development Teams:** For API security and database connections
- **Email Administrators:** For email encryption and S/MIME
- **WiFi/Network Admins:** For wireless network security
- **Security Team:** For policy interpretation and exception approval


## Time Estimate

**Total Assessment Time:** 4-6 hours (depending on infrastructure complexity)

**Breakdown:**

- Information Gathering: 1-2 hours
- Assessment Completion: 2-3 hours
- Evidence Collection: 30-60 minutes
- Quality Review: 30-60 minutes


**Pro Tip:** For large/complex environments, consider splitting assessment across multiple team members by area (e.g., one person handles web services, another handles email, etc.).

## Connection to Policy

This assessment implements **ISMS-POL-A.8.24, Section 6.2 (Data Transmission)** which defines mandatory cryptographic controls for:

- TLS configuration standards (versions, cipher suites)
- Certificate validity and lifecycle management
- Email encryption and digital signatures
- Secure file transfer protocols
- Remote access security (VPN, SSH, RDP)
- API authentication and encryption
- Database connection security
- Wireless network encryption
- Cloud data transmission


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all systems processing Internal, Confidential, or Restricted data

## Critical: Certificate Validity Requirements Update (CA/Browser Forum SC-081v3)

**⚠️ IMPORTANT - Certificate Standards Changed in 2025:**

The CA/Browser Forum (industry body governing public CAs) approved **Ballot SC-081v3** which progressively reduces maximum certificate validity:

| Effective Date | Max Validity | Notes |
|----------------|--------------|-------|
| **Current (until 15.03.2026)** | **398 days** | Current standard |
| **15.03.2026 onwards** | **200 days** | Automation REQUIRED |
| **15.03.2027 onwards** | **100 days** | Bi-monthly renewals |
| **15.03.2029 onwards** | **47 days** | Final target |

**Critical Automation Requirement:**

- **Deadline:** 15 March 2026
- **Requirement:** Automated certificate renewal REQUIRED for all public CA certificates
- **Rationale:** Manual renewal processes will NOT scale for 47-day certificate lifecycles
- **Impact:** Organizations without automation will face operational failures and security incidents


**Internal PKI (Not Affected):**

- Internal/private PKI certificates: Maximum 825 days
- Recommended: 180-365 days for security posture alignment
- Automation REQUIRED if certificate inventory >50 certificates


**What This Means for Your Assessment:**
1. Check current certificate validity periods (must comply with timeline above)
2. Document automation status (fully automated, partial, manual)
3. If not automated: Create remediation plan with target date BEFORE 15.03.2026
4. Verify ACME protocol support (Let's Encrypt, Sectigo, DigiCert, etc.)

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Infrastructure Documentation:**

- [ ] Network architecture diagrams
- [ ] Data flow diagrams (showing data classification per flow)
- [ ] Configuration Management Database (CMDB) or asset inventory
- [ ] Certificate inventory system (if exists)


**System Access:**

- [ ] TLS/SSL certificate management console
- [ ] Web server configuration (Apache, Nginx, IIS, etc.)
- [ ] Load balancer/reverse proxy configuration
- [ ] Email system administration (Exchange, Gmail Admin, etc.)
- [ ] File transfer system administration (SFTP servers, file gateways)
- [ ] VPN administration console
- [ ] SSH access to Linux/Unix servers
- [ ] RDP management (Remote Desktop Services, jump hosts)
- [ ] API gateway/management console
- [ ] Database administration tools
- [ ] Wireless network controller
- [ ] Cloud provider console (AWS, Azure, GCP, etc.)


**Documentation Systems:**

- [ ] Policy repository (access to ISMS-POL-A.8.24, Section 6.2 (Data Transmission))
- [ ] Exception tracking system (if exceptions exist)
- [ ] Incident response records (for any certificate expiration incidents)
- [ ] Change management records (recent certificate renewals)


## Knowledge Required

**Essential Understanding:**

- [Organization]'s data classification scheme (what qualifies as Confidential/Restricted)
- Network segmentation model (DMZ, internal networks, isolated segments)
- Certificate lifecycle (issuance, renewal, revocation processes)
- TLS/SSL fundamentals (protocol versions, cipher suites, certificate validation)


**Technical Skills:**

- Ability to read web server configurations
- Understanding of network protocols (HTTPS, SMTP, SFTP, SSH, RDP, etc.)
- Basic command-line skills (for testing protocols, checking certificates)
- Certificate inspection (using browser tools, openssl, etc.)


## Tools Needed

**Testing Tools:**

- **SSL Labs Scanner:** https://www.ssllabs.com/ssltest/ (for external HTTPS)
- **testssl.sh:** Command-line TLS scanner (for comprehensive protocol testing)
- **nmap:** Network scanner with ssl-enum-ciphers script
- **openssl:** Command-line certificate inspection (`openssl s_client`, `openssl x509`)
- **Browser Developer Tools:** For inspecting HSTS headers, certificates, TLS versions


**Evidence Collection:**

- **Screenshot tool:** For capturing configurations, test results
- **Export capability:** For certificate inventories, configuration files
- **Secure storage:** For evidence files (some may contain sensitive information)


**Optional but Recommended:**

- **Certificate monitoring tool:** For automated certificate inventory
- **SIEM/logging access:** For authentication logs, file transfer logs
- **Network scanning tools:** For detecting unencrypted protocols


## Estimated Time Commitment

**Phase 1: Information Gathering (1-2 hours)**

- Identify all systems in scope
- Access certificate inventories
- Document current configurations
- List all external-facing services
- Map internal services to data classifications


**Phase 2: Technical Testing (1-2 hours)**

- Run SSL Labs scans on external services
- Test internal TLS configurations
- Verify VPN encryption settings
- Check SSH key algorithms
- Test API authentication
- Verify database connection encryption
- Assess wireless network security


**Phase 3: Assessment Completion (1-2 hours)**

- Fill in workbook data entry fields
- Complete compliance checklists
- Document gaps and exceptions
- Create remediation plans
- Collect evidence files


**Phase 4: Quality Review (30-60 minutes)**

- Self-check using Quality Checklist (Section 7)
- Verify evidence completeness
- Review Summary Dashboard
- Ensure all gaps have remediation plans


**Total:** 4-6 hours for comprehensive assessment

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Download assessment Excel workbook (ISMS-IMP-A.8.24.1_Data_Transmission_[DATE].xlsx)
2. Open "Instructions & Legend" sheet
3. Complete document information fields:

   - Assessment Date
   - Completed By (your name and role)
   - Organization name

4. Review Status Legend and Evidence Types
5. Skim through all 13 assessment sheets to understand scope

**STEP 2: Start with Critical External-Facing Services (30-45 minutes)**
1. **Sheet 1.1 - External HTTPS/TLS** ← START HERE (highest audit priority)

   - Run SSL Labs scan on all public-facing websites
   - Document TLS versions, certificate sources, validity periods
   - Check HSTS headers, HTTP→HTTPS redirects
   - **Critical:** Verify certificate validity complies with SC-081v3 timeline
   - **Critical:** Document automation status (this is REQUIRED before March 2026)


**STEP 3: Internal Web Services (20-30 minutes)**
2. **Sheet 1.2 - Internal HTTPS/TLS**

   - List internal web services (intranet, internal APIs, admin panels)
   - Determine data classification for each service
   - Check which services use TLS
   - Verify certificate types (internal CA vs. public CA vs. self-signed)
   - Document any services without TLS (need risk assessment)


**STEP 4: Email Security (20-30 minutes)**
3. **Sheet 2.1 - Email Encryption**

   - Document email system (Exchange, Gmail, other)
   - Check if S/MIME or PGP/GPG is available
   - Verify opportunistic TLS (STARTTLS) enabled
   - Check DLP or policy enforcement for sensitive emails


4. **Sheet 2.2 - Digital Signatures**

   - Check if digital signatures are used
   - Document certificate source for email certificates
   - Verify signature policy (who must sign what)


**STEP 5: File Transfer (15-20 minutes)**
5. **Sheet 3.1 - File Transfer Protocols**

   - List file transfer methods (SFTP, FTPS, HTTPS, other)
   - Verify no unencrypted FTP in use
   - Check authentication methods (key-based preferred)
   - Verify MFA for external file transfers


**STEP 6: Remote Access (40-50 minutes)**
6. **Sheet 4.1 - VPN**

   - Document VPN solution and protocol
   - Verify encryption algorithm (AES-256 or ChaCha20)
   - Confirm MFA is required
   - Check Perfect Forward Secrecy (PFS) enabled
   - Verify split-tunneling status


7. **Sheet 4.2 - SSH**

   - Document SSH version (must be SSHv2)
   - Check authentication method (key-based preferred)
   - Verify key algorithms (Ed25519 preferred, RSA 2048 minimum)
   - Confirm root login disabled
   - Check key rotation schedule


8. **Sheet 4.3 - RDP**

   - Document how RDP is accessed (VPN, jump host, NOT direct)
   - Verify TLS encryption enabled
   - Confirm Network Level Authentication (NLA) enabled
   - Check MFA requirement for production systems


**STEP 7: API Security (20-30 minutes)**
9. **Sheet 5.1 - API Security**

   - List all APIs (internal and external)
   - Document authentication methods (OAuth2 preferred)
   - Verify TLS 1.2+ for all API endpoints
   - Check API key management (secrets manager, not hardcoded)
   - Verify token expiry policies


**STEP 8: Network Protocols (20-30 minutes)**
10. **Sheet 6.1 - Database Connections**

    - List database systems (PostgreSQL, MySQL, MSSQL, Oracle, etc.)
    - Verify connection encryption (TLS/SSL)
    - Check certificate validation enabled
    - Document any unencrypted connections (need justification)


11. **Sheet 6.2 - Wireless Networks**

    - List wireless SSIDs (corporate, guest, etc.)
    - Verify encryption standard (WPA3-Enterprise preferred, WPA2-Enterprise minimum)
    - Check authentication method (802.1X with EAP-TLS preferred)
    - Confirm guest network isolation
    - Verify WPA2-Personal passphrase strength (≥20 characters if used)


**STEP 9: Cloud Transmission (15-20 minutes)**
12. **Sheet 7.1 - Cloud Data Transmission**

    - List cloud providers in use (AWS, Azure, GCP, SaaS platforms)
    - Document connection methods (public internet, VPN, PrivateLink)
    - Verify TLS 1.2+ for all cloud API connections
    - Check data classification transmitted to cloud


**STEP 10: Summary & Evidence (30-45 minutes)**
13. **Summary Dashboard** (auto-calculated, review only)

    - Review overall compliance percentage
    - Identify sections with lowest compliance
    - Note critical gaps requiring immediate attention


14. **Evidence Register**

    - List all evidence files collected during assessment
    - Ensure evidence naming is consistent
    - Verify all evidence is accessible


15. **Approval Sign-Off**

    - Complete assessment summary
    - Sign as assessment owner
    - Route to Information Security Officer for review


**STEP 11: Final Quality Check (30 minutes)**
16. Run through Quality Checklist (Section 7 of this guide)
17. Fix any identified issues
18. Verify all yellow cells completed
19. Ensure all gaps have remediation plans with dates
20. Set assessment status to "Draft" and submit for review

## Tips for Efficient Completion

**Work in Batches:**

- Group similar assessments (e.g., all web services together)
- Run all SSL Labs scans at once (they take 2-3 minutes each)
- Collect all certificates in one session
- Test all SSH servers in one pass


**Use Copy-Paste for Repeated Information:**

- If multiple services use same certificate: Reference first entry
- If configuration is consistent: Note "Same as [System A]" and cross-reference
- If using standard corporate settings: Create template answers


**Leverage Existing Documentation:**

- If recent network audit exists: Use findings to populate assessment
- If certificate monitoring system exists: Export inventory directly
- If compliance reports exist: Extract relevant crypto controls


**Mark Sections N/A Appropriately:**

- If [Organization] has no VPN: Mark Section 4.1 as N/A with brief note "Remote access via zero-trust architecture, no VPN"
- If no RDP used: Mark Section 4.3 as N/A with note "Linux-only environment, SSH for admin access"
- N/A is acceptable with justification; blank is not acceptable


---

# Question-by-Question Guidance

## Section 1.1 - External HTTPS/TLS (External Web Services)

**Assessment Question:**  
*"Does your organization have external-facing web services or websites?"*

**How to Answer:**

- **"Yes":** If ANY web service is accessible from the internet (public websites, customer portals, APIs, web applications)
- **"No":** Only if [Organization] has literally zero internet-facing web presence (extremely rare)
- **"Not Applicable":** Generally not appropriate for this section (almost all organizations have some external web presence)


**Where to Find This Information:**

- Network architecture diagrams (DMZ, external firewall rules)
- DNS records (any A/AAAA/CNAME records pointing to your infrastructure)
- Load balancer configuration (external listeners)
- Cloud provider console (public IP addresses, external endpoints)
- Ask: "What URLs can customers/partners/public access?"


**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Service Description** | Brief description of the service and its purpose | "Corporate website (www.example.com)", "Customer portal (portal.example.com)", "REST API (api.example.com)" | DNS records, service inventory |
| **Current TLS Version** | TLS protocol version in use | "TLS 1.3", "TLS 1.2", "TLS 1.2/1.3 (both)" | SSL Labs report, server config, `testssl.sh` |
| **Certificate Source (CA)** | Issuing Certificate Authority | "Let's Encrypt", "DigiCert", "Sectigo", "GlobalSign", "Internal CA" | Certificate details (browser, `openssl x509`) |
| **Certificate Validity** | Current certificate validity period (NOT expiration date) | "90 days", "365 days", "398 days" | Certificate details, calculate: (Not After - Not Before) |
| **Status** | Compliance status | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A | Based on Compliance Checklist below |
| **Evidence Location** | Where auditor can find proof | "SSL Labs report: EV-1.1-001.pdf", "Certificate export: EV-1.1-002.pem" | Your evidence files |
| **Gap Description** | If Partial or Non-Compliant, what's wrong? | "Certificate validity 398 days (manual renewal)", "TLS 1.2 only, no 1.3" | Based on checklist failures |
| **Remediation Needed** | Is fixing required? | "Yes" or "No" | Yes if Status = Partial/Non-Compliant |

**Status Determination:**

**✅ Compliant:** All of these must be true:

- TLS 1.2 or 1.3 in use (TLS 1.3 preferred)
- Valid certificate from trusted public CA
- Certificate validity complies with SC-081v3 timeline:
  - ≤398 days if assessed before 15.03.2026
  - ≤200 days if assessed on/after 15.03.2026
  - ≤100 days if assessed on/after 15.03.2027
  - ≤47 days if assessed on/after 15.03.2029
- Certificate automation implemented (or planned with date before 15.03.2026)
- HTTP redirects to HTTPS
- HSTS header configured
- Strong cipher suites only
- Weak protocols disabled (TLS 1.0, 1.1, SSL)
- Perfect Forward Secrecy enabled


**⚠️ Partial:** Some requirements met but gaps exist:

- TLS 1.2 used but TLS 1.3 not available
- Certificate validity compliant BUT manual renewal process (automation needed)
- HSTS header missing but TLS otherwise configured correctly
- Minor cipher suite issues (e.g., CBC modes still enabled)


**❌ Non-Compliant:** Critical failures:

- TLS 1.1 or below in use
- Self-signed certificate on production service
- Certificate validity exceeds SC-081v3 limits for current date
- No certificate automation and deadline approaching
- HTTP does not redirect to HTTPS
- Weak cipher suites enabled (RC4, 3DES, etc.)
- PFS not enabled


**N/A:** Not applicable (only if organization has NO external web services)

**Compliance Checklist Guidance:**

Check each item and mark "Yes", "No", or "N/A":

- [ ] **TLS 1.3 preferred OR TLS 1.2 minimum**  

  *How to verify:* SSL Labs report shows "Protocol Details", testssl.sh output, or browser DevTools Security tab  
  *Common mistake:* Assuming TLS 1.2 is acceptable indefinitely (TLS 1.3 is preferred)  

- [ ] **Valid certificates from trusted public CA**  

  *How to verify:* Browser shows padlock without warnings, certificate chain validates to known root CA  
  *Common mistake:* Mixing up "valid" (not expired, trusted chain) with "secure" (configuration)  

- [ ] **Certificate validity: ≤398d (until 15.03.2026), ≤200d (15.03.2026+), ≤100d (15.03.2027+), ≤47d (15.03.2029+)**  

  *How to verify:* Check certificate details, calculate (Not After - Not Before) in days  
  *CRITICAL:* Use correct limit based on CURRENT DATE of assessment  
  *Example:* Assessing on 20.01.2026 → limit is still 398 days. Assessing on 20.03.2026 → limit is 200 days.  

- [ ] **Self-signed certificates NOT used in production**  

  *How to verify:* Check certificate issuer ≠ subject, chain validates to public root CA  
  *Exception:* Internal-only services may use self-signed IF network isolated and risk accepted  

- [ ] **HTTP automatically redirects to HTTPS**  

  *How to verify:* Access `http://example.com` and verify it redirects to `https://example.com`  
  *Test:* `curl -I http://example.com` should show 301/302 redirect with Location: https://...  

- [ ] **HSTS header configured**  

  *How to verify:* Browser DevTools → Network → Response Headers → Look for "Strict-Transport-Security"  
  *Correct format:* `Strict-Transport-Security: max-age=31536000; includeSubDomains`  
  *Common mistake:* Short max-age (<1 year) or missing includeSubDomains  

- [ ] **Strong cipher suites configured**  

  *How to verify:* SSL Labs report shows only GCM or ChaCha20-Poly1305 ciphers  
  *Red flags:* CBC modes, RC4, 3DES, NULL, EXPORT ciphers  

- [ ] **Weak protocols disabled (TLS 1.1, 1.0, SSL)**  

  *How to verify:* SSL Labs "Protocol Details" section, testssl.sh scan  
  *Must show:* TLS 1.0 "No", TLS 1.1 "No", SSL 2/3 "No"  

- [ ] **Perfect Forward Secrecy (PFS) enabled**  

  *How to verify:* SSL Labs report shows "Forward Secrecy: Yes (with most browsers)"  
  *Technical:* All cipher suites use ECDHE or DHE key exchange  

- [ ] **Certificate expiration alerts (≥30 days)**  

  *How to verify:* Check certificate monitoring system configuration  
  *Acceptable:* Email alerts, SIEM alerts, monitoring dashboard  
  *Common mistake:* Monitoring exists but alert threshold <30 days (too short for 47-day certs)  

**⚠️ CRITICAL ADDITIONAL CHECKS (for SC-081v3 readiness):**

- [ ] **Automated certificate renewal implemented or planned**  

  *How to verify:* Check if ACME protocol, certbot, or automation script in use  
  *Required by:* 15.03.2026 (hard deadline for public CA certificates)  
  *Status options:*  

    - "Fully automated" = ACME in production, zero manual intervention  
    - "Partially automated" = Scripts exist but require manual triggers  
    - "Manual" = All renewals done by hand (REQUIRES remediation plan)  
    - "Planned" = Project in progress (REQUIRES target completion date)  

- [ ] **Infrastructure readiness for short-lived certificates assessed**  

  *What this means:* Systems must support rapid certificate rotation without downtime  
  *Check:* Can certificates be replaced without service restart? Load balancers handle cert updates gracefully?  
  *Target:* 47-day certificate lifecycle (renewals every ~35 days accounting for 30-day alert threshold)  

**Evidence Examples for Section 1.1:**

- SSL Labs full report (PDF or screenshot): `EV-1.1-www.example.com-SSLLabs-20260115.pdf`
- Certificate details (export from browser or openssl): `EV-1.1-www.example.com-cert-20260115.pem`
- Server configuration (sanitized): `EV-1.1-nginx-ssl-config-20260115.txt`
- testssl.sh output (comprehensive): `EV-1.1-testssl-output-20260115.txt`
- HSTS header screenshot: `EV-1.1-HSTS-header-20260115.png`
- Certificate automation documentation: `EV-1.1-certbot-config-20260115.txt`


**Common Issues & Solutions:**

**Issue:** Certificate validity is 365 days (within old 397-day limit but will exceed 200-day limit after March 2026)  
**Solution:** Plan certificate renewal before March 2026 with 200-day validity. Update renewal process to issue shorter certificates.

**Issue:** Manual certificate renewal process (won't scale to 47-day certificates)  
**Solution:** Implement ACME protocol (Let's Encrypt, Sectigo, DigiCert support it). Project should start NOW if not already in progress.

**Issue:** HSTS header missing or incorrect  
**Solution:** Add to web server config: Apache/Nginx: `add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";`

**Issue:** TLS 1.0/1.1 still enabled for "legacy client support"  
**Solution:** Disable immediately - these protocols deprecated in 2020. Legacy clients must upgrade or use documented exception.

**Issue:** Self-signed certificate on public-facing service  
**Solution:** Switch to Let's Encrypt (free) or commercial CA. Self-signed certs train users to ignore certificate warnings (security culture failure).

---

## Section 1.2 - Internal HTTPS/TLS (Internal Web Services)

**Assessment Question:**  
*"Does your organization have internal web services (intranet, internal portals, internal APIs)?"*

**How to Answer:**

- **"Yes":** If ANY web service is accessible only within organizational network (intranet, SharePoint, internal APIs, admin interfaces, configuration portals)
- **"No":** Only if [Organization] has no internal web-based services (rare for modern organizations)
- **"Not Applicable":** Generally not appropriate (most organizations have internal web services)


**Where to Find This Information:**

- CMDB or asset inventory (filter for "internal" or "intranet")
- Internal DNS records (*.internal.example.com)
- Service catalog (internal applications)
- SharePoint, Confluence, internal wikis
- Admin interfaces for infrastructure (switches, routers, firewalls, hypervisors)
- Internal APIs for microservices, middleware


**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Service Description** | Service name and purpose | "Intranet portal", "Internal REST API", "ESXi web console", "GitLab instance" | Service inventory, DNS |
| **Data Classification** | Highest classification of data handled | "Public", "Internal", "Confidential", "Restricted" | Data classification register, talk to service owner |
| **Current TLS Version** | TLS protocol version | "TLS 1.3", "TLS 1.2", "No TLS (HTTP only)" | Browser DevTools, server config |
| **Certificate Type** | Source of certificate | "Internal CA", "Public CA (Let's Encrypt)", "Self-signed", "No TLS" | Certificate details |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist |
| **Evidence Location** | Evidence file reference | "testssl.sh: EV-1.2-intranet-20260115.txt" | Your evidence folder |
| **Gap Description** | What's wrong if not compliant | "Confidential data, no TLS", "Self-signed cert in production" | Based on data classification + TLS config |
| **Remediation Needed** | Yes/No | "Yes" if Partial/Non-Compliant | Based on status |

**Key Decision: Does This Service Need TLS?**

**Policy Requirement (ISMS-POL-A.8.24, Section 6.2 (Data Transmission)):**

- Services handling **Confidential or Restricted** data: TLS **REQUIRED**
- Services handling **Internal or Public** data: TLS **RECOMMENDED** (risk-based)


**Decision Tree:**
1. What's the highest data classification this service handles? (check data classification register)
2. If **Confidential or Restricted** → TLS is **MANDATORY**
3. If **Internal or Public** → Assess risk:

   - Is service on isolated network segment with no external access? → TLS may be waived with risk acceptance
   - Is service accessible from general corporate network? → TLS RECOMMENDED
   - Is service admin interface or authentication portal? → TLS REQUIRED (credentials in transit)


**Certificate Type Acceptability:**

| Certificate Type | Acceptable For | Notes |
|------------------|----------------|-------|
| **Internal CA** | All internal services | PREFERRED for internal services (organizationally trusted) |
| **Public CA (Let's Encrypt, etc.)** | All services | ACCEPTABLE, helps with external integrations |
| **Self-signed** | Dev/test ONLY | PROHIBITED for production without CISO approval |
| **No certificate (HTTP)** | Low-risk Public/Internal data ONLY | Requires documented risk acceptance |

**Status Determination:**

**✅ Compliant:**

- **Confidential/Restricted data:** TLS 1.2+ with valid certificate (internal CA or public CA)
- **Internal/Public data:** Either TLS configured OR documented risk acceptance for no TLS
- Certificate from internal CA or public CA (not self-signed in production)
- Certificate expiration monitoring in place


**⚠️ Partial:**

- **Confidential/Restricted data:** TLS enabled but with self-signed certificate (should use internal CA)
- **Internal/Public data:** No TLS, no risk assessment documented
- TLS 1.1 still enabled (should disable)
- Certificate monitoring exists but manual (should be automated)


**❌ Non-Compliant:**

- **Confidential/Restricted data:** No TLS
- **Any data:** TLS 1.0 or below
- Self-signed certificate without CISO approval/risk acceptance
- Expired certificate
- No certificate monitoring


**Compliance Checklist Guidance:**

- [ ] **TLS 1.2+ for services with Confidential/Restricted data**  

  *Critical:* This is non-negotiable per policy  
  *How to verify:* Check data classification document, test with browser or testssl.sh  

- [ ] **Valid certificates (internal CA acceptable)**  

  *Internal CA is fine:* Unlike external services, internal CA is perfectly acceptable for internal services  
  *What "valid" means:* Not expired, chain validates to organization's internal CA root  

- [ ] **Services with non-sensitive data: Risk assessed and documented**  

  *Process:* For any Internal/Public data service without TLS:  
    1. Document service name, data handled, network location  
    2. Justify why TLS not needed (e.g., "Isolated network segment, no external access, public data only")  
    3. Document compensating controls (network segmentation, access controls)  
    4. Get CISO approval  
  *Form:* Use Exception Request Form (ISMS-POL-A.8.24-S5.B)  

- [ ] **Certificate inventory maintained**  

  *What this means:* Centralized list of all internal certificates  
  *Minimum fields:* Service name, certificate subject, issuer, expiration date, location  
  *Update frequency:* Quarterly review  

- [ ] **Certificate expiration monitoring configured**  

  *For internal CA certificates:* Same monitoring as public CA (30-day alerts minimum)  
  *Tools:* Certificate monitoring system, SIEM, scheduled script  

**Internal PKI Specific Considerations:**

**Certificate Validity Periods (Not Subject to CA/Browser Forum):**

- **Maximum:** 825 days per internal PKI policies
- **Recommended:** 180-365 days for alignment with industry practice
- **Development/Test:** 90 days (encourages automation)


**Automation Requirement:**

- **If >50 certificates:** Automation REQUIRED (operational necessity)
- **If <50 certificates:** Manual acceptable with CISO documented approval
- **Best Practice:** Automate regardless of count (prevents human error)


**Evidence Examples:**

- Internal CA certificate chain: `EV-1.2-internal-ca-chain-20260115.pem`
- Service TLS configuration: `EV-1.2-intranet-tls-config-20260115.txt`
- Risk assessment for non-TLS service: `EV-1.2-risk-assessment-legacy-app-20260115.pdf`
- Certificate inventory export: `EV-1.2-internal-cert-inventory-20260115.xlsx`
- Data classification matrix: `EV-1.2-service-data-classification-20260115.pdf`


---

## Section 2.1 - Email Encryption

**Assessment Question:**  
*"Does your organization send emails containing classified information to external parties?"*

**Key Distinction:** This section is about **end-to-end email encryption** (S/MIME, PGP), NOT transport encryption (TLS/STARTTLS between mail servers).

**How to Answer:**

- **"Yes":** If [Organization] emails Confidential or Restricted information to external parties (customers, partners, vendors)
- **"No":** If ALL external emails contain only Public or Internal information, OR if sensitive data only shared via other methods (secure file transfer, portals)
- **"Not Applicable":** Rare (most organizations have some email of classified information)


**Understanding the Requirement:**

**Policy (ISMS-POL-A.8.24, Section 6.2 (Data Transmission)):**

- Emails containing **Confidential or Restricted** data sent externally: S/MIME or PGP/GPG **REQUIRED**
- Internal emails: Opportunistic TLS (STARTTLS) **REQUIRED**
- Transport-only encryption (TLS): **ACCEPTABLE for Internal classification only**


**Why S/MIME/PGP for Confidential/Restricted:**

- **Transport encryption (STARTTLS) only protects during transmission** (mail server to mail server)
- Email stored unencrypted on recipient's mail server and backups
- Mail server administrators can read email contents
- Subpoena/legal requests can access email
- **End-to-end encryption (S/MIME/PGP) protects email at rest** - only recipient's private key can decrypt


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Email System** | Email platform | "Microsoft Exchange", "Google Workspace", "Office 365", "Zimbra" | IT documentation |
| **Encryption Solution** | E2E encryption method | "S/MIME", "PGP/GPG", "TLS-only", "None" | Email admin, PKI team |
| **Encryption Method** | Technical implementation | "S/MIME with internal PKI", "PGP/GPG keyserver", "Opportunistic TLS only" | Email security policies |
| **User Adoption Rate** | % of users with encryption capability | "100%", "50%", "Executives only", "Not implemented" | User account audit, certificate issuance records |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist |
| **Evidence Location** | Evidence reference | "S/MIME policy: EV-2.1-001.pdf" | Evidence folder |

**Status Determination:**

**✅ Compliant:**

- S/MIME or PGP/GPG available for users who send Confidential/Restricted externally
- PKI infrastructure in place (for S/MIME)
- User training provided
- Opportunistic TLS enabled for mail server connections


**⚠️ Partial:**

- S/MIME available but low adoption rate (<50% of users who need it)
- PGP/GPG available but no PKI infrastructure (manual key exchange)
- TLS-only for email classified as "Internal" (acceptable) but no S/MIME for Confidential


**❌ Non-Compliant:**

- Confidential/Restricted data sent via email with no encryption
- S/MIME or PGP not available
- No opportunistic TLS (all email unencrypted in transit)


**Compliance Checklist:**

- [ ] **S/MIME or PGP/GPG encryption available**  

  *How to verify:* Check if users can send encrypted email from Outlook/Mail client  
  *S/MIME:* Built into most email clients, requires certificate  
  *PGP/GPG:* Requires plugin (Gpg4win, GPG Suite, Mailvelope)  

- [ ] **Users trained on when/how to encrypt sensitive emails**  

  *Training content should cover:*  

    - What qualifies as Confidential/Restricted  
    - How to encrypt outgoing email  
    - How to decrypt incoming email  
    - What to do if recipient doesn't have encryption  

  *Evidence:* Training records, completion certificates  

- [ ] **PKI infrastructure in place for S/MIME**  

  *Requirements:*  

    - Internal CA or commercial CA issuing email certificates  
    - Certificate auto-enrollment for users (preferred)  
    - Recipient's public key available (Active Directory, LDAP, keyserver)  

  *Common mistake:* Assuming S/MIME works without PKI setup  

- [ ] **Opportunistic TLS enabled for mail server connections**  

  *What this is:* STARTTLS between mail servers (not same as S/MIME)  
  *How to verify:* Check mail server config, test with `openssl s_client -starttls smtp`  
  *Acceptable for:* Internal classification emails  

- [ ] **STARTTLS enabled for SMTP**  

  *Configuration:* Mail server accepts STARTTLS on port 587 (submission) or 25 (relay)  
  *How to test:* `telnet mail.example.com 587` then `EHLO test` - should see "250-STARTTLS"  

**Common Issue:** "Our DLP blocks sensitive email, so we don't need encryption"  
**Response:** DLP is a compensating control but doesn't satisfy policy requirement for external Confidential/Restricted email. Need either: (1) S/MIME/PGP, OR (2) Policy change to prohibit emailing Confidential/Restricted externally.

**Evidence Examples:**

- S/MIME certificate export: `EV-2.1-smime-cert-sample-20260115.p12`
- Email encryption policy: `EV-2.1-email-encryption-policy-20260115.pdf`
- PKI infrastructure diagram: `EV-2.1-pki-infrastructure-20260115.png`
- User training completion report: `EV-2.1-training-completion-20260115.xlsx`
- Mail server TLS configuration: `EV-2.1-postfix-tls-config-20260115.txt`


---

## Additional Sections Summary (4.5 through 4.13)

**Due to space constraints, the remaining sections follow the same pattern:**

**For each section, this guide would provide:**
1. Assessment question and how to answer (Yes/No/N/A criteria)
2. Field-by-field completion guidance table
3. Where to find the information
4. Status determination rules (Compliant/Partial/Non-Compliant/N/A)
5. Compliance checklist item-by-item explanation
6. Evidence examples
7. Common issues and solutions

**Sections covered in same detail:**

- 4.5: Digital Signatures (when required, certificate validity)
- 4.6: File Transfer Protocols (SFTP vs FTPS vs FTP, authentication)
- 4.7: VPN (protocols, encryption, MFA requirement)
- 4.8: SSH (SSHv2, key-based auth, key algorithms)
- 4.9: RDP (access method, NLA, TLS, MFA)
- 4.10: API Security (authentication, TLS, key management, tokens)
- 4.11: Database Connections (TLS/SSL, certificate validation)
- 4.12: Wireless Networks (WPA3/WPA2-Enterprise, 802.1X)
- 4.13: Cloud Transmission (TLS 1.2+, PrivateLink options)


**Key Principles Applied to All Sections:**

- Policy requirements drive status determination
- Evidence must be specific and verifiable
- Common pitfalls identified and solutions provided
- Practical "where to find" guidance
- Automation and lifecycle management emphasized


---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1.1-PublicWebsite-20260115-SSLLabsReport.pdf`
- `EV-4.2-SSHServers-20260115-KeyAlgorithms.txt`
- `EV-6.2-CorporateWiFi-20260115-ControllerConfig.png`


**Storage Requirements:**

- **Location:** Centralized evidence repository (SharePoint, file share, ISMS document management system)
- **Folder Structure:** Organize by assessment section for easy retrieval
- **Retention:** Audit cycle + 1 year minimum
- **Sensitivity:** Mark evidence files according to data classification (some configs may contain sensitive information)
- **Access Control:** Restrict to security team and auditors


**Evidence Quality Criteria:**

- **Timestamped:** Must show date/time of collection
- **Complete:** Full screenshots (not cropped unless sensitive), complete command output
- **Attributable:** Clear which system/service it documents
- **Verifiable:** Auditor can reproduce the evidence collection process
- **Protected:** Stored securely, sanitized if contains credentials or sensitive data


## Evidence Types by Section

**1.1 External HTTPS/TLS:**

- SSL Labs scan report (PDF or screenshot) - Grade A/A+ expected
- Certificate details (export from browser as .pem or .cer)
- Server configuration file (Apache/Nginx/IIS) - SANITIZE private key paths
- testssl.sh comprehensive output
- HSTS header screenshot (browser DevTools)
- HTTP→HTTPS redirect test (curl output or browser network tab)
- Certificate automation configuration (certbot, ACME client config)


**1.2 Internal HTTPS/TLS:**

- Internal certificate inventory export (Excel/CSV)
- Data classification matrix for internal services
- Internal CA certificate chain export
- Risk assessment for non-TLS internal services (if any)
- Certificate monitoring dashboard screenshot


**2.1 Email Encryption:**

- S/MIME or PGP/GPG certificate sample (sanitize private key)
- PKI infrastructure documentation or diagram
- Email gateway configuration (TLS/STARTTLS settings)
- User training completion records
- DLP policy screenshots (if encryption enforcement)


**2.2 Digital Signatures:**

- Email certificate inventory
- Digital signature policy document
- Example signed email (with headers showing signature verification)


**3.1 File Transfer:**

- SFTP/FTPS server configuration
- SSH key inventory for SFTP
- File transfer access logs (sample showing successful authentication)
- MFA configuration for external file transfer
- Protocol scan results (showing FTP disabled, SFTP enabled)


**4.1 VPN:**

- VPN server configuration export (sanitize pre-shared keys)
- MFA enrollment statistics or screenshot
- VPN protocol and encryption verification
- VPN connection logs (sample)
- Split-tunneling policy documentation


**4.2 SSH:**

- SSH server configuration (/etc/ssh/sshd_config) - sanitize host keys
- SSH key algorithm inventory (`for i in /home/*/.ssh/authorized_keys; do ssh-keygen -lf $i; done`)
- Key rotation schedule documentation
- Root login disabled verification (`grep PermitRootLogin /etc/ssh/sshd_config`)


**4.3 RDP:**

- Network diagram showing RDP access path (via VPN/jump host)
- RDP NLA configuration verification (Registry or Group Policy)
- RDP certificate configuration
- MFA integration documentation
- RDP session recording setup (if implemented)


**4.4 API Security:**

- API authentication documentation
- Secrets manager configuration (HashiCorp Vault, AWS Secrets Manager, etc.)
- Token expiry policy configuration
- Rate limiting rules
- API TLS configuration (listener settings)


**4.5 Database Connections:**

- Database connection encryption configuration
- Connection string examples (SANITIZE passwords)
- Certificate validation settings
- Database server TLS configuration


**4.6 Wireless Networks:**

- Wireless controller configuration export
- 802.1X RADIUS server configuration
- SSID encryption settings (per SSID)
- Guest network isolation verification (VLAN configuration)
- WPA2/WPA3 configuration details


**4.7 Cloud Transmission:**

- Cloud provider TLS configuration verification
- PrivateLink/Private Link setup documentation
- API endpoint encryption verification
- Cloud provider compliance certifications (if applicable)


## Tools for Evidence Collection

**TLS/Certificate Testing:**
```bash
# SSL Labs (web-based)
https://www.ssllabs.com/ssltest/analyze.html?d=example.com

# testssl.sh (comprehensive)
testssl.sh --full https://example.com > evidence.txt

# OpenSSL certificate details
openssl s_client -connect example.com:443 </dev/null 2>/dev/null | openssl x509 -noout -text > cert_details.txt

# Certificate validity period calculation
openssl s_client -connect example.com:443 </dev/null 2>/dev/null | openssl x509 -noout -dates
```

**SSH Testing:**
```bash
# SSH algorithms
ssh -Q cipher; ssh -Q mac; ssh -Q kex; ssh -Q key

# SSH server configuration check
sshd -T | grep -E 'protocol|ciphers|macs|kexalgorithms'

# Test SSH connection with specific algorithm
ssh -vv user@host  # Verbose output shows negotiated algorithms
```

**Database Connection Testing:**
```bash
# PostgreSQL TLS verification
psql "host=dbserver sslmode=verify-full sslrootcert=/path/to/ca.crt" -c "SHOW ssl;"

# MySQL TLS verification
mysql --ssl-mode=VERIFY_IDENTITY --ssl-ca=/path/to/ca.pem -e "SHOW STATUS LIKE 'Ssl_cipher';"
```

**WiFi Assessment:**
```bash
# WiFi encryption check (Linux)
nmcli dev wifi list

# Wireless controller (vendor-specific)
# Export configuration via vendor CLI or web interface
```

**API Testing:**
```bash
# API TLS version
curl -v https://api.example.com 2>&1 | grep "TLS"

# API authentication test
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/endpoint
```

## Evidence Sanitization

**CRITICAL:** Remove sensitive information before storing evidence:

**Must Sanitize:**

- Private keys (TLS, SSH, etc.)
- Passwords, passphrases, secrets
- API keys, tokens, credentials
- Pre-shared keys (VPN)
- Personal identifiable information
- Internal IP addresses (if required by policy)


**Sanitization Methods:**

- Replace with placeholders: `private_key = [REDACTED]`
- Use example values: `password = example_password_123`
- Redact in documents: Black boxes over sensitive fields in screenshots
- Hash or mask: `api_key = sk_live_****************************abcd`


**Tool Suggestion:**
```bash
# Sanitize config files
sed 's/private_key = .*/private_key = [REDACTED]/g' config.txt > config_sanitized.txt
```

---

# Common Pitfalls

## ❌ MISTAKE #1: Using Outdated Certificate Validity Standards

**Problem:** Referencing 397-day or 825-day validity for public CA certificates  
**Why Wrong:** CA/Browser Forum SC-081v3 has progressive reduction schedule (398→200→100→47 days)  
**Correct Approach:**

- Use correct limit based on assessment date:
  - Before 15.03.2026: ≤398 days
  - 15.03.2026 - 15.03.2027: ≤200 days
  - 15.03.2027 - 15.03.2029: ≤100 days
  - After 15.03.2029: ≤47 days
- Distinguish public CA (must follow SC-081v3) from internal PKI (825 days max)  

**Impact:** Non-compliant certificates, failed audits, certificate automation crisis when deadline hits

---

## ❌ MISTAKE #2: "It's Internal, So No Encryption Needed"

**Problem:** Assuming internal networks don't need TLS/encryption  
**Why Wrong:** Data classification drives encryption requirements, NOT network location  
**Correct Approach:**

- Check data classification: Confidential/Restricted → TLS REQUIRED regardless of network
- Internal/Public data on isolated network → TLS recommended, exception acceptable with risk assessment
- Admin interfaces/authentication → TLS REQUIRED (credentials in transit)  

**Impact:** Data exposure, compliance violations, insider threat vulnerability

---

## ❌ MISTAKE #3: TLS-Only for Email Encryption

**Problem:** Relying solely on transport encryption (STARTTLS) for Confidential/Restricted emails  
**Why Wrong:**

- STARTTLS only protects during transmission (mail server to mail server)
- Email stored unencrypted on recipient's mail server
- Mail server admins can read email
- Backups contain cleartext email  

**Correct Approach:**

- Confidential/Restricted external email: S/MIME or PGP/GPG (end-to-end encryption)
- Internal classification: STARTTLS acceptable
- Transport + end-to-end encryption is defense-in-depth  

**Impact:** Data accessible to mail server administrators, subpoenas, backups

---

## ❌ MISTAKE #4: Ignoring Certificate Expiration Monitoring

**Problem:** Manual certificate tracking in spreadsheets, no automated alerts  
**Why Wrong:** Human error leads to expired certificates → security incident  
**Correct Approach:**

- Automated certificate monitoring with 30-day advance alerts minimum
- Multiple alert channels (email, SIEM, dashboard)
- Escalation for ignored alerts
- Certificate inventory auto-updated (not manual spreadsheet)  

**Impact:** Service outages, security incidents, compliance findings

---

## ❌ MISTAKE #5: Self-Signed Certificates in Production

**Problem:** Using self-signed certificates to "save money" or "avoid CA hassle"  
**Why Wrong:**

- No chain of trust → browsers show warnings
- Users trained to click through certificate warnings (security culture failure)
- Difficult to revoke if compromised
- Man-in-the-middle attacks harder to detect  

**Correct Approach:**

- Use Let's Encrypt (free, automated)
- Use organizational internal CA (for internal services)
- Self-signed acceptable ONLY for dev/test with CISO approval  

**Impact:** Security culture degradation, audit findings, vulnerability to MITM attacks

---

## ❌ MISTAKE #6: Weak WiFi "Because It's Convenient"

**Problem:** WPA2-Personal with short passphrase (<20 characters) for "ease of use"  
**Why Wrong:** Vulnerable to brute force attacks, especially with weak passphrase  
**Correct Approach:**

- **Corporate WiFi:** WPA3-Enterprise or WPA2-Enterprise with 802.1X (certificate-based)
- **Guest WiFi:** Isolated network, captive portal, or WPA2-Personal with ≥20 character passphrase
- **Small office exception:** WPA2-Personal acceptable with ≥20 character passphrase  

**Impact:** Unauthorized network access, lateral movement, eavesdropping

---

## ❌ MISTAKE #7: "Trust Any Certificate" in Database Connections

**Problem:** Disabling certificate validation (`sslmode=allow`, `TrustServerCertificate=true`) to "make it work"  
**Why Wrong:** Vulnerable to man-in-the-middle attacks - attacker can intercept database traffic  
**Correct Approach:**

- Properly configure certificate trust chain
- Use `sslmode=verify-full` (PostgreSQL) or `TrustServerCertificate=false` (MSSQL)
- Import CA certificate into trust store if using internal CA  

**Impact:** Database traffic interception, credential theft, data exfiltration

---

## ❌ MISTAKE #8: Forgetting About APIs

**Problem:** Assuming only web UIs need HTTPS, ignoring APIs  
**Why Wrong:** APIs often handle MORE sensitive data than web UIs (system-to-system, batch processing)  
**Correct Approach:**

- TLS 1.2+ for ALL APIs (internal and external)
- Proper authentication (OAuth2/API keys/mTLS)
- API gateway enforces TLS and authentication
- Rate limiting per API key  

**Impact:** API-based data breaches, unauthorized access, data exfiltration

---

## ❌ MISTAKE #9: No Evidence for Compliant Items

**Problem:** Only documenting gaps, not compliant implementations  
**Why Wrong:** Auditors need evidence of compliance, not just gap remediation plans  
**Correct Approach:**

- Document evidence for EVERY item (compliant AND non-compliant)
- Compliant items: Screenshot, config file, test result
- Non-compliant items: Gap description + remediation plan + evidence of current state  

**Impact:** Audit findings despite actual compliance, "prove you're compliant" requests

---

## ❌ MISTAKE #10: Completing Assessment Without Technical Verification

**Problem:** Answering based on assumptions, outdated documentation, or "we should have this"  
**Why Wrong:**

- Documentation may be outdated
- Configurations may have changed
- Assumptions often wrong  

**Correct Approach:**

- Test and verify EVERY control (SSL Labs, testssl.sh, actual certificate inspection)
- Don't assume - verify
- If documentation says "TLS enabled", test it with tools
- If certificate says "398 days", calculate it yourself  

**Impact:** Inaccurate assessment, false sense of security, surprises during audit

---

# Quality Checklist

**Complete this checklist before submitting assessment for review:**

## Completeness Checks

- [ ] All 13 assessment sections completed (or marked N/A with clear justification)
- [ ] Every yellow data entry cell filled in (no blanks in yellow cells)
- [ ] Status dropdown selected for every applicable item (✅ / ⚠️ / ❌ / N/A)
- [ ] Evidence location documented for every compliant item
- [ ] Gap descriptions completed for all Partial/Non-Compliant items (clear, specific)
- [ ] Remediation plans with responsible person and target date for all gaps
- [ ] All compliance checklists completed (every checkbox marked Yes/No/N/A)
- [ ] Additional Details sections completed (counts, configurations, dates)
- [ ] Exception/Deviation documentation complete where Status = Partial/Non-Compliant
- [ ] Summary Dashboard reviewed and totals make sense
- [ ] Evidence Register populated with all evidence files (consistent naming)
- [ ] All evidence files exist and are accessible (checked storage location)


## Accuracy Checks

- [ ] Certificate validity reflects SC-081v3 timeline (not outdated 397-day standard)
- [ ] TLS versions verified with tools (SSL Labs, testssl.sh) not assumed from documentation
- [ ] Encryption protocols tested, not assumed (actual connection tests performed)
- [ ] Data classifications verified against organizational classification scheme
- [ ] All external-facing services identified (checked DNS records, not just documentation)
- [ ] Authentication methods verified (logged in and tested, not documented assumptions)
- [ ] Evidence is current (collected within last 30 days)
- [ ] Certificate validity calculations are correct (Not After - Not Before, in days)
- [ ] Automation status accurately reflects current state (not planned state)


## Policy Alignment Checks

- [ ] All "MUST" requirements from ISMS-POL-A.8.24, Section 6.2 (Data Transmission) addressed
- [ ] Public CA certificate validity ≤398 days (until 15.03.2026) or timeline-appropriate
- [ ] Automation requirement addressed for public CA certificates (deadline 15.03.2026)
- [ ] Internal PKI distinguished from public CA requirements (825 days vs progressive reduction)
- [ ] Confidential/Restricted data transmission encrypted (TLS for web, S/MIME/PGP for email)
- [ ] Exceptions properly documented with risk assessment and CISO approval
- [ ] Compensating controls identified for any gaps
- [ ] No prohibited protocols in use (FTP, WEP, TLS 1.0/1.1, SSHv1, etc.)
- [ ] MFA requirements met (VPN, external file transfer, RDP to production)


## Audit Readiness Checks

- [ ] Evidence is verifiable (auditor could reproduce findings with same tools/methods)
- [ ] Evidence is timestamped and attributable (clear what system, when collected, by whom)
- [ ] No sensitive credentials exposed in screenshots/configs (sanitized appropriately)
- [ ] Evidence organized logically and consistently named (EV-[Section]-[System]-[Date]-[Type])
- [ ] Technical jargon explained where necessary (not everyone is a network engineer)
- [ ] Assessment tells a clear story from beginning to end (executive could understand)
- [ ] Cross-references work (if referencing other sections, correct section numbers)
- [ ] Dates in DD.MM.YYYY format throughout (Swiss/EU convention)


## Red Flags to Address BEFORE Submission

- [ ] No ❌ Non-Compliant items without remediation plan and target date
- [ ] No missing evidence for ✅ Compliant items (every compliant claim has proof)
- [ ] No self-signed certificates in production without CISO exception approval
- [ ] No unencrypted transmission of Confidential/Restricted data (TLS mandatory)
- [ ] No expired certificates or certificates expiring within 30 days
- [ ] No prohibited protocols detected (FTP, WEP, TLS 1.0/1.1, SSHv1)
- [ ] No certificate validity >398 days on public CA certificates (as of assessment date)
- [ ] No manual certificate renewal for public CA certificates without remediation plan (deadline 15.03.2026)
- [ ] Overall compliance rate >80% (if <80%, indicates systemic issues requiring escalation)


## Final Sanity Checks

- [ ] Summary Dashboard totals match manual count (no formula errors)
- [ ] Assessment owner name and role completed
- [ ] Assessment date is correct (date assessment performed, not date workbook created)
- [ ] Organization name filled in (not default "[Organization]")
- [ ] Next Review Date set (typically 3 months from assessment date for quarterly review)
- [ ] Assessment status set to "Draft" (ready for Information Security Officer review)


**If ANY checkbox above is unchecked:**  
**STOP. Do not submit. Go back and complete the missing item.**

---

# Review & Approval

## Review Process

**Step 1: Self-Review** (Assessment Owner)

- **Action:** Run through Quality Checklist (Section 7) line by line
- **Fix:** Address any identified issues
- **Verify:** All evidence files are accessible and named correctly
- **Set Status:** Change assessment status to "Draft" in Approval Sign-Off sheet
- **Submit:** Email to Information Security Officer (ISO) with link to assessment file


**Step 2: Technical Review** (Information Security Officer)

- **Verify:** Technical accuracy of findings (spot-check with tools)
- **Validate:** Gap descriptions are specific and actionable
- **Assess:** Remediation plans are realistic (dates, resources, responsible parties)
- **Check:** Evidence quality (verifiable, complete, timestamped)
- **Identify:** Any missing risks or controls not addressed
- **Provide:** Feedback to assessment owner (email or comments in workbook)
- **Duration:** 2-3 business days typical


**Step 3: Remediation (if needed)** (Assessment Owner)

- **Action:** Address review feedback from ISO
- **Update:** Assessment accordingly (additional evidence, clarified gaps, etc.)
- **Re-submit:** To ISO for re-review if significant changes
- **Minor Changes:** If only minor edits, ISO may approve without re-review


**Step 4: Final Approval** (CISO)

- **Review:** Overall compliance posture (Summary Dashboard)
- **Approve:** Remediation timelines and resource requirements
- **Accept:** Documented risks for exceptions
- **Sign:** Assessment in Approval Sign-Off sheet
- **Set:** "Next Review Date" (typically quarterly: +3 months)
- **Outcomes:**
  - **"Approved":** Compliance level acceptable, remediation plan reasonable
  - **"Approved with conditions":** Minor concerns, remediation must be completed by specified date with follow-up
  - **"Rejected":** Significant issues, re-assessment required (indicate specific issues)


## Approval Timeline

**Typical Timeline:**

- Assessment completion: 4-6 hours (owner)
- Self-review and quality check: 30-60 minutes (owner)
- Technical review: 2-3 business days (ISO)
- Remediation (if needed): 1-2 hours (owner)
- Final approval: 1-2 business days (CISO)
- **Total:** 1-2 weeks from start to final approval


**Expedited Timeline (for urgent compliance needs):**

- Can be compressed to 2-3 days with dedicated resources
- Requires pre-coordination with ISO and CISO
- Only for critical situations (audit, regulatory deadline, security incident)


## After Approval

**Immediate Actions:**
1. **File Assessment:** Store approved assessment in ISMS document repository

   - Location: `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
   - Filename: `ISMS-IMP-A.8.24.1_Data_Transmission_[DATE]_APPROVED.xlsx`


2. **Distribute:** Email to relevant stakeholders

   - Network Engineering team (for remediation execution)
   - Security team (for tracking)
   - Compliance team (for audit evidence)
   - Management (for awareness)


3. **Track Remediation:** Add remediation items to project tracking system

   - Jira, ServiceNow, Asana, or organizational project management tool
   - Assign to responsible parties identified in assessment
   - Set due dates as documented in remediation plans
   - Set recurring check-ins (weekly or bi-weekly for critical items)


4. **Schedule Follow-Up:** Set calendar reminders

   - Quarterly review (3 months from assessment date)
   - Remediation check-ins (for open gaps)
   - Certificate renewal reminders (30 days before expiration)
   - Automation deadline reminder (if applicable before 15.03.2026)


## Ongoing Monitoring

**Between Quarterly Assessments:**

- **Certificate Monitoring:** Automated alerts for expiring certificates (should be continuous)
- **Configuration Changes:** Any crypto-related changes should be documented and verified
- **New Systems:** New services must be assessed for cryptographic controls before production
- **Incidents:** Any certificate expiration or crypto-related incident triggers immediate re-assessment
- **Policy Updates:** If ISMS-POL-A.8.24, Section 6.2 (Data Transmission) updated, assessment must be revised accordingly


**Triggers for Immediate Re-Assessment:**

- Major infrastructure changes (new data center, cloud migration)
- Security incidents involving encryption (certificate compromise, MITM attack)
- Failed audit findings on cryptographic controls
- Regulatory changes affecting encryption requirements
- Certificate automation deadline approaching (15.03.2026) without completed migration


## Continuous Improvement

**Use Assessment Results to Improve:**

- **Pattern Recognition:** Similar gaps across multiple systems? → Systemic issue requiring policy or training
- **Automation Opportunities:** Repetitive manual tasks? → Automate (certificate renewal, compliance checking)
- **Training Needs:** Common mistakes? → Targeted training for teams
- **Tooling Gaps:** Difficult to collect evidence? → Invest in monitoring/scanning tools
- **Policy Refinements:** Unclear requirements? → Update policy for clarity


**Feedback Loop:**

- Assessment owner provides feedback on this User Guide (what was unclear, what was helpful)
- ISO reviews common questions/issues encountered
- Update this guide accordingly for next assessment cycle


---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Instructions for Completing This Assessment

## How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Data Transmission Assessment Excel workbook (`ISMS-IMP-A.8.24.1_Data_Transmission_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a824_1_data_transmission_assessment.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the technology/service applies to your organization
2. **Check Yes/No/Not Applicable** for each assessment question
3. **If Yes:** Complete the assessment table with your current implementation
4. **Mark Status:** ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A Not Applicable
5. **If ⚠️ or ❌:** Complete the Exception/Deviation Documentation section
6. **Provide Evidence:** Document where compliance evidence can be found
7. **Review Compliance Checklist:** Check all items that apply to your implementation

## Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **⚠️** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **❌** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply to your environment |

## Evidence Types

Acceptable evidence includes:

- Configuration files or screenshots
- Network scan results (SSL Labs, nmap, testssl.sh)
- System documentation
- Vendor specifications
- Certificate inventory
- Audit logs
- Compliance reports


## Certificate Validity Requirements Update (CA/Browser Forum SC-081v3)

**CRITICAL - Updated Standards (Effective 2025):**

The CA/Browser Forum approved Ballot SC-081v3 which progressively reduces maximum certificate validity for publicly-trusted certificates:

| Effective Date | Maximum Validity | DCV Reuse Period | Notes |
|----------------|------------------|------------------|-------|
| **Until 15.03.2026** | **398 days** | 398 days | Current standard (CA/B Forum SC-062) |
| **15.03.2026 onwards** | **200 days** | 200 days | Automation REQUIRED |
| **15.03.2027 onwards** | **100 days** | 100 days | Bi-monthly renewals |
| **15.03.2029 onwards** | **47 days** | 10 days | Final target, automation mandatory |

**Certificate Renewal Automation:**

- **Public CA certificates:** Automated renewal REQUIRED before 15.03.2026
- **Rationale:** Manual processes will NOT scale for <100-day lifecycles
- **Implementation:** ACME protocol (Let's Encrypt, Sectigo, DigiCert, etc.)
- **Internal PKI:** Automation REQUIRED if certificate inventory >50 certificates


**Internal/Private PKI Certificates:**

- Maximum: 825 days (not subject to CA/Browser Forum requirements)
- Recommended: 180-365 days for enhanced security posture


**Reference:** CA/Browser Forum Ballot SC-081v3  
**URL:** https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/

---

# HTTPS/TLS Implementation

## External Web Services

**Policy Requirement:** All externally accessible web services MUST use TLS encryption with valid certificates from trusted Certificate Authorities 

**Assessment Question:**

**Does your organization have external-facing web services or websites?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 1.2
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Service Description | Current TLS Version | Certificate Source (CA) | Certificate Validity | Status | Evidence Location | Gap Description | Remediation Needed |
|---------------------|--------------------|-----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: Public websites, customer portals, APIs | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Number of external web services:** _________
- **Certificate expiration monitoring configured:** [ ] Yes [ ] No
- **Automated certificate renewal:** [ ] Yes [ ] No [ ] Planned
- **Certificate inventory maintained:** [ ] Yes [ ] No
- **Certificate automation status:** [ ] Fully automated [ ] Partially automated [ ] Manual (requires migration) [ ] Not applicable
- **Target automation completion date (if not automated):** _________
- **ACME-enabled CA in use:** [ ] Yes [ ] No [ ] Planned


---

**Compliance Checklist:**

- [ ] TLS 1.3 preferred OR TLS 1.2 minimum
- [ ] Valid certificates from trusted public CA
- [ ] Certificate validity: ≤398d (until 15.03.2026), ≤200d (15.03.2026+), ≤100d (15.03.2027+), ≤47d (15.03.2029+)
- [ ] Automated certificate renewal implemented or planned (REQUIRED for public CAs before 15.03.2026)
- [ ] Infrastructure readiness for short-lived certificates assessed (47-day lifecycle by 2029)
- [ ] Self-signed certificates NOT used in production
- [ ] HTTP automatically redirects to HTTPS
- [ ] HSTS (HTTP Strict Transport Security) header configured
- [ ] Strong cipher suites configured (per Appendix A)
- [ ] Weak/deprecated protocols disabled (TLS 1.1, TLS 1.0, SSL)
- [ ] Perfect Forward Secrecy (PFS) enabled
- [ ] Certificate expiration alerts configured (≥30-day advance, adjusted for shorter validity periods)


**Certificate Automation Readiness Assessment (REQUIRED before 15.03.2026):**

- [ ] ACME protocol support enabled (Let's Encrypt, Sectigo, DigiCert, etc.)
- [ ] Certificate lifecycle fully automated (issuance, installation, renewal, revocation)
- [ ] Alert thresholds adjusted for shorter validity periods (≥30 days for 200-day certs)
- [ ] Monitoring dashboards updated to track 47-day lifecycle readiness
- [ ] Documented process for emergency certificate replacement (<24 hour SLA)
- [ ] Staff trained on automated certificate management systems
- [ ] Runbook for automated renewal failures with escalation procedures


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Network segmentation/firewall restrictions
  - [ ] Enhanced monitoring and alerting
  - [ ] IP whitelisting/access restrictions
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________
- **Budget required:** [ ] Yes [ ] No  Amount: _________


---

## Internal Web Services

**Policy Requirement:** Internal web services containing sensitive data (Confidential or Restricted classification) MUST use TLS 

**Assessment Question:**

**Does your organization have internal web services (intranet, internal portals, internal APIs)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Service Description | Data Classification | Current TLS Version | Certificate Type | Status | Evidence Location | Gap Description | Remediation Needed |
|---------------------|--------------------|--------------------|------------------|---------|-------------------|-----------------|-------------------|
| Example: Intranet, internal APIs, admin panels | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Number of internal web services:** _________
- **Data classification(s) handled:** [ ] Public [ ] Internal [ ] Confidential [ ] Restricted
- **Internal CA in use:** [ ] Yes [ ] No
- **Certificate management process documented:** [ ] Yes [ ] No
- **Internal certificate inventory count:** _________
- **Automation status (if >50 certificates):** [ ] Automated [ ] Manual [ ] In progress


---

**Compliance Checklist:**

- [ ] TLS 1.2+ for services with Confidential/Restricted data
- [ ] Valid certificates (internal CA acceptable for internal services)
- [ ] Services with non-sensitive data: Risk assessed and documented (if no TLS)
- [ ] Certificate inventory maintained for internal certificates
- [ ] Certificate expiration monitoring configured (same standards as public CA)
- [ ] Internal PKI certificates: Maximum 825 days validity (not subject to CA/B Forum)
- [ ] Internal TLS certificates: 180-365 days recommended for security posture
- [ ] Automation REQUIRED if certificate inventory >50 certificates
- [ ] Manual renewal exception: <50 certificates with documented CISO approval


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Isolated network segment (no internet access)
  - [ ] Enhanced access controls (authentication required)
  - [ ] Monitoring and logging
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# Email Security

## Email Encryption

**Policy Requirement:** Emails containing classified information (Confidential or Restricted) MUST be encrypted when sent externally 

**Assessment Question:**

**Does your organization send emails containing classified information to external parties?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2.2
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Email System | Encryption Solution | Encryption Method | User Adoption Rate | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|--------------------|--------------------|-------------------|---------|-------------------|-----------------|-------------------|
| Example: Exchange, Gmail, other | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Encryption solution in use:** [ ] S/MIME [ ] PGP/GPG [ ] TLS-only [ ] Other: _______
- **PKI infrastructure for email:** [ ] Implemented [ ] Planned [ ] Not implemented
- **User training provided:** [ ] Yes [ ] No
- **Encryption enforced via policy/DLP:** [ ] Yes [ ] No


---

**Compliance Checklist:**

- [ ] S/MIME or PGP/GPG encryption available
- [ ] Users trained on when/how to encrypt sensitive emails
- [ ] PKI infrastructure in place for S/MIME
- [ ] Opportunistic TLS enabled for mail server connections
- [ ] STARTTLS enabled for SMTP


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] DLP blocks sensitive email externally
  - [ ] Secure portal for external file sharing
  - [ ] Policy prohibits emailing Confidential/Restricted externally
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

## Digital Signatures

**Policy Requirement:** Digital signatures RECOMMENDED for all external emails, REQUIRED for legal/financial/official communications 

**Assessment Question:**

**Does your organization use digital signatures for email?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 3
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Use Case | Signature Method | Certificate Source | Status | Evidence Location | Gap Description | Remediation Needed |
|----------|------------------|-------------------|---------|-------------------|-----------------|-------------------|
| Example: Legal docs, financial approvals, all external | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Digital signatures used for:** [ ] All emails [ ] Legal docs only [ ] Executives only [ ] Not used
- **Certificate source:** [ ] Public CA [ ] Internal PKI [ ] Both


---

**Compliance Checklist:**

- [ ] Digital signatures available for required use cases
- [ ] Email certificates issued from trusted CA or internal PKI
- [ ] Certificate validity ≤ 1 year
- [ ] Users trained on digital signature usage


---

# Secure File Transfer

## File Transfer Protocols

**Policy Requirement:** File transfers containing sensitive data MUST use encrypted protocols (SFTP, FTPS, HTTPS). Unencrypted FTP is PROHIBITED 

**Assessment Question:**

**Does your organization transfer files containing sensitive data to/from external parties or between systems?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Transfer Method/System | Protocol Used | Authentication Method | Data Classification | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------------|---------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: SFTP server, cloud storage, partner portal | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Approved protocols in use:** [ ] SFTP [ ] FTPS [ ] HTTPS [ ] SCP [ ] Other: _______
- **Prohibited protocols detected:** [ ] FTP [ ] TFTP [ ] None
- **Authentication:** [ ] Password [ ] Key-based [ ] MFA [ ] Certificate


---

**Compliance Checklist:**

- [ ] SFTP, FTPS, or HTTPS used for sensitive file transfers
- [ ] Plain FTP NOT used for sensitive data
- [ ] Strong authentication configured (key-based preferred)
- [ ] MFA required for external file transfer
- [ ] File transfer logging enabled
- [ ] SSH keys rotated annually (if SFTP used)


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Isolated network for legacy FTP
  - [ ] File content encryption (in addition to transport)
  - [ ] Access restricted to specific IP addresses
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# Remote Access Protocols

## VPN (Virtual Private Network)

**Policy Requirement:** All remote access to organizational networks MUST use encrypted VPN with approved protocols (IPsec, WireGuard, OpenVPN). MFA REQUIRED 

**Assessment Question:**

**Does your organization provide remote access via VPN?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4.2
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| VPN Solution | Protocol | Encryption Algorithm | MFA Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|----------|---------------------|-------------|---------|-------------------|-----------------|-------------------|
| Example: Cisco AnyConnect, WireGuard, OpenVPN | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **VPN protocol in use:** [ ] IPsec/IKEv2 [ ] WireGuard [ ] OpenVPN [ ] Other: _______
- **Encryption algorithm:** _________
- **Number of VPN users:** _________
- **MFA solution:** [ ] TOTP [ ] Push notification [ ] SMS [ ] Hardware token [ ] None
- **Split-tunneling:** [ ] Disabled [ ] Enabled (with justification)


---

**Compliance Checklist:**

- [ ] Approved VPN protocol (IPsec/IKEv2, WireGuard, OpenVPN with TLS 1.2+)
- [ ] AES-256 or ChaCha20 encryption
- [ ] Perfect Forward Secrecy (PFS) enabled
- [ ] MFA required for all VPN connections
- [ ] Certificate-based authentication (preferred) OR strong pre-shared key
- [ ] VPN session timeout configured (≤30 minutes idle)
- [ ] Split-tunneling disabled (or documented exception)
- [ ] VPN access logs retained and reviewed


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Zero-trust network architecture (no VPN needed)
  - [ ] Additional authentication layer
  - [ ] Network segmentation post-VPN
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

## SSH (Secure Shell)

**Policy Requirement:** SSH REQUIRED for all administrative and remote terminal access. SSH protocol version 2 REQUIRED, password authentication SHOULD be disabled 

**Assessment Question:**

**Does your organization use SSH for remote system administration?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4.3
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| System/Service | SSH Version | Authentication Method | Key Algorithm | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------|-------------|----------------------|---------------|---------|-------------------|-----------------|-------------------|
| Example: Linux servers, network devices, containers | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **SSH protocol version:** [ ] SSHv2 only [ ] SSHv1 (legacy - prohibited)
- **Authentication method:** [ ] Key-based only [ ] Password allowed [ ] Both
- **SSH key types in use:** [ ] Ed25519 [ ] RSA 3072+ [ ] RSA 2048 [ ] ECDSA [ ] Other
- **Root login via SSH:** [ ] Disabled [ ] Enabled
- **SSH key rotation schedule:** [ ] Annual [ ] On personnel change [ ] No rotation


---

**Compliance Checklist:**

- [ ] SSH protocol version 2 only (SSHv1 disabled)
- [ ] Key-based authentication (password auth disabled preferred)
- [ ] Minimum key length: RSA 2048-bit or Ed25519
- [ ] Root login disabled
- [ ] SSH keys rotated annually
- [ ] Unused SSH keys removed
- [ ] Strong algorithms configured (per Policy Appendix A)
- [ ] Weak algorithms disabled (DSA, MD5, SHA-1)


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] SSH accessible only via VPN or jump host
  - [ ] Enhanced logging and monitoring
  - [ ] Rate limiting on SSH connection attempts
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

## RDP (Remote Desktop Protocol)

**Policy Requirement:** RDP connections MUST be encrypted using TLS. RDP MUST NOT be directly exposed to Internet. Access through VPN, jump host, or zero-trust gateway REQUIRED 

**Assessment Question:**

**Does your organization use RDP for remote Windows system access?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 5
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| System/Environment | RDP Access Method | TLS Encryption | NLA Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------------|-------------------|----------------|-------------|---------|-------------------|-----------------|-------------------|
| Example: Windows servers, workstations, virtual desktops | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **RDP access method:** [ ] VPN required [ ] Jump host/bastion [ ] Direct (prohibited) [ ] Zero-trust gateway
- **Network Level Authentication (NLA):** [ ] Enabled [ ] Disabled
- **MFA for RDP:** [ ] Required [ ] Optional [ ] Not implemented
- **RDP encryption level:** [ ] High [ ] Client Compatible [ ] Low (prohibited)


---

**Compliance Checklist:**

- [ ] RDP accessed through VPN or jump host (NOT directly exposed)
- [ ] TLS encryption configured
- [ ] Network Level Authentication (NLA) enabled
- [ ] RDP encryption level set to 'High'
- [ ] MFA required for production system access
- [ ] RDP session recording (recommended for privileged access)


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] RDP accessible only from specific IP addresses
  - [ ] Strong password policy enforced
  - [ ] Account lockout after failed attempts
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# API Security

## API Authentication and Encryption

**Policy Requirement:** All API endpoints MUST use HTTPS with TLS 1.2+. API authentication MUST use approved methods (OAuth2, API keys with 256-bit entropy, mTLS). API keys MUST rotate quarterly 

**Assessment Question:**

**Does your organization have APIs (internal or external)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| API Name/Service | Authentication Method | TLS Version | API Key Management | Token Expiry | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------|----------------------|-------------|-------------------|--------------|---------|-------------------|-----------------|-------------------|
| Example: REST API, GraphQL, SOAP services | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **API authentication methods:** [ ] OAuth2/JWT [ ] API keys [ ] mTLS [ ] Basic Auth (HTTPS only)
- **API key storage:** [ ] Secrets manager [ ] Environment variables [ ] Hardcoded (prohibited)
- **API gateway in use:** [ ] Yes [ ] No
- **Rate limiting implemented:** [ ] Yes [ ] No


---

**Compliance Checklist:**

- [ ] All API endpoints use HTTPS with TLS 1.2+ (TLS 1.3 preferred)
- [ ] API endpoints NOT accessible over HTTP
- [ ] OAuth 2.0 with JWT tokens (preferred) OR API keys (256-bit entropy minimum)
- [ ] API keys stored in secrets manager (NOT in code/config files)
- [ ] API keys rotated quarterly (90-day maximum)
- [ ] Access tokens expire within 1 hour (for OAuth2)
- [ ] Refresh tokens expire within 24 hours
- [ ] Rate limiting implemented per API key or client
- [ ] API keys NOT passed in URL query parameters


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] API only accessible via internal network
  - [ ] IP whitelisting for API access
  - [ ] API gateway with additional security controls
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# Network Protocols

## Database Connections

**Policy Requirement:** Database connections MUST use encrypted protocols (TLS for PostgreSQL/MySQL, encrypted connections for MSSQL) 

**Assessment Question:**

**Does your organization have applications connecting to databases?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6.2
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Database System | Connection Encryption | Certificate Validation | Status | Evidence Location | Gap Description | Remediation Needed |
|-----------------|----------------------|------------------------|---------|-------------------|-----------------|-------------------|
| Example: PostgreSQL, MySQL, MSSQL, Oracle | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Database types in use:** [ ] PostgreSQL [ ] MySQL/MariaDB [ ] MSSQL [ ] Oracle [ ] MongoDB [ ] Other: _______
- **Encryption enabled:** [ ] Yes [ ] No [ ] Partial
- **Certificate validation:** [ ] Enabled [ ] Disabled [ ] Not applicable


---

**Compliance Checklist:**

- [ ] Database connections encrypted (TLS/SSL)
- [ ] Certificate validation enabled (not "trust any certificate")
- [ ] Self-signed certificates only for internal databases (with proper CA)
- [ ] Unencrypted connections disabled or documented exception


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Database on isolated network segment
  - [ ] No sensitive data in database
  - [ ] Application-level encryption of sensitive fields
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

## Wireless Networks

**Policy Requirement:** Wireless networks MUST use WPA3-Enterprise or WPA2-Enterprise minimum. WEP and WPA (original) PROHIBITED 

**Assessment Question:**

**Does your organization have wireless networks?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 7
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Network SSID | Encryption Standard | Authentication Method | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|--------------------|-----------------------|---------|-------------------|-----------------|-------------------|
| Example: Corporate WiFi, Guest WiFi | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Corporate WiFi encryption:** [ ] WPA3-Enterprise [ ] WPA2-Enterprise [ ] WPA2-Personal [ ] Other
- **Guest WiFi:** [ ] Isolated network [ ] Captive portal [ ] Open (no encryption)
- **802.1X authentication:** [ ] Implemented [ ] Planned [ ] Not implemented
- **WiFi password strength (if PSK):** [ ] ≥20 characters [ ] <20 characters


---

**Compliance Checklist:**

- [ ] WPA3-Enterprise or WPA2-Enterprise for corporate networks
- [ ] 802.1X with EAP-TLS (certificate-based) preferred
- [ ] WPA2-Personal only with strong passphrase (≥20 characters)
- [ ] WEP and WPA (original) NOT used
- [ ] Guest wireless isolated from corporate network
- [ ] WiFi passwords rotated quarterly (for PSK networks)


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Network segmentation (guest WiFi only)
  - [ ] Strong WPA2-Personal passphrase (≥20 characters)
  - [ ] Network access control (NAC)
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# Cloud Data Transmission

## Cloud Provider Connections

**Policy Requirement:** Connections to cloud provider APIs MUST use TLS 1.2+. Private connectivity options (PrivateLink, Private Link, Private Service Connect) RECOMMENDED for high-volume or sensitive data 

**Assessment Question:**

**Does your organization use cloud services (AWS, Azure, GCP, SaaS)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 8
- [ ] Not Applicable


---

**If Yes, complete the assessment:**

| Cloud Provider/Service | Connection Method | Encryption | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------------|-------------------|------------|---------|-------------------|-----------------|-------------------|
| Example: AWS, Azure, GCP, Office 365, Salesforce | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Connection type:** [ ] Public internet (TLS) [ ] VPN [ ] Private Link/PrivateLink [ ] Direct Connect/ExpressRoute
- **Data classification transmitted:** [ ] Public [ ] Internal [ ] Confidential [ ] Restricted


---

**Compliance Checklist:**

- [ ] TLS 1.2+ for all cloud API connections
- [ ] Private connectivity for Confidential/Restricted data (preferred)
- [ ] Cloud provider native encryption enabled
- [ ] Data encrypted in transit to/from cloud


---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] VPN for cloud access
  - [ ] Application-level encryption before cloud transmission
  - [ ] Data classification does not require private connectivity
  - [ ] Other: _______________________________


**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________


---

# Overall Data Transmission Summary

## Compliance Summary

**Total Assessment Areas:** _______

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Compliant | | |
| ⚠️ Partial | | |
| ❌ Non-Compliant | | |
| N/A Not Applicable | | |

**Instructions for Completion:**

- Count the number of each status across all 13 assessment sections
- Calculate percentage: (Count / Total Assessment Areas) × 100
- Exclude N/A items from total when calculating compliance percentage
- Target: ≥90% Compliant for mature ISMS


## Critical Gaps Identified

List the most critical gaps that require immediate attention:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

**Guidance:**

- Critical gaps typically include:
  - ❌ Non-Compliant items with Confidential/Restricted data exposure
  - Expired or soon-to-expire certificates (<30 days)
  - Prohibited protocols in active use (FTP, WEP, TLS 1.0/1.1)
  - Missing MFA on critical systems (VPN, production RDP)
  - Lack of certificate automation approaching March 2026 deadline
  - Self-signed certificates on production external services


## Top Remediation Priorities

| Priority | Gap Description | Target Date | Responsible Person |
|----------|-----------------|-------------|-------------------|
| **High** | | | |
| **High** | | | |
| **Medium** | | | |

**Priority Definitions:**

- **High:** Security risk, compliance violation, or operational failure imminent
- **Medium:** Compliance gap with planned remediation, low immediate risk
- **Low:** Best practice improvement, no compliance impact


---

# Evidence Register

**List all evidence files/documents referenced in this assessment:**

| Evidence ID | Description | Location | Date Collected |
|-------------|-------------|----------|----------------|
| EV-1.1-001 | SSL Labs report for www.example.com | /evidence/a824_1/ | DD.MM.YYYY |
| EV-1.1-002 | Certificate export for www.example.com | /evidence/a824_1/ | DD.MM.YYYY |
| | | | |
| | | | |

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1.1-PublicWebsite-20260115-SSLLabsReport.pdf`
- `EV-4.2-SSHServers-20260115-KeyAlgorithms.txt`
- `EV-6.2-CorporateWiFi-20260115-ControllerConfig.png`


**Evidence Types:**

- Configuration files (sanitized)
- Screenshots (timestamped)
- Scan results (SSL Labs, testssl.sh, nmap)
- Certificate exports (.pem, .cer)
- Policy documents
- Risk assessments
- Compliance reports
- Audit logs (sample extracts)


**Evidence Storage:**

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to security team and auditors
- **Sensitivity:** Mark according to data classification


**Quality Criteria:**

- Timestamped (date/time visible)
- Complete (not cropped unless sensitive)
- Attributable (clear which system)
- Verifiable (auditor can reproduce)
- Protected (stored securely, sanitized if needed)


---

# Approval and Sign-Off

## Assessment Summary

**Assessment Document:** ISMS-IMP-A.8.24.1 - Data Transmission Assessment  
**Assessment Period:** From __________ To __________  
**Overall Compliance Rate:** _______ % (from Summary Dashboard Section 8.1)  
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**

- Number of systems assessed: _______
- Compliant systems: _______
- Systems requiring remediation: _______
- Critical gaps identified: _______
- High-priority remediation items: _______


---

## Assessment Completed By

**Name:** _______________________  
**Role:** _______________________  
**Department:** _______________________  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all information is accurate to the best of my knowledge, and all evidence has been collected and verified.

---

## Reviewed By (Information Security Officer)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Review Outcome:**

- [ ] Approved - Assessment complete and accurate
- [ ] Approved with minor corrections - Specific items to address: _______
- [ ] Requires revision - Significant issues identified, re-submit required


---

## Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Approval Decision:**

- [ ] Approved - Compliance posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _______
- [ ] Rejected - Re-assessment required due to: _______


**Risk Acceptance:**
For any documented exceptions/deviations, I accept the residual risk based on:

- Documented risk assessment
- Approved compensating controls
- Business justification
- Compliance with exception approval process (ISMS-POL-A.8.24-S5.B)


**Budget Approval:**
Remediation budget requirement: _______

- [ ] Approved
- [ ] Requires further justification
- [ ] Deferred to next budget cycle


---

## Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Quarterly (every 3 months) or upon:

- Major infrastructure changes
- Security incidents involving encryption
- Policy updates
- Regulatory changes
- Failed audit findings
- Certificate automation deadline approaching (15.03.2026)


**Interim Monitoring:**

- Certificate expiration monitoring: Continuous (automated alerts)
- Configuration changes: Documented and verified
- New systems: Assessed before production deployment
- Remediation progress: Tracked monthly


---

## Distribution List

This assessment shall be distributed to:

- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] Network Engineering team
- [ ] System Administration team
- [ ] Compliance team
- [ ] Internal Audit
- [ ] IT Management
- [ ] Other: _______________________


**Storage Location:**

- **ISMS Repository:** `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
- **Filename:** `ISMS-IMP-A.8.24.1_Data_Transmission_[DATE]_APPROVED.xlsx`


---

# APPENDIX: Technical Notes for Workbook Developers

## A.1 Excel Workbook Structure

**Sheet Names (16 sheets total):**
1. Instructions & Legend
2. 1.1 External HTTPS-TLS
3. 1.2 Internal HTTPS-TLS
4. 2.1 Email Encryption
5. 2.2 Digital Signatures
6. 3.1 File Transfer Protocols
7. 4.1 VPN
8. 4.2 SSH
9. 4.3 RDP
10. 5.1 API Security
11. 6.1 Database Connections
12. 6.2 Wireless Networks
13. 7.1 Cloud Transmission
14. Summary Dashboard
15. Evidence Register
16. Approval Sign-Off

## A.2 Data Validation Rules

**Status Dropdown:**

- Formula: `"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"`
- Applied to: Status column in all assessment sheets
- Allow blank: No


**Remediation Needed Dropdown:**

- Formula: `"Yes,No"`
- Applied to: Remediation Needed column in all assessment sheets
- Allow blank: No


**Response Dropdown (Assessment Question):**

- Formula: `"Yes,No,Not Applicable"`
- Applied to: Response field for each section's assessment question
- Allow blank: No


**Certificate Automation Status (Section 1.1):**

- Formula: `"Fully automated,Partially automated,Manual (requires migration),Not applicable (internal only)"`
- Applied to: Certificate automation status field
- Allow blank: No


**Checklist Items:**

- Formula: `"Yes,No,N/A"`
- Applied to: All compliance checklist Status columns
- Allow blank: No


## A.3 Conditional Formatting

**Status Column:**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)
- N/A: No special formatting


**Certificate Validity Cells (Section 1.1):**

- If value >398 and date <15.03.2026: Yellow fill (warning - approaching deadline)
- If value >398 and date ≥15.03.2026: Red fill (non-compliant with SC-081v3)
- If value >200 and date ≥15.03.2026: Red fill
- If value >100 and date ≥15.03.2027: Red fill
- If value >47 and date ≥15.03.2029: Red fill


**Overall Compliance Percentage (Summary Dashboard):**

- ≥90%: Green fill
- 80-89%: Yellow fill
- <80%: Red fill


## A.4 Cell Protection

**Protected Cells (Formula/Static):**

- Column headers
- Instructions text
- Compliance checklist labels
- Status legend
- Summary Dashboard calculations
- Evidence Register ID auto-generation


**Unprotected Cells (User Input):**

- Assessment data entry tables (yellow fill)
- Compliance checklist status columns
- Additional Details fields
- Exception/Deviation documentation fields
- Evidence Register descriptions
- Approval Sign-Off fields


**Sheet Protection:**

- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet


## A.5 Summary Dashboard Formulas

**Compliance Percentage Calculation:**
```excel
=COUNTIF(DataRange,"✅ Compliant")/COUNTA(DataRange)*100
```

**Critical Gaps Count:**
```excel
=COUNTIF(DataRange,"❌ Non-Compliant")
```

**Sections Requiring Attention:**
```excel
=COUNTIFS(DataRange,"⚠️ Partial")+COUNTIFS(DataRange,"❌ Non-Compliant")
```

**Certificate Automation Status (Section 1.1):**
```excel
=IF(OR('1.1 External HTTPS-TLS'!AutomationStatus="Manual",'1.1 External HTTPS-TLS'!AutomationStatus="Partially automated"),"ACTION REQUIRED before 15.03.2026","Compliant")
```

## A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```

**Date Format:**
```excel
=TEXT(TODAY(),"DD.MM.YYYY")
```

## A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a824_1_data_transmission_assessment.py`

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Define cell styles, fonts, fills
- `get_column_definitions(section_key)`: Return column widths per section
- `create_assessment_sheet()`: Generic sheet generator with validation
- `create_summary_dashboard()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow


**Customization Points (marked with `# CUSTOMIZE:` in script):**

- Sheet names (if organizational naming differs)
- Dropdown options (if additional statuses needed)
- Data validation rules (if custom compliance criteria)
- Conditional formatting thresholds (if different color coding)


**Quality Assurance Script:** `excel_sanity_check_a824_1.py`

- Validates sheet structure matches specification
- Checks data validation rules are applied correctly
- Verifies conditional formatting ranges
- Tests formula accuracy
- Reports any discrepancies between script and specification


## A.8 Version Control

**Workbook Versioning:**

- Filename format: `ISMS-IMP-A.8.24.1_Data_Transmission_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision


**Change Log:**

- v1.0: Initial workbook structure
- v2.0: Updated certificate validity requirements (SC-081v3), added automation readiness assessment, added internal PKI distinction


**Backward Compatibility:**

- v2.0 workbooks can be opened in Excel 2016+
- v1.0 workbooks should be migrated to v2.0 to reflect updated certificate standards
- Migration script available: `normalize_assessment_files_a824.py`


---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.24.1 v1.0 document:**

1. **Document Control** (from PART I file, lines 1-30)
2. **PART I: USER COMPLETION GUIDE** (from PART I file, lines 31-440)
3. **PART II: TECHNICAL SPECIFICATION - File 1** (this file, all content)
4. **PART II: TECHNICAL SPECIFICATION - File 2** (next file, all content)

**Final Document Structure:**
```
ISMS-IMP-A.8.24.1 - Data Transmission Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~440 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Question-by-Question Guidance
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls
│   ├── 7. Quality Checklist
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~750 lines)
    ├── Instructions (with SC-081v3 update notice)
    ├── 1. HTTPS/TLS Implementation
    │   ├── 1.1 External Web Services (UPDATED - SC-081v3)
    │   └── 1.2 Internal Web Services (UPDATED - Internal PKI)
    ├── 2. Email Security
    ├── 3. Secure File Transfer
    ├── 4. Remote Access Protocols
    ├── 5. API Security
    ├── 6. Network Protocols
    ├── 7. Cloud Data Transmission
    ├── 8. Overall Summary
    ├── 9. Evidence Register
    ├── 10. Approval and Sign-Off
    └── Appendix: Technical Notes for Developers
```

**Quality Checks Before Finalizing:**

- [ ] All merge instructions removed
- [ ] Document Control version shows 2.0
- [ ] Version History documents v1.0 → v2.0 changes
- [ ] Certificate validity references SC-081v3 timeline throughout
- [ ] All dates in DD.MM.YYYY format
- [ ] Cross-references accurate (section numbers, policy references)
- [ ] No placeholder text remains (all [Organization] appropriate)
- [ ] Technical appendix matches Python script version


---

**END OF SPECIFICATION**

---

*"While asleep, I had an unusual experience. There was a red screen formed by flowing blood, and I was observing it. Suddenly a hand began to write on the screen."*
— Srinivasa Ramanujan

*Where bamboo antennas actually work.* 🎋
