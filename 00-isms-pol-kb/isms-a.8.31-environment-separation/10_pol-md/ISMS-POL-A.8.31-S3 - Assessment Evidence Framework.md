# ISMS-POL-A.8.31-S3
## Environment Separation - Assessment & Evidence Framework

**Document ID**: ISMS-POL-A.8.31-S3  
**Title**: Assessment & Evidence Framework  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial assessment framework |

**Review Cycle**: Annual (aligned with audit schedule)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Audit Liaison: Internal Audit Manager
- Compliance Review: Legal/Compliance Officer

**Distribution**: Security team, internal audit, external auditors, system owners  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary)
- ISMS-POL-A.8.31-S2.1-S2.5 (Requirements Sections)
- ISMS-IMP-A.8.31 (Implementation Guides and Assessment Tools)
- ISO/IEC 27001:2022 - Control A.8.31

---

## 3.1 Purpose and Scope

This section establishes the framework for assessing compliance with environment separation requirements and collecting evidence for audit purposes.

**Assessment Objectives**:
- Verify that environment separation controls are implemented effectively
- Identify gaps and weaknesses in environment separation
- Provide evidence for ISO 27001:2022 A.8.31 compliance
- Enable continuous improvement of environment separation practices

**In Scope**: All aspects of environment separation (architecture, access control, data handling, promotion, production support)  
**Primary Stakeholder**: Information Security Team, Internal Audit, External Auditors

---

## 3.2 Assessment Methodology

### 3.2.1 Assessment Types

[Organization] **SHALL** conduct multiple types of environment separation assessments:

**1. Self-Assessment (Quarterly)**:
- **Who**: System owners, IT operations
- **Scope**: Assess own systems against environment separation requirements
- **Method**: Checklist-based assessment (using assessment workbooks from IMP-A.8.31)
- **Output**: Self-assessment report, gap analysis
- **Timeline**: Completed within first month of each quarter

**2. Independent Security Assessment (Semi-Annual)**:
- **Who**: Information Security team (independent from operations)
- **Scope**: In-depth assessment of environment separation controls
- **Method**: Technical testing (network scans, access reviews, configuration audits)
- **Output**: Security assessment report, findings and recommendations
- **Timeline**: Every 6 months (aligned with audit schedule)

**3. Internal Audit (Annual)**:
- **Who**: Internal Audit team
- **Scope**: Compliance audit against ISMS-POL-A.8.31 requirements
- **Method**: Evidence review, interviews, technical testing
- **Output**: Internal audit report, compliance rating
- **Timeline**: Annually (aligned with ISO 27001 audit)

**4. External Audit (Annual)**:
- **Who**: External auditor (ISO 27001 certification body)
- **Scope**: ISO 27001:2022 A.8.31 compliance verification
- **Method**: Evidence sampling, interviews, technical verification
- **Output**: ISO 27001 audit findings (compliance/non-compliance)
- **Timeline**: Annual surveillance audit or recertification audit

**5. Continuous Monitoring (Ongoing)**:
- **Who**: Automated monitoring tools, Security Operations Center (SOC)
- **Scope**: Real-time monitoring of environment separation violations
- **Method**: Automated scans, log analysis, anomaly detection
- **Output**: Continuous compliance dashboards, alerts for violations
- **Timeline**: 24/7 continuous monitoring

**Audit Verification Criteria**:
- ✅ Self-assessments completed quarterly (100% compliance)
- ✅ Independent security assessments conducted semi-annually
- ✅ Internal audits conducted annually
- ✅ External audits passed (no major non-conformances)
- ✅ Continuous monitoring active and effective

### 3.2.2 Assessment Scope and Coverage

[Organization] **SHALL** ensure comprehensive assessment coverage:

**Systems In Scope**:
- All production systems (100% coverage mandatory)
- All staging/pre-production systems (100% coverage mandatory)
- Sample of development/testing systems (minimum 25% coverage)
- High-risk systems (100% coverage - e.g., systems processing personal data, payment data)

