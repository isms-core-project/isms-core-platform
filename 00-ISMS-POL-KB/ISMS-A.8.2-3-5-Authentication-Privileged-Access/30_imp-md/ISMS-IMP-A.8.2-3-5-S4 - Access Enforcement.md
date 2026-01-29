# ISMS-IMP-A.8.2-3-5-S4
## Access Enforcement Implementation Guide

**Document ID**: ISMS-IMP-A.8.2-3-5-S4  
**Title**: Technical Access Control Implementation  
**Version**: 1.0  
**Classification**: Internal  
**Owner**: Systems Administration Lead

---

## 1. File System Permission Implementation

### 1.1 Windows NTFS Permissions

**Standard Permission Template**:
```powershell
# Remove Everyone group
$acl = Get-Acl "D:\Shared\Finance"
$acl.Access | Where-Object {$_.IdentityReference -eq "Everyone"} | ForEach-Object {$acl.RemoveAccessRule($_)}

# Add specific group with specific rights
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("DOMAIN\Finance-Team","ReadAndExecute","Allow")
$acl.SetAccessRule($rule)
Set-Acl "D:\Shared\Finance" $acl
```

**Audit File Permissions**:
```powershell
# Export current permissions to CSV
Get-ChildItem "D:\Shared" -Recurse | ForEach-Object {
  Get-Acl $_.FullName | Select-Object Path,Owner,AccessToString
} | Export-Csv permissions-audit.csv
```

### 1.2 Linux ACL Management

**Standard Permissions**:
```bash
# Sensitive data: 600 (rw-------)
chmod 600 /data/sensitive/passwords.txt

# Shared team directory: 770 (rwxrwx---)
chmod 770 /data/shared/finance
chown :finance-team /data/shared/finance
```

**Extended ACLs**:
```bash
# Grant specific user access
setfacl -m u:john.doe:rx /data/shared/hr

# Remove ACL
setfacl -x u:john.doe /data/shared/hr

# View ACLs
getfacl /data/shared/hr
```

---

## 2. Database Access Control Implementation

### 2.1 SQL Server Permissions

**Create Application Account**:
```sql
-- Create login
CREATE LOGIN app_crm_user WITH PASSWORD = 'GeneratedPassword123!';

-- Create database user
USE CRM_Database;
CREATE USER app_crm_user FOR LOGIN app_crm_user;

-- Grant specific permissions (NOT db_owner)
GRANT SELECT, INSERT, UPDATE ON dbo.Customers TO app_crm_user;
GRANT SELECT ON dbo.Products TO app_crm_user;
-- Note: No DELETE, no DDL privileges
```

**Audit Database Permissions**:
```sql
-- List all database permissions
SELECT 
  dp.name AS UserName,
  dp.type_desc AS UserType,
  o.name AS ObjectName,
  p.permission_name,
  p.state_desc
FROM sys.database_permissions p
JOIN sys.database_principals dp ON p.grantee_principal_id = dp.principal_id
LEFT JOIN sys.objects o ON p.major_id = o.object_id
ORDER BY dp.name, o.name;
```

### 2.2 PostgreSQL Permissions

**Grant Specific Privileges**:
```sql
-- Create role
CREATE ROLE app_user LOGIN PASSWORD 'GeneratedPassword123!';

-- Grant schema access
GRANT USAGE ON SCHEMA public TO app_user;

-- Grant table-specific permissions
GRANT SELECT, INSERT, UPDATE ON public.customers TO app_user;
GRANT SELECT ON public.products TO app_user;

-- Revoke all other privileges
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM app_user;
```

---

## 3. Application RBAC Implementation

### 3.1 Role-Permission Matrix

**Example for CRM Application**:
| Role | View Customers | Edit Customers | Delete Customers | View Reports | Export Data |
|------|----------------|----------------|------------------|--------------|-------------|
| Sales Rep | ✅ Own only | ✅ Own only | ❌ | ✅ Own only | ❌ |
| Sales Manager | ✅ Team only | ✅ Team only | ❌ | ✅ Team only | ✅ Team only |
| Admin | ✅ All | ✅ All | ✅ | ✅ All | ✅ All |

**Implementation** (example pseudo-code):
```python
def can_user_edit_customer(user, customer):
  if user.role == "Admin":
    return True
  elif user.role == "Sales Manager":
    return customer.owner in user.team_members
  elif user.role == "Sales Rep":
    return customer.owner == user.id
  else:
    return False
```

