<!-- ISMS-CORE:POLICY:AI-POL-A.6.1-IT:ai:POL:a.6.1 -->
**AI-POL-A.6.1 — Governance dello sviluppo IA**

---

## Controllo del documento

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Governance dello sviluppo IA |
| **Tipo di documento** | Politica |
| **ID del documento** | AI-POL-A.6.1 |
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

**Ciclo di revisione**: Annuale (o in caso di variazioni significative nella metodologia di sviluppo IA o negli standard di IA responsabile)
**Prossima data di revisione**: [Data di entrata in vigore + 12 mesi]

**Catena di approvazione**:

- Primaria: Responsabile della Governance IA (RGIA)
- Secondaria: Direttore Tecnico (DT) / Responsabile IA Engineering
- Conformità: Responsabile della Sicurezza dei Sistemi Informativi (RSSI)
- Autorità finale: Direzione generale

**Documenti correlati**:

- AI-POL-00 (Quadro di applicabilità normativa IA)
- AI-POL-01 (Quadro di governance e processo decisionale AIMS)
- AI-POL-A.5.2-5 (Valutazione d'impatto dei sistemi IA — la VISIA guida la selezione dei controlli)
- AI-POL-A.6.2 (Ciclo di vita dei sistemi IA — controlli del ciclo di vita operativo)
- AI-IMP-A.6.1-UG (Governance dello sviluppo IA — Guida utente)
- AI-IMP-A.6.1-TG (Governance dello sviluppo IA — Guida tecnica)
- ISO/IEC 42001:2023 Controlli A.6.1.2, A.6.1.3
- ISO/IEC 42001:2023 Allegato B.6.1 (Linee guida di attuazione — Governance dello sviluppo di sistemi IA)

---

## Sintesi esecutiva

La presente politica stabilisce i requisiti dell'[Organizzazione] per l'identificazione e l'integrazione di obiettivi di sviluppo responsabile e per la definizione e documentazione dei processi con cui i sistemi IA vengono progettati e sviluppati in modo responsabile — in conformità con i Controlli A.6.1.2 e A.6.1.3 della norma ISO/IEC 42001:2023.

**Ambito**: Tutti i sistemi IA sviluppati dall'[Organizzazione] (ruolo di fornitore IA); gli obiettivi, i processi e le pratiche di governance che guidano il ciclo di vita dello sviluppo dalla progettazione alla consegna per il dispiegamento.

**Nota di applicabilità**: I controlli A.6.1 si applicano principalmente alle organizzazioni che agiscono in qualità di **fornitori IA** — quelle che sviluppano, addestrano o creano in altro modo sistemi IA. Le organizzazioni che agiscono esclusivamente come deployer IA (che utilizzano IA di terze parti senza modifiche) devono documentarlo nella DDA AIMS e applicare A.6.1 dove esercitano un'influenza rilevante sulla progettazione o configurazione del sistema IA.

**Scopo**: Definire QUALI obiettivi di sviluppo responsabile devono essere stabiliti e documentati (A.6.1.2) e QUALI processi per la progettazione e lo sviluppo responsabile devono essere definiti (A.6.1.3). L'attuazione è descritta in AI-IMP-A.6.1-UG e AI-IMP-A.6.1-TG.

**Motivazione dei controlli combinati**: A.6.1.2 e A.6.1.3 formano il livello di governance strategica e di processo per lo sviluppo IA. Gli obiettivi (A.6.1.2) stabiliscono i principi di IA responsabile che devono essere integrati nel ciclo di sviluppo; i processi (A.6.1.3) definiscono COME questi principi vengono attuati operativamente. Entrambi i controlli devono essere applicati insieme per garantire una governance dello sviluppo efficace.

---

## Ambito e applicabilità

### Dichiarazioni dei controlli ISO/IEC 42001:2023

**Controllo A.6.1.2 — Obiettivi per lo sviluppo responsabile del sistema IA**
L'organizzazione deve identificare e documentare obiettivi per guidare lo sviluppo responsabile dei sistemi IA, e tenere conto di tali obiettivi e integrare misure per raggiungerli nel ciclo di vita dello sviluppo.

**Controllo A.6.1.3 — Processi per la progettazione e lo sviluppo responsabile del sistema IA**
L'organizzazione deve definire e documentare i processi specifici per la progettazione e lo sviluppo responsabile del sistema IA.

### Cosa copre la presente politica

- Obiettivi di sviluppo IA responsabile da stabilire per ciascun sistema IA
- Requisiti di processo per la progettazione e lo sviluppo IA responsabile
- Integrazione dei risultati della VISIA nella governance dello sviluppo
- Checkpoint di IA responsabile nel corso dell'intero ciclo di vita dello sviluppo

### Cosa NON copre la presente politica

- Controlli del ciclo di vita operativo (requisiti, V&V, dispiegamento, monitoraggio — trattati in AI-POL-A.6.2)
- Processi di gestione dei dati (trattati in AI-POL-A.7.2-6)
- Procedure di valutazione della conformità al Regolamento IA UE (trattate in AI-POL-A.8.2-5 e AI-POL-00)

### Quadro normativo

**Livello 1: Conformità obbligatoria** (per AI-POL-00):

- **Regolamento IA UE (Regolamento 2024/1689)**: Articolo 9 — i fornitori di IA ad alto rischio devono istituire un sistema di gestione della qualità che riguardi gli obiettivi di IA responsabile; Articolo 9(1)(b) — metodologia di progettazione e sviluppo; Articolo 10 — requisiti di addestramento, validazione e test per lo sviluppo responsabile

**Livello 2: Condizionale** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controlli A.6.1.2, A.6.1.3 — applicabile se la certificazione AIMS rientra nell'ambito o è richiesta contrattualmente

**Livello 3: Informativo** (per AI-POL-00):

- NIST AI RMF: GOVERN 4.x — pratiche di sviluppo IA organizzative; MAP 2.x — identificazione dell'impatto nello sviluppo
- ISO/IEC 23894:2023: Considerazioni sulla gestione dei rischi durante lo sviluppo IA

---

## Dichiarazioni di politica: Obiettivi per lo sviluppo responsabile (A.6.1.2)

### Requisito degli obiettivi per lo sviluppo responsabile

L'[Organizzazione] DEVE identificare e documentare obiettivi per lo sviluppo responsabile di ciascun sistema IA. Questi obiettivi devono:

- Essere stabiliti prima dell'inizio dello sviluppo (non retroattivamente)
- Riflettere i principi di IA responsabile nella Politica IA (AI-POL-A.2.2-4)
- Essere informati dai risultati della VISIA per il sistema IA (AI-POL-A.5.2-5)
- Essere integrati nel ciclo di vita dello sviluppo come criteri di progettazione misurabili, non come dichiarazioni aspirazionali
- Essere approvati dal RGIA prima dell'inizio dello sviluppo

### Proprietà fondamentali dello sviluppo responsabile

Le seguenti proprietà di IA responsabile devono essere considerate come obiettivi per ogni sistema IA sviluppato dall'[Organizzazione]. L'applicabilità e il livello di attuazione sono determinati dalla classificazione d'impatto della VISIA (Basso / Medio / Alto):

**Equità e non discriminazione**

Il sistema IA deve trattare individui e gruppi in modo equo. Gli obiettivi devono specificare:

- Quali gruppi demografici o caratteristiche protette sono rilevanti per la valutazione dell'equità
- Quali metriche di equità sono appropriate per il caso d'uso (ad es. parità demografica, equalised odds, parità predittiva)
- Soglie accettabili per le metriche di equità prima del dispiegamento — le soglie sono definite dal RGIA in consultazione con il DT e la pertinente expertise di dominio, documentate nella VISIA e approvate prima dell'inizio della V&V
- Processo di monitoraggio dell'equità in produzione (A.6.2.6)

**Trasparenza e spiegabilità**

Gli output del sistema IA devono essere interpretabili nella misura necessaria per la supervisione umana e la comunicazione con le persone interessate. Gli obiettivi devono specificare:

- Livello richiesto di spiegabilità (importanza delle feature, giustificazione delle decisioni, spiegazioni locali) in base al caso d'uso e alla classificazione d'impatto
- Pubblico di riferimento per le spiegazioni (operatori interni, persone interessate, autorità di regolamentazione)
- Documentazione dei limiti del modello e delle condizioni in cui gli output potrebbero non essere affidabili

**Robustezza e sicurezza**

Il sistema IA deve funzionare in modo affidabile nelle sue condizioni operative documentate e fallire in modo sicuro quando le condizioni sono al di fuori del perimetro operativo definito. Gli obiettivi devono specificare:

- Condizioni operative definite e requisiti di rilevamento out-of-distribution
- Requisiti di robustezza adversarial (quando il sistema IA potrebbe essere un bersaglio)
- Modi di guasto accettabili e comportamento fail-safe
- Copertura di test per casi limite e input adversarial

**Privacy by Design**

Il sistema IA deve elaborare i dati personali in modo minimale e per progettazione, non come aggiunta successiva. Gli obiettivi devono specificare:

- Requisiti di minimizzazione dei dati per i dati di addestramento e operativi
- Requisiti di anonimizzazione o pseudonimizzazione
- Requisiti del RGPD Articolo 25 (protezione dei dati fin dalla progettazione e per impostazione predefinita) ove applicabile
- Riferimento incrociato agli obblighi PRIV-POL-00

**Supervisione umana**

La progettazione del sistema IA deve sostenere, e non compromettere, una significativa supervisione umana. Gli obiettivi devono specificare:

- Punti di controllo della supervisione umana richiesti prima che le decisioni guidate dall'IA influenzino le persone
- Meccanismi di override — capacità per gli esseri umani di ignorare gli output dell'IA
- Requisiti di registrazione e traccia di audit per supportare la supervisione umana
- Meccanismi di allerta per comportamenti anomali del sistema IA

**Responsabilità**

Una chiara responsabilità umana per il comportamento del sistema IA deve essere mantenuta. Gli obiettivi devono specificare:

- Responsabile rischi IA nominato e responsabile del sistema IA (AI-POL-A.3.2-3)
- Percorso di escalation per gli incidenti IA
- Requisiti della traccia di audit che collegano gli output IA alla versione del sistema che li ha prodotti

### Documentazione degli obiettivi per lo sviluppo responsabile

Gli obiettivi per lo sviluppo responsabile devono essere documentati in un **Registro degli obiettivi di sviluppo del sistema IA** per ciascun sistema IA, firmato da:

- RGIA (approvazione della governance IA responsabile)
- Responsabile rischi IA (accettazione del rischio)
- DT / Responsabile IA Engineering (conferma della fattibilità tecnica)

Il registro deve essere aggiornato se il risultato della VISIA cambia in modo significativo.

---

## Dichiarazioni di politica: Processi per la progettazione e lo sviluppo IA responsabile (A.6.1.3)

### Requisito di definizione dei processi

L'[Organizzazione] DEVE definire e documentare i processi specifici per la progettazione e lo sviluppo responsabile di ciascun sistema IA. Questi processi devono operazionalizzare gli obiettivi per lo sviluppo responsabile definiti ai sensi di A.6.1.2.

### Processi di sviluppo responsabile richiesti

**1. Revisione della progettazione IA responsabile**

Prima dell'inizio dello sviluppo, un processo di revisione della progettazione deve validare che:

- L'architettura proposta del sistema IA supporti gli obiettivi documentati di IA responsabile
- Le considerazioni di equità, spiegabilità e privacy by design siano integrate nella progettazione, non aggiunte a posteriori
- L'uso previsto sia chiaramente specificato e i controlli di limitazione dell'ambito siano progettati sin dall'inizio

La revisione della progettazione deve essere documentata, con approvazione del RGIA.

**2. Processo di valutazione dei bias e dell'equità**

Per i sistemi IA con classificazione d'impatto Medio o Alto (per AI-POL-A.5.2-5), il processo di sviluppo deve includere:

- Pre-sviluppo: Valutazione della rappresentatività del dataset — i dati di addestramento rappresentano la popolazione di dispiegamento?
- Sviluppo: Selezione e addestramento del modello con attenzione all'equità — quali vincoli o obiettivi di equità sono integrati?
- Pre-dispiegamento: Valutazione dell'equità rispetto alle metriche e alle soglie approvate
- Post-dispiegamento: Monitoraggio continuo dell'equità (A.6.2.6)

Il processo di valutazione dei bias deve essere documentato per ciascun sistema IA con conservazione delle prove.

**3. Checkpoint per lo sviluppo IA responsabile**

Il processo di sviluppo deve includere checkpoint definiti in cui i criteri di IA responsabile vengono valutati prima di procedere alla fase successiva:

| Checkpoint | Fase | Cosa viene verificato |
|-----------|------|----------------------|
| Approvazione della progettazione | Prima dell'inizio dello sviluppo | Obiettivi di IA responsabile documentati; VISIA completata; fonti di dati approvate |
| Gate di qualità dei dati | Prima dell'addestramento del modello | Rappresentatività dei dati, criteri di qualità soddisfatti; provenienza documentata |
| Revisione dello sviluppo | Durante lo sviluppo attivo | Controlli di equità, spiegabilità e privacy implementati come progettato |
| Revisione pre-validazione | Prima della V&V (A.6.2.4) | Documentazione del modello completa; criteri di test definiti inclusi i criteri di IA responsabile |
| Approvazione pre-dispiegamento | Prima del dispiegamento (A.6.2.5) | Tutti gli obiettivi di IA responsabile valutati; VISIA aggiornata; meccanismi di supervisione umana implementati |

Ogni checkpoint deve produrre un risultato documentato. Un sistema che non supera un checkpoint di IA responsabile non può procedere alla fase successiva fino alla risoluzione dei problemi.

**4. Processo di documentazione dell'IA responsabile**

Nel corso dell'intero sviluppo, deve essere mantenuta la seguente documentazione:

- **Model card**: Uso previsto, descrizione dei dati di addestramento, risultati della valutazione incluse le metriche di equità, limitazioni note, usi non rientranti nell'ambito
- **Data card**: Descrizione del dataset, metodologia di raccolta, valutazione della rappresentatività, analisi dei bias
- **Registro dei criteri di IA responsabile**: Come ciascun obiettivo di IA responsabile è stato affrontato nella progettazione e nello sviluppo

---

## Ruoli e responsabilità

| Ruolo | Responsabilità |
|-------|----------------|
| **RGIA** | Approvazione degli obiettivi per lo sviluppo responsabile; approvazione della revisione della progettazione; conduzione o commissione delle revisioni dei checkpoint di IA responsabile; gestione dei registri degli obiettivi |
| **DT / Responsabile IA Engineering** | Guida delle revisioni della progettazione IA responsabile; garanzia che il processo di sviluppo includa i checkpoint; garanzia che i team di engineering siano formati nelle pratiche di IA responsabile |
| **Proprietario del sistema IA** | Manutenzione del registro degli obiettivi di sviluppo responsabile; garanzia della completezza della documentazione dei checkpoint |
| **Data Scientist / Ingegneri ML** | Applicazione di tecniche attente all'equità; conduzione delle valutazioni di rappresentatività dei dataset; documentazione di model card e data card |
| **Responsabile rischi IA** | Accettazione del rischio residuo di IA responsabile; escalation quando gli obiettivi non possono essere raggiunti |

---

## Requisiti probatori

| Evidenza | Descrizione | Conservazione |
|----------|-------------|---------------|
| Registro degli obiettivi di sviluppo | Documento per sistema IA degli obiettivi di IA responsabile con approvazione | Durata del sistema + 3 anni |
| Registri di revisione della progettazione | Documentazione delle revisioni della progettazione IA responsabile con i risultati | Durata del sistema + 3 anni |
| Registri dei checkpoint | Prove di ciascun checkpoint di IA responsabile con risultato superato/non superato | Durata del sistema + 3 anni |
| Model card | Documentazione del modello inclusa la valutazione dell'equità e le limitazioni | Durata del sistema + 3 anni |
| Data card | Documentazione del dataset incluse rappresentatività e analisi dei bias | Durata di utilizzo dei dati + 3 anni |

---

## Considerazioni per l'audit

Gli auditor che verificano la conformità con A.6.1.2–A.6.1.3 dovranno trovare:

- Obiettivi documentati per lo sviluppo responsabile per ciascun sistema IA, precedenti allo sviluppo
- Prove che gli obiettivi siano stati informati dai risultati della VISIA
- Processo di sviluppo definito con checkpoint di IA responsabile
- Registri dei checkpoint che dimostrino che i criteri di IA responsabile sono stati valutati prima delle transizioni di fase
- Model card e data card come artefatti di output del processo di sviluppo

---

<!-- QA_VERIFIED: 2026-04-15 -->
