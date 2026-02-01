**ISMS-CTX-A.8.24 — Kryptographische Landschaft-Referenz**
**Industrie-Algorithmen und Cipher Suite Übersicht (Nicht-ISMS Technische Referenz)**

---

**Dokumentenlenkung**

| Feld | Wert |
|------|------|
| **Dokumenten Titel** | Kryptographische Landschaft-Referenz |
| **Dokumententyp** | Intern — Technische Referenz (Nicht-ISMS) |
| **Dokument-ID** | ISMS-CTX-A.8.24 |
| **Ersteller/in** | Chief Information Security Officer (CISO) |
| **Dokumenteneigentümer/in** | Chief Executive Officer (CEO) |
| **Freigabe durch** | Geschäftsleitung (GL) |
| **Erstellt** | [Date] |
| **Version** | 1.0 |
| **Versionsdatum** | [Zu bestimmen] |
| **Klassifizierung** | Intern |
| **Status** | Entwurf |

**Versions-Verzeichnis**:

| Version | Datum | Autor | Änderungsvermerk |
|---------|-------|-------|------------------|
| 1.0 | [Date] | CISO | Initiale Richtlinie für ISO 27001:2022 Erstzertifizierung |

**Review-Zyklus**: Nach Bedarf (bei Industrie-Standards-Evolution)  
**Nächstes Review-Datum**: [Datum + 12 Monate]  
**Freigabe**: Security Architecture / Kryptographie SME (technische Referenz, keine ISMS-Freigabe erforderlich)

**Verteilung**: Security Engineering, System Architects, Development Teams (zur Kenntnisnahme)

---

⚠️ **WICHTIG – NICHT-ISMS TECHNISCHES SUPPORT-DOKUMENT**

Dieses Dokument dient ausschliesslich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Teil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert KEINE obligatorischen kryptographischen Kontrollen.
- Dieses Dokument etabliert KEINE bindenden Anforderungen, Deadlines, KPIs oder SLAs.
- Dieses Dokument schreibt NICHT die Verwendung, das Verbot oder die Konfiguration spezifischer kryptographischer Algorithmen, Ciphers, Protokolle, Tools oder Plattformen vor.
- Dieses Dokument überschreibt oder erweitert KEINE ISMS-Richtlinie.


Alle bindenden kryptographischen Anforderungen, Verpflichtungen und Governance-Entscheidungen sind ausschliesslich in **ISMS-POL-A.8.24 (Kryptografie)** und anderen genehmigten ISMS-Dokumentationen definiert.

Dieses Dokument dient ausschliesslich als technische Referenz für:

- Beschreibung häufig anzutreffender kryptographischer Algorithmen und Cipher Suites
- Verfolgung der Evolution von Industrie-Standards und Algorithmen-Lebenszyklus-Status
- Unterstützung der Sensibilisierung für kryptographische Agilität
- Information technischer Diskussionen und zukünftiger Implementierungsplanung
- **Dieses Dokument darf NICHT als Audit-Nachweis für Implementierungen verwendet werden**


Die Verwendung dieses Dokuments impliziert keine Implementierung, Compliance oder operative Reife.

**Kritische Positionierungs-Erklärung**:
Dieses Dokument übersteigt absichtlich den Detaillierungsgrad, der für ISO/IEC 27001 Policy-Dokumentation erforderlich ist. Sein Zweck ist ausschliesslich technische Sensibilisierung. Es dürfen keine Audit-Schlussfolgerungen aus der Präsenz, Absenz oder Klassifizierung von Algorithmen, Ciphers oder Parametern in diesem Dokument gezogen werden.

---

# Dokumentenzweck und Geltungsbereich

## Zweck

Dieses Dokument bietet eine technische Übersicht der kryptographischen Algorithmen-Landschaft, die häufig in modernen Informationssystemen anzutreffen ist. Es dient zur Unterstützung von:

- Technischem Bewusstsein für kryptographische Optionen
- Verständnis von Algorithmen-Lebenszyklus und -Reife
- Kontext für kryptographische Entscheidungsfindung
- Zukünftiger Implementierungsplanungs-Diskussionen


## Was dieses Dokument NICHT ist

Dieses Dokument:

