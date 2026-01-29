# ISMS-POL-A.8.23-S5.C
## Web Filtering - Incident Response Procedures

**Document ID**: ISMS-POL-A.8.23-S5.C
**Title**: Web Filtering Incident Response Procedures  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal (or Confidential - contains response details)  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / SOC Lead / Incident Response Team | Initial IR procedures |

**Review Cycle**: Semi-annual (or following major incidents or IR plan updates)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Review: Security Operations Center (SOC) Lead
- IR Coordination: Incident Response Manager / Team Lead
- Compliance: Legal/Compliance Officer (for notification requirements)

**Distribution**: Security team, SOC analysts, incident response team (restricted access)  
**Related Documents**: Master Incident Response Plan, ISMS-IMP-A.8.23.4 (Monitoring Assessment)
---

## C.1 Purpose and Scope

This annex defines **incident response procedures** for security events detected or managed by web filtering solutions, implementing requirements from policy sections S2.1 (Threat Protection) and S2.3 (Logging & Monitoring).

**Purpose**:
- Provide step-by-step response procedures for web filtering incidents
- Define severity classification and escalation criteria
- Ensure consistent, effective incident handling
- Support incident investigation and forensics
- Enable continuous improvement through lessons learned

**Scope**: All security incidents involving web filtering controls, including:
- Malware/phishing detection and blocking
- Command & Control (C2) communication attempts
- Policy violations and bypass attempts
- Web filtering system failures or compromises
- False positives/negatives requiring investigation

**Audience**: Security Team, SOC, IT Operations, Incident Response Team

**Integration**: These procedures integrate with organization-wide Incident Response Plan

---

## C.2 Incident Classification

### C.2.1 Severity Levels

Web filtering incidents are classified into four severity levels:

#### CRITICAL (P1)

**Definition**: Incident poses immediate, severe threat to organizational security or operations

**Examples**:
- **C2 Communication Detected**: System attempting to contact command-and-control infrastructure (indicates active compromise)
- **Mass Malware Outbreak**: Multiple systems attempting to access malware distribution sites simultaneously
- **Web Filtering System Compromise**: Filtering solution itself has been compromised
- **Complete Filtering Failure**: All web filtering protection disabled or bypassed organization-wide

**Response Time**: Immediate (within 15 minutes)  
**Escalation**: CISO notified within 1 hour, Executive Management within 4 hours if impact confirmed  
**Business Impact**: High - potential for data breach, system compromise, operational disruption

---

#### HIGH (P2)

**Definition**: Incident represents significant security threat requiring urgent response

**Examples**:
- **Repeated Malware/Phishing Blocks**: Single user/system with multiple malware blocks (possible infection)
- **Targeted Phishing Campaign**: Multiple users targeted by coordinated phishing attack
- **Policy Bypass Attempts**: Repeated attempts to circumvent web filtering controls
- **Partial System Failure**: Web filtering degraded but not completely failed
- **Critical False Negative**: Known malicious site not blocked (filtering gap)

**Response Time**: Within 1 hour (business hours), 2 hours (after hours)  
**Escalation**: Security Team Lead notified immediately, CISO within 4 hours  
**Business Impact**: Medium-High - potential for compromise, requires investigation

---

#### MEDIUM (P3)

**Definition**: Incident requires investigation but does not pose immediate severe threat

**Examples**:
- **Single Malware/Phishing Block**: One-off blocking event for single user
- **Anomalous Web Access Pattern**: Unusual but not clearly malicious activity
- **Moderate False Positive Rate**: Legitimate sites incorrectly blocked (usability impact)
- **Policy Violation**: User accessing prohibited content (non-malicious)
- **Performance Degradation**: Filtering system slow but operational

**Response Time**: Within 4 hours (business hours), next business day (after hours)  
**Escalation**: Security Team Lead notified daily summary  
**Business Impact**: Low-Medium - investigation needed, low immediate risk

---

#### LOW (P4)

**Definition**: Informational events or minor issues requiring documentation and routine follow-up

**Examples**:
- **Expected Blocks**: Normal blocking of known bad sites (no user impact)
- **Single False Positive**: One-off miscategorization (quickly resolved)
- **Configuration Change**: Routine policy update or maintenance
- **User Support Request**: General question or assistance request
- **Trend Analysis Findings**: Patterns identified in periodic reviews

**Response Time**: As time permits, within 3 business days  
**Escalation**: None (documented in routine reports)  
**Business Impact**: Minimal - informational or routine

---

### C.2.2 Severity Assessment Criteria

When classifying incidents, consider:

**Threat Severity**:
- Type of threat (C2 > Malware > Phishing > Category violation)
- Known exploitation or active attack
- Potential for data breach or system compromise

**Scope**:
- Number of affected users/systems
- Criticality of affected systems (servers, executives, high-value targets)
- Organizational impact (operations, reputation, compliance)

**Urgency**:
- Active ongoing attack vs. historical detection
- Time-sensitive response requirements
- Potential for threat propagation

**Evidence Quality**:
- High confidence detection vs. potential false positive
- Corroborating evidence from other security controls
- Threat intelligence validation

---

## C.3 Incident Response Workflow

### C.3.1 General Response Process

All web filtering incidents follow this general workflow:

1. **DETECTION** → Alert generated by web filtering system or identified through monitoring
2. **TRIAGE** → Security Team validates alert, classifies severity, assigns incident ID
3. **CONTAINMENT** → Immediate actions to prevent spread or mitigate impact
4. **INVESTIGATION** → Determine root cause, scope, and impact
5. **REMEDIATION** → Remove threat, restore normal operations, implement fixes
6. **RECOVERY** → Verify systems are clean and secure, resume normal operations
7. **POST-INCIDENT** → Document lessons learned, update policies/procedures

---

## C.4 Response Procedures by Incident Type

### C.4.1 C2 Communication Attempt (CRITICAL)

**Indicators**:
- Web filtering blocks connection to known C2 infrastructure
- Alert: "Command & Control communication blocked"
- User/system attempting to contact botnet, RAT, or APT infrastructure

**Immediate Actions** (within 15 minutes):

1. **Isolate Affected System**:
   - Disconnect from network immediately (physical or logical isolation)
   - Do NOT shut down (preserve memory for forensics)
   - Block system at firewall/switch level

2. **Alert Security Team and CISO**:
   - Page on-call security personnel
   - Initiate CRITICAL incident response
   - Notify CISO within 1 hour

3. **Gather Initial Evidence**:
   - Web filtering logs (C2 connection attempts, timestamps, URLs)
   - User identity and system information
   - Endpoint logs (if available without disrupting forensics)
   - Network traffic logs (identify other connections)

**Investigation** (within 4 hours):

4. **Endpoint Forensics**:
   - Deploy EDR/forensic tools to isolated system
   - Image memory and disk for analysis
   - Identify malware or backdoor
   - Determine infection vector (email, web, USB, lateral movement)

5. **Scope Assessment**:
   - Check for C2 attempts from other systems (historical log analysis)
   - Identify lateral movement indicators
   - Check for data exfiltration attempts
   - Assess what data/systems the compromised system could access

6. **Threat Intelligence**:
   - Research C2 infrastructure (known campaigns, attribution)
   - Check IOCs against threat intelligence feeds
   - Identify attack patterns and TTPs

**Remediation**:

7. **Eradicate Threat**:
   - Remove malware/backdoor from affected system
   - Reset compromised credentials
   - Apply security patches if vulnerability exploited
   - Consider full system rebuild for high-confidence clean state

8. **Block IOCs Organization-Wide**:
   - Add C2 domains/IPs to blocklist
   - Update web filtering and firewall rules
   - Update endpoint protection signatures

9. **Credential Reset**:
   - Force password reset for affected user
   - Review privileged account access
   - Enable MFA if not already enforced

**Recovery**:

10. **System Restoration**:
    - Verify system is clean (multiple scans, behavioral monitoring)
    - Restore to network under enhanced monitoring
    - Monitor for 30 days for re-infection indicators

**Escalation**: Report to Executive Management if:
- Multiple systems compromised
- Data exfiltration confirmed
- High-value system affected (servers, executives, finance)
- Regulatory notification required

---

### C.4.2 Malware Distribution Site Access (HIGH)

**Indicators**:
- User/system blocked attempting to access malware distribution site
- Multiple blocks from same user/system (repeated attempts)

**Immediate Actions** (within 1 hour):

1. **Validate Alert**:
   - Confirm blocking was legitimate (not false positive)
   - Check threat intelligence for site reputation
   - Review user's recent web activity

2. **Check for Infection**:
   - Scan endpoint for malware (full AV/EDR scan)
   - Review endpoint logs for suspicious activity
   - Check for successful downloads before blocking

3. **User Contact**:
   - Contact user to understand context
   - "Did you intentionally visit this site? What were you trying to access?"
   - Assess if user was socially engineered (phishing link, malvertising)

**Investigation**:

4. **Determine Root Cause**:
   - If intentional: Security awareness issue (refer to training)
   - If unintentional: Likely phishing victim or malvertising
   - If automated: Malware already present (escalate to CRITICAL)

