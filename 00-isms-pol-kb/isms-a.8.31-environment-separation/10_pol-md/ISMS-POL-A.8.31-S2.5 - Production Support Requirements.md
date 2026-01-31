# ISMS-POL-A.8.31-S2.5
## Environment Separation - Production Support Requirements

**Document ID**: ISMS-POL-A.8.31-S2.5  
**Title**: Production Support Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / IT Operations | Initial production support requirements |

**Review Cycle**: Annual (or upon incident management process changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager
- Service Delivery: Service Delivery Manager

**Distribution**: Security team, IT operations, incident response team, developers  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary)
- ISMS-POL-A.8.31-S2.2 (Access Control Requirements)
- ISMS-POL-A.5.24-27 (Incident Management)
- ISMS-POL-A.8.2-3-5 (PAM and Authentication)

---

## 2.5.1 Purpose and Scope

This section establishes requirements for supporting production systems while maintaining environment separation.

**The Production Support Challenge**:
- Production issues require investigation and troubleshooting
- Developers may need to assist with production incidents
- Support must balance security (restrictive access) with operational efficiency (quick resolution)
- Environment separation cannot make production unsupportable

**In Scope**: Production monitoring, troubleshooting, incident response, emergency access  
**Primary Stakeholder**: IT Operations, Incident Response, Support Teams  
**Key Balance**: Security (limited access) vs. Operability (effective support)

---

## 2.5.2 Production Monitoring and Observability

### 2.5.2.1 Read-Only Monitoring Access

[Organization] **SHALL** provide read-only monitoring access for production support:

**Permitted Read-Only Access**:
- **Operations Team**: Full monitoring access (metrics, logs, traces, dashboards)
- **Developers**: Limited monitoring access (application logs, metrics - NO system logs, NO sensitive data)
- **Security Team**: Full monitoring access (security events, audit logs, system logs)
- **Service Desk**: Dashboard access only (service status, basic metrics)

**Monitoring Tools and Access**:
- Application Performance Monitoring (APM): New Relic, Datadog, Dynatrace - read-only dashboards
- Log aggregation (SIEM): Splunk, ELK, CloudWatch - query access with data masking
- Metrics/dashboards: Grafana, Prometheus - read-only viewing
- Distributed tracing: Jaeger, Zipkin - read-only trace viewing

**Data Sensitivity in Logs**:
- Personal data REDACTED from logs (email addresses, names, etc.)
- Credentials NEVER logged (passwords, API keys)
- Payment card data NEVER logged (PCI DSS requirement)
- Sensitive business data MASKED in logs

**Audit Verification Criteria**:
- ✅ Monitoring access documented per role
- ✅ Read-only access enforced (cannot modify logs/metrics)
- ✅ Sensitive data redacted from logs
- ✅ Monitoring access reviewed quarterly

### 2.5.2.2 Alerting and Notification

[Organization] **SHALL** implement production alerting while respecting environment separation:

**Alert Routing**:
- **Critical alerts** (production down, security incidents): Operations on-call + Security team
- **High-priority alerts** (performance degradation, errors): Operations team + Incident Commander
- **Medium-priority alerts** (warnings, capacity issues): Operations team (business hours)
- **Low-priority alerts** (informational): Operations team (weekly digest)

**Developer Notification** (not direct production access):
- Developers notified of application errors (via monitoring tools)
- Developers receive sanitized log excerpts (sensitive data removed)
- Developers DO NOT receive production access for investigation
- Developers support operations team remotely (screen sharing, guidance)

**Audit Verification Criteria**:
- ✅ Alert routing configured per priority
- ✅ Developers receive notifications (not production access)
- ✅ Sensitive data removed from alert content
- ✅ Alert noise managed (false positive rate <10%)

---

## 2.5.3 Production Troubleshooting

### 2.5.3.1 Troubleshooting Without Production Access

[Organization] **SHALL** enable troubleshooting without granting developers production access:

**Remote Troubleshooting Methods**:

**1. Enhanced Logging and Monitoring**:
- Comprehensive application logging (capture errors, stack traces, context)
- Distributed tracing (trace requests across services)
- Performance profiling (identify bottlenecks without system access)
- Error aggregation (Sentry, Rollbar - developers see application errors without system access)

**2. Synthetic Data Reproduction**:
- Reproduce issues in staging using sanitized production data
- Developers troubleshoot in staging (not production)
- Issue fixed in dev/test/staging, then promoted to production

**3. Screen Sharing and Remote Support**:
- Operations team shares screen with developer (read-only viewing)
- Developer guides operations team through troubleshooting steps
- Developer DOES NOT control operations team system
- Session recorded for audit

**4. Diagnostic Modes and Debug Logging**:
- Temporary debug logging enabled in production (specific module only)
- Debug logs automatically disabled after timeframe (4 hours)
- Debug logs sanitized (sensitive data removed before developer viewing)

**Audit Verification Criteria**:
- ✅ Troubleshooting procedures documented (no direct dev access required)
- ✅ Screen sharing sessions recorded
- ✅ Debug logging time-limited and sanitized
- ✅ Issues reproduced in staging when possible

### 2.5.3.2 Production Incident Response

[Organization] **SHALL** follow defined incident response procedures maintaining environment separation:

**Incident Response Tiers**:

**Tier 1 (Operations Team)**:
- Investigate using monitoring tools and logs
- Execute runbooks (documented troubleshooting procedures)
- Restart services, apply known fixes
- Escalate to Tier 2 if unresolved

**Tier 2 (Senior Operations + On-Call Developer - Remote)**:
- Operations shares screen, developer guides remotely
- Developer analyzes logs/metrics (read-only access)
- Developer proposes solutions (operations executes)
- Escalate to Tier 3 if developer access required

**Tier 3 (Emergency Break-Glass)**:
- Developer requires production access (cannot resolve remotely)
- Incident Commander + CISO approve break-glass
- Developer accesses production via PAM (time-limited)
- Session recorded, post-incident review mandatory

**Incident Communication**:
- Incident declared and logged (ticket system)
- Stakeholders notified (business, security, management)
- Status updates provided (regular cadence during incident)
- Post-incident review completed (lessons learned)

**Audit Verification Criteria**:
- ✅ Incident response procedures documented and followed
- ✅ Tier 1/2 incidents resolved without developer production access (>80%)
- ✅ Tier 3 break-glass approved and documented
- ✅ Post-incident reviews completed within 48 hours

---

## 2.5.4 Break-Glass Emergency Access (Detailed Requirements)

### 2.5.4.1 Break-Glass Conditions (Reiteration from S2.2)

[Organization] **SHALL** grant temporary developer production access only under these conditions:

**Approved Break-Glass Scenarios**:
- Severity 1 production incident (complete service outage, data loss risk)
- Security incident requiring developer expertise (active exploitation, vulnerability patching)
- Critical bug fix requiring immediate code change (cannot wait for normal deployment)
- Operations team unable to resolve issue without developer expertise
- Remote troubleshooting insufficient (issue cannot be diagnosed remotely)

**PROHIBITED Break-Glass Usage**:
- Convenience (developer wants to "check something quickly")
- Training (new developer wants to "see production")
- Curiosity (developer wants to "explore production environment")
- Non-critical issues (can wait for normal troubleshooting process)

**Audit Verification Criteria**:
- ✅ Break-glass policy documented and communicated
- ✅ Break-glass usage criteria enforced
- ✅ Denied break-glass requests logged (attempted misuse)
- ✅ <10 break-glass activations per year (trending down)

### 2.5.4.2 Break-Glass Access Lifecycle

[Organization] **SHALL** manage break-glass access with strict controls:

**Access Request Process**:
1. **Incident Declared**: Incident Commander declares Severity 1 incident (formal declaration)
2. **Remote Troubleshooting Attempted**: Tier 1/2 troubleshooting exhausted (documented)
3. **Access Justification**: Developer documents why production access required
4. **Dual Approval**: Incident Commander + Security Team approve (or CISO if available)
5. **PAM Checkout**: Developer checks out temporary production credentials (4-hour expiration)
6. **Session Recording**: All developer activity in production recorded (video + audit log)

