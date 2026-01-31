# Control A.8.24: Use of Cryptography
## SECTION 4
## Policy Governance

---

**Document ID**: ISMS-POL-A.8.24-S4  
**Title**: Use of Cryptography - Policy Governance  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Governance Manager | Initial governance and lifecycle management framework |

**Review Cycle**: Annual (or upon ISMS framework changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) or IT Director
- Governance: Quality Management / ISMS Coordinator
- Compliance: Legal/Compliance Officer (for governance frameworks)
- Risk: Risk Management Officer (for risk assessment processes)

**Distribution**: ISMS Steering Committee, Management Team, Internal Audit, Risk Management, Quality Management  
**Related Standards**: ISO/IEC 27001:2022 Clauses 4-10, Control A.8.24, ISO/IEC 27002:2022 governance guidance, PDCA cycle

---

## 4. Policy Governance

### Purpose
This section establishes the framework for maintaining, reviewing, updating, and enforcing this cryptography policy to ensure it remains effective, current, and aligned with organizational objectives and regulatory requirements.

---

## 4.1 Policy Review and Updates

### 4.1.1 Review Schedule

#### Annual Policy Review

**Timing:**
- Scheduled annually on **[Month]** each year
- Review date: Anniversary of policy approval date (or designated month)
- Review must be completed within 30 days of scheduled date

**Responsible Party:**
- **Lead:** Chief Information Security Officer (CISO)
- **Support:** Information Security Officer/Security Manager
- **Participants:**
  - IT Manager
  - Network Team Lead
  - Security Team Lead
  - Database Administrator Lead
  - Development Manager
  - Compliance Manager
  - Representatives from key business units

**Review Scope:**
- **Cryptographic standards review:**
  - Compare approved algorithms against current NIST/BSI/ENISA recommendations
  - Review key length requirements
  - Update TLS/SSL version requirements
  - Assess password hashing algorithm recommendations
- **Emerging threats assessment:**
  - Quantum computing readiness
  - New cryptanalytic attacks
  - Supply chain vulnerabilities
  - Side-channel attack evolution
- **Technology evaluation:**
  - New cryptographic technologies (post-quantum cryptography, homomorphic encryption)
  - Cloud provider cryptographic capabilities
  - HSM and KMS product updates
- **Regulatory changes:**
  - New or updated regulations (GDPR, PCI DSS, HIPAA, etc.)
  - Export control regulation changes
  - Industry-specific requirement updates
- **Gap remediation progress:**
  - Review implementation status document (ISMS-IMP-A.8.24)
  - Assess remediation plan completion
  - Identify new gaps or challenges
- **Incident lessons learned:**
  - Review cryptographic incidents from past year
  - Incorporate lessons learned into policy
  - Update procedures based on incident experience
- **Stakeholder feedback:**
  - Collect feedback from policy users (IT, security, development teams)
  - Address practical implementation challenges
  - Consider exception request patterns for policy improvement

**Review Outputs:**
- Documented review meeting minutes
- List of identified changes/updates
- Updated risk assessment (if applicable)
- Recommendations for policy updates
- Updated implementation roadmap
- Budget recommendations for cryptographic upgrades

#### Quarterly Implementation Review

**Timing:**
- End of each quarter (Q1, Q2, Q3, Q4)
- Review conducted by Security Team with ISO oversight

**Review Scope:**
- Certificate inventory validation and expiration forecast
- Gap remediation progress tracking
- Cryptographic incident review (if any occurred)
- Compliance metrics review (KPIs from Section 2.5)
- Exception register review
- Key rotation compliance verification
- Training completion status

**Outputs:**
- Quarterly compliance report
- Action items for remediation
- Escalation of critical issues to CISO

#### Triggered Reviews

**Policy review MUST be triggered upon:**
- **Major security incident** involving cryptography
  - Example: Widespread key compromise, major cryptographic vulnerability exploitation
  - Review initiated within 30 days of incident resolution
- **Significant cryptographic vulnerability disclosure**
  - Example: Heartbleed-scale vulnerability affecting organizational systems
  - Emergency assessment within 24 hours, policy review within 7 days if necessary
- **Regulatory changes** affecting cryptographic requirements
  - Review initiated within 60 days of regulatory publication
- **Major infrastructure changes**
  - Cloud migration, data center consolidation, major application deployment
  - Review conducted during project planning phase
- **Merger/acquisition activities**
  - Cryptographic posture assessment of acquired entity
  - Policy harmonization within 90 days of acquisition close
- **External audit findings** related to cryptography
  - Review initiated within 30 days of audit report
