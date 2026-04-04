<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.24-IT-cryptographic-landscape-reference:framework:CTX:a.8.24 -->
**ISMS-CTX-A.8.24 — Riferimento sul panorama crittografico**
**Panoramica degli algoritmi e delle suite di cifratura del settore (Riferimento tecnico non-SGSI)**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento sul panorama crittografico |
| **Tipo di documento** | Interno — Riferimento tecnico (non SGSI) |
| **Identificativo del documento** | ISMS-CTX-A.8.24 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Distribuzione**: Ingegneria della sicurezza, Architetti di sistema, Team di sviluppo (per sensibilizzazione)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. NON fa parte del SGSI e NON sostituisce ISMS-POL-A.8.24. I requisiti vincolanti sono definiti esclusivamente in **ISMS-POL-A.8.24 (Utilizzo della crittografia)**.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce una panoramica tecnica del panorama degli algoritmi crittografici comunemente incontrati nei moderni sistemi informativi. È inteso a supportare:

- La consapevolezza tecnica delle opzioni crittografiche
- La comprensione del ciclo di vita e della maturità degli algoritmi
- Il contesto per il processo decisionale crittografico
- La pianificazione dell'implementazione futura

## Relazione con il SGSI

Questo documento è un **riferimento tecnico non vincolante**. Tutti i requisiti di controllo crittografico sono definiti esclusivamente in ISMS-POL-A.8.24.

## Organizzazione dei contenuti

Questo riferimento organizza gli algoritmi crittografici per funzione:

- Crittografia simmetrica (riservatezza dei dati)
- Crittografia asimmetrica (scambio di chiavi, firme digitali)
- Funzioni di hash (integrità dei dati, autenticazione)
- Suite di cifratura TLS/SSL (comunicazioni sicure)
- Lunghezze delle chiavi e stato di maturità degli algoritmi

---

# Algoritmi di crittografia simmetrica

## Cifrari a blocchi

Algoritmi di cifratura a blocchi simmetrici comunemente incontrati:

| Algoritmo | Dimensione blocco | Lunghezze chiave | Stato | Casi d'uso comuni |
|-----------|-------------------|------------------|-------|-------------------|
| **AES** (Advanced Encryption Standard) | 128-bit | 128, 192, 256-bit | Moderno, ampiamente distribuito | Crittografia dati, TLS, VPN, crittografia disco |
| **ChaCha20** | Flusso 64 byte | 256-bit | Moderno, ottimizzato mobile | TLS (dispositivi mobili), VPN (WireGuard) |
| **3DES** (Triple DES) | 64-bit | 168-bit (efficace 112-bit) | Legacy, deprecato | Solo supporto sistemi legacy |
| **DES** (Data Encryption Standard) | 64-bit | 56-bit | Obsoleto, compromesso | Solo riferimento storico |
| **Blowfish** | 64-bit | 32-448 bit | Legacy | Riferimento storico, sostituito da AES |
| **Twofish** | 128-bit | 128, 192, 256-bit | Moderno ma meno comune | Alternativa ad AES |

**Osservazioni del settore**:

- AES è lo standard dominante per la crittografia simmetrica a livello globale
- ChaCha20 sta guadagnando adozione in ambienti con risorse limitate
- 3DES deprecato da NIST (vietato dopo il 2023 nella maggior parte dei contesti)
- DES considerato crittograficamente compromesso dalla fine degli anni '90

## Modalità operative dei cifrari a blocchi

Modalità comuni per operare con i cifrari a blocchi:

| Modalità | Autenticazione | Parallelizzabile | Stato | Note |
|---------|----------------|------------------|-------|------|
| **GCM** (Modalità Galois/Contatore) | Sì (AEAD) | Sì | Moderna, raccomandata | Crittografia autenticata, default TLS 1.2+ |
| **CCM** (Contatore con CBC-MAC) | Sì (AEAD) | Parziale | Moderna | Ambienti vincolati |
| **CTR** (Modalità Contatore) | No | Sì | Moderna | Richiede autenticazione separata (HMAC) |
| **CBC** (Concatenazione di blocchi cifranti) | No | Parziale | Legacy | Vulnerabile agli attacchi con oracolo di padding |
| **ECB** (Libro dei codici elettronico) | No | Sì | Obsoleto | Deterministico, non raccomandato |
| **XTS** | No | Sì | Moderna | Crittografia disco (BitLocker, dm-crypt) |

**Osservazioni del settore**:

- Le modalità AEAD (GCM, CCM) fortemente preferite per le nuove implementazioni
- La modalità CBC richiede un'implementazione attenta per evitare le vulnerabilità
- La modalità ECB fornisce sicurezza insufficiente per la maggior parte delle applicazioni

## Cifrari di flusso

| Cifrario | Lunghezza chiave | Stato | Casi d'uso comuni |
|---------|------------------|-------|-------------------|
| **ChaCha20-Poly1305** | 256-bit | Moderna | TLS 1.3, VPN mobile, protocolli moderni |
| **RC4** (Rivest Cipher 4) | 40-2048 bit | Obsoleto, compromesso | Solo riferimento storico |
| **Salsa20** | 128, 256-bit | Moderna | Predecessore di ChaCha20 |

---

# Algoritmi di crittografia asimmetrica

## Algoritmi a chiave pubblica

Algoritmi asimmetrici comunemente incontrati:

| Algoritmo | Lunghezze chiave | Stato | Casi d'uso principali |
|-----------|------------------|-------|----------------------|
| **RSA** (Rivest-Shamir-Adleman) | 2048, 3072, 4096-bit | Moderno (≥2048-bit) | Certificati TLS, SSH, crittografia email, firma codice |
| **ECDSA** (DSA su curva ellittica) | P-256, P-384, P-521 | Moderna | Certificati TLS, SSH, mobile/IoT, blockchain |
| **EdDSA** (DSA su curva di Edwards) | Ed25519 (equiv. 256-bit) | Moderna | Chiavi SSH, protocolli moderni, criptovalute |
| **DH** (Diffie-Hellman) | 2048, 3072, 4096-bit | Moderno (≥2048-bit) | Scambio di chiavi (legacy) |
| **ECDH** (DH su curva ellittica) | P-256, P-384, P-521, X25519 | Moderna | TLS 1.2+, scambio di chiavi |
| **DSA** (Digital Signature Algorithm) | 2048, 3072-bit | Legacy | Solo sistemi più vecchi, sostituito da RSA/ECDSA |
| **RSA-1024** | 1024-bit | Obsoleto, deprecato | Solo riferimento storico |

**Osservazioni del settore**:

- RSA-2048 minimo per i nuovi deployment (NIST, CA/Browser Forum)
- RSA-3072 sempre più adottato per le chiavi a lungo termine (durata >5 anni)
- ECC (ECDSA, EdDSA) fornisce sicurezza equivalente con dimensioni di chiave inferiori
- Ed25519 sta guadagnando adozione per SSH e protocolli moderni

## Equivalenza delle lunghezze delle chiavi

Equivalenza di sicurezza approssimativa tra famiglie di algoritmi:

| Simmetrico | RSA/DH | ECC | Hash | Bit di sicurezza |
|-----------|--------|-----|------|-----------------|
| 3DES (2-chiavi) | 1024 | 160 | SHA-1 | ~80 bit (deprecato) |
| AES-128 | 3072 | 256 (P-256) | SHA-256 | ~128 bit |
| AES-192 | 7680 | 384 (P-384) | SHA-384 | ~192 bit |
| AES-256 | 15360 | 521 (P-521) | SHA-512 | ~256 bit |

**Fonte**: NIST SP 800-57 Parte 1 Rev. 5

---

