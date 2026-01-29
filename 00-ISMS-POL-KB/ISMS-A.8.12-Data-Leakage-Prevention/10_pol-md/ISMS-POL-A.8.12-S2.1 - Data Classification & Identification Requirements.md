**Dependency Chain:**
- **S2.1 output** = Classified data inventory
- **S2.2 input** = What data requires channel protection
- **S2.3 input** = What patterns DLP rules should detect
- **S2.4 input** = Incident severity classification

**Without S2.1 implementation, S2.2-S2.4 cannot function effectively.**

---

## 2. Data Classification Schema

### 2.1 Organizational Classification Levels

Organizations SHALL implement a data classification schema aligned with **ISMS-POL-A.5.12 (Classification of Information)**. The standard classification levels are:

| Classification | Definition | DLP Protection | Examples |
|----------------|------------|----------------|----------|
| **Public** | Information intended for public disclosure | ❌ No DLP protection required | Press releases, marketing materials, public website content |
| **Internal** | Information for internal use only | ⚠️ Optional DLP monitoring | Internal memos, org charts, standard operating procedures |
| **Confidential** | Sensitive business information requiring protection | ✅ DLP protection REQUIRED | Customer lists, contracts, financial records, business strategies |
| **Restricted** | Highly sensitive information with regulatory or legal protection requirements | ✅✅ Enhanced DLP protection REQUIRED | PII under FADP/GDPR, payment card data, health records, trade secrets, source code |

**Compliance Note:**  
Per ISO 27002:2022 Control 5.12, the classification schema SHOULD consider:
- Confidentiality requirements
- Integrity requirements  
- Availability requirements
- Legal and regulatory obligations (FADP, GDPR)
- Business value and criticality

Organizations MAY adopt alternative classification schemas (e.g., TLP - Traffic Light Protocol) if aligned with ISMS-POL-A.5.12. **DLP requirements apply to any data classified as requiring protection (equivalent to Confidential or Restricted).**

### 2.2 Data Classification Ownership

**Data Owners SHALL be responsible for:**
- Classifying data within their domain
- Defining protection requirements for classified data
- Reviewing and updating classifications based on business value changes
- Approving exceptions to DLP policies for their data

**Data Custodians (IT Operations) SHALL be responsible for:**
- Implementing technical controls to enforce data classification
- Deploying DLP solutions per data owner requirements
- Reporting classification coverage gaps

**Information Security SHALL be responsible for:**
- Defining classification schema and standards
- Auditing classification compliance
- Enforcing DLP policies across all data classifications

---

## 3. Sensitive Data Categories

### 3.1 Regulatory-Protected Data

Organizations SHALL identify and protect data categories subject to regulatory requirements:

#### 3.1.1 Personally Identifiable Information (PII)

**Definition (Swiss FADP / EU GDPR):**  
Any information relating to an identified or identifiable natural person ("data subject").

**PII Categories Requiring DLP Protection:**

