<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.11-IT:operational:OP-POL:a.8.11 -->
**ISMS-OP-POL-A.8.11 — Mascheratura dei dati**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Mascheratura dei dati |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.11 |
| **Creatore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione esecutiva |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
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

- ISO/IEC 27001:2022 Controllo A.8.11 — Mascheratura dei dati

**Politiche interne correlate**:

- Politica di classificazione e gestione delle informazioni
- Politica di controllo degli accessi
- Politica di privacy e protezione dei dati personali
- Politica sull'uso della crittografia
- Politica di sviluppo sicuro
- Politica di cancellazione delle informazioni

**Controlli Allegato A correlati**:

| Controllo | Relazione con la mascheratura dei dati |
|-----------|----------------------------------------|
| A.5.12 Classificazione delle informazioni | La classificazione dei dati definisce i requisiti di mascheratura per livello di sensibilità |
| A.5.15 Controllo degli accessi | La mascheratura fornisce difesa in profondità oltre ai controlli di accesso |
| A.5.34 Privacy e protezione dei dati personali | Pseudonimizzazione e anonimizzazione come misure di protezione della privacy |
| A.8.3 Restrizione dell'accesso alle informazioni | Gli utenti privilegiati possono accedere a dati non mascherati con monitoraggio |
| A.8.10 Cancellazione delle informazioni | La cancellazione è separata dalla mascheratura; entrambe riducono l'esposizione |
| A.8.24 Uso della crittografia | La crittografia protegge i dati a riposo/in transito; la mascheratura oscura i dati in uso |
| A.8.25 Ciclo di vita dello sviluppo sicuro | Gli sviluppatori utilizzano dati mascherati negli ambienti non di produzione |

---

# Politica di mascheratura dei dati

## Scopo

Lo scopo della presente politica è garantire il corretto utilizzo della mascheratura dei dati per proteggere le informazioni sensibili — tra cui le informazioni di identificazione personale (PII), i dati finanziari e le credenziali — oscurando i dati quando la piena visibilità non è necessaria per legittime finalità aziendali.

La presente politica supporta la nLPD svizzera (revDSG) Art. 7 (protezione dei dati by design e by default) e Art. 8 (sicurezza dei dati tramite misure tecniche e organizzative). Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche il GDPR Art. 25 (protezione dei dati by design e by default) e Art. 32 (sicurezza del trattamento, inclusa la pseudonimizzazione). La mascheratura dei dati è una misura tecnica fondamentale per dimostrare la conformità agli obblighi di minimizzazione dei dati nell'ambito di entrambi i quadri normativi.

## Ambito di applicazione

La presente politica si applica a:

- Tutte le categorie di dati sensibili: PII, dati finanziari, informazioni sanitarie, credenziali di autenticazione, informazioni aziendali proprietarie e qualsiasi dato classificato come Riservato o Ristretto.
- Tutti gli ambienti: produzione (ove operativamente appropriato), test/QA, sviluppo, analytics, formazione, sandbox e sistemi di backup/archiviazione.
- Tutti i casi d'uso della mascheratura: provisioning di dati non di produzione, generazione di report, condivisione di dati con terze parti, sviluppo e test di applicazioni, analytics e formazione di modelli di machine learning.
- Tutti i dipendenti, i collaboratori e i fornitori di servizi di terze parti che gestiscono dati sensibili.

I dati classificati come Pubblici secondo lo schema di classificazione dell'organizzazione sono fuori ambito. La protezione dei dati crittografati è disciplinata da A.8.24 (Uso della crittografia). La cancellazione e la distruzione dei dati sono disciplinate da A.8.10 (Cancellazione delle informazioni).

## Principio

La mascheratura dei dati viene applicata sulla base del principio di minimizzazione dei dati: il personale deve avere accesso ai dati sensibili reali solo quando è strettamente necessario per il proprio ruolo e compito. In tutti gli altri casi, i dati devono essere mascherati, pseudonimizzati o resi anonimi nella misura in cui l'utilità aziendale sia preservata.

Devono essere utilizzate solo tecniche e strumenti di mascheratura approvati dall'organizzazione. La selezione della tecnica di mascheratura deve tener conto della sensibilità dei dati, dei requisiti normativi, delle esigenze di reversibilità, della preservazione del formato e dell'integrità referenziale.

---

## Classificazione dei dati e requisiti di mascheratura

I requisiti di mascheratura sono determinati dallo schema di classificazione delle informazioni dell'organizzazione (per il Controllo A.5.12). La seguente tabella definisce l'obbligo di mascheratura per livello di classificazione:

| Classificazione | Requisito di mascheratura | Motivazione |
|-----------------|--------------------------|-------------|
| **Ristretto** | Mascheratura obbligatoria in TUTTI gli ambienti non di produzione | Massima sensibilità — l'esposizione causa danni gravi |
| **Riservato** | Mascheratura obbligatoria in non produzione; basata sul rischio in produzione | Alta sensibilità — l'esposizione causa danni sostanziali |
| **Interno** | Mascheratura basata sul rischio dove si applicano PII o requisiti normativi | Sensibilità moderata — mascheratura selettiva in base al contenuto |
| **Pubblico** | Nessuna mascheratura richiesta | Nessun requisito di riservatezza |