# Funzioni di hash e autenticazione dei messaggi

## Funzioni di hash crittografiche

| Algoritmo | Dimensione output | Stato | Casi d'uso comuni |
|-----------|-------------------|-------|-------------------|
| **SHA-256** | 256-bit | Moderna | Firme digitali, certificati, archiviazione password (con KDF), blockchain |
| **SHA-384** | 384-bit | Moderna | Applicazioni ad alta sicurezza, firme a lungo termine |
| **SHA-512** | 512-bit | Moderna | Applicazioni ad alta sicurezza, hashing password (con KDF) |
| **SHA-3** (Keccak) | 224, 256, 384, 512-bit | Moderna | Alternativa a SHA-2, blockchain |
| **BLAKE2** | 256, 512-bit | Moderna | Hashing ad alte prestazioni, archiviazione password |
| **SHA-1** | 160-bit | Obsoleto, compromesso | Solo riferimento storico, deprecato 2017 |
| **MD5** | 128-bit | Obsoleto, compromesso | Solo riferimento storico, deprecato 2004 |

**Osservazioni del settore**:

- SHA-256 minimo per le nuove implementazioni (certificati, firme)
- SHA-1 deprecato per i certificati (2017), migrazione git in corso
- MD5 considerato crittograficamente compromesso

## Codici di autenticazione dei messaggi (MAC)

| Algoritmo | Basato su | Dimensione output | Stato |
|-----------|-----------|-------------------|-------|
| **HMAC-SHA256** | SHA-256 | 256-bit | Moderna |
| **HMAC-SHA384** | SHA-384 | 384-bit | Moderna |
| **HMAC-SHA512** | SHA-512 | 512-bit | Moderna |
| **Poly1305** | ChaCha20 | 128-bit | Moderna (con ChaCha20) |
| **HMAC-SHA1** | SHA-1 | 160-bit | Legacy, in fase di eliminazione |
| **HMAC-MD5** | MD5 | 128-bit | Obsoleto |

## Funzioni di hashing delle password

Funzioni specializzate per l'archiviazione delle password:

| Funzione | Tipo | Stato | Note |
|----------|------|-------|------|
| **Argon2** (Argon2id) | KDF password | Moderna, raccomandata | Vincitrice del Password Hashing Competition 2015 |
| **bcrypt** | KDF password | Moderna | Ampiamente distribuita, fattore di lavoro automatico |
| **scrypt** | KDF password | Moderna | Funzione a elevato uso di memoria |
| **PBKDF2-HMAC-SHA256** | KDF password | Moderna | Approvata NIST, fattore di costo inferiore |
| **SHA-256 (grezza)** | Hash generale | Non appropriata | Troppo veloce per l'archiviazione delle password |
| **MD5 (grezza)** | Hash generale | Obsoleta | Non adatta per le password |

**Osservazioni del settore**:

- L'hashing delle password richiede funzioni di derivazione delle chiavi (KDF) con fattore di lavoro
- Le funzioni di hash grezze (SHA-256, MD5) non adatte all'archiviazione delle password
- Argon2id raccomandato per le nuove implementazioni (OWASP)

---

# Suite di cifratura TLS/SSL

**Nota importante**: Gli esempi di suite di cifratura seguenti sono illustrativi e non esaustivi. Sono forniti solo per spiegare le costruzioni e le convenzioni di denominazione comuni del settore. Non rappresentano configurazioni approvate, richieste o attese all'interno di [Organizzazione].

## Suite di cifratura TLS 1.3

TLS 1.3 ha semplificato la progettazione delle suite di cifratura (5 suite standardizzate):

