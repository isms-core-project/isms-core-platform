<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.30-8.13-14-IT:operational:OP-POL:a.5.30-8.13-14 -->
**ISMS-OP-POL-A.5.30-8.13-14 — Continuità operativa e disaster recovery**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Continuità operativa e disaster recovery |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.30-8.13-14 |
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
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- Controllo ISO/IEC 27001:2022 A.5.30 — Prontezza ICT per la continuità operativa
- Controllo ISO/IEC 27001:2022 A.8.13 — Backup delle informazioni
- Controllo ISO/IEC 27001:2022 A.8.14 — Ridondanza delle strutture di elaborazione delle informazioni
- ISO/IEC 22301 — Sistemi di gestione della continuità operativa (riferimento informativo)
- NIST SP 800-34 Rev 1 — Guida alla pianificazione delle contingenze per i sistemi informativi federali (riferimento informativo)

**Controlli Annex A correlati**:

| Controllo | Relazione con la continuità operativa e il disaster recovery |
|-----------|-------------------------------------------------------------|
| A.5.9 Inventario delle informazioni e degli asset | L'inventario degli asset guida la BIA e l'identificazione dell'ambito dei backup |
| A.5.19–23 Relazioni con i fornitori e servizi cloud | Impegni BC/DR dei fornitori e modello di responsabilità condivisa |
| A.5.24–28 Ciclo di vita della gestione degli incidenti | Gli incidenti gravi possono innescare l'attivazione dei piani BC/DR |
| A.5.29 Sicurezza delle informazioni durante le interruzioni | Continuità della sicurezza durante gli eventi BC/DR |
| A.8.6 Gestione della capacità | La pianificazione della capacità supporta la ridondanza e l'infrastruttura DR |
| A.8.9 Gestione della configurazione | Le baseline di configurazione sono necessarie per la ricostruzione e il ripristino del sistema |
| A.8.15 Logging | Le operazioni di backup e ripristino DEVONO essere registrate |
| A.8.16 Attività di monitoraggio | Monitoraggio dei backup e controlli di integrità della ridondanza |

**Policy interne correlate**:

- Policy di gestione degli asset
- Policy di gestione degli incidenti
- Policy sulla sicurezza dei servizi cloud e dei fornitori
- Policy di logging
- Policy sulle attività di monitoraggio (A.8.16)
- Policy di gestione dei cambiamenti

---

# Policy di continuità operativa e disaster recovery

## Scopo

Lo scopo di questa policy è garantire che l'organizzazione possa continuare o ripristinare le proprie operazioni aziendali critiche e le strutture di elaborazione delle informazioni a seguito di un incidente che causa interruzioni. Stabilisce i requisiti per l'analisi dell'impatto sul business, il backup delle informazioni, la ridondanza dei sistemi e la pianificazione della continuità ICT.

Questa policy affronta tre controlli correlati di ISO 27001:2022 come quadro unificato perché operano come un ecosistema BC/DR integrato: il backup fornisce la capacità di recupero dei dati (A.8.13), la ridondanza fornisce la capacità di disponibilità del sistema (A.8.14) e la prontezza ICT fornisce la preparazione e la governance complessiva (A.5.30). Ogni controllo mantiene requisiti distinti ai fini della Dichiarazione di applicabilità.

Questa policy supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere la disponibilità e l'integrità dei dati personali e dei sistemi di elaborazione delle informazioni. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR Art. 32(1)(c) per la capacità di ripristinare tempestivamente la disponibilità e l'accesso ai dati personali.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i sistemi informativi, le applicazioni, le infrastrutture e i servizi inclusi nell'ambito della dichiarazione di scopo ISO 27001, inclusi:

- Server, database e repository di codice
- Infrastruttura cloud e applicazioni SaaS
- Infrastruttura di rete e sistemi di sicurezza
- Applicazioni e dati business-critical
- Configurazioni di sistema e infrastructure-as-code

**Escluso dall'ambito del backup** (salvo specifica valutazione del rischio):

- Archiviazione locale su desktop e portatili (i dati DEVONO risiedere su server con backup, servizi cloud o repository; i dati solo in locale sono a rischio di perdita permanente e non sono protetti da questa policy)
- Archiviazione locale su dispositivi mobili

**Escluso dall'ambito di questa policy**:

- Continuità operativa non ICT (quadro organizzativo BCM)
- Archivi fisici e informazioni non digitali (coperti dai controlli di sicurezza fisica)

## Principio

**La sicurezza delle persone è la nostra prima priorità. Sempre.**

La gestione della continuità operativa e la continuità della sicurezza delle informazioni DEVONO affrontare le minacce, i rischi e gli incidenti che influiscono sulla continuità delle operazioni. Il quadro si basa sulle best practice del settore e si allinea con ISO 22301 Business Continuity Management.

L'organizzazione DEVE:

- Condurre analisi dell'impatto sul business per identificare i sistemi critici e determinare i requisiti di ripristino.
- Mantenere copie di backup delle informazioni, del software e dei sistemi, testate regolarmente per confermarne la recuperabilità.
- Implementare la ridondanza per le strutture critiche di elaborazione delle informazioni per soddisfare i requisiti di disponibilità.
- Pianificare, implementare, mantenere e testare la continuità ICT in base agli obiettivi di continuità operativa.

**Principio critico — "Ripristino non testato = Nessun ripristino"**: Il successo del backup senza test di ripristino, la ridondanza senza test di failover e i piani BC senza test di scenario forniscono una falsa sicurezza. È richiesta la verifica basata sulle evidenze attraverso test sistematici.

