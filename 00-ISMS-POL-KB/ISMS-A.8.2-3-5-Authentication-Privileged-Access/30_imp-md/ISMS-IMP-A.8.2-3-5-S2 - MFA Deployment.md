# ISMS-IMP-A.8.2-3-5-S2
## MFA Deployment Guide

**Document ID**: ISMS-IMP-A.8.2-3-5-S2  
**Title**: Multi-Factor Authentication Deployment  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Identity & Access Management Lead  
**Status**: Draft

---

## 1. MFA Deployment Strategy

### 1.1 Phased Rollout Plan

**Phase 1: Privileged Users (Week 1-2)** - MANDATORY
- Target: 100% of privileged users (admins, DBAs, security team)
- Deadline: 7 days
- MFA Method: Hardware tokens preferred, authenticator app minimum
- Enforcement: No MFA = No privileged access

**Phase 2: Remote Access Users (Week 3-4)** - MANDATORY  
- Target: 100% of VPN users, external access
- Deadline: 14 days
- MFA Method: Authenticator app or push notification
- Enforcement: VPN requires MFA enrollment before access

**Phase 3: Pilot Group (Month 2)** - Voluntary
- Target: 10-20 volunteers from different departments
- MFA Method: Authenticator app or push notification
- Purpose: Identify issues, gather feedback, refine process

**Phase 4: All Standard Users (Months 3-12)** - Gradual Mandatory
- Target: 95%+ of all users
- Rollout: Department by department (10-20 users per week)
- MFA Method: Authenticator app, push notification, or biometric
- Enforcement: Soft enforcement (Month 3-6), Hard enforcement (Month 7+)

### 1.2 Enrollment Targets and Metrics

| User Type | MFA Target | Timeline | Enforcement |
|-----------|------------|----------|-------------|
| Privileged | 100% | 7 days | Hard (no MFA = access revoked) |
| Remote Access | 100% | 14 days | Hard (VPN requires MFA) |
| Standard Users | 95%+ | 12 months | Gradual (soft → hard) |
| Contractors | 100% | Before access | Hard (no access without MFA) |

---

## 2. MFA Platform Configuration

### 2.1 Azure MFA Setup

**Enable Azure MFA**:
```
Azure AD → Security → MFA → Getting started

Deployment model: Cloud-based (Azure MFA)
(Alternative: On-premises MFA Server - legacy, not recommended)

User settings:
- Allow users to remember MFA on trusted devices: Yes (30 days)
- Allow users to select authentication method: Yes
- Require re-registration: Every 180 days (update contact info)
```

**Conditional Access Policy** (Azure AD P1 required):
```
Azure AD → Security → Conditional Access → New policy

Name: "MFA for All Users"
Assignments:
  Users: All users (exclude break-glass accounts)
  Cloud apps: All cloud apps
  Conditions: Any location
Access controls:
  Grant: Require multi-factor authentication
  Session: Sign-in frequency 12 hours
Enable policy: Report-only (test first), then On
```

### 2.2 Okta MFA Setup

**Enable Okta MFA**:
```
Security → Multifactor → Factor types

Enabled factors:
- Okta Verify (push notification) - Recommended
- Google Authenticator (TOTP) - Enabled
- SMS Authentication - Disabled (insecure)
- Voice Call Authentication - Disabled
- Security Question - Disabled (weak factor)

Factor enrollment:
- Required factors: Okta Verify OR Google Authenticator (user choice)
- Optional factors: None
```

**Okta Sign-On Policy**:
```
Security → Authentication → Sign On

Policy: "MFA for All Users"
Rule: "Require MFA"
  IF user is: Any user in Any group
  AND user's IP is: Anywhere
  THEN prompt for factor: Every sign-on (or every 12 hours for trusted device)
```

### 2.3 Google Workspace 2-Step Verification

**Enable 2-Step Verification**:
```
Admin console → Security → Authentication → 
2-Step Verification

Enforcement: On (allow users to turn on 2-Step Verification)
(Advanced: Enforcement period - 3 months warning, then mandatory)

Allowed methods:
- Google prompts (push) - Recommended
- Authenticator app (TOTP) - Enabled
- Security Key (FIDO) - Enabled
- SMS - Backup only
```

---

## 3. MFA Method Deployment

### 3.1 Authenticator App Deployment

**Supported Apps**:
- Microsoft Authenticator (recommended for Azure AD)
- Google Authenticator (universal)
- Authy (universal, cloud backup)
- Okta Verify (Okta-specific, has push)

**User Enrollment Process**:
1. User installs authenticator app on smartphone
2. User logs into identity provider portal
3. User navigates to Security Settings → MFA Setup
4. System displays QR code
5. User scans QR code with authenticator app
6. App generates 6-digit code
7. User enters code to verify enrollment
8. System confirms MFA enrolled successfully

