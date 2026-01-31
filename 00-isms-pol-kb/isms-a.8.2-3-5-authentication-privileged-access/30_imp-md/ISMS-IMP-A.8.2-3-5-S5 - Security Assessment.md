# ISMS-IMP-A.8.2-3-5-S5
## Security Assessment Implementation Guide

**Document ID**: ISMS-IMP-A.8.2-3-5-S5  
**Title**: Authentication & PAM Security Assessment Procedures  
**Version**: 1.0  
**Classification**: Internal  
**Owner**: Security Assessment Lead

---

## 1. Quarterly Assessment Execution

### 1.1 Data Collection Schedule

**Week 1: Export Data from Systems**:
```bash
# Day 1-2: Identity provider exports
az ad user list --output json > azure-ad-users.json
az ad group member list --group "Domain Admins" > domain-admins.json

# Day 3-4: MFA enrollment data
# Azure AD MFA Report (via Azure Portal → Users → Per-user MFA)
# Okta: Reports → MFA Enrollment

# Day 5: PAM solution exports
# CyberArk: Export vaulted accounts, session logs
# BeyondTrust: Export privileged access activity

# Day 6-7: Configuration scans
# Run CIS benchmark scans
# Export firewall rules, permission audits
```

### 1.2 Workbook Population

**Workbook 1 - Authentication Inventory**:
```python
# Populate from identity provider API
import pandas as pd

# Load application catalog
apps = get_sso_applications()  # Azure AD/Okta API
inventory = []

for app in apps:
  inventory.append({
    'System': app['name'],
    'Auth Method': app['signOnMode'],  # SAML, OAuth, password
    'SSO Integrated': 'Yes' if app['signOnMode'] in ['SAML', 'OAuth'] else 'No',
    'MFA Available': 'Yes' if app['mfaRequired'] else 'No'
  })

df = pd.DataFrame(inventory)
df.to_excel('Workbook-1-Auth-Inventory.xlsx')
```

**Workbook 2 - MFA Coverage**:
```python
# Calculate MFA coverage by user type
users = get_all_users()  # AD/Azure AD API
privileged_users = get_privileged_users()  # From privileged groups

mfa_enrolled = [u for u in users if u['mfaEnabled']]
priv_with_mfa = [u for u in privileged_users if u['mfaEnabled']]

metrics = {
  'Privileged MFA %': len(priv_with_mfa) / len(privileged_users) * 100,
  'Overall MFA %': len(mfa_enrolled) / len(users) * 100
}
```

---

## 2. Authentication Security Testing

### 2.1 Password Policy Compliance Check

**Test Script**:
```python
import activedirectory  # Example library

policy = activedirectory.get_password_policy()

checks = {
  'Min Length ≥12': policy['minLength'] >= 12,
  'Complexity Required': policy['complexityEnabled'],
  'No Expiration': policy['maxAge'] == 0 or policy['maxAge'] >= 90,
  'History ≥5': policy['historyCount'] >= 5
}

compliance = sum(checks.values()) / len(checks) * 100
print(f"Password Policy Compliance: {compliance}%")
```

### 2.2 Legacy Authentication Detection

**Query Failed Authentications**:
```sql
-- Azure AD Sign-in Logs
SELECT 
  UserPrincipalName,
  AppDisplayName,
  ClientAppUsed,  -- Look for "Exchange ActiveSync", "IMAP", "POP"
  AuthenticationProtocol
FROM SigninLogs
WHERE ClientAppUsed IN ('Exchange ActiveSync', 'IMAP', 'POP', 'SMTP', 'Other clients')
  AND TimeGenerated > ago(30d)
GROUP BY UserPrincipalName, AppDisplayName
```

---

## 3. Privileged Access Assessment

### 3.1 Privileged Account Discovery

**PowerShell Script**:
```powershell
# Find all Domain Admins
$DomainAdmins = Get-ADGroupMember "Domain Admins" -Recursive

# Find all Enterprise Admins
$EnterpriseAdmins = Get-ADGroupMember "Enterprise Admins" -Recursive

# Export to CSV
$DomainAdmins | Select-Object Name,SamAccountName,DistinguishedName | 
  Export-Csv "Domain-Admins.csv"
```