---

## Analisi dell'impatto sul business e criticità dei sistemi

### Analisi dell'impatto sul business

La continuità operativa DEVE essere basata su un'analisi dell'impatto sul business (BIA) documentata e su una valutazione del rischio. La BIA DEVE:

- Identificare i processi aziendali critici e le relative dipendenze ICT.
- Quantificare l'impatto delle interruzioni ICT (finanziario, operativo, reputazionale, normativo).
- Stabilire Recovery Point Objective (RPO) e Recovery Time Objective (RTO) per ogni sistema critico.
- Identificare le interdipendenze tra i sistemi.

**Frequenza della BIA**: La BIA DEVE essere condotta inizialmente durante l'implementazione del SGSI, rivista annualmente e aggiornata in caso di significativi cambiamenti aziendali (nuovi servizi, acquisizioni, importanti modifiche ai sistemi) o dopo gravi incidenti.

### Livelli di criticità dei sistemi

I sistemi DEVONO essere classificati in livelli di criticità in base ai risultati della BIA. Questi livelli determinano la frequenza dei backup, i requisiti di ridondanza e i calendari di test:

| Livello | Classificazione | RPO massimo | RTO massimo | Esempi |
|---------|----------------|-------------|-------------|--------|
| **Tier 1** | Critico | 1 ora | 4 ore | Applicazione aziendale core, database principale, sistema di autenticazione |
| **Tier 2** | Alto | 6 ore | 24 ore | Email, piattaforma di collaborazione, applicazioni aziendali secondarie |
| **Tier 3** | Medio | 24 ore | 72 ore | Strumenti interni, ambienti di sviluppo, sistemi di reporting |
| **Tier 4** | Basso | 7 giorni | > 72 ore | Archivi, servizi interni non critici |

I proprietari dei sistemi, in consultazione con il Coordinatore BC/DR, DEVONO determinare il livello appropriato per ogni sistema in base ai risultati della BIA.

**Assegnazione del ruolo**: Laddove l'organizzazione non disponga di un Coordinatore BC/DR dedicato, l'IT Operations Manager assume le responsabilità di coordinamento BC/DR. Questa assegnazione DEVE essere formalmente documentata nella descrizione del ruolo.

### RPO e RTO

Il **Recovery Point Objective (RPO)** definisce la massima perdita di dati accettabile misurata nel tempo. L'RPO determina la frequenza dei backup. Esempio: un RPO di 6 ore significa che è accettabile una perdita di dati fino a 6 ore, quindi i backup DEVONO avvenire almeno ogni 6 ore.

Il **Recovery Time Objective (RTO)** definisce il tempo massimo accettabile per ripristinare un sistema dopo un'interruzione. L'RTO determina la strategia di ridondanza e ripristino. Esempio: un RTO di 4 ore significa che il sistema DEVE essere operativo entro 4 ore dall'interruzione.

I sistemi che non riescono a soddisfare il proprio RPO o RTO definito DEVONO seguire il processo di gestione delle eccezioni (si veda Conformità alla policy — Deroghe).

---

## Backup delle informazioni

### Ambito del backup

Le seguenti categorie di informazioni DEVONO essere sottoposte a backup:

| Categoria | Requisito di backup |
|----------|---------------------|
| Dati aziendali critici (cliente, finanziario, operativo) | Obbligatorio |
| Dati e configurazioni dei sistemi di produzione | Obbligatorio |
| Software applicativo e dipendenze | Obbligatorio |
| Configurazioni di sicurezza e dati di controllo degli accessi | Obbligatorio |
| Dati aziendali importanti | Obbligatorio |
| Ambienti di sviluppo/test | Basato sul rischio (backup se il costo di ricreazione supera il costo del backup) |
| Dati effimeri (cache, log temporanei) | Non richiesto |

### Calendario e conservazione dei backup

DEVE essere mantenuto e reso disponibile un calendario di backup, un calendario di conservazione e un calendario di test. La frequenza dei backup DEVE essere allineata all'RPO per ogni livello di sistema:

| Livello del sistema | Frequenza di backup | Conservazione minima |
|--------------------|---------------------|----------------------|
| **Tier 1 (Critico)** | Replica continua o oraria | Giornaliero: 30 giorni; Settimanale: 90 giorni; Mensile: 12 mesi |
| **Tier 2 (Alto)** | Ogni 4–6 ore | Giornaliero: 30 giorni; Settimanale: 90 giorni; Mensile: 12 mesi |
| **Tier 3 (Medio)** | Giornaliero | Giornaliero: 7 giorni; Settimanale: 28 giorni; Mensile: 12 mesi |
| **Tier 4 (Basso)** | Settimanale o a ogni modifica | Settimanale: 28 giorni; Mensile: 12 mesi |

**Conservazione estesa**: Periodi di conservazione più lunghi possono essere richiesti dalla normativa (ad es. documenti finanziari 7–10 anni), da richieste di legal hold o da obblighi contrattuali. La conservazione estesa DEVE essere giustificata (requisito normativo, legal hold o obbligo contrattuale) per evitare l'accumulo non necessario di dati. I periodi di conservazione più brevi richiedono l'approvazione del RSSI con documentata accettazione del rischio.

### Tipi di backup

L'organizzazione DEVE selezionare strategie di backup appropriate in base ai requisiti di sistema:

| Tipo di backup | Descrizione | Caso d'uso |
|----------------|-------------|-----------|
| **Completo** | Copia completa di tutti i dati | Backup baseline; settimanale o mensile |
| **Incrementale** | Dati modificati dall'ultimo backup (qualsiasi tipo) | Backup giornalieri; veloce, efficiente in termini di storage |
| **Differenziale** | Dati modificati dall'ultimo backup completo | Backup giornalieri; ripristino più veloce dell'incrementale |
| **Snapshot** | Copia point-in-time a livello di storage | Backup frequenti; VM e carichi di lavoro cloud |
| **Continuous Data Protection** | Replica in tempo reale o quasi | Sistemi Tier 1 che richiedono RPO < 1 ora |

### Regola di backup 3-2-1

L'organizzazione DEVE implementare la regola di backup 3-2-1 come minimo per i sistemi Tier 1 e Tier 2:

| Elemento | Requisito |
|---------|-----------|
| **3 copie** | Dati originali più almeno 2 copie di backup |
| **2 tipi di supporto** | Tecnologie di archiviazione diverse (ad es. disco + cloud, disco + nastro) |
| **1 copia fuori sede** | Ubicazione geograficamente separata (edificio, regione o regione cloud diversi) |

**Backup immutabili**: Per i sistemi Tier 1 e Tier 2, almeno una copia di backup DEVE essere immutabile (write-once-read-many) o air-gapped per proteggersi da ransomware ed eliminazione accidentale. Le tecnologie includono object storage con object lock (ad es. AWS S3 Object Lock, Azure Immutable Blob Storage o equivalente), nastro WORM o supporti offline air-gapped.

**Condizionale**: Le organizzazioni soggette a DORA (entità finanziarie UE) DEVONO implementare copie di backup immutabili ove tecnicamente fattibile (Art. 12(4)) e archiviazione di backup fuori sede a sufficiente distanza geografica.

### Sicurezza dei backup

- I backup DEVONO essere cifrati sia in transito che a riposo utilizzando AES-256 o equivalente, ai sensi della Policy sull'uso della crittografia (A.8.24). La soluzione di backup (ad es. Veeam, Commvault, AWS Backup, Azure Backup o equivalente) DEVE supportare la cifratura integrata.
- I backup archiviati in soluzioni cloud DEVONO essere ospitati come minimo presso un fornitore certificato ISO 27001.
- Laddove il backup avvenga su supporti fisici:
  - Il supporto DEVE essere cifrato.
  - Il supporto DEVE essere etichettato e conservato in modo sicuro con controllo degli accessi limitato e con autorizzazione richiesta.
  - Il trasferimento fuori sede DEVE utilizzare un corriere sicuro approvato o un trasferimento elettronico cifrato.
- I backup DEVONO essere protetti almeno allo stesso livello di sicurezza dei dati originali.
- **Gestione delle chiavi di cifratura dei backup**: Le chiavi di cifratura DEVONO essere gestite separatamente dai dati di backup. Le procedure di recupero delle chiavi DEVONO essere documentate e testate (le chiavi DEVONO essere accessibili quando i sistemi principali non sono disponibili). Le chiavi DEVONO essere ruotate annualmente o in caso di sospetta compromissione. Si raccomanda il key escrow o la custodia con chiave divisa per i backup di sistemi critici. La gestione delle chiavi DEVE essere conforme alla Policy sull'uso della crittografia (A.8.24).

### Portabilità dei backup

Per evitare il vendor lock-in, le implementazioni di backup dovrebbero garantire:

- I backup sono esportabili in formati standard del settore ove fattibile.
- I backup cloud sono ripristinabili in ambienti alternativi (provider cloud diverso o on-premises).
- Le procedure di ripristino affrontano gli scenari di uscita dal provider.

### Monitoraggio dei backup

Le operazioni di backup DEVONO essere monitorate:

| Elemento | Requisito |
|---------|-----------|
| Successo/fallimento del backup | Monitoraggio in tempo reale; avviso immediato in caso di fallimento per i sistemi Tier 1–2 |
| Durata del backup | Avviso se la durata supera la finestra di backup |
| Capacità di archiviazione | Avviso al 70% di utilizzo; allerta all'80%; critico al 90% |
| Replica fuori sede | Avviso in caso di fallimento della replica |

I log di backup DEVONO essere prodotti e verificati per errori e prestazioni almeno settimanalmente. Laddove vengano riscontrati errori, DEVONO essere adottate e registrate azioni correttive.

DEVONO essere forniti rapporti mensili sullo stato dei backup al RSSI, inclusa la copertura dei backup, i tassi di successo e i problemi in sospeso.

### Test e verifica dei backup

I backup DEVONO essere testati regolarmente per garantire che possano essere affidabili in un'emergenza e soddisfino le esigenze dei piani di continuità operativa:

| Livello del sistema | Frequenza del test di ripristino | Ambito del test |
|--------------------|----------------------------------|-----------------|
| **Tier 1 (Critico)** | Trimestrale | Ripristino completo del sistema in ambiente alternativo |
| **Tier 2 (Alto)** | Semestrale | Set di dati rappresentativi; sistema completo annualmente |
| **Tier 3 (Medio)** | Annuale | Verifica del ripristino campione |
| **Tier 4 (Basso)** | In caso di modifica significativa | Ripristino campione o documentata accettazione del rischio |

Ogni test di ripristino DEVE documentare: data del test, sistemi testati, sorgente del backup, tempo di ripristino previsto vs. effettivo, verifica dell'integrità dei dati, problemi riscontrati e firma del responsabile del test.

