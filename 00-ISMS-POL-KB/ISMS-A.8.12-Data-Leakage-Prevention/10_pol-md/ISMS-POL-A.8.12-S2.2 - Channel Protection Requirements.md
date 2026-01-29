**Dependency:**  
Channel protection requirements depend on **S2.1 (Data Classification)** output. Organizations must know **what data** to protect before defining **how to protect** it across channels.

---

## 2. Channel Coverage Philosophy

### 2.1 Defense in Depth

Organizations SHALL implement DLP protection across **multiple layers**:

| Layer | Protection Mechanism | Coverage |
|-------|---------------------|----------|
| **Network Perimeter** | Network-based DLP (inline appliances, proxies) | Email gateway, web proxy, network egress |
| **Endpoint** | Endpoint DLP agents | USB, print, clipboard, screenshots, local file operations |
| **Cloud** | Cloud Access Security Broker (CASB) or cloud-native DLP | SaaS, cloud storage, cloud applications |
| **Application** | Application-level controls | Database exports, API calls, reporting functions |

**Rationale:** Single-layer protection creates bypass opportunities. Attackers circumvent network DLP via personal hotspots or encrypted tunnels. Endpoint DLP provides last-mile protection.

### 2.2 Phased Deployment by Channel Risk

Organizations SHALL prioritize channel protection based on **exfiltration risk**:

| Priority Tier | Channels | Rationale | Deployment Timeline |
|---------------|----------|-----------|---------------------|
| **Tier 1 (Critical)** | Email, Web uploads, USB drives | Highest volume, easiest to exploit | Months 1-3 |
| **Tier 2 (High)** | Cloud storage (SaaS), Mobile devices | Growing attack surface, shadow IT | Months 4-6 |
| **Tier 3 (Medium)** | Network file shares, Print | Lower volume, monitored environments | Months 7-9 |
| **Tier 4 (Low)** | Bluetooth, optical drives, screen capture | Niche attack vectors | Months 10-12 |

**Resource Constraints:** If simultaneous deployment is infeasible, Tier 1 channels MUST be protected first. Tier 2-4 deployment MAY be deferred with documented risk acceptance.

### 2.3 Technology Neutrality

Channel protection requirements are **vendor-agnostic**. Organizations MAY implement protection using:
- **Network-based DLP** (e.g., Symantec DLP, Forcepoint DLP, McAfee DLP)
- **Endpoint DLP** (e.g., Microsoft Purview Endpoint DLP, Forcepoint Endpoint, Digital Guardian)
- **Cloud-native DLP** (e.g., Microsoft Purview, Google Workspace DLP, Salesforce Shield)
- **CASB solutions** (e.g., Netskope, Zscaler, Microsoft Defender for Cloud Apps)
- **Custom solutions** (e.g., in-house scripts, open-source tools)

**Requirement:** Technology must meet stated capabilities. Implementation is documented in **ISMS-IMP-A.8.12.3 (Channel Coverage Assessment)**.

---

## 3. Email Channel Protection

### 3.1 Email Channel Scope

**In-Scope Email Systems:**
- **SMTP** (Simple Mail Transfer Protocol - traditional email)
- **Webmail** (browser-based email access - Gmail, Outlook.com, Yahoo)
- **Microsoft 365** (Exchange Online, Outlook, Teams email integration)
- **Google Workspace** (Gmail, Google Vault)
- **Email attachments** (all file types, encrypted archives, embedded objects)

**Out-of-Scope:**
- Internal email (internal-to-internal) MAY have reduced DLP protection (monitoring-only vs. blocking)
- Personal email on personal devices (non-BYOD) outside organizational control

### 3.2 Email DLP Requirements

Organizations SHALL implement email DLP with the following capabilities:

#### 3.2.1 Content Inspection

**Requirement:** Email DLP SHALL inspect:
- **Email body** (plain text, HTML, rich text formats)
- **Email attachments** (Office documents, PDFs, images, archives, encrypted files)
- **Email headers** (sender, recipient, subject line for classification markers)
- **Embedded objects** (OLE objects, macros, hidden content)

**Encrypted Attachments:** Organizations SHOULD implement:
- Password-protected archive detection (`.zip`, `.7z`, `.rar` with password)
- User notification requirement (decrypt for inspection or manager approval)
- Quarantine for manual review (high-risk scenarios)