| Suite di cifratura | Scambio chiavi | Cifrario di massa | Stato |
|-------------------|----------------|-------------------|-------|
| **TLS_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | Moderna, raccomandata |
| **TLS_AES_128_GCM_SHA256** | ECDHE | AES-128-GCM | Moderna, raccomandata |
| **TLS_CHACHA20_POLY1305_SHA256** | ECDHE | ChaCha20-Poly1305 | Moderna, ottimizzata mobile |
| **TLS_AES_128_CCM_SHA256** | ECDHE | AES-128-CCM | Moderna, IoT/vincolato |
| **TLS_AES_128_CCM_8_SHA256** | ECDHE | AES-128-CCM (tag 8 byte) | Moderna, dispositivi vincolati |

**Osservazioni del settore**:

- TLS 1.3 elimina la complessità della negoziazione delle suite di cifratura
- Tutte le suite TLS 1.3 forniscono la confidenzialità in avanti (ECDHE obbligatorio)
- Tutte le suite TLS 1.3 forniscono la crittografia autenticata (AEAD)

## Suite di cifratura TLS 1.2 (Esempi comuni selezionati)

| Suite di cifratura | Scambio chiavi | Auth. | Cifrario di massa | MAC | Stato |
|-------------------|----------------|-------|-------------------|-----|-------|
| **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384** | ECDHE | RSA | AES-256-GCM | (AEAD) | Moderna, ampiamente distribuita |
| **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256** | ECDHE | RSA | AES-128-GCM | (AEAD) | Moderna, ampiamente distribuita |
| **TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256** | ECDHE | RSA | ChaCha20-Poly1305 | (AEAD) | Moderna, mobile |
| **TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384** | ECDHE | ECDSA | AES-256-GCM | (AEAD) | Moderna, certificati ECC |
| **TLS_RSA_WITH_AES_256_GCM_SHA384** | RSA | RSA | AES-256-GCM | (AEAD) | Legacy, senza confidenzialità in avanti |
| **TLS_RSA_WITH_3DES_EDE_CBC_SHA** | RSA | RSA | 3DES-CBC | SHA-1 | Obsoleto, deprecato |
| **TLS_RSA_WITH_RC4_128_SHA** | RSA | RSA | RC4 | SHA-1 | Obsoleto, compromesso |

## Protocolli e suite di cifratura deprecati/obsoleti

| Protocollo/Cifrario | Deprecato | Motivo |
|---------------------|-----------|--------|
| **SSL v2** | 2011 | Molteplici falle crittografiche |
| **SSL v3** | 2015 | Attacco POODLE, crittografia debole |
| **TLS 1.0** | 2020 | Crittografia obsoleta, attacco BEAST |
| **TLS 1.1** | 2020 | Crittografia obsoleta |
| **Cifrario RC4** | 2015 | Distorsioni nel flusso di chiavi, attacchi pratici |
| **Cifrario 3DES** | 2023 | Attacco Sweet32, dimensione blocco 64-bit |
| **Cifrari di qualità export** | 1990-2015 | Intenzionalmente indeboliti (40-56 bit) |
| **Crittografia NULL** | Sempre | Nessuna crittografia |
| **DH anonimo (ADH)** | Sempre | Nessuna autenticazione, vulnerabile a MITM |

---

# Lunghezze delle chiavi e ciclo di vita degli algoritmi

## Lunghezze delle chiavi comunemente citate nelle raccomandazioni del settore

| Famiglia di algoritmi | Lunghezza minima chiave | Valido fino a | Note |
|----------------------|------------------------|---------------|------|
| **RSA (firma, scambio chiavi)** | 2048-bit | ~2030 | 3072-bit per chiavi >2030 |
| **RSA (chiavi a lungo termine)** | 3072-bit | Oltre 2030 | CA radice, firma codice |
| **Diffie-Hellman** | 2048-bit | ~2030 | 3072-bit per uso futuro |
| **ECDSA/ECDH** | P-256 (256-bit) | Oltre 2030 | P-384 per alta sicurezza |
| **AES** | 128-bit | Oltre 2030 | 256-bit per alta sicurezza |
| **Funzioni di hash** | SHA-256 | Oltre 2030 | SHA-384 per alta sicurezza |

