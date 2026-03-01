<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.32:framework:POL:a.8.32 -->
**ISMS-POL-A.8.32 – Change Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Change Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.32 |
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
| 1.0 | [Date] | CISO | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) / IT Operations Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (CEO)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.32.1-UG/TG (Change Process Assessment)
- ISMS-IMP-A.8.32.2-UG/TG (Change Types & Categories Assessment)
- ISMS-IMP-A.8.32.3-UG/TG (Environment Separation Assessment)
- ISMS-REF-A.8.32 (Change Management Reference - Templates, Tools, Quick Guides)
- ISO/IEC 27001:2022 Control A.8.32

---

## Executive Summary

This policy establishes [Organisation]'s requirements for change management controls to ensure secure, controlled modifications to information systems in accordance with ISO/IEC 27001:2022 Control A.8.32.

**Scope**: This policy applies to all changes to information processing systems, applications, infrastructure, network equipment, and supporting systems regardless of deployment model (on-premises, cloud, hybrid). All change types (hardware, software, configuration, infrastructure, data, process, documentation) and all environments (development, test, staging, production, disaster recovery) are covered.

**Purpose**: Define organisational requirements for change management control implementation and governance. This policy establishes WHAT change management is required and WHO is accountable. Implementation procedures (HOW changes are executed) are documented separately in ISMS-IMP-A.8.32 assessment workbooks. Templates, tools, and quick reference guides are provided in ISMS-REF-A.8.32 (non-ISMS technical reference).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022 Control 8.32, and conditional sector-specific requirements that apply where [Organisation]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.32

**ISO/IEC 27001:2022 Annex A.8.32 - Change Management**

> *Changes to information processing facilities and information systems should be subject to change management procedures.*

**ISO/IEC 27002:2022 Guidance (Paraphrased)**:

Change management procedures should ensure:

- Changes are planned, assessed for impact, authorised, tested, communicated, implemented, and documented
- Emergency changes have accelerated procedures while maintaining control
- All changes maintain or improve information security
- Risks of changes are understood and mitigated

**Nine Mandatory Elements (ISO/IEC 27002:2022)**:

| Element | Description | Section Reference |
|---------|-------------|-------------------|
| **(a) Planning and impact assessment** | Assess potential impacts before implementation | 2.1 |
| **(b) Authorisation** | Obtain appropriate approvals based on risk/impact | 2.1 |
| **(c) Communication** | Inform stakeholders of changes and impacts | 2.1 |
| **(d) Testing and acceptance** | Verify changes work as intended before deployment | 2.3 |
| **(e) Implementation** | Execute changes in controlled manner | 2.1 |
| **(f) Emergency and contingency** | Handle urgent changes with expedited procedures | 2.4 |
| **(g) Record keeping** | Maintain audit trail of all changes | 2.1 |
| **(h) Documentation updates** | Update operational procedures and runbooks | 2.1 |
| **(i) Continuity plan updates** | Update business continuity plans when infrastructure changes | 2.1 |

## Purpose

This policy establishes [Organisation]'s change management framework ensuring:

**Risk Mitigation**:

- Unauthorised or unplanned changes prevented
- Impact of changes assessed before implementation
- Change failures minimised through proper testing
- Rollback procedures available when changes fail
- System availability maintained during change implementation

**Compliance & Audit**:

- Complete audit trail of all changes
- Demonstration of change control maturity
- Evidence of due diligence in system modifications
- Regulatory compliance verification

**Operational Excellence**:

- Standardized approach to changes
- Clear accountability for change decisions
- Efficient approval workflows based on risk
- Continuous improvement through post-implementation review

## Scope

**This policy applies to:**

**Information Systems** (all systems processing, storing, or transmitting organisational information):

- Production systems (business applications, databases, ERP, CRM, financial systems)
- Infrastructure systems (servers, storage, virtualization, networking equipment)
- Security systems (firewalls, IDS/IPS, SIEM, authentication systems, encryption systems)
- Cloud services (IaaS, PaaS, SaaS - customer-controlled configurations)
- Communication systems (email, collaboration platforms, telephony)
- Development and testing environments (including CI/CD pipelines and deployment automation)
- Office productivity systems (email, collaboration, document management)
- Website and web applications (public-facing and internal)

**Change Types:**

- Hardware changes (server installations, network equipment upgrades, storage expansions)
- Software changes (application updates, OS patches, security updates, new software installations)
- Configuration changes (parameter modifications, rule updates, policy changes)
- Infrastructure changes (network topology, virtualization, cloud resources)
- Data changes (database schema modifications, data migrations, master data updates)
- Process changes (workflow modifications, integration changes, automation updates)
- Documentation changes (operating procedures, configuration documentation, runbooks)

**All Environments:**

- Development (Dev)
- Testing / Quality Assurance (Test/QA)
- Staging / Pre-Production (where applicable)
- Production (Prod)
- Disaster Recovery (DR)
- Transitions between environments (promotion/deployment)

**Out of Scope:**

**Business Process Changes:**

- Organisational restructuring (unless affecting IT systems)
- Business policy changes (unless affecting IT system configurations)
- Human resource changes (hiring, terminations, role changes)
  - *Exception: Changes to system access/privileges follow this framework*

**Content Changes:**

- Website content updates (text, images, marketing materials)
- Document content modifications in content management systems
- Email/communication content
  - *Exception: Changes to website functionality or CMS configuration follow this framework*