- Definiert NICHT [Organisation]s genehmigte oder verbotene Algorithmen
- Etabliert KEINE obligatorischen Implementierungsanforderungen
- Schafft KEINE Compliance-Verpflichtungen oder Audit-Kriterien
- Ersetzt NICHT ISMS-POL-A.8.24 Richtlinien-Anforderungen
- Schreibt KEINE spezifischen Cipher Suite Konfigurationen vor
- Etabliert KEINE Key Management Verfahren


## Beziehung zum ISMS

Dieses Dokument ist eine **nicht-bindende technische Referenz**. Alle kryptographischen Kontrollanforderungen sind ausschliesslich in ISMS-POL-A.8.24 definiert.

Implementierungsentscheidungen werden durch separate Verfahren dokumentiert, basierend auf Risikobewertung, operativem Kontext und regulatorischen Anforderungen.

## Inhaltsorganisation

Diese Referenz organisiert kryptographische Algorithmen nach Funktion:

- Symmetrische Verschlüsselung (Datenvertraulichkeit)
- Asymmetrische Verschlüsselung (Key Exchange, digitale Signaturen)
- Hash-Funktionen (Datenintegrität, Authentifizierung)
- TLS/SSL Cipher Suites (sichere Kommunikation)
- Schlüssellängen und Algorithmen-Reifegrad-Status


---

# Symmetrische Verschlüsselungs-Algorithmen

## Block Ciphers

Symmetrische Block Ciphers, die häufig in modernen Systemen anzutreffen sind:

| Algorithmus | Block-Grösse | Schlüssellängen | Status | Häufige Anwendungsfälle |
|-------------|--------------|-----------------|--------|-------------------------|
| **AES** (Advanced Encryption Standard) | 128-bit | 128, 192, 256-bit | Modern, weit verbreitet | Datenverschlüsselung, TLS, VPN, Festplatten-Verschlüsselung |
| **ChaCha20** | 64-byte Stream | 256-bit | Modern, mobil-optimiert | TLS (mobile Geräte), VPN (WireGuard) |
| **3DES** (Triple DES) | 64-bit | 168-bit (effektiv 112-bit) | Legacy, deprecated | Nur Legacy-System-Support |
| **DES** (Data Encryption Standard) | 64-bit | 56-bit | Obsolet, gebrochen | Nur historische Referenz |
| **Blowfish** | 64-bit | 32-448 bit | Legacy | Historische Referenz, ersetzt durch AES |
| **Twofish** | 128-bit | 128, 192, 256-bit | Modern aber weniger verbreitet | Alternative zu AES |

**Industrie-Beobachtungen**:

- AES ist der dominante Standard für symmetrische Verschlüsselung global
- ChaCha20 gewinnt an Akzeptanz in ressourcenbeschränkten Umgebungen
- 3DES von NIST deprecated (nach 2023 in den meisten Kontexten nicht mehr erlaubt)
- DES gilt seit Ende der 1990er Jahre als kryptographisch gebrochen


## Block Cipher Betriebsmodi

Häufige Modi für den Betrieb von Block Ciphers:

| Modus | Authentifizierung | Parallelisierbar | Status | Hinweise |
|-------|-------------------|------------------|--------|----------|
| **GCM** (Galois/Counter Mode) | Ja (AEAD) | Ja (Ver-/Entschlüsselung) | Modern, empfohlen | Authenticated Encryption, TLS 1.2+ Standard |
| **CCM** (Counter with CBC-MAC) | Ja (AEAD) | Teilweise | Modern | Verwendet in Constrained Environments |
| **CTR** (Counter Mode) | Nein | Ja | Modern | Benötigt separate Authentifizierung (HMAC) |
| **CBC** (Cipher Block Chaining) | Nein | Teilweise | Legacy | Anfällig für Padding Oracle Angriffe |
| **ECB** (Electronic Codebook) | Nein | Ja | Obsolet | Deterministisch, nicht empfohlen |
| **XTS** | Nein | Ja | Modern | Festplatten-Verschlüsselung (BitLocker, dm-crypt) |

**Industrie-Beobachtungen**:

- AEAD-Modi (GCM, CCM) stark bevorzugt für neue Implementierungen
- CBC-Modus benötigt sorgfältige Implementierung zur Vermeidung von Schwachstellen
- ECB-Modus bietet unzureichende Sicherheit für die meisten Applikationen


