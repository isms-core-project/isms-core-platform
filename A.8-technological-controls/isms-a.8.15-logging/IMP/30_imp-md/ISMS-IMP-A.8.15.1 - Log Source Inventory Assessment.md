**ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.1 |
| **Version** | 1.0 |
| **Assessment Area** | Log Source Inventory & Event Logging Completeness |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements) |
| **Purpose** | Catalog all systems generating logs, verify logging completeness against policy requirements, and identify gaps in event logging coverage |
| **Target Audience** | IT Operations, System Owners, Application Owners, Security Team, Compliance Officers, Auditors, Workbook Developers (Python/Excel script maintainers) |
| **Assessment Type** | Inventory & Compliance Verification |
| **Review Cycle** | Annual (full inventory), Quarterly (new systems update) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Log Source Inventory assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Question-by-Question Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure Overview
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Formula Definitions
  - Python Script Usage Notes


**Target Audiences:**

- **Part I:** Assessment users (IT Operations, System Owners, Application Owners, Security Team)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** IT Operations, System Owners, Application Owners, Security Team

---

# Assessment Overview

## What This Assessment Evaluates

This assessment creates a comprehensive inventory of ALL systems generating logs within [Organization] and verifies that required events are being logged per policy requirements.

**Key Questions Answered:**

- What systems exist in our environment? (servers, applications, network devices, security tools, cloud services)
- What events are these systems logging?
- Are we logging ALL required event types per ISMS-POL-A.8.15, Section 2.1?
- What gaps exist? (systems not logging, required events missing)
- Where is logging configuration documented?


## Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.8.15**: Logs that record activities, exceptions, faults and other relevant events should be produced, stored, protected and analysed
- **ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements)**: Mandatory log events including authentication, authorization, administrative actions, security events, system events, network events, application events
- **ISMS-POL-A.8.15, Section 1.4 (Scope)**: All information systems, network devices, security tools, databases, cloud services, authentication systems


**Security Impact**: You cannot investigate what you don't log. Incomplete log coverage creates blind spots attackers exploit.

**Compliance Impact**: Insufficient logging is a **major non-conformity** in ISO 27001 audits. Auditors will verify comprehensive log source inventory exists.

**Audit Evidence**: This assessment workbook provides **objective evidence** of systematic logging implementation.

## Assessment Outputs

**Primary Deliverable**: Excel workbook with 13 sheets containing:

1. **Complete Log Source Inventory**: Every system, application, network device cataloged
2. **Event Logging Completeness**: Verification each system logs required event types
3. **Gap Analysis**: Systems with missing or incomplete logging identified
4. **Compliance Scoring**: Percentage of systems meeting logging requirements
5. **Remediation Plan**: Prioritized action items with owners and timelines

**Typical Assessment Results**:

- **100-250 log sources** (small organization)
- **250-1000 log sources** (medium organization)
- **1000+ log sources** (large/complex organization)


**Time Investment**: 

- Initial assessment: 40-80 hours (depending on environment size)
- Quarterly updates: 4-8 hours (new systems only)


---

# Prerequisites

## Required Information

Before starting this assessment, gather:

**System Inventories**:

- [ ] CMDB (Configuration Management Database) export or equivalent system inventory
- [ ] Network device inventory (routers, switches, firewalls, load balancers)
- [ ] Application portfolio list (all business applications)
- [ ] Cloud service inventory (SaaS, IaaS, PaaS subscriptions)
- [ ] Database inventory (all database systems)
- [ ] Security tool inventory (SIEM, IDS/IPS, anti-malware, DLP, web filters)


**Documentation**:

- [ ] System architecture diagrams
- [ ] Network topology diagrams
- [ ] Application dependency maps
- [ ] Data flow diagrams
- [ ] Existing logging documentation (if any)


**Access**:

- [ ] Read access to system configurations for sampling
- [ ] Access to SIEM console (if deployed)
- [ ] Coordination with System Owners for configuration verification


## Required Resources

**Personnel** (involvement required):

- **IT Operations Manager**: Provides system inventory, coordinates with System Owners
- **System Owners**: Verify logging configuration for their systems (15-30 mins per system)
- **Application Owners**: Document application-specific logging
- **Network Team**: Document network device logging
- **Security Team**: Verify security tool logging
- **Cloud Administrators**: Document cloud service logging


**Tools**:

- Microsoft Excel 2016 or later (workbook compatibility)
- Access to system management consoles for verification
- SIEM console access (if applicable)


**Timeline**:

- **Week 1-2**: Gather inventories and documentation
- **Week 3-6**: System-by-system assessment and verification
- **Week 7**: Gap analysis and remediation planning
- **Week 8**: Review, validation, and approval


## Policy Knowledge Required

**Assessors MUST be familiar with**:

- **ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements)**: Mandatory log events by category
- **ISMS-POL-A.8.15, Annex A (Logging Decision Matrix)**: Decision tree for determining required events
- **ISMS-REF-A.8.15 (Logging Standards Reference)**: Log format specifications (optional - technical detail)


**Recommended**: Review ISMS-POL-A.8.15 Section 2.1 before starting assessment.

---

# Assessment Workflow

## High-Level Process

```
Step 1: Gather System Inventory
  |
  v
Step 2: Categorize Systems (by type, criticality, data classification)
  |
  v
Step 3: Determine Required Events (per ISMS-POL-A.8.15, Section 2.1 + Annex A)
  |
  v
Step 4: Verify Actual Logging Configuration (sample systems, review configs)
  |
  v
Step 5: Identify Gaps (required events not logged)
  |
  v
Step 6: Calculate Compliance Scores (automated in workbook)
  |
  v
Step 7: Prioritize Remediation (critical gaps first)
  |
  v
Step 8: Approval & Sign-Off (3-level approval)
```

## Detailed Workflow

**Phase 1: System Inventory Collection (Sheet 2)**

1. Export system list from CMDB or asset management system
2. Add network devices from network inventory
3. Add applications from application portfolio
4. Add cloud services from subscription lists
5. Add security tools from security architecture documentation
6. **Result**: Comprehensive system list (typically 100-1000+ entries)

**Phase 2: System Categorization (Sheet 2)**

For each system, document:

- System name, owner, business function
- System type (server, application, network device, security tool, cloud service, database)
- Data classification (Public, Internal, Confidential, Restricted per organizational classification)
- System criticality (Critical, High, Standard, Low per business impact)
- Deployment model (On-premises, Cloud, Hybrid, Third-party hosted)


**Phase 3: Required Events Determination (Sheet 3)**

For each system, use **ISMS-POL-A.8.15, Annex A (Logging Decision Matrix)** to determine:

- What event categories are mandatory? (Authentication, Authorization, Administrative, Security, System, Network, Application)
- What retention period applies? (per ISMS-POL-A.8.15, Section 2.3 + Annex A.2)
- Are there special regulatory requirements? (PCI DSS, HIPAA, SOX per ISMS-POL-A.8.15, Section 1.5)


**Phase 4: Logging Configuration Verification (Sheets 4-9)**

For each system, verify actual logging configuration:

- **Authentication Logging** (Sheet 4): Login success/failure, logout, account lockouts, password changes, MFA events
- **Authorization & Access** (Sheet 5): Access to sensitive data, privilege escalation, access control changes
- **Administrative Activity** (Sheet 6): Configuration changes, account management, privilege grants, policy changes
- **Security Event Logging** (Sheet 7): Malware detection, intrusion attempts, firewall blocks, DLP alerts
- **Application & Database** (Sheet 8): Errors, exceptions, database transactions, API authentication
- **Network Device Logging** (Sheet 9): Firewall rule matches, VPN connections, network segmentation traversals


**Verification Methods**:

- Review system logging configuration (syslog.conf, application.properties, registry settings)
- Sample logs from SIEM or local log files to verify events present
- Interview System Owners to confirm logging configuration
- Review vendor documentation for logging capabilities


