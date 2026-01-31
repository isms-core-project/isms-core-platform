# ISMS-POL-A.8.12-S5.C
## Annex C: DLP Incident Response Procedures

**Document ID**: ISMS-POL-A.8.12-S5.C  
**Title**: DLP Incident Response Procedures  
**Version**: 1.0  
**Date**: 2025-01-03  
**Classification**: Internal  
**Owner**: Incident Response Lead  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-03 | IR Lead | Initial incident procedures |

**Review Cycle**: Semi-annual (or after major incidents)  
**Next Review Date**: 2025-07-03  
**Approvers**: Incident Response Lead + CISO

**Distribution**: SOC analysts, Incident Response team, IT Operations  
**Related Documents**: ISMS-POL-A.8.12-S2.4 (Incident Response & Remediation)

---

## 1. Purpose

This annex provides **step-by-step procedures** for handling DLP incidents. These procedures translate policy requirements (S2.4) into operational playbooks.

**Use Case:** SOC triage, incident investigation, containment actions

---

## 2. Incident Severity Quick Reference

| Severity | Examples | Response SLA | Escalation |
|----------|----------|--------------|------------|
| **Critical** | Credentials emailed externally, source code to GitHub, mass PII export | 15 min | CISO, Legal, DPO, HR |
| **High** | Finance data to unapproved cloud, repeated USB blocks, IP to personal email | 1 hour | IR Lead, Data Owner |
| **Medium** | Contract sent to wrong recipient, confidential file to personal OneDrive | 4 hours | SOC Lead |
| **Low** | Employee emailed confidential without encryption (should use secure portal) | 24 hours | Security Analyst |

---

## 3. PLAYBOOK 1: Credential / Secret Leak

**Scenario:** DLP detected credentials, API keys, private keys, passwords in outbound transfer

### Phase 1: Detection & Triage (0-15 minutes)

**SOC Analyst Actions:**
1. **Validate alert** - Review DLP log, confirm true positive (not test/false positive)
2. **Identify credential type:**
   - ☐ Password (user account, database, application)
   - ☐ API key (cloud provider, SaaS, internal API)
   - ☐ Private key (SSH, SSL/TLS, code signing)
   - ☐ Other secrets (tokens, connection strings)
3. **Classify severity:** CRITICAL (all credential leaks are Critical)
4. **Create incident ticket** (auto-escalate to IR team)
5. **Notify IR Lead** (phone call + email)

### Phase 2: Containment (15-30 minutes)

**IR Team Actions:**
1. **Rotate credentials immediately:**
   - Password: Force password reset for affected account
   - API key: Revoke key via cloud provider console
   - Private key: Revoke certificate, generate new keypair
2. **Disable compromised account** (if user account credentials leaked)
3. **Block external access** (if API key for cloud service)
4. **Preserve evidence:**
   - Export DLP alert details
   - Screenshot of leaked credential (sanitized)
   - Email audit log (if emailed externally)
5. **Notify stakeholders:**
   - ☐ CISO (within 15 min)
   - ☐ System owner (whose credential was leaked)
   - ☐ Legal/DPO (if potential breach)

### Phase 3: Investigation (30 min - 4 hours)

**IR Team Actions:**
1. **Determine how credential was leaked:**
   - Accidental paste into email?
   - Credential stored in code file?
   - Screenshot containing credential?
2. **Check for unauthorized access:**
   - Review authentication logs (did attacker use credential?)
   - Cloud provider audit logs (API key usage)
   - Database logs (connection attempts with leaked password)
3. **Assess scope:**
   - Was credential used elsewhere? (same password for multiple accounts)
   - How long was credential active before rotation?
   - What resources did credential grant access to?
4. **Interview user** (if employee leak):
   - Why was credential in transferrable format?
   - Are there other credentials at risk?
   - Training gap or malicious intent?

### Phase 4: Remediation (4 hours - 48 hours)

**IR Team + Security Engineering Actions:**
1. **Deploy detection improvements:**
   - Update DLP regex for credential formats
   - Enable GitHub secret scanning (if code repository)
   - Implement secrets management (HashiCorp Vault, Azure Key Vault)
2. **User education:**
   - Security awareness training on credential handling
   - Manager notification (if negligent)
   - Disciplinary action if willful (HR consultation)
3. **Monitor for recurrence:**
   - Enhanced DLP monitoring for this user (30 days)
   - Watch for similar patterns organization-wide

### Phase 5: Closure & Lessons Learned (48 hours - 7 days)

**IR Lead Actions:**
1. **Post-incident review** (all stakeholders)
2. **Document lessons learned:**
   - How did credential end up in transferrable format?
   - Why did user not use secrets management?
   - How can we prevent similar incidents?
3. **Update DLP rules** (based on findings)
4. **Close incident ticket**

---

## 4. PLAYBOOK 2: Mass Data Exfiltration

**Scenario:** DLP detected >100 files or >1GB transferred in <10 minutes

### Phase 1: Detection & Triage (0-15 minutes)

**SOC Analyst Actions:**
1. **Validate alert** - Review DLP log, confirm volume anomaly
2. **Identify transfer details:**
   - User identity
   - Channel (email, USB, web, network)
   - Destination (personal email, cloud, USB device)
   - Data classification (Restricted, Confidential, Internal)