### Categorie di dati sensibili che richiedono valutazione

| Categoria | Esempi | Classificazione tipica |
|-----------|--------|------------------------|
| **Informazioni di identificazione personale (PII)** | Nome, AVS/SSN, numero di passaporto, e-mail, telefono, indirizzo | Ristretto / Riservato |
| **Dati finanziari** | Numero carta di credito (PAN), IBAN, saldo del conto, stipendio, codice fiscale | Ristretto / Riservato |
| **Informazioni sanitarie** | Numero di cartella clinica, diagnosi, prescrizioni, risultati di laboratorio | Ristretto |
| **Credenziali di autenticazione** | Password, chiavi API, token, chiavi private, stringhe di connessione | Ristretto |
| **Dati aziendali proprietari** | Segreti commerciali, strategie di prezzo, contratti con i clienti | Riservato |
| **Dati di categoria speciale** (GDPR Art. 9 / dati sensibili nLPD) | Origine razziale/etnica, opinioni politiche, credenze religiose, dati biometrici | Ristretto |

### Scoperta e inventario dei dati

L'organizzazione deve mantenere un inventario dei dati sensibili che richiedono mascheratura, inclusi:

- Sistemi e database contenenti dati sensibili.
- Elementi di dati (tabelle, colonne, campi) che richiedono mascheratura.
- Classificazione dei dati per elemento e requisiti normativi applicabili.
- Proprietario dei dati responsabile delle decisioni di mascheratura.

La scoperta dei dati deve essere automatizzata per tutti gli ambienti contenenti dati Ristretti o Riservati, utilizzando [Strumento di scoperta dati] o equivalente. La scoperta automatizzata deve eseguire la scansione alla ricerca di pattern di dati sensibili noti (pattern PII, numeri di carte di credito, formati AVS/SSN, identificatori sanitari) almeno su base trimestrale. L'inventario manuale è accettabile per le organizzazioni con patrimoni di dati limitati e senza dati Ristretti, ma deve essere integrato dalla scoperta automatizzata man mano che il patrimonio di dati cresce.

I Proprietari dei dati sono responsabili della classificazione dei dati nei propri domini, della determinazione dei requisiti di mascheratura, dell'approvazione delle tecniche di mascheratura per i propri dati e della convalida dell'efficacia della mascheratura.

---

## Tecniche di mascheratura approvate

Le seguenti tecniche di mascheratura sono approvate per l'uso organizzativo:

| Tecnica | Descrizione | Reversibilità | Casi d'uso principali |
|---------|-------------|---------------|-----------------------|
| **Static Data Masking (SDM)** | Sostituzione permanente dei dati nei database non di produzione prima che i dati lascino l'ambiente di produzione | Irreversibile | Ambienti non di produzione, condivisione esterna dei dati |
| **Dynamic Data Masking (DDM)** | Mascheratura in tempo reale al momento della query in base al ruolo dell'utente; i dati originali rimangono invariati nello storage | N/D (originale invariato) | Accesso basato su ruoli in produzione, regole di visualizzazione per la conformità |
| **Redazione / Nullificazione** | Rimozione completa o sostituzione con caratteri segnaposto (es. `****`, `[REDATTO]`) | Irreversibile | Report, esportazioni, screenshot, visualizzazione nell'interfaccia utente |
| **Sostituzione** | Sostituzione con dati fittizi realistici che preservano formato e distribuzione | Irreversibile | Generazione di dati di test, mantenimento dell'utilità dei dati |
| **Tokenizzazione** | Sostituzione con token non sensibili; i dati originali sono conservati in un vault di token sicuro | Reversibile (con accesso al vault) | Sistemi di pagamento, integrità referenziale, PCI DSS |
| **Pseudonimizzazione** | Sostituzione con pseudonimi; re-identificabile solo con la chiave separata | Reversibile (con chiave) | Conformità GDPR/nLPD, ricerca, analytics |
| **Anonimizzazione** | Rimozione irreversibile di tutte le informazioni identificative; nessuna chiave o mappatura conservata | Irreversibile | Pubblicazione di dati pubblici, analisi statistica, dataset aperti |

### Criteri di selezione della tecnica

Nella selezione di una tecnica di mascheratura, si devono considerare i seguenti fattori:

1. **Sensibilità dei dati**: maggiore è la sensibilità, più forte e meno reversibile deve essere la mascheratura.
2. **Requisiti normativi**: pseudonimizzazione GDPR (Art. 32, Art. 89), mascheratura dei PAN PCI DSS (Req. 3.4–3.5), minimizzazione dei dati nLPD (Art. 6).
3. **Caso d'uso aziendale**: sviluppo/test, analytics, condivisione esterna o formazione.
4. **Necessità di reversibilità**: se esiste una legittima necessità di recuperare i dati originali.
5. **Preservazione del formato**: se l'applicazione richiede che il formato dei dati sia mantenuto.
6. **Integrità referenziale**: se le relazioni tra tabelle e le chiavi esterne devono rimanere valide.
7. **Impatto sulle prestazioni**: overhead del DDM in tempo reale rispetto all'elaborazione batch dell'SDM.

