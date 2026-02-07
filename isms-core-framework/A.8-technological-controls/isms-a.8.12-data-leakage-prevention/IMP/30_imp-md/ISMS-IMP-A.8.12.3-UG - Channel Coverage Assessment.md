**ISMS-IMP-A.8.12.3-UG - Channel Coverage Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.3-UG |
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