## Stream Ciphers

| Cipher | Schlüssellänge | Status | Häufige Anwendungsfälle |
|--------|----------------|--------|-------------------------|
| **ChaCha20-Poly1305** | 256-bit | Modern | TLS 1.3, mobiler VPN, moderne Protokolle |
| **RC4** (Rivest Cipher 4) | 40-2048 bit | Obsolet, gebrochen | Nur historische Referenz |
| **Salsa20** | 128, 256-bit | Modern | ChaCha20 Vorgänger |

**Industrie-Beobachtungen**:

- RC4 formal deprecated in allen grösseren Protokollen (TLS, WPA, etc.)
- ChaCha20 zunehmend als AES-Alternative für Performance adoptiert


---

# Asymmetrische Verschlüsselungs-Algorithmen

## Public Key Algorithmen

Asymmetrische Algorithmen, die häufig anzutreffen sind:

| Algorithmus | Schlüssellängen | Status | Primäre Anwendungsfälle |
|-------------|-----------------|--------|-------------------------|
| **RSA** (Rivest-Shamir-Adleman) | 2048, 3072, 4096-bit | Modern (≥2048-bit) | TLS-Zertifikate, SSH, E-Mail-Verschlüsselung, Code Signing |
| **ECDSA** (Elliptic Curve DSA) | P-256, P-384, P-521 | Modern | TLS-Zertifikate, SSH, mobile/IoT, Blockchain |
| **EdDSA** (Edwards-curve DSA) | Ed25519 (256-bit äquivalent) | Modern | SSH Keys, moderne Protokolle, Cryptocurrency |
| **DH** (Diffie-Hellman) | 2048, 3072, 4096-bit | Modern (≥2048-bit) | Key Exchange (Legacy) |
| **ECDH** (Elliptic Curve DH) | P-256, P-384, P-521, X25519 | Modern | TLS 1.2+, Key Exchange |
| **DSA** (Digital Signature Algorithm) | 2048, 3072-bit | Legacy | Nur ältere Systeme, ersetzt durch RSA/ECDSA |
| **RSA-1024** | 1024-bit | Obsolet, deprecated | Nur historische Referenz |

**Industrie-Beobachtungen**:

- RSA-2048 Minimum für neue Deployments (NIST, CA/Browser Forum)
- RSA-3072 zunehmend adoptiert für langlebige Schlüssel (5+ Jahre Lebensdauer)
- ECC (ECDSA, EdDSA) bietet äquivalente Sicherheit mit kleineren Schlüsselgrössen
- Ed25519 gewinnt an Akzeptanz für SSH und moderne Protokolle


## Schlüssellängen-Äquivalenz

Ungefähre Sicherheits-Äquivalenz zwischen Algorithmen-Familien:

| Symmetrisch | RSA/DH | ECC | Hash | Sicherheits-Bits |
|-------------|--------|-----|------|------------------|
| 3DES (2-key) | 1024 | 160 | SHA-1 | ~80 bits (deprecated) |
| AES-128 | 3072 | 256 (P-256) | SHA-256 | ~128 bits |
| AES-192 | 7680 | 384 (P-384) | SHA-384 | ~192 bits |
| AES-256 | 15360 | 521 (P-521) | SHA-512 | ~256 bits |

**Quelle**: NIST SP 800-57 Part 1 Rev. 5

---

# Hash-Funktionen und Message Authentication

## Kryptographische Hash-Funktionen

Hash-Funktionen, die häufig anzutreffen sind:

| Algorithmus | Output-Grösse | Status | Häufige Anwendungsfälle |
|-------------|---------------|--------|-------------------------|
| **SHA-256** | 256-bit | Modern | Digitale Signaturen, Zertifikate, Password Storage (mit KDF), Blockchain |
| **SHA-384** | 384-bit | Modern | Hochsicherheits-Applikationen, Langzeit-Signaturen |
| **SHA-512** | 512-bit | Modern | Hochsicherheits-Applikationen, Password Hashing (mit KDF) |
| **SHA-3** (Keccak) | 224, 256, 384, 512-bit | Modern | Alternative zu SHA-2, Blockchain |
| **BLAKE2** | 256, 512-bit | Modern | High-Performance Hashing, Password Storage |
| **SHA-1** | 160-bit | Obsolet, gebrochen | Nur historische Referenz, deprecated 2017 |
| **MD5** | 128-bit | Obsolet, gebrochen | Nur historische Referenz, deprecated 2004 |

