# ISMS Control A.8.10 - Information Deletion
## Implementation Roadmap (System Engineering Approach)

---

**Document ID:** ISMS-A.8.10-ROADMAP  
**Control:** ISO/IEC 27001:2022 Annex A Control 8.10 - Löschung von Informationen  
**Approach:** System Engineering Methodology (following A.8.23/A.8.24 pattern)  
**Status:** Planning Phase

---

## 1. Control Overview

### 1.1 ISO/IEC 27002:2022 Control 8.10 - Information Deletion

**Control Statement (EN):**
> *Information stored in information systems, devices or in any other storage media should be deleted when no longer required.*

**Purpose:**
> Prevent unnecessary exposure of sensitive data and compliance with legal, statutory, regulatory and contractual requirements for data deletion.

### 1.2 Key Requirements (from ISO 27002:2022)

The standard requires organizations to:

| Requirement Area | Description |
|-----------------|-------------|
| **Deletion Methods** | Select appropriate deletion method (overwriting, cryptographic erasure) per business requirements and applicable laws |
| **Evidence/Records** | Record deletion results as evidence |
| **Third-Party Verification** | Obtain deletion confirmation from service providers |
| **Contractual Requirements** | Include deletion requirements in third-party agreements |
| **Retention Alignment** | Delete per data retention policies when no longer needed |
| **Automated Deletion** | Configure systems for secure destruction when retention expires |
| **Version/Copy Management** | Delete outdated versions, copies, and temporary files |
| **Approved Tools** | Use approved, secure deletion software |
| **Certified Providers** | Use certified secure disposal service providers |
| **Media-Appropriate Methods** | Use disposal mechanisms suited to storage media type |
| **Cloud Services** | Verify cloud provider deletion methods are acceptable |
| **Physical Device Handling** | Protect sensitive info before returning devices to vendors |
| **Logging** | Track/log deletion operations based on data sensitivity |

### 1.3 Related Controls (Integration Points)

| Control | Integration |
|---------|-------------|
| A.5.9 | Asset Inventory → Deletion requires knowing what assets contain data |
| A.5.10 | Acceptable Use → Defines user responsibilities for data handling |
| A.5.12 | Data Classification → Classification drives deletion requirements |
| A.5.13 | Labeling → Ensures data requiring deletion is identifiable |
| A.5.33 | Protection of Records → Retention vs. deletion requirements |
| A.5.34 | Privacy/PII Protection → GDPR/FADP deletion rights |
| A.7.10 | Storage Media → Physical destruction requirements |
| A.7.14 | Secure Disposal → Equipment disposal with data sanitization |
| A.8.10 | THIS CONTROL |
| A.8.24 | Cryptography → Cryptographic erasure methods |

---

## 2. Regulatory Scoping (Per ISMS-POL-00)

### 2.1 Mandatory Compliance

| Regulation | Deletion Requirements |
|------------|----------------------|
| **Swiss FADP** | Art. 6 (Purpose limitation), Right to erasure, proportionality |
| **EU GDPR** | Art. 17 (Right to erasure/"Right to be forgotten") |
| **ISO 27001:2022** | Control A.8.10 implementation required for certification |

### 2.2 Informational Reference / Best Practice

| Framework | Relevance |
|-----------|-----------|
| **NIST SP 800-88** | Guidelines for Media Sanitization (Clear/Purge/Destroy) |
| **ISO/IEC 27040** | Storage security guidance including sanitization |
| **ISO/IEC 27555** | Deletion of PII (specific guidance) |
| **ISO/IEC 27017** | Cloud services - user data deletion guidance |
| **DoD 5220.22-M** | Historical reference for secure overwrite |

### 2.3 Conditional Applicability

| Regulation | Condition |
|------------|-----------|
| **US Federal (NIST SP 800-88)** | Only if contractor/subcontractor to US federal agencies |
| **PCI DSS** | Only if processing payment card data |
| **HIPAA** | Only if handling US healthcare data |
| **Sector-specific** | Financial services, healthcare, etc. retention rules |

---

## 3. Framework Structure

### 3.1 Policy Layer (~13 documents)

