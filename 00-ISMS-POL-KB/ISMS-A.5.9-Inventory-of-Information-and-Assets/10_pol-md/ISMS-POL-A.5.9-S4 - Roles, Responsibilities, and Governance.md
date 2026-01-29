# ISMS-POL-A.5.9-S4
## Inventory of Information and Assets - Roles, Responsibilities, and Governance

**Document ID**: ISMS-POL-A.5.9-S4  
**Title**: Inventory of Information and Assets - Roles, Responsibilities, and Governance  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial roles and governance document |

**Review Cycle**: Annual (aligned with ISMS policy review cycle)  
**Next Review Date**: 10.01.2027  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Executive Sponsor: Chief Information Officer (CIO)
- Governance Review: ISMS Steering Committee
- Legal Review: Legal/Compliance Officer

**Distribution**: All management levels, ISMS stakeholders, audit team  
**Related Documents**: ISMS-POL-A.5.9 (Master), ISMS-POL-A.5.9-S2 (Requirements)

---

## 4.1 Roles and Responsibilities

### 4.1.1 Executive Roles

#### Chief Information Security Officer (CISO)

**Accountability**: Overall accountability for asset inventory framework effectiveness and ISO 27001:2022 A.5.9 compliance.

**Responsibilities**:
- Approve asset inventory policy framework
- Allocate resources (budget, personnel, tools)
- Review quarterly compliance dashboards
- Approve exceptions to policy requirements
- Accept residual risks related to inventory gaps
- Escalate significant gaps to executive management
- Champion asset inventory program across organization
- Ensure integration with broader ISMS

**Authority**:
- Approve/reject policy changes
- Approve/reject major exceptions
- Direct remediation activities
- Engage executive management for resource needs

**Accountability Principle**: CISO cannot delegate accountability. If asset inventory fails, CISO is answerable to executive management and Board.

---

#### Chief Information Officer (CIO) / IT Director

**Accountability**: Technology infrastructure and tooling to support asset inventory.

**Responsibilities**:
- Provide IT infrastructure for inventory system
- Support integration with CMDB, discovery tools, HR system
- Allocate IT resources for inventory maintenance
- Ensure custodians have necessary tools and access
- Support automation and efficiency improvements
- Coordinate with CISO on technology decisions

**Authority**:
- Approve IT infrastructure investments
- Assign IT personnel to inventory support roles
- Prioritize inventory system enhancements

**Collaboration**: CIO and CISO collaborate as partners. CIO provides "how" (technology), CISO provides "what" and "why" (requirements).

---

#### Business Unit Leaders / Department Heads

**Accountability**: Asset identification and owner assignment within their areas.

**Responsibilities**:
- Identify information and associated assets in their business units
- Assign appropriate asset owners
- Ensure owners acknowledge responsibilities
- Support owners in fulfilling their duties
- Review asset inventory for their area quarterly
- Attest to inventory completeness annually
- Provide resources for asset management activities
- Escalate inventory issues to CISO

**Authority**:
- Assign owners within their organizational scope
- Approve asset classification decisions
- Approve acceptable use determinations
- Provide business context for security decisions

---

#### Executive Management / Board

**Accountability**: Strategic oversight and risk acceptance.

**Responsibilities**:
- Approve asset inventory policy framework (initial)
- Review annual compliance summary
- Accept residual risks for documented gaps
- Provide strategic direction on priorities
- Ensure adequate resources allocated
- Hold CISO accountable for program effectiveness

**Authority**:
- Final approval on major policy changes
- Final acceptance of significant risks
- Resource allocation decisions

---

### 4.1.2 Asset Owner Role (Detailed)

**Definition**: Individual or group with approved accountability for an asset throughout its lifecycle.

**Selection Criteria**:
- **Business Alignment**: Typically business role for information assets
- **Authority**: Must have decision-making authority over asset use
- **Availability**: Must be able to fulfill responsibilities
- **Accountability Acceptance**: Must explicitly acknowledge accountability

**Core Responsibilities** (ISO 27002:2022 Section 5.9):

**a) Inventorying**
- Ensure asset is added to inventory upon acquisition/creation
- Verify inventory record accuracy during reviews
- Update inventory when asset changes
- Remove asset from inventory upon disposal

**b) Classification and Protection**
- Determine appropriate classification level (per A.5.12)
- Ensure security controls match classification
- Approve control implementations
- Verify controls are operating effectively

**c) Periodic Review**
- Review asset attributes per required schedule (quarterly/semi-annually/annually)
- Attest to accuracy of inventory record
- Update any changed information
- Document review completion