**Routine Operations:**

- Daily backups (scheduled, automated)
- Log rotation and archival (automated processes)
- Monitoring alert acknowledgments
- Routine maintenance tasks (pre-approved as standard changes)

**User Activities:**

- User-initiated self-service actions (password resets via approved self-service portal)
- User preference configurations within applications
- Personal file storage and sharing (within approved limits)

**External Service Provider Changes:**

- Changes managed entirely by SaaS providers (behind the scenes)
- Cloud provider infrastructure changes (outside customer control)
  - *Exception: Changes to customer-controlled configurations follow this framework*

**Exclusion Rationale**: These exclusions represent activities that either (1) do not materially affect information security, (2) are managed through separate governance processes, (3) are fully automated with adequate controls, or (4) are outside the organisation's control.

Any changes falling into gray areas SHALL be escalated to the Change Manager for classification.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

[Organisation] MUST comply with change management requirements from applicable regulations. For complete regulatory categorization, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

**Key Principle**: This policy provides technology-agnostic requirements. Organisations determine specific controls through risk assessment considering their operational context, industry, jurisdiction, and regulatory obligations.

## What This Policy Does NOT Do

This policy does NOT:

- **Specify change management tools or platforms** (see ISMS-REF-A.8.32 for tool evaluation criteria)
- **Define step-by-step change procedures** (see ISMS-IMP-A.8.32.1 Change Process Assessment)
- **Provide change request form templates** (see ISMS-REF-A.8.32 for templates)
- **Specify approval authority levels for specific systems** (determined by [Organisation]'s risk assessment)
- **Define standard change catalog entries** (see ISMS-IMP-A.8.32.2 Change Types Assessment)
- **Provide risk assessment matrices** (see ISMS-REF-A.8.32 for risk assessment methodology)
- **Replace technical procedures** (technical implementation in ISMS-IMP documents)
- **Define tool configurations** (tool-specific configurations are implementation details)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving technology and change management best practices
- Technical agility for tool updates, process improvements, and methodology changes without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors verify policy compliance, not tool configurations)
- Adaptability for different organisational contexts, industries, and risk profiles

## Definitions

**Change**: Any addition, modification, or removal of information system components (hardware, software, configuration, data, documentation) that could affect information security or system availability.

**Change Advisory Board (CAB)**: Multi-disciplinary group providing expert review, impact assessment, and recommendations for normal and emergency changes. May be standing committee or ad-hoc assembly.

**Change Manager**: Individual accountable for change management process, CAB coordination, metrics tracking, and continuous improvement.

**Change Request**: Formal record documenting proposed change including description, justification, impact assessment, implementation plan, testing approach, and rollback procedure.

**Emergency Change**: Change requiring expedited implementation to resolve critical incident, security vulnerability, or prevent significant business impact. Emergency changes follow accelerated approval but maintain control rigor.

**Normal Change**: Change requiring full assessment, CAB review, and standard approval workflow due to moderate or high risk/impact.

**Post-Implementation Review (PIR)**: Structured review after change implementation verifying objectives achieved, identifying lessons learned, and capturing improvement opportunities.

**Production Environment**: Live operational systems directly supporting business operations and accessible to end users.

**Rollback**: Procedure to reverse change and return system to previous working state if change fails or causes unexpected issues.

**Standard Change**: Pre-approved, low-risk, routine change following documented procedure from Standard Change Catalog. May be implemented without CAB review.

**Test Environment**: Non-production environment isolated from production where changes are validated before production deployment.

---

# Change Management Requirements

This section defines change management requirements organised into three domains:

1. **Change Process Requirements** (2.1): Core workflow from initiation through closure
2. **Change Classification Requirements** (2.2): Standard, normal, and emergency change types
3. **Emergency Change Requirements** (2.3): Expedited procedures for urgent situations

## Change Process Requirements

**Purpose**: Define core change management process covering complete change lifecycle from initiation through closure. These requirements implement ISO/IEC 27002:2022 Control 8.32 elements (a), (b), (c), (e), (g), (h), and (i).

### Change Request Submission

**REQ-PROCESS-001: Change Request Documentation**

[Organisation] SHALL require all in-scope changes to be submitted as formal change requests in the change management system.

**Rationale**: Formal change requests provide audit trail, enable proper assessment, prevent undocumented "shadow changes", and create single source of truth.

**Minimum Required Information**:

- Unique change identifier
- Change description and scope
- Business justification
- Systems/components affected
- Implementation date/window
- Requestor and implementer identification
- Impact assessment (availability, confidentiality, integrity)
- Risk classification
- Rollback procedure
- Testing approach
- Dependencies on other changes
- Communication plan

**Assessment Criteria**: ISMS-IMP-A.8.32.1 (Change Process Assessment) verifies change request forms capture required information and change management system maintains complete records.

**Exceptions**: Pre-approved standard changes may use simplified submission but SHALL still create change request record.

---

### Planning & Impact Assessment

**REQ-PROCESS-002: Impact Assessment**

[Organisation] SHALL require impact assessment for all changes evaluating:

- Technical impact (systems affected, dependencies, integration points)
- Business impact (services affected, user impact, business operations disruption)
- Security impact (confidentiality, integrity, availability risks)
- Compliance impact (regulatory obligations, audit controls)
- Risk level (likelihood of failure × magnitude of impact)

