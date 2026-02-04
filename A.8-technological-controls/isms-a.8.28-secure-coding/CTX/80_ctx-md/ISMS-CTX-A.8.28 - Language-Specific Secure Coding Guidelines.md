**ISMS-CTX-A.8.28 - Language-Specific Secure Coding Guidelines**

**Document Control - ISMS-CTX-A.8.28**

| Field | Value |
|-------|-------|
| **Document Title** | Language-Specific Secure Coding Guidelines |
| **Document Type** | Technical Context (CTX) |
| **Document ID** | ISMS-CTX-A.8.28 |
| **Document Creator** | Application Security Lead |
| **Document Owner** | Application Security Lead |
| **Approved By** | Application Security Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

---

## Disclaimer

**CRITICAL**: This is an informational reference document and is **NOT** part of the formal ISMS policy framework.

The information contained herein provides technical context, language-specific secure coding patterns, and technology-specific guidance but **does NOT establish mandatory requirements**.

**Binding policy requirements** are defined in **ISMS-POL-A.8.28 (Secure Coding Policy)**.

**Purpose**: Support informed secure coding decisions by providing:

- Language-specific vulnerability patterns and prevention techniques
- Technology evolution and framework security features
- Best practice guidance for programming languages used by [Organization]
- Code examples demonstrating secure vs. insecure patterns

**Usage**: Technical reference for developers and Security Champions. Content may require updates as languages evolve and new frameworks emerge—check publication date.

---

# Purpose & Scope

## Document Objective

This document provides **language-specific secure coding patterns** that operationalize the generic security requirements from ISMS-POL-A.8.28. Security vulnerabilities manifest differently across programming languages due to:

- Language design choices (memory safety, type systems)
- Standard library implementations
- Common frameworks and patterns
- Developer community practices

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled." - Richard Feynman*

**This document answers**: "How do I implement secure coding standards *in this specific language*?"

## Coverage Philosophy

**High-Value Focus**: We cover vulnerabilities that are:
1. **Common** in organizational code
2. **High-severity** (exploitable, high impact)
3. **Language-specific** (require language-specific guidance)

**We do NOT**:

- Duplicate generic security principles (see ISMS-POL-A.8.28 Section 2.2)
- Cover every possible vulnerability (focus on OWASP Top 10 + language-specific)
- Replace authoritative external standards (we reference OWASP, CERT, vendor guides)

## Language Priority

