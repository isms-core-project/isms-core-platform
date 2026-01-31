# ISMS-POL-A.8.15-S5.B
## Log Source Template

**Document ID**: ISMS-POL-A.8.15-S5.B  
**Title**: Log Source Template  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Log Administrator / System Owner | Initial template |

**Review Cycle**: As needed (template updates)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: Information Security Manager  
**Distribution**: System owners, log administrators, project managers

---

## B.1 Purpose

This template provides a standardized form for documenting and onboarding new log sources into the centralized log management system.

**Use this template when**:
- Deploying new systems, applications, or devices
- Onboarding existing systems to centralized logging
- Conducting log source inventory assessments
- Planning logging for new projects

---

## B.2 Log Source Information Form

### Section 1: System Identification

**Log Source Name**: ________________________________________  
(Unique identifier for this log source)

**System Type** (select one):
- [ ] Physical Server
- [ ] Virtual Server
- [ ] Cloud Instance (IaaS)
- [ ] Container
- [ ] Network Device (router, switch, firewall, load balancer)
- [ ] Security Appliance (IDS/IPS, web filter, email gateway)
- [ ] Application (web app, database, API)
- [ ] SaaS Application
- [ ] Other: ___________________

**Operating System / Platform**:
- [ ] Windows Server (version: _______)
- [ ] Linux (distribution: _____, version: _______)
- [ ] Unix (type: _______)
- [ ] Network OS (vendor: _____, version: _______)
- [ ] Cloud Platform (AWS, Azure, GCP, other: _______)
- [ ] Application Platform (vendor: _____, version: _______)
- [ ] Other: ___________________

**System Hostname / FQDN**: ________________________________________

**Primary IP Address**: ________________________________________

**Location** (physical or cloud region): ________________________________________

**Environment**:
- [ ] Production
- [ ] Staging / UAT
- [ ] Development
- [ ] Test

---

### Section 2: System Owner and Contacts

**System Owner**:
- Name: ________________________________________
- Email: ________________________________________
- Phone: ________________________________________
- Department: ________________________________________

**Technical Contact** (if different from owner):
- Name: ________________________________________
- Email: ________________________________________
- Phone: ________________________________________

**Backup Contact**:
- Name: ________________________________________
- Email: ________________________________________

---

### Section 3: Log Source Classification

**Data Classification** (highest classification of data processed by this system):
- [ ] Public
- [ ] Internal
- [ ] Confidential
- [ ] Restricted / Highly Confidential

**Regulatory Scope** (check all that apply):
- [ ] PCI DSS (payment card data)
- [ ] HIPAA (healthcare data)
- [ ] GDPR (EU personal data)
- [ ] FADP (Swiss personal data)
- [ ] SOX (financial reporting systems)
- [ ] DORA (financial ICT systems)
- [ ] NIS2 (critical infrastructure)
- [ ] None / Not applicable

**Business Criticality**:
- [ ] Critical (tier 1) - Business cannot operate without this system
- [ ] High (tier 2) - Major business impact if unavailable
- [ ] Medium (tier 3) - Moderate business impact
- [ ] Low (tier 4) - Minimal business impact

---

### Section 4: Logging Requirements

**Logging Priority** (based on classification, regulatory scope, criticality):
- [ ] P1 - Critical (must log all security events, high retention)
- [ ] P2 - High (must log security events, standard retention)
- [ ] P3 - Medium (should log security events, standard retention)
- [ ] P4 - Low (may log for operational purposes)

**Required Log Event Types** (check all that apply - see S2.1 for details):
- [ ] Authentication events (login, logout, failed attempts)
- [ ] Authorization events (access granted/denied)
- [ ] Administrative actions (config changes, user management)
- [ ] Security events (malware, intrusions, policy violations)
- [ ] Application events (transactions, errors, exceptions)
- [ ] System events (start/stop, errors, resource issues)
- [ ] Network events (connections, firewall blocks)
- [ ] Database events (queries, schema changes)

**Estimated Log Volume**:
- Events per day: __________________ (estimate)
- Data volume per day: __________________ MB/GB (estimate)

**Log Retention Period** (per S2.3):
- Hot storage: ______ months
- Warm storage: ______ months / years
- Cold storage: ______ years
- **Retention Justification**: _____________________________________________

---

### Section 5: Log Collection Configuration

**Log Format** (select one):
- [ ] Syslog (RFC 5424)
- [ ] Legacy Syslog (RFC 3164)
- [ ] Common Event Format (CEF)
- [ ] JSON
- [ ] Windows Event Log (EVTX)
- [ ] Vendor-specific: ___________________

**Log Transport Method**:
- [ ] Syslog over TLS (port 6514) - Preferred
- [ ] Syslog over TCP (port 601)
- [ ] Syslog over UDP (port 514) - Legacy only
- [ ] Log forwarder agent (Splunk, Fluentd, Logstash, etc.)
- [ ] API pull (cloud services)
- [ ] File collection (SFTP, SMB)
- [ ] Other: ___________________

**Log Forwarder / Agent**:
- [ ] None (native syslog)
- [ ] Splunk Universal Forwarder
- [ ] Fluentd / Fluent Bit
- [ ] Logstash
- [ ] rsyslog
- [ ] Other: ___________________

