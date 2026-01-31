# ISMS-IMP-A.8.25-26-29-S1
## Security Requirements Process - Implementation Guide
### ISO/IEC 27001:2022 Controls A.8.26 (Application Security Requirements)

---

## Document Control

**Document ID:** ISMS-IMP-A.8.25-26-29-S1  
**Implementation Area:** Security Requirements Specification Process  
**Related Policy:** ISMS-POL-A.8.25-26-29-S2 (Security Requirements - A.8.26)  
**Purpose:** Step-by-step implementation guidance for establishing and executing security requirements processes

**Regulatory Context:**
- ISO/IEC 27001:2022 Control A.8.26 (Application Security Requirements)
- OWASP SAMM - Security Requirements domain
- NIST SP 800-218 - Secure Software Development Framework
- See ISMS-POL-00 for complete regulatory applicability framework

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides practical, step-by-step procedures for implementing the security requirements specification process defined in POL-S2. It covers:

- Security requirements elicitation and documentation
- Threat modeling execution and workshop facilitation
- Security architecture review processes
- Requirements traceability management
- Assessment workbook usage and evidence collection

### 1.2 Target Audience

- **Primary:** Product Managers, Application Owners, Security Architects
- **Supporting:** Development Leads, Business Analysts, Compliance Officers
- **Oversight:** CISO, Security Leadership, Audit Teams

### 1.3 Prerequisites

**Before implementing this process:**
- [ ] Read ISMS-POL-A.8.25-26-29-S2 (Security Requirements Policy)
- [ ] Application inventory available (current applications and new projects)
- [ ] Application risk classification criteria defined
- [ ] Security requirements approval workflow established
- [ ] Document repository configured (SharePoint, Confluence, etc.)

### 1.4 Process Dependencies

**Integrates with:**
- Application lifecycle management processes
- Change management and release processes
- Risk assessment processes (ISMS-POL-A.5.7 - Threat Intelligence)
- Secure development lifecycle (POL-S3, IMP-S2)
- Security testing processes (POL-S4, IMP-S4)

---

## 2. Application Risk Classification

### 2.1 Risk Classification Process

**Purpose:** Determine security requirements rigor based on application risk level.

**Step-by-Step Process:**

**Step 1: Gather Application Information**
- Application name and description
- Business function/purpose
- User base (internal, external, both)
- Data handled (types and classifications)
- Deployment model (on-premises, cloud, hybrid)
- Internet accessibility

**Step 2: Apply Risk Criteria**

Use the risk scoring matrix from POL-S2 Section 3. Score each criterion:

| Criterion | Weight | Score (0-5) | Weighted Score |
|-----------|--------|-------------|----------------|
| Data Sensitivity | 30% | [0-5] | [Weight × Score] |
| User Base | 20% | [0-5] | [Weight × Score] |
| Internet Exposure | 25% | [0-5] | [Weight × Score] |
| Business Criticality | 15% | [0-5] | [Weight × Score] |
| Regulatory Scope | 10% | [0-5] | [Weight × Score] |
| **Total** | **100%** | | **[Sum]** |

**Scoring Guidelines:**

**Data Sensitivity (0-5):**
- 5: Handles PII, financial data, healthcare data (PHI), payment card data (PCI)
- 4: Handles confidential business data, intellectual property
- 3: Handles internal-use data with moderate sensitivity
- 2: Handles low-sensitivity internal data
- 1: Handles public information only
- 0: No data storage/processing

**User Base (0-5):**
- 5: Public/anonymous users, customers
- 4: Business partners, contractors
- 3: Mixed internal/external users
- 2: Authenticated employees only
- 1: Restricted user group (<20 users)

**Internet Exposure (0-5):**
- 5: Publicly accessible via internet
- 4: Internet-accessible with VPN/authentication
- 3: Hybrid (some components internet-facing)
- 2: Internal network only with remote access
- 1: Isolated internal network
- 0: Air-gapped/standalone

**Business Criticality (0-5):**
- 5: Critical to business operations (outage = business stoppage)
- 4: High impact (significant revenue/operational impact)
- 3: Moderate impact (workarounds available)
- 2: Low impact (convenience/efficiency only)
- 1: Minimal impact

**Regulatory Scope (0-5):**
- 5: Subject to multiple regulations (GDPR + PCI DSS + HIPAA, etc.)
- 4: Subject to one major regulation (GDPR, PCI DSS, HIPAA)
- 3: Subject to industry standards (ISO 27001, SOC 2)
- 2: Subject to internal policies only
- 1: Minimal regulatory requirements

**Step 3: Determine Risk Classification**

Based on total weighted score:
- **High Risk:** Score ≥ 3.5 (requires comprehensive security requirements)
- **Medium Risk:** Score 2.0 - 3.4 (requires standard security requirements)
- **Low Risk:** Score < 2.0 (requires baseline security requirements)

**Step 4: Document Classification**
- Record classification in application inventory
- Assign Application ID (format: APP-[XXX])
- Document scoring rationale
- Obtain stakeholder agreement on classification

### 2.2 Classification Examples

**Example 1: Customer-Facing E-Commerce Portal**
- Data Sensitivity: 5 (PCI DSS payment data, customer PII)
- User Base: 5 (Public customers)
- Internet Exposure: 5 (Public internet)
- Business Criticality: 5 (Revenue generation)
- Regulatory Scope: 5 (GDPR + PCI DSS)
- **Total:** 5.0 → **High Risk**

**Example 2: Internal HR System**
- Data Sensitivity: 4 (Employee PII, payroll)
- User Base: 2 (HR staff only)
- Internet Exposure: 2 (Internal with remote access)
- Business Criticality: 3 (Important but not critical)
- Regulatory Scope: 4 (GDPR)
- **Total:** 3.15 → **Medium Risk**

**Example 3: Internal Knowledge Base**
- Data Sensitivity: 2 (Internal documentation)
- User Base: 2 (All employees)
- Internet Exposure: 2 (Internal with remote access)
- Business Criticality: 2 (Convenience)
- Regulatory Scope: 2 (Internal policies)
- **Total:** 2.0 → **Medium Risk** (borderline)

**Example 4: Marketing Website (Static Content)**
- Data Sensitivity: 1 (Public information only)
- User Base: 5 (Public visitors)
- Internet Exposure: 5 (Public internet)
- Business Criticality: 3 (Brand presence)
- Regulatory Scope: 2 (Cookie compliance)
- **Total:** 3.25 → **Medium Risk** (due to internet exposure)

---

## 3. Security Requirements Elicitation

### 3.1 Requirements Elicitation Process

**Purpose:** Systematically identify and document security requirements for an application.

**Timeline:** 2-4 weeks depending on application complexity

**Step 1: Assemble Requirements Team**

**Required Participants:**
- Product Owner/Manager (requirements owner)
- Security Architect (security expertise)
- Application Architect (technical feasibility)
- Compliance Officer (regulatory requirements) [if applicable]
- Key Developers (implementation perspective)

**Optional Participants:**
- Legal/Privacy Officer (for high-sensitivity data)
- Business Analysts (business process understanding)
- Infrastructure/Operations (deployment constraints)

**Step 2: Conduct Kick-Off Workshop**

**Workshop Agenda (2 hours):**

*Hour 1: Context Setting*
1. Application overview (15 min)
   - Business purpose and value proposition
   - User workflows and use cases
   - High-level architecture
2. Risk classification review (10 min)
   - Present risk scoring
   - Confirm classification agreement
3. Regulatory requirements overview (20 min)
   - Identify applicable regulations (GDPR, PCI DSS, HIPAA, etc.)
   - Review compliance obligations
4. Data flow mapping (15 min)
   - Identify data sources and sinks
   - Map data flows through application
   - Identify trust boundaries

*Hour 2: Requirements Identification*
5. Security requirements brainstorming (30 min)
   - Use security requirements template (see Section 3.2)
   - Walk through each category
   - Capture requirements
6. Prioritization (20 min)
   - Mark mandatory vs. optional requirements
   - Identify dependencies
7. Next steps and assignments (10 min)

**Step 3: Document Requirements Using Template**

See Section 3.2 for detailed template structure.

**Step 4: Requirements Review and Refinement**

*Review Cycle (1 week):*
- Security Architect reviews for completeness and technical accuracy
- Product Owner reviews for business alignment
- Compliance Officer reviews for regulatory compliance
- Development Lead reviews for feasibility

*Common Issues to Address:*
- Vague requirements (make specific and testable)
- Technology-specific requirements (make technology-agnostic)
- Missing acceptance criteria (define how to verify)
- Conflicting requirements (resolve conflicts)

**Step 5: Requirements Approval**

*Approval Workflow:*
1. Security Architect approves technical adequacy
2. Compliance Officer approves regulatory compliance (if applicable)
3. Product Owner approves business alignment
4. CISO or delegate approves for high-risk applications

*Approval Documentation:*
- Record approver names and dates
- Document approval sign-off
- Store in document repository
- Link to application record

### 3.2 Security Requirements Template

**Template Structure:**

Use the following template structure to document security requirements. Requirements should be numbered sequentially: SEC-REQ-[APP-ID]-[NUMBER]

#### Template Header

```
Application Name:          [Application Name]
Application ID:            APP-[XXX]
Risk Classification:       [High/Medium/Low Risk]
Document Version:          1.0
Last Updated:              [Date]
Owner:                     [Product Owner Name]
Security Architect:        [Security Architect Name]
```