**Phase 5: Gap Identification (Sheet 10: Gap_Analysis)**

For each gap discovered:

- Document system affected
- Identify missing event types or configuration issues
- Assess risk severity (Critical, High, Medium, Low)
- Propose remediation action
- Assign owner and timeline


**Phase 6: Evidence Collection (Sheet 11: Evidence_Register)**

For key findings, attach evidence:

- Configuration screenshots
- Sample log entries
- System Owner confirmations
- Vendor documentation excerpts


**Phase 7: Summary Review (Sheet 12: Summary_Dashboard)**

Review overall assessment results:
- Compliance scores by system category
- Gap distribution by severity
- Remediation priority matrix
- Overall logging maturity score

**Phase 8: Approval (Sheet 13: Approval_Sign_Off)**

Three-level approval workflow:
1. **System Owner Confirmation**: Owners confirm assessment accuracy for their systems
2. **IT Operations Manager**: Validates overall inventory completeness
3. **Information Security Manager / CISO**: Approves assessment and remediation plan

---

# Question-by-Question Guidance

This section provides detailed guidance for completing each assessment sheet.

## Sheet 2: System Inventory

**Purpose**: Catalog every system that should be logging.

**Column-by-Column Guidance**:

**Column A: System ID**

- Format: Auto-increment (SYS-001, SYS-002, etc.)
- Unique identifier for tracking across assessment cycles


**Column B: System Name**

- Official system name (hostname for servers, product name for applications)
- Example: "PROD-WEB-01", "SAP ERP", "Microsoft 365", "FortiGate Firewall"


**Column C: System Type**

- Dropdown: Server, Application, Network Device, Security Tool, Database, Cloud Service, Authentication System, Other
- **Decision Guide**:
  - Server: Physical/virtual server OS (Windows Server, Linux, ESXi)
  - Application: Business application (ERP, CRM, HR system, custom apps)
  - Network Device: Router, switch, firewall, load balancer, proxy
  - Security Tool: SIEM, IDS/IPS, anti-malware, DLP, web filter
  - Database: Database management system (SQL Server, Oracle, MySQL, PostgreSQL, MongoDB)
  - Cloud Service: SaaS, IaaS, PaaS (AWS, Azure, GCP, Microsoft 365, Salesforce)
  - Authentication System: Active Directory, LDAP, SSO, MFA platform
  - Other: Anything not fitting above categories


**Column D: System Owner**

- Person responsible for the system (email or name)
- **Important**: System Owner confirms logging configuration accuracy during review


**Column E: Business Function**

- What business purpose does this system serve?
- Examples: "Financial Reporting", "Customer Relationship Management", "Email Communication", "Network Security", "User Authentication"


**Column F: Data Classification**

- Dropdown: Public, Internal, Confidential, Restricted
- Per [Organization]'s data classification policy
- **Impact**: Higher classification = more comprehensive logging required (per ISMS-POL-A.8.15, Annex A.1)


**Column G: System Criticality**

- Dropdown: Critical, High, Standard, Low
- **Definition**:
  - Critical: System failure causes major business disruption, financial loss, or regulatory violation
  - High: System failure causes significant operational impact
  - Standard: System supports business operations but failure is manageable
  - Low: Minimal business impact if system fails
- **Impact**: Higher criticality = more comprehensive logging required (per ISMS-POL-A.8.15, Annex A.1)


**Column H: Deployment Model**

- Dropdown: On-Premises, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS), Hybrid, Third-Party Hosted
- **Impact**: Affects where logs are stored and how they're collected


**Column I: Operating System / Platform**

- For servers: OS and version (e.g., "Windows Server 2022", "Ubuntu 22.04 LTS", "ESXi 8.0")
- For applications: Platform (e.g., "Java 11", ".NET 6", "Node.js 18")
- For network devices: OS (e.g., "FortiOS 7.2", "Cisco IOS 15.7", "Junos 22.1")
- For cloud: Service name (e.g., "AWS EC2", "Azure SQL Database", "Google Workspace")


**Column J: Vendor / Manufacturer**

- For commercial products: Vendor name (Microsoft, Cisco, Fortinet, Oracle, etc.)
- For open-source: "Open Source" or project name (Apache, Nginx, PostgreSQL, etc.)
- For custom/in-house: "In-House Development"


**Column K: Logging Capability**

- Dropdown: Yes, Partial, No, Unknown
- **Yes**: System has native logging capabilities
- **Partial**: Limited logging (e.g., only errors, not all required events)
- **No**: System does not log or logging not enabled
- **Unknown**: Logging capability not yet determined (requires investigation)


**Column L: Log Forwarding Status**

- Dropdown: Implemented, Partial, Planned, Not Implemented, N/A
- **Implemented**: Logs forwarded to central SIEM/log management
- **Partial**: Some logs forwarded, some local only
- **Planned**: Log forwarding scheduled but not yet configured
- **Not Implemented**: No log forwarding, logs remain local only
- **N/A**: Centralized logging not applicable (e.g., isolated test system)


**Column M: SIEM Integration**

- Dropdown: Yes, No, Planned, N/A
- **Yes**: System logs parsed and correlated in SIEM
- **No**: System exists but logs not integrated into SIEM
- **Planned**: SIEM integration scheduled
- **N/A**: System not intended for SIEM integration (e.g., standalone test lab)


**Column N: Notes**

- Free text for additional context, exceptions, or special considerations
- Example: "Logs retained locally due to performance concerns", "Third-party managed service - logs available via API", "Decommissioned Q2 2026"


---

## Sheet 3: Event Logging Requirements Summary

**Purpose**: For each system, determine WHAT events must be logged based on system characteristics and policy requirements.

This sheet links system attributes (from Sheet 2) to logging requirements (from ISMS-POL-A.8.15, Section 2.1).

**Column-by-Column Guidance**:

**Columns A-B: System ID, System Name**

- Auto-populated from Sheet 2 (external reference)


**Columns C-D: System Type, Data Classification**

- Auto-populated from Sheet 2 (external reference)


**Column E: Required Event Categories**

- Multi-select or comma-separated list
- Values: Authentication, Authorization, Administrative, Security, System, Network, Application
- **Decision Logic** (per ISMS-POL-A.8.15, Annex A.1):
  - **Critical Systems OR Restricted Data**: ALL event categories required
  - **High-Value Systems OR Confidential Data**: Authentication, Authorization, Administrative, Security, System, Application
  - **Standard Systems (Internal Data)**: Authentication, Administrative, Security (optional: Application, System)
  - **Low-Impact Systems (Public Data)**: Authentication (failures), Administrative, Critical Security Events


**Column F: Authentication Events Required?**

- Dropdown: Yes (All), Yes (Failures Only), No
- Per ISMS-POL-A.8.15, Section 2.1 (Authentication Events): Login success/failure, logout, lockouts, password changes, MFA


**Column G: Authorization Events Required?**

- Dropdown: Yes, No
- Per ISMS-POL-A.8.15, Section 2.1 (Authorization Events): Access to sensitive data, privilege escalation, access control changes


**Column H: Administrative Actions Required?**

- Dropdown: Yes, No
- Per ISMS-POL-A.8.15, Section 2.1 (Administrative Actions): Configuration changes, account management, privilege grants, policy changes


**Column I: Security Events Required?**

- Dropdown: Yes, No
- Per ISMS-POL-A.8.15, Section 2.1 (Security Events): Malware detection, intrusion attempts, firewall blocks, DLP alerts


**Column J: System Events Required?**

- Dropdown: Yes, No
- Per ISMS-POL-A.8.15, Section 2.1 (System Events): Startup/shutdown, service status, errors, resource warnings


**Column K: Network Events Required?**

- Dropdown: Yes, No, N/A
- Per ISMS-POL-A.8.15, Section 2.1 (Network Events): Firewall rule matches, VPN connections, network segmentation traversals
- N/A for non-network systems