### 3.2 PAM Coverage Assessment

**Check Which Accounts Are Vaulted**:
```python
# Get privileged accounts from AD
privileged_accounts = get_privileged_accounts()

# Get vaulted accounts from PAM
vaulted_accounts = pam_api.get_vaulted_accounts()

# Calculate coverage
vaulted_names = [a['name'] for a in vaulted_accounts]
coverage = sum(1 for acc in privileged_accounts if acc in vaulted_names)
coverage_pct = coverage / len(privileged_accounts) * 100

print(f"PAM Vault Coverage: {coverage_pct}%")
```

### 3.3 Tier Isolation Compliance Check

**Detect Cross-Tier Logins**:
```sql
-- Windows Event Logs (Event ID 4624 - Successful Logon)
SELECT 
  TargetUserName,
  ComputerName,
  TimeCreated
FROM SecurityEvent
WHERE EventID = 4624
  AND TargetUserName IN (SELECT UserName FROM Tier0Admins)
  AND ComputerName NOT IN (SELECT ComputerName FROM PAWs)
-- Result: Tier 0 accounts logging into non-PAW devices = VIOLATION
```

---

## 4. Access Control Testing

### 4.1 Permission Audit Scripts

**Windows File Permissions**:
```powershell
# Audit sensitive directories
$sensitivePaths = @("D:\Finance", "D:\HR", "D:\Legal")

foreach ($path in $sensitivePaths) {
  $acl = Get-Acl $path
  $acl.Access | Where-Object {
    $_.IdentityReference -eq "Everyone" -and $_.FileSystemRights -match "Write|FullControl"
  } | ForEach-Object {
    Write-Warning "FINDING: Everyone has write access to $path"
  }
}
```

**Database Permission Audit**:
```sql
-- Find users with db_owner (excessive privilege)
SELECT 
  dp.name AS UserName,
  dp.type_desc
FROM sys.database_role_members drm
JOIN sys.database_principals dp ON drm.member_principal_id = dp.principal_id
WHERE drm.role_principal_id = (SELECT principal_id FROM sys.database_principals WHERE name = 'db_owner')
```

### 4.2 Penetration Testing

**Access Control Bypass Tests**:
```
Test 1: Horizontal Privilege Escalation
- User A logs in, accesses /api/users/123 (their own profile)
- User A tries /api/users/456 (User B's profile)
- Expected: 403 Forbidden
- Finding: If 200 OK → IDOR vulnerability

Test 2: Vertical Privilege Escalation
- Standard user logs in
- Standard user tries /api/admin/delete-user
- Expected: 403 Forbidden or 401 Unauthorized
- Finding: If 200 OK → privilege escalation vulnerability

Test 3: File Traversal
- User uploads file to /uploads/user123/file.jpg
- User tries to access /uploads/../../../etc/passwd
- Expected: 403 Forbidden or sanitized path
- Finding: If /etc/passwd returned → path traversal vulnerability
```

---

## 5. Continuous Monitoring Setup

### 5.1 SIEM Alert Configuration

**Authentication Alerts** (Splunk/Datadog):
```
Alert: "Brute Force Attack"
Query: 
  source=authentication_logs 
  | stats count by src_ip, user 
  | where count > 10
Trigger: More than 10 failed logins from same IP in 5 minutes
Action: Block IP, alert security team
```

**Privileged Access Alerts**:
```
Alert: "Tier 0 Account Activity"
Query: 
  source=privileged_access_logs 
  | search user IN (tier0_admins)
Trigger: ANY Tier 0 account login
Action: Alert security team (informational)

Alert: "Tier Isolation Violation - CRITICAL"
Query:
  source=privileged_access_logs
  | join user tier0_admins
  | search computer NOT IN (PAW_list)
Trigger: Tier 0 account logging into non-PAW device
Action: Terminate session, critical alert, investigate immediately
```

### 5.2 Automated Compliance Dashboards

