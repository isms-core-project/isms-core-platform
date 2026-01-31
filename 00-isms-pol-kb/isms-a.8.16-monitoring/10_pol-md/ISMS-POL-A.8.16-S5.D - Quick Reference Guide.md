# ISMS-POL-A.8.16-S5.D
## Quick Reference Guide

**Document ID**: ISMS-POL-A.8.16-S5.D
**Title**: Quick Reference Guide (Monitoring Activities Policy)  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: SOC Lead  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead | Initial quick reference guide |

**Review Cycle**: As needed (updated when core policies change)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: SOC Lead

**Distribution**: All Personnel (especially SOC, System Owners, Security Team)  
**Format**: Available as PDF, HTML (SOC wiki), laminated desk card, digital wallpaper

**Related Documents**: 
- ISMS-POL-A.8.16-S1 through S4 (Full Policy)
- ISMS-POL-A.8.16-S5.A (Capability Standards)
- ISMS-POL-A.8.16-S5.B (Baseline Template)
- ISMS-POL-A.8.16-S5.C (Alert Response Procedures)

---

## 1. Policy Summary (30-Second Version)

**What**: Security monitoring infrastructure detects threats and anomalies 24×7.

**Why**: Early detection = faster response = reduced impact.

**Scope**: All systems handling organization data (servers, workstations, network devices, applications).

**Key Requirements**:
- ✅ All critical systems monitored
- ✅ Baselines established for normal behavior
- ✅ Alerts triaged within SLA timeframes
- ✅ Logs retained 90 days (hot storage), 1 year total

**Your Role**:
- **SOC Analysts**: Triage alerts, investigate, escalate
- **System Owners**: Collaborate on baselines, respond to escalations
- **Everyone**: Report suspicious activity

---

## 2. Severity Classification Quick Reference

| Severity | Definition | Examples | Response Time |
|----------|-----------|----------|---------------|
| **Critical (P1)** | Active attack, confirmed compromise, critical system affected | • Ransomware<br>• Active data breach<br>• Root compromise<br>• Critical system down | **<15 minutes** |
| **High (P2)** | Likely security event, high-value target, rapid action needed | • Malware detected<br>• Brute force on admin account<br>• Suspicious data exfil<br>• Lateral movement | **<1 hour** |
| **Medium (P3)** | Potential security event, normal systems, investigation needed | • Baseline deviation<br>• Failed logins (non-admin)<br>• Policy violation<br>• Suspicious process | **<4 hours** |
| **Low (P4)** | Informational, low risk, routine investigation | • Scan detected<br>• Minor policy violation<br>• Informational alerts<br>• Audit findings | **<1 business day** |

**Severity Multipliers**:
- Admin/privileged account affected → Increase 1 level
- Critical system affected → Increase 1 level
- After-hours + no on-call coverage → Treat as one level higher for urgency

---

## 3. SLA Timeframes (How Fast Must We Respond?)

### 3.1 Alert Response SLAs

| Severity | MTTA (Mean Time to Acknowledge) | MTTT (Mean Time to Triage) | MTTI (Mean Time to Investigate) |
|----------|--------------------------------|---------------------------|--------------------------------|
| **Critical** | <5 minutes | <15 minutes | <1 hour |
| **High** | <15 minutes | <1 hour | <4 hours |
| **Medium** | <1 hour | <4 hours | <24 hours |
| **Low** | <4 hours | <1 business day | <3 business days |

**Definitions**:
- **MTTA**: Time from alert fired → analyst acknowledges
- **MTTT**: Time from alert fired → triage complete (disposition determined)
- **MTTI**: Time from triage → full investigation complete (for True Positives)

**If You're Going to Miss SLA**: Escalate immediately. Better to escalate early than miss SLA.

### 3.2 Baseline Review SLAs

| System Criticality | Baseline Review Frequency |
|-------------------|--------------------------|
| Critical | Quarterly (every 3 months) |
| High | Semi-annually (every 6 months) |
| Medium/Low | Annually |

**Also review if**: System changes, excessive FPs/FNs, business function changes.

---

