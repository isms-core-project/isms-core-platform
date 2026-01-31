# ISMS Control A.8.12 - Data Leakage Prevention
## Claude Implementation Roadmap — POL Layer

---

## 1. Project Context

### 1.1 What We're Building
ISMS Control A.8.12 (Data Leakage Prevention) documentation following ISO/IEC 27001:2022, using the **System Engineering approach** established in Controls 8.23 (Web Filtering) and 8.24 (Cryptography).

### 1.2 Key Principles
- **Vendor-agnostic:** NO specific product names in policies (generic requirements only)
- **Modular structure:** Each document <400 lines for timeout prevention and auditability
- **System Engineering:** Python-generated Excel workbooks, not checkbox theater
- **Denglisch approach:** English IT terms preserved even in German documents
- **No "Maybe":** Response values are Yes/No/Partial/Planned/N/A only

### 1.3 Reference Documents in Project Knowledge
- `ISMS Control A.8.23 - Web Filtering Policy.md` — Framework template (fil rouge)
- `ISMS-POL-A.8.24 - Use of Cryptography Policy.md` — Established pattern
- `ISMS-IMP-A.8.24.3 - Authentication Assessment.md` — Assessment spec example
- `27002-2022_Controls_Umsetzungshinweise.pdf` — ISO 27002 guidance (German)

---

## 2. Regulatory Scoping (MUST Include)

Every POL document MUST reference this scoping framework:

```markdown
### Applicability of Regulatory Frameworks

**Mandatory Compliance:**
- Swiss Federal Data Protection Act (FADP)
- EU GDPR (where applicable)
- ISO/IEC 27001:2022

**Informational Reference / Best Practice:**
- NIST Special Publications (SP 800-series)

**US Federal Requirements:**
Apply ONLY where organization acts as contractor to US federal agencies
or has explicit contractual obligations. Otherwise informational only.
```

---

## 3. Naming Conventions

### 3.1 Document IDs
| Type | Format | Example |
|------|--------|---------|
| Master Policy | ISMS-POL-A.8.12 | ISMS-POL-A.8.12.md |
| Policy Sections | ISMS-POL-A.8.12-S[N] | ISMS-POL-A.8.12-S1.md |
| Sub-sections | ISMS-POL-A.8.12-S[N].[N] | ISMS-POL-A.8.12-S2.1.md |
| Annexes | ISMS-POL-A.8.12-S5.[A-Z] | ISMS-POL-A.8.12-S5.A.md |
| Assessment Specs | ISMS-IMP-A.8.12.[1-5] | ISMS-IMP-A.8.12.1.md |

### 3.2 File Naming
```
ISMS-POL-A.8.12-S2.1 - Data Classification Requirements.md
ISMS-IMP-A.8.12.1 - DLP Infrastructure Assessment.md
```

---

## 4. Document Control Block (Standard Header)

Every POL document MUST start with:

```markdown
## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-POL-A.8.12-S[X] |
| **Title** | [Document Title] |
| **Parent Document** | ISMS-POL-A.8.12 |
| **Version** | 1.0 |
| **Effective Date** | [DATE] |
| **Review Cycle** | Annual |
| **Owner** | Information Security Officer |
| **Classification** | Internal |
```

---

## 5. POL Documents — Status Tracker

### 5.1 Completed ✅
| Document ID | Title | Status |
|-------------|-------|--------|
| ISMS-POL-A.8.12 | Master Policy Framework | ✅ DONE |

### 5.2 To Be Created 📝