**Access Restrictions**:
- Time-limited: 4 hours maximum (extendable with re-approval)
- Scope-limited: Access to specific systems only (not full production access)
- Action-limited: Read-only preferred, write access only if necessary
- Monitored: Real-time monitoring of developer actions

**Access Expiration**:
- Automatic: Credentials expire after 4 hours
- Early termination: Developer completes task, checks in credentials early
- Forced revocation: Security team can revoke access immediately if misuse detected

**Post-Access Review**:
- Mandatory: Post-incident review within 48 hours
- Session review: Recorded session reviewed by security team
- Actions validated: All developer actions in production reviewed and justified
- Documentation: Break-glass usage documented in incident report

**Audit Verification Criteria**:
- ✅ 100% of break-glass access approved (dual approval)
- ✅ 100% of break-glass sessions recorded
- ✅ 100% of break-glass sessions reviewed post-incident
- ✅ Average break-glass duration <2 hours (quick resolution)

---

## 2.5.5 Production Debugging Without Data Exposure

### 2.5.5.1 Safe Production Debugging Techniques

[Organization] **SHALL** enable production debugging without exposing sensitive data:

**Debugging Methods**:

**1. Application Error Tracking** (Sentry, Rollbar, Bugsnag):
- Errors automatically reported to developers (no production access needed)
- Stack traces and context captured
- Sensitive data scrubbed from error reports
- Developers see application behavior without system access

**2. Session Replay** (LogRocket, FullStory - with privacy controls):
- User sessions recorded (clicks, navigation, errors)
- Personal data masked (form inputs, names, etc.)
- Developers replay sessions to understand user issues
- Privacy-compliant (GDPR consent, data minimization)

**3. Feature Flags and Canary Deployments**:
- New features deployed but disabled (flag = off)
- Feature enabled for small user subset (canary release)
- Developers monitor canary metrics in real-time
- If issues detected, feature flag disabled (instant rollback without code deployment)

**4. Synthetic Monitoring and E2E Tests**:
- Automated tests run in production (synthetic users)
- Tests validate critical functionality continuously
- Developers notified if tests fail (indicates production issue)
- No real user data involved (synthetic test accounts)

**Audit Verification Criteria**:
- ✅ Error tracking configured with data scrubbing
- ✅ Session replay (if used) privacy-compliant
- ✅ Feature flags used for controlled releases
- ✅ Synthetic monitoring covers critical paths

### 2.5.5.2 Production Data Anonymization for Support

[Organization] **MAY** extract production data for support purposes IF properly anonymized:

**When Production Data Extraction Permitted**:
- Critical bug requiring realistic data for reproduction
- Performance issue requiring production-scale data analysis
- Data corruption investigation requiring specific records
- DPO approval + CISO approval REQUIRED

**Data Extraction and Anonymization Process**:
1. **Request**: Developer requests specific production data subset
2. **DPO Approval**: DPO reviews request and approves anonymization approach
3. **Extraction**: Operations team extracts data from production
4. **Anonymization**: Data anonymized per approved technique (see S2.3 and Annex B)
5. **Verification**: DPO verifies anonymization effectiveness
6. **Transfer**: Anonymized data provided to developer (in non-production environment)
7. **Deletion**: Anonymized data deleted after use (30-day maximum retention)

**Anonymization Requirements**:
- Personal data removed or masked
- Re-identification impossible (k-anonymity validation)
- Data minimization (only necessary records extracted)
- Audit trail (who extracted, what data, why, when deleted)

**Audit Verification Criteria**:
- ✅ All production data extractions approved (DPO + CISO)
- ✅ Anonymization effectiveness verified
- ✅ Extracted data deleted per retention policy (30 days)
- ✅ Extraction audit trail maintained

---

## 2.5.6 Runbooks and Standard Operating Procedures

