# ISMS-POL-A.8.16-S2.3
## Monitoring Activities - Alert Management & Response Requirements

**Document ID**: ISMS-POL-A.8.16-S2.3
**Title**: Monitoring Activities - Alert Management & Response Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead / Incident Response Manager | Initial alert management and response requirements |

**Review Cycle**: Quarterly (alert procedures evolve rapidly based on operational experience)  
**Next Review Date**: [Approval Date + 3 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Review: Security Operations Center (SOC) Lead
- Response Review: Incident Response Manager
- Business Review: IT Operations Manager

**Distribution**: Security team, SOC analysts, incident response team, IT operations  
**Related Documents**: ISMS-IMP-A.8.16.4 (Alert Management Assessment), ISMS-POL-A.5.24-28 (Incident Management), ISMS-POL-A.8.16-S5.C (Alert Response Procedures)

---

## 2.3.1 Purpose and Scope

This section establishes **mandatory requirements** for alert management and response—the operational processes that determine what happens when monitoring detects something suspicious.

**In Scope**: Alert generation, classification, triage, investigation, escalation, performance metrics  
**Primary Stakeholders**: SOC, Incident Response Team, Security Engineering  
**Implementation Evidence**: ISMS-IMP-A.8.16.4 (Alert Management & Response Assessment)

**Critical Principle:**  
*"Detection without response is theater. Alerts without triage are noise. Response without metrics is cargo cult security."*

**This section prevents:**
- Alert fatigue (too many meaningless alerts)
- Alert apathy (analysts ignoring alerts due to high false positive rates)
- Response paralysis (unclear procedures for what to do)
- Accountability gaps (no one owns alert response)

---

## 2.3.2 Alert Management Philosophy

### 2.3.2.1 The Alert Quality Imperative

Organizations must balance competing objectives:

**Detection Completeness vs. Operational Workload:**
- More alerts = better detection coverage BUT overwhelms analysts
- Fewer alerts = manageable workload BUT increases blind spots

**The Goal:** Every alert should be:
- **Actionable**: Clear next steps exist
- **Accurate**: Low false positive rate
- **Timely**: Generated quickly enough to enable response
- **Contextual**: Enriched with information needed for triage

### 2.3.2.2 Alert vs. Incident

Organizations **SHALL** distinguish between:

**Security Alert:**
- Notification that monitoring detected something requiring investigation
- May or may not represent actual security incident
- Requires triage to determine disposition

**Security Incident:**
- Confirmed violation of security policy or imminent threat
- Requires incident response procedures (per ISMS-POL-A.5.24-28)
- Results in incident ticket, investigation, remediation, lessons learned

**Relationship:** Alerts → Triage → Confirmed Incidents OR False Positives

### 2.3.2.3 Alert Lifecycle

Every alert follows a lifecycle:

1. **Generation**: Monitoring system creates alert based on detection rule
2. **Enrichment**: Alert is enriched with context (asset info, user info, threat intel)
3. **Triage**: SOC analyst reviews alert and determines disposition
4. **Investigation**: If suspicious, deeper investigation occurs
5. **Escalation**: If confirmed incident, escalated to incident response
6. **Resolution**: Alert closed with documented outcome
7. **Tuning**: Feedback loop to improve detection rule

---

## 2.3.3 Alert Generation Requirements

### 2.3.3.1 Alert Triggering

Organizations **SHALL** generate alerts based on:

**Threshold-Based Triggers:**
- Metric exceeds baseline threshold (per ISMS-POL-A.8.16-S2.2)
- Example: "Failed logins > 10 in 5 minutes"

**Signature-Based Triggers:**
- Known attack pattern detected
- Example: "MITRE ATT&CK T1003 (Credential Dumping) detected"

**Correlation-Based Triggers:**
- Multiple events indicate attack chain
- Example: "Privilege escalation followed by lateral movement"

**Anomaly-Based Triggers:**
- Deviation from learned behavior
- Example: "User accessing never-before-accessed systems"

**Threat Intelligence Triggers:**
- IOC match detected
- Example: "Connection to known C2 IP address"

### 2.3.3.2 Alert Content Requirements

Every alert **SHALL** include:

**Core Alert Data:**
- Unique alert ID
- Alert timestamp (generation time)
- Alert severity (Critical/High/Medium/Low)
- Alert title (concise description)
- Detection rule ID that triggered alert

**Event Data:**
- Source system(s) involved
- User account(s) involved (if applicable)
- Timestamp of detected event(s)
- Summary of detected activity

**Context Enrichment (SHOULD include):**
- Asset information (criticality, owner, location)
- User information (role, department, manager)
- Threat intelligence (IP reputation, domain categorization)
- Historical context (past alerts for same user/system)
- Related alerts (correlated events)

**Response Guidance:**
- Initial triage steps
- Investigation playbook reference
- Expected false positive scenarios
- Escalation criteria

### 2.3.3.3 Alert Deduplication

Organizations **SHALL** implement alert deduplication to reduce noise:

**Deduplication Strategies:**
- Suppress duplicate alerts within time window (e.g., only alert once per 15 minutes for same condition)
- Aggregate multiple similar alerts into single meta-alert
- Suppress alerts during known maintenance windows
- Suppress alerts for known exceptions (documented and approved)

**Note:** Deduplication must be carefully configured to avoid suppressing distinct security incidents.

---

## 2.3.4 Alert Severity Classification

### 2.3.4.1 Severity Levels

Organizations **SHALL** classify alerts into four severity levels:

**CRITICAL (P1):**
- **Definition**: Confirmed active attack in progress OR high-confidence indicator of imminent breach
- **Examples**:
  - C2 communication detected (active malware)
  - Ransomware execution detected
  - Data exfiltration in progress
  - Privileged account compromise
  - Multiple failed login attempts to critical system followed by success from unusual location
- **Response Timeframe**: Immediate (< 15 minutes)
- **Availability**: 24/7 response required

**HIGH (P2):**
- **Definition**: Strong indicator of security incident requiring urgent investigation
- **Examples**:
  - Multiple failed authentication attempts (potential brute force)
  - Lateral movement detected
  - Unusual privileged access patterns
  - Known vulnerability exploitation attempt
  - Suspicious network scanning activity
- **Response Timeframe**: Within 1 hour (business hours), within 4 hours (after hours)
- **Availability**: Business hours + on-call

**MEDIUM (P3):**
- **Definition**: Suspicious activity requiring investigation but not urgent
- **Examples**:
  - Policy violations (acceptable use, access policy)
  - Minor baseline deviations
  - Reconnaissance activities detected
  - Configuration changes on non-critical systems
- **Response Timeframe**: Within 4 business hours
- **Availability**: Business hours

**LOW (P4):**
- **Definition**: Informational alerts requiring review but minimal urgency
- **Examples**:
  - Trend analysis findings
  - Compliance monitoring results
  - Informational threat intelligence matches
  - Non-urgent system health alerts
- **Response Timeframe**: Within 1-3 business days
- **Availability**: Business hours

### 2.3.4.2 Severity Assignment Methodology

Organizations **SHALL** assign severity based on:

**Asset Criticality:**
- Critical systems/data → Higher severity
- Non-critical systems → Lower severity

**Attack Stage:**
- Later stage attacks (exfiltration, impact) → Higher severity
- Early stage (reconnaissance) → Lower severity

**Confidence Level:**
- High confidence (low false positive rate) → Higher severity
- Low confidence (high false positive expected) → Lower severity

**Threat Context:**
- Active exploitation → Higher severity
- Attempted but blocked → Lower severity

**Example Severity Matrix:**

| Asset Criticality | Attack Confidence | Attack Stage | Severity |
|-------------------|-------------------|--------------|----------|
| Critical | High | Late (Impact) | CRITICAL |
| Critical | High | Mid (Execution) | HIGH |
| Critical | Medium | Early (Recon) | MEDIUM |
| Standard | High | Late | HIGH |
| Standard | High | Mid | MEDIUM |
| Standard | Low | Any | LOW |

---

## 2.3.5 Alert Triage Requirements

### 2.3.5.1 Triage Process

Organizations **SHALL** implement structured triage process:

**Step 1: Alert Acknowledgment**
- SOC analyst acknowledges alert ownership within SLA timeframe
- Alert status updated to "In Progress"
- Analyst name/ID logged

**Step 2: Initial Assessment**
- Review alert details and context
- Verify alert is not obvious false positive (known exception, maintenance activity)
- Assess severity appropriateness (escalate/de-escalate if needed)

**Step 3: Disposition Decision**
- **True Positive**: Confirmed security incident → Escalate to incident response
- **False Positive**: Legitimate activity incorrectly flagged → Document and close
- **Requires Investigation**: Unclear, needs deeper analysis → Proceed to investigation
- **Benign True Positive**: Detection correct but activity is authorized/expected → Document and close

**Step 4: Documentation**
- Document triage findings
- Update alert status and disposition
- Add notes for future reference
- Close or escalate alert

### 2.3.5.2 Triage Timeframes

Organizations **SHALL** complete initial triage within:

- **Critical alerts**: 15 minutes
- **High alerts**: 1 hour (business hours), 4 hours (after hours)
- **Medium alerts**: 4 business hours
- **Low alerts**: 1 business day

**Note:** Triage is not full investigation—it's initial assessment to determine disposition.

### 2.3.5.3 Triage Documentation

Organizations **SHALL** document for every alert:

- Triage start and completion timestamp
- Analyst performing triage
- Disposition (True Positive / False Positive / Benign / Needs Investigation)
- Rationale for disposition
- Actions taken (if any)
- Escalation decision (if applicable)

---

## 2.3.6 Alert Investigation Requirements

### 2.3.6.1 Investigation Triggers

Full investigation is required when:

- Alert severity is Critical or High
- Triage disposition is "True Positive" or "Requires Investigation"
- Multiple related alerts suggest attack campaign
- Executive/management requests investigation

### 2.3.6.2 Investigation Process

Organizations **SHALL** follow structured investigation process:

**Gather Evidence:**
- Collect relevant logs (authentication, network, system, application)
- Identify timeline of events (before, during, after detected activity)
- Identify affected systems, users, data

**Analyze Context:**
- Correlate with other security events
- Check threat intelligence for known indicators
- Review user/system normal behavior baseline
- Assess lateral movement or privilege escalation indicators

**Determine Scope:**
- Which systems are affected?
- Which accounts are compromised (if any)?
- What data was accessed/exfiltrated?
- How did attacker gain access?

**Assess Impact:**
- Confidentiality impact (data exposed?)
- Integrity impact (data/systems modified?)
- Availability impact (systems disrupted?)
- Business impact (operations affected?)

**Recommend Response:**
- Containment actions needed
- Eradication steps required
- Recovery procedures
- Escalation to incident response (if confirmed incident)

### 2.3.6.3 Investigation Timeframes

Organizations **SHALL** complete investigation within:

- **Critical alerts**: 4 hours (preliminary findings), 24 hours (complete investigation)
- **High alerts**: 8 hours (preliminary), 48 hours (complete)
- **Medium alerts**: 3 business days
- **Low alerts**: 5 business days

**Note:** Timeframes may extend for complex investigations—document justification for extensions.

### 2.3.6.4 Investigation Documentation

Organizations **SHALL** maintain investigation records including:

- Investigation timeline (chronology of events)
- Evidence collected (log excerpts, screenshots, analysis results)
- Analysis methodology and findings
- Scope and impact assessment
- Recommendations
- Lessons learned

**Retention:** Investigation records retained per ISMS-POL-A.8.16-S2.4 (minimum 1 year recommended).

---

## 2.3.7 Alert Escalation Requirements

### 2.3.7.1 Escalation Triggers

Alerts **SHALL** be escalated to incident response when:

- Confirmed security incident (actual compromise or policy violation)
- Potential data breach requiring regulatory notification
- Attack in progress requiring immediate containment
- Multiple systems/users affected
- Executive/management involvement needed
- Legal/compliance implications

### 2.3.7.2 Escalation Paths

Organizations **SHALL** define clear escalation paths:

**Technical Escalation (Capability-Based):**
- SOC Tier 1 → SOC Tier 2 → SOC Tier 3 → Security Engineering → External Experts
- Escalate when technical expertise exceeds current responder capability

**Incident Escalation (Severity-Based):**
- SOC → Incident Response Team → Incident Manager → CISO
- Escalate when confirmed incident requires coordination and remediation

**Management Escalation (Impact-Based):**
- Security Team → CISO → CIO/CTO → CEO → Board
- Escalate when business impact is significant or regulatory notification required

**External Escalation:**
- Law Enforcement (criminal activity)
- Regulators (data breach notification)
- Customers/Partners (if their data affected)
- External Incident Response Firm (if internal capability insufficient)

### 2.3.7.3 Escalation Procedures

Organizations **SHALL** establish procedures for:

- How to escalate (communication method—phone, ticket, secure channel)
- What information to provide (alert details, investigation findings, recommendations)
- Who to escalate to (primary and backup contacts)
- When to escalate (decision criteria)
- Escalation timeframes (urgency-based)

### 2.3.7.4 Escalation Documentation

Organizations **SHALL** document:

- Escalation timestamp
- Escalation reason and justification
- Who escalated and to whom
- Information provided during escalation
- Acknowledgment of escalation receipt
- Outcome of escalation (incident created, further investigation, false alarm)

---

## 2.3.8 Alert Closure and Resolution

### 2.3.8.1 Closure Criteria

Alerts may be closed when:

**False Positive:**
- Investigation confirms legitimate activity
- Detection rule is overly sensitive (tuning needed)
- Alert is duplicate of already-investigated alert

**Benign True Positive:**
- Detection is correct but activity is authorized/expected
- Example: Security team conducting authorized penetration test

**Resolved Incident:**
- Alert escalated to incident response
- Incident has been remediated and closed
- Alert linked to incident record

**Investigation Complete:**
- Investigation finished with documented findings
- No further action required

### 2.3.8.2 Closure Documentation

Organizations **SHALL** document for closed alerts:

- Closure timestamp
- Analyst closing alert
- Closure reason (False Positive / Benign / Resolved / Investigated)
- Summary of findings
- Recommendations for detection tuning (if applicable)
- Link to incident record (if escalated)

### 2.3.8.3 Post-Closure Activities

Organizations **SHALL** conduct post-closure activities:

**For False Positives:**
- Update detection rule to reduce false positives
- Document false positive scenario for future reference
- If persistent false positives, consider rule retirement

**For True Positives:**
- Verify remediation was effective
- Update detection rules if new attack technique learned
- Share threat intelligence with relevant teams/communities
- Conduct lessons learned review

---

## 2.3.9 Alert Performance Metrics

### 2.3.9.1 Mandatory Metrics

Organizations **SHALL** measure and report:

**Alert Volume Metrics:**
- Total alerts per day/week/month
- Alerts by severity level
- Alerts by detection rule (identify noisy rules)

**Alert Disposition Metrics:**
- True Positive rate (% of alerts that are real incidents)
- False Positive rate (% of alerts that are false alarms) - **Target: <25%**
- Benign True Positive rate
- Escalation rate (% of alerts escalated to incident response)

**Response Time Metrics:**
- Mean Time To Acknowledge (MTTA): Alert generation → Analyst acknowledgment
  - **Target: <15 min for Critical, <1 hour for High**
- Mean Time To Triage (MTTT): Alert generation → Triage complete
  - **Target: <1 hour for Critical, <4 hours for High**
- Mean Time To Investigate (MTTI): Triage → Investigation complete
  - **Target: <4 hours for Critical, <24 hours for High**
- Mean Time To Resolve (MTTR): Alert generation → Alert closed
  - **Target: <8 hours for Critical, <48 hours for High**

**Effectiveness Metrics:**
- Alert-to-Incident ratio (how many alerts result in incidents)
- Detection rate (% of test attacks detected) - **Target: >90%**
- Escalation accuracy (% of escalations that were justified)

### 2.3.9.2 Reporting Frequency

Metrics **SHALL** be:
- Calculated **daily** (operational dashboards)
- Reviewed **weekly** by SOC management
- Reported **monthly** to CISO
- Included in **quarterly** ISMS management review

### 2.3.9.3 Metric-Driven Improvement

Organizations **SHALL** use metrics to drive improvement:

**High False Positive Rate (>25%):**
- Prioritize detection rule tuning
- Review baseline accuracy
- Consider more advanced detection methods

**High Alert Volume (analyst overwhelm):**
- Increase alert deduplication/aggregation
- Retire low-value detection rules
- Automate triage for common scenarios

**Slow Response Times (exceeding SLA):**
- Increase SOC staffing
- Improve automation and enrichment
- Enhance analyst training
- Simplify triage procedures

**Low Detection Rate (<90%):**
- Expand detection rule coverage
- Improve baseline establishment
- Enhance threat intelligence integration
- Increase red team testing frequency

---

## 2.3.10 Alert Automation and Orchestration

### 2.3.10.1 Automation Opportunities

Organizations **SHOULD** automate where possible:

**Alert Enrichment:**
- Automatic asset lookup (criticality, owner)
- Automatic user lookup (role, department, history)
- Automatic threat intelligence enrichment
- Related alert correlation

**Triage Automation:**
- Automatic false positive detection (known maintenance windows, authorized activity)
- Automatic severity adjustment based on context
- Automatic alert routing to appropriate analyst queue

**Response Automation:**
- Automatic containment actions (account disable, network isolation) for high-confidence threats
- Automatic ticket creation for escalated incidents
- Automatic notification to relevant stakeholders
- Automatic evidence collection

### 2.3.10.2 Security Orchestration (SOAR)

Organizations with SOAR platforms **SHOULD**:

- Implement playbooks for common alert types
- Automate repetitive investigation tasks
- Orchestrate response across multiple security tools
- Maintain human oversight for critical decisions

**Balance:** Automate routine/repetitive tasks, but maintain human judgment for complex decisions.

### 2.3.10.3 Automation Guardrails

Organizations **SHALL** implement safeguards:

- No automatic containment actions without human review (for P1/P2) unless very high confidence
- Maintain audit trail of all automated actions
- Provide override capability for automated decisions
- Test automation thoroughly before production deployment
- Review automated actions regularly for accuracy

---

## 2.3.11 Integration with Incident Response

### 2.3.11.1 Alert-to-Incident Handoff

Organizations **SHALL** establish clear handoff between monitoring and incident response:

**SOC Responsibilities (Alert Management):**
- Detect and triage alerts
- Conduct initial investigation
- Determine if incident response needed
- Provide evidence package to IR team

**Incident Response Responsibilities:**
- Coordinate incident response activities
- Execute containment and eradication
- Manage stakeholder communications
- Conduct post-incident review

**Handoff Criteria:**
- When to escalate from alert to incident
- What information to provide to IR team
- How to transition ownership
- How to maintain continuity

### 2.3.11.2 Bi-Directional Communication

Organizations **SHALL** maintain communication:

**SOC → IR:**
- Real-time updates on new related alerts
- Additional evidence as discovered
- Technical support during incident response

**IR → SOC:**
- Incident status updates
- New IOCs to add to detection
- Lessons learned for detection improvement
- Feedback on alert quality/accuracy

---

## 2.3.12 Continuous Improvement

Organizations **SHALL**:

- Review alert management metrics **weekly**
- Conduct alert quality reviews **monthly** (analyze false positives, tune rules)
- Update response procedures based on lessons learned
- Test alert and escalation procedures **quarterly**
- Benchmark alert metrics against industry standards **annually**
- Conduct SOC tabletop exercises **semi-annually**

Organizations **SHOULD**:
- Implement feedback loop from incident response to detection
- Conduct regular SOC analyst training on alert triage
- Share alert handling best practices across shifts/teams
- Participate in industry SOC communities for benchmarking

---

## 2.3.13 Exceptions to Alert Response Requirements

**General Rule**: Exceptions to alert response requirements create response gaps and are strongly discouraged.

Where operational constraints prevent full compliance, organizations **SHALL**:

- Document exception with operational justification
- Identify compensating controls
- Require SOC Lead and CISO approval
- Review exceptions quarterly
- Establish remediation timeline

**Example Valid Exception**: Organization lacks 24/7 SOC but implements on-call rotation for Critical alerts. Compensating control: Automated containment for highest-confidence Critical alerts, on-call response within 30 minutes.

**Example Invalid Exception**: "We don't have time to investigate alerts." (Then you have cargo cult monitoring—logs and alerts without action.)

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation and terminology
- **ISMS-POL-A.8.16-S2** (Requirements Overview) - Framework overview
- **ISMS-POL-A.8.16-S2.1** (Infrastructure) - Monitoring platforms and log sources
- **ISMS-POL-A.8.16-S2.2** (Baseline & Detection) - How alerts are generated
- **ISMS-POL-A.8.16-S2.4** (Retention) - How long to keep alert data
- **ISMS-POL-A.5.24-28** (Incident Management) - What happens after escalation
- **ISMS-POL-A.8.16-S5.C** (Alert Response Procedures) - Detailed playbooks
- **ISMS-IMP-A.8.16.4** (Implementation Assessment) - Assessment workbook for alert management

---

*"An alert that generates no response is just a log entry with extra steps. Response without metrics is hope. Metrics without improvement is cargo cult operations."*  
*—SOC Management Wisdom*