**Rationale**: Understanding change impact before implementation prevents surprises, enables appropriate approval levels, and supports informed decision-making.

**Assessment Criteria**: Change requests demonstrate documented impact assessment. High-risk changes show detailed analysis.

---

**REQ-PROCESS-003: Implementation Planning**

[Organisation] SHALL require implementation plans for normal and emergency changes including:

- Step-by-step procedure
- Resource requirements (personnel, tools, access)
- Implementation timeframe
- Dependencies and prerequisites
- Verification steps
- Rollback triggers and procedure
- Communication checkpoints

**Rationale**: Detailed planning reduces implementation failures, enables smooth execution, and provides clear guidance for implementers.

**Assessment Criteria**: Change requests include implementation plans. Complex changes demonstrate detailed planning.

---

### Authorisation & Approval

**REQ-PROCESS-004: Approval Workflows**

[Organisation] SHALL define approval authority based on change risk level:

| Risk Level | Approval Authority | CAB Review | Documentation Level |
|------------|-------------------|------------|---------------------|
| **Low** | Standard Change (pre-approved) | Not required | Standard Change Catalog |
| **Medium** | Service Owner / Team Lead | Recommended | Standard |
| **High** | IT Operations Manager / CISO | Required | Comprehensive |
| **Critical** | Executive Management | Required | Comprehensive + Risk Acceptance |

**Implementation**: Approval authority matrix is documented in ISMS-IMP-A.8.32.1 (Change Process Assessment) identifying specific roles/positions with approval authority for each risk level. Matrix SHALL be reviewed and approved by CISO annually and updated within 30 days of organisational changes affecting approval authorities.

**Assessment Criteria**: ISMS-IMP-A.8.32.1 contains current approval authority matrix with named roles. Evidence shows approvals obtained from designated authorities per matrix. Annual review records demonstrate matrix accuracy.

**Rationale**: Risk-based approvals balance control with efficiency. Low-risk changes move quickly; high-risk changes get appropriate oversight.

---

**REQ-PROCESS-005: Change Advisory Board (CAB)**

[Organisation] SHALL establish Change Advisory Board (CAB) for review of normal and emergency changes.

**CAB Responsibilities:**

- Review change requests for completeness and risk assessment accuracy
- Identify potential conflicts between scheduled changes
- Assess impact on dependent systems
- Recommend approval, deferral, or rejection
- Review emergency changes (retrospectively for time-critical emergencies)

**CAB Composition** (minimum):

- Change Manager (chair)
- IT Operations representative
- Security representative
- Business application owners (for relevant changes)
- Additional subject matter experts (as needed)

**Quorum Requirements**: CAB meetings require minimum attendance of (1) Change Manager (chair), (2) IT Operations representative, (3) Security representative, and (4) at least one additional CAB member. Emergency CAB meetings MAY proceed with reduced quorum (Change Manager + one additional member) if time-critical, with full CAB retrospective review required within 48 hours.

**Evidence of Operation**: CAB operation is verified through: (1) meeting minutes for all scheduled and emergency meetings with date, attendees, changes reviewed, decisions, rationale, and action items, (2) attendance records showing quorum requirements met, (3) change request records showing CAB review notes and recommendations, (4) annual CAB charter review. CAB meeting minutes are retained for minimum 3 years and accessible in change management system/document repository.

**CAB Frequency**: 

- Regular meetings (weekly recommended for active change environments)
- Emergency CAB meetings (as needed for urgent changes)
- Virtual CAB review (for time-sensitive changes between meetings)

**Rationale**: Multi-disciplinary review prevents single points of failure in change assessment, identifies risks implementers may miss, and provides governance oversight.

**Assessment Criteria**: CAB charter documented. Meeting minutes demonstrate regular operation. Change requests show CAB review notes.

### Communication

**REQ-PROCESS-006: Stakeholder Communication**

[Organisation] SHALL communicate changes to affected stakeholders including:

- Change schedule and timing
- Expected service impact (duration, scope)
- User actions required (if any)
- Contact information for support
- Rollback decision and communication

**Communication Timing:**

- **Planned Changes**: Minimum advance notification per [Organisation]'s operational requirements
- **Emergency Changes**: Communication as soon as safely possible
- **Change Completion**: Confirmation to stakeholders when change complete

**Communication Channels**: Email, service portal notifications, collaboration platforms, or other methods appropriate to [Organisation]'s operations.

**Rationale**: Advance notification enables users to plan around service impacts, reduces support burden, and demonstrates transparency.

**Assessment Criteria**: Change records show stakeholder notifications sent. Communication templates documented in ISMS-REF-A.8.32.

---

### Implementation Execution

**REQ-PROCESS-007: Controlled Implementation**

[Organisation] SHALL implement changes following approved implementation plan with:

- Verification of prerequisites and dependencies
- Execution of documented steps
- Real-time monitoring during implementation
- Verification testing post-implementation
- Documentation of actual steps performed

**Implementation Windows:**
[Organisation] SHOULD establish preferred change windows (e.g., maintenance windows) to minimise business disruption while balancing operational needs.

**Rationale**: Controlled execution reduces errors, enables troubleshooting if issues arise, and creates audit trail of actual work performed.

**Assessment Criteria**: Change records document implementation steps. Verification test results recorded.

---

**REQ-PROCESS-008: Rollback Execution**

[Organisation] SHALL execute rollback procedure when:

- Change fails to achieve objectives
- Unacceptable performance degradation occurs
- Security vulnerability introduced
- Critical business function impaired
- Rollback triggers (defined in change request) are met

**Rollback Decision Authority**: Same approval authority as original change (or higher for emergency rollback).

**Rationale**: Quick rollback capability minimises impact of failed changes, maintains system availability, and prevents prolonged incidents.

**Assessment Criteria**: Failed changes show documented rollback decisions and execution.

---

### Record Keeping & Audit Trail

**REQ-PROCESS-009: Change Records**

[Organisation] SHALL maintain complete change records including:

- All change request information (per REQ-PROCESS-001)
- Approval records with timestamps and approvers
- CAB review notes and recommendations
- Implementation logs and verification results
- Communication records
- Incidents or issues during implementation
- Rollback decisions and execution (if applicable)
- Post-implementation review results

**Record Retention**: Minimum [Organisation-defined] period (recommended: 7 years for audit, 3 years for operational reference).

**Rationale**: Complete records enable audit verification, incident investigation, trend analysis, and regulatory compliance demonstration.

**Assessment Criteria**: ISMS-IMP-A.8.32.1 (Change Process Assessment) verifies record completeness. Sample audits show records available.

---

### Documentation Updates

**REQ-PROCESS-010: Operational Documentation Updates**

[Organisation] SHALL update operational documentation following changes:

- System configuration documentation
- Network diagrams and topology
- Application architecture documents
- Operational procedures and runbooks
- Troubleshooting guides
- Disaster recovery procedures
- User documentation (where applicable)

**Update Timing**: Within [Organisation-defined] timeframe (recommended: 5 business days for non-emergency changes).

**Rationale**: Accurate documentation enables effective operations, supports troubleshooting, and provides knowledge continuity when personnel change.

**Assessment Criteria**: Change records reference documentation updates. Sample review shows documentation current.

---

**REQ-PROCESS-011: Continuity Plan Updates**

[Organisation] SHALL review and update business continuity plans when changes affect:

- Critical business systems or applications
- Infrastructure supporting business continuity
- Disaster recovery procedures
- Recovery time objectives (RTO) or recovery point objectives (RPO)
- Backup and restoration procedures

**Review Trigger**: All changes to in-scope systems SHALL trigger continuity plan review assessment.

**Rationale**: Business continuity plans must reflect current system configurations to ensure effective recovery during incidents.

**Assessment Criteria**: Changes to critical systems show continuity plan review. Updates documented where impact identified.

---

### Post-Implementation Review

**REQ-PROCESS-012: Post-Implementation Review (PIR)**

[Organisation] SHALL conduct post-implementation review for:

- All emergency changes (mandatory)
- All failed changes (mandatory)
- Normal changes above [Organisation-defined] risk threshold
- Standard changes when patterns suggest review needed

**PIR Content:**

- Objectives achieved vs. planned outcomes
- Implementation issues encountered
- Effectiveness of planning and execution
- User feedback and service impact
- Lessons learned and improvement opportunities

**PIR Timing**: Within [Organisation-defined] period (recommended: 7 business days for emergency changes, 14 days for normal changes).

**Rationale**: Structured review drives continuous improvement, captures lessons learned, identifies process gaps, and recognizes successful practices.

**Assessment Criteria**: ISMS-IMP-A.8.32.1 shows PIR completion rates. PIR records demonstrate learning and improvement actions.

---

## Change Classification Requirements

**Purpose**: Define requirements for classifying changes into three categories (Standard, Normal, Emergency). Classification determines approval workflow, testing requirements, and documentation rigor.

### Standard Change Requirements

**REQ-CLASSIFY-001: Standard Change Catalog**

[Organisation] SHALL maintain Standard Change Catalog containing pre-approved, low-risk changes that:

- Have well-understood impacts and outcomes
- Follow documented, repeatable procedures
- Have low risk of failure
- Have defined rollback procedures (if needed)

**Standard Change Catalog SHALL include:**

- Change description and scope
- Pre-conditions and prerequisites
- Step-by-step procedure
- Estimated duration
- Rollback procedure
- Risk assessment (completed once during catalog approval)

**Implementation**: Standard Change Catalog is maintained in change management system/document repository and accessible to all authorised change implementers. Catalog is reviewed quarterly by Change Manager with CAB input. Current catalog version is documented in ISMS-IMP-A.8.32.2 (Change Types & Categories Assessment).

**Catalog Version Control**: Maintain version history of Standard Change Catalog documenting: (1) version number and date, (2) changes made (additions, removals, modifications), (3) reason for changes, (4) approver. Previous versions retained per organisational retention policy.

**Assessment Criteria**: ISMS-IMP-A.8.32.2 contains current Standard Change Catalog with all required elements. Quarterly review records demonstrate catalog maintenance. Change tickets reference catalog entries for standard changes.

**Rationale**: Standard changes streamline low-risk activities, reduce CAB burden, enable faster implementation while maintaining control.

---

**REQ-CLASSIFY-002: Standard Change Execution**

Standard changes SHALL:

- Be logged in change management system (no CAB approval required)
- Follow documented procedure from Standard Change Catalog
- Be executed by authorised personnel
- Include post-execution verification

Standard changes MAY be self-service where appropriate (e.g., password resets via approved portal).

**Rationale**: Even pre-approved changes need tracking for audit trail and incident correlation.

