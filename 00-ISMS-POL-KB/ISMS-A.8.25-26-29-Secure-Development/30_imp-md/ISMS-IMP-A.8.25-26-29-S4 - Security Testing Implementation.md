# ISMS-IMP-A.8.25-26-29-S4
## Security Testing Implementation - Implementation Guide
### ISO/IEC 27001:2022 Control A.8.29 (Security Testing in Development and Acceptance)

---

## Document Control

**Document ID:** ISMS-IMP-A.8.25-26-29-S4  
**Implementation Area:** Security Testing Throughout Development  
**Related Policy:** ISMS-POL-A.8.25-26-29-S4 (Security Testing - A.8.29)  
**Purpose:** Step-by-step implementation guidance for security testing activities including SAST, DAST, SCA, penetration testing, and security acceptance testing

**Regulatory Context:**
- ISO/IEC 27001:2022 Control A.8.29 (Security Testing in Development and Acceptance)
- OWASP Testing Guide
- NIST SP 800-115 (Technical Guide to Information Security Testing)
- See ISMS-POL-00 for complete regulatory applicability framework

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides practical, step-by-step procedures for implementing comprehensive security testing throughout the software development lifecycle as defined in POL-S4. It covers:

- Static Application Security Testing (SAST) implementation and optimization
- Dynamic Application Security Testing (DAST) deployment and execution
- Software Composition Analysis (SCA) continuous monitoring
- Interactive Application Security Testing (IAST) deployment (if applicable)
- Penetration testing program establishment
- Security acceptance testing integration
- Security testing results management and remediation workflows

**Note:** SAST and SCA tool deployment basics are covered in IMP-S3. This guide focuses on comprehensive security testing strategy, advanced configurations, and testing execution.

### 1.2 Target Audience

- **Primary:** Security Team, QA/Test Engineers, Security Champions
- **Supporting:** Developers, DevOps Engineers, Penetration Testers
- **Oversight:** Security Architects, CISO, QA Leadership

### 1.3 Prerequisites

**Before implementing security testing:**
- [ ] Read ISMS-POL-A.8.25-26-29-S4 (Security Testing Policy)
- [ ] Security requirements defined (IMP-S1)
- [ ] SDLC security integration in place (IMP-S2)
- [ ] SAST and SCA tools deployed (IMP-S3)
- [ ] Test environments available (dev, test, staging)

### 1.4 Process Dependencies

**Integrates with:**
- Security requirements (IMP-S1) - defines test cases
- SDLC integration (IMP-S2) - defines when testing occurs
- Secure coding (IMP-S3) - SAST/SCA basics
- Environment separation (ISMS-POL-A.8.31) - test environment security
- Vulnerability management (ISMS-POL-A.8.8) - production vulnerability handling

---

## 2. Security Testing Strategy

### 2.1 Layered Security Testing Approach

**Testing Types by SDLC Phase:**

