# ISMS-POL-A.8.28-S5.A
## Secure Coding - Language-Specific Guidelines

**Document ID**: ISMS-POL-A.8.28-S5.A
**Title**: Secure Coding - Language-Specific Guidelines  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial language-specific guidelines |

**Review Cycle**: Semi-annual (or when major language version released)
**Next Review Date**: [Approval Date + 6 months] 
**Approvers**: 
- Primary: Application Security Lead
- Technical Review: Senior Developers (by language)
- Consulted: Security Champions

**Distribution**: All developers
**Related Documents**: 
- ISMS-POL-A.8.28-S2.2 (Secure Coding Standards)
- ISMS-POL-A.8.28-S5 (Annexes Overview)
- ISMS-POL-A.8.28-S5.D (Quick Reference Guide)

---

## 1. Introduction

### 1.1 Purpose

> *"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled." - Richard Feynman*

This annex provides **language-specific secure coding patterns** that operationalize the generic security requirements from ISMS-POL-A.8.28-S2.2. Security vulnerabilities manifest differently across programming languages due to:

- Language design choices (memory safety, type systems)
- Standard library implementations
- Common frameworks and patterns
- Developer community practices

**This annex answers**: "How do I implement secure coding standards *in this specific language*?"

### 1.2 Coverage Philosophy

**High-Value Focus**: We cover vulnerabilities that are:
1. **Common** in organizational code
2. **High-severity** (exploitable, high impact)
3. **Language-specific** (require language-specific guidance)

**We do NOT**:
- Duplicate generic security principles (see S2.2 for those)
- Cover every possible vulnerability (focus on OWASP Top 10 + language-specific)
- Replace authoritative external standards (we reference OWASP, CERT, vendor guides)

### 1.3 Language Priority

Languages covered based on organizational usage (descending priority):

1. **Python** (backend services, data processing, automation)
2. **JavaScript/TypeScript** (frontend, Node.js backend)
3. **Java** (enterprise applications, microservices)
4. **C#/.NET** (Windows applications, Azure services)
5. **Go** (infrastructure tools, microservices)
6. **SQL** (cross-language, data access)

**Note**: If your language isn't here, reference OWASP Cheat Sheet Series and SEI CERT for that language, and request addition via S5 feedback process.

### 1.4 External References

**Authoritative Sources** (always check for updates):
- **OWASP Cheat Sheet Series**: https://cheatsheetseries.owasp.org/
- **SEI CERT Coding Standards**: https://wiki.sei.cmu.edu/confluence/
- **CWE (Common Weakness Enumeration)**: https://cwe.mitre.org/
- **Vendor-specific**: Microsoft SDL, Oracle Secure Coding, Node.js Security

---

## 2. Python Security Guidelines

### 2.1 Common Vulnerability Patterns

**Top Vulnerabilities in Python**:
1. **SQL Injection** (CWE-89): String formatting in queries
2. **Command Injection** (CWE-78): Unsafe use of os.system(), subprocess with shell=True
3. **Deserialization** (CWE-502): Unsafe pickle usage
4. **Path Traversal** (CWE-22): Unvalidated file paths
5. **Weak Cryptography** (CWE-327): Use of MD5/SHA1, insecure random

### 2.2 Input Validation

**SQL Injection Prevention**:

✅ **CORRECT - Parameterized Queries**:
```python
# Using sqlite3
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Using psycopg2 (PostgreSQL)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Using SQLAlchemy ORM
user = session.query(User).filter(User.id == user_id).first()
```

❌ **INSECURE - String Formatting**:
```python
# NEVER use f-strings or % formatting for SQL
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection!
cursor.execute("SELECT * FROM users WHERE id = %s" % user_id)  # SQL injection!

# Even with .format()
cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # SQL injection!
```

**Command Injection Prevention**:

✅ **CORRECT - List Arguments, No Shell**:
```python
import subprocess

# Pass arguments as list, shell=False (default)
result = subprocess.run(['ls', '-l', directory_name], 
                       capture_output=True, check=True)

# For complex commands, use shlex to safely quote
import shlex
filename = shlex.quote(user_filename)
subprocess.run(['tar', '-czf', 'backup.tar.gz', filename])
```

❌ **INSECURE - Shell Command Strings**:
```python
# NEVER use shell=True with user input
subprocess.run(f'ls -l {directory_name}', shell=True)  # Command injection!
os.system(f'rm {filename}')  # Command injection!

# Even with escaping, prefer list arguments
subprocess.run(['rm', filename])  # Safer
```

**Path Traversal Prevention**:

✅ **CORRECT - Validate and Resolve Paths**:
```python
import os
from pathlib import Path

UPLOAD_DIR = Path('/var/app/uploads')

def safe_file_access(user_filename):
    # Resolve to absolute path and check it's within allowed directory
    requested_path = (UPLOAD_DIR / user_filename).resolve()
    
    # Ensure path is within UPLOAD_DIR
    if not requested_path.is_relative_to(UPLOAD_DIR):
        raise ValueError("Invalid file path")
    
    return requested_path

# Usage
safe_path = safe_file_access(user_input)
with open(safe_path, 'r') as f:
    content = f.read()
```

❌ **INSECURE - Direct Path Concatenation**:
```python
# Path traversal vulnerability: user_input could be "../../etc/passwd"
filepath = f'/var/app/uploads/{user_input}'
with open(filepath, 'r') as f:  # Can access any file!
    content = f.read()
```

### 2.3 Output Encoding

**XSS Prevention in Templates**:

✅ **CORRECT - Use Template Auto-Escaping**:
```python
# Jinja2 (Flask default) - auto-escaping enabled by default
from flask import render_template

@app.route('/profile')
def profile():
    # user_data['name'] will be auto-escaped
    return render_template('profile.html', name=user_data['name'])

# In template (profile.html):
# <h1>Welcome {{ name }}</h1>  <!-- Auto-escaped -->
```

❌ **INSECURE - Manual String Formatting**:
```python
# NEVER build HTML with string formatting
html = f"<h1>Welcome {user_data['name']}</h1>"  # XSS if name contains <script>
return html

# Even with .format()
html = "<h1>Welcome {}</h1>".format(user_data['name'])  # Still XSS!
```

**Note**: If you MUST output unescaped HTML, use `|safe` filter in Jinja2, but ONLY with trusted, sanitized input.

### 2.4 Cryptography

**Secure Password Hashing**:

✅ **CORRECT - bcrypt or Argon2**:
```python
import bcrypt

# Hashing password
password = b"user_password"
salt = bcrypt.gensalt(rounds=12)  # Cost factor 12 (adjust based on performance)
hashed = bcrypt.hashpw(password, salt)

# Verifying password
if bcrypt.checkpw(password, hashed):
    print("Password correct")

# Or use Argon2 (recommended for new systems)
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("user_password")
ph.verify(hash, "user_password")  # Raises exception if wrong
```

❌ **INSECURE - MD5, SHA1, or Plaintext**:
```python
import hashlib

# NEVER use MD5 or SHA1 for passwords
hashed = hashlib.md5(password.encode()).hexdigest()  # Vulnerable!
hashed = hashlib.sha1(password.encode()).hexdigest()  # Vulnerable!

# Even SHA256 without salt is weak
hashed = hashlib.sha256(password.encode()).hexdigest()  # No salt = vulnerable to rainbow tables
```

**Secure Random Number Generation**:

✅ **CORRECT - secrets Module**:
```python
import secrets

# Generate tokens, API keys, session IDs
token = secrets.token_urlsafe(32)  # 32 bytes = 256 bits
api_key = secrets.token_hex(32)

# Random integers for security purposes
secure_number = secrets.randbelow(100)  # Range [0, 100)
```

❌ **INSECURE - random Module**:
```python
import random

# NEVER use random module for security purposes
token = str(random.randint(1000000, 9999999))  # Predictable!
api_key = ''.join(random.choices('abcdef0123456789', k=32))  # Predictable!
```

**Secure Encryption**:

✅ **CORRECT - cryptography Library with AES-GCM**:
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generate key (store securely, don't hardcode!)
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# Encrypt
nonce = os.urandom(12)  # 96-bit nonce for GCM
ciphertext = aesgcm.encrypt(nonce, plaintext, None)

# Decrypt
plaintext = aesgcm.decrypt(nonce, ciphertext, None)
```

❌ **INSECURE - DES, ECB Mode, or Homebrew Crypto**:
```python
# NEVER use DES, 3DES, or RC4
# NEVER use ECB mode (no IV)
# NEVER implement your own cryptography
```

### 2.5 Deserialization Security

**Avoid pickle with Untrusted Data**:

✅ **CORRECT - Use JSON for Untrusted Data**:
```python
import json

# JSON is safe for untrusted data (no code execution)
data = json.loads(user_input)

# For complex objects, use safer alternatives:
# - MessagePack, Protocol Buffers (limited functionality)
# - JSON with manual object reconstruction
```

❌ **INSECURE - pickle with Untrusted Data**:
```python
import pickle

# NEVER use pickle on data from users, network, or untrusted sources
obj = pickle.loads(user_data)  # Remote code execution if malicious!

# Even pickle from files can be dangerous if file is user-controlled
with open(user_uploaded_file, 'rb') as f:
    obj = pickle.load(f)  # RCE vulnerability!
```

**Note**: pickle is safe ONLY for data you control (e.g., internal caching). For any external data, use JSON or protobuf.

### 2.6 Recommended Tools

**SAST (Static Analysis)**:
- **Bandit**: Python security linter (detects common vulnerabilities)
- **Semgrep**: Pattern-based code analysis
- **Pylint with security plugins**: Code quality + security

**Dependency Scanning**:
- **pip-audit**: Scan for known CVEs in dependencies
- **Safety**: Python dependency security checker
- **Dependabot**: Automated dependency updates (GitHub)

**Linters with Security Rules**:
- **Ruff**: Fast Python linter with security rules
- **Flake8 with plugins**: flake8-bandit, flake8-bugbear

**Configuration**:
```bash
# Install Bandit
pip install bandit

# Run Bandit on codebase
bandit -r . -f json -o bandit-report.json

# Install pip-audit
pip install pip-audit

# Scan dependencies
pip-audit
```

### 2.7 Reference Standards

- **OWASP Python Security Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/Python_Security_Cheat_Sheet.html
- **PyPA Security Guidelines**: https://www.python.org/dev/security/
- **Bandit Documentation**: https://bandit.readthedocs.io/

---

## 3. JavaScript/TypeScript Security Guidelines

### 3.1 Common Vulnerability Patterns

**Top Vulnerabilities in JavaScript**:
1. **XSS (Cross-Site Scripting)** (CWE-79): Unescaped output, innerHTML, dangerouslySetInnerHTML
2. **Prototype Pollution** (CWE-1321): Unsafe object merging
3. **ReDoS (Regular Expression DoS)** (CWE-1333): Catastrophic backtracking
4. **CSRF** (CWE-352): Missing CSRF tokens
5. **Insecure Dependencies** (CWE-1104): npm package vulnerabilities

### 3.2 XSS Prevention

**React XSS Prevention**:

✅ **CORRECT - Use JSX Default Escaping**:
```javascript
// React automatically escapes by default
function UserProfile({ username }) {
  return <div>Welcome {username}</div>;  // Safe: JSX escapes
}

// Using text content (safe)
element.textContent = userInput;
```

❌ **INSECURE - dangerouslySetInnerHTML, innerHTML**:
```javascript
// NEVER use dangerouslySetInnerHTML with user input
function UserProfile({ userBio }) {
  return <div dangerouslySetInnerHTML={{__html: userBio}} />;  // XSS!
}

// NEVER use innerHTML with user input
element.innerHTML = userInput;  // XSS!

// Even with sanitization, prefer textContent
element.innerHTML = sanitize(userInput);  // Risky if sanitizer has bypass
```

**DOMPurify for Rich Content**:

✅ **CORRECT - Sanitize HTML Before Rendering**:
```javascript
import DOMPurify from 'dompurify';

function RichTextDisplay({ htmlContent }) {
  // Sanitize before rendering
  const clean = DOMPurify.sanitize(htmlContent, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p'],
    ALLOWED_ATTR: []
  });
  
  return <div dangerouslySetInnerHTML={{__html: clean}} />;
}
```

**URL Handling**:

✅ **CORRECT - Validate URLs**:
```javascript
function SafeLink({ userUrl }) {
  // Validate URL is http/https only
  const url = new URL(userUrl);
  if (!['http:', 'https:'].includes(url.protocol)) {
    throw new Error('Invalid URL protocol');
  }
  
  return <a href={url.href} rel="noopener noreferrer">{url.href}</a>;
}
```

❌ **INSECURE - Unvalidated javascript: URLs**:
```javascript
// NEVER allow javascript: protocol
<a href={userUrl}>Link</a>  // XSS if userUrl is "javascript:alert(1)"
```

### 3.3 Prototype Pollution Prevention

✅ **CORRECT - Safe Object Operations**:
```javascript
// Use Object.create(null) for maps
const safeMap = Object.create(null);
safeMap[userKey] = userValue;  // No prototype pollution

// Use Map for key-value pairs
const map = new Map();
map.set(userKey, userValue);  // Safe

// Validate keys before assignment
function safeAssign(obj, key, value) {
  if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
    throw new Error('Invalid key');
  }
  obj[key] = value;
}
```

❌ **INSECURE - Unchecked Property Assignment**:
```javascript
// Prototype pollution vulnerability
const obj = {};
const userKey = '__proto__';
obj[userKey] = { polluted: true };  // Pollutes Object.prototype!

