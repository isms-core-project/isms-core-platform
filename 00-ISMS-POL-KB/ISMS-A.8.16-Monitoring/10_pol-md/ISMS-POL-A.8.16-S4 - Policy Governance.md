# ISMS-POL-A.8.16-S4
## Monitoring Activities - Policy Governance

**Document ID**: ISMS-POL-A.8.16-S4
**Title**: Monitoring Activities - Policy Governance  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / SOC Lead | Initial governance framework |

**Review Cycle**: Annual (or upon changes to ISMS governance structure)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Governance Review: Information Security Steering Committee
- Operational Review: Security Operations Center (SOC) Lead
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (for governance authority)

**Distribution**: ISMS governance stakeholders, SOC, security team, audit team, management  
**Related Documents**: ISMS Manual (Clause 5.2, 5.3), Document Control Procedure

---

## 4.1 Purpose and Scope

This section establishes the **governance framework** for monitoring activities policies, ensuring they remain current, effective, and aligned with organizational objectives throughout their lifecycle.

**Governance Objectives**:
- Maintain policy relevance and effectiveness over time
- Ensure proper approval and oversight
- Communicate policies clearly to stakeholders
- Monitor compliance and effectiveness
- Continuously improve based on metrics, incidents, and feedback
- Integrate with broader ISMS governance

**In Scope**: Policy lifecycle management, change control, version management, communication, compliance monitoring  
**Primary Stakeholders**: CISO, SOC, Security Team, All Personnel  
**Implementation Evidence**: ISMS-IMP-A.8.16.5 (Compliance Dashboard - governance metrics)

---

## 4.2 Policy Lifecycle

### 4.2.1 Lifecycle Stages

Monitoring activities policies follow a structured lifecycle:

1. **CREATION**: Policy developed in response to organizational need, regulatory requirement, or risk assessment
2. **REVIEW**: Stakeholder review and feedback integration
3. **APPROVAL**: Formal approval by designated authorities
4. **PUBLICATION**: Communication and distribution to organization
5. **IMPLEMENTATION**: Technical implementation (monitoring infrastructure, baselines, detection rules)
6. **MONITORING**: Ongoing compliance and effectiveness monitoring
7. **REVIEW/UPDATE**: Periodic or triggered review and updates
8. **RETIREMENT**: Archival when policy is superseded or no longer applicable

### 4.2.2 Lifecycle Ownership

Policy Owner (CISO) is accountable for policy lifecycle management, supported by SOC Lead and Security Team for execution.

---

## 4.3 Policy Creation and Development

### 4.3.1 Triggers for New Policy Development

New policies or policy sections **MAY** be created when:

- ISO 27001 or regulatory requirements mandate new controls
- Risk assessment identifies monitoring gaps requiring policy coverage
- Technology changes create new monitoring considerations (new SIEM, cloud monitoring, EDR)
- Organizational changes require policy adaptation (mergers, cloud migration, new business lines)
- Security incidents reveal monitoring gaps or policy failures
- Threat landscape evolution requires updated detection strategies
- Industry best practices evolve (MITRE ATT&CK updates, new detection techniques)

### 4.3.2 Development Process

**Step 1 - Needs Assessment**:
- Document business/security driver for new policy
- Define scope and objectives
- Identify affected stakeholders (SOC, Security Engineering, System Owners, IT Ops)
- Assess resources required (tools, staffing, budget)

**Step 2 - Drafting**:
- Security Team/SOC drafts policy using organizational templates
- Research best practices (NIST, CIS, SANS, MITRE)
- Ensure consistency with existing ISMS policies
- Apply modular structure (consistent with this framework)
- Focus on requirements (WHAT), not implementation details (HOW)

**Step 3 - Stakeholder Consultation**:
- Engage relevant parties:
  - **SOC**: Operational feasibility, alert management procedures
  - **Security Engineering**: Technical feasibility, infrastructure requirements
  - **IT Operations**: System integration, resource impact
  - **System Owners**: Monitoring coverage expectations
  - **Legal/Compliance**: Privacy implications, retention requirements
- Solicit feedback on draft
- Conduct impact assessment (operational, technical, privacy, cost)
- Revise based on feedback

