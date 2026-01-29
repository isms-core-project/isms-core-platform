# ISMS-POL-A.8.2-3-5-S5
## Assessment Methodology and Evidence Framework

**Document ID**: ISMS-POL-A.8.2-3-5-S5  
**Title**: Assessment Methodology and Evidence Framework (ISO/IEC 27001:2022 Controls A.8.2, A.8.3, A.8.5)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Assessment Lead | Initial assessment methodology for A.8.2/3/5 |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Assessment Review: Internal Audit Lead
- Technical Review: Security Architect

**Distribution**: Security team, internal audit, external auditors, compliance team  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 through S4 (Policy requirements)
- ISMS-IMP-A.8.2-3-5-S5 (Security Assessment Implementation)
- All assessment workbooks (Workbook 1-5, Dashboard)

---

## 1. Assessment Framework Overview

### 1.1 Purpose and Scope

**Purpose**: Define unified assessment methodology for evaluating compliance and effectiveness of Authentication & Privileged Access Security Framework across controls A.8.2, A.8.3, and A.8.5.

**Assessment Objectives**:
1. Verify technical implementation of authentication, privileged access, and access restriction controls
2. Measure control effectiveness (not just control existence)
3. Identify security gaps requiring remediation
4. Collect evidence for ISO 27001:2022 audits (internal and external)
5. Track compliance trends over time

**Scope**: This assessment methodology covers:
- **A.8.5** - Secure Authentication (authentication mechanisms, MFA, SSO, passwords)
- **A.8.2** - Privileged Access Rights (PAM, admin tiering, privileged monitoring)
- **A.8.3** - Information Access Restriction (permissions, access enforcement)

### 1.2 Combined Assessment Rationale

**Why Unified Assessment?**

1. **Shared Identity Infrastructure**: All three controls use same identity systems (AD, Azure AD, Okta, PAM)
2. **Evidence Consolidation**: Single data collection serves multiple controls
3. **Efficiency**: 3x faster than three separate assessments
4. **Holistic View**: Authentication → Privileged Access → Access Enforcement forms complete security layer

**Assessment Independence**:

Despite unified methodology, each control maintains:
- Separate requirements verification (S2 for A.8.5, S3 for A.8.2, S4 for A.8.3)
- Individual compliance scoring (separate scores per control)
- Distinct evidence collection (clear mapping: evidence → control)
- Statement of Applicability (SoA) clarity (auditors can assess each control independently)

---

## 2. Assessment Structure and Workbooks

### 2.1 Assessment Workbook Architecture

**5 Specialized Assessment Workbooks + 1 Consolidated Dashboard**:

| Workbook | Primary Control | Purpose | Key Metrics |
|----------|----------------|---------|-------------|
| **WB1: Authentication Inventory** | A.8.5 | Document authentication mechanisms by system | Auth method coverage, SSO adoption |
| **WB2: MFA Coverage** | A.8.5 | Track MFA enrollment and coverage | MFA coverage by user type, gaps |
| **WB3: Privileged Accounts** | A.8.2 | Inventory privileged accounts and tier classification | PAM coverage, tier isolation |
| **WB4: Privileged Monitoring** | A.8.2 | Track privileged access activity and reviews | Session recording, alert response |
| **WB5: Access Restrictions** | A.8.3 | Assess technical access control effectiveness | Permission compliance, pen test results |
| **Dashboard** | A.8.2/3/5 | Executive compliance overview | Overall scores, gap prioritization |

### 2.2 Workbook Integration Flow

```
Data Collection → Individual Workbooks → Consolidated Dashboard → Executive Reporting

Workbook 1 (Auth Inventory) ┐
Workbook 2 (MFA Coverage)   ├→ Dashboard → Executive Summary
Workbook 3 (Priv Accounts)  ├→ Compliance Scores per Control
Workbook 4 (Priv Monitoring)├→ Gap Prioritization
Workbook 5 (Access Controls)┘  Trend Analysis
```

### 2.3 Assessment Frequency

**Continuous Monitoring** (automated where possible):
- MFA enrollment status (daily updates)
- Authentication logs (real-time SIEM)
- Privileged access activity (real-time PAM logs)
- Permission changes (daily configuration scans)

**Monthly Reviews**:
- Privileged account inventory updates
- Failed authentication analysis
- Privileged access anomaly review

**Quarterly Assessments** (formal):
- Complete all 5 workbooks
- Privileged access rights review (A.8.2 requirement)
- Permission audits (sample of critical systems)
- Generate dashboard and executive report

**Annual Assessments** (comprehensive):
- Full system coverage (not just samples)
- Penetration testing (access control bypass attempts)
- Deep review of service accounts, break-glass accounts
- Admin tier classification review
- ISO 27001:2022 annual audit preparation

---

## 3. Workbook 1: Authentication Inventory & Methods (A.8.5)

### 3.1 Assessment Objectives

