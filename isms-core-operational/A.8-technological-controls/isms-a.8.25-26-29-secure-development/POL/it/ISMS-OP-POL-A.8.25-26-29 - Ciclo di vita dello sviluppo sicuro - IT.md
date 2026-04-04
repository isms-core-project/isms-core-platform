<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.25-26-29-IT:operational:OP-POL:a.8.25-26-29 -->
**ISMS-OP-POL-A.8.25-26-29 — Ciclo di vita dello sviluppo sicuro**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ciclo di vita dello sviluppo sicuro |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.25-26-29 |
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

- ISO/IEC 27001:2022 Controllo A.8.25 — Ciclo di vita dello sviluppo sicuro
- ISO/IEC 27001:2022 Controllo A.8.26 — Requisiti di sicurezza delle applicazioni
- ISO/IEC 27001:2022 Controllo A.8.29 — Test di sicurezza nello sviluppo e nell'accettazione
- OWASP Application Security Verification Standard (ASVS) 4.0
- OWASP Top 10:2025
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1

**Controlli Allegato A correlati**:

| Controllo | Relazione con lo sviluppo sicuro |
|-----------|----------------------------------|
| A.5.8 Sicurezza delle informazioni nella gestione dei progetti | Requisiti di sicurezza integrati nel ciclo di vita del progetto |
| A.5.15–16–18 Gestione dell'identità e degli accessi | Controllo degli accessi ai repository, agli ambienti e agli strumenti di distribuzione |
| A.8.4 Accesso al codice sorgente | Restrizione e protezione dell'accesso al codice sorgente |
| A.8.8 Gestione delle vulnerabilità tecniche | Rimedio delle vulnerabilità per le applicazioni distribuite |
| A.8.28 Codifica sicura | Standard e pratiche di codifica sicura |
| A.8.31 Separazione degli ambienti di sviluppo, test e produzione | Requisiti di segregazione degli ambienti |
| A.8.32 Gestione delle modifiche | Controllo delle modifiche per la promozione del codice e la distribuzione |
| A.8.33 Informazioni di test | Protezione dei dati di test |

**Politiche interne correlate**:

- Politica di controllo degli accessi
- Politica di gestione delle vulnerabilità
- Politica di gestione delle modifiche
- Politica di classificazione e gestione delle informazioni
- Politica di sicurezza degli endpoint

---

# Politica sul ciclo di vita dello sviluppo sicuro

## Scopo

Lo scopo di questa politica è garantire che la sicurezza delle informazioni sia progettata e implementata nel ciclo di vita dello sviluppo del software e dei sistemi, che i requisiti di sicurezza siano identificati e specificati durante lo sviluppo o l'acquisizione di applicazioni, e che i test di sicurezza siano definiti ed eseguiti prima della distribuzione in produzione.

Questa politica supporta la nLPD svizzera (revDSG) implementando misure tecniche e organizzative adeguate al rischio per proteggere i dati personali, in conformità con l'Art. 7 (protezione dei dati per impostazione predefinita e fin dalla progettazione) e l'Art. 8 (misure tecniche e organizzative di sicurezza). Laddove l'organizzazione tratta dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR (Art. 25 — protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 32 — sicurezza del trattamento).

## Ambito

Sviluppo di sistemi per soluzioni software interne su misura dell'organizzazione, incluse applicazioni web, API, applicazioni mobili e infrastruttura come codice (IaC).

Tutte le attività di sviluppo interno e in outsourcing ritenute nell'ambito dalla dichiarazione di ambito ISO 27001.

Tutti i dipendenti e gli utenti terzi coinvolti nello sviluppo, nel test e nella distribuzione del software.

## Principio

I principi e gli standard di ingegneria del software e dei sistemi sicuri sono implementati e testati durante tutto il ciclo di vita dello sviluppo del software.

La sicurezza delle informazioni e la privacy sono per impostazione predefinita e fin dalla progettazione, in conformità con i gruppi di pratiche NIST SP 800-218 (SSDF): Preparare l'organizzazione (PO), Proteggere il software (PS), Produrre software sicuro (PW) e Rispondere alle vulnerabilità (RV).

I controlli di sicurezza sono applicati in modo proporzionale al rischio applicativo, con applicazioni ad alto rischio soggette a requisiti più rigorosi.

---

## Toolchain di sicurezza per lo sviluppo

L'organizzazione deve mantenere una toolchain di sicurezza approvata integrata nel ciclo di vita dello sviluppo.

**Toolchain di sicurezza approvata**:

| Categoria | Scopo | Responsabile | Punto di integrazione |
|-----------|-------|--------------|----------------------|
| **Repository del codice sorgente** | Controllo di versione, protezione dei branch, controllo degli accessi | DevOps / Team piattaforma | Fase di sviluppo |
| **SAST** (Static Application Security Testing) | Rilevamento delle vulnerabilità nel codice sorgente (ad esempio, SonarQube, Semgrep, Checkmarx o equivalente) | DevOps / Responsabile sviluppo | Pipeline CI/CD — fase di build |
| **SCA** (Software Composition Analysis) | Rilevamento delle vulnerabilità nelle dipendenze open source (ad esempio, Snyk, OWASP Dependency-Check o equivalente) | DevOps / Responsabile sviluppo | Pipeline CI/CD — fase di build |
| **DAST** (Dynamic Application Security Testing) | Rilevamento delle vulnerabilità in fase di esecuzione (ad esempio, OWASP ZAP, Burp Suite o equivalente) | QA / Team sicurezza | Fase pre-distribuzione |
| **Scansione dei segreti** | Rilevamento di credenziali, chiavi API, token nel codice (ad esempio, GitLeaks, TruffleHog o equivalente) | DevOps / Team piattaforma | Hook pre-commit + pipeline CI/CD |
| **Database delle dipendenze** | Intelligence sulle vulnerabilità per componenti di terze parti (ad esempio, NVD, OSV, GitHub Advisory Database) | Responsabile sviluppo | Monitoraggio continuo |
| **Generatore SBOM** | Generazione della Software Bill of Materials (ad esempio, Syft, CycloneDX CLI o equivalente) | DevOps / Team piattaforma | Pipeline CI/CD — fase di build |
| **Piattaforma di code review** | Revisione tra pari, flusso di approvazione, traccia di audit (ad esempio, GitHub, GitLab, Bitbucket o equivalente) | Responsabile sviluppo | Fase pre-merge |
| **Test di penetrazione** | Valutazione manuale della sicurezza da parte di specialisti esterni qualificati | RSSI | Pre-rilascio (alto rischio) / periodico |