**Industrie-Beobachtungen**:

- SHA-256 Minimum für neue Implementierungen (Zertifikate, Signaturen)
- SHA-1 deprecated für Zertifikate (2017), Git-Migration laufend
- MD5 gilt als kryptographisch gebrochen, nur für Nicht-Sicherheits-Verwendung geeignet (Checksummen)


## Message Authentication Codes (MAC)

| Algorithmus | Basiert auf | Output-Grösse | Status |
|-------------|-------------|---------------|--------|
| **HMAC-SHA256** | SHA-256 | 256-bit | Modern |
| **HMAC-SHA384** | SHA-384 | 384-bit | Modern |
| **HMAC-SHA512** | SHA-512 | 512-bit | Modern |
| **Poly1305** | ChaCha20 | 128-bit | Modern (mit ChaCha20) |
| **HMAC-SHA1** | SHA-1 | 160-bit | Legacy, wird ausgemustert |
| **HMAC-MD5** | MD5 | 128-bit | Obsolet |

## Password Hashing Funktionen

Spezialisierte Funktionen für Password Storage:

| Funktion | Typ | Status | Hinweise |
|----------|-----|--------|----------|
| **Argon2** (Argon2id) | Password KDF | Modern, empfohlen | Gewinner der Password Hashing Competition 2015 |
| **bcrypt** | Password KDF | Modern | Weit verbreitet, automatischer Work Factor |
| **scrypt** | Password KDF | Modern | Memory-Hard Function |
| **PBKDF2-HMAC-SHA256** | Password KDF | Modern | NIST genehmigt, niedrigerer Cost Factor |
| **SHA-256 (raw)** | General Hash | Ungeeignet | Zu schnell für Password Storage |
| **MD5 (raw)** | General Hash | Obsolet | Ungeeignet für Passwords |

**Industrie-Beobachtungen**:

- Password Hashing benötigt Key Derivation Functions (KDFs) mit Work Factor
- Raw Hash-Funktionen (SHA-256, MD5) ungeeignet für Password Storage
- Argon2id empfohlen für neue Implementierungen (OWASP)


---

# TLS/SSL Cipher Suites

**Wichtiger Hinweis zu Cipher Suite Auflistungen**:
Die untenstehenden TLS Cipher Suite Beispiele sind illustrativ und nicht-exhaustiv. Sie dienen zur Erklärung von häufigen Industrie-Konstruktionen und Namenskonventionen. Sie repräsentieren NICHT genehmigte, geforderte oder erwartete Konfigurationen innerhalb von [Organisation].

## TLS 1.3 Cipher Suites

TLS 1.3 vereinfachtes Cipher Suite Design (5 standardisierte Suites):

| Cipher Suite | Key Exchange | Bulk Cipher | Status |
|--------------|--------------|-------------|--------|
| **TLS_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | Modern, empfohlen |
| **TLS_AES_128_GCM_SHA256** | ECDHE | AES-128-GCM | Modern, empfohlen |
| **TLS_CHACHA20_POLY1305_SHA256** | ECDHE | ChaCha20-Poly1305 | Modern, mobil-optimiert |
| **TLS_AES_128_CCM_SHA256** | ECDHE | AES-128-CCM | Modern, IoT/Constrained |
| **TLS_AES_128_CCM_8_SHA256** | ECDHE | AES-128-CCM (8-byte Tag) | Modern, Constrained Devices |

**Industrie-Beobachtungen**:

- TLS 1.3 entfernt Cipher Suite Negotiation-Komplexität
- Alle TLS 1.3 Suites bieten Forward Secrecy (ECDHE obligatorisch)
- Alle TLS 1.3 Suites bieten Authenticated Encryption (AEAD)


## TLS 1.2 Cipher Suites (Ausgewählte häufige Beispiele)

TLS 1.2 Cipher Suite Beispiele (nicht-exhaustiv, nur beschreibend):