## 4. Escalation Paths

### 4.1 Technical Escalation (During Investigation)
```
Alert → Tier 1 SOC → Tier 2 SOC → Tier 3 SOC → Security Engineering
           ↓             ↓            ↓
        (Simple)    (Complex)   (Advanced)
```

**When to Escalate**:
- Can't determine disposition within SLA
- Need specialized expertise (forensics, malware analysis)
- Tool/platform issues blocking investigation

### 4.2 Incident Escalation (Confirmed Security Event)
```
True Positive → SOC Tier 2 → Incident Response → CISO → Executive Management
                                    ↓
                            (Coordinates response)
```

**When to Escalate to IR**:
- Confirmed compromise
- Malware detection
- Data exfiltration
- Critical system affected
- Any True Positive requiring remediation

### 4.3 After-Hours Escalation

**Critical or High Severity**:
1. Create incident ticket
2. Page on-call: [ON-CALL PAGER NUMBER]
3. If no response in 15 minutes, call SOC Lead: [CELL PHONE]

**Medium or Low Severity**:
1. Create ticket in queue
2. Next shift will triage
3. Document findings so far

---

## 5. Common Alert Types - Quick Response Guide

| Alert Type | Triage Questions | Immediate Actions | Escalate If... |
|-----------|------------------|-------------------|----------------|
| **Brute Force** | • Source IP?<br>• Successful login after?<br>• User confirm? | • Check auth logs<br>• Check threat intel<br>• Contact user | • Success after failures<br>• Known bad IP<br>• Admin account targeted |
| **Malware** | • Contained?<br>• C2 communication?<br>• Spread? | • **Isolate host**<br>• Check EDR telemetry<br>• Collect sample | • **ALWAYS ESCALATE**<br>(All malware → IR) |
| **Data Exfil** | • Destination?<br>• Data type?<br>• User confirm? | • Check flow logs<br>• Check file access<br>• Geo-locate dst | • Unknown destination<br>• Sensitive data<br>• User denies |
| **Lateral Movement** | • User normal behavior?<br>• Systems related?<br>• User confirm? | • Check RDP/SSH logs<br>• Check process exec<br>• Contact user | • User denies<br>• Systems unrelated<br>• Attack tools detected |
| **Baseline Deviation** | • Legit business event?<br>• Happened before?<br>• Owner aware? | • Check historical data<br>• Contact system owner<br>• Review underlying logs | • No legit explanation<br>• Extreme deviation<br>• Attack patterns |

---

## 6. Baseline Establishment - Quick Guide

**Step-by-Step** (See Annex B for full details):

1. **Identify System** - Name, type, criticality, owner, business function
2. **Define Metrics** - What to measure (auth events, network traffic, etc.)
3. **Collect Data** - 30-90 days observation, exclude incidents
4. **Calculate Statistics** - Mean, median, std dev, 95th percentile
5. **Create Time-Aware Baselines** - Business hours, off-hours, weekends
6. **Document** - Use template in Annex B
7. **Derive Thresholds** - 95th percentile × 1.2 (recommended)
8. **Approve** - System owner + SOC lead sign off

**Quick Threshold Formula**:
```
Alert Threshold = 95th Percentile × 1.2 (moderate tolerance)
OR
Alert Threshold = Mean + (2 × Std Dev)
```

**Review Schedule**:
- Critical systems: Every 3 months
- High systems: Every 6 months
- Medium/Low systems: Annually

---

## 7. Roles and Responsibilities - Who Does What?

| Role | Responsibilities |
|------|------------------|
| **SOC Tier 1** | • Monitor alerts 24×7<br>• Triage within SLA<br>• Escalate True Positives<br>• Document false positives |
| **SOC Tier 2/3** | • Complex investigations<br>• Establish baselines<br>• Tune detection rules<br>• Mentor Tier 1 |
| **System Owners** | • Collaborate on baselines<br>• Provide business context<br>• Approve baselines<br>• Respond to escalations |
| **Security Engineering** | • Deploy/maintain monitoring infrastructure<br>• Develop detection rules<br>• Integration with other tools<br>• Capacity planning |
| **Incident Response** | • Respond to confirmed incidents<br>• Coordinate remediation<br>• Post-incident analysis<br>• Update playbooks |
| **SOC Lead** | • Manage SOC operations<br>• Approve baselines<br>• Review metrics<br>• Policy governance |
| **CISO** | • Policy approval<br>• Strategic oversight<br>• Executive reporting<br>• Budget/resources |