- **Technology obsolescence**
  - Example: Vendor end-of-support for cryptographic products
  - Review initiated when obsolescence becomes known

#### Industry Standards and Policy Changes

**Review triggered by:**
- **CA/Browser Forum ballot approvals** affecting baseline requirements
- **Browser root program policy changes** (Chrome Root Program, Apple Certificate Transparency, Mozilla CA Certificate Policy, Microsoft Trusted Root Program)
- **Certificate Authority security incidents** or trust store removals
- **NIST cryptographic standard publications** (FIPS updates, algorithm deprecations)
- **Post-quantum cryptography milestones** (NIST PQC standardization phases)
- **Critical cryptanalysis discoveries** (practical attacks on approved algorithms)

**Monitoring Sources:**
- CA/Browser Forum: https://cabforum.org/ballots/
- NIST Cryptographic Standards: https://csrc.nist.gov/publications/
- Browser root programs:
  - Chrome: https://g.co/chrome/root-policy
  - Apple: https://www.apple.com/certificateauthority/ca_program.html
  - Mozilla: https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/
  - Microsoft: https://aka.ms/RootCert

**Review Timeline:**
- Critical security events: Expedited review within 7 days (CISO approval)
- Ballot approvals affecting operations: Review within 30 days of effective date
- Informational updates: Next scheduled quarterly/annual review cycle

**Responsibility:**
- Monitoring: Information Security team (primary), CISO (oversight)
- Assessment: ISO/Security Manager + Technical Lead (joint)
- Policy updates: CISO (author), Executive Management (approval for major changes)

---

### 4.1.2 Update Process

#### Change Proposal

**Who Can Propose Changes:**
- CISO or ISO (policy owner)
- IT Management
- Security Team
- Compliance Team
- Any employee via formal suggestion process

**Proposal Requirements:**
- Rationale for change (business need, regulatory requirement, security improvement)
- Impact analysis (systems affected, implementation effort, cost)
- Risk assessment (risk of change vs. risk of no change)
- Implementation timeline recommendation

#### Change Review and Approval

**Review Process:**

1. **Initial Review (ISO/Security Manager):**
   - Assess proposal validity and completeness
   - Conduct preliminary impact analysis
   - Determine if change is minor (editorial) or major (substantive)

2. **Minor Changes (Editorial):**
   - Examples: Typos, formatting, clarifications without changing requirements
   - Approval: ISO or Security Manager
   - Notification: Inform stakeholders of change
   - No formal approval cycle required

3. **Major Changes (Substantive):**
   - Examples: New requirements, changed standards, modified procedures
   - Convene review meeting with stakeholders
   - Technical feasibility assessment
   - Business impact assessment
   - Cost-benefit analysis

**Approval Authority:**

| Change Type | Approval Required | Timeline |
|-------------|-------------------|----------|
| **Minor (editorial)** | ISO or Security Manager | Immediate |
| **Moderate (single section)** | CISO + IT Manager | 2-4 weeks |
| **Major (multiple sections)** | CISO + IT Manager + Management Team | 4-8 weeks |
| **Significant (strategic change)** | Executive Committee | 8-12 weeks |

**Approval Documentation:**
- Signed approval form or email approval
- Document version control updated
- Change log in Document Control table (page 1) updated

#### Communication and Implementation

**Communication Plan:**
- **Material policy changes (Part 2 - Policy Requirements):**
  - Email notification to all employees
  - Announcement in company communication channels
  - Training update if necessary
  - 30-day transition period (unless urgent security need)
  
- **Implementation updates (Part 3 - Compliance tracking):**
  - Notification to IT and Security teams only
  - Update in next scheduled meeting
  
- **Technical standard updates (Appendices):**
  - Notification to technical teams (IT, Development, Database, Network)
  - Technical bulletin or wiki update
  - Include in next quarterly review meeting

**Implementation Timeline:**
- Target implementation date MUST be specified
- Reasonable transition period for systems to comply
- Critical security changes: Immediate to 30 days
- Standard changes: 30-90 days
- Strategic changes: 90-180 days

**Training and Awareness:**
- Update training materials to reflect policy changes
- Conduct refresher training if significant changes
- Update quick reference guides and job aids

---

### 4.1.3 Version Control

#### Versioning Scheme

**Format:** Major.Minor (e.g., 1.0, 1.1, 2.0)

**Major Version (X.0):**
- Policy requirements changes requiring management approval
- New or removed mandatory controls
- Significant changes to scope or applicability
- Changes requiring board or executive approval

**Minor Version (x.X):**
- Implementation status updates
- Gap remediation progress
- Editorial changes and clarifications
- Appendix updates (technical standards)
- Minor procedural updates

