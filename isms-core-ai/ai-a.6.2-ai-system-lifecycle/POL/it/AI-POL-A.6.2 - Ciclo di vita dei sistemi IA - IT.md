<!-- ISMS-CORE:POLICY:AI-POL-A.6.2-IT:ai:POL:a.6.2 -->
**AI-POL-A.6.2 — Ciclo di vita dei sistemi IA**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Ciclo di vita dei sistemi IA |
| **Tipo di documento** | Politica |
| **ID del documento** | AI-POL-A.6.2 |
| **Autore del documento** | Responsabile della Governance IA (RGIA) / Direttore Tecnico (DT) |
| **Proprietario del documento** | Amministratore Delegato (AD) |
| **Approvato da** | Direzione generale |
| **Data di creazione** | [Data da definire] |
| **Versione** | 1.0 |
| **Data versione** | [Data da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |
| **Versione prodotto AIMS** | 1.0 |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data da definire] | RGIA / DT | Politica iniziale per la prima certificazione ISO/IEC 42001:2023 |

**Ciclo di revisione**: Annuale (o in caso di variazioni significative nelle pratiche di sviluppo e operatività IA)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (RGIA)
- Secondaria: Direttore Tecnico (DT) / Responsabile IA Engineering
- Conformità: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-00 (Quadro di applicabilità normativa IA)
- AI-POL-A.6.1 (Governance dello sviluppo IA — obiettivi e processi pre-ciclo di vita)
- AI-POL-A.7.2-6 (Dati per i sistemi IA)
- AI-POL-A.5.2-5 (Valutazione d'impatto dei sistemi IA — la VISIA deve precedere il dispiegamento)
- AI-IMP-A.6.2-UG (Ciclo di vita dei sistemi IA — Guida utente)
- AI-IMP-A.6.2-TG (Ciclo di vita dei sistemi IA — Guida tecnica)
- ISO/IEC 42001:2023 Controlli A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8
- ISO/IEC 42001:2023 Allegato B.6.2 (Linee guida di attuazione — Ciclo di vita del sistema IA)

---

## Sintesi esecutiva

La presente politica stabilisce i requisiti dell'[Organizzazione] per il ciclo di vita dei sistemi IA — che comprende specifica, documentazione della progettazione e dello sviluppo, verifica e validazione, dispiegamento, esercizio e monitoraggio, documentazione tecnica e registrazione degli eventi — in conformità con i Controlli A.6.2.2–A.6.2.8 della norma ISO/IEC 42001:2023.

**Ambito**: Tutti i sistemi IA nell'ambito dell'AIMS in tutte le fasi del ciclo di vita, dalla specifica alla dismissione. I controlli si applicano ai fornitori IA (in via prioritaria) e ai deployer IA dove questi esercitano un'influenza significativa sulla gestione del ciclo di vita.

**Scopo**: Definire COSA deve essere documentato e controllato in ciascuna fase del ciclo di vita, CHI è responsabile e QUANDO si applicano i controlli. I dettagli di attuazione sono in AI-IMP-A.6.2-UG e AI-IMP-A.6.2-TG.

**Motivazione dei controlli combinati**: A.6.2.2–A.6.2.8 corrispondono direttamente alle fasi del ciclo di vita del sistema IA. Ogni controllo regola una fase distinta: specifica → documentazione progettazione/sviluppo → verifica/validazione → dispiegamento → esercizio/monitoraggio → documentazione tecnica → registrazione degli eventi. Questi sette controlli sono interdipendenti — ogni fase produce output da cui dipende la fase successiva.

---

## Ambito e applicabilità

### Dichiarazioni dei controlli ISO/IEC 42001:2023

**Controllo A.6.2.2 — Requisiti e specifica del sistema IA**
L'organizzazione deve specificare e documentare i requisiti per nuovi sistemi IA o per miglioramenti rilevanti ai sistemi esistenti.

**Controllo A.6.2.3 — Documentazione della progettazione e dello sviluppo del sistema IA**
L'organizzazione deve documentare la progettazione e lo sviluppo del sistema IA sulla base degli obiettivi organizzativi, dei requisiti documentati e dei criteri di specifica.

**Controllo A.6.2.4 — Verifica e validazione del sistema IA**
L'organizzazione deve definire e documentare le misure di verifica e validazione per il sistema IA e specificare i criteri per il loro utilizzo.

**Controllo A.6.2.5 — Dispiegamento del sistema IA**
L'organizzazione deve documentare un piano di dispiegamento e garantire che i requisiti appropriati siano soddisfatti prima del dispiegamento.

**Controllo A.6.2.6 — Esercizio e monitoraggio del sistema IA**
L'organizzazione deve definire e documentare gli elementi necessari per il funzionamento continuo del sistema IA. Come minimo, ciò deve includere il monitoraggio del sistema e delle prestazioni, le riparazioni, gli aggiornamenti e il supporto.

**Controllo A.6.2.7 — Documentazione tecnica del sistema IA**
L'organizzazione deve determinare quale documentazione tecnica del sistema IA è necessaria per ciascuna categoria rilevante di parti interessate, quali utenti, partner, autorità di supervisione, e fornire la documentazione tecnica nella forma appropriata.

**Controllo A.6.2.8 — Registrazione dei log degli eventi del sistema IA**
L'organizzazione deve determinare in quali fasi del ciclo di vita del sistema IA la tenuta dei log degli eventi deve essere attivata, ma come minimo quando il sistema IA è in uso.

### Quadro normativo

**Livello 1: Conformità obbligatoria** (per AI-POL-00):

- **Regolamento IA UE (Regolamento 2024/1689)**: Articolo 11 (documentazione tecnica), Articolo 12 (tenuta dei registri e registrazione), Articolo 13 (trasparenza e fornitura di informazioni), Articolo 14 (supervisione umana), Articolo 15 (accuratezza, robustezza, cybersicurezza), Articolo 17 (SGQ — tutte le fasi del ciclo di vita)

**Livello 2: Condizionale** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controlli A.6.2.2–A.6.2.8 — applicabile se la certificazione AIMS rientra nell'ambito o è richiesta contrattualmente

---

## Dichiarazioni di politica: Requisiti e specifica (A.6.2.2)

### Requisito di specifica del sistema IA

L'[Organizzazione] DEVE specificare e documentare i requisiti per ogni nuovo sistema IA e per qualsiasi miglioramento rilevante dei sistemi esistenti, prima dell'inizio dello sviluppo o del miglioramento.

### Requisiti per il documento di specifica

La specifica del sistema IA deve documentare:

| Elemento | Contenuto richiesto |
|---------|---------------------|
| **Finalità prevista** | Dichiarazione chiara di cosa il sistema IA è progettato per fare, per chi e in quale contesto |
| **Requisiti funzionali** | Cosa il sistema deve fare (input, output, tipi di decisioni, aspettative di prestazione) |
| **Requisiti non funzionali** | Affidabilità, disponibilità, tempo di risposta, scalabilità, sicurezza |
| **Requisiti di IA responsabile** | Metriche e soglie di equità; livello di spiegabilità; meccanismi di supervisione umana; derivati dalla VISIA e dagli obiettivi di AI-POL-A.6.1 |
| **Condizioni operative** | Condizioni in cui il sistema IA dovrebbe funzionare correttamente (ipotesi sulla distribuzione dei dati, condizioni ambientali) |
| **Usi fuori ambito** | Usi esplicitamente documentati per i quali il sistema NON è progettato o validato |
| **Parti interessate** | Parti interne ed esterne che interagiranno con il sistema o ne saranno influenzate |
| **Vincoli normativi** | Classificazione del rischio del Regolamento IA UE; trigger RGPD Articolo 22; altri obblighi applicabili |
| **Requisiti di integrazione** | Come il sistema IA si integra con i sistemi e i processi esistenti |

**Miglioramento rilevante** è definito come qualsiasi modifica che: modifica gli output del sistema IA in modo rilevante; introduce il sistema a una nuova popolazione; cambia il contesto operativo o la finalità prevista; o modifica l'architettura del modello, i dati di addestramento o gli iperparametri chiave.

---

## Dichiarazioni di politica: Documentazione della progettazione e dello sviluppo (A.6.2.3)

### Requisito di documentazione della progettazione e dello sviluppo

L'[Organizzazione] DEVE documentare la progettazione e lo sviluppo del sistema IA, garantendo che la documentazione sia tracciabile alla specifica e agli obiettivi di IA responsabile.

### Documentazione richiesta

| Documentazione | Contenuto |
|---------------|-----------|
| **Documentazione dell'architettura** | Architettura di sistema ad alto livello; diagramma dei componenti; flusso di dati; punti di integrazione |
| **Documentazione del modello** | Motivazione della scelta dell'algoritmo; architettura del modello; approccio di addestramento; scelte degli iperparametri |
| **Documentazione dei dati di addestramento** | Dataset utilizzati; fasi di pre-elaborazione; metodologia di suddivisione dei dati; collegamento ai record di dati A.7 |
| **Registro delle decisioni di progettazione** | Decisioni di progettazione chiave con motivazione; compromessi effettuati; alternative considerate |
| **Decisioni di progettazione per l'IA responsabile** | Come i requisiti di equità, trasparenza e sicurezza sono stati affrontati nella progettazione |
| **Cronologia delle versioni** | Tutte le versioni del modello con modifiche documentate; informazioni sulla riproducibilità |

La documentazione deve essere versionata e collegata alla versione del sistema IA che descrive.

---

## Dichiarazioni di politica: Verifica e validazione (A.6.2.4)

### Requisito di V&V

L'[Organizzazione] DEVE definire e documentare le misure di verifica e validazione per ciascun sistema IA prima del dispiegamento, e specificare i criteri che devono essere soddisfatti per l'autorizzazione al dispiegamento.

### Verifica

La verifica conferma che il sistema IA è stato costruito correttamente secondo le specifiche:

- Test funzionali rispetto ai requisiti della specifica
- Test di prestazione (accuratezza, precision/recall o metriche specifiche al compito) rispetto alle soglie definite
- Test di sicurezza — test di input adversarial, valutazione della robustezza del modello
- Test di integrazione nell'ambiente di staging

### Validazione

La validazione conferma che il sistema IA risolve il problema corretto ed è adatto all'uso previsto:

- Validazione dell'IA responsabile — metriche di equità valutate rispetto alle soglie approvate; spiegabilità validata per il pubblico di riferimento
- Validazione dell'uso previsto — test con condizioni reali e casi limite
- Test out-of-distribution — comportamento documentato quando gli input si trovano al di fuori della distribuzione di addestramento
- Validazione della supervisione umana — i meccanismi di override funzionano correttamente; soglie di allerta calibrate

### Criteri di dispiegamento

Ogni sistema IA deve avere criteri documentati che devono essere soddisfatti prima dell'autorizzazione al dispiegamento. Il RGIA deve convalidare il completamento della V&V rispetto ai criteri. Un sistema che non soddisfa i criteri di V&V non deve essere dispiegato.

---

## Dichiarazioni di politica: Dispiegamento (A.6.2.5)

### Requisito del piano di dispiegamento

L'[Organizzazione] DEVE documentare un piano di dispiegamento per ciascun sistema IA e garantire che tutti i requisiti pre-dispiegamento siano soddisfatti prima del dispiegamento operativo.

### Contenuto del piano di dispiegamento

| Elemento | Contenuto richiesto |
|---------|---------------------|
| **Ambito del dispiegamento** | Quali ambienti, popolazioni di utenti e casi d'uso sono coperti in questo dispiegamento |
| **Checklist pre-dispiegamento** | Tutti i requisiti che devono essere confermati prima del dispiegamento (VISIA approvata, V&V superata, documentazione tecnica pronta, supervisione umana implementata, registrazione attivata) |
| **Approccio al rollout** | Rollout graduale / shadow mode / dispiegamento completo — con motivazione |
| **Procedura di rollback** | Come tornare allo stato precedente se il dispiegamento causa problemi inattesi |
| **Attivazione del monitoraggio** | Come il monitoraggio operativo (A.6.2.6) viene attivato al momento del dispiegamento |
| **Comunicazione alle parti interessate** | Chi deve essere informato del dispiegamento e come |
| **Autorizzazione al dispiegamento** | Autorizzatore nominato (il RGIA deve approvare) e data di autorizzazione |

**Gate di deployment**: Nessun sistema IA può essere dispiegato senza l'approvazione documentata del RGIA che confermi che tutti i requisiti pre-dispiegamento sono soddisfatti, inclusa una VISIA aggiornata.

---

## Dichiarazioni di politica: Esercizio e monitoraggio (A.6.2.6)

### Requisito di monitoraggio operativo

L'[Organizzazione] DEVE definire e documentare gli elementi necessari per il funzionamento e il monitoraggio continui di ciascun sistema IA nell'ambito.

### Elementi di monitoraggio obbligatori

**Monitoraggio delle prestazioni**:

- Indicatori chiave di prestazione (KPI) definiti nella fase di specifica (A.6.2.2)
- Frequenza di monitoraggio appropriata al caso d'uso (continua / giornaliera / settimanale)
- Soglie di degradazione delle prestazioni — quando le prestazioni scendono sotto la soglia, viene attivato un avviso
- Rilevamento della deriva del modello — monitoraggio statistico della distribuzione dei dati di input e della distribuzione degli output

**Monitoraggio dell'IA responsabile**:

- Monitoraggio dell'equità — metriche di equità misurate in produzione secondo un calendario definito
- Rilevamento dei bias — monitoraggio dell'emergenza di bias in produzione non presente alla V&V
- Efficacia della supervisione umana — i meccanismi di override vengono utilizzati in modo appropriato?
- Conformità all'ambito — il sistema IA viene utilizzato solo per le finalità previste documentate?

**Monitoraggio operativo**:

- Disponibilità e uptime del sistema
- Tempo di risposta e throughput
- Tassi di errore e modi di guasto
- Stato dell'infrastruttura (collegato ad A.4.5)

**Allarmi per incidenti**:

- Condizioni di allarme definite per ciascuna dimensione di monitoraggio
- Percorso di escalation dall'allarme automatizzato al Proprietario del sistema IA fino al Responsabile rischi IA
- Integrazione con il processo di risposta agli incidenti IA (AI-POL-A.8.2-5)

### Documentazione del monitoraggio

Il piano di monitoraggio per ciascun sistema IA deve essere documentato prima del dispiegamento, coprendo tutti gli elementi di monitoraggio obbligatori con:

- Cosa viene monitorato
- Come viene monitorato (strumento, metodo)
- Frequenza
- Soglie di allarme
- Percorso di escalation in caso di superamento delle soglie

---

## Dichiarazioni di politica: Documentazione tecnica (A.6.2.7)

### Requisito di documentazione tecnica

L'[Organizzazione] DEVE determinare quale documentazione tecnica è necessaria per ciascuna categoria rilevante di parti interessate e fornirla nella forma appropriata.

### Categorie di parti interessate e requisiti di documentazione

| Parte interessata | Documentazione richiesta |
|------------------|-------------------------|
| **Operatori / utenti interni** | Guida utente; specifica dell'uso previsto; limitazioni; procedure operative; meccanismi di override |
| **Proprietario sistema IA / Governance** | Specifica tecnica completa; model card; rapporto di V&V; sintesi VISIA; piano di monitoraggio |
| **IT / Infrastruttura** | Architettura del sistema; documentazione di integrazione; requisiti infrastrutturali; runbook di dispiegamento |
| **Autorità di regolamentazione** | Documentazione tecnica del Regolamento IA UE (Articolo 11 per l'IA ad alto rischio); sintesi VISIA; documentazione della valutazione di conformità |
| **Clienti / partner** | Descrizione delle capacità; limitazioni; avviso di trasparenza (A.8.2); meccanismo di segnalazione degli incidenti (A.8.3) |
| **Auditor (interni/esterni)** | Insieme completo di documentazione; prove di V&V; VISIA; riferimento DDA |

La documentazione tecnica deve essere versionata, collegata alla versione del sistema IA che descrive e rivista a ogni modifica rilevante.

---

## Dichiarazioni di politica: Registrazione degli eventi (A.6.2.8)

### Requisito di registrazione degli eventi

L'[Organizzazione] DEVE determinare in quali fasi del ciclo di vita del sistema IA la registrazione degli eventi deve essere attivata. Come minimo, la registrazione deve essere attiva quando il sistema IA è in uso operativo.

### Fasi di registrazione obbligatorie

| Fase del ciclo di vita | Requisito di registrazione |
|----------------------|---------------------------|
| **Uso operativo** | OBBLIGATORIA — tutte le interazioni, gli input, gli output e le decisioni del sistema IA devono essere registrati |
| **Validazione e test** | Richiesta — input di test, output e risultati di valutazione registrati per la tracciabilità |
| **Dispiegamento** | Richiesta — evento di dispiegamento, versione, autorizzatore, timestamp |
| **Allarmi di monitoraggio** | Richiesta — tutti i superamenti di soglia e gli eventi di allarme |
| **Incidenti** | Richiesta — tutti gli eventi di incidente IA per la revisione post-incidente |
| **Sviluppo** | Best practice — cicli di addestramento del modello, set di iperparametri, metriche di valutazione |

### Requisiti per il contenuto dei log

Per i log operativi del sistema IA, ogni record di evento deve includere almeno:

- Timestamp (UTC)
- Identificativo e versione del sistema IA
- Riepilogo degli input (o hash degli input quando la registrazione completa degli input è vietata da obblighi di protezione dei dati)
- Output o decisione prodotta
- Qualsiasi override umano applicato
- Identificativo utente o di sessione (ove applicabile e consentito)

### Conservazione dei log

I log degli eventi dei sistemi IA devono essere conservati per:

- La durata della vita operativa del sistema IA, PIÙ
- Almeno 3 anni dopo la dismissione (da prolungare se il Regolamento IA UE o le normative settoriali richiedono periodi più lunghi)

### Protezione dei log

I log degli eventi dei sistemi IA costituiscono prove di audit. Devono essere:

- Protetti contro modifiche o cancellazioni (immutabili o solo in aggiunta ove fattibile)
- Sottoposti a controllo degli accessi (sola lettura per gli auditor; accesso in scrittura limitato per la gestione dei log)
- Sottoposti a backup conformemente ai requisiti ISMS

---

## Dichiarazioni di politica: Dismissione

### Requisito di dismissione

L'[Organizzazione] DEVE gestire il fine vita pianificato dei sistemi IA in modo controllato, preservando le prove, proteggendo gli interessati e garantendo che non si verifichino danni residui dai sistemi dismessi.

### Condizioni che attivano la dismissione

Un processo di dismissione del sistema IA deve essere avviato quando:

- Il sistema IA viene ritirato definitivamente dall'uso operativo
- Un sistema sostitutivo viene dispiegato e il sistema esistente viene ritirato
- La VISIA del sistema IA identifica rischi che non possono essere adeguatamente mitigati
- Il caso d'uso previsto viene abbandonato
- Una modifica rilevante richiederebbe una rivalutazione completa che il sistema non è in grado di soddisfare

### Processo di dismissione

Il Proprietario del sistema IA deve eseguire un piano di dismissione documentato, approvato dal RGIA, che copra:

| Fase | Requisito |
|------|-----------|
| **Notifica agli utenti** | Notificare tutti gli utenti e le parti interessate della data di dismissione pianificata con un preavviso adeguato (minimo 30 giorni per i sistemi operativi; in base agli obblighi contrattuali per i sistemi rivolti ai clienti) |
| **Destinazione dei dati** | Definire la sorte di tutti i dati di addestramento, operativi e di output: cancellazione, archiviazione o trasferimento — documentato secondo i requisiti del ciclo di vita dei dati RGPD |
| **Eliminazione del modello** | Confermare la cancellazione dei pesi del modello e degli artefatti associati da tutti gli ambienti (produzione, staging, backup) o documentare la motivazione per la conservazione |
| **Revoca degli accessi** | Revocare tutti gli accessi utente e API al sistema prima o alla dismissione |
| **Conservazione dei log** | Conservare i log degli eventi per almeno 3 anni dopo la dismissione o come richiesto dalla normativa applicabile |
| **Chiusura della VISIA** | Chiudere la VISIA con un registro di dismissione, annotando il metodo di smaltimento e confermando che i rischi in sospeso sono stati risolti |
| **Registro Regolamento IA UE** | Dove il sistema era registrato nel database del Regolamento IA UE, aggiornare lo stato di registrazione a «dismesso» |
| **Notifica a terze parti** | Notificare le terze parti pertinenti (fornitori di componenti IA, responsabili del trattamento dei dati) della dismissione e ottenere conferma della cancellazione dei dati ove richiesto |

### Requisiti probatori per la dismissione

Il RGIA deve conservare un **Registro di dismissione** per sistema che include: identità del sistema, data di dismissione, metodo di smaltimento per dati e artefatti del modello, conferma della notifica agli utenti e chiusura della VISIA.

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RGIA** | Approvazione del dispiegamento (tutte le fasi); proprietario della politica del ciclo di vita; revisione dei rapporti di monitoraggio; approvazione della documentazione tecnica per le autorità di regolamentazione; approvazione dei piani di dismissione |
| **DT / Responsabile IA Engineering** | Proprietario della specifica A.6.2.2, della documentazione A.6.2.3, dei processi V&V A.6.2.4; garanzia che le pratiche di engineering soddisfino la politica |
| **Proprietario del sistema IA** | Manutenzione di tutta la documentazione del ciclo di vita per i sistemi di propria competenza; proprietario del piano di monitoraggio; risposta agli allarmi di monitoraggio |
| **RSSI** | Revisione delle dimensioni di sicurezza della V&V (A.6.2.4), del monitoraggio (A.6.2.6) e della registrazione (A.6.2.8) |
| **Responsabile rischi IA** | Accettazione dei rischi residui identificati dalla V&V; approvazione dell'accettazione dei rischi al dispiegamento |

---

## Requisiti probatori

| Evidenza | Descrizione | Conservazione |
|----------|-------------|---------------|
| Specifica del sistema IA | Requisiti documentati per versione del sistema IA | Durata del sistema + 3 anni |
| Documentazione progettazione e sviluppo | Architettura, modello, addestramento, registro delle decisioni | Durata del sistema + 3 anni |
| Registri di V&V | Piani di test, risultati dei test, superato/non superato dei criteri di dispiegamento | Durata del sistema + 3 anni |
| Piano e autorizzazione di dispiegamento | Piano di dispiegamento con approvazione del RGIA | Durata del sistema + 3 anni |
| Piano di monitoraggio | Piano di monitoraggio documentato con soglie | Durata del sistema + 3 anni |
| Documentazione tecnica | Documentazione versionata per categoria di parti interessate | Durata del sistema + 3 anni |
| Log degli eventi | Log operativi del sistema IA | Durata del sistema + 3 anni post-dismissione |
| Registri di dismissione | Metodo di smaltimento, conferma cancellazione dati, chiusura VISIA, notifica utenti | 5 anni post-dismissione |

---

## Considerazioni per l'audit

Gli auditor che verificano la conformità con A.6.2.2–A.6.2.8 dovranno trovare:

- Documenti di specifica per tutti i sistemi IA nell'ambito, precedenti allo sviluppo
- Documentazione di progettazione e sviluppo tracciabile alle specifiche
- Rapporti di V&V con criteri di dispiegamento documentati e risultati superato/non superato
- Registri di autorizzazione al dispiegamento con convalida del RGIA
- Piani di monitoraggio attivi con configurazioni degli allarmi
- Documentazione tecnica disponibile per ciascuna categoria di parti interessate
- Registrazione attiva degli eventi nell'uso operativo, con politica di conservazione documentata
- Registri di dismissione per i sistemi IA ritirati, inclusa la conferma dello smaltimento di dati/modelli e la chiusura della VISIA

---

<!-- QA_VERIFIED: 2026-04-15 -->
