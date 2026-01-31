# ISMS-POL-A.8.32-S3
## Change Management - Roles and Responsibilities

**Document ID**: ISMS-POL-A.8.32-S3  
**Title**: Change Management - Roles and Responsibilities  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Change Manager / HR / CISO | Initial roles document |

**Review Cycle**: Annual or upon organizational changes  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: CISO, Change Manager, HR/People Operations  
**Distribution**: All IT staff, CAB members, management  
**Related Documents**: ISMS-POL-A.8.32 (Master), Job descriptions, Organizational charts

---

## 3.1 Purpose

This document defines roles and responsibilities for change management activities, establishing clear accountability, authority, and consultation requirements. All personnel involved in change management SHALL understand their roles and responsibilities.

---

## 3.2 Role Definitions

### 3.2.1 Change Requester / Change Owner

**Purpose:** Individual or team proposing the change.

**Responsibilities:**
- Submit complete change request with required information
- Provide business justification for change
- Conduct initial impact and risk assessment
- Coordinate with technical teams for implementation planning
- Communicate change status to stakeholders
- Ensure change documentation is complete
- Participate in post-implementation review

**Authority:**
- Request changes
- Withdraw change requests
- Recommend implementation timing

**Qualifications:**
- Understands business need driving change
- Has authority to commit resources (or has sponsor who does)
- Understands affected systems/processes

**Reporting:** Reports to functional manager; coordinates with Change Manager for change lifecycle

---

### 3.2.2 Change Manager

**Purpose:** Orchestrates change management process, ensures compliance, facilitates CAB.

**Responsibilities:**
- Overall change management process governance
- Chair Change Advisory Board meetings
- Validate change classification (standard/normal/emergency)
- Coordinate change scheduling and conflict resolution
- Monitor change management metrics and KPIs
- Report to management on change activity
- Maintain standard change catalog
- Ensure change documentation completeness
- Drive continuous improvement of change processes
- Escalate issues to CISO or IT Operations Manager

**Authority:**
- Approve low-risk standard changes
- Reject inappropriately classified changes
- Prioritize change scheduling
- Call emergency CAB meetings
- Enforce change management procedures

**Qualifications:**
- Strong understanding of IT infrastructure and applications
- Experience with ITSM tools and processes
- Excellent organizational and communication skills
- ITIL Foundation or equivalent (recommended)

**Reporting:** Reports to IT Operations Manager or CISO (organization-dependent)

---

### 3.2.3 Change Advisory Board (CAB)

**Purpose:** Multi-stakeholder body reviewing and approving normal changes.

**Core Membership:**
- Change Manager (chair)
- Infrastructure representative (network, servers, storage)
- Application representative (application teams)
- Security representative (InfoSec team)
- Business representative (service owners, business analysts)

**Optional Members (as needed):**
- Database administrator
- Cloud platform specialist
- Vendor representatives
- External consultants

**Collective Responsibilities:**
- Review normal changes for technical feasibility
- Assess business impact and timing appropriateness
- Evaluate risk and approve/defer/reject changes
- Identify dependencies and conflicts
- Ensure resource availability
- Provide diverse perspectives on change implications

**Authority:**
- Approve medium-risk normal changes
- Recommend high/critical risk changes to senior management
- Defer changes requiring additional information
- Reject changes with unacceptable risk

**Meeting Frequency:** Weekly (minimum), additional meetings as needed

**Qualifications (members):**
- Deep knowledge in their respective domains
- Authority to make decisions for their areas
- Availability to attend meetings regularly

---

### 3.2.4 Emergency CAB (E-CAB)

**Purpose:** Rapid decision-making for emergency changes outside normal CAB cycle.

**Core Membership (24/7 availability required):**
- Change Manager or delegate
- Senior Technical Authority (infrastructure or applications)
- Information Security representative

**Responsibilities:**
- Rapid review and approval of emergency changes
- Balance urgency with risk assessment
- Ensure emergency process not abused
- Participate in post-implementation reviews

**Authority:**
- Approve emergency changes
- Authorize testing bypasses with documented justification
- Escalate to CISO or executive management for major incidents

**On-Call Requirements:**
- 24/7 availability via on-call rotation
- 15-minute response time to emergency change requests
- Authority to make immediate decisions

---

### 3.2.5 Change Implementer

**Purpose:** Technical personnel executing approved changes.

**Responsibilities:**
- Implement changes according to approved implementation plan
- Follow documented procedures and security controls
- Document implementation progress in change ticket
- Monitor system during implementation
- Perform verification testing post-implementation
- Execute rollback if issues occur
- Update documentation after successful implementation
- Participate in post-implementation review

**Authority:**
- Execute approved changes during approved change window
- Recommend rollback if issues encountered
- Request change deferral if prerequisites not met

**Qualifications:**
- Technical competence in relevant technology
- Authorized access to target systems
- Training on change procedures
- Understanding of rollback procedures

**Reporting:** Reports to technical team lead; coordinates with Change Manager

---

### 3.2.6 Technical Reviewer / Subject Matter Expert

**Purpose:** Provide technical expertise for change impact assessment.

**Responsibilities:**
- Review change requests in area of expertise
- Assess technical feasibility and risks
- Identify dependencies and potential issues
- Recommend implementation approaches
- Review implementation plans
- Participate in CAB as domain expert

**Authority:**
- Recommend change approval/deferral/rejection
- Require additional testing or documentation
- Escalate high-risk changes for senior review

**Qualifications:**
- Deep technical expertise in specific domain
- Experience with similar changes
- Understanding of system architectures and dependencies

---

### 3.2.7 Security Reviewer

**Purpose:** Assess and approve security implications of changes.

**Responsibilities:**
- Review all changes for security impact
- Conduct or coordinate security testing per Control 8.29
- Ensure changes don't introduce vulnerabilities
- Verify security controls maintained after changes
- Approve security aspects of changes before production
- Participate in CAB for security perspective
- Review emergency changes retrospectively

**Authority:**
- Require additional security testing
- Block changes with unacceptable security risk
- Require remediation before production deployment
- Escalate to CISO for high-risk changes

**Qualifications:**
- Security engineering or architecture expertise
- Understanding of threat landscape and vulnerabilities
- Experience with security testing methodologies

**Reporting:** Reports to CISO; coordinates with Change Manager

---

### 3.2.8 Business Approver / Service Owner

**Purpose:** Approve changes from business perspective.

**Responsibilities:**
- Provide business justification for changes
- Approve User Acceptance Testing results
- Authorize changes affecting business services
- Communicate changes to business users
- Participate in CAB as business representative

**Authority:**
- Approve/reject changes affecting owned services
- Define acceptable implementation timing
- Determine user communication requirements

**Qualifications:**
- Accountability for business service delivery
- Understanding of business impact of changes
- Authority to represent business interests

---

### 3.2.9 Chief Information Security Officer (CISO)

**Purpose:** Executive oversight of change management from security perspective.

**Responsibilities:**
- Policy ownership for change management framework
- Approval of high-risk and critical changes
- Oversight of security aspects in change process
- Exception approval for security-related deviations
- Escalation point for security incidents requiring emergency changes
- Annual review of change management effectiveness

**Authority:**
- Final approval for critical changes
- Policy exceptions and waivers
- Escalation authority for CAB disputes
- Emergency change authorization during security incidents

---

### 3.2.10 IT Operations Manager / CIO

**Purpose:** Executive oversight of operational aspects of change management.

**Responsibilities:**
- Organizational accountability for change management effectiveness
- Approval of high-risk and critical changes
- Resource allocation for change activities
- Escalation point for change conflicts
- Annual change management process review
- Budget approval for change management tools

**Authority:**
- Final approval for critical operational changes
- Override CAB decisions (with documented justification)
- Organizational structure decisions
- Investment decisions for change management capability

---

## 3.3 RACI Matrix

**Key:**  
**R** = Responsible (does the work)  
**A** = Accountable (decision authority, single point)  
**C** = Consulted (input sought)  
**I** = Informed (kept updated)

| Activity | Requester | Change Mgr | CAB | E-CAB | Implementer | Tech Review | Security | Business | CISO | IT Ops Mgr |
|----------|-----------|------------|-----|-------|-------------|-------------|----------|----------|------|------------|
| **Submit change request** | R,A | I | I | - | - | - | - | C | - | - |
| **Classify change** | C | R,A | - | - | - | - | - | - | I | - |
| **Impact assessment** | R | C | - | - | - | C | C | C | - | - |
| **Risk assessment** | R | C | - | - | - | C | C | C | - | - |
| **CAB review (normal)** | C | R,A | R,A | - | - | C | C | C | - | I |
| **Approve standard change** | I | R,A | - | - | - | - | - | - | - | - |
| **Approve medium risk** | I | I | R,A | - | - | - | - | A | - | I |
| **Approve high risk** | I | I | R | - | - | - | - | A | C | A |
| **Approve critical risk** | I | I | R | - | - | - | - | C | A | A |
| **Emergency change review** | C | R | - | R,A | - | C | C | C | I | I |
| **Implement change** | C | I | - | - | R,A | - | - | - | - | - |
| **Security testing** | I | I | - | - | - | - | R,A | - | I | - |
| **UAT approval** | C | I | - | - | - | - | - | R,A | - | - |
| **Production deployment** | I | C | - | - | R,A | - | - | - | - | I |
| **Rollback decision** | I | A | - | - | R | C | C | C | I | I |
| **Communication** | R | A | - | - | - | - | - | C | - | I |
| **Documentation update** | C | C | - | - | R,A | - | - | - | - | - |
| **PIR** | C | R,A | - | - | C | - | - | C | - | I |
| **Process improvement** | C | R,A | C | - | - | - | - | C | I | I |

---

## 3.4 Role Assignment Requirements

**Requirement:** Organizations SHALL:
- Document role assignments with named individuals
- Maintain current role assignment matrix
- Define backup personnel for critical roles (Change Manager, E-CAB)
- Ensure 24/7 coverage for emergency roles (E-CAB members)
- Update role assignments within 5 business days of personnel changes

**Assessment:** Role assignment matrix documented in ISMS-IMP-A.8.32.1

---

## 3.5 Training Requirements

**Requirement:** Personnel SHALL receive training appropriate to their role:

**All IT Staff:**
- Change management process overview
- How to submit change requests
- Standard change catalog usage

**Change Manager:**
- Change management methodology (ITIL recommended)
- ITSM tool administration
- CAB facilitation
- Metrics and reporting

**CAB Members:**
- CAB roles and responsibilities
- Risk assessment techniques
- Change impact evaluation

**Change Implementers:**
- Implementation procedures
- Rollback procedures
- Documentation requirements

**Training frequency:**
- Initial: Upon role assignment
- Refresher: Annual
- Updated: When processes change significantly

**Assessment:** Training records demonstrate completion of required training

---

## 3.6 Segregation of Duties

**Requirement:** Organizations SHALL maintain segregation of duties:

**Not allowed (conflicts of interest):**
- Same person as Change Requester and sole Approver (peer review required)
- Change Implementer also authorizing deployment (independent verification required)
- Audit or compliance team as Change Manager (independence conflict)

**Allowed with documented justification:**
- Small organizations may have overlapping roles if properly documented
- Emergency situations may require combined roles with retrospective review

**Assessment:** Role assignments demonstrate adequate segregation, exceptions documented

---

**END OF SECTION 3**

*"In any organization, the person who controls the change control process effectively controls the organization's IT future. Choose wisely."* 🎯
