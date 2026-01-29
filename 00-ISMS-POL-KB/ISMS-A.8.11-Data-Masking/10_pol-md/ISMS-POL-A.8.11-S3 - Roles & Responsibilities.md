ISMS-POL-A.8.11-S3 — Roles & Responsibilities# ISMS-POL-A.8.11-S3 — Roles & Responsibilities
## ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document ID**: ISMS-POL-A.8.11-S3  
**Title**: Data Masking - Roles & Responsibilities  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Information Security Officer (ISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / HR / Governance Team | Initial section document |

**Review Cycle**: Annual (synchronized with Master Policy review), or upon:
- Organizational restructuring
- Changes to key personnel or role definitions
- Introduction of new data processing activities requiring new roles  

**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Human Resources: HR Director or CHRO
- Privacy/Legal: Data Protection Officer (DPO)
- Final Authority: Executive Management (for accountability assignment)

**Distribution**: All personnel with data handling responsibilities, management, HR  
**Parent Document**: ISMS-POL-A.8.11 - Data Masking Policy (Master)  
**Related Standards**: ISO/IEC 27001:2022 Clause 5.3 (Roles and responsibilities), GDPR Articles 24, 37-39

---

## 1. Purpose

This section defines **WHO is responsible for WHAT** in the data masking control 
framework. Clear role definition prevents the classic "someone else's problem" 
syndrome and ensures accountability.

**What this section covers:**
- Role definitions and responsibilities
- Accountability matrix (RACI model)
- Escalation paths
- Delegation and substitution rules
- Cross-functional coordination requirements

**What this section does NOT cover:**
- Specific individuals (roles, not names — names change, roles persist)
- Organizational chart (this is functional, not hierarchical)
- Job descriptions (this is control-specific responsibilities)

---

## 2. Core Principles

> "For a successful technology, reality must take precedence over public relations, 
> for Nature cannot be fooled."  
*— Richard Feynman (Rogers Commission Report on Challenger Disaster)

**Translation for ISMS:**
- **Assigned ≠ Accountable:** Just because someone is "assigned" doesn't mean they're doing it
- **Title ≠ Competence:** "Data Protection Officer" doesn't automatically mean competent in masking
- **Policy ≠ Implementation:** Having a role defined doesn't mean the role is being executed

**Core Principles:**
1. **Clear Ownership:** Every task has ONE accountable person (no "shared accountability")
2. **Separation of Duties:** No single person controls both masking and validation
3. **Competence Required:** Roles SHALL be filled by personnel with appropriate skills
4. **Documented Delegation:** If primary role-holder unavailable, backup SHALL be designated
5. **No Assumed Responsibility:** If it's not written here, it's not your responsibility

---

## 3. Role Definitions

### 3.1 Chief Information Security Officer (CISO)

**Accountability Level:** Executive (Strategic)

**Primary Responsibilities:**

1. **Policy Approval:**
   - Approve data masking policy and all sections
   - Approve exceptions to masking requirements
   - Approve major changes to masking framework

2. **Resource Allocation:**
   - Ensure adequate budget for masking tools and personnel
   - Approve staffing for masking operations
   - Prioritize masking initiatives

3. **Risk Acceptance:**
   - Accept residual risks from masking exceptions
   - Approve risk treatment plans for masking gaps
   - Review high-severity masking incidents

4. **Strategic Oversight:**
   - Quarterly review of masking effectiveness metrics
   - Annual review of masking framework
   - Ensure alignment with business objectives

**Delegated Authority:**
- May delegate operational decisions to ISO
- May delegate technical decisions to Security Architect
- CANNOT delegate risk acceptance for critical exceptions

**Skills Required:**
- Executive leadership
- Information security management
- Risk management
- Understanding of regulatory requirements (GDPR, HIPAA, etc.)

---

### 3.2 Information Security Officer (ISO)

**Accountability Level:** Management (Tactical)

**Primary Responsibilities:**

1. **Policy Management:**
   - Maintain data masking policy and all sections
   - Propose policy updates based on regulatory/technical changes
   - Coordinate policy reviews with stakeholders

2. **Control Implementation Oversight:**
   - Ensure masking controls implemented per policy
   - Review and approve masking implementation plans
   - Track implementation progress and gaps

3. **Exception Management:**
   - Receive and review exception requests
   - Conduct risk assessments for exceptions
   - Recommend approval/rejection to CISO
   - Maintain exception register

4. **Compliance Monitoring:**
   - Monitor compliance with masking policy
   - Coordinate internal audits of masking controls
   - Track and report KPIs to CISO

5. **Incident Coordination:**
   - Coordinate response to masking failures
   - Conduct root cause analysis
   - Implement corrective actions

**Delegated Authority:**
- Approve low-risk masking exceptions (with CISO notification)
- Approve minor policy updates (procedural, not substantive)
- Initiate emergency masking actions (with CISO notification within 24h)

**Skills Required:**
- Information security management (CISSP, CISM, or equivalent)
- ISO 27001 implementation experience
- Data protection knowledge (GDPR, privacy regulations)
- Risk assessment methodology

**Backup/Deputy:** Security Manager or Senior Security Analyst (designated by CISO)

---

### 3.3 Data Owner

**Accountability Level:** Business (Strategic for their data domain)

**Primary Responsibilities:**

1. **Data Classification:**
   - Classify data under their ownership (PII, confidential, etc.)
   - Identify sensitive fields requiring masking
   - Maintain data classification inventory

2. **Masking Requirements Definition:**
   - Define masking requirements for their data
   - Approve masking techniques for their data
   - Determine acceptable data utility after masking

3. **Access Authorization:**
   - Approve access to unmasked production data (for authorized users)
   - Approve exception requests for their data
   - Review access logs for their data

4. **Business Impact Assessment:**
   - Assess business impact of masking on operations
   - Balance security requirements with business needs
   - Approve data utility validation results

**Example Data Owners (by domain):**
- **HR Director:** Employee data
- **Sales Director:** Customer data
- **Finance Director:** Financial transaction data
- **Marketing Director:** Marketing contact data

**Delegated Authority:**
- May delegate data classification tasks (but retains accountability)
- May delegate access approval (with documented delegation)
- CANNOT delegate exception approval for high-risk data

**Skills Required:**
- Deep understanding of business data in their domain
- Understanding of data protection requirements
- Risk-aware decision making

**Backup/Deputy:** Designated business manager in same functional area

---

### 3.4 System Owner

**Accountability Level:** Technical (Tactical)

**Primary Responsibilities:**

1. **Masking Implementation:**
   - Implement masking controls in their systems
   - Configure masking tools per approved requirements
   - Integrate masking into data flows and processes

2. **Technical Validation:**
   - Validate masking effectiveness in their systems
   - Conduct testing per ISMS-POL-A.8.11-S2.4
   - Document test results and evidence

3. **System Maintenance:**
   - Maintain masking configurations
   - Apply masking tool updates and patches
   - Monitor masking performance

4. **Incident Response:**
   - Respond to masking failures in their systems
   - Implement corrective actions
   - Report incidents to ISO

**Example System Owners:**
- **ERP System Owner:** Masking in ERP databases (production, non-production)
- **CRM System Owner:** Masking in CRM databases
- **Data Warehouse Owner:** Masking in analytics platforms

**Delegated Authority:**
- Implement approved masking configurations
- Execute routine masking operations
- CANNOT approve changes to masking requirements (only Data Owner can)

**Skills Required:**
- System administration for their specific systems
- Understanding of masking techniques and tools
- Database/application security knowledge

**Backup/Deputy:** Secondary system administrator or senior engineer for that system

---

### 3.5 Database Administrator (DBA)

**Accountability Level:** Operational (Execution)

**Primary Responsibilities:**

1. **Masking Execution:**
   - Execute masking scripts and processes
   - Perform data refresh from production to non-production with masking
   - Monitor masking job execution

2. **Technical Implementation:**
   - Configure database-level masking tools (if used)
   - Implement Dynamic Data Masking (DDM) rules
   - Maintain masking scripts and automation

3. **Data Validation:**
   - Validate post-masking data integrity
   - Check referential integrity after masking
   - Verify data format compliance

4. **Performance Monitoring:**
   - Monitor masking performance impact
   - Optimize masking queries and processes
   - Report performance issues

**Delegated Authority:**
- Execute approved masking processes
- Optimize masking performance (without changing masking logic)
- CANNOT approve masking approach or techniques

**Skills Required:**
- Database administration (SQL, Oracle, PostgreSQL, etc.)
- Scripting (Python, PowerShell, etc.)
- Understanding of masking techniques
- Performance tuning

**Backup/Deputy:** Junior DBA or designated senior DBA

---

### 3.6 Security Architect

**Accountability Level:** Technical (Strategic)

**Primary Responsibilities:**

1. **Masking Architecture Design:**
   - Design masking architecture (tools, data flows, checkpoints)
   - Select appropriate masking techniques for use cases
   - Design integration with existing security controls

2. **Technical Standards:**
   - Define technical standards for masking implementations
   - Evaluate masking tools and technologies
   - Recommend best practices

3. **Security Assessment:**
   - Assess re-identification risks
   - Conduct security reviews of masking implementations
   - Validate separation of duties in masking processes

4. **Innovation and Improvement:**
   - Research new masking techniques and tools
   - Propose improvements to masking framework
   - Stay current with industry best practices

**Delegated Authority:**
- Recommend masking tools and techniques
- Approve technical implementation designs
- CANNOT approve business exceptions (only technical feasibility)

**Skills Required:**
- Security architecture experience
- Cryptography and data protection knowledge
- Understanding of privacy regulations
- Knowledge of masking tools and technologies

**Backup/Deputy:** Senior Security Engineer or ISO (for architectural decisions)

---

### 3.7 Application Developer

**Accountability Level:** Operational (Execution)

**Primary Responsibilities:**

1. **Application Integration:**
   - Integrate masking into application code (if applicable)
   - Implement application-level masking logic
   - Ensure masked data compatibility with application functions

2. **Testing:**
   - Test applications with masked data
   - Validate application functionality post-masking
   - Report masking-related application issues

3. **Code Maintenance:**
   - Maintain application masking code
   - Update masking logic per requirement changes
   - Document masking implementations in code

**Delegated Authority:**
- Implement approved masking logic in applications
- CANNOT define masking requirements (only implement)

**Skills Required:**
- Application development (Java, .NET, Python, etc.)
- Understanding of data protection principles
- Testing and debugging

**Backup/Deputy:** Senior developer or team lead

---

### 3.8 Compliance Officer / Data Protection Officer (DPO)

**Accountability Level:** Oversight (Compliance)

**Primary Responsibilities:**

1. **Regulatory Alignment:**
   - Ensure masking controls meet regulatory requirements (GDPR, HIPAA, etc.)
   - Advise on masking requirements for specific regulations
   - Review masking framework for compliance gaps

2. **Privacy Impact Assessments:**
   - Conduct privacy impact assessments for masking implementations
   - Assess re-identification risks from privacy perspective
   - Recommend privacy-enhancing masking techniques

3. **Audit Coordination:**
   - Coordinate external audits related to data masking
   - Provide audit evidence for masking controls
   - Track and remediate audit findings

4. **Training and Awareness:**
   - Develop masking awareness training
   - Communicate regulatory requirements to stakeholders
   - Promote privacy-by-design principles

**Delegated Authority:**
- Recommend compliance-driven masking requirements
- Escalate compliance risks to CISO
- CANNOT override business decisions (only advise)

**Skills Required:**
- Data protection law (GDPR, CCPA, HIPAA, etc.)
- Privacy impact assessment methodology
- Audit and compliance experience

**Backup/Deputy:** Legal Counsel or ISO (for compliance matters)

---

### 3.9 Internal Audit

**Accountability Level:** Independent Assurance

**Primary Responsibilities:**

1. **Audit Planning:**
   - Develop audit plan for data masking controls
   - Define audit scope and objectives
   - Coordinate audit schedule with ISO

2. **Audit Execution:**
   - Conduct independent audits of masking effectiveness
   - Test masking controls per audit program
   - Interview stakeholders and review documentation

3. **Findings and Recommendations:**
   - Document audit findings (gaps, weaknesses)
   - Recommend improvements to masking controls
   - Track remediation of findings

4. **Reporting:**
   - Report audit results to CISO and senior management
   - Provide assurance on masking control effectiveness
   - Escalate critical findings

**Delegated Authority:**
- None (independent function)
- Reports directly to Audit Committee / Board (per ISO 27001)

**Skills Required:**
- IT audit experience (CISA, CIA, or equivalent)
- Understanding of ISO 27001 controls
- Data protection knowledge

**Note:** Internal Audit is INDEPENDENT and does not participate in masking implementation.

---

### 3.10 IT Operations / DevOps

**Accountability Level:** Operational (Execution)

**Primary Responsibilities:**

1. **Environment Management:**
   - Provision and maintain non-production environments
   - Ensure data refresh processes include masking
   - Monitor environment access and usage

2. **Automation:**
   - Automate masking processes (CI/CD integration)
   - Maintain masking scripts in version control
   - Implement infrastructure-as-code for masking

3. **Monitoring:**
   - Monitor masking job execution
   - Alert on masking failures
   - Maintain masking logs

**Delegated Authority:**
- Execute approved masking processes
- Optimize automation (without changing masking logic)

**Skills Required:**
- DevOps / IT operations
- Automation and scripting
- CI/CD pipelines

**Backup/Deputy:** DevOps team lead or senior engineer

---

### 3.11 End Users (Employees, Contractors)

**Accountability Level:** Compliance (Individual)

**Primary Responsibilities:**

1. **Policy Compliance:**
   - Comply with data masking policies
   - Use masked data appropriately
   - Do not attempt to unmask or re-identify data

2. **Reporting:**
   - Report visible sensitive data in masked environments
   - Report masking failures or issues
   - Complete masking awareness training

3. **Appropriate Use:**
   - Use unmasked production data only when authorized
   - Do not share unmasked data inappropriately
   - Follow data handling procedures

**Delegated Authority:**
- None (end users execute, do not decide)

**Skills Required:**
- Basic data protection awareness
- Understanding of organizational data classification

---

## 4. Accountability Matrix (RACI)

**RACI Definitions:**
- **R = Responsible:** Executes the task
- **A = Accountable:** Ultimately answerable (only ONE per task)
- **C = Consulted:** Provides input (two-way communication)
- **I = Informed:** Kept informed (one-way communication)

### 4.1 Policy and Governance

| Task | CISO | ISO | Data Owner | System Owner | Security Architect | Compliance Officer | Internal Audit |
|------|------|-----|------------|--------------|-------------------|-------------------|----------------|
| **Approve masking policy** | A | R | C | I | C | C | I |
| **Maintain masking policy** | I | A/R | C | I | C | C | I |
| **Define masking requirements** | I | C | A/R | C | C | C | I |
| **Approve exceptions** | A | R | C | I | C | C | I |
| **Risk acceptance (exceptions)** | A | R | C | I | C | C | I |
| **Annual policy review** | A | R | C | I | C | C | I |

---

### 4.2 Implementation and Operations

| Task | ISO | Data Owner | System Owner | DBA | App Developer | Security Architect | DevOps |
|------|-----|------------|--------------|-----|---------------|-------------------|--------|
| **Design masking architecture** | C | C | C | I | I | A/R | C |
| **Select masking tools** | C | C | C | C | I | A/R | I |
| **Implement masking (systems)** | I | C | A/R | R | R | C | R |
| **Execute masking (data refresh)** | I | I | C | A/R | I | I | C |
| **Configure DDM rules** | I | C | C | A/R | I | C | I |
| **Automate masking processes** | I | I | C | R | R | C | A/R |
| **Monitor masking jobs** | I | I | C | R | I | I | A/R |

---

### 4.3 Testing and Validation

| Task | ISO | Data Owner | System Owner | DBA | Security Architect | QA Team |
|------|-----|------------|--------------|-----|-------------------|---------|
| **Define test requirements** | A/R | C | C | I | C | C |
| **Execute masking tests** | I | I | R | R | C | A/R |
| **Re-identification testing** | C | C | C | R | A/R | C |
| **Data utility validation** | I | A/R | C | R | C | R |
| **Performance testing** | I | C | R | R | C | A/R |
| **Approve test results** | A | R | C | I | C | I |

---

### 4.4 Monitoring and Incident Response

| Task | ISO | Data Owner | System Owner | DBA | CISO | Compliance Officer |
|------|-----|------------|--------------|-----|------|-------------------|
| **Monitor masking effectiveness** | A/R | I | R | R | I | I |
| **Detect masking failures** | R | I | R | R | I | I |
| **Respond to incidents** | A/R | C | R | R | I | C |
| **Root cause analysis** | A/R | C | R | R | I | C |
| **Implement corrective actions** | R | C | A/R | R | I | C |
| **Report incidents to CISO** | A/R | I | C | C | I | C |

---

### 4.5 Compliance and Audit

| Task | ISO | Compliance Officer | Data Owner | Internal Audit | CISO |
|------|-----|--------------------|------------|----------------|------|
| **Ensure regulatory compliance** | R | A/R | C | I | I |
| **Conduct privacy impact assessment** | C | A/R | C | I | I |
| **Coordinate audits** | R | R | C | A/R | I |
| **Provide audit evidence** | R | R | R | I | I |
| **Remediate audit findings** | A/R | C | C | I | I |
| **Report compliance status** | R | R | C | I | A |

---

## 5. Escalation Paths

### 5.1 Operational Issues
```
End User → System Owner → ISO → CISO
           ↓
         DBA (if database-related)
```

**Examples:**
- Masking job failure
- Performance degradation
- Data format issues

**Escalation Criteria:**
- **L1 (User/DBA):** Resolve within 4 hours or escalate
- **L2 (System Owner):** Resolve within 24 hours or escalate
- **L3 (ISO):** Resolve within 48 hours or escalate to CISO

---

### 5.2 Security Incidents (Masking Failures)
```
Detector → ISO (immediate) → CISO (within 1 hour) → Executive Team (if critical)
            ↓
          Security Architect (for technical response)
            ↓
          System Owner / DBA (for remediation)
```

**Escalation Criteria:**
- **Critical:** Unmasked PII exposed to unauthorized users → CISO within 1 hour
- **High:** Unmasked data in non-production → ISO within 4 hours
- **Medium:** Masking ineffectiveness detected in testing → ISO within 24 hours

---

### 5.3 Exception Requests
```
Requestor → Data Owner → ISO (risk assessment) → CISO (approval)
                                  ↓
                        Compliance Officer (regulatory impact assessment)
```

**Escalation Timeline:**
- **Low-risk exceptions:** ISO approval within 5 business days
- **Medium-risk exceptions:** CISO approval within 10 business days
- **High-risk exceptions:** CISO + Compliance Officer approval within 15 business days

---

## 6. Delegation and Substitution

### 6.1 Delegation Rules

**When primary role-holder is unavailable:**

1. **Designated Backup:**
   - Each critical role SHALL have designated backup
   - Backup SHALL be documented in role assignment matrix
   - Backup SHALL be trained and competent

2. **Delegation Documentation:**
   - Delegation SHALL be documented (email, delegation log)
   - Delegation period SHALL be specified (start/end dates)
   - Delegated authority limits SHALL be clear

3. **Notification:**
   - ISO SHALL be notified of delegations >5 business days
   - CISO SHALL be notified of CISO-level delegations

**Example Delegation:**
```
From: ISO
To: Security Manager
Subject: Delegation of ISO Responsibilities (2025-01-15 to 2025-01-22)

I am delegating my ISO responsibilities to you during my absence.

Delegated Authority:
- Approve low-risk masking exceptions (≤ €5,000 risk value)
- Coordinate routine masking operations
- Respond to masking incidents (severity: Low, Medium)

NOT Delegated:
- Approve high-risk exceptions (escalate to CISO)
- Approve policy changes (defer until my return)
- Accept residual risks (escalate to CISO)

Contact me at [emergency number] for critical issues.
```

---

### 6.2 Emergency Substitution

**In case of unplanned absence (illness, emergency):**

1. **Automatic Backup Activation:**
   - Designated backup assumes responsibilities automatically
   - ISO SHALL be notified within 24 hours
   - CISO SHALL be notified if CISO-level substitution

2. **Limited Authority:**
   - Emergency substitutes have authority only to maintain operations
   - Major decisions deferred until primary returns (unless critical)

---

## 7. Cross-Functional Coordination

### 7.1 Coordination Requirements

**Masking is NOT a siloed activity. Coordination required:**

| Scenario | Coordination Required |
|----------|----------------------|
| **New system deployment** | ISO + System Owner + Security Architect + Data Owner |
| **Data refresh to non-production** | DBA + System Owner + DevOps |
| **Masking tool update** | Security Architect + System Owner + DBA |
| **Exception approval** | Data Owner + ISO + Compliance Officer + CISO |
| **Incident response** | ISO + System Owner + DBA + CISO + Compliance Officer |
| **Audit** | ISO + Compliance Officer + System Owner + Internal Audit |

---

### 7.2 Communication Mechanisms

**Coordination SHALL use:**

1. **Regular Meetings:**
   - **Monthly:** ISO + System Owners (masking operations review)
   - **Quarterly:** CISO + ISO + Compliance Officer (strategic review)
   - **Annual:** All stakeholders (policy review)

2. **Incident Communication:**
   - **Email:** For non-urgent matters
   - **Phone/SMS:** For urgent incidents
   - **Incident Management System:** For tracking

3. **Documentation:**
   - **Shared Repository:** Policy, procedures, test results
   - **Ticketing System:** For tasks and issues
   - **Audit Trail:** All decisions and approvals

---

## 8. Competency Requirements

### 8.1 Training Requirements

**All roles SHALL complete:**

1. **General Awareness (All Employees):**
   - Data protection awareness (annual)
   - Data masking policy overview (annual)
   - Acceptable use of data (annual)

2. **Role-Specific Training:**

| Role | Training Required | Frequency |
|------|------------------|-----------|
| **ISO** | ISO 27001 Lead Implementer, Data Protection | Every 2 years |
| **Data Owner** | Data classification, Business impact assessment | Annually |
| **System Owner** | Masking tools, Security best practices | Annually |
| **DBA** | Masking techniques, Database security | Annually |
| **Security Architect** | Advanced masking techniques, Privacy engineering | Every 2 years |
| **Compliance Officer** | GDPR, HIPAA, Regulatory updates | Annually |

3. **Tool-Specific Training:**
   - Training on specific masking tools deployed
   - Vendor certifications (if required)
   - Hands-on practice with masking processes

---

### 8.2 Competency Assessment

**Competency SHALL be verified:**

1. **Initial Assessment:**
   - Before assigning critical roles
   - Skills test or certification verification

2. **Ongoing Assessment:**
   - Annual performance reviews include masking competency
   - Incident reviews assess competency gaps
   - Training completion tracked

---

## 9. Performance Metrics

### 9.1 Role-Specific KPIs

**Example KPIs per role:**

| Role | KPI | Target |
|------|-----|--------|
| **ISO** | % of environments compliant with masking policy | ≥95% |
| **System Owner** | % of masking tests passed | 100% |
| **DBA** | Data refresh masking completion time | <2 hours (per refresh) |
| **Security Architect** | Re-identification risk score | Low |
| **Compliance Officer** | % of regulatory requirements met | 100% |

---

## 10. Accountability Enforcement

### 10.1 Consequences of Non-Performance

**If role responsibilities not met:**

1. **First Instance:**
   - Discussion with role-holder (understand root cause)
   - Provide additional training/support if needed
   - Document improvement plan

2. **Repeated Non-Performance:**
   - Escalate to role-holder's manager
   - Reassign responsibilities (if competency gap)
   - Formal performance improvement plan

3. **Severe Non-Performance:**
   - Disciplinary action (per HR policy)
   - Removal from role
   - Incident investigation (if security impact)

**Note:** Accountability is not about blame, but ensuring controls function.

---

## 11. Compliance and Audit

### 11.1 Audit Evidence

Auditors SHALL be provided with:

- Role assignment matrix (current)
- RACI matrix for masking tasks
- Delegation log (if applicable)
- Training completion records
- Competency assessment results
- Performance metrics per role

### 11.2 Audit Checklist (Sample)

- [ ] All critical roles assigned to qualified personnel?
- [ ] RACI matrix documented and approved?
- [ ] Backups designated for all critical roles?
- [ ] Role-specific training completed?
- [ ] Competency assessments conducted?
- [ ] Escalation paths documented and tested?
- [ ] Cross-functional coordination mechanisms in place?
- [ ] Performance metrics tracked?

---

## 12. Review and Updates

This section SHALL be reviewed:

- **Annually** as part of policy review cycle
- Upon **organizational changes** (restructuring, new roles)
- Upon **audit findings** related to roles/responsibilities
- Upon **incident reviews** revealing role gaps

---

## 13. References

- **ISMS-POL-A.8.11-S1:** Purpose, Scope, Definitions
- **ISMS-POL-A.8.11-S2.1-2.4:** Technical Requirements (for role responsibilities)
- **ISMS-POL-A.8.11-S4:** Policy Governance
- **ISO/IEC 27001:2022 Control A.8.11**
- **ISO/IEC 27002:2022 Guidance for A.8.11**

---

## Appendix A: Role Assignment Template
```
Data Masking Role Assignment Matrix

Organization: [Your Organization Name]
Last Updated: [Date]
Approved By: [CISO Name and Signature]

| Role | Primary | Backup | Contact | Last Training |
|------|---------|--------|---------|---------------|
| CISO | [Name] | [Name] | [Email/Phone] | [Date] |
| ISO | [Name] | [Name] | [Email/Phone] | [Date] |
| Data Owner (HR) | [Name] | [Name] | [Email/Phone] | [Date] |
| Data Owner (Sales) | [Name] | [Name] | [Email/Phone] | [Date] |
| System Owner (ERP) | [Name] | [Name] | [Email/Phone] | [Date] |
| System Owner (CRM) | [Name] | [Name] | [Email/Phone] | [Date] |
| DBA (Production) | [Name] | [Name] | [Email/Phone] | [Date] |
| DBA (Non-Production) | [Name] | [Name] | [Email/Phone] | [Date] |
| Security Architect | [Name] | [Name] | [Email/Phone] | [Date] |
| Compliance Officer | [Name] | [Name] | [Email/Phone] | [Date] |
| DevOps Lead | [Name] | [Name] | [Email/Phone] | [Date] |

Review Cycle: Quarterly
Next Review: [Date]
```

---

**END OF SECTION S3**