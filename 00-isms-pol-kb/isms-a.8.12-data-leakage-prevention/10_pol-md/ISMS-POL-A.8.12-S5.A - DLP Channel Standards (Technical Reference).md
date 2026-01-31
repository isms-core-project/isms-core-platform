# ISMS-POL-A.8.12-S5.A
## Annex A: DLP Channel Standards

**Document ID**: ISMS-POL-A.8.12-S5.A  
**Title**: DLP Channel Standards (Technical Reference)  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Security Engineering Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | Security Engineering | Initial technical standards |

**Review Cycle**: Annual (or upon technology evolution)  
**Next Review Date**: 2026-01-03  
**Approvers**: Security Engineering Manager

**Distribution**: Security Engineering, IT Operations, DLP administrators  
**Related Documents**: ISMS-POL-A.8.12-S2.2 (Channel Protection Requirements)

---

## 1. Purpose

This annex provides **technology-neutral technical standards** for DLP channel protection. These standards translate policy requirements (S2.2) into measurable capabilities without specifying vendors.

**Use Case:** Procurement evaluation, solution validation, technology assessment

---

## 2. Email Channel Standards

### 2.1 Required Capabilities

**Content Inspection:**
- Scan email body, attachments, headers, embedded objects
- Support common file formats (Office, PDF, images, archives, text)
- Extract and inspect compressed archives (ZIP, RAR, 7z, TAR)
- Detect encrypted archives (flag for manual review)

**Detection Methods:**
- Regular expression (regex) pattern matching
- Keyword and phrase matching (context-aware)
- Document fingerprinting (exact and fuzzy match)
- Classification label detection (Microsoft Sensitivity Labels, Adobe AIP)
- Machine learning / AI-based classification (optional, recommended)

**Policy Actions:**
- Allow, Alert (log only), Block, Quarantine, Encrypt, Redirect
- User notification (configurable messaging)
- Manager notification workflow
- Exception approval workflow

### 2.2 Performance Standards

- **Latency:** <500ms average email scan time
- **Throughput:** Support peak email volume (measure: emails/second)
- **Availability:** >99.5% uptime during business hours

### 2.3 Integration Requirements

- SMTP gateway integration (inline or API-based)
- Microsoft 365 / Google Workspace native integration
- SIEM integration (Syslog, CEF, API)
- Ticketing system integration (ServiceNow, Jira, etc.)

---

## 3. Web/Cloud Channel Standards

### 3.1 Required Capabilities

**Content Inspection:**
- HTTP/HTTPS upload monitoring (POST requests)
- Cloud storage monitoring (Dropbox, Box, OneDrive, Google Drive)
- SaaS application monitoring (Salesforce, Workday, custom apps)
- Social media upload detection (LinkedIn, Facebook, Twitter)
- Code repository monitoring (GitHub, GitLab, Bitbucket)

**SSL/TLS Decryption:**
- Decrypt HTTPS traffic for inspection (with DPO approval)
- Certificate management (trusted CA, certificate pinning support)
- Decryption bypass for banking, healthcare, legal sites (privacy protection)

**Detection Methods:**
- URL categorization (via web filtering integration per ISMS-POL-A.8.23)
- File type detection (MIME type, magic bytes)
- Content inspection (same as email: regex, keywords, fingerprints, ML)

### 3.2 Cloud Access Security Broker (CASB) Integration

If organization uses CASB (Netskope, Zscaler, Palo Alto Prisma Access, Microsoft Defender for Cloud Apps):
- DLP policies deployed via CASB for cloud apps
- Shadow IT discovery (identify unapproved cloud usage)
- API-based CASB for sanctioned apps (M365, Salesforce, Box)
- Proxy-based CASB for all web traffic

### 3.3 Performance Standards

- **Latency:** <100ms additional latency for web browsing
- **Throughput:** Support peak bandwidth (measure: Gbps)
- **Availability:** >99.9% uptime (critical business path)

---

## 4. Endpoint Channel Standards

### 4.1 Required Capabilities

