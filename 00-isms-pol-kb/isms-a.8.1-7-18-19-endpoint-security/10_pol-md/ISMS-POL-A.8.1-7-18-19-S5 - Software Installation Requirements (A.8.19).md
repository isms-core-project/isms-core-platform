# ISMS-POL-A.8.1-7-18-19-S5
## Software Installation Requirements (A.8.19)

**Document ID**: ISMS-POL-A.8.1-7-18-19-S5  
**Title**: Software Installation Requirements (ISO/IEC 27001:2022 Control A.8.19)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations Manager | Initial software installation requirements (A.8.19) |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager
- Security Review: Information Security Manager

**Distribution**: IT operations, security team, endpoint administrators, change management, auditors  
**Related Documents**: 
- ISMS-POL-A.8.1-7-18-19 (Master Framework)
- ISMS-POL-A.8.1-7-18-19-S1 (Executive Summary)
- ISMS-POL-A.8.8 (Vulnerability Management)
- ISMS-IMP-A.8.1-7-18-19-S4 (Software Control Process)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.19

**Official Control Text**:

> *Procedures and measures shall be implemented to securely manage the installation of software on operational systems.*

**Control Purpose**: Ensure that software installations are controlled, approved, tested, and do not introduce security vulnerabilities, malware, or unauthorized functionality to operational endpoints.

**Why This Matters**:

Uncontrolled software installation poses significant security risks:
- **Malware Introduction**: Malicious software installed disguised as legitimate applications
- **Vulnerability Introduction**: Outdated or unpatched software introduces exploitable vulnerabilities
- **Licensing Violations**: Unauthorized or pirated software creates legal and security risks
- **Compatibility Issues**: Untested software conflicts with existing systems, causing instability
- **Data Leakage**: Unauthorized software exfiltrates sensitive data (spyware, unauthorized cloud sync)
- **Resource Consumption**: Cryptocurrency miners, unauthorized applications consume system resources
- **Shadow IT**: Users install unauthorized tools, bypassing security controls and creating visibility gaps
- **Supply Chain Attacks**: Compromised software updates introduce backdoors

Comprehensive software installation controls reduce these risks through approval processes, application control technologies, change management integration, and continuous monitoring.

### 1.2 Scope of A.8.19 Requirements

This section defines mandatory requirements for:

1. **Approved Software List** - Maintaining catalog of permitted software
2. **Software Approval Process** - Evaluating and approving new software
3. **Change Control Integration** - Managing software installations as changes
4. **Unauthorized Software Detection** - Identifying and removing unapproved software
5. **Application Control Technologies** - Technical enforcement of software restrictions
6. **Software Vulnerability Management** - Tracking and patching software vulnerabilities
7. **Software Inventory Management** - Maintaining current software inventory
8. **BYOD Software Controls** - Managing software on personal devices

### 1.3 Integration with A.8.1, A.8.7, A.8.18

While A.8.19 focuses on software installation control:
- **A.8.1** ensures endpoints are managed and baselined (foundation for software control)
- **A.8.7** prevents malware installation (malicious software is unauthorized software)
- **A.8.18** controls privileged utilities (which can bypass software controls)

All four controls work together to create comprehensive endpoint security.

---

## 2. Approved Software List

### 2.1 Requirement: Comprehensive Approved Software List

**REQ-A819-001**: [Organization] **MUST** maintain a comprehensive approved software list (whitelist) covering all permitted software on endpoints.

**Software Categories**:

1. **Universally Approved Software**:
   - Standard tools for all users (e.g., Microsoft Office, web browsers, PDF readers)
   - Corporate applications (e.g., email client, VPN client, collaboration tools)
   - Security tools (anti-malware, endpoint management agents)
   - Operating system and core utilities

2. **Role-Based Approved Software**:
   - Tools for specific job functions (e.g., development tools for developers, CAD software for engineers)
   - Access requires role membership (enforced via application control)

3. **Exception-Based Approved Software**:
   - Software approved for specific users on case-by-case basis
   - Requires individual approval (not role-based)
   - Time-limited approval (e.g., 90 days for temporary project)

