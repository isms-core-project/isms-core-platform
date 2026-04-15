<!-- ISMS-CORE:POLICY:AI-POL-A.7.2-6-IT:ai:POL:a.7.2-6 -->
**AI-POL-A.7.2-6 — Dati per i sistemi IA**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Dati per i sistemi IA |
| **Tipo di documento** | Politica |
| **ID del documento** | AI-POL-A.7.2-6 |
| **Autore del documento** | Responsabile della Governance IA (RGIA) / Responsabile governance dei dati |
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
| 1.0 | [Data da definire] | RGIA / Responsabile governance dei dati | Politica iniziale per la prima certificazione ISO/IEC 42001:2023 |

**Ciclo di revisione**: Annuale (o in caso di variazioni significative nelle pratiche relative ai dati IA o nelle normative applicabili)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (RGIA)
- Secondaria: Responsabile governance dei dati / Chief Data Officer
- Conformità: Legale / Responsabile della protezione dei dati (DPD)
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-00 (Quadro di applicabilità normativa IA)
- AI-POL-A.4.2-6 (Risorse dei sistemi IA — documentazione delle risorse di dati)
- AI-POL-A.6.2 (Ciclo di vita dei sistemi IA — dati utilizzati nello sviluppo e nell'esercizio)
- AI-IMP-A.7.2-6-UG (Dati per i sistemi IA — Guida utente)
- AI-IMP-A.7.2-6-TG (Dati per i sistemi IA — Guida tecnica)
- PRIV-POL-00 (Applicabilità normativa in materia di privacy — per i dati IA contenenti dati personali)
- ISO/IEC 42001:2023 Controlli A.7.2, A.7.3, A.7.4, A.7.5, A.7.6
- ISO/IEC 42001:2023 Allegato B.7 (Linee guida di attuazione — Dati per i sistemi IA)

---

## Sintesi esecutiva

La presente politica stabilisce i requisiti dell'[Organizzazione] per la gestione dei dati nel corso dell'intero ciclo di vita dei sistemi IA — che comprende processi di gestione dei dati, acquisizione e selezione dei dati, qualità dei dati, provenienza dei dati e preparazione dei dati — in conformità con i Controlli A.7.2–A.7.6 della norma ISO/IEC 42001:2023.

**Ambito**: Tutti i dati utilizzati nello sviluppo, nell'addestramento, nella validazione, nel test e nell'esercizio dei sistemi IA nell'ambito dell'AIMS.

**Nota sulla privacy**: Quando i dati IA contengono o derivano da dati personali, la presente politica opera congiuntamente a PRIV-POL-00 e alla suite di controlli PIMS. Il RGPD Articolo 5 (minimizzazione dei dati, limitazione delle finalità per i dati di addestramento IA contenenti dati personali) e l'Articolo 25 (protezione dei dati fin dalla progettazione) si applicano in aggiunta ai requisiti della presente politica.

**Scopo**: Definire QUALI requisiti di governance dei dati si applicano ai sistemi IA, CHI è responsabile e QUANDO i processi di governance dei dati devono essere applicati. L'attuazione è descritta in AI-IMP-A.7.2-6-UG e AI-IMP-A.7.2-6-TG.

**Motivazione dei controlli combinati**: A.7.2–A.7.6 formano il quadro di governance dei dati per l'IA. La gestione dei dati (A.7.2) stabilisce i requisiti di processo generali; l'acquisizione (A.7.3) regola come i dati entrano nella pipeline IA; la qualità (A.7.4) fissa gli standard che i dati devono soddisfare; la provenienza (A.7.5) garantisce che l'origine e i diritti sui dati siano tracciati; la preparazione (A.7.6) regola la trasformazione dei dati grezzi in forma pronta per il modello.

---

## Ambito e applicabilità

### Dichiarazioni dei controlli ISO/IEC 42001:2023

**Controllo A.7.2 — Dati per lo sviluppo e il miglioramento del sistema IA**
L'organizzazione deve definire, documentare e attuare processi di gestione dei dati relativi allo sviluppo dei sistemi IA.

**Controllo A.7.3 — Acquisizione dei dati**
L'organizzazione deve determinare e documentare i dettagli relativi all'acquisizione e alla selezione dei dati utilizzati nei sistemi IA.

**Controllo A.7.4 — Qualità dei dati per i sistemi IA**
L'organizzazione deve definire e documentare i requisiti di qualità dei dati e garantire che i dati utilizzati per sviluppare e gestire il sistema IA soddisfino tali requisiti.

**Controllo A.7.5 — Provenienza dei dati**
L'organizzazione deve definire e documentare un processo per la registrazione della provenienza dei dati utilizzati nei suoi sistemi IA nel corso dei cicli di vita dei dati e del sistema IA.

**Controllo A.7.6 — Preparazione dei dati**
L'organizzazione deve definire e documentare i criteri per la selezione degli approcci di preparazione dei dati e i metodi di preparazione dei dati da utilizzare.

### Quadro normativo

**Livello 1: Conformità obbligatoria** (per AI-POL-00):

- **Regolamento IA UE (Regolamento 2024/1689)**: Articolo 10 — requisiti di governance dei dati per i dati di addestramento IA ad alto rischio (criteri di qualità, rappresentatività, assenza di errori e bias, pratiche di governance dei dati); Articolo 11 — la documentazione tecnica deve includere una descrizione dei dati di addestramento
- **RGPD**: Articolo 5 (limitazione delle finalità, minimizzazione dei dati per i dati di addestramento IA contenenti dati personali); Articolo 25 (protezione dei dati fin dalla progettazione); Articolo 35 (DPIA quando il trattamento dei dati IA pone un rischio elevato)

**Livello 2: Condizionale** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controlli A.7.2–A.7.6 — applicabile se la certificazione AIMS rientra nell'ambito o è richiesta contrattualmente

---

## Dichiarazioni di politica: Processi di gestione dei dati (A.7.2)

### Requisito del quadro di gestione dei dati

L'[Organizzazione] DEVE definire, documentare e attuare processi di gestione dei dati che regolino tutti i dati utilizzati nello sviluppo e nel miglioramento dei sistemi IA. Questi processi devono essere integrati nel ciclo di vita dello sviluppo IA (AI-POL-A.6.2) e devono coprire l'intero ciclo di vita dei dati dall'acquisizione alla cancellazione.

### Governance del ciclo di vita dei dati IA

I processi di gestione dei dati devono coprire ogni fase del ciclo di vita dei dati:

| Fase | Requisito di governance |
|------|------------------------|
| **Acquisizione** | Criteri di acquisizione documentati e processo di approvazione (A.7.3) |
| **Ingestione** | Intake sotto controllo di versione con registrazione della provenienza (A.7.5) |
| **Valutazione della qualità** | Criteri di qualità applicati prima dell'utilizzo (A.7.4) |
| **Preparazione** | Metodologia di preparazione documentata (A.7.6) |
| **Archiviazione** | Controlli degli accessi, cifratura, backup secondo ISMS |
| **Utilizzo in addestramento / validazione / esercizio** | Collegamento di versioni — quale versione del dataset è stata utilizzata in quale versione del modello |
| **Aggiornamento / re-addestramento** | Criteri di trigger per gli aggiornamenti del dataset e il re-addestramento |
| **Archiviazione a lungo termine** | Cosa conservare, per quanto tempo e in quale formato |
| **Cancellazione** | Criteri e processo per la cancellazione sicura; collegamento a PRIV-POL-00 dove sono coinvolti dati personali |

---

## Dichiarazioni di politica: Acquisizione e selezione dei dati (A.7.3)

### Requisito di acquisizione dei dati

L'[Organizzazione] DEVE determinare e documentare i dettagli dell'acquisizione e della selezione dei dati per ciascun sistema IA. Nessun dato può entrare nella pipeline di sviluppo IA senza l'approvazione documentata dell'acquisizione.

### Documentazione dell'acquisizione dei dati

Per ogni dataset acquisito per uso IA:

| Campo | Contenuto richiesto |
|-------|---------------------|
| Identificativo del dataset | Nome univoco e versione |
| Fonte | Origine dei dati (sistema interno, dataset pubblico, dataset su licenza, raccolta commissionata, web scraping, altro) |
| Metodo di acquisizione | Come i dati sono stati ottenuti |
| Base giuridica / licenza | Licenza con cui i dati vengono utilizzati; conferma di proprietà; per i dati personali: base giuridica ai sensi del RGPD |
| Uso previsto | Per quali sistemi IA e fase/i del ciclo di vita i dati sono destinati |
| Ambito e copertura | Cosa i dati rappresentano; cosa non rappresentano |
| Data di acquisizione | Quando i dati sono stati ottenuti |
| Approvatore responsabile | Approvazione del Responsabile governance dei dati per l'acquisizione |

### Fonti di dati vietate

Le seguenti fonti NON devono essere utilizzate come dati di addestramento o operativi IA senza esplicita approvazione documentata del RGIA e dell'Ufficio Legale:

- Dati ottenuti tramite web scraping quando i termini di servizio del sito web vietano tale utilizzo
- Dati contenenti dati personali senza una base giuridica documentata ai sensi del RGPD
- Dati sintetici in cui il metodo di generazione introduce bias sistematici senza misure di mitigazione documentate
- Dati i cui diritti di proprietà intellettuale sono incerti o controversi
- Dati la cui provenienza non può essere stabilita

---

## Dichiarazioni di politica: Qualità dei dati (A.7.4)

### Requisito di qualità dei dati

L'[Organizzazione] DEVE definire e documentare i requisiti di qualità dei dati per ciascun sistema IA e verificare che i dati soddisfino tali requisiti prima dell'utilizzo in addestramento, validazione o esercizio.

### Dimensioni della qualità dei dati

I criteri di qualità devono essere definiti secondo le seguenti dimensioni per ciascun dataset:

| Dimensione | Definizione | Metodo di valutazione |
|------------|------------|----------------------|
| **Completezza** | Quale proporzione di campi o record richiesti è presente | Controllo statistico di completezza |
| **Accuratezza** | Grado in cui i dati rappresentano correttamente l'entità reale che descrivono | Campionamento e validazione rispetto alla ground truth |
| **Rappresentatività** | Grado in cui i dati rappresentano la popolazione di dispiegamento attraverso le dimensioni demografiche rilevanti | Analisi della distribuzione; valutazione della copertura demografica |
| **Attualità** | I dati sono sufficientemente recenti per il caso d'uso; la deriva temporale viene valutata | Analisi della distribuzione temporale |
| **Coerenza** | I dati sono coerenti tra le fonti e nel tempo | Validazione incrociata tra fonti; controlli di coerenza |
| **Assenza di bias nocivi** | I dati non contengono bias sistematici che produrrebbero output IA iniqui | Analisi dei bias sulle caratteristiche protette |
| **Qualità delle etichette** (per l'apprendimento supervisionato) | Le etichette sono accurate, coerenti e prodotte da annotatori qualificati | Accordo inter-annotatori; audit delle etichette |

### Gate di qualità

Ogni dataset deve essere valutato rispetto ai criteri di qualità definiti prima dell'utilizzo. I dataset che non soddisfano le soglie di qualità minime devono:

1. Essere rifiutati per l'utilizzo, OPPURE
2. Essere corretti (raccolta dati aggiuntiva, pulizia, augmentazione) con la correzione documentata, OPPURE
3. Essere utilizzati con accettazione del rischio documentata dal Responsabile rischi IA, con le limitazioni di qualità note annotate nella model card

Nessun dataset può essere utilizzato in un sistema IA senza risultati documentati di valutazione della qualità.

---

## Dichiarazioni di politica: Provenienza dei dati (A.7.5)

### Requisito di provenienza dei dati

L'[Organizzazione] DEVE definire e attuare un processo per la registrazione e il mantenimento della provenienza di tutti i dati utilizzati nei sistemi IA nel corso dei cicli di vita sia dei dati che del sistema IA.

### Requisiti per i registri di provenienza

Deve essere mantenuto un registro di provenienza dei dati per ciascun dataset, tracciando:

| Elemento | Contenuto |
|---------|-----------|
| Identificativo e versione del dataset | Riferimento univoco |
| Fonte originale | Da dove provengono i dati (con riferimento al registro di acquisizione) |
| Cronologia delle trasformazioni | Tutte le pulizie, normalizzazioni, augmentazioni o altre trasformazioni applicate — con date e parte responsabile |
| Dataset derivati | Se questo dataset è stato derivato da un altro, collegamento al registro di provenienza genitore |
| Sistemi IA che utilizzano questo dataset | Quali sistemi IA (e versioni di modello) hanno utilizzato questo dataset |
| Registro di conservazione e cancellazione | Quando i dati sono stati archiviati o cancellati e sotto quale autorità |

### Collegamento di versioni

Il sistema di provenienza deve consentire la tracciabilità: per qualsiasi versione di modello IA dispiegato, deve essere possibile identificare la/le versione/i esatta/e del dataset utilizzata/e nell'addestramento e nella validazione. Questa tracciabilità è richiesta per:

- Prove di audit e certificazione
- Indagine sugli incidenti (determinare se un problema dei dati ha contribuito a un incidente IA)
- Conformità normativa (documentazione tecnica Regolamento IA UE Articolo 11)
- Conformità al diritto alla cancellazione (RGPD Articolo 17 — identificare quali modelli sono stati addestrati su dati oggetto di una richiesta di cancellazione)

### RGPD Articolo 17 — Diritto alla cancellazione per i dati di addestramento IA

Quando un interessato presenta una richiesta di cancellazione valida ai sensi del RGPD Articolo 17, l'[Organizzazione] DEVE:

1. **Cancellare immediatamente il record dei dati di addestramento sorgente** — rimuovere i dati della persona da tutti i dataset di addestramento, set di validazione e archivi dati associati senza ingiustificato ritardo.
2. **Valutare il rischio residuo nei pesi del modello** — utilizzando la tracciabilità della provenienza, identificare tutte le versioni di modelli IA addestrate sui dati. Documentare una valutazione tecnica sulla possibilità di recuperare o attribuire i dati della persona ai pesi del modello addestrato. Per le architetture di reti neurali standard, la cancellazione completa dai pesi è generalmente tecnicamente non realizzabile; questa non realizzabilità deve essere documentata.
3. **Rispondere all'interessato** — accusare ricevuta della richiesta di cancellazione, confermare la cancellazione dei dati sorgente e, dove la cancellazione completa dai pesi del modello è tecnicamente non realizzabile, documentare questa limitazione e la valutazione del rischio residuo secondo le linee guida dell'Autorità di protezione dei dati applicabile.
4. **Attivare il re-addestramento o il ritiro del modello** — quando la valutazione del rischio residuo identifica una significativa probabilità di identificabilità della persona dagli output del modello (ad es. il modello è stato addestrato su un dataset piccolo, o la persona è un punto dati distintivo), il Proprietario del sistema IA deve valutare se è necessario un re-addestramento o un ritiro del modello. Il DPD deve fornire consulenza sulla soglia di rischio per questa determinazione.
5. **Registrare tutte le azioni di cancellazione** — registrare la richiesta, la conferma della cancellazione dei dati sorgente, la valutazione del modello e qualsiasi decisione di re-addestramento nel Registro di governance dei dati IA. Conservare i registri per 5 anni.

Dove l'[Organizzazione] utilizza tecniche di privacy differenziale durante l'addestramento, ciò deve essere documentato nella VISIA e referenziato nelle risposte alle cancellazioni come misura di mitigazione del rischio.

---

## Dichiarazioni di politica: Preparazione dei dati (A.7.6)

### Requisito di preparazione dei dati

L'[Organizzazione] DEVE definire e documentare i criteri per la selezione degli approcci di preparazione dei dati e i metodi da utilizzare. Le decisioni di preparazione dei dati devono essere documentate e riproducibili.

### Governance della preparazione dei dati

La preparazione dei dati — il processo di trasformazione dei dati grezzi in una forma adatta all'addestramento o all'esercizio del modello IA — deve essere:

**Documentata**: Ogni pipeline di preparazione deve essere documentata, includendo:
- Fasi di pre-elaborazione applicate (normalizzazione, codifica, imputation, tokenizzazione, ecc.)
- Decisioni di feature engineering con motivazione
- Criteri di filtraggio (record esclusi e perché)
- Metodi di augmentazione applicati (e i loro parametri)
- Strategia di campionamento dove i volumi di dati richiedono campionamento

**Sotto controllo di versione**: Gli script e le pipeline di preparazione dei dati devono essere versionati insieme al codice del modello, consentendo la riproduzione del dataset preparato esatto dalla sorgente grezza.

**Consapevole dei bias**: Le decisioni di preparazione dei dati devono essere esaminate per il loro potenziale di introdurre o amplificare bias. I passaggi che potrebbero influenzare in modo sproporzionato i gruppi sottorappresentati (ad es. sotto-campionamento, strategie di imputation) devono essere documentati con motivazione e valutazione dell'impatto sui bias.

**Governance degli annotatori** (per i dati etichettati):

- Le linee guida per l'annotazione devono essere documentate
- Le qualifiche degli annotatori documentate
- L'accordo inter-annotatori misurato e documentato
- La qualità delle etichette al di sotto delle soglie accettabili attiva la ri-annotazione

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RGIA** | Proprietario della politica di governance dei dati IA; approvazione dell'acquisizione dei dati per dataset ad alta sensibilità; revisione dei problemi di qualità dei dati escalati dal Responsabile governance dei dati |
| **Responsabile governance dei dati** | Proprietario e operatore quotidiano dei processi A.7.x; approvazione delle acquisizioni di dati standard; manutenzione dei registri di provenienza; presidio dei gate di qualità dei dati |
| **DPD / Responsabile della privacy** | Revisione dei dati IA contenenti dati personali; garanzia della conformità RGPD per i dati di addestramento; consulenza sulle implicazioni del diritto alla cancellazione |
| **Data Scientist / Ingegneri ML** | Conduzione delle valutazioni della qualità dei dati; documentazione delle pipeline di preparazione; segnalazione dei problemi di qualità al Responsabile governance dei dati |
| **Proprietario del sistema IA** | Garanzia che i registri di governance dei dati siano aggiornati per i sistemi IA di propria competenza |

---

## Requisiti probatori

| Evidenza | Descrizione | Conservazione |
|----------|-------------|---------------|
| Registri di acquisizione dei dati | Documentazione di acquisizione per dataset con base giuridica e approvazione | Durata di utilizzo del dataset + 5 anni |
| Registri di valutazione della qualità dei dati | Risultati della valutazione della qualità per dataset rispetto ai criteri definiti | Durata di utilizzo del dataset + 3 anni |
| Registri di provenienza dei dati | Cronologia delle trasformazioni e registri di collegamento delle versioni | Durata del sistema IA + 5 anni post-dismissione |
| Documentazione di preparazione dei dati | Documentazione della pipeline con riferimento al codice versionato | Durata del sistema IA + 3 anni |
| Risultati dei gate di qualità | Registri delle decisioni superato/non superato ai gate di qualità con approvazione | Durata del sistema IA + 3 anni |

---

## Considerazioni per l'audit

Gli auditor che verificano la conformità con A.7.2–A.7.6 dovranno trovare:

- Processi di gestione dei dati documentati che coprono l'intero ciclo di vita dei dati
- Registri di acquisizione per tutti i dataset utilizzati nei sistemi IA nell'ambito
- Criteri di qualità dei dati definiti per sistema IA e registri di valutazione della qualità che confermano il soddisfacimento dei criteri
- Registri di provenienza dei dati che consentono la tracciabilità dal modello dispiegato al dataset di addestramento
- Pipeline di preparazione dei dati documentate e sotto controllo di versione
- Prove che i gate di qualità dei dati vengono applicati prima che i dataset entrino in produzione

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