**Step 4 - Legal/Compliance Review**:
- Legal validates compliance with data protection laws (GDPR, FADP)
- Compliance verifies alignment with standards (ISO 27001, PCI-DSS, etc.)
- Privacy officer reviews monitoring scope and data retention
- Revise as needed

**Step 5 - Finalization**:
- Incorporate all feedback
- Prepare final draft for approval
- Document decision rationale and risk considerations
- Prepare implementation roadmap (if new technical requirements)

---

## 4.4 Policy Approval

### 4.4.1 Approval Authority

Policy approval authority varies by scope and impact:

| Policy Type | Approval Authority | Additional Reviewers |
|-------------|-------------------|---------------------|
| New Policy Framework (S1-S5) | CISO + IT Management + Legal | Executive Management (informed) |
| Policy Section Updates (major) | CISO | SOC Lead, IT Management, Legal (if legal impact) |
| Policy Section Updates (minor) | SOC Lead or Security Team Lead | CISO (informed) |
| Baseline Documentation | SOC Lead | System Owners (for their systems) |
| Detection Rules | SOC Tier 2/3 | SOC Lead (approval for production deployment) |

**Major Update**: Changes to scope, requirements, responsibilities, governance, retention periods  
**Minor Update**: Clarifications, formatting, corrections, non-substantive changes, baseline refreshes

### 4.4.2 Approval Process

**Submission**:
- Policy author submits final draft to approvers
- Include summary of changes (if update)
- Include stakeholder feedback summary
- Include risk assessment
- Include implementation impact (cost, timeline, resources)

**Review Period**:
- Approvers have 10 business days to review and decide
- Extensions granted for complex policies
- Reviewers may request clarifications or modifications

**Decision**:
- Approve (policy proceeds to publication)
- Approve with conditions (minor revisions required)
- Deny (policy returned for substantial revision)
- Defer (more information needed)

**Documentation**:
- Approval recorded in document control table
- Decision rationale documented
- Conditions or modifications documented

### 4.4.3 Emergency Policy Changes

In case of critical security incidents, urgent threat landscape changes, or regulatory deadlines:

- CISO **MAY** approve emergency policy updates verbally
- Implementation proceeds immediately
- Formal documentation and approval completed within 5 business days
- Emergency changes reviewed at next scheduled policy review

**Example Emergency Scenarios**:
- Active threat campaign requiring immediate detection rule deployment
- Data breach requiring immediate retention policy extension (legal hold)
- Critical vulnerability requiring immediate monitoring coverage expansion

---

## 4.5 Policy Publication and Communication

### 4.5.1 Publication Channels

Approved policies **SHALL** be published via:

**Primary Channel**: Organization's policy portal or document management system

**Secondary Channels**:
- SOC internal wiki/knowledge base
- Intranet security page
- Email notification to affected stakeholders
- Security awareness training updates
- New hire onboarding materials (security-focused roles)

### 4.5.2 Accessibility

Policies **SHALL** be:

- Accessible to all personnel (no unnecessary access restrictions)
- Available in searchable format (PDF + markdown)
- Organized logically (by control number, topic, role)
- Linked to related policies (cross-references to A.8.15, A.5.24-28, etc.)
- Available in primary organizational language (English)
- Translated if legally required (e.g., German for Swiss employees if mandated)

### 4.5.3 Communication Strategy

**New Policies**:
- Announcement email from CISO explaining purpose and impact
- SOC briefing (detailed walkthrough for operational team)
- System Owner notification (responsibilities and expectations)
- Summary presentation for IT management
- FAQ document addressing common questions
- Training materials updated
- Implementation timeline communicated

**Policy Updates**:
- Change summary distributed to affected stakeholders
- Highlight what changed, why, and impact
- SOC shift handover notes (ensure all shifts aware)
- Communicate implementation date (if technical changes required)
- Provide transition period if significant changes

**Detection Rule Updates**:
- SOC-specific communication channel (Slack, Teams, email list)
- Document in detection rule repository
- Update investigation playbooks if affected
- Brief all shifts on new detections

**Periodic Reminders**:
- Quarterly SOC policy review session
- Annual monitoring effectiveness review with system owners
- Security newsletter highlights monitoring successes

### 4.5.4 Acknowledgment

For critical monitoring policies:

- SOC analysts **SHALL** acknowledge they have read and understand operational procedures (S5.C)
- System Owners **SHALL** acknowledge monitoring responsibilities
- Acknowledgment tracked in training system or HR system
- New SOC hires acknowledge during onboarding
- Re-acknowledgment required after major procedural updates

Technical policy sections (S2.1-S2.4) do not require individual user acknowledgment but **SHOULD** be communicated to affected technical teams.

---

## 4.6 Version Control and Document Management

### 4.6.1 Versioning Scheme

Policies use **semantic versioning**:

**Major.Minor** (e.g., 1.0, 1.1, 2.0)

**Major Version Change (X.0)**:
- Significant scope changes (new monitoring capabilities, coverage requirements)
- Substantial requirement changes (new SLAs, retention periods)
- Organizational structure changes (new SOC tiers, role changes)
- Requires full re-approval

**Minor Version Change (X.Y)**:
- Clarifications, corrections
- Minor requirement adjustments (SLA fine-tuning)
- Baseline updates
- Non-substantive updates
- Requires limited approval (SOC Lead or CISO)

### 4.6.2 Document Metadata

Each policy document **SHALL** include:

- Document ID (e.g., ISMS-POL-A.8.16-S2.1)
- Title
- Version number
- Publication date (DD.MM.YYYY)
- Classification (typically "Internal")
- Owner (typically CISO)
- Status (Draft, Approved, Retired)
- Review cycle
- Next review date
- Version history table

### 4.6.3 Change Log

For each version update, document:

- Version number
- Date of change
- Author
- Summary of changes (what was modified)
- Rationale (why change was made)
- Approver

### 4.6.4 Repository Management

Policies **SHALL** be stored in:

- **Production Repository**: Approved, published versions
- **Draft Repository**: Work-in-progress versions
- **Archive Repository**: Retired/superseded versions

Access controls:
- **Read**: All personnel (for approved policies)
- **Edit**: Policy authors only (draft repository)
- **Approve**: Designated approvers only
- **Archive**: Document control administrator only

---

## 4.7 Policy Review and Update

### 4.7.1 Scheduled Reviews

**Annual Comprehensive Review**:
- Full review of all policy sections (S1 through S5)
- Assess continued relevance and effectiveness
- Update for regulatory changes, threat landscape evolution
- Review metrics and adjust targets if needed
- Engage all stakeholders
- Document review outcomes

**Quarterly Operational Reviews**:
- Review operational sections (S2.2 baselines, S2.3 alert management, S5.C procedures)
- Analyze metrics (MTTD, MTTR, false positive rates, detection coverage)
- Identify tuning opportunities
- Quick adjustments without full policy cycle

**Baseline Reviews** (per ISMS-POL-A.8.16-S2.2):
- Critical systems: Quarterly
- Standard systems: Semi-annually

### 4.7.2 Triggered Reviews

Policy review **MAY** be triggered by:

**Incidents**:
- Major security incidents revealing monitoring gaps
- Missed detections (false negatives requiring new rules)
- Alert fatigue incidents (SOC overwhelmed)

**Organizational Changes**:
- Mergers, acquisitions, divestitures
- Cloud migration projects
- New business lines or services
- Significant technology changes (new SIEM, cloud platforms)

**Regulatory Changes**:
- New data protection requirements
- Industry-specific regulation updates
- Audit findings requiring policy updates

**Performance Issues**:
- Consistently missed SLAs
- Unacceptably high false positive rates
- Detection rate below targets

**Technology Evolution**:
- New monitoring capabilities available
- Deprecated technologies requiring replacement
- Industry best practice updates (MITRE ATT&CK, CIS Controls)

### 4.7.3 Review Process

**Initiate Review**:
- SOC Lead or Security Team identifies need for review
- Document trigger and scope
- Assign review owner

**Gather Input**:
- Collect metrics and performance data
- Solicit stakeholder feedback (SOC analysts, system owners, IT ops)
- Review incident lessons learned
- Research industry best practices

**Analyze**:
- Identify gaps, issues, improvement opportunities
- Prioritize changes (critical, important, nice-to-have)
- Assess implementation impact

**Propose Updates**:
- Draft proposed changes
- Document rationale
- Estimate implementation effort

