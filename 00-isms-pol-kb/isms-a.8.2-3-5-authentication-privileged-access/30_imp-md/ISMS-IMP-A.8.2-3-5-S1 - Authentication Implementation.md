# ISMS-IMP-A.8.2-3-5-S1
## Authentication Implementation Guide

**Document ID**: ISMS-IMP-A.8.2-3-5-S1  
**Title**: Authentication Architecture and Implementation  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Identity & Access Management Lead  
**Status**: Draft

---

## 1. Implementation Overview

**Purpose**: Practical guidance for implementing authentication architecture aligned with A.8.5 requirements.

**Scope**: 
- Authentication platform selection and deployment
- Authentication protocol configuration
- SSO platform deployment
- Password policy implementation

**Target Audience**: IAM team, IT operations, security architects

---

## 2. Authentication Architecture Design

### 2.1 Architecture Decision Points

**Key Decisions**:
1. **On-premises vs. Cloud vs. Hybrid** authentication
2. **Identity provider selection** (Azure AD, Okta, Google Workspace, AD)
3. **Authentication protocols** (SAML, OAuth/OIDC, Kerberos)
4. **MFA platform** (native or third-party)

### 2.2 Common Architecture Patterns

**Pattern 1: Pure Cloud (Small-Medium Organizations)**
```
Users → Azure AD / Okta / Google Workspace → SaaS Apps
- Authentication: Cloud-native (Azure AD, Okta)
- MFA: Built-in (Azure MFA, Okta MFA)
- SSO: SAML/OIDC to SaaS apps
- Best for: <500 users, cloud-first, no on-prem infrastructure
```

**Pattern 2: Hybrid (Large Organizations)**
```
Users → Azure AD Connect / Okta AD Agent
        ↓
        On-premises AD ← → Azure AD / Okta
        ↓                    ↓
    On-prem Apps         Cloud SaaS Apps
- Authentication: AD for on-prem, Azure AD/Okta for cloud
- MFA: Centralized (Azure MFA, Okta MFA for all)
- SSO: Federated (on-prem apps via AD FS, cloud apps via Azure AD/Okta)
- Best for: >500 users, existing AD investment, hybrid apps
```

**Pattern 3: Pure On-Premises (Legacy/High-Security)**
```
Users → Active Directory → AD FS → Apps
- Authentication: On-premises AD
- MFA: Third-party (Duo, RSA) or AD FS MFA
- SSO: AD FS for web apps
- Best for: Air-gapped, highly regulated, government
```

### 2.3 Platform Selection Criteria

| Criteria | Azure AD | Okta | Google Workspace | On-Prem AD |
|----------|----------|------|------------------|------------|
| **Cost** | $$$ (per user/month) | $$$ | $$ | $ (infrastructure only) |
| **Deployment** | Fast (days) | Fast (days) | Fast (days) | Slow (weeks-months) |
| **MFA Built-in** | Yes (excellent) | Yes (excellent) | Yes (good) | No (add-on required) |
| **App Catalog** | 4500+ | 7000+ | 1000+ | Limited |
| **API Integration** | Excellent | Excellent | Good | Limited |
| **Best For** | Microsoft shops | Multi-cloud | Google shops | Legacy/air-gapped |

---

## 3. Authentication Protocol Implementation

### 3.1 SAML 2.0 Configuration

**Use Case**: Enterprise SSO for web applications

**Implementation Steps**:
1. **Identity Provider (IdP) Setup**:
   - Configure SAML app in Azure AD/Okta
   - Generate signing certificate (validity: 2-3 years)
   - Define user attributes to send (email, name, groups)
   
2. **Service Provider (SP) Configuration**:
   - Obtain SP metadata URL from application
   - Configure Assertion Consumer Service (ACS) URL
   - Configure Entity ID
   - Upload IdP certificate to application

3. **Attribute Mapping**:
   ```
   IdP Attribute → SP Attribute
   user.email → email
   user.givenName → firstName
   user.surname → lastName
   user.department → department
   user.groups → roles
   ```

4. **Testing**:
   - Test user login (initiate from IdP and from SP)
   - Verify attributes received correctly
   - Test logout (single logout if supported)

**Common Issues**:
- Clock skew (sync time on IdP and SP, max 5 min difference)
- Certificate expiration (monitor 30 days before expiry)
- Attribute case sensitivity (SP expects "email", IdP sends "Email")

### 3.2 OAuth 2.0 / OpenID Connect Configuration