**Device Coverage:**
- Windows (10, 11, Server 2016+)
- macOS (last 3 major versions)
- Linux (Ubuntu, RHEL, limited support acceptable)
- VDI / Citrix / VMware Horizon (virtual desktops)

**Egress Vector Monitoring:**
- USB / Removable media (block, encrypt, whitelist)
- Print / Print-to-PDF (watermark, block, log)
- Clipboard / Copy-paste (monitor, block paste to unauthorized apps)
- Screen capture (disable, watermark)
- Bluetooth file transfer (OBEX block)
- Local application sync (personal Dropbox, OneDrive)

**Detection Methods:**
- File-based DLP (scan files at rest, in motion)
- Context-aware DLP (application control, user/device identity)
- Behavioral analytics (anomaly detection for mass transfers)

### 4.2 Agent Requirements

- Lightweight agent (<50MB disk, <100MB RAM)
- Offline mode (queue events when disconnected, sync when online)
- Tamper protection (prevent user disable/uninstall)
- Encrypted communication with management server
- Auto-update capability

### 4.3 Performance Standards

- **CPU Impact:** <5% average CPU utilization
- **Battery Impact:** <10% battery reduction (laptops)
- **User Experience:** No noticeable degradation of normal operations

---

## 5. Network Channel Standards

### 5.1 Required Capabilities

**Protocol Coverage:**
- SMB/CIFS (Windows file shares)
- FTP/SFTP/FTPS (file transfer)
- NFS (Unix file shares)
- SCP/Rsync (Unix file copy)
- WebDAV (web-based file access)

**Deployment Options:**
- Inline network appliance (proxy mode)
- Network TAP/SPAN (passive monitoring mode)
- Endpoint agent fallback (if network DLP gaps exist)

**Detection Methods:**
- Deep packet inspection (DPI)
- File reconstruction from network streams
- Content inspection (same patterns as email/web)

### 5.2 Performance Standards

- **Latency:** <10ms additional latency (inline mode)
- **Throughput:** Line-rate performance (10 Gbps minimum for enterprise)
- **Availability:** >99.9% uptime (redundant deployment recommended)

---

## 6. Application Channel Standards

### 6.1 Database Activity Monitoring (DAM)

**Required Capabilities:**
- Monitor database queries (SELECT, INSERT, UPDATE, DELETE)
- Alert on bulk exports (>1000 rows)
- Block unauthorized exports (per policy)
- Track privileged user activity (DBAs, developers)

**Supported Databases:**
- Microsoft SQL Server
- Oracle Database
- MySQL / MariaDB
- PostgreSQL
- NoSQL (MongoDB, Cassandra) - optional

### 6.2 API Monitoring

**Required Capabilities:**
- REST API monitoring (JSON/XML payload inspection)
- OAuth scope validation
- Rate limiting (detect data exfiltration via API)
- API call logging (user, endpoint, data volume)

### 6.3 Reporting Tools

**Required Capabilities:**
- Block or restrict export formats (allow PDF, block CSV/Excel)
- Watermark exported reports (classification, user ID, timestamp)
- Log report execution (user, report name, parameters, rows returned)

---

## 7. Mobile Channel Standards

### 7.1 Mobile Device Management (MDM) Integration

**Required Capabilities:**
- MDM integration (Microsoft Intune, VMware Workspace ONE, MobileIron)
- Mobile Application Management (MAM) for BYOD
- Containerization (corporate data isolation)

**Egress Vector Monitoring:**
- Mobile email (block attachments, enforce encryption)
- Mobile cloud apps (block personal cloud, allow corporate)
- Camera / Screenshots (disable in corporate container)
- AirDrop / Nearby Share (block file transfers)

### 7.2 Performance Standards

- **Battery Impact:** <15% battery reduction
- **User Experience:** Seamless corporate app access
- **Offline Mode:** Support offline work, sync when online

---

## 8. Logging and Reporting Standards

### 8.1 Log Requirements (per S2.3)