| Cipher Suite | Key Exchange | Authentifizierung | Bulk Cipher | MAC | Status |
|--------------|--------------|-------------------|-------------|-----|--------|
| **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384** | ECDHE | RSA | AES-256-GCM | (AEAD) | Modern, weit verbreitet |
| **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256** | ECDHE | RSA | AES-128-GCM | (AEAD) | Modern, weit verbreitet |
| **TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256** | ECDHE | RSA | ChaCha20-Poly1305 | (AEAD) | Modern, mobil |
| **TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384** | ECDHE | ECDSA | AES-256-GCM | (AEAD) | Modern, ECC-Zertifikate |
| **TLS_RSA_WITH_AES_256_GCM_SHA384** | RSA | RSA | AES-256-GCM | (AEAD) | Legacy, keine Forward Secrecy |
| **TLS_RSA_WITH_AES_128_CBC_SHA256** | RSA | RSA | AES-128-CBC | SHA-256 | Legacy, Padding Oracle Risiko |
| **TLS_RSA_WITH_3DES_EDE_CBC_SHA** | RSA | RSA | 3DES-CBC | SHA-1 | Obsolet, deprecated |
| **TLS_RSA_WITH_RC4_128_SHA** | RSA | RSA | RC4 | SHA-1 | Obsolet, gebrochen |

**Industrie-Beobachtungen**:

- ECDHE bietet Forward Secrecy (empfohlen)
- AEAD-Modi (GCM, Poly1305) bevorzugt gegenüber CBC + HMAC
- RSA Key Exchange (kein ECDHE) fehlt Forward Secrecy
- CBC-Modus anfällig für Padding Oracle Angriffe bei nicht sorgfältiger Implementierung


## Deprecated/Obsolete Protokolle und Cipher Suites

| Protokoll/Cipher | Deprecated | Grund |
|------------------|------------|-------|
| **SSL v2** | 2011 | Multiple kryptographische Fehler |
| **SSL v3** | 2015 | POODLE-Angriff, schwache Verschlüsselung |
| **TLS 1.0** | 2020 | Veraltete Kryptographie, BEAST-Angriff |
| **TLS 1.1** | 2020 | Veraltete Kryptographie |
| **RC4 Cipher** | 2015 | Biases im Keystream, praktische Angriffe |
| **3DES Cipher** | 2023 | Sweet32-Angriff, 64-bit Block-Grösse |
| **Export-Grade Ciphers** | 1990er-2015 | Absichtlich geschwächt (40-56 bit), gebrochen |
| **NULL Encryption** | Immer | Keine Verschlüsselung, nur Authentifizierung |
| **Anonymous DH (ADH)** | Immer | Keine Authentifizierung, MITM-anfällig |

---

# Schlüssellängen und Algorithmen-Lebenszyklus

## Häufig referenzierte Schlüssellängen in Industrie-Leitlinien

Häufig referenzierte Schlüssellängen in Industrie-Leitlinien (NIST, BSI, ENISA):

| Algorithmen-Familie | Minimale Schlüssellänge | Verwendung bis | Hinweise |
|---------------------|------------------------|----------------|----------|
| **RSA (Signing, Key Exchange)** | 2048-bit | ~2030 | 3072-bit für Schlüssel >2030 |
| **RSA (Langzeit-Schlüssel)** | 3072-bit | Nach 2030 | Root CAs, Code Signing |
| **Diffie-Hellman** | 2048-bit | ~2030 | 3072-bit für zukünftige Verwendung |
| **ECDSA/ECDH** | P-256 (256-bit) | Nach 2030 | P-384 für Hochsicherheit |
| **AES** | 128-bit | Nach 2030 | 256-bit für Hochsicherheit |
| **Hash-Funktionen** | SHA-256 | Nach 2030 | SHA-384 für Hochsicherheit |

**Quelle**: NIST SP 800-57 Part 1 Rev. 5, BSI TR-02102-1

## Algorithmen-Lebenszyklus-Status

Klassifizierung von Algorithmen-Reife und Adoptions-Status:

| Status | Definition | Beispiele |
|--------|------------|-----------|
| **Modern** | Aktuelle Best Practice, aktiv deployed | AES, RSA-2048+, ECDSA P-256+, SHA-256, TLS 1.3 |
| **Weit verbreitet** | Ausgereift, stabil, breites Deployment | TLS 1.2, RSA-2048, SHA-256, ChaCha20 |
| **Legacy** | Alternd, wird ersetzt, limitiertes neues Deployment | 3DES, DSA, SHA-1 (Nicht-Zertifikate), TLS 1.1 |
| **Deprecated** | Nicht mehr empfohlen, Ausmusterung läuft | SSL v3, TLS 1.0, RC4, MD5-Signaturen |
| **Obsolet** | Kryptographisch gebrochen oder stark geschwächt | DES, MD5 (Sicherheits-Verwendung), RC4, SHA-1 (Zertifikate) |
| **Emerging** | Standardisiert aber limitiertes Deployment | Post-Quantum Algorithmen (ML-KEM, ML-DSA) |

## Post-Quantum Cryptography Status

NIST Post-Quantum Cryptography (PQC) Standardisierung:

| Algorithmus | Typ | Status (2024-2025) | Hinweise |
|-------------|-----|-------------------|----------|
| **ML-KEM** (Kyber) | Key Encapsulation | FIPS 203 publiziert 2024 | Key Exchange, Hybrid-Modus mit ECDH |
| **ML-DSA** (Dilithium) | Digital Signature | FIPS 204 publiziert 2024 | Signaturen, Hybrid-Modus mit ECDSA/RSA |
| **SLH-DSA** (SPHINCS+) | Digital Signature | FIPS 205 publiziert 2024 | Stateless Hash-basierte Signaturen |
| **FN-DSA** (Falcon) | Digital Signature | In Evaluation | Lattice-basiert, kompakte Signaturen |

**Industrie-Beobachtungen**:

- Post-Quantum Algorithmen werden standardisiert aber noch nicht weit deployed
- Hybrid-Modi (PQC + klassisch) erwartet während Übergangsperiode
- TLS 1.3 Hybrid Key Exchange (X25519 + ML-KEM) in Entwicklung
- Certificate Authorities beginnen PQC Trial-Ausstellung


---

# Zertifikats-Gültigkeit und Lebenszyklus-Trends

## Historische Zertifikats-Gültigkeits-Evolution

Public TLS-Zertifikats-Maximum-Gültigkeitsperioden:

| Periode | Maximale Gültigkeit | Autorität |
|---------|---------------------|-----------|
| Vor 2011 | Kein definiertes Limit | Vendor-Ermessen |
| 2011-2015 | 60 Monate (5 Jahre) | CA/Browser Forum |
| 2015-2017 | 39 Monate (~3 Jahre) | CA/Browser Forum Ballot 193 |
| 2017-2020 | 825 Tage (~27 Monate) | CA/Browser Forum Ballot 193 |
| 2020-heute | 398 Tage (~13 Monate) | CA/Browser Forum Ballot SC-31 |

## Zukünftige Zertifikats-Gültigkeit (Ballot SC-081v3)

CA/Browser Forum Ballot SC-081v3 (verabschiedet April 2025):

| Inkraftsetzungsdatum | Maximale Gültigkeit | DCV-Wiederverwendungs-Periode |
|----------------------|---------------------|-------------------------------|
| 15. März 2026 | 200 Tage | 200 Tage |
| 15. März 2027 | 100 Tage | 100 Tage |
| 15. März 2029 | 47 Tage | 10 Tage |

**Industrie-Beobachtungen**:

- Zertifikats-Lebenszeiten reduzieren sich zur Verbesserung von Sicherheit und Agilität
- Kürzere Lebenszeiten erhöhen die Wichtigkeit von automatisiertem Lifecycle Management
- Private/interne PKI nicht Gegenstand von CA/Browser Forum Anforderungen


**Hinweis zu interner PKI**: Interne Zertifikats-Richtlinien werden durch Risikobewertung und operativen Kontext bestimmt und nicht automatisch von Public-Trust-Anforderungen abgeleitet. Organisationen können kürzere oder längere Lebenszeiten basierend auf ihrer spezifischen Sicherheitsposture und operativen Bedürfnissen wählen.

---

# Standards und Referenz-Quellen

## Autoritative Standards-Organisationen