**Purpose**: Document authentication mechanisms across all systems and evaluate security posture.

**Key Questions**:
- What authentication methods are used? (password, MFA, SSO, certificate, biometric)
- Which systems use modern authentication protocols? (SAML, OAuth vs. legacy NTLM, Basic Auth)
- What is SSO adoption rate?
- Are password policies compliant with requirements?

### 3.2 Data Collection

**Systems to Inventory**:
- All user-facing systems (applications, web portals, VPNs)
- Infrastructure systems (servers, network devices, databases)
- Cloud platforms (AWS, Azure, GCP consoles)
- SaaS applications

**Data Points per System**:
- System name and description
- Authentication method (password-only, password+MFA, SSO, certificate, biometric)
- Authentication protocol (SAML, OAuth, OIDC, Kerberos, LDAP, RADIUS, Basic Auth)
- Authentication provider (Azure AD, Okta, AD, local, other)
- SSO integration status (integrated, not integrated, in progress)
- Password policy enforced (yes/no, policy details)
- MFA available (yes/no, MFA methods)

**Data Sources**:
- Identity provider reports (Azure AD, Okta application catalogs)
- Application inventory (IT asset management)
- Network discovery scans
- Manual documentation review

### 3.3 Assessment Criteria

**Compliance Scoring**:

| Authentication Method | Security Score | Rationale |
|----------------------|----------------|-----------|
| Password-only (no MFA option) | 🔴 0% | Unacceptable - vulnerable to credential compromise |
| Password-only (MFA available but not enforced) | 🟡 25% | Poor - MFA should be mandatory |
| Password + MFA (optional) | 🟡 50% | Marginal - MFA not enforced |
| Password + MFA (mandatory) | 🟢 75% | Good - strong authentication |
| SSO + MFA (mandatory) | 🟢 90% | Very Good - centralized + strong |
| Certificate-based + MFA | 🟢 95% | Excellent - phishing-resistant |
| Hardware token (FIDO2) + MFA | 🟢 100% | Excellent - strongest authentication |

**SSO Adoption Metrics**:
- Target: 90%+ of SaaS applications integrated with SSO
- Current: Calculate (SSO-integrated apps / total apps) × 100%
- Gap: Applications not yet integrated with SSO

**Password Policy Compliance**:
- Minimum length 12 characters: Yes/No
- Complexity enforced: Yes/No
- Breach detection enabled: Yes/No
- Password expiration: Acceptable (disabled or 90+ days)

### 3.4 Evidence Collection

**Evidence for A.8.5 (Authentication)**:
- Authentication inventory report (Workbook 1 export)
- SSO application catalog screenshots
- Password policy configurations (GPO, Azure AD, Okta)
- Sample authentication logs

**Audit Value**:
- Demonstrates comprehensive authentication mechanism documentation
- Shows technology-agnostic assessment (works for any identity provider)
- Provides baseline for measuring SSO adoption progress

---

## 4. Workbook 2: MFA Coverage Assessment (A.8.5)

### 4.1 Assessment Objectives

**Purpose**: Measure multi-factor authentication coverage across user population and identify gaps.

**Key Questions**:
- What % of users have MFA enrolled?
- What % of privileged users have MFA? (Target: 100%)
- What % of remote access users have MFA? (Target: 100%)
- What MFA methods are used? (Hardware token, authenticator app, SMS)
- What are high-priority gaps? (Privileged users without MFA)

### 4.2 Data Collection

**User Population Segmentation**:
1. **Privileged users** (system admins, DBAs, security admins, cloud admins)
2. **Remote access users** (VPN users, external access)
3. **Standard internal users** (office-based, internal access only)
4. **Contractors/vendors** (temporary accounts)

**Data Points per User**:
- User ID and name
- User type (privileged, remote, standard, contractor)
- MFA enrolled (yes/no)
- MFA method (hardware token, authenticator app, push notification, SMS, biometric, none)
- MFA enrollment date
- Backup MFA method registered (yes/no)
- Last successful MFA authentication

**Data Sources**:
- Identity provider MFA reports (Azure AD, Okta MFA enrollment reports)
- Active Directory privileged group memberships
- VPN access logs (who authenticated to VPN)
- PAM solution user lists (privileged users)

### 4.3 Assessment Criteria

**MFA Coverage Targets**:

| User Type | MFA Target | Current Status | Gap |
|-----------|------------|----------------|-----|
| **Privileged users** | 100% MANDATORY | Calculate from data | High priority gap |
| **Remote access users** | 100% MANDATORY | Calculate from data | High priority gap |
| **Standard users** | 90%+ target | Calculate from data | Medium priority gap |
| **Contractors/vendors** | 100% MANDATORY | Calculate from data | High priority gap |

**Compliance Scoring**:
- 🟢 Green (Compliant): ≥95% MFA coverage for user type
- 🟡 Yellow (Partial): 75-94% MFA coverage
- 🔴 Red (Non-Compliant): <75% MFA coverage