Languages covered based on organizational usage (adjust per [Organization]'s technology stack):

1. **Python** (backend services, data processing, automation)
2. **JavaScript/TypeScript** (frontend, Node.js backend)
3. **Java** (enterprise applications, microservices)
4. **C#/.NET** (Windows applications, Azure services)
5. **Go** (infrastructure tools, cloud-native microservices)
6. **SQL** (cross-language, data access)

**Note**: If your language isn't covered, reference OWASP Cheat Sheet Series and SEI CERT Coding Standards for that language.

## Relationship to Policy

**ISMS-POL-A.8.28 establishes** (binding):

- Requirement to follow secure coding standards
- Requirement for input validation, output encoding, secure authentication
- Requirement to avoid prohibited practices (hardcoded secrets, weak crypto)

**This CTX document provides** (informational):

- How to implement those requirements in Python
- How to implement those requirements in JavaScript/TypeScript
- How to implement those requirements in Java
- Language-specific patterns and anti-patterns

## External References

**Authoritative Sources** (always check for updates):

- **OWASP Cheat Sheet Series**: https://cheatsheetseries.owasp.org/
- **SEI CERT Coding Standards**: https://wiki.sei.cmu.edu/confluence/
- **CWE (Common Weakness Enumeration)**: https://cwe.mitre.org/
- **Vendor-specific**: Microsoft SDL, Oracle Secure Coding Standards, Node.js Security Best Practices

---

# Python Security Guidelines

## Common Vulnerability Patterns

**Top Vulnerabilities in Python**:
1. **SQL Injection** (CWE-89): String formatting in queries
2. **Command Injection** (CWE-78): Unsafe use of `os.system()`, `subprocess` with `shell=True`
3. **Deserialization** (CWE-502): Unsafe pickle usage
4. **Path Traversal** (CWE-22): Unvalidated file paths
5. **Weak Cryptography** (CWE-327): Use of MD5/SHA1, insecure random

## SQL Injection Prevention

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
cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # SQL injection!
```

## Command Injection Prevention

✅ **CORRECT - List Arguments, No Shell**:
```python
import subprocess

# Pass arguments as list, shell=False (default)
result = subprocess.run(['ls', '-l', directory_name], 
                       capture_output=True, check=True)

# For filenames with special characters, use shlex
import shlex
filename = shlex.quote(user_filename)
subprocess.run(['tar', '-czf', 'backup.tar.gz', filename])
```

❌ **INSECURE - Shell Command Strings**:
```python
# NEVER use shell=True with user input
subprocess.run(f'ls -l {directory_name}', shell=True)  # Command injection!
os.system(f'rm {filename}')  # Command injection!
```

## Path Traversal Prevention

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
# Path traversal: user_input could be "../../etc/passwd"
filepath = f'/var/app/uploads/{user_input}'
with open(filepath, 'r') as f:  # Can access any file!
    content = f.read()
```

## XSS Prevention in Templates

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
```

## Secure Password Hashing

✅ **CORRECT - bcrypt or Argon2**:
```python
import bcrypt

# Hashing password
password = b"user_password"
salt = bcrypt.gensalt(rounds=12)  # Cost factor 12
hashed = bcrypt.hashpw(password, salt)

# Verifying password
if bcrypt.checkpw(password, hashed):
    print("Password correct")

# Or use Argon2 (recommended for new systems)
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("user_password")
ph.verify(hash, "user_password")
```

❌ **INSECURE - MD5, SHA1, or Plaintext**:
```python
import hashlib

# NEVER use MD5 or SHA1 for passwords
hashed = hashlib.md5(password.encode()).hexdigest()  # Vulnerable!
hashed = hashlib.sha1(password.encode()).hexdigest()  # Vulnerable!

# Even SHA256 without salt is weak
hashed = hashlib.sha256(password.encode()).hexdigest()  # Vulnerable to rainbow tables
```

## Secure Random Number Generation

✅ **CORRECT - secrets Module**:
```python
import secrets

# Generate secure random token
token = secrets.token_urlsafe(32)  # 32 bytes = 256 bits

# Generate secure random numbers
random_number = secrets.randbelow(100)  # Random number 0-99
```

❌ **INSECURE - random Module**:
```python
import random

# NEVER use random module for security
token = random.randint(0, 1000000)  # NOT cryptographically secure!
```

## Deserialization Safety

✅ **CORRECT - Use JSON or Restricted Unpickler**:
```python
import json

# Prefer JSON for data serialization
data = json.loads(user_input)  # Safe

# If pickle required, restrict allowed classes
import pickle
import io

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Only allow specific safe classes
        if module == "myapp.models" and name in ["User", "Config"]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Forbidden class: {module}.{name}")

def safe_unpickle(data):
    return RestrictedUnpickler(io.BytesIO(data)).load()
```

❌ **INSECURE - Unrestricted pickle.loads()**:
```python
import pickle

# NEVER unpickle untrusted data
obj = pickle.loads(user_input)  # Remote code execution risk!
```

---

# JavaScript/TypeScript Security Guidelines

## Common Vulnerability Patterns

**Top Vulnerabilities in JavaScript**:
1. **XSS** (CWE-79): innerHTML with user input, eval() usage
2. **Prototype Pollution** (CWE-1321): Unsafe object merging
3. **CSRF** (CWE-352): Missing CSRF tokens in forms
4. **Open Redirect** (CWE-601): Unvalidated redirect targets
5. **ReDoS** (CWE-1333): Regular expression denial of service

## XSS Prevention

✅ **CORRECT - Use textContent or Framework Auto-Escaping**:
```javascript
// Vanilla JS - use textContent (not innerHTML)
element.textContent = userInput;  // Safe - automatically escapes

// React - JSX auto-escapes by default
function Welcome({ name }) {
  return <h1>Welcome {name}</h1>;  // Auto-escaped
}

// Vue - templates auto-escape by default
<template>
  <h1>Welcome {{ userName }}</h1>  <!-- Auto-escaped -->
</template>
```

❌ **INSECURE - innerHTML with User Input**:
```javascript
// NEVER use innerHTML with user input
element.innerHTML = userInput;  // XSS vulnerability!

// Even with template literals
element.innerHTML = `<h1>Welcome ${userInput}</h1>`;  // XSS!

// React - dangerouslySetInnerHTML (avoid!)
<div dangerouslySetInnerHTML={{__html: userInput}} />  // XSS!
```

## Prototype Pollution Prevention

✅ **CORRECT - Safe Object Operations**:
```javascript
// Use Object.create(null) for safe objects
const safeObj = Object.create(null);
safeObj[userKey] = userValue;  // No prototype pollution

// Or validate keys before assignment
function safeAssign(obj, key, value) {
  if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
    throw new Error('Forbidden key');
  }
  obj[key] = value;
}

