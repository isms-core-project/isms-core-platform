# ISMS-POL-A.8.15-S5
## Logging - Annexes

**Document ID**: ISMS-POL-A.8.15-S5  
**Title**: Logging - Annexes Overview  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial annexes framework |

**Review Cycle**: Annual (aligned with policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: CISO, Information Security Manager  
**Distribution**: All personnel with logging responsibilities

---

## 5.1 Purpose of Annexes

The annexes provide **supporting materials** for the logging policy framework:

- **Technical Specifications**: Detailed technical standards and configurations
- **Templates**: Standardized forms and documentation templates
- **Procedures**: Step-by-step operational procedures
- **Quick Reference**: Decision aids and frequently asked questions

Annexes are designed to be **practical operational tools** rather than policy statements.

---

## 5.2 Annex Structure

The logging policy framework includes four annexes:

### **Annex A: Logging Standards (S5.A)**
**Document ID**: ISMS-POL-A.8.15-S5.A  
**Purpose**: Technical specifications for log formats, protocols, and configurations

**Contents**:
- Syslog configuration standards (RFC 5424)
- Common Event Format (CEF) specifications
- JSON logging standards
- Timestamp format requirements (ISO 8601)
- Log field naming conventions
- Character encoding standards

**Target Audience**: System administrators, application developers, security engineers, log administrators

**When to Use**: 
- Configuring new systems to generate logs
- Developing applications with logging requirements
- Implementing log forwarding and collection
- Standardizing log formats across organization

---

### **Annex B: Log Source Template (S5.B)**
**Document ID**: ISMS-POL-A.8.15-S5.B  
**Purpose**: Standardized template for documenting and onboarding new log sources

**Contents**:
- Log source identification form
- System information checklist
- Log configuration documentation template
- Integration checklist
- Approval workflow
- Testing and validation procedures

**Target Audience**: System owners, log administrators, project managers

**When to Use**:
- Onboarding new systems, applications, or devices
- Documenting existing log sources
- Planning log collection for new projects
- Conducting log source inventory assessments

---

### **Annex C: Log Review Procedures (S5.C)**
**Document ID**: ISMS-POL-A.8.15-S5.C  
**Purpose**: Detailed operational procedures for log review activities

**Contents**:
- Daily log review procedures (what to check, how to escalate)
- Weekly log review procedures (trend analysis, reporting)
- Monthly log review procedures (management reporting)
- Incident response log analysis procedures
- Forensic investigation procedures (chain of custody, evidence handling)

**Target Audience**: SOC analysts, security engineers, incident responders, forensic investigators

**When to Use**:
- Daily operational log review
- Investigating security incidents
- Conducting forensic analysis
- Training new SOC analysts
- Auditing log review processes

---

### **Annex D: Quick Reference Guide (S5.D)**
**Document ID**: ISMS-POL-A.8.15-S5.D  
**Purpose**: Practical guidance for common scenarios and quick decision-making

**Contents**:
- Decision trees (when to log, what retention period, what protection level)
- Common scenarios and solutions
- Troubleshooting guide (missing logs, storage issues, performance problems)
- FAQ (frequently asked questions)
- Compliance quick reference (regulatory requirements by industry)

**Target Audience**: All stakeholders (general reference)

**When to Use**:
- Quick decision support during daily operations
- First-time policy users seeking guidance
- Troubleshooting common problems
- Training and onboarding
- Audit preparation

---

## 5.3 Relationship to Policy Sections

Annexes support policy requirements:

| Policy Requirement | Supporting Annex |
|-------------------|------------------|
| **S2.1: Event Logging** | S5.A (Standards), S5.B (Template) |
| **S2.2: Log Protection** | S5.A (Standards), S5.D (Quick Reference) |
| **S2.3: Log Retention** | S5.D (Quick Reference - retention guide) |
| **S2.4: Log Review** | S5.C (Procedures), S5.D (Troubleshooting) |
| **S3: Roles** | S5.C (Procedures define who does what) |

---

## 5.4 Maintenance and Updates

### 5.4.1 Update Frequency

**Annexes A, B, C**: Updated as needed when:
- Technical standards evolve
- New technologies introduced
- Operational procedures improve
- Incident lessons learned incorporated

**Annex D**: Updated quarterly to reflect:
- New FAQ questions
- Updated troubleshooting guidance
- Regulatory requirement changes

### 5.4.2 Version Control

Annexes follow same version control as policy sections:
- Major version (X.0): Significant changes
- Minor version (X.Y): Clarifications, corrections

Annexes can be updated independently without requiring full policy review.

---

## 5.5 Document Navigation

**Need technical specifications?** → Read **S5.A** (Logging Standards)

**Onboarding a new system?** → Use **S5.B** (Log Source Template)

**Conducting daily log review?** → Follow **S5.C** (Log Review Procedures)

**Need quick answer?** → Check **S5.D** (Quick Reference Guide)

**Need policy requirements?** → Read **S2.1-S2.4** (Requirements sections)

**Need to understand roles?** → Read **S3** (Roles & Responsibilities)

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S5 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **Document Type** | Policy Section - Annexes Overview |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Line Count** | ~110 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Annexes** | S5.A, S5.B, S5.C, S5.D |

---

**END OF SECTION S5**

---

*"Good documentation is like good code: it makes the complex understandable."*  
— Software Engineering Wisdom (applies to policies too)