**MFA Method Quality**:

| MFA Method | Security Rating | Suitable For |
|------------|-----------------|--------------|
| Hardware token (FIDO2) | 🟢 Excellent | Tier 0 privileged users (required) |
| Authenticator app (TOTP) | 🟢 Good | Privileged users, standard users |
| Push notification | 🟢 Good | Standard users (convenient) |
| Biometric | 🟡 Acceptable | Mobile devices, workstation login |
| SMS | 🔴 Poor | Backup only (not primary MFA) |

### 4.4 Gap Analysis

**High-Priority Gaps** (immediate remediation required):
- Privileged users without MFA (critical security risk)
- Remote access users without MFA (exposure to external threats)
- Service accounts without certificate-based auth (password-only service accounts)

**Medium-Priority Gaps**:
- Standard users without MFA (phishing risk)
- Users with SMS as primary MFA (upgrade to authenticator app)

**Gap Remediation Tracking**:
- Gap identified date
- User notified date
- Deadline for MFA enrollment (7 days for privileged, 30 days for standard)
- Remediation status (in progress, complete, overdue)
- Escalation (if overdue: notify manager, restrict access)

### 4.5 Evidence Collection

**Evidence for A.8.5 (Authentication)**:
- MFA enrollment report by user type (Workbook 2 export)
- MFA coverage trend chart (quarterly comparison)
- Gap remediation tracking (high-priority gaps addressed)
- NIS2 compliance evidence (MFA mandatory per Article 21(2)(e))

**Audit Value**:
- Demonstrates MFA deployment progress toward targets
- Shows prioritization (privileged users first, then all users)
- Provides regulatory compliance evidence (NIS2, FINMA, DORA)

---

## 5. Workbook 3: Privileged Account Inventory (A.8.2)

### 5.1 Assessment Objectives

**Purpose**: Maintain complete inventory of privileged accounts with admin tier classification and PAM coverage tracking.

**Key Questions**:
- How many privileged accounts exist? (Named, shared, service, break-glass)
- What admin tier is each account? (Tier 0, Tier 1, Tier 2)
- Which privileged accounts are in PAM vault? (Target: 100% of shared accounts)
- Do all privileged users have MFA? (Target: 100%)
- Are Tier 0 accounts using PAWs and hardware tokens?

### 5.2 Data Collection

**Privileged Account Discovery**:

**Windows Active Directory**:
- Domain Admins, Enterprise Admins, Schema Admins (Tier 0)
- Server Administrators, Backup Operators (Tier 1)
- Workstation administrators (Tier 2)
- Local Administrator accounts on servers/workstations

**Azure AD / Entra ID**:
- Global Administrator (Tier 0)
- Security Administrator, Compliance Administrator (Tier 0)
- Application Administrator, Cloud Application Administrator (Tier 1)

**AWS IAM**:
- Root account (Tier 0 - should be break-glass only)
- AdministratorAccess policy users (Tier 0)
- PowerUser policy users (Tier 1)

**Databases**:
- sa (SQL Server), SYSTEM (Oracle), postgres (PostgreSQL) - Tier 1
- DBA accounts - Tier 1

**Data Points per Privileged Account**:
- Account name (john.doe.admin, root, sa, Administrator)
- Account type (named, shared, service, break-glass)
- Privileged role (Windows admin, Linux admin, DBA, security admin, cloud admin)
- **Admin tier** (Tier 0, Tier 1, Tier 2, N/A)
- Owner (for named accounts) or responsible party (for shared/service)
- Systems/platforms (Windows servers, Linux servers, AWS, Azure, databases)
- Last password change date
- PAM vaulted (yes/no - for shared accounts)
- MFA enabled (yes/no - for named accounts)
- **Tier isolation compliance**: Has this Tier 0 account logged into Tier 1/2 systems? (violation count)

### 5.3 Admin Tier Classification

**Critical Requirement**: Every privileged account must be classified into tier.

**Tier 0 Accounts** (Domain/Enterprise/Critical):
- Domain Admins, Enterprise Admins, Schema Admins
- Azure Global Administrator, AWS root account
- SIEM administrators, PAM administrators
- Backup administrators (can restore any system)
- Certificate Authority administrators

**Tier 1 Accounts** (Server/Application):
- Server administrators (Windows server admin, Linux admin)
- Database administrators (SQL Server DBA, Oracle DBA)
- Application administrators (SAP admin, Salesforce admin)
- Virtualization administrators (VMware admin, Hyper-V admin)
- Cloud infrastructure admins (AWS EC2 admin, Azure VM admin)

**Tier 2 Accounts** (Workstation/Endpoint):
- Desktop support / Help desk (local admin on workstations)
- MDM administrators (Intune, Jamf - device management)
- Endpoint management (patch management for workstations)

### 5.4 Assessment Criteria