**Assessment Criteria**: Change tickets demonstrate standard changes are logged. Execution follows catalog procedures.

---

**REQ-CLASSIFY-003: Standard Change Review**

[Organisation] SHALL review Standard Change Catalog:

- Quarterly (minimum)
- After any standard change failure
- When usage patterns suggest reclassification needed

**Review Criteria:**

- Success rate remains high (>95% recommended)
- No significant incidents caused by standard change
- Procedure remains accurate and complete

**Catalog Updates**: Add new standard changes from successful normal changes. Remove or reclassify standard changes with failure patterns.

**Rationale**: Regular review ensures catalog remains accurate and standard changes truly are low-risk.

**Assessment Criteria**: Catalog review records show quarterly reviews. Failed standard changes trigger reclassification.

---

### Normal Change Requirements

**REQ-CLASSIFY-004: Normal Change Process**

Normal changes SHALL follow full change management process including:

- Formal change request with impact assessment
- Risk assessment and classification
- CAB review and recommendation
- Approval by appropriate authority (per REQ-PROCESS-004)
- Testing in non-production environment (per Section 2.3)
- Stakeholder communication
- Scheduled implementation
- Post-implementation verification
- Post-implementation review (for high-risk changes)

**Rationale**: Full process provides appropriate control for moderate and high-risk changes.

**Assessment Criteria**: Sample normal change requests show complete process followed.

---

**REQ-CLASSIFY-005: Change Risk Assessment**

[Organisation] SHALL assess normal change risk using [Organisation-defined] methodology considering:

- **Impact**: Scope of systems/users affected, business criticality, data sensitivity
- **Likelihood**: Complexity, novelty, implementer experience, testing completeness
- **Risk Level**: Combination of impact and likelihood

**Risk Assessment Output**: Low / Medium / High / Critical classification determining approval authority and rigor level.

**Rationale**: Risk-based assessment enables appropriate oversight. Low-risk changes move quickly; high-risk changes get scrutiny.

**Assessment Criteria**: ISMS-REF-A.8.32 provides risk assessment methodology. Change requests show documented risk assessments.

---

### Change Calendar & Scheduling

**REQ-CLASSIFY-006: Change Calendar**

[Organisation] SHALL maintain change calendar identifying:

- Scheduled changes (date, time, systems affected)
- Change freeze periods (no non-emergency changes)
- Blackout windows (business-critical periods)
- Conflicts between changes (overlapping impacts)

**Change Freeze Periods** (examples):

- Year-end financial close
- Major product launches
- Peak business seasons
- Major regulatory submission periods

**Rationale**: Change calendar prevents conflicts, protects critical business periods, and enables coordination across teams.

**Assessment Criteria**: Change calendar maintained and accessible. Evidence shows change freeze periods respected.

---

## Testing & Validation Requirements

**Purpose**: Define requirements for environment separation and comprehensive testing before production deployment. These requirements implement ISO/IEC 27002:2022 Control 8.32 element (d) and integrate with Controls 8.29 (Security Testing), 8.31 (Environment Separation), and 8.33 (Test Data Protection).

### Environment Separation Requirements

**REQ-TEST-001: Non-Production Environments**

[Organisation] SHALL maintain separate non-production environments for change testing:

- **Development Environment**: For building and unit testing changes
- **Test/QA Environment**: For integration testing and user acceptance testing
- **Staging/Pre-Production Environment** (optional but recommended): For final validation before production

**Environment Isolation Requirements:**

- Logical or physical separation from production
- Separate credentials and access controls
- No direct production data access from non-production
- Clear marking/identification of non-production systems

**Rationale**: Separated environments enable safe testing without production impact, prevent test failures from affecting operations, and protect production data.

**Assessment Criteria**: ISMS-IMP-A.8.32.3 (Environment Separation Assessment) documents environment architecture. Evidence shows logical/physical separation maintained.

---

**REQ-TEST-002: Environment Promotion Workflow**

[Organisation] SHALL implement controlled promotion workflow:

- **Dev → Test**: Code complete, unit tests passed
- **Test → Staging**: Integration tests passed, UAT complete
- **Staging → Production**: Final validation complete, approvals obtained

**Promotion Controls:**

- Formal sign-off at each stage
- Verification testing at each environment
- Documentation of promotion steps
- Rollback capability at each stage

**Rationale**: Controlled promotion prevents untested changes from reaching production, provides multiple validation checkpoints, and maintains change control rigor.

**Assessment Criteria**: Promotion procedures documented. Sample changes show progression through environments.

---

**REQ-TEST-003: Production Environment Protection**

[Organisation] SHALL restrict production changes to:

- Authorised change implementers only
- Changes with completed testing (except approved emergency changes)
- Scheduled change windows (except emergencies)
- Changes with proper approvals

**Production Access Controls:**

- Privileged access management for production changes
- Multi-factor authentication for production access
- Audit logging of all production changes
- Separation of duties (developers do not deploy to production)

**Rationale**: Production protection prevents unauthorised changes, ensures only tested changes reach production, and creates accountability for production modifications.

**Assessment Criteria**: Production access controls documented. Access logs show restricted access. Separation of duties maintained.

---

### Testing Requirements

**REQ-TEST-004: Testing Procedures**

[Organisation] SHALL require testing appropriate to change risk:

| Change Risk | Required Testing |
|-------------|------------------|
| **Low** | Implementer verification testing |
| **Medium** | Functional testing, integration testing |
| **High** | Comprehensive testing: functional, integration, performance, UAT |
| **Critical** | Full testing suite: functional, integration, performance, security, UAT, disaster recovery |

**Minimum Testing Requirements (all changes):**

- Functional testing (change achieves intended purpose)
- Integration testing (change does not break dependent systems)
- Rollback testing (rollback procedure verified)

**Enforcement**: Change management system enforces testing requirements by requiring test result documentation before approval workflow proceeds to production deployment stage. High and critical-risk changes cannot be approved for production deployment without documented evidence of: (1) test plan completion, (2) acceptance criteria met, (3) test results sign-off by designated approver. Testing enforcement is verified through change request audit trail in change management system.

**Rationale**: Risk-appropriate testing balances thorough validation with implementation speed.

**Assessment Criteria**: Change requests show testing performed and results documented. Audit trail demonstrates enforcement of testing gates.

---

**REQ-TEST-005: Security Testing Integration**

[Organisation] SHALL incorporate security testing for changes that:

- Affect authentication or authorisation mechanisms
- Modify security controls or configurations
- Expose new external interfaces
- Process restricted or confidential data
- Affect cryptographic implementations

**Security Testing Types:**

- Vulnerability scanning (automated)
- Security configuration review
- Penetration testing (for high-risk changes to external interfaces)
- Code security review (for application changes)

**Integration with Control 8.29**: Security testing requirements align with ISMS-POL-A.8.25-26-29 (Secure Development Lifecycle).

**Rationale**: Security testing prevents introduction of vulnerabilities, validates security control effectiveness, and supports defense-in-depth.

**Assessment Criteria**: Security-relevant changes show security testing performed. Integration with secure development lifecycle demonstrated.

---

**REQ-TEST-006: Acceptance Criteria**

[Organisation] SHALL define acceptance criteria for changes including:

- Functional requirements met
- Performance requirements met (no unacceptable degradation)
- Integration points validated
- Security requirements validated
- No critical or high-severity defects
- User acceptance obtained (where applicable)

**Acceptance Sign-Off**: Required before production deployment for medium and high-risk changes.

**Rationale**: Clear acceptance criteria prevent subjective "looks good" assessments, ensure changes truly ready for production, and document formal acceptance.

**Assessment Criteria**: Change requests define acceptance criteria. Test results show criteria met. Sign-offs documented.

---

### Test Data Management

**REQ-TEST-007: Production Data Protection**

[Organisation] SHALL protect production data in test environments:

- Production data SHALL NOT be used in test environments without protection
- If production data required for testing, data SHALL be masked/anonymized per ISMS-POL-A.8.11 (Data Masking)
- Synthetic test data SHOULD be used where feasible
- Test data SHALL be classified and protected per ISMS-POL-A.5.12 (Classification of Information)

**Integration with Control 8.33**: Test data requirements align with ISO/IEC 27001:2022 Control 8.33 (Test Information).

**Rationale**: Unprotected production data in test environments creates data breach risk, regulatory non-compliance risk, and unauthorised access risk.

**Assessment Criteria**: Test environments show data masking/anonymization or synthetic data. No unprotected production data in test.

---

## Emergency Change Requirements

**Purpose**: Define requirements for expedited handling of urgent changes while maintaining control and oversight. These requirements implement ISO/IEC 27002:2022 Control 8.32 element (f).

### Emergency Change Criteria

**REQ-EMERGENCY-001: Emergency Classification**

[Organisation] SHALL classify changes as emergency only when:

- Resolving active security incident or vulnerability
- Restoring critical service outage
- Preventing imminent system failure
- Addressing urgent regulatory requirement
- Mitigating active data breach

**Emergency changes SHALL NOT be used for:**

- Convenience or schedule pressure
- Poor planning
- Routine work
- Desired features

**Rationale**: Emergency designation enables expedited process but requires strong justification. Overuse of emergency changes indicates process failure.

**Assessment Criteria**: Emergency change requests demonstrate valid justification. Emergency change percentage tracked (target: <5% of all changes).

---

**REQ-EMERGENCY-005: Emergency Change Threshold Management**

[Organisation] SHALL monitor emergency change percentage monthly. When emergency changes exceed target threshold (<5% of all changes) for two consecutive months, Change Manager SHALL:

- Conduct root cause analysis identifying systemic issues
- Present findings to CAB with remediation recommendations
- Implement corrective actions within 30 days
- Report threshold exceedance and remediation plan to CISO

**Assessment Criteria**: Monthly emergency change percentage tracked in assessment workbooks' Summary Dashboard sheets (ISMS-IMP-A.8.32.1-4). Evidence shows root cause analysis and corrective actions when threshold exceeded.

---

### Emergency Change Approval

**REQ-EMERGENCY-002: Expedited Approval**

Emergency changes SHALL obtain approval from:

- IT Operations Manager or CISO (minimum)
- Additional approvals as feasible given time constraints
- Retrospective CAB review within [Organisation-defined] period (recommended: 24-48 hours)

**Approval Documentation:**

- Emergency justification
- Assessed risk and impact
- Alternative options considered
- Risk acceptance decision

**Rationale**: Expedited approval enables rapid response while maintaining executive oversight and accountability.

**Assessment Criteria**: Emergency changes show appropriate approvals. Retrospective CAB reviews documented.

---

### Emergency Change Testing

**REQ-EMERGENCY-003: Risk-Appropriate Testing**

