# ISMS-POL-A.8.15-S5.C
## Log Review Procedures

**Document ID**: ISMS-POL-A.8.15-S5.C  
**Title**: Log Review Procedures  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Security Operations Center (SOC) Lead  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC Lead / Security Analyst | Initial procedures |

**Review Cycle**: Quarterly (or after significant process changes)  
**Next Review Date**: [Approval Date + 3 months]  
**Approvers**: SOC Lead, Information Security Manager  
**Distribution**: SOC analysts, security team, incident responders

---

## C.1 Daily Log Review Procedures

### C.1.1 Purpose
Detect security incidents and policy violations through daily review of critical security logs.

### C.1.2 Frequency
Every business day (Monday-Friday, or 7 days/week for 24x7 SOCs)

### C.1.3 Responsible Party
SOC Analyst (designated daily reviewer)

### C.1.4 Time Required
30-60 minutes (small environment), 2-4 hours (large environment)

### C.1.5 Procedure Steps

**Step 1: Open SIEM Dashboard** (5 minutes)
1. Log into SIEM platform with individual account (no shared accounts)
2. Open "Daily Security Review" dashboard
3. Verify dashboard data is current (check last update timestamp)
4. Note any SIEM platform alerts or health issues

**Step 2: Review Critical Security Alerts** (15-30 minutes)
1. **Review High/Critical Severity Alerts**:
   - Sort by severity (Critical, High first)
   - For each alert:
     - Determine if true positive or false positive
     - If true positive: Initiate incident investigation (see C.4)
     - If false positive: Document reason, tune rule if pattern
   - Document all alerts reviewed in incident tracking system

2. **Priority Alert Types** (focus here first):
   - Malware detections (anti-malware, EDR alerts)
   - C2 communication attempts (critical - always investigate)
   - Failed authentication spikes (10+ failures in 1 hour)
   - Privileged access outside business hours
   - Data exfiltration indicators (large outbound transfers)
   - Critical system configuration changes

**Step 3: Review Authentication Logs** (10-15 minutes)
1. **Failed Authentication Review**:
   - Query: Failed logins in last 24 hours
   - Look for:
     - Multiple failures from same source IP (brute force)
     - Multiple failures across multiple accounts (password spraying)
     - Failed logins for administrative accounts
     - Failed logins from unusual locations/IPs
   - **Action if suspicious**: Create incident ticket, investigate further

2. **Successful Authentication Review**:
   - Query: Successful logins for administrative/privileged accounts
   - Look for:
     - Logins at unusual times (nights, weekends)
     - Logins from unusual locations
     - Logins for recently terminated accounts (should be disabled)
   - **Action if suspicious**: Verify with account owner, investigate if cannot confirm

**Step 4: Review Administrative Activities** (10-15 minutes)
1. **User Account Changes**:
   - Query: User accounts created, deleted, modified in last 24 hours
   - Verify each change is authorized:
     - Check against HR notifications (new hires, terminations)
     - Check against change tickets
   - **Action if unauthorized**: Escalate immediately (potential compromise)

2. **Privilege Escalation**:
   - Query: Users granted administrative privileges in last 24 hours
   - Verify each privilege grant is authorized
   - **Action if unauthorized**: Escalate immediately, revoke access

3. **Critical Configuration Changes**:
   - Query: Changes to security systems (firewall, SIEM, AD, etc.)
   - Verify changes authorized via change management
   - **Action if unauthorized**: Investigate, escalate

**Step 5: Review Security Tool Events** (10-15 minutes)
1. **Firewall Blocks**:
   - Review unusual blocked traffic (not routine port scans)
   - Look for:
     - Internal systems blocked (potential lateral movement)
     - High-volume blocks from single source (potential attack)
     - Blocks to unusual ports/protocols
   - **Action if suspicious**: Investigate source and destination

2. **Web Filtering Blocks**:
   - Review malware/phishing site blocks
   - Look for:
     - Repeated access attempts to malicious sites
     - Multiple users accessing same malicious site (potential campaign)
   - **Action if pattern detected**: Investigate, send user awareness notice