Le nuove tecniche di mascheratura o le modifiche significative alle tecniche approvate devono essere proposte al Team di sicurezza, sottoposte a revisione e test di sicurezza, e approvate dal RSSI prima dell'uso.

### Pseudonimizzazione vs. anonimizzazione (distinzione normativa)

Ai sensi sia del GDPR che della nLPD, i dati pseudonimizzati rimangono dati personali perché la re-identificazione è possibile con la chiave separata. I dati anonimizzati — laddove la re-identificazione non sia più ragionevolmente possibile — non rientrano nell'ambito della normativa sulla protezione dei dati. L'organizzazione deve garantire che la tecnica corretta sia applicata in base al fatto che i dati debbano rimanere nell'ambito della protezione dei dati (pseudonimizzazione) o possano essere completamente rimossi dall'ambito (anonimizzazione).

**Valutazione dell'utilità dei dati anonimizzati**: Prima di applicare l'anonimizzazione, il Proprietario dei dati deve valutare se i dati anonimizzati conservino un'utilità aziendale sufficiente per lo scopo previsto. La valutazione deve considerare:

- Se le proprietà statistiche (distribuzioni, correlazioni, tendenze) siano preservate.
- Se i dati anonimizzati supportino il caso d'uso di analisi, formazione o test previsto.
- Se la generalizzazione o la soppressione eccessiva renda i dati inutilizzabili.
- I trade-off tra protezione della privacy (k-anonimato più elevato) e utilità dei dati (meno generalizzazione).

Laddove l'anonimizzazione riduca eccessivamente l'utilità dei dati, la pseudonimizzazione con controlli di accesso appropriati può essere un'alternativa preferibile.

Le chiavi di pseudonimizzazione devono essere conservate separatamente dai dati pseudonimizzati, con i seguenti requisiti di separazione:

- **Separazione fisica o logica**: Le chiavi devono essere conservate in un sistema, database o dominio di sicurezza diverso dai dati pseudonimizzati. È vietato co-localizzare chiavi e dati sullo stesso server o nello stesso database.
- **Separazione degli accessi**: Il personale con accesso ai dati pseudonimizzati non deve avere accesso alle chiavi di re-identificazione salvo specifica autorizzazione per uno scopo documentato. Il controllo duale (autorizzazione a due persone) è richiesto per la re-identificazione dei dati Ristretti.
- **Registrazione della re-identificazione**: Tutti gli eventi di re-identificazione devono essere registrati con l'identità del richiedente, la giustificazione, l'ambito dei dati e il riferimento all'approvazione.

La gestione delle chiavi deve seguire la Politica sull'uso della crittografia (A.8.24).

---

## Pratiche vietate

Le seguenti pratiche NON sono accettabili come tecniche di mascheratura:

| Pratica vietata | Motivazione |
|-----------------|-------------|
| **ROT13 o cifrario di Cesare** | Banalmente reversibile; non crittograficamente sicuro |
| **Solo codifica reversibile** (Base64, codifica URL, esadecimale) | Non è mascheratura — è solo codifica; facilmente reversibile da chiunque |
| **Semplice sostituzione di caratteri** (A=1, B=2) | Schema prevedibile; banalmente reversibile |
| **Solo mascheratura lato client** (JavaScript / livello UI) | Aggirabile — i dati rimangono non mascherati nel backend |
| **"Crittografia" auto-progettata** | Sicurezza non convalidata; non accettata per la conformità |
| **Dati di produzione in non produzione senza alcuna mascheratura** | Violazione fondamentale della politica |
| **Utilizzo indefinito dello stesso dataset mascherato senza aggiornamento** | Dati obsoleti; potenziale per la circumvenzione nel tempo |

Queste pratiche forniscono un'apparenza di sicurezza senza una protezione reale. Non sono accettabili in nessuna circostanza e non può essere concessa alcuna eccezione per il loro utilizzo.

---

## Requisiti di copertura degli ambienti

I dati sensibili devono essere mascherati negli ambienti in cui la piena visibilità non è necessaria per le operazioni aziendali legittime.

| Ambiente | Requisito di mascheratura | Motivazione |
|----------|--------------------------|-------------|
| **Produzione** | Basata sul rischio; applicare DDM ove operativamente fattibile | Le operazioni aziendali possono richiedere alcuni dati reali; documentare la giustificazione per i dati non mascherati |
| **Test / QA** | Obbligatoria per dati Ristretti e Riservati | Nessuna necessità aziendale di dati sensibili reali nei test |
| **Sviluppo** | Obbligatoria per dati Ristretti e Riservati | Gli sviluppatori non hanno bisogno di dati sensibili reali |
| **Analytics / BI** | Obbligatoria salvo che i dati siano aggregati o anonimizzati | L'analytics può funzionare con dati mascherati o aggregati |
| **Formazione / Demo** | Obbligatoria per TUTTI i dati sensibili — nessuna eccezione | Gli ambienti di formazione devono utilizzare dati non sensibili |
| **Sandbox / Sperimentale** | Obbligatoria per TUTTI i dati sensibili — nessuna eccezione | Gli ambienti non controllati sono ad alto rischio |
| **Backup / Archivio** | Stessa protezione dell'ambiente sorgente | I backup rispecchiano la sensibilità dei dati sorgente |