**Assessment Areas** (per Section 2 requirements):
- Environment architecture (S2.1): Network separation, infrastructure separation, credential isolation
- Environment access control (S2.2): Access provisioning, production access restrictions, break-glass usage
- Data handling (S2.3): Production data in dev/test detection, anonymization effectiveness
- Environment promotion (S2.4): Promotion path adherence, deployment approval, rollback procedures
- Production support (S2.5): Break-glass usage, remote troubleshooting, incident response

**Assessment Depth**:
- **High-risk systems**: Detailed technical assessment (penetration testing, full configuration review)
- **Medium-risk systems**: Standard assessment (configuration sampling, access review)
- **Low-risk systems**: Light-touch assessment (self-assessment verification)

**Audit Verification Criteria**:
- ✅ 100% of production systems assessed
- ✅ Assessment covers all requirement areas (S2.1-S2.5)
- ✅ High-risk systems receive detailed assessment
- ✅ Assessment scope documented and approved

---

## 3.3 Assessment Execution

### 3.3.1 Environment Architecture Assessment

[Organization] **SHALL** assess environment architecture per S2.1 requirements:

**Assessment Activities**:

**1. Network Separation Verification**:
- Review network diagrams (verify environment segmentation documented)
- Test network connectivity (attempt dev → prod network access - should fail)
- Review firewall rules (verify default deny between environments)
- Penetration test (attempt to bypass network isolation)

**2. Infrastructure Separation Verification**:
- Review infrastructure inventory (verify separate resources per environment)
- Cloud account/subscription review (verify separate accounts for prod vs. non-prod)
- Kubernetes namespace review (if applicable - verify NetworkPolicies enforce isolation)
- Compute resource audit (verify no shared servers between prod and dev/test)

**3. Credential and Secrets Verification**:
- Credential inventory review (verify separate credentials per environment)
- Secret management audit (verify production secrets in PAM vault)
- Code repository scan (verify no production credentials in source control)
- Configuration review (verify no production configs in dev/test)

**Evidence Collection**:
- Network diagrams (current and approved)
- Firewall rule exports (sanitized)
- Cloud account/subscription list
- Credential inventory (redacted)
- Code scan results (credential detection)

**Compliance Scoring**:
- **Fully Compliant (Green)**: All requirements met, no gaps
- **Mostly Compliant (Yellow)**: Minor gaps (e.g., documentation outdated but controls in place)
- **Partially Compliant (Orange)**: Moderate gaps (e.g., some environments not properly separated)
- **Non-Compliant (Red)**: Major gaps (e.g., no network separation, shared credentials)

**Assessment Workbook**: ISMS-IMP-A.8.31-S1 (Environment Architecture Assessment)

### 3.3.2 Environment Access Control Assessment

[Organization] **SHALL** assess access controls per S2.2 requirements:

**Assessment Activities**:

**1. Production Access Audit** (CRITICAL):
- User access review (who has production access - verify operations only)
- **Developer production access count** (should be ZERO except break-glass)
- Break-glass usage review (review all break-glass activations in period)
- Service account review (verify prod service accounts separate from dev/test)

**2. Access Provisioning Audit**:
- Access request review (verify all access requests approved)
- Deprovisioning audit (verify terminated users have zero access)
- Access review completion (verify quarterly reviews conducted)
- Orphaned account detection (accounts with no owner)

**3. Authentication and Authorization Audit**:
- MFA enforcement (verify production requires MFA)
- PAM usage (verify all production admin access via PAM)
- RBAC implementation (verify role-based access enforced)
- Local account audit (should be minimal - emergency accounts only)

**Evidence Collection**:
- User-environment access matrix
- Developer production access list (should be empty or break-glass only)
- Break-glass access logs (all activations in period)
- Access request tickets (sample)
- Deprovisioning logs (terminated users)
- MFA enforcement status
- PAM usage logs

**Compliance Metrics** (CRITICAL):
- **0 developers** with standing production access
- **100%** of production access via PAM
- **100%** of production access with MFA
- **>95%** deprovisioning completion rate (within 24 hours)
- **100%** access reviews completed on schedule

**Assessment Workbook**: ISMS-IMP-A.8.31-S2 (Environment Access Control Assessment)

### 3.3.3 Data Handling Assessment

[Organization] **SHALL** assess data handling per S2.3 requirements:

**Assessment Activities**:

**1. Production Data Detection in Dev/Test** (CRITICAL):
- Automated scan (database content analysis, pattern matching)
- Manual review (sample database records in dev/test)
- Network traffic analysis (detect prod → dev data transfers)
- Code repository scan (detect production data exports)

**2. Anonymization Effectiveness Review**:
- Review anonymization approvals (DPO signed off?)
- Test re-identification (can individuals be identified from anonymized data?)
- Anonymization technique validation (techniques appropriate for data sensitivity)

**3. Test Data Management Audit**:
- Test data retention (verify test data deleted per policy)
- Test data volume monitoring (not growing indefinitely?)
- Synthetic data usage (verify synthetic data used where possible)

**Evidence Collection**:
- Production data detection scan results (should find ZERO production data in dev/test)
- Anonymization approvals (DPO signatures)
- Re-identification test results
- Test data retention reports
- Test data deletion logs

**Compliance Metrics** (CRITICAL):
- **0 production personal data** found in dev/test (automated scan)
- **100%** of production data usage exceptions approved (CISO + DPO)
- **100%** of anonymization approaches approved by DPO
- **100%** test data deleted per retention schedule

**Assessment Workbook**: ISMS-IMP-A.8.31-S1 (Data Separation section)

### 3.3.4 Environment Promotion Assessment

[Organization] **SHALL** assess promotion process per S2.4 requirements:

**Assessment Activities**:

**1. Promotion Path Audit**:
- Review deployment logs (verify all promotions follow dev → test → staging → prod)
- Direct production deployment detection (should be ZERO except hot-fixes)
- Hot-fix approval review (all hot-fixes approved by CISO?)

**2. Approval Gate Audit**:
- Review CAB approvals (all production deployments approved?)
- QA sign-off review (all staging promotions have QA approval?)
- Peer review audit (sample code reviews)

**3. Rollback Procedure Audit**:
- Rollback plan review (all production deployments have rollback plan?)
- Rollback execution audit (how many rollbacks, were they successful?)
- Rollback time validation (rollbacks completed within target time?)

**Evidence Collection**:
- Deployment logs (who, what, when, where)
- CAB approval records
- QA sign-off records
- Rollback plans (sample)
- Rollback execution logs

**Compliance Metrics**:
- **0** direct deployments to production (bypassing staging) except approved hot-fixes
- **100%** of production deployments have CAB approval
- **<5%** rollback rate (indicates quality promotion process)
- **<10** hot-fixes per year (trending down)

**Assessment Workbook**: ISMS-IMP-A.8.31 (derived from deployment logs)

### 3.3.5 Production Support Assessment

[Organization] **SHALL** assess production support per S2.5 requirements:

**Assessment Activities**:

**1. Break-Glass Usage Audit**:
- Review all break-glass activations (justified? approved? time-limited?)
- Session recording review (what did developer do in production?)
- Post-incident review completion (all PIRs completed?)

**2. Remote Troubleshooting Effectiveness**:
- Incident resolution analysis (how many resolved remotely vs. requiring production access?)
- Tier 1/2 resolution rate (percentage resolved by ops without dev access)

**3. Runbook Coverage Audit**:
- Runbook inventory (all incident types covered?)
- Runbook currency (updated within 30 days of incidents?)
- Runbook testing (tested annually in DR drills?)

**Evidence Collection**:
- Break-glass activation logs (complete list for period)
- Break-glass session recordings (sample review)
- Post-incident reviews (PIRs)
- Incident resolution statistics
- Runbook inventory

**Compliance Metrics**:
- **<10** break-glass activations per year (trending down)
- **>80%** incidents resolved without developer production access
- **100%** break-glass sessions recorded and reviewed
- **>90%** runbook coverage

**Assessment Workbook**: ISMS-IMP-A.8.31 (incident management integration)

---

## 3.4 Evidence Collection and Management

### 3.4.1 Evidence Types and Sources

[Organization] **SHALL** collect and maintain evidence for audit:

**Technical Evidence**:
- Network diagrams (environment architecture)
- Firewall rule exports (network separation)
- Cloud account/subscription configurations (infrastructure separation)
- Access control matrices (who has access to which environment)
- Deployment logs (promotion tracking)
- Monitoring dashboards (continuous compliance)