3. **DLP Alerts** (if applicable):
   - Review data loss prevention policy violations
   - Verify if legitimate business activity or policy violation
   - **Action if violation**: Notify user's manager, document incident

**Step 6: Document Review** (5 minutes)
1. Complete daily log review checklist (template below)
2. Document findings in log review report
3. Create incident tickets for items requiring investigation
4. Note any trends or patterns for weekly review

**Step 7: Escalation** (as needed)
- **Critical Findings**: Escalate immediately to SOC Lead
- **High Findings**: Escalate same day to SOC Lead
- **Medium Findings**: Create ticket, investigate within 4 hours
- **Low Findings**: Create ticket, investigate next business day

### C.1.6 Daily Review Checklist Template
```
DAILY LOG REVIEW CHECKLIST
Date: __________
Reviewer: __________
Time Started: __________ Time Completed: __________

[ ] SIEM Dashboard accessed and verified current
[ ] Critical/High severity alerts reviewed (count: ___)
    - True positives: ___
    - False positives: ___
    - Incidents created: ___
[ ] Failed authentication logs reviewed
    - Suspicious patterns identified: Yes / No
    - Action taken: _______________________
[ ] Administrative activities reviewed
    - Unauthorized changes identified: Yes / No
    - Action taken: _______________________
[ ] Security tool events reviewed
    - Notable events: _____________________
[ ] Documentation completed (incident tickets, notes)

Significant Findings:
_____________________________________________
_____________________________________________

Escalations:
[ ] None
[ ] SOC Lead notified (reason: ______________)
[ ] CISO notified (reason: ______________)

Reviewer Signature: __________
```

---

## C.2 Weekly Log Review Procedures

### C.2.1 Purpose
Identify trends, patterns, and anomalies not apparent in daily reviews.

### C.2.2 Frequency
Weekly (recommended: Monday morning reviewing previous week)

### C.2.3 Responsible Party
SOC Analyst or SOC Lead (senior analyst)

### C.2.4 Time Required
1-2 hours

### C.2.5 Procedure Steps

**Step 1: Trend Analysis** (30 minutes)
1. **Authentication Trend Analysis**:
   - Compare failed login attempts this week vs. previous 4 weeks
   - Identify accounts with increasing failure rates
   - Identify new IP addresses attempting authentication
   - Graph: Failed logins by day (spot spikes)

2. **Security Alert Trend Analysis**:
   - Compare alert volumes this week vs. previous 4 weeks
   - Identify alert types increasing in volume
   - Identify new threat patterns
   - Calculate false positive rate (target: <10%)

3. **User Activity Trend Analysis**:
   - Identify users with unusual activity patterns
   - After-hours access trends
   - Data access volume trends
   - Geographic access patterns (unusual locations)

**Step 2: Top 10 Analysis** (20 minutes)
1. **Top 10 Users by Failed Logins**:
   - Are these legitimate users struggling with passwords?
   - Or potential attack targets?
   - Action: Send password reset reminder to top users

2. **Top 10 Source IPs by Security Events**:
   - Are these internal or external?
   - Are these known attackers or scanning services?
   - Action: Block repeat offenders if appropriate

3. **Top 10 Blocked Websites/Domains**:
   - Are these legitimate sites miscategorized?
   - Or malicious sites users attempting to access?
   - Action: Recategorize if needed, investigate repeated attempts

4. **Top 10 Users by Data Access Volume**:
   - Is this consistent with job role?
   - Potential data exfiltration?
   - Action: Investigate outliers

**Step 3: Administrative Activity Review** (20 minutes)
1. **Weekly Change Summary**:
   - All user account changes (created, deleted, modified)
   - All privilege grants/revocations
   - All critical system configuration changes
   - Verify changes align with change tickets

2. **Unused Privileged Accounts**:
   - Identify administrative accounts not used in past week
   - Consider revoking unused privileges (least privilege principle)

**Step 4: System Health Review** (20 minutes)
1. **Log Collection Health**:
   - Identify any log sources not forwarding logs
   - Check for gaps in log data (missing hours/days)
   - Verify all critical systems logging
   - Action: Fix broken log forwarders, notify system owners

2. **SIEM Performance**:
   - Check SIEM storage utilization (alert if >70%)
   - Check SIEM query performance (slow queries?)
   - Check parsing errors (unparsed logs?)