| Organisation | Fokusbereich | Schlüssel-Publikationen |
|--------------|-------------|------------------------|
| **NIST** (National Institute of Standards and Technology) | Kryptographische Standards (US) | FIPS 140-2/3, SP 800-Serie |
| **BSI** (Bundesamt für Sicherheit in der Informationstechnik) | Kryptographische Standards (Deutschland) | TR-02102-1 bis TR-02102-4 |
| **ENISA** (European Union Agency for Cybersecurity) | Kryptographische Empfehlungen (EU) | Algorithmen-Berichte, Guidelines |
| **IETF** (Internet Engineering Task Force) | Protokoll-Standards | RFCs (TLS, SSH, IPsec) |
| **CA/Browser Forum** | Certificate Authority Standards | Baseline Requirements, Ballots |
| **ISO/IEC JTC 1/SC 27** | Informationssicherheits-Standards | ISO/IEC 18033 (Verschlüsselungs-Algorithmen) |

## Schlüssel-Referenz-Dokumente

**NIST Publikationen**:

- FIPS 140-2/140-3: Security Requirements for Cryptographic Modules
- NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations
- NIST SP 800-57 Part 1 Rev. 5: Key Management Recommendations
- NIST SP 800-131A Rev. 2: Transitioning the Use of Cryptographic Algorithms
- NIST SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards


**BSI Publikationen**:

- TR-02102-1: Kryptographische Verfahren - Empfehlungen und Schlüssellängen
- TR-02102-2: Verwendung von TLS
- TR-02102-3: Geeignete kryptographische Algorithmen
- TR-02102-4: Verwendung von Secure Shell (SSH)


**IETF RFCs**:

- RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2
- RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2
- RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)


**CA/Browser Forum**:

- Baseline Requirements for TLS Certificates
- Extended Validation Guidelines
- Code Signing Requirements
- S/MIME Requirements


## Algorithmen-Deprecation-Tracking

Organisationen verfolgen Algorithmen-Status häufig durch:

- NIST Cryptographic Algorithm Validation Program (CAVP)
- NIST Deprecated Algorithm List
- Browser Vendor Security Policies (Chrome, Firefox, Safari, Edge Root Programs)
- CA/Browser Forum Ballot Tracking
- Vendor Security Bulletins (OpenSSL, Microsoft, Apple, etc.)


---

# Dokumenten-Wartung

## Update-Auslöser

Dieses Referenzdokument kann aktualisiert werden, wenn:

- Grössere Algorithmen-Standardisierung erfolgt (NIST, IETF RFCs)
- Signifikante Algorithmen-Deprecations angekündigt werden
- TLS/SSL Protokoll-Updates publiziert werden
- Post-Quantum Cryptography Deployment-Meilensteine erreicht werden
- CA/Browser Forum Baseline Requirement-Änderungen erfolgen


## Verantwortlichkeit

**Dokumenten-Eigentümer**: Security Architecture / Kryptographie SME  
**Review-Frequenz**: Jährlich oder nach Bedarf  
**Update-Autorität**: Technisches Update (keine ISMS-Freigabe-Prozess)

---

# Beziehung zu ISMS-POL-A.8.24

Dieses Dokument bietet **technischen Kontext**, der informieren kann:

- Sensibilisierung für kryptographische Agilität (ISMS-POL-A.8.24 Abschnitt 2.6)
- Algorithmen-Auswahl-Diskussionen während Implementierungsplanung
- Risikobewertung von Legacy-kryptographischen Systemen
- Verständnis der Industrie-Standards-Evolution


Dieses Dokument:

- Überschreibt oder erweitert NICHT ISMS-POL-A.8.24 Anforderungen
- Etabliert KEINE obligatorischen Algorithmen-Auswahlen
- Schafft KEINE Compliance-Verpflichtungen
- Definiert NICHT genehmigte/verbotene Algorithmen für [Organisation]


Alle kryptographischen Kontrollanforderungen sind ausschliesslich in ISMS-POL-A.8.24 definiert und werden durch separate Verfahren implementiert, basierend auf Risikobewertung und operativem Kontext.

---

**ENDE DES DOKUMENTS**

*Dies ist ein technisches Referenzdokument ausschliesslich zu Sensibilisierungszwecken. Es etabliert keine ISMS-Anforderungen oder schafft Compliance-Verpflichtungen.*

*Where bamboo antennas actually work.* 🎋