**PAM Coverage**:
- 🟢 Target: 100% of shared privileged accounts in PAM vault
- Calculate: (Shared accounts in PAM / Total shared accounts) × 100%

**Privileged MFA Coverage**:
- 🟢 Target: 100% of privileged users with MFA
- Calculate: (Privileged users with MFA / Total privileged users) × 100%

**Tier 0 Security Requirements**:
- Hardware MFA tokens: 100% of Tier 0 users (yes/no per user)
- PAW deployment: 100% of Tier 0 admins (yes/no per user)
- Tier isolation: Zero cross-tier violations (Tier 0 logging into Tier 1/2)

**Credential Rotation Compliance**:
- Shared accounts: Password changed within last 30 days (yes/no)
- Service accounts: Password changed within last 90 days (yes/no)
- Break-glass accounts: Password changed after each use (yes/no)

### 5.5 Evidence Collection

**Evidence for A.8.2 (Privileged Access)**:
- Privileged account inventory with tier classification (Workbook 3 export)
- PAM vault coverage report (% of shared accounts vaulted)
- MFA enrollment for privileged users (100% target)
- Tier 0 PAW deployment status
- Hardware MFA token assignment records
- Tier isolation compliance (cross-tier violation count = 0)
- Quarterly privileged access review attestations

**Audit Value**:
- Demonstrates complete privileged account visibility
- Shows admin tiering implementation (critical for preventing lateral movement)
- Provides evidence of PAM deployment and coverage
- Documents privileged access oversight (quarterly reviews)

---

## 6. Workbook 4: Privileged Access Monitoring (A.8.2)

### 6.1 Assessment Objectives

**Purpose**: Track privileged access activity, detect anomalies, and verify monitoring controls effectiveness.

**Key Questions**:
- Is privileged access being monitored? (session recording, logging, alerting)
- Are privileged sessions recorded? (Target: 90%+ coverage)
- Are privileged access alerts responding quickly? (Target: <30 min response)
- Are quarterly privileged access reviews completed? (Target: 100%)
- Are there tier isolation violations? (Target: zero violations)

### 6.2 Data Collection

**Privileged Access Activity Monitoring**:

**Data Points**:
- Privileged account used
- System accessed
- Login date/time (timestamp)
- Session duration
- Session recorded (yes/no)
- Off-hours access (yes/no - outside 8 AM - 6 PM business hours)
- Unusual location (yes/no - new location/IP never seen before)
- Commands executed (if logged)
- Alert generated (yes/no)
- Alert response time (minutes)

**Data Sources**:
- PAM solution session logs
- Active Directory Security Event Logs (Event ID 4672 - Special Privileges)
- Linux sudo logs (centralized via rsyslog)
- Database audit logs (privileged account usage)
- Cloud platform audit logs (AWS CloudTrail, Azure Activity Log)
- SIEM alerts (privileged access anomalies)

### 6.3 Privileged Access Anomalies

**Anomaly Detection**:

| Anomaly Type | Detection Method | Priority | Response Time Target |
|--------------|------------------|----------|---------------------|
| Off-hours privileged access | Login 10 PM - 6 AM or weekends | Medium | 1 hour |
| Unusual location | New country/city | High | 30 minutes |
| Tier 0 activity | ANY Tier 0 account use | High | 15 minutes |
| Tier isolation violation | Tier 0 account on Tier 1/2 system | Critical | 5 minutes |
| Failed privileged login | 3+ failed attempts | High | 15 minutes |
| Long session | Session >4 hours | Medium | 1 hour |
| Break-glass usage | Break-glass account login | Critical | Immediate |

**Anomaly Response Tracking**:
- Anomaly detected date/time
- Alert sent to (security team, SOC, on-call admin)
- Response initiated date/time
- Investigation findings (legitimate access or security incident)
- Resolution (approved, password reset required, account suspended)

### 6.4 Session Recording Coverage

**Session Recording Assessment**:

**Recording Targets**:
- 🟢 100% of Tier 0 sessions (mandatory)
- 🟢 90%+ of Tier 1 production sessions (highly recommended)
- 🟡 50%+ of Tier 2 sessions (recommended)

**Recording Quality**:
- Video recording (for RDP/GUI sessions)
- Keystroke logging (for SSH/CLI sessions)
- Recording retention: 90 days online, 1 year archived
- Recordings searchable (by user, system, date, commands)

### 6.5 Quarterly Privileged Access Reviews

**Review Completion Tracking**:

**For each quarterly review period**:
- Review period (Q1, Q2, Q3, Q4)
- Privileged users reviewed (count and %)
- Privileged access confirmed appropriate (count)
- Privileged access removed as no longer needed (count)
- Privileged access justified as exception (count)
- Manager attestations collected (yes/no per manager)
- Review completion date (within 30 days of quarter end?)

**Review Metrics**:
- 🟢 Target: 100% of privileged users reviewed quarterly
- Access removal rate: 5-10% typical (continuous cleanup)
- Overdue reviews: 0 (all reviews completed on time)