**Risposta ai test falliti**: I test di ripristino che rivelano fallimenti del recovery DEVONO attivare l'escalation in base al livello del sistema:

| Livello | Notifica | Piano di remediation | Aggiornamenti di stato | Escalation |
|---------|----------|---------------------|----------------------|------------|
| **Tier 1** | Notifica alla direzione entro 4 ore | Entro 24 ore | Giornaliero | Segnalato alla prossima revisione del management; i fallimenti ricorrenti (stesso sistema due volte in 12 mesi) attivano una revisione architetturale |
| **Tier 2** | Notifica al RSSI entro 24 ore | Entro 5 giorni lavorativi | Settimanale | Segnalato alla prossima revisione del management |
| **Tier 3–4** | Aggiornamento del registro dei rischi entro 10 giorni lavorativi | Prossima finestra di manutenzione | Mensile | Revisione trimestrale |

Il re-test DEVE avvenire entro 30 giorni dalla remediation per i sistemi Tier 1–2.

**Condizionale**: Le organizzazioni soggette a DORA DEVONO testare il ripristino dei backup almeno annualmente (Art. 12(6)).

### Procedure di ripristino

Le procedure di backup e ripristino DEVONO essere documentate, mantenute e rese accessibili (anche quando i sistemi principali non sono disponibili). Le procedure di ripristino per ogni sistema critico DEVONO includere:

- Processo di ripristino passo per passo.
- Credenziali di accesso e autorizzazione richieste.
- Stima del tempo di ripristino rispetto all'obiettivo RTO (includere un buffer del 25% per complicazioni impreviste).
- Passaggi di validazione per confermare il ripristino riuscito.
- Contatti di escalation.

### Responsabilità del backup cloud

Per i sistemi ospitati nel cloud, l'organizzazione DEVE:

- Comprendere il modello di responsabilità condivisa del fornitore (cosa esegue il backup il fornitore rispetto a cosa deve eseguire il backup il cliente).
- Implementare backup gestiti dal cliente laddove le capacità del fornitore non soddisfino i requisiti RPO.
- Testare le procedure di esportazione e ripristino dei dati SaaS.
- Documentare le procedure di ripristino da cloud a on-premises per gli scenari di interruzione prolungata del cloud.

### Allineamento agli SLA del fornitore cloud

- Le garanzie degli SLA del fornitore cloud DEVONO essere verificate rispetto ai requisiti RTO dell'organizzazione per ogni livello di sistema.
- Le prestazioni storiche di uptime e risposta agli incidenti del fornitore DEVONO essere documentate durante la valutazione del fornitore (ai sensi di A.5.19–23).
- Laddove lo SLA del fornitore sia insufficiente per i sistemi Tier 1 o Tier 2, DEVE essere implementata la ridondanza gestita dal cliente.
- Le capacità BC/DR del fornitore (multi-AZ, backup/ripristino, failover) DEVONO essere documentate.
- Gli impegni BC/DR del fornitore cloud DEVONO essere inclusi nella valutazione del rischio del fornitore.
- I fornitori dovrebbero mantenere la certificazione ISO 22301 o equivalente ove disponibile.

---

## Ridondanza delle strutture di elaborazione delle informazioni

### Requisiti di ridondanza per livello

Le strutture di elaborazione delle informazioni DEVONO essere implementate con ridondanza sufficiente per soddisfare i requisiti di disponibilità:

| Livello del sistema | Ridondanza minima | Tipo di failover | RTO target |
|--------------------|-------------------|-----------------|-----------|
| **Tier 1 (Critico)** | Active-active o active-passive con failover automatico | Automatico | Minuti |
| **Tier 2 (Alto)** | Warm standby o failover manuale documentato | Manuale con runbook | Ore |
| **Tier 3 (Medio)** | Cold standby o ricostruzione da backup | Ricostruzione | Giorni |
| **Tier 4 (Basso)** | Ripristino basato su backup | Ripristino | Secondo l'RTO |

**Opzioni di architettura per la ridondanza**:

- **Active-active**: Più sistemi servono il traffico contemporaneamente; il guasto è gestito dai sistemi rimanenti.
- **Active-passive**: Il sistema principale serve il traffico; il sistema standby è pronto per l'attivazione immediata in caso di guasto.
- **Warm standby**: L'ambiente standby è parzialmente provisionato; richiede la sincronizzazione dei dati prima di diventare operativo.
- **Cold standby**: L'infrastruttura è disponibile ma non provisionata; richiede provisioning e ripristino dei dati.

### Analisi dei Single Point of Failure (SPOF)

I proprietari dei sistemi DEVONO condurre un'analisi SPOF per i sistemi Tier 1 e Tier 2 per identificare i componenti il cui guasto causerebbe la completa indisponibilità del sistema. I SPOF comuni includono:

- Server singolo senza clustering o failover.
- Percorso di rete singolo senza connettività ridondante.
- Controller di archiviazione, alimentatore o UPS singolo.
- Singola zona di disponibilità cloud o data center.
- DNS singolo o server di autenticazione singolo.

**Remediation dei SPOF**: I SPOF identificati per i sistemi Tier 1 DEVONO essere rimediati entro 90 giorni o avere un'accettazione del rischio documentata del RSSI. I SPOF dei sistemi Tier 2 DEVONO essere rimediati entro 180 giorni o avere un'accettazione del rischio documentata.