#### 3.2.2 Detection Methods

**Requirement:** Email DLP SHALL support:
- **Pattern matching** (PII, credit cards, SSN, IBAN, etc. - per S2.1)
- **Keyword matching** (classification labels, project code names)
- **Fingerprinting** (exact/partial match for sensitive documents)
- **Contextual analysis** (sender/recipient whitelisting, authorized business partners)

#### 3.2.3 Policy Actions

**Requirement:** Email DLP SHALL support the following actions:

| Action | Use Case | Data Classification |
|--------|----------|---------------------|
| **Allow** | Internal email, public data | Public, Internal |
| **Alert** (monitor-only) | Initial tuning phase, low-risk confidential data | Confidential (initial deployment) |
| **Block** | External transfer of restricted data | Restricted, high-risk Confidential |
| **Quarantine** | Suspicious transfers requiring manager approval | Ambiguous scenarios (e.g., Finance sending invoices to new vendor) |
| **Encrypt** | Authorized external transfer with encryption | Confidential data to approved partners |
| **Redirect** | Route email through secure portal or encrypted channel | PII to external parties (FADP/GDPR compliance) |

**Mandatory Blocking:** Organizations SHALL block:
- **Credentials/secrets** (passwords, API keys, private keys) to any external recipient
- **Payment card data** (PCI DSS scope) to unauthorized recipients
- **Special categories of PII** (GDPR Article 9: health data, biometric data) to external recipients without encryption and legal basis

#### 3.2.4 Exception Management

**Requirement:** Organizations SHALL implement exception workflow for email DLP:
- User requests exception (business justification required)
- Manager approves exception (time-limited, e.g., 7-30 days)
- Security team documents exception (ISMS-POL-A.8.12-S5.B Exception Request Template)
- Audit trail maintained (who, what, when, why)

**Exception Criteria:**
- Legitimate business need (customer communication, partner collaboration)
- No alternative secure channel available
- Risk acceptance by data owner
- Compensating controls (encryption, redaction, password protection)

### 3.3 Specific Email Channel Requirements

#### 3.3.1 SMTP (Traditional Email)

Organizations SHALL:
- Deploy DLP at **email gateway** (inline inspection before delivery)
- Inspect **outbound email only** (inbound email is threat protection, not DLP)
- Support **TLS encryption** (STARTTLS) for encrypted email channels
- Integrate with **SIEM** for alert correlation

#### 3.3.2 Microsoft 365 / Exchange Online

Organizations SHALL:
- Implement **Microsoft Purview DLP** (native cloud DLP) OR
- Deploy **CASB solution** with M365 integration (e.g., Defender for Cloud Apps)
- Configure **sensitivity labels** (classification-based DLP policies)
- Enable **audit logging** (Microsoft 365 Compliance Center)

**Cloud Provider Reference:** See **ISMS-REF-A.5.23 (Cloud Service Provider Registry)** for Microsoft 365 DLP capabilities and integration options.

#### 3.3.3 Google Workspace / Gmail

Organizations SHALL:
- Implement **Google Workspace DLP** (native Gmail DLP) OR
- Deploy **CASB solution** with Google Workspace integration
- Configure **content compliance rules** (Google Admin Console)
- Enable **audit logging** (Google Vault, Cloud Logging)

#### 3.3.4 Webmail (Personal Email via Browser)

Organizations SHALL:
- **Block** or **monitor** access to webmail (Gmail.com, Outlook.com, Yahoo Mail) via web filtering (ISMS-POL-A.8.23 Web Filtering)
- Deploy **endpoint DLP** to detect copy-paste from corporate email to webmail
- Use **CASB** to detect cloud-based webmail usage (shadow IT detection)

**Risk:** Personal webmail is primary channel for insider data exfiltration. Organizations SHOULD block personal webmail for users with access to Confidential/Restricted data.

---

## 4. Web/Cloud Channel Protection

### 4.1 Web/Cloud Channel Scope