**Log Destination** (SIEM / log management system):
- Hostname: ________________________________________
- IP Address: ________________________________________
- Port: ________________________________________
- Protocol: ________________________________________

**Authentication / Credentials** (if required):
- Authentication method: ___________________
- Credential storage location: ___________________

---

### Section 6: Log Content Details

**Key Log Fields** (list important fields in logs from this source):
1. ________________________________________
2. ________________________________________
3. ________________________________________
4. ________________________________________
5. ________________________________________

**Sample Log Event** (paste representative log entry):
```
[Paste sample log message here]
```

**Parsing Requirements**:
- [ ] Standard parsing (syslog, CEF, JSON) - no custom parsing needed
- [ ] Custom parsing required (attach parsing rule specification)

**Sensitive Data in Logs** (check if logs may contain):
- [ ] Passwords or credentials (MUST be excluded - see S2.1)
- [ ] Personal data (PII) - requires access controls
- [ ] Payment card data (MUST be masked per PCI DSS)
- [ ] Health information (HIPAA considerations)
- [ ] None of the above

---

### Section 7: Integration Checklist

**Pre-Implementation**:
- [ ] Log source documented in this template
- [ ] Log format and content reviewed
- [ ] Parsing rules developed (if needed)
- [ ] Network connectivity verified (test log forwarding)
- [ ] Firewall rules created (if needed)
- [ ] Storage capacity planned for estimated volume
- [ ] Retention period configured

**Implementation**:
- [ ] Log forwarder / agent installed (if needed)
- [ ] Log forwarding configured on source system
- [ ] Logs receiving in SIEM / log management system
- [ ] Parsing working correctly (no parse errors)
- [ ] All required fields present
- [ ] Timestamp format correct (timezone verified)
- [ ] Log volume within expected range

**Post-Implementation**:
- [ ] Log source added to inventory (ISMS-IMP-A.8.15.1)
- [ ] Monitoring alerts configured (collection failures)
- [ ] Retention policies applied
- [ ] Access controls configured (who can view these logs)
- [ ] Documentation updated (architecture diagrams, runbooks)

---

### Section 8: Testing and Validation

**Test Date**: __________________

**Tests Performed**:
- [ ] Log generation verified (system produces expected logs)
- [ ] Log forwarding verified (logs arrive at SIEM)
- [ ] Parsing validated (logs parsed correctly, no errors)
- [ ] All required fields present and populated
- [ ] Timestamp accuracy verified (time synchronization checked)
- [ ] Log search verified (can query logs in SIEM)
- [ ] Alert generation tested (if applicable)

**Test Results**: 
- [ ] Pass - ready for production
- [ ] Fail - issues identified (see below)

**Issues Identified**:
________________________________________________________________________
________________________________________________________________________
________________________________________________________________________

**Resolution Plan**:
________________________________________________________________________
________________________________________________________________________

---

### Section 9: Approvals

**System Owner Approval** (confirms logging configuration acceptable):
- Name: ________________________________________
- Signature: ____________________ Date: ____________________

**Log Administrator Approval** (confirms successful integration):
- Name: ________________________________________
- Signature: ____________________ Date: ____________________

**Information Security Approval** (confirms compliance with policy):
- Name: ________________________________________
- Signature: ____________________ Date: ____________________

---

### Section 10: Change Management

**Changes to Log Source** (document any configuration changes):

| Date | Change Description | Changed By | Reason |
|------|-------------------|------------|--------|
| | | | |
| | | | |
| | | | |

---

### Section 11: Exception Management

**If this log source does not fully comply with logging policy (S2.1), document exception**:

**Exception Requested**: 
- [ ] No exception needed - fully compliant
- [ ] Exception required (complete below)

**Policy Requirement Not Met**: ________________________________________

**Justification for Exception**: 
________________________________________________________________________
________________________________________________________________________

**Compensating Controls**: 
________________________________________________________________________
________________________________________________________________________

**Exception Duration**: 
- [ ] Temporary (expires: __________)
- [ ] Permanent (with annual review)

**Exception Approval**:
- CISO Name: ________________________________________
- Signature: ____________________ Date: ____________________

---

## B.3 Template Usage Instructions

### Step 1: System Owner Completes Sections 1-4
- Identify system and contacts
- Determine logging priority based on classification
- Estimate log volume

### Step 2: Log Administrator Completes Section 5-6
- Determine log format and transport
- Configure log collection
- Document parsing requirements

### Step 3: Joint Completion of Section 7-8
- System Owner and Log Administrator work together
- Complete integration checklist
- Conduct testing and validation

### Step 4: Approvals (Section 9)
- System Owner confirms configuration
- Log Administrator confirms successful integration
- Information Security confirms policy compliance

### Step 5: Ongoing Maintenance (Sections 10-11)
- Document changes over time
- Manage exceptions if applicable

---

## B.4 Template Customization

Organizations **MAY** customize this template to include:
- Additional fields specific to organizational needs
- Custom approval workflows
- Integration with CMDB or asset management systems
- Automated form submission via ServiceNow, Jira, etc.

Organizations **SHALL NOT** remove mandatory sections:
- System identification (Section 1-2)
- Classification and requirements (Section 3-4)
- Integration checklist (Section 7)
- Approvals (Section 9)

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S5.B |
| **Document Type** | Annex - Template |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~315 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |

---

**END OF ANNEX B**