**Version History:**
- All changes documented in Document Control table (Section 1)
- Summary of changes required for each version
- Previous versions archived and accessible

#### Document Storage and Access

**Master Copy:**
- Stored in: **[ISMS document repository location - e.g., SharePoint, Document Management System]**
- Format: **[Word/PDF/Both]**
- Access control: Read access for all employees, edit access for document owner only

**Version Archive:**
- Previous versions retained for audit and reference
- Retention period: Permanent for major versions, 7 years for minor versions
- Storage location: **[Archive location]**

**Distribution:**
- Policy published in organizational intranet/wiki
- Direct links sent via email for material changes
- Included in onboarding materials for new employees

---

## 4.2 Policy Exceptions

### 4.2.1 Exception Philosophy

**Principles:**
- Exceptions are **temporary** and **risk-based**
- Exceptions do NOT eliminate compliance obligation, only defer or provide alternative
- Exceptions require compensating controls
- Exceptions MUST have documented business justification
- Exceptions expire and require renewal

**When Exceptions Are Appropriate:**
- Technical impossibility of full compliance
- Legacy systems with documented end-of-life and replacement plan
- Unique business requirement that cannot be met otherwise
- Compensating controls provide equivalent or near-equivalent risk mitigation
- Cost of compliance grossly disproportionate to risk (with risk acceptance)

**When Exceptions Are NOT Appropriate:**
- Convenience or preference
- Lack of planning or resources (without risk acceptance at executive level)
- Fundamental violation of regulatory requirements (e.g., PCI DSS mandate)
- Unacceptable risk without adequate compensating controls

---

### 4.2.2 Exception Request Process

#### Step 1: Exception Request Submission

**Request Initiator:**
- System owner, project manager, or business unit manager
- Must complete Exception Request Form (see Appendix B in Section 5)

**Required Information:**
- System/application identification and description
- Specific policy requirement(s) unable to comply with
- Current implementation state
- Detailed technical justification
- Business justification and impact if not granted
- Risk assessment (likelihood and impact of non-compliance)
- Proposed compensating controls
- Requested exception duration (with justification)
- Remediation plan (if temporary exception)

**Submission:**
- Submit to Information Security Officer (ISO) or Security Team
- Submission via **[ticketing system/email/form]**

#### Step 2: Initial Review and Risk Assessment

**Conducted By:** Information Security Officer (ISO) or Security Manager

**Review Activities:**
- Validate completeness of request
- Conduct independent risk assessment
- Evaluate adequacy of compensating controls
- Assess precedent (similar exceptions previously granted?)
- Determine approval authority level required

**Risk Classification:**

| Risk Level | Criteria | Examples |
|------------|----------|----------|
| **Low** | Limited scope, adequate compensating controls, low impact | Single internal non-production system, TLS 1.2 instead of 1.3 |
| **Medium** | Moderate scope, partial compensating controls, moderate impact | Internal production system, delayed key rotation (3-6 months overdue) |
| **High** | Broad scope, limited compensating controls, high impact | Customer-facing system, unencrypted database with network segmentation |
| **Critical** | Enterprise-wide, no adequate compensating controls, regulatory violation | No encryption for payment card data, plaintext password storage |

**Initial Review Outcome:**
- **Approved for further review:** Proceed to approval authority
- **Denied:** Insufficient justification, unacceptable risk, or no compensating controls
- **Returned for revision:** Incomplete or unclear, requires additional information

**Timeline:** Initial review within 5 business days

#### Step 3: Approval

**Approval Authority (based on risk level):**

| Risk Level | Approval Required | Timeline |
|------------|-------------------|----------|
| **Low** | IT Manager + Security Team Lead | 5 business days |
| **Medium** | CISO (or delegated ISO with CISO notification) | 10 business days |
| **High** | CISO + Senior Management (CIO/CTO) | 15 business days |
| **Critical** | Executive Committee + Risk Committee | 20 business days |

**Approval Considerations:**
- Adequacy of risk assessment
- Quality of compensating controls
- Business justification strength
- Regulatory compliance impact
- Precedent and consistency
- Remediation plan credibility (for temporary exceptions)

**Approval Conditions:**
- Exception may be approved with conditions (additional compensating controls, shorter duration, specific monitoring requirements)
- Approval must be documented in writing (email or signed form)

**Denial:**
- Denial reasons must be documented
- Requestor has right to appeal to next level of authority
- Alternative solutions may be suggested

#### Step 4: Exception Documentation and Tracking

