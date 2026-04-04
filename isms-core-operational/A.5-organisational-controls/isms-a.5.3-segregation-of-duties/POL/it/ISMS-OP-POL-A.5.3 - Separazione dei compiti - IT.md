<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.3-IT:operational:OP-POL:a.5.3 -->
**ISMS-OP-POL-A.5.3 — Separazione dei compiti**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Separazione dei compiti |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.5.3 |
| **Autore del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
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
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.5.3 — Separazione dei compiti
- ISO/IEC 27002:2022 Sezione 5.3 — Guida all'implementazione
- CO svizzero Art. 728a — Sistema di controllo interno
- NIST SP 800-53 Rev 5 AC-5 — Separazione dei compiti

**Controlli Annex A correlati**:

| Controllo | Relazione con la separazione dei compiti |
|-----------|------------------------------------------|
| A.5.1 Politiche per la sicurezza delle informazioni | Quadro normativo generale che disciplina i requisiti di SoD |
| A.5.2 Ruoli e responsabilità per la sicurezza delle informazioni | Definizioni di ruolo che abilitano la separazione dei compiti |
| A.5.15 Controllo degli accessi | Le regole di controllo degli accessi applicano i confini della separazione |
| A.5.16 Gestione delle identità | Le identità univoche garantiscono la responsabilità individuale |
| A.5.18 Diritti di accesso | Il provisioning degli accessi implementa i vincoli di esclusione reciproca |
| A.8.2 Diritti di accesso privilegiato | Gli account privilegiati sono separati dalle operazioni standard |
| A.8.3 Restrizione dell'accesso alle informazioni | Applicazione tecnica delle regole di separazione |
| A.8.5 Autenticazione sicura | L'autenticazione verifica l'identità dell'attore in ogni fase del processo |
| A.8.15 Registrazione | I registri di audit tracciano le attività separate ai fini della verifica |
| A.8.32 Gestione delle modifiche | Il processo di modifica impone la separazione tra sviluppatore/tester/deployer |

**Politiche interne correlate**:

- Politica di gestione delle identità e degli accessi
- Politica di autenticazione e accesso privilegiato
- Politica di gestione delle modifiche
- Politica di registrazione
- Politica di classificazione e gestione delle informazioni

---

# Politica di separazione dei compiti

## Scopo

Lo scopo della presente politica è ridurre il rischio di frodi, errori e aggiramento dei controlli di sicurezza delle informazioni, garantendo che i compiti in conflitto e le aree di responsabilità in conflitto siano separati tra individui o ruoli diversi. La separazione dei compiti impedisce a qualsiasi singola persona di avere il controllo completo end-to-end su un processo critico — dall'avvio all'autorizzazione, dall'esecuzione alla verifica.

La presente politica supporta la nLPD svizzera attuando misure organizzative proporzionate al rischio per proteggere l'integrità del trattamento dei dati personali. La separazione dei compiti è un controllo interno riconosciuto ai sensi del CO svizzero Art. 728a, che impone alle società soggette a revisione ordinaria di mantenere un sistema di controllo interno. Laddove l'organizzazione tratti dati di soggetti nell'UE/SEE, si applicano altresì i requisiti del GDPR.

## Ambito di applicazione

Tutti i dipendenti, i collaboratori e gli utenti terzi coinvolti in processi aziendali in cui compiti in conflitto potrebbero consentire frodi, errori o violazioni della sicurezza se svolti da un singolo individuo.

Ciò include:

- Transazioni finanziarie, approvazioni ed erogazioni.
- Amministrazione, sviluppo e deployment di sistemi informativi.
- Provisioning, revisione e revoca degli accessi.
- Monitoraggio della sicurezza, revisione dei log e risposta agli incidenti.
- Approvvigionamento, gestione dei fornitori e amministrazione dei contratti.
- Operazioni di backup, ripristino e recupero dei dati.

**Escluso dall'ambito**: I processi operativi non sensibili con adeguata supervisione; i processi completamente automatizzati con controlli di separazione integrati (laddove la separazione sia realizzata tramite automazione, la configurazione del controllo e i registri di audit DEVONO essere validati almeno annualmente dal RSSI o da un revisore designato).

## Principio

I compiti in conflitto e le aree di responsabilità in conflitto dovrebbero essere separati. Laddove la piena separazione non sia realizzabile a causa delle dimensioni dell'organizzazione, DEVONO essere attuati controlli compensativi — inclusi monitoraggio rafforzato, revisione da parte del management, audit indipendente e registri di audit a prova di manomissione — e formalmente documentati.

