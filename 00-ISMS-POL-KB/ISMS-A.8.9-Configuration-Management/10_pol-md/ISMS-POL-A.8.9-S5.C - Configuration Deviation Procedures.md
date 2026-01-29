# ISMS-POL-A.8.9-S5.C
## Configuration Management - Configuration Deviation Procedures

**Document ID**: ISMS-POL-A.8.9-S5.C  
**Title**: Configuration Deviation Procedures  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Configuration Manager / SOC Manager | Initial deviation procedures |

**Review Cycle**: Annually  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Configuration Manager
- Review: SOC Manager, IT Operations Manager

**Distribution**: SOC team, configuration management team, system administrators, security team  
**Related Documents**: ISMS-POL-A.8.9-S2.3 (Configuration Monitoring Requirements), ISMS-POL-A.8.9-S4 (Policy Governance - Exceptions), ISMS-IMP-A.8.9.3 (Monitoring Assessment)

---

## C.1 Purpose

This annex provides **step-by-step procedures** for detecting, investigating, and remediating configuration deviations. Configuration deviation (also called "configuration drift") occurs when actual system configuration differs from approved baselines.

**Scope**:
- Deviation detection and alerting
- Triage and classification
- Investigation and root cause analysis
- Remediation procedures
- Exception request process
- Escalation procedures

---

## C.2 Deviation Detection

### C.2.1 Automated Detection Sources

**Configuration deviations are detected through**:
1. **Configuration Monitoring Tools**
   - Automated baseline comparison scans
   - File integrity monitoring (FIM) alerts
   - Security compliance scanners (CIS-CAT, OpenSCAP, etc.)
   - Cloud configuration monitoring (AWS Config, Azure Policy, etc.)

2. **Security Information and Event Management (SIEM)**
   - Configuration change events
   - Unauthorized access alerts
   - Privilege escalation events

3. **Change Management System**
   - Changes detected without corresponding approved change request
   - Post-change validation failures

4. **Manual Discovery**
   - Configuration audits
   - Incident investigation
   - System troubleshooting

---

## C.3 Deviation Triage Procedure

### C.3.1 Initial Assessment

**When a deviation alert is received**:

**STEP 1: Validate Alert (2 minutes)**
```
Action: Verify the alert is genuine (not false positive)
- Check alert details (system, parameter, expected vs actual value)
- Confirm system is reachable and monitoring tool is functioning
- Review recent alerts for patterns

Decision:
☐ Valid deviation → Proceed to STEP 2
☐ False positive → Close alert, tune monitoring rule if needed
☐ Monitoring tool error → Escalate to monitoring team
```

**STEP 2: Classify Severity (5 minutes)**
```
Severity Classification Criteria:

CRITICAL - Immediate action required
- Security control disabled (firewall, encryption, authentication)
- Unauthorized administrative access created
- Critical service configuration compromised
- Indicators of compromise (malware, backdoor)
→ SLA: Triage within 30 minutes, escalate immediately

HIGH - Urgent action required
- Significant hardening standard violation
- Non-compliance with regulatory requirement
- Unauthorized change detected
- Multiple systems affected
→ SLA: Triage within 2 hours, remediate within 24 hours

MEDIUM - Action required soon
- Moderate baseline deviation
- Single system affected, non-critical
- Approved change not yet reflected in baseline
→ SLA: Triage within 24 hours, remediate within 5 days

LOW - Action can be scheduled
- Minor cosmetic configuration difference
- No security or operational impact
- Planned change in progress
→ SLA: Triage within 5 days, remediate within 30 days

Record severity in tracking system
```

**STEP 3: Determine Root Cause Category (10 minutes)**
```
Root Cause Categories:

1. AUTHORIZED CHANGE - Baseline not yet updated
   - Approved change implemented recently
   - Baseline documentation update pending
   → Action: Update baseline, close drift alert

2. UNAUTHORIZED CHANGE - No approved change request
   - Change made without following change control process
   → Action: Investigate who/why, remediate or submit retroactive change request

3. CONFIGURATION DECAY - Gradual drift over time
   - Patches missed, accounts not removed, logs not rotated
   → Action: Remediate, review maintenance procedures

4. SYSTEM FAILURE - Unintentional configuration loss
   - System restore, failed update, database corruption
   → Action: Remediate, investigate system reliability

5. SECURITY INCIDENT - Malicious modification
   - Attacker changed configuration, privilege escalation
   → Action: Escalate to incident response team immediately

6. MONITORING ERROR - False positive
   - Baseline definition incorrect, monitoring rule error
   → Action: Correct baseline/rule, close alert

Record root cause category in tracking system
```

---

## C.4 Investigation Procedures

### C.4.1 For Authorized Changes

**If deviation correlates with approved change request**:
```
1. Verify change request ID and approval
2. Confirm deviation matches intended change
3. Update baseline documentation within 5 business days
4. Close deviation ticket
5. Link deviation ticket to change request in tracking system
```

