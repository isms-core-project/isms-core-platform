<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.24-IT:framework:POL:a.8.24 -->
**ISMS-POL-A.8.24 — Utilizzo della crittografia**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Utilizzo della crittografia |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.24 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DSI → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.24.1–4-UG/TG; ISMS-CTX-A.8.24 (Riferimento sul panorama crittografico); ISO/IEC 27001:2022 Controllo A.8.24.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per i controlli crittografici per proteggere la riservatezza, l'integrità e l'autenticità delle informazioni, conformemente al Controllo A.8.24 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutti gli asset informativi, i sistemi e il personale che gestisce informazioni classificate (Interno, Riservato o Limitato).

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.24

> *Deve essere sviluppata e implementata una politica sull'utilizzo dei controlli crittografici per la protezione delle informazioni.*

**Obiettivo del controllo**: Stabilire la politica organizzativa per i controlli crittografici che proteggono le informazioni durante il loro ciclo di vita.

---

# Enunciati di politica

## Standard crittografici approvati

[Organizzazione] DEVE utilizzare solo algoritmi crittografici approvati e configurati in modo sicuro.

**Algoritmi approvati**:

| Scopo | Algoritmo approvato | Dimensione minima della chiave | Note |
|-------|--------------------|-----------------------------|------|
| **Cifratura simmetrica** | AES-GCM | 256 bit | AES-CBC accettabile con IV corretto |
| **Cifratura asimmetrica** | RSA | 3072 bit | 4096 bit per i nuovi sistemi |
| **Cifratura a curve ellittiche** | ECDSA/ECDH | P-256 (NIST) | P-384 preferito per dati sensibili |
| **Hash** | SHA-256, SHA-3 | N/A | SHA-1 vietato per applicazioni di sicurezza |
| **Accordo di chiave** | ECDH, DH | Vedere EC/RSA | Gruppi DH ≥2048 bit |
| **Firma digitale** | RSA-PSS, ECDSA | Vedere sopra | |
| **TLS** | TLS 1.2, TLS 1.3 | N/A | TLS 1.3 preferito; TLS 1.0/1.1 vietati |

**Algoritmi vietati**: MD5 (per qualsiasi scopo crittografico); SHA-1 (per firme e certificati); DES/3DES; RC4; cifrari di esportazione; cifrari con lunghezze di chiave inferiori ai minimi; crittografia personalizzata o non standard.

## Cifratura dei dati in transito

**Obbligatoria per**: Tutte le trasmissioni di informazioni classificate (Interne, Riservate, Limitate) su reti non affidabili; tutte le connessioni di accesso remoto (VPN); tutte le API che gestiscono dati sensibili; tutti i servizi web (HTTPS obbligatorio); tutta la posta elettronica che contiene informazioni classificate.

**Standard TLS**: TLS 1.3 preferito; TLS 1.2 accettabile; TLS 1.0 e 1.1 VIETATI; i certificati DEVONO avere: lunghezza della chiave ≥2048 bit (RSA) o ≥256 bit (EC); algoritmo hash SHA-256 o superiore; periodo di validità ≤1 anno (90 giorni raccomandato per i certificati pubblici).

## Cifratura dei dati a riposo

**Obbligatoria per**:

| Tipo di dati | Requisito di cifratura |
|-------------|----------------------|
| Dati Riservati e Limitati su laptop/desktop | FDE obbligatoria (AES-256) |
| Dati Riservati e Limitati su server | Cifratura del volume o del file system obbligatoria |
| Dati Riservati e Limitati su archiviazione cloud | Cifratura gestita dal cliente obbligatoria (BYOK preferito) |
| Chiavi API, credenziali, segreti | Archiviazione cifrata (vault delle password o secrets manager) |
| Database contenenti dati sensibili | Cifratura dei dati trasparente (TDE) o cifratura a livello di colonna |
| Supporti rimovibili (Riservato/Limitato) | Cifratura hardware AES-256 obbligatoria |

## Gestione delle chiavi crittografiche

[Organizzazione] DEVE implementare procedure sicure di gestione delle chiavi.

**Requisiti del ciclo di vita delle chiavi**:

| Fase | Requisiti |
|------|-----------|
| **Generazione** | Generatori di numeri casuali approvati; lunghezze delle chiavi conformi agli standard; documentazione dell'uso previsto |
| **Distribuzione** | Canali sicuri per la distribuzione delle chiavi; registrazione degli accessi alle chiavi |
| **Archiviazione** | Hardware Security Module (HSM) per le chiavi critiche; archiviazione cifrata per le chiavi meno critiche; accesso RBAC |
| **Rotazione** | Chiavi simmetriche: ≤2 anni; certificati TLS: ≤1 anno; chiavi di firma del codice: ≤3 anni; rotazione immediata dopo una compromissione sospetta |
| **Revoca** | Revoca immediata in caso di compromissione; CRL o OCSP per i certificati |
| **Distruzione** | Cancellazione sicura delle chiavi ritirate; documentazione della distruzione |

**Chiavi di deposito (escrow) e ripristino**: Le chiavi di cifratura critiche DEVONO avere copie di recupero sicure; le procedure di recupero delle chiavi DEVONO richiedere l'autorizzazione multi-persona; le chiavi di recupero DEVONO essere archiviate separatamente dalle chiavi operative.

## Certificati e PKI

[Organizzazione] DEVE gestire i certificati digitali in modo efficace.

**Inventario dei certificati**: Tutti i certificati TLS/SSL DEVONO essere inventariati; i certificati con scadenza entro 30 giorni DEVONO generare avvisi; i rinnovi DEVONO essere pianificati con almeno 30 giorni di anticipo. **Autorità di certificazione**: [Organizzazione] DEVE utilizzare CA affidabili per i certificati pubblici; i certificati auto-firmati DEVONO essere usati solo per la comunicazione interna con gestione appropriata della fiducia.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione degli algoritmi crittografici; supervisione della conformità |
| **Responsabile Sicurezza Informatica** | Definizione degli standard crittografici; gestione dell'inventario dei certificati |
| **Operazioni IT** | Implementazione della cifratura; gestione operativa delle chiavi |
| **Sviluppatori** | Uso degli algoritmi approvati; non implementazione di crittografia personalizzata |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DSI** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per l'utilizzo della crittografia. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.24 (UG/TG). Il riferimento tecnico è in ISMS-CTX-A.8.24.*

<!-- QA_VERIFIED: 2026-04-03 -->
