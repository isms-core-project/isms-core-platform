# ISMS-POL-A.8.23-S2.4
## Web Filtering - Exception Management Requirements

**Document ID**: ISMS-POL-A.8.23-S2.4
**Title**: Web Filtering - Exception Management Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial exception management framework |

**Review Cycle**: Annual (or upon changes to risk management framework)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Information Security Manager
- Risk Management: Risk Manager / Compliance Officer

**Distribution**: Security team, IT operations, business unit managers  
**Related Documents**: ISMS-POL-A.8.23-S5.B (Exception Request Form), Risk Management Policy

---

## 2.4.1 Purpose and Scope

This section establishes requirements for **managing exceptions** to web filtering policies - the controlled process for deviating from standard filtering rules when business requirements justify the risk.

**Core Principle**: Exceptions are not failures - they are **risk-based decisions** where business need outweighs security benefit of strict enforcement. However, exceptions **SHALL** be:
- Justified with clear business rationale
- Approved by appropriate authority
- Documented and auditable
- Time-limited or periodically reviewed
- Compensated with alternative controls where feasible
- Minimal in scope (least privilege principle)

**In Scope**: Exception request, approval, implementation, documentation, review, and revocation processes  
**Primary Stakeholders**: CISO, Security Team, Business Unit Managers, IT Operations  
**Implementation Evidence**: ISMS-IMP-A.8.23.3 (Policy Configuration Assessment), ISMS-IMP-A.8.23.4 (Monitoring & Response Assessment)

---

## 2.4.2 Types of Exceptions

### 2.4.2.1 Category-Based Exceptions

**Definition**: Allowing access to blocked website categories for specific users or groups.

**Examples**:
- Marketing team requires access to social media platforms (category normally blocked)
- Research team requires access to competitor websites (category monitored/restricted)
- Security team requires access to malware analysis sites (high-risk category)

**Scope**: Typically user-based or role-based

### 2.4.2.2 URL/Domain-Specific Exceptions

**Definition**: Allowing access to specific URLs or domains that would otherwise be blocked.

**Examples**:
- Legitimate business site incorrectly categorized and blocked
- Partner/vendor portal requiring allowlist entry
- Cloud service provider domain needed for business operations

**Scope**: Typically organization-wide or user-group-based

### 2.4.2.3 Threat Protection Exceptions

**Definition**: Bypassing threat protection controls (malware, phishing blocking) for specific purposes.

**Examples**:
- Security research requiring access to malware samples
- Incident response investigation requiring access to phishing infrastructure
- Threat intelligence gathering from suspicious sites

**Scope**: Extremely limited - typically individual users in isolated environments

**WARNING**: Threat protection exceptions are **high-risk** and require strictest controls.

### 2.4.2.4 Technical Exceptions

**Definition**: Bypassing filtering for technical reasons unrelated to content.

**Examples**:
- Application compatibility (filtering breaks legitimate application functionality)
- Performance optimization (bypass filtering for high-bandwidth, low-risk traffic)
- Network architecture constraints (certain network segments cannot route through filtering)

**Scope**: Varies - may be organization-wide, network-segment-specific, or application-specific

---

## 2.4.3 Exception Request Process

### 2.4.3.1 Request Initiation

Exception requests **SHALL** be initiated through formal process:

**Requestor Responsibilities**:
- Submit exception request via defined channel (ticketing system, self-service portal, email to security team)
- Provide business justification (why exception is needed)
- Specify scope (who/what needs exception, for how long)
- Propose compensating controls (if applicable)
- Accept accountability for risk

**Request Information Requirements**:
- Requestor name, department, manager
- Type of exception (category, URL/domain, threat protection, technical)
- Specific sites/categories requiring exception
- Business justification (detailed explanation of need)
- Affected users/systems (scope of exception)
- Duration requested (temporary vs. permanent)
- Proposed compensating controls or risk mitigations
- Date submitted

### 2.4.3.2 Initial Review

Security Team **SHALL** conduct initial review within defined SLA:

**Review SLA**: 
- **Standard requests**: 3-5 business days
- **Urgent requests**: 1 business day (requires manager approval for urgency)
- **Emergency requests**: 4 business hours (see Emergency Exception Process)

**Review Activities**:
- Validate business justification (is need legitimate and reasonable?)
- Assess security risk (what threats does exception expose organization to?)
- Check for alternatives (can business need be met without exception?)
- Verify requestor authority (is requestor authorized to request on behalf of users?)
- Recommend approve/deny/modify to approval authority

### 2.4.3.3 Risk Assessment

Security Team **SHALL** conduct risk assessment for exception requests:

**Risk Factors to Evaluate**:
- **Threat exposure**: What malicious content could users encounter?
- **Data leakage risk**: Could exception enable unauthorized data exfiltration?
- **Compliance impact**: Does exception violate regulatory requirements?
- **Scope impact**: How many users/systems affected?
- **Duration impact**: Temporary exception less risky than permanent
- **User awareness**: Are affected users trained to recognize threats?
- **Compensating controls**: What other protections exist?

**Risk Rating**: HIGH / MEDIUM / LOW (documented in exception record)

### 2.4.3.4 Enhanced Approval for Privileged Users

Exception requests from privileged users (administrators, security personnel, users with elevated access rights) **SHALL** receive enhanced scrutiny due to:
- Greater potential impact of security incidents involving privileged accounts
- Higher likelihood of targeting by sophisticated threat actors
- Expanded access to sensitive systems and data

**Additional Requirements for Privileged User Exceptions**:
- **Approval Authority**: Minimum CISO level (cannot be delegated to Information Security Manager)
- **Review Frequency**: Quarterly (vs. annual for standard exceptions)
- **Compensating Controls**: Mandatory (enhanced logging, behavior analytics, session recording where technically feasible)
- **Justification Standard**: Must demonstrate specific technical need, not general convenience

See Section 1.2.1.4 for applicability definition and S3 (Roles & Responsibilities) for privileged user categorization.

### 2.4.3.5 Approval Authority

Exception approvals **SHALL** follow defined authority levels based on risk:

| Risk Level | Approval Authority | Additional Requirements |
|------------|-------------------|-------------------------|
| **LOW** | Security Team Lead | None |
| **MEDIUM** | CISO or Deputy | Business manager confirmation |
| **HIGH** | CISO + Senior Management | Documented risk acceptance, compensating controls mandatory |

**Threat protection exceptions**: Always **HIGH** risk - require CISO approval regardless of scope

**Permanent exceptions**: Require higher approval authority than temporary (e.g., MEDIUM risk temporary = Security Team Lead, MEDIUM risk permanent = CISO)

### 2.4.3.6 Approval Decision

Approver **SHALL** make decision within defined timeframe:

- Review request, business justification, and risk assessment
- Approve, deny, or request modifications
- Document decision rationale
- Specify conditions or limitations on approval (e.g., "approved for 6 months, review after 3 months")

**Denial**: If denied, provide clear explanation and suggest alternatives if available

**Conditional Approval**: Approve with conditions (e.g., enhanced logging, user training, limited scope)

---

## 2.4.4 Exception Implementation

### 2.4.4.1 Implementation Requirements

Approved exceptions **SHALL** be implemented by IT Operations/Security Team:

- Configure filtering solution to implement exception (allowlist, category override, user group policy)
- Test exception (verify users can access previously blocked resources)
- Document technical implementation details
- Enable enhanced logging/monitoring for exception (if applicable)
- Notify requestor of implementation completion

**Implementation SLA**: Within 2 business days of approval (urgent requests: same business day)

### 2.4.4.2 Least Privilege Principle

Exceptions **SHALL** be implemented with minimum necessary scope:

**User Scope**: Grant exception only to users who need it (not organization-wide unless justified)

**Site Scope**: Allow only specific URLs/domains needed (not entire categories unless justified)

**Time Scope**: Implement shortest duration meeting business need

**Network Scope**: Limit to specific network segments if possible

**Example - Good Exception**:
> "Allow marketing@company.com access to linkedin.com and twitter.com for 12 months (renewable) for social media management purposes."

**Example - Bad Exception**:
> "Allow everyone access to all social media sites permanently because someone in marketing needs LinkedIn."

### 2.4.4.3 Technical Controls

Where technically feasible, exceptions **SHOULD** include:

**Enhanced Monitoring**:
- Increased logging verbosity for exception usage
- Alerting on anomalous usage patterns
- Periodic usage reports to exception owner

**Time-Based Controls**:
- Automatic expiration of exception at end of approved period
- Time-of-day restrictions (e.g., allow social media only during business hours)

**Network Isolation** (for high-risk exceptions):
- Dedicated network segment or VLAN
- Additional egress filtering
- Separate internet breakout

---

## 2.4.5 Exception Documentation

### 2.4.5.1 Exception Register

Organizations **SHALL** maintain central Exception Register documenting all active exceptions:

**Required Information**:
- Exception ID (unique identifier)
- Type (category, URL/domain, threat protection, technical)
- Description (what is being excepted)
- Affected users/systems (scope)
- Business justification
- Risk rating (HIGH/MEDIUM/LOW)
- Approver and approval date
- Implementation date
- Expiration date (or "permanent" with review date)
- Compensating controls
- Review frequency
- Current status (Active, Expired, Revoked, Under Review)
- Last review date and outcome

### 2.4.5.2 Audit Trail

Organizations **SHALL** maintain audit trail for exception lifecycle:

- Request submitted (who, when, what)
- Review activities (who reviewed, risk assessment)
- Approval decision (who approved/denied, when, rationale)
- Implementation (who implemented, when, technical details)
- Reviews (when reviewed, outcome, any changes)
- Revocation (who revoked, when, reason)

Audit trail **SHALL** be retained per organizational record retention policy (minimum 3 years recommended).

### 2.4.5.3 Reporting

Security Team **SHALL** generate exception reports:

**Monthly**:
- Active exceptions summary (count by type, risk level)
- New exceptions approved/denied
- Exceptions expiring soon (30-day warning)
- High-risk exception review

**Quarterly**:
- Exception trend analysis (growing, stable, declining)
- Risk posture assessment (cumulative risk from exceptions)
- Recommendations for policy adjustments (if many similar exceptions, maybe policy should change)

**Annual**:
- Comprehensive exception review for ISMS audit
- Exception process effectiveness assessment
- Recommendations for process improvements

---

## 2.4.6 Exception Review and Renewal

### 2.4.6.1 Periodic Review

Active exceptions **SHALL** be reviewed periodically:

**Review Frequency**:
- **High-risk exceptions**: Quarterly
- **Medium-risk exceptions**: Semi-annually
- **Low-risk exceptions**: Annually
- **Permanent exceptions**: Annually (regardless of risk)
- **Threat protection exceptions**: Monthly (highest scrutiny)

### 2.4.6.2 Review Activities

During review, Security Team **SHALL**:

- Verify exception is still needed (contact business owner)
- Assess if risk profile has changed (new threats, policy changes)
- Confirm users still require access (personnel changes?)
- Review usage logs (is exception being used as expected?)
- Evaluate if alternatives now exist (better solutions available?)
- Update exception documentation
- Recommend: Renew, Modify, or Revoke

### 2.4.6.3 Renewal Process

If exception should continue, owner **SHALL** request renewal:

- Reconfirm business need (justification may have changed)
- Update scope if needed (add/remove users, extend duration)
- Reassess risk (same approval authority as original request)
- Document renewal decision

**Automatic Expiration**: If exception is not renewed before expiration date, it **SHALL** be automatically revoked (access blocked).

### 2.4.6.4 Modification Process

If exception scope needs to change:

- Submit modification request (similar to original request)
- Expansion of scope (more users, broader access): Requires same approval as new exception
- Reduction of scope (fewer users, narrower access): Security Team can approve without escalation
- Document modification in exception record

---

## 2.4.7 Exception Revocation

### 2.4.7.1 Revocation Triggers

Exceptions **SHALL** be revoked when:

- Expiration date reached and not renewed
- Business need no longer exists
- Security incident linked to exception (compromise via excepted access)
- Policy change eliminates need for exception (category now allowed by default)
- User/system no longer requires access (personnel departure, system decommissioning)
- Risk profile changes making exception unacceptable (new threat intelligence)
- Compliance requirement prohibits exception (regulatory change)
- Exception owner requests revocation

### 2.4.7.2 Revocation Process

Revoking authority **SHALL**:

- Document revocation reason
- Notify affected users/systems (advance notice where feasible)
- Remove exception from filtering configuration
- Verify access is properly blocked
- Update Exception Register status to "Revoked"
- Archive exception record for audit purposes

**Revocation SLA**: Within 1 business day of revocation decision (immediate for security incidents)

### 2.4.7.3 Emergency Revocation

For security incidents, exceptions **MAY** be revoked immediately:

- No advance notice to users (security takes precedence)
- CISO or Security Team Lead authority
- Document reason in exception record
- Investigate incident to determine if exception was attack vector
- Report findings to management

---

## 2.4.8 Compensating Controls

### 2.4.8.1 Risk Mitigation

High-risk exceptions **SHALL** implement compensating controls to reduce risk:

**Common Compensating Controls**:
- **Enhanced Monitoring**: Increased logging, alerting on anomalous behavior
- **User Training**: Security awareness specific to exception risks
- **Network Isolation**: Separate VLAN, additional egress controls
- **Endpoint Protection**: Enhanced AV/EDR on systems using exception
- **Time Restrictions**: Limit exception to specific hours/days
- **Manager Oversight**: Regular review of usage reports by business manager
- **Dual Authorization**: Require two users to authorize high-risk actions

### 2.4.8.2 Documentation

Compensating controls **SHALL** be:

- Documented in exception record
- Verified during implementation
- Tested for effectiveness
- Reviewed during periodic exception reviews
- Updated if controls change or prove ineffective

---

## 2.4.9 Emergency Exception Process

### 2.4.9.1 Emergency Definition

**Emergency Exception**: Immediate access required for critical business need where standard approval process would cause unacceptable business disruption.

