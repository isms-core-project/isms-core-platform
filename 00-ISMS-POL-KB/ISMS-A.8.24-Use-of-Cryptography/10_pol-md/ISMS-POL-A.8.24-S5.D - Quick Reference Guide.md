# Control A.8.24: Use of Cryptography
## APPENDIX D
## Quick Reference Guide

---

**Document ID**: ISMS-POL-A.8.24-S5.D  
**Title**: Use of Cryptography - Quick Reference Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Team Lead / Technical Writer | Initial quick reference documentation |

**Review Cycle**: Annual (or upon S5.A technical reference updates)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Security Team Lead (for technical accuracy)
- Secondary: Chief Information Security Officer (CISO)
- User Validation: Development Team Lead / System Administrator Lead (for usability)

**Distribution**: All technical staff, developers, system administrators, infrastructure teams, helpdesk/support teams  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, user documentation best practices

---

## Purpose of This Guide

This quick reference provides at-a-glance guidance for common cryptographic tasks and scenarios. For detailed requirements, always refer to the full policy sections.

**Print this guide and keep it accessible for quick reference.**

---

## D.1 Common Scenarios - Quick Answers

### "I need to generate a new TLS certificate"

**Quick Steps:**
1. Generate private key: `openssl genrsa -out server.key 3072` or use ECDSA: `openssl ecparam -genkey -name prime256v1 -out server.key`
2. Create CSR: `openssl req -new -key server.key -out server.csr`
3. Submit CSR to CA (internal or public)
4. Install certificate + private key on server
5. Verify: https://www.ssllabs.com/ssltest/

**Requirements:**
- Key: RSA ≥3072-bit OR ECDSA P-256+
- Max validity: 397 days (90 days recommended)
- Must include Subject Alternative Name (SAN)

---

### "I need to encrypt data at rest in a database"

**Options:**
1. **Transparent Data Encryption (TDE)** - Preferred
   - SQL Server: Enable TDE, use AES-256
   - Oracle: Configure TDE with AES-256
   - PostgreSQL: Use pgcrypto or pg_tde extension
   - MySQL: Enable InnoDB encryption

2. **Column-level encryption** - For specific sensitive fields
   - Encrypt at application layer before INSERT
   - Use AES-256-GCM
   - Store keys in KMS (NOT in database)

3. **Full disk encryption** - Base layer protection
   - Server storage encrypted with LUKS/BitLocker
   - Keys separate from data

**Key Management:**
- Store keys in KMS or HSM
- Rotate database keys annually
- Test key recovery procedures

---

### "I need to set up file transfer for external partners"

**Approved Methods:**
1. **SFTP** (Preferred)
   - Configure SSH server, use key-based auth
   - Disable password authentication
   - Restrict access to specific directory

2. **FTPS**
   - FTP over TLS 1.2+
   - Valid certificate required
   - Enforce encrypted authentication

3. **HTTPS upload portal**
   - Web-based file upload
   - TLS 1.2+ required
   - MFA for authentication

**Prohibited:** Plain FTP, unencrypted HTTP

---

### "I need to configure TLS on a web server"