### Requisiti di implementazione SDM

- L'SDM deve essere applicato PRIMA che i dati lascino l'ambiente di produzione.
- L'SDM deve mantenere l'integrità referenziale tra le tabelle correlate. Dove esistono relazioni multi-tabella, la mascheratura deve essere applicata in modo coerente utilizzando la stessa chiave o mappatura di mascheratura per preservare le relazioni di chiave esterna, l'integrità dei join e le regole aziendali tra tabelle. L'integrità referenziale deve essere convalidata tramite test automatizzati dopo ogni ciclo di mascheratura.
- L'SDM deve preservare il formato dei dati per la compatibilità delle applicazioni. Nota: la preservazione del formato può ridurre l'entropia di mascheratura (numero di valori mascherati possibili), il che aumenta il rischio di re-identificazione. Per i dati Ristretti, l'organizzazione deve valutare se la mascheratura con preservazione del formato fornisca una sicurezza sufficiente o se siano richieste tecniche senza preservazione del formato con adattamento a livello applicativo.
- I dati mascherati devono essere sufficientemente realistici per i test delle applicazioni.
- **Aggiornamento dei dati mascherati**: Gli ambienti non di produzione che utilizzano SDM devono essere aggiornati con dati nuovamente mascherati a una frequenza definita — almeno trimestralmente per gli ambienti di sviluppo attivi e semestralmente per gli ambienti meno attivi. La frequenza di aggiornamento deve tener conto delle modifiche ai dati di produzione che possono influire sulla validità dei test e della riduzione del rischio di circumvenzione della mascheratura attraverso la conoscenza accumulata di dataset mascherati obsoleti.

### Requisiti di implementazione DDM

- Il DDM deve essere applicato a livello di database o applicativo — non lato client.
- Le regole DDM devono essere basate su ruoli utente documentati e privilegio minimo.
- Il DDM non deve essere aggirabile dagli utenti senza autorizzazione appropriata. I controlli di prevenzione del bypass devono includere:
  - L'accesso diretto al database (che bypassa il livello applicativo) deve essere limitato agli amministratori di database autorizzati.
  - Le regole DDM devono essere applicate a livello di motore di database ove supportato, non esclusivamente a livello applicativo.
  - I tentativi di interrogare i dati sottostanti non mascherati tramite viste, stored procedure o percorsi di accesso alternativi devono essere bloccati o registrati e segnalati.
  - I test periodici devono verificare che il DDM non possa essere aggirato tramite SQL injection, escalation dei privilegi o manipolazione dello schema.
- L'impatto sulle prestazioni deve essere valutato e mantenuto entro soglie definite:
  - **Latenza delle query**: Il DDM non deve aggiungere più del 15% di latenza ai tempi di risposta delle query di base per le query standard.
  - **Throughput**: Il DDM non deve ridurre il throughput del database di più del 10% nelle normali condizioni operative.
  - **Misurazione della baseline**: Le baseline delle prestazioni devono essere stabilite prima della distribuzione del DDM e ri-misurate trimestralmente.
  - **Escalation**: Laddove il DDM superi le soglie di prestazione, il Team di sicurezza deve valutare approcci di mascheratura alternativi (pre-elaborazione SDM, mascheratura a livello applicativo o ottimizzazione delle regole DDM).

### Requisiti di tokenizzazione

- Il vault dei token deve essere protetto con controlli di accesso e crittografia. Le chiavi di crittografia del vault devono essere:
  - Generate e conservate in un hardware security module (HSM) o [KMS] ove disponibile.
  - Ruotate almeno annualmente, con rotazione automatizzata preferita.
  - Sottoposte a backup e recuperabili per le procedure di gestione delle chiavi dell'organizzazione (A.8.24).
  - Con controllo degli accessi separato dai dati tokenizzati — gli amministratori del vault non devono avere accesso diretto ai dataset tokenizzati, e viceversa.
- I token devono preservare il formato ove richiesto (es. formato carta di credito per PCI DSS).
- La de-tokenizzazione deve richiedere autorizzazione esplicita ed essere registrata. L'accesso alla de-tokenizzazione deve essere rivisto trimestralmente nell'ambito delle revisioni degli accessi privilegiati.
- La gestione delle chiavi del vault deve seguire la Politica sull'uso della crittografia (A.8.24).

---

## Test e convalida

Le implementazioni di mascheratura devono essere testate prima della distribuzione e dopo qualsiasi modifica alla configurazione della mascheratura.

