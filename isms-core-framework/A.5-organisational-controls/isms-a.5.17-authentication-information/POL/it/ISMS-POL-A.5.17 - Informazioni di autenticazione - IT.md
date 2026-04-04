<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.17-IT:framework:POL:a.5.17 -->
**ISMS-POL-A.5.17 — Informazioni di autenticazione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Informazioni di autenticazione |
| **Tipo di documento** | Politica |
| **Identificativo del documento** | ISMS-POL-A.5.17 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RSSI | Politica iniziale per la certificazione ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Principale: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Secondario: Direttore dei Sistemi Informativi (DSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- ISMS-POL-00 (Quadro di applicabilità normativa)
- ISMS-POL-A.5.15-16-18 (Gestione delle identità e degli accessi)
- ISMS-POL-A.8.2-3-5 (Autenticazione e accesso privilegiato)
- ISMS-POL-A.8.24 (Utilizzo della crittografia)
- ISMS-IMP-A.5.17.1-UG/TG (Guida all'implementazione della politica delle password)
- ISMS-IMP-A.5.17.2-UG/TG (Valutazione del dispiegamento dell'AMF)
- ISMS-IMP-A.5.17.3-UG/TG (Procedure di gestione dell'autenticazione)
- ISO/IEC 27001:2022 Controllo A.5.17

---

## Riepilogo esecutivo

Questa politica stabilisce i requisiti di [Organizzazione] per la gestione e la protezione delle informazioni di autenticazione al fine di prevenire l'accesso non autorizzato ai sistemi informativi e ai dati.

**Perimetro**: Questa politica si applica a tutte le informazioni di autenticazione incluse password, PIN, chiavi crittografiche, token, modelli biometrici e altri segreti di autenticazione utilizzati per accedere ai sistemi e ai dati di [Organizzazione].

**Scopo**: Definire i requisiti organizzativi per la gestione delle informazioni di autenticazione. Questa politica stabilisce QUALI controlli di autenticazione sono richiesti e CHI è responsabile. Le procedure di attuazione (COME) sono documentate separatamente in ISMS-IMP-A.5.17 (varianti UG/TG).

**Allineamento normativo**: nLPD svizzera; RGPD dell'UE; ISO/IEC 27001:2022; FINMA, PCI DSS v4.0.1, NIS2, DORA (applicabilità condizionale per ISMS-POL-00).

---

# Allineamento sul controllo e perimetro

**ISO/IEC 27001:2022 Allegato A.5.17 — Informazioni di autenticazione**

Le informazioni di autenticazione vengono emesse, gestite, protette e revocate attraverso processi definiti del ciclo di vita. Il personale è istruito sulla gestione sicura e deve seguire i requisiti documentati per la riservatezza e la segnalazione delle compromissioni.

**Obiettivi del controllo**: Garantire che le informazioni di autenticazione siano allocate in modo sicuro attraverso processi verificati; proteggere le informazioni di autenticazione durante il loro ciclo di vita; prevenire l'accesso non autorizzato attraverso la compromissione delle credenziali; mantenere la responsabilità per l'utilizzo delle credenziali di autenticazione.

## Applicabilità normativa

**Livello 1 — Conformità obbligatoria**:

| Normativa | Applicabilità | Requisiti chiave |
|-----------|---------------|-----------------|
| **nLPD svizzera Art. 8** | Tutto il trattamento dei dati personali | Misure tecniche per la protezione dei dati |
| **ISO/IEC 27001:2022** | Ambito di certificazione | Controllo A.5.17 — Informazioni di autenticazione |

**Livello 2 — Applicabilità condizionale**:

| Normativa | Condizione scatenante | Requisiti di autenticazione |
|-----------|----------------------|-----------------------------|
| **RGPD dell'UE Art. 32** | Elaborazione di dati personali UE | Misure di sicurezza appropriate inclusa l'autenticazione |
| **FINMA** | Istituto finanziario svizzero regolamentato | Autenticazione avanzata per i sistemi finanziari |
| **PCI DSS v4.0.1** | Elaborazione di carte di pagamento | Requisito 8 — Autenticazione avanzata |
| **NIS2** | Entità essenziale/importante (UE) | Requisiti di autenticazione avanzata |
| **DORA** | Entità dei servizi finanziari UE | Sicurezza TIC inclusi i controlli di autenticazione |

**Livello 3 — Riferimento informativo**: NIST SP 800-63B; CIS Controls v8.1 (Controlli 5, 6); Linee guida OWASP sull'autenticazione; Raccomandazioni Microsoft Security Baseline.

---

# Enunciati di politica

## Allocazione delle informazioni di autenticazione

### Requisiti di allocazione iniziale

[Organizzazione] DEVE allocare le informazioni di autenticazione attraverso processi controllati:

**Verifica dell'identità**: Verificare l'identità dell'utente prima di emettere le credenziali di autenticazione; utilizzare la verifica fuori banda per l'accesso ai sistemi sensibili; documentare il metodo di verifica utilizzato per la pista di audit.

**Distribuzione sicura**:

| Tipo di autenticazione | Metodo di distribuzione |
|----------------------|------------------------|
| **Password iniziali** | Canale sicuro, separato dal nome utente, modifica forzata al primo utilizzo |
| **Token/Hardware** | Consegna di persona con verifica dell'identità, ricevuta firmata |
| **Certificati** | Processo sicuro di registrazione dei certificati, email verificata |
| **Chiavi API** | Canale cifrato, validità limitata, emissione registrata |

**Autenticazione temporanea**: Le informazioni di autenticazione temporanee DEVONO avere una validità massima di 24 ore; gli utenti DEVONO essere obbligati a modificare le credenziali temporanee al primo utilizzo; il sistema DEVE applicare la scadenza delle credenziali temporanee.

### Gestione delle credenziali predefinite

[Organizzazione] NON DEVE utilizzare informazioni di autenticazione predefinite: Tutte le password predefinite del fornitore/produttore DEVONO essere modificate prima del dispiegamento in produzione; gli account predefiniti DEVONO essere disabilitati o rinominati dove tecnicamente fattibile; la verifica della modifica delle credenziali predefinite DEVE essere inclusa nella lista di controllo del commissioning del sistema.

**Condizioni «Tecnicamente non fattibile»**: L'account predefinito non può essere disabilitato/rinominato quando: (1) il firmware/supporto del fornitore richiede l'account, (2) il sistema non ha la funzionalità per rinominarlo, (3) la disabilitazione interrompe funzionalità critiche. Dove non fattibile, si applicano controlli compensativi obbligatori: password univoca robusta per dispositivo, segmentazione di rete che limita l'accesso, AMF dove supportata, monitoraggio/avvisi avanzati, archiviazione sicura delle credenziali e eccezione documentata in ISMS-REG-EXCEPTIONS.

## Requisiti delle password

### Standard di complessità delle password

[Organizzazione] DEVE applicare i seguenti requisiti per le password:

| Requisito | Accesso standard | Accesso privilegiato | Account di servizio |
|-----------|-----------------|---------------------|---------------------|
| **Lunghezza minima** | 12 caratteri | 16 caratteri | 24 caratteri |
| **Complessità** | 3 su 4 tipi di caratteri | 4 su 4 tipi di caratteri | Complessa + casuale |
| **Cronologia** | 12 password ricordate | 24 password ricordate | N/D (uso singolo) |
| **Età massima** | 90 giorni | 60 giorni | 90 giorni o basata su certificato |
| **Soglia di blocco** | 5 tentativi falliti | 3 tentativi falliti | Avviso al singolo tentativo fallito |

**Tipi di carattere**: Maiuscole, minuscole, numeri, caratteri speciali.

**Giustificazione dell'anzianità delle password**: La rotazione basata sul tempo è integrata da trigger di rotazione basati su eventi: (1) compromissione sospetta, (2) scoperta di credenziali condivise, (3) assenza di protezione AMF, (4) cambio di ruolo del personale che incide sull'ambito degli accessi. Dove AMF avanzata e monitoraggio continuo sono verificati, la rotazione può essere estesa tramite eccezione documentata con approvazione del RSSI.

### Pratiche vietate per le password

Il personale NON DEVE:

- Condividere le password con qualsiasi altra persona (incluso il supporto IT)
- Scrivere le password in luoghi non protetti
- Archiviare le password in file di testo normale o documenti
- Utilizzare la stessa password su più sistemi
- Utilizzare password basate su informazioni facilmente indovinabili (nomi, date, parole del dizionario)
- Trasmettere le password tramite canali non cifrati

### Archiviazione delle password

[Organizzazione] DEVE archiviare le password in modo sicuro: Le password DEVONO essere archiviate utilizzando hashing crittografico one-way approvato con salt; algoritmi di hashing delle password: bcrypt, Argon2, PBKDF2 (con parametri appropriati); l'archiviazione di password in chiaro è VIETATA; i database delle password DEVONO essere protetti con cifratura a riposo.

## Autenticazione multi-fattore

### Requisiti AMF

[Organizzazione] DEVE richiedere l'autenticazione multi-fattore per:

| Tipo di accesso | Requisito AMF |
|----------------|--------------|
| **Accesso remoto** (VPN, cloud) | Obbligatorio |
| **Accesso privilegiato/amministratore** | Obbligatorio |
| **Sistemi critici** | Obbligatorio |
| **Accesso ai dati dei clienti** | Obbligatorio |
| **Email (accesso esterno)** | Obbligatorio |
| **Accesso interno standard** | Basato sul rischio per la classificazione del sistema in ISMS-IMP-A.5.17; decisioni registrate nella politica di accesso condizionale dell'IdP; copertura rivista trimestralmente |

### Tipi di fattori AMF

Fattori di autenticazione accettabili:

| Categoria del fattore | Esempi | Requisiti |
|-----------------------|--------|-----------|
| **Qualcosa che conosci** | Password, PIN, passphrase | Per i requisiti delle password |
| **Qualcosa che hai** | Token hardware, autenticatore mobile, smart card | Registrato all'utente individuale |
| **Qualcosa che sei** | Impronta digitale, riconoscimento facciale | Modello biometrico archiviato in modo sicuro |

Le implementazioni AMF DEVONO utilizzare fattori di almeno due categorie diverse.

## Protezione delle informazioni di autenticazione

### Responsabilità degli utenti

Tutto il personale DEVE:

- Mantenere riservate le informazioni di autenticazione
- Utilizzare password robuste e univoche per ogni sistema
- Segnalare immediatamente la compromissione sospetta
- Non consentire ad altri di utilizzare le proprie credenziali
- Modificare immediatamente le password se si sospetta una compromissione
- Utilizzare gestori di password approvati per l'archiviazione sicura

### Requisiti di sistema

I sistemi DEVONO: mascherare l'inserimento della password sugli schermi; non visualizzare le password precedentemente utilizzate; cifrare il traffico di autenticazione in transito; registrare gli eventi di autenticazione (successi e fallimenti); avvisare in caso di anomalie di autenticazione; implementare il blocco dell'account dopo tentativi falliti.

### Informazioni di autenticazione condivise

Le informazioni di autenticazione condivise sono SCONSIGLIATE. Dove richiesto: approvazione del RSSI obbligatoria con giustificazione aziendale documentata; archiviazione nel vault delle credenziali approvato (non in documenti/email/chat in chiaro); custode nominato assegnato per ogni credenziale condivisa; registrazione dei check-out con identificazione dell'utente e timestamp; registrazione della sessione per gli account condivisi privilegiati dove tecnicamente fattibile; responsabilità individuale mantenuta tramite registrazione degli audit; revisione trimestrale dell'accesso e dell'utilizzo; riautorizzazione annuale richiesta.

## Reset e ripristino della password

### Reset della password self-service

Dove implementato, il reset della password self-service DEVE:

- Richiedere la verifica basata sull'AMF (push dell'autenticatore, FIDO2, token hardware) per gli account privilegiati, l'accesso remoto e i sistemi critici
- Le domande di sicurezza basate sulla conoscenza sono vietate a meno che non siano approvate come eccezione con controlli compensativi documentati
- La verifica tramite email/SMS può essere utilizzata solo per gli account a basso rischio dove approvato nella valutazione del rischio del sistema e dove è in atto un monitoraggio aggiuntivo
- Utilizzare token di reset a tempo limitato (validità massima 1 ora)
- Registrare tutte le attività di reset incluso il metodo di verifica utilizzato
- Avvisare l'utente della modifica della password tramite il contatto registrato
- Non rivelare se l'account esiste

### Reset della password assistito

I reset della password assistiti dall'helpdesk DEVONO: verificare l'identità dell'utente utilizzando informazioni pre-registrate; generare una password temporanea con modifica forzata; documentare la richiesta di reset e il metodo di verifica; comunicare la nuova password tramite canale sicuro; non rivelare le password al personale di supporto dopo l'emissione.

---

# Ruoli e responsabilità

| Ruolo | Responsabilità di autenticazione |
|-------|----------------------------------|
| **Direzione generale** | Approvare la politica di autenticazione, fornire risorse per l'implementazione |
| **RSSI** | Proprietà della politica, strategia AMF, approvazione delle eccezioni |
| **Operazioni IT** | Implementazione tecnica, configurazione dei sistemi, infrastruttura delle password |
| **Team IAM** | Provisioning degli utenti, emissione delle credenziali, procedure di reset |
| **Helpdesk** | Reset della password assistito, verifica dell'identità |
| **Proprietari dei sistemi** | Configurazione dell'autenticazione specifica del sistema, verifica della conformità |
| **Tutto il personale** | Protezione delle credenziali, conformità alla politica, segnalazione degli incidenti |

## Percorso di escalation

- Domande sulla politica di autenticazione: Personale → Team IAM → RSSI
- Richieste di eccezione: Richiedente → Responsabile → RSSI
- Incidente di autenticazione: Personale → Team di sicurezza → RSSI → Direzione generale

---

# Governance e conformità

## Quadro di valutazione

| Valutazione | Frequenza | Responsabile | Prove |
|------------|-----------|-------------|-------|
| Conformità alla politica delle password | Mensile | Operazioni IT | Audit della configurazione del sistema |
| Verifica della copertura AMF | Trimestrale | Team di sicurezza | Report del sistema di accesso |
| Revisione dei log di autenticazione | Mensile | Team di sicurezza | Report di analisi SIEM |
| Scansione delle credenziali predefinite | Trimestrale | Team di sicurezza | Risultati della scansione delle vulnerabilità |
| Verifica della sensibilizzazione degli utenti | Annuale | HR | Documenti di completamento della formazione |

**Metriche di governance**:

- Tasso di adozione dell'AMF (obiettivo: 100% per i sistemi obbligatori)
- Tasso di conformità alla politica delle password (obiettivo: >98%)
- Distribuzione dell'anzianità media delle password
- Schemi di autenticazione falliti
- Volume delle richieste di reset delle password e tempi di risoluzione
- Conteggio dei risultati delle credenziali predefinite (obiettivo: 0)

## Revisione della politica

- **Frequenza**: Annuale come minimo
- **Trigger**: Cambiamenti tecnologici dell'autenticazione, incidenti di sicurezza, aggiornamenti normativi
- **Revisori**: RSSI, Operazioni IT, Team IAM
- **Approvazione**: Direzione generale

## Gestione delle eccezioni

**Eccezioni consentite**: Sistemi legacy non in grado di soddisfare la complessità delle password (con mitigazione documentata); sistemi incompatibili con l'AMF (con controlli compensativi); account di servizio che richiedono politiche di password diverse (con monitoraggio avanzato).

**Non ammissibile**: Eccezioni che consentono la condivisione delle password senza responsabilità; eccezioni che eliminano l'AMF per l'accesso privilegiato; eccezioni che consentono le credenziali predefinite in produzione.

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni (ISMS-REG-EXCEPTIONS).

---

# Implementazione e riferimenti

**Controlli correlati**:

| Controllo | Relazione |
|-----------|----------|
| **A.5.15-16-18** | L'IAM definisce le identità; A.5.17 protegge la loro autenticazione |
| **A.8.2-3-5** | L'accesso privilegiato richiede un'autenticazione più rigorosa |
| **A.8.24** | Protezione crittografica delle informazioni di autenticazione |
| **A.8.12** | Il DLP rileva la perdita delle credenziali |
| **A.8.15** | Registrazione degli eventi di autenticazione |

## Risorse di implementazione

| ID documento | Titolo | Scopo |
|-------------|--------|-------|
| **ISMS-IMP-A.5.17.1-UG/TG** | Guida all'implementazione della politica delle password | Procedure di configurazione tecnica |
| **ISMS-IMP-A.5.17.2-UG/TG** | Valutazione del dispiegamento dell'AMF | Rollout e verifica AMF |
| **ISMS-IMP-A.5.17.3-UG/TG** | Procedure di gestione dell'autenticazione | Procedure operative per il ciclo di vita delle credenziali |

---

# Definizioni

| Termine | Definizione |
|---------|-------------|
| **Informazioni di autenticazione** | Dati utilizzati per dimostrare l'identità, incluse password, token, chiavi, dati biometrici |
| **Autenticazione multi-fattore (AMF)** | Autenticazione che richiede due o più fattori di verifica da categorie diverse |
| **Hash della password** | Rappresentazione crittografica one-way di una password |
| **Salt** | Dati casuali aggiunti alle password prima dell'hashing per prevenire gli attacchi con tabelle arcobaleno |
| **Verifica fuori banda** | Verifica dell'identità utilizzando un canale di comunicazione separato |
| **Attacco a forza bruta** | Tentativo di indovinare le credenziali attraverso una prova sistematica |
| **Credential stuffing** | Attacco che utilizza credenziali trapelate da altre violazioni |

---

# Registro di approvazione

| Ruolo | Nome | Data |
|-------|------|------|
| **Responsabile della Sicurezza dei Sistemi Informativi (RSSI)** | [Nome] | [Data da definire] |
| **Direttore dei Sistemi Informativi (DSI)** | [Nome] | [Data da definire] |
| **Direzione generale** | [Nome] | [Data da definire] |

---

**FINE DEL DOCUMENTO DI POLITICA**

*Questa politica stabilisce i requisiti per la gestione delle informazioni di autenticazione. Le procedure di attuazione sono documentate in ISMS-IMP-A.5.17 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-03 -->
