# ISMS-POL-A.8.15-S5.D
## Logging - Quick Reference Guide

**Document ID**: ISMS-POL-A.8.15-S5.D  
**Title**: Logging - Quick Reference Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial quick reference |

**Review Cycle**: Quarterly (keep current with policy updates)  
**Next Review Date**: [Approval Date + 3 months]  
**Approvers**: Information Security Manager  
**Distribution**: All personnel with logging responsibilities

---

## D.1 Decision Trees

### D.1.1 "Should I Log This Event?"
```
START: Is this a system, application, or network device?
  |
  NO --> Out of scope (end-user devices, IoT, etc. - separate policies)
  |
  YES
  |
  V
Is it processing sensitive data OR performing security functions?
  |
  YES --> MUST LOG (SHALL requirement)
  |     - Authentication events
  |     - Authorization events
  |     - Administrative actions
  |     - Security events
  |     - Data access (for sensitive data)
  |
  NO
  |
  V
Is it business-critical or required for compliance?
  |
  YES --> SHOULD LOG (strong recommendation)
  |     - Application transactions
  |     - System errors
  |     - Configuration changes
  |
  NO --> MAY LOG (optional, operational benefit only)
        - Debug logs
        - Performance metrics
        - Non-critical informational events
```

### D.1.2 "What Retention Period Should I Use?"
```
START: What type of logs are these?

Security Events / Authentication / Administrative Actions
  --> 12 months online + 7 years archive
  (Rationale: Forensics, compliance, legal evidence)

Database Logs (with sensitive data)
  --> 12 months online + 7 years archive
  (Rationale: Audit trails, SOX, GDPR accountability)

Application Logs / System Logs
  --> 6 months online + 1 year archive
  (Rationale: Troubleshooting, performance analysis)

Network Device Logs
  --> 6 months online + 1 year archive
  (Rationale: Network troubleshooting, incident investigation)

Special Cases:
  - PCI DSS systems --> Minimum 12 months online (no flexibility)
  - HIPAA systems --> 6 years minimum
  - SOX financial systems --> 7 years minimum
  - GDPR with no other requirement --> 6-24 months (document necessity)

When in doubt: Use 12 months online + 3 years archive (safe default)
```

### D.1.3 "What Log Protection Do I Need?"
```
START: What is the criticality of these logs?

CRITICAL (audit logs, privileged access, security events):
  --> Implement ALL protections:
      - Write-Once storage (WORM)
      - Cryptographic hashing
      - Separate log admin from system admin
      - Encrypted transmission (TLS)
      - Encrypted storage at rest
      - Access controls (RBAC)
      - Backup and DR

HIGH (authentication, application logs with sensitive data):
  --> Implement MOST protections:
      - Encrypted transmission (TLS)
      - Access controls (RBAC)
      - Integrity monitoring (hashing)
      - Backup
      - Separation of duties (where feasible)

MEDIUM (system logs, operational logs):
  --> Implement BASIC protections:
      - Access controls (RBAC)
      - Backup
      - Encrypted transmission (within secure network optional)

LOW (non-sensitive operational logs):
  --> MINIMUM protections:
      - Access controls
      - Standard backup
```

---

## D.2 Common Scenarios

### Scenario 1: New Server Deployment
**Question**: "We're deploying a new web server. What logging do I need?"

**Answer**:
1. **Configure OS logging**: Authentication, administrative actions, system events
2. **Configure web server logging**: Access logs, error logs, security events
3. **Configure application logging**: Transaction logs, errors, security events
4. **Set up log forwarding**: Use syslog over TLS or install log forwarder agent
5. **Document in inventory**: Complete Log Source Template (S5.B)
6. **Test**: Verify logs arriving at SIEM, parsing correctly
7. **Configure retention**: 12 months online for security logs, 6 months for operational
8. **Set up monitoring**: Alert if log forwarding fails

**Time Required**: 2-4 hours  
**Template**: Use S5.B (Log Source Template)