```
┌────────────────────────────────────────────────────────────────┐
│ LAYERED SECURITY TESTING STRATEGY                             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│ Development Phase (Continuous)                                 │
│   ├─ SAST: Per commit (automated in CI/CD)                    │
│   ├─ SCA: Per build (automated in CI/CD)                      │
│   └─ Secret Scanning: Pre-commit (hook)                       │
│                                                                │
│ Testing Phase (Pre-Release)                                   │
│   ├─ DAST: Per deployment to test environment                 │
│   ├─ API Security Testing: Per API deployment                 │
│   └─ Security Acceptance Testing: Before UAT                  │
│                                                                │
│ Staging Phase (High-Risk Applications)                        │
│   ├─ IAST: Runtime analysis in staging                        │
│   └─ Penetration Testing: Before production                   │
│                                                                │
│ Production (Ongoing)                                          │
│   ├─ Vulnerability Scanning: Weekly/monthly                   │
│   └─ Bug Bounty: Continuous (if applicable)                   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 2.2 Security Testing Coverage Goals

**Coverage Targets:**

| Testing Type | Frequency | Coverage Goal | Responsibility |
|-------------|-----------|---------------|----------------|
| **SAST** | Per commit | 100% of code | Developers + CI/CD |
| **SCA** | Per build | 100% of dependencies | Developers + CI/CD |
| **Secret Scanning** | Pre-commit | 100% of commits | Developers |
| **DAST** | Per release | 100% of internet-facing apps | Security Team + QA |
| **API Security Testing** | Per release | 100% of public APIs | Security Team |
| **Penetration Testing** | Annually or per major release | 100% of high-risk apps | Security Team or External |
| **Security Acceptance Testing** | Per release | Critical security requirements | QA + Security Champion |

### 2.3 Risk-Based Testing Approach

**Testing Intensity by Risk Level:**

**High-Risk Applications:**
- SAST: Per commit (fail build on high/critical)
- SCA: Per build (fail build on high/critical)
- DAST: Weekly + per release
- Penetration Testing: Annually + per major release
- Security Acceptance Testing: All security requirements

**Medium-Risk Applications:**
- SAST: Per commit (fail build on critical)
- SCA: Per build (fail build on critical)
- DAST: Per release
- Penetration Testing: Every 2 years or major changes
- Security Acceptance Testing: Critical security requirements

**Low-Risk Applications:**
- SAST: Per commit (warning on critical, no fail)
- SCA: Per build (warning on critical, no fail)
- DAST: Annually or major changes
- Penetration Testing: Optional
- Security Acceptance Testing: Basic security checks

---

## 3. SAST Implementation and Optimization

**Note:** Basic SAST deployment is covered in IMP-S3 Section 4.1. This section covers advanced configuration and optimization.

### 3.1 SAST Tool Optimization

**Reducing False Positives:**

**Step 1: Baseline Scan and Initial Triage**
- Run SAST on entire codebase
- Triage all findings (true positive, false positive, won't fix)
- Suppress false positives (tool-specific suppression mechanisms)

**Step 2: Configure Quality Gates**

**SonarQube Quality Gate Example:**
```
Security Rating: A (no vulnerabilities) for new code
Security Hotspots: No open hotspots for new code
Coverage on New Code: >= 80%
```

**Snyk Policy Example:**
```yaml
# .snyk
version: v1.22.0
ignore:
  'SNYK-JS-LODASH-590103':  # Prototype pollution in lodash
    - '*':
        reason: Not exploitable in our usage (no user-controlled input)
        expires: 2025-12-31
```

**Step 3: Custom Rules (if needed)**

**SonarQube Custom Rule Example (Java):**
```java
// Detect usage of insecure cryptography
// Pattern: Cipher.getInstance("DES/...")
@Rule(key = "InsecureCipher", name = "Insecure cryptographic algorithm")
public class InsecureCipherCheck extends BaseTreeVisitor {
    @Override
    public void visitMethodInvocation(MethodInvocationTree tree) {
        if ("getInstance".equals(tree.symbol().name()) &&
            tree.arguments().get(0).is(Tree.Kind.STRING_LITERAL)) {
            String algorithm = ((LiteralTree) tree.arguments().get(0)).value();
            if (algorithm.contains("DES") || algorithm.contains("RC4")) {
                reportIssue(tree, "Insecure algorithm: " + algorithm);
            }
        }
        super.visitMethodInvocation(tree);
    }
}
```

### 3.2 SAST Findings Triage Workflow

**Triage Process:**

**Step 1: Automated Triage**
- SAST tool creates issue in tracking system (Jira, Azure DevOps)
- Issue assigned to developer who committed code (auto-assignment)

**Step 2: Developer Assessment**
- Developer reviews finding
- Determines: True Positive, False Positive, or Won't Fix

**Step 3: Security Champion Review (for Critical/High)**
- Security Champion reviews critical/high findings
- Validates developer's assessment
- Approves suppression (if false positive)

**Step 4: Remediation**
- If true positive: Developer fixes, re-scans
- If false positive: Suppress in SAST tool, document rationale
- If won't fix: Risk acceptance process (document, CISO approval)

**Triage SLA:**
- Critical: 2 business days
- High: 5 business days
- Medium: 10 business days
- Low: Best effort

---

## 4. DAST Implementation

### 4.1 DAST Tool Selection

**DAST Tool Options:**

| Tool | Type | Features | Integration | Cost | Best For |
|------|------|----------|-------------|------|----------|
| **OWASP ZAP** | Open-source | Comprehensive, actively maintained | CLI, CI/CD | Free | Most organizations |
| **Burp Suite Pro** | Commercial | Deep scanning, manual testing | CLI, manual | Paid | Penetration testing teams |
| **Acunetix** | Commercial | Fast, low false positives | CI/CD | Paid | Enterprise |
| **AppScan** (IBM) | Commercial | Enterprise features, compliance reports | CI/CD | Paid | Large enterprises |
| **Netsparker** (Invicti) | Commercial | Proof-based scanning (low false positives) | CI/CD | Paid | Accuracy-focused |

**Recommendation:** **OWASP ZAP** for most organizations (free, comprehensive). Upgrade to commercial if needed (lower false positives, better support).

### 4.2 OWASP ZAP Deployment

**Installation:**

**Docker (Recommended for CI/CD):**
```bash
# Pull OWASP ZAP Docker image
docker pull owasp/zap2docker-stable
```

**Standalone:**
```bash
# Download from https://www.zaproxy.org/download/
# Install on test server or security team workstation
```

### 4.3 DAST Scan Types

**Three Scan Types:**

**1. Baseline Scan (Fast, Passive)**
- **Purpose:** Quick security check, no attacks
- **Time:** 5-15 minutes
- **Use Case:** CI/CD per deployment (fast feedback)
- **Command:**
```bash
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t https://test.example.com \
  -r baseline-report.html