**Step 5: Report Generation** (10 minutes)
1. Generate weekly security report:
   - Total incidents detected this week
   - Top threats/attack types
   - Top false positive sources
   - Log collection health
   - Recommendations for improvements

2. Distribute report to:
   - SOC Lead
   - Information Security Manager
   - File in log review documentation

---

## C.3 Monthly Log Review Procedures

### C.3.1 Purpose
Strategic analysis for management reporting and continuous improvement.

### C.3.2 Frequency
Monthly (recommended: First week of new month, reviewing previous month)

### C.3.3 Responsible Party
SOC Lead or Information Security Manager

### C.3.4 Time Required
2-4 hours (analysis + report preparation)

### C.3.5 Procedure Steps

**Step 1: Monthly Metrics Calculation** (60 minutes)
1. **Detection Metrics**:
   - Total incidents detected
   - Mean Time to Detect (MTTD)
   - Incidents by severity (Critical, High, Medium, Low)
   - Incidents by type (malware, intrusion, policy violation, etc.)

2. **Response Metrics**:
   - Mean Time to Respond (MTTR)
   - Percentage of incidents responded to within SLA
   - Incident closure time

3. **Compliance Metrics**:
   - Log source coverage (% of systems logging)
   - Log review compliance (% of reviews completed on schedule)
   - Retention compliance (% of logs meeting retention requirements)

4. **Quality Metrics**:
   - False positive rate
   - Alert quality score (true positives / total alerts)
   - Detection rule effectiveness

**Step 2: Month-over-Month Comparison** (30 minutes)
1. Compare all metrics to previous month
2. Identify improving trends (celebrate successes)
3. Identify declining trends (root cause analysis)
4. Year-over-year comparison (if data available)

**Step 3: Gap Identification** (30 minutes)
1. Review incident investigations:
   - Were there detection gaps (attacks not detected)?
   - Were logs sufficient for investigation?
   - What additional log sources would help?

2. Review false positives:
   - Which rules generate most false positives?
   - Can they be tuned?
   - Should they be disabled?

3. Review coverage gaps:
   - Which systems still not logging?
   - What's the risk?
   - What's the remediation plan?

**Step 4: Management Report Preparation** (60 minutes)
1. **Executive Summary** (1 page):
   - Key findings
   - Top threats detected
   - Significant incidents
   - Recommendations

2. **Detailed Metrics** (2-3 pages):
   - Charts and graphs of all metrics
   - Month-over-month trends
   - Compliance status

3. **Action Items** (1 page):
   - Gaps requiring remediation
   - Recommendations for improvement
   - Resource requests (if needed)

**Step 5: Management Presentation** (30-60 minutes)
- Present report to CISO or Security Steering Committee
- Discuss findings and recommendations
- Obtain approval for action items

---

## C.4 Incident Investigation Procedures

### C.4.1 Purpose
Investigate security incidents identified through log review.

### C.4.2 Trigger
Security event requiring investigation (alert, suspicious pattern, user report)

### C.4.3 Responsible Party
SOC Analyst (initial investigation), escalate to Incident Response Team for major incidents

### C.4.4 Procedure Steps

**Step 1: Initial Triage** (5-15 minutes)
1. **Create Incident Ticket**:
   - Incident ID: [auto-generated]
   - Severity: [Critical / High / Medium / Low]
   - Type: [Malware / Intrusion / Policy Violation / Other]
   - Detected by: [Alert / Manual Review / User Report]
   - Brief description

2. **Initial Assessment**:
   - Is this a true positive or false positive?
   - What is the potential impact?
   - Is this ongoing or historical?
   - Does this require immediate containment?

3. **Escalation Decision**:
   - P1 Critical: Escalate immediately to Incident Response Team
   - P2 High: Notify SOC Lead, proceed with investigation
   - P3 Medium: Proceed with investigation
   - P4 Low: Document for next business day review

**Step 2: Evidence Gathering** (30-60 minutes)
1. **Collect Relevant Logs**:
   - Identify affected systems (victim, attacker, related systems)
   - Collect logs from time window (before, during, after event)
   - Export logs for preservation (in case of retention expiration)