**Enrollment Communications**:
```
Subject: Action Required: Enable Multi-Factor Authentication (MFA)

Dear [User],

To enhance security, multi-factor authentication (MFA) is now required 
for accessing [Organization] systems.

What you need to do:
1. Install Microsoft Authenticator app (iOS/Android)
2. Visit https://aka.ms/mfasetup (or your org's enrollment portal)
3. Scan the QR code with your app
4. Complete verification

Deadline: [Date - 7 days for privileged, 30 days for standard]

Need help? Contact IT Support at support@example.com

Thank you for helping keep [Organization] secure.
```

### 3.2 Hardware Token Deployment

**Token Types**:
- YubiKey 5 NFC ($45-50) - USB-A + NFC
- YubiKey 5C NFC ($55-60) - USB-C + NFC
- Titan Security Key ($30-50) - Google's FIDO2 key

**Deployment Process for Tier 0 Admins**:
1. Procure hardware tokens (2 per user - primary + backup)
2. Pre-register tokens (if platform supports bulk registration)
3. Ship tokens to users (secure shipping)
4. User receives tokens → enrolls in identity provider
5. User tests both tokens (primary and backup)
6. User stores backup token in secure location (home safe, office locked drawer)

**Enrollment Steps** (Azure AD):
```
User → Security Settings → Security info → Add method → Security key
1. Insert YubiKey into USB port
2. Click "Next"
3. Touch YubiKey button when it blinks
4. Create PIN for YubiKey (if not already set)
5. Touch YubiKey button again to confirm
6. Name the key (e.g., "YubiKey Primary")
7. Repeat for backup key
```

### 3.3 Push Notification Deployment

**Platforms with Native Push**:
- Microsoft Authenticator (push to phone)
- Okta Verify (push to phone)
- Duo Mobile (push to phone)

**User Experience**:
1. User enters username + password
2. System sends push notification to phone
3. User receives notification: "Sign-in request from Windows PC in New York"
4. User taps "Approve" or "Deny"
5. System grants access (if approved)

**Security Considerations**:
- MFA fatigue attacks: User approves without checking
- Mitigation: Number matching (user enters number shown on screen)
- Azure AD: Enable number matching in Conditional Access

---

## 4. MFA Enrollment Automation

### 4.1 Automated Enrollment Reminders

**Enrollment Tracking**:
```python
# Pseudo-code for enrollment reminder automation

daily_check:
  enrolled_users = get_mfa_enrolled_users()
  all_users = get_all_users()
  not_enrolled = all_users - enrolled_users
  
  for user in not_enrolled:
    days_until_deadline = user.mfa_deadline - today()
    
    if days_until_deadline == 7:
      send_email(user, "MFA Required in 7 Days")
    elif days_until_deadline == 3:
      send_email(user, "MFA Required in 3 Days - Urgent")
    elif days_until_deadline == 0:
      if user.is_privileged:
        disable_account(user)  # Hard enforcement
        send_email(user, "Account Disabled - MFA Not Enrolled")
      else:
        send_email(user, "MFA Past Due - Enroll Now")
```

### 4.2 Enrollment Dashboards

**Metrics to Track**:
- MFA enrollment rate overall (%)
- MFA enrollment by department (%)
- MFA enrollment by user type (privileged, remote, standard)
- MFA method distribution (hardware token, app, push, etc.)
- Days until enrollment deadline per user
- Users overdue for MFA enrollment

**Dashboard Tools**:
- Power BI (Azure AD sign-in logs + MFA registration events)
- Okta Reports (MFA adoption report)
- Custom Python script (export user list, check MFA status, generate Excel report)

---

## 5. MFA Recovery Procedures

### 5.1 Lost Device Recovery

**Scenario**: User loses smartphone with authenticator app

**Recovery Process**:
1. User contacts IT support helpdesk
2. IT support verifies user identity:
   - Employee ID + manager confirmation, OR
   - In-person verification with ID badge, OR
   - Security questions + callback to registered phone number
3. IT support resets MFA registration (removes old device)
4. User re-enrolls MFA on new device:
   - Install authenticator app on new phone
   - Scan QR code to re-register
   - Verify enrollment works
5. IT support logs MFA reset (audit trail)

**Identity Verification Requirements**:
```
Verification Method 1: Manager confirmation
- User provides employee ID
- IT support emails user's manager
- Manager confirms user identity and device loss
- IT support proceeds with MFA reset

Verification Method 2: In-person
- User visits IT support in person
- User shows government ID and employee badge
- IT support verifies photo matches
- IT support proceeds with MFA reset

Verification Method 3: Multi-factor verification
- User answers 3 security questions correctly
- IT support calls user's registered mobile number
- User confirms reset request on call
- IT support proceeds with MFA reset
```

