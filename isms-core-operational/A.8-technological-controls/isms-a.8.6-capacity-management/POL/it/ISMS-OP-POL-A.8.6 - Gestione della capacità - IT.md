<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.6-IT:operational:OP-POL:a.8.6 -->
**ISMS-OP-POL-A.8.6 — Gestione della capacità**

---

**Controllo del documento**

| Campo | Valore |
|-------|-------|
| **Titolo del documento** | Gestione della capacità |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.6 |
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

**Ciclo di revisione**: Annuale (allineato al ciclo di pianificazione della capacità)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- ISO/IEC 27001:2022 Controllo A.8.6 — Gestione della capacità
- ISO/IEC 27002:2022 Sezione 8.6 — Linee guida di implementazione per la gestione della capacità
- NIST SP 800-53 Rev 5 — AU-4 (Capacità di archiviazione del log di audit), CP-2(2) (Pianificazione della capacità), SC-5 (Protezione dal denial-of-service)
- ITIL 4 — Pratica di gestione della capacità e delle prestazioni

**Controlli Annex A correlati**:

| Controllo | Relazione con la gestione della capacità |
|---------|-------------------------------------|
| A.5.30–8.13–14 Continuità operativa e DR | Pianificazione della capacità del sito di ripristino; capacità di archiviazione dei backup |
| A.7.11 Servizi di supporto | Capacità dell'infrastruttura fisica (alimentazione, raffreddamento, spazio rack) |
| A.8.1–7–18–19 Sicurezza degli endpoint | Monitoraggio delle risorse degli endpoint e capacità del parco macchine |
| A.8.8 Gestione delle vulnerabilità | Capacità degli strumenti di scansione; requisiti di risorse per il rilascio delle patch |
| A.8.9 Gestione della configurazione | Le configurazioni di base includono soglie di capacità |
| A.8.15 Registrazione | Pianificazione della capacità di archiviazione dei log e gestione della conservazione |
| A.8.16 Attività di monitoraggio | Le metriche di capacità come sottoinsieme del monitoraggio complessivo |
| A.8.20–22 Sicurezza di rete | Capacità di larghezza di banda e throughput di rete |

**Politiche interne correlate**:

- Politica delle attività di monitoraggio (A.8.16)
- Politica di continuità operativa e ripristino di emergenza (A.5.30–8.13–14)
- Politica di registrazione (A.8.15)
- Politica di sicurezza di rete (A.8.20–22)
- Politica di gestione delle modifiche (A.8.32)

---

# Politica di gestione della capacità

## Scopo

Lo scopo di questa politica è garantire che l'utilizzo delle risorse di elaborazione delle informazioni sia monitorato e adeguato in linea con i requisiti di capacità attuali e previsti, prevenendo le interruzioni del servizio causate dall'esaurimento delle risorse e supportando decisioni di investimento informate.

La gestione della capacità è sia una necessità operativa che un controllo di sicurezza. Una capacità insufficiente può causare interruzioni del servizio, degradare il monitoraggio della sicurezza, impedire la raccolta dei log di audit e creare condizioni sfruttabili da attacchi denial-of-service. La pianificazione proattiva della capacità garantisce che l'infrastruttura, le applicazioni e i servizi di supporto rimangano disponibili, performanti e sicuri.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative appropriate al rischio per proteggere la disponibilità e l'integrità dei sistemi che trattano dati personali. Dove l'organizzazione tratta dati di individui nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32 per garantire la continua disponibilità e resilienza dei sistemi di trattamento.

## Ambito

Questa politica si applica a tutte le risorse infrastrutturali, applicative e di servizio nell'ambito del SGSI che richiedono il monitoraggio e la pianificazione della capacità. Ciò include:

- **Risorse di elaborazione**: Server, macchine virtuali, container, istanze cloud (utilizzo di CPU e memoria).
- **Risorse di archiviazione**: Archiviazione su disco, archiviazione di database, archiviazione di backup, archiviazione di archivio, archiviazione dei log.
- **Risorse di rete**: Larghezza di banda, throughput, connessioni, capacità del load balancer, capacità delle query DNS.
- **Risorse applicative**: Utenti simultanei, tassi di transazione, limiti di frequenza delle API, profondità delle code dei messaggi.
- **Risorse di servizi cloud**: Quote dei servizi, limiti delle istanze, limiti delle chiamate API, capacità riservata.
- **Capacità delle licenze**: Licenze software, postazioni di abbonamento, utilizzo di licenze simultanee.
- **Infrastruttura fisica**: Capacità di alimentazione, capacità di raffreddamento, spazio rack (per A.7.11).

Tutti i dipendenti, i collaboratori esterni e i fornitori di servizi terzi con responsabilità per la gestione dell'infrastruttura, delle applicazioni o dei servizi.

**Fuori ambito**: Ottimizzazione delle prestazioni delle applicazioni e del codice (coperta dallo sviluppo sicuro); gestione dettagliata degli asset software e approvvigionamento delle licenze (coperto dalla gestione degli asset A.5.9); capacità fisica degli edifici non correlata all'elaborazione delle informazioni.

## Principio