**d) Component Tracking**
- For technology assets: identify dependencies and components
- Maintain linkages between assets (e.g., database → application → server)
- Update component relationships when changes occur

**e) Acceptable Use Definition**
- Define who may use the asset (per A.5.10)
- Define how the asset may be used
- Define prohibited uses
- Communicate use requirements to users

**f) Access Control**
- Approve access requests to asset
- Review access rights periodically (quarterly minimum for critical, annually for others)
- Revoke access when no longer needed
- Ensure access restrictions match classification

**g) Secure Disposal**
- Approve disposal requests (per A.8.10)
- Verify disposal method appropriate for classification
- Confirm disposal was completed
- Verify removal from inventory

**h) Risk Management**
- Participate in risk assessments involving asset
- Identify threats and vulnerabilities
- Approve risk treatment decisions
- Accept residual risks (with CISO approval for high risks)

**i) User Support**
- Provide business context to custodians/administrators
- Answer questions about asset purpose and use
- Resolve access disputes
- Support incident investigations

**Additional Owner Responsibilities**:
- **Delegation**: May delegate tasks to custodians but retains accountability
- **Communication**: Keep stakeholders informed of asset status changes
- **Compliance**: Ensure asset complies with applicable regulations
- **Budget**: Justify budget needs for asset protection
- **Succession**: Ensure smooth ownership transition when leaving role

**Owner Authority**:
- Approve access to asset
- Approve changes to asset
- Approve asset disposal
- Define acceptable use
- Accept risks (with appropriate escalation)

**What Owner CANNOT Delegate**:
- Accountability (owner remains answerable)
- Final approval authority (for access, changes, disposal)
- Risk acceptance (for risks within their authority level)

---

### 4.1.3 Asset Custodian Role

**Definition**: Individual or group with delegated day-to-day responsibility for implementing and maintaining security controls, acting under owner's authority.

**Typical Custodians**:
- Database Administrators (for databases)
- System Administrators (for servers, infrastructure)
- Application Administrators (for applications)
- Network Engineers (for network infrastructure)
- Facilities Managers (for physical assets)

**Responsibilities**:
- Implement security controls per owner's direction
- Perform day-to-day asset management (backups, monitoring, updates)
- Apply patches and configuration changes (per change management)
- Monitor asset health and security status
- Respond to security alerts and events
- Maintain technical documentation
- Notify owner of significant issues
- Execute owner-approved changes
- Support access provisioning (after owner approval)
- Provide technical input to owner decisions

**Authority**:
- Implement technical controls within approved scope
- Execute approved changes
- Respond to operational issues
- Escalate to owner when policy decisions needed

**Accountability**: Custodian is accountable to owner for proper execution of delegated tasks. Custodian is NOT accountable to executive management for asset protection (that remains with owner).

**Owner-Custodian Relationship**:
- Owner provides direction, custodian executes
- Owner makes decisions, custodian implements
- Owner accepts risks, custodian mitigates
- Owner is business-focused, custodian is technically-focused
- Clear communication essential

---

### 4.1.4 Information Security Team

**Roles**: Information Security Manager, Security Engineers, Security Analysts, Compliance Officers

**Responsibilities**:
- **Policy Ownership**: Maintain asset inventory policy framework
- **Framework Oversight**: Ensure framework operates effectively
- **Tool Management**: Administer inventory system/tools
- **Assessment Coordination**: Coordinate quarterly assessments
- **Compliance Monitoring**: Track compliance metrics
- **Gap Management**: Identify and track gaps
- **Remediation Support**: Support gap remediation efforts
- **Training**: Develop and deliver asset inventory training
- **Reporting**: Generate compliance dashboards and reports
- **Audit Support**: Coordinate audit activities
- **Integration**: Ensure integration with ISMS processes
- **Continuous Improvement**: Drive improvement initiatives

**Authority**:
- Interpret policy requirements
- Request evidence from owners/custodians
- Escalate non-compliance to CISO
- Recommend policy improvements
- Coordinate with auditors

---

### 4.1.5 IT Asset Management Team

**Roles**: Asset Managers, CMDB Administrators, Discovery Tool Administrators

**Responsibilities**:
- **Tool Operation**: Operate inventory system/CMDB
- **Discovery**: Execute automated discovery scans
- **Data Quality**: Maintain data quality and accuracy
- **Reconciliation**: Reconcile inventory with discovery/CMDB
- **Integration**: Maintain system integrations
- **Reporting**: Generate operational reports
- **User Support**: Support owners/custodians with technical issues
- **Training**: Provide tool training
- **Process Improvement**: Optimize inventory processes