**Fonte**: NIST SP 800-57 Parte 1 Rev. 5, BSI TR-02102-1

## Stato del ciclo di vita degli algoritmi

| Stato | Definizione | Esempi |
|-------|-------------|--------|
| **Moderno** | Migliore pratica attuale, attivamente distribuito | AES, RSA-2048+, ECDSA P-256+, SHA-256, TLS 1.3 |
| **Ampiamente utilizzato** | Maturo, stabile, ampia distribuzione | TLS 1.2, RSA-2048, SHA-256, ChaCha20 |
| **Legacy** | In invecchiamento, in corso di sostituzione | 3DES, DSA, SHA-1 (non certificato), TLS 1.1 |
| **Deprecato** | Non più raccomandato, eliminazione in corso | SSL v3, TLS 1.0, RC4, firme MD5 |
| **Obsoleto** | Crittograficamente compromesso | DES, MD5 (uso sicurezza), RC4, SHA-1 (certificati) |
| **Emergente** | Standardizzato ma distribuzione limitata | Algoritmi post-quantistici (ML-KEM, ML-DSA) |

## Stato della crittografia post-quantistica

Standardizzazione della crittografia post-quantistica (PQC) del NIST:

| Algoritmo | Tipo | Stato (2024-2025) | Note |
|-----------|------|-------------------|------|
| **ML-KEM** (Kyber) | Incapsulamento chiavi | FIPS 203 pubblicato 2024 | Scambio di chiavi, modalità ibrida con ECDH |
| **ML-DSA** (Dilithium) | Firma digitale | FIPS 204 pubblicato 2024 | Firme, modalità ibrida con ECDSA/RSA |
| **SLH-DSA** (SPHINCS+) | Firma digitale | FIPS 205 pubblicato 2024 | Firme basate su hash senza stato |
| **FN-DSA** (Falcon) | Firma digitale | In esame | Basato su reticoli, firme compatte |

**Osservazioni del settore**:

- Algoritmi post-quantistici in fase di standardizzazione ma non ancora ampiamente distribuiti
- Modalità ibride (PQC + classica) attese durante il periodo di transizione
- Scambio di chiavi ibrido TLS 1.3 (X25519 + ML-KEM) in sviluppo
- Le autorità di certificazione stanno iniziando l'emissione sperimentale PQC

---

# Validità e ciclo di vita dei certificati

## Evoluzione storica della validità dei certificati

Periodi di validità massima dei certificati TLS pubblici:

| Periodo | Validità massima | Autorità |
|---------|-----------------|----------|
| Prima del 2011 | Nessun limite definito | Discrezione del fornitore |
| 2011-2015 | 60 mesi (5 anni) | CA/Browser Forum |
| 2015-2017 | 39 mesi (~3 anni) | CA/Browser Forum Ballot 193 |
| 2017-2020 | 825 giorni (~27 mesi) | CA/Browser Forum Ballot 193 |
| 2020-presente | 398 giorni (~13 mesi) | CA/Browser Forum Ballot SC-31 |

## Validità futura dei certificati (Ballot SC-081v3)

CA/Browser Forum Ballot SC-081v3 (approvato aprile 2025):

| Data di entrata in vigore | Validità massima | Periodo di riutilizzo DCV |
|--------------------------|-----------------|--------------------------|
| 15 marzo 2026 | 200 giorni | 200 giorni |
| 15 marzo 2027 | 100 giorni | 100 giorni |
| 15 marzo 2029 | 47 giorni | 10 giorni |

**Osservazioni del settore**:

- La durata dei certificati si sta riducendo per migliorare la sicurezza e l'agilità
- Le durate più brevi aumentano l'importanza della gestione automatizzata del ciclo di vita
- La PKI interna/privata non è soggetta ai requisiti del CA/Browser Forum

