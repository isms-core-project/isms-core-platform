<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.12-13-IT:operational:OP-POL:a.7.12-13 -->
**ISMS-OP-POL-A.7.12-13 — Sicurezza dei cablaggi e manutenzione delle attrezzature**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza dei cablaggi e manutenzione delle attrezzature |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.7.12-13 |
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

- ISO/IEC 27001:2022 Controlli A.7.12, A.7.13 — Sicurezza dei cablaggi, Manutenzione delle attrezzature
- ISO/IEC 27002:2022 Sezioni 7.12, 7.13 — Guida all'implementazione
- NIST SP 800-53 Rev 5 PE-4 (Controllo degli accessi per la trasmissione), PE-9 (Attrezzature elettriche e cablaggi), MA-2 (Manutenzione controllata), MA-5 (Personale di manutenzione)
- IEC 11801 / EN 50173 / TIA-568 — Standard per il cablaggio strutturato
- NIN svizzera (Niederspannungs-Installationsnorm) — Standard per installazioni a bassa tensione

**Controlli Allegato A correlati**:

| Controllo | Relazione con la sicurezza dei cablaggi e la manutenzione delle attrezzature |
|-----------|-------------------------------------------------------------------------------|
| A.5.9 Inventario delle informazioni e delle altre risorse associate | L'inventario delle risorse garantisce la completezza del programma di manutenzione |
| A.5.24–28 Ciclo di vita della gestione degli incidenti | I guasti alle infrastrutture vengono gestiti tramite il processo di gestione degli incidenti |
| A.5.30 Preparazione ICT per la continuità operativa | La disponibilità delle attrezzature supporta gli obiettivi di continuità operativa |
| A.7.1–3 Perimetri di sicurezza fisica e accesso | Controllo degli accessi alle sale cavi e agli armadi di distribuzione |
| A.7.4 Monitoraggio della sicurezza fisica | Monitoraggio delle aree infrastrutturali dove passano i cablaggi |
| A.7.5 Protezione contro minacce fisiche e ambientali | Protezione ambientale per cablaggi e attrezzature |
| A.7.8–9 Ubicazione e protezione delle attrezzature | Il posizionamento delle attrezzature tiene conto del percorso dei cavi e dell'accesso per la manutenzione |
| A.7.14 Smaltimento sicuro o riutilizzo delle attrezzature | Le procedure di smaltimento si applicano al ritiro delle attrezzature a fine vita dopo la manutenzione |
| A.8.6 Gestione della capacità | La pianificazione della capacità informa la programmazione della manutenzione e il dimensionamento dell'infrastruttura di cablaggio |
| A.8.32 Gestione delle modifiche | Le modifiche all'infrastruttura e al cablaggio seguono il processo di gestione delle modifiche |

**Politiche interne correlate**:

- Politica di controllo degli accessi fisici
- Politica di sicurezza delle infrastrutture fisiche
- Politica di ubicazione e protezione delle attrezzature
- Politica di gestione delle risorse
- Politica di gestione delle modifiche
- Politica di gestione degli incidenti
- Politica di continuità operativa e disaster recovery

---

# Politica di sicurezza dei cablaggi e manutenzione delle attrezzature

## Scopo

Lo scopo della presente politica è proteggere l'infrastruttura fisica che trasporta e tratta le informazioni — nello specifico i cablaggi di alimentazione e dati e le attrezzature ad essi collegate. Il cablaggio costituisce il sistema nervoso dell'ambiente di elaborazione delle informazioni dell'organizzazione. I cavi non protetti sono vulnerabili all'intercettazione, alle interferenze elettromagnetiche e ai danni fisici. Le attrezzature manutenute in modo inadeguato si deteriorano, si guastano e creano esposizioni di sicurezza. La presente politica stabilisce i requisiti per entrambi.

I Controlli A.7.12 (Sicurezza dei cablaggi) e A.7.13 (Manutenzione delle attrezzature) sono combinati in quanto riguardano aspetti complementari della protezione dell'infrastruttura: il cablaggio fornisce le fondamenta della connettività, e la manutenzione garantisce l'affidabilità nel tempo. Condividono strutture, personale e processi di valutazione comuni.

La presente politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere la disponibilità, l'integrità e la riservatezza dei dati personali attraverso controlli sull'infrastruttura fisica. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano altresì i requisiti del GDPR Art. 32 relativi alla sicurezza del trattamento, incluse le misure fisiche.

## Ambito di applicazione

Tutti i dipendenti, i collaboratori e il personale di manutenzione di terze parti con accesso all'infrastruttura di cablaggio o alle attrezzature che richiedono manutenzione.

Ciò include:

- **Cablaggio**: Cavi di alimentazione, cavi di rete (rame e fibra ottica), cavi di telecomunicazione, sistemi di cablaggio strutturato, patch panel, quadri di distribuzione, passerelle cavi, condotti e percorsi.
- **Attrezzature**: Server, dispositivi di rete (switch, router, firewall), sistemi di storage, gruppi UPS, PDU, sistemi HVAC a supporto dell'elaborazione delle informazioni, sistemi di sicurezza fisica (controllo accessi, CCTV) e attrezzature di telecomunicazione.
- **Strutture**: Data center, sale server, armadi di distribuzione, sale telecomunicazioni, risers per cavi e percorsi sotterranei.
- **Attività**: Installazione di cavi, ispezione di cavi, manutenzione delle attrezzature, manutenzione preventiva, manutenzione correttiva, manutenzione da remoto e rimozione delle attrezzature per riparazione.

**Fuori ambito**:

- Controllo degli accessi fisici alle aree infrastrutturali (disciplinato da A.7.1–3).
- Sistemi di monitoraggio e protezione ambientale (disciplinati da A.7.4–5-11).
- Smaltimento delle attrezzature e distruzione sicura (disciplinati da A.7.14 e A.7.10).
- Infrastruttura cloud-hosted gestita interamente dal fornitore cloud (disciplinata attraverso la gestione dei fornitori, A.5.19–23). Laddove l'organizzazione operi esclusivamente in cloud senza attrezzature in sede, i Controlli A.7.12 e A.7.13 possono essere contrassegnati come "Non applicabili" nella Dichiarazione di applicabilità con giustificazione documentata.

## Principio

I cavi che trasportano energia o dati dovrebbero essere protetti da intercettazioni, interferenze e danni. Le attrezzature dovrebbero essere manutenute correttamente per garantire disponibilità, integrità e riservatezza delle informazioni. I livelli di protezione e manutenzione devono essere proporzionati alla criticità delle risorse servite, determinati attraverso la valutazione del rischio e la classificazione delle risorse dell'organizzazione.

---

## Standard di protezione dei cavi (A.7.12)

> *I cavi che trasportano energia, dati o che supportano i servizi informativi dovrebbero essere protetti da intercettazioni, interferenze e danni.*

### Protezione fisica dei cavi

Tutti i cavi che trasportano energia, dati o che supportano i servizi informativi devono essere fisicamente protetti:

- I cavi devono essere instradati attraverso percorsi protetti — condotti, passerelle cavi, pavimenti sopraelevati o controsoffitti — e non esposti in aree aperte.
- Il cablaggio sotterraneo deve essere protetto da danni accidentali mediante condotti blindati o sistemi a canale. I marker di percorso devono identificare i tracciati dei cavi interrati.
- I cavi devono essere protetti da rischi ambientali tra cui infiltrazioni d'acqua, fonti di calore, esposizione chimica e impatti fisici. I percorsi dei cavi devono evitare aree ad alto rischio di danneggiamento.
- Laddove i cavi attraversino tra edifici, deve essere applicata una protezione adeguata (cavo blindato, canale sigillato o condotto interrato diretto).
- Gli armadi di distribuzione, le sale telecomunicazioni e i quadri di distribuzione dei cavi devono essere fisicamente protetti. Queste aree devono essere chiuse a chiave quando non occupate e l'accesso deve essere limitato al personale autorizzato.
- I pozzetti di ispezione e i punti di accesso ai cunicoli devono essere protetti e l'accesso registrato.