**Direct Identifiers (High Risk):**
- Full name combined with any sensitive attribute
- Government-issued ID numbers (SSN, passport, driver's license)
- Biometric data (fingerprints, facial recognition, iris scans)
- Financial account numbers (bank accounts, credit cards, IBAN)
- Healthcare identifiers (patient ID, insurance numbers)

**Indirect Identifiers (Medium-High Risk when combined):**
- Date of birth + postal code
- Employee ID + salary information
- Email address + geolocation data
- Phone number + employment history

**Special Categories of Personal Data (GDPR Article 9 - Highest Risk):**
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Health data
- Sex life or sexual orientation

**DLP Requirement:** Organizations SHALL configure DLP solutions to detect and prevent unauthorized transfer of PII, with **enhanced protection** (block mode, manager approval) for Special Categories.

#### 3.1.2 Payment Card Data (PCI DSS Scope)

**Definition:** Payment card information subject to PCI DSS requirements.

**PCI Data Requiring DLP Protection:**
- Primary Account Number (PAN) - 13-19 digit credit/debit card number
- Cardholder name + expiration date + CVV/CVC
- Track data (magnetic stripe or chip)
- PIN blocks and encryption keys

**Detection Patterns:**
- Visa: `^4[0-9]{12}(?:[0-9]{3})?$`
- Mastercard: `^5[1-5][0-9]{14}$`
- American Express: `^3[47][0-9]{13}$`
- Luhn algorithm validation (checksum verification)

**DLP Requirement:** Organizations SHALL block unauthorized transmission of payment card data via email, web uploads, and unencrypted channels. Exceptions require PCI DSS compliance verification (encrypted channels, authorized payment processors).

#### 3.1.3 Financial Data

**Definition:** Non-PCI financial information with business confidentiality or regulatory requirements.

**Financial Data Categories:**
- Bank account statements and transaction records
- Investment portfolios and trading records
- Tax records and declarations
- Financial forecasts and budgets
- Merger & acquisition (M&A) documents
- Audit reports and regulatory filings

**DLP Requirement:** Organizations SHOULD protect financial data based on classification level (Confidential or Restricted). Board-level financial data and M&A information require **enhanced protection** equivalent to trade secrets.

#### 3.1.4 Health Data (Swiss FADP / EU GDPR Article 9)

**Definition:** Information concerning the physical or mental health of an individual.

**Health Data Categories:**
- Medical diagnoses and treatment records
- Prescription and medication information
- Lab results and medical imaging
- Health insurance claims
- Employee sick leave records (diagnosis-specific)
- COVID-19 test results or vaccination status

**DLP Requirement:** Organizations processing health data SHALL configure DLP to **block** unauthorized transmission. Legitimate transfers (to healthcare providers, insurers) require encryption and documented legal basis (GDPR Article 6 + Article 9 exception).

### 3.2 Business-Sensitive Data

Organizations SHALL identify and protect business-sensitive data based on impact to competitive advantage, intellectual property, or contractual obligations:

#### 3.2.1 Intellectual Property (IP)

**Definition:** Proprietary information providing competitive advantage.

**IP Categories Requiring DLP Protection:**
- **Source code and software** (proprietary applications, algorithms, libraries)
- **Technical designs** (engineering drawings, CAD files, specifications)
- **Patents and trade secrets** (formulas, processes, inventions)
- **Research and development** (R&D data, experimental results, prototypes)
- **Product roadmaps** (unreleased features, strategic plans)

**Detection Methods:**
- File type detection (`.java`, `.py`, `.cpp`, `.dwg`, `.pdf` from R&D folders)
- Keyword patterns ("Proprietary", "Confidential", "Patent Pending")
- Source code repository markers (GitHub, GitLab, BitBucket URLs in metadata)
- Document fingerprinting (hash-based matching of known IP documents)

**DLP Requirement:** Organizations SHALL prevent unauthorized transfer of IP to external parties, including personal email, cloud storage, and USB devices. Developers exporting code require manager approval and audit logging.

#### 3.2.2 Business Confidential Information

**Definition:** Non-IP business information with confidentiality requirements.

**Categories:**
- **Contracts and agreements** (customer contracts, NDAs, supplier agreements)
- **Customer lists and CRM data** (customer databases, contact lists, sales pipelines)
- **Pricing and proposals** (rate cards, bids, quotes, discount structures)
- **Business strategies** (strategic plans, board presentations, competitive analysis)
- **Employee data** (salaries, performance reviews, disciplinary records)

**Detection Methods:**
- Document classification labels (manual or automated tagging)
- Keyword combinations ("Confidential" + customer name, "Pricing" + date range)
- Structured data patterns (CSV files with >100 customer records)

**DLP Requirement:** Organizations SHOULD protect business confidential information based on data owner risk assessment. High-value contracts and M&A documents require **block mode**; routine internal communications MAY use **alert-only mode**.

#### 3.2.3 Credentials and Secrets

**Definition:** Authentication credentials and cryptographic secrets.

**Categories Requiring DLP Protection:**
- **Passwords and passphrases** (plaintext or weakly hashed)
- **API keys and tokens** (AWS secret keys, OAuth tokens, service account keys)
- **Private keys and certificates** (SSH private keys, TLS/SSL private keys, code signing certificates)
- **Database connection strings** (with embedded credentials)
- **Encryption keys** (symmetric keys, master keys, recovery keys)

**Detection Patterns:**
- Regex patterns for common API key formats:
  - AWS: `AKIA[0-9A-Z]{16}`
  - GitHub: `ghp_[a-zA-Z0-9]{36}`
  - Slack: `xox[baprs]-[0-9]{10,13}-[a-zA-Z0-9]{24,34}`
- Private key headers: `-----BEGIN RSA PRIVATE KEY-----`
- Database strings: `jdbc:mysql://.*password=`

**DLP Requirement:** Organizations SHALL **block** credentials and secrets from email, chat, code repositories (except encrypted vaults), and web uploads. Detection of credential leakage triggers **immediate incident response** (key rotation, access revocation, forensic investigation).

---

## 4. Data Identification Methods

### 4.1 Content Inspection

Organizations SHALL implement content inspection methods to identify sensitive data within files, emails, and network traffic:

#### 4.1.1 Keyword Matching

**Method:** Search for specific words or phrases indicating sensitive content.

**Use Cases:**
- Document classification markers ("Confidential", "Restricted", "Internal Use Only")
- Project code names ("Project Apollo", "Merger-Acme Corp")
- Organizational terminology ("Board Confidential", "Executive Summary")

**Limitations:**
- High false positive rate (generic words like "confidential" in signatures)
- Language-dependent (English keywords don't detect German/French documents)
- Easy to bypass (synonyms, obfuscation)

**DLP Requirement:** Organizations SHOULD use keyword matching as **secondary detection** method, combined with contextual analysis or fingerprinting.

#### 4.1.2 Pattern Matching (Regular Expressions)

**Method:** Search for structured data patterns using regex.

**Use Cases:**
- **SSN (US):** `\b\d{3}-\d{2}-\d{4}\b` or `\b\d{9}\b`
- **Credit Card:** Luhn-validated 13-19 digit sequences
- **IBAN:** `[A-Z]{2}\d{2}[A-Z0-9]{1,30}`
- **Swiss AHV Number:** `756\.\d{4}\.\d{4}\.\d{2}`
- **Email addresses:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- **IPv4 addresses:** `\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`

**DLP Requirement:** Organizations SHALL use pattern matching for structured data (PII, financial data, credentials). Regex patterns MUST include validation (e.g., Luhn algorithm for credit cards) to reduce false positives.

#### 4.1.3 Data Fingerprinting

**Method:** Create unique signatures (hashes or partial hashes) for sensitive documents or databases, then detect unauthorized copies.

**Fingerprinting Types:**

**Exact Match Fingerprinting:**
- Hash entire document (SHA-256 or MD5)
- Detect exact copies or renames
- **Use Case:** Protect specific high-value documents (M&A agreements, board presentations, customer databases)

**Partial Match Fingerprinting (Fuzzy Matching):**
- Hash document sections or paragraphs
- Detect partial copies, excerpts, or modified versions
- **Use Case:** Detect when employees extract portions of source code, financial models, or customer lists

**Structured Data Fingerprinting:**
- Hash database columns (e.g., customer ID + name + email)
- Detect database exports or CRM data extracts
- **Use Case:** Prevent CRM data exfiltration (Salesforce exports, database dumps)

**DLP Requirement:** Organizations SHOULD use fingerprinting for high-value documents and structured databases. Fingerprinting requires initial indexing/crawl of sensitive data repositories (file servers, SharePoint, databases).

#### 4.1.4 Machine Learning / AI Classification

**Method:** Train models to identify sensitive content based on statistical patterns, context, and semantic analysis.

**ML/AI Capabilities:**
- **Document classification:** Identify contracts, financial reports, or HR documents without keyword reliance
- **Anomaly detection:** Detect unusual data access or transfer patterns
- **Context-aware classification:** Distinguish "password" in security documentation vs. actual password
- **Natural language processing (NLP):** Understand intent and context in unstructured text

**Limitations:**
- Requires training data (labeled examples of sensitive documents)
- False positives during training phase (model tuning required)
- Explainability challenges (why did the model flag this document?)

**DLP Requirement:** Organizations MAY implement ML/AI classification for **complex document types** (legal contracts, medical records, research papers) where keyword/pattern matching is insufficient. ML models require continuous training and validation.

### 4.2 Contextual Analysis

Organizations SHALL use contextual information to reduce false positives and improve detection accuracy:

**Context Factors:**

**Sender / Recipient Context:**
- Internal-to-internal transfer = Lower risk
- Internal-to-external transfer = Higher risk
- Authorized business partner recipient = Medium risk (requires validation)

**Data Location Context:**
- File from designated secure repository (e.g., `/secure/board-docs/`) = High sensitivity assumed
- File from public folder (e.g., `/public/marketing/`) = Low sensitivity assumed

**User Role Context:**
- Finance team emailing financial data to bank = Legitimate business process
- Developer emailing source code to personal Gmail = Policy violation

**Time / Frequency Context:**
- Occasional large file transfer = Normal backup or collaboration
- 100+ files transferred in 5 minutes = Potential mass exfiltration

**DLP Requirement:** Organizations SHOULD implement contextual rules to whitelist legitimate business workflows (Finance → Bank, HR → Payroll Processor) while flagging anomalies.

### 4.3 Data Discovery and Inventory

Organizations SHALL conduct **periodic data discovery** to identify where sensitive data resides:

#### 4.3.1 Data Discovery Tools

**Discovery Methods:**
- **Agent-based scanning:** Install agents on servers and endpoints to scan file systems, databases
- **Network-based scanning:** Passive monitoring of network traffic to identify data flows
- **Cloud API scanning:** Query cloud provider APIs (AWS S3, Azure Blob, Google Drive) to inventory cloud-stored data

**Discovery Scope:**
- File servers (Windows shares, NAS, NFS)
- Databases (SQL Server, Oracle, PostgreSQL, MySQL)
- Collaboration platforms (SharePoint, Confluence, Google Workspace, Microsoft 365)
- Cloud storage (AWS S3, Azure Blob Storage, Dropbox, Box)
- Endpoints (laptops, desktops, mobile devices)

**DLP Requirement:** Organizations SHALL conduct data discovery **before DLP deployment** (baseline) and **quarterly thereafter** (ongoing validation). Discovery results feed DLP rule tuning and risk assessment.

#### 4.3.2 Data Inventory Maintenance

**Inventory Requirements:**
- **Data category** (PII, financial, IP, credentials)
- **Classification level** (Public, Internal, Confidential, Restricted)
- **Storage location** (file path, database name, cloud bucket)
- **Data owner** (responsible business unit or individual)
- **Volume** (number of records, file count, data size)
- **Last access date** (identify stale data for deletion per ISMS-POL-A.8.10)

**DLP Requirement:** Organizations SHALL maintain data inventory in **ISMS-IMP-A.8.12.2 (Data Classification Assessment)** workbook. Inventory SHALL be updated quarterly and validated by data owners.

---

## 5. Data Labeling Requirements

### 5.1 Manual Labeling

**Method:** Users manually classify and label documents during creation or saving.

**Labeling Mechanisms:**
- **Document properties/metadata:** Set classification in file properties (Microsoft Office, Adobe PDF)
- **Email subject tags:** `[CONFIDENTIAL]` or `[RESTRICTED]` in subject line
- **Document headers/footers:** "CONFIDENTIAL - Internal Use Only" watermark

**Advantages:**
- User awareness of data sensitivity (teachable moment during creation)
- Immediate classification without scanning delay

**Disadvantages:**
- User error or neglect (forgetting to label)
- Inconsistent labeling across users
- Requires user training and enforcement

**DLP Requirement:** Organizations SHOULD implement manual labeling for user-created documents (Office files, emails) combined with automated validation (DLP scans for mislabeled sensitive content).

### 5.2 Automated Labeling

**Method:** DLP or data classification tools automatically label content based on detection rules.

**Automated Labeling Triggers:**
- **Pattern detection:** File contains 10+ credit card numbers → auto-label "Restricted"
- **Location-based:** Files in `/secure/hr/` → auto-label "Confidential"
- **Fingerprint match:** Document matches board presentation hash → auto-label "Restricted"

**Labeling Actions:**
- **Add metadata:** Set file property or extended attribute
- **Rename file:** Append `[CONFIDENTIAL]` to filename
- **Apply visual markers:** Inject header/footer watermark

**DLP Requirement:** Organizations SHALL implement automated labeling for **high-risk data** (PII, credentials, IP) discovered without existing labels. Automated labels SHOULD be validated by data owners to prevent over-classification.

### 5.3 Cloud Data Labeling

For cloud services and SaaS platforms, organizations SHALL leverage **cloud-native data classification** where available:

**Microsoft 365:**
- **Microsoft Purview Information Protection** (formerly Azure Information Protection)
- Labels: Public, General, Confidential, Highly Confidential
- DLP policies enforce label-based protection

**Google Workspace:**
- **Google Cloud DLP** labels and classification
- Data classification rules for Drive, Gmail, Calendar

**AWS:**
- **Amazon Macie** for S3 bucket data discovery and classification
- Tags and object metadata for classification

**Cloud Provider Integration:**  
Organizations MAY reference **ISMS-REF-A.5.23 (Cloud Service Provider Registry)** to identify which cloud providers support native data classification and integrate with organizational DLP solutions.

**DLP Requirement:** Organizations SHALL configure cloud-native DLP where available (Microsoft 365 DLP, Google Workspace DLP) to enforce classification-based policies. For cloud providers without native DLP, organizations SHALL deploy **Cloud Access Security Broker (CASB)** solutions.

---

## 6. Classification Review and Updates

### 6.1 Review Triggers

Data classifications SHALL be reviewed and updated when:

**Regulatory Changes:**
- New data protection law enacted (e.g., Swiss FADP revision)
- Regulatory guidance updated (e.g., GDPR adequacy decisions)

**Business Changes:**
- Merger or acquisition (new data categories, systems)
- New products or services (new data collection practices)
- Market entry/exit (jurisdictional compliance changes)

**Incident-Driven:**
- Data breach or leakage incident reveals classification gaps
- Audit findings identify over-classification or under-classification

**Periodic:**
- Annual classification review (minimum)
- Quarterly for high-risk data (PII, financial, IP)

### 6.2 Declassification

Data MAY be declassified (downgraded from Confidential/Restricted to Internal/Public) when:

**Business Value Declines:**
- Contract expires and is publicly filed
- Product launched and formerly secret features are now public
- Financial results published in annual report

**Retention Expiry:**
- Data retention period expires per ISMS-POL-A.8.10
- Legal hold lifted after litigation concludes

**DLP Impact:** Declassified data SHALL be removed from DLP fingerprinting databases and monitoring rules to reduce false positive rates.

---

## 7. Integration with DLP Framework

### 7.1 Data Classification → DLP Rules Mapping

| Data Category | Classification | DLP Action | Channel Restrictions |
|---------------|----------------|------------|---------------------|
| **PII (General)** | Confidential | Alert + Block (external) | Email (encrypt), Web (block), USB (block) |
| **PII (Special Categories)** | Restricted | Block + Incident | All external channels blocked |
| **Payment Card Data** | Restricted | Block + Incident | All channels except PCI-compliant processors |
| **Financial Data** | Confidential | Alert + Review | Email (encrypt), Web (whitelist partners) |
| **Intellectual Property** | Restricted | Block + Approval | Repositories (audit), Email (encrypt), USB (block) |
| **Credentials/Secrets** | Restricted | Block + Immediate Incident | All channels blocked, key rotation triggered |
| **Business Confidential** | Confidential | Alert | Email (monitor), Web (whitelist), USB (alert) |

### 7.2 Assessment Integration

Data classification requirements SHALL be assessed using **ISMS-IMP-A.8.12.2 (Data Classification Assessment)** workbook, which evaluates:

- Existence of organizational data classification schema
- Classification coverage (% of sensitive data classified)
- Labeling compliance (% of files with classification labels)
- Data inventory completeness (all repositories cataloged)
- Data owner accountability (ownership assigned)
- Discovery tool deployment (automated scanning enabled)

**Compliance Target:** >95% of sensitive data classified and inventoried within 12 months of DLP deployment.

---

## 8. Legal and Privacy Considerations

### 8.1 Employee Data Classification

Employee personal data (HR records, payroll, performance reviews) is subject to **Swiss FADP Article 26 and GDPR Article 5 (purpose limitation)**.

**Requirements:**
- Employee data SHALL be classified as **Confidential** minimum
- Sensitive employee data (health, union membership, disciplinary records) SHALL be classified as **Restricted**
- Data classification enables appropriate DLP protection and access control

### 8.2 Proportionality in Data Discovery

Automated data discovery tools scan file systems, databases, and cloud storage to identify sensitive data. Organizations MUST ensure discovery is **proportionate** and **privacy-respecting**:

**Proportionate Discovery:**
- Scan only business data repositories (exclude personal folders unless justified)
- Use hash-based fingerprinting (do not retain full document content)
- Limit access to discovery results (security team, data owners only)
- Document legal basis for discovery (legitimate interest, security necessity)

**DPO Consultation:** Organizations SHALL consult the Data Protection Officer (DPO) before deploying data discovery tools that scan employee data or communications.

---

## 9. References

### 9.1 Internal Policy Documents

- **ISMS-POL-A.8.12** - Master DLP Policy Framework
- **ISMS-POL-A.8.12-S1** - Purpose, Scope & Definitions
- **ISMS-POL-A.8.12-S2** - DLP Requirements Overview
- **ISMS-POL-A.5.12** - Classification of Information (organizational classification schema)
- **ISMS-POL-A.8.10** - Information Deletion (data retention and deletion)
- **ISMS-REF-A.5.23** - Cloud Service Provider Registry (cloud data classification)

### 9.2 Implementation Documents

- **ISMS-IMP-A.8.12.2** - Data Classification Assessment (Excel workbook)

### 9.3 Regulatory References

- **ISO/IEC 27002:2022** - Control 5.12 (Classification of Information)
- **Swiss FADP** - Article 4 (Definition of personal data), Article 5 (Special categories)
- **EU GDPR** - Article 4(1) (Definition of personal data), Article 9 (Special categories), Article 5 (Lawfulness, fairness, transparency)
- **PCI DSS v4.0** - Requirement 3 (Protect stored cardholder data)

---

**END OF DOCUMENT**

*"The tragedy of DLP is not the data you protect. It's the data you didn't know existed until it leaked."*  
*— The Second Law of Data Protection*