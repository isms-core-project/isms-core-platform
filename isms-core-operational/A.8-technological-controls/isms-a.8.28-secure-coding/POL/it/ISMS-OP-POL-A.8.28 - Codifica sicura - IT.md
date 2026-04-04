<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.28-IT:operational:OP-POL:a.8.28 -->
**ISMS-OP-POL-A.8.28 — Codifica sicura**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Codifica sicura |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.28 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.28 — Codifica sicura
- ISO/IEC 27002:2022 Sezione 8.28 — Guida all'implementazione della codifica sicura
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- NIST SP 800-53 Rev 5 — SA-15 (Development Process, Standards, and Tools), SA-16 (Developer-Provided Training), SA-17 (Developer Security Architecture and Design)
- OWASP Secure Coding Practices — Quick Reference Guide
- OWASP Top 10 (2021) — Rischi per la sicurezza delle applicazioni web
- CWE/SANS Top 25 — Le vulnerabilità software più pericolose (edizione 2025)
- CIS Controls v8 — Salvaguardie 16.1–16.14 (Sicurezza del software applicativo)
- CERT Secure Coding Standards (SEI/Carnegie Mellon)

**Controlli Allegato A correlati**:

| Controllo | Relazione con la codifica sicura |
|-----------|----------------------------------|
| A.5.8 Sicurezza delle informazioni nella gestione dei progetti | Requisiti di sicurezza definiti all'avvio del progetto |
| A.5.23 Sicurezza delle informazioni per l'uso dei servizi cloud | Codifica sicura per le applicazioni distribuite nel cloud |
| A.8.4 Accesso al codice sorgente | Controllo degli accessi al repository e protezione dei branch |
| A.8.8 Gestione delle vulnerabilità tecniche | Rimedio delle vulnerabilità per il codice distribuito |
| A.8.9 Gestione della configurazione | Configurazione sicura degli strumenti e degli ambienti di sviluppo |
| A.8.15 Registrazione degli eventi | Requisiti di registrazione della sicurezza a livello applicativo |
| A.8.24 Uso della crittografia | Implementazione crittografica nel codice applicativo |
| A.8.25–26–29 Ciclo di vita dello sviluppo sicuro | Framework SDLC generale; requisiti di sicurezza, testing |
| A.8.31 Separazione degli ambienti | Isolamento degli ambienti di sviluppo, test e produzione |
| A.8.32 Gestione delle modifiche | Distribuzione controllata delle modifiche al codice in produzione |

**Politiche interne correlate**:

- Politica sul ciclo di vita dello sviluppo sicuro
- Politica di accesso al codice sorgente
- Politica di gestione delle vulnerabilità
- Politica sull'uso della crittografia
- Politica di gestione delle modifiche
- Politica di registrazione degli eventi

---

# Politica sulla codifica sicura

## Scopo

Lo scopo di questa politica è stabilire i principi obbligatori di codifica sicura che devono essere applicati durante tutto il ciclo di vita dello sviluppo del software. La codifica sicura previene l'introduzione di vulnerabilità nel codice, riducendo la superficie di attacco e proteggendo le risorse informative dell'organizzazione, i clienti e la reputazione. Le pratiche di codifica inadeguate — validazione impropria degli input, generazione di chiavi deboli, credenziali hardcoded, gestione degli errori insufficiente — creano debolezze sfruttabili che gli avversari prendono sistematicamente di mira.

Questa politica supporta la nLPD svizzera (revDSG) Art. 7 (protezione dei dati per impostazione predefinita e fin dalla progettazione) e Art. 8 (misure tecniche e organizzative) richiedendo che la sicurezza sia integrata nel codice applicativo fin dalla fase di progettazione. Laddove l'organizzazione tratta dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 25 (protezione dei dati per impostazione predefinita e fin dalla progettazione) e Art. 32 (sicurezza del trattamento). La codifica sicura è una misura tecnica fondamentale per dimostrare che i sistemi che trattano dati personali sono costruiti per prevenire accessi non autorizzati, violazioni dei dati e violazioni dell'integrità.

## Ambito

Tutte le attività di sviluppo software in cui l'organizzazione scrive, modifica o mantiene codice sorgente. Ciò include:

- Tutte le applicazioni sviluppate internamente (web, mobile, desktop, API, microservizi).
- Infrastruttura come codice (IaC), script di gestione della configurazione e definizioni delle pipeline CI/CD.
- Integrazioni personalizzate, plugin ed estensioni a piattaforme di terze parti.
- Contributi open source effettuati a nome dell'organizzazione.
- Codice scritto da collaboratori, team di sviluppo in outsourcing e sviluppatori offshore che lavorano per conto dell'organizzazione.

Tutti gli sviluppatori, gli ingegneri della sicurezza, gli ingegneri QA, gli ingegneri DevOps, i collaboratori e i team di sviluppo terzi che scrivono codice per l'organizzazione.

**Fuori ambito**: Software commerciale off-the-shelf (COTS) senza personalizzazione (coperto dalla valutazione della sicurezza dei fornitori); gestione delle vulnerabilità runtime post-distribuzione in produzione (coperto dalla A.8.8); governance del ciclo di vita dello sviluppo sicuro (coperto dalla A.8.25-26-29); controllo degli accessi al codice sorgente (coperto dalla A.8.4).

## Principio

Tutto il codice sorgente prodotto per o per conto dell'organizzazione deve seguire standard di codifica sicura documentati. La sicurezza deve essere considerata prima di iniziare a codificare, applicata durante la codifica e verificata dopo il completamento della codifica. Gli sviluppatori non devono fare affidamento esclusivamente sui test di sicurezza per trovare i difetti — la codifica sicura previene l'introduzione dei difetti in primo luogo.

L'organizzazione deve definire esplicitamente quali standard di codifica segue, facendo riferimento a framework di settore riconosciuti (OWASP, CWE/SANS Top 25, CERT o linee guida specifiche per linguaggio). Le affermazioni generiche di "codifica sicura" senza citare un framework sono insufficienti ai fini dell'audit.

---

## Standard di codifica sicura

L'organizzazione deve stabilire e mantenere standard di codifica sicura documentati applicabili a ciascun linguaggio di programmazione e framework in uso attivo.

**Framework di base**:

| Framework | Ambito | Applicazione |
|-----------|--------|--------------|
| OWASP Top 10 (2021) | Vulnerabilità delle applicazioni web | Riferimento obbligatorio per tutto il codice rivolto al web |
| CWE/SANS Top 25 | Vulnerabilità software più pericolose | Riferimento obbligatorio per tutto il codice |
| OWASP Secure Coding Practices | Checklist di codifica indipendente dalla tecnologia | Riferimento obbligatorio per tutto lo sviluppo |
| CERT Secure Coding Standards | Codifica sicura specifica per linguaggio (C, C++, Java, Perl) | Obbligatorio dove esistono standard specifici per linguaggio |

**Standard specifici per linguaggio**:

Il Responsabile sviluppo deve mantenere un registro dei linguaggi approvati e dei relativi riferimenti per la codifica sicura. Come minimo:

| Linguaggio / Framework | Riferimento per la codifica sicura |
|------------------------|-----------------------------------|
| Python | PEP 8 + OWASP Python Security + set di regole Bandit |
| JavaScript / TypeScript | Regole del plugin ESLint per la sicurezza + riferimento OWASP NodeGoat |
| Java | CERT Oracle Secure Coding Standard for Java + regole SpotBugs/FindSecBugs |
| C / C++ | CERT C/C++ Secure Coding Standards + applicazione degli avvisi del compilatore |
| Go | Best practice di sicurezza Go + govulncheck |
| .NET / C# | Microsoft Secure Coding Guidelines + analizzatori Roslyn |
| PHP | OWASP PHP Security Cheat Sheet + regole Psalm/PHPStan |

