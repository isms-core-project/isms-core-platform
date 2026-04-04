<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.16-IT:operational:OP-POL:a.8.16 -->
**ISMS-OP-POL-A.8.16 — Attività di monitoraggio**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Attività di monitoraggio |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.8.16 |
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

- ISO/IEC 27001:2022 Controllo A.8.16 — Attività di monitoraggio

**Controlli correlati dell'Annex A**:

| Controllo | Relazione con le attività di monitoraggio |
|-----------|-------------------------------------------|
| A.5.7 Intelligence sulle minacce | L'intelligence sulle minacce informa le regole di monitoraggio e i pattern di rilevamento |
| A.5.24–28 Gestione degli incidenti | Il monitoraggio attiva il rilevamento degli incidenti e l'escalation |
| A.5.28 Raccolta delle prove | I dati di monitoraggio costituiscono prove forensi |
| A.5.34 Privacy e protezione dei dati personali | Il monitoraggio dei dipendenti deve essere conforme ai requisiti sulla privacy |
| A.8.7 Protezione contro il malware | Gli eventi di rilevamento del malware alimentano il monitoraggio |
| A.8.15 Registrazione degli eventi | I log forniscono i dati grezzi che il monitoraggio analizza |
| A.8.17 Sincronizzazione dell'orologio | I timestamp accurati sono essenziali per la correlazione degli eventi |
| A.8.20 Sicurezza della rete | Il traffico di rete è una fonte di dati di monitoraggio primaria |

**Politiche interne correlate**:

- Politica di registrazione degli eventi (A.8.15)
- Politica di gestione degli incidenti
- Politica di sicurezza della rete
- Politica di sicurezza degli endpoint
- Politica di controllo degli accessi
- Politica sulla privacy e protezione dei dati personali

---

# Politica delle attività di monitoraggio

## Scopo

Lo scopo di questa politica è definire i requisiti per il monitoraggio attivo di reti, sistemi e applicazioni al fine di rilevare comportamenti anomali, minacce alla sicurezza e violazioni delle policy. Laddove la registrazione degli eventi (A.8.15) acquisisce e preserva gli eventi, il monitoraggio analizza quegli eventi in tempo reale o quasi in tempo reale per identificare e rispondere alle minacce prima che causino danni.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando il monitoraggio come misura tecnica e organizzativa adeguata al rischio. Le attività di monitoraggio DEVONO essere conformi al diritto del lavoro svizzero (CO svizzero Art. 328/328b) e al divieto di sorveglianza comportamentale (OLL3 Art. 26). Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32.

## Ambito di applicazione

Questa politica si applica a:

- Tutte le reti, i sistemi, le applicazioni e i servizi cloud nell'ambito del SGSI.
- Tutte le tecnologie di monitoraggio: SIEM, EDR/XDR, NDR, IDS/IPS, UEBA e strumenti equivalenti.
- Tutti i dipendenti e gli utenti terzi le cui attività generano eventi rilevanti per la sicurezza.
- Tutti gli ambienti: produzione, staging e sistemi rivolti all'esterno.

Il monitoraggio dei sistemi di sicurezza fisica (CCTV, lettori di badge) è disciplinato dalla Politica di controllo degli accessi fisici. La configurazione della registrazione e la conservazione dei log sono disciplinati dalla Politica di registrazione degli eventi (A.8.15).

## Principio

Il monitoraggio è un controllo attivo e di rilevamento. Reti, sistemi e applicazioni DEVONO essere monitorati per rilevare comportamenti anomali e DEVONO essere intraprese azioni appropriate per valutare i potenziali incidenti di sicurezza delle informazioni. Il monitoraggio DEVE operare sulla base di profili di comportamento di riferimento (baseline) stabiliti, regole di rilevamento definite e intelligence sulle minacce — non tramite sorveglianza indiscriminata.

---

## Cosa monitorare

### Ambito del monitoraggio

I seguenti elementi DEVONO essere monitorati per rilevare comportamenti anomali ed eventi di sicurezza:

| N. | Dominio di monitoraggio | Cosa monitorare |
|----|-------------------------|-----------------|
| 1 | **Traffico di rete** | Flussi di traffico in entrata e in uscita, traffico est-ovest (laterale) tra i segmenti, connessioni verso IP/domini malevoli noti |
| 2 | **Autenticazione e accesso** | Tentativi di accesso falliti, viaggi impossibili, pattern di credential stuffing, accessi da posizioni o dispositivi inattesi |
| 3 | **Attività privilegiate** | Azioni amministrative, escalation dei privilegi, utilizzo degli account di servizio, accesso privilegiato fuori orario |
| 4 | **Comportamento degli endpoint** | Anomalie nell'esecuzione dei processi, binari non firmati, esecuzione di script, meccanismi di persistenza, iniezione di codice in memoria |
| 5 | **Attività applicative** | Volumi di transazioni insoliti, operazioni sui dati in blocco, pattern di abuso delle API, picchi di errori applicativi |
| 6 | **Modifiche alla configurazione** | Modifiche alle impostazioni di sicurezza, alle regole del firewall, alle policy di gruppo, ai record DNS, alle configurazioni dei certificati |
| 7 | **Stato degli strumenti di sicurezza** | Disabilitazione di antivirus/EDR, modifiche alle regole del firewall, interruzioni del servizio di registrazione, tentativi di elusione di IDS/IPS |
| 8 | **Servizi cloud** | Accesso alle console di amministrazione, modifiche alla configurazione del tenant, chiamate API eccessive, operazioni di esportazione dei dati |
| 9 | **Spostamento dei dati** | Trasferimenti di file di grandi dimensioni, download in blocco, utilizzo di dispositivi USB, caricamenti su archiviazione cloud, allegati e-mail che superano le soglie |
| 10 | **Utilizzo delle risorse** | Anomalie di CPU/memoria/disco/larghezza di banda che possono indicare cryptomining, partecipazione a DDoS o compromissione del sistema |

### Priorità dei sistemi critici

I sistemi DEVONO essere prioritizzati per il monitoraggio in base al rischio:

| Priorità | Tipo di sistema | Livello di monitoraggio |
|----------|-----------------|-------------------------|
| **Critica** | Infrastruttura di autenticazione, firewall, VPN, domain controller, sistemi di pagamento | In tempo reale con avvisi automatici |
| **Alta** | Server che ospitano dati riservati/personali, gateway e-mail, console di amministrazione cloud | In tempo reale o quasi in tempo reale (entro 15 minuti) |
| **Media** | Server applicativi interni, infrastruttura di sviluppo, condivisioni di file interne | Quasi in tempo reale (entro 1 ora) |
| **Standard** | Workstation, stampanti, infrastruttura non critica | Revisione periodica (aggregazione giornaliera o settimanale) |

---

## Baseline comportamentali

### Definizione delle baseline

Prima che il rilevamento delle anomalie sia efficace, l'organizzazione DEVE stabilire baseline del comportamento normale. Le baseline iniziali DEVONO essere stabilite entro 30 giorni dalla distribuzione del monitoraggio per ciascun sistema o gruppo di sistemi. Durante il periodo di definizione delle baseline, il monitoraggio DEVE operare in "modalità apprendimento" — gli avvisi devono essere generati ma revisionati con una maggiore tolleranza per i falsi positivi fino alla convalida delle baseline.

Le baseline DEVONO documentare:

- Utilizzo del sistema durante i periodi operativi standard e di picco.
- Pattern di accesso tipici: tempi, posizione, frequenza e volume per gruppo di utenti.
- Flussi di traffico di rete previsti: coppie sorgente-destinazione, protocolli, volumi di dati.
- Tassi di transazione applicativa standard e livelli di errore.

Le baseline DEVONO essere revisionate e aggiornate:

- **Trimestralmente** per i sistemi generali.
- **Dopo cambiamenti significativi** (nuovi sistemi, riorganizzazioni, migrazioni cloud, cicli aziendali stagionali).
- **Dopo gli incidenti** in cui l'incidente ha rivelato una lacuna nella definizione della baseline.

### Rilevamento delle deviazioni

I sistemi di monitoraggio DEVONO essere configurati per rilevare deviazioni dalle baseline stabilite, incluse:

- Traffico da o verso fonti malevole note (server C2, infrastruttura botnet, IP/domini segnalati dall'intelligence sulle minacce).
- Firme e pattern di attacco noti (brute force, DDoS, buffer overflow, SQL injection, credential stuffing).
- Comportamento anomalo del sistema: terminazioni di processo impreviste, esecuzione di processi non autorizzati, indicatori di keylogging, deviazioni del protocollo.
- Anomalie del comportamento utente: accesso al di fuori del normale orario lavorativo, accesso a risorse non precedentemente accessibili, viaggi impossibili tra posizioni geografiche. I **viaggi impossibili** sono definiti come eventi di autenticazione da due posizioni geografiche entro un arco temporale che rende fisicamente impraticabile il viaggio tra di esse (ad es. accessi da Zurigo e Tokyo entro 2 ore). L'organizzazione DEVE definire i parametri dei viaggi impossibili sulla base di: velocità massima di viaggio plausibile, esclusioni VPN/proxy per i punti di uscita aziendali noti e tolleranza per l'imprecisione della posizione dei dispositivi mobili.
- Anomalie delle prestazioni di rete: latenza imprevista, saturazione della larghezza di banda, volumi di query DNS insoliti.
- Anomalie nel consumo delle risorse: picchi di CPU, I/O su disco imprevisto, esaurimento della memoria senza carico di lavoro corrispondente.

---

## Architettura del monitoraggio

### Piattaforma di monitoraggio

L'organizzazione DEVE distribuire una piattaforma di monitoraggio centralizzata in grado di:

| Capacità | Requisito |
|----------|-----------|
| **Correlazione degli eventi** | Correlare eventi da più fonti (log, rete, endpoint, cloud, identità) in una visione unificata |
| **Avvisi automatici** | Generare avvisi basati su regole predefinite, soglie e rilevamento delle anomalie |
| **Integrazione dell'intelligence sulle minacce** | Acquisire feed di intelligence sulle minacce esterni per arricchire le regole di rilevamento e identificare indicatori di compromissione noti |
| **Dashboard** | Fornire visibilità in tempo reale sulla postura di sicurezza, i volumi di avvisi e le tendenze |
| **Supporto alle indagini** | Consentire il drill-down dall'avviso agli eventi grezzi per le indagini sugli incidenti |
| **Conservazione** | Conservare i dati di monitoraggio secondo la pianificazione di conservazione della Politica di registrazione degli eventi (A.8.15) |

Esempi di piattaforme: SIEM (ad es. Microsoft Sentinel, Splunk, Elastic SIEM, Wazuh), XDR o equivalente.

### Livelli di rilevamento

DEVE essere implementato un approccio di monitoraggio a livelli:

| Livello | Tecnologia | Copertura |
|---------|-----------|-----------|
| **Rete** | NDR, IDS/IPS, log firewall, monitoraggio DNS | Visibilità del traffico nord-sud ed est-ovest |
| **Endpoint** | Agenti EDR/XDR su tutti i dispositivi gestiti | Esecuzione di processi, operazioni sui file, analisi della memoria |
| **Identità** | Monitoraggio del provider di identità, UEBA | Anomalie di autenticazione, uso improprio delle credenziali, indicatori di minaccia interna |
| **Applicazione** | Log applicativi inoltrati al SIEM, WAF | Anomalie delle transazioni, errori di validazione dell'input, abuso delle API |
| **Cloud** | Monitoraggio cloud-nativo (ad es. AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs) | Azioni amministrative, modifiche alla configurazione, accesso ai dati |

Laddove l'organizzazione non disponga delle risorse per un Security Operations Centre (SOC) interno completo, dovrebbe essere considerato un servizio MDR (Managed Detection and Response) per fornire una copertura di monitoraggio 24/7.

### Monitoraggio specifico del cloud

Per gli ambienti cloud (IaaS, PaaS, SaaS), si applicano ulteriori requisiti di monitoraggio:

- I **log di audit cloud** (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) DEVONO essere inoltrati alla piattaforma di monitoraggio centralizzata.
- Le modifiche alla **postura di sicurezza cloud** (ad es. creazione di bucket S3 pubblici, modifica dei security group, modifiche alle policy IAM) DEVONO generare avvisi immediati.
- I servizi di **rilevamento delle minacce cloud-nativo** (AWS GuardDuty, Azure Defender, GCP Security Command Center) dovrebbero essere abilitati e integrati con la piattaforma di monitoraggio centralizzata.
- Le **azioni amministrative SaaS** (portale di amministrazione M365, admin Google Workspace, modifiche alla configurazione Salesforce) DEVONO essere monitorate per rilevare modifiche alla configurazione non autorizzate.
- L'**attività API cloud** DEVE essere monitorata per rilevare volumi insoliti, accessi da posizioni inattese e utilizzo di endpoint API deprecati o ad alto rischio.

### Integrità del sistema di monitoraggio (SOC 2: CC4.1)

L'infrastruttura di monitoraggio stessa DEVE essere monitorata per garantire la disponibilità continua:

- **Acquisizione dei dati**: Avviso se l'acquisizione dei log da una fonte si interrompe o scende al di sotto del volume baseline per più di 15 minuti.
- **Integrità degli agenti**: Monitorare lo stato degli agenti EDR/monitoraggio su tutti gli endpoint; avviso per disconnessione degli agenti superiore a 1 ora.
- **Capacità di archiviazione**: Avviso all'80% di utilizzo dello spazio di archiviazione con pianificazione della capacità per una crescita minima di 30 giorni.
- **Disponibilità della piattaforma**: Obiettivo del 99,9% di uptime per la piattaforma di monitoraggio; failover o ridondanza per i componenti critici.
- **Rapporto mensile sulla salute**: IT Operations DEVE produrre un rapporto mensile sulla salute della piattaforma di monitoraggio che comprende uptime, tassi di acquisizione, copertura degli agenti e proiezioni della capacità.

### Indicazioni per l'implementazione graduale

Le organizzazioni che distribuiscono capacità di monitoraggio per la prima volta o che ampliano l'ambito dovrebbero seguire un approccio graduale:

| Fase | Durata | Ambito | Obiettivo |
|------|--------|--------|-----------|
| **Fase 1 — Fondazione** | Mesi 1-3 | Log di autenticazione, log firewall, eventi di protezione degli endpoint inoltrati al SIEM | Rilevamento delle minacce di base; capacità di correlazione dei log |
| **Fase 2 — Espansione** | Mesi 4-6 | Aggiungere monitoraggio del traffico di rete, log di audit cloud, log applicativi | Visibilità più ampia; definizione delle baseline per sistemi aggiuntivi |
| **Fase 3 — Maturazione** | Mesi 7-12 | UEBA, playbook di risposta automatica, mapping della copertura MITRE ATT&CK, analisi avanzata | Threat hunting proattivo; riduzione del MTTD |
| **Fase 4 — Ottimizzazione** | Continuativa | Ottimizzazione continua, arricchimento dell'intelligence sulle minacce, esercizi red team/purple team per convalidare il rilevamento | Efficacia sostenuta; riduzione dei falsi positivi |

---

## Gestione degli avvisi

### Classificazione degli avvisi

Gli avvisi DEVONO essere classificati per gravità al fine di determinare le tempistiche di risposta:

| Gravità | Descrizione | Tempo di risposta | Esempi |
|---------|-------------|-------------------|--------|
| **Critica** | Compromissione attiva o minaccia imminente | **15 minuti** (orario lavorativo), **1 ora** (fuori orario) | Esecuzione di malware confermata, esfiltrazione attiva di dati, indicatori di ransomware |
| **Alta** | Probabile evento di sicurezza che richiede indagine | **1 ora** (orario lavorativo), **4 ore** (fuori orario) | Multipli tentativi di autenticazione falliti dalla stessa fonte, disabilitazione dei controlli di sicurezza, download di dati in blocco |
| **Media** | Attività sospetta che richiede analisi | **4 ore** (orario lavorativo), **prossimo giorno lavorativo** (fuori orario) | Singolo accesso fallito da posizione insolita, violazione minore della policy, modifica imprevista della configurazione |
| **Bassa** | Informativa o anomalia minore | **Prossimo giorno lavorativo** | Scansione di porte da IP esterno, richiesta web bloccata verso categoria sospetta, lieve superamento della soglia |

### Processo di triage degli avvisi

**Modello di personale per la risposta agli avvisi**: L'organizzazione DEVE definire il proprio approccio di personale per la risposta agli avvisi:

| Modello | Copertura | Adatto a |
|---------|-----------|----------|
| **SOC interno** | Analisti di sicurezza dedicati durante l'orario lavorativo; rotazione di reperibilità fuori orario | Organizzazioni con ≥3 addetti alla sicurezza; ambienti ad alto rischio |
| **MDR (Managed Detection and Response)** | Monitoraggio 24/7 da provider esterno; escalation al team interno per eventi confermati | Organizzazioni con personale di sicurezza limitato; copertura 24/7 conveniente |
| **Ibrido** | MDR per il triage di primo livello 24/7; team interno per le indagini e la risposta | Approccio equilibrato; più comune per le PMI |
| **Reperibilità** | Monitoraggio durante l'orario lavorativo con reperibilità fuori orario solo per avvisi Critici/Alti | Approccio minimo praticabile per piccoli team; richiede avvisi ben ottimizzati |

Il modello scelto DEVE essere documentato e approvato dal RSSI. La capacità di risposta fuori orario DEVE essere testata trimestralmente.

Quando viene generato un avviso:

1. **Ricezione**: Avviso ricevuto dall'analista della sicurezza delle informazioni (o dal provider MDR).
2. **Triage**: L'analista valuta se l'avviso è un vero positivo, un falso positivo o richiede ulteriori indagini.
3. **Arricchimento**: Raccogliere ulteriore contesto — criticità dell'asset, profilo dell'utente, intelligence sulle minacce, eventi correlati.
4. **Decisione**: Se vero positivo o probabile evento di sicurezza, creare un record di incidente secondo la Politica di gestione degli incidenti.
5. **Escalation**: Gli incidenti di gravità Critica e Alta vengono escalati immediatamente al RSSI. Gli incidenti di gravità Media vengono escalati se non risolti entro i tempi definiti.
6. **Documentazione**: Tutte le decisioni di triage vengono documentate — inclusi i falsi positivi con giustificazione.

### Ottimizzazione degli avvisi

Per mantenere l'efficacia del monitoraggio e ridurre al minimo l'affaticamento da avvisi:

- Le regole di rilevamento DEVONO essere revisionate e ottimizzate **mensilmente** per ridurre i tassi di falsi positivi.
- Le regole di soppressione DEVONO essere documentate con giustificazione e revisionate **trimestralmente**.
- Nuove regole di rilevamento DEVONO essere aggiunte quando: l'intelligence sulle minacce identifica nuovi pattern di attacco, gli incidenti rivelano lacune nel rilevamento o vengono distribuiti nuovi sistemi/applicazioni.
- **Controllo delle modifiche alle regole di rilevamento**: Tutte le modifiche alle regole di rilevamento (nuove regole, modifiche, soppressioni, eliminazioni) DEVONO seguire un processo documentato: richiesta di modifica con giustificazione, revisione tra pari da parte di un secondo analista, test in un ambiente non di produzione/staging ove fattibile, approvazione dal responsabile della sicurezza delle informazioni e distribuzione con capacità di rollback. Le modifiche di emergenza alle regole (ad es. in risposta a una minaccia attiva) possono bypassare la revisione tra pari ma DEVONO essere revisionate retrospettivamente entro 48 ore.
- I volumi degli avvisi e i tassi di falsi positivi DEVONO essere monitorati come indicatori chiave di prestazione.
- Obiettivo: tasso di falsi positivi inferiore al **20%** per gli avvisi di alta gravità.
- **Processo di gestione dei falsi positivi**: Quando viene identificato un falso positivo, l'analista DEVE: (a) documentare la causa principale (regola mal configurata, processo aziendale legittimo, rumore ambientale), (b) determinare l'azione appropriata (ottimizzare la regola, aggiungere un'eccezione, sopprimere con scadenza, accettare), (c) implementare la modifica attraverso il processo di controllo delle modifiche alle regole di rilevamento e (d) verificare che l'ottimizzazione non sopprima i veri positivi. Le fonti di falsi positivi persistenti (>10 occorrenze alla settimana dalla stessa regola) DEVONO essere prioritizzate per l'ottimizzazione entro 5 giorni lavorativi.

---

## Pianificazione delle revisioni del monitoraggio

| Tipo di revisione | Frequenza | Responsabile | Ambito |
|-------------------|-----------|--------------|--------|
| **Avvisi in tempo reale** | Continuativa | Sicurezza delle informazioni / MDR | Gli eventi di gravità Critica e Alta attivano una notifica immediata |
| **Revisione della coda degli avvisi** | Giornaliera | Analista della sicurezza delle informazioni | Triage degli avvisi in sospeso; chiusura dei falsi positivi; escalation degli eventi confermati |
| **Revisione delle regole di rilevamento** | Mensile | Sicurezza delle informazioni | Ottimizzare le regole; aggiungere nuovi rilevamenti; sopprimere i falsi positivi convalidati |
| **Audit della copertura del monitoraggio** | Trimestrale | IT Operations / Sicurezza delle informazioni | Verificare che tutti i sistemi nell'ambito siano monitorati; identificare le lacune; integrare i nuovi sistemi |
| **Revisione delle baseline** | Trimestrale | Sicurezza delle informazioni | Aggiornare le baseline comportamentali per i cambiamenti nei sistemi, negli utenti o nelle operazioni aziendali |
| **Revisione dell'efficacia** | Semestrale | RSSI | Revisione delle metriche MTTD e MTTR; valutazione della copertura del rilevamento rispetto a MITRE ATT&CK; reporting alla direzione. **Deliverable**: rapporto scritto sull'efficacia che include: analisi delle lacune di copertura, heatmap della copertura delle tecniche MITRE ATT&CK (percentuale di tecniche rilevanti con regole di rilevamento attive), analisi delle tendenze di MTTD/MTTR/tasso di falsi positivi e miglioramenti raccomandati per il periodo successivo |

---

## Indicatori chiave di prestazione

Le seguenti metriche DEVONO essere monitorate per misurare l'efficacia del monitoraggio:

| N. | Metrica | Obiettivo | Reporting |
|----|---------|-----------|-----------|
| 1 | **MTTD (Mean Time to Detect)** | Gli eventi critici vengono rilevati entro 15 minuti dall'occorrenza | Mensile al RSSI |
| 2 | **MTTR (Mean Time to Respond)** | Gli avvisi critici vengono sottoposti a triage entro gli SLA di risposta | Mensile al RSSI |
| 3 | **Copertura del monitoraggio** | 100% dei sistemi critici, ≥95% di tutti i sistemi nell'ambito. Copertura = (sistemi con agente di monitoraggio attivo + sistemi con inoltro dei log al SIEM) / totale dei sistemi nell'ambito dall'inventario degli asset. I sistemi contrassegnati come fuori ambito richiedono una giustificazione documentata. | Trimestrale |
| 4 | **Tasso di falsi positivi** | <20% per gli avvisi di alta gravità | Mensile |
| 5 | **Aggiornamento delle regole di rilevamento** | Tutte le regole revisionate negli ultimi 90 giorni | Trimestrale |
| 6 | **Arretrato degli avvisi** | Critica: nessun avviso non sottoposto a triage da più di 1 ora; Alta: 4 ore; Media: 24 ore; Bassa: 48 ore | Settimanale |

---

## Privacy dei dipendenti e monitoraggio

### Requisiti legali

Le attività di monitoraggio DEVONO essere conformi al diritto del lavoro svizzero:

- **OLL3 Art. 26**: I sistemi di sorveglianza o controllo il cui unico o principale scopo è monitorare il comportamento dei dipendenti sono vietati.
- **CO svizzero Art. 328b**: Il trattamento dei dati dei dipendenti deve essere proporzionato e limitato a quanto necessario per il rapporto di lavoro o per verificare l'idoneità del dipendente.
- **nLPD**: Il trattamento dei dati dei dipendenti tramite monitoraggio richiede liceità, proporzionalità, limitazione delle finalità e trasparenza.

### Misure di salvaguardia della privacy

DEVONO essere applicate le seguenti misure di salvaguardia:

- Il monitoraggio DEVE servire **scopi legittimi di sicurezza** (rilevamento delle minacce, indagine sugli incidenti, verifica della conformità) — non sorveglianza comportamentale o gestione delle prestazioni.
- I dipendenti DEVONO essere **informati in anticipo** che il monitoraggio ha luogo, cosa viene monitorato e perché, attraverso la politica di uso accettabile e la documentazione di impiego.
- Devono essere raccolti e conservati solo i **dati minimi necessari** (minimizzazione dei dati).
- I dati di monitoraggio **non devono essere utilizzati** per valutazione delle prestazioni HR, azioni disciplinari per questioni non legate alla sicurezza o profilazione comportamentale generale.
- L'**analisi personalizzata** (che identifica singoli utenti) DEVE avvenire solo quando: (a) un avviso indica un potenziale incidente di sicurezza o violazione della policy e (b) l'indagine è documentata con giustificazione.
- Laddove i dati di monitoraggio vengano condivisi con parti esterne (ad es. provider MDR, investigatori forensi), gli identificatori personali DEVONO essere ridotti al minimo o anonimizzati ove fattibile.
- Una Valutazione d'impatto sulla protezione dei dati (VIPD) ai sensi della nLPD Art. 22 DEVE essere condotta prima della distribuzione del monitoraggio che soddisfa uno qualsiasi dei seguenti criteri:
  - Monitoraggio di tutta l'attività di rete dei dipendenti (acquisizione completa dei pacchetti, registrazione degli URL).
  - Distribuzione di sistemi UEBA (User and Entity Behaviour Analytics) che profilano singoli dipendenti.
  - Monitoraggio che acquisisce dati di posizione dei dipendenti (geolocalizzazione della connessione VPN, posizionamento WiFi).
  - Monitoraggio dell'attività dei dispositivi personali nell'ambito di accordi BYOD.
  - Qualsiasi attività di monitoraggio in cui il DPD o il Consulente per la protezione dei dati determini che il trattamento è suscettibile di comportare un rischio elevato per i diritti della personalità dei dipendenti.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|---------------|
| **RSSI** | Proprietà della politica; approvazione dell'ambito del monitoraggio e delle priorità di rilevamento; punto di escalation per gli avvisi critici; revisione semestrale dell'efficacia |
| **Analista della sicurezza delle informazioni** | Triage giornaliero degli avvisi; escalation degli incidenti; manutenzione delle regole di rilevamento; gestione dei falsi positivi; ottimizzazione mensile |
| **IT Operations / Team della piattaforma** | Amministrazione della piattaforma di monitoraggio; distribuzione degli agenti; onboarding delle fonti di log; gestione della capacità; monitoraggio della salute del sistema |
| **Amministratori di sistema** | Garantire che gli agenti di monitoraggio siano installati e operativi sui sistemi gestiti; segnalare i guasti o le lacune del monitoraggio |
| **Provider MDR** (se applicabile) | Monitoraggio degli avvisi 24/7; triage iniziale e arricchimento; escalation degli eventi confermati secondo i runbook concordati |
| **Consulente per la protezione dei dati** | Orientamento sull'impatto sulla privacy delle attività di monitoraggio; requisiti VIPD; requisiti di notifica ai dipendenti |

---

## Prove

Le seguenti prove dimostrano la conformità a questa politica:

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Configurazione della piattaforma di monitoraggio** e inventario dei sistemi (fonti di dati, regole di rilevamento, instradamento degli avvisi) | IT Operations | *Configurazione documentata; inventario delle fonti di dati revisionato trimestralmente* |
| 2 | **Metrica della copertura del monitoraggio** (percentuale di sistemi nell'ambito con monitoraggio attivo) | IT Operations / Sicurezza delle informazioni | *Trimestrale; obiettivo: 100% critico, ≥95% tutti nell'ambito* |
| 3 | **Documentazione delle baseline comportamentali** per i sistemi critici e i gruppi di utenti | Sicurezza delle informazioni | *Documentata; revisionata trimestralmente e dopo cambiamenti significativi* |
| 4 | **Registrazioni del triage degli avvisi** che mostrano la classificazione, la decisione di triage e la tempistica di risposta | Sicurezza delle informazioni | *Conservate 12 mesi; campionate durante l'audit* |
| 5 | **Log delle modifiche alle regole di rilevamento** (nuove regole, regole ottimizzate, regole soppresse con giustificazione) | Sicurezza delle informazioni | *Mensile; log conservato 12 mesi* |
| 6 | **Metriche MTTD e MTTR** riportate alla direzione | RSSI | *Mensile al RSSI; semestralmente alla revisione della direzione* |
| 7 | **Tasso di falsi positivi** e tendenze del volume degli avvisi | Sicurezza delle informazioni | *Mensile; obiettivo <20% di tasso di falsi positivi per alta gravità* |
| 8 | **Registrazioni della notifica ai dipendenti** (politica di uso accettabile, informativa sulla privacy riguardo al monitoraggio) | HR / Sicurezza delle informazioni | *Aggiornato per ogni modifica della politica; presa di conoscenza monitorata annualmente* |
| 9 | **Registrazioni VIPD** (se è implementato un monitoraggio su larga scala) | Consulente per la protezione dei dati | *Completata prima della distribuzione; revisionata annualmente* |
| 10 | **Registrazioni sulla salute della piattaforma di monitoraggio** — uptime, tassi di acquisizione dei dati, salute degli agenti, capacità di archiviazione (SOC 2: CC4.1) | IT Operations | *Monitoraggio continuo; rapporto di riepilogo mensile* |
| 11 | **Registrazioni di escalation** — utilizzo documentato del percorso di escalation, tempestività dell'escalation, risultati della risoluzione | Sicurezza delle informazioni | *Per escalation; revisionato mensilmente* |
| 12 | **Mapping della copertura MITRE ATT&CK** — tecniche coperte dalle regole di rilevamento, lacune identificate, piani di rimedio | Sicurezza delle informazioni | *Semestrale* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso audit della copertura del monitoraggio, revisioni della risposta agli avvisi, monitoraggio degli indicatori chiave di prestazione, audit interni ed esterni e feedback al proprietario della politica.

## Eccezioni

Qualsiasi eccezione a questa politica deve essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con accettazione del rischio documentata, controlli compensativi e una data di revisione definita. Le eccezioni devono essere riportate al team di revisione della direzione.

## Non conformità

Un dipendente che risulti aver violato questa politica può essere soggetto ad azioni disciplinari, fino al licenziamento.

## Miglioramento continuo

Questa politica viene rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono considerare i cambiamenti nelle tecnologie di monitoraggio, gli sviluppi del panorama delle minacce, i requisiti normativi e le lessons learned dagli incidenti e dall'analisi dei falsi positivi.

---

# Aree dello standard ISO 27001 trattate

Politica delle attività di monitoraggio — Mapping dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi di sicurezza delle informazioni | 5.36 Conformità a politiche, regole e standard |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 5.37 Procedure operative documentate |
| | 6.3 Sensibilizzazione, educazione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.16 Attività di monitoraggio** |

**Quadro normativo e legale**:

| Quadro normativo | Rilevanza |
|-----------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative; Art. 6 — Proporzionalità |
| CO svizzero | Art. 328b — Limitazioni al trattamento dei dati dei dipendenti |
| OLL3 svizzera | Art. 26 — Divieto della sorveglianza comportamentale |
| GDPR UE (se applicabile) | Art. 32 — Sicurezza del trattamento |
| ISO/IEC 27001:2022 | Annex A Controllo 8.16 |
| ISO/IEC 27002:2022 | Sezione 8.16 — Indicazioni di implementazione |
| NIST SP 800-53 Rev 5 | SI-4 (Information System Monitoring), AU-6 (Audit Record Review), CA-7 (Continuous Monitoring) |
| NIST CSF 2.0 | DE.CM (Continuous Monitoring), DE.AE (Adverse Event Analysis) |
| CIS Controls v8 | Controllo 8 (Audit Log Management), Controllo 13 (Network Monitoring and Defence) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
