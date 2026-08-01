<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.19-23-IT:operational:OP-POL:a.5.19-23 -->
**ISMS-OP-POL-A.5.19-23 — Sicurezza dei servizi cloud e dei fornitori**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Sicurezza dei servizi cloud e dei fornitori |
| **Tipo di documento** | Policy operativa |
| **ID documento** | ISMS-OP-POL-A.5.19-23 |
| **Autore del documento** | Responsabile della sicurezza delle informazioni (RSSI) |
| **Proprietario del documento** | Amministratore delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data] |
| **Versione** | 0.1 |
| **Data versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 0.1 | [Data] | RSSI | Policy operativa iniziale per ISO 27001:2022 |

**Ciclo di revisione**: Annuale
**Data prossima revisione**: [Data di entrata in vigore + 12 mesi]

**Approvato da**: [RSSI / Direzione generale]

**Documenti correlati**:

- Controlli ISO/IEC 27001:2022 A.5.19–A.5.23 — Sicurezza dei fornitori e dei servizi cloud
- Controlli ISO/IEC 27002:2022 5.19–5.23 — Linee guida per l'implementazione

**Controlli Annex A correlati**:

| Controllo | Relazione con la sicurezza dei fornitori e del cloud |
|-----------|------------------------------------------------------|
| A.5.9 Inventario delle informazioni e degli asset | Fornitori e servizi cloud tracciati nell'inventario degli asset |
| A.5.12–13 Classificazione ed etichettatura delle informazioni | La classificazione dei dati guida i requisiti di sicurezza dei fornitori |
| A.5.14 Trasferimento delle informazioni | Requisiti di trasferimento cifrato per lo scambio di dati con i fornitori |
| A.5.15–16–18 Gestione delle identità e degli accessi | Provisioning e revoca degli accessi del personale dei fornitori |
| A.5.24–28 Gestione degli incidenti | La notifica degli incidenti dei fornitori si integra nel processo di gestione degli incidenti |
| A.5.30, A.8.13–14 Continuità operativa e backup | Scenari di interruzione dei fornitori, validazione della strategia di uscita, backup indipendenti |
| A.5.31 Requisiti legali, normativi e contrattuali | Obblighi contrattuali, requisiti del responsabile del trattamento nLPD/GDPR |
| A.5.34 Privacy e dati personali | Accordi di trattamento dei dati, divulgazione dei sub-responsabili, trasferimenti transfrontalieri |
| A.8.8 Gestione delle vulnerabilità | Impegni dei fornitori in materia di patching, divulgazione delle vulnerabilità |
| A.8.10 Cancellazione delle informazioni | Verifica della distruzione dei dati del fornitore alla fine del contratto |
| A.8.24 Uso della crittografia | Requisiti di cifratura per i dati del fornitore a riposo e in transito |

**Policy interne correlate**:

- Policy di classificazione e gestione delle informazioni
- Policy di gestione degli incidenti
- Policy di trasferimento delle informazioni
- Policy sulla privacy e protezione dei dati personali
- Policy di continuità operativa e disaster recovery

---

# Policy sulla sicurezza dei servizi cloud e dei fornitori

## Scopo

Lo scopo di questa policy è gestire la sicurezza delle informazioni per l'utilizzo dei servizi cloud e garantire i requisiti di sicurezza dei dati dei fornitori terzi, dei loro subappaltatori e della catena di fornitura.

Questa policy supporta la nLPD svizzera (revDSG) implementando misure tecniche e organizzative proporzionate al rischio per proteggere i dati personali (inclusi i dati personali degni di particolare protezione) quando trattati da fornitori esterni e fornitori di servizi cloud. Laddove l'organizzazione tratti dati di persone fisiche nell'UE/SEE, si applicano anche i requisiti del GDPR. I controlli di sicurezza dei fornitori e dei servizi cloud sono misure chiave per dimostrare la conformità agli obblighi di protezione dei dati nell'ambito di entrambi i quadri normativi.