### 5.2 Backup MFA Methods

**Why Backup Methods Matter**:
- Primary device lost/stolen/broken
- Primary device battery dead
- Primary device left at home
- Authenticator app accidentally deleted

**Recommended Backup Strategy**:
1. **Primary**: Authenticator app on smartphone
2. **Backup Option 1**: Second device (tablet, old phone)
3. **Backup Option 2**: Hardware token (YubiKey)
4. **Backup Option 3**: Backup codes (one-time use codes)

**Backup Codes Implementation** (Azure AD, Okta):
```
User → Security Settings → MFA → Backup codes
- Generate 10 backup codes (8-digit codes)
- User saves codes securely (password manager, printed and locked in safe)
- Each code can be used once
- User regenerates codes after using half of them
```

---

## 6. MFA Monitoring and Compliance

### 6.1 MFA Enrollment Monitoring

**Automated Checks**:
```
Weekly Report: MFA Enrollment Status

Privileged Users:
- Enrolled: 45/45 (100%) ✅
- Not Enrolled: 0 (0%)

Remote Access Users:
- Enrolled: 128/130 (98%) ⚠️
- Not Enrolled: 2 (2%) - [List names]

Standard Users:
- Enrolled: 450/500 (90%) ⚠️
- Not Enrolled: 50 (10%) - [List names, escalate to managers]

Action Items:
- Follow up with 2 remote users (deadline passed)
- Escalate 50 standard users to department managers
```

### 6.2 MFA Bypass Detection

**Monitor for**:
- MFA bypass attempts (authentication without MFA when required)
- Conditional Access policy exclusions (users excluded from MFA requirement)
- Legacy authentication (protocols that don't support MFA - disable these)

**Alert Rules**:
```
Alert: "MFA Bypass Attempt"
Trigger: User authenticated without MFA when policy requires MFA
Action: 
  - Send alert to security team
  - Log incident
  - Investigate (was this legitimate break-glass or policy violation?)

Alert: "Legacy Authentication Detected"
Trigger: Authentication using Basic Auth, IMAP, POP3, SMTP AUTH
Action:
  - Send alert to security team
  - Identify application using legacy auth
  - Plan migration to modern auth
```

---

## 7. User Training and Support

### 7.1 MFA Training Materials

**Training Topics**:
1. Why MFA is required (security benefits, compliance)
2. How to install authenticator app
3. How to enroll MFA (step-by-step with screenshots)
4. How to use MFA (daily login experience)
5. What to do if device is lost
6. How to register backup MFA method

**Training Delivery**:
- Email with video tutorial (5 minutes)
- Live training sessions (30 minutes, Q&A)
- Help desk support (phone, chat, in-person)
- Self-service knowledge base articles

### 7.2 Common User Issues and Solutions

| Issue | Solution |
|-------|----------|
| "I don't have a smartphone" | Provide hardware token (YubiKey) or desk phone push (if supported) |
| "App doesn't generate codes" | Check phone time/date is synced correctly (TOTP requires accurate time) |
| "Lost my phone" | Contact IT support for MFA reset with identity verification |
| "MFA is annoying" | Explain "remember this device for 30 days" option |
| "Push notification not received" | Check internet connection, retry, or use authenticator code instead |

---

## 8. Implementation Checklist

**Pre-Deployment**:
- [ ] MFA platform selected (Azure MFA, Okta MFA, Google 2-Step, etc.)
- [ ] Licensing confirmed (P1 for Azure AD Conditional Access, etc.)
- [ ] Phased rollout plan created
- [ ] User communications drafted

**Pilot Phase**:
- [ ] Pilot group identified (10-20 users)
- [ ] MFA enrollment tested with pilot users
- [ ] Feedback collected
- [ ] Issues resolved

**Privileged User Rollout**:
- [ ] Hardware tokens procured for Tier 0 admins
- [ ] Privileged users enrolled (100% target)
- [ ] MFA enforcement enabled for privileged accounts
- [ ] No privileged access without MFA verified

**Standard User Rollout**:
- [ ] Department-by-department rollout schedule created
- [ ] Enrollment reminders automated
- [ ] Help desk trained on MFA support
- [ ] Enrollment dashboard created (track progress)

**Monitoring**:
- [ ] MFA enrollment metrics tracked weekly
- [ ] MFA bypass attempts monitored
- [ ] Legacy authentication disabled
- [ ] Quarterly MFA compliance report generated

---

**END OF IMPLEMENTATION GUIDE S2**

**Next**: IMP-S3 (PAM Implementation)