**Real-Time Dashboards**:
```python
# Daily refresh: MFA enrollment status
def update_mfa_dashboard():
  users = get_all_users()
  privileged = get_privileged_users()
  
  dashboard_data = {
    'total_users': len(users),
    'mfa_enrolled': sum(1 for u in users if u['mfaEnabled']),
    'privileged_total': len(privileged),
    'privileged_mfa': sum(1 for u in privileged if u['mfaEnabled']),
    'mfa_coverage_pct': sum(1 for u in users if u['mfaEnabled']) / len(users) * 100,
    'privileged_mfa_pct': sum(1 for u in privileged if u['mfaEnabled']) / len(privileged) * 100
  }
  
  publish_to_dashboard(dashboard_data)
```

---

## 6. Evidence Collection for Audits

### 6.1 ISO 27001 Audit Evidence Package

**For A.8.5 (Authentication)**:
```
Evidence Package:
├── POL-S2-Secure-Authentication.pdf (policy)
├── Workbook-1-Auth-Inventory.xlsx (authentication mechanisms)
├── Workbook-2-MFA-Coverage.xlsx (MFA enrollment metrics)
├── Screenshots/
│   ├── Azure-MFA-Settings.png
│   ├── Conditional-Access-Policies.png
│   └── Password-Policy-GPO.png
└── Logs/
    ├── Authentication-Logs-Sample.csv (30 days)
    └── MFA-Enrollment-Events.csv
```

**For A.8.2 (Privileged Access)**:
```
Evidence Package:
├── POL-S3-Privileged-Access.pdf (policy)
├── Workbook-3-Privileged-Accounts.xlsx (account inventory, tier classification)
├── Workbook-4-Privileged-Monitoring.xlsx (activity logs, reviews)
├── Screenshots/
│   ├── PAM-Vault-Configuration.png
│   ├── Session-Recording-Sample.mp4 (redacted)
│   └── Tier-Isolation-GPO.png
└── Attestations/
    ├── Q1-2024-Privileged-Access-Review.pdf (manager attestations)
    └── Q2-2024-Privileged-Access-Review.pdf
```

**For A.8.3 (Access Restriction)**:
```
Evidence Package:
├── POL-S4-Access-Restriction.pdf (policy)
├── Workbook-5-Access-Restrictions.xlsx (permission audits, encryption status)
├── Penetration-Test-Report-2024.pdf (access control testing)
├── Screenshots/
│   ├── File-Permissions-Sample.png
│   ├── Database-Grants-Sample.png
│   └── Cloud-IAM-Policies.png
└── Config-Scans/
    ├── CIS-Benchmark-Windows-Server.pdf
    └── CIS-Benchmark-Linux.pdf
```

---

## 7. Remediation Tracking

### 7.1 Gap Remediation Workflow

**Gap Identified → Remediation Process**:
```
1. Gap Detected: 5 privileged users without MFA
   - Priority: CRITICAL (privileged access without MFA = high risk)
   - Deadline: 7 days
   - Owner: IAM Lead

2. Remediation Plan Created:
   - Contact 5 users
   - Provide MFA enrollment instructions
   - Schedule enrollment assistance if needed

3. Remediation Executed:
   - Day 1-3: Users notified
   - Day 4-5: 3 users enrolled successfully
   - Day 6: Follow-up with 2 remaining users
   - Day 7: All 5 users enrolled ✅

4. Verification:
   - Re-run MFA coverage assessment
   - Confirm 100% privileged user MFA coverage
   - Update dashboard

5. Closure:
   - Gap marked as CLOSED
   - Evidence collected (enrollment logs)
```

### 7.2 Remediation Metrics

**Track Remediation Effectiveness**:
| Metric | Target | Current |
|--------|--------|---------|
| Critical gaps remediated within 30 days | 100% | 95% |
| High gaps remediated within 90 days | 100% | 90% |
| Average remediation time (critical) | <30 days | 25 days |
| Overdue remediations | 0 | 2 |

---

**END OF IMPLEMENTATION GUIDE S5**

**Implementation guides complete. Next: Python assessment scripts.**