#### Requirement Categories

**Category 1: Authentication Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-001 | Application MUST support multi-factor authentication (MFA) for all users | Protect against credential theft per NIST 800-63B | MFA enrollment required for all users; supports TOTP, push notifications, or hardware tokens | Functional test: Verify MFA enrollment flow, verify login requires MFA | Mandatory |
| SEC-REQ-[APP]-002 | Application MUST enforce password complexity: min 12 characters, mixture of character types | Prevent weak passwords per organizational policy | Password creation validates complexity rules; existing passwords grandfathered until next change | Functional test: Attempt to set weak password (must fail) | Mandatory |
| SEC-REQ-[APP]-003 | Application MUST implement account lockout after 5 failed login attempts | Prevent brute force attacks | Account locked for 15 minutes after 5 consecutive failures; user notification sent | Functional test: Simulate failed logins | Mandatory |

**Category 2: Authorization Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-010 | Application MUST implement role-based access control (RBAC) | Enforce least privilege principle | All functions assigned to roles; users assigned to roles; no direct user-to-permission mapping | Code review: Verify RBAC implementation; Functional test: Verify role enforcement | Mandatory |
| SEC-REQ-[APP]-011 | Application MUST verify authorization on every request (server-side) | Prevent privilege escalation and IDOR vulnerabilities | Authorization check executed server-side for every resource access; cannot bypass via client manipulation | Penetration test: Attempt to access unauthorized resources via direct requests | Mandatory |
| SEC-REQ-[APP]-012 | Application MUST support principle of least privilege | Minimize blast radius of compromised accounts | Default role has minimal permissions; users receive only permissions necessary for their job function | Configuration review: Verify default permissions; User access review | Mandatory |

**Category 3: Input Validation Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-020 | Application MUST validate all user inputs against allowlists | Prevent injection attacks (SQL, XSS, command injection) | Input validation applied to all user-controllable data; validation uses allowlists (positive validation) where possible; server-side validation required | SAST scan: Check for input validation; DAST scan: Injection testing | Mandatory |
| SEC-REQ-[APP]-021 | Application MUST encode output to prevent XSS | Prevent cross-site scripting attacks | Output encoding applied based on context (HTML, JavaScript, URL, CSS); content security policy (CSP) implemented | DAST scan: XSS testing; Code review: Verify output encoding | Mandatory |
| SEC-REQ-[APP]-022 | Application MUST validate file uploads (type, size, content) | Prevent malicious file upload attacks | File type validated via magic bytes (not extension); size limits enforced; content scanned for malware | Functional test: Upload malicious files; Penetration test: Bypass attempts | Mandatory |

**Category 4: Cryptography Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-030 | Application MUST use TLS 1.2 or higher for all network communications | Protect data in transit per PCI DSS/regulatory requirements | TLS 1.2+ configured; older protocols disabled; strong cipher suites only | Configuration scan: Verify TLS settings; SSLLabs test | Mandatory |
| SEC-REQ-[APP]-031 | Application MUST encrypt sensitive data at rest using AES-256 or equivalent | Protect data at rest per regulatory requirements | Sensitive data encrypted in database; encryption keys managed separately (key management system) | Configuration review: Verify encryption settings; Database inspection | Mandatory |
| SEC-REQ-[APP]-032 | Application MUST NOT store sensitive data in logs or cache | Prevent data exposure via logs/cache | Sensitive data (passwords, tokens, PII, payment data) masked or excluded from logs and cache | Log review: Verify no sensitive data; Code review: Check logging statements | Mandatory |

**Category 5: Session Management Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-040 | Application MUST use secure session tokens | Prevent session hijacking | Session tokens cryptographically random (min 128-bit entropy); HttpOnly and Secure flags set; SameSite attribute configured | Code review: Verify session implementation; DAST scan: Session testing | Mandatory |
| SEC-REQ-[APP]-041 | Application MUST implement session timeout (15 min idle, 8 hr absolute) | Reduce window for session hijacking | Session expires after 15 minutes of inactivity; absolute timeout of 8 hours; user notified before timeout | Functional test: Verify timeout behavior | Mandatory |
| SEC-REQ-[APP]-042 | Application MUST invalidate session on logout | Prevent session reuse after logout | Session invalidated server-side on logout; session token cannot be reused | Functional test: Logout then attempt to reuse token | Mandatory |

**Category 6: Logging and Monitoring Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-050 | Application MUST log security-relevant events | Enable security monitoring and incident investigation | Logs include: authentication (success/failure), authorization failures, input validation failures, access to sensitive data, configuration changes | Log review: Verify event coverage; SIEM integration test | Mandatory |
| SEC-REQ-[APP]-051 | Application MUST include sufficient context in logs | Enable effective investigation and forensics | Logs include: timestamp, user ID, IP address, action, resource, result | Log review: Verify log format and content | Mandatory |
| SEC-REQ-[APP]-052 | Application MUST protect log integrity | Prevent log tampering | Logs written to centralized log system; log files protected from modification; log forwarding uses secure protocol | Configuration review: Verify log protection | Mandatory |

**Category 7: Error Handling Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-060 | Application MUST use generic error messages | Prevent information disclosure | Error messages to users do not reveal technical details, stack traces, database errors, or system paths | Functional test: Trigger errors, verify messages generic; Code review | Mandatory |
| SEC-REQ-[APP]-061 | Application MUST log detailed errors securely | Enable debugging without information disclosure | Detailed errors logged server-side (not sent to client); logs protected and only accessible to authorized personnel | Error testing: Verify detailed logs captured server-side | Mandatory |

**Category 8: API Security Requirements** (if applicable)

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-070 | API MUST use OAuth 2.0 or equivalent for authorization | Industry standard API authorization | API implements OAuth 2.0 with appropriate grant types; API keys not used for user authorization | API testing: Verify OAuth implementation | Mandatory |
| SEC-REQ-[APP]-071 | API MUST implement rate limiting | Prevent DoS attacks and abuse | Rate limits configured per API endpoint; limits enforced per user/API key; 429 status returned when exceeded | API testing: Exceed rate limits, verify enforcement | Mandatory |
| SEC-REQ-[APP]-072 | API MUST validate content-type headers | Prevent content-type attacks | Content-Type header validated; requests rejected if Content-Type mismatches body | API testing: Send mismatched content-type | Mandatory |

**Category 9: Data Protection Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-080 | Application MUST implement data retention policies | Comply with GDPR/regulatory requirements | Data retention periods defined per data type; automated deletion implemented; deletion verified | Configuration review: Verify retention policies; Test: Verify deletion | Mandatory (if GDPR) |
| SEC-REQ-[APP]-081 | Application MUST support data subject access requests (DSAR) | Comply with GDPR Article 15 | Mechanism to export all user data in machine-readable format; response within 30 days | Functional test: Request data export, verify completeness | Mandatory (if GDPR) |
| SEC-REQ-[APP]-082 | Application MUST support right to erasure ("right to be forgotten") | Comply with GDPR Article 17 | Mechanism to delete all user data; deletion cascades to backups and logs (where feasible) | Functional test: Request deletion, verify removal | Mandatory (if GDPR) |

**Category 10: Third-Party Component Security Requirements**

| Req ID | Requirement | Rationale | Acceptance Criteria | Test Method | Priority |
|--------|-------------|-----------|---------------------|-------------|----------|
| SEC-REQ-[APP]-090 | Application MUST maintain inventory of third-party components | Enable vulnerability management | All third-party libraries/components documented (name, version, purpose); inventory updated with each release | SCA scan: Generate component inventory, verify accuracy | Mandatory |
| SEC-REQ-[APP]-091 | Application MUST NOT use components with known high/critical vulnerabilities | Prevent exploitation of known vulnerabilities | SCA scanning in CI/CD pipeline; builds fail on high/critical vulnerabilities; documented exceptions only | SCA scan: Verify no high/critical vulns unaddressed | Mandatory |
| SEC-REQ-[APP]-092 | Application MUST validate third-party component licenses | Ensure license compliance | All component licenses reviewed; incompatible licenses flagged; legal approval obtained | License scanning: Verify no prohibited licenses | Mandatory |

### 3.3 Requirements Documentation Best Practices

**Writing Effective Requirements:**

✅ **DO:**
- Use "MUST", "SHOULD", "MAY" keywords per RFC 2119
- Write testable requirements (clear acceptance criteria)
- Include security rationale (why is this needed?)
- Define clear test methods
- Prioritize requirements (Mandatory, Recommended, Optional)
- Make requirements technology-agnostic (unless technology-specific is necessary)

❌ **DON'T:**
- Write vague requirements ("Application must be secure")
- Conflate multiple requirements in one (split them)
- Specify implementation details in requirements (describe what, not how)
- Forget acceptance criteria (how do we verify this?)
- Create untestable requirements

**Example Transformation:**

❌ **Bad Requirement:**
"Application must be secure against attacks"
- Problem: Too vague, not testable, no acceptance criteria

✅ **Good Requirement:**
"Application MUST validate all user inputs using allowlist validation to prevent injection attacks. Acceptance Criteria: Input validation implemented server-side for all user-controllable parameters; validation uses allowlists where possible; SAST scan shows no injection vulnerabilities. Test Method: SAST scan + DAST injection testing + code review."

### 3.4 Requirements Traceability

**Purpose:** Link requirements through design, code, and testing for audit traceability.

**Traceability Matrix Structure:**

