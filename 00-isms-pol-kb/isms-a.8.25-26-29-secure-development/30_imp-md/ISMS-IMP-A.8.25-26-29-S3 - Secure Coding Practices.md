# ISMS-IMP-A.8.25-26-29-S3
## Secure Coding Practices - Implementation Guide
### ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle) & A.8.28 (Secure Coding)

---

## Document Control

**Document ID:** ISMS-IMP-A.8.25-26-29-S3  
**Implementation Area:** Secure Coding Standards and Practices  
**Related Policies:** 
- ISMS-POL-A.8.25-26-29-S3 (Secure Development Lifecycle - A.8.25)
- ISMS-POL-A.8.28 (Secure Coding - if applicable)  
**Purpose:** Step-by-step implementation guidance for establishing and enforcing secure coding standards, code review processes, and security tool deployment

**Regulatory Context:**
- ISO/IEC 27001:2022 Control A.8.25 (Secure Development Lifecycle)
- ISO/IEC 27001:2022 Control A.8.28 (Secure Coding)
- OWASP Secure Coding Practices
- CWE/SANS Top 25 Most Dangerous Software Weaknesses
- See ISMS-POL-00 for complete regulatory applicability framework

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides practical, step-by-step procedures for establishing secure coding practices as defined in POL-S3 Section 2.2. It covers:

- Secure coding standards adoption and customization
- Code review process implementation (peer review + security-focused review)
- Security tool deployment and integration (SAST, SCA, secret scanning)
- IDE security plugin configuration
- Security defect management workflows

**Note:** This guide focuses on the HOW of secure coding - the practical implementation. For WHAT security requirements applications must meet, see IMP-S1 (Security Requirements). For WHERE security fits in SDLC, see IMP-S2 (SDLC Integration).

### 1.2 Target Audience

- **Primary:** Development Leads, Senior Developers, Security Champions
- **Supporting:** All Developers, DevOps Engineers, QA Engineers
- **Oversight:** Security Architects, CISO, Engineering Leadership

### 1.3 Prerequisites

**Before implementing secure coding practices:**
- [ ] Read ISMS-POL-A.8.25-26-29-S3 Section 2.2 (Secure Coding Standards)
- [ ] Developer security training completed (IMP-S2 Section 5)
- [ ] SDLC security integration in place (IMP-S2)
- [ ] Code repository infrastructure available (Git, GitLab, GitHub, Azure DevOps, etc.)
- [ ] CI/CD pipeline established

### 1.4 Process Dependencies

**Integrates with:**
- Security requirements (IMP-S1) - defines WHAT to build securely
- SDLC integration (IMP-S2) - defines WHERE secure coding fits in development
- Security testing (IMP-S4) - verifies that secure coding standards are met
- Source code access control (ISMS-POL-A.8.4) - controls WHO can access code

---

## 2. Secure Coding Standards Implementation

### 2.1 Standards Selection and Adoption

**Step 1: Select Base Secure Coding Standard**

**Recommended Approach:** Adopt industry-standard frameworks as foundation, then customize.

**Primary Standard Options:**

**Option A: OWASP Secure Coding Practices (Recommended for Most)**
- **Source:** https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- **Pros:** Free, comprehensive, language-agnostic, regularly updated
- **Cons:** High-level (needs language-specific supplements)
- **Best For:** Web applications, API development, most organizations

**Option B: CWE/SANS Top 25 (Vulnerability-Focused)**
- **Source:** https://cwe.mitre.org/top25/
- **Pros:** Focuses on most dangerous weaknesses, prioritized by impact
- **Cons:** Not comprehensive (only top 25)
- **Best For:** Organizations prioritizing highest-impact vulnerabilities

**Option C: SEI CERT Coding Standards (Language-Specific)**
- **Source:** https://wiki.sei.cmu.edu/confluence/display/seccode
- **Pros:** Very detailed, language-specific (C, C++, Java, Perl, Android)
- **Cons:** Highly technical, lengthy, not all languages covered
- **Best For:** Organizations developing in C/C++/Java with high security requirements

**Option D: Language/Framework-Specific Standards**
- Java: Oracle Secure Coding Guidelines for Java SE
- Python: Python Security Best Practices (OWASP)
- JavaScript/Node.js: Node.js Security Best Practices
- .NET: Microsoft Secure Coding Guidelines
- Go: Go Security Guide

**Recommended Hybrid Approach:**
```
Base Standard: OWASP Secure Coding Practices
+ Language-Specific Supplements (per language used)
+ Framework-Specific Guidance (Spring, Django, React, etc.)
= Organization's Secure Coding Standard
```

**Step 2: Customize Standard for Organization**

**Customization Checklist:**
- [ ] Remove sections not applicable (e.g., mobile security if no mobile apps)
- [ ] Add organization-specific requirements (e.g., mandatory MFA, specific encryption algorithms)
- [ ] Adjust for technology stack (specific frameworks, libraries)
- [ ] Incorporate regulatory requirements (GDPR, PCI DSS, HIPAA)
- [ ] Define severity ratings for violations (critical, high, medium, low)
- [ ] Add code examples (both vulnerable and secure) in languages used

**Example Customization:**

Base OWASP Standard says:
> "Use cryptography to protect sensitive data in transit and at rest"

Organization-Specific Version:
> **CRYPTO-001 (CRITICAL):** All sensitive data MUST be encrypted in transit using TLS 1.2 or higher. Sensitive data at rest MUST be encrypted using AES-256. Approved encryption libraries: [List specific libraries for Java, Python, etc.]. Never implement custom encryption.
> 
> **Example (Java - CORRECT):**
> ```java
> // Encrypt data at rest using AES-256
> Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
> SecretKeySpec secretKey = new SecretKeySpec(keyBytes, "AES");
> GCMParameterSpec gcmSpec = new GCMParameterSpec(128, iv);
> cipher.init(Cipher.ENCRYPT_MODE, secretKey, gcmSpec);
> byte[] encrypted = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
> ```

**Step 3: Document and Publish Standard**

**Secure Coding Standard Document Structure:**

