# ISMS-POL-A.8.32-S5.D
## Quick Reference Guide

**Document ID**: ISMS-POL-A.8.32-S5.D  
**Title**: Change Management - Quick Reference Guide (Annex D)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Change Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Change Manager | Initial quick reference |

**Review Cycle**: Annual  
**Approvers**: Change Manager  
**Purpose**: One-page practitioner guide for most common change management scenarios

---

## D.1 Change Type Decision Tree

**START HERE → Is this change needed?**

```
┌─ Is change already in Standard Change Catalog?
│   ├─ YES → Standard Change
│   │        ▼
│   │   Submit change request (self-service OK)
│   │   No CAB approval needed
│   │   Follow catalog procedure
│   │   Log in change system
│   │
│   └─ NO → Continue...
│
├─ Is this an emergency situation?
│   ├─ YES → Does it meet ALL emergency criteria?
│   │        • Immediate action required?
│   │        • Critical incident/security/failure?
│   │        • Risk of inaction > risk of action?
│   │        ▼
│   │   ├─ YES → Emergency Change
│   │   │        • Contact E-CAB immediately
│   │   │        • Document justification
│   │   │        • Accelerated approval
│   │   │        • PIR mandatory within 2 days
│   │   │
│   │   └─ NO → Urgent Normal Change
│   │            • Call special CAB meeting
│   │            • Expedite but follow full process
│   │
│   └─ NO → Normal Change
│            ▼
│       Submit change request
│       Risk assessment
│       CAB review
│       Full process
```

---

## D.2 Approval Authority Quick Reference

| Risk Level | Who Approves | Typical Timeline |
|------------|--------------|------------------|
| **Low** (Standard) | Change Manager | Immediate - 1 day |
| **Medium** (Normal) | CAB | Weekly CAB meeting |
| **High** (Normal) | CAB + Senior IT Mgmt | 1-2 weeks |
| **Critical** (Normal) | CAB + CISO + Exec Mgmt | 2-4 weeks |
| **Emergency** | E-CAB | <4 hours |

---

## D.3 Required Information Checklist