// Merge without validation
function merge(target, source) {
  for (let key in source) {
    target[key] = source[key];  // Vulnerable if source has __proto__
  }
}
```

### 3.4 Regular Expression DoS (ReDoS) Prevention

✅ **CORRECT - Safe Regex Patterns**:
```javascript
// Safe: No nested quantifiers
const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

// Safe: Possessive quantifiers or atomic groups (when available)
const safeRegex = /^(a+)+b$/;  // This specific pattern is vulnerable

// Use libraries that detect ReDoS
import { isSafe } from 'recheck';
if (!isSafe(userRegex)) {
  throw new Error('Unsafe regex pattern');
}

// Timeout for regex execution
function safeMatch(text, regex, timeout = 100) {
  const start = Date.now();
  return text.match(regex);
  // Note: JS doesn't have native regex timeout, use worker threads for untrusted regex
}
```

❌ **INSECURE - Vulnerable Regex Patterns**:
```javascript
// Catastrophic backtracking: nested quantifiers
const badRegex = /^(a+)+$/;  // Exponential time on input "aaaaaaaaaa!"
const badRegex2 = /^(a|a)*$/;  // Also vulnerable
const badRegex3 = /^(.*a){x}$/;  // Vulnerable

// Testing with attacker input
const userInput = 'a'.repeat(50) + '!';
userInput.match(badRegex);  // Hangs!
```

### 3.5 Authentication & CSRF

**CSRF Token Handling**:

✅ **CORRECT - Include CSRF Tokens**:
```javascript
// Axios example (reads token from cookie or meta tag)
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// Fetch API example
fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': getCsrfToken()  // Get from cookie or meta tag
  },
  body: JSON.stringify(data)
});

function getCsrfToken() {
  return document.querySelector('meta[name="csrf-token"]').content;
}
```

**JWT Handling**:

✅ **CORRECT - Secure JWT Storage**:
```javascript
// Store JWT in memory (React state, Redux)
// NEVER in localStorage (XSS can steal)

// Use httpOnly cookies for refresh tokens (backend sets)
// Short-lived access token in memory

function useAuth() {
  const [accessToken, setAccessToken] = useState(null);
  
  // Refresh token stored in httpOnly cookie (set by backend)
  async function refreshAccessToken() {
    const response = await fetch('/auth/refresh', {
      credentials: 'include'  // Send httpOnly cookie
    });
    const { accessToken } = await response.json();
    setAccessToken(accessToken);
  }
  
  return { accessToken, refreshAccessToken };
}
```

❌ **INSECURE - JWT in localStorage**:
```javascript
// NEVER store sensitive tokens in localStorage
localStorage.setItem('jwt', token);  // XSS can steal this!

// Same for sessionStorage
sessionStorage.setItem('jwt', token);  // Still vulnerable to XSS
```

### 3.6 Recommended Tools

**SAST**:
- **ESLint with security plugins**: eslint-plugin-security, eslint-plugin-no-unsanitized
- **Semgrep**: Pattern-based security scanning
- **SonarQube**: Comprehensive code quality + security

**Dependency Scanning**:
- **npm audit**: Built-in vulnerability scanner
- **Snyk**: Continuous dependency monitoring
- **OWASP Dependency-Check**: Multi-language dependency scanner

**Runtime Protection**:
- **Content Security Policy (CSP)**: Mitigate XSS impact
- **Subresource Integrity (SRI)**: Verify CDN resource integrity

**Configuration**:
```bash
# Install ESLint security plugin
npm install --save-dev eslint-plugin-security

# Run npm audit
npm audit

# Fix auto-fixable vulnerabilities
npm audit fix
```

### 3.7 Reference Standards

- **OWASP JavaScript Security Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/Nodejs_Security_Cheat_Sheet.html
- **Node.js Security Best Practices**: https://nodejs.org/en/docs/guides/security/
- **OWASP Top 10 for JavaScript**: Focus on XSS, prototype pollution, insecure dependencies

---

## 4. SQL Security Guidelines (Cross-Language)

### 4.1 Parameterized Queries

**This applies to ALL languages accessing SQL databases.**

✅ **CORRECT - Always Use Parameterized Queries**:
```sql
-- Python (sqlite3)
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

-- Python (psycopg2 - PostgreSQL)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

-- Java (PreparedStatement)
PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
stmt.setInt(1, userId);

-- C# (.NET)
var cmd = new SqlCommand("SELECT * FROM users WHERE id = @id", conn);
cmd.Parameters.AddWithValue("@id", userId);