### 2.5.6.1 Production Runbook Requirements

[Organization] **SHALL** maintain runbooks for common production support tasks:

**Runbook Coverage**:
- Application restart procedures
- Log file analysis (where to find logs, how to interpret)
- Common error resolution (troubleshooting steps)
- Performance tuning (configuration changes for common issues)
- Health check procedures (validate system health)
- Rollback procedures (revert to previous version)
- Emergency contact list (who to call for specific issues)

**Runbook Maintenance**:
- Runbooks version controlled (Wiki, Git repository)
- Runbooks updated after incidents (lessons learned incorporated)
- Runbooks tested periodically (disaster recovery drills)
- Runbooks accessible to operations team 24/7 (online, offline copy)

**Runbook Security**:
- Runbooks DO NOT contain credentials (reference PAM vault instead)
- Runbooks accessible to operations team only (not developers)
- Sensitive runbooks encrypted (disaster recovery procedures)

**Audit Verification Criteria**:
- ✅ Runbooks documented for critical systems (100% coverage)
- ✅ Runbooks updated within 30 days of incidents
- ✅ Runbooks tested annually
- ✅ No credentials in runbooks

---

## 2.5.7 Vendor and Third-Party Production Support

### 2.5.7.1 Vendor Production Support Requirements

[Organization] **SHALL** control vendor production access per same principles as employees:

**Vendor Production Access Restrictions**:
- Vendors cannot access production independently (supervised access only)
- Vendor access via screen sharing (operations team controls system)
- Vendor sessions recorded and reviewed
- Vendor access time-limited (support session duration only)
- Vendor NDA and data protection agreement required

**Vendor Support Process**:
1. **Support Request**: [Organization] opens support ticket with vendor
2. **Initial Troubleshooting**: Vendor troubleshoots using logs/info provided by [Organization]
3. **If Remote Access Needed**: Vendor requests production access (CISO approval)
4. **Screen Sharing Session**: Operations team shares screen, vendor observes (read-only)
5. **Vendor Guidance**: Vendor guides operations team through troubleshooting steps
6. **Session Recording**: Session recorded for audit
7. **Post-Session Review**: Security team reviews session within 24 hours

**Vendor Access Alternatives** (preferred over production access):
- Vendor analyzes logs/data exported by [Organization] (anonymized if personal data)
- Vendor tests in vendor's own environment (not [Organization] production)
- Vendor provides guidance remotely (no system access)

**Audit Verification Criteria**:
- ✅ Vendor production access approved (CISO)
- ✅ Vendor sessions supervised (screen sharing only)
- ✅ Vendor sessions recorded
- ✅ Vendor access reviewed post-session

---

## 2.5.8 Production Support Training and Awareness

### 2.5.8.1 Operations Team Training

[Organization] **SHALL** train operations team on production support procedures:

**Operations Training Topics**:
- Incident response procedures (tiers, escalation)
- Monitoring tools usage (dashboards, logs, metrics)
- Runbook execution (how to follow documented procedures)
- When to escalate (criteria for requesting developer assistance)
- Break-glass approval process (when and how to approve developer access)
- Security awareness (protecting production data, detecting suspicious activity)

**Training Frequency**:
- New hire onboarding (within first 30 days)
- Annual refresher training
- After major incidents (lessons learned training)
- When new tools/systems deployed

**Audit Verification Criteria**:
- ✅ Operations team training completion rate 100%
- ✅ Training materials current and accessible
- ✅ Training effectiveness measured (incident resolution time trending down)

### 2.5.8.2 Developer Awareness Training

[Organization] **SHALL** train developers on production support boundaries:

**Developer Training Topics**:
- Environment separation policy (why developers don't have production access)
- Remote troubleshooting techniques (how to support without access)
- Break-glass process (when and how to request emergency access)
- Monitoring and error tracking tools (how to diagnose issues remotely)
- Production data handling (prohibition of production data in dev/test)
- Incident response procedures (developer role during incidents)

**Training Frequency**:
- New developer onboarding (first week)
- Annual refresher training
- When policy changes

**Audit Verification Criteria**:
- ✅ Developer training completion rate 100%
- ✅ Developers understand break-glass process
- ✅ Developers use remote troubleshooting effectively (evidence: low break-glass usage)

---

## 2.5.9 Continuous Improvement of Production Support

### 2.5.9.1 Post-Incident Reviews

[Organization] **SHALL** conduct post-incident reviews to improve production support:

**Post-Incident Review (PIR) Process**:
1. **Incident Closure**: Incident resolved and production stable
2. **Data Collection**: Incident timeline, actions taken, access used
3. **PIR Meeting**: Operations, developers, security, management (within 48 hours)
4. **Analysis**: Root cause analysis, contributing factors
5. **Lessons Learned**: What went well, what could improve
6. **Action Items**: Specific improvements (runbook updates, tooling enhancements, training)
7. **Documentation**: PIR documented and shared (knowledge base)
8. **Follow-Up**: Action items tracked to completion

**PIR Focus Areas**:
- Was environment separation maintained during incident? (or bypassed inappropriately)
- Was break-glass access necessary? (could it have been avoided with better tools/training)
- Were runbooks effective? (or need updating)
- Was communication effective? (stakeholders informed, status clear)
- How to prevent recurrence? (fix root cause, not just symptoms)

**Audit Verification Criteria**:
- ✅ PIRs conducted for all Severity 1/2 incidents (100%)
- ✅ PIRs completed within 48 hours of incident resolution
- ✅ PIR action items tracked and completed
- ✅ PIR findings incorporated into runbooks/training

### 2.5.9.2 Production Support Metrics and KPIs

[Organization] **SHALL** track production support metrics to measure effectiveness:

**Key Performance Indicators (KPIs)**:
- **Mean Time to Detect (MTTD)**: How quickly are issues detected? (target: <5 minutes)
- **Mean Time to Resolve (MTTR)**: How quickly are issues resolved? (target: <2 hours for Sev 1)
- **Break-Glass Usage Rate**: How often is developer production access needed? (target: trending down, <10/year)
- **Tier 1 Resolution Rate**: Percentage of incidents resolved by operations without escalation (target: >60%)
- **Remote Troubleshooting Effectiveness**: Incidents resolved remotely without production access (target: >80%)
- **Runbook Coverage**: Percentage of incident types with documented runbooks (target: >90%)
- **Alert Noise**: False positive alert rate (target: <10%)

**Metrics Review**:
- Monthly operational review (operations manager + security team)
- Quarterly business review (present metrics to management)
- Annual trend analysis (year-over-year improvement)

**Continuous Improvement Actions**:
- Runbook gaps → Create missing runbooks
- High break-glass usage → Improve monitoring/troubleshooting tools
- Slow MTTR → Additional training, better automation
- High false positive alerts → Tune alerting rules

**Audit Verification Criteria**:
- ✅ Production support metrics tracked and reported
- ✅ Metrics reviewed monthly
- ✅ Continuous improvement actions identified and tracked
- ✅ Break-glass usage trending down (improving maturity)

---

## 2.5.10 Measurable Compliance Criteria

For audit and compliance verification, [Organization] must demonstrate:

**Production Support Compliance Metrics**:
- **<10** break-glass activations per year (trending down)
- **>80%** of incidents resolved without developer production access (Tier 1/2 resolution)
- **100%** of break-glass sessions recorded and reviewed
- **100%** of vendor production access supervised and recorded
- **>90%** runbook coverage for incident types
- **<2 hours** MTTR for Severity 1 incidents
- **100%** of production data extractions approved (DPO + CISO)
- **100%** PIRs completed for Sev 1/2 incidents

**Verification Methods**:
- Monthly break-glass usage audit
- Quarterly incident response effectiveness review
- Semi-annual runbook coverage assessment
- Annual vendor access audit
- Continuous production support metrics tracking

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Incident Response Lead | [Name] | ________________ | [Date] |
| Service Delivery Manager | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S2.5*