| Req ID | Requirement | Design Reference | Code Reference | Test Case ID | Test Result | Status |
|--------|-------------|------------------|----------------|--------------|-------------|--------|
| SEC-REQ-APP-001 | MFA support | Architecture Doc §3.2 | auth/mfa.py:50-120 | TC-001, TC-002 | Pass | ✅ |
| SEC-REQ-APP-002 | Password complexity | Architecture Doc §3.1 | auth/password.py:30-45 | TC-003 | Pass | ✅ |

**Implementation Steps:**

**Step 1: Create Traceability Matrix**
- Use Excel template or requirements management tool (Jira, Azure DevOps)
- Create one row per security requirement
- Link to application's master requirements

**Step 2: Update During Development**
- Developer responsibility: Update design/code references during implementation
- Code reviews verify traceability updates
- References should be specific (file:line or section numbers)

**Step 3: Update During Testing**
- QA/Security tester responsibility: Link test cases to requirements
- Record test results (pass/fail)
- Document any requirement modifications (with approval)

**Step 4: Periodic Audits**
- Quarterly review of traceability matrix
- Verify all mandatory requirements traced
- Identify orphaned requirements (not implemented)
- Identify orphaned code (not traced to requirement)

**Tool Options:**
- **Excel/Spreadsheet:** Simple, works for small applications
- **Jira/Azure DevOps:** Built-in traceability links
- **IBM DOORS, Jama Connect:** Enterprise requirements management (for complex/regulated applications)
- **Custom tools:** API-based traceability (code annotations → automated traceability)

---

## 4. Threat Modeling Execution

### 4.1 Threat Modeling Overview

**Purpose:** Systematically identify security threats and define mitigations.

**When to Perform:**
- **Required:** All High Risk applications
- **Recommended:** All Medium Risk applications
- **Optional:** Low Risk applications (lightweight threat analysis acceptable)

**Timing:**
- Design phase (before coding starts)
- Major feature additions or architecture changes
- Annual updates for existing applications

**Methodologies:**
We support three threat modeling methodologies. Choose based on your needs:

| Methodology | Best For | Time Required | Skill Level |
|-------------|----------|---------------|-------------|
| **STRIDE** | General applications, developer-friendly | 2-4 hours | Beginner-friendly |
| **PASTA** | Risk-centric analysis, compliance-focused | 4-8 hours | Intermediate |
| **LINDDUN** | Privacy-focused applications, GDPR compliance | 3-6 hours | Intermediate |

### 4.2 STRIDE Threat Modeling (Recommended)

**STRIDE Acronym:**
- **S** - Spoofing (pretending to be someone else)
- **T** - Tampering (modifying data or code)
- **R** - Repudiation (denying actions)
- **I** - Information Disclosure (exposing information)
- **D** - Denial of Service (disrupting availability)
- **E** - Elevation of Privilege (gaining unauthorized permissions)

**Step-by-Step STRIDE Process:**

**Step 1: Create Data Flow Diagram (DFD)**

**DFD Components:**
- **External Entities** (users, external systems) - rectangles
- **Processes** (application components, services) - circles
- **Data Stores** (databases, file systems, caches) - parallel lines
- **Data Flows** (data movement) - arrows
- **Trust Boundaries** (security boundaries) - dashed lines

**Example DFD:**

```
┌─────────────────────────────────────────────────────┐
│          INTERNET (Untrusted Zone)                  │
│                                                     │
│  ┌────────┐                                        │
│  │  User  │────────────────────┐                   │
│  └────────┘                    │                   │
│                                │                   │
└────────────────────────────────┼───────────────────┘
                                 │ HTTPS
                 TRUST BOUNDARY  ↓
┌─────────────────────────────────────────────────────┐
│          DMZ (Web Tier)                             │
│                                                     │
│          ┌──────────────┐                          │
│          │  Web Server  │                          │
│          │   (Process)  │                          │
│          └──────────────┘                          │
│                 │ HTTP/REST API                    │
└─────────────────┼───────────────────────────────────┘
                  │
  TRUST BOUNDARY  ↓
┌─────────────────────────────────────────────────────┐
│    Internal Network (App Tier)                      │
│                                                     │
│          ┌──────────────┐                          │
│          │ App Server   │                          │
│          │  (Process)   │                          │
│          └──────────────┘                          │
│                 │ SQL                              │
│                 ↓                                  │
│          ┌──────────────┐                          │
│          │  Database    │                          │
│          │ (Data Store) │                          │
│          └──────────────┘                          │
└─────────────────────────────────────────────────────┘
```

**Step 2: Identify Trust Boundaries**

Trust boundaries separate zones with different trust levels:
- Internet ↔ DMZ (external users → web tier)
- DMZ ↔ Internal Network (web tier → app tier)
- Process ↔ Data Store (app → database)
- User ↔ Application (authentication boundary)

**Key Principle:** Data crossing trust boundaries requires security controls.

**Step 3: Apply STRIDE to Each Element**

**For Each Element in DFD:**

**External Entities (Users):**
- Spoofing: Can user pretend to be another user?
- Repudiation: Can user deny actions they performed?

**Processes (Web/App Servers):**
- Spoofing: Can processes be impersonated?
- Tampering: Can process code/config be modified?
- Repudiation: Are process actions logged?
- Information Disclosure: Does process leak sensitive information?
- Denial of Service: Can process be overwhelmed?
- Elevation of Privilege: Can process be exploited for higher privileges?

**Data Stores (Databases):**
- Tampering: Can data be modified by unauthorized parties?
- Repudiation: Are data changes logged?
- Information Disclosure: Can data be accessed by unauthorized parties?
- Denial of Service: Can data store be overwhelmed or corrupted?

**Data Flows (Network Communications):**
- Tampering: Can data be modified in transit?
- Information Disclosure: Can data be intercepted?
- Denial of Service: Can communication be disrupted?

**Step 4: Document Threats**

**Threat Documentation Template:**

| Threat ID | Element | STRIDE Category | Threat Description | Impact | Likelihood | Risk | Mitigation |
|-----------|---------|----------------|-------------------|--------|------------|------|-----------|
| THR-001 | User → Web Server | Spoofing | Attacker obtains user credentials via phishing | High | Medium | High | Implement MFA (SEC-REQ-001) |
| THR-002 | User → Web Server | Tampering | Attacker modifies request parameters to escalate privileges | High | Medium | High | Server-side authorization checks (SEC-REQ-011) |
| THR-003 | Web Server → Database | Information Disclosure | SQL injection exposes database contents | Critical | Medium | Critical | Input validation (SEC-REQ-020), parameterized queries |
| THR-004 | Database | Tampering | Direct database access modifies data | High | Low | Medium | Database access controls, encryption at rest (SEC-REQ-031) |
| THR-005 | Internet → Web Server | Denial of Service | DDoS attack overwhelms web server | Medium | High | High | Rate limiting, CDN/DDoS protection |

**Step 5: Define Mitigations**

**For Each Threat:**
1. Identify existing security controls (if any)
2. Determine if additional controls needed
3. Link to security requirements (SEC-REQ-XXX)
4. Document mitigation in threat model
5. Track mitigation implementation

**Mitigation Strategies by STRIDE Category:**

**Spoofing:**
- Strong authentication (passwords, MFA, certificates)
- Mutual TLS for service-to-service communication
- Digital signatures

**Tampering:**
- Authorization checks
- Integrity checks (hashes, signatures)
- Audit logging
- Input validation
- Secure coding practices

**Repudiation:**
- Audit logging (who, what, when, where)
- Digital signatures for non-repudiation
- Time stamping

**Information Disclosure:**
- Encryption (TLS, AES)
- Access controls
- Data minimization
- Secure error handling (no stack traces)

**Denial of Service:**
- Rate limiting
- Resource quotas
- Input validation (prevent algorithmic complexity attacks)
- DDoS protection (CDN, scrubbing services)

**Elevation of Privilege:**
- Least privilege principle
- Input validation
- Separation of duties
- Privilege separation (run services with minimal privileges)

**Step 6: Review and Approve Threat Model**

**Review Checklist:**
- [ ] All components in DFD analyzed
- [ ] All trust boundaries identified
- [ ] All data flows analyzed
- [ ] Threats documented for each element
- [ ] Mitigations defined for all high/critical risks
- [ ] Mitigations linked to security requirements
- [ ] Assumptions documented
- [ ] Out-of-scope items documented

**Approval:**
- Security Architect approves threat model
- Product Owner acknowledges accepted risks (if any)
- Document approval in threat model document

### 4.3 STRIDE Threat Modeling Workshop Template

**Workshop Preparation (1 week before):**
- [ ] Create initial DFD (architect prepares draft)
- [ ] Gather architecture documentation
- [ ] Schedule 3-hour workshop
- [ ] Invite participants (architect, developers, security, product owner)
- [ ] Send pre-read materials (DFD, architecture docs)

**Workshop Agenda (3 hours):**

**Hour 1: DFD Creation and Validation (60 min)**
- Presentation: Application overview (10 min)
- Activity: DFD review and refinement (30 min)
  - Walk through each component
  - Validate data flows
  - Identify trust boundaries
- Activity: DFD finalization (20 min)

**Hour 2: Threat Identification (60 min)**
- Presentation: STRIDE methodology (15 min)
- Activity: STRIDE analysis (45 min)
  - Divide into groups (if large team)
  - Each group analyzes subset of DFD
  - Document threats using template
  - Focus on high-impact, realistic threats