```markdown
# [Organization] Secure Coding Standard v1.0

## 1. Introduction
- Purpose and scope
- Applicability (all applications, specific types)
- Standard version and change history

## 2. General Security Principles
- Least privilege
- Defense in depth
- Fail secure
- Keep it simple
- Trust nothing (zero trust)

## 3. Input Validation
- INPUT-001: Validate all user input (allowlist preferred)
- INPUT-002: Sanitize special characters
- INPUT-003: Validate file uploads
- [Code examples for each rule]

## 4. Output Encoding
- OUTPUT-001: Context-aware output encoding (HTML, JavaScript, URL, CSS)
- OUTPUT-002: Content Security Policy (CSP)
- [Code examples]

## 5. Authentication and Password Management
- AUTH-001: Use strong password hashing (bcrypt, Argon2, PBKDF2)
- AUTH-002: Implement multi-factor authentication (MFA)
- AUTH-003: Secure password reset flows
- [Code examples]

## 6. Session Management
- SESSION-001: Use cryptographically random session tokens
- SESSION-002: Set HttpOnly, Secure, SameSite flags
- SESSION-003: Implement session timeout (idle and absolute)
- [Code examples]

## 7. Access Control
- ACCESS-001: Implement role-based access control (RBAC)
- ACCESS-002: Enforce authorization on every request (server-side)
- ACCESS-003: No IDOR vulnerabilities (object-level authorization)
- [Code examples]

## 8. Cryptographic Practices
- CRYPTO-001: TLS 1.2+ for data in transit
- CRYPTO-002: AES-256 for data at rest
- CRYPTO-003: Use approved libraries only (no custom crypto)
- CRYPTO-004: Secure key management (KMS, HSM, vault)
- [Code examples]

## 9. Error Handling and Logging
- ERROR-001: Generic error messages to users (no stack traces)
- ERROR-002: Detailed errors logged server-side
- LOG-001: Log security events (auth, authz failures, input validation)
- LOG-002: Do NOT log sensitive data (passwords, tokens, PII)
- [Code examples]

## 10. Data Protection
- DATA-001: Minimize data collection (only what's needed)
- DATA-002: Data retention policies enforced
- DATA-003: Secure data deletion (right to erasure)
- [Code examples]

## 11. Communication Security
- COMM-001: Use HTTPS for all web traffic
- COMM-002: Validate SSL/TLS certificates
- COMM-003: API authentication (OAuth 2.0, API keys)
- [Code examples]

## 12. Database Security
- DB-001: Use parameterized queries (no string concatenation)
- DB-002: Least privilege database accounts
- DB-003: Encrypt sensitive database fields
- [Code examples]

## 13. File Management
- FILE-001: Validate file types (magic bytes, not extension)
- FILE-002: Limit file upload sizes
- FILE-003: Store uploads outside web root
- FILE-004: Scan uploads for malware
- [Code examples]

## 14. Memory Management (C/C++)
- MEM-001: Avoid buffer overflows (use safe functions)
- MEM-002: Free allocated memory
- MEM-003: Avoid use-after-free
- [Code examples - if applicable]

## 15. Third-Party Components
- THIRD-001: Maintain component inventory
- THIRD-002: No components with known high/critical vulnerabilities
- THIRD-003: Validate component licenses
- [Code examples]

## Appendix A: Language-Specific Guidelines
- Java Secure Coding
- Python Secure Coding
- JavaScript Secure Coding
- [Other languages]

## Appendix B: Framework-Specific Guidelines
- Spring Security (Java)
- Django Security (Python)
- Express.js Security (Node.js)
- [Other frameworks]

## Appendix C: OWASP Top 10 Mapping
[Map each OWASP Top 10 item to standard rules]

## Appendix D: Severity Ratings
- Critical: Immediate exploitation possible, high impact
- High: Exploitation likely, significant impact
- Medium: Exploitation requires conditions, moderate impact
- Low: Difficult to exploit or minimal impact
```

**Publication:**
- Store in central documentation repository (Confluence, SharePoint, GitHub Wiki)
- Make easily accessible to all developers
- Provide permalink (stable URL)
- Include in developer onboarding

**Step 4: Communicate Standard to Developers**

**Communication Plan:**
- **Announcement:** Email to all developers with standard link
- **Training Session:** 2-hour workshop explaining key rules (see IMP-S2 Section 5)
- **Integration:** Reference in code review guidelines
- **Tooling:** Configure SAST tools to check standard compliance

### 2.2 Language-Specific Secure Coding Guidelines

**Purpose:** Provide actionable guidance for developers in their specific programming languages.

**For Each Language Used:**

#### 2.2.1 Java Secure Coding

**Key Vulnerabilities in Java:**
- Insecure deserialization
- SQL injection (if not using parameterized queries)
- XML external entity (XXE) injection
- Path traversal
- Cross-site scripting (XSS) in JSP/Spring templates

**Critical Security Rules:**

**JAVA-001: Use Parameterized Queries (Prevent SQL Injection)**
```java
// ❌ WRONG - Vulnerable to SQL injection
String query = "SELECT * FROM users WHERE username = '" + userInput + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);

// ✅ CORRECT - Parameterized query
String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, userInput);
ResultSet rs = pstmt.executeQuery();
```

**JAVA-002: Disable XXE Processing (Prevent XXE Attacks)**
```java
// ✅ CORRECT - Disable external entities
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(inputStream);
```

**JAVA-003: Secure Deserialization (Prevent Remote Code Execution)**
```java
// ❌ WRONG - Unsafe deserialization
ObjectInputStream ois = new ObjectInputStream(untrustedInput);
Object obj = ois.readObject(); // Can execute arbitrary code

// ✅ CORRECT - Use serialization filters (Java 9+)
ObjectInputStream ois = new ObjectInputStream(untrustedInput);
ois.setObjectInputFilter(ObjectInputFilter.Config.createFilter(
    "com.example.SafeClass;!*")); // Only allow SafeClass
Object obj = ois.readObject();

// ✅ BETTER - Avoid deserialization, use JSON instead
ObjectMapper mapper = new ObjectMapper();
SafeClass obj = mapper.readValue(jsonInput, SafeClass.class);
```

**JAVA-004: Output Encoding (Prevent XSS)**
```java
// ❌ WRONG - No encoding
out.println("<div>" + userInput + "</div>");

// ✅ CORRECT - HTML encoding
import org.apache.commons.text.StringEscapeUtils;
out.println("<div>" + StringEscapeUtils.escapeHtml4(userInput) + "</div>");

// ✅ CORRECT - In Spring templates (Thymeleaf)
// Use th:text (auto-escapes) instead of th:utext (raw HTML)
<div th:text="${userInput}"></div>
```

**JAVA-005: Secure Random Number Generation**
```java
// ❌ WRONG - Predictable random
Random random = new Random();
String token = String.valueOf(random.nextLong());

// ✅ CORRECT - Cryptographically secure random
SecureRandom secureRandom = new SecureRandom();
byte[] tokenBytes = new byte[32];
secureRandom.nextBytes(tokenBytes);
String token = Base64.getEncoder().encodeToString(tokenBytes);
```

