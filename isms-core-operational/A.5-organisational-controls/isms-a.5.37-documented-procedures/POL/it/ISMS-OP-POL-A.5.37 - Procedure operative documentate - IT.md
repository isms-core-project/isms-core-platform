<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.37-IT:operational:OP-POL:a.5.37 -->
**ISMS-OP-POL-A.5.37 — Procedure operative documentate**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Procedure operative documentate |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.37 |
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
| 1.0 | [Data] | RSSI | Policy operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.5.37 — Procedure operative documentate
- ISO/IEC 27001:2022 Clausola 7.5 — Informazioni documentate

**Controlli Allegato A correlati**:

| Controllo | Relazione con le procedure operative documentate |
|-----------|--------------------------------------------------|
| A.5.1 Policy per la sicurezza delle informazioni | Le policy definiscono i requisiti; le procedure li implementano |
| A.5.24–28 Gestione degli incidenti | Le procedure di risposta agli incidenti documentate per questa policy |
| A.6.3 Consapevolezza, formazione e istruzione sulla sicurezza delle informazioni | Il personale formato sulle procedure pertinenti |
| A.8.32 Gestione dei cambiamenti | Le procedure aggiornate tramite il processo di gestione dei cambiamenti |
| A.8.9 Gestione della configurazione | Le procedure di configurazione documentate |

**Policy interne correlate**:

- Policy per la sicurezza delle informazioni
- Policy sulla gestione dei cambiamenti
- Policy sulla gestione degli incidenti
- Policy sulla consapevolezza e formazione in materia di sicurezza delle informazioni

---

# Policy sulle procedure operative documentate

## Scopo

Lo scopo di questa policy è garantire che le procedure operative per le strutture di elaborazione delle informazioni siano documentate, mantenute e rese disponibili al personale che ne ha bisogno, consentendo operazioni coerenti, sicure e verificabili.

Questa policy supporta la nLPD svizzera (revLPD) e l'Ordinanza sulla protezione dei dati (OPDo) implementando misure tecniche e organizzative documentate adeguate al rischio. Le procedure documentate dimostrano l'impegno dell'organizzazione verso controlli sistematici di protezione dei dati e sicurezza. Laddove l'organizzazione tratti dati di persone nell'UE/SEE, si applicano anche i requisiti del GDPR.

## Ambito

Tutti i dipendenti e gli utenti terzi.

Tutte le procedure operative per le strutture di elaborazione delle informazioni, i sistemi, le applicazioni e i controlli di sicurezza operati dall'organizzazione o per suo conto.

Tutti gli ambienti: produzione, test, sviluppo e disaster recovery.

## Principio

Le procedure operative per le strutture di elaborazione delle informazioni DEVONO essere documentate e rese disponibili al personale che ne ha bisogno. I documenti richiesti per il sistema di gestione della sicurezza delle informazioni sono controllati, gestiti e disponibili. Non è possibile operare in modo sicuro senza procedure documentate, testate e mantenute.

---

## Procedure documentate obbligatorie

L'organizzazione DEVE documentare le procedure operative per le seguenti categorie:

### Operazioni di sicurezza

| Categoria di procedura | Esempi |
|------------------------|--------|
| **Gestione degli accessi** | Provisioning degli utenti, revisione degli accessi, accesso di emergenza, deprovisioning |
| **Risposta agli incidenti** | Rilevamento, triage, escalation, comunicazione, conservazione delle prove |
| **Gestione delle vulnerabilità** | Scansione, valutazione, prioritizzazione, rimedio |
| **Backup e ripristino** | Esecuzione del backup, verifica, test di ripristino |
| **Monitoraggio e revisione dei log** | Revisione dei log, risposta agli avvisi, escalation |
| **Gestione delle patch** | Valutazione, test, distribuzione, verifica |

### Operazioni di sistema

