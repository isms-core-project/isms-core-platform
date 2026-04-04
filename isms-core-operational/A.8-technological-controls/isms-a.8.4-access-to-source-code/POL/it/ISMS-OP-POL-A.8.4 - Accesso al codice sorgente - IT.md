<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.4-IT:operational:OP-POL:a.8.4 -->
**ISMS-OP-POL-A.8.4 — Accesso al codice sorgente**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Accesso al codice sorgente |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.4 |
| **Creatore del documento** | Responsabile della Sicurezza delle Informazioni (RSSI) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|---------|------|--------|---------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.4 — Accesso al codice sorgente
- ISO/IEC 27002:2022 Sezione 8.4 — Linee guida di implementazione per il controllo degli accessi al codice sorgente
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- CIS Controls v8 — Salvaguardia 16.1–16.14 (Sicurezza del software applicativo)

**Controlli Annex A correlati**:

| Controllo | Relazione con l'accesso al codice sorgente |
|---------|------------------------------------|
| A.5.9 Inventario delle informazioni e degli altri asset associati | I repository del codice sorgente inclusi nell'inventario degli asset |
| A.5.15–16–18 Gestione delle identità e degli accessi | Framework IAM fondamentale; autenticazione e autorizzazione per i repository |
| A.5.19–23 Sicurezza dei fornitori e dei servizi cloud | Accesso degli sviluppatori terzi e controlli dei repository cloud |
| A.8.2–3–5 Autenticazione e accesso privilegiato | Requisiti AMF; l'accesso admin trattato come privilegiato |
| A.8.9 Gestione della configurazione | Configurazioni di base della piattaforma repository |
| A.8.15 Registrazione | Registrazione degli audit per l'accesso al repository e le modifiche al codice |
| A.8.25–26–29 Ciclo di vita dello sviluppo sicuro | Codifica sicura, protezione dei rami, integrazione della revisione del codice |
| A.8.32 Gestione delle modifiche | Controllo delle modifiche per il rilascio del codice in produzione |

**Politiche interne correlate**:

- Politica di gestione delle identità e degli accessi
- Politica del ciclo di vita dello sviluppo sicuro
- Politica di registrazione e monitoraggio
- Politica di gestione delle modifiche
- Politica di classificazione e gestione delle informazioni

---

# Politica di accesso al codice sorgente

## Scopo

Lo scopo di questa politica è garantire che l'accesso in lettura e scrittura al codice sorgente, agli strumenti di sviluppo e alle librerie software sia gestito in modo appropriato per proteggere la proprietà intellettuale, prevenire l'introduzione di funzionalità non autorizzate, evitare modifiche non intenzionali o malevole e mantenere la riservatezza degli asset software organizzativi.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative appropriate al rischio per proteggere i dati personali incorporati o trattati dai sistemi di codice sorgente. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32. Il controllo degli accessi al codice sorgente è una misura tecnica fondamentale per dimostrare che i sistemi che trattano dati personali sono soggetti a adeguate restrizioni di accesso.

## Ambito

Repository del codice sorgente, strumenti di sviluppo e librerie software di proprietà, gestiti o controllati dall'organizzazione e considerati nell'ambito dalla dichiarazione di applicabilità ISO 27001. Ciò include:

- Tutti i repository del codice sorgente (applicazioni di produzione, strumenti interni, infrastructure-as-code, gestione della configurazione, contributi open source, codice archiviato).
- Tutte le piattaforme repository ([Piattaforma repository] — ad es. GitHub Enterprise, GitLab, Bitbucket, Azure DevOps o server Git auto-ospitato). L'organizzazione deve documentare le proprie piattaforme repository principali nell'inventario degli asset, inclusi: modello di hosting (cloud o auto-ospitato), residenza dei dati, accordi di backup e controlli degli accessi amministrativi. Dove si utilizzano più piattaforme, questa politica si applica ugualmente a tutte le piattaforme.
- Tutti gli artefatti di sviluppo (codice sorgente, librerie, script di build, codice di test, definizioni di container, definizioni di pipeline CI/CD).

Tutti i dipendenti, i collaboratori esterni e gli utenti terzi con accesso al codice sorgente.

**Fuori ambito**: Binari compilati ed eseguibili; configurazioni di runtime di produzione (coperte da A.8.9); standard di codifica sicura (coperti da A.8.25-26-29); software commerciale di terze parti al quale l'organizzazione non ha accesso al codice sorgente.

## Principio

L'accesso al codice sorgente deve seguire il principio del privilegio minimo. L'accesso viene concesso solo in base a una necessità aziendale documentata e approvata dal proprietario del repository.