| Tipo di test | Scopo | Quando richiesto |
|--------------|-------|-----------------|
| **Test di efficacia** | Verificare che i dati originali non siano recuperabili dall'output mascherato | Prima della distribuzione; dopo le modifiche |
| **Test di integrità referenziale** | Verificare che le relazioni tra tabelle siano preservate | Prima della distribuzione |
| **Test di convalida del formato** | Verificare che i dati mascherati superino le regole di convalida delle applicazioni | Prima della distribuzione |
| **Test delle prestazioni** | Verificare che l'overhead del DDM sia entro i limiti accettabili | Prima della distribuzione del DDM |
| **Valutazione del rischio di re-identificazione** | Verificare che i dati anonimizzati/pseudonimizzati non possano essere re-identificati | Annualmente; dopo le modifiche alla struttura dei dati |
| **Test di regressione** | Verificare che la mascheratura continui a funzionare dopo le modifiche al sistema | Dopo le modifiche alla configurazione della mascheratura |

### Metodi di convalida

- Ispezione di campioni di dati: confronto manuale di dati mascherati e non mascherati.
- Rilevamento automatizzato di pattern: scansione degli ambienti non di produzione per pattern di dati sensibili non mascherati (es. numeri di carte di credito, numeri AVS, indirizzi e-mail).
- Tentativi di reverse engineering: tentativo di recuperare i dati originali dall'output mascherato.
- Per l'anonimizzazione: analisi statistica con soglie basate sul rischio:
  - **Dati Ristretti**: k-anonimato ≥ 20, l-diversità ≥ 5 ove applicabile.
  - **Dati Riservati**: k-anonimato ≥ 10, l-diversità ≥ 3 ove applicabile.
  - **Dati Interni**: k-anonimato ≥ 5 minimo.
  - Laddove le soglie di k-anonimato non possano essere raggiunte, l'utilità dei dati deve essere valutata rispetto al rischio di re-identificazione, e devono essere applicate tecniche alternative (generalizzazione, soppressione, aggiunta di rumore) per raggiungere la soglia target.

### Criteri di accettazione

La mascheratura è accettabile quando:

- I valori originali dei dati sensibili NON sono presenti nei dataset mascherati.
- Il formato dei dati e l'integrità referenziale sono preservati.
- La funzionalità delle applicazioni non è compromessa.
- L'impatto sulle prestazioni è entro i limiti accettabili.
- I requisiti normativi sono soddisfatti.

Quando i test identificano guasti, l'implementazione deve essere corretta prima dell'uso in produzione, la causa principale documentata e il re-test eseguito.

### Frequenza delle valutazioni

- **Valutazione completa**: annuale (allineata al programma di audit interno).
- **Verifica periodica**: trimestrale per i sistemi ad alto rischio e gli ambienti modificati di recente.
- **Valutazione attivata**: entro 30 giorni da un significativo incidente di esposizione dei dati, da un cambiamento importante al sistema che influisce sui dati sensibili, dalla distribuzione di una nuova soluzione di mascheratura, o da una modifica ai requisiti normativi.

---

## Registrazione e monitoraggio

I seguenti eventi correlati alla mascheratura devono essere registrati ove tecnicamente fattibile:

- Esecuzione del processo di mascheratura (avvio, completamento, errori).
- Modifiche alla configurazione della mascheratura (cambi di tecnica, aggiornamenti delle regole). Le modifiche alla configurazione devono seguire il processo di gestione delle modifiche dell'organizzazione: richieste da personale autorizzato, revisionate dal Team di sicurezza, testate in un ambiente non di produzione, approvate dal Proprietario dei dati e dal Responsabile del Team di sicurezza prima della distribuzione in produzione, e registrate con gli stati di configurazione prima e dopo.
- Eccezioni e bypass alla mascheratura (approvati o tentati).
- Applicazione delle politiche di mascheratura dinamica (chi ha avuto accesso a quali dati con quale regola di mascheratura).
- Guasti alla mascheratura (processi che non si sono completati).

**Conservazione dei log**:

| Tipo di evento | Conservazione minima |
|----------------|---------------------|
| Log del processo di mascheratura | 90 giorni |
| Modifiche alla configurazione | 12 mesi |
| Eventi di eccezione e bypass | 12 mesi |
| Log di accesso alla mascheratura dinamica | 90 giorni (Riservato+) |

Si applica una conservazione estesa ove i requisiti normativi prevedano periodi più lunghi.

L'organizzazione deve monitorare i guasti ai processi di mascheratura, i tentativi ripetuti di bypass, le modifiche non autorizzate alla configurazione e il degrado delle prestazioni del DDM. Gli avvisi devono essere integrati nel programma di monitoraggio della sicurezza dell'organizzazione.

**Rilevamento di tentativi di re-identificazione**: L'organizzazione deve implementare il monitoraggio per rilevare potenziali tentativi di re-identificazione, inclusi:

- Pattern di query insoliti contro dataset pseudonimizzati o anonimizzati (es. enumerazione sistematica, correlazione con fonti di dati esterne).
- Estrazione massiva di dati da ambienti contenenti dati mascherati.
- Tentativi di accedere a chiavi di pseudonimizzazione o vault di token da parte di personale non autorizzato.
- Query di correlazione che uniscono dataset mascherati con dati di riferimento non mascherati.

I tentativi di re-identificazione rilevati devono essere trattati come incidenti di sicurezza di gravità Alta e investigati immediatamente.

---

## Risposta agli incidenti per i guasti alla mascheratura

Gli incidenti di sicurezza relativi alla mascheratura dei dati includono:

| Tipo di incidente | Gravità | Risposta |
|-------------------|---------|----------|
| Dati sensibili non mascherati scoperti in non produzione | Alta | Contenimento entro 1 ora — interrompere il flusso di dati, eliminare i dati esposti, notificare il Proprietario dei dati |
| Guasto al processo di mascheratura che espone dati sensibili | Critica | Contenimento entro 15 minuti — interrompere l'esposizione, isolare i sistemi interessati, notificare il RSSI |
| Re-identificazione riuscita di dati mascherati | Alta | Valutare la debolezza della tecnica, rafforzare la mascheratura |
| Tentativo di bypass o circumvenzione della mascheratura | Alta | Investigare, prevenire la ricorrenza |
| Accesso non autorizzato al vault dei token o alle chiavi di pseudonimizzazione | Critica | Risposta alla compromissione delle chiavi per A.8.24 |
| Esfiltrazione di dati da un ambiente insufficientemente mascherato | Critica | Risposta completa agli incidenti, valutazione della notifica della violazione |

### Processo di risposta

1. **Rilevare e segnalare**: tramite monitoraggio, segnalazioni degli utenti o test.
2. **Classificare**: gravità in base alla sensibilità dei dati e all'ambito dell'esposizione.
3. **Contenere**: interrompere il flusso di dati, isolare i sistemi, prevenire ulteriore esposizione.
4. **Investigare**: analisi della causa principale, determinazione dell'ambito, valutazione dell'impatto.
5. **Rimediare**: correggere la mascheratura, convalidare l'efficacia, prevenire la ricorrenza.
6. **Notificare**: escalation interna; valutare i requisiti di notifica della violazione normativa.
7. **Rivedere**: lezioni apprese, miglioramenti dei controlli.

### Valutazione della notifica della violazione

Gli incidenti di esposizione dei dati devono essere valutati per i requisiti di notifica della violazione:

- **nLPD svizzera**: Notifica all'IFPDT se rischio elevato per la personalità o i diritti fondamentali (Art. 24).
- **GDPR UE** (ove applicabile): Notifica entro 72 ore se rischio per i diritti e le libertà (Art. 33–34).
- **Specifici del settore**: Notifica della violazione PCI DSS, notifica della violazione HIPAA (se applicabile).

Il DPD e il Legale/Compliance devono essere coinvolti in tutte le decisioni di notifica della violazione.

---

## Gestione delle eccezioni

Le eccezioni ai requisiti di mascheratura dei dati richiedono:

- Giustificazione aziendale documentata che spieghi perché la mascheratura non può essere implementata.
- Valutazione del rischio che copre probabilità e impatto dell'esposizione dei dati.
- Controlli compensativi (controlli di accesso potenziati, crittografia, monitoraggio).
- Durata definita e percorso verso il raggiungimento della piena conformità.
- Approvazione del Proprietario dei dati per il dominio dei dati interessato.
- Approvazione del RSSI per eccezioni ai dati Riservati/Ristretti.

| Tipo di eccezione | Approvazione richiesta | Durata massima |
|-------------------|----------------------|----------------|
| Sistema singolo (bassa sensibilità) | Responsabile del Team di sicurezza + Proprietario dei dati | 12 mesi, con revisione intermedia a 6 mesi |
| Sistema singolo (alta sensibilità) | RSSI + Proprietario dei dati | 6 mesi, con revisione intermedia a 3 mesi |
| Eccezione a livello di ambiente | RSSI + Proprietario dei dati | 6 mesi, con reportistica mensile sui progressi |
| Deroga alla mascheratura di produzione | RSSI + Direzione esecutiva | Ri-approvazione annuale, con revisioni trimestrali degli obiettivi |
| Override delle tecniche vietate | NON CONSENTITO | N/D |

Le eccezioni attive devono essere riviste trimestralmente, revocate in caso di modifica della giustificazione aziendale e automaticamente scadono al termine della durata approvata (nessun rinnovo implicito).

---

## Opzionale: Controlli sui dati delle carte di pagamento (PCI DSS)

*Applicabile solo se vengono trattati dati delle carte di pagamento e sussiste l'ambito PCI.*

Se sussiste l'ambito PCI, si applicano i seguenti requisiti aggiuntivi di mascheratura dei dati:

- I Primary Account Number (PAN) devono essere resi illeggibili ovunque vengano memorizzati, per PCI DSS Req. 3.4 (tokenizzazione, troncamento, hashing o crittografia forte).
- Quando i PAN vengono visualizzati, la mascheratura deve mostrare al massimo le prime sei e le ultime quattro cifre, per PCI DSS Req. 3.5.1.
- I PAN completi non devono essere presenti negli ambienti non di produzione salvo che l'ambiente non di produzione soddisfi tutti i controlli PCI DSS applicabili. L'SDM o la tokenizzazione devono essere applicati prima che i dati lascino l'ambiente dei dati dei titolari di carta.
- L'utilizzo di dati di carte di pagamento in non produzione deve essere disciplinato da una politica documentata sull'utilizzo dei dati per PCI DSS Req. 12.3.

---

## Formazione e sensibilizzazione