**Minimum Configuration:**
```nginx
# Nginx example
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305';
ssl_prefer_server_ciphers on;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

**Testing:**
- SSL Labs: https://www.ssllabs.com/ssltest/
- Target Grade: A or A+

**Apache example:**
```apache
SSLProtocol -all +TLSv1.2 +TLSv1.3
SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384
SSLHonorCipherOrder on
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
```

---

### "I suspect a private key has been compromised"

**IMMEDIATE ACTIONS:**
1. Contact Security Team: security@[organization].com or [phone]
2. DO NOT delete any evidence
3. Document: When discovered, how discovered, what key
4. Isolate affected systems if ongoing unauthorized access suspected

**Follow incident response procedures in Appendix C**

---

### "A certificate is about to expire"

**30 Days Before Expiration:**
1. Generate new CSR (can reuse private key if NOT compromised, but new key preferred)
2. Submit to CA for renewal
3. Test new certificate in staging/development
4. Schedule deployment before expiration

**Certificate Expired (Emergency):**
1. Generate emergency certificate immediately
2. Deploy ASAP to restore service
3. Notify stakeholders of outage
4. Conduct post-mortem: Why did monitoring fail?

---

### "I need to hash passwords in my application"

**Use these algorithms (in priority order):**

**1. Argon2id** (Preferred)
```python
# Python example
import argon2
ph = argon2.PasswordHasher(memory_cost=65536, time_cost=3, parallelism=4)
hash = ph.hash("password")
ph.verify(hash, "password")
```

**2. bcrypt**
```python
# Python example
import bcrypt
hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
bcrypt.checkpw(password.encode('utf-8'), hash)
```

**Requirements:**
- Always use unique salt per password
- Never store passwords in plaintext
- Never use plain SHA-256/MD5 for passwords

---

### "I need to generate an API key"

**Requirements:**
- 256-bit entropy minimum (32 bytes)
- Use cryptographically secure random generator

**Generation Examples:**

```python
# Python
import secrets
api_key = secrets.token_urlsafe(32)  # 32 bytes = 256 bits
```

```javascript
// Node.js
const crypto = require('crypto');
const apiKey = crypto.randomBytes(32).toString('hex');
```

```bash
# Command line
openssl rand -hex 32
```

**Management:**
- Store in secrets manager (Vault, AWS Secrets Manager, Azure Key Vault)
- Rotate every 90 days
- Never commit to version control

---

## D.2 Algorithm Quick Reference

### Symmetric Encryption
✅ **USE:** AES-256-GCM, ChaCha20-Poly1305
❌ **NEVER:** DES, 3DES, RC4

### Asymmetric Encryption
✅ **USE:** RSA ≥3072-bit, ECDSA P-256+, Ed25519
❌ **NEVER:** RSA <2048-bit, DSA

### Hashing
✅ **USE:** SHA-256, SHA-384, SHA-512, SHA-3
❌ **NEVER:** MD5, SHA-1

### Password Hashing
✅ **USE:** Argon2id, bcrypt (cost ≥12)
❌ **NEVER:** Plain SHA-256, MD5, unsalted hashes

### TLS
✅ **USE:** TLS 1.3 (preferred), TLS 1.2 (minimum)
❌ **NEVER:** TLS 1.1, TLS 1.0, SSL 3.0, SSL 2.0

---

## D.3 Key Rotation Schedule

| Key Type | Rotation Frequency |
|----------|-------------------|
| **TLS Certificates** | Annual (90 days recommended) |
| **API Keys** | 90 days |
| **Database Encryption Keys** | Annual |
| **SSH Keys** | Annual + on personnel change |
| **Service Account Passwords** | 90 days |
| **User Passwords** | 90-365 days |

---

## D.4 Useful Commands and Tools

### Certificate Operations

**View certificate details:**
```bash
openssl x509 -in certificate.crt -text -noout
```

**Check certificate expiration:**
```bash
openssl x509 -in certificate.crt -noout -dates
```

**Test TLS connection:**
```bash
openssl s_client -connect example.com:443 -servername example.com
```

**Check certificate on server:**
```bash
echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -dates
```

**Generate self-signed certificate (testing only):**
```bash
openssl req -x509 -newkey rsa:3072 -keyout key.pem -out cert.pem -days 365 -nodes
```

### SSH Operations

**Generate SSH key (Ed25519 - preferred):**
```bash
ssh-keygen -t ed25519 -C "user@example.com"
```

**Generate SSH key (RSA):**
```bash
ssh-keygen -t rsa -b 3072 -C "user@example.com"
```

**Test SSH configuration:**
```bash
ssh -T git@github.com  # Example for testing
```

### Hashing and Verification

**Generate SHA-256 hash:**
```bash
sha256sum file.txt
openssl dgst -sha256 file.txt
```

**Verify file integrity:**
```bash
sha256sum -c checksums.txt
```

### Random Number Generation

**Generate random password:**
```bash
openssl rand -base64 32
```

**Generate random hex string:**
```bash
openssl rand -hex 16
```

---

## D.5 Testing and Validation Tools

### Online Tools

| Tool | Purpose | URL |
|------|---------|-----|
| **SSL Labs Server Test** | Test TLS configuration | https://www.ssllabs.com/ssltest/ |
| **Mozilla Observatory** | Security header check | https://observatory.mozilla.org/ |
| **testssl.sh** | Command-line TLS scanner | https://testssl.sh/ |

### Command-Line Tools

**nmap with SSL scripts:**
```bash
nmap --script ssl-enum-ciphers -p 443 example.com
```

**testssl.sh (comprehensive TLS test):**
```bash
./testssl.sh https://example.com
```

**Check specific cipher support:**
```bash
nmap --script ssl-enum-ciphers -p 443 example.com
```

---

## D.6 Configuration Templates

### Strong SSH Configuration (/etc/ssh/sshd_config)

```
Protocol 2
HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key

