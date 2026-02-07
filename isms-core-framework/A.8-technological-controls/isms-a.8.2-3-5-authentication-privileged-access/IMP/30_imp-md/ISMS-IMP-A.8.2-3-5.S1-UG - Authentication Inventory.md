**ISMS-IMP-A.8.2-3-5.S1-UG - Authentication Inventory & Methods**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Authentication Mechanisms Inventory |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.1 - Secure Authentication) |
| **Purpose** | Systematic inventory of authentication mechanisms across all systems, applications, and services to verify authentication security controls |
| **Target Audience** | Security Team, IT Operations, System Owners, IAM Team |
| **Assessment Type** | Technical Inventory & Configuration Review |
| **Review Cycle** | Monthly updates, Quarterly comprehensive review |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for authentication inventory | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.2-3-5.S1-TG.

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.1 - Authentication Inventory & Methods

**What This Assessment Does:**

- Inventories ALL authentication mechanisms across the organization
- Documents authentication methods per system/application/service
- Identifies authentication protocols in use (SAML, OAuth, Kerberos, LDAP, etc.)
- Tracks password policy implementation
- Measures SSO adoption
- Identifies authentication security gaps

**What This Assessment Does NOT Do:**

- Track individual user MFA enrollment (see IMP.2 - MFA Coverage Assessment)
- Inventory privileged accounts (see IMP.3 - Privileged Account Inventory)
- Assess access control effectiveness (see IMP.5 - Access Restrictions Assessment)

**Primary ISO 27001 Control:** A.8.5 - Secure Authentication

**Related Controls:**

- A.5.16 - Identity Management (identity foundation for authentication)
- A.8.2 - Privileged Access Rights (authentication for privileged users)
- A.8.3 - Information Access Restriction (authentication enables access)

## When to Use This Assessment

**Use this assessment when:**

- Conducting initial authentication security baseline (first certification)
- Monthly updates (new systems deployed, authentication changes)
- Quarterly formal compliance reporting
- Preparing for ISO 27001 certification audits
- Investigating authentication-related security incidents
- Planning authentication modernization projects (SSO rollout, MFA deployment)

**Assessment Frequency:**

- **Monthly**: Update inventory for new systems, document authentication changes
- **Quarterly**: Comprehensive review, validate all entries, update compliance scores
- **Annual**: Deep assessment with penetration testing, full validation

## Who Completes This Assessment

**Primary Responsibility:** Security Team (authentication security lead)

**Supporting Roles:**

- **IT Operations**: Provide system authentication configuration details
- **System Owners**: Verify authentication methods for owned systems
- **Application Owners**: Document application authentication integration
- **IAM Team**: Provide identity provider configuration (Entra ID, Okta, Active Directory)
- **Network Team**: Provide authentication infrastructure details (RADIUS, TACACS+)

**Approval Authority:** Chief Information Security Officer (CISO)

## Expected Time Investment

**Initial Assessment** (first time completing):

- Data collection: 4-8 hours (depends on number of systems)
- Workbook completion: 2-4 hours
- Evidence collection: 2-3 hours
- Review and validation: 1-2 hours
- **Total**: 9-17 hours (spread over 1-2 weeks)

**Monthly Updates** (after initial baseline):

- New system authentication review: 30-60 minutes
- Workbook updates: 15-30 minutes
- Evidence updates: 15-30 minutes
- **Total**: 1-2 hours per month

**Quarterly Comprehensive Review**:

- Full inventory validation: 2-3 hours
- Evidence update: 1-2 hours
- Compliance reporting: 1 hour
- **Total**: 4-6 hours per quarter

---

# Prerequisites

## Required Information

Before starting the assessment, gather the following information:

**System Inventory:**

- [ ] Complete list of all systems, applications, and services requiring authentication
- [ ] System owners and responsible teams
- [ ] System criticality classification (Tier 0, Tier 1, Tier 2, Standard)

**Authentication Infrastructure:**

- [ ] Identity provider details (Entra ID, Okta, Active Directory, Google Workspace)
- [ ] Authentication protocols in use (SAML, OAuth, Kerberos, LDAP, RADIUS)
- [ ] SSO platform configuration
- [ ] MFA platform details