Tutte le decisioni in materia di separazione DEVONO essere basate sul rischio, tenendo conto del valore e della classificazione degli asset coinvolti, del potenziale di perdita finanziaria o danno reputazionale e dei requisiti normativi.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Separazione dei compiti (SoD)** | La pratica di suddividere compiti e privilegi tra più individui per impedire a qualsiasi singola persona di avere il controllo completo su un processo critico |
| **Compiti in conflitto** | Responsabilità che, se combinate in un unico individuo, consentirebbero a tale persona di commettere e occultare errori o frodi senza essere rilevata |
| **Controllo compensativo** | Una misura di controllo alternativa attuata quando non è possibile ottenere la separazione primaria, che fornisce una riduzione del rischio equivalente |
| **Esclusione reciproca** | Un controllo tecnico che impedisce a un utente di essere assegnato a ruoli in conflitto simultaneamente in un sistema di controllo degli accessi |
| **Principio dei quattro occhi** | Il requisito che le azioni critiche richiedano l'approvazione o la verifica di almeno due persone autorizzate prima dell'esecuzione |
| **Matrice SoD** | Una mappatura documentata di ruoli, compiti e conflitti identificati, utilizzata per pianificare e verificare la separazione dei compiti |

---

## Principi di separazione

Tutti i processi aziendali e i sistemi informativi DEVONO attuare la separazione dei compiti laddove:

- Le attività comportano transazioni finanziarie **superiori a CHF 10.000**, salvo che non sia definita una soglia inferiore in una procedura specifica del dipartimento approvata dal CFO e dal RSSI sulla base di una valutazione del rischio.
- È richiesto l'accesso a informazioni riservate o con restrizioni.
- Viene esercitata l'amministrazione di sistemi o l'accesso privilegiato.
- I controlli di sicurezza possono essere aggirati, modificati o disabilitati.
- I registri di audit o le prove di conformità possono essere modificati o cancellati.

**Determinazione della soglia finanziaria**:
- **CHF 10.000** è la soglia di riferimento dell'organizzazione, basata su una valutazione del rischio che considera le dimensioni organizzative, il volume delle transazioni e i precedenti storici di frode.
- Soglie inferiori possono essere definite per categorie ad alto rischio (es. CHF 5.000 per i pagamenti in contanti, CHF 2.000 per i rimborsi spese dei dipendenti) dal CFO e dal RSSI sulla base di una valutazione del rischio specifica per dipartimento.
- Soglie superiori non sono consentite senza l'approvazione della Direzione generale e l'adozione di controlli compensativi.

**Revisione della soglia**: Le soglie finanziarie DEVONO essere riviste annualmente dal CFO e dal RSSI e adeguate in base all'inflazione, alla crescita organizzativa e alla rivalutazione del rischio di frode.

### Standard minimi di separazione

Si applicano i seguenti requisiti minimi di separazione:

| Tipo di processo | Requisito minimo di separazione |
|------------------|---------------------------------|
| **Transazioni finanziarie** >CHF 10.000 | L'iniziatore NON DEVE essere l'approvatore |
| **Richieste di accesso ai sistemi** | Il richiedente NON DEVE essere l'approvatore; l'approvatore NON DEVE essere il provisioner |
| **Gestione delle modifiche** | Lo sviluppatore NON DEVE essere il tester; il tester NON DEVE essere il deployer |
| **Monitoraggio della sicurezza** | L'amministratore di sistema NON DEVE essere il revisore dei log |
| **Backup e ripristino** | L'operatore di backup NON DEVE essere il verificatore del ripristino |

Laddove un individuo detenga attualmente compiti in conflitto, il conflitto DEVE essere risolto entro 30 giorni di calendario dall'identificazione — tramite riassegnazione, esclusione reciproca tecnica o documentazione formale di un controllo compensativo.

---

## Identificazione dei compiti in conflitto

L'organizzazione DEVE mantenere una matrice SoD documentata che identifichi le combinazioni di compiti che richiedono separazione. Le seguenti categorie forniscono la baseline:

### Processi finanziari

Le seguenti combinazioni di compiti DEVONO essere separate:

- Avviare pagamenti E approvare pagamenti.
- Creare anagrafiche fornitori E elaborare pagamenti ai fornitori.
- Registrare transazioni E riconciliare i conti.
- Gestire le buste paga E approvare le erogazioni salariali.
- Preparare il budget E approvare il budget.