**Approve and Implement**:
- Follow approval process (section 4.4)
- Communicate changes (section 4.5)
- Implement technical changes
- Monitor effectiveness post-implementation

---

## 4.8 Implementation Coordination

### 4.8.1 Implementation Planning

When policy updates require technical implementation:

**Assessment**:
- Identify systems/processes affected
- Estimate effort and timeline
- Identify dependencies and prerequisites
- Assess risk of implementation

**Planning**:
- Create implementation project plan
- Assign responsibilities (Security Engineering, SOC, IT Ops)
- Define success criteria
- Plan testing and validation
- Define rollback procedures

**Execution**:
- Implement in dev/test environment first
- Validate functionality
- Deploy to production in controlled manner
- Monitor for issues
- Adjust as needed

**Validation**:
- Verify implementation matches policy requirements
- Test detection effectiveness
- Confirm alert generation works
- Validate baseline accuracy
- Conduct user acceptance testing (SOC)

### 4.8.2 Communication During Implementation

**Pre-Implementation**:
- Notify affected stakeholders of upcoming changes
- Communicate timeline and expected impact
- Provide training if procedures change
- Answer questions

**During Implementation**:
- Status updates to stakeholders
- Escalation path for issues
- SOC awareness (new alerts, changed thresholds)

**Post-Implementation**:
- Confirmation of completion
- Summary of what changed
- Training on new capabilities/procedures
- Feedback collection

---

## 4.9 Policy Integration with ISMS

### 4.9.1 ISMS Alignment

Monitoring activities policies are part of broader ISMS and **SHALL** integrate with:

**Related ISMS Policies**:
- **ISMS-POL-A.8.15** (Logging) - Monitoring analyzes logs generated by logging control
- **ISMS-POL-A.5.24-28** (Incident Management) - Monitoring feeds incident response
- **ISMS-POL-A.5.7** (Threat Intelligence) - Threat intel informs detection rules
- **ISMS-POL-A.8.8** (Vulnerability Management) - Monitoring detects exploitation
- **ISMS-POL-A.8.23** (Web Filtering) - Web filtering logs feed monitoring
- **Privacy Policy** - Monitoring respects privacy obligations
- **Data Retention Policy** - Monitoring data retention alignment

**Cross-References**:
- Policies reference each other where dependencies exist
- Avoid duplication (point to authoritative policy)
- Ensure consistency across policies (e.g., retention periods consistent with data retention policy)

### 4.9.2 ISO 27001 Compliance

Monitoring activities policies implement ISO 27001:2022 Control A.8.16:

- Annual ISMS review includes monitoring policy review
- Internal audits verify policy compliance
- External certification audits validate policy effectiveness
- Gap analysis conducted when ISO standard updated
- Continuous improvement aligned with ISMS improvement objectives
- Statement of Applicability (SoA) references monitoring controls

### 4.9.3 Risk Management Integration

Monitoring activities policies support organizational risk management:

- Risk register includes undetected threat risks
- Risk assessments inform monitoring priorities (what to monitor)
- Risk treatment plans reference monitoring controls
- Residual risks documented and accepted (monitoring gaps, coverage limitations)
- Risk metrics reported to senior management (detection rate, MTTD, coverage %)

---

## 4.10 Compliance Monitoring

### 4.10.1 Compliance Measurement

Policy compliance **SHALL** be measured through:

**Technical Compliance**:
- Monitoring infrastructure deployed per requirements (S2.1)
- Baselines documented for critical systems (S2.2)
- Detection rules deployed and functional
- Alert response SLAs met (S2.3)
- Retention periods implemented correctly (S2.4)

**Operational Compliance**:
- Roles and responsibilities executed (S3)
- Review schedules adhered to (baselines, policies, detection rules)
- Incidents handled per procedures
- Metrics collected and reported

**Coverage Compliance**:
- Percentage of critical systems monitored (target: 100%)
- Percentage of all systems monitored (target: >80%)
- Detection coverage (MITRE ATT&CK techniques covered)

### 4.10.2 Monitoring Methods

**Automated Monitoring**:
- Configuration compliance checks (monitoring platforms configured per policy)
- Coverage dashboards (ISMS-IMP-A.8.16.3 - which systems monitored)
- Metric dashboards (ISMS-IMP-A.8.16.5 - MTTD, MTTR, false positives)
- Alert SLA tracking (time to triage, time to investigate)

