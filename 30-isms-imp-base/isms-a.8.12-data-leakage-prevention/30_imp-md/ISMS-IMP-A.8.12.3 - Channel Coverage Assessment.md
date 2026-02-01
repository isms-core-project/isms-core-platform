**ISMS-IMP-A.8.12.3 - Channel Coverage Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.3 |
| **Version** | 1.0 |
| **Assessment Area** | DLP Channel Coverage and Policy Effectiveness |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - Section 2.2 |
| **Purpose** | Assess DLP deployment across all data egress channels to identify coverage gaps, verify policy enforcement, and ensure no data exfiltration bypass paths exist |
| **Target Audience** | DLP Administrators, Security Engineers, Network Engineers, SOC Analysts, CISO, Compliance Officers |
| **Assessment Type** | Technical Coverage & Policy Verification |
| **Review Cycle** | Quarterly or After Network/Application Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Channel Coverage assessment | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** DLP Administrators, Security Engineers, Network Engineers, SOC Analysts

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **DLP channel coverage completeness** to ensure compliance with ISO/IEC 27001:2022 Control A.8.12 and eliminate data exfiltration bypass paths.

**Scope:** 7 data egress channel categories covering all possible data leakage paths:
1. **Email Channel** - SMTP/Exchange/M365/Google Workspace, attachments, encryption, external domains
2. **Web Channel** - HTTP/HTTPS uploads, webmail, cloud storage, file sharing, social media
3. **Endpoint Channel** - USB/removable media, clipboard, print, screen capture, local file operations, Bluetooth
4. **Network Channel** - FTP/SFTP, network shares, data in transit, tunneling protocols
5. **Cloud Channel** - SaaS applications, cloud storage, API-based exports, OAuth integrations
6. **Mobile Channel** - Mobile devices, BYOD, MDM-managed devices, mobile apps
7. **Application Channel** - Database exports, application APIs, bulk data downloads, reporting tools

**Assessment Output:** Excel workbook with ~70 channel coverage checkpoints documenting DLP deployment status per channel, policy effectiveness, bypass testing results, and coverage gap remediation plans.

## Why This Matters

**ISO 27001:2022 Control A.8.12 Requirement:**
> *"Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information."*

**Critical Principle:** DLP is only effective if it covers **ALL** data egress paths. A single unprotected channel creates a bypass that renders entire DLP investment ineffective.

**Regulatory Context:**

- **Swiss nDSG (Art. 8):** Requires appropriate organizational and technical measures against data loss
- **EU GDPR (Art. 32):** Technical measures must be appropriate to the risk (gaps = inadequate measures)
- **Industry Standards:** PCI DSS (Req. 4), HIPAA (§164.312), SOC 2 all require comprehensive data egress protection


**Business Impact:**

- **Data Exfiltration Bypasses:** 80% of insider data theft uses unprotected channels (USB, personal cloud, mobile)
- **Compliance Violations:** Auditors specifically test for DLP bypass paths - gaps = audit findings
- **ROI on DLP:** DLP investment wasted if attackers/insiders can simply use unprotected channels
- **Shadow IT Risk:** Unmanaged cloud services, mobile apps, personal devices create coverage gaps


**Why Channel Coverage Assessment Matters:**

- **Gap Identification:** Which channels lack DLP protection? (USB blocked but Bluetooth open = gap)
- **Policy Effectiveness:** Is DLP deployed but not actually blocking sensitive data? (monitor-only mode)
- **Bypass Testing:** Can users/attackers circumvent DLP using alternative channels?
- **Integration Validation:** Are DLP policies consistent across channels or fragmented?


## Who Should Complete This Assessment

**Primary Responsibility:** DLP Administrators, Security Engineers with cross-functional system knowledge

**Required Knowledge:**

- [Organization]'s complete data egress channel inventory (all ways data can leave organization)
- DLP deployment architecture across all channels
- Network topology including internet egress points, cloud connections, VPNs
- Endpoint configurations (USB policies, clipboard restrictions, print management)
- Cloud application portfolio (sanctioned SaaS, shadow IT)
- Mobile device management (MDM) policies and coverage


**Support Roles:**

- **Network Engineers:** Network-level DLP, firewall rules, proxy configurations, cloud gateways
- **Endpoint Teams:** Endpoint DLP, USB blocking, clipboard management, print restrictions
- **Email Administrators:** Email gateway DLP, attachment scanning, encryption policies
- **Cloud/SaaS Teams:** CASB deployment, SaaS DLP, API monitoring, OAuth application review
- **Mobile Device Management:** MDM policies, BYOD enrollment, mobile DLP apps
- **Application Owners:** Database export restrictions, API rate limits, bulk download controls
- **SOC Analysts:** DLP alert monitoring, bypass attempt detection, incident response


## Time Estimate

**Total Assessment Time:** 6-8 hours (depending on channel complexity and organization size)

**Breakdown:**

- **Channel Inventory:** 1-2 hours (identify all data egress paths, document each channel)
- **Coverage Verification:** 2-3 hours (verify DLP deployment per channel, review policies)
- **Bypass Testing:** 1-2 hours (attempt data exfiltration via each channel, document results)
- **Policy Effectiveness Review:** 1-2 hours (test DLP detection/blocking accuracy per channel)
- **Evidence Collection:** 30-60 minutes (screenshots, test results, configuration exports)
- **Quality Review:** 30 minutes (self-check using Section 7 quality checklist)


**Pro Tip:** For organizations with >500 employees or complex multi-site deployments, consider splitting by channel:

- Day 1: Email + Web channels (Network/Email admins)
- Day 2: Endpoint + Mobile channels (Endpoint/MDM teams)
- Day 3: Network + Cloud + Application channels (Cloud/Network/App teams)
- Day 4: Consolidation, bypass testing, gap analysis (DLP admin)


## Connection to Policy

This assessment implements **ISMS-POL-A.8.12 (Data Leakage Prevention Policy)** Section 2.2 (Channel Protection Requirements) which mandates:

**Policy Requirements Verified:**

- **Section 2.2 - Channel Protection:** DLP controls on email, web, endpoint, network, cloud, mobile, application channels
- **Section 2.2 - Coverage Completeness:** No unprotected data egress paths (bypass prevention)
- **Section 2.2 - Policy Enforcement:** DLP set to blocking mode for Restricted/Confidential data (not just monitoring)
- **Section 3.2 - Assessment & Verification:** Quarterly channel coverage review, bypass testing
- **Section 4.2 - Implementation Resources:** Structured assessment workbooks


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all data egress channels

**Relationship to Other Assessments:**

- **A.8.12.1 (DLP Infrastructure):** Verifies DLP technology exists → THIS assessment verifies WHERE it's deployed
- **A.8.12.2 (Data Classification):** Defines WHAT data to protect → THIS assessment verifies ALL CHANNELS are protected
- **A.8.12.4 (Monitoring & Response):** Assesses alerting → THIS assessment ensures channels generate alerts when data leaked
- **A.8.12.5 (Compliance Dashboard):** Consolidates all assessments → THIS provides channel coverage metrics


## Critical: Coverage Gap = Bypass Risk

**⚠️ IMPORTANT - Every Unprotected Channel is a Data Leakage Bypass:**

Organizations often deploy DLP on "obvious" channels (email, web) but miss "alternative" channels that attackers/insiders readily exploit.

**Common Bypass Scenarios:**

| Protected Channel | Unprotected Bypass | Result |
|-------------------|-------------------|--------|
| ✅ Email DLP blocks attachments | ❌ No USB blocking | User copies to USB, takes home |
| ✅ Web DLP blocks Dropbox uploads | ❌ Mobile devices not managed | User uploads via mobile Dropbox app |
| ✅ Network DLP monitors FTP | ❌ No cloud app DLP | User exports to personal OneDrive |
| ✅ Endpoint DLP blocks clipboard | ❌ Bluetooth file transfer allowed | User sends file via Bluetooth to phone |
| ✅ Email encryption required | ❌ No print management | User prints confidential document, walks out |
| ✅ Database export logging | ❌ API rate limits not enforced | User scripts API to export entire database |

**Real-World Example:**

- Organization deployed email DLP (99% of sensitive data sent via email)
- Did NOT deploy USB blocking (assumed "users don't use USB anymore")
- Insider copied 50GB customer database to USB drive, walked out
- DLP completely bypassed, no alert generated
- Post-incident: "We had DLP, how did this happen?" → Coverage gap


**Attacker/Insider Behavior:**

- **Path of least resistance:** Will use whichever channel is unprotected
- **Reconnaissance:** Test each channel to find gaps (send test file via email, web, USB, etc.)
- **Adaptation:** If email blocked, try web; if web blocked, try USB; if USB blocked, try mobile
- **Obfuscation:** Rename file extensions, encrypt, split into parts to evade detection