2. **Timeline Construction**:
   - What happened first?
   - What happened next?
   - When did it end (or is it ongoing)?

3. **Scope Assessment**:
   - How many systems affected?
   - How many users affected?
   - What data potentially compromised?

**Step 3: Analysis** (varies by incident complexity)
1. **Root Cause Analysis**:
   - How did attacker gain access?
   - What vulnerabilities were exploited?
   - What systems were compromised?

2. **Impact Assessment**:
   - What data was accessed/stolen/modified?
   - What systems were compromised?
   - What is the business impact?

3. **Indicators of Compromise (IOCs)**:
   - IP addresses involved
   - File hashes (malware)
   - Domains/URLs accessed
   - User accounts involved

**Step 4: Containment** (immediate for P1/P2)
1. **Isolate Compromised Systems**:
   - Disconnect from network (if safe to do so)
   - Disable compromised user accounts
   - Block malicious IP addresses at firewall

2. **Preserve Evidence**:
   - Take disk images of compromised systems
   - Preserve memory dumps
   - Export all relevant logs

**Step 5: Eradication** (after containment)
1. **Remove Malware**:
   - Anti-malware scan and clean
   - Manual removal if necessary
   - Rebuild system if heavily compromised

2. **Close Attack Vectors**:
   - Patch vulnerabilities
   - Update configurations
   - Strengthen access controls

**Step 6: Recovery** (after eradication)
1. **Restore Systems**:
   - Restore from clean backup (if needed)
   - Verify system clean before reconnecting to network
   - Reset credentials

2. **Monitor for Reinfection**:
   - Enhanced monitoring for 7-14 days
   - Watch for IOCs reappearing

**Step 7: Documentation** (throughout investigation)
1. **Incident Report**:
   - Timeline of events
   - Systems affected
   - Data compromised
   - Actions taken (containment, eradication, recovery)
   - Root cause
   - Lessons learned

2. **Post-Incident Review**:
   - What worked well?
   - What could be improved?
   - Detection gaps identified?
   - Policy/procedure updates needed?

---

## C.5 Forensic Investigation Procedures

### C.5.1 Purpose
Conduct forensic analysis of security incidents for legal proceedings or detailed investigation.

### C.5.2 When to Use
- Law enforcement investigation
- Insider threat investigation
- Major data breach
- Incident requiring legal evidence

### C.5.3 Chain of Custody Requirements

**All evidence SHALL**:
1. Be documented from collection to disposal
2. Be handled only by authorized personnel
3. Be stored securely (encrypted, access-controlled)
4. Have integrity verified (cryptographic hashes)

**Chain of Custody Log** (for each evidence item):
- Evidence ID
- Description
- Collection date/time
- Collected by (name, signature)
- Custody transfers (from → to, date, signatures)
- Storage location
- Hash values (MD5, SHA-256)

### C.5.4 Evidence Collection

**Log Evidence**:
1. Export logs covering incident timeframe
2. Export extended timeframe (before/after for context)
3. Generate cryptographic hashes of exported logs
4. Store on write-once media (WORM, CD-R, signed PDF)
5. Document collection process

**System Evidence** (if needed):
1. Disk images (forensic imaging tools)
2. Memory dumps
3. Network packet captures
4. Configuration files

**Documentation**:
1. Who collected evidence
2. When and where collected
3. Methods used
4. Tools used (versions)
5. Hash values

### C.5.5 Analysis

**Forensic Analysis** (typically by specialist):
1. Use forensic workstation (isolated, clean environment)
2. Work only on copies (never original evidence)
3. Document all analysis steps
4. Generate timeline of events
5. Identify indicators of compromise
6. Prepare forensic report

### C.5.6 Legal Considerations

**Consult Legal Counsel**:
- Before collecting evidence from personal devices
- Before sharing evidence with law enforcement
- Before sharing evidence with third parties
- If evidence may be used in legal proceedings

**Admissibility Requirements**:
- Proper chain of custody
- Proper collection methods
- Expert testimony may be required

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S5.C |
| **Document Type** | Annex - Procedures |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~395 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |

---

**END OF ANNEX C**