```
ISMS-POL-A.8.10 (Master) ← Main Policy Document
├── S1 - Purpose, Scope, Definitions
├── S2 - Requirements Overview
│   ├── S2.1 - Retention & Deletion Triggers
│   ├── S2.2 - Deletion Methods by Media Type
│   ├── S2.3 - Verification & Evidence Requirements
│   └── S2.4 - Third-Party & Cloud Deletion
├── S3 - Roles & Responsibilities
├── S4 - Policy Governance
└── S5 - Annexes
    ├── S5.A - Approved Deletion Methods Matrix
    ├── S5.B - Data Subject Erasure Request Form
    ├── S5.C - Deletion Verification Checklist
    └── S5.D - Quick Reference Guide
```

### 3.2 Assessment/Implementation Layer (5 Excel Workbooks)

| ID | Assessment Area | Sheets | Purpose |
|----|----------------|--------|---------|
| **IMP-A.8.10.1** | Data Retention & Deletion Triggers | ~8 | Map data categories to retention periods and deletion triggers |
| **IMP-A.8.10.2** | Deletion Methods Assessment | ~10 | Assess deletion capabilities by media/platform type |
| **IMP-A.8.10.3** | Third-Party & Cloud Deletion | ~8 | Document cloud/vendor deletion capabilities and SLAs |
| **IMP-A.8.10.4** | Verification & Evidence Management | ~8 | Track deletion certificates, logs, and audit evidence |
| **IMP-A.8.10.5** | Compliance Dashboard | ~6 | Consolidated compliance metrics and gap analysis |

### 3.3 Automation Layer (5 Python Generators)

```
generate_a810_1_retention_triggers.py
generate_a810_2_deletion_methods.py
generate_a810_3_third_party_cloud.py
generate_a810_4_verification_evidence.py
generate_a810_5_compliance_dashboard.py
```

---

## 4. Implementation Phases

### Phase 1: Foundation (Week 1-2)

| # | Deliverable | Lines | Status |
|---|------------|-------|--------|
| 1.1 | ISMS-POL-A.8.10 (Master Policy) | ~300 | To Do |
| 1.2 | ISMS-POL-A.8.10-S1 (Purpose, Scope, Definitions) | ~350 | To Do |
| 1.3 | ISMS-POL-A.8.10-S3 (Roles & Responsibilities) | ~250 | To Do |

### Phase 2: Requirements (Week 2-3)

| # | Deliverable | Lines | Status |
|---|------------|-------|--------|
| 2.1 | ISMS-POL-A.8.10-S2 (Requirements Overview) | ~200 | To Do |
| 2.2 | ISMS-POL-A.8.10-S2.1 (Retention & Deletion Triggers) | ~350 | To Do |
| 2.3 | ISMS-POL-A.8.10-S2.2 (Deletion Methods by Media) | ~350 | To Do |
| 2.4 | ISMS-POL-A.8.10-S2.3 (Verification & Evidence) | ~300 | To Do |
| 2.5 | ISMS-POL-A.8.10-S2.4 (Third-Party & Cloud) | ~300 | To Do |

### Phase 3: Governance & Annexes (Week 3-4)

| # | Deliverable | Lines | Status |
|---|------------|-------|--------|
| 3.1 | ISMS-POL-A.8.10-S4 (Policy Governance) | ~200 | To Do |
| 3.2 | ISMS-POL-A.8.10-S5.A (Deletion Methods Matrix) | ~300 | To Do |
| 3.3 | ISMS-POL-A.8.10-S5.B (Erasure Request Form) | ~200 | To Do |
| 3.4 | ISMS-POL-A.8.10-S5.C (Verification Checklist) | ~200 | To Do |
| 3.5 | ISMS-POL-A.8.10-S5.D (Quick Reference Guide) | ~150 | To Do |

### Phase 4: Implementation Specifications (Week 4-5)

| # | Deliverable | Lines | Status |
|---|------------|-------|--------|
| 4.1 | ISMS-IMP-A.8.10.1 Spec (Retention Triggers) | ~400 | To Do |
| 4.2 | ISMS-IMP-A.8.10.2 Spec (Deletion Methods) | ~500 | To Do |
| 4.3 | ISMS-IMP-A.8.10.3 Spec (Third-Party/Cloud) | ~400 | To Do |
| 4.4 | ISMS-IMP-A.8.10.4 Spec (Verification/Evidence) | ~350 | To Do |
| 4.5 | ISMS-IMP-A.8.10.5 Spec (Dashboard) | ~400 | To Do |