**Approved Software List Attributes**:
- Software name and publisher
- Approved versions (specific versions or version range)
- Category (universal, role-based, exception-based)
- Approval date and approver
- Business justification
- Security review status
- License information (license type, count available)
- Update/patch requirements (auto-update enabled? manual patches required?)
- Known vulnerabilities (CVE references if applicable)

**List Maintenance**:
- **Monthly Updates**: New software approvals added monthly
- **Quarterly Reviews**: Entire list reviewed quarterly (remove obsolete software)
- **Annual Comprehensive Review**: Complete list reviewed annually by Security Manager and IT Operations

**Approved Software List Ownership**:
- **IT Operations Manager**: Overall list ownership and maintenance
- **Security Manager**: Security review and approval
- **Software Asset Manager**: License tracking and compliance

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Approved_Software worksheet), approved software list documentation
- Verification Method: Review approved software list for completeness and currency
- Acceptance Criteria: Approved software list exists, reviewed quarterly, documented approvals

### 2.2 Requirement: Software Categorization and Risk Classification

**REQ-A819-002**: Software **MUST** be categorized by business purpose and classified by security risk.

**Business Purpose Categories**:
- **Productivity**: Office applications, email, calendaring
- **Communication**: Chat, video conferencing, collaboration
- **Development**: IDEs, compilers, version control, testing tools
- **Security**: Anti-malware, VPN, encryption, authentication
- **System Utilities**: Backup, file management, compression, drivers
- **Business Applications**: CRM, ERP, industry-specific applications
- **Creative**: Graphic design, video editing, CAD
- **Web Browsers**: Chrome, Firefox, Edge, Safari

**Security Risk Classification**:

| Risk Level | Criteria | Examples | Approval Required |
|------------|----------|----------|-------------------|
| **High** | Internet-facing, processes untrusted data, high privilege requirements | Web browsers, email clients, PDF readers, file transfer tools | Security Manager + IT Operations Manager |
| **Medium** | Local processing, limited network access, standard user privileges | Office applications, collaboration tools, business applications | IT Operations Manager |
| **Low** | No network access, no data processing, minimal privileges | Calculators, basic utilities, drivers | Automated approval (pre-approved list) |

**Risk Assessment Factors**:
- Network connectivity (internet-facing, local network only, no network)
- Privilege requirements (admin rights required, standard user, minimal)
- Data processing (processes sensitive data, processes public data, no data)
- Vulnerability history (frequent CVEs, occasional CVEs, no known CVEs)
- Update mechanisms (automatic secure updates, manual updates, no updates)

**Categorization Benefits**:
- Prioritize security reviews (high-risk software reviewed more thoroughly)
- Tailor controls (high-risk software may require additional monitoring)
- Resource allocation (focus efforts on high-risk software)

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Approved_Software worksheet with risk classifications)
- Verification Method: Review software categorization and risk classifications
- Acceptance Criteria: 100% of approved software has category and risk classification

---

## 3. Software Approval Process

### 3.1 Requirement: New Software Security Review

**REQ-A819-003**: New software **MUST** undergo security review before approval for deployment.

**Security Review Process**:

1. **Initial Request**:
   - Requester (user or department) submits software request
   - Request includes:
     - Software name, version, publisher
     - Business justification (what problem does it solve?)
     - Number of licenses needed
     - Target deployment (which users/endpoints?)
     - Alternative solutions considered

2. **IT Operations Review**:
   - License verification (legitimate source, no pirated software)
   - Compatibility assessment (compatible with existing infrastructure?)
   - Cost analysis (license cost, support cost, training cost)
   - Alternative evaluation (existing approved software that meets need?)