**Manual Reviews**:
- Periodic audits (internal, external)
- Management reviews (quarterly/annual)
- Baseline documentation reviews
- Detection rule quality reviews
- Stakeholder interviews (system owners, SOC analysts)

**Continuous Monitoring**:
- Meta-monitoring (monitoring the monitoring infrastructure)
- SOC performance metrics (real-time dashboards)
- Incident analysis (were incidents detected? How quickly?)

### 4.10.3 Non-Compliance Handling

When non-compliance is identified:

**Minor Non-Compliance** (administrative, low risk):
- Example: Baseline review overdue by 2 weeks
- Document finding
- Create remediation plan (owner, timeline)
- Track to closure
- Report in routine compliance reports

**Major Non-Compliance** (technical gap, high risk):
- Example: Critical system not monitored, detection rate <70%
- Escalate to CISO immediately
- Conduct risk assessment
- Implement interim compensating controls if needed
- Create urgent remediation plan (7-30 day timeline)
- Report to executive management
- Track as high-priority issue

**Systemic Non-Compliance** (pattern indicating process failure):
- Example: Consistent SLA misses, baselines never updated, SOC not triaging
- CISO escalates to Executive Management
- Root cause analysis (resource shortage? Training gap? Tool limitation?)
- Strategic remediation plan (may require budget, hiring, tool replacement)
- Quarterly progress reporting to management

---

## 4.11 Metrics and Reporting

### 4.11.1 Policy Effectiveness Metrics

Organizations **SHALL** track:

**Coverage Metrics**:
- Systems monitored / total systems (target: 100% critical, >80% all)
- Log sources integrated / total log sources
- MITRE ATT&CK techniques covered / total techniques (target: >60%)

**Detection Metrics**:
- Detection rate from testing (target: >90%)
- Mean Time To Detect (MTTD) (target: <5 minutes for critical alerts)
- False Positive Rate (target: <25% overall, <10% for critical)

**Response Metrics**:
- Mean Time To Acknowledge (MTTA) (target: <15 min for critical)
- Mean Time To Triage (MTTT) (target: <1 hour for critical)
- Mean Time To Investigate (MTTI)
- Mean Time To Resolve (MTTR) (target: <8 hours for critical)
- SLA compliance rate (target: >95%)

**Operational Metrics**:
- Alert volume (trend over time - should stabilize or decrease with tuning)
- Alert-to-Incident ratio (how many alerts become incidents)
- Baseline documentation completeness (% of systems with baselines)
- Baseline staleness (days since last review)
- Detection rule count (active rules)
- SOC analyst workload (alerts per analyst per shift)

**Governance Metrics**:
- Policy review adherence (reviews completed on time)
- Audit findings (open, closed, overdue)
- Training completion (SOC, system owners)

### 4.11.2 Reporting Frequency

- **Daily**: Operational dashboards (alert volume, response times)
- **Weekly**: SOC performance metrics (MTTD, MTTR, SLA compliance)
- **Monthly**: Compliance metrics, baseline reviews, detection tuning
- **Quarterly**: Effectiveness metrics, risk posture, management reports
- **Annual**: Comprehensive policy review, ISMS reporting, strategic recommendations

### 4.11.3 Reporting Audience

- **SOC Team**: Daily/weekly operational metrics
- **SOC Lead**: All metrics, detailed analysis
- **CISO**: Weekly summaries, monthly/quarterly detailed reports
- **IT Management**: Quarterly coverage and compliance metrics
- **Executive Management**: Quarterly executive summaries (1-2 pages)
- **Board of Directors**: Annual risk and compliance summary
- **Auditors**: Compliance evidence, effectiveness metrics, audit artifacts

---

## 4.12 Continuous Improvement

### 4.12.1 Improvement Sources

Policy and operational improvements derive from:

- **Metrics analysis** (identify underperforming areas, trends)
- **Incident lessons learned** (detection gaps, response failures)
- **SOC feedback** (operational pain points, tool limitations)
- **Audit findings** (external recommendations, compliance gaps)
- **Industry benchmarking** (peer comparison, maturity models)
- **Technology evolution** (new detection methods, automation opportunities)
- **Regulatory changes** (new requirements)
- **Threat landscape evolution** (new adversary TTPs)