3. **Classify severity:** CRITICAL (mass exfiltration always Critical)
4. **Create incident ticket** (auto-escalate to IR team)
5. **Notify IR Lead + CISO** (phone call)

### Phase 2: Immediate Containment (15-30 minutes)

**IR Team Actions:**
1. **Disable user account** (prevent further exfiltration)
2. **Isolate endpoint** (EDR quarantine, disconnect from network)
3. **Block external access:**
   - If personal cloud: Contact provider (Dropbox, Google) - request account suspension
   - If USB: Device already blocked by DLP
   - If email: Block forwarding rules, review sent items
4. **Preserve evidence:**
   - Endpoint disk image (for forensics)
   - DLP logs (all events last 90 days)
   - Email audit (if exfiltration via email)
   - HR records (recent termination, resignation, PIP?)

### Phase 3: Investigation (30 min - 24 hours)

**IR Team + Forensics Actions:**
1. **Determine intent:**
   - Malicious (insider threat, pre-termination data theft)
   - Negligent (user syncing work folder to personal OneDrive)
   - Automated (backup script, sync tool misconfiguration)
2. **Assess scope:**
   - What data was exfiltrated? (file names, data categories)
   - Was exfiltration successful or blocked by DLP?
   - How long has exfiltration been happening? (review historical DLP logs)
3. **Check for compromise:**
   - Malware on endpoint? (EDR scan)
   - Unusual authentication? (VPN from foreign country, off-hours access)
   - Phishing victim? (email audit for suspicious links)
4. **Interview user** (if employee):
   - Why were you transferring this data?
   - Where did you send it?
   - Can you delete it? (if cloud/personal device)
5. **Notify Legal/DPO** (if breach notification required)

### Phase 4: Remediation (1-7 days)

**IR Team + HR + Legal Actions:**
1. **User consequences:**
   - Malicious: Termination, legal action (breach of contract, NDA)
   - Negligent: Warning, training, enhanced monitoring
2. **Data recovery:**
   - Request deletion from recipient (if identifiable, trusted)
   - Legal injunction (if competitor, malicious)
   - Breach notification (FADP/GDPR if required)
3. **Technical remediation:**
   - Deploy enhanced DLP for high-risk users (departing employees)
   - Block personal cloud for all users (if policy gap)
   - Implement Data Rights Management (DRM) for IP (if applicable)
4. **Monitor for recurrence:**
   - Watch for similar patterns (same user cohort, same data type)

### Phase 5: Closure & Lessons Learned (7-14 days)

**IR Lead + CISO Actions:**
1. **Post-incident review**
2. **Document lessons learned:**
   - Early warning signs missed (resignation, performance issues)
   - DLP coverage gaps (unprotected channel)
   - HR process improvements (offboarding controls)
3. **Update policy/procedures**
4. **Close incident ticket**

---

## 5. PLAYBOOK 3: Negligent Disclosure (Medium/Low Severity)

**Scenario:** Employee emailed confidential document without encryption to approved partner

### Quick Response (4-24 hours)

**SOC Analyst Actions:**
1. **Validate:** Review email, confirm recipient is approved partner
2. **Contact user's manager:**
   - Explain policy violation (should have used secure portal)
   - Request manager educate user on proper procedure
3. **User education:**
   - Email user with policy reminder
   - Provide link to secure file transfer portal
   - Log training in HR system
4. **Monitor:**
   - Watch for repeat violations (if >3 in 30 days, escalate to HR)
5. **Close ticket** (no further action if isolated incident)

---

## 6. Decision Trees

### Severity Classification Decision Tree
```
START: DLP Alert Received
   ↓
Q1: Is data Restricted (PII/credentials/IP/payment cards)?
   YES → Severity = HIGH minimum
   NO → Go to Q2
   ↓
Q2: Is destination external/untrusted?
   YES → Severity = HIGH
   NO → Go to Q3
   ↓
Q3: Is this a repeat violation (same user, >5 in 24 hours)?
   YES → Severity = HIGH
   NO → Go to Q4
   ↓
Q4: Is data Confidential?
   YES → Severity = MEDIUM
   NO → Severity = LOW
```

### Containment Decision Tree
```
START: Incident Confirmed
   ↓
Q1: Is severity CRITICAL?
   YES → Disable account, isolate endpoint, notify CISO
   NO → Go to Q2
   ↓
Q2: Is severity HIGH?
   YES → Notify manager, review user activity, preserve evidence
   NO → Go to Q3
   ↓
Q3: Is severity MEDIUM?
   YES → User education, monitor for 30 days
   NO → Log incident, close ticket
```

---

## 7. Contact Information

| Role | Contact | Availability |
|------|---------|--------------|
| **SOC Hotline** | [phone], [email] | 24x7 |
| **Incident Response Lead** | [phone], [email] | On-call rotation |
| **CISO** | [phone], [email] | Business hours + on-call |
| **DPO** | [email] | Business hours |
| **Legal** | [phone], [email] | Business hours + on-call |
| **HR** | [email] | Business hours |

---

**END OF DOCUMENT**

*"In incident response, speed matters. These playbooks ensure you don't waste time figuring out what to do."* 🚨