-- Node.js (pg - PostgreSQL)
await client.query("SELECT * FROM users WHERE id = $1", [userId]);
```

❌ **INSECURE - String Concatenation**:
```sql
-- NEVER build queries with string concatenation (ANY language)
query = "SELECT * FROM users WHERE id = " + userId;  -- SQL injection!
query = f"SELECT * FROM users WHERE id = {userId}";  -- SQL injection!
```

### 4.2 Stored Procedures (Use Carefully)

✅ **CORRECT - Parameterized Stored Procedures**:
```sql
-- Create stored procedure (SQL Server example)
CREATE PROCEDURE GetUserById
    @UserId INT
AS
BEGIN
    SELECT * FROM Users WHERE Id = @UserId;
END

-- Call from application (C#)
var cmd = new SqlCommand("GetUserById", conn);
cmd.CommandType = CommandType.StoredProcedure;
cmd.Parameters.AddWithValue("@UserId", userId);
```

❌ **INSECURE - Dynamic SQL in Stored Procedures**:
```sql
-- NEVER use dynamic SQL inside stored procedures with user input
CREATE PROCEDURE GetUser
    @TableName NVARCHAR(50),
    @UserId INT
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'SELECT * FROM ' + @TableName + ' WHERE Id = ' + CAST(@UserId AS NVARCHAR);
    EXEC(@sql);  -- SQL injection!
END
```

### 4.3 ORM Security

✅ **CORRECT - ORM with Proper Usage**:
```python
# SQLAlchemy (Python) - Safe by default
user = session.query(User).filter(User.id == user_id).first()

# Django ORM - Safe by default
user = User.objects.get(id=user_id)

# Entity Framework (C#) - Safe by default
var user = context.Users.FirstOrDefault(u => u.Id == userId);
```

❌ **INSECURE - Raw SQL Through ORM**:
```python
# Even with ORM, raw SQL can be vulnerable
user = session.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection!

# Django raw() with interpolation
user = User.objects.raw(f"SELECT * FROM users WHERE id = {user_id}")  # SQL injection!
```

**ORM Raw Query Safety**:
```python
# If you MUST use raw SQL, still parameterize
user = session.execute("SELECT * FROM users WHERE id = :id", {"id": user_id})

# Django raw() with parameters
user = User.objects.raw("SELECT * FROM users WHERE id = %s", [user_id])
```

---

## 5. Cross-Language Security Principles

### 5.1 Universal Best Practices

**These apply to ALL languages**:

1. **Never Trust User Input**: Validate everything from users, files, APIs, databases
2. **Use Framework Security Features**: Don't reinvent authentication, use proven libraries
3. **Keep Dependencies Updated**: Monitor and patch vulnerable dependencies
4. **Fail Securely**: Default deny, never expose error details
5. **Least Privilege**: Run with minimum necessary permissions
6. **Defense in Depth**: Multiple security layers (validation + encoding + CSP)

### 5.2 Input Validation Principles

**Whitelist over Blacklist**:
```python
# Good: Whitelist approach
if input_type not in ['pdf', 'doc', 'docx']:
    raise ValueError("Invalid file type")

# Bad: Blacklist approach (always incomplete)
if input_type in ['exe', 'bat', 'sh']:  # What about .com, .vbs, .js, ...?
    raise ValueError("Invalid file type")
```

### 5.3 Error Handling Principles

**Generic Error Messages to Users**:
```python
# Good: Generic message
try:
    authenticate(username, password)
except AuthenticationError:
    return "Invalid username or password"  # Don't reveal which is wrong

# Bad: Information disclosure
except UserNotFoundError:
    return "User not found"  # Reveals username validity
except InvalidPasswordError:
    return "Invalid password"  # Reveals username is valid
```

---

## 6. Language Update Process

### 6.1 Requesting New Language

**If your language isn't covered**:
1. Submit request via security feedback channel
2. Include: language name, usage context, common vulnerabilities
3. Application Security Lead reviews within 10 business days
4. If approved, section added within 30 days

### 6.2 Updating Existing Language Section

**Triggers for update**:
- New vulnerability pattern discovered in organizational code
- Major language version with security-relevant changes
- Framework update with new security features
- OWASP/CERT guidance updated

**Process**: See ISMS-POL-A.8.28-S5 Section 3.2

---

## 7. Document History

| Date | Version | Change Summary | Author |
|------|---------|----------------|--------|
| [Approval Date] | 1.0 | Initial language-specific guidelines (Python, JS/TS, SQL) | Application Security Lead |

**Future Additions Planned**:
- Version 1.1: Java security guidelines (Q2 2026)
- Version 1.2: C#/.NET security guidelines (Q3 2026)
- Version 1.3: Go security guidelines (Q4 2026)

---

**END OF DOCUMENT**