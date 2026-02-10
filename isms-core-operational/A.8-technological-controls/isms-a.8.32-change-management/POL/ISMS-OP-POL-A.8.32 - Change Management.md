<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.32:operational:OP-POL:a.8.32 -->
**ISMS-OP-POL-A.8.32 — Change Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Change Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.32 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.32 — Change management

**Related Annex A Controls**:

| Control | Relationship to Change Management |
|---------|-----------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset inventory defines change scope and impact assessment |
| A.5.24–28 Incident management | Failed changes may trigger incident response |
| A.5.37 Documented operating procedures | Procedures updated following system changes |
| A.8.8 Management of technical vulnerabilities | Patch deployment follows change management process |
| A.8.9 Configuration management | Configuration baselines updated after changes |
| A.8.19 Installation of software on operational systems | Software installations follow change management |
| A.8.25–29 Secure development lifecycle | Development changes follow change management |
| A.8.31 Separation of environments | Environment promotion controlled via change process |
| A.8.33 Test information | Test data protected during change testing |

**Related Internal Policies**:

- Asset Management Policy
- Incident Management Policy
- Documented Operating Procedures Policy
- Endpoint Security Policy (patch management)
- Network Security Policy

---

# Change Management Policy

## Purpose

The purpose of this policy is to manage the risk posed by changes to information processing systems, applications, infrastructure, and supporting technology, ensuring changes are planned, assessed, approved, tested, implemented, and documented in a controlled manner.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk, ensuring that changes to systems processing personal data do not compromise data protection safeguards. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All changes to information processing systems, applications, infrastructure, network equipment, cloud services, and supporting systems regardless of deployment model (on-premises, cloud, hybrid).

This includes hardware changes, software changes, configuration changes, infrastructure changes, data schema changes, and security system changes.

**Out of scope**: Website content updates (text, images), user self-service actions (password resets via approved portal), routine automated operations (scheduled backups, log rotation), and changes managed entirely by SaaS providers outside customer control.

## Principle

All changes to information processing systems shall be subject to formal change management procedures. Changes shall be planned, assessed for impact and risk, authorised, tested, communicated, implemented in a controlled manner, and documented. Emergency changes shall follow expedited procedures while maintaining control and oversight.

---

## Definitions

| Term | Definition |
|------|------------|
| **Change** | Any addition, modification, or removal of information system components (hardware, software, configuration, data) that could affect information security or system availability |
| **Standard Change** | Pre-approved, low-risk, routine change following documented procedure from the Standard Change Catalogue |
| **Normal Change** | Change requiring full assessment, CAB review, and standard approval workflow |
| **Emergency Change** | Change requiring expedited implementation to resolve critical incident, active vulnerability, or prevent significant business impact |
| **Change Advisory Board (CAB)** | Multi-disciplinary group providing expert review, impact assessment, and recommendations for changes |
| **Post-Implementation Review (PIR)** | Structured review after change implementation verifying objectives achieved and capturing lessons learned |
| **Failed Change** | Change that is rolled back due to failure to achieve objectives, unacceptable performance degradation, security vulnerability introduction, or critical business function impairment. A change requiring post-implementation fixes is not necessarily "failed" if the original change was not rolled back |

---

## Change Classification

All changes shall be classified into one of three categories:

| Type | Risk Level | Approval | CAB Review | Testing |
|------|-----------|----------|------------|---------|
| **Standard** | Low | Pre-approved (catalogue) | Not required | Per catalogue procedure |
| **Normal** | Medium–High | Service Owner / CAB / CISO (risk-based) | Required for high-risk | Non-production testing required |
| **Emergency** | Critical | CISO or IT Operations Manager | Retrospective (within 48 hours) | Risk-appropriate (may be abbreviated) |

Changes that fall into grey areas shall be escalated to the Change Manager for classification.

---

## Change Request Process

### Change Request Submission

All in-scope changes shall be submitted as formal change requests in the change management system: **[Specify: ServiceNow, Jira Service Management, Azure DevOps, or "In selection; interim: ticketing system/spreadsheet"]**.

**System access**: Change submission available to all IT staff; change approval and CAB coordination restricted to authorised personnel.