3. **Security Review**:
   - **Vulnerability Assessment**:
     - Check CVE database for known vulnerabilities
     - Review vendor security track record
     - Assess vendor's security update process
   - **Malware Scan**:
     - Installer scanned with multiple anti-malware engines (VirusTotal)
     - Installer verified against publisher's official hash
   - **Behavior Analysis** (high-risk software):
     - Sandbox testing (observe software behavior in isolated environment)
     - Network traffic analysis (does software phone home? to where?)
     - File system analysis (what files does software create/modify?)
     - Registry analysis (what registry keys modified?)
   - **Privacy Assessment**:
     - Data collection practices (what data does software collect?)
     - Data transmission (where is data sent?)
     - Privacy policy review (acceptable data handling?)
   - **License Review**:
     - Open source license compatibility (GPL, MIT, Apache, etc.)
     - Compliance with organizational policies

4. **Approval Decision**:
   - **Approved**: Software added to approved software list
   - **Approved with Conditions**: Approved with restrictions (specific versions only, specific users only, enhanced monitoring)
   - **Denied**: Software rejected (security risks too high, alternatives available, no business justification)

**Approval Authority**:
- **Low-Risk Software**: IT Operations Manager approval sufficient
- **Medium-Risk Software**: IT Operations Manager + Security Manager approval
- **High-Risk Software**: Security Manager + CISO approval required
- **Development Tools on Production Endpoints**: CISO approval required (security risk)

**Approval SLA**:
- Low-risk: 5 business days
- Medium-risk: 10 business days
- High-risk: 15 business days
- Emergency requests: 24 hours (with CISO approval for expedited review)

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Approval_Requests worksheet), approval documentation
- Verification Method: Review sample software approvals for security review completeness
- Acceptance Criteria: 100% of approved software has documented security review

### 3.2 Requirement: Vendor and Supply Chain Verification

**REQ-A819-004**: Software **MUST** be obtained from legitimate vendors and verified for authenticity.

**Vendor Verification**:
- **Official Sources**: Download software only from official vendor websites or authorized distributors
- **No Third-Party Sites**: No downloads from third-party software aggregators (CNET Download, Softonic - risk of bundled malware)
- **No Torrents**: No pirated software or torrents (legal and security risks)

**Authenticity Verification**:
- **Digital Signatures**: Verify installer signed by legitimate publisher (code signing certificate)
- **Hash Verification**: Compare installer hash (SHA-256) against vendor-published hash
- **HTTPS**: Download only via HTTPS (not HTTP - risk of man-in-the-middle)

**Supply Chain Risk Assessment**:
- **Vendor Security Posture**: Has vendor experienced security breaches? How did they respond?
- **Vendor Location**: Geographic considerations (data sovereignty, export controls)
- **Vendor Acquisition**: Has vendor been acquired by potentially problematic entity?
- **Open Source Provenance**: For open source software, verify legitimate source (GitHub official repository, not forks)

**Enterprise Software Repositories**:
- Preferred: Software downloaded from vendor, then uploaded to [Organization]'s internal software repository
- Benefit: Single source of truth, version control, malware scanning before distribution
- All endpoints download from internal repository (not directly from vendors)

**Audit Verification**:
- Evidence: Software approval documentation showing source verification
- Verification Method: Review sample software approvals for vendor verification
- Acceptance Criteria: 100% of approved software has verified source

---

## 4. Change Control Integration

### 4.1 Requirement: Software Installation Change Management

**REQ-A819-005**: Software installations on production endpoints **MUST** follow change management procedures.