**Column L: Application Events Required?**

- Dropdown: Yes, No, N/A
- Per ISMS-POL-A.8.15, Section 2.1 (Application Events): Errors, exceptions, database transactions, API authentication
- N/A for infrastructure systems without applications


**Column M: Retention Period (Online)**

- Auto-calculated based on log category and regulatory requirements
- Per ISMS-POL-A.8.15, Annex A.2 (Retention Period Selection Matrix)
- Typical values: 3 months, 6 months, 12 months


**Column N: Retention Period (Archive)**

- Auto-calculated based on regulatory requirements
- Per ISMS-POL-A.8.15, Annex A.2
- Typical values: 6 months, 1 year, 7 years


**Column O: Special Regulatory Requirements**

- Dropdown: None, PCI DSS, HIPAA, SOX, GDPR/nDSG, Multiple
- Per ISMS-POL-A.8.15, Section 1.5 (Regulatory Applicability)
- **PCI DSS**: 12 months minimum online retention
- **HIPAA**: 6 years minimum total retention
- **SOX**: 7 years minimum for financial systems


**Column P: Rationale / Policy Reference**

- Auto-populated text explaining WHY these requirements apply
- Example: "Critical system with Restricted data requires comprehensive logging per ISMS-POL-A.8.15, Annex A.1"


---

## Sheets 4-9: Event Category Verification

These sheets verify actual logging configuration against requirements for each event category.

**Common Structure** (all event category sheets):

**Columns A-B**: System ID, System Name (from Sheet 2)
**Column C**: Logging Required? (Yes/No from Sheet 3)
**Column D**: Logging Status (Implemented, Partial, Not Implemented, N/A)
**Column E**: Log Format (Syslog, CEF, JSON, Windows Event Log, Proprietary, Other)
**Column F**: Log Location (Local, SIEM, Cloud Service, Both)
**Column G**: Specific Events Logged (checklist of required sub-events)
**Column H**: Sample Log Entry (paste sample showing required fields)
**Column I**: Verification Method (Configuration Review, Log Sample, System Owner Confirmation, Documentation Review)
**Column J**: Verification Date
**Column K**: Verified By
**Column L**: Compliance Status (Compliant, Non-Compliant, Partial Compliance)
**Column M**: Gap Description (if non-compliant or partial)
**Column N**: Evidence Reference (pointer to Sheet 11 Evidence_Register)
**Column O**: Notes

### Sheet 4: Authentication Logging

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (Authentication Events):

- [ ] Successful login attempts (user ID, timestamp, source IP, authentication method)
- [ ] Failed login attempts (attempted user ID, timestamp, source IP, failure reason)
- [ ] Logout events (user ID, session duration, timestamp)
- [ ] Account lockouts (user ID, lockout reason, timestamp, triggering events)
- [ ] Password changes/resets (user ID, timestamp, initiated by whom)
- [ ] Multi-factor authentication events (MFA success/failure, method used, timestamp)


**Common Gaps to Check For**:

- Successful logins logged but failed logins not captured
- Local logins logged but remote/RDP logins missing
- Interactive logins captured but service account logins ignored
- Password changes not logged
- MFA events not logged (common oversight)


**Verification Example**:
```
Sample Log Entry (Column H):
Jan 21 2026 14:35:22 PROD-WEB-01 sshd[12345]: Accepted publickey for admin from 192.168.1.50 port 55832 ssh2: RSA SHA256:xyz123...

Interpretation: Successful SSH login captured with timestamp, user, source IP, authentication method
```

### Sheet 5: Authorization & Access

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (Authorization Events):

- [ ] Access to sensitive data (user ID, data classification, action performed, timestamp)
- [ ] Privilege escalation (user ID, escalated privileges, justification, timestamp)
- [ ] Access control changes (modified permissions, affected resources, change initiator, timestamp)
- [ ] File/object access for classified data (user ID, resource accessed, action, outcome)
- [ ] Denied access attempts (user ID, attempted resource, denial reason, timestamp)


**Common Gaps**:

- Successful access logged but denied attempts not captured
- Permission changes not logged
- Privilege escalation (sudo, Run As Administrator) not logged
- File access auditing not enabled on sensitive shares/folders


### Sheet 6: Administrative Activity

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (Administrative Actions):

- [ ] System configuration changes (changed parameters, previous/new values, administrator, timestamp)
- [ ] User account creation/modification/deletion (affected user, changes made, administrator, timestamp)
- [ ] Privilege grants/revocations (affected user, privilege type, administrator, timestamp)
- [ ] Security policy changes (policy modified, change details, administrator, approval reference, timestamp)
- [ ] Installation/removal of software/services (package name, version, administrator, timestamp)
- [ ] Firmware/system updates (system identifier, update applied, administrator, timestamp)


**Common Gaps**:

- Configuration changes logged but not detailed (missing before/after values)
- Software installations logged but not de-installations
- Policy changes not logged or insufficient detail
- No correlation with change management tickets


### Sheet 7: Security Event Logging

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (Security Events):

- [ ] Malware detection/prevention actions (malware type, affected system, action taken, timestamp)
- [ ] Intrusion detection/prevention alerts (alert type, source/destination, action taken, timestamp)
- [ ] Firewall blocks/rule violations (source/destination, protocol/port, rule violated, timestamp)
- [ ] Data loss prevention (DLP) events (data type, egress channel, action taken, timestamp)
- [ ] Encryption/decryption operations for audit trails (user, operation type, data classification, timestamp)
- [ ] Certificate validation failures (certificate subject, validation error, timestamp)
- [ ] Security tool configuration changes (tool name, configuration modified, administrator, timestamp)


**Common Gaps**:

- Anti-malware detections logged but not prevention actions
- Firewall allows logged but not blocks (inverse of expected)
- IDS alerts generated but not logged centrally
- DLP policy violations not logged (configuration oversight)


### Sheet 8: Application & Database

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (System Events):

- [ ] System startup/shutdown (system identifier, event type, timestamp)
- [ ] Service starts/stops/restarts (service name, action, initiated by, timestamp)
- [ ] System errors/crashes (error type, affected system/component, error details, timestamp)
- [ ] Resource exhaustion warnings (resource type, utilization level, affected system, timestamp)
- [ ] Time synchronization events (time source, synchronization status, drift detected, timestamp)


**Common Gaps**:

- Startup logged but not shutdown (system down before log written)
- Service starts logged but not stops
- Generic errors logged without sufficient detail for investigation
- Time sync failures not logged (critical for log correlation)


### Sheet 9: Network Device Logging

**Specific Events Checklist (Column G)**:
Per ISMS-POL-A.8.15, Section 2.1 (Network Events):

- [ ] Firewall rule matches for security-relevant traffic (source/destination, rule matched, action, timestamp)
- [ ] VPN connections/disconnections (user ID, VPN gateway, connection duration, timestamp)
- [ ] Network segmentation traversals (source/destination segment, protocol, user context, timestamp)
- [ ] DNS query anomalies (queried domain, source system, response, timestamp)
- [ ] Network device configuration changes (device identifier, configuration modified, administrator, timestamp)


**Common Gaps**:

- Firewall rules match logged but insufficient detail (missing source/destination)
- VPN connections logged but not disconnections
- Network segmentation not enforced or logged
- DNS queries not logged (privacy vs. security tradeoff)


---

# Evidence Collection

## Evidence Requirements

For each system assessed, collect evidence demonstrating logging configuration:

**Required Evidence Types**:

1. **Configuration Screenshots**

   - System logging configuration (syslog.conf, application.properties, registry, GUI settings)
   - Log forwarding configuration (SIEM agent config, syslog destination)
   - File/folder showing where logs are stored


2. **Sample Log Entries**

   - Copy/paste or screenshot of sample log entry for each required event type
   - Verify log contains required fields (timestamp, user, action, outcome per ISMS-POL-A.8.15, Section 2.1)