**Authority**:
- Manage inventory system operations
- Execute discovery scans
- Coordinate reconciliation activities
- Recommend process improvements

**Coordination**: Works closely with Information Security Team. Asset Management provides operational execution, Security Team provides governance and compliance oversight.

---

### 4.1.6 Internal Audit

**Responsibilities**:
- **Independent Verification**: Verify inventory completeness and accuracy independently
- **Compliance Assessment**: Assess compliance with policy framework
- **Control Testing**: Test effectiveness of inventory controls
- **Risk Assessment**: Identify risks related to inventory gaps
- **Recommendations**: Provide recommendations for improvement
- **Follow-Up**: Verify remediation of findings

**Authority**:
- Request evidence from any party
- Access all inventory systems and records
- Report findings to CISO, Audit Committee, Board
- Escalate significant issues

**Independence**: Internal Audit maintains independence from implementation teams to provide objective assessment.

---

### 4.1.7 Supporting Roles

**Legal / Data Protection Officer**:
- Interpret regulatory requirements affecting inventory
- Review inventory practices for privacy compliance
- Advise on data retention requirements
- Support incident investigations

**Human Resources**:
- Provide personnel data for personnel asset inventory
- Support owner assignment for departing personnel
- Coordinate return of assets upon termination (per A.5.11)

**Procurement**:
- Notify Asset Management of new asset purchases
- Provide purchase records for reconciliation
- Support license management

**Compliance Team**:
- Track regulatory requirements
- Coordinate with external auditors
- Monitor compliance with inventory obligations

---

## 4.2 RACI Matrix

### 4.2.1 Policy Framework Activities

| Activity | CISO | CIO | Business Leaders | Asset Owners | Custodians | Security Team | Asset Mgmt | Audit |
|----------|------|-----|------------------|--------------|------------|---------------|------------|-------|
| **Policy Approval** | A | C | C | I | I | R | I | I |
| **Policy Maintenance** | A | I | C | I | I | R | C | C |
| **Framework Oversight** | A | C | I | I | I | R | C | C |
| **Resource Allocation** | A/R | A/R | C | I | I | C | C | I |

**Legend**: R = Responsible (does the work), A = Accountable (answerable for completion), C = Consulted (provides input), I = Informed (kept updated)

---

### 4.2.2 Inventory Management Activities

| Activity | Asset Owners | Custodians | Security Team | Asset Mgmt | Business Leaders | Audit |
|----------|--------------|------------|---------------|------------|------------------|-------|
| **Asset Identification** | A/R | C | C | C | C | I |
| **Inventory Data Entry** | A | R | C | R | I | I |
| **Owner Assignment** | - | I | C | C | A/R | I |
| **Owner Acknowledgment** | A/R | I | C | C | C | I |
| **Attribute Accuracy** | A | R | C | C | I | I |
| **Periodic Review** | A/R | C | C | C | I | I |
| **Classification Determination** | A/R | C | C | I | C | I |
| **Access Approval** | A/R | I | I | I | I | I |
| **Disposal Approval** | A/R | R | C | C | I | I |

---

### 4.2.3 Assessment and Compliance Activities

| Activity | Security Team | Asset Mgmt | Asset Owners | CISO | Audit |
|----------|---------------|------------|--------------|------|-------|
| **Assessment Coordination** | A/R | R | C | I | C |
| **Completeness Verification** | A/R | R | I | I | C |
| **Accuracy Verification** | A/R | C | C | I | R |
| **Gap Identification** | A/R | C | I | I | C |
| **Compliance Reporting** | A/R | C | I | A | C |
| **Dashboard Generation** | R | C | I | A | I |
| **Audit Support** | R | R | C | A | A |
| **Remediation Tracking** | A/R | C | R | A | C |

---

## 4.3 Policy Governance

### 4.3.1 Policy Ownership

**Policy Owner**: Chief Information Security Officer (CISO)

**Responsibilities**:
- Maintain policy framework
- Ensure policy remains current and effective
- Approve policy changes
- Communicate policy to stakeholders
- Monitor policy compliance
- Report policy effectiveness to executive management

**Delegation**: CISO may delegate policy maintenance activities to Information Security Manager but retains accountability.

---

### 4.3.2 Policy Lifecycle

**Policy Stages**:

**1. Creation** (Initial Development)
- Needs identified (regulatory requirement, audit finding, risk assessment)
- Policy drafted by Security Team
- Stakeholder review and feedback
- CISO approval
- Executive management approval (for initial framework)
- Publication and communication

**2. Active** (In Effect)
- Policy enforced
- Compliance monitored
- Training delivered
- Exceptions managed
- Feedback collected

**3. Review** (Periodic Assessment)
- Annual review minimum
- Effectiveness assessment
- Stakeholder feedback incorporation
- Update needs identified

**4. Update** (Revision)
- Updates drafted
- Stakeholder review
- Approval (CISO for minor, Executive for major)
- Communication of changes
- Training updates

**5. Retirement** (Superseded or Obsolete)
- Archive previous version
- Maintain for historical reference
- Update all references

---

### 4.3.3 Policy Review Process

**Review Frequency**: Annual minimum, or triggered by:
- Significant organizational changes (merger, acquisition, restructuring)
- Regulatory changes
- Audit findings requiring policy updates
- Major incidents revealing policy gaps
- Technology evolution (new asset types)
- Effectiveness metrics below target

**Review Process**:
1. **Initiation**: CISO or Security Team initiates review
2. **Data Collection**: Gather compliance metrics, feedback, incidents, audit findings
3. **Assessment**: Evaluate policy effectiveness and relevance
4. **Stakeholder Input**: Collect feedback from owners, custodians, business leaders
5. **Gap Analysis**: Identify policy gaps or areas for improvement
6. **Recommendations**: Document proposed changes
7. **Review**: CISO reviews recommendations
8. **Approval**: Approve changes (or escalate to Executive Management if major)
9. **Communication**: Announce changes to stakeholders
10. **Implementation**: Update documentation, training, tools

**Review Evidence**:
- Review meeting notes
- Stakeholder feedback
- Metrics analysis
- Proposed changes
- Approval documentation

---

### 4.3.4 Policy Communication

**Initial Communication** (New Policy):
- Executive announcement from CISO
- All-hands briefing (or town halls)
- Email to all affected stakeholders
- Intranet publication
- Training sessions scheduled

**Ongoing Communication** (Policy in Effect):
- Policy included in new employee onboarding
- Annual refresher training
- Policy accessible via intranet/knowledge base
- Reference in relevant procedures
- Mention in management meetings

**Change Communication** (Updates):
- Change summary email to stakeholders
- "What changed and why" briefing
- Updated training materials
- Highlighted changes in documentation
- Q&A sessions for significant changes

---

### 4.3.5 Exception Management

**Exception Definition**: Approved deviation from policy requirements.

**Valid Exception Scenarios**:
- Temporary gap during transition (e.g., owner vacancy)
- Technical impossibility (e.g., vendor system limitations)
- Business criticality (e.g., urgent business need)
- Cost-benefit (e.g., disproportionate cost for low-risk asset)

**Exception Request Process**:
1. **Request**: Requester submits exception request with justification
2. **Risk Assessment**: Security Team assesses risk of deviation
3. **Compensating Controls**: Identify alternative controls if feasible
4. **Recommendation**: Security Team recommends approve/deny
5. **Decision**: CISO approves/denies (escalate to Executive for high-risk exceptions)
6. **Documentation**: Document exception, risk, compensating controls, duration
7. **Tracking**: Add to exception register
8. **Review**: Review exceptions quarterly

**Exception Documentation**:
- Exception ID
- Description of deviation
- Justification (why needed)
- Risk assessment
- Compensating controls
- Duration (time-limited)
- Approval authority and date
- Review schedule

**Exception Expiration**:
- All exceptions are time-limited (maximum 1 year)
- Renewal requires re-assessment and re-approval
- Exceptions automatically expire unless renewed
- Long-term exceptions indicate policy problem (fix policy)

---

### 4.3.6 Non-Compliance Management

**Non-Compliance Definition**: Failure to meet policy requirements without approved exception.

**Detection**:
- Quarterly compliance assessments
- Automated monitoring alerts
- Audit findings
- Incident investigations
- User reports

**Response**:
1. **Identification**: Non-compliance identified and documented
2. **Notification**: Owner/responsible party notified
3. **Root Cause**: Determine why non-compliance occurred
4. **Remediation Plan**: Develop plan with timeline
5. **Tracking**: Track remediation progress
6. **Verification**: Verify compliance restored
7. **Follow-Up**: Address root cause to prevent recurrence