| Priority | Document ID | Title | Est. Lines | Key Content |
|----------|-------------|-------|------------|-------------|
| **1** | ISMS-POL-A.8.12-S1 | Purpose, Scope & Definitions | ~200 | Terminology, scope boundaries, exclusions |
| **2** | ISMS-POL-A.8.12-S2 | DLP Requirements Overview | ~150 | Introduction to requirements sections |
| **3** | ISMS-POL-A.8.12-S2.1 | Data Classification & Identification | ~250 | What data to protect, classification levels, identification methods |
| **4** | ISMS-POL-A.8.12-S2.2 | Channel Protection Requirements | ~300 | Email, Web, Endpoint, Network, Cloud, Mobile channels |
| **5** | ISMS-POL-A.8.12-S2.3 | Monitoring & Detection | ~250 | Alerting, logging, analysis, thresholds |
| **6** | ISMS-POL-A.8.12-S2.4 | Incident Response & Remediation | ~250 | DLP event handling, escalation, remediation |
| **7** | ISMS-POL-A.8.12-S3 | Roles & Responsibilities | ~200 | RACI matrix, role definitions |
| **8** | ISMS-POL-A.8.12-S4 | Policy Governance | ~200 | Review cycle, exceptions, compliance measurement |
| **9** | ISMS-POL-A.8.12-S5.A | DLP Channel Standards | ~200 | Technical standards per channel |
| **10** | ISMS-POL-A.8.12-S5.B | Exception Request Template | ~100 | Form template for DLP exceptions |
| **11** | ISMS-POL-A.8.12-S5.C | Incident Response Procedures | ~200 | Step-by-step DLP incident handling |
| **12** | ISMS-POL-A.8.12-S5.D | Quick Reference Guide | ~100 | One-pager for end users |

**Total: 13 POL documents (1 done, 12 remaining)**

---

## 6. Content Guidelines per Document

### 6.1 S1 - Purpose, Scope & Definitions
```
- Purpose statement (why DLP matters)
- Scope inclusions (systems, data, users)
- Scope exclusions (what's NOT covered)
- Definitions/Glossary:
  - Data Leakage Prevention (DLP)
  - Sensitive Data / Confidential Information
  - Data Loss vs Data Leakage (distinction!)
  - Egress Channel
  - Data Classification
  - Data at Rest / In Transit / In Use
  - Exfiltration
  - False Positive / False Negative
  - Policy Rule / DLP Rule
- Abbreviations table
```

### 6.2 S2 - DLP Requirements Overview
```
- Brief introduction to requirement sections
- Link to S2.1, S2.2, S2.3, S2.4
- Requirement hierarchy (SHALL/MUST/SHOULD/MAY)
- Compliance measurement approach
```

### 6.3 S2.1 - Data Classification & Identification
```
- Classification levels (Public, Internal, Confidential, Restricted)
- Data categories requiring DLP:
  - Personal Data (PII/PbD)
  - Financial Data
  - Health Data
  - Intellectual Property
  - Credentials/Secrets
- Identification methods:
  - Content inspection (keywords, patterns, regex)
  - Context-based (source, destination, user)
  - Fingerprinting (exact/partial match)
  - Machine learning classification
- Labeling requirements
- Data discovery/inventory requirements
```

### 6.4 S2.2 - Channel Protection Requirements
```
FOR EACH CHANNEL (Email, Web, Endpoint, Network, Cloud, Mobile):
- Requirements (SHALL/SHOULD statements)
- Protection capabilities expected
- Minimum coverage expectations
- Exception handling

Channel list:
1. Email (SMTP, Webmail, Exchange Online, attachments)
2. Web/Cloud (HTTP uploads, SaaS, cloud storage)
3. Endpoint (USB, print, clipboard, screenshots)
4. Network (SMB, FTP, file shares)
5. Applications (DB exports, APIs, reporting)
6. Mobile (BYOD, MDM-managed)
```

### 6.5 S2.3 - Monitoring & Detection
```
- Logging requirements (what to log)
- Log retention requirements
- Real-time alerting requirements
- Alert severity levels
- Dashboard/reporting requirements
- Analysis and review frequency
- Integration with SIEM
- Privacy considerations (employee monitoring)
```

### 6.6 S2.4 - Incident Response & Remediation
```
- DLP incident definition
- Severity classification
- Escalation matrix
- Response procedures (block, alert, quarantine)
- Investigation requirements
- Remediation actions
- Documentation requirements
- Lessons learned process
- Integration with incident management (link to other controls)
```

### 6.7 S3 - Roles & Responsibilities
```
RACI matrix for:
- CISO
- Information Security Officer
- Security Engineering
- IT Operations
- Data Owners
- System Owners
- Employees
- HR (for policy violations)
- Legal (for monitoring compliance)
```

### 6.8 S4 - Policy Governance
```
- Policy review cycle
- Change management process
- Exception process (criteria, approval, time limits)
- Compliance measurement
- Non-compliance handling
- Training requirements
- Audit support
```

### 6.9 S5.A - DLP Channel Standards
```
Technical reference per channel:
- Recommended capabilities
- Minimum configuration standards
- Integration requirements
- Testing requirements
(Still vendor-agnostic but more technical detail)
```