### Operazioni IT

Le seguenti combinazioni di compiti DEVONO essere separate:

- Sviluppare codice E effettuare il deployment in produzione.
- Amministrare sistemi E revisionare i log di sistema.
- Creare account utente E approvare le richieste di accesso.
- Gestire i backup E autorizzare il ripristino dei dati.
- Configurare i controlli di sicurezza E verificare l'efficacia della sicurezza.
- Gestire le regole del firewall E revisionare la conformità del firewall.

### Approvvigionamento e contratti

Le seguenti combinazioni di compiti DEVONO essere separate:

- Selezionare i fornitori E negoziare i contratti.
- Approvare gli acquisti E ricevere beni o servizi.
- Gestire i contratti E verificare la conformità contrattuale.

### Risorse umane

Le seguenti combinazioni di compiti DEVONO essere separate:

- Decisioni di assunzione E verifica dei controlli sui precedenti.
- Fissare la retribuzione E approvare le buste paga.
- Revocare gli accessi E confermare la revoca degli accessi.

I responsabili di dipartimento DEVONO revisionare annualmente la matrice SoD per la propria area e segnalare eventuali nuovi conflitti identificati al RSSI. Il RSSI DEVE mantenere la matrice SoD organizzativa consolidata in [Strumento GRC] o nel registro equivalente.

> **Ubicazione della matrice SoD**: [Specificare: modulo GRC ServiceNow, Archer, MetricStream, registro SharePoint, oppure "In fase di selezione; in via transitoria: registro Excel in spazio di archiviazione condiviso controllato"]
>
> **Ubicazione del registro delle eccezioni**: [Stesso sistema della matrice SoD o specificare separatamente]
>
> Laddove non sia ancora disponibile uno strumento GRC dedicato, l'organizzazione DEVE mantenere i registri in un archivio condiviso controllato con controllo delle versioni, registrazione degli accessi e verifica trimestrale dell'integrità da parte del RSSI.

---

## Controlli compensativi per piccoli team e PMI

Laddove la separazione non possa essere pienamente realizzata a causa del numero limitato di personale — situazione comune nelle piccole e medie organizzazioni — DEVONO essere attuati controlli compensativi per fornire una mitigazione del rischio equivalente.

### Controlli compensativi obbligatori

Quando la piena separazione dei compiti non è fattibile, DEVONO essere attuati **tutti e cinque** i seguenti controlli compensativi per ogni conflitto identificato:

| # | Controllo compensativo | Implementazione |
|---|------------------------|-----------------|
| 1 | **Monitoraggio e registrazione rafforzati** | Tutte le attività nel processo in conflitto DEVONO essere registrate con registri di audit immutabili. I log DEVONO acquisire l'identità dell'utente, l'azione, il timestamp e i record interessati |
| 2 | **Revisione delle transazioni da parte del management** | Un manager o un collega senior non coinvolto nel processo DEVE revisionare tutte le transazioni con cadenza settimanale come minimo |
| 3 | **Revisione indipendente periodica** | Una parte indipendente (revisione interna, revisore esterno o alta direzione) DEVE revisionare il processo con cadenza trimestrale come minimo |
| 4 | **Avvisi automatici per anomalie** | Il [SIEM] o il sistema di monitoraggio equivalente DEVE generare avvisi per pattern insoliti, quali transazioni al di fuori degli orari normali, importi che superano le soglie o operazioni in blocco |
| 5 | **Registro delle transazioni post-hoc con protezione antimanomissione** | I record delle transazioni DEVONO essere archiviati in modo tale da impedirne la modifica o la cancellazione da parte dell'individuo che ha eseguito la transazione |

### Ambito della revisione indipendente periodica (Controllo compensativo n. 3)

Una parte indipendente DEVE revisionare il processo **trimestralmente** come minimo. La revisione DEVE includere:

**Ambito della revisione**:
- **Campione di transazioni** (minimo 10% del volume di transazioni o 20 transazioni, a seconda di quale sia il valore maggiore).
- **Verifica del registro di audit** (confermare che tutte le attività siano registrate; i log siano immutabili).
- **Completamento della revisione da parte del management** (verificare che le revisioni settimanali del management siano avvenute con approvazione documentata).
- **Rilevamento delle anomalie** (verificare che gli avvisi automatici funzionino; revisionare gli avvisi attivati e la relativa risoluzione).
- **Conformità al processo** (confermare che il processo sia stato seguito come documentato).