**Change Management Integration**:
- All software installations are changes (follows [Organization]'s change management process)
- Change request created before software deployment
- Change request includes:
  - What software is being installed
  - Why (business justification)
  - Where (which endpoints)
  - When (deployment schedule)
  - Who (responsible party)
  - Rollback plan (if deployment fails)

**Change Types**:

| Change Type | Examples | Approval Required | Testing Required |
|-------------|----------|-------------------|------------------|
| **Standard Change** | Pre-approved software from approved list, standard deployment | Automated approval (pre-authorized) | Minimal (already tested) |
| **Normal Change** | New software deployment, software updates | Change Advisory Board (CAB) | Full testing in non-production |
| **Emergency Change** | Critical security patches, urgent business need | Emergency CAB or CISO | Abbreviated testing, rollback plan mandatory |

**Testing Requirements** (Normal Changes):
1. **Pilot Deployment**: Deploy to small pilot group (5-10 users)
2. **Pilot Duration**: Minimum 1 week pilot period
3. **Pilot Validation**: Confirm no compatibility issues, no performance degradation, no user impact
4. **Pilot Feedback**: Collect user feedback, address issues before full rollout
5. **Approval to Proceed**: CAB approves full rollout based on pilot results

**Deployment Methods**:
- **Automated Deployment**: Preferred - deploy via endpoint management (SCCM, Intune, Jamf)
- **Self-Service Portal**: Users request software from self-service portal (if pre-approved)
- **Manual Deployment**: Acceptable for small-scale deployments (<10 endpoints)

**Rollback Plan**:
- All change requests include rollback plan
- Ability to uninstall software if issues arise
- Restoration of previous state (if software replaced existing version)

**Audit Verification**:
- Evidence: Change management records, software deployment logs
- Verification Method: Review sample software installations for change control compliance
- Acceptance Criteria: ≥95% of software installations have change control records

### 4.2 Requirement: Software Update and Patch Management

**REQ-A819-006**: Software updates and security patches **MUST** be managed systematically and deployed according to risk-based SLAs.

**Patch Classification**:
- **Critical Security Patches**: Patches for actively exploited vulnerabilities (zero-day patches)
- **High-Severity Patches**: Patches for high-severity vulnerabilities (CVSS ≥7.0)
- **Medium-Severity Patches**: Patches for medium-severity vulnerabilities (CVSS 4.0-6.9)
- **Feature Updates**: Non-security updates adding functionality

**Patch Deployment SLAs**:

| Patch Type | Testing Required | Deployment SLA | Exceptions |
|------------|------------------|----------------|------------|
| **Critical Security** | Minimal (emergency) | 7 days of release | Emergency CAB approval for same-day deployment if actively exploited |
| **High-Severity** | Pilot testing (1 week) | 30 days of release | Standard change process |
| **Medium-Severity** | Pilot testing (1 week) | 60 days of release | Standard change process |
| **Feature Updates** | Full testing (2 weeks) | 90 days of release (or defer) | Optional updates - deploy based on business need |

**Automatic vs. Manual Updates**:
- **Critical Software (OS, browsers, security tools)**: Automatic updates enabled (where supported)
- **Business Applications**: Manual updates via controlled deployment (test compatibility first)
- **Development Tools**: Manual updates (developer choice, within approved version range)

**Update Testing**:
- Test updates in non-production environment before production deployment
- Validate compatibility with existing applications
- Monitor for performance degradation or instability
- User acceptance testing for business-critical applications

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Patch_Status worksheet), patch deployment reports
- Verification Method: Review patch deployment compliance against SLAs
- Acceptance Criteria: ≥90% compliance with patch deployment SLAs

---

## 5. Unauthorized Software Detection

### 5.1 Requirement: Daily Unauthorized Software Scanning

**REQ-A819-007**: All endpoints **MUST** be scanned daily for unauthorized software, with findings reported to Security team.

**Unauthorized Software Definition**:
- Software not on approved software list
- Approved software but unapproved version (outdated or too new)
- Approved software on unauthorized endpoint (e.g., development tools on production server)
- End-of-life software (no longer supported by vendor)
- Pirated software (unlicensed)

**Detection Methods**:

1. **Software Inventory Tools**:
   - **Windows**: SCCM, Intune, third-party asset management tools
   - **macOS**: Jamf Pro, Intune, Munki
   - **Linux**: Package manager queries (dpkg, rpm, yum), configuration management tools
   - **Cross-Platform**: Unified endpoint management (UEM) solutions

2. **Inventory Collection**:
   - Daily inventory refresh (all installed applications collected)
   - Inventory includes: Application name, version, publisher, install date, install location

3. **Comparison Against Approved List**:
   - Automated comparison: Installed software vs. approved software list
   - Discrepancies flagged as unauthorized software
   - False positives reviewed (legitimate software not yet in approved list)