**In-Scope:**
- **HTTP/HTTPS uploads** (web forms, file upload dialogs)
- **Cloud storage** (Dropbox, Box, Google Drive, OneDrive, iCloud)
- **SaaS applications** (Salesforce, Workday, ServiceNow, Zendesk, etc.)
- **File sharing** (WeTransfer, SendAnywhere, Firefox Send)
- **Social media** (LinkedIn, Facebook, Twitter - posting confidential info)
- **Code repositories** (GitHub, GitLab, Bitbucket - source code leakage)

**Out-of-Scope:**
- **Approved cloud services** with DLP integration (e.g., company OneDrive with Microsoft Purview DLP)

### 4.2 Web/Cloud DLP Requirements

Organizations SHALL implement web/cloud DLP with the following capabilities:

#### 4.2.1 Content Inspection

**Requirement:** Web DLP SHALL inspect:
- **HTTP/HTTPS POST requests** (file uploads, form submissions)
- **Cloud API traffic** (REST API calls, OAuth-authenticated sessions)
- **SSL/TLS encrypted traffic** (HTTPS inspection, SSL decryption)
- **Uploaded file content** (same detection as email: patterns, keywords, fingerprinting)

**SSL/TLS Decryption Considerations:**
- **Privacy concern:** HTTPS inspection decrypts all web traffic (employee browsing)
- **Legal requirement:** Consult DPO/Legal before deploying (employee notification, works council)
- **Technical challenge:** Certificate trust, performance impact
- **Risk-based approach:** Decrypt only for users with Confidential/Restricted data access

Organizations SHOULD implement SSL/TLS decryption for DLP, with documented legal basis and proportionality assessment.

#### 4.2.2 Cloud Application Control

**Requirement:** Organizations SHALL:
- **Whitelist approved cloud services** (corporate OneDrive, approved SaaS)
- **Block unauthorized cloud storage** (personal Dropbox, Google Drive, iCloud)
- **Monitor shadow IT** (detect usage of unapproved SaaS applications)
- **Enforce DLP policies** on whitelisted cloud services (via CASB or cloud-native DLP)

**Cloud Service Categories (ISMS-REF-A.5.23):**
- **Tier 1-2 (Critical):** Require CASB or cloud-native DLP (Microsoft 365, Google Workspace, Salesforce)
- **Tier 3-5 (High):** Risk assessment required, DLP recommended
- **Tier 6-10 (Medium/Regional):** Usage allowed with monitoring, DLP optional

#### 4.2.3 File Upload Protection

**Requirement:** Organizations SHALL:
- **Block uploads of sensitive file types** to unauthorized sites:
  - Office documents (`.docx`, `.xlsx`, `.pptx`) containing confidential data
  - Archives (`.zip`, `.7z`, `.rar`) with confidential files
  - Source code files (`.java`, `.py`, `.cpp`, `.cs`)
  - Database exports (`.csv`, `.sql`, `.db`)
- **Alert on suspicious upload patterns**:
  - Large file uploads (>100MB) to personal cloud storage
  - Multiple file uploads in short time (>50 files in 10 minutes)
  - Uploads to newly registered domains (potential phishing/exfiltration sites)

#### 4.2.4 Code Repository Protection

**Requirement:** Organizations SHALL:
- Monitor **GitHub, GitLab, Bitbucket** for:
  - Public repository creation with corporate code
  - Credential commits (API keys, passwords in code)
  - Large binary file uploads (data exfiltration disguised as code commits)
- Deploy **GitHub Advanced Security** or equivalent for secret scanning
- Integrate **endpoint DLP** to detect `git push` commands with sensitive data

### 4.3 Specific Web/Cloud Requirements

#### 4.3.1 Cloud Storage (Dropbox, Box, Google Drive, OneDrive)

Organizations SHALL:
- **Block personal cloud storage** for users with Restricted data access
- **Allow corporate cloud storage** with DLP enforcement (Microsoft 365 DLP, Google Workspace DLP, Box Shield)
- **Monitor shadow IT** cloud storage via CASB (detect unapproved usage)

#### 4.3.2 SaaS Applications (Salesforce, Workday, ServiceNow)

Organizations SHALL:
- Assess SaaS applications for DLP capabilities (ISMS-REF-A.5.23)
- Deploy **CASB** for SaaS without native DLP
- Configure **data export controls** (prevent CSV exports, report downloads)