**Documentazione della revisione**: Ogni revisione trimestrale DEVE produrre un rapporto scritto che documenti l'ambito, i risultati, i problemi identificati e le raccomandazioni. I rapporti DEVONO essere conservati per 3 anni.

**Escalation dei problemi**: I problemi identificati durante la revisione indipendente DEVONO essere segnalati al RSSI entro 5 giorni lavorativi e risolti entro 30 giorni di calendario.

### Requisito di documentazione

Ogni accordo di controllo compensativo DEVE essere formalmente documentato con:

- I compiti in conflitto specifici che non possono essere separati.
- La giustificazione aziendale per l'impossibilità di separare.
- I controlli compensativi in vigore (tutti e cinque quelli sopra indicati).
- L'accettazione formale del rischio firmata dalla Direzione generale.
- Un calendario di revisione definito (trimestrale come minimo).

La documentazione dei controlli compensativi DEVE essere conservata in [Strumento GRC] o in un registro equivalente accessibile al RSSI e alla Revisione interna.

### Trigger per la rivalutazione

Gli accordi di controllo compensativo DEVONO essere rivalutati quando:

- Vengono assunti ulteriori dipendenti che potrebbero assumere compiti separati.
- La struttura organizzativa cambia.
- La valutazione del rischio identifica un'esposizione maggiore.
- I risultati dell'audit indicano carenze nei controlli.
- Si verifica un incidente di sicurezza relativo all'area del controllo compensativo.

### Verifica dell'efficacia dei controlli compensativi

L'efficacia dei controlli compensativi DEVE essere verificata attraverso:

**Revisione indipendente trimestrale** (Controllo compensativo n. 3):
- Verificare che tutti e cinque i controlli compensativi funzionino come documentato.
- Campionare le transazioni per confermare l'integrità del registro di audit.
- Confermare il completamento della revisione da parte del management con approvazione documentata.
- Testare la configurazione degli avvisi automatici e la relativa risposta.

**Valutazione annuale dell'efficacia** da parte del RSSI:
- Revisionare tutti gli accordi di controllo compensativo.
- Valutare se i controlli mitighino adeguatamente il rischio di separazione.
- Identificare opportunità per realizzare la piena separazione (es. un nuovo assunto può assumere il compito separato).
- Aggiornare la documentazione di accettazione del rischio.

**Fallimento del controllo compensativo**: Se un controllo compensativo risulta inefficace, è necessaria la notifica immediata alla Direzione generale e la remediation entro 14 giorni di calendario, oppure la ri-accettazione formale del rischio residuo.

---

## Controlli tecnici di separazione

I sistemi informativi che supportano i processi separati DEVONO implementare i seguenti controlli tecnici:

> **Sistema di registrazione e monitoraggio**: [Specificare: Splunk, Elastic SIEM, Azure Sentinel, oppure "Selezione in corso; in via transitoria: registrazione centralizzata su server syslog con revisione manuale"]
>
> **Identity provider**: [Specificare: Azure AD, Okta, Google Workspace, oppure "Active Directory on-premises"]
>
> **ERP/Sistema finanziario**: [Specificare: SAP, Oracle, NetSuite, o il sistema applicabile]
>
> Laddove i sistemi siano in fase di selezione o transizione, documentare l'approccio transitorio e la data di deployment target.

### Applicazione del controllo degli accessi

- **Controllo degli accessi basato sui ruoli (RBAC)**: I ruoli DEVONO essere definiti nell'identity provider o nell'applicazione per applicare la separazione dei compiti. I ruoli in conflitto DEVONO essere documentati come reciprocamente esclusivi.
- **Vincoli di esclusione reciproca**: Il sistema di controllo degli accessi ([Identity Provider / ERP / Sistema HR]) DEVE impedire a un singolo utente di detenere ruoli in conflitto simultaneamente. Laddove il sistema non supporti nativamente l'esclusione reciproca, DEVE essere effettuata una revisione manuale ad ogni evento di provisioning degli accessi.
- **Controlli del flusso di lavoro**: I processi aziendali multifase DEVONO richiedere individui autorizzati diversi in ogni fase di approvazione. L'auto-approvazione DEVE essere bloccata tecnicamente ove possibile ed è vietata dalla politica in tutti i casi.
- **Gestione degli accessi privilegiati**: Gli account privilegiati DEVONO essere separati dagli account standard. Nessun individuo DEVE approvare le proprie richieste di accesso elevato.

