<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.4-5-11-IT:operational:OP-POL:a.7.4-5-11 -->
**ISMS-OP-POL-A.7.4-5-11 — Sicurezza delle infrastrutture fisiche**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza delle infrastrutture fisiche |
| **Tipo di documento** | Politica operativa |
| **ID documento** | ISMS-OP-POL-A.7.4-5-11 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
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

- ISO/IEC 27001:2022 Controlli A.7.4, A.7.5, A.7.11 — Monitoraggio della sicurezza fisica, protezione dalle minacce fisiche e ambientali, servizi di supporto
- ISO/IEC 27002:2022 Sezioni 7.4, 7.5, 7.11 — Linee guida di attuazione

**Controlli correlati dell'Allegato A**:

| Controllo | Relazione con la sicurezza delle infrastrutture fisiche |
|-----------|--------------------------------------------------------|
| A.7.1 Perimetri di sicurezza fisica | I confini del perimetro definiscono l'ambito del monitoraggio e le zone di protezione ambientale |
| A.7.2 Ingresso fisico | I controlli di ingresso generano eventi di accesso per il monitoraggio e la correlazione |
| A.7.3 Messa in sicurezza di uffici, stanze e strutture | Le aree sicure richiedono protezione ambientale e resilienza dei servizi di supporto |
| A.7.8 Ubicazione e protezione delle attrezzature | L'ubicazione delle attrezzature tiene conto delle condizioni ambientali e della disponibilità dei servizi di supporto |
| A.7.12 Sicurezza del cablaggio | L'integrità del cablaggio di alimentazione e telecomunicazioni supporta la resilienza dei servizi di supporto |
| A.7.13 Manutenzione delle attrezzature | Programmi di manutenzione per i sistemi ambientali e di supporto |
| A.5.24–28 Ciclo di vita della gestione degli incidenti | Gli incidenti di sicurezza fisica e ambientale vengono escalati alla gestione degli incidenti |
| A.5.30 Preparazione dell'ICT per la continuità aziendale | La resilienza dei servizi di supporto supporta gli obiettivi di continuità aziendale |
| A.8.16 Attività di monitoraggio | Gli eventi di sicurezza fisica si integrano con il SIEM per un rilevamento correlato |

**Politiche interne correlate**:

- Politica sul controllo degli accessi fisici
- Politica di gestione degli incidenti
- Politica sulla continuità aziendale e il ripristino di emergenza
- Politica di registrazione
- Politica sulle attività di monitoraggio (A.8.16)
- Politica sui servizi cloud e la sicurezza dei fornitori
- Politica di gestione degli asset

---

# Politica sulla sicurezza delle infrastrutture fisiche

## Scopo

Lo scopo di questa politica è proteggere le strutture di elaborazione delle informazioni e le infrastrutture associate attraverso il monitoraggio della sicurezza fisica, la protezione dalle minacce ambientali e la resilienza dei servizi di supporto. Stabilisce i requisiti per la sorveglianza continua, la protezione antincendio e idrica, il controllo del clima e la continuità dell'alimentazione elettrica e delle telecomunicazioni.

Questa politica tratta tre controlli correlati di ISO 27001:2022 come quadro unificato perché operano sulla stessa infrastruttura fisica, creano interdipendenze e condividono processi di valutazione comuni: il monitoraggio rileva le minacce (A.7.4), i controlli ambientali prevengono i danni (A.7.5) e i sistemi di supporto mantengono le operazioni (A.7.11). Ciascun controllo mantiene requisiti distinti ai fini della Dichiarazione di applicabilità.

Questa politica supporta la nLPD svizzera (revDSG) Art. 8 implementando misure tecniche e organizzative proporzionate al rischio per proteggere la disponibilità, l'integrità e la riservatezza dei dati personali attraverso controlli di sicurezza delle infrastrutture fisiche. Nei casi in cui l'organizzazione tratti dati di persone nell'UE/SEE, si applicano altresì i requisiti dell'Art. 32 del RGPD per la sicurezza del trattamento, incluse le misure fisiche.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutte le sedi di proprietà, in locazione o in colocation dell'organizzazione, inclusi:

- Data center in sede e siti di ripristino di emergenza
- Sale server e armadi per le telecomunicazioni
- Uffici aziendali (sede centrale, regionali, filiali)
- Strutture di colocation (con modello di responsabilità condivisa)
- Strutture remote e temporanee dove si trovano attrezzature di proprietà dell'organizzazione

**Escluso dall'ambito**:

- Sicurezza fisica dei dispositivi portatili (coperta da A.7.9, A.8.1)
- Sicurezza del trasporto delle attrezzature (coperta da A.7.13)
- Archiviazione off-site dei supporti di backup (coperta da A.8.13)
- Sicurezza del personale e verifiche dei precedenti (coperta da A.6.1–6.4)
- Sicurezza delle strutture di terze parti e fornitori (coperta da A.5.19–23, ad eccezione della colocation come indicato di seguito)

### Organizzazioni esclusivamente cloud

Le organizzazioni che operano al 100% in ambienti cloud senza strutture di elaborazione delle informazioni in sede possono contrassegnare i Controlli A.7.4, A.7.5 e A.7.11 come "Non applicabile" nella Dichiarazione di applicabilità.

La determinazione "Non applicabile" DEVE essere documentata con:

- Riferimento all'inventario degli asset che conferma l'assenza di strutture di elaborazione delle informazioni in sede.
- Verifica della sicurezza fisica del provider cloud tramite rapporto SOC 2 Type II o revisione della certificazione ISO 27001.
- Conferma della revisione annuale che lo stato esclusivamente cloud rimanga accurato.

La sicurezza fisica del provider cloud DEVE essere valutata attraverso il processo di gestione dei fornitori (A.5.19–23).

### Strutture di colocation

Quando si utilizza spazio in data center di colocation, le responsabilità dell'infrastruttura fisica sono condivise tra il provider di colocation e l'organizzazione. L'organizzazione DEVE:

- Mantenere una matrice formale delle responsabilità nel contratto di colocation che documenti quale parte è responsabile di ciascun controllo dell'infrastruttura fisica (monitoraggio, ambiente, servizi di supporto).
- Verificare i controlli del provider annualmente tramite rapporti di audit SOC 2 Type II o certificazione ISO 27001.
- Mantenere la responsabilità per i controlli di monitoraggio e ambientali all'interno dello spazio allocato dell'organizzazione (ad es., monitoraggio ambientale a livello di rack, controlli di accesso alla gabbia).

## Principio

La sicurezza fisica e ambientale si basa sul principio di protezione delle strutture di elaborazione delle informazioni dall'accesso non autorizzato, dalle minacce ambientali e dai guasti ai servizi di supporto — proporzionatamente alla criticità degli asset che contengono. I controlli DEVONO essere selezionati sulla base di una valutazione documentata del rischio e della classificazione per livello di criticità della struttura definita in questa politica.

---

## Monitoraggio della sicurezza fisica (A.7.4)

> *I locali dovrebbero essere monitorati continuamente per rilevare accessi fisici non autorizzati.*

Il monitoraggio della sicurezza fisica DEVE rilevare e scoraggiare l'accesso fisico non autorizzato alle strutture e alle aree riservate. La progettazione e l'implementazione del sistema di monitoraggio DEVONO essere proporzionate alla criticità della struttura.

### Sistemi di sicurezza fisica

I seguenti sistemi di sicurezza fisica DEVONO essere implementati e mantenuti. Le organizzazioni DEVONO specificare i sistemi effettivamente implementati (o documentare lo stato di selezione) per ciascuna categoria:

| Categoria di sistema | Scopo | Soluzioni di esempio | Stato |
|----------------------|-------|----------------------|-------|
| **Sistema di controllo degli accessi** | Ingresso/uscita con badge e registrazione degli eventi | Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY, Salto | [Specificare o "Selezione in corso"] |
| **CCTV / Videosorveglianza** | Monitoraggio visivo e registrazione | Verkada, Axis, Milestone, Genetec | [Specificare o "Selezione in corso"] |
| **Rilevamento delle intrusioni** | Rilevamento di violazioni del perimetro e degli interni | Honeywell, Bosch, DSC, Texecom | [Specificare o "Selezione in corso"] |
| **Servizio di monitoraggio allarmi** | Risposta agli allarmi e intervento 24/7 | Securitas, Protectas, centrale di monitoraggio locale | [Specificare o "Selezione in corso"] |
| **Monitoraggio ambientale** | Sensori di temperatura, umidità e rilevamento acqua | Paessler PRTG, Raritan, APC NetBotz, Sensaphone | [Specificare o "Selezione in corso"] |
| **Sistema di gestione dell'edificio (BMS)** | Controllo centralizzato dei servizi dell'edificio (HVAC, illuminazione, alimentazione) | Siemens Desigo, Honeywell Niagara, Schneider EcoStruxure | [Specificare o "Selezione in corso"] |
| **Rilevamento e soppressione incendi** | Rilevamento fumo/calore e soppressione a agente pulito | Siemens, Minimax, Kidde, Wagner | [Specificare o "Selezione in corso"] |
| **Sistemi UPS** | Alimentazione ininterrotta per attrezzature critiche | Eaton, APC/Schneider, Vertiv/Liebert, Riello | [Specificare o "Selezione in corso"] |
| **Generatore di emergenza** | Continuità dell'alimentazione prolungata | Caterpillar, Cummins, MTU, SDMO | [Specificare o "Selezione in corso"] |

**Requisiti di integrazione**: Ove tecnicamente fattibile, i sistemi di sicurezza fisica dovrebbero inviare gli eventi al [SIEM] per la correlazione con gli eventi di sicurezza logica. Come minimo, gli eventi del sistema di controllo degli accessi e gli allarmi del sistema di rilevamento delle intrusioni DEVONO essere inoltrati.

### Controllo degli accessi elettronico

- Il controllo degli accessi elettronico DEVE essere implementato in tutti i punti di ingresso e uscita della struttura con autenticazione, registrazione degli eventi e integrazione con la gestione delle identità.
- Gli eventi di accesso (concesso, negato, porta forzata, porta tenuta aperta) DEVONO essere registrati con timestamp, identità dell'individuo e identificatore della porta.
- I log degli accessi DEVONO essere conservati per un minimo di 12 mesi.
- I diritti di accesso DEVONO essere riesaminati semestralmente e revocati quando non più necessari (ad es., cambio di ruolo, cessazione).
- La revoca degli accessi lo stesso giorno DEVE essere applicata alla cessazione del rapporto di lavoro.

#### Processo di revisione dei diritti di accesso

I diritti di accesso fisico DEVONO essere riesaminati semestralmente utilizzando il seguente flusso di lavoro strutturato:

| Passaggio | Azione | Responsabile | Tempistica |
|-----------|--------|--------------|------------|
| 1 | Generare il rapporto sui diritti di accesso dal [Sistema di controllo degli accessi] con tutto il personale per zona e reparto | Responsabile delle strutture | 1° giorno lavorativo del mese di revisione |
| 2 | Distribuire gli elenchi di accesso specifici per zona ai responsabili autorizzanti per l'attestazione | Responsabile delle strutture | Entro 2 giorni lavorativi |
| 3 | I responsabili riesaminano l'accesso di ogni persona: confermano quello necessario, segnalano quello da rimuovere o pongono quesiti | Responsabili diretti | Entro 10 giorni lavorativi |
| 4 | Raccogliere le risposte dei responsabili; generare l'elenco delle revoche per gli accessi non più necessari | Responsabile delle strutture | Entro 2 giorni lavorativi dalla scadenza dell'attestazione |
| 5 | Eseguire le revoche degli accessi nel [Sistema di controllo degli accessi] | Responsabile delle strutture | Entro 5 giorni lavorativi |
| 6 | Confermare le revoche completate; archiviare i registri di attestazione | Responsabile delle strutture | Entro 2 giorni lavorativi |

**Escalation per mancata risposta**:
- Mancata risposta del responsabile a 10 giorni lavorativi → Promemoria inviato con proroga di 5 giorni
- Mancata risposta del responsabile a 15 giorni lavorativi → Escalation al responsabile di reparto
- Mancata risposta del responsabile a 20 giorni lavorativi → Accesso per il personale non attestato nelle zone riservate sospeso in attesa di attestazione

**Metriche di completamento**:
- Obiettivo: 100% dei diritti di accesso riesaminati per ciclo
- Obiettivo: tutte le revoche eseguite entro 5 giorni lavorativi dall'attestazione
- Non conformità riferita al RSSI nel rapporto di conformità trimestrale

### Videosorveglianza (CCTV)

- La copertura CCTV DEVE essere fornita agli ingressi della struttura, ai punti di accesso alle aree riservate e nelle posizioni delle infrastrutture critiche (sale server, locali tecnici).
- I sistemi CCTV DEVONO registrare continuamente durante l'orario operativo come minimo; la registrazione 24/7 è richiesta per le strutture di Livello 1.
- Conservazione delle registrazioni: minimo 30 giorni per le aree generali, 90 giorni per le aree riservate. Una conservazione più lunga può essere richiesta per le indagini su incidenti.
- I sistemi CCTV DEVONO rispettare i requisiti applicabili per la protezione dei dati (nLPD svizzera, normative cantonali). La segnaletica che indica la videosorveglianza DEVE essere esposta nelle aree monitorate.
- Lo stato delle telecamere (connettività, qualità delle immagini, capacità di archiviazione) DEVE essere verificato settimanalmente.

### Rilevamento delle intrusioni

- I sistemi di rilevamento delle intrusioni (SRI) DEVONO essere installati nelle strutture di Livello 1, coprendo le porte perimetrali, le finestre e i punti di accesso alle aree riservate.
- Il rilevamento delle intrusioni è raccomandato per le strutture di Livello 2 sulla base della valutazione del rischio.
- Gli allarmi DEVONO essere collegati a un punto di risposta monitorato (operazioni di sicurezza, servizio di monitoraggio allarmi o [Provider di monitoraggio allarmi]).
- Il SRI DEVE essere testato trimestralmente per confermare il corretto funzionamento.

### Gestione dei visitatori

- Tutti i visitatori DEVONO registrarsi all'arrivo, ricevere un'identificazione temporanea ed essere accompagnati nelle aree riservate.
- I registri dei visitatori (nome, organizzazione, referente interno, orario di arrivo/partenza) DEVONO essere conservati per un minimo di 12 mesi.
- I badge dei visitatori DEVONO identificare chiaramente lo stato di visitatore, negare l'accesso alle aree riservate e scadere alla fine della giornata lavorativa in cui sono stati emessi.

### Monitoraggio degli eventi di sicurezza e integrazione

- Gli eventi di sicurezza fisica (accesso negato, ingresso forzato, allarme intrusione, porta tenuta aperta) dovrebbero essere inoltrati al [SIEM] per la correlazione con gli eventi di sicurezza logica ove tecnicamente fattibile.
- I tentativi di accesso falliti ripetuti (3 o più entro 30 minuti) DEVONO attivare un avviso e un'indagine.

### Protezione del sistema di monitoraggio

- La progettazione e la configurazione dei sistemi di monitoraggio DEVONO essere mantenute riservate.
- I sistemi di monitoraggio DEVONO essere protetti da manomissioni, disabilitazione non autorizzata e interferenze remote.
- Le attrezzature di monitoraggio DEVONO essere alimentate da UPS per garantire il funzionamento continuato durante le interruzioni di corrente.