## Ambito di applicazione

Tutti i dipendenti e gli utenti terzi.

Tutti i fornitori terzi e i fornitori di servizi cloud che trattano, archiviano o trasmettono dati riservati o personali.

Tutti i servizi cloud (IaaS, PaaS, SaaS) utilizzati dall'organizzazione.

## Principio

I fornitori terzi e i fornitori di servizi cloud DEVONO soddisfare i requisiti dell'organizzazione, della legislazione e della normativa in materia di sicurezza dei dati. L'attendibilità dei fornitori DEVE essere verificata, non presunta — è richiesta una validazione basata sulle evidenze della postura di sicurezza del fornitore attraverso una due diligence sistematica, impegni contrattuali e monitoraggio continuo.

I contratti per i servizi cloud sono spesso predefiniti e non aperti a negoziazione. Laddove questo sia il caso, l'organizzazione DEVE valutare se le condizioni standard del fornitore soddisfano i propri requisiti di sicurezza e documentare eventuali rischi residui. Laddove le condizioni non siano negoziabili e non soddisfino i requisiti, DEVONO essere identificati controlli compensativi o DEVE essere valutato un fornitore alternativo.

L'organizzazione DEVE comprendere e documentare il modello di responsabilità condivisa per ogni servizio cloud. Le responsabilità di sicurezza sono suddivise tra il fornitore di servizi cloud e l'organizzazione, e questa suddivisione varia in base al modello di servizio (IaaS, PaaS, SaaS). L'organizzazione rimane responsabile della sicurezza dei propri dati, della gestione delle identità e degli accessi e della protezione degli endpoint indipendentemente dal modello di servizio. Il fornitore è responsabile della sicurezza dell'infrastruttura sottostante. Le aree di responsabilità condivisa DEVONO essere esplicitamente documentate e riviste.

**La documentazione della responsabilità condivisa DEVE includere**:

| Area di responsabilità | Responsabilità del fornitore | Responsabilità dell'organizzazione | Note |
|-----------------------|-----------------------------|------------------------------------|------|
| Sicurezza fisica del data center | Sì | | Il fornitore controlla l'accesso fisico |
| Infrastruttura di rete | Sì | | Il fornitore protegge la rete sottostante |
| Infrastruttura host | Sì (IaaS/PaaS/SaaS) | Sì (solo IaaS — patching OS) | Per IaaS, l'organizzazione gestisce il sistema operativo |
| Sicurezza dell'applicazione | Sì (solo SaaS) | Sì (IaaS/PaaS) | Per SaaS, il fornitore è responsabile |
| Cifratura dei dati a riposo | Sì (predefinita) | Sì (gestione delle chiavi) | L'organizzazione può portare le proprie chiavi (BYOK) |
| Gestione delle identità e degli accessi | | Sì | L'organizzazione è sempre responsabile |
| Classificazione e gestione dei dati | | Sì | L'organizzazione è sempre responsabile |
| Sicurezza degli endpoint | | Sì | L'organizzazione è sempre responsabile |

I modelli di responsabilità condivisa DEVONO essere documentati per ogni servizio cloud **Critico** e rivisti annualmente.

---

## Registro dei fornitori e dei servizi cloud

Tutti i fornitori terzi e i servizi cloud DEVONO essere registrati e documentati nel **Registro dei fornitori e dei servizi cloud**.

**Posizione del registro**: [Piattaforma GRC, sistema di approvvigionamento o foglio di calcolo dedicato in SharePoint/equivalente]

**Proprietario del registro**: [RSSI, Responsabile degli acquisti o IT Manager]

**Accesso**: L'accesso al registro è limitato al personale autorizzato (leadership IT, team di sicurezza delle informazioni, approvvigionamento). Il registro è classificato come **Interno**.

