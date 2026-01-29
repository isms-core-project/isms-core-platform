# ISMS-POL-A.8.9-S5.D
## Configuration Management - Quick Reference Guide

**Document ID**: ISMS-POL-A.8.9-S5.D  
**Title**: Quick Reference Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft

---

## D.1 Purpose

This **one-page quick reference** provides essential information for common configuration management activities. Suitable for printing and posting in IT work areas.

---

## D.2 Configuration Management at a Glance

### D.2.1 Core Principles

✅ **All systems must have documented baselines**  
✅ **All changes require approval before implementation**  
✅ **Monitor for configuration drift and remediate promptly**  
✅ **Apply security hardening standards (CIS, STIG, or equivalent)**

---

## D.3 Do I Need to Submit a Change Request?
```
┌─────────────────────────────────────────────────────────────┐
│                    CHANGE DECISION TREE                      │
└─────────────────────────────────────────────────────────────┘

Is this a Standard Change (in the Standard Change Catalog)?
├─ YES → Follow documented procedure. No change request needed.
│         Log the change in tracking system.
│
└─ NO → Is this an emergency (critical incident or security vulnerability)?
    ├─ YES → EMERGENCY CHANGE
    │         • Get verbal approval from CTO or CISO
    │         • Implement change
    │         • Submit post-implementation documentation within 24 hours
    │
    └─ NO → NORMAL CHANGE
              • Submit change request form (ISMS-POL-A.8.9-S5.B)
              • Submit at least 5 business days before desired implementation
              • Wait for CAB approval
              • Implement after approval
```

---

## D.4 Who Approves What?

| Change Type | Approver | Timeframe |
|-------------|----------|-----------|
| **Standard Change** | Pre-approved (Configuration Manager reviews annually) | Immediate |
| **Normal Change (Low/Medium Risk)** | Change Advisory Board (CAB) | Next CAB meeting (weekly) |
| **Normal Change (High Risk)** | CAB + CISO/CTO sign-off | Next CAB + executive review |
| **Emergency Change** | CTO or CISO (verbal OK) | Immediate (post-docs required) |

---

## D.5 Configuration Deviation Response

**If you detect or receive an alert about configuration drift:**
```
STEP 1: Is this from an approved change I just made?
  YES → Update baseline documentation, close alert
  NO → Go to STEP 2

STEP 2: Is this a security concern?
  (Security control disabled, unauthorized admin access, suspicious change)
  YES → STOP. Call SOC immediately: [SOC phone]
  NO → Go to STEP 3

STEP 3: Can I fix this in under 30 minutes without service impact?
  YES → Remediate now, document action, close alert
  NO → Submit change request for remediation OR request exception

STEP 4: Document everything in deviation tracking system
```

---

## D.6 Key Contacts

| Role | Name | Email | Phone |
|------|------|-------|-------|
| **Configuration Manager** | [Name] | [Email] | [Phone] |
| **CAB Chair** | [Name] | [Email] | [Phone] |
| **Security Operations Center (SOC)** | 24/7 Team | [Email] | [Phone] |
| **CISO** | [Name] | [Email] | [Phone] |
| **IT Operations Manager** | [Name] | [Email] | [Phone] |

---

## D.7 Common Tasks - Quick Links

| I need to... | Document/System | Link/Location |
|-------------|-----------------|---------------|
| Submit a change request | Change Request Form | [Link or Email] |
| Find a baseline for my asset type | Annex A - Configuration Standards | [Link to policy] |
| Request an exception to policy | Exception Request Process | [Link or Email Config Mgr] |
| Report a security incident | Incident Response | [SOC contact] |
| Check Standard Change Catalog | Standard Changes List | [Link or SharePoint] |
| Access CMDB | Configuration Database | [Link to CMDB] |
| Find hardening standards | CIS Benchmarks / STIGs | [Internal repository link] |

---

## D.8 SLA Reminders

**Configuration Drift Remediation:**
- Critical: 4 hours
- High: 24 hours
- Medium: 5 business days
- Low: 30 days

**Change Request Processing:**
- Normal Changes: CAB reviews weekly
- Emergency Changes: Immediate verbal approval, paperwork within 24 hours

---

## D.9 Frequently Asked Questions

**Q: I made an emergency change at 2 AM to fix a critical outage. What do I do now?**  
A: Document the change immediately. Submit emergency change post-implementation form within 24 hours. Be prepared to explain justification in post-change review.

**Q: I found a configuration that doesn't match our baseline, but it's needed for the application to work. What should I do?**  
A: Request a configuration exception (contact Configuration Manager). Provide business justification and describe any compensating controls.

**Q: Can I test a configuration change in production?**  
A: NO. Use DEV/TEST environments. Production changes require change approval.

**Q: The baseline documentation for my system is out of date. How do I update it?**  
A: Contact Configuration Manager. Provide updated configuration details and justification for changes.

**Q: I received a configuration drift alert but I didn't make any changes. What should I do?**  
A: Investigate immediately. Check system logs to determine who/what made the change. If suspicious, contact SOC. If a legitimate but undocumented change, follow deviation procedures.

---

## D.10 Red Flags - When to Escalate Immediately

**🚨 Call SOC immediately if you observe:**
- Unauthorized administrative accounts created
- Security controls (firewall, antivirus, encryption) disabled
- Unknown scheduled tasks or cron jobs
- Configuration changes you didn't make and can't explain
- Suspicious processes or network connections
- System behavior inconsistent with configuration

**Do NOT attempt to "fix" these yourself - preserve evidence and escalate.**

---

## D.11 Policy Documents - Where to Find Them

All configuration management policies are available at: [Intranet/SharePoint/Wiki Link]

**Master Policy**: ISMS-POL-A.8.9 - Configuration Management  
**Key Sections**:
- S1: Purpose, Scope, Definitions
- S2.1: Baseline Configuration Requirements
- S2.2: Change Control Requirements
- S2.3: Configuration Monitoring Requirements
- S2.4: Security Hardening Requirements
- S3: Roles and Responsibilities
- S4: Policy Governance

**Annexes**:
- S5.A: Configuration Standards by Asset Type
- S5.B: Change Request Form Template
- S5.C: Configuration Deviation Procedures
- S5.D: Quick Reference Guide (this document)

---

## D.12 Remember

**Configuration Management exists to:**
✅ Ensure systems are secure and stable  
✅ Prevent unauthorized or harmful changes  
✅ Enable rapid recovery from incidents  
✅ Demonstrate compliance to auditors

**It's not bureaucracy - it's risk management.**

*"If you think following change control is slow, try recovering from an unplanned outage caused by an undocumented change at 3 AM."* - Every IT Operations Manager, Ever

---

**END OF DOCUMENT**

**For detailed procedures, refer to the full policy at [link]**  
**Questions? Contact Configuration Manager: [email]**

---