#### 4.3.3 Web-Based File Sharing (WeTransfer, SendAnywhere)

Organizations SHALL:
- **Block** web-based file sharing sites for users with Confidential/Restricted data
- **Monitor** usage via web filtering logs (ISMS-POL-A.8.23)

---

## 5. Endpoint Channel Protection

### 5.1 Endpoint Channel Scope

**In-Scope Endpoints:**
- **Corporate laptops and desktops** (Windows, macOS, Linux)
- **BYOD devices** with access to corporate data (managed via MDM/MAM)
- **Virtual desktops (VDI/DaaS)** (Citrix, VMware Horizon, Windows Virtual Desktop)

**In-Scope Egress Vectors:**
- **USB drives** (flash drives, external hard drives)
- **Removable media** (optical drives - CD/DVD/Blu-ray, SD cards)
- **Print** (physical printers, print-to-PDF, print-to-file, virtual printers)
- **Clipboard** (copy-paste to unauthorized applications)
- **Screen capture** (screenshots, screen recording)
- **Bluetooth** (file transfers to mobile devices, wireless speakers)
- **Local applications** (unauthorized file sync clients, messaging apps)

### 5.2 Endpoint DLP Requirements

Organizations SHALL deploy **endpoint DLP agents** on all corporate endpoints processing Confidential/Restricted data.

#### 5.2.1 USB/Removable Media Control

**Requirement:** Organizations SHALL:
- **Block** USB storage devices for users with Restricted data access
- **Monitor** USB usage for users with Confidential data access (alert on large transfers)
- **Whitelist** approved USB devices (encrypted USB drives, authorized peripherals)
- **Enforce encryption** for authorized USB transfers (BitLocker To Go, encrypted volumes)

**Exception Management:**
- Users MAY request USB exception (temporary, time-limited)
- Manager approval required (business justification)
- Compensating controls enforced (encryption, read-only mode)

**Device Categories:**
- **Block:** USB storage (flash drives, external HDDs)
- **Allow:** USB peripherals (keyboards, mice, printers, webcams)
- **Monitor:** Hybrid devices (smartphones with USB storage mode)

#### 5.2.2 Print Control

**Requirement:** Organizations SHALL:
- **Monitor** printing of Confidential/Restricted documents
- **Watermark** printed documents with classification labels, user ID, timestamp
- **Log** all print jobs (document name, page count, printer, user, timestamp)
- **Block** print-to-PDF for Restricted data (without manager approval)

**Print Scenarios:**
- **Physical printers:** Monitor, watermark, log
- **Print-to-PDF:** Block (high risk - PDF easily uploaded to cloud)
- **Print-to-file** (XPS, PostScript): Block (similar to PDF risk)
- **Virtual printers** (print-to-email, print-to-cloud): Block

#### 5.2.3 Clipboard and Screen Capture Control

**Requirement:** Organizations SHALL:
- **Monitor** clipboard operations (copy from corporate apps to personal apps)
- **Block** clipboard paste to unauthorized applications (personal webmail, messaging)
- **Disable** screen capture utilities (screenshots, screen recording) for Restricted data applications
- **Watermark** screen content (visible overlay with user ID, classification)

**Technical Challenges:**
- Clipboard monitoring is **challenging** on macOS/Linux (limited OS APIs)
- Screen capture blocking has **usability impact** (users accustomed to screenshots)
- Organizations SHOULD implement for **high-value applications** (financial systems, HR portals) rather than all apps

#### 5.2.4 Bluetooth Control

**Requirement:** Organizations SHALL:
- **Block** Bluetooth file transfers (OBEX protocol) for users with Restricted data
- **Allow** Bluetooth peripherals (keyboards, mice, headsets) with device whitelisting
- **Monitor** Bluetooth activity for anomaly detection (large data transfers)

#### 5.2.5 Application Control

**Requirement:** Organizations SHALL:
- **Block** unauthorized file sync applications (personal Dropbox client, Google Drive sync)
- **Block** unauthorized messaging applications (WhatsApp Desktop, Telegram, Signal) for file sharing
- **Whitelist** approved applications (corporate messaging, authorized file sync)