```

**2. Full Scan (Comprehensive, Active)**
- **Purpose:** Deep scan with active attacks
- **Time:** 1-4 hours (depending on application size)
- **Use Case:** Weekly or per release (pre-production)
- **Command:**
```bash
docker run -t owasp/zap2docker-stable zap-full-scan.py \
  -t https://test.example.com \
  -r full-scan-report.html
```

**3. API Scan**
- **Purpose:** Scan REST APIs
- **Time:** 30 minutes - 2 hours
- **Use Case:** Per API release
- **Command:**
```bash
# Provide OpenAPI/Swagger specification
docker run -t owasp/zap2docker-stable zap-api-scan.py \
  -t https://api.example.com/swagger.json \
  -f openapi \
  -r api-scan-report.html
```

### 4.4 DAST CI/CD Integration

**GitLab CI/CD Integration:**

```yaml
# .gitlab-ci.yml
dast_scan:
  stage: security
  image: owasp/zap2docker-stable
  script:
    - mkdir -p /zap/wrk/
    # Baseline scan (fast)
    - zap-baseline.py -t $TEST_URL -r baseline-report.html || true
    # Generate JSON report for parsing
    - zap-baseline.py -t $TEST_URL -J dast-report.json || true
  artifacts:
    reports:
      dast: dast-report.json
    paths:
      - baseline-report.html
    expire_in: 1 week
  allow_failure: true  # Don't fail pipeline on findings (review manually)
  only:
    - main
    - develop
```

**GitHub Actions Integration:**

```yaml
# .github/workflows/dast.yml
name: DAST Scan

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * 1'  # Weekly on Monday 2 AM

jobs:
  zap_scan:
    runs-on: ubuntu-latest
    steps:
      - name: ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.7.0
        with:
          target: 'https://test.example.com'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'
```

### 4.5 DAST Authenticated Scanning

**Challenge:** Many applications require authentication. DAST needs to scan authenticated pages.

**Solution: Session-Based Authentication**

**Step 1: Manual Login and Session Capture**
- Manually log in to application via browser
- Use ZAP proxy to capture login request
- Export session cookies

**Step 2: Configure ZAP with Session**

**Context File (zap-context.xml):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <context>
    <name>Test App</name>
    <desc>Authenticated context for test.example.com</desc>
    <incregexes>https://test.example.com.*</incregexes>
    <authentication>
      <type>2</type>  <!-- Form-based -->
      <loggedin>\QLogged in as\E</loggedin>
      <loggedout>\QLog in\E</loggedout>
    </authentication>
    <users>
      <user>
        <name>test-user</name>
        <credentials>
          <field>
            <key>username</key>
            <value>testuser@example.com</value>
          </field>
          <field>
            <key>password</key>
            <value>${TEST_PASSWORD}</value>
          </field>
        </credentials>
      </user>
    </users>
  </context>
</configuration>
```

**Step 3: Run Authenticated Scan**
```bash
docker run -t owasp/zap2docker-stable zap-full-scan.py \
  -t https://test.example.com \
  -n zap-context.xml \
  -U test-user \
  -r authenticated-scan.html
```

**Alternative: API Token Authentication**
```bash
# Pass API token via header
docker run -t owasp/zap2docker-stable zap-api-scan.py \
  -t https://api.example.com/swagger.json \
  -z "-config api.addkey=Authorization -config api.addvalue='Bearer ${API_TOKEN}'" \
  -r api-scan.html
```

### 4.6 DAST Findings Management

**DAST Report Review:**

**ZAP Report Sections:**
- **Alerts:** Vulnerabilities found (severity, confidence, instances)
- **Risk:** High, Medium, Low, Informational
- **Instances:** URLs where vulnerability found

**Triage Workflow:**

**Step 1: Review High/Medium Findings**
- Validate findings (manually test to confirm)
- Categorize: True Positive, False Positive

**Step 2: Create Remediation Tickets**
- True positives → Create Jira/ADO tickets
- Assign to developers
- Link to DAST report finding