Laddove viene utilizzato un linguaggio che non ha una voce in questo registro, il Responsabile sviluppo deve documentare il riferimento applicabile per la codifica sicura prima che il linguaggio entri in uso di produzione.

**Revisione degli standard di codifica**: Gli standard di codifica sicura devono essere revisionati annualmente, o quando viene adottato un nuovo linguaggio o framework, o quando emerge una classe di vulnerabilità significativa che richiede una guida aggiuntiva.

---

## Prevenzione delle vulnerabilità comuni

Gli sviluppatori devono scrivere codice che prevenga le classi di vulnerabilità identificate dall'OWASP Top 10 e dal CWE/SANS Top 25. Le seguenti sezioni definiscono pratiche di codifica obbligatorie per le categorie di vulnerabilità più diffuse.

### Validazione degli input

Tutti gli input provenienti da fonti esterne devono essere trattati come non attendibili e validati prima dell'elaborazione.

**Requisiti**:

- Validare tutti gli input sul lato server, indipendentemente dalla validazione lato client. La validazione lato client migliora l'esperienza utente ma non fornisce sicurezza.
- Utilizzare la validazione con allowlist (positiva): definire cosa è consentito, rifiutare tutto il resto. La validazione con denylist (negativa) è insufficiente come unico controllo.
- Validare il tipo di dati, la lunghezza, l'intervallo e il formato. Rifiutare gli input non conformi prima dell'elaborazione.
- Validare e sanificare tutti gli input da moduli, parametri URL, intestazioni HTTP, cookie, payload API, upload di file e dati provenienti da sistemi upstream.
- Utilizzare query parametrizzate o prepared statement per tutte le interazioni con il database. La concatenazione di input utente in istruzioni SQL è vietata.
- Validare i file caricati: limitare i tipi di file consentiti, applicare limiti di dimensione, eseguire la scansione per malware, archiviare i file caricati al di fuori della web root e non eseguire mai i file caricati.

### Codifica degli output

Tutti gli output visualizzati agli utenti o ai sistemi esterni devono essere codificati per prevenire gli attacchi di iniezione.

**Requisiti**:

- Applicare la codifica dell'output appropriata al contesto (HTML, JavaScript, URL, CSS, XML) durante la visualizzazione di contenuto dinamico.
- Utilizzare le funzioni di codifica fornite dal framework anziché implementazioni personalizzate.
- Codificare l'output al punto di visualizzazione, non al punto di archiviazione.
- Impostare correttamente le intestazioni Content-Type e charset su tutte le risposte HTTP.
- Implementare le intestazioni Content Security Policy (CSP) per mitigare i rischi di cross-site scripting (XSS).

### Autenticazione e gestione delle sessioni

Il codice applicativo che implementa l'autenticazione e la gestione delle sessioni deve seguire schemi sicuri consolidati.

**Requisiti**:

- Non implementare schemi di autenticazione personalizzati. Utilizzare il framework di autenticazione approvato dall'organizzazione o il provider di identità.
- Archiviare le password utilizzando algoritmi di hashing adattativi approvati (bcrypt, scrypt o Argon2id) con salt univoci. MD5, SHA-1 e gli hash non salati sono vietati.
- Implementare il blocco dell'account o ritardi progressivi dopo tentativi di autenticazione ripetutamente falliti.
- Generare identificatori di sessione utilizzando generatori di numeri casuali crittograficamente sicuri. Gli ID di sessione devono essere di lunghezza sufficiente (minimo 128 bit di entropia).
- Impostare attributi sicuri per i cookie: `Secure`, `HttpOnly`, `SameSite`. Trasmettere i cookie di sessione solo tramite TLS.
- Invalidare le sessioni al logout, al cambio della password e all'escalation dei privilegi. Impostare valori appropriati di timeout della sessione.
- Non esporre gli identificatori di sessione in URL, messaggi di errore o log.

### Gestione degli errori e registrazione

La gestione degli errori applicativi deve prevenire la divulgazione di informazioni e supportare il monitoraggio della sicurezza.

**Requisiti**:

- Visualizzare messaggi di errore generici agli utenti. Non esporre stack trace, messaggi di errore del database, percorsi di file interni, numeri di versione del framework o dettagli di configurazione del server.
- Registrare tutti gli eventi rilevanti per la sicurezza: autenticazioni riuscite e fallite, fallimenti dell'autorizzazione, fallimenti della validazione degli input, errori applicativi e azioni amministrative.
- Registrare un contesto sufficiente per l'indagine: timestamp (UTC), identità dell'utente, indirizzo IP sorgente, azione tentata, risorsa interessata e stato di successo o fallimento.
- Non registrare dati sensibili: password, token di sessione, dati personali, numeri di carta di credito o chiavi crittografiche.
- Utilizzare un framework di registrazione centralizzato. Non scrivere meccanismi di registrazione personalizzati che bypassino l'infrastruttura di registrazione dell'organizzazione.
- Garantire che le voci di registro contenenti dati non attendibili non possano essere eseguite come codice nell'interfaccia di visualizzazione dei log (prevenzione dell'iniezione nei log).

### Pratiche crittografiche

Il codice applicativo che implementa o utilizza la crittografia deve seguire la politica crittografica dell'organizzazione.

**Requisiti**:

- Utilizzare le librerie crittografiche fornite dalla piattaforma o librerie di terze parti approvate. Non implementare algoritmi crittografici personalizzati.
- Utilizzare algoritmi correnti e approvati: AES-256 per la cifratura simmetrica, RSA-2048+ o ECDSA P-256+ per le operazioni asimmetriche, SHA-256+ per l'hashing. MD5 e SHA-1 sono vietati per scopi di sicurezza.
- TLS 1.2 minimo (TLS 1.3 preferito) per tutti i dati in transito. SSL, TLS 1.0 e TLS 1.1 sono vietati.
- Generare chiavi crittografiche utilizzando generatori di numeri casuali crittograficamente sicuri. Non utilizzare seed prevedibili.
- Non codificare chiavi crittografiche, chiavi API o segreti nel codice sorgente. Utilizzare la soluzione di gestione dei segreti approvata dall'organizzazione.
- Fare riferimento a ISMS-OP-POL-A.8.24 (Uso della crittografia) per i requisiti crittografici completi.

### Controllo degli accessi nel codice

Il codice applicativo deve applicare l'autorizzazione in modo coerente.

**Requisiti**:

- Applicare il controllo degli accessi sul lato server per ogni richiesta. Non fare affidamento esclusivamente sul nascondere gli elementi dell'interfaccia utente.
- Applicare il rifiuto predefinito: se il livello di autorizzazione di un utente non può essere determinato, negare l'accesso.
- Applicare il principio del privilegio minimo nel codice: concedere le autorizzazioni minime richieste per ciascuna funzione.
- Validare l'autorizzazione per ogni endpoint API, inclusi i riferimenti indiretti agli oggetti.
- Non fidarsi delle affermazioni di ruolo o autorizzazione fornite dal client senza verifica lato server.

---

## Gestione delle dipendenze e delle librerie

Le librerie di terze parti, i framework e i componenti open source introducono rischi nella catena di approvvigionamento e devono essere gestiti durante tutto il loro ciclo di vita.

**Requisiti**:

- Mantenere un inventario delle dipendenze per ciascuna applicazione. Tutte le applicazioni di produzione devono mantenere una Software Bill of Materials (SBOM) in formato CycloneDX o SPDX, generata automaticamente tramite la pipeline di build.
- Utilizzare strumenti di Software Composition Analysis (SCA) ([Strumento SCA] — ad esempio, Dependabot, Snyk, OWASP Dependency-Check o equivalente) per eseguire la scansione delle dipendenze alla ricerca di vulnerabilità note.
- La scansione SCA deve essere eseguita ad ogni build (integrazione nella pipeline CI/CD). Le build devono fallire se vengono rilevate vulnerabilità di dipendenze critiche o ad alta gravità non risolte.
- Bloccare le versioni delle dipendenze nei file di blocco (lock file). Non utilizzare intervalli di versione variabili (ad esempio, `*` o `>=`) per le dipendenze di produzione.
- Valutare le nuove dipendenze prima dell'adozione: verificare lo stato di manutenzione, le vulnerabilità note, la compatibilità delle licenze e l'attività della community. Le librerie abbandonate o non mantenute non devono essere introdotte.
- Rimuovere le dipendenze inutilizzate. Condurre un audit delle dipendenze almeno annualmente per identificare e rimuovere le librerie non più in uso.

**Requisiti della Software Bill of Materials (SBOM)**:

La generazione di SBOM deve essere una pratica standard per tutte le applicazioni, non limitata alle applicazioni ad alto rischio.

- **Formato**: CycloneDX o SPDX (JSON o XML).
- **Generazione**: Automatizzata tramite pipeline di build (ogni build genera uno SBOM aggiornato). Strumenti: [Strumento SBOM — ad esempio, syft, cdxgen, cyclonedx-maven-plugin o equivalente specifico per linguaggio].
- **Contenuto**: Tutte le dipendenze dirette e transitive, versioni, licenze, fornitori, vulnerabilità note.
- **Copertura**: Applicazioni di produzione — SBOM richiesto (copertura 100%). Strumenti interni — SBOM richiesto. Prove di concetto / esperimenti — SBOM raccomandato (se il codice persiste >30 giorni).
- **Archiviazione e accesso**: Gli SBOM vengono archiviati in [Repository di artefatti / Dependency Track / Piattaforma SBOM], accessibili al Team di sviluppo, al Team di sicurezza, al Legale (per la conformità delle licenze) e al team di risposta agli incidenti. Ogni SBOM deve essere taggato con la versione corrispondente dell'applicazione (relazione 1:1).
- **Utilizzo**: Gestione delle vulnerabilità (lo strumento SCA acquisisce l'SBOM, lo confronta con i database CVE, identifica le applicazioni interessate); conformità delle licenze (il team Legale revisiona l'SBOM per i conflitti di licenze); risposta agli incidenti (quando viene divulgata una nuova vulnerabilità, interroga il repository SBOM per identificare le applicazioni interessate entro poche ore); trasparenza della catena di approvvigionamento (richieste di audit di terze parti o due diligence dei clienti).
- **Validazione dell'accuratezza**: Audit trimestrale — campione del 10% delle applicazioni, confronto dell'SBOM con le dipendenze effettivamente distribuite (analisi binaria). Se l'SBOM non corrisponde alla realtà, investigare la causa principale (problema del processo di build, installazione manuale delle dipendenze).
- **Eccezioni**: Applicazioni legacy senza pipeline di build — generazione manuale dell'SBOM trimestrale (interim fino alla migrazione o dismissione dell'applicazione legacy). Software COTS di terze parti — richiedere l'SBOM al fornitore (se il fornitore non lo fornisce, documentare il gap nel registro dei rischi).
- **Tempistica**: Tutte le applicazioni di produzione devono generare SBOM entro [Data — suggerire 6 mesi dalla data di entrata in vigore della politica]. Implementazione graduale: applicazioni critiche prima (Mesi 1–3), poi tutta la produzione (Mesi 4–6).

**Gestione delle versioni delle dipendenze (blocco e aggiornamento)**:

Il blocco delle versioni delle dipendenze garantisce build riproducibili ma crea un rischio di obsolescenza se le versioni non vengono mai aggiornate. L'organizzazione deve mantenere una cadenza di aggiornamento delle dipendenze per bilanciare la stabilità con la sicurezza.

- **File di blocco**: Richiesti (package-lock.json, Gemfile.lock, poetry.lock, go.sum, ecc.).
- **Intervalli variabili**: Vietati per la produzione (`*`, `>=`, `^` consentiti solo in ambienti non di produzione).
- **Versioni esatte**: Bloccate nel file di blocco (ad esempio, `lodash@4.17.21` non `lodash@^4.0.0`).

**Cadenza di aggiornamento delle dipendenze**:

| Tipo di aggiornamento | Frequenza | Elemento scatenante | Ambito della revisione |
|----------------------|-----------|---------------------|------------------------|
| **Patch di sicurezza** (correzioni di vulnerabilità) | Immediato | Avviso SCA (CVE Critica/Alta) | Mirato (solo dipendenza interessata) |
| **Aggiornamenti minori** (retrocompatibili) | Mensile | Finestra di manutenzione programmata | Aggiornamento batch (più dipendenze contemporaneamente) |
| **Aggiornamenti principali** (modifiche incompatibili) | Trimestrale o per dipendenza | Manutenzione programmata o lavoro su funzionalità pianificate | Valutazione individuale per dipendenza |

**Procedura di aggiornamento**:
1. **Identificare gli aggiornamenti**: Lo strumento SCA segnala le dipendenze obsolete, o Dependabot/Renovate genera una PR.
2. **Revisionare il changelog**: Verificare le note di rilascio per modifiche incompatibili, correzioni di sicurezza, nuove funzionalità.
3. **Aggiornare e testare**: Aggiornare il file di blocco, eseguire la suite di test completa (unitari, di integrazione, E2E).
4. **Scansione di sicurezza**: Eseguire SAST e SCA sulle dipendenze aggiornate.
5. **Distribuire**: Seguire il processo di gestione delle modifiche (staging poi produzione).
6. **Monitorare**: Monitoraggio post-distribuzione per regressioni (tassi di errore, prestazioni).

**Aggiornamenti automatici delle dipendenze** (raccomandati):
- Strumento: Dependabot, Renovate o equivalente.
- Configurazione: Creazione automatica di PR per le patch di sicurezza (auto-merge se i test superano), revisione manuale per aggiornamenti minori/principali.
- SLA di revisione: Patch di sicurezza revisionate entro 2 giorni lavorativi, aggiornamenti minori entro 1 settimana.

**Limiti di obsolescenza delle dipendenze**:
- Dipendenze critiche (autenticazione, crittografia, framework web): Nessuna versione con più di 12 mesi.
- Dipendenze standard: Nessuna versione con più di 24 mesi.
- Esenzione: Se la versione più recente presenta problemi noti, documentare perché viene mantenuta la versione precedente (con controlli compensativi — monitoraggio potenziato).

**Metriche di gestione delle dipendenze**:
- Età media delle dipendenze (giorni dalla data di rilascio della versione).
- Percentuale di dipendenze con vulnerabilità note.
- Frequenza di aggiornamento delle dipendenze (aggiornamenti al mese).
- Tempo dalla divulgazione del CVE alla distribuzione della patch.
- Obiettivo: Età media delle dipendenze <180 giorni; <1% di dipendenze con CVE Critiche/Alte note.

**SLA di remediation per le vulnerabilità delle dipendenze**:

| Gravità | Punteggio CVSS | SLA di remediation |
|---------|----------------|-------------------|
| Critica | 9,0–10,0 | 7 giorni |
| Alta | 7,0–8,9 | 30 giorni |
| Media | 4,0–6,9 | 90 giorni |
| Bassa | 0,1–3,9 | Prossimo rilascio pianificato |

---

## Requisiti per la code review