**Verifica dei vincoli di esclusione reciproca**:
- **Sistemi automatizzati**: I vincoli di esclusione reciproca DEVONO essere testati **annualmente** tentando di assegnare ruoli in conflitto a un utente di test e verificando che il sistema blocchi l'assegnazione. I risultati del test DEVONO essere documentati.
- **Sistemi a revisione manuale**: Le checklist di provisioning degli accessi DEVONO includere la verifica dei conflitti SoD con conferma documentata prima della concessione dell'accesso. Il provisioner DEVE consultare la matrice SoD e confermare l'assenza di conflitti.
- **Revisione trimestrale degli accessi**: Tutte le assegnazioni di ruolo degli utenti DEVONO essere confrontate con la matrice SoD per rilevare eventuali conflitti che abbiano aggirato i controlli di provisioning. I risultati DEVONO essere risolti entro 30 giorni di calendario.

### Requisiti del registro di audit

- **Registrazione immutabile**: Tutte le attività nei processi separati DEVONO essere registrate su una piattaforma di logging centralizzata ([SIEM] o equivalente) che i partecipanti al processo non possono modificare o cancellare.
- **Identificazione dell'attore**: I log DEVONO identificare chiaramente l'individuo che esegue ogni azione in ogni fase del processo.
- **Registrazione di timestamp e azioni**: Tutte le approvazioni, modifiche e completamenti di processo DEVONO essere registrati con timestamp accurati.
- **Protezione dei log**: I registri di audit DEVONO essere protetti da modifiche o cancellazioni ai sensi della Politica di registrazione. Le implementazioni accettabili includono lo storage in sola scrittura, l'accesso amministrativo ristretto con revisore dei log separato, i blocchi di conservazione o l'aggregazione centralizzata dei log con verifica dell'integrità.

---

## Gestione delle eccezioni

Le eccezioni ai requisiti di separazione DEVONO essere gestite attraverso un processo formale. L'auto-approvazione delle eccezioni di separazione non è mai consentita.

### Eccezioni di emergenza (durata pari o inferiore a 24 ore)

Quando l'urgenza operativa richiede di bypassare temporaneamente i controlli di separazione:

1. **Autorizzazione verbale** dal Responsabile di dipartimento e dal RSSI (o delegato del RSSI) — registrare chi ha autorizzato, quando e la specifica eccezione concessa.
2. **Documentazione entro 4 ore** dall'utilizzo dell'eccezione tramite [modulo di eccezione di emergenza / sistema di ticketing / e-mail al RSSI] includendo:
   - ID eccezione (identificatore univoco).
   - Nome e ruolo del richiedente.
   - Autorizzatori verbali (nomi, orario dell'autorizzazione).
   - Giustificazione aziendale (specifica urgenza operativa).
   - Eccezione concessa (compiti specifici combinati; durata).
   - Azioni intraprese durante il periodo di eccezione.
   - Controlli compensativi attivi (monitoraggio rafforzato, revisione post-hoc immediata).
3. **Revisione completa entro 24 ore** dalla fine dell'eccezione — il RSSI o delegato DEVE verificare che i controlli compensativi siano stati efficaci e che non si siano verificate irregolarità. L'approvazione della revisione DEVE essere documentata.
4. **Controlli compensativi attivi** durante il periodo di eccezione — monitoraggio rafforzato e revisione post-attività come minimo.

**Registro delle eccezioni di emergenza**: Tutte le eccezioni di emergenza DEVONO essere registrate nel Registro delle eccezioni con flag "Emergenza".

### Eccezioni pianificate (durata superiore a 24 ore)

Quando è richiesta un'eccezione a lungo termine (es. assenza di personale, vincoli di progetto):

1. **Richiesta di eccezione formale** presentata al RSSI con giustificazione aziendale.
2. **Valutazione del rischio** dell'impatto dell'eccezione sulla prevenzione di frodi ed errori.
3. **Controlli compensativi** documentati e approvati prima che l'eccezione entri in vigore.
4. **Approvazione del RSSI e della Direzione generale** — entrambe obbligatorie.
5. **Durata massima**: 90 giorni di calendario. Il rinnovo richiede una nuova valutazione e una nuova approvazione.

### Non ammissibile

Le seguenti eccezioni NON DEVONO essere concesse in nessuna circostanza:

- Eccezioni permanenti ai requisiti di separazione finanziaria.
- Eccezioni che eliminano o aggirano le capacità di registro di audit.
- Auto-approvazione della propria eccezione di separazione.

### Registro delle eccezioni

Tutte le eccezioni DEVONO essere registrate nel Registro delle eccezioni conservato in [Strumento GRC] o equivalente. Ogni record DEVE includere:

- Sistema/i e processo/i interessati.
- Identità e ruolo/i cui è stata concessa l'eccezione.
- Finestra temporale (data di inizio e data di fine).
- Autorità approvante con evidenza dell'approvazione.
- Controlli compensativi attivi durante l'eccezione.
- Esito della revisione post-eccezione.
- Data di chiusura.

Il RSSI DEVE revisionare il Registro delle eccezioni mensilmente e riferire le eccezioni attive alla Direzione generale con cadenza trimestrale.

---

## Manutenzione della matrice SoD

### Revisione annuale

La matrice SoD organizzativa DEVE essere revisionata e aggiornata annualmente. La revisione DEVE:

- Confermare che tutti i conflitti documentati rimangano validi e completi.
- Identificare nuovi conflitti derivanti da cambiamenti organizzativi, nuovi sistemi o nuovi processi.
- Verificare che i controlli compensativi rimangano efficaci per i conflitti non risolti.
- Aggiornare la matrice per riflettere la struttura organizzativa attuale.

### Verifica trimestrale dei diritti di accesso

Le Operazioni IT DEVONO generare trimestralmente report degli accessi dall'identity provider e dai sistemi di accesso alle applicazioni. Il RSSI DEVE confrontare questi report con la matrice SoD per verificare:

- Che nessun individuo detenga ruoli in conflitto nei sistemi di produzione.
- Che i vincoli di esclusione reciproca funzionino correttamente.
- Che le nuove assegnazioni di ruolo dall'ultima revisione non creino conflitti non documentati.

I risultati DEVONO essere documentati e i conflitti risolti entro 30 giorni di calendario dalla scoperta.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità relative alla separazione dei compiti |
|-------|------------------------------------------------------|
| **Direzione generale** | Approvare la politica di separazione; accettare i rischi residui; approvare i controlli compensativi; approvare le eccezioni pianificate |
| **RSSI** | Definire e mantenere la matrice SoD; monitorare la conformità; approvare le eccezioni di emergenza e pianificate; revisionare il Registro delle eccezioni mensilmente |
| **CFO** | Supervisionare la separazione dei processi finanziari; approvare le eccezioni ai controlli finanziari congiuntamente al RSSI; definire gli adeguamenti delle soglie finanziarie |
| **Responsabili di dipartimento** | Attuare la separazione all'interno dei dipartimenti; identificare nuovi conflitti; richiedere eccezioni; garantire la revisione settimanale del management nelle aree di controllo compensativo |
| **Risorse umane** | Mantenere la struttura organizzativa che supporta la separazione; notificare alle Operazioni IT i cambiamenti di ruolo che influenzano le assegnazioni dei compiti |
| **Operazioni IT** | Implementare i controlli tecnici (RBAC, esclusione reciproca, flusso di lavoro); generare report trimestrali sugli accessi; mantenere i registri di audit |
| **Revisione interna** | Verificare l'efficacia della separazione; valutare l'adeguatezza dei controlli compensativi; segnalare le violazioni; condurre le revisioni indipendenti trimestrali |

### Percorso di escalation

- **Conflitti di separazione identificati**: Il Responsabile di dipartimento notifica il RSSI. Il RSSI sottopone alla Direzione generale se la risoluzione richiede un cambiamento organizzativo.
- **Richieste di eccezione**: Il richiedente presenta al Responsabile di dipartimento. Il Responsabile di dipartimento presenta al RSSI. Il RSSI ottiene l'approvazione della Direzione generale per le eccezioni pianificate.
- **Violazione rilevata**: Notifica immediata al RSSI e alla Revisione interna. Indagine avviata entro 24 ore.

### Processo di indagine sulle violazioni

Quando viene rilevata una violazione della separazione:

1. **Notifica immediata** al RSSI e alla Revisione interna (entro 4 ore dal rilevamento).
2. **Indagine avviata** entro 24 ore dalla Revisione interna o dall'investigatore designato dal RSSI.
3. **Ambito dell'indagine**:
   - Determinare se la violazione sia stata involontaria (configurazione errata del sistema, errore di provisioning degli accessi) o intenzionale.
   - Revisionare tutte le transazioni eseguite durante il periodo di violazione.
   - Valutare se si siano verificate frodi o errori.
   - Identificare la causa principale (errore di processo, lacuna formativa, aggiramento intenzionale).
4. **Tempistiche dell'indagine**: Completare entro 10 giorni lavorativi per le violazioni amministrative; entro 5 giorni lavorativi per i sospetti di frode.
5. **Remediation**: Revoca immediata degli accessi se la violazione è in corso; piano di azione correttiva entro 14 giorni di calendario.
6. **Reportistica**: Rapporto di indagine al RSSI, al CFO e alla Direzione generale (per violazioni finanziarie o sospetti di frode).

**Azione disciplinare**: Ai sensi della sezione Non conformità della presente politica e delle procedure disciplinari dell'organizzazione.

---

## Formazione e sensibilizzazione

**Formazione annuale sulla SoD** DEVE essere erogata a tutti i dipendenti e comprendere:
- Scopo della separazione dei compiti (prevenzione di frodi ed errori).
- Esempi di compiti in conflitto (finanziari, IT, approvvigionamento).
- Responsabilità individuali (non approvare il proprio lavoro, segnalare i conflitti).
- Processo delle eccezioni (come richiedere correttamente le eccezioni).
- Conseguenze delle violazioni della SoD (azione disciplinare, potenziali implicazioni di frode).

**Formazione specifica per ruolo**:
- **Responsabili di dipartimento**: Procedure di revisione settimanale del management per le aree di controllo compensativo; come identificare nuovi conflitti.
- **Operazioni IT**: Configurazione RBAC, implementazione dell'esclusione reciproca, protezione dei registri di audit.
- **Team Finance**: Requisiti di separazione finanziaria, conformità del flusso di lavoro approvativo.

Il completamento della formazione DEVE essere tracciato; obiettivo: **100% dei dipendenti con responsabilità di separazione formati annualmente**.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità alla presente politica:

| # | Evidenza | Proprietario | Frequenza |
|---|----------|--------------|-----------|
| 1 | **Matrice SoD** che documenta tutte le combinazioni di compiti in conflitto identificate e lo stato di separazione | RSSI | *Revisionata annualmente; aggiornata al verificarsi di cambiamenti organizzativi* |
| 2 | **Report sui diritti di accesso** che mostrano le assegnazioni di ruolo nei sistemi, verificate rispetto alla matrice SoD | Operazioni IT | *Generati trimestralmente; revisionati dal RSSI* |
| 3 | **Registro dei controlli compensativi** con approvazione dell'accettazione del rischio da parte della Direzione generale | RSSI | *Revisionato trimestralmente; aggiornato al verificarsi di eventi trigger* |
| 4 | **Registro delle eccezioni** con evidenze di approvazione, controlli compensativi e record di chiusura | RSSI | *Revisionato mensilmente; riferito trimestralmente alla Direzione generale* |
| 5 | **Verbali di revisione del management** per le aree di controllo compensativo (revisioni settimanali delle transazioni) | Responsabili di dipartimento | *Settimanali; conservati per 3 anni* |
| 6 | **Rapporti di revisione indipendente** per le aree in cui la separazione non è realizzabile | Revisione interna | *Trimestrali; conservati per 3 anni* |
| 7 | **Evidenze di configurazione RBAC** che mostrano i vincoli di esclusione reciproca nei sistemi di controllo degli accessi | Operazioni IT | *Acquisite annualmente o in caso di modifica; conservate per 3 anni* |
| 8 | **Verbali di approvazione del flusso di lavoro** che mostrano il controllo multipartitico per le transazioni finanziarie e le modifiche ai sistemi | Operazioni IT | *Per transazione; conservati secondo il piano di conservazione* |
| 9 | **Verbali di verifica dell'integrità dei log di audit** per la registrazione dei processi separati | Operazioni IT | *Mensili; conservati per 3 anni* |
| 10 | **Approvazione della revisione annuale della matrice SoD** e matrice aggiornata | RSSI | *Annuale; conservata per 3 anni* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica attraverso vari metodi, inclusi ma non limitati a: revisioni della matrice SoD, analisi dei diritti di accesso rispetto alla matrice dei conflitti, valutazioni dell'efficacia dei controlli compensativi, audit del Registro delle eccezioni, audit interni ed esterni, e feedback al proprietario della politica.

Le seguenti metriche DEVONO essere tracciate e riferite al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia critica |
|---------|-----------|----------------|
| Conflitti di separazione identificati e documentati | 100% dei processi revisionati | <80% di copertura |
| Tempo per risolvere i conflitti identificati | 30 giorni di calendario | >60 giorni di calendario |
| Eccezioni attive | Ridotte al minimo; in diminuzione | >5 contemporanee o qualsiasi >90 giorni |
| Completamento della revisione trimestrale dei controlli compensativi | 100% | <80% |
| Revisione annuale della matrice SoD completata nei tempi previsti | Sì | In ritardo >30 giorni |

**Requisiti di reportistica**:
- **Dashboard mensile RSSI**: Stato del Registro delle eccezioni, eccezioni attive, risoluzioni di conflitti in scadenza.
- **Rapporto trimestrale alla Direzione generale**: Stato delle metriche, analisi delle tendenze (conflitti risolti vs. nuovi conflitti identificati), valutazione dell'efficacia dei controlli compensativi.
- **Riesame annuale della direzione**: Valutazione completa dell'efficacia del programma SoD, incluse le tendenze delle metriche, i risultati significativi e le raccomandazioni di miglioramento.

Le metriche che superano le soglie critiche DEVONO essere segnalate al RSSI per attenzione immediata e riferite nel successivo Riesame della direzione.

## Eccezioni

Qualsiasi eccezione alla presente politica DEVE essere approvata e registrata dal RSSI in anticipo, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni pianificate richiedono l'approvazione congiunta del RSSI e della Direzione generale. Le eccezioni DEVONO essere riferite al team di Riesame della direzione. Le eccezioni permanenti alla separazione finanziaria e le eccezioni che eliminano le capacità di registro di audit non sono consentite.

## Non conformità

Un dipendente che abbia violato la presente politica può essere soggetto a provvedimenti disciplinari, fino e inclusa la risoluzione del rapporto di lavoro. Le violazioni della separazione che coinvolgono processi finanziari DEVONO essere segnalate al CFO e possono comportare un'indagine aggiuntiva nell'ambito delle procedure di risposta alle frodi dell'organizzazione.

## Miglioramento continuo

La presente politica è revisionata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare i cambiamenti della struttura organizzativa, i nuovi sistemi o processi, i risultati degli audit, i cambiamenti normativi, le tendenze delle eccezioni, l'efficacia dei controlli compensativi e le lezioni apprese dagli incidenti relativi alla separazione. Le non conformità relative alla presente politica DEVONO essere registrate e gestite attraverso il processo di azione correttiva del SGSI (Clausola 10.2) con analisi della causa principale e remediation tracciata.

---

# Aree dello standard ISO 27001 trattate

Politica di separazione dei compiti — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.2 Ruoli e responsabilità per la sicurezza delle informazioni |
| Clausola 5.3 Ruoli, responsabilità e autorità organizzative | **5.3 Separazione dei compiti** |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.4 Responsabilità del management |
| Clausola 7.3 Consapevolezza | 5.15 Controllo degli accessi |
| Clausola 8.1 Pianificazione e controllo operativi | 5.16 Gestione delle identità |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 5.18 Diritti di accesso |
| Clausola 10.2 Non conformità e azioni correttive | 8.2 Diritti di accesso privilegiato |
| | 8.3 Restrizione dell'accesso alle informazioni |
| | 8.15 Registrazione |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|------------------|-----------|
| nLPD svizzera | Art. 8 — Misure tecniche e organizzative (la separazione dei compiti come misura organizzativa a protezione dell'integrità del trattamento dei dati) |
| OPDo svizzera | Art. 1-3 — Requisiti minimi per la sicurezza dei dati |
| CO svizzero Art. 728a | Sistema di controllo interno — i revisori DEVONO esaminare l'esistenza del SCI, inclusi i controlli di separazione dei compiti |
| GDPR dell'UE (ove applicabile) | Art. 32 — Sicurezza del trattamento (misure tecniche e organizzative adeguate) |
| ISO/IEC 27001:2022 | Controllo Annex A 5.3 — Separazione dei compiti |
| ISO/IEC 27002:2022 | Sezione 5.3 — Guida all'implementazione per la separazione dei compiti |
| NIST SP 800-53 Rev 5 | AC-5 (Separazione dei compiti) — Divisione delle funzioni tra individui o ruoli diversi |
| CIS Controls v8 | Controllo 5 (Gestione degli account) e Controllo 6 (Gestione del controllo degli accessi) — Misure di protezione a supporto della separazione dei compiti tramite la governance degli accessi |
| Framework COSO di controllo interno | Principio 10 — Separazione dei compiti come parte delle attività di controllo |

---

<!-- QA_VERIFIED: 2026-04-03 -->