**Detection Output**:
- Daily report: Endpoints with unauthorized software
- Report includes: Endpoint, software name, version, install date, risk assessment
- Report delivered to Security team and IT Operations

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Unauthorized_Software worksheet), daily scan reports
- Verification Method: Review daily unauthorized software detection reports (last 30 days)
- Acceptance Criteria: Daily scans performed, unauthorized software detected and reported

### 5.2 Requirement: Unauthorized Software Remediation

**REQ-A819-008**: Unauthorized software **MUST** be removed or approved within 24 hours of detection.

**Remediation Process**:

1. **Triage** (within 4 hours):
   - Security team reviews unauthorized software report
   - Determine if software is:
     - **Malicious**: Malware, potentially unwanted program (PUP)
     - **Unauthorized but Legitimate**: User installed without approval
     - **False Positive**: Legitimate approved software not in inventory

2. **Remediation Actions**:

   **Malicious Software**:
   - Immediate removal via anti-malware/EDR
   - Endpoint quarantine (isolate from network)
   - Incident response procedures initiated
   - Root cause investigation (how did malware get installed?)
   - SLA: Immediate (within 1 hour)

   **Unauthorized but Legitimate**:
   - Contact user (why was software installed? what is business need?)
   - Options:
     - **Submit for Approval**: User submits formal software request (if legitimate need)
     - **Remove Software**: No business justification, software removed
     - **Provide Alternative**: Approved alternative software meets user's need
   - SLA: Removal or approval within 24 hours

   **False Positive**:
   - Add software to approved software list (if legitimate)
   - Update inventory system (correct software identification)
   - No user action required
   - SLA: Inventory correction within 24 hours

3. **Automated Remediation** (where feasible):
   - Endpoint management automatically uninstalls unauthorized software
   - User notified of removal and reason
   - User can submit appeal (software request) if needed

4. **User Notification**:
   - User notified when unauthorized software detected
   - Explanation of why software is not permitted
   - Guidance on how to request software approval (if needed)

**Remediation Tracking**:
- All unauthorized software findings tracked to closure
- Remediation actions documented
- Recurring unauthorized software (same software detected multiple times) triggers escalation

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Remediation_Tracking worksheet), remediation records
- Verification Method: Review sample unauthorized software findings for timely remediation
- Acceptance Criteria: ≥95% of unauthorized software remediated within 24 hours

---

## 6. Application Control Technologies

### 6.1 Requirement: Application Control Implementation

**REQ-A819-009**: Application control technologies **MUST** be deployed on all corporate endpoints to enforce software installation restrictions.

**Application Control Technologies**:

1. **Windows Endpoints**:
   - **AppLocker**: Policy-based application control (Windows 10 Pro and above)
   - **Windows Defender Application Control (WDAC)**: Kernel-level application control (Windows 10 Enterprise)
   - Preferred: WDAC (stronger security) or AppLocker (easier management)

2. **macOS Endpoints**:
   - **Gatekeeper**: Verifies apps from identified developers
   - **System Integrity Protection (SIP)**: Protects system files and processes
   - **MDM Restrictions**: Block app installation except from approved sources

3. **Linux Endpoints**:
   - **AppArmor**: Mandatory access control (Ubuntu, Debian)
   - **SELinux**: Security-Enhanced Linux (Red Hat, CentOS, Fedora)
   - **Package Manager Restrictions**: Restrict package installation to authorized users only

4. **Mobile Devices**:
   - **iOS**: App Store restrictions via MDM, block app installation from untrusted sources
   - **Android**: Google Play restrictions, block sideloading (unknown sources)

**Application Control Policies**:

**Default Deny Approach** (Whitelisting - Recommended):
- Only approved software can execute
- Any software not on whitelist is blocked
- Stronger security, more management overhead

**Default Allow with Blacklist** (Blacklisting - Less Secure):
- All software can execute except known bad software
- Easier to implement, weaker security
- Acceptable only if whitelist not feasible (e.g., development environments)