**Exception Register:**
- All approved exceptions logged in centralized Exception Register
- Register maintained by ISO or Compliance Team
- Register includes: System, policy section, risk level, approval date, expiration date, compensating controls, responsible person

**Documentation Requirements:**
- Signed exception approval form
- Risk assessment documentation
- Compensating control implementation evidence
- Monitoring and review schedule

**Communication:**
- Exception approval communicated to requestor and relevant stakeholders
- Security Team notified for monitoring setup
- Audit team notified for compliance tracking

---

### 4.2.3 Exception Lifecycle Management

#### Monitoring and Compliance

**Ongoing Monitoring:**
- Compensating controls MUST be verified as operational
- Monitoring frequency based on risk level:
  - Critical/High: Monthly
  - Medium: Quarterly
  - Low: Semi-annually
- Non-compliance with exception terms triggers incident response

**Quarterly Exception Review:**
- ISO reviews all active exceptions quarterly
- Verify continued justification
- Assess whether compensating controls remain effective
- Check progress on remediation plan (if applicable)
- Escalate overdue remediations to management

#### Exception Renewal

**Expiration:**
- All exceptions have maximum duration (typically 1 year)
- Notification sent 60 days before expiration
- System owner must either:
  - Come into compliance (close exception)
  - Request renewal with updated justification

**Renewal Process:**
- Renewal is NOT automatic
- Requires new justification (why still necessary?)
- Updated risk assessment
- Review of compensating controls effectiveness
- Same approval authority as original exception
- Maximum renewal period: 1 year (unless regulatory prohibition prevents compliance)

**Permanent Exceptions:**
- Very rare, only for legacy systems with documented end-of-life
- Require executive-level approval
- Annual review mandatory
- Sunset date MUST be defined (system decommission date)

#### Exception Closure

**Closure Triggers:**
- System comes into compliance
- System decommissioned
- Exception expires without renewal
- Compensating controls deemed inadequate
- Risk level becomes unacceptable

**Closure Process:**
- Verify compliance or system decommission
- Update Exception Register (closed status)
- Document closure date and reason
- Remove from active monitoring

---

## 4.3 Non-Compliance and Enforcement

### 4.3.1 Non-Compliance Identification

**How Non-Compliance is Detected:**
- Automated compliance scanning (TLS configuration, encryption status)
- Internal audits
- Security assessments and penetration testing
- Incident investigations
- Employee reporting
- External audit findings
- Compliance monitoring reports

**Non-Compliance Categories:**

| Category | Description | Examples |
|----------|-------------|----------|
| **Unintentional** | Lack of awareness, misconfiguration, oversight | Developer unaware of password hashing requirements |
| **Systemic** | Process or technology gap | No automated certificate expiration monitoring |
| **Resource Constraint** | Insufficient budget or staff | Cannot afford HSM for key management |
| **Willful** | Intentional disregard of policy | Disabling encryption "for performance" |

---

### 4.3.2 Non-Compliance Response Process

#### Step 1: Discovery and Documentation

**Upon discovering non-compliance:**
- Document the non-compliance:
  - System/application affected
  - Policy requirement violated
  - Current state vs. required state
  - Discovery method and date
  - Potential risk/impact
- Classify severity:
  - **Critical:** Immediate security risk, regulatory violation
  - **High:** Significant risk, material non-compliance
  - **Medium:** Moderate risk, limited scope
  - **Low:** Minor deviation, low risk

#### Step 2: Notification

**Notification Recipients:**
- System owner
- Responsible team/individual
- Information Security Officer (ISO)
- IT Manager (if infrastructure-related)
- CISO (for High/Critical severity)

**Notification Timeline:**
- Critical: Immediate (within 2 hours)
- High: Same business day
- Medium: Within 2 business days
- Low: Within 5 business days

#### Step 3: Remediation Planning

**Remediation Options:**
1. **Immediate Remediation:** Come into compliance immediately
2. **Scheduled Remediation:** Develop plan with target date
3. **Exception Request:** Submit formal exception if compliance not possible
4. **Risk Acceptance:** Formal acceptance of risk by appropriate authority (rare)

**Remediation Plan Requirements:**
- Root cause analysis (why did non-compliance occur?)
- Specific remediation actions
- Responsible person assigned
- Target completion date
- Interim compensating controls (if necessary)
- Verification method

**Approval:**
- ISO approves remediation plans for Medium/Low severity
- CISO approves remediation plans for High/Critical severity

#### Step 4: Remediation Implementation

**Implementation Tracking:**
- Remediation tracked in compliance tracking system or risk register
- Regular status updates required (frequency based on severity)
- Escalation if milestones missed