L'organizzazione deve amministrare centralmente l'accesso ai repository del codice sorgente utilizzando un sistema di gestione del codice sorgente. Le autorizzazioni predefinite del repository devono essere "nessun accesso" — è necessaria una concessione esplicita per qualsiasi livello di accesso.

Il codice sorgente è classificato come un asset organizzativo critico. L'accesso non autorizzato, la modifica o la divulgazione del codice sorgente possono comportare la perdita di proprietà intellettuale, l'introduzione di vulnerabilità, la non conformità normativa o danni reputazionali.

---

## Classificazione dei repository

Tutti i repository del codice sorgente devono essere classificati per determinare i livelli di protezione appropriati.

**Categorie di classificazione**:

| Classificazione | Descrizione | Esempi |
|----------------|-------------|----------|
| **Produzione** | Codice rilasciato in sistemi di produzione critici per il business o rivolti ai clienti | Applicazione web per i clienti, servizio di elaborazione dei pagamenti, API gateway, backend dell'app mobile |
| **Strumenti interni** | Codice per automazione interna, utility e strumenti operativi | Script pipeline CI/CD, dashboard di monitoraggio, strumenti di amministrazione interni, automazione del rilascio |
| **Open source** | Codice di progetto pubblico o open source a cui l'organizzazione contribuisce | Librerie open-source con fork, contributi alla community, documentazione pubblica |
| **Archiviato** | Codice storico non più in sviluppo attivo | Codice dell'applicazione legacy (dismessa), versioni precedenti del prodotto, proof-of-concept completati |

La classificazione del repository deve essere assegnata dal proprietario del repository al momento della creazione e revisionata annualmente. La classificazione deve essere aggiornata quando lo scopo del repository cambia.

**Repository ereditati e inattivi**: I repository che sono ereditati (ad es. attraverso acquisizioni, ristrutturazioni del team o dimissioni degli sviluppatori) o inattivi (nessun commit da più di 12 mesi) devono essere gestiti come segue:

- **Repository ereditati**: Il responsabile del team ricevente deve essere assegnato come proprietario del repository ad interim entro 5 giorni lavorativi. Il repository deve essere revisionato per l'accuratezza della classificazione, le autorizzazioni di accesso e la conformità alla scansione dei segreti entro 30 giorni.
- **Repository inattivi**: I repository senza attività di commit per 12 mesi devono essere segnalati per revisione. Il proprietario del repository deve confermare: (a) il repository è ancora necessario (mantenere con la classificazione corrente), (b) il repository deve essere archiviato (passare alla classificazione Archiviato, limitare a sola lettura), o (c) il repository deve essere eliminato (seguire la politica di conservazione dei dati). La mancata risposta dopo 30 giorni comporterà l'archiviazione automatica con notifica al Responsabile dello sviluppo.

---

## Controllo degli accessi basato sui ruoli

L'accesso al repository deve essere concesso in base a ruoli definiti con le autorizzazioni minime richieste.

**Ruoli di accesso**:

| Ruolo | Autorizzazioni | Restrizioni |
|------|-------------|--------------|
| **Sviluppatore** | Clone, pull, creazione di rami, push su rami non protetti, invio di pull request | Non può fare push su rami protetti, approvare le proprie pull request o modificare le impostazioni del repository |
| **Revisore di sicurezza** | Accesso in lettura a tutti i repository per revisioni di sicurezza e audit | Non può effettuare commit o modificare le impostazioni a meno che non sia specificamente concesso |
| **Auditor** | Accesso in sola lettura a tempo limitato durante il periodo di audit; accesso ai log di audit e ai rapporti sulle autorizzazioni | L'accesso scade automaticamente al completamento dell'audit |
| **Collaboratore esterno** | Accesso in scrittura a tempo limitato e specifico per repository limitato al lavoro contrattuale | Non può accedere ai repository al di fuori dell'ambito del progetto; tutti i commit soggetti a revisione avanzata; l'accesso scade alla data di fine contratto |
| **Amministratore di repository** | Gestisce le impostazioni del repository, la protezione dei rami e l'accesso dei collaboratori | L'accesso admin non concede automaticamente l'accesso in scrittura al codice (separazione dei compiti); le azioni admin sono registrate |
| **Proprietario del repository** | Approva le richieste di accesso, conduce le revisioni degli accessi, imposta la classificazione | Potrebbe o meno avere l'accesso in scrittura al codice a seconda del ruolo |
| **Account di servizio** | Accesso automatizzato per strumenti CI/CD, rilascio e scansione della sicurezza | Denominazione descrittiva; autenticazione basata su token con scadenza; accesso limitato a repository specifici; proprietario e scopo documentati. Gli scope dei token devono essere minimizzati — ad es. build CI: `repo:read`, `actions:write`; rilascio: `repo:read`, `packages:write`; scanner di sicurezza: `repo:read`, `security_events:write` |