**Framework-Specific: Spring Security**
```java
// ✅ Enable CSRF protection (default in Spring Security)
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .csrf().and() // CSRF enabled (default)
            .headers()
                .contentSecurityPolicy("default-src 'self'").and()
                .frameOptions().deny();
    }
}
```

#### 2.2.2 Python Secure Coding

**Key Vulnerabilities in Python:**
- SQL injection
- Command injection (subprocess, os.system)
- SSTI (Server-Side Template Injection) in Flask/Jinja2
- Insecure deserialization (pickle)
- Path traversal

**Critical Security Rules:**

**PY-001: Use Parameterized Queries**
```python
# ❌ WRONG - SQL injection vulnerability
cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")

# ✅ CORRECT - Parameterized query
cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))

# ✅ CORRECT - Django ORM (automatically parameterized)
User.objects.filter(username=user_input)
```

**PY-002: Avoid Command Injection**
```python
# ❌ WRONG - Command injection via shell=True
import subprocess
subprocess.run(f"ls {user_input}", shell=True)

# ✅ CORRECT - No shell, pass as list
subprocess.run(["ls", user_input], shell=False)

# ✅ BETTER - Validate input, use allowlist
allowed_dirs = ['/home', '/var/log']
if user_input in allowed_dirs:
    subprocess.run(["ls", user_input], shell=False)
```

**PY-003: Secure Template Rendering (Prevent SSTI)**
```python
# ❌ WRONG - Server-Side Template Injection (Flask)
from flask import render_template_string
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template_string(f"<h1>Hello {name}</h1>")  # SSTI!

# ✅ CORRECT - Use templates with auto-escaping
from flask import render_template
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)  # Auto-escaped

# hello.html template
# <h1>Hello {{ name }}</h1>  <!-- Jinja2 auto-escapes by default -->
```

**PY-004: Never Use pickle with Untrusted Data**
```python
# ❌ WRONG - Pickle can execute arbitrary code
import pickle
obj = pickle.loads(untrusted_data)  # DANGER!

# ✅ CORRECT - Use JSON instead
import json
obj = json.loads(untrusted_data)
```

**PY-005: Secure Password Hashing**
```python
# ❌ WRONG - MD5/SHA1 are not suitable for passwords
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()

# ✅ CORRECT - Use bcrypt, Argon2, or PBKDF2
from werkzeug.security import generate_password_hash, check_password_hash

# Hash password
password_hash = generate_password_hash(password, method='pbkdf2:sha256')

# Verify password
is_valid = check_password_hash(password_hash, password)
```

**Framework-Specific: Django Security**
```python
# ✅ Django security settings (settings.py)
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # Never hardcode!
DEBUG = False  # Always False in production
ALLOWED_HOSTS = ['example.com']  # Restrict hosts

# Security middleware (enabled by default)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # ...
]

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True  # HTTPS only
SESSION_COOKIE_SECURE = True  # HTTPS only
```

#### 2.2.3 JavaScript/Node.js Secure Coding

**Key Vulnerabilities in JavaScript:**
- Cross-site scripting (XSS)
- Prototype pollution
- Regular expression denial of service (ReDoS)
- NoSQL injection (MongoDB)
- Command injection

**Critical Security Rules:**

**JS-001: Prevent XSS (Client-Side)**
```javascript
// ❌ WRONG - innerHTML with user data
element.innerHTML = userInput;  // XSS!

// ✅ CORRECT - Use textContent (no HTML parsing)
element.textContent = userInput;

// ✅ CORRECT - Sanitize HTML if needed
import DOMPurify from 'dompurify';
element.innerHTML = DOMPurify.sanitize(userInput);
```

**JS-002: Prevent Prototype Pollution**
```javascript
// ❌ WRONG - Directly assigning user-controlled keys
function merge(target, source) {
    for (let key in source) {
        target[key] = source[key];  // Prototype pollution!
    }
}

// ✅ CORRECT - Check for __proto__, constructor, prototype
function merge(target, source) {
    for (let key in source) {
        if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
            continue;
        }
        if (source.hasOwnProperty(key)) {
            target[key] = source[key];
        }
    }
}

// ✅ BETTER - Use Object.assign or spread operator
const merged = { ...target, ...source };
```

**JS-003: Secure NoSQL Queries (MongoDB)**
```javascript
// ❌ WRONG - NoSQL injection
const user = await User.findOne({ username: req.body.username });

// If req.body.username = { $ne: null }, this returns first user!

// ✅ CORRECT - Validate input type
const username = String(req.body.username);  // Force to string
const user = await User.findOne({ username: username });
```

**JS-004: Avoid ReDoS (Regular Expression Denial of Service)**
```javascript
// ❌ WRONG - Catastrophic backtracking
const regex = /^(a+)+$/;
regex.test(userInput);  // ReDoS with input like "aaaaaaaaaaaaaaaaaaaaX"

// ✅ CORRECT - Avoid nested quantifiers
const regex = /^a+$/;

// ✅ CORRECT - Use regex timeout libraries (safe-regex)
import isSafeRegex from 'safe-regex';
if (!isSafeRegex(regexPattern)) {
    throw new Error('Unsafe regex pattern');
}
```

**JS-005: Secure JWT Handling**
```javascript
// ❌ WRONG - Algorithm confusion attack
const jwt = require('jsonwebtoken');
const decoded = jwt.verify(token, publicKey);  // Accepts any algorithm!

// ✅ CORRECT - Specify allowed algorithm
const decoded = jwt.verify(token, publicKey, { algorithms: ['RS256'] });
```

**Framework-Specific: Express.js Security**
```javascript
// ✅ Express security middleware
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const mongoSanitize = require('express-mongo-sanitize');

app.use(helmet());  // Security headers (CSP, X-Frame-Options, etc.)
app.use(mongoSanitize());  // Prevent NoSQL injection

// Rate limiting
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000,  // 15 minutes
    max: 100  // 100 requests per IP
});
app.use('/api/', limiter);

// CSRF protection
const csrf = require('csurf');
app.use(csrf({ cookie: true }));
```

**React-Specific: XSS Prevention**
```jsx
// ✅ React auto-escapes by default
function UserProfile({ user }) {
    return <div>{user.name}</div>;  // Auto-escaped, safe
}

// ❌ WRONG - dangerouslySetInnerHTML
function UserComment({ comment }) {
    return <div dangerouslySetInnerHTML={{ __html: comment.text }} />;  // XSS!
}

// ✅ CORRECT - Sanitize if HTML needed
import DOMPurify from 'dompurify';
function UserComment({ comment }) {
    const sanitized = DOMPurify.sanitize(comment.text);
    return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}
```