**Step 3: Suppress False Positives**

**ZAP Alert Suppression:**
```
# Create .zap/rules.tsv
# Format: rule_id  IGNORE  url_pattern  reason
10020  IGNORE  https://test.example.com/public/*  X-Frame-Options not needed for public pages
```

**Step 4: Track Remediation**
- Monitor ticket status
- Re-scan after fixes deployed
- Verify vulnerabilities resolved

---

## 5. SCA Continuous Monitoring

**Note:** Basic SCA deployment is covered in IMP-S3 Section 4.2. This section covers continuous monitoring and advanced dependency management.

### 5.1 SCA Continuous Monitoring Setup

**Snyk Monitor (Continuous Monitoring):**

```bash
# In CI/CD pipeline, after deployment
snyk monitor --project-name=my-app-production

# This creates ongoing monitoring
# Snyk will alert when new vulnerabilities discovered in dependencies
```

**GitHub Dependabot Alerts:**
- Automatically enabled for public repos
- Dependabot creates PRs for dependency updates
- Security → Dependabot alerts shows active vulnerabilities

### 5.2 Dependency Update Policy

**Automated Updates (Low-Risk):**
- Patch versions (e.g., 1.2.3 → 1.2.4): Auto-merge (if tests pass)
- Minor versions (e.g., 1.2.0 → 1.3.0): Auto-create PR, manual review

**Manual Updates (High-Risk):**
- Major versions (e.g., 1.0.0 → 2.0.0): Manual upgrade, testing required
- Breaking changes: Test thoroughly before merging

**Security Updates (Critical):**
- Critical vulnerabilities: Emergency process (fix within 7 days)
- Bypass normal release cycle if needed

### 5.3 Vulnerability Remediation Workflow

**When Vulnerability Discovered:**

**Step 1: Assess Vulnerability**
- **Severity:** Critical, High, Medium, Low (from CVE/NVD)
- **Exploitability:** Is vulnerable code path used in application?
- **Fix Availability:** Is patched version available?

**Step 2: Determine Remediation Path**

**Path A: Upgrade Dependency (Preferred)**
```bash
# Upgrade to patched version
npm update vulnerable-package

# Or specify version
npm install vulnerable-package@4.5.6

# Test application
npm test

# Verify vulnerability fixed
snyk test
```

**Path B: Patch (if no upgrade available)**
```bash
# Apply patch file
patch -p1 < fix.patch

# Or use package manager patches
# .yarnrc.yml
packageExtensions:
  "vulnerable-package@*":
    peerDependencies:
      safe-dependency: "^2.0.0"
```

**Path C: Workaround (if no fix available)**
- Disable vulnerable feature (if feature not used)
- Input validation (prevent exploitation)
- WAF rule (block exploit attempts)
- Document as technical debt (monitor for fix)

**Path D: Accept Risk (if no other option)**
- Document vulnerability
- Document why not fixed (no fix available, not exploitable, etc.)
- CISO approval required
- Monitor for fix availability

**Step 3: Deploy Fix**
- Deploy to test environment
- Run regression tests + security tests
- Deploy to production
- Verify vulnerability resolved (re-scan)

---

## 6. Interactive Application Security Testing (IAST)

### 6.1 IAST Overview

**What is IAST:**
- Agents/sensors inside running application
- Monitors application behavior at runtime
- Detects vulnerabilities during functional testing
- Combines aspects of SAST (code analysis) and DAST (runtime testing)

**Benefits:**
- Low false positive rate (observes actual execution)
- Accurate findings (sees real vulnerabilities)
- Developer-friendly (points to exact code location)

**Drawbacks:**
- Requires agent installation (performance overhead)
- Only detects vulnerabilities in executed code paths
- More expensive than SAST/DAST

**When to Use IAST:**
- High-risk applications (where accuracy critical)
- Applications with complex business logic
- When SAST/DAST false positives are too high

### 6.2 IAST Tool Options

| Tool | Type | Languages | Integration | Cost |
|------|------|-----------|-------------|------|
| **Contrast Security** | Commercial | Java, .NET, Node.js, Python, Ruby | Runtime agent | Paid |
| **Checkmarx CxIAST** | Commercial | Java, .NET | Runtime agent | Paid |
| **Hdiv** | Commercial | Java | Runtime agent | Paid |
| **Seeker** (Synopsys) | Commercial | Java, .NET | Runtime agent | Paid |

**Recommendation:** IAST is optional for most organizations. Consider for high-risk applications where accuracy is critical.

### 6.3 IAST Deployment (Example: Contrast Security)