---

## 4. API Access Control Implementation

### 4.1 OAuth 2.0 Scope Definition

**Define API Scopes**:
```
read:customers    - Read customer data
write:customers   - Create/update customers
delete:customers  - Delete customers (high-risk)
read:orders       - Read order data
write:orders      - Create/update orders
admin:all         - Full administrative access
```

**Assign Scopes to Clients**:
```json
{
  "client_id": "crm-mobile-app",
  "allowed_scopes": ["read:customers", "read:orders"],
  "client_secret": "..."
}
```

**Validate Scopes in API**:
```python
@app.route('/api/customers/<id>', methods=['DELETE'])
@require_scope('delete:customers')
def delete_customer(id):
  # Only executed if token has delete:customers scope
  customer = Customer.query.get(id)
  db.session.delete(customer)
  db.session.commit()
  return {"status": "deleted"}
```

### 4.2 API Rate Limiting

**Implement Rate Limiting**:
```python
from flask_limiter import Limiter

limiter = Limiter(
  app,
  key_func=lambda: request.headers.get('X-API-Key'),
  default_limits=["1000 per hour", "10 per second"]
)

@app.route('/api/search')
@limiter.limit("100 per minute")
def search():
  # Limited to 100 requests per minute per API key
  return perform_search(request.args.get('q'))
```

---

## 5. Cloud IAM Implementation

### 5.1 AWS IAM Least Privilege

**Create Specific IAM Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-*",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Environment": "Production"
        }
      }
    }
  ]
}
```

**Avoid Wildcard Permissions**:
```json
// ❌ BAD - Overly permissive
{"Action": "s3:*", "Resource": "*"}

// ✅ GOOD - Specific permissions
{"Action": ["s3:GetObject", "s3:PutObject"], 
 "Resource": "arn:aws:s3:::my-bucket/*"}
```

### 5.2 Azure RBAC Custom Roles

**Create Custom Role**:
```json
{
  "Name": "VM Operator",
  "Description": "Can start/stop VMs but not delete",
  "Actions": [
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/powerOff/action"
  ],
  "NotActions": [
    "Microsoft.Compute/virtualMachines/delete"
  ],
  "AssignableScopes": ["/subscriptions/{subscription-id}"]
}
```

---

## 6. Encryption Implementation

### 6.1 File Encryption (BitLocker)

**Enable BitLocker on Windows**:
```powershell
# Enable BitLocker on C: drive
Enable-BitLocker -MountPoint "C:" -EncryptionMethod Aes256 -UsedSpaceOnly -TpmProtector

# Save recovery key to file
(Get-BitLockerVolume -MountPoint "C:").KeyProtector | Where-Object {$_.KeyProtectorType -eq "RecoveryPassword"} | Select-Object -ExpandProperty RecoveryPassword | Out-File recovery-key.txt
```

### 6.2 Database Encryption (TDE)

**Enable SQL Server TDE**:
```sql
-- Create master key
USE master;
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'MasterKeyPassword123!';

-- Create certificate
CREATE CERTIFICATE TDE_Cert WITH SUBJECT = 'TDE Certificate';

-- Create database encryption key
USE MyDatabase;
CREATE DATABASE ENCRYPTION KEY
WITH ALGORITHM = AES_256
ENCRYPTION BY SERVER CERTIFICATE TDE_Cert;

-- Enable TDE
ALTER DATABASE MyDatabase SET ENCRYPTION ON;
```

---

## 7. Configuration Auditing

### 7.1 CIS Benchmark Scanning

**Windows Server CIS Scan** (using PowerShell):
```powershell
# Example: Check password policy
$policy = Get-ADDefaultDomainPasswordPolicy
if ($policy.MinPasswordLength -lt 12) {
  Write-Output "FAIL: Minimum password length is $($policy.MinPasswordLength), should be 12+"
} else {
  Write-Output "PASS: Password length compliant"
}
```

**Linux CIS Scan** (using Lynis):
```bash
# Install Lynis
apt-get install lynis

# Run security audit
lynis audit system --quick

# Review results
cat /var/log/lynis.log
```

### 7.2 Cloud Configuration Compliance

**AWS Config Rules**:
```
- s3-bucket-public-read-prohibited
- s3-bucket-public-write-prohibited
- ec2-encrypted-volumes
- rds-encryption-enabled
- iam-password-policy
```

---

**END OF IMPLEMENTATION GUIDE S4**