### 2.3 Secure Coding Standard Maintenance

**Annual Review Process:**
- Review OWASP Top 10 updates (if released)
- Review CWE Top 25 updates (annually)
- Analyze vulnerabilities found in organization's code (lessons learned)
- Update standard with new rules or refinements
- Communicate updates to developers

**Version Control:**
- Version numbering: Major.Minor (e.g., 1.0, 1.1, 2.0)
- Change log maintained
- Archived versions retained (reference)

---

## 3. Code Review Process Implementation

### 3.1 Code Review Process Overview

**Two-Tier Review Approach:**

**Tier 1: Peer Code Review (Every Change)**
- **Who:** Developer peer (another developer on team)
- **Focus:** Functionality, code quality, basic security (obvious issues)
- **Tool:** Pull Request (PR) / Merge Request (MR) in Git platform
- **Timeline:** Before merge to main branch

**Tier 2: Security-Focused Review (High-Risk Changes)**
- **Who:** Security Champion or Security Team
- **Focus:** Deep security analysis, threat scenarios
- **Trigger:** Changes to authentication, authorization, cryptography, input validation, high-risk applications
- **Timeline:** Before merge to main branch (for high-risk changes)

### 3.2 Peer Code Review Process

**Step 1: Developer Submits Pull Request (PR)**

**PR Requirements:**
- [ ] Code changes with clear description
- [ ] Link to user story/ticket (Jira, Azure DevOps)
- [ ] Self-review completed (developer reviews own code first)
- [ ] Unit tests written and passing
- [ ] SAST/SCA scans passing (automated in CI/CD)
- [ ] No merge conflicts

**PR Description Template:**
```markdown
## Summary
[Brief description of changes]

## Related Ticket
[JIRA-123] or [Link to ticket]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Security fix
- [ ] Refactoring
- [ ] Documentation update

## Security Considerations
[Any security-relevant changes? Authentication, authorization, input validation, cryptography, etc.]

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Checklist
- [ ] Code follows secure coding standards
- [ ] No hardcoded secrets (passwords, API keys)
- [ ] SAST scan passed
- [ ] SCA scan passed (no new high/critical vulnerabilities)
```

**Step 2: Peer Reviewer Conducts Review**

**Peer Review Checklist (General Code Quality + Basic Security):**

**Code Quality:**
- [ ] Code is readable and well-documented
- [ ] Code follows project conventions (naming, formatting)
- [ ] No code duplication (DRY principle)
- [ ] Functions/methods are appropriately sized (single responsibility)
- [ ] Error handling is appropriate

**Basic Security (Peer Reviewer):**
- [ ] No hardcoded secrets (passwords, API keys, tokens)
- [ ] No sensitive data in logs (passwords, PII, payment data)
- [ ] Input validation present (if handling user input)
- [ ] SQL queries use parameterized queries (no string concatenation)
- [ ] No obvious XSS vulnerabilities (output encoding)
- [ ] Authentication/authorization checks present (if accessing protected resources)

**Tool Support:** Use Git platform review features (GitHub PR review, GitLab MR review, Azure DevOps PR)

**Step 3: Address Review Comments**

**Developer Actions:**
- Respond to each comment (agree, disagree with rationale, or request clarification)
- Make code changes to address valid comments
- Push updates to PR branch
- Request re-review

**Step 4: Approval and Merge**

**Approval Criteria:**
- Peer reviewer approves (typically "Approve" button in Git platform)
- All CI/CD checks passing (builds, tests, SAST, SCA)
- No unresolved comments (all discussions resolved)

**Merge:**
- Developer or peer reviewer merges to main branch
- PR branch deleted (cleanup)

### 3.3 Security-Focused Code Review

**When Required:**

Security-focused review (by Security Champion or Security Team) is required for:
- [ ] Changes to authentication logic (login, logout, session management)
- [ ] Changes to authorization logic (access control, permissions)
- [ ] Changes to cryptographic functions (encryption, hashing, key management)
- [ ] Changes to input validation/sanitization (especially SQL, XSS, command injection vectors)
- [ ] New API endpoints (especially public-facing)
- [ ] Changes to security configurations (CORS, CSP, security headers)
- [ ] Third-party library additions (dependency changes)
- [ ] High-risk applications (per risk classification in IMP-S1)

**Security Review Checklist (Deep Security Analysis):**

**Authentication & Session Management:**
- [ ] Strong password requirements enforced (complexity, length)
- [ ] Passwords hashed with approved algorithm (bcrypt, Argon2, PBKDF2) - NOT MD5/SHA1
- [ ] Multi-factor authentication (MFA) implemented (if required)
- [ ] Session tokens cryptographically random (128+ bit entropy)
- [ ] Session cookies have Secure, HttpOnly, SameSite flags
- [ ] Session timeout implemented (idle timeout, absolute timeout)
- [ ] Session invalidated on logout
- [ ] No session fixation vulnerabilities
- [ ] Password reset flow secure (token expiration, no password in email)

