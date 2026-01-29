# ISMS-POL-A.8.11-S2.3 — Environment Requirements
## ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document ID**: ISMS-POL-A.8.11-S2.3  
**Title**: Environment-Specific Masking Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Information Security Officer (ISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IT Operations Manager / DevOps Lead | Initial section document |

**Review Cycle**: Annual (synchronized with Master Policy review), or upon:
- Introduction of new environments (dev, test, staging, UAT)
- Infrastructure changes or cloud migrations
- Security incidents involving non-production data  

**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical: Chief Information Officer (CIO) or IT Operations Director
- Privacy/Legal: Data Protection Officer (DPO)
- Development: Development Manager / DevOps Manager

**Distribution**: IT operations, DevOps teams, cloud architects, environment owners  
**Parent Document**: ISMS-POL-A.8.11-S2 - Data Masking Requirements  
**Related Standards**: ISO/IEC 27002:2022 Control 8.11, 8.31 (Separation of environments), GDPR Article 25

---

## 1. Purpose

This section defines **WHERE data masking SHALL be applied** across the 
organization's information processing environments. This is environment-level 
guidance, not application-specific.

**What this section covers:**
- Mandatory masking environments (production, non-production, etc.)
- Environment-specific masking requirements
- Data flow masking checkpoints
- External data sharing masking requirements
- Cloud and hybrid environment considerations

**What this section does NOT cover:**
- HOW to mask (see S2.2 Masking Techniques)
- Specific data fields to mask (see implementation workbooks)
- Specific vendor tools (see implementation guides)

---

## 2. Environment Classification

The organization SHALL classify its information processing environments into 
the following categories for masking purposes:

### 2.1 Production Environments

**Definition:** Systems and databases containing **real, live data** used for 
actual business operations.

**Characteristics:**
- Contains real customer/employee/business data
- Directly impacts business operations
- Subject to regulatory compliance requirements
- Requires highest security controls

**Masking Requirement:** **CONDITIONAL**
- Sensitive data MAY remain unmasked if required for business operations
- Dynamic Data Masking (DDM) SHALL be used for role-based access
- Field-level encryption SHALL be considered for highly sensitive data
- Access to unmasked data SHALL be strictly controlled and logged

---

### 2.2 Non-Production Environments

**Definition:** Systems and databases used for development, testing, training, 
or other non-operational purposes.

**Environment Types:**
- **Development (DEV):** Software development and coding
- **Testing (TEST/QA):** Quality assurance and functional testing
- **User Acceptance Testing (UAT):** Business user validation
- **Training (TRAIN):** Employee training and demonstrations
- **Staging (STAGE):** Pre-production deployment testing
- **Sandbox (SANDBOX):** Experimental and proof-of-concept work

**Masking Requirement:** **MANDATORY**
- ALL sensitive data SHALL be masked before deployment to non-production
- Static Data Masking (SDM) SHALL be applied during data refresh
- NO production data SHALL be copied to non-production without masking
- Exceptions require documented risk acceptance and compensating controls

---

### 2.3 Analytics and Reporting Environments

**Definition:** Systems and databases used for business intelligence, 
analytics, data science, and reporting.

**Characteristics:**
- May contain aggregated or sampled data
- Used for analysis, not operational transactions
- May be shared with broader user base
- May use cloud-based analytics platforms

**Masking Requirement:** **MANDATORY**
- Individual-level PII SHALL be masked or aggregated
- Synthetic data SHALL be used for ML/AI training where possible
- Data exports for analytics SHALL be masked at source
- Re-identification risk SHALL be assessed before data release

---

### 2.4 Backup and Archive Environments

**Definition:** Long-term data storage for business continuity and regulatory 
retention.

**Characteristics:**
- Contains historical snapshots of production data
- Stored for extended periods (months to years)
- May be stored off-site or in cloud
- Subject to data protection regulations

**Masking Requirement:** **CONDITIONAL**
- Production backups MAY contain unmasked data if operationally required
- Backup encryption SHALL be applied (reference ISMS-POL-A.8.24)
- Backups for non-production restoration SHALL be masked
- Archived data for long-term retention SHALL be assessed for masking feasibility

---

### 2.5 Third-Party and External Sharing

**Definition:** Data shared with external parties including vendors, partners, 
auditors, and customers.

**Characteristics:**
- Data leaves organizational control
- Subject to contractual and regulatory obligations
- May be accessed by unknown third-party personnel
- Difficult to enforce security controls post-sharing

**Masking Requirement:** **MANDATORY**
- ALL data shared externally SHALL be masked unless contractually required
- Minimum necessary data principle SHALL apply
- Data sharing agreements SHALL specify masking requirements
- Re-identification risk SHALL be assessed before external release

---

### 2.6 Cloud Environments

**Definition:** Systems and databases hosted by third-party cloud service 
providers.

**Characteristics:**
- Data processed/stored outside direct organizational control
- Subject to cloud provider security controls
- May cross geographic/regulatory boundaries
- Multi-tenancy concerns

**Masking Requirement:** **CONDITIONAL**
- Cloud environments SHALL follow same masking requirements as on-premises
- Cloud-hosted production → CONDITIONAL masking (as per 2.1)
- Cloud-hosted non-production → MANDATORY masking (as per 2.2)
- Cloud analytics → MANDATORY masking (as per 2.3)
- Cloud backup → CONDITIONAL masking (as per 2.4)
- Client-side masking SHALL be considered before cloud upload

---

### 2.7 Endpoint and User Devices

**Definition:** Laptops, workstations, mobile devices accessing or storing 
organizational data.

**Characteristics:**
- High risk of loss or theft
- May be used in untrusted networks
- Limited security controls compared to servers
- User may have local data copies

**Masking Requirement:** **MANDATORY**
- Sensitive data downloaded to endpoints SHALL be masked
- Data exports (CSV, Excel, PDF) SHALL apply masking
- Screenshots and reports SHALL contain masked data
- Clipboard data containing sensitive information SHALL be protected

---

## 3. Environment-Specific Masking Requirements

### 3.1 Production Environment Masking

**When masking is REQUIRED in production:**

| Scenario | Masking Technique |
|----------|-------------------|
| **Customer service representatives** viewing customer data | Dynamic Data Masking (DDM) |
| **Reports** generated for non-privileged users | Redaction or DDM |
| **Audit logs** containing sensitive data | Field-level encryption or redaction |
| **Application outputs** (invoices, statements) for end-users | Partial redaction (e.g., show last 4 digits of card) |
| **Production data exports** for analysis | Static masking before export |

**When masking is NOT required in production:**
- Authorized users with legitimate business need (fully logged access)
- Application functionality requiring real data for processing
- Regulatory reporting requiring unmasked data (with appropriate controls)

**Requirements:**
- DDM SHALL be implemented for role-based masking in production
- All access to unmasked production data SHALL be logged
- Production data exports SHALL be masked unless explicitly authorized
- Masking exceptions SHALL be documented and risk-accepted

---

### 3.2 Non-Production Environment Masking

**Masking checkpoints for non-production data:**
```
Production DB → [MASKING CHECKPOINT] → Non-Production DB
```

**Mandatory masking before non-production deployment:**
1. **Data Refresh Process:**
   - Production snapshot taken
   - Static Data Masking (SDM) applied
   - Masked data loaded to non-production
   - Validation of masking effectiveness

2. **Prohibited Practices:**
   - ❌ Direct production database cloning without masking
   - ❌ "We'll mask it later" (mask BEFORE deployment)
   - ❌ "It's only test data" (test data is often production copy)
   - ❌ "Developers signed NDAs" (NDAs are not technical controls)

**Non-production environment checklist:**

| Environment | Masking Required? | Technique | Frequency |
|-------------|-------------------|-----------|-----------|
| **Development** | ✅ Yes | SDM | Every data refresh |
| **Testing** | ✅ Yes | SDM | Every data refresh |
| **UAT** | ✅ Yes | SDM | Every data refresh |
| **Training** | ✅ Yes | SDM + Substitution | Every data refresh |
| **Sandbox** | ✅ Yes | SDM | Every data refresh |
| **Staging** | ✅ Yes (unless production-identical required) | SDM or DDM | Every data refresh |

**Exception Process:**
- Non-production environments requiring unmasked data SHALL document justification
- Risk assessment SHALL be conducted
- Compensating controls SHALL be implemented (encryption, access logging, etc.)
- Exception SHALL be approved by ISO and Data Owner
- Exception SHALL be reviewed quarterly

---

### 3.3 Analytics and Reporting Environment Masking

**Masking requirements for analytics:**

1. **Business Intelligence (BI) Tools:**
   - Data extracted from production SHALL be masked
   - Aggregated reports MAY use unmasked data if aggregation prevents re-identification
   - Individual-level reports SHALL use masked data

2. **Data Warehouses:**
   - ETL processes SHALL include masking steps
   - Historical data SHALL be masked unless retention of unmasked data is justified
   - Data warehouse exports SHALL be masked

3. **Machine Learning / AI Training:**
   - Training datasets SHALL use synthetic data or masked production data
   - PII SHALL be removed or anonymized
   - Re-identification risk SHALL be assessed

4. **Ad-hoc Data Exports:**
   - All ad-hoc queries SHALL apply masking filters
   - Self-service BI tools SHALL enforce masking rules
   - CSV/Excel exports SHALL contain masked data

**Requirements:**
- Analytics platforms SHALL integrate masking at data ingestion
- Aggregation level SHALL be assessed to prevent re-identification
- Data minimization SHALL be applied (only export necessary fields)

---

### 3.4 Backup and Archive Environment Masking

**Masking considerations for backups:**

1. **Production Backups:**
   - MAY contain unmasked data if required for disaster recovery
   - SHALL be encrypted at rest (reference ISMS-POL-A.8.24)
   - SHALL be access-controlled (only authorized backup administrators)
   - SHALL be logged (all access and restoration operations)

2. **Non-Production Backups:**
   - SHALL contain only masked data
   - Backup of masked non-production databases is acceptable

3. **Archive for Long-Term Retention:**
   - Data archived for compliance SHALL be assessed for masking feasibility
   - If masking would compromise compliance requirements, encryption SHALL be used
   - Archive access SHALL be strictly controlled

**Backup restoration masking checkpoint:**
```
Backup Media → [RESTORE] → Target Environment
                              ↓
                      [MASKING CHECKPOINT if non-production]
```

**Requirements:**
- Backup restoration to non-production SHALL trigger masking process
- Backup media SHALL be encrypted if containing unmasked data
- Backup access logs SHALL be maintained

---

### 3.5 Third-Party and External Sharing Masking

**Masking requirements for external data sharing:**

1. **Vendor Access to Organizational Data:**
   - Vendors SHALL receive masked data unless contractually required
   - Data Processing Agreements SHALL specify masking requirements
   - Vendor access to unmasked data SHALL be logged and monitored
   - Vendor environments SHALL be audited for security controls

2. **Customer Data Exports:**
   - Customers downloading their own data MAY receive unmasked data (their data)
   - Customers receiving reports about others SHALL receive masked data

3. **Auditor Data Provision:**
   - Auditors MAY receive unmasked data samples if necessary for audit
   - Auditors SHALL sign confidentiality agreements
   - Audit data SHALL be masked where possible without compromising audit effectiveness

4. **Research and Academic Data Sharing:**
   - Data shared for research SHALL be anonymized or masked
   - Re-identification risk SHALL be assessed
   - Data sharing agreements SHALL prohibit re-identification attempts

**Data sharing masking checkpoint:**
```
Internal System → [MASKING CHECKPOINT] → External Party
```

**Requirements:**
- ALL external data transfers SHALL be reviewed for masking requirements
- Data sharing SHALL follow principle of least privilege (minimum necessary data)
- Data sharing agreements SHALL include masking and data protection clauses

---

### 3.6 Cloud Environment Masking

**Cloud-specific masking requirements:**

1. **Infrastructure-as-a-Service (IaaS):**
   - Follow same masking requirements as on-premises equivalents
   - Cloud production → CONDITIONAL masking (as per 2.1)
   - Cloud non-production → MANDATORY masking (as per 2.2)

2. **Platform-as-a-Service (PaaS):**
   - Data uploaded to PaaS SHALL be assessed for masking requirements
   - Database-as-a-Service (DBaaS) SHALL use DDM or encryption
   - Application hosting SHALL apply masking at application layer

3. **Software-as-a-Service (SaaS):**
   - Data entered into SaaS applications SHALL be minimized
   - SaaS exports SHALL apply masking (if exporting to non-production)
   - SaaS vendor SHALL provide masking capabilities (evaluated during procurement)

4. **Client-Side Masking for Cloud Upload:**
   - Consider masking data BEFORE uploading to cloud
   - Reduces risk of cloud provider data exposure
   - Requires coordination with application functionality

**Cloud data flow masking checkpoints:**
```
On-Premises Production → [MASKING CHECKPOINT?] → Cloud Production (conditional)
On-Premises Production → [MASKING CHECKPOINT!] → Cloud Non-Production (mandatory)
Cloud Production → [MASKING CHECKPOINT!] → On-Premises Non-Production (mandatory)
```

**Requirements:**
- Cloud environments SHALL be classified (production vs. non-production)
- Cloud provider security controls SHALL be assessed
- Data residency and sovereignty requirements SHALL be considered

---

### 3.7 Endpoint and User Device Masking

**Masking requirements for endpoint data:**

1. **Data Downloads:**
   - Users downloading data SHALL receive masked data (unless authorized)
   - Download requests SHALL be logged
   - Self-service data export tools SHALL enforce masking

2. **Reports and Screenshots:**
   - Screenshots containing sensitive data SHALL use masked views
   - Reports printed or saved SHALL contain masked data
   - Presentation materials SHALL use masked data

3. **Clipboard and Temporary Files:**
   - Applications SHALL limit sensitive data in clipboard
   - Temporary files SHALL be cleared after use
   - Data loss prevention (DLP) tools SHALL monitor endpoint data

**Requirements:**
- Endpoint data protection SHALL include masking controls
- User training SHALL cover appropriate use of sensitive data on endpoints
- Data exports SHALL default to masked unless explicitly authorized

---

## 4. Data Flow Masking Checkpoints

The organization SHALL identify and enforce masking checkpoints in data flows:

### 4.1 Checkpoint Identification

**Masking checkpoint criteria:**
- Data moves from higher security environment to lower security environment
- Data crosses trust boundary (internal → external, production → non-production)
- Data is accessed by users without full authorization
- Data is exported for purposes not requiring real values

**Example checkpoints:**
```
[Production DB] → CHECKPOINT → [Test DB]
[Production DB] → CHECKPOINT → [Analytics Platform]
[Production DB] → CHECKPOINT → [External Vendor]
[Production DB] → CHECKPOINT → [User Download]
[Production DB] → CHECKPOINT → [Backup (if non-production restore)]
[Application]   → CHECKPOINT → [User Screen (if DDM)]
```

### 4.2 Checkpoint Enforcement

**Requirements for each checkpoint:**
1. **Document checkpoint location** (system, process, data flow)
2. **Define masking technique** to be applied at checkpoint
3. **Implement technical control** (script, tool, application logic)
4. **Validate effectiveness** (test that masking occurs)
5. **Log checkpoint activity** (data passed through, masking applied)
6. **Monitor bypass attempts** (direct database access, unauthorized exports)

---

## 5. Environment-Specific Technique Mapping

The organization SHALL use appropriate masking techniques per environment:

| Environment | Recommended Techniques | Rationale |
|-------------|------------------------|-----------|
| **Production (role-based)** | Dynamic Data Masking (DDM) | Real-time masking without data modification |
| **Non-Production** | Static Data Masking (SDM), Substitution | One-time masking, preserves data utility |
| **Analytics** | Substitution, Aggregation, Synthetic Data | Preserves statistical properties |
| **Backups (production)** | Encryption | Allows restoration without re-identification risk |
| **External Sharing** | Redaction, Hashing, Tokenization | Minimizes exposure, prevents re-identification |
| **Cloud (non-prod)** | SDM before upload | Masking before data leaves premises |
| **Endpoints** | Redaction, Partial Masking | User-friendly but protected |

---

## 6. Geographic and Regulatory Considerations

The organization SHALL consider geographic-specific masking requirements:

### 6.1 Data Residency

- Data processed in certain jurisdictions MAY have specific masking requirements
- Cross-border data transfers MAY require masking to comply with regulations
- Cloud data storage SHALL consider data residency requirements

### 6.2 Regulatory Alignment

| Regulation | Environment Impact |
|------------|-------------------|
| **GDPR (EU)** | Pseudonymization required for processing, anonymization for transfers |
| **HIPAA (US)** | De-identification required for non-production use of PHI |
| **PCI-DSS** | Cardholder data masking required in non-production |
| **CCPA/CPRA (California)** | Consumer data masking for analytics and third-party sharing |

---

## 7. Prohibited Practices

The organization SHALL NOT:

❌ **Clone production to non-production without masking**
- Even with access controls, this is insufficient

❌ **Rely solely on NDAs for non-production data protection**
- NDAs are legal controls, not technical controls

❌ **Use "obfuscation by complexity"**
- Complexity is not security (e.g., "the data is encrypted in transit")

❌ **Allow unmasked production data on personal laptops**
- Endpoints are high-risk for data loss

❌ **Share unmasked data externally without contractual necessity**
- Default to masking for all external sharing

---

## 8. Masking Environment Inventory

The organization SHALL maintain an inventory of:

1. **All environments** (production, non-production, cloud, etc.)
2. **Masking requirements** per environment (mandatory, conditional, not required)
3. **Masking techniques** deployed in each environment
4. **Data flow checkpoints** and masking enforcement
5. **Exceptions** and compensating controls

**Inventory maintenance:**
- Reviewed quarterly
- Updated upon environment changes (new systems, cloud migrations)
- Audited annually for compliance

---

## 9. Exception Management

When masking cannot be applied in a required environment:

### 9.1 Exception Request Process

1. **Requestor** documents business justification
2. **Data Owner** assesses necessity
3. **ISO** conducts risk assessment
4. **Compensating controls** identified (encryption, access logging, monitoring)
5. **CISO** approves exception (or rejects)
6. **Exception documented** in risk register
7. **Exception reviewed** quarterly for continued validity

### 9.2 Compensating Controls

If masking exception approved, compensating controls SHALL include:
- Encryption at rest and in transit
- Strict access controls (MFA, privileged access management)
- Enhanced logging and monitoring
- Data minimization (only necessary fields/records)
- Time-limited access (automatic expiration)
- User training and acknowledgment

---

## 10. Compliance and Audit

### 10.1 Audit Evidence

Auditors SHALL be provided with:
- Environment classification documentation
- Data flow diagrams with masking checkpoints
- Masking technique mapping to environments
- Exception register with compensating controls
- Validation results (masking effectiveness per environment)

### 10.2 Audit Checklist (Sample)

- [ ] All non-production environments documented and classified?
- [ ] Masking requirements defined per environment?
- [ ] Data flow checkpoints identified and enforced?
- [ ] Masking techniques appropriate for each environment?
- [ ] Production-to-non-production data refresh process includes masking?
- [ ] External data sharing includes masking?
- [ ] Cloud environments follow masking requirements?
- [ ] Endpoint data downloads masked?
- [ ] Exceptions documented and approved?
- [ ] Inventory maintained and current?

---

## 11. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **ISO** | Define environment masking requirements, approve exceptions |
| **Data Owner** | Classify data and approve masking approach per environment |
| **System Owner** | Implement masking in their environments |
| **Database Administrator** | Execute data refresh masking processes |
| **Cloud Architect** | Ensure cloud environments meet masking requirements |
| **Security Architect** | Design data flow checkpoints and masking enforcement |

---

## 12. Review and Updates

This section SHALL be reviewed:
- **Annually** as part of policy review cycle
- Upon **new environment deployment** (new cloud, new system)
- Upon **data flow changes** (new integrations, new data sharing agreements)
- Upon **regulatory changes** affecting environment requirements

---

## 13. References

- **ISMS-POL-A.8.11-S2.1:** Data Identification Requirements
- **ISMS-POL-A.8.11-S2.2:** Masking Techniques (HOW to mask)
- **ISMS-POL-A.8.11-S2.4:** Testing & Validation
- **ISMS-POL-A.8.24:** Use of Cryptography Policy (for encryption)
- **ISO/IEC 27001:2022 Control A.8.11**
- **ISO/IEC 27002:2022 Guidance for A.8.11**

---

**END OF SECTION S2.3**