**Use Case**: Modern authentication for APIs and mobile apps

**OAuth 2.0 Flows**:
- **Authorization Code Flow**: User-facing web apps (most secure)
- **Client Credentials Flow**: Server-to-server APIs (no user involved)
- **Implicit Flow**: DEPRECATED (use Auth Code + PKCE instead)

**OIDC Implementation (Auth Code Flow)**:
1. **Register Application**:
   - Register app in Azure AD/Okta
   - Configure redirect URIs (https://app.example.com/callback)
   - Generate client ID and client secret
   
2. **Authorization Request**:
   ```
   GET https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize
   ?client_id={client_id}
   &response_type=code
   &redirect_uri={redirect_uri}
   &scope=openid profile email
   &state={random_state}
   &nonce={random_nonce}
   ```

3. **Token Exchange**:
   ```
   POST https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
   client_id={client_id}
   &client_secret={client_secret}
   &code={authorization_code}
   &redirect_uri={redirect_uri}
   &grant_type=authorization_code
   ```

4. **ID Token Validation**:
   - Verify signature (using JWKS endpoint)
   - Verify issuer (iss claim)
   - Verify audience (aud claim = client_id)
   - Verify expiration (exp claim)
   - Verify nonce matches

**Security Best Practices**:
- Always use PKCE (Proof Key for Code Exchange) for public clients
- Store client secrets securely (Azure Key Vault, environment variables)
- Validate state parameter (CSRF protection)
- Use short-lived access tokens (1 hour max)
- Use refresh tokens for long-lived sessions

---

## 4. Single Sign-On (SSO) Platform Deployment

### 4.1 SSO Platform Selection

**Azure AD (Microsoft Entra ID)**:
- **Best for**: Organizations using Microsoft 365
- **Strengths**: Tight Office 365 integration, Conditional Access, PIM
- **MFA**: Built-in Azure MFA (excellent)
- **Licensing**: Azure AD P1 ($6/user/month), P2 ($9/user/month)

**Okta**:
- **Best for**: Multi-cloud, heterogeneous environments
- **Strengths**: Largest app catalog (7000+ apps), excellent APIs
- **MFA**: Built-in Okta MFA (excellent)
- **Licensing**: Workforce Identity ($2-8/user/month), depends on features

**Google Workspace**:
- **Best for**: Organizations using Google services
- **Strengths**: Simple, Google ecosystem integration
- **MFA**: Built-in 2-Step Verification (good)
- **Licensing**: Business Starter ($6/user/month), Business Plus ($18/user/month)

### 4.2 SSO Deployment Phases

**Phase 1: Platform Setup (Weeks 1-2)**
- Provision SSO platform tenant
- Configure directory sync (Azure AD Connect, Okta AD Agent)
- Import users from source directory
- Configure MFA policies (enforce MFA for admins first)

**Phase 2: Pilot Deployment (Weeks 3-4)**
- Select 3-5 pilot applications (low-risk, high-value)
- Configure SSO integrations (SAML/OIDC)
- Test with pilot user group (10-20 users)
- Collect feedback and refine

**Phase 3: Rollout to All Apps (Months 2-6)**
- Prioritize applications by usage (integrate high-usage apps first)
- Configure SSO for each application (target: 5-10 apps per month)
- Communicate to users (training, documentation)
- Monitor adoption (% of authentications via SSO)

**Phase 4: Decommission Legacy Auth (Month 7+)**
- Identify apps still using local passwords
- Migrate or retire apps not supporting SSO
- Disable legacy authentication methods (Basic Auth, NTLM)

### 4.3 Application SSO Integration

**Pre-built Integrations** (fastest):
- Use app gallery (Azure AD Enterprise Apps, Okta App Catalog)
- Example: Salesforce, Slack, ServiceNow, AWS, GitHub
- Configuration time: 15-30 minutes per app

**Custom SAML Integration** (moderate effort):
- Obtain SAML metadata from application
- Configure in SSO platform (manual attribute mapping)
- Configuration time: 1-2 hours per app

**No SSO Support** (legacy apps):
- Option 1: Use password vaulting (Okta Secure Web Authentication)
- Option 2: Use reverse proxy (Azure AD Application Proxy)
- Option 3: Retire application (if possible)

---

## 5. Password Policy Implementation

### 5.1 Modern Password Policy Configuration

**Active Directory Group Policy**:
```
Computer Configuration → Policies → Windows Settings → 
Security Settings → Account Policies → Password Policy

Minimum password length: 12 characters
Password must meet complexity requirements: Enabled
Maximum password age: 0 (disabled - no expiration)
Minimum password age: 1 day
Enforce password history: 5 passwords remembered
```

**Azure AD Password Policy**:
```
Azure AD → Security → Authentication methods → 
Password protection

Custom banned password list: 
- Company name variants
- Product names
- Common passwords (password, welcome, etc.)

Password protection for Windows Server Active Directory:
- Enabled (syncs banned list to on-prem AD)

Lockout threshold: 10 failed attempts
Lockout duration: 10 minutes
```

**Okta Password Policy**:
```
Security → Authentication → Password

Minimum length: 12 characters
Character requirements: At least 3 of 4 types
Password age: No expiration
Password history: 5 passwords
Exclude username: Enabled
Exclude first name: Enabled
Exclude last name: Enabled
```

### 5.2 Password Breach Detection

**Azure AD Password Protection**:
- Automatically enabled for Azure AD
- Checks passwords against Microsoft breach database
- Blocks known-breached passwords
- Custom banned password list (organization-specific terms)

**Okta Compromised Credential Detection**:
- Automatically enabled
- Checks against Have I Been Pwned database
- Forces password reset if breach detected

**On-Premises AD (Manual Integration)**:
- Use PowerShell module: `Test-PasswordAgainstHaveIBeenPwned`
- Schedule weekly password audit
- Force reset for compromised passwords

---

## 6. Implementation Checklist

### 6.1 Authentication Platform Deployment

**Pre-Deployment**:
- [ ] Architecture decision made (cloud, hybrid, on-prem)
- [ ] Platform selected (Azure AD, Okta, Google, AD)
- [ ] Licensing procured
- [ ] Project team assigned (IAM lead, architect, engineers)

**Initial Setup**:
- [ ] Tenant provisioned
- [ ] Directory sync configured (if hybrid)
- [ ] User import completed and verified
- [ ] Admin accounts configured with MFA
- [ ] Break-glass accounts created and secured

**SSO Configuration**:
- [ ] Pilot applications identified (3-5 apps)
- [ ] SSO integrations configured and tested
- [ ] User testing completed successfully
- [ ] Rollout plan created (prioritize by app usage)

**Password Policy**:
- [ ] Modern password policy configured (12+ chars, no expiration)
- [ ] Breach detection enabled
- [ ] Custom banned password list created
- [ ] Policy applied and verified

**MFA Deployment** (see IMP-S2):
- [ ] MFA platform configured
- [ ] Pilot group enrolled
- [ ] Full rollout planned

**Monitoring**:
- [ ] Authentication logs forwarded to SIEM
- [ ] Failed authentication alerts configured
- [ ] SSO adoption metrics dashboard created

---

## 7. Common Implementation Challenges

### 7.1 Challenge: Legacy Applications Without SSO Support

**Problem**: Application built 10+ years ago, no SAML/OAuth support

**Solutions**:
1. **Password Vaulting** (Okta Secure Web Authentication):
   - SSO platform stores app credentials
   - Auto-fills username/password on login page
   - Pro: Works with any app, Con: Still uses passwords

2. **Reverse Proxy** (Azure AD Application Proxy):
   - Proxy provides authentication layer before app
   - User authenticates to Azure AD, proxy passes to app
   - Pro: Modern auth, Con: Requires agent installation

3. **Application Upgrade**:
   - Contact vendor for SSO support
   - Implement custom SAML in app (if source available)
   - Pro: Proper solution, Con: Expensive/time-consuming

4. **Application Retirement**:
   - Replace with modern alternative
   - Pro: Removes technical debt, Con: Business process change

### 7.2 Challenge: Directory Sync Conflicts

**Problem**: User exists in both AD and Azure AD with different attributes

**Solutions**:
- Use Azure AD Connect matching rules (match by UPN or objectGUID)
- Soft-match users (manual attribute mapping)
- Hard-match users (set ImmutableID attribute)

### 7.3 Challenge: MFA Fatigue and User Resistance

**Problem**: Users complain MFA is inconvenient

**Solutions**:
- Use remember MFA on trusted devices (30-90 days)
- Deploy authenticator app push (easier than typing codes)
- Implement risk-based MFA (Conditional Access - only challenge on unusual login)
- User training (explain why MFA matters - real breach examples)

---

**END OF IMPLEMENTATION GUIDE S1**

**Next**: IMP-S2 (MFA Deployment)