3. **System Owner Confirmation**

   - Email or documented confirmation from System Owner verifying logging configuration
   - System Owner signs Sheet 13 (Approval) for their systems


4. **Vendor Documentation**

   - Excerpts from vendor documentation showing logging capabilities
   - Vendor support confirmation for any capability questions


5. **SIEM Integration Evidence**

   - Screenshot from SIEM showing log source integrated and logs arriving
   - SIEM parser configuration for the log format


## Evidence Register (Sheet 11)

All evidence cataloged in Sheet 11 (Evidence_Register) with:

- Evidence ID (auto-increment: EVD-001, EVD-002, etc.)
- Related System ID(s)
- Evidence Type (Configuration Screenshot, Sample Log, Owner Confirmation, Vendor Doc, SIEM Screenshot, Other)
- Description
- File Location (network path, SharePoint link, email reference)
- Collection Date
- Collected By


**Evidence Storage**:

- Store all evidence files in dedicated folder: `[Assessment_Folder]/Evidence/A.8.15.1/`
- Use consistent naming: `EVD-001_PROD-WEB-01_Config_Screenshot.png`


## Evidence Quality Criteria

**Acceptable Evidence**:

- Clear, readable screenshots with timestamps
- Complete configuration files (not excerpts that might omit relevant settings)
- Signed/dated confirmations from System Owners
- Official vendor documentation (not forum posts or blogs)


**Insufficient Evidence**:

- Blurry or illegible screenshots
- Undated or unsigned confirmations
- Vendor documentation not specific to product version in use
- "Trust me" statements without supporting documentation


---

# Common Pitfalls

## Inventory Completeness Issues

**Pitfall**: Missing systems from inventory (shadow IT, forgotten test systems, cloud services)

**Impact**: Blind spots in logging coverage, audit findings, undetected security incidents

**Prevention**:

- Cross-reference multiple sources (CMDB, network scans, cloud subscription lists, billing records)
- Interview department heads about departmental systems
- Review firewall logs for systems making outbound connections not in inventory
- Conduct network discovery scans to identify unknown devices


## Classification Errors

**Pitfall**: Incorrect data classification or system criticality assignment leading to insufficient logging

**Example**: Development system classified as "Low" but contains production data copy

**Impact**: Inadequate logging for actual risk, compliance gaps

**Prevention**:

- Review data classification with System Owners and Data Owners
- Challenge assumptions (e.g., "test system" that accesses production APIs)
- Verify with Business Impact Analysis (BIA) results if available


## "Logging is Enabled" But Insufficient Detail

**Pitfall**: System Owner confirms "logging is on" but doesn't log all required event types

**Example**: Windows Server logging authentication but not privilege escalation or access to sensitive files

**Impact**: False compliance status, gaps discovered during incident investigation

**Prevention**:

- Don't accept generic "yes logging is configured" responses
- Request specific evidence for each required event type
- Sample logs to verify required fields present


## Local Logs Only (Not Centralized)

**Pitfall**: Logs generated but only stored locally, not forwarded to SIEM

**Impact**: Logs can be tampered with or deleted by attacker, log analysis difficult without centralization

**Prevention**:

- Verify log forwarding configuration, not just log generation
- Check SIEM to confirm logs actually arriving
- Document systems with local-only logs as gaps requiring remediation


## Default Logging Levels (Insufficient)

**Pitfall**: Relying on vendor default logging settings which are often minimal

**Example**: Application logs only ERRORs by default, not WARNINGs or INFO-level security events

**Impact**: Security-relevant events not logged, compliance gaps

**Prevention**:

- Review vendor documentation for available logging options
- Configure logging to capture all required events per ISMS-POL-A.8.15, Section 2.1
- Test logging configuration by triggering events and verifying they appear in logs


## Cloud Services Assumptions

**Pitfall**: Assuming cloud services "automatically log everything" without verification

**Example**: Microsoft 365 audit logging not enabled by default for all workloads

**Impact**: No logs for cloud service activities, compliance violation, investigation impossible

**Prevention**:

- Verify audit logging explicitly enabled for each cloud service
- Review cloud provider logging capabilities (may require premium tier)
- Test log export/forwarding from cloud service to SIEM


## Encrypted Traffic Blindness

**Pitfall**: HTTPS/TLS traffic not inspected, no application-layer logging

**Impact**: Cannot detect malware download, data exfiltration, or command-and-control traffic in encrypted channels

**Prevention**:

- Deploy TLS inspection where appropriate (consider privacy implications per ISMS-POL-A.8.15, Section 2.5)
- At minimum, log TLS handshake metadata (certificate, TLS version, cipher suite)
- For web proxies/gateways, ensure application-layer visibility


## Decommissioned Systems Still in Inventory

**Pitfall**: Assessment includes systems that have been decommissioned, wasting effort

**Impact**: Assessment accuracy reduced, effort wasted on non-existent systems

**Prevention**:

- Verify system operational status before assessing
- Establish process for removing decommissioned systems from inventory
- Quarterly inventory reconciliation against active systems


## Inconsistent Assessment Across Similar Systems

**Pitfall**: Different assessors evaluate similar systems differently

**Example**: One assessor marks web server logging as "Compliant", another marks identical configuration as "Partial"

**Impact**: Assessment unreliable, inconsistent remediation priorities

**Prevention**:

- Conduct assessor calibration session before beginning assessment
- Use consistent examples and test cases
- Peer review subset of assessments for consistency
- Document decision rationale in Notes column


## Ignoring Legacy/End-of-Life Systems

**Pitfall**: "We know it's old and can't log properly, so we'll skip it"

**Impact**: Known gaps not documented, audit findings, potential compliance violation

**Prevention**:

- Document ALL systems including legacy/EOL
- Mark as non-compliant with justification and compensating controls
- Include in remediation plan (upgrade, replace, or accept risk with approval)


---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] **All systems inventoried**: Cross-referenced against CMDB, network scans, cloud subscriptions
- [ ] **All sheets completed**: No blank sections in Sheets 2-11
- [ ] **All required fields filled**: No "TBD" or placeholder text (except in Notes where appropriate)
- [ ] **Evidence attached**: Every non-compliant finding has evidence reference (Sheet 11 Evidence_Register)


## Accuracy

- [ ] **System classifications verified**: Data classification and criticality confirmed with System Owners
- [ ] **Logging requirements correct**: Requirements match ISMS-POL-A.8.15, Section 2.1 and Annex A
- [ ] **Configuration verification**: At least 10% of systems sampled with direct configuration review
- [ ] **Log samples validated**: Sample logs contain required fields per ISMS-POL-A.8.15, Section 2.1 (timestamp, user, action, outcome)


## Compliance Scoring

- [ ] **Formulas correct**: Compliance percentages calculate correctly (spot-check 5 systems manually)
- [ ] **Scoring methodology**: Documented in Instructions sheet
- [ ] **Partial compliance**: Systems marked "Partial" have clear explanation of what's missing


## Gap Analysis

- [ ] **All gaps identified**: Every "Non-Compliant" or "Partial Compliance" has corresponding gap in Sheet 10 (Gap_Analysis)
- [ ] **Gaps prioritized**: Severity assigned based on risk (Critical, High, Medium, Low)
- [ ] **Remediation feasible**: Proposed actions are technically achievable
- [ ] **Owners assigned**: Every gap has responsible owner and realistic timeline


## Evidence Quality

- [ ] **Evidence complete**: All evidence files present in Evidence folder
- [ ] **Evidence linkage**: Evidence Register (Sheet 11) correctly references evidence files
- [ ] **Evidence readable**: Screenshots clear, documents legible, confirmations signed/dated
- [ ] **Evidence current**: Evidence collected within assessment period (not stale/outdated)


## Documentation

- [ ] **Notes explain exceptions**: Any unusual configurations or decisions documented in Notes columns
- [ ] **Assumptions documented**: Any assumptions made during assessment clearly stated
- [ ] **Methodology documented**: Assessment approach described in Instructions sheet
- [ ] **Limitations noted**: Any limitations or scope exclusions clearly stated