| Categoria di procedura | Esempi |
|------------------------|--------|
| **Avvio e arresto** | Avvio del sistema, arresto controllato, arresto di emergenza |
| **Elaborazione batch** | Pianificazione dei job, monitoraggio, gestione dei guasti |
| **Gestione degli errori** | Rilevamento degli errori, registrazione, escalation |
| **Gestione dei supporti** | Archiviazione, trasporto, dismissione dei supporti rimovibili |
| **Manutenzione del sistema** | Manutenzione ordinaria, operazioni di pulizia, controlli dello stato di salute |

### Operazioni amministrative

| Categoria di procedura | Esempi |
|------------------------|--------|
| **Supporto agli utenti** | Gestione delle richieste, risoluzione dei problemi |
| **Implementazione dei cambiamenti** | Verifiche pre-cambiamento, esecuzione, verifica post-cambiamento |
| **Disaster recovery** | Attivazione del DR, esecuzione del ripristino, ritorno alle operazioni normali |

---

## Creazione e aggiornamento delle procedure

### Standard di documentazione

Tutte le procedure operative DEVONO includere i seguenti elementi obbligatori:

| Elemento | Requisito |
|----------|-----------|
| **ID documento** | Identificatore univoco secondo la convenzione di denominazione dell'organizzazione: **[Specificare il formato, es. "PROC-[CATEGORIA]-[###]" dove CATEGORIA = SEC (sicurezza), OPS (operazioni), ADM (amministrativo), DR (disaster recovery)]**. Esempi: PROC-SEC-001 (Provisioning utenti), PROC-DR-005 (Ripristino backup) |
| **Titolo** | Titolo chiaro e descrittivo |
| **Versione** | Numero di versione e data |
| **Responsabile** | Responsabile della procedura designato (nome e ruolo) responsabile dell'accuratezza e dell'aggiornamento |
| **Responsabile di backup** | Responsabile di backup designato per le procedure critiche per evitare punti di guasto singoli |
| **Approvazione** | Nome e data dell'approvatore |
| **Scopo** | Perché la procedura esiste |
| **Ambito** | Cosa copre la procedura |
| **Prerequisiti** | Condizioni, accessi, strumenti richiesti |
| **Passaggi** | Passaggi sequenziali e numerati |
| **Output attesi** | Cosa l'operatore dovrebbe vedere nei passaggi chiave |
| **Verifica** | Come confermare il completamento con successo |
| **Rollback** | Passaggi di ripristino in caso di fallimento della procedura |
| **Riferimenti** | Documenti correlati e contatti |

### Requisiti di qualità

- Redatta chiaramente per il livello di competenza del pubblico di destinazione.
- Sufficientemente dettagliata affinché un operatore competente ma non familiare con la procedura possa eseguirla.
- Priva di ambiguità e supposizioni non dichiarate.
- Testata prima dell'uso in produzione.
- Revisionata e approvata prima della pubblicazione.

### Formato e supporto

Le procedure DEVONO essere create in formato elettronico utilizzando applicazioni per ufficio standard e supportate o sistemi operativi nativi. L'organizzazione DEVE garantire un'adeguata identificazione e descrizione (titolo, data, autore, numero di riferimento), un formato coerente (lingua, versione del software, grafica) e revisione e approvazione per idoneità e adeguatezza.

---

## Archiviazione e disponibilità dei documenti

### Repository autorevole

Le procedure DEVONO essere archiviate nel sistema di gestione dei documenti dell'organizzazione: **[Specificare: SharePoint, Confluence, Notion, o equivalente]**.

**Ubicazione del repository**: [URL o percorso: es. "https://company.sharepoint.com/sites/ISMS/Procedures"]

**Accesso**: L'accesso al repository dei documenti è limitato al personale autorizzato per la Policy sul controllo degli accessi. Tutti i dipendenti possono visualizzare le procedure pertinenti al proprio ruolo; solo i responsabili delle procedure e il personale designato possono modificare.

Questo repository è la fonte autorevole unica per le procedure operative. Le copie locali e i duplicati sono vietati, eccetto per le copie offline di emergenza approvate.

### Requisiti di disponibilità