### Protezione elettromagnetica

- I cavi devono essere protetti dalle interferenze elettromagnetiche (EMI) mediante schermatura appropriata, separazione dalle fonti di interferenza e selezione del tipo di cavo adatto all'ambiente.
- In ambienti con elevate interferenze elettromagnetiche (es. in prossimità di apparecchiature elettriche pesanti, macchinari industriali o trasmettitori radio), devono essere utilizzati cavi schermati (STP/FTP) o cavi in fibra ottica.
- Le installazioni di cablaggio devono essere conformi allo standard di cablaggio strutturato adottato dall'organizzazione (IEC 11801 / EN 50173 / TIA-568 secondo applicabilità) per i requisiti di schermatura e separazione.

---

## Segregazione dei cavi

### Separazione alimentazione e dati

I cavi di alimentazione e i cavi di comunicazione devono essere segregati per prevenire le interferenze elettromagnetiche:

- Le distanze minime di separazione devono seguire lo standard di cablaggio strutturato adottato dall'organizzazione. Come riferimento di base: separazione minima di 200 mm tra cavi dati non schermati e cavi di alimentazione che corrono in parallelo. Dove un incrocio è inevitabile, i cavi devono incrociarsi ad angolo retto.
- I cavi di alimentazione e i cavi dati devono utilizzare condotti, passerelle cavi o percorsi separati. I percorsi condivisi non sono consentiti per cavi dati non schermati e cavi di alimentazione.
- I requisiti di separazione devono essere documentati nello standard di cablaggio dell'organizzazione e applicati in modo coerente in tutte le installazioni.

### Separazione per classificazione di rete

- I cavi che trasportano traffico di classificazioni di sicurezza diverse devono essere fisicamente separati ove fattibile, o chiaramente identificati mediante codifica a colori o etichettatura per prevenire cross-connection.
- I cavi di rete ad alta sicurezza (es. reti di gestione, sistemi finanziari, sistemi di sicurezza) devono essere identificabili tramite una convenzione di codifica a colori o etichettatura coerente definita dall'organizzazione.

---

## Documentazione e etichettatura dei cavi

### Requisiti di documentazione

L'infrastruttura di cablaggio deve essere documentata e aggiornata:

- Un registro dei cavi o un database di gestione del cablaggio deve registrare tutte le installazioni di cablaggio strutturato, inclusi tipo di cavo, endpoint, percorso, data di installazione e classificazione.
- I disegni as-built del cablaggio devono essere mantenuti per tutte le strutture. I disegni devono mostrare i percorsi dei cavi, le ubicazioni dei patch panel, i quadri di distribuzione e le interconnessioni.
- La documentazione del cablaggio deve essere tenuta aggiornata. Tutte le modifiche al cablaggio devono essere riflesse nella documentazione entro 5 giorni lavorativi dal completamento.
- La documentazione del cablaggio deve essere protetta e ad accesso controllato. Solo il personale autorizzato deve avere accesso ai diagrammi di cablaggio dettagliati (questi rivelano la topologia di rete e i percorsi fisici).

### Standard di etichettatura

- Tutti i cavi devono essere etichettati a entrambe le estremità con un identificatore univoco che si colleghi al registro dei cavi.
- Patch panel, quadri di distribuzione e prese di telecomunicazione devono essere chiaramente etichettati.
- Le etichette devono essere durevoli, leggibili e consentire l'identificazione senza necessità di consultare la documentazione dettagliata per le operazioni di routine.
- L'organizzazione deve definire e documentare una convenzione di etichettatura coerente (es. edificio-piano-sala-rack-porta).

### Controllo delle modifiche al cablaggio

Tutte le installazioni, le modifiche e le rimozioni di cablaggio devono seguire il processo di gestione delle modifiche dell'organizzazione (A.8.32) con i seguenti requisiti specifici:

#### Requisiti delle richieste di modifica

Le richieste di modifica del cablaggio devono includere:
- **Giustificazione aziendale**: Perché la modifica è necessaria
- **Ambito**: Cavi specifici, percorsi e punti di terminazione interessati
- **Valutazione dell'impatto sui servizi**: Potenziale downtime, sistemi/servizi interessati
- **Piano di implementazione**: Procedura passo-passo incluso il piano di test
- **Piano di rollback**: Come ripristinare il servizio in caso di fallimento dell'implementazione
- **Aggiornamenti della documentazione**: Quali diagrammi e registri saranno aggiornati

#### Requisiti di approvazione

| Tipo di modifica | Approvazione richiesta | Test richiesti | Scadenza aggiornamento documentazione |
|-----------------|----------------------|----------------|--------------------------------------|
| **Nuova installazione di cablaggio** | Responsabile IT Operations + Responsabile della struttura | Test del cablaggio (continuità, prestazioni) per gli standard IEC/TIA | 5 giorni lavorativi |
| **Rimozione del cablaggio** | Responsabile IT Operations | Verifica dell'assenza di connessioni attive prima della rimozione | 5 giorni lavorativi |
| **Modifica del percorso del cablaggio** | Responsabile IT Operations + Responsabile della struttura | Test del cablaggio post-modifica | 5 giorni lavorativi |
| **Installazione/modifica fibra ottica** | RSSI + Responsabile IT Operations (infrastruttura ad alta sicurezza) | Test fibra (attenuazione, continuità) | 5 giorni lavorativi |
| **Riparazione d'emergenza** | Responsabile IT Operations (approvazione post-implementazione entro 24 ore) | Test post-riparazione obbligatori | 2 giorni lavorativi |

#### Test e convalida

Tutte le modifiche al cablaggio devono includere test post-implementazione:
- **Cavo in rame**: Continuità, mappatura dei fili, lunghezza, attenuazione, diafonia near-end (NEXT), perdita di ritorno per i requisiti TIA-568 Categoria 6A come minimo
- **Cavo in fibra ottica**: Perdita ottica, continuità, polarità per TIA-568 o specifiche del produttore
- **Documentazione dei risultati dei test**: Report dei test conservati con il registro delle modifiche; i test falliti richiedono rimedio prima dell'accettazione
- **Criteri di accettazione**: Devono soddisfare o superare le specifiche di prestazione dello standard di cablaggio pertinente

#### Revisione post-implementazione

Entro 30 giorni dalle modifiche al cablaggio che interessano più di 10 connessioni o infrastrutture critiche:
- Revisione dell'impatto effettivo sui servizi rispetto al previsto
- Revisione dei risultati dei test e delle eventuali deviazioni dal piano
- Aggiornamento degli standard o delle procedure di cablaggio in base alle lezioni apprese
- Documentazione dei risultati della revisione nel registro delle modifiche

- I cavi inutilizzati devono essere disconnessi, documentati e rimossi o chiaramente contrassegnati come inattivi.
- Devono essere condotte ispezioni fisiche trimestrali per identificare aggiunte, modifiche o danni non autorizzati. I risultati devono essere riconciliati con i disegni as-built e i registri delle modifiche, con i risultati documentati e firmati dal Responsabile della struttura.

---

## Requisiti per la fibra ottica

Il cavo in fibra ottica deve essere utilizzato in preferenza al rame per la trasmissione dati nelle seguenti circostanze:

- **Aree ad alta sicurezza**: Sale server, data center e zone sicure dove il rischio di intercettazione è elevato. Il cavo in fibra ottica non emette radiazioni elettromagnetiche ed è significativamente più difficile da intercettare senza rilevamento rispetto al cavo in rame.
- **Percorsi a lunga distanza**: Tra edifici, tra piani (risers) e qualsiasi percorso orizzontale superiore a 90 metri (limite di distanza rame Categoria 6A).
- **Requisiti di larghezza di banda elevata**: Dove le esigenze di larghezza di banda superano le capacità del rame (es. 40 Gbps e oltre).
- **Ambienti sensibili alle EMI**: Aree con elevate interferenze elettromagnetiche dove le prestazioni del cavo in rame sarebbero degradate.