### 6.10 S5.B - Exception Request Template
```
Form fields:
- Requestor info
- Exception type
- Business justification
- Risk assessment
- Compensating controls
- Duration requested
- Approval workflow
```

### 6.11 S5.C - Incident Response Procedures
```
Step-by-step procedures:
1. Detection & Triage
2. Initial Assessment
3. Containment
4. Investigation
5. Remediation
6. Reporting
7. Closure
Flowchart/decision tree format
```

### 6.12 S5.D - Quick Reference Guide
```
One-page summary for end users:
- Do's and Don'ts
- How to request exceptions
- How to report incidents
- Contact information
- Common scenarios
```

---

## 7. Style Guidelines

### 7.1 Requirement Language
| Keyword | Meaning |
|---------|---------|
| **SHALL / MUST** | Mandatory requirement |
| **SHOULD** | Recommended, deviation needs justification |
| **MAY** | Optional |
| **SHALL NOT / MUST NOT** | Prohibited |

### 7.2 Formatting Rules
- Use tables for structured information
- Use code blocks for examples/templates
- Headers: ## for main sections, ### for subsections
- Keep paragraphs concise
- NO bullet points in prose (per user preference) unless essential
- Minimal bold emphasis

### 7.3 Cross-References
Format: `See ISMS-POL-A.8.12-S2.1 Section 3.2`

### 7.4 Output Format
- All markdown outputs in code windows (```markdown)
- Maximum 300-400 lines per document to avoid timeout

---

## 8. DLP-Specific Technical Context

### 8.1 Core DLP Concepts
```
Data States:
- At Rest (storage)
- In Transit (network)
- In Use (endpoint)

DLP Modes:
- Monitor/Audit (log only)
- Warn (notify user, allow)
- Block (prevent action)
- Quarantine (hold for review)
- Encrypt (force encryption)

Detection Methods:
- Keyword matching
- Regular expressions (patterns)
- Data fingerprinting
- Machine learning/AI
- Context analysis
```

### 8.2 Common Egress Vectors
```
Email: Attachments, body text, headers
Web: Form uploads, cloud storage, webmail
Endpoint: USB, Bluetooth, print, clipboard, screen capture
Network: FTP, SMB shares, unauthorized protocols
Cloud: SaaS apps, IaaS storage, shadow IT
Mobile: Camera, screenshots, app data sharing
```

---

## 9. Legal Considerations (MUST Address)

DLP involves employee monitoring. Every relevant document MUST acknowledge:

```markdown
### Legal & Privacy Considerations

DLP implementation involves monitoring user activities and communications.
Organizations SHALL:

- Establish legal basis for monitoring (FADP/GDPR compliance)
- Ensure proportionality (security need vs. privacy impact)
- Provide transparency (policy notification to employees)
- Limit access (need-to-know for DLP alerts/logs)
- Define retention (aligned with legal requirements)
- Document purpose limitation (DLP data used only for security)
```

---

## 10. Easter Eggs (Optional, Subtle)

Maintain tradition from 8.23/8.24:
- Feynman quotes on self-deception
- Michel Rocard quote on stupidity vs conspiracy
- Subtle humor in comments (harmless, removable)

Example:
```markdown
*"The first principle is that you must not fool yourself—
and you are the easiest person to fool."* — Richard Feynman
```

---

## 11. Workflow for Each Document

```
1. User requests document (e.g., "Let's do S1")
2. Claude searches project knowledge for patterns
3. Claude creates document following this roadmap
4. Output in markdown code block
5. User reviews, provides feedback
6. Claude updates as needed
7. Move to next document
```

---

## 12. IMP Layer (Future - After POL Complete)

Once all POL documents are done, we proceed to:

| Phase | Documents |
|-------|-----------|
| IMP Specs | ISMS-IMP-A.8.12.[1-5].md (5 assessment specifications) |
| Generators | generate_a812_[1-5]_*.py (5 Python scripts) |
| Validators | excel_sanity_check_a812_[1-5].py (reuse patterns from 8.24) |

---

## 13. Current Status

**Last Updated:** [Current Date]
**POL Progress:** 1/13 documents complete
**Next Document:** ISMS-POL-A.8.12-S1 (Purpose, Scope & Definitions)

---

**END OF ROADMAP**

*Paste this into new chat sessions to maintain continuity.*