**Hour 3: Mitigation Definition and Prioritization (60 min)**
- Activity: Mitigation brainstorming (30 min)
  - For each high/critical threat
  - Identify existing controls
  - Propose new controls
  - Link to security requirements
- Activity: Risk prioritization (20 min)
  - Prioritize mitigations
  - Assign owners and timelines
- Wrap-up: Next steps (10 min)

**Post-Workshop (1 week):**
- [ ] Security Architect documents threat model
- [ ] Link threats to security requirements
- [ ] Create Jira/ADO tickets for mitigations
- [ ] Obtain approval
- [ ] Store in document repository

### 4.4 PASTA Threat Modeling (Risk-Centric)

**PASTA (Process for Attack Simulation and Threat Analysis)** - 7-stage process focused on risk and business impact.

**When to Use:** Compliance-heavy applications, risk-based approach needed, business impact analysis required.

**Seven Stages:**

**Stage 1: Define Objectives**
- Business objectives for application
- Security/compliance objectives
- Risk appetite

**Stage 2: Define Technical Scope**
- Application boundaries
- Technologies used
- Dependencies

**Stage 3: Application Decomposition**
- Data flow diagrams
- Trust boundaries
- Entry/exit points

**Stage 4: Threat Analysis**
- Threat intelligence
- Attack vectors
- Threat actors

**Stage 5: Vulnerability & Weakness Analysis**
- Known vulnerabilities
- Design weaknesses
- Configuration issues

**Stage 6: Attack Modeling**
- Attack trees
- Attack scenarios
- Exploitability analysis

**Stage 7: Risk & Impact Analysis**
- Business impact assessment
- Risk scoring
- Mitigation prioritization

**Output:** Risk-scored threat model with business impact analysis.

**Resource:** Process documented at: https://versprite.com/pasta-threat-modeling/

### 4.5 LINDDUN Threat Modeling (Privacy-Focused)

**LINDDUN** - Privacy threat modeling methodology (complement to STRIDE for GDPR compliance).