| Tipo di procedura | Requisito di disponibilità |
|-------------------|-----------------------------|
| **Procedure di emergenza e DR** | Copie cartacee + copia digitale offline, testate trimestralmente |
| **Operazioni critiche** | Disponibili 24/7 con accesso ridondante |
| **Operazioni standard** | Disponibili 24/7 dove a supporto di infrastrutture orientate ai clienti; minimo orario lavorativo per le altre |
| **Procedure di riferimento** | Disponibili su richiesta |

### Pacchetto offline di emergenza

Per i servizi critici, l'organizzazione DEVE mantenere un pacchetto offline contenente, come minimo:

- Procedura di attivazione del disaster recovery.
- Procedura di accesso break-glass / accesso di emergenza.
- Procedura di accesso alla rete principale.
- Procedure di ripristino del backup per i sistemi critici.

**Archiviazione e accesso**:

- **Ubicazione primaria**: [Specificare: Cassaforte chiusa nel locale server / armadio ignifugo in ufficio / struttura sicura fuori sede]
- **Ubicazione di backup**: [Specificare: Cassaforte sicura a casa dell'IT Operations Manager / struttura di backup fuori sede]
- **Custode**: IT Operations Manager ([Nome o "Detentore attuale: vedere lista contatti"])
- **Autorizzazione all'accesso**: RSSI, AD, IT Operations Manager e [contatti di emergenza designati]
- **Procedura di accesso**: Busta break-glass o contenitore sigillato; accesso registrato con data, accedente e motivazione

La validità DEVE essere verificata **trimestralmente** con una lista di controllo registrata che confermi l'allineamento delle versioni con il repository autorevole.

**Audit annuale**: Durante l'audit interno annuale, il pacchetto offline DEVE essere aperto e verificato rispetto al repository autorevole (corrispondenza al 100% delle versioni richiesta).

---

## Controllo versioni e approvazione

### Documenti di policy

- I documenti di policy sono soggetti a modifiche come risultato del processo di miglioramento continuo.
- Le modifiche ai documenti di policy vengono apportate dal team di gestione della sicurezza delle informazioni e approvate dal team di revisione della Direzione.
- La cronologia del controllo versioni è mantenuta, registrando come minimo: autore, data, descrizione della modifica e nuovo numero di versione.

### Documenti e registrazioni operative

- I documenti e le registrazioni operative vengono aggiornati dal proprietario del processo come parte delle operazioni quotidiane e secondo necessità.
- La cronologia del controllo versioni è mantenuta, registrando come minimo: autore, data, descrizione della modifica e nuovo numero di versione.
- Solo l'ultima versione approvata DEVE essere presentata agli utenti.
- Le versioni precedenti DEVONO essere archiviate (non eliminate) per la traccia di audit.
- Gli aggiornamenti DEVONO essere notificati al personale coinvolto.

---

## Revisione e manutenzione delle procedure

### Calendario di revisione

| Tipo di revisione | Frequenza | Ambito |
|------------------|-----------|--------|
| **Revisione programmata** | Annuale (minimo) | Tutte le procedure |
| **Revisione post-incidente** | Dopo un incidente pertinente | Procedure interessate |
| **Revisione attivata da cambiamenti** | Dopo modifiche al sistema | Procedure interessate |
| **Revisione normativa** | Dopo cambiamenti normativi | Procedure interessate |

### Attività di revisione

- Verificare l'accuratezza rispetto ai sistemi e ai processi attuali.
- Aggiornare per i cambiamenti tecnologici e del personale.
- Migliorare in base al feedback degli utenti e alle lezioni apprese.
- Allineare con i requisiti di sicurezza attuali.
- Aggiornare i riferimenti ai documenti correlati.

### Miglioramento continuo e feedback degli utenti

Il personale che utilizza le procedure DEVE segnalare:

- **Imprecisioni**: Passaggi che non corrispondono ai sistemi attuali o producono risultati inattesi.
- **Ambiguità**: Istruzioni poco chiare o prerequisiti mancanti.
- **Miglioramenti**: Suggerimenti per l'efficienza o la chiarezza.

**Meccanismo di feedback**: [Specificare: E-mail al responsabile della procedura, ticket in [sistema], funzione di commento nel repository dei documenti, sondaggio trimestrale sugli utenti delle procedure].

**Gestione del feedback**:

- Tutto il feedback viene registrato e revisionato dal responsabile della procedura entro **14 giorni**.
- Il feedback viene incorporato nella prossima revisione programmata o affrontato immediatamente se critico.
- Il mittente viene notificato della disposizione (accettato / rinviato / rifiutato con motivazione).

### Test delle procedure

Le procedure critiche DEVONO essere testate a intervalli definiti:

| Tipo di procedura | Requisito di test |
|------------------|--------------------|
| **Disaster recovery** | Test completo annuale; esercitazione tabletop trimestrale |
| **Risposta agli incidenti** | Esercitazione semestrale |
| **Backup e ripristino** | Test di ripristino mensile |
| **Accesso di emergenza** | Test break-glass annuale |
| **Operazioni critiche** | Dopo cambiamenti significativi |

I test DEVONO essere documentati, inclusi: data e partecipanti al test, scenario di test, risultati (riuscito/parzialmente riuscito/non riuscito), problemi identificati e azioni di rimedio.

**Classificazione dei risultati dei test**:

- **Riuscito**: Procedura completata come scritto con i risultati attesi; nessun rimedio richiesto.
- **Parzialmente riuscito**: Procedura completata con deviazioni minori o soluzioni alternative; sono necessari aggiornamenti ma la procedura è utilizzabile.
- **Non riuscito**: La procedura non ha potuto essere completata come scritto, o ha prodotto un risultato errato; è necessaria una revisione immediata prima del prossimo utilizzo.

**Azione in caso di fallimento del test**:

- Procedura contrassegnata come "In revisione" nel repository (flag visibile agli utenti).
- Rivista entro **14 giorni** per le procedure critiche, **30 giorni** per quelle non critiche.
- Ritestata dopo la revisione prima che venga ripristinato lo stato "Approvato".

---

## Metriche di documentazione delle procedure

L'organizzazione DEVE monitorare le seguenti metriche di documentazione delle procedure:

| Metrica | Obiettivo | Frequenza di revisione |
|---------|-----------|------------------------|
| **Completezza dell'inventario delle procedure** (tutte le categorie obbligatorie documentate) | 100% | Trimestrale |
| **Validità delle revisioni** (procedure revisionate entro il periodo programmato) | 100% | Trimestrale |
| **Conformità agli standard di documentazione** (le procedure campionate soddisfano gli elementi obbligatori) | 100% | Annuale (tramite campionamento di audit interno) |
| **Tasso di completamento dei test** (procedure critiche testate per calendario) | 100% | Trimestrale |
| **Completamento della formazione** (operatori di procedure critiche formati) | 100% | Trimestrale |
| **Tasso di successo dei test delle procedure** | ≥95% | Annuale |

Le metriche che superano gli obiettivi DEVONO essere escalate all'RSSI e segnalate alla prossima Revisione della Direzione.

---

## Gestione dei documenti

### Esempi di registrazioni

Le registrazioni sono prove di un evento e vengono utilizzate per la gestione operativa e l'audit. Includono, ma non si limitano a:

- Verbali di riunione.
- Registrazioni di formazione.
- Report di audit.
- Report di incidenti.
- Registrazioni dei cambiamenti.
- Registrazioni delle valutazioni del rischio.

### Documenti e registrazioni obsoleti

**Archiviazione (richiesta per scopi di audit/legali/normativi)**:

- I documenti e le registrazioni obsoleti DEVONO essere archiviati in conformità ai requisiti di conservazione dei dati:
  - **Registrazioni operative** (registri dei cambiamenti, report di incidenti): **3 anni** dopo l'obsolescenza.
  - **Prove di audit** (cronologia delle versioni delle procedure): **7 anni** dopo l'obsolescenza.
  - **Legale/normativo** (prove di conformità): Per il consulente legale o requisito normativo (tipicamente **7–10 anni**).
- I documenti archiviati vengono rimossi dall'accessibilità generale; accessibili solo al personale autorizzato di audit/conformità.

**Cancellazione sicura (non richiesta per la conservazione)**:

- I documenti e le registrazioni obsoleti che non sono richiesti per scopi di audit e/o legali e normativi DEVONO essere eliminati in modo sicuro per la Policy sulla classificazione e gestione delle informazioni entro **90 giorni** dalla determinazione dell'obsolescenza.

### Documenti di origine esterna

Le informazioni documentate di origine esterna determinate dall'organizzazione come necessarie per la pianificazione e l'operatività del Sistema di gestione della sicurezza delle informazioni DEVONO essere identificate e controllate (es. standard ISO, documentazione dei fornitori, orientamenti normativi).

**Requisiti di controllo per i documenti esterni**:

- **Identificazione**: I documenti esterni contrassegnati come "Esterno" nei metadati del repository.
- **Controllo versioni**: La versione del documento esterno e la data di pubblicazione vengono registrate.
- **Revisione**: Revisionati annualmente per la validità; le versioni aggiornate vengono ottenute quando disponibili.
- **Accessibilità**: Archiviati nello stesso repository dei documenti interni per facilità di riferimento.
- **Nessuna modifica**: I documenti esterni NON DEVONO essere modificati; le annotazioni o i riepiloghi vengono creati come documenti interni separati.

**Esempi**: Standard ISO/IEC 27001:2022, manuali di prodotto dei fornitori, orientamenti normativi dell'IFPDT, framework NIST.

### Classificazione dei documenti

I documenti DEVONO essere classificati in conformità alla Policy sulla classificazione e gestione delle informazioni.

**Classificazioni tipiche delle procedure**:

- **Pubblico**: Nessuno (le procedure sono dettagli operativi, non per divulgazione pubblica).
- **Interno**: Procedure operative standard, procedure amministrative non sensibili.
- **Confidenziale**: Procedure di sicurezza (risposta agli incidenti, gestione delle vulnerabilità), procedure DR, procedure break-glass, procedure contenenti credenziali o dettagli dell'architettura di sicurezza.

Le procedure classificate DEVONO essere gestite, archiviate e trasmesse in conformità al loro livello di classificazione. Le procedure riservate DEVONO avere accesso limitato (basato sul ruolo, necessità di sapere).

---

## Formazione e competenza

### Formazione degli operatori

Il personale DEVE essere formato sulle procedure pertinenti prima di eseguirle in modo autonomo.

- Le registrazioni di formazione DEVONO essere mantenute.
- La competenza DEVE essere verificata attraverso osservazione, valutazione o approvazione del supervisore.
- La formazione di aggiornamento DEVE essere fornita quando le procedure vengono significativamente aggiornate.
- La formazione incrociata DEVE essere implementata per le procedure critiche per evitare punti di guasto singoli.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della policy; standard delle procedure di sicurezza; approvazione delle procedure di sicurezza |
| **IT Operations Manager** | Proprietà delle procedure di infrastruttura; custode del pacchetto offline; coordinamento dei test delle procedure |
| **Responsabili delle procedure** | Accuratezza, aggiornamento e qualità delle procedure di propria competenza; conduzione delle revisioni; approvazione degli aggiornamenti |
| **Responsabili di backup delle procedure** | Competenti per revisionare e approvare gli aggiornamenti in assenza del responsabile primario; formati incrociati sul contenuto delle procedure; notificati di tutti gli aggiornamenti delle procedure (richiesto per le procedure critiche) |
| **Responsabile qualità / registrazioni** | Standard dei modelli di procedura; monitoraggio delle revisioni; governance del repository |
| **Tutto il personale tecnico** | Seguire le procedure; segnalare problemi e imprecisioni; suggerire miglioramenti |

---

## Prove

Le seguenti prove dimostrano la conformità a questa policy:

| # | Prova | Responsabile | Frequenza |
|---|-------|--------------|-----------|
| 1 | **Inventario delle procedure** con metadati (responsabile, versione, ultima revisione, prossima revisione) | Responsabile qualità / registrazioni | *Mantenuto continuamente; audit completo annuale; obiettivo: 100% con responsabile attuale* |
| 2 | **Procedure campionate** che soddisfano gli standard di documentazione (elementi obbligatori presenti) | Responsabile qualità / registrazioni | *Campione di 5–10 procedure revisionate annualmente durante l'audit interno* |
| 3 | **Registrazioni del completamento delle revisioni** (procedure revisionate entro il periodo programmato) | Responsabile qualità / registrazioni | *Monitorate trimestralmente; obiettivo: 100% entro il periodo di revisione* |
| 4 | **Risultati dei test delle procedure** (DR, risposta agli incidenti, ripristino del backup, break-glass) | IT Operations Manager | *Per calendario di test; conservati 3 anni* |
| 5 | **Registrazioni di formazione** per gli operatori delle procedure (completamento, verifica della competenza) | HR / IT Operations | *Per evento; obiettivo: 100% degli operatori di procedure critiche formati* |
| 6 | **Prove di controllo versioni** dal repository (traccia di audit delle modifiche) | Responsabile qualità / registrazioni | *Continua; verificata durante l'audit annuale* |
| 7 | **Registrazioni di verifica della validità del pacchetto offline di emergenza** | IT Operations Manager | *Trimestrale; lista di controllo firmata e conservata* |
| 8 | **Registrazioni di archiviazione e cancellazione dei documenti obsoleti** | Responsabile qualità / registrazioni | *Per evento; conservate per il calendario di conservazione* |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, tra cui: audit dell'inventario delle procedure, revisioni della qualità campionate, monitoraggio del completamento delle revisioni, analisi dei risultati dei test delle procedure, audit interni ed esterni e feedback al proprietario della policy.

## Eccezioni

Qualsiasi eccezione a questa policy DEVE essere approvata e registrata anticipatamente dal Responsabile della sicurezza delle informazioni, con accettazione documentata del rischio, controlli compensativi e una data di revisione definita (massimo 90 giorni, rinnovabile). Le eccezioni DEVONO essere riportate al team di revisione della Direzione. Le procedure critiche e le procedure di sicurezza NON DEVONO essere operate senza documentazione.

## Non conformità

Un dipendente che violi questa policy può essere soggetto a provvedimenti disciplinari, fino al licenziamento.

## Miglioramento continuo

Questa policy viene rivista e aggiornata come parte del processo di miglioramento continuo. Le revisioni DEVONO tenere conto dei cambiamenti agli standard operativi, ai cambiamenti tecnologici, ai risultati degli audit, ai cambiamenti normativi e alle lezioni apprese dagli incidenti e dai fallimenti dei test delle procedure.

---

# Aree dello standard ISO 27001 trattate

Policy sulle procedure operative documentate — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.36 Conformità a policy, regole e standard |
| Clausola 7.3 Consapevolezza | **5.37 Procedure operative documentate** |
| Clausola 7.5.1 Informazioni documentate — Generalità | 5.13 Etichettatura delle informazioni |
| Clausola 7.5.2 Creazione e aggiornamento dei documenti | 6.3 Consapevolezza, formazione e istruzione sulla sicurezza delle informazioni |
| Clausola 7.5.3 Controllo delle informazioni documentate | 6.4 Processo disciplinare |

**Framework normativo e legale**:

| Framework | Rilevanza |
|-----------|-----------|
| nLPD svizzera (revLPD) | Art. 8 — Misure tecniche e organizzative (le procedure documentate come misura organizzativa) |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati (processi documentati) |
| GDPR UE (ove applicabile) | Art. 5(2) — Principio di responsabilizzazione (le procedure documentate dimostrano la conformità); Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Controllo A.5.37 dell'Allegato A; Clausole 7.5.1, 7.5.2, 7.5.3 — Informazioni documentate |
| ISO/IEC 27002:2022 | Sezione 5.37 — Guida all'implementazione |
| NIST SP 800-53 Rev 5 | PL-2 (Piani di sicurezza del sistema e privacy), SA-5 (Documentazione del sistema), PS-1 (Policy e procedure) |
| CIS Controls v8 | Controllo 16 (Sicurezza del software applicativo — Salvaguardia 16.1: Stabilire e mantenere un processo di sviluppo sicuro delle applicazioni — richiede procedure documentate) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
