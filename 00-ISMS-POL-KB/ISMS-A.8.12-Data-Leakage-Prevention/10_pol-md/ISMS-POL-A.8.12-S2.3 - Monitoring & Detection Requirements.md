# ISMS-POL-A.8.12-S2.3
## Data Leakage Prevention - Monitoring & Detection Requirements

**Document ID**: ISMS-POL-A.8.12-S2.3  
**Title**: Monitoring & Detection Requirements  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | Information Security Manager / SOC Lead | Initial monitoring and detection requirements |

**Review Cycle**: Semi-annual (or upon significant threat/infrastructure changes)  
**Next Review Date**: 2025-07-03  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Lead / Information Security Manager
- Operational Review: IT Operations Manager
- Compliance Review: Data Protection Officer (DPO) / Legal

**Distribution**: SOC analysts, security team, IT operations, audit team  
**Related Documents**: ISMS-POL-A.8.12-S2.1 (Data Classification), ISMS-POL-A.8.12-S2.2 (Channel Protection), ISMS-POL-A.8.15 (Logging - organizational control)

---

## 1. Introduction

### 1.1 Document Purpose

This document establishes **mandatory requirements** for logging, alerting, monitoring, and analysis of Data Leakage Prevention (DLP) events to support:

- **Security incident detection** - Identify data exfiltration attempts
- **Policy compliance verification** - Ensure DLP policies are enforced
- **Forensic investigation** - Provide audit trail for incident analysis
- **False positive management** - Tune DLP rules to reduce noise
- **Threat intelligence** - Understand attack patterns and insider risks
- **Regulatory compliance** - Demonstrate FADP/GDPR data protection controls

**Critical Principle:**  
> *"Detection without response is security theater. Monitoring without tuning is alert fatigue."*  
> — The First Law of SOC Operations

Organizations that deploy DLP without effective monitoring generate thousands of alerts that nobody investigates, creating a **false sense of security** while actual data leakage goes undetected.

### 1.2 Relationship to DLP Framework

This document (S2.3) is the **third domain** in the DLP requirements hierarchy:
```
ISMS-POL-A.8.12-S2 (Requirements Overview)
    ├── ISMS-POL-A.8.12-S2.1 (Data Classification) → What data to protect
    ├── ISMS-POL-A.8.12-S2.2 (Channel Protection) → Prevent exfiltration
    ├── ISMS-POL-A.8.12-S2.3 (Monitoring & Detection) ← YOU ARE HERE → Detect violations
    └── ISMS-POL-A.8.12-S2.4 (Incident Response) → Handle detected incidents
```

**Dependency:**  
Monitoring requirements depend on **S2.2 (Channel Protection)** - DLP channels generate alerts that monitoring processes handle.

---

## 2. DLP Event Logging Requirements

### 2.1 Mandatory Log Events

DLP solutions SHALL log the following events for **all protected channels**:

#### 2.1.1 Data Transfer Attempts

**Event Data:**
- **Timestamp** (UTC, ISO 8601 format: `DD.MM.YYYYTHH:MM:SSZ`)
- **User identity** (username, email, employee ID, domain account)
- **Endpoint/device** (hostname, IP address, MAC address, device ID)
- **Channel** (email, web, USB, network, application, mobile)
- **Action** (allow, block, alert, quarantine, encrypt)
- **Data classification** (Public, Internal, Confidential, Restricted)
- **Data category** (PII, financial, IP, credentials, business confidential)
- **Volume** (file size, record count, page count)

**Example:**
```json
{
  "timestamp": "2025-01-03T14:32:18Z",
  "user": "john.smith@company.com",
  "endpoint": "LAPTOP-JS-WIN11",
  "channel": "email",
  "action": "block",
  "classification": "Restricted",
  "category": "PII-GDPR-Article9",
  "volume": "1 file, 245KB",
  "reason": "Fingerprint match: customer_database_export.xlsx"
}
```

#### 2.1.2 Policy Rule Matches

**Event Data:**
- **Rule ID** (unique identifier for DLP policy rule)
- **Rule name** (human-readable: "Block credit cards via email")
- **Detection method** (pattern, keyword, fingerprint, ML, contextual)
- **Confidence score** (0-100%, for ML-based detection)
- **Matched content** (sanitized excerpt or hash, NOT full sensitive data)