// Use Object.freeze() for immutable objects
const config = Object.freeze({ apiKey: 'secret' });
```

❌ **INSECURE - Direct Property Assignment**:
```javascript
// Prototype pollution vulnerability
const obj = {};
obj[userControlledKey] = userValue;  // If userControlledKey is '__proto__'

// Unsafe merge operations
Object.assign(target, userInput);  // Can pollute prototype
```

## CSRF Protection

✅ **CORRECT - Use CSRF Tokens**:
```javascript
// Express.js with csurf middleware
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.post('/transfer', csrfProtection, (req, res) => {
  // CSRF token validated automatically
  processTransfer(req.body);
});

// Frontend - include CSRF token in forms
<form method="POST" action="/transfer">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <button type="submit">Transfer</button>
</form>

// For AJAX requests
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'CSRF-Token': csrfToken,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
});
```

## Secure Password Hashing (Node.js)

✅ **CORRECT - bcrypt**:
```javascript
const bcrypt = require('bcrypt');

// Hash password
const saltRounds = 12;
const hash = await bcrypt.hash(password, saltRounds);

// Verify password
const match = await bcrypt.compare(password, hash);
if (match) {
  console.log('Password correct');
}
```

❌ **INSECURE - crypto.createHash()**:
```javascript
const crypto = require('crypto');

// NEVER use MD5 or SHA for passwords
const hash = crypto.createHash('md5').update(password).digest('hex');  // Vulnerable!
const hash = crypto.createHash('sha256').update(password).digest('hex');  // Still weak!
```

## Secure Random Generation (Node.js)

✅ **CORRECT - crypto.randomBytes()**:
```javascript
const crypto = require('crypto');

// Generate secure random token
const token = crypto.randomBytes(32).toString('hex');

// Generate secure random number
const randomValue = crypto.randomInt(0, 100);
```

❌ **INSECURE - Math.random()**:
```javascript
// NEVER use Math.random() for security
const token = Math.random().toString(36).substring(2);  // NOT secure!
```

## Avoid eval() and Dynamic Code Execution

❌ **DANGEROUS - eval() with User Input**:
```javascript
// NEVER use eval() with user input
eval(userInput);  // Remote code execution!

// Also dangerous
new Function(userInput)();  // Remote code execution!
setTimeout(userInput, 1000);  // Code injection!
```

✅ **SAFER - JSON.parse() or Specific Parsing**:
```javascript
// For data, use JSON.parse()
const data = JSON.parse(userInput);  // Safe if input is JSON

// For expressions, use expression parser library
const mathjs = require('mathjs');
const result = mathjs.evaluate(userInput);  // Sandboxed evaluation
```

---

# Java Security Guidelines

## Common Vulnerability Patterns

**Top Vulnerabilities in Java**:
1. **SQL Injection** (CWE-89): String concatenation in queries
2. **XXE** (CWE-611): XML External Entity attacks
3. **Deserialization** (CWE-502): Unsafe ObjectInputStream
4. **Path Traversal** (CWE-22): Unvalidated file paths
5. **Weak Cryptography** (CWE-327): Use of DES, MD5, weak RNG

## SQL Injection Prevention

✅ **CORRECT - PreparedStatement**:
```java
// JDBC PreparedStatement
String query = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();

// JPA/Hibernate (parameterized)
String jpql = "SELECT u FROM User u WHERE u.id = :userId";
TypedQuery<User> query = em.createQuery(jpql, User.class);
query.setParameter("userId", userId);
User user = query.getSingleResult();
```

❌ **INSECURE - String Concatenation**:
```java
// NEVER concatenate strings for SQL
String query = "SELECT * FROM users WHERE id = " + userId;  // SQL injection!
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

## XXE Prevention

✅ **CORRECT - Disable External Entities**:
```java
import javax.xml.parsers.DocumentBuilderFactory;

DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

// Disable external entities to prevent XXE
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);

DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(inputStream);
```

## Secure Deserialization