Emergency changes SHALL undergo testing appropriate to time constraints:

- **Minimum**: Implementer verification in isolated environment (where possible)
- **Preferred**: Limited testing in test environment
- **If no testing possible**: Documented risk acceptance and rollback plan

**Testing Shortcuts Permitted (documented and justified):**

- Abbreviated test cases
- Testing in production with monitoring
- Parallel deployment with fallback
- Testing limited to critical functionality

**Rationale**: Balances urgency with control. Some testing better than no testing. Risk acceptance explicit when testing not feasible.

**Assessment Criteria**: Emergency changes document testing performed or risk acceptance for testing shortcuts.

---

### Post-Emergency Review

**REQ-EMERGENCY-004: Mandatory Post-Implementation Review**

[Organisation] SHALL conduct post-implementation review for ALL emergency changes within [Organisation-defined] period (recommended: 5 business days) addressing:

- Emergency justification validated
- Alternative approaches available
- Change effectiveness
- Process improvements to prevent future emergencies
- Whether change should be added to Standard Change Catalog

**Review Participants**: Change Manager, CISO, CAB members, implementers.

**Rationale**: Emergency changes often indicate process gaps. Structured review drives improvement and prevents recurring emergencies.

**Assessment Criteria**: All emergency changes have PIR completed within timeframe. PIR records show learning and improvement actions.

---

### Timeframe Specifications

**REQ-PROCESS-013: Organisation-Defined Timeframes**

[Organisation] SHALL document specific timeframes for change management activities in ISMS-IMP-A.8.32.1 (Change Process Assessment) based on operational requirements and risk assessment. Required timeframe specifications:

| Activity | Recommended Default | Reference |
|----------|---------------------|-----------|
| Documentation updates following changes | 5 business days | REQ-PROCESS-010 |
| Continuity plan review trigger | Within change approval process | REQ-PROCESS-011 |
| Post-implementation review (normal changes) | 14 business days | REQ-PROCESS-012 |
| Post-implementation review (emergency changes) | 5 business days | REQ-EMERGENCY-004 |
| Emergency CAB retrospective review | 24-48 hours | REQ-EMERGENCY-002 |
| Stakeholder communication advance notice | Per operational requirements | REQ-PROCESS-006 |
| Change record retention | 7 years (audit), 3 years (operational) | REQ-PROCESS-009 |

Timeframes SHALL be reviewed annually during policy review and updated to reflect operational realities.

---

# Roles & Responsibilities

[Organisation] SHALL define clear accountability for change management using RACI matrix (Responsible, Accountable, Consulted, Informed).

## Key Roles

**Change Manager**:

- **Accountable** for change management process
- Chairs Change Advisory Board (CAB)
- Maintains Standard Change Catalog
- Tracks change metrics and trends
- Drives continuous improvement

**Change Advisory Board (CAB)**:

- Reviews and recommends on normal and emergency changes
- Identifies conflicts between changes
- Assesses risks and impacts
- Multi-disciplinary membership (IT Ops, Security, Business, SMEs)

**Change Requestor**:

- Submits change requests with complete information
- Obtains business justification and sponsorship
- Participates in impact assessment

**Change Implementer**:

- Executes approved changes following documented procedures
- Verifies prerequisites and dependencies
- Performs post-implementation verification
- Documents implementation steps and issues

**System Owner**:

- Reviews changes to owned systems
- Provides impact assessment for owned systems
- Approves changes per approval authority matrix
- Accountable for system availability and security

**CISO / Information Security**:

- Reviews security-relevant changes
- Provides security risk assessment
- Approves high-risk changes
- Monitors change-related security incidents

**IT Operations Manager**:

- Approves medium and high-risk changes
- Chairs emergency CAB meetings
- Coordinates change windows
- Resolves conflicts and escalations

**Executive Management**:

- Approves critical-risk changes
- Provides strategic direction for change management
- Receives change metrics and risk reporting

## RACI Matrix

[Detailed RACI matrix defining responsibilities for each change management activity across all roles - see ISMS-IMP-A.8.32.1 for complete matrix]

---

# Policy Governance

## Policy Ownership

**Policy Owner**: Chief Information Security Officer (CISO)

**Responsibilities**:

- Overall accountability for change management policy framework
- Approve policy updates and versions
- Ensure policy alignment with ISO/IEC 27001:2022 requirements
- Report policy effectiveness to executive management
- Authorise policy exceptions

## Policy Lifecycle

### Policy Review Schedule

**Annual Review** (mandatory):

- Comprehensive review of policy
- Timing: Q4 of each year (recommended)
- Led by: Change Manager
- Participants: CAB, Security Team, IT Operations, Legal/Compliance

**Triggered Reviews**:

- ISO/IEC 27001 standard updates affecting Control 8.32
- Significant regulatory changes
- Major organisational changes
- Technology changes (new change management tools)
- Major change management incidents or failures
- Audit findings requiring policy updates

### Policy Update Process

**Standard Policy Changes:**
1. Change Request to Policy Owner (CISO)
2. Impact Assessment (affected stakeholders, systems, processes)
3. Stakeholder Consultation (Change Manager, IT Operations, CAB, Legal)
4. Draft Revision
5. Review Period (14 days)
6. Approval (required approvers sign off)
7. Communication (policy updates communicated to all personnel)
8. Implementation (30-day transition period unless urgent)