## Review Readiness

- [ ] **System Owner review**: Owners have reviewed and confirmed accuracy for their systems
- [ ] **IT Operations review**: IT Ops Manager validated inventory completeness
- [ ] **Security Team review**: InfoSec Manager spot-checked compliance assessments
- [ ] **Approval signatures**: All approval levels documented in Sheet 13


---

# Review & Approval

## Three-Level Approval Process

**Level 1: System Owner Confirmation**

- **Who**: Each System Owner reviews assessment for their systems
- **What**: Verify logging configuration accurately documented
- **Outcome**: System Owner signs Sheet 13 confirming accuracy
- **Timeline**: 5 business days for review


**Level 2: IT Operations Manager Approval**

- **Who**: IT Operations Manager
- **What**: Validate overall inventory completeness, technical accuracy
- **Outcome**: IT Ops Manager approves assessment and certifies inventory complete
- **Timeline**: 3 business days after System Owner confirmations


**Level 3: Information Security Manager / CISO Approval**

- **Who**: Information Security Manager or CISO
- **What**: Review compliance scores, gap analysis, remediation plan
- **Outcome**: InfoSec Manager/CISO approves assessment and authorizes remediation actions
- **Timeline**: 5 business days after IT Ops approval


## Approval Criteria

**Assessment approved if**:

- All sections complete with no placeholder text
- Compliance scoring methodology documented and calculations correct
- Gap analysis comprehensive with prioritization and remediation plans
- Evidence sufficient to support findings
- System Owners and IT Operations confirmed accuracy


**Assessment requires rework if**:

- Significant systems missing from inventory
- Logging requirements misapplied (not matching ISMS-POL-A.8.15 requirements)
- Insufficient evidence for key findings
- Gaps identified but no remediation plan
- Quality checklist items not satisfied


## Post-Approval Actions

1. **Publish Final Assessment**: Distribute approved workbook to stakeholders (CISO, InfoSec Manager, IT Ops, System Owners)
2. **Initiate Remediation**: Create project plan for closing identified gaps
3. **Track Progress**: Quarterly updates on gap closure progress
4. **Schedule Next Assessment**: Annual full assessment, quarterly updates for new systems

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook Developers (Python/Excel Script Maintainers)

---

# Workbook Structure Overview

| Sheet # | Sheet Name | Purpose | Row Estimate |
|---------|------------|---------|--------------|
| 1 | Instructions_Legend | Usage guide, color codes, dropdown values, scoring methodology | ~60 |
| 2 | System_Inventory | Complete system catalog with attributes | ~300-1000+ |
| 3 | Event_Requirements_Summary | Required events per system based on policy | ~300-1000+ |
| 4 | Authentication_Events | Authentication event logging verification | ~300-1000+ |
| 5 | Authorization_Events | Authorization event logging verification | ~300-1000+ |
| 6 | Administrative_Actions | Administrative action logging verification | ~300-1000+ |
| 7 | Security_Events | Security event logging verification | ~300-1000+ |
| 8 | System_Events | System event logging verification | ~300-1000+ |
| 9 | Network_Events | Network event logging verification | ~300-1000+ |
| 10 | Application_Events | Application event logging verification | ~300-1000+ |
| 11 | Gap_Analysis | Consolidated gaps requiring remediation | ~50-200 |
| 12 | Evidence_Register | Evidence catalog and linkage | ~100-500 |
| 13 | Approval_Sign_Off | Three-level approval workflow | ~30 |

**Total Sheets**: 13  
**Estimated Total Rows**: ~2,500-8,000+ (depends on environment size)

**Workbook Filename Format**: `ISMS-IMP-A.8.15.1_Log_Source_Inventory_YYYYMMDD.xlsx`

---

# Sheet 1: Instructions_Legend

## Header Section

**Cells A1:O1** (Merged):

- **Text**: "ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment"
- **Font**: Calibri 20pt, Bold, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle
- **Row Height**: 40px


**Cells A2:O2** (Merged):

- **Text**: "ISO/IEC 27001:2022 - Control A.8.15: Logging"
- **Font**: Calibri 14pt, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle
- **Row Height**: 25px


## Document Information Block (Rows 4-14)

```
| Field (Col A) | Value (Col B-D, merged) | Styling |
|---------------|-------------------------|---------|
| Document ID | ISMS-IMP-A.8.15.1 | Bold label, normal value |
| Assessment Area | Log Source Inventory & Event Logging Completeness | Normal |
| Related Policy | ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements) | Blue hyperlink style |
| Version | 2.0 | Normal |
| Assessment Date | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Completed By | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Organization | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Review Cycle | Annual (full), Quarterly (updates) | Normal |
```

## Status Dropdown Values (Rows 16-23)

**Table Headers** (Row 16): Status Value | Color | Meaning