### Test di failover

I sistemi con ridondanza DEVONO avere i propri meccanismi di failover testati:

| Livello del sistema | Frequenza del test di failover |
|--------------------|-------------------------------|
| **Tier 1 (Critico)** | Trimestrale (failover completo in ambiente di produzione o simile) |
| **Tier 2 (Alto)** | Semestrale (test di failover documentato o esercitazione tabletop) |
| **Tier 3 (Medio)** | Annuale (esercitazione tabletop o validazione della procedura) |

Ogni test di failover DEVE documentare: sistemi testati, meccanismo di trigger del failover, tempo di failover effettivo rispetto all'obiettivo RTO, problemi identificati e firma.

**Test di failback**: I test di failover DEVONO validare anche il processo di failback (ritorno all'infrastruttura principale dopo il ripristino). Le procedure di failback DEVONO essere documentate e testate insieme al failover per garantire la capacità completa del ciclo di ripristino.

**Risposta ai failover falliti**: I test che rivelano l'incapacità di soddisfare l'RTO DEVONO attivare la remediation immediata e la valutazione del rischio ai sensi della tabella di escalation in Test e verifica dei backup.

### Ridondanza geografica e di rete

**Ridondanza geografica**: Per i sistemi Tier 1, la ridondanza DEVE essere implementata a sufficiente distanza geografica per proteggersi dai disastri a livello di sito:

| Livello di distanza | Separazione | Protezione contro |
|--------------------|------------|-------------------|
| **Minimo** | Edificio o campus diverso | Incidenti localizzati (incendio, allagamento, interruzione di corrente) |
| **Raccomandato** | Città o regione diversa (>100 km) | Disastri regionali |
| **Best practice** | Zona geografica o sismica diversa | Catastrofi naturali su larga scala |

Guida specifica per il cloud: Il deployment multi-AZ (separazione di decine di chilometri) soddisfa il livello minimo. Il deployment multi-regione (centinaia o migliaia di chilometri) soddisfa il livello raccomandato.

**Ridondanza di rete**: I sistemi critici dovrebbero implementare la ridondanza di rete inclusi ISP o provider doppi, switch/router ridondanti e firewall ridondanti laddove l'infrastruttura dell'organizzazione lo supporti.

**Analisi costi-benefici**: Le decisioni di ridondanza DEVONO bilanciare il costo dell'infrastruttura ridondante con l'impatto aziendale delle interruzioni prolungate e i requisiti normativi. Per molte PMI, la ridondanza cloud-native (deployment multi-AZ) fornisce ridondanza geografica conveniente senza mantenere un'infrastruttura fisica separata.

**Condizionale**: Le organizzazioni soggette a DORA o NIS2 dovrebbero implementare la ridondanza geografica per i sistemi critici per soddisfare i requisiti di resilienza operativa.

---

## Pianificazione della continuità ICT

### Piani di continuità operativa

L'organizzazione DEVE mantenere procedure documentate per rispondere a un incidente che causa interruzioni e per continuare o ripristinare le proprie attività entro tempi prestabiliti. I piani di continuità operativa DEVONO soddisfare le esigenze di chi li utilizzerà.

**I piani di continuità operativa DEVONO coprire**:

- Ruoli e responsabilità per le persone e i team con autorità durante e dopo un incidente.
- Un processo per attivare la risposta.
- Dettagli per gestire le conseguenze immediate di un incidente che causa interruzioni, con la dovuta considerazione per il benessere delle persone.
- Opzioni strategiche, tattiche e operative per rispondere alle interruzioni.
- Prevenzione di ulteriori perdite o indisponibilità delle attività prioritizzate.
- Come e in quali circostanze l'organizzazione comunicherà con i dipendenti e i loro familiari, i principali stakeholder e i contatti di emergenza.
- Come l'organizzazione continuerà o ripristinerà le proprie attività prioritizzate entro tempi prestabiliti.
- Dettagli sulla risposta dell'organizzazione ai media a seguito di un incidente, inclusa una strategia di comunicazione, l'interfaccia preferita con i media e linee guida per la stesura di comunicati stampa.
- Un processo per la fase di "cessato allarme" al termine dell'incidente.

**Ogni piano DEVE definire**: scopo e ambito, obiettivi, criteri e procedure di attivazione, procedure di implementazione, ruoli e autorità, requisiti di comunicazione, interdipendenze interne ed esterne, requisiti di risorse e processi di flusso delle informazioni e documentazione.

### Piani di ripristino ICT

Per ogni sistema Tier 1 e Tier 2, l'organizzazione DEVE mantenere piani di ripristino ICT che documentino:

1. **Criteri di attivazione** — Quando attivare il piano (processo di dichiarazione del disastro).
2. **Team di ripristino** — Ruoli, responsabilità e procedure di escalation.
3. **Contatti di emergenza** — Team di ripristino, fornitori, stakeholder.
4. **Procedure di ripristino** — Istruzioni passo per passo per il ripristino del sistema in ordine di priorità.
5. **Procedure di comunicazione** — Template di comunicazione interna ed esterna.
6. **Priorità di ripristino** — Sequenza di ripristino del sistema in base alle dipendenze e alla classificazione del livello.
7. **Procedure di validazione** — Come verificare che i sistemi siano operativi dopo il ripristino.
8. **Procedure di rollback** — Azioni in caso di fallimento del ripristino.

I piani di ripristino DEVONO essere sottoposti a version control, rivisti annualmente e aggiornati dopo esercitazioni di test, gravi incidenti o significative modifiche ai sistemi.

### Processo di dichiarazione del disastro

Un disastro DEVE essere dichiarato quando:

- Un'interruzione di un sistema Tier 1 supera il 50% del suo RTO definito.
- Più sistemi si guastano contemporaneamente.
- Un'interruzione infrastrutturale prolungata (data center, regione cloud, rete) è confermata.
- Un incidente informatico (ransomware, violazione di dati) impedisce le normali operazioni.
- Si verifica la perdita o l'inaccessibilità di un sito fisico.

**Gerarchia delle autorità di dichiarazione**: L'ingegnere di turno valuta → escalation all'IT Operations Manager → il RSSI valuta entro 30 minuti → AD/Direzione generale autorizza la dichiarazione se necessario → i piani BC/DR vengono attivati e i team di ripristino vengono notificati.

**Notifica di attivazione**: DEVONO essere mantenuti template di notifica pre-approvati nel piano BC/DR. La notifica DEVE essere emessa contemporaneamente tramite il canale principale (email, piattaforma di collaborazione) e il canale di backup (SMS, telefono).

**Escalation da incidente a disastro**: Non ogni incidente è un disastro. La Policy di gestione degli incidenti (A.5.24–28) governa la risposta iniziale agli incidenti. L'escalation alla dichiarazione di disastro avviene quando la risposta agli incidenti determina che il normale ripristino entro l'RTO non è raggiungibile.

### Programma di test BC/DR

I piani di continuità operativa e i piani di ripristino tecnico DEVONO essere testati almeno annualmente e quando si verificano cambiamenti significativi.

**Tipi di test**:

| Tipo di test | Descrizione | Frequenza |
|-------------|-------------|-----------|
| **Esercitazione tabletop** | Walkthrough discussione di uno scenario con il personale chiave | Annuale (tutti i processi critici) |
| **Test dei componenti** | Test del ripristino del singolo sistema (ripristino da backup, failover) | Trimestrale per Tier 1; semestrale per Tier 2 |
| **Test DR completo** | Failover completo al sito DR o ambiente alternativo | Annuale per i sistemi Tier 1 |

**Test integrato annuale**: Almeno un test annuale BC/DR dovrebbe esercitare il ripristino dei backup, l'attivazione della ridondanza, la validazione dei processi aziendali e le procedure di comunicazione insieme per verificare la capacità di ripristino end-to-end.

**Documentazione dei test**: Ogni test DEVE documentare: data del test, ambito, obiettivi, partecipanti, scenario, risultati (successo/parziale/fallimento), RTO/RPO effettivi vs. target, problemi identificati, lezioni apprese, azioni correttive e firma.

**Risposta ai test falliti**: I test che rivelano l'incapacità di soddisfare gli obiettivi RTO/RPO DEVONO attivare un'indagine immediata, un piano di remediation delle lacune, controlli compensativi provvisori e notifica alla direzione per i sistemi Tier 1.

**Condizionale**: Le organizzazioni soggette a DORA DEVONO testare gli accordi BC almeno annualmente (Art. 11(9)) e testare il backup e il ripristino ICT almeno annualmente (Art. 12(6)).

### Formazione e sensibilizzazione BC/DR

| Destinatari | Contenuto della formazione | Frequenza |
|------------|---------------------------|-----------|
| **Tutti i dipendenti** | Sensibilizzazione BC/DR (responsabilità individuali, procedure di segnalazione, canali di comunicazione, concetti base) | Annuale |
| **Membri del team di ripristino** | Formazione specifica per ruolo (procedure di ripristino, protocolli di comunicazione, utilizzo degli strumenti) | Annuale; nuovi membri formati entro 30 giorni dall'assegnazione |
| **Direzione generale** | Processo decisionale in crisi, processo di dichiarazione del disastro, gestione dei media | Annuale (esercitazione tabletop) |

Formazione post-test: I risultati dei test BC/DR e le lezioni apprese DEVONO essere comunicati a tutti i partecipanti entro 30 giorni da ogni test.

**Obiettivi di formazione**: 100% del team di ripristino formato; 95% di tutti i dipendenti ha completato la sensibilizzazione BC/DR.

### Comunicazione di crisi

I piani BC/DR DEVONO includere procedure di comunicazione per:

**Comunicazione interna**:

- Notifica di attivazione entro 30 minuti dalla dichiarazione del disastro (chi viene notificato, attraverso quali canali).
- Aggiornamenti di stato durante il ripristino a intervalli definiti (orari per Tier 1, ogni 4 ore per Tier 2).
- Notifica di "cessato allarme" al completamento del ripristino e alla validazione dei sistemi.

**Comunicazione esterna**:

- Notifica ai clienti (proattiva per le interruzioni note che influiscono sul servizio).
- Coordinamento con fornitori/partner (se necessario per il ripristino).
- Notifica normativa (se richiesta — ad es. notifica di violazione di dati ai sensi della nLPD Art. 24 o GDPR Art. 33).

**Canali di comunicazione**: Canali principali (email, [Piattaforma di collaborazione]); canali di backup (SMS, telefono) se i canali principali non sono disponibili. Gli elenchi contatti DEVONO essere mantenuti, accessibili offline (stampati o su dispositivi mobili) e rivisti trimestralmente.

### Procedure di ripristino

L'organizzazione DEVE mantenere procedure documentate per ripristinare e restituire le attività aziendali dalle misure temporanee adottate durante un incidente alle normali operazioni aziendali.

**Checklist di validazione del ripristino**: Prima di dichiarare un sistema ripristinato e tornare alle normali operazioni, DEVE essere verificato quanto segue:

- Integrità dei dati confermata (checksum, conteggi dei record, validazione a livello di applicazione).
- Tutti i sistemi dipendenti e le integrazioni operativi.
- Accesso degli utenti ripristinato e testato.
- Controlli di sicurezza riabilitati e verificati (EDR, regole firewall, logging).
- Prestazioni entro parametri accettabili.
- Firma del proprietario del sistema.

### Ripristino da ransomware

Data la prevalenza delle minacce ransomware, le seguenti considerazioni specifiche di ripristino integrano il quadro generale BC/DR:

**Azioni immediate al rilevamento del ransomware**:

1. Isolare i sistemi infetti dalla rete (non spegnere — preservare le prove forensi).
2. Attivare il team di risposta agli incidenti ai sensi della Policy di gestione degli incidenti (A.5.24–28).
3. Valutare l'integrità dei backup — verificare che le copie di backup non siano compromesse prima di avviare il ripristino.

**Considerazioni di ripristino**:

- Ricostruire da backup noti-puliti verificati come precedenti all'infezione.
- Patchare la vulnerabilità sfruttata prima di ripristinare i sistemi in produzione.
- Reimpostare tutte le credenziali (utente, account di servizio, amministratore) prima di ripristinare l'accesso.
- Implementare un monitoraggio esteso per 30–90 giorni dopo il ripristino per rilevare meccanismi di persistenza.

**Importanza dei backup immutabili**: Lo storage WORM, l'object lock o i supporti air-gapped garantiscono che almeno un punto di ripristino sia immune alla cifratura del ransomware.

**Pagamento del riscatto**: L'organizzazione NON deve effettuare pagamenti di riscatto senza l'esplicita approvazione della Direzione generale e la preventiva consultazione del consulente legale e del fornitore di assicurazione cyber (se applicabile).

### Segnalazione degli incidenti e della continuità operativa

DEVE essere in vigore e seguito un processo di gestione degli incidenti. Gli incidenti di continuità operativa DEVONO inoltre essere:

- Registrati e tracciati in un registro.
- Segnalati al Team di revisione del management.
- Soggetti a revisione post-incidente per acquisire le lezioni apprese.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità BC/DR |
|-------|---------------------|
| **AD / Direzione generale** | Responsabilità ultima per la continuità operativa; approvare la strategia e il budget BC/DR; dichiarare i disastri che richiedono l'attivazione del piano |
| **RSSI** | Titolare della policy BC/DR; approvare i requisiti e le accettazioni del rischio; garantire risorse adeguate; segnalare lo stato BC/DR alla direzione trimestrale |
| **Coordinatore BC/DR** | Gestione quotidiana del programma BC/DR; coordinare il processo BIA; mantenere i piani di ripristino; pianificare e facilitare i test; tracciare la conformità ai requisiti di backup e ridondanza; gestire il programma di formazione BC/DR; valutare l'impatto delle modifiche sui piani BC/DR |
| **Amministratori di sistema / cloud** | Implementare e gestire le soluzioni di backup; configurare i meccanismi di ridondanza e failover; monitorare i job di backup; partecipare ai test BC/DR; mantenere la documentazione di ripristino |
| **Proprietari di sistema / applicazione** | Definire i requisiti RTO/RPO; fornire input alla BIA; approvare le priorità di ripristino del sistema; validare i sistemi ripristinati; partecipare ai test BC/DR |
| **Tutti i dipendenti** | Segnalare gli incidenti di continuità operativa; seguire i piani BC durante le interruzioni; partecipare alla formazione di sensibilizzazione BC/DR |

---

## Metriche e reportistica BC/DR

Le seguenti metriche DEVONO essere tracciate per misurare l'efficacia del programma BC/DR:

| # | Metrica | Obiettivo | Monitoraggio | Reportistica |
|---|---------|----------|--------------|--------------|
| 1 | **Tasso di successo dei backup** | ≥99% Tier 1; ≥98% Tier 2–3 | Giornaliero | Mensile al RSSI |
| 2 | **Completamento dei test di ripristino** | 100% per calendario | Per test | Trimestrale |
| 3 | **Risultati dei test RTO/RPO** | 100% Tier 1 entro target; ≥95% Tier 2 | Per test | Tendenza trimestrale |
| 4 | **Completamento dei test di failover** | 100% per calendario | Per test | Trimestrale |
| 5 | **Aggiornamento dei piani BC/DR** | 100% revisionati nel ciclo annuale | Trimestrale | Trimestrale |
| 6 | **Remediation dei SPOF** | ≥90% rimediati o risk-accepted entro la tempistica | Trimestrale | Trimestrale |
| 7 | **Formazione del team di ripristino** | 100% formato | Annuale | Annuale |

Le metriche che superano i target per due periodi di reportistica consecutivi DEVONO essere escalate al RSSI e segnalate alla prossima revisione del management.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

| # | Evidenza | Proprietario | Frequenza |
|---|---------|--------------|-----------|
| 1 | **Analisi dell'impatto sul business** con livelli di criticità dei sistemi, RPO/RTO e mappatura delle dipendenze | Coordinatore BC/DR / RSSI | *Revisione annuale; aggiornata in caso di cambiamenti significativi; conservata 5 anni* |
| 2 | **Inventario dei backup** (sistemi con backup, tipo di backup, frequenza, conservazione, stato fuori sede) | Amministratori di sistema | *Mantenuto continuamente; revisione trimestrale; conservato 3 anni* |
| 3 | **Log di monitoraggio dei backup e rapporti** (tassi successo/fallimento, registri di risoluzione degli errori) | Amministratori di sistema | *Verifiche log settimanali; rapporti mensili al RSSI; conservati 12 mesi* |
| 4 | **Risultati dei test di ripristino dai backup** (data del test, sistemi, RTO/RPO effettivo vs. target, verifica dell'integrità dei dati) | Coordinatore BC/DR | *Per calendario (trimestrale/annuale per livello); conservati 3 anni* |
| 5 | **Analisi SPOF** per i sistemi Tier 1 e Tier 2 con stato di remediation | Proprietari di sistema | *Revisione annuale; aggiornata in caso di modifiche infrastrutturali; conservata 3 anni* |
| 6 | **Risultati dei test di failover** (tempo di failover, problemi, firma) | Coordinatore BC/DR | *Per calendario (trimestrale/annuale per livello); conservati 3 anni* |
| 7 | **Piani BC/DR** (piani di continuità operativa e piani di ripristino ICT, versioni correnti) | Coordinatore BC/DR / RSSI | *Revisione annuale; aggiornati dopo test e incidenti; conservare versione corrente + 2 precedenti* |
| 8 | **Registri dei test BC/DR** (esercitazioni tabletop, test dei componenti, test DR completi con scenari e risultati) | Coordinatore BC/DR | *Annuale come minimo; conservati 3 anni* |
| 9 | **Registro delle eccezioni** (sistemi che non soddisfano RPO/RTO, accettazioni del rischio, controlli compensativi) | RSSI | *Per evento; revisione trimestrale; conservato 5 anni* |
| 10 | **Elenchi contatti per la comunicazione di crisi** (team interno, contatti esterni, contatti dei fornitori, disponibili offline) | Coordinatore BC/DR | *Revisione trimestrale; aggiornato ad ogni modifica* |
| 11 | **Registri di formazione BC/DR** (completamento della formazione del team di ripristino, tassi di completamento della sensibilizzazione annuale) | Coordinatore BC/DR | *Annuale; conservati 3 anni* |
| 12 | **Rapporti sulle metriche BC/DR** (tassi di successo dei backup, completamento dei test, tendenze dell'aggiornamento dei piani) | Coordinatore BC/DR | *Mensile al RSSI; rapporti di tendenza trimestrali; conservati 3 anni* |
| 13 | **Documentazione SLA e capacità BC/DR del fornitore cloud** (garanzie SLA, modello di responsabilità condivisa, verifica dell'allineamento BC/DR) | Proprietari di sistema / Amministratori cloud | *Revisione annuale e al rinnovo del contratto; conservata 3 anni* |

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: rapporti di monitoraggio dei backup, registri dei test di ripristino, risultati dei test BC/DR, rapporti di analisi SPOF, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy (ad es. sistema escluso dal backup, ridondanza non implementata, RPO/RTO non soddisfatti) DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio, dei controlli compensativi e di una data di revisione definita (massimo 12 mesi, rinnovabile). Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni alle operazioni aziendali, all'infrastruttura tecnologica, ai requisiti normativi, alle lezioni apprese dai test BC/DR e dagli incidenti reali, ai risultati degli audit, alle minacce emergenti (ad es. ransomware, interruzioni della catena di fornitura), alle valutazioni delle minacce ambientali e alla previsione della capacità per l'infrastruttura di backup e DR.

L'organizzazione si impegna allo sviluppo e al miglioramento continuo del processo, dei piani e del sistema di continuità operativa.

---

# Sezioni della norma ISO 27001 trattate

Policy di continuità operativa e disaster recovery — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.29 Sicurezza delle informazioni durante le interruzioni |
| Clausola 7.3 Consapevolezza | **5.30 Prontezza ICT per la continuità operativa** |
| Clausola 8.1 Pianificazione e controllo operativi | 5.36 Conformità a policy, regole e standard |
| | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **8.13 Backup delle informazioni** |
| | **8.14 Ridondanza delle strutture di elaborazione delle informazioni** |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative inclusa la protezione della disponibilità e la capacità di recupero dei dati |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati |
| GDPR UE (ove applicabile) | Art. 32(1)(c) — Capacità di ripristinare tempestivamente la disponibilità e l'accesso ai dati personali |
| ISO/IEC 27001:2022 | Controlli Annex A 5.30 (Prontezza ICT), 8.13 (Backup delle informazioni), 8.14 (Ridondanza) |
| ISO/IEC 27002:2022 | Sezioni 5.30, 8.13, 8.14 — Linee guida per l'implementazione |
| ISO/IEC 22301 | Sistemi di gestione della continuità operativa (riferimento informativo) |
| NIST SP 800-34 Rev 1 | Guida alla pianificazione delle contingenze (riferimento informativo) |
| CIS Controls v8 | Controllo 11 (Recupero dei dati) |
| DORA (condizionale) | Art. 11–12 — Continuità operativa ICT, policy di backup, piani di disaster recovery, test annuali |
| NIS2 (condizionale) | Art. 21 — Continuità operativa e gestione delle crisi, gestione dei backup |
| FINMA (condizionale) | Gestione della continuità operativa per gli istituti finanziari svizzeri |

---

<!-- QA_VERIFIED: 2026-04-03 -->