**Frequenza di aggiornamento**: Il registro DEVE essere rivisto e aggiornato almeno **trimestralmente** o in occasione di ogni nuovo rapporto con un fornitore, modifica contrattuale o uscita del fornitore.

I fornitori e i servizi cloud DEVONO essere valutati in base alla loro criticità per il business.

I fornitori e i servizi cloud DEVONO essere classificati in base ai dati trattati, archiviati o trasmessi e alla loro criticità per le operazioni aziendali:

| Classificazione | Criteri | Frequenza di revisione |
|-----------------|---------|------------------------|
| **Critico** | Accesso a dati Riservati/Limitati, OPPURE operazioni aziendali fondamentali (un'interruzione causa impatto immediato al business), OPPURE trattamento di dati personali degni di particolare protezione (nLPD Art. 5) | Annuale |
| **Importante** | Accesso a dati Interni ma non Riservati, OPPURE servizi di supporto (un'interruzione causa moderate interruzioni entro 24–48 ore), OPPURE trattamento limitato di dati personali | Ogni due anni |
| **Standard** | Nessun accesso ai dati o solo dati Pubblici, OPPURE servizi commodity (facilmente sostituibili, impatto minimo sul business) | Al rinnovo del contratto |

**Esempi**: Critico — fornitore di hosting cloud, elaboratore di buste paga, servizio di backup, CRM con dati dei clienti. Importante — strumento di marketing automation, SaaS per la gestione dei progetti, strumenti di collaborazione. Standard — fornitore di forniture per ufficio, servizi di sicurezza fisica (senza accesso ai dati).

Oltre a quanto sopra, DEVONO essere acquisite come minimo le seguenti informazioni:

- Nome e dati di contatto del fornitore o del servizio cloud
- Cosa fa per noi (descrizione del servizio)
- Quali dati tratta, archivia o trasmette
- Livello di classificazione dei dati (Pubblico, Interno, Riservato, Limitato)
- Se è in vigore un contratto e una copia del contratto
- Quali assicurazioni abbiamo sulla loro sicurezza dei dati (certificazioni, rapporti di audit)
- Luoghi di trattamento e archiviazione dei dati (paese e regione)
- Data di scadenza del contratto e data della prossima revisione
- Sub-responsabili del trattamento utilizzati dal fornitore (ove noti)

## Requisiti di sicurezza delle informazioni

I fornitori e i fornitori di servizi cloud dovrebbero possedere certificazioni di sicurezza delle informazioni pertinenti che coprono i servizi forniti. Come minimo dovrebbero avere:

- Una certificazione ISO 27001, **oppure**
- Un rapporto SOC 2 Type II (attuale, entro 12 mesi)

Per i fornitori di servizi cloud che gestiscono dati personali, è inoltre attesa la norma ISO 27018 (protezione dei dati personali nei cloud pubblici) o evidenza equivalente dei controlli di protezione dei dati personali.

La certificazione CSA STAR Livello 2 (ISO 27001 + Cloud Controls Matrix) è riconosciuta come un forte indicatore di maturità della sicurezza specifica per il cloud.

Laddove un fornitore non possa fornire certificazioni riconosciute, l'organizzazione DEVE condurre una valutazione del rischio documentata e, se il fornitore viene ingaggiato, implementare controlli compensativi e ottenere l'accettazione del rischio da parte del Responsabile della sicurezza delle informazioni e del proprietario del rischio.

**Potenziali controlli compensativi**:

- Condizioni contrattuali rafforzate con specifici obblighi di sicurezza (cifratura, logging degli accessi, notifica degli incidenti)
- Questionario di sicurezza completato annualmente con risposte verificate rispetto ai risultati successivi
- Accesso limitato ai dati — limitare il fornitore ai soli dati non personali o non riservati
- Diritti di audit — diritto di condurre un audit di sicurezza o un penetration test (se contrattualmente realizzabile)
- Accordi di escrow — escrow del codice o dei dati per la continuità operativa
- Requisiti di assicurazione cyber

## Audit e revisione

Ogni fornitore e servizio cloud è soggetto ad audit e revisione della sicurezza dei dati in conformità con il seguente calendario basato sul rischio:

| Classificazione del fornitore | Frequenza di revisione | Ambito della revisione |
|------------------------------|------------------------|------------------------|
| **Critico** (accesso a dati Riservati/Limitati o operazioni fondamentali) | Annuale | Revisione completa della conformità, prestazioni SLA, aggiornamento delle certificazioni, rivalutazione del rischio |
| **Importante** (accesso limitato ai dati o servizi di supporto) | Ogni due anni | Validazione della conformità, stato del contratto, verifica delle certificazioni |
| **Standard** (nessun accesso ai dati, servizi commodity) | Al rinnovo del contratto | Necessità aziendale continuata, verifica di sicurezza di base |

Il livello di audit e revisione è basato sulla classificazione del rischio del fornitore e sulla sensibilità dei dati coinvolti.

I fornitori di servizi cloud sono soggetti agli stessi requisiti di audit e revisione.

### Approccio all'audit dei servizi cloud

I principali fornitori di servizi cloud (AWS, Azure, Google Cloud, Microsoft 365, Salesforce, ecc.) in genere non consentono audit diretti da parte dei clienti a causa dei vincoli di sicurezza multi-tenant e di scalabilità operativa.

**Meccanismi di assicurazione alternativi** (accettati in sostituzione dell'audit diretto):

- Rapporti di terze parti indipendenti: SOC 2 Type II, certificazione ISO 27001, attestazione CSA STAR
- Certificazioni di conformità: ISO 27017, ISO 27018 e attestazioni specifiche di settore ove applicabili
- Rapporti di trasparenza: documentazione di sicurezza pubblicata dal fornitore, matrici di conformità, elenchi di sub-responsabili del trattamento
- Dashboard di stato del servizio: disponibilità del servizio in tempo reale e divulgazione degli incidenti

L'organizzazione DEVE ottenere e revisionare i rapporti di audit indipendenti più recenti (**entro 12 mesi**) per ogni servizio cloud Critico su base annuale.

Laddove un fornitore cloud non fornisca rapporti indipendenti di terze parti, il servizio NON deve essere utilizzato per dati Riservati o Limitati senza l'approvazione del RSSI e la documentata accettazione del rischio residuo.

## Gestione del rischio

Ogni fornitore che gestisce dati riservati o personali DEVE essere inserito nel Registro dei rischi e gestito tramite il processo di gestione del rischio dell'organizzazione.

I rischi dei servizi cloud DEVONO includere la valutazione di:

- Disponibilità del servizio e impatto aziendale dell'interruzione
- Residenza dei dati ed esposizione giurisdizionale
- Vendor lock-in e fattibilità dell'uscita
- Rischio di concentrazione (dipendenza da un singolo fornitore per servizi critici) — laddove un singolo fornitore ospiti più del 50% dei servizi critici o più del 75% dei dati Riservati, ciò DEVE essere evidenziato nel registro dei rischi con un piano di mitigazione o accettazione del rischio residuo. Le opzioni di mitigazione includono la diversificazione multi-fornitore, il deployment multi-regione presso lo stesso fornitore e la strategia di uscita validata
- Rischio dei sub-responsabili del trattamento (trattamento dei dati a valle)

## Selezione dei fornitori e dei servizi cloud

I fornitori e i servizi cloud DEVONO essere selezionati in base alla loro capacità di soddisfare le esigenze del business.

Prima di ingaggiare un fornitore o un fornitore di servizi cloud, DEVE essere svolta una due diligence sulla sicurezza dei dati che include:

- Un livello accettabile di sicurezza dei dati con rischi identificati, registrati e gestiti
- Referenze appropriate da clienti esistenti
- Certificazioni appropriate (ISO 27001, SOC 2 Type II o equivalente — si vedano i requisiti di sicurezza delle informazioni sopra)
- Contratti e accordi appropriati con i fornitori che includono i requisiti di sicurezza dei dati
- Conformità legale e normativa, inclusa la nLPD (revDSG) e il GDPR ove applicabile
- Valutazione dei luoghi di trattamento e archiviazione dei dati rispetto ai requisiti di residenza dei dati dell'organizzazione
- Verifica che le condizioni standard del fornitore soddisfino i requisiti di sicurezza dell'organizzazione (in particolare per i servizi cloud con accordi non negoziabili)
- Valutazione della fattibilità dell'uscita: capacità di esportazione dei dati, formati supportati, assistenza alla transizione e fornitori alternativi

## Contratti, accordi e accordi di trattamento dei dati

DEVE essere in vigore un contratto, un accordo e/o un Accordo di trattamento dei dati (ATD) appropriato e applicabile prima di ingaggiare qualsiasi fornitore o fornitore di servizi cloud per trattare, archiviare o trasmettere informazioni riservate o personali.

I contratti e gli accordi DEVONO trattare, come minimo:

- Descrizione dei dati trattati, archiviati o trasmessi
- Requisiti e obblighi in materia di sicurezza delle informazioni
- Requisiti di notifica degli incidenti (si veda la Gestione degli incidenti di sicurezza di seguito)
- Diritti di audit ove appropriato, praticabile e consentito (si riconosce che i principali fornitori cloud in genere non consentono audit diretti; l'attestazione di terze parti indipendenti è accettata come evidenza alternativa)
- Requisiti di divulgazione e approvazione dei sub-responsabili del trattamento
- Obblighi di restituzione e distruzione dei dati alla cessazione del contratto
- Accordi sul livello di servizio relativi a disponibilità, tempi di risposta al supporto e metriche di sicurezza
- Disposizioni di uscita inclusa l'esportazione dei dati, l'assistenza alla transizione e i periodi di preavviso per la cessazione

Tutte le policy dell'organizzazione si applicano all'utilizzo del fornitore o del servizio cloud.

### Requisiti per subappaltatori e sub-responsabili del trattamento

L'utilizzo da parte dei fornitori di subappaltatori o sub-responsabili del trattamento DEVE essere approvato dal Responsabile della sicurezza delle informazioni. I subappaltatori e i sub-responsabili del trattamento sono soggetti alle stesse condizioni e requisiti di sicurezza del fornitore.

**Modelli di approvazione**:

- **Autorizzazione specifica**: L'organizzazione approva ogni sub-responsabile del trattamento individualmente (preferito per i fornitori Critici che trattano dati Riservati o Limitati)
- **Autorizzazione generale con notifica**: L'organizzazione concede l'autorizzazione generale per i sub-responsabili del trattamento che soddisfano criteri specificati, con preavviso di almeno 30 giorni in caso di modifiche (accettabile per i fornitori Importanti)

I fornitori di servizi cloud DEVONO divulgare il proprio elenco di sub-responsabili del trattamento. L'organizzazione DEVE essere notificata delle modifiche ai sub-responsabili del trattamento **almeno 30 giorni prima** e DEVE mantenere il diritto di opporsi ove contrattualmente realizzabile. Laddove i diritti di opposizione non possano essere ottenuti (come è comune con i principali fornitori cloud), questa limitazione DEVE essere documentata nel registro dei rischi come rischio residuo con controlli compensativi (cifratura, monitoraggio degli accessi).

### Accordi di trattamento dei dati (nLPD/GDPR)

Tutti i fornitori che trattano dati personali per conto dell'organizzazione DEVONO avere in vigore un Accordo di trattamento dei dati che soddisfi i requisiti della nLPD svizzera (revDSG) Art. 9 e, ove applicabile, del GDPR Art. 28.

L'Accordo di trattamento dei dati DEVE trattare:

- Oggetto e durata del trattamento
- Natura e finalità del trattamento
- Tipo di dati personali e categorie di interessati
- Obblighi e diritti del titolare del trattamento
- Requisiti di approvazione dei sub-responsabili del trattamento (specifici o generali con notifica)
- Misure di sicurezza dei dati (tecniche e organizzative)
- Assistenza con le richieste di esercizio dei diritti degli interessati
- Restituzione o cancellazione dei dati alla cessazione del contratto
- Diritti di audit e ispezione

### Trasferimenti transfrontalieri di dati

Laddove i fornitori o i fornitori di servizi cloud trattino o archivino dati personali al di fuori della Svizzera, l'organizzazione DEVE verificare che esista un'adeguata protezione dei dati nel paese di destinazione ai sensi dell'elenco di adeguatezza del Consiglio federale svizzero (Allegato 1 all'Ordinanza sulla protezione dei dati).

Per i trasferimenti verso paesi non inclusi nell'elenco di adeguatezza, DEVONO essere in vigore salvaguardie appropriate:

- Clausole Contrattuali Standard (SCC) modificate per la conformità al diritto svizzero, **oppure**
- Norme vincolanti d'impresa (BCR) approvate dall'IFPDT, **oppure**
- Altri meccanismi di trasferimento riconosciuti

Per i trasferimenti verso gli Stati Uniti, l'organizzazione DEVE verificare che l'organizzazione ricevente sia certificata nell'ambito del Swiss-U.S. Data Privacy Framework. Laddove il fornitore abbia sede negli USA e sia soggetto al CLOUD Act statunitense, DEVE essere documentata una valutazione del rischio giurisdizionale, inclusi gli accordi di cifratura e gestione delle chiavi e gli impegni del fornitore in materia di contestazione legale.

## Gestione degli incidenti di sicurezza

I fornitori e i fornitori di servizi cloud DEVONO disporre di un processo di gestione degli incidenti di sicurezza.

Gli incidenti di sicurezza dei fornitori e dei servizi cloud che impattano informazioni riservate o personali DEVONO essere segnalati all'organizzazione entro i seguenti termini:

| Classificazione del fornitore | Termine di notifica | Note |
|------------------------------|---------------------|------|
| **Critico** | **12 ore** (obbligatorio) | DEVE essere contrattualmente impegnato |
| **Importante** | **24 ore** (obiettivo) | Best effort dove le 12 ore non sono realizzabili |
| **Standard** | **72 ore** (accettabile) | Accettabile se non è coinvolta una violazione di dati personali |

Laddove un fornitore non possa impegnarsi al termine di 12 ore, ciò DEVE essere documentato come rischio residuo con controlli compensativi (revisioni più frequenti del fornitore, monitoraggio potenziato, fornitore di backup).

La notifica DEVE includere, come minimo:

- Descrizione dell'incidente
- Sistemi e dati interessati
- Misure di contenimento adottate
- Impatto stimato e tempistica di risoluzione

Gli incidenti di sicurezza dei fornitori e dei servizi cloud DEVONO essere gestiti nell'ambito del processo di gestione degli incidenti dell'organizzazione, in conformità con la Policy di gestione degli incidenti.

Laddove un incidente del fornitore implichi una violazione di dati personali, l'organizzazione DEVE valutare gli obblighi di notifica ai sensi della nLPD (notifica all'IFPDT il prima possibile) e, ove applicabile, del GDPR Art. 33 (notifica all'autorità di controllo entro 72 ore).

Laddove appropriato, il processo di gestione degli incidenti del fornitore DEVE essere seguito in coordinamento con le procedure proprie dell'organizzazione.

## Fine del contratto

Alla fine del contratto, il fornitore o il fornitore di servizi cloud DEVE confermare per iscritto di aver soddisfatto i propri obblighi contrattuali e legali per la distruzione delle informazioni riservate e personali dell'organizzazione.

Laddove appropriato, praticabile e pertinente (riconoscendo le limitazioni dei servizi cloud), DEVONO essere completate le seguenti attività:

- Tutti i dati dell'organizzazione vengono restituiti in un formato utilizzabile o distrutti in modo sicuro, secondo le indicazioni dell'organizzazione
- Viene fornita conferma scritta della distruzione dei dati, incluso il metodo utilizzato
- Tutti gli accessi ai sistemi e alle informazioni dell'organizzazione vengono revocati
- Tutti gli asset dell'organizzazione (fisici e logici) vengono restituiti
- I certificati di distruzione vengono ottenuti laddove i dati siano stati classificati come Riservati o Limitati

## Modifiche al fornitore di servizi cloud

Le modifiche a un fornitore di servizi cloud richiedono l'approvazione formale, scritta e documentata del AD o dell'autorità delegata.

Le modifiche DEVONO seguire la Policy di gestione dei cambiamenti e il relativo processo.

Le modifiche ai fornitori cloud sono cambiamenti significativi e NON devono essere prese alla leggera. Tali modifiche DEVONO essere trattate come un progetto con risorse appropriate, gestione del rischio, project management e comunicazione agli stakeholder.

L'organizzazione DEVE mantenere una strategia di uscita per ogni servizio cloud **Critico** per garantire che una transizione o un'uscita possano essere eseguiti in modo controllato se necessario.

**Componenti minimi della strategia di uscita**:

- **Capacità di esportazione dei dati**: processo di esportazione dei dati documentato e formati supportati (CSV, JSON, API, ripristino da backup)
- **Tempistica della transizione**: tempo stimato per la migrazione a un fornitore alternativo (ipotizzare il caso peggiore: uscita forzata)
- **Fornitori alternativi**: almeno un fornitore alternativo pre-identificato e valutato
- **Costi di uscita**: costo stimato (licenze, servizi professionali, migrazione dei dati)
- **Dipendenze**: integrazioni e dipendenze identificate che richiederebbero la riconfigurazione
- **Test di uscita**: verifica che l'esportazione dei dati funzioni (test eseguito annualmente per i servizi Critici)

Le strategie di uscita DEVONO essere riviste **annualmente** o al rinnovo del contratto.

---

## Evidenze

Le seguenti evidenze dimostrano la conformità a questa policy:

- **Registro dei fornitori e dei servizi cloud** — completo, aggiornato, con classificazione dei dati e date di revisione; *revisione trimestrale*
- **Contratti firmati e Accordi di trattamento dei dati** — per tutti i fornitori che gestiscono dati riservati o personali; *registro dei contratti mantenuto da [Approvvigionamento/Legale]*
- **Certificazioni dei fornitori archiviate** — ISO 27001, SOC 2 Type II, CSA STAR (attuali entro 12 mesi); *revisione annuale per i fornitori Critici*
- **Verbali di riunioni di revisione dei fornitori** e rapporti sulle prestazioni — *revisioni annuali per Critici, biennali per Importanti*
- **Voci del Registro dei rischi** — per i fornitori che gestiscono dati riservati o personali; *revisione trimestrale*
- **Registri di notifica degli incidenti** dai fornitori — *tracciati nel sistema di gestione degli incidenti*
- **Accordi di trattamento dei dati** con condizioni conformi a nLPD/GDPR — *revisionati al rinnovo del contratto o in caso di modifica normativa*
- **Valutazioni dei trasferimenti transfrontalieri** — verifica di adeguatezza, SCC o certificazione DPF; *documentate per ogni fornitore/servizio cloud con trasferimento transfrontaliero*
- **Documentazione della strategia di uscita** per i servizi cloud Critici — *revisionata annualmente; test di uscita eseguiti per i principali servizi Critici*
- **Registri dei sub-responsabili del trattamento** e documenti di notifica delle modifiche — *mantenuti ai sensi delle condizioni degli ATD*
- **Conferme di distruzione dei dati** alla cessazione del contratto — *certificati di distruzione o conferma scritta conservati per 2 anni*
- **Documentazione del modello di responsabilità condivisa** — per ogni servizio cloud Critico; *revisionata annualmente*

---

# Conformità alla policy

## Misurazione della conformità

Il team di gestione della sicurezza delle informazioni verificherà la conformità a questa policy attraverso vari metodi, inclusi a titolo non esaustivo: revisioni del registro dei fornitori, audit dei contratti, verifiche delle certificazioni, audit interni ed esterni, e feedback al proprietario della policy.

## Deroghe

Qualsiasi deroga a questa policy DEVE essere approvata e registrata preventivamente dal Responsabile della sicurezza delle informazioni, con documentazione dell'accettazione del rischio e dei controlli compensativi. Le deroghe DEVONO essere segnalate al Team di revisione del management.

## Non conformità

Un dipendente ritenuto responsabile di aver violato questa policy potrà essere soggetto a misure disciplinari, fino alla risoluzione del rapporto di lavoro.

## Miglioramento continuo

Questa policy è rivista e aggiornata nell'ambito del processo di miglioramento continuo. Le revisioni DEVONO tener conto delle variazioni al panorama del rischio dei fornitori, degli sviluppi del mercato dei servizi cloud, dei cambiamenti normativi (inclusi la nLPD, il GDPR e i quadri normativi emergenti), degli sviluppi delle minacce alla catena di fornitura e delle lezioni apprese dagli incidenti con i fornitori.

---

# Sezioni della norma ISO 27001 trattate

Policy sulla sicurezza dei servizi cloud e dei fornitori — Mappatura dei controlli ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clausola 5.1 Leadership e impegno | 5.1 Policy per la sicurezza delle informazioni |
| Clausola 5.2 Policy | 5.4 Responsabilità del management |
| Clausola 6.2 Obiettivi per la sicurezza delle informazioni | 5.19 Sicurezza delle informazioni nelle relazioni con i fornitori |
| Clausola 7.3 Consapevolezza | 5.20 Trattamento della sicurezza delle informazioni negli accordi con i fornitori |
| Clausola 8.1 Pianificazione e controllo operativi | 5.21 Gestione della sicurezza delle informazioni nella catena di fornitura ICT |
| | 5.22 Monitoraggio, revisione e gestione dei cambiamenti dei servizi dei fornitori |
| | **5.23 Sicurezza delle informazioni per l'utilizzo dei servizi cloud** |
| | 5.36 Conformità a policy, regole e standard |
| | 6.3 Sensibilizzazione, istruzione e formazione sulla sicurezza delle informazioni |
| | 6.4 Processo disciplinare |
| | 8.30 Sviluppo in outsourcing |

**Quadro normativo e legale**:

| Quadro di riferimento | Rilevanza |
|-----------------------|-----------|
| nLPD svizzera (revDSG) | Art. 9 — Accordi con i responsabili del trattamento e requisiti per i sub-responsabili |
| OPDo svizzera (Ordinanza sulla protezione dei dati) | Allegato 1 — Elenco dei paesi adeguati per i trasferimenti transfrontalieri |
| GDPR UE (ove applicabile) | Art. 28 — Obblighi del responsabile del trattamento; Art. 44–50 — Trasferimenti internazionali |
| Swiss-U.S. Data Privacy Framework | Meccanismo di adeguatezza per i trasferimenti verso organizzazioni statunitensi certificate |
| ISO/IEC 27001:2022 | Controlli Annex A 5.19–5.23 |
| ISO/IEC 27002:2022 | Sezioni 5.19–5.23 — Linee guida per l'implementazione |
| ISO/IEC 27017:2026 | Controlli di sicurezza del cloud (informativo) |
| ISO/IEC 27018:2025 | Linee guida per la protezione dei dati personali nel cloud (informativo) |

---

<!-- QA_VERIFIED: 2026-04-03 -->