**What This Means for Assessment:**
1. **Complete channel inventory required** - Can't protect what you don't know exists
2. **Assume attackers know your gaps** - Red team mindset: "How would I exfiltrate data if I were malicious insider?"
3. **Single gap = total failure** - 6/7 channels protected but 1 unprotected = DLP ineffective
4. **Bypass testing mandatory** - Don't assume DLP works, test it on every channel
5. **Remediation priority:** Unprotected channels = Critical risk (fix immediately)

---

# Prerequisites

## Access Required

**Network & Infrastructure Documentation:**

- [ ] Network topology diagram (all internet egress points, VPN exits, cloud connections)
- [ ] Data flow diagrams (how data moves between systems and out of organization)
- [ ] Firewall rules and access control lists (what traffic is allowed outbound)
- [ ] Proxy/web gateway configurations (which URLs/categories allowed)
- [ ] VPN configurations (split tunnel vs. full tunnel, DLP enforcement on VPN)


**System Access:**

- [ ] DLP management consoles (all DLP products deployed)
- [ ] Email gateway administration (email DLP, attachment policies, encryption)
- [ ] Web proxy/CASB administration (web DLP, cloud app blocking, SSL inspection)
- [ ] Endpoint management console (USB policies, clipboard restrictions, print management)
- [ ] Mobile Device Management (MDM) console (BYOD enrollment, mobile DLP apps)
- [ ] Network DLP appliance (if separate from email/web DLP)
- [ ] Cloud application admin portals (M365, Google Workspace, Salesforce DLP settings)
- [ ] Database/application consoles (export restrictions, API rate limits)


**Policy Documentation:**

- [ ] Acceptable Use Policy (what channels users allowed to use)
- [ ] BYOD/Mobile Device Policy (MDM enrollment requirements, mobile app restrictions)
- [ ] Removable Media Policy (USB, external drives, CD/DVD burning)
- [ ] Cloud Application Policy (sanctioned vs. unsanctioned SaaS)
- [ ] Data Handling Procedures (how users supposed to transfer sensitive data)


**Testing Environment/Capability:**

- [ ] Test user accounts (to simulate data exfiltration attempts)
- [ ] Test data files (with DLP patterns, various file formats)
- [ ] Access to all channels for bypass testing (email, web, USB, mobile, etc.)


## Knowledge Required

**Essential Understanding:**