**Hybrid Approach**:
- Whitelist for production endpoints (stricter control)
- Blacklist for development endpoints (developer flexibility)

**Whitelisting Methods**:
- **Publisher Rules**: Allow all software signed by specific publishers (e.g., Microsoft, Adobe)
- **Hash Rules**: Allow specific files based on SHA-256 hash
- **Path Rules**: Allow software in specific directories (e.g., C:\Program Files\)
- **Certificate Rules**: Allow software signed with specific certificates

**Enforcement Modes**:
- **Audit Mode**: Log violations without blocking (initial deployment, tuning)
- **Enforcement Mode**: Block unauthorized software execution (production mode)

**Deployment Approach**:
1. **Audit Mode** (2-4 weeks): Collect baseline of all software usage
2. **Tuning**: Create whitelist based on audit mode findings
3. **Pilot Enforcement** (2 weeks): Enforcement mode on pilot group, address exceptions
4. **Full Enforcement**: Enforcement mode on all corporate endpoints

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Application_Control worksheet), AppLocker/WDAC policies
- Verification Method: Review application control configuration, test blocking of unauthorized software
- Acceptance Criteria: Application control deployed on ≥90% of corporate endpoints in enforcement mode

### 6.2 Requirement: Application Control Exceptions

**REQ-A819-010**: Application control exceptions **MUST** be documented, approved, and reviewed regularly.

**Exception Types**:

1. **User Exceptions**:
   - Specific users need broader software access (e.g., developers, power users)
   - Approval: Security Manager + User's Manager
   - Review: Semi-annual

2. **Path Exceptions**:
   - Specific directories allowed for software execution (e.g., development directories)
   - Approval: Security Manager
   - Compensating Controls: Enhanced monitoring, no sensitive data in exception paths
   - Review: Quarterly

3. **Publisher Exceptions**:
   - Trust all software from specific publisher (lower overhead)
   - Approval: Security Manager (trusted publishers only)
   - Review: Annual

**Exception Documentation**:
- Exception type and scope
- Business justification
- Approver and approval date
- Compensating controls (if applicable)
- Review frequency
- Expiration date (if time-limited)

**Exception Review**:
- Quarterly review of all exceptions
- Remove expired or unnecessary exceptions
- Verify compensating controls still effective

**Audit Verification**:
- Evidence: Application control exception list, approval records, review documentation
- Verification Method: Review exception list for completeness and currency
- Acceptance Criteria: All exceptions documented, approved, and reviewed per schedule

---

## 7. Software Vulnerability Management

### 7.1 Requirement: Software Vulnerability Tracking

**REQ-A819-011**: Known vulnerabilities in installed software **MUST** be tracked and remediated according to risk-based SLAs.

**Vulnerability Identification**:
- **Vulnerability Scanners**: Tenable Nessus, Qualys, Rapid7 (scan endpoints for vulnerable software)
- **Software Inventory Correlation**: Cross-reference software inventory with CVE database
- **Vendor Notifications**: Monitor vendor security advisories for installed software
- **Threat Intelligence**: Monitor security blogs, CERT advisories for emerging threats

**Vulnerability Assessment**:
- **CVSS Score**: Common Vulnerability Scoring System (0.0-10.0 severity)
- **Exploitability**: Is vulnerability actively exploited? (CISA KEV catalog)
- **Attack Complexity**: How difficult is exploitation? (low complexity = higher priority)
- **Impact**: Confidentiality, integrity, availability impact

**Vulnerability Prioritization**:

| Priority | Criteria | Remediation SLA |
|----------|----------|-----------------|
| **Critical** | CVSS ≥9.0 AND actively exploited | 7 days |
| **High** | CVSS ≥7.0 OR remotely exploitable without authentication | 30 days |
| **Medium** | CVSS 4.0-6.9 | 60 days |
| **Low** | CVSS <4.0 | 90 days or next maintenance cycle |