### 6.6 Evidence Collection

**Evidence for A.8.2 (Privileged Access)**:
- Privileged access activity logs (Workbook 4 export)
- Session recording samples (demonstrate recording capability)
- Anomaly detection alerts and response times
- Tier isolation violation report (target: zero violations)
- Quarterly review completion attestations
- Alert response metrics (average response time <30 minutes)

**Audit Value**:
- Demonstrates privileged access is monitored (not just controlled)
- Shows timely response to suspicious privileged activity
- Provides evidence of quarterly review process (A.8.2 requirement)
- Documents tier isolation enforcement and monitoring

---

## 7. Workbook 5: Access Restriction Compliance (A.8.3)

### 7.1 Assessment Objectives

**Purpose**: Assess technical access control effectiveness across operating systems, databases, applications, and APIs.

**Key Questions**:
- Are file permissions configured with default deny? (Target: 95%+)
- Are database permissions following least privilege? (Target: 90%+ with specific grants)
- Are access controls tested? (Penetration testing, configuration audits)
- Is encryption deployed per data classification? (Target: 100% for restricted data)
- Are there access control vulnerabilities? (Target: zero high/critical findings)

### 7.2 Data Collection

**Multi-Layer Assessment**:

**1. Operating System Permissions**:
- Systems assessed (Windows servers, Linux servers, workstations)
- Permission audit date
- Default deny configured (yes/no)
- Permission compliance score (% compliant with baseline)
- Findings (overly permissive permissions, Everyone group with write access, etc.)

**2. Database Access Controls**:
- Databases assessed (SQL Server, Oracle, PostgreSQL, MySQL, MongoDB, etc.)
- Database accounts reviewed
- Least privilege compliance (% accounts with specific grants vs. db_owner/ALL)
- Unused accounts identified (no connections in 90 days)
- Service accounts with excessive privileges (count)

**3. Application Access Controls**:
- Applications assessed
- RBAC implemented (yes/no)
- Role-permission matrix documented (yes/no)
- User-role assignments reviewed (date)
- SoD (Segregation of Duties) violations (count)

**4. API Access Controls**:
- APIs assessed
- Authentication method (OAuth, API keys, certificates, none)
- Rate limiting configured (yes/no)
- Scope-based authorization (yes/no)
- API vulnerabilities (OWASP API Top 10)

**5. Cloud IAM Policies**:
- Cloud platform (AWS, Azure, GCP)
- IAM policies reviewed (count)
- Overly permissive policies (wildcard actions like s3:*, ec2:*)
- Unused roles/policies (no activity in 90 days)

### 7.3 Data Classification and Encryption

**Encryption Compliance by Classification**:

| Data Classification | Encryption Required | Current Status | Gap |
|---------------------|---------------------|----------------|-----|
| **Restricted** | At rest + in transit | Calculate from data | High priority |
| **Confidential** | At rest | Calculate from data | Medium priority |
| **Internal** | Recommended | Calculate from data | Low priority |
| **Public** | Not required | N/A | N/A |

**Encryption Technologies**:
- Full disk encryption (BitLocker, FileVault, LUKS)
- Database TDE (Transparent Data Encryption)
- File encryption (EFS, encrypted shares)
- TLS for data in transit (TLS 1.2+ minimum)

### 7.4 Access Control Testing Results

**Penetration Testing Findings**:

**Test Scope**:
- Access control bypass attempts (horizontal/vertical privilege escalation)
- API authorization bypass (IDOR vulnerabilities)
- File traversal attacks (../../../etc/passwd)
- SQL injection (database access control bypass)

**Finding Severity**:
- 🔴 Critical: Direct access to restricted data without authentication
- 🔴 High: Privilege escalation (standard user → admin)
- 🟡 Medium: Information disclosure (access to data outside assigned scope)
- 🟢 Low: Minor configuration issues

**Remediation Tracking**:
- Finding ID and description
- Severity (critical, high, medium, low)
- Identified date
- Remediation deadline (30 days for critical/high, 90 days for medium, 180 days for low)
- Remediation status (open, in progress, resolved, verified)
- Re-test date (verify fix works)

### 7.5 Assessment Criteria

**Access Control Compliance Scoring**:

| Metric | Target | Scoring |
|--------|--------|---------|
| Systems with default deny | 95%+ | 🟢 ≥95%, 🟡 85-94%, 🔴 <85% |
| Database least privilege | 90%+ | 🟢 ≥90%, 🟡 75-89%, 🔴 <75% |
| APIs with authentication | 100% | 🟢 100%, 🔴 <100% (critical) |
| Encryption - restricted data | 100% | 🟢 100%, 🔴 <100% (critical) |
| Pen test critical findings | 0 | 🟢 0, 🔴 >0 (unacceptable) |
| Pen test high findings | <3 | 🟢 0-2, 🟡 3-5, 🔴 >5 |