**Procedural Evidence**:
- Policy documents (ISMS-POL-A.8.31)
- Implementation guides (ISMS-IMP-A.8.31)
- Runbooks and SOPs
- Training records (completion rates)
- Access request approvals
- Change management approvals (CAB)

**Assessment Evidence**:
- Self-assessment reports
- Independent security assessment reports
- Internal audit reports
- External audit reports
- Penetration test reports
- Compliance dashboards

**Incident Evidence**:
- Incident reports (security incidents, operational incidents)
- Break-glass access logs
- Post-incident reviews (PIRs)
- Corrective action tracking

**Audit Verification Criteria**:
- ✅ Evidence collection automated where possible
- ✅ Evidence retained per retention requirements (3 years for production)
- ✅ Evidence accessible to auditors (secured repository)
- ✅ Evidence complete and current (no gaps)

### 3.4.2 Evidence Retention Requirements

[Organization] **SHALL** retain evidence per regulatory and contractual requirements:

**Retention Periods**:
- **Production environment evidence**: 3 years minimum (regulatory requirement)
- **Staging environment evidence**: 2 years
- **Development/testing evidence**: 1 year
- **Assessment reports**: 5 years (ISO 27001 certification lifecycle)
- **Audit findings and responses**: 7 years (legal requirement)
- **Incident evidence**: 5 years

**Evidence Storage**:
- Centralized evidence repository (SharePoint, document management system)
- Access controls (security team, auditors only)
- Version control (track evidence updates)
- Backup and recovery (evidence protected like production data)

**Evidence Disposal**:
- Secure deletion after retention period
- Disposal logged and auditable
- Exception process (legal hold, ongoing litigation)

**Audit Verification Criteria**:
- ✅ Evidence retention policy documented
- ✅ Evidence retained per requirements (no premature deletion)
- ✅ Evidence securely disposed after retention period
- ✅ Evidence accessible for audit on request

---

## 3.5 Compliance Reporting

### 3.5.1 Compliance Dashboard and Metrics

[Organization] **SHALL** maintain real-time compliance dashboards:

**Dashboard Components**:
- **Overall Compliance Score**: Percentage compliance with A.8.31 requirements
- **Environments with Proper Separation**: Percentage of systems meeting separation requirements
- **Developer Production Access Count**: Should be ZERO (critical metric)
- **Production Data in Dev/Test Incidents**: Should be ZERO (critical metric)
- **Break-Glass Usage**: Count and trend (should trend down)
- **Promotion Process Adherence**: Percentage of deployments following proper path
- **Critical Findings**: Count of critical gaps requiring immediate action

**Dashboard Audience**:
- **CISO**: Overall compliance and risk exposure
- **IT Operations**: Operational metrics (break-glass usage, incident resolution)
- **System Owners**: Compliance status of their systems
- **Auditors**: Evidence of continuous monitoring

**Dashboard Tool**: ISMS-IMP-A.8.31 (Compliance Dashboard - Excel or BI tool)

### 3.5.2 Compliance Reporting Frequency

[Organization] **SHALL** report compliance status regularly:

**Monthly**:
- Break-glass usage report (to CISO and IT Ops)
- Production access audit (developer prod access count - should be zero)
- Production data detection scan results (to CISO and DPO)

**Quarterly**:
- Self-assessment results (system owners → security team)
- Compliance dashboard summary (security team → management)
- Gap remediation tracking (open findings and status)

**Semi-Annual**:
- Independent security assessment report (security team → CISO)
- Comprehensive compliance report (all metrics and trends)

**Annual**:
- Internal audit report (internal audit → audit committee)
- External audit report (external auditor → certification body)
- Year-in-review (trends, improvements, challenges)

**Audit Verification Criteria**:
- ✅ Compliance reports generated per schedule
- ✅ Reports distributed to appropriate stakeholders
- ✅ Report findings tracked to closure
- ✅ Trends analyzed (compliance improving over time?)

---

## 3.6 Gap Analysis and Remediation

### 3.6.1 Gap Identification and Prioritization

[Organization] **SHALL** identify and prioritize environment separation gaps:

**Gap Severity Levels**:

**Critical (Red)**:
- Developers have standing production access (violates zero-access requirement)
- Production personal data found in dev/test (GDPR/FADP violation)
- No network separation between dev and production (direct access possible)
- Shared credentials between production and non-production
- Direct production deployments (bypassing staging)

**High (Orange)**:
- Production access not via PAM (administrative access without session recording)
- Inadequate access reviews (not conducted quarterly)
- Break-glass usage excessive (>10 per year)
- Incomplete environment architecture documentation
- Configuration drift between staging and production (>5%)

**Medium (Yellow)**:
- Runbook gaps (incident types without documented procedures)
- Training not completed (operations or developers missing training)
- Anonymization not optimal (DPO approved but technique could be stronger)
- Deployment approvals inconsistent (some bypassed)

**Low (Green)**:
- Documentation outdated (controls in place but docs need updating)
- Minor process deviations (isolated incidents, not systematic)
- Optimization opportunities (process works but could be more efficient)

**Gap Prioritization**:
- Critical gaps: Remediate immediately (within 7 days)
- High gaps: Remediate urgently (within 30 days)
- Medium gaps: Remediate promptly (within 90 days)
- Low gaps: Remediate as resources permit (within 180 days)

**Audit Verification Criteria**:
- ✅ Gaps identified and documented
- ✅ Severity assigned per criteria
- ✅ Remediation timeline defined
- ✅ Critical gaps remediated within 7 days (100%)

### 3.6.2 Remediation Tracking and Verification

[Organization] **SHALL** track gaps to closure:

**Remediation Process**:
1. **Gap Identified**: During assessment or continuous monitoring
2. **Gap Logged**: Entered into tracking system (Jira, ServiceNow, etc.)
3. **Owner Assigned**: System owner or functional lead responsible
4. **Remediation Plan**: Owner documents how gap will be closed
5. **Timeline Set**: Based on severity (critical = 7 days, high = 30 days, etc.)
6. **Progress Tracked**: Regular status updates (weekly for critical/high)
7. **Verification**: Security team verifies gap closed
8. **Closure**: Gap marked closed in tracking system

**Remediation Reporting**:
- Weekly: Critical and high gap status (to CISO)
- Monthly: All gap status (to security team and system owners)
- Quarterly: Gap trends and closure rates (to management)

**Escalation**:
- Gaps past due → Escalate to system owner's manager
- Gaps significantly past due (2x timeline) → Escalate to CISO
- Unresolvable gaps → Risk acceptance or exception process

**Audit Verification Criteria**:
- ✅ All gaps tracked to closure (0% lost gaps)
- ✅ Critical gaps closed within 7 days (>95% on time)
- ✅ High gaps closed within 30 days (>90% on time)
- ✅ Gap closure verified by security team (100%)

---

## 3.7 Audit Preparation and Support

### 3.7.1 Internal Audit Support

[Organization] **SHALL** support internal audit activities:

**Audit Preparation**:
- Evidence package prepared (all required evidence collected and organized)
- System owners notified (prepare for interviews)
- Assessment results current (self-assessment and independent assessment completed)
- Compliance dashboard updated (real-time metrics available)

**Audit Execution Support**:
- Evidence provided to auditors promptly (within 24 hours of request)
- Interviews scheduled and conducted (system owners, operations, developers)
- Technical demonstrations (show environment separation controls in action)
- Walkthroughs (explain processes like break-glass, promotion workflow)

**Audit Findings Response**:
- Findings reviewed and acknowledged
- Corrective action plans developed (timeline, owner, verification)
- Findings tracked to closure
- Follow-up audit conducted (verify findings closed)

**Audit Verification Criteria**:
- ✅ Evidence provided to auditors on time (100%)
- ✅ Audit findings responded to within 10 business days
- ✅ Corrective actions completed per agreed timeline (>90%)
- ✅ Follow-up audits passed (findings closed)

### 3.7.2 External Audit Support

[Organization] **SHALL** support external ISO 27001 audit activities:

**Pre-Audit Preparation**:
- ISO 27001 A.8.31 control effectiveness self-assessed
- Evidence package prepared per ISO 27001 requirements
- Mock audit conducted (internal dry-run)
- Gaps identified in mock audit closed