### 4.12.2 Improvement Process

1. **Identify**: Opportunities for improvement recognized (metrics, incidents, feedback)
2. **Analyze**: Root cause analysis, impact assessment, cost-benefit
3. **Propose**: Improvement recommendation developed with business case
4. **Approve**: CISO approves improvement initiative and resources
5. **Implement**: Changes made to policy, tools, processes, training
6. **Measure**: Effectiveness of improvement tracked (did metrics improve?)
7. **Standardize**: Successful improvements become standard practice

### 4.12.3 Lessons Learned

After significant incidents or events:

- Conduct post-incident review (ISMS-POL-A.5.24-28)
- Identify monitoring/detection gaps (what should have been detected but wasn't?)
- Identify alert response failures (delays, missed escalations, inadequate investigation)
- Recommend policy updates (new baselines, detection rules, procedures)
- Share lessons across SOC and security team
- Update training and playbooks (ISMS-POL-A.8.16-S5.C)
- Track remediation actions to closure
- Re-test detection (validate improvements work)

### 4.12.4 SOC Maturity Progression

Organizations **SHOULD** assess SOC maturity and plan progression:

**Maturity Levels**:
- **Level 1 (Initial)**: Reactive, ad-hoc monitoring, no baselines
- **Level 2 (Managed)**: Documented procedures, basic baselines, 24/7 monitoring
- **Level 3 (Defined)**: Comprehensive baselines, tuned detection, threat hunting
- **Level 4 (Quantitatively Managed)**: Metrics-driven, optimized processes, automation
- **Level 5 (Optimizing)**: Continuous improvement, predictive analytics, advanced threat hunting

**Progression Strategy**:
- Assess current maturity level
- Define target maturity (based on risk, budget, organizational needs)
- Create roadmap (what needs to improve to reach next level)
- Implement improvements incrementally
- Measure progress

---

## 4.13 Policy Retirement and Archival

### 4.13.1 Retirement Triggers

Policies **MAY** be retired when:

- Superseded by new policy version (e.g., v2.0 replaces v1.0)
- Organizational changes make policy obsolete (monitoring outsourced to MSSP)
- Regulatory changes invalidate policy approach
- Technology changes eliminate need for policy (platform replaced)
- Merger/acquisition creates redundant policies (consolidation needed)

### 4.13.2 Retirement Process

**Assessment**:
- Confirm policy is truly obsolete (not still needed)
- Identify dependencies (what relies on this policy? Other policies? Procedures?)
- Determine transition plan

**Communication**:
- Notify stakeholders of retirement
- Communicate replacement policy (if applicable)
- Provide transition timeline
- Update cross-references in other policies

**Archival**:
- Mark policy as "Retired" with effective date
- Move to archive repository (retain per retention policy)
- Remove from active policy portal
- Maintain for historical/audit purposes (minimum 7 years)
- Preserve version history

---

## 4.14 Governance Framework Summary

This governance framework ensures monitoring activities policies:

✅ Remain current and effective through lifecycle management  
✅ Align with organizational objectives and risk appetite  
✅ Comply with legal, regulatory, and standard requirements (ISO 27001, GDPR, etc.)  
✅ Engage stakeholders appropriately throughout lifecycle  
✅ Are communicated clearly to SOC and all affected parties  
✅ Adapt to changing threats, technologies, and business needs  
✅ Support continuous improvement culture (learn from incidents, metrics, feedback)  
✅ Integrate seamlessly with broader ISMS  
✅ Enable effective security operations without excessive bureaucracy

**Governance is not bureaucracy** - it's the framework ensuring monitoring delivers detection capability sustainably over time, adapting as threats evolve and organization changes.

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation
- **ISMS-POL-A.8.16-S2.x** (Requirements) - What is governed
- **ISMS-POL-A.8.16-S3** (Roles) - Who governs
- **ISMS-POL-A.8.16-S5** (Annexes) - Supporting materials
- **ISMS Manual** (Clause 5.2, 5.3) - Broader ISMS governance
- **Document Control Procedure** - General document lifecycle

---

*"Policy without governance rots. Governance without improvement ossifies. Balance both."*  
*—Security Governance Wisdom*