L'accesso admin o owner non deve essere concesso a collaboratori esterni salvo in casi eccezionali documentati con l'approvazione del RSSI.

---

## Richiesta e approvazione degli accessi

Tutte le richieste di accesso al repository devono includere:

- Nome e ruolo del richiedente.
- Nome e classificazione del repository.
- Livello di accesso richiesto (lettura/scrittura/admin).
- Giustificazione aziendale.
- Durata prevista (se limitata nel tempo).

**Requisiti di approvazione**:

| Livello di accesso | Approvatori richiesti |
|--------------|--------------------|
| Accesso in lettura | Proprietario del repository |
| Accesso in scrittura | Proprietario del repository + Team Lead dello sviluppo |
| Accesso admin (qualsiasi repository) | Proprietario del repository + Team Lead dello sviluppo |
| Accesso admin (repository di produzione) | Proprietario del repository + RSSI o delegato |

L'accesso deve essere provisioned entro 24 ore dall'approvazione durante l'orario lavorativo. Le richieste di accesso d'emergenza devono seguire un processo di approvazione accelerato con revisione post-facto entro 48 ore.

Tutte le richieste e le approvazioni degli accessi devono essere documentate e conservate per un minimo di 3 anni.

---

## Revisione degli accessi e deprovisioning

L'accesso al repository deve essere revisionato trimestralmente per confermare la giustificazione aziendale continuata.

**Processo di revisione degli accessi trimestrale**:

1. Il proprietario del repository rivede l'accesso di ogni utente e conferma: accesso ancora richiesto (sì/no), livello di accesso appropriato (sì/no), azione (mantenere/modificare/revocare).
2. Revisione documentata con la conferma del proprietario del repository e la data.
3. Mancata risposta escalata al Responsabile dello sviluppo dopo 10 giorni lavorativi; al RSSI dopo 15 giorni lavorativi.

**Revisione degli account di servizio** (trimestrale):

- L'automazione o la pipeline è ancora attiva? (Segnalare per la rimozione se inattiva da più di 90 giorni.)
- Il proprietario documentato è ancora responsabile?
- Il livello di accesso è ancora appropriato?
- La scadenza del token è impostata in modo appropriato? (Massimo 1 anno; 90 giorni consigliati per gli account ad alto privilegio.)

**Deprovisioning**:

- L'accesso al repository deve essere revocato entro lo stesso giorno lavorativo dalla cessazione del rapporto di lavoro, dal cambio di ruolo che elimina la necessità di accesso, o dalla scadenza del contratto.
- Il deprovisioning automatizzato tramite il sistema di gestione delle identità è preferibile.
- Il deprovisioning deve essere verificato entro 24 ore dall'evento scatenante.

---

## Protezione dei rami e revisione del codice

Il ramo principale (main/master/trunk) dei repository di produzione e strumenti interni deve essere protetto.

**Requisiti di protezione dei rami**:

| Requisito | Produzione | Strumenti interni |
|-------------|------------|----------------|
| Commit diretti bloccati | Sì | Sì |
| Pull request richiesta prima del merge | Sì | Sì |
| Revisori minimi | 2 | 1 |
| Annulla le approvazioni obsolete sui nuovi commit | Sì | Consigliato |
| I controlli di stato devono passare (test CI/CD, linter, scansioni di sicurezza) | Sì | Sì |
| Commit firmati | Consigliato | Opzionale |