---

## Protezione ambientale (A.7.5)

> *La protezione contro le minacce fisiche e ambientali dovrebbe essere progettata e implementata.*

I controlli di protezione ambientale DEVONO prevenire o attenuare i danni da incendio, acqua, condizioni climatiche estreme e altre minacce fisiche. I livelli di protezione DEVONO essere proporzionati alla criticità della struttura.

### Valutazione delle minacce ambientali

- Una valutazione del rischio delle minacce ambientali DEVE essere condotta per ciascuna struttura, tenendo conto della posizione geografica, delle caratteristiche dell'edificio, degli eventi storici e dei pericoli circostanti.
- La valutazione DEVE essere riesaminata annualmente e aggiornata in seguito a incidenti o modifiche significative della struttura.
- Le minacce da considerare includono: incendio, alluvione, infiltrazione d'acqua, temperature estreme, umidità, fulmini, attività sismica, cedimento strutturale, disordini civili e pericoli industriali.

### Rilevamento e soppressione incendi

Il rilevamento incendi DEVE essere implementato in tutte le strutture contenenti attrezzature di elaborazione delle informazioni.

| Requisito | Livello 1 — Strutture critiche | Livello 2 — Strutture standard |
|-----------|-------------------------------|-------------------------------|
| **Rilevamento** | Rilevamento fumo (VESDA/aspirante o convenzionale) in tutte le zone; rilevamento calore nelle aree tecniche | Rilevamento fumo convenzionale nelle aree server/attrezzature |
| **Soppressione** | Sistema di soppressione a gas inerte (ad es., IG-541/Inergen, IG-55/Argonite, o equivalente) nelle sale server e sui pavimenti del data center | Soppressione richiesta se il valore delle attrezzature supera CHF 500.000 o se la criticità dei dati lo giustifica; estintori portatili altrove |
| **Integrazione allarmi** | Collegato al sistema di gestione dell'edificio (BMS), ai vigili del fuoco e al monitoraggio della sicurezza | Collegato al pannello antincendio dell'edificio |
| **Ispezione** | Ispezione semestrale e test annuale completo ai sensi delle normative antincendio cantonali | Ispezione annuale ai sensi delle normative antincendio cantonali |

**Note sugli agenti di soppressione**: I sistemi a agente pulito conformi a NFPA 2001 e ISO 14520 sono richiesti per gli spazi occupati contenenti attrezzature elettroniche. I sistemi sprinkler ad acqua NON DEVONO essere utilizzati nelle sale server o nei data center. Le organizzazioni dovrebbero considerare la disponibilità a lungo termine e il profilo ambientale degli agenti selezionati nella specifica dei sistemi di soppressione.

#### Linee guida per la selezione degli agenti di soppressione incendi

Le organizzazioni che selezionano sistemi di soppressione a agente pulito per sale server e data center dovrebbero valutare le opzioni in base all'efficacia, alla sicurezza, al profilo ambientale e alla disponibilità normativa a lungo termine:

| Agente | Tipo | Riduzione ozono | Potenziale di riscaldamento globale | Sicurezza (spazi occupati) | Prospettive di disponibilità | Raccomandazione |
|--------|------|-----------------|-------------------------------------|----------------------------|------------------------------|-----------------|
| **IG-541 (Inergen)** | Miscela di gas inerte (N₂, Ar, CO₂) | Zero | Zero | Sicuro — respirabile alla concentrazione di progetto | Stabilità a lungo termine | **Raccomandato** per nuove installazioni |
| **IG-55 (Argonite)** | Miscela di gas inerte (N₂, Ar) | Zero | Zero | Sicuro — respirabile alla concentrazione di progetto | Stabilità a lungo termine | Alternativa raccomandata |
| **IG-100 (Azoto)** | Azoto puro | Zero | Zero | Sicuro — respirabile alla concentrazione di progetto | Stabilità a lungo termine | Adatto per grandi volumi |
| **FK-5-1-12 (Novec 1230)** | Fluorochetone | Zero | 1 | Sicuro — bassa tossicità | Stabile (produzione 3M in corso) | Accettabile per installazioni con spazio limitato |
| **HFC-227ea (FM-200)** | Idrofluorocarburo | Zero | 3.220 | Sicuro — bassa tossicità alla concentrazione di progetto | **Fase di eliminazione** ai sensi del Regolamento UE sugli F-gas e dell'Emendamento di Kigali | **Non raccomandato** per nuove installazioni |

**Criteri di selezione per nuove installazioni**:
1. Sistemi a gas inerte (IG-541, IG-55) preferiti per il loro impatto ambientale zero e la certezza normativa a lungo termine
2. FK-5-1-12 (Novec 1230) accettabile dove lo spazio per lo stoccaggio delle bombole è limitato (volume inferiore rispetto ai gas inerti)
3. HFC-227ea (FM-200) non raccomandato per nuove installazioni a causa della traiettoria di eliminazione normativa

**Sistemi FM-200 esistenti**: Non è richiesta una sostituzione immediata. Mantenere secondo il programma del produttore. Pianificare il budget per la sostituzione con un sistema a gas inerte al prossimo intervento di ristrutturazione importante o entro 10 anni (il primo che si verifica). Documentare la tempistica di sostituzione nel piano di investimento delle strutture.

- Le porte antincendio sui perimetri di sicurezza DEVONO essere allarmate, monitorate e testate in conformità con i codici antincendio applicabili.
- L'illuminazione di emergenza e le vie di evacuazione DEVONO essere mantenute e testate semestralmente.

### Rilevamento e protezione idrica

- I sensori di rilevamento dell'acqua DEVONO essere installati nelle strutture di Livello 1 — sotto i pavimenti sopraelevati, sopra i soffitti pensili, vicino alle infrastrutture di raffreddamento e in tutte le zone dove è possibile l'infiltrazione d'acqua.
- Le strutture di Livello 2 DEVONO avere il rilevamento dell'acqua nelle aree ad alto rischio (vicino agli impianti idraulici, ai sistemi HVAC, ai locali al piano terra).
- Gli allarmi idrici DEVONO attivare un avviso immediato alla gestione delle strutture.
- Le strutture DEVONO implementare drenaggi, impermeabilizzazioni e barriere fisiche appropriate al rischio alluvionale identificato.

### Controllo del clima

Le attrezzature di elaborazione delle informazioni DEVONO essere mantenute entro intervalli controllati di temperatura e umidità per prevenire danni e garantire un funzionamento affidabile.

| Parametro | Intervallo raccomandato (Classe ASHRAE A1–A4) | Soglia di avviso | Soglia critica |
|-----------|----------------------------------------------|------------------|----------------|
| **Temperatura** | 18–27 °C (64–81 °F) | Fuori dall'intervallo 18–27 °C | Inferiore a 15 °C o superiore a 32 °C |
| **Umidità** | 20–80% umidità relativa (UR) | Fuori dall'intervallo 20–80% UR | Inferiore al 10% UR o superiore al 90% UR |
| **Tasso di variazione della temperatura** | < 5 °C per ora | Supera 5 °C/ora | Supera 10 °C/ora |

**Strutture di Livello 1**: La temperatura DEVE essere mantenuta tra 18–27 °C con tolleranza di +/- 2 °C. È richiesto il monitoraggio ambientale continuo con avvisi in tempo reale.

**Strutture di Livello 2**: La temperatura DEVE essere mantenuta tra 18–27 °C con tolleranza di +/- 5 °C. È richiesto il monitoraggio ambientale con avvisi durante le ore presidiate.