**No further action needed** - This is normal lifecycle.

### C.4.2 For Unauthorized Changes

**If no approved change request exists**:
```
STEP 1: Gather Information (15-30 minutes)
- Who: Check system logs for user account that made change
  * Review authentication logs (Windows Event ID 4624, Linux /var/log/auth.log)
  * Check command history (Windows PowerShell history, Linux ~/.bash_history)
  * Identify source IP address and session information

- What: Determine exactly what changed
  * Compare current config to baseline (automated diff)
  * Identify all affected parameters
  * Assess completeness (partial change or full reconfiguration?)

- When: Establish timeline
  * Check system logs for exact timestamp
  * Correlate with other events (logins, service restarts, etc.)
  * Determine if change happened during maintenance window or business hours

- How: Determine method of change
  * GUI/console access?
  * SSH/RDP session?
  * Automated script or tool?
  * Configuration management system (Ansible, Puppet, etc.)?

Document findings in investigation notes

STEP 2: Contact Person Responsible (if identified)
- Contact system owner or administrator who made change
- Ask:
  * Was this change intentional?
  * Why was change control process not followed?
  * Was there an emergency situation?
  * Is the change needed for operations?

STEP 3: Determine Action
Based on investigation:

☐ LEGITIMATE BUT UNDOCUMENTED
  - Change was needed for valid business reason
  - Admin bypassed process (mistake or urgency)
  → Action: Submit retroactive change request OR revert change
  → Education: Remind admin of change control process

☐ TESTING/TROUBLESHOOTING
  - Admin was testing configuration
  - Intended to revert but forgot
  → Action: Revert to baseline
  → Education: Use non-production environments for testing

☐ EMERGENCY CHANGE NOT DOCUMENTED
  - Legitimate emergency but paperwork skipped
  → Action: Complete emergency change post-implementation form
  → Follow emergency change review process

☐ CONFIGURATION MANAGEMENT TOOL
  - Automated tool made change (Ansible, Puppet, Chef)
  - Change control integrated with CM tool
  → Action: Verify CM tool configuration is approved
  → Update baseline if needed

☐ SUSPICIOUS/UNAUTHORIZED
  - Cannot identify responsible party OR
  - Person denies making change OR
  - No legitimate business reason
  → Action: Escalate to security incident response (Section C.7)
```

---

## C.5 Remediation Procedures

### C.5.1 Standard Remediation

**For deviations requiring correction**:
```
STEP 1: Plan Remediation
- Determine remediation approach:
  ☐ Manual reapplication of baseline configuration
  ☐ Restore from configuration backup
  ☐ Re-run configuration management tool (Ansible, Puppet, etc.)
  ☐ Rebuild system from golden image

- Assess impact of remediation:
  * Will remediation cause service interruption?
  * Does remediation require change request?
  * Can remediation be performed immediately or needs scheduling?

- If service interruption expected or High/Critical system:
  → Submit change request for remediation
  → Schedule during maintenance window
- If no service interruption and Low/Medium system:
  → Proceed with remediation (document action)

STEP 2: Create Configuration Backup
BEFORE making any changes:
- Backup current configuration
- Verify backup is readable
- Document backup location

STEP 3: Execute Remediation
- Follow remediation plan
- Document steps taken
- Timestamp start and end of remediation

STEP 4: Verify Remediation
- Scan system to confirm deviation resolved
- Test system functionality
- Confirm no unintended side effects

STEP 5: Document and Close
- Update tracking system
- Document remediation actions
- Close deviation ticket
- Update baseline if needed

SLA Compliance:
- Critical: Remediate within 4 hours
- High: Remediate within 24 hours
- Medium: Remediate within 5 business days
- Low: Remediate within 30 days
```

### C.5.2 Remediation Decision Tree
```
┌─────────────────────────────────┐
│ Configuration Deviation Detected │
└────────────┬────────────────────┘
             │
             ▼
┌────────────────────────────────┐
│ Authorized Change?              │
│ (Approved change request exists)│
└───┬─YES─────────────┬─NO───────┘
    │                 │
    ▼                 ▼
┌───────────┐  ┌──────────────────┐
│Update     │  │Investigate       │
│Baseline   │  │Root Cause        │
│Close      │  │(Section C.4)     │
└───────────┘  └────────┬─────────┘
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      ┌──────────────┐      ┌──────────────┐
      │Legitimate    │      │Suspicious/   │
      │Business Need?│      │Unauthorized? │
      └──┬─YES───┬NO─┘      └──────┬───────┘
         │       │                 │
         ▼       ▼                 ▼
   ┌─────────┐ ┌──────┐     ┌──────────────┐
   │Request  │ │Revert│     │Escalate to   │
   │Exception│ │to    │     │Incident      │
   │OR       │ │Base- │     │Response      │
   │Submit   │ │line  │     │(Section C.7) │
   │Change   │ │      │     └──────────────┘
   │Request  │ └──────┘
   └─────────┘
```