**Tutto il personale** deve ricevere formazione annuale sulla sensibilizzazione alla sicurezza che includa:

- L'obbligo di utilizzare dati mascherati negli ambienti non di produzione.
- Come riconoscere e segnalare dati sensibili non mascherati.
- Il divieto di tentare di re-identificare dati mascherati, pseudonimizzati o anonimizzati.

**Il personale tecnico** (Team di sicurezza, IT Operations, sviluppatori) deve ricevere formazione su:

- Tecniche di mascheratura approvate e utilizzo degli strumenti.
- Procedure di test e convalida.
- Risposta agli incidenti per i guasti alla mascheratura.

**I Proprietari dei dati** devono essere informati su:

- Responsabilità di classificazione dei dati e decisioni di mascheratura.
- Criteri di valutazione e approvazione delle richieste di eccezione.
- Convalida dell'efficacia della mascheratura per i propri domini di dati.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Anonimizzazione** | Rimozione irreversibile di tutte le informazioni identificative tale che la re-identificazione non sia possibile. I dati anonimizzati non sono più dati personali ai sensi del GDPR/nLPD. |
| **Mascheratura dei dati** | Processo di oscuramento dei dati originali con contenuto modificato per proteggere le informazioni sensibili preservando il formato e l'usabilità dei dati. |
| **Dynamic Data Masking (DDM)** | Mascheratura in tempo reale applicata al momento dell'accesso ai dati in base al ruolo o al contesto dell'utente. I dati originali rimangono invariati nello storage. |
| **Pseudonimizzazione** | Sostituzione degli identificatori diretti con pseudonimi tale che i dati non possano identificare gli individui senza informazioni aggiuntive (chiave) detenute separatamente. I dati pseudonimizzati rimangono dati personali. |
| **Re-identificazione** | Processo di determinazione dell'identità originale di un interessato da dati mascherati, pseudonimizzati o anonimizzati. |
| **Integrità referenziale** | Mantenimento di relazioni valide tra dati correlati tra tabelle o dataset dopo la mascheratura. |
| **Static Data Masking (SDM)** | Sostituzione permanente dei dati sensibili con valori mascherati nei database non di produzione. I dati originali vengono sostituiti irreversibilmente. |
| **Tokenizzazione** | Sostituzione dei dati sensibili con token non sensibili; i dati originali sono conservati in un vault di token sicuro che consente una reversibilità controllata. |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **Direzione esecutiva** | Approvare la politica di mascheratura dei dati; garantire risorse adeguate; accettare il rischio residuo dove la mascheratura non è fattibile |
| **RSSI** | Responsabile dell'efficacia della politica e del programma di mascheratura; approvare le eccezioni ad alto rischio e le nuove tecniche; revisione annuale della politica |
| **DPD** | Fornire consulenza sulla conformità GDPR/nLPD per le implementazioni di mascheratura; rivedere le tecniche di pseudonimizzazione e anonimizzazione per l'adeguatezza normativa |
| **Proprietari dei dati** | Classificare i dati; determinare i requisiti di mascheratura; approvare tecniche ed eccezioni per i propri domini di dati; convalidare l'efficacia della mascheratura |
| **Team di sicurezza** | Implementare la politica di mascheratura; valutare e selezionare gli strumenti; configurare e mantenere le soluzioni; condurre i test di efficacia |
| **IT Operations** | Distribuire e mantenere l'infrastruttura di mascheratura; eseguire i job batch SDM e la configurazione DDM; monitorare le prestazioni del processo di mascheratura |
| **Team di sviluppo** | Utilizzare dati mascherati in non produzione; implementare il DDM nelle applicazioni ove richiesto; segnalare i problemi di mascheratura; vietato aggirare i controlli |
| **Tutto il personale** | Rispettare la politica di mascheratura; segnalare sospetti dati sensibili non mascherati in non produzione; vietato tentare la re-identificazione |

---

## Prove