### 7.6 Evidence Collection

**Evidence for A.8.3 (Access Restriction)**:
- Permission audit reports (file system, database, application) - Workbook 5 export
- Configuration compliance scan results (CIS benchmarks)
- Penetration test reports (access control testing)
- Encryption inventory by data classification
- Finding remediation tracking (critical/high findings resolved)
- Network segmentation documentation (firewall rules - reference A.8.22)

**Audit Value**:
- Demonstrates technical access controls are assessed (not just documented)
- Shows access control effectiveness testing (penetration testing)
- Provides evidence of encryption deployment per data classification
- Documents remediation of access control vulnerabilities

---

## 8. Consolidated Dashboard

### 8.1 Dashboard Purpose

**Purpose**: Executive-level view of authentication and privileged access security compliance across all three controls (A.8.2, A.8.3, A.8.5).

**Dashboard Consumers**:
- CISO and security leadership (compliance status, risk prioritization)
- Internal audit (evidence for ISO 27001:2022 audit)
- External auditors (Statement of Applicability verification)
- Management (security investment justification)

### 8.2 Dashboard Structure

**Section 1: Overall Compliance Summary**

- **Overall Authentication & PAM Security Score**: Weighted average of three control scores
  - A.8.5 (Authentication) score: Weight 30%
  - A.8.2 (Privileged Access) score: Weight 40% (highest risk)
  - A.8.3 (Access Restriction) score: Weight 30%

- **Compliance Status**: 🟢 Compliant (≥90%), 🟡 Partial (75-89%), 🔴 Non-Compliant (<75%)

**Section 2: Control-Specific Scores**

**A.8.5 - Secure Authentication**:
- MFA coverage: Overall % and by user type (privileged, remote, standard)
- SSO adoption: % of applications integrated with SSO
- Password policy compliance: % systems with compliant password policies
- Authentication security score: 0-100%

**A.8.2 - Privileged Access Rights**:
- Privileged MFA coverage: % privileged users with MFA (target 100%)
- PAM vault coverage: % shared accounts in PAM vault (target 100%)
- Session recording coverage: % privileged sessions recorded
- Tier 0 security: % Tier 0 with PAWs and hardware MFA
- Tier isolation compliance: Cross-tier violation count (target 0)
- Quarterly review completion: % privileged users reviewed
- Privileged access score: 0-100%

**A.8.3 - Information Access Restriction**:
- Systems with default deny: % systems configured default deny
- Database least privilege: % DB accounts with specific grants
- Encryption compliance: % by data classification (restricted, confidential)
- Penetration test findings: Critical/high findings count
- Access restriction score: 0-100%

**Section 3: Critical Gaps Requiring Remediation**

**High-Priority Gaps** (top 10 most critical):
1. Privileged users without MFA (count) - CRITICAL RISK
2. Tier 0 accounts without PAWs (count) - CRITICAL RISK
3. Shared privileged accounts not in PAM vault (count) - HIGH RISK
4. Access control penetration test critical findings (count) - HIGH RISK
5. Restricted data not encrypted (count) - HIGH RISK
6. Tier isolation violations (count) - HIGH RISK
7. Standard users without MFA (count) - MEDIUM RISK
8. Applications not integrated with SSO (count) - MEDIUM RISK
9. Privileged sessions not recorded (count) - MEDIUM RISK
10. Database accounts with excessive privileges (count) - MEDIUM RISK

**Section 4: Compliance Trends**

- Quarterly trend charts:
  - MFA coverage trend (increasing over time)
  - PAM vault coverage trend
  - Tier isolation compliance trend
  - Overall security score trend

**Section 5: Evidence Summary**

- Total evidence items collected (count across all workbooks)
- Evidence completeness: % of required evidence collected
- Evidence freshness: Date of last assessment per workbook
- Next scheduled assessment: When is next quarterly assessment due?

### 8.3 Dashboard Generation

**Consolidation Logic**:

Dashboard script imports data from all 5 workbooks:
- Import Workbook 1 (Authentication Inventory) → SSO adoption, auth method distribution
- Import Workbook 2 (MFA Coverage) → MFA coverage by user type
- Import Workbook 3 (Privileged Accounts) → PAM coverage, tier classification, MFA for privileged
- Import Workbook 4 (Privileged Monitoring) → Session recording, alert response, reviews
- Import Workbook 5 (Access Restrictions) → Permission compliance, encryption, pen test results

**Automated Calculations**:
- Calculate weighted scores per control
- Identify top 10 critical gaps (by risk priority)
- Generate trend charts (if historical data available)
- Flag overdue remediation items

### 8.4 Evidence Collection

**Evidence for Combined Assessment (A.8.2/3/5)**:
- Executive dashboard (consolidated view)
- All 5 workbooks (detailed evidence per control)
- Quarterly assessment reports
- Trend analysis (compliance improving over time)
- Gap remediation tracking