**Valid Emergency Scenarios**:
- Production outage requiring access to blocked vendor support site
- Security incident investigation requiring access to threat intelligence source
- Executive travel requiring urgent access to blocked collaboration tool
- Critical deadline where delay in approval would cause significant financial/reputational harm

**Invalid Emergency Scenarios**:
- Poor planning (knew need in advance, didn't request)
- Convenience (don't want to wait for standard process)
- Personal preference (user preference, not business requirement)

### 2.4.9.2 Emergency Approval

Emergency exceptions **MAY** be approved verbally by:

- CISO (any risk level)
- Security Team Lead (LOW/MEDIUM risk only)
- IT Operations Manager (LOW risk, after-hours only)

**Emergency Approval Requirements**:
- Verbal approval documented immediately (email, ticket, incident log)
- Business justification captured (why emergency, what's the impact of delay)
- Scope minimized (shortest duration, fewest users possible)
- Formal exception request submitted within **1 business day** (retroactive documentation)
- Formal approval decision within **3 business days** (validate emergency was legitimate)

### 2.4.9.3 Post-Emergency Review

After emergency, Security Team **SHALL**:

- Validate emergency was legitimate (was urgency justified?)
- Assess if standard process should be improved (was delay unreasonable?)
- Review usage during emergency (was access used appropriately?)
- Determine if exception should continue (convert to standard exception or revoke)
- Document lessons learned (prevent future emergencies where possible)

**Abuse of Emergency Process**: Repeated "emergencies" from same user/department indicate planning failure or process abuse - escalate to management.

---

## 2.4.10 User Communication

### 2.4.10.1 Request Status Updates

Requestors **SHALL** receive status updates:

- Request received acknowledgment (automated, immediate)
- Under review notification (within 1 business day)
- Approval/denial decision (within defined SLA)
- Implementation completion (when exception is active)
- Expiration warnings (30 days, 7 days, 1 day before expiration)
- Revocation notification (if exception revoked)

### 2.4.10.2 Exception Awareness

Users granted exceptions **SHALL** be informed:

- What exception provides (which sites/categories are accessible)
- Duration of exception (when it expires)
- Responsibilities (acceptable use, security awareness)
- Risks (potential threats from excepted access)
- Reporting procedures (how to report issues, security concerns)

### 2.4.10.3 Training

Users with high-risk exceptions **SHOULD** receive additional security training:

- Threat awareness specific to excepted content (e.g., malware analysis training for security researchers)
- Incident reporting procedures
- Safe handling practices
- Organizational responsibilities

---

## 2.4.11 Metrics and Continuous Improvement

### 2.4.11.1 Exception Metrics

Organizations **SHALL** track:

**Volume Metrics**:
- Total active exceptions (trend over time)
- Exceptions by type (category, URL, threat, technical)
- Exceptions by risk level (HIGH/MEDIUM/LOW)
- New exceptions per month
- Expired/revoked exceptions per month

**Process Metrics**:
- Request-to-approval cycle time
- Approval rate (percentage approved vs. denied)
- Emergency exception frequency
- Exception renewal rate (percentage renewed vs. expired)

**Risk Metrics**:
- Cumulative risk score (sum of all exception risks)
- Incidents linked to exceptions (security events involving excepted access)
- Compensating control effectiveness

### 2.4.11.2 Process Improvement

Organizations **SHALL** review exception process annually:

- Analyze metrics for trends (growing number of exceptions = policy too restrictive?)
- Identify process bottlenecks (slow approvals, unclear requirements)
- Solicit user feedback (is process reasonable, overly bureaucratic?)
- Benchmark against industry practices
- Implement improvements based on findings

**Red Flags**:
- >50% approval rate (are requests being rubber-stamped?)
- <10% approval rate (is policy too rigid? Are users bypassing process?)
- Growing backlog of pending requests (process not scaling)
- Frequent emergency exceptions (standard process too slow or users not planning)

---

## 2.4.12 Compliance and Audit

### 2.4.12.1 Audit Evidence

Exception Register **SHALL** serve as primary audit evidence for:

- ISO 27001 audits (demonstrate controlled exception process)
- Regulatory compliance audits (show risk-based decision making)
- Internal audits (verify policy compliance)

### 2.4.12.2 Audit Procedures

During audits, organizations **SHALL** be able to:

- Produce complete Exception Register
- Show approval workflows and authorities
- Demonstrate periodic reviews are conducted
- Provide examples of denied requests (not rubber-stamping)
- Show risk assessments for high-risk exceptions
- Demonstrate exceptions are actually implemented as documented (test sample)

### 2.4.12.3 Non-Compliance

Bypassing exception process (unauthorized exceptions) **SHALL** be treated as policy violation:

- Investigation by Security Team
- Revocation of unauthorized exception
- Disciplinary action per HR policy
- Root cause analysis (why was process bypassed?)
- Process improvement if legitimate gap identified

---

**END OF DOCUMENT**