### Phase 5: Excel Generators (Week 5-7)

| # | Deliverable | Est. Lines | Status |
|---|------------|------------|--------|
| 5.1 | generate_a810_1_retention_triggers.py | ~800-1000 | To Do |
| 5.2 | generate_a810_2_deletion_methods.py | ~900-1100 | To Do |
| 5.3 | generate_a810_3_third_party_cloud.py | ~700-900 | To Do |
| 5.4 | generate_a810_4_verification_evidence.py | ~600-800 | To Do |
| 5.5 | generate_a810_5_compliance_dashboard.py | ~800-1000 | To Do |

### Phase 6: Validation & Testing (Week 7-8)

| # | Deliverable | Status |
|---|------------|--------|
| 6.1 | Reuse excel_sanity_check.py (adapted) | To Do |
| 6.2 | Generate sample workbooks | To Do |
| 6.3 | Validate formulas and cross-references | To Do |
| 6.4 | Stakeholder review | To Do |

---

## 5. Domain-Specific Content

### 5.1 IMP-A.8.10.1 - Retention & Deletion Triggers

**Sheets:**
1. Instructions & Legend
2. Data_Categories_Inventory
3. Retention_Periods_Matrix
4. Deletion_Triggers
5. Legal_Hold_Register
6. Automated_Deletion_Config
7. Summary_Dashboard
8. Evidence_Register
9. Approval_Sign_Off

**Key Questions:**
- What data categories exist in the organization?
- What are the retention periods per category/regulation?
- What triggers deletion (expiry, request, contract end)?
- Are legal holds properly managed?

### 5.2 IMP-A.8.10.2 - Deletion Methods Assessment

**Sheets:**
1. Instructions & Legend
2. Storage_Media_Inventory
3. Software_Deletion_Tools
4. Physical_Destruction_Methods
5. Cryptographic_Erasure
6. Method_Capability_Matrix
7. Gap_Analysis
8. Summary_Dashboard
9. Evidence_Register
10. Approval_Sign_Off

**Key Media Types:**
- HDDs (magnetic) → DoD 5220.22-M, degaussing, physical destruction
- SSDs → Secure erase, cryptographic erasure
- Flash/USB → Secure erase, physical destruction
- Tapes → Degaussing, physical destruction
- Paper → Cross-cut shredding (DIN 66399)
- Cloud storage → Cryptographic erasure, vendor processes
- Virtual machines → Secure wipe, storage pool management
- Mobile devices → Factory reset + crypto erasure
- Databases → Secure DELETE + vacuum/rebuild

### 5.3 IMP-A.8.10.3 - Third-Party & Cloud Deletion

**Sheets:**
1. Instructions & Legend
2. Cloud_Provider_Inventory
3. Third_Party_Vendor_Register
4. Deletion_SLAs_Matrix
5. Contractual_Requirements
6. Deletion_Verification_Log
7. Gap_Analysis
8. Evidence_Register
9. Approval_Sign_Off

**Key Questions:**
- Which cloud providers hold organizational data?
- What deletion methods do providers offer?
- Do contracts include deletion clauses?
- How is deletion verified/certified?

### 5.4 IMP-A.8.10.4 - Verification & Evidence

**Sheets:**
1. Instructions & Legend
2. Deletion_Request_Log
3. Deletion_Certificate_Register
4. Audit_Log_Repository
5. Physical_Destruction_Certificates
6. Third_Party_Confirmations
7. Compliance_Verification
8. Evidence_Register
9. Approval_Sign_Off

**Evidence Types:**
- Deletion request forms (data subject requests)
- System deletion logs
- Physical destruction certificates
- Cloud provider deletion confirmations
- Audit trail exports
- Photographic evidence (physical destruction)

### 5.5 IMP-A.8.10.5 - Compliance Dashboard