- Complete inventory of data egress channels in [Organization]
- DLP policy configurations per channel (what's blocked, what's monitored, what's allowed)
- Difference between monitor mode and blocking mode (monitoring = data still leaked, just logged)
- How users actually work (what channels they use daily for legitimate work)


**Technical Skills:**

- Ability to test DLP across multiple channels (send email, upload to web, copy to USB)
- Read DLP logs to verify detection/blocking
- Understand network protocols and traffic flows
- Basic scripting for API testing (if assessing application channel DLP)


**NOT Required:**

- DLP rule development (covered in A.8.12.2 Data Classification)
- Deep packet inspection expertise
- Advanced evasion technique knowledge (but helpful)


## Tools Needed

**Testing Tools:**

- **Test data files:** Files containing sensitive patterns (credit cards, SSNs, etc.)
- **USB drives:** For endpoint channel testing
- **Personal cloud accounts:** Dropbox, Google Drive personal (for web channel bypass testing)
- **Mobile device:** Personal phone (for mobile channel testing)
- **Email account:** Personal email (for email channel testing)


**Monitoring Tools:**

- **DLP console access:** To verify alerts generated during testing
- **SIEM access:** To verify DLP logs flowing correctly
- **Network packet capture:** Optional, for deep traffic analysis


**Documentation Tools:**

- **Screenshot capability:** To capture test results (DLP blocks, user notifications)
- **Screen recording:** For documenting bypass testing methodology


## Estimated Time Commitment

**Phase 1: Channel Inventory (1-2 hours)**

- List ALL data egress channels in organization
- For each channel: technology used, user population, data sensitivity
- Identify sanctioned vs. unsanctioned channels (shadow IT)
- Review firewall/proxy logs to discover unknown channels


**Phase 2: DLP Deployment Verification (2-3 hours)**

- For each channel: verify DLP deployed (Yes/No/Partial)
- Review DLP policy configuration (blocking vs. monitoring)
- Check coverage scope (all users or subset?)
- Verify integration with upstream security (firewall allows DLP traffic)


**Phase 3: Bypass Testing (1-2 hours)**

- **Email:** Send test email with sensitive data to personal email
- **Web:** Upload test file to personal Dropbox via web browser
- **Endpoint:** Copy test file to USB drive
- **Network:** FTP test file to external server
- **Cloud:** Export data from Salesforce to personal OneDrive
- **Mobile:** Transfer test file via mobile device (AirDrop, Bluetooth, mobile app)
- **Application:** Export data via application API or bulk download
- Document: Was DLP triggered? Was data blocked or just logged?


**Phase 4: Policy Effectiveness Review (1-2 hours)**

- For channels with DLP: test detection accuracy (false positives/negatives)
- Review DLP logs from last 30 days (alert volume, blocked vs. allowed)
- Interview users: Are DLP policies too restrictive (blocking legitimate work)?
- Check exception processes: How many exceptions granted? Are they justified?


**Phase 5: Assessment Completion (1 hour)**

- Complete all 7 channel sheets in workbook
- Document gaps (unprotected channels, monitor-only channels)
- Create remediation plans (priority: Critical gaps first)
- Collect evidence, populate Evidence Register


**Total:** 6-8 hours for comprehensive channel coverage assessment

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Open workbook: `ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx`
2. Review Instructions_Legend sheet
3. Complete Organization Metadata (yellow cells)

**STEP 2: Channel Inventory & Scoping (30-45 minutes)**
1. Navigate to Channel_Inventory sheet
2. List all data egress channels:

   - Email (internal, external, encrypted, unencrypted)
   - Web (proxy, direct internet, VPN, guest network)
   - Endpoint (USB, clipboard, print, screen capture, Bluetooth, WiFi Direct)
   - Network (FTP, SMB shares, NFS, rsync, database connections)
   - Cloud (M365, Google Workspace, Salesforce, Box, Dropbox, Slack, etc.)
   - Mobile (iOS, Android, BYOD, corporate-owned, MDM-managed, unmanaged)
   - Application (database exports, API, reporting tools, data warehouse queries)

3. For each channel: user population, data sensitivity, business criticality
4. Identify shadow IT channels (not officially sanctioned but used anyway)
5. Collect evidence: Network diagram, application inventory

**STEP 3: Email Channel Assessment (30-45 minutes)**
1. Navigate to Email_Channel sheet
2. Document email infrastructure:

   - Email system (Exchange, M365, Google Workspace, other)
   - DLP deployment (gateway, cloud service, both)
   - Coverage scope (all users or subset?)
   - Enforcement mode (blocking, monitoring, user prompt)

3. Test email DLP:

   - Send internal email with sensitive data → Should trigger alert
   - Send external email with sensitive data → Should block or encrypt
   - Send email via personal webmail (Gmail) → Should be blocked by web DLP

4. Review email DLP logs (last 30 days):

   - Alert volume, block rate, user exceptions

5. Status determination (see Section 4.2)
6. Collect evidence: Email DLP policy screenshot, test email block notification

**STEP 4: Web Channel Assessment (30-45 minutes)**
1. Navigate to Web_Channel sheet
2. Document web DLP architecture:

   - Web proxy/CASB (Zscaler, Netskope, Forcepoint Web Security, etc.)
   - SSL/TLS inspection status (required for encrypted uploads)
   - Cloud application control (blocked, allowed, monitored)
   - Personal cloud storage blocking (Dropbox, Google Drive, OneDrive personal)

3. Test web DLP:

   - Upload test file to personal Dropbox via browser → Should block
   - Upload to webmail (Gmail attachment) → Should block
   - Upload to file sharing site (WeTransfer, SendAnywhere) → Should block

4. Check bypass paths:

   - Direct internet access (bypassing proxy) → Should be prevented by firewall
   - VPN split tunneling → DLP should enforce on VPN traffic

5. Status determination (see Section 4.3)
6. Collect evidence: Web proxy logs showing blocks, CASB dashboard

**STEP 5: Endpoint Channel Assessment (45-60 minutes)**
1. Navigate to Endpoint_Channel sheet
2. For each endpoint sub-channel:

   - **USB/Removable Media:** DLP agent blocks USB? Read-only? Allowed but logged?
   - **Clipboard:** Copy/paste restrictions (between apps, to external apps)?
   - **Print:** Print management (watermarking, print logging, print blocking)?
   - **Screen Capture:** Screenshot blocking or watermarking?
   - **Bluetooth:** File transfer via Bluetooth allowed?
   - **WiFi Direct / AirDrop:** Peer-to-peer file transfer blocked?
   - **Local File Operations:** File rename/move/delete logged?

3. Test each sub-channel:

   - Plug in USB, try to copy sensitive file → Should block or encrypt
   - Copy sensitive text, try to paste into personal app → Should block
   - Print sensitive document → Should watermark or require justification
   - Screenshot sensitive data → Should block or watermark

4. Check endpoint agent deployment coverage (% of endpoints with DLP agent)
5. Status determination (see Section 4.4)
6. Collect evidence: Endpoint DLP policy, USB block screenshot

**STEP 6: Network Channel Assessment (30 minutes)**
1. Navigate to Network_Channel sheet
2. Document network protocols:

   - FTP/SFTP (blocked, allowed but monitored, open?)
   - SMB file shares (internal vs. external access control)
   - Database connections (direct DB access from endpoints blocked?)
   - Backup/sync tools (rsync, robocopy to external destinations)

3. Test network DLP:

   - FTP file to external server → Should block if DLP monitors FTP
   - Access external SMB share, copy sensitive file → Should block

4. Review network DLP logs (if network DLP appliance deployed)
5. Status determination (see Section 4.5)
6. Collect evidence: Firewall rules blocking outbound FTP, network DLP logs

**STEP 7: Cloud Channel Assessment (30-45 minutes)**
1. Navigate to Cloud_Channel sheet
2. For each cloud application:

   - **Sanctioned SaaS:** M365, Google Workspace, Salesforce, etc. - DLP deployed?
   - **Unsanctioned SaaS:** Personal cloud storage, file sharing - blocked?
   - **API access:** API rate limits, API key restrictions, OAuth app review

3. Test cloud DLP:

   - Upload file to M365 OneDrive → DLP should scan and block if sensitive
   - Share Salesforce report externally → DLP should block or require approval
   - Export data via API → Rate limits should prevent bulk export

4. Review CASB dashboard (if deployed):

   - Shadow IT discovery (what unsanctioned apps detected?)
   - DLP policy enforcement across SaaS apps

5. Status determination (see Section 4.6)
6. Collect evidence: CASB policy screenshot, M365 Purview DLP rules

**STEP 8: Mobile Channel Assessment (30-45 minutes)**
1. Navigate to Mobile_Channel sheet
2. Document mobile device landscape:

   - Corporate-owned devices: MDM enrollment rate, DLP app deployment
   - BYOD devices: MDM enrollment requirement, container/app wrapping
   - Unmanaged devices: Can access corporate data? (if yes, gap!)

3. Test mobile DLP:

   - Access corporate email on personal phone → Should require MDM enrollment or containerization
   - Try to forward corporate email from mobile → Should block
   - Try to save attachment to mobile device storage → Should block or encrypt
   - AirDrop/Bluetooth file transfer from corporate app → Should block

4. Check mobile application management (MAM):

   - Corporate apps: DLP policies enforced? (copy/paste restrictions, save-as blocking)

5. Status determination (see Section 4.7)
6. Collect evidence: MDM policy, mobile DLP app config

**STEP 9: Application Channel Assessment (30 minutes)**
1. Navigate to Application_Channel sheet
2. For each business application:

   - **Databases:** Export restrictions (no SELECT *, row limits, approval required?)
   - **APIs:** Rate limiting (prevent bulk data export via scripting)
   - **Reporting tools:** Output controls (email reports = DLP scanned, file exports = DLP scanned)
   - **Data warehouse / BI tools:** Query limits, export controls

3. Test application-level DLP:

   - Run database query returning sensitive data, try to export → Should limit rows or require approval
   - Call API repeatedly to export data → Should hit rate limit
   - Generate report with sensitive data, save to local file → Should trigger DLP scan

4. Status determination (see Section 4.8)
5. Collect evidence: Database export policy, API rate limit config

**STEP 10: Gap Analysis & Remediation Planning (30-45 minutes)**
1. Navigate to Gap_Analysis sheet
2. For each unprotected or partially protected channel:

   - Describe gap (e.g., "USB ports not blocked on 40% of endpoints")
   - Assess risk: Critical (Restricted data exfiltration path), High (Confidential data), Medium, Low
   - Define remediation (e.g., "Deploy endpoint DLP to all endpoints, enable USB blocking")
   - Assign owner (DLP admin + Endpoint team)
   - Set target date (Critical <30 days, High <90 days)

3. Prioritize:

   - **Critical:** Unprotected channels for Restricted data (e.g., no USB blocking but HR data on endpoints)
   - **High:** Monitor-only channels that should be blocking (e.g., email DLP in monitor mode for Confidential data)
   - **Medium:** Incomplete coverage (e.g., 80% of users protected, 20% gap)
   - **Low:** Documentation gaps, policy improvements


**STEP 11: Bypass Testing Summary (30 minutes)**
1. Navigate to Bypass_Testing sheet
2. Document all bypass tests performed:

   - Channel tested (Email, Web, USB, etc.)
   - Test methodology (what you did)
   - Expected result (DLP should block)
   - Actual result (did DLP block? Just log? Nothing?)
   - Bypass success/failure (bypass = data exfiltration succeeded)

3. For successful bypasses:

   - **Critical gap** - Escalate immediately to CISO
   - Create remediation plan
   - Retest after remediation


**STEP 12: Evidence Register & Final Review (15 minutes)**
1. Navigate to Evidence_Register sheet
2. Document all evidence collected (minimum 2 per channel = 14 items)
3. Review Summary_Dashboard:

   - Overall channel coverage percentage
   - Critical gaps highlighted
   - Channel coverage heatmap

4. Quality check (Section 7)

**STEP 13: Approval & Sign-Off (15 minutes)**
1. Complete Approval_Sign-Off sheet
2. Save with completion date in filename

---

# Sheet-by-Sheet Guidance

## Sheet: Channel_Inventory

**Assessment Question:** *"What are all the data egress channels in your organization?"*

**How to Answer:**

- **Comprehensive inventory:** List EVERY way data can leave organization (email, web, USB, print, mobile, cloud, etc.)
- **Include shadow IT:** Unsanctioned channels users actually use (personal Dropbox, WhatsApp, Telegram)
- **Don't assume:** Just because something is blocked by policy doesn't mean users aren't using it (verify with logs)


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Channel ID** | Unique identifier | "CH-001", "CH-EMAIL-01" | Create systematically |
| **Channel Category** | Primary category | Email/Web/Endpoint/Network/Cloud/Mobile/Application | Predefined list |
| **Channel Sub-Type** | Specific channel | "SMTP", "USB", "Dropbox", "iOS AirDrop" | Technical specification |
| **Technology/Service** | What implements it | "Microsoft Exchange", "Zscaler", "Intune MDM" | IT documentation |
| **User Population** | Who uses this | "All employees", "Finance only", "Executives" | User access logs |
| **Business Criticality** | How essential | Critical/High/Medium/Low | Business impact if blocked |
| **Data Sensitivity** | What data flows | Restricted/Confidential/Internal/Public | Data flow analysis |
| **Sanctioned Status** | Officially approved? | Sanctioned/Unsanctioned/Shadow IT | Policy documentation |
| **DLP Coverage** | Is DLP protecting? | Yes/No/Partial/Planned | DLP deployment matrix |
| **Evidence ID** | Reference | A812-3-INV-001 | Link to Evidence Register |

**Status Determination:**

**✅ Compliant:**

- All data egress channels inventoried and documented
- DLP coverage for all channels with Restricted/Confidential data
- Shadow IT channels identified and either blocked or brought under management


**⚠️ Partial:**

- Channel inventory incomplete (some channels missing)
- Shadow IT channels known but not yet remediated
- DLP coverage gaps documented with remediation plans


**❌ Non-Compliant:**

- No systematic channel inventory
- Unknown shadow IT channels (discovered during assessment)
- Multiple channels with Restricted data completely unprotected


**Compliance Checklist:**

- [ ] **All 7 channel categories represented** (Email, Web, Endpoint, Network, Cloud, Mobile, Application)
- [ ] **Shadow IT channels identified** (review proxy logs, CASB discovery, user surveys)
- [ ] **User population documented** (who uses each channel, how many users)
- [ ] **Data sensitivity verified** (what classification levels flow through each channel)
- [ ] **Business criticality assessed** (impact if channel blocked for DLP compliance)


**Evidence Examples:**

- Network topology diagram: `EV-1-Inventory-20260121-Network-Topology.pdf`
- Application inventory: `EV-1-Inventory-20260121-Application-Portfolio.xlsx`
- Shadow IT discovery report (from CASB): `EV-1-Inventory-20260121-Shadow-IT-CASB-Discovery.pdf`


---

## Sheet: Email_Channel

**Assessment Question:** *"Is email DLP deployed to prevent sensitive data leakage via email?"*

**Understanding the Requirement:**

Email is historically the #1 data leakage channel, but coverage alone is insufficient - must verify enforcement mode and effectiveness.

**Policy (ISMS-POL-A.8.12 Section 2.2):**

- Email DLP required for all outbound email (internal and external)
- Restricted data: Blocking mode (prevent send)
- Confidential data: Blocking or encryption required
- Internal data: Monitoring acceptable


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Email System** | Platform | "Microsoft Exchange", "Google Workspace" | IT documentation |
| **DLP Deployment** | Where DLP deployed | Gateway/Cloud Service/Both | Email architecture diagram |
| **Coverage Scope** | Who protected | "All users", "95% (5% VIPs exempt)" | DLP policy config |
| **Enforcement Mode** | Action taken | Block/Encrypt/User Prompt/Monitor Only | DLP rule settings |
| **Attachment Scanning** | Files scanned | Yes/No/Partial (file size limits) | DLP capabilities |
| **Encrypted Email** | S/MIME, PGP handled | Scanned Before Encryption/Not Scanned | Technical capability |
| **External Domains** | External send allowed | Blocked/Allowed w/DLP/Allowed w/o DLP | Policy rules |
| **Webmail Blocking** | Gmail, Yahoo blocked | Yes/No/Partial | Web proxy rules |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on testing |
| **Evidence ID** | Reference | A812-3-EML-001 | Evidence register |

**Status Determination:**

**✅ Compliant:**

- Email DLP deployed on all outbound email (internal + external)
- Blocking mode for Restricted/Confidential data
- Attachment scanning enabled (all file types)
- Encrypted email scanned before encryption
- Coverage: 100% of users
- Bypass paths closed (webmail blocked by web DLP)
- Testing confirms: Sensitive data send blocked, user notified, alert generated


**⚠️ Partial:**

- Email DLP deployed but monitor-only (data still sent, just logged)
- Coverage gaps (some users exempt, some email paths not scanned)
- Encrypted email not scanned (blind spot)
- Webmail not blocked (bypass via Gmail)
- Attachment size limits (large files bypass DLP)


**❌ Non-Compliant:**

- No email DLP deployed
- Email DLP deployed but disabled or ineffective
- Testing shows: Sensitive data sent successfully with no alert


**Compliance Checklist:**

- [ ] **DLP deployed on ALL outbound email paths** (Exchange, M365, Gmail if used)
- [ ] **Blocking mode enabled for Restricted/Confidential data** (not just monitoring)
- [ ] **Attachment scanning covers all file types** (not just .doc/.pdf, include .zip/.rar/.7z)
- [ ] **Encrypted email scanned BEFORE encryption** (S/MIME, PGP integration)
- [ ] **100% user coverage** (no VIP exemptions without risk acceptance)
- [ ] **Webmail blocked** (personal Gmail, Yahoo, Outlook.com via web browser)
- [ ] **Testing passed:** Send test email with fake SSN → Blocked, user notified, alert logged


**Common Pitfalls:**

**Pitfall 1:** "Email DLP deployed but set to monitor-only"
**Problem:** Data still leaks, DLP just logs it (compliance theater)
**Solution:** Change to blocking mode for Restricted/Confidential; monitor-only only acceptable for Internal classification

**Pitfall 2:** "Large attachments bypass DLP (>50MB size limit)"
**Problem:** Attacker splits data into multiple emails or compresses heavily
**Solution:** Remove size limits or set to maximum (500MB+); monitor compression ratios

**Evidence Examples:**

- Email DLP policy screenshot: `EV-2-Email-20260121-DLP-Policy-Config.png`
- Test email block notification: `EV-2-Email-20260121-Test-SSN-Block-UserNotification.png`
- Email DLP logs (last 30 days): `EV-2-Email-20260121-DLP-Logs-Summary.xlsx`


---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Domain]-[Channel]-[Date]-[Description].[ext]
```

**Domain Codes:**

- 1 = Channel Inventory
- 2 = Email Channel
- 3 = Web Channel
- 4 = Endpoint Channel
- 5 = Network Channel
- 6 = Cloud Channel
- 7 = Mobile Channel
- 8 = Application Channel
- 9 = Bypass Testing


**Examples:**

- `EV-1-Inventory-20260121-Network-Topology.pdf`
- `EV-2-Email-20260121-DLP-Block-Screenshot.png`
- `EV-3-Web-20260121-CASB-Dashboard.png`
- `EV-4-Endpoint-20260121-USB-Block-Test.png`
- `EV-9-Bypass-20260121-Email-to-USB-Test-Results.xlsx`


**Storage:** `ISMS/Controls/A.8.12_DLP/Assessments/Channel_Coverage/Evidence/`  
**Retention:** 2-3 years  
**Sensitivity:** Internal (may contain infrastructure details)

## Evidence Types by Channel

**1. Channel Inventory:**

- Network topology diagram (data egress points)
- Application inventory (all systems processing sensitive data)
- Shadow IT discovery report (CASB or proxy log analysis)


**2. Email Channel:**

- Email DLP policy configuration screenshot
- Test email block notification (user-facing message)
- Email DLP logs (last 30 days summary)
- Encrypted email handling documentation


**3. Web Channel:**

- Web proxy/CASB dashboard screenshot
- SSL inspection configuration
- Personal cloud storage blocking rules
- Test web upload block screenshot


**4. Endpoint Channel:**

- Endpoint DLP policy export (USB, clipboard, print rules)
- USB block test screenshot
- Clipboard restriction test
- Print management configuration
- Endpoint agent deployment coverage report


**5. Network Channel:**

- Firewall rules (FTP, SMB outbound blocking)
- Network DLP logs (if network DLP deployed)
- Database direct access blocking evidence


**6. Cloud Channel:**

- CASB policy configuration
- M365/Google Workspace DLP rules
- OAuth application review process
- API rate limit configuration


**7. Mobile Channel:**

- MDM policy documentation
- Mobile DLP app configuration
- BYOD enrollment rate report
- Mobile app management (MAM) policies


**8. Application Channel:**

- Database export restriction configuration
- API rate limit settings
- Reporting tool output control documentation


**9. Bypass Testing:**

- Bypass test results spreadsheet (all channels tested)
- Screenshots of successful/failed bypasses
- DLP alert logs from testing
- Retest results after remediation


**Minimum Evidence:** 2 items per channel × 7 channels + inventory = **15 items minimum**

---

# Common Pitfalls and How to Avoid Them

## "We protect email and web, so we're covered"

**Problem:** Attackers/insiders simply use alternative channels (USB, mobile, cloud apps)

**Reality Check:**

- Email + Web = ~60% of data egress channels
- Unprotected: USB (15%), Mobile (10%), Cloud apps (10%), Print (5%)
- Result: 40% of data leakage paths completely open


**Solution:**
1. Complete channel inventory (all 7 categories)
2. Deploy DLP across ALL high-risk channels
3. Prioritize by data sensitivity × channel usage
4. Accept residual risk for low-usage channels (with CISO approval)

## "DLP is deployed but set to monitor-only everywhere"

**Problem:** Monitor-only = data leakage still happens, just logged

**When Monitor-Only Acceptable:**

- Initial tuning period (2-4 weeks) to reduce false positives
- Internal data classification (low sensitivity)
- Channels with very high false positive rate (requires more tuning)


**When Blocking Required:**

- Restricted data on any channel
- Confidential data on high-risk channels (email external, web upload, USB)


**Solution:**

- Review enforcement mode per channel
- Change Restricted/Confidential to blocking
- Keep Internal as monitoring (acceptable)
- Document risk acceptance if monitor-only for business reasons


## "USB is blocked, but users can still use Bluetooth/AirDrop"

**Problem:** Partial endpoint channel coverage creates bypass

**Common Endpoint Gaps:**

- USB blocked → Bluetooth file transfer allowed
- Clipboard blocked → Screen capture allowed (user takes photo of screen)
- Print blocked → Mobile camera allowed (photo of screen)
- File save blocked → Drag-and-drop to external app allowed


**Solution:**

- Comprehensive endpoint DLP covering all sub-channels:
  - USB, Bluetooth, WiFi Direct, AirDrop
  - Clipboard, screen capture, print, file operations
- Regularly test endpoint DLP (users are creative at finding bypasses)


## "We have CASB, so cloud is covered"

**Problem:** CASB covers sanctioned apps, but unsanctioned apps still accessible

**CASB Limitations:**

- Only monitors apps you configure (if you don't know about app, CASB doesn't monitor)
- API-based CASB: Only works for apps with API (custom apps, legacy SaaS not covered)
- Proxy-based CASB: Can be bypassed with VPN, mobile apps, split tunneling


**Solution:**

- CASB + Web DLP (proxy) = comprehensive coverage
- Block unsanctioned cloud storage (Dropbox personal, Box personal, WeTransfer)
- OAuth application review (block risky third-party apps)
- Regular shadow IT discovery (CASB or proxy log analysis)


## "Mobile devices are MDM-managed, so we're safe"

**Problem:** MDM enrollment ≠ DLP enforcement

**MDM vs. MAM vs. DLP:**

- **MDM:** Device management (inventory, remote wipe, policy push)
- **MAM:** Application management (app distribution, app config, app wrapping)
- **DLP:** Data loss prevention (copy/paste block, save-as block, sharing restrictions)


**Common Mobile Gaps:**

- MDM enrolled but no DLP policies enabled
- Corporate apps containerized but copy/paste between container and device allowed
- BYOD enrollment optional (unmanaged devices can access corporate email)


**Solution:**

- MDM + MAM + DLP policies (all three required)
- Enforce BYOD enrollment (unmanaged devices blocked from corporate resources)
- Test mobile DLP (try to forward email, save attachment, copy/paste from corporate app)


## "Application-level DLP is too complex, we skip it"

**Problem:** Database exports, API bulk downloads completely unprotected

**Impact:**

- Insider exports entire customer database via SQL query or API script
- DLP deployed on all perimeter channels (email, web, USB) but missed application layer
- Result: Largest data breach vectors unprotected


**Solution (Practical Approach):**

- **Phase 1:** Database query limits (no SELECT * on tables >10K rows without approval)
- **Phase 2:** API rate limiting (prevent bulk export via scripting)
- **Phase 3:** Application-level logging (log all exports, integrate with SIEM)
- **Phase 4:** Application DLP (scan database exports, API responses for sensitive data)


Start with Phase 1-2 (easy), add Phase 3-4 (complex) over time

---

# Quality Checklist (Self-Review Before Submission)

**Completeness:**

- [ ] All 7 channel categories assessed (Email, Web, Endpoint, Network, Cloud, Mobile, Application)
- [ ] Channel inventory complete (no missing egress paths)
- [ ] Shadow IT channels identified and documented
- [ ] Bypass testing performed on each channel
- [ ] Gap Analysis completed for all ❌ and ⚠️ items
- [ ] Remediation plans created (gap description, risk, action, owner, target date)
- [ ] Summary Dashboard calculated (overall coverage %, critical gaps)


**Accuracy:**

- [ ] DLP deployment status verified through testing (not assumptions)
- [ ] Enforcement mode confirmed (blocking vs. monitoring)
- [ ] Coverage scope verified (% of users, devices, applications)
- [ ] Bypass tests documented with actual results (success/failure)
- [ ] False positive/negative rates measured (if data available)


**Evidence Quality:**

- [ ] Minimum 2 evidence items per channel (14+ total)
- [ ] Bypass test results documented (screenshots, logs)
- [ ] DLP policy configurations exported
- [ ] Test methodology documented (reproducible)
- [ ] Evidence naming convention followed


**Policy Alignment:**

- [ ] Assessment covers all channels from ISMS-POL-A.8.12 Section 2.2
- [ ] Enforcement modes verified against policy requirements (Restricted = block)
- [ ] Coverage gaps mapped to risk levels (Restricted data gap = Critical)


**Testing Verification:**

- [ ] Bypass testing performed on each channel (not just theoretical)
- [ ] DLP alerts verified in logs (testing actually triggered DLP)
- [ ] User notifications verified (users know why action blocked)
- [ ] Successful bypasses escalated to CISO


**Final Checks:**

- [ ] Filename includes date: `ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx`
- [ ] All formulas calculate correctly
- [ ] Conditional formatting working
- [ ] Sheet protection enabled


---

# Review & Approval Process

## Assessment Metadata

**Assessment Period:** _______  
**Assessment Date:** _______  
**Assessment Type:**

- [ ] Initial Assessment
- [ ] Quarterly Review
- [ ] Post-Incident (data breach)
- [ ] Post-Deployment (new DLP channel)


## Completed By

**Name:** _______________________  
**Role:** _______________________ (DLP Administrator, Security Engineer)  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Declaration:**
I confirm:

- All channels inventoried through network analysis and user interviews
- Bypass testing performed on each channel
- Evidence authentic and reproducible
- Critical gaps escalated to CISO immediately


## Reviewed By (Security Team Lead)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Outcome:**

- [ ] Approved
- [ ] Approved with corrections: _______
- [ ] Requires revision: _______


## Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Decision:**

- [ ] Approved - Channel coverage adequate
- [ ] Approved with conditions - Remediate gaps by: _______
- [ ] Rejected - Critical gaps require immediate action


**Risk Acceptance:**
For documented gaps/exceptions:

- [ ] Residual risk accepted
- [ ] Remediation required
- [ ] Escalate to Executive Management


**Budget Approval (if needed):**
Cost: _______

- [ ] Approved
- [ ] Requires business case
- [ ] Deferred


## Next Review Date

**Next Assessment:** _______________________

**Review Cycle:** Quarterly or upon:

- Network changes (new VPN, cloud connection, internet egress)
- Application deployments (new SaaS, new database, new API)
- DLP deployment changes (new channel coverage, policy updates)
- Security incidents (data breach, bypass discovery)
- User complaints (DLP blocking legitimate work - requires tuning)


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 12

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 50 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | Channel_Overview | 30 | Complete channel catalog overview | Yes (all egress channels) |
| 3 | Email_Channel | 20 | Email DLP assessment | Yes (email DLP config) |
| 4 | Web_Cloud_Channel | 30 | Web/proxy/cloud/CASB DLP assessment | Yes (web/cloud DLP config) |
| 5 | Endpoint_Channel | 30 | Endpoint DLP (USB, clipboard, print) | Yes (endpoint controls) |
| 6 | Network_Channel | 20 | Network protocols (FTP, SMB, etc.) | Yes (network DLP) |
| 7 | Application_Channel | 20 | Database, API, app-level controls | Yes (app controls) |
| 8 | Mobile_Channel | 25 | Mobile devices, MDM, MAM | Yes (mobile DLP) |
| 9 | Coverage_Metrics | 35 | Coverage metrics and testing results | Yes (test outcomes) |
| 10 | Gap_Analysis | 45 | Gaps and remediation | Yes (gap details) |
| 11 | Evidence_Register | 110 | Evidence tracking | Yes (evidence entries) |
| 12 | Summary_Dashboard | 40 | KPIs, coverage heatmap | No (formulas) |

**Total Assessment Items:** ~70 channel coverage checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance, assessment metadata, response value legend

**Layout:**

- Rows 1-5: Document header
- Rows 7-12: Organization metadata (yellow cells)
- Rows 14-30: Instructions
- Rows 32-40: Response value legend
- Rows 42-50: Coverage status color coding


**Organization Metadata:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Assessment Date | Date | 21.01.2026 |
| 8 | Completed By | Text | Jane Doe |
| 9 | Role | Text | DLP Administrator |
| 10 | Organization | Text | [Organization] |
| 11 | Review Cycle | Text | Quarterly |
| 12 | Next Review | Date | 21.04.2026 |

---

## Sheet: Channel_Inventory

**Purpose:** Comprehensive inventory of all data egress channels

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Channel ID | Text | 15 | None | Unique ID (CH-001) |
| B | Channel Category | Dropdown | 20 | 7 categories | Email/Web/Endpoint/etc. |
| C | Channel Sub-Type | Text | 25 | None | SMTP, USB, Dropbox, etc. |
| D | Technology/Service | Text | 30 | None | Exchange, Zscaler, etc. |
| E | User Population | Text | 20 | None | "All users", "Finance" |
| F | Business Criticality | Dropdown | 18 | Critical/High/Medium/Low | Impact if blocked |
| G | Data Sensitivity | Dropdown | 18 | Classification levels | Restricted/Confidential/etc. |
| H | Sanctioned Status | Dropdown | 18 | Pre-defined list | Sanctioned/Unsanctioned |
| I | DLP Coverage | Dropdown | 15 | Yes/No/Partial/Planned | Is DLP deployed? |
| J | Coverage Notes | Text (wrap) | 35 | None | Details, exceptions |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance status |
| L | Evidence ID | Text | 15 | None | A812-3-INV-001 |

**Pre-Populated Examples (Gray rows 6-12):**

| Channel ID | Category | Sub-Type | Technology |
|------------|----------|----------|------------|
| CH-001 | Email | SMTP Outbound | Microsoft Exchange |
| CH-002 | Web | HTTPS Upload | Zscaler Web Proxy |
| CH-003 | Endpoint | USB Storage | Endpoint DLP Agent |
| CH-004 | Cloud | Cloud Storage | Microsoft Purview |
| CH-005 | Mobile | iOS Devices | Intune MDM |
| CH-006 | Network | FTP Outbound | Network Firewall |
| CH-007 | Application | Database Export | Database ACLs |

**Data Rows:** 30 total (7 examples + 23 blank)

**Data Validation:**

```python
# Column B: Channel Category
validation_category = {
    'type': 'list',
    'formula1': '"Email,Web,Endpoint,Network,Cloud,Mobile,Application"',
    'allow_blank': False
}