La toolchain deve essere revisionata annualmente dal Responsabile sviluppo e dal RSSI. Le modifiche agli strumenti devono seguire il processo di gestione delle modifiche. Tutti gli strumenti devono essere mantenuti alle versioni correnti supportate.

---

## Segregazione degli ambienti

Gli ambienti di sviluppo, test e produzione devono essere separati e non devono condividere componenti comuni, database o storage.

Gli ambienti di sviluppo, test e produzione devono trovarsi su reti o segmenti di rete separati.

Deve esserci una segregazione dei compiti amministrativi tra gli ambienti di sviluppo/test e di produzione. Il personale con accesso in scrittura ai repository di sviluppo non deve avere accesso amministrativo diretto ai sistemi di produzione senza un'autorizzazione separata.

I dati non devono fluire dalla produzione agli ambienti di sviluppo o test senza approvazione esplicita e un'appropriata sanificazione (si veda la sezione Protezione dei dati di test).

La configurazione della segregazione degli ambienti deve essere documentata e la conformità deve essere verificata almeno annualmente.

---

## Classificazione del rischio applicativo

Tutte le applicazioni devono essere classificate per livello di rischio per determinare i requisiti di sicurezza appropriati.

**Criteri di classificazione del rischio**:

| Livello di rischio | Criteri |
|--------------------|---------|
| **Alto rischio** | Soddisfa UNO QUALSIASI: tratta dati Riservato o Ristretto; gestisce dati personali soggetti a nLPD/GDPR; accessibile da Internet o da parti esterne; funzione aziendale critica o elaborazione di transazioni finanziarie; informazioni sulle carte di pagamento (se esiste un ambito PCI) |
| **Rischio medio** | Soddisfa UNO QUALSIASI: tratta dati ad uso interno; esposizione limitata di dati personali (solo nomi, indirizzi e-mail); accesso solo interno; funzione aziendale importante ma non critica |
| **Basso rischio** | Soddisfa TUTTI: tratta solo dati Pubblico; nessun dato personale, nessun dato aziendale sensibile; funzione aziendale non critica |

Le classificazioni del rischio applicativo devono essere revisionate annualmente dal Responsabile sviluppo e dal RSSI.

**Elementi scatenanti per la riclassificazione** (in aggiunta alla revisione annuale):

| Evento scatenante | Azione |
|-------------------|--------|
| Nuovo tipo di dati trattati (ad esempio, dati personali, finanziari, sanitari) | Riclassificare entro 14 giorni |
| Cambio di esposizione di rete (interno → accessibile da Internet) | Riclassificare prima della distribuzione |
| Modifica significativa dell'architettura (nuova API, nuova integrazione) | Riclassificare nella fase di progettazione |
| Modifica normativa che riguarda l'applicazione | Riclassificare entro 30 giorni |
| Incidente di sicurezza che coinvolge l'applicazione | Riclassificare entro 14 giorni dalla chiusura dell'incidente |
| Acquisizione o fusione che riguarda l'ambito dell'applicazione | Riclassificare entro 60 giorni |

**Processo di riclassificazione**: (1) Il Proprietario dell'applicazione invia una richiesta di modifica con giustificazione → (2) Il Responsabile sviluppo valuta in base ai criteri di classificazione → (3) Il RSSI approva se la classificazione aumenta → (4) I requisiti di sicurezza aggiornati vengono applicati entro 60 giorni se la classificazione aumenta → (5) La classificazione aggiornata viene registrata nel registro.

La classificazione deve essere registrata nel registro di classificazione del rischio applicativo.

---

## Requisiti di sicurezza

I requisiti di sicurezza devono essere specificati per tutte le applicazioni in base alla classificazione del rischio.

**Requisiti obbligatori per livello di rischio**:

| Requisito | Alto rischio | Rischio medio | Basso rischio |
|-----------|--------------|---------------|---------------|
| Specifica dei requisiti di sicurezza | Obbligatorio | Obbligatorio | Lista di controllo base |
| Modello delle minacce (ad esempio, STRIDE, PASTA o Alberi di attacco) | Obbligatorio | Raccomandato | Facoltativo |
| Revisione dell'architettura di sicurezza | Obbligatorio | Raccomandato | Facoltativo |
| Tracciabilità dei requisiti | Obbligatorio | Raccomandato | Facoltativo |

**Processo di modellazione delle minacce**:

Dove è richiesta la modellazione delle minacce (obbligatoria per l'alto rischio, raccomandata per il rischio medio), deve essere seguito il seguente processo:

| Fase | Attività | Output |
|------|----------|--------|
| 1. **Preparazione** | Assemblare il team (sviluppatore, architetto, Security Champion/RSSI); raccogliere documentazione del sistema, diagrammi del flusso di dati, diagrammi dell'architettura | Definizione dell'ambito e pacchetto di materiali |
| 2. **Identificazione delle minacce** | Applicare la metodologia STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) a ciascun componente e flusso di dati | Catalogo delle minacce |
| 3. **Valutazione del rischio** | Valutare la probabilità e l'impatto di ciascuna minaccia identificata utilizzando i criteri di rischio dell'organizzazione | Elenco delle minacce prioritizzato |
| 4. **Pianificazione delle mitigazioni** | Definire controlli di sicurezza e requisiti per affrontare ciascuna minaccia; mappare ai task di implementazione | Piano di mitigazione con responsabili e scadenze |
| 5. **Documentazione** | Registrare il modello delle minacce nel formato approvato; collegare alla specifica dei requisiti di sicurezza | Documento del modello delle minacce completato |

