<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.28-IT:framework:POL:a.8.28 -->
**ISMS-POL-A.8.28 — Codifica sicura**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Politica di codifica sicura |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.8.28 |
| **Autore del documento** | RSSI |
| **Proprietario del documento** | AD |
| **Approvato da** | Direzione generale |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Ciclo di revisione**: Annuale | **Catena di approvazione**: RSSI → DT → Conformità → Direzione generale.

**Documenti correlati**: ISMS-POL-00; ISMS-IMP-A.8.28.1–4-UG/TG; ISMS-CTX-A.8.28 (Linee guida di codifica sicura specifiche per linguaggio); ISMS-REF-A.8.28 (Riferimento tecnico per la revisione del codice); ISO/IEC 27001:2022 Controllo A.8.28.

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per lo sviluppo software sicuro, conformemente al Controllo A.8.28 della norma ISO/IEC 27001:2022.

**Perimetro**: Si applica a tutte le attività di sviluppo software (sviluppo interno, esternalizzato, personalizzazione del software acquisito); a tutti i tipi di applicazioni, fasi di sviluppo e linguaggi di programmazione.

**Rischio aziendale affrontato**: Le vulnerabilità del software che portano a violazioni dei dati, interruzioni del servizio, perdite finanziarie, danni reputazionali e sanzioni normative.

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; PCI DSS v4.0.1, FINMA, DORA, NIS2 (applicabilità condizionale per ISMS-POL-00).

---

# Controllo ISO/IEC 27001:2022 A.8.28

> *Principi di codifica sicura devono essere applicati allo sviluppo del software.*

**Obiettivo del controllo**: Garantire che il software sia sviluppato seguendo pratiche di codifica sicura per prevenire l'introduzione di vulnerabilità di sicurezza durante lo sviluppo.

---

# Enunciati di politica

## Standard di codifica sicura

[Organizzazione] DEVE adottare e applicare standard di codifica sicura per tutte le attività di sviluppo software.

**Framework di riferimento obbligatori**: OWASP Top 10 (aggiornato); OWASP Application Security Verification Standard (ASVS) per i sistemi ad alto rischio; linee guida specifiche per linguaggio (ISMS-CTX-A.8.28).

**Pratiche obbligatorie di codifica sicura**:

| Categoria | Requisiti |
|----------|-----------|
| **Validazione degli input** | Validare tutte le input dall'utente; usare l'approccio whitelist; rifiutare l'input non valido; never trust client-side validation |
| **Output encoding** | Codificare l'output in base al contesto (HTML, SQL, URL, comandi); prevenire XSS e injection |
| **Autenticazione** | Non implementare meccanismi di autenticazione personalizzati; usare librerie testate e approvate |
| **Gestione delle sessioni** | Token di sessione generati in modo crittograficamente sicuro; scadenza della sessione implementata; invalidazione della sessione al logout |
| **Cifratura** | Usare solo algoritmi approvati (ISMS-POL-A.8.24); non implementare crittografia personalizzata; non archiviare dati sensibili in chiaro |
| **Gestione degli errori** | Messaggi di errore generici agli utenti; errori dettagliati solo nei log; mai esporre stack trace o informazioni di sistema |
| **Registrazione e monitoraggio** | Registrare gli eventi di sicurezza (autenticazione, autorizzazione, errori); non registrare dati sensibili (password, token, DCP) |
| **Gestione delle dipendenze** | Mantenere un SBOM aggiornato; monitorare le dipendenze per le vulnerabilità note; aggiornare le dipendenze vulnerabili per ISMS-POL-A.8.8 |

## Requisiti di revisione del codice

[Organizzazione] DEVE implementare la revisione del codice come controllo obbligatorio.

**Revisione del codice per la sicurezza**: Tutta la modifica del codice DEVE essere soggetta a revisione del codice prima del merge ai branch protetti (per ISMS-POL-A.8.4); la revisione del codice DEVE includere la verifica della sicurezza; i revisori DEVONO essere formati sulle pratiche di codifica sicura.

**Requisiti di revisione specifici per la sicurezza**: Le modifiche che influenzano i meccanismi di autenticazione/autorizzazione richiedono la revisione del team di sicurezza; le modifiche che influenzano il trattamento dei DCP richiedono la revisione della sicurezza e la consulenza del RPD; le modifiche all'infrastruttura critica richiedono la revisione dell'architetto sicuro.

## Strumenti di sicurezza nello sviluppo

**Strumenti obbligatori nella pipeline CI/CD**:

| Strumento | Tipo | Trigger |
|---------|------|---------|
| SAST | Analisi statica del codice sorgente | Ogni commit/PR |
| SCA | Analisi delle dipendenze open source/di terze parti | Ogni build |
| Scansione dei segreti | Rilevamento dei segreti hard-coded | Ogni commit |

**Strumenti raccomandati**: DAST (test dinamico) per ogni release; SBOM per il tracciamento delle dipendenze.

**Gestione dei risultati degli strumenti**: Le vulnerabilità Critiche DEVONO bloccare il pipeline CI/CD; le vulnerabilità Alte DEVONO essere remediate prima del dispiegamento in produzione; le eccezioni richiedono l'approvazione documentata del RSSI.

## Formazione sulla codifica sicura

[Organizzazione] DEVE garantire che gli sviluppatori ricevano formazione sulla codifica sicura.

**Requisiti di formazione**: Formazione sulla codifica sicura durante l'onboarding per tutti gli sviluppatori; formazione annuale di aggiornamento; formazione specifica per linguaggio (ISMS-CTX-A.8.28) per i linguaggi principali utilizzati; simulazioni di phishing specifiche per gli sviluppatori (per ISMS-POL-A.8.1-7-18-19). **Obiettivo di completamento**: ≥95% degli sviluppatori annualmente.

## Gestione del software open source e di terze parti

**Requisiti**: Mantenere un inventario di tutte le dipendenze open source e di terze parti (SBOM); valutare le dipendenze per le vulnerabilità note prima dell'adozione; monitorare continuamente le vulnerabilità nelle dipendenze esistenti; aggiornare o sostituire le dipendenze vulnerabili per i tempi ISMS-POL-A.8.8.

**Criteri di valutazione delle dipendenze**: Attività di manutenzione del progetto (repository abbandonati richiedono scrutinio aggiuntivo); licenza (verificare la compatibilità con le licenze aziendali); storico della sicurezza (CVE precedenti, patch tempestive).

---

# Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approva le eccezioni agli standard di codifica sicura |
| **DT** | Applicazione degli standard di codifica sicura; formazione degli sviluppatori |
| **Application Security Lead** | Definizione degli standard di codifica sicura; supervisione delle revisioni del codice di sicurezza |
| **Team di sviluppo** | Conformità agli standard di codifica sicura; rimedio delle vulnerabilità identificate |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **RSSI** | [Nome] | [Data] |
| **DT** | [Nome] | [Data] |
| **Direzione generale** | [Nome] | [Data] |

---

**FINE DEL DOCUMENTO**

*Questa politica stabilisce i requisiti per la codifica sicura. Le procedure di attuazione sono documentate in ISMS-IMP-A.8.28 (UG/TG). Il riferimento tecnico è in ISMS-CTX-A.8.28 e ISMS-REF-A.8.28.*

<!-- QA_VERIFIED: 2026-04-03 -->