**Integration with Application Control (ISMS-POL-A.8.26):**  
Endpoint DLP complements application whitelisting. If unauthorized app is blocked, DLP cannot be bypassed through it.

### 5.3 Endpoint OS-Specific Requirements

#### 5.3.1 Windows Endpoints

Organizations SHALL:
- Deploy **Microsoft Purview Endpoint DLP** OR third-party endpoint DLP
- Integrate with **Windows Defender for Endpoint** (behavioral analytics)
- Enforce **BitLocker** encryption for USB exemptions

#### 5.3.2 macOS Endpoints

Organizations SHALL:
- Deploy **macOS-compatible endpoint DLP** (Microsoft Purview, Forcepoint, Digital Guardian)
- Address macOS limitations (System Extensions, TCC permissions)
- Implement **FileVault** encryption for USB exemptions

#### 5.3.3 Linux Endpoints

Organizations SHOULD:
- Assess endpoint DLP support for Linux (limited vendor support)
- Consider **manual controls** (disable USB in BIOS, audit logging) if endpoint DLP unavailable
- Restrict Linux endpoints to non-Confidential data if DLP cannot be enforced

---

## 6. Network Channel Protection

### 6.1 Network Channel Scope

**In-Scope Protocols:**
- **SMB/CIFS** (Windows file sharing)
- **FTP/SFTP** (File Transfer Protocol)
- **NFS** (Network File System)
- **SCP** (Secure Copy Protocol)
- **Rsync** (file synchronization)
- **WebDAV** (web-based file access)

### 6.2 Network DLP Requirements

Organizations SHALL implement network-based DLP to inspect:
- **SMB file shares** (copy to external shares, unauthorized NAS devices)
- **FTP transfers** (outbound file uploads to FTP servers)
- **Unauthorized protocols** (peer-to-peer, tunneling protocols)

**Deployment:**
- **Inline network DLP appliance** (Symantec DLP Network Prevent, Forcepoint DLP)
- **Network TAP/SPAN** (passive monitoring if inline not feasible)
- **Integration with firewall** (protocol blocking, policy enforcement)

**Limitations:**
- Network DLP effectiveness limited by **encryption** (SSH, SFTP, encrypted tunnels)
- Organizations SHOULD combine with **endpoint DLP** for comprehensive coverage

---

## 7. Application Channel Protection

### 7.1 Application Channel Scope

**In-Scope Applications:**
- **Databases** (SQL exports, query results, CSV exports)
- **Reporting tools** (Crystal Reports, Tableau, Power BI exports)
- **CRM systems** (Salesforce data exports, contact list downloads)
- **ERP systems** (SAP, Oracle, financial report exports)
- **APIs** (REST/SOAP API data exfiltration)

### 7.2 Application DLP Requirements

Organizations SHALL implement application-level controls:

#### 7.2.1 Database Activity Monitoring (DAM)

**Requirement:** Organizations SHALL:
- Monitor **bulk database queries** (SELECT statements returning >1000 rows)
- Alert on **data exports** (CSV, Excel, SQL dumps)
- Block **unauthorized exports** by non-privileged users
- Integrate with **SIEM** for correlation (unusual export patterns)

#### 7.2.2 API Access Controls

**Requirement:** Organizations SHALL:
- Enforce **rate limiting** on sensitive API endpoints (prevent bulk data extraction)
- Require **OAuth scopes** for API data access (principle of least privilege)
- Log **API calls** with data volume metrics (monitor for exfiltration)

#### 7.2.3 Reporting Tool Controls

**Requirement:** Organizations SHALL:
- Restrict **report export formats** (allow PDF view, block CSV/Excel exports)
- Watermark **exported reports** (user ID, timestamp, classification)
- Audit **report execution** (who ran what report, when, data volume)

---

## 8. Mobile Channel Protection

### 8.1 Mobile Channel Scope

**In-Scope Devices:**
- **Corporate-owned mobile devices** (smartphones, tablets)
- **BYOD devices** with access to corporate data (MDM/MAM-managed)

**In-Scope Egress Vectors:**
- **Mobile email** (native email apps, webmail via mobile browser)
- **Mobile apps** (Dropbox, Google Drive, OneDrive mobile apps)
- **Camera** (photographing computer screens, documents)
- **Screenshots** (screen capture on mobile devices)
- **Messaging apps** (WhatsApp, Signal, Telegram file sharing)
- **AirDrop / Nearby Share** (wireless file transfers)