**Step 1: Install Agent**

**Java Application:**
```bash
# Download Contrast agent JAR
# Add to application startup
java -javaagent:contrast.jar \
  -Dcontrast.api.key=$API_KEY \
  -Dcontrast.user.name=$USERNAME \
  -Dcontrast.service.key=$SERVICE_KEY \
  -jar my-application.jar
```

**.NET Application:**
```powershell
# Install Contrast agent via NuGet
Install-Package Contrast.NET

# Configure in web.config
<configuration>
  <appSettings>
    <add key="contrast.api.key" value="YOUR_API_KEY"/>
  </appSettings>
</configuration>
```

**Step 2: Run Functional Tests**
- Execute normal QA tests (manual or automated)
- IAST agent observes application behavior
- Detects vulnerabilities in executed code paths

**Step 3: Review Findings**
- Contrast console shows detected vulnerabilities
- Findings include exact code location (file, line number)
- Triage and remediate similar to SAST findings

---

## 7. Penetration Testing

### 7.1 Penetration Testing Program

**Penetration Testing Frequency:**

| Application Risk | Frequency | Scope |
|-----------------|-----------|-------|
| **High Risk** | Annually + per major release | Full application, infrastructure, APIs |
| **Medium Risk** | Every 2 years | Application and APIs |
| **Low Risk** | Every 3 years or on significant changes | Targeted testing |