**Audit Day Support**:
- Auditor access provided (secure workspace, system access as needed)
- Evidence presented professionally (organized, indexed, accessible)
- Questions answered accurately and completely
- Technical demonstrations prepared (if requested)

**Post-Audit Response**:
- Non-conformances addressed urgently (critical = immediate, major = 30 days, minor = 90 days)
- Corrective action plans submitted to certification body
- Corrective actions verified by follow-up audit
- Certification maintained (no non-conformances preventing certification)

**Audit Verification Criteria**:
- ✅ External audit passed (ISO 27001 certification maintained)
- ✅ Zero major non-conformances (for A.8.31)
- ✅ Minor non-conformances closed within 90 days
- ✅ Certification body satisfied with corrective actions

---

## 3.8 Continuous Improvement

### 3.8.1 Assessment Findings Analysis

[Organization] **SHALL** analyze assessment findings for improvement opportunities:

**Trend Analysis**:
- **Compliance trending**: Is overall compliance improving or declining?
- **Common gaps**: Which requirements are frequently non-compliant?
- **System patterns**: Are specific systems or technologies problematic?
- **Process effectiveness**: Are controls effective or just documented?

**Root Cause Analysis**:
- Why are gaps occurring? (lack of awareness, lack of tools, process complexity, resource constraints)
- Are gaps systematic or isolated? (widespread issue vs. one-off incident)
- What can prevent recurrence? (training, automation, process simplification)

**Improvement Actions**:
- Policy updates (clarify confusing requirements)
- Process improvements (simplify complex workflows)
- Tool enhancements (automation to enforce controls)
- Training improvements (address knowledge gaps)
- Resource allocation (provide budget/staff for compliance)

**Audit Verification Criteria**:
- ✅ Findings analyzed quarterly (trends identified)
- ✅ Root cause analysis conducted for recurring gaps
- ✅ Improvement actions documented and tracked
- ✅ Compliance trends improving year-over-year

### 3.8.2 Assessment Framework Evolution

[Organization] **SHALL** continuously improve the assessment framework itself:

**Framework Review Triggers**:
- Annual policy review (update assessment framework with policy changes)
- New regulatory requirements (add new assessment areas)
- Technology changes (update for cloud, containers, serverless, etc.)
- Audit feedback (incorporate auditor suggestions)
- Assessment findings (if framework missing gaps, enhance framework)

**Framework Enhancements**:
- Assessment workbooks updated (new checks added)
- Automation improvements (more automated evidence collection)
- Compliance dashboard enhancements (better metrics and visualizations)
- Assessment efficiency (reduce manual effort, maintain rigor)

**Audit Verification Criteria**:
- ✅ Assessment framework reviewed annually
- ✅ Framework updated to reflect policy changes
- ✅ Automation percentage increasing (manual effort decreasing)
- ✅ Assessment coverage comprehensive (no gaps in assessment scope)

---

## 3.9 Measurable Assessment Success Criteria

For effective environment separation assessment, [Organization] must demonstrate:

**Assessment Coverage Metrics**:
- **100%** of production systems assessed (no exceptions)
- **100%** of assessment areas covered (architecture, access, data, promotion, support)
- **>95%** assessment completion rate (on schedule)

**Assessment Quality Metrics**:
- **<5%** false positives in automated scans (accurate detection)
- **>90%** auditor satisfaction (auditors rate evidence quality as good/excellent)
- **Zero** surprise findings in external audit (self-assessment identified all gaps)

**Remediation Metrics**:
- **>95%** critical gaps closed within 7 days
- **>90%** high gaps closed within 30 days
- **100%** gaps tracked to closure (no lost findings)

**Compliance Metrics** (Overall A.8.31):
- **>90%** overall compliance score (trending to 95%+)
- **Zero** major non-conformances in ISO 27001 audit
- **Zero** production data found in dev/test (ongoing)
- **Zero** developers with standing production access (ongoing)

**Verification Methods**:
- Quarterly assessment metrics review
- Semi-annual compliance dashboard analysis
- Annual assessment effectiveness evaluation
- External audit results (ultimate validation)

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |
| Internal Audit Manager | [Name] | ________________ | [Date] |
| External Auditor Liaison | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S3*