# Column F: Business Criticality
validation_criticality = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False
}

# Column G: Data Sensitivity
validation_sensitivity = {
    'type': 'list',
    'formula1': '=Classification_Levels!$A$2:$A$10',  # Dynamic reference
    'allow_blank': False
}

# Column H: Sanctioned Status
validation_sanctioned = {
    'type': 'list',
    'formula1': '"Sanctioned,Unsanctioned,Shadow IT,Under Review"',
    'allow_blank': False
}

# Column I: DLP Coverage
validation_coverage = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column K: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column I (DLP Coverage):
  - "Yes" = Green fill
  - "Partial" = Yellow fill
  - "No" = Red fill
  - "Planned" = Light blue fill
- Column K (Status): Standard status colors


---

## Sheet: Email_Channel

**Purpose:** Detailed email DLP assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Email System | Text | 25 | None | Exchange, M365, Gmail |
| B | DLP Deployment | Dropdown | 22 | Gateway/Cloud/Both | Where DLP is |
| C | Coverage Scope | Text | 20 | None | "All users" or % |
| D | Enforcement Mode | Dropdown | 20 | Block/Encrypt/Prompt/Monitor | Action taken |
| E | Attachment Scanning | Dropdown | 20 | Yes/No/Partial | Files scanned |
| F | Encrypted Email Handling | Dropdown | 25 | Before/After/Not Scanned | S/MIME, PGP |
| G | External Domain Policy | Dropdown | 22 | Block/Allow+DLP/Allow | External send |
| H | Webmail Blocking | Dropdown | 18 | Yes/No/Partial | Gmail, Yahoo blocked |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert Only | Test outcome |
| K | False Positive Rate (%) | Number | 18 | 0-100 | If measured |
| L | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| M | Evidence ID | Text | 15 | None | A812-3-EML-001 |