### 8.2 Mobile DLP Requirements

Organizations SHALL implement **Mobile Device Management (MDM)** or **Mobile Application Management (MAM)** with DLP capabilities:

#### 8.2.1 Corporate Data Containerization

**Requirement:** Organizations SHALL:
- Isolate **corporate data** in secure container (work profile)
- Block **copy-paste** between corporate and personal apps
- Prevent **screenshots** in corporate apps (Confidential/Restricted data)
- Disable **camera** access from corporate apps (prevent photo-based exfiltration)

#### 8.2.2 Mobile Email and Cloud Controls

**Requirement:** Organizations SHALL:
- Enforce **mobile email DLP** (Microsoft Intune, Google Workspace mobile DLP)
- Block **personal cloud app access** to corporate data (prevent "Open In..." to Dropbox)
- Require **encryption** for mobile data storage

#### 8.2.3 BYOD-Specific Controls

**Requirement:** Organizations SHALL:
- Deploy **MAM** (app-level controls) rather than full MDM (device control) for BYOD
- Enforce **selective wipe** (remove corporate data without wiping personal data)
- Restrict **Confidential/Restricted data access** from BYOD unless enhanced controls deployed

---

## 9. Channel Coverage Measurement

### 9.1 Coverage Metrics

Organizations SHALL measure channel protection coverage:

| Metric | Formula | Target |
|--------|---------|--------|
| **Email Coverage** | (Protected email systems / Total email systems) × 100% | >95% |
| **Web Coverage** | (Users with web DLP / Total users) × 100% | >90% |
| **Endpoint Coverage** | (Endpoints with DLP agent / Total endpoints) × 100% | >95% |
| **Cloud Coverage** | (Protected cloud services / Total cloud services in use) × 100% | >80% |
| **Mobile Coverage** | (MDM/MAM-managed devices / Mobile devices with corporate data) × 100% | >90% |

### 9.2 Gap Analysis

Organizations SHALL:
- Document **unprotected channels** (ISMS-IMP-A.8.12.3 Gap Analysis sheet)
- Assess **risk** of each gap (likelihood × impact)
- Create **remediation plan** (timeline, budget, owner)
- Accept **residual risk** for low-priority gaps (CISO approval)

---

## 10. Integration with DLP Framework

### 10.1 Assessment Integration

Channel protection SHALL be assessed using **ISMS-IMP-A.8.12.3 (Channel Coverage Assessment)** workbook, evaluating:
- Deployment status per channel (Yes/No/Partial/Planned)
- DLP technology used (vendor-agnostic documentation)
- Coverage percentage (% of users, devices, traffic protected)
- Policy enforcement mode (monitor-only, alert, block)
- Exception count and justification

### 10.2 Monitoring Integration

Channel protection generates alerts for **S2.3 (Monitoring & Detection)**:
- Email DLP alerts → SOC triage
- Web DLP alerts → Security team investigation
- Endpoint DLP alerts → User education or incident response
- Mobile DLP alerts → MDM admin review

---

## 11. References

### 11.1 Internal Policy Documents

- **ISMS-POL-A.8.12** - Master DLP Policy
- **ISMS-POL-A.8.12-S2.1** - Data Classification & Identification
- **ISMS-POL-A.8.12-S2.3** - Monitoring & Detection
- **ISMS-POL-A.8.23** - Web Filtering (web channel overlap)
- **ISMS-REF-A.5.23** - Cloud Service Provider Registry

### 11.2 Implementation Documents

- **ISMS-IMP-A.8.12.3** - Channel Coverage Assessment

### 11.3 Regulatory References

- **ISO/IEC 27002:2022** - Control 5.14 (Information Transfer), Control 8.12 (Data Leakage Prevention)
- **Swiss FADP** - Article 8 (Data security), Article 26 (Employee monitoring)
- **EU GDPR** - Article 32 (Security of processing)

---

**END OF DOCUMENT**

*"The best DLP policy is worthless if you forget to protect the USB port."*  
*— Murphy's Law of Data Leakage*