L'organizzazione deve monitorare, prevedere e pianificare proattivamente i requisiti di capacità su tutte le risorse critiche. La gestione della capacità segue il principio della prevenzione rispetto alla reazione — è significativamente meno costoso e meno dirompente pianificare la crescita della capacità piuttosto che rispondere agli incidenti di esaurimento della capacità.

Le decisioni sulla capacità devono essere basate sui dati, sulla base delle tendenze di utilizzo misurate e delle proiezioni di crescita aziendale documentate, non su supposizioni o aneddoti. Le risorse devono mantenere un margine sufficiente per assorbire picchi di domanda imprevisti senza degradazione del servizio.

---

## Monitoraggio delle risorse

### Copertura del monitoraggio

Tutti i sistemi e i servizi di produzione devono avere il monitoraggio della capacità abilitato. Il monitoraggio deve coprire, come minimo, le categorie di risorse elencate nella sezione Ambito.

**Requisiti di copertura**:

| Ambiente | Obiettivo di copertura | Frequenza di monitoraggio |
|-------------|-----------------|----------------------|
| Sistemi di produzione | 100% | Ogni 5 minuti o meno |
| Ripristino di emergenza / standby | 100% | Ogni 15 minuti o meno |
| Non di produzione (staging, test) | 90% | Ogni 15 minuti o meno |

Il monitoraggio deve essere implementato utilizzando [Piattaforma di monitoraggio] (ad es. Prometheus, Zabbix, Datadog, Azure Monitor, CloudWatch o equivalente). La piattaforma deve essere documentata nell'inventario degli asset con il suo modello di hosting, la residenza dei dati e i controlli degli accessi amministrativi.

### Metriche monitorate

Le seguenti metriche devono essere raccolte per ogni tipo di risorsa applicabile:

| Tipo di risorsa | Metriche | Unità |
|---------------|---------|-------|
| **CPU** | Utilizzo (medio, picco), media del carico, ready time | Percentuale, conteggio |
| **Memoria** | Utilizzo, utilizzo dello swap, memoria disponibile | Percentuale, GB |
| **Archiviazione** | Capacità utilizzata, capacità disponibile, tasso di crescita, IOPS | GB/TB, percentuale, ops/sec |
| **Rete** | Utilizzo della larghezza di banda, perdita di pacchetti, latenza, conteggio delle connessioni | Mbps/Gbps, percentuale, ms, conteggio |
| **Applicazione** | Utenti simultanei, sessioni attive, tasso di transazione, profondità della coda | Conteggio, transazioni/sec |
| **Quote cloud** | Utilizzo dei limiti di servizio per regione e account | Percentuale della quota |
| **Licenze** | Allocazioni attive rispetto ai diritti totali | Conteggio, percentuale |

### Conservazione delle metriche