---

## C.6 Exception Request Process

**When deviation is legitimate but cannot be immediately remediated**:

### C.6.1 When to Request Exception

- Business or technical justification exists for deviation
- Compliance with baseline is not immediately feasible
- Compensating controls can mitigate risk

**Examples**:
- Legacy application requires specific configuration incompatible with hardening standard
- Vendor-supported configuration conflicts with baseline
- Performance requirements necessitate deviation

### C.6.2 Exception Request Procedure
```
STEP 1: Prepare Exception Request
Complete exception request form including:
- Description of deviation from policy/baseline
- Business or technical justification
- Risk assessment
- Compensating controls (if any)
- Duration (temporary or permanent)
- Remediation plan (for temporary exceptions)

STEP 2: Submit for Review
- Submit to Configuration Manager
- CC: Asset Owner, Security Team

STEP 3: Review and Approval
- Configuration Manager: Operational feasibility review
- Security Team: Risk assessment
- Compliance Team: Regulatory impact (if applicable)

Approval Authority (based on risk):
- Low Risk: Configuration Manager
- Medium Risk: CISO or CTO
- High Risk: CISO + CTO jointly
- Critical Risk: Executive Leadership

STEP 4: Track Exception
- Add to exception register
- Set review/expiration date
- Schedule periodic reviews (quarterly for High risk)

STEP 5: Monitor Compliance
- Verify compensating controls remain effective
- Re-evaluate justification periodically
- Plan remediation for temporary exceptions
```

---

## C.7 Security Incident Escalation

**Escalate to Security Incident Response Team if**:
- Unauthorized administrative access created
- Security controls disabled without authorization
- Malware or backdoor indicators detected
- Deviation matches known attack patterns
- Cannot identify responsible party for unauthorized change
- Person responsible denies making change
- Indicators of compromise (IOCs) present

### C.7.1 Escalation Procedure
```
IMMEDIATE ACTIONS (within 15 minutes):
1. Contact Security Operations Center (SOC)
   - Phone: [SOC phone number]
   - Email: [SOC email]
   - Ticket System: [Incident ticket system]

2. Preserve Evidence
   - Do NOT revert configuration yet (evidence preservation)
   - Capture current system state (memory dump if possible)
   - Copy relevant logs
   - Document everything observed

3. Isolate If Necessary
   - If system is actively compromised, consider isolation
   - Consult with SOC before taking action
   - Document isolation decision and actions

4. Provide SOC with:
   - System identification (asset ID, name, IP address)
   - Timeline of deviation detection
   - Investigation findings
   - Configuration changes observed
   - Any suspicious indicators

5. Incident Response Team Takes Over
   - Follow incident response procedures
   - Configuration Manager supports as needed
   - Remediation occurs under incident response plan
```

---

## C.8 Escalation Matrix

| Situation | Escalate To | Timeframe |
|-----------|-------------|-----------|
| Critical deviation, no security concern | IT Operations Manager | Immediately |
| High deviation, no security concern | Configuration Manager | Within 2 hours |
| Suspicious unauthorized change | Security Operations Center (SOC) | Immediately |
| Security controls disabled | SOC + CISO | Immediately |
| Cannot remediate within SLA | Configuration Manager | Before SLA expires |
| Exception request needed | Configuration Manager | As soon as justified |
| High-risk exception | CISO + CTO | When exception prepared |
| Repeated deviations on same system | Asset Owner + Config Manager | After 3rd occurrence |

---

## C.9 Documentation Requirements

**For every deviation, document**:
- Detection date/time and method
- Deviation description (what changed)
- Severity classification
- Root cause category
- Investigation findings
- Remediation actions taken
- Time to remediate (measure against SLA)
- Lessons learned

**Use tracking system for**:
- Deviation ticket ID
- Link to change request (if applicable)
- Link to incident ticket (if escalated)
- Link to exception request (if approved)
- Status updates throughout lifecycle

---

## C.10 Metrics and Reporting

**Configuration Manager tracks**:
- Total deviations detected (by severity)
- Mean time to detect (MTTD)
- Mean time to remediate (MTTR)
- SLA compliance percentage
- Deviations by root cause category
- Repeat deviations (same system/configuration)
- Exception requests granted
- Security incidents resulting from deviations

**Reports generated**:
- Weekly summary (to IT Operations Manager)
- Monthly summary (to CISO, CTO)
- Quarterly trends (to Executive Leadership)

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9-S2.3: Configuration Monitoring Requirements
- ISMS-POL-A.8.9-S4: Policy Governance (Exception Management)
- ISMS-POL-A.8.9-S5.B: Change Request Form Template
- ISMS-IMP-A.8.9.3: Configuration Monitoring Assessment

---