Dove la fibra ottica è installata, la giunzione a fusione deve essere utilizzata per le connessioni permanenti (non giunzione meccanica) nelle aree sicure. I patch panel in fibra devono essere alloggiati in contenitori chiusi a chiave.

Dove il cavo in rame viene utilizzato in aree con rischio di intercettazione, devono essere specificati cavi schermati (STP/FTP) e i percorsi dei cavi devono essere fisicamente protetti.

---

## Ispezione e manutenzione dei cavi

Devono essere eseguite regolari ispezioni e manutenzioni dell'infrastruttura di cablaggio:

- L'infrastruttura di cablaggio deve essere inclusa nel programma di manutenzione dell'organizzazione con intervalli di ispezione definiti.
- Devono essere condotte ispezioni visive trimestrali per i percorsi dei cavi accessibili, verificando danni, modifiche non autorizzate, integrità dell'etichettatura e ostruzioni del percorso.
- Test formali del cablaggio (continuità, prestazioni) devono essere condotti annualmente o a seguito di problemi segnalati.
- I cavi danneggiati devono essere riparati o sostituiti tempestivamente. Le riparazioni temporanee devono essere documentate e la riparazione permanente programmata entro 30 giorni di calendario.
- I risultati delle ispezioni devono essere documentati e conservati per un minimo di 3 anni.

---

## Programma di manutenzione (A.7.13)

> *Le attrezzature dovrebbero essere manutenute correttamente per garantire disponibilità, integrità e riservatezza delle informazioni.*

### Istituzione del programma

L'organizzazione deve istituire e mantenere un programma di manutenzione che copra tutte le attrezzature che trattano, memorizzano o supportano l'elaborazione delle informazioni:

- Tutte le attrezzature in ambito registrate nell'inventario delle risorse (per A.5.9) devono essere incluse nel programma di manutenzione. L'inventario delle risorse è la fonte autorevole per la completezza del programma.
- La riconciliazione trimestrale deve verificare che tutte le attrezzature inventariate abbiano copertura di manutenzione. I risultati della riconciliazione e la firma devono essere conservati come prove.
- I calendari di manutenzione devono seguire le raccomandazioni del produttore come minimi. Le deviazioni richiedono l'accettazione documentata del rischio tramite il registro delle eccezioni.
- Il programma di manutenzione deve essere gestito tramite [CMMS] o sistema equivalente di tracciamento della manutenzione. Laddove non sia disponibile un CMMS dedicato, deve essere utilizzato un foglio di calcolo o registro controllato.

### Calendario di manutenzione

Si applicano le seguenti frequenze minime di manutenzione preventiva:

| Categoria di attrezzature | Frequenza manutenzione preventiva | Attività |
|--------------------------|----------------------------------|----------|
| **Server** | Annuale | Aggiornamenti firmware, pulizia, ispezione fisica, controlli di salute dei componenti |
| **Attrezzature di rete** (switch, router, firewall) | Semestrale | Aggiornamenti firmware, pulizia ventole, ispezione porte, revisione log |
| **Sistemi UPS** | Controllo batterie trimestrale; test completo di capacità annuale | Condizione batteria, test di carico, test di trasferimento, integrità delle connessioni |
| **PDU** | Annuale | Ispezione connessioni, revisione bilanciamento carico, termografia |
| **HVAC/Raffreddamento** (a servizio delle aree IT) | Trimestrale | Sostituzione filtri, controllo refrigerante, verifica delle prestazioni |
| **Rilevamento incendi e soppressione** | Per regolamenti cantonali antincendio (minimo annuale) | Test dei rilevatori, ispezione del sistema, verifica dell'agente di soppressione |
| **Sistemi di sicurezza fisica** (controllo accessi, CCTV) | Semestrale | Salute delle telecamere, test dei lettori, firmware del controller, verifica della registrazione |
| **Cablaggio strutturato** | Annuale (ispezione visiva trimestrale) | Test del cablaggio, ispezione del percorso, verifica dell'etichettatura |

I calendari di manutenzione devono essere adeguati in base all'età delle attrezzature, alle condizioni ambientali, agli avvisi del produttore e alla storia degli incidenti. Le attrezzature che si avvicinano alla fine vita devono avere la frequenza di manutenzione aumentata o essere pianificate per la sostituzione.

---

## Disponibilità e continuità dei servizi

Il cablaggio e l'infrastruttura delle attrezzature supportano direttamente gli impegni di disponibilità del servizio dell'organizzazione nei confronti dei clienti. Le attività di manutenzione devono essere pianificate ed eseguite per ridurre al minimo le interruzioni del servizio.

### Valutazione dell'impatto sui servizi

Tutte le attività di manutenzione devono essere valutate per il potenziale impatto sui servizi prima della programmazione:

| Livello di impatto | Definizione | Notifica al cliente | Approvazione richiesta |
|--------------------|------------|---------------------|------------------------|
| **Impatto zero** | Sistema ridondante; nessuna interruzione del servizio | Nessuna | Responsabile IT Operations |
| **Impatto minore** | Possibile breve degrado delle prestazioni (<5 minuti) | Preavviso 48 ore | Responsabile IT Operations |
| **Impatto moderato** | Interruzione pianificata del servizio (5-60 minuti) | Preavviso 5 giorni lavorativi | RSSI + Proprietario del business |
| **Impatto maggiore** | Interruzione prolungata (>60 minuti) o servizio rivolto al cliente offline | Preavviso 10 giorni lavorativi | Direzione esecutiva + approvazione del cliente (se contrattuale) |

### Finestre di manutenzione

