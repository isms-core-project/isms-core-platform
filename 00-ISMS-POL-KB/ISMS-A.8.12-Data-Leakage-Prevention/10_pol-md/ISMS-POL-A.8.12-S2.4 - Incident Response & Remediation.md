**Dependency:**  
Incident response depends on **S2.3 (Monitoring & Detection)** - DLP alerts trigger incidents that this domain handles.

### 1.3 Integration with Organizational Incident Management

DLP incident response SHALL integrate with organizational incident management framework (**ISMS-POL-A.5.24-28**):

- **Shared incident classification** (severity, impact assessment)
- **Common escalation paths** (CISO, Legal, HR, Executive Management)
- **Unified ticketing system** (incident tracking and documentation)
- **Coordinated communication** (internal notifications, external reporting)
- **Joint lessons learned** (post-incident reviews, policy updates)

**DLP-Specific Considerations:**
- Data breach notification requirements (FADP Article 24, GDPR Article 33-34)
- Forensic preservation (potential litigation, regulatory investigation)
- Employee privacy (monitoring logs, proportionality in investigation)
- HR involvement (policy violations, disciplinary action)

---

## 2. DLP Incident Definition

### 2.1 What Constitutes a DLP Incident?

A **DLP incident** is any event where:
- **Sensitive data** (Confidential or Restricted classification) is transferred in violation of policy
- **Attempted exfiltration** is detected and blocked (prevention is still an incident - indicates intent or negligence)
- **Suspicious behavior** suggests data theft or unauthorized disclosure (mass transfers, anomalous patterns)
- **Policy violations** with potential business impact (repeated violations, high-value data)

### 2.2 DLP Events vs. DLP Incidents

**Not every DLP alert is an incident:**

| Event Type | Definition | Response |
|------------|------------|----------|
| **Routine Block** | Policy violation, no malicious intent, no business impact | Log, no incident ticket, user education if repeated |
| **False Positive** | Legitimate business activity incorrectly blocked | Log, tune policy, no incident ticket |
| **Policy Violation** | Intentional or negligent violation, low business impact | Incident ticket (Low), user warning, manager notification |
| **Data Exfiltration Attempt** | Malicious or negligent attempt to steal data | Incident ticket (High/Critical), investigation, containment |
| **Successful Data Breach** | Sensitive data confirmed exfiltrated | Incident ticket (Critical), breach notification, forensic investigation |

**Escalation Criteria:**  
SOC analysts SHALL escalate DLP events to Incident Response when:
- Event severity is High or Critical (per S2.3 classification)
- Multiple related events suggest coordinated attack or insider threat
- Data classification is Restricted (PII, financial, IP, credentials)
- User is departing employee, contractor with elevated access, or exhibits anomalous behavior
- Legal, regulatory, or reputational impact is possible

---

## 3. Incident Severity Classification

### 3.1 Severity Levels

DLP incidents SHALL be classified by severity to prioritize response:

| Severity | Definition | Response SLA | Escalation | Examples |
|----------|------------|--------------|------------|----------|
| **Critical** | Confirmed or highly likely data exfiltration of Restricted data | 15 minutes | CISO, Legal, DPO, HR | Credentials emailed externally, source code to personal GitHub, mass PII export to USB, database export to cloud |
| **High** | Attempted exfiltration blocked, high-value data, or multiple violations suggesting malicious intent | 1 hour | Incident Response Lead, Data Owner | Finance data to unapproved cloud, repeated USB blocks, IP to personal email |
| **Medium** | Policy violation with potential business impact, unclear intent | 4 hours | SOC Lead | Contract sent to wrong recipient, confidential file to personal OneDrive |
| **Low** | Minor policy violation, legitimate business activity with procedural gap | 24 hours | Security Analyst | Employee emailed confidential document without encryption (should have used secure portal) |

### 3.2 Severity Factors

When determining severity, consider:

**Data Sensitivity:**
- Restricted (PII/Special Categories, credentials, IP, payment cards) = High/Critical
- Confidential (business sensitive, contracts, financial) = Medium/High
- Internal (non-sensitive) = Low/Medium

**Transfer Destination:**
- External (personal email, public cloud, USB) = Higher severity
- Internal (approved collaboration, authorized partners) = Lower severity

**User Intent:**
- Malicious (insider threat, sabotage, espionage) = Critical
- Negligent (careless, untrained, policy ignorance) = High/Medium
- Legitimate (business need, procedural gap) = Medium/Low

**Volume & Frequency:**
- Mass transfer (>100 files, >1GB) = Higher severity
- Repeated violations (>5 in 24 hours) = Higher severity
- Single incident = Lower severity (unless high-value data)

**Business Impact:**
- Regulatory breach (FADP/GDPR notification required) = Critical
- Competitive harm (IP to competitor, M&A leak) = Critical
- Financial loss (fraud, contract breach) = High/Critical
- Reputational damage (customer data, media attention) = High/Critical
- No business impact (prevented exfiltration, no harm) = Low/Medium

---

## 4. Incident Response Lifecycle

### 4.1 Phase 1: Detection & Triage (S2.3 → S2.4 Handoff)

**Responsibility:** SOC Analysts  
**SLA:** Per S2.3 alert severity (Critical: 15 min, High: 1 hour, Medium: 4 hours)

**Activities:**
1. **Validate alert** (is this a true DLP event or false positive?)
2. **Classify severity** (Critical/High/Medium/Low per Section 3.1)
3. **Initial context gathering:**
   - User identity, role, department, manager
   - Data category, classification, volume
   - Transfer channel, destination
   - Recent HR events (resignation, termination, PIP)
   - Historical violations (repeat offender?)
4. **Escalation decision** (create incident ticket or close as routine/false positive)
5. **Notify Incident Response** (if High/Critical) or handle within SOC (if Medium/Low)

**Output:** Incident ticket with severity, initial context, assigned to Incident Response team

### 4.2 Phase 2: Initial Assessment

**Responsibility:** Incident Response Team  
**SLA:** Critical: 30 minutes, High: 2 hours, Medium: 8 hours

**Activities:**
1. **Verify severity** (confirm or adjust based on deeper analysis)
2. **Assess scope:**
   - How much data was involved? (file count, record count, data volume)
   - Was exfiltration successful or blocked?
   - Are there related events? (same user, similar data, coordinated activity)
3. **Identify stakeholders:**
   - Data Owner (business unit responsible for data)
   - User's Manager (if employee policy violation)
   - HR (if disciplinary action likely)
   - Legal/DPO (if breach notification may be required)
   - Executive Management (if reputational or regulatory risk)
4. **Determine investigation approach:**
   - Forensic investigation (preserve evidence, legal hold)
   - User interview (negligence vs. malicious intent)
   - Technical analysis (endpoint forensics, network logs, email audit)
5. **Document initial findings** (incident ticket updated with assessment)

**Output:** Incident severity confirmed, investigation plan, stakeholders notified

### 4.3 Phase 3: Containment

**Responsibility:** Incident Response Team + IT Operations  
**SLA:** Immediate for Critical, 1 hour for High, 4 hours for Medium

**Containment Actions (Severity-Dependent):**

#### 4.3.1 Critical Incidents

**Immediate Actions (within 15 minutes):**
- **Disable user account** (prevent further exfiltration)
- **Isolate endpoint** (disconnect from network, EDR quarantine)
- **Block external accounts** (if user forwarded to personal email, work with provider to suspend)
- **Notify Legal/DPO** (potential breach notification required)
- **Preserve evidence** (snapshot endpoint, export logs, legal hold on email)

**Follow-Up Actions (within 1 hour):**
- **Review user access** (revoke unnecessary privileges, VPN access)
- **Notify data owner** (assess business impact)
- **Notify HR** (suspension, termination, escorted exit if malicious)
- **Engage law enforcement** (if criminal activity suspected - CISO/Legal decision)

