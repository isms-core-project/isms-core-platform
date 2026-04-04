<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.15-IT:operational:OP-POL:a.8.15 -->
**ISMS-OP-POL-A.8.15 — Registrazione degli eventi**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Registrazione degli eventi |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.15 |
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
|----------|------|--------|-----------|
| 1.0 | [Data] | RSSI | Politica operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.15 — Registrazione degli eventi
- Vedere anche: ISMS-OP-POL-A.8.16 (Attività di monitoraggio), ISMS-OP-POL-A.8.17 (Sincronizzazione dell'orologio)

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con la registrazione degli eventi |
|-----------|---------------------------------------------|
| A.5.7 Intelligence sulle minacce | L'intelligence sulle minacce informa le regole di monitoraggio e i pattern di rilevamento |
| A.5.15–18 Controllo degli accessi e gestione delle identità | Gli eventi di autenticazione e accesso sono le principali fonti di log |
| A.5.24–28 Gestione degli incidenti | L'analisi dei log supporta il rilevamento, l'indagine e la raccolta di prove degli incidenti |
| A.5.28 Raccolta delle prove | I log costituiscono prove forensi; l'integrità deve essere preservata |
| A.5.34 Privacy e protezione dei dati personali | Il monitoraggio dei dipendenti deve essere conforme ai requisiti sulla privacy |
| A.8.1 Dispositivi endpoint degli utenti | Gli eventi endpoint vengono registrati per il monitoraggio della sicurezza |
| A.8.7 Protezione contro il malware | Gli eventi di rilevamento del malware vengono registrati e inoltrati |
| A.8.8 Gestione delle vulnerabilità tecniche | I risultati delle scansioni delle vulnerabilità vengono registrati |
| A.8.20 Sicurezza della rete | Il traffico di rete e gli eventi di sicurezza vengono registrati |

**Politiche interne correlate**:

- Politica di controllo degli accessi
- Politica di gestione degli incidenti
- Politica sulla privacy e protezione dei dati personali
- Politica di sicurezza della rete
- Politica di sicurezza degli endpoint
- Politica di classificazione e gestione delle informazioni

---

# Politica di registrazione degli eventi

## Scopo

Lo scopo di questa politica è affrontare l'identificazione e la gestione degli eventi di sicurezza attraverso la registrazione dei sistemi di elaborazione delle informazioni. I log forniscono la traccia delle prove per il rilevamento degli incidenti, le indagini, la verifica della conformità e l'analisi forense.

Questa politica supporta la nLPD svizzera (revDSG) e l'Ordinanza sulla protezione dei dati (OPDo) implementando la registrazione come misura tecnica e organizzativa adeguata al rischio, inclusi gli obblighi specifici di registrazione ai sensi dell'OPDo Art. 4 per il trattamento di dati personali degni di particolare protezione. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR. Per le attività di monitoraggio, vedere ISMS-OP-POL-A.8.16. Per la sincronizzazione dell'orologio, vedere ISMS-OP-POL-A.8.17.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i dispositivi, i sistemi e le applicazioni utilizzati per trattare, memorizzare o trasmettere informazioni dell'organizzazione rientranti nell'ambito definito dalla dichiarazione di ambito ISO 27001.

## Principio

Tutti i sistemi che trattano, memorizzano o trasmettono informazioni riservate o dati personali devono avere la registrazione abilitata laddove la registrazione sia possibile e praticabile. I log devono essere raccolti centralmente, protetti dalla manomissione, conservati per un periodo definito e revisionati regolarmente per rilevare gli eventi di sicurezza.

---

## Registrazione degli eventi

### Eventi da registrare

I registri degli eventi che documentano le attività degli utenti, le eccezioni, gli errori e gli eventi di sicurezza delle informazioni DEVONO essere prodotti, conservati e revisionati regolarmente. I seguenti eventi DEVONO essere registrati:

| N. | Categoria di evento | Dettagli |
|----|---------------------|----------|
| 1 | **Eventi di autenticazione** | Tentativi di accesso e di disconnessione riusciti e respinti, incluso l'accesso remoto (VPN, applicazioni web) |
| 2 | **Accesso a dati e risorse** | Tentativi riusciti e respinti di accedere a file, database, applicazioni e risorse di rete |
| 3 | **Modifiche alla configurazione del sistema** | Modifiche alle impostazioni di sistema, ai parametri di sicurezza, alla configurazione di rete e alle regole del firewall |
| 4 | **Utilizzo di privilegi elevati** | Tutte le azioni eseguite con accesso amministrativo, root o sudo |
| 5 | **Utilità di sistema e applicazioni** | Utilizzo di programmi di utilità privilegiati, strumenti di manutenzione e utilità diagnostiche |
| 6 | **Operazioni sui file** | Creazione, modifica, eliminazione e migrazione di file sui sistemi critici |
| 7 | **Allarmi del controllo degli accessi** | Blocchi dell'account, violazioni delle soglie e avvisi del sistema di rilevamento delle intrusioni |
| 8 | **Modifiche ai sistemi di sicurezza** | Attivazione, disattivazione o modifica di antivirus, firewall, IDS/IPS e altri sistemi di protezione |
| 9 | **Gestione delle identità** | Creazione, modifica, eliminazione e disabilitazione di account utente e autorizzazioni |
| 10 | **Transazioni applicative** | Transazioni eseguite dagli utenti nelle applicazioni business-critical (sistemi finanziari, HR, CRM) |

### Contenuto delle voci di registro

Ogni voce di registro DEVE includere, come minimo:

| Campo | Descrizione |
|-------|-------------|
| **ID utente/account** | L'account che ha eseguito l'azione |
| **Timestamp** | Data e ora in formato ISO 8601, sincronizzate con la fonte oraria di riferimento dell'organizzazione |
| **Tipo di evento** | Descrizione di ciò che è accaduto (accesso, accesso a file, modifica della configurazione, ecc.) |
| **Esito** | Se l'azione è riuscita o è stata respinta |
| **ID sistema/dispositivo** | Nome host, ID asset o indirizzo IP del sistema in cui si è verificato l'evento |
| **Indirizzo sorgente** | Indirizzo IP sorgente o posizione di rete (ove applicabile) |

---

## Controllo degli accessi ai registri degli eventi

La registrazione degli eventi e il monitoraggio DEVONO essere eseguiti esclusivamente da personale autorizzato.

I registri degli eventi e i sistemi di monitoraggio DEVONO essere protetti e l'accesso limitato in conformità con la Politica di controllo degli accessi. L'accesso ai log grezzi deve essere limitato al team di gestione della sicurezza delle informazioni e al personale IT autorizzato.

Gli amministratori di sistema NON devono avere l'autorizzazione di cancellare o disattivare i log delle proprie attività. Laddove ciò non sia tecnicamente applicabile, DEVONO essere implementati controlli compensativi (ad es. inoltro dei log verso un sistema centralizzato al di fuori del controllo dell'amministratore, revisione periodica delle attività dell'amministratore da parte di un ruolo separato).

---

## Protezione delle informazioni dei registri degli eventi

Le strutture di registrazione e le informazioni dei log DEVONO essere protette dalla manomissione e dall'accesso non autorizzato.

I controlli DEVONO proteggere contro:

- **Alterazione** delle voci di registro registrate o dei tipi di messaggio.
- **Eliminazione** dei file di log o delle singole voci.
- **Esaurimento dello spazio di archiviazione** che causa la perdita di dati di log (i log devono fallire in modalità aperta — generare un avviso quando l'archiviazione raggiunge l'**80% della capacità** anziché sovrascrivere silenziosamente). La capacità di archiviazione dei log deve essere monitorata continuamente, con avvisi automatici alle soglie dell'80% e del 90%. Quando viene raggiunta la capacità del 90%, i log archiviati devono essere scaricati nell'archiviazione a lungo termine e il team della piattaforma deve valutare se è necessaria capacità aggiuntiva.
- **Accesso non autorizzato** ai dati di log (i log possono contenere dati personali e sono classificati come minimo come Interni).

La protezione dei log DEVE essere ottenuta tramite:

- Inoltro dei log verso un **sistema di registrazione centralizzato** separato dai sistemi sorgente.
- Archiviazione **solo in aggiunta** (append-only) o **a scrittura singola** (write-once) per i dati di log laddove tecnicamente fattibile.
- **Controlli di integrità crittografici** (hashing) per rilevare manomissioni laddove richiesto per scopi forensi o legali.
- **Controlli di accesso** che limitano la modifica dei log al solo personale di sicurezza autorizzato.

---

## Registrazione centralizzata

### Piattaforma di registrazione centralizzata

La piattaforma di registrazione centralizzata DEVE soddisfare i seguenti requisiti:

| Requisito | Specifica |
|-----------|-----------|
| **Tipo di piattaforma** | SIEM, aggregatore di log o equivalente (ad es. Splunk, Microsoft Sentinel, Elastic SIEM, Wazuh o equivalente) |
| **Distribuzione** | Separata dai sistemi sorgente; gli amministratori dei sistemi sorgente non devono avere accesso amministrativo |
| **Archiviazione** | Capacità sufficiente per i periodi di conservazione definiti; soglia di avviso all'80% della capacità |
| **Ricerca** | Capacità di query full-text e strutturate per l'indagine sugli incidenti e le query di conformità |
| **Avvisi** | Regole configurabili con notifica al team di gestione della sicurezza delle informazioni (e-mail, SMS, sistema di ticketing) |
| **Integrità** | Archiviazione solo in aggiunta o a scrittura singola; controlli di integrità crittografici ove richiesti |
| **Controllo degli accessi** | Accesso basato sui ruoli; sola lettura per gli analisti; accesso amministrativo limitato agli amministratori della piattaforma |

I log di tutti i sistemi critici DEVONO essere inoltrati alla piattaforma di registrazione centralizzata. La piattaforma DEVE essere:

- **Separata** dai sistemi che generano i log (gli amministratori dei sistemi sorgente non devono avere accesso amministrativo all'archivio log centralizzato).
- **Ricercabile** per supportare le indagini sugli incidenti e le query di conformità.
- **Con capacità di avviso** per notificare al team di gestione della sicurezza delle informazioni gli eventi ad alto rischio.
- **Protetta** con gli stessi o superiori controlli di sicurezza dei sistemi sorgente.

Sistemi da includere nella registrazione centralizzata come minimo:

- Sistemi di autenticazione e di identità (Active Directory, provider di identità, SSO).
- Firewall e dispositivi di sicurezza della rete.
- Server che ospitano dati riservati o dati personali.
- Gateway di posta elettronica e web.
- Sistemi VPN e di accesso remoto.
- Sistemi EDR (Endpoint Detection and Response).
- Console di amministrazione dei servizi cloud (Microsoft 365, AWS, Azure, ecc.).

Laddove la registrazione centralizzata automatizzata non sia fattibile per un sistema specifico, DEVONO essere eseguite la raccolta e la revisione manuale dei log a una frequenza definita con giustificazione documentata.

---

## Log degli amministratori e degli operatori

Le attività degli amministratori di sistema e degli operatori di sistema DEVONO essere registrate, e i log protetti e revisionati regolarmente.

I titolari di account privilegiati possono essere in grado di manipolare i log sui sistemi sotto il loro diretto controllo. Per mantenere la responsabilità per gli utenti privilegiati:

- Le azioni degli amministratori DEVONO essere inoltrate al sistema di registrazione centralizzato in tempo reale o quasi in tempo reale.
- DEVE essere condotta una revisione periodica dell'attività degli utenti privilegiati (almeno trimestralmente).
- Le attività privilegiate anomale (ad es. accesso fuori orario, operazioni sui dati in blocco, modifiche alla configurazione della sicurezza) DEVONO generare avvisi.

---

## Sincronizzazione dell'orologio

I timestamp dei log DEVONO essere accurati e coerenti su tutti i sistemi. I requisiti di sincronizzazione dell'orologio sono definiti in **ISMS-OP-POL-A.8.17 — Sincronizzazione dell'orologio**. Tutti i sistemi che generano dati di log DEVONO conformarsi ai requisiti di fonte oraria e tolleranza alla deriva di A.8.17.

---

## Revisione dei registri degli eventi

### Requisiti di revisione

DEVONO essere assegnate responsabilità per l'analisi e il monitoraggio degli eventi di sicurezza.

| Tipo di revisione | Frequenza | Responsabile | Ambito |
|-------------------|-----------|--------------|--------|
| **Avvisi automatici** | In tempo reale | Sicurezza delle informazioni | Gli eventi ad alto rischio attivano una notifica immediata al team di gestione della sicurezza delle informazioni |
| **Revisione degli eventi di sicurezza** | Settimanale | Analista della sicurezza delle informazioni | Tutti gli eventi di sicurezza, errori di autenticazione, anomalie di accesso |
| **Revisione dell'attività privilegiata** | Trimestrale | RSSI / Responsabile della sicurezza delle informazioni | Azioni degli amministratori e degli operatori, escalation dei privilegi |
| **Revisione completa dei log** | Mensile | Sicurezza delle informazioni | Tendenze, pattern e anomalie su tutte le fonti di log |
| **Audit della copertura delle fonti di log** | Trimestrale | IT Operations | Verificare che tutti i sistemi nell'ambito stiano inoltrando i log; identificare le lacune |

### Eventi ad alto rischio

I seguenti eventi DEVONO attivare avvisi automatici immediati ed essere escalati al processo di gestione degli incidenti:

| N. | Evento ad alto rischio | Soglia di avviso | Risposta |
|----|------------------------|------------------|----------|
| 1 | Multipli tentativi di autenticazione falliti | **5 fallimenti** entro 10 minuti (account singolo) o **20 fallimenti** entro 10 minuti (account multipli dalla stessa fonte) | Blocco dell'account; indagine sulla fonte |
| 2 | Autenticazione riuscita da posizioni inattese | Accesso da un nuovo paese o intervallo IP non incluso nel profilo di riferimento | Verifica con l'utente; sospendere se non confermato |
| 3 | Disabilitazione o modifica dei controlli di sicurezza | Qualsiasi modifica all'antivirus, alle regole del firewall o alla configurazione della registrazione | Avviso immediato alla sicurezza delle informazioni |
| 4 | Accesso in blocco, download o eliminazione di dati | **>500 file** o **>1 GB** a cui ha acceduto/scaricato un singolo utente entro 1 ora | Indagare; sospendere l'accesso se giustificato |
| 5 | Creazione di nuovi account privilegiati o escalation dei privilegi | Qualsiasi nuovo account admin/root o escalation dei privilegi | Verificare l'autorizzazione rispetto ai record delle modifiche |
| 6 | Rilevamento di malware o tentativi di intrusione | Qualsiasi rilevamento confermato | Processo di gestione degli incidenti |
| 7 | Modifica o eliminazione di file di log | Qualsiasi tentativo | Avviso immediato; indagine forense |

### Escalation degli incidenti dal monitoraggio

Quando viene rilevato un evento ad alto rischio, DEVE essere seguito il seguente processo di escalation:

1. **Avviso**: Avviso automatico generato e inviato al team di gestione della sicurezza delle informazioni.
2. **Triage** (entro **30 minuti** durante l'orario lavorativo; **2 ore** fuori dall'orario lavorativo): L'analista valuta l'avviso, determina se si tratta di un vero positivo, un falso positivo o richiede un'indagine.
3. **Indagine**: Se confermato come potenziale evento di sicurezza, viene creato un record di incidente secondo la Politica di gestione degli incidenti.
4. **Escalation**: Gli incidenti classificati come Alti o Critici vengono escalati immediatamente al RSSI.

---

## Conservazione dei registri degli eventi

| Tipo di log | Online (ricercabile) | Archivio (recuperabile) | Conservazione totale |
|-------------|---------------------|-------------------------|----------------------|
| Eventi di sicurezza (autenticazione, controllo degli accessi) | 90 giorni | 9 mesi | **12 mesi** |
| Log di sistema e infrastruttura | 90 giorni | 6 mesi | **9 mesi** |
| Log applicativi | 90 giorni | 6 mesi | **9 mesi** |
| Log del firewall e della sicurezza della rete | 90 giorni | 9 mesi | **12 mesi** |
| Log del trattamento di dati personali degni di particolare protezione (OPDo Art. 4) | 90 giorni | 9 mesi | **12 mesi** (minimo per OPDo) |
| Log del sistema finanziario | 90 giorni | Per la conservazione legale | **Ai sensi del CO svizzero Art. 958f** |

**Motivazione della conservazione**: I log degli eventi di sicurezza e del firewall vengono conservati per 12 mesi per supportare le indagini sugli incidenti (il tempo medio di permanenza per le minacce avanzate è di 10-21 giorni e le indagini normative possono durare 12 mesi). I log di sistema e applicativi vengono conservati per 9 mesi per bilanciare l'utilità operativa con i costi di archiviazione. I log dell'OPDo Art. 4 richiedono un minimo di 12 mesi per regolamentazione.

### Archiviazione e recupero dei log

I log archiviati DEVONO essere crittografati, memorizzati in una posizione sicura e recuperabili entro i seguenti tempi:

| Età dell'archivio | Obiettivo di recupero |
|-------------------|-----------------------|
| 0-90 giorni (online) | Immediato (ricercabile nella piattaforma) |
| 91 giorni - 6 mesi | Entro **4 ore** |
| 6-12 mesi | Entro **24 ore** |
| >12 mesi (se conservati per motivi legali/normativi) | Entro **5 giorni lavorativi** |

Le procedure di recupero DEVONO essere testate almeno annualmente per verificare che i log archiviati siano accessibili e integri.

I log NON devono essere conservati oltre il necessario. Alla scadenza dei periodi di conservazione, i log DEVONO essere eliminati in modo sicuro in conformità con la Politica di classificazione e gestione delle informazioni.

---

## nLPD svizzera — Obblighi di registrazione ai sensi dell'OPDo Art. 4

Laddove l'organizzazione tratti dati personali degni di particolare protezione (nLPD Art. 5) in modo automatizzato su larga scala o esegua profili ad alto rischio, si applicano i seguenti requisiti di registrazione aggiuntivi ai sensi dell'OPDo Art. 4:

**Operazioni da registrare**: Memorizzazione, modifica, lettura, comunicazione, eliminazione e distruzione di dati personali degni di particolare protezione.

**Contenuto del log**: Identità della persona o del sistema che esegue il trattamento, tipo di trattamento, data e ora.

**Archiviazione dei log**: I log del trattamento dei dati personali degni di particolare protezione DEVONO essere archiviati **separatamente** dal sistema di trattamento, conservati per un minimo di **1 anno** e l'accesso limitato alla verifica della conformità alla sicurezza dei dati e alla garanzia di riservatezza, integrità, disponibilità e tracciabilità.

### Valutazione dell'applicabilità dell'OPDo Art. 4

L'organizzazione DEVE determinare se si applica l'OPDo Art. 4 valutando i seguenti criteri:

| Criterio | Valutazione |
|----------|-------------|
| L'organizzazione tratta **dati personali degni di particolare protezione** (nLPD Art. 5)? | Sì / No |
| Il trattamento è **automatizzato** (non puramente manuale/cartaceo)? | Sì / No |
| Il trattamento è **su larga scala** (volume degli interessati, volume dei dati, ambito geografico)? | Sì / No |
| L'organizzazione esegue **profili ad alto rischio**? | Sì / No |

Se la risposta al primo criterio E a uno qualsiasi dei criteri rimanenti è **Sì**, si applicano gli obblighi di registrazione dell'OPDo Art. 4. Laddove l'organizzazione non sia sicura dell'applicabilità dell'Art. 4, l'implementazione di questi requisiti di registrazione è raccomandata come best practice.

---

## Privacy personale

La privacy dei dipendenti e dei clienti DEVE essere rispettata in conformità con la nLPD svizzera e i requisiti legali applicabili nell'implementazione della registrazione.

### Principi per il monitoraggio dei dipendenti

- I sistemi di registrazione devono servire **scopi legittimi di sicurezza** (rilevare minacce, indagare sugli incidenti, verificare la conformità) — non principalmente per monitorare il comportamento dei dipendenti.
- I dipendenti DEVONO essere **informati in anticipo** che la registrazione ha luogo, cosa viene registrato e perché, attraverso il programma di sensibilizzazione alla sicurezza delle informazioni e la documentazione di impiego.
- Devono essere raccolti e conservati solo i **dati minimi necessari** (minimizzazione dei dati).
- L'accesso ai log contenenti dati dei dipendenti deve essere limitato al personale di sicurezza e conformità autorizzato — non ai responsabili diretti per la consultazione generale.
- Il **keylogging** e la **sorveglianza continua dell'attività individuale** sono sproporzionati e NON devono essere implementati.
- Laddove i log contenenti dati personali vengano condivisi con parti esterne (ad es. fornitori per la risoluzione dei problemi), gli identificatori personali DEVONO essere mascherati o anonimizzati.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione dell'ambito del monitoraggio; punto di escalation per gli avvisi critici; revisione trimestrale dell'attività privilegiata |
| **Analista della sicurezza delle informazioni** | Revisione giornaliera/settimanale dei log; triage degli avvisi; escalation degli incidenti; manutenzione delle regole di rilevamento |
| **IT Operations / Team della piattaforma** | Amministrazione della piattaforma di registrazione; gestione della capacità; onboarding delle fonti di log; configurazione NTP; archiviazione |
| **Amministratori di sistema** | Garantire che la registrazione sia abilitata sui sistemi gestiti; cooperare con l'onboarding delle fonti di log; segnalare i guasti della registrazione |
| **Consulente per la protezione dei dati** | Orientamento sull'applicabilità dell'OPDo Art. 4; impatto sulla privacy delle attività di monitoraggio; requisiti di notifica ai dipendenti |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Configurazione della piattaforma di registrazione centralizzata** e inventario delle fonti di log | IT Operations | *Inventario delle fonti di log revisionato trimestralmente; configurazione documentata* |
| 2 | **Voci di registro campione** che dimostrano che i campi richiesti vengono acquisiti | Sicurezza delle informazioni | *Verificato annualmente durante l'audit; campione di 5 sistemi* |
| 3 | **Controlli di protezione dei log** (restrizioni di accesso, archiviazione solo in aggiunta, controlli di integrità) | IT Operations | *Configurazione revisionata annualmente; log di accesso conservati 12 mesi* |
| 4 | **Conformità alla sincronizzazione dell'orologio** per ISMS-OP-POL-A.8.17 (fonte NTP, monitoraggio della deriva, soglia di avviso) | IT Operations | *Vedere i requisiti di evidenza di ISMS-OP-POL-A.8.17* |
| 5 | **Configurazione della conservazione dei log** corrispondente ai periodi di conservazione definiti | IT Operations | *Verificato semestralmente; recupero archiviazione testato annualmente* |
| 6 | **Registrazioni delle revisioni degli eventi di sicurezza** (revisioni settimanali, revisioni trimestrali dell'attività privilegiata) | Sicurezza delle informazioni | *Log delle revisioni settimanali conservati 12 mesi; revisioni trimestrali presentate alla revisione della direzione* |
| 7 | **Regole di avviso** e notifiche di avviso campione per gli eventi ad alto rischio | Sicurezza delle informazioni | *Regole revisionate trimestralmente; avvisi campione conservati 12 mesi* |
| 8 | **Registrazioni della conformità all'OPDo Art. 4** (valutazione dell'applicabilità; log del trattamento dei dati personali degni di particolare protezione memorizzati separatamente) | Consulente per la protezione dei dati | *Valutazione dell'applicabilità revisionata annualmente; separazione dei log verificata trimestralmente* |
| 9 | **Registrazioni della notifica ai dipendenti** (formazione sulla consapevolezza, informativa sulla privacy riguardo al monitoraggio) | HR / Sicurezza delle informazioni | *Aggiornato per ogni modifica della politica; completamento della formazione monitorato annualmente* |
| 10 | **Metrica della copertura delle fonti di log** (percentuale di sistemi nell'ambito che inoltrano i log) | IT Operations | *Trimestrale; obiettivo: 100% dei sistemi critici, ≥95% di tutti i sistemi nell'ambito* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni DEVE verificare la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, audit della copertura delle fonti di log, controlli della conformità alla conservazione, completamento della revisione dei log, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere riportate al team di revisione della direzione.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti agli standard di registrazione, i requisiti normativi (inclusi gli aggiornamenti dell'OPDo) e le lessons learned dagli incidenti.

---

# Aree dello standard ISO 27001 trattate

Politica di registrazione degli eventi — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 7.3 Consapevolezza | 5.37 Procedure operative documentate |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.15 Registrazione degli eventi** |
| | 8.16 Attività di monitoraggio *(vedere ISMS-OP-POL-A.8.16)* |
| | 8.17 Sincronizzazione dell'orologio *(vedere ISMS-OP-POL-A.8.17)* |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; Art. 6 — Proporzionalità del monitoraggio |
| OPDo svizzero | Art. 4 — Obblighi di registrazione per il trattamento di dati personali degni di particolare protezione |
| CO svizzero | Art. 328b — Limitazioni al trattamento dei dati dei dipendenti; Art. 958f — Conservazione dei registri aziendali |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento (registrazione come misura appropriata) |
| ISO/IEC 27001:2022 | Annex A Controllo 8.15 (vedere anche 8.16, 8.17) |
| ISO/IEC 27002:2022 | Sezione 8.15 — Indicazioni di implementazione |
| NIST SP 800-53 Rev 5 | AU-2 (Event Logging), AU-3 (Content of Audit Records), AU-6 (Audit Review/Analysis), AU-8 (Time Stamps), AU-9 (Protection of Audit Information), AU-11 (Audit Record Retention) |
| NIST SP 800-92 | Guide to Computer Security Log Management |
| CIS Controls v8 | Controllo 8 (Audit Log Management) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