- **Finestra di manutenzione standard**: [Definire: es. "Domeniche 02:00-06:00 ora locale" o "Primo sabato del mese 20:00-mezzanotte"]
- Tutta la manutenzione non di emergenza che può avere impatto sui servizi deve essere programmata durante le finestre di manutenzione approvate
- La manutenzione d'emergenza al di fuori delle finestre di manutenzione richiede l'approvazione del RSSI e la notifica immediata al cliente (laddove l'impatto superi le soglie SLA)

### Impatto sull'obiettivo di disponibilità

Il programma di manutenzione dell'infrastruttura deve supportare gli impegni di disponibilità dell'organizzazione:

| Servizio | Impegno di disponibilità | Downtime annuale massimo consentito | Contributo dell'infrastruttura |
|---------|--------------------------|-------------------------------------|-------------------------------|
| [Servizio principale] | Uptime 99,5% | 43,8 ore | Manutenzione pianificata: <24 ore annue; Guasti non pianificati: <20 ore annue |
| [Servizio secondario] | Uptime 99,0% | 87,6 ore | Manutenzione pianificata: <40 ore annue; Guasti non pianificati: <48 ore annue |

**Vincolo di programmazione della manutenzione preventiva**: Il downtime pianificato totale per la manutenzione dell'infrastruttura non deve superare il 50% del budget annuale di downtime consentito, riservando capacità per i guasti non pianificati.

### Requisiti di ridondanza

Il programma di manutenzione delle attrezzature deve tenere conto della progettazione della ridondanza:

- **Singoli punti di guasto**: Le attrezzature prive di ridondanza devono avere la manutenzione programmata durante i periodi di basso utilizzo con preavviso al cliente
- **Sistemi ridondanti**: Dove esiste ridondanza N+1 o 2N, la manutenzione deve essere scaglionata per mantenere almeno la capacità N in ogni momento
- **Attrezzature sul percorso critico** (UPS, rete core, server primari): La manutenzione deve includere la verifica dello stato di ridondanza pre-manutenzione e il test di failover post-manutenzione

### Capacità durante la manutenzione

Quando le attrezzature ridondanti vengono portate offline per la manutenzione, la capacità rimanente deve essere verificata sufficiente per il carico attuale più un buffer del 20%:
- Se la capacità scende al di sotto della soglia del buffer, la manutenzione deve essere riprogrammata o deve essere predisposta capacità temporanea aggiuntiva
- Il test di carico dopo la manutenzione deve verificare il completo ripristino della ridondanza prima che le attrezzature vengano contrassegnate come "in servizio"

### Dipendenze per continuità operativa e disaster recovery

Il programma di manutenzione dell'infrastruttura deve supportare la pianificazione della continuità operativa:

#### Identificazione delle infrastrutture critiche

Le attrezzature e il cablaggio critici per la continuità operativa devono essere identificati e prioritizzati:

| Classificazione | Definizione | Priorità di manutenzione | Parti di ricambio |
|-----------------|------------|--------------------------|-------------------|
| **Tier 1 - Mission Critical** | Attrezzature il cui guasto causa un'interruzione immediata del servizio senza soluzioni alternative | Priorità massima; manutenzione preventiva mai rinviata | Ricambi critici in loco o disponibili entro <4 ore |
| **Tier 2 - Business Critical** | Attrezzature il cui guasto causa degrado del servizio o influenza un sottoinsieme di utenti | Alta priorità; la manutenzione può essere rinviata al massimo 30 giorni con approvazione del RSSI | Parti di ricambio disponibili entro 24 ore |
| **Tier 3 - Importante** | Attrezzature il cui guasto causa inconvenienti ma i servizi rimangono operativi | Priorità standard; i rinvii della manutenzione sono consentiti con giustificazione documentata | Parti di ricambio ordinate su richiesta |

#### Test dell'infrastruttura di disaster recovery

- Il **test annuale di failover DR** deve includere i componenti dell'infrastruttura:
  - Sistemi di alimentazione di backup (UPS, generatore se presente)
  - Percorsi di rete ridondanti
  - Sistemi di raffreddamento di backup
  - Percorsi di cablaggio critici (verificare che esistano percorsi alternativi documentati)
- Il test DR deve verificare che il programma di manutenzione abbia mantenuto l'infrastruttura in uno stato pronto per il DR
- I risultati del test DR che rivelano lacune nell'infrastruttura devono attivare aggiornamenti al programma di manutenzione

#### Infrastruttura del sito alternativo

Se l'organizzazione mantiene un sito di disaster recovery:
- Tutti i requisiti del programma di manutenzione si applicano alle attrezzature del sito DR
- L'infrastruttura di cablaggio del sito DR è documentata agli stessi standard del sito primario
- Sincronizzazione delle attività di manutenzione (se le batterie UPS primarie vengono sostituite, le batterie del sito DR vengono valutate e sostituite se necessario)
- La manutenzione delle attrezzature del sito DR può avere frequenza inferiore se l'ambiente è controllato e le attrezzature sono utilizzate raramente (con giustificazione documentata)

---

## Autorizzazione del personale di manutenzione

### Personale interno

- Solo il personale con autorizzazione documentata deve eseguire la manutenzione delle attrezzature informatiche.
- L'autorizzazione alla manutenzione deve specificare le categorie di attrezzature e le attività di manutenzione che l'individuo è qualificato a eseguire.
- I registri di autorizzazione devono essere mantenuti e rivisti annualmente.

### Personale di manutenzione di terze parti

- La manutenzione di terze parti deve essere eseguita solo da fornitori contrattualizzati e approvati. I contratti di manutenzione devono includere obblighi di riservatezza e requisiti di sicurezza.
- Il personale di manutenzione di terze parti deve essere identificato e verificato (documento d'identità rilasciato da un'autorità governativa) prima di ottenere l'accesso alle attrezzature.
- L'organizzazione deve mantenere un registro dei fornitori di manutenzione di terze parti approvati, rivisto annualmente.

### Requisiti di supervisione

- Il personale di manutenzione di terze parti deve essere supervisionato quando accede a attrezzature che trattano o memorizzano informazioni sensibili o riservate, salvo che una valutazione documentata del rischio concluda che l'accesso non supervisionato è accettabile (es. contratto di manutenzione dedicato con personale controllato, attrezzature isolate).
- L'accesso non supervisionato di manutenzione di terze parti deve essere registrato con identificazione individuale, orario di entrata/uscita e attrezzature accedute.
- I registri di supervisione devono essere mantenuti come prove.

---

## Gestione dei fornitori di manutenzione di terze parti

### Requisiti contrattuali

I contratti di manutenzione con fornitori di terze parti devono includere:

| Elemento contrattuale | Requisito |
|-----------------------|-----------|
| **Service Level Agreement (SLA)** | Tempo di risposta (arrivo in loco); tempo di risoluzione; procedure di escalation |
| **Orario di copertura** | 24x7 per attrezzature critiche; orario lavorativo per attrezzature non critiche |
| **Disponibilità delle parti di ricambio** | Ricambi critici in loco o impegno di consegna entro <4 ore |
| **Requisiti di sicurezza** | Verifiche dei precedenti per il personale; obblighi di riservatezza; accettazione della supervisione |
| **Protezione dei dati** | Procedure di gestione dei dati; capacità di cancellazione sicura; obblighi di notifica delle violazioni dei dati |
| **Reportistica** | Report di servizio mensili; riunioni annuali di revisione delle prestazioni |
| **Assicurazione** | Responsabilità professionale; responsabilità informatica (per i fornitori di accesso remoto) |
| **Diritti di rescissione** | Rescissione per violazione della sicurezza; obblighi di assistenza alla transizione |

### Monitoraggio delle prestazioni del fornitore

Le prestazioni del fornitore di manutenzione devono essere tracciate e revisionate:

| Metrica | Obiettivo | Frequenza di revisione |
|---------|-----------|------------------------|
| **Conformità SLA (tempo di risposta)** | >95% | Trimestrale |
| **Conformità SLA (tempo di risoluzione)** | >90% | Trimestrale |
| **Qualità della manutenzione** | <5% di guasti ricorrenti entro 30 giorni | Trimestrale |
| **Tasso di incidenti di sicurezza** | 0 | Per evento |
| **Soddisfazione del cliente** (utenti interni) | >4/5 | Per evento di servizio |
| **Conformità alla documentazione** | 100% dei report di servizio ricevuti nei tempi | Trimestrale |

### Revisione annuale del fornitore

Ogni fornitore di manutenzione deve ricevere una revisione annuale che comprenda:
- Prestazioni SLA rispetto agli obiettivi
- Conformità alla sicurezza (rispetto della supervisione, record privo di incidenti)
- Rapporto costo-efficacia rispetto alle alternative
- Reattività e qualità della comunicazione
- Raccomandazione: Continuare, rinegoziare o sostituire

**Documentazione della revisione**: Conservata per 3 anni; le decisioni di rinnovo/sostituzione documentate con giustificazione.

### Incidenti di sicurezza del fornitore

Se un fornitore di manutenzione causa o contribuisce a un incidente di sicurezza:
1. **Azione immediata**: Sospendere l'accesso del fornitore in attesa di indagini
2. **Indagine**: Analisi della causa principale; determinare se si è verificata una violazione contrattuale
3. **Azione correttiva**: Piano di rimedio fornito dal fornitore; supervisione potenziata se l'accesso viene ripristinato
4. **Revisione del contratto**: Valutare se la rescissione è giustificata; documentare la decisione
5. **Lezioni apprese**: Aggiornare le procedure di gestione dei fornitori o i requisiti contrattuali

---

## Sicurezza durante la manutenzione

### Protezione dei dati durante la manutenzione

- I dati sensibili devono essere protetti durante tutte le attività di manutenzione. Il personale di manutenzione non deve avere accesso ai dati memorizzati sulle attrezzature salvo ove specificamente richiesto e autorizzato.
- Le attrezzature contenenti dati non devono essere rimosse dalle strutture per la manutenzione laddove la riparazione in loco sia fattibile.
- Se è richiesta la manutenzione fuori sede, i dati devono essere cancellati in modo sicuro dalle attrezzature prima della rimozione (per le procedure di smaltimento sicuro A.7.14), oppure il supporto di memorizzazione deve essere rimosso e conservato dall'organizzazione.
- Per le attrezzature in cui la cancellazione dei dati non è fattibile prima della rimozione (es. il guasto impedisce l'accesso), deve essere completata una valutazione documentata del rischio e gli obblighi di gestione dei dati del fornitore di manutenzione devono essere confermati per iscritto.

### Verifica fisica dopo la manutenzione

- Dopo la manutenzione, le attrezzature devono essere fisicamente ispezionate prima di essere rimesse in servizio per verificare che non siano state apportate modifiche non autorizzate.
- Tutti gli strumenti e le attrezzature portate in loco dal personale di manutenzione devono essere contabilizzati prima e dopo la manutenzione.
- Le versioni di firmware e software devono essere verificate dopo la manutenzione per confermare l'assenza di modifiche non autorizzate.

### Controlli degli accessi per la manutenzione

- L'accesso per la manutenzione deve essere limitato nel tempo. Le finestre di accesso devono essere concordate in anticipo e documentate.
- Tutto l'accesso per la manutenzione deve essere registrato: chi ha eseguito il lavoro, quando, a quali attrezzature si è avuto accesso e quale lavoro è stato eseguito.
- Al personale di manutenzione devono essere emesse credenziali di accesso temporanee (badge, accesso ai sistemi) che scadono al termine della finestra di manutenzione.

---

## Manutenzione da remoto

La manutenzione da remoto introduce rischi aggiuntivi. Si applicano i seguenti controlli:

- La manutenzione da remoto deve essere esplicitamente autorizzata prima di ogni sessione. L'autorizzazione permanente per l'accesso remoto non è consentita.
- Le sessioni di manutenzione da remoto devono utilizzare connessioni crittografate (VPN, SSH o protocollo sicuro equivalente). L'accesso remoto non crittografato non è consentito.
- Le sessioni di manutenzione da remoto devono essere registrate, inclusi orario di inizio/fine della sessione, identità dell'individuo e azioni eseguite. La registrazione della sessione è raccomandata per le attrezzature critiche.
- L'accesso remoto deve essere disabilitato quando non è attivamente in uso. Le connessioni di accesso remoto persistenti per scopi di manutenzione non devono rimanere aperte.
- La manutenzione da remoto delle attrezzature contenenti dati sensibili richiede la stessa autorizzazione dell'accesso fisico a tali attrezzature.
- Laddove il fornitore di manutenzione richieda l'accesso remoto ai sistemi interni, deve essere utilizzato un jump host o un bastion server dedicato con autenticazione a più fattori (AMF).

---

## Rimozione e restituzione delle attrezzature

Quando le attrezzature devono essere rimosse dalle strutture per la manutenzione fuori sede:

1. **Autorizzazione**: La rimozione deve essere autorizzata per iscritto dal proprietario delle attrezzature o dal delegato designato.
2. **Protezione dei dati**: I dati devono essere cancellati in modo sicuro prima della rimozione. Se la cancellazione non è possibile, il supporto di memorizzazione deve essere rimosso e conservato dall'organizzazione. L'approccio alla protezione dei dati deve essere documentato.
3. **Catena di custodia**: Deve essere creato un registro della catena di custodia con: identificazione delle attrezzature, condizioni al momento della rimozione, data/ora di rimozione, autorizzato da, vettore/trasportatore, destinazione, data di rientro prevista.
4. **Ispezione al rientro**: Al rientro, le attrezzature devono essere ispezionate per rilevare manomissioni, modifiche non autorizzate e correttezza della configurazione. Le versioni di firmware e software devono essere verificate.
5. **Aggiornamento del registro delle risorse**: Il rientro delle attrezzature deve essere registrato nel [Sistema di gestione delle risorse] con il riepilogo della manutenzione e i risultati dell'ispezione.

---

## Risposta agli incidenti di guasto delle infrastrutture

I guasti alle infrastrutture (danni ai cavi, malfunzionamento delle attrezzature) che hanno o potrebbero avere impatto sui servizi devono essere gestiti attraverso il processo di gestione degli incidenti dell'organizzazione.

### Classificazione degli incidenti per eventi infrastrutturali

| Gravità | Definizione | Esempi | Tempo di risposta | Notifica |
|---------|------------|--------|-------------------|---------|
| **P1 - Critica** | Interruzione completa del servizio o rischio imminente | Guasto all'alimentazione principale, guasto allo switch di rete core, interruzione completa del cavo | Risposta immediata; obiettivo di ripristino entro 1 ora | RSSI, Direzione esecutiva, clienti interessati immediatamente |
| **P2 - Alta** | Significativo degrado del servizio; ridondanza persa | Guasto UPS (rete elettrica operativa), guasto al link di backup, danno parziale al cavo | Risposta entro 2 ore; obiettivo di ripristino entro 4 ore | Responsabile IT Operations, RSSI, notifica al cliente se lo SLA è impattato |
| **P3 - Media** | Degrado minore; ridondanza intatta | Guasto a un singolo server (in cluster), guasto all'unità di raffreddamento (backup operativo) | Risposta entro 4 ore; obiettivo di ripristino entro 24 ore | Responsabile IT Operations |
| **P4 - Bassa** | Nessun impatto corrente sui servizi; avvisi di monitoraggio | Batteria UPS in invecchiamento, attrezzatura che scalda ma nei limiti di tolleranza | Risposta il prossimo giorno lavorativo; manutenzione programmata | IT Operations |

### Flusso di risposta agli incidenti infrastrutturali

1. **Rilevamento e registrazione**
   - Gli avvisi di monitoraggio dell'infrastruttura o le segnalazioni degli utenti attivano la creazione dell'incidente
   - Il ticket di incidente viene creato nel [Sistema di gestione degli incidenti] con classificazione della gravità
   - Valutazione iniziale: ambito dell'impatto, servizi interessati, clienti interessati

2. **Escalation**
   - P1: Escalation immediata al RSSI e al Responsabile IT Operations
   - P2: Escalation al Responsabile IT Operations entro 30 minuti
   - P3/P4: Assegnato all'ingegnere di turno

3. **Comunicazione**
   - **Interna**: Aggiornamenti sullo stato dell'incidente ogni 2 ore (P1), ogni 4 ore (P2) fino alla risoluzione
   - **Cliente**: Notifica per la tabella di valutazione dell'impatto sui servizi sopra; aggiornamenti di stato per i termini SLA
   - **Fornitori**: Coinvolgere i fornitori di manutenzione per le procedure di escalation contrattuale

4. **Indagine e rimedio**
   - Analisi della causa principale obbligatoria per tutti gli incidenti P1/P2
   - Soluzioni temporanee documentate con la correzione permanente programmata
   - Guasti alle attrezzature: Determinare la storia della manutenzione, lo stato della garanzia, i requisiti di sostituzione

5. **Revisione post-incidente**
   - Incidenti P1/P2: Revisione post-incidente entro 5 giorni lavorativi
   - Lezioni apprese: Identificare misure preventive, miglioramenti al programma di manutenzione
   - Documentazione: Aggiornare le procedure di manutenzione, gli standard di cablaggio o le soglie di monitoraggio in base ai risultati

### Raccolta delle prove per gli incidenti infrastrutturali

Gli incidenti infrastrutturali devono documentare:
- Cronologia degli eventi (rilevamento, escalation, azioni intraprese, risoluzione)
- Valutazione dell'impatto (servizi interessati, impatto sui clienti, durata del downtime)
- Analisi della causa principale (età delle attrezzature, storia della manutenzione, fattori ambientali)
- Azioni di risoluzione (riparazioni, sostituzioni, modifiche di configurazione)
- Azioni preventive (adeguamenti al calendario di manutenzione, miglioramenti al monitoraggio)

La documentazione della revisione post-incidente deve essere conservata per un minimo di 3 anni.

---

## Registri di manutenzione

### Requisiti di documentazione

Tutta la manutenzione — preventiva e correttiva — deve essere documentata:

- **Manutenzione preventiva**: Data, identificatore delle attrezzature, attività di manutenzione eseguite, risultati, parti sostituite, prossima data di manutenzione programmata, personale che ha eseguito il lavoro.
- **Manutenzione correttiva**: Data, identificatore delle attrezzature, descrizione del guasto, causa principale (ove determinata), azioni di riparazione intraprese, parti sostituite, risultati della verifica post-riparazione, personale che ha eseguito il lavoro.
- **Manutenzione da remoto**: Data/ora della sessione, attrezzature accedute, identità dell'individuo, azioni eseguite, durata della sessione.

### Conservazione dei registri

- I registri di manutenzione devono essere conservati per un minimo di 3 anni o per il ciclo di vita delle attrezzature, a seconda di quale sia il periodo più lungo.
- I registri devono essere disponibili per l'audit in qualsiasi momento.
- I registri devono essere conservati in [CMMS] o in un registro controllato equivalente.

### Analisi dei trend di manutenzione

- I registri di manutenzione devono essere esaminati trimestralmente per individuare trend: guasti ricorrenti, attrezzature che si avvicinano alla fine vita, frequenza crescente dei guasti o violazioni dello SLA di manutenzione.
- L'analisi dei trend deve informare la pianificazione della sostituzione delle attrezzature e gli adeguamenti al programma di manutenzione.
- I report di analisi dei trend trimestrali devono essere forniti al Responsabile IT Operations e al RSSI.

---

## Monitoraggio delle prestazioni dell'infrastruttura

Oltre alle metriche di completamento della manutenzione, l'organizzazione deve monitorare gli indicatori di salute dell'infrastruttura per consentire la manutenzione predittiva e dimostrare l'efficacia della disponibilità.

### Monitoraggio della salute delle attrezzature

| Metrica | Metodo di monitoraggio | Soglia di allerta | Frequenza di revisione |
|---------|----------------------|-------------------|------------------------|
| **Salute batteria UPS** | Test di impedenza della batteria | >20% degrado dalla baseline | Analisi dei trend mensile |
| **Capacità di autonomia UPS** | Test di carico annuale con banco di carico | <90% dell'autonomia nominale | Annuale con trend |
| **Temperatura delle attrezzature** | Sistema di monitoraggio ambientale | >80% della temperatura massima di esercizio | Avvisi continui |
| **Errori delle attrezzature di rete** | Monitoraggio SNMP / syslog | >0,1% tasso di errore dell'interfaccia | Revisione giornaliera |
| **Salute dell'hardware del server** | Monitoraggio dell'interfaccia di gestione (iDRAC, iLO) | Avvisi di guasto predittivo | Avvisi continui |
| **Prestazioni HVAC** | Sensori temperatura/umidità | Temp >24°C o <18°C; UR >60% o <40% | Avvisi continui |
| **Trend di consumo energetico** | Monitoraggio PDU | >80% della capacità nominale | Trend mensile |
| **Problemi all'infrastruttura di cablaggio** | Ticket dell'helpdesk, risultati delle ispezioni | Qualsiasi danno, modifiche non autorizzate | Revisione trimestrale |

### Trigger di manutenzione predittiva

Il monitoraggio della salute deve attivare azioni di manutenzione anticipate prima del guasto:

| Indicatore | Soglia di attivazione | Azione |
|------------|----------------------|--------|
| Degrado batteria UPS | Perdita di capacità del 15-20% | Pianificare la sostituzione della batteria entro 30 giorni |
| Temperatura delle attrezzature in aumento | Aumento medio su 3 mesi >5°C | Investigare il raffreddamento, pianificare pulizia approfondita |
| Errori dell'interfaccia di rete in aumento | Il trend su 3 mesi mostra un raddoppio degli errori | Pianificare test del cablaggio, ispezione dell'interfaccia |
| Avviso di guasto predittivo hardware del server | Errore SMART, errori ECC della memoria | Pianificare la sostituzione prima del guasto; verifica del backup |

### Dashboard delle metriche di disponibilità

Report mensile al Responsabile IT Operations e al RSSI:

| Metrica | Obiettivo | Calcolo |
|---------|-----------|---------|
| **Downtime non pianificato dell'infrastruttura** | <20 ore annue | Somma di tutte le durate degli incidenti P1/P2 |
| **Downtime pianificato per manutenzione** | <24 ore annue | Somma di tutte le durate delle finestre di manutenzione con impatto sui servizi |
| **Disponibilità dell'infrastruttura** | >99,5% | (Ore totali - ore di downtime) / Ore totali x 100% |
| **Mean Time Between Failures (MTBF)** | Trend in aumento | Tracciato per categoria di attrezzature |
| **Mean Time To Repair (MTTR)** | <4 ore (P1/P2) | Tempo medio dal rilevamento alla risoluzione |
| **Conformità manutenzione preventiva** | 100% | Completate nei tempi / Totale programmate x 100% |
| **Attrezzature oltre la fine vita** | 0 attrezzature critiche | Conteggio delle attrezzature critiche che superano la data EOL del produttore |

**Analisi trimestrale dei trend**: Rivedere le metriche per i trend in deterioramento; adeguare il programma di manutenzione o pianificare le sostituzioni delle attrezzature.

---

## Definizioni

| Termine | Definizione |
|---------|-------------|
| **Cablaggio strutturato** | Un'infrastruttura di cablaggio standardizzata (rame e fibra ottica) secondo gli standard di settore (IEC 11801, EN 50173, TIA-568) che fornisce un framework flessibile e affidabile per le comunicazioni voce, dati e video |
| **Infrastruttura di cablaggio** | Tutti i cavi di alimentazione e di comunicazione, condotti, percorsi, patch panel, quadri di distribuzione e punti di terminazione |
| **Cavo in fibra ottica** | Un cavo contenente una o più fibre ottiche che trasmettono dati come impulsi luminosi, offrendo larghezza di banda superiore, maggiore distanza, immunità alle EMI e maggiore resistenza all'intercettazione rispetto al cavo in rame |
| **Manutenzione preventiva** | Manutenzione programmata eseguita a intervalli definiti per prevenire guasti alle attrezzature e mantenere le prestazioni nelle specifiche |
| **Manutenzione correttiva** | Manutenzione non pianificata eseguita per ripristinare le attrezzature alle condizioni operative a seguito di un guasto o malfunzionamento |
| **Manutenzione da remoto** | Manutenzione eseguita tramite accesso di rete remoto senza presenza fisica all'ubicazione delle attrezzature |
| **Catena di custodia** | Un registro cronologico documentato del trasferimento della responsabilità per le attrezzature, che traccia il possesso dalla rimozione attraverso la manutenzione fino al rientro |
| **CMMS** | Sistema di gestione della manutenzione computerizzato — software utilizzato per pianificare, tracciare e documentare le attività di manutenzione |
| **EMI** | Interferenza elettromagnetica — rumore elettrico indesiderato da fonti esterne che può degradare la qualità del segnale nei cavi dati |

---

## Ruoli e responsabilità

| Ruolo | Responsabilità per cablaggio e manutenzione |
|-------|---------------------------------------------|
| **Direzione esecutiva** | Approvare la politica; allocare il budget per la manutenzione dell'infrastruttura e gli aggiornamenti del cablaggio |
| **RSSI** | Titolarità della politica; standard di sicurezza per le attività di manutenzione; accettazione del rischio per le eccezioni; reportistica trimestrale sulla conformità dell'infrastruttura |
| **Responsabile IT Operations** | Titolarità del programma di manutenzione delle attrezzature; gestione dei fornitori di manutenzione; supervisione del calendario di manutenzione; revisione dell'analisi dei trend |
| **Responsabile della struttura** | Titolarità dell'infrastruttura di cablaggio; manutenzione e ispezione del cablaggio; coordinamento dei servizi dell'edificio; gestione dei percorsi fisici |
| **Proprietari di sistema** | Garantire che le attrezzature di propria competenza siano incluse nel programma di manutenzione; autorizzare la rimozione delle attrezzature; definire i requisiti di protezione dei dati per la manutenzione |
| **IT Operations** | Esecuzione e coordinamento della manutenzione quotidiana; tenuta dei registri di manutenzione; gestione delle sessioni di manutenzione da remoto |
| **Audit interno** | Verifica annuale della conformità al programma di manutenzione; audit dell'infrastruttura di cablaggio; revisione delle prove |
| **Tutti i dipendenti** | Segnalare tempestivamente eventuali danni ai cavi, guasti alle attrezzature o modifiche non autorizzate all'infrastruttura |

### Percorso di escalation

- Danni ai cavi o modifiche non autorizzate rilevate: L'individuo che segnala notifica il Responsabile della struttura. Il Responsabile della struttura valuta l'impatto e notifica il RSSI se rilevante per la sicurezza.
- Guasti alla manutenzione delle attrezzature: IT Operations notifica il Responsabile IT Operations. I guasti alle attrezzature critiche vengono escalati al RSSI.
- Problemi di sicurezza durante la manutenzione: Qualsiasi membro del personale notifica direttamente il RSSI.

---

## Prove

Le seguenti prove dimostrano la conformità alla presente politica. **Per gli audit SOC 2 Tipo II**, i revisori testeranno l'efficacia operativa nel periodo di audit (tipicamente 12 mesi).

| # | Prova | Responsabile | Frequenza | Requisiti della pista di audit |
|---|-------|-------------|-----------|--------------------------------|
| 1 | **Registro cavi / database di gestione del cablaggio** con tipo, endpoint, percorso e classificazione per tutto il cablaggio strutturato | Responsabile della struttura | *Mantenuto continuamente; rivisto annualmente* | Registro aggiornato con cronologia delle versioni che mostra gli aggiornamenti |
| 2 | **Disegni as-built del cablaggio** per tutte le strutture, aggiornati e con controllo delle versioni | Responsabile della struttura | *Aggiornato entro 5 giorni lavorativi dalle modifiche; rivisto annualmente* | Versioni dei disegni correlate ai registri delle modifiche |
| 3 | **Report delle ispezioni trimestrali del cablaggio** con risultati, riconciliazione con i disegni e firma | Responsabile della struttura | *Trimestrale; conservato 3 anni* | Report di ispezione firmato con risultati e azioni correttive |
| 4 | **Registrazioni dei test del cablaggio** (continuità, prestazioni) per le nuove installazioni e la verifica annuale | Responsabile della struttura | *Annuale e per installazione; conservato 3 anni* | Report dei test con risultati pass/fail per standard di cablaggio |
| 5 | **Programma di manutenzione** con tutte le attrezzature in ambito e calendari allineati alle raccomandazioni del produttore | Responsabile IT Operations | *Rivisto trimestralmente; conservato 3 anni* | Documento del programma con firma della revisione trimestrale |
| 6 | **Riconciliazione trimestrale** dell'inventario delle risorse rispetto alla copertura del programma di manutenzione | Responsabile IT Operations | *Trimestrale; conservato 3 anni* | Report di riconciliazione con percentuale di copertura e rimedio delle lacune |
| 7 | **Registrazioni della manutenzione preventiva** con documentazione della manutenzione completata, risultati e prossima data programmata | IT Operations | *Per evento di manutenzione; conservato minimo 3 anni* | Singole registrazioni di manutenzione con timestamp di completamento |
| 8 | **Registrazioni della manutenzione correttiva** con guasti, causa principale, azioni di riparazione e verifica post-riparazione | IT Operations | *Per evento; conservato minimo 3 anni* | Registrazioni di manutenzione collegate agli incidenti con analisi della causa principale |
| 9 | **Registrazioni di autorizzazione del personale di manutenzione** (interno e di terze parti) | Responsabile IT Operations | *Rivisto annualmente; conservato 3 anni* | Registro di autorizzazione con firma della revisione annuale |
| 10 | **Registro dei fornitori di manutenzione di terze parti** con dettagli dei contratti e revisione annuale | Responsabile IT Operations | *Rivisto annualmente; conservato attivo + 2 anni* | Registro dei fornitori con riepiloghi dei contratti e date di revisione |
| 11 | **Log delle sessioni di manutenzione da remoto** con identificazione individuale, orari e azioni | IT Operations | *Per sessione; conservato 3 anni* | Log di sessione con registrazioni di autorizzazione |
| 12 | **Registrazioni di rimozione e restituzione delle attrezzature** con catena di custodia, prove di protezione dei dati e ispezione al rientro | IT Operations | *Per evento; conservato 3 anni* | Moduli della catena di custodia con firma dell'ispezione |
| 13 | **Report di analisi dei trend di manutenzione** che identificano problemi ricorrenti e raccomandazioni sul ciclo di vita delle attrezzature | Responsabile IT Operations | *Trimestrale; conservato 3 anni* | Report di trend con raccomandazioni attuabili e risposta della direzione |
| 14 | **Registro delle eccezioni** per le deviazioni approvate dai calendari di manutenzione o dagli standard di cablaggio | RSSI | *Per evento; rivisto trimestralmente; conservato attivo + 2 anni* | Registrazioni delle eccezioni con valutazione del rischio e controlli compensativi |
| 15 | **Valutazioni dell'impatto sui servizi** per le attività di manutenzione | IT Operations | *Per evento di manutenzione con impatto sui servizi* | Richiesta di modifica con valutazione dell'impatto, approvazione, notifica al cliente (se applicabile) |
| 16 | **Report di utilizzo della finestra di manutenzione** | Responsabile IT Operations | *Trimestrale* | Riepilogo con: downtime pianificato vs. budget di disponibilità, conformità SLA, notifiche ai clienti inviate |
| 17 | **Metriche di disponibilità dell'infrastruttura** | Responsabile IT Operations | *Mensile; aggregato trimestralmente* | Dashboard con % uptime, downtime non pianificato, MTBF, MTTR per categoria di attrezzature |
| 18 | **Registrazioni degli incidenti infrastrutturali (P1/P2)** | IT Operations | *Per incidente* | Ticket di incidente con: cronologia, analisi della causa principale, impatto sui clienti, risoluzione, revisione post-incidente |
| 19 | **Report di monitoraggio della salute delle attrezzature** | IT Operations | *Mensile* | Trend di salute delle batterie UPS, monitoraggio della temperatura, trend dei tassi di errore, avvisi di guasto predittivo |
| 20 | **Schede di valutazione delle prestazioni del fornitore** | Responsabile IT Operations | *Trimestrale per fornitore* | Dati di conformità SLA, metriche di qualità, tracciamento degli incidenti di sicurezza, soddisfazione del cliente |
| 21 | **Revisioni annuali dei fornitori** | Responsabile IT Operations | *Annuale per fornitore* | Documento di revisione con valutazione delle prestazioni, raccomandazione di rinnovo/sostituzione, firma di approvazione |
| 22 | **Risultati dei test dell'infrastruttura DR** | Responsabile IT Operations | *Annuale (o per test DR)* | Report del test DR con test di failover dell'infrastruttura, risultati, azioni correttive |
| 23 | **Registrazioni della gestione delle modifiche al cablaggio** | Responsabile della struttura | *Per modifica al cablaggio* | Richiesta di modifica, approvazione, risultati dei test, aggiornamenti dei disegni as-built, firma di completamento |

### Aspettative dei test SOC 2 Tipo II

I revisori tipicamente esamineranno a campione:
- **25 eventi di manutenzione preventiva** nel periodo di audit (verificare programmazione, completamento nei tempi, documentazione)
- **Tutti gli incidenti infrastrutturali P1/P2** (verificare classificazione, escalation, notifica al cliente, revisione post-incidente)
- **Tutte le revisioni delle prestazioni dei fornitori** (verificare completamento, metriche tracciate, decisioni documentate)
- **Tutte le modifiche all'infrastruttura di cablaggio** (verificare approvazione della modifica, test, aggiornamenti della documentazione)
- **Riconciliazioni trimestrali** (inventario delle risorse vs. copertura del programma di manutenzione)
- **Metriche di disponibilità mensili** (verificare accuratezza, analisi dei trend, escalation dei problemi)

**La completezza è critica**: Prove mancanti per qualsiasi elemento nel campione = rilievo di audit.

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità alla presente politica tramite vari metodi, inclusi tra gli altri: audit dell'infrastruttura di cablaggio, revisioni del programma di manutenzione, audit dei registri di manutenzione, ispezioni fisiche, valutazioni della conformità dei fornitori, audit interni ed esterni e feedback al proprietario della politica.

Le seguenti metriche devono essere tracciate e riportate al RSSI trimestralmente:

| Metrica | Obiettivo | Soglia rossa |
|---------|-----------|-------------|
| Manutenzione preventiva completata nei tempi | 100% | < 85% |
| Guasti alle attrezzature attribuibili a manutenzione mancata o inadeguata | 0 | Qualsiasi occorrenza |
| Accuratezza della documentazione del cablaggio (risultati delle ispezioni vs. disegni) | > 95% | < 85% |
| Modifiche non autorizzate al cablaggio rilevate | 0 | Qualsiasi occorrenza |
| Incidenti di sicurezza correlati alla manutenzione | 0 | Qualsiasi occorrenza |
| Riconciliazione inventario delle risorse con programma di manutenzione | Copertura 100% | < 90% di copertura |
| Personale di manutenzione di terze parti correttamente autorizzato e supervisionato | 100% | < 95% |

## Eccezioni

Qualsiasi eccezione alla presente politica deve essere approvata e registrata preventivamente dal RSSI, con valutazione documentata del rischio, controlli compensativi e una data di revisione definita (massimo 6 mesi, rinnovabile). Gli scenari di eccezione validi includono:

- Manutenzione rinviata per sistemi critici dove la finestra di manutenzione non può essere programmata senza un impatto aziendale inaccettabile (con monitoraggio compensativo).
- Intervalli di manutenzione estesi per attrezzature a bassa criticità (con giustificazione documentata e consultazione del produttore ove applicabile).
- Utilizzo di cavo in rame in ubicazioni dove è specificata la fibra ottica ma l'installazione non è fattibile (con schermatura e controlli di protezione fisica compensativi).
- Manutenzione di terze parti senza supervisione completa (con registrazione potenziata e ispezione post-manutenzione).

Le eccezioni devono essere registrate nel Registro delle eccezioni e segnalate al Team di revisione della direzione.

**Non consentito**:

- Saltare la manutenzione critica per la sicurezza (UPS, sistemi antincendio, sistemi di sicurezza) senza controlli compensativi.
- Modifiche al cablaggio non documentate.
- Manutenzione di terze parti non supervisionata e non registrata su attrezzature contenenti dati sensibili.
- Eccezioni permanenti alla copertura del programma di manutenzione.

## Non conformità

Un dipendente che risulti aver violato la presente politica può essere soggetto a provvedimenti disciplinari, fino al licenziamento. Le modifiche al cablaggio effettuate senza autorizzazione o documentazione devono essere trattate come incidente di sicurezza e investigate di conseguenza. La manutenzione delle attrezzature aggirata senza approvazione deve essere segnalata al RSSI per la valutazione del rischio.

## Miglioramento continuo

La presente politica è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni devono tener conto di: modifiche alle operazioni delle strutture, evoluzione tecnologica dell'infrastruttura, standard di cablaggio, raccomandazioni del produttore per la manutenzione, stato del ciclo di vita delle attrezzature, requisiti normativi, risultati degli audit, trend degli incidenti e lezioni apprese dai guasti alle attrezzature. Le non conformità relative alla presente politica devono essere registrate e gestite attraverso il processo di azione correttiva del SGSI (Clausola 10.2) con analisi della causa principale e rimedio tracciato.

---

# Aree della norma ISO 27001 trattate

Politica di sicurezza dei cablaggi e manutenzione delle attrezzature — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.9 Inventario delle informazioni e delle altre risorse associate |
| Clausola 6.1 Azioni per affrontare rischi e opportunità | 5.30 Preparazione ICT per la continuità operativa |
| Clausola 7.3 Consapevolezza | 7.4 Monitoraggio della sicurezza fisica |
| Clausola 8.1 Pianificazione e controllo operativo | 7.5 Protezione contro minacce fisiche e ambientali |
| Clausola 9.1 Monitoraggio, misurazione, analisi e valutazione | 7.8 Ubicazione e protezione delle attrezzature |
| Clausola 10.2 Non conformità e azioni correttive | **7.12 Sicurezza dei cablaggi** |
| | **7.13 Manutenzione delle attrezzature** |
| | 7.14 Smaltimento sicuro o riutilizzo delle attrezzature |
| | 8.32 Gestione delle modifiche |

**Quadro normativo e legale**:

| Quadro | Rilevanza |
|--------|-----------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la sicurezza fisica dell'infrastruttura di elaborazione dei dati |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Art. 1–3 — Requisiti minimi per la sicurezza dei dati incluse le misure fisiche |
| NIN svizzera (Niederspannungs-Installationsnorm) | Standard per installazioni elettriche a bassa tensione applicabili al cablaggio di alimentazione negli edifici |
| Ordinanza federale svizzera sulle installazioni a bassa tensione (RS 734.27) | Prerequisiti e requisiti di ispezione per le installazioni elettriche |
| GDPR UE (ove applicabile) | Art. 32 — Sicurezza del trattamento incluse misure per l'infrastruttura fisica |
| ISO/IEC 27001:2022 | Allegato A Controlli 7.12 (Sicurezza dei cablaggi), 7.13 (Manutenzione delle attrezzature) |
| ISO/IEC 27002:2022 | Sezioni 7.12, 7.13 — Guida all'implementazione per la sicurezza dei cablaggi e la manutenzione delle attrezzature |
| IEC 11801 / EN 50173 | Standard internazionali ed europei per il cablaggio strutturato per cablaggio generico nelle strutture dei clienti |
| TIA-568 / TIA-942 | Standard nordamericani per il cablaggio strutturato e i data center |
| NIST SP 800-53 Rev 5 | PE-4 (Controllo degli accessi per la trasmissione), PE-9 (Attrezzature elettriche e cablaggi), MA-2 (Manutenzione controllata), MA-5 (Personale di manutenzione) |
| CIS Controls v8 | Controllo 1 (Inventario e controllo delle risorse aziendali), Controllo 12 (Gestione dell'infrastruttura di rete) |
| **Condizionale**: Circolare FINMA 2023/1 | Istituto finanziario svizzero regolamentato — requisiti potenziati di resilienza dell'infrastruttura |
| **Condizionale**: DORA (UE) 2022/2554 | Entità di servizi finanziari UE — resilienza operativa ICT per l'infrastruttura |
| **Condizionale**: NIS2 (UE) 2022/2555 | Entità essenziale/importante nell'UE — requisiti di protezione dell'infrastruttura |

---

<!-- QA_VERIFIED: 2026-04-03 -->