---

## 8. FAQ (Frequently Asked Questions)

**Q: What is a baseline?**  
A: Documented normal behavior for a system/metric. Used to detect anomalies (deviations from normal).

**Q: How long are logs retained?**  
A: 90 days in hot storage (fast search), 1 year total (warm/cold storage for compliance).

**Q: Who do I contact if I have questions about an alert?**  
A: SOC Lead (business hours) or on-call (after hours). See Section 9 for contact info.

**Q: What if I can't triage an alert within SLA?**  
A: Escalate immediately to Tier 2. Better to escalate early than miss SLA.

**Q: Can I suppress a noisy alert?**  
A: No. Alert suppression hides potential threats. Instead, tune the detection rule (adjust threshold, whitelist legitimate activity). Create tuning ticket.

**Q: What if I think an alert is a false positive but I'm not sure?**  
A: Investigate thoroughly using playbooks (Annex C). If still unclear after investigation, escalate to Tier 2. Document your uncertainty.

**Q: How do I know if a baseline is outdated?**  
A: Check review date in baseline document. Also review if: excessive false positives, missed detections, or system changed significantly.

**Q: What if system owner doesn't respond to my baseline approval request?**  
A: Escalate to their manager and SOC Lead after 3 business days. Baseline cannot go live without approval.

**Q: Can I close a malware alert as false positive?**  
A: Only if confirmed EICAR test file or vendor-signed legitimate software. When in doubt, escalate. Malware false negatives = breach.

**Q: What's the difference between "False Positive" and "Benign True Positive"?**  
A: 
- **False Positive**: Alert fired but underlying event didn't actually happen (e.g., scanner misidentified as attack)
- **Benign True Positive**: Alert fired correctly, event happened, but it's non-malicious (e.g., user typo'd password)

**Q: Who has access to monitoring data?**  
A: SOC, Security Team, Incident Response. Access is logged. Request access via [ACCESS REQUEST PROCESS].

**Q: What if I discover a monitoring coverage gap?**  
A: Document the gap, create ticket, escalate to Security Engineering. Gaps = blind spots = risk.

---

## 9. Contact Information

### 9.1 SOC Contacts

| Contact | Hours | Method |
|---------|-------|--------|
| **SOC Tier 1 (Shift)** | 24×7 | Email: soc-t1@company.com<br>Chat: #soc-tier1 |
| **SOC Tier 2** | Business Hours | Email: soc-t2@company.com<br>Chat: #soc-tier2 |
| **SOC Lead** | Business Hours | Email: soc-lead@company.com<br>Cell (Emergency): [PHONE] |
| **On-Call (After Hours)** | Nights/Weekends | Pager: [PAGER NUMBER]<br>Backup: [PHONE] |

### 9.2 Escalation Contacts

| Team | Contact | When to Contact |
|------|---------|-----------------|
| **Incident Response** | Email: ir-team@company.com<br>Chat: #incident-response | True Positive, Confirmed Compromise |
| **Security Engineering** | Email: sec-eng@company.com<br>Chat: #sec-engineering | Tool Issues, Detection Tuning, Coverage Gaps |
| **CISO Office** | Email: ciso-office@company.com | Critical Incidents, Policy Questions |

### 9.3 System Owner Contacts

| System Type | Primary Contact | Secondary Contact |
|-------------|-----------------|-------------------|
| **Domain Controllers** | Windows Infra Team<br>winfra@company.com | IT Operations<br>itops@company.com |
| **Databases** | Database Team<br>dbteam@company.com | App Owners (varies) |
| **Network Devices** | Network Security<br>netsec@company.com | Network Operations<br>netops@company.com |
| **Cloud Infrastructure** | Cloud Platform Team<br>cloudteam@company.com | DevOps<br>devops@company.com |

