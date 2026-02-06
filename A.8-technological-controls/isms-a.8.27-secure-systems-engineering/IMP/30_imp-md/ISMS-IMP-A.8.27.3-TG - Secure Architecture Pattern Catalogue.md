**ISMS-IMP-A.8.27.3-TG - Secure Architecture Pattern Catalogue**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Architecture Pattern Catalogue |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.3-TG |
| **Assessment Domain** | Domain 3 - Architecture Patterns and Standards |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Enterprise Security Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Enterprise Security Architect | Initial pattern catalogue assessment specification |

**Review Cycle**: Annual (or after significant architecture changes)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)
- ISMS-POL-A.8.25-26-29 (Secure Development Framework)
- ISO/IEC 27002:2022 Control A.8.27
- NIST SP 800-160 Vol. 1 Rev. 1 (Engineering Trustworthy Secure Systems)
- OWASP Security Architecture Cheat Sheet

---

# Technical Specification

# Excel Workbook Specification

## Workbook Overview

| Property | Value |
|----------|-------|
| **Filename** | ISMS-IMP-A.8.27.3_Secure_Architecture_Pattern_Catalogue_YYYYMMDD.xlsx |
| **Sheets** | 10 |
| **Purpose** | Secure architecture pattern catalogue assessment |
| **Generator** | generate_a827_3_pattern_catalogue.py |

## Sheet Specifications

### Sheet 1: Instructions

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Instructions |
| **Purpose** | User guidance |
| **Protection** | Read-only |

### Sheet 2: PatternInventory

| Property | Specification |
|----------|---------------|
| **Sheet Name** | PatternInventory |
| **Purpose** | Complete pattern catalogue |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Pat-ID | 15 | Text | PAT-XXX-### format |
| B | Category | 20 | Dropdown | Pattern categories |
| C | Name | 35 | Text | Required |
| D | Version | 10 | Text | Version format |
| E | Status | 15 | Dropdown | Approved/Draft/Deprecated/Under Review |
| F | Owner | 20 | Text | Required |
| G | LastReview | 12 | Date | Date validation |
| H | NextReview | 12 | Date | Future date |
| I | DocumentRef | 25 | Text | Required |
| J | Notes | 25 | Text | Optional |

**Category Dropdown:**
Authentication, Authorisation, DataProtection, NetworkSecurity, Integration, Cloud, LoggingMonitoring, Identity, Container, Serverless

**Pre-populated Rows:** 30 standard patterns

### Sheet 3: PatternQuality

| Property | Specification |
|----------|---------------|
| **Sheet Name** | PatternQuality |
| **Purpose** | Documentation quality assessment |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Pat-ID | 15 | Dropdown | From PatternInventory |
| B | Element | 25 | Dropdown | Documentation elements |
| C | Present | 10 | Dropdown | Yes/Partial/No |
| D | Quality | 10 | Dropdown | 1/2/3/4/5 |
| E | Notes | 40 | Text | Optional |

**Element Dropdown:**
ProblemStatement, Context, Solution, SecurityRationale, Implementation, Example, AntiPatterns, RelatedPatterns, ComplianceMapping, ThreatModel

### Sheet 4: Adoption

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Adoption |
| **Purpose** | Pattern adoption tracking |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Pat-ID | 15 | Dropdown | From PatternInventory |
| B | ProjectCount | 15 | Number | Integer |
| C | TotalApplicable | 15 | Number | Integer |
| D | AdoptionRate | 15 | Formula | =B/C |
| E | Trend | 12 | Dropdown | Increasing/Stable/Decreasing |
| F | Barriers | 35 | Text | If <80% |
| G | Action | 30 | Text | Improvement action |

### Sheet 5: Governance

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Governance |
| **Purpose** | Pattern governance assessment |

**Standard governance assessment structure with 15 requirements**

### Sheet 6: Deviations

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Deviations |
| **Purpose** | Deviation tracking |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Dev-ID | 10 | Auto | DEV-001 format |
| B | Pattern | 15 | Dropdown | From PatternInventory |
| C | Project | 25 | Text | Required |
| D | Category | 20 | Dropdown | Deviation categories |
| E | Justification | 40 | Text | Required |
| F | Approved | 10 | Dropdown | Yes/No/Pending |
| G | ApprovedBy | 20 | Text | Required if Approved |
| H | Compensating | 35 | Text | Required |
| I | Expiry | 12 | Date | Future date |
| J | Status | 12 | Dropdown | Active/Closed/Expired |

### Sheet 7: Effectiveness

| Property | Specification |
|----------|---------------|
| **Sheet Name** | Effectiveness |
| **Purpose** | Pattern effectiveness metrics |

**Column Definitions:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Pat-ID | 15 | Dropdown | From PatternInventory |
| B | SecurityIncidents | 15 | Number | Integer |
| C | VulnFindings | 15 | Text | Count and severity |
| D | AuditFindings | 15 | Number | Integer |
| E | UserFeedback | 12 | Decimal | 1.0-5.0 |
| F | Effectiveness | 12 | Dropdown | High/Medium/Low |
| G | Notes | 30 | Text | Optional |

### Sheet 8: Compliance

Standard compliance sheet structure

### Sheet 9: GapRegister

Standard gap register structure

### Sheet 10: Dashboard

**Dashboard Elements:**

1. Pattern catalogue statistics (count by category, status)
2. Overall documentation quality score
3. Adoption rate by category (bar chart data)
4. Active deviations summary
5. Effectiveness summary (patterns by rating)
6. Key metrics and trends

## Pre-populated Data

**Pattern Inventory (30 patterns):**

| Category | Patterns |
|----------|----------|
| Authentication | SSO Integration, MFA Implementation, Service Authentication, Token Management |
| Authorisation | RBAC Implementation, ABAC Implementation, API Authorisation, Delegated Admin |
| Data Protection | Encryption at Rest, Encryption in Transit, Key Management, Tokenisation |
| Network Security | DMZ Architecture, Micro-segmentation, API Gateway, Zero Trust Network |
| Integration | Secure REST API, Message Queue Security, Event-Driven Security, Service Mesh |
| Cloud | Landing Zone, Workload Isolation, Serverless Security, Container Security |
| Logging | Centralised Logging, SIEM Integration, Audit Trail, Log Protection |
| Identity | Identity Lifecycle, PAM, Federation, Directory Integration |

---

# Generator Script Reference

| Property | Value |
|----------|-------|
| **Script Name** | generate_a827_3_pattern_catalogue.py |
| **Location** | 10-isms-scr-base/isms-a.8.27-secure-systems-engineering/10_generator-master/ |
| **Output** | ISMS-IMP-A.8.27.3_Secure_Architecture_Pattern_Catalogue_YYYYMMDD.xlsx |

---

**END OF SPECIFICATION**

---

*"Good judgment comes from experience, and experience comes from bad judgment. Architecture patterns capture good judgment so others need not repeat the bad."*
— Fred Brooks (paraphrased)

<!-- QA_VERIFIED: [Date] -->