**Password Policies:**

- [ ] Password policy configurations (AD Group Policy, Entra ID password policy, Okta policy)
- [ ] Password complexity requirements
- [ ] Password expiration settings (if applicable)
- [ ] Password breach detection status

**SSO Integration Status:**

- [ ] Applications integrated with SSO
- [ ] Applications not integrated with SSO (legacy, no SSO support)
- [ ] SSO rollout roadmap

## Required Access

**System Access Needed:**

- [ ] Read access to identity providers (Entra ID, Okta, Active Directory)
- [ ] Read access to authentication configuration (not credentials themselves)
- [ ] Read access to system documentation
- [ ] Access to configuration management database (CMDB) if available

**People Access Needed:**

- [ ] System owners (for authentication configuration details)
- [ ] IT operations teams (for authentication infrastructure)
- [ ] Application teams (for application authentication)

## Required Tools

**Software:**

- [ ] Microsoft Excel 2016 or later (for assessment workbook)
- [ ] Python 3.8+ (if using automated workbook generation scripts)
- [ ] Access to identity provider admin consoles (Entra ID, Okta, etc.)

**Optional Tools:**

- [ ] Configuration management tools (for automated data extraction)
- [ ] SIEM access (for authentication log analysis)
- [ ] PowerShell / Azure CLI / Okta API (for automated data collection)

---

# Assessment Workflow

## Assessment Process Overview

```
1. PREPARE
   â†' Gather prerequisites (system inventory, access, tools)
   â†' Generate workbook (Python script or manual Excel template)
   â†' Assign responsibilities (who inventories which systems)

2. COLLECT DATA
   â†' Sheet 1: Authentication Mechanism Inventory

      - Document each system's authentication method
      - Identify authentication provider and protocol

   â†' Sheet 2: Password Policy Compliance

      - Document password policy per system
      - Verify complexity, expiration, breach detection

   â†' Sheet 3: SSO Integration Status

      - Track SSO adoption by application
      - Identify SSO gaps and roadmap

3. ANALYZE & SCORE
   â†' Automated compliance calculations
   â†' Identify gaps (systems without modern authentication)
   â†' Flag high-risk configurations

4. COLLECT EVIDENCE
   â†' Screenshot authentication configurations
   â†' Export identity provider reports
   â†' Document authentication architecture diagrams

5. REVIEW & APPROVE
   â†' Security Team review (completeness, accuracy)
   â†' System Owner validation (confirm authentication methods)
   â†' CISO approval (formal sign-off)

6. REMEDIATE GAPS
   â†' Address identified authentication security gaps
   â†' Track remediation progress
   â†' Update assessment with improvements
```

## Step-by-Step Completion Guide