**Mandatory Log Fields:**
- Timestamp (UTC, ISO 8601 format)
- User identity (username, email, employee ID)
- Device/endpoint (hostname, IP, MAC, device ID)
- Channel (email, web, USB, network, application, mobile)
- Action (allow, block, alert, quarantine, encrypt)
- Data classification (Public, Internal, Confidential, Restricted)
- Data category (PII, financial, IP, credentials, business confidential)
- Volume (file size, record count)
- Rule matched (policy ID, rule name)
- Confidence score (if ML-based detection)

**Log Format:**
- Structured format (JSON, CEF, Syslog)
- SIEM-compatible (Splunk, Elastic, QRadar, Sentinel)

### 8.2 Retention Requirements (per S2.3)

- Active alerts: Retain until case closure + 90 days
- Resolved incidents: 2-7 years (per incident retention policy)
- Routine logs: 90-120 days
- Compliance logs: Per regulatory requirement (GDPR/FADP)

---

## 9. Integration Standards

### 9.1 SIEM Integration

**Required:**
- Real-time log forwarding (Syslog, CEF, API)
- Alert forwarding (Critical/High severity)
- Correlation ID support (link related events)

### 9.2 Incident Response Integration

**Required:**
- Ticketing system integration (auto-create tickets for High/Critical)
- Workflow automation (containment actions via API)
- Evidence export (forensic packages)

### 9.3 IAM Integration

**Recommended:**
- Active Directory / LDAP integration (user identity)
- Azure AD / Okta integration (cloud identity)
- HR system integration (departing employee flags)

---

## 10. Compliance and Audit Standards

### 10.1 Audit Trail Requirements

- Immutable audit logs (append-only, tamper-evident)
- Administrator action logging (config changes, exception approvals)
- Policy change tracking (version control, approval workflow)

### 10.2 Compliance Reporting

**Required Reports:**
- Coverage dashboard (% of users/devices/channels protected)
- Alert volume (daily/weekly/monthly trends)
- False positive rate (target <10% after 6 months)
- Incident summary (Critical/High incidents, resolutions)
- Exception register (active exceptions, approvals, expirations)

---

## 11. Vendor-Agnostic Capability Matrix

| Capability | Email | Web/Cloud | Endpoint | Network | Application | Mobile |
|------------|-------|-----------|----------|---------|-------------|--------|
| **Content Inspection** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Regex Patterns** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Fingerprinting** | ✓ | ✓ | ✓ | ✓ | Partial | Partial |
| **ML/AI Classification** | Recommended | Recommended | Recommended | Optional | Optional | Optional |
| **Block/Alert/Quarantine** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Encryption Support** | ✓ | N/A | ✓ (USB) | N/A | N/A | N/A |
| **Offline Mode** | N/A | N/A | ✓ | N/A | N/A | ✓ |
| **SIEM Integration** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 12. Testing and Validation

### 12.1 Acceptance Testing

Before production deployment, DLP solutions SHALL be tested for:

**Functional Testing:**
- Detection accuracy (true positive rate >90%)
- False positive rate (<10% after tuning)
- Policy action execution (block actually blocks, alert actually alerts)
- Exception workflow (approval, expiration, revocation)

**Performance Testing:**
- Latency impact (within standards per channel)
- Throughput capacity (peak load)
- Scalability (agent deployment to 1000+ endpoints)

**Integration Testing:**
- SIEM log forwarding (100% delivery rate)
- Ticketing system (auto-ticket creation)
- User notification (email delivery, message clarity)

### 12.2 Ongoing Validation

**Monthly:**
- Test sample detection rules (verify still working)
- Review false positive rates (identify tuning needs)
- Verify coverage (% of devices with active agents)

**Quarterly:**
- Full DLP assessment (ISMS-IMP-A.8.12.3 Channel Coverage)
- Penetration testing (attempt bypass, exfiltration)
- Compliance audit (logs retained, policies enforced)

---

**END OF DOCUMENT**

*"The best DLP technology is worthless if you don't configure it properly. These standards ensure you do."* 🎯