**Sheets:**
1. Instructions & Legend
2. Executive_Summary
3. Retention_Compliance
4. Deletion_Method_Coverage
5. Third_Party_Compliance
6. Critical_Gaps
7. Trend_Analysis

---

## 6. Key Differentiators from A.8.23/A.8.24

| Aspect | A.8.23 (Web Filtering) | A.8.24 (Cryptography) | A.8.10 (Deletion) |
|--------|----------------------|----------------------|-------------------|
| Focus | Network protection | Data protection | Data lifecycle end |
| Primary Asset | Network traffic | Encrypted data | Stored data/media |
| Third-Party Role | Minimal | Moderate (CAs) | Critical (cloud/vendors) |
| Verification | Blocking logs | Crypto configs | Deletion certificates |
| Regulatory Driver | Productivity/security | Data protection | GDPR Art. 17 / FADP |
| Physical Component | Minimal | HSMs | Media destruction |
| Time Dimension | Real-time | Key lifecycle | Retention periods |

---

## 7. Critical Success Factors

### 7.1 Audit Readiness Checklist

- [ ] All data categories mapped to retention periods
- [ ] Deletion methods documented per media type
- [ ] Third-party deletion requirements in contracts
- [ ] Deletion certificates collected and stored
- [ ] Data subject erasure process documented
- [ ] Legal hold procedures defined
- [ ] Evidence of deletion maintained for audit
- [ ] Exception process for extended retention

### 7.2 Common Audit Findings (to prevent)

| Finding | Prevention Measure |
|---------|-------------------|
| "No documented retention policy" | IMP-A.8.10.1 comprehensive |
| "Cannot prove deletion occurred" | IMP-A.8.10.4 evidence mgmt |
| "Third-party deletion not verified" | IMP-A.8.10.3 SLAs + certs |
| "Backup tapes never purged" | Include backups in media inventory |
| "Dev/test data not deleted" | Include non-prod environments |
| "Legacy systems excluded" | Full scope in POL-S1 |

---

## 8. Recommended Execution Order

```
Week 1:   POL-A.8.10 (Master) + S1 (Purpose/Scope) + S3 (Roles)
Week 2:   S2 (Requirements Overview) + S2.1 (Retention Triggers)
Week 3:   S2.2 (Deletion Methods) + S2.3 (Verification)
Week 4:   S2.4 (Third-Party) + S4 (Governance) + S5.A-D (Annexes)
Week 5:   IMP-A.8.10.1 Spec + IMP-A.8.10.2 Spec
Week 6:   IMP-A.8.10.3 Spec + IMP-A.8.10.4 Spec + IMP-A.8.10.5 Spec
Week 7:   Python generators (1-3)
Week 8:   Python generators (4-5) + Validation + Testing
```

---

## 9. Files Reviewed / Available References

| File | Purpose |
|------|---------|
| ISMS-POL-A.8.23 - Web Filtering Policy.md | Structure reference |
| ISMS-POL-A.8.24 - Use of Cryptography Policy.md | Structure reference |
| ISMS-POL-A.8.23-S1 / A.8.24-S1 | Section structure |
| ISMS-IMP-A.8.23.1 - Threat Protection | IMP spec pattern |
| ISMS-IMP-A.8.23.5 - Compliance Dashboard | Dashboard pattern |
| imp_template.md | Template patterns |
| 27002-2022_Controls_Umsetzungshinweise.pdf | Control 8.10 German guidance |
| ISMS-POL-00 - Regulatory Framework | Scoping reference |
| generate_a823_1/5 + excel_sanity_check | Python patterns |

---

## 10. Next Steps

**Immediate Action Required:**

1. **Confirm Scope**: Any specific regulatory requirements beyond FADP/GDPR?
2. **Confirm Priority**: Start with Master Policy (POL-A.8.10) or jump to specific section?
3. **Data Categories**: Does organization have existing data classification scheme?
4. **Third-Party Focus**: Critical cloud providers to consider?

---

> *"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
*— Richard Feynman

**Translation for ISMS:** Having a "data deletion policy" that nobody follows is cargo cult compliance. The Excel workbooks force you to document WHAT you delete, HOW you delete it, and PROVE it happened.

---

**END OF ROADMAP**

*Ready to proceed with Phase 1 upon confirmation.*