**Every change request needs:**
- [ ] Clear description (what's changing?)
- [ ] Business justification (why?)
- [ ] Affected systems/users
- [ ] Risk assessment (Impact × Likelihood)
- [ ] Implementation date/time
- [ ] Testing evidence (for normal changes)
- [ ] Rollback plan
- [ ] Communication plan (if stakeholders affected)

**Additional for high/critical risk:**
- [ ] Detailed implementation plan
- [ ] Comprehensive testing results
- [ ] UAT sign-off
- [ ] Security review approval
- [ ] Phased deployment plan

---

## D.4 Testing Requirements

| Change Risk | Testing Required |
|-------------|------------------|
| **Low** | Basic verification |
| **Medium** | Integration testing + UAT |
| **High** | Full testing suite + UAT + Security |
| **Critical** | Comprehensive + Pilot/Canary |

**All changes:** Production validation after deployment

---

## D.5 Timeline Guidance

**Standard Change:**
- Submission to implementation: 0-2 days (depends on catalog procedure)

**Normal Change (Medium Risk):**
- Submission → CAB review: 3-5 days
- CAB approval → implementation: 5-10 days
- Total: 1-2 weeks typical

**Normal Change (High Risk):**
- Submission → Approval: 1-2 weeks
- Approval → Implementation: 1-3 weeks
- Total: 2-5 weeks typical

**Emergency Change:**
- Submission → E-CAB approval: <4 hours
- Approval → Implementation: Immediate
- PIR completion: Within 2 business days

**Plan ahead!** Don't turn normal changes into emergencies through poor planning.

---

## D.6 Common Mistakes to Avoid

❌ **"This is urgent, make it emergency"**  
✅ Urgent ≠ Emergency. Use expedited normal change process.

❌ **"We don't have time to test"**  
✅ You don't have time NOT to test. Fixing production issues takes longer than testing.

❌ **"Just a small change, no need for change request"**  
✅ ALL changes need change requests. "Small" changes cause big incidents.

❌ **"We'll document it later"**  
✅ Document during implementation. You won't remember details later.

❌ **"CAB always approves, why bother?"**  
✅ CAB process catches issues before production. That's why you haven't had more incidents.

---

## D.7 Emergency Change Fast Facts

**What qualifies as emergency:**
- Active security breach/exploitation
- Critical system failure affecting business
- Data loss/corruption imminent
- Regulatory deadline (with documented urgency)

**What does NOT qualify:**
- CEO wants feature tomorrow (poor planning)
- Marketing deadline (scheduled event)
- "We're behind schedule" (project management issue)
- Vendor's preferred timing (convenience)

**Emergency change process:**
1. Call E-CAB hotline: [PHONE NUMBER]
2. Document emergency justification
3. Get E-CAB approval (2+ members)
4. Implement change
5. Complete full documentation within 24 hours
6. PIR within 2 business days (MANDATORY)

**Emergency change abuse leads to process restrictions and management escalation.**

---

## D.8 Rollback Decision Criteria

**Rollback if:**
- Critical functionality not working
- Severe performance degradation (>50% slower)
- Security vulnerability introduced
- Data integrity issues detected
- Unacceptable number of users affected
- Issues cannot be fixed forward in reasonable time

**Rollback decision maker:**
- Primary: Change Implementer recommends
- Approval: Change Manager or CAB (based on original approval authority)
- Emergency: Incident Manager can authorize immediate rollback

**After rollback:**
- Document reason
- Root cause analysis
- Fix identified issues
- Retest
- Resubmit as new change request

---

## D.9 Key Contacts

| Role | Contact | Availability |
|------|---------|--------------|
| **Change Manager** | [Name, Email, Phone] | Business hours |
| **E-CAB Hotline** | [Phone Number] | 24/7 |
| **CAB Chair** | [Name, Email] | Business hours |
| **Security Reviewer** | [Name, Email] | Business hours |
| **IT Operations Manager** | [Name, Email, Phone] | Business hours + on-call |

**After hours emergency:** Call E-CAB hotline → Automated system pages on-call personnel

---

## D.10 Helpful Resources

**Change Management System:** [URL]  
**Policy Documents:** [SharePoint/Portal URL]  
**Standard Change Catalog:** [URL or ITSM system path]  
**Training Materials:** [Learning Management System URL]  
**Change Calendar:** [URL]  
**CAB Meeting Schedule:** [URL]

**Questions?** Email: changemanagement@[organization].com  
**Training Request:** Contact Change Manager

---

## D.11 Monthly Checklist (For Change Managers)

**Week 1:**
- [ ] Review previous month's metrics
- [ ] Update CAB on trends
- [ ] Identify failed changes for analysis

**Week 2:**
- [ ] Review Standard Change Catalog for updates needed
- [ ] Check compliance with PIR completion
- [ ] Review emergency changes for abuse patterns

**Week 3:**
- [ ] Exception register review
- [ ] Training needs assessment
- [ ] Process improvement suggestions collection

**Week 4:**
- [ ] Monthly report to management
- [ ] Update change calendar with known freeze periods
- [ ] Quarterly review preparation (if applicable)

---

## D.12 Remember

**Change management exists to:**
- ✅ Prevent incidents
- ✅ Enable controlled innovation
- ✅ Provide audit trail
- ✅ Protect users and systems

**Change management does NOT exist to:**
- ❌ Slow down progress
- ❌ Create bureaucracy
- ❌ Give CAB veto power
- ❌ Punish people for making changes

**The goal:** Safe, efficient, documented changes that improve the organization while minimizing risk.

---

**END OF ANNEX D**

*"The best change management process is one you barely notice because it's so well-integrated into how people actually work."* ⚙️

*Feynman's principle: If the process requires a 50-page manual to understand, you don't have a process—you have a problem.* 📚

*This quick reference should fit on one page (or two max). Print it. Put it on your desk. Refer to it. That's why it exists.* 🎯