KexAlgorithms curve25519-sha256,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com

PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
ChallengeResponseAuthentication no
```

### Strong PostgreSQL Connection (postgresql.conf)

```
ssl = on
ssl_ciphers = 'HIGH:MEDIUM:+3DES:!aNULL'
ssl_prefer_server_ciphers = on
ssl_min_protocol_version = 'TLSv1.2'
```

### MySQL Secure Connection (my.cnf)

```
[mysqld]
require_secure_transport=ON
ssl-ca=/path/to/ca.pem
ssl-cert=/path/to/server-cert.pem
ssl-key=/path/to/server-key.pem
tls_version=TLSv1.2,TLSv1.3
```

---

## D.7 Troubleshooting Common Issues

### "SSL Handshake Failed"

**Possible Causes:**
- Certificate expired → Check expiration date
- Certificate name mismatch → Check Common Name/SAN
- Weak cipher suites → Update server configuration
- TLS version incompatibility → Enable TLS 1.2+

**Debugging:**
```bash
openssl s_client -connect server:443 -servername server.example.com
# Look for error messages in output
```

### "Certificate Verification Failed"

**Possible Causes:**
- Incomplete certificate chain → Install intermediate certificates
- Self-signed certificate → Install CA certificate on client
- Certificate revoked → Check OCSP/CRL status

**Check certificate chain:**
```bash
openssl s_client -connect server:443 -showcerts
```

### "Authentication Failed (SSH)"

**Possible Causes:**
- Wrong key → Verify ~/.ssh/authorized_keys on server
- Key permissions wrong → `chmod 600 ~/.ssh/id_rsa`
- SSH server config → Check PasswordAuthentication, PubkeyAuthentication settings

**Debug SSH connection:**
```bash
ssh -v user@server  # Verbose mode
ssh -vv user@server  # More verbose
ssh -vvv user@server  # Maximum verbosity
```

---

## D.8 When to Contact Security Team

**IMMEDIATELY contact Security Team for:**
- Suspected key compromise
- Certificate compromise
- Critical cryptographic vulnerability disclosed
- Encryption failure exposing data
- Active security incident

**Contact for guidance:**
- Exception requests
- New cryptographic implementation
- Unclear policy requirements
- Cryptographic product evaluation

**Security Team Contact:**
- **Email:** security@[organization].com
- **Phone:** [phone number]
- **Emergency (24/7):** [on-call phone]
- **Ticketing:** [system/portal]

---

## D.9 Compliance Quick Checklist

### Before Deploying a New Service

☐ TLS 1.2+ configured (TLS 1.3 preferred)
☐ Valid certificate from trusted CA
☐ Strong cipher suites enabled
☐ Weak protocols/ciphers disabled
☐ HSTS header configured (for HTTPS)
☐ Certificate monitoring configured
☐ Data encrypted at rest (if storing sensitive data)
☐ Authentication uses MFA (if applicable)
☐ Passwords hashed with Argon2id/bcrypt
☐ API keys managed in secrets manager
☐ SSH key-based authentication (if applicable)
☐ Logs configured for security monitoring

### Monthly Security Checks

☐ Review certificate expiration (30-day window)
☐ Check for new cryptographic vulnerabilities
☐ Verify key rotation compliance
☐ Review exception register
☐ Check monitoring alerts for crypto issues

### Quarterly Reviews

☐ Certificate inventory audit
☐ TLS configuration scans
☐ Compliance dashboard review
☐ Exception register review
☐ Training completion verification

---

## D.10 Emergency Procedures

### Certificate Expiration Causing Outage

1. Generate emergency certificate (self-signed if necessary)
2. Deploy immediately to restore service
3. Obtain proper certificate from CA within 24 hours
4. Post-mortem: Fix monitoring gap

### Key Compromise Suspected

1. Call Security Team immediately: [phone]
2. Do not destroy evidence
3. Document discovery
4. Follow Appendix C procedures

### Critical Vulnerability Disclosed

1. Check security team notifications
2. Inventory affected systems
3. Prioritize patching
4. Follow timeline in Appendix C

---

## D.11 Acronyms and Abbreviations

| Acronym | Full Name |
|---------|-----------|
| **AEAD** | Authenticated Encryption with Associated Data |
| **AES** | Advanced Encryption Standard |
| **CA** | Certificate Authority |
| **CBC** | Cipher Block Chaining |
| **CMEK** | Customer-Managed Encryption Key |
| **CRL** | Certificate Revocation List |
| **CSR** | Certificate Signing Request |
| **DH** | Diffie-Hellman |
| **ECC** | Elliptic Curve Cryptography |
| **ECDH** | Elliptic Curve Diffie-Hellman |
| **ECDSA** | Elliptic Curve Digital Signature Algorithm |
| **GCM** | Galois/Counter Mode |
| **HMAC** | Hash-based Message Authentication Code |
| **HSM** | Hardware Security Module |
| **HTTPS** | HTTP Secure (HTTP over TLS) |
| **KMS** | Key Management System |
| **LUKS** | Linux Unified Key Setup |
| **MAC** | Message Authentication Code |
| **MFA** | Multi-Factor Authentication |
| **OCSP** | Online Certificate Status Protocol |
| **PFS** | Perfect Forward Secrecy |
| **PKI** | Public Key Infrastructure |
| **RSA** | Rivest-Shamir-Adleman |
| **SAN** | Subject Alternative Name |
| **SFTP** | SSH File Transfer Protocol |
| **SSH** | Secure Shell |
| **TDE** | Transparent Data Encryption |
| **TLS** | Transport Layer Security |
| **TOTP** | Time-based One-Time Password |

---

## D.12 Additional Resources

### Internal Resources
- **Full Policy:** ISMS-POL-A.8.24 (all sections)
- **Implementation Status:** ISMS-IMP-A.8.24
- **Exception Request Form:** Appendix B
- **Incident Response:** Appendix C
- **Technical Standards:** Appendix A

### External Standards
- **NIST Cryptographic Standards:** https://csrc.nist.gov/publications
- **OWASP Cryptographic Storage Cheat Sheet:** https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- **Mozilla SSL Configuration Generator:** https://ssl-config.mozilla.org/
- **CA/Browser Forum:** https://cabforum.org/

### Training
- **Security Awareness Training:** [Internal LMS link]
- **Cryptography Fundamentals:** [Internal training or recommended courses]
- **Certificate Management Training:** [Internal training]

---

## D.13 Policy Version Reference

**This Quick Reference applies to:**
- Policy Version: 1.0
- Effective Date: [Date]
- Last Updated: [Date]

**If policy version differs, refer to the current policy document.**

---

**Questions or need help?**
Contact the Information Security Team:
- **Email:** security@[organization].com
- **Phone:** [phone]
- **Documentation:** [Wiki/SharePoint link]

---

**End of Appendix D - Quick Reference Guide**

*"Make it work, make it right, make it fast, make it simple. In cryptography, skip straight to 'make it right'."*  
*— Kent Beck's wisdom, adapted for security-critical systems*