I rami di rilascio (release/*, hotfix/*) devono avere la stessa protezione del ramo principale.

Solo gli amministratori del repository possono modificare le regole di protezione dei rami. La rimozione temporanea della protezione del ramo richiede giustificazione documentata, approvazione del RSSI e riabilitazione automatica dopo il periodo specificato.

**Requisiti delle pull request**:

- Tutte le modifiche al codice nei rami protetti devono essere inviate tramite pull request.
- Le pull request non possono essere approvate dall'autore del codice (separazione dei compiti).
- Le pull request devono includere una descrizione chiara delle modifiche, un collegamento all'issue o al ticket correlato dove applicabile, e l'evidenza del testing.
- Le modifiche rilevanti per la sicurezza devono includere una valutazione dell'impatto sulla sicurezza.

**Revisione fast-track**: Le modifiche a basso rischio (aggiornamenti della documentazione, correzioni di errori tipografici, modifiche solo alla configurazione senza logica di codice) possono utilizzare un periodo di revisione di 1 ora per i repository di produzione se etichettate come "basso rischio" o "solo documentazione", limitate a file di documentazione o configurazione, e approvate da un code owner. Periodo di revisione standard per le modifiche al codice di produzione: 4 ore.

---

## Gestione dei segreti

I repository del codice sorgente non devono contenere password, chiavi API, token, chiavi private, stringhe di connessione al database con credenziali incorporate, chiavi SSH private, chiavi di cifratura o qualsiasi altro materiale di autenticazione sensibile.

**Scansione dei segreti**:

Tutti i repository devono avere la scansione automatizzata dei segreti abilitata utilizzando [Strumento di scansione dei segreti] (ad es. GitLeaks, TruffleHog, GitHub Secret Scanning o equivalente).

| Tipo di scansione | Ambito | Frequenza |
|---------------|-------|-----------|
| Scansione pre-commit | Impedisce ai segreti di entrare nel repository | In tempo reale (ad ogni commit) |
| Scansione lato server | Rileva i segreti già presenti nel repository | Scansione completa giornaliera |

I repository di produzione devono avere la scansione pre-commit dei segreti abilitata (modalità bloccante).

La scansione dei segreti deve rilevare segreti generici (pattern basati su regex), segreti specifici del fornitore (chiavi AWS, token GitHub, credenziali Azure) e pattern personalizzati definiti dal team di sicurezza.

**Remediation dei segreti**:

| Classificazione del repository | SLA di remediation |
|---------------------------|-----------------|
| Produzione | 1 ora (rotazione immediata se il segreto è confermato esposto) |
| Strumenti interni | 24 ore |

La remediation deve includere: (1) rotazione immediata del segreto esposto, (2) rimozione dalla cronologia del repository se committato, (3) valutazione dell'impatto (il segreto è stato accessibile da parti non autorizzate?), e (4) segnalazione dell'incidente se necessario.

**Gestione approvata dei segreti**:

| Ambiente | Metodo approvato |
|-------------|-----------------|
| Sviluppo | Variabili d'ambiente; file `.env` esclusi dal controllo versione tramite `.gitignore` |
| Pipeline CI/CD | Archivio segreti della piattaforma ([Piattaforma CI/CD] Secrets o equivalente); nessun segreto hardcoded nelle definizioni della pipeline |
| Produzione | Gestore di segreti dedicato (ad es. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault o equivalente) |

Gli sviluppatori devono essere formati sulle best practice di gestione dei segreti, incluso l'uso di variabili d'ambiente, sistemi di gestione dei segreti e hook pre-commit.

---

## Autenticazione e autenticazione a più fattori

L'accesso ai repository del codice sorgente deve essere autenticato utilizzando metodi approvati: nome utente/password (con AMF), autenticazione con chiave pubblica SSH, token di accesso personali (con scadenza), autenticazione basata su certificato o single sign-on (SSO) tramite il provider di identità organizzativo.

**Requisiti AMF**:

L'autenticazione a più fattori deve essere richiesta per:

- Tutti gli account utente umani con accesso in scrittura o admin ai repository di produzione.
- Tutti gli account utente umani con accesso admin a qualsiasi repository.
- Accesso ai repository tramite web per tutti gli utenti.

Metodi AMF accettati: applicazioni di autenticazione (ad es. Google Authenticator, Microsoft Authenticator, Authy), chiavi di sicurezza hardware (ad es. YubiKey) o notifica push al dispositivo registrato. I codici basati su SMS sono il metodo meno preferito e devono essere utilizzati solo se altri metodi non sono disponibili.

**Chiavi SSH e token di accesso personali**:

- Univoci per utente e dispositivo.
- Protetti con passphrase o archiviazione sicura.
- Ruotati annualmente o immediatamente in caso di sospetta compromissione.
- Revocati in caso di smarrimento o dismissione del dispositivo.

**Account di servizio**: Gli account di servizio non possono eseguire AMF interattiva. I controlli compensativi devono includere: token emessi con scope minimi richiesti, scadenza del token applicata (massimo 1 anno; 90 giorni consigliati per gli account ad alto privilegio), attività registrata e monitorata per anomalie, e revisione trimestrale per la necessità continua.

---

## Registrazione degli audit e monitoraggio

Le piattaforme repository devono registrare i seguenti eventi:

| Categoria di evento | Eventi registrati |
|----------------|---------------|
| **Accesso** | Tentativi di accesso, eventi di logout, durata della sessione |
| **Accesso al repository** | Clone, pull, operazioni di navigazione |
| **Modifiche al codice** | Commit (autore, timestamp, messaggio, file), push, force push |
| **Operazioni sui rami** | Creazione, eliminazione, modifiche alla protezione |
| **Pull request** | Creazione, revisione, approvazione, merge, rifiuto |
| **Modifiche alle autorizzazioni** | Accesso concesso, revocato, cambi di ruolo |
| **Azioni amministrative** | Modifiche alle impostazioni del repository, gestione dei collaboratori |
| **Eventi di sicurezza** | Alert di scansione dei segreti, autenticazione fallita, pattern di accesso sospetti |

I log devono includere: timestamp (UTC), identità dell'utente, indirizzo IP di origine, azione eseguita, repository interessato e stato di successo o fallimento.

**Conservazione dei log**:

| Tipo di evento | Conservazione minima |
|------------|-------------------|
| Eventi di accesso | 1 anno |
| Eventi di modifica del codice | 3 anni |
| Modifiche alle autorizzazioni | 3 anni |
| Eventi di sicurezza | 3 anni |
| Azioni amministrative | 3 anni |

I log devono essere a prova di manomissione e protetti da modifiche o cancellazioni non autorizzate.

**Monitoraggio e alerting**:

I log di accesso al repository devono essere monitorati per: multipli tentativi di autenticazione falliti, accesso da ubicazioni geografiche insolite, accesso al di fuori del normale orario lavorativo, operazioni di download in blocco, tentativi di elevazione dei privilegi, force push su rami protetti e alert di scansione dei segreti.

Gli alert di sicurezza devono essere generati e consegnati al team delle operazioni di sicurezza entro 15 minuti dal rilevamento. Gli eventi critici (accesso non autorizzato confermato, modifiche di massa alle autorizzazioni) devono attivare la risposta immediata agli incidenti secondo il processo di gestione degli incidenti dell'organizzazione. Gli incidenti di sicurezza confermati che coinvolgono il codice sorgente (accesso non autorizzato, manomissione del codice, furto di proprietà intellettuale) devono essere escalati al RSSI entro 1 ora dalla conferma. Dove l'incidente coinvolge dati dei clienti o sistemi di produzione, il processo di gestione degli incidenti (A.5.24-28) deve essere attivato immediatamente.

---

## Backup e ripristino

Tutti i repository del codice sorgente devono essere sottoposti a backup per consentire il ripristino dalla perdita di dati, dalla corruzione o dal guasto della piattaforma.

**Requisiti di backup**:

| Requisito | Standard |
|-------------|----------|
| Frequenza | Incrementale giornaliero; completo settimanale |
| Conservazione | 90 giorni (repository attivi); 7 anni (repository di produzione) |
| Ridondanza geografica | Backup archiviati in una posizione geografica diversa dal repository principale |
| Cifratura | Cifrato a riposo utilizzando la cifratura approvata dall'organizzazione |
| Controllo degli accessi | Limitato agli amministratori di backup autorizzati; AMF richiesta |

I backup devono includere il codice sorgente (tutti i rami, i commit, la cronologia completa), i metadati del repository (autorizzazioni, impostazioni, configurazioni), la cronologia delle pull request e i dati di tracciamento delle issue se integrati.

**Testing del ripristino**:

| Classificazione del repository | Frequenza del testing | Recovery Time Objective (RTO) |
|---------------------------|-------------------|-------------------------------|
| Produzione | Trimestrale | 4 ore |
| Strumenti interni | Annuale | 24 ore |

Il testing del ripristino deve verificare: il ripristino del repository entro l'RTO, l'integrità dei dati (tutti i commit, i rami, la cronologia integri), il ripristino delle autorizzazioni e la funzionalità del repository ripristinato. Il testing deve utilizzare un campione rappresentativo di repository (minimo 3 repository di produzione per trimestre, a rotazione per coprire tutti annualmente). I risultati devono essere documentati.

---

## Gestione degli accessi di terze parti

Gli sviluppatori terzi, i collaboratori esterni e i team di sviluppo offshore devono soddisfare i seguenti requisiti prima di ricevere l'accesso al repository:

- Accordo di non divulgazione (NDA) firmato verificato da procurement o legale.
- Accesso limitato ai repository specifici richiesti per il lavoro contrattuale.
- Accesso a tempo limitato legato alla durata del contratto con scadenza automatica.
- Accesso approvato dal proprietario del repository (obbligatorio) e dal RSSI o delegato (per i repository di produzione).

**Monitoraggio delle terze parti**:

- L'accesso delle terze parti viene revisionato mensilmente per la necessità continua.
- Tutti i contributi al codice da parte di terze parti devono richiedere la revisione da parte di uno sviluppatore interno (minimo un revisore) e una revisione di sicurezza per le modifiche rilevanti per la sicurezza.
- L'accesso delle terze parti deve essere revocato immediatamente alla scadenza del contratto, alla risoluzione del contratto, a un incidente di sicurezza che coinvolge la terza parte, o su richiesta del proprietario del repository.

L'accesso delle terze parti deve essere documentato in un registro degli accessi delle terze parti con: società contraente, nomi individuali, repository a cui si è avuto accesso, date del contratto e responsabilità del project manager.

---

## Gestione delle eccezioni

Le eccezioni a questa politica devono essere richieste per iscritto e devono includere:

- Requisiti specifici che richiedono l'eccezione.
- Giustificazione aziendale.
- Controlli compensativi.
- Durata richiesta dell'eccezione (massimo 12 mesi).
- Valutazione e accettazione del rischio.

Le eccezioni devono essere approvate dal proprietario del repository e dal Responsabile della sicurezza delle informazioni (obbligatorio), più dal RSSI per le eccezioni ai repository di produzione. Tutte le eccezioni attive devono essere revisionate trimestralmente.

Dove tecnicamente non è fattibile soddisfare un requisito, devono essere implementati controlli compensativi per raggiungere una riduzione del rischio equivalente, documentati, verificati dal Responsabile della sicurezza delle informazioni e revisionati annualmente.

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Protezione del ramo** | Regole di configurazione che impediscono commit diretti a rami specificati, richiedendo pull request, revisioni e il superamento dei controlli di stato |
| **Code owner** | Individuo o team designato come responsabile della revisione delle modifiche a parti specifiche del codebase |
| **Force push** | Un'operazione Git che sovrascrive la cronologia del ramo remoto; limitata sui rami protetti |
| **AMF** | Autenticazione a più fattori (MFA) — richiede due o più fattori di verifica per ottenere l'accesso |
| **Hook pre-commit** | Uno script che viene eseguito prima della creazione di un commit, utilizzato per impedire che segreti o violazioni della politica entrino nel repository |
| **Pull request (merge request)** | Una richiesta di merge delle modifiche al codice da un ramo a un altro, consentendo la revisione prima dell'integrazione |
| **RBAC** | Controllo degli accessi basato sui ruoli — assegnazione delle autorizzazioni in base ai ruoli organizzativi definiti |
| **Repository** | Una posizione di archiviazione per il codice sorgente, gestita da un sistema di controllo versione (ad es. Git) |
| **Segreto** | Qualsiasi credenziale, chiave API, token, chiave privata o materiale di autenticazione che non deve essere archiviato nel codice sorgente |
| **Account di servizio** | Un account non umano utilizzato per automazione, CI/CD e integrazione sistema-sistema |
| **SSO** | Single sign-on — autenticazione che consente agli utenti di accedere a più sistemi con un unico set di credenziali |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; approvazione dell'accesso admin ai repository di produzione; approvazione delle eccezioni; supervisione degli incidenti di sicurezza che coinvolgono il codice sorgente; revisione annuale della politica; reportistica alla Direzione generale |
| **CTO / Responsabile dello sviluppo** | Selezione e configurazione della piattaforma di sviluppo; approvazione della classificazione dei repository; conformità del team di sviluppo; allocazione delle risorse per l'implementazione della politica |
| **Responsabile della sicurezza delle informazioni** | Manutenzione della politica; revisione delle eccezioni (repository non di produzione); monitoraggio della sicurezza e indagine sugli incidenti; coordinamento dell'audit; reportistica trimestrale della conformità al RSSI |
| **Proprietari dei repository** | Assegnazione della classificazione del repository; approvazione delle richieste di accesso; revisioni trimestrali degli accessi; configurazione della sicurezza del repository; segnalazione degli incidenti al team di sicurezza |
| **Team Lead dello sviluppo** | Revisione delle richieste di accesso per i membri del team; applicazione del processo di revisione del codice; formazione degli sviluppatori sulle pratiche di sicurezza del repository; applicazione della gestione dei segreti nel team |
| **Team di sicurezza** | Configurazione del monitoraggio e alerting della sicurezza; gestione degli strumenti di scansione dei segreti; audit e valutazioni di sicurezza; risposta agli incidenti per gli eventi di sicurezza del codice sorgente |
| **Operazioni IT** | Manutenzione e disponibilità della piattaforma repository; implementazione del backup e ripristino; automazione del provisioning e deprovisioning degli accessi; raccolta e conservazione dei log |
| **Sviluppatori e collaboratori esterni** | Conformità ai requisiti di controllo degli accessi e autenticazione; protezione delle credenziali; nessuna archiviazione di segreti nei repository; partecipazione alla revisione del codice; segnalazione degli incidenti; completamento della formazione di sicurezza richiesta |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza | Conservazione |
|---|----------|-------|-----------|-----------|
| 1 | **Inventario dei repository** con classificazione, proprietario e metadati della piattaforma | CTO / Responsabile dello sviluppo | Mantenuto continuamente; revisionato annualmente | Vita del repository + 3 anni |
| 2 | **Registri di richiesta e approvazione degli accessi** (richieste, giustificazioni, approvazioni) | Proprietari dei repository | Per richiesta | 3 anni |
| 3 | **Registri delle revisioni trimestrali degli accessi** (conferma utente per utente, azioni intraprese) | Proprietari dei repository | Trimestrale | 3 anni |
| 4 | **Inventario degli account di servizio** con proprietario, scopo e registri di revisione trimestrale | Operazioni IT / Responsabile dello sviluppo | Mantenuto continuamente; revisionato trimestralmente | Vita dell'account + 1 anno |
| 5 | **Esportazioni della configurazione della protezione dei rami** dalla piattaforma repository | Responsabile dello sviluppo / DevOps | Trimestrale | 2 anni |
| 6 | **Registri delle pull request e della revisione del codice** (commenti di revisione, approvazioni, cronologia dei merge) | Responsabile dello sviluppo | Per modifica al codice | 3 anni |
| 7 | **Configurazione della scansione dei segreti e log dei risultati** (impostazioni dello strumento, alert, registri di remediation) | Team di sicurezza / DevOps | Continuamente; risultati revisionati settimanalmente | 3 anni |
| 8 | **Rapporti di registrazione AMF** che mostrano la copertura tra gli utenti del repository | Operazioni IT / Team di sicurezza | Trimestrale | 1 anno |
| 9 | **Log di autenticazione e accesso** dalla piattaforma repository | Operazioni IT | Continuamente | Per tabella di conservazione (1–3 anni per tipo di evento) |
| 10 | **Registri di esecuzione del backup e test di ripristino** (log di backup, rapporti di test, misurazioni RTO) | Operazioni IT | Backup: giornaliero; Test di ripristino: trimestrale (produzione) / annuale (altri) | 3 anni |
| 11 | **Registro degli accessi di terze parti** (dettagli del contraente, registri NDA, date del contratto, scadenza degli accessi) | Proprietari dei repository / Procurement | Mantenuto continuamente; revisionato mensilmente | Durata del contratto + 3 anni |
| 12 | **Registro delle eccezioni** (richieste, approvazioni, controlli compensativi, revisioni trimestrali) | Responsabile della sicurezza delle informazioni | Mantenuto continuamente; revisionato trimestralmente | Durata dell'eccezione + 3 anni |
| 13 | **Registri della formazione di sicurezza degli sviluppatori** (gestione dei segreti, pratiche di sicurezza del repository) | RSSI / HR | Annualmente | Durata dell'impiego + 3 anni |
| 14 | **Registri di verifica del deprovisioning** (conferme di revoca attivate dalla cessazione) | Operazioni IT / HR | Per evento di cessazione | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui rapporti sugli accessi alla piattaforma repository, audit della configurazione della protezione dei rami, rapporti degli strumenti di scansione dei segreti, registri di completamento delle revisioni degli accessi, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|--------|--------|-----------------------|
| Repository con RBAC conforme e revisioni trimestrali completate | >= 90% | Trimestrale |
| Repository con protezione dei rami richiesta abilitata | >= 95% | Trimestrale |
| Repository con scansione dei segreti abilitata e segreti remediati entro SLA | >= 90% | Mensile |
| Account di terze parti con NDA valido e contratto corrente | 100% | Mensile |
| Registrazione AMF per gli utenti con accesso in scrittura o admin | 100% | Trimestrale |
| Accesso deprovisioned entro lo stesso giorno lavorativo dalla cessazione | 100% | Per evento |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|-----------|--------|-------------|
| Conformità degli accessi al repository | 35% | (Repository con RBAC conforme + revisioni trimestrali completate) / Totale repository x 100 |
| Conformità della protezione dei rami | 35% | (Repository con protezione dei rami richiesta abilitata) / Repository applicabili x 100 |
| Conformità della gestione dei segreti | 20% | (Repository con scansione abilitata + segreti remediati entro SLA) / Totale x 100 |
| Conformità degli accessi di terze parti | 10% | (Account di terze parti con NDA valido + contratto corrente) / Totale account di terze parti x 100 |

**Gestione della non conformità**: Al di sotto del 70% è richiesta un'escalation immediata al RSSI e un piano di remediation. Tra il 70–89% è richiesta la supervisione del Responsabile della sicurezza delle informazioni con revisioni mensili. Al 90% e oltre si segue il monitoraggio trimestrale standard.

**Responsabilità della remediation per componente del punteggio**:

| Componente | Sotto l'obiettivo | Responsabile della remediation | Escalation |
|-----------|-------------|-------------------|------------|
| Conformità degli accessi al repository | <90% | Proprietari dei repository + Responsabile dello sviluppo | RSSI a 30 giorni di ritardo |
| Conformità della protezione dei rami | <95% | DevOps / Responsabile dello sviluppo | RSSI a 15 giorni di ritardo |
| Conformità della gestione dei segreti | <90% | Team di sicurezza + DevOps | RSSI immediatamente se segreti attivi esposti |
| Conformità degli accessi di terze parti | <100% | Procurement + Proprietari dei repository | RSSI a 5 giorni di ritardo (rischio legale/contrattuale) |

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni devono essere segnalate al Team di revisione della direzione.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e segnalate al RSSI.

## Fasi di implementazione SOC 2

Per le organizzazioni che perseguono la certificazione SOC 2 Tipo II, si raccomanda la seguente implementazione graduale:

| Fase | Focus | Azioni chiave |
|-------|-------|-------------|
| 1 | **Inventario degli asset** | Completare l'inventario dei repository con classificazione e proprietario |
| 2 | **Implementazione RBAC** | Controllo degli accessi basato sui ruoli con privilegio minimo |
| 3 | **Applicazione AMF** | AMF per tutti gli accessi in scrittura/admin |
| 4 | **Protezione dei rami** | Rami protetti con revisioni obbligatorie |
| 5 | **Scansione dei segreti** | Scansione automatizzata pre-commit e lato server |
| 6 | **Registrazione e monitoraggio** | Registrazione degli audit completa inoltrata al SIEM |
| 7 | **Revisioni degli accessi** | Revisioni trimestrali con evidenze documentate |
| 8 | **Backup e ripristino** | Strategia di backup con ripristino testato |
| 9 | **Controlli delle terze parti** | NDA, accesso a tempo limitato, revisione avanzata |
| 10 | **Miglioramento continuo** | Metriche, punteggio di conformità, reportistica trimestrale |

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti nelle capacità della piattaforma repository, le minacce emergenti alla sicurezza del codice sorgente (attacchi alla supply chain, dependency confusion, compromissione della pipeline CI/CD), le modifiche normative, i risultati degli audit e le lezioni apprese dagli incidenti di sicurezza.

---

# Aree della norma ISO 27001 affrontate

Politica di accesso al codice sorgente — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.4 Accesso al codice sorgente** |
| | 8.5 Autenticazione sicura |
| | 8.25 Ciclo di vita dello sviluppo sicuro |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati; il controllo degli accessi al codice sorgente come misura tecnica |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (controllo degli accessi come misura tecnica appropriata) |
| ISO/IEC 27001:2022 | Controllo Annex A 8.4 — Accesso al codice sorgente |
| ISO/IEC 27002:2022 | Sezione 8.4 — Linee guida di implementazione per il controllo degli accessi al codice sorgente |
| NIST SP 800-218 (SSDF) | PS.1 — Proteggere tutte le forme di codice da accessi e manomissioni non autorizzati |
| NIST SP 800-53 Rev 5 | AC-3 (Applicazione dell'accesso), AC-6 (Privilegio minimo), CM-5 (Restrizioni di accesso per le modifiche), AU-2 (Eventi di audit) |
| CIS Controls v8 | 6.1–6.2 (Concessione/Revoca dell'accesso), 6.7 (Controllo centralizzato degli accessi), 6.8 (Accesso basato sui ruoli), 16.1–16.4 (Sicurezza del software applicativo) |
| FINMA (se applicabile) | Circolare 2023/1 Margine 50–62 — La sicurezza delle informazioni include la protezione del codice sorgente |
| DORA (se applicabile) | Art. 9 — La gestione degli asset ICT include il codice sorgente; Art. 15 — La segnalazione degli incidenti include la compromissione del codice sorgente |
| NIS2 (se applicabile) | Art. 21(2) — La gestione degli asset include il codice sorgente; Art. 23 — Segnalazione degli incidenti per gli incidenti di sicurezza del codice sorgente |

---

<!-- QA_VERIFIED: 2026-04-03 -->