**Pre-Populated Examples (Gray rows 6-8):**

| System | DLP Deployment | Scope | Enforcement | Attachment Scanning |
|--------|----------------|-------|-------------|---------------------|
| Microsoft Exchange | Gateway + Cloud (Purview) | All users (100%) | Block | Yes |
| Google Workspace | Cloud Service (native DLP) | All users (100%) | User Prompt | Yes |

**Data Rows:** 20 total (2 examples + 18 blank for different email flows/systems)

**Data Validation:**

```python
# Column B: DLP Deployment
validation_deployment = {
    'type': 'list',
    'formula1': '"Gateway,Cloud Service,Both,None"',
    'allow_blank': False
}

# Column D: Enforcement Mode
validation_enforcement = {
    'type': 'list',
    'formula1': '"Block,Encrypt,User Prompt,Monitor Only,None"',
    'allow_blank': False
}

# Column E, H, I: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,N/A"',
    'allow_blank': False
}

# Column F: Encrypted Email
validation_encrypted = {
    'type': 'list',
    'formula1': '"Scanned Before Encryption,Scanned After Decryption,Not Scanned,N/A"',
    'allow_blank': False
}

# Column G: External Domain
validation_external = {
    'type': 'list',
    'formula1': '"Blocked,Allowed with DLP,Allowed without DLP,Requires Approval"',
    'allow_blank': False
}

# Column J: Test Result
validation_testresult = {
    'type': 'list',
    'formula1': '"Blocked (Pass),Allowed (Fail),Alert Only (Partial),Not Tested"',
    'allow_blank': False
}

# Column K: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}
```