✅ **CORRECT - Use Look-Ahead Deserialization Filter (Java 9+)**:
```java
// Define allowed classes for deserialization
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.myapp.model.*;!*"  // Allow com.myapp.model classes only
);

ObjectInputStream ois = new ObjectInputStream(inputStream);
ois.setObjectInputFilter(filter);
Object obj = ois.readObject();
```

❌ **INSECURE - Unrestricted readObject()**:
```java
// NEVER deserialize untrusted data without validation
ObjectInputStream ois = new ObjectInputStream(inputStream);
Object obj = ois.readObject();  // Deserialization vulnerability!
```

## Secure Random Generation

✅ **CORRECT - SecureRandom**:
```java
import java.security.SecureRandom;

SecureRandom random = new SecureRandom();
byte[] token = new byte[32];
random.nextBytes(token);
```

❌ **INSECURE - java.util.Random**:
```java
import java.util.Random;

Random random = new Random();
int value = random.nextInt();  // NOT cryptographically secure!
```

---

# C#/.NET Security Guidelines

## Common Vulnerability Patterns

**Top Vulnerabilities in C#/.NET**:
1. **SQL Injection** (CWE-89): String interpolation in queries
2. **XSS** (CWE-79): Unencoded output in Razor views
3. **Path Traversal** (CWE-22): Unvalidated file paths
4. **XXE** (CWE-611): XML parsing vulnerabilities
5. **Deserialization** (CWE-502): BinaryFormatter usage

## SQL Injection Prevention

✅ **CORRECT - Parameterized Queries**:
```csharp
// ADO.NET with parameters
string query = "SELECT * FROM Users WHERE Id = @userId";
using (SqlCommand cmd = new SqlCommand(query, connection))
{
    cmd.Parameters.AddWithValue("@userId", userId);
    SqlDataReader reader = cmd.ExecuteReader();
}

// Entity Framework (LINQ - automatically parameterized)
var user = context.Users.FirstOrDefault(u => u.Id == userId);
```

❌ **INSECURE - String Interpolation**:
```csharp
// NEVER use string interpolation for SQL
string query = $"SELECT * FROM Users WHERE Id = {userId}";  // SQL injection!
SqlCommand cmd = new SqlCommand(query, connection);
```

## XSS Prevention in Razor

✅ **CORRECT - Razor Auto-Encoding**:
```csharp
@* Razor automatically HTML-encodes by default *@
<h1>Welcome @Model.UserName</h1>  @* Auto-encoded *@
```

❌ **INSECURE - Html.Raw()**:
```csharp
@* NEVER use Html.Raw() with user input *@
<div>@Html.Raw(Model.UserInput)</div>  @* XSS vulnerability! *@
```

## Secure Password Hashing

✅ **CORRECT - ASP.NET Core Identity or Rfc2898DeriveBytes**:
```csharp
using Microsoft.AspNetCore.Identity;

// ASP.NET Core Identity (recommended)
var passwordHasher = new PasswordHasher<User>();
string hash = passwordHasher.HashPassword(user, password);

// Verify
var result = passwordHasher.VerifyHashedPassword(user, hash, password);
if (result == PasswordVerificationResult.Success)
{
    // Password correct
}

// Manual PBKDF2 (if Identity not available)
using System.Security.Cryptography;

byte[] salt = new byte[16];
using (var rng = RandomNumberGenerator.Create())
{
    rng.GetBytes(salt);
}

var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000, HashAlgorithmName.SHA256);
byte[] hash = pbkdf2.GetBytes(32);
```

## Secure Deserialization

✅ **CORRECT - Use JSON.NET or System.Text.Json**:
```csharp
using System.Text.Json;

// Use JSON serialization (safe)
string json = JsonSerializer.Serialize(obj);
var obj = JsonSerializer.Deserialize<MyClass>(json);
```

❌ **INSECURE - BinaryFormatter**:
```csharp
// NEVER use BinaryFormatter with untrusted data
BinaryFormatter formatter = new BinaryFormatter();
object obj = formatter.Deserialize(stream);  // Deserialization vulnerability!
```

---

# Go Security Guidelines

## Common Vulnerability Patterns

**Top Vulnerabilities in Go**:
1. **SQL Injection** (CWE-89): String formatting in queries
2. **Command Injection** (CWE-78): Unsafe exec.Command usage
3. **Path Traversal** (CWE-22): Unvalidated file paths
4. **Race Conditions** (CWE-362): Improper goroutine synchronization
5. **Weak Cryptography** (CWE-327): Use of MD5, insecure random

