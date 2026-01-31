# ISMS-IMP-A.5.15-16-18-S2: Identity Lifecycle Process
## Implementation Guide for Joiner/Mover/Leaver Automation

**Document ID**: ISMS-IMP-A.5.15-16-18-S2  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: IAM Manager / IT Operations Manager  
**Status**: Active

---

## Document Purpose

This implementation guide provides **step-by-step procedures** for implementing identity lifecycle management in accordance with ISO/IEC 27001:2022 Control A.5.16. It translates policy requirements from **ISMS-POL-A.5.15-16-18-S3** into actionable implementation steps for joiner, mover, and leaver processes.

**Target Audience**: IAM team, IT operations, HR integration team, system administrators

**Prerequisites**:
- Read ISMS-POL-A.5.15-16-18-S3 (Identity Management requirements)
- Access control governance established (IMP-S1 completed)
- HR system identified as authoritative source
- Identity systems documented (AD, Azure AD, Okta, etc.)

---

## 1. Joiner Process Implementation (New Hire Onboarding)

### 1.1 HR System Integration

**Objective**: Automate detection of new hires from HR system.

**Step 1: Identify HR System as Authoritative Source**

HR system is the **single source of truth** for employee data:
- Employee name, email, job title, department
- Manager, location, start date
- Employment type (full-time, part-time, contractor)
- Termination date (when applicable)

**Common HR Systems**:
- **Workday** (cloud-based HRIS)
- **SAP SuccessFactors** (enterprise HCM)
- **ADP Workforce Now** (payroll + HRIS)
- **BambooHR** (small-medium business)
- **Oracle HCM Cloud** (enterprise)
- **Custom/legacy** (in-house systems)

**Question to Answer**: Which system in [Organization] is authoritative source for employee data?

---

**Step 2: Assess Integration Options**

**Option A: API Integration** (Best Practice)

**Requirements**:
- HR system has API (REST, SOAP, or vendor-specific)
- Identity system can call HR API
- Network connectivity between systems

**Benefits**:
- Real-time or near-real-time sync (hourly, daily)
- Automated detection of new hires
- Reduced manual effort
- Lower error rate

**Implementation**:
```
1. Request API access from HR vendor
2. Obtain API credentials (API key, OAuth token)
3. Configure identity system to call HR API
   - Frequency: Daily at 2am (detect new hires before business hours)
   - Query: New employees with start_date ≤ today + 3 days
   - Response: Employee details (name, email, title, manager, start_date)
4. Map HR fields to identity system attributes
   - HR: first_name → AD: givenName
   - HR: last_name → AD: sn (surname)
   - HR: email → AD: mail, userPrincipalName
   - HR: employee_id → AD: employeeID
   - HR: department → AD: department
   - HR: manager_email → AD: manager (lookup manager's DN)
5. Test with sample data (create test employee in HR, verify account created)
6. Monitor daily (logs, error notifications)
```

**Example: Workday API Integration**

```python
# Pseudo-code for Workday API integration
import requests
from datetime import datetime, timedelta

# Workday API endpoint
workday_url = "https://[tenant].workday.com/ccx/service/[tenant]/Human_Resources/v38.0"
headers = {"Authorization": "Bearer [API_TOKEN]"}

# Query for new hires (start date within next 3 days)
today = datetime.today()
query_date = today + timedelta(days=3)
params = {
    "start_date_from": today.strftime("%Y-%m-%d"),
    "start_date_to": query_date.strftime("%Y-%m-%d")
}

response = requests.get(f"{workday_url}/Get_Workers", headers=headers, params=params)
new_hires = response.json()["workers"]

# For each new hire, create AD account
for employee in new_hires:
    create_ad_account(
        first_name=employee["first_name"],
        last_name=employee["last_name"],
        email=employee["email"],
        title=employee["title"],
        department=employee["department"],
        manager=employee["manager_email"],
        start_date=employee["start_date"]
    )
```

**Estimated Effort**: 2-4 weeks (API setup, testing, monitoring)

---

**Option B: File Export/Import** (Common for Legacy Systems)

**Requirements**:
- HR system can export employee data (CSV, Excel, XML)
- Identity system can import file
- Secure file transfer method (SFTP, secure network share)

**Benefits**:
- Works with legacy HR systems (no API)
- Relatively simple to implement
- Can include manual verification step

**Drawbacks**:
- Not real-time (daily or weekly sync)
- Manual steps (export, transfer, import)
- Higher error rate (file corruption, format changes)

**Implementation**:
```
1. Configure HR system to export employee data
   - File format: CSV (comma-separated values)
   - Columns: employee_id, first_name, last_name, email, title, department, manager_email, start_date, termination_date, status
   - Export frequency: Daily at 1am
   - Export location: Secure SFTP server or network share

2. Configure identity system to import file
   - Import frequency: Daily at 2am (after HR export)
   - Import location: Same SFTP server or network share
   - Data validation: Check for required fields, valid email format, etc.
   - Error handling: Log errors, send notification to IT

3. Reconciliation process
   - Compare HR export with identity system data
   - Identify new employees (in HR but not in identity system)
   - Identify terminated employees (status = "Terminated" in HR)
   - Trigger provisioning/deprovisioning workflows

4. Manual verification (optional)
   - HR reviews new hire list daily
   - HR confirms new hires are correct before auto-provisioning
   - Reduces risk of errors (e.g., test employee records)
```

**Example: CSV File Format**

```csv
employee_id,first_name,last_name,email,title,department,manager_email,start_date,termination_date,status
10001,John,Smith,john.smith@company.com,Software Engineer,Engineering,alice.johnson@company.com,2026-01-20,,Active
10002,Jane,Doe,jane.doe@company.com,Marketing Manager,Marketing,bob.williams@company.com,2026-01-22,,Active
10003,Alice,Johnson,alice.johnson@company.com,Engineering Manager,Engineering,cto@company.com,2020-05-15,,Active
10004,Bob,Williams,bob.williams@company.com,CMO,Marketing,ceo@company.com,2019-03-10,,Active
10005,Charlie,Davis,charlie.davis@company.com,Finance Analyst,Finance,cfo@company.com,2023-06-01,2026-01-15,Terminated
```

**Estimated Effort**: 1-2 weeks (export/import setup, testing)

---

**Option C: Manual Process** (Small Organizations Only)

**Requirements**:
- Small organization (<50 employees)
- Low hiring volume (<5 new hires per month)
- IT team available to process requests

**Process**:
```
1. HR emails IT when new hire confirmed
   - Email subject: "New Hire - [Name] - Start Date [Date]"
   - Email body: Employee details (name, email, title, department, manager)

2. IT manually creates accounts
   - Active Directory account
   - Email account
   - Access to default systems (intranet, HR portal, etc.)
   
3. IT notifies manager (access is ready)

4. Manager confirms access with new hire (first day)
```