**Verification:**
- Compliance verification required upon claimed completion
- Verification by Security Team or independent audit
- Evidence documentation required

#### Step 5: Closure

**Closure Criteria:**
- Full compliance achieved, OR
- Exception formally granted, OR
- Risk formally accepted by appropriate authority

**Documentation:**
- Final verification evidence
- Lessons learned documentation
- Process improvements identified

---

### 4.3.3 Enforcement and Consequences

#### Progressive Discipline for Willful Non-Compliance

**First Offense:**
- Written warning to individual and manager
- Mandatory security refresher training
- Escalation to HR for documentation

**Second Offense:**
- Formal disciplinary action per HR policy
- Potential suspension of access privileges
- Mandatory review of all work for compliance

**Third Offense:**
- Escalation to senior management
- Potential termination of employment (or contract)
- Legal action if gross negligence or malicious intent

#### Organizational Consequences

**System-Level:**
- Non-compliant systems MAY be blocked from network or shut down if posing unacceptable risk
- Access to non-compliant systems may be restricted
- Non-compliant systems excluded from production promotion

**Team-Level:**
- Performance reviews may reflect compliance failures
- Budget allocation may be affected by persistent non-compliance
- Additional oversight and controls for teams with compliance issues

#### Regulatory and Legal Consequences

**Regulatory Non-Compliance:**
- Potential fines and penalties (GDPR, PCI DSS, HIPAA)
- Loss of regulatory certifications or licenses
- Mandatory reporting to regulators
- Increased audit scrutiny

**Legal Liability:**
- Potential lawsuits from customers or partners (breach of contract)
- Regulatory enforcement actions
- Civil penalties
- Reputational damage

---

### 4.3.4 Incentives for Compliance

**Positive Reinforcement:**
- Recognition of teams/individuals with excellent compliance records
- Compliance metrics included in performance reviews (positive factor)
- "Security Champion" awards or recognition program
- Compliance success stories shared in company communications

**Organizational Support:**
- Budget priority for compliance initiatives
- Training and resources to support compliance
- Streamlined exception process for legitimate needs
- Collaboration rather than enforcement-first approach

---

## 4.4 Continuous Improvement

### 4.4.1 Feedback Mechanisms

**How to Provide Feedback:**
- Email to CISO or ISO: **[email address]**
- Submit via ticketing system: **[system name]**
- Discuss at Cryptography Working Group meetings
- Anonymous feedback option: **[survey/form link]**

**Types of Feedback Encouraged:**
- Policy clarity issues
- Implementation challenges
- Suggestions for improvement
- New use cases not addressed
- Technology recommendations
- Process improvement ideas

**Feedback Response:**
- Acknowledgment of receipt within 5 business days
- Evaluation of feedback
- Response or action plan within 20 business days
- Incorporation into next policy review cycle

---

### 4.4.2 Metrics and Performance Tracking

**Policy Effectiveness Metrics:**
- Compliance rate (percentage of systems in compliance)
- Exception rate (percentage of systems with active exceptions)
- Non-compliance incident frequency
- Time to remediate non-compliance
- Certificate expiration incident rate
- Cryptographic vulnerability remediation time

**Continuous Improvement Targets:**
- Year-over-year improvement in compliance rates
- Reduction in non-compliance incidents
- Faster remediation times
- Increased automation of compliance verification

**Reporting:**
- Quarterly dashboard to IT and Security leadership
- Annual report to executive management
- KPIs reviewed during policy review cycle

---

### 4.4.3 Lessons Learned Process

**Incident Lessons Learned:**
- Post-incident review for all cryptographic incidents
- Identify policy gaps or ambiguities that contributed
- Recommend policy or process improvements
- Implement improvements within 60 days

**Audit Findings:**
- Review audit findings for policy-related issues
- Assess whether policy was inadequate or compliance was lacking
- Update policy if gaps identified
- Track audit finding trends

**Industry Best Practice Monitoring:**
- Security team monitors industry developments
- Participation in security forums and working groups
- Evaluation of new cryptographic technologies
- Benchmarking against peers and standards

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1 to S2.5** - Policy Requirements
- **ISMS-POL-A.8.24-S3** - Roles & Responsibilities
- **ISMS-POL-A.8.24-S5** - Appendices (next section)
- **ISMS-IMP-A.8.24** - Implementation Status
- **ISMS Incident Response Plan**
- **ISMS Risk Management Framework**
- **ISMS Change Management Policy**

---

**End of Section 4 - Policy Governance**

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled."*  
*— Richard Feynman, Rogers Commission Report*