**LINDDUN Acronym:**
- **L** - Linkability (linking different actions to same user)
- **I** - Identifiability (identifying users from data)
- **N** - Non-repudiation (user cannot deny actions)
- **D** - Detectability (detecting user's data/actions)
- **D** - Disclosure of Information (exposing private information)
- **U** - Unawareness (users unaware of data processing)
- **N** - Non-compliance (violating privacy policies/regulations)

**When to Use:** Applications handling PII, GDPR compliance required, privacy-by-design needed.

**Process:**
1. Create DFD (same as STRIDE)
2. Apply LINDDUN categories to each element
3. Identify privacy threats
4. Define privacy-enhancing mitigations
5. Link to data protection requirements (SEC-REQ-080 series)

**Example LINDDUN Threats:**

| Threat | Privacy Concern | Mitigation |
|--------|----------------|-----------|
| Linkability: User actions across sessions linkable via persistent identifiers | User profiling without consent | Minimize data collection, use pseudonymization |
| Identifiability: IP address + browser fingerprint identifies users | Re-identification risk | Anonymization techniques, data minimization |
| Disclosure: Data breach exposes PII | GDPR breach notification required | Encryption at rest (SEC-REQ-031), access controls |
| Unawareness: Users unaware data shared with third parties | GDPR transparency violation | Privacy policy, consent mechanisms, data flow transparency |

**Resource:** LINDDUN framework at: https://www.linddun.org/

### 4.6 Threat Modeling Tools

**Recommended Tools:**

**Free/Open Source:**
- **Microsoft Threat Modeling Tool** (Windows) - STRIDE-based, generates reports
- **OWASP Threat Dragon** (Cross-platform) - Web-based, STRIDE methodology
- **Threagile** - Risk-based threat modeling, generates reports
- **PyTM** - Python-based, code-as-threat-model approach

**Commercial:**
- **IriusRisk** - Automated threat modeling, integrates with SDLC
- **ThreatModeler** - Visual threat modeling, compliance mapping
- **SD Elements** - Security requirements + threat modeling integrated

**Manual Approach:**
- Whiteboard + sticky notes (workshop)
- Excel/Google Sheets (documentation)
- Visio/Draw.io (DFD creation)

**Tool Selection Criteria:**
- Team size and distribution (collab features needed?)
- Methodology preference (STRIDE, PASTA, LINDDUN)
- Integration needs (Jira, ADO, GitHub)
- Budget constraints

---

## 5. Security Architecture Review

### 5.1 Architecture Review Process

**Purpose:** Validate that application architecture implements security requirements and addresses threats identified in threat model.

**When to Conduct:**
- **Required:** High Risk applications
- **Recommended:** Medium Risk applications
- **Optional:** Low Risk applications (design review with security checklist)

**Timing:**
- Design phase (after requirements, before implementation)
- Major architecture changes
- Pre-production review (final validation)

**Review Timeline:** 1-2 weeks (preparation + review + remediation)

**Step-by-Step Process:**

**Step 1: Schedule Architecture Review**

**Participants:**
- **Required:** Security Architect (lead reviewer), Application Architect, Product Owner
- **Recommended:** Senior Developer, Infrastructure/Cloud Architect, Compliance Officer (if regulated)
- **Optional:** Penetration Tester (if available)

**Logistics:**
- Schedule 2-3 hour review meeting
- Send materials to reviewers 1 week in advance
- Prepare presentation/walkthrough

**Step 2: Prepare Review Materials**

**Required Materials:**
- Architecture diagrams (logical, deployment)
- Security requirements document (from Section 3)
- Threat model (from Section 4)
- Technology stack documentation
- Integration points documentation
- Authentication/authorization design
- Data flow diagrams
- Compliance requirements (if applicable)

**Step 3: Conduct Architecture Review Meeting**

**Meeting Agenda (2-3 hours):**

*Part 1: Architecture Presentation (45-60 min)*
- Application overview and business context (10 min)
- High-level architecture walkthrough (15 min)
- Security controls overview (15 min)
- Integration points and trust boundaries (10 min)
- Q&A (10 min)

*Part 2: Deep-Dive Security Review (60-90 min)*
- Authentication architecture
- Authorization architecture
- Data protection (encryption, data flow)
- Network architecture and segmentation
- API security
- Third-party integrations
- Deployment architecture
- Incident response/logging

*Part 3: Findings Discussion and Next Steps (15-30 min)*
- Document findings
- Prioritize issues
- Assign remediation owners
- Set follow-up timeline

**Step 4: Document Findings**

**Architecture Review Report Structure:**

```markdown
# Security Architecture Review Report

## Application Information
- Application Name: [Name]
- Application ID: APP-[XXX]
- Risk Classification: [High/Medium/Low]
- Review Date: [Date]
- Reviewers: [Names]

## Executive Summary
- Overall Assessment: [Pass / Pass with Findings / Fail]
- Critical Findings: [Number]
- High Findings: [Number]
- Medium Findings: [Number]
- Low Findings: [Number]

## Review Scope
[What was reviewed]

## Methodology
[STRIDE, manual review, automated tools]

## Findings

### Finding 1: [Title]
- **Severity:** Critical / High / Medium / Low
- **Category:** Authentication / Authorization / Cryptography / etc.
- **Description:** [Detailed description]
- **Risk:** [Security risk if not addressed]
- **Recommendation:** [Specific remediation steps]
- **Affected Requirement:** SEC-REQ-[XXX]
- **Owner:** [Name]
- **Due Date:** [Date]
- **Status:** Open / In Progress / Resolved

[Repeat for each finding]

## Positive Observations
[Security controls implemented well]

## Recommendations
[General security recommendations]

## Conclusion
[Overall assessment, approval status]

## Appendices
- Architecture diagrams reviewed
- Checklists used
```

**Step 5: Track Remediation**

- Create tickets for each finding (Jira, ADO, etc.)
- Assign owners and due dates
- Track remediation progress
- Schedule follow-up review (if needed)

**Step 6: Approval and Sign-Off**

**Approval Criteria:**
- All Critical findings resolved
- All High findings resolved or accepted (with risk acceptance)
- Medium/Low findings have remediation plan

**Approval Workflow:**
- Security Architect approves architecture
- Document approval in review report
- Store report in document repository
- Link to application record

### 5.2 Architecture Review Checklist

Use this checklist to ensure comprehensive review coverage:

#### Authentication Architecture

- [ ] **MFA Implemented:** Multi-factor authentication required for all users (or documented exception for low-risk apps)
- [ ] **Password Policy:** Strong password requirements enforced (complexity, length, history)
- [ ] **Account Lockout:** Brute force protection via account lockout
- [ ] **Session Management:** Secure session token generation (cryptographically random, sufficient entropy)
- [ ] **Session Timeout:** Idle timeout and absolute timeout implemented
- [ ] **Logout:** Session invalidated on logout (server-side)
- [ ] **Password Reset:** Secure password reset flow (no password in email, token expiration)
- [ ] **Credential Storage:** Passwords hashed with strong algorithm (bcrypt, Argon2, PBKDF2)
- [ ] **SSO Integration:** If using SSO, secure integration (SAML, OIDC)

#### Authorization Architecture

- [ ] **RBAC Implemented:** Role-based access control implemented
- [ ] **Server-Side Authorization:** Authorization enforced server-side (not client-side only)
- [ ] **Least Privilege:** Default roles have minimal permissions
- [ ] **Authorization on Every Request:** Authorization checked on every resource access
- [ ] **No IDOR Vulnerabilities:** Object-level authorization prevents IDOR
- [ ] **API Authorization:** API endpoints protected with authorization
- [ ] **Admin Functions:** Privileged functions restricted to admin roles

#### Input Validation

- [ ] **Allowlist Validation:** Input validation uses allowlists (positive validation)
- [ ] **Server-Side Validation:** Validation performed server-side (not only client-side)
- [ ] **All Inputs Validated:** All user-controllable inputs validated (forms, APIs, headers, cookies)
- [ ] **File Upload Validation:** File uploads validated (type, size, content)
- [ ] **SQL Injection Prevention:** Parameterized queries or ORM used (no string concatenation)
- [ ] **XSS Prevention:** Output encoding based on context
- [ ] **Command Injection Prevention:** No shell commands with user input (or properly sanitized)

#### Cryptography

- [ ] **TLS 1.2+:** TLS 1.2 or higher for all network communications
- [ ] **Strong Cipher Suites:** Only strong cipher suites enabled
- [ ] **Certificate Validation:** Certificate validation enabled (no self-signed in production)
- [ ] **Encryption at Rest:** Sensitive data encrypted at rest (AES-256 or equivalent)
- [ ] **Key Management:** Encryption keys managed separately (KMS, HSM, secrets manager)
- [ ] **No Hardcoded Secrets:** No hardcoded passwords, API keys, encryption keys in code
- [ ] **Secure Random:** Cryptographically secure random number generator used

#### Data Protection

- [ ] **Data Classification:** Data classified (PII, sensitive, public, etc.)
- [ ] **Data Minimization:** Only necessary data collected and stored
- [ ] **Data Retention:** Retention policies defined and implemented
- [ ] **Data Deletion:** Deletion mechanisms implemented (right to erasure)
- [ ] **No Sensitive Data in Logs:** Sensitive data not logged (passwords, PII, payment data)
- [ ] **No Sensitive Data in URLs:** Sensitive data not passed in URLs/query strings
- [ ] **Backups Encrypted:** Backups encrypted

#### Logging and Monitoring

- [ ] **Security Events Logged:** Authentication, authorization failures, security events logged
- [ ] **Sufficient Log Context:** Logs include timestamp, user, IP, action, resource, result
- [ ] **Centralized Logging:** Logs forwarded to centralized log system (SIEM)
- [ ] **Log Integrity:** Logs protected from tampering
- [ ] **Log Retention:** Logs retained per policy (typically 90 days minimum)
- [ ] **Alerting:** Real-time alerts for security events
- [ ] **No Sensitive Data in Logs:** Passwords, tokens, PII excluded from logs

#### Error Handling

- [ ] **Generic Error Messages:** Error messages to users are generic (no stack traces, SQL errors)
- [ ] **Detailed Errors Logged:** Detailed errors logged server-side for debugging
- [ ] **Error Logging:** Errors logged with context
- [ ] **No Information Disclosure:** Error messages don't reveal system details

#### API Security (if applicable)

- [ ] **API Authentication:** APIs require authentication (OAuth 2.0, API keys)
- [ ] **API Authorization:** APIs enforce authorization
- [ ] **Rate Limiting:** Rate limiting implemented per API endpoint
- [ ] **Input Validation:** API inputs validated
- [ ] **Content-Type Validation:** Content-Type header validated
- [ ] **CORS Policy:** CORS policy restrictive (not allow-all)
- [ ] **API Versioning:** API versioning strategy defined

#### Network Architecture

- [ ] **Network Segmentation:** Application deployed in appropriate network segment (DMZ for internet-facing)
- [ ] **Firewall Rules:** Firewall rules restrictive (least privilege)
- [ ] **No Direct Database Access:** Database not directly accessible from internet
- [ ] **Internal Services Protected:** Internal services not exposed to internet
- [ ] **DDoS Protection:** DDoS protection in place (for internet-facing apps)

#### Third-Party Integrations

- [ ] **Third-Party Authentication:** Third-party integrations use secure authentication
- [ ] **API Key Protection:** Third-party API keys stored securely (secrets manager)
- [ ] **Data Sharing Minimized:** Only necessary data shared with third parties
- [ ] **Third-Party SLA:** Third-party providers have security SLAs
- [ ] **Third-Party Access Reviewed:** Third-party access reviewed periodically

#### Deployment Architecture

- [ ] **Environment Separation:** Dev, test, prod environments separated (see A.8.31)
- [ ] **Prod Data Not in Non-Prod:** Production data not used in dev/test
- [ ] **Deployment Automation:** Deployments automated (CI/CD)
- [ ] **Infrastructure as Code:** Infrastructure defined as code (reviewed, version-controlled)
- [ ] **Secrets Management:** Secrets not hardcoded (use secrets manager)
- [ ] **Container Security:** If using containers, images scanned for vulnerabilities

#### Incident Response

- [ ] **Incident Response Plan:** Incident response plan defined
- [ ] **Security Contacts:** Security contact information documented
- [ ] **Monitoring Coverage:** Application monitored for security incidents
- [ ] **Alerting:** Alerts defined for security events

### 5.3 Architecture Review Report Template

**File:** `Architecture_Review_Report_[APP-ID]_[Date].docx`

```markdown
# Security Architecture Review Report

---

## Document Information

**Application Name:** [Application Name]  
**Application ID:** APP-[XXX]  
**Risk Classification:** [High/Medium/Low Risk]  
**Review Date:** [Date]  
**Report Date:** [Date]  
**Version:** 1.0

**Review Team:**
- Security Architect: [Name]
- Application Architect: [Name]
- Additional Reviewers: [Names]

---

## Executive Summary

**Overall Assessment:** [✅ Pass / ⚠️ Pass with Findings / ❌ Fail]

**Summary:**
[2-3 paragraph summary of review findings and overall security posture]

**Findings Summary:**
- **Critical:** [Number] findings requiring immediate remediation
- **High:** [Number] findings requiring remediation before production
- **Medium:** [Number] findings requiring remediation per timeline
- **Low:** [Number] recommendations for continuous improvement

**Approval Status:**
- [ ] Architecture approved for implementation
- [ ] Architecture conditionally approved (findings must be resolved)
- [ ] Architecture not approved (critical issues identified)

---

## Review Scope

**In Scope:**
- Application architecture and design
- Security controls implementation
- Compliance with security requirements (ISMS-POL-A.8.25-26-29-S2)
- Threat mitigation verification
- Integration security
- Deployment architecture

**Out of Scope:**
- Code-level review (addressed in SAST/code review)
- Penetration testing (separate activity)
- Infrastructure security (covered by infrastructure team)
- [Other exclusions]

---

## Methodology

**Review Approach:**
- Architecture documentation review
- Security requirements verification (SEC-REQ-XXX)
- Threat model validation
- Architecture review checklist (Section 5.2)
- Security best practices assessment

**Materials Reviewed:**
- Architecture diagrams (logical, deployment)
- Security requirements document (v[X.X])
- Threat model (v[X.X])
- Data flow diagrams
- Technology stack documentation
- [Additional materials]

---

## Architecture Overview

[Brief summary of application architecture - reference diagrams]

**Key Components:**
- [Component 1]: [Description]
- [Component 2]: [Description]
- [Component 3]: [Description]

**Trust Boundaries:**
- [Boundary 1]: [Description]
- [Boundary 2]: [Description]

**Technology Stack:**
- Frontend: [Technologies]
- Backend: [Technologies]
- Database: [Technologies]
- Infrastructure: [Cloud/On-Prem, specific platforms]

---

## Findings

### Finding 1: [Title]

**Finding ID:** ARCH-[APP-ID]-001  
**Severity:** ⚠️ Critical / 🔴 High / 🟡 Medium / 🟢 Low  
**Status:** 🔓 Open / 🔄 In Progress / ✅ Resolved

**Category:** Authentication / Authorization / Data Protection / etc.

**Affected Requirement:** SEC-REQ-[XXX]

**Description:**
[Detailed description of the security issue identified]

**Current State:**
[What is currently implemented]

**Security Risk:**
[What could happen if this is not addressed? What's the security impact?]

**Recommendation:**
[Specific steps to remediate]

**Remediation Owner:** [Name]  
**Target Resolution Date:** [Date]

---

### Finding 2: [Title]

[Repeat structure for each finding]

---

## Positive Observations

**Security Strengths:**
- [Observation 1]: [Description]
- [Observation 2]: [Description]
- [Observation 3]: [Description]

[Highlight security controls implemented well]

---

## Architecture Review Checklist Results

[Reference to checklist from Section 5.2 - summary of results]

| Category | Compliant | Non-Compliant | N/A |
|----------|-----------|---------------|-----|
| Authentication | [#] | [#] | [#] |
| Authorization | [#] | [#] | [#] |
| Input Validation | [#] | [#] | [#] |
| Cryptography | [#] | [#] | [#] |
| [etc.] | | | |

**Overall Checklist Score:** [%] compliant

---

## Recommendations

**General Recommendations:**
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

**Future Considerations:**
- [Long-term improvement 1]
- [Long-term improvement 2]

---

## Conclusion

[Summary paragraph on overall security architecture assessment]

**Next Steps:**
1. Remediate Critical findings by [Date]
2. Remediate High findings by [Date]
3. Schedule follow-up review [Date]
4. [Additional next steps]

---

## Approval

**Security Architect:**

Name: ___________________________  
Signature: ___________________________  
Date: ___________________________

**Product Owner:**

Name: ___________________________  
Signature: ___________________________  
Date: ___________________________

---

## Appendices

### Appendix A: Architecture Diagrams
[Attach diagrams reviewed]

### Appendix B: Review Checklist
[Attach completed checklist]

### Appendix C: Related Documents
- Security Requirements Document: [Link]
- Threat Model: [Link]
- [Other documents]
```

---

## 6. Assessment Workbook Specification (Script 1)

### 6.1 Workbook Overview

**Workbook Name:** `ISMS_A826_Security_Requirements_Assessment_[Date].xlsx`

**Purpose:** Assess security requirements compliance for all applications in portfolio.

**Assessment Scope:**
- ISO/IEC 27001:2022 Control A.8.26 (Application Security Requirements)
- Security requirements documentation completeness
- Threat modeling completion
- Architecture review completion
- Requirements traceability

**Target Users:**
- Security Architects
- Application Security Teams
- Compliance Officers
- Auditors

### 6.2 Workbook Sheet Structure

**Sheet 1: Instructions & Legend**
- Workbook purpose and scope
- How to use the workbook
- Status legend (emoji indicators)
- Acceptable evidence examples
- Scoring methodology overview

**Sheet 2: Application_Inventory**
- Application name, ID, owner
- Risk classification (High/Medium/Low)
- Technology stack
- Deployment model
- Regulatory scope
- Internet-facing (Yes/No)
- Last assessment date

**Sheet 3: Requirements_Documentation_Status**
- Application name
- Requirements document exists? (Yes/No)
- Document location/link
- Last updated date
- Requirements approved? (Yes/No)
- Approver name and date
- Functional requirements coverage (%)
- Non-functional requirements coverage (%)
- Data protection requirements coverage (%)
- Overall completeness score (auto-calculated %)

**Sheet 4: Threat_Modeling_Status**
- Application name
- Threat model exists? (Yes/No/Planned)
- Threat modeling methodology used (STRIDE/PASTA/LINDDUN/Other)
- Threat model location/link
- Last updated date
- DFD created? (Yes/No)
- Threats documented? (Yes/No)
- Mitigations defined? (Yes/No)
- Threat model approved? (Yes/No/Pending)
- Approver name and date
- Completeness score (auto-calculated %)

**Sheet 5: Architecture_Review_Status**
- Application name
- Architecture review conducted? (Yes/No/Scheduled)
- Review date
- Review report location/link
- Reviewers (names)
- Critical findings (count)
- High findings (count)
- Medium findings (count)
- Low findings (count)
- Open findings (count)
- Architecture approved? (✅ Approved / ⏳ Pending / ❌ Not Approved)
- Approval date

**Sheet 6: Traceability_Matrix_Status**
- Application name
- Traceability matrix exists? (Yes/No)
- Matrix location/link
- Last updated date
- Requirements traced to design? (Yes/No/Partial)
- Requirements traced to code? (Yes/No/Partial)
- Requirements traced to tests? (Yes/No/Partial)
- Traceability coverage (%)
- Traceability quality score (auto-calculated %)

**Sheet 7: Compliance_Summary**
- **Dashboard view** with overall scores
- Applications by risk level (High/Medium/Low)
- Compliance status by application
- Overall portfolio compliance score
- Gap summary (applications missing requirements, threat models, etc.)
- Conditional formatting (green/yellow/red)

**Sheet 8: Evidence_Register**
- Evidence type (Requirements Doc, Threat Model, Architecture Review, Traceability Matrix)
- Application name
- Document title/description
- Document location/link
- Last updated
- Owner
- Status (Current, Outdated, Missing)

**Sheet 9: Approval_Sign_Off**
- Assessment information (date, assessor, organization)
- Approval table (Approver, Role, Date, Signature/Comments)
- Overall compliance determination
- Recommended actions

### 6.3 Data Sources

**Where to Get Data:**

**Application Inventory (Sheet 2):**
- Source: Application portfolio database, CMDB, Jira/ADO
- Update: Quarterly or when applications added/retired

**Requirements Documentation (Sheet 3):**
- Source: Document repository (SharePoint, Confluence, Google Drive)
- Validation: Check for SEC-REQ-XXX document per application
- Update: After each requirements approval

**Threat Models (Sheet 4):**
- Source: Document repository, threat modeling tool exports
- Validation: Check for threat model document per application
- Update: After each threat modeling workshop

**Architecture Reviews (Sheet 5):**
- Source: Architecture review reports (document repository)
- Validation: Check for architecture review report
- Update: After each architecture review

**Traceability Matrices (Sheet 6):**
- Source: Requirements management tool (Jira, ADO, Excel)
- Validation: Check for traceability matrix per application
- Update: Quarterly review

### 6.4 Scoring Algorithms

**Requirements Documentation Completeness Score (Sheet 3, Column K):**

Formula:
```
Completeness Score = (Functional_Coverage + NonFunctional_Coverage + DataProtection_Coverage) / 3

Where:
- Functional_Coverage = % of functional security requirements documented
- NonFunctional_Coverage = % of non-functional security requirements documented
- DataProtection_Coverage = % of data protection requirements documented

If all three categories = 100%, then Completeness Score = 100%
```

Example Excel Formula (Cell K3):
```
=IF(AND(H3<>"",I3<>"",J3<>""), (H3+I3+J3)/3, "")
```

**Threat Modeling Completeness Score (Sheet 4, Column K):**

Formula:
```
Completeness Score = (DFD_Created × 25%) + (Threats_Documented × 25%) + 
                     (Mitigations_Defined × 25%) + (Approved × 25%)

Where each component is 1 (Yes) or 0 (No)
```

Example Excel Formula (Cell K3):
```
=IF(B3="Yes", 
  (IF(F3="Yes",25,0) + IF(G3="Yes",25,0) + IF(H3="Yes",25,0) + IF(I3="✅ Approved",25,0)),
  "N/A")
```

**Traceability Quality Score (Sheet 6, Column I):**

Formula:
```
Traceability Score = (Design_Traced × 33%) + (Code_Traced × 33%) + (Tests_Traced × 34%)

Where:
- Design_Traced: 100% if "Yes", 50% if "Partial", 0% if "No"
- Code_Traced: 100% if "Yes", 50% if "Partial", 0% if "No"
- Tests_Traced: 100% if "Yes", 50% if "Partial", 0% if "No"
```

Example Excel Formula (Cell I3):
```
=IF(B3="Yes",
  (IF(E3="Yes",33,IF(E3="Partial",16.5,0)) + 
   IF(F3="Yes",33,IF(F3="Partial",16.5,0)) + 
   IF(G3="Yes",34,IF(G3="Partial",17,0))),
  "N/A")
```

**Overall Application Compliance Score (Sheet 7):**

Formula:
```
Overall Score = (Requirements_Score × 40%) + (ThreatModel_Score × 30%) + 
                (ArchReview_Score × 20%) + (Traceability_Score × 10%)

Where:
- Requirements_Score from Sheet 3, Column K
- ThreatModel_Score from Sheet 4, Column K
- ArchReview_Score = 100% if approved, 50% if pending, 0% if not approved
- Traceability_Score from Sheet 6, Column I
```

**Compliance Status:**
- ✅ **Compliant:** Overall Score ≥ 80%
- ⚠️ **Partial Compliance:** Overall Score 60-79%
- ❌ **Non-Compliant:** Overall Score < 60%

### 6.5 Conditional Formatting Rules

**Apply to Sheet 7 (Compliance_Summary):**

**Overall Compliance Score (Column):**
- Green (C6EFCE): Score ≥ 80%
- Yellow (FFEB9C): Score 60-79%
- Red (FFC7CE): Score < 60%

**Compliance Status (Column):**
- Green fill: "✅ Compliant"
- Yellow fill: "⚠️ Partial Compliance"
- Red fill: "❌ Non-Compliant"

**Open Findings Count (Column in Sheet 5):**
- Red bold: Count > 0 (open critical findings)
- Yellow: Count > 0 (open high findings)

### 6.6 Example Data Rows

**Sheet 2 Example (Application_Inventory):**

| Application Name | App ID | Owner | Risk | Technology | Deployment | Regulatory | Internet | Last Assessment |
|------------------|--------|-------|------|------------|------------|-----------|----------|-----------------|
| Customer Portal | APP-001 | Jane Doe | High Risk | Java/Spring | AWS Cloud | GDPR, PCI | Yes | 2025-01-15 |
| Internal HR | APP-002 | John Smith | Medium Risk | Python/Django | On-Prem | GDPR | No | 2024-12-10 |
| Marketing Site | APP-003 | Alice Johnson | Medium Risk | Static HTML | CDN | None | Yes | 2025-01-05 |

**Sheet 3 Example (Requirements_Documentation_Status):**

| Application | Doc Exists | Location | Updated | Approved | Approver | Functional | Non-Functional | Data Protection | Completeness |
|-------------|-----------|----------|---------|----------|----------|-----------|---------------|-----------------|--------------|
| Customer Portal | Yes | /docs/APP-001-sec-req.pdf | 2025-01-10 | Yes | J. Doe | 95% | 90% | 100% | 95% |
| Internal HR | Yes | /docs/APP-002-sec-req.pdf | 2024-11-20 | Yes | J. Smith | 85% | 80% | 90% | 85% |
| Marketing Site | Partial | /docs/APP-003-baseline.pdf | 2024-12-15 | Yes | A. Johnson | 60% | 50% | 70% | 60% |

**Sheet 7 Example (Compliance_Summary):**

| Application | Risk | Req Score | TM Score | Arch Score | Trace Score | Overall | Status |
|-------------|------|-----------|----------|------------|-------------|---------|--------|
| Customer Portal | High | 95% | 100% | 100% | 90% | 96% | ✅ Compliant |
| Internal HR | Medium | 85% | 75% | 100% | 80% | 84% | ✅ Compliant |
| Marketing Site | Medium | 60% | N/A | 50% | N/A | 56% | ❌ Non-Compliant |

### 6.7 Data Validation Dropdowns

**Risk Classification (Sheet 2, Column E):**
- Values: "High Risk", "Medium Risk", "Low Risk"

**Yes/No Fields:**
- Values: "Yes", "No"

**Yes/No/Partial:**
- Values: "Yes", "No", "Partial"

**Yes/No/Planned:**
- Values: "Yes", "No", "Planned"

**Approval Status:**
- Values: "✅ Approved", "⏳ Pending", "❌ Not Approved"

**Threat Modeling Methodology:**
- Values: "STRIDE", "PASTA", "LINDDUN", "Other", "N/A"

**Evidence Status:**
- Values: "Current", "Outdated", "Missing"

### 6.8 Workbook Formulas Summary

**Key Formulas:**

```excel
// Requirements Completeness (Sheet 3, K3)
=IF(AND(H3<>"",I3<>"",J3<>""), (H3+I3+J3)/3, "")

// Threat Modeling Completeness (Sheet 4, K3)
=IF(B3="Yes", 
  (IF(F3="Yes",25,0) + IF(G3="Yes",25,0) + IF(H3="Yes",25,0) + IF(I3="✅ Approved",25,0)),
  "N/A")

// Traceability Quality (Sheet 6, I3)
=IF(B3="Yes",
  (IF(E3="Yes",33,IF(E3="Partial",16.5,0)) + 
   IF(F3="Yes",33,IF(F3="Partial",16.5,0)) + 
   IF(G3="Yes",34,IF(G3="Partial",17,0))),
  "N/A")

// Overall Compliance Score (Sheet 7, G3)
=IF(COUNT('Requirements_Documentation_Status'!K:K,'Threat_Modeling_Status'!K:K) > 0,
  ('Requirements_Documentation_Status'!K3*0.4) + 
  ('Threat_Modeling_Status'!K3*0.3) + 
  (IF('Architecture_Review_Status'!K3="✅ Approved",100,IF('Architecture_Review_Status'!K3="⏳ Pending",50,0))*0.2) +
  ('Traceability_Matrix_Status'!I3*0.1),
  "")

// Compliance Status (Sheet 7, H3)
=IF(G3>=80,"✅ Compliant",IF(G3>=60,"⚠️ Partial Compliance","❌ Non-Compliant"))
```

---

## 7. Implementation Timeline

### 7.1 Phased Rollout Plan

**Phase 1: Pilot (Weeks 1-4)**

*Week 1-2: Training and Preparation*
- [ ] Train Product Managers on security requirements process
- [ ] Train Security Architects on threat modeling
- [ ] Set up document repository structure
- [ ] Configure requirements template
- [ ] Select 2-3 pilot applications (mix of High/Medium risk)

*Week 3-4: Pilot Execution*
- [ ] Execute requirements elicitation for pilot apps
- [ ] Conduct threat modeling workshops
- [ ] Perform architecture reviews
- [ ] Create traceability matrices
- [ ] Collect feedback and refine process

**Phase 2: High-Risk Applications (Months 2-3)**

*Month 2:*
- [ ] Identify all High Risk applications (from application inventory)
- [ ] Schedule requirements workshops for each application
- [ ] Conduct security requirements elicitation
- [ ] Document requirements using template

*Month 3:*
- [ ] Conduct threat modeling for High Risk applications
- [ ] Perform architecture reviews
- [ ] Establish traceability matrices
- [ ] Complete Assessment Workbook 1 for High Risk apps

**Phase 3: Medium-Risk Applications (Months 4-6)**

*Month 4-6:*
- [ ] Identify all Medium Risk applications
- [ ] Execute security requirements process (may be streamlined vs. High Risk)
- [ ] Conduct threat modeling (STRIDE recommended)
- [ ] Perform architecture reviews (may be less formal)
- [ ] Complete Assessment Workbook 1 for Medium Risk apps

**Phase 4: Low-Risk Applications (Months 7-9)**

*Month 7-9:*
- [ ] Identify Low Risk applications
- [ ] Apply baseline security requirements (streamlined process)
- [ ] Lightweight threat analysis (may skip formal threat model)
- [ ] Design review with security checklist (may skip formal architecture review)
- [ ] Complete Assessment Workbook 1 for Low Risk apps

**Phase 5: Continuous Improvement (Month 10+)**

*Ongoing:*
- [ ] Annual updates for existing applications
- [ ] Security requirements for new applications (integrated into SDLC)
- [ ] Quarterly assessment workbook updates
- [ ] Process refinement based on lessons learned

### 7.2 Resource Requirements

**Roles and Time Commitment:**

**Security Architects:**
- Training: 8 hours (one-time)
- Requirements review: 2-4 hours per application
- Threat modeling facilitation: 3-4 hours per application
- Architecture review: 2-3 hours per application

**Product Owners/Managers:**
- Training: 4 hours (one-time)
- Requirements elicitation: 4-8 hours per application
- Threat modeling participation: 3 hours per application
- Architecture review participation: 2 hours per application

**Application Architects:**
- Requirements elicitation support: 2-4 hours per application
- Threat modeling participation: 3 hours per application
- Architecture review preparation: 4-6 hours per application
- Architecture review meeting: 2-3 hours per application

**Developers:**
- Traceability matrix updates: 1-2 hours per sprint (ongoing)
- Threat modeling participation: 3 hours per application (optional)

### 7.3 Success Metrics

**Key Performance Indicators (KPIs):**

**Coverage Metrics:**
- % of High Risk applications with documented security requirements
- % of High Risk applications with approved threat models
- % of High Risk applications with architecture reviews
- % of applications with requirements traceability

**Target:** 100% of High Risk applications within 6 months

**Quality Metrics:**
- Average requirements completeness score (target: ≥ 90%)
- Average threat model completeness score (target: ≥ 90%)
- % of applications with zero open architecture review findings (target: ≥ 70%)

**Process Metrics:**
- Average time from requirements elicitation to approval (target: ≤ 2 weeks)
- Average time from threat modeling to approval (target: ≤ 1 week)
- Average time from architecture review to approval (target: ≤ 2 weeks)

**Compliance Metrics:**
- Overall portfolio compliance score (target: ≥ 85%)
- % of applications meeting compliance threshold (target: ≥ 90%)

**Track Metrics:**
- Monthly compliance dashboard review
- Quarterly trend analysis
- Annual compliance report

---

## 8. Common Pitfalls and Solutions

### 8.1 Requirements Elicitation Pitfalls

**Pitfall 1: Vague Requirements**

❌ **Example:** "Application must be secure"  
**Problem:** Not testable, not specific, not implementable

✅ **Solution:** Make specific and testable
- "Application MUST implement multi-factor authentication (MFA) for all users"
- Acceptance Criteria: MFA enrollment required; supports TOTP/push/hardware tokens
- Test Method: Functional test - verify MFA required for login

**Pitfall 2: Technology-Specific Requirements**

❌ **Example:** "Application must use Auth0 for authentication"  
**Problem:** Locks into specific vendor, limits implementation options

✅ **Solution:** Make technology-agnostic
- "Application MUST support industry-standard authentication protocols (OAuth 2.0, OIDC, SAML 2.0)"
- Rationale: Vendor flexibility, standards compliance

**Pitfall 3: Missing Acceptance Criteria**

❌ **Example:** "Application must validate inputs"  
**Problem:** How do we verify this requirement is met?

✅ **Solution:** Define clear acceptance criteria
- "Application MUST validate all user inputs using allowlist validation"
- Acceptance Criteria: Input validation applied server-side; uses allowlists where possible; no SQL injection, XSS, command injection vulnerabilities
- Test Method: SAST scan + DAST scan + code review

### 8.2 Threat Modeling Pitfalls

**Pitfall 1: Incomplete DFD**

❌ **Problem:** Missing components, data flows, or trust boundaries  
**Impact:** Threats not identified, false sense of security

✅ **Solution:**
- Involve architects and developers in DFD creation
- Walk through user workflows to validate completeness
- Identify ALL trust boundaries (especially authentication boundaries)
- Review DFD with team before STRIDE analysis

**Pitfall 2: Analysis Paralysis**

❌ **Problem:** Trying to identify every possible threat (hundreds of threats documented)  
**Impact:** Workshop takes too long, team overwhelmed, threat model not actionable

✅ **Solution:**
- Focus on realistic, high-impact threats
- Use risk scoring to prioritize
- Time-box threat identification (2-3 hours max)
- Document top 10-20 threats, not every theoretical threat

**Pitfall 3: No Follow-Up on Mitigations**

❌ **Problem:** Threats identified, mitigations defined, but never implemented  
**Impact:** Threat model becomes "shelf-ware", no security improvement

✅ **Solution:**
- Link threats to security requirements (SEC-REQ-XXX)
- Create Jira/ADO tickets for mitigations
- Track mitigation implementation
- Include mitigation status in architecture review

### 8.3 Architecture Review Pitfalls

**Pitfall 1: Review Too Late**

❌ **Problem:** Architecture review conducted after implementation complete  
**Impact:** Expensive to fix architectural issues, resistance to changes

✅ **Solution:**
- Schedule architecture review in design phase (before coding starts)
- Make architecture review a gate in SDLC
- For existing applications, conduct review before major refactoring

**Pitfall 2: No Clear Findings**

❌ **Problem:** Review conducted but no documented findings or action items  
**Impact:** Issues not tracked, not resolved

✅ **Solution:**
- Document all findings in architecture review report
- Assign severity, owner, due date for each finding
- Track findings in Jira/ADO
- Follow up until resolved

**Pitfall 3: Rubber Stamp Review**

❌ **Problem:** Review meeting is just a presentation, no critical analysis  
**Impact:** Security issues not identified

✅ **Solution:**
- Security Architect asks probing questions
- Use architecture review checklist systematically
- Challenge assumptions
- Don't approve architecture with unresolved critical issues

### 8.4 Traceability Pitfalls

**Pitfall 1: Traceability Matrix Never Updated**

❌ **Problem:** Matrix created but never updated during development  
**Impact:** Traceability outdated, not useful for audits

✅ **Solution:**
- Make traceability update part of "definition of done"
- Code review checklist includes traceability verification
- Quarterly traceability audits

**Pitfall 2: No Tool Support**

❌ **Problem:** Using Excel for traceability in large applications  
**Impact:** Manual updates error-prone, doesn't scale

✅ **Solution:**
- Use requirements management tool (Jira, Azure DevOps)
- Consider automated traceability (code annotations → automated links)
- For small apps, Excel is fine; for large apps, use tools

---

## 9. Templates and Resources

### 9.1 Available Templates

**Requirements Template:**
- File: `Security_Requirements_Template_[APP-ID].docx`
- Location: `/templates/security-requirements/`
- Format: Word document with requirement table structure

**Threat Modeling Workshop Agenda:**
- File: `Threat_Modeling_Workshop_Agenda.docx`
- Location: `/templates/threat-modeling/`
- Format: Workshop facilitation guide

**Architecture Review Checklist:**
- File: `Architecture_Review_Checklist.xlsx`
- Location: `/templates/architecture-review/`
- Format: Excel checklist (Section 5.2)

**Architecture Review Report:**
- File: `Architecture_Review_Report_Template.docx`
- Location: `/templates/architecture-review/`
- Format: Word document (Section 5.3)

**Traceability Matrix:**
- File: `Requirements_Traceability_Matrix_Template.xlsx`
- Location: `/templates/traceability/`
- Format: Excel template

### 9.2 Training Materials

**Security Requirements Training:**
- Audience: Product Managers, Business Analysts
- Duration: 4 hours
- Topics: Risk classification, requirements elicitation, template usage, approval workflow
- Delivery: Instructor-led workshop

**Threat Modeling Training:**
- Audience: Security Architects, Application Architects, Senior Developers
- Duration: 8 hours (4 hours theory + 4 hours hands-on)
- Topics: STRIDE methodology, DFD creation, threat identification, mitigation definition
- Delivery: Instructor-led workshop with hands-on exercise

**Architecture Review Training:**
- Audience: Security Architects, Architects
- Duration: 4 hours
- Topics: Review process, checklist usage, findings documentation, remediation tracking
- Delivery: Instructor-led workshop

### 9.3 Tool Recommendations

**Document Repository:**
- SharePoint, Confluence, Google Drive
- Version control for requirements documents

**Threat Modeling Tools:**
- Microsoft Threat Modeling Tool (free, Windows)
- OWASP Threat Dragon (open-source, cross-platform)
- Manual: Whiteboard + Excel/Visio

**Requirements Management:**
- Small organizations: Excel, Google Sheets
- Medium organizations: Jira, Azure DevOps (built-in traceability)
- Large/regulated organizations: IBM DOORS, Jama Connect

**Diagram Tools:**
- Visio, Draw.io, Lucidchart (for DFDs, architecture diagrams)

---

## 10. Integration with SDLC

### 10.1 Security Requirements in SDLC Phases

**Requirements Phase:**
- Activity: Security requirements elicitation (Section 3)
- Deliverable: Security requirements document (SEC-REQ-XXX)
- Owner: Product Owner + Security Architect
- Gate: Requirements approval required before design

**Design Phase:**
- Activity: Threat modeling (Section 4)
- Activity: Security architecture review (Section 5)
- Deliverable: Threat model, Architecture review report
- Owner: Application Architect + Security Architect
- Gate: Architecture approval required before implementation

**Implementation Phase:**
- Activity: Requirements traceability updates (Section 3.4)
- Activity: Secure coding per requirements (see IMP-S3)
- Deliverable: Code with traceability to requirements
- Owner: Developers
- Gate: Code review includes requirements verification

**Testing Phase:**
- Activity: Security testing per requirements (see IMP-S4)
- Activity: Test case linkage to requirements
- Deliverable: Test results with requirement coverage
- Owner: QA + Security Tester
- Gate: All security requirements tested

**Deployment Phase:**
- Activity: Final security sign-off
- Deliverable: Security acceptance
- Owner: Security Architect
- Gate: All critical/high findings resolved

**Maintenance Phase:**
- Activity: Annual security requirements review
- Activity: Requirements updates for changes
- Deliverable: Updated security requirements
- Owner: Product Owner + Security Architect

### 10.2 Gate Criteria

**Design Gate:**
- [ ] Security requirements documented and approved
- [ ] Threat model completed and approved
- [ ] Architecture review passed (no open critical findings)

**Implementation Gate:**
- [ ] Code review includes security requirements verification
- [ ] Traceability matrix updated

**Release Gate:**
- [ ] Security testing complete (SAST, DAST, SCA - see IMP-S4)
- [ ] All critical findings resolved
- [ ] All high findings resolved or risk-accepted
- [ ] Security sign-off obtained

---

## 11. Continuous Improvement

### 11.1 Process Review

**Quarterly Review:**
- Review process effectiveness
- Collect feedback from Product Owners, Architects, Developers
- Identify process bottlenecks
- Update templates based on lessons learned

**Annual Review:**
- Comprehensive process assessment
- Update templates for new threats/vulnerabilities (e.g., OWASP Top 10 updates)
- Benchmark against industry standards
- Update training materials

### 11.2 Metrics-Driven Improvement

**Track:**
- Requirements approval timeline (target: ≤ 2 weeks)
- Threat modeling workshop effectiveness (participant feedback)
- Architecture review finding resolution time
- Requirement traceability coverage

**Analyze:**
- Identify trends (common findings, common gaps)
- Identify high-friction process steps
- Assess training effectiveness

**Improve:**
- Streamline high-friction steps
- Enhance training for common gaps
- Update templates to address common issues

### 11.3 Staying Current

**Industry Updates:**
- Monitor OWASP Top 10 updates (annually)
- Review NIST SSDF updates
- Follow security research and trends
- Update threat models for new threat vectors

**Regulatory Updates:**
- Monitor GDPR guidance updates
- Track industry-specific regulations (PCI DSS, HIPAA, etc.)
- Update requirements templates for new regulatory requirements

---

## 12. Support and Escalation

### 12.1 Support Contacts

**Security Requirements Questions:**
- Contact: Security Architecture Team
- Email: security-architecture@[organization].com
- Response SLA: 2 business days

**Threat Modeling Support:**
- Contact: Security Architecture Team
- Email: security-architecture@[organization].com
- Threat modeling workshop scheduling: [booking link]

**Architecture Review Scheduling:**
- Contact: Security Architecture Team
- Email: security-architecture@[organization].com
- Review scheduling SLA: 1 week notice

**Tool Support:**
- Contact: IT Help Desk
- Email: helpdesk@[organization].com
- For: Document repository access, requirements management tools

### 12.2 Escalation Path

**Issue:** Security requirements dispute (disagreement on requirements)  
**Escalation:** Product Owner → Security Architect → CISO

**Issue:** Architecture review finding dispute (disagreement on severity/remediation)  
**Escalation:** Application Architect → Security Architect → CISO + CTO

**Issue:** Resource constraints (insufficient time for security requirements process)  
**Escalation:** Product Owner → Business Unit Leadership → CISO

---

## 13. Conclusion

This implementation guide provides comprehensive, step-by-step procedures for implementing the security requirements process defined in ISMS-POL-A.8.25-26-29-S2.

**Key Takeaways:**
- Security requirements must be **specific, testable, and risk-based**
- Threat modeling is **essential** for High Risk applications
- Architecture reviews **catch design issues early** (cheapest to fix)
- Requirements traceability enables **audit compliance**
- Process must be **integrated into SDLC**, not bolted on

**Success Factors:**
- Executive support and resource allocation
- Training for all participants
- Clear templates and tools
- Metrics and continuous improvement
- Integration with existing processes

**Next Steps:**
1. Review this guide with Security Architecture team
2. Customize templates for your organization
3. Conduct pilot with 2-3 applications
4. Refine process based on pilot feedback
5. Roll out to High Risk applications
6. Expand to full application portfolio

For questions or support, contact the Security Architecture team.

---

**Document End**