**Remediation Options**:
1. **Patch**: Apply vendor security patch (preferred)
2. **Upgrade**: Upgrade to non-vulnerable version
3. **Workaround**: Apply vendor-recommended workaround (temporary mitigation)
4. **Remove**: Uninstall vulnerable software if not needed
5. **Compensating Controls**: Network isolation, access restrictions (if patching not feasible)
6. **Risk Acceptance**: CISO accepts risk if remediation not possible (documented)

**Vulnerability Tracking**:
- All vulnerabilities tracked in vulnerability management system
- Status: Open, In Progress, Remediated, Risk Accepted
- Owner assigned for remediation
- SLA monitoring and escalation

**Audit Verification**:
- Evidence: Software_Controls.xlsx (Vulnerability_Status worksheet), vulnerability scan reports
- Verification Method: Review vulnerability remediation compliance against SLAs
- Acceptance Criteria: ≥90% of vulnerabilities remediated within SLA

### 7.2 Requirement: End-of-Life Software Management

**REQ-A819-012**: End-of-life (EOL) software **MUST** be identified and replaced or isolated.

**End-of-Life Definition**:
- Vendor no longer provides security updates (no patches)
- Vendor no longer provides technical support
- Software reached vendor-announced EOL date

**EOL Software Risks**:
- New vulnerabilities will not be patched (perpetual risk)
- Incompatibility with modern systems
- Compliance violations (some regulations prohibit EOL software)

**EOL Software Handling**:

1. **Preferred: Replace**:
   - Upgrade to current supported version
   - Migrate to alternative supported software
   - SLA: Replace within 90 days of EOL date

2. **If Replacement Not Immediately Feasible**:
   - **Isolate**: Network segmentation (no internet access, limited network access)
   - **Monitor**: Enhanced monitoring for anomalous activity
   - **Restrict Access**: Minimal users, MFA required
   - **Plan Replacement**: Documented replacement plan with timeline (max 12 months)
   - **Risk Acceptance**: CISO accepts risk until replacement (documented)

3. **Prohibited**:
   - EOL software on internet-facing endpoints (unacceptable risk)
   - EOL software processing sensitive data (without isolation and compensating controls)

**EOL Software Monitoring**:
- Quarterly scan for EOL software
- Proactive monitoring of vendor EOL announcements (plan ahead)
- Replacement projects initiated 6 months before EOL date

**Audit Verification**:
- Evidence: Software_Controls.xlsx (EOL_Software worksheet), replacement plans
- Verification Method: Review EOL software inventory and replacement status
- Acceptance Criteria: All EOL software has replacement plan or risk acceptance

---

## 8. BYOD Software Controls

### 8.1 Requirement: BYOD Software Restrictions

**REQ-A819-013**: BYOD devices **MUST** implement software controls for corporate data containers, while respecting user privacy.

**BYOD Software Control Approach**:

**Containerized Management** (Mobile Application Management - MAM):
- Corporate apps and data in separate container
- [Organization] controls corporate container only
- Personal apps outside container (user privacy protected)

**Corporate Container Controls**:
1. **Approved Corporate Apps**: Only approved corporate apps deployed to container
2. **Container Isolation**: Corporate apps cannot access personal data, personal apps cannot access corporate data
3. **Copy/Paste Restrictions**: No copy/paste between corporate and personal apps
4. **Document Sharing Restrictions**: Corporate documents cannot be opened in personal apps
5. **Screenshot Prevention**: Screenshots blocked in corporate apps (data leakage prevention)

**Personal App Restrictions** (What [Organization] Does NOT Control):
- [Organization] does not inventory personal apps (privacy protection)
- [Organization] does not restrict personal app installation
- [Organization] does not monitor personal app usage
- User has full control over personal apps and data

**Minimum OS Requirements**:
- **iOS**: iOS 15 or later (security updates)
- **Android**: Android 11 or later (security features)
- Older OS versions prohibited from accessing corporate data (security risk)

**BYOD Laptops/Desktops** (Different Approach):
- If BYOD laptops allowed (less common):
  - VDI/Remote Desktop access only (no local corporate data)
  - Network access control (NAC) verifies anti-malware and OS updates before network access
  - No application control on BYOD laptops (user privacy)