**Drawbacks**:
- Not scalable (>10 new hires/month becomes overwhelming)
- High error rate (typos, missed steps)
- No audit trail (unless IT documents in tickets)
- Delays (IT busy, email missed)

**Recommendation**: Avoid if possible, use File Export at minimum

**Estimated Effort**: 1 day (document process), ongoing manual effort

---

**Step 3: Select Integration Method**

**Decision Matrix**:

| Organization Size | HR System | Recommendation |
|-------------------|-----------|----------------|
| Enterprise (1000+ employees) | Workday, SAP SuccessFactors, Oracle HCM | API Integration (Option A) |
| Medium (100-1000 employees) | ADP, BambooHR, or modern HRIS | API Integration or File Export |
| Small (10-100 employees) | Legacy HRIS or payroll system | File Export (Option B) |
| Very Small (<10 employees) | Manual records or simple database | Manual Process (Option C) - temporary only |

**For [Organization]**: [Select appropriate option based on environment]

---

### 1.2 Account Provisioning Workflow

**Objective**: Automate account creation for new hires.

**Step 1: Define Provisioning Timeline**

**Provisioning SLA**: Access ready **by start date** (Day 0)

**Timeline**:
```
Day -7 (One Week Before Start):
  - New hire appears in HR system (or HR notifies IT)
  - Identity system detects new hire (API sync or file import)

Day -3 (Three Days Before Start):
  - Account provisioning workflow triggered
  - IT creates user account (AD, Azure AD, Okta)
  - Manager receives notification: "New hire [Name] starts on [Date], review default access"

Day -1 (One Day Before Start):
  - Email account created and tested
  - Welcome email sent to new hire's personal email (login credentials)
  - IT confirms all access provisioned

Day 0 (Start Date):
  - New hire logs in (account active)
  - Manager confirms access working
```

**Why 3 days before start?**
- Allows time for IT to provision access
- Allows time for manager to request additional access
- Ensures access ready on Day 0 (no delays)

---

**Step 2: Define Account Creation Process**

**Accounts to Create** (varies by organization):

| Account Type | System | Created By | Timeline |
|--------------|--------|-----------|----------|
| Active Directory (AD) account | On-premises AD | Automated (API) or IT | Day -3 |
| Azure AD account | Microsoft 365, Entra ID | Automated (sync from AD) or API | Day -3 |
| Email account | Microsoft 365, Google Workspace | Automated (tied to Azure AD or Google) | Day -3 |
| Okta account (if using Okta) | Okta identity platform | Automated (API) | Day -3 |
| VPN account | VPN system (Cisco, Palo Alto) | Automated or IT | Day -2 |
| Badge/physical access | Access control system | Facilities team | Day -1 |

**Account Attributes**:

Required attributes for new user account:
- **Username** (format: first.last, first.last001 if duplicate)
- **Email** (format: first.last@company.com)
- **First Name, Last Name**
- **Display Name** (format: "Last, First")
- **Employee ID** (from HR system)
- **Job Title**
- **Department**
- **Manager** (manager's username or email)
- **Office Location**
- **Start Date**
- **Account Expiration** (blank for employees, contract end date for contractors)

---

**Step 3: Implement Automated Provisioning**

**Using Identity Management Platform** (Azure AD, Okta, SailPoint):

```
Provisioning Workflow Configuration

Trigger: New employee detected in HR system
Conditions:
  - start_date ≤ today + 3 days
  - status = "Active"
  - employee_type = "Employee" or "Contractor"

Actions:
  1. Create AD account
     - Username: [first].[last] (check for duplicates, append number if needed)
     - Password: [Auto-generated, 16 chars, complexity requirements met]
     - OU: Based on department (e.g., OU=Finance,OU=Users,DC=company,DC=com)
     - Groups: Add to default groups ("All-Employees", department group)
     
  2. Create Email account
     - Email: [first].[last]@company.com
     - Mailbox: 50GB
     - Alias: [first].[last], [f.last] (if needed)
     
  3. Provision default access (based on job title/department)
     - All employees: Intranet, HR Portal, IT Service Desk
     - Finance employees: ERP (read access)
     - Engineering: Code repository (read access), Jira
     - Sales: CRM (standard user access)
     
  4. Send welcome email (to personal email)
     - Subject: "Welcome to [Organization] - Your Account is Ready"
     - Body: Login credentials, instructions, first-day information
     - Attachment: IT onboarding guide (how to connect to VPN, set up email on phone, etc.)
     
  5. Notify manager
     - Email: "New hire [Name] starts on [Date], default access provisioned"
     - Action item: Review default access, request additional access if needed
     
  6. Create ticket (audit trail)
     - Ticket type: "New Hire Provisioning"
     - Status: "Provisioned"
     - Details: Account created, email sent, manager notified
```

**Estimated Effort**: 2-3 weeks configuration, 1 week testing

---

**Using Scripts** (for organizations without identity management platform):

**PowerShell Script Example** (Active Directory + Microsoft 365):

```powershell
# New-EmployeeAccount.ps1
# Automates new hire provisioning for AD + M365

param(
    [Parameter(Mandatory=$true)]
    [string]$FirstName,
    
    [Parameter(Mandatory=$true)]
    [string]$LastName,
    
    [Parameter(Mandatory=$true)]
    [string]$Email,
    
    [Parameter(Mandatory=$true)]
    [string]$Title,
    
    [Parameter(Mandatory=$true)]
    [string]$Department,
    
    [Parameter(Mandatory=$true)]
    [string]$ManagerEmail,
    
    [Parameter(Mandatory=$true)]
    [string]$StartDate
)

# Generate username (first.last)
$Username = "$($FirstName.ToLower()).$($LastName.ToLower())"

# Check for duplicate username
if (Get-ADUser -Filter "SamAccountName -eq '$Username'") {
    # Append number (first.last001, first.last002, etc.)
    $Counter = 1
    while (Get-ADUser -Filter "SamAccountName -eq '$Username$Counter'") {
        $Counter++
    }
    $Username = "$Username$Counter"
}

# Generate temporary password
$Password = ConvertTo-SecureString -String (New-RandomPassword -Length 16) -AsPlainText -Force

# Determine OU based on department
$OU = switch ($Department) {
    "Finance" { "OU=Finance,OU=Users,DC=company,DC=com" }
    "Engineering" { "OU=Engineering,OU=Users,DC=company,DC=com" }
    "Sales" { "OU=Sales,OU=Users,DC=company,DC=com" }
    default { "OU=General,OU=Users,DC=company,DC=com" }
}

# Create AD account
New-ADUser `
    -SamAccountName $Username `
    -UserPrincipalName "$Username@company.com" `
    -GivenName $FirstName `
    -Surname $LastName `
    -DisplayName "$LastName, $FirstName" `
    -EmailAddress $Email `
    -Title $Title `
    -Department $Department `
    -Manager (Get-ADUser -Filter "EmailAddress -eq '$ManagerEmail'" | Select-Object -ExpandProperty DistinguishedName) `
    -Path $OU `
    -AccountPassword $Password `
    -Enabled $true `
    -ChangePasswordAtLogon $true

# Add to default groups
Add-ADGroupMember -Identity "All-Employees" -Members $Username
Add-ADGroupMember -Identity "VPN-Users" -Members $Username

# Department-specific groups
switch ($Department) {
    "Finance" { Add-ADGroupMember -Identity "Finance-Team" -Members $Username }
    "Engineering" { Add-ADGroupMember -Identity "Engineering-Team" -Members $Username }
    "Sales" { Add-ADGroupMember -Identity "Sales-Team" -Members $Username }
}

# Sync to Azure AD (if using Azure AD Connect)
Start-ADSyncSyncCycle -PolicyType Delta

# Wait for Azure AD sync (60 seconds)
Start-Sleep -Seconds 60

# Assign Microsoft 365 license (requires Azure AD module)
Connect-AzureAD
Set-AzureADUserLicense -ObjectId "$Username@company.com" -AddLicenses "company:ENTERPRISEPACK"

# Send welcome email
Send-MailMessage `
    -To $Email `
    -From "it@company.com" `
    -Subject "Welcome to [Organization] - Your Account is Ready" `
    -Body "Dear $FirstName,

Your account has been created. Here are your login details:

Username: $Username@company.com
Temporary Password: [Provided separately via secure channel]

Please log in on your first day and change your password.

Welcome to the team!

IT Department" `
    -SmtpServer "smtp.company.com"

# Log provisioning
Write-Output "Account created: $Username ($FirstName $LastName) - Department: $Department - Start Date: $StartDate"
```

**Estimated Effort**: 1-2 weeks scripting, 1 week testing

---

**Step 4: Define Default Access by Role**

**Default Access Matrix**:

Create standard access packages based on job function:

| Job Role / Department | Default Systems |
|-----------------------|-----------------|
| **All Employees** | - Email (Microsoft 365 or Google Workspace)<br>- Intranet (SharePoint, Confluence)<br>- HR Portal (self-service: benefits, payroll, time-off)<br>- IT Service Desk (ticket system)<br>- VPN (remote access) |
| **Finance** | All Employees +<br>- ERP (SAP, Oracle) - Read access<br>- Finance SharePoint<br>- Expense Management System |
| **Engineering** | All Employees +<br>- Code Repository (GitHub, GitLab, Bitbucket)<br>- Jira / Project Management<br>- Development Environments (non-production) |
| **Sales** | All Employees +<br>- CRM (Salesforce, HubSpot) - Standard User<br>- Sales Portal<br>- Commission Tracking System |
| **Marketing** | All Employees +<br>- CMS (WordPress, Drupal)<br>- Marketing Automation (HubSpot, Marketo)<br>- Analytics (Google Analytics, Adobe Analytics) |
| **HR** | All Employees +<br>- HRIS (Workday, SAP SuccessFactors) - Read/Write per role<br>- Recruiting System (Greenhouse, Lever)<br>- Benefits Portal - Admin access |
| **IT** | All Employees +<br>- Ticketing System (ServiceNow, Jira) - Technician role<br>- Monitoring Dashboards<br>- Knowledge Base - Edit access |

**Customization**: [Organization] defines role-based access based on job analysis

**Implementation**:
- Automate provisioning of default access (scripted or via identity platform)
- Manager can request additional access via standard access request workflow
- Review default access matrix annually (add/remove systems as business changes)

---

### 1.3 Welcome Email and First-Day Experience

**Objective**: Ensure new hires have clear instructions for first-day access.

**Step 1: Welcome Email Content**

**Welcome Email Template**:

```
Subject: Welcome to [Organization] - Your IT Account is Ready!

Dear [First Name],

Welcome to [Organization]! We're excited to have you join us on [Start Date].

Your IT account has been created. Here are your login details:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USERNAME: [username]@company.com
TEMPORARY PASSWORD: [Provided separately via SMS or phone call]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT YOU CAN ACCESS:
✓ Email: [username]@company.com (Microsoft Outlook or Gmail)
✓ Intranet: https://intranet.company.com
✓ HR Portal: https://hr.company.com (benefits, payroll, time-off)
✓ IT Service Desk: https://helpdesk.company.com (for IT support)

FIRST-DAY CHECKLIST:
☐ Log in to your email using the credentials above
☐ Change your temporary password (you'll be prompted on first login)
☐ Complete IT onboarding training (link sent to your email)
☐ Set up multi-factor authentication (MFA) for added security
☐ Connect to VPN if working remotely (instructions attached)

NEED HELP?
Contact IT Service Desk:
  Email: helpdesk@company.com
  Phone: +41 XX XXX XX XX
  Hours: Monday-Friday, 8am-5pm CET

We look forward to seeing you on [Start Date]!

Best regards,
IT Department
[Organization]

---
Attachments:
- IT Onboarding Guide.pdf
- VPN Setup Instructions.pdf
- Company Policies.pdf
```

**Delivery Method**:
- Send to **personal email** (provided by HR, not work email)
- Send **3 days before start date** (gives new hire time to review)
- CC manager (so manager knows email was sent)

---

**Step 2: Temporary Password Delivery**

**Security Consideration**: Never send password in email (security risk)

**Secure Password Delivery Options**:

**Option 1: SMS** (Most Common)
- IT sends temporary password via SMS to new hire's mobile phone
- New hire must change password on first login
- Pros: Secure, out-of-band delivery
- Cons: Requires mobile phone number

**Option 2: Phone Call**
- IT calls new hire, verbally provides temporary password
- New hire must change password on first login
- Pros: Personal touch, confirms identity
- Cons: Time-consuming, requires phone number

**Option 3: Self-Service Password Reset**
- New hire uses self-service portal to set initial password
- Requires identity verification (email, SMS code, security questions)
- Pros: Fully automated, no IT involvement
- Cons: Requires self-service infrastructure

**Option 4: Manager Delivery** (In-Person)
- IT provides temporary password to manager (sealed envelope)
- Manager gives to new hire on first day
- Pros: No technology required
- Cons: Only works for in-office employees

**Recommendation**: Option 1 (SMS) or Option 3 (Self-Service Portal)

---

**Step 3: First-Day IT Support**

**IT Onboarding Checklist** (for IT Support):

```
New Hire IT Onboarding - Day 1

☐ Greet new hire (if in office)
☐ Verify login works (username, password)
☐ Assist with password change (if needed)
☐ Set up MFA (multi-factor authentication)
  - Microsoft Authenticator app or Google Authenticator
  - Register phone number for SMS backup
☐ Configure email on laptop/phone (if needed)
☐ Connect to VPN (if remote worker)
☐ Test access to default systems (intranet, HR portal, etc.)
☐ Assign any additional access requested by manager
☐ Answer questions (VPN, email, password reset, etc.)
☐ Provide IT contact info (helpdesk email/phone)
```

**First-Day Experience Goals**:
- New hire can log in successfully (no password issues)
- New hire can access email and intranet
- New hire knows how to get IT support

**Success Metric**: ≥95% of new hires log in successfully on Day 1 (no IT issues)

---

## 2. Mover Process Implementation (Role Change / Transfer)

### 2.1 Detect Role Changes

**Objective**: Automatically detect when employees change roles, departments, or managers.

**Step 1: Define "Mover" Triggers**

**What qualifies as a "mover" event?**

| Change Type | Example | Access Impact | Review Trigger? |
|-------------|---------|---------------|-----------------|
| Department transfer | Finance → Marketing | Remove Finance access, add Marketing access | Yes |
| Job title change (promotion) | Analyst → Manager | Add managerial access (budget tools, HR systems) | Yes |
| Job title change (lateral move) | Software Engineer → Product Manager | Different system access | Yes |
| Manager change (same role) | Reports to Alice → Reports to Bob | Manager reviews access | Optional |
| Office location change | Zurich → Geneva | Physical access (badge), network segment | Optional |
| Employment type change | Contractor → Employee | Convert account type | Yes |

**For [Organization]**: Define which changes trigger access review

---

**Step 2: Detect Changes from HR System**

**Automated Detection**:

```
Daily HR Sync Process

1. Export current employee data from HR system
2. Compare with yesterday's export (identify changes)
3. Flag changes:
   - Department change: [Old Department] → [New Department]
   - Title change: [Old Title] → [New Title]
   - Manager change: [Old Manager] → [New Manager]
4. Trigger mover workflow for each flagged employee
5. Notify old manager, new manager, and IT
```

**Implementation** (using script):

```python
# Pseudo-code for detecting role changes
import pandas as pd

# Load yesterday's employee data
yesterday = pd.read_csv("hr_export_2026-01-10.csv")

# Load today's employee data
today = pd.read_csv("hr_export_2026-01-11.csv")

# Merge on employee_id, compare fields
merged = yesterday.merge(today, on="employee_id", suffixes=("_old", "_new"))

# Identify department changes
dept_changes = merged[merged["department_old"] != merged["department_new"]]

# For each department change, trigger mover workflow
for index, row in dept_changes.iterrows():
    employee_id = row["employee_id"]
    old_dept = row["department_old"]
    new_dept = row["department_new"]
    
    print(f"Mover Detected: {employee_id} - {old_dept} → {new_dept}")
    
    # Send notification
    send_notification(
        to=row["manager_email_old"],  # Old manager
        subject=f"Employee Transfer: {row['first_name']} {row['last_name']}",
        body=f"{row['first_name']} has transferred from {old_dept} to {new_dept}. Please review and remove access no longer needed."
    )
    
    send_notification(
        to=row["manager_email_new"],  # New manager
        subject=f"New Team Member: {row['first_name']} {row['last_name']}",
        body=f"{row['first_name']} has joined your team ({new_dept}). Please review default access and request additional access if needed."
    )
```

**Estimated Effort**: 1 week scripting, 1 week testing

---

### 2.2 Access Modification Workflow

**Objective**: Update user access when role changes.

**Step 1: Define Access Update Process**

```
Mover Workflow - Role Change

Day 0 (Effective Date of Role Change):
☐ HR system updated (new title, department, manager)
☐ Identity system detects change (daily sync)
☐ Notifications sent:
  - Old Manager: "Employee X transferred to [Department], review access"
  - New Manager: "Employee X joined your team, review access"
  - IT: "Role change detected for Employee X, prepare for access updates"

Day 1-3 (Access Review Period):
☐ Old Manager reviews employee's current access
  - Remove department-specific access (old team's systems)
  - Remove project-based access (if projects completed)
  - Submit removal requests via ticketing system
☐ New Manager requests new access
  - Grant default access for new department
  - Grant role-specific access based on new job function
  - Submit access requests via ticketing system

Day 4-7 (Access Modification):
☐ IT processes removal requests (old access removed)
☐ IT processes access requests (new access granted)
☐ User confirms access is correct:
  - Can access new systems (required for new role)
  - Old access removed (cannot access old systems)

Day 14 (Compliance Check):
☐ Security Team reviews role change
☐ Confirm user has appropriate access for new role
☐ Confirm old access removed (prevent privilege creep)
☐ Flag discrepancies (access not aligned with new role)
```

**Access Modification SLA**: 1 business day from manager approval

---

**Step 2: Implement Privilege Creep Prevention**

**Problem**: Users accumulate excess access over time (retain access from previous roles)

**Solution**: Automated privilege creep detection

```
Privilege Creep Detection - Role Change

1. User changes role (Finance Analyst → HR Analyst)

2. System compares current access vs. new role's default access
   Current Access:
   - ERP (Finance module) [Read]
   - Finance SharePoint [Write]
   - HR Portal [Read]
   
   New Role Default Access:
   - HR Portal [Write]
   - Benefits Portal [Read/Write]
   - HRIS [Read]

3. System flags discrepancies:
   - ERP (Finance module) - NOT in new role's default
   - Finance SharePoint - NOT in new role's default

4. System creates access review task for manager
   Task: "Review excess access for [Employee]"
   Details:
   ☐ ERP (Finance module) - Still needed? [Keep / Remove]
   ☐ Finance SharePoint - Still needed? [Keep / Remove]

5. Manager decision:
   - Remove: IT removes access
   - Keep: Manager provides business justification (documented in ticket)

6. Result:
   - Remove: ERP, Finance SharePoint
   - Add: Benefits Portal (Write), HRIS (Read)
   - Modify: HR Portal (Read → Write)
```

**Estimated Effort**: 2-3 weeks configuration (if using identity platform), or manual process (security team reviews role changes quarterly)

---

### 2.3 Contractor-to-Employee Conversion

**Objective**: Handle special case when contractor becomes full-time employee.

**Step 1: Define Conversion Process**

```
Contractor → Employee Conversion

Week -1 (Before Conversion):
☐ HR updates employee type in HR system (Contractor → Employee)
☐ HR updates contract end date (remove expiration)
☐ Identity system detects change (daily sync)
☐ IT receives notification: "Contractor [Name] converting to employee on [Date]"

Conversion Day:
☐ IT updates account type (remove "Contractor" flag, remove account expiration)
☐ IT updates email alias (remove "EXT-" prefix if used for contractors)
☐ IT updates group memberships (remove "Contractors" group, add "Employees" group)
☐ IT provisions employee-specific access (benefits portal, stock options, etc.)
☐ Manager confirms conversion complete

Week 1 (Post-Conversion):
☐ Verify account expiration removed (account won't auto-disable)
☐ Verify employee benefits access granted (HR portal, benefits)
☐ Remove contractor restrictions (if any)
```

**Key Difference**: Account already exists (don't create new account), just update attributes

---

## 3. Leaver Process Implementation (Termination / Offboarding)

### 3.1 Detect Terminations

**Objective**: Automatically detect when employees terminate (voluntary or involuntary).

**Step 1: Define Termination Detection**

**Termination Types**:

| Termination Type | HR System Update | IT Action | Timeline |
|------------------|------------------|-----------|----------|
| Involuntary (Fired) | Status = "Terminated", termination_date = today | Disable account immediately | Within 1 hour |
| Voluntary (Resignation) | Status = "Terminated", termination_date = last working day | Disable account on last day (5pm) | End of last working day |
| Contract End (Contractor) | Status = "Inactive", contract_end_date = today | Disable account on contract end | End of contract date |
| Leave of Absence | Status = "On Leave", leave_end_date = [future date] | Disable account temporarily | Start of leave |
| Retirement | Status = "Retired", retirement_date = [date] | Disable account on retirement date | Retirement date |

---

**Step 2: Automated Termination Detection**

**Daily Sync Process**:

```
1. Query HR system for terminations
   - SQL: SELECT * FROM employees WHERE termination_date = today()
   - API: GET /employees?status=Terminated&termination_date=today

2. For each terminated employee:
   - Check termination type (voluntary vs. involuntary)
   - Trigger offboarding workflow (immediate or scheduled)

3. Send notifications:
   - Manager: "Employee [Name] termination processed, access disabled"
   - IT: "Offboarding task created for [Name]"
   - Security: "Monitor for suspicious activity from [Name] (if involuntary)"
```

**Immediate Termination Detection** (for involuntary terminations):

For security, involuntary terminations should be processed immediately:

```
HR notifies IT via phone/email (urgent)
  ↓
IT disables account within 1 hour (manual override if necessary)
  ↓
Automated workflow triggered (post-facto documentation)
```

---

### 3.2 Account Deactivation Process

**Objective**: Disable access promptly when employees terminate.

**Step 1: Define Deactivation Timeline**

**Deactivation SLA**:
- **Involuntary termination**: Within 1 hour of HR notification
- **Voluntary resignation**: End of last working day (5pm)
- **Contractor contract end**: End of contract date (11:59pm)

**Why Immediate for Involuntary?**
- Security risk (disgruntled employee may sabotage systems)
- Data exfiltration risk (employee may steal IP, customer data)
- Compliance requirement (especially financial services, healthcare)

**Why End of Day for Voluntary?**
- Employee needs access to complete handover
- Reasonable notice (employee knows last day in advance)
- Lower security risk (amicable departure)

---

**Step 2: Deactivation Actions**

**Immediate Deactivation** (within 1 hour for involuntary):

```
Hour 0 (Termination Notification):
☐ HR updates status in HR system (Status = "Terminated")
☐ HR notifies IT via phone or urgent email

Hour 1 (Account Deactivation):
☐ IT disables AD/Azure AD account (user cannot log in)
  - Set account to disabled (not deleted yet)
  - Reset password (prevent re-access if account re-enabled by mistake)
☐ IT disables email (prevent sending/receiving)
  - Option 1: Convert to shared mailbox (manager can access for 30 days)
  - Option 2: Forward to manager (auto-reply set)
☐ IT disables VPN access (prevent remote access)
☐ IT revokes physical access badge (coordinate with facilities)
☐ IT removes from all groups (application access removed)

Hour 2-4 (Verification):
☐ IT verifies account disabled (test login - should fail)
☐ IT verifies VPN access revoked (test VPN connection - should fail)
☐ Security Team notified (monitor for suspicious activity, unauthorized access attempts)

Day 1-7 (Data Handover):
☐ Manager accesses ex-employee's email (review for critical threads)
☐ Manager accesses ex-employee's files (OneDrive, network drives)
☐ Manager transfers ownership of critical files to team
☐ IT exports email to PST (archive for legal retention)

Day 30 (Post-Deactivation Review):
☐ IT reviews account for complete removal
☐ Confirm all access removed (verify in all systems)
☐ Reassign service accounts (if employee was owner)
☐ Update distribution lists (remove ex-employee)

Day 90 (Account Deletion):
☐ IT deletes account (if no legal hold or retention requirement)
☐ IT deletes email archive (if retention period expired)
☐ IT removes from all systems (complete cleanup)
```

**Scheduled Deactivation** (end of day for voluntary):

Same process, but triggered automatically at 5pm on last working day.

---

**Step 3: Implement Automated Deactivation**

**Using Identity Management Platform**:

```
Offboarding Workflow Configuration

Trigger: Termination detected in HR system
Conditions:
  - termination_date ≤ today
  - status = "Terminated"
  
Decision:
  IF termination_type = "Involuntary"
    THEN Deactivate immediately
  ELSE IF termination_type = "Voluntary"
    THEN Deactivate at end of termination_date (5pm)

Actions (Immediate Deactivation):
  1. Disable AD account (Set-ADUser -Identity [user] -Enabled $false)
  2. Reset AD password (prevent re-access)
  3. Remove from all AD groups (except "Disabled-Accounts")
  4. Disable Azure AD account (if separate from AD)
  5. Convert Exchange mailbox to shared mailbox (manager can access)
  6. Revoke VPN access (remove from VPN group)
  7. Create offboarding ticket (audit trail)
  8. Notify manager (email: access disabled, data handover instructions)
  9. Notify security (email: monitor for suspicious activity)

Actions (Scheduled Deactivation):
  Same as above, but scheduled for 5pm on termination_date
```

**Estimated Effort**: 2-3 weeks configuration, 1 week testing

---

### 3.3 Data Handover Process

**Objective**: Ensure business continuity by transferring ex-employee's data to manager or team.

**Step 1: Manager Responsibilities**

**Manager Data Handover Checklist**:

```
☐ Email Review (within 7 days)
  - Access ex-employee's mailbox (shared mailbox or forwarding)
  - Identify important email threads (customer communications, project updates)
  - Forward critical emails to yourself or team members
  - Set auto-reply: "[Name] is no longer with [Organization]. For assistance, contact [Manager] at [Email]."

☐ File Review (within 7 days)
  - Access ex-employee's files (OneDrive, network drives, SharePoint)
  - Identify critical documents (project files, customer data, intellectual property)
  - Transfer ownership to yourself or appropriate team member
  - Archive files according to retention policy

☐ Task Reassignment (within 7 days)
  - Review ex-employee's open tasks (Jira, Asana, project management tools)
  - Reassign tasks to team members
  - Update project assignments (remove ex-employee, add new assignees)

☐ Service Account Ownership (within 7 days)
  - If ex-employee was owner of service accounts, reassign to new owner
  - Update service account documentation (new contact, new owner)

☐ External Communication (within 3 days)
  - Notify key external contacts (customers, partners, vendors)
  - Provide new point of contact (yourself or team member)
  - Update email signatures, contact lists

☐ Distribution Lists (within 7 days)
  - Remove ex-employee from team email aliases
  - Update department distribution lists
  - Update external contact lists (customer-facing email addresses)

☐ Confirm Handover Complete (Day 7)
  - Manager confirms all critical data transferred
  - Manager signs off on handover (documented in offboarding ticket)
```

**IT Support for Handover**:
- IT provides manager with access to ex-employee's mailbox (shared mailbox)
- IT provides manager with access to ex-employee's files (OneDrive ownership transfer)
- IT exports email to PST (archive) upon manager's request
- IT deletes account only after manager confirms handover complete (typically Day 30)

---

**Step 2: Data Retention and Deletion**

**Data Retention Policy** (varies by organization and regulation):

| Data Type | Retention Period | Reason |
|-----------|------------------|--------|
| Email | 90 days (accessible to manager) → then archived for legal retention | Business continuity + legal hold |
| Files (OneDrive, network drives) | Manager discretion (transfer or delete) | Business continuity |
| Email archive (PST) | 7 years (typical for legal/regulatory) | Legal compliance (e.g., GDPR, SOX) |
| User account | 90 days (disabled) → then deleted | Audit trail + prevent accidental deletion |
| Audit logs (access logs, activity logs) | Per organization's log retention policy (typically 1-3 years) | Security investigation, compliance |

**Customization**: [Organization] defines retention based on legal and regulatory requirements

---

### 3.4 Orphaned Account Detection and Remediation

**Objective**: Identify and clean up accounts that slipped through deprovisioning process.

**Step 1: Define Orphaned Account**

**What is an orphaned account?**

| Orphaned Account Type | Definition | Example |
|-----------------------|------------|---------|
| Ex-employee not deprovisioned | Employee terminated but account still active | Termination not processed by IT |
| No valid business owner | Account exists but user not in HR system | Contractor whose contract ended, not properly offboarded |
| Inactive account | No login in 90+ days, user status unclear | Employee on extended leave, or forgotten test account |
| Contractor expired | Contractor account past contract end date, still active | Contractor contract ended, account not disabled |
| Service account without owner | Service account exists but owner left organization | Ex-employee was service account owner, no reassignment |

**Impact of Orphaned Accounts**:
- **Security Risk**: Unauthorized access, backdoor for attackers
- **Compliance Risk**: Violates access control policies, audit findings
- **License Waste**: Paying for unused licenses (e.g., Microsoft 365)

---

**Step 2: Automated Orphaned Account Detection**

**Monthly Scan Process**:

```
Orphaned Account Detection - Monthly Process

Day 1 (First Monday of Month):
☐ Export current user accounts (from AD, Azure AD, Okta)
☐ Export current employee list (from HR system)
☐ Cross-reference (identify accounts NOT in HR system)

Day 2 (Analysis):
☐ For each account not in HR:
  - Check last login date (if < 90 days ago, may still be active)
  - Check account type (employee, contractor, service account)
  - Check manager (if manager exists, contact manager)
  - Check business owner (documented in account notes)

Day 3-7 (Verification):
☐ Contact account owner or manager:
  - Email: "Account [username] not found in HR system. Is this account still needed?"
  - Options:
    a) Still needed (provide justification, update documentation)
    b) No longer needed (disable account)
    c) Service account (reassign owner, document)

Day 14 (Remediation):
☐ For accounts confirmed no longer needed:
  - Disable account (not deleted yet, in case of error)
  - Remove from all groups (access revoked)
  - Notify security team (for audit log review)

Day 30 (Deletion):
☐ For accounts disabled in previous month:
  - If no objection raised, delete account
  - Archive audit logs (if required)

Day 31 (Reporting):
☐ Generate orphaned account report
  - Total accounts scanned
  - Orphaned accounts detected
  - Accounts disabled
  - Accounts deleted
  - Accounts retained (with justification)
☐ Report to CISO (monthly)
```

**Estimated Effort**: 1 week scripting, ongoing 2-4 hours/month

---

**Step 3: Orphaned Account Report Template**

```
Orphaned Account Detection Report - January 2026

Total Accounts Scanned: 500
Orphaned Accounts Detected: 12
Accounts Disabled This Month: 8
Accounts Deleted This Month: 4
Accounts Retained (Justified): 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DETAILS:

Orphaned Account #1:
  Username: john.smith
  Type: Employee
  Last Login: 2025-11-15 (78 days ago)
  HR Status: Not found (termination date: 2025-11-30)
  Action: Disabled on 2026-01-05
  Status: Pending deletion (30 days)

Orphaned Account #2:
  Username: jane.contractor
  Type: Contractor
  Last Login: 2025-10-01 (102 days ago)
  HR Status: Contract ended 2025-10-31
  Action: Disabled on 2026-01-05
  Status: Pending deletion (30 days)

[...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

REMEDIATION SUMMARY:
- 8 accounts disabled (access revoked)
- 4 accounts deleted (cleanup complete)
- 0 accounts retained with justification

RECOMMENDATIONS:
- Improve HR-IT integration (reduce manual offboarding errors)
- Implement automated contractor expiration checks
- Quarterly review of service account ownership

Report Prepared By: IT Security Team
Report Date: 2026-02-01
Distribution: CISO, IT Director, Internal Audit
```

---

## 4. Contractor/Vendor Identity Management

### 4.1 Contractor Onboarding (Time-Bound Access)

**Objective**: Manage contractor identities with automatic expiration.

**Step 1: Define Contractor Account Requirements**

**Contractor Account Attributes**:

| Attribute | Employee Account | Contractor Account |
|-----------|------------------|-------------------|
| Account Type | Employee | Contractor |
| Username Format | first.last | EXT-first.last (or first.last.ext) |
| Email Domain | first.last@company.com | first.last.ext@company.com (or external email) |
| Account Expiration | No expiration | Contract end date + 1 day |
| Sponsorship | N/A | Internal sponsor required (employee) |
| Access Level | Based on role | Restricted (no admin access unless justified) |
| Access Review Frequency | Annual | Quarterly |

**Why Different Treatment?**
- **Security**: Contractors are external (less trust, higher risk)
- **Compliance**: Regulations require tighter control (e.g., GDPR, NIS2)
- **Accountability**: Sponsor ensures contractor access is appropriate

---

**Step 2: Implement Contractor Onboarding Workflow**

```
Contractor Onboarding Process

Week -2 (Before Contract Start):
☐ Hiring manager submits contractor request
  - Contractor name, email (personal), job title
  - Contract start date, contract end date
  - Sponsor (internal employee responsible)
  - Access requirements (systems, access level)
☐ HR creates contractor record in HR system
  - Employee type: Contractor
  - Contract end date (account expiration)
  - Sponsor: [Internal employee]

Week -1:
☐ IT receives contractor onboarding request
☐ IT creates contractor account
  - Username: EXT-[first.last] (clearly identify as external)
  - Email: [first.last].ext@company.com (or allow external email)
  - Account expiration: Contract end date + 1 day (grace period)
  - Groups: "Contractors" (restricted access), sponsor's team group
☐ IT provisions access (based on access request, approved by sponsor)
☐ IT sends welcome email to contractor's personal email
  - Login credentials (username, temporary password via SMS)
  - Access instructions
  - Contract end date reminder

Contract Start Date:
☐ Contractor logs in (account active)
☐ Sponsor confirms access working
☐ Sponsor reviews contractor's access (quarterly review scheduled)

Quarterly Review:
☐ Sponsor receives reminder: "Review contractor [Name] access"
☐ Sponsor confirms access still appropriate OR requests removal

Contract End Date:
☐ Account automatically expires (account disabled)
☐ Sponsor receives notification: "Contractor [Name] account expired"
☐ Manager confirms contractor departure
☐ IT processes offboarding (data handover if needed)

Day 30 (After Contract End):
☐ IT deletes contractor account (if no retention requirement)
```

---

**Step 3: Automatic Expiration Implementation**

**Active Directory Example**:

```powershell
# Set account expiration for contractor
Set-ADUser -Identity "EXT-john.smith" -AccountExpirationDate "2026-06-30 23:59:59"
```

**Azure AD Example**:

```powershell
# Set account expiration using Azure AD
$expirationDate = Get-Date "2026-06-30"
Set-AzureADUser -ObjectId "ext-john.smith@company.com" -ExtensionProperty @{ExpirationDate=$expirationDate}
```

**Automated Expiration Check** (daily script):

```powershell
# Check for expired contractor accounts
$expiredContractors = Get-ADUser -Filter {AccountExpirationDate -lt (Get-Date)} -Properties AccountExpirationDate

foreach ($user in $expiredContractors) {
    # Disable account
    Disable-ADAccount -Identity $user
    
    # Notify sponsor
    $sponsor = Get-ADUser -Filter {EmailAddress -eq $user.Manager} -Properties EmailAddress
    Send-MailMessage -To $sponsor.EmailAddress `
        -Subject "Contractor Account Expired: $($user.Name)" `
        -Body "The contractor account for $($user.Name) expired on $($user.AccountExpirationDate). Please confirm contractor departure."
}
```

---

### 4.2 Contractor Access Extension

**Objective**: Handle contract extensions (contractor stays beyond original end date).

**Step 1: Define Extension Process**

```
Contractor Contract Extension Process

Week -2 (Before Contract End):
☐ Sponsor receives reminder: "Contractor [Name] contract ends on [Date]"
☐ Sponsor decides:
  Option A: Contract extension needed
  Option B: Contract ending, no extension

If Extension Needed:

Week -1:
☐ Sponsor submits access extension request
  - New contract end date
  - Business justification (why extension needed)
☐ HR updates contract end date in HR system
☐ IT updates account expiration date
  - Set-ADUser -Identity [user] -AccountExpirationDate [new date]
☐ Contractor notified: "Contract extended to [new date]"

If Contract Ending:

Contract End Date:
☐ Account expires automatically (disabled)
☐ Offboarding process triggered (data handover, account deletion)
```

**Extension Approval**:
- **Standard Extension** (<3 months): Sponsor approval sufficient
- **Long Extension** (>3 months): Manager + HR approval required
- **Multiple Extensions** (3+ times): CISO review (why not hire as employee?)

---

### 4.3 Vendor Access Management

**Objective**: Manage third-party vendor access (different from contractors).

**Vendor vs. Contractor**:
- **Contractor**: Individual working on-site or remotely (like an employee)
- **Vendor**: Company providing services (may have multiple users)

**Vendor Access Scenarios**:
- IT vendor (remote support access to systems)
- Auditor (access to financial systems, documents)
- Consultant (project-based access)
- Managed service provider (ongoing access to infrastructure)

---

**Step 1: Vendor Access Request Process**

```
Vendor Access Request

1. Vendor Manager submits access request
   - Vendor company name
   - Vendor user(s) needing access
   - Systems to access
   - Access level (read-only, admin, etc.)
   - Business justification (SOC 2 audit, IT support, etc.)
   - Access duration (start date, end date)

2. Approval workflow
   - Vendor Manager approves
   - System Owner approves (for sensitive systems)
   - Security Team reviews (assess risk)
   - CISO approves (for admin access or sensitive data)

3. IT provisions access
   - Create vendor account (username: VENDOR-[company]-[user])
   - Set account expiration (access end date)
   - Grant minimal access (least privilege)
   - Enable logging (all vendor actions logged)

4. Vendor signs NDA / Agreement
   - Non-disclosure agreement (protect confidential data)
   - Acceptable use policy (vendor must follow rules)
   - Security requirements (MFA required, password complexity)

5. Access granted
   - Vendor notified (login credentials via secure channel)
   - Access monitored (Security Team reviews logs)

6. Quarterly review
   - Vendor Manager reviews vendor access
   - Confirms access still needed OR requests removal

7. Access removal
   - On end date, account automatically expires
   - Vendor Manager confirms vendor departure
   - IT deletes account after 30 days
```

---

## 5. Service Account Lifecycle

### 5.1 Service Account Management

**Objective**: Manage non-human accounts (applications, systems, automated processes).

**Step 1: Define Service Account**

**What is a service account?**
- Account used by applications, systems, or automated processes (not humans)
- Examples:
  - Database service account (SQL Server runs under service account)
  - API service account (app-to-app authentication)
  - Backup service account (backup software uses service account)
  - Monitoring service account (monitoring agent runs under service account)

**Service Account Characteristics**:
- No interactive login (cannot log in via GUI)
- Long-lived (no expiration unless service decommissioned)
- Privileged (often has elevated access)
- Owner assigned (human responsible for service account)

---

**Step 2: Service Account Creation Process**

```
Service Account Creation

1. System Owner submits service account request
   - Service account name (descriptive, e.g., "svc-backup-prod")
   - Purpose (what application/process uses it)
   - Required access (systems, databases, file shares)
   - Access level (read, write, admin)
   - Owner (person responsible for service account)

2. Approval workflow
   - System Owner approves
   - Security Team reviews (assess risk, especially for privileged accounts)
   - CISO approves (for admin/root access)

3. IT creates service account
   - Username: svc-[purpose]-[environment] (e.g., svc-backup-prod)
   - Password: Long, complex, randomly generated (32+ characters)
   - Password storage: Secure password vault (CyberArk, HashiCorp Vault, Azure Key Vault)
   - Account expiration: None (unless temporary project)
   - Owner: [Documented in account description or notes]

4. Password management
   - Password rotated regularly (quarterly or annually)
   - Password never shared (only in password vault)
   - Password complexity requirements enforced

5. Monitoring
   - Service account activity logged
   - Unusual activity flagged (interactive login, access from unexpected IP)
   - Quarterly review (owner confirms service account still needed)
```

---

**Step 3: Service Account Ownership**

**Owner Responsibilities**:
- Ensure service account is used only for intended purpose
- Approve password rotations (coordinate with IT)
- Review service account activity (quarterly)
- Request service account deletion when no longer needed

**What Happens When Owner Leaves?**
- Service account ownership must be reassigned
- IT identifies service accounts owned by ex-employee
- Manager assigns new owner (typically another team member)
- Ownership documented (update account notes)

**Example**:
```
Service Account: svc-backup-prod
Original Owner: Alice Johnson (left company on 2026-01-15)
New Owner: Bob Williams (backup system administrator)
Ownership Transfer Date: 2026-01-20
```

---

### 5.2 Privileged Service Accounts

**Objective**: Extra controls for service accounts with elevated privileges.

**Privileged Service Account Examples**:
- SQL Server service account (sysadmin role)
- Active Directory service account (domain admin)
- Application pool account (admin access to web servers)
- Backup service account (read access to all data)

**Additional Controls**:
- **Password Vault**: Passwords stored in privileged access management (PAM) system (CyberArk, BeyondTrust)
- **Password Rotation**: Automated password rotation (monthly or quarterly)
- **Session Recording**: All privileged account activity recorded (for audit)
- **Just-in-Time Access**: Privileged access granted only when needed (not permanent)
- **Monitoring**: Real-time alerting for privileged account misuse

**See ISMS-A.8.2 (Privileged Access Rights)** for detailed PAM requirements.

---

## 6. Implementation Roadmap

### 6.1 Phased Implementation

**Phase 1: Foundation** (Months 1-2)
- ☐ Identify HR system as authoritative source
- ☐ Document current identity systems (AD, Azure AD, Okta)
- ☐ Map HR-to-identity integration points
- ☐ Select integration method (API, file export, or manual)

**Phase 2: Joiner Process** (Months 3-4)
- ☐ Implement HR-to-identity integration (new hire detection)
- ☐ Automate account provisioning (AD, email, default access)
- ☐ Define default access by role
- ☐ Create welcome email template
- ☐ Test with pilot group (IT department first)

**Phase 3: Leaver Process** (Months 5-6)
- ☐ Implement termination detection (HR system integration)
- ☐ Automate account deactivation (immediate for involuntary, scheduled for voluntary)
- ☐ Define data handover process (manager responsibilities)
- ☐ Implement orphaned account detection (monthly scan)
- ☐ Test with terminated employees

**Phase 4: Mover Process** (Months 7-8)
- ☐ Implement role change detection (department, title, manager changes)
- ☐ Automate access review trigger (for role changes)
- ☐ Implement privilege creep prevention (compare access vs. role)
- ☐ Test with employees changing roles

**Phase 5: Contractor Management** (Months 9-10)
- ☐ Implement contractor account creation (with expiration)
- ☐ Define contractor access restrictions
- ☐ Implement sponsorship model (internal sponsor required)
- ☐ Automate quarterly access reviews for contractors
- ☐ Test with active contractors

**Phase 6: Service Accounts** (Months 11-12)
- ☐ Inventory all service accounts (current state)
- ☐ Assign owners to all service accounts
- ☐ Implement service account password vault
- ☐ Define service account creation process
- ☐ Implement quarterly service account reviews

---

### 6.2 Success Metrics

**Measure identity lifecycle effectiveness**:

| Metric | Target | Measurement Frequency |
|--------|--------|----------------------|
| New hire access ready by start date | ≥95% | Monthly |
| Terminated employee access removed within 24h | ≥98% | Monthly |
| Orphaned accounts detected and remediated | ≤1% of total accounts | Monthly |
| Contractor accounts with valid expiration date | 100% | Monthly |
| Service accounts with assigned owner | 100% | Quarterly |
| Role change access updates within 7 days | ≥90% | Monthly |

---

## 7. Common Pitfalls and Solutions

**Challenge 1: "HR system doesn't have API"**

**Solution**: Use file export (Option B). Configure HR to export daily CSV, import to identity system.

---

**Challenge 2: "IT can't provision access by start date"**

**Solution**: 
- Provision 3 days before start (gives buffer time)
- Use automated provisioning (reduce manual effort)
- Prioritize onboarding over other IT tasks (new hires are critical)

---

**Challenge 3: "Managers don't complete data handover"**

**Solution**:
- Require manager sign-off before deleting account
- Escalate to manager's manager if not completed within 7 days
- Tie to performance evaluation (accountability)

---

**Challenge 4: "Orphaned accounts everywhere after first scan"**

**Solution**:
- Prioritize high-risk orphaned accounts (privileged access)
- Phase cleanup (100 accounts/month)
- Improve joiner/mover/leaver processes (prevent future orphans)

---

## 8. Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], IAM Manager / IT Operations Manager - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation guide |

---

**END OF IMPLEMENTATION GUIDE S2 (Identity Lifecycle Process)**

**Related Documents**:
- ISMS-POL-A.5.15-16-18-S3 (Identity Management Requirements)
- ISMS-IMP-A.5.15-16-18-S1 (Access Control Governance)
- ISMS-IMP-A.5.15-16-18-S3 (Role Definition and Assignment)

**Next Implementation Guide**: ISMS-IMP-A.5.15-16-18-S3 (Role Definition and Assignment)