**Step 1: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_1_authentication_inventory.py
```
This creates: `ISMS-IMP-A.8.2-3-5.1_Authentication_Inventory_YYYYMMDD.xlsx`

Option B - Manual:

- Use Excel template (provided in ISMS repository)
- Save as: `ISMS-IMP-A.8.2-3-5.1_Authentication_Inventory_[DATE].xlsx`

**Step 2: Complete Sheet 1 - Authentication Mechanism Inventory**

For each system/application/service:

1. **System Identification** (Columns A-D):

   - System ID: Unique identifier (SYS-001, APP-WEB-001, etc.)
   - System Name: Full system name
   - System Type: Dropdown (Web App, Database, API, Network Device, etc.)
   - System Owner: Person/team responsible

2. **Authentication Method** (Columns E-H):

   - Authentication Provider: Where authentication happens (Entra ID, Okta, AD, Local, etc.)
   - Authentication Method: How users authenticate (Password, Password+MFA, SSO, Certificate, API Key, etc.)
   - Authentication Protocol: Technical protocol (SAML 2.0, OAuth 2.0/OIDC, Kerberos, LDAP, etc.)
   - Protocol Version: Specific version if applicable (e.g., TLS 1.3, SAML 2.0)

3. **Security Assessment** (Columns I-L):

   - MFA Required: Yes/No (is MFA enforced for this system?)
   - Password Policy Enforced: Yes/No (if password-based, is policy enforced?)
   - SSO Integrated: Yes/No (is system integrated with SSO platform?)
   - Compliance Status: Auto-calculated (Compliant, Partial, Non-Compliant)

4. **Notes & Evidence** (Columns M-N):

   - Configuration Notes: Brief notes on authentication setup
   - Evidence Location: Link to evidence (screenshot, config export, documentation)

**Step 3: Complete Sheet 2 - Password Policy Compliance**

For each system using password authentication:

1. **Password Requirements** (Columns A-F):

   - System: Reference to Sheet 1
   - Minimum Length: Number of characters required
   - Complexity Required: Yes/No (uppercase, lowercase, numbers, symbols)
   - Password Expiration: Days until expiration (0 = no expiration)
   - Password History: Number of passwords remembered
   - Breach Detection: Yes/No (integration with HaveIBeenPwned or similar)

2. **Compliance Check** (Columns G-H):

   - Policy Compliance: Auto-calculated (meets ISMS-POL-A.8.2-3-5 requirements?)
   - Gap Description: If non-compliant, what's missing?

**Step 4: Complete Sheet 3 - SSO Integration Status**

For each application:

1. **Application Details** (Columns A-D):

   - Application Name
   - Application Owner
   - User Count: Number of users
   - Business Criticality: High/Medium/Low

2. **SSO Status** (Columns E-H):

   - SSO Integrated: Yes/No
   - SSO Platform: Entra ID, Okta, Google, etc.
   - Integration Method: SAML, OIDC, etc.
   - Integration Date: When SSO was implemented

3. **Gap Analysis** (Columns I-K):

   - SSO Support: Yes/No (does application support SSO?)
   - Planned Integration Date: If not integrated, when will it be?
   - Blocking Issue: Why not integrated? (No SSO support, budget, priority, etc.)

**Step 5: Review Calculated Metrics**

The workbook automatically calculates:

- **Overall Authentication Security Score**: Percentage of systems with modern authentication
- **MFA Coverage**: Percentage of systems with MFA enforcement
- **Password Policy Compliance**: Percentage of systems with compliant password policies
- **SSO Adoption**: Percentage of applications integrated with SSO

Review these metrics and validate accuracy.

**Step 6: Collect Evidence**

Required evidence for each system:

- **Authentication Configuration Screenshots**: Identity provider configuration, system authentication settings
- **Identity Provider Reports**: User count, authentication method distribution, MFA enrollment
- **SSO Integration Documentation**: SAML metadata, OAuth configuration, attribute mapping
- **Password Policy Configuration**: Group Policy exports, Entra ID policy screenshots

Store evidence in: `/evidence/authentication/[system_id]/`

**Step 7: Complete Evidence Register (Sheet 4)**

Document all collected evidence:

- Evidence ID, Type, Description, Location, Collection Date

**Step 8: Approval & Sign-Off (Sheet 5)**

Three-level approval process:
1. **Preparer**: Security team member who completed assessment
2. **Reviewer**: Senior security team member or IAM lead
3. **Approver**: CISO (final authority)

---

# Evidence Collection Guidelines

## Required Evidence Types

**For Each System:**

1. **Authentication Method Evidence**:

   - Screenshot of authentication configuration
   - Identity provider user object (redacted credentials)
   - Authentication flow diagram (for complex setups)

2. **Password Policy Evidence**:

   - Group Policy export (for AD-based systems)
   - Entra ID password policy screenshot
   - Application password policy configuration

3. **SSO Integration Evidence**:

   - SAML metadata export
   - OAuth/OIDC application configuration
   - Attribute mapping documentation

## Evidence Storage

**Structure:**
```
/evidence/authentication/
â"œâ"€â"€ SYS-001-EmailServer/
â"'   â"œâ"€â"€ auth-config-screenshot.png
â"'   â"œâ"€â"€ saml-metadata.xml
â"'   â""â"€â"€ password-policy.pdf
â"œâ"€â"€ APP-WEB-001-Intranet/
â"'   â"œâ"€â"€ azure-ad-config.png
â"'   â""â"€â"€ sso-integration-doc.pdf
â""â"€â"€ identity-provider-reports/
    â"œâ"€â"€ azure-ad-auth-methods-report.csv
    â""â"€â"€ okta-user-authentication-report.pdf