**Audit Value**:
- Provides executive summary for auditors (high-level view)
- Demonstrates unified assessment methodology
- Shows compliance trends (continuous improvement)
- Clear mapping: Dashboard → Workbooks → Individual Controls → ISO Requirements

---

## 9. Assessment Execution Procedures

### 9.1 Quarterly Assessment Schedule

**Assessment Timeline** (30-day cycle per quarter):

**Week 1: Data Collection**
- Days 1-3: Export data from identity providers (Azure AD, Okta, AD)
- Days 4-5: Export data from PAM solutions (CyberArk, BeyondTrust)
- Days 6-7: Run configuration scans (CIS benchmarks, custom scripts)

**Week 2: Workbook Population**
- Days 8-10: Populate Workbooks 1-2 (Authentication, MFA)
- Days 11-13: Populate Workbooks 3-4 (Privileged Accounts, Monitoring)
- Day 14: Populate Workbook 5 (Access Restrictions)

**Week 3: Analysis and Review**
- Days 15-17: Analyze data, identify gaps, prioritize remediation
- Days 18-19: Generate dashboard, prepare executive report
- Days 20-21: Internal review (security team validates findings)

**Week 4: Reporting and Remediation Planning**
- Days 22-24: Present findings to CISO and security leadership
- Days 25-27: Develop remediation plans for critical gaps
- Days 28-30: Initiate remediation (assign owners, set deadlines)

### 9.2 Data Sources and Integration

**Identity Provider APIs**:
- **Azure AD Graph API**: MFA enrollment, authentication methods, privileged role assignments
- **Okta API**: MFA enrollment, authentication logs, application integrations
- **Active Directory PowerShell**: Privileged group memberships, account attributes

**PAM Solution APIs**:
- **CyberArk REST API**: Vaulted accounts, session recordings, check-out logs
- **BeyondTrust API**: Session recordings, privileged access activity

**SIEM Integration**:
- **Splunk/Datadog/Elastic**: Authentication logs, privileged access logs, security alerts
- **Query for**: Failed authentication attempts, privileged access anomalies, tier isolation violations

**Configuration Management**:
- **Ansible/PowerShell DSC**: Configuration compliance (file permissions, database grants)
- **Cloud APIs**: AWS IAM policies, Azure RBAC assignments, GCP IAM bindings

**Manual Data Collection** (where automation unavailable):
- Service account inventory (spreadsheet from application teams)
- Break-glass account documentation (sealed envelopes verification)
- Permission matrices (documented by system owners)

### 9.3 Assessment Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **CISO** | Approve assessment methodology, review findings, prioritize remediation |
| **Security Architect** | Design assessment procedures, interpret results, recommend controls |
| **IAM Lead** | Execute authentication/MFA assessments (WB1, WB2), provide identity data |
| **PAM Administrator** | Execute privileged access assessments (WB3, WB4), provide PAM data |
| **Systems Administrators** | Provide access control data (WB5), execute configuration audits |
| **Internal Audit** | Verify assessment methodology, validate evidence quality |
| **System Owners** | Attest to access control configurations, approve permission matrices |

---

## 10. Evidence Management

### 10.1 Evidence Collection Requirements

**Evidence Repository Structure**:

```
ISMS-A.8.2-3-5-Evidence/
├── 2024-Q1/
│   ├── Workbook-1-Authentication-Inventory.xlsx
│   ├── Workbook-2-MFA-Coverage.xlsx
│   ├── Workbook-3-Privileged-Accounts.xlsx
│   ├── Workbook-4-Privileged-Monitoring.xlsx
│   ├── Workbook-5-Access-Restrictions.xlsx
│   ├── Dashboard-Authentication-PAM.xlsx
│   ├── Executive-Report-Q1-2024.pdf
│   └── Raw-Data/
│       ├── AzureAD-MFA-Export.csv
│       ├── PAM-Session-Logs.csv
│       ├── Privileged-Access-Review-Attestations.pdf
│       └── Penetration-Test-Report.pdf
├── 2024-Q2/
│   └── [same structure]
└── Annual-Reports/
    └── ISO27001-Annual-Audit-2024.pdf
```

### 10.2 Evidence Retention

**Retention Requirements**:
- **Current year**: All workbooks and raw data (immediate access)
- **Previous 2 years**: Archived workbooks (compliance audits)
- **Older than 3 years**: Quarterly summaries only (historical trends)

**Evidence Access Control**:
- Evidence contains sensitive data (privileged account lists, security vulnerabilities)
- Access restricted to: Security team, internal audit, external auditors (with NDA)
- Evidence stored in secure location (encrypted file share)

### 10.3 Evidence Quality Assurance

**Quality Checks**:
1. **Completeness**: All required data fields populated (no blank cells for mandatory fields)
2. **Accuracy**: Data validated against source systems (spot checks)
3. **Timeliness**: Assessment data current (not older than 30 days at time of report)
4. **Consistency**: Data consistent across workbooks (e.g., privileged user count matches in WB2, WB3, WB4)

