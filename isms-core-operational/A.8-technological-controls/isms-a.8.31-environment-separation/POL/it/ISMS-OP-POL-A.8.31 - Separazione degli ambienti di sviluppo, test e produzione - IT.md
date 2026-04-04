<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.31-IT:operational:OP-POL:a.8.31 -->
**ISMS-OP-POL-A.8.31 — Separazione degli ambienti di sviluppo, test e produzione**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Separazione degli ambienti di sviluppo, test e produzione |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.31 |
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

- ISO/IEC 27001:2022 Controllo A.8.31 — Separazione degli ambienti di sviluppo, test e produzione
- ISO/IEC 27002:2022 Sezione 8.31 — Linee guida di implementazione per la separazione degli ambienti
- NIST SP 800-53 Rev 5 — CM-4 (Analisi dell'impatto), CM-7 (Funzionalità minima), SA-11 (Test da parte degli sviluppatori), SC-32 (Partizionamento del sistema)
- CIS Controls v8 — Salvaguardia 16.1–16.14 (Sicurezza del software applicativo)

**Controlli Annex A correlati**:

| Controllo | Relazione con la separazione degli ambienti |
|---------|----------------------------------------|
| A.5.15–16–18 Gestione delle identità e degli accessi | Framework IAM fondamentale; accesso basato sul ruolo per livello di ambiente |
| A.5.34 Privacy e dati personali | I dati di test contenenti dati personali richiedono anonimizzazione o sostituzione sintetica |
| A.8.2–3–5 Autenticazione e accesso privilegiato | AMF per l'accesso alla produzione; gestione degli accessi privilegiati per l'accesso d'emergenza |
| A.8.4 Accesso al codice sorgente | I controlli di accesso al repository e la protezione dei rami si integrano nei flussi di promozione |
| A.8.9 Gestione della configurazione | Configurazioni di base specifiche per ambiente e rilevamento delle derive |
| A.8.11 Mascheratura dei dati | Tecniche per proteggere i dati utilizzati in ambienti non di produzione |
| A.8.15 Registrazione | Registrazione degli accessi agli ambienti, delle promozioni e degli eventi di accesso d'emergenza |
| A.8.25–26–29 Ciclo di vita dello sviluppo sicuro | Integrazione SDLC; gate di testing della sicurezza tra gli ambienti |
| A.8.32 Gestione delle modifiche | Approvazione del Comitato consultivo per le modifiche (CAB) per i rilasci in produzione |
| A.8.33 Informazioni di test | Protezione e gestione dei dati di test negli ambienti |

**Politiche interne correlate**:

- Politica di gestione delle identità e degli accessi
- Politica del ciclo di vita dello sviluppo sicuro
- Politica di gestione delle modifiche
- Politica di registrazione e monitoraggio
- Politica di classificazione e gestione dei dati
- Politica sulla privacy e protezione dei dati personali
- Politica di risposta agli incidenti

---

# Politica di separazione degli ambienti di sviluppo, test e produzione

## Scopo

Lo scopo di questa politica è garantire che gli ambienti di sviluppo, test e produzione siano separati e protetti per ridurre il rischio di accesso non autorizzato o di modifiche all'ambiente di produzione. La separazione degli ambienti protegge le operazioni aziendali dalle attività di sviluppo e test che potrebbero introdurre errori, vulnerabilità o modifiche non autorizzate ai sistemi e ai dati in produzione.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative appropriate al rischio per proteggere i dati personali trattati negli ambienti di produzione, e vietando l'utilizzo di dati personali di produzione negli ambienti di sviluppo e test senza controlli di protezione equivalenti. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32. La separazione degli ambienti è una misura tecnica fondamentale per dimostrare che i sistemi che trattano dati personali sono soggetti a adeguate restrizioni di accesso e controlli sulla gestione dei dati.

## Ambito

Tutti i sistemi informativi, le applicazioni e le infrastrutture gestite, controllate o operate dall'organizzazione e considerate nell'ambito dalla dichiarazione di applicabilità ISO 27001. Ciò comprende:

- Tutti i livelli di ambiente: sviluppo, testing/QA, staging/pre-produzione e produzione.
- Tutti i modelli di hosting: on-premises, cloud ([Fornitore cloud] — ad es. AWS, Azure, GCP o equivalente), ibrido e infrastruttura basata su container ([Piattaforma container] — ad es. Kubernetes, Docker Swarm o equivalente).
- Tutte le pipeline CI/CD ([Piattaforma CI/CD] — ad es. GitHub Actions, GitLab CI, Jenkins, Azure DevOps o equivalente) che promuovono le modifiche tra gli ambienti.
- Sistemi gestiti da terze parti che trattano dati organizzativi dove l'organizzazione mantiene la responsabilità di gestione dell'ambiente.

Tutti i dipendenti, i collaboratori esterni e gli utenti terzi con accesso a qualsiasi ambiente.

**Fuori ambito**: Ambienti di ricerca isolati per singolo utente non connessi alle reti organizzative; sistemi temporanei di proof-of-concept privi di dati organizzativi o personali; sistemi dimostrativi dei fornitori gestiti interamente dai fornitori stessi. Una volta che i sistemi di ricerca o proof-of-concept passano all'uso organizzativo, devono conformarsi a questa politica.

## Principio

Gli ambienti di sviluppo, test e produzione devono essere separati per proteggere l'integrità, la disponibilità e la riservatezza dei sistemi e dei dati di produzione. Le modifiche devono seguire percorsi di promozione definiti con revisione e approvazione appropriate ad ogni fase. Nessun individuo deve avere la capacità di apportare modifiche sia all'ambiente di sviluppo che a quello di produzione senza previa revisione e approvazione. Il livello di separazione deve essere commisurato al rischio per le operazioni aziendali e alla sensibilità dei dati trattati.

L'organizzazione deve amministrare centralmente l'accesso agli ambienti utilizzando controlli degli accessi basati sui ruoli. L'accesso predefinito agli ambienti di produzione deve essere "nessun accesso" — è necessaria una concessione esplicita per qualsiasi livello di accesso. Gli sviluppatori non devono avere accesso permanente all'infrastruttura di produzione.

---

## Definizioni degli ambienti

L'organizzazione deve mantenere almeno i seguenti livelli di ambiente. Ogni livello deve avere uno scopo definito, risorse infrastrutturali dedicate, restrizioni documentate sulla gestione dei dati e controlli degli accessi applicati.

**Livelli di ambiente**:

| Ambiente | Scopo | Dati consentiti | Accesso |
|-------------|---------|----------------|--------|
| **Sviluppo** | Sviluppo attivo del codice, sperimentazione, integrazione | Solo dati sintetici; nessun dato di produzione | Sviluppatori (completo); QA (lettura); Operazioni (secondo necessità) |
| **Testing / QA** | Assicurazione della qualità, test di integrazione, test di accettazione utente | Dati sintetici o anonimizzati (approvati dal DPD) | Team QA (completo); Sviluppatori (limitato); Operazioni (secondo necessità) |
| **Staging / Pre-produzione** | Validazione finale prima del rilascio in produzione; rispecchia la configurazione di produzione | Dati sintetici o anonimizzati; configurazione di produzione (non i dati) | Operazioni (completo); QA (lettura); Sviluppatori (solo lettura per il monitoraggio) |
| **Produzione** | Operazioni aziendali live che servono utenti reali con dati aziendali reali | Dati di produzione (dati aziendali e personali reali) | Operazioni (completo); Sviluppatori (nessun accesso permanente; solo accesso d'emergenza) |
| **Sandbox** (opzionale) | Sperimentazione isolata, valutazione tecnologica, proof-of-concept | Solo dati sintetici; nessuna connettività di rete ad altri ambienti | Sviluppatori (completo); nessuna connettività alle reti di produzione |

I nomi degli ambienti e le etichette visive devono identificare chiaramente il tipo di ambiente (ad es. banner con codice colore, prefissi hostname, etichette della console) per prevenire operazioni accidentali nell'ambiente sbagliato.

---

## Separazione di rete

Gli ambienti devono essere isolati attraverso la segmentazione di rete per prevenire flussi di dati e accessi non intenzionali tra ambienti diversi.

**Requisiti di separazione di rete**:

| Requisito | Standard |
|-------------|----------|
| Isolamento di rete | Ogni ambiente su un segmento di rete separato, VLAN, VPC o equivalente |
| Regola di traffico predefinita | Nega tutto tra gli ambienti; sono consentiti solo i percorsi di promozione controllati |
| Connettività produzione-sviluppo | Vietata — nessun percorso di rete diretto tra produzione e sviluppo |
| Regole del firewall | Documentate, revisionate trimestralmente e limitate ai flussi strettamente necessari |
| Separazione DNS | Zone DNS o spazi dei nomi separati per ambiente per prevenire la risoluzione tra ambienti |

**Separazione degli ambienti cloud**:

Dove l'organizzazione utilizza infrastrutture cloud, la separazione degli ambienti deve essere implementata utilizzando il modello di confine per account o sottoscrizione del fornitore cloud:

| Fornitore cloud | Meccanismo di separazione |
|----------------|---------------------|
| AWS | Account AWS separati per ambiente all'interno di un'organizzazione AWS |
| Azure | Sottoscrizioni separate per ambiente all'interno di un gruppo di gestione |
| GCP | Progetti separati per ambiente all'interno di un'organizzazione |
| Multi-cloud | Modello di separazione coerente documentato per fornitore |

**Separazione di container e Kubernetes**:

Dove l'organizzazione utilizza piattaforme di orchestrazione dei container, gli ambienti devono essere separati usando:

- Cluster separati per ambiente (preferibile per l'isolamento della produzione).
- Separazione a livello di namespace con criteri di rete applicati per gli ambienti non di produzione.
- I carichi di lavoro di produzione non devono condividere un cluster con carichi di lavoro di sviluppo o test.
- I registri delle immagini container devono essere separati o controllati per accesso per ambiente.

**Sicurezza dei container in produzione:**

- I container di produzione non devono montare i filesystem dell'host salvo casi d'uso esplicitamente approvati.
- I container di produzione devono essere eseguiti come utenti non root.
- Le immagini dei container di produzione devono essere firmate e verificate prima del rilascio.
- I registri dei container devono essere separati per ambiente (ad es. `prod.registry.example.com` vs `dev.registry.example.com`).

**Hardening Kubernetes in produzione:**

- I cluster di produzione devono utilizzare control plane e pool di nodi separati.
- I Pod Security Standards (PSS) devono essere applicati al livello "Restricted" per la produzione.
- I criteri di rete devono negare tutto per impostazione predefinita con regole di autorizzazione esplicite.
- Gli account di servizio devono essere limitati alle autorizzazioni minime richieste.

---

## Controllo degli accessi per ambiente

L'accesso a ciascun ambiente deve seguire il principio del privilegio minimo. I diritti di accesso devono essere definiti per ruolo e livello di ambiente.

**Matrice degli accessi**:

| Ruolo | Sviluppo | Testing / QA | Staging | Produzione |
|------|-------------|-------------|---------|------------|
| **Sviluppatore** | Accesso completo | Lettura + rilascio in test | Solo lettura | Nessun accesso permanente |
| **Ingegnere QA** | Lettura | Accesso completo | Lettura + esecuzione test | Nessun accesso |
| **Operazioni / SRE** | Secondo necessità | Secondo necessità | Accesso completo | Accesso completo |
| **Amministratore di database** | Secondo necessità | Secondo necessità | Secondo necessità | Accesso completo (con PAM) |
| **Team di sicurezza** | Lettura (audit) | Lettura (audit) | Lettura (audit) | Lettura (audit + monitoraggio) |
| **Collaboratore esterno** | Limitato al progetto | Limitato al progetto | Nessun accesso | Nessun accesso |

**Restrizioni di accesso alla produzione**:

- Gli sviluppatori non devono avere accesso permanente all'infrastruttura di produzione, ai database o alle console applicative.
- Ogni accesso alla produzione deve richiedere l'autenticazione a più fattori (AMF).
- Le sessioni di accesso alla produzione devono essere registrate, tracciate e monitorate.
- L'accesso privilegiato alla produzione deve essere gestito attraverso un sistema di Gestione degli accessi privilegiati (PAM) ([Strumento PAM] — ad es. CyberArk, HashiCorp Boundary, AWS SSM Session Manager o equivalente).

**Accesso d'emergenza (break-glass)**:

L'accesso d'emergenza degli sviluppatori alla produzione è consentito solo durante incidenti dichiarati in cui le competenze degli sviluppatori sono necessarie per la risoluzione. L'accesso d'emergenza deve:

- Richiedere l'approvazione del Responsabile dell'incidente e del RSSI (o delegato).
- Essere limitato nel tempo a un massimo di 8 ore, rinnovabile con nuova approvazione.
- Essere limitato allo scopo dell'incidente dichiarato.
- Essere registrato con: identificativo dell'incidente, sviluppatore richiedente, autorità approvante, durata dell'accesso, sistemi a cui si è avuto accesso e azioni eseguite.
- Attivare una revisione post-incidente obbligatoria entro 7 giorni dalla chiusura dell'incidente.

Le attivazioni dell'accesso d'emergenza devono essere revisionate mensilmente dal Responsabile della sicurezza delle informazioni e riportate nella dashboard trimestrale del RSSI con analisi delle tendenze.

**Revisioni degli accessi**:

| Ambiente | Frequenza di revisione |
|-------------|-----------------|
| Produzione | Trimestrale |
| Staging | Semestrale |
| Sviluppo / Test | Annuale |

L'accesso dei dipendenti cessati deve essere revocato entro lo stesso giorno lavorativo in tutti gli ambienti. Il deprovisioning automatizzato tramite il sistema di gestione delle identità è preferibile.

---

## Regole per la gestione dei dati

I dati di produzione non devono essere utilizzati negli ambienti di sviluppo o test. Questo requisito protegge i dati aziendali critici dall'esposizione in ambienti meno controllati e supporta la conformità alla nLPD per i dati personali.

**Divieto di dati di produzione**:

- I dati di produzione non devono essere copiati, esportati, ripristinati o replicati negli ambienti di sviluppo, test o staging.
- I backup del database di produzione non devono essere ripristinati in ambienti non di produzione.
- Le credenziali di produzione, le chiavi API, le stringhe di connessione e i segreti non devono essere utilizzati in ambienti non di produzione.
- I file di log contenenti dati personali di produzione non devono essere trasferiti in ambienti non di produzione senza anonimizzazione.

**Fonti di dati approvate per ambienti non di produzione**:

| Fonte di dati | Approvazione richiesta | Restrizioni |
|-------------|-------------------|-------------|
| **Dati sintetici** (generati, non derivati dalla produzione) | Nessuna approvazione aggiuntiva | Metodo preferito; strutturalmente rappresentativo ma interamente artificiale |
| **Dati anonimizzati** (de-identificati irreversibilmente dalla produzione) | Approvazione del Responsabile della protezione dei dati (DPD) | L'anonimizzazione deve essere irreversibile; validata rispetto al rischio di re-identificazione; eliminata entro 30 giorni dal completamento del progetto |
| **Dati pseudonimizzati** (de-identificati reversibilmente) | Approvazione del RSSI e del DPD; trattati come dati personali ai sensi della nLPD | Accettabile solo dove l'anonimizzazione o i dati sintetici sono tecnicamente impossibili; sono richiesti controlli di sicurezza equivalenti |
| **Sottoinsieme della struttura di produzione** (solo schema, nessun dato) | Approvazione del Responsabile dello sviluppo | Schemi di database, contratti API, template di configurazione senza valori dei dati |

Ai sensi della nLPD svizzera (revDSG), i dati pseudonimizzati rimangono dati personali per qualsiasi parte che detiene o può accedere alla chiave di pseudonimizzazione. I dati completamente anonimizzati — dove la re-identificazione non è possibile con nessun mezzo ragionevole — esulano dall'ambito della nLPD.

**Applicazione della classificazione dei dati**:

- Le classificazioni dei dati Riservato e Ristretto devono essere vietate negli ambienti di sviluppo e test.
- Deve essere implementata la scansione automatizzata per rilevare i pattern di dati di produzione vietati (ad es. nomi reali, identificatori nazionali, numeri di conto finanziario) negli ambienti non di produzione. La scansione deve coprire database, file system, file di log e immagini container.
- Le violazioni devono essere remediate entro 7 giorni dal rilevamento e segnalate al Responsabile della sicurezza delle informazioni.

---

## Gestione dei dati di test

I dati di test devono essere gestiti come un asset controllato lungo tutto il ciclo di vita dello sviluppo software.

**Principi per i dati di test**:

- I dati sintetici devono essere l'approccio predefinito e preferito per tutte le attività di test.
- I dati di test devono essere strutturalmente rappresentativi dei dati di produzione (stesso schema, tipi di dati, relazioni e caratteristiche di volume) senza contenere dati personali o aziendali reali.
- La generazione dei dati di test deve essere automatizzata dove praticabile utilizzando [Strumento per dati di test] (ad es. Faker, Mockaroo, Tonic.ai, Delphix o equivalente).
- I dati di test devono essere versionati e riproducibili per supportare i test di regressione.
- I dati di test devono essere eliminati dagli ambienti non di produzione entro 30 giorni dal completamento del progetto o dalla conclusione del ciclo di test.

**Validazione dell'anonimizzazione**:

Dove i dati di produzione anonimizzati sono approvati per l'uso in ambienti non di produzione, il processo di anonimizzazione deve essere validato prima di ogni utilizzo:

1. Il Responsabile della protezione dei dati deve verificare che gli identificatori diretti siano stati rimossi o sostituiti.
2. Le combinazioni di quasi-identificatori devono essere valutate per il rischio di re-identificazione.
3. I risultati della validazione devono essere documentati e conservati a fini di audit.
4. Una validazione fallita deve comportare il rifiuto e la remediation prima che i dati possano essere utilizzati.

**Dati dei titolari di carta**: I dati dei titolari di carta (PAN, CVV, dati di traccia) non devono mai essere utilizzati negli ambienti di sviluppo o test, indipendentemente dallo stato di anonimizzazione. Al loro posto devono essere utilizzati numeri di carta sintetici conformi agli intervalli di test.

---

## Processo di promozione del codice

Le modifiche devono seguire un percorso di promozione definito dallo sviluppo alla produzione. Il rilascio diretto in produzione deve essere vietato salvo per le correzioni d'emergenza approvate.

**Percorso di promozione standard**:

```
Sviluppo → Testing / QA → Staging → Produzione
```

Ogni fase di promozione deve includere gate di qualità e sicurezza definiti.

**Requisiti dei gate di promozione**:

| Gate | Da → A | Requisiti |
|------|-----------|-------------|
| **Gate 1** | Sviluppo → Testing | Revisione del codice completata (minimo 1 revisore, non l'autore); test unitari automatizzati superati; scansione dell'analisi statica superata; nessuna vulnerabilità critica o alta |
| **Gate 2** | Testing → Staging | Test di integrazione superati; approvazione QA; test di sicurezza completi (SAST, DAST dove applicabile); test delle prestazioni superati per i sistemi critici |
| **Gate 3** | Staging → Produzione | Approvazione del Comitato consultivo per le modifiche (CAB) (per A.8.32); piano di rollback documentato e testato; backup di produzione verificato; runbook di rilascio revisionato; approvazione del proprietario del sistema |

**Separazione dei compiti nella promozione**:

- Lo sviluppatore che scrive il codice non deve essere la stessa persona che approva la sua promozione in produzione.
- La persona che promuove il codice in staging non deve essere la stessa persona che lo promuove in produzione, dove le dimensioni del team lo consentono.
- Le credenziali della pipeline CI/CD per il rilascio in produzione devono essere limitate al team delle operazioni.

**Sicurezza della pipeline CI/CD**:

- Le definizioni delle pipeline devono essere sotto controllo versione e soggette a revisione del codice.
- Le credenziali e i segreti della pipeline devono essere archiviati nell'archivio segreti della piattaforma di pipeline — non codificati nelle definizioni della pipeline.
- Ogni ambiente deve avere credenziali di pipeline dedicate con le autorizzazioni minime richieste.
- I log di esecuzione della pipeline devono essere conservati a fini di audit (minimo 1 anno).
- Gli artefatti devono essere costruiti una volta sola e promossi attraverso gli ambienti (artefatti immutabili) — non ricostruiti per ogni ambiente.

**Rilasci d'emergenza**:

Le correzioni d'emergenza possono bypassare il percorso di promozione standard nelle seguenti condizioni:

- Un incidente dichiarato o una vulnerabilità critica della sicurezza che richiede una remediation immediata.
- Approvazione del Responsabile dell'incidente (o del responsabile di turno) e del RSSI (o delegato).
- Revisione post-implementazione entro 48 ore, inclusi test retrospettivi in tutti gli ambienti saltati.
- Documentazione dell'emergenza nel sistema di gestione delle modifiche con giustificazione per il bypass dei gate.

**Capacità di rollback**:

- Le versioni precedenti devono essere conservate per supportare il rollback.
- Le procedure di rollback devono essere documentate e testate almeno trimestralmente.
- Il team delle operazioni deve essere autorizzato a eseguire rollback senza approvazione aggiuntiva durante gli incidenti.
- Gli ambienti di produzione devono essere sottoposti a backup prima di ogni rilascio per facilitare il rollback.
- I dati di test e gli artefatti di sviluppo devono essere rimossi prima della promozione in produzione.

---

## Separazione della configurazione

Le configurazioni degli ambienti devono essere gestite per prevenire fughe di credenziali, contaminazione tra ambienti e deriva della configurazione.

**Requisiti di separazione della configurazione**:

| Requisito | Standard |
|-------------|----------|
| Credenziali e segreti | Univoci per ambiente; archiviati in un gestore di segreti ([Gestore segreti] — ad es. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault o equivalente) |
| Stringhe di connessione al database | Specifiche per ambiente; non condivise tra livelli |
| Endpoint API | URL specifici per ambiente; nessun endpoint di produzione hardcoded nel codice non di produzione |
| Feature flag | Configurazione specifica per ambiente; i flag di produzione gestiti separatamente dallo sviluppo |
| Infrastructure as Code | Configurazioni di ambiente archiviate nel controllo versione; le modifiche seguono lo stesso percorso di promozione del codice applicativo |

**Parità di configurazione**:

- Gli ambienti di staging devono rispecchiare il più possibile la configurazione di produzione (stesse versioni del software, stessa dimensione dell'infrastruttura entro i vincoli di budget, stessi controlli di sicurezza).
- La deriva della configurazione tra staging e produzione deve essere rilevata e segnalata. Il rilevamento delle derive deve essere eseguito almeno settimanalmente.
- Le differenze tra staging e produzione devono essere documentate, giustificate e approvate dal Responsabile delle operazioni IT.

**Differenze documentate tra staging e produzione:**

La tabella seguente deve essere mantenuta dal Responsabile delle operazioni IT e revisionata trimestralmente. Le differenze non approvate rilevate tramite il rilevamento delle derive devono essere investigate e risolte.

| Elemento di configurazione | Staging | Produzione | Giustificazione |
|-------------------|---------|------------|---------------|
| Dimensione delle istanze | Ridotta (ottimizzazione dei costi) | Specifica di produzione completa | Ottimizzazione dei costi; lo staging valida la funzionalità, non il carico |
| Numero di repliche | Minimo (1-2) | Per i requisiti di disponibilità (3+) | Ottimizzazione dei costi; lo staging non richiede alta disponibilità |
| Conservazione dei backup | 7 giorni | Per la politica di conservazione dei dati (90+ giorni) | Requisito di conformità solo per i dati di produzione |
| Granularità del monitoraggio | Intervalli di 5 minuti | Intervalli di 1 minuto | La produzione richiede alerting più granulare |

**Identificazione dell'ambiente**:

- Ogni ambiente deve mostrare un'identificazione visiva chiara per prevenire operazioni accidentali nell'ambiente sbagliato.
- Prefissi hostname, banner della console, etichette delle schede del browser ed elementi UI con codice colore devono distinguere i livelli di ambiente.
- Gli ambienti di produzione devono mostrare un'identificazione prominente (ad es. banner rossi, etichette "[PRODUZIONE]").

---

## Separazione degli ambienti cloud

Dove l'organizzazione opera in un ambiente cloud o multi-cloud, si applicano i seguenti controlli aggiuntivi.

**Isolamento di account e sottoscrizioni**:

- I carichi di lavoro di produzione devono risiedere in account, sottoscrizioni o progetti cloud dedicati — separati da tutti i carichi di lavoro non di produzione.
- Le policy IAM devono impedire l'accesso tra account salvo tramite ruoli esplicitamente definiti e sottoposti ad audit.
- Le policy di controllo dei servizi (SCP), le policy di Azure o le policy dell'organizzazione devono applicare i confini degli ambienti a livello organizzativo.
- La fatturazione deve essere separata per ambiente per consentire l'attribuzione dei costi e il rilevamento delle anomalie.

**Tagging delle risorse cloud**:

Tutte le risorse cloud devono essere taggate con l'identificazione dell'ambiente (ad es. `env:production`, `env:staging`, `env:development`) per supportare:

- L'applicazione automatizzata delle policy (ad es. impedire ai ruoli di sviluppo di accedere ai servizi dati di produzione).
- L'allocazione e la reportistica dei costi per ambiente.
- La scansione di conformità e la reportistica di audit.

**Governance dell'Infrastructure as Code**:

- Le definizioni dell'infrastruttura devono essere archiviate in repository sotto controllo versione.
- Le modifiche all'infrastruttura devono seguire lo stesso flusso di promozione del codice applicativo (sviluppo, revisione, test, rilascio).
- Le modifiche manuali all'infrastruttura di produzione ("ClickOps") sono vietate; tutte le modifiche devono essere applicate attraverso la pipeline CI/CD.

---

## Separazione degli ambienti e risposta agli incidenti

La separazione degli ambienti supporta gli obiettivi di risposta agli incidenti:

| Tipo di incidente | Vantaggio della separazione degli ambienti | Procedura di risposta |
|--------------|-------------------------------|-------------------|
| **Compromissione della produzione** | L'attaccante non può spostarsi al codice di sviluppo/staging | Isolare l'ambiente di produzione interessato; lo sviluppo continua senza interruzioni |
| **Compromissione dello sviluppo** | L'attaccante non può accedere ai dati o ai sistemi di produzione | Ricostruire l'ambiente di sviluppo; nessun impatto sulla produzione |
| **Attacco alla supply chain** | Il codice malevolo rilevato nel testing non raggiunge la produzione | Bloccare la promozione; investigare l'ambito; remediation nello sviluppo |
| **Compromissione della pipeline CI/CD** | Le credenziali della pipeline limitate per ambiente limitano il raggio d'azione | Ruotare le credenziali interessate; verificare la configurazione della pipeline; ricostruire gli artefatti interessati |

Durante gli incidenti che coinvolgono violazioni dei confini degli ambienti (accesso non autorizzato tra ambienti, dati di produzione rilevati in ambienti non di produzione), il Responsabile della sicurezza delle informazioni deve:

- Notificare immediatamente il RSSI e il DPD.
- Valutare l'esposizione dei dati e i requisiti di notifica normativi ai sensi della nLPD.
- Implementare misure di contenimento per prevenire ulteriori accessi tra ambienti.
- Condurre una revisione post-incidente per identificare la causa principale e prevenire il ripetersi.
- Documentare la violazione nel registro delle eccezioni con le azioni correttive.

---

## Esperienza degli sviluppatori e produttività

Questa politica è progettata per proteggere i sistemi di produzione consentendo al contempo una consegna software efficiente. Per supportare la produttività degli sviluppatori:

- **Gli ambienti di sviluppo locali** sono senza restrizioni (nelle workstation degli sviluppatori).
- **L'accesso in sola lettura alla produzione** è disponibile per il monitoraggio, i log e le metriche.
- **L'ambiente di staging** rispecchia da vicino la produzione per test realistici.
- **L'accesso d'emergenza** è disponibile durante gli incidenti (con approvazione).
- **I dati di test sintetici** sono prontamente disponibili e rappresentativi dei pattern di produzione.

Gli sviluppatori sono incoraggiati a proporre miglioramenti agli ambienti di sviluppo e test che mantengano la sicurezza migliorando la produttività.

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Anonimizzazione** | Processo irreversibile di rimozione dei dati personali tale che gli individui non possano essere re-identificati con nessun mezzo ragionevole; i dati anonimizzati non sono dati personali ai sensi della nLPD |
| **Accesso d'emergenza (break-glass)** | Procedura d'emergenza che consente un accesso alla produzione limitato nel tempo e approvato a personale privo di accesso permanente alla produzione |
| **Comitato consultivo per le modifiche (CAB)** | Gruppo interfunzionale che rivede e approva le modifiche agli ambienti di produzione |
| **Pipeline CI/CD** | Flusso di lavoro automatizzato che costruisce, testa e rilascia le modifiche software attraverso i livelli di ambiente |
| **Deriva della configurazione** | Divergenza non intenzionale tra la configurazione prevista (come definita nel codice o nella documentazione) e la configurazione effettiva in esecuzione di un ambiente |
| **Artefatto immutabile** | Un artefatto di build software creato una volta sola e promosso invariato attraverso tutti gli ambienti, garantendo la coerenza |
| **AMF** | Autenticazione a più fattori (MFA) — richiede due o più fattori di verifica per ottenere l'accesso |
| **PAM** | Gestione degli accessi privilegiati — sistema per gestire, monitorare e proteggere l'accesso agli account e alle credenziali privilegiati |
| **Pod Security Standards (PSS)** | Framework nativo di Kubernetes per la definizione di policy di sicurezza a livello di pod; definisce tre livelli (Privileged, Baseline, Restricted) |
| **Ambiente di produzione** | Ambiente operativo live che serve utenti reali con dati aziendali reali |
| **Promozione** | Processo di spostamento delle modifiche da un livello di ambiente a un altro attraverso un flusso di lavoro definito e controllato |
| **Pseudonimizzazione** | Processo reversibile di sostituzione dei dati identificativi con pseudonimi; i dati pseudonimizzati rimangono dati personali ai sensi della nLPD per qualsiasi parte che può accedere alla chiave di re-identificazione |
| **Ambiente di staging** | Ambiente pre-produzione che rispecchia la configurazione di produzione per la validazione finale prima del rilascio |
| **Dati sintetici** | Dati generati artificialmente che mantengono le proprietà statistiche e strutturali dei dati di produzione senza contenere alcuna informazione personale o aziendale reale |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; approvazione delle eccezioni alla separazione degli ambienti; autorità di approvazione per l'accesso d'emergenza; revisione trimestrale della conformità; revisione annuale della politica; reportistica alla Direzione generale |
| **CTO / Responsabile dello sviluppo** | Gestione degli ambienti di sviluppo e test; implementazione della pipeline CI/CD; applicazione del flusso di promozione; formazione degli sviluppatori sulla separazione degli ambienti; allocazione delle risorse per l'infrastruttura degli ambienti |
| **Responsabile delle operazioni IT** | Sicurezza dell'ambiente di produzione; approvazione degli accessi alla produzione; gestione del PAM; esecuzione dei rilasci; procedure di rollback; monitoraggio dell'infrastruttura; rilevamento della deriva della configurazione; documentazione della parità staging-produzione |
| **Responsabile della sicurezza delle informazioni** | Manutenzione della politica; valutazioni di conformità; revisione degli accessi d'emergenza; revisione delle eccezioni; monitoraggio della sicurezza; indagine sugli incidenti; reportistica trimestrale della conformità al RSSI; risposta alle violazioni dei confini degli ambienti |
| **Responsabile della protezione dei dati (DPD)** | Approvazione dell'anonimizzazione per l'utilizzo dei dati in ambienti non di produzione; valutazione del rischio di re-identificazione; conformità dei dati di test alla nLPD; audit sulla gestione dei dati |
| **Responsabile del team QA** | Gestione degli ambienti di test; gestione del ciclo di vita dei dati di test; integrità dell'ambiente di test; approvazione QA per i gate di promozione |
| **Proprietari dei sistemi** | Documentazione dell'architettura degli ambienti; evidenze di conformità per i sistemi di proprietà; segnalazione delle eccezioni; approvazione della promozione per i propri sistemi |
| **Sviluppatori** | Utilizzo esclusivo degli ambienti assegnati; rispetto dei requisiti di gestione dei dati; utilizzo dei flussi di promozione definiti; segnalazione delle violazioni degli ambienti; completamento della formazione sulla separazione degli ambienti; proposta di miglioramenti della produttività entro i limiti della politica |
| **Team di sicurezza** | Monitoraggio dei log di accesso agli ambienti; scansione dei dati di produzione in ambienti non di produzione; indagine sulle violazioni; valutazione della sicurezza dei controlli di separazione degli ambienti; risposta agli incidenti di violazione dei confini degli ambienti |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza | Conservazione |
|---|----------|-------|-----------|-----------|
| 1 | **Inventario degli ambienti** con classificazione del livello, modello di hosting, dettagli di segmentazione di rete e proprietario responsabile | Responsabile delle operazioni IT | Mantenuto continuamente; revisionato annualmente | Vita dell'ambiente + 3 anni |
| 2 | **Documentazione della segmentazione di rete** (regole del firewall, configurazioni VPC, assegnazioni VLAN) con registri di revisione trimestrale | Responsabile delle operazioni IT / Team di rete | Trimestrale | 3 anni |
| 3 | **Matrici di controllo degli accessi** per livello di ambiente con mappature ruolo-autorizzazione | Responsabile delle operazioni IT / Responsabile dello sviluppo | Mantenuto continuamente; revisionato per ciclo di revisione degli accessi | 3 anni |
| 4 | **Registri delle revisioni degli accessi** (produzione trimestrale, staging semestrale, sviluppo/test annuale) | Proprietari dei sistemi / Responsabile delle operazioni IT | Per calendario | 3 anni |
| 5 | **Log delle attivazioni dell'accesso d'emergenza** con identificativo dell'incidente, approvatore, durata, azioni e revisione post-incidente | Responsabile della sicurezza delle informazioni | Per evento; revisione mensile | 3 anni |
| 6 | **Configurazione della pipeline CI/CD** con gate di promozione, requisiti di approvazione e separazione dei compiti | Responsabile dello sviluppo / DevOps | Mantenuto continuamente; revisionato trimestralmente | 2 anni |
| 7 | **Registri dei rilasci in produzione** con approvazione CAB, piano di rollback e risultato del rilascio | Responsabile delle operazioni IT | Per rilascio | 3 anni |
| 8 | **Registri di gestione dei dati di test** (log di generazione di dati sintetici, approvazioni di anonimizzazione, conferme di eliminazione dei dati) | Responsabile del team QA / DPD | Per ciclo di test | 3 anni |
| 9 | **Risultati della scansione dei dati negli ambienti non di produzione** che mostrano l'assenza di dati di produzione rilevati (o registri di remediation per le violazioni) | Team di sicurezza | Scansione settimanale; reportistica mensile | 2 anni |
| 10 | **Rapporti sulla deriva della configurazione** tra staging e produzione con registri di risoluzione | Responsabile delle operazioni IT | Rilevamento settimanale; revisione trimestrale | 2 anni |
| 11 | **Documentazione sulla separazione degli account/sottoscrizioni cloud** con esportazioni delle policy IAM e policy di controllo dei servizi | Responsabile delle operazioni IT / Team cloud | Trimestrale | 3 anni |
| 12 | **Registro delle eccezioni** (richieste, approvazioni, controlli compensativi, date di scadenza, revisioni trimestrali) | Responsabile della sicurezza delle informazioni | Mantenuto continuamente; revisionato trimestralmente | Durata dell'eccezione + 3 anni |
| 13 | **Registri della formazione sulla separazione degli ambienti** per sviluppatori, QA e personale delle operazioni | RSSI / HR | Annualmente | Durata dell'impiego + 3 anni |
| 14 | **Registri dei rilasci d'emergenza** con giustificazione per il bypass del percorso di promozione standard e revisione post-implementazione | Responsabile delle operazioni IT / Responsabile dello sviluppo | Per evento | 3 anni |
| 15 | **Documentazione sulla parità di configurazione staging-produzione** con differenze approvate e registri di revisione trimestrale | Responsabile delle operazioni IT | Trimestrale | 2 anni |
| 16 | **Registri degli incidenti di violazione dei confini degli ambienti** con azioni di contenimento, analisi della causa principale e azioni correttive | Responsabile della sicurezza delle informazioni | Per evento | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui report sugli accessi agli ambienti, audit della segmentazione di rete, revisioni della configurazione della pipeline CI/CD, rapporti di scansione dei dati, registri delle approvazioni dei rilasci, registri di completamento delle revisioni degli accessi, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|--------|--------|-----------------------|
| Ambienti con separazione di rete conforme (nega tutto per default, nessun percorso da sviluppo a produzione) | 100% | Trimestrale |
| Accesso alla produzione limitato al personale delle operazioni autorizzato (nessun accesso permanente degli sviluppatori) | 100% | Trimestrale |
| Rilasci in produzione con approvazione CAB e piano di rollback documentato | >= 95% | Mensile |
| Ambienti non di produzione senza dati di produzione rilevati (scansione pulita) | >= 95% | Mensile |
| Attivazioni dell'accesso d'emergenza con documentazione completa e revisione post-incidente | 100% | Per evento |
| Revisioni degli accessi completate nei tempi previsti per livello di ambiente | >= 90% | Trimestrale |
| Pipeline CI/CD che applicano i gate di promozione e la separazione dei compiti | >= 95% | Trimestrale |
| Dati di test eliminati entro 30 giorni dal completamento del progetto | >= 90% | Trimestrale |
| Immagini container in produzione firmate e verificate | 100% | Mensile |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|-----------|--------|-------------|
| Conformità della separazione di rete | 25% | (Ambienti con separazione di rete conforme) / Totale ambienti x 100 |
| Conformità del controllo degli accessi | 25% | (Ambienti con accesso basato sul ruolo corretto + revisioni completate) / Totale x 100 |
| Conformità del processo di promozione | 25% | (Rilasci in produzione conformi con approvazione + piano di rollback) / Totale rilasci x 100 |
| Conformità della gestione dei dati | 25% | (Ambienti non di produzione senza dati di produzione + dati di test eliminati nei tempi previsti) / Totale x 100 |

**Dashboard di conformità (obiettivo):**

Il Responsabile della sicurezza delle informazioni deve generare questa dashboard trimestralmente e presentarla durante la revisione della direzione:

| Dominio | Punteggio | Stato |
|--------|-------|--------|
| **Conformità complessiva** | [calcolato] | VERDE (>=90%) / GIALLO (>=70%) / ROSSO (<70%) |
| Separazione di rete | [calcolato] | |
| Controllo degli accessi | [calcolato] | |
| Processo di promozione | [calcolato] | |
| Gestione dei dati | [calcolato] | |

Gli elementi che richiedono attenzione e i recenti miglioramenti devono essere evidenziati nel rapporto della dashboard.

**Gestione della non conformità**: Al di sotto del 70% è richiesta un'escalation immediata al RSSI e un piano di remediation. Tra il 70-89% è richiesta la supervisione del Responsabile della sicurezza delle informazioni con revisioni mensili. Al 90% e oltre si segue il monitoraggio trimestrale standard.

**Responsabilità della remediation per componente del punteggio**:

| Componente | Sotto l'obiettivo | Responsabile della remediation | Escalation |
|-----------|-------------|-------------------|------------|
| Conformità della separazione di rete | <100% | Responsabile delle operazioni IT | RSSI a 15 giorni di ritardo |
| Conformità del controllo degli accessi | <100% (produzione) | Responsabile delle operazioni IT / Responsabile dello sviluppo | RSSI a 15 giorni di ritardo |
| Conformità del processo di promozione | <95% | Responsabile dello sviluppo / DevOps | RSSI a 30 giorni di ritardo |
| Conformità della gestione dei dati | <95% | Responsabile del team QA / DPD | RSSI immediatamente se dati personali di produzione trovati in ambienti non di produzione |

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni devono essere segnalate al Team di revisione della direzione.

Le eccezioni possono essere approvate solo per: sistemi legacy programmati per la dismissione entro 12 mesi; limitazioni tecniche dove la separazione completa non è fattibile (con giustificazione documentata e controlli compensativi); eccezioni temporanee durante progetti di migrazione o trasformazione (con data di fine definita).

Quando le eccezioni sono approvate, i controlli compensativi devono includere uno o più dei seguenti: registrazione e monitoraggio avanzati degli accessi, revisione obbligatoria del codice per tutte le modifiche, restrizioni di accesso in sola lettura, requisiti di mascheratura dei dati, maggiore rigore nella gestione delle modifiche e valutazioni di sicurezza più frequenti.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e segnalate al RSSI.

Le violazioni che comportano l'esposizione di dati di produzione in ambienti non di produzione devono essere trattate come incidenti sui dati e segnalate al Responsabile della protezione dei dati per la valutazione ai sensi dei requisiti di notifica delle violazioni della nLPD.

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti nelle capacità delle piattaforme cloud e container, le minacce emergenti alla separazione degli ambienti (attacchi alla supply chain, compromissione della pipeline CI/CD, vulnerabilità di escape dei container), le modifiche normative (nLPD, GDPR), i risultati degli audit e le lezioni apprese dalle attivazioni dell'accesso d'emergenza e dagli incidenti negli ambienti.

---

# Aree della norma ISO 27001 affrontate

Politica di separazione degli ambienti di sviluppo, test e produzione — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.9 Gestione della configurazione |
| | 8.11 Mascheratura dei dati |
| | 8.25 Ciclo di vita dello sviluppo sicuro |
| | **8.31 Separazione degli ambienti di sviluppo, test e produzione** |
| | 8.32 Gestione delle modifiche |
| | 8.33 Informazioni di test |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la protezione dei dati; separazione degli ambienti come misura tecnica; divieto di dati personali di produzione in ambienti non di produzione senza controlli equivalenti |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati; controlli degli accessi agli ambienti come misura di sicurezza |
| GDPR UE (ove applicabile) | Art. 25 — Protezione dei dati fin dalla progettazione e per impostazione predefinita (separazione degli ambienti); Art. 32 — Sicurezza del trattamento (controllo degli accessi per ambiente) |
| ISO/IEC 27001:2022 | Controllo Annex A 8.31 — Separazione degli ambienti di sviluppo, test e produzione |
| ISO/IEC 27002:2022 | Sezione 8.31 — Linee guida di implementazione per la separazione degli ambienti |
| NIST SP 800-53 Rev 5 | CM-4 (Analisi dell'impatto), CM-7 (Funzionalità minima), SA-11 (Test e valutazione da parte degli sviluppatori), SC-32 (Partizionamento del sistema) |
| CIS Controls v8 | 4.1 (Configurazione sicura degli asset aziendali), 16.1–16.4 (Sicurezza del software applicativo) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