**Conditional Formatting:**

- Column D (Enforcement Mode):
  - "Block" or "Encrypt" = Green (compliant for Restricted data)
  - "User Prompt" = Yellow (acceptable for Confidential)
  - "Monitor Only" or "None" = Red (non-compliant for sensitive data)
- Column J (Test Result):
  - "Blocked (Pass)" = Green
  - "Alert Only (Partial)" = Yellow
  - "Allowed (Fail)" = Red


---

## Sheet: Web_Channel

**Purpose:** Web proxy, CASB, and cloud storage DLP assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Web Technology | Text | 25 | None | Zscaler, Netskope, Forcepoint |
| B | Deployment Type | Dropdown | 20 | Proxy/CASB/Cloud Gateway | Architecture |
| C | SSL/TLS Inspection | Dropdown | 20 | Enabled/Partial/Disabled | HTTPS decrypt |
| D | Cloud Storage Blocking | Text (wrap) | 30 | None | Which services blocked |
| E | Webmail Blocking | Dropdown | 20 | Blocked/Allowed/Partial | Gmail, Yahoo, etc. |
| F | File Upload DLP | Dropdown | 20 | Block/Monitor/None | Upload scanning |
| G | Coverage Scope | Text | 20 | None | "All users" or % |
| H | Bypass Paths | Text (wrap) | 30 | None | VPN, direct, mobile |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-WEB-001 |

**Pre-Populated Examples (Gray rows 6-8):**

| Technology | Type | SSL Inspection | Cloud Blocking | Webmail Blocking |
|------------|------|----------------|----------------|------------------|
| Zscaler Internet Access | Cloud Proxy | Enabled | Dropbox, Box personal, WeTransfer | Blocked |
| Netskope CASB | CASB | Enabled | OneDrive personal, Google Drive personal | Allowed with DLP |

**Data Rows:** 25 total (2 examples + 23 blank)

**Data Validation:**

```python
# Column B: Deployment Type
validation_deployment = {
    'type': 'list',
    'formula1': '"On-Premise Proxy,Cloud Proxy,CASB,Cloud Gateway,None"',
    'allow_blank': False
}

# Column C: SSL/TLS Inspection
validation_ssl = {
    'type': 'list',
    'formula1': '"Enabled (All Traffic),Enabled (Selective),Disabled,N/A"',
    'allow_blank': False
}

# Column E: Webmail Blocking
validation_webmail = {
    'type': 'list',
    'formula1': '"Blocked,Allowed with DLP,Allowed without DLP,Partial"',
    'allow_blank': False
}

# Column F: File Upload DLP
validation_upload = {
    'type': 'list',
    'formula1': '"Block,Monitor Only,User Prompt,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (SSL Inspection):
  - "Enabled (All Traffic)" = Green (required for HTTPS DLP)
  - "Enabled (Selective)" = Yellow (gaps exist)
  - "Disabled" = Red (blind to encrypted uploads)
- Column F (File Upload DLP):
  - "Block" = Green
  - "Monitor Only" or "User Prompt" = Yellow
  - "None" = Red


---

## Sheet: Endpoint_Channel

**Purpose:** Endpoint DLP covering USB, clipboard, print, screen capture

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Endpoint Control | Text | 25 | None | USB, Clipboard, Print, etc. |
| B | DLP Agent Deployed | Dropdown | 18 | Yes/No/Partial | Agent coverage |
| C | Agent Coverage (%) | Number | 18 | 0-100 | % of endpoints |
| D | Control Type | Dropdown | 20 | Block/Encrypt/Log Only/None | Action |
| E | OS Coverage | Text | 25 | None | Windows, macOS, Linux |
| F | Offline Protection | Dropdown | 18 | Yes/No/Partial | Works when offline? |
| G | User Override Allowed | Dropdown | 18 | Yes/No/With Justification | Can users bypass? |
| H | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test done? |
| I | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| J | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| K | Evidence ID | Text | 15 | None | A812-3-EPT-001 |

**Pre-Populated Endpoint Controls (Gray rows 6-13):**

| Control | Description | Typical Policy |
|---------|-------------|----------------|
| USB Storage | USB drives, external HDDs | Block or Encrypt-Only |
| Clipboard | Copy/paste between apps | Block external paste |
| Print | Printing documents | Watermark or Require Justification |
| Screen Capture | Screenshots, screen recording | Block or Watermark |
| Bluetooth | File transfer via Bluetooth | Block |
| WiFi Direct / AirDrop | Peer-to-peer file transfer | Block |
| Local File Operations | File rename, move, delete | Log Only |
| CD/DVD Burning | Optical media writes | Block |

**Data Rows:** 30 total (8 pre-populated controls + 22 blank for custom controls)

**Data Validation:**

```python
# Column B: DLP Agent Deployed
validation_agent = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned"',
    'allow_blank': False
}

# Column C: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Control Type
validation_control = {
    'type': 'list',
    'formula1': '"Block,Encrypt Only,Read-Only,Log Only,User Prompt,None"',
    'allow_blank': False
}

# Column F, G, H: Yes/No variations
validation_yesno = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,With Justification,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Agent Coverage):
  - ≥95% = Green
  - 80-94% = Yellow
  - <80% = Red
- Column D (Control Type):
  - "Block" or "Encrypt Only" = Green
  - "Read-Only" or "Log Only" = Yellow
  - "User Prompt" or "None" = Red (for Restricted data channels)


---

## Sheet: Network_Channel

**Purpose:** Network protocol DLP (FTP, SMB, database connections)

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Protocol/Service | Text | 25 | None | FTP, SFTP, SMB, RDP |
| B | Network DLP Deployed | Dropdown | 20 | Yes/No/Partial | Is DLP monitoring? |
| C | Firewall Policy | Dropdown | 20 | Blocked/Allowed/Conditional | Outbound rule |
| D | DLP Action | Dropdown | 18 | Block/Monitor/None | If DLP deployed |
| E | Coverage Scope | Text | 20 | None | Which networks/sites |
| F | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| G | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| H | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| I | Evidence ID | Text | 15 | None | A812-3-NET-001 |

**Pre-Populated Network Protocols (Gray rows 6-11):**