**Audit Verification**:
- Evidence: BYOD policy documentation, MDM configuration showing containerization
- Verification Method: Review BYOD software controls and privacy protections
- Acceptance Criteria: BYOD devices use containerized approach, corporate/personal data separated

---

## 9. Audit Verification Criteria

### 9.1 Evidence Requirements for A.8.19 Compliance

**Mandatory Evidence**:

1. **Approved Software List**: Software_Controls.xlsx (Approved_Software worksheet)
   - Complete list with categorization and risk classification
   - Quarterly review documentation

2. **Software Approval Records**: Software_Controls.xlsx (Approval_Requests worksheet)
   - Security reviews for new software
   - 100% of approved software has documented approval

3. **Change Control Records**: Change management system records
   - Software installations follow change management
   - ≥95% compliance with change control

4. **Unauthorized Software Detection**: Software_Controls.xlsx (Unauthorized_Software worksheet)
   - Daily scans performed
   - ≥95% remediated within 24 hours

5. **Application Control**: Software_Controls.xlsx (Application_Control worksheet)
   - Application control deployed on ≥90% of corporate endpoints
   - Enforcement mode active

6. **Patch Management**: Software_Controls.xlsx (Patch_Status worksheet)
   - Patch deployment compliance ≥90% against SLAs
   - Critical patches deployed within 7 days

7. **Vulnerability Management**: Software_Controls.xlsx (Vulnerability_Status worksheet)
   - Vulnerability remediation ≥90% within SLA
   - EOL software identified with replacement plans

8. **Software Inventory**: Current software inventory from endpoint management tools

### 9.2 Assessment Methodology

**Compliance Scoring**:

**A.8.19 Compliance Score** = Weighted average:
- Approval Compliance (40%): (Approved software installs / Total software installs) × 100
- Unauthorized Software Rate (inverse, 30%): 100 - (Unauthorized software incidents / Total endpoints) × 100
- Application Control Deployment (30%): (Endpoints with application control / Total corporate endpoints) × 100

**Compliance Thresholds**:
- **Green (Compliant)**: ≥90%
- **Yellow (Partial Compliance)**: 70-89%
- **Red (Non-Compliant)**: <70%

**Assessment Frequency**:
- **Daily**: Unauthorized software detection
- **Weekly**: Patch deployment progress
- **Monthly**: Comprehensive software control metrics
- **Quarterly**: Approved software list review
- **Annual**: Full assessment, policy review

### 9.3 Auditor Verification Steps

**For ISO 27001 Certification Audits**:

1. **Review Policy Documentation**:
   - ISMS-POL-A.8.1-7-18-19-S5 (this document)
   - Implementation procedures (ISMS-IMP-A.8.1-7-18-19-S4)
   - Approved software list

2. **Review Evidence**:
   - Software_Controls.xlsx (all worksheets)
   - Software approval records
   - Change control records
   - Unauthorized software reports
   - Application control configuration
   - Patch deployment reports

3. **Sample Testing**:
   - Select random sample of 20 endpoints
   - Verify software inventory accurate
   - Verify application control active (test unauthorized software execution - should be blocked)
   - Verify approved software only (compare inventory to approved list)

4. **Interview Personnel**:
   - IT Operations: Understanding of approval process, change control
   - Security team: Knowledge of unauthorized software remediation, vulnerability management

5. **Verify Processes**:
   - Review sample software approval requests for completeness
   - Review sample unauthorized software incidents for timely remediation
   - Review patch deployment compliance

**Acceptance Criteria for Audit**:
- All evidence available and complete
- Compliance scores meet thresholds (≥90% target)
- Sample testing confirms controls effective
- Personnel demonstrate understanding of processes
- Unauthorized software remediated promptly
- Patches deployed per SLAs

---

**END OF SECTION 5**

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations Manager | Initial software installation requirements (A.8.19) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**

**Next Document**: ISMS-POL-A.8.1-7-18-19-S6 (Assessment & Evidence Framework)