---

## 10. Key Metrics to Know

### 10.1 SOC Performance Metrics

| Metric | Target | How Measured |
|--------|--------|--------------|
| **MTTA** (Acknowledge) | <5 min (Critical)<br><15 min (High) | Time from alert → acknowledged |
| **MTTT** (Triage) | <15 min (Critical)<br><1 hr (High) | Time from alert → triaged |
| **MTTI** (Investigate) | <1 hr (Critical)<br><4 hr (High) | Time from triage → investigation complete |
| **False Positive Rate** | <20% | (False Positives / Total Alerts) × 100 |
| **True Positive Rate** | >80% of escalations | (Confirmed Incidents / Escalations) × 100 |

**Check SOC Dashboard**: [DASHBOARD URL] for real-time metrics.

### 10.2 Coverage Metrics

| Metric | Target | Status |
|--------|--------|--------|
| **Critical Systems Monitored** | 100% | [CHECK STATUS] |
| **High Systems Monitored** | ≥95% | [CHECK STATUS] |
| **Log Sources Active** | ≥98% | [CHECK STATUS] |
| **Baselines Established** | 100% (Critical)<br>≥80% (High) | [CHECK STATUS] |

---

## 11. Common Commands / Queries

### 11.1 SIEM Quick Searches (Example Syntax - Adapt to Your SIEM)

**Failed Authentication Events**:
```
index=windows EventCode=4625 
| stats count by src_ip, user
| where count > 10
```

**Successful Logins After Failed Attempts**:
```
index=windows EventCode=4625 OR EventCode=4624
| transaction src_ip user maxspan=1h
| where eventcount > 10 AND EventCode=4624
```

**Outbound Connections to External IPs**:
```
index=firewall action=allowed direction=outbound
| where NOT (dest_ip IN internal_networks)
| stats sum(bytes) by dest_ip, dest_port
```

**Process Execution on Servers**:
```
index=windows EventCode=4688 host=PROD-*
| stats count by process_name, user, host
| where count > 100
```

### 11.2 Useful Commands (Linux/Windows)

**Check Active Connections (Linux)**:
```bash
netstat -tuln | grep ESTABLISHED
ss -tuln
```

**Check Active Connections (Windows)**:
```powershell
netstat -ano | findstr ESTABLISHED
Get-NetTCPConnection | Where-Object {$_.State -eq "Established"}
```

**Check Running Processes (Linux)**:
```bash
ps aux | grep [suspicious_process]
top -b -n 1 | head -20
```

**Check Running Processes (Windows)**:
```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 20
tasklist /v
```

---

## 12. Compliance Quick Reference

**ISO 27001:2022 Controls Addressed**:
- **A.8.15**: Logging - Log collection and retention
- **A.8.16**: Monitoring - This entire policy framework
- **A.5.24**: Incident Response - Alert escalation and IR coordination

**Retention Requirements**:
- Security logs: 1 year minimum
- Hot storage (searchable): 90 days
- Compliance reports: 3 years (varies by regulation)

**Audit Evidence**:
- Baseline documentation (Annex B templates)
- Alert response records (triage documentation)
- SLA compliance reports (MTTA/MTTT metrics)
- Detection rule versioning (change history)

---

## 13. Emergency Procedures

### 13.1 Critical Alert Response

**If Critical Alert Fires**:
1. ⏰ **Acknowledge within 5 minutes**
2. 🚨 **Page on-call if after hours**
3. 🔍 **Start triage immediately** (use Annex C playbooks)
4. 📞 **Notify SOC Lead within 15 minutes**
5. 📝 **Document everything** (timestamps, actions, findings)

### 13.2 System Down / Monitoring Outage

**If SIEM/Monitoring Platform Down**:
1. 🚨 **Notify SOC Lead immediately**
2. 📝 **Document outage start time**
3. 🔄 **Attempt manual log collection** (if feasible)
4. 📞 **Escalate to Security Engineering**
5. 📊 **Post-outage: Identify missed alerts** (review logs after system restored)

