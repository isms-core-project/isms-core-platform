# ISMS-POL-A.8.28-S2.2
## Secure Coding - Secure Coding Standards

**Document ID**: ISMS-POL-A.8.28-S2.2
**Title**: Secure Coding - Secure Coding Standards  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead / Development Standards Committee | Initial secure coding standards |

**Review Cycle**: Annual (or upon discovery of new vulnerability classes or OWASP Top 10 updates)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Application Security Lead
- Implementation Owner: Development Manager / Engineering Director
- Standards Committee: Senior Developers / Tech Leads

**Distribution**: All developers, security team, code reviewers, third-party development vendors  
**Related Documents**: ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines), ISMS-IMP-A.8.28.2 (Standards & Tools Assessment)

---

## 2.2.1 Introduction

This section establishes **secure coding standards** that developers must follow during software implementation. These standards are informed by industry best practices (OWASP, CWE, SANS, SEI CERT) and organizational experience with vulnerabilities.

*"Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it."* - Brian Kernighan

**Translation for Security**: If you write code using every obscure language feature and clever trick, you're guaranteeing you won't be able to reason about its security properties. Clarity and simplicity are prerequisites for security.

**Standards Organization**:
This document covers **language-agnostic secure coding principles** applicable to all development. For language-specific guidance (Java, C#, Python, JavaScript, etc.), refer to **ISMS-POL-A.8.28-S5.A (Language-Specific Guidelines)**.

**Primary Stakeholders**: All Developers, Code Reviewers, Security Champions

---

## 2.2.2 Universal Secure Coding Principles

### 2.2.2.1 Foundational Principles

All developers **SHALL** adhere to these foundational principles:

**PRINCIPLE 1: Validate All Input**
- Trust no input, regardless of source (user, database, API, file, environment variable)
- Implement whitelist validation (define what is allowed) not blacklist (define what is forbidden)
- Validate input at boundaries (where external data enters application)
- Reject invalid input, do not attempt to "sanitize" or "fix" malformed input

**PRINCIPLE 2: Encode All Output**
- Apply context-appropriate encoding when displaying user-controlled data
- HTML encode for HTML context, JavaScript encode for JavaScript context, SQL parameterize for SQL context
- Never trust output from one context to be safe in another context

**PRINCIPLE 3: Fail Securely**
- Default to denial (deny access unless explicitly permitted)
- Handle errors without exposing sensitive information
- Fail closed (restrictive) rather than fail open (permissive)

**PRINCIPLE 4: Minimize Attack Surface**
- Disable unnecessary features, services, and ports
- Remove debug code, unused libraries, and dead code
- Implement least privilege for application components

**PRINCIPLE 5: Establish Secure Defaults**
- Applications should be secure "out of the box" without configuration changes
- Force users to explicitly opt-in to less secure configurations (never opt-out)
- Document security implications of configuration changes

**PRINCIPLE 6: Separate Code from Data**
- Never mix executable code with untrusted data
- Use parameterized queries instead of string concatenation for SQL
- Use structured formats (JSON, XML with schema validation) instead of parsing untrusted strings

**PRINCIPLE 7: Defense in Depth**
- Never rely on a single security control
- Layer multiple controls (authentication + authorization + input validation + output encoding)
- Assume any single control can fail or be bypassed

---

## 2.2.3 Input Validation Requirements

### 2.2.3.1 Validation Strategy

**REQ-2.2.3.1-A: Whitelist Validation**

All input validation **MUST** use whitelist (allow-list) approach:

✅ **CORRECT - Whitelist Pattern**:
```
ALLOWED_COUNTRIES = ['CH', 'DE', 'FR', 'IT', 'AT']

if user_input not in ALLOWED_COUNTRIES:
    raise ValidationError("Invalid country code")
```

❌ **INCORRECT - Blacklist Pattern**:
```
FORBIDDEN_CHARS = ['<', '>', '"', "'", ';']

if any(char in user_input for char in FORBIDDEN_CHARS):
    raise ValidationError("Invalid characters detected")
```

**Rationale**: Blacklists are incomplete by nature - attackers discover new bypass techniques constantly. Whitelists define the expected "good" input space and reject everything else.

**REQ-2.2.3.1-B: Type and Format Validation**

Validation must verify:
1. **Data Type**: String, integer, boolean, date, etc.
2. **Format**: Regex pattern, structured format (email, phone, UUID)
3. **Range**: Minimum/maximum length, value bounds
4. **Business Logic**: Cross-field validation, consistency checks

**REQ-2.2.3.1-C: Validation Location**

Input validation **MUST** occur:
- **Server-side**: All validation must occur on trusted server (never trust client-side validation)
- **At Trust Boundaries**: Where external data enters application (API endpoints, form submissions, file uploads)
- **Before Use**: Validate immediately before using data in sensitive operations (database queries, system calls)

Client-side validation (JavaScript) is acceptable for **user experience only**, never for security.

### 2.2.3.2 Injection Prevention

**REQ-2.2.3.2-A: SQL Injection Prevention**

**MANDATORY - Use Parameterized Queries**:

✅ **CORRECT - Parameterized Query**:
```python
# Python example
cursor.execute("SELECT * FROM users WHERE username = ? AND status = ?", 
               (username, status))
```
```java
// Java example
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE username = ? AND status = ?");
stmt.setString(1, username);
stmt.setString(2, status);
ResultSet rs = stmt.executeQuery();
```

❌ **PROHIBITED - String Concatenation**:
```python
# NEVER DO THIS - SQL Injection vulnerability
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)
```

**Exceptions**: If parameterized queries are not feasible (dynamic table names, column names, ORDER BY clauses):
- Use whitelist validation for table/column names
- Map user input to predefined safe values
- Apply strict input validation (alphanumeric only, maximum length)

**REQ-2.2.3.2-B: Command Injection Prevention**

**AVOID** system command execution with user input. If unavoidable:

✅ **SAFER - Use Libraries Instead**:
```python
# Use library instead of shelling out
import subprocess
subprocess.run(['ls', '-l', user_directory], check=True)  # Argument array
```

❌ **DANGEROUS - Shell with String Concatenation**:
```python
# NEVER DO THIS - Command Injection vulnerability
os.system('ls -l ' + user_directory)
```

**REQ-2.2.3.2-C: LDAP Injection Prevention**
- Escape special characters: `*`, `(`, `)`, `\`, `NUL`
- Use framework-provided LDAP query builders with parameterization
- Validate DN (Distinguished Name) components against whitelist

**REQ-2.2.3.2-D: XML/XPath Injection Prevention**
- Use parameterized XPath queries where available
- Validate XML structure against schema (XSD validation)
- Escape special characters in XPath expressions: `'`, `"`, `/`, `[`, `]`

**REQ-2.2.3.2-E: NoSQL Injection Prevention**
- Use database driver's parameterization features
- Never pass raw JSON from user input directly to NoSQL queries
- Validate input types (e.g., ensure user_id is integer, not object with `$gt` operator)

### 2.2.3.3 File Upload Validation

**REQ-2.2.3.3-A: File Type Validation**

File uploads **MUST** implement:
1. **Extension Whitelist**: Allow only expected file extensions (`.jpg`, `.pdf`, `.docx`)
2. **MIME Type Verification**: Check Content-Type header **AND** file magic bytes
3. **Content Validation**: Open and parse file to verify it matches expected format
4. **Size Limits**: Maximum file size to prevent denial-of-service

❌ **INSUFFICIENT - Extension Check Only**:
```python
# Easily bypassed - attacker uploads shell.php.jpg
if filename.endswith('.jpg'):
    save_file(filename, content)
```

✅ **CORRECT - Multi-Layer Validation**:
```python
ALLOWED_EXTENSIONS = {'.jpg', '.png', '.pdf'}
ALLOWED_MIME_TYPES = {'image/jpeg', 'image/png', 'application/pdf'}

# Check extension
ext = os.path.splitext(filename)[1].lower()
if ext not in ALLOWED_EXTENSIONS:
    raise ValidationError("Invalid file extension")

# Check MIME type
mime_type = magic.from_buffer(content, mime=True)
if mime_type not in ALLOWED_MIME_TYPES:
    raise ValidationError("Invalid file type")

# Verify content (e.g., open image with PIL to confirm it's valid)
try:
    Image.open(io.BytesIO(content)).verify()
except Exception:
    raise ValidationError("Corrupted image file")
```

**REQ-2.2.3.3-B: File Storage Security**
- Store uploaded files **outside** web root to prevent direct execution
- Rename files using random UUID, do not preserve original filename
- Strip metadata (EXIF data from images, document properties) if not needed
- Scan files with antivirus/malware scanner before processing

---

## 2.2.4 Output Encoding Requirements

### 2.2.4.1 Cross-Site Scripting (XSS) Prevention

**REQ-2.2.4.1-A: Context-Aware Encoding**

All user-controlled data displayed in web pages **MUST** be encoded based on context:

| Context | Encoding Required | Example |
|---------|------------------|---------|
| **HTML Body** | HTML Entity Encoding | `<div>{{user_input \| html_encode}}</div>` |
| **HTML Attribute** | HTML Attribute Encoding | `<input value="{{user_input \| attr_encode}}">` |
| **JavaScript String** | JavaScript Encoding | `var x = "{{user_input \| js_encode}}";` |
| **URL Parameter** | URL Encoding | `<a href="/page?q={{user_input \| url_encode}}">` |
| **CSS** | CSS Encoding (or avoid dynamic CSS) | `<style>.user {color: {{user_input \| css_encode}};}</style>` |

**REQ-2.2.4.1-B: Use Framework Encoding Functions**

✅ **CORRECT - Use Framework Built-in Encoding**:
```python
# Django template (auto-escapes by default)
<div>{{ user_input }}</div>

# Jinja2 (auto-escapes if enabled)
<div>{{ user_input | e }}</div>

# React (auto-escapes by default)
<div>{userInput}</div>
```

❌ **DANGEROUS - Manual Encoding or Bypassing Framework**:
```python
# Django - Bypassing auto-escape (DANGEROUS unless you're certain data is safe)
<div>{{ user_input | safe }}</div>

# React - Bypassing auto-escape (DANGEROUS)
<div dangerouslySetInnerHTML={{__html: userInput}} />
```

**REQ-2.2.4.1-C: Content Security Policy (CSP)**

Web applications **SHOULD** implement Content Security Policy headers:
```
Content-Security-Policy: default-src 'self'; 
                         script-src 'self' https://trusted-cdn.com;
                         style-src 'self' 'unsafe-inline';
                         img-src 'self' data: https:;
```

CSP provides defense-in-depth by restricting sources of executable content even if XSS vulnerabilities exist.

### 2.2.4.2 Cross-Site Request Forgery (CSRF) Prevention

**REQ-2.2.4.2-A: CSRF Tokens for State-Changing Requests**

All state-changing operations (POST, PUT, DELETE) **MUST** implement CSRF protection:

✅ **CORRECT - Framework CSRF Token**:
```html
<!-- Django form with CSRF token -->
<form method="post">
    {% csrf_token %}
    <input name="email" value="...">
    <button type="submit">Update</button>
</form>
```

**REQ-2.2.4.2-B: SameSite Cookie Attribute**

Session cookies **SHOULD** use `SameSite` attribute:
```
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Strict
```

- `SameSite=Strict`: Cookie never sent on cross-site requests (most secure, may break legitimate workflows)
- `SameSite=Lax`: Cookie sent on top-level navigation (GET requests), not on embedded requests (recommended default)

**REQ-2.2.4.2-C: Custom Headers for API Requests**

REST APIs **SHOULD** require custom header for authentication:
```
X-CSRF-Token: <token>
Authorization: Bearer <jwt>
```

Browsers prevent cross-origin requests from setting custom headers, providing CSRF protection.

---

## 2.2.5 Authentication and Session Management

### 2.2.5.1 Password Storage

**REQ-2.2.5.1-A: Hashing Algorithm**

Passwords **MUST** be hashed using adaptive key derivation functions:

✅ **APPROVED ALGORITHMS**:
- **bcrypt** (cost factor ≥ 12, recommended default)
- **scrypt** (N=16384, r=8, p=1 minimum)
- **Argon2** (Argon2id variant recommended)
- **PBKDF2-HMAC-SHA256** (iterations ≥ 600,000)

❌ **PROHIBITED ALGORITHMS**:
- MD5, SHA-1, SHA-256 (without key derivation)
- Reversible encryption
- Plaintext storage

✅ **CORRECT - bcrypt Example**:
```python
import bcrypt

# Hashing password
password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))

# Verifying password
if bcrypt.checkpw(user_password.encode('utf-8'), stored_hash):
    # Authentication successful
```

**REQ-2.2.5.1-B: Password Policy**

Applications **SHOULD** enforce:
- Minimum length: 8 characters (12+ recommended)
- No maximum length restriction (support passphrases up to 128 characters)
- No composition requirements (uppercase, digits, symbols) - length matters more
- Check against compromised password lists (e.g., HaveIBeenPwned API)
- No password expiration without reason (causes weak, predictable passwords)

### 2.2.5.2 Multi-Factor Authentication (MFA)

**REQ-2.2.5.2-A: MFA for High-Risk Operations**

MFA is **REQUIRED** for:
- Administrative access
- Financial transactions
- Personal data modifications
- Password resets
- Access to production systems

MFA is **RECOMMENDED** for:
- All user authentication (organization-wide MFA)
- Remote access (VPN, SSH)

**REQ-2.2.5.2-B: MFA Implementation**

Acceptable MFA methods (in order of preference):
1. **FIDO2/WebAuthn** (hardware security keys, biometric authenticators)
2. **TOTP** (Time-based One-Time Password - authenticator apps)
3. **Push Notifications** (approved authenticator apps)
4. **SMS** (discouraged, acceptable only if no other option available)

❌ **UNACCEPTABLE**: Email-based "MFA", security questions (not a second factor)

### 2.2.5.3 Session Management

**REQ-2.2.5.3-A: Session Token Generation**

Session tokens **MUST**:
- Be cryptographically random (at least 128 bits of entropy)
- Be unpredictable (use `secrets` module in Python, `SecureRandom` in Java)
- Never include user information (user ID, email) in token

✅ **CORRECT - Secure Random Token**:
```python
import secrets
session_token = secrets.token_urlsafe(32)  # 256 bits of entropy
```

❌ **INSECURE - Predictable Token**:
```python
session_token = str(hash(username + timestamp))  # Predictable
```

**REQ-2.2.5.3-B: Session Cookie Security**

Session cookies **MUST** have:
- `HttpOnly` flag (prevent JavaScript access)
- `Secure` flag (HTTPS only)
- `SameSite` attribute (CSRF protection)
- Appropriate `Path` and `Domain` (restrict scope)
```
Set-Cookie: sessionId=...; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=3600
```

**REQ-2.2.5.3-C: Session Timeout**

Sessions **MUST** implement:
- **Idle timeout**: 15-30 minutes of inactivity
- **Absolute timeout**: 8-12 hours maximum session lifetime
- **Re-authentication**: For sensitive operations even within active session

**REQ-2.2.5.3-D: Session Invalidation**

Sessions **MUST** be invalidated:
- On user logout (destroy session on server)
- On privilege escalation (e.g., after MFA)
- After password change
- On security event (e.g., detection of session hijacking attempt)

---

## 2.2.6 Authorization and Access Control

### 2.2.6.1 Authorization Checks

**REQ-2.2.6.1-A: Server-Side Authorization**

Authorization checks **MUST** occur on server, never rely on client-side checks:

❌ **INSECURE - Client-Side Authorization**:
```javascript
// Client-side check - easily bypassed
if (user.role === 'admin') {
    showAdminPanel();
}
```

✅ **CORRECT - Server-Side Authorization**:
```python
@require_role('admin')
def admin_panel(request):
    # Server enforces authorization
    return render(request, 'admin.html')
```

**REQ-2.2.6.1-B: Direct Object Reference Protection**

Prevent Insecure Direct Object Reference (IDOR) vulnerabilities:

❌ **VULNERABLE - No Authorization Check**:
```python
# User can access any account by changing account_id parameter
def view_account(request, account_id):
    account = Account.objects.get(id=account_id)
    return render(request, 'account.html', {'account': account})
```

✅ **CORRECT - Verify Ownership**:
```python
def view_account(request, account_id):
    account = Account.objects.get(id=account_id)
    
    # Verify current user owns this account
    if account.user_id != request.user.id:
        raise PermissionDenied("Access denied")
    
    return render(request, 'account.html', {'account': account})
```

**REQ-2.2.6.1-C: Role-Based Access Control (RBAC)**

Applications **SHOULD** implement RBAC:
- Define roles with specific permissions (Admin, Editor, Viewer)
- Assign users to roles
- Check permissions, not roles directly (check `can_delete_post` not `is_admin`)

### 2.2.6.2 Privilege Escalation Prevention

**REQ-2.2.6.2-A: Least Privilege Principle**

Application components **MUST** run with minimum necessary privileges:
- Database connections use read-only accounts where possible
- Service accounts cannot escalate to administrative privileges
- File system access limited to required directories only

**REQ-2.2.6.2-B: Mass Assignment Protection**

Prevent mass assignment vulnerabilities where user input directly updates database:

❌ **VULNERABLE - Direct Mass Assignment**:
```python
# User can set is_admin=True by adding it to form data
user.update(**request.POST.dict())
```

✅ **CORRECT - Whitelist Allowed Fields**:
```python
ALLOWED_FIELDS = ['email', 'first_name', 'last_name']
update_data = {k: v for k, v in request.POST.items() if k in ALLOWED_FIELDS}
user.update(**update_data)
```

---

## 2.2.7 Cryptography Requirements

### 2.2.7.1 Encryption Standards

**REQ-2.2.7.1-A: Approved Algorithms**

Use only industry-standard, vetted cryptographic algorithms:

✅ **APPROVED - Symmetric Encryption**:
- **AES-256-GCM** (recommended for new applications)
- AES-256-CBC with HMAC (acceptable for legacy compatibility)
- ChaCha20-Poly1305 (acceptable alternative to AES-GCM)

✅ **APPROVED - Asymmetric Encryption**:
- **RSA** (minimum 2048-bit key, 3072-bit or 4096-bit recommended)
- **ECDSA** (P-256, P-384, or P-521 curves)
- **Ed25519** (recommended for new implementations)

✅ **APPROVED - Hashing**:
- **SHA-256, SHA-384, SHA-512** (for integrity, not passwords)
- **BLAKE2** (acceptable alternative)

❌ **PROHIBITED ALGORITHMS**:
- DES, 3DES, RC4, MD5, SHA-1
- ECB mode for block ciphers
- Custom/homegrown cryptography

**REQ-2.2.7.1-B: Never Implement Custom Cryptography**

*"Anyone, from the most clueless amateur to the best cryptographer, can create an algorithm that he himself can't break."* - Bruce Schneier

Developers **MUST NOT**:
- Implement custom cryptographic algorithms
- Modify existing algorithms
- Combine cryptographic primitives without expert review

Developers **MUST**:
- Use established cryptographic libraries (OpenSSL, libsodium, JCA, .NET Cryptography)
- Follow library documentation exactly
- Have cryptographic code reviewed by security expert

### 2.2.7.2 Key Management

**REQ-2.2.7.2-A: Secret Storage**

Cryptographic keys and secrets **MUST NOT** be:
- Hardcoded in source code
- Stored in configuration files committed to version control
- Logged or displayed in error messages
- Transmitted via email or chat

Secrets **MUST** be:
- Stored in dedicated secret management systems (HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
- Accessed via environment variables or secret APIs
- Encrypted at rest
- Access-controlled with audit logging

**REQ-2.2.7.2-B: Key Rotation**

Cryptographic keys **SHOULD**:
- Be rotated periodically (annually minimum, quarterly recommended)
- Be rotated immediately if compromise suspected
- Have rotation procedures documented and tested

### 2.2.7.3 Random Number Generation

**REQ-2.2.7.3-A: Cryptographically Secure RNG**

For security-sensitive operations (token generation, key generation, IV/nonce generation), use cryptographically secure random number generators:

✅ **CORRECT - Secure RNG**:
```python
import secrets
random_token = secrets.token_bytes(32)
```
```java
import java.security.SecureRandom;
SecureRandom secureRandom = new SecureRandom();
byte[] randomBytes = new byte[32];
secureRandom.nextBytes(randomBytes);
```

❌ **INSECURE - Standard RNG**:
```python
import random  # NOT cryptographically secure
token = random.randint(0, 1000000)  # Predictable
```

---

## 2.2.8 Error Handling and Logging

### 2.2.8.1 Secure Error Handling

**REQ-2.2.8.1-A: Generic Error Messages**

Error messages shown to users **MUST NOT** expose:
- Stack traces or debug information
- Database structure or SQL queries
- File paths or system information
- Cryptographic key material or credentials
- Existence of specific usernames or accounts (timing attacks)

✅ **CORRECT - Generic Error Message**:
```
"Invalid username or password"  (don't reveal which one is wrong)
"An error occurred. Please contact support." (for unexpected errors)
```

❌ **INFORMATION DISCLOSURE**:
```
"Password incorrect for user john.doe@example.com"
"SQLException: Table 'users' doesn't exist at line 42"
"FileNotFoundError: /var/www/app/config/secrets.yml not found"
```

**REQ-2.2.8.1-B: Detailed Logging (Server-Side Only)**

Detailed error information (stack traces, variables) **MUST**:
- Be logged server-side only
- Never be displayed to end users
- Include contextual information for debugging
- Exclude sensitive data (passwords, tokens, PII)

### 2.2.8.2 Security Logging

**REQ-2.2.8.2-A: Security Events to Log**

Applications **MUST** log:
- Authentication events (success/failure, MFA usage)
- Authorization failures (access denied events)
- Input validation failures
- Security-relevant configuration changes
- Administrative actions
- Cryptographic operations (key usage, certificate verification failures)

**REQ-2.2.8.2-B: Log Content Requirements**

Security logs **MUST** include:
- Timestamp (UTC, high precision)
- User identifier (username, user ID, IP address)
- Event type (authentication, authorization, data access)
- Outcome (success, failure, error)
- Relevant context (resource accessed, operation attempted)

Security logs **MUST NOT** include:
- Passwords or password hashes
- Session tokens or API keys
- Credit card numbers or other PII (unless specifically required for audit)

**REQ-2.2.8.2-C: Log Protection**

Logs **MUST** be:
- Stored securely with access controls
- Protected from tampering (append-only, cryptographic signatures)
- Retained per organizational retention policy
- Monitored for suspicious patterns

---

## 2.2.9 Configuration Management

### 2.2.9.1 Secure Configuration

**REQ-2.2.9.1-A: Security Defaults**

Applications **MUST**:
- Be secure by default without configuration changes
- Disable unnecessary features and services
- Require explicit opt-in for less secure configurations
- Document security implications of all configuration options

**REQ-2.2.9.1-B: Debug Code Removal**

Production deployments **MUST NOT** include:
- Debug endpoints or test pages
- Development credentials or API keys
- Verbose logging or stack trace display
- Source maps (for compiled/minified code)
- Unused dependencies or dead code

**REQ-2.2.9.1-C: Security Headers**

Web applications **MUST** implement security headers:
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'
Permissions-Policy: geolocation=(), microphone=(), camera=()
Referrer-Policy: strict-origin-when-cross-origin
```

### 2.2.9.2 Dependency Management

**REQ-2.2.9.2-A: Dependency Scanning**

Third-party dependencies addressed in **ISMS-POL-A.8.28-S2.4** (covered separately for detailed treatment)

---

## 2.2.10 Language-Specific Standards

Detailed language-specific secure coding guidelines are provided in **ISMS-POL-A.8.28-S5.A** for:
- Java
- C# / .NET
- Python
- JavaScript / TypeScript
- C / C++
- Go
- Ruby
- PHP
- Swift / Objective-C (iOS)
- Kotlin (Android)

Developers **MUST** follow language-specific guidelines in addition to these universal standards.

---

## 2.2.11 Compliance and Evidence

### 2.2.11.1 Standards Compliance Assessment

Compliance with secure coding standards is assessed in:
- **ISMS-IMP-A.8.28.2**: Standards & Tools Assessment

Evidence includes:
- Code review records showing standards enforcement
- SAST tool findings and remediation tracking
- Developer training completion on secure coding standards
- Coding standards documentation (internal wiki, style guides)
- Security champion engagement and knowledge sharing activities

### 2.2.11.2 Prohibited Practices Registry

Organizations **SHOULD** maintain a "Prohibited Practices" registry documenting:
- Insecure coding patterns identified in incidents or audits
- Vulnerable libraries or functions that must not be used
- Deprecated APIs or methods with security issues
- Organization-specific anti-patterns

This registry serves as organizational memory, preventing repetition of past mistakes.

---

**END OF DOCUMENT**

*"Controlling complexity is the essence of computer programming." - Brian Kernighan*

**Application to Security**: Secure code is maintainable code. Complex, clever code is impossible to reason about security properties. Simplicity, clarity, and defensive programming are the foundation of security.