## SQL Injection Prevention

✅ **CORRECT - Parameterized Queries**:
```go
// database/sql with parameters
query := "SELECT * FROM users WHERE id = $1"
row := db.QueryRow(query, userId)

// Using sqlx
var user User
err := db.Get(&user, "SELECT * FROM users WHERE id=$1", userId)
```

❌ **INSECURE - fmt.Sprintf() for SQL**:
```go
// NEVER use fmt.Sprintf() for SQL
query := fmt.Sprintf("SELECT * FROM users WHERE id = %d", userId)  // SQL injection!
rows, err := db.Query(query)
```

## Command Injection Prevention

✅ **CORRECT - exec.Command with Separate Arguments**:
```go
import "os/exec"

// Pass arguments separately
cmd := exec.Command("ls", "-l", directory)
output, err := cmd.Output()
```

❌ **INSECURE - exec.Command with Shell**:
```go
// NEVER use shell with user input
cmd := exec.Command("sh", "-c", fmt.Sprintf("ls -l %s", directory))  // Command injection!
```

## Secure Password Hashing

✅ **CORRECT - golang.org/x/crypto/bcrypt**:
```go
import "golang.org/x/crypto/bcrypt"

// Hash password
hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

// Verify password
err = bcrypt.CompareHashAndPassword(hash, []byte(password))
if err == nil {
    // Password correct
}
```

## Secure Random Generation

✅ **CORRECT - crypto/rand**:
```go
import "crypto/rand"

// Generate secure random bytes
token := make([]byte, 32)
_, err := rand.Read(token)
```

❌ **INSECURE - math/rand**:
```go
import "math/rand"

// NEVER use math/rand for security
value := rand.Intn(100)  // NOT cryptographically secure!
```

---

# SQL Security Guidelines (Cross-Language)

## Parameterized Queries by Database

**PostgreSQL**:
```sql
-- Parameterized query (safe)
SELECT * FROM users WHERE id = $1;  -- Parameter: userId
```

**MySQL**:
```sql
-- Parameterized query (safe)
SELECT * FROM users WHERE id = ?;  -- Parameter: userId
```

**SQL Server**:
```sql
-- Parameterized query (safe)
SELECT * FROM users WHERE id = @userId;  -- Parameter: @userId
```

## Least Privilege Database Accounts

✅ **CORRECT - Minimal Permissions**:
```sql
-- Create application-specific user with minimal permissions
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Grant only necessary permissions
GRANT SELECT, INSERT, UPDATE ON users TO app_user;
GRANT SELECT ON products TO app_user;

-- Deny dangerous permissions
REVOKE DROP, CREATE, ALTER ON DATABASE FROM app_user;
```

## Avoid Dynamic SQL in Stored Procedures

❌ **INSECURE - Dynamic SQL in Stored Procedure**:
```sql
-- SQL injection vulnerability in stored procedure
CREATE PROCEDURE GetUserById(@userId VARCHAR(50))
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'SELECT * FROM users WHERE id = ' + @userId;  -- SQL injection!
    EXEC sp_executesql @sql;
END
```

✅ **CORRECT - Parameterized Stored Procedure**:
```sql
-- Safe parameterized stored procedure
CREATE PROCEDURE GetUserById(@userId INT)
AS
BEGIN
    SELECT * FROM users WHERE id = @userId;  -- Safe
END
```

---

# Document Maintenance

**Update Frequency**: Semi-annual or when:

- Major language version released (Python 3.x, Java 17+, Node.js LTS)
- New framework security features available
- OWASP Top 10 updated
- Organizational language adoption changes

**Owner**: Application Security Lead

**Review Triggers**:

- New vulnerability patterns discovered
- Language/framework security advisories published
- Developer feedback on unclear guidance
- Tool integration changes (new SAST rules)

**Collaboration**:

- Senior Developers review for technical accuracy
- Security Champions validate practical applicability
- Development Teams provide feedback on usability

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Application Security Lead | Initial language guidelines extracted from consolidated policy |

---

**END OF ISMS-CTX-A.8.28**

*This technical reference supports ISMS-POL-A.8.28 implementation. Binding requirements are in the policy, not this document.*
<!-- QA_VERIFIED: 2026-02-01 -->