**Sensitive Data Handling:**  
Logs SHALL NOT contain actual sensitive data (credit card numbers, SSNs, passwords). Use:
- **Masked values** (`4111-****-****-1111` instead of full PAN)
- **Hash values** (SHA-256 hash of detected pattern)
- **Match count** ("Detected 15 credit card numbers" instead of listing them)

#### 2.1.3 Administrative Actions

**Event Data:**
- **Administrator identity** (who made the change)
- **Action type** (policy created/modified/deleted, exception granted, configuration change)
- **Change details** (before/after values for audit trail)
- **Justification** (business reason for change, if documented)

**Examples:**
- Policy rule "Block SSH Private Keys" severity changed from Alert to Block
- Exception granted for user jane.doe@company.com to email contract to partner@acmecorp.com for 7 days
- Endpoint DLP disabled on LAPTOP-CEO-MACBOOK for emergency travel (24-hour exception)

#### 2.1.4 False Positive Reports

**Event Data:**
- **User identity** (who reported false positive)
- **Original alert ID** (link to blocked/alerted event)
- **User justification** (why they believe it's legitimate)
- **Review status** (pending, approved, rejected)
- **Resolution** (whitelisted, policy tuned, user educated)

### 2.2 Optional Log Events

DLP solutions SHOULD log (where technically feasible and storage permits):

**Enhanced Transfer Metadata:**
- **Source location** (file path, database table, SharePoint site)
- **Destination** (email recipient, cloud storage bucket, USB drive serial number, external IP)
- **Transfer duration** (start/end timestamps)
- **User-agent** (application used: Outlook, Chrome, FileZilla)

**Behavioral Analytics Data:**
- **Transfer frequency** (5th file transfer by this user today)
- **Time of day** (transfer at 2:00 AM - anomalous for this user)
- **Baseline deviation** (user typically transfers 5MB/day, today transferred 500MB)

**Contextual Information:**
- **Business context** (transfer during quarter-end close vs. routine day)
- **Related events** (user accessed HR system 5 minutes before USB transfer)

### 2.3 Log Format and Structure

DLP logs SHALL:
- Use **structured format** (JSON, CEF, Syslog, or vendor-specific structured format)
- Include **consistent field naming** across all channels
- Support **parsing by SIEM** (Splunk, Elastic, QRadar, Sentinel, etc.)
- Include **unique event ID** for correlation (e.g., `DLP-2025010314321812345`)

DLP logs SHOULD:
- Use **UTC timestamps** (avoid timezone confusion)
- Include **correlation IDs** linking related events (email send + attachment scan = same correlation ID)
- Support **export** in standard formats (CSV, JSON, XML for external analysis)

---

## 3. Privacy and Legal Compliance

### 3.1 Employee Monitoring Compliance

DLP monitoring involves **employee activity surveillance**, which is subject to **Swiss FADP Article 26 and GDPR Article 5 (lawfulness, fairness, transparency)**.

#### 3.1.1 Transparency Requirements

Organizations SHALL:
- **Notify employees** that DLP monitoring is active (Acceptable Use Policy, employment contract, annual training)
- **Explain what is monitored** (email, web, USB, file transfers, NOT personal communications on personal devices)
- **State retention period** (how long DLP logs are kept)
- **Clarify access rights** (employees MAY request access to logs about them under FADP/GDPR)

**Employee Notification Template (minimum):**
> "The organization monitors data transfers via email, web, USB drives, and other channels to prevent unauthorized disclosure of confidential information. DLP systems log user identity, transfer timestamps, data classification, and actions taken. Logs are retained for [X months] and accessible only to authorized security personnel. Employees have the right to request access to logs pertaining to their activities. For questions, contact the Data Protection Officer."

#### 3.1.2 Proportionality Assessment

Organizations SHALL conduct **proportionality assessment** before deploying DLP monitoring:

**Proportionality Test (Swiss Employment Law - Article 328b CO):**
1. **Legitimate purpose?** (Data protection is legitimate business interest ✅)
2. **Suitable means?** (DLP monitoring is suitable for detecting data leakage ✅)
3. **Necessary?** (Is monitoring the least intrusive means to achieve purpose? Evaluate alternatives)
4. **Reasonable?** (Would reasonable person find monitoring excessive? If yes = non-proportionate)

**Documenting Proportionality:**
Organizations SHALL document:
- Business justification (regulatory compliance, intellectual property protection)
- Alternative measures considered (training-only, trust-based approach)
- Why DLP monitoring is necessary (history of incidents, regulatory mandates)
- Safeguards implemented (data minimization, limited log access, retention limits)

DPO SHALL review proportionality assessment before DLP deployment.

#### 3.1.3 Data Minimization

Logs SHALL capture **only data necessary** for security and compliance:

**Minimize:**
- Log domain-level URLs (`example.com`) rather than full URLs (`example.com/sensitive-report?user=john&password=123`)
- Log file names/types, NOT file contents
- Log transfer volume (MB), NOT actual data transferred
- Log "credit card detected" NOT actual card numbers

**Avoid:**
- Logging personal email content (body text, attachments)
- Logging web search queries (privacy-invasive)
- Logging unrelated application data (screenshots, keystrokes)

### 3.2 Log Access Controls

DLP logs contain **sensitive information** about employee behavior. Access SHALL be restricted:

**Access Tiers:**
- **Tier 1 (SOC Analysts):** Read-only access to DLP alerts for triage
- **Tier 2 (Security Engineers):** Read access to all logs for investigation, tuning
- **Tier 3 (DPO/Legal/HR):** Access to specific user logs upon formal request
- **Tier 4 (Auditors):** Read-only access for compliance verification

**Access Logging:**  
All log access SHALL be audited (who accessed DLP logs, when, which user's data, justification).

### 3.3 Data Retention

DLP logs SHALL be retained according to **organizational data retention policy** (ISMS-POL-A.8.10):

**Recommended Retention Tiers:**
- **Active alerts (under investigation):** Retain until case closure + 90 days
- **Resolved incidents:** Retain per incident retention policy (typically 2-7 years)
- **Non-incident logs (routine allows):** 90 days to 12 months (balance storage vs. investigation needs)
- **Regulatory compliance logs:** Per regulatory requirement (GDPR: no specific mandate, Swiss FADP: business justification required)

**Retention Rationale:**
- **Too short (<30 days):** Insufficient for investigation, pattern analysis
- **Too long (>24 months for routine logs):** Excessive storage cost, privacy concern, FADP proportionality risk

Organizations SHALL document retention period justification and DPO SHALL approve.

---

## 4. Real-Time Alerting Requirements

### 4.1 Alert Severity Classification

DLP alerts SHALL be classified by **severity** to prioritize SOC response:

| Severity | Definition | Response SLA | Examples |
|----------|------------|--------------|----------|
| **Critical** | Active data exfiltration, high-value data, external transfer | Immediate (15 min) | Credentials emailed externally, mass file transfer to personal Dropbox, source code to GitHub |
| **High** | Unauthorized transfer of Restricted data | 1 hour | PII emailed without encryption, financial data via USB, IP exported to cloud |
| **Medium** | Confidential data transfer requiring review | 4 hours | Contract emailed to new vendor, Finance sending data to unapproved partner |
| **Low** | Policy violation, tuning needed | 24 hours | False positive reports, policy exceptions usage, routine alerts |
| **Informational** | Monitoring-only events, no violation | No SLA | Allowed transfers logged for audit, classification label usage stats |

### 4.2 Mandatory Real-Time Alerts

Organizations SHALL configure real-time alerts for:

#### 4.2.1 Critical Alerts (15-Minute SLA)

- **Credentials/secrets detected** (passwords, API keys, private keys) - ANY channel
- **Mass exfiltration** (>100 files or >1GB in <10 minutes) - USB, cloud, network
- **Repeated blocking** (same user blocked >5 times in 1 hour) - potential malicious insider
- **C2 indicators** (DLP + network correlation: data sent to known malicious IPs)

**Alert Delivery:**  
Critical alerts SHALL be delivered via **multiple channels** (SIEM, email, SMS, ticketing system) to ensure visibility.

#### 4.2.2 High Alerts (1-Hour SLA)

- **PII/Special Categories** (GDPR Article 9) transferred externally without encryption
- **Payment card data** (PCI DSS scope) to unauthorized recipients
- **IP/source code** transferred to personal accounts or external repositories
- **Database exports** (>1000 records) to unauthorized locations

### 4.3 Alert Enrichment

DLP alerts SHOULD be enriched with contextual data:

**User Context:**
- User role/department (Finance user transferring financial data = lower suspicion)
- User tenure (new employee <30 days = higher risk)
- User access level (admin, privileged, standard)
- Recent HR events (resignation submitted, termination pending)

**Behavioral Context:**
- Historical transfer patterns (user normally transfers 5MB/day, today 500MB)
- Time-of-day anomaly (transfer at 3:00 AM, user normally works 9-5)
- Location anomaly (transfer from unknown IP address, VPN from foreign country)

**Threat Intelligence:**
- Destination IP/domain reputation (known malicious, newly registered, anonymous hosting)
- File hash reputation (VirusTotal, internal hash database)

### 4.4 Alert Deduplication

Organizations SHOULD implement alert deduplication to reduce noise:

**Deduplication Rules:**
- Same user, same file, same violation within 5 minutes = 1 alert (not 10 alerts)
- Bulk operations (user copies 100 files to USB) = 1 summary alert with file count
- Scheduled jobs (automated reports) = suppress after first occurrence, review weekly

---

## 5. False Positive Management

### 5.1 False Positive Lifecycle

Organizations SHALL implement structured false positive management:
```
1. User reports false positive (via self-service portal or helpdesk)
2. SOC triages report (verify legitimacy, check business context)
3. Security Engineering investigates (analyze DLP rule, detection pattern)
4. Remediation:
   a) Whitelist legitimate business flow (permanent exception)
   b) Tune DLP rule (adjust regex, confidence threshold)
   c) User education (explain policy, suggest alternative workflow)
5. Documentation (update exception register, track FP metrics)
6. Periodic review (quarterly recertification of exceptions)
```

### 5.2 False Positive Metrics

Organizations SHALL track:

| Metric | Formula | Target |
|--------|---------|--------|
| **False Positive Rate** | (False Positives / Total Alerts) × 100% | <10% (after 6 months tuning) |
| **Time to Resolve FP** | Average days from report to resolution | <3 business days |
| **Repeat False Positives** | Same FP reported >1 time | <5% of total FPs |
| **Exception Growth** | Month-over-month exception count increase | <5% growth (stable state) |

**Unacceptable Thresholds:**
- FP Rate >40% = **DLP is unusable**, emergency tuning required
- FP Rate 20-40% = **Alert fatigue imminent**, aggressive tuning needed
- FP Rate 10-20% = **Acceptable during initial 6 months**, continuous improvement required

### 5.3 Tuning Strategies

Organizations SHOULD implement systematic tuning:

**Phase 1 (Months 1-3): Aggressive Tuning**
- Review top 10 false positive patterns weekly
- Whitelist obvious legitimate workflows (Finance → Bank, HR → Payroll)
- Adjust overly sensitive rules (reduce keyword matches, increase confidence thresholds)

**Phase 2 (Months 4-6): Refinement**
- Review false positive trends monthly
- Implement contextual rules (allow Finance sending invoices, block everyone else)
- User education on proper data handling (reduce policy violations)

**Phase 3 (Months 7+): Steady State**
- Quarterly false positive review
- Exception recertification (validate business need still exists)
- New rule deployment (careful testing in monitor-only mode first)

---

## 6. Monitoring and Analysis

### 6.1 Daily Monitoring (SOC Responsibility)

SOC analysts SHALL perform daily monitoring:

**Morning Review (30 minutes):**
- Review Critical/High alerts from previous 24 hours
- Triage alerts (validate vs. false positive vs. policy violation vs. incident)
- Escalate incidents to Incident Response team (S2.4)
- Document triage decisions (alert disposition, justification)

**Real-Time Monitoring:**
- Monitor SIEM dashboard for incoming Critical alerts
- Respond within SLA (Critical: 15 min, High: 1 hour)

### 6.2 Weekly Monitoring (Security Team)

Security team SHALL perform weekly analysis:

**Trend Analysis:**
- Top blocked users (identify repeat offenders, potential insider threats)
- Top blocked data categories (PII, financial, IP - understand risk areas)
- Top blocked channels (email, USB, web - identify unprotected attack vectors)
- False positive patterns (identify systemic tuning opportunities)

**User Education Opportunities:**
- Identify users with >5 violations/week (targeted training)
- Identify departments with high violation rates (department-wide training)

### 6.3 Monthly Monitoring (Management Reporting)

Security management SHALL generate monthly reports:

**Executive Summary:**
- Total DLP events (allows, blocks, alerts)
- Critical incidents (data exfiltration attempts, credential leaks)
- False positive rate trend (improving, stable, degrading)
- Top risks (users, departments, data categories, channels)

**Operational Metrics:**
- DLP system uptime and performance
- Alert response SLA compliance (% of alerts triaged within SLA)
- Investigation backlog (open alerts >7 days old)
- Policy coverage (% of sensitive data protected)

### 6.4 Quarterly Monitoring (Strategic Review)

CISO/Security Director SHALL conduct quarterly strategic review:

**Risk Assessment:**
- Emerging threats (new exfiltration techniques, insider threat trends)
- Policy effectiveness (are we detecting actual incidents?)
- Coverage gaps (unprotected channels, data types, user populations)
- Compliance posture (FADP/GDPR, audit findings)

**Continuous Improvement:**
- Lessons learned from incidents
- Technology enhancements (new DLP capabilities, ML improvements)
- Training effectiveness (has user behavior improved?)
- ROI analysis (prevented incidents vs. DLP cost)

---

## 7. SIEM and SOC Integration

### 7.1 SIEM Integration Requirements

DLP logs SHALL be forwarded to organizational SIEM for:

**Correlation with Other Security Events:**
- DLP block + malware detection = compromised endpoint exfiltrating data
- DLP alert + failed login attempts = credential theft attempt
- DLP alert + VPN from foreign country = potential account compromise
- DLP alert + HR termination record = departing employee data theft

**Unified Incident Response:**
- Single pane of glass for SOC (DLP + EDR + Network + Email + IAM)
- Automated playbooks (if DLP Critical alert + malware = isolate endpoint)

### 7.2 SIEM Use Cases

Organizations SHOULD implement SIEM correlation rules:

**Use Case 1: Insider Threat Detection**
```
IF (User = "departing_employee" OR User.termination_date < 30_days)
AND (DLP_alerts > 5 in 24_hours OR Mass_file_transfer > 1GB)
THEN Alert(Severity=Critical, Title="Potential Insider Threat: Departing Employee Data Exfiltration")
```

**Use Case 2: Compromised Credentials**
```
IF (DLP_credential_detected_outbound)
AND (Failed_logins_from_unusual_location > 3 in 1_hour)
THEN Alert(Severity=Critical, Title="Credential Compromise + Exfiltration Attempt")
```

**Use Case 3: Mass Data Exfiltration**
```
IF (DLP_files_blocked > 100 in 10_minutes)
OR (DLP_volume_blocked > 10GB in 1_hour)
THEN Alert(Severity=Critical, Title="Mass Data Exfiltration Attempt - Potential Ransomware/Insider")
```

### 7.3 SOC Playbooks

Organizations SHALL define SOC playbooks for DLP alerts:

**Critical Alert Playbook:**
1. Validate alert (not false positive)
2. Identify user (employee, contractor, service account)
3. Check user context (recent HR events, access changes)
4. Correlate with other events (malware, unusual logins, network anomalies)
5. Containment decision (block user, disable account, isolate endpoint)
6. Escalate to Incident Response (S2.4)

**High Alert Playbook:**
1. Validate alert
2. Contact user manager (verify business justification)
3. Request exception approval or educate user
4. Document decision
5. Escalate if suspicious

---

## 8. Dashboards and Reporting

### 8.1 Real-Time Dashboards

Organizations SHALL implement real-time DLP dashboards:

**SOC Dashboard (Real-Time):**
- Alert queue (Critical/High/Medium pending triage)
- Alert volume over time (last 24 hours, hourly buckets)
- Top blocked users (last 24 hours)
- Top blocked channels (email, USB, web, network)
- False positive rate (rolling 7-day average)

**Executive Dashboard (Updated Daily):**
- Critical incidents (last 30 days)
- DLP effectiveness (prevented incidents, blocked volume)
- Compliance metrics (coverage %, policy enforcement rate)
- Risk heatmap (users, departments, data categories, channels)

### 8.2 Scheduled Reports

Organizations SHALL generate scheduled reports:

**Weekly Report (Security Team):**
- Alert summary (Critical/High/Medium/Low counts)
- Top users by alert volume
- Top data categories detected
- False positive trend
- Open investigations

**Monthly Report (Management):**
- Executive summary (1-page, business language)
- Incident summary (critical events, resolved vs. ongoing)
- DLP effectiveness metrics (prevented exfiltration, policy compliance)
- Recommendations (policy updates, training needs, technology enhancements)

**Quarterly Report (CISO/Board):**
- Strategic risk assessment (emerging threats, insider risk trends)
- Compliance posture (FADP/GDPR, audit findings)
- ROI analysis (prevented incident value vs. DLP cost)
- Future roadmap (planned improvements, budget requests)

---

## 9. Performance and Scalability

### 9.1 Logging Performance

DLP logging SHALL NOT degrade system performance:

**Performance Targets:**
- Logging overhead <5% CPU utilization
- Log write latency <50ms (do not block data transfers while writing logs)
- Asynchronous logging (buffer logs, write in batches)

### 9.2 Storage Scalability

Organizations SHALL plan for log storage growth:

**Storage Planning:**
- Estimate log volume (events/day × average event size × retention period)
- Provision storage with 30% headroom
- Implement tiered storage (hot: 30 days SSD, warm: 31-90 days HDD, cold: 91-365 days archive)
- Monitor storage utilization, alert at 80% capacity

**Example Calculation:**
```
Users: 1,000
Events per user per day: 50 (email, web, USB, network)
Event size: 2KB (JSON structured log)
Retention: 365 days

Storage = 1,000 users × 50 events/day × 2KB × 365 days = 36.5 GB/year
With 30% headroom = 48 GB/year provisioned
```

### 9.3 Analysis Scalability

Organizations SHALL ensure log analysis systems scale:

**Indexing:**
- Index logs for fast search (Elastic, Splunk, etc.)
- Optimize queries (avoid full-table scans, use indexed fields)

**Sampling:**
- For extremely high-volume environments (>1M events/day), consider sampling for analytics
- Always log Critical/High alerts (never sample security events)
- Sample Low/Informational events for trend analysis

---

## 10. Continuous Improvement

### 10.1 Lessons Learned

Organizations SHALL conduct lessons learned after major incidents:

**Post-Incident Review:**
- What happened? (timeline, root cause)
- What did DLP detect? (did alerts fire correctly?)
- What did DLP miss? (gaps in coverage, detection)
- What were the false positives? (unnecessary noise during incident)
- How can we improve? (new rules, policy changes, training)

**Documentation:**  
Lessons learned SHALL be documented in incident reports and used to update DLP policies, rules, and training.

### 10.2 Threat Intelligence Integration

Organizations SHOULD integrate external threat intelligence:

**Sources:**
- Vendor threat feeds (DLP vendor threat intelligence)
- OSINT (GitHub secret scanning, leaked credential databases)
- Industry sharing (ISAC, CERT, sector-specific groups)

**Use Cases:**
- Update detection patterns (new credential formats, new exfiltration techniques)
- Enhance SIEM correlation (known attacker IPs, malicious cloud infrastructure)

---

## 11. Integration with DLP Framework

### 11.1 Assessment Integration

Monitoring and detection SHALL be assessed using **ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)** workbook, evaluating:
- Logging completeness (all channels logging correctly)
- SIEM integration status (logs forwarded, correlation rules deployed)
- Alert response SLA compliance (% of alerts triaged within SLA)
- False positive rate (trend, target achievement)
- Dashboard/reporting implementation

### 11.2 Incident Response Integration

Monitoring feeds directly into **S2.4 (Incident Response & Remediation)**:
- Alerts generate incidents
- SOC triage determines severity
- Incident Response handles Critical/High alerts
- Remediation closes the loop (fix gaps, tune rules, educate users)

---

## 12. References

### 12.1 Internal Policy Documents

- **ISMS-POL-A.8.12** - Master DLP Policy
- **ISMS-POL-A.8.12-S2.2** - Channel Protection Requirements
- **ISMS-POL-A.8.12-S2.4** - Incident Response & Remediation
- **ISMS-POL-A.8.15** - Logging (organizational control)
- **ISMS-POL-A.8.10** - Information Deletion (data retention)

### 12.2 Implementation Documents

- **ISMS-IMP-A.8.12.4** - Monitoring & Response Assessment

### 12.3 Regulatory References

- **ISO/IEC 27002:2022** - Control 8.15 (Logging), Control 8.16 (Monitoring)
- **Swiss FADP** - Article 26 (Employee data processing), Article 8 (Data security)
- **Swiss Employment Law** - Article 328b CO (Proportionality in employee monitoring)
- **EU GDPR** - Article 5 (Lawfulness, fairness, transparency), Article 32 (Security of processing)

---

**END OF DOCUMENT**

*"The difference between a good SOC and a great SOC: A good SOC detects incidents. A great SOC tunes away the noise so they can actually investigate."*  
*— The Wisdom of Alert Fatigue Survivors*