| Protocol | Typical Use | Common Policy |
|----------|-------------|---------------|
| FTP/FTPS (Port 21/990) | File transfer | Blocked outbound |
| SFTP (Port 22) | Secure file transfer | Allowed to known servers only |
| SMB/CIFS (Port 445) | File sharing | Blocked outbound (internal only) |
| RDP (Port 3389) | Remote desktop | Blocked outbound (VPN only) |
| Database Protocols (1433, 3306, 5432) | Direct DB access | Blocked from endpoints |
| rsync (Port 873) | File synchronization | Blocked outbound |

**Data Rows:** 20 total (6 pre-populated + 14 blank)

**Data Validation:**

```python
# Column B: Network DLP
validation_dlp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column C: Firewall Policy
validation_firewall = {
    'type': 'list',
    'formula1': '"Blocked,Allowed (All),Allowed (Specific Destinations),Conditional,None"',
    'allow_blank': False
}

# Column D: DLP Action
validation_action = {
    'type': 'list',
    'formula1': '"Block,Monitor Only,Alert Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Firewall Policy):
  - "Blocked" = Green (preferred for FTP, SMB outbound)
  - "Allowed (Specific Destinations)" = Yellow (acceptable with DLP)
  - "Allowed (All)" = Red (uncontrolled egress)


---

## Sheet: Cloud_Channel

**Purpose:** SaaS applications, cloud storage, API-based DLP

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Cloud Application | Text | 30 | None | M365, Salesforce, etc. |
| B | Application Type | Dropdown | 20 | SaaS/IaaS/PaaS | Service model |
| C | CASB Coverage | Dropdown | 18 | Yes/No/Partial | CASB monitoring |
| D | Native DLP Enabled | Dropdown | 20 | Yes/No/Partial | App's built-in DLP |
| E | DLP Policy Type | Dropdown | 25 | API-based/Proxy-based/Both | How DLP works |
| F | Data Classification Integration | Dropdown | 25 | Yes/No/Partial | Reads doc labels |
| G | Sharing Controls | Dropdown | 20 | Enforced/Advisory/None | External sharing |
| H | OAuth App Review | Dropdown | 20 | Enabled/Disabled | Third-party apps |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-CLD-001 |

**Pre-Populated Cloud Apps (Gray rows 6-10):**

| Application | Type | Native DLP | Typical Policy |
|-------------|------|------------|----------------|
| Microsoft 365 | SaaS | Yes (Purview) | Classification-based DLP |
| Google Workspace | SaaS | Yes (native DLP) | Context-aware policies |
| Salesforce | SaaS | Yes (Shield) | Sharing controls |
| Box | SaaS | Yes (Shield) | Classification-based |
| AWS S3 (if used) | IaaS | No (via CASB) | CASB monitoring |

**Data Rows:** 25 total (5 examples + 20 blank)

**Data Validation:**

```python
# Column B: Application Type
validation_apptype = {
    'type': 'list',
    'formula1': '"SaaS,IaaS,PaaS,Hybrid,Other"',
    'allow_blank': False
}

# Column C, D, F, H, I: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column E: DLP Policy Type
validation_policytype = {
    'type': 'list',
    'formula1': '"API-based,Proxy-based,Inline,Hybrid,None"',
    'allow_blank': False
}