**Change ID format**: [Specify: CHG-YYYYMMDD-### or auto-generated by system].

Each change request shall include, at minimum:

| Field | Description |
|-------|-------------|
| Change ID | Unique identifier assigned by the system |
| Description | What is being changed and why |
| Business justification | Reason for the change |
| Systems affected | Assets, services, and dependencies impacted |
| Risk classification | Low / Medium / High / Critical |
| Implementation plan | Step-by-step procedure |
| Implementation window | Proposed date, time, and duration |
| Rollback plan | How to reverse the change if it fails |
| Testing approach | What testing will be performed |
| Requestor and implementer | Who requested and who will execute |
| Communication plan | Who needs to be informed |

### Impact and Risk Assessment

All changes shall be assessed for impact before implementation:

- **Technical impact**: Systems affected, dependencies, integration points.
- **Business impact**: Services affected, user impact, business operations disruption.
- **Security impact**: Confidentiality, integrity, availability risks. Changes affecting systems that process personal data shall include an assessment of data protection impact.
- **Compliance impact**: Regulatory obligations, audit controls.
- **Risk level**: Combination of likelihood of failure and magnitude of impact.

### Approval Workflow

Approval authority shall be based on change risk level:

| Risk Level | Approval Authority |
|------------|-------------------|
| **Low** (Standard Change) | Pre-approved via Standard Change Catalogue |
| **Medium** | Service Owner or Team Lead |
| **High** | IT Operations Manager and CISO |
| **Critical** | Executive Management |

---

## Change Advisory Board (CAB)

The organisation shall establish a Change Advisory Board for review of normal and emergency changes.

### CAB Composition

| Role | Responsibility |
|------|---------------|
| **Change Manager** (Chair) | Process ownership, scheduling, metrics, continuous improvement |
| **IT Operations representative** | Technical feasibility, infrastructure impact |
| **Security representative** | Security risk assessment, compliance impact |
| **Business application owners** | Business impact assessment (for relevant changes) |
| **Subject matter experts** | Technical expertise as needed |

### CAB Operations

- **Regular meetings**: **[Specify: Weekly on [day] at [time] CET]** (or as appropriate to change volume).
- **Meeting format**: [In-person / virtual / hybrid].
- **Agenda published**: 24 hours before meeting (change requests submitted by [day before] 17:00 for [meeting day] CAB).
- **Emergency CAB**: Convened as needed for urgent changes via [email/Teams/Slack]; may proceed with reduced quorum (Change Manager + one additional member) with full CAB retrospective within **48 hours**.
- **Quorum**: Change Manager, IT Operations representative, Security representative, and at least one additional member.
- **Records**: Meeting minutes shall be maintained for all CAB meetings, documenting date, attendees, changes reviewed, decisions, rationale, and action items. Minutes retained for **3 years**.

---

## Standard Change Catalogue

The organisation shall maintain a Standard Change Catalogue containing pre-approved, low-risk, routine changes.

### Catalogue Requirements

Each catalogue entry shall include:

- Change description and scope.
- Pre-conditions and prerequisites.
- Step-by-step procedure.
- Estimated duration.
- Rollback procedure (if applicable).
- Risk assessment (completed once during catalogue approval).

### Catalogue Governance

- Catalogue reviewed **quarterly** by the Change Manager with CAB input.
- New entries added from successful normal changes that are repeatable and low-risk.
- Entries removed or reclassified after any standard change failure.
- Success rate target: **>95%** for standard changes.

Standard changes shall still be logged in the change management system for audit trail and incident correlation, even though CAB review is not required.

### Standard Change Catalogue Examples

Typical pre-approved standard changes include:

| Change | Procedure Reference | Estimated Duration | Prerequisites |
|--------|--------------------|--------------------|---------------|
| Add user to Active Directory group | IT-SOP-001 | 5 minutes | Approved access request ticket |
| Restart application server (non-production) | IT-SOP-015 | 10 minutes | Service owner notification |
| SSL certificate renewal | IT-SOP-023 | 30 minutes | New certificate obtained, backup of old cert |
| DNS record addition (internal domain) | IT-SOP-031 | 10 minutes | DNS change request form completed |
| Firewall rule for approved application | IT-SOP-045 | 15 minutes | Security team pre-approval, rule documented |

**Not standard changes**: Database schema changes, OS upgrades, network topology changes, new software installations, security configuration changes affecting production.

---

## Testing and Validation

### Testing Requirements

Changes shall be tested before deployment to production:

| Change Risk | Required Testing |
|-------------|-----------------|
| **Low** (Standard) | Per catalogue procedure; implementer verification |
| **Medium** | Functional testing and integration testing in non-production environment |
| **High** | Functional, integration, performance, and user acceptance testing |
| **Critical** | Full testing suite including security testing and disaster recovery validation |

### Environment Separation

- Changes shall be tested in non-production environments (development, test/QA, staging) before production deployment.
- Non-production environments shall be logically or physically separated from production with separate credentials and access controls.
- Production data shall not be used in test environments without masking or anonymisation per the Information Classification and Handling Policy.
- Promotion from test to production shall require formal sign-off and verified test results.

### Production Environment Protection

Production changes shall be executed only by authorised personnel with the following controls:

- **Separation of duties**: Developers shall not deploy their own changes to production without independent review and approval from a designated release manager, operations team member, or CAB.
- **Peer review**: Code changes require peer review and approval before production deployment (via pull request or equivalent mechanism).
- **Multi-factor authentication** shall be required for production access.
- **Privileged access management**: Production deployment accounts shall be separate from development accounts.
- **All production changes shall be audit-logged** with user identity, timestamp, and change content.

**Exception**: In organisations with fewer than 5 IT staff where full separation is not feasible, compensating controls shall include enhanced logging, CISO review of all production changes monthly, and peer review post-implementation.

---

## Implementation and Rollback

### Controlled Implementation

Changes shall be implemented following the approved implementation plan with:

- Verification of prerequisites and dependencies before starting.
- Execution of documented steps.
- Real-time monitoring during implementation.
- Post-implementation verification testing.
- Documentation of actual steps performed and any deviations.

### Maintenance Windows

The organisation shall establish preferred change windows to minimise business disruption:

**Preferred change windows**:
- **Standard window**: [Specify: e.g., Tuesdays and Thursdays 20:00–23:00 CET]
- **Extended window**: [Specify: e.g., Saturday 08:00–16:00 CET]
- **Emergency**: Any time with CISO approval

**Restricted periods** (no non-emergency changes):
- [Business-specific: e.g., "First week of each month (financial close)", "December 15–January 5 (year-end freeze)"]
- Public holidays: Swiss federal holidays
- Major business events: documented in change calendar 90 days in advance

Changes outside preferred windows require **High risk approval authority** (IT Operations Manager + CISO) regardless of technical risk level.

### Rollback

A rollback procedure shall be agreed upon before implementing changes to production systems. Rollback shall be executed when:

- The change fails to achieve its objectives.
- Unacceptable performance degradation occurs.
- A security vulnerability is introduced.
- Critical business functions are impaired.

Rollback decision authority: same approval authority as the original change (or higher for emergency rollback).

### Rollback Testing

For **High** and **Critical** risk changes, rollback procedures shall be:

- Documented and approved as part of the change request.
- **Tested in non-production** before production implementation (where feasible).
- Verified as executable within the defined rollback window.

Rollback testing shall verify:

- Rollback procedure steps are accurate and complete.
- Rollback can be completed within the change window.
- Data integrity is maintained during rollback.
- Service restoration is confirmed.

Where rollback testing is not feasible (one-way migrations, destructive changes), a **forward-fix** plan shall be documented as an alternative to rollback.

---

## Communication

### Stakeholder Notification

Affected stakeholders shall be notified of changes, including:

- Change schedule and timing.
- Expected service impact (duration, scope).
- User actions required (if any).
- Contact information for support during the change.

**Planned changes**: Minimum advance notification per organisational requirements (recommended: 5 business days for high-impact, 2 business days for medium-impact).

**Emergency changes**: Communication as soon as safely possible.

**Change completion**: Confirmation sent to stakeholders when the change is complete.

---

## Emergency Changes

### Emergency Classification Criteria

Changes shall be classified as emergency only when:

- Resolving an active security incident or actively exploited vulnerability.
- Restoring a critical service outage.
- Preventing imminent system failure.
- Addressing an urgent regulatory requirement.
- Mitigating an active data breach.

Emergency classification shall **not** be used for convenience, poor planning, routine work, or desired features.

### Emergency Change Process

1. Emergency justification documented (even if brief).
2. Approval from CISO or IT Operations Manager (minimum).
3. Risk-appropriate testing (abbreviated test cases, or documented risk acceptance if testing not feasible).
4. Implementation with enhanced monitoring.
5. Rollback plan in place before execution.
6. Retrospective CAB review within **48 hours**.
7. Mandatory Post-Implementation Review within **5 business days**.

### Emergency Change Monitoring

Emergency change percentage shall be tracked monthly. Target: **<5%** of all changes.

When emergency changes exceed 5% for two consecutive months:

1. Root cause analysis conducted by Change Manager within **14 days**.
2. Findings presented to CAB and CISO.
3. Remediation actions implemented within **30 days**, which may include: additional training on change classification, process improvements (e.g., faster approval workflows for urgent but non-emergency changes), resource adjustments, or disciplinary action for abuse of emergency classification.
4. Follow-up review after **60 days** to verify effectiveness.

**Emergency change abuse**: Using emergency classification inappropriately (convenience, poor planning) constitutes policy non-compliance and shall be escalated to the CISO.

---

## Post-Implementation Review (PIR)

Post-implementation reviews shall be conducted for:

- **All emergency changes** (mandatory).
- **All failed changes** (mandatory).
- **Normal changes classified as high-risk or critical**.

### PIR Content

- Objectives achieved vs. planned outcomes.
- Issues encountered during implementation.
- Effectiveness of planning and testing.
- User feedback and service impact.
- Lessons learned and improvement opportunities.
- Whether the change should be added to the Standard Change Catalogue.

### PIR Timing

- Emergency changes: within **5 business days**.
- Failed changes: within **5 business days**.
- High-risk normal changes: within **14 business days**.

---

## Change Freeze Periods

At critical times of the year, the organisation may impose a change freeze period during which only emergency changes are permitted.

Change freeze periods shall be:

- Approved by executive management or the CISO.
- Communicated to all stakeholders in advance (minimum 2 weeks).
- Documented in the change calendar.
- Examples: year-end financial close, major product launches, peak business seasons, regulatory submission periods.

---

## Record Keeping and Documentation

### Change Records

Complete change records shall be maintained including:

- All change request information.
- Approval records with timestamps and approvers.
- CAB review notes and recommendations.
- Implementation logs and verification results.
- Communication records.
- Issues or incidents during implementation.
- Rollback decisions and execution (if applicable).
- Post-implementation review results.

Change records shall be retained for a minimum of **3 years** for operational reference and **7 years** for audit evidence.

### Documentation Updates

Following system changes, the following documentation shall be updated within **5 business days**:

- System configuration documentation.
- Network diagrams and topology.
- Operational procedures and runbooks.
- Disaster recovery procedures (where the change affects critical systems or RTO/RPO).

---

## Configuration Management Integration

Change management and configuration management are complementary disciplines:

- **Change management** controls *how* changes are made (approval, testing, implementation).
- **Configuration management** controls *what* the current state is (baselines, versions, configuration items).

**Integration points**:

- Configuration baselines shall be updated following approved changes.
- Configuration drift detection (actual vs. baseline) shall trigger investigation and a corrective change request.
- The configuration management database (CMDB) or equivalent inventory shall be the authoritative source for impact assessment (what systems are affected).

See **Configuration Management Policy (A.8.9)** for detailed baseline and version control requirements.

---

## Unauthorised Changes

Unauthorised changes — changes made without following the change management process — shall be:

- Detected through monitoring, audit logging, and configuration management tools.
- Investigated to determine root cause and impact.
- Reported to the CISO and escalated to the Management Review Team.
- Subject to corrective action, which may include disciplinary action per the organisation's disciplinary process.

---

## Change-Incident Correlation

When a security incident or service outage occurs, the Change Manager shall:

1. **Review recent changes** within 48 hours prior to incident start time.
2. **Correlate incident timeline** with change implementation timestamps.
3. **Identify potentially related changes** (same systems, dependencies, timeframe).
4. **Escalate to CAB and CISO** if a change is suspected as root cause.

Where a change is confirmed as the root cause of an incident:

- **Mandatory Post-Implementation Review** within **3 business days**.
- **Root cause analysis** to identify process gaps (testing inadequate, impact assessment missed, approval insufficient).
- **Corrective actions** to prevent recurrence.
- If the change was in the Standard Change Catalogue, the catalogue entry shall be reviewed and potentially reclassified or removed.

Change-related incident rate is tracked as a key metric (target: 0 per quarter).

---

## Change Management Metrics

The information security management team shall report change management metrics to the CISO at least quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Change success rate (changes completed without rollback or incident) | ≥95% | <85% |
| Emergency change percentage | <5% | >10% |
| PIR completion rate (for mandatory PIRs) | 100% | <80% |
| Standard Change Catalogue utilisation | ≥30% of all changes | <15% |
| Change-related incidents | 0 | >2 per quarter |
| Overdue changes (past scheduled implementation) | 0 | >5 |
| Documentation update compliance (within 5 business days) | ≥95% | <80% |

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of high-risk and emergency changes; exception authorisation; metrics review |
| **Change Manager** | Process ownership; CAB chair; Standard Change Catalogue maintenance; metrics tracking; continuous improvement |
| **IT Operations Manager** | Medium/high-risk change approval; emergency CAB chair; change window coordination |
| **CAB Members** | Change review, impact assessment, risk identification, approval recommendations |
| **Change Requestors** | Submit complete change requests with business justification and impact assessment |
| **Change Implementers** | Execute approved changes following documented procedures; perform verification testing |
| **System Owners** | Approve changes to owned systems; provide impact assessment; accountable for system availability |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Change management system** records (all change requests with required fields) | Change Manager | *Per event; audited quarterly* |
| 2 | **CAB meeting minutes** (attendees, decisions, rationale, action items) | Change Manager | *Per meeting; retained 3 years* |
| 3 | **Standard Change Catalogue** with version history and quarterly review records | Change Manager | *Reviewed quarterly; version-controlled* |
| 4 | **Change calendar** with freeze periods and scheduled changes | Change Manager | *Maintained continuously; reviewed monthly* |
| 5 | **Post-Implementation Review** records for emergency, failed, and high-risk changes | Change Manager | *Per qualifying change; target: 100% completion* |
| 6 | **Approval records** with timestamps showing appropriate authority per risk level | Change Manager | *Per change; retained 7 years* |
| 7 | **Testing records** (test plans, results, sign-offs) for normal and high-risk changes | IT Operations | *Per change; retained 3 years* |
| 8 | **Emergency change justification** and retrospective CAB review records | CISO | *Per emergency change; reviewed monthly* |
| 9 | **Change management metrics** reports | Change Manager | *Quarterly; presented at management review* |
| 10 | **Unauthorised change** investigation and corrective action records | CISO | *Per event; retained 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, change record audits, CAB meeting reviews, PIR completion tracking, emergency change analysis, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to change management standards, technology changes, emerging risks, regulatory changes, PIR findings, and lessons learned from change-related incidents.

---

# Areas of the ISO 27001 Standard Addressed

Change Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 6.3 Planning of changes | 5.37 Documented operating procedures |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| Clause 8.1 Operational planning and control | 6.4 Disciplinary process |
| | **8.32 Change management** |
| | 8.9 Configuration management |
| | 8.19 Installation of software on operational systems |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (change management as organisational measure protecting data processing systems) |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (change management as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Control 8.32 — Change management |
| ISO/IEC 27002:2022 | Section 8.32 — Implementation guidance (9 mandatory elements) |
| NIST SP 800-53 Rev 5 | CM-3 (Configuration Change Control), CM-4 (Impact Analyses), CM-5 (Access Restrictions for Change) |
| CIS Controls v8 | Control 2 (Inventory and Control of Software Assets — Safeguard 2.5: Allowlist Authorised Software) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