5. **Assess Impact**:
   - Was malware downloaded before block?
   - Check browser cache, downloads folder
   - Review network logs for suspicious connections

**Remediation**:

6. **If No Infection Found**:
   - Document incident (legitimate block, no compromise)
   - Provide security awareness guidance to user
   - Close incident as "Prevented Threat"

7. **If Infection Found**:
   - Escalate to CRITICAL (follow C2 procedures)
   - Isolate, investigate, remediate per malware response procedures

---

### C.4.3 Phishing Site Access (HIGH)

**Indicators**:
- User blocked attempting to access known phishing site
- Multiple users targeted by same phishing campaign

**Immediate Actions** (within 1 hour):

1. **User Interview**:
   - How did user arrive at phishing site? (email link, search result, typo)
   - Did user enter credentials or sensitive information?
   - Urgency: If credentials entered, immediate action required

2. **Credential Reset** (if credentials compromised):
   - Force password reset immediately
   - Revoke active sessions
   - Enable MFA if not already active
   - Monitor account for unauthorized access

3. **Check for Campaign**:
   - Search logs for other users accessing same phishing site
   - If multiple users: Phishing campaign targeting organization
   - Escalate to organization-wide alert

**Investigation**:

4. **Email Analysis** (if phishing link from email):
   - Obtain original phishing email
   - Identify sender, subject, content
   - Check email gateway logs (did it bypass filters?)
   - Extract IOCs (sender domain, URLs, attachments)

5. **Scope Assessment**:
   - How many users received phishing email?
   - How many clicked link?
   - How many entered credentials?

**Remediation**:

6. **Block Phishing Infrastructure**:
   - Add phishing URLs to web filtering blocklist
   - Update email gateway rules
   - Report to phishing database (PhishTank, vendor threat intel)

7. **User Communication**:
   - Alert affected users (if targeted campaign)
   - Remind of phishing indicators
   - Report suspicious emails to Security Team

8. **Security Awareness**:
   - Use incident as training opportunity (anonymized example)
   - Update security awareness materials if new tactics observed

---

### C.4.4 Policy Bypass Attempt (MEDIUM-HIGH)

**Indicators**:
- User attempting to use proxy/VPN to bypass filtering
- Multiple failed attempts to access blocked sites
- Use of anonymization tools detected

**Immediate Actions** (within 2 hours):

1. **Validate Bypass Attempt**:
   - Review logs (is user trying to circumvent controls?)
   - Determine method (proxy site, personal VPN, Tor, DNS tunneling)

2. **User Contact**:
   - Contact user (understand intent - malicious vs. unaware)
   - Explain policy and risks
   - Determine if legitimate business need (exception process)

**Investigation**:

3. **Assess Intent**:
   - **Unaware**: User didn't know bypass was prohibited → Education
   - **Frustrated**: User has legitimate need → Exception process (S2.4)
   - **Malicious**: Intentional policy violation → Escalate to HR

4. **Check for Success**:
   - Did bypass succeed (gap in filtering)?
   - What sites did user access via bypass?
   - Any security incidents while bypassed?

**Remediation**:

5. **Technical Controls**:
   - Block proxy/VPN services used
   - Close filtering gaps identified
   - Enhance detection for bypass methods

6. **Policy Enforcement**:
   - **First offense**: Verbal warning, education
   - **Repeated offense**: Written warning, manager notification
   - **Severe/malicious**: Disciplinary action per HR policy (suspension, termination)

7. **Exception Offer** (if legitimate need):
   - Guide user to exception request process (S2.4, Annex B)
   - Explain proper channels for policy deviations

---

### C.4.5 Web Filtering System Failure (CRITICAL-HIGH)

**Indicators**:
- Web filtering unavailable or degraded
- Alerts not generating
- Users report unrestricted internet access
- Monitoring shows traffic bypassing filters

**Immediate Actions** (within 30 minutes):

1. **Assess Scope**:
   - Complete failure or partial degradation?
   - Which network segments affected?
   - Fail-open or fail-closed behavior? (S2.1)

2. **Implement Interim Controls** (if fail-open):
   - Enhanced endpoint protection alerting
   - Firewall rule adjustments (block known bad IPs/domains)
   - DNS filtering as backup (if available)
   - User notification (exercise caution)

3. **Engage Vendor Support**:
   - Open CRITICAL support ticket
   - Provide logs and diagnostic information
   - Request engineer engagement

**Investigation**:

4. **Root Cause Analysis**:
   - Hardware failure?
   - Software bug or misconfiguration?
   - Capacity exceeded?
   - Attack on filtering system itself?