I dati del monitoraggio ambientale (temperatura, umidità) DEVONO essere registrati e conservati per un minimo di 12 mesi.

#### Configurazione degli avvisi del monitoraggio ambientale

I sistemi di monitoraggio ambientale DEVONO essere configurati con le seguenti soglie di avviso, requisiti di risposta e percorsi di escalation:

| Parametro | Avviso di attenzione | Avviso critico | Tempo di risposta (Livello 1) | Tempo di risposta (Livello 2) |
|-----------|---------------------|----------------|-------------------------------|-------------------------------|
| **Temperatura** | Fuori dall'intervallo 18–27°C | Inferiore a 15°C o superiore a 32°C | 15 minuti | Giorno lavorativo successivo |
| **Umidità** | Fuori dall'intervallo 20–80% UR | Inferiore al 10% o superiore al 90% UR | 15 minuti | Giorno lavorativo successivo |
| **Tasso di variazione della temperatura** | Supera 5°C/ora | Supera 10°C/ora | 15 minuti | 1 ora |
| **Rilevamento acqua** | Qualsiasi attivazione di sensore | Più sensori o acqua in aumento | Immediato | 30 minuti |
| **Alimentazione (UPS a batteria)** | L'UPS passa alla batteria | Batteria sotto il 50% di capacità | Immediato | 15 minuti |
| **Sistema di raffreddamento** | Guasto di una singola unità (unità ridondante attiva) | Guasto di tutte le unità di raffreddamento | 30 minuti | 1 ora |

**Instradamento degli avvisi**:
- Avvisi di attenzione → Responsabile delle strutture + Operazioni IT (email + dashboard)
- Avvisi critici → Responsabile delle strutture + Operazioni IT + RSSI (email + SMS + dashboard)
- Avvisi critici fuori orario → Reperibile delle strutture + Operazioni IT di reperibilità

**Escalation**:
- Avviso di attenzione non confermato dopo 30 minuti → Escalation a critico
- Avviso critico non confermato dopo 15 minuti → Escalation al RSSI + Direzione generale