- **Font**: Bold, Dark Blue (#003366)
- **Fill**: Light Blue (#BDD7EE)


**Data Rows** (17-22):
| Status | Fill Color | Text | Meaning |
|--------|------------|------|---------|
| Implemented | Green (#C6EFCE) | Dark Green (#006100) | Fully configured and verified |
| Partial | Yellow (#FFEB9C) | Dark Yellow (#9C5700) | Partially configured, gaps exist |
| Planned | Blue (#BDD7EE) | Dark Blue (#003366) | Scheduled, not yet implemented |
| Not Implemented | Red (#FFC7CE) | Dark Red (#9C0006) | Not configured or no capability |
| N/A | Gray (#D9D9D9) | Black | Not applicable to this system |

## Compliance Status Values (Rows 25-29)

| Status | Fill Color | Meaning |
|--------|------------|---------|
| Compliant | Green (#C6EFCE) | Meets all policy requirements |
| Partial Compliance | Yellow (#FFEB9C) | Meets some requirements, gaps exist |
| Non-Compliant | Red (#FFC7CE) | Does not meet requirements |

## Priority Values (for Gap Analysis) (Rows 31-35)

| Priority | Fill Color | Meaning |
|----------|------------|---------|
| Critical | Dark Red (#9C0006) white text | Immediate risk, address within 30 days |
| High | Red (#FF0000) | Significant risk, address within 90 days |
| Medium | Yellow (#FFEB9C) | Moderate risk, address within 180 days |
| Low | Blue (#BDD7EE) | Minor risk, address within 12 months |

## Instructions Summary (Rows 37-55)

**Title** (Row 37): "How to Use This Workbook"

- **Font**: Calibri 14pt, Bold, Dark Blue


**Steps** (Rows 38-55):
1. Start with Sheet 2 (System Inventory): Document all systems in environment
2. Complete Sheet 3 (Event Requirements): Determine what each system must log
3. Verify logging for each event category (Sheets 4-9)
4. Identify gaps in Sheet 10 (Gap_Analysis)
5. Collect evidence in Sheet 11 (Evidence_Register)
6. Review Summary Dashboard (Sheet 12)
7. Obtain approvals in Sheet 13 (Approval_Sign_Off)

**Key Points**:

- Use dropdown menus for consistent data entry
- Yellow-highlighted cells require user input
- Gray-shaded cells auto-calculate (do not edit formulas)
- Link evidence files for all non-compliant findings
- Review quality checklist before submission


## Scoring Methodology (Rows 57-60)

**Compliance Score Calculation**:

- **Compliant systems**: 100% weight
- **Partial compliance**: 50% weight
- **Non-compliant**: 0% weight
- **Formula**: `(Compliant_Count + 0.5 * Partial_Count) / Total_Applicable_Systems * 100`


---

# Sheet 2: System_Inventory

## Purpose
Complete catalog of all systems that should be logging per ISMS-POL-A.8.15, Section 1.4 (Scope).

## Column Specifications

| Col | Column Name | Width | Data Type | Data Validation | Conditional Formatting |
|-----|-------------|-------|-----------|-----------------|------------------------|
| A | System ID | 12 | Text | None (auto-increment SYS-001) | None |
| B | System Name | 25 | Text | None | None |
| C | System Type | 20 | Dropdown | Server, Application, Network Device, Security Tool, Database, Cloud Service, Authentication System, Other | None |
| D | System Owner | 20 | Text | Email format validation (optional) | None |
| E | Business Function | 25 | Text | None | None |
| F | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted | Color: Public=Green, Internal=Yellow, Confidential=Orange, Restricted=Red |
| G | System Criticality | 15 | Dropdown | Critical, High, Standard, Low | Color: Critical=Red, High=Orange, Standard=Yellow, Low=Green |
| H | Deployment Model | 18 | Dropdown | On-Premises, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS), Hybrid, Third-Party Hosted | None |
| I | OS / Platform | 20 | Text | None | None |
| J | Vendor / Manufacturer | 20 | Text | None | None |
| K | Logging Capability | 15 | Dropdown | Yes, Partial, No, Unknown | Color: Yes=Green, Partial=Yellow, No/Unknown=Red |
| L | Log Forwarding Status | 18 | Dropdown | Implemented, Partial, Planned, Not Implemented, N/A | Status color scheme |
| M | SIEM Integration | 15 | Dropdown | Yes, No, Planned, N/A | Yes=Green, No=Red, Planned=Yellow |
| N | Notes | 30 | Text | None | None |

**Header Row** (Row 1):

- **Font**: Bold, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle, Wrap Text
- **Row Height**: 45px
- **Freeze Panes**: Row 2 (header always visible)


**Data Rows** (Starting Row 2):

- **Row Height**: Auto (minimum 20px)
- **Borders**: Light gray (#D9D9D9) grid lines
- **Alternating Row Colors**: White / Light Gray (#F2F2F2) for readability


**Auto-Increment Formula** (Column A, starting A2):
```excel
="SYS-" & TEXT(ROW()-1, "000")
```

**Data Validation Examples**:

Column C (System Type):

- List: `Server, Application, Network Device, Security Tool, Database, Cloud Service, Authentication System, Other`
- Input Message: "Select the primary system type"
- Error Alert: "Please select a valid system type from the list"


Column F (Data Classification):

- List: `Public, Internal, Confidential, Restricted`
- Input Message: "Per organizational data classification policy"


Column G (System Criticality):

- List: `Critical, High, Standard, Low`
- Input Message: "Critical = Major business disruption if unavailable; High = Significant impact; Standard = Manageable impact; Low = Minimal impact"


**Conditional Formatting Rules**:

Data Classification (Column F):
```excel
Rule 1: If F2="Public" then Fill=Green (#C6EFCE)
Rule 2: If F2="Internal" then Fill=Yellow (#FFEB9C)
Rule 3: If F2="Confidential" then Fill=Orange (#FFC000)
Rule 4: If F2="Restricted" then Fill=Red (#FFC7CE)
```

System Criticality (Column G):
```excel
Rule 1: If G2="Critical" then Fill=Red (#FFC7CE)
Rule 2: If G2="High" then Fill=Orange (#FFC000)
Rule 3: If G2="Standard" then Fill=Yellow (#FFEB9C)
Rule 4: If G2="Low" then Fill=Green (#C6EFCE)
```

Logging Capability (Column K):
```excel
Rule 1: If K2="Yes" then Fill=Green (#C6EFCE)
Rule 2: If K2="Partial" then Fill=Yellow (#FFEB9C)
Rule 3: If K2 IN ("No","Unknown") then Fill=Red (#FFC7CE)
```

---

# Sheet 3: Event_Requirements_Summary

## Purpose
Determines WHAT events each system must log based on system attributes and policy requirements (ISMS-POL-A.8.15, Section 2.1 + Annex A).

## Column Specifications

| Col | Column Name | Width | Data Type | Formula / Validation | Notes |
|-----|-------------|-------|-----------|---------------------|-------|
| A | System ID | 12 | Reference | `='System_Inventory'!A2` | External reference to Sheet 2 |
| B | System Name | 25 | Reference | `='System_Inventory'!B2` | External reference |
| C | System Type | 20 | Reference | `='System_Inventory'!C2` | External reference |
| D | Data Classification | 18 | Reference | `='System_Inventory'!F2` | External reference |
| E | System Criticality | 15 | Reference | `='System_Inventory'!G2` | External reference |
| F | Required Event Categories | 30 | Calculated | See formula below | Comma-separated list |
| G | Authentication Events? | 15 | Calculated | See formula | Yes (All), Yes (Failures Only), No |
| H | Authorization Events? | 15 | Calculated | See formula | Yes, No |
| I | Administrative Actions? | 15 | Calculated | Yes always | Yes, No |
| J | Security Events? | 15 | Calculated | Yes always | Yes, No |
| K | System Events? | 15 | Calculated | See formula | Yes, No |
| L | Network Events? | 15 | Calculated | See formula | Yes, No, N/A |
| M | Application Events? | 15 | Calculated | See formula | Yes, No, N/A |
| N | Retention (Online) | 12 | Calculated | See formula | Months |
| O | Retention (Archive) | 12 | Calculated | See formula | Years |
| P | Special Regulatory? | 18 | Manual Input | Dropdown | None, PCI DSS, HIPAA, SOX, GDPR/nDSG, Multiple |
| Q | Rationale | 40 | Calculated | See formula | Auto-generated explanation |

**Formula Examples**:

Column F (Required Event Categories):
```excel
=IF(OR(E2="Critical", D2="Restricted"), 
  "Authentication, Authorization, Administrative, Security, System, Network, Application",
  IF(OR(E2="High", D2="Confidential"),
    "Authentication, Authorization, Administrative, Security, System, Application",
    IF(E2="Standard",
      "Authentication, Administrative, Security",
      "Authentication (Failures), Administrative, Critical Security Events"
    )
  )
)
```

Column G (Authentication Events Required):
```excel
=IF(OR(E2="Critical", E2="High", E2="Standard", D2<>"Public"), 
  "Yes (All)", 
  "Yes (Failures Only)"
)
```

Column H (Authorization Events Required):
```excel
=IF(OR(E2="Critical", E2="High", D2="Restricted", D2="Confidential"), "Yes", "No")
```

Column N (Retention Online - Months):
```excel
=IF(OR(E2="Critical", D2="Restricted", D2="Confidential"), 12,
  IF(E2="High", 6, 3)
)
```

Column O (Retention Archive - Years):
```excel
=IF(OR(E2="Critical", D2="Restricted", D2="Confidential", P2<>"None"), 7,
  IF(E2="High", 1, 0.5)
)
```

Column Q (Rationale):
```excel
=IF(E2="Critical",
  "Critical system requires comprehensive logging per ISMS-POL-A.8.15, Annex A.1",
  IF(D2="Restricted",
    "Restricted data requires comprehensive logging per ISMS-POL-A.8.15, Annex A.1",
    IF(OR(E2="High", D2="Confidential"),
      "High-value system/Confidential data requires detailed logging per ISMS-POL-A.8.15, Section 2.1",
      "Standard logging requirements per ISMS-POL-A.8.15, Section 2.1"
    )
  )
)
```

**Cell Protection**:

- Columns A-O: **LOCKED** (formulas protected)
- Column P: **UNLOCKED** (user input allowed)
- Column Q: **LOCKED** (calculated)


---

# Sheets 4-9: Event Category Verification

These sheets follow identical structure. Only column names and specific event checklists differ.

## Common Column Structure

| Col | Column Name | Width | Data Type | Source / Validation |
|-----|-------------|-------|-----------|---------------------|
| A | System ID | 12 | Reference | From Sheet 2 |
| B | System Name | 25 | Reference | From Sheet 2 |
| C | Logging Required? | 15 | Reference | From Sheet 3 (appropriate column) |
| D | Logging Status | 15 | Dropdown | Implemented, Partial, Not Implemented, N/A |
| E | Log Format | 18 | Dropdown | Syslog, CEF, JSON, Windows Event Log, Proprietary, Other |
| F | Log Location | 18 | Dropdown | Local Only, SIEM, Cloud Service, Both (Local+SIEM) |
| G | Specific Events Logged | 40 | Checklist Text | Multi-line text with checkbox ASCII: [X] or [ ] |
| H | Sample Log Entry | 40 | Text | Copy/paste of actual log entry |
| I | Verification Method | 20 | Dropdown | Configuration Review, Log Sample, Owner Confirmation, Documentation Review |
| J | Verification Date | 12 | Date | Date picker |
| K | Verified By | 18 | Text | Name or email |
| L | Compliance Status | 15 | Dropdown | Compliant, Non-Compliant, Partial Compliance |
| M | Gap Description | 30 | Text | Required if L="Non-Compliant" or "Partial" |
| N | Evidence Reference | 15 | Text | Link to Sheet 11 (e.g., "EVD-045") |
| O | Notes | 25 | Text | Additional context |

**Conditional Formatting** (Column L - Compliance Status):
```excel
Rule 1: If L2="Compliant" then Fill=Green (#C6EFCE)
Rule 2: If L2="Partial Compliance" then Fill=Yellow (#FFEB9C)
Rule 3: If L2="Non-Compliant" then Fill=Red (#FFC7CE)
```

**Data Validation** (Column G - Specific Events):

- Type: Text (multi-line allowed)
- Input Message: "Check all events that are logged. Use [X] for yes, [ ] for no. See ISMS-POL-A.8.15, Section 2.1 for required events."


**Formula for Column C (Example - Sheet 4 Authentication Events)**:
```excel
='Event_Requirements_Summary'!G2
```
(References appropriate column from Sheet 3 depending on event category)

---

## Sheet 4: Authentication_Events - Specific Details

**Column G Sample Content** (Specific Events Logged):
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Successful login attempts (user ID, timestamp, source IP, method)
[X] Failed login attempts (user ID, timestamp, source IP, failure reason)
[X] Logout events (user ID, session duration, timestamp)
[ ] Account lockouts (user ID, lockout reason, timestamp)
[X] Password changes/resets (user ID, timestamp, initiated by)
[ ] Multi-factor authentication events (MFA success/failure, method, timestamp)
```

---

## Sheet 5: Authorization_Events - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Access to sensitive data (user, classification, action, timestamp)
[X] Privilege escalation (user, escalated privileges, justification, timestamp)
[ ] Access control changes (modified permissions, affected resources, initiator)
[X] File/object access for classified data (user, resource, action, outcome)
[X] Denied access attempts (user, attempted resource, denial reason, timestamp)
```

---

## Sheet 6: Administrative_Actions - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] System configuration changes (parameters, previous/new values, admin, timestamp)
[X] User account creation/modification/deletion (affected user, changes, admin)
[X] Privilege grants/revocations (affected user, privilege type, admin, timestamp)
[ ] Security policy changes (policy modified, details, admin, approval ref)
[X] Installation/removal of software/services (package, version, admin, timestamp)
[ ] Firmware/system updates (system ID, update applied, admin, timestamp)
```

---

## Sheet 7: Security_Events - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Malware detection/prevention (malware type, system, action, timestamp)
[X] Intrusion detection/prevention alerts (alert type, source/dest, action)
[X] Firewall blocks/rule violations (source/dest, protocol/port, rule violated)
[ ] Data loss prevention (DLP) events (data type, egress channel, action)
[ ] Encryption/decryption operations (user, operation type, data classification)
[X] Certificate validation failures (certificate subject, validation error)
[ ] Security tool configuration changes (tool name, config modified, admin)
```

---

## Sheet 8: Application_Database - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Application errors/exceptions (app name, error type, error details, timestamp)
[X] Database transactions with sensitive data (user, table/record, operation)
[X] API authentication/authorization (API endpoint, user/service account, outcome)
[ ] Data export operations (user, data scope, export format, destination)
[X] Application-level access control decisions (user, requested resource, decision)
```

---

## Sheet 9: Network_Device_Logging - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Firewall rule matches for security traffic (source/dest, rule, action)
[X] VPN connections/disconnections (user ID, VPN gateway, connection duration)
[ ] Network segmentation traversals (source/dest segment, protocol, user context)
[ ] DNS query anomalies (queried domain, source system, response, timestamp)
[X] Network device configuration changes (device ID, config modified, admin)
```

---

# Sheet 10: Gap_Analysis

## Purpose
Consolidated list of all logging gaps requiring remediation.

## Column Specifications

| Col | Column Name | Width | Data Type | Data Validation |
|-----|-------------|-------|-----------|-----------------|
| A | Gap ID | 10 | Text | Auto-increment (GAP-001) |
| B | System ID | 12 | Reference | From System_Inventory |
| C | System Name | 25 | Reference | From System_Inventory |
| D | Gap Category | 20 | Dropdown | Missing Log Source, Incomplete Events, No Log Forwarding, Retention Non-Compliance, Format Issues, Other |
| E | Gap Description | 40 | Text | Detailed description of the gap |
| F | Policy Reference | 25 | Text | E.g., "ISMS-POL-A.8.15, Section 2.1 - Authentication Events" |
| G | Risk Severity | 12 | Dropdown | Critical, High, Medium, Low |
| H | Business Impact | 30 | Text | What is the impact if not remediated? |
| I | Proposed Remediation | 35 | Text | Actionable remediation steps |
| J | Responsible Owner | 18 | Text | Name or email of person responsible |
| K | Target Date | 12 | Date | Remediation deadline |
| L | Status | 15 | Dropdown | Open, In Progress, Resolved, Accepted Risk |
| M | Evidence Reference | 15 | Text | Link to Sheet 11 (e.g., "EVD-087") |
| N | Notes | 25 | Text | Additional context |

**Auto-Increment Formula** (Column A):
```excel
="GAP-" & TEXT(ROW()-1, "000")
```

**Conditional Formatting** (Column G - Risk Severity):
```excel
Rule 1: If G2="Critical" then Fill=Dark Red (#9C0006), Font=White
Rule 2: If G2="High" then Fill=Red (#FF0000)
Rule 3: If G2="Medium" then Fill=Yellow (#FFEB9C)
Rule 4: If G2="Low" then Fill=Blue (#BDD7EE)
```

**Conditional Formatting** (Column L - Status):
```excel
Rule 1: If L2="Resolved" then Fill=Green (#C6EFCE)
Rule 2: If L2="In Progress" then Fill=Yellow (#FFEB9C)
Rule 3: If L2="Open" then Fill=Red (#FFC7CE)
Rule 4: If L2="Accepted Risk" then Fill=Gray (#D9D9D9)
```

**Data Validation** (Column G - Risk Severity):

- List: `Critical, High, Medium, Low`
- Input Message: "Critical = Immediate risk (30 days); High = Significant risk (90 days); Medium = Moderate risk (180 days); Low = Minor risk (12 months)"


**Target Date Auto-Suggestion** (Column K - based on severity):
```excel
=IF(G2="Critical", TODAY()+30,
  IF(G2="High", TODAY()+90,
    IF(G2="Medium", TODAY()+180,
      IF(G2="Low", TODAY()+365, ""))))
```
(User can override this suggested date)

---

# Sheet 11: Evidence_Register

## Purpose
Catalog all evidence files supporting assessment findings.

## Column Specifications

| Col | Column Name | Width | Data Type | Notes |
|-----|-------------|-------|-----------|-------|
| A | Evidence ID | 12 | Text | Auto-increment (EVD-001) |
| B | Related System ID(s) | 20 | Text | Comma-separated list if evidence covers multiple systems |
| C | Evidence Type | 20 | Dropdown | Configuration Screenshot, Sample Log, Owner Confirmation, Vendor Doc, SIEM Screenshot, Other |
| D | Description | 40 | Text | What does this evidence show? |
| E | File Location | 50 | Hyperlink | Network path, SharePoint link, or "Email dated DD.MM.YYYY" |
| F | Collection Date | 12 | Date | When was evidence collected? |
| G | Collected By | 18 | Text | Who collected this evidence? |
| H | Notes | 25 | Text | Additional context |

**Auto-Increment Formula** (Column A):
```excel
="EVD-" & TEXT(ROW()-1, "000")
```

**Hyperlink Format** (Column E):
```excel
=HYPERLINK("\\fileserver\share\A.8.15.1\Evidence\" & A2 & "_filename.png", "Link to Evidence")
```

**Conditional Formatting** (Column F - highlight old evidence):
```excel
Rule 1: If F2 < TODAY()-90 then Fill=Orange (#FFC000)
```
(Evidence older than 90 days may be stale)

---

# Sheet 12: Summary_Dashboard

## Purpose
Overall compliance metrics and summary view for management review.

## Structure

**Title Block** (Rows 1-3):
- **Row 1**: "Log Source Inventory - Summary Dashboard"
- **Row 2**: "ISMS-IMP-A.8.15.1"
- **Row 3**: Assessment Date: [Auto-populated]

**Compliance Summary** (Rows 5-12):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Systems Assessed | [Count from Sheet 2] | - | - |
| Fully Compliant Systems | [Count] | 100% | [%] |
| Partially Compliant | [Count] | 0% | [%] |
| Non-Compliant | [Count] | 0% | [%] |
| Open Gaps | [Count from Sheet 10] | 0 | - |
| Critical Gaps | [Count] | 0 | - |

**By Event Category** (Rows 14-22):

| Event Category | Compliant | Partial | Non-Compliant |
|----------------|-----------|---------|---------------|
| Authentication (Sheet 4) | [Count] | [Count] | [Count] |
| Authorization (Sheet 5) | [Count] | [Count] | [Count] |
| Administrative (Sheet 6) | [Count] | [Count] | [Count] |
| Security (Sheet 7) | [Count] | [Count] | [Count] |
| Application/Database (Sheet 8) | [Count] | [Count] | [Count] |
| Network (Sheet 9) | [Count] | [Count] | [Count] |

**Formulas**:
```excel
Total Systems: =COUNTA('System_Inventory'!A:A)-1
Fully Compliant: =COUNTIF('Gap_Analysis'!L:L,"Compliant")
Open Gaps: =COUNTA('Gap_Analysis'!A:A)-1
Critical Gaps: =COUNTIF('Gap_Analysis'!G:G,"Critical")
```

**Conditional Formatting**:
- Overall compliance >= 90%: Green
- Overall compliance 70-89%: Yellow
- Overall compliance < 70%: Red

---

# Sheet 13: Approval_Sign_Off

## Purpose
Three-level approval workflow for assessment validation.

## Structure

**Title Block** (Rows 1-3):

- **Row 1**: "Assessment Approval & Sign-Off"
- **Row 2**: "ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment"
- **Row 3**: "Version 1.0"


**Approval Table** (Rows 5-15):

| Col A | Col B | Col C | Col D | Col E |
|-------|-------|-------|-------|-------|
| **Approval Level** | **Role** | **Name** | **Signature / Date** | **Comments** |
| Level 1 | System Owners | [Multiple rows] | [Date] | [Optional feedback] |
| Level 2 | IT Operations Manager | [Name] | [Date] | Inventory completeness certified |
| Level 3 | Information Security Manager / CISO | [Name] | [Date] | Assessment approved, remediation authorized |

**System Owner Approval Rows** (Rows 6-10, expandable):

- One row per System Owner
- Column B: System Owner Name
- Column C: Systems Owned (list)
- Column D: Signature/Date
- Column E: Confirmation statement: "I confirm the logging assessment for my systems is accurate"


**IT Operations Manager Approval** (Row 12):

- Column B: IT Operations Manager
- Column C: [Name]
- Column D: [Date]
- Column E: "I certify the system inventory is complete and logging configurations are technically accurate"


**InfoSec Manager / CISO Approval** (Row 14):

- Column B: Information Security Manager / CISO
- Column C: [Name]
- Column D: [Date]
- Column E: "I approve this assessment and authorize the remediation plan per Sheet 10 (Gap_Analysis)"


**Conditional Formatting** (Approval status):
```excel
If signature/date cell is blank: Fill=Red (pending approval)
If signature/date cell has content: Fill=Green (approved)
```

---

# Python Script Usage Notes

## Script Name
`generate_a815_1_log_source_inventory.py`

## Purpose
Generates the ISMS-IMP-A.8.15.1 Excel workbook with all 13 sheets, data validation, conditional formatting, formulas, and cell protection.

## Key Customization Points (marked with `# CUSTOMIZE:` in script)

1. **Sheet Names**: If organizational naming conventions differ
2. **Dropdown Options**: If additional status values needed beyond standard set
3. **Data Validation Rules**: If custom compliance criteria required
4. **Conditional Formatting Thresholds**: If different risk color coding desired
5. **Formula Logic**: If organizational policy has different criticality/classification definitions
6. **Cell Protection**: If different cells need to be unlocked for user input

## Quality Assurance

**Validation Script**: `excel_sanity_check_a815_1.py`

- Validates sheet structure matches this specification
- Checks all data validation rules applied correctly
- Verifies conditional formatting ranges accurate
- Tests formula calculations
- Reports discrepancies between generated workbook and specification


## Version Control

**Workbook Versioning**:

- Filename format: `ISMS-IMP-A.8.15.1_Log_Source_Inventory_YYYYMMDD.xlsx`
- Version tracking in Instructions_Legend sheet (Document Control block)
- Document Control section updated with each revision


**Change Log**:

- v1.0: Initial workbook structure with consolidated policy references to ISMS-POL-A.8.15


**Compatibility**:

- Workbooks can be opened in Excel 2016+
- Requires openpyxl 3.0+ for Python generation


---

# Integration Points

## External References

**From Other Assessment Workbooks**:

- ISMS-IMP-A.8.15.2 (Log Collection & Centralization) references this workbook's System_Inventory sheet for log source list
- ISMS-IMP-A.8.15.5 (Compliance Dashboard) references this workbook's compliance scores and gap counts


**To Policy Documents**:

- All "Related Policy" references point to consolidated ISMS-POL-A.8.15-Logging.md
- Specific section references: Section 2.1 (Event Logging Requirements), Annex A (Logging Decision Matrix)


**To Technical Reference**:

- ISMS-REF-A.8.15 (Logging Standards Reference) provides detailed log format specifications referenced in this assessment


## Data Flow

```
System Inventory (Sheet 2)
  |
  v
Event Requirements (Sheet 3) - Determines what to log based on system attributes
  |
  v
Event Category Verification (Sheets 4-9) - Verifies actual configuration
  |
  v
Gap_Analysis (Sheet 10) - Consolidates non-compliance findings
  |
  v
Evidence_Register (Sheet 11) - Links supporting evidence
  |
  v
Summary_Dashboard (Sheet 12) - Overall compliance metrics
  |
  v
Approval_Sign_Off (Sheet 13) - Three-level sign-off
  |
  v
External: Dashboard Consolidation (IMP-A.8.15.5) - Aggregates this + other assessments
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Document Assembly Complete**: ISMS-IMP-A.8.15.1 consists of Part I (User Completion Guide) + Part II (Technical Specification)

**Total Document Length**: ~1,600 lines (Part I: ~600 lines, Part II: ~1,000 lines)

**Quality Review**: All policy references updated to consolidated ISMS-POL-A.8.15-Logging.md (v1.0)

---

**END OF SPECIFICATION**

---

*"Once you stop learning, you start dying."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-01 -->