I modelli delle minacce devono essere revisionati e aggiornati: ad ogni rilascio principale; quando l'architettura dell'applicazione cambia significativamente; quando vengono identificate nuove informazioni sulle minacce rilevanti per l'applicazione; e almeno annualmente per le applicazioni ad alto rischio.

**I requisiti di sicurezza devono affrontare almeno le seguenti aree**:

- **Autenticazione e autorizzazione** — verifica dell'identità, accesso basato sui ruoli, gestione delle sessioni.
- **Validazione degli input e codifica degli output** — difesa contro gli attacchi di iniezione (OWASP Top 10 A05:2025).
- **Crittografia** — cifratura dei dati in transito (TLS 1.2 minimo) e a riposo secondo la Politica sull'uso della crittografia.
- **Gestione delle sessioni** — token di sessione sicuri, timeout, invalidazione al logout.
- **Gestione degli errori e registrazione** — nessun dato sensibile nei messaggi di errore; eventi di sicurezza registrati secondo la Politica di registrazione degli eventi.
- **Sicurezza delle API** — autenticazione, limitazione della frequenza (rate limiting), validazione degli input per tutti gli endpoint API.
- **Protezione dei dati** — gestione dei dati personali secondo nLPD Art. 7 (privacy per impostazione predefinita e fin dalla progettazione); minimizzazione dei dati; cancellazione sicura.

Per le applicazioni che forniscono servizi transazionali tra l'organizzazione e parti esterne, i requisiti aggiuntivi devono affrontare i livelli di fiducia nell'identità, l'integrità delle informazioni scambiate, il non ripudio e la riservatezza delle transazioni.

**Modello di specifica dei requisiti di sicurezza**:

Le specifiche dei requisiti di sicurezza devono seguire un modello standardizzato che copra le seguenti sezioni:

| # | Sezione | Descrizione |
|---|---------|-------------|
| 1 | Panoramica dell'applicazione | Nome, scopo, classificazione del rischio, classificazione dei dati |
| 2 | Diagramma del flusso di dati | Diagramma del contesto di sistema che mostra i flussi di dati, i confini di fiducia, le interfacce esterne |
| 3 | Requisiti di autenticazione | Metodi di autenticazione, requisiti AMF, gestione delle sessioni |
| 4 | Requisiti di autorizzazione | Modello di controllo degli accessi (RBAC/ABAC), livelli di privilegio, separazione dei compiti |
| 5 | Validazione degli input | Regole di validazione per tipo di input, requisiti di codifica, restrizioni per l'upload di file |
| 6 | Requisiti crittografici | Standard di cifratura (secondo la Politica sull'uso della crittografia), gestione delle chiavi |
| 7 | Sicurezza delle API | Autenticazione, rate limiting, validazione degli input, versioning, gestione degli errori |
| 8 | Protezione dei dati | Gestione dei dati personali, minimizzazione dei dati, conservazione, cancellazione, conformità nLPD Art. 7 |
| 9 | Registrazione e monitoraggio | Eventi di sicurezza da registrare, formato dei log, conservazione, soglie di allerta |
| 10 | Gestione degli errori | Restrizioni sul contenuto dei messaggi di errore, comportamento di fallback, degradazione controllata |
| 11 | Integrazione di terze parti | Valutazione della fiducia, condivisione dei dati, sicurezza delle API, requisiti SLA |
| 12 | Requisiti di conformità | Requisiti normativi (nLPD, GDPR ove applicabile), standard di settore |
| 13 | Sintesi del modello delle minacce | Minacce chiave identificate, mitigazioni richieste (per applicazioni ad alto rischio) |
| 14 | Piano di test di sicurezza | Tipi di test richiesti, ambito, pianificazione, criteri di accettazione |

I requisiti di sicurezza devono essere approvati dal RSSI (alto rischio) o dal Responsabile sviluppo (rischio medio/basso) prima dell'inizio dello sviluppo.

---

## Linee guida per la codifica sicura

Il software deve essere progettato e sviluppato sulla base di linee guida per la codifica sicura riconosciute dal settore, tra cui:

- **OWASP** — OWASP Top 10:2025, OWASP Application Security Verification Standard (ASVS) e OWASP Secure Coding Practices.
- **NIST SP 800-218 (SSDF)** — Secure Software Development Framework per la mitigazione del rischio di vulnerabilità software.
- **CWE/SANS Top 25** — Le vulnerabilità software più pericolose, che affrontano categorie quali iniezione, corruzione della memoria e fallimenti dell'autenticazione.

Gli standard di codifica sicura specifici per linguaggio devono essere documentati e mantenuti per ciascun linguaggio di programmazione in uso attivo. Questi devono coprire, come minimo:

- Funzioni vietate e schemi non sicuri.
- Tecniche richieste di validazione degli input e codifica degli output.
- Librerie crittografiche approvate e schemi d'uso.
- Pratiche di gestione degli errori e di registrazione sicure.
- Gestione delle dipendenze e blocco delle versioni (version pinning).

**Esempio — Standard di codifica sicura Python** (illustrativo; ogni linguaggio deve avere documentazione equivalente):

| Categoria | Requisito |
|-----------|-----------|
| **Funzioni vietate** | `eval()`, `exec()`, `pickle.loads()` su input non attendibile, `os.system()` (usare `subprocess.run()` con shell=False), `yaml.load()` senza SafeLoader |
| **Pratiche obbligatorie** | Query parametrizzate (nessuna concatenazione di stringhe per SQL), modulo `secrets` per la generazione casuale (non `random`), type hint per funzioni critiche per la sicurezza, validazione degli input usando allowlist |
| **Librerie crittografiche approvate** | Libreria `cryptography` (preferita), `hashlib` (solo hashing); vietate: `pycrypto` (non manutenuta), implementazioni crittografiche personalizzate |
| **Gestione degli errori** | Nessun dato sensibile nei messaggi di eccezione; usare logging strutturato; intercettare eccezioni specifiche (non `except:` generico) |
| **Dipendenze** | Blocco delle versioni in `requirements.txt` o `pyproject.toml`; revisione dei changelog prima degli aggiornamenti di versione principale; nessuna dipendenza con CVE critiche note |

Gli standard specifici per linguaggio devono essere archiviati nel repository del codice (ad esempio, `docs/secure-coding/` o equivalente), revisionati annualmente e aggiornati quando emergono nuove vulnerabilità o schemi.

Tutti gli sviluppatori devono completare la formazione sulla codifica sicura prima di ricevere l'accesso per scrivere codice di produzione (si veda la sezione Formazione sulla sicurezza per gli sviluppatori).

---

## Repository del codice e controllo di versione

Il codice di sviluppo deve essere archiviato in un repository del codice sicuro che applica e soddisfa i requisiti della Politica di controllo degli accessi e della separazione dei compiti.

L'accesso al repository deve seguire il principio del privilegio minimo:

- L'accesso deve essere concesso in base all'assegnazione al progetto e al ruolo.
- L'accesso al repository deve essere revisionato almeno annualmente, in linea con le revisioni della gestione dell'identità e degli accessi.
- L'accesso degli ex membri del team deve essere revocato entro lo stesso giorno lavorativo dalla partenza.

I repository del codice devono applicare:

- **Controllo di versione** con appropriato archivio delle versioni e strategia di ramificazione.
- **Protezione dei branch** sui branch principali/di produzione — i commit diretti sono vietati; le modifiche richiedono l'approvazione di una pull/merge request.
- **Firma dei commit** raccomandata per le applicazioni ad alto rischio.
- **Scansione dei segreti** per prevenire commit accidentali di credenziali, chiavi API o token.

**Scansione dei segreti e gestione dei segreti**:

La scansione dei segreti deve rilevare, come minimo: chiavi API, token di accesso, chiavi private, stringhe di connessione ai database, credenziali di provider cloud e URL di webhook.

**Processo di rimedio in caso di segreto rilevato**:

| Fase | Azione | Tempistica |
|------|--------|------------|
| 1 | **Bloccare il commit** (hook pre-commit) o segnalare nella pipeline CI/CD | Immediato |
| 2 | **Revocare e ruotare** la credenziale esposta | Entro 4 ore per i segreti di produzione; entro 24 ore per quelli non di produzione |
| 3 | **Rimuovere dalla cronologia del repository** (se già committato) usando strumenti approvati (ad esempio, git filter-branch, BFG Repo-Cleaner) | Entro 24 ore |
| 4 | **Investigare l'esposizione** — determinare se il segreto è stato acceduto da parti non autorizzate | Entro 48 ore |
| 5 | **Documentare l'incidente** — registrare nel log degli incidenti; escalare al RSSI se il segreto di produzione è stato esposto a parti esterne | Secondo la politica di gestione degli incidenti |

**Gestione approvata dei segreti**:

| Ambiente | Metodo approvato |
|----------|-----------------|
| Sviluppo | Variabili di ambiente, file `.env` (esclusi dal controllo di versione via `.gitignore`) |
| Test | Secrets manager o variabili di ambiente cifrate |
| Produzione | Secrets manager dedicato (ad esempio, HashiCorp Vault, AWS Secrets Manager, Azure Key Vault o equivalente) |
| Pipeline CI/CD | Archivio segreti della pipeline (ad esempio, GitHub Secrets, GitLab CI/CD Variables o equivalente); nessun segreto hardcoded nelle definizioni della pipeline |

I segreti hardcoded nel codice sorgente sono vietati. I risultati della scansione dei segreti devono essere revisionati settimanalmente dal Responsabile sviluppo.

---

## Code review

Tutto il codice deve essere revisionato prima del rilascio da personale qualificato diverso dall'autore o dallo sviluppatore del codice.

Il codice deve essere revisionato in base alle linee guida per la codifica sicura documentate dall'organizzazione.

Le code review devono impiegare sia tecniche manuali che automatizzate:

- **Revisione tra pari manuale** — obbligatoria per tutte le modifiche al codice prima del merge nei branch protetti.
- **Revisione focalizzata sulla sicurezza** — obbligatoria per le applicazioni ad alto rischio, condotta da un Security Champion o da un revisore con formazione in sicurezza.
- **Revisione automatizzata** — strumenti SAST (Static Application Security Testing) integrati nella pipeline CI/CD (ad esempio, SonarQube, Semgrep, Checkmarx o equivalente).

**Flusso di lavoro della code review**:

| Fase | Attività | Responsabile |
|------|----------|--------------|
| 1. **Invio** | Lo sviluppatore crea una pull/merge request con descrizione, requisiti collegati e checklist di auto-revisione | Sviluppatore |
| 2. **Controlli automatizzati** | La pipeline CI/CD esegue SAST, SCA, scansione dei segreti, linting, test unitari | Automatizzato (DevOps) |
| 3. **Revisione tra pari manuale** | Il revisore controlla la logica, la leggibilità, l'aderenza agli standard di codifica, la copertura dei test | Revisore tra pari |
| 4. **Revisione della sicurezza** | Revisione focalizzata sulla sicurezza in base alla checklist di codifica sicura (alto rischio: obbligatoria; rischio medio: raccomandata) | Security Champion o revisore con formazione in sicurezza |
| 5. **Approvazione e merge** | Il/i revisore/i approva/no; merge nel branch protetto | Revisore/i / Responsabile sviluppo |

**Checklist per la code review di sicurezza** (elementi minimi per la revisione focalizzata sulla sicurezza):

1. Validazione degli input applicata a tutti gli input esterni (input utente, parametri API, upload di file)
2. Codifica degli output applicata dove i dati vengono visualizzati (HTML, JSON, SQL, LDAP)
3. Controlli di autenticazione e autorizzazione presenti e corretti
4. Nessun segreto, credenziale o chiave API hardcoded
5. Le funzioni crittografiche utilizzano librerie e algoritmi approvati
6. La gestione degli errori non espone informazioni sensibili
7. La registrazione include eventi rilevanti per la sicurezza senza registrare dati sensibili
8. Le query SQL utilizzano istruzioni parametrizzate (nessuna concatenazione di stringhe)
9. Le operazioni sui file validano i percorsi (nessun path traversal)
10. Le dipendenze di terze parti sono bloccate alle versioni revisionate

**Requisiti di approvazione per livello di rischio**:

| Livello di rischio | Approvatori minimi | Revisione della sicurezza richiesta |
|--------------------|--------------------|-------------------------------------|
| Alto rischio | 2 (incluso Security Champion o revisore designato dal RSSI) | Obbligatoria |
| Rischio medio | 1 | Raccomandata |
| Basso rischio | 1 | Facoltativa |

I risultati della code review devono essere documentati e tracciati fino alla risoluzione prima che il codice sia approvato per la promozione.

Il codice deve essere approvato prima di essere promosso negli ambienti di test o di produzione.

---

## Gate di sicurezza della pipeline CI/CD

I controlli di sicurezza devono essere automatizzati nella pipeline CI/CD a gate definiti.

**Gate di sicurezza della pipeline**:

| Gate | Fase | Controlli | Azione in caso di fallimento |
|------|------|-----------|------------------------------|
| **Gate 1: Pre-commit** | Workstation dello sviluppatore | Scansione dei segreti (hook pre-commit) | Bloccare il commit; lo sviluppatore deve rimuovere il segreto |
| **Gate 2: Build** | Pipeline CI — fase di build | Scansione SAST, scansione delle dipendenze SCA, controllo della conformità delle licenze, test unitari | Bloccare il merge; lo sviluppatore deve rimediare |
| **Gate 3: Pre-distribuzione** | Pipeline CI — pre-distribuzione | Scansione DAST (alto/medio rischio), test di integrazione, test di regressione della sicurezza | Bloccare la distribuzione; rimediare o escalare |
| **Gate 4: Distribuzione in produzione** | Pipeline di distribuzione | Verifica degli approvatori richiesti, verifica del ticket di modifica, validazione dell'ambiente | Bloccare la distribuzione fino all'ottenimento delle approvazioni |

**Soglie di fallimento** (blocco automatico del gate):

| Gravità del risultato | SAST/SCA Gate 2 | DAST Gate 3 |
|-----------------------|-----------------|-------------|
| Critica | Bloccare | Bloccare |
| Alta | Bloccare | Bloccare |
| Media | Avvisare (tracciare come debito tecnico) | Avvisare (tracciare come debito tecnico) |
| Bassa | Solo registrare | Solo registrare |

**Regole di override**: Gli override dei gate della pipeline richiedono l'approvazione del RSSI (documentata nel ticket di modifica con accettazione del rischio e controlli compensativi). Le distribuzioni di emergenza possono bypassare il DAST del Gate 3 con l'approvazione del RSSI e una scansione retrospettiva obbligatoria entro 72 ore.

I risultati dei gate di sicurezza della pipeline devono essere comunicati settimanalmente al Responsabile sviluppo e mensilmente al RSSI.

---

## Requisiti di test di sicurezza

I processi di test di sicurezza devono essere definiti e implementati nel ciclo di vita dello sviluppo. I test devono validare che i requisiti di sicurezza siano stati soddisfatti prima della distribuzione in produzione.

**Test richiesti per livello di rischio**:

| Tipo di test | Alto rischio | Rischio medio | Basso rischio |
|--------------|--------------|---------------|---------------|
| **SAST** (Static Application Security Testing) | Per commit o giornaliero | Per commit o giornaliero | Settimanale |
| **SCA** (Software Composition Analysis / scansione delle dipendenze) | Giornaliero o continuo | Giornaliero o continuo | Settimanale |
| **DAST** (Dynamic Application Security Testing) | Per distribuzione o settimanale | Mensile | Facoltativo |
| **Test di penetrazione** | Annualmente + prima del rilascio iniziale + dopo modifiche significative | Ogni 2 anni | Facoltativo |

**Requisiti di base per i test**:

- Tutti i test di sicurezza delle applicazioni devono, come minimo, testare le categorie **OWASP Top 10:2025**: Broken Access Control, Security Misconfiguration, Software Supply Chain Failures, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Software or Data Integrity Failures, Security Logging and Alerting Failures e Mishandling of Exceptional Conditions.
- Tutti i test pre-produzione devono avvenire in un ambiente di test che rispecchi l'ambiente di produzione nel modo più fedele possibile.

**Requisiti di similarità dell'ambiente di test**:

| Componente | Requisito di parità con la produzione |
|------------|---------------------------------------|
| Sistema operativo | Stesso sistema operativo e versione |
| Versioni del runtime / framework | Stesse versioni principali e secondarie |
| Motore del database | Stesso motore e versione principale |
| Architettura di rete | Stesso modello di segmentazione e regole del firewall (gli intervalli IP possono differire) |
| Configurazione TLS/SSL | Stessi cipher suite e versioni del protocollo |
| Autenticazione | Stesso meccanismo di autenticazione e configurazione AMF |
| Bilanciatore di carico / reverse proxy | Stesso tipo e configurazione |
| Containerizzazione / orchestrazione | Stessa piattaforma e versione (se applicabile) |

**Differenze accettabili**: Indirizzi IP, nomi host, scala (meno istanze consentite in test), soglie del volume di monitoraggio e dati sintetici/anonimizzati invece dei dati di produzione.

**Verifica dell'ambiente**: La parità dell'ambiente deve essere verificata prima dei principali test di sicurezza (test di penetrazione, DAST). La verifica deve essere documentata e approvata dal Team DevOps / piattaforma.

**Sicurezza dell'ambiente di test**: Gli ambienti di test devono essere soggetti agli stessi controlli di accesso degli ambienti di produzione. Gli ambienti di test non devono essere accessibili da Internet a meno che non sia necessario per i test DAST (con regole del firewall a tempo limitato).
- Tutti i test di penetrazione devono essere condotti da una società specializzata esterna.
- Tutte le applicazioni web pubblicamente accessibili devono essere testate utilizzando strumenti di sicurezza manuali o automatizzati almeno annualmente o dopo una modifica significativa.

**Standard e ambito dei test di penetrazione**:

| Tipo di applicazione | Approccio di test | Frequenza |
|----------------------|-------------------|-----------|
| Applicazione web accessibile da Internet (alto rischio) | Valutazione completa secondo la OWASP Testing Guide + test della logica applicativa | Annualmente + prima del rilascio iniziale + dopo modifiche significative |
| Applicazione web accessibile da Internet (rischio medio) | Valutazione focalizzata su OWASP Top 10 | Ogni 2 anni |
| Applicazione interna (alto rischio) | Test autenticato con revisione della logica applicativa | Annualmente |
| Servizio solo API (alto rischio) | Test di sicurezza delle API (OWASP API Security Top 10) | Annualmente |
| Applicazione mobile | Test specifici per mobile (OWASP MASTG) | Annualmente per alto rischio |

**Nell'ambito** (minimo): Autenticazione e gestione delle sessioni, autorizzazione e controllo degli accessi, validazione degli input (iniezione, XSS, SSRF), logica applicativa, sicurezza delle API, implementazione crittografica, configurazione e distribuzione, gestione degli errori e divulgazione di informazioni.

**Fuori ambito** (a meno che non sia esplicitamente incluso): Test di denial-of-service, social engineering, test di sicurezza fisica, componenti ospitati da terze parti (testati separatamente dal fornitore).

**Standard di test**: I test di penetrazione devono seguire la OWASP Testing Guide v4.2 e/o il PTES (Penetration Testing Execution Standard). I report dei test devono includere: sintesi esecutiva, metodologia, risultati con punteggio CVSS, prove (screenshot, richiesta/risposta), raccomandazioni per la remediation e verifica del re-test.

**Criteri di selezione del fornitore**: I fornitori di test di penetrazione devono possedere certificazioni pertinenti (ad esempio, CREST, OSCP, CEH) e fornire prove di assicurazione per la responsabilità professionale. Gli incarichi con i fornitori devono includere regole di ingaggio firmate e accordo di riservatezza (NDA).

**Azioni post-test**: (1) Rimediare ai risultati secondo gli SLA di rimedio delle vulnerabilità → (2) Il fornitore ri-testa i risultati critici/alti dopo la remediation → (3) Il report finale con i risultati del re-test viene presentato al RSSI e al Team di revisione della direzione → (4) Le lezioni apprese vengono incorporate negli standard di codifica sicura → (5) Il report viene conservato per 5 anni.

**Software Bill of Materials (SBOM)**:

- Le applicazioni ad alto rischio devono mantenere un SBOM in formato CycloneDX o SPDX.
- Gli SBOM devono essere generati automaticamente durante il processo di build (ad ogni build per alto rischio; settimanalmente per rischio medio).
- Gli SBOM devono essere aggiornati in caso di modifiche alle dipendenze e revisionati trimestralmente per le vulnerabilità note.

**Requisiti di contenuto degli SBOM**: Ogni SBOM deve includere: nome e versione del componente, fornitore/autore, tipo di licenza, relazioni di dipendenza (dirette e transitive) e stato delle vulnerabilità note (riferimenti CVE ove applicabili).

**Processo di revisione trimestrale degli SBOM**: (1) Generare l'SBOM corrente → (2) Incrociare tutti i componenti con i database delle vulnerabilità (NVD, OSV, GitHub Advisory Database) → (3) Identificare i componenti con vulnerabilità note, stato di fine vita o modifiche alle licenze → (4) Creare un piano di remediation per i problemi identificati (secondo gli SLA di rimedio delle vulnerabilità).

**Monitoraggio delle vulnerabilità degli SBOM**: Gli strumenti SCA devono monitorare continuamente i componenti degli SBOM rispetto ai database delle vulnerabilità. Le nuove vulnerabilità critiche/alte che riguardano i componenti degli SBOM devono generare avvisi al Responsabile sviluppo entro 24 ore.

**Conservazione degli SBOM**: Gli SBOM devono essere conservati per il ciclo di vita dell'applicazione più 3 anni.

I risultati dei test, inclusi i report dei test di penetrazione, devono essere comunicati al Team di revisione della direzione.

---

## Rimedio delle vulnerabilità

Le vulnerabilità di sicurezza identificate durante lo sviluppo e il testing devono essere remediate entro i tempi definiti in base alla gravità.

**Service Level Agreement per la remediation**:

| Gravità | Punteggio CVSS | SLA di remediation | Impatto sulla distribuzione |
|---------|----------------|-------------------|------------------------------|
| **Critica** | 9,0–10,0 | 7 giorni | Bloccare la distribuzione se non risolta |
| **Alta** | 7,0–8,9 | 30 giorni | Bloccare la distribuzione se scaduto |
| **Media** | 4,0–6,9 | 90 giorni | Tracciare come debito tecnico |
| **Bassa** | 0,1–3,9 | 180 giorni | Pianificare per il prossimo rilascio principale |

Tutte le vulnerabilità identificate nella fase di test, inclusi i test di penetrazione, devono essere corrette prima della promozione in produzione o gestite tramite il processo di gestione del rischio e delle eccezioni.

**Processo di escalation**:

- Le vulnerabilità che superano l'SLA di remediation devono essere escalate al RSSI e al Proprietario dell'applicazione.
- Le vulnerabilità critiche e alte scadute oltre l'SLA devono bloccare le distribuzioni successive fino alla remediation o all'approvazione di un'eccezione con controlli compensativi.
- Lo stato della remediation delle vulnerabilità deve essere revisionato mensilmente e comunicato trimestralmente al Team di revisione della direzione.

---

## Protezione dei dati di test

I dati di produzione non devono essere utilizzati per il testing o lo sviluppo.

I dati personali (come definiti dall'Art. 5 della nLPD svizzera) non devono essere utilizzati per il testing o lo sviluppo.

Se le informazioni sensibili sono richieste come parte del processo di testing, devono essere:

- **sanificate** (campi sensibili rimossi o sostituiti),
- **anonimizzate** (rimozione irreversibile delle caratteristiche identificative), oppure
- **pseudonimizzate** (dati identificativi sostituiti con identificatori artificiali).

I **dati sintetici** (dati generati artificialmente senza connessione a persone reali) sono l'approccio preferito e devono essere utilizzati ove fattibile.

La creazione e l'uso dei dataset di test devono essere documentati e approvati dal proprietario dei dati. I dataset di test contenenti dati personali trasformati devono essere trattati come classificazione Interno come minimo.

I dati di test devono essere cancellati in modo sicuro quando non sono più necessari.

---

## Promozione del codice in produzione

Il codice deve essere promosso in produzione solo dal personale autorizzato ed essere soggetto al processo documentato di gestione delle modifiche.

Prima della promozione in produzione:

- Tutti i gate di sicurezza richiesti devono essere superati (test di sicurezza, code review, rimedio delle vulnerabilità).
- L'ambiente di produzione deve essere sottoposto a backup per facilitare il rollback in caso di modifica non riuscita.
- I dati di test devono essere rimossi dall'applicazione.
- Nell'ambiente di produzione non devono essere presenti file di sviluppo, configurazioni di debug, account di test o dati di test.
- Per le applicazioni ad alto rischio, il RSSI o l'autorità di sicurezza designata deve fornire approvazione esplicita.

I registri di promozione devono includere il riferimento al ticket di modifica, il responsabile dell'approvazione, lo stato dei gate di sicurezza e il timestamp della distribuzione.

---

## Sviluppo in outsourcing

Laddove lo sviluppo del software è esternalizzato a contraenti terzi o partner di sviluppo, si applicano i requisiti di sviluppo sicuro dell'organizzazione.

**I requisiti contrattuali devono includere**:

- Conformità agli standard di codifica sicura e ai requisiti di sicurezza dell'organizzazione.
- Obblighi di test di sicurezza (SAST, DAST, SCA) con report all'organizzazione.
- SLA di rimedio delle vulnerabilità allineati con questa politica.
- Notifica degli incidenti di sicurezza entro 24 ore dalla scoperta.
- Il diritto dell'organizzazione di verificare le pratiche di sicurezza del contraente con un preavviso di 30 giorni.
- Diritti di partecipazione alla code review e alla revisione dell'architettura di sicurezza.

**Verifica della conformità del contraente**:

- I contraenti devono presentare i report dei test di sicurezza (risultati SAST/DAST/SCA, stato della remediation) agli intervalli concordati.
- I progetti in outsourcing ad alto rischio devono essere soggetti alla revisione della sicurezza da parte del personale qualificato in sicurezza dell'organizzazione nelle principali tappe (approvazione del design, pre-produzione).
- Il codice consegnato dai contraenti deve seguire lo stesso processo di code review e test di sicurezza del codice sviluppato internamente prima dell'accettazione.

---

## Formazione sulla sicurezza per gli sviluppatori

Tutti gli sviluppatori devono completare una formazione sulla sicurezza adeguata al loro ruolo e alle loro responsabilità.

**Requisiti di formazione**:

| Tipo di formazione | Destinatari | Frequenza | Durata minima |
|--------------------|-------------|-----------|---------------|
| **Formazione iniziale sulla sicurezza** | Tutti gli sviluppatori | Prima dell'accesso al codice di produzione | 4 ore |
| **Aggiornamento annuale** | Tutti gli sviluppatori | Annualmente | 2 ore |
| **Formazione Security Champion** (facoltativa per le PMI) | Security Champion nominati | Iniziale + annualmente | 8 ore + 4 ore |

La formazione deve coprire, come minimo:

- Le vulnerabilità OWASP Top 10 e le tecniche di mitigazione.
- Le pratiche di codifica sicura rilevanti per lo stack tecnologico dello sviluppatore.
- La politica di sviluppo sicuro e gli standard di codifica dell'organizzazione.
- Le vulnerabilità software più comuni (CWE/SANS Top 25).

Il completamento della formazione deve essere registrato e verificato prima di concedere l'accesso al codice di produzione. I registri di formazione devono essere conservati per la durata dell'impiego più 3 anni.

Ove le risorse lo consentano, l'organizzazione dovrebbe istituire un **programma Security Champion** — sviluppatori nominati all'interno di ciascun team che ricevono formazione avanzata sulla sicurezza e fungono da primo punto di contatto per le domande sulla sicurezza all'interno del loro team.

**Programma Security Champion** (ove istituito):

**Criteri di selezione**: I Security Champion devono essere nominati dai team di sviluppo sulla base di: interesse dimostrato per la sicurezza, almeno 2 anni di esperienza nello sviluppo, disponibilità a dedicare circa il 10% del tempo di lavoro alle attività di sicurezza e approvazione del responsabile del team.

**Responsabilità**:
- Condurre code review focalizzate sulla sicurezza per le modifiche ad alto rischio all'interno del proprio team.
- Fornire orientamento e mentoring sulla codifica sicura ai membri del team.
- Partecipare alle sessioni di modellazione delle minacce come rappresentante della sicurezza del team.
- Escalare le preoccupazioni di sicurezza al RSSI o al team di sicurezza.
- Mantenersi aggiornato sulle minacce e vulnerabilità emergenti rilevanti per lo stack tecnologico del team.
- Promuovere la cultura della sicurezza e la consapevolezza all'interno del team.

**Formazione**: Formazione iniziale: 8 ore (approfondimento OWASP Top 10, schemi di architettura sicura, modellazione delle minacce, strumenti di test di sicurezza). Aggiornamento annuale: 4 ore (minacce emergenti, nuove tecniche di attacco, standard aggiornati).

**Incentivi**: I contributi dei Security Champion devono essere riconosciuti nelle valutazioni delle prestazioni. L'organizzazione dovrebbe considerare la partecipazione a conferenze, la sponsorizzazione di certificazioni o opportunità di sviluppo professionale simili.

**Metriche del programma**: Numero di Security Champion attivi (obiettivo: almeno 1 per team di sviluppo), tasso di partecipazione alla revisione della sicurezza, risultati di sicurezza identificati nella code review, tasso di completamento della formazione.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RSSI** | Titolarità della politica; approvazione dei gate di sicurezza per le applicazioni ad alto rischio; approvazione delle eccezioni; autorità di escalation; supervisione del programma di formazione |
| **Responsabile sviluppo** | Integrazione della sicurezza nel ciclo di sviluppo; applicazione della code review; manutenzione degli standard di codifica sicura; supervisione della remediation delle vulnerabilità; classificazione del rischio applicativo |
| **Security Champion** (ove istituito) | Promozione della sicurezza all'interno del team di sviluppo; code review focalizzata sulla sicurezza; mentoring sulla codifica sicura |
| **Sviluppatori** | Aderenza agli standard di codifica sicura; remediation delle vulnerabilità; completamento della formazione sulla sicurezza; partecipazione alla code review |
| **QA / Responsabile test** | Esecuzione dei test di sicurezza; gestione dell'ambiente di test; protezione dei dati di test; reportistica dei test di sicurezza |
| **DevOps / Team piattaforma** | Integrazione degli strumenti di sicurezza CI/CD; segregazione degli ambienti; automazione della distribuzione; scansione dei segreti |
| **Proprietario dell'applicazione** | Input per la classificazione del rischio applicativo; richieste di eccezione; approvazione dei requisiti di sicurezza |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| # | Prova | Responsabile | Frequenza |
|---|-------|--------------|-----------|
| 1 | **Registro di classificazione del rischio applicativo** (tutte le applicazioni classificate per livello di rischio) | Responsabile sviluppo / RSSI | *Mantenuto continuamente; rivisto annualmente; obiettivo: 100% delle applicazioni classificate* |
| 2 | **Documentazione dei requisiti di sicurezza** (specifiche dei requisiti, modelli delle minacce per alto rischio) | Responsabile sviluppo | *Per progetto; conservato per il ciclo di vita dell'applicazione* |
| 3 | **Report delle scansioni SAST/SCA** (log di esecuzione degli strumenti, risultati, stato della remediation) | DevOps / Responsabile sviluppo | *Secondo la frequenza della politica per livello di rischio; conservati 2 anni* |
| 4 | **Report dei test di penetrazione** (ambito, risultati, verifica della remediation) | RSSI | *Annualmente per alto rischio; ogni 2 anni per rischio medio; conservati 5 anni* |
| 5 | **Registri della code review** (commenti di revisione, registri di approvazione, cronologia delle merge request) | Responsabile sviluppo | *Per modifica del codice; conservati 2 anni* |
| 6 | **Registri di remediation delle vulnerabilità** (ticket con tracciamento degli SLA, prove di chiusura) | Responsabile sviluppo | *Per vulnerabilità; rivisti mensilmente; conservati 3 anni* |
| 7 | **Documentazione della segregazione degli ambienti** (diagrammi di rete, registri di controllo degli accessi) | DevOps / IT Operations | *Revisionata annualmente; aggiornata in caso di modifica* |
| 8 | **Registri di formazione sulla sicurezza per sviluppatori** (date di completamento, contenuto della formazione) | RSSI / HR | *Tracciati per sviluppatore; revisionati annualmente; obiettivo: 100% completamento* |
| 9 | **Report di sicurezza dello sviluppo in outsourcing** (risultati SAST/DAST/SCA del contraente, registri di audit) | Responsabile sviluppo / RSSI | *Secondo i termini del contratto; conservati per la durata del contratto + 3 anni* |
| 10 | **Registri di distribuzione in produzione** (ticket di modifica, approvazione dei gate di sicurezza, piani di rollback) | Gestione delle modifiche / DevOps | *Per distribuzione; conservati 3 anni* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, report delle scansioni SAST/DAST/SCA, registri della code review, report dei test di penetrazione, registri di formazione degli sviluppatori, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere comunicate al Team di revisione della direzione. Le distribuzioni di emergenza che bypassano i gate di sicurezza richiedono l'approvazione del RSSI e una validazione retrospettiva della sicurezza entro 72 ore.

## Non conformità

Un dipendente che si constata abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare le modifiche agli standard di sviluppo sicuro (OWASP, NIST SSDF, CWE/SANS Top 25), le minacce e le tecniche di attacco emergenti, le modifiche normative, i cambiamenti negli strumenti e nelle metodologie di sviluppo, e le lezioni apprese dagli incidenti di sicurezza e dai test di penetrazione.

---

# Aree della norma ISO 27001 trattate

Politica sul ciclo di vita dello sviluppo sicuro — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.4 Accesso al codice sorgente |
| | **8.25 Ciclo di vita dello sviluppo sicuro** |
| | **8.26 Requisiti di sicurezza delle applicazioni** |
| | 8.27 Principi di architettura e ingegneria del sistema sicuro |
| | 8.28 Codifica sicura |
| | **8.29 Test di sicurezza nello sviluppo e nell'accettazione** |
| | 8.30 Sviluppo in outsourcing |
| | 8.31 Separazione degli ambienti di sviluppo, test e produzione |
| | 8.33 Informazioni di test |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera (revDSG) | Art. 7 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 8 — Misure tecniche e organizzative per la protezione dei dati |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 25 — Protezione dei dati per impostazione predefinita e fin dalla progettazione; Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controlli Allegato A 8.25, 8.26, 8.29 — Sviluppo sicuro, requisiti di sicurezza delle applicazioni, test di sicurezza |
| ISO/IEC 27002:2022 | Sezioni 8.25–8.31, 8.33 — Guida all'implementazione dei controlli di sviluppo sicuro |
| NIST SP 800-218 (SSDF) | Secure Software Development Framework — gruppi di pratiche PO, PS, PW, RV |
| OWASP Top 10:2025 | Base minima per i test — include Software Supply Chain Failures e Mishandling of Exceptional Conditions |
| CWE/SANS Top 25 | Vulnerabilità software più pericolose — riferimento per la codifica sicura |

---

<!-- QA_VERIFIED: 2026-04-03 -->