| # | Prova | Responsabile | Frequenza | Conservazione |
|---|-------|-------------|-----------|---------------|
| 1 | Inventario dei dati sensibili (sistemi, elementi di dati, classificazione, stato di mascheratura) | Proprietari dei dati / Team di sicurezza | Revisione annuale, aggiornamento continuo | 3 anni |
| 2 | Inventario delle tecniche di mascheratura (tecniche approvate, strumenti, configurazioni) | Team di sicurezza | Revisione annuale | 3 anni |
| 3 | Valutazione della copertura degli ambienti (quali ambienti sono mascherati, lacune, eccezioni) | Team di sicurezza | Annuale, trimestrale per gli ambienti ad alto rischio | 3 anni |
| 4 | Risultati dei test di efficacia della mascheratura (ispezioni di campioni, scansioni di pattern) | Team di sicurezza | Prima della distribuzione; dopo le modifiche | 3 anni |
| 5 | Registro delle eccezioni (eccezioni attive, approvazioni, controlli compensativi, date di scadenza) | RSSI / Team di sicurezza | Revisione trimestrale | 3 anni |
| 6 | Log del processo di mascheratura e registrazioni delle modifiche alla configurazione | IT Operations | Continuo | Per la tabella di conservazione dei log |
| 7 | Registrazioni degli incidenti per i guasti alla mascheratura | Team di sicurezza | Per incidente | 3 anni |
| 8 | **Accordi di condivisione dei dati con terze parti** (requisiti di mascheratura, divieto di re-identificazione, diritti di audit) | Legale / Team di sicurezza | Per accordo di condivisione; revisione annuale | Attivo + 3 anni |
| 9 | **Risultati della valutazione del rischio di re-identificazione** (misurazioni k-anonimato, l-diversità, valutazioni dell'utilità dei dati) | Team di sicurezza / Proprietari dei dati | Annualmente; dopo le modifiche alla struttura dei dati | 3 anni |
| 10 | **Registrazioni delle modifiche alla configurazione della mascheratura** (richieste di modifica, approvazioni, stati prima/dopo, risultati dei test) (SOC 2: CC8.1) | Team di sicurezza / IT Operations | Per modifica | 3 anni |
| 11 | **Registrazioni del monitoraggio delle prestazioni DDM** (misurazioni baseline, report di prestazioni trimestrali, avvisi di soglia) | IT Operations | Trimestrale | 12 mesi |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri: scansioni automatizzate dei dati sensibili negli ambienti non di produzione, test di efficacia della mascheratura, revisioni del registro delle eccezioni, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita. Le eccezioni devono essere segnalate al Team di revisione della direzione. Le tecniche vietate non possono essere oggetto di eccezione in nessuna circostanza.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento. I tentativi deliberati di aggirare i controlli di mascheratura o di re-identificare dati mascherati sono trattati come gravi violazioni della sicurezza.

## Requisiti per la condivisione di dati con terze parti

Laddove l'organizzazione condivida dati mascherati, pseudonimizzati o anonimizzati con terze parti (fornitori, partner, ricercatori, clienti):

- **Requisiti contrattuali**: Gli accordi di condivisione dei dati devono specificare:
  - La tecnica di mascheratura applicata e la classificazione dei dati originali.
  - Il divieto di tentare di re-identificare dati mascherati, pseudonimizzati o anonimizzati.
  - Obblighi di restituzione o distruzione alla risoluzione dell'accordo di condivisione.
  - Disposizioni di diritto di audit per verificare le pratiche di gestione dei dati della terza parte.
  - Obblighi di notifica della violazione se la terza parte scopre che i dati sono stati re-identificati o esposti.
- **Valutazione del rischio**: Una valutazione del rischio di condivisione dei dati deve essere eseguita prima della condivisione iniziale, valutando il rischio di re-identificazione, la maturità nella gestione dei dati della terza parte e le implicazioni normative.
- **Monitoraggio continuativo**: Gli accordi di condivisione dei dati devono essere rivisti annualmente e in caso di modifiche rilevanti all'ambiente della terza parte o all'ambito dei dati condivisi.

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di modifiche ai regolamenti sulla protezione dei dati, nuove tecniche di re-identificazione emergenti, nuove tecnologie di mascheratura, risultati degli audit e lezioni apprese dagli incidenti di mascheratura.

---

# Aree della norma ISO 27001 trattate

Politica di mascheratura dei dati — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.12 Classificazione delle informazioni |
| Clausola 6.1 Azioni per affrontare i rischi | 5.15 Controllo degli accessi |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.34 Privacy e protezione dei dati personali |
| Clausola 7.3 Consapevolezza | 8.3 Restrizione dell'accesso alle informazioni |
| | 8.10 Cancellazione delle informazioni |
| | **8.11 Mascheratura dei dati** |
| | 8.24 Uso della crittografia |

**Quadro normativo e legale**:

| Quadro | Rilevanza | Applicabilità |
|--------|-----------|---------------|
| nLPD svizzera (revDSG) | Art. 7 — Protezione dei dati by design e by default; Art. 8 — Sicurezza dei dati (misure tecniche e organizzative) | Obbligatorio |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati | Obbligatorio |
| GDPR UE (ove applicabile) | Art. 25 — Protezione dei dati by design e by default; Art. 32 — Sicurezza del trattamento (pseudonimizzazione); Art. 89 — Misure di salvaguardia per ricerca/statistiche | Dove vengono trattati dati personali UE/SEE |
| ISO/IEC 27001:2022 | Allegato A Controllo 8.11 — Mascheratura dei dati | Ambito di certificazione |
| ISO/IEC 27002:2022 | Sezione 8.11 — Guida all'implementazione per i controlli di mascheratura dei dati | Guida |
| PCI DSS v4.0 | Req. 3.4–3.5 — Mascheratura e rendere illeggibili i PAN; Req. 12.3 — Politiche sui dati non di produzione | Se vengono trattati dati di carte di pagamento |
| HIPAA Privacy Rule | §164.514 — Standard di de-identificazione (Expert Determination / Safe Harbor) | Se vengono trattati dati sanitari USA (ePHI) |
| FINMA | Protezione dei dati dei clienti; gestione del rischio di outsourcing (Circolare 2018/3) | Se istituto finanziario svizzero regolamentato |

---

<!-- QA_VERIFIED: 2026-04-03 -->