#### 4.3.2 High Incidents

**Immediate Actions (within 1 hour):**
- **Notify user's manager** (explain situation, assess intent)
- **Review user activity** (endpoint logs, email, file access, cloud usage)
- **Adjust DLP rules** (if repeat pattern, tighten controls for this user/data type)
- **Preserve evidence** (export DLP logs, endpoint forensics if needed)

**Follow-Up Actions (within 4 hours):**
- **User interview** (understand intent, negligence vs. malicious)
- **Assess data impact** (was data actually exfiltrated or blocked?)
- **Notify stakeholders** (data owner, Legal if needed)

#### 4.3.3 Medium/Low Incidents

**Standard Actions (within 4-24 hours):**
- **User notification** (policy reminder, education)
- **Manager notification** (if repeated violations)
- **Monitor user** (enhanced DLP monitoring for 30 days)
- **No account suspension** unless repeat offender

**Containment Principles:**
- **Proportionality:** Response must be proportionate to risk (don't suspend employee for single low-risk violation)
- **Evidence preservation:** Always preserve evidence before account suspension (logs, snapshots, email export)
- **Employee rights:** Consult HR/Legal before disciplinary action (Swiss Employment Law, works council if applicable)

### 4.4 Phase 4: Investigation

**Responsibility:** Incident Response Team + Forensic Analysts (if needed)  
**SLA:** Critical: 24 hours, High: 3 days, Medium: 7 days

**Investigation Objectives:**
1. **Determine intent** (malicious, negligent, or legitimate business need?)
2. **Assess scope** (total data exfiltrated, timeframe, related incidents)
3. **Identify root cause** (policy gap, training gap, control gap, insider threat)
4. **Preserve evidence** (for legal, regulatory, or disciplinary proceedings)

**Investigation Activities:**

#### 4.4.1 Technical Analysis

- **DLP logs:** Review all events for this user (last 90 days minimum)
- **Endpoint forensics:** File access, application usage, USB activity, browser history
- **Email audit:** Sent items, forwarding rules, external email accounts
- **Cloud audit:** SaaS usage, file uploads, collaboration tool activity
- **Network logs:** VPN usage, off-hours access, unusual destinations
- **Authentication logs:** Failed logins, password resets, MFA anomalies

#### 4.4.2 User Interview

Organizations SHALL conduct user interviews for High/Critical incidents:

**Interview Preparation:**
- Consult HR/Legal (employee rights, works council notification if required)
- Prepare questions (avoid leading questions, gather facts)
- Document interview (written notes, audio recording if legally permitted)

**Interview Questions:**
- What were you trying to accomplish?
- Why did you transfer this data? (business justification)
- Were you aware of the DLP policy?
- Have you transferred similar data before?
- Did anyone ask you to transfer this data? (social engineering, coercion)
- Where did you transfer the data? (destination, purpose)
- Do you still have access to the data? (recovery options)

**Employee Rights:**
- Right to representation (union, legal counsel if company allows)
- Right to understand allegations (explain violation, show evidence)
- Right to appeal (grievance process per employment contract)

#### 4.4.3 Data Owner Consultation

Organizations SHALL consult data owners for High/Critical incidents:

**Data Owner Questions:**
- What is the business impact of this data exfiltration?
- Is this data subject to regulatory requirements? (FADP, GDPR, PCI DSS)
- Who are the affected parties? (customers, partners, employees)
- What is the competitive/financial impact? (IP loss, contract breach)
- Is breach notification required? (FADP Article 24, GDPR Article 33-34)

**Output:** Business impact assessment, breach notification decision, remediation priority

### 4.5 Phase 5: Remediation

**Responsibility:** Incident Response Team + IT Operations + Security Engineering  
**SLA:** Critical: 72 hours, High: 7 days, Medium: 14 days

**Remediation Objectives:**
- **Close control gaps** (prevent recurrence)
- **Recover data** (if possible and legally required)
- **Notify affected parties** (if breach notification required)
- **Implement lessons learned** (policy updates, training, technology enhancements)

**Remediation Actions (Root Cause-Specific):**

#### 4.5.1 Policy Gap

**Root Cause:** DLP policy does not cover this scenario

**Remediation:**
- Update DLP policy (add new rule, adjust classification)
- Communicate policy change (user awareness, training update)
- Retroactive scan (check for similar past violations)

**Example:** USB drives were not blocked for Finance department, insider used USB to exfiltrate customer database.  
**Remediation:** Block USB for all users with Restricted data access, implement encrypted USB exception process.

#### 4.5.2 Training Gap

**Root Cause:** User was unaware of policy or did not understand risk

**Remediation:**
- User education (security awareness training, policy reminder)
- Department-wide training (if multiple users show same gap)
- Update training materials (add this scenario to onboarding/annual training)
- Manager notification (ensure manager reinforces policy)

**Example:** Employee emailed customer list to personal email for work-from-home convenience, unaware this violated policy.  
**Remediation:** User completes DLP awareness training, manager explains policy, monitor user for 30 days.

#### 4.5.3 Control Gap

**Root Cause:** DLP control exists but is ineffective (false negative, coverage gap)

**Remediation:**
- Tune DLP rules (improve detection pattern, reduce false negatives)
- Expand DLP coverage (deploy to missed channels, users, endpoints)
- Implement compensating controls (if DLP cannot cover this scenario)

**Example:** Source code exfiltrated via Git push to personal GitHub, endpoint DLP did not detect Git protocol.  
**Remediation:** Deploy GitHub Advanced Security (secret scanning), block Git push to non-corporate repos, developer training on secure code practices.

#### 4.5.4 Insider Threat

**Root Cause:** Malicious employee intentionally exfiltrated data

**Remediation:**
- **Immediate:** Termination (HR/Legal decision), account revocation, exit interview, legal hold
- **Short-term:** Enhanced monitoring for similar roles (trust but verify), access review (principle of least privilege)
- **Long-term:** Insider threat program (behavioral analytics, UEBA, HR collaboration)
- **Legal action:** Civil litigation (breach of contract, NDA violation), criminal prosecution (if applicable)

**Example:** Departing employee exfiltrated customer database to competitor before resignation.  
**Remediation:** Termination for cause, pursue injunction (prevent competitor use of data), criminal complaint (computer fraud), implement offboarding DLP controls (enhanced monitoring for 30 days pre-departure).

### 4.6 Phase 6: Recovery

**Responsibility:** IT Operations + Business Units  
**SLA:** Critical: 24 hours, High: 3 days, Medium: 7 days

**Recovery Objectives:**
- Restore normal business operations
- Mitigate business impact (data recovery, customer notification, contract remediation)
- Monitor for recurrence

**Recovery Actions:**

#### 4.6.1 Data Recovery (if possible)

- **Request deletion:** Contact recipient (if legitimate external party), request deletion and confirm
- **Legal injunction:** Court order to prevent use/disclosure (if malicious exfiltration)
- **Data breach notification:** Notify affected individuals (FADP Article 24, GDPR Articles 33-34) if required
- **Regulatory notification:** Notify FDPIC (Swiss) or DPA (EU) if required (GDPR: 72 hours from breach discovery)

#### 4.6.2 Business Continuity

- **Customer notification:** If customer data breached, notify customers per SLA/contract
- **Partner notification:** If shared data breached, notify partners
- **Contract remediation:** Address breach of contract obligations
- **Reputational management:** Public relations, media response (if public incident)

#### 4.6.3 Monitoring for Recurrence

- **Enhanced user monitoring:** 30-90 days of elevated DLP scrutiny for involved users
- **Pattern detection:** Monitor for similar incidents (same data type, channel, user cohort)
- **Policy compliance verification:** Quarterly audit of remediation effectiveness

### 4.7 Phase 7: Post-Incident Review (Lessons Learned)

**Responsibility:** Incident Response Lead + CISO + Stakeholders  
**SLA:** Critical: 7 days post-closure, High: 14 days, Medium: 30 days

**Post-Incident Review Objectives:**
- Document what happened (timeline, root cause, impact)
- Evaluate response effectiveness (what went well, what didn't)
- Identify systemic improvements (policy, technology, process, training)
- Share lessons learned (organization-wide learning)

**Post-Incident Review Agenda:**

1. **Incident Summary** (5 min)
   - What happened? (factual timeline)
   - What was the impact? (business, regulatory, reputational)

2. **Response Effectiveness** (10 min)
   - Did we detect quickly? (MTTD - Mean Time To Detect)
   - Did we respond quickly? (MTTR - Mean Time To Respond, containment SLA)
   - Did we investigate thoroughly? (evidence quality, root cause identification)
   - Did we remediate effectively? (gap closure, recurrence prevention)

3. **What Went Well** (5 min)
   - Celebrate successes (fast detection, good collaboration, effective containment)

4. **What Could Be Improved** (10 min)
   - Identify gaps (detection gaps, response delays, communication issues)
   - Prioritize improvements (high-impact, low-effort first)

5. **Action Items** (5 min)
   - Document improvements (policy updates, technology enhancements, training)
   - Assign owners and deadlines
   - Track completion (quarterly review)

**Output:** Post-incident review report, action item tracker, policy/procedure updates

---

## 5. Breach Notification Requirements

### 5.1 Legal Obligations

Organizations SHALL comply with data breach notification requirements:

#### 5.1.1 Swiss FADP (Article 24)

**Obligation:** Notify FDPIC "as soon as possible" if breach "likely to result in high risk to personality or fundamental rights" of data subjects.

**Threshold:** High risk (not all breaches require notification)

**Examples Requiring Notification:**
- Mass PII breach (>1000 individuals)
- Special categories of personal data (health, biometric, GDPR Article 9 equivalent)
- Financial data enabling fraud (bank accounts, credit cards)
- Credentials enabling identity theft (SSN equivalent)

**Examples NOT Requiring Notification:**
- Low-volume breach (<10 individuals)
- Data encrypted/pseudonymized (risk mitigated)
- Data already public (no new risk)
- Breach prevented (DLP blocked exfiltration before disclosure)

**Notification Content:**
- Nature of breach (what data, how many individuals)
- Likely consequences (fraud risk, identity theft risk)
- Measures taken or proposed (containment, remediation)

**Timeline:** "As soon as possible" (no specific deadline, interpret as <72 hours)

#### 5.1.2 EU GDPR (Articles 33-34)

**Obligation:** Notify DPA within 72 hours of breach discovery (Article 33) AND notify data subjects "without undue delay" if high risk (Article 34).

**Threshold:** Notify DPA for all breaches UNLESS "unlikely to result in risk" to rights and freedoms of data subjects.

**DPA Notification (Article 33):**
- Nature of breach
- Categories and approximate number of data subjects affected
- Categories and approximate number of records affected
- Likely consequences
- Measures taken or proposed
- Contact point (DPO)

**Data Subject Notification (Article 34):**
- Required if breach "likely to result in high risk" to rights and freedoms
- Content: Nature of breach, contact point, likely consequences, measures taken
- Exemptions: Encrypted data, subsequent measures reduce risk, disproportionate effort (public communication instead)

**Timeline:** DPA notification within 72 hours of discovery, data subject notification "without undue delay"

### 5.2 Breach Notification Decision Process

**Decision-Maker:** Data Protection Officer (DPO) in consultation with Legal and CISO

**Decision Criteria:**
1. **Is personal data involved?** (If no → not a data breach under FADP/GDPR)
2. **Was data exfiltrated?** (If DLP blocked → likely no breach, but document decision)
3. **What is the risk level?** (High risk → notify, low risk → document but may not notify)
4. **Are there exemptions?** (Encrypted data, measures reducing risk)
5. **What is the timeline?** (GDPR: 72 hours to DPA, FADP: "as soon as possible")

**Documentation:** Breach notification decision SHALL be documented (whether or not notification is required) for audit purposes (GDPR Article 33(5) - breach register).

---

## 6. Escalation Matrix

### 6.1 Internal Escalation

| Incident Severity | Immediate Notification | Within 1 Hour | Within 4 Hours | Within 24 Hours |
|-------------------|------------------------|---------------|----------------|-----------------|
| **Critical** | Incident Response Lead, SOC Lead | CISO, DPO, Data Owner | Legal, HR, Exec Management | Board (if regulatory/reputational) |
| **High** | Incident Response Lead | SOC Lead, Data Owner | CISO, DPO | Legal, HR (if disciplinary) |
| **Medium** | SOC Lead | Incident Response Team | Data Owner | Manager |
| **Low** | SOC Analyst | - | Manager (if repeated) | - |

### 6.2 External Escalation

| Scenario | Authority | Timeline | Rationale |
|----------|-----------|----------|-----------|
| **Breach notification (FDPIC)** | DPO/Legal + CISO | "As soon as possible" (<72h) | Swiss FADP Article 24 |
| **Breach notification (EU DPA)** | DPO/Legal + CISO | 72 hours from discovery | GDPR Article 33 |
| **Law enforcement** | CISO + Legal + Exec Management | Case-by-case | Criminal activity, espionage, sabotage |
| **Cyber insurance** | CISO + Legal | 24-48 hours | Policy requirement, forensic support |
| **External IR firm** | CISO | Case-by-case | Resource constraint, specialized expertise |

---

## 7. Documentation Requirements

### 7.1 Incident Ticket

ALL DLP incidents (Medium and above) SHALL be documented in incident ticketing system:

**Required Fields:**
- Incident ID (unique identifier)
- Severity (Critical/High/Medium/Low)
- Date/time detected
- Detected by (SOC analyst, automated alert)
- User involved (identity, role, department, manager)
- Data category and classification
- Channel (email, USB, web, network, etc.)
- DLP action taken (block, alert, quarantine)
- Investigation summary (timeline, findings, root cause)
- Remediation actions (what was done to close gap)
- Lessons learned (what to improve)
- Status (Open, In Progress, Resolved, Closed)

### 7.2 Forensic Evidence

For High/Critical incidents, organizations SHALL preserve forensic evidence:

**Evidence Types:**
- **DLP logs:** Export all related DLP events (90-day window minimum)
- **Endpoint forensics:** Disk image, memory dump, file system snapshot
- **Email audit:** Sent items, deleted items, forwarding rules (export from mail server)
- **Network logs:** Firewall logs, proxy logs, VPN logs (matching timeframe)
- **Authentication logs:** Login history, password changes, MFA events

**Chain of Custody:**
- Document who collected evidence, when, and how
- Hash evidence files (SHA-256) to prove integrity
- Store evidence securely (encrypted, access-controlled)
- Maintain chain of custody log (who accessed evidence, when, why)

**Legal Hold:**
- If litigation or regulatory investigation likely, implement legal hold
- Preserve ALL related data (email, files, logs) until Legal advises otherwise
- Notify custodians (users, IT admins) not to delete data

### 7.3 Breach Register (GDPR Article 33(5))

Organizations SHALL maintain a breach register documenting ALL breaches (notified or not):

**Required Fields:**
- Date/time of breach
- Nature of breach (what data, how many subjects)
- Consequences of breach (risk assessment)
- Remediation actions taken
- Notification decision (notified or not, rationale)
- DPA notification (if applicable - date, reference number)
- Data subject notification (if applicable - date, method)

**Purpose:** Demonstrate GDPR compliance to DPA during audits

---

## 8. Training and Awareness

### 8.1 Incident Response Team Training

Incident Response team members SHALL receive DLP-specific training:

**Training Topics:**
- DLP technology capabilities and limitations
- DLP alert triage and severity classification
- Forensic evidence collection and preservation
- Breach notification requirements (FADP, GDPR)
- Employee privacy and proportionality in investigations
- Interview techniques and legal considerations
- Lessons learned and continuous improvement

**Training Frequency:** Annual (minimum), refresher after major incidents

### 8.2 User Awareness

ALL employees SHALL receive DLP awareness training:

**Training Topics:**
- What is DLP and why it matters
- What data is protected (classification levels)
- What channels are monitored (email, USB, web, etc.)
- What happens if you violate policy (incident response, potential consequences)
- How to request exceptions (legitimate business needs)
- How to report suspected data leakage (incident reporting)

**Training Frequency:** Annual (minimum), during onboarding for new hires

---

## 9. Continuous Improvement

### 9.1 Metrics

Organizations SHALL track incident response metrics:

| Metric | Formula | Target |
|--------|---------|--------|
| **MTTD (Mean Time To Detect)** | Average time from data transfer to DLP alert | <5 minutes (real-time detection) |
| **MTTR (Mean Time To Respond)** | Average time from alert to containment | Critical: <15 min, High: <1 hour |
| **Incident Recurrence** | % of incidents that recur (same root cause) | <5% (effective remediation) |
| **Breach Notification Compliance** | % of breaches notified within legal timeline | 100% (GDPR 72-hour deadline) |
| **Lessons Learned Completion** | % of action items from PIR completed on time | >90% |

### 9.2 Quarterly Review

Organizations SHALL conduct quarterly incident response review:

**Review Agenda:**
- Incident volume trends (increasing, stable, decreasing)
- Common root causes (training gap, policy gap, control gap, insider threat)
- Response effectiveness (MTTD, MTTR, SLA compliance)
- Lessons learned completion (are we improving?)
- Policy updates needed (based on incident patterns)

---

## 10. Integration with DLP Framework

### 10.1 Assessment Integration

Incident response SHALL be assessed using **ISMS-IMP-A.8.12.4 (Monitoring & Response Assessment)** workbook, evaluating:
- Incident response procedures documented
- SOC/IR team trained on DLP incidents
- Escalation matrix defined and tested
- Forensic evidence collection capability
- Breach notification process defined
- Post-incident review conducted for all High/Critical incidents

### 10.2 S5.C Integration

Detailed step-by-step procedures are documented in **ISMS-POL-A.8.12-S5.C (Incident Response Procedures)** annex:
- Playbooks for common scenarios (insider threat, negligent disclosure, credential leak, mass exfiltration)
- Decision trees for severity classification
- Checklists for containment, investigation, remediation
- Templates for breach notification, user communication, post-incident review

---

## 11. References

### 11.1 Internal Policy Documents

- **ISMS-POL-A.8.12** - Master DLP Policy
- **ISMS-POL-A.8.12-S2.3** - Monitoring & Detection
- **ISMS-POL-A.5.24-28** - Organizational Incident Management
- **ISMS-POL-A.8.12-S5.C** - Incident Response Procedures (Annex)

### 11.2 Implementation Documents

- **ISMS-IMP-A.8.12.4** - Monitoring & Response Assessment

### 11.3 Regulatory References

- **Swiss FADP** - Article 24 (Data breach notification), Article 26 (Employee data processing)
- **EU GDPR** - Article 33 (Breach notification to DPA), Article 34 (Breach notification to data subjects), Article 5 (Lawfulness, fairness, transparency)
- **Swiss Employment Law** - Article 328b CO (Proportionality in employee monitoring)

---

**END OF DOCUMENT**

*"The best incident response plan is the one you never need. The second-best is the one you've practiced before the incident."*  
*— Murphy's Law of Incident Response*