**Internet-Facing vs. Internal:**
- Internet-facing applications: More frequent (higher threat)
- Internal applications: Less frequent (lower threat, but don't ignore)

### 7.2 Penetration Testing Scope Definition

**Scope Document (Pentest Statement of Work):**

```markdown
# Penetration Testing Scope - [Application Name]

## 1. In-Scope
### Applications
- Customer Portal (https://portal.example.com)
- Customer API (https://api.example.com)

### Infrastructure
- Web servers (IPs: 203.0.113.10-15)
- API servers (IPs: 203.0.113.20-25)

### User Access Levels
- Unauthenticated user
- Authenticated user (regular)
- Authenticated user (admin) - provided credentials

### Testing Types
- Web application testing (OWASP Testing Guide)
- API testing (REST API security)
- Infrastructure testing (network, OS hardening)

## 2. Out-of-Scope
- Production database servers (no direct access)
- Third-party integrations (e.g., payment gateway)
- Physical security testing
- Social engineering attacks
- Denial of Service (DoS) attacks

## 3. Testing Methodology
- OWASP Testing Guide v4.0
- PTES (Penetration Testing Execution Standard)

## 4. Rules of Engagement
- Testing window: [Dates/times - e.g., Mon-Fri 9 AM - 5 PM]
- Emergency contact: [Name, phone, email]
- Data handling: No exfiltration of real customer data
- Reporting: Draft report within 2 weeks, final within 3 weeks

## 5. Credentials Provided
- Test user account: testuser@example.com (regular user)
- Admin account: admin-test@example.com (admin privileges)
- API key: [Provided separately]

## 6. Expected Deliverables
- Executive summary
- Detailed findings (severity, exploitability, remediation)
- Proof-of-concept exploits (where applicable)
- Remediation timeline recommendations
```

### 7.3 Internal vs. External Penetration Testing

**Internal Penetration Testing:**
- **Who:** Internal security team or dedicated pentester
- **Pros:** Continuous availability, lower cost, organization knowledge
- **Cons:** May lack objectivity, may lack advanced skills

**External Penetration Testing:**
- **Who:** Third-party security consultancy
- **Pros:** Objective, advanced skills, attacker perspective
- **Cons:** Higher cost, less frequent, learning curve for organization

**Recommendation:** 
- **High-risk applications:** External pentesting (annually)
- **Medium-risk applications:** Internal pentesting (with external validation every 2 years)
- **Low-risk applications:** Internal pentesting only

### 7.4 Penetration Testing Execution

**Penetration Testing Phases:**

**Phase 1: Reconnaissance (1-2 days)**
- Information gathering (public sources)
- Target enumeration (domains, IPs, technologies)
- Attack surface mapping

**Phase 2: Vulnerability Identification (2-3 days)**
- Automated scanning (Nessus, Burp Suite)
- Manual testing (OWASP Top 10)
- Vulnerability validation

**Phase 3: Exploitation (3-5 days)**
- Attempt to exploit identified vulnerabilities
- Gain unauthorized access
- Pivot to other systems (lateral movement)
- Privilege escalation

**Phase 4: Post-Exploitation (1-2 days)**
- Maintain access (persistence)
- Data access attempts (what data can attacker access?)
- Document impact

**Phase 5: Reporting (3-5 days)**
- Document findings
- Create proof-of-concept exploits
- Remediation recommendations
- Executive summary

**Total Timeline:** 2-3 weeks (depending on scope)

### 7.5 Penetration Testing Report Review

**Pentest Report Sections:**

**1. Executive Summary**
- High-level findings
- Overall security posture
- Critical risks

**2. Detailed Findings**
- Per vulnerability:
  - Title and description
  - Severity (Critical, High, Medium, Low, Informational)
  - CVSS score
  - Affected systems/URLs
  - Steps to reproduce
  - Proof-of-concept (if applicable)
  - Impact (what can attacker do?)
  - Remediation recommendation

**3. Appendices**
- Scope and methodology
- Tools used
- Raw scan results

**Remediation Process:**

**Step 1: Findings Review Meeting**
- Security team + Development team + Pentesters
- Review each finding
- Clarify questions
- Validate findings (confirm exploitability)

**Step 2: Remediation Planning**
- Prioritize findings (Critical → High → Medium → Low)
- Assign to developers
- Create Jira/ADO tickets
- Set SLAs (Critical: 7 days, High: 30 days, etc.)

**Step 3: Remediation Execution**
- Developers fix vulnerabilities
- Deploy fixes to test environment

**Step 4: Retest**
- Pentesters retest fixed vulnerabilities
- Verify remediation effective
- Issue final "Remediation Verified" report

---

## 8. Security Acceptance Testing

### 8.1 Security Acceptance Testing Overview

**Purpose:** Verify that security requirements (from IMP-S1) are implemented correctly before production deployment.

**When:** During User Acceptance Testing (UAT) phase, before production.

**Who:** QA Team + Security Champion

### 8.2 Security Test Case Development

**Security Test Cases Derived from Requirements:**

For each security requirement (SEC-REQ-XXX from IMP-S1), create corresponding test case(s).

**Example Mapping:**

| Security Requirement | Test Case ID | Test Case Description |
|---------------------|--------------|----------------------|
| SEC-REQ-001: MFA required | TC-SEC-001 | Verify that login requires MFA after username/password |
| SEC-REQ-002: Password complexity | TC-SEC-002 | Attempt to set weak password (must fail) |
| SEC-REQ-011: Server-side authorization | TC-SEC-011 | Attempt to access admin page as regular user (must fail) |
| SEC-REQ-020: Input validation | TC-SEC-020 | Submit SQL injection payload in form (must be rejected) |
| SEC-REQ-031: Encryption at rest | TC-SEC-031 | Verify database encryption enabled |

**Security Test Case Template:**

```markdown
## Test Case TC-SEC-001: Multi-Factor Authentication Required

**Requirement:** SEC-REQ-001 (MFA required for all users)

**Preconditions:**
- User has valid username and password
- User has MFA enrolled (TOTP app or SMS)

**Test Steps:**
1. Navigate to login page
2. Enter valid username and password
3. Click "Login"
4. Observe MFA prompt
5. Enter invalid MFA code
6. Observe error message
7. Enter valid MFA code
8. Observe successful login

**Expected Results:**
- Step 4: MFA prompt displayed (TOTP or SMS)
- Step 6: Login denied with error "Invalid MFA code"
- Step 8: Login successful, user redirected to dashboard

**Actual Results:** [PASS/FAIL]

**Pass Criteria:**
- MFA prompt displayed after username/password
- Invalid MFA code rejected
- Valid MFA code grants access

**Notes:**
[Any observations]
```

### 8.3 Security Acceptance Test Execution

**Test Execution Process:**

**Step 1: Prepare Test Environment**
- Deploy application to test environment
- Configure test data (test users with known credentials)
- Ensure test environment mirrors production (configuration, integrations)

**Step 2: Execute Security Test Cases**
- QA tester executes test cases
- Security Champion observes (spot-checks)
- Document results (Pass/Fail)

**Step 3: Document Failures**
- Any failed test → create bug ticket
- Assign to developer
- Block production deployment until resolved

**Step 4: Retest After Fixes**
- Retest failed cases after fixes deployed
- Verify all tests pass

**Step 5: Security Sign-Off**
- Security Champion signs off (approves for production)
- Document sign-off in release notes

### 8.4 Automated Security Acceptance Testing

**Integration with Test Automation:**

Security test cases can be automated (if using test automation framework like Selenium, Cypress, etc.).

**Example: Selenium Security Test (Java)**

```java
@Test
public void testMFARequired() {
    // SEC-REQ-001: MFA required
    driver.get("https://test.example.com/login");
    
    // Enter valid credentials
    driver.findElement(By.id("username")).sendKeys("testuser@example.com");
    driver.findElement(By.id("password")).sendKeys("ValidPassword123!");
    driver.findElement(By.id("login-button")).click();
    
    // Verify MFA prompt appears
    WebElement mfaPrompt = driver.findElement(By.id("mfa-code-input"));
    assertTrue(mfaPrompt.isDisplayed(), "MFA prompt should be displayed");
    
    // Enter invalid MFA code
    mfaPrompt.sendKeys("000000");
    driver.findElement(By.id("mfa-submit")).click();
    
    // Verify error message
    String errorMessage = driver.findElement(By.id("error")).getText();
    assertEquals("Invalid MFA code", errorMessage);
    
    // Enter valid MFA code (from TOTP secret)
    String validCode = generateTOTP(TEST_USER_TOTP_SECRET);
    mfaPrompt.clear();
    mfaPrompt.sendKeys(validCode);
    driver.findElement(By.id("mfa-submit")).click();
    
    // Verify successful login
    assertTrue(driver.getCurrentUrl().contains("/dashboard"), "Should redirect to dashboard");
}
```

---

## 9. Security Testing Results Management

### 9.1 Centralized Vulnerability Management

**Challenge:** Multiple testing tools (SAST, DAST, SCA, pentest) generate findings in different formats.

**Solution:** Centralized vulnerability management platform.

**Options:**

| Platform | Type | Features | Cost |
|----------|------|----------|------|
| **DefectDojo** | Open-source | Vulnerability aggregation, reporting | Free |
| **ThreadFix** | Commercial | Vulnerability deduplication, workflow | Paid |
| **Jira** | Issue tracker | Flexible, customizable | Paid |
| **Azure DevOps** | Issue tracker | Integrated with dev workflow | Paid |

**Recommendation:** **DefectDojo** (free, purpose-built) or **Jira** (if already using for bug tracking).

### 9.2 DefectDojo Setup (Centralized Vulnerability Management)

**Installation:**

```bash
# Docker deployment
git clone https://github.com/DefectDojo/django-DefectDojo
cd django-DefectDojo
docker-compose up -d
```

**Configuration:**

1. **Create Products:**
   - Product = Application
   - Example: "Customer Portal", "API Gateway"

2. **Create Engagements:**
   - Engagement = Testing activity
   - Example: "Q1 2025 Penetration Test", "Sprint 23 SAST Scan"

3. **Import Scan Results:**
   - Upload SAST/DAST/SCA reports
   - DefectDojo parses findings
   - Deduplicates findings across scans

4. **Manage Findings:**
   - Triage findings (true positive, false positive, accepted risk)
   - Assign to developers
   - Track remediation

**Automated Import (CI/CD):**

```bash
# Upload SAST results to DefectDojo
curl -X POST "https://defectdojo.example.com/api/v2/import-scan/" \
  -H "Authorization: Token $DEFECTDOJO_API_KEY" \
  -F "scan_type=SonarQube Scan" \
  -F "file=@sonar-report.json" \
  -F "engagement=1" \
  -F "verified=true"
```

### 9.3 Vulnerability Remediation Workflow

**Standard Workflow:**

**1. Discovery**
- Vulnerability detected by tool (SAST, DAST, SCA, pentest)
- Finding imported to DefectDojo or Jira

**2. Triage**
- Security team or Security Champion reviews
- Validate: True positive, false positive, duplicate
- Assign severity: Critical, High, Medium, Low

**3. Assignment**
- Assign to developer or team
- Set SLA based on severity:
  - Critical: 7 days
  - High: 30 days
  - Medium: 90 days
  - Low: Best effort

**4. Remediation**
- Developer fixes vulnerability
- Developer documents fix in ticket
- Developer deploys fix to test environment

**5. Verification**
- Re-scan (SAST/DAST) or manual retest
- Verify vulnerability resolved
- Close ticket if resolved

**6. Deployment**
- Deploy fix to production
- Update vulnerability management system (mark as "Fixed in Production")

---

## 10. Assessment Workbook Specifications

### 10.1 Assessment Workbook 3: Security Testing Results

**Purpose:** Track security testing execution and results across all testing types.

**Workbook Sheets:**

**Sheet 1: Instructions & Legend**
- Workbook purpose and scope
- How to use
- Status legend

**Sheet 2: Security_Testing_Coverage**
- Application name
- SAST coverage (% of code scanned)
- DAST coverage (last scan date, frequency)
- SCA coverage (% of dependencies scanned)
- Penetration testing status (last test date, next scheduled)
- Security acceptance testing status
- Overall testing coverage score

**Sheet 3: SAST_Scan_Results**
- Application name
- Last scan date
- Critical findings count
- High findings count
- Medium findings count
- Low findings count
- Total findings
- Trend (vs. previous scan)
- Remediation rate (% fixed within SLA)

**Sheet 4: DAST_Scan_Results**
- Application name
- Last scan date
- Scan type (Baseline, Full, API)
- Critical findings count
- High findings count
- Medium findings count
- Low findings count
- Remediation status

**Sheet 5: SCA_Scan_Results**
- Application name
- Last scan date
- Vulnerable dependencies count (by severity)
- Outdated dependencies count
- License compliance issues
- Remediation status

**Sheet 6: Penetration_Testing_Results**
- Application name
- Pentest date
- Pentester (internal/external)
- Critical findings count
- High findings count
- Medium findings count
- Low findings count
- Retest date
- Retest results (findings resolved)

**Sheet 7: Security_Acceptance_Testing**
- Application name
- Release version
- Security test cases total
- Security test cases passed
- Security test cases failed
- Pass rate (%)
- Security sign-off (Approved/Pending/Rejected)

**Sheet 8: Compliance_Summary**
- Overall testing compliance dashboard
- Testing coverage by application
- Findings by severity
- Remediation SLA compliance
- Gap analysis

**Sheet 9: Evidence_Register**
- Evidence type (SAST report, DAST report, Pentest report)
- Application name
- Document location
- Owner
- Status

**Sheet 10: Approval_Sign_Off**
- Assessment information
- Approval sign-off

### 10.2 Assessment Workbook 4: Vulnerability Remediation Tracking

**Purpose:** Track open vulnerabilities and remediation compliance.

**Workbook Sheets:**

**Sheet 1: Instructions & Legend**

**Sheet 2: Open_Vulnerabilities_Inventory**
- Vulnerability ID
- Application name
- Vulnerability type (SQL Injection, XSS, etc.)
- Severity (Critical, High, Medium, Low)
- Source (SAST, DAST, SCA, Pentest)
- Discovered date
- Age (days since discovery)
- SLA due date
- Days until due (or overdue)
- Status (Open, In Progress, Fixed, Accepted Risk)
- Owner

**Sheet 3: Remediation_SLA_Compliance**
- Severity level
- SLA (days)
- Open vulnerabilities count
- Vulnerabilities within SLA
- Vulnerabilities overdue
- SLA compliance rate (%)

**Sheet 4: Vulnerability_Trends**
- Month
- Vulnerabilities opened (by severity)
- Vulnerabilities closed (by severity)
- Net change
- Trend chart

**Sheet 5: Security_Technical_Debt**
- Vulnerability ID
- Application name
- Risk acceptance rationale
- Accepted date
- Accepted by (CISO/Security Architect)
- Review date (annual review)
- Mitigating controls

**Sheet 6: Compliance_Summary**
- Overall remediation compliance
- SLA compliance by severity
- Vulnerability aging distribution
- Top vulnerable applications

**Sheet 7: Evidence_Register**

**Sheet 8: Approval_Sign_Off**

---

## 11. Common Pitfalls and Solutions

### 11.1 Security Testing Pitfalls

**Pitfall 1: Testing Only in Production**
❌ **Problem:** Vulnerabilities found too late (expensive to fix)
✅ **Solution:** Shift left - test early and often (SAST per commit, DAST in test environment)

**Pitfall 2: Too Many False Positives**
❌ **Problem:** Developers ignore findings (alert fatigue)
✅ **Solution:** Tune tools, suppress false positives, start with critical/high only

**Pitfall 3: No Remediation Workflow**
❌ **Problem:** Findings detected but never fixed
✅ **Solution:** Integrate with Jira/ADO, assign SLAs, track compliance

---

## 12. Conclusion

This implementation guide provides comprehensive procedures for security testing throughout the SDLC.

**Key Takeaways:**
- Layered testing approach (SAST, DAST, SCA, pentesting)
- Test early and often (shift left)
- Automate testing (CI/CD integration)
- Track remediation with SLAs
- Centralize vulnerability management

**Success Factors:**
- Tool automation (fast feedback)
- Clear remediation workflows
- SLA enforcement
- Metrics-driven improvement

**Next Steps:**
1. Deploy DAST tools
2. Establish pentest program
3. Implement security acceptance testing
4. Centralize vulnerability management
5. Track metrics and improve

For questions or support, contact the Security Team.

---

**Document End**