### 13.3 Mass Alert Event (Alert Storm)

**If >50 Alerts Fire in <10 Minutes**:
1. 🛑 **Don't panic** - likely single root cause
2. 🔍 **Identify pattern** (same alert type? same system? same user?)
3. 📞 **Escalate to Tier 2 immediately**
4. 💭 **Hypothesis**: System issue? Attack? Detection misconfiguration?
5. 🎯 **Triage highest severity first**, batch-close if same root cause confirmed

---

## 14. Quick Decision Trees

### 14.1 "Should I Escalate This Alert?"
```
Is it a confirmed security event?
├─ YES → Escalate to IR
└─ NO → Continue...
    │
    Can I determine disposition within SLA?
    ├─ YES → Triage and close (or escalate if TP)
    └─ NO → Escalate to Tier 2
        │
        Is it Critical or High severity?
        ├─ YES → Escalate immediately
        └─ NO → Document and escalate if near SLA deadline
```

### 14.2 "Is This a False Positive?"
```
Did the event actually happen?
├─ NO → False Positive (e.g., scanner misidentified)
└─ YES → Continue...
    │
    Is it malicious or unauthorized?
    ├─ YES → True Positive (escalate)
    └─ NO → Benign True Positive (close with notes)
        │
        Examples:
        • User password typo (benign TP)
        • Authorized security scan (benign TP)
        • Scheduled maintenance (benign TP)
```

---

**END OF DOCUMENT**

---

## Appendix: One-Page Desk Reference (Print This!)
```
╔═══════════════════════════════════════════════════════════════╗
║           MONITORING ACTIVITIES - QUICK REFERENCE             ║
╠═══════════════════════════════════════════════════════════════╣
║ SEVERITY        │ RESPONSE TIME  │ ESCALATION TRIGGER         ║
║─────────────────┼────────────────┼────────────────────────────║
║ Critical (P1)   │ <15 minutes    │ Active attack, compromise  ║
║ High (P2)       │ <1 hour        │ Malware, brute force       ║
║ Medium (P3)     │ <4 hours       │ Baseline deviation         ║
║ Low (P4)        │ <1 day         │ Informational alerts       ║
╠═══════════════════════════════════════════════════════════════╣
║ ESCALATION PATHS                                              ║
║ Technical:   Tier 1 → Tier 2 → Tier 3 → Security Eng         ║
║ Incident:    SOC → IR → CISO → Executive                     ║
║ After Hours: Page [PAGER] or Call [SOC LEAD CELL]            ║
╠═══════════════════════════════════════════════════════════════╣
║ TRIAGE STEPS (EVERY ALERT)                                    ║
║ 1. Acknowledge (claim ownership)                              ║
║ 2. Read alert (understand what triggered)                     ║
║ 3. Gather context (user, asset, threat intel)                ║
║ 4. Determine disposition (TP / FP / Benign / Investigate)    ║
║ 5. Document (findings, rationale, actions)                    ║
╠═══════════════════════════════════════════════════════════════╣
║ ALWAYS ESCALATE                                               ║
║ ✓ Any malware detection                                       ║
║ ✓ Confirmed compromise                                        ║
║ ✓ Data exfiltration                                          ║
║ ✓ Can't determine disposition within SLA                     ║
╠═══════════════════════════════════════════════════════════════╣
║ CONTACTS                                                       ║
║ SOC Tier 2:        soc-t2@company.com                        ║
║ Incident Response: ir-team@company.com                        ║
║ On-Call (24×7):    [PAGER NUMBER]                            ║
║ SOC Lead:          [CELL PHONE] (Emergency)                   ║
╚═══════════════════════════════════════════════════════════════╝
```

---

*"This guide is your compass. The playbooks are your map. Your judgment is your destination."*  
*—SOC Wisdom*

*"When in doubt, escalate. When certain, document. When done, improve."*  
*—The SOC Analyst's Mantra*

*"Cargo cult security: We have a quick reference guide! (Do people actually use it?) Well, it exists..."*  
*—Feynman's Ghost, Haunting Every ISMS Audit*