**Authorization:**
- [ ] Authorization enforced server-side (not client-side only)
- [ ] Authorization checked on EVERY request (not just UI)
- [ ] Role-based access control (RBAC) or attribute-based access control (ABAC) implemented
- [ ] No insecure direct object reference (IDOR) vulnerabilities
- [ ] Least privilege principle applied (users have minimum necessary permissions)
- [ ] No horizontal privilege escalation (user A cannot access user B's data)
- [ ] No vertical privilege escalation (regular user cannot access admin functions)

**Input Validation:**
- [ ] ALL user inputs validated (forms, APIs, headers, cookies, query params)
- [ ] Allowlist validation preferred (validate allowed values, not block bad values)
- [ ] Input type validation (string, integer, email, URL, etc.)
- [ ] Input length validation (prevent buffer overflows, DoS)
- [ ] File upload validation (file type via magic bytes, size limits, malware scanning)
- [ ] No SQL injection vulnerabilities (parameterized queries used)
- [ ] No command injection vulnerabilities (no shell execution with user input)
- [ ] No LDAP injection vulnerabilities
- [ ] No XML injection vulnerabilities (XXE disabled)

**Output Encoding:**
- [ ] Output encoding based on context (HTML, JavaScript, URL, CSS, JSON)
- [ ] No XSS vulnerabilities (output encoded)
- [ ] Content Security Policy (CSP) implemented
- [ ] No reflected XSS (user input not echoed without encoding)
- [ ] No stored XSS (data from database encoded before display)
- [ ] No DOM-based XSS (client-side JavaScript handles user input safely)

**Cryptography:**
- [ ] TLS 1.2 or higher for data in transit (no TLS 1.0/1.1, no SSL)
- [ ] Strong cipher suites configured (no weak ciphers like RC4, DES)
- [ ] Certificate validation enabled (no self-signed certs in production)
- [ ] Sensitive data encrypted at rest (AES-256 or equivalent)
- [ ] Encryption keys managed securely (KMS, HSM, vault - not hardcoded)
- [ ] No custom cryptography (use standard libraries)
- [ ] Cryptographically secure random number generator used (SecureRandom, /dev/urandom, crypto.getRandomValues)
- [ ] No hardcoded encryption keys or secrets

**Error Handling & Logging:**
- [ ] Error messages to users are generic (no stack traces, SQL errors, file paths)
- [ ] Detailed errors logged server-side (for debugging)
- [ ] Security events logged (authentication failures, authorization failures, input validation failures)
- [ ] Logs include context (timestamp, user ID, IP address, action, resource, result)
- [ ] No sensitive data in logs (passwords, tokens, full credit card numbers, PII)
- [ ] Logs protected from tampering (write-once, centralized logging)

**Data Protection:**
- [ ] Principle of least data (only collect necessary data)
- [ ] Data classification applied (PII, sensitive, public)
- [ ] Data retention policy enforced (delete data when no longer needed)
- [ ] Sensitive data masked/redacted in non-production environments
- [ ] No sensitive data in URLs/query strings
- [ ] No sensitive data in GET requests (use POST)
- [ ] GDPR compliance (if applicable): data subject access, right to erasure

**API Security (if API changes):**
- [ ] API authentication required (OAuth 2.0, API keys, JWT)
- [ ] API rate limiting implemented (prevent DoS)
- [ ] API input validation (same as web input validation)
- [ ] API output encoding (prevent injection in API responses)
- [ ] CORS policy restrictive (not allow-all "*")
- [ ] API versioning strategy defined
- [ ] API documentation accurate (OpenAPI/Swagger)

**Third-Party Components:**
- [ ] Component inventory updated (if new dependencies)
- [ ] No known high/critical vulnerabilities in dependencies (SCA scan passed)
- [ ] Licenses compatible (no GPL if proprietary, etc.)
- [ ] Components from trusted sources (official repositories, verified publishers)

**Configuration:**
- [ ] No debug mode in production
- [ ] No default credentials (admin/admin, root/password)
- [ ] Security headers configured (X-Frame-Options, X-Content-Type-Options, CSP)
- [ ] HTTPS enforced (HTTP redirects to HTTPS)
- [ ] Unnecessary services/features disabled

**Step-by-Step Security Review:**

**Step 1: Security Champion Reviews PR**
- Security Champion receives notification (tagged in PR or automated based on changed files)
- Reviews code using Security Review Checklist
- Adds comments to PR with findings

**Step 2: Severity Assignment**
If vulnerabilities found, Security Champion assigns severity:
- **Critical:** Immediate exploitation possible, high impact (e.g., SQL injection, authentication bypass)
- **High:** Exploitation likely, significant impact (e.g., XSS, IDOR)
- **Medium:** Exploitation requires conditions, moderate impact (e.g., missing security headers)
- **Low:** Difficult to exploit or minimal impact (e.g., verbose error messages)

**Step 3: Developer Remediates**
- Developer fixes vulnerabilities
- Updates PR with fixes
- Responds to Security Champion comments

**Step 4: Security Champion Re-Reviews**
- Verifies fixes
- Approves PR if all critical/high findings resolved
- May accept medium/low findings with documented risk acceptance (time-sensitive releases)

**Step 5: Merge**
- PR merged after both peer approval AND security approval

### 3.4 Code Review Tool Configuration

**GitHub Pull Request Settings:**
```yaml
# .github/CODEOWNERS - Require Security Champion review for sensitive files
# Authentication and authorization code
/src/auth/* @security-champions
/src/permissions/* @security-champions

# Cryptography
/src/crypto/* @security-champions

# Security configurations
/config/security.* @security-champions
```

**GitLab Merge Request Approval Rules:**
- Settings → Merge Requests → Merge Request Approvals
- Rule: "Security Review Required"
  - Approvers: Security Champions group
  - Target branches: main, develop
  - Eligible approvers: 1 (at least one Security Champion must approve)
  - Files: Specify patterns for security-sensitive files

**Azure DevOps Branch Policies:**
- Repos → Branches → main → Branch Policies
- Require a minimum number of reviewers: 1
- Additional required reviewers: Add Security Champions for specific paths
- Check for linked work items: Required
- Check for comment resolution: Required

---

## 4. Security Tool Deployment

### 4.1 Static Application Security Testing (SAST)

**Purpose:** Analyze source code for security vulnerabilities without executing the code.

**SAST Tool Selection:**

**Criteria:**
- Language support (supports languages used in organization)
- Integration (IDE, CI/CD, Git platform)
- Accuracy (low false positive rate)
- Reporting (clear, actionable findings)
- Cost (free, open-source, commercial)

**SAST Tool Options:**

| Tool | Type | Languages | Integration | Cost | Notes |
|------|------|-----------|-------------|------|-------|
| **SonarQube** | Self-hosted | 25+ languages | IDE, CI/CD, Git | Free (Community) / Paid (Enterprise) | Comprehensive, widely used |
| **Snyk Code** | Cloud/Self-hosted | 10+ languages | IDE, CI/CD, Git | Free tier / Paid | Fast, low false positives |
| **Checkmarx** | Self-hosted/Cloud | 25+ languages | IDE, CI/CD, Git | Commercial | Enterprise-grade, detailed findings |
| **Semgrep** | CLI/Cloud | 20+ languages | CI/CD, Git | Open-source / Paid (Team) | Fast, customizable rules |
| **CodeQL** (GitHub) | GitHub-hosted | 10+ languages | GitHub Actions | Free (public repos) / Paid (private) | Deep semantic analysis |
| **Fortify** | Self-hosted | 25+ languages | IDE, CI/CD | Commercial | Enterprise-grade, compliance reports |

**Recommendation for Most Organizations:** Start with **SonarQube Community Edition** (free) or **Snyk Code** (free tier). Upgrade to commercial if needed.

**SAST Deployment Steps:**

**Step 1: Install and Configure SAST Tool**

**Option A: SonarQube (Self-Hosted)**

1. **Deploy SonarQube Server:**
```bash
# Docker deployment (easiest for testing)
docker run -d --name sonarqube -p 9000:9000 sonarqube:latest
```

2. **Configure SonarQube:**
- Access: http://localhost:9000
- Login: admin/admin (change password immediately)
- Create project: Projects → Create Project
- Generate token: My Account → Security → Generate Token

3. **Configure Quality Gate:**
- Quality Gates → Create
- Add conditions:
  - Security Rating: A (no vulnerabilities)
  - Coverage on New Code: 80%
  - Duplicated Lines: < 3%

**Option B: Snyk Code (Cloud-Based)**

1. **Sign Up:**
- Visit: https://snyk.io
- Sign up with GitHub/GitLab/Bitbucket account

2. **Import Repositories:**
- Snyk will scan existing repositories automatically

3. **Configure Settings:**
- Set severity thresholds (fail on high/critical)
- Configure notifications

**Step 2: Integrate SAST into CI/CD Pipeline**

**GitLab CI/CD Integration (SonarQube):**

```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - security

sonarqube_scan:
  stage: security
  image: 
    name: sonarsource/sonar-scanner-cli:latest
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"
    GIT_DEPTH: "0"
  script:
    - sonar-scanner
      -Dsonar.projectKey=$CI_PROJECT_NAME
      -Dsonar.host.url=$SONAR_HOST_URL
      -Dsonar.login=$SONAR_TOKEN
      -Dsonar.qualitygate.wait=true
  allow_failure: false  # Fail pipeline if quality gate fails
  only:
    - merge_requests
    - main
```

**GitHub Actions Integration (CodeQL):**

```yaml
# .github/workflows/codeql.yml
name: "CodeQL"

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3
    
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v2
      with:
        languages: javascript, python, java
    
    - name: Autobuild
      uses: github/codeql-action/autobuild@v2
    
    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v2
```

**Step 3: Configure SAST Rules**

**SonarQube: Activate Security Rules**
- Quality Profiles → [Language] → Activate More Rules
- Filter by: Security
- Bulk activate all security rules

**Custom Rules (if needed):**
- Rules → Create Custom Rule
- Example: Detect specific insecure patterns in organization's code

**Step 4: Baseline Scan and Triage**

**Initial Scan:**
- Run SAST on entire codebase
- Expect many findings (technical debt)

**Triage Findings:**
- **True Positives:** Real vulnerabilities → Create tickets, prioritize, fix
- **False Positives:** Not actually vulnerabilities → Mark as false positive, suppress
- **Won't Fix:** Low priority, accepted risk → Document, accept

**Prioritization:**
- **Critical/High:** Fix immediately (within 1 sprint)
- **Medium:** Fix within 2-3 sprints
- **Low:** Fix opportunistically (when touching that code anyway)

### 4.2 Software Composition Analysis (SCA)

**Purpose:** Identify vulnerabilities in third-party dependencies (libraries, frameworks).

**SCA Tool Options:**

| Tool | Type | Package Managers | Integration | Cost | Notes |
|------|------|-----------------|-------------|------|-------|
| **Snyk Open Source** | Cloud | npm, Maven, pip, etc. | CI/CD, Git, CLI | Free tier / Paid | Comprehensive, fix guidance |
| **Dependabot** (GitHub) | GitHub-hosted | Multiple | GitHub PRs | Free | Automated dependency updates |
| **OWASP Dependency-Check** | CLI | Multiple | CI/CD | Open-source | Free, self-hosted |
| **WhiteSource** (Mend) | Cloud/Self-hosted | Multiple | CI/CD, Git | Commercial | Enterprise-grade |
| **Black Duck** | Self-hosted | Multiple | CI/CD | Commercial | License compliance |

**Recommendation:** **Snyk Open Source** (best free tier) or **Dependabot** (if using GitHub).

**SCA Deployment Steps:**

**Step 1: Enable SCA Tool**

**Option A: Snyk (Multi-Platform)**

```bash
# Install Snyk CLI
npm install -g snyk

# Authenticate
snyk auth

# Test dependencies
snyk test

# Monitor project (continuous monitoring)
snyk monitor
```

**Option B: Dependabot (GitHub)**

```yaml
# .github/dependabot.yml
version: 2
updates:
  # Enable npm dependency updates
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    reviewers:
      - "security-champions"
    
  # Enable pip dependency updates
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
```

**Step 2: Integrate SCA into CI/CD**

**GitLab CI/CD (Snyk):**

```yaml
# .gitlab-ci.yml
snyk_scan:
  stage: security
  image: snyk/snyk:node
  script:
    - snyk test --severity-threshold=high
  allow_failure: false  # Fail on high/critical vulnerabilities
```

**Step 3: Configure SCA Policies**

**Vulnerability Severity Thresholds:**
- **Critical:** Block build (cannot deploy)
- **High:** Block build (must fix or risk-accept)
- **Medium:** Warning (fix within SLA, 30 days)
- **Low:** Info (fix opportunistically)

**License Policies:**
- **Prohibited Licenses:** GPL (if proprietary software), AGPL
- **Allowed Licenses:** MIT, Apache 2.0, BSD

**Step 4: Dependency Update Workflow**

**When Dependabot/Snyk Opens PR for Dependency Update:**

1. **Review PR:**
   - What changed? (dependency version bump)
   - Why? (security vulnerability fixed, feature update)
   - Breaking changes? (check changelog)

2. **Test:**
   - Run automated tests
   - Manual testing (if critical dependency)

3. **Merge:**
   - If tests pass, merge
   - If tests fail, investigate, fix tests or defer update

**Vulnerability Remediation Workflow:**

1. **Vulnerability Alert Received:**
   - Snyk/Dependabot creates issue/PR

2. **Assess:**
   - Severity? (Critical, High, Medium, Low)
   - Exploitable? (is vulnerable code path used?)
   - Fix available? (upgrade, patch, workaround)

3. **Remediate:**
   - **If fix available:** Upgrade dependency, test, deploy
   - **If no fix available:**
     - Workaround (disable vulnerable feature, input validation)
     - Monitor for fix
     - Consider alternative dependency

4. **SLA:**
   - **Critical:** 7 days
   - **High:** 30 days
   - **Medium:** 90 days
   - **Low:** Best effort

### 4.3 Secret Scanning

**Purpose:** Detect hardcoded secrets (passwords, API keys, tokens) in code before commit.

**Secret Scanning Tool Options:**

| Tool | Type | Secrets Detected | Integration | Cost | Notes |
|------|------|------------------|-------------|------|-------|
| **TruffleHog** | CLI | 700+ patterns | Pre-commit hook, CI/CD | Open-source | Entropy-based detection |
| **git-secrets** (AWS) | CLI | AWS keys, custom patterns | Pre-commit hook | Open-source | Lightweight |
| **GitGuardian** | Cloud | 350+ secret types | Git platform, CI/CD | Free tier / Paid | Comprehensive |
| **GitHub Secret Scanning** | GitHub-hosted | 200+ secret types | GitHub | Free (public) / Paid | Native GitHub |
| **Gitleaks** | CLI | Multiple patterns | Pre-commit hook, CI/CD | Open-source | Fast, configurable |

**Recommendation:** **TruffleHog** (pre-commit hook) + **GitHub Secret Scanning** or **GitGuardian** (continuous monitoring).

**Secret Scanning Deployment Steps:**

**Step 1: Deploy Pre-Commit Hook (TruffleHog)**

**Install TruffleHog:**
```bash
pip install trufflehog
```

**Create Pre-Commit Hook:**

```bash
# .git/hooks/pre-commit (in each repository)
#!/bin/bash

# Run TruffleHog on staged changes
trufflehog filesystem . --only-verified --fail --json | jq

if [ $? -ne 0 ]; then
    echo "❌ Secret detected! Commit blocked."
    echo "Remove secrets and try again."
    exit 1
fi

echo "✅ No secrets detected."
exit 0
```

**Make Hook Executable:**
```bash
chmod +x .git/hooks/pre-commit
```

**Alternative: Use pre-commit Framework**

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/trufflesecurity/trufflehog
    rev: main
    hooks:
      - id: trufflehog
        args: ['filesystem', '.', '--only-verified', '--fail']
```

**Step 2: Enable GitHub Secret Scanning (if using GitHub)**

- Settings → Security → Code security and analysis
- Enable "Secret scanning" (automatically scans for secrets)
- Enable "Secret scanning push protection" (blocks commits with secrets)

**Step 3: Configure GitGuardian (Optional, for Multi-Platform)**

1. **Sign Up:** https://www.gitguardian.com/
2. **Install GitGuardian App:** On GitHub/GitLab
3. **Configure Policies:**
   - Block commits: Yes
   - Notification: Email to security team

**Step 4: Secret Remediation Process**

**If Secret Detected:**

1. **Do NOT commit secret:**
   - Remove secret from code
   - Use environment variable or secrets manager instead

2. **If secret already committed (historical):**
   - **Rotate secret immediately** (invalidate old secret, generate new one)
   - Remove from Git history (if recently committed):
     ```bash
     # Remove file from last commit
     git reset HEAD~1
     # Remove secret, commit again
     ```
   - If deep in history, use BFG Repo-Cleaner or git-filter-repo

3. **Prevent recurrence:**
   - Use environment variables:
     ```python
     import os
     API_KEY = os.environ.get('API_KEY')
     ```
   - Use secrets manager (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault)

### 4.4 IDE Security Plugins

**Purpose:** Provide real-time security feedback to developers as they write code.

**IDE Plugin Options:**

| IDE | Plugin | Features | Cost |
|-----|--------|----------|------|
| **IntelliJ IDEA** | SonarLint | Real-time SAST, code quality | Free |
| **VS Code** | SonarLint | Real-time SAST, code quality | Free |
| **VS Code** | Snyk | Real-time SAST, SCA, secrets | Free |
| **Eclipse** | SonarLint | Real-time SAST | Free |
| **Visual Studio** | SonarLint | Real-time SAST | Free |

**Recommendation:** **SonarLint** (most comprehensive free option).

**IDE Plugin Deployment:**

**Step 1: Install Plugin**

**IntelliJ IDEA:**
- Settings → Plugins → Marketplace
- Search "SonarLint"
- Install and restart

**VS Code:**
- Extensions (Ctrl+Shift+X)
- Search "SonarLint"
- Install

**Step 2: Configure Plugin**

**Connect to SonarQube Server (Optional):**
- SonarLint Settings → Connected Mode
- Add SonarQube server URL and token
- Bind project to SonarQube project
- Sync rules and quality profile

**Step 3: Use Plugin**

- As developer types code, SonarLint highlights issues in real-time
- Hover over issue to see description and remediation guidance
- Fix issues before committing

**Developer Workflow with IDE Plugin:**
1. Write code
2. SonarLint highlights security issue (red squiggle)
3. Hover to read issue description
4. Fix issue immediately
5. Commit clean code

**Benefits:**
- Immediate feedback (seconds, not hours/days)
- Learn secure coding (explanations + remediation)
- Fewer findings in CI/CD (issues caught earlier)

---

## 5. Security Defect Management

### 5.1 Security Defect Tracking

**Integration with Issue Tracking:**
- SAST/SCA findings automatically create tickets (Jira, Azure DevOps, GitHub Issues)
- Manual security findings (from code review, pentesting) also tracked as tickets

**Security Defect Ticket Template:**

```markdown
**Title:** [SECURITY] [Severity] Brief description

**Severity:** Critical / High / Medium / Low

**Vulnerability Type:** SQL Injection / XSS / Authentication Bypass / etc.

**Affected Component:** [File path or component]

**Description:**
[Detailed description of vulnerability]

**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Observe vulnerability]