- **Metriche grezze**: Minimo 30 giorni alla risoluzione completa (per l'indagine sugli incidenti).
- **Metriche aggregate**: Minimo 12 mesi a granularità oraria o giornaliera (per l'analisi delle tendenze).
- **Sintesi storiche**: Minimo 36 mesi a granularità mensile (per la pianificazione strategica).

I dati delle metriche devono essere protetti da modifiche o cancellazioni non autorizzate. Dove le metriche alimentano il monitoraggio della sicurezza (A.8.16), si applicano anche i requisiti di integrità dei log della Politica di registrazione (A.8.15).

---

## Framework delle soglie e alerting

### Livelli di soglia

Tutte le risorse monitorate devono avere soglie di capacità definite a tre livelli:

| Livello | Scopo | Intervallo tipico | Azione |
|-------|---------|---------------|--------|
| **Avviso** | Indicazione precoce di pressione sulla capacità | 70–80% di utilizzo | Revisione della pianificazione della capacità; analisi della tendenza di crescita |
| **Critico** | Capacità prossima all'esaurimento | 85–90% di utilizzo | Indagine immediata; avvio dell'espansione della capacità o mitigazione del carico |
| **Massimo** | Esaurimento imminente o in corso della risorsa | 95%+ di utilizzo | Risposta d'emergenza; attivazione della gestione degli incidenti se impatto sul servizio |

I valori esatti delle soglie devono essere definiti per tipo di risorsa e classificazione del sistema, documentati nella piattaforma di monitoraggio e revisionati trimestralmente. Le soglie devono essere ottimizzate in base ai tassi di falsi positivi, ai pattern del carico di lavoro e agli incidenti quasi-mancati.

**Soglie specifiche per l'archiviazione**: devono anche considerare il tasso di crescita: se si prevede che l'archiviazione raggiunga il 95% entro 30 giorni al tasso di consumo attuale, deve essere generato un alert di avviso indipendentemente dalla percentuale corrente.

### Configurazione degli alert

Gli alert di soglia della capacità devono essere configurati con:

- **Routing**: Alert consegnati al team delle operazioni responsabile tramite [Strumento di alerting] (ad es. PagerDuty, Opsgenie, ServiceNow o equivalente).
- **Tempo di consegna**: Alert consegnati entro 5 minuti dal rilevamento della violazione della soglia.
- **Escalation**: Alert di avviso non riconosciuti escalati dopo 4 ore; alert critici non riconosciuti escalati dopo 30 minuti.
- **Deduplicazione**: Alert ripetuti per la stessa risorsa e soglia soppressi per prevenire l'affaticamento da alert; ri-alert se la condizione persiste oltre la finestra di soppressione.
- **Integrazione**: Gli alert critici e massimi devono creare incidenti automaticamente in [Strumento ITSM] (ad es. ServiceNow, Jira Service Management o equivalente).

### Risposta agli alert

| Livello di alert | SLA di risposta | Azione di risposta |
|-------------|--------------|-----------------|
| **Avviso** | Riconosciuto entro 4 ore (orario lavorativo) | Rivedere i dati delle tendenze; aggiornare la previsione della capacità; pianificare l'espansione se necessario |
| **Critico** | Riconosciuto entro 30 minuti | Investigare la causa principale; implementare la mitigazione immediata (riduzione del carico, scalabilità temporanea); avviare l'espansione della capacità |
| **Massimo** | Riconosciuto entro 15 minuti | Eseguire la risposta d'emergenza; attivare la gestione degli incidenti per A.5.24–28 se impatto sul servizio; implementare l'espansione d'emergenza della capacità |

---

## Previsione della capacità

### Orizzonti di previsione

L'organizzazione deve sviluppare e mantenere previsioni della capacità a tre orizzonti:

| Orizzonte | Arco temporale | Scopo | Frequenza di aggiornamento |
|---------|-----------|---------|------------------|
| **Breve termine** | 3–6 mesi | Pianificazione tattica; approvvigionamento immediato | Mensile |
| **Medio termine** | 6–12 mesi | Pianificazione del budget; rinnovi dei contratti | Trimestrale |
| **Lungo termine** | 12–24 mesi | Pianificazione strategica; decisioni di migrazione al data center o al cloud | Annuale |

### Metodologia di previsione

Le previsioni devono basarsi su:

- **Analisi delle tendenze storiche**: Estrapolazione dai dati di utilizzo misurati (minimo 6 mesi di dati richiesti per tendenze affidabili).
- **Proiezioni di crescita aziendale**: Input dai proprietari delle applicazioni e dalle unità aziendali su progetti pianificati, crescita degli utenti, aumento del volume dei dati e nuovi lanci di servizi.
- **Pattern stagionali**: Identificazione e modellazione delle variazioni periodiche della domanda (elaborazione di fine mese, cicli di reporting annuale, campagne di marketing).
- **Modifiche pianificate**: Rilasci pianificati, migrazioni, dismissioni e modifiche all'infrastruttura.

Dove i dati storici sono insufficienti (nuovi sistemi o servizi), devono essere utilizzate stime conservative con revisioni più frequenti durante i primi 6 mesi di funzionamento.

### Accuratezza delle previsioni

- **Accuratezza target**: Le previsioni devono essere entro +/-15% dell'utilizzo effettivo (misurato trimestralmente).
- **Nuovi sistemi (primi 6 mesi)**: Accuratezza +/-30% accettabile mentre si stabiliscono le baseline.
- **Carichi di lavoro ad alta variabilità**: Accuratezza +/-25% con giustificazione documentata.
- **Deviazioni superiori al 15%**: Analisi della causa principale richiesta entro 10 giorni lavorativi; risultati documentati e incorporati nel ciclo di previsione successivo.

---

## Policy di auto-scalabilità

Dove l'organizzazione opera infrastrutture cloud, l'auto-scalabilità deve essere configurata per i carichi di lavoro con pattern di domanda variabile.

### Requisiti di auto-scalabilità

| Requisito | Standard |
|-------------|----------|
| **Trigger di scalabilità** | Utilizzo CPU, utilizzo memoria, tasso di richieste, profondità della coda o metriche applicative personalizzate |
| **Soglia di scale-out** | Definita per carico di lavoro; tipicamente 70–80% della metrica target per 3–5 minuti sostenuti |
| **Soglia di scale-in** | Definita per carico di lavoro; tipicamente 30–40% della metrica target per 10–15 minuti sostenuti |
| **Istanze minime** | Almeno 2 per i carichi di lavoro di produzione (disponibilità); almeno 1 per non di produzione |
| **Istanze massime** | Definite per carico di lavoro per prevenire sforamenti dei costi; allineate ai vincoli di budget |
| **Periodo di cooldown** | Minimo 5 minuti tra le azioni di scalabilità per prevenire oscillazioni |

### Governance dell'auto-scalabilità

- Le configurazioni di auto-scalabilità devono essere documentate e sotto controllo versione.
- Le modifiche alle policy di auto-scalabilità per i carichi di lavoro di produzione devono seguire il processo di gestione delle modifiche (A.8.32).
- I limiti massimi delle istanze devono essere revisionati trimestralmente e allineati ai budget approvati.
- Gli eventi di auto-scalabilità devono essere registrati e revisionati mensilmente per opportunità di ottimizzazione.
- **Guardrail dei costi**: I limiti di spesa mensile massima devono essere configurati a livello di account o sottoscrizione cloud. L'auto-scalabilità che supererebbe il limite di spesa deve attivare un alert al Responsabile dell'infrastruttura e al delegato CFO.

Dove l'auto-scalabilità non è disponibile o non è appropriata (infrastruttura on-premises, servizi a capacità fissa), le procedure manuali di espansione della capacità devono essere documentate con i tempi di approvvigionamento e rilascio definiti.

---

## Ottimizzazione della capacità e dei costi

La gestione della capacità deve bilanciare disponibilità, prestazioni e costi. L'over-provisioning spreca budget; l'under-provisioning crea rischi. L'organizzazione deve ottimizzare attivamente l'allocazione delle risorse in base ai dati di utilizzo misurati.

### Strategie di ottimizzazione

| Strategia | Descrizione | Applicabilità |
|----------|-------------|---------------|
| **Right-sizing** | Eliminare le risorse over-provisioned dove l'utilizzo sostenuto è inferiore al 40% | Tutti gli ambienti |
| **Capacità riservata** | Acquistare istanze riservate o sconti per uso committed per i carichi di lavoro stazionari (ad es. AWS RI, Azure RI, GCP CUD) | Ambienti cloud con baseline prevedibile |
| **Istanze spot/preemptibili** | Utilizzare per carichi di lavoro non critici e interrompibili (elaborazione batch, test, sviluppo) | Ambienti cloud con carichi di lavoro fault-tolerant |
| **Auto-scalabilità** | Allineare la capacità alla domanda in tempo reale per evitare di pagare per risorse inattive | Ambienti cloud con domanda variabile |
| **Ciclo di vita dell'archiviazione** | Spostare i dati accessibili raramente su classi di archiviazione a costo inferiore (ad es. S3 Glacier, Azure Cool/Archive, GCS Nearline/Coldline) | Tutta l'archiviazione con pattern di accesso definiti |

### Revisione trimestrale dei costi

Il Responsabile dell'infrastruttura deve condurre una revisione trimestrale dei costi che include:

- Identificazione delle risorse over-provisioned (utilizzo sostenuto costantemente inferiore al 40%).
- Valutazione dei rapporti tra capacità riservata e spesa on-demand.
- Valutazione delle opportunità di tiering dell'archiviazione.
- Reportistica delle azioni di ottimizzazione dei costi intraprese e dei risparmi realizzati.

I risultati dell'ottimizzazione dei costi devono essere inclusi nel rapporto trimestrale di revisione della capacità presentato al CIO, RSSI e delegato CFO.

---

## Capacità e obiettivi di livello di servizio

Le soglie di capacità devono essere allineate agli obiettivi di livello di servizio (SLO) per garantire che i vincoli di capacità non degradino la qualità del servizio al di sotto dei livelli concordati. La connessione tra l'utilizzo delle risorse e le prestazioni del servizio deve essere documentata per ogni servizio critico.

### Allineamento agli SLO

| Tipo di servizio | SLO tipico | Allineamento delle soglie di capacità |
|--------------|-------------|------------------------------|
| Applicazione web | Disponibilità 99,9%, latenza p95 <500ms | La CPU deve rimanere al di sotto del 75% medio (la latenza degrada sopra il 75%) |
| Servizio API | Disponibilità 99,95%, latenza p95 <200ms | CPU al di sotto del 70% medio; memoria al di sotto dell'80% |
| Database | Disponibilità 99,99%, risposta alle query <50ms | IOPS al di sotto dell'80% massimo; connessioni al di sotto del 90% massimo |
| Coda di messaggi | Disponibilità 99,9%, ritardo di elaborazione <5s | Profondità della coda al di sotto dell'80% massimo; capacità del consumer mantenuta |

Dove l'utilizzo misurato delle risorse si avvicina ai livelli che degraderebbero le prestazioni degli SLO, le soglie di capacità devono essere abbassate per attivare un intervento più precoce. L'allineamento agli SLO deve essere revisionato trimestralmente come parte del processo di revisione della capacità.

---

## Reportistica della capacità

### Cadenza di reportistica

| Rapporto | Destinatari | Frequenza | Contenuto |
|--------|----------|-----------|---------|
| **Dashboard operativa** | Operazioni IT | Continuamente (tempo reale) | Utilizzo attuale, alert attivi, indicatori di tendenza |
| **Rapporto mensile della capacità** | Leadership IT, Responsabile dell'infrastruttura | Mensile | Sintesi dell'utilizzo, cronologia degli alert, punti salienti delle previsioni, azioni sulla capacità intraprese |
| **Revisione trimestrale della capacità** | CIO, RSSI, delegato CFO | Trimestrale | Previsioni, piani di espansione, impatto sul budget, scorecard di salute, metriche di conformità |
| **Piano annuale della capacità** | Direzione generale | Annuale | Piano strategico con proiezioni pluriennali, requisiti di investimento, valutazione del rischio |

### Requisiti del contenuto dei rapporti

I rapporti mensili e trimestrali devono includere:

- Utilizzo attuale per tipo di risorsa (medio, picco, direzione della tendenza).
- Conteggio delle violazioni delle soglie e tempi di risposta.
- Incidenti legati alla capacità (conteggio, gravità, sintesi della causa principale).
- Misurazione dell'accuratezza delle previsioni (effettivo vs. previsto).
- Modifiche pianificate alla capacità (espansioni, dismissioni, migrazioni).
- Utilizzo del budget per le spese relative alla capacità.

I rapporti devono essere generati dai dati della [Piattaforma di monitoraggio]. Il piano annuale della capacità deve essere approvato dal CIO e incluso nella revisione della direzione per ISO 27001 Clausola 9.3.

---

## Gestione della capacità di archiviazione

La capacità di archiviazione richiede un'attenzione specifica a causa delle sue caratteristiche di crescita continua e dell'impatto diretto sulla sicurezza dell'esaurimento dell'archiviazione (perdita dei log di audit, impossibilità di scrivere eventi di sicurezza, guasti delle applicazioni).

### Archiviazione dei log

- La capacità di archiviazione dei log deve essere pianificata in coordinamento con la Politica di registrazione (A.8.15) per garantire che i requisiti di conservazione possano essere soddisfatti senza esaurimento dell'archiviazione.
- L'archiviazione dei log deve avere una soglia di avviso dedicata al 70% e una soglia critica all'85%.
- Se l'archiviazione dei log raggiunge la soglia critica, la rotazione automatizzata dei log o l'archiviazione devono essere attivate prima che si verifichi la perdita di dati.
- Il tasso di crescita dell'archiviazione dei log deve essere monitorato e previsto mensilmente.

### Archiviazione dei database

- La crescita dell'archiviazione dei database deve essere monitorata e prevista separatamente dall'archiviazione dei file.
- Le attività di manutenzione dei database (vacuum, ricostruzione degli indici, archiviazione) devono essere considerate nella pianificazione della capacità.
- Le soglie di archiviazione dei database devono tenere conto dell'overhead operativo (tabelle temporanee, log delle transazioni, lag della replica).

### Archiviazione dei backup

- La capacità di archiviazione dei backup deve essere pianificata per contenere set di backup completi per il periodo di conservazione richiesto secondo la politica di backup (A.5.30–8.13–14).
- La crescita nell'archiviazione dei backup deve essere prevista in base alla crescita dei dati di produzione e alle modifiche alla politica di conservazione.

---

## Gestione della capacità delle licenze

La capacità delle licenze software deve essere monitorata per prevenire violazioni di conformità e interruzioni del servizio causate dall'esaurimento delle licenze.

### Requisiti di monitoraggio delle licenze

| Requisito | Standard |
|-------------|----------|
| **Inventario delle licenze** | Mantenuto nell'inventario degli asset (A.5.9) con conteggi dei diritti, date di scadenza e tipo di licenza (simultanea, nominativa, dispositivo) |
| **Monitoraggio dell'utilizzo** | Utilizzo attivo monitorato rispetto ai diritti per tutto il software critico |
| **Soglia di avviso** | Alert quando l'utilizzo raggiunge l'80% dei diritti |
| **Soglia critica** | Alert quando l'utilizzo raggiunge il 90% dei diritti |
| **Frequenza di revisione** | Revisione trimestrale dell'utilizzo; pianificazione annuale del rinnovo |

### Pianificazione del rinnovo delle licenze

I rinnovi delle licenze devono essere monitorati con un tempo di preavviso minimo di 90 giorni prima della scadenza. I requisiti di capacità delle licenze devono essere inclusi nella previsione della capacità a medio termine (6–12 mesi) e allineati ai cicli di pianificazione del budget.

---

## Risposta agli incidenti di capacità

Quando l'esaurimento della capacità causa o minaccia di causare un impatto sul servizio, deve essere attivato il processo di gestione degli incidenti dell'organizzazione (A.5.24–28).

### Procedure specifiche per gli incidenti di capacità

| Scenario | Classificazione | Risposta immediata |
|----------|---------------|-------------------|
| **Soglia di avviso sostenuta per più di 24 ore** | Evento di capacità (non incidente) | Rivedere e pianificare; nessuna azione d'emergenza richiesta |
| **Soglia critica sostenuta per più di 1 ora** | Incidente Priorità 3 | Implementare la mitigazione del carico; avviare l'espansione d'emergenza della capacità |
| **Degradazione del servizio per capacità** | Incidente Priorità 2 | Scalabilità d'emergenza o riduzione del carico; notifica ai clienti se impatto esterno |
| **Interruzione del servizio per esaurimento della capacità** | Incidente Priorità 1 | Risposta completa agli incidenti; approvvigionamento d'emergenza; revisione post-incidente obbligatoria |

### Revisione post-incidente

Tutti gli incidenti legati alla capacità classificati Priorità 1 o Priorità 2 devono essere sottoposti a revisione post-incidente entro 5 giorni lavorativi. La revisione deve determinare:

- Perché il monitoraggio e la previsione non hanno prevenuto l'incidente.
- Se le soglie richiedono aggiustamenti.
- Se la metodologia di previsione richiede miglioramenti.
- Quale espansione della capacità è necessaria per prevenire il ripetersi.
- Se l'incidente ha evidenziato una lacuna nella copertura del monitoraggio.

I risultati devono essere monitorati nel registro dei miglioramenti della capacità fino al completamento della remediation.

---

## Resilienza al denial-of-service

La pianificazione della capacità deve incorporare la resilienza alle condizioni di denial-of-service (DoS/DDoS). La capacità non deve essere pianificata esclusivamente per i carichi medi o di picco previsti — deve essere mantenuto un margine per assorbire picchi di domanda imprevisti, inclusi quelli causati da attività malevole.

### Requisiti di margine

| Risorsa | Margine minimo al picco | Motivazione |
|----------|--------------------------|-----------|
| **CPU** | 20% | Assorbire picchi di traffico senza degradazione |
| **Memoria** | 20% | Prevenire guasti out-of-memory sotto carico |
| **Archiviazione** | 3 mesi al tasso di crescita attuale | Tempo di approvvigionamento e provisioning |
| **Larghezza di banda di rete** | 30% durante l'orario lavorativo | Assorbire picchi di traffico; accogliere l'overhead di mitigazione DDoS |

Dove i servizi rivolti all'esterno sono esposti al rischio DDoS, devono essere implementate misure di mitigazione aggiuntive (CDN, servizi di protezione DDoS, limitazione della frequenza) in coordinamento con la Politica di sicurezza di rete (A.8.20–22).

---

## Comitato di pianificazione della capacità

Le organizzazioni con infrastrutture complesse o su larga scala (50+ server o carichi di lavoro cloud equivalenti) dovrebbero istituire un Comitato di pianificazione della capacità per coordinare la gestione della capacità tra i team e garantire l'allineamento tra le decisioni tecniche sulla capacità e la strategia aziendale.

### Struttura del comitato

| Ruolo | Funzione |
|------|----------|
| **Responsabile dell'infrastruttura** (presidente) | Stabilisce l'agenda; presenta i dati e le previsioni della capacità |
| **Architetto cloud / Ingegnere della piattaforma** | Tendenze della capacità cloud, efficacia dell'auto-scalabilità, ottimizzazione dei costi |
| **Amministratore di database** | Crescita dell'archiviazione dei database, capacità delle prestazioni, capacità della replica |
| **Proprietari delle applicazioni** (a rotazione) | Proiezioni di crescita aziendale, lanci pianificati, cambiamenti della domanda |
| **Delegato CFO** | Revisione del budget, approvazione degli investimenti, analisi costi-benefici |

### Cadenza delle riunioni

Il Comitato di pianificazione della capacità deve riunirsi trimestralmente. L'agenda deve includere:

- Revisione delle previsioni della capacità e dell'accuratezza delle previsioni.
- Approvazione delle espansioni di capacità pianificate e dei budget associati.
- Revisione degli incidenti legati alla capacità e degli eventi quasi-mancati.
- Discussione sull'impatto del budget e opportunità di ottimizzazione dei costi.
- Identificazione dei rischi emergenti di capacità dalla crescita aziendale o dai cambiamenti tecnologici.

I verbali delle riunioni devono essere conservati come evidenza di governance (Evidenza #10).

Dove l'organizzazione è troppo piccola per giustificare un comitato formale, la riunione trimestrale di revisione della capacità tra il Responsabile dell'infrastruttura e il CIO deve svolgere questa funzione di governance.

---

## Definizioni

| Termine | Definizione |
|------|------------|
| **Auto-scalabilità** | Aggiustamento automatizzato delle risorse di elaborazione (istanze, container) in risposta alla domanda misurata, tipicamente negli ambienti cloud |
| **Previsione della capacità** | Proiezione dei requisiti futuri delle risorse basata sulle tendenze storiche, sui piani di crescita aziendale e sui pattern stagionali |
| **Margine di capacità** | Capacità inutilizzata rimanente disponibile per la crescita o la domanda imprevista al di sopra dell'utilizzo di picco attuale |
| **Soglia di capacità** | Un livello di utilizzo definito che attiva alert o azioni quando viene superato (avviso, critico o massimo) |
| **Periodo di cooldown** | Intervallo minimo tra le azioni di auto-scalabilità per prevenire una rapida oscillazione tra scale-in e scale-out |
| **DDoS** | Distributed denial-of-service — un attacco che tenta di sopraffare un servizio inondandolo di traffico da più fonti |
| **Tasso di crescita** | Il tasso con cui il consumo di risorse aumenta nel tempo, tipicamente misurato come percentuale al mese o unità assolute al mese |
| **IOPS** | Input/output operations per second — una metrica delle prestazioni di archiviazione che misura il tasso delle operazioni di lettura e scrittura |
| **Riduzione del carico** | Riduzione deliberata del carico del sistema durante la pressione sulla capacità dando priorità ai carichi di lavoro non essenziali o limitando la frequenza delle richieste |
| **Right-sizing** | Aggiustamento dell'allocazione delle risorse per corrispondere all'utilizzo effettivo, eliminando le risorse over-provisioned o under-provisioned |
| **Scale-in** | Riduzione del numero di risorse allocate (istanze, container) quando la domanda diminuisce |
| **Scale-out** | Aumento del numero di risorse allocate (istanze, container) quando la domanda aumenta |
| **SLO** | Obiettivo di livello di servizio — un target misurabile per le prestazioni del servizio (ad es. disponibilità, latenza) che la capacità deve supportare |
| **Utilizzo** | La proporzione della capacità totale di una risorsa attualmente in uso, tipicamente espressa come percentuale |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|------|-----------------|
| **RSSI** | Proprietà della politica; garantire la capacità per i sistemi di sicurezza (SIEM, registrazione, EDR); verifica della conformità per A.8.6; escalation dei rischi di capacità che influenzano la postura di sicurezza; revisione annuale della politica |
| **CIO / Direttore IT** | Responsabilità complessiva per l'efficacia del programma di gestione della capacità; approvazione dei piani di espansione della capacità; pianificazione strategica della capacità; supervisione del budget |
| **CFO / Finanza** | Approvazione dei budget di gestione della capacità (CapEx e OpEx); revisione finanziaria degli investimenti nella capacità; supervisione dell'ottimizzazione dei costi |
| **Responsabile dell'infrastruttura / Responsabile delle operazioni IT** | Monitoraggio quotidiano della capacità e risposta agli alert; configurazione e ottimizzazione delle soglie; previsione della capacità; reportistica; mitigazione d'emergenza della capacità |
| **Architetto cloud / Ingegnere della piattaforma** | Progettazione e implementazione delle policy di auto-scalabilità; gestione delle quote cloud; ottimizzazione dei costi per le risorse cloud; pianificazione delle istanze riservate |
| **Proprietari delle applicazioni / Proprietari dei sistemi** | Proiezioni di crescita aziendale per la pianificazione della capacità; partecipazione alle riunioni di revisione della capacità; budget per la capacità specifica dell'applicazione |
| **Responsabile della sicurezza delle informazioni** | Manutenzione della politica; revisione delle eccezioni; reportistica della conformità; coordinamento dell'audit; monitoraggio delle non conformità |
| **Tutto il personale** | Segnalazione dei problemi di prestazioni osservati; rispetto delle politiche di utilizzo approvato delle risorse |

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa politica:

| # | Evidenza | Proprietario | Frequenza | Conservazione |
|---|----------|-------|-----------|-----------|
| 1 | **Rapporto sulla copertura del monitoraggio** che mostra la percentuale di sistemi di produzione e non di produzione monitorati | Responsabile dell'infrastruttura | Mensile | 3 anni |
| 2 | **Documentazione della configurazione delle soglie** per tutte le risorse monitorate | Responsabile dell'infrastruttura | Revisionata trimestralmente; aggiornata secondo necessità | Corrente + 2 anni |
| 3 | **Cronologia degli alert e registri delle risposte** (alert generati, riconosciuti, risolti, tempi di risposta) | Operazioni IT | Continuamente | 3 anni |
| 4 | **Rapporti mensili sulla capacità** con sintesi dell'utilizzo e dati sulle tendenze | Responsabile dell'infrastruttura | Mensile | 3 anni |
| 5 | **Previsioni trimestrali della capacità** con misurazioni dell'accuratezza (effettivo vs. previsto) | Responsabile dell'infrastruttura | Trimestrale | 3 anni |
| 6 | **Piano annuale della capacità** con proiezioni strategiche e requisiti di investimento | CIO / Responsabile dell'infrastruttura | Annuale | 5 anni |
| 7 | **Registri di configurazione dell'auto-scalabilità** e cronologia delle modifiche | Architetto cloud / Ingegnere della piattaforma | Mantenuto continuamente; revisionato trimestralmente | Vita della configurazione + 1 anno |
| 8 | **Registri degli incidenti legati alla capacità** e rapporti di revisione post-incidente | Operazioni IT / Responsabile dell'infrastruttura | Per incidente | 3 anni |
| 9 | **Inventario delle licenze e rapporti sull'utilizzo** che mostrano i diritti rispetto alle allocazioni attive | Operazioni IT / Procurement | Trimestrale | 3 anni |
| 10 | **Verbali delle riunioni del Comitato di pianificazione della capacità** o note delle riunioni di revisione della capacità | Responsabile dell'infrastruttura | Per riunione | 3 anni |
| 11 | **Registro delle eccezioni** per le eccezioni alla politica di capacità con approvazioni e controlli compensativi | Responsabile della sicurezza delle informazioni | Mantenuto continuamente; revisionato trimestralmente | Durata eccezione + 3 anni |
| 12 | **Rapporti sulle tendenze di crescita dell'archiviazione** (inclusa archiviazione log, database e backup) | Responsabile dell'infrastruttura | Mensile | 3 anni |
| 13 | **Rapporti di ottimizzazione dei costi** che documentano le azioni di right-sizing, le decisioni sulla capacità riservata e i risparmi realizzati | Responsabile dell'infrastruttura / Architetto cloud | Trimestrale | 3 anni |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso audit della copertura del monitoraggio, revisioni della configurazione delle soglie, valutazioni dell'accuratezza delle previsioni, puntualità della reportistica della capacità, audit interni ed esterni, e feedback al proprietario della politica.

**Metriche di conformità**:

| Metrica | Obiettivo | Frequenza di misurazione |
|--------|--------|-----------------------|
| Sistemi di produzione con monitoraggio della capacità abilitato | 100% | Mensile |
| Sistemi non di produzione con monitoraggio della capacità abilitato | >= 90% | Trimestrale |
| Risorse con soglie definite e documentate | >= 95% | Trimestrale |
| Alert di avviso riconosciuti entro 4 ore (orario lavorativo) | >= 90% | Mensile |
| Alert critici riconosciuti entro 30 minuti | >= 95% | Mensile |
| Accuratezza delle previsioni della capacità (entro +/-15%) | >= 80% delle previsioni | Trimestrale |
| Rapporti mensili sulla capacità consegnati nei tempi previsti | 100% | Mensile |
| Interruzioni del servizio legate alla capacità per trimestre | < 2 | Trimestrale |

**Punteggio di conformità**:

| Componente | Peso | Calcolo |
|-----------|--------|-------------|
| Copertura del monitoraggio | 30% | (Sistemi di produzione monitorati / Totale sistemi di produzione) x 100 |
| Soglie e alerting | 25% | (Risorse con soglie conformi + alert risposti entro SLA) / Totale x 100 |
| Previsione e pianificazione | 25% | (Previsioni accurate + previsioni consegnate nei tempi previsti) / Totale previsioni x 100 |
| Reportistica e governance | 20% | (Rapporti consegnati nei tempi previsti + revisioni completate) / Totale richiesti x 100 |

**Gestione della non conformità**: Al di sotto del 70% è richiesta un'escalation immediata al CIO e al RSSI con piano di remediation entro 10 giorni lavorativi. Tra il 70-89% è richiesta la supervisione del Responsabile dell'infrastruttura con revisioni mensili dei progressi. Al 90% e oltre si segue il monitoraggio trimestrale standard.

**Responsabilità della remediation per componente del punteggio**:

| Componente | Sotto l'obiettivo | Responsabile della remediation | Escalation |
|-----------|-------------|-------------------|------------|
| Copertura del monitoraggio | <100% produzione | Responsabile dell'infrastruttura | CIO a 30 giorni di ritardo |
| Soglie e alerting | <95% | Operazioni IT / Responsabile dell'infrastruttura | RSSI a 15 giorni di ritardo |
| Previsione e pianificazione | <80% accuratezza | Responsabile dell'infrastruttura | CIO alla revisione trimestrale |
| Reportistica e governance | <100% puntuale | Responsabile dell'infrastruttura | CIO a 15 giorni di ritardo |

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita (massimo 12 mesi). Le eccezioni per i sistemi di produzione critici richiedono l'approvazione congiunta del CIO e del RSSI. Tutte le eccezioni attive devono essere revisionate trimestralmente e segnalate al Team di revisione della direzione.

## Non conformità

Un dipendente che viola questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro. Le violazioni della politica devono essere documentate, investigate dal Responsabile della sicurezza delle informazioni e segnalate al RSSI. Gli incidenti legati alla capacità causati dalla non conformità alla politica (ad es. mancato monitoraggio, mancata risposta agli alert) devono essere trattati come fattori contributivi nelle revisioni post-incidente.

## Miglioramento continuo

Questa politica viene revisionata e aggiornata come parte del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti alle piattaforme infrastrutturali e ai servizi cloud, le tendenze degli incidenti legati alla capacità e l'analisi degli eventi quasi-mancati, i miglioramenti agli strumenti di monitoraggio e previsione, le modifiche normative che influenzano i requisiti di disponibilità, le opportunità di ottimizzazione dei costi e le lezioni apprese dagli eventi di esaurimento della capacità.

---

# Aree della norma ISO 27001 affrontate

Politica di gestione della capacità — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 5.37 Procedure operative documentate |
| Clausola 9.3 Revisione della direzione | 6.3 Consapevolezza, istruzione e formazione sulla sicurezza delle informazioni |
| | **8.6 Gestione della capacità** |
| | 8.13 Backup delle informazioni |
| | 8.14 Ridondanza delle strutture di elaborazione delle informazioni |
| | 8.16 Attività di monitoraggio |

**Quadro normativo e legale**:

| Quadro | Pertinenza |
|-----------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; la gestione della capacità garantisce la disponibilità dei sistemi che trattano dati personali |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — I requisiti minimi per la sicurezza dei dati includono la disponibilità del sistema |
| GDPR UE (ove applicabile) | Art. 32(1)(b) — Capacità di garantire la continua disponibilità e resilienza dei sistemi e dei servizi di trattamento |
| ISO/IEC 27001:2022 | Controllo Annex A 8.6 — Gestione della capacità |
| ISO/IEC 27002:2022 | Sezione 8.6 — Linee guida di implementazione per la gestione della capacità |
| NIST SP 800-53 Rev 5 | AU-4 (Capacità di archiviazione del log di audit), CP-2(2) (Pianificazione della capacità), SC-5 (Protezione dal denial-of-service) |
| NIST CSF 2.0 | PR.IR-01 (Reti e ambienti protetti da accesso logico non autorizzato), DE.CM (Monitoraggio continuo) |
| CIS Controls v8 | Controllo 8 (Gestione dei log di audit — capacità di archiviazione dei log), Controllo 13 (Monitoraggio e difesa della rete) |
| ITIL 4 | Pratica di gestione della capacità e delle prestazioni |
| FINMA (se applicabile) | Circolare 2023/1 — La resilienza operativa ICT include la gestione della capacità |
| DORA (se applicabile) | Art. 11 — Pianificazione della capacità ICT per la resilienza operativa digitale |
| NIS2 (se applicabile) | Art. 21(2) — La continuità operativa include la gestione della capacità |

---

<!-- QA_VERIFIED: 2026-04-03 -->