**Escalation**:
- Minor non-compliance: Security Team manages
- Repeated non-compliance: Escalate to CISO
- Significant non-compliance: Escalate to Executive Management
- Willful non-compliance: HR/disciplinary action

---

## 4.4 Training and Awareness

### 4.4.1 Training Requirements

**Asset Owner Training** (Mandatory):
- Owner responsibilities (ISO 27002:2022 a-i)
- Inventory system usage
- Classification guidance
- Access approval process
- Review procedures
- Exception process
- **Frequency**: Upon assignment, annual refresher
- **Duration**: 2 hours initial, 1 hour refresher
- **Assessment**: Quiz to verify understanding

**Asset Custodian Training** (Mandatory):
- Custodian responsibilities
- Inventory system usage (technical)
- Update procedures
- Discovery tool operation
- Integration maintenance
- **Frequency**: Upon assignment, annual refresher
- **Duration**: 3 hours initial, 1.5 hours refresher
- **Format**: Hands-on workshop

**General Awareness** (All Personnel):
- Asset inventory purpose and importance
- User responsibilities
- How to report unidentified assets
- **Frequency**: Annual (part of security awareness)
- **Duration**: 15 minutes
- **Format**: E-learning module

---

### 4.4.2 Training Delivery

**Methods**:
- Instructor-led workshops (for owners, custodians)
- E-learning modules (for general awareness)
- Documentation (reference materials)
- Job aids (quick reference guides)
- On-demand videos (for asynchronous learning)

**Responsibility**: Information Security Team develops content, HR coordinates delivery

---

### 4.4.3 Training Effectiveness

**Measurement**:
- Training completion rates
- Assessment scores
- Post-training compliance metrics
- Owner/custodian feedback

**Target**: 
- ≥95% completion rate
- ≥85% average assessment score
- ≥80% satisfaction score

---

## 4.5 Continuous Improvement

### 4.5.1 Improvement Cycle

**Quarterly**:
- Review compliance metrics
- Analyze gap trends
- Assess remediation progress
- Identify process improvements

**Annually**:
- Comprehensive policy review
- Training effectiveness assessment
- Tool adequacy evaluation
- User satisfaction survey

**Ad-Hoc**:
- Post-incident reviews
- Audit finding remediation
- Technology change assessment

---

### 4.5.2 Improvement Sources

**Internal**:
- Compliance metrics trends
- User feedback
- Operational efficiency analysis
- Cost-benefit analysis

**External**:
- Audit recommendations
- Regulatory changes
- Industry best practices
- Peer benchmarking

---

### 4.5.3 Improvement Implementation

**Process**:
1. **Identify**: Improvement opportunity identified
2. **Assess**: Evaluate feasibility, cost, benefit
3. **Plan**: Develop implementation plan
4. **Approve**: CISO approves investment
5. **Implement**: Execute improvement
6. **Measure**: Assess effectiveness
7. **Sustain**: Maintain improvement

**Examples**:
- Automation of manual processes
- Enhanced discovery capabilities
- Improved user interface
- Streamlined workflows
- Better reporting
- Reduced compliance burden

---

## 4.6 Document Change History

| Version | Date | Section | Change Description | Approver |
|---------|------|---------|-------------------|----------|
| 1.0 | [Date] | All | Initial document creation | CISO |
| | | | | |
| | | | | |

**Future Changes**: All changes documented in this section with date, section affected, description, and approver.

---

**END OF SECTION 4 (S4)**

**Previous Document**: ISMS-POL-A.5.9-S3 - Implementation and Assessment  
**Framework Complete**: All policy documents (Master + S1-S4) delivered

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**This document establishes clear roles, responsibilities, and governance framework, enabling [Organization] to effectively implement and maintain Control A.5.9 with appropriate accountability and oversight.** 🎯

---

## Phase 1 Policy Framework: COMPLETE ✅

**Policy Documents Delivered**:
1. ✅ ISMS-POL-A.5.9.md - Master Framework (748 lines)
2. ✅ ISMS-POL-A.5.9-S1 - Purpose, Scope, Definitions (provided)
3. ✅ ISMS-POL-A.5.9-S2 - Requirements Framework (800 lines)
4. ✅ ISMS-POL-A.5.9-S3 - Implementation & Assessment (867 lines)
5. ✅ ISMS-POL-A.5.9-S4 - Roles, Responsibilities, Governance (THIS DOCUMENT)

**Total Policy Framework**: 5 comprehensive documents ready for implementation

**Next Phase**: Implementation Guidance (IMP-1, IMP-2, IMP-3) - recommend new chat for fresh token budget