```

## Evidence Quality Checklist

For each piece of evidence:

- [ ] Clear and readable (screenshots not blurry)
- [ ] Dated (timestamp visible)
- [ ] Redacted (no passwords, secrets, or sensitive data visible)
- [ ] Linked in workbook (Evidence Register sheet)
- [ ] Stored securely (access-controlled directory)

---

# Common Pitfalls & How to Avoid Them

## Pitfall 1: Incomplete System Inventory

**Problem**: Not all systems inventoried, authentication gaps missed

**Solution**:

- Cross-reference with CMDB (configuration management database)
- Review network diagrams (find network-authenticated devices)
- Check application portfolio (find all web applications)
- Ask system owners: "What authenticates to your system?"

## Pitfall 2: Confusing Authentication Method vs. Protocol

**Problem**: Mixing up high-level method (SSO) with low-level protocol (SAML)

**Correct Documentation**:

- Authentication Method: "SSO" or "Password + MFA"
- Authentication Protocol: "SAML 2.0" or "OAuth 2.0/OIDC"

**Example**:

- System: "Corporate Intranet"
- Authentication Method: "SSO"
- Authentication Provider: "Entra ID"
- Authentication Protocol: "SAML 2.0"

## Pitfall 3: Assuming All Entra ID Users Have MFA

**Problem**: Entra ID subscription does not automatically mean MFA is enforced

**Solution**:

- Check Conditional Access policies (Entra ID Premium P1/P2)
- Verify MFA enforcement per application
- Use IMP.2 (MFA Coverage Assessment) to validate actual MFA enrollment

## Pitfall 4: Missing Legacy Systems

**Problem**: Old systems (VPN, database, network device) forgotten in inventory

**Solution**:

- Check network device authentication (switches, routers - TACACS+, RADIUS)
- Check VPN authentication (IPsec, SSL VPN)
- Check database authentication (SQL Server, Oracle, PostgreSQL)
- Check file server authentication (SMB/CIFS, NFS)

## Pitfall 5: Not Tracking SSO Gaps

**Problem**: Knowing an application doesn't have SSO, but not tracking WHY or WHEN it will be fixed

**Solution**:

- Document blocking issue: "Application vendor doesn't support SAML"
- Document remediation plan: "Migrate to alternative SaaS app with SSO by Q3 2026"
- Track in SSO Integration Status sheet

## Pitfall 6: Redacting Too Much

**Problem**: Evidence so heavily redacted it's not useful for audit

**Solution**:

- Redact passwords, secrets, API keys (YES)
- Redact usernames, system names, configuration details (NO - these are needed for audit)

## Pitfall 7: Not Validating with System Owners

**Problem**: Security team documents authentication method incorrectly

**Solution**:

- Share draft assessment with system owners
- Ask: "Is this authentication configuration correct?"
- Get confirmation before final approval

## Pitfall 8: Forgetting Service Accounts

**Problem**: Only inventorying interactive user authentication, missing service account authentication

**Solution**:

- Check service account authentication (API keys, certificates, OAuth client credentials)
- Document in Authentication Mechanism Inventory
- Note: Service account privilege is tracked in IMP.3 (Privileged Account Inventory)

## Pitfall 9: Not Updating Monthly

**Problem**: Assessment becomes stale, doesn't reflect current state

**Solution**:

- Set calendar reminder: "Update authentication inventory - 1st of every month"
- Integrate with change management: "New system deployed? Update authentication inventory."

## Pitfall 10: Checkbox Compliance Without Understanding

**Problem**: Filling in workbook without understanding authentication security

**Solution**:

- Read ISMS-POL-A.8.2-3-5 Section 2.1 (Authentication Requirements) FIRST
- Understand WHY MFA matters, WHY SSO reduces risk
- This is EVIDENCE-DRIVEN SECURITY, not checkbox compliance

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All known systems inventoried (cross-checked with CMDB)
- [ ] All authentication mechanisms documented (no "TBD" or blank fields)
- [ ] All password policies documented (for password-based systems)
- [ ] All SSO status documented (for web applications)
- [ ] All evidence collected and linked

## Accuracy

- [ ] Authentication methods validated with system owners
- [ ] Password policies verified (not assumed)
- [ ] SSO integration status confirmed (tested login)
- [ ] Calculated metrics reviewed (make sense?)

## Evidence Quality

- [ ] All evidence redacted properly (no passwords visible)
- [ ] All evidence dated (timestamps visible)
- [ ] All evidence linked in Evidence Register
- [ ] Evidence storage location documented

## Compliance

- [ ] Systems without MFA identified and tracked
- [ ] Systems without password policy compliance identified
- [ ] Applications without SSO identified with remediation plan
- [ ] High-risk authentication gaps flagged for immediate remediation

## Professional Presentation

- [ ] No spelling errors
- [ ] Consistent formatting (dates in DD.MM.YYYY format)
- [ ] Clear and concise notes
- [ ] Proper capitalization and grammar

---

# Interpreting Results

## Understanding Compliance Scores

**Overall Authentication Security Score**:

- **90-100%**: Excellent - Modern authentication across nearly all systems
- **75-89%**: Good - Most systems have modern authentication, some legacy gaps
- **60-74%**: Moderate - Significant legacy authentication, modernization needed
- **<60%**: Poor - Major authentication security gaps, immediate action required

**MFA Coverage**:

- **100%**: All systems enforce MFA (ideal state)
- **80-99%**: Most systems have MFA, some exceptions (acceptable with documented compensating controls)
- **<80%**: Insufficient MFA coverage (high risk)

**SSO Adoption**:

- **80-100%**: Most applications integrated (ideal state)
- **60-79%**: Good progress, continue SSO rollout
- **<60%**: Low SSO adoption (password sprawl risk)

## Gap Prioritization

**Priority 1 - Critical (Immediate Action)**:

- Systems without MFA that handle Tier 0 data (domain controllers, PKI, etc.)
- Systems with weak password policies (length <12, no breach detection)
- Systems using deprecated authentication protocols (NTLM v1, Telnet, FTP)

**Priority 2 - High (Within 90 Days)**:

- Systems without MFA that handle Confidential data
- Applications without SSO (high user count, frequent logins)
- Systems with password expiration (migrate to no-expiration + MFA)

**Priority 3 - Medium (Within 180 Days)**:

- Applications without SSO (moderate user count)
- Systems with suboptimal password policies (expiration but compliant length/complexity)

**Priority 4 - Low (Ongoing Improvement)**:

- Legacy systems scheduled for decommissioning
- Systems with documented exceptions and compensating controls

---

# Review & Approval Process

## Approval Workflow

**Level 1 - Preparer (Security Team)**:

- Complete assessment workbook
- Collect evidence
- Perform initial quality check
- Submit for review

**Level 2 - Reviewer (Senior Security / IAM Lead)**:

- Validate completeness and accuracy
- Spot-check evidence
- Verify compliance calculations
- Request corrections if needed
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:

- Review summary metrics
- Validate critical gaps identified
- Approve remediation priorities
- Sign off on assessment
- Present to Executive Management (if required)

## Approval Criteria

Assessment is approved when:

- [ ] All sections complete (no blank fields without justification)
- [ ] Evidence collected and linked
- [ ] System owners validated authentication methods
- [ ] Compliance scores calculated and reviewed
- [ ] Critical gaps identified and prioritized
- [ ] Remediation plan documented

## Post-Approval Actions

After CISO approval:
1. **Archive Assessment**: Store approved version in ISMS repository
2. **Communicate Gaps**: Notify system owners of authentication security gaps
3. **Track Remediation**: Move gaps to remediation tracking (Sheet 4 in Dashboard IMP.6)
4. **Schedule Next Review**: Set calendar reminder for monthly update / quarterly review

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