# Column G: Sharing Controls
validation_sharing = {
    'type': 'list',
    'formula1': '"Enforced (Block),Enforced (Approval),Advisory Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column D (Native DLP):
  - "Yes" = Green (preferred)
  - "Partial" = Yellow (some features enabled)
  - "No" = Red (requires CASB)
- Column G (Sharing Controls):
  - "Enforced (Block)" = Green
  - "Enforced (Approval)" = Yellow
  - "Advisory Only" or "None" = Red


---

## Sheet: Mobile_Channel

**Purpose:** Mobile device DLP, MDM/MAM, BYOD assessment

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Device Type | Dropdown | 20 | iOS/Android/Other | Platform |
| B | Ownership Model | Dropdown | 20 | Corporate/BYOD/Mixed | Who owns device |
| C | MDM Enrollment | Dropdown | 20 | Mandatory/Optional/None | Enrollment policy |
| D | Enrollment Rate (%) | Number | 18 | 0-100 | % of devices enrolled |
| E | MAM/DLP App Deployed | Dropdown | 20 | Yes/No/Partial | DLP app coverage |
| F | Containerization | Dropdown | 20 | Yes/No/Partial | Corporate data isolated |
| G | Copy/Paste Restrictions | Dropdown | 22 | Enforced/Advisory/None | Between apps |
| H | Save-As Blocking | Dropdown | 18 | Yes/No/Partial | Save to device storage |
| I | Sharing Controls | Dropdown | 20 | Enforced/Advisory/None | AirDrop, Bluetooth |
| J | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| K | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| L | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| M | Evidence ID | Text | 15 | None | A812-3-MOB-001 |

**Pre-Populated Device Types (Gray rows 6-9):**

| Device Type | Ownership | MDM Mandatory | Typical DLP Controls |
|-------------|-----------|---------------|----------------------|
| iOS (iPhone/iPad) | Corporate-Owned | Yes | Full MDM + MAM + DLP app |
| iOS (iPhone/iPad) | BYOD | Yes | MAM + DLP app (container) |
| Android (Corporate) | Corporate-Owned | Yes | Full MDM + MAM + DLP app |
| Android (BYOD) | BYOD | Optional | MAM only (if enrolled) |

**Data Rows:** 25 total (4 examples + 21 blank)

**Data Validation:**

```python
# Column A: Device Type
validation_device = {
    'type': 'list',
    'formula1': '"iOS,Android,Windows Mobile,Other"',
    'allow_blank': False
}

# Column B: Ownership
validation_ownership = {
    'type': 'list',
    'formula1': '"Corporate-Owned,BYOD,Mixed"',
    'allow_blank': False
}

# Column C: MDM Enrollment
validation_mdm = {
    'type': 'list',
    'formula1': '"Mandatory (Blocked if Unenrolled),Mandatory (Advisory),Optional,None"',
    'allow_blank': False
}

# Column D: Percentage
validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column E, F, H: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,Planned,N/A"',
    'allow_blank': False
}

# Column G, I: Enforcement levels
validation_enforcement = {
    'type': 'list',
    'formula1': '"Enforced,Advisory Only,None"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column D (Enrollment Rate):
  - 100% = Green
  - 90-99% = Yellow
  - <90% = Red (gap in mobile coverage)
- Column G, I (Restrictions):
  - "Enforced" = Green
  - "Advisory Only" = Yellow
  - "None" = Red


---

## Sheet: Application_Channel

**Purpose:** Application-level DLP (database, API, reporting)

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Application/System | Text | 30 | None | Database name, API |
| B | Application Type | Dropdown | 20 | Database/API/Reporting/BI | System type |
| C | Export Restrictions | Dropdown | 22 | Enforced/Advisory/None | Can users export? |
| D | Row Limit (if DB) | Text | 18 | None | Max rows per query |
| E | API Rate Limiting | Dropdown | 20 | Enforced/None | Prevent bulk export |
| F | Approval Required | Dropdown | 20 | Yes/No/Conditional | For large exports |
| G | Output DLP Scanning | Dropdown | 20 | Yes/No/Partial | Scan exports |
| H | Audit Logging | Dropdown | 18 | Yes/No/Partial | Log all exports |
| I | Tested (Yes/No) | Dropdown | 12 | Yes/No | Bypass test |
| J | Test Result | Dropdown | 15 | Blocked/Allowed/Alert | Test outcome |
| K | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| L | Evidence ID | Text | 15 | None | A812-3-APP-001 |

**Pre-Populated Systems (Gray rows 6-10):**

| System | Type | Export Restrictions | Row Limit |
|--------|------|---------------------|-----------|
| HR Database (Oracle) | Database | Enforced (HR only) | 10,000 rows |
| Salesforce CRM | SaaS/API | Advisory | API rate: 100K calls/day |
| Tableau Server | BI/Reporting | None | Unlimited |
| Customer Database (SQL) | Database | Enforced (Approval >100K rows) | 100,000 rows |
| REST API (Custom) | API | Rate limiting | 1000 calls/hour |

**Data Rows:** 20 total (5 examples + 15 blank)

**Data Validation:**

```python
# Column B: Application Type
validation_apptype = {
    'type': 'list',
    'formula1': '"Database,API,Reporting Tool,BI/Analytics,Data Warehouse,Other"',
    'allow_blank': False
}

# Column C, G, H: Enforcement
validation_enforcement = {
    'type': 'list',
    'formula1': '"Enforced,Advisory Only,None"',
    'allow_blank': False
}

# Column E: API Rate Limiting
validation_ratelimit = {
    'type': 'list',
    'formula1': '"Enforced (Hard Limit),Enforced (Soft Limit),Advisory Only,None"',
    'allow_blank': False
}

# Column F: Approval Required
validation_approval = {
    'type': 'list',
    'formula1': '"Yes (Always),Yes (Large Exports),Conditional,No"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column C (Export Restrictions):
  - "Enforced" = Green
  - "Advisory Only" = Yellow
  - "None" = Red (uncontrolled exports)
- Column E (API Rate Limiting):
  - "Enforced (Hard Limit)" = Green
  - "Enforced (Soft Limit)" or "Advisory Only" = Yellow
  - "None" = Red


---

## Sheet: Bypass_Testing

**Purpose:** Document bypass testing methodology and results

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Test ID | Text | 12 | Auto: TEST-001 |
| B | Channel Tested | Dropdown | 20 | Which channel |
| C | Test Date | Date | 15 | DD.MM.YYYY |
| D | Test Methodology | Text (wrap) | 40 | What you did |
| E | Expected Result | Dropdown | 20 | Should Block/Should Monitor |
| F | Actual Result | Dropdown | 20 | Blocked/Allowed/Alert Only |
| G | Bypass Successful | Dropdown | 18 | Yes (Failed)/No (Passed) |
| H | DLP Alert Generated | Dropdown | 18 | Yes/No |
| I | Severity | Dropdown | 15 | Critical/High/Medium/Low |
| J | Remediation Status | Dropdown | 18 | Fixed/In Progress/Open |
| K | Evidence ID | Text | 15 | A812-3-BYP-001 |

**Test ID Auto-Generation:**
```python
="TEST-"&TEXT(ROW()-5,"000")
```

**Data Rows:** 35 (all blank, populated during testing)

**Data Validation:**

```python
# Column B: Channel Tested
validation_channel = {
    'type': 'list',
    'formula1': '"Email,Web,Endpoint USB,Endpoint Clipboard,Endpoint Print,Network FTP,Cloud Storage,Mobile,API,Other"',
    'allow_blank': False
}

# Column E: Expected Result
validation_expected = {
    'type': 'list',
    'formula1': '"Should Block,Should Monitor,Should Encrypt,Should Alert"',
    'allow_blank': False
}

# Column F: Actual Result
validation_actual = {
    'type': 'list',
    'formula1': '"Blocked (Pass),Allowed (Fail),Alert Only (Partial),Encrypted (Pass),Not Tested"',
    'allow_blank': False
}

# Column G: Bypass Successful
validation_bypass = {
    'type': 'list',
    'formula1': '"Yes (Fail - DLP Bypassed),No (Pass - DLP Worked)"',
    'allow_blank': False
}

# Column H: DLP Alert
validation_alert = {
    'type': 'list',
    'formula1': '"Yes,No,Unknown"',
    'allow_blank': False
}

# Column I: Severity
validation_severity = {
    'type': 'list',
    'formula1': '"Critical,High,Medium,Low"',
    'allow_blank': False
}

# Column J: Status
validation_status = {
    'type': 'list',
    'formula1': '"Fixed (Retested Pass),In Progress,Open,Risk Accepted"',
    'allow_blank': False
}
```

**Conditional Formatting:**

- Column G (Bypass Successful):
  - "No (Pass - DLP Worked)" = Green
  - "Yes (Fail - DLP Bypassed)" = Red
- Column J (Remediation Status):
  - "Fixed (Retested Pass)" = Green
  - "In Progress" = Yellow
  - "Open" = Red


---

## Sheet: Gap_Analysis

**Purpose:** Document coverage gaps and remediation plans

*(Same structure as IMP-A.8.12.1 and A.8.12.2)*

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto: GAP-001 |
| B | Channel | Dropdown | 20 | Which channel |
| C | Gap Description | Text (wrap) | 40 | What's missing |
| D | Current State | Text (wrap) | 25 | Now |
| E | Required State | Text (wrap) | 25 | Target |
| F | Risk Level | Dropdown | 15 | Critical/High/Medium/Low |
| G | Regulatory Impact | Text | 25 | Which regulations |
| H | Remediation Action | Text (wrap) | 35 | What to do |
| I | Owner | Text | 20 | Who |
| J | Target Date | Date | 15 | When |
| K | Status | Dropdown | 15 | Open/In Progress/Resolved |
| L | Evidence ID | Text | 15 | A812-3-GAP-001 |

**Data Rows:** 45 total

---

## Sheet: Evidence_Register

*(Same structure as previous IMP documents)*

**Data Rows:** 110 total (1 example + 109 blank)

---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary with channel coverage heatmap

**Layout:**

**Rows 1-5:** Header

**Rows 7-20: Key Metrics**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Channel Coverage % | Weighted average across 7 channels | ≥90% |
| Channels Fully Covered | COUNT of ✅ Compliant channels | 7/7 |
| Channels with Gaps | COUNT of ⚠️ Partial or ❌ Non-Compliant | 0 |
| Critical Gaps | COUNT of Critical risk gaps | 0 |
| Bypass Tests Passed | Tests where DLP blocked / Total tests × 100 | 100% |
| Shadow IT Channels Identified | COUNT of unsanctioned channels | Document all |
| Unprotected Restricted Data Channels | Critical risk | 0 |

**Rows 22-32: Channel Coverage Heatmap**

| Channel | Coverage Status | Enforcement Mode | Bypass Test | Overall Status |
|---------|----------------|------------------|-------------|----------------|
| Email | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Web | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Endpoint | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Network | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Cloud | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Mobile | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |
| Application | ✅/⚠️/❌ | Block/Monitor/None | Pass/Fail | ✅/⚠️/❌ |

**Rows 34-42: Top 5 Critical Bypass Paths** (if any)

- Dynamically pulled from Gap_Analysis (filtered by "Critical")


**Key Formulas:**

```python
# Overall Channel Coverage %
=ROUND(
  (COUNTIF(Email_Channel!L:L,"✅ Compliant") / COUNTA(Email_Channel!L6:L20) * 14) +
  (COUNTIF(Web_Channel!K:K,"✅ Compliant") / COUNTA(Web_Channel!K6:K25) * 14) +
  (COUNTIF(Endpoint_Channel!J:J,"✅ Compliant") / COUNTA(Endpoint_Channel!J6:J30) * 15) +
  (COUNTIF(Network_Channel!H:H,"✅ Compliant") / COUNTA(Network_Channel!H6:H20) * 14) +
  (COUNTIF(Cloud_Channel!K:K,"✅ Compliant") / COUNTA(Cloud_Channel!K6:K25) * 14) +
  (COUNTIF(Mobile_Channel!L:L,"✅ Compliant") / COUNTA(Mobile_Channel!L6:L25) * 14) +
  (COUNTIF(Application_Channel!K:K,"✅ Compliant") / COUNTA(Application_Channel!K6:K20) * 15),
  0
)

# Bypass Tests Passed %
=IFERROR(
  ROUND(
    COUNTIF(Bypass_Testing!G6:G40,'No (Pass - DLP Worked)') /
    COUNTA(Bypass_Testing!G6:G40) * 100,
    0
  ),
  0
)

# Shadow IT Channels
=COUNTIF(Channel_Inventory!H6:H30,"Shadow IT") +
 COUNTIF(Channel_Inventory!H6:H30,"Unsanctioned")

# Unprotected Restricted Data Channels (CRITICAL)
=SUMPRODUCT(
  (Channel_Inventory!G6:G30="Restricted") *
  (Channel_Inventory!I6:I30="No") *
  1
)
```

**Conditional Formatting:**

- Overall Coverage %:
  - ≥90% = Dark green
  - 80-89% = Light green
  - 70-79% = Yellow
  - <70% = Red
- Unprotected Restricted Data Channels:
  - 0 = Green ("✅ No Critical Gaps")
  - ≥1 = Red ("❌ CRITICAL: [count] Unprotected Restricted Data Channels")


---

# 3-7. [Same as IMP-A.8.12.1 & A.8.12.2]

*Data Validation Rules, Conditional Formatting, Cell Protection, Summary Formulas, Evidence Auto-Numbering sections follow same patterns as previous IMP documents.*

---

# APPENDIX: Technical Notes

## A.1 Python Script Integration

**Script:** `generate_a812_3_channel_coverage_assessment.py`

**Key Customization Points:**

- 7 channel sheets (unique structures per channel)
- Bypass testing results tracking
- Channel coverage heatmap in dashboard
- Weighted compliance calculation (different weights per channel)


## A.2 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_3.py`

**Critical Checks:**

- All 7 channel categories present
- Bypass testing sheet populated (at least 1 test per channel)
- Coverage heatmap calculates correctly
- No channels with Restricted data showing "No" DLP coverage


## A.3 Deployment

```bash
python3 generate_a812_3_channel_coverage_assessment.py
# Output: ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx

python3 excel_sanity_check_a812_3.py ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

**Status:** Complete  
**Next Action:** Implement Python generator per specification

---

**END OF SPECIFICATION**

---

*"Life is like riding a bicycle. To keep your balance, you must keep moving."*
— Albert Einstein

*Where bamboo antennas actually work.* 🎋