**Impact:**
[What could an attacker do? Data breach, account takeover, etc.]

**Remediation:**
[Specific steps to fix]

**References:**
- [CWE-XXX link]
- [OWASP guidance link]
- [SAST tool finding link]

**SLA:** [Due date based on severity]
```

### 5.2 Security Defect SLAs

**Service Level Agreements for Vulnerability Remediation:**

| Severity | SLA | Definition | Example |
|----------|-----|------------|---------|
| **Critical** | 7 days | Immediate exploitation, high impact | SQL injection, authentication bypass |
| **High** | 30 days | Likely exploitation, significant impact | XSS, IDOR, SSRF |
| **Medium** | 90 days | Exploitation requires conditions, moderate impact | Missing security headers, verbose errors |
| **Low** | Best effort | Difficult to exploit or minimal impact | Information disclosure (version numbers) |

**SLA Tracking:**
- Track age of open security defects (days since creation)
- Alert when approaching SLA (e.g., 5 days for critical)
- Escalate if SLA exceeded

### 5.3 Security Technical Debt Management

**Accepted Risks:**
- Some security findings may be accepted as risk (not fixed)
- Requires formal risk acceptance process:
  - Document finding
  - Document rationale for acceptance (business justification, mitigating controls)
  - CISO or Security Architect approval
  - Periodic review (annually)

**Technical Debt Tracking:**
- Maintain register of accepted security risks
- Review quarterly (are mitigations still effective? should risk be re-evaluated?)

---

## 6. Training and Documentation

### 6.1 Developer Onboarding

**New Developer Onboarding Checklist (Security):**
- [ ] Read secure coding standard
- [ ] Complete secure coding training (IMP-S2 Section 5.2)
- [ ] Install IDE security plugin (SonarLint/Snyk)
- [ ] Familiarize with code review process
- [ ] Review recent security incidents (lessons learned)
- [ ] Meet Security Champion (if on team)

### 6.2 Continuous Learning

**Monthly Security Tips:**
- Send monthly email with security tip (e.g., "Secure Coding Tip: Always validate file uploads")
- Include code examples

**Security Brown Bags:**
- Monthly 30-minute session (optional attendance)
- Topics: Recent vulnerabilities, new security tools, lessons learned

**Security Champion Meetings:**
- Monthly meeting for Security Champions
- Share experiences, discuss challenges, learn from each other

---

## 7. Metrics and Continuous Improvement

### 7.1 Secure Coding Metrics

**Track:**
- SAST findings per month (by severity)
- SCA vulnerabilities per month (by severity)
- Secret scanning incidents
- Average time to remediate (by severity)
- Code review coverage (% of code reviewed)
- Security training completion rate

**Analyze:**
- Trends (improving or degrading?)
- Common vulnerability types (focus training)
- Tool effectiveness (false positive rate)

**Improve:**
- Update secure coding standard (address common issues)
- Enhance training (focus on top vulnerability types)
- Tune tools (reduce false positives)

### 7.2 Process Improvement

**Quarterly Review:**
- Review metrics
- Collect developer feedback (is process too burdensome? are tools helpful?)
- Identify bottlenecks

**Annual Review:**
- Comprehensive assessment
- Update secure coding standard
- Evaluate tools (should we switch tools?)
- Benchmark against industry (how do we compare?)

---

## 8. Common Pitfalls and Solutions

### 8.1 Secure Coding Pitfalls

**Pitfall 1: Secure Coding Standard Too Long/Complex**
❌ **Problem:** 500-page standard, developers don't read it
✅ **Solution:** Concise standard (50-100 pages), use cheat sheets, focus on most critical rules

**Pitfall 2: No Tool Support**
❌ **Problem:** Manual enforcement of coding standards (not scalable)
✅ **Solution:** Automate with SAST tools, IDE plugins

**Pitfall 3: All or Nothing Approach**
❌ **Problem:** Block ALL findings, including low severity (developers frustrated, bypass tools)
✅ **Solution:** Start with critical/high only, expand gradually

### 8.2 Code Review Pitfalls

**Pitfall 1: Security Review Bottleneck**
❌ **Problem:** All PRs require Security Team review (Security Team overwhelmed)
✅ **Solution:** Peer review for all, security review only for high-risk changes, train Security Champions

**Pitfall 2: Rubber Stamp Reviews**
❌ **Problem:** Reviewers approve without actually reviewing
✅ **Solution:** Require comments (at least 1 comment per PR), track review quality

**Pitfall 3: No Follow-Up**
❌ **Problem:** Review comments ignored, PR merged anyway
✅ **Solution:** Require comment resolution (Git platform feature), approval from reviewer after fixes

### 8.3 Tool Deployment Pitfalls

**Pitfall 1: Alert Fatigue**
❌ **Problem:** Too many findings, developers ignore
✅ **Solution:** Tune tools (reduce false positives), baseline (suppress existing issues), focus on new issues

**Pitfall 2: No Remediation Workflow**
❌ **Problem:** Findings detected but never fixed
✅ **Solution:** Integrate with issue tracking (auto-create tickets), assign SLAs, track remediation

**Pitfall 3: Tool Sprawl**
❌ **Problem:** 10 different security tools, findings not consolidated
✅ **Solution:** Consolidate (one SAST, one SCA, one secret scanner), integrate findings into single dashboard

---

## 9. Templates and Resources

### 9.1 Available Templates

**Secure Coding Standard Template:**
- File: `Secure_Coding_Standard_Template.md`
- Location: `/templates/secure-coding/`

**Code Review Checklist:**
- File: `Code_Review_Security_Checklist.xlsx`
- Location: `/templates/code-review/`

**Security Defect Ticket Template:**
- File: `Security_Defect_Template.md`
- Location: `/templates/issue-tracking/`

### 9.2 Tool Configuration Files

**SonarQube Configuration:**
- File: `sonar-project.properties.example`
- Location: `/templates/tools/sonarqube/`

**Snyk Configuration:**
- File: `.snyk.example`
- Location: `/templates/tools/snyk/`

**Pre-Commit Hooks:**
- File: `pre-commit-secrets.sh`
- Location: `/templates/git-hooks/`

### 9.3 External Resources

**OWASP:**
- Secure Coding Practices: https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/
- Cheat Sheets: https://cheatsheetseries.owasp.org/

**Language-Specific:**
- Java: https://www.oracle.com/java/technologies/javase/seccodeguide.html
- Python: https://python.readthedocs.io/en/latest/library/security_warnings.html
- Node.js: https://nodejs.org/en/docs/guides/security/

**Tool Documentation:**
- SonarQube: https://docs.sonarqube.org/
- Snyk: https://docs.snyk.io/
- TruffleHog: https://github.com/trufflesecurity/trufflehog

---

## 10. Integration with Other ISMS Controls

**Integrates with:**
- A.8.26 (Security Requirements - IMP-S1): Requirements inform secure coding
- A.8.25 (SDLC Integration - IMP-S2): Secure coding is part of development phase
- A.8.29 (Security Testing - IMP-S4): Testing verifies secure coding compliance
- A.8.4 (Source Code Access): Access control to code repositories
- A.8.32 (Change Management): Code review is part of change approval

---

## 11. Conclusion

This implementation guide provides practical, step-by-step procedures for establishing secure coding practices.

**Key Takeaways:**
- Adopt industry-standard secure coding frameworks (OWASP, CWE)
- Customize standards for organization's technology stack
- Implement two-tier code review (peer + security-focused)
- Deploy security tools (SAST, SCA, secret scanning) in CI/CD
- Use IDE plugins for real-time feedback
- Track security defects with SLAs
- Continuous improvement via metrics

**Success Factors:**
- Tool automation (SAST, SCA automated in CI/CD)
- Developer training (IMP-S2 Section 5)
- Security champions (distributed security responsibility)
- Clear processes (code review, defect management)
- Metrics-driven improvement

**Next Steps:**
1. Select and adopt secure coding standard
2. Deploy SAST/SCA tools in CI/CD
3. Implement code review process
4. Train developers
5. Track metrics and improve

For questions or support, contact the Security Architecture team.

---

**Document End**