**Validation Procedures**:
- Automated validation script checks workbook data quality
- Manual review by second security team member
- Internal audit spot-checks (random sample of 10% of data verified against source)

---

## 11. Continuous Improvement

### 11.1 Assessment Methodology Updates

**Annual Review**:
- Review assessment methodology effectiveness (did assessments identify real security gaps?)
- Update workbook templates (add new data fields, improve calculations)
- Incorporate lessons learned (what worked well, what didn't)
- Align with updated regulatory requirements (new NIS2 guidance, FINMA circulars)

**Triggers for Interim Updates**:
- New technology deployment (new authentication method, new PAM solution)
- Regulatory changes (new compliance requirements)
- Security incidents (assessment should have detected the issue)
- Auditor feedback (external auditors recommend improvements)

### 11.2 Automation Opportunities

**Current Manual Processes** (candidates for automation):
- Data export from identity providers → Automate with API scripts
- Workbook data entry → Automate with Python scripts (direct data import)
- Configuration scanning → Automate with Ansible/PowerShell scheduled tasks
- Dashboard generation → Automate with Python script (reads all 5 workbooks, generates dashboard)

**Automation Benefits**:
- Reduce assessment time (30 days → 7 days with full automation)
- Improve data accuracy (eliminate manual data entry errors)
- Enable more frequent assessments (monthly instead of quarterly)
- Real-time dashboards (dashboard updates daily instead of quarterly)

---

## 12. Integration with Broader ISMS

### 12.1 Integration with Other Controls

**Assessment Synergies**:

**A.5.15-16-18 (Identity & Access Management)**:
- User provisioning (A.5.16) → Feeds authentication assessment (WB1, WB2)
- Access rights management (A.5.18) → Quarterly reviews align with privileged access reviews (WB4)

**A.8.16 (Monitoring)**:
- SIEM alerts → Feed privileged access monitoring (WB4)
- Authentication logs → Feed authentication assessment (WB1)

**A.8.15 (Logging)**:
- Log retention → Supports audit evidence requirements

**A.8.22 (Network Segmentation)**:
- Firewall rules → Support access restriction assessment (WB5)

### 12.2 Integration with Risk Management

**Risk Assessment Integration**:
- Assessment findings → Update risk register (privileged access risks)
- Critical gaps → Escalate to risk management (risk acceptance or mitigation)
- Compliance scores → Input to overall information security risk scoring

**Risk Mitigation Tracking**:
- Gap remediation plans → Risk treatment plans
- Remediation completion → Risk reduction evidence

---

## 13. Regulatory and Audit Considerations

### 13.1 ISO 27001:2022 Annual Audit Preparation

**Assessment Evidence for External Auditors**:

**For A.8.5 (Secure Authentication)**:
- Policy: ISMS-POL-A.8.2-3-5-S2
- Evidence: Workbook 1 (Authentication Inventory), Workbook 2 (MFA Coverage)
- Demonstrate: MFA deployment progress, SSO adoption, password policy compliance

**For A.8.2 (Privileged Access Rights)**:
- Policy: ISMS-POL-A.8.2-3-5-S3
- Evidence: Workbook 3 (Privileged Accounts), Workbook 4 (Privileged Monitoring)
- Demonstrate: PAM deployment, admin tiering, session recording, quarterly reviews

**For A.8.3 (Information Access Restriction)**:
- Policy: ISMS-POL-A.8.2-3-5-S4
- Evidence: Workbook 5 (Access Restrictions), penetration test reports
- Demonstrate: Permission audits, configuration compliance, encryption deployment, access control testing

**Audit Interview Preparation**:
- Security team can articulate assessment methodology
- Examples of gap identification and remediation
- Trend analysis showing continuous improvement

### 13.2 Regulatory Compliance Evidence

**NIS2 Compliance** (if applicable):
- **Article 21(2)(e)**: MFA deployment → Workbook 2 shows MFA coverage (must be >0% and increasing)
- **Article 21(2)(d)**: Access control policies → All policy sections S2, S3, S4

**FINMA Compliance** (if applicable):
- **Margin 56**: Authentication for critical systems → Workbook 1 shows authentication mechanisms
- **Margin 63-72**: Logging and monitoring → Workbook 4 shows privileged access monitoring

**GDPR Article 32** (if applicable):
- Security of processing → Assessment demonstrates technical security measures (MFA, access controls, encryption)

---

**END OF SECTION 5 (ASSESSMENT METHODOLOGY AND EVIDENCE FRAMEWORK)**

**POLICY SUITE COMPLETE**

All 5 policy sections (S1-S5) now complete. Next deliverables: Implementation guides and assessment scripts.

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISMS Assessment Lead | Initial assessment methodology for A.8.2/3/5 |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**