**Test degli avvisi**: I percorsi degli avvisi del monitoraggio ambientale DEVONO essere testati trimestralmente (simulare il superamento della soglia; verificare la consegna dell'avviso a tutti i destinatari configurati entro le tempistiche target).

### Protezione strutturale e fisica

- L'esterno dell'edificio (tetto, pareti, pavimentazione) DEVE essere di costruzione solida appropriata alle minacce identificate.
- La protezione dai fulmini DEVE essere applicata agli edifici che ospitano strutture di elaborazione delle informazioni. La protezione contro i sovraccarichi DEVE essere installata sulle linee di alimentazione e telecomunicazione in entrata.
- L'ubicazione delle attrezzature DEVE ridurre al minimo il rischio derivante dalle minacce ambientali identificate (ad es., evitare le posizioni in scantinato nelle aree soggette a alluvioni, evitare le posizioni adiacenti a processi pericolosi).
- Linee guida per mangiare, bere e fumare in prossimità delle strutture di elaborazione delle informazioni DEVONO essere stabilite e comunicate.

### Risposta alle emergenze

Le procedure di risposta alle emergenze DEVONO essere documentate per gli incidenti ambientali e testate regolarmente. Le informazioni di contatto di emergenza DEVONO essere affisse agli ingressi della struttura e all'interno delle sale server.

#### Procedura di emergenza antincendio

| Passaggio | Azione | Responsabile | Tempistica |
|-----------|--------|--------------|------------|
| 1 | L'allarme antincendio si attiva (rilevamento automatico o azionamento manuale) | Automatico / qualsiasi personale | Immediato |
| 2 | Evacuare la zona interessata; raccolta nel punto di raccolta designato | Tutto il personale | Entro 3 minuti |
| 3 | Vigili del fuoco allertati (automaticamente tramite BMS o chiamata manuale) | Responsabile delle strutture / Reception | Entro 2 minuti |
| 4 | Confermare l'evacuazione di tutto il personale (conteggio delle presenze al punto di raccolta) | Coordinatori di piano | Entro 5 minuti |
| 5 | Se il sistema di soppressione a gas si è attivato: NON rientrare finché la concentrazione di gas non è verificata sicura | Responsabile delle strutture | Dopo la soppressione |
| 6 | I vigili del fuoco liberano i locali; avvio della valutazione dei danni | Responsabile delle strutture + RSSI | Dopo il via libera |

**Azioni post-incendio**: Valutazione dei danni alle attrezzature entro 24 ore; verifica dell'integrità dei dati per i sistemi interessati; rapporto sull'incidente presentato entro 48 ore; notifica all'assicurazione se applicabile.

#### Procedura di emergenza per infiltrazione d'acqua / alluvione

| Passaggio | Azione | Responsabile | Tempistica |
|-----------|--------|--------------|------------|
| 1 | Scatta l'allarme idrico o l'acqua viene rilevata visivamente | Automatico / qualsiasi personale | Immediato |
| 2 | Identificare la fonte dell'acqua (impianto idraulico, ingresso esterno, condensa HVAC) | Responsabile delle strutture | Entro 15 minuti |
| 3 | Se la fonte è controllabile: isolare (chiudere la valvola, reindirizzare il flusso) | Responsabile delle strutture | Immediato |
| 4 | Spostare le attrezzature e i supporti al di sopra del livello dell'acqua o in un'area asciutta | Operazioni IT + Strutture | Immediato |
| 5 | Scollegare l'alimentazione alle attrezzature a rischio (se sicuro farlo) | Operazioni IT | Come richiesto |
| 6 | Azionare l'estrazione dell'acqua (pompe, aspiratori per acqua); coinvolgere un appaltatore di ripristino di emergenza se l'entità è estesa | Responsabile delle strutture | Entro 1 ora |

#### Procedura di emergenza per guasto del sistema di raffreddamento

| Passaggio | Azione | Responsabile | Tempistica |
|-----------|--------|--------------|------------|
| 1 | Avviso di temperatura ricevuto (soglia di attenzione superata) | Avviso automatico alle Operazioni IT | Immediato |
| 2 | Verificare lo stato del sistema di raffreddamento; tentare il riavvio o il failover all'unità ridondante | Responsabile delle strutture | Entro 15 minuti |
| 3 | Se la temperatura si avvicina alla soglia critica (32°C): Avviare lo spegnimento ordinato dei sistemi non essenziali per ridurre il carico termico | Operazioni IT | Entro 30 minuti |
| 4 | Installare raffreddamento temporaneo (unità AC portatili) se disponibili | Responsabile delle strutture | Entro 1 ora |
| 5 | Se la temperatura supera la soglia critica: Spegnimento ordinato di tutti i sistemi; notifica alle parti interessate | Operazioni IT + RSSI | Come richiesto |
| 6 | Appaltatore HVAC coinvolto per la riparazione di emergenza | Responsabile delle strutture | Entro 2 ore |

#### Procedura di emergenza per interruzione totale di corrente

| Passaggio | Azione | Responsabile | Tempistica |
|-----------|--------|--------------|------------|
| 1 | Rilevamento interruzione di rete; l'UPS si attiva automaticamente | Automatico | Immediato |
| 2 | Verificare l'avvio del generatore (Livello 1) o confermare che l'UPS sostenga il carico | Responsabile delle strutture | Entro 2 minuti |
| 3 | Se il generatore non si avvia: Avviare lo spegnimento ordinato dei sistemi non essenziali | Operazioni IT | Entro 10 minuti |
| 4 | Notificare il fornitore dell'utenza; richiedere il tempo stimato di ripristino | Responsabile delle strutture | Entro 15 minuti |
| 5 | Se la durata dell'UPS si avvicina al limite e il generatore non è disponibile: Completare lo spegnimento ordinato di tutti i sistemi | Operazioni IT | Prima dell'esaurimento dell'UPS |
| 6 | Post-ripristino: Verificare il corretto riavvio di tutti i sistemi; verificare l'integrità dei dati | Operazioni IT | Dopo il ripristino dell'alimentazione |

Le procedure di emergenza DEVONO essere testate almeno annualmente tramite esercitazioni pratiche o simulazioni su tavolo.

### Formazione sulla consapevolezza della sicurezza fisica

Tutto il personale con accesso alla struttura DEVE completare la formazione sulla consapevolezza della sicurezza fisica. La formazione viene erogata annualmente e il completamento per i nuovi assunti è richiesto entro 10 giorni lavorativi dalla concessione dell'accesso alla struttura.

#### Programma di formazione

| Modulo | Contenuto | Durata | Destinatari |
|--------|-----------|--------|-------------|
| **Modulo 1: Fondamenti di sicurezza delle strutture** | Livelli di criticità delle strutture; modello delle zone di sicurezza; utilizzo del badge e responsabilità; obblighi di gestione dei visitatori; prevenzione del tailgating | 10 minuti | Tutto il personale |
| **Modulo 2: Consapevolezza ambientale** | Sicurezza antincendio e vie di evacuazione; consapevolezza del rilevamento acqua; importanza del controllo del clima; segnalazione delle anomalie ambientali; numeri di contatto di emergenza | 10 minuti | Tutto il personale |
| **Modulo 3: Riconoscimento e segnalazione degli incidenti** | Riconoscimento degli eventi di sicurezza fisica (persone non autorizzate, porte aperte, anomalie ambientali); canali di segnalazione e aspettative; conservazione delle prove (non toccare/spostare) | 5 minuti | Tutto il personale |
| **Modulo 4: Responsabilità specifiche per ruolo** | Procedure di accompagnamento dei visitatori; protocolli di accesso alla sala server; compiti del coordinatore di emergenza; consapevolezza dei sistemi di supporto | 5 minuti | Personale con accesso alle strutture di Livello 1 o responsabilità di accompagnamento |

**Durata totale**: 30 minuti (tutti i moduli).

**Valutazione**: Quiz breve (5 domande, punteggio minimo di superamento dell'80%). Valutazione non superata: rifacimento entro 5 giorni lavorativi.

**Orientamento per le strutture di Livello 1** (aggiuntivo, in presenza):
- Sopralluogo fisico delle uscite di emergenza, delle ubicazioni degli estintori e dei punti di raccolta
- Dimostrazione del lettore di badge e delle procedure di accesso
- Introduzione ai display del monitoraggio ambientale (ove applicabile)
- Durata: 15 minuti, condotto dal Responsabile delle strutture o delegato

**Obiettivo di completamento della formazione**: 95% del personale con accesso alle strutture annualmente. Il completamento è monitorato tramite [LMS o registro della formazione]. Il mancato completamento viene segnalato al responsabile diretto a 30 giorni di ritardo; l'accesso alla struttura viene sospeso a 60 giorni di ritardo.

---

## Servizi di supporto (A.7.11)

> *Le strutture di elaborazione delle informazioni dovrebbero essere protette da guasti all'alimentazione e altre interruzioni causate da guasti ai servizi di supporto.*

I sistemi di supporto DEVONO essere implementati con capacità e ridondanza proporzionate alla criticità della struttura e testati regolarmente per garantirne l'affidabilità.

### Protezione dell'alimentazione — Gruppo di continuità (UPS)

| Requisito | Livello 1 — Strutture critiche | Livello 2 — Strutture standard |
|-----------|-------------------------------|-------------------------------|
| **Configurazione** | Ridondanza N+1 (doppia unità UPS) | UPS singolo |
| **Autonomia** | Minimo 30 minuti per unità (sufficiente per l'avvio e la stabilizzazione del generatore o per lo spegnimento ordinato) | Minimo 15 minuti (sufficiente per lo spegnimento ordinato) |
| **Monitoraggio** | Monitoraggio in tempo reale con avvisi automatici per lo stato della batteria, il carico e gli eventi di trasferimento | Monitorato durante le ore presidiate |
| **Manutenzione** | Sostituzione della batteria secondo il programma del produttore; test annuale della capacità | Sostituzione della batteria secondo il programma del produttore |

- I sistemi UPS DEVONO proteggere tutte le attrezzature critiche di elaborazione delle informazioni, le infrastrutture di rete e i sistemi di sicurezza (controllo degli accessi, CCTV, rilevamento incendi).
- I sistemi UPS DEVONO essere configurati per supportare lo spegnimento ordinato delle attrezzature che supportano le operazioni aziendali critiche in caso di interruzione prolungata che supera l'autonomia dell'UPS.

#### Metodologia di dimensionamento degli UPS

La capacità degli UPS DEVE essere calcolata utilizzando il seguente processo in quattro fasi per garantire un'autonomia adeguata per le attrezzature protette:

**Fase 1 — Calcolo del carico**:
- Inventariare tutte le attrezzature da proteggere (server, switch di rete, storage, sistemi di sicurezza)
- Sommare il consumo totale di energia in watt (W) o volt-ampere (VA) dalle targhette delle attrezzature o dalle misurazioni del consumo energetico
- Applicare la correzione del fattore di potenza se si utilizzano valori VA (fattore di potenza tipico del carico IT: 0,9)

**Fase 2 — Fattore di crescita**:
- Applicare un margine di crescita del 20–30% al di sopra del carico attuale per accogliere le aggiunte pianificate di attrezzature
- Strutture di Livello 1: margine di crescita del 30% (orizzonte di pianificazione di 3 anni)
- Strutture di Livello 2: margine di crescita del 20%

**Fase 3 — Selezione della capacità degli UPS**:
- Selezionare le unità UPS con capacità nominale superiore al totale della Fase 2
- Livello 1: Ridondanza N+1 (due unità UPS, ciascuna in grado di supportare il carico completo in modo indipendente)
- Livello 2: UPS singolo con capacità superiore al totale della Fase 2
- Verificare che l'autonomia della batteria al carico calcolato soddisfi i requisiti minimi (30 minuti Livello 1, 15 minuti Livello 2)

**Fase 4 — Verifica dell'autonomia**:
- Dopo l'installazione, eseguire un test di scarica a pieno carico per verificare l'autonomia effettiva
- Documentare l'autonomia effettiva rispetto a quella calcolata
- Se l'autonomia effettiva è inferiore al requisito minimo: aggiungere moduli batteria o ridurre il carico protetto
- Riverificare annualmente durante il test della capacità (il degrado della batteria riduce l'autonomia nel tempo)

**Registro del dimensionamento degli UPS**: Documentato nel registro degli asset delle strutture con il calcolo del carico, il modello UPS selezionato, la capacità nominale, il carico misurato, l'autonomia calcolata e l'autonomia effettiva testata.

### Generazione di energia di emergenza

| Requisito | Livello 1 — Strutture critiche | Livello 2 — Strutture standard |
|-----------|-------------------------------|-------------------------------|
| **Generatore** | Generatore di emergenza richiesto | Non richiesto (decisione basata sul rischio) |
| **Capacità del carburante** | Minimo 48 ore a pieno carico | N/A salvo installazione del generatore |
| **Tempo di avvio** | Avvio automatico entro 30 secondi dall'interruzione della rete; commutatore automatico di rete (ATS) | Manuale o automatico come appropriato |
| **Gestione del carburante** | Qualità del carburante testata annualmente; contratti di rifornimento in vigore | Secondo i requisiti del produttore |

- Ove i generatori siano installati, DEVONO essere ispezionati settimanalmente e sottoposti a test di carico secondo il programma di test di seguito.

#### Selezione e gestione del carburante per i generatori

Il tipo di carburante DEVE essere selezionato in base ai requisiti della struttura, all'infrastruttura locale e alle considerazioni ambientali:

| Tipo di carburante | Vantaggi | Svantaggi | Uso raccomandato |
|--------------------|----------|-----------|------------------|
| **Gasolio** | Alta densità energetica; lunga durata di stoccaggio (12–18 mesi con trattamento); ampiamente disponibile; avvio affidabile al freddo | Richiede stoccaggio di carburante in sede; la qualità del carburante degrada nel tempo; normative ambientali per lo stoccaggio in serbatoi | Strutture di Livello 1 che richiedono un'autonomia prolungata (48+ ore) |
| **Gas naturale** | Nessuno stoccaggio di carburante in sede; autonomia illimitata (fornitura utility); minori emissioni; manutenzione ridotta | Dipendente dalla fornitura di gas utility (potrebbe interrompersi durante un disastro regionale); densità energetica inferiore; richiede un gruppo elettrogeno omologato per gas | Strutture di Livello 1 con infrastruttura gas affidabile e percorso utility separato dall'alimentazione elettrica |
| **Propano (GPL)** | Lunga durata di conservazione (indefinita); combustione pulita; affidabile nei climi freddi | Richiede stoccaggio in serbatoi pressurizzati; densità energetica inferiore al gasolio; logistica di rifornimento del serbatoio | Strutture di Livello 2; backup per generatori a gas naturale |

**Calcolo della capacità del carburante** (generatori a gasolio):
1. Determinare il tasso di consumo del carburante del generatore a pieno carico (litri/ora, dai dati del produttore)
2. Moltiplicare per l'autonomia richiesta (48 ore per il Livello 1)
3. Aggiungere un margine di sicurezza del 20%
4. Risultato = capacità minima del serbatoio di carburante

**Requisiti di gestione del carburante** (gasolio):
- Qualità del carburante testata annualmente (contenuto d'acqua, contaminazione microbica, stabilità all'ossidazione)
- Trattamento del carburante (biocida, stabilizzante) applicato secondo il programma del produttore
- Ispezione del serbatoio annualmente (corrosione interna, accumulo d'acqua, integrità strutturale)
- Contratto di rifornimento in vigore con consegna garantita entro 24 ore dalla richiesta
- Livello minimo di carburante mantenuto al 75% della capacità (monitoraggio automatico ove possibile)

### Sistemi di raffreddamento

| Requisito | Livello 1 — Strutture critiche | Livello 2 — Strutture standard |
|-----------|-------------------------------|-------------------------------|
| **Ridondanza** | Doppi percorsi di raffreddamento (minimo N+1) | Sistema di raffreddamento singolo |
| **Monitoraggio** | Monitoraggio continuo della temperatura con avvisi automatici | Monitorato durante le ore presidiate |
| **Risposta ai guasti** | Failover automatico all'unità ridondante; avviso alla gestione delle strutture | Avviso alla gestione delle strutture; risposta manuale |

- La capacità di raffreddamento DEVE essere sufficiente per il carico termico attuale più la crescita pianificata.
- I sistemi di raffreddamento DEVONO essere mantenuti secondo i programmi di manutenzione del produttore, con i filtri dell'aria sostituiti agli intervalli raccomandati.

### Ridondanza delle telecomunicazioni

| Requisito | Livello 1 — Strutture critiche | Livello 2 — Strutture standard |
|-----------|-------------------------------|-------------------------------|
| **Connettività Internet** | Doppio ISP con failover automatico | ISP singolo (secondario raccomandato sulla base della valutazione del rischio) |
| **Diversità del percorso** | Punti di ingresso fisici diversi ove possibile | Ingresso singolo accettabile |
| **Monitoraggio** | Continuo con failover automatico e avvisi | Monitorato durante le ore presidiate |

- Il cablaggio di alimentazione e telecomunicazioni che trasporta dati o supporta i servizi informativi DEVE essere protetto da intercettazioni, interferenze o danni.
- I cavi di alimentazione DEVONO essere segregati dai cavi di comunicazione per prevenire interferenze.
- L'accesso ai locali cavi e ai patch panel DEVE essere limitato dal controllo degli accessi fisici.

#### Procedure di failover delle telecomunicazioni

Le procedure di failover automatico e manuale DEVONO essere documentate e testate per garantire la continuità della connettività:

**Failover automatico** (strutture di Livello 1 con doppio ISP):

| Passaggio | Azione | Tempo target |
|-----------|--------|--------------|
| 1 | Rilevamento guasto ISP primario (link down, perdita di pacchetti >5%, latenza >200ms) | Rilevamento entro 30 secondi |
| 2 | Failover automatico all'ISP secondario avviato dalle attrezzature di routing | Failover entro 60 secondi |
| 3 | Avviso generato alle Operazioni IT (email + dashboard di monitoraggio) | Immediato |
| 4 | Operazioni IT verifica il ripristino del servizio e indaga il guasto dell'ISP primario | Entro 15 minuti |
| 5 | ISP primario ripristinato → failback automatico (o failback manuale se configurato) | Al ripristino dell'ISP |

**Failover manuale** (strutture di Livello 2 o ISP singolo con backup):

| Passaggio | Azione | Responsabile |
|-----------|--------|--------------|
| 1 | Interruzione ISP segnalata o rilevata tramite monitoraggio | Operazioni IT |
| 2 | Verificare che l'interruzione sia lato ISP (non guasto interno delle attrezzature) | Operazioni IT |
| 3 | Attivare la connettività di backup (failover 4G/5G, hotspot mobile o ISP alternativo) | Operazioni IT |
| 4 | Notificare gli utenti interessati della connettività degradata e del ripristino stimato | Operazioni IT |
| 5 | Monitorare il ripristino dell'ISP primario; ripristinare il routing normale quando disponibile | Operazioni IT |

**Backup con ISP singolo per strutture di Livello 2**: Ove sia implementato un ISP singolo, un dispositivo di failover mobile a banda larga 4G/5G (ad es., Cradlepoint, Peplink, o equivalente) DEVE essere disponibile come backup. Il dispositivo di failover DEVE essere testato trimestralmente per confermare l'attivazione della SIM e la sufficienza della larghezza di banda per i servizi critici.

### Programma di test dei servizi di supporto

Tutti i sistemi di resilienza dei servizi di supporto DEVONO essere testati a intervalli regolari per verificare la prontezza operativa:

| Sistema | Tipo di test | Frequenza | Criteri di superamento | Responsabile |
|---------|-------------|-----------|------------------------|--------------|
| **UPS** | Test di failover (simulare interruzione rete, verificare trasferimento alla batteria) | Trimestrale | Trasferimento netto entro il tempo nominale; carico sostenuto per l'autonomia nominale | Responsabile delle strutture |
| **UPS** | Test della capacità della batteria (scarica completa sotto carico) | Annuale | Capacità della batteria >= 80% della capacità nominale | Responsabile delle strutture |
| **Generatore di emergenza** | Test di avvio a vuoto | Mensile | Avvio entro 30 secondi; tensione e frequenza stabili entro 60 secondi | Responsabile delle strutture |
| **Generatore di emergenza** | Test con banco di carico (minimo 30% della potenza nominale, 30 minuti) | Semestrale | Sostiene il carico nominale; temperatura di scarico entro i limiti | Responsabile delle strutture |
| **Generatore di emergenza** | Test di trasferimento a pieno carico (end-to-end con ATS) | Annuale | Trasferimento e ritrasferimento automatici senza interruzione al carico protetto | Responsabile delle strutture |
| **Raffreddamento** | Verifica del failover di ridondanza | Trimestrale | L'unità di standby si attiva; la temperatura rimane entro le soglie | Responsabile delle strutture |
| **Telecomunicazioni** | Test di failover ISP | Annuale | Failover automatico o manuale entro il tempo target documentato; servizi ripristinati | Operazioni IT |

I risultati dei test DEVONO essere documentati con: data del test, sistema testato, procedura di test, risultato (superato/non superato), problemi identificati e azioni correttive. I registri dei test DEVONO essere conservati per 5 anni.

**Risposta al test non superato**: Qualsiasi test non superato DEVE attivare un'indagine immediata, controlli compensativi transitori (ad es., limitare l'utilizzo della struttura, aumentare il monitoraggio) e rimediazione entro 30 giorni. I fallimenti ripetuti DEVONO essere escalati al RSSI.

### Monitoraggio dei servizi di supporto

- I sistemi di supporto (alimentazione, raffreddamento, telecomunicazioni) DEVONO essere monitorati in tempo reale con avvisi per guasti, superamenti delle soglie e condizioni degradate.
- I sistemi di monitoraggio dei servizi di supporto dovrebbero essere integrati con il [BMS] o il [Sistema di monitoraggio ambientale] per la visibilità centralizzata.
- Gli incidenti relativi ai servizi di supporto DEVONO essere registrati e gestiti ai sensi del processo di gestione degli incidenti.

---

## Livelli di criticità delle strutture

Le strutture DEVONO essere classificate per livello di criticità sulla base dell'analisi dell'impatto aziendale. La classificazione del livello determina l'intensità del monitoraggio, i requisiti di protezione ambientale e i livelli di resilienza dei servizi di supporto in tutta questa politica.

| Attributo | Livello 1 — Critico | Livello 2 — Standard |
|-----------|---------------------|----------------------|
| **Definizione** | Data center, sale server primarie, siti di ripristino di emergenza | Uffici aziendali, filiali, sale server non critiche |
| **Criteri di classificazione** | Ospita sistemi aziendali di Livello 1/2; elabora dati RISERVATI; RTO < 4 ore | Ospita sistemi di Livello 3/4; elabora dati INTERNI; RTO > 4 ore |
| **Monitoraggio** | Monitoraggio 24/7 (SOC o servizio di monitoraggio allarmi); SLA di risposta < 15 minuti; rilevamento intrusioni obbligatorio | Monitoraggio durante l'orario lavorativo (8/5); risposta entro il giorno lavorativo successivo accettabile; rilevamento intrusioni basato sul rischio |
| **Ambiente** | Soppressione + rilevamento incendi; rilevamento acqua in tutte le zone; temperatura 18–27 °C +/- 2 °C; monitoraggio continuo | Rilevamento incendi obbligatorio (soppressione se attrezzature > CHF 500k); rilevamento acqua nelle aree ad alto rischio; temperatura 18–27 °C +/- 5 °C |
| **Servizi — Alimentazione** | N+1 UPS (doppie unità, 30 min autonomia ciascuna); generatore di emergenza (carburante per 48 ore); ATS | UPS singolo (autonomia minima 15 min); generatore opzionale |
| **Servizi — Raffreddamento** | Doppi percorsi di raffreddamento (N+1); monitoraggio continuo | Sistema di raffreddamento singolo; monitoraggio durante le ore presidiate |
| **Servizi — Telecom** | Doppio ISP con failover automatico; ingresso con percorso diversificato | ISP singolo; secondario raccomandato |
| **Frequenza di revisione** | Verifica manuale mensile di tutti i sistemi | Verifica manuale trimestrale di tutti i sistemi |

**Processo di assegnazione del livello**: I proprietari dei sistemi, in consultazione con il Responsabile delle strutture e il RSSI, DEVONO determinare il livello appropriato per ciascuna struttura sulla base dei risultati dell'analisi dell'impatto aziendale. Le assegnazioni dei livelli DEVONO essere riesaminate annualmente.

---

## Classificazione degli incidenti

Gli eventi di sicurezza delle infrastrutture fisiche DEVONO essere classificati e gestiti in base alla gravità:

| Gravità | Esempi | Risposta richiesta |
|---------|--------|-------------------|
| **Critica** | Accesso non autorizzato alle aree riservate; violazione fisica; furto di attrezzature; incendio o alluvione grave; guasto totale dell'alimentazione o del raffreddamento | Risposta immediata; attivazione del processo di gestione degli incidenti; notifica al RSSI e alla Direzione generale entro 1 ora |
| **Alta** | Tentativi di accesso falliti ripetuti; tailgating rilevato; badge di accesso smarriti; avvisi ambientali che si avvicinano alle soglie critiche; guasto parziale ai servizi di supporto | Indagine e risposta nella stessa giornata; notifica al RSSI entro 4 ore |
| **Media** | Avvisi di porta tenuta aperta; frequenti falsi allarmi; escursioni ambientali minori (entro le soglie di avviso ma non critiche); singolo guasto al test dei servizi di supporto | Documentato e investigato entro 5 giorni lavorativi; analisi dei trend |
| **Bassa** | Singolo tentativo di accesso fallito; violazioni minori delle politiche; notifiche di manutenzione programmata | Registrato per l'analisi dei trend; riesaminato mensilmente |

Gli incidenti di sicurezza fisica DEVONO essere segnalati e gestiti attraverso il processo di gestione degli incidenti dell'organizzazione (A.5.24–28).

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **Responsabile della sicurezza delle informazioni (RSSI)** | Responsabilità complessiva per la politica di sicurezza delle infrastrutture fisiche; accettazione del rischio per le eccezioni; approvazione del budget; rendicontazione esecutiva sulla postura di sicurezza fisica |
| **Responsabile delle strutture** | Operazioni quotidiane dell'infrastruttura fisica; manutenzione dei sistemi ambientali e di supporto; gestione dei fornitori per i servizi edilizi; esecuzione del programma di test dei servizi di supporto |
| **Responsabile delle operazioni di sicurezza** | Implementazione del monitoraggio della sicurezza fisica; gestione del sistema di controllo degli accessi; operazioni CCTV; gestione del rilevamento delle intrusioni; coordinamento degli incidenti di sicurezza fisica |
| **Operazioni IT** | Integrazione fisico-logica della sicurezza (SIEM); infrastruttura di rete a supporto dei sistemi di sicurezza; gestione della ridondanza delle telecomunicazioni |
| **Proprietari dei sistemi** | Definire i requisiti di sicurezza fisica per i sistemi di propria competenza; partecipare alla classificazione per livello della struttura; segnalare gli incidenti di sicurezza fisica |
| **Audit interno** | Verifica annuale della conformità alla sicurezza fisica; revisione delle prove; test dei controlli |
| **Tutti i dipendenti** | Segnalare incidenti di sicurezza fisica e attività sospette; rispettare le procedure di controllo degli accessi e di gestione dei visitatori; seguire le procedure di emergenza ambientale |

---

## Prove per questa politica

| N. | Prova | Responsabile | Frequenza |
|----|-------|--------------|-----------|
| 1 | **Log del sistema di controllo degli accessi fisici** (eventi di accesso concesso/negato con identificazione individuale) | Responsabile delle operazioni di sicurezza | *Registrazione continua; riesaminato mensilmente; conservato 12 mesi* |
| 2 | **Registri operativi del sistema CCTV** (rapporti di uptime, verifiche dello stato delle telecamere, verifica delle registrazioni) | Responsabile delle operazioni di sicurezza | *Verifiche settimanali dello stato; conservato 12 mesi* |
| 3 | **Registri dei test del sistema di rilevamento delle intrusioni** (risultati dei test trimestrali, verifica della risposta agli allarmi) | Responsabile delle operazioni di sicurezza | *Trimestrale; conservato 3 anni* |
| 4 | **Registri della gestione dei visitatori** (registro dei visitatori con nome, organizzazione, referente interno, conformità all'accompagnamento) | Responsabile delle operazioni di sicurezza | *Continuo; conservato 12 mesi* |
| 5 | **Registri della revisione dei diritti di accesso** (risultati della revisione semestrale, azioni di revoca) | Responsabile delle operazioni di sicurezza | *Semestrale; conservato 3 anni* |
| 6 | **Registri di ispezione e test del sistema antincendio** (certificati dei sistemi di rilevamento e soppressione, test delle porte antincendio) | Responsabile delle strutture | *Semestrale / annuale per livello; conservato 5 anni* |
| 7 | **Dati del monitoraggio ambientale** (log di temperatura e umidità; registrazioni dei superamenti delle soglie) | Responsabile delle strutture | *Registrazione continua; conservato 12 mesi* |
| 8 | **Registri di manutenzione e test del sistema di rilevamento acqua** | Responsabile delle strutture | *Verifica trimestrale; conservato 3 anni* |
| 9 | **Registri dei test degli UPS** (test di failover trimestrali, test annuali della capacità) | Responsabile delle strutture | *Secondo il programma di test; conservato 5 anni* |
| 10 | **Registri dei test del generatore** (test di avvio mensili, test di carico semestrali, test di trasferimento annuali) | Responsabile delle strutture | *Secondo il programma di test; conservato 5 anni* |
| 11 | **Registri di verifica della ridondanza del raffreddamento** (test di failover trimestrali) | Responsabile delle strutture | *Trimestrale; conservato 3 anni* |
| 12 | **Registri dei test di failover delle telecomunicazioni** | Operazioni IT | *Annuale; conservato 3 anni* |
| 13 | **Valutazione del rischio delle minacce ambientali** (valutazione del rischio specifica per struttura con cronologia delle revisioni) | Responsabile delle strutture / RSSI | *Revisione annuale; conservato 5 anni* |
| 14 | **Registri delle esercitazioni di risposta alle emergenze** (data, scenario, partecipanti, risultanze, azioni) | Responsabile delle strutture | *Annuale; conservato 3 anni* |
| 15 | **Registro delle eccezioni** (deroghe approvate alla politica con accettazione del rischio e controlli compensativi) | RSSI | *Per evento; riesaminato trimestralmente; conservato attivo + 2 anni* |

---

# Conformità alla politica

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa politica attraverso vari metodi, tra cui, a titolo non esaustivo, rapporti dei sistemi di sicurezza fisica, registri dei test dei servizi di supporto, dati del monitoraggio ambientale, ispezioni delle strutture, audit interni ed esterni, e feedback al proprietario della politica.

La conformità DEVE essere valutata utilizzando le seguenti metriche ponderate:

| Metrica | Peso | Fonte di misurazione |
|---------|------|----------------------|
| Disponibilità del sistema di controllo degli accessi e completezza dei log | 20% | Log del [Sistema di controllo degli accessi] |
| Conformità dei parametri ambientali (temperatura/umidità entro le soglie) | 20% | [Sistema di monitoraggio ambientale] / [BMS] |
| Tasso di successo dei test di resilienza dei servizi di supporto (tutti i test superati secondo il programma) | 15% | Registri dei test |
| Stato operativo dei sistemi di rilevamento incendi e acqua | 15% | Registri delle ispezioni |
| Rispetto delle tempistiche di risposta agli incidenti di sicurezza fisica | 15% | Registrazioni degli incidenti |
| Conformità alla gestione dei visitatori (registrazione, accompagnamento, restituzione badge) | 10% | Registri dei visitatori |
| Completamento della formazione sulla consapevolezza della sicurezza fisica | 5% | Registri della formazione |

| Punteggio | Valutazione | Azione |
|-----------|-------------|--------|
| > 90% | Eccellente | Mantenere i controlli attuali |
| 75–89% | Buono | Affrontare le lacune nel prossimo ciclo di revisione |
| 60–74% | Accettabile | Sviluppare un piano di rimediazione entro 30 giorni |
| < 60% | Non conforme | Rimediazione immediata richiesta; escalation al RSSI |

## Eccezioni

Qualsiasi eccezione a questa politica DEVE essere approvata e registrata in anticipo dal Responsabile della sicurezza delle informazioni, con valutazione documentata del rischio, controlli compensativi e una data di revisione definita (massimo 6 mesi, rinnovabile). Gli scenari di eccezione validi includono l'infeasibilità tecnica, i costi sproporzionati rispetto al rischio e le variazioni temporanee durante le transizioni delle strutture. Le eccezioni DEVONO essere riferite al team di revisione della direzione.

## Non conformità

Un dipendente che abbia violato questa politica può essere soggetto a provvedimenti disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa politica è riesaminata e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO considerare le modifiche alle operazioni delle strutture, i profili di rischio ambientale, i requisiti normativi, i progressi tecnologici nei sistemi di sicurezza fisica, le lezioni apprese dagli incidenti e dai guasti ai test dei servizi di supporto, e i risultati degli audit.

---

# Aree della norma ISO 27001 trattate

Politica sulla sicurezza delle infrastrutture fisiche — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Politiche per la sicurezza delle informazioni |
| Clausola 5.2 Politica | 5.4 Responsabilità della direzione |
| Clausola 6.2 Obiettivi della sicurezza delle informazioni | 5.36 Conformità alle politiche, norme e standard |
| Clausola 7.3 Consapevolezza | 6.3 Consapevolezza, formazione e addestramento sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | **7.4 Monitoraggio della sicurezza fisica** |
| | **7.5 Protezione dalle minacce fisiche e ambientali** |
| | 7.8 Ubicazione e protezione delle attrezzature |
| | **7.11 Servizi di supporto** |
| | 7.12 Sicurezza del cablaggio |

**Quadro normativo e giuridico**:

| Framework | Pertinenza |
|-----------|------------|
| nLPD svizzera (revDSG) | Art. 8 — Misure tecniche e organizzative per la sicurezza fisica delle strutture di elaborazione dei dati |
| OPDo svizzera | Art. 1–3 — Requisiti minimi per la sicurezza dei dati, incluse le misure fisiche |
| RGPD UE (ove applicabile) | Art. 32 — Sicurezza del trattamento incluse le misure fisiche |
| ISO/IEC 27001:2022 | Allegato A Controlli 7.4 (Monitoraggio della sicurezza fisica), 7.5 (Protezione ambientale), 7.11 (Servizi di supporto) |
| ISO/IEC 27002:2022 | Sezioni 7.4, 7.5, 7.11 — Linee guida di attuazione |
| ASHRAE | Linee guida termiche per gli ambienti di elaborazione dati (temperatura/umidità) |
| NFPA 2001 / ISO 14520 | Sistemi di soppressione a agente pulito per spazi occupati |
| NFPA 110 | Requisiti di test dei sistemi di alimentazione di emergenza e standby |
| NIST SP 800-53 Rev 5 | PE-1 fino a PE-20 — Famiglia di protezione fisica e ambientale |
| CIS Controls v8 | Controllo 1 (Inventario), Controllo 12 (Infrastruttura di rete — cablaggio fisico) |
| **Condizionale**: Circolare FINMA 2023/1 | Istituto finanziario regolamentato svizzero — requisiti di sicurezza fisica rafforzati |
| **Condizionale**: DORA (UE) 2022/2554 | Entità dei servizi finanziari UE — resilienza operativa per le infrastrutture ICT |
| **Condizionale**: NIS2 (UE) 2022/2555 | Entità essenziale/importante nell'UE — sicurezza fisica per le infrastrutture critiche |

---

<!-- QA_VERIFIED: 2026-04-03 -->