Tutte le modifiche al codice devono essere revisionate prima del merge nei branch protetti.

**Tipi di revisione**:

| Tipo di revisione | Quando richiesto | Revisore |
|-------------------|-----------------|---------|
| Revisione tra pari del codice | Tutte le modifiche al codice | Almeno uno sviluppatore diverso dall'autore |
| Revisione del codice focalizzata sulla sicurezza | Modifiche al codice di autenticazione, autorizzazione, crittografia, validazione degli input, gestione delle sessioni o protezione dei dati | Sviluppatore con formazione sulla sicurezza o Security Champion |
| Revisione automatica del codice | Tutte le modifiche al codice | [Strumento SAST] integrato nella pipeline CI/CD |

**Requisiti di code review basati sul rischio**:

Il numero di revisori e le loro qualifiche devono essere determinati dalla classificazione del rischio della modifica al codice:

**Codice standard** (non critico per la sicurezza):
- Revisori: Minimo 1 sviluppatore tra pari (non l'autore).
- Qualifiche: Qualsiasi sviluppatore del team con >3 mesi di esperienza.
- Approvazione: 1 approvazione richiesta per il merge.

**Codice critico per la sicurezza** (autenticazione, autorizzazione, gestione delle sessioni, validazione degli input, crittografia, protezione dei dati):
- Revisori: Minimo 2 revisori: (1) Sviluppatore tra pari (chiunque nel team), E (2) Security Champion O membro del Team di sicurezza (obbligatorio).
- Qualifiche: Il Security Champion deve aver completato la formazione Security Champion.
- Approvazione: Entrambi i revisori devono approvare prima del merge.

**Codice di infrastruttura/distribuzione** (IaC, modifiche alla pipeline CI/CD, gestione della configurazione):
- Revisori: Minimo 1 tra pari + approvazione del responsabile DevOps.
- Qualifiche: Il revisore deve comprendere le implicazioni sull'infrastruttura.
- Approvazione: 2 approvazioni richieste.

**Modifiche ad alto rischio** (API rivolte all'esterno, elaborazione dei pagamenti, funzioni amministrative):
- Revisori: 2 tra pari + membro del Team di sicurezza (3 in totale).
- Testing: Devono includere test di sicurezza automatizzati (SAST superato, test di integrazione superati).
- Approvazione: Tutti e 3 i revisori approvano + i test automatizzati superano.

**Integrità a due persone** (script di rotazione dei segreti, codice di escalation dei privilegi, bypass dei controlli di sicurezza):
- Revisori: 2 sviluppatori senior O 1 senior + membro del Team di sicurezza.
- Approvazione: Entrambi approvano + RSSI notificato (a conoscenza, nessuna approvazione richiesta a meno che non si tratti di una modifica alla produzione).

**Disponibilità dei Security Champion**:
- Minimo 1 Security Champion per team di sviluppo (rapporto 1:8 sviluppatori).
- I Security Champion devono avere un'allocazione di tempo dedicata per le revisioni della sicurezza (10% del tempo di lavoro).
- Se il Security Champion non è disponibile: il Team di sicurezza deve fornire la revisione entro 48 ore.

Documentazione: La descrizione della PR deve indicare il tipo di revisione richiesta in base alla classificazione del codice (standard, critico per la sicurezza, ad alto rischio). I controlli CI/CD devono verificare che il numero di approvazioni della revisione soddisfi il requisito.

**Requisiti per la revisione tra pari del codice**:

- L'autore del codice non deve approvare il proprio codice (separazione dei compiti).
- I revisori devono verificare la conformità agli standard di codifica sicura dell'organizzazione.
- I revisori devono verificare: segreti hardcoded, schemi di codifica non sicuri, validazione degli input mancante, codifica degli output mancante, autorizzazioni eccessive, gestione degli errori inadeguata e registrazione mancante.
- Le pull request devono includere una descrizione delle modifiche, un collegamento al problema o al ticket correlato e prove del testing.
- Le revisioni devono essere completate prima che il codice venga unito a un branch protetto.

**Checklist per la code review focalizzata sulla sicurezza**:

- [ ] Validazione degli input applicata a tutti gli input esterni
- [ ] Codifica degli output applicata ai punti di visualizzazione
- [ ] Nessun segreto, chiave o credenziale hardcoded
- [ ] Query parametrizzate utilizzate per le interazioni con il database
- [ ] L'autenticazione e la gestione delle sessioni utilizzano librerie approvate
- [ ] I messaggi di errore non divulgano dettagli interni
- [ ] Gli eventi rilevanti per la sicurezza vengono registrati
- [ ] I dati sensibili non vengono registrati
- [ ] Le operazioni crittografiche utilizzano algoritmi e librerie approvati
- [ ] I controlli degli accessi sono lato server e applicati per ogni richiesta
- [ ] Le dipendenze sono bloccate e prive di vulnerabilità critiche note

---

## Static Application Security Testing (SAST)

L'analisi statica automatizzata deve essere integrata nel flusso di lavoro di sviluppo per rilevare i difetti di sicurezza prima della distribuzione.

**Requisiti**:

- L'organizzazione deve implementare uno strumento SAST ([Strumento SAST] — ad esempio, SonarQube, Semgrep, CodeQL, Checkmarx o equivalente) integrato nella pipeline CI/CD.
- Le scansioni SAST devono essere eseguite su ogni pull request o merge request verso un branch protetto.
- I risultati SAST devono essere revisionati prima del merge. I risultati critici e ad alta gravità devono bloccare il merge fino alla risoluzione o all'accettazione esplicita come falsi positivi con giustificazione documentata.
- I set di regole SAST devono coprire, come minimo, le classi di vulnerabilità OWASP Top 10 e CWE/SANS Top 25.
- I falsi positivi devono essere documentati e soppressi seguendo la procedura di soppressione indicata di seguito. La soppressione senza giustificazione e revisione tra pari è vietata.
- La configurazione dello strumento SAST e i set di regole devono essere revisionati annualmente dal Responsabile sviluppo e dal Team di sicurezza.

**Procedura di soppressione dei falsi positivi SAST**:

Sopprimere un risultato SAST come falso positivo senza revisione tra pari è vietato. Gli sviluppatori potrebbero inavvertitamente sopprimere vulnerabilità reali.

**Processo di richiesta di soppressione**:
1. Lo sviluppatore identifica il risultato SAST ritenuto un falso positivo.
2. Lo sviluppatore documenta nella richiesta di soppressione: ID del risultato, perché il risultato è un falso positivo (giustificazione tecnica), frammento di codice che mostra perché la regola non si applica e metodo di soppressione proposto (commento inline, file di configurazione).
3. **Revisione tra pari richiesta**: Un altro sviluppatore O Security Champion deve revisionare la richiesta di soppressione.
4. **Approvazione del Team di sicurezza** (per risultati Critici/Alti): Il Team di sicurezza deve approvare la soppressione dei risultati a gravità Critica/Alta. I risultati Media/Bassa possono essere approvati da un revisore tra pari.
5. Soppressione applicata: Commento inline + aggiornamento del file di configurazione dello strumento (doppia documentazione).

**Modello di giustificazione della soppressione** (commento inline):
```
// SAST-SUPPRESS: [Nome strumento] [ID regola] - [Data]
// Motivo: [Breve spiegazione del perché si tratta di un falso positivo]
// Revisionato da: [Nome revisore]
// Approvato da: [Membro del Team di sicurezza] (se Critico/Alto)
```

**Audit delle soppressioni**:
- Revisione trimestrale: Il Team di sicurezza deve campionare il 20% dei risultati soppressi.
- Rivalidare: Le soppressioni sono ancora valide? (il codice è cambiato, la regola è stata aggiornata, nuovo contesto?)
- Revocare: Se la soppressione non è più giustificata, rimuovere la soppressione e rimediare al risultato.

**Metriche delle soppressioni monitorate**:
- Soppressioni attive totali per gravità.
- Tasso di soppressione (percentuale di risultati SAST soppressi rispetto a quelli rimediati).
- Età media delle soppressioni (soppressioni vecchie revisionate per la validità continua).
- Soppressioni revocate (quante soppressioni si sono rivelate in seguito errate).

**Segnali d'allarme** (attivano la revisione del Team di sicurezza):
- Lo sviluppatore sopprime >5 risultati in una singola PR (insolito — suggerisce uso improprio).
- Il team sopprime >20% dei risultati Critici/Alti (suggerisce la necessità di tarare le regole o che il team non comprende lo strumento).
- Soppressione senza giustificazione adeguata (generico "non applicabile" — insufficiente).

Obiettivo: <5% dei risultati SAST soppressi (>95% rimediati o confermati come falsi positivi con giustificazione documentata).

**Requisiti di copertura SAST**:

| Classificazione dell'applicazione | Frequenza di scansione | Revisione dei risultati |
|-----------------------------------|------------------------|-------------------------|
| Applicazioni di produzione | Per commit / pull request | Prima del merge |
| Strumenti interni | Per commit / pull request | Prima del merge |
| Prove di concetto | Settimanale (se archiviate nei repository dell'organizzazione) | Triage settimanale |

---

## Formazione sulla codifica sicura

Gli sviluppatori devono ricevere una formazione per scrivere codice sicuro in modo efficace.

**Requisiti di formazione**:

| Tipo di formazione | Destinatari | Frequenza | Durata minima |
|--------------------|-------------|-----------|---------------|
| Fondamenti della codifica sicura | Tutti gli sviluppatori (inclusi i collaboratori) | Prima di scrivere codice di produzione | 4 ore |
| Aggiornamento annuale | Tutti gli sviluppatori | Annualmente | 2 ore |
| Formazione Security Champion | Security Champion designati | Iniziale + annuale | 8 ore iniziali; 4 ore di aggiornamento |
| Codifica sicura specifica per linguaggio | Sviluppatori che adottano un nuovo linguaggio | Prima dell'uso in produzione di quel linguaggio | 2 ore |

**Il contenuto della formazione** deve coprire, come minimo:

- Classi di vulnerabilità OWASP Top 10 e CWE/SANS Top 25.
- Standard di codifica sicura applicabili al linguaggio principale dello sviluppatore.
- Validazione degli input, codifica degli output e prevenzione dell'iniezione.
- Schemi di autenticazione, gestione delle sessioni e controllo degli accessi.
- Gestione dei segreti e il divieto di credenziali hardcoded.
- Uso sicuro delle librerie crittografiche.
- Gestione delle dipendenze e sicurezza della catena di approvvigionamento.
- Uso degli strumenti SAST e SCA dell'organizzazione.

**Prove di formazione**: I registri di completamento devono essere mantenuti in [Sistema HR / LMS] e revisionati trimestralmente dal Responsabile sviluppo.

**Applicazione dei requisiti di formazione sulla codifica sicura**:

I requisiti di formazione devono essere applicati attraverso conseguenze crescenti per la non conformità:

**Requisiti di completamento** (per la tabella dei requisiti di formazione):
- Fondamenti della codifica sicura: Prima di scrivere codice di produzione (nuovi assunti, collaboratori).
- Aggiornamento annuale: Entro 30 giorni dalla data anniversario (tutti gli sviluppatori).
- Specifico per linguaggio: Prima dell'uso in produzione del nuovo linguaggio.
- Formazione Security Champion: Entro 30 giorni dalla nomina.

**Conseguenze della non conformità** (crescenti):

| Giorni di ritardo | Azione | Autorità |
|-------------------|--------|----------|
| **0–14 giorni** | E-mail di promemoria (automatica) | Sistema |
| **15–30 giorni** | Notifica al responsabile + secondo promemoria | Responsabile sviluppo |
| **31–60 giorni** | Approvazione della distribuzione in produzione bloccata (lo sviluppatore non può approvare PR verso branch di produzione) | Responsabile sviluppo |
| **61–90 giorni** | Privilegi di code review sospesi (lo sviluppatore non può revisionare il codice altrui) | Responsabile sviluppo + RSSI |
| **>90 giorni** | Accesso ai sistemi di produzione sospeso (non può distribuire, non può accedere agli ambienti di produzione) | RSSI |

**Esenzioni temporanee**:
- Congedo a lungo termine (parentale, medico): La scadenza della formazione viene estesa a 30 giorni dal rientro.
- Esigenza aziendale urgente (incidente critico, emergenza del cliente): Il RSSI concede un'estensione di 30 giorni con giustificazione documentata.

**Verifica del completamento della formazione**:
- Automatizzata: Il sistema LMS/HR invia lo stato di completamento a [Strumento di distribuzione] o [Piattaforma di code review].
- Controllo pre-distribuzione: La pipeline CI/CD verifica lo stato della formazione prima di consentire la distribuzione in produzione (se lo sviluppatore non è conforme, la distribuzione viene bloccata con il motivo "Formazione scaduta — completare [Nome formazione]").

**Metriche di applicazione della formazione**:
- Percentuale di sviluppatori con formazione corrente (obiettivo: >95% entro 30 giorni dalla data di scadenza).
- Tempo medio di completamento della formazione (giorni dalla data di scadenza al completamento).
- Numero di sviluppatori con privilegi sospesi (obiettivo: 0).

**Comunicazioni**:
- 30 giorni prima della scadenza: Promemoria "Formazione in scadenza a breve".
- 7 giorni prima della scadenza: Promemoria "Formazione in scadenza questa settimana".
- Alla data di scadenza: Notifica "Formazione scaduta" allo sviluppatore + responsabile.
- Promemoria automatici: Settimanali fino al completamento della formazione.

Applicazione attiva da [Data — suggerire 3 mesi dopo la data di entrata in vigore della politica per consentire agli sviluppatori esistenti di aggiornarsi].

---

## Pratiche di codifica non sicura — divieto

Le seguenti pratiche di codifica sono vietate:

| Pratica vietata | Motivo | Alternativa richiesta |
|-----------------|--------|----------------------|
| Password, chiavi API o segreti hardcoded nel codice sorgente | I segreti vengono esposti tramite l'accesso al repository o le fughe di codice | Usare variabili di ambiente o la gestione dei segreti approvata ([Gestore segreti]) |
| Costruzione di istruzioni SQL mediante concatenazione di stringhe con input utente | Vulnerabilità SQL injection | Usare query parametrizzate o prepared statement |
| Deserializzazione di dati non attendibili senza validazione | Rischio di esecuzione di codice remoto | Validare e sanificare prima della deserializzazione; usare librerie di deserializzazione sicure |
| Uso di algoritmi crittografici deprecati o non sicuri (MD5, SHA-1, DES, RC4) | Debolezze note; attacchi a forza bruta o collisioni | Usare algoritmi approvati secondo la politica crittografica |
| Validazione del certificato TLS disabilitata o bypassata | Esposizione agli attacchi man-in-the-middle | Applicare la validazione del certificato in tutti gli ambienti tranne i test isolati |
| Campioni di codice non approvati copiati da fonti pubbliche senza revisione | Possono contenere vulnerabilità, backdoor o violazioni di licenza | Rivedere e adattare; verificare la compatibilità della licenza; eseguire la scansione con SAST |
| Registrazione di dati sensibili (password, token, dati personali) | Esposizione dei dati attraverso i file di log | Usare la mascheratura dei dati o escludere i campi sensibili dalla registrazione |
| Uso di `eval()` o equivalente esecuzione dinamica di codice con input utente | Vulnerabilità di iniezione di codice | Usare alternative sicure; validare e sanificare gli input |

### Rilevamento di segreti hardcoded (strumenti obbligatori)

Il divieto di segreti hardcoded nella tabella sopra deve essere applicato attraverso il rilevamento automatizzato a più livelli.

**Scansione pre-commit** (raccomandata, workstation dello sviluppatore):
- Strumento: [git-secrets / Talisman / detect-secrets] installato sulle macchine degli sviluppatori.
- Scansiona i commit per i pattern regex (chiavi API, chiavi private, password, token).
- Blocca il commit se vengono rilevati segreti (lo sviluppatore deve rimuoverli prima di ricommittare).
- Onboarding: Tutti gli sviluppatori devono essere istruiti ad installare l'hook pre-commit durante l'onboarding.

**Scansione della pipeline CI/CD** (obbligatoria, livello di applicazione):
- Strumento: [GitGuardian / TruffleHog / Gitleaks] integrato nella pipeline CI/CD.
- Scansiona ogni commit/PR per i pattern dei segreti.
- Le build devono fallire se vengono rilevati segreti (nessun merge fino alla remediation).
- Avviso: Il Team di sicurezza viene notificato immediatamente dei segreti rilevati (gravità Critica).

**Scansione del repository** (periodica, rilevamento storico):
- Strumento: GitHub Advanced Security / GitLab Secret Detection / scanner dedicato.
- Scansiona l'intera cronologia del repository (non solo i nuovi commit — rileva i segreti storici).
- Frequenza: Scansione completa del repository settimanale.
- Remediation: I segreti trovati nella cronologia richiedono: rimozione dalla cronologia (git filter-repo), rotazione del segreto compromesso (presumere compromesso) e documentazione dell'incidente nel log delle violazioni dei segreti.

**Pattern minimi di segreti rilevati**:
- Chiavi AWS (AKIA..., pattern AWS Secret Access Key).
- Chiavi API (pattern generici di chiavi API, formati specifici del fornitore).
- Chiavi private (intestazioni di chiavi RSA, SSH, PGP).
- Password dei database (stringhe di connessione con credenziali incorporate).
- Token OAuth, segreti JWT, chiavi crittografiche.

**Procedura di remediation dei segreti**:
1. **Immediato**: Lo sviluppatore rimuove il segreto dal codice, committa la correzione.
2. **Entro 1 ora**: Il segreto viene ruotato (presumere compromesso anche se solo nel branch di sviluppo).
3. **Entro 24 ore**: La cronologia del repository viene pulita (se il segreto è stato committato — usare git filter-repo o BFG Repo-Cleaner).
4. **Entro 48 ore**: Rapporto dell'incidente presentato al RSSI (come è stato committato il segreto, valutazione dell'impatto, azioni preventive).

**Eccezioni** (rare):
- Fixture di test con segreti fittizi (chiaramente contrassegnati come falsi, non funzionali).
- Frammenti di codice di esempio nella documentazione (chiaramente contrassegnati come esempi, utilizzando valori segnaposto come `your-api-key-here`).

Documentazione: La configurazione dello strumento di rilevamento dei segreti deve essere mantenuta in [Repository di configurazione CI/CD] e revisionata trimestralmente dal Team di sicurezza.

---

## Sviluppo in outsourcing

Il codice prodotto da collaboratori esterni e team di sviluppo in outsourcing deve soddisfare gli stessi standard di codifica sicura del codice sviluppato internamente.

**Requisiti contrattuali**:

- I contratti devono richiedere l'adesione agli standard di codifica sicura dell'organizzazione e a questa politica.
- I collaboratori devono fornire prove della formazione sulla codifica sicura per i loro sviluppatori.
- Tutto il codice prodotto dai collaboratori deve essere sottoposto allo stesso processo di code review e scansione SAST del codice interno.
- I collaboratori devono rimediare ai risultati di sicurezza entro gli SLA definiti dall'organizzazione.
- L'organizzazione si riserva il diritto di verificare le pratiche di codifica sicura del collaboratore.

**Verifica**:

- Il codice del collaboratore deve essere revisionato da uno sviluppatore interno prima del merge.
- I risultati SAST e SCA per il codice prodotto dai collaboratori devono essere visibili al Team di sicurezza dell'organizzazione.
- Il codice ad alto rischio prodotto dai collaboratori (autenticazione, autorizzazione, crittografia, protezione dei dati) deve ricevere una code review focalizzata sulla sicurezza da parte di un Security Champion o Architetto della sicurezza.

**Garanzia di qualità dello sviluppo in outsourcing**:

Oltre alla code review e alla scansione continue, l'organizzazione deve condurre audit periodici del codice prodotto dai collaboratori per verificare la qualità e la conformità continuative.

**Audit trimestrale dei collaboratori** (per ogni contratto attivo):
- Dimensione del campione: 10% del codice prodotto dal collaboratore (minimo 5 PR/MR) del trimestre precedente.
- Ambito dell'audit:
  - Conformità alla sicurezza: Il codice segue gli standard di codifica sicura? (validazione degli input, codifica degli output, nessun segreto hardcoded, ecc.)
  - Qualità del codice: Leggibilità, manutenibilità, copertura dei test.
  - Documentazione: Commenti al codice adeguati? Decisioni architetturali documentate?
- Revisore: Sviluppatore senior interno O membro del Team di sicurezza (non la stessa persona che ha eseguito la revisione iniziale — controllo indipendente).
- Risultati: Documentati nel Rapporto di audit del collaboratore con gravità (Critica/Alta/Media/Bassa).

**Gestione dei risultati dell'audit**:
- Critici/Alti: Escalare immediatamente alla direzione del collaboratore, rimediare entro 14 giorni, considerare la revisione del contratto se emerge un modello.
- Medi/Bassi: Feedback fornito al collaboratore, rimediare nel prossimo sprint/rilascio.

**Valutazione delle prestazioni del collaboratore**:
- Metriche: Tasso di risultati SAST/SCA (risultati per KLOC), tasso di rifiuto della code review, tasso di risultati dell'audit, tasso di incidenti di sicurezza (incidenti causati dal codice del collaboratore).
- Scorecard trimestrale: Condivisa con la direzione del collaboratore.
- Prestazioni scadenti: 3 trimestri consecutivi al di sotto della soglia devono attivare la revisione del contratto e la possibile risoluzione.

**Valutazione annuale della sicurezza del collaboratore** (completa):
- Ambito: Revisione del processo di sviluppo sicuro del collaboratore, programma di formazione, strumenti, qualità del codice dell'anno passato.
- Metodo: Questionario + colloquio + analisi approfondita dei campioni di codice.
- Output: Rapporto di valutazione della sicurezza del collaboratore con raccomandazioni.
- Azione: I collaboratori devono affrontare le raccomandazioni Critiche/Alte entro 90 giorni.

Documentazione: I rapporti di audit dei collaboratori devono essere conservati per la durata del contratto + 3 anni.

---

## Framework del programma Security Champion

I Security Champion sono fondamentali per incorporare la sicurezza all'interno dei team di sviluppo. Il seguente framework formalizza il ruolo di Security Champion con chiara responsabilità, allocazione del tempo e supporto.

**Selezione e nomina**:
- Rapporto: 1 Security Champion per team di sviluppo (o per 8 sviluppatori se i team sono più grandi).
- Selezione: Volontario preferito, nominato dal Responsabile sviluppo in assenza di volontari.
- Qualifiche: Sviluppatore di livello medio o senior, interesse per la sicurezza, buone capacità comunicative.
- Mandato: Mandato di 12 mesi (rinnovabile), con tutoraggio di 6 mesi per i nuovi Security Champion.

**Responsabilità** (formali, documentate nella descrizione del ruolo):
- Code review focalizzate sulla sicurezza (tutto il codice critico per la sicurezza del team).
- Tutoraggio sulla codifica sicura (aiutare i membri del team a comprendere i problemi di sicurezza).
- Triage SAST/SCA (revisione in prima linea dei risultati delle scansioni, escalare al Team di sicurezza se necessario).
- Partecipazione alla modellazione delle minacce (per nuove funzionalità/modifiche significative).
- Collegamento con il Team di sicurezza (partecipare alle riunioni mensili dei Security Champion, trasferire gli aggiornamenti sulla sicurezza al team).
- Supporto alla risposta agli incidenti di sicurezza (assistere il Team di sicurezza durante gli incidenti che riguardano il codice del team).

**Allocazione del tempo**:
- 10% del tempo di lavoro dedicato alle attività di Security Champion (~4 ore/settimana).
- Il tempo di code review conta per l'allocazione del 10%.
- Gestito dal Responsabile sviluppo (garantire che il Security Champion abbia tempo, non sia sovraccaricato di lavoro sulle funzionalità).

**Formazione e sviluppo**:
- Formazione iniziale: 8 ore (modellazione delle minacce, code review sicura, approfondimento OWASP Top 10, strumenti SAST/SCA).
- Aggiornamento annuale: 4 ore (nuove vulnerabilità, aggiornamenti degli strumenti, casi di studio).
- Facoltativo: Partecipazione a conferenze (OWASP AppSec, conferenze sulla sicurezza), corsi online.

**Supporto e risorse**:
- Riunione mensile della community dei Security Champion (apprendimento tra pari, casi di studio, domande e risposte con il Team di sicurezza).
- Canale di comunicazione dedicato (supporto asincrono, condivisione delle conoscenze).
- Accesso al Team di sicurezza per l'escalation (SLA di risposta entro 24 ore).
- Riconoscimento: Ringraziamento pubblico (assemblee, newsletter), possibile considerazione per bonus/promozione.

**Metriche di prestazione** (misurate trimestralmente):
- Code review focalizzate sulla sicurezza completate (obiettivo: 100% del codice critico per la sicurezza).
- Risultati SAST triagiti entro l'SLA (obiettivo: 95% entro 48 ore).
- Incidenti di sicurezza che coinvolgono il codice del team (tendenza al ribasso nel tempo).
- Completamento della formazione sulla sicurezza per gli sviluppatori del team (il Security Champion incoraggia la formazione del team).

**Pianificazione della successione**:
- Programma shadow: Identificare il successore 3 mesi prima della fine del mandato, affiancare il Security Champion attuale.
- Trasferimento delle conoscenze: Documentato nel Manuale del Security Champion.

**Governance del programma**:
- Proprietario del programma: RSSI o Responsabile del Team di sicurezza.
- Revisione trimestrale del programma: Metriche, feedback dei Security Champion, miglioramenti del programma.
- Valutazione annuale della maturità del programma: Copertura (tutti i team hanno Security Champion?), coinvolgimento (i Security Champion sono attivi?), efficacia (i risultati sulla sicurezza stanno migliorando?).

Documentazione: Il Registro dei Security Champion deve essere mantenuto in [Sistema HR / Wiki] con nomi, team, date di nomina e completamento della formazione.

---

## Gestione delle eccezioni

Le eccezioni a questa politica devono essere richieste per iscritto e devono includere:

- Requisito/i specifici che richiedono un'eccezione.
- Giustificazione aziendale.
- Controlli compensativi.
- Durata richiesta dell'eccezione (massimo 12 mesi).
- Valutazione e accettazione del rischio.

Le eccezioni devono essere approvate dal Responsabile sviluppo e dal Responsabile della sicurezza delle informazioni (obbligatori), più il RSSI per le eccezioni alle applicazioni di produzione. Tutte le eccezioni attive devono essere revisionate trimestralmente.

Laddove sia tecnicamente impossibile soddisfare un requisito (ad esempio, una base di codice legacy che non può essere immediatamente sottoposta a refactoring), devono essere implementati controlli compensativi, documentati, verificati dal Responsabile della sicurezza delle informazioni e revisionati annualmente.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **CSP** | Content Security Policy — intestazione di risposta HTTP che limita le risorse che un browser è autorizzato a caricare per una pagina, mitigando i rischi XSS |
| **CWE** | Common Weakness Enumeration — un elenco sviluppato dalla community di tipi di debolezze del software e dell'hardware |
| **Dipendenza** | Una libreria, un framework o un componente di terze parti utilizzato dal codice applicativo |
| **Iniezione** | Una classe di vulnerabilità in cui dati non attendibili vengono inviati a un interprete come parte di un comando o di una query (ad esempio, SQL injection, XSS, command injection) |
| **OWASP** | Open Worldwide Application Security Project — fondazione non-profit che produce standard, strumenti e guida per la sicurezza delle applicazioni |
| **Query parametrizzata** | Una tecnica di query al database che separa la logica SQL dai dati forniti dall'utente, prevenendo l'SQL injection |
| **SAST** | Static Application Security Testing — analisi automatizzata del codice sorgente per identificare i difetti di sicurezza senza eseguire l'applicazione |
| **SBOM** | Software Bill of Materials — un inventario leggibile da macchina di tutti i componenti, le librerie e le dipendenze in un'applicazione software |
| **SCA** | Software Composition Analysis — scansione automatizzata delle dipendenze di terze parti per vulnerabilità note e rischi di licenza |
| **Security Champion** | Uno sviluppatore con formazione specializzata nella sicurezza che funge da referente per la sicurezza all'interno di un team di sviluppo |
| **TLS** | Transport Layer Security — protocollo crittografico per la protezione dei dati in transito |
| **XSS** | Cross-Site Scripting — una vulnerabilità che consente agli attaccanti di iniettare script dannosi nelle pagine web visualizzate da altri utenti |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RSSI** | Titolarità della politica; approvazione delle eccezioni per le applicazioni di produzione; supervisione della conformità alla codifica sicura; revisione annuale della politica; reportistica alla Direzione generale; governance del programma Security Champion |
| **Responsabile sviluppo** | Manutenzione degli standard di codifica sicura (per linguaggio); applicazione della code review; selezione e configurazione degli strumenti SAST/SCA; coordinamento della formazione degli sviluppatori; reportistica sulla conformità al RSSI; garanzia dell'allocazione del tempo dei Security Champion |
| **Responsabile della sicurezza delle informazioni** | Manutenzione della politica; revisione delle eccezioni; monitoraggio della sicurezza e indagine sugli incidenti; coordinamento degli audit; reportistica trimestrale sulla conformità al RSSI |
| **Security Champion** | Code review focalizzate sulla sicurezza; tutoraggio sulla codifica sicura all'interno dei team di sviluppo; promozione degli standard di codifica sicura; triage dei risultati SAST/SCA; partecipazione alla modellazione delle minacce; escalation delle preoccupazioni di sicurezza al Team di sicurezza |
| **Team di sicurezza** | Gestione degli strumenti SAST/SCA e aggiornamenti dei set di regole; code review focalizzata sulla sicurezza per le modifiche ad alto rischio; coordinamento dei test di sicurezza; risposta agli incidenti per le vulnerabilità a livello di codice; approvazione della soppressione SAST per i risultati Critici/Alti; partecipazione agli audit dei collaboratori |
| **Ingegneri DevOps** | Integrazione degli strumenti SAST e SCA nella pipeline CI/CD; applicazione dei gate di sicurezza nella pipeline di build; infrastruttura di gestione dei segreti; integrazione degli strumenti di scansione dei segreti |
| **Sviluppatori e collaboratori individuali** | Aderenza agli standard di codifica sicura; partecipazione alla code review; remediation tempestiva dei risultati di sicurezza; completamento della formazione sulla codifica sicura; segnalazione degli incidenti per i difetti di sicurezza; installazione dell'hook pre-commit |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|--------------|-----------|---------------|
| 1 | **Registro degli standard di codifica sicura** (linguaggi approvati, framework e riferimenti di codifica associati) | Responsabile sviluppo | Mantenuto continuamente; rivisto annualmente | Versione corrente + 3 anni |
| 2 | **Risultati delle scansioni SAST** (log di esecuzione degli strumenti, risultati, giustificazioni dei falsi positivi) | Responsabile sviluppo / DevOps | Per pull request; rivisti mensilmente | 2 anni |
| 3 | **Risultati delle scansioni SCA delle dipendenze** (risultati delle vulnerabilità, output SBOM, registri di remediation) | Responsabile sviluppo / DevOps | Per build; rivisti mensilmente | 2 anni |
| 4 | **Registri della code review** (revisioni delle pull request, checklist di revisione della sicurezza, registri di approvazione) | Responsabile sviluppo | Per modifica del codice | 3 anni |
| 5 | **Registri della code review focalizzata sulla sicurezza** per le modifiche ad alto rischio (autenticazione, autorizzazione, crittografia) | Security Champion / Team di sicurezza | Per modifica applicabile | 3 anni |
| 6 | **Registri di completamento della formazione sulla codifica sicura** (fondamenti, aggiornamento, specifico per linguaggio, Security Champion) | Responsabile sviluppo / HR | Annualmente; per onboarding | Durata dell'impiego + 3 anni |
| 7 | **Registri di remediation delle vulnerabilità delle dipendenze** (tracciamento dalla scoperta alla chiusura con conformità agli SLA) | Responsabile sviluppo | Per risultato | 3 anni |
| 8 | **Registri di configurazione degli strumenti SAST/SCA** (set di regole, controlli abilitati, giustificazioni delle soppressioni) | Team di sicurezza / DevOps | Rivisti annualmente | Versione corrente + 1 anno |
| 9 | **Registri di violazioni delle pratiche vietate** (incidenti di segreti hardcoded, schemi non sicuri rilevati e rimediati) | Team di sicurezza | Per incidente | 3 anni |
| 10 | **Registro delle eccezioni** (richieste, approvazioni, controlli compensativi, revisioni trimestrali) | Responsabile della sicurezza delle informazioni | Mantenuto continuamente; rivisto trimestralmente | Durata dell'eccezione + 3 anni |
| 11 | **Prove di codifica sicura dello sviluppo in outsourcing** (registri di formazione del collaboratore, registri della code review, conformità agli SLA, rapporti di audit trimestrali, valutazioni annuali della sicurezza) | Responsabile sviluppo / Acquisti | Per contratto; audit trimestrali | Durata del contratto + 3 anni |
| 12 | **Registri della revisione annuale degli standard di codifica sicura** (data di revisione, modifiche apportate, approvazione) | Responsabile sviluppo | Annualmente | 3 anni |
| 13 | **Tendenze dei risultati SAST/SCA** — Report mensili che mostrano i tassi di risultati, i tempi di remediation, i risultati aperti per gravità per il campionamento degli audit SOC 2 | Team di sicurezza | Mensile | 2 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, report degli strumenti SAST/SCA, registri di completamento della code review, registri di completamento della formazione, risultati degli audit delle dipendenze, audit interni ed esterni e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|---------|-----------|--------------------------|
| Modifiche al codice con revisione tra pari completata prima del merge | 100% | Mensile |
| Scansioni SAST eseguite per pull request (applicazioni di produzione) | >= 95% | Mensile |
| Risultati SAST critici/alti rimediati prima del merge o documentati come falsi positivi | >= 95% | Mensile |
| Vulnerabilità critiche/alte delle dipendenze remediate entro l'SLA | >= 90% | Mensile |
| Sviluppatori con formazione sulla codifica sicura corrente | >= 95% | Trimestrale |
| Segreti hardcoded rilevati e rimediati entro 24 ore | 100% | Per incidente |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|------------|------|---------|
| Conformità della code review | 30% | (Modifiche al codice con revisione completata) / Totale modifiche al codice x 100 |
| Copertura SAST | 25% | (Pull request con scansione SAST superata) / Totale pull request x 100 |
| Sicurezza delle dipendenze | 25% | (Vulnerabilità critiche/alte delle dipendenze remediate entro l'SLA) / Totale risultati critici/alti x 100 |
| Conformità alla formazione | 20% | (Sviluppatori con formazione corrente) / Totale sviluppatori x 100 |

**Gestione della non conformità**: Al di sotto del 70% richiede un'escalation immediata al RSSI e un piano di remediation. Tra 70-89% richiede la supervisione del Responsabile della sicurezza delle informazioni con revisioni mensili. Il 90% e oltre segue il monitoraggio trimestrale standard.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni devono essere comunicate al Team di revisione della direzione.

## Non conformità

Un dipendente che si constata abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e comunicate al RSSI.

## Miglioramento continuo

Questa politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare le classi di vulnerabilità emergenti, le modifiche all'OWASP Top 10 e al CWE/SANS Top 25, i nuovi linguaggi di programmazione o framework adottati dall'organizzazione, l'evoluzione degli strumenti SAST/SCA, i risultati degli audit e le lezioni apprese dagli incidenti di sicurezza che coinvolgono vulnerabilità a livello applicativo.

---

# Aree della norma ISO 27001 trattate

Politica sulla codifica sicura — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.4 Accesso al codice sorgente |
| | 8.25 Ciclo di vita dello sviluppo sicuro |
| | 8.26 Requisiti di sicurezza delle applicazioni |
| | **8.28 Codifica sicura** |
| | 8.29 Test di sicurezza nello sviluppo e nell'accettazione |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera (revDSG) | Art. 7 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 8 — Misure tecniche e organizzative; la codifica sicura come misura tecnica preventiva |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati, inclusi i controlli a livello applicativo |
| GDPR UE (ove applicabile) | Art. 25 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controllo Allegato A 8.28 — Codifica sicura |
| ISO/IEC 27002:2022 | Sezione 8.28 — Guida all'implementazione della codifica sicura |
| NIST SP 800-218 (SSDF) v1.1 | PW.4 — Creare codice sorgente aderente alle pratiche di codifica sicura; PW.5 — Configurare il processo di build in modo sicuro; PW.6 — Rivedere e testare il codice |
| NIST SP 800-53 Rev 5 | SA-15 (Development Process, Standards, and Tools), SA-16 (Developer-Provided Training), SA-17 (Developer Security Architecture and Design) |
| CIS Controls v8 | 16.1 (Processo di sviluppo di applicazioni sicure), 16.2 (Gestire l'architettura del software), 16.4 (Proteggere il software sviluppato su misura), 16.12 (Implementare controlli di sicurezza a livello di codice) |
| OWASP Top 10 (2021) | A01–A10 — Categorie di rischio per la sicurezza delle applicazioni web affrontate attraverso pratiche di codifica sicura |
| CWE/SANS Top 25 (2025) | Vulnerabilità software più pericolose affrontate attraverso la validazione degli input, la codifica degli output e gli standard di codifica sicura |

---

<!-- QA_VERIFIED: 2026-04-03 -->