**Emergency Policy Changes:**

- Abbreviated review period (3-5 business days)
- Emergency approval by CISO with executive notification
- Immediate implementation
- Retrospective stakeholder review within 30 days

## Exception Management

### When Exceptions Are Appropriate

**Valid Exception Scenarios:**

- Technical constraints prevent full compliance
- Business circumstances require temporary deviation
- Alternative compensating controls provide equivalent protection
- Emergency situations (formalized via emergency change process)

**Exceptions NOT Appropriate:**

- Convenience or preference
- Resource constraints
- Disagreement with policy intent
- "We've always done it this way"

### Exception Request Process

**Exception Request SHALL include:**

- Requirement being excepted
- Business or technical justification
- Duration of exception
- Compensating controls (if any)
- Residual risk assessment
- Exception owner and approver

**Exception Approval Authority:**

- Standard requirement exceptions: Change Manager
- Critical requirement exceptions: CISO
- All exceptions: Risk accepted by System Owner

**Exception Review**: All exceptions reviewed quarterly. Expired exceptions require renewal or remediation.

## Compliance Monitoring

**Compliance Metrics** (tracked via Summary Dashboard sheets in assessment workbooks ISMS-IMP-A.8.32.1-4):

- Change success rate
- Emergency change percentage
- PIR completion rate
- Standard change catalog utilization
- Change-related incidents
- Average change duration
- CAB meeting frequency and attendance

**Compliance Reporting**:

- Quarterly Summary Dashboard to CISO
- Annual compliance summary to Executive Management
- Audit findings tracking and remediation

## Integration with ISMS

**Change management integrates with related ISO 27001 controls:**

- **A.5.30** (ICT Continuity): Continuity plans updated after infrastructure changes
- **A.5.37** (Documented Procedures): Operational docs updated after changes
- **A.8.19** (Software Installation): Software deployment controls
- **A.8.29** (Security Testing): Security testing before deployment
- **A.8.31** (Environment Separation): Dev/Test/Prod isolation
- **A.8.33** (Test Information): Production data protection in test

**Information Flows:**

- **Change → Incident**: Failed changes trigger incident response
- **Change → Asset**: Changes update asset inventory
- **Change → Continuity**: Infrastructure changes update continuity plans
- **Change → Documentation**: Changes update system documentation

---

# Integration & Resources

## Integration with Related Controls

Change management (A.8.32) integrates with six related ISO 27001 controls:

**Control 5.30 - ICT Continuity Planning**:

- Continuity plans updated when infrastructure changes affect RTO/RPO
- Change management considers continuity impact
- DR procedures updated after relevant changes

**Control 5.37 - Documented Operating Procedures**:

- Operational procedures updated following system changes
- Runbooks and troubleshooting guides maintained current
- Documentation updates tracked in change records

**Control 8.19 - Installation of Software on Operational Systems**:

- Software installation follows change management process
- Installation controls enforced through change approval
- Software changes subject to testing requirements

**Control 8.29 - Security Testing in Development and Acceptance**:

- Security testing integrated into change testing procedures
- Security-relevant changes undergo additional validation
- Security test results required for acceptance

**Control 8.31 - Separation of Development, Testing, and Production**:

- Environment separation enforced through change promotion workflow
- Production environment protected from unauthorised changes
- Testing performed in non-production environments

**Control 8.33 - Test Information**:

- Production data protected in test environments
- Test data requirements enforced through change process
- Data masking/anonymization validated before testing

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.32 Suite):

[Organisation] implements change management controls using structured assessment workbooks:

- **ISMS-IMP-A.8.32.1-UG/TG**: Change Process Assessment (process maturity, tools, workflows, approvals, documentation)
- **ISMS-IMP-A.8.32.2-UG/TG**: Change Types & Categories Assessment (standard change catalog, normal change workflows, risk classification)
- **ISMS-IMP-A.8.32.3-UG/TG**: Environment Separation Assessment (dev/test/prod architecture, promotion workflows, access controls)

**Technical Reference** (non-ISMS):

- **ISMS-REF-A.8.32**: Change Management Reference (tool requirements, form templates, risk assessment methodology, quick reference guide)

**Assessment Tools**:

- Python-generated Excel workbooks with automated compliance calculations
- Data validation dropdowns (Yes/No/Partial/Planned/N/A response values)
- KPI calculations and gap analysis
- Evidence registers and remediation tracking
- Executive dashboard with trend analysis

**Automation**: All assessment workbooks generated via Python scripts to ensure consistency, repeatability, and maintainability.

## Training & Awareness

**General Awareness** (all personnel):

- Annual training module on change management
- User responsibilities during changes
- How to request changes
- Recognizing unauthorised changes

**Technical Training** (change implementers):

- Change management process and tools training
- Standard Change Catalog procedures
- Testing requirements and verification
- Rollback procedure execution

**CAB Training** (CAB members):

- CAB responsibilities and authority
- Impact assessment techniques
- Risk classification methodology
- Conflict identification

**Management Training** (approval authorities):

- Approval authority responsibilities
- Risk acceptance decisions
- Exception management
- Metrics interpretation

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **IT Operations Manager** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (CEO)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for change management. Implementation procedures, templates, tools, and quick reference guides are documented in ISMS-IMP-A.8.32 (assessment workbooks) and ISMS-REF-A.8.32 (technical reference).*

<!-- QA_VERIFIED: 2026-03-01 -->