**Nota sulla PKI interna**: Le politiche dei certificati interni sono determinate dalla valutazione del rischio e dal contesto operativo. Le organizzazioni possono scegliere durate più brevi o più lunghe in base alla propria postura di sicurezza specifica.

---

# Norme e fonti di riferimento

## Organismi normativi autorevoli

| Organizzazione | Area di competenza | Pubblicazioni chiave |
|---------------|-------------------|---------------------|
| **NIST** | Standard crittografici (USA) | FIPS 140-2/3, serie SP 800 |
| **BSI** | Standard crittografici (Germania) | TR-02102-1 a TR-02102-4 |
| **ENISA** | Raccomandazioni crittografiche (UE) | Report sugli algoritmi, linee guida |
| **IETF** | Standard di protocollo | RFC (TLS, SSH, IPsec) |
| **CA/Browser Forum** | Standard delle autorità di certificazione | Requisiti di base, ballot |
| **ISO/IEC JTC 1/SC 27** | Standard di sicurezza delle informazioni | ISO/IEC 18033 (algoritmi di crittografia) |

## Documenti di riferimento chiave

**Pubblicazioni NIST**:

- FIPS 140-2/140-3: Requisiti di sicurezza per i moduli crittografici
- NIST SP 800-52 Rev. 2: Linee guida per le implementazioni TLS
- NIST SP 800-57 Parte 1 Rev. 5: Raccomandazioni per la gestione delle chiavi
- NIST SP 800-131A Rev. 2: Transizione dell'uso degli algoritmi crittografici

**Pubblicazioni BSI**:

- TR-02102-1: Meccanismi crittografici — Raccomandazioni e lunghezze delle chiavi
- TR-02102-2: Utilizzo di TLS
- TR-02102-3: Algoritmi crittografici appropriati
- TR-02102-4: Utilizzo di Secure Shell (SSH)

**RFC IETF**:

- RFC 8446: Il protocollo Transport Layer Security (TLS) Versione 1.3
- RFC 5246: Il protocollo Transport Layer Security (TLS) Versione 1.2
- RFC 8032: Algoritmo di firma digitale su curva di Edwards (EdDSA)

## Monitoraggio della deprecazione degli algoritmi

Le organizzazioni monitorano comunemente lo stato degli algoritmi tramite:

- Programma di validazione degli algoritmi crittografici del NIST (CAVP)
- Elenco degli algoritmi deprecati del NIST
- Politiche di sicurezza dei fornitori di browser (Chrome, Firefox, Safari, Edge)
- Monitoraggio dei ballot del CA/Browser Forum
- Bollettini di sicurezza dei fornitori (OpenSSL, Microsoft, Apple, ecc.)

---

# Manutenzione del documento

## Trigger di aggiornamento

Questo documento di riferimento può essere aggiornato quando:

- Si verifica una standardizzazione importante degli algoritmi (NIST, RFC IETF)
- Vengono annunciate deprecazioni significative di algoritmi
- Vengono pubblicate aggiornamenti del protocollo TLS/SSL
- Vengono raggiunte tappe importanti nel deployment della crittografia post-quantistica
- Cambiano i requisiti di base del CA/Browser Forum

---

# Relazione con ISMS-POL-A.8.24

Questo documento fornisce un **contesto tecnico** che può informare:

- La consapevolezza dell'agilità crittografica (ISMS-POL-A.8.24 Sezione 2.6)
- Le discussioni sulla selezione degli algoritmi durante la pianificazione dell'implementazione
- La valutazione del rischio dei sistemi crittografici legacy
- La comprensione dell'evoluzione degli standard del settore

---

**FINE DEL DOCUMENTO**

*Questo è un documento di riferimento tecnico esclusivamente a scopo di sensibilizzazione. Non stabilisce requisiti SGSI e non crea obblighi di conformità.*

<!-- QA_VERIFIED: 2026-04-04 -->