5. **Timeline Assessment**:
   - When did failure occur?
   - What traffic was unfiltered during outage?
   - Any security incidents during unprotected period?

**Remediation**:

6. **Restore Service**:
   - Apply vendor fix or workaround
   - Failover to redundant system (if available)
   - Restore from backup configuration
   - Verify filtering is operational (test blocks)

7. **Post-Outage Security Check**:
   - Analyze logs from failure period for threats
   - Scan endpoints for infections acquired during outage
   - Review anomalous traffic patterns

**Recovery**:

8. **Preventive Measures**:
   - Implement high availability if single point of failure
   - Update monitoring to detect failures faster
   - Test disaster recovery procedures
   - Update runbooks based on lessons learned

---

## C.5 Escalation Procedures

### C.5.1 Technical Escalation Path

**Level 1** → SOC / Security Analyst (initial triage)  
**Level 2** → Security Team Lead (incident coordination)  
**Level 3** → CISO (critical incidents, strategic decisions)  
**Level 4** → Executive Management (business impact, regulatory notification)  
**Level 5** → Board of Directors (material incidents, crisis management)

### C.5.2 Escalation Timelines

| Severity | Security Team Lead | CISO | Executive Management |
|----------|-------------------|------|---------------------|
| **CRITICAL** | Immediate | Within 1 hour | Within 4 hours |
| **HIGH** | Within 1 hour | Within 4 hours | If impact significant |
| **MEDIUM** | Daily summary | Weekly summary | Not escalated |
| **LOW** | Weekly summary | Not escalated | Not escalated |

### C.5.3 After-Hours Escalation

**On-Call Rotation**:
- Security Team maintains 24/7 on-call coverage
- Escalation via pager/phone for CRITICAL/HIGH incidents
- CISO contact info available for critical escalations

**Threshold for After-Hours CISO Notification**:
- CRITICAL incidents (always)
- HIGH incidents with confirmed business impact
- Incidents requiring emergency decision (e.g., shut down systems)

---

## C.6 Communication Protocols

### C.6.1 Internal Communication

**During Incident**:
- Use dedicated incident Slack channel or MS Teams room
- Log all actions in incident ticket (single source of truth)
- Provide status updates every 2 hours (CRITICAL), 4 hours (HIGH)

**Stakeholder Notification**:
- Affected users: Notify when action required (password reset, system rebuild)
- IT Operations: Engage for containment actions (network isolation)
- Management: Briefed per escalation timeline
- Legal/Compliance: Notified if regulatory implications

### C.6.2 External Communication

**Vendor Engagement**:
- Web filtering vendor: For system issues, threat intelligence
- Incident response firm: For complex investigations (if retainer exists)
- Law enforcement: For criminal activity (CISO approval required)

**Regulatory Notification**:
- Data breach notification: Legal/Compliance determines requirements
- Timeline: Varies by jurisdiction (GDPR: 72 hours, others vary)
- CISO coordinates with Legal for all external disclosures

**Media/Public Communication**:
- All media inquiries routed to Corporate Communications
- No technical staff speaks to media without CISO approval
- Coordinated messaging for public incidents

---

## C.7 Post-Incident Activities

### C.7.1 Post-Incident Review (PIR)

**Timing**: Within 5 business days of incident closure

**Participants**: Incident response team, affected stakeholders, management (for significant incidents)

**Agenda**:
1. **Incident Summary**: What happened, timeline, impact
2. **Response Effectiveness**: What went well, what didn't
3. **Root Cause**: Why did incident occur (technical, process, human factors)
4. **Lessons Learned**: Key takeaways
5. **Action Items**: Preventive measures, policy updates, training needs

**Documentation**: PIR report filed with incident ticket

### C.7.2 Continuous Improvement

**Policy Updates**:
- If incident revealed policy gap → Update relevant policy section
- If procedure ineffective → Revise incident response procedures (this document)

**Technical Improvements**:
- Deploy additional controls to prevent recurrence
- Update detection rules to catch similar threats earlier
- Enhance monitoring and alerting

**Training**:
- User security awareness (if social engineering involved)
- Security team skills development (new attack techniques)
- Tabletop exercises based on real incidents

### C.7.3 Metrics and Reporting

**Incident Metrics Tracked**:
- Incident count by severity and type
- Mean time to detect (MTTD)
- Mean time to respond (MTTR)
- Mean time to resolve (MTTR)
- Incidents prevented by web filtering

**Reporting**:
- **Monthly**: Incident summary to CISO
- **Quarterly**: Trend analysis and metrics to Executive Management
- **Annual**: Comprehensive incident review for ISMS audit

---

**END OF DOCUMENT**