---

### Scenario 2: Cloud Service (SaaS) Onboarding
**Question**: "We're using a new SaaS application. How do we log it?"

**Answer**:
1. **Check SaaS logging capabilities**:
   - Does it generate audit logs?
   - Can logs be exported/forwarded?
   - What events are logged?

2. **Configure SaaS audit logging**:
   - Enable all available audit logging in SaaS admin console
   - Configure log forwarding (SIEM API, syslog, webhook)
   - Or set up scheduled log export (daily/weekly)

3. **Common SaaS logging methods**:
   - API pull (SIEM polls SaaS API for logs)
   - Webhook push (SaaS sends logs to SIEM endpoint)
   - Email export (manual, not recommended for automation)
   - CSV/JSON export (scheduled download)

4. **Critical SaaS events to log**:
   - User authentication (SSO logins)
   - Administrative actions (user provisioning, permission changes)
   - Data access (downloads, exports, shares)
   - Configuration changes

**Common SaaS Platforms**:
- **Microsoft 365**: Use Azure AD logs, Exchange logs, SharePoint logs
- **Salesforce**: Enable Event Monitoring, Shield Event Monitoring
- **Google Workspace**: Enable audit logs, export via API
- **Slack**: Enable audit logs (Enterprise plan), export via API
- **GitHub**: Enable audit log streaming

---

### Scenario 3: Legacy System Cannot Meet Requirements
**Question**: "Our legacy AS/400 system can't forward logs. What do we do?"

**Answer**:
1. **Assess current logging capabilities**:
   - Does system generate any logs locally?
   - Can logs be accessed programmatically?
   - Can logs be exported manually?

2. **Explore workarounds**:
   - Install log agent on system (if OS supports)
   - Set up scheduled script to export/forward logs
   - Use database audit tables (if applicable)
   - Monitor at network level (firewall logs, database proxy logs)

3. **Document exception request**:
   - Use Exception section in S5.B template
   - Identify compensating controls:
     - Network-level logging (firewall logs of connections)
     - Database proxy logging (if using database gateway)
     - Enhanced access controls (restrict who can access system)
     - Manual periodic review of any available logs
   - Get CISO approval

4. **Plan remediation**:
   - Set decommission date for legacy system
   - Or plan upgrade/migration to modern platform
   - Include logging capability in requirements for replacement

---

### Scenario 4: Developer Needs Access to Production Logs
**Question**: "Developer needs to troubleshoot production issue. How do we give log access?"

**Answer**:
1. **Assess necessity**:
   - Is production log access truly required?
   - Can issue be reproduced in test environment?
   - Can sanitized/anonymized logs be provided instead?

2. **If production access required**:
   - **Grant temporary access** (duration: hours/days, not permanent)
   - **Limit scope** (only logs for specific application/timeframe)
   - **Require justification** (incident ticket, approval from manager)
   - **Sanitize sensitive data** (mask PII, credentials, payment data)
   - **Monitor access** (log all queries developer executes)
   - **Revoke after use** (remove access when issue resolved)

3. **Privacy considerations**:
   - Developers SHALL NOT access logs containing:
     - Personal health information (HIPAA)
     - Payment card data (PCI DSS)
     - Personal data without business need (GDPR)
   - If such logs needed, involve DPO/Legal

4. **Alternative approaches** (preferred):
   - Security team runs queries on behalf of developer
   - Provide aggregated/statistical data (not raw logs)
   - Set up dedicated test/staging environment with realistic logs

---

### Scenario 5: Log Storage Full - Emergency Response
**Question**: "Our SIEM storage is 95% full! What do we do?"

**Answer**:
1. **Immediate actions** (stop the bleeding):
   - Check for log storms (one source generating excessive logs)
   - Temporarily reduce retention of non-critical logs
   - Temporarily disable verbose debug logging
   - Prioritize critical logs (keep security/audit logs)

2. **Short-term solution** (hours to days):
   - Archive older logs to cold storage
   - Add temporary storage capacity
   - Implement log filtering/sampling for high-volume sources

3. **Long-term solution** (days to weeks):
   - Increase storage capacity (buy more storage)
   - Implement tiered storage (hot/warm/cold)
   - Review log volume by source (identify top consumers)
   - Tune logging levels (reduce unnecessary verbosity)
   - Implement lifecycle policies (automated tiering)

4. **Prevention**:
   - Implement capacity monitoring (alert at 70%, 85%)
   - Forecast growth (plan capacity 12 months ahead)
   - Regular capacity reviews (quarterly)

**DO NOT**:
- Delete security or audit logs before retention period
- Delete logs under legal hold
- Delete logs from critical systems without approval

---

## D.3 Troubleshooting Guide

### Problem: Logs Not Arriving at SIEM

**Symptom**: System should be sending logs but nothing appearing in SIEM

**Troubleshooting Steps**:
1. **Check source system**:
   - Is logging enabled?
   - Is log forwarder running? (`systemctl status rsyslog` or equivalent)
   - Check local log files (are logs being generated?)
   - Check log forwarder configuration (correct destination IP/port?)

2. **Check network connectivity**:
   - Can source ping SIEM? (`ping siem.example.com`)
   - Is firewall blocking? (check firewall rules for port 514/601/6514)
   - Test connectivity: `telnet siem.example.com 601`

3. **Check SIEM receiver**:
   - Is SIEM receiver running?
   - Check SIEM logs for connection attempts
   - Check SIEM configuration (listening on correct port?)
   - Check SIEM disk space (full disk = can't receive)

4. **Check credentials** (if using authenticated forwarding):
   - Are credentials correct?
   - Are certificates valid (not expired)?

5. **Check parsing**:
   - Logs arriving but not parsed = check SIEM parsing rules
   - Look for parsing errors in SIEM

**Common Causes**:
- Firewall blocking traffic (most common)
- Log forwarder not running
- Incorrect destination IP/hostname
- Certificate validation failure (TLS)
- SIEM disk full

---

### Problem: Excessive False Positives

**Symptom**: SIEM generating too many false positive alerts, analysts overwhelmed

**Troubleshooting Steps**:
1. **Identify top false positive sources**:
   - Which rules generate most false positives?
   - Generate report: False positives by rule (last 30 days)

2. **For each high-volume rule**:
   - **Tune thresholds**: Increase threshold (e.g., 10 failures → 20 failures)
   - **Add exceptions**: Allowlist known-good IPs, users, or patterns
   - **Improve detection logic**: Add additional conditions to rule
   - **Disable rule**: If rule provides no value, disable it

3. **Validate business processes**:
   - Some "false positives" are legitimate business activities
   - Example: Failed logins from mobile app (app retries on network issues)
   - Solution: Whitelist legitimate patterns

4. **Balance precision vs. recall**:
   - Reducing false positives may increase false negatives
   - Prefer false positives for critical threats (malware, C2)
   - Accept fewer alerts for low-severity issues

**Target False Positive Rate**: <10%

---

### Problem: Slow Log Queries

**Symptom**: Searching logs in SIEM is very slow (minutes to complete)

**Troubleshooting Steps**:
1. **Optimize query**:
   - Narrow time range (search last 24 hours, not last 90 days)
   - Use indexed fields (don't search free text if avoidable)
   - Use filters before wildcards
   - Limit result count

2. **Check SIEM performance**:
   - CPU/memory usage high?
   - Disk I/O saturated?
   - Too many concurrent queries?

3. **Review indexing strategy**:
   - Are commonly searched fields indexed?
   - Is indexing up to date?

4. **Consider tiered storage**:
   - Move old logs to warm/cold storage
   - Keep recent logs (30-90 days) on fast storage

5. **Upgrade hardware** (if needed):
   - Add more storage IOPS
   - Add more RAM
   - Add more CPU cores

---

### Problem: Missing Log Fields

**Symptom**: Logs arriving but missing expected fields (user ID, source IP, etc.)

**Troubleshooting Steps**:
1. **Check source configuration**:
   - Is source system configured to include these fields?
   - Example: Web server logs need to include client IP in log format

2. **Check parsing rules**:
   - Is SIEM correctly parsing log format?
   - Check for parsing errors
   - Review parsing rule (field extraction patterns)

3. **Check log format**:
   - Compare sample log to expected format
   - Is log format documented?
   - Did log format change (application update)?

4. **Fix parsing**:
   - Update parsing rule to extract missing fields
   - Test with sample logs before deploying to production

---

## D.4 Frequently Asked Questions (FAQ)

### Q1: Do we need to log everything?
**A**: No. Log what is necessary for security, compliance, and operations. Logging everything is expensive (storage) and makes finding important events harder (needle in haystack). Focus on:
- Authentication and authorization events
- Administrative actions
- Security events
- Access to sensitive data
- System errors and failures

---

### Q2: How long do we need to keep logs?
**A**: Depends on log type and regulatory requirements:
- **Security/audit logs**: 12 months online + 7 years archive (safe default)
- **PCI DSS systems**: Minimum 12 months (mandatory)
- **HIPAA systems**: 6 years minimum
- **Operational logs**: 6 months online + 1 year archive
- **See Section D.1.2** for decision tree

---

### Q3: Can we delete logs to free up space?
**A**: Only under these conditions:
- Retention period has expired
- No legal hold in effect
- Not required for ongoing investigation
- CISO approval for emergency deletion

**NEVER delete**:
- Logs before retention period
- Logs under legal hold
- Security event logs from critical systems
- Logs from past 30 days (minimum)

---

### Q4: Who can access logs?
**A**: Access based on role and need-to-know:
- **SOC Analysts**: Read access to security logs
- **System Admins**: Read access to their own systems (NOT logs of their own actions)
- **Incident Responders**: Full access during investigations
- **Auditors**: Read access for audits
- **Management**: Reports and summaries (not raw logs)
- **Developers**: Generally NO production log access (use test environments)

All log access is logged (meta-logging).

---

### Q5: Can system administrators see logs of their own actions?
**A**: This creates conflict of interest (administrator could hide malicious actions). Best practice:
- **Separate log administrators from system administrators**
- System admin X cannot modify logs from system X
- Independent review of administrative actions

For small organizations where complete separation not feasible:
- Implement compensating controls (frequent independent review, WORM storage)
- Document exception

---

### Q6: What if a system can't meet logging requirements?
**A**: Document an exception:
1. Identify what requirement cannot be met
2. Document business/technical justification
3. Identify compensating controls
4. Get CISO approval
5. Review exception annually
6. Plan remediation (upgrade, replace, decommission)

Use Exception section in Log Source Template (S5.B).

---

### Q7: Do we log personal data? (GDPR/FADP considerations)
**A**: Yes, but with privacy protections:
- **Log only what's necessary** (data minimization)
- **Don't log message content** (log metadata: who, what, when, where)
- **Implement access controls** (not everyone needs log access)
- **Limit retention** (don't keep logs forever)
- **Inform users** (privacy notice, acceptable use policy)
- **Support data subject rights** (provide logs on request, delete if required with security exceptions)

Logs for security purposes are generally permitted under GDPR Article 6(1)(f) (legitimate interests).

---

### Q8: What's the difference between logging and monitoring?
**A**:
- **Logging** (this policy): Recording events that occur
- **Monitoring** (A.8.16): Actively watching logs for anomalies and incidents

Logging provides the data; monitoring analyzes the data.

Both required for effective security.

---

### Q9: How do we handle logs from cloud services?
**A**: Most cloud services provide audit logs:
- **Enable audit logging** in cloud console/admin panel
- **Forward logs to SIEM** (API, webhook, or scheduled export)
- **Configure retention** in cloud service (backup, don't rely solely on cloud provider)
- **Check what's logged** (authentication, admin actions, data access)

Common cloud logging:
- **AWS**: CloudTrail, VPC Flow Logs, S3 access logs
- **Azure**: Activity Logs, Diagnostic Logs, Azure AD logs
- **GCP**: Cloud Audit Logs, VPC Flow Logs
- **Microsoft 365**: Unified Audit Log, Azure AD logs

---

### Q10: What should I do if I discover log tampering?
**A**: This is a **CRITICAL security incident**:
1. **Immediately escalate** to CISO and Incident Response Team
2. **Preserve evidence** (copy tampered logs, forensic images)
3. **Isolate compromised systems** (prevent further tampering)
4. **Investigate** (who had access? when did tampering occur?)
5. **Assess impact** (what evidence is lost? what attacks may be hidden?)
6. **Remediate** (fix vulnerability, strengthen controls)
7. **Report** (to management, possibly law enforcement or regulators)

Tampering indicates sophisticated attacker or malicious insider.

---

## D.5 Regulatory Quick Reference

### ISO 27001:2022 - Control A.8.15
**Requirement**: "Event logs recording user activities, exceptions, faults and information security events shall be produced, kept and regularly reviewed."

**Key Points**:
- Must log user activities
- Must log security events
- Must keep logs (retention)
- Must regularly review logs

**Evidence for Audit**:
- Log source inventory (ISMS-IMP-A.8.15.1)
- Log review documentation (daily/weekly/monthly reports)
- Incident investigation reports
- Retention compliance reports

---

### GDPR - Article 32(1)(d)
**Requirement**: "A process for regularly testing, assessing and evaluating the effectiveness of technical and organizational measures for ensuring the security of the processing."

**Logging Relevance**: Logs provide evidence of security measures and enable detection of breaches.

**Key Points**:
- Logs necessary for security monitoring
- Logs must be protected (controller accountability)
- Personal data in logs must be protected
- Data subjects have rights (access, deletion with security exceptions)

**Retention**: Log only as long as necessary, document necessity (6-24 months typical with justification)

---

### PCI DSS 4.0 - Requirement 10
**Requirement**: "Log and monitor all access to system components and cardholder data."

**Key Points**:
- **10.2**: Log all user activities
- **10.3**: Record required data elements for each log entry
- **10.4**: Protect log data from unauthorized modification
- **10.5**: Retain log data for at least 12 months, 3 months immediately available
- **10.7**: Detect and report failures of critical security control systems

**Mandatory Retention**: 12 months minimum, 3 months hot storage

---

### HIPAA Security Rule - 164.312(b)
**Requirement**: "Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use electronic protected health information."

**Key Points**:
- Audit controls required (Standard)
- Record and examine system activity
- Protect audit information from unauthorized access

**Typical Retention**: 6 years (aligns with HIPAA record retention requirements)

---

## D.6 Escalation Quick Reference

| Severity | Response Time | Escalate To | Notification Method |
|----------|---------------|-------------|---------------------|
| **P1 Critical** | <15 minutes | SOC Lead → Incident Response Manager → CISO → Exec Management | Phone call (immediate) |
| **P2 High** | <1 hour | SOC Lead → Information Security Manager | Phone/email (urgent) |
| **P3 Medium** | <4 hours | SOC Lead | Email/ticket |
| **P4 Low** | Next business day | SOC Analyst (self-managed) | Ticket only |

**Examples**:
- **P1**: Active malware outbreak, C2 communication detected, ongoing data breach
- **P2**: Failed authentication spike, privilege escalation, data exfiltration attempt
- **P3**: Policy violation, system anomaly, failed access attempts
- **P4**: Informational events, low-severity alerts

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S5.D |
| **Document Type** | Annex - Quick Reference |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~385 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |

---

**END OF ANNEX D**

---

*"When in doubt, log it. When certain, log it anyway."*  
— SOC Wisdom

*"The answer to your security question is probably in the logs. The trick is finding it."*  
— Log Analysis Truth