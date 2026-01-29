# ISMS-POL-A.8.31-S2.2
## Environment Separation - Environment Access Control Requirements

**Document ID**: ISMS-POL-A.8.31-S2.2  
**Title**: Environment Access Control Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / IAM Team | Initial access control requirements |

**Review Cycle**: Semi-annual (or upon significant role/responsibility changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager
- HR Review: Human Resources (for role definitions)

**Distribution**: Security team, IT operations, HR, all technical staff  
**Related Documents**: 
- ISMS-POL-A.8.31-S1 (Executive Summary)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISMS-POL-A.8.2-3-5 (Authentication and PAM)
- ISMS-IMP-A.8.31-S2 (Access Control Implementation)

---

## 2.2.1 Purpose and Scope

This section establishes **mandatory access control requirements** for environment separation. These requirements define WHO can access WHICH environments and under what conditions.

**Core Principle**: **Production access is restricted to operations personnel ONLY. Developers access production ONLY via break-glass emergency procedures.**

**In Scope**: Human and non-human access to all environment tiers  
**Primary Stakeholder**: Security Team, IT Operations, HR  
**Implementation Evidence**: ISMS-IMP-A.8.31-S2 (Access Control Assessment)

---

## 2.2.2 Development Environment Access Control

### 2.2.2.1 Developer Access to Development

[Organization] **SHALL** provide developers full access to development environments for their assigned projects:

**Permitted Development Access**:
- **Who**: Software developers, DevOps engineers, QA engineers (for test automation development)
- **Access Level**: Full (create, read, update, delete)
- **Authentication**: SSO (Single Sign-On) required, MFA optional but recommended
- **Authorization**: Role-based (Developer, Senior Developer, DevOps Engineer)
- **Scope**: Development environments only (isolated per project/team)

**Development Access Restrictions**:
- No access to production environments from development accounts
- No access to production credentials or secrets
- No access to other teams' development environments (unless explicitly authorized)
- Development accounts cannot execute production deployment pipelines

**Audit Verification Criteria**:
- ✅ Developer role definitions documented
- ✅ Developer access limited to development environments
- ✅ Access requests approved by development manager
- ✅ Access reviews conducted quarterly

### 2.2.2.2 Non-Developer Access to Development

[Organization] **SHOULD** restrict non-developer access to development environments:

**Limited Development Access**:
- **Security Team**: Read-only access for security assessments and monitoring
- **IT Operations**: Administrative access for infrastructure maintenance
- **Management**: No access (unless technically qualified and approved)

**Audit Verification Criteria**:
- ✅ Non-developer access justified and approved
- ✅ Access limited to specific business need
- ✅ Access reviewed semi-annually

---

## 2.2.3 Testing/QA Environment Access Control

### 2.2.3.1 QA Team Access to Testing

[Organization] **SHALL** provide QA team full access to testing environments:

**Permitted Testing Access**:
- **Who**: QA engineers, test automation engineers, business users (UAT only)
- **Access Level**: Full for QA engineers, limited for business users
- **Authentication**: SSO required, MFA recommended
- **Authorization**: Role-based (QA Engineer, UAT User)

**Testing Access Restrictions**:
- No access to production environments
- No access to production credentials
- UAT users access UAT environment only (not dev or integration test)
- QA access cannot bypass test approval gates

**Audit Verification Criteria**:
- ✅ QA role definitions documented
- ✅ QA access limited to test environments
- ✅ UAT user access time-limited (project duration only)
- ✅ Access reviews conducted quarterly

### 2.2.3.2 Developer Access to Testing

[Organization] **SHOULD** provide developers limited access to testing environments:

**Developer Testing Access**:
- **Access Level**: Read-only OR deployment-only (cannot modify test data directly)
- **Purpose**: Deploy code for testing, view test results, troubleshoot test failures
- **Restriction**: Cannot modify QA test data or bypass test approval processes

**Audit Verification Criteria**:
- ✅ Developer test access is read-only or deployment-only
- ✅ Developers cannot modify test environment configuration without approval
- ✅ Developer actions in test environment logged and auditable

---

## 2.2.4 Staging/Pre-Production Environment Access Control

### 2.2.4.1 Operations Team Access to Staging

[Organization] **SHALL** provide operations team full administrative access to staging environments:

**Permitted Staging Access**:
- **Who**: IT operations engineers, SREs (Site Reliability Engineers), DevOps leads
- **Access Level**: Full administrative (mirrors production access level)
- **Authentication**: SSO + MFA required (production-equivalent)
- **Authorization**: Role-based (Operations Engineer, SRE)

**Staging Access Purpose**:
- Final validation before production deployment
- Production-equivalent testing (performance, security, disaster recovery)
- Training for production procedures

**Audit Verification Criteria**:
- ✅ Operations team access to staging documented
- ✅ Staging access requires MFA (production-equivalent)
- ✅ Access reviews conducted quarterly

### 2.2.4.2 Developer Access to Staging

[Organization] **SHALL** restrict developer access to staging environments:

**Developer Staging Access**:
- **Access Level**: Read-only ONLY (view logs, metrics, dashboards)
- **Purpose**: Troubleshoot issues found in staging before production deployment
- **Restriction**: No write access, no configuration changes, no code deployment (operations responsibility)

**Exception**: Senior developers MAY be granted limited staging access with CISO approval for specific technical reasons (documented and time-limited).

**Audit Verification Criteria**:
- ✅ Developer staging access is read-only
- ✅ Write access exceptions approved by CISO
- ✅ Exception access time-limited and reviewed monthly

---

## 2.2.5 Production Environment Access Control (CRITICAL)

### 2.2.5.1 Operations-Only Production Access

[Organization] **SHALL** restrict production environment access to operations personnel ONLY:

**Permitted Production Access**:
- **Who**: IT operations engineers, SREs, production DBAs, network engineers (operations roles only)
- **Access Level**: Administrative (via PAM system)
- **Authentication**: SSO + MFA + PAM checkout REQUIRED
- **Authorization**: Role-based (Production Operator, Production DBA, Production Network Admin)
- **Session Recording**: All production sessions recorded and retained per compliance requirements

**Production Access Restrictions**:
- **ZERO developer access** to production (except break-glass - see 2.2.5.3)
- **ZERO shared credentials** between production and non-production
- **ZERO service accounts** with production access unless approved and monitored
- Production access requires business justification and approval

**Audit Verification Criteria** (CRITICAL):
- ✅ **Zero developers** with standing production access (measured monthly)
- ✅ Production access via PAM system only (100% compliance)
- ✅ All production sessions recorded and logged
- ✅ Production access reviews conducted monthly (not quarterly)

### 2.2.5.2 Production Read-Only Access

[Organization] **MAY** provide limited read-only production access for specific roles:

**Permitted Read-Only Production Access**:
- **Monitoring/Observability**: View-only access to metrics, logs, dashboards (not system admin)
- **Security Team**: Read-only access for security monitoring and incident investigation
- **Compliance/Audit**: Read-only access for compliance verification
- **Senior Management**: Dashboard/reporting access (no system access)

**Read-Only Restrictions**:
- No configuration changes
- No data modification
- No code deployment
- No credential access
- Logged and audited like full access

**Audit Verification Criteria**:
- ✅ Read-only access documented with business justification
- ✅ Read-only access cannot escalate to write access
- ✅ Access reviews conducted quarterly

### 2.2.5.3 Break-Glass Emergency Access (Developers to Production)

[Organization] **SHALL** implement break-glass procedures allowing temporary developer production access during critical incidents:

**Break-Glass Conditions**:
- Critical production incident (Severity 1) requiring developer expertise
- Operations team unable to resolve issue without developer assistance
- Incident Commander approves developer production access
- Security team notified of break-glass activation

**Break-Glass Access Process**:
1. **Incident Declared**: Incident Commander declares Severity 1 incident
2. **Access Request**: Developer requests break-glass access (documented in incident ticket)
3. **Approval**: Incident Commander + Security Team approve (or CISO if available)
4. **PAM Checkout**: Developer checks out temporary production credentials from PAM vault
5. **Time-Limited**: Access expires after 4 hours (extendable with re-approval)
6. **Session Recording**: All developer production sessions recorded
7. **Post-Incident Review**: Mandatory review of break-glass access within 48 hours

**Break-Glass Access Restrictions**:
- Time-limited (4 hours maximum per checkout)
- Fully logged and recorded
- Requires multi-person approval
- Post-incident review mandatory
- Used ONLY for critical incidents (not convenience)

**Audit Verification Criteria**:
- ✅ Break-glass access policy documented and communicated
- ✅ All break-glass access activations logged
- ✅ Post-incident reviews completed for 100% of break-glass events
- ✅ Break-glass usage trending down over time (indicates improving operations maturity)

---

## 2.2.6 Service Account and Non-Human Identity Access

### 2.2.6.1 Service Account Environment Separation

[Organization] **SHALL** create separate service accounts per environment:

**Service Account Separation Requirements**:
- Production service accounts NEVER used in dev/test environments
- Service accounts named with environment identifier (app-dev-svc, app-prod-svc)
- Service account credentials stored in secret management per environment
- Service accounts cannot cross environment boundaries

**Service Account Access Control**:
- Service accounts follow same access restrictions as human users
- Production service accounts require same rigor as human production access
- Service account credentials rotated per environment rotation schedule
- Service accounts reviewed quarterly for necessity

**Audit Verification Criteria**:
- ✅ Service account inventory per environment
- ✅ No shared service accounts between environments
- ✅ Service account credentials rotated regularly
- ✅ Unused service accounts deactivated

### 2.2.6.2 CI/CD Pipeline Access Control

[Organization] **SHALL** restrict CI/CD pipeline access to authorized deployment processes:

**Pipeline Service Account Access**:
- Deployment pipelines use dedicated service accounts
- Production deployment service account separate from dev/test deployment accounts
- Pipeline service accounts cannot be used interactively (automation only)
- Pipeline access to production requires approval gate (not fully automated for production)

**Pipeline Access Restrictions**:
- Development pipeline CANNOT deploy to production
- Production pipeline requires manual approval by operations team
- Pipeline credentials stored in CI/CD secret management (not in code)
- Pipeline service accounts follow least privilege (deploy only, no admin)

**Audit Verification Criteria**:
- ✅ Pipeline service accounts separate per environment
- ✅ Production deployment requires manual approval
- ✅ Pipeline credentials not in source control
- ✅ Pipeline access logs reviewed monthly

---

## 2.2.7 Access Provisioning and Deprovisioning

### 2.2.7.1 Access Request and Approval Process

[Organization] **SHALL** implement formal access request processes per environment:

**Access Request Requirements**:
- All access requests submitted via access management system (ticketing system, IAM portal)
- Access requests include: environment, access level, business justification, duration
- Approval required before access granted (approver varies by environment)

**Approval Authority**:
- **Development**: Development Manager approves developer access
- **Testing**: QA Manager approves QA access, Development Manager approves developer test access
- **Staging**: IT Operations Manager approves operations access, CISO approves developer read-only access
- **Production**: CISO approves production access (operations personnel only), Incident Commander approves break-glass

**Access Provisioning Timeline**:
- Standard access: Provisioned within 24 hours of approval
- Emergency access: Provisioned within 4 hours (business hours) or immediate (break-glass)
- Access confirmation sent to requester and approver

**Audit Verification Criteria**:
- ✅ All access requests documented and approved
- ✅ Access provisioned only after approval
- ✅ Access confirmations sent to requesters
- ✅ Approval authorities defined per environment

### 2.2.7.2 Access Deprovisioning

[Organization] **SHALL** deprovision access promptly upon role change or termination:

**Deprovisioning Triggers**:
- Employee termination (same day deprovisioning)
- Role change (within 24 hours)
- Contractor end date (automatic deprovisioning)
- Access no longer required (user request or access review)

**Deprovisioning Process**:
- HR notifies IT of terminations/role changes
- IT deactivates accounts in all environments
- Production access deactivated immediately (within 1 hour)
- Non-production access deactivated within 24 hours
- Access removal confirmed to HR and manager

**Audit Verification Criteria**:
- ✅ Terminated users have zero active access (100% compliance)
- ✅ Production access deactivated within 1 hour of termination
- ✅ Deprovisioning completion rate >95% within 24 hours
- ✅ Quarterly audit of orphaned accounts (should be zero)

---

## 2.2.8 Access Review and Recertification

### 2.2.8.1 Regular Access Reviews

[Organization] **SHALL** conduct periodic access reviews to ensure access remains appropriate:

**Access Review Frequency**:
- **Production access**: Monthly (due to high risk)
- **Staging access**: Quarterly
- **Development/Testing access**: Quarterly
- **Service accounts**: Quarterly
- **Break-glass access**: After every use (post-incident review)

**Access Review Process**:
1. Access review report generated (who has access to what environment)
2. Environment owner reviews access list (IT Ops Manager for production, Dev Manager for dev, etc.)
3. Owner certifies access is appropriate or requests removal
4. Access removals processed within 5 business days
5. Review completion documented and signed off

**Access Review Criteria**:
- Is the user still employed? (HR verification)
- Does the user's role require this access? (manager verification)
- Has the access been used in the last 90 days? (usage logs)
- Is the access level appropriate? (least privilege review)

**Audit Verification Criteria**:
- ✅ Access reviews conducted per schedule (100% compliance)
- ✅ Access review documentation retained for audit
- ✅ Access removals processed within 5 days
- ✅ Unused access (no usage in 90 days) flagged for removal

### 2.2.8.2 Access Anomaly Detection

[Organization] **SHOULD** implement automated anomaly detection for access patterns:

**Anomaly Detection Examples**:
- Developer accessing production (should be zero - alert immediately)
- Access from unusual location (geolocation anomaly)
- Access at unusual time (3am login from developer - investigate)
- Privilege escalation (user suddenly has admin access)
- Lateral movement (access to multiple environments in short time)

**Anomaly Response**:
- High-risk anomalies (developer → production) alert immediately to security team
- Medium-risk anomalies logged and reviewed within 24 hours
- Low-risk anomalies aggregated and reviewed weekly
- Confirmed violations trigger incident response

**Audit Verification Criteria**:
- ✅ Anomaly detection rules configured per environment
- ✅ High-risk anomalies alert immediately
- ✅ Anomaly alerts reviewed and actioned
- ✅ False positive rate <10% (tuning required)

---

## 2.2.9 Authentication and Authorization Requirements

### 2.2.9.1 Authentication Strength Per Environment

[Organization] **SHALL** implement authentication strength aligned with environment sensitivity:

**Authentication Requirements**:

| Environment | SSO Required | MFA Required | PAM Required |
|-------------|--------------|--------------|--------------|
| Development | Yes | No (recommended) | No |
| Testing | Yes | No (recommended) | No |
| Staging | Yes | Yes | Recommended |
| Production | Yes | Yes | **YES (mandatory)** |

**SSO (Single Sign-On)**:
- All environment access via organizational SSO (Azure AD, Okta, etc.)
- Local accounts prohibited (except emergency break-glass account)
- SSO integrated with HR system for automatic deprovisioning

**MFA (Multi-Factor Authentication)**:
- Production access REQUIRES MFA (no exceptions)
- Staging access REQUIRES MFA (production-equivalent)
- Dev/test MFA recommended but not mandatory (balance security with developer productivity)

**PAM (Privileged Access Management)**:
- Production administrative access REQUIRES PAM vault checkout
- PAM session recording mandatory for production
- PAM credentials rotated automatically after each use

**Audit Verification Criteria**:
- ✅ SSO enforced for all environments (100% compliance)
- ✅ MFA enforced for production (100% compliance)
- ✅ PAM enforced for production admin access (100% compliance)
- ✅ Local accounts minimized (<5 emergency accounts only)

### 2.2.9.2 Authorization Model

[Organization] **SHALL** implement role-based access control (RBAC) per environment:

**RBAC Principles**:
- Predefined roles per environment (Developer, QA Engineer, Operations Engineer, etc.)
- Users assigned to roles (not individual permissions)
- Least privilege by default (grant minimum access required)
- Role definitions documented and approved

**Environment-Specific Roles**:
- Development roles: Developer, Senior Developer, DevOps Engineer
- Testing roles: QA Engineer, UAT User, Test Manager
- Staging roles: Operations Engineer (full), Senior Developer (read-only)
- Production roles: Production Operator, Production DBA, SRE

**Role Assignment Process**:
- Manager requests role assignment for user (via access request)
- Security team validates role is appropriate for user's job function
- Role assigned with defined access scope (which environment, which systems)
- Role assignments reviewed quarterly

**Audit Verification Criteria**:
- ✅ RBAC implemented for all environments
- ✅ Role definitions documented
- ✅ Users assigned to roles (not individual permissions)
- ✅ Role assignments reviewed quarterly

---

## 2.2.10 Access Logging and Monitoring

### 2.2.10.1 Access Log Requirements

[Organization] **SHALL** log all access to environments for security monitoring and audit:

**Mandatory Access Logging**:
- **Authentication events**: Login attempts (success and failure), logout, session timeout
- **Authorization events**: Permission grants, permission denials, privilege escalation
- **Administrative actions**: Configuration changes, user management, system changes
- **Data access**: File access (production), database queries (production), API calls (production)
- **Cross-environment access attempts**: Alert on any dev → prod access attempts

**Log Retention**:
- **Production logs**: 12 months minimum (regulatory requirement)
- **Staging logs**: 6 months
- **Development/testing logs**: 3 months (or per compliance requirement)

**Log Protection**:
- Logs forwarded to centralized SIEM (tamper-proof)
- Log modification alerts (integrity monitoring)
- Log access restricted to security team and auditors

**Audit Verification Criteria**:
- ✅ Access logs collected for all environments (100% coverage)
- ✅ Logs forwarded to SIEM in real-time
- ✅ Log retention meets requirements
- ✅ Log integrity monitoring active

### 2.2.10.2 Access Monitoring and Alerting

[Organization] **SHALL** monitor access logs for security violations:

**High-Priority Alerts** (immediate notification):
- Developer access to production (should be ZERO except break-glass)
- Failed authentication attempts (brute force detection)
- Privilege escalation (unauthorized admin access)
- Access from blacklisted IP/location
- Production access outside change window (unauthorized change)

**Medium-Priority Alerts** (review within 24 hours):
- Unusual access patterns (off-hours access, unusual location)
- Service account interactive login (should be automation only)
- Access to sensitive data (PII, financial data)
- Excessive failed authorization attempts (permission testing)

**Alert Response**:
- High-priority alerts page security on-call
- Medium-priority alerts create security ticket
- Alerts investigated within defined SLA
- Confirmed violations trigger incident response

**Audit Verification Criteria**:
- ✅ Alerting rules configured per environment
- ✅ High-priority alerts investigated within 15 minutes
- ✅ Alert response SLAs met >95% of time
- ✅ False positive rate <10%

---

## 2.2.11 Third-Party and Vendor Access

### 2.2.11.1 Vendor Access to Environments

[Organization] **SHALL** control third-party vendor access to environments:

**Vendor Access Restrictions**:
- Vendors access development/testing only (no production access unless absolutely necessary)
- Vendor production access requires CISO approval and business justification
- Vendor access time-limited (project duration only)
- Vendor access monitored more closely than employee access

**Vendor Access Process**:
1. Contract includes access requirements and restrictions
2. Vendor completes security questionnaire
3. Vendor personnel vetted (background check for production access)
4. Vendor assigned temporary accounts (never shared credentials)
5. Vendor access expires automatically at contract end
6. Vendor access logged and audited

**Vendor Production Access** (if unavoidable):
- Vendor cannot access production independently (supervised access only)
- Screen sharing session with [Organization] employee present
- Session recording mandatory
- Vendor access reviewed weekly while active

**Audit Verification Criteria**:
- ✅ All vendor access documented in contracts
- ✅ Vendor production access approved by CISO
- ✅ Vendor access time-limited and reviewed
- ✅ Vendor sessions recorded and auditable

---

## 2.2.12 Measurable Compliance Criteria

For audit and compliance verification, [Organization] must demonstrate:

**Access Control Compliance Metrics** (CRITICAL):
- **0 developers** with standing production access (measured monthly)
- **100%** of production access via PAM system
- **100%** of production access with MFA enabled
- **0** shared credentials between environments
- **100%** of access requests approved before provisioning
- **>95%** deprovisioning completion within 24 hours of termination
- **100%** access reviews completed on schedule
- **<10** break-glass activations per year (trending down)
- **100%** break-glass post-incident reviews completed
- **0** unauthorized cross-environment access attempts (or all investigated)

**Verification Methods**:
- Monthly production access audit (security team)
- Quarterly access reviews (environment owners)
- Semi-annual access compliance assessment (independent audit)
- Continuous monitoring via SIEM alerts
- Annual penetration test including access control verification

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Development Manager | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |
| HR Director | [Name] | ________________ | [Date] |

---

